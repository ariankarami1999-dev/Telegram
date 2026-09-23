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
<img src="https://cdn5.telesco.pe/file/Ea51rqoYYKdDhSbQGqDh9u9M7e6EALwsRwsWS0-UrwH7TET7HZpN9iHY2VJzlWKBcBMpR_WvLonOZuuUSSiJ4spYe86oMqCYYhx69vL2WNQbSOVObdfjks7SAWpmUvbuJ_8UgElFj4cKEg0lrQSeSx_7H4Ku3JXvP5XCsUtPGgoziMKYAGx_gTUquQzdoR3UjyTx2FMQap5vbjBQOoaqbthsSt4TIGA10l9DVhZ_cHKE5x58Ti6gI0JjYr3__wbT8QkeL3C-eeFW30J5jnfmOQ1-qpngYgBKt70jWejVSrWX9eYM4cLtQTByMrgmc4jwKa4BBbkmHxa4I00DHhxH1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 403K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 18:37:34</div>
<hr>

<div class="tg-post" id="msg-107139">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
آنالیز جذاب از بازی‌هفته‌قبل برایتون و آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/Futball180TV/107139" target="_blank">📅 18:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107138">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=fzgW1jgN7tex502XUMz0OMEbAaMp0HXVHlrUu3cgBhZK2JpMZ5-0C0mmBYkZaTpzgXAlU4CNJfMrfcgQJuU5TlYZVNCiEHFO_X4Vl4pUCCcCe6W_c3lt-wyooHeLQ3CoJzRRB7WmjCT9QSB95YQPqdD9tmsSsGd_irIZe4Ix8rFVL4nildbNnhs94ZvCXsLppwbAGUkAB1-w6b8i2IfQ4v-WeoZ1V8E6eaUi9DK8FCvM8oHul4U7wE5AmKCXVWTacN0AsnRgGNJB5xw0tUj0LzNPkW5ls2DGnh523lph4t1R44lCNAT-OVFZSWy_HJJDcwJCmk-xjmAwfqNb2HJCNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=fzgW1jgN7tex502XUMz0OMEbAaMp0HXVHlrUu3cgBhZK2JpMZ5-0C0mmBYkZaTpzgXAlU4CNJfMrfcgQJuU5TlYZVNCiEHFO_X4Vl4pUCCcCe6W_c3lt-wyooHeLQ3CoJzRRB7WmjCT9QSB95YQPqdD9tmsSsGd_irIZe4Ix8rFVL4nildbNnhs94ZvCXsLppwbAGUkAB1-w6b8i2IfQ4v-WeoZ1V8E6eaUi9DK8FCvM8oHul4U7wE5AmKCXVWTacN0AsnRgGNJB5xw0tUj0LzNPkW5ls2DGnh523lph4t1R44lCNAT-OVFZSWy_HJJDcwJCmk-xjmAwfqNb2HJCNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
تشویق مسعود پزشکیان توسط عباس عراقچی و... پس از پایان سخنرانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/107138" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107137">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
⭕️
🇮🇷
پزشکیان: انرژی هسته‌ای حق مسلم ماست و برای درمان و کشاورزی نیاز داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/Futball180TV/107137" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107136">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=JmWeROaan1jK-OVUCLuGYfsAzHUBEhFy814dj0T43gcku2Dhq2FLC6qLuBlG_lIF-6vljPCe__LYtpjnkd7WitD7qZ29b0QqgmJVJQFhQ6Hv9Pkwlqhm9IikJjWksWen65gzh2geNM8A4GkAKo60S0kqgHXh3KBJ6RO-d4KiM8iRdLCEnFzQ5YiSCJx3sNcaKtFAmDnvBC5vsoa4kt4gn4ylPvq1lX4lxMwye6lGr96cWV-O294mAkomN3p8yciF79WjSAVp1AZmx_vL0Qu_sw30tUd0caYolWcMOQefjrwB9VNtgTL8LDzjxXMFJb8EZbgl1yyY5eWEa-KwZ3_bv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=JmWeROaan1jK-OVUCLuGYfsAzHUBEhFy814dj0T43gcku2Dhq2FLC6qLuBlG_lIF-6vljPCe__LYtpjnkd7WitD7qZ29b0QqgmJVJQFhQ6Hv9Pkwlqhm9IikJjWksWen65gzh2geNM8A4GkAKo60S0kqgHXh3KBJ6RO-d4KiM8iRdLCEnFzQ5YiSCJx3sNcaKtFAmDnvBC5vsoa4kt4gn4ylPvq1lX4lxMwye6lGr96cWV-O294mAkomN3p8yciF79WjSAVp1AZmx_vL0Qu_sw30tUd0caYolWcMOQefjrwB9VNtgTL8LDzjxXMFJb8EZbgl1yyY5eWEa-KwZ3_bv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
پزشکیان: اسرائیل هر محله‌ای را در هر شهری و در هر استانی هدف قرار می‌دهد و عملیات ترور انجام می‌دهد، درست مانند گروه‌های تروریستی واقعی. در غزه، بیش از 80 هزار غیرنظامی بی‌گناه به طرز وحشیانه‌ای کشته شده‌اند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/Futball180TV/107136" target="_blank">📅 17:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=qEcgXhq9E-0ew5qlQkPiLUmbEy7-xPX6jELVV868zju9k9rMFFWzEeHfJGoRtKBskM46WtY06r07h_M78lIb5nhf-4HVawXQF6z8s9X5oiS5cOHg9YnjPGLRPbY26FeutjIhMuPdhoRjaG6Jj6l6IplXQpGLse5SyhZuLXiBBWN17RJ5weIvkxkIXM9S3l9ouDNnmblfOcFxZV7pcvXXdVweYqkTYJAKIZ1zdWyBZ2JB5BnRbRfrBFNcJdg5AIgeDiCN8lYZ5ozGDtx5vknBkw9tQFrMlPJLx3YIw18bpqFrHCmDCoEL-s1AMdSKu_1U_vhHAlx9ysZOOcd_vK6RlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=qEcgXhq9E-0ew5qlQkPiLUmbEy7-xPX6jELVV868zju9k9rMFFWzEeHfJGoRtKBskM46WtY06r07h_M78lIb5nhf-4HVawXQF6z8s9X5oiS5cOHg9YnjPGLRPbY26FeutjIhMuPdhoRjaG6Jj6l6IplXQpGLse5SyhZuLXiBBWN17RJ5weIvkxkIXM9S3l9ouDNnmblfOcFxZV7pcvXXdVweYqkTYJAKIZ1zdWyBZ2JB5BnRbRfrBFNcJdg5AIgeDiCN8lYZ5ozGDtx5vknBkw9tQFrMlPJLx3YIw18bpqFrHCmDCoEL-s1AMdSKu_1U_vhHAlx9ysZOOcd_vK6RlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
خروج هیئت کشور آمریکا حین سخنرانی پزشکیان در سازمان‌ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/Futball180TV/107135" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107134">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=HxjO8DuXiESqNtsKKILg_RWGX4JXw-gBM8jtfknTCguF-L5z2O6skI0w0UpBUBuF_iQkRHhFM06CN-N9m8VuoO10lTE4DdN_84vGmTyrkhe9RpNSvYUCTKmV8y3yllbvsk57WN3arGcDlHCCNenbDVuoBC1V18ZpEFib45-ORVgxdTkOjsdz0BC5CB5ELLHWnvEcnJ8qfFvgX67lN1H5WJ3xf6eX6xzhCdyG0VwEutm3KdJ-p-of1XU59FNZNIo9Ce6DHXYLJzT68Cy_P8TDPuPQXckilVdPT4ZUkaa2p0_0Axqitg8lKHyAxUBPHdBZNYW6K-KNy-v3SNZRDMOpzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=HxjO8DuXiESqNtsKKILg_RWGX4JXw-gBM8jtfknTCguF-L5z2O6skI0w0UpBUBuF_iQkRHhFM06CN-N9m8VuoO10lTE4DdN_84vGmTyrkhe9RpNSvYUCTKmV8y3yllbvsk57WN3arGcDlHCCNenbDVuoBC1V18ZpEFib45-ORVgxdTkOjsdz0BC5CB5ELLHWnvEcnJ8qfFvgX67lN1H5WJ3xf6eX6xzhCdyG0VwEutm3KdJ-p-of1XU59FNZNIo9Ce6DHXYLJzT68Cy_P8TDPuPQXckilVdPT4ZUkaa2p0_0Axqitg8lKHyAxUBPHdBZNYW6K-KNy-v3SNZRDMOpzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پزشکیان: این بچه‌هارو می‌بینید؟ اینارو بمباران کردند و کشتند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/Futball180TV/107134" target="_blank">📅 17:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107133">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=ZLtOQyALGf9qz6eTnaTIPH07jcBcEkjheNJILOVZn2stxK_ZmNzL0dH79ZahBGqetKkyU-oKfEcAacXfDRcett4lkzgL56y_vSJVxseQVtz0x05CQZqAz50IAtU59_JxjxSUZGoZlUYqgMUgYLr4elUVAPrTOeS29epjbDE86G_pLv4xy5v5aqNRDOFz4htvPEd52YMKQyUWGkvcsvOflS0ETaAt6uzzxZbUp4F_bcNj77HmErn5NAmVT43FXsDoJx4tRm7jASbPSp45aEyIGmQN_hC0nVMZh15lWcU6_-FmIN6nJ71WeuUDJ4srdI1Bs7boMg0Eu0y9A43_AmthwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=ZLtOQyALGf9qz6eTnaTIPH07jcBcEkjheNJILOVZn2stxK_ZmNzL0dH79ZahBGqetKkyU-oKfEcAacXfDRcett4lkzgL56y_vSJVxseQVtz0x05CQZqAz50IAtU59_JxjxSUZGoZlUYqgMUgYLr4elUVAPrTOeS29epjbDE86G_pLv4xy5v5aqNRDOFz4htvPEd52YMKQyUWGkvcsvOflS0ETaAt6uzzxZbUp4F_bcNj77HmErn5NAmVT43FXsDoJx4tRm7jASbPSp45aEyIGmQN_hC0nVMZh15lWcU6_-FmIN6nJ71WeuUDJ4srdI1Bs7boMg0Eu0y9A43_AmthwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نشان دادن تصویر خامنه‌ای توسط پزشکیان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/Futball180TV/107133" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107132">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWKkO8Hv-kl_4Rbgl4MiPpV-Z_wkWXKLZ0CQdYS3CrKR24Kv3UnY4lS6xkM_onry4PokQjPkDALf-Y_pmUp9sFNx4Iz9cLLJTux6GBmG3YHZ4uV_YNylpL4ez3KcbxRI16OvCweoPW1PLg6OBByIgPitQgDlGnfRhnyeXmcdWWj2K6MV_54zaL04ppXY4vE0dnTngpu4xUZghCcFfX9rPPYjG15l29M5h-F8ieBSpUkbcb8dv30ug3exHXUclfcssgrmBhwhjfe5yy8Ki8MgWAfVcZGtwgkitstQt7AYqZWM1VBuivvCYJ8K1jUtQ-oVsvtWgruhTVJw9BiEoMJU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مسعود پزشکیان در مقر سازمان ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/107132" target="_blank">📅 17:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107131">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=e0Jp0KuKuAw7CtvkXJqiBm6H24PFV6DyVGDeAQczAUzRBxFhZ6eQa-Z9ThY3HkcFl9vXjxYDeXidlBbEZD8vWDO2qyP4BIEGTBZJmJGEHj3H-2eW9cjBBV0zYQiNBQBr1NLc_KGU8qatEEqGYB93JRgRSzUMU4gHx0aajaoOWcxjfS5XxpGIulCMmVsEJSIa3ZfQ7IxTUZfm-ZD3uKcLyDt--VHLC1CJ5p8zdlt6zGy4nLHauCvyT0tXwTHBVD5pO-sL59WwB38xibjluI5zXzhlPO80Cqg7oQuPk64ZA-jDly-OVIkUrKBW7bmPDxT15aYxaPaotOQbDaa_s4mF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=e0Jp0KuKuAw7CtvkXJqiBm6H24PFV6DyVGDeAQczAUzRBxFhZ6eQa-Z9ThY3HkcFl9vXjxYDeXidlBbEZD8vWDO2qyP4BIEGTBZJmJGEHj3H-2eW9cjBBV0zYQiNBQBr1NLc_KGU8qatEEqGYB93JRgRSzUMU4gHx0aajaoOWcxjfS5XxpGIulCMmVsEJSIa3ZfQ7IxTUZfm-ZD3uKcLyDt--VHLC1CJ5p8zdlt6zGy4nLHauCvyT0tXwTHBVD5pO-sL59WwB38xibjluI5zXzhlPO80Cqg7oQuPk64ZA-jDly-OVIkUrKBW7bmPDxT15aYxaPaotOQbDaa_s4mF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید عارف‌غلامی مدافع سابق استقلال:
شجاع تر از آنچه ميپنداريم، كمي دورتر برانيد ، زني درحال فتح ترس هايش است ، ١ مهر به ياد تمام دانش آموزان و دانشجوياني كه ميتوانستند در بين ما باشند اما نيستند ، روحشان شاد يادشان گرامي
🖤
🥀
💔
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/107131" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107130">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107130" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/107130" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107129">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGJkykgZD7lKoYgdBaBydWHPODaP6JpivLi_uRlqrZZlxOdrr14NibOpfzPzFMQV6rwqM6Qa23h7QkUIRaHnlx0aSkS1flKpixFExbfme7jh7Ig8uNM1GBa2QevvtIH8rZxnxAG78Lx3LU2uAIYmwuTrBss68xY0DDzUalLE1bBO8g8twFS8r2piMJnWyWcSd5xim8Mf0KOYWcE-vBlmWU6H4M_OJRwo8FDicdG5lJXUwwrB3VM4wg1iZvDmzIgaZIR2hbP4S-K09DG83tVmcntcc5Bw6VDP000hj20Z3zLnonbB9AUOARqWyX_u2cX2axK09dcOLWZhNU7VBiyaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/Futball180TV/107129" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107128">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQG5qQ4q5vls4gs5A5he1Rk4yu5xpZ2st1KLfJvNZbmpgQqeKQfvXdGJo3bZ0jtRhtwj1ixclwmO4NQ9hKudnrEzosc38a7GXgUw-JSdbPurYAe-0Ck1MJY0n_HN_0wSfhKcVQVcPSHSpf0cETrNFL1Q3JW3kvmVCHqxXiG1hTXJIVfVWHBhK87_pyFAzvtSCSy9nWqsrplrJuuqhrRt1Ls9kmGdusKpAmadoDUTTAQ4CqT4ixQMer9iry_mGH9aACVnINeVz16MrDHvB-E_bmnhhhkdGVjQmsSidd_NeSoAUIam-OVwb89fmW9CMQf0w6yrztEs2jbTwSI7ojLv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اسطوره محسن‌رضایی: به لطف تلاش‌های ترامپ، ایران اکنون قدرت چهارم جهان است و بزودی با تلاش‌های خود به قدرت اول تبدیل می‌شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/107128" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107127">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1QrcQqkdUcv7mjKfL1Jkus-0-gKds8d_RKfC-lan_2MWjnLuVO1W2y2ZW_e2mU1j4b0dFjpL3knSEqkMcsaxsHhBVj3pRY0HPJCbQzegzT-X4-dJAaqjVAYa4HJKqKJggw1pbPgm8DEH0Fgy-eJnATZBVgnZXUWrqQT8RTYmzrhbr7jFT3ZlzN4P_cQrGfBM22fNttS-_Pa92v-wxpan3neiyT9uiPmad_dDsLpSez_w2n-oxs_qpInzOLselbfJldjBQZRynHLvub8JxFNAAUgWziWS3fBAh4Z8UJmTYL95gDQv4Lvqw8rOGnd_HoCto1d0FP-zXyj72A5NEzNwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
کنایه‌های خداداد عزیزی به فدراسیون فوتبال پس از حذف تیم‌ملی امید از مسابقات ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/107127" target="_blank">📅 16:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107126">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHIj7TfGLD4AkaVF_nPN1eTsCydoF8Q3SWJ5fd8cqKI8oXPDwIFGnsqt7W4u6bI1cQ2_mcpK7p0-RSnrL81YHaxxsg9DBUxS5f5FV-RHZ8B3IYGyUNFMii9YZdUIXOnkhsCIjZ7qWMJipC6Or-xfqbT7-AmK81Q8XfmJA-pWroL5He0NswaiwOQFeqpAmfKXSX09GsepesYSvS6JGTvhcUjkXEymMtPPrlt89G_O8bzSQZO45FkcP_6-igK0wXXwgnjaav19_ZXFYOJgFUDP2N57DiQNMu12v2tJpSq6n7ZpNSorPsYlxuzyocyodjou5kdES_qgyeMhS4BsC9oT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🙂
در فیفادی فعلی و از اسکواد بارسلونا، فقط ۵ بازیکن برای تمرینات در دسترس فلیک هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/107126" target="_blank">📅 16:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107125">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=AAMV4fUyIPk4E061mJkijQ5sNc8FwywASXAd-P1KMG5AZAIdm8_gGvknBj1tLZfKVNYx7VJda0DeRkpis6KWV85l40VgfkbNzUvt9okTyNnB61ppAoCZFE0CcjlQ9Ih9bfvyCFMQ_0A0_drMiwsyb8bXmG52bQ62j63L1UG5gCjVDGoJCMYU4GliCjW67ZgdmiG8XBoRHbQLyJFwW2mZeTpYs9gQ9Hu8EyoRJDgP5QxjrSWiG1QzVOkV9oll0gQK5L0k6vhrbOkne1m24BMzJk1DkWn1xEO8kX1EW85YG0UqHmFuOWHV-EOqK0q7bKuoQl7L1MGyL1ebTNinjn6QOILoLMmFxemrcD2VqVRUc9cnG17jXLqbHRlcIC6uhAPEyg0O0LbHJEhRXCnwDGsOc0NfWTePzlOruLel3RGntH05ciCuPkIHQnQVQy7R6HNOPPByLLnS4LzLgBvpTgU8EhBLXm0JrQdai7WTI8w4xEuEUNLyvsJM7WRPYTpE4_0zPq4Hc24UlS20ws9AYkXXB1lKLGmz0PYgmV-09XgKgFj6pLf65lJj81Bdogne_K2iOmnBPmAC2DWf15p6RHs9CRU78Y_5NBZRZY-3lyxz8P7ge1kw_YmA7p_hnaJX09m22bw1G0rBlmOE-9QoPH8Sdph_QkPxaYdutAPaPctMxCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=AAMV4fUyIPk4E061mJkijQ5sNc8FwywASXAd-P1KMG5AZAIdm8_gGvknBj1tLZfKVNYx7VJda0DeRkpis6KWV85l40VgfkbNzUvt9okTyNnB61ppAoCZFE0CcjlQ9Ih9bfvyCFMQ_0A0_drMiwsyb8bXmG52bQ62j63L1UG5gCjVDGoJCMYU4GliCjW67ZgdmiG8XBoRHbQLyJFwW2mZeTpYs9gQ9Hu8EyoRJDgP5QxjrSWiG1QzVOkV9oll0gQK5L0k6vhrbOkne1m24BMzJk1DkWn1xEO8kX1EW85YG0UqHmFuOWHV-EOqK0q7bKuoQl7L1MGyL1ebTNinjn6QOILoLMmFxemrcD2VqVRUc9cnG17jXLqbHRlcIC6uhAPEyg0O0LbHJEhRXCnwDGsOc0NfWTePzlOruLel3RGntH05ciCuPkIHQnQVQy7R6HNOPPByLLnS4LzLgBvpTgU8EhBLXm0JrQdai7WTI8w4xEuEUNLyvsJM7WRPYTpE4_0zPq4Hc24UlS20ws9AYkXXB1lKLGmz0PYgmV-09XgKgFj6pLf65lJj81Bdogne_K2iOmnBPmAC2DWf15p6RHs9CRU78Y_5NBZRZY-3lyxz8P7ge1kw_YmA7p_hnaJX09m22bw1G0rBlmOE-9QoPH8Sdph_QkPxaYdutAPaPctMxCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امان از دست رامین رضاییان و اداهاش
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107125" target="_blank">📅 16:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107124">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9325345835.mp4?token=p0UcUH5lpZyZo6ZVvOUHqKdQE72bysmt5m6G4edGifqm52OxlC2FIDfrFfrUgmG5GeQCeAgnEnbayWjVmo6tlTzML7u9125h-9pMRsuQRVxUtlYAC4-YpGP6Sb9qziCENVHmmKmT8K3NBLwnQkugcdMiSroMvaIoCabKkXkTd1TJRFAKwYBWMtEKgqWVWEktIBF2uN5tHUAUm_4midq1dpq_ac1NAhBUtg6tSBOF5caPIL9C5QXaG_EJpaQ43OA2meCaivu4_clJeSdPxwdTXgBgaduDyJynk0cBUtxiH5CTkamlwSQKAVSvMGp26hPe0erfKL8LCqsFOo76Hqq4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9325345835.mp4?token=p0UcUH5lpZyZo6ZVvOUHqKdQE72bysmt5m6G4edGifqm52OxlC2FIDfrFfrUgmG5GeQCeAgnEnbayWjVmo6tlTzML7u9125h-9pMRsuQRVxUtlYAC4-YpGP6Sb9qziCENVHmmKmT8K3NBLwnQkugcdMiSroMvaIoCabKkXkTd1TJRFAKwYBWMtEKgqWVWEktIBF2uN5tHUAUm_4midq1dpq_ac1NAhBUtg6tSBOF5caPIL9C5QXaG_EJpaQ43OA2meCaivu4_clJeSdPxwdTXgBgaduDyJynk0cBUtxiH5CTkamlwSQKAVSvMGp26hPe0erfKL8LCqsFOo76Hqq4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شوخی‌های بامزه ابوطالب با پرسپولیسی‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107124" target="_blank">📅 15:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107123">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=bDqGH15T-XKPIzjWQcsk77qkvno1gSi6DRoQtDMJAtKfwhN7x9fKA5ktBElBuStoBYyzlUDZDleNlOJoV7rda3Ws_jMKhwSff3wLOOOycmu0sa1_u4Ga0x-ImWL9RcG2l-Zkj_7yuwwdKRHmQMIBj1v-Td4c64071uwZnMrpSVxBQFo5bYO-PoiMqGOw--KlhC9grjtyj66qLFnb5I6iZ8YsOW4Om66x8bG_vmBAWahNJOALaseEHG4JWYyny-qI8a7YXi5lQhfqvRLhzwpoxWGF8IKa1LTv6j4KYc5kCxA26hqZDRWI0S1rHhCmXAqmPR67NW1SiuqDUmzTDJS6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=bDqGH15T-XKPIzjWQcsk77qkvno1gSi6DRoQtDMJAtKfwhN7x9fKA5ktBElBuStoBYyzlUDZDleNlOJoV7rda3Ws_jMKhwSff3wLOOOycmu0sa1_u4Ga0x-ImWL9RcG2l-Zkj_7yuwwdKRHmQMIBj1v-Td4c64071uwZnMrpSVxBQFo5bYO-PoiMqGOw--KlhC9grjtyj66qLFnb5I6iZ8YsOW4Om66x8bG_vmBAWahNJOALaseEHG4JWYyny-qI8a7YXi5lQhfqvRLhzwpoxWGF8IKa1LTv6j4KYc5kCxA26hqZDRWI0S1rHhCmXAqmPR67NW1SiuqDUmzTDJS6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جدیدترین صحبت‌های رامین‌رضاییان درباره عشق‌وحال با توصیه به بازیکنان رده‌های پایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107123" target="_blank">📅 15:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107122">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=TlSVQAz2HrEzTk2i5prHdtWrToVycX6-F-PfzLHXI9QHpoxPknRGdDe4HKDiWJ8_lzRMCcG0DGmk1t6Obkbdtf6rLMBR_1Y1qaUzCo12lUhYDRATRynSfH4R3a7iWfVSHKyFdygLPE5Yf_s-JGMb9NMu0VcOgJixwxDbxETp6fXWVXQJwu04Bly9YqvSw1lmLsGCkktUr42mvym_qy_w-rYQm-vHv016hqa9wUX_hddFEsRQK4OEwfvBHm48X8AKPe7rn5foXjlBw_sPM9sswTxlogM5meCUV3vM5A43eCv0CWlXapelpBHI1UjYiXEdwYCTOQL8Grtl9ZYzrRq3pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=TlSVQAz2HrEzTk2i5prHdtWrToVycX6-F-PfzLHXI9QHpoxPknRGdDe4HKDiWJ8_lzRMCcG0DGmk1t6Obkbdtf6rLMBR_1Y1qaUzCo12lUhYDRATRynSfH4R3a7iWfVSHKyFdygLPE5Yf_s-JGMb9NMu0VcOgJixwxDbxETp6fXWVXQJwu04Bly9YqvSw1lmLsGCkktUr42mvym_qy_w-rYQm-vHv016hqa9wUX_hddFEsRQK4OEwfvBHm48X8AKPe7rn5foXjlBw_sPM9sswTxlogM5meCUV3vM5A43eCv0CWlXapelpBHI1UjYiXEdwYCTOQL8Grtl9ZYzrRq3pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
مقایسه فوق‌العاده سمی ابوطالب حسینی از فحاشی تاریخی مرتضی فنونی‌زاده و خداداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107122" target="_blank">📅 14:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107121">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=qEVlkgYbdayQ1OiPun7Y-alsfM0uGa5ZezRVefVg6kDeUstZsjLjf360-0LDm6hw2o0d7rNKhR2-GyfBt6Tb8w6a8bKJF_vjt3EKW8EGfjLtdCDFTQJxsgqmSyKQ9six70NXdIYWU1CRAZke20NDuZCfSET3Xog5bHZp4_7AfuEBtQqYGRFE9RKmMI5LpOWvg4SrWTjeuuoIBYhzU9Ci5GaztRRvoagAG0qUtk4ZNXlqpxaxHvkTTFBqKlBLUa0PcihBuZFuodYmoySrkZZFsH5se4t4s4n811O4NWyxAxnZcf1I1WrP1mP_qf96wMCQOxBoEBRT1-RuBIUFGJrnGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=qEVlkgYbdayQ1OiPun7Y-alsfM0uGa5ZezRVefVg6kDeUstZsjLjf360-0LDm6hw2o0d7rNKhR2-GyfBt6Tb8w6a8bKJF_vjt3EKW8EGfjLtdCDFTQJxsgqmSyKQ9six70NXdIYWU1CRAZke20NDuZCfSET3Xog5bHZp4_7AfuEBtQqYGRFE9RKmMI5LpOWvg4SrWTjeuuoIBYhzU9Ci5GaztRRvoagAG0qUtk4ZNXlqpxaxHvkTTFBqKlBLUa0PcihBuZFuodYmoySrkZZFsH5se4t4s4n811O4NWyxAxnZcf1I1WrP1mP_qf96wMCQOxBoEBRT1-RuBIUFGJrnGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی مدعی شده که یک‌سری افراد میخوان این یابو‌ رو حذف کنن ولی حذف شدنی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107121" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107120">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=eR92BCmug5eVtKOmu5BLNY5emq3lHNNENxfQnyrCiX6H2dSroAGHQCi78V4bU3tM0CHEZb5PyuD5ErapSAPCfo0B2HJplgQc4Y7CqQRrK1hamBb9EChELLGqzO8fWSBz6s5_NAAqxbtLP_Yg1LGba7LfBuR_2fuQNtw7YVQbvWnGVZxyiyR0Y4WdPYTJMhZ0o-D5GLXK4tQRh1_UTjtqpX7UFY11PMszK8-aqUnZ6eBpPN8ndTMa7fcOjesKP-yHdWV9fLHXXaVN_N_eEWdxcfbilLGsGhF2L5fyXypiTs4a8YPuAe0_HMZFBUvIZf_M06zEtkZwXJbsOVUSwiZbXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=eR92BCmug5eVtKOmu5BLNY5emq3lHNNENxfQnyrCiX6H2dSroAGHQCi78V4bU3tM0CHEZb5PyuD5ErapSAPCfo0B2HJplgQc4Y7CqQRrK1hamBb9EChELLGqzO8fWSBz6s5_NAAqxbtLP_Yg1LGba7LfBuR_2fuQNtw7YVQbvWnGVZxyiyR0Y4WdPYTJMhZ0o-D5GLXK4tQRh1_UTjtqpX7UFY11PMszK8-aqUnZ6eBpPN8ndTMa7fcOjesKP-yHdWV9fLHXXaVN_N_eEWdxcfbilLGsGhF2L5fyXypiTs4a8YPuAe0_HMZFBUvIZf_M06zEtkZwXJbsOVUSwiZbXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لحظه‌ای که سیمئونه شورت امباپه رو کشید پایین؛ سیمئونه گفته اگه قوانین اجازه می‌داد حتی اون‌شورت دومیش هم پایین میکشیدم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107120" target="_blank">📅 14:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107119">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=QgiaEfwa4DMfPiPN00JsUCt69yVSnj37vqb-Dfy-66p-DPGx18zjNX_60WOJIGG3d_umohRXnCF6-kvFWjbwMRPD_YfXITLzuQ7Me1m7T84DLWt38bJcGLxgVJVjZzXsBC2xTY4dM2nQVhZCg8At2sfODzjqRMhTBM4PJCom17milpj7Zp96K-j9Q-YILZcy-Z0jaKjPSO3bZhBtSg3oOvCppY5IY03w2wxJho4OkFxgSpSIk46YfJU02ohVYPfX569R1G1R7jOssN6QMoRCOO9SYuByEhYs_Hz6NEi8eEV_uOGVqvwcWVV49ZA_y5w8dUPkzf8RSoK_hEER1E-ENg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=QgiaEfwa4DMfPiPN00JsUCt69yVSnj37vqb-Dfy-66p-DPGx18zjNX_60WOJIGG3d_umohRXnCF6-kvFWjbwMRPD_YfXITLzuQ7Me1m7T84DLWt38bJcGLxgVJVjZzXsBC2xTY4dM2nQVhZCg8At2sfODzjqRMhTBM4PJCom17milpj7Zp96K-j9Q-YILZcy-Z0jaKjPSO3bZhBtSg3oOvCppY5IY03w2wxJho4OkFxgSpSIk46YfJU02ohVYPfX569R1G1R7jOssN6QMoRCOO9SYuByEhYs_Hz6NEi8eEV_uOGVqvwcWVV49ZA_y5w8dUPkzf8RSoK_hEER1E-ENg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه دردناک سرقت تلفن‌همراه پاکبان در مشهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107119" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107118">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOKCXLmGNxq_5Vdnw_2hqlstWOS9Zju9xSJ1_hc2w3MdIUpGmCDoooCaFTTbgX54giNfFSi5f0B9TK9aYZ8u8IF7XUPGhJGLLAnVV9WD_gJTQaQS3tKoH4NFdebVB3PRLKDXThRKzv-7keDoRapJleqao06hcYkDAX05tS2XH9_7MI-xIcwnaowb9nyaq4b5aZyaaCvxnPx3oaYCNQH5u_nuzm4P7ffFHdhRorl2G4Onvar9xDDCMHZ2Rzr_irF6VkYJyjtx37X8FAYB7EcsXqp-y5NiFhjXPejucLodHH2uUsges59-n9bbPIuriJ65h7Xep0bm4nOQTn7-GrSnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
📊
5 بازیکن برتر در زمینه خلق موقعیت گلزنی در لیگ‌های معتبر اروپایی تا به امروز:
🇪🇸
لامین یامال – 6 پاس گل.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز – 5 پاس گل.
🇫🇷
خاویر هرناندز – 4 پاس گل.
🇮🇹
پائولو دیبالا – 4 پاس گل.
🇪🇸
آنتونی گوردون – 4 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107118" target="_blank">📅 13:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107117">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiB3scoQjTeAmWB8NrYqm-h5qBSdR9iohkXA6EazK70OXokUJQqB9yA-P9Z1O1QXec0DQEVJEknR6PXu0inqvPPDq9_nE16fVxF4R2w_gN02DGxUEnkHDnYcFitLiB4jWAQE8aH4HFE26st0JJeVdxLh_S70E5rNwgWq0nwaj7rq2OnC73vOgD6ibsL_9n1ciIl0KJf_ds99l4EFiV5p0196lLstxABNEMVFXpaijEFvOyUiDrR_XA4RTo_28P57l56h7BfivasepeIV8Fr-Mx2DJF0em5xaaHsV2FzvuysiIVJjRgr2H9v8YJLbCw4K5l5LQAqF7HCNkRBdQzOJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خاویر آگیره سرمربی تیم والنسیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107117" target="_blank">📅 12:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107116">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocGTV_2zloGhXjzXmBgA1RFQtYsVsydXJsG_P8Wt_bk7BqNtrHvvuw2tGcJLu6Gc2OSAd3rubyBY2qjl4GBBsYE7BRnYFOQSDmwgYf_y8jh_SN7WEGeBeeFTs28V-qcMUhEKmS9yVp2n890IiGQkZMu8uAbVlIkR6A4Mwg5S7S_e3C8iG9AX0LSxp3929xH31TSbg-Z_uWNiSSGczDoSUKSYmj7-BGHQZw0wDEQoOELwcoPqiCTLNKJK0gyv89MVy6plPrglSHIzq1YbER9LesrASdhTTVCXUQEVaua_JgxIJ8o3AXCpaWcx6QJZ3hhIYyBqA-1ifwgWHLmNjWRX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107116" target="_blank">📅 12:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107115">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvin1MBSNjselkuQy0SvJvMxzYZ26QCj__o_Szov0HRjb3vODi4Rgr4fGIqm3TBchNLx2QGfEc9NxZIzLtoKp3N-sfjzAL0TPEuwFtV6umhvHXmv779oTp44C0NuTwzGRyqDFoV__FnWMTD_dpdY60bbXFne1rldrwCz10gBS4bHbLj_vk_2lqxNzXWtc5V260GKJ0OPRtwVZtr2UIrRawizlXrod2Wk8aBkHW_anui2cmYigL1oZQfRJULqyH77YQuuhOk1ARp9I1rOt5mJmkz9PJliHr5vr172Tr_iXC9oKup491P_TCqtvUVb0uXGgW1vfx9LsWW1vNRCRMhapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خداداد عزیزی از اونجایی که خیلی الگوی خوبی برای بچه‌هاست بردنش یه مدرسه تو مشهد تا زنگ آغاز سال تحصیلی هم بزنه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107115" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107114">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a29oajhSbkSrelgw66WvRT3LOXbf-lHoBNNagwcLO01UlC7zaHpG18zl2csd8n6mLM5olPbjdp4wLlIzkwwinAXAjKWAjO3otpGZw1QOZh8LzPVN0D_QQcfs32_5EhfxoyzjO_jk0c8HJeT01dAQD4TgPDofS0eyjEldWMJJP-DG4x1TCRI_j4vTvyF3y_Xv4vDrLkSw8X7RoDIAZVxUbg7T20jr_OWNeg-yFXPsCIlUhcz3xyE26YruwxpE14zspJGw743hPmYk6XmfO5DYHPP_shpu4Q44zAV54kK-eSfUOlUQvNjLN9hdFG5KiRca0spThXWxE-fbdbTYuVLfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان امباپه:
🔹
"من نظر شخصی، سال فوق‌العاده‌ای را سپری کردم و این مهم‌ترین معیار برای جایزه توپ طلایی است.
🔹
من نسبت به توپ طلایی امسال خوش‌بین هستم ولی اگر برنده نشوم، ناامید خواهم شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107114" target="_blank">📅 11:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107113">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53478857b1.mp4?token=c9GtfbSUMc-nvPkwnl7sTDsFcVaJqEsXk-wf40mHjeREi-mk06xuqx-eYaLBQVMGPMabn2Jj0MK3tvmFXQgfTajqZJAa9ugGWEb_s7ppxfjwZnANNKQiWEEusTSYcxGIcQ1OgNPVG4fniklOZAusGPJyNtFpjZ9_Dmt_b0rhtQH5Afp_OhiBC_tEAN5gw2e00cY5eiRSl-mKtSb9zNT4eNGr_GPjDVILHJ-qp6RpgzR4IKa9N9uXyrrVe8FhFuUg6CN5mfNv3UXibcp4bK3X0wS1yFNjciv2c9UVIiSbaQejl2zFBaSNhtC6k1BzMLrQog8XfbrZkfkoix0j3C5fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53478857b1.mp4?token=c9GtfbSUMc-nvPkwnl7sTDsFcVaJqEsXk-wf40mHjeREi-mk06xuqx-eYaLBQVMGPMabn2Jj0MK3tvmFXQgfTajqZJAa9ugGWEb_s7ppxfjwZnANNKQiWEEusTSYcxGIcQ1OgNPVG4fniklOZAusGPJyNtFpjZ9_Dmt_b0rhtQH5Afp_OhiBC_tEAN5gw2e00cY5eiRSl-mKtSb9zNT4eNGr_GPjDVILHJ-qp6RpgzR4IKa9N9uXyrrVe8FhFuUg6CN5mfNv3UXibcp4bK3X0wS1yFNjciv2c9UVIiSbaQejl2zFBaSNhtC6k1BzMLrQog8XfbrZkfkoix0j3C5fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه گزارشگر صداوسیما به قلعه‌نویی و عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107113" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107112">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1yn0lD3Vb145FN8xomL3DA_cC7pYFuGsVwjytvpwwzD0JsZS04BF9lFpQRYIntLcEIfHwySchpbD3shaXD-FoVD66g-CI7xmXbyYVXTRcUzfm4lJLpv9Gi8P6PLquPRe0Arx2lvomOgNRl6MmX5TxW_RS9kdqHpRJvD6kowtQeHatJJgqFsadD2A0LFzsCDLjsw0LsF4DA0-DnHxnmCi_3VVAsyvTr-rw3fNrp4rQrchX8EH71DZjn5hLDJht1y-YqlpQtLNbp3m47n4OkktloHsfIbg_JCJRgcVm2D34XDQh1Bqsvg4Bqxz5o1ZbuElEJlqEIGCRvvhW6-3qaS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
رافینیا:
🔻
"به نظر من، لامین یامال باید بدون شک برنده توپ طلایی شود. او آمار فوق‌العاده، افتخارات، جذابیت و کاریزمایی را دارد که او را برای این جایزه واجد شرایط می‌کند.
🔻
به نظر من، عملکردی که او با بارسلونا و تیم ملی اسپانیا داشته، این موضوع را کاملاً واضح می‌کند و او شایسته این جایزه است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107112" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107111">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107111" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107111" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107110">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8ulsxGLTf-i73_7HduF4Dixj8O0ivyKh_TY_8fj2NSyCJxCIZX-0izbc00MOR-RsbrOJ3jkWT-x9F1WUEUsgT_Qz5A2zk6f8rKV88_Vn-kYG4Q9uSP1qulgDWuYzv_DJcSnbnXmAzllWncjguQcwinWqqw111S6YXHOShL51794kyyb-8Wvj4QYupDktmSnZ6_NRzwuZn6SDze9xtd9kfUgsiq8lVfWphDvkW3qOmrHh56eX79OuesyqQ-G2TEffqi5PWnSC6cJYLSnQpJpahKrY3EuNZTxCIMm13ALOzvePsPIEHchPgsxcMt_G6fOKZdbCr5EWip1G_KxnD5jIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107110" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107108">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9548a0e3ec.mp4?token=TM5kRr5Dd8BHdNjihYaBhvU4cUPg9ytI3BZEFa14b-gs_bCay6hfyHjOtCk7npJo69YXWpxInip5Ymh2lIkJLW4yS54ZFI6A-AHaA9toEZ_s5BSE_FeanPeohl1WUEtb0zh1-WK5t6qi4SET6dxJodf3csXxWk4hsqy-o-KwxtkDTCYLTp4b9RMfWFQqKXS0scYssnQNZV5bgkuj4dgQxZ00WN6hsjR1F52XII9HXe5YcbIhQETlR_iPazf5jNPxr3NoxIxTrYj2OxA1nY68fiYyGvYWKwv_V1-gjqApusUGR8Q7IGQ5UkDdnsa28v7Ufq0-LUNp3eoAQB2OQ7R3LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9548a0e3ec.mp4?token=TM5kRr5Dd8BHdNjihYaBhvU4cUPg9ytI3BZEFa14b-gs_bCay6hfyHjOtCk7npJo69YXWpxInip5Ymh2lIkJLW4yS54ZFI6A-AHaA9toEZ_s5BSE_FeanPeohl1WUEtb0zh1-WK5t6qi4SET6dxJodf3csXxWk4hsqy-o-KwxtkDTCYLTp4b9RMfWFQqKXS0scYssnQNZV5bgkuj4dgQxZ00WN6hsjR1F52XII9HXe5YcbIhQETlR_iPazf5jNPxr3NoxIxTrYj2OxA1nY68fiYyGvYWKwv_V1-gjqApusUGR8Q7IGQ5UkDdnsa28v7Ufq0-LUNp3eoAQB2OQ7R3LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دیدنی تیم فوتبال الکترونیک ایران به حریف ژاپنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107108" target="_blank">📅 11:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107107">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcZwqwg4VzZvmK_5z1WitwS-ncBnM8ayg-83iBcF-iJWAtMlN5q4M048u6PMnMsc6qmP3Etv5gSEJwKgQInK58F82zCR1V1nKFN-g-onBUWl76uK3VeG4g25-vDvsh4Y8Rn9Y9mx735UzJ52IOo-Xy6sG5nsWlWtYIhkHiIUZqYWaqeqTl7QKsDCm9MgvQirn_-F2vn6U22pWFvuKZDNR8jStM_Uzb4TKqcl-MC2T7qwksW_fW6K7PnEr0EewsNXbZlxSRSavKCMjKeYfomItnLmotlQEQSu3c80CeS0veuHGaYgw83rYayBs5q0izmz53R2AiAggSjhtDbK2umQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107107" target="_blank">📅 10:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107106">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWFFjfiEqb5NToyvnk3MC-qMlQtn6f_YWipnD2leyLO8-eNXUzt82UtZUadp6rvMk6KkK7C4Plgk9hkc-y4psMCfJ2y1yw0T88dbPgv-wJ2eatB158ZWUZvGD-qPFkpS3tsobD4YYrgGUKo3uTPVoJgeTQl2rn5bo3aTTfWn7SR8Yuw0UOud4v9ODtVh_ug2W_uwcPQ1Tsa2viC6XM42ddx1nIeqIYWvo0Bu34pITB76j24I3gEAQ0gP7-s3VdfuiEfXRI51QJwbDc_0jyUnlR0BAI-rL5HXdBlNw9LWBfwbnZKoOBLssGgfviQiDg-oJ2w-rBhhrWeiNOc3uemdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی|شاهکار حسین‌عبدی پرادعا در ناگویا؛ ایران با شکست سنگین مقابل پسران کیم‌جونگ‌اون از صعود به مرحله حذفی بازماند
🇮🇷
ایران
😃
-
😀
کره‌شمالی
🇰🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107106" target="_blank">📅 10:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107105">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnHmLD2dAyaFH8NGYyPPoiAIMslHKpvYRNkEWPU2p6qSpwL-UDGjqqRDUu6Xg_TmezTC3VqI4taAKak-0ZREO1ngrbP8vXyEe2XfqfeZ8Q4cPH-flyfVEMiWeNfcgC3jK3C8Dl1oPE9NQXfPjSanBBWi1jf4KLmm3aWaHtcZ6gyKS1AWtBO9qqldwffszZDLpR9UgsR93ynGmvB_6baOtTVwLZ1UjCFRTgm6GjaEbBWUv0cXc332CpZWnJkANJrOPeXz3levE2vEsxXhWk3AIcl-6v3Z4e3FsSKpiDceFEUqYzSu6BJRLjKRgRkyU12WxPVP1iV8XqAOhqbxiXS4JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی|شاهکار حسین‌عبدی پرادعا در ناگویا؛ ایران با شکست سنگین مقابل پسران کیم‌جونگ‌اون از صعود به مرحله حذفی بازماند
🇮🇷
ایران
😃
-
😀
کره‌شمالی
🇰🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107105" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107104">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65dff3514a.mp4?token=WgC9GBTlk0CiJ7H1ttle8GUyGYc21nGo07rsD2-0epvA0gqqsFk2Iji0rAMHpUu5YnGa9aZ9EDS76nMDhtS4Svyci1kDTiMw6Mv04XQLu7aGd68EMfVFQJkb5brbECOJB6Qg2wHBsiBCegv35xQRwCx-N3dM6cnkQpw_AMOsP-E3J05svzFx8Q4nYwdISv3gAxq4k7tSexTnWWl2F5NbqxzzqkHx4vCw18Yq_8CR2H9j_Gsj3EdMN9d6PT0X_Sphg1vHpqA9W4T5vnJXeElLer78hCVzUIv9XLfEFuJdgSxU9POGycinMgKV_K9C7VCH4Hl59Oiul8JrjAnJNwigKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65dff3514a.mp4?token=WgC9GBTlk0CiJ7H1ttle8GUyGYc21nGo07rsD2-0epvA0gqqsFk2Iji0rAMHpUu5YnGa9aZ9EDS76nMDhtS4Svyci1kDTiMw6Mv04XQLu7aGd68EMfVFQJkb5brbECOJB6Qg2wHBsiBCegv35xQRwCx-N3dM6cnkQpw_AMOsP-E3J05svzFx8Q4nYwdISv3gAxq4k7tSexTnWWl2F5NbqxzzqkHx4vCw18Yq_8CR2H9j_Gsj3EdMN9d6PT0X_Sphg1vHpqA9W4T5vnJXeElLer78hCVzUIv9XLfEFuJdgSxU9POGycinMgKV_K9C7VCH4Hl59Oiul8JrjAnJNwigKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم کره شمالی به ایران توسط چونگ سونگ(68)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107104" target="_blank">📅 10:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107103">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلگگلگل چهارم کره‌شمالی
😐
😐
😐
😐
🚨</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107103" target="_blank">📅 10:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107102">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c68b593c8.mp4?token=tlTaT7cSgx-MZ2Xmb2h7bYzkOrKyjowvLdJeYknMHrUJOPujHmOZTWLOkv7IbYrnkuHhk7e6DkKp45_tM5Nqei7IkYBhPxgs2eCgygd-tGBbnEAlBIiYdCtJz9HewwfKnG2qR-5GwCPNZjHQmqEou7GfjI3NJQs5Vp7HHdxLmgsK7ccePcZGdobZXycVLzGUTFLlO8mt0DACVOzKp-7KAxbzLBTeJOjYhg28pYYWXQCDGGdgi8Wd5EyW4hc6P9scrDQdPkNrJkgb4CLGA-3kh8TcUBXTE_xliZ_V9kBpNms8s9KNSbUYEuNkqUUOw3Nve47-d7VCp6ROlTSw68YSmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c68b593c8.mp4?token=tlTaT7cSgx-MZ2Xmb2h7bYzkOrKyjowvLdJeYknMHrUJOPujHmOZTWLOkv7IbYrnkuHhk7e6DkKp45_tM5Nqei7IkYBhPxgs2eCgygd-tGBbnEAlBIiYdCtJz9HewwfKnG2qR-5GwCPNZjHQmqEou7GfjI3NJQs5Vp7HHdxLmgsK7ccePcZGdobZXycVLzGUTFLlO8mt0DACVOzKp-7KAxbzLBTeJOjYhg28pYYWXQCDGGdgi8Wd5EyW4hc6P9scrDQdPkNrJkgb4CLGA-3kh8TcUBXTE_xliZ_V9kBpNms8s9KNSbUYEuNkqUUOw3Nve47-d7VCp6ROlTSw68YSmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل دوم امید کره شمالی | را میونگ سونگ '44 امید ایران 1 - امید کره شمالی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107102" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107101">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23009325d2.mp4?token=XjpMapAwKcmcIi7Q2rUEp76tVCYwiqh4QSIuQD6RaUCIxwfIjv_wTlzRiOKnHM7GZulLDRVMrbhb6dyP-SOxV_YKeAXwRckO5HDApBolE9Fcy1fH7e3sbE6DwA7VdOcjH8PRgOwgervb1riRGTmSF--mi_xihJCDF6u17BeeRJrEOuOjKk_U_ulufCQm1b7vUcJDG4DZ26KmCDpJhnZ2bbHbBFlTWn99e-tPilsw_dDsAv10GuLoF19Td4A50df2uh2x9dzbCKbderH4jmUfgz6D-JjE7p9mN2bC6G_FCrWA1A_pRbIaf_ConJXvzbVdRJcT5zMYnHCgPY2_0ohjBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23009325d2.mp4?token=XjpMapAwKcmcIi7Q2rUEp76tVCYwiqh4QSIuQD6RaUCIxwfIjv_wTlzRiOKnHM7GZulLDRVMrbhb6dyP-SOxV_YKeAXwRckO5HDApBolE9Fcy1fH7e3sbE6DwA7VdOcjH8PRgOwgervb1riRGTmSF--mi_xihJCDF6u17BeeRJrEOuOjKk_U_ulufCQm1b7vUcJDG4DZ26KmCDpJhnZ2bbHbBFlTWn99e-tPilsw_dDsAv10GuLoF19Td4A50df2uh2x9dzbCKbderH4jmUfgz6D-JjE7p9mN2bC6G_FCrWA1A_pRbIaf_ConJXvzbVdRJcT5zMYnHCgPY2_0ohjBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل اول امید کره شمالی | چو کوک '41 امید ایران 1 - امید کره شمالی 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107101" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107100">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663cefc9c1.mp4?token=G41pLqkkifQ9F0-0plze3i5I27fGP4uwLWJt1QmO-tf11k98eZe8MRdaX1gWnvOOKFFJ8iCeBGKXP5eOvQB9VgYffsUJPJuCFOn5wX82IEVOK3ONDvBsts6q5lcHZE4mIzAZiZjm8Ya4Xfa8YGmkeVKEjt3QZHzBQeLyKo_N_qbVjLT0wJ520cjf4KIRwXhkarZzCHbYO4YCQMC5I4h3UY5ZWzNQPaV2Kv30XeZEn5rz4snEekABgs9fr4ysJTHj2S_sfQyCxC1PHsYWKHMAqGXRa5H9l831MuRB_D3NK_EQAsfQW1k-pR7KBRJqEmtol2UNFSox76VaZIGNqEnb7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663cefc9c1.mp4?token=G41pLqkkifQ9F0-0plze3i5I27fGP4uwLWJt1QmO-tf11k98eZe8MRdaX1gWnvOOKFFJ8iCeBGKXP5eOvQB9VgYffsUJPJuCFOn5wX82IEVOK3ONDvBsts6q5lcHZE4mIzAZiZjm8Ya4Xfa8YGmkeVKEjt3QZHzBQeLyKo_N_qbVjLT0wJ520cjf4KIRwXhkarZzCHbYO4YCQMC5I4h3UY5ZWzNQPaV2Kv30XeZEn5rz4snEekABgs9fr4ysJTHj2S_sfQyCxC1PHsYWKHMAqGXRa5H9l831MuRB_D3NK_EQAsfQW1k-pR7KBRJqEmtol2UNFSox76VaZIGNqEnb7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل اول امید کره شمالی | چو کوک '41
امید ایران 1 - امید کره شمالی 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107100" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107098">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b315f04dc.mp4?token=MqwGaflYArnK3Q5CqjDffV-kqqkjsJADJxLqH-v9i0OR2uBWHiAlvTGweXzONKK88n9yes8apLBt9n2dCKracB14jM-X30q8AcQ5x9ETMJ-D7TTOJaAdOV-fiAs6kl_49ga8DxkcjCTMY4mbxqMBXapruGIT91lxUDliLlu9eE6Rd1BQ_tlkv2xtQJdsURWAayILKAfuaI3R_kmSqYYkiJhJbMmn8IbrEudT3JegaWZ-2SfbIdcmRN_eHVN0eCMo1P4_r3Ol97tVg4xWcmMt82B5C-7WkAW6z4GWUE2yF7tgvGGI_I6qXolmVZ0jwzSxBkg0D5WSrbBIr_cC-NJD4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b315f04dc.mp4?token=MqwGaflYArnK3Q5CqjDffV-kqqkjsJADJxLqH-v9i0OR2uBWHiAlvTGweXzONKK88n9yes8apLBt9n2dCKracB14jM-X30q8AcQ5x9ETMJ-D7TTOJaAdOV-fiAs6kl_49ga8DxkcjCTMY4mbxqMBXapruGIT91lxUDliLlu9eE6Rd1BQ_tlkv2xtQJdsURWAayILKAfuaI3R_kmSqYYkiJhJbMmn8IbrEudT3JegaWZ-2SfbIdcmRN_eHVN0eCMo1P4_r3Ol97tVg4xWcmMt82B5C-7WkAW6z4GWUE2yF7tgvGGI_I6qXolmVZ0jwzSxBkg0D5WSrbBIr_cC-NJD4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول ایران به کره‌شمالی توسط حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107098" target="_blank">📅 09:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107097">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1971f21e3.mp4?token=KOQ_J_1JEj_Dp4lVFk9bw5po-Hr1JejPVDP7-eaVR28Vs1YtiMtaDDajBnEzuM3Y0dzXkoLMQsSzIZRhRvaIHRkJmx2F0DUXloXzRe2qHeFDh0oS9pHlo6BQMlouQf-Uiai2q-9HLvi9OcjcmFnZTrNXeYHxaH3RclNIfIQSbF1n9xJsdDoSqFttRIdv0wnUhAZTuA185QIQ8X9eXmZz-xNKKo2tqOIIb1sYw2FFGci-0R4JPYoN3W1K-hoDz_uRpKO5QMyXvgLq0r_DmEVJXfhWcNaxgt5kvtczF_t9Qq2kmSUmbLTYikUoWZQRfshZK9BGlx91xGnUGycVVk5DVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1971f21e3.mp4?token=KOQ_J_1JEj_Dp4lVFk9bw5po-Hr1JejPVDP7-eaVR28Vs1YtiMtaDDajBnEzuM3Y0dzXkoLMQsSzIZRhRvaIHRkJmx2F0DUXloXzRe2qHeFDh0oS9pHlo6BQMlouQf-Uiai2q-9HLvi9OcjcmFnZTrNXeYHxaH3RclNIfIQSbF1n9xJsdDoSqFttRIdv0wnUhAZTuA185QIQ8X9eXmZz-xNKKo2tqOIIb1sYw2FFGci-0R4JPYoN3W1K-hoDz_uRpKO5QMyXvgLq0r_DmEVJXfhWcNaxgt5kvtczF_t9Qq2kmSUmbLTYikUoWZQRfshZK9BGlx91xGnUGycVVk5DVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
دلقک‌ترین استاد کسخل در تاریخ سرزمین ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107097" target="_blank">📅 09:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107096">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/625edd4ac9.mp4?token=nNUOs3ksXEuToY79NX0_5c8OjkUvMhMbfO1Frh0TrbwBtZg_T2dQvMsBwQL2ySqBqR72GFso9FQy6-XmSMTVLnJAeld1YXiqnNScJ0BfzkClfkBJGdtPtnKbKKOscA4vHFo0OxfYEi1-iNQ2Fy_f4CmXASnov9Lixq4-NyEgp7rYVwjJ3NcZOcgcVj4qVWKNy_CJFEo-96Sw5XyMstzvo3WIVArYiZv0Nmc11hgpfKebDO58lb9DodRoeb7wRPZ-D9anTvQQ6tRw2ItrHyL-8QkGExJ2KrF2H-mBy1wNWR6XM_ZXGk6OSPtg3sRdiFu_mqVrljwsfZL5BZHhsBZ29A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/625edd4ac9.mp4?token=nNUOs3ksXEuToY79NX0_5c8OjkUvMhMbfO1Frh0TrbwBtZg_T2dQvMsBwQL2ySqBqR72GFso9FQy6-XmSMTVLnJAeld1YXiqnNScJ0BfzkClfkBJGdtPtnKbKKOscA4vHFo0OxfYEi1-iNQ2Fy_f4CmXASnov9Lixq4-NyEgp7rYVwjJ3NcZOcgcVj4qVWKNy_CJFEo-96Sw5XyMstzvo3WIVArYiZv0Nmc11hgpfKebDO58lb9DodRoeb7wRPZ-D9anTvQQ6tRw2ItrHyL-8QkGExJ2KrF2H-mBy1wNWR6XM_ZXGk6OSPtg3sRdiFu_mqVrljwsfZL5BZHhsBZ29A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
هیچکس نباید قهرمان شود؛ خیابانی: فصل گذشته باید از تاریخچه حذف شود
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107096" target="_blank">📅 09:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107095">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107095" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107094">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107094" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107093">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfrFY9Hk4MCifHyW2Bpa2woSRg4NsAejrl_kSizv8Wcz3pUnP0Ht9Px_uwZ8vE8S5nGZh1zRoXY0wNxAiLffaZ4p5eM5af28XJ_fChsDedOiX--_SoDvvRdY5qNFFcjcBo13tsTisFvmKST2JM7Hz_EepwV2U8whGGsT-tHwe63z3SedhAt6J9ymArbl6XHWSlXgksxTtgzOonKMaaQo1CDQiBBNdbB9F2NpnzxAimQKYuJhb9njoPw8pd0nqd9-e_3Ph8jbO3ia2HzIiR_jBvzGA8FhqHxHm3vBINKoozG0CCipmsKktrTtHczg9LA9-1sLUtWU3uG7yg3mC_I_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو اعلام کرد: قرارداد آرتتا با آرسنال به مدت ۴ فصل تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107092">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Siukmh3VqTiRt5AShb8VfjrYz6HWahS1bqso6DEyolfhNnNBJn5nrGL5NT1nC260AZ3skuOOVsF2MFU3V2l223pz_EqNS22wzNOAv4viaz5eVyZbo4ybC7UaGj0xJfABuJ-g5HeGv6OcVOSFA-qQByJgdixOOUlTTtprHAJZGShmDN-dKcIKgAASIdfmLSlq5tFuDKaYCCe-l9CxTBkDQdaKheqG30h8ohaTMC-onlEJnuzwwPjHtMXKcIdYgTaRpQk5vqJ_tWS6qEUfRrS0pvGB34z4gwejp5asWMqlWN-V1M1irNIggilQ4uifglAbWq1hNKnHoCg0p_S2Ak8CIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔥
بعد فیفا دی عجب روزایی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107092" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107091">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rujAL8pUzTaMuNt73fA6KNH-1s8iEiEuyjbCZEB8QwQi6sZa2dHfocCRozuC4uy3BZ_l2kxSweznU8Gc7EBcHqAESATz4Q16KmU0CKSDFfSywVcx3GJtNnUG14q20gvznASWQkPFFrOKEsRkzAk1tKDEy_q5U8schaK32kbQ6vq6mr-INkMXUCFCnCPu81WX4O4BbHGB0d02qHikh4UKGtWOr6Blgaq9HpeKoCdYO0iAzvfCSRij890xLFQQSHz8PcNVUb6qYRDhwk51IPN2AT3vb2tbUK99t88UEiqc9Ia_j6nF1Eei7KazQT4xaO6WftZQd38QIe4CBqKPaRdniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیفو سکسی عربستانی‌ها برای بازی فرداشب با کویت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107091" target="_blank">📅 00:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107090">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhVI5qpphDMjBHsxQZOoqoncY1ApjLCkfqBMPWCGaEZnX6meX0Jb3W68V1tkC2YpN8b_4fBmyNf4Ej-FHrQscyR_lnoA_6FERbjp1pR4thUCiMS0I6Noyu6Pp9pTqmsfF13jo0P5x1fqRRgwGTPAVTRBOLzPG1zGRSTYYUoYVwgq_oQ4oA54G-HF9ZX_PeYz4uI_rPsV3v0llMDJF3nQUu67KSJO8hggYNzuVMFCaahKkUiDbcqvAtThc2nM7f0cqFPmQo8YsO_2pJbCjXuZgrdsdy1TskC4B3mZ8D8Wq2pKTkmFKmkFK2SNU48NKzoTZVTJIRGBVie9RHaW_30qpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
عراقچی و ویتکاف در حاشیه نشست امروز سازمان‌ملل با هم دیدار کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107090" target="_blank">📅 23:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107089">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec872952d.mp4?token=bL-W7lkCpgHUOvYzfADqM3TR5JimlhwC-zH7m5XuovqSfGI5JBtNtc8rT8kJ24RmrAt4y3BLchRTbj40ja9ydqgzk5mFNe5pEQwQocEgpZ_ts2KzsSXlZyEr8x-4fz65KwP7CVUmYhazYQ_00rVBOJnVZEL3bavuPfPc3XuaIBEJUckX_FgBcw2m9JpVjQJYppq5D8trDzs7fsg0h1u0h5t4QA5hkvBGqFURBp7mScwGWYkAElVEHihAMe291J4wogomtIxA73ldPO8PRna9Ia1HjY27607aLFomJXBJU0Hy-Lj7fLtXS5PLLhfpgL414Bhv7aArsCt1AgaRqLdhP29YibrqYGmJev5WK4g_IkVvlLoMHjF2IJNQd79gIQBl7M5JY11cWFij_b4Tkm6prThyploWd2rOj5sT4AdzSXwKwZcNckaJtt019wWEh-_dxgMD_NzENJWcxTotk8OD1r86V1VRbXVM30YXt0IZZJqS9Cdn2uBJ814XIGvT5srrSsTzfwnpqF_Obr4FF5gWsgzjpJMeav9Z89q13OLFsbwxmMOT6A5XhZa_cyXRm2OQxADtA14aeAsZ3RnfWbI7pxGjARZ6G2mai2jsC2GsgVrInhxXHipHKJvbg24oG2mbOwVt9ttjw8XEdBxQS5f1ZtVhlCT2no2T3cCdeYfgCnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec872952d.mp4?token=bL-W7lkCpgHUOvYzfADqM3TR5JimlhwC-zH7m5XuovqSfGI5JBtNtc8rT8kJ24RmrAt4y3BLchRTbj40ja9ydqgzk5mFNe5pEQwQocEgpZ_ts2KzsSXlZyEr8x-4fz65KwP7CVUmYhazYQ_00rVBOJnVZEL3bavuPfPc3XuaIBEJUckX_FgBcw2m9JpVjQJYppq5D8trDzs7fsg0h1u0h5t4QA5hkvBGqFURBp7mScwGWYkAElVEHihAMe291J4wogomtIxA73ldPO8PRna9Ia1HjY27607aLFomJXBJU0Hy-Lj7fLtXS5PLLhfpgL414Bhv7aArsCt1AgaRqLdhP29YibrqYGmJev5WK4g_IkVvlLoMHjF2IJNQd79gIQBl7M5JY11cWFij_b4Tkm6prThyploWd2rOj5sT4AdzSXwKwZcNckaJtt019wWEh-_dxgMD_NzENJWcxTotk8OD1r86V1VRbXVM30YXt0IZZJqS9Cdn2uBJ814XIGvT5srrSsTzfwnpqF_Obr4FF5gWsgzjpJMeav9Z89q13OLFsbwxmMOT6A5XhZa_cyXRm2OQxADtA14aeAsZ3RnfWbI7pxGjARZ6G2mai2jsC2GsgVrInhxXHipHKJvbg24oG2mbOwVt9ttjw8XEdBxQS5f1ZtVhlCT2no2T3cCdeYfgCnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇫🇷
اولین تمرین خروس‌ها زیر نظر زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107089" target="_blank">📅 22:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107088">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=F8FmfRg7U6E20BO-MYrupZwOVD8QN4LFWy43FXWUB60oB-1V1R2QNsoc3VKdYt4TEU-TvopO-eJv5UWu1-aDyP7uUYsMngDx1v_fxm74gLZIbucx8Fp7gE1QVv8X2lClGi508ev0WJemfFzU-UZ2IAMLx27A8e2EMETelY3yJzAOYhc2b7ubanpk4lSHYJYWNAEACyrN7GpbagH8fYmoVUAAvDzpLB_SJxVLDmNmv85ucZNjE9zekDWe7keXVvIkVkdQcUT856cMKZrjRPoZFwAJPCCbgxYP6nwo4KowYZ9MYCu-r6Ym3zVJniRnCcHkOqaCINCP_J99QTr6gdB59TuDJKnQ_DhFHVvohmIgOcbXKLb3NTCxjR0VD7ZlaB2TP7l5yxb9fxox6FiZB1DM-kMCf2npf4pmAZuABSGcov2KNuad1iGaiUaNRdu28-s6Z1rCqS8mm7nbpmG4ERfmII7Y-dhOOJlXO4PGmVgn5lNg28Jd3pW7A1jW7vxJUTtkYh-SEUPuTfWKqEuZGRYtJvREHL97Hi9hswLh9tO5BaGa7Ad3WGGh2nnDf-L-y-5jx_xzVx1OGinjTDtWLEhSAubzaknmndJ0o49_lHfE2_dNb-GP8cn2giUZh-HAdI9sexzmrGUSIdS_tzkBOq-t56Ja_yxert2jUkjfKG8QSa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=F8FmfRg7U6E20BO-MYrupZwOVD8QN4LFWy43FXWUB60oB-1V1R2QNsoc3VKdYt4TEU-TvopO-eJv5UWu1-aDyP7uUYsMngDx1v_fxm74gLZIbucx8Fp7gE1QVv8X2lClGi508ev0WJemfFzU-UZ2IAMLx27A8e2EMETelY3yJzAOYhc2b7ubanpk4lSHYJYWNAEACyrN7GpbagH8fYmoVUAAvDzpLB_SJxVLDmNmv85ucZNjE9zekDWe7keXVvIkVkdQcUT856cMKZrjRPoZFwAJPCCbgxYP6nwo4KowYZ9MYCu-r6Ym3zVJniRnCcHkOqaCINCP_J99QTr6gdB59TuDJKnQ_DhFHVvohmIgOcbXKLb3NTCxjR0VD7ZlaB2TP7l5yxb9fxox6FiZB1DM-kMCf2npf4pmAZuABSGcov2KNuad1iGaiUaNRdu28-s6Z1rCqS8mm7nbpmG4ERfmII7Y-dhOOJlXO4PGmVgn5lNg28Jd3pW7A1jW7vxJUTtkYh-SEUPuTfWKqEuZGRYtJvREHL97Hi9hswLh9tO5BaGa7Ad3WGGh2nnDf-L-y-5jx_xzVx1OGinjTDtWLEhSAubzaknmndJ0o49_lHfE2_dNb-GP8cn2giUZh-HAdI9sexzmrGUSIdS_tzkBOq-t56Ja_yxert2jUkjfKG8QSa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توضیحات بازگشا سخنگوی پرسپولیس درباره شکایت از آسانی به کمیته استیناف
🔻
فردا به آقای تاج و فدراسیون فوتبال نامه می‌زنیم و سه درخواست داریم. حضور وکلای پرسپولیس، ضبط جلسه و پخش آنلاین جلسه رسیدگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107088" target="_blank">📅 22:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107087">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjtYRguElYP6hx1XE8zl-931xEKvloVXBM4UrmW201UWT9Vr8Rda4gd1l9WND9WB_AyVAk5tAUunYNIuK1yVXrTasf8YdRMimIAQ6ZyNCfz9XEq_m7dhKOJgv6g97GRwd73RhVK-CQuvNLVeB_1BQGNI8O7r_AUZF6071Ne3PrrG4f1BSTCfsg4-RWXwq26oEtjz5QXyJ654Qm6eidM1mKqrmNxVBOHiCDDRw5UhKbewPvZ-O_B5T4p6egf62VucAJvXowPoTX-QvkAqAcJFiEisBXOvDhMD81tVt0K3iyPK-S3PouP9XlLtOK8aRg8E2hbk_bjBvtyn4FeWTno0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
جمهوری آذربایجان رسماً پروازها به ایران را تا اطلاع ثانوی متوقف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107087" target="_blank">📅 21:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107086">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91400e175a.mp4?token=jn3jKIcGbtw0d74Dq5WrdAbiU6147SyxVz_9Ft745od3kasv-TKCnr730EjF2yIaJ4oBbFbcj7rwIeA64PDvqPEvhOsb3AlLiuhAJm6jaiCKDsBadlNcurHGP2YwIYfrh1W2WH5STeJT-O0ikuG3pu7gZS-QZLSiGEtHVQPRog0FFg-hDfyLLFpocWVNK-BQfvjdWOvSzrtY6poYJOReC-09s31_RcXm18hzYzLMZh5clLkoiMM5PF1lv2ALH1uFC4VX95Ut5ZmdcZuJDj9xgGcAQ-FrEwVGl4BwCHfdq4tMvH-SYRjiXhLKI3enAHTAxyy9ZR7qkgcXMBiUnJndbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91400e175a.mp4?token=jn3jKIcGbtw0d74Dq5WrdAbiU6147SyxVz_9Ft745od3kasv-TKCnr730EjF2yIaJ4oBbFbcj7rwIeA64PDvqPEvhOsb3AlLiuhAJm6jaiCKDsBadlNcurHGP2YwIYfrh1W2WH5STeJT-O0ikuG3pu7gZS-QZLSiGEtHVQPRog0FFg-hDfyLLFpocWVNK-BQfvjdWOvSzrtY6poYJOReC-09s31_RcXm18hzYzLMZh5clLkoiMM5PF1lv2ALH1uFC4VX95Ut5ZmdcZuJDj9xgGcAQ-FrEwVGl4BwCHfdq4tMvH-SYRjiXhLKI3enAHTAxyy9ZR7qkgcXMBiUnJndbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد چلغوز گودرزی رو داشته باشید که دوباره تصمیم گرفته بره مقبره کوروش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107086" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107085">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
تمرین تیم‌ملی فرانسه
✔️
کلاس آموزشی تیپ زدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107085" target="_blank">📅 21:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107084">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🙂
💥
مسکات حلال‌خور اتلتیکو مینیرو برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107084" target="_blank">📅 20:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107083">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=uB2sw6KV1VXIsh9jtFFh1HlPS0bGLOXqtMnUL6yHkuz6U0b9JN8_vxFQgHnMyyrJKJ8hq_L7Go5cnuf_gFTsidraGwdOmyq_VT63u0CyNx-Cwo4_hmlnd9C0TuD-YoaPSjbxn6Rec9BH1gYHiJn-NWAdzPnrPXVeTU4BLj9uffAMVuXq-tDs1-ignD7a5zvDtUPNmUZMM2MRp-fs6GNkMY2SyBKNN7Bjr3BiORbE7x-3G73QA7Ps0Zq-T1w6r5l-C7tsTCJy12F4RhkSXx8xJKXwpekYm-WBsS47AvW8oTwUVmt8x20_X6idecgwpPnIwWIQFLgCi1bgDifCiKougw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=uB2sw6KV1VXIsh9jtFFh1HlPS0bGLOXqtMnUL6yHkuz6U0b9JN8_vxFQgHnMyyrJKJ8hq_L7Go5cnuf_gFTsidraGwdOmyq_VT63u0CyNx-Cwo4_hmlnd9C0TuD-YoaPSjbxn6Rec9BH1gYHiJn-NWAdzPnrPXVeTU4BLj9uffAMVuXq-tDs1-ignD7a5zvDtUPNmUZMM2MRp-fs6GNkMY2SyBKNN7Bjr3BiORbE7x-3G73QA7Ps0Zq-T1w6r5l-C7tsTCJy12F4RhkSXx8xJKXwpekYm-WBsS47AvW8oTwUVmt8x20_X6idecgwpPnIwWIQFLgCi1bgDifCiKougw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
🇮🇷
پیش بینی چند هوش مصنوعی مختلف از قهرمان فصل گذشته لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107083" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107082">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=Z-nrTowok21kF_LDRzgvhYl1UDTNwpcmtVilJUH5R3iohuhCsICc0PaWS-hm8fTsrCjbVaZnKUfHYGgNFRm4LjCK5tNccvzQzYS011D8gJ6ZrX-uS816tE4FWshvwQQDAMn3vahH9YS4SpXuf8UEAtwj9YAHrQaqnDtFBEiTMVYhKpA24DNGNeeGxKsuLRQ_p4w86Z1DvKQGwSSAIfZ1XZnhD27EuVhhaJJ6qtXe-7z5ruj96IB9lp0_s1UtNPHeXXDwHHaS_9keILTyKPM3fDrFPWNUCDA8n-cN7QSocd-mOX8g7VaccPMZAyS3GcZ3hRL436C6PuAx_JL2djfaJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=Z-nrTowok21kF_LDRzgvhYl1UDTNwpcmtVilJUH5R3iohuhCsICc0PaWS-hm8fTsrCjbVaZnKUfHYGgNFRm4LjCK5tNccvzQzYS011D8gJ6ZrX-uS816tE4FWshvwQQDAMn3vahH9YS4SpXuf8UEAtwj9YAHrQaqnDtFBEiTMVYhKpA24DNGNeeGxKsuLRQ_p4w86Z1DvKQGwSSAIfZ1XZnhD27EuVhhaJJ6qtXe-7z5ruj96IB9lp0_s1UtNPHeXXDwHHaS_9keILTyKPM3fDrFPWNUCDA8n-cN7QSocd-mOX8g7VaccPMZAyS3GcZ3hRL436C6PuAx_JL2djfaJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107082" target="_blank">📅 18:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107081">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=KCJi-xYmtdaepEU4B0EQwyWuyvCCrcOqdghaOZhBYdYmLySSPm9vu24D6PLU8hQN4YQH9iXDGVHJTY9jNzBk0cwf4a9Wp2h3F1jpP6g7H-IBpyHRXxaqfF87hYPUHJlYNALH3FrtV4slKv6J0bPGpEKQZtbOrkyWYp0gXqS13lEULS0xsrgnyrdXAzLmzwWLM1sLdUpybSZXVBMetNnNvbDFnvxxaubEQS0y8iYXUZXYAfwAgI-cezmFASCtpEmj7FGW90KhpFuy2W7XpZQ04EGxThqrIiCYz65iGXtvK16xYnnWlOg5FY6Di0086qN43q0GBoefA_WmdW2rUDtnNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=KCJi-xYmtdaepEU4B0EQwyWuyvCCrcOqdghaOZhBYdYmLySSPm9vu24D6PLU8hQN4YQH9iXDGVHJTY9jNzBk0cwf4a9Wp2h3F1jpP6g7H-IBpyHRXxaqfF87hYPUHJlYNALH3FrtV4slKv6J0bPGpEKQZtbOrkyWYp0gXqS13lEULS0xsrgnyrdXAzLmzwWLM1sLdUpybSZXVBMetNnNvbDFnvxxaubEQS0y8iYXUZXYAfwAgI-cezmFASCtpEmj7FGW90KhpFuy2W7XpZQ04EGxThqrIiCYz65iGXtvK16xYnnWlOg5FY6Di0086qN43q0GBoefA_WmdW2rUDtnNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ: انتخابات هیچ تأثیری بر تصمیم من درباره ایران ندارد و تنها تمرکز من بر عدم دستیابی این کشور به سلاح هسته‌ای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107081" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107080">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
⭕️
⭕️
ترامپ: باید تصمیم بزرگی بگیرم درباره اینکه آیا می‌خواهم ایران را نابود کنم یا اجازه دهم به حیات و شکوفایی خود ادامه دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107080" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107079">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=XOZilsge10sD1sMUG9Zq-VFvqpMQLIAumNZNBe8yd-fKpumECgxPAMKDqpAeh15O3KM32ylTOKNNQz9sZTYDw39ncr5lODaKdH8lemUz7IDgznXiPHVBDd9cPEQdff46qDvudXOnr5W0OVkEvIcqOfrPxWFZhfmUC8bNe8m98TAOeqPzpgPkY3nMv0GKgbGlvLDqeFWftRdCqRGQOu7jtbWvzFIrtLxs27CkFhzyT6qdrDp67hPjsMCK8XZ6AyRvVGLFMJaTb-8akkEe0rae6rGigcplefemm-3TGMCpDgdm1Oun_GHHQhAeBiAkTmo8qaq0_oyouef1RhmRiEAKJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=XOZilsge10sD1sMUG9Zq-VFvqpMQLIAumNZNBe8yd-fKpumECgxPAMKDqpAeh15O3KM32ylTOKNNQz9sZTYDw39ncr5lODaKdH8lemUz7IDgznXiPHVBDd9cPEQdff46qDvudXOnr5W0OVkEvIcqOfrPxWFZhfmUC8bNe8m98TAOeqPzpgPkY3nMv0GKgbGlvLDqeFWftRdCqRGQOu7jtbWvzFIrtLxs27CkFhzyT6qdrDp67hPjsMCK8XZ6AyRvVGLFMJaTb-8akkEe0rae6rGigcplefemm-3TGMCpDgdm1Oun_GHHQhAeBiAkTmo8qaq0_oyouef1RhmRiEAKJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: ایران موشکی با قابلیت هدف قرار دادن اروپا ساخته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107079" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107078">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=SPI98lXMoKJPLOet2kBbDOh4MvnrvWb6A3dz2LVqH-yqN3VIvFAtvFSzuy_Wut3K7dyA9UJceA8Sgjgy0bevAvV0ajBxrkVQv6Gb8TZTilK7wUMoOOJeDYLvyUlRblBlOhRANAuLjoAGKADV0QveJt99uQV8zwJCzowwp3UZMbxfctddZYvNGsKxdUcbML0nBCjcODOFQQ8B90_OLCzmx-mtX_NNZ227EhH2qIvJkA2hP_e-oMNl_Yo9i-8EjUzT7SjN_3m51PQWOJ-41zDiEKyvG54RwairSLkX12t-T1uG49bAucJe0CCEFUAfHYiCyDy62dpG8g-M56sOhvGZnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=SPI98lXMoKJPLOet2kBbDOh4MvnrvWb6A3dz2LVqH-yqN3VIvFAtvFSzuy_Wut3K7dyA9UJceA8Sgjgy0bevAvV0ajBxrkVQv6Gb8TZTilK7wUMoOOJeDYLvyUlRblBlOhRANAuLjoAGKADV0QveJt99uQV8zwJCzowwp3UZMbxfctddZYvNGsKxdUcbML0nBCjcODOFQQ8B90_OLCzmx-mtX_NNZ227EhH2qIvJkA2hP_e-oMNl_Yo9i-8EjUzT7SjN_3m51PQWOJ-41zDiEKyvG54RwairSLkX12t-T1uG49bAucJe0CCEFUAfHYiCyDy62dpG8g-M56sOhvGZnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ در سازمان ملل: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107078" target="_blank">📅 18:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107077">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=WRaJeLCh8LrFpFmjrhskegpabtvWMsKWcyWu7CdadhnFEsS76DazWMOp08ObwSoCXaDHfe_9cR6zKm0OaMxcLWWU_JbDGWgInQAfnRI5dj4Bd95GGUFvXYH6iQHQHZ2DZIvR-cNCyfAz63nn32MIrHhRWbiqhu72r-iRdj0Oh6wvQoy2mm_bBnm2qPdXmC9yg5M71cttrPY3nswbz9lZ3ew3LySg-f0m46NBpVyuBm7NPbg8QfYrhDqecq73wCB-5jfhXDJPfpjJdPJ512_H53SEI66D9luquyYfMAX9vwnRa-k8MDcVKvKpho3y0WVJ2u8AhXj8HuicBpd6fd4Ksw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=WRaJeLCh8LrFpFmjrhskegpabtvWMsKWcyWu7CdadhnFEsS76DazWMOp08ObwSoCXaDHfe_9cR6zKm0OaMxcLWWU_JbDGWgInQAfnRI5dj4Bd95GGUFvXYH6iQHQHZ2DZIvR-cNCyfAz63nn32MIrHhRWbiqhu72r-iRdj0Oh6wvQoy2mm_bBnm2qPdXmC9yg5M71cttrPY3nswbz9lZ3ew3LySg-f0m46NBpVyuBm7NPbg8QfYrhDqecq73wCB-5jfhXDJPfpjJdPJ512_H53SEI66D9luquyYfMAX9vwnRa-k8MDcVKvKpho3y0WVJ2u8AhXj8HuicBpd6fd4Ksw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
تعریف عجیب علیرضا علیزاده از نوید عاشوری که موجب پاره شدن دوباره عادل شد: گفتم ازدواج نکرده بودی، با هم زندگی می‌کردیم!
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107077" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107076">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=V-7Q_j20UOpBcPNj-UWLafvptuGzaFHd3CzVwoYDci4bV4EjCnKTP55HauBmqeOK2dx9tjXE5xHriLO8jpXMsMoqFuKZjREk0_wx-gf-mCdq0VYH5a9Jj0lK0Hj_LjwLHqvLbDnRWKIazonMc2t0HoCrLpiu6zPfUgv7Gpm498h_miv5DrLNjOV0iF821xecBbH9HP6qN_t26LsxkrYwDFysjAgjv4qEx8R7nGv_HI7kYHXIbXsGt0r9NqpbKDLPk6LyTB4eFdvZxCc492YGOxEeIn9DYalAR-mLAjHTrfsTCorF6IDGFAy7ZmNVCCaWZwriGt0WFrgLayoW0OIM5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=V-7Q_j20UOpBcPNj-UWLafvptuGzaFHd3CzVwoYDci4bV4EjCnKTP55HauBmqeOK2dx9tjXE5xHriLO8jpXMsMoqFuKZjREk0_wx-gf-mCdq0VYH5a9Jj0lK0Hj_LjwLHqvLbDnRWKIazonMc2t0HoCrLpiu6zPfUgv7Gpm498h_miv5DrLNjOV0iF821xecBbH9HP6qN_t26LsxkrYwDFysjAgjv4qEx8R7nGv_HI7kYHXIbXsGt0r9NqpbKDLPk6LyTB4eFdvZxCc492YGOxEeIn9DYalAR-mLAjHTrfsTCorF6IDGFAy7ZmNVCCaWZwriGt0WFrgLayoW0OIM5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعضی‌وقتا آدم فکر میکنه لیونل‌مسی تو زمین فوتبال بیشتر از دوتا چشم داره
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107076" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107075">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107075" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107075" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107074">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcK376-DLcmcNfaqigUwuGqNfJILwoLUfDDfHdyIm3TU-A8UMhbRUdcCH0wqnLe72grAJJVKUTGH--EbKWwR8IMHe0Y-C18klU0BnUlMSJl3GFYsgfohtZ2HD7_V38h6LKNVYdAcwtIBrT1n7yRZDXupB3-qOyDgrXVjFio1ZOPs87v9TEp0mw94UN-fnDyiQJs9t4WpeCQDCy_0771RKOkVrEJSWRwhGQbXxgKq0gk_YyQbcX-ckLLmiUWwVE_bLYYafLrd2A8iY_VpPuTxb8F6kwQ9KmSoBLXpE_P_2f29nKHfYHV7c61JtSbqMOMaQnsTRSyritraU8bIl9NSDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107074" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107073">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtYHT2TnMv7_8WF3Pmv6KNFSd7b8Jw3lonVEo3Xai6q2s3XMKt7Ue2ZcFI_41U_NgCyJzQXhwXQNu6y5TnFjzZk6or9QYaADeQcwdbO5zlJumv79xBSrkP4Dor0FW4SN_Qj_70pc-TO2xp-m9lnkP-qDiOFeCVsmMWQgeaEerBQLi2TBjtnnqclZWC_9C54CgYv5oUNNEBH_Cb5hIeJC3T1r26AAwaTWsKJbjZhrHAkPpZideTQlu0B8oh_EjjdH_c7CC7VPWQiMVhzgJYAbkHU78UAVmBKqRHnZa8lJs5_doTmrmRKU-p7-2GpuznuD2aSIkHLtggO1XDNeFwwb3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
لامین یامال :
🔻
به نظرم همون‌طور که می‌گن، توپ طلا جایزه بهترین بازیکن ساله؛ برای بازیکنی که متفاوته، از تماشای بازی کردنش لذت می‌بری و حتی فقط برای دیدن اون بازیکن حاضر می‌شی بری استادیوم. فکر می‌کنم توپ طلا برای همون بازیکن متفاوته؛ ربطی به تعداد گل‌هایی که می‌زنه یا چیزای دیگه نداره.
🔻
وقتی به توپ طلا فکر می‌کنم، یاد مسی، رونالدینیو و بازیکنایی از این دست می‌افتم. اونا متفاوتن و وقتی بازیشون رو می‌بینی، باعث می‌شن لبخند بزنی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107073" target="_blank">📅 17:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107072">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olbHoLeigikYX9IPmypawqZw2ae_tm6RMqEiXOkNHzdIZtSHbXPnKCH2GbJ0DluMinX05Lm4j3A-A1tXgFo1SOCK2ozbuj53vVvtf78NB36G78XhNEwS5RiNmzTIrx3PgEug6FFvXStYKcX5_5COILkrl6mLJSLlT0F9KLH4-VC5BQAn2w9I2NTUlMMQX7aXze4fQAKUF8oarLiJgi7XFdUnACoIEO9m2pRKeQYTj2m50JV5_j39HtM-vr5eSE2SFSpN945PI8-ZwsNmLrBdeDwJvlNEXvIbyrO97OX5Dc_EbrhZ_yH8aTf8PWI8Rk8mRenQ5uNFhMe3Vv2cpy57ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد جدید آرسنال با آرتتا بزودی امضا میشه و این سرمربی به مدت طولانی قراردادش رو تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107072" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107071">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=Ofp850tu9Oa8RpqrulLJ--F92bEetw4HBHHSOdK9HBmKxrQIasJ4Rx1y4flj8ACv45TZBoF9BjuJCQIW93SvVLfwTeUYrBwd3vKdqzTWWROvBit7GtyK6qa_Mxu5qr8C25qQcqXUOrzAMgmXtF2IRV6qOvlfjB8tUc7M4z4ossuG_-UhrpmurYVsI97TusZfeyDiKtYjafAkYR350ovlxwmCxN86pnxXTatJ-sMHz2UH2rZLpNRIkNRQDhFSfB_feZY458iB0yu5YaVZdXlmq_-zh5hXE1TXFojHl5EmkFywEoGkN9fn1owx0tmrCW-vxePFmd3RyNWOLX08hVCsSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=Ofp850tu9Oa8RpqrulLJ--F92bEetw4HBHHSOdK9HBmKxrQIasJ4Rx1y4flj8ACv45TZBoF9BjuJCQIW93SvVLfwTeUYrBwd3vKdqzTWWROvBit7GtyK6qa_Mxu5qr8C25qQcqXUOrzAMgmXtF2IRV6qOvlfjB8tUc7M4z4ossuG_-UhrpmurYVsI97TusZfeyDiKtYjafAkYR350ovlxwmCxN86pnxXTatJ-sMHz2UH2rZLpNRIkNRQDhFSfB_feZY458iB0yu5YaVZdXlmq_-zh5hXE1TXFojHl5EmkFywEoGkN9fn1owx0tmrCW-vxePFmd3RyNWOLX08hVCsSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارلتو، نشون بده یه مادریدیستای واقعی هستی.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107071" target="_blank">📅 16:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107070">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u98eUeDU1ECxAsUYp6O3gLIG3IEnR_AkIwkCnfNCPzm9aLHmAkNNvQVk1pVxzrhGAuUNwqJOYmZ0U2TsDMMu1Z3bzuVTzxnlA0lzFWxT1QAIhrcW4q1M4LJ-OabgN3ukBnjCkiPASjQ24uw-qQS_fh9fiHeHv6LPn8PZubiGXkLjDsEDrDI0Nqni-JEj48l6jaPoCdsU9QWYy66b7ffIpWAtNWrFoAiDxAJorgz_lF18WUdJ-tEM3WSAXLIQ1LNR_B0qM2J-YGy5NmsQcMyDXh2iLs8DuiecnQbiK36s07qSVYaXCgWpjuTpB1JS3MLcFjgZyjODb2IQmhRGYbKdjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
سهراب بختیاری‌زاده برای نیم‌فصل خواهان جذب یک‌مهاجم خارجی، یک وینگر چپ خارجی و تلاش برای جذب محمد جواد حسین‌نژاد شده است. از سویی بازگشت خلیفه و گودرزی نیز جزو برنامه‌های بختیاری‌زاده در اعلام به تاجرنیا بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107070" target="_blank">📅 16:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107068">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS3DamVqa_id3EYW9Krav54-0Bn_JAzirfz98rtKtkukOPBsTq1a-DAdvD8yMJ1r01wnxvxFQ2BENWnkft-cilsRmBx_Ptyi-n4FdKrrPHtzMLplZedj3EZ7Lr9nfULdeBpR2Xd3R7lWSB1RGoQ2vhh6DB-YRIgBN1sRVx_z55iKkZ4D082JgiEj53sD_m-qh35uuL0mUvBh2RVEQZHfqwbXy2Jmbv8p6Fp_ZJ8UDEC6IZasqEgglQBOivx74uof5nyGLrYgMgVtrBp2Gwyy7h_Rv5xc8dB-vorm_BBN0xi685ubrag3c_VvXcCa0upIFE6GnaQ1Wl2_4dfl3Vdqzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
اوج تلاش خداداد عزیزی برای درخواست بخشش از مردم بابت وویس زشتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107068" target="_blank">📅 16:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107067">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vfta0HIDg99SAVloZm1Cpf5kD6rsY2duS4-vkt3GSQZGTcIBgpYsg4YJ8i8giskJLS2f5h6BJCyNkGrlLkP3IQVDJZVscilIZQYS6nAVXcZJUDYO8NCa5WF1xOQ0WBe8pjtbkeX9rQq0iDL1L7X53ZXdPqRoNPASfVL0mQZR69UzXWxDiCO7BJrgW4nZg1t5qZQMlvoA8B4To5SOEEZNqG9TPoqv_3dkoaE3GNaNYN_ojVHjUhlnyKDQJ1PrOaq7K5F3r_04f98VJF06dEVu-HI104fWwtAOZ2N20KxjIsr1jITPRhX8UqIZAcDmzhzR5QcqbHqAIfGDOewwJywuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عملکرد فوق‌العاده موناکو زیر دست فلیپه‌لوئیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107067" target="_blank">📅 16:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107066">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVbvAkP2p-vh9j6NEx_VN18KvaDqhatWUNk3tspbquqMxGe19vv2Pb4d-IQsKV8b1THhiyEgAIFqeOC52kgHADNUJJXNmkE1QakE2OFH9CArOF6OvlgIbT4TdL900mJxJ_kJKXER_SG803rJ4BKU1zIT8_rSY7i3oQVahK_DLpc3hfYDHE8HGMi_Nqze7_E0iNleERRGTEgre36r5i1KvBDTn4EM5Hhu-zckBVncKCjGAPpxXWw83puCYM1BLhVO1za8p6SMtdxJzgZMoYuwoNZ18Xs2j6PQ67cBg8hZlumuQbNJeHC_vPjqHXuiwVNvKveg1tQGVgY7XrsDHglahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار
تیم با ۱۰۰ درصد برد اروپا تا پیش‌از فیفادی جاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107066" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107065">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoPbqHpx8WTS6NfLSK8-eUR38SC6XJZ71Z5dn6S7wkwB_om6mCe3OxtGALOCZgehpWMPAOW4G9n9j73-nb9R8s45tHJ2_v77jbhv51I1tVT90K18sj4CtlBSu88QXyB6qiNP7MjAgGvGkV7sdXwX8T7cysf6DJXgFcAMqyFO4gRQT__VJYvY6srG9t0OYKfJTiGcVckMdXQ58oHHlepc7Y6ltqsgCJ2S5l9lqFXc9mHJ6lPVQRZk35Z5_216wOYyi3XBtWBgqFEJzUQe6bHEvx0utyXnwTqvDXUrmfwuZ-C5PC4R6U05ubQTU5W5MD45FF67-Suh18gSemScnE-VYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
عربستان و چند کشور خاورمیانه در آستانه جام ملتهای آسیا با فشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107065" target="_blank">📅 15:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107064">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=Qd2XGSYsk52eHUVWHZFM2mXePoLBHdNJ-t201GnajhrvCWjqj0GPlSgE3dPBwd65NrJ7-xl8o1RcaloFVo63cwwLOvKqPckX1kTThcm6fpjKtaAnmpiTHag60ii-Q606KUgnhw5X4KQ0zdbLOctQBKyKXRUVCydA74Qsx6hda0BfvTRzjqbT6kmZK8vpLteyhtqr8o4YdNDgk6Tn7_Ylx70bZE5-sPewKBJzqaSS9gUtHunL-4W6_lrtA5fozu2wmOu0h8IWWuSZMmv-g0LIBkMbXLiEctWSXojD132WP73Gy-_Hi-NpI7ylvoavlh6uOEKS_H73vifyesOyXukvLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=Qd2XGSYsk52eHUVWHZFM2mXePoLBHdNJ-t201GnajhrvCWjqj0GPlSgE3dPBwd65NrJ7-xl8o1RcaloFVo63cwwLOvKqPckX1kTThcm6fpjKtaAnmpiTHag60ii-Q606KUgnhw5X4KQ0zdbLOctQBKyKXRUVCydA74Qsx6hda0BfvTRzjqbT6kmZK8vpLteyhtqr8o4YdNDgk6Tn7_Ylx70bZE5-sPewKBJzqaSS9gUtHunL-4W6_lrtA5fozu2wmOu0h8IWWuSZMmv-g0LIBkMbXLiEctWSXojD132WP73Gy-_Hi-NpI7ylvoavlh6uOEKS_H73vifyesOyXukvLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
مرور هفته‌عجیب فوتبال در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107064" target="_blank">📅 14:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107063">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=sNxCNXcM85R01aQEmQ_gBNLwwlwnpR92cgHtJHKogY5oHu2SLAl_ew1Fq7M38h7BhMZqDPEzj7cRNqOB3FNtPHTd-CS9kuLDt1BUHSu4Dr9LVVm7-Cp-rQ62nTA18BieIgN0cggVU-tT4z1IUxJWq5lLFC0_p7eDl2ZSQnjWvhplUTA7IS2F-a13I_BhYwgi_3MKxrPkEVfMJfkdla8FxwrQLlYCxBmH1hHE_arCtHdiusvxB9WY3Jxw3HCY0Y3dKFnmACCaJiVRsWQgTNhyadwYBAu7h4KW-yHewOP9SuIk9ULFE3MABNN4QGQa2jQj48y6tMdnohT2DYJrZZhI1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=sNxCNXcM85R01aQEmQ_gBNLwwlwnpR92cgHtJHKogY5oHu2SLAl_ew1Fq7M38h7BhMZqDPEzj7cRNqOB3FNtPHTd-CS9kuLDt1BUHSu4Dr9LVVm7-Cp-rQ62nTA18BieIgN0cggVU-tT4z1IUxJWq5lLFC0_p7eDl2ZSQnjWvhplUTA7IS2F-a13I_BhYwgi_3MKxrPkEVfMJfkdla8FxwrQLlYCxBmH1hHE_arCtHdiusvxB9WY3Jxw3HCY0Y3dKFnmACCaJiVRsWQgTNhyadwYBAu7h4KW-yHewOP9SuIk9ULFE3MABNN4QGQa2jQj48y6tMdnohT2DYJrZZhI1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
🇪🇸
پست‌سمی تیم رئال‌بتیس از جدول لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107063" target="_blank">📅 14:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107062">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068efa824d.mp4?token=dIvgFWjSgCnffR3bEEmnU4u_93Qqj9bcMsS6P4TnQYwNIsK6fx1le9kmCisfMuX9NGZ8RA7z5-Sex7RCdE7DE3Cb6JQwCtbN8m5JeXgqlrr-HE6fstpVALSiShvF5c-V__LJiQZ_PqPQWTa_1ojgn6BVcTJdJwas2OClYBfIdZwzKo4yXB14fVrpYFIZRv628AyHZjoSsYTdqHBuIQ4kOtF6e5H8JAsWvuajdEgEinbH5SPEfzX01kGZBQ_It7tPe_ND-eFfzVLd_5rjNjgUGVr1vTqgAhOpJwIT-79mdJw6gCCuhZF61nc3tEDYPPSB5kG-txUpKDFCi-bpuktyCIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068efa824d.mp4?token=dIvgFWjSgCnffR3bEEmnU4u_93Qqj9bcMsS6P4TnQYwNIsK6fx1le9kmCisfMuX9NGZ8RA7z5-Sex7RCdE7DE3Cb6JQwCtbN8m5JeXgqlrr-HE6fstpVALSiShvF5c-V__LJiQZ_PqPQWTa_1ojgn6BVcTJdJwas2OClYBfIdZwzKo4yXB14fVrpYFIZRv628AyHZjoSsYTdqHBuIQ4kOtF6e5H8JAsWvuajdEgEinbH5SPEfzX01kGZBQ_It7tPe_ND-eFfzVLd_5rjNjgUGVr1vTqgAhOpJwIT-79mdJw6gCCuhZF61nc3tEDYPPSB5kG-txUpKDFCi-bpuktyCIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇮🇷
🇮🇷
شوخی ابوطالب‌حسینی با عدم قهرمانی پرسپولیس در آسیا و ناکامی‌های استقلال در دربی به سبک هوادار مشهور منچستریونایتد
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107062" target="_blank">📅 14:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107061">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=OONgjnr_B6S8p9Tv1aUbNz7HP515V0b_B_6pWoNoV7GyFDDjYMPu8C7mYDWBQSG4C5tQmJUaE2VAiXZ3QL_TgfWuaFmEuG_gktGqJ-JoI_Qwc1QL874GCD2yKKB8FbGmurdzuOf2hS2cNbSUqxupUIUDbCXdqZGMfRDrM0I6OPHwpWrYyj8uVifjohXHVERlbj2hg63BnNuKwiWZ79yBhnFC0nAyJz6wz3Igm6uvzinagfd-2WiYYGz0vtlt9B_fIVAT00NvJWUNBdH9NmJbGVfop9FKhHpZZEMsnfUHhWcQexNAGVaOZnhhfPAFBMl9hsjmSbP7LMHFiyzPUlcTaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=OONgjnr_B6S8p9Tv1aUbNz7HP515V0b_B_6pWoNoV7GyFDDjYMPu8C7mYDWBQSG4C5tQmJUaE2VAiXZ3QL_TgfWuaFmEuG_gktGqJ-JoI_Qwc1QL874GCD2yKKB8FbGmurdzuOf2hS2cNbSUqxupUIUDbCXdqZGMfRDrM0I6OPHwpWrYyj8uVifjohXHVERlbj2hg63BnNuKwiWZ79yBhnFC0nAyJz6wz3Igm6uvzinagfd-2WiYYGz0vtlt9B_fIVAT00NvJWUNBdH9NmJbGVfop9FKhHpZZEMsnfUHhWcQexNAGVaOZnhhfPAFBMl9hsjmSbP7LMHFiyzPUlcTaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
🇸🇳
سادیو مانه با حضور در زادگاهش در کشور سنگال، مبلغ ۲۰ میلیون دلار را برای احداث یک پروژه با اشتغال‌زایی بیش از هزار نفر، سرمایه‌گذاری خواهد کرد. مانه اعلام کرده که بیشتر دستمزدش در دوران فوتبال را صرف رشد منطقه محروم خودش در سنگال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107061" target="_blank">📅 13:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107060">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=BO4BjZinuNR-XSteoS6AB4UTmaOWM9oNavKg3kRqKJUox6dXoXL_kGnWHmStM37u4IoiHJHxartv5xr1lEdE_cTjwoRvHJf9-ooBLr-GHnOrLx2z5NwnryxOTrHNrdg0Z3Q_5dqhYsmKX3NlL4l9J0EB-Jfobzcmq6d01SIEMgb4YIUnS5cjouxHJL32up-ZgBam7YmBY7vYansjWDj3wk72ocvL0SwHXjAXSRDQwfGBSdt-rqSJEjRXIs3O_F1AuAeh83NbjHyjrSZEvqPakhEhhEJqVe6OuyeL2KRgHiq2A9u9dnqu3nWhqJpZ_1UGV-jzRBEduTdLkUvBebKSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=BO4BjZinuNR-XSteoS6AB4UTmaOWM9oNavKg3kRqKJUox6dXoXL_kGnWHmStM37u4IoiHJHxartv5xr1lEdE_cTjwoRvHJf9-ooBLr-GHnOrLx2z5NwnryxOTrHNrdg0Z3Q_5dqhYsmKX3NlL4l9J0EB-Jfobzcmq6d01SIEMgb4YIUnS5cjouxHJL32up-ZgBam7YmBY7vYansjWDj3wk72ocvL0SwHXjAXSRDQwfGBSdt-rqSJEjRXIs3O_F1AuAeh83NbjHyjrSZEvqPakhEhhEJqVe6OuyeL2KRgHiq2A9u9dnqu3nWhqJpZ_1UGV-jzRBEduTdLkUvBebKSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
علت جدایی ابوطالب از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107060" target="_blank">📅 13:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107059">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=lN6ufzDusLipf1XjgZIi4vWXvjp5mVTlRfmJVFzu9bVsLv29jdg9gDv4k5AtXFLwg-4CvY4fM16rH0Befccqc1_Smozw6ulZlpuhCI1Bynh32u1FLGJ9NKD-Q31unpe2Ul4LbooyUqlrYWhUIGrbdaLznu-DSJmfGfQE9dcyYMc5Yu4CTMa6yaRyETLwHp_xucynYNQYjhPoC-q0IEmOUf86GP-48E3EuPObKvZdX7myT0ZaWGDo9IOXaCrJi_GWoE0SQnv-iAjCviJBmTn3eDbfCCCqUryWsONseRhGd_DjWVf31N7TjQ84SNeSQCq_t8X6E642Y8km4uNnp5aMhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=lN6ufzDusLipf1XjgZIi4vWXvjp5mVTlRfmJVFzu9bVsLv29jdg9gDv4k5AtXFLwg-4CvY4fM16rH0Befccqc1_Smozw6ulZlpuhCI1Bynh32u1FLGJ9NKD-Q31unpe2Ul4LbooyUqlrYWhUIGrbdaLznu-DSJmfGfQE9dcyYMc5Yu4CTMa6yaRyETLwHp_xucynYNQYjhPoC-q0IEmOUf86GP-48E3EuPObKvZdX7myT0ZaWGDo9IOXaCrJi_GWoE0SQnv-iAjCviJBmTn3eDbfCCCqUryWsONseRhGd_DjWVf31N7TjQ84SNeSQCq_t8X6E642Y8km4uNnp5aMhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
‼️
دیس سنگین ابوطالب به خداداد عزیزی: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107059" target="_blank">📅 13:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107058">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=g015JLgP_MNvjdsVtpShA0iKtv4mFW9DsnJoS6hN9HD1CNNCNbpuGMG34QSJs1ntpNnOkQSBNbbfPek-_Pt5s9dkO4m154JOfCtlzTZb6YQ1H7ebL7miMu-z3EHiwrNAwZWS3Qx7wbmBm3bRj_-vPM8dV8C7fZVx2MsHolv6y3g5zfqZGFzPVdIkO2BAowpYkZe_2JQlg6tt45CMdH6ssaqK1Jc89cE6tgjZZ_vNrb13fNN8lfCl5IGqaE8XLadXJLtqQ619O13_hWb8oFVv4-1OjukyJAaSgDlwwpyuACL77uhcOhXFNYmGEZjKOeHLmpeXGzoD04Ic4C0nw1OWlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=g015JLgP_MNvjdsVtpShA0iKtv4mFW9DsnJoS6hN9HD1CNNCNbpuGMG34QSJs1ntpNnOkQSBNbbfPek-_Pt5s9dkO4m154JOfCtlzTZb6YQ1H7ebL7miMu-z3EHiwrNAwZWS3Qx7wbmBm3bRj_-vPM8dV8C7fZVx2MsHolv6y3g5zfqZGFzPVdIkO2BAowpYkZe_2JQlg6tt45CMdH6ssaqK1Jc89cE6tgjZZ_vNrb13fNN8lfCl5IGqaE8XLadXJLtqQ619O13_hWb8oFVv4-1OjukyJAaSgDlwwpyuACL77uhcOhXFNYmGEZjKOeHLmpeXGzoD04Ic4C0nw1OWlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
ابوطالب حسینی ویس لو رفته خداداد عزیزی رو مودبانه ترجمه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107058" target="_blank">📅 12:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107057">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS97ya3zJoT27u_-NJvyERH5XL0BLfz4CdWy45OR6Aia1scrxjJGf4W-RTxyXbwBOYdQiu9gAdxpZVNiTl83BkjAgjW3pV2yBnetJPCAMau26XXXIzz3stZnE_SdeX1pT8VhN1MlkWkNSWsMusX3VYGH6qWqkkYD1rnOP55dBb-OiyFVbrGvhcrlT4u8j1h6BvH_7m7uV3R1YEW8UFZ-g94gBVXKR9tGCSZFO27hNO4yHAIfUubGCq8VC35W0KyvlotNfjHke_zw8uLPkrElbQ4vYoQYtfpX43GTofM0VvQ1Ix2c1-ili3HRGGch6BflFkaftM7DMTHqzKz8XRYZsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107057" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107056">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT85ItYJsTUj6rfmq6URr-ZwQXrU4XjyqPCuQIaDVVh7ET3gyuMHtVSqUcbM3VHh2CAM4pNTKt9nUAlL3k7pb8XNCGiehxDa7LRw6xKxGApo7J7iL64kcEStIo0XmKcjehVG5CQaA07j9StcjAwy8mhH-CDiQzLJwQ5PkYptXN5ghikZHD7y1jns_7YHgWGBNk8XD32F5hJpJlErerz_3V9NcU0tCqsEzyWJCY-CK9LTYAZiA39KbVMt513pXPfSZcO7RUCIbKIJZQxvWoGee9GadkMJWjsFL2mWHRHZe_cn45lAGnZ8OuLbg1BWZAEZdUF_nIHxx8O2zhsOR3cQog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمع سن سه نفر جلو: 110 سال
احتمال فیکس شدن هر سه بازیکن تو جام ملتهای آسیا هم زیاده. جوان‌گرایی بی‌نظیر امیر قلعه نویی بعد از سال چهارم مربیگریش در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107056" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107055">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=Lbz29bQUiGiK2Cgbecxd41RcZhQkLcbJLOaNHjjbLbVa7hf2BUOPyIxbZS4Vk1V85-jkRIuO8HHmZrzZYkoFO_G9yR5wyWuHpk-pBUnSwUgvEHzgxjfSntEUFSEwV2UvgziExu3YzxUNa8t7JDdXZmPm935ZDm8v_6yq8ZzyTaBJUvJhj4bIEEieKe2v66GxZJ6I8uNeWUrCT7KuIm8MC4Qng_XVUPpyBIpPoRn0KmZmF0pl6J827VY9cbNDmHVWM17fSjoqQjGBv_0W_PfvsIoLA5QSa_3my_i4iD-ySlC63b2dyPFh4OH-QAifbudXcalPpuocksUPveHB977dlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=Lbz29bQUiGiK2Cgbecxd41RcZhQkLcbJLOaNHjjbLbVa7hf2BUOPyIxbZS4Vk1V85-jkRIuO8HHmZrzZYkoFO_G9yR5wyWuHpk-pBUnSwUgvEHzgxjfSntEUFSEwV2UvgziExu3YzxUNa8t7JDdXZmPm935ZDm8v_6yq8ZzyTaBJUvJhj4bIEEieKe2v66GxZJ6I8uNeWUrCT7KuIm8MC4Qng_XVUPpyBIpPoRn0KmZmF0pl6J827VY9cbNDmHVWM17fSjoqQjGBv_0W_PfvsIoLA5QSa_3my_i4iD-ySlC63b2dyPFh4OH-QAifbudXcalPpuocksUPveHB977dlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما هم از فیفادی بدتون میاد
🙄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107055" target="_blank">📅 11:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107054">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=i4_2YZp9Zq6QvySvI-JZRyBQhteG4TMNID5KTWHVs6xWnpb4AtOr2gpGXIyNrtqfgBwSIIJIjrOUe9nEZytRJoV0FF2T_JvMrO4tcRDD35SzMJgdG--0siLjlxkRYnxwddw9OVaXn7nyrYB_twyrrExRd00kEU9GIUvB2IEmzc6tEkzPio_31TC7DFjLC3Nv4_EVYeCcj1hWOflxSjWFzlntHZugSSUi2Rfe2fhE9pxxTuTvHko69VfKG063t-Y2TuoTrkc6dzAiFoHIdEljfpTsLIxX-w0sJeAhZPUz1-_odNoNA-Rv3bP2rWcI_vZe1pmTd7ptN-OfBVhQd53TgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=i4_2YZp9Zq6QvySvI-JZRyBQhteG4TMNID5KTWHVs6xWnpb4AtOr2gpGXIyNrtqfgBwSIIJIjrOUe9nEZytRJoV0FF2T_JvMrO4tcRDD35SzMJgdG--0siLjlxkRYnxwddw9OVaXn7nyrYB_twyrrExRd00kEU9GIUvB2IEmzc6tEkzPio_31TC7DFjLC3Nv4_EVYeCcj1hWOflxSjWFzlntHZugSSUi2Rfe2fhE9pxxTuTvHko69VfKG063t-Y2TuoTrkc6dzAiFoHIdEljfpTsLIxX-w0sJeAhZPUz1-_odNoNA-Rv3bP2rWcI_vZe1pmTd7ptN-OfBVhQd53TgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
اولین تمرین لاله‌های نارنجی زیر نظر ژاوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107054" target="_blank">📅 11:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107053">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107053" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107053" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107052">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fubaNs2PPaPf8KnG3-knQd0eJ3d81IUJGrpe2DPh39coQgXwdM5hu7-BAWqFzxKkgTsYHebkhV3RQo5xVsklTtITrlRDoEyOJ8jszMo9u6f7osnGq5gE-MeBdeOiPs3U32Jo_i5zH4UOIVa52CiNNa3T_dDNaEGajFbnmX9gUIaMXBwO2V90t7wLhQOp6HPnJvdFBOHUX4jQKWsykZTpbSwZAtcC1dneBdoLotsdu4IuXQ0dus3yESr5JCjanSu7KWqyl59ap6OOBbpOhSBMGjC_PY3nj71QhAJJFZreMtANCF-157zQkZHlfxzMMiBk2Xej3Zm43MRRiURS2TTilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107052" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107051">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXSCcE0Gl-0HmNzCVGe9LdqvFe4sZruSce2uLLnSrM_94CeJvQaDtj7GqhEma10yuHg-PZ5mRYMKuVwQuwS0QqePaIbYHtc5ZanJL_dcPIM0i5QUkkgMbJULSTPrVxjSrBxRZKj7CFk0FJdFMe0JLzXrEFpp2QVwMAFO_ZGD9DFJrXN3qJL8lOnCd19R3xSVY5nKD9kzuqruSHIAgdG12XzJqP9jk4BOEiocSms9OKCYJQz6oJIKJMWD-emxMXK1hGfoiGoQT-9hf1Q8VQNX_E4OgIF33kXYWwVPUE1zmR_qpldrShk6mg8ElnzAjnMYChJUztUJEKBS4-NG6Q3Jrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل مسی ۲.۶ میلیون یورو برای کمک به ساخت مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
✅
این مرکز تخصصی سرطان کودکان در بیمارستان سنت خوآن دِ دئو بارسلونا قرار دارد و ظرفیت رسیدگی به حدود ۴۰۰ بیمار در سال را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107051" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107050">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=nmQMlBa-3dJWJZVGW8lv7MT3Pr_x-ws584AA1MnI7pHM8-o3KFneJT-DE949g_hzqTlzzlasTFdcPkWLaZV2fKXVDA6WI_a8VuiunJrKr8lBd02ij8JNLb6e7a3dTr_K4-EsxqP7011I_tEMRhEprcFzC8_9zmKNaPYH-AYs7KFE6h5sdnQ-48JTC1g2hDeJev5yMreov8fsbfbImV2iIQxWwKXaqCr9SORIjfi6d7ONA-z1noOErKARAlIQL5Xfyxw7ND07IUbEkP0bp-a_EwZi66jwRA-A1OwfZkcDDlHTBYskBXKdEWmQMRLg0_fhkztpes9FWjWRNxV5teIqVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=nmQMlBa-3dJWJZVGW8lv7MT3Pr_x-ws584AA1MnI7pHM8-o3KFneJT-DE949g_hzqTlzzlasTFdcPkWLaZV2fKXVDA6WI_a8VuiunJrKr8lBd02ij8JNLb6e7a3dTr_K4-EsxqP7011I_tEMRhEprcFzC8_9zmKNaPYH-AYs7KFE6h5sdnQ-48JTC1g2hDeJev5yMreov8fsbfbImV2iIQxWwKXaqCr9SORIjfi6d7ONA-z1noOErKARAlIQL5Xfyxw7ND07IUbEkP0bp-a_EwZi66jwRA-A1OwfZkcDDlHTBYskBXKdEWmQMRLg0_fhkztpes9FWjWRNxV5teIqVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
در این ویدیو پیرترین موجود زنده دنیا را مشاهده ‌می‌کنید، کوسه گرینلند که بیش از 390 ساله که در اعماق اقیانوس زندگی میکنه؛ این کوسه زمانی متولد شد که آیزاک نیوتون، موتسارت و چارلز داروین هنوز متولد نشده بودن؛ البته که گالیله 70 ساله و شکسپیر چندین سال قبل از دنیا رفته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107050" target="_blank">📅 11:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107049">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=nF5MgiZ9WxNcIi5Dc9X1BQrFFPxxbyaGzQPaJMbc3yCPpskbIIOdJxnsP0xWiiBi93RSsxtHbnYGdCPmEhjUHaC2WiE_ATV-r8-YhNm5xJVzdqAQdD5S789CUm5kJDIzBPng6yvcvFTbBLzqS6RSKT0XWdaREVnduOQTldzjF6EujCOpI7yAd5Z5Z0-B-XZSpk_Z9iqWklLX7HNZXIqTPKPBj71YIPX3NqUapjSP6OXtqDVgTYONNsjri4-9mlAsc4cZIzZlP2J-zOe0faQiNQRhwWzfNbr3pVBuOsaZXTWqhpUUECglVBfnTQbHbFslHRj0nKbKagxL3NHTGaXsgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=nF5MgiZ9WxNcIi5Dc9X1BQrFFPxxbyaGzQPaJMbc3yCPpskbIIOdJxnsP0xWiiBi93RSsxtHbnYGdCPmEhjUHaC2WiE_ATV-r8-YhNm5xJVzdqAQdD5S789CUm5kJDIzBPng6yvcvFTbBLzqS6RSKT0XWdaREVnduOQTldzjF6EujCOpI7yAd5Z5Z0-B-XZSpk_Z9iqWklLX7HNZXIqTPKPBj71YIPX3NqUapjSP6OXtqDVgTYONNsjri4-9mlAsc4cZIzZlP2J-zOe0faQiNQRhwWzfNbr3pVBuOsaZXTWqhpUUECglVBfnTQbHbFslHRj0nKbKagxL3NHTGaXsgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاییز با بوی نو کتاب فارسی شروع می‌شه
🍁
✏️
حتی زمان ما، شروع مدرسه ها صفای دیگه ای داشت ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107049" target="_blank">📅 10:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107048">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=TE6u4M3P3crEEkeFvqBYuFQr0W3oy7IwG0J91wJHAAb5SShBaDJLpa2_ndy5R87uJa_MBSx-ss5jyo09l5VNswYEUsANTRhyIJs4G-3VPhNXLjzoYZCEcqRJLOojAD1wyogti9vyz-jKYCUcvj0eo1690PS7DcJ7_JQogVpHPx3QCfH87y8Q-vwfFMSnifo_qjNTNLcNSMBHAunWWHwYU_0HH7UchQdTiVqYk3VMur6kIXv3kXbzoawnTLOtk4c2c7lgTTSYM-fIJSoNN3OQWjcnDFNWbobYmP4S_gtIqrHIyI2cxCax99MVIugLOIfvskMn-BFD-uamREi-i2gDVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=TE6u4M3P3crEEkeFvqBYuFQr0W3oy7IwG0J91wJHAAb5SShBaDJLpa2_ndy5R87uJa_MBSx-ss5jyo09l5VNswYEUsANTRhyIJs4G-3VPhNXLjzoYZCEcqRJLOojAD1wyogti9vyz-jKYCUcvj0eo1690PS7DcJ7_JQogVpHPx3QCfH87y8Q-vwfFMSnifo_qjNTNLcNSMBHAunWWHwYU_0HH7UchQdTiVqYk3VMur6kIXv3kXbzoawnTLOtk4c2c7lgTTSYM-fIJSoNN3OQWjcnDFNWbobYmP4S_gtIqrHIyI2cxCax99MVIugLOIfvskMn-BFD-uamREi-i2gDVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107048" target="_blank">📅 10:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107047">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090ef42156.mp4?token=PkigsQf0MzLHyr23kMh3N9a4iFY8geiWaGYcdPqjSOFntQhxsnVIywqTU9z7SejQyYj21m1elIL8C8XAONnyHahvA5Gg-GjygKr-TOPyrUjnDunfvRFsxTaNnJb2NX14soM_g-OL5SWhlJnROqHmzfb9iA3l4ugHxU7Q-fl0DkgdzxzgOrkIiw7SsqiHUokwoYxV1paRCDgMQvl3xZWuki7XEIqqMKMO6R4ZJecKJrXOtvbRe52BvRS_qu1WZ6E9C7U5MWwOCdC8B8YvrcH8cRmWVD6VcJ67QogAGPwkF-WZKQWAckesYnt5G420Ge2Fq-cwm5FzgKIHu1WlqZJatA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090ef42156.mp4?token=PkigsQf0MzLHyr23kMh3N9a4iFY8geiWaGYcdPqjSOFntQhxsnVIywqTU9z7SejQyYj21m1elIL8C8XAONnyHahvA5Gg-GjygKr-TOPyrUjnDunfvRFsxTaNnJb2NX14soM_g-OL5SWhlJnROqHmzfb9iA3l4ugHxU7Q-fl0DkgdzxzgOrkIiw7SsqiHUokwoYxV1paRCDgMQvl3xZWuki7XEIqqMKMO6R4ZJecKJrXOtvbRe52BvRS_qu1WZ6E9C7U5MWwOCdC8B8YvrcH8cRmWVD6VcJ67QogAGPwkF-WZKQWAckesYnt5G420Ge2Fq-cwm5FzgKIHu1WlqZJatA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی: مربی داشتیم (کمک فرهاد مجیدی) که آدم بسیار فاسدی بود. همه فوتبالی‌ها میدونن فاسده اما هنوز داره مربیگری می‌کنه
+احتمالا این شخص فراز کمالوند هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107047" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107046">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=SD-pyBe9wUqIr61M7C7ROu1M7VE79nPsH933CQ1ZJOXXY_Gh9XYN6GJaUgrPYGyf0KCjPpV6N8NYpjo8iUa2Tf9CHIRihZU-9gVsLumV3zj0ZT5yxdgGNIxX_0jUImA8Jamy8TemquuvR8k8WX4nagsmDEc-ZV4H32Xef6zwbLUTSHwfu76JvPOrDWr8SyD7-s7tRr4rJ0h5ZCB3zG7miT2y_FOzkSXbRyKwB5c7ABMt3WKeu-0ZVpZ0_C_4Orop_FiOsEhSUTI31Y4q_zSeWNIxUnIensX-cURABlf_bkdXR5QccwS9lxjU-xrE7St3ub4Zl2Wt-AezIPVvHNfn5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=SD-pyBe9wUqIr61M7C7ROu1M7VE79nPsH933CQ1ZJOXXY_Gh9XYN6GJaUgrPYGyf0KCjPpV6N8NYpjo8iUa2Tf9CHIRihZU-9gVsLumV3zj0ZT5yxdgGNIxX_0jUImA8Jamy8TemquuvR8k8WX4nagsmDEc-ZV4H32Xef6zwbLUTSHwfu76JvPOrDWr8SyD7-s7tRr4rJ0h5ZCB3zG7miT2y_FOzkSXbRyKwB5c7ABMt3WKeu-0ZVpZ0_C_4Orop_FiOsEhSUTI31Y4q_zSeWNIxUnIensX-cURABlf_bkdXR5QccwS9lxjU-xrE7St3ub4Zl2Wt-AezIPVvHNfn5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
تعریف و تمجید حمید مطهری سرمربی فولاد خوزستان از سهراب بختیاری زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107046" target="_blank">📅 09:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107045">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=QEYfVo0Vv0Vy0pp_54pKRdLymMzAVPvFAVYfhQwfSSYcXbPK52wvvhdDed5lpSkLYm3YfuPHFJRVN9VIeE1MEVE6adxH8sPUmccNBrjeTZwvFY_xLmW2j71C8LFFfjc5kTSuKmotEgdqFB0-FkMVFE0A-IJTZjxEY7eBfSxIMlWXhQUOapWdzHBnFJSMXAQ4Z-bo7ygxCo-ho71qHl6_rkce1fWsTGfQtP4t5RjdudaIx0xEvZcN0bX8K0xW71pHsc3uZ80-Rj5PiU8tAFxVEV_zqmWM6Sx1kusmiLKASCCUSgiLFLsUScvQRnc0Aj-b9ti8ODi-eIG0ntJVBxupLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=QEYfVo0Vv0Vy0pp_54pKRdLymMzAVPvFAVYfhQwfSSYcXbPK52wvvhdDed5lpSkLYm3YfuPHFJRVN9VIeE1MEVE6adxH8sPUmccNBrjeTZwvFY_xLmW2j71C8LFFfjc5kTSuKmotEgdqFB0-FkMVFE0A-IJTZjxEY7eBfSxIMlWXhQUOapWdzHBnFJSMXAQ4Z-bo7ygxCo-ho71qHl6_rkce1fWsTGfQtP4t5RjdudaIx0xEvZcN0bX8K0xW71pHsc3uZ80-Rj5PiU8tAFxVEV_zqmWM6Sx1kusmiLKASCCUSgiLFLsUScvQRnc0Aj-b9ti8ODi-eIG0ntJVBxupLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
فوش ناموسی بلینگهام به مادر داور بازی با اتلتیکو که شکار رسانه‌ها شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107045" target="_blank">📅 09:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107044">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=sKEFvg2xDVYWqxt-zltuPC_LLR4_vAIXyGopMrbT23He-7j4_b2BUDpOzd-z2mi-iwSgVhhpDMdEe1zByDIcG1Cp16btt2oe1MhnM_A0wwmPmY0mUJ4k7-yIHGko_fHUEYCINd1BMHzdB5PGsmKW02-uNnuoB2h7m160Br7IIJc31ggGiolBs7dQeocKo4Rc3K6ROQl-XTEWisfZL-N1XJytcfbGjzBvWBzLVmfV3Z-bX1G_hpe_UYSQrVmemXyuXDvOY2MTL6QnO2xZgau_GC3vU4YJnMeMsg-EZ8R16YIGrH0tn7tFNPnhcqAokMIitA0ZiZoFD7SA-GF2k40luQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=sKEFvg2xDVYWqxt-zltuPC_LLR4_vAIXyGopMrbT23He-7j4_b2BUDpOzd-z2mi-iwSgVhhpDMdEe1zByDIcG1Cp16btt2oe1MhnM_A0wwmPmY0mUJ4k7-yIHGko_fHUEYCINd1BMHzdB5PGsmKW02-uNnuoB2h7m160Br7IIJc31ggGiolBs7dQeocKo4Rc3K6ROQl-XTEWisfZL-N1XJytcfbGjzBvWBzLVmfV3Z-bX1G_hpe_UYSQrVmemXyuXDvOY2MTL6QnO2xZgau_GC3vU4YJnMeMsg-EZ8R16YIGrH0tn7tFNPnhcqAokMIitA0ZiZoFD7SA-GF2k40luQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
شعر خوانی جالب قیاسی:
«مثل رابطه سهراب بختیاری‌زاده و صالح حردانی
مثل حال دروازه‌بان بعد از تک به تک شدن با یاسر آسانی
یا مثل حال اتوبوس تیم ملی بعد از جریان کنعانی»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107044" target="_blank">📅 08:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107041">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=hVV6OxgjT6Jz_GoTaUa1nCtCin_6WbP2IYRm7R-PRkthnpc40BLJRevSSP1ZSxpAlbOpaw76a46jdytGvnxmzCqXtxe85H5Er2R7wsAvgOsKz_RY-Br-jKRvS-0wuFRFBprT4mo4e4GVhrqoqP6DJiBGFYbbAcNpm-i1gQ4KYsrKG5aQt_Y02jwHIcuiFE60trutVpu7r-uwJobhN_TTFoknwfvwtVnbL3zT6D8S_8CvV6TMGuGbCHxaT4vvEQhp5_6zI4Yqhxzo_2bsveQvXUOp3XFa5q6MnqPTvdycOpcSSNTKSqb4y-0DQ01TJ5E6xvIrA3TApDo6rbXWt8VyVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=hVV6OxgjT6Jz_GoTaUa1nCtCin_6WbP2IYRm7R-PRkthnpc40BLJRevSSP1ZSxpAlbOpaw76a46jdytGvnxmzCqXtxe85H5Er2R7wsAvgOsKz_RY-Br-jKRvS-0wuFRFBprT4mo4e4GVhrqoqP6DJiBGFYbbAcNpm-i1gQ4KYsrKG5aQt_Y02jwHIcuiFE60trutVpu7r-uwJobhN_TTFoknwfvwtVnbL3zT6D8S_8CvV6TMGuGbCHxaT4vvEQhp5_6zI4Yqhxzo_2bsveQvXUOp3XFa5q6MnqPTvdycOpcSSNTKSqb4y-0DQ01TJ5E6xvIrA3TApDo6rbXWt8VyVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🐐
🇦🇷
رونمایی‌رسمی لیونل‌مسی از پیراهن ویژه خودش در آخرین بازی ملی با آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107041" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107040">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b37185041.mp4?token=ZH4mX-LUkzcvYAyCJP8__8aw53oOzcCJU7WqTZ4qCxzEHAumLL3Lwr3Xpx8_XJniFBjNxW22nuv7vDOwTD0K9GEWwKHWKcuKst1MuPmIchiuuaroQAHD60X_Nwb41TPH4GFSOXKNXg9Dot6jaHcdfm1-glWPx9AyrfFvBVwPIx0MfqOXursIDCf1aWpCtTB1b3YzA7qTWrb9YeoHMjIRPOScsk7lVp42bsA0jYW6OjUxjupc8d4wlOEQdMtZe71px3PJZUxwZkZv7uz4OWtrin3WoXIgL1rIjJrRM3lCjaNhQByO52YfD2ZXvD91HjVI3_9lIwB49Z7bwMB3D-2uvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b37185041.mp4?token=ZH4mX-LUkzcvYAyCJP8__8aw53oOzcCJU7WqTZ4qCxzEHAumLL3Lwr3Xpx8_XJniFBjNxW22nuv7vDOwTD0K9GEWwKHWKcuKst1MuPmIchiuuaroQAHD60X_Nwb41TPH4GFSOXKNXg9Dot6jaHcdfm1-glWPx9AyrfFvBVwPIx0MfqOXursIDCf1aWpCtTB1b3YzA7qTWrb9YeoHMjIRPOScsk7lVp42bsA0jYW6OjUxjupc8d4wlOEQdMtZe71px3PJZUxwZkZv7uz4OWtrin3WoXIgL1rIjJrRM3lCjaNhQByO52YfD2ZXvD91HjVI3_9lIwB49Z7bwMB3D-2uvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام علیرضا بیرانوند به میثاقی روی آنتن زنده: اگر نظام وظیفه اعلام کند من چه زمانی باید به سربازی بروم به جان 2 تا بچه ام فردا می روم سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107040" target="_blank">📅 00:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107038">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0QQVQtrpsLsjTM6lH6ldFyQQ7q3E_983zTNNckEBxpCXH5yOcIKLO3w3VBp4K124HIELR-ANCa2u0gU_wdZH4KilIUyKWzGjXIPPYTSXQfBO_yd9vBET4yusJ5tuVb2Lz66T-1_JULWx1wWSXwZWqWleX_UJTEElXQwPNX4d7S2G3rYCoV2yp9OETEu8znsWjqv1Tj9ndy6J2VjaVkQM96Qc0VoUNfMXsFekDijlcIZLKmfXdmP3A2pakQ2ZDyzFkgm6TVEeYOXl-ckuxhz_jbMIt_knDmeriaYw8CasCyEnj7WUym4H0G_O2H2dImvUfKbHk6H50KY6rq6q6Jm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qiekR-dcc9bOCKlNWCoRm24-1CLrRlSPXIdUeRGxIRLrYiDuFWndDHwBR_CohHY9mC1J6TxGJqLrff8n_hprUDTRgntSKMN9x0Pz1PGtpgz9J_pTPKEvCOffcnMSX-S2pq3xPe4_8JBMlRKlYLFrcHIhT0KI0U60MgdPyNnmrf2gdwhbFu1qGgsuDbNMdKmEG38g1_4xlZcdk60HIrUqRkUsuXaAeuMXDihvIm0_1PUY3a3tu5W2XiuAsYtoibGuzAc5J_oDXel9IOOAyVgfox7g51Mf0s_O5YyWppoOVRQKW_NYwaEEf75uGkfiFYiKAB7j0lgTNWyTM7z9oRRIQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
دلیل عدم دعوت اللهیار صیادمنش انتشار این استوری در ایام اعتراضات سراسری دی‌ماه ۱۴۰۴ است که باعث شده حداقل تا چند سال قید حضور در تیم‌ملی را بزند مگر اینکه به مانند سردار آزمون دست به پاچه‌خواری بزند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107038" target="_blank">📅 00:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107037">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
⭕️
‼️
اللهیار صیادمنش: در اردوها به بازیکن احترام نمی‌گذاشتند. حرف‌هایی که جوان‌ها نمی‌توانند بزنند را می‌گویم. در این چهار سال ۱۰ بازی دوستانه روی نیمکت بودم، ۲۰ دقیقه هم بازی نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107037" target="_blank">📅 00:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107036">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
⭕️
🎙
اللهیار صیادمنش: تا این افراد در تیم‌ملی باشند حتی اگر بخواهند هم دیگر برایشان بازی نمی‌کنم. در اردوهایی که زیر دست این آقا(قلعه‌نویی) دعوت شدم هم چیزی به من اضافه نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107036" target="_blank">📅 00:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107035">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
⭕️
‼️
🎙
گلایه تند اللهیار صیادمنش بابت ربط‌دادن عدم دعوت به تیم ملی، به مسائل اخلاقی: می‌دانستم قلعه‌نویی هیچ اعتقادی به من ندارد چون اصلا هیچ مسابقه‌ای را از لژیونرها نمی‌بیند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107035" target="_blank">📅 00:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107034">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1TutHKgPQ6BsPJ6lExBjINzWW8ue8jGOkU52rT0qAn4H-t_Un540MEdvthcw3c1ZGzVZsgfj0XXea94WAnCbqb4wAfKBNzfRLeivyBc0OynVz5uWfuDsRs3SPzlQZfPlQXFd4gArJMV0DwKyrVZb6S4gdTTwoRN76jW4mcWAcLmRSd3sZWNRHln7FQxjyayi61x2YO6MLL-ZiepVoKO9HZF3LVnhOO72UHWLXnR3GrJRvhL5vFPOvmOxVcdVjMydoRxOKnDzYXerXnzDlI0RCXVA-7y16j0ckZ7mUBjw5kKcuLYHNG9YS3Whhh0_lVbtyrfmwkSZF8n_W7UJyY4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
خاویر‌تباس رئیس لالیگا:
🔹
باخت دیروز رئال مقابل اتلتیکو صرفا جنبه فنی داشت. درست است که اخراج یک بازیکن حریف نادیده گرفته شد اما اینها بهانه خوبی برای باختن نیست. امیدواریم رئال‌مادرید واقعیت تیمش را ببیند و دست از جنجال بردارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107034" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
