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
<img src="https://cdn4.telesco.pe/file/FLqrrkH7dfYZnlFJ_0DR1tfCWC2Ylq_8ogAXJieR_QKRaIZdAb4pkAfMlNvMIZ2-JmAkPWK3Vb0pQu0cKG8_QEL3cE7F1I3k11NA1acX0ZIEPtGqcjNeHx8qwtdgs-kmnEY9wfpKSjF81KC8rPbUgHyz5edwXhxm9-cutXavYU2HSLMODpjrzBhrrV7Q9jp6QDXSXm-Gr_Ht08ZFJy5ijmi-GquDd7IqsV8hSWtFoHP8MnlLm5wpGL_VjeZ0vegLQ8W-HEAB1IyozVrjlPCfUJCsPxGC7ZSBhwZdKAjizXI100yge9WQBp0dhCuJdLTJCpJGWu59CQRtTWLlPqkTCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 495K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال ۱۲ اسرائیل به نقل از یک مقام ارشد گزارش داد که اسرائیل تا پیش از برگزاری انتخابات، هیچ حمله‌ای به ایران انجام نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/25374" target="_blank">📅 21:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5697d70b60.mp4?token=gFpwljJXQZhZ0K6QR3PXBcMeoOvT5Qya4wyOCBNEPR9JRznr4mFcnJ2LeOKOOQ-13cVzeRQ8AQwLQaXzkwCosSpGzbbGfntKyBQwH2dYQo28oVlSJ1XjwtzsjCpoI4wBFRQ8yTxCHqcy0335y9-NUOdz0a_B8Sb44Jzyk0TKsrlxPiZxwNNr5Uw984Jrg5mPQnzOcXQceztCP4clmE8_xaMdntt7UTfER6g3UXsnmxZEn8R9YJbyCF_p1VNQaKk1y4z7tDSL22TrnONOybHicfiA-umusVX98ct-SIzujlZXL_XAxEaff5LvEpSPzY9irCuyI0P-53QHqbNE4QKtDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5697d70b60.mp4?token=gFpwljJXQZhZ0K6QR3PXBcMeoOvT5Qya4wyOCBNEPR9JRznr4mFcnJ2LeOKOOQ-13cVzeRQ8AQwLQaXzkwCosSpGzbbGfntKyBQwH2dYQo28oVlSJ1XjwtzsjCpoI4wBFRQ8yTxCHqcy0335y9-NUOdz0a_B8Sb44Jzyk0TKsrlxPiZxwNNr5Uw984Jrg5mPQnzOcXQceztCP4clmE8_xaMdntt7UTfER6g3UXsnmxZEn8R9YJbyCF_p1VNQaKk1y4z7tDSL22TrnONOybHicfiA-umusVX98ct-SIzujlZXL_XAxEaff5LvEpSPzY9irCuyI0P-53QHqbNE4QKtDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: شما گفته بودید که قبل از انتخابات میان‌دوره‌ای به ایران حمله نخواهید کرد. آیا این حمله اخیر در عربستان سعودی این موضوع را تغییر داد؟
ترامپ: ما این موضوع را بررسی خواهیم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/withyashar/25373" target="_blank">📅 20:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cbf3c2b2.mp4?token=BNndhOPKF4j4yKLUVIFi-5iLB_norJ6Qkqa4ryCAicoQ3OOnzKpCNxqhtsVJqKSmaPFszMy1NO4ib24IjXam3fEogfF5JXi8-INURMDjECsc-QYeOSFon9XA8HYd4xVz4usKRJ5oUunNdKEmIaRiE9eNS0OIZCz1K0Ci-CNdp0fnbfIj9hL8ttmdN_IhX1kOMYafQDPSGIOHY50XEdQ_PQtJUWGuS9Kk8GzKZ2hL86W5XekPjrN34PWzHoPKk-IICdq_c5Rx65qyriZGCSQD6Pu7IiELCqRt7wYBLYJ3HOYup6U6YdfP1EPCuvUkDD-LyBPmBHgavyk1IzZvSOlqPLVZz9zx7x4EppdwfUm9CpwQfNcwbAQb4j7enPwsRz9xiYtVAIyjUbMwC6R3rgtut7KUwKfX_10e3jkATi3t_7NHM8hsNuh9nJizdfWUe_10iaHY32ossMruqhIK-pIiTbGELnRBqs5h13qdiuNnHXqVqqrdp_s08WPPwjq8UUWFR23v2fcRfs3zGt9I8KY2XeQ5XvDp-nG0uNSRDRDoNs33xEhWFYud0aXY34ok18mOAP7iIxmBxIfHncryhqswSQ44bjb6dzJ4YUZdl_6nPyhTde0WARL9FYVs1uFy5MJSUTQx0VFuJSNG9alBJn1LpmMo2G5CK1EExtc2LYg-OIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cbf3c2b2.mp4?token=BNndhOPKF4j4yKLUVIFi-5iLB_norJ6Qkqa4ryCAicoQ3OOnzKpCNxqhtsVJqKSmaPFszMy1NO4ib24IjXam3fEogfF5JXi8-INURMDjECsc-QYeOSFon9XA8HYd4xVz4usKRJ5oUunNdKEmIaRiE9eNS0OIZCz1K0Ci-CNdp0fnbfIj9hL8ttmdN_IhX1kOMYafQDPSGIOHY50XEdQ_PQtJUWGuS9Kk8GzKZ2hL86W5XekPjrN34PWzHoPKk-IICdq_c5Rx65qyriZGCSQD6Pu7IiELCqRt7wYBLYJ3HOYup6U6YdfP1EPCuvUkDD-LyBPmBHgavyk1IzZvSOlqPLVZz9zx7x4EppdwfUm9CpwQfNcwbAQb4j7enPwsRz9xiYtVAIyjUbMwC6R3rgtut7KUwKfX_10e3jkATi3t_7NHM8hsNuh9nJizdfWUe_10iaHY32ossMruqhIK-pIiTbGELnRBqs5h13qdiuNnHXqVqqrdp_s08WPPwjq8UUWFR23v2fcRfs3zGt9I8KY2XeQ5XvDp-nG0uNSRDRDoNs33xEhWFYud0aXY34ok18mOAP7iIxmBxIfHncryhqswSQ44bjb6dzJ4YUZdl_6nPyhTde0WARL9FYVs1uFy5MJSUTQx0VFuJSNG9alBJn1LpmMo2G5CK1EExtc2LYg-OIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: من جلوی چین و تایوان را گرفتم، اما جایزه نوبل را به کسی دادند که هیچ‌کس تا به حال اسمش را هم نشنیده بود. فکر می‌کنم او به‌شدت ضداسرائیل است. با این حال، جایزه نوبل را به او دادند. به نظرم یک جای کار در نروژ می‌لنگد.
@WarRoom</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/withyashar/25372" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5bf39d5eb.mp4?token=Q8TUc3_aDf4oDy5Op21KjpC0FNRUC_aQmX1vP_NCo0xs8HS8rXkzqlnqCZEg0WKWCMevxEDm1vKwttjRNb9BlAUVkjgZIXlmfOOJe39BqBXcC5vKf5Y7o5H7oZzpycNsRTRka1x9a489W885V1ujS_pL9hIoe5CGR1Co858I7QzRfGxWM6fI3hTSAv_ys8W0EG0F7d_-KBH1jcJPQwZLxYtFEgYTLAgz9Gz9uPniAce1R113xrt_N7vVDcZ7TRPhTPbOn6fF_L1sIXej-bB3nkLDr7I_3OsO7S-9NTGGGYRmZiKJgED32ymv9KWAov4Q8dd_Wa6V_ggk0aBBeqHCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5bf39d5eb.mp4?token=Q8TUc3_aDf4oDy5Op21KjpC0FNRUC_aQmX1vP_NCo0xs8HS8rXkzqlnqCZEg0WKWCMevxEDm1vKwttjRNb9BlAUVkjgZIXlmfOOJe39BqBXcC5vKf5Y7o5H7oZzpycNsRTRka1x9a489W885V1ujS_pL9hIoe5CGR1Co858I7QzRfGxWM6fI3hTSAv_ys8W0EG0F7d_-KBH1jcJPQwZLxYtFEgYTLAgz9Gz9uPniAce1R113xrt_N7vVDcZ7TRPhTPbOn6fF_L1sIXej-bB3nkLDr7I_3OsO7S-9NTGGGYRmZiKJgED32ymv9KWAov4Q8dd_Wa6V_ggk0aBBeqHCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: متعهد هستید که نتیجه انتخابات میان‌دوره‌ای را، فارغ از اینکه کدام حزب پیروز شود، بپذیرید؟
ترامپ: البته که می‌پذیرم. اما نمی‌خواهیم تقلبی صورت بگیرد.
خبرنگار: پس اگر جمهوری‌خواهان شکست بخورند…
ترامپ: نمی‌خواهیم تقلبی صورت بگیرد. متوجه منظورم هستید؟
@WarRoom</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/withyashar/25371" target="_blank">📅 20:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: در جریان حمله به فرودگاه ریاض قرار گرفتم و تصمیم خواهم گرفت؛ شاید به حملات عربستان به یمن بپیوندیم
@WarRoom</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/withyashar/25370" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: زلنسکی بارها می‌توانست جنگ اوکراین را پایان دهد، اما نخواست , زمان آن رسیده که اوکراین رئیس‌جمهور جدیدی داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/withyashar/25369" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6ed719e9.mp4?token=np4c3nkrRH85moO-qKMXkQ6TxnLBCLYx922yF7MBkJ8-Qv_TctilqkmouwvMC2MH-JPAsRwZfu9nlpHGOUTU6fO0PWDXFa3y3CF2U3xlW6GquCGId6HZ1z_HvzTG--witxr_UCBWUab9pbbmXrjGMwCZt6Y2pqMCsQGAzGR1YiLNNVypcRQGPvvgeevDr3SoFVFZyGYOzkknyWDoXyV792anEy4e2i10JmbRzgEBV7OD3LYPteOvUHdxESu-3WKS-O64oHkPmPqlP3vP9gPcVhzgKTxlBIAv5SEhkOUoUCEyt1I5I0zNq7std2SxP0-Zl9rpOjqQ5HeFW-GZIsiMACLduAzbBhV5N7a2N-eNb2FLZdug004V2zOIIH6x2UT851pEBemwsSyyHNsSGiXakh3f8z5UiX6SCTgsFsoiDFNf4W9cbDUTzh3sYoQctMYEaei8TtaEZCr6JKc47JmV3aMSx1v9jmGnBPeJuTHClcnbDejGSE__SKnOITbpGV-p8VxojzmyLoaSpuOZUY2KVuzcEa9JXHpUehbRwa7VvjI2khGkn0ziWDk0064xFop6yxWXp-q6mmpCmOce7HPz2sAuRrn-gt4BunZN92Z4CZoHnJFBULjw0sxuDySeWn45Ef9AAHj0U4iIOJB3-47o46rab2RGa6a9IiyhbnNEMYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6ed719e9.mp4?token=np4c3nkrRH85moO-qKMXkQ6TxnLBCLYx922yF7MBkJ8-Qv_TctilqkmouwvMC2MH-JPAsRwZfu9nlpHGOUTU6fO0PWDXFa3y3CF2U3xlW6GquCGId6HZ1z_HvzTG--witxr_UCBWUab9pbbmXrjGMwCZt6Y2pqMCsQGAzGR1YiLNNVypcRQGPvvgeevDr3SoFVFZyGYOzkknyWDoXyV792anEy4e2i10JmbRzgEBV7OD3LYPteOvUHdxESu-3WKS-O64oHkPmPqlP3vP9gPcVhzgKTxlBIAv5SEhkOUoUCEyt1I5I0zNq7std2SxP0-Zl9rpOjqQ5HeFW-GZIsiMACLduAzbBhV5N7a2N-eNb2FLZdug004V2zOIIH6x2UT851pEBemwsSyyHNsSGiXakh3f8z5UiX6SCTgsFsoiDFNf4W9cbDUTzh3sYoQctMYEaei8TtaEZCr6JKc47JmV3aMSx1v9jmGnBPeJuTHClcnbDejGSE__SKnOITbpGV-p8VxojzmyLoaSpuOZUY2KVuzcEa9JXHpUehbRwa7VvjI2khGkn0ziWDk0064xFop6yxWXp-q6mmpCmOce7HPz2sAuRrn-gt4BunZN92Z4CZoHnJFBULjw0sxuDySeWn45Ef9AAHj0U4iIOJB3-47o46rab2RGa6a9IiyhbnNEMYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی‌های متعدد در ایری، پنسیلوانیا. به نظر می‌رسد که این یک مسئله خانگی باشد. تیم ضربت به خانه رفت و احتمالاً 9 نفر از جمله 2 کودک جان خود را از دست داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/25368" target="_blank">📅 19:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانال ۱۴ اسرائیل : سفیر عربستان در یمن مدعی شد تنگه راهبردی باب‌المندب از بقایای نیروهای حوثی پاک‌سازی شده است. محمد آل‌جابر این اظهارات را در شرایطی مطرح کرده که طبق این گزارش، نیروهای ترکیه و پاکستان نیز به‌تازگی مستقر شده‌اند تا از نیروهای یمنی مورد حمایت…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/25367" target="_blank">📅 19:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏یزدانیان، معاون توسعه شبکه ملی اطلاعات وزارت ارتباطات: در صورت وقوع مجدد جنگ یا ناآرامی، احتمال قطع اینترنت وجود دارد. تفاوت احتمالی این دوره می‌تواند این باشد که اگر قرار بر اعمال قطعی یا محدودیت در دسترسی به اینترنت باشد، بر اساس آنچه رییس‌جمهور مطرح کرده است، نقش وی در این زمینه پررنگ‌تر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/25366" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حادثه‌ای با شماری تلفات در فرودگاه بین‌المللی ملک خالد در ریاض، عربستان سعودی، رخ داد. به گفته چندین شاهد عینی، آمبولانس‌های متعددی با شتاب به محل حادثه اعزام شدند و افراد از فرودگاه تخلیه گردیدند؛ همچنین گزارش‌هایی مبنی بر مشاهده «خون در همه جای» ترمینال…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/25365" target="_blank">📅 19:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25364">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانال ۱۴ اسرائیل : سفیر عربستان در یمن مدعی شد تنگه راهبردی باب‌المندب از بقایای نیروهای حوثی پاک‌سازی شده است. محمد آل‌جابر این اظهارات را در شرایطی مطرح کرده که طبق این گزارش، نیروهای ترکیه و پاکستان نیز به‌تازگی مستقر شده‌اند تا از نیروهای یمنی مورد حمایت عربستان در عملیات علیه حوثی‌ها پشتیبانی کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/25364" target="_blank">📅 19:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لاکهید مارتین از رهگیر موشکی جدید PAC-3 Edge رونمایی کرد. آزمایش این سامانه قرار است از سال آینده آغاز شود و استقرار آن برای سال ۲۰۳۱ برنامه‌ریزی شده است. این رهگیر نسخه ارتقایافته PAC-3 MSE است که برای رهگیری اهداف در ارتفاع و برد بیشتر طراحی شده و مقابله با موشک‌های هایپرسونیک (فراصوت) را نیز هدف قرار می‌دهد. PAC-3 Edge همچنین به جست‌وجوگر جدیدی مجهز است که با افزایش مانورپذیری، دقت رهگیری را بهبود می‌بخشد.
@WarRoom</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/25363" target="_blank">📅 19:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">روزنامه اسرائیلی معاریو: آمریکا از اسرائیل خواسته بود پیش از انتخابات میان‌دوره‌ای آمریکا، به‌تنهایی و بدون مشارکت نظامی واشنگتن به ایران حمله کند تا مسئولیت سیاسی و پیامدهای احتمالی این حمله متوجه دولت ترامپ نباشد. به گزارش معاریو، واشنگتن تصور می‌کرد اسرائیل…</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/25362" target="_blank">📅 19:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcJus9ezbGyK2cowcj09gvOdbxVF1X4qEOP1ejDrGZfUdGHl72V7cGvXL98OBpV_VZ7mDkGQCijX7qHaion8AVxE1PtySZc0g7bmMsFKy1H2dOY3nTFTN_IcyzryXUBYYQQCJvFoKVGVEp3ZFQigUFFmB-TgCV8y9bL_ZL2lC68nto16mo6QgKzodYxiZHac0jj8p-1I1-_FD8y5UhrGIIEhutSkDt5YSAOtfcY8Q6foGttCVsfSypM96WCNhTgI-zouc7y_kKHT0G-kL8NfxvcpCOhIGlumCCzaQfaTeNm7mJE1dAK6UlzRR3ZPMIsVzDYQayWviDSKgjEuN-ypFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/731112f8da.mp4?token=g5DzxEe0F2R_pfKekzGsfcLXloEapB-y4RgGslWvLIRSj60DLTW4j6mtNa7JCtitixHgwdA6zMDDAXCDZYA8TChwFILan1og1wy21plg2H4jOREbcRJuKhqdBGyoTXSzLjt4z3DxJrvW-TnOxf26PmzSNAtYjTM6kY9lClXaXQPgFK0Ht1ze4f27YSGoqjlntpAQvBkTsz6wIPkJ3bk8RB7ghSOw37iVozFeMN6pf0Y44mg54UTTISpmi94uinrjddfm6AGyHq3Tsrp29hNGbWtq5nEBMZji5vUoJN8aJd-WJJckBupWU9imoUlInWwju1Ei3N0_dPT9h3TE0zLioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/731112f8da.mp4?token=g5DzxEe0F2R_pfKekzGsfcLXloEapB-y4RgGslWvLIRSj60DLTW4j6mtNa7JCtitixHgwdA6zMDDAXCDZYA8TChwFILan1og1wy21plg2H4jOREbcRJuKhqdBGyoTXSzLjt4z3DxJrvW-TnOxf26PmzSNAtYjTM6kY9lClXaXQPgFK0Ht1ze4f27YSGoqjlntpAQvBkTsz6wIPkJ3bk8RB7ghSOw37iVozFeMN6pf0Y44mg54UTTISpmi94uinrjddfm6AGyHq3Tsrp29hNGbWtq5nEBMZji5vUoJN8aJd-WJJckBupWU9imoUlInWwju1Ei3N0_dPT9h3TE0zLioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادثه‌ای با شماری تلفات در فرودگاه بین‌المللی ملک خالد در ریاض، عربستان سعودی، رخ داد.
به گفته چندین شاهد عینی، آمبولانس‌های متعددی با شتاب به محل حادثه اعزام شدند و افراد از فرودگاه تخلیه گردیدند؛ همچنین گزارش‌هایی مبنی بر مشاهده «خون در همه جای» ترمینال ۳ منتشر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/25358" target="_blank">📅 18:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIYJOxC5Of3WGi8KLOy1WjDyvO6EY6zkxq5r90VvzsxgcXuTHLl3BuLjNC5Yc5puZAmnwA5jbmu8Op_PTBqwsoGPEgm9fDrjEVzRbgRK36cq21QTscQlw2lJwhL0nViuorHpikdzvmM3s-1MlwXQZqfiInheijWDQr9T1nvvw0ZuxKQCKPW8ynbY7VM-PzEXK1ClSBkNO8MBRczaYEVp0LerkHY5M6BKcuiL5qFVOZGgO3cnER8bnIyjBPoPGSMNVQZiMmckchQdt9UCnW_olmjWD8A-4h-PP-z3ZRrIgv-9c_SaSzXFDP3udEG-UH5YVCbSlk3FAiQ2NMfxdYXCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب اتاق جنگ : فیک نیوز های دزد تلگرام یک عکس‌مربوط به خبر ۱۷ اسفند ۱۴۰۴ را قسمت بالایش را بریدند و پایین را به عنوان کیل لیست جدید اسرائیل معرفی کرده‌اند که جو بدن! فاکس نیوز در این گزارش قدیمی میگفت چندین مقام ارشد در جریان عملیات مشترک آمریکا و اسرائیل هدف قرار گرفته‌اند. این فهرست همچنین مشخص می‌کند کدام چهره‌ها همچنان فعال هست نه یک لیست جدید و نهایی
@WarRoom</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/25357" target="_blank">📅 18:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e05301f48d.mp4?token=WxcD_4sHbZFtvhworq7FBEGmdhwUgKhA8zbSACpYfuD_72wsNlHga07rIWS-FdstNM_DrFBAl8LMn9_gA3oqtNwUoDadTRsrmRh3ym29rxSI7PKBsSqZL3uHFsjVaqu7IFLCM3Emeuz_BneLyuAVS--quqZw6a9JU2KbDwI9XZ1vuTg9bDRSM4B9WqAMLkiAhMzN12cw78z0XUU8EVLGi0G1LZb4LxiCOOola4HF1FilI_cYtJA6greqZv7itkj1AQR-0xNb9gJuyOwkHciMpE4o5eY585BfF30bvPHmcKFx3wJ-MPmjGKRb29SZKVVCNMxUHPUoLSLH9SphuaFGmYHl9yUmfVPpQrR7q8Qh64bK2Qo02Z-vcT0ebIcPVB27xe4G2r5nZkeuAkd5c2ldGjAt5XiGc0PNH66wEDbUTRupyVKRMR1j2_RU76kRtBHhKy-HZYRBEstbqpjoWshk60Jmup1iQ6iho-w-t736Z74V22COCsOQuq8qJd32ioc8WVMVNXiOG9RmOA9N80XNY1B-EqMUqyWXsRrMaX065MKJkFWHt1J2Ow4NaYefRSUF8ZlWQ38UZluYcZQX9YguINbeOmwz2EAzqIuQQ2Nw3fjJBemrY9L4lPnQeGfAftd9o-dOTzBbLPAuAjZzZX_Xcpykr1-1aMfVxEGBzbLMqgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e05301f48d.mp4?token=WxcD_4sHbZFtvhworq7FBEGmdhwUgKhA8zbSACpYfuD_72wsNlHga07rIWS-FdstNM_DrFBAl8LMn9_gA3oqtNwUoDadTRsrmRh3ym29rxSI7PKBsSqZL3uHFsjVaqu7IFLCM3Emeuz_BneLyuAVS--quqZw6a9JU2KbDwI9XZ1vuTg9bDRSM4B9WqAMLkiAhMzN12cw78z0XUU8EVLGi0G1LZb4LxiCOOola4HF1FilI_cYtJA6greqZv7itkj1AQR-0xNb9gJuyOwkHciMpE4o5eY585BfF30bvPHmcKFx3wJ-MPmjGKRb29SZKVVCNMxUHPUoLSLH9SphuaFGmYHl9yUmfVPpQrR7q8Qh64bK2Qo02Z-vcT0ebIcPVB27xe4G2r5nZkeuAkd5c2ldGjAt5XiGc0PNH66wEDbUTRupyVKRMR1j2_RU76kRtBHhKy-HZYRBEstbqpjoWshk60Jmup1iQ6iho-w-t736Z74V22COCsOQuq8qJd32ioc8WVMVNXiOG9RmOA9N80XNY1B-EqMUqyWXsRrMaX065MKJkFWHt1J2Ow4NaYefRSUF8ZlWQ38UZluYcZQX9YguINbeOmwz2EAzqIuQQ2Nw3fjJBemrY9L4lPnQeGfAftd9o-dOTzBbLPAuAjZzZX_Xcpykr1-1aMfVxEGBzbLMqgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاصره هوایی چه بلایی سر جمهوری اسلامی آورده است؟
خداداد کوتول سرپرست تراکتورسازی تبریز: با اتوبوس از ایران وارد عراق شدیم و الان در فرودگاه عراق هستیم که به عمان برویم ولی سگها در فردوگاه بغداد در حال تجاوز به ما هستند و سفر ما ۱۸ ساعت به عمان طول میکَشد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/25354" target="_blank">📅 18:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">المانیتور: واشنگتن از اسرائیل خواسته است برای احتمال ازسرگیری حملات به ایران آماده باشد؛ درخواستی که به گفته مقام‌های اسرائیلی غیرمنتظره بوده است. این در حالی است که ترامپ گفته آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد. در اسرائیل نگرانی وجود دارد که ترامپ یا جنگ را از سر بگیرد یا به توافقی با تهران برسد که از نظر اسرائیل برای مهار برنامه هسته‌ای ایران کافی نباشد.
@WarRoom</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/25353" target="_blank">📅 17:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">روزنامه اسرائیلی معاریو: آمریکا از اسرائیل خواسته بود پیش از انتخابات میان‌دوره‌ای آمریکا، به‌تنهایی و بدون مشارکت نظامی واشنگتن به ایران حمله کند تا مسئولیت سیاسی و پیامدهای احتمالی این حمله متوجه دولت ترامپ نباشد. به گزارش معاریو، واشنگتن تصور می‌کرد اسرائیل پیش از انتخابات خود در ۲۷ اکتبر، تمایل به حمله به ایران داشته باشد. با این حال، منابع گزارش می‌گویند موضع نتانیاهو درباره این پیشنهاد همچنان نامشخص است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/25352" target="_blank">📅 17:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/814d6e3065.mp4?token=B5VMU8uqkmMmxfZ_Gwpjhvmodaf4DShZCFg5UJSVe2q6xa6gRNEByP3VzRmy8qrfieSndIVsRGawHq5IKLqJCFr2Q_jH4zy2-YvlncOtbI5EivNxkWeNgQmWwUWhA3rp6JLObVcgXnKQMiN2jJ6lnYj8zCkKY-63LTYKxPPzbOET2xB7dBURbdnU4QLC_QBRwQaFj9uZKzbXDVxFhipEu4co0-RZTbgbIpRVRXl3ciYUixScLgTe50-eqTtRB6j2gDMWY2-dCR9mIYNMILBVnrzHDcqJYFmKXjZHbelyau9dceOV2sqZW-Nb9XrcHIkRc-zUalRNZi1dt1csSmfrlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/814d6e3065.mp4?token=B5VMU8uqkmMmxfZ_Gwpjhvmodaf4DShZCFg5UJSVe2q6xa6gRNEByP3VzRmy8qrfieSndIVsRGawHq5IKLqJCFr2Q_jH4zy2-YvlncOtbI5EivNxkWeNgQmWwUWhA3rp6JLObVcgXnKQMiN2jJ6lnYj8zCkKY-63LTYKxPPzbOET2xB7dBURbdnU4QLC_QBRwQaFj9uZKzbXDVxFhipEu4co0-RZTbgbIpRVRXl3ciYUixScLgTe50-eqTtRB6j2gDMWY2-dCR9mIYNMILBVnrzHDcqJYFmKXjZHbelyau9dceOV2sqZW-Nb9XrcHIkRc-zUalRNZi1dt1csSmfrlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ثبت‌شده توسط ماهیگیر مینابی از گشت‌زنی یک بالگرد ناشناس، احتمالاً از نوع آپاچی، در نزدیکی تنگه هرمز در صبح امروز منتشر شده است. این پرواز پس از انتشار گزارش‌هایی درباره هدف قرار گرفتن یک نفتکش در این منطقه انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25351" target="_blank">📅 16:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUDyPbKRmDp-9IxWVtRNNDUbbldnvEnfEa7ETF7dFf4OuCwEIzS6TJHle8PdaQN_oyq60xDFrMqFpc0NqbjvsRkcglPE9dLFHwRIgjswn7qDB52mi8YbOSx5otE8ibiJ9PoOk0Jhc0Sw2ds4YLI9nBxsK0sVdK1o3aYbYzKRsG-ODg83KLhBXWDiONKw0F3ccvvRDajt3sXpLKEI2ajb0h605Y41Ek1ipV-02W38TuROS9arOGi8dTPnpO7LTqU5lWtilGHxglBfOvgbfD90NtkpcWWrET5JV4ovqAypoRBsgRD5HE7kSXiW_6a49X3DCyPwOfLBbxiDfC3euARskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من به ۸ جنگ پایان دادم و به پایان دادن یا حل‌وفصل ۲ جنگ دیگر نیز نزدیک هستم. تمام گروگان‌های اسرائیلی، از جمله ۲۸ نفر آخر، چه زنده و چه جان‌باخته، را بازگرداندم. همچنین صدها گروگان از کشورهای مختلف جهان آزاد شدند و به خانه‌هایشان بازگشتند. در ونزوئلا در جنگ پیروز شدیم و دیکتاتور خشنی را که با بی‌رحمی بر آن کشور حکومت می‌کرد، دستگیر کردیم. علاوه بر این، جمهوری اسلامی ایران، بزرگ‌ترین حامی دولتی تروریسم در جهان، را از دستیابی به سلاح هسته‌ای بازداشتیم — و کارهای بسیار دیگری هم انجام دادیم! با وجود تمام این اقدامات، نه من و نه ایالات متحده آمریکا جایزه صلح نوبل را دریافت نکردیم. عجب!
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25350" target="_blank">📅 15:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پزشکیان: جایگاه فعلی زیبندۀ ما نیست
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25349" target="_blank">📅 15:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرنگار الجزیره: حمله هوایی اسرائیل به اطراف شهر طلوسه در منطقه مرجعیون در جنوب لبنان.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25348" target="_blank">📅 15:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آسوشیتدپرس گزارش داد مقام‌های ائتلاف به رهبری عربستان مدعی شده‌اند ۱۳۶ هدف نظامی در مناطق تحت کنترل حوثی‌ها را منهدم کرده‌اند. هم‌زمان، انفجارهایی در صنعا گزارش شده و سخنگوی وزارت بهداشت وابسته به حوثی‌ها گفته است حملات دو نفر از جمله یک کودک را مجروح کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25347" target="_blank">📅 15:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-c4Z0nHpd2SV-X8Grp1j_CqTHMtGBNU5eR0gFM9VGeyLqEFNmGYd6tlMoKRuyc_WOiqOIpF0Gn0i3kx-JlP88yE8rH294OdNcX_GYJIFnsWs8dvmO3kKCR1pWDxu7ysBUr8ilKB958skatJNIdk-wYFkIFa7qz32exJOn0NyyKMSeLtqsJbpet9U_GpHQY8m5uPGLSdKZr0p4UjRvVIOzG6TgToHOa-DnIFkg2JMHHR_21e4UiONe21USsZOz-8MQwSvlnmjz-Kjf9dMDDqvmKzuJVvE_Y00yxLC7G7hKxC-C6-AyGLGK7Gybyj78grFTpyN5svQclGd7TAJLrGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا:
تا سقف ۱۵ میلیون دلار پاداش برای ارائه اطلاعات درباره شبکه‌های مالی سپاه پاسداران
سپاه پاسداران انقلاب اسلامی از سازوکارهای مالی متعددی برای تأمین هزینه فعالیت‌های تروریستی خود استفاده می‌کند؛ از جمله فروش غیرقانونی نفت از طریق شرکت‌های پوششی و ناوگان سایه (کشتی‌هایی که برای پنهان کردن مبدأ، مقصد یا مالکیت محموله‌های نفتی به کار می‌روند).
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25346" target="_blank">📅 14:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جلسه خطرناک اتاق بی فکر ها : نفوذی ، سوپاپ اطمینان  ، کودن ، چپ ، هزار چهره و … در منزل محمد مهاجری @WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25345" target="_blank">📅 14:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzr4L6JOBQxQ7bp-TFyP8ew6nqwAy7UW5eywmapcN_OQKw-CK_4Yioz6RphOKcAVQ7ZQldKAFpzHaRgDR0H5gFKais2OpQrxbYwHvtL-PtfWWPOyx23OPw8lue6KY5f-KOZH39YG0rLcWC4LAM2RDw9A4UHtqW9YgXZ80J7Lzgw7MezgfLgncEP6lrHvaUE2CSBx4HubEpVIFm7B2negEKjMWVNxZCntSi_pxTy_XihigHJMC_yw3CXMlDYTXhRgJ3mlH4EqCV9pmC1pQnZdV11JTC9ZsiNZcmsPteyxMbeCWxFl3kdMck7n2BE_9NmelAEBHHbxRQxdnPIgRrnRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه خطرناک اتاق بی فکر ها : نفوذی ، سوپاپ اطمینان  ، کودن ، چپ ، هزار چهره و … در منزل محمد مهاجری
@WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25344" target="_blank">📅 13:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5467fef82.mp4?token=N7JrSX98oIhrjLNREqjEHQYT4dU-YUARK3k1xkE1N49r5WuXnsIte7UkVyMD3tPAXfsgGyITf9PT063IANBTPtwzrWfpLDDUAaVLeLWRhfht3IK_00WMPp8noNMUB0dNocCmFeZ2i5ejDb1Po_94zk-YIw4ZYragkw9ezlW7V8lqEBIB30DLReHU0OWCexguV6JUdKhU8d8plNUrkCrkWi-H3vmG75b2QjKNsfnMpaplUGu9AyKVGKcad4rE-lKOKywmo9ScgbP5HJ9QBAR3nV2FWQxcQ6NowmJ0knkdQFI9Uy-2qVlJkRr8WmRlyIwRPgwNFb20zaW4Ao66YvwMBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5467fef82.mp4?token=N7JrSX98oIhrjLNREqjEHQYT4dU-YUARK3k1xkE1N49r5WuXnsIte7UkVyMD3tPAXfsgGyITf9PT063IANBTPtwzrWfpLDDUAaVLeLWRhfht3IK_00WMPp8noNMUB0dNocCmFeZ2i5ejDb1Po_94zk-YIw4ZYragkw9ezlW7V8lqEBIB30DLReHU0OWCexguV6JUdKhU8d8plNUrkCrkWi-H3vmG75b2QjKNsfnMpaplUGu9AyKVGKcad4rE-lKOKywmo9ScgbP5HJ9QBAR3nV2FWQxcQ6NowmJ0knkdQFI9Uy-2qVlJkRr8WmRlyIwRPgwNFb20zaW4Ao66YvwMBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی رفته یه پاساژ تو محدوده سعدی تهران یه منشی رو کشته بعد هم خودشو
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25343" target="_blank">📅 12:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کرملین: ولادیمیر پوتین با هماهنگی مسعود پزشکیان، دیدگاه ایران درباره راه‌های احتمالی حل‌وفصل مناقشه را به دونالد ترامپ منتقل کرد. دیمیتری پسکوف، سخنگوی کرملین، گفت پوتین در حاشیه نشست‌های ترکمنستان دو بار با پزشکیان دیدار کرد و پیش از گفت‌وگوی تلفنی با ترامپ، او را در جریان این تماس قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25342" target="_blank">📅 12:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25341">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35bbce1ecb.mp4?token=Jt_FTOhRZ2XnEcmwF2YFaOV-4nVGSXfBw_bTzLqMdY2mvQBMNMi355KyHYCGS5fXAyqR4ISE5zRFXVUMNbDKhvvj7ZQ_uCbW2Q2doUbG3Ep5YPbjNpXD-nleu6zo944ARRm6vgL4aoOKtQi_qzhWotBFLpr1PDDwSPWibGBYi-QJ_JhgTKzw9MQavfuvCPZZtIaDKCPGrxMSvl2HKqO-UcY8iMmpR_UE1XcGtjBA9lC3yNTtz24ncPEsOPhtAnA0_Ylud7xVk4UTd4JZJFW0cImFPzUXdIfstP9CaazOasvJjyFI4IOag0D8zmeybHpqGGVf9lPZxc7ExSdPhVfoeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35bbce1ecb.mp4?token=Jt_FTOhRZ2XnEcmwF2YFaOV-4nVGSXfBw_bTzLqMdY2mvQBMNMi355KyHYCGS5fXAyqR4ISE5zRFXVUMNbDKhvvj7ZQ_uCbW2Q2doUbG3Ep5YPbjNpXD-nleu6zo944ARRm6vgL4aoOKtQi_qzhWotBFLpr1PDDwSPWibGBYi-QJ_JhgTKzw9MQavfuvCPZZtIaDKCPGrxMSvl2HKqO-UcY8iMmpR_UE1XcGtjBA9lC3yNTtz24ncPEsOPhtAnA0_Ylud7xVk4UTd4JZJFW0cImFPzUXdIfstP9CaazOasvJjyFI4IOag0D8zmeybHpqGGVf9lPZxc7ExSdPhVfoeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیک موشتبی در تجمعات دیشب ، سوژه خنده کاربران شده است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25341" target="_blank">📅 12:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c561009016.mp4?token=PXMnkdn7neLmfg1Vg0ibEewvTXKbfk3gvUMCD0UN0-uWiW5CO5xEPHVVE0C8Q_U_WkP93z3ryoQsTS9VWNT_1-iuSxaapNtp-ug8MvTNS1skcAD14Fy-depTS_mn65qBnO2a2NGx1VQUp3Fg0zrNoy7m-g1WjNptfQRD8UnFx70I6PGZxbkIyT2e0vG3OReDc8O4G3EvUvWc8edkCH8lLeQEb9ZQVfWKB4LRBWqbWgsOD6IA5vmX-qenn0ZOGqS_50TgKnuuN6OH6tkL5MFhhClnZnPrsiWyG-USBY4yu8MeedUfitaDLzzCZmOz9YYP5GiA5l7pRlUXJ3WBPjj-lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c561009016.mp4?token=PXMnkdn7neLmfg1Vg0ibEewvTXKbfk3gvUMCD0UN0-uWiW5CO5xEPHVVE0C8Q_U_WkP93z3ryoQsTS9VWNT_1-iuSxaapNtp-ug8MvTNS1skcAD14Fy-depTS_mn65qBnO2a2NGx1VQUp3Fg0zrNoy7m-g1WjNptfQRD8UnFx70I6PGZxbkIyT2e0vG3OReDc8O4G3EvUvWc8edkCH8lLeQEb9ZQVfWKB4LRBWqbWgsOD6IA5vmX-qenn0ZOGqS_50TgKnuuN6OH6tkL5MFhhClnZnPrsiWyG-USBY4yu8MeedUfitaDLzzCZmOz9YYP5GiA5l7pRlUXJ3WBPjj-lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم اکشن‌کمدی «مچ‌باکس» (Matchbox: The Movie) با بازی گلشیفته فراهانی و جان سینا و به کارگردانی سم هارگریو، دیشب از اپل تی‌وی پلاس منتشر شد. داستان فیلم درباره گروهی از دوستان قدیمی است که درگیر ماجرایی جاسوسی و پر از تعقیب‌وگریز می‌شوند. داستان فیلم بر اساس برند اسباب‌بازی خودروهای مچ‌باکس ساخته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25340" target="_blank">📅 11:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رویترز: بازارهای جهانی در پایان معاملات جمعه، ۹ اکتبر، با افزایش قیمت نفت و طلا بسته شدند. نفت برنت با رشد ۰٫۴۲ درصدی،
۱۰۴٫۷۲ دلار
در هر بشکه و نفت خام آمریکا (WTI) با افزایش ۰٫۳۹ درصدی،
۹۱٫۸۵ دلار
بسته شد. طلای نقدی با رشد حدود ۱٫۵ درصدی به
۴٬۱۹۴٫۳۶ دلار
در هر اونس رسید و قرارداد آتی طلا برای تحویل دسامبر با رشد ۱٫۴ درصدی در
۴٬۲۱۶٫۳۰ دلار
تسویه شد. نگرانی از اختلال عرضه انرژی، تنش‌های مرتبط با جنگ ایران و توقف بیش از ۷۰ درصد تولید نفت فراساحلی آمریکا در خلیج مکزیک از عوامل اثرگذار بر بازار نفت بود.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25339" target="_blank">📅 11:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آسوشیتدپرس:
سریلانکا اعلام کرده فعلاً برنامه فوری برای کمک به ۱۹ نفتکش ایرانی گرفتار در آب‌های نزدیک سواحل خود ندارد. این کشتی‌ها بنا بر گزارش، با کاهش ذخایر غذا، آب و سوخت روبه‌رو هستند و دولت سریلانکا نگرانی از تحریم‌های ثانویه آمریکا را نیز در تصمیم خود لحاظ می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25338" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25337">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f0fa0967.mp4?token=mCCtHZ2CPoDKgRPu-49rVR9bLi_dV0_KP4an6CXoyrFJ9IC4UEcfhk_Ah6hEBYiOhd4_emuCTAm76ERHlzy2kHjmYDw8OpR40oNpwZXHPY7ezCdC1UTqaCOECJHDpHxIE9zPk1jr526kh_qukUyLQxHtZX-0AaVFcmB7dTUcqqbazB1kDNu1cYjuv4TNPYPOte1ygW4KfnhbjtJqGn005i2fuiFn0hx-5uyuNrNyQlBHGSSp6gURnwVGyO6cHgY6zSo3ija06m02xzTGxhW1R3l4vbqPIPuK-1wqgFqMqyd8H0i18i8GjngvPWMRJbJMPc0WBOwsWYY7h39_3lOt3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f0fa0967.mp4?token=mCCtHZ2CPoDKgRPu-49rVR9bLi_dV0_KP4an6CXoyrFJ9IC4UEcfhk_Ah6hEBYiOhd4_emuCTAm76ERHlzy2kHjmYDw8OpR40oNpwZXHPY7ezCdC1UTqaCOECJHDpHxIE9zPk1jr526kh_qukUyLQxHtZX-0AaVFcmB7dTUcqqbazB1kDNu1cYjuv4TNPYPOte1ygW4KfnhbjtJqGn005i2fuiFn0hx-5uyuNrNyQlBHGSSp6gURnwVGyO6cHgY6zSo3ija06m02xzTGxhW1R3l4vbqPIPuK-1wqgFqMqyd8H0i18i8GjngvPWMRJbJMPc0WBOwsWYY7h39_3lOt3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما یک سال پیش با بمب‌افکن‌های «بی-۲» آن‌ها را بمباران کردیم و از آن زمان تاکنون نیز به بمباران آن‌ها ادامه داده‌ایم.
آن‌ها هرگز به سلاح هسته‌ای دست نخواهند یافت.
ما عملکرد بسیار خوبی داشته‌ایم. این ماجرا خیلی زود، به هر طریقی که باشد، پایان خواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25337" target="_blank">📅 11:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فایننشال تایمز:
حملات به نفتکش‌ها از تنگه هرمز فراتر رفته و به بخش‌های دیگر خلیج فارس گسترش یافته است. این گزارش از حمله به نفتکش ترکیه‌ای «Acers» در نزدیکی قطر و نفتکش بزرگ چینی «Gem No. 2» در نزدیکی امارات خبر می‌دهد. افزایش خطر حمل‌ونقل دریایی هزینه فعالیت نفتکش‌ها را بالا برده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25336" target="_blank">📅 11:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پنتاگون آمار تلفات نظامی آمریکا در جنگ با ایران را به‌روزرسانی کرد:
با اضافه شدن ۲ کشته و ۴ مجروح به آمار قبلی، شمار نظامیان آمریکایی کشته‌شده به ۲۱ نفر و تعداد مجروحان به ۸۶۵ نفر افزایش یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25335" target="_blank">📅 10:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">المانیتور به نقل از کریس مورفی، سناتور دموکرات ایالت کنتیکت، پس از دیدار با امیر قطر و میانجی ارشد این کشور: توافق با ایران برای پایان دادن به جنگ، در شرایط فعلی قریب‌الوقوع به نظر نمی‌رسد. مورفی همچنین ارزیابی کرده است که چارچوب توافق احتمالی احتمالاً بسیار محدود خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25334" target="_blank">📅 10:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/074cfb2840.mp4?token=nLvmY74ANNP06sb-RhIJzzmTndTCYsven7Tt_RLvu4t1UdkIiGCBJv7DF6yzeyoGnW-6THzkAXTKWfiCd5vNtM2-ScpsoKl0MZnlhbJZiagIr2dkrfxCa2ZzWYChVO6_rY2qiFYJncD2vQsF_F8Tv_u9_EejNZvMSmj2HDZg6506R5M4l6WVC6HUsEiUip3nlFIIr2hXzUYo6nt72mFLnFkDfWRs8JclAr4X1vLQmkHHa5p3GhOF_kw8spmeyy2eIucD073idzIkXRhCrEDoLC1IqBlAkgZctA7mD8sIRz5juwKLOusKZrk58yeEWxMr4jGgAipk25ZpaTzgOd83Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/074cfb2840.mp4?token=nLvmY74ANNP06sb-RhIJzzmTndTCYsven7Tt_RLvu4t1UdkIiGCBJv7DF6yzeyoGnW-6THzkAXTKWfiCd5vNtM2-ScpsoKl0MZnlhbJZiagIr2dkrfxCa2ZzWYChVO6_rY2qiFYJncD2vQsF_F8Tv_u9_EejNZvMSmj2HDZg6506R5M4l6WVC6HUsEiUip3nlFIIr2hXzUYo6nt72mFLnFkDfWRs8JclAr4X1vLQmkHHa5p3GhOF_kw8spmeyy2eIucD073idzIkXRhCrEDoLC1IqBlAkgZctA7mD8sIRz5juwKLOusKZrk58yeEWxMr4jGgAipk25ZpaTzgOd83Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: این جنگ یا از طریق نبرد پایان می‌یابد، یا آن‌ها توافق‌نامه‌ای را که ما می‌خواهیم، امضا خواهند کرد
اگر اجازه می‌دادیم آن‌ها به سلاح هسته‌ای دست پیدا کنند، شاهد سطحی از مرگ، آشوب و ویرانی می‌بودید که هرگز مانند آن را ندیده‌اید. و من جلوی آن را گرفتم
رؤسای‌جمهور قبلی باید مدت‌ها پیش از روی کار آمدن من، جلوی این اتفاق را می‌گرفتند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25333" target="_blank">📅 10:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25332">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بلومبرگ:
ایران با وجود ماه‌ها حملات آمریکا و اسرائیل، کارخانه‌های تولید موشک و پهپاد خود را حفظ کرده و همچنان توانایی بازسازی و تکمیل ذخایر تسلیحاتی‌اش را دارد. به گفته مقام‌های آگاه غربی، تهران هنوز ذخایر قابل‌توجهی از موشک‌های بالستیک و برخی تسلیحات ضدکشتی در اختیار دارد و می‌تواند به‌سرعت بر تعداد آن‌ها بیفزاید. این مقام‌ها همچنین مدعی‌اند که روسیه در حال تأمین موشک برای ایران است؛ ادعایی که وزارت دفاع روسیه به درخواست بلومبرگ درباره آن پاسخی نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25332" target="_blank">📅 10:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ : ایران یا خیلی سریع همه چیز را به ما خواهد داد، یا دیگر وجود نخواهد داشت. آن‌ها این را می‌دانند @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25331" target="_blank">📅 10:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25330">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3d0a7be4.mp4?token=fosIzmhxVD_WhfPS-hwlj1rdpE0RViEvdNgq7a22gHGxFheQmRqoO2MEFb2ZOM6rIaBmooU3i_NqXwfpWVB_HiMAaqXikYZZeeXd52tZ8aa7NNrNPFeA-bfq74bw_w8LvcXhGYK7DonAq9zKL0oHQOBEmP6vNNRYI7NpflJB3MV5D-JKsMK1u-a_MxZdotTwW8qpSUsmlBr3jiZ568P6QEaDX7tY7i3eOKJYMPAFMlkNkdRzjl2jzV64EivV89B0p8ZzCMft9BBQ3HT6timLAbh_sWqMkVcyMGBceoony_KMMY-RGHdNaKo-yVZSNhqnUnnDiQOjM6PonmlCeCoN0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3d0a7be4.mp4?token=fosIzmhxVD_WhfPS-hwlj1rdpE0RViEvdNgq7a22gHGxFheQmRqoO2MEFb2ZOM6rIaBmooU3i_NqXwfpWVB_HiMAaqXikYZZeeXd52tZ8aa7NNrNPFeA-bfq74bw_w8LvcXhGYK7DonAq9zKL0oHQOBEmP6vNNRYI7NpflJB3MV5D-JKsMK1u-a_MxZdotTwW8qpSUsmlBr3jiZ568P6QEaDX7tY7i3eOKJYMPAFMlkNkdRzjl2jzV64EivV89B0p8ZzCMft9BBQ3HT6timLAbh_sWqMkVcyMGBceoony_KMMY-RGHdNaKo-yVZSNhqnUnnDiQOjM6PonmlCeCoN0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : ایران یا خیلی سریع همه چیز را به ما خواهد داد، یا دیگر وجود نخواهد داشت. آن‌ها این را می‌دانند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25330" target="_blank">📅 10:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نیویورک‌تایمز گزارش داد کاخ سفید سمت سخنگویی را به کیتی زکریا، مفسر محافظه‌کار و مشاور ارتباطات نزدیک به دونالد ترامپ، پیشنهاد کرده است. او پیش‌تر نیز برای مدتی سخنگوی وزارت امنیت داخلی آمریکا بود. در صورت نهایی‌شدن این انتصاب، زکریا جایگزین کارولین لیویت…</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/25329" target="_blank">📅 03:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450a7d0c9a.mp4?token=WUftHVcscDgQgS57I_arjdIWyLnNlrFT_j71DQE4p4IanRLW5hMhMzSicWfURbGugwY_C07Mdu3Sva2XfvWLxiQZVc_x-iuzrUA2s3500lCS6bDuaIEg4X4amcUCHb9W3R5aOiuDGCLfXv05NK6k2-QW-cJzzEXFKHwfi11T_YVIJk8dJXagYtjGs43G7kmJZfCOfnxpaupkvb2i8SDgIMENy-ONr_9AmN8PVe5TOhnXBlH9kUWuIh2FqsSQ2QtaOT0fJtIZVAYpeheFGGyNW_aQwDq-SqrF6x7fDKXJI3OjvoB_u7HnKT9LeXPWbn0eVb9ttXyfKoMAoAODAICJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450a7d0c9a.mp4?token=WUftHVcscDgQgS57I_arjdIWyLnNlrFT_j71DQE4p4IanRLW5hMhMzSicWfURbGugwY_C07Mdu3Sva2XfvWLxiQZVc_x-iuzrUA2s3500lCS6bDuaIEg4X4amcUCHb9W3R5aOiuDGCLfXv05NK6k2-QW-cJzzEXFKHwfi11T_YVIJk8dJXagYtjGs43G7kmJZfCOfnxpaupkvb2i8SDgIMENy-ONr_9AmN8PVe5TOhnXBlH9kUWuIh2FqsSQ2QtaOT0fJtIZVAYpeheFGGyNW_aQwDq-SqrF6x7fDKXJI3OjvoB_u7HnKT9LeXPWbn0eVb9ttXyfKoMAoAODAICJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا اقدام نظامی به انتخابات میان‌دوره‌ای آمریکا گره خورده است؟ چرا همین حالا علیه ایران اقدام نمی‌کنید؟
دونالد ترامپ: ممکن است اقدام کنیم
. خواهیم دید، اما فکر می‌کنم آن‌ها به‌شدت در حال شکست خوردن هستند و کشورشان وضعیت بسیار بدی دارد. ارتش آن‌ها شکست خورده است؛ نیروی دریایی ندارند و نیروی هوایی‌شان هم از بین رفته است. تورم در ایران به ۳۰۰ درصد رسیده و این کشور در وضعیت بسیار وخیمی قرار دارد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/25328" target="_blank">📅 02:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کرملین: در جریان تماس تلفنی، نه پوتین و نه ترامپ نمی‌خواستند زودتر از دیگری تماس را قطع کنند.  @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25327" target="_blank">📅 02:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کرملین: در جریان تماس تلفنی، نه پوتین و نه ترامپ نمی‌خواستند زودتر از دیگری تماس را قطع کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/25326" target="_blank">📅 02:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25325">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">من همجا هستم
🫡
فک نکنین نمیبینم</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/25325" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تحلیل بازار
🤑
💵
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/25324" target="_blank">📅 01:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">زلنسکی به ترامپ: " دادن هدایایی به پوتین، منجر به طولانی شدن جنگ خواهد شد."
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/25323" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خوش‌قلبه تاریخ‌ندان ، مارک روبیو :  «ایران تلاش می‌کرد توان نظامی متعارف خود را آن‌قدر گسترش دهد که دیگر نتوان با آن مقابله کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25322" target="_blank">📅 01:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_V0fLU6YerLyfi2ihepQgI1e1d4dgeL2M3J0Iu-61oJXa2vvk9MYIRWjqV6ZmGUPCbAKFU_eluz0GX5VavBcRr4lARwaxvrf2xA9fRDhe3Adtcthyryi4FWU6O0Q8buoiL1xtHXZuIGyU5178d3ZMEYlNs_eX5eEICEqXf4FhYohYnmWpVLaeClSyGKTaw0azlgxsPbwcECRg1wfGtS-KM610hSC14tsc33NmH7AWoSFyq7DvGcoD3cNb66mI1Ih3L3--LGk4GywKOtlVederw6Cwm-ANUgYH8PKORcBc70ghq3QNVvDHlU9-3r-X9sZuvDW5yKlETvkc9sna1NAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب چند کپسول پیکنیکی تپل از سیریک  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/25321" target="_blank">📅 01:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">@WarRoom
زمان حمله
💥
⌛️</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25320" target="_blank">📅 01:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25319" target="_blank">📅 01:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25318" target="_blank">📅 01:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25317">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: ممکن است زودتر از حد انتظار به ایران حمله کنیم.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/25317" target="_blank">📅 01:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پرتاب چند کپسول پیکنیکی تپل از سیریک
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/25316" target="_blank">📅 01:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9893251f9d.mp4?token=NxumhaU8jDU8XEGoywjX2AZGf5BYdOhh03hywza1hmM8WA48_K-iTdD9gExAXDleUYbLMtDg_kz0g0rBbGr5nseJb1QhX5QDgUueqF4q_fGPzv94RM9nALG5XJA6cEfF37_4tGFqqp3xCf5y42gYUwGDhholNcYB5xBD6HUMsAGkHLlnus_elS-FMgcodZ4gHufz7WgUPevm9gq3JdQe0dC_LhEe0yRRTi-EEd3Z6ybK59mIQJbhdgd-GfhRSoARNv2VI9uFSICPESQNkEmV5VwkPu-hjahYsCOc8KPCthbGLlnkuqCiZUtbmTTCVr_QhL9icuV5herW3vuljLIvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9893251f9d.mp4?token=NxumhaU8jDU8XEGoywjX2AZGf5BYdOhh03hywza1hmM8WA48_K-iTdD9gExAXDleUYbLMtDg_kz0g0rBbGr5nseJb1QhX5QDgUueqF4q_fGPzv94RM9nALG5XJA6cEfF37_4tGFqqp3xCf5y42gYUwGDhholNcYB5xBD6HUMsAGkHLlnus_elS-FMgcodZ4gHufz7WgUPevm9gq3JdQe0dC_LhEe0yRRTi-EEd3Z6ybK59mIQJbhdgd-GfhRSoARNv2VI9uFSICPESQNkEmV5VwkPu-hjahYsCOc8KPCthbGLlnkuqCiZUtbmTTCVr_QhL9icuV5herW3vuljLIvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو رو دیدم حالم خوب‌شد
🫡
اول باید هوای همو داشته باشیم تا پیروز بشیم
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/25315" target="_blank">📅 01:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25314" target="_blank">📅 00:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25313">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نمیبخشم و فراموش نمیکنم
😉</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25313" target="_blank">📅 00:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaedbc2620.mp4?token=Vj-9JzokpdWor4HKGluq59ujfbq5H1s_CcyE1kySMIQzK2yySVQ7SF2y-qj2Vn6wgIAl3jZMH2lG2JT5L2XZz7lKFMK2s8_Pyx7xcVx7fwRASZzClaQWS3ofpRUcjwOdeLL9x5RwzxSjoHhFbVh2jjq_423sNdsQEPRsLe6iu-iErOKAqKdwE-EEjw5buWb-J5hJuA0qZFml4sU5O6pSETfL6uCxgfVQpAKXqXL7eyDpDQb8B5FGBnqo4OVBTwkuMLU-yX5UYE6iZ4t75_hAVwBIkthgMksWrSy1YPqycGl4-BEhtnxUQ-9J6a_o-JkLOCxgwdOReVd4wWeB-uVx-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaedbc2620.mp4?token=Vj-9JzokpdWor4HKGluq59ujfbq5H1s_CcyE1kySMIQzK2yySVQ7SF2y-qj2Vn6wgIAl3jZMH2lG2JT5L2XZz7lKFMK2s8_Pyx7xcVx7fwRASZzClaQWS3ofpRUcjwOdeLL9x5RwzxSjoHhFbVh2jjq_423sNdsQEPRsLe6iu-iErOKAqKdwE-EEjw5buWb-J5hJuA0qZFml4sU5O6pSETfL6uCxgfVQpAKXqXL7eyDpDQb8B5FGBnqo4OVBTwkuMLU-yX5UYE6iZ4t75_hAVwBIkthgMksWrSy1YPqycGl4-BEhtnxUQ-9J6a_o-JkLOCxgwdOReVd4wWeB-uVx-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته است که به‌خاطر توافق نفتی‌تان با پوتین، شما ضعیف هستید.
ترامپ: چه کسی این را گفته؟
خبرنگار: زلنسکی.
ترامپ: باشه.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/25312" target="_blank">📅 00:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25311" target="_blank">📅 00:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25310" target="_blank">📅 00:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0b707c6d.mp4?token=YIQ_rxGVnae4WQSIgQyPU3G0vCO0i3sOwntASogC8ceJVy_kRqk1PHdxdyS14a18LdplwagJahsAlRh34OI3dpX3RLYlIQHvKEqXi2KXxG4Oo4rO0TfKoAcMhioyIur0eTNfEd2cuA0hjkGqX7AK5VcJrC5D_B77KsieLPz4bcEih1hM5RhUjE4F1ljMNy77bDILbX3QM24xsnpGWklTK6r2zAf5JhX_7P_tT9BWpfAPg3-c5XdPVsJVveHVeWRyePg5FPno3yyHsLCYs6gD_asxJLMoT4TUX0_c801K72ORQEnxWMat03Oe-LnnHF2_hbvWQN5tTnRIBwXEmnThvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0b707c6d.mp4?token=YIQ_rxGVnae4WQSIgQyPU3G0vCO0i3sOwntASogC8ceJVy_kRqk1PHdxdyS14a18LdplwagJahsAlRh34OI3dpX3RLYlIQHvKEqXi2KXxG4Oo4rO0TfKoAcMhioyIur0eTNfEd2cuA0hjkGqX7AK5VcJrC5D_B77KsieLPz4bcEih1hM5RhUjE4F1ljMNy77bDILbX3QM24xsnpGWklTK6r2zAf5JhX_7P_tT9BWpfAPg3-c5XdPVsJVveHVeWRyePg5FPno3yyHsLCYs6gD_asxJLMoT4TUX0_c801K72ORQEnxWMat03Oe-LnnHF2_hbvWQN5tTnRIBwXEmnThvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در کنار مایک تایسون در کاخ سفید: امروز با او مبارزه نخواهم کرد، اما مدت‌هاست که طرفدارش هستم. ما مدت‌هاست با هم دوست هستیم. هیچ‌کس مثل او نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25309" target="_blank">📅 00:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">استوری های اینستاگرام رو عکس دار‌کردم مطلب رو بهتر بگیرین ، خیلی باحال شده دیدید ؟
instagram.com/yashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25308" target="_blank">📅 00:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017aa950d4.mp4?token=DirPQarLe_Damc3V-h0o-tsFRqrhOC8ZZrvL5GkFkFDDe_9bjjoax3drdKa6t_mbKDE5dW2nVXEBuFiEOMWfsNEl6sFzPIr3zgTin0l5B0rF-6ZsQo0MvbGhg6VlOvwI1OXhbySp9h8BqUB8NoOPFo0V56mLKbyNtwNm9C2cu3avcPl-bHBZUE_27jZzf2bf2pPKzTSS-dpVQRQBB7nAeUO3zhy3WpDpwchEMBASlO9jkdbCihVXmPpjASMF7bfmuCex7DGGUp5R6pojUNWj0zpb6vgAlv4y2sMyTBR52vLKbCp9V7cQYZzej3VB692wfchksUKcaVZxyiV5nqgzCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017aa950d4.mp4?token=DirPQarLe_Damc3V-h0o-tsFRqrhOC8ZZrvL5GkFkFDDe_9bjjoax3drdKa6t_mbKDE5dW2nVXEBuFiEOMWfsNEl6sFzPIr3zgTin0l5B0rF-6ZsQo0MvbGhg6VlOvwI1OXhbySp9h8BqUB8NoOPFo0V56mLKbyNtwNm9C2cu3avcPl-bHBZUE_27jZzf2bf2pPKzTSS-dpVQRQBB7nAeUO3zhy3WpDpwchEMBASlO9jkdbCihVXmPpjASMF7bfmuCex7DGGUp5R6pojUNWj0zpb6vgAlv4y2sMyTBR52vLKbCp9V7cQYZzej3VB692wfchksUKcaVZxyiV5nqgzCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25307" target="_blank">📅 00:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کاش زن داشتم فردا نهار کتلت درست میکرد شاید میزد
😁
یا موسی</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25306" target="_blank">📅 00:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25305">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqxjhgyPu-9SUy0ulzMJElC1tAwxlmS6TEPu_YJW1rrC2DyzLung7b89QNk9na6O-a6145O2Z_mzpwIKHev4Nhyg114ByFW0KoJp6RclEx0dxtjWtjlbVvC1jm7zD4AbGTlKZY4ANP1H7Tj96I8i8NhaLEEkofHTW4WOAwv1K2wet4R5-I_1be22tZoY8exp-VqGHHFGIstodDsO_wJENuYp-H5PIWUmL91DJpjDUPnuQuRmALjZUW4uos0qJlfZqui9pV3XIoBlFXz1mmp-o_sKxpZYQt63iQ1M8BcIXFj3I7NdabtbGr0TCWRg7mAnW5wXf8qDcLgkIs_o4qy4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه فارسی وزارت خارجه آمریکا از شهروندان این کشور خواست با توجه به شرایط امنیتی منطقه، برای لغو پروازها و بسته‌شدن حریم هوایی آماده باشند.
به هیچ دلیلی به ایران سفر نکنید و اگر شهروند آمریکایی در ایران هستید، فوراً کشور را ترک کنید.
همچنین به شهروندان آمریکایی توصیه میشود از تجمعات بزرگ دور بمانند، هشدارهای امنیتی را دنبال کنند و اطلاعات سفر خود را در سامانه STEP ثبت کنند.
شماره‌های تماس اضطراری وزارت خارجه آمریکا:
از خارج آمریکا و کانادا: ‎+1-202-501-4444
از داخل آمریکا و کانادا: ‎+1-888-407-4747
امور کنسولی شهروندان آمریکایی در ایران:
ایمیل: BernACS@state.gov
تلفن سفارت آمریکا در برن: ‎+41-31-357-7011
توجه: بخش سوئیس حافظ منافع آمریکا در تهران موقتاً تعطیل است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/25305" target="_blank">📅 23:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">علیرضا بیرانوند پس از اتفاقات روز گذشته و درگیری لفظی با مدیران باشگاه تراکتور، امروز در اردوی این تیم پیش از اعزام به عمان در هتل حاضر شد اما در اقدامی جالب مدیران باشگاه تراکتور او را از اردوی تراکتور
اخراج کردند.
@WarRoom
👃</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/25304" target="_blank">📅 23:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیویورک‌تایمز گزارش داد کاخ سفید سمت سخنگویی را به کیتی زکریا، مفسر محافظه‌کار و مشاور ارتباطات نزدیک به دونالد ترامپ، پیشنهاد کرده است. او پیش‌تر نیز برای مدتی سخنگوی وزارت امنیت داخلی آمریکا بود. در صورت نهایی‌شدن این انتصاب، زکریا جایگزین کارولین لیویت…</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/25303" target="_blank">📅 23:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ: به‌تازگی گفت‌وگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که در جریان آن توافق شد روسیه فوراً بیش از ۳۰۰ هزار تن سوخت دیزل به بازار آمریکا و بازار جهانی عرضه کند. همچنین، ۵۰۰ هزار تن دیگر در طول ماه نوامبر و یک میلیون تن دیگر بلافاصله…</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/25302" target="_blank">📅 23:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شرق هم چنان گزارش سر و صدا میاد واسم
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/25301" target="_blank">📅 23:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سلامتی همگی</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/25300" target="_blank">📅 22:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhcsMHD5mgj-pzJFeeXr4Ih4JIo4OE3aknNgxbsJ40Gk_3JPcand3NXRL-r7TMxSpxDvoXGjim8rzfxg9xzxVJ5e4c_1DqMf0c90xRmfCRk7LRuFe5lRgSW9fiv4Jxsap4TSeWLJgMogDEoAvBlQbaHnrrUJQBv_J2s85ksnPYJaWzGqTmx0HoXdKeK4CU1fH1Nx7LTtPvYwRrqmFTUpp9Y4SS5nkuMPMmZUVLsFizuZbUJCzsOsQgRHqlQKZ1bZg4LBBD9TKh4h7EFcHFYoKyvFzLzE51vIQyxafpu9tOVniHmxccvhfvoii9eg1_EK0M4NNMxvNEERjQ6gjKUXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به‌تازگی گفت‌وگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که در جریان آن توافق شد روسیه فوراً بیش از ۳۰۰ هزار تن سوخت دیزل به بازار آمریکا و بازار جهانی عرضه کند. همچنین، ۵۰۰ هزار تن دیگر در طول ماه نوامبر و یک میلیون تن دیگر بلافاصله پس از آن تحویل داده خواهد شد. علاوه بر این، با توجه به وضعیت پالایشگاه‌های دیزل روسیه، این کشور در مدت کوتاهی پس از آن، ۳ میلیون تن سوخت دیزل دیگر نیز عرضه خواهد کرد. با توجه به کنترل کامل ما بر تنگه هرمز و این خبر بزرگ درباره تأمین انرژی از روسیه، قیمت گازوئیل برای آمریکایی‌ها و در واقع برای سراسر جهان، به‌سرعت و با کاهشی بی‌سابقه پایین خواهد آمد! پایین آوردن قیمت‌ها برای مردم آمریکا، به‌ویژه کشاورزان، دامداران و رانندگان کامیون، بزرگ‌ترین اولویت من است. این خبر بسیار مهم و بزرگی است. همچنین باید روشن باشد که ایران به سلاح هسته‌ای دست پیدا نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/25299" target="_blank">📅 22:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امشب مثل اینکه من باید جنگ راه بندازم</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/25298" target="_blank">📅 22:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اتاق جنگ با یاشار : ترابری ۲۴ ساعت پیش تا همین الانه الان ! دارن پرررر میان (عرزشی هستی نبین سکته میکنی) فقط آخرش که مال همین چند ساعته یکی از‌ زیبا ترین پل های هوایی شکل میگیره @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/25297" target="_blank">📅 22:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfsvHWhH6HTrrXa1az9ToeoDnXoTOjzLpjjaJd1rBxdObBuZo-IOcby7BDVnDposkT3wi2ctnA_J9kK0YoUojfWQzIQY1zmcPpJzYcN2eGyGV12VJ67JYuuepTgTTgI8lsjtFPn2F-ncK03vuTYOd9aQu1PmN045_VflzEHzd9eSlpOXrq1SoueUes7PVvThkP4i0IK6jiT5sj2wGyBTqMK6Y91r3ldwwPdnxzNmB8-WNBryA1pRpT7IT3BwD3pl5I6GpbNuXfD2i4RItgfxCUsYoHIwtqd8CSu0AkM1zdaP-vPbbXBTnAvXxYnTwulz-RsyQqqY1t-tAN5NZph40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز گزارش داد کاخ سفید سمت سخنگویی را به
کیتی زکریا
، مفسر محافظه‌کار و مشاور ارتباطات نزدیک به دونالد ترامپ، پیشنهاد کرده است. او پیش‌تر نیز برای مدتی سخنگوی وزارت امنیت داخلی آمریکا بود. در صورت نهایی‌شدن این انتصاب، زکریا جایگزین کارولین لیویت خواهد شد که در ماه اوت از سمت خود کناره‌گیری کرد. پذیرش نهایی پیشنهاد هنوز تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/25296" target="_blank">📅 22:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خلاصه پیغام های زیاد : تهرانپارس بین فلکه دوم و سوم انفجار شدید اومد آسمون رو دود گرفته و بعد صدای تیر اندازی شنیده شد! علت نامشخص ولی حمله هوایی نیست @WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/25295" target="_blank">📅 21:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">معاون وزیر خزانه‌داری آمریکا: بیش از ۱۵۰۰ فرد و نهاد مرتبط با ایران را تحریم کرده‌ایم
وزارت خزانه‌داری آمریکا دیروز هم ، تحریم‌های تازه‌ای علیه
۱۷ کشتی مرتبط با ناوگان پنهان نفتی ایران
اعلام کرد. هم‌زمان، وزارت خارجه آمریکا نیز ۱۰ نهاد، ۶ فرد و ۵ کشتی را هدف تحریم قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/25294" target="_blank">📅 21:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGia56Mryujy1Nvyz5nSSDhbcOIxZOhgUB5spM7r-QY8o8aI-90Mr8YRqXTmgaA3SaENlK7BrfK93DSBoijP-8HU-inhRYU_Ty3jwyskP-fjzAkruz4kb4jW4upkrlzwiRXerTXZ1jEPKFhHCejJYXIaffV7BEoHMVFarZ2FDQLuUkjomQnmBr86qkKsFNIVWQWdbYXVdYGO1Cda5CHpAyWrB7oQ9Sj6TqBLXlDdLtKPdo_69icgLwIssTwjbgQ31dK6Rdn_RAR6ABfRIuofb3jyrdj2sRO1Hjr7mSwM_wjGMqs-c01rIxyccD_Kq8XKLLLqbt-Ec8AxRt8gxvV4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تا ۹ اکتبر، نیروهای آمریکایی ۱۳۳ کشتی تجاری را برای رعایت محاصره تغییر مسیر داده‌اند.
یک بالگرد نیروی دریایی آمریکا از ناوشکن موشک‌انداز «یواس‌اس جان پل جونز» برخاست؛ ناوشکنی که در پشتیبانی از محاصره دریایی آمریکا علیه ایران فعالیت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/25293" target="_blank">📅 21:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bedb14bbb5.mp4?token=aTxrfLaHQZKwcdVyRVYR92tw3N0ajW6FeVgAG4ZF68fcEk1GoZ3bFjAwNLNNGC7u9zneKSicQDt3WBaSK0DnbCatJ21Ii-6oZtTGu1qom51n2nXeATQ5KCUDGta6oGi2UtpFbwIBJivXHmjFQU5DIzbXr6QjdUwPc1hBXwggGMvPBaNl9FZie0IdOdqBQoR1nqm7EYF1Zb19eF5XlyixAKzD68hqKa6Ua8cgpjIkKUi7WhlmqCgl1hpfxtL3BogafGFDhj4a54Ji-TjFvae03zFHdLjwsT6U8RqKCRzgMtVStJv5vH3btPUi4FY1MvR8COgoGuENLBvR6rcv-Bn1Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bedb14bbb5.mp4?token=aTxrfLaHQZKwcdVyRVYR92tw3N0ajW6FeVgAG4ZF68fcEk1GoZ3bFjAwNLNNGC7u9zneKSicQDt3WBaSK0DnbCatJ21Ii-6oZtTGu1qom51n2nXeATQ5KCUDGta6oGi2UtpFbwIBJivXHmjFQU5DIzbXr6QjdUwPc1hBXwggGMvPBaNl9FZie0IdOdqBQoR1nqm7EYF1Zb19eF5XlyixAKzD68hqKa6Ua8cgpjIkKUi7WhlmqCgl1hpfxtL3BogafGFDhj4a54Ji-TjFvae03zFHdLjwsT6U8RqKCRzgMtVStJv5vH3btPUi4FY1MvR8COgoGuENLBvR6rcv-Bn1Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سنتکام : به لطف نیروهای ما  که با موفقیت مین‌های دریایی را از مسیرهای اصلی تردد پاکسازی کرده‌اند، مسیرهای عبور آزاد از تنگه هرمز برای تمامی شناورهایی که تحریم‌های دریایی آمریکا علیه ایران را نقض نمی‌کنند، باز است؛ در نتیجه، هزاران شناور تجاری با ایمنی کامل از این تنگه عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25292" target="_blank">📅 21:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سخنگوی ارتش اسرائیل: امروز جمعه، در حمله‌ای هوایی در منطقه مرزی سوریه و لبنان، یوسف علی الحسن کشته شد. به گفته ارتش اسرائیل، او با هدایت جمهوری اسلامی در حال برنامه‌ریزی حملات علیه نیروهای اسرائیلی در جنوب سوریه، از جمله با پهپادهای انفجاری و راکت، بوده است. ارتش اسرائیل مدعی شد این طرح‌ها خنثی شده‌اند و اعلام کرد به اقدام برای رفع تهدیدها ادامه می‌دهد و به توافق با لبنان پایبند است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25291" target="_blank">📅 21:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انتقاد و تکذیب روایت تاریخی مارکو روبیو درباره جنگ‌های ایران و یونان باستان
مارکو روبیو، وزیر خارجه آمریکا، در سخنرانی خود در آتن، با اشاره به حمله خشایارشا به آتن در سال ۴۸۰ پیش از میلاد، تلاش کرد میان تاریخ یونان باستان و سیاست امروز آمریکا ارتباط برقرار کند.(تورج دریایی: ایران‌شناس برجسته و استاد تاریخ ایران باستان.)
می‌گوید این روایت بخشی از زمینه تاریخی جنگ‌های ایران و یونان را نادیده می‌گیرد؛ از جمله شورش ایونی‌ها و حمله یونانیان به سارد، مرکز مهم هخامنشیان، در سال ۴۹۸ پیش از میلاد. همچنین فتوحات اسکندر مقدونی و سقوط امپراتوری هخامنشی نشان می‌دهد که تاریخ این دو تمدن، برخلاف روایت یک‌طرفه از حمله ایران به یونان، مجموعه‌ای پیچیده از جنگ‌ها، لشکرکشی‌ها و رقابت‌های سیاسی بوده است.
آتش‌گرفتن آتن واقعیتی تاریخی است، اما استفاده از آن برای ترسیم تقابل تمدنی میان ایران و غرب امروز، نیازمند در نظر گرفتن تمام زمینه تاریخی است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25290" target="_blank">📅 21:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فرمانداری چابهار خبر واگذاری ۱۱۰ هکتار از اراضی این منطقه به افغانستان را تکذیب کرد. این شایعه پس از انتشار گزارش‌هایی درباره اختصاص زمین در بندر چابهار و منطقه آزاد برای سرمایه‌گذاری افغانستان مطرح شد. با این حال، تکذیب واگذاری زمین به معنای رد کامل موضوع اختصاص اراضی برای سرمایه‌گذاری نیست؛ چراکه اختصاص زمین برای اجرای پروژه‌های اقتصادی با واگذاری مالکیت یا انتقال اراضی به یک کشور دیگر تفاوت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25289" target="_blank">📅 21:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سپاه تصاویری را منتشر کرد که نشان می‌دهد پهپادهای شاهد در جریان جنگ، به سمت کشتی ها پرتاب می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25288" target="_blank">📅 21:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایلان ماسک به اپراتورهای موبایل اعلان جنگ کرد!
اسپیس‌ایکس با توافقی ۸ میلیارد دلاری برای خرید فرکانس‌های رادیویی باند ۸۰۰ مگاهرتز، گام بزرگی برای رقابت با اپراتورهای موبایل برداشت. این شرکت همچنین مجوز استقرار ۱۵ هزار ماهواره نسل جدید برای ارائه اینترنت مستقیم به گوشی‌های معمولی را دریافت کرده است؛ طرحی که می‌تواند وابستگی کاربران به دکل‌های مخابراتی زمینی را کاهش دهد. البته انتقال کامل شبکه موبایل به فضا هنوز واقعیت ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25287" target="_blank">📅 21:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a757bdbbc.mp4?token=ViEI_L6oj9VaALC34PsbxTx1584cXnLH_cjVj4dyp_Tewxcq-bg9aGDa97A4aR-dqPwrqZ0nWwx3ty80QjrYXs31Qymj_XQLtmRnuN-GDS-ua6-gjUrZOA3HmHCWh-Ix7reHQxqbqT4sT9aa6YNPv-Ir5RI1UasWqshiFOhKewrVIZ1w31jDRblyQyiPYzn6BXNyPQ8b_Xasp0SGdke4Du-I_qqT3-J7mIA44cjdeXGHDxmtHjXNK8y-bWJjb14U5YHaFLkRjjRPEZ5prgVPQA_d8cmeIDpgwsnbOfdsJikPejMVU3KLTjOvgAAxybHbaV0-AJV7tzeX_njCqLFJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a757bdbbc.mp4?token=ViEI_L6oj9VaALC34PsbxTx1584cXnLH_cjVj4dyp_Tewxcq-bg9aGDa97A4aR-dqPwrqZ0nWwx3ty80QjrYXs31Qymj_XQLtmRnuN-GDS-ua6-gjUrZOA3HmHCWh-Ix7reHQxqbqT4sT9aa6YNPv-Ir5RI1UasWqshiFOhKewrVIZ1w31jDRblyQyiPYzn6BXNyPQ8b_Xasp0SGdke4Du-I_qqT3-J7mIA44cjdeXGHDxmtHjXNK8y-bWJjb14U5YHaFLkRjjRPEZ5prgVPQA_d8cmeIDpgwsnbOfdsJikPejMVU3KLTjOvgAAxybHbaV0-AJV7tzeX_njCqLFJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس ، معاون ترامپ : می‌دانیم که مردم نگران هزینه‌های معیشت هستند و این موضوعی است که هر روز با تمرکز کامل بر حل آن متمرکز هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25286" target="_blank">📅 21:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واشنگتن‌پست: یک مقام ارشد دولت ترامپ اعلام کرد هرچه متحدان آمریکا سریع‌تر مسیرهای حیاتی ارتباط اقتصادی ایران با جهان را محدود کنند و منابع مالی و منافع جمهوری اسلامی را تحت فشار قرار دهند، واشنگتن زودتر به هدف خود خواهد رسید. دولت ترامپ با تشدید فشارهای اقتصادی، محدود کردن صادرات نفت و مسدود کردن مسیرهای مالی، در تلاش است ایران را به پذیرش خواسته‌های آمریکا وادار کند. با این حال، هنوز مشخص نیست این کارزار فشار چه زمانی به نتیجه خواهد رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25285" target="_blank">📅 21:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25284">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25284" target="_blank">📅 20:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خلاصه پیغام های زیاد : تهرانپارس بین فلکه دوم و سوم انفجار شدید اومد آسمون رو دود گرفته و بعد صدای تیر اندازی شنیده شد! علت نامشخص ولی حمله هوایی نیست @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25283" target="_blank">📅 20:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJSTr8Pi2mHV6kqEl-7WJ368bQ9m9fx0dMBq6-oDdwDJ7WuYNJDnQkrdR3xPm1r-M7zEZw3aTyHKwngMMeJts4pEHjsuS24sWp8bAIpsqgKVJGDeEmvnoYV9LleHucZwo-XoJdfEOJ5A8AII0Qv2Nfk6X4Ql7FYw_SBYI5pTq3w3nWH2Ut-DESKOYPm7W-W4o7AmJhmKYf9XcYNqP873t5mC3fjz1OVt25iW99_Qg17hzFZgeb_6l6FPlqJ2_Ogyiz5zvpNO1rmqu3wARgYStGHZlAFDLEnICQpEn5M9EoD4COkm69Sj5YldSkLoCbh6lsDopFDiPDA-ktQVKvEKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKUdVXoVD2s45ZS9qeRRGrUuEx_6OyUbqHoTSSsRwJuJ3XbJ8L1JKJbpZqXkU6AzXjRhvDcEalpVIXJJ0TLEjMSXNKfEfj1ufuYyUWhaeqt0SQEBMlHTdQjVuQUO3EIQD6QAULOCOUV2x0kGU8-VWup6lnU-sMiOcriVQ7DSbznt1dOgfp_DnRn1_dTGPOjwSwO46KHOaZhAX2GevyVUCfiA_0aybdvf98nm2mgVgYFO4N9Q6l_TDerVK0r0TsZtg26t4O76rOWweHh4KFdUxgCkfL0t9n_hWn_glKRmMJsUCk5av4HQ2ncAuhmgG2c1dWeNSPdRnn_RKUW7g4D6CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خلاصه پیغام های زیاد : تهرانپارس بین فلکه دوم و سوم انفجار شدید اومد آسمون رو دود گرفته و بعد صدای تیر اندازی شنیده شد!
علت نامشخص ولی حمله هوایی نیست
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/25281" target="_blank">📅 20:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هم اکنون صدای انفجار مهیب از محدوده فلکه سوم تهران پارس ، شرق تهران ، دود مشاهده میشود
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25280" target="_blank">📅 20:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a4aeebe5.mp4?token=TCcNGrtbBGkw4ETCkZMtC3DBinI1owM7Uux5H0xynlF7xGPEbGjIJClApekSzCoDnIN3Hh-hUGY3w_WOJcWQliP3l_G4wDVtEfScPiHMV2egtUdnBoJmBE4AzYBAB2f770UGUIsPK2n5hj2SEPxjzp8tJP8ltt3O06JVNyZTpw-tbgqlXshFbEWZ9cLsU6_FQAoWBiuDRo3WIwjzddyFP7xNqHsgOnvPKOY5YD1c4QY-6e8owRzlaQZTieGKtSUKeG3kSCbF02nal-JqlKtAULhlgwQUGkW2oaPV-9mUW0Eu7WOnFepHuYxKbzAJPumFqkORv8aneyRGMiWlItd5Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a4aeebe5.mp4?token=TCcNGrtbBGkw4ETCkZMtC3DBinI1owM7Uux5H0xynlF7xGPEbGjIJClApekSzCoDnIN3Hh-hUGY3w_WOJcWQliP3l_G4wDVtEfScPiHMV2egtUdnBoJmBE4AzYBAB2f770UGUIsPK2n5hj2SEPxjzp8tJP8ltt3O06JVNyZTpw-tbgqlXshFbEWZ9cLsU6_FQAoWBiuDRo3WIwjzddyFP7xNqHsgOnvPKOY5YD1c4QY-6e8owRzlaQZTieGKtSUKeG3kSCbF02nal-JqlKtAULhlgwQUGkW2oaPV-9mUW0Eu7WOnFepHuYxKbzAJPumFqkORv8aneyRGMiWlItd5Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: بعد از آن، موشک‌هایشان به سمت کشور ما حرکت می‌کردند. آن‌ها در تلویزیون با این موضوع شوخی می‌کنند و می‌گویند: «تو گفته بودی قرار است لس‌آنجلس را هدف قرار دهند!» اما واقعیت این است که مسیر پرتاب موشک به سمت شهرهایی مثل سن‌دیگو و لس‌آنجلس برای آن‌ها مناسب‌تر بود. البته احتمالاً پیش از آمریکا، اروپا را هدف قرار می‌دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25279" target="_blank">📅 20:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بن‌گویر وزیر امنیت اسرائیل : زنده باد جنگ.
@WarRoom
😂
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25278" target="_blank">📅 19:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b2196422.mp4?token=voJCL-Wb19msMYeMIt75qa7jSH0MAwmLtV7-HUk_2bzdUj_DHhTNiu9hjLe3o6w1HlAIGDjMcfXjAmvLNGN9nNfNuQ0a2PW8brhzOzQ0QALDL28fld4gZ3wp3Wz1TV-tYW-n3uweZ3A1_WBYJxN_kNHsu9NqFGH1cswOULompXvI8VSKEU3KCFlwcIOlONy771jIRvep7oV0kez5vNZOq7Mv7mMThr-YJbsUzsbc-q1rzaw1YdlXqwXG-WFseJnG8NZtj2RxC-bO-PnCsXa70MWCQ5EdEVF1UKusAAsiTEUQm872WVY5f12to0OmMiuQs9cSicvylwjMm1TcFtA2SAqeTyyhmIgDJhsCWzis7Jp8k7RX9w5N1ET4260D4ElK5RBt-jGBnVKRdCxStENujlUy0PwvzJTNRic5xrynQvcy-JEYGcmQ9VuTBn8ilOkg-4EegcYKCQ17_XvsagZIVJdfsBE7UK4CStvUffZ1tH4pZZL0g1gmkyX94E90UmXzwVteDYynP7LRIFX2dS0y-FCVxuTv9DC-Hr3AILgUPhi30JLJGNnsr7PGigISo-USBndt4W49c8KdfkKSX5XIevtxA90lMAlRycGvDeX5tg7jU8FJd5SU785kq42ki0_XoVoiTMdCGmPn0x_Q4XcN-dGsUXLRiAAkRG9hLgHKhaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b2196422.mp4?token=voJCL-Wb19msMYeMIt75qa7jSH0MAwmLtV7-HUk_2bzdUj_DHhTNiu9hjLe3o6w1HlAIGDjMcfXjAmvLNGN9nNfNuQ0a2PW8brhzOzQ0QALDL28fld4gZ3wp3Wz1TV-tYW-n3uweZ3A1_WBYJxN_kNHsu9NqFGH1cswOULompXvI8VSKEU3KCFlwcIOlONy771jIRvep7oV0kez5vNZOq7Mv7mMThr-YJbsUzsbc-q1rzaw1YdlXqwXG-WFseJnG8NZtj2RxC-bO-PnCsXa70MWCQ5EdEVF1UKusAAsiTEUQm872WVY5f12to0OmMiuQs9cSicvylwjMm1TcFtA2SAqeTyyhmIgDJhsCWzis7Jp8k7RX9w5N1ET4260D4ElK5RBt-jGBnVKRdCxStENujlUy0PwvzJTNRic5xrynQvcy-JEYGcmQ9VuTBn8ilOkg-4EegcYKCQ17_XvsagZIVJdfsBE7UK4CStvUffZ1tH4pZZL0g1gmkyX94E90UmXzwVteDYynP7LRIFX2dS0y-FCVxuTv9DC-Hr3AILgUPhi30JLJGNnsr7PGigISo-USBndt4W49c8KdfkKSX5XIevtxA90lMAlRycGvDeX5tg7jU8FJd5SU785kq42ki0_XoVoiTMdCGmPn0x_Q4XcN-dGsUXLRiAAkRG9hLgHKhaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما مانع دستیابی جمهوری اسلامی به سلاح هسته‌ای شدیم و این موضوع به‌زودی، به یک شکل یا شکل دیگر، حل‌وفصل خواهد شد.
ترامپ: ایران دیگر ارتش، نیروی دریایی، نیروی هوایی یا سامانه‌های پدافند هوایی ندارد.
ترامپ: دیروز بیشترین حجم نفت از زمان آغاز جنگ از تنگه هرمز عبور کرد.
ترامپ: دیروز ۲۸ میلیون بشکه نفت از تنگه هرمز عبور دادیم؛ رقمی که از زمان آغاز جنگ بی‌سابقه بوده است.
ترامپ: خبرهای مهمی درباره بحران گازوئیل داریم و برای حل این ران با قدرت اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25277" target="_blank">📅 19:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00c1954a3.mp4?token=LmOZhCs3cJu-FV00oBaM0xgzVioSqdlIZXxzZyspcC4A-lUP9RMFl_LPJEQo3qV8O_GMxi3VuC2mC4wzS5PV213MwD0mx8oJZt8ffSaggm_FUY-hg-Cf1wsLV1Hku2WVnQt5Ug777_wBuFogS20qNRMrz-h_7_dwHD39QXaYwVZZtvg_iNN-CqMKBXXoy1cok_wCmYewjI7Nj4r1ESgRedwgb01FRqJjSuePll7UjWPjsxynK1PMJUAFPFVohpKp-L90i0Vz-H0ZX71eqvr-fYpcgWWUycgGps20Ga36I6M94p31etAX6-x0B4uN8F3LiY1BC4E08Y6zayhpOX0DoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00c1954a3.mp4?token=LmOZhCs3cJu-FV00oBaM0xgzVioSqdlIZXxzZyspcC4A-lUP9RMFl_LPJEQo3qV8O_GMxi3VuC2mC4wzS5PV213MwD0mx8oJZt8ffSaggm_FUY-hg-Cf1wsLV1Hku2WVnQt5Ug777_wBuFogS20qNRMrz-h_7_dwHD39QXaYwVZZtvg_iNN-CqMKBXXoy1cok_wCmYewjI7Nj4r1ESgRedwgb01FRqJjSuePll7UjWPjsxynK1PMJUAFPFVohpKp-L90i0Vz-H0ZX71eqvr-fYpcgWWUycgGps20Ga36I6M94p31etAX6-x0B4uN8F3LiY1BC4E08Y6zayhpOX0DoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: دیروز ۲۸ میلیون بشکه نفت از منطقه تنگه هرمز خارج کردیم؛ فکر می‌کنم این رقم از هر زمان دیگری، حتی قبل از جنگ، بیشتر است.
ترامپ درباره محاصره دریایی: ما محاصره برقرار کردیم و هیچ‌کس از آن عبور نمی‌کند. انگار اگر محاصره را به ایتالیایی‌ها می‌سپردم؛ شاید آن‌ها حتی بهتر هم عمل می‌کردند، اما شما این کار را خیلی خشن و با شدت انجام می‌دهید.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25276" target="_blank">📅 19:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edb5373c67.mp4?token=nsWU9d4j6l2Xx0Gb-jb2avqhptyfOB4B-r-Hd3C3tuGDztgSMjkh_cy1hvhHoMDJBEqH1Ll9E8u_onzsCgTQHssbhWaepGxNRZJ9qp1zCCyGVYoigB-kPgy_06WqEsYAQj0xXsVADjnX0vKUqPCHwr0RFdcGcPRsla5dtxhsT0UUoc_XtMpHAmTJujYahHyrynCnxsxDytHQNrPur7FyS1tGAAqXgSv4FY1V7kFwxJo9VoQXv-nKbEK0zarlVehxNTjdyf8fiOhaBEI765LUFYN7_P0vvgAyXPWp5i32T8v2wOfq3cKH4TtGuISlLmKbtnASOQqWYgCUovcVWQ9QZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edb5373c67.mp4?token=nsWU9d4j6l2Xx0Gb-jb2avqhptyfOB4B-r-Hd3C3tuGDztgSMjkh_cy1hvhHoMDJBEqH1Ll9E8u_onzsCgTQHssbhWaepGxNRZJ9qp1zCCyGVYoigB-kPgy_06WqEsYAQj0xXsVADjnX0vKUqPCHwr0RFdcGcPRsla5dtxhsT0UUoc_XtMpHAmTJujYahHyrynCnxsxDytHQNrPur7FyS1tGAAqXgSv4FY1V7kFwxJo9VoQXv-nKbEK0zarlVehxNTjdyf8fiOhaBEI765LUFYN7_P0vvgAyXPWp5i32T8v2wOfq3cKH4TtGuISlLmKbtnASOQqWYgCUovcVWQ9QZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران و محاصره دریایی: ایتالیایی‌ها شاید حتی بهتر از شما هم این کار را انجام بدهند، اما شما این کار را خیلی خشن و با شدت زیادی انجام می‌دهید.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25275" target="_blank">📅 19:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2623ad9e11.mp4?token=bFFiqfFfmr3xGaCZUc5-KxzbO5lvI9undqweeOLVHfH7y7VeioCJagg4RiB8p8H11KE4y1rWUMxW0q_rq10_VOmuadzfsKAy4DRBSN7ooWfNOs4ykn7SObEKJKwA_bU_k48N5xj71IADwrNC7Y96_lLktfdj4xuCKulzIvbZkfthSewC39xmtJuKUWjOlDZ2la_UJYEYxGq5C1NlQWHpvxvlqWfmXCquhMsAjOq3r6UrjCDYyxu9WPsAzLY6FcAv2kKxnx131Jk7Wxp41t6kV4aAqVu8JJS7DQfV-zLRmfDYVGJNS3WGgWY7_jwp8JtIfCM9YLYnaGg-tKqrUSYXCXn5AJCOmGQnS_mpLK1nbP3KDpv30OXNXHfQevOrvei-j_bwfdsYFIcKXlDtKqUNtN0kpr18lu92Uq02nc5nLsPwkDhu_YyRiQSmsfchJByiT_Am8xMqPV_LPuvfloSG1BNkog1gpiRIKLafBnDs_sHzvL4RKUvtK4vPIZmcwY-T9c_DzCSfjaEX61IH_gUl5foO-OYXhczFTDw0pfPOpxHv0oZmYPazKg-oJUE0vI3teEPh5KHs3miJLRVgXdSb-zS0G2PaWiae_gDf39XDQQIw06w9V7em2Rsg3nMN_OKismfk5JXGAOhFf76R99EKAZV45H9HVaW4c8K5N_Cva6E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2623ad9e11.mp4?token=bFFiqfFfmr3xGaCZUc5-KxzbO5lvI9undqweeOLVHfH7y7VeioCJagg4RiB8p8H11KE4y1rWUMxW0q_rq10_VOmuadzfsKAy4DRBSN7ooWfNOs4ykn7SObEKJKwA_bU_k48N5xj71IADwrNC7Y96_lLktfdj4xuCKulzIvbZkfthSewC39xmtJuKUWjOlDZ2la_UJYEYxGq5C1NlQWHpvxvlqWfmXCquhMsAjOq3r6UrjCDYyxu9WPsAzLY6FcAv2kKxnx131Jk7Wxp41t6kV4aAqVu8JJS7DQfV-zLRmfDYVGJNS3WGgWY7_jwp8JtIfCM9YLYnaGg-tKqrUSYXCXn5AJCOmGQnS_mpLK1nbP3KDpv30OXNXHfQevOrvei-j_bwfdsYFIcKXlDtKqUNtN0kpr18lu92Uq02nc5nLsPwkDhu_YyRiQSmsfchJByiT_Am8xMqPV_LPuvfloSG1BNkog1gpiRIKLafBnDs_sHzvL4RKUvtK4vPIZmcwY-T9c_DzCSfjaEX61IH_gUl5foO-OYXhczFTDw0pfPOpxHv0oZmYPazKg-oJUE0vI3teEPh5KHs3miJLRVgXdSb-zS0G2PaWiae_gDf39XDQQIw06w9V7em2Rsg3nMN_OKismfk5JXGAOhFf76R99EKAZV45H9HVaW4c8K5N_Cva6E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ترابری ۲۴ ساعت پیش تا همین الانه الان ! دارن پرررر میان (عرزشی هستی نبین سکته میکنی) فقط آخرش که مال همین چند ساعته یکی از‌ زیبا ترین پل های هوایی شکل میگیره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25274" target="_blank">📅 19:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">😾</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25272" target="_blank">📅 18:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رویترز: دولت ترامپ تحریم‌های گسترده‌ای علیه دیوان کیفری بین‌المللی اعمال کرد که ممکن است دسترسی این نهاد به خدمات بانکی، بیمه و نرم‌افزار را مختل کند. این اقدام در واکنش به صدور حکم بازداشت برای بنیامین نتانیاهو و دیگر مقام‌های اسرائیلی و تحقیقات قبلی درباره…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25271" target="_blank">📅 18:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یسرائیل کاتس، وزیر دفاع اسرائیل: یائیر گولان اکنون با حذف خامنه‌ای و عملیات «غرش شیر» مخالف است؛ نفتالی بنت با عملیات «ملت شیر» مخالفت کرد؛ یائیر لاپید بخشی از قلمرو حاکمیتی اسرائیل را به حزب‌الله واگذار کرد؛ آویگدور لیبرمن می‌خواهد بزرگراه ۶ را به کنترل یک ارتش عربی بسپارد؛ گادی آیزنکوت می‌خواهد از لبنان فرار کند و منصور عباس پشت پرده پنهان شده است. اگر این‌ها گزینه جایگزین باشند، چه جای تعجب دارد که همه دشمنان ما برای سرنگونی نتانیاهو و دولت راست‌گرای او تلاش می‌کنند؟
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25270" target="_blank">📅 18:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVPP02z0GOMKVk5pxNVJwjv9j8F4Dn3zjaIOqRs6swRCCR97KgrxkrPe7kuW51q9SdSbHnr4NbH88Z8-ugh84YfDximc9eZJvS8WEYl3EC8WltDjfVY3-x6C6QatVVLqeOM2-Z16MNdBRA7Y34262-6Tsbng5AXhPlB2L1KWNwg7ZpN1OnattA-4nGmr04ci10oZJYNhrk3HzQ11dhd3eyoSBs5RlIhQ3gzyZg_VaQamMQytdhK1yOTG0hM1NL25hySgup3qrG1JGCvpn4MT6CEJGqTMiksreO_tb1S9yl2XXHyZFOScOb_0ClWgBdViQsH8Qr0DhH9LE8PCycAFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/683fae1eda.mp4?token=WG4XQWGJn15TyX1YV1riZTV0V8dKUMQ7JRahAdRiqrwLeB7tuzB_2t_gYPdLbWUscPGMlHMN5muofr5fQsGDqEV6Hh5AOpWNm_D8N5UboU007GqAqVClQjGg69awA3rhCfvxI6v-vdN1TREW9Ns5l8u8UN9iTkHcKWSV1xh821CMkgY6SlmjhcrpVSy3d32jBcTC6aH2PFvjWaCxLrgFbdSjYv07Mchir8Ev9fo6nGFJ-nVdaoyn2buT28ct4Mj5KsQk3iyYsvflimo2JRH_Qnn6tV2EoS8MqTgtUhJ10rbQwfgtWJNQjwGo3WZhELlu5KpHvs9SWxUe_UNOqZ7Reg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/683fae1eda.mp4?token=WG4XQWGJn15TyX1YV1riZTV0V8dKUMQ7JRahAdRiqrwLeB7tuzB_2t_gYPdLbWUscPGMlHMN5muofr5fQsGDqEV6Hh5AOpWNm_D8N5UboU007GqAqVClQjGg69awA3rhCfvxI6v-vdN1TREW9Ns5l8u8UN9iTkHcKWSV1xh821CMkgY6SlmjhcrpVSy3d32jBcTC6aH2PFvjWaCxLrgFbdSjYv07Mchir8Ev9fo6nGFJ-nVdaoyn2buT28ct4Mj5KsQk3iyYsvflimo2JRH_Qnn6tV2EoS8MqTgtUhJ10rbQwfgtWJNQjwGo3WZhELlu5KpHvs9SWxUe_UNOqZ7Reg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع محلی از کشته شدن معاونت اجتماعی انتظامی استان سیستان و بلوچستان در منطقه چشمه زیارت زاهدان بر اثر یک بمب کنار جاده‌ای خبر می‌دهند. @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25267" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رویترز: دولت ترامپ تحریم‌های گسترده‌ای علیه دیوان کیفری بین‌المللی اعمال کرد که ممکن است دسترسی این نهاد به خدمات بانکی، بیمه و نرم‌افزار را مختل کند. این اقدام در واکنش به صدور حکم بازداشت برای بنیامین نتانیاهو و دیگر مقام‌های اسرائیلی و تحقیقات قبلی درباره…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25266" target="_blank">📅 18:03 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
