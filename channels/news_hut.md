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
<img src="https://cdn4.telesco.pe/file/I4aHwKbs0rQ6BbiQKC5zczX10670ykBkK0copiM2clwhZTrmfDGnA09aCgXaYlAA9P8G2sZxHRPoPgdHOA75O0XdxO3DRDd2jzsQoQgVGUOwmJERA-Igelhss8akD7FlPsRwswqBUn1Zj8HEniBl5RCV3hRhXfk0CsG5kDQeFdsPWwdpkgfvDnHHW-JUT9owANJxOQNv2ZHi2hC-wvdYzD_mQRubXccffui-45VDM6D6qeucbJLm9Gvsz1UlLnG_xro4hROlkHy--PrutSMfM-jJ71-Nnr4XtHjkprS-6rqBl79OmwoiLr7b-XctKqs-qYiYeD81SG_7tQyWHwLl4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 218K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 08:38:32</div>
<hr>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q1QuHE63OsTASea9aKnkJrAOr19Vdk-1EaIUgiF2znWyfGvLy_Jv5LRSfirXLejJqznD4kn7yEUeZ2evYDdfFVaabshRAaFLbyEfHSKJzkIxYCVKRuqPxSLX4gEdNdLVyZIMFUzvaXYN0YXRxTMoBhbikLIG_oFZ2-8ZTeb1tKwA98TauuW8rrzmvUVNPcX2JS9F4g1ZAJo-9R_aHeW1uD52WJ39aMmbwArLT9Fb9RErFtnRJ3zHgKHe6QHFp-Ku7BozMF63jhPdAIuSRfTz_jnTawqyGtCSGUgCMWfDarGVz8rz_MUrHirI2BbM2E1e_aGMThqF-tJorOuSWFdBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=Z8_HBrdrLAvPtTFIdCsN6vFEkIxXqTp8FuSKjb4Cj7mCl1h1IoxFG2QYtXvxhiyflSCkQnkHiWE-6yEX31fmjsVONKGh3Iyxgd-6r-2xlVO8jJdUlkdbfirdk8WqMdeTLMRvWTIcxkjqAmszwyZD2_JUUdKzewvJetLfSlGz0_8OJhcrLOff9_nDdzqqPsMhKYfoqqtDSc0wfO51giqLIQhzUpniCKM2mqq_7j5aFFszpoJ4azbmBx0GYXNwKGi7uradDaHcSmeiRPKYtt-z3SNPBQIOGaR3hMqa9Wgb7q9OtZ6jDnmEwZYAtKYfxBgdnKFY1wy4Qg5zoyG7ELHIkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=Z8_HBrdrLAvPtTFIdCsN6vFEkIxXqTp8FuSKjb4Cj7mCl1h1IoxFG2QYtXvxhiyflSCkQnkHiWE-6yEX31fmjsVONKGh3Iyxgd-6r-2xlVO8jJdUlkdbfirdk8WqMdeTLMRvWTIcxkjqAmszwyZD2_JUUdKzewvJetLfSlGz0_8OJhcrLOff9_nDdzqqPsMhKYfoqqtDSc0wfO51giqLIQhzUpniCKM2mqq_7j5aFFszpoJ4azbmBx0GYXNwKGi7uradDaHcSmeiRPKYtt-z3SNPBQIOGaR3hMqa9Wgb7q9OtZ6jDnmEwZYAtKYfxBgdnKFY1wy4Qg5zoyG7ELHIkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=ot432rS62Td3kR6ec_wLozGEAmBdB5rICwc2vneoyJPfgNYl6DvTN8hKzrGTPyOqoRby25hwW0C0BmLGteuMxyCToz6cvia77kY-3hIYT6yO1-1eYZYJIHaI9gsGTqGZ8i9TMKJTxiGpRa6YVGxVAXf3aiLhmK2vJMMRKOlLIY2uVPqvaAxyLCmVOcefczWPP9UOp1cQzTCDwWYjM11sShifTbeIewFx8l2pg_K--wUeEn0F1JtSpdt1s3WgFIpqGHCPqsVzxmp5Tqhp-vCDWlsoPZYHmT2fHufmBUh_73uqG8_R4v5oxOoucuak0MMwJfPHPWSi0wFEJ7fLHJ23Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=ot432rS62Td3kR6ec_wLozGEAmBdB5rICwc2vneoyJPfgNYl6DvTN8hKzrGTPyOqoRby25hwW0C0BmLGteuMxyCToz6cvia77kY-3hIYT6yO1-1eYZYJIHaI9gsGTqGZ8i9TMKJTxiGpRa6YVGxVAXf3aiLhmK2vJMMRKOlLIY2uVPqvaAxyLCmVOcefczWPP9UOp1cQzTCDwWYjM11sShifTbeIewFx8l2pg_K--wUeEn0F1JtSpdt1s3WgFIpqGHCPqsVzxmp5Tqhp-vCDWlsoPZYHmT2fHufmBUh_73uqG8_R4v5oxOoucuak0MMwJfPHPWSi0wFEJ7fLHJ23Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1q71CYhLnSDuybInhRzU9CHxv5rDxKGw4PYGH2mFPKHLV5wsQK4v4VNYgs16WLLncdYVmhkIrDIWPhverll-2TS401dKAZzPMG1JETWd9Cd_ERR2PElraqY_TM4cZNrH8u1zDwyC1hjQ-PRvpqLCYQnuZEHcqfbLS-V3paWA_V4LsOB-noLR47M0T0Scl2lL8pdw0wLl1kf8SnUMvzk5JQ9qB73fdxdEb3i8X_6T4KT0qMTLGJFTLIR5VNVZSXxC7pFn9tZcpvgndkxAUVW8fGN8aRAlnOX5FUZAg04nAfI0xtEjDsPXBth67rUnghaMly9rOTr6BpzXrEoiYv3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=NMgzHPrzWv7xXAJC8BAyASoAvnC0doj6_choqWgHamRYYoVKZs4SWPy7ZGF0AZXdICQaZpsPsYTFsqOQJafFShkVQTKeGMqTYF3gFiEMdY3Mn2RE_771wobDcfBD0ojT2UXCjrTTrjZ7vMUS4P1xoqJuCouJ_fwsGOAX4LPH0N2WyZTW1xdUdmr6EqHqNehvPc2ixyNlA8s58eeD-ZnaHfvBaHGXZdTFQX1Zkd-snamLjgN1ppLziWOT-pO5sx4ImRSJL5wqyGBApqu0SrzoNXSnkcaTh1DrP_L54_v9H_8Re_p6_RKAQlbn8iteUYSJNvWrOzgfw3zjsIWIwpH6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=NMgzHPrzWv7xXAJC8BAyASoAvnC0doj6_choqWgHamRYYoVKZs4SWPy7ZGF0AZXdICQaZpsPsYTFsqOQJafFShkVQTKeGMqTYF3gFiEMdY3Mn2RE_771wobDcfBD0ojT2UXCjrTTrjZ7vMUS4P1xoqJuCouJ_fwsGOAX4LPH0N2WyZTW1xdUdmr6EqHqNehvPc2ixyNlA8s58eeD-ZnaHfvBaHGXZdTFQX1Zkd-snamLjgN1ppLziWOT-pO5sx4ImRSJL5wqyGBApqu0SrzoNXSnkcaTh1DrP_L54_v9H_8Re_p6_RKAQlbn8iteUYSJNvWrOzgfw3zjsIWIwpH6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=DF2nxGBaOeE7EapkCI_WOLOJHa9MzLyyzXk7ktr4nl5H6LqXxLWzyESQOVlQwnr5_pufhS7iHEgD1Clg7SSIYcMWEXAtOvFbkRXbEA3VT4hjsvvGkmh9F_gxEtcNpf_WpMAvc3oozHhQMUEUVGAIMgybUWKdBl06xusQDHIp4KzDQ0XEbpAq8kidG9g7wcOAcc8QL0Wo3GFS_x2zlp1GmSJ-RSyGckES5R_aEUVCs8hz4RGjkQNLvbeRAL5VnhDssy7vECJEvfLTbeXKH3sc8yQDY1y0Q27c7ocOIOsu2hxh7w3HTI7lFtMouuT7E1xif7ov5n3-FYZWdME56uDOvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=DF2nxGBaOeE7EapkCI_WOLOJHa9MzLyyzXk7ktr4nl5H6LqXxLWzyESQOVlQwnr5_pufhS7iHEgD1Clg7SSIYcMWEXAtOvFbkRXbEA3VT4hjsvvGkmh9F_gxEtcNpf_WpMAvc3oozHhQMUEUVGAIMgybUWKdBl06xusQDHIp4KzDQ0XEbpAq8kidG9g7wcOAcc8QL0Wo3GFS_x2zlp1GmSJ-RSyGckES5R_aEUVCs8hz4RGjkQNLvbeRAL5VnhDssy7vECJEvfLTbeXKH3sc8yQDY1y0Q27c7ocOIOsu2hxh7w3HTI7lFtMouuT7E1xif7ov5n3-FYZWdME56uDOvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1vSYvEDcq0l4ZKUSn0z6sN-oYHQmCv0-V9H7aFVKPdulX9_Pas3013MzLKtywWtjEufUgjWjBzfaGdddh5xziVLc-v3yxEtej6Rikgw6wT6-zfqiGE6Xko0FzUfBEqKcSdcXZvBtLYl45N1mVKb-18w7RE1uCH_A9iGjPnif3Wfhk1LUdkdkR97B3icYxq-8djgmMT7Mmk_vqffFg2YCBrWpPnqe_o1mcFLVIjd2YYHxFTAZEVr8SWnZn5WhWI87IC47et5pzO5y-2_V3ecPWKauncr0fl5HSVgVP9poDCbXf_mvKuTOVuaYUKyGhWiKw4yYbdAJg5C73ka2DCcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvnlZH-QNiC2Ltq_mHe9ekVhgGZ9lDrAMKIgTJmpRs53XL6p-KKtc0B-F1ljXS2z374u5FIgI8Lu71XhzACIX3Z1OqOn326mzpM3NUZ5RbxXNdGVDFx0o7J_cPVHKakX9l6Dy3uKgUKtTYJePR1-C9QxEJ0jAFEXnUckbJUm6KsdGLf01MResvarSBmvw7KddVgJusXcfUZ_9oSYwG-1wTP4fPDl63SXnuV6RpatNe6ndJ5YD2R-qiDeF41-XJEzHJHDRoBRhA3F0Ir9YDwftswOZUi-4BSHxEfJMh-llgeE0-D38eIrCETKTymbiST8rHQHffxaIeQZ9yfkQoqF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l9G-ZtQ3Lrncz9vtTI5IPMhWmXqK08eNnO8USvvFS6AscUQjOGZEtM4ia0B-ozEj59kyhLE0cytUt_gJ_PiiKyGWAqb9Fif9Bi_E2qeur0GxC2o95x8xW9-oyzwGyTxStnq7OdgMTYTjED4jAKU0m8GM-GOy98MQuvujnHyF8-mtja6fu9wOq44mnAWQdJzklpz3NQKIDzbutGOK0olsZ-usIzFlhKz02m9eyWZCV-zbBKCrbNhcLv92HRodA-luTbmQwEsoNmHDIh9ndxfFyoSgGJDJj4_sHv6kFfnqRAglMS1_EbaD-OwzTpDdarok1D5ktjL3i3OtkGxG7R1GfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=YSHPKGdHt9PaYOuxS5_PajL-93r3jUbXebT_8zsVR11dKRl6nSyCLP_N7-2Qte4sCWH263luZ-8X1jhy0A1H6fYFV2N-lKgAU8YOd6MbEFbwEqkhk8fz8U1pjp8rg6XhfD3byROnBYWnLIMYv-hptmJPgeFjPXl2ZZPwJokEITYs1qdxYblapAOpqdjVmKmhPyr1lcmt6mE7tAMDBbaA9-zjS6jybr5aVaZEqrUMEcnIvx0feYQbm4Lo7V6COVfVnarSmYtKF8EJNFNp41HUt9mKbovrhc0Ze2ikXNhMTvdnXzzame3BfUBYwTa7yLyA9tnXUA4yJ4As3ltxfuDpIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=YSHPKGdHt9PaYOuxS5_PajL-93r3jUbXebT_8zsVR11dKRl6nSyCLP_N7-2Qte4sCWH263luZ-8X1jhy0A1H6fYFV2N-lKgAU8YOd6MbEFbwEqkhk8fz8U1pjp8rg6XhfD3byROnBYWnLIMYv-hptmJPgeFjPXl2ZZPwJokEITYs1qdxYblapAOpqdjVmKmhPyr1lcmt6mE7tAMDBbaA9-zjS6jybr5aVaZEqrUMEcnIvx0feYQbm4Lo7V6COVfVnarSmYtKF8EJNFNp41HUt9mKbovrhc0Ze2ikXNhMTvdnXzzame3BfUBYwTa7yLyA9tnXUA4yJ4As3ltxfuDpIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txE5BLGY47fqy4AdX46zKMrx8hN7TiTCWmMXUBZwcI5n-Lp9lld0B6sue7D1K3S10gSYwaQj1XpnCQieJDM6k0hmbA7U1X32HnPPwprlx7bdxW44ntKa4HyHn0PseUKSZSSiUIPzLWglTHvwMKe020kLhiKbymTrD6WsBVysiFODAj4zh5U0iwT3WNyzeBUVALPFIyswQVLYlOa7LdZsdtJak25WTlLBDVMPetNomVse1OtVGQLhPQDtFI9yWpjApLzqXP_mUCMciyFOC8QqeCz8-uNaRB9E0PXrxOJdryYecgo_xy_vV37k9pa8LVKKqpoIUs4m6yiVXbfaVxr5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m93ZWito6W-WrsHfqGSvISSUuH7WJniT8ebdG-FuV-jHeAvzNrFSd0OhhwHtu2f7t9cMm9eVq3eRtnH1eEnTNQFKm4YJXExdv3HSlvhcNWlG65pqLfs1UGPI5hCUb_5alcaR671OpUBUJtUl8CsfPxoIPctM1t_3oJRInfIF-NqCRsH9Ib6d3TwSg0U5zskPSkFG4ifBSukdRyTEYMYOHLx4zIhBfVLo_oItRl9lpUgvKKUaZteIPyd4vVEg5z_5U60iWaXsbgsC1ST5Hr9sPzM1MVwt-rbN2eQQiGWRD0ZfHFnp3ysbqtJmLDaNF9XDjtynuUwX7Z_gCPg2NevsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=mSl7-pZNuLVQgDVCFwaZ3nkPicvCYMZHKy3yuitS6-eD6tBn60wy_Hn4vzanu1zPYJ8YkPiXvPbCQ32t-gtdYRdDXVI4sEUhE3HPZYt-1AvKJEPuIeksh1PHKa86OmSerjCBRKejAKfj_zjwu_fR4kTvVfMcnQhdR_HyMcUy3i80Xo_1weGfq-ZsZkv1TlgwMJQmygHqLBGkXPvmbLgsOME7he6CamdhZty-wxO69LYr5pw0M5CBpj9UJpXhrPpG8HsJRk00VDYg1g7t9gLyd6jwK30flkcM93z7EBOTbfDoE7YsWoA5-GBMHsRon91rQSN-KHMvgoPvbt2fxYSjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=mSl7-pZNuLVQgDVCFwaZ3nkPicvCYMZHKy3yuitS6-eD6tBn60wy_Hn4vzanu1zPYJ8YkPiXvPbCQ32t-gtdYRdDXVI4sEUhE3HPZYt-1AvKJEPuIeksh1PHKa86OmSerjCBRKejAKfj_zjwu_fR4kTvVfMcnQhdR_HyMcUy3i80Xo_1weGfq-ZsZkv1TlgwMJQmygHqLBGkXPvmbLgsOME7he6CamdhZty-wxO69LYr5pw0M5CBpj9UJpXhrPpG8HsJRk00VDYg1g7t9gLyd6jwK30flkcM93z7EBOTbfDoE7YsWoA5-GBMHsRon91rQSN-KHMvgoPvbt2fxYSjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=NlxcDwdQlOnTsPz7VqSy5kqrI5aNrZijwu26OWwjyBGlDB7Yh-YzHfR2x90TSkIYjJGRN6lSTcH_q4CPwuHGlcSTt6jiq5ygNaeDRZuNZ8--4R6FVm-6Wfw7EtXZa-2ZBSl-snOYdo8nslQ9YiBpR64xAZxCsix22Cd9nx31lXyuDz05Fye6zOKxgBMMrzjw04nIqsuEoKRKA3CUEU1E7sU9AoIxfbD4xFNWg8ecgtxL9raEWsSloUwu9DYKIoV7LmcaZTba7RjZCDlxOaFPBwz8N1a-96do-KacvretjcISFtfKSaSK8ll3Y1vvfNrbeNrM_INb9_RIi6S-jMXT7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=NlxcDwdQlOnTsPz7VqSy5kqrI5aNrZijwu26OWwjyBGlDB7Yh-YzHfR2x90TSkIYjJGRN6lSTcH_q4CPwuHGlcSTt6jiq5ygNaeDRZuNZ8--4R6FVm-6Wfw7EtXZa-2ZBSl-snOYdo8nslQ9YiBpR64xAZxCsix22Cd9nx31lXyuDz05Fye6zOKxgBMMrzjw04nIqsuEoKRKA3CUEU1E7sU9AoIxfbD4xFNWg8ecgtxL9raEWsSloUwu9DYKIoV7LmcaZTba7RjZCDlxOaFPBwz8N1a-96do-KacvretjcISFtfKSaSK8ll3Y1vvfNrbeNrM_INb9_RIi6S-jMXT7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=DEJnCqf3548-JaBv-NjEXP0GI4yMGSbNTEYxv4QrNDcIahAa_F0wTwveBTHxLFbEmjFwYQQLEKypDH72Jb1l9OfTaDjsqEcJPkHwZ96dw7hDLB8yAX0RqYNLdCZItohW-1IZnuv-NW0bfd0WPcgP0RqxFgGAyv7LhcHIS94rG0QFjEOwR3dWDnUYmDXV0wNOPoLaj-8T4Kn_xW4F1LHzX6rWZzG0ySmPqkrCcw4DdmTSmmOnJpPjcZleYXfANUOFYUyzQiH2boe8kBjsYmg55Uj_R0Q3D_oeSjob_joIrr3PRrIscbWBjWz0U7_WhP9x3Oqx8bIihvmFu86ivR3DNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=DEJnCqf3548-JaBv-NjEXP0GI4yMGSbNTEYxv4QrNDcIahAa_F0wTwveBTHxLFbEmjFwYQQLEKypDH72Jb1l9OfTaDjsqEcJPkHwZ96dw7hDLB8yAX0RqYNLdCZItohW-1IZnuv-NW0bfd0WPcgP0RqxFgGAyv7LhcHIS94rG0QFjEOwR3dWDnUYmDXV0wNOPoLaj-8T4Kn_xW4F1LHzX6rWZzG0ySmPqkrCcw4DdmTSmmOnJpPjcZleYXfANUOFYUyzQiH2boe8kBjsYmg55Uj_R0Q3D_oeSjob_joIrr3PRrIscbWBjWz0U7_WhP9x3Oqx8bIihvmFu86ivR3DNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=WF4mLTc_7M5gsN2wRX3uJvA6o7TGBPKsiZImu5Ypf2WKvv6JyiVqcqEBYGukjf_EFoJqrlHqyC7YP8ASWRSU2563mt2IZ96_YkkMm4JPCag2pnx2X_yTb-MFWFwjm_xIr7ofoCfybVIiwdmkaRQQP1FO5sNpdGmomXcw014sv5er-6TKkyC5sfeTlppLgkiNWMhL3f-xAjWeZ0QU7c3ckxCa0i_cBrSnsNR-HCuX2WezJMKWeH0gvDuQSwvS3EcjmbjDFYxMXCxaNrgx8X-YYEbRpoJmGqO_721Y0Zsnmuipc0lRsZxIbs4DuioBCcDJDrv6hRtTQ-pkbiIfg2m2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=WF4mLTc_7M5gsN2wRX3uJvA6o7TGBPKsiZImu5Ypf2WKvv6JyiVqcqEBYGukjf_EFoJqrlHqyC7YP8ASWRSU2563mt2IZ96_YkkMm4JPCag2pnx2X_yTb-MFWFwjm_xIr7ofoCfybVIiwdmkaRQQP1FO5sNpdGmomXcw014sv5er-6TKkyC5sfeTlppLgkiNWMhL3f-xAjWeZ0QU7c3ckxCa0i_cBrSnsNR-HCuX2WezJMKWeH0gvDuQSwvS3EcjmbjDFYxMXCxaNrgx8X-YYEbRpoJmGqO_721Y0Zsnmuipc0lRsZxIbs4DuioBCcDJDrv6hRtTQ-pkbiIfg2m2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYCDizrkm7F0QVQGygRuz8lDk3HO_q0O9LdnTwIcdRvn7VmIIcCuKkjkoRPi8wSJEW4i8BSlcs_Eeb7fdOpLJWzgKPF30bIRHG0f4MKBAB_3SmalopIdKLqUKY_dCvhpVJvv6PmzH2t4DMC7f1DUwaynmNM7E8apSNcN_oUa56Dy6PBRsu53_Mfu91X2OrWwIXOS7X9A1fl5BlZspgUMq8VhZnqYY319HPJzKhnp77Orz5e7ORcwdLfoaOa-0htLJ70uzE9XVVP8GyOWEoCjIF-8M2VDT3AkLenUEnEsvr2Xo5nybgx8cIFR6f1vXNRzfY4jcscyoD5dlXZYAOQv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=iWJvxx-JqrMxyM48BJ70lWBvZNBy8Rv9eOvydf7UPMFp5GnpnXDRHGZ1DQILyzf4iFSyz-kLwMXFObXeLrqgWD5XJKH4KfRU6wXOjlnYM9bmryeZyu8eArTX9HzuTqd1mO8-67gYv5719cbFJEyOUSEI0LIhKT_y2XVSx9vrucXONMRzcuXLqthVjjU6GXmjS8tujqel6y3NjUsUKu6ibBWej18_oZcjSygN1HzyyNoWu1JjA90x3z-LMNb8YLlcp9p0OPgFfbiY6LPPbs45_jVrOebRPE_GEvqKdF24PZ0x0MhJ8h-16lQA6-6vjIZey0G8oaSuWW7w5NYFAPuytQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=iWJvxx-JqrMxyM48BJ70lWBvZNBy8Rv9eOvydf7UPMFp5GnpnXDRHGZ1DQILyzf4iFSyz-kLwMXFObXeLrqgWD5XJKH4KfRU6wXOjlnYM9bmryeZyu8eArTX9HzuTqd1mO8-67gYv5719cbFJEyOUSEI0LIhKT_y2XVSx9vrucXONMRzcuXLqthVjjU6GXmjS8tujqel6y3NjUsUKu6ibBWej18_oZcjSygN1HzyyNoWu1JjA90x3z-LMNb8YLlcp9p0OPgFfbiY6LPPbs45_jVrOebRPE_GEvqKdF24PZ0x0MhJ8h-16lQA6-6vjIZey0G8oaSuWW7w5NYFAPuytQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=r2yQae6oEcArODVBh38Bkj1Fd3deAh-EIy67Jv-J3-L_1cdjLHjO0HVYW-IA0-QDZrK8SZVPvzuvI6YCnw4jtQhZ--QHXI8W2eB0XxoDVM9ha_M3wXzSTuE7SUnx1L4G8zmvotCV6i8QYI2h061a6FPVewlsxkagtDsGhRhdgCxC7g29hrgTzVhAxNdAIy3sv_HA4Gnd-xVrfEd1arYiUXczpGaBjafp_GxhJ3Vhubc1jJZCvsH9UCXPTZGSmDaPQEtzZpciA_oA_4RjLM1cs2Kpg5dYagfTuhrcH13BLVMB4ruHvKiKhR38Bhdksu9fea6S_UNZejuyLYey4o42YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=r2yQae6oEcArODVBh38Bkj1Fd3deAh-EIy67Jv-J3-L_1cdjLHjO0HVYW-IA0-QDZrK8SZVPvzuvI6YCnw4jtQhZ--QHXI8W2eB0XxoDVM9ha_M3wXzSTuE7SUnx1L4G8zmvotCV6i8QYI2h061a6FPVewlsxkagtDsGhRhdgCxC7g29hrgTzVhAxNdAIy3sv_HA4Gnd-xVrfEd1arYiUXczpGaBjafp_GxhJ3Vhubc1jJZCvsH9UCXPTZGSmDaPQEtzZpciA_oA_4RjLM1cs2Kpg5dYagfTuhrcH13BLVMB4ruHvKiKhR38Bhdksu9fea6S_UNZejuyLYey4o42YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icxYaxT0dPbYtk6Ex6DJiTIGM33z2zh0Gae5ldKlw6uB7EGb9E8Rv3B7fFu-mkrK59Gy4PSM_ZxGM-xZ-RfkFLsNzGyXa8wjKpn22kUKKGcpJijQl9Fr_dWZDdbHGY49uwLopaUj7JNkZ4SbGuVq6NDVm_SCc76v8YRIDtjrdsz0O8KT2YBB1g9o4kfT0L3Pw_BCVbfLc-t7wFXzvwKXHbf8_qfq2SFLMTsk07jQ_JqDDe6oYshl1VvFncGeH3lCE9cmle2V3sBX82fhxtH3ToWKyNeCTuo9R2Co9c-2joLPP4E_ZmmmaiDnrkDAZH_R8OjsH4EhW6-7LmfaPmf7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2Bytnx-JfVnaEo-4uyRYhFQNMi7Zc30JVlMSC_oVWkt9EhG3iunWi7jeBLufd806y1-voY3xna4mbyLYmaZVY80xNaiytoDdyCIbFs1yAVEZMbTWER3Ol1vsAffIlOca0meS32LOyGcD7A6G77tdrseGZMNflqQJjv2aQuE1cfXpttbBrxv75Pt3rShApg1BLAIwg939ZscvsDR_ptso-h0BhjQVIv5JrQ0gryJPqCkRaVNWCJKT1OMt2UZJJ6RqT-0n8Ks7U9D_GXGn00Eh4qtivukcr_iiPJMso5JTCV1QLdbbM5I15Ff-mhsAMhS-tZk6399vL8Ro82t5NQcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMMB4Bm5kr1_zorJPOi0MCcWf5jq53bsPm5V6QD66n7ZotwBUmGhEcUl5W7W7pXrDhSG4xb33xCInPGjIpEyPwwGmdXCYxm3dI3uKXMAALDDFXHPFdCK-uvriTA1ed3lPraE-ZEm_TWORFJnTRAtdR4l4-_A95i9bhlMP2y3pxnjILwv0CDOAHV-rXDD6v1ihMRFhqIfM6bKmvel0Cqh8TcLO4GXnRhYtAow4M2RoBB3_nIKHrRi9IoR3qvkbaNDWFugmJWw5bbei6S_5_8m-v315EoYKhjcvHCTaLHa9eUGS-1pHXEct6Xzi-PNDpUbWlaMLkY8NUV8xOj390za9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=JxsmW1O5EgT39huAoUIZmEjW0tNIq0UI3r1zQEqLxgrQRzGylseU2Xp999zJwpKTHsMpb3hoNnlaHzk3kp8UyqZifJCiRxKiv2nbOusyNVb4eQuC-SuvPFHJ47nwxK-TGEx5BhGT0wUT7sCpbHebYwscS0rPIzp2A4sZDh0ZxhLDUwAatgHAa3qprwlVRkzn7mFv7RfJWvIrbkYXpuqa3IfC79jqNuUx0ePY3uyOnkGJf_wy730TKh8Ech7i2zYuvOc4uhJkCyFYiKSLghBQfeWkmfHsPTpGwcMZeD7M6pwodcmqaQn0kehM7l3VR5W2_em2lLPyJhS1jA3l7aKv0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=JxsmW1O5EgT39huAoUIZmEjW0tNIq0UI3r1zQEqLxgrQRzGylseU2Xp999zJwpKTHsMpb3hoNnlaHzk3kp8UyqZifJCiRxKiv2nbOusyNVb4eQuC-SuvPFHJ47nwxK-TGEx5BhGT0wUT7sCpbHebYwscS0rPIzp2A4sZDh0ZxhLDUwAatgHAa3qprwlVRkzn7mFv7RfJWvIrbkYXpuqa3IfC79jqNuUx0ePY3uyOnkGJf_wy730TKh8Ech7i2zYuvOc4uhJkCyFYiKSLghBQfeWkmfHsPTpGwcMZeD7M6pwodcmqaQn0kehM7l3VR5W2_em2lLPyJhS1jA3l7aKv0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIQM-uPy12KcyYUgBE3mioISFRhNqun5z3f6disfdg44e3bYVbWojHThe-CY98_dScLumV5cced1GZQVUMDXeYDe_z3i6lZu5l6tVgtMxO0nDv5CZ0dzmbPQy81CeBTvkaWyAb9dFY8lnxrx8CXtQrdRG0ksYi4gG9mSBpLItMqLxgSKup3ruOArsuPQvmJhmfJlrJO9Cb-S5WxiaUAsWjMnd-QyCd-hXq_iCr2Bz6epsViQAK7D_nBDenYssmCGRf5q07LC9aa6q9CPPRKlaFdZAGEPB-jWxXyhwpdgWKDz3FRrbppX8xhpWtqXmblmP19YcASm4JHbz3h1yx92bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=LQlSYHueaBX-cPCcBsf0uzgqMw-93j2Fa_mk5_pOjfAN9mpYPJvQ2N7Wydx9c2KYGMBvd1VkALBKCoKlB3IElxfo5EYtT_hjpRggojLYeOShrIHJ55vj381C4UXNzh2bXLSGyyYGZI1T6qLqatzldWaqFYwbwteKzGrTL9LxaFGDTo4LNNtOC_mL6cG1Fi54iZPfXDkuO6R3zlY5X2e_bzK-aiJ5E4tWJ2K_2uMXsXe87FEpN27JHqKsmC_dIpfGvEAMA_kqGQL7AAyXUr8lYc9yHE_m87xgpTCLCyTzm_pnOQf_nta8yXn-QheO4gBR_1_5nd0e8VJAGRMUJ4U5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=LQlSYHueaBX-cPCcBsf0uzgqMw-93j2Fa_mk5_pOjfAN9mpYPJvQ2N7Wydx9c2KYGMBvd1VkALBKCoKlB3IElxfo5EYtT_hjpRggojLYeOShrIHJ55vj381C4UXNzh2bXLSGyyYGZI1T6qLqatzldWaqFYwbwteKzGrTL9LxaFGDTo4LNNtOC_mL6cG1Fi54iZPfXDkuO6R3zlY5X2e_bzK-aiJ5E4tWJ2K_2uMXsXe87FEpN27JHqKsmC_dIpfGvEAMA_kqGQL7AAyXUr8lYc9yHE_m87xgpTCLCyTzm_pnOQf_nta8yXn-QheO4gBR_1_5nd0e8VJAGRMUJ4U5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=J4xZAqm4bidhhXw2cNLqghjjAJj21RgX7EpLtLfvuT3Q-smZfkcupOQdUUIA3bj14rlMHdlNXn1JK1kmo3-qU9CYCaaW2MWyIc5g8xNtIqLaxEVBSIkq23qVgh4we74aSG6o-9Zoa79jMGdU323OGuUp5EzFZMzrABNyq03L1tOf4izN8dxrnRIgUOdmPt4QQ1_znCzlLjAHzwAef-RpQoU_HW-CP0udCFTVj0B08duYwXjaClA1qt-zmRopB1TgL0erIIoOkpQBvfG0juGvRu_1dXMAGDyc0Xa5HV8zPgyNcFVVvIWJcGbnXvN8CP86osyR0fi8ngIPjYyhPNp1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=J4xZAqm4bidhhXw2cNLqghjjAJj21RgX7EpLtLfvuT3Q-smZfkcupOQdUUIA3bj14rlMHdlNXn1JK1kmo3-qU9CYCaaW2MWyIc5g8xNtIqLaxEVBSIkq23qVgh4we74aSG6o-9Zoa79jMGdU323OGuUp5EzFZMzrABNyq03L1tOf4izN8dxrnRIgUOdmPt4QQ1_znCzlLjAHzwAef-RpQoU_HW-CP0udCFTVj0B08duYwXjaClA1qt-zmRopB1TgL0erIIoOkpQBvfG0juGvRu_1dXMAGDyc0Xa5HV8zPgyNcFVVvIWJcGbnXvN8CP86osyR0fi8ngIPjYyhPNp1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=YdgQzL6lSgoQ4_9-j3avo_aH9ugoOntoBkWIjCIB2BRvoRTGbMFVlltvDaLouWo3SSME1nyfnyR3X-ojtmVnTWcqC2CUEtACYHaZoiftCzbscYIXljMg-x289Yr_5ZIdJtrjKj4po2raGbDPUlgRzHP3CttUfMqGEQu4mLFvtJC0WxAJMr8ASEsoDQXLZBNVNiOQYoNOjpRoYLAV-huez6PpcGSOaLOirAwt3zF5Nf6eyVlMbV_jQRtlOh-vDBpPhxj5xbEUeIKtPaZ0FLnwteHLyqDnbevs8uokuWxVwB7K3aHidJBak9AO1U1YADsnb7sw2E02Wiz2ZIvAP04LxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=YdgQzL6lSgoQ4_9-j3avo_aH9ugoOntoBkWIjCIB2BRvoRTGbMFVlltvDaLouWo3SSME1nyfnyR3X-ojtmVnTWcqC2CUEtACYHaZoiftCzbscYIXljMg-x289Yr_5ZIdJtrjKj4po2raGbDPUlgRzHP3CttUfMqGEQu4mLFvtJC0WxAJMr8ASEsoDQXLZBNVNiOQYoNOjpRoYLAV-huez6PpcGSOaLOirAwt3zF5Nf6eyVlMbV_jQRtlOh-vDBpPhxj5xbEUeIKtPaZ0FLnwteHLyqDnbevs8uokuWxVwB7K3aHidJBak9AO1U1YADsnb7sw2E02Wiz2ZIvAP04LxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Tk9H2xyG7qZdF1Bpd2Pn-XzT1m-oEg5R3e2YSCndA31DLL-3Q7vCtk2EHoUQvAiHol0J9EJVq5WTFqwboj_WApb6NTXnEzlq_p8FCxsy7RANR7rM7G6-XS5eOytQCTi3x4WktQbDh9zkC89prVn4JKg383U9uxAun-p0-Jjshq2HQCBbe85cCQkm0v4deBHOrIyL2tRuAYW3CTw-Blt3zO1L-EQfIOsnLH72GUZYLlR06oG9Dt9WM4I9yDjGJpzDsDG9OAt3ojk-Io9HDE7bT-cFV7N048tpvxQ4PUM8zdS8i0avrJUKq6G7B_LzsbTqd2dODzEy-RMgT5KKLve89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Tk9H2xyG7qZdF1Bpd2Pn-XzT1m-oEg5R3e2YSCndA31DLL-3Q7vCtk2EHoUQvAiHol0J9EJVq5WTFqwboj_WApb6NTXnEzlq_p8FCxsy7RANR7rM7G6-XS5eOytQCTi3x4WktQbDh9zkC89prVn4JKg383U9uxAun-p0-Jjshq2HQCBbe85cCQkm0v4deBHOrIyL2tRuAYW3CTw-Blt3zO1L-EQfIOsnLH72GUZYLlR06oG9Dt9WM4I9yDjGJpzDsDG9OAt3ojk-Io9HDE7bT-cFV7N048tpvxQ4PUM8zdS8i0avrJUKq6G7B_LzsbTqd2dODzEy-RMgT5KKLve89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C210IUSQPHmJrC0gHd6J40wi18_0DQ_Dd6BhKb3cnIjAhlUtpkoQg80Q62fOjF7tS8cblSsaJb5CYjuRssu-GAEoDmdJXcBHGlvQN7JzzAMYdLlp3GLSW7DzvF-0CUVjIWoRh96rwcO7nMJztamMoVsY1okB52jONOZC_5Id50unheNuA4pssY5mIHyeWzJs-WXuFO2khaOGD7IimuQrquAZ52ZRJWpGtV1c2y0XKsyNHiE6FSNbZMUyTDF_DaQFrm4w3cXo-gwIWA0NN_hLMB_ts3qjcmVPsE7aUDMWSWlRUM6Q6ONHYZOfLFdXnJhnioMqUctZVEnsqb_YQuB5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNcoPS50F0sYADlqbDiN-3LaXvD32AzvGmd-rt4QAV-FHU1OoyHRDv39BOr2Gl44qM5xq8oVr6F0pufSzEQ2liUFMsHgW6e34iNXrC11HmsPptFJ_wHNt7mU-hn_isSiUPOiZEA3d71_1dHO8HH9XmtFNXgxbOlqQxAu29JE41LFzaPlsDG9BymSx8yhgG82B-RBCEzIYskSFRZWaOnOoabDh2d3Vo_wz6r7icfFh49eUNlkPAkvKwIKTUyRSz8s5A0AxEH5Tioy9z7WVH2vAk8XgMkDsLlx3tBHSJfGabBdzPKN6pR0HlSG5IzsUxtAjCrGLLSjAvWnDXjIKo8JCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=eK1YlnYAPK6X7bno0JjDP7Rm-NVer74xLu_puONCFoD05Y3oC4xm8NUGeC4VGpMlOMK_F2HrngOMBWoKVGzY0hseWkyfVLXbb0Eb7QcEQd-0kXBerhft509p5Z20VtGIgBeFwWl1MPag4-p6Ne7owyYeKZaxcku5S9ZyGWUftlWSku3zkH-dVUadWdtyuUuvB1U0UuIh7NigZlZxje6912ot_M3m-OPNXXvIWO6exqqbF7-VMH0vAPKJbJ_jUKz9-wHpuip8We8F9OOW0kvmoL9f62YKFgZw3ifbAHQTbAb8aJLHqzlVAcV9U_rC44JjFuFvcmAfpoMHEK_Vvb_kdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=eK1YlnYAPK6X7bno0JjDP7Rm-NVer74xLu_puONCFoD05Y3oC4xm8NUGeC4VGpMlOMK_F2HrngOMBWoKVGzY0hseWkyfVLXbb0Eb7QcEQd-0kXBerhft509p5Z20VtGIgBeFwWl1MPag4-p6Ne7owyYeKZaxcku5S9ZyGWUftlWSku3zkH-dVUadWdtyuUuvB1U0UuIh7NigZlZxje6912ot_M3m-OPNXXvIWO6exqqbF7-VMH0vAPKJbJ_jUKz9-wHpuip8We8F9OOW0kvmoL9f62YKFgZw3ifbAHQTbAb8aJLHqzlVAcV9U_rC44JjFuFvcmAfpoMHEK_Vvb_kdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=iS5c20PnR4aHpgYA8Qab4NYuegsEuzdMYEyNUzCPlvJrTJrK0hKA0r3OPJsOQoWzZyklGBWwlb3iQ6-F5CxC-EeEbL95XG89GJEFZjcCokSfjSV88JdlPmgfBMaPSLpsBn5wPMA2wEFsK0r-o6nUSueeJtrn8inSVmIBtNddOCr7P0_IZAh7lwFY7tmDPwU4BwLrHXgAVb14UvBbWRMQimQbh801ifLK6wX9fkFG5oRHQ8QV-e4T7tGVmb254dM-eLA7cThwKwnfXDe2Kn38ZWf_i8bCvjZkJpeFKbXIcrhqMu3GvMPew37w8Lom6M5WAVz2P7Vr48O038d2-JY9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=iS5c20PnR4aHpgYA8Qab4NYuegsEuzdMYEyNUzCPlvJrTJrK0hKA0r3OPJsOQoWzZyklGBWwlb3iQ6-F5CxC-EeEbL95XG89GJEFZjcCokSfjSV88JdlPmgfBMaPSLpsBn5wPMA2wEFsK0r-o6nUSueeJtrn8inSVmIBtNddOCr7P0_IZAh7lwFY7tmDPwU4BwLrHXgAVb14UvBbWRMQimQbh801ifLK6wX9fkFG5oRHQ8QV-e4T7tGVmb254dM-eLA7cThwKwnfXDe2Kn38ZWf_i8bCvjZkJpeFKbXIcrhqMu3GvMPew37w8Lom6M5WAVz2P7Vr48O038d2-JY9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTGYue_dRYRzTKU6PEHhK2TAqucF44vGzvkCTwQsQ2_1Et8kyXbj0ses0z8OtUXSNpwf1hjWopWxqn-G8KwJs5M44J9-FThvMeJZZTHu8PSlSS5TT60VrjF7GJTgwZLO_3DKk_cWiXMl9oRYxErR2XDbUc-LznFJIJySmk5urLU81j1gVtY9N-rcIEDbcuq_bveKU4ChOdrVmhzJVFi1No0j20RmXp7cMoHK8v65aL3D70C5dpqMo9Zx26eELNHKcVIeU7dWQ9DZpplecAMtJuBu0-zTCtsHMriouoUwX71stKCbZCQ9Mvt4C7gzULbf4L4X09yOm7H46RhGLtnilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=DLRrmGBYG9rU3nJ0aVPQWIFbS5bXRmszaZM74NrR6cdlL3oNot2GXvkzXUNko3foH0hDkBV3L0FHL4y-OSPrio2YPnOBIdS_umRiPfUL764c4LY6Pvliq7nKtNDFNiIhF4dUIrQfMr7D6ryvJGJ4JT1467Q9cD3Hu2bH7wKMJzlP-9OskXDoOkC_rahs-jFtLk9TulEhUnpwzVU_6On044HE61u43vqDyIbyelytwTMvrc5HIopeVjDNCCaFylQVAiSX84OAcDLqlaKtTcTzg0DO6OCq85VqwGioGf63l1har31MwNTwfiBqg67-vizOLh4KNxO2hSrL_x3gPJ_kAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=DLRrmGBYG9rU3nJ0aVPQWIFbS5bXRmszaZM74NrR6cdlL3oNot2GXvkzXUNko3foH0hDkBV3L0FHL4y-OSPrio2YPnOBIdS_umRiPfUL764c4LY6Pvliq7nKtNDFNiIhF4dUIrQfMr7D6ryvJGJ4JT1467Q9cD3Hu2bH7wKMJzlP-9OskXDoOkC_rahs-jFtLk9TulEhUnpwzVU_6On044HE61u43vqDyIbyelytwTMvrc5HIopeVjDNCCaFylQVAiSX84OAcDLqlaKtTcTzg0DO6OCq85VqwGioGf63l1har31MwNTwfiBqg67-vizOLh4KNxO2hSrL_x3gPJ_kAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=ReS2uwHvgr-WNk3n_KjS2LzTThPQeD2VE3mFmGoMVD2ymxsJv70oBlAjOPWG4d8-4Tl5R72qkfguO5wqGqJBu14mAgRSIARptorGTcUluhUS3OELWxZV2z6yOvBtZBZvYA0s7szK0tP7Hf3KeRVIqRHzXqXnOvA0GyMeLyiZAIhIdn0bLLsE-bEVyYyEZLz_2I_kHTEhQRhdPtfRauAOXJ-_fVKQGUUeyapAhqJEHnwzHz3qypO79Z29n3RpOsAPyuR6jzvaSXMKhTFdyZhbHr_m01lyOCu2RUY4Eo1ZTx0G5poiyeybMfuSYIE8we8zEXWZZ0o_KlBMOPHcesXdTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=ReS2uwHvgr-WNk3n_KjS2LzTThPQeD2VE3mFmGoMVD2ymxsJv70oBlAjOPWG4d8-4Tl5R72qkfguO5wqGqJBu14mAgRSIARptorGTcUluhUS3OELWxZV2z6yOvBtZBZvYA0s7szK0tP7Hf3KeRVIqRHzXqXnOvA0GyMeLyiZAIhIdn0bLLsE-bEVyYyEZLz_2I_kHTEhQRhdPtfRauAOXJ-_fVKQGUUeyapAhqJEHnwzHz3qypO79Z29n3RpOsAPyuR6jzvaSXMKhTFdyZhbHr_m01lyOCu2RUY4Eo1ZTx0G5poiyeybMfuSYIE8we8zEXWZZ0o_KlBMOPHcesXdTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا ابد موندگار شد این سکانس
😂
😂
😂
😂
😂
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=NEuSMcbqL5hLjFzhTfBLTWeQCQy5GU-0EAYW888wrMATGR5zPry3OcawRE4hrb7YMForlwi_qsiqzS3MzU1fmxv2J9nV-aMhENypmlDXuWTbSmwaJamZcJr6Q63HSsrqZ2-9FUoK1GQXIttu6cytBWDHDo_vGGUe27pAoRD0v8Orbs4YppETadbIarfpvMq6Yz6cFgnGPUMsCiLxkMhcO-r-eQzn2aW2rP00HwJAD-MUKiot3cdKmjPRMg4UKQIogjbTCIKNoJuAsBsIUdzf2nuhxzWb_XsVBfFBLVoWq9CI2SRDi-NHwOqtHfvQJ3ql0tkTWC0bhIA8fc95ky4-dw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=NEuSMcbqL5hLjFzhTfBLTWeQCQy5GU-0EAYW888wrMATGR5zPry3OcawRE4hrb7YMForlwi_qsiqzS3MzU1fmxv2J9nV-aMhENypmlDXuWTbSmwaJamZcJr6Q63HSsrqZ2-9FUoK1GQXIttu6cytBWDHDo_vGGUe27pAoRD0v8Orbs4YppETadbIarfpvMq6Yz6cFgnGPUMsCiLxkMhcO-r-eQzn2aW2rP00HwJAD-MUKiot3cdKmjPRMg4UKQIogjbTCIKNoJuAsBsIUdzf2nuhxzWb_XsVBfFBLVoWq9CI2SRDi-NHwOqtHfvQJ3ql0tkTWC0bhIA8fc95ky4-dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNwC1MqG6G_j6wFr9tiskWRusjYJCOgogSqhXIJga65P_di3PR7qWc1U9kYYjI9WyrGkkrAeEWXEBuiYnPeM7sPiO2dhjWWB0UfrU2x2RuXvy_Bi7gUd0W13Qm2ZehQ2LCfUX84rKekmFCHBgIr_gbIALDl8xM_nWxXqhl7Ymubvexlc53aVHvO8ONOHzkRg6s6LrtTe8i8nyRtG_OPp6-UROhLyleAtc7V2z1rG61rA19-ncSe0_15SapdmkbWTxvb1vfyT0AAbSTP6_mQXojT2R7PmSZleN-D9-8ONIm6CXvjIhOMvRzzbHeTj4N9sUcI_DtbVQpj6O1dzrY1H6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpW4jnUmOBYWHdPN6ExhMfdxNhIgV4z2CbUH02YA298H6uDCeaOu2CTuI5MH92PzROW7ofARYE05jHboOml03gQlB1vgpABh4fuCUAbraseXTuL-5ov7zQW578zOazD5DKxB2IUM-Ugyspofi_y2U0FlNdpWgVw5IeWnyoPOQhzAvk8toHCm2C6OSWhr3TVOfIxhP4wIH9cHPNp59hRM2LLliqsWF8lMX8HdGp8e0fi1S3a4ff8Ig1FTtiPwl-lZB0r04Q68EaHMh6txcHFkm-XFcMJuxpz3r7Oyoc5yHmApzCzXj7j-x7VEKmxcBzOcZnJALBGpuB2BEBbtmkvexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای
😂
😂
😂
😂
یکک دقیقه مونده بود
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
اتریش
😂
😂
😂
😂
😂
دقیققققه ۹۴
😂
😂
😂
زدددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLUw1KMM1MqhWKe9gNNS1zVOGDIbwAgjQFvt_hCJmKxQsEbHN_SXWB_Q2_3diH-jCp9x5MQLfDLuAGsmIXVfdRNM15iiebsEqGa197YbhTuT4yz0fosivWS7KNQX9Cydnr56VJa9QcFErj_gvuREsWjE9Xd9z07vKJaqhcIGmKVblua1PNBAJiF8oENf8OCJYKhkOMcS-n-3HoDJwxSqG_gBY8Cp-LJ77gjBnexZLBYg9No50ZNGgXtQBqoksjDcBaF4E-hom4HOUJ9ie-gy85v5I3mG7mKFLOQpuafhZAPWgV8K487HsuU2A2UBw_A-CNtAhXFFCyCoz8jJlkIe2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iw84z-g3D7O7DSbEJA3GTowrcLaaCvGPtZJgrH3z6ocSUSLogAcBN4wlM3b7RKp1AM5N_qn-32UoU5Z5u8BXtmxKTlOLQi4iqQz-bqNQGVKrZQgsIkHalGBXHKLJxLWJdQvUpdqIYThCWMxFUa3XMAJ5OKIlz6srGE_SBVvCRQXugQDWAqad3ZjgIMYhuQLYFMCdyYpsrytDATCvm6jikYVvGzleqlt_rgZFsEJjAPOOMsvL42bJDJqSOa_gqQ_hnr0WfeHufelzamYFKQAv42GKBYIgXVdaBMO0q50zHf8d5dsqwi4NUGdji8lzWZh_Y2x9uBqMR0F-0fg2kLeJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=rwT-ZtoSpywIUHyaO_OQIeaeHIH3LIm-Dx-5-s7aJiEwNKMmapdymcCuRINFlPkVnjR739IaSNIdURMaD4cEkREZqmkXA7lSTDt_Wz8bSTkWerwZmKrUPp7LNsYkJGUP-BkiMEVBo40_CT5VMFxqQ64G-rJ9BpmxpVBNaw8tEgxv3Y4wG7kaoXJSxqPeXCgoxXErCKE3J8wzFE0YoK83DWUkFIagEiuvusudJWOLnZJFY5JzftrjwRI-j5aDbQY9jajAIgShI2Rcl3-IInVkZu0WaqaPhoXcVyhLCIwA8EuCXZGHDKbnuSxUFIrhLCzBrwzvFxsLVDXDCfrwzsdlhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=rwT-ZtoSpywIUHyaO_OQIeaeHIH3LIm-Dx-5-s7aJiEwNKMmapdymcCuRINFlPkVnjR739IaSNIdURMaD4cEkREZqmkXA7lSTDt_Wz8bSTkWerwZmKrUPp7LNsYkJGUP-BkiMEVBo40_CT5VMFxqQ64G-rJ9BpmxpVBNaw8tEgxv3Y4wG7kaoXJSxqPeXCgoxXErCKE3J8wzFE0YoK83DWUkFIagEiuvusudJWOLnZJFY5JzftrjwRI-j5aDbQY9jajAIgShI2Rcl3-IInVkZu0WaqaPhoXcVyhLCIwA8EuCXZGHDKbnuSxUFIrhLCzBrwzvFxsLVDXDCfrwzsdlhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFOu7zTcAI9mi-G8m722o81RirF6DUSoWUtqSucEML7td6XQjPZmwjA9xGyTAtlt1lY7mjEOv5mMuwwGT_wlfXKYVyYhyUFjXMUKy-mluUuhByyeBvuLjhLuaJ8JKAG3XtAbUniIf9o7cU-tRzhWbzLnhcfMDShSm64dWhs_ICavrdehQmhZsR6iqP4ezaaJIhhJC6U6rWYEeUuOXlXzn-nGd5hTWs3F1rAd_xcmdPi3TNsdauPwQooj1cG4mXJ7xUxjcb27GVDuyVD89iHNT7yzZQ7SXH5qnNCfDXfehTAisqi-XRRsGQyC9gGv4vWOFIuunS180aHuZMgZ77I47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AZ6i1v4hP5STnG18rVt6PEFwTMx-E0ELwoJf5aaLudBMmkWVi1Jw7iJgUzCZjNOvX8nTnKJ0Qu666dSGMJP1wwUbhVztE6CUtj2tL-NhHmmSI86PD5VzuRNOJmmjDIrFKYVHIYRm_0WfGcNXSNIdWE3lSgBb7BaoL-SacUqiTSenIZbnalyTiBYMknfn756eMFrCtqD0HJIDgF1J2edkWc8YYK6EpDX-QcHJ1UtoBc-J33qjKTv_mQIpDrpAx_xKhPbBbcfx-OIfZc-zNTEnXzk-ZMsXkPBZW8qX9Bft3BjLRe4xvMVo446LN8Bb1BPHXxn7ExOa3rvJ-VeXA3ANxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTFXPMoEQ2Ta_mpvwjJSib_2gV7wtUpYI78rfrP2QtJ7vOKs8nv8T5ztirBGSpRqnFPiaCZ3boybkzysvrzE-xZAdhKdSrek7apmrp3XRsGU9N2b8WfxmXv2QhCgpWpnNpzaTUNjrvgFPGKA1bzsM5mLH63PfAAhPzMhVEKY-ndyJlB_Hz5cxY1yAJlZN_A-en7zQwXwerK27Sxsw4ylxN5B9QspbJrc5T_am6Uz97EwwtMAbLCk6_7L4-GentomPCaw4EvOwor_xKtJGTafagszMDJ-_xZ-B3VMsUltNaxqFyvZyy0hXWg8ULDYJ47iezuILgIMmfWR_zapLisMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxlCv2p_hcmNQef-WvPl6sR6baSddWoDpcwNCv4nzmBCL0lpYBYbVCAns-U9Cj1wRCHJe03l3xlAV5gDyekMCMX35_YAdRe-zsAahn66OfNYGv8OD7XCC66ijXdKmshn0UN6VoZWSIYrJ-c946gpdXLckcAUo2Dba0jyOpbmTRzs-A9VwMKzO-1ER2Wth2xKaca8puQ3TDUX8_8akTCxCN_BGnzS7VOTHhfB05CucdhJZGJsrhf89n1l11If5XBx_USQikZLE4a32RMp0L9W54Z2c-pDe7e3I7Iz6kWnfmzUBD0_rPh3lZruKDn40VvkiZYYKVCQ5if4R3Ya-txCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcPlq5-bhVmesKacv_s-Pfu520QOac-6G05nswNpLVZdqr1H1rg6h3227rdHyg14RCrxd4_Lqrgx31HHGQDzwQyYCvzFkuGcOINwLV3WWggq-U_MYf1asjoDwFGXmxhERiofVUe_PJ0bJXFLG84oK44QciauRyhiATH7M6nAFc3XQC6n-FUNoxqXd0pTG88XL_fXFtFiEA7oP338rE20Cz9wgw4Bcao3kaeWzyEsh2Nyu1yN34gPuA9-TfxhFzqXWqaO7bJoKOV6Ysi8DNnKaD5lgBQPC8qkE3IACOCbWQ8ve4G0eO_mus8OBC5zSxxBpDrdXeC5xoxXLp3j8jt1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
به گزارش وال‌استریت ژورنال، یک مقام آمریکایی اعلام کرده است:
🔴
در جریان حمله روز شنبه به بحرین، دو پهپاد ایرانی شناسایی شدند.
🔴
یکی از آن‌ها توسط سامانه‌های پدافند هوایی زمینی سرنگون شد.پهپاد دوم بدون اینکه هدفی را مورد اصابت قرار دهد، در منطقه‌ای دورافتاده از یک فرودگاه به زمین نشست.
🔴
این مقام همچنین مدعی شد که:
یک پهپاد ایرانی به یک نفتکش حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز برخورد کرده است.
🔴
نیروهای آمریکایی نیز دو پهپاد دیگر را که به سمت کشتی‌های تجاری در حرکت بودند، رهگیری و متوقف کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=Lsb_lhz8bv8hYBdPwNv2h1k_jxz6Mk8sWpwczJFs3JSmmz4LWonrUEMWQ2L-sgWncDJ5OKX8FaTuqdY_RXg7u7Ti1Lb1SRhEEb0p_QFptwbRxscxkewhrhZP1M5ewc2nPFMAE9BT5jTncMk8TSQJ8EzotF6KMxlsciqUaYw2ujgyOj9WwYp01ee8jf03LSceKtlrmbUTNoM9ZuEwAhtZ5VDx3HOq5DhS_BjHF0ni-i-TMFbqiVagvktU4eg2dZ2oMLphF5EH4v6fTJiQrf0kwBBu3Mdx4D2r-l11PInuVRoAypJ_-G-SqEskEanBeajemEK2I6MCgluAG6hOpNvY-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=Lsb_lhz8bv8hYBdPwNv2h1k_jxz6Mk8sWpwczJFs3JSmmz4LWonrUEMWQ2L-sgWncDJ5OKX8FaTuqdY_RXg7u7Ti1Lb1SRhEEb0p_QFptwbRxscxkewhrhZP1M5ewc2nPFMAE9BT5jTncMk8TSQJ8EzotF6KMxlsciqUaYw2ujgyOj9WwYp01ee8jf03LSceKtlrmbUTNoM9ZuEwAhtZ5VDx3HOq5DhS_BjHF0ni-i-TMFbqiVagvktU4eg2dZ2oMLphF5EH4v6fTJiQrf0kwBBu3Mdx4D2r-l11PInuVRoAypJ_-G-SqEskEanBeajemEK2I6MCgluAG6hOpNvY-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=Vg2-gkrTKdBn9X47vQPACEuTqWGVYKY3jWdt5XoLxaarQ-hJxSAEPlT1vN5eyPurir2JJDFLRC_3nP5RNHiZTH8LslWlKtqsDGg_ZWYOXH4SKlxB2pJbmaL5P6fiyjFvR3oxSJM4VuFjUHOwy2iLFYG4k1i2_nAQ9n-4t2iKiCn5M4BPyhrcc1XCLdV4mUGcPGJfLNOduVaRxevD8CPi6HKGoZIERZQc_j_djcXuNJZvoaB2BBCFpm9yzB5nMAo4mD98CyYyV9ngzDE4qHNGcZfgr-DL0GYtpzav3AVdaDtJkkAjQwt6W2fKOm_BMR4kpHmV2Rjt3-4QJoo1gS7gaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=Vg2-gkrTKdBn9X47vQPACEuTqWGVYKY3jWdt5XoLxaarQ-hJxSAEPlT1vN5eyPurir2JJDFLRC_3nP5RNHiZTH8LslWlKtqsDGg_ZWYOXH4SKlxB2pJbmaL5P6fiyjFvR3oxSJM4VuFjUHOwy2iLFYG4k1i2_nAQ9n-4t2iKiCn5M4BPyhrcc1XCLdV4mUGcPGJfLNOduVaRxevD8CPi6HKGoZIERZQc_j_djcXuNJZvoaB2BBCFpm9yzB5nMAo4mD98CyYyV9ngzDE4qHNGcZfgr-DL0GYtpzav3AVdaDtJkkAjQwt6W2fKOm_BMR4kpHmV2Rjt3-4QJoo1gS7gaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e1890541.mp4?token=i3m14qgsJMcx6iLiZSCKcAbO_vH7s0PHm2xXLA4ZOCV9v7HA9IlQjPro32tqX4eOVOMIZhLbyUEkitYucbPAx_ThWzSeNMsonzsR7vzcxrQP-Ln_IOEpXw7AJEFW7k40_L1yHe5ScQYrQ8ElofkEx-75ctSdRCdoxSiOVklsGnscA_VMU4eqoI4oInOrR7PuC34bkOb13tfcXFsjb6ZcnEclbRh4wY9eywsfIn_m-90zjygclhjD0lQdGbcznSm_IkhTDSnBMcmg-mHKw4tarQWOmmtkxdwZRai6L6JY2VUZ6KqkWJimu7_HvFrll8h5z9EqLfFjeRcjuBsTraFXWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e1890541.mp4?token=i3m14qgsJMcx6iLiZSCKcAbO_vH7s0PHm2xXLA4ZOCV9v7HA9IlQjPro32tqX4eOVOMIZhLbyUEkitYucbPAx_ThWzSeNMsonzsR7vzcxrQP-Ln_IOEpXw7AJEFW7k40_L1yHe5ScQYrQ8ElofkEx-75ctSdRCdoxSiOVklsGnscA_VMU4eqoI4oInOrR7PuC34bkOb13tfcXFsjb6ZcnEclbRh4wY9eywsfIn_m-90zjygclhjD0lQdGbcznSm_IkhTDSnBMcmg-mHKw4tarQWOmmtkxdwZRai6L6JY2VUZ6KqkWJimu7_HvFrll8h5z9EqLfFjeRcjuBsTraFXWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف گرفت رو تندروها؛
اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=WbEd7JEafhtEtQE6UTq-BOdrEna6g3xY-kFX372DiA9RcjWpL6jKnbZKdzh5NprjUiTlLqgpGzmmaZWH3A7_2QIF6qpAjBoSdtPFHqtfNaLE_T048truEzbqOuIvwPCcHjWeUEUtRGHygz0x5doSV_OJlbb9oKVFEGJ6jEWw9spBcUQHJwVDxWy0YGgbo84pBgU2QAd1-V5_-x8qoUtwn17ZnXZrI3Uk10yRT1ix5558AD9XDyAwMb_IGFqvUKXDrg-gPOeK39-ReaRfwgNsaTWPf_W5dFo944QD_ggNsR0z40G7ZDNt0ekMPWyr9Ibzp_ly2fUnf2l8St4vy8yi9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=WbEd7JEafhtEtQE6UTq-BOdrEna6g3xY-kFX372DiA9RcjWpL6jKnbZKdzh5NprjUiTlLqgpGzmmaZWH3A7_2QIF6qpAjBoSdtPFHqtfNaLE_T048truEzbqOuIvwPCcHjWeUEUtRGHygz0x5doSV_OJlbb9oKVFEGJ6jEWw9spBcUQHJwVDxWy0YGgbo84pBgU2QAd1-V5_-x8qoUtwn17ZnXZrI3Uk10yRT1ix5558AD9XDyAwMb_IGFqvUKXDrg-gPOeK39-ReaRfwgNsaTWPf_W5dFo944QD_ggNsR0z40G7ZDNt0ekMPWyr9Ibzp_ly2fUnf2l8St4vy8yi9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66939">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=fC5Wn8iHRuYh201BtTbO1-AG6JGgDHhMSVbJrnlbEeEvDmBfSOb_Jhnbl0YY7e92fz4V0WNVeZFId0Cvw5ffNAxvWDZGxYYIGlsOk742p10YkNI7sbjmpH7fLlgX0kYk7J8bYKQlDZXgNt-Xv6ms9EJjzFCyfDoUo9DrJvu0Dn2ZNx2V2-Y8OiuYHBFiGM0z7tdZefO0hqGDkuwiXvOtVZKq907tJz7PHN5VRsIrv6tZBQmxyymEdl51l2B8bcLvVRo50O-ktBkXA7pAAbpVlgHdi9vTKcSbeb8MGiWeEZkRwZzcGjyw9mvmuJIa-UuC80cXK8Ze96Gjr2c1RkooqrK4dkrCogSAo_a1ggUDguRg93BXQtyx-G-uHLooTAKCsTzzU17DF4qdNqes8EBk2BduSL4mecBdOZNih7zJaqrwrBBq3pidSv_UpIYrVzk1Z45_6G_gmRiRoZTPL5ztYaKDqcTIXb4Kdf0KsCyd3bTh2IcrbSjL4k9YVGs6oH35oCz4gZKWZjOrGJeAq_gKYx56q8K02jG5jYzKrbROsF5HdeC1EgyPn_UGgNu51_Nx9vomsslQT--fsjRFXkKiA03KnBtDzQgKQsQhwzxCuehqlYMwSO1Iyii5GRwZU-qmRZa4DirkfTD7upOUeP7xBr95pmVPxQSG83-9x7ZsfKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=fC5Wn8iHRuYh201BtTbO1-AG6JGgDHhMSVbJrnlbEeEvDmBfSOb_Jhnbl0YY7e92fz4V0WNVeZFId0Cvw5ffNAxvWDZGxYYIGlsOk742p10YkNI7sbjmpH7fLlgX0kYk7J8bYKQlDZXgNt-Xv6ms9EJjzFCyfDoUo9DrJvu0Dn2ZNx2V2-Y8OiuYHBFiGM0z7tdZefO0hqGDkuwiXvOtVZKq907tJz7PHN5VRsIrv6tZBQmxyymEdl51l2B8bcLvVRo50O-ktBkXA7pAAbpVlgHdi9vTKcSbeb8MGiWeEZkRwZzcGjyw9mvmuJIa-UuC80cXK8Ze96Gjr2c1RkooqrK4dkrCogSAo_a1ggUDguRg93BXQtyx-G-uHLooTAKCsTzzU17DF4qdNqes8EBk2BduSL4mecBdOZNih7zJaqrwrBBq3pidSv_UpIYrVzk1Z45_6G_gmRiRoZTPL5ztYaKDqcTIXb4Kdf0KsCyd3bTh2IcrbSjL4k9YVGs6oH35oCz4gZKWZjOrGJeAq_gKYx56q8K02jG5jYzKrbROsF5HdeC1EgyPn_UGgNu51_Nx9vomsslQT--fsjRFXkKiA03KnBtDzQgKQsQhwzxCuehqlYMwSO1Iyii5GRwZU-qmRZa4DirkfTD7upOUeP7xBr95pmVPxQSG83-9x7ZsfKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=m9LjH4Jafpb0jSelG-fJaY5dIOvWcwyY4Cz_2xrDZATtQ708ZMr53ULG0QLHx5_ckAAFQEYvRQx0_ijCr3aE0E1LjAoLwqggq4I3yxbP4sMcWjy2BVx0miyikvthUWVDM4NhGqhLE4ZUJl9QTnAfVPWkRU3U8mQN5w54QXBE3TB1-nriOiAA6V_hPH0ZfiGERup8fkb6rMcVFrXJ9fBpxC187bRkrkPbm6PidGvUG1Er5FgezTJerFiHNmOXUzjIurlUznHvHYg3WYml8GLI2oaz3zX00Xm8d6PED838IPZmwXv9Y2t5IaEBYUpVrQFByo47vtXXPM56W5HI3jDc0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=m9LjH4Jafpb0jSelG-fJaY5dIOvWcwyY4Cz_2xrDZATtQ708ZMr53ULG0QLHx5_ckAAFQEYvRQx0_ijCr3aE0E1LjAoLwqggq4I3yxbP4sMcWjy2BVx0miyikvthUWVDM4NhGqhLE4ZUJl9QTnAfVPWkRU3U8mQN5w54QXBE3TB1-nriOiAA6V_hPH0ZfiGERup8fkb6rMcVFrXJ9fBpxC187bRkrkPbm6PidGvUG1Er5FgezTJerFiHNmOXUzjIurlUznHvHYg3WYml8GLI2oaz3zX00Xm8d6PED838IPZmwXv9Y2t5IaEBYUpVrQFByo47vtXXPM56W5HI3jDc0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzQpmeb0YklzukUIVKXpAdwuWzpqLzRfJFUvffT6T9YQSPjElKnz_2VRebGo0q0MJwIx-XtAkANO9HCOt-1-nN7sxvroz045eLHJXSWkCphtPUy8CxDRTQHe0YAwcfobFkZkPoxKC37qboqZWpSa6o9X-gWKTRxlR0jYsoRPbm3xRsRpDA_lJi3jr-oOSXI2szZuK2mRequ2R_iMsgLvG9sgWNUMiJZ__8TjI9mcdvV5OUQeG95KhRlFmaU1sLxkdY-dufojR85N_a7P90GToMJ6uCFZRF-Gt2cNbRLGjFks_wP1c26R1wJRFKoVYOb3tB05OyCkRSp86wt8_RI-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppTMHclvGPWHotKgMFkBPRatH1d_LCf0paHMVrG0ETFTcefJ7gzJ-BYpzMYDZsWJe_m_ABFdp2a-tD4op8Dhjju3oSeQEZ7GILjYY0zQ2AYJtYoaEUDDXwRhH0A-imCZCSDCpzK5azutUa_MwmLevz5PeWYf0UnTwcoSH6tlcwXbH_N0OFOWVgsbH5Jo0AA4iRAfX5dwuFuYNXudIjMS9LcfbhFhBwZu-fUy4FCdHnTXTigDVdhg3x0mWEigiL_I9OXDs62-OIJiS_fEl9YDV1u13sTpYIFQwFlH9-TTIM2VltFobhUxZXmOzKAW5vo0Se0o7uZXohemzLCmRQBHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXFGcwXsVIlUY2FLLliNr7GCu6mNhdEIvKEBm726EtSSHtChr21iOUH9RCLwGEpoE7lWk16XuFHzRmpCgOEW9iUi_LCnGDH4w6z3vYcKgJaNNGk5-x9BpMKOAL87-0VGLHqfejJKnoUSPdGKgz3BIuyRBe_uA1qr3byCpvuNGNr2jPeo4G5Z_TxEl4srFn6tdivN_x9AsP60fAIBhNVFFWc_Cyve8ZeH8JghzfuVP5wVwqlsqW8515wZVddkZJBDyFBqFI17mTQjh-cp1AtK-k7x8-n-PnGlSNsJOs1oR9f48MnJwRe7ilhAxoO7OSm8xZiHEfexD5BYup389dR8BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI30X5r4sIUK2t1a-1wWobgdi9RnT5TDkAfWOthUmUflH3o3lUow6hYKTb226BytAoek8yL3eAN-oI4Wl4Pl0RWPXiXfhGtEcUPNFYW0u5ks0P7aW0oFu-SLcwTUHtMae0IIGVvhKMb4zQqNIlGReSpMDrGcDhoDVZDCKT7A8ICg2YS6xI7aXEhXvxkq4owXku2YDzQutfRt8VVsCDZHH1TTt-QqCDK8z3egTA6hqpCuJUoDXfH7dM_uQf0uCRM_eM263aj9KE3ghoovtBLTKPdAH5yO4ILyZ9AC72w4XZgAPD2IvjKNzdS1NRtru-3q25eN09djpMoLjEertTcmDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAeaofHLF4loqR-kqMJB3mA7gBzaVwAgXNJe1yKJPRV8ngWrfYP7GOvASyMoxw2H8zxZyS22KrJrRsrlA1c-AnFEVx84ukMbB_7KeUnixX3pusF0tMoiUpIJAYE3wQ6KXnYKV99yjlA98RgQlK7THEOQTeSdsw3wKhYYA12UVihApXKBTTKn-9NtT7GvtYnt6uGiLfaXgFlr6ARYrj_Aq_O8Gw5Vx4i40OEnR3DozeP27IU2ODubdSWdALkiXR5wOHt4yB9A-kANpXfbJUhkTcH0auT-iQY6A5I602iqtVcOhhxG8hT0sFv-2LnPRnP7d9Qcb6h-0W-jWlVZEQU5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=fkACqRU-IAtuY9nAjCRPKed7XkKw-F2o7u5OhZ2z5FEczpjy0FmlksYO8EPPuLztlNCylLZNqRCTjcyu7esM59fpunW6y-aF-pOCz9rlkhSHHTkc3xJBBabo1gM0Fv2jWcqXHZmdQk4DzE_ejV_uw9x7oz4jHQAbjvshnlm9f7kTR5SC7TbcCUND0Vkaz5sr9_kRminmq4pRLiLCS-RXuMzpzi51-z5OncfrGld5eihGo6WXyHnFUxrudW-SxbxYZbkNcW8U6nvKk2DsUI02dDltT6DnHrY_jgAZMm3t-hkV-uZD81B_a2bk5FleAy5_ID01t8Z9XHElKzRnXTXX5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=fkACqRU-IAtuY9nAjCRPKed7XkKw-F2o7u5OhZ2z5FEczpjy0FmlksYO8EPPuLztlNCylLZNqRCTjcyu7esM59fpunW6y-aF-pOCz9rlkhSHHTkc3xJBBabo1gM0Fv2jWcqXHZmdQk4DzE_ejV_uw9x7oz4jHQAbjvshnlm9f7kTR5SC7TbcCUND0Vkaz5sr9_kRminmq4pRLiLCS-RXuMzpzi51-z5OncfrGld5eihGo6WXyHnFUxrudW-SxbxYZbkNcW8U6nvKk2DsUI02dDltT6DnHrY_jgAZMm3t-hkV-uZD81B_a2bk5FleAy5_ID01t8Z9XHElKzRnXTXX5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=RZQHYnA4_ZN79jvt7ZjfkjXwh3pP6qDbJEws_8O8hnJa2CosHJCr9RgG79NzdW2WioUAeDS3kNDSJE7Q-9D5KadgFvhEVn6rRlgV2lBSGTyMUPVVRNnzwSLpJ_x1Lnh075zN_GOjCvlurekWBVwJfYqDfuJKAMKHaFjk22Mwosg2fKIcvLF4FIr9pDs8J4TW5k7UrLO2PtTF1yrGGVOQKmOtEIIbFRgGl0tGCsA3R2cb1MCtMj3LurqU5wCnZB71EP77EcBRJlYucOcPUtbVZscaup0lG3P6sE6vIcFZJ_t2zvphxebcWH0yd7apzsRZLTOE0G1EX9ByxNqr7EkQ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=RZQHYnA4_ZN79jvt7ZjfkjXwh3pP6qDbJEws_8O8hnJa2CosHJCr9RgG79NzdW2WioUAeDS3kNDSJE7Q-9D5KadgFvhEVn6rRlgV2lBSGTyMUPVVRNnzwSLpJ_x1Lnh075zN_GOjCvlurekWBVwJfYqDfuJKAMKHaFjk22Mwosg2fKIcvLF4FIr9pDs8J4TW5k7UrLO2PtTF1yrGGVOQKmOtEIIbFRgGl0tGCsA3R2cb1MCtMj3LurqU5wCnZB71EP77EcBRJlYucOcPUtbVZscaup0lG3P6sE6vIcFZJ_t2zvphxebcWH0yd7apzsRZLTOE0G1EX9ByxNqr7EkQ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نفهمیدند رفتنش فقط پایانِ یک پادشاه نبود؛
شروع رقص طنابِ دار و بوسه مرگ بود.
عکسش رو از اسکناس‌ها پاره کردن،
و از همون لحظه سقوط شروع شد
و نسلی که خیال می‌کرد وارثِ آزادی می‌شه،
وارثِ تحقیر و فقر و چوبه‌های دار شد...
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=BBFuKteJtAFuaWsJ5K1kqXJDIV2pYsFBfDayHrKG-g7JebZXeecT9KRi6ueqh_lEgn0KvWx9JkR5MY8LvYfr9qx7sI_Mow_6yNkF9oFgAwQ2W7tuFBIq_HT-U90f6U2kQ9USjKSKq3DDh3U9-dtIvar-gt5C_U7BerF1ewS90dwnCDnzeFASup7tqLqy12pFta-s3sWdYH0Myj0810vsONFhayDy7PZmMXEN7x5Phy_vnTDL2OVZh-9K3rEoFhujbPhbYj_6nG9wAyUIiV1TUAk0m2pIh5yJGLyMkJ0cPYZo76aG7rKrPUgnQrKdL0ZztSul7chTqqni5oq4mNcX-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=BBFuKteJtAFuaWsJ5K1kqXJDIV2pYsFBfDayHrKG-g7JebZXeecT9KRi6ueqh_lEgn0KvWx9JkR5MY8LvYfr9qx7sI_Mow_6yNkF9oFgAwQ2W7tuFBIq_HT-U90f6U2kQ9USjKSKq3DDh3U9-dtIvar-gt5C_U7BerF1ewS90dwnCDnzeFASup7tqLqy12pFta-s3sWdYH0Myj0810vsONFhayDy7PZmMXEN7x5Phy_vnTDL2OVZh-9K3rEoFhujbPhbYj_6nG9wAyUIiV1TUAk0m2pIh5yJGLyMkJ0cPYZo76aG7rKrPUgnQrKdL0ZztSul7chTqqni5oq4mNcX-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy8czo8801lboW0w88YKUNLtzj2Zk-fF5-Wk6-AlRdLlqdurfG6zXQHiVtfLQ69Ge_p8kY7QRkg8NXhV-SzWQCzWsFfEul7bbqP7aPRk6PFN6Ge5C5WH5WGkOaezSK0fRKlkZBYtuR7H7SUQMr_eVnEu-J0_ClfMoFvsmRQSU-3QN8oC_pyWGXBShaN8UchK7ttYzBn6jNIxRVUyXsMSg9GDZ7SKEtveDvxYjo73kpc-cNzMiNmPt35NV6LtcMQlt21VBfVUIbpOqKrSUO7lpYFvjcwgM0U6HN5yIBTbxYlLD9No3pteIwBoBaru1HSyKBbrmsKR_FBJb5HMZDVwcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=u4i2MukRNW6bAW34j91svQ_QJP6_hKF5-xpD6R2r8UuSz6uHNBkdYsXb-IFOezo6EZ28Lm7fyh6ESLK5J56GG6eSMcB0dynd-R0EWKX40t4XvJiZYqfjQSDpUV35ipikZ1q0DU3oe26Q-6ur3MHXkiP0o3kGhsdFJXIgf44lyoF2HNbDtJ4sdNR5t7EExlV2APEtjYumyBqHrlnrtX_kPFocH5yGFIu5_sBUFi0fhBmdKB0l5atYn6UB9j9b6ZfXJqk347SSYSQYFZw8pz6M5YyM8pBgi8jkLWDL8JtTU3VrBZaiklouth69bEXrPZMcFuZFRa5Vc2j9AKJOBqHvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=u4i2MukRNW6bAW34j91svQ_QJP6_hKF5-xpD6R2r8UuSz6uHNBkdYsXb-IFOezo6EZ28Lm7fyh6ESLK5J56GG6eSMcB0dynd-R0EWKX40t4XvJiZYqfjQSDpUV35ipikZ1q0DU3oe26Q-6ur3MHXkiP0o3kGhsdFJXIgf44lyoF2HNbDtJ4sdNR5t7EExlV2APEtjYumyBqHrlnrtX_kPFocH5yGFIu5_sBUFi0fhBmdKB0l5atYn6UB9j9b6ZfXJqk347SSYSQYFZw8pz6M5YyM8pBgi8jkLWDL8JtTU3VrBZaiklouth69bEXrPZMcFuZFRa5Vc2j9AKJOBqHvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
صادق خرازی برادرزاده کمال خرازی اعلام کرد عموش بعد بمبارون خونش زنده میمونه و تو بیمارستان بستری میشه که موساد میره بالا سرش و با گاز خفش میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=sfG0qsW3WCxr8Yot4YV0kePqY6Sp9JzO7KsuSr5W7Ud7JfwbG7V-jsILmF9aw3KGquKakLCXLUgMw69w4lGZv3J4J-_c780xOSRK1K89ysKLSZy-7iKzAMq4a3il1C6x88NBWkZbrj8aarFny2yKJkEC8qxntHrsnqqhuxScOlIVakqqlfSzTYJ9QS7Rx_QpvP2ubUGIpJRuWGp8Q6mjsW4SzGKeNjOl0gE3GyboNy7IFMWuDW7L032blvV3KOHD1r9bsj9m81w_BRlB6gZnVhTm_fB_GwT-RUOj9lu-tBBCplOTdg6jgyRskBub6llr-6iE2LMDIewy98W5DNBgoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=sfG0qsW3WCxr8Yot4YV0kePqY6Sp9JzO7KsuSr5W7Ud7JfwbG7V-jsILmF9aw3KGquKakLCXLUgMw69w4lGZv3J4J-_c780xOSRK1K89ysKLSZy-7iKzAMq4a3il1C6x88NBWkZbrj8aarFny2yKJkEC8qxntHrsnqqhuxScOlIVakqqlfSzTYJ9QS7Rx_QpvP2ubUGIpJRuWGp8Q6mjsW4SzGKeNjOl0gE3GyboNy7IFMWuDW7L032blvV3KOHD1r9bsj9m81w_BRlB6gZnVhTm_fB_GwT-RUOj9lu-tBBCplOTdg6jgyRskBub6llr-6iE2LMDIewy98W5DNBgoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=TWI051fYGYoOnrkXyhaAZzBiOd0PsY1ZnNSDrGW9nWHJSq-sD-3S4OLtZd0vd8Bg6YNWwNu-RT1Jbd8JYJYrirc0Ri9lWjkzMXeQ_cT5Z9oUtl0LUp-JcDU-Qa2DHVmWiGT3SjPTBT-b6L2-ifuaXKsclzeDzCdDgwJzoG8k9xKOKbMVOwDjrPkso1-g2MfqLSQcrXjVyyjsH8MaXMnTTsTUcT4Wmo7J8aSBX1pzFlLKjNXrOwG7jlB--klW18C6g4BfaTCcUAnlDVBAXVXUnd-KbJCnmien3j-sM9W7TIzq4gC041EYe4fMScbBbZaykjOQN4J-ZtJe3FZTmdcVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=TWI051fYGYoOnrkXyhaAZzBiOd0PsY1ZnNSDrGW9nWHJSq-sD-3S4OLtZd0vd8Bg6YNWwNu-RT1Jbd8JYJYrirc0Ri9lWjkzMXeQ_cT5Z9oUtl0LUp-JcDU-Qa2DHVmWiGT3SjPTBT-b6L2-ifuaXKsclzeDzCdDgwJzoG8k9xKOKbMVOwDjrPkso1-g2MfqLSQcrXjVyyjsH8MaXMnTTsTUcT4Wmo7J8aSBX1pzFlLKjNXrOwG7jlB--klW18C6g4BfaTCcUAnlDVBAXVXUnd-KbJCnmien3j-sM9W7TIzq4gC041EYe4fMScbBbZaykjOQN4J-ZtJe3FZTmdcVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=DpdDqBqRBaMDyPixhtEuYuFOU7_BNeR7PdpoNLYSj7dHoQtWHteTELb8xRNnZcUcbxLNfZ4WbYXFKEHCKGY0KtcSXVebG1IRR9DY-8UJpxP9qGR-ObkwW-81M79mq-Ww87ifg7vfTzv8AS3L66Y6zh9xlySiom-tPYXm5MyvOKz0PqHWewM2w1GQRz2L9NYllBgMuUUXnfIARu84PyTfbxxpVWvbCza2do61UJ5pgak2IeZbuUBzvPWfVQKvYKD5KL6wUauzsMGBehMaHq44Ru7VxCBchl6Pqq7FzJ2jXGE39LegdYclNqqErm5UgW0OD3jx3j4cd0xzSH8977YESg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=DpdDqBqRBaMDyPixhtEuYuFOU7_BNeR7PdpoNLYSj7dHoQtWHteTELb8xRNnZcUcbxLNfZ4WbYXFKEHCKGY0KtcSXVebG1IRR9DY-8UJpxP9qGR-ObkwW-81M79mq-Ww87ifg7vfTzv8AS3L66Y6zh9xlySiom-tPYXm5MyvOKz0PqHWewM2w1GQRz2L9NYllBgMuUUXnfIARu84PyTfbxxpVWvbCza2do61UJ5pgak2IeZbuUBzvPWfVQKvYKD5KL6wUauzsMGBehMaHq44Ru7VxCBchl6Pqq7FzJ2jXGE39LegdYclNqqErm5UgW0OD3jx3j4cd0xzSH8977YESg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=akjtCheIDFdf4LZ_45X-N9V0LBdAjir40CCCpEh13o-Tk-H4dlR4sa7PJ2xDgliEBoZ3WKQCljgwgCIrGodtKMaBpaMD7jQr2-3BiCW3pyTwxHkXhKIwU6J12ubqwNMiK7jrC2sf50htkjKPDWSnPowvo7rs02O8Jal3rve0j08zXdpnPE0UlsQUTLgbR5UvUtai_XmPLkD_TpnB6t1wM_DCU3PAXd04QLp0kp9tFTvWkbruDVf9aWSLwfrtMYbmBA0FngligAglVJz_w0-_shpJI9R-kUpczcfjtRUq7Fd3qwIY-5mSGxvnhaQJ8rCdqj70fA9kv86wtYP1tYwteA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=akjtCheIDFdf4LZ_45X-N9V0LBdAjir40CCCpEh13o-Tk-H4dlR4sa7PJ2xDgliEBoZ3WKQCljgwgCIrGodtKMaBpaMD7jQr2-3BiCW3pyTwxHkXhKIwU6J12ubqwNMiK7jrC2sf50htkjKPDWSnPowvo7rs02O8Jal3rve0j08zXdpnPE0UlsQUTLgbR5UvUtai_XmPLkD_TpnB6t1wM_DCU3PAXd04QLp0kp9tFTvWkbruDVf9aWSLwfrtMYbmBA0FngligAglVJz_w0-_shpJI9R-kUpczcfjtRUq7Fd3qwIY-5mSGxvnhaQJ8rCdqj70fA9kv86wtYP1tYwteA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQO4FLStA3P3jjRjCp19VyTz-GsCbczvqhchKE2l_MCLlgKmT2EBdGLjH3LHYRUhx_UiqqI3oQ4CdyP_mODe9D0lylefiZXuXDCD9d-WK2iieBe_nED3mCrQ1-SO7DlbfvkhKpGjzRClOLkZm4mDQzFne3sb9CqLsgVNA4UxvTG_sb6qeeG45wYn_zH1_dVOj98one6I35K9NN9IlvlCZNd-1Iul019SbkRHuss1iiubPC_CzcIft-OgrgTS_Vcc-Zgljn0gj9g45Wb0DDkwGApJAH1jRzSGZRHAkzbZmQPR_B4W6ItSi5TWvSLR39yef82yX61JjIsdk4p5b2IE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTbu0MLaeyj7UXzbvKStW3rHn0Jrc15yHp9ZYqPL7afNQo-deDK-HOz9aJB5puMNczWCU-FOIqZCJ8PZHo9wY6vmuwlB8xmLiiyAm8PnV-4exNV5q90bN7OwMQ4U_fUvHS9KwbDTP81vWN6nlY2Mlh_5qWzXLfDoQXW4nhgVbZWsnzI5FnKy7OHuOtXaUPQokZgAc2ObHbddxi9AxGCgxtuc8Gm2VUsVBPcjKa8535NSd7bgXPbpwZa9m842qPgH5JkfXhQ0kP4XVtXMsYvkkZ7-xUu9oi_2iZtAnrnljcW7f8EERGKwkxgYbwSBR60VnzYuE-i9P0cOoqZj34YqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-L0Lc5cWrKiVev1OF2bgP5MXbpCbCYjg71-vUqvIo7mbEPUUagH0oxe4OsZtNNTqRZuRVv6Lo4J9Nkx-oaRZHaY4o4oZqnXeqzXWbzrXAukZQR-ekTIai0VWCXyKuOUHDaIn_p6Hg7nR3VTSzIjcfpYTlvTbz-YWe2oG4NhHC_ZcLr514wLKkfLJzwAHPBJpsFbybRxbs40MablGSxj7XG2aQj3XXgC5G7mt3xCsh_1NF0K3oSnPGGMZPi7Z-EKjXa5Hq1O4g24zrYknnMt2D92IpZBeLkQdPyUlrfnAO9OAtpBHc3B7AMQY3bIrhoPkWlmX45ASAIX2CPbs8RPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=cHLFhuJpuDZQ6GX-VxYJt89yUizQzTY4xcfBCNm9B3hzOU1AR_QK4q8Ykg8fa5QM7ZVG4OdMWbpKZPBNDvcX-Y65LmRPeHFE8lnxGfskx9zEEIocByjUmn01JwxISnjpnoDMA-_OAz1PhJCab7IusfbnB17T32kOGiub11dTHJzr76cGlorvzGlv1u3YC2P_a5_nQORK584t25Fy9zHw5Mq9TEchWnT1Nj6Dc23Sy3j7xADRP5T-iZ1Obqp35DGGa1tP_u31mQh8SLh2VWx3LYtHn1zE79EK-4TTrJhNHkDff5dSMdq6C7P0ILRXzGLCgdNyLMJcrtq96kJW-dYz_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=cHLFhuJpuDZQ6GX-VxYJt89yUizQzTY4xcfBCNm9B3hzOU1AR_QK4q8Ykg8fa5QM7ZVG4OdMWbpKZPBNDvcX-Y65LmRPeHFE8lnxGfskx9zEEIocByjUmn01JwxISnjpnoDMA-_OAz1PhJCab7IusfbnB17T32kOGiub11dTHJzr76cGlorvzGlv1u3YC2P_a5_nQORK584t25Fy9zHw5Mq9TEchWnT1Nj6Dc23Sy3j7xADRP5T-iZ1Obqp35DGGa1tP_u31mQh8SLh2VWx3LYtHn1zE79EK-4TTrJhNHkDff5dSMdq6C7P0ILRXzGLCgdNyLMJcrtq96kJW-dYz_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=iIb7ZrZP435Nsi51GQIaQmVDBJbj8QGXG-ewlwG42cuASrY9wfbstyqTIQDBJtSYqOWKpWJkpE_qogqawdLaksMPQBVxWIgskuTp6cnT88lFTncXCPmGtv-Zw4jVQw2cFqwIZnb5Tt6aczIcRVaVEOpxwX5zbP6IMEtvaX4pFAyikVdsXEd8sfa-pxWlyJeGXABaruMuqNgRzUuX4_u9AcJgPFz2vu_7czK-UV_kW3Q7lKEXcdljxBT9Gr4cglvhc5epzek-ph1ZTSzHXDNuN1OtshNL08qb4obEd5jd0ADImxvrFjqI8PWboRz-k6vyMMpPe8UuOJUCPoNyV3Om8kcoI7CsyOrb5_QgRhSMyJghCSDPCPa3AAbmRFp3ug69rcgbh3cDpd7qN2ekwa9O5xlxtiHmBF6TgugMQ09K3P_rBiWh8Xr8EdQtp9ELOZd5edlTy1xl5PZjJpe6T_PeVMvbYQjhAwbcap_5243mtMyvkH14uzECZBgtjKvumLkfcemIeyr5RCyH6qMcvuzRDIva4yO90Pt0DUOXdJYxLOeVOYK1upnQbf3TpfLuziDwliO7wFClydbSJezHQOZ9Nf48t5dUMyjuwm2UD2MqEMDhKTb9LPPt2hR8UOqUMyX-_U9C2m7xKP5sepUwNKrlK7V23yYc9rDuL8nlX6d9vuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=iIb7ZrZP435Nsi51GQIaQmVDBJbj8QGXG-ewlwG42cuASrY9wfbstyqTIQDBJtSYqOWKpWJkpE_qogqawdLaksMPQBVxWIgskuTp6cnT88lFTncXCPmGtv-Zw4jVQw2cFqwIZnb5Tt6aczIcRVaVEOpxwX5zbP6IMEtvaX4pFAyikVdsXEd8sfa-pxWlyJeGXABaruMuqNgRzUuX4_u9AcJgPFz2vu_7czK-UV_kW3Q7lKEXcdljxBT9Gr4cglvhc5epzek-ph1ZTSzHXDNuN1OtshNL08qb4obEd5jd0ADImxvrFjqI8PWboRz-k6vyMMpPe8UuOJUCPoNyV3Om8kcoI7CsyOrb5_QgRhSMyJghCSDPCPa3AAbmRFp3ug69rcgbh3cDpd7qN2ekwa9O5xlxtiHmBF6TgugMQ09K3P_rBiWh8Xr8EdQtp9ELOZd5edlTy1xl5PZjJpe6T_PeVMvbYQjhAwbcap_5243mtMyvkH14uzECZBgtjKvumLkfcemIeyr5RCyH6qMcvuzRDIva4yO90Pt0DUOXdJYxLOeVOYK1upnQbf3TpfLuziDwliO7wFClydbSJezHQOZ9Nf48t5dUMyjuwm2UD2MqEMDhKTb9LPPt2hR8UOqUMyX-_U9C2m7xKP5sepUwNKrlK7V23yYc9rDuL8nlX6d9vuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrdfvFrtOMuWjMo96dSdv23cZU3OMNeFB6dJsN6BcpDcV6YjhVuv9sS0OIPS-7esBwneSv7uCGRyH88d4TDYSkTIr3T2oQrvPZJyUPAy7Bz0LrhOA8b0AzXLg3KUcT00MNoJD-LsdPLRoHWOjSZd7ax37YSXGz5S5dGUyK4FNovvCm9IIHvqno5qZu0DiobYNfIwjs2w7lTP85cMvqDRApyDwBwDw9MG6Wpzh_1pb9eitfutxH5Qh5RlgP6VdKWqJWSrw1xn3OX4eXgBcyaIwA5Cv_iW0iU7WydXOiuuhXvf74pled2jpv79EIX7oyHqZYr67sNwgcnSS5ZZFyrD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-61B9rEvCnEGOfxwzLe6kAiukiZiy7YUJQ3-gGqGiQFgrij0_mtk9APYgKmHT_p3739c27TMduJTnSAf1YXQB99IbZzc1POnCAYNmATgzuTOaDnYWHogcCpGBBdOrfiXxajbBmdVibWa7DfKBCwTXRNyxavDqa1cmZLtKCCjab66tqMWxPBDL5FChXBNXf4MbhLrvV1TTCgxmq9wYeQ0roljJwtWHF3SVr-GZHnhFTHlbOzu83jRSyntu5AHdnwdE2tcMqpGnQsUVWN2kcD21vzn6uBP1C-qcVxqBLt18-dLY_bjpBUM3PBQd2ZixdsTR_-I8UFvrA8ph8eP4v5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVBJlyixxNTNnn0Z8hm_Txehenarod6AFG302L_nhHpU7Q-i8mTpGv9xfL9fT67lgw7v0oVyIrM6aD6iFhmLdD73qEGcCq-0c6XzANOVpw9wG9Z1zAOg0QZvSCjhGvGsIZBmnjEjVDqQEsfrN_WuPLCJOsogd00v9lC1kSOXk-P-gmgRb05qwBXyjpKzgXd7rbgPMLZ3CT9s5KbulW3yNAwA6pZBog8GmoltSFuXv9wqb42IJf4pWg-qeXA3TiQyLw9BStCv0t0es5pDeI1wIOsPiEgvWjavz1X3O92EemKPt3rmad_OwU6M_w-oVQBGymVl0-cQbDdZVHoJqH-_Tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=KiJI1doYIjOLV3TXwqwzFyZ_78m6aVfTfEvorRkSZ5fyio-slvU4HJivZmjvh5WgAVQ6RYUCjoFFjYPm-Sbpj5IGlBPtZPDZoxw22fvkfyaeaQK_x2KTcQ_1UP9IW0j42tRHE4U0PPNxCWY2ix2f692n7iYxmXNMBdnKVK2BUTkApkhHzryANUOWxokFzh_uXr3rSNMbKCn4D0oHV08rDjRi_qCtzuPMBj5pL6t4Vm8WSLUwG5wUISi55nV55YsKjrHPuG0xMotHIs3ju6PSptH1bmErJnntMao9DviMBQNipjWZWFoBqQiMBAvKyvdIccoDOTi1G1v1PwQDmCNqWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=KiJI1doYIjOLV3TXwqwzFyZ_78m6aVfTfEvorRkSZ5fyio-slvU4HJivZmjvh5WgAVQ6RYUCjoFFjYPm-Sbpj5IGlBPtZPDZoxw22fvkfyaeaQK_x2KTcQ_1UP9IW0j42tRHE4U0PPNxCWY2ix2f692n7iYxmXNMBdnKVK2BUTkApkhHzryANUOWxokFzh_uXr3rSNMbKCn4D0oHV08rDjRi_qCtzuPMBj5pL6t4Vm8WSLUwG5wUISi55nV55YsKjrHPuG0xMotHIs3ju6PSptH1bmErJnntMao9DviMBQNipjWZWFoBqQiMBAvKyvdIccoDOTi1G1v1PwQDmCNqWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoIvtTe_-MPkkOGCn0f3spbBD92uNBbpz71S87NkeUldhSXLlQWK2TbU_vZ8GIR7YiFCFDo2YRruqKyTbi3os6TjDLmLlQi6Xm9k8ne3aTFDcw38rj-lIf3AWklRgI1emMTuxld9_APcIm7DABHskwDh8JILvuX4-fk5gdTZk51NTdlR0GsMxjCYJvH6Y6VhIQFsFPeBEIm-GkRZuadqAArXOL9QemN23mPMTmteE9jC4qAwhxz9vysXGxCkNJZO18l4I8_iteAViL1pgQBmDn6BmGWaURi9YdBe-hv1OPSDLesUjcGrJuAeEOkjHSGbqsRx8G_S8qckn3eZiVu9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=A7Ur3V1A7nNkPQElhxG73klzWLpcwE2eVmeR_HBsN09_bFx3RTFyQkKmlAFtiAZ7IrBvbrM0s698ESqezhBIcTlQYLRcKzpfmHIg6eNDCmbkDRabuqe_8fYEVRBCtx6eBcU-jkKkWcGXQhnPtcscbeGQu9bT5FImHo_-tPvZW1z-mjyzCl-vcqF8XEB6B-ltdWjXUeDKOvGvTofsTIpgZbq5eVmiTU3dFO207i0CiWR00P-oDel55AjC_qRgw9jXPuiiRMT3vKX_8tqvsI4K9eRQaZuejGoizGHoq0Olzi1KhHvqPCVzcs15ATJM2gl2jNygjGkKk__k5CNh1lXyFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=A7Ur3V1A7nNkPQElhxG73klzWLpcwE2eVmeR_HBsN09_bFx3RTFyQkKmlAFtiAZ7IrBvbrM0s698ESqezhBIcTlQYLRcKzpfmHIg6eNDCmbkDRabuqe_8fYEVRBCtx6eBcU-jkKkWcGXQhnPtcscbeGQu9bT5FImHo_-tPvZW1z-mjyzCl-vcqF8XEB6B-ltdWjXUeDKOvGvTofsTIpgZbq5eVmiTU3dFO207i0CiWR00P-oDel55AjC_qRgw9jXPuiiRMT3vKX_8tqvsI4K9eRQaZuejGoizGHoq0Olzi1KhHvqPCVzcs15ATJM2gl2jNygjGkKk__k5CNh1lXyFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=HQ8jgAZqJBGFxKfMXEmRBI2jC85-bLwIStaahufL5cpL5JrPIe6wqwehSWlKnHIqo3ubYCVs8itlCcvrTUaYCTOeBbEXiRpkQfGMdQbC1j6x1XJNk-YnB7Pdoya4eKTu2kHiZGOhTzsiQD88c6KzUU-7EnSbALUgd8YbBnypf9XiOpKxFbYUR52oabu4AK1PbWxV8CiL-hE1aPDBzKHobXZIfWy0hiZx5pWqXbop3W9PjGqj5h--RhuKCt8HKEeANXHHvPsMSVlOLxMzbMxY7dexSRoVpGWq3kS-UGZj96QcB6LYY2NP2V_8mCQn-XsaEbntxkXciSdZqbxRA4YhKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=HQ8jgAZqJBGFxKfMXEmRBI2jC85-bLwIStaahufL5cpL5JrPIe6wqwehSWlKnHIqo3ubYCVs8itlCcvrTUaYCTOeBbEXiRpkQfGMdQbC1j6x1XJNk-YnB7Pdoya4eKTu2kHiZGOhTzsiQD88c6KzUU-7EnSbALUgd8YbBnypf9XiOpKxFbYUR52oabu4AK1PbWxV8CiL-hE1aPDBzKHobXZIfWy0hiZx5pWqXbop3W9PjGqj5h--RhuKCt8HKEeANXHHvPsMSVlOLxMzbMxY7dexSRoVpGWq3kS-UGZj96QcB6LYY2NP2V_8mCQn-XsaEbntxkXciSdZqbxRA4YhKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=ddcWR9qDI2d3WSVEO6ghCF5GeTrIjrIJC7BO7MxWR-Tde-CZQuQECl820jxFHVVcS0Jhr-1oSvgwuyjxdZWYKvs1G7tyhwn5k32LFlwJ0b6RTBFgRe1cct7bDjOCPDFyyzZOcwgsVC4Om9oghI3etVVLEfCl6zAY7wnpuuBNVQ8gMiv2TIG2IQAXEk_9Z1EEGkrlhz326HxDOFc72xfYsa2JzmjPfkeloHcW22ucUYCprLcp-MClatbUzwWetkfFTRD82AMQv5qTKHvCSfXMVUVK2d75nfOr5wfHXJZy5fiNx0G-TFKJJZdbUXiMaSSWnk2N-H053ujyN6-IrRchJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=ddcWR9qDI2d3WSVEO6ghCF5GeTrIjrIJC7BO7MxWR-Tde-CZQuQECl820jxFHVVcS0Jhr-1oSvgwuyjxdZWYKvs1G7tyhwn5k32LFlwJ0b6RTBFgRe1cct7bDjOCPDFyyzZOcwgsVC4Om9oghI3etVVLEfCl6zAY7wnpuuBNVQ8gMiv2TIG2IQAXEk_9Z1EEGkrlhz326HxDOFc72xfYsa2JzmjPfkeloHcW22ucUYCprLcp-MClatbUzwWetkfFTRD82AMQv5qTKHvCSfXMVUVK2d75nfOr5wfHXJZy5fiNx0G-TFKJJZdbUXiMaSSWnk2N-H053ujyN6-IrRchJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
