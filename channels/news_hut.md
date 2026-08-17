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
<img src="https://cdn4.telesco.pe/file/iAPiwbzVj1zNLbp5VekDiDWwcDIAa4-kO7InvCF31_TYaNR6iPbUB1nYAAg_C-I7XjzbQK7r5n9ZcTnq_Ym3t4Y-ZHTvHEJoueZGFyeV2nmihtIqxa1FwB3yjhSgyT4wiyruIqQpQlcsx9TYWCaEDKMvsJQZkjCIBsjtr_e-AS8mzGB5UQV8D5mSaXwra7rNmDQDM234XbC7Iy6NgAXcaERU3tXwaRS53I66IVcqo5hREI_buZZ-uOq7xmt2RPQpBCLghANbNFdrq16RlrOSCmaT349gxGqKsuYdTvvy_O6T_bAvwFYHgKlj65KKKKaesBhS-E5rzP1cCaszJhCQeg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 121K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 17:57:56</div>
<hr>

<div class="tg-post" id="msg-70195">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af0d57a79.mp4?token=TxCUB0CocfcewxqZFHQTEiQCVHUZg8ixvKWBimVBn7vhRT7xsdLpdhza4ujL2gA5oIWjan4FXpeRXx0HXJ7Dreu6wElgMPOxjWRZZ64CPtFLuX2PGOgp69r_UAQUVetoIoLGSQSd58dxdrs-iamJyDDr0uJ8YfPkn7YO1K30iVD0S-2mtc0DmlOKOrgrX0QztfHpBiPKZH46nJvapAZvWNrkaSe3rAbMx12gNOTiel782b36hrE5_nHjFt0lx_3tODOp0H1WZ8wokarJi-r3H3egQ9ZC6B3JdarwCeV5LG82KGAAyly9KiCi7gk0SXI3HoDnaEVlNtYTmiwKLmyKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af0d57a79.mp4?token=TxCUB0CocfcewxqZFHQTEiQCVHUZg8ixvKWBimVBn7vhRT7xsdLpdhza4ujL2gA5oIWjan4FXpeRXx0HXJ7Dreu6wElgMPOxjWRZZ64CPtFLuX2PGOgp69r_UAQUVetoIoLGSQSd58dxdrs-iamJyDDr0uJ8YfPkn7YO1K30iVD0S-2mtc0DmlOKOrgrX0QztfHpBiPKZH46nJvapAZvWNrkaSe3rAbMx12gNOTiel782b36hrE5_nHjFt0lx_3tODOp0H1WZ8wokarJi-r3H3egQ9ZC6B3JdarwCeV5LG82KGAAyly9KiCi7gk0SXI3HoDnaEVlNtYTmiwKLmyKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اخیراً عرزشی‌ها این فیلم رو با موضوع «فیلم لو رفته از نشست مجتبی خامنه‌ای و پزشکیان» به مغز نداشته بقیه عرزشیا قالب کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/news_hut/70195" target="_blank">📅 17:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70194">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:  ما یک کانال ارتباطی مخفی با سپاه پاسداران انقلاب اسلامی داریم.  ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم.  @News_Hut</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/news_hut/70194" target="_blank">📅 17:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70193">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db02877d6b.mp4?token=X20XmLT5xBFnECpNMymUHdPF_QADnqCiG733pgJVUctZcAY1RHvpmaaZUdnhhfcRXELSv5vYgWsDD7ICHWi1-R56f74M2YsguqQ0Irn2SpmPz9kxscSBlNQAuLB2fbiwc4cT48YVODLtTsZ21uHy59C9mbhpLW3usnyl5AVtChBFoETgNYMdY2vrBEREpddUeSGBG_0eP9VSj_xXgWzE_1TbXPZdN_Wq1t9z1MXs4jXeBGT2iW3VZzzAIi-u0g0QbJgADX-9zE-nOg2pH-J453bIHSlcuq9FmoR7aHsbNs7zp1MciGLjsaiTJ6t5q5UstWycV3gGs8TsQiREWmKPsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db02877d6b.mp4?token=X20XmLT5xBFnECpNMymUHdPF_QADnqCiG733pgJVUctZcAY1RHvpmaaZUdnhhfcRXELSv5vYgWsDD7ICHWi1-R56f74M2YsguqQ0Irn2SpmPz9kxscSBlNQAuLB2fbiwc4cT48YVODLtTsZ21uHy59C9mbhpLW3usnyl5AVtChBFoETgNYMdY2vrBEREpddUeSGBG_0eP9VSj_xXgWzE_1TbXPZdN_Wq1t9z1MXs4jXeBGT2iW3VZzzAIi-u0g0QbJgADX-9zE-nOg2pH-J453bIHSlcuq9FmoR7aHsbNs7zp1MciGLjsaiTJ6t5q5UstWycV3gGs8TsQiREWmKPsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دزدی خونوادگی یه خونواده از فروشگاه؛ از دختربچه تا مادربزرگ، همه توی دزدی نقش دارن!!
@News_Hut</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/news_hut/70193" target="_blank">📅 16:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70192">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy_nDMSCk72-259resnuwInUgbLH5TDSNBsTcPFtFGnWTrToGTMfrb19jPzDL4sUygbB6ghgC1dWjrUXXNXqEMlCkvfR-EOLONmXxfzUcpzWXyu9DSEaHRXgNNQcHm4e1P7a9sZyLlPzNcsR8H5ZLZtvTKOQxNX8T_Hy10fzcI3T-dfwKbE8a7MZ5LwcJa5R2T36M1MRGt2wUDI29lMfF7y9V8DAEw5L_OP24uwTYas5aY56q7PoBxBIbiRJwDwicQI8vyM3edyDCuCvorHxqIPnM1YR75PgIsaDQwTwvonVg0SexE2epSiE1o7D_zHm7Evj5UaU7frdPYo-OLR5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس‌نیوز به نقل از ترامپ:«اگر عمان سد راه شود، آن‌ها را به‌شدت بمباران خواهیم کرد.»
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه گفت که اگر عمان در جریان تنش‌ها با ایران در تنگه هرمز سد راه شود، آمریکا آن کشور را «به‌شدت بمباران خواهد کرد».
ترامپ این اظهارات را روز دوشنبه در مصاحبه با «تری یینگست» از شبکه فاکس‌نیوز بیان کرد؛ آن هم در شرایطی که مهلت آتش‌بس میان آمریکا و ایران رو به پایان است.
ترامپ گفت: «اگر عمان سد راه شود، آن‌ها را به‌شدت بمباران خواهیم کرد.»
ایران هفته گذشته اعلام کرد که در حال مذاکره با عمان درباره چگونگی بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/news_hut/70192" target="_blank">📅 16:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70191">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4155a42fb1.mp4?token=OZmkk1NNp3h906Gb6cs9f49pJ2ea7tZLyfTcNIyM7TuEf6bVtrg-tLjXfeiQ268qTh4qf1jCawrzGwoj7zbdElL-s1Dn4-r9OXjTu_nJj5yzL_zn8hfUzShT8EgIWcS1AXM7l_Zx4FoOSvm218YpVU2yZUbncxtXFj6RI-yiQxtsUvXBZkgMRGbgau99uRxqnFPO3UeKOfX2-cxtOEPHnIAfQQgRSxOTxeZpw2pfO4pmCQ6GmWD7TBOxYsBNe7xC8xGt9vqVhpCSigbqjOhG4Wdtwnw9W4TQedNIIT6A7hlpCYmGUjXIApd6UuBFmuL9XfNumB0aZQT9vvjwatayxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4155a42fb1.mp4?token=OZmkk1NNp3h906Gb6cs9f49pJ2ea7tZLyfTcNIyM7TuEf6bVtrg-tLjXfeiQ268qTh4qf1jCawrzGwoj7zbdElL-s1Dn4-r9OXjTu_nJj5yzL_zn8hfUzShT8EgIWcS1AXM7l_Zx4FoOSvm218YpVU2yZUbncxtXFj6RI-yiQxtsUvXBZkgMRGbgau99uRxqnFPO3UeKOfX2-cxtOEPHnIAfQQgRSxOTxeZpw2pfO4pmCQ6GmWD7TBOxYsBNe7xC8xGt9vqVhpCSigbqjOhG4Wdtwnw9W4TQedNIIT6A7hlpCYmGUjXIApd6UuBFmuL9XfNumB0aZQT9vvjwatayxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یولکا؛ رهگیر پهپادی روسیه که برای مقابله با پهپادهای اوکراینی به کار گرفته شده است.
این پهپاد با تکیه بر رهگیری خودکار، به سمت هدف حرکت کرده و با برخورد مستقیم آن را منهدم می‌کند.
مزیت اصلی یولکا، هزینه پایین و امکان مقابله با پهپادهای کوچک با یک رهگیر ارزان‌قیمت است.
ویدیو، نمونه‌ای از استفاده این سامانه در جنگ روسیه و اوکراین را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/70191" target="_blank">📅 15:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70190">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2a93816b.mp4?token=CNjqPxD1-RwB0SWOry07ZSdsWB5AjYnpKQBsRPlJiBLVERznho-q-m23cJUcU7tkPhImFTNcbcbwND-1212YE0-Wl8osbkSMTQxmiqRTXBQa2dDfekJRGHmx0i9es1IsdqE1T-yUm7k-hqQSDUJGym1_pdeakq6YLNkgHdXXc0Z2_dsLAtwsVDo5PxG2CiOuVOehbMQW_jQAklODnbuE7LfZXr00AQwYOQByd1xcknJWNbqYqMM9SdsoFFm--0FJQO-5hmHySouBv66yjb8hLhYXzRALxuqAMozVyqndmJQbgMvkdwvg0dcQd5LruNPp0OnI6whDK26-xAh3cSlouw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2a93816b.mp4?token=CNjqPxD1-RwB0SWOry07ZSdsWB5AjYnpKQBsRPlJiBLVERznho-q-m23cJUcU7tkPhImFTNcbcbwND-1212YE0-Wl8osbkSMTQxmiqRTXBQa2dDfekJRGHmx0i9es1IsdqE1T-yUm7k-hqQSDUJGym1_pdeakq6YLNkgHdXXc0Z2_dsLAtwsVDo5PxG2CiOuVOehbMQW_jQAklODnbuE7LfZXr00AQwYOQByd1xcknJWNbqYqMM9SdsoFFm--0FJQO-5hmHySouBv66yjb8hLhYXzRALxuqAMozVyqndmJQbgMvkdwvg0dcQd5LruNPp0OnI6whDK26-xAh3cSlouw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما یک کانال ارتباطی مخفی با سپاه پاسداران انقلاب اسلامی داریم.
ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/70190" target="_blank">📅 14:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70189">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5140e7e1a.mp4?token=rYcpmPzBtv6CORoUcU9BYC3lZythqmDkAgn40_68RBK89KGAXZ5ueG7J1QsahMVazO6tkIS74LRyf1WbMKaTH5qryV9XQpDLQms8Tu-jbipEICEkqNCCywvd6-V6s9UO5I6F5ldseQJYziHgB-L4YwpIjKXRKKItdnIZfdfrRpgW9R0bdX1EhsrCigIdQemHZx8ojaUdunFdoPlvOck1nCgMZvwmvJUQtKPboiueO8uC7aCtsAq1xyVLwgNNhUzAO6JST02djeXodEOvXHbHTVLLr_8QURMmiFGdUf_L7OB9SXOL1U6xrVaI7-nNmRz4rH7zG9YKvBiKXuP9W9b_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5140e7e1a.mp4?token=rYcpmPzBtv6CORoUcU9BYC3lZythqmDkAgn40_68RBK89KGAXZ5ueG7J1QsahMVazO6tkIS74LRyf1WbMKaTH5qryV9XQpDLQms8Tu-jbipEICEkqNCCywvd6-V6s9UO5I6F5ldseQJYziHgB-L4YwpIjKXRKKItdnIZfdfrRpgW9R0bdX1EhsrCigIdQemHZx8ojaUdunFdoPlvOck1nCgMZvwmvJUQtKPboiueO8uC7aCtsAq1xyVLwgNNhUzAO6JST02djeXodEOvXHbHTVLLr_8QURMmiFGdUf_L7OB9SXOL1U6xrVaI7-nNmRz4rH7zG9YKvBiKXuP9W9b_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به شبکه فاکس نیوز:
اگر عمان مانع ما شود، ما آن‌ها را به شدت بمباران خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/70189" target="_blank">📅 14:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70188">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1480b179a0.mp4?token=CL5AR1JtknoMv87iPkgm_PpUpmZQtvGFL7SVfs03Ocy1GcPR4dA-mV_6-OzBlElFbh_ZUwGuEJnnnHl3qne0GXMhgiI_FfqFqrSjk7cnXMNu3DgH2hxnCPF9QBTwcz0xIKQeVL-sljK6ub-dSfknRmxcht2rVpljCZBNd8IUXCiG1EElhokTv0mVBIb5gKI6YdnwXsioIaycI5XRy-fWr5OfciWzWaAo1LX2isTyzRG0a9cPA8gjRLv4EzJ-dxIxcVT4HbVRowX3MqFnFsHMkqIDFJHBqDhgtQfvFXEVZfvjycJ2ZsVbRx2bQ5DGUCoN4hrOZ0h7NxCnl0N6zFoDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1480b179a0.mp4?token=CL5AR1JtknoMv87iPkgm_PpUpmZQtvGFL7SVfs03Ocy1GcPR4dA-mV_6-OzBlElFbh_ZUwGuEJnnnHl3qne0GXMhgiI_FfqFqrSjk7cnXMNu3DgH2hxnCPF9QBTwcz0xIKQeVL-sljK6ub-dSfknRmxcht2rVpljCZBNd8IUXCiG1EElhokTv0mVBIb5gKI6YdnwXsioIaycI5XRy-fWr5OfciWzWaAo1LX2isTyzRG0a9cPA8gjRLv4EzJ-dxIxcVT4HbVRowX3MqFnFsHMkqIDFJHBqDhgtQfvFXEVZfvjycJ2ZsVbRx2bQ5DGUCoN4hrOZ0h7NxCnl0N6zFoDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به شبکه فاکس نیوز:
ایران باید پرچم سفید تسلیم را بالا ببرد.
آنها در بازی پوکر خوب هستند، اما در حال نابودی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/70188" target="_blank">📅 14:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70187">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmhEi4ISno7nELNrDqlQ34lHO1CEjixqTzy4Bc2CQTktI4KXq3S3d6ROnidayIB-RtxrPh1U6rMfkg4psxHK3tR3zLKGhzS9fC23bEMHBSCPyexUMaJ38F9K3QTKj4c2kOTGVTavZTeYsKRj6hCn8j9X4s5MXAhlw5KbczWnZjdlWsGZ5QAwl-V6pmP4t7-Eije2MdpwWl_UD2oEm8PHd9dYVTCwXFZ-OHr0RS9Fp6SL-BlDuwqSqTyWxd8Rm58T7x1w2QuVTkwB_ZPdHRUiAmf6BfNaRZFS1yKHSwVGZ0FMdf-GfhUt6oblPNaN1PeDJVNnuj18KCIesNS08qwxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ترامپ در گفتگو با شبکه فاکس نیوز:اگر عمان بخواهد مانع‌تراشی کند آنها را به شدت بمباران و نابود خواهیم کرد.
ترامپ همچنین وجود یک کانال مخفی غیررسمی با سپاه پاسداران را تایید کرد و در ادامه گفت «هیچ عجله ای ندارد»
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/70187" target="_blank">📅 14:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70186">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnaCOeujyMJrihK4l-Oc4lLng9aWdOHQLQWyDNZMP8fV3C7ZLeY7r9YYO5gkexo56iNnmN9kJQWslhXdmkNqFFbB4gGLjdL4ZSEHUoXoeQz-5_m9Q2sSlWNJaCOvRFdOLRTVsi0KQgOOOpxACLs-GZd_cUypeh6kFOgS0Jgu_nqN3YljwU0_xUdAZzmqMMhegYSXAMl9wfLrv5ixirvkdPLkvBDMjsgSB_-u0zIkvgGAPrCxZYTr8u-R9ZjjW6n6ylAOZaxZgW4ZEmYJd8M9NMCr22xhNlNcHww2NGJsnfSGPJ5ou-Hl9WMfg1BVQA1D5hkNb9pDEOdahb7q6zfc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
📰
وال استریت ژورنال:رهبری ایران ظاهراً جنگ و درگیری فعلی را پایان ماجرا نمی‌داند و خود را برای احتمال یک رویارویی گسترده‌تر و طولانی‌تر آماده می‌کند؛ هرچند ایران همچنان از نظر اقتصادی و نظامی با محدودیت‌هایی روبه‌روست.
🔴
آماده‌سازی ایران برای رویارویی احتمالی گسترده‌تر؛
بر اساس گزارش وال‌استریت ژورنال، ایران پس از آرامش ایجادشده در پی توافق ژوئن، به‌جای تکیه صرف بر دیپلماسی، روند بازسازی توان موشکی و پهپادی و تقویت ساختارهای نظامی و امنیتی خود را دنبال کرده است.
این گزارش همچنین از افزایش هماهنگی با نیروهای منطقه‌ای، تشدید فشار بر کشتیرانی در تنگه هرمز و دریای سرخ و افزایش تهدید علیه زیرساخت‌های انرژی منطقه خبر می‌دهد.
به نوشته این گزارش، جریان‌های تندرو نیز نفوذ بیشتری در ساختار نظامی و امنیتی ایران پیدا کرده‌اند. هدف این راهبرد، ظاهراً افزایش هزینه هرگونه حمله احتمالی به ایران و تقویت بازدارندگی در برابر آمریکا، اسرائیل و کشورهای خلیج فارس است.
در مجموع، ارزیابی مطرح‌شده این است که تهران درگیری کنونی را پایان ماجرا نمی‌داند و خود را برای احتمال یک رویارویی بزرگ‌تر و طولانی‌تر آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/70186" target="_blank">📅 14:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70185">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ygb4laiRUG0Pu4onXoUeXa5NIWzWXOUnFav9alpFFzW3W5RjtXaR0j3-hkuZFQ1e4YQsUnT_PI3YmzcSjtfgR_TK1lD3sUo9uJ6OEiF2Wbc_IPgUHPTmGeFFhkbg-i07K8aCkBq6aF1ldGBNIN4cef460a2IAD5nca6rGSZELVtbj9wJGUIOCzZsxBx1SKXyYRdEuQT5F_o8tn9MjI4GqBis5pI334T7KeNl4quXt4bdOutVsGfepOvi8O6rGeRJk_6SFhXOZGT5AutXuP471chLre3PtcFPOysQ8UPMIBJG53D1gGGezWTj41txePrkt13KoAsXqCI8pKuoVxqOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
هدف اصلی این است — و همواره چنین خواهد بود — که ایران به هیچ‌وجه و تحت هیچ شرایطی نباید به سلاح هسته‌ای دست یابد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/70185" target="_blank">📅 13:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70184">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎤
خبرنگار
:
آیا جلسه‌ای داشتید؟
🇺🇸
ترامپ:
جلسات زیادی.
🎤
خبرنگار:
جلسه‌ای درباره ایران؟ پیشرفتی؟
🇺🇸
ترامپ:
🚶‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/70184" target="_blank">📅 13:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70183">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4BnMB25mDWXE_PrOTz9k6kXp_pBAqJchO-jazDtRu4-doSsLacln_akZ8EW8kLtjfCXI9_PMP6ApYnnpIrMcxb81-qiALQidlPaO4Omt24NTSkqm2Ml7CDO92J1hotlwuuCXmWxbvS8gJo4yj37YYX6eo57aRY0ZCB8m-J2qoTFmA7K91dYW_dLTEZjaF5-9z-0I9wiM3N3qLif5ZhxMqUPrm7gCyPdNoRQD-2e35uOwsufMQa013kM893u8FJdgVzxVMnHa5-zcqF7B-8jdD65ap52P82GeVrpOPE9xZXqdU4b7Vlv1A2jPwPcrqdT-OwBAW79DfG-0uWWInlutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی: آتش‌بسی وجود ندارد که بخواهیم آن را تمدید کنیم؛
آنچه در پایان جنگ و در یادداشت تفاهم اسلام‌آباد اعلام شد «پایان جنگ» بود. آمریکا تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شده.
ما چیزی به‌عنوان آتش‌بس نداشتیم که حالا بخواهد تمدید شود؛ ما «پایان جنگ» را داشتیم که حالا وضعیت جدیدی پیدا کرده است.
مهلت ۶۰ روزه در واقع ۶۰ روز فرصت برای مذاکره به‌منظور دستیابی به توافق نهایی بود و اساساً چیزی به‌نام «تمدید آتش‌بس» وجود ندارد.
قطر و پاکستان به‌عنوان واسطه پیام‌هایی را ردوبدل می‌کنند و با ما در تماس هستند، ولی این به‌معنای مذاکره نیست و تصمیمی برای شروع مجدد مذاکرات با آمریکا نگرفته‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70183" target="_blank">📅 12:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70182">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3274b73d22.mp4?token=XdXl9GOIrP0bguhOIV5pkKSwgQot6RmEZGN_uFDkFdK3fgTwjMb2J095Vants3pIEk8GBtHwfxxcEtSQ1QM2VqlG4foF_GRpcoZqTbtYY7pJfqJPDtWOLITAni2a2DsOqtBRgNUNuQOUg9yuJcgsy1mATJqIXoLUtgocOFHw4ZlxQoVF-TPKyZrpbW4O5HgpjE4e1YogpVan4obcygqF2BhzaX9lbUL6OQ1ondX6unPF2m4x1D3jCP44SwFJ3OzxxBBkJtJ8Vqq7jVQCH9Nk_NM59CaiTdY3lNZ-x3MshjoYCishxOA0LvDvmuMUrGdMSOZWyF6Iq8JYyFePN2BqXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3274b73d22.mp4?token=XdXl9GOIrP0bguhOIV5pkKSwgQot6RmEZGN_uFDkFdK3fgTwjMb2J095Vants3pIEk8GBtHwfxxcEtSQ1QM2VqlG4foF_GRpcoZqTbtYY7pJfqJPDtWOLITAni2a2DsOqtBRgNUNuQOUg9yuJcgsy1mATJqIXoLUtgocOFHw4ZlxQoVF-TPKyZrpbW4O5HgpjE4e1YogpVan4obcygqF2BhzaX9lbUL6OQ1ondX6unPF2m4x1D3jCP44SwFJ3OzxxBBkJtJ8Vqq7jVQCH9Nk_NM59CaiTdY3lNZ-x3MshjoYCishxOA0LvDvmuMUrGdMSOZWyF6Iq8JYyFePN2BqXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی که دانش آموز ایرانی استرس کنکور و بمب و موشک رو داره همون لحظه وزیر آموزش پرورش و هیئتش
😵
😵
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/70182" target="_blank">📅 12:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70181">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70181" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/70181" target="_blank">📅 12:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70180">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V88nIbZVqU-Y4fNWZ-PSmfEqLcMAKBr2rw9wQT8XM3SO8BtK-fjyrbG_hxbJ-PobBJzSv1rH761UD8Ubbm6wC1Ru_06IeD7t-EGnd_i3GcGDiaWe-l8JNd7i4llGCmqfOi2D8-lDDw9W7nRzmr4SbHkiRUA7rFdSQ_CPaWDdbvhgywl_tyLCt-Byq3qfH9H3krqfgQg65DuDRa-uCr5_KNuzwXt5NLHThElnBneI7_a9kta_X-U57kpdwUoX1BagUopTWiR_UFMwoNc8dTIwmItki_4fYrYULbLJ4U2X0G2ncW1KgS4dY91eDliA-seTPirriwNKv1q02Yv0Go2lIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r26
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/70180" target="_blank">📅 12:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70179">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cd85b555.mp4?token=uuyGfrvKYGZUsEPJ_W2NEI-UHE2mDtOv37ObufFp2pwV8RxsE4esi7uGbwwKYKHil9yK65yadPlldyr24YAePJZGQfOqp_s7MsbhozlP0UUzB3I2CW5xb0uCFQTCi3lPeFrlbr04PlooOTefeffLPMmgkr1EO4tISQytSO4lZUGf0rhVhRsGUUd-GOdzG5AUg4vkqRh0r7fkURb6CNQEWUN14W75k9pDgH5vaC9sl0RzlSaQhDhBnxvq7Fr2UlyGZSWw07g2b-B6vz9G8AIMKzcTi8cpwIYbD8DY6rEHitoZUEjqZBcPrlzic4R6CqVlns9KIO75OMpNw3Ej7J360w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cd85b555.mp4?token=uuyGfrvKYGZUsEPJ_W2NEI-UHE2mDtOv37ObufFp2pwV8RxsE4esi7uGbwwKYKHil9yK65yadPlldyr24YAePJZGQfOqp_s7MsbhozlP0UUzB3I2CW5xb0uCFQTCi3lPeFrlbr04PlooOTefeffLPMmgkr1EO4tISQytSO4lZUGf0rhVhRsGUUd-GOdzG5AUg4vkqRh0r7fkURb6CNQEWUN14W75k9pDgH5vaC9sl0RzlSaQhDhBnxvq7Fr2UlyGZSWw07g2b-B6vz9G8AIMKzcTi8cpwIYbD8DY6rEHitoZUEjqZBcPrlzic4R6CqVlns9KIO75OMpNw3Ej7J360w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
کارشناس پدافند هوایی سپاه پاسداران:
«در روزهای نخست جنگ، ۶ تا ۷ فروند پهپاد «هرمس» و «هرون» متعلق به رژیم صهیونیستی به‌طور همزمان بر فراز جنوب لبنان در حال گشت‌زنی بودند.
با هدف قرار گرفتن این پهپادها [توسط ایران]، شمار آن‌ها در جنوب لبنان به تنها یک فروند کاهش یافت و بدین ترتیب، آزادی عمل بیشتری برای انجام عملیات در اختیار حزب‌الله قرار گرفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/70179" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70178">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe1c04e38.mp4?token=SpI5jjybyIImF2soxDh1PYtppD46qJ-p8DrBM6-1Spx023vpBUBc3PNrXnZ8gXs2CTCtfHLaAl53vG0HJVH1n4aCV-hlW3QImfHmWa2bKq8Yy4e1GRIkzJTgQ7Vaun6HlaZTyOu-cdQbjKXYScpuAoJt7UQ2tmsl2N-a6o_UVnxpbC1c4CKtvdXe2QMTPdh7aAV6ENLuXeE3j72J1Nvdl3pJlg1cMnbTCf-7srZuIspQ1YCPHEKBxKItd3gRwGiNI_BqD02OhL0bTojhyn522Z4NXNeWqWUP_Xtza0XurZEkks57J7Z5WrfIek7iwP0yNMXKolGSv2YaE3U-qy6brg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe1c04e38.mp4?token=SpI5jjybyIImF2soxDh1PYtppD46qJ-p8DrBM6-1Spx023vpBUBc3PNrXnZ8gXs2CTCtfHLaAl53vG0HJVH1n4aCV-hlW3QImfHmWa2bKq8Yy4e1GRIkzJTgQ7Vaun6HlaZTyOu-cdQbjKXYScpuAoJt7UQ2tmsl2N-a6o_UVnxpbC1c4CKtvdXe2QMTPdh7aAV6ENLuXeE3j72J1Nvdl3pJlg1cMnbTCf-7srZuIspQ1YCPHEKBxKItd3gRwGiNI_BqD02OhL0bTojhyn522Z4NXNeWqWUP_Xtza0XurZEkks57J7Z5WrfIek7iwP0yNMXKolGSv2YaE3U-qy6brg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ممدانی اومده یه ویدیو از خودش منتشر کرده و برای شهروندان چینی نیویورک، با زبان چینی صحبت کرده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/70178" target="_blank">📅 11:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70177">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b0e3619.mp4?token=jZeXu_VkNBe9GSfU8ICfbYZ_0zRZ1i8rPOSmptiGoajE1hSqU_pvVfVRyIINYBRoim3quHg5ecN5XFEWc8963g0MMTyVZeNdS_wBnoXoEayKRaoyhWBKtEhj6MszPBsPIm15eMh59dYnhkvfWCM84V1-Dakib_zfzrSvHIH4CCkVsW86Sz2_Hv_R2PBsUWHds3YcGIAbuJRKIex1PEtHfovQCT_j8BnE_db0K-ixVu_3bZBagEeR2xf4S2x8wya8TaD4eSye1fW9NaixpGIxgGTEWHE02LYzshXZTeKLvTmNG5tKtNHDkf_WrzAq106H5kZ75sQJ8AvT5U0PY3t2yrfpvFAtDFqUfevp5QCmBExpQ5ycN1mCYf_L7aleVsDakJEiGkMYPTAxxYFFCBX017I2NxI3XzoybFyz8qr7hBfDeLI34sHK6K5oLioL8BGAALIPD5R6yIT9jM0rnzwipmTHbTapzVAc-DS-y6-0S3KlqeBnoqKv75pKExhWF7JdKZ6hzJFsrHzTjPitP4FfO-d5WV29P5VNtGVIUVp8kBx4IvvH88bm0mNrtMSp_ndWpZ19z0GggMBauljZ0QU82gROLJ7qaqdyad4qufDQEsjQblYWHQGWN8DWJ84H_62HlI4vxF8TnFw763niLmIa81V2rkEuaDp5c7aBE8FJhHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b0e3619.mp4?token=jZeXu_VkNBe9GSfU8ICfbYZ_0zRZ1i8rPOSmptiGoajE1hSqU_pvVfVRyIINYBRoim3quHg5ecN5XFEWc8963g0MMTyVZeNdS_wBnoXoEayKRaoyhWBKtEhj6MszPBsPIm15eMh59dYnhkvfWCM84V1-Dakib_zfzrSvHIH4CCkVsW86Sz2_Hv_R2PBsUWHds3YcGIAbuJRKIex1PEtHfovQCT_j8BnE_db0K-ixVu_3bZBagEeR2xf4S2x8wya8TaD4eSye1fW9NaixpGIxgGTEWHE02LYzshXZTeKLvTmNG5tKtNHDkf_WrzAq106H5kZ75sQJ8AvT5U0PY3t2yrfpvFAtDFqUfevp5QCmBExpQ5ycN1mCYf_L7aleVsDakJEiGkMYPTAxxYFFCBX017I2NxI3XzoybFyz8qr7hBfDeLI34sHK6K5oLioL8BGAALIPD5R6yIT9jM0rnzwipmTHbTapzVAc-DS-y6-0S3KlqeBnoqKv75pKExhWF7JdKZ6hzJFsrHzTjPitP4FfO-d5WV29P5VNtGVIUVp8kBx4IvvH88bm0mNrtMSp_ndWpZ19z0GggMBauljZ0QU82gROLJ7qaqdyad4qufDQEsjQblYWHQGWN8DWJ84H_62HlI4vxF8TnFw763niLmIa81V2rkEuaDp5c7aBE8FJhHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک شهروند اهل فلسطین:
لعنت بر ایران که ما رو به این روز انداخته
عامل تمامی بدبختی های خاورمیانه و کشور های عربی ایرانه
اونا ما رو تحریک کردن گفتن حمله بکنید
اونا باعث شدن نزدیک دو میلیون نفر اینجا آواره و کشته بشه
کاری با مردم ایران نداریم اونا هم مسلمون هستن ولی حکومتشون خدا لعنت کنه
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70177" target="_blank">📅 11:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70173">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDV2QJH6vYFJVHs4zHE0YScwpSSxdosxdTTpAGc1WX7yRAs3cRDf0DrITDXaSpptBpCa0q15JENUzpG7XXq42dGuHz6B-Bt1wGL608bv-KUBy1ASxAGffugI7Cyz8ZRR0_BHp1C1vHJPF0AewaOMme-hdGLItR1Po1ScGANe0ou9tzaGNQqVemWO0XkmINbp1mU6l65PGvtJtrh13A9r6hCV6RzngyFEossmty5yKuOYQ4YRxj5gxloqQXIlMgildh8VGFeGzpXPHJYQ2Qny1pyBE63CzX878N5IK1IfooOzlPO-mHIsBTrruxM-hdkhgIrTa3ZQq38VEt0U5tQHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168e601701.mp4?token=lJjEx9ZfDvtZT9xCyQR9lVp_5VtxqADaiOa56J9kvrVQ6huP7sWIZ-PjyfAY31ha9gYX43tWUN7TPUinH3A8AQNcrksGn5ZaFUc5u6ViQ7w2yhH8GzbVEfX5oxgwum-ZD_sxnaljNAZYea3IUf9iMQCfGYggWDfxD0TJ0bAKQTKHAQER5_7E-lSPlvnjAUnuXaGNLropUTiArp7p_MsvXCNW9xJJfTNnmuyxrgRq9z5stBUsa75l3OfTi7k7f7yqM-9jKkWYYOFJFfqQxwBtCCKUTxmZLjiGSWCqrju23xn13BoPm5iEFRjwNjhqzE161pg9GvOXhL0Yhpmb48orJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168e601701.mp4?token=lJjEx9ZfDvtZT9xCyQR9lVp_5VtxqADaiOa56J9kvrVQ6huP7sWIZ-PjyfAY31ha9gYX43tWUN7TPUinH3A8AQNcrksGn5ZaFUc5u6ViQ7w2yhH8GzbVEfX5oxgwum-ZD_sxnaljNAZYea3IUf9iMQCfGYggWDfxD0TJ0bAKQTKHAQER5_7E-lSPlvnjAUnuXaGNLropUTiArp7p_MsvXCNW9xJJfTNnmuyxrgRq9z5stBUsa75l3OfTi7k7f7yqM-9jKkWYYOFJFfqQxwBtCCKUTxmZLjiGSWCqrju23xn13BoPm5iEFRjwNjhqzE161pg9GvOXhL0Yhpmb48orJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بالاخره عکس‌های عروسی رونالدو هم اومد؛ این دو زوج خوشبخت تو همون اتاق نشیمن خونه‌شون تو پرتغال ازدواج کردن.
⏺
جورجینا میگه اونا عمداً اتاق نشیمن خونه‌ رو انتخاب کردن؛ همون جایی که:
صبحونه، ناهار و شام میخورن و زندگی روزمره‌شون رو میگذرونن...
اونا میخوان 30 سال بعد، وقتی بچه‌هاشون به اون میز نگاه میکنن، بگن: "اینجا یه اتفاق فوق‌العاده افتاد؛ مراسم عقدِ پدر و مادرمون."
+اونا تو خونه‌ای ازدواج کردن که تو ماهِ 7اُم سال تحویلش گرفتن و ساختنش هم 7 سال طول کشید.
+تاریخ عروسی هم 11 آگوست، دقیقاً دهمین سالگرد روزی بود که واسه اولین بار همدیگرو توفروشگاه Gucci تو مادرید دیدن، اصلا به همین دلیل هم کل لباس‌هاشون از برند گوچی بود...
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70173" target="_blank">📅 10:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70172">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
📚
كارت ورود به جلسه آزمون سراسری کنکور ۱۴۰۵-۱۴۰۶ منتشر شد
؛
داوطلبان کنکور تا چهارشنبه ۲۸ مرداد فرصت دارند کارت آزمون خود را از سایت سازمان سنجش دریافت و چاپ کنند
.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/70172" target="_blank">📅 10:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70171">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b010614a.mp4?token=UcUbWpBfv5f9oVUDaHIkomaDm5v3owgaIGJzalmnaRn6ol04kUwh7WJWwfXWV_26CCVi3_wZqnNG7qM3jOmMjDvMSmXXB4CoDOACX8_7vnlDy4DFK2hfn7LgnKVWR-9ohdYjfAhAj2_ncvT_fnkAgxaIMbznupsuGvNXLy0u-qbiCCd5Ls-b2DCl-V67gpsJsqCvWcMEM8yL98RWywdcxz_PswfOfsknhuNAGbss2sdrOOShFE7JA5i8njVpBWqalq0zYnk5VI7fu8UsM3pO7_eA406bg8ByzwC1TKpkzqw7iulVX8gWAssu8RlAmD3VcpKaicrq-ejr4zNBJN2LeQmqHOnDJxGznGBpU74HCv7vcYgzG1LiosOhGTS0jQIzk4Y3BF8OT5r43lS_Tq2UBz3MK6nr0JPQ-X5nLBAxHh3QCn7DKDGt4dQQjgPm673VkBYlRNGsV-KK_Q-fJYgjDK19csk4nZ5W9v6cj9uELeb1uZMzcQ-CmiAyIj0oNrr9RY1hZhWk62NvxSseU6O3CkVXei5kj258NuTHVbG5nFqpEJcUlIZWJuPNFgHWllhQhZarE_S729et2w55Uicpq7COmFwCRBeV9xGfUoB0t_uZ70feuinxVAqjWgr7YXhiH2JToV9fFX8hIFU6a5Ccy0YS9zpEtrXGpUiQLsQFlXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b010614a.mp4?token=UcUbWpBfv5f9oVUDaHIkomaDm5v3owgaIGJzalmnaRn6ol04kUwh7WJWwfXWV_26CCVi3_wZqnNG7qM3jOmMjDvMSmXXB4CoDOACX8_7vnlDy4DFK2hfn7LgnKVWR-9ohdYjfAhAj2_ncvT_fnkAgxaIMbznupsuGvNXLy0u-qbiCCd5Ls-b2DCl-V67gpsJsqCvWcMEM8yL98RWywdcxz_PswfOfsknhuNAGbss2sdrOOShFE7JA5i8njVpBWqalq0zYnk5VI7fu8UsM3pO7_eA406bg8ByzwC1TKpkzqw7iulVX8gWAssu8RlAmD3VcpKaicrq-ejr4zNBJN2LeQmqHOnDJxGznGBpU74HCv7vcYgzG1LiosOhGTS0jQIzk4Y3BF8OT5r43lS_Tq2UBz3MK6nr0JPQ-X5nLBAxHh3QCn7DKDGt4dQQjgPm673VkBYlRNGsV-KK_Q-fJYgjDK19csk4nZ5W9v6cj9uELeb1uZMzcQ-CmiAyIj0oNrr9RY1hZhWk62NvxSseU6O3CkVXei5kj258NuTHVbG5nFqpEJcUlIZWJuPNFgHWllhQhZarE_S729et2w55Uicpq7COmFwCRBeV9xGfUoB0t_uZ70feuinxVAqjWgr7YXhiH2JToV9fFX8hIFU6a5Ccy0YS9zpEtrXGpUiQLsQFlXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثبت تصویر یکی از مرموزترین و کمیاب‌ترین گربه سانان جهان تو ایران
:
ویدیویی جدید از گربه پالاس تو ایران منتشر شده؛ گربه‌ای فوق‌العاده مخفی‌کار و گوشه‌گیر که دیدنش حتی برای محیط‌بان‌ها هم بشدت نادره.
واقعی بودن ویدیو توسط منابع معتبر تایید شده
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70171" target="_blank">📅 10:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70170">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e92b4117c.mp4?token=BdbrYSrpJCTlVtU6jdYzieF0F6Sxcd88_sY7Kvx9jUQ_i8PwRJUVvkvG141OelL5WgOK3JHl6LqTAOnNt4udg3g1-Vs4zkYodMdNiScanWoFFhl-lb-kw5CskE3gYc2URUGZ7Nv7CPrnF2Z665v2dTNwlgU2puLTrWHSmUuHlpvcY5JLeIStuWYjiVNyqDZZZJev4yH2xaby6vf8_-GPrvnHsk3arlZdUSJc2PWZFOKPiP30kXcpm2-InH4ZXWEXPStXprbZF1lBnqY9M2pWLpKbMc01gsE-B2wlvpUYxzS_c2XtLUVmUr5Ys6zQzb8g5YcOSAqN9GA6H3Fb_CYgPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e92b4117c.mp4?token=BdbrYSrpJCTlVtU6jdYzieF0F6Sxcd88_sY7Kvx9jUQ_i8PwRJUVvkvG141OelL5WgOK3JHl6LqTAOnNt4udg3g1-Vs4zkYodMdNiScanWoFFhl-lb-kw5CskE3gYc2URUGZ7Nv7CPrnF2Z665v2dTNwlgU2puLTrWHSmUuHlpvcY5JLeIStuWYjiVNyqDZZZJev4yH2xaby6vf8_-GPrvnHsk3arlZdUSJc2PWZFOKPiP30kXcpm2-InH4ZXWEXPStXprbZF1lBnqY9M2pWLpKbMc01gsE-B2wlvpUYxzS_c2XtLUVmUr5Ys6zQzb8g5YcOSAqN9GA6H3Fb_CYgPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
آریایی‌نژاد نماینده مجلس:
من تو مناظره ای که داشتم در وصف مرحومه مهسا امینی لفظ نامناسبی بکار بردم از خانواده ایشون و همه منتقدین عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70170" target="_blank">📅 09:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70169">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
نوید محمدزاده که پست حمایتی از فلسطین گذاشت مردم گرفتن روش حالا حمله کرده به مردمی که بهش انتقاد کرده:
قبلا از فلسطین حمایت کردم و الانم کردم و درادامه هم میکنم.
چون اصلا با اسرائیل حال نمیکنم و تا همیشه فن فلسطینم.
ما حکومتی کثیفیم اونوری ها میگن اینوری هام هم میگن وطن فروش
کله ببرید تو زندگیتون.
به بشر یکبار فرصت زندگی دادن چیشد که همه تیم کشی کردن و چرا انقدر باید راحت تهدید کنید ؟
من نه طرف اونوریام نه اینوریام من طرفدار زندگی ام.
میتونستم هرجا که میخواستیم در تاپ‌ترین جا زندگی کنم ولی اینجا موندم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70169" target="_blank">📅 08:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70168">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70168" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70167">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Gtk9O_3v81VGY1gi5UEisWt4y8XwOwbTPRsjjR5tjn9wzmpDP4IMRkY93cNFQ4h_SwKqMNXnEz9pLRY4Dn_480xoAFYdNeEp7l7JyGqj2nsnPiFiaH1_uQW9FYPDM2ns74ETFHmsox36JEjjtZiCdRnr9T013d8rgo0_DMkFOeyhdETNyHkVQmlg3-wJYoUN82Riuwj6clLWOzyZ-Oes5kWQDsqhWqaVi_-bMpuCoBqbCIlN4vms3TNJ8UZgeh2pI6B1A0Mzg2WuZybFv7doHYgBba7SXRGxvyzzJWxBNda-bD1xus46TrEC6zBOqSYKVWC_n3meFCHRgNA0lwZzaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Gtk9O_3v81VGY1gi5UEisWt4y8XwOwbTPRsjjR5tjn9wzmpDP4IMRkY93cNFQ4h_SwKqMNXnEz9pLRY4Dn_480xoAFYdNeEp7l7JyGqj2nsnPiFiaH1_uQW9FYPDM2ns74ETFHmsox36JEjjtZiCdRnr9T013d8rgo0_DMkFOeyhdETNyHkVQmlg3-wJYoUN82Riuwj6clLWOzyZ-Oes5kWQDsqhWqaVi_-bMpuCoBqbCIlN4vms3TNJ8UZgeh2pI6B1A0Mzg2WuZybFv7doHYgBba7SXRGxvyzzJWxBNda-bD1xus46TrEC6zBOqSYKVWC_n3meFCHRgNA0lwZzaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a25
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70167" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70166">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQok7quRRpPHq2kXrr2B28gsW4eOhrg6iodjae0Es_DH0qygJViIWIch6qQ3TzkC3uofgPa7A9JXtuCl_bhvHS7fUhcCuOECSaUXfVr6InC0zqNAYUFY3muwYoYS-aR8fa1bx6dbKNLlZFQMYM2vjHDsPHBvoCeij8bWG67aO2AM-JaboP2m5jXIJoFAUn_yt5tCcszOzHj1Yo2T4w6s8hys6W1mO99LSgyKEqCb8vERWZebZViWXnZoAy8XgtY5IOPH0vyf_JhbnfqbaWi6NzVYfIlnJxzF0G0m2lqDMxldhqx8DgtiVfWD80GDyJcip1P_LknCu0Lj3G3yvLSLQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
❌
مارجوری تیلور گرین، نماینده پیشین مجلس آمریکا:
در جلسات راهبردی درباره استفاده از سلاح‌های هسته‌ای علیه ایران بحث می‌شود:
بله، درست خواندید.
این واقعیت دارد. من حدس و گمان نمی‌زنم؛ من از این موضوع خبر دارم. و این شرّی مطلق است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70166" target="_blank">📅 01:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70165">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI8-YJ4bOMnZBXtQF-54SluStJDE0-AmFUtuiWGPf05EzZ3SArBc29hdAJKBELFAooBT1dMA0Db6KeaiVUlFi2_x8nw5G9fJ8hmcWGWCiAKE3c-hBa5FMj3c0j67NZmntmuEujMrPi9EY99F6KLXSUfI97w6NySVlj67qP2VsLZg_C4HUeXYwgxqIxA6gFYXHdMjGyqkF9oei45J7NBuAwioqyhdAqZeBgWLRBdH7FNIFCRTU6PU3x2ynE6QYHOmPR-rlLlF0grqT1q2blziIsdhz6YuHHKnaiaV1bGeX41rRYL30dn212QoSC8zEzYIMJHTuOuix1jz0fdT6ZDIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
ستاد تبلیغات انتخاباتی جدید نتانیاهو:
🔴
مجتبی خامنه‌ای، زهران ممدانی، رجب طیب اردوغان و نعیم قاسم را کنار هم قرار می‌دهد:
«آن‌ها می‌خواهند نتانیاهو شکست بخورد. نگذارید آن‌ها پیروز شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70165" target="_blank">📅 01:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70164">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOiVbrNzny_uGZkYbeCr_w68iS0Lk02dT2ojqz9IZSL1INCd_z_TObTqoaO3ymZMimtG-HW9UW2YfaRWm-kR2VUouuurmanoFnNxmeF_pdlCMJdG22pcmxHJ5bENmf_nZ-3fsOpCsphbUfCDzrR9D2fmr7sX1wSjPriWCDrtRFxC58YwCDhbvMCVNxvks_ipdQCllVdL-pqWjH6xg2SMyBLvajMv_DFhl2Aj0o7pVOQXf-DplOfiKDUnBCH4Qdqfh4_z05rnGSgpCOwu06H25_x4zTPsM58eVhZADvJLLorpJBeS8fNAYDkYQR81Fd_mZF-16FzwY_FWqzNjXZR8zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
🇮🇷
#فوری
؛مهلت ۶۰ روزه مذاکرات در چارچوب توافق صلح ایران و آمریکا در اسلام‌آباد به پایان رسید، بدون آنکه توافق نهایی حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70164" target="_blank">📅 01:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70163">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/letSbXlp1Q2yKX7L0DR-bpd85svGtuh6uw_oVrqtzP9v6xLCzveyF0TenKpcpTLrquQW7-DQhJ-0Bk8jA50Eox3aCIk8n0Ndty9oMZApoMhecCN0EtnoOenem_kKoC2X16kt0fh7dJ4AmO9D-Dz24k6voDSECR2A5TENDMC4wpjOa50k0MymyyfyBL5c1R9GnBJwJSoSLpfKsxp7QvDvP7fqEFPSH9QuKNvXWT0QecUbNGufrCZceVVWkot82SkQpFrCOdWFuF9LMooCv148E8USM6zM4yeGfzFu3p2BcH-NqWRShg9ffxAnP6Qx68MqDJBf_yL35naQD2AwC--vsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
با توجه به رابطه بسیار خوبم با کیم جونگ‌اون، رهبر کره شمالی، از اینکه ایالات متحده مدت‌ها پیش با مشارکت در رزمایش‌های نظامی مشترک با کره جنوبی موافقت کرده است، خشنود نیستم. این رزمایش‌ها نه تنها پرهزینه هستند — و بخش عمده این هزینه‌ها (طبق معمول!) توسط ایالات متحده آمریکا پرداخت می‌شود — بلکه پیامی کاملاً نامناسب و خصمانه به کشوری مخابره می‌کنند که در تمام دوران ریاست‌جمهوری دونالد جی. ترامپ، رفتاری محترمانه و عاری از تهدید داشته است. از این رو، و با در نظر گرفتن اینکه برای لغو کامل آن‌ها دیگر دیر شده است، به وزیر دفاع، پیت هگسث، دستور داده‌ام که این رزمایش‌های نظامی مشترک را به میزان قابل‌توجهی کاهش دهد!
⏺
اگرچه شاید موضوعی بی‌ربط  باشد، اما اخیراً از رئیس‌جمهور کره جنوبی پرسیدم که آیا مایلند در زمینه خلع سلاح هسته‌ای جمهوری اسلامی ایران با ما همراه شوند یا خیر، که پاسخ دادند: «نه، ممنون!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70163" target="_blank">📅 01:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70161">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRLbSZ5E3PK3dptuVoKGTYmXzPT0syHan_s7jiDvAh2PHltyHLyNxO_xzJl-W3iF2wSFZNh98CI9-FpXcc8BlWnr1Wd9biHld6u_F237Ark7MIvQqb2egBYREgZur9phQOjmKKrphsKNdk3cOyBpEaLFL5VLOY4WskXFwR2-kse5yLV6KU30aeRvDLbg6RWRq6-g7xqaNSOxi8F78b3-pze7OGYCU7HfCPeGKwslnL4yjDm7l_zusgPE_XRTlmaBYTOUSjvB-bFvL6wf5fLn-RFTj9VUxkTsg7UqNT5hRTGvYsKEnEWxLNBhZr6X9RmDQJ9Klfiq5R-_JEpJLXXnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d94596467.mp4?token=nxi5QgYZ_JjCvoF1BdkM-GCkbrnGyZno2FmCxMAXzy-ipHxR05yn8i50mzpzP06KI36vOQlgVRceLJc-dFdvYaMx79ERGfCtwBYaFZPaID48NwgI_J-qGIHXiALzqmpdAfFBrKme-Hb0vcgieafFxHkf79YmQ6yMBSw_i80leIjNU2CNIgrNKaA-n6OoK3Y01OPdZwoCQU3IiuhpXZHDp2U8kgOtYCNR73YMn9hrFxMqKIogU8uDHFzY21mK7ri0s1axiiq_FVPW_OTaH00GWaI5pS0r8ESW6Uqf29iVgWWRFqvZ_A5BA3F1Lc-_kzVhrSA-m4VGV8-iv4N_YdmbrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d94596467.mp4?token=nxi5QgYZ_JjCvoF1BdkM-GCkbrnGyZno2FmCxMAXzy-ipHxR05yn8i50mzpzP06KI36vOQlgVRceLJc-dFdvYaMx79ERGfCtwBYaFZPaID48NwgI_J-qGIHXiALzqmpdAfFBrKme-Hb0vcgieafFxHkf79YmQ6yMBSw_i80leIjNU2CNIgrNKaA-n6OoK3Y01OPdZwoCQU3IiuhpXZHDp2U8kgOtYCNR73YMn9hrFxMqKIogU8uDHFzY21mK7ri0s1axiiq_FVPW_OTaH00GWaI5pS0r8ESW6Uqf29iVgWWRFqvZ_A5BA3F1Lc-_kzVhrSA-m4VGV8-iv4N_YdmbrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام:
یک جنگنده رادارگریز F-35A نیروی هوایی آمریکا هنگام گشت‌زنی در آب‌های منطقه‌ای خاورمیانه، توسط یک هواپیمای سوخت‌رسان KC-135 Stratotanker در هوا سوخت‌گیری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70161" target="_blank">📅 00:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70160">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fddf8c9b.mp4?token=c53RRjnrf-jw7TbqDotZAzelhzYXwlhPhUSiGXgpwQtpeGjKkC8lz_4RSz6efLkZSxGyAWnWjBXXjokBbxoIqjseuSMis7cVqKTCP7JRPlWKOHAPl2QdwPMIKn7ZeK3Jjg22DoH4QkO_Fd1cUf9z-5x0cIgSkNaS4Xi0JhYPrX0me77xQzoScBfS8ysTTpCM7ZqM7Fb_zl0_8Y_x0LgrW2Eu1zBNfouMVsdnfJ5Z6RNhJrCzKEi0ACtBjxD6jfsSAJCvLxbOhUl6paEICQVoP3xsVz0LKdbpyC_1E7K4jKJ4QT79VLTrJQT0h5jip2ruBbwbx3ACA3GuJmtyJzuE1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fddf8c9b.mp4?token=c53RRjnrf-jw7TbqDotZAzelhzYXwlhPhUSiGXgpwQtpeGjKkC8lz_4RSz6efLkZSxGyAWnWjBXXjokBbxoIqjseuSMis7cVqKTCP7JRPlWKOHAPl2QdwPMIKn7ZeK3Jjg22DoH4QkO_Fd1cUf9z-5x0cIgSkNaS4Xi0JhYPrX0me77xQzoScBfS8ysTTpCM7ZqM7Fb_zl0_8Y_x0LgrW2Eu1zBNfouMVsdnfJ5Z6RNhJrCzKEi0ACtBjxD6jfsSAJCvLxbOhUl6paEICQVoP3xsVz0LKdbpyC_1E7K4jKJ4QT79VLTrJQT0h5jip2ruBbwbx3ACA3GuJmtyJzuE1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
قالیباف:ما در برابر آمریکا پیروز شدیم
منظور از این پیروزی، این نیست که ما ارتش آمریکا رو منهدم کردیم؛ منظور اینه که آمریکا و اسرائیل با ۹ هدف مشخص و اعلام‌شده به ما حمله کردن، ولی به هیچ‌کدوم از ۹ هدف، در هیچ سطحی دست پیدا نکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70160" target="_blank">📅 23:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70159">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e64058ea.mp4?token=PL7xrCEdBDMaN545J6G48G8tlErH8HnnPSWo3-eUXM3RlUacJ_fsk-cynT_ASQinvHYjLEyJ-Avvc_36am8T3P6RT_RaETlisT1o1vXvJFWzUR911Yx8J-OrBgaCB_qKumFTXgrAk6d1v5S2DfUzHtlzAMdvorCOjKnPZwv4TVHQL139iaG3y7tQcsWpC2Hc_7bs56vGlalE9ohD30Po05cqRV7zcEblxlXfLNDJIJpwlYE8o2xKzuaJ83w6p3hLgAIE2zZQcPYFH0UUheMTeiS50m_Yk5XZGMwy0b6eO8o4WCZjLCcoA2MmhMl6V8GmAyyTdZcf6BMcrIEYTPAGbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e64058ea.mp4?token=PL7xrCEdBDMaN545J6G48G8tlErH8HnnPSWo3-eUXM3RlUacJ_fsk-cynT_ASQinvHYjLEyJ-Avvc_36am8T3P6RT_RaETlisT1o1vXvJFWzUR911Yx8J-OrBgaCB_qKumFTXgrAk6d1v5S2DfUzHtlzAMdvorCOjKnPZwv4TVHQL139iaG3y7tQcsWpC2Hc_7bs56vGlalE9ohD30Po05cqRV7zcEblxlXfLNDJIJpwlYE8o2xKzuaJ83w6p3hLgAIE2zZQcPYFH0UUheMTeiS50m_Yk5XZGMwy0b6eO8o4WCZjLCcoA2MmhMl6V8GmAyyTdZcf6BMcrIEYTPAGbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ریحانه قاسمی زاده مجری صداوسیما:
جنوب ایران،فدای جنوب لبنان،اینو یادتون باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70159" target="_blank">📅 23:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70158">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGjzcips0jfONWvtPZy81GckeiaIiyZraf6BwxxeUYOMKwe9WAWilwICyWXzmPCDRnibkRrYHfo_rUbMeyyiAt23CWrSEzCic-t8_qknWWPLv9ToXvyxaxqEBb3p9galOsby65jPiDXiElvLjaLXLWA9_5gpVZVRPdgfUJsZTMMeMtCEcejMrZ11XTJiXbsAxDCMI7BeFVq8Or27o707hqjNDEQUKyE-iTXeI0Qmj0fpzPi-fHPM5Lf_VEbSm4S5z9mLvrQXCWt5DD_qfXT89xgLvLb9Dz5B-kJRT-USYPROqEahWt5QE8xz6JiVGtJokrEsY_6NBkwYjSU-byc_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
آسوشیتدپرس:
ایالات متحده در حال خارج کردن آخرین ناو هواپیمابر خود از غرب اقیانوس آرام است؛ در همین راستا، ناو «یو‌اس‌اس جورج واشنگتن» که در ژاپن مستقر بود، در بحبوحه جنگ جاری با ایران، برای جایگزینی ناو «یو‌اس‌اس آبراهام لینکلن» عازم خاورمیانه می‌شود.
این اقدام، غرب اقیانوس آرام را فعلاً بدون ناو هواپیمابر آمریکایی باقی می‌گذارد؛ هرچند اگر نیروی دریایی در ماه‌های پیش‌رو ناو دیگری را به این منطقه اعزام کند، این خلأ ممکن است کوتاه‌مدت باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70158" target="_blank">📅 22:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70157">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0bb40eea.mp4?token=gF7YnldcdJfZWatEEvpiFF9CUfub6OeuZev55z2gry-b_UwL0BKzNaVRP59vaeGW_zVrpdbL3F-54ITX6uw6L4o1MKgCakvUcHnNODEguAJ4llTCDnwCudTQAbkW4x2Z1CZuCWA_kZakd4KbmxCnr1EqqK00VBjxco8jOzuj4YBVIgaBgOJcdKs1-hboE9YliDDIMJngpZOZGgfFE6ufJdYvXOgMjAawKgMOZ21miS1MzZx65LiqVLNTPEVQB9CDWsTachxims0SSs6KywrIa6z7OeWxvvWJP9zHf12QbeswaObPFQelFftFwu4JyCiXVlLN-R7Zi3DrsoTaSbucdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0bb40eea.mp4?token=gF7YnldcdJfZWatEEvpiFF9CUfub6OeuZev55z2gry-b_UwL0BKzNaVRP59vaeGW_zVrpdbL3F-54ITX6uw6L4o1MKgCakvUcHnNODEguAJ4llTCDnwCudTQAbkW4x2Z1CZuCWA_kZakd4KbmxCnr1EqqK00VBjxco8jOzuj4YBVIgaBgOJcdKs1-hboE9YliDDIMJngpZOZGgfFE6ufJdYvXOgMjAawKgMOZ21miS1MzZx65LiqVLNTPEVQB9CDWsTachxims0SSs6KywrIa6z7OeWxvvWJP9zHf12QbeswaObPFQelFftFwu4JyCiXVlLN-R7Zi3DrsoTaSbucdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
املاکیه دلقک درباره کارولین لیویت سخنگوی کاخ سفید:
متوجه شدم که کارولین لیویت فرزندانش رو بیشتر از من دوست داره؛ بابت این موضوع خیلی نگرانم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70157" target="_blank">📅 21:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70156">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbbbc717f.mp4?token=eoBKN62tMbbxah7dcHtADHbTZnrbW6gsLKQPzjLsGmW4yxlxeTXONvT-nOrkJsruIr6hixq2OlHMtsJ889nYFdRRX46pi_AQNCiSvew5TuO9GwlN8wTKCrS5BlyZ-s0pUnDV3v6g6hSfI9lHQDl8Zz1i8e7Ll8MdlM1sdhfTyjysSvV__4fGqATBS_FHlxJnWUVR7N08EUk6hNMiWRBPaznf8GGY9X3B1w5FBWexeWrt2FOQ8mdQT-EbWNdEg89Z5pIUzuSHlNbf4BP_ypESb4F1smUQjpvPmJna2fOidU0UhiLoLYAyP5lt9z79Wn4J2Cy8JvHRzOgoAizffE02fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbbbc717f.mp4?token=eoBKN62tMbbxah7dcHtADHbTZnrbW6gsLKQPzjLsGmW4yxlxeTXONvT-nOrkJsruIr6hixq2OlHMtsJ889nYFdRRX46pi_AQNCiSvew5TuO9GwlN8wTKCrS5BlyZ-s0pUnDV3v6g6hSfI9lHQDl8Zz1i8e7Ll8MdlM1sdhfTyjysSvV__4fGqATBS_FHlxJnWUVR7N08EUk6hNMiWRBPaznf8GGY9X3B1w5FBWexeWrt2FOQ8mdQT-EbWNdEg89Z5pIUzuSHlNbf4BP_ypESb4F1smUQjpvPmJna2fOidU0UhiLoLYAyP5lt9z79Wn4J2Cy8JvHRzOgoAizffE02fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فرمانده کل ارتش ایران:
هر ایرانی ای که بتونه یه نیروی آمریکایی رو دستگیر کنه یا بکشه، ۳۰ هزار دلار (حدود ۵.۶ میلیارد تومن) جایزه میگیره
😳
پاداش نیروهای زن آمریکایی هم دو برابره و به حدود ۱۱.۲ میلیارد تومن میرسه
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70156" target="_blank">📅 21:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70155">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f4c542f7f.mp4?token=kTXDiFoLrjeWlzY3OrjtcZ2urBHpe3GGY4OnqOXxfioGpde_0AcOUV9xADHTroM1W52an1RhrUYuErEmO8b_Z7m58KU0GxrqHqEhRcg4Z0fzoPYcy9TGUW2Sddme4Sdw6EuYH4O4QcDr8ovDftAS9KZBwBs35eRTxaK9FIVmfwaEhhZJGZjhJNDwMiHqyLE9KnSsu3gQ3nSRrofIp2nBgjVvEaDoSgZRrOytM625XhbaPAvvF_N1hUpTjoV2ZIbewWp3befeSb6GchNCCA0ecypElZXj12Dtctufg3SgO8d840md9ph0V9LqQiuRWhYmvEZp7JHIrcvLUrpcllDvLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f4c542f7f.mp4?token=kTXDiFoLrjeWlzY3OrjtcZ2urBHpe3GGY4OnqOXxfioGpde_0AcOUV9xADHTroM1W52an1RhrUYuErEmO8b_Z7m58KU0GxrqHqEhRcg4Z0fzoPYcy9TGUW2Sddme4Sdw6EuYH4O4QcDr8ovDftAS9KZBwBs35eRTxaK9FIVmfwaEhhZJGZjhJNDwMiHqyLE9KnSsu3gQ3nSRrofIp2nBgjVvEaDoSgZRrOytM625XhbaPAvvF_N1hUpTjoV2ZIbewWp3befeSb6GchNCCA0ecypElZXj12Dtctufg3SgO8d840md9ph0V9LqQiuRWhYmvEZp7JHIrcvLUrpcllDvLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار خطاب به پزشکیان: نوه‌هاتون بهتون نمیگن کاری کنید که مدارس مجازی بشن؟
🇮🇷
پزشکیان : ما داریم کاری میکنیم بچه ها اگه مدرسه نیان ناراحت بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70155" target="_blank">📅 20:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70151">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf26ef809.mp4?token=XK8qJPLXJ7j1_SvNKHs21ZhuJF64Ta0f-Wm-YvHWbv3affDgnxcRr0KnZL82Ox00DWJpYUmOub93KU6G8YsPwX28CdjIZCdsgqk32S2sf4GPHuJmwrFaf7kEGEXvoLM_ymjLA0JQVcQZBcSwWzYfOoCdvcZGG-g4gi4fhj1nozdmmmduVMxMMe0RVS62XOJ2bY7qTsVYd5MES9K4Ksb6zbq2qmjprN4CC0BeNXf2-AgdSCicHmsglbguttYGdpfbO9r9yxOtxmLPYpTHxgOBCIekxtEX6j1amX878tVWlJY_CVq-PcnGquFvqvv67hnu67qh_zm24NC3uOQDp8VlxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf26ef809.mp4?token=XK8qJPLXJ7j1_SvNKHs21ZhuJF64Ta0f-Wm-YvHWbv3affDgnxcRr0KnZL82Ox00DWJpYUmOub93KU6G8YsPwX28CdjIZCdsgqk32S2sf4GPHuJmwrFaf7kEGEXvoLM_ymjLA0JQVcQZBcSwWzYfOoCdvcZGG-g4gi4fhj1nozdmmmduVMxMMe0RVS62XOJ2bY7qTsVYd5MES9K4Ksb6zbq2qmjprN4CC0BeNXf2-AgdSCicHmsglbguttYGdpfbO9r9yxOtxmLPYpTHxgOBCIekxtEX6j1amX878tVWlJY_CVq-PcnGquFvqvv67hnu67qh_zm24NC3uOQDp8VlxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🚀
🇷🇺
امروز صبح پهپادهای اوکراینی به یکی از اصلی‌ترین مراکز انبار، دسته‌بندی و توزیع کالای Wildberries حمله و اينجوری داغونش کردن:
این فروشگاه اینترنتی که به آمازون روسیه معروفه،‌ سال پیش حدود 75 میلیارد دلار کالا از طریق این پلتفرم معامله شد...
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70151" target="_blank">📅 20:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70149">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63850d9e4e.mp4?token=lyurKovoRkWHiQ9aNTpWfvIRRz22ugBNUEI_jfIyo5HhADKOOjWpVGwAgqSfB4vhyGqhfjJ_Ch0gGvRVzDftq7CPIWTtSPNM1pG48Ax-d4mdFDbcYIrVrjJk6omvAmi5k84ET73wUtme1YRUPmhMhd6UP8eEEzC1TuyDDM49HJHipiecqtI0928a7UtiMmcfIcuIvTyyFFIexYpA64IvxvB0VILGjTTYY4IfdLtlkBl3-YABjqv1cf-ZunXzT3y5xxmLJ45lxegGxOat_BMcVYcvbqD6fvA9aorlpP9ulgn1-QsrRQMPDQPEqBePemSS7fc1KveLRfQh34Ctcy-5n2GxQIM_0hhsjfyy3ZpZEsxEMmX1haYTAcGeorXQgGP8Ot2ZDv2lUV977GnOVz6RT66VIu5pXT_fNZqG4LYNeqVVwzZw4kdgD6ihhbNkhpnqppsYl5MPByvY6PnIqRWmXRormoCDoghn3ssQJDyqPJBvwgBFMP2sSO57zXkSoD-yyoJD37syNthCF14aYzteMejyLqyNCSaj1NdLWGqye5jlOnFbOSmmjF655nfia_10m3VDdJOG2eauLzkMOFaTvaWNBlozp5v4XnIPhVS76gPeq_YwruDVBu60-9VaRm5OgH7ghsrPFhTRdKgBN2tMeyib3yxDfkBaAE5yUwYu8Ro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63850d9e4e.mp4?token=lyurKovoRkWHiQ9aNTpWfvIRRz22ugBNUEI_jfIyo5HhADKOOjWpVGwAgqSfB4vhyGqhfjJ_Ch0gGvRVzDftq7CPIWTtSPNM1pG48Ax-d4mdFDbcYIrVrjJk6omvAmi5k84ET73wUtme1YRUPmhMhd6UP8eEEzC1TuyDDM49HJHipiecqtI0928a7UtiMmcfIcuIvTyyFFIexYpA64IvxvB0VILGjTTYY4IfdLtlkBl3-YABjqv1cf-ZunXzT3y5xxmLJ45lxegGxOat_BMcVYcvbqD6fvA9aorlpP9ulgn1-QsrRQMPDQPEqBePemSS7fc1KveLRfQh34Ctcy-5n2GxQIM_0hhsjfyy3ZpZEsxEMmX1haYTAcGeorXQgGP8Ot2ZDv2lUV977GnOVz6RT66VIu5pXT_fNZqG4LYNeqVVwzZw4kdgD6ihhbNkhpnqppsYl5MPByvY6PnIqRWmXRormoCDoghn3ssQJDyqPJBvwgBFMP2sSO57zXkSoD-yyoJD37syNthCF14aYzteMejyLqyNCSaj1NdLWGqye5jlOnFbOSmmjF655nfia_10m3VDdJOG2eauLzkMOFaTvaWNBlozp5v4XnIPhVS76gPeq_YwruDVBu60-9VaRm5OgH7ghsrPFhTRdKgBN2tMeyib3yxDfkBaAE5yUwYu8Ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت این‌ روزهای جاده چالوس:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70149" target="_blank">📅 19:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70148">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b0bac1f2.mp4?token=H59s6MPvRTb0mletiMo9lQA10z8esOn0epmvKZ6MPAd03Rt-sbNlJHIyaiI4bDrKa-Sq-Lg1yLl7voDT9tj79X63Gw4ixOLerzuSmi-4xeR5PXnES9URPJwgubgQ5P7cwUjuutt2amcItHM8xveq0973CAhtAMAmfMuDK4L7K_yC572WEhSOzt_If9wvn1LYDNVB4AJIYf2eizSmppQXZhoKhNK_ST6BjLdND2MUPgt6AWju_vJYcaB_nRUmeEC8iemQQDXfjP6jJE5jfxTyGUI9g3M86V6KTAW2pit6C4qGjWo8V6Llz-GZsyOdYCa-glpetbMY_nBL2u8BTYGbUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b0bac1f2.mp4?token=H59s6MPvRTb0mletiMo9lQA10z8esOn0epmvKZ6MPAd03Rt-sbNlJHIyaiI4bDrKa-Sq-Lg1yLl7voDT9tj79X63Gw4ixOLerzuSmi-4xeR5PXnES9URPJwgubgQ5P7cwUjuutt2amcItHM8xveq0973CAhtAMAmfMuDK4L7K_yC572WEhSOzt_If9wvn1LYDNVB4AJIYf2eizSmppQXZhoKhNK_ST6BjLdND2MUPgt6AWju_vJYcaB_nRUmeEC8iemQQDXfjP6jJE5jfxTyGUI9g3M86V6KTAW2pit6C4qGjWo8V6Llz-GZsyOdYCa-glpetbMY_nBL2u8BTYGbUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محمدرضا نقدی، مسئول ارشد سپاه پاسداران:
پیروزی کافی نیست. ایران به دنبال انتقام برای خامنه‌ای است و به بسیج دستور داده شده است تا فعالیت‌های خود را در خارج از کشور گسترش دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70148" target="_blank">📅 19:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f0e41933.mp4?token=IpJke78a7KBf1cYQKMq5LShoaQ4MgMNTJMcXduOR5leTBFk019AmN3KkpX9jyHvnQvSkpF1rPK5bePJQvRaiRRHIapnXA3YfDuEJ-acYA-hapJB6UDSO_tckZOKLhQK000nEzbl-UD3ttY2ekCfA2L4SwHCNLGhoRheKukAnsznMIqiQdSpFeSqihx90j5JCTofPvbEWaOZV9QzBT_R-U4IAjZ7hH1Cfgmi6YnSScipW-VtQWT4JVTA83YC-0ltbYj4Peacw33rPFF6cjE_ZV1R6HCkKOxx0qhFhRijqbrjmPUDIYqCpwphypUq_OEtwrXG96V3x6w8-TEcHeeO4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f0e41933.mp4?token=IpJke78a7KBf1cYQKMq5LShoaQ4MgMNTJMcXduOR5leTBFk019AmN3KkpX9jyHvnQvSkpF1rPK5bePJQvRaiRRHIapnXA3YfDuEJ-acYA-hapJB6UDSO_tckZOKLhQK000nEzbl-UD3ttY2ekCfA2L4SwHCNLGhoRheKukAnsznMIqiQdSpFeSqihx90j5JCTofPvbEWaOZV9QzBT_R-U4IAjZ7hH1Cfgmi6YnSScipW-VtQWT4JVTA83YC-0ltbYj4Peacw33rPFF6cjE_ZV1R6HCkKOxx0qhFhRijqbrjmPUDIYqCpwphypUq_OEtwrXG96V3x6w8-TEcHeeO4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیمان طالبی مجری صداوسیما:
نمیشود بنزین قیمتش جهانی باشد و حقوق ما ایرانی.
حقوق مارو جهانی کنید و ماشین ها رو با قیمت جهانی بدید، اونوقت بنزین هم با قیمت جهانی حساب کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70147" target="_blank">📅 18:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsVI4d0CdM7T6vxAOVZBbWWZ5OtROam1DWgNHIkIc9NQqe1pd-OTCyGWtKqvEOEODjIVzUCeMGAT2yuSRDQBvOygE0HR5McTTIzsut3XQJUYN209A228lQ2ZJoljyS1UjwL5Kg4lPrkD1vYJuSjxk1dKGVhWAt_H16qxZ6jrcze3fcZn08rGoyUFIO4EV3Bkl0BF-pbzQ8rL8W8q0af71MgIZevhEFLdNqKWIS5Yi4OVZuwalk_ACtB0w9zm-J0LI9WCTy5q8WDN0YWsl_-JQEBPTnAv-1EoVnfF82oHMriY5iXTtkC13mB6YP1CYrtFsJKqeaxx4_-g4Tpu45CSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در ۷۲ ساعت گذشته سه کشتی در تنگه هرمز مورد حمله قرار گرفتند؛
طبق آخرین اطلاعیه مرکز اطلاعات دریایی مشترک (JMIC)، از زمان گزارش قبلی آن در ۷۲ ساعت پیش، سه کشتی هنگام عبور از تنگه هرمز مورد اصابت قرار گرفته‌اند.
دو فروند از آنها در آب‌های سرزمینی عمان در حال حرکت بودند، در حالی که فروند سوم در مکانی نامعلوم هنگام حرکت به سمت تنگه مورد اصابت قرار گرفت.
هیچ آسیبی گزارش نشده است و هر سه کشتی به سفر خود ادامه داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70146" target="_blank">📅 18:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70145">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70145" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70144">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvpIJ-0f0aK5a2Tg4Med5btWcjS52384dtIvu2NogbmzKx5krUCir9zvAzCRREEgK7eDXwkeBKqlz6vRT7IIGJ5h8jbtQC2bg1pluh_qPUcLQjl-3_OmhT3zPVP05a4vJsHvtQXXuuKFEXUQQ4GE5VU4DngTtGJxQ2r-li5LGkFkCUc2HRA3dxjWDkswcS0X4oxzEPEFrTzR1bMVFDhLVfPTpfHig_z_jYZ4ILJCYqlHPcCm7MrN-7x99EDZHgNDDj5fAJugU3jccGxPgtusDcLlkhG1ShuzkK89ZaJFCDWxBC7itzQHjEtA2POkc24wzVTyBX16GCYuJGv58F_2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g25
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70144" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70143">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f965699a0.mp4?token=ui-4n45RFWuiR6bK6GSV_Q1dk0gBk5vkeTAR4dUSfYfbuHXrO91H5FjIUhRY6wHZI0Wyp4fNaBrNaEzvwandAPS7yB9EVnZIDpaSz1GFs3CWupcR-R_F__BUgFVSJXr1Z4cY-u30mKwmkWFWEFdlR2t7gdxqdVcyfOSiRZQftCfylK2Lnd0jxQd9AJiZY_XZcuPjAKLRCMN49T6P1S_34ceM4Ak6fDAPZS1Pclhu_H-KnBoXwmj5s14zd4EoPGDaWt6hi6Nr9PTSw96SfWz8QAt-_kFDQjn4zxpFA1JNvtzNEHPz5zbeVSOT3y08GBvcnfzMWWvCXQqISxiuYZy4qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f965699a0.mp4?token=ui-4n45RFWuiR6bK6GSV_Q1dk0gBk5vkeTAR4dUSfYfbuHXrO91H5FjIUhRY6wHZI0Wyp4fNaBrNaEzvwandAPS7yB9EVnZIDpaSz1GFs3CWupcR-R_F__BUgFVSJXr1Z4cY-u30mKwmkWFWEFdlR2t7gdxqdVcyfOSiRZQftCfylK2Lnd0jxQd9AJiZY_XZcuPjAKLRCMN49T6P1S_34ceM4Ak6fDAPZS1Pclhu_H-KnBoXwmj5s14zd4EoPGDaWt6hi6Nr9PTSw96SfWz8QAt-_kFDQjn4zxpFA1JNvtzNEHPz5zbeVSOT3y08GBvcnfzMWWvCXQqISxiuYZy4qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: از سال ۶۴ درگیر مباحث لبنان هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70143" target="_blank">📅 18:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70142">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa40fcbf2.mp4?token=hzN36YJH4x13vNHMDGaqj4VcP4WeXY0RlsxAaUnuaS6DiJWk_CuNB2UWJJLpviikKuvTeh25ujKxsQotxPDw9gxWDhys8ZS-ugI7BS9hrSebQDaAA4_wOO_6SZNF3_WuKHqGNX5GL9uAx3MCvC6iAAicOtSIUaNO9vt1L9DfVgEDd8gsgsilaEhfuHRdpG_F8qz7pV7H4haWAxSdecyjPNBHk8C8GIw2h-sX0NardT2wfh5q8wm5VYH_AAnaKLm7S9HUUM1ulAW0gNDybh7FdoBCBfgDVf7g_0cS5ENgLWNSBcsrOTbP43iY4DwsGQyicrBUXbHfP1GWJPW6Q1NyHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa40fcbf2.mp4?token=hzN36YJH4x13vNHMDGaqj4VcP4WeXY0RlsxAaUnuaS6DiJWk_CuNB2UWJJLpviikKuvTeh25ujKxsQotxPDw9gxWDhys8ZS-ugI7BS9hrSebQDaAA4_wOO_6SZNF3_WuKHqGNX5GL9uAx3MCvC6iAAicOtSIUaNO9vt1L9DfVgEDd8gsgsilaEhfuHRdpG_F8qz7pV7H4haWAxSdecyjPNBHk8C8GIw2h-sX0NardT2wfh5q8wm5VYH_AAnaKLm7S9HUUM1ulAW0gNDybh7FdoBCBfgDVf7g_0cS5ENgLWNSBcsrOTbP43iY4DwsGQyicrBUXbHfP1GWJPW6Q1NyHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مجری صداوسیما:
تاکنون ۸۱میلیون تومان پاداش برای قاتل ترامپ جمع کردیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70142" target="_blank">📅 17:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1YVBSX2YBJxInA-_tvGOMiOs0JXJ1eyok9sP7OpnYpteg1pd3l5Fx1MpSl80FdkzwNQB2C4K93NTs00kYiBsB-Q0lM9Ewoy0wKbtoeC5EWx3Z1svAXetxjcz3y9qjrF4nANB89tfTGPpFS-6VJJsElqA8K_Pj2xf7rFInys50MyYiHvbgaCyJyjTFr0ux7NP1M_rccbxzrqMVAp5LaK-FMhrbXnBWWjTuQEN0eXalfZwaB0BSJgjSYvo7PVCEzff5Q30xwrNJGDMmjp7ulCjql8j_4PRLUjMWRTH_Mk1X8onMxrGvzYh4mTDlHm3pTb_Z7Ur7SMRs7s8wrvz7DOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:دولت ترامپ در اواسط ماه مه، از «نیچروان بارزانی»، رئیس اقلیم کردستان عراق، به عنوان کانال ارتباطی محرمانه و غیررسمی برای گفتگو مستقیم با رهبری سپاه پاسداران انقلاب اسلامی استفاده کرد. مقامات آمریکایی پس از تردید در مورد اینکه آیا مذاکره‌کنندگان رسمی ایران — یعنی محمدباقر قالیباف، رئیس مجلس، و عباس عراقچی، وزیر امور خارجه — اختیار نهایی کردن توافق دیپلماتیک برای پایان دادن به جنگ را دارند یا خیر، این تماس را برقرار کردند.
در حدود ۱۰ مه، «تولسی گابارد»، مدیر اطلاعات ملی، با تأیید صریح رئیس‌جمهور ترامپ و معاونش «ونس»، با بارزانی تماس گرفت. او به دنبال ایجاد خط ارتباطی مستقیم با سردار احمد وحیدی، فرمانده سپاه، بود تا بررسی کند که آیا رهبری نظامی با مذاکره‌کنندگان سیاسی هم‌سو است یا مطالبات جداگانه‌ای دارد. بارزانی که به زبان فارسی مسلط است و پیوندهای عمیقی با تهران دارد، در ۱۴ مه امکان برقراری تماسی امن را از طریق تلفنی رمزگذاری‌شده فراهم کرد؛ تلفنی که توسط یکی از مقامات سپاه به دفتر او در اربیل آورده شده بود.
سردار وحیدی هم‌سویی کامل خود را با تیم دیپلماتیک ایران تأیید کرد و اظهار داشت که سپاه ترجیح می‌دهد بحران از طریق مذاکره حل‌وفصل شود. در پی آن، آمریکا پیشنهاد مذاکرات محرمانه و رودررو در اربیل را مطرح کرد. با این حال، مقامات ایرانی به دلیل نگرانی‌های شدید امنیتی در مورد احتمال ترور توسط عوامل اطلاعاتی اسرائیل که در کردستان عراق فعال هستند، از پذیرش این پیشنهاد خودداری کردند.
بستر ژئوپلیتیک نشان می‌دهد که ترور علی خامنه‌ای، رهبر عالی ایران، و درگیری‌های ۴۰ روزه پس از آن، ساختار رهبری ایران را به شدت دگرگون کرد و موجب تحکیم تسلط سپاه پاسداران بر امنیت ملی و سیاست خارجی کشور شد. اگرچه از طریق این کانال ارتباطی غیررسمی، تفاهم‌نامه‌ای اولیه میان آمریکا و ایران حاصل شد، اما این توافق به سرعت از هم پاشید. تلاش‌های میانجی‌گرانه موازی از سوی پاکستان و قطر نیز کاملاً متوقف مانده است؛ چرا که به گفته مشاوران آمریکایی، مانع اصلی همچنان سیاست سرسختانه ایران در قبال تنگه [هرمز] است، نه عملکرد میانجی.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70141" target="_blank">📅 16:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo8d-J2MS_EUECxtKCO2ZB_Cbwh7KbvK7ds9WkGwK_4q02LSd9-rVeMTOAWiLySDMYOeAcjychuvPda7iX10exhgTx9djXv6ITpkS6ADZekX6mUBKTE--0vNCmQ-RYkGZ4pwyNKuuV0f1_Zr1tAvstvXu3hBBtIUFuPzGKEL8pQMg9vazhfFUU95cs9CZOVoiLsYNRM_5QXYnxnQOQ83CHmIKS5LvgBJUZXpAsnZu2CWUKlOM1MWM23LbGie_-XaG_vBQtoeTuZl3YxjI_oeAQFJ9p0S-iHSuLBS82SGLDgX9oswB8cgO4LDPo5GZCihhOSFFIGGeU61pdcHd4qsdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
کانال 14 اسرائیل:
🔴
ثانیه ها به شمارش در‌آمده‌اند:
تنها ۲۴ ساعت تا پایان مهلت اولیه ۶۰ روزه صلح/مذاکره بین ایران و آمریکا از تفاهم‌نامه ژوئن باقی مانده است.
توافق موقت متزلزل بوده است - موارد نقض، تنش‌ها، و هر دو طرف قبلاً آن را لغو یا به حالت تعلیق درآورده‌اند. هیچ تمدیدی تأیید نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70140" target="_blank">📅 16:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1685ca6213.mp4?token=V-K0aaeuT2S7NZU98PMsR-X2ck2CNsG4BFxENj2sOurkDmEtWf1gdkNhlL6-RkGVmlVh06i0_jljD3OiKztMlQHzL6MEPZpD5XcwoEjfNpuP_AXrmUPGQ8ukYALyx85k39nGoGsj8_WnXosVBE5r9rZTv6Ct5LD9VKC9VV6Dm7R51iEO_f5fEK_ZZ4jNr-JBLx_S8KBjMzt3stPPaHM5rOAAKch7WDbBbXV8lLEre5GRUZAB8z7bsV8TSSjfZ3w5HBdcLF3RqMtHCLPtSs3l99AkDRyPMErhPhZnpaM0RThVJLcMd1P_MmzyDJZpoH1Wkul05UZXpEq45xsHZo6XzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1685ca6213.mp4?token=V-K0aaeuT2S7NZU98PMsR-X2ck2CNsG4BFxENj2sOurkDmEtWf1gdkNhlL6-RkGVmlVh06i0_jljD3OiKztMlQHzL6MEPZpD5XcwoEjfNpuP_AXrmUPGQ8ukYALyx85k39nGoGsj8_WnXosVBE5r9rZTv6Ct5LD9VKC9VV6Dm7R51iEO_f5fEK_ZZ4jNr-JBLx_S8KBjMzt3stPPaHM5rOAAKch7WDbBbXV8lLEre5GRUZAB8z7bsV8TSSjfZ3w5HBdcLF3RqMtHCLPtSs3l99AkDRyPMErhPhZnpaM0RThVJLcMd1P_MmzyDJZpoH1Wkul05UZXpEq45xsHZo6XzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیف شاهنشاه آریامهر و ترامپ از خمینی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70139" target="_blank">📅 15:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f147bdc.mp4?token=uUg4DdNI5zJ0okBN54A3Z5PhL23bak3g6T8ElK40FmpF8DJcgtvd3AedmF25ScuoW14Srxq147cJGU95Dn-j3OUmOxSdFjE88Q5gKVeAv_p8doLYLh8FQpDcyT4CBcu0uLGsJjAmP-qtiYGSCeeAnVkaherMG4n0OMzbNXySBpw_IXjrJpdWUnVC9v0cShIk2AqKAFjh_qn4A5kbySTTt1kCMA9-v2AU8dsNhnTXneH3oVdAQknGybYj9HTqfzEcSRyUlch6Bm0-YRdZT7LF1Toct-roMiLSymBzPZ-gRid6Y1NFVxb89tsVJknPLaJCfDkX1QPShVKpw3bvQXpvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f147bdc.mp4?token=uUg4DdNI5zJ0okBN54A3Z5PhL23bak3g6T8ElK40FmpF8DJcgtvd3AedmF25ScuoW14Srxq147cJGU95Dn-j3OUmOxSdFjE88Q5gKVeAv_p8doLYLh8FQpDcyT4CBcu0uLGsJjAmP-qtiYGSCeeAnVkaherMG4n0OMzbNXySBpw_IXjrJpdWUnVC9v0cShIk2AqKAFjh_qn4A5kbySTTt1kCMA9-v2AU8dsNhnTXneH3oVdAQknGybYj9HTqfzEcSRyUlch6Bm0-YRdZT7LF1Toct-roMiLSymBzPZ-gRid6Y1NFVxb89tsVJknPLaJCfDkX1QPShVKpw3bvQXpvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مایکل مترینکو و کاترین کوب، گروگان‌های سفارت آمریکا در تهران، درباره معصومه ابتکار از اعضای دانشجویان پیرو خط امام:
یک عوضی تمام‌عیار بود؛
هنگام تعارف شیرینی می‌گفت مرگ بر آمریکا.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70138" target="_blank">📅 15:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70137">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig6TgX7tcU12LtNTU4zCKHWHn2NyjAOa9Ybskd-VbeoWrvnUFhw6omFvNTQHyftBJFgs7JOKuLNw3r1pV3DRIU0LAPJ2LXbA9kIOaKPP4yeFa3MWQnlPe5QzkW5oKBsPaodYAAYcB56egTIo88uIDqfq7cX9AsYeCP6D_tMEKFvMMnOL_2UDkl0X7r4LLVpRm787Y-di3AcQkS-4B9l0OnQDkJN1-ej-prFxFWrX8eIoSw8h4bHkpu6EkNHfwKSs_qxU4YsQdUh8XVHg2XhP4Q338iITXI1Uw8s_U-8OssJz4jYXBCXn-dQaQ0qCa1R-aRzxkql-AAQPLnaDsswhYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سند ازدواج کریس رونالدو و جورجینا:
در صورت جدایی و طلاق ، جورجینا ماهانه "100 هزار یورو" تا آخر عمر دریافت می‌کنه و مالکیت خونشون تو مادرید، به ارزش تقریبی "6 میلیون یورو" هم به جورجینا واگذار میشه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70137" target="_blank">📅 14:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70133">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HWjv0D0zqEzd2uwG0-edw9lcvKS9P0Dic_R6ILSP4etKS82lnjMF-eN_ObDDuCAwWme-3PkDBHFexwQRgRQimHMl3101UeeO-YMuPbfdhd1x17RJypRdqamDAK-C_BFwbcQgTM-siK3sp1EM0Zm-huM_6rqnl1Wi96MPhm7aVZPNHCuDN-uVIHdqaBiIa0LEizacNm0aJ8fTIgBfMvPKv4gCezMr5pWwYDw4qKIOtbaZcoDlt2gUcuXYFQ5iZRXTBRCgWy_b1kvuiqagmNaR3CkY-cPUJnTj3pzCZhGYpov4SPLGO1OB6gnN7nO3zSt5ExUzJUNS5ZJcZ9SdyTd6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKual8wEzfIytzGp6Tz2EOA6dNA5zYNrux5h6Zb6ZSdy_gMhKuBE8VkgG2togFMWf_5OxZbypm88Y_U0zitz3AiHiJJAN2UquPWjluuB9OyAqXMCxmzfpZAYP65_sbppyovPmzUa8JGLGABPTmimwChcDHpXP9lCkaB-ZN38LfSx7lKwj_VgJWqmxhQN8KG2C8XiPp-DW3_MREpQkvmsUI0uw9d28Dq8rW_IkG8ND7xaHws-SJUhRM4Nx9pBT_WiqKImucI-a1j-o_mFKQv5fKeG-tVH9XwwlIdgZzdA79xObUzIaEUVB_UKBhLTPauYRDUSHTRWfeAysogspDJPXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b276eb7f.mp4?token=k_2uAU9yTjhSmOx5O0xfWP0PQEmk2J1jvMzgzliUOKNDGKDdclGcKlQ83MbEEZl4dn86hNFFWIi2IXjrkT0jGgSET0nN23373zLnACxRk86XLyzQJjq-4KWqc8gzf7BeTkpm3O3dpPRS5zY1cdxGmj3ztzqBKWDTnJYXHso4Pvt0Mp9o5JeBop_tgiE3e8Kzipwe7ax2G354TM-tSt2gxThaFl49jgWvxqiwwVGmyES9sNSbCYvvY2VTCiaT30OgVT2ns3GgUNFfe5H9a3asCrz7af1qewykx1YGbgNoap23j5kVRlbTJUwQx-uR8UA52tIk-V_ORaTyRYHQOmZtEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b276eb7f.mp4?token=k_2uAU9yTjhSmOx5O0xfWP0PQEmk2J1jvMzgzliUOKNDGKDdclGcKlQ83MbEEZl4dn86hNFFWIi2IXjrkT0jGgSET0nN23373zLnACxRk86XLyzQJjq-4KWqc8gzf7BeTkpm3O3dpPRS5zY1cdxGmj3ztzqBKWDTnJYXHso4Pvt0Mp9o5JeBop_tgiE3e8Kzipwe7ax2G354TM-tSt2gxThaFl49jgWvxqiwwVGmyES9sNSbCYvvY2VTCiaT30OgVT2ns3GgUNFfe5H9a3asCrz7af1qewykx1YGbgNoap23j5kVRlbTJUwQx-uR8UA52tIk-V_ORaTyRYHQOmZtEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇨🇳
اختراع جدید چین؛پدافند پشه‌کش:
این دستگاهِ قابل حمل، با استفاده از هوش مصنوعی پشه‌های درحال پرواز رو تشخیص میده و با لیزر نابود می‌کنه.
قدرتش هم خیلی زیاده و می‌تونه تا 30 پشه رو تو هر ثانیه بکُشه و تا 6 متر هم پوشش میده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70133" target="_blank">📅 13:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70132">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8ff4c5f43.mp4?token=RuduVCxs5TyvKs6gCpPeUQ8ASnP-vSOXknf4AXMZjQEKwyvvzp8DBrdIDvsxpR7NCXdPDFDflvm1Tm3FRFMfuxkzbH9tV-toy4D7nyVZcn7VkJeiXfdZ07gixlkQ6IhKmEucAUeFKy5pnXzpJhmsr4OpLJkp-Tfqy4kq6eIXMkHU327KpofwenERJu0BCJaSd9XueLKk8zb6xp8YT9ssvkEr0nssVetyfxAJt2o-ZYWVZm42cejxn0Y7lXtpRmhsXh8y4oz0GhwIGR2mP1sTrHfiUlxkY9OGnuHAYofv3tDmeNdUwgqpBEQerBuXJTAei4WnUikXpmXA3zb5IM7P7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8ff4c5f43.mp4?token=RuduVCxs5TyvKs6gCpPeUQ8ASnP-vSOXknf4AXMZjQEKwyvvzp8DBrdIDvsxpR7NCXdPDFDflvm1Tm3FRFMfuxkzbH9tV-toy4D7nyVZcn7VkJeiXfdZ07gixlkQ6IhKmEucAUeFKy5pnXzpJhmsr4OpLJkp-Tfqy4kq6eIXMkHU327KpofwenERJu0BCJaSd9XueLKk8zb6xp8YT9ssvkEr0nssVetyfxAJt2o-ZYWVZm42cejxn0Y7lXtpRmhsXh8y4oz0GhwIGR2mP1sTrHfiUlxkY9OGnuHAYofv3tDmeNdUwgqpBEQerBuXJTAei4WnUikXpmXA3zb5IM7P7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
صحنه‌هایی بر فراز منطقه مسکو در روسیه، پس از حملات پهپادی اوکراین به کولدینو و دوموددوو.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70132" target="_blank">📅 13:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70131">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
چهلم بعد از ۵ ماه؟
در روزهای ۲۷، ۲۸ و ۲۹مرداد  مراسم چهلم علی خامنه‌ای برگزار خواهد شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70131" target="_blank">📅 12:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70130">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e871b80a60.mp4?token=Ez_Y5-PiL4YO4xLGt2eJW_-X91fh6V3fz0B4FRFYJ7FAgmghC9GyqRHr9uHOQNc6xrxSj37LC4CE7Rl4ijU_hMS70rymZAZtvPlTWUJrD0sG5ek8EtdpP_IPsDOHz5j7j0oZHpmrlL-fr9Tfe-R1Yu7KhEYCWQB2D_7rWh7Jr7pbZAg40i-gT2EzGz1sBZY2129JiwLkd7u3nfp8WQLceeqPhy1mObGvMVvZdDXMmUUP8YjCfGjSmvOKKG7NLCokNevyh7eayQL8Tp6jMKO14esIEIhpKAiAJcf38v3piXcrdFj84bZ144YExJW7Pw7XeW7WQzx72IkdZ5L3AgKCIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e871b80a60.mp4?token=Ez_Y5-PiL4YO4xLGt2eJW_-X91fh6V3fz0B4FRFYJ7FAgmghC9GyqRHr9uHOQNc6xrxSj37LC4CE7Rl4ijU_hMS70rymZAZtvPlTWUJrD0sG5ek8EtdpP_IPsDOHz5j7j0oZHpmrlL-fr9Tfe-R1Yu7KhEYCWQB2D_7rWh7Jr7pbZAg40i-gT2EzGz1sBZY2129JiwLkd7u3nfp8WQLceeqPhy1mObGvMVvZdDXMmUUP8YjCfGjSmvOKKG7NLCokNevyh7eayQL8Tp6jMKO14esIEIhpKAiAJcf38v3piXcrdFj84bZ144YExJW7Pw7XeW7WQzx72IkdZ5L3AgKCIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به یه خانم گفتن معیارات برای همسر آینده‌ات و مشخصات خودتو بنویس؛
نتیجه نهایی عجیب و جالب بود!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70130" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70129">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70129" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70129" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70128">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lutjdHz2C81eXHEn_SsNClDOy6hGcTm7zLX0f_nKp2TOgV7VNv2UW3ZAzeS946YOgv84bODTGjKA8d3WTuXUwgp4F2LSiGZkXK1BeNg_kWstn-9hpTfsg7ZULwSSHz-mOlk_EEZLZfu8mWNrHSGrAVcnNZWEhQNaAbE9ogdp0utLDrXaiQ0ZeNbpKvEuZ4mFTMhyCM85wExQoxc4AjOxz_IGiN14vPZ26WLNUi0BtDSAZEkPyrSqUckq-a9qjmpx7X-K8oA-K3uf4SAdKDyWS6c_-pjQudiEPy5Z26hSbVwd7inqs_cUFgCJN8JmHA_xqTnWsBtoHfMcagiZWYUEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r25
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70128" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70126">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a53c7e6e.mp4?token=mM0ZxJep7ao2vu5WArGYIAibU5WPXQl8Nty1yW183QxgtUj_F7BiJeGfJXyKMlOFvY8BSiXtMkiPEpNnxp5hLZwR_p4wcybHvFk4yx0uDRCCfsd2DfNlTQ3O9VgzUfkxDyi7Ydsz_JqnflJWEU0mv4wSVBp-BVa4MvDOGgWniQTYANImlAI-kGmmxofnHYLzi66beqL6G4k1TRjbJgBsMQK1ILD_cJObRdHUPux8NTli32fb8uhxJSAzIK6Tp2Ou_fv1tWX8Juz89HOSOzSs3xo_2CH5wkLm_1GvpXkuqTaoC2SQpTJAiiQOT_iTEeyMZWmJ8oxzJ3RxsMo4NzTV2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a53c7e6e.mp4?token=mM0ZxJep7ao2vu5WArGYIAibU5WPXQl8Nty1yW183QxgtUj_F7BiJeGfJXyKMlOFvY8BSiXtMkiPEpNnxp5hLZwR_p4wcybHvFk4yx0uDRCCfsd2DfNlTQ3O9VgzUfkxDyi7Ydsz_JqnflJWEU0mv4wSVBp-BVa4MvDOGgWniQTYANImlAI-kGmmxofnHYLzi66beqL6G4k1TRjbJgBsMQK1ILD_cJObRdHUPux8NTli32fb8uhxJSAzIK6Tp2Ou_fv1tWX8Juz89HOSOzSs3xo_2CH5wkLm_1GvpXkuqTaoC2SQpTJAiiQOT_iTEeyMZWmJ8oxzJ3RxsMo4NzTV2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
شاید براتون جالب باشه؛ کلیپ سمت چپی برای یه پسرایرانیه که بعد از سال‌ها تلاش، این حرکتو زد.
اما کلیپ سمت راستی یه نفر اومده با هوش مصنوعی همین پسره رو تبدیل به دختر کرده و گذاشته تو پیجش و حالا میلیونی بازدید گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70126" target="_blank">📅 12:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70122">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkKgBFlgrp9Tm025jadSCqv2AhbN8w6_kYTrJvq0y8wLnrAq1p1ucinWiaaybF5FNw2EwL8BWRk3b7tCQI6X_JM2xPaJmNEf6aNrOYwhoQD_NNPG-6OtqyzVjsALsxtJh6pNQWjDZLhyI8pKqyVYMB8GlQgrRLCny7lXlpRAwfzAcm_xapElQf_YMkr8JCirAqnSUbAf4F7yqQEDrU31K6gxgFoLV9tZucNnZM8ZtQKE7UJ2fMMBfol7BfqQAkd8lhMnaQ0fGst65Imnf0tYDCMDnezCgSKnRs6DQOvtAZ1BGzcrlmfhV6lKSeukM9vV89vLXfLeqHWcD9NIyzqEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoxoIbjjnSfElWZ_PwYti-2JCIcP8gCdYCZYlKYq4l_q8DsqO8-e-H5_aY2aQOfVXMzcGCqAglNtQqutgtUhiimLM6rM1Us7_GHi1P7dmOputnfbkkKRnuDnhB685BLniyXL957McWh08K7vz0zDXUsOC0ZtzvZxqgCS3ZkEUNo3N8N__OMeiufVAny-D43xN8a1AIuNpQ2GonPOsWsbgzh6THDqX5KRmnUV9kUoKTGNwysh3TOPcSi8A1YCcMQEnATEMba2TjeIU_LhNJp_aODASi3gbbVKl5Q7mocok4uZM-fe7CgNkH9-I0mi1nGh4iqNVLvK4bcQGYaPUjriCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JmelqkCizwQBvILtTvVfL-rhIvH-q7WxfdKYN157a_t8WXb6RsnxvMoCR-nHI6n03kqI9k7aOOhcCihjw1-x9mZ7PrFyHTQL9RSv_PYBNLkrvhc389THT6wHbzcYUgM8zH0rkJxfGkAgIrtgSGf7xIvhWAiGf1mlWYW8vH6pekHDvPKNyon_JuPlJSv941r6sdEzpxB5kh0dRec_GAKL50biCQtfGZNO2yfpbhFy9-EUiv7f4du9uNieQtKgt5VZgwu7AIpt33hZNlFvmXr_51NMc2T0TvrShUB1rJurLOWZVVK2HxvfOlke7796La8N0bdZcN3LynPKhnWViHUdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvO3VDIxH2HhUceUns8BvbH5Qa-3CbVRgptD1RDihQfZmHg66ISU7zQEtRykbchjGjutoC-9l_ZDDlY1Eu6Aww2J6mNplNwMUG720j36_RTmsky_59gAyJ-rDM786xDLJx2E3Jv-lxk7Ch7ufRAGLSciJ04S2z1kKtfO1SBD52L2HJz3-8KWBrcrCUpdGIyOjfvtlXgWcNvfLD4KzV7V0AAx956-CwG7SkcLThKHkPRlBX0PST_daJXycuAwITJ6Xe86PzfqSU9rr1Z2aAgso6rdPDGeDW2IcuS79WqFTqJ_kS07BB7xonOVFWm1byMkE7cFsIb-hwJwShWjabEsiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👀
رامین رضاییان رفته دایرکت یه خانم دو رگه ایرانی-امریکایی به اسم «جول فرشاد» که بازیگر سریال ایفوریا هم هست و ازش درخواست نود و ...کرده.
خود بانو "جول فرشاد" هم با استوریایی که گذاشتن این موضوع رو تایید کردن:
بله میخواهم تایید کنم که این شایعات درست هستن. به زودی جزئیات این ماجرا رو با شما در میون میذارم.
اون (رامین رضاییان) جلوی دوربین گریه میکرد و از مردم ایران طلب بخشش میکرد ولی تو دایرکت از من درخواست هایی با موضوع خصوصی و نامناسب داشت.
خطاب به رامین رضاییان: میتونی منو بلاک کنی ، عکس پروفایلت رو عوض کنی  و هر روز سعی کنی اکانت هام رو هک کنی اما نمیتونی حمایت ملتی رو بدست بیاری که مدام بهش دروغ میگی و بهش پشت میکنی.
‌
‌
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70122" target="_blank">📅 11:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70121">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad5ddb268.mp4?token=nbTRf8MdsLRKD-6YtVY8yVQ4JXKAQ-tI8etWmbuU7MW9Ui4faE-Emt5idCC4oj0ZElFBdDSdwGh5r7dd-AdPMxJoJrusG4NVNfaOO862tuXYOfVDNbLwKYm51g928xpjY9t3GOGup-4jghMPNwL8tU-jUTlPeUikIUk3wdDpkqgBwxwNXtvxda6_L_anYqcMNPbdyE2PdHmfxAKnExRklYpnkBN_bWnGAe8kHyPGUSSjN4thxJodksJUl2IgKqyovZevfHjt_9XTCwjuVPPYRWwfjRONNVfoH9IysOGPwmVlLvsIasMl-0K0o8hhs25h-nosKAMQVip9IBPWRGfrnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad5ddb268.mp4?token=nbTRf8MdsLRKD-6YtVY8yVQ4JXKAQ-tI8etWmbuU7MW9Ui4faE-Emt5idCC4oj0ZElFBdDSdwGh5r7dd-AdPMxJoJrusG4NVNfaOO862tuXYOfVDNbLwKYm51g928xpjY9t3GOGup-4jghMPNwL8tU-jUTlPeUikIUk3wdDpkqgBwxwNXtvxda6_L_anYqcMNPbdyE2PdHmfxAKnExRklYpnkBN_bWnGAe8kHyPGUSSjN4thxJodksJUl2IgKqyovZevfHjt_9XTCwjuVPPYRWwfjRONNVfoH9IysOGPwmVlLvsIasMl-0K0o8hhs25h-nosKAMQVip9IBPWRGfrnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی چندین مرکز توزیع تجارت الکترونیک در مسکو را هدف قرار دادند و طبق گزارش‌ها، انبار "وایلدبریز" در منطقه کولدینو دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70121" target="_blank">📅 10:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70120">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61d35336a.mp4?token=tf5l7kSUOn-AyIa_qyUuDPULNxU61VVjC1NFklGgKXXDSeKbwMR-gilp_p8WZrqYs5uCQhfUL-nvxnk0XbnNu_9tFeVEE76SQQ4nQZDs-7Vds9-4Bit8Aq81XDcZMuNHjtu59ZIuRWBYnMvQHuikLIqt0dVLlCOG_XD6b52ZJ6nQmmIUyuy1JCHceXk5lA72BGhG4so-LiISZFmwpS7pYVcpax5ZC2ieayOWUyUG47nn7PfA4w-rFsUdBLVncxUSwLZZMajmlRyntM1nMhJT0CBrTyE1w7JlEK662LV8ia7vPMgiVix6IEB5OHHAsF3GdEnbO7c5aXgAgCpiFHXutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61d35336a.mp4?token=tf5l7kSUOn-AyIa_qyUuDPULNxU61VVjC1NFklGgKXXDSeKbwMR-gilp_p8WZrqYs5uCQhfUL-nvxnk0XbnNu_9tFeVEE76SQQ4nQZDs-7Vds9-4Bit8Aq81XDcZMuNHjtu59ZIuRWBYnMvQHuikLIqt0dVLlCOG_XD6b52ZJ6nQmmIUyuy1JCHceXk5lA72BGhG4so-LiISZFmwpS7pYVcpax5ZC2ieayOWUyUG47nn7PfA4w-rFsUdBLVncxUSwLZZMajmlRyntM1nMhJT0CBrTyE1w7JlEK662LV8ia7vPMgiVix6IEB5OHHAsF3GdEnbO7c5aXgAgCpiFHXutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از افرادی که وظیفه نگهداری از جنازه علی خامنه‌ای رو داشت:
زمانی که محل نگهداری پیکر رهبر هنوز مشخص نبود منو بردن تو محل نگهداریش جای خلوت تاریک و تنها بود، تو اون لحظه تمام غربت تاریخ شیعه رو دیدم بعد با خودم گفتم خدایا مگه میشه رهبر یه جایی باشه که حتی یک نگهبانم نداشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70120" target="_blank">📅 10:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70119">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4PKklfElhsvA3syGCeS8_qrZ2obigJnokPIy_p51zm21M19bJmI1iJmyJGKAdZmCCZyiETuX4YDDjz6BxjmGg2DiOK8kJxBZtbcnfV8ZfCVi4W7Cvs9Epz3_OPzoCafmS0--7vpDD-8qHGJjkH09ysKfEPuI0E11mcGY_WqXMVVlrjKpFe1wBMnqHlmO-unV4Ib7gZZXmVVsqzRlQSZAXVHp4PyUS9QyhVKDTq4v6Kzh_C5TxtBjfVCqw5j3S9nqhzXHmOihnKHQjFJ2LA8R3QRCJ-yY8_snYvGtvxxMHiswujhpWchqyPZPVLzwn-bXMsV5-Fj1X1_beyxpIZqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسره:
۵/۵/۵ با یه دختر وارد رابطه شده و نزدیک ۱۳ روز باهم تو رابطه بودن.
بعد از اینکه کات کردن، آقا پسر یه لیست تهیه کرده و خرجایی که کرده بوده رو فاکتور کرده و فرستاده برای دختره.‌‌
اونم کل دنگش رو داده، البته جا ۱۹۰۰، دو میلیون براش زده و گفته فقط گموشو...
لیوان یکبارمصرفم حساب کردی مشتی؟ باز خوبه پول اینترنت و شارژی که مصرف کردی رو تخفیف دادی
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70119" target="_blank">📅 10:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70118">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6731c5b6.mp4?token=JFqeASwiQbsUBL5ScjDvsGES0grZdRASqL_jfoxUPbvH7UjOo8a082DVnnJiOrCGL712dJhBqAmwFjdUfZRLZLKM7nnfyl942S1kpiEjMBhp5Hpqd-pqO8wX3aN26Rwbnz_ykn8UyRWF_0kkwmiDu0iow7qPHV2-OfxtPCc5lr_GkONjMlXyEsnDQPidYdEn5aN2ioVCXfTevUwKKpU4RgUh4rN0COQpD_2bHiVdP_Y8U-q2d9iCVm4U-w5QLVXubdA_iBvfW2a0qgODb42_qYrz7J8BQ5EPJih4cVC0T3etiPEuCtNfZalS40BNtsjkajfkeYeQgkMjJsT-vs75yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6731c5b6.mp4?token=JFqeASwiQbsUBL5ScjDvsGES0grZdRASqL_jfoxUPbvH7UjOo8a082DVnnJiOrCGL712dJhBqAmwFjdUfZRLZLKM7nnfyl942S1kpiEjMBhp5Hpqd-pqO8wX3aN26Rwbnz_ykn8UyRWF_0kkwmiDu0iow7qPHV2-OfxtPCc5lr_GkONjMlXyEsnDQPidYdEn5aN2ioVCXfTevUwKKpU4RgUh4rN0COQpD_2bHiVdP_Y8U-q2d9iCVm4U-w5QLVXubdA_iBvfW2a0qgODb42_qYrz7J8BQ5EPJih4cVC0T3etiPEuCtNfZalS40BNtsjkajfkeYeQgkMjJsT-vs75yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
احمد آریایی
‌
نژاد نماینده مجلس:
مهسا امینی به درک واصل شد!!
اونوقت رئیس جمهور قبلی ما اومد گفت مگه میشه یه نفر همینطوری بیوفته بمیره ؟
بخدا یه ادم عادی هم میدونه ممکنه یکی یهو بمیره اما هشت ماه برای مملکت تبعات اغتشاش داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70118" target="_blank">📅 09:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70117">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=oLXPcn_d7PSiG8UUx6AhMXowP0pmNvAXJyHbHgN-mU9iXXoLrBl6q5Mr6GzvDKxM6S2vLfIlRhMpZOQjiiLvakyydaZNZz4OZOtAGW1MPMH2HVBTsandL9FtC0QEDkKBVChGTskTYCiP8k6IPA6ozaIW4UpSJAx_VrQcr-j9sNhf9bTmHVj1d7v4NOiogeNmuSQCU7e18aJBqY6JA2WaEHQqxBMp2KFm_hzUyQFfnIlyqGL8YDbPRuOcd_-NTCZY_Vegm5NB2SuNxWlaR0l76hdYJlocbSm05TEzNsLj4g-bjmSiry6_GJce8-UrQUTTsv4S13bc8jokSzC4tYXcwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=oLXPcn_d7PSiG8UUx6AhMXowP0pmNvAXJyHbHgN-mU9iXXoLrBl6q5Mr6GzvDKxM6S2vLfIlRhMpZOQjiiLvakyydaZNZz4OZOtAGW1MPMH2HVBTsandL9FtC0QEDkKBVChGTskTYCiP8k6IPA6ozaIW4UpSJAx_VrQcr-j9sNhf9bTmHVj1d7v4NOiogeNmuSQCU7e18aJBqY6JA2WaEHQqxBMp2KFm_hzUyQFfnIlyqGL8YDbPRuOcd_-NTCZY_Vegm5NB2SuNxWlaR0l76hdYJlocbSm05TEzNsLj4g-bjmSiry6_GJce8-UrQUTTsv4S13bc8jokSzC4tYXcwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسنپ لیستی منتشر کرده از حواس پرتی های مردم که وسایل خودشون داخل تاکسی ها جا گذاشتن :
261 هزار کارت بانکی
178 هزار کیف
137 هزار موبایل
یه کنسول PS5
لباس عروس
یه قابلمه قرمه سبزی
یه قفس طوطی
27 هزار ایرپاد
و پشیم ریزون ترینش : یه نوزاد شیرخوار
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70117" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70116">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70116" target="_blank">📅 01:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70115">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=UEYVO5qfldyKiiv8DGIgu3i9YrFR4qf_imYEXu61ig3RZDTUFFoA-MjiPW6I0YKoqLTov7CW6ZseYGSmEK-JrP6TOrIdCMc4PwNhzm43mjoGKWsQFAlMhq0OmuLV5dzXW8SFjcxkfFH0S5ZQOH1xEIFE6OwDpKbs4a_x3DZ3-wud-tq2uwn_66K7wvVWCVpS8qhCXYPecydUPJzMJZ7W4W4VVFMerKk5SsPcAXXpA9RSi3s_50od2f2MDwScuCCxnVQ5tKSUv9gfFaNFlPwKEXf0dPtXe5i0iE77U71OGHYURWO-XpGHIag2JXq_IZ2rLq9PkXBKideDyXvXlkPQkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=UEYVO5qfldyKiiv8DGIgu3i9YrFR4qf_imYEXu61ig3RZDTUFFoA-MjiPW6I0YKoqLTov7CW6ZseYGSmEK-JrP6TOrIdCMc4PwNhzm43mjoGKWsQFAlMhq0OmuLV5dzXW8SFjcxkfFH0S5ZQOH1xEIFE6OwDpKbs4a_x3DZ3-wud-tq2uwn_66K7wvVWCVpS8qhCXYPecydUPJzMJZ7W4W4VVFMerKk5SsPcAXXpA9RSi3s_50od2f2MDwScuCCxnVQ5tKSUv9gfFaNFlPwKEXf0dPtXe5i0iE77U71OGHYURWO-XpGHIag2JXq_IZ2rLq9PkXBKideDyXvXlkPQkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a24
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70115" target="_blank">📅 01:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70114">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhOgm9s180WqEy2oxuGFJVbqoOalUsY5GDF4SyMzqqN9kqtUgRA1RvQtq84xj4EI0vTqeq5wW8WIQ8e0gIuo6tZyS_n7h1ObA-Dre_WpQYKtGBLShQTaW2OW9fWFJXDdxJF4dUjWAKCfaU4VOPB7Xk28vBtuDzwLe9gXK8aIQVGl-mKFU63UY9nqwNXvqeOqzlC-ag0w6eMOY8wXCKm3Q1ncRaw3p4keLIwO1kZYL3q5ORd1YO27QKLhdbNdz0_eMrgPETQO6wzYBX1XDbBduuS2sNdZcXYxN3iRLykQ42KnUnbWvqGCIwEFpPx9671d7-zRmNWhjDSOLh13oYYzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
〰️
فرماندهی مرکزی ایالات متحده (سنتکام):
در تاریخ ۱۵ اوت سفر ۱۰ روزه خود به خاورمیانه را به پایان رساند؛ سفری که شامل بازدید از شش کشور و همچنین یک ناو هواپیمابر نیروی دریایی آمریکا در حال عملیات در دریای عرب بود.
دریاسالار برد کوپر با مقامات ارشد غیرنظامی و نظامی در بحرین، عراق، اسرائیل، اردن، عربستان سعودی و امارات متحده عربی دیدار کرد و با نیروهای نظامی مستقر آمریکایی وقت گذراند. بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه مشغول انجام مأموریت‌های مختلف هستند.
کوپر در جریان حضور خود در خشکی، از نیروهای دارای عملکرد ممتاز و کسانی که قرارداد خدمت خود را تمدید کرده بودند تقدیر کرد و بر مراسم انتقال فرماندهی «نیروی ضربت مشترک ترکیبی - عملیات عزم راسخ» (CJTF-OIR) نظارت داشت. در تاریخ ۱۱ اوت، طی مراسمی در مقر این نیرو در اردن، سرلشکر کوین لمبرت فرماندهی CJTF-OIR را به دریادار دوم لیام هولین واگذار کرد.
کوپر در زمان حضور در دریا، برای دومین بار در سال جاری با ملوانان و تفنگداران دریایی مستقر در ناو «یو‌اس‌اس آبراهام لینکلن» (CVN 72) دیدار کرد. او پیش‌تر در ماه فوریه به همراه استیو ویتکاف (فرستاده ویژه آمریکا برای مأموریت‌های صلح) و جرد کوشنر از این ناو هواپیمابر بازدید کرده بود.
در جریان آخرین سفر کوپر، او برای تمامی اعضای تیم ناو لینکلن سخنرانی کرد و از فداکاری و شجاعت فوق‌العاده آن‌ها تشکر نمود. او همچنین با نیروهای رده‌های پایین‌تر دیدار کرد و به افراد شایسته نشان و تقدیرنامه اعطا کرد.
کوپر گفت: «گروه ضربت ناو هواپیمابر لینکلن تیمی قدرتمند از آمریکایی‌های موفق است که با افتخاری عظیم و بجا، به دستاوردهای خود می‌بالند. تاریخ، این مأموریت را به عنوان یکی از فشرده‌ترین و تأثیرگذارترین عملیات‌های دوران مدرن ثبت خواهد کرد.»
ناو آبراهام لینکلن که پایگاه اصلی آن در سن‌دیگو قرار دارد، در ماه نوامبر برای انجام مأموریت اعزام شد و در ماه ژانویه به خاورمیانه رسید. این گروه ضربت با موفقیت هزاران پرواز رزمی را در حمایت از «عملیات خشم حماسی» (Epic Fury)، مأموریت‌های امنیت منطقه‌ای و محاصره دریایی جاری آمریکا علیه ایران انجام داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70114" target="_blank">📅 01:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70113">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSIXugHQApWMG-fbtuoP9vYSiLERbe5J_QM7v2vCUA1YzzhEt8YKdIq5k4nZ8qpt3L4mH5dhxlwfnhzWwuuondDe6HBF7k-4iOqnYLlge6SoUzxJr1yH4rJI_qP_0qVN4rGQgczeeg0o2r0rYF1jkdFIX6BOLJk98LaQnU9cN3Cu6XG2HWA38YX18QjXSXaJcVKY0P40gFXPK2c49lHxe_xiFvSV4jLFSLNjxss4o3k1VdXfoUUmvVYmeKUDSUci4hN6p6xBSk655bFYvTrm_zcpRhoGELKMoEZVN-WkabBrWDBMOD47maln0bunAhlDkV-YoWSOLAn770V7_QpgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ با تصویری از خودش با کلاهی که شعار «ترامپ ۲۰۲۸» به سر دارد:
«ما پیروز خواهیم شد».
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70113" target="_blank">📅 01:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70111">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCpK4V34cn0y8zNNp6iEedA2u14qbKEqGZh1lUvTiyxwTLaUL2-mrInqWFijZlple9phZ-Hg5r_yY0rxFF2SY-66OskoiorgCDEatweKmUu1o84y3MakY-p7PA9qoAqZGU3J_Lmb9NOhKaiLNa6IrA3FTO0Jy-uA__fLVNtuthZ4jDDZiuhSdYurz_YbXZie5DzoM2VkekEXkKpkV7rOL_Xp-dJGgNq7Ig4gnE3PUKkce2qIdokXRNGCORVNTpn11i4ulgOYuUNnudE4kQL3A-fMR9YnXe2UyvJaUj542quUllSvYVc4-4ACs1xtTUM9PrRAKMnkquz9m4WpLnJfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0a274391.mp4?token=hr21bQW_J-akl7uwKkFcI3Oq4AFIg9VV3RFNppYbh8b2Hk14Sj-XzezBzNZu76lwjTflWX9RKq--H0_D3T_oQ36Q0mODQp4VhMCeLylKhxZMVtU5fyqQW30qrciKNgrIKr2Z4zDaaMlokfa_rpMiYTz4WfuDIqPPu-vYvPD5Y4QO0glsN0mJhLe4WcyKxb9BhJobiQsaxBsh-N9veCAs0z8Wd10oBv8K-SL76lg3KR6yrOuYfu5hnzSqv4NGw5gn8_QDApDs87PkymdSuTA3u0dCx3wB3Iu270-2K6TXR3IxvuA5ah4fE-INZ34Jtx_gnJBNpJiFIAD0CEItMwPWYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0a274391.mp4?token=hr21bQW_J-akl7uwKkFcI3Oq4AFIg9VV3RFNppYbh8b2Hk14Sj-XzezBzNZu76lwjTflWX9RKq--H0_D3T_oQ36Q0mODQp4VhMCeLylKhxZMVtU5fyqQW30qrciKNgrIKr2Z4zDaaMlokfa_rpMiYTz4WfuDIqPPu-vYvPD5Y4QO0glsN0mJhLe4WcyKxb9BhJobiQsaxBsh-N9veCAs0z8Wd10oBv8K-SL76lg3KR6yrOuYfu5hnzSqv4NGw5gn8_QDApDs87PkymdSuTA3u0dCx3wB3Iu270-2K6TXR3IxvuA5ah4fE-INZ34Jtx_gnJBNpJiFIAD0CEItMwPWYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70111" target="_blank">📅 00:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70110">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
رئیس سازمان بهینه سازی:
🔴
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
🔴
دومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش ۱۲۱ میلیون لیتر تولیدی روز بین خودروهای موجود تقسیم شود و هرکس بیش از سهمیه بخواهد باید بنزینش را با نرخ آزاد بخرد؛ تقریبا مشابه روشی که قرار بود در کرمان اجرا شود.
🔴
سومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش سهمیۀ بنزین به‌جای خودروها به مردم اختصاص داده می‌شود؛ چه خودرو داشته باشند چه نداشته باشند.
روزانه حدود ۳۰ میلیون لیتر به حمل‌ونقل عمومی و تاکسی‌های آنلاین و غیرآنلاین اختصاص داشته می‌شود تا قیمت آن‌ها تغییر نکند.
تقریبا ماهی ۳۰ لیتر به هر فرد می‌رسد و امکان انتقال و خرید و فروش آن وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70110" target="_blank">📅 00:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70109">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3808337972.mp4?token=ODjQD44UigYhArwmFkqYDo0SK6voUvAutRbFTl6rh7Fwmxbbrp-x-aC5uvbCV9ODHBw4Gdx4W1gGeEkJIOMkK9CRqTYWzV2n2lfndBTQH047uemZvIrvsDueJLlOtEizv-BQ6M-zrrhF5PPYX8oF_Th2hi22WCkoP3Cm-O5H4ixxmzExYShgaRC-khCav9AYZeBhEYLUdErRtc1aYgpcrGZt3iAKDjQGbUxg4kYEIa6LDXN6IR4SOM-VUtafOVjQn4Ku-GxRZjBDmpAkaVfEuuOcILDxM5w80XtFIw30oLgRjH8I_V_Lj9SLsGuxKA3CCH1xCsFKYFXeMEQk6j0HEzL-hUIrEk6fTb5Bau68sHWTI4kPHfWM1E05giPRIb-Jw-4phwHSVKQUoSy9X0a2MJdXocvS7c-tmXXvMrQxvmFf4YZQ0zG5O6LeON98FPlt7j1hLpYKsiCPwDJIP4Fw4T24fG5nQNhpTBVV-MpPj7B1nf1OW52fHK15LQVAUnZeyJMZg5APjkDzPieoXbU0xaNGuaLKMyFlit9yXBT5glN91ZMszFAJxpHklp3fFCCXgA3ZpKw7pQ-A-RvucQIRkfqd06RC-SNMauSn91Xie_I8rqJBkHMQAYuPpx9EVeh2cTnwO8gI9TRztkn8i1wdHqWNrm7_EKgwsjXIbb9qPUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3808337972.mp4?token=ODjQD44UigYhArwmFkqYDo0SK6voUvAutRbFTl6rh7Fwmxbbrp-x-aC5uvbCV9ODHBw4Gdx4W1gGeEkJIOMkK9CRqTYWzV2n2lfndBTQH047uemZvIrvsDueJLlOtEizv-BQ6M-zrrhF5PPYX8oF_Th2hi22WCkoP3Cm-O5H4ixxmzExYShgaRC-khCav9AYZeBhEYLUdErRtc1aYgpcrGZt3iAKDjQGbUxg4kYEIa6LDXN6IR4SOM-VUtafOVjQn4Ku-GxRZjBDmpAkaVfEuuOcILDxM5w80XtFIw30oLgRjH8I_V_Lj9SLsGuxKA3CCH1xCsFKYFXeMEQk6j0HEzL-hUIrEk6fTb5Bau68sHWTI4kPHfWM1E05giPRIb-Jw-4phwHSVKQUoSy9X0a2MJdXocvS7c-tmXXvMrQxvmFf4YZQ0zG5O6LeON98FPlt7j1hLpYKsiCPwDJIP4Fw4T24fG5nQNhpTBVV-MpPj7B1nf1OW52fHK15LQVAUnZeyJMZg5APjkDzPieoXbU0xaNGuaLKMyFlit9yXBT5glN91ZMszFAJxpHklp3fFCCXgA3ZpKw7pQ-A-RvucQIRkfqd06RC-SNMauSn91Xie_I8rqJBkHMQAYuPpx9EVeh2cTnwO8gI9TRztkn8i1wdHqWNrm7_EKgwsjXIbb9qPUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
وضعیت کنکوری های امسال
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70109" target="_blank">📅 23:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70108">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
❌
طبق گزارش های غیررسمی سپاه لحظاتی قبل از سیریک به طرف تنگه هرمز چند موشک/پهباد شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70108" target="_blank">📅 22:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70107">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmcwrnJE6RpoLQ9K_XfK3TsZYvUMygsJBNeli2FyPSOu66ZuwKFC6QcUFHi4Nfb_ankyzZgCB9RsSRPLIbyLprH-KAWyzO5Ya8nNMMAQEcddngu-lSVE0bX2CrxyugqvLnb9gYbhcKvSPg8iS5WlMHLm0I_IP-QxHCa-rQ55O2Fr2VOlW22UGZIVtebL1Q043WtErLGEihRtwGSOk1vANPetjbF3RVjbKwLNaSiNjoKWlqcpaRuxaRIoCXEXtqtXNhHm7S41QHeZo1dmEomOZx10NfXUi4hmJaxgFBj2eTDuNW0Ds7LCwa0wgjvaDWRHTp4ThuThCgRbOysf_ommNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
با وجود آن چهره‌ی غیردوستانه در این عکس خاص، عکس‌های بسیاری هم وجود دارد که در آن‌ها لبخند بر لب داریم؛ من و کیم جونگ‌اون رابطه‌ی بسیار خوبی با هم داریم!
رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70107" target="_blank">📅 22:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70106">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c505095a40.mp4?token=BN-OH6kA8Ww3_UBkewbedFF3vQiPp_fIrlS9Jpg40ArIaeGbUT9GEzBR6TE7MPhTHldLLx5th-T9UHDHsLUvCtt3RHa3R3jiM0XehCuOkD-7BdYDgafj58KBaTicig87KGkFcG9DSyf3hHmyuwvey0Dkrm5KRADJSc4Q5xWyv69P-2gXMfBnsRmz3F1CK2D0-oL6nzR1ofEQinudHZtamgE4qdlmKN5BbRBi5bJ_K3jslqEs36Nh7hKsS2vA3BNB7nodoceyMWEMV7T4zdrLa1tjMHQV9eij-lSJdiDbiavkemXbNBw40hEfp0r8blfgbpUPrjfORBjDBW6dVkddRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c505095a40.mp4?token=BN-OH6kA8Ww3_UBkewbedFF3vQiPp_fIrlS9Jpg40ArIaeGbUT9GEzBR6TE7MPhTHldLLx5th-T9UHDHsLUvCtt3RHa3R3jiM0XehCuOkD-7BdYDgafj58KBaTicig87KGkFcG9DSyf3hHmyuwvey0Dkrm5KRADJSc4Q5xWyv69P-2gXMfBnsRmz3F1CK2D0-oL6nzR1ofEQinudHZtamgE4qdlmKN5BbRBi5bJ_K3jslqEs36Nh7hKsS2vA3BNB7nodoceyMWEMV7T4zdrLa1tjMHQV9eij-lSJdiDbiavkemXbNBw40hEfp0r8blfgbpUPrjfORBjDBW6dVkddRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب یکی از هوادارای استقلال داشت شاد و خندون از تیمش تو مصاحبه تعریف می‌کرد؛
که یهو رفیقش تصمیم گرفت این شاهکار رو پیاده کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/70106" target="_blank">📅 21:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70103">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzdXBA1fdXYDNrZ6NBsfSLLO_e9b3bglmhw4_2H1BohnAPQW9Ge3qwsQIyGYl2h57KPXmJqeJn5vlcBy2rW6lebid1XMi8vpRrYjZOO9kPjK9Q-giRSUqUMNXCkpwCF7EyA95Hom53mPmWAlV8qaq-SHTmCJMMecg0I6PbTWbO_GxNEUvOslwZRWd5gCRbN5V-_4PNHrn001xUN7tlD3AHBhyjpIM8_gANLT8FnUHzRX7qcziOIDYowCnuWmuvUQl8EeJyN5bav6NHNu-IBpsz3h71cg3cJMGOr0o2immBJVC342U_Ae-kUAunHr5iUnslv7FKyEuLQFOhSYpV5ulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLbVvrVHi3e-jiDD6qRFIkb6Msp02pUwEb203mepziYjbRNtUnfoQ8o2RsDfOg-BF4FsB1Cx8rNZk9KpAUJ0Hhw-9nvdFu85vHApd6MBY6eQXo8s4BHrcgtdmh20xexmPO2sSkbzZbecm8ofuGjNDUXegnGPSPloENjSkAPXS0hjQ87-m8Pu3qnwa3dGFUdopFgHfS_aimg1d8ZDSDJR4EkDyz3NMEeh1JjDGQn9UbBOGY7p1Iwmidbt3y7gmVEJZWsYyIfUlcsnREzMhfRN6xR_ZNNyV8QxPUYrhh51ABlFWotjzlCNfQaC-VqNvmiIY6nVPKM5LYhaiRYHRxIbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxX21Z4p_W01b0bHtfqnPlMKwziqDnb34ixxr4_4QbIk4uiBdissip9ssZU0rpHwnMecpKyjmKgxnZTqxCfWgrCu4OAip5xBxMWJZSyarb_PtmN8QPWr6W0njibzmh-B0cxgZIhrSvmfGYOjf1yJ_XJScXDW_rIFzYiAU9T9Kx79_b_qHmZrX8IGPXSuY69QszMCz5IhVwPOqbTCKtdiWwtlIe5oalPXmY4AdkdVy7yxa06sBXSp_UGAAa5kbs75v8OPU8y1bQp88ZO7roy7I7efL5Fm5XiT3lKU4H86GRoyrTtma-6CWWdIMtEIQIwUwqUvorP2MHDTm7waXLr6Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست و استوری نوید محمدزاده و حمایت از فلسطین
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70103" target="_blank">📅 20:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70102">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
🇮🇷
🇺🇸
میدل‌ایست:
به گفته منابع، ایران معتقد است که دور جدیدی از درگیری با ایالات متحده اجتناب‌ناپذیر است و تصمیم گرفته است تا به‌جای دیپلماسی، تمام تلاش خود را بر آمادگی برای نبرد متمرکز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70102" target="_blank">📅 20:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70101">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39fe384fd.mp4?token=TWg-jEqEBrCHEi6mTHA0JMcUoThvrE1UXAPnOv1TcUY_sxUkoxPU5kyhZYc4CBmAbTklpDkGEkhN0jg4Z3Kq2462hhHGeZ2t-2jfjG3phaxiTUMU39bCIuo4QVBFZNCPLNY1Q8rA5emgqxs2CmAlyDF6AjKQTm9JPZZCGs7sMSGmYEEDEIHe-ii2letA5TkTKtRGuBCV5zUz9QCvVFxRZ00fDxXnYA-6RypDXPDEUmLl700N44Z5wr2vhnkST_vxMs4HIdx12StQPN5F7WPezHlYBZLEDQvUPTzvlmHxQRMLzoBfoTcUNHV9gyYdKvZk5dlYNhYmn4OP5NSe8AdsbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39fe384fd.mp4?token=TWg-jEqEBrCHEi6mTHA0JMcUoThvrE1UXAPnOv1TcUY_sxUkoxPU5kyhZYc4CBmAbTklpDkGEkhN0jg4Z3Kq2462hhHGeZ2t-2jfjG3phaxiTUMU39bCIuo4QVBFZNCPLNY1Q8rA5emgqxs2CmAlyDF6AjKQTm9JPZZCGs7sMSGmYEEDEIHe-ii2letA5TkTKtRGuBCV5zUz9QCvVFxRZ00fDxXnYA-6RypDXPDEUmLl700N44Z5wr2vhnkST_vxMs4HIdx12StQPN5F7WPezHlYBZLEDQvUPTzvlmHxQRMLzoBfoTcUNHV9gyYdKvZk5dlYNhYmn4OP5NSe8AdsbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوتا گربه داشتن دعوا میکردن که یهو یکیشون تصمیم گرفت گرفت خارکصده بازی در بیاره و تا موتوری نزدیک شد رفت جلو موتور و باعث زمین خوردنش شد:
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70101" target="_blank">📅 20:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70100">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMyEdRj0S1jx98sJsc8rpc9B9EvFX-qQmlV6qNixWbEv3-2hlAutecRfbS_nyVtQbRks4WPoOd8H0r8CRzfo1aUvo3rTnXzUtnVg0fmYRnIAVc80_VUHAjQpCozff-ztpwbrP0bLWGdQfaFhzSnZH__r3nxSEsG8BllvHofkpU5CzkCIiVeOzX7R6WoNrmdF4bGt3RoZ6Fn4mgagXUNCnsFK0oCOOQ-JhBr1oyrp0csRT_w7MJk0QWF8RL5Ccxnr3TGjr3wbnyHdgSpKXhPKmlIYLjMyftZAetIMFs8SBwZeBblwdpIjJrH_4U43zH6JGyDzXKsTRYVTs9QJQmFpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
تصویری جدید از سردار عظمایی فرمانده نیرو دریایی سپاه که توی اتیکت اسمشو نوشتن عظمابی
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70100" target="_blank">📅 19:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70099">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e3b71c01.mp4?token=r9EJkUIAEl6OCCuIDut87UOnVcE2VgFZCxicE6rvAUq2isZZeZZSbP8Np2FbmgNa1-krKJKlkbclpn_yQcY_DqOnnQFcnesnIyHcDGzf3lD8o3P3kGd4L_vBT2vIc1m7ilFaxNlLYz6Uy4rLQ0CkBgHaTVoUnupW1olRRt3LBCVrzkPjXzz99-hk5v9PMY6LKc7rTk6l4AUq9Yw-ZDIm_P12-mxfVoqM63e560BiGE1LqDquYJbfiLmOwPv3tsUmi4CNI6THg9f9xrezS6LN2pG4Way7C7oFPAk8bJj5PUsdp3_aNNmwvDvNQbPiGTRNQOpWSSkSZ7wokHraDlpBWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e3b71c01.mp4?token=r9EJkUIAEl6OCCuIDut87UOnVcE2VgFZCxicE6rvAUq2isZZeZZSbP8Np2FbmgNa1-krKJKlkbclpn_yQcY_DqOnnQFcnesnIyHcDGzf3lD8o3P3kGd4L_vBT2vIc1m7ilFaxNlLYz6Uy4rLQ0CkBgHaTVoUnupW1olRRt3LBCVrzkPjXzz99-hk5v9PMY6LKc7rTk6l4AUq9Yw-ZDIm_P12-mxfVoqM63e560BiGE1LqDquYJbfiLmOwPv3tsUmi4CNI6THg9f9xrezS6LN2pG4Way7C7oFPAk8bJj5PUsdp3_aNNmwvDvNQbPiGTRNQOpWSSkSZ7wokHraDlpBWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کص‌مغز بازی واسه ویو یا پیک‌نیکی بودنِ خایه؟ مسئله این است
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70099" target="_blank">📅 18:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70098">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5505f54825.mp4?token=QtUb1p4iWVizVmLsoyY38lViqpXpoLAxpXEanPw-hLBFXcTp3bN96VAFSPmyYhMqvn0yo6-wQZ5Uc4XPaYvqUSrZW8LndzhoNfnZq_XseJX03iWdNJttKWphMUjCApj4LdiHNxjiyrRVXBdiH6Fe5eAbzaEfxeWEDuzWqfb3oeXPsK9Ou3s81ncBQYEbzbyDjRsTQ2M5j7u-Y-tgIu-FQc_Qqj1wkymxqMiVEMVci9R-VV5H_4tC4ncnvNNzFX_nFRA9Dn1s6biVR2Ip81Rsye_lxh8ICNQ7lZZfadmQh5uIFyMPr8GlbFGEziV7v-mitgz3IeYqnNV0MbqrQoxYww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5505f54825.mp4?token=QtUb1p4iWVizVmLsoyY38lViqpXpoLAxpXEanPw-hLBFXcTp3bN96VAFSPmyYhMqvn0yo6-wQZ5Uc4XPaYvqUSrZW8LndzhoNfnZq_XseJX03iWdNJttKWphMUjCApj4LdiHNxjiyrRVXBdiH6Fe5eAbzaEfxeWEDuzWqfb3oeXPsK9Ou3s81ncBQYEbzbyDjRsTQ2M5j7u-Y-tgIu-FQc_Qqj1wkymxqMiVEMVci9R-VV5H_4tC4ncnvNNzFX_nFRA9Dn1s6biVR2Ip81Rsye_lxh8ICNQ7lZZfadmQh5uIFyMPr8GlbFGEziV7v-mitgz3IeYqnNV0MbqrQoxYww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بعد از این صحبتای پزشکیان موجی از انتقادها از طرف تندرو ها به سمتش در حال روانه شدن هست.
دلیلشم اینه، میگن چرا مسعود داره اطلاعات محرمانه کشور رو لو میده، باید باهاش برخورد قضایی بشه و...
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70098" target="_blank">📅 18:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70097">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70097" target="_blank">📅 18:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70096">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjruQvT_Kwl6JB4rkvp8hGPzJN4sn_5-o_MYnqGmlLJQx8aawAp9wsjM0gYPMioHsbmSy9zSpEfxHwzBOEZs1eIf05KyeY615D2w3GJ-rW9U6Ywb25HZ0oIuWqPm3LxgWg_TYIemdrqx8acG2hEaff6lPLTaJE91KveifsthPYR4NhiGb_kVg9cTsuVGD7dkKs8lSU6vmgJ2uYKHlS3LXBIPcPwajbG55BYMp3RxUqyaz0ESWDj9lyY5vsrwQew6FMOV3fWN3ZEt-_eHAE5TZHuiA_m5nn07eIiS9Bfslg5N5onHND7JZRHI9hr69PICclB4r0DlyTjY2RsiKKWttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g24
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70096" target="_blank">📅 18:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70095">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2573e39307.mp4?token=YX6neWbg1SHCz9ab6yvq_RQrfeE7Lj4XOXRe30mqrBm1EFKxL8ZuZAWzPYY7uPF_4paRuVLvYLoI7eIwX8G02B-QjWc7j6Il7h2Z7VJCXMe3akjQQQbX09GKgN22AyEk6EJdHPoHCLSmGOUiW8sUc0jD6JEOS3wU7sTE8L18sXSX48oq0XC1cTam0jyRrgTnaI3lUsPT0bzamBLFGKm056J8_s4U9ZIwTgc6kYdYHHVnECyq2zG0FXPJvvSPxvEKJBbFRWBMEiWM72QQzwOCrhSP-V4vWdKK2snMCYyfXvIb_thEiYyOadrfS9onuoyRVpq21jNIbuKujO1_ilekgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2573e39307.mp4?token=YX6neWbg1SHCz9ab6yvq_RQrfeE7Lj4XOXRe30mqrBm1EFKxL8ZuZAWzPYY7uPF_4paRuVLvYLoI7eIwX8G02B-QjWc7j6Il7h2Z7VJCXMe3akjQQQbX09GKgN22AyEk6EJdHPoHCLSmGOUiW8sUc0jD6JEOS3wU7sTE8L18sXSX48oq0XC1cTam0jyRrgTnaI3lUsPT0bzamBLFGKm056J8_s4U9ZIwTgc6kYdYHHVnECyq2zG0FXPJvvSPxvEKJBbFRWBMEiWM72QQzwOCrhSP-V4vWdKK2snMCYyfXvIb_thEiYyOadrfS9onuoyRVpq21jNIbuKujO1_ilekgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش چند تا جوون مست کرده بودن و توی ویلا همچین کاری رو کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70095" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70094">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532b4ed793.mp4?token=ReWTbcMbnnEm_XDaGqUSk0Gngalnw4HKaor0aQv4G6IhzUlhYEPWtb4oB3GyZ8oAvCzDQ6UDv5gq6wDcXfqaasUgUzRsirvgWD6eTAq50x_HGqjYnIcTpvqGJT8DeLddqZkNNv00c62Xdc2RGNtI4dXlRDkQkOPTojE4fofucZUJXq9IOHOo2K_4Ic-hwO_R55R7bcpkxRBDRsCD93cnWLf7fEPyeA1GQ6Aw4AwsIUH_STS1KSuN9D2VFGwpUvZ3SJHBMVF0LTj40gd3QZbIF-BoE8TXHwpFOaVPpX9V2RreInCJEuGGw6KiCkcJOW10xOniNxTf1dyUl7XRSyJsUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532b4ed793.mp4?token=ReWTbcMbnnEm_XDaGqUSk0Gngalnw4HKaor0aQv4G6IhzUlhYEPWtb4oB3GyZ8oAvCzDQ6UDv5gq6wDcXfqaasUgUzRsirvgWD6eTAq50x_HGqjYnIcTpvqGJT8DeLddqZkNNv00c62Xdc2RGNtI4dXlRDkQkOPTojE4fofucZUJXq9IOHOo2K_4Ic-hwO_R55R7bcpkxRBDRsCD93cnWLf7fEPyeA1GQ6Aw4AwsIUH_STS1KSuN9D2VFGwpUvZ3SJHBMVF0LTj40gd3QZbIF-BoE8TXHwpFOaVPpX9V2RreInCJEuGGw6KiCkcJOW10xOniNxTf1dyUl7XRSyJsUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
صداوسیما: پنج هزار قبر برای آمریکایی‌ها در اطراف تهران آماده کردیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70094" target="_blank">📅 17:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70093">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIf2UovNEo5iFg0J7EMiRREfxsuOK_hCr1YFA_kV8s1yTPhtv6fStVgVAU3ZljX9do2TrrtHX_-3UuVLo9LRnetrstKVu7p9haOBRRsVHg4cQwK8FaKu0OFuDajcKxn1E0r19T8dTa-BuXCnEwi3QLM30uHeGl4V6lDG0b9t4pVPTDr2ZlbljQtJB4CQBhVabBevebqlFjDP6FFWFVRHlPQrU5Vas59zIEmFbbOXcC2KUcfTLXzw7j3Zuzb39DO0K4rCXABsSYRXa98UZYwfqWvxfdMtqt6co3KG2qXKnnic45ZQi4kYElQEt10ujZqauryvBzcC7Q-AYI-HAWyjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
🇺🇸
کراسنشتاین خبرنگار آمریکایی:
دلیل استعفای لیویت این بود که فهمید ترامپ اونو به عنوان طعمه مرگ توی هواپیمای اصلی سوار نکرده و با خودش نبرده(ماجرای هواپیمای ترکیه)
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70093" target="_blank">📅 16:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70092">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZRoDFhIomxLdIQm6gGPE5pkje3LhcOz4hfqXNTZU1WrVjNIReJERUlaHdgIDbTT8DjhoGPOJAxIDWYoR2dBzFeCwWrawCMUbpN5dwUfQUwNeT4DV_O1g8T0Da14HaW58mBq_WzQOslc1taKoQGsaVvFLAk4sEK4-KVLSuUTX5XUC6isS0drNL6zplYkFh7SOWi7GFq1fu410UTsk7KB6kJdVRwFRyVl_ouyDFiQF8tzqs4nuAGUzqT6h84D27jH3P4DlfhxgbZfvefWQuJjCzEUgGQ6Rd8_oG6_nzskHo3plfbCc5DHW6QEBm0A5XoMWnykxWs66OvcqFbG-oUmGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰‌هزار تومن تخفیف خرید با اسنپ‌پی در شبکه‌های اجتماعی!
دیگه با اسنپ‌پی می‌تونی از بیشتر از ۴هزار فروشگاه و برند محبوب در شبکه‌های اجتماعی مثل اینستاگرام، بله و تلگرام، خرید کنی
و با درگاه پرداخت امن اسنپ‌پی هزینه‌ش رو در
۴قسط، بدون سود و کارمزد
پرداخت کنی.
با وارد کردن این کد تخفیف توی درگاه اسنپ‌پی، خریدت رو نهایی کن:
✨
کد تخفیف:PAY5SCMD
از طریق لینک زیر، لیست برندها رو ببین و با تخفیف و قسطی خرید کن:
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70092" target="_blank">📅 16:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70091">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6444186749.mp4?token=kDVHeLTvzkD_aOO0_oqeG5i_3xWVKg56p1FYLekgI0CzYEHDjynoqzVdpvfeUVz_Rt0C26a-aqQdMrjcNB_hg6MKH4RaJEHrp1Jo-rAuN5dxlsziORp3rCKYfyi5KXYxBsiI-mQFuCGZYUFClxUdmjzXuhSBWRwfK4z7DFzjDEURQqUh5pE4U4dQP9m1ByYQx_6oX2m1WAKJL2chGuMqVtfUxj702rGnZOGZ0IM0TK_bkfbNQ0SFaWgchRPgu99FuEEhXXd780rJKgO3bmJoTBZghxtzOltMno_h4RWm24cdBXsuCcFkThD7Wfg9g6NF_Ny_APrmtL1THlBwqGjuIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6444186749.mp4?token=kDVHeLTvzkD_aOO0_oqeG5i_3xWVKg56p1FYLekgI0CzYEHDjynoqzVdpvfeUVz_Rt0C26a-aqQdMrjcNB_hg6MKH4RaJEHrp1Jo-rAuN5dxlsziORp3rCKYfyi5KXYxBsiI-mQFuCGZYUFClxUdmjzXuhSBWRwfK4z7DFzjDEURQqUh5pE4U4dQP9m1ByYQx_6oX2m1WAKJL2chGuMqVtfUxj702rGnZOGZ0IM0TK_bkfbNQ0SFaWgchRPgu99FuEEhXXd780rJKgO3bmJoTBZghxtzOltMno_h4RWm24cdBXsuCcFkThD7Wfg9g6NF_Ny_APrmtL1THlBwqGjuIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
رسانه های اسرائیلی با انتشار این فیلم‌ نوشتن:
خیلیا فکر میکنن پرواز جنگنده‌های اسرائیلی بر فراز ایران خیلی سخت و طولانی و پرتنشه ولی کاملا برعکسه و زمان زیادیش شبیه پرواز هواپیماهای مسافربریه.
چون مراکز اطلاعاتی اسرائیل همواره مختصات پدافندها رو به اطلاع خلبانا میرسونن.
فیلمی از پرواز جنگنده های اسرائیل بر فراز آسمان تهران در زمان جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70091" target="_blank">📅 16:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70090">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxIQT7VLTdMmePS4bJliBLlHe0_LPD4A9zFIUgodNjqnvShp98wDHo5n_MXY5lPk3CI-6h67Kbagh3rrZvkmfYfArpMQRq_pxd4VJJXsLh44fJIEX-_e3kbCrYHtyQBv0l7qq4CbZdn2wQnJh7mGAqO51D7Z_SPymttyxXMDha5zYLx6aLcDzrQiHJ8qDArwPmozOVH3bmNVSoaWXIaJLt-bmVX_mLMl5KiY3I1sycb00TGKDe8Ru8F0M-Wc99EfLP-Norgix-mhsGeK0ZLQhE5T7R8THlyFoCXwRZT09EHUwqWMV8bdfoIEo1mYpkwkLk_vimt9tFHFJTPoqMcKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار باقرزاده: سه خلبان ایرانی توسط قطر به اسارت درآمده‌اند؛
فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح: ۳ خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند.
«جواد صالحی»، «عبدالمجید دشتیان» و «عمران به‌روشیان» از ۶ ماه پیش در اسارت نیروهای قطری هستند و دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این افراد با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
طبق کنوانسیون سوم ژنو، صلیب سرخ جهانی باید هرچه سریع‌تر با خلبانان ایرانی در قطر دیدار و درباره وضعیت سلامت آنان تحقیق کند و شرایط آزادی آن‌ها را فراهم آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70090" target="_blank">📅 15:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70088">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a18fbcabf.mp4?token=o4KEg8X697NtZzb8oLyHd9H9UWL8YAfSE6To6lOEf1G9TLiNc9DlTHsjgsFOVgY9ndM9UhlJG3iyE97VsAUkqMEaJdGA8HgHcxax0HAyQz3p_YeADlXM-x-vNXXVidtVkFN_IQj9OiNOt1HQKEHTJeMso6BJmw3LRUyqdgo0Ai5w0ItqzumG9vdlimn4OlBPgm7o24yl6ZDR9AckqJsIY9gRTMdvXkPEYc1o1TWEfhwOtMDpSMzHG1eI7q1IFc2V58h_k50YWby0W1CzsIzBG2ath1bpG0-ZAF9CfdWhkuoXOlYIXq2NzB1lRH_vixhXyz5XOJoCupAlVQcVqsMVdiQda-XCCdNKYF6tq2VUGt6jXcoPgUwb98zb6xr4a5YGgzE9bvWaLWEU4aDa3AogdjAL34UmoqcJO92QAi6_SAO4B_FdCiB7DpwmPjAGigJyJc3xMt7kAdCnoTKDnvLOvKFPcmkFnGYQ2vr7nLFSF-2xsMCQPFe0BILk112mUM6LvIDY17xu1y3m8Y3LepvWHMG7WMYVDhEWaIro2UgXo2dUiJ8ILGc6NjQfJKGb5DeAUmp--u_8pKBsioUS7Nba3UeZQ0DqJ3ec2Ws4jvhCFyYOuXeNEHLaTuMFfEU6TOH3uOapxNwkVYro3NzbOQx1JhG8JZbau7jWyoD-yXrCUVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a18fbcabf.mp4?token=o4KEg8X697NtZzb8oLyHd9H9UWL8YAfSE6To6lOEf1G9TLiNc9DlTHsjgsFOVgY9ndM9UhlJG3iyE97VsAUkqMEaJdGA8HgHcxax0HAyQz3p_YeADlXM-x-vNXXVidtVkFN_IQj9OiNOt1HQKEHTJeMso6BJmw3LRUyqdgo0Ai5w0ItqzumG9vdlimn4OlBPgm7o24yl6ZDR9AckqJsIY9gRTMdvXkPEYc1o1TWEfhwOtMDpSMzHG1eI7q1IFc2V58h_k50YWby0W1CzsIzBG2ath1bpG0-ZAF9CfdWhkuoXOlYIXq2NzB1lRH_vixhXyz5XOJoCupAlVQcVqsMVdiQda-XCCdNKYF6tq2VUGt6jXcoPgUwb98zb6xr4a5YGgzE9bvWaLWEU4aDa3AogdjAL34UmoqcJO92QAi6_SAO4B_FdCiB7DpwmPjAGigJyJc3xMt7kAdCnoTKDnvLOvKFPcmkFnGYQ2vr7nLFSF-2xsMCQPFe0BILk112mUM6LvIDY17xu1y3m8Y3LepvWHMG7WMYVDhEWaIro2UgXo2dUiJ8ILGc6NjQfJKGb5DeAUmp--u_8pKBsioUS7Nba3UeZQ0DqJ3ec2Ws4jvhCFyYOuXeNEHLaTuMFfEU6TOH3uOapxNwkVYro3NzbOQx1JhG8JZbau7jWyoD-yXrCUVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اجرای یه پسربچه ۱۲ ساله ایرانی از آهنگ ترکی «NAPIYOSUN MESELA» حسابی وایرال شد!
اجرای این پسربچه تو رسانه‌های خارجی، مخصوصاً ترکیه، کلی سر و صدا کرده و خیلی‌ها معتقدن حتی از نسخه اصلی آهنگ هم بهتر خونده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70088" target="_blank">📅 15:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70084">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPAYZAAC48jhLZ43qFtL-96RzloAr9WLjLYNK30ZoyoBDwaljGn1Ee9r2EXkawYcUzjANNxVvZfYxB7YpRrGi66CI7TS4_LtPIzFVeJFyu-SkRBZ2svsGQnYt474z5QOziZabrHXhdtzxXjks8FQbKTzkY_zKju1RAW1caQVpMkr3HixyoBTjHzAzK5OeZfHjV_Hi_vq2Ev855zdyEVhkILFvrwjKxV5Sh9awEjRoltGzw8eVTTSRkrlWpRElYtGkmnuVHSu_R-zJlyLlQAGDYLcLbyienKV9dkBilt1igcVCy6wJDYKPXFB8bIosB8lVVJGVzTJzYyQrbng4vB5xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596d386743.mp4?token=mBn0H7N-Rh2fwMIvKSa8pmAsjG1_DunIPp53dnZ81F8xrKLLoHbl0pblgbjtJGH4XAdQSBIzfxqxnAvo2k0-v86ZEUXcmT1eaRByusJJ2IcWmKWpf2SeiFHFRakTPX_bSChbaNaAKMVTnn1rJtQxsF0Hrob8LpnQERq4OcB_ynuzgVX9MwY-XM1p0BU3IqH1ngqszOPCUoBoQ9SHpU_QiuSYB57TxtODVxRtQJ76ILfTZIbvTQ_pyehIVGQ6_DmA_jdT-rvpfgM1489XqFqIiKMfA7HijY0GIJ9K1c_-Br2HPdzTJ5Oo8g25XxXuqvAL2yl2VWwBsp4t2fZ6VK6hkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596d386743.mp4?token=mBn0H7N-Rh2fwMIvKSa8pmAsjG1_DunIPp53dnZ81F8xrKLLoHbl0pblgbjtJGH4XAdQSBIzfxqxnAvo2k0-v86ZEUXcmT1eaRByusJJ2IcWmKWpf2SeiFHFRakTPX_bSChbaNaAKMVTnn1rJtQxsF0Hrob8LpnQERq4OcB_ynuzgVX9MwY-XM1p0BU3IqH1ngqszOPCUoBoQ9SHpU_QiuSYB57TxtODVxRtQJ76ILfTZIbvTQ_pyehIVGQ6_DmA_jdT-rvpfgM1489XqFqIiKMfA7HijY0GIJ9K1c_-Br2HPdzTJ5Oo8g25XxXuqvAL2yl2VWwBsp4t2fZ6VK6hkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70084" target="_blank">📅 14:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70083">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fbd8e1f85.mp4?token=X2k_MVGW76rv7GIFdWBvK2h7isaWo5LBMRlCSehTzxPPZ0HPOuqidUz4ijYTCSqmMORWN1VumJu6D3sb3_k6HxwMdgZhwBRMhAQol0yOCVjFJWWtUePRTRrBqdSCRLZ8meqfEnF-KZaP2xNADFv7mZNolIn-ofpvozIZlrTxf1MY1y03GYjQN6MybAKzNfhxDwn352XtvduuOQWdDamiX4xm8fWbe1UBMBFUd1fnhPacJsZt9rVRamtGpq7Xfd5hoR7LNTprVeGrU8L27mJaM1aLA7jrN5mF1mTYvpBwEL_RXjg-EqW-4J-TFEbNRwMQ-RejKZGAH5KIt3ipraCk1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fbd8e1f85.mp4?token=X2k_MVGW76rv7GIFdWBvK2h7isaWo5LBMRlCSehTzxPPZ0HPOuqidUz4ijYTCSqmMORWN1VumJu6D3sb3_k6HxwMdgZhwBRMhAQol0yOCVjFJWWtUePRTRrBqdSCRLZ8meqfEnF-KZaP2xNADFv7mZNolIn-ofpvozIZlrTxf1MY1y03GYjQN6MybAKzNfhxDwn352XtvduuOQWdDamiX4xm8fWbe1UBMBFUd1fnhPacJsZt9rVRamtGpq7Xfd5hoR7LNTprVeGrU8L27mJaM1aLA7jrN5mF1mTYvpBwEL_RXjg-EqW-4J-TFEbNRwMQ-RejKZGAH5KIt3ipraCk1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مم‌باقر قالیباف:
همون روز که به ضاحیه بیروت حمله شد همه چی لغو شد حتی مذاکرات
گفتم امشب اینطوری اینطوری اینطوری رژیم صهیونیستی رو خواهیم زد
اگه اونا جواب حمله مون رو بدن کل منطقه رو آتیش میکشیم
ترامپ اومد سریعا توییت زد محاصره لغو شد چرا چون ترسیده بود ولی دیدم زیرش نوشته تنگه هرمز باید باز بشه
به میانجی ها گفتم چنین چیزی نداریم‌اگه ترامپ این توییت رو پس نگیره دستور شلیک موشک ها رو میدم
درست بعد ۵۸ دقیقه ترامپ توییت رو ویرایش زد گفت تنگه طبق تفاهم نامه باز میشه نه بی قید و شرط
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70083" target="_blank">📅 13:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70081">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/98817f7767.mp4?token=WLXRMLgsS_gP6t_MU4-aqyuzogvfmSmEME2WmC92qO1t0Q5S5fPbZ5YxqVH5te9Mf6EpimR8UrYg6JLOutYKgs1y3fqjy7W3m4JTIUt57ScPFYcBYvHGLedpEkZl4i2eeffz_aw7p7ADl7BPDTuKNnbYAFTUd5fUxgbrmvVnm8hnsNO_T6KSwYeQuHkGJ6rg5mWawSpKXoa6WX8Vf2bqgT6ef3ZcFORwm0RCNofzNzth_tdSJXKoWZNwTHh7ZDNA3JFKqI5vMY48XvcGWPMH2NLFvl7TgKJ7Y82qK1cVMrvLlHPVM6BVXRzD2gztWpIBAMMwsP0CLGnvgHWbpwjv9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/98817f7767.mp4?token=WLXRMLgsS_gP6t_MU4-aqyuzogvfmSmEME2WmC92qO1t0Q5S5fPbZ5YxqVH5te9Mf6EpimR8UrYg6JLOutYKgs1y3fqjy7W3m4JTIUt57ScPFYcBYvHGLedpEkZl4i2eeffz_aw7p7ADl7BPDTuKNnbYAFTUd5fUxgbrmvVnm8hnsNO_T6KSwYeQuHkGJ6rg5mWawSpKXoa6WX8Vf2bqgT6ef3ZcFORwm0RCNofzNzth_tdSJXKoWZNwTHh7ZDNA3JFKqI5vMY48XvcGWPMH2NLFvl7TgKJ7Y82qK1cVMrvLlHPVM6BVXRzD2gztWpIBAMMwsP0CLGnvgHWbpwjv9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزرائیل این روزا تبدیل به کراش دخترا شده!
یه انیمه ساختن، عزرائیل میاد جون یه دختر کوچولو رو بگیره، اما تصمیم میگیره ببره پیش خودش و بزرگش کنه.
همه جوره ازش مراقبت میکنه، مثل یه ملکه بزرگش میکنه و میفرسته مدرسه و...
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70081" target="_blank">📅 13:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70080">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1ed49791.mp4?token=OtBtTyziXH6b0nXsEoRpSKjNez6J4sa5nllVTmC4btDKqctiscCULSK-45-i2bLDGsI85yWVN5SS0hDhSznoE5_wflrh64PbH6bhZnhsX8EQVQFdqHmzKxieQaOdr80vWStQPdDClGtZQqvQb2T8rh-_tGYEdVI-wzKLtk30ARmF8KeUdKxonVDzL1vIVpPcr-MecPdZnK8cN3GlgxK0SS0JrZbxMVn5smY7WJaC3k3FsbWlmAKuRztlwplhV_mAfaF3qCqHV5BLY6PnvvZND6bGJyNCJbGzLIb4upMzKbIBFrj2vz_1XhqgIKzwFg7BXICGxuPHglQc_8dIKTOCsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1ed49791.mp4?token=OtBtTyziXH6b0nXsEoRpSKjNez6J4sa5nllVTmC4btDKqctiscCULSK-45-i2bLDGsI85yWVN5SS0hDhSznoE5_wflrh64PbH6bhZnhsX8EQVQFdqHmzKxieQaOdr80vWStQPdDClGtZQqvQb2T8rh-_tGYEdVI-wzKLtk30ARmF8KeUdKxonVDzL1vIVpPcr-MecPdZnK8cN3GlgxK0SS0JrZbxMVn5smY7WJaC3k3FsbWlmAKuRztlwplhV_mAfaF3qCqHV5BLY6PnvvZND6bGJyNCJbGzLIb4upMzKbIBFrj2vz_1XhqgIKzwFg7BXICGxuPHglQc_8dIKTOCsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
با همه وجودم می‌گویم که برای من هیچ فرقی بین امام شهید و رهبر معظم انقلاب نیست؛ حکم، حکم ولایت و رهبری است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70080" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70077">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7suS_478yEZHTBbVA4C0eRESiCXzG5pf2njAPj1WNAijcowowUEaEub0xEBLwGeEeZBvBYyhvv0WjgqdUH1SgxvO9uhNyiBpd4v-WY86GqEMJVYU7at-5CSQLCfe4DWByW3yCCwtR8n0QpvUyHo6FwNHhq8nDJyRbndI3gNfGpsiPxBY5bMy2IzRh43KncMQVjxnqeOvGihU3lRwTHhpYGeF8fwpW4r1gfWHhRLTHyO4u1mKwiUJK1GmSMccxI49NeDHf3heaCr5KpN7DdZwEmcqq68rTQKhHogynNMBvSBJfbRFE66-UPLCSzIehv60_Jh3sk0Ds4Jhe2W8Fj15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTsEd5V3fFvBk8t2H8329JpW2Obp-wn_9TIW0T5sJCtwVep4-mpqChQmsGs81v79ZUocmxWfMNr2q7N6VxQ2aP1n_x7PGxW6VxEkHFqOmNu2fQPoyN8_XrEqecdLMgetCrVYQXU0GBlpc6RPb3AqaDt03W1svBLQwQw6FdJdxU0V9mogSCwnSIXzNaP2w1uzl1sy7kbrEakqZP7lWaejelWOIHaPgN7zq3t5MDAXrKp67MX7N4aKZavZvzLmzpa6lbaTTCLbHS5jfpbiA4sN2vRLhHjrAIlwfUsa8hcXfXdPR_Vc0NtB-s36jfx9lmmaCC2LTVKz6LzMBIV_jKOngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EpEE9qUHX9YRh3db51gYHHVMdmcRNf9MGfuJt6JJwvpCiefb4C9A4Cf4gkV91VNyxHdFcVQGlgOHB-zYotzxON6gV3J7b1xgFBKVhj2RuHg_vjOrwI6zFOnN9-_HVGxFbWagBLaldFFv0RtrnK_g7njEytTHiGpqQG_lUNQxw0DuJTW1PTT4lIQPAzB1HA8d405JPcaYzpxbogrvCEX3RtoR7rWeHCjeh1xfKGN3p2o-hvvzTdBr6Z3-ldTls_aE9xAChral8qDBS7mx3J2004QnlGaxEhdd47uzHLcRrS4hLsWxmP3yObh7nBPSUTSJL7nTwfGMGTcDk5ydYihTlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
〰️
❌
ناو هواپیمابر USS George Washington (CVN-73)
یو‌اس‌اس جورج واشنگتن یکی از ناوهای هواپیمابر هسته‌ای کلاس Nimitz نیروی دریایی آمریکا است و ششمین ناو این کلاس محسوب می‌شود. این ناو به نام اولین رئیس‌جمهور آمریکا، جورج واشنگتن، نام‌گذاری شده است.
🔴
مشخصات اصلی؛
کلاس: نیمیتز (Nimitz-class)
شماره بدنه: CVN-73
ورود به خدمت: ۴ ژوئیه ۱۹۹۲ �
طول: حدود ۳۳۳ متر
وزن جابه‌جایی: حدود ۱۰۰ هزار تن
پیشرانه: ۲ رآکتور هسته‌ای
سرعت: بیش از ۳۰ گره دریایی (حدود ۵۵ کیلومتر بر ساعت)
خدمه: حدود ۵۰۰۰ تا ۶۰۰۰ نفر
توان حمل هواگرد: معمولاً حدود ۷۰ تا ۹۰ هواپیما و بالگرد (بسته به مأموریت)
این ناو در عمل یک پایگاه هوایی متحرک روی دریا است؛ یعنی می‌تواند هزاران کیلومتر دور از خاک آمریکا، عملیات هوایی انجام دهد.
🔴
جنگنده‌ها و هواگردهای روی ناو
هواگردهای جورج واشنگتن توسط یک بال هوایی ناو (Carrier Air Wing) اداره می‌شوند. در سال‌های مختلف ترکیب این بال تغییر کرده است؛
جنگنده‌های ضربتی
1) F/A-18E/F Super Hornet
جنگنده اصلی تهاجمی ناو
توانایی حمل موشک‌های هوا‌به‌هوا و هوا‌به‌سطح
سرعت بالا و مناسب نبرد دریایی
اسکادران‌های معروفی که با جورج واشنگتن پرواز کرده‌اند:
VFA-102 "Diamondbacks"
VFA-27 "Royal Maces"
VFA-195 "Dambusters"
VFA-115 "Eagles"
2) F-35C Lightning II
در سال‌های اخیر، بال هوایی مرتبط با جورج واشنگتن به سمت استفاده از جنگنده نسل پنجم F-35C حرکت کرده است.
نیروی دریایی
ویژگی‌ها:
رادارگریزی
سنسورهای پیشرفته
توان حمله دقیق
3) EA-18G Growler
هواپیمای جنگ الکترونیک:
ایجاد اختلال در رادار دشمن
پشتیبانی از حملات هوایی
اسکادران:
VAQ-141 "Shadowhawks"
4) E-2D Hawkeye
هواپیمای هشدار زودهنگام:
دارای رادار بزرگ روی بدنه
کشف هواپیماها و موشک‌های دشمن از فاصله زیاد
اسکادران:
VAW-115 "Liberty Bells" (در دوره‌های مرتبط با CVW-5)
5) بالگردها
برای عملیات‌هایی مثل:
ضدزیردریایی
نجات خلبان
حمل تجهیزات
مدل‌ها:
MH-60R Seahawk
MH-60S Seahawk
اسکادران‌ها:
HSM-77
HSC-12
اسکادران‌های نمونه بال هوایی CVW-5 روی جورج واشنگتن
(ترکیب ممکن است با توجه به دوره زمانی تغییر کند)
VFA-102 — F/A-18F Super Hornet
VFA-115 — F/A-18E Super Hornet
VFA-27 — F/A-18E/F
VFA-195 — F/A-18E/F
VAQ-141 — EA-18G Growler
VAW-115 — E-2D Hawkeye
HSM-77 — MH-60R Seahawk
HSC-12 — MH-60S Seahawk
🔴
دو رآکتور هسته‌ای؛ بدون نیاز به سوخت‌گیری معمولی برای سال‌های طولانی
.
⚠️
این ناو به احتمال قوی جایگزین ناو (CVN-72)USS Abraham Lincolnخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70077" target="_blank">📅 12:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70076">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW84KW7a-AqDGykQN0OsKyNK7r25s0yWg07NOevekP8DE8RQ-b5j19ambB8BavyE1tieNVRWbnOPAs3j7XhP8vkTS3QIdi0mwWsnONtH5FiyVLi0fPwnI93qLjoj2BO_27iQz4XkOMyEVsE0aJq6gkocN-TkNCoTviIjF4kaemCZ0HFdZCDLVN_L6GcBfEzpI86hfAGGAU12AQ6NNdrRWhylYLDejE3RcYftjH9dbLrrFFvV9X32o23nNQ0XFW5s8_szDYasgRVmECihBAhubh3riEBAokGjQ6LPxaZqFEvyyXaFiMm_XRuoMBRjbrIpbu2pWYnFk02F2cjEoF1_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش تأیید شده‌ای مبنی بر برخورد یک پرتابه ناشناخته به بدنه یک کشتی فله‌بر دریافت کرده است. خدمه در سلامت گزارش شده‌اند، هیچ ارزیابی خسارتی گزارش نشده است و در حال حاضر تأثیر زیست‌محیطی آن مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70076" target="_blank">📅 11:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70075">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqnWrP1i1ebsLw4fKz4tX3JVOdt1SYzIe_GFH4E1ymOhozlcZ22GTseV1xA8C3UPNN6MWRg4yu2ba_lwS6KF9Z_n8e_FBDo54hsXQVNMdKkO3P6n_4ZRhpESxVUWvqa1PPFDSLuD8JeWda233AAVm9YevqO35V5EKx8HrWs_nxDkGQE_ZXdaTiQMmLQSk65X8XDeu8hUhfMcQ5Pmm0_mv29uMVsQhrKHONmcojYRDr3IotthmzB2LXulsJrc_SijWmCimcscLFnjPD3362R19yAw0IZK1IU9x99cLOqO7u9nY3m-iv2wV5i9o3dFlsP42baJi4TAuPq8rzONl5zNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
اکسیوس:دونالد ترامپ، رئیس‌جمهور آمریکا، در آستانه انتخابات ۲۷ اکتبر اسرائیل، بارها از اعلام حمایت صریح از بنیامین نتانیاهو، نخست‌وزیر اسرائیل، خودداری کرده است؛ این در حالی است که ائتلاف نتانیاهو در نظرسنجی‌ها از جناح مخالف عقب‌تر است و تنش‌ها میان این دو رهبر رو به افزایش است.
پیش‌بینی می‌شود ائتلاف نتانیاهو حدود ۴۹ تا ۵۳ کرسی به دست آورد که بسیار کمتر از ۶۱ کرسیِ مورد نیاز برای کسب اکثریت است، حال آنکه مجموع کرسی‌های احزاب مخالف بین ۶۷ تا ۷۰ کرسی برآورد می‌شود. همچنین در اکثر نظرسنجی‌ها، گادی آیزنکوت، رئیس پیشین ستاد کل ارتش اسرائیل، از نظر میزان محبوبیت از نتانیاهو پیشی گرفته است.
اختلاف‌نظر میان ترامپ و نتانیاهو بر سر مسائلی همچون ایران، غزه و لبنان افزایش یافته است. ترامپ از رهبر اسرائیل دل‌چرکین شده و در محافل خصوصی او را «بزرگ‌ترین دشمن خودش» توصیف کرده است.
آخرین مورد اختلاف آن‌ها مربوط به مخالفت علنی نتانیاهو با طرح ترامپ برای غزه و خلع سلاح حماس بود؛ هرچند نتانیاهو متعاقباً پذیرفت که به این طرح فرصتی بدهد و از شدت حملات اسرائیل بکاهد.
در همین حال، رقبای نتانیاهو از جمله آیزنکوت، نفتالی بنت و یائیر لاپید، از طریق کانال‌های غیررسمی پیام‌هایی به اطرافیان ترامپ ارسال کرده و از او خواسته‌اند که در انتخابات بی‌طرف بماند. ترامپ در هفته‌های اخیر چهار بار با این پرسش مواجه شده که آیا از نتانیاهو حمایت می‌کند یا خیر، اما هر بار از اعلام چنین حمایتی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70075" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70074">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70074" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70074" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70073">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPg63QS7HqR0v02CgBgBZIxDvRBefBjfvIZVSi6njFEhtKdANI0cqLPAlOqxx_Qg3wG2yBDzPJVwcTp7bB_KXRMC_1fdXP3J8yr17OPdbdwA3tdixlbqZK0JfCmC6w8Gf_tmURAwx3dW4301QOJgmNy5Y4Y1q7brtMgyOXyGIh9JrsVcBhmOV6NLo4xIz9rt6KN3kDKa9dF6SYtCAtdtJLmgyesCn-nTffkvSXXESEiejdVnOwLkmKx5QKdByzn9LdC7QFCvnagJAy8TBaC7KwrG_dCf7nmPcZyw5eVdXd8e6jFCJT9yVqTFmO9-iIuJ5kDx2xE_eBEOkhyW04LW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r24
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70073" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70072">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f783bdf6d2.mp4?token=HnP8wpvCR9FlenpBTJ3To6Yo_lwX1_Umm0HhJUKpoOO3a67BVUSHhiO8UdpX5ZDO9syyLo0BJZFffui9fnl4qfzja4sMN9bpiZwH5FDz5DSIDK2lFI_Fmz-PGN4YkmO0be7ESTqwtc5qnLs6X5591Yz9dqzhXQ4FhUHenLxOInYto6R1hlqSsdP5K4FjYHJPvbTwBLH6nPWy1h5tqMKfuE6zca33Zp-9vuHAS9T6fAivbp9Du6z3wdPXl7J5ZI6MJYynG_1tgPoiq6VZf09zDXXV6Jdpoakgxt5oZpAaHuphOP2_WER15mk-u9w_u4NzSUtAUCPaVqZW4QR1aizO6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f783bdf6d2.mp4?token=HnP8wpvCR9FlenpBTJ3To6Yo_lwX1_Umm0HhJUKpoOO3a67BVUSHhiO8UdpX5ZDO9syyLo0BJZFffui9fnl4qfzja4sMN9bpiZwH5FDz5DSIDK2lFI_Fmz-PGN4YkmO0be7ESTqwtc5qnLs6X5591Yz9dqzhXQ4FhUHenLxOInYto6R1hlqSsdP5K4FjYHJPvbTwBLH6nPWy1h5tqMKfuE6zca33Zp-9vuHAS9T6fAivbp9Du6z3wdPXl7J5ZI6MJYynG_1tgPoiq6VZf09zDXXV6Jdpoakgxt5oZpAaHuphOP2_WER15mk-u9w_u4NzSUtAUCPaVqZW4QR1aizO6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیروز تو محل دفن خامنه‌ای یکی اومد به ترامپ فحش بده، حراست زد دهنشو بست:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70072" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70071">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/59dbb77b21.mp4?token=MVa8fHRStJFXRd4TAsM6seOqaGoon0bOaZ0F7vQtFzlwIZUaK4HL7SNLpQx-taL1946bDEyXpCEzN66WWxEkBpZkX_yatmfGZnofPzNkyiU0EUQRhOO5YBKhK-Z1j--Z_PPAzzORfWexgFCa7Wo3ylWlpn3kWVpIUhroEdMfNxhepfQEDdk1kL--qbMsLWfv891Hsw1N_R6Pdr8rfJFb_F9Hgy_M4tPGzMz65JD147kfU7NMqoYQIzzcnWjIPuVfbOyVb9HhSBcv9a51-S3l50bUs8HTjkBouPJ2WICAtAZBgfpiQTxjD4MksdTy1ewQi5sCDQino2Afb9zSsYGgJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/59dbb77b21.mp4?token=MVa8fHRStJFXRd4TAsM6seOqaGoon0bOaZ0F7vQtFzlwIZUaK4HL7SNLpQx-taL1946bDEyXpCEzN66WWxEkBpZkX_yatmfGZnofPzNkyiU0EUQRhOO5YBKhK-Z1j--Z_PPAzzORfWexgFCa7Wo3ylWlpn3kWVpIUhroEdMfNxhepfQEDdk1kL--qbMsLWfv891Hsw1N_R6Pdr8rfJFb_F9Hgy_M4tPGzMz65JD147kfU7NMqoYQIzzcnWjIPuVfbOyVb9HhSBcv9a51-S3l50bUs8HTjkBouPJ2WICAtAZBgfpiQTxjD4MksdTy1ewQi5sCDQino2Afb9zSsYGgJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهارتا دختر یه سفره سه روزه رفتن شمال، حالا چقدر خرج کرده باشن خوبه؟
۵۸ میلیون تومن ناقابل
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70071" target="_blank">📅 10:34 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
