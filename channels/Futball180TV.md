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
<img src="https://cdn5.telesco.pe/file/eRSeeeySrNGfWjrabe7o3KWU7ceNymieZ__s1q_MOjfO42DGhv6rqap40I4-myINheI013Le5g0HGYxVXBPC-9Qb14N0InbWd_HWgOqqbYVIszmJXkX-E4rQX2Ge7-hrNTzO4BGJklD8c3BDBS8RQh45b8BhH4j1KHeW4s08DSt3pq09w03rkcd7HLct2eoI3b0bOGk4bQEUvgxfVsthWExpvO7kb7-JDWE84uzHvPD3wy7VU2Y0zMe_CJcPEWkx-LXo765A4ZsTforpfSVV9MA3KAGZvVVrsUKD6p-G7T9yqyTRbP67iOmSfYe6dVm-i5xWfdA_dEpr4HzcKDJlCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 407K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-106934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">برررررریم سراغ دربی حساس مادریددددد</div>
<div class="tg-footer">👁️ 484 · <a href="https://t.me/Futball180TV/106934" target="_blank">📅 17:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUs95whhT5D3GVmL544FIGpL1IellY8fmR-OX9_M3BFYm_8Q0n4IDmsrueva-fiaGSfxAWQBBB2xPiS0QATL_oiMeuqGffNKxtzeY_7KDH0pdGrBHCBgii_i6SS4fDhBl9dejYiWhK3_Y-K4tJj5x0L1nXBzk7tF1ZiH06Kb-Fk1GBB9n3jOOlC3UYGcbHFj3rju2qZ6IvZ558BY0dr3H_dc0Z0dkPTObccvoK-AhYHTOzMgybEfPekTczkA8boCGTA0U__jE7fzRQ-lMVX61U8kN9U83LF8Dsi61LdJRIsO6ik5OxFUE0CHi_oacsUlspQ89QtBDlf1U_6wMtRdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhV3KKWvIln2XvnymP5wvK3W6_tjfpfFjRbHT3HUgBaVky_RNB3RTLgZuFwN9h8tNATSObo8dKRLveXaAEroZY7g8CIVJEEfEjB5BhXPG8vXiAN8eN1VVM-1bqJy1murh6WNtmnyqIrnmvAaby_YTkLCYUMKf76AAHeHAAshZAAQ64V6wNDbW5BJj2ntoSQxZkkA2UDqJzZkZdnsLDVO9vEZXo9Z9HHZVgCtvi49lUuUlKEN_yWQuZsObPZAS4AzzWBooTyxvVETAwvCujy_5A96S7lHYG1K1mGt8tOmXwvpzcISiFsgWLSbcNxsJOQo4jLNC639FpCN15KOWmrTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
ترکیب دو تیم رئال مادرید و اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/106932" target="_blank">📅 16:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=fZaSs0GoahiUdKUfBBhWGsWDX3hAA8z3n7nlUq4nFLgGcruvlf4xJNDhwmEkiQPr5l82059uzJAQitSb5TLY25A0DsMxvH5aU4J2ejsf2w3CvFF9R3naWdRwG5XC4PzKIwNcyGQAfGMEiqY_oKH8_50BTcmc5zEVyTOL51gtGC9G_3_ZZEMuQLO0iZiiINJJXHCiUCMVOoDbueIgny_MEl7rXMU58LAdhJuCs3qDkpJ6zXw2J1JCq01eI0maR1uq-J8PXLR1kXnuC9dDxPzR3WIFp43wWldtPzGABEYHwC7XdNFzhYVHHFvgUULDTzUp4-_rr84qERc2fdAKiYbP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=fZaSs0GoahiUdKUfBBhWGsWDX3hAA8z3n7nlUq4nFLgGcruvlf4xJNDhwmEkiQPr5l82059uzJAQitSb5TLY25A0DsMxvH5aU4J2ejsf2w3CvFF9R3naWdRwG5XC4PzKIwNcyGQAfGMEiqY_oKH8_50BTcmc5zEVyTOL51gtGC9G_3_ZZEMuQLO0iZiiINJJXHCiUCMVOoDbueIgny_MEl7rXMU58LAdhJuCs3qDkpJ6zXw2J1JCq01eI0maR1uq-J8PXLR1kXnuC9dDxPzR3WIFp43wWldtPzGABEYHwC7XdNFzhYVHHFvgUULDTzUp4-_rr84qERc2fdAKiYbP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
دوباره از ایتالیا صدای گرگ میاد.
🔥
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/Futball180TV/106931" target="_blank">📅 16:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=LujImQncATJxsDas9QTaJJTaQH1Nh7dLtUomBa35QfgzqAFxUh-CKHOpmX6o35co6PgfiprmpEgM8pOInYVAjzdNN55moVNJ9Pm2Ml0I71XQrZNecJyj2nokHSkMs4XviIbk8ZnkNl2D7crg9y6Mu56Me-ekXZa1VndNovFckaA26lyxA_65Cn4cSlYDVYfm5khgxw3hrXT2LvSj3FgGpkxFyDn-kjS9WPcGvfPbj-jjY-Uf_SLCEvDKFR3z1qdF0ukaK4MhT7_RxawzYull2Sabo-IBIOA7wpszqv1DOMKAVoLADYUP7QNQ7HXLHb9rStPQ6LzSplWkW1p-gABaJoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=LujImQncATJxsDas9QTaJJTaQH1Nh7dLtUomBa35QfgzqAFxUh-CKHOpmX6o35co6PgfiprmpEgM8pOInYVAjzdNN55moVNJ9Pm2Ml0I71XQrZNecJyj2nokHSkMs4XviIbk8ZnkNl2D7crg9y6Mu56Me-ekXZa1VndNovFckaA26lyxA_65Cn4cSlYDVYfm5khgxw3hrXT2LvSj3FgGpkxFyDn-kjS9WPcGvfPbj-jjY-Uf_SLCEvDKFR3z1qdF0ukaK4MhT7_RxawzYull2Sabo-IBIOA7wpszqv1DOMKAVoLADYUP7QNQ7HXLHb9rStPQ6LzSplWkW1p-gABaJoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
بغض ایراندوست از طلسمی که شکست
پدر و خواهران مریم ایراندوست در ورزشگاه، برای اولین‌بار؛ خانواده‌ای که بالاخره برای یک بازی زنان دور هم جمع شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/106930" target="_blank">📅 15:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=LYXFg4tyxwWZjdshWNIiEXuGlryB6cTWcNlesOUbU6t0WlrnBQHK6O9dWXnWPVRvlcLkppsZql7aik90ZSkMO7qt7skBb7n04eTpy9lJHfgQQwfJVHzDa1XlEjioRzYAxITNyGNZ-2408JV-OJChnB1X6ANOj0fH8XEBeB_KS3EgxrWTdwXq8izA0bTiLhkxGXFVCH5va4rPpAhxKMp-9V0S4JHp8DD5xfHGxQYK3wlSektow3Jo82pwOC-cV2URRrnhcQO0EmoCyv_Xypk-vLxXH_w29Ld350eWVplimxPvOlReXgryW9wu0o4B1MReKBJqehhNFEc7EogwfeGVdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=LYXFg4tyxwWZjdshWNIiEXuGlryB6cTWcNlesOUbU6t0WlrnBQHK6O9dWXnWPVRvlcLkppsZql7aik90ZSkMO7qt7skBb7n04eTpy9lJHfgQQwfJVHzDa1XlEjioRzYAxITNyGNZ-2408JV-OJChnB1X6ANOj0fH8XEBeB_KS3EgxrWTdwXq8izA0bTiLhkxGXFVCH5va4rPpAhxKMp-9V0S4JHp8DD5xfHGxQYK3wlSektow3Jo82pwOC-cV2URRrnhcQO0EmoCyv_Xypk-vLxXH_w29Ld350eWVplimxPvOlReXgryW9wu0o4B1MReKBJqehhNFEc7EogwfeGVdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
🇮🇷
فرشید اسماعیلی: یک‌زمانی در زمان رویانیان در آستانه حضور در پرسپولیس بودم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106929" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P15GtKUD0HvUTmdzT7M4lIOTGksS0bRRBCgSCO7L9eEsAWfSanO5fVOIWJHcsrk-ej_vkqaIhftDkpmRMBMApe8T9ayU7biIp52qhXLOqCYSk7f6f_0mzsIsdk9xRMWnKhdDkOyAOwJSViD4ZYgZOWkah1PcADqWOr32DGsheuEIVZa5lg0iFO_i08emMAwcLzDn2hZvObaw_Du2zR7wSJ3XBect9wkTUHrlWNRD9EeAz72PAOKXT7NshBD4n-INXFHl8pvPdOusmP7taJGGH1kKR1C6WQn_DUiQLohfYQKLZM7qie6IyGj39Z1LgnBGpNB7QpjVLVeSrYfzB6s54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشون زید دیومانده هستن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106928" target="_blank">📅 13:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=JhoYQtNv8GcS_9jNrTW6qtwmha6zqXY1wi4uIqCXy8vY89iXtCYGPFb0BRm5WK6QaB-s7IYdVt5Jwg6vo2EGDQaSwQ_ql8usuCod2yoS3QK3ItqRph9_-krOixB_6vpWzNYtpdl3n-jkcXpQHBEehTk7DPoQl1YWEk7uFqNT7kQGtxShxc03MQ3XzqHLd4nRKc7DCf70BjMoi7ZneDRk7ZXCCEvhWodRN7iLc4FudMFLgaPG97ZwEq8rJPDkj99VLAZwpz1RZA0odZTanuPSRrJP0j9Q1eL5plFErCpnsWMqElsp59xXEmuUtq5bBxT8Qa7VkBF2-MLrHEX0aFdqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=JhoYQtNv8GcS_9jNrTW6qtwmha6zqXY1wi4uIqCXy8vY89iXtCYGPFb0BRm5WK6QaB-s7IYdVt5Jwg6vo2EGDQaSwQ_ql8usuCod2yoS3QK3ItqRph9_-krOixB_6vpWzNYtpdl3n-jkcXpQHBEehTk7DPoQl1YWEk7uFqNT7kQGtxShxc03MQ3XzqHLd4nRKc7DCf70BjMoi7ZneDRk7ZXCCEvhWodRN7iLc4FudMFLgaPG97ZwEq8rJPDkj99VLAZwpz1RZA0odZTanuPSRrJP0j9Q1eL5plFErCpnsWMqElsp59xXEmuUtq5bBxT8Qa7VkBF2-MLrHEX0aFdqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رختکن چلسی بعد باخت جلو برنتفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106927" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=ETF9-mpnCwieix9wbTmewedhxmAlH_ouDkwn6XydJbErHXhjcBguJQLjdp0xM-yCOB1meT3Rxz6ySz2mg4961UpTAYToDc740-Lv8ru0wWDC21Yr60brlIqnjo216A96RyFAml-U_gehlhzMEw0KqRQP12dwmNEM8dJ9TmqvXOaPH30G0_XB6Iu-m4YrB6EJobxp_7z2qsZYndu_4tpzA_1gE_t6HTS90FBKMX-cZScSAkdUrLNdl_MRYHrCUgSXbZZ3iGr9zyHtVbHWZl7raszNYsAGeMvIpb-MSszMGmsohNojpoPLxMouwA9QG9FjWj8-1FuWjhc1ZRcgd-0KaEUQx0tDl12YLYyo9G0I6AIctL4nHylfMl4tVTuS_cBlNgPYqPeXdLjsQ1v7zO6FOID2rrdrl2erCSV6ISWzXEvAADQWwAvlrOmvcs8WCd9ejGgDOGp3macPFGpsXXxknOTWF-UiLFV8pL5WqatvIr48kyUaoRjrEpICQsy786H_VjDxhQYyml2ti_UYO1EBZCQnHLgaoEpHb_aCrfwZK6OhpjaojmZzLGGLkHI78Eps4EbJez9UDmxlJQ4PN3kvrExK8z9lhWoj877lJjbgUG1oM-vJ2fX-C0of7MPF7CP-1_N84OvkcW8MYjEVUma2nqVx07vKCtBu56CfVI6UDR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=ETF9-mpnCwieix9wbTmewedhxmAlH_ouDkwn6XydJbErHXhjcBguJQLjdp0xM-yCOB1meT3Rxz6ySz2mg4961UpTAYToDc740-Lv8ru0wWDC21Yr60brlIqnjo216A96RyFAml-U_gehlhzMEw0KqRQP12dwmNEM8dJ9TmqvXOaPH30G0_XB6Iu-m4YrB6EJobxp_7z2qsZYndu_4tpzA_1gE_t6HTS90FBKMX-cZScSAkdUrLNdl_MRYHrCUgSXbZZ3iGr9zyHtVbHWZl7raszNYsAGeMvIpb-MSszMGmsohNojpoPLxMouwA9QG9FjWj8-1FuWjhc1ZRcgd-0KaEUQx0tDl12YLYyo9G0I6AIctL4nHylfMl4tVTuS_cBlNgPYqPeXdLjsQ1v7zO6FOID2rrdrl2erCSV6ISWzXEvAADQWwAvlrOmvcs8WCd9ejGgDOGp3macPFGpsXXxknOTWF-UiLFV8pL5WqatvIr48kyUaoRjrEpICQsy786H_VjDxhQYyml2ti_UYO1EBZCQnHLgaoEpHb_aCrfwZK6OhpjaojmZzLGGLkHI78Eps4EbJez9UDmxlJQ4PN3kvrExK8z9lhWoj877lJjbgUG1oM-vJ2fX-C0of7MPF7CP-1_N84OvkcW8MYjEVUma2nqVx07vKCtBu56CfVI6UDR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اقدام عجیب و جنجالی سیگار کشیدن مجید واشقانی با اردشیر رستمی در برنامه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106926" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1S4Iw_slfXumC44s0F5NrewQFjcTfHDpRtFwEOHoVg7bYxOzAfroQ55pT2yJqcCiMFWyMnhb3HUG2btbfNXO3pOeZq-Miq8pGqsJTJ2xVzjCYKMxK6waqy5QqEsTI5Pax8gdO8nURWyaJpEAvsGHLuTwnpV8iBe6U1Tqv8MWxb_9EpOAcTd5lTn8CTNcTERZOo4CrBbTDn6uxfkCE5lRuoARt7aPTrEYOBcKyxpVxD0A9-W7UBkQ-ToqtB9szjPy1qXUCeZeNfZphBofM5J_JeRIXUO9DRUBS6ltynF00aB1T459Hcfr-aE1xTYUwkFZ2E4L_DtCzK7g9Kes6huGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106925" target="_blank">📅 10:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز متفاوت و جذاب از تاتنهام که برخلاف نتایجش، فوتبال نسبتا خوبی ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106924" target="_blank">📅 09:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=T60kH4uVgFNqSyp6D19b9dEVbmpDWvjqL20fyi16nIHzXusKHMzRK5db3EnZG1vvaumvIFrHuiT9OveX22Q_SOM54iF-RewsgNNLrrli0anwkrKzZwGuB053hzARZmQSh609VGn5uiIq6F6_w4hU-knLHD8ujc61aqbPzPTkieTgKuFXBIU-ymRFkC3HB9pZhAkRIuhlFA9-tEO1tKZEsHHi4wavZdvKGB499Ie2UB0ySSVfFMlWh8TFb_Up89EnwFTNRYM54BzaP0Xb8uuZcVzVFsykSn78EACWLXAACM4B88id8zBDZxpGpQTdQIYzxFbOZd6E6LvBOoEHsSzAlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=T60kH4uVgFNqSyp6D19b9dEVbmpDWvjqL20fyi16nIHzXusKHMzRK5db3EnZG1vvaumvIFrHuiT9OveX22Q_SOM54iF-RewsgNNLrrli0anwkrKzZwGuB053hzARZmQSh609VGn5uiIq6F6_w4hU-knLHD8ujc61aqbPzPTkieTgKuFXBIU-ymRFkC3HB9pZhAkRIuhlFA9-tEO1tKZEsHHi4wavZdvKGB499Ie2UB0ySSVfFMlWh8TFb_Up89EnwFTNRYM54BzaP0Xb8uuZcVzVFsykSn78EACWLXAACM4B88id8zBDZxpGpQTdQIYzxFbOZd6E6LvBOoEHsSzAlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😢
جوآنا ویتژیک ورزشکار ایتالیایی در مسابقات چین یهو وسط کار اسهال میشه و بی‌اختیار ازش خارج میشه اما با این وجود مسابقه رو ادامه میده و قهرمان میشه. در نهایت از مردم عذرخواهی کرده و گفته امتیازاتی که گرفته رو ازش صرف نظر میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106923" target="_blank">📅 09:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106922" target="_blank">📅 01:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNggQyWyHlEyUiSuL6gVNQmdaaeTcYvRwwEDK9BqVAFZyxQfNomWhP8B5iu147aHwzJz0qrUQPCNRbZFmegJyGBoRPZeaIWQujrYPwgPdDTOosJYFVUuZ1rR5AkifXcdco0imGyD_8EsKS8cALxgK6xbeJbzl7vX5yrqosZw2jq9oWm8VbIDocCPo0VIyiANQYjVqxjrsUyBVRG57kturJR-xtlEaeu_Fthx-f4KLY2QVAipWU9qgpXLDsZO0uffHme7Pzfnp1ufeA1aSIT3plokITRRff5qvCSVQzekLPC-3CCNuG2GnR4JJaVXg8BWUTtbquhbk72NsMGKtupFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106921" target="_blank">📅 01:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571388041d.mp4?token=m1N37iKAjZKT-ctbA2B8bjKuBStgMF9zuvAbMzoxsJ3NYtn6iob2r0YHrDK17-rTik6kcMw2_qSKthJGsOrB250UON3aHD-PezeBSojRmtp5D1cvN28qrIxN0wnpQTDVicbtXHk6SX3beQaX3tmROHA5QlFpsrQyB396lbb65I7hf5scytrvu7U_tnTkb7vt0UlA8Zq9F3wSrqlOhpFPeW7lUAVSUAtNUcPamEAzJQq3FKbZGqMLfiQWJ8ueBCp2rqatE81zzYmRDQ1gFsjad_2CwJ-DflpVfKtmI2Ut8ectowAesvrJhnr_qG_YGAnBAP_164NMecGKW96wjZIrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571388041d.mp4?token=m1N37iKAjZKT-ctbA2B8bjKuBStgMF9zuvAbMzoxsJ3NYtn6iob2r0YHrDK17-rTik6kcMw2_qSKthJGsOrB250UON3aHD-PezeBSojRmtp5D1cvN28qrIxN0wnpQTDVicbtXHk6SX3beQaX3tmROHA5QlFpsrQyB396lbb65I7hf5scytrvu7U_tnTkb7vt0UlA8Zq9F3wSrqlOhpFPeW7lUAVSUAtNUcPamEAzJQq3FKbZGqMLfiQWJ8ueBCp2rqatE81zzYmRDQ1gFsjad_2CwJ-DflpVfKtmI2Ut8ectowAesvrJhnr_qG_YGAnBAP_164NMecGKW96wjZIrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
کار جدید حمید سحری از برد امشب بارسا: واقعا کی میخواد جلوی این بارسا رو بگیره؟
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106920" target="_blank">📅 01:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106919">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iitqhZeAqWIL7H_KMOnmjdmZ3fEaet__KvmJS1KyvjQBe1KktfUtty1hCqq_UemIK1gMmUm99c4WTA5Wr6jm9lj07YV1dcBfJmwkyUUUsNJG4XuKDah0AQ9XnI9OjcnL9UOnB7k6LwC176CK-AZGZ5ZIYkLxT1ecOsdo_tcoGai3QYFwF13-rzRFsJ8ZVpnk2je6WSDWF9qFRW7qC9q19HcmM0ulCvoc0oGzz0FX3LH3IO7E0Pd32PVsl8JBNhft1aIJvRwrYpFurLJt0tMPgcJQN0CXqRdPUGa0um8XzjlIjLSIK_gI8LwCNaY3HgoSb0XecLklsVg4dYZ8wucZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106919" target="_blank">📅 01:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106918">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwoqs_iI-79DrxjjnDtZ3mLVFQ_C5hfc_nlfxsCnqMI6Ck-RJa7adSvAxejqH8Vl5Ik75_J8K2HWuSynizQWiFipwHXgutceLapuuANsZfN6whWOab_i73e_rrkUq02xRnSVrAH9fe23n0olu3RoeA467QoA0yHT1VyDhZONKG8awq_vKbUJySAWfTP0PkvD4H0nGhvURfA7uVND4JnGPeoh50i5kAlleP5eWMs8Ml76rHGjXEb9B_Gcl-jjHyxSj9yAROLtcInmD6-BFarF-OMEr0MUb1n3tAW2UTTdg2OFePYis5v5dZD5iOn9HUhWbwFcEnvZfIUG6-eQonz2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇪🇸
هانسی‌فلیک: شگفت‌زدگی بابت عملکرد رافینیا؟ بله من شگفت‌زده شدم اما نه امروز بلکه دو سال پیش و هنگام اولین تمرین با این بازیکن. او و لامین دو عنصر فوق‌العاده تیم ما هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106918" target="_blank">📅 00:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106917">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxuVVLkRzcX3ijjOENM1cJ1UlJ1L6Vo_hUOUrg81cA3_u-d3tZDWmC7ocpPg4OuLBTvdjQ2Qk9GJjWqa1C3sSAWlZpMRiFXWGxzvQ0VoYqesmg8Lp5TfPLra_iGf3drEKFem4LuWrnDTKaaRSXFp6Ai6PsRlrGNxqminchyXBwEqgCrlbO70OT_NXZ3AwQW5N546ZxrJqJO3ft8POve-3KIe3pArT_fDITdD9ktxJ4zyYc8MYtlOOjmtLSKWpCsUJfDjwGBahv_dwoIptgrqjjAUlRWM3RlSzZ9SBjIO2xHLRSPLBpLUbAAe92zWDdYW12zQtFg1qIq30OVe4IAPsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد بارسلونا از شروع‌فصل تا امروز؛ بازی بعدی تیم وحشی فلیک ۲۰ روز دیگه مقابل ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106917" target="_blank">📅 00:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106916">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnUR6Y4X_iynVwb0WEWyzDD0lpgme0PZS8qaaw4FVBGjNKQJl1V8Wh3Z6H8Lswg0VdEwZ7X7Nr9x3ehhDoP0a6we2KScQ2h7RHR-Idn3a6OZXXqdJjJhoZ5PDr32VnWBdpfNJ-x4Jg9bjvd-BM-0Z4ND6faF0rBHQJZimVhSF2cFNozIbexYTERe3G3P_XopgInwE7z0oNddl8snbP1c3pZ0mo-W3fGpp3-z8WcUaWWR3uJ_maoqj6UTRcyRkMpCcV2Gx71_fEt-vw1P5S00abcyppjYJv4ebMbzedT3kV-ZLf05XNI29BiF-JI6_4mz1jGOCmeejasy1HpTIpyc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
هفته‌هفتم لالیگا اسپانیا|یکه‌تازی غایب بزرگ بالندور در این‌فصل اروپا؛ بارسلونا با هتریک کاپیتان رافینیا در جهنم خانگی سویا برنده شد
🇪🇸
بارسلونا
😆
-
😃
سویا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106916" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106915">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCmLAhIwuF2UKEfLAoM4BEwQWXH_b-UZUWjikJv0Rs0-Z6G0_0fDSOFa7zC6xfN2jQg6lE58TmVWUWqLwqbt0KJGdrj2_VNkY3-pyCPbo2NA71f0Q1_xHXrSUq-8gF-G1ffodHDpSUVIa39mK45VTY9FyRvLzvCwKWMFBvBSxepFuGz_aI08Ey_cKME8880ywb7vuic0Xa_4QnRU1SJmJoLVQuWTjrgtKh6Yukgzw6VBD3Q_ensnxaNa03jofvnCrjCqribI8kywsmpRGMgGqnv34nMtGvU5Pod-LsuRQnJ2_rnoBEumm3C2c9FVvsfVF0YvVpx8VEnDF6Y87CKJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
😳
😳
😳
🔥
🔥
🔥
🔥
🥶
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106915" target="_blank">📅 00:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106914">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Govy1_SgFGvkumRjJvsfQXntfChtyseBKPyd74-1QpvYQ-jtjXEB2mJGrDAtY4YIdWHLL5oJFHmuSW-L0NZdS3iUhcMnNpl6S_7CkBmwbDNses-a-3G-L12s2iw7RzwpQd222a_HkscC6Fl_JezDIQEXY5Q2vqb0ld-NzamNByEGDzgycMfVi5_Q4Iokgx1aGjNg-ugwduZ5pU8w51Bs6JGNGBqjs4bMrOT9t3rkLfRRzmTqQAMYU305yaaavYY5lsl6Stm6t4TRcZukL45sQ6wJOmBy6Y3UKxNO1qQ5KV2xrBkohcb9f0OzF5PPK-EqejEJoMbXNDzma0We1wpRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106914" target="_blank">📅 00:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106913">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCgQKh7g8MMhzLFpyuvtZnVU8T_RohyvRxoXUS4hdVoWVUdmeXHHeBBm4D_g_7msNHjucC2cV7NJ2kgrU15NjytYNcPmKZReIPiJURzzAJajteQAt_8iP2mtEXp1IhlClSibf73XlpjdzV015239THeryDpYPpgnnLTs-d677-F1xH8DbL0jVoD8GpANDjwzCfoBE1F0Br4nIRTespROx6ZcCTxYvxQt6IKY2_ZynTJOoCEtQ8uNFVlQMwG8iEVh8NpCnCxB1q69eZYEaklJKszOhJtjsbDhtq4SaILdNIpX9foDEWQwRLiW-LUSlamfDbQ3MnaTJskuOsz7vVj_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106913" target="_blank">📅 00:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106912">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چه پاس گلی یامال داد
😐
😐
😐
😐
😳
😳</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106912" target="_blank">📅 00:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106911">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چه چیپ سکسی زدددددددد
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106911" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هتریک رافینیااااااااا
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106910" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106909">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106909" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106908">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=ST19CnnTFZzaZUy5CK1UZwosEoA8OjTy6nyrLkUSNBHW5xnBzOOPDxAYJkMuyFfnQjSOy0bmLvWww1pZwZ4zz5X0Tm8ODK32iLACgtPkS1pLOuv2b2O8wC0tIzDWkhJH-6jEbHuCrkSIYaHc17wTVnPuVjF-hV_eezFWkA3aFkbNWZvQCwwsAPpmZeyU4PhES0bunkJTEfpYEfNw_9P_sG1bUTdHO4ndDIeJ0xGYqSBUEjyqHrG6J2Df9PPKrdwKLySrh4gGL7jHmZXrdYs6EsNHaarcYgobhIVLyTu167ULiHTaXxIl78eS7-kMO0n4rupwvkTzmyDmfivTnEYI_yNpXmgenc4zl0sYHaAzh4dJbDNHefdQhjkCVf7bpdH-Yp9Ko9VSjKdoJPR1ToeWlxS0ViztD8oNdWUdG0xcrrnU1PeULujEmwTRBLfws0C0oElU2zvMY9aZiYNBQ9HueTRNPYaeFLmL7wfAZE6JICEd_LRj30nbNsJi175gGNQNAAGd_W43mdbQP0wRhGovdMYahKb2QnZ1HpJ8h3cHStFO16QTFsES42TtZ3x1DhsJpOns9f5VhHIkx9mAA273GOTdjrkAEBFhWy8GIfJtvfosU9hHnFcjWVzCp2upXlTvCkaT_sS1mQ79Ad4gS4f2fUjT-A9vsl8Evdc-LeSW3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=ST19CnnTFZzaZUy5CK1UZwosEoA8OjTy6nyrLkUSNBHW5xnBzOOPDxAYJkMuyFfnQjSOy0bmLvWww1pZwZ4zz5X0Tm8ODK32iLACgtPkS1pLOuv2b2O8wC0tIzDWkhJH-6jEbHuCrkSIYaHc17wTVnPuVjF-hV_eezFWkA3aFkbNWZvQCwwsAPpmZeyU4PhES0bunkJTEfpYEfNw_9P_sG1bUTdHO4ndDIeJ0xGYqSBUEjyqHrG6J2Df9PPKrdwKLySrh4gGL7jHmZXrdYs6EsNHaarcYgobhIVLyTu167ULiHTaXxIl78eS7-kMO0n4rupwvkTzmyDmfivTnEYI_yNpXmgenc4zl0sYHaAzh4dJbDNHefdQhjkCVf7bpdH-Yp9Ko9VSjKdoJPR1ToeWlxS0ViztD8oNdWUdG0xcrrnU1PeULujEmwTRBLfws0C0oElU2zvMY9aZiYNBQ9HueTRNPYaeFLmL7wfAZE6JICEd_LRj30nbNsJi175gGNQNAAGd_W43mdbQP0wRhGovdMYahKb2QnZ1HpJ8h3cHStFO16QTFsES42TtZ3x1DhsJpOns9f5VhHIkx9mAA273GOTdjrkAEBFhWy8GIfJtvfosU9hHnFcjWVzCp2upXlTvCkaT_sS1mQ79Ad4gS4f2fUjT-A9vsl8Evdc-LeSW3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا توسط رافینیا با پاس یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106908" target="_blank">📅 23:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106907">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رافینیاااااا دبل کرددددددددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106907" target="_blank">📅 23:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106906">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلگلگگلگلگگلگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106906" target="_blank">📅 23:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106905">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoFnbas6Ion6k_QIntLDPFx1hO6tuDfuqyeiWa3ky50M5RuTXYZzhpRrajbNYN2vENC9lq8ecQE3WsEFiAw1p24rilDZfNHwwubLLGyPFGtbfPFs_UHUOh_wALNEQHudlMQ3X5lS-dzEYrHy_gXyqtkSny5up43Shth8l5xFvHNDoO7Jp4v3MRXkgDbrN2dgYJunDNkbDZGD7s-Cd7YyybJizJbM0d1ird2RNs9d4ds6EFuudsLDVhu0euDH6E_GywOtnsikS2V8GLmkOh-aK3HGl1Ll7OgIaBqfxxqFfXxOkJ3-BKSqqceZy_H6pPHbvm_kAXH_o0TInPakK7wt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید زلفی و نیما تاجیک ۲ گزارشگر مطرح و باسابقه تلویزیون به پلتفرم اینترنتی نماوا اسپورت پیوستند و از تلویزیون کناره گیری کردند. پیش تر محمدرضا احمدی هم از تلوزیون کناره گیری کرده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106905" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e51312166.mp4?token=RXxvGg-HLyyARdktzuHd-hyBn5NqwiXAe5Foe-T19U720VfENo8h2vBAmnq4NP2kk2ydRSIzkVyqcjumnUb6MsHRbOGnf_q2esL5Yx8vhSpR-1LsqBB1wjcDJEYRFUKSEubv1C_qSt44Hh-gyt758bFUxbjfnveiYLx8VubMWeItX0jv8FapKQ9m_o1qAqOEsNjjE7h0Yvdv_byy-gTBRrwu9ewz3SNLNIH8zNNJ9EiflxRpBFPJfuyfa5X-gnQqY-KOluwmgNYOho5XIyxxgEl86x41jN12skeJMoeEgHyaP6DHLIY3Ir4O5kTJqbOy3UvtH29gT66a78SqsVV3omtuSd9lW2HKtv2cb6y-5YBSeaplbjA0ypeXKz088BkNYB5fYCY1INhpYZ6Ixow6euhCBBIrGav7tSJ-o0wAc5Wg6SyDkhS6knxE4dw0jtppnbgSnqFUQrxOTOR6QNu2D_fHfJzZPlWDDpf_CC1DD9_veY8pqHCVidi82df_PtGS6MiS_qU6oqA4sPju3jmNOVBpdzo19FleeNcOi-_Chf7AJpjj_JSP8980GBNdsBh2KrXKy-3TQUIJd7K3PxqYz9xL-XB3dMC7Xl7KxV8zcIma3ZUwBLnESZxH7yayZ0bOxsIRZcNsioQdvYKsEjaPbbeh42CKfDcJ2wYiS9OnR5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e51312166.mp4?token=RXxvGg-HLyyARdktzuHd-hyBn5NqwiXAe5Foe-T19U720VfENo8h2vBAmnq4NP2kk2ydRSIzkVyqcjumnUb6MsHRbOGnf_q2esL5Yx8vhSpR-1LsqBB1wjcDJEYRFUKSEubv1C_qSt44Hh-gyt758bFUxbjfnveiYLx8VubMWeItX0jv8FapKQ9m_o1qAqOEsNjjE7h0Yvdv_byy-gTBRrwu9ewz3SNLNIH8zNNJ9EiflxRpBFPJfuyfa5X-gnQqY-KOluwmgNYOho5XIyxxgEl86x41jN12skeJMoeEgHyaP6DHLIY3Ir4O5kTJqbOy3UvtH29gT66a78SqsVV3omtuSd9lW2HKtv2cb6y-5YBSeaplbjA0ypeXKz088BkNYB5fYCY1INhpYZ6Ixow6euhCBBIrGav7tSJ-o0wAc5Wg6SyDkhS6knxE4dw0jtppnbgSnqFUQrxOTOR6QNu2D_fHfJzZPlWDDpf_CC1DD9_veY8pqHCVidi82df_PtGS6MiS_qU6oqA4sPju3jmNOVBpdzo19FleeNcOi-_Chf7AJpjj_JSP8980GBNdsBh2KrXKy-3TQUIJd7K3PxqYz9xL-XB3dMC7Xl7KxV8zcIma3ZUwBLnESZxH7yayZ0bOxsIRZcNsioQdvYKsEjaPbbeh42CKfDcJ2wYiS9OnR5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇪🇸
گل‌اول بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106904" target="_blank">📅 22:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چه گلیییییی زدددددد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106903" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106902">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رافینیاااااااااااا</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106902" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106901">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلگگلگلگاگگاگاگاگا</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106901" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106900">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گلگگلگلگگلگلگلگلگ اول سویااااااا</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106900" target="_blank">📅 22:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f072da801.mp4?token=Mm8tkozMkq5BJ9KA9o6pOflZTeFJLJVpsr7b04-MLCuGHGM-JEdkRVib1KJiy9cZHfyadLl7XQGtQPcSwIanAxj--DJ19kLYPfjYdpgqR2I-xjgMee189KkDP42c9z-5J0bLX12etb-OZXaCF9r3OmdxQqhxhbQoeAX8Gqsl6NTUXde5hoFlVG1FcnK8dEcuYqAlJ5YDo6gMJIs8tV4VXSEhzXHqgO_vfOKvWn-GXN_IIaL383HI9rNIAJ1SKvZvPtUcrcvalo0XZBx-M2Q-rn-OtvlxlK071WYAgbUp8Z0nycnwqeBz0BtCfY5H8LUNfa3NAdCiXImEc3MTEITKoXmoTuQ_xTWnqUZvNyJg7NpG6RPtt4BCpQ130rjmOEF_9nU6KqDytP2shUa7niBKjQ8fbShNOjaNeltWNXPoMozbA-egNrI1a8HFggQ8LH3sas0c29JTR8qkdfVo10ovmS15TPxSOCY83F-leV9QhecGUknb1yomP_RDnUP4bY3PhVKkH_SzBzYJuAg8CpoK27rE9QCxWauqr8zFpU4DTTJ8i2fYqjJEpUlk5kc6GGOxyLWBRHttgK83-WmfaUrOqmtAIzUWbj4Si8t1y9CUcnm8wSMglOOAZU6OLs1Rf4y7kpRMChJxMeDCCNnRTWFeUz4LUK86s0-RwlW-6Ev8rYI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f072da801.mp4?token=Mm8tkozMkq5BJ9KA9o6pOflZTeFJLJVpsr7b04-MLCuGHGM-JEdkRVib1KJiy9cZHfyadLl7XQGtQPcSwIanAxj--DJ19kLYPfjYdpgqR2I-xjgMee189KkDP42c9z-5J0bLX12etb-OZXaCF9r3OmdxQqhxhbQoeAX8Gqsl6NTUXde5hoFlVG1FcnK8dEcuYqAlJ5YDo6gMJIs8tV4VXSEhzXHqgO_vfOKvWn-GXN_IIaL383HI9rNIAJ1SKvZvPtUcrcvalo0XZBx-M2Q-rn-OtvlxlK071WYAgbUp8Z0nycnwqeBz0BtCfY5H8LUNfa3NAdCiXImEc3MTEITKoXmoTuQ_xTWnqUZvNyJg7NpG6RPtt4BCpQ130rjmOEF_9nU6KqDytP2shUa7niBKjQ8fbShNOjaNeltWNXPoMozbA-egNrI1a8HFggQ8LH3sas0c29JTR8qkdfVo10ovmS15TPxSOCY83F-leV9QhecGUknb1yomP_RDnUP4bY3PhVKkH_SzBzYJuAg8CpoK27rE9QCxWauqr8zFpU4DTTJ8i2fYqjJEpUlk5kc6GGOxyLWBRHttgK83-WmfaUrOqmtAIzUWbj4Si8t1y9CUcnm8wSMglOOAZU6OLs1Rf4y7kpRMChJxMeDCCNnRTWFeUz4LUK86s0-RwlW-6Ev8rYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوووووف صلاح ببینید چیکار داره میکنه
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106899" target="_blank">📅 22:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106898" target="_blank">📅 22:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlcsvUzMdmg5HBJxGprtXjWciRn8uxbBuvSNMOXvcdIzRhvuP-tOx0NLKvnrD-1HetEUX4zByKtjviX4ZQlP4hUroNXF-K6s_AwPTRgCNhNrNIDex2XCvPJV9_i2C85YaOviyL4EH34vwgso1IIx5qZkQYbuFitFr0evSww9WcREDDvBt9ywYjHvy6vbuVIeHG8L_t8AhgwSMHAyVhSA4ykdl347jmo5smUxR-Jmf40lMQQlENbYKJuJhB0Ge5787YVISyYsbhsWEjxzFFTa6EjyxlTymw8JMUGf1OH9HbJEznt3ZjYzXnrsYe-wdYesI3BFCdGRifq4afcMfb-qGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
حمله شدید دی‌زربی به بازیکنان تاتنهام:
🔻
ضعیف‌ترین تیم‌تاریخی دوران مربیگریم رو دارم. اصلا نمیدونم این بازیکنان چیزی از فوتبال میفهمن یا نه. اصلا امکان نداره یک تیم اینقدر بازیکنانش ضعیف باشن! واقعا براشون متاسفم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106897" target="_blank">📅 22:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106896">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f38027f14b.mp4?token=IavIAsB9Ut04PbXvnwZonH5gAs-8FvQOZzS2MWrSC60tCN4D7v4O-f3ckhcigTuZ3WX5-FFeCxuJm7WlpznHdlGDSDEND8Fhgc0T8FN5nGkIJewdU5EYUZk-bojJXyzElQEi78PG8pGsOvDXr5aD1He6_xjRJN1lhgZnHM2G-RWccPWdQG516LHXPvKLkamyRdlyoPewqIxrHMUJlyIRYMzu8z7qJfxnvyA9K6JYLUUMS1LP8OG5a3rn4MLLQL09ONTv4PwfIjwR0jJdwjIoWs0MpFDkgn8fRBrONdfBSlx-8oEgFEbR4u05oCGCxuSE1hMarWLpEyMzd30yL0L6Or7jhSrA4jepnfKPJhdnPZf0v6Bba-5BjrdFCy6xhBzlwAoIOgaFdtk6hXwk5FG4wXKsNMDTXpQTp1Ry_FALQgXnl5gTluFxnLKP4uIBH60mu2NY5yuMR059PNVzux06fo0J_UnUAU_xli_-6Fwb3afec4eZg2yExs7N6ax8c2MsPOJZr8el06xBjdi_YKbPiIPnAIPI7LNbWhxpmEa-7PqC3r_hICroEBAreQ6Al3jlWBFUyG444cwMt3X82sQkQMSqg5ixx_UtatMcoODG1LrsfWJYA7rtl90zzUo1bPoYsC74Yz-Z-T_gaSQrRDZ2BugBANyMcrD2OPUlnFbpUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f38027f14b.mp4?token=IavIAsB9Ut04PbXvnwZonH5gAs-8FvQOZzS2MWrSC60tCN4D7v4O-f3ckhcigTuZ3WX5-FFeCxuJm7WlpznHdlGDSDEND8Fhgc0T8FN5nGkIJewdU5EYUZk-bojJXyzElQEi78PG8pGsOvDXr5aD1He6_xjRJN1lhgZnHM2G-RWccPWdQG516LHXPvKLkamyRdlyoPewqIxrHMUJlyIRYMzu8z7qJfxnvyA9K6JYLUUMS1LP8OG5a3rn4MLLQL09ONTv4PwfIjwR0jJdwjIoWs0MpFDkgn8fRBrONdfBSlx-8oEgFEbR4u05oCGCxuSE1hMarWLpEyMzd30yL0L6Or7jhSrA4jepnfKPJhdnPZf0v6Bba-5BjrdFCy6xhBzlwAoIOgaFdtk6hXwk5FG4wXKsNMDTXpQTp1Ry_FALQgXnl5gTluFxnLKP4uIBH60mu2NY5yuMR059PNVzux06fo0J_UnUAU_xli_-6Fwb3afec4eZg2yExs7N6ax8c2MsPOJZr8el06xBjdi_YKbPiIPnAIPI7LNbWhxpmEa-7PqC3r_hICroEBAreQ6Al3jlWBFUyG444cwMt3X82sQkQMSqg5ixx_UtatMcoODG1LrsfWJYA7rtl90zzUo1bPoYsC74Yz-Z-T_gaSQrRDZ2BugBANyMcrD2OPUlnFbpUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
در هفته چهارم بوندسلیگا، دورتمند با یک گل مقابل اشتوتگارت برنده شد و به صدر بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106896" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106895">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gheOMi9XghpkbWQjKmEYjNDBD5tTIFpu0qRjETk9kzpn7iwBFtyw_kXTaDq9zF9rK49OvtubZUDabXA9ZlIZuC02fGfXj6DzujfdW3ykigURTSpFGvxL5L82u0iaNKxTwW2D8TmzFgrIumrq0HXFWXZm869-eGtVHPEsaHi0l0BSDH0rsj1XiQhehTY1LTc8tLubt8Vm1kVEKjZFK-nUryEo8I69_CoiywAFn1eJaOntdSwrZjficImw52jUaCMXPSNY0flYhClvgpYYFmbaWplUQEomN6g3zpns3nyU2kc99q5T4AkXSAu9gk8b5Bx9_HXvAlirY-s8pOSOzYxhTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست اتلتیکومادرید مقابل رئال‌مادرید با حضور خولیان آلوارز و غیبت سورلوث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106895" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106894">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=ascoG8c-PqCahUVNiJiGt3o60GKTqfGP39nPGQsZyB0qwo6L_CL6dAppcyQPr4KUbKUGoZ_pDxPkOTKvc5VhMPJGDNhOZLfMGSVBslbAtbk91vYrzvdh7WKrsEIAfsQRynccl-UPhgJRJS0DxyNBi4pQw28LJZ4vOv-xx3--EVq1BAZ-KebgbOQ7Uxwd4QgFYsXe2rF1hiQr0E2jq6xewYjm_xe_Jq3QCuEwxHSWCPsgzHFDBVah7J4n7MPI1Ys0s4NmMUneYTTxBpB7AI-7camygNzc0-Ufl7enykHu152BIEYbf000_TRNUszHqP-N9kpWXl4ctfXqtlM7yYiTi35nFQZ6Bp-i8-bI0XdufAYpGxNqfDIrYATY4YJzDa-78-pW7p6sFRama06ltOLWIgNP4cNtj20uYVFTDqW8zR41K75_XxTAxkRGm_KESdK0hRjWThYVwEGPOZJaNpWJWf5ilhrc2K4aOdOe9_R0PKkOSD2lnnfKr_JfkUqxbEsZy5kXH1K5RDktDD7f1qftYnUEATlrKxZxx3qpXVaVttiCvnkEz1X1zqI1BUjvkf4U3OQRd2rQLnn54WA6We_lyDWE8gva9X3RglN98WZTZQnmUswU_oLk_USeAUguzlcrW8RM-o0f-W7V5GDhp03YUXOPebJkparBIvpIRSYlfJE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=ascoG8c-PqCahUVNiJiGt3o60GKTqfGP39nPGQsZyB0qwo6L_CL6dAppcyQPr4KUbKUGoZ_pDxPkOTKvc5VhMPJGDNhOZLfMGSVBslbAtbk91vYrzvdh7WKrsEIAfsQRynccl-UPhgJRJS0DxyNBi4pQw28LJZ4vOv-xx3--EVq1BAZ-KebgbOQ7Uxwd4QgFYsXe2rF1hiQr0E2jq6xewYjm_xe_Jq3QCuEwxHSWCPsgzHFDBVah7J4n7MPI1Ys0s4NmMUneYTTxBpB7AI-7camygNzc0-Ufl7enykHu152BIEYbf000_TRNUszHqP-N9kpWXl4ctfXqtlM7yYiTi35nFQZ6Bp-i8-bI0XdufAYpGxNqfDIrYATY4YJzDa-78-pW7p6sFRama06ltOLWIgNP4cNtj20uYVFTDqW8zR41K75_XxTAxkRGm_KESdK0hRjWThYVwEGPOZJaNpWJWf5ilhrc2K4aOdOe9_R0PKkOSD2lnnfKr_JfkUqxbEsZy5kXH1K5RDktDD7f1qftYnUEATlrKxZxx3qpXVaVttiCvnkEz1X1zqI1BUjvkf4U3OQRd2rQLnn54WA6We_lyDWE8gva9X3RglN98WZTZQnmUswU_oLk_USeAUguzlcrW8RM-o0f-W7V5GDhp03YUXOPebJkparBIvpIRSYlfJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
نبرد اینتر و رم با تساوی دو بر دو خاتمه یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106894" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106893">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=G0obT-ZYSUXI105g7d_hhfmSXc3mOT_CPosHeraUYRRpbbLFpjhymJ10EFAGH8QokSwd4rT2LHr6cp98RBx8NE8StpvRotjJ5vjxkBG-oBzCWRbrfxwFKc615Z1J2UyNn5mf8M5mqub84RJSkqvl2v4J3QkjetW2uF7sQWsI197or4PlVUb5WRFk_YP6XE8N1hW2acq6PfWcJVXzYYSAFphlDNsBFAy-UcDyNnu3tEEmYe-37Fr7TKXxIONciGnsHAiUETzFOhn-pMImJAtPpUdPNRNMvpgl8Gc47vFjSlebM44UZ59Fg0hC9ph1okO7rG3bkLFQXnpR5DWB454bUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=G0obT-ZYSUXI105g7d_hhfmSXc3mOT_CPosHeraUYRRpbbLFpjhymJ10EFAGH8QokSwd4rT2LHr6cp98RBx8NE8StpvRotjJ5vjxkBG-oBzCWRbrfxwFKc615Z1J2UyNn5mf8M5mqub84RJSkqvl2v4J3QkjetW2uF7sQWsI197or4PlVUb5WRFk_YP6XE8N1hW2acq6PfWcJVXzYYSAFphlDNsBFAy-UcDyNnu3tEEmYe-37Fr7TKXxIONciGnsHAiUETzFOhn-pMImJAtPpUdPNRNMvpgl8Gc47vFjSlebM44UZ59Fg0hC9ph1okO7rG3bkLFQXnpR5DWB454bUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106893" target="_blank">📅 21:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otG_JQIKR0z3YzyhuHRZoiuVszbKDzMao5ieRBtiGJnATxT7A2niKbkg2YNnmLQa5-jQZbpyia1y-4L8HRCKCr72Yv4UeAc5AllnHblmEJyd-Y3hH0ZiPZ2i652NJI2gxHWdHRMwX5j4Y73SMwH2zPHmrOjPab_q_sMaCq9EzGql7fnOsqOdeofHKduYJX0y39L5DTGw2uXXg2S6-bNpHbO7Cjezd0jerch_zLK3zc_IiTCof8536SpDrgDMc3EhM-pgEN6kc7TrOhUXVZGdCGVkx62FnOpAfutRnvjmPfi8nbtToIFkbsTu_A6023wXOngm8bSBkZOC5Jn_0AMdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
شماتیک ترکیب بارسلونا مقابل سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106892" target="_blank">📅 21:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d419048b91.mp4?token=du-mIYskChyWehxF9-mU1OfraLzcITw5MElDHu8QZXttJFhwmFHXmbXCXPlm76USrgQraSUULjzbHG0-FeKi2TH3KGQ87Y7LFSTazMGMOXZ_He8t-EL8HmSv6rjyJ_JopV1ZoBEQrOG1SibsMe6-oLCXbXXkEBjHnndAhdipA7IO0eF74GCWAIzdcm3-MHU4P-JgbHbsh-nlvjlWCbsVofp-Qzty1M0xQ4UJeyC7DcUmVDZxUVAd2jj1Vy7FaWpUvA21LvhfwtzRyBjrC37hqlHD0by-Cz8KYbIStyVjI20P9u9vtqs36fW1lrmtUboJKZDr02ZKl3XVXmp-rcrkUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d419048b91.mp4?token=du-mIYskChyWehxF9-mU1OfraLzcITw5MElDHu8QZXttJFhwmFHXmbXCXPlm76USrgQraSUULjzbHG0-FeKi2TH3KGQ87Y7LFSTazMGMOXZ_He8t-EL8HmSv6rjyJ_JopV1ZoBEQrOG1SibsMe6-oLCXbXXkEBjHnndAhdipA7IO0eF74GCWAIzdcm3-MHU4P-JgbHbsh-nlvjlWCbsVofp-Qzty1M0xQ4UJeyC7DcUmVDZxUVAd2jj1Vy7FaWpUvA21LvhfwtzRyBjrC37hqlHD0by-Cz8KYbIStyVjI20P9u9vtqs36fW1lrmtUboJKZDr02ZKl3XVXmp-rcrkUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
گلزنی محمد صلاح مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106891" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=WZ4XmxY3NopF8HYEFociujC2H9zj-27uD-ZJkqdyVMzEvjFKBEkx_XjyPFtzdeDngdom8WsD6YEbmJE3j3jxFvVglRI13rwtoh7gNTR6h9bTCZsoSUPihsNAyjuR6CPGyDdaBTqzUD0emG4ODOrqpc8MyLk-gf5J9OPthycDy7Ydgd06hmfNXZRpvbVEJCX7h11hCcgM1-FDWTYKfaAjQMW2A4Q4lVq6e_JU3bb_MJBH4HaAizMZbWAD30w0Mq8aOuBNNhHca9gbWMrPOHvdnhQc7Fgw9eIOTszHXjac_b93aw1yzjx1SbAzvRNvu8lzT07DAd599NQGnPYHwyNnSFZfnMbbgsKhW3QgNFjmoVFcQebvfV2kr0ArGi2YHFcee__JJPXwDsg7nCZdyrgvHWf5C4-m6zRTMWMXAtOWYkmKzauTbdy4tTb5D_bShg6nx2RJ4kxe5LJCeUdXeO4foL04flYak-yLkBTGULCrFFkuPYibdecRyKsLZFCALEu70OigFLkYxrsxsg81BZzq2W_gIce6YqIShSc8B9KlLrmGM44R97aWc8Vj95Mj9kklU2mRs6OqFXHO4VP2PFI7PUUdRzi0GX9OU5rZWP01R4EIjL7oNn06A5-Bki2KVikPTsrxo5r8H_dbaF12ERBeteIMb4UmzhEqvpoIrW_tWp4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=WZ4XmxY3NopF8HYEFociujC2H9zj-27uD-ZJkqdyVMzEvjFKBEkx_XjyPFtzdeDngdom8WsD6YEbmJE3j3jxFvVglRI13rwtoh7gNTR6h9bTCZsoSUPihsNAyjuR6CPGyDdaBTqzUD0emG4ODOrqpc8MyLk-gf5J9OPthycDy7Ydgd06hmfNXZRpvbVEJCX7h11hCcgM1-FDWTYKfaAjQMW2A4Q4lVq6e_JU3bb_MJBH4HaAizMZbWAD30w0Mq8aOuBNNhHca9gbWMrPOHvdnhQc7Fgw9eIOTszHXjac_b93aw1yzjx1SbAzvRNvu8lzT07DAd599NQGnPYHwyNnSFZfnMbbgsKhW3QgNFjmoVFcQebvfV2kr0ArGi2YHFcee__JJPXwDsg7nCZdyrgvHWf5C4-m6zRTMWMXAtOWYkmKzauTbdy4tTb5D_bShg6nx2RJ4kxe5LJCeUdXeO4foL04flYak-yLkBTGULCrFFkuPYibdecRyKsLZFCALEu70OigFLkYxrsxsg81BZzq2W_gIce6YqIShSc8B9KlLrmGM44R97aWc8Vj95Mj9kklU2mRs6OqFXHO4VP2PFI7PUUdRzi0GX9OU5rZWP01R4EIjL7oNn06A5-Bki2KVikPTsrxo5r8H_dbaF12ERBeteIMb4UmzhEqvpoIrW_tWp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول اینتر به رم توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106890" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/102cd70646.mp4?token=kmYpXvOfRBq2neGex7H11oW2138-AsROLcC4KOngZJgO9eYd56VUCVtTddYnm0nKxsWs96i6wZ22cx43I05Cvbl76czDS-Ijr4uCubmRsK6nOOjbNfnhpfzMaKSMg-0k4PZLSfAIZaH3GylHeQV-ylNYQ0PFk48lO3-x_eArVCu39dnA5OQMzXhDOepUhOepaQHnCqgXYoLxGTJOaXWsJDSbMB88oEnOWqgkOMeD1zxBNpenBu9081qvlJ560qeYAnZFWryno4dER-CGoWbE7PA7B0bHS8JZiobmhiO5kXmg7NGr_PL7wI2NbQ-ylEufyFJRkaC4rL-3vaL-3xFyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/102cd70646.mp4?token=kmYpXvOfRBq2neGex7H11oW2138-AsROLcC4KOngZJgO9eYd56VUCVtTddYnm0nKxsWs96i6wZ22cx43I05Cvbl76czDS-Ijr4uCubmRsK6nOOjbNfnhpfzMaKSMg-0k4PZLSfAIZaH3GylHeQV-ylNYQ0PFk48lO3-x_eArVCu39dnA5OQMzXhDOepUhOepaQHnCqgXYoLxGTJOaXWsJDSbMB88oEnOWqgkOMeD1zxBNpenBu9081qvlJ560qeYAnZFWryno4dER-CGoWbE7PA7B0bHS8JZiobmhiO5kXmg7NGr_PL7wI2NbQ-ylEufyFJRkaC4rL-3vaL-3xFyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106889" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=B_5p2DXdJCjDQlGYwWv9odNlQ1aqYGrQAOanuuTwVCW59MQUVQ0DhDzTO4I8NJxn5wQRk6hTAXaFktAAUjM5lwq5xE81XDF6ZkCDhV0_W493y-t1XLqVjkjUpIYjA4LS6iFvJQeUjoeXBPEXwxsfaZmNkZPceP9p2rf4RNK9BID16WF0uGi4E64HDEvaEHn6OF6y8UWqhcF-fh_ZFrAECGQQ7QvgIv_hc2PykkO3IMPZmDwtIc1mHOGuOvlZs3WtV0OjCEnd8GN-NWLxhhfRog3fWVJ2BjCr0i9zIyKfM230I93HYMTqV08d3pJFMfQT6RXjHslZ8kbsMiPun5McVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=B_5p2DXdJCjDQlGYwWv9odNlQ1aqYGrQAOanuuTwVCW59MQUVQ0DhDzTO4I8NJxn5wQRk6hTAXaFktAAUjM5lwq5xE81XDF6ZkCDhV0_W493y-t1XLqVjkjUpIYjA4LS6iFvJQeUjoeXBPEXwxsfaZmNkZPceP9p2rf4RNK9BID16WF0uGi4E64HDEvaEHn6OF6y8UWqhcF-fh_ZFrAECGQQ7QvgIv_hc2PykkO3IMPZmDwtIc1mHOGuOvlZs3WtV0OjCEnd8GN-NWLxhhfRog3fWVJ2BjCr0i9zIyKfM230I93HYMTqV08d3pJFMfQT6RXjHslZ8kbsMiPun5McVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
⭕️
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106888" target="_blank">📅 20:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=T2au_wPKdy6uFSsKJzGcWTQmRuouQQRSxU4XshG1IyN9hWT5V4GUJN7QuWpLpyB-tgFKy6OJOaBHqultYzAuXlkpnoagLt5P3iuGGfzEuLIl1i08xV2nGHbgdDt46Yxsq71LRwzXQ_QeOJcpkPJF9gZ1bRipoVCnEhjxEeZFUCwY3mmyqwzNncpeINfJM8HOYyOIM-2wI925j61rt17ZLeeT6gy_W8IHx5Yw9xil8jh3DypRhZYu-VatlQwKpumPH-HQS-H7sXfY_nroosE3DUttgSeEBfcGOGS9bVZvdxsmWaneCfx9eZYWkePgJGSpCW1NNM4Ray8QiVIyVkcfgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=T2au_wPKdy6uFSsKJzGcWTQmRuouQQRSxU4XshG1IyN9hWT5V4GUJN7QuWpLpyB-tgFKy6OJOaBHqultYzAuXlkpnoagLt5P3iuGGfzEuLIl1i08xV2nGHbgdDt46Yxsq71LRwzXQ_QeOJcpkPJF9gZ1bRipoVCnEhjxEeZFUCwY3mmyqwzNncpeINfJM8HOYyOIM-2wI925j61rt17ZLeeT6gy_W8IHx5Yw9xil8jh3DypRhZYu-VatlQwKpumPH-HQS-H7sXfY_nroosE3DUttgSeEBfcGOGS9bVZvdxsmWaneCfx9eZYWkePgJGSpCW1NNM4Ray8QiVIyVkcfgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
انتقاد کاویانپور پیشکسوت پرسپولیس از کامنت‌ پرسپولیسی‌ها در پیج السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106887" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzD9hx_nhqtw2Wiczu2NMfc5eTUYPVHccnM2MilfB7JiJsnV-1jiRI-N2qvW6OF0vKQuC96WSbcT5fusfov0n3T6uBd6qN5fKjdceZrTxSz0mWkLb5-qXhqQz0YvTaAS_xp1pBuMBeMQcJAghC_6omevj3Dn9ZDd_fbp5l7Qq89L0iBwipfx8aH_eCXGp-c9KAFY_yFmNgWFGYdloXsOeuYDaT427wEyHX927lkey6rsm3rc_Ham5tDA86URJWSreIQQpFrXYpT7BEmfkAvsSnCQnSj6y6rb05u8jjYiw7520ReFZZbMK2p4tiaG6j-vdBzW1U0yfNzc1wLKpjR8L-Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzD9hx_nhqtw2Wiczu2NMfc5eTUYPVHccnM2MilfB7JiJsnV-1jiRI-N2qvW6OF0vKQuC96WSbcT5fusfov0n3T6uBd6qN5fKjdceZrTxSz0mWkLb5-qXhqQz0YvTaAS_xp1pBuMBeMQcJAghC_6omevj3Dn9ZDd_fbp5l7Qq89L0iBwipfx8aH_eCXGp-c9KAFY_yFmNgWFGYdloXsOeuYDaT427wEyHX927lkey6rsm3rc_Ham5tDA86URJWSreIQQpFrXYpT7BEmfkAvsSnCQnSj6y6rb05u8jjYiw7520ReFZZbMK2p4tiaG6j-vdBzW1U0yfNzc1wLKpjR8L-Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل‌اول آاس‌رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106886" target="_blank">📅 19:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947613cda4.mp4?token=E2veE-pdAg26PAcVvnuV8mHxZn9EPpljJYLPKLT8rnw0dQMLteKKhz-yCElYwclPxJgedaRa7ff68rkl2BSHxcdDXz21mo6DBvxBV0HexcQJnk3jYDdM9muumJtBwk6Q2ZeSDPf1Vg12ZHZ-yNamaOao3X9VxDIx5j_IU26mslc-ZcTzTniqZVoz3MDIk4YBpkfegFA8iVDRUVbfLjnGZ60j-ZQHBSYyaJfaVQkx3YCpAe-htcWJTd_RDSeCGsyayfDca8vMy_n_ZuTtyFzPyU83_yWDhY1_PM9RUzGcI5H4lOimgeWXeW3KAzm0Z6mp6j8Yv43f52_t2nsqFy1N9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947613cda4.mp4?token=E2veE-pdAg26PAcVvnuV8mHxZn9EPpljJYLPKLT8rnw0dQMLteKKhz-yCElYwclPxJgedaRa7ff68rkl2BSHxcdDXz21mo6DBvxBV0HexcQJnk3jYDdM9muumJtBwk6Q2ZeSDPf1Vg12ZHZ-yNamaOao3X9VxDIx5j_IU26mslc-ZcTzTniqZVoz3MDIk4YBpkfegFA8iVDRUVbfLjnGZ60j-ZQHBSYyaJfaVQkx3YCpAe-htcWJTd_RDSeCGsyayfDca8vMy_n_ZuTtyFzPyU83_yWDhY1_PM9RUzGcI5H4lOimgeWXeW3KAzm0Z6mp6j8Yv43f52_t2nsqFy1N9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خواجوی گلر پرسپولیس: الگویم نویر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106885" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=Fsw4jtHX_6RgZlytHrqbWnmX33NLupmH1kInSGrcLSHeQKmzgkX_eOpGHq5tb1MuMtcG8hhT7eLtvjuYLctqHG-fAln2gd2-qrDh21HV2QIZ9E0WxtUF9bez5SHYuqB_XdwYY3JY1WO-4W4mcmk2LH5jD38gmLpRLr9yA1xWIrvfbLAdm78hW64Vo6ad8CBacCBIHY0oNf_CiTmHsT_W7AhjRRO72UHlAyFbo4y1VThlfxSgIghLsyigCCEsiQmkVOIZ64bIaH4UCM9Mn2Yrgb3smGdDGpr6NE-_8wihqnPKvrjDlc0KEYRnwR2fnHVBJt3L2ogRIVxPxzcpJExn6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=Fsw4jtHX_6RgZlytHrqbWnmX33NLupmH1kInSGrcLSHeQKmzgkX_eOpGHq5tb1MuMtcG8hhT7eLtvjuYLctqHG-fAln2gd2-qrDh21HV2QIZ9E0WxtUF9bez5SHYuqB_XdwYY3JY1WO-4W4mcmk2LH5jD38gmLpRLr9yA1xWIrvfbLAdm78hW64Vo6ad8CBacCBIHY0oNf_CiTmHsT_W7AhjRRO72UHlAyFbo4y1VThlfxSgIghLsyigCCEsiQmkVOIZ64bIaH4UCM9Mn2Yrgb3smGdDGpr6NE-_8wihqnPKvrjDlc0KEYRnwR2fnHVBJt3L2ogRIVxPxzcpJExn6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های جنجالی یاشار سلطانی خبرنگار، درباره چرایی برهم خوردن توافق پایان جنگ از سوی نیروهای سپاه و جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106884" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ernpZntuzOA3X4jMjo03t-faV5YcnRh5dQ22Udx7F49YkcS9vKFaFm10QBqitRnVgeXBK9JJaI36swU8FQgL4vR0oPz6iexl9ovxUySrHQvYa5_r2V6E-EYn4jiD0Mw6_o5WcF2FI4wGawqx_BIcc3CYAVOfvWw91Z3S6cXcrn8W15YV1bsy3OR0EaLp001C38UnZlsTIjoN1PgYLhIitRjC8uXWEzaGfzy2gF23WPKySWQQW19vkK_XAYRUQXYdCtaWiKy3jsIOeajwqKqgCjtZ-M3yMsXI4SUvQS8nptbUyeXEw9ZZ84HCj-ncK1KolGtaTplWE_XNGMKfaLuHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکار جدید کاربران برای تأمین نقدینگی به جای فروش طلا
🔹
با روند صعودی قیمت طلا، فروش دارایی برای رفع نیازهای کوتاه‌مدت نقدی توجیه اقتصادی خود را از دست داده است و حفظ طلا و استفاده از آن به عنوان وثیقه راهکار جایگزین بازار است.
🔹
وال‌گلد و بانک کارآفرین امکان دریافت وام تا سقف ۳۰۰ میلیون تومان را با پشتوانه‌ی طلای کاربران فراهم کرده‌اند. این تسهیلات کاملاً آنلاین، بدون ضامن و بدون چک از طریق اپلیکیشن وال‌گلد ارائه می‌شود.
برای دیدن شرایط وام کلیک کنید
برای دیدن شرایط وام کلیک کنید</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106883" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da8b096322.mp4?token=B4Sef2LOb7gBbUXAkMFkb0s-M4cHSbRySlH382DOa3tETdbxEPI3kssCpPU6TSSG_8xlpA3YPEIZK2QucUbDoKpVQfKynd8pX8V8ivVqq71TsEF-NHutOSIFt-vTkjw_o6z3v_BbROPQYWPKohEw5Zh08ny1TZZpO_8rPBP-7-xmY8OsScAwyPT6nBYuzcddiwwybKsTvQNzoZp2QmtQC6hTkPclfAcnSGxLFqPpB2IaDyTDuCJeyKt0XnhMOfVWNbd7mVVcisdnt58juiyTIYALREURyEYwaHjeQ0bRuvgS-VrhbOyIqi5k5XMKw31gPC1zdh07hrcVtRAE_EVsFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da8b096322.mp4?token=B4Sef2LOb7gBbUXAkMFkb0s-M4cHSbRySlH382DOa3tETdbxEPI3kssCpPU6TSSG_8xlpA3YPEIZK2QucUbDoKpVQfKynd8pX8V8ivVqq71TsEF-NHutOSIFt-vTkjw_o6z3v_BbROPQYWPKohEw5Zh08ny1TZZpO_8rPBP-7-xmY8OsScAwyPT6nBYuzcddiwwybKsTvQNzoZp2QmtQC6hTkPclfAcnSGxLFqPpB2IaDyTDuCJeyKt0XnhMOfVWNbd7mVVcisdnt58juiyTIYALREURyEYwaHjeQ0bRuvgS-VrhbOyIqi5k5XMKw31gPC1zdh07hrcVtRAE_EVsFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106882" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmPnz6EfMlz-39wQzwwdvN6K7Cyv06EB1YPGtmcGj1bne5d5OwE6upSS34KC-aU1NtOdoItoD4UdwVI52oeObceIv1ZHo7kdSvlu-YFHezuGDh3lIf2fPpZoDGXqUJnr8iE689vvRAmUrbc7YURu2hYjPpsPqFI3mBfkEDGXH1ZvoEi-IlX3XPJReZrbeUQzP5QdxOuNwLJS_Pkk-4ylVmC7SDfG9gpN5ORqKSr3xd3bY5RzzBK7o8dbDETd3bjlOJ5eDqYeTyTPxSOG0qBkz3dt39ns_ot0shg9CrI0xXaA2FyYdjf7QP-Ybu4B56j7bXJQvnsJePgLHe_ZAMDwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اینتر مقابل رم؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106881" target="_blank">📅 18:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=Cg3YJKZYcbLXljyWSdRl_kkPKNWy2x8ObG70D1xRvj-lud2e6RpSLb2D3kD7TECBaUfwpcTA58IWa9NZ84WW-wuwp65Wx5IuE1JKbGcUGGKtpAK43gJru9THYYtaM9VT_Tgf8dR5UPfU1O9JFF-ewhpw6erveo5PpJPH5lZv9J2IlH7o7fjdJIpTG9owi5Pv_TCrWCd8TzKCi-X5YHBWf3cnBuh8BsjOPZ_9tc_Ha-2dVMWp_svsLB6xnwzy_wWl8QCJCuk4Era9DG3cC3ENmEAcmO6hf6X2h1DWlTXXASkDvKofwV-JBh-4TUWLds2bx1_0PGql6lbtB33WS1z1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=Cg3YJKZYcbLXljyWSdRl_kkPKNWy2x8ObG70D1xRvj-lud2e6RpSLb2D3kD7TECBaUfwpcTA58IWa9NZ84WW-wuwp65Wx5IuE1JKbGcUGGKtpAK43gJru9THYYtaM9VT_Tgf8dR5UPfU1O9JFF-ewhpw6erveo5PpJPH5lZv9J2IlH7o7fjdJIpTG9owi5Pv_TCrWCd8TzKCi-X5YHBWf3cnBuh8BsjOPZ_9tc_Ha-2dVMWp_svsLB6xnwzy_wWl8QCJCuk4Era9DG3cC3ENmEAcmO6hf6X2h1DWlTXXASkDvKofwV-JBh-4TUWLds2bx1_0PGql6lbtB33WS1z1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106880" target="_blank">📅 18:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگلگگلل آرسنال دومییییی خورد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106879" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106877">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3613208345.mp4?token=hdNXK5QNlypi028aJaGDDTY25RN-KrPStCOHbijdUDEVCclYVDr9pQEPzq7EtwH6KqEYoixPhbXz-yIjiCMTncT18LGvRT9lbRyGR4tQLFmHaXeIiYiugIpi4eEm6-gh4eZNGC6p6clc2y8hzpwtxUlH6x5JwS-vy2gONl9sSznDw2lT1Yoc6UJHv6FyZtIjwi06BC_RMx5chQi9HDZD9cPMT1ZtgBe8hFlr9_ce8op8exG8zYKyuej490JGplqCXCeaytx3MGswlUvidnUtmhz9W_YSsVbvzH8BE30oiL5f_JO6kwfum7ts9LpkapMAPkMlpIS8D5R4eA9phc4zSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3613208345.mp4?token=hdNXK5QNlypi028aJaGDDTY25RN-KrPStCOHbijdUDEVCclYVDr9pQEPzq7EtwH6KqEYoixPhbXz-yIjiCMTncT18LGvRT9lbRyGR4tQLFmHaXeIiYiugIpi4eEm6-gh4eZNGC6p6clc2y8hzpwtxUlH6x5JwS-vy2gONl9sSznDw2lT1Yoc6UJHv6FyZtIjwi06BC_RMx5chQi9HDZD9cPMT1ZtgBe8hFlr9_ce8op8exG8zYKyuej490JGplqCXCeaytx3MGswlUvidnUtmhz9W_YSsVbvzH8BE30oiL5f_JO6kwfum7ts9LpkapMAPkMlpIS8D5R4eA9phc4zSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل‌اول برایتون مقابل آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106877" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106876">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ-vInd77-nmJGDM44vL5SasSR3_6W_6JHcF2UarmUNBV-9R6FAiGxjFiDRLmyahJtX_oZuRHZS5uLcnZdCrH4Sad1rGWukK3BJJ1DQwwueZm28QvFrLc23LmD2cRrkVJ18qDL6o8wWEow1xpT77C-Qd1Y2-o60ywM4vZBXpreTJY9K6KwA4nLj78RuZSwR3jB1Ej1CerqVoEff7TAmNYi8Wuvvp7vyklHsg5_ONx7WiEiVZoKy7fd0WXG5huPbfQgQMoL7hx8WecYjeMj6tOY_GONnL6G6qyQL_IWtmzgFP6iQxKHza4ySWHqPefcDKbpk9KclMmlIBIlHSqq_WKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106876" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106875">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyvyKUb0NRwIAelvYsCj17NN1EKhmw30o9SNN9MZgQBQUY9R0ltzLJFxf0IqkjYV27yR0dulAsD-IG2KRq3Hu0yrUj3MJCoBw5UB-WIZaj5JcZK05HKMNy1G6pKpIL0WCF5cr7Hc1atk6RhIi4_wMGrIPYxHshvwPn5w8pO04aTYGKvI8CSZxWRMXyxoeotLRGA1hESKZWVKFH-K3j5zSCFWr1w-dNMvt5HW9ttaa2vnCVw3T4xVl0-wO_Se_IKEp6oCbYFL0L6ry2T0d7pGSIiRUS4RsZlWg-WvJuGkpOMQomLMbP1el7Obnkr4sE6bK5WdSCdah320XYoYPrbZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106875" target="_blank">📅 17:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106874">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=o3i7lNQRYGZUAHdup2sXaPeKi11bmCM4w55jgt7y8Bnre-mlDmt7BmBkpyWw5sNX0ny7Vtqp79ljZejuT_MxDt-nxh84pi1ZdIjFpVKfRr9DbPH-RO7wRIpBfv23AtPiW8CaNWpoQbA341NSMpOIIvJldbT2G8sQJOrd_jw21d3_jbvMZLm0v5kr-V7WBcaRnxNPjUjFxBkNOUs8AR310z7BHISmQm_Juqz-CiKZDH0a6Ppe6Jh_wYr-ezrtUFUCl6QnGAVItEkQixvsQF-8YY63a4A4s_Vr-zC4UjhH-zWPVMTGred1uWSSzZ0WvGZfygifZGE4LqZNw5RZyavqMqzQC3fCAyfMmWLltQeBmZf5mClfM-HSJVsIWbUHH5VPqyk5tVzV1TtoZqZeZELWmt30ph_vUXzcB2CG_xJFhoNZxwvAE3iBlE9bOIDuRwY2wBwwJNPj7-fIXucneBQfGuN2zQbEiuT_Rr0LvTAPfMflaWHMDjXgZSYkcjL8IOswtMrUrE6RIxSTO3gKPxeexoikgD-wnmmXgZGkYSlJ9GYAI0Vh9yuHEWuYlkPzP0NzM4s7FAK1sbmY3ZG8B3qpqew4JJiiR_KkNcP9p1sYXwzUGBNhijrLuKDOJIvNQ9l9UI81qQolcmBiecGH4mmxiUok3sR4HAt9amGnpN7ufg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=o3i7lNQRYGZUAHdup2sXaPeKi11bmCM4w55jgt7y8Bnre-mlDmt7BmBkpyWw5sNX0ny7Vtqp79ljZejuT_MxDt-nxh84pi1ZdIjFpVKfRr9DbPH-RO7wRIpBfv23AtPiW8CaNWpoQbA341NSMpOIIvJldbT2G8sQJOrd_jw21d3_jbvMZLm0v5kr-V7WBcaRnxNPjUjFxBkNOUs8AR310z7BHISmQm_Juqz-CiKZDH0a6Ppe6Jh_wYr-ezrtUFUCl6QnGAVItEkQixvsQF-8YY63a4A4s_Vr-zC4UjhH-zWPVMTGred1uWSSzZ0WvGZfygifZGE4LqZNw5RZyavqMqzQC3fCAyfMmWLltQeBmZf5mClfM-HSJVsIWbUHH5VPqyk5tVzV1TtoZqZeZELWmt30ph_vUXzcB2CG_xJFhoNZxwvAE3iBlE9bOIDuRwY2wBwwJNPj7-fIXucneBQfGuN2zQbEiuT_Rr0LvTAPfMflaWHMDjXgZSYkcjL8IOswtMrUrE6RIxSTO3gKPxeexoikgD-wnmmXgZGkYSlJ9GYAI0Vh9yuHEWuYlkPzP0NzM4s7FAK1sbmY3ZG8B3qpqew4JJiiR_KkNcP9p1sYXwzUGBNhijrLuKDOJIvNQ9l9UI81qQolcmBiecGH4mmxiUok3sR4HAt9amGnpN7ufg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
‼️
🎙
ماجرای دست رد مهدوی کيا به قرارداد ۲‌.۵ میلیون دلاری!
🔻
مهدی مهدوی‌کیا: مدیر باشگاه داریان چین بعد از دوگل من به این تیم پیشنهاد قرارداد ۱.۵ میلیون دلاری را مطرح کرد اما بعد از جام جهانی به دلیل عملکرد، خوبم آقای عابدینی رقم رو به ۲.۵ میلیون دلار افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106874" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106873" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106873" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFJJ3xU18GR2K0niJazUxVNX1Nj7z5d2SBIEFji7D2ON9WknbCaFgTQRdj9eH8ZMJQBKaNQUCmsC4_G6Ie4b6hv7GqcqZ2Jn8eBQNto5NkD4yXM3OkE2AvFOzOzoVaydFDSuZ4jlt2rCz0FFcp6iZoefWYea2mMiKRxMnqAaPrUEEaowEtadtv0Thb2iOlFKmbC3GYf0_AI91HOJrj6s5anZRdNANti7En4FVt56-yAk7gMtxSr25745OWiqyXHfgUNtPLewbogrRi66KkV_lF9HVc1uDXtwGFJVkjKTz8tPwQXooiax0K1B2DNTHfCHWvv8da3AlDcB_vNB9nYPSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106872" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106871">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLNxK-gqC4nnqW-6VONnfEQktg9SwsKecau7cK8wF6yVoE823U0v2rXa4renFrfYrEqhw6GglzqLx8RE2aHEy9wuFtBEkSWBv80vJGDIESL1pT3y1HktlFSgU_oWry8h_HOCqMkt3ntS1H6GwU1iA5R3w1ZJzv3skBsrXQwzHOXsjtsr9FPC46rIY4C4tds1lvJBC62qqSvMdE1ONhcUlVT6qGGB36Cc8Psr80NSmLr6jzkVVurEdkkGGdTmnI5JJty-jaFJh25eQuoDBe6Ap1HoXYl6bG4b0_cPreikP3oDZ4P5nZgOiBdJMtAH4N3o4CDw7luk8WLL4zDhfLQbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
ژوزه مورینیو در پاسخ به اینکه آیا از شرایط بارسلونا نگرانه :
🔻
از نظر تاریخی و فرهنگی، رئال مادرید قابل مقایسه با هیچ تیمی نیست؛ بنابراین من هم خودم را با هیچ تیمی مقایسه نمی‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106871" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106870">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwDZl4Y_-oXr7bEspDfvLtNlCPDm9CHSZ1b2RCyZrFaVACU4L1rvyDxRXQDJbkB1wRtLwXmpKbZBwfcF06anbvNQhWyctPPi3dAbW0wTcyqm-4ifWtylyOecTt8MlNqoLQd5idJLqF3DLm9ghFn1DtEdF4ROEqXIYCuVIlc21HcKDGVV6rDZPEIn_WOZs66351_nR4c1B_Gq7cNdYp3Sft7v1brvlu_iLT3KryrFqWP2hOabnmgGMB457v0gVGnDEcbuK6LNrxrbRBNbNuOdqWbwSx0Rtt98e0H5dWwuwYQ6t5HQsx_xP1da-wuCDBbj3ILFcI5PVoSN5ZtDlN5BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
❌
رسمی؛ مجتبی حسینی با توافقی دوجانبه از نساجی جدا شد
📊
2 پیروزی - 2 تساوی و 3 شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106870" target="_blank">📅 17:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106869">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf935413.mp4?token=QqT1Bc7j-3O1J3HjgJ6PTDGgSoLmcBowticCVvbCOD1tNoQkJ_8deDKb6FeMYrzFQvCdtW7ENhLrLIlpTaOR2snR2O-OqxyaLt56mu6HD7X2V3zIzB1Upy0mINAFoCttgx2enilL6ppvD_dBsU3BsMXNQk41JoQtoJX3Qk6iAk--vjC4tRCW7OgU2jXCdBWPP-XbEoXhYpBtPPYlzzNchyOGS5DkoMrAG1T2tvRaOq3aH2nCpDLX_lLx1qybgaSka5lR-vlSmJYQG3YgZLZ7rRgR_L0W6FUtzm3138Hv4SSCtOS5fNcdGWD1TCp0d_2jdDYXcCdheo1_zIVRjNMJIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf935413.mp4?token=QqT1Bc7j-3O1J3HjgJ6PTDGgSoLmcBowticCVvbCOD1tNoQkJ_8deDKb6FeMYrzFQvCdtW7ENhLrLIlpTaOR2snR2O-OqxyaLt56mu6HD7X2V3zIzB1Upy0mINAFoCttgx2enilL6ppvD_dBsU3BsMXNQk41JoQtoJX3Qk6iAk--vjC4tRCW7OgU2jXCdBWPP-XbEoXhYpBtPPYlzzNchyOGS5DkoMrAG1T2tvRaOq3aH2nCpDLX_lLx1qybgaSka5lR-vlSmJYQG3YgZLZ7rRgR_L0W6FUtzm3138Hv4SSCtOS5fNcdGWD1TCp0d_2jdDYXcCdheo1_zIVRjNMJIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
سکانس‌جالب از قسمت جدید مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106869" target="_blank">📅 16:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106868">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98bb41c972.mp4?token=mV2bgomnV3lLEZ6AB82EfKldIU1jgSDUfKmLAJyM3uvraoteCFP7UCZx2RNLAklxIxYEPjkMCflAvrs4Vo0ds5eRPrCv7fJgB3XtyxE1f9l-OQBx9jCHPdstH3IVKwaa8uR4wMZxyY3GfThe_wuzQEwzk6r5wcFqk3pIHfWSGB2n9gD2ZeTK_IfT6Tp5rO4CxY6qMsxs73urzrmohf1foToPRyC7vGlxZXWmMZ0WyTlkNbBDdxqDfgzV1ZCzsmdYir-Ms0O0q3srsICVOrjlfPMAGfUuLxqlBLFJESmwwHcmw186xE3vHkauGNcXEcMKSsyIvPxUJRAlnNo4esNf0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98bb41c972.mp4?token=mV2bgomnV3lLEZ6AB82EfKldIU1jgSDUfKmLAJyM3uvraoteCFP7UCZx2RNLAklxIxYEPjkMCflAvrs4Vo0ds5eRPrCv7fJgB3XtyxE1f9l-OQBx9jCHPdstH3IVKwaa8uR4wMZxyY3GfThe_wuzQEwzk6r5wcFqk3pIHfWSGB2n9gD2ZeTK_IfT6Tp5rO4CxY6qMsxs73urzrmohf1foToPRyC7vGlxZXWmMZ0WyTlkNbBDdxqDfgzV1ZCzsmdYir-Ms0O0q3srsICVOrjlfPMAGfUuLxqlBLFJESmwwHcmw186xE3vHkauGNcXEcMKSsyIvPxUJRAlnNo4esNf0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
ژرژ ژسوس سرمربی تیم‌ملی پرتغال:
🔻
کریستیانو هم مثل بقیه بازیکناست؛ اگه عملکردش خوب باشه بازی می‌کنه و اگه خوب نباشه، بازی نمی‌کنه. آیا جایگاه ویژه‌ای داره؟ بله، دوران حرفه‌ای متفاوتی داشته و پنج توپ طلا برده، اما آیا این چیزها روی تصمیمات من تأثیر می‌ذاره؟ نه، اصلاً.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106868" target="_blank">📅 16:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106867">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a989591ba.mp4?token=Qy00LEg5mL1SaR9sHOTiJuGxgpsZfyVCbKZAwzxIeuhLl4bRQwmFAxya0Huf6dChTjaJ0bl1Mjdz2HYY74uqgkDlz0-5KunIYcJXdiG_F_38ypwOMCMLUZYYnc8egycxp3y5jX3YKURWAshdaa4Nj73WccwpaxIBWI_UZ9d5TyRP9Bhw30HjIss_kFkj6CuOWnYiN0PEqP_kPbH781l68f3x4w4A-su4sZjwS99PTpSO0GMx4UpPckZQK17rBePLAJeyIEVAV0-JMORJa3yWpDBF5VbOheeiLliGRZMrxrzXRItWkyWYiyCQ3WFEfuzatvcYQsrFrSroE9ptOP0_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a989591ba.mp4?token=Qy00LEg5mL1SaR9sHOTiJuGxgpsZfyVCbKZAwzxIeuhLl4bRQwmFAxya0Huf6dChTjaJ0bl1Mjdz2HYY74uqgkDlz0-5KunIYcJXdiG_F_38ypwOMCMLUZYYnc8egycxp3y5jX3YKURWAshdaa4Nj73WccwpaxIBWI_UZ9d5TyRP9Bhw30HjIss_kFkj6CuOWnYiN0PEqP_kPbH781l68f3x4w4A-su4sZjwS99PTpSO0GMx4UpPckZQK17rBePLAJeyIEVAV0-JMORJa3yWpDBF5VbOheeiLliGRZMrxrzXRItWkyWYiyCQ3WFEfuzatvcYQsrFrSroE9ptOP0_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
جمله قصار فنونی‌زاده خطاب به امید عالیشاه: با آدم بی‌ادب باید بی‌ادب رفتار کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106867" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106866">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-F5Jv9IXdRZvGcy0OjGFe4QLHNpGp1Chg9KyjXaI9NLVCawULLh52OljhXiYgIMxBAmnK8BifeOv6y8d1_MvvzxF5YyInXdsAq63jSldmLRewzQa7IHS07FZ1L2SAA_op_xZCuNDn3VjpYSfCZ35M195_4HXiXi8_GU515Bqxbqq6zp729x3CciGL15_tBz_IYEgxIEllFibgo8yd2XKh66dyayU9T8pogiotAGPRuQvmslDbS1tLr7Cr802U_3ybwMLvnftiw8if2008f204CpCJvdklXP-koXOAy9HdAWRULClZUOWLN7vRumuNCKOkW8jLx2WGCKvaUVL7_68Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد ضعیف املیانو مارتینز از زمان حضور در باشگاه چلسی:
⚽️
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل برنتفورد دریافت 3گل
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل هال‌سیتی دریافت 2گل
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل آرسنال دریافت 2گل
⚽️
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل برایتون دریافت 2گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106866" target="_blank">📅 15:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106865">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWWYTGkU6r-CZazelknFDvaWxM2332COyTcE1jkmvIdaZV2wFQYV3rJ7WilMlTXd2cqbhtJdKdb2v0PBHYGomuUtLtMbmQ2v0gUaCtbUMQZTfxC14MusRkfabmeq3bXK28XYVF32Xtn4n4l8dGOyVxwH120Eatley5wnvDyqnP_b_XAQlpgdTFjjVR2wj3zGi2tEbFbjhEP_k6y1AG1H-tncPg0tr2NNhzfsPDLxHp3lnMlW9jtm8OHMtIDK_E9sHVN0IZQ4gk8rsyYKqTemLsf1EeGkNFGFeryIoeUbNRnLnoc2o_sRQEUv5521vUnzJWAOI9lKwmdjPIOb7nv_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
لیست‌تیم‌ملی آلبانی برای فیفادی بدون حضور یاسر‌آسانی ستاره تیم‌فوتبال استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106865" target="_blank">📅 15:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106864">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed8ff21de.mp4?token=E3hb6_zw00oRDUcmTBvEi_GX4t5BK9J_gkKnjUHV-0r2o7vgxmwYJ4bFJIO6WoOnNPjeggpU47LG8vBjZadjJz6qbmDSnk23REbTAYccFvNbdz7nGEdrHGGo-JpHUegLeExuax0FU8VxhMyi3iLHHq7ZPdOdEGz6cxQ7PDbMr2uehgLYW4FTe2oMYvOhMuKqt-7KD75qv5byJFVj-Chs880h2a1dgrHOAtvPnb6ANvbwB7TA__NIgbpj66kwRxCBi799BpkiSsy0OJ_u7lgQ16WLHq0M06dSlyIF2gyAddjI8OH8wy2tiweAaxMdHPEQE8EcVyEPIgXGZ0VEsYIjeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed8ff21de.mp4?token=E3hb6_zw00oRDUcmTBvEi_GX4t5BK9J_gkKnjUHV-0r2o7vgxmwYJ4bFJIO6WoOnNPjeggpU47LG8vBjZadjJz6qbmDSnk23REbTAYccFvNbdz7nGEdrHGGo-JpHUegLeExuax0FU8VxhMyi3iLHHq7ZPdOdEGz6cxQ7PDbMr2uehgLYW4FTe2oMYvOhMuKqt-7KD75qv5byJFVj-Chs880h2a1dgrHOAtvPnb6ANvbwB7TA__NIgbpj66kwRxCBi799BpkiSsy0OJ_u7lgQ16WLHq0M06dSlyIF2gyAddjI8OH8wy2tiweAaxMdHPEQE8EcVyEPIgXGZ0VEsYIjeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
سوال مهم از هانی رامبد؛ برای رشد پایین تنه حتما باید اسکات بزنیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106864" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106863">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cfdef19.mp4?token=FcZo7MNSngmGRildpBrPPRX_BlvRvFJNNucS5qVBDz03muN6U4d1MKw8N-FbOnFEEEO7z46PJtJgHtZ7wp0RLMtAzGhCNyonyNjcbuB1050T6wAKp_HbB9UQ1IMGS0pRy6OodBto9W4GBQWhxfr8wxh3FQ5ZV8ZStjVFTXyHGrvFnjz50Mx3ZXqcFfKQOO68JUYj9xG2QdoCAISbVOw_oLDrrko8b6h0sIJSLNZxdJzkS-FMcCw7yZpWglgUEqNB8atx28w6MpBlXWGxTFOSxBmMThpHzTKpVGn6QgdfjoA64keyxX48XjVSSANqqJ7CTRYXfxxQbCYoGqo_RqiF1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cfdef19.mp4?token=FcZo7MNSngmGRildpBrPPRX_BlvRvFJNNucS5qVBDz03muN6U4d1MKw8N-FbOnFEEEO7z46PJtJgHtZ7wp0RLMtAzGhCNyonyNjcbuB1050T6wAKp_HbB9UQ1IMGS0pRy6OodBto9W4GBQWhxfr8wxh3FQ5ZV8ZStjVFTXyHGrvFnjz50Mx3ZXqcFfKQOO68JUYj9xG2QdoCAISbVOw_oLDrrko8b6h0sIJSLNZxdJzkS-FMcCw7yZpWglgUEqNB8atx28w6MpBlXWGxTFOSxBmMThpHzTKpVGn6QgdfjoA64keyxX48XjVSSANqqJ7CTRYXfxxQbCYoGqo_RqiF1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
صحنه دلخراش مصدومیت یک‌بازیکن در هندوراس که پای بازیکن در آستانه قطع شدن رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106863" target="_blank">📅 14:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106862">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔥
👍
🇩🇪
شب فوق‌العاده اولیسه در برابر یونیون برلین با سه گل و یک پاس گل و هدیه‌ای از طرف نیمار؛ بایرن مونیخ ۷ - ۰ یونیون برلین⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106862" target="_blank">📅 14:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106861">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIdtXFo1vE9T-MGUPvUd8GGnA7FvBsTZ76VNIvArhjrxkZFEbT3LGexMa8xtJ4sPl7ofhJLDcXOX3yJo1rTzFS1oL8u6sSBzrr1FWtko0WurWUHi_i_CRKrSJKYAnAGLcSy5zHWBMHCwwlDk8qifoK2VOE4USJmp4Y5j1Dc-WUHH6ogtmgyYzrRqFA1tWdSDI6UAfIaj6G7uiQ3cF3PMiMTDCWSZSPr5nV33WL37zxoZ71f0hIoCm9ABxFla7Pjf-K0Jq8Ro_NduRORYarsPquyiK5FmeN07uoaLL4xYdlUWYXLspiwWkRmGqhGMP2LhTTA1gvDU4Y272PrbZeDSCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌پنجم پریمیرلیگ انگلیس: ترکیب تاتنهام مقابل استون‌ویلا؛ ساعت ۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106861" target="_blank">📅 13:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106860">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3121f63a1.mp4?token=g_pchX9UQ8RUmw8O95irtY4axgFqU_G25faAIys3KUDFm2erOLPiS6gRLvMkwjTmhoyjUnXKge6hoyGp8ZgmeHykWLV49ClmOFGdAQVcKvaDY-yKDKFsj_nwvjnDRcyAQdMmdgjT6vf-sGl6gcRepOQD2GO7lGqMSRZ8hh_5zzRiEwWQCwHEKoeVnQC04XyctEQC_eBlPIWrY85plsXt0yTdCYC9Cx_D6JInNDLpRDS4RQyomkr2ziyj6c_rG6zmJoddAYB9diqC1W4tT93dVu9TDwAgzaw_hkG4nssmy5OYeilkazin696wIPsRUh-eaoo3A3REFgOh1vIZDzTppQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3121f63a1.mp4?token=g_pchX9UQ8RUmw8O95irtY4axgFqU_G25faAIys3KUDFm2erOLPiS6gRLvMkwjTmhoyjUnXKge6hoyGp8ZgmeHykWLV49ClmOFGdAQVcKvaDY-yKDKFsj_nwvjnDRcyAQdMmdgjT6vf-sGl6gcRepOQD2GO7lGqMSRZ8hh_5zzRiEwWQCwHEKoeVnQC04XyctEQC_eBlPIWrY85plsXt0yTdCYC9Cx_D6JInNDLpRDS4RQyomkr2ziyj6c_rG6zmJoddAYB9diqC1W4tT93dVu9TDwAgzaw_hkG4nssmy5OYeilkazin696wIPsRUh-eaoo3A3REFgOh1vIZDzTppQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
▶️
ابوطالب حسینی با این ویدیو اعلام کرد که دیگه تو کار ساخت برنامه فان 360 عادل فردوسی‌پور نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106860" target="_blank">📅 13:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106859">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqSLMumNOjhxd5hAsg-k4YCWw8MgW5SxnJekqKsDmFva-wsQpHMK3-83xrwJcoyDOjSacplGilOfZWfEDtRii0SNOVSoyAryT2A_gJc0_hOBWWFAMirimccwU-l4gknvkOl6LaLyUhFbJxP1X4P0qOboLC4qb8v2MiC0rMw_J7OUiKPczB85CpMw4Pm_38YOhgbkMyhcFZ9o5Tz_Fk1RftqNLU0rpab0glJDLKgK72oK2SNJULKPc8bQ_k7bufsv5VHSx_nZcGVRv0IWd_IWiixa9rzOZShyxVbtwIH7cgFP6wYSK9geCKSfER3YKTE37EWK8elcbiB5HrtHVh5bPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🏆
رافینیا: بدون‌شک برنده توپ‌طلا باید یامال باشد. او آمار فوق‌العاده‌ای داشته و قهرمان جهان شده. مردم حاضرند برای تماشای فوتبال او هر رقمی را بپردازند و من یکی از آن مردم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106859" target="_blank">📅 13:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106858">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-L-8QXW1Wf1-D3fFaVUP6ySJ6NxFvNcoKEqEvDgV28gOLfnumH_rtPFfaChSLJ-hLB95LYVGh7O_yni2Pfnu76BV44d4kC-PN-jIFFO5IEsNdHL09AWyruvj7WkEuHwnntAFl-Y54lIWkWMYJPc22m0vT-RmftF4vFVmqKSy7cw_wc7779JF8jq-9XLlT-VEi7r5gZxZMANTwMb_pVdBQgXDYQzPURUg9OeIU5fCBg5a_8F3xQUgTKvv8CeGkgzUh_g8a4v4AhKsjwkOJdc6ZavvhuAk8XREKWOHOUELFwGki7DeP855oIzkhBUv230kqb55O9SdBe3joy3osDmZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
رافینیا
: در ابتدای فصل یک‌پیشنهاد بزرگ از نظر مالی به دستم رسید که مقصد عربستان بود. این پیشنهاد می‌توانست آینده من و نسل‌های آینده خانواده‌ام را به کلی دگرگون کند اما بخاطر عشق و علاقه خودم به بارسلونا به سرعت با پیشنهاد مخالفت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106858" target="_blank">📅 13:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106857">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da53ddde15.mp4?token=bF3IQs-ntLF9XDiCXuEpqySdlXNalw8bzXt8pi3kHSoLZ5FZ5GLs0wIt1D5iiLmV-z8sxZfRawBFi7CrlGnfKNho32gxOsM78rpqqlS8lSJHq8hCsDO3dZoxcsU7gyDsM_rEpWmjDI8nNZ_Iljx2G6IHbNzkYdAc2Zon50pdPJkGp386TG4ICrtyTFXM5kdwYgllycAAld58Eki1DJiY1d468D67Ug_0_5Q4vzM2_6NBSEInCgmg4SL4X9SsOm9W1lazy1hsodS6jPs5wtJRc7dOcRElDmS4M28XS14rcpCypyRTh75oOx9xnXHMv9bfYWSQtHeixk1w9Dzco9N2mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da53ddde15.mp4?token=bF3IQs-ntLF9XDiCXuEpqySdlXNalw8bzXt8pi3kHSoLZ5FZ5GLs0wIt1D5iiLmV-z8sxZfRawBFi7CrlGnfKNho32gxOsM78rpqqlS8lSJHq8hCsDO3dZoxcsU7gyDsM_rEpWmjDI8nNZ_Iljx2G6IHbNzkYdAc2Zon50pdPJkGp386TG4ICrtyTFXM5kdwYgllycAAld58Eki1DJiY1d468D67Ug_0_5Q4vzM2_6NBSEInCgmg4SL4X9SsOm9W1lazy1hsodS6jPs5wtJRc7dOcRElDmS4M28XS14rcpCypyRTh75oOx9xnXHMv9bfYWSQtHeixk1w9Dzco9N2mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
رژه کاروان ایران در مراسم افتتاحیه بازی‌های آسیایی ناگویا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106857" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106856">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDMoT4-MhXsVLBg40qhMNTdQKf6YpIwMrILle8nmKjkzID7OITQNa_B9tDDqgUEdNwvJnS9ojsZpizUZtqMaDYzjnMFStbTDUiECqM1n5tHgRXZWE5Z0wa4Lh9wbYuNL--A1_WAyuJoSKtNxHfVB_nCsYckFcspcVNyi96nWLuKE6IZD2dXCVMWqlXUFyKprJCgQADxosOKsSm3huQVoyze-7h8At5SzJhkhYn5OsrdjKcfYMKqTunjMXS0XyOIUTVCDHmwFn6H0map7hLn2hAzRFhzxeiGuPeUjE4-XpqllYeunc8bHhY-WHBfhetNovzBfUC6Qe5E5iF2jmAIzQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
نتایج مانوئل پلگرینی در تیم رئال بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106856" target="_blank">📅 12:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106855">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJn8XT6WZJKmJhf4Uwo67wK_xnhD_yqFsTNlmrp1WZ-Noh_gkGmXnu-qklRHf4eyDKzvhmqwMEk-SyoZWipcoeN2pbrdTErTOCjfErF1G80J6dD91bSOu6ONed9On5f42SXP7ISBbpiUB9-41Z8XjhbbralaE9fJb22ZeHvtwRkfECTJpGIBLuyiKqER3V0tlLGLG1EhTiDrD5DRlV8DdosCu62uqach7SksKd2GyWiSF3ZgLeUE9R-fBH8yipURyd2D4fXHtqCBDwcs6hCo5QueiUkdn7mn-ZM4THQ7F4ql5tltNti6Cex6EysJEMomKjwp1MrNDqgwhbC-80cTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🏆
با برد استقلال مقابل السد جایگاه 5 ام ایران حفظ شد و سه سهمیه مستقیم باقی موند؛ نتایج مسابقات استقلال و تراکتور مقابل تیم های قطری تاثیر زیادی روی حفظ این جایگاه داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106855" target="_blank">📅 12:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106854">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRpwRN_SIWWvBmO84bPqjPmrumGYIlt2by9lzOjVvSFsPQE6dMo3lCUGZkyPl9f5Oqbdret-WgAEZLHjj-f-OaFxlnoskmPOccyX2sNcugcPDKiuCtoj1uWS76X_f9u6g2EaaXm2RnpJbjlhrLV3ZO5f0dn3jGsLCWmGEiTwzNyesk_g8iXxH65-CeGMp5Isx4y6Lu22BQhs7E9jWYS6lJycW8jdqqxWgtx2lKa9NFNRAZxN02mB-f3mS_Zk3NqLj6wrME1hzKTjeMxRM1n6zRDhzzrbeYYw3sUmsvD-abHLcZyT0ALYLAwbIfvtnv8UMr7sFO2kavknJ91w-OU1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
لیست‌بارسلونا برای دیدار امشب با سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106854" target="_blank">📅 12:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106853">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdowzVg7Ygk3oQLKHQ3BRp4BMsQ3XtKF8eDLiDWlZauy4yZPmm_xo4jlSkctmQJhBBYdNSF4RdSSSF8W2MVo_9rPHCryS6djJQOQB_tUtzEICFKjV3SLLmrre2C-ycKxTy5ulficnR7xCYwuU4V-E1AtAHcGTnDft-zSQ1VkGL_3_I6jNQ3zB8KBPmpmhfUqfilTAsn-SYYjrj3SaFKEpJVZ-8lFHePsZrkQGkiqRGJbFpMvIugTq616h7jDG3u-12M2pOr7EIW8zzLXpNVh-61UP_4zH3oNk8RV1qL25FrgeP6vAOYW2RLEjA8HwEb7N5BvHTkY0vHRIrxf2EBbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
▶️
مسابقه دوی نیمه ماراتن بانوان که امروز در بوستان ولایت تهران برگزار شد که حجاب شرکت کنندگان بدون محدودیت خاصی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106853" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106852">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106852" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106851">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMiJ0Zy9JHFQMX1hXKRhCQkno-pMzJZAjoDWgWgW7DQA8rN20AphC6bWY_YgZou8h2CwBBw0cM2uY7lTEQsbBeGO6pvMXiSyMvom4xuIELrgJuhV4O8ASg2FwqaHIjEKllDpr5VeLXc0YyUUHfLI2X-5nX_xFMdrCODlgjMJ7IXbC6M-fCm81Odp7hKebc-wqgQdghCGZ4Cbili50OnLxlJ2D8TzEKQnR3xbhdga2wb_B4evKKE2rEyEhibsskt6Vd-AsViRb4sYNoJCA3A99guK_0VFjUg5xItBXHe6w3Akm-9eD0B8lfzzgPalzN5OmtSLtRx7CvvAvV_7HGYhDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106851" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106850">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👍
▶️
🇪🇸
🇪🇸
در دیدار خونگی رئال بتیس برابر ختافه، ۱۱ نفر از مسن‌ترین و باسابقه‌ترین هوادارای رسمی باشگاه، بازیکنا رو موقع ورود به زمین همراهی کردن. این مراسم بخشی از برنامه‌های هفته افراد سالمند بنیاد رئال بتیس بود که با هدف قدردانی از هواداران سالخورده و یادآوری نقش اونها در خانواده بتیس برگزار شد.⁣
از اونجایی که بتیس توی بازه اصلی هفته افراد سالمند، یعنی ۷ تا ۱۳ مهر، بازی خونگی نداشت، باشگاه این مراسم رو زودتر و در دیدار برابر ختافه برگزار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106850" target="_blank">📅 11:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106849">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feAuP-i_xIR9HejKt5slbC3mKcSbjEuvZL5hOaJKEedMnzD7tgU07UXqF4H06bIiPY0qW6AMysDAU70hyLP3N4iJ0ORQdf5YL83s2bvHRTMZtmRj-Nnmmq-n4Sa5TYw46OR7FXXeyjVhXo1V6C71wnfE5e3XrNnVGJiVM3fKcyY06D1o8d-_lA2NoNXKdoRkRO2xqyR0bkrvtaKPB7nv6vEPsT8dLfanE0r8d2qXOefClKIlwrZZ38oOQLzY-Uep_DbNCl99Vk5OTif6_Ruxv1JHGfIfWVf1iKs0sDMPOz4ceY9zj4447OS57lrZ24QAoN5pprFQHbERDvIRfRu8gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
😆
وضعیت سه‌فصل اخیر اندریک در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106849" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106848">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f6de555a.mp4?token=AQ49WFMTHc6r-ILl0I2p3Pi4j7SBKsVTnOLhTuYoOFURrZ-b_pH3W3_6pKBIqInx36V_ujDFp6ogqLhen4GW9TSB7mLxXaOWwH4tlANGUsKu5GzcmOYsIMPtfREfjsRJjsJtakSfllIFKjulfzxstldnK-4k2IUrHesV8kLi1DnvokpZ5qqD91vFgEloitXsQ4sSHdt-Ql0azK2BEvQ_yPHfyyiKBT5h2rGbvRAp5aBbmFj-p5-fy7SXds40i_wP0kEWariZ9nVcYnSlF8ny8sreDAEIVToYRd__ipGIGvv7oUSvQqJWUR5hmGJtJzltgV6ttNTXinCfMVyJyo4Mww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f6de555a.mp4?token=AQ49WFMTHc6r-ILl0I2p3Pi4j7SBKsVTnOLhTuYoOFURrZ-b_pH3W3_6pKBIqInx36V_ujDFp6ogqLhen4GW9TSB7mLxXaOWwH4tlANGUsKu5GzcmOYsIMPtfREfjsRJjsJtakSfllIFKjulfzxstldnK-4k2IUrHesV8kLi1DnvokpZ5qqD91vFgEloitXsQ4sSHdt-Ql0azK2BEvQ_yPHfyyiKBT5h2rGbvRAp5aBbmFj-p5-fy7SXds40i_wP0kEWariZ9nVcYnSlF8ny8sreDAEIVToYRd__ipGIGvv7oUSvQqJWUR5hmGJtJzltgV6ttNTXinCfMVyJyo4Mww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رئال‌بتیس که خیلی شیک‌ و بی سر و‌صدا خودش رو در جمع تیم‌های برتر لالیگا رسونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106848" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106847">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=mzv25Ypm1AHeW1Huk2y8lZ4fnswmVKMkSDGrQBTOHCZ1eN_7lgUfIVEVEVtxOQDXoWWogmSn0a7jdWV2MkQjQJgeK2cZUfcDC7GZqSaN2b9bKwdl2NU5RwX65ptabT7OW_vSnB_TWYQw0h5tWfj_Ik1tZZzjh6PVdRbn6TV4v0eiHK24x6ugE_Ke_CLuwinDxIfiI0KlhTt0DFJj7aSd78ztle6relGzDry9PnYpSQPspsI9QFKITGxXOp_6HAMjnMLRTbdUF6zhEk8ViOkdUtVFMucGhob9svvHrRtDFnd_Bo9ZPsCltbhL4Hn_GhFOpVPCky0TZTX6v4730BEUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=mzv25Ypm1AHeW1Huk2y8lZ4fnswmVKMkSDGrQBTOHCZ1eN_7lgUfIVEVEVtxOQDXoWWogmSn0a7jdWV2MkQjQJgeK2cZUfcDC7GZqSaN2b9bKwdl2NU5RwX65ptabT7OW_vSnB_TWYQw0h5tWfj_Ik1tZZzjh6PVdRbn6TV4v0eiHK24x6ugE_Ke_CLuwinDxIfiI0KlhTt0DFJj7aSd78ztle6relGzDry9PnYpSQPspsI9QFKITGxXOp_6HAMjnMLRTbdUF6zhEk8ViOkdUtVFMucGhob9svvHrRtDFnd_Bo9ZPsCltbhL4Hn_GhFOpVPCky0TZTX6v4730BEUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇸🇦
استادیوم آرامکو عربستان که 2 سال پیش یه زمین بایر بود حالا تبدیل به ورزشگاه لوکسی شده و در مراحل پایانی واسه افتتاح هست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106847" target="_blank">📅 10:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106846">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=pPTnGCykkEdfJkATlVONWsL3uqTDYHAvPmblABFU6vnbZcebf5wN6A8816Edv_62ygYKUBxLViTY5AH47Ir7UM2g7q9Z88Go-rBhkG1SRGzJZVpJcnov8x7zykgJAdWtzt6nL3i-nlcYekdDM448qBy-hSidH9wkZapetENP82LeAU_TQR66yfTA5pj_-R4FB9U4e4HQaGENg-81Js8lrTyawsNPcrCHrTuFGZexzVfX6cM8fkGeQhZyA_3uXBRD_XtNq_U4y21oxrvFSCcFUUkOIzKKgCjNy-cFRp08AsXUFLyFU3rgtT6HQ-oLdzroRwFuBgda4R6ojsU4v8OsQIjoeEeH2oAQ-S1_Iag9HFJ6JzcFRtY3pdZrzQD2zpPxtVKiCvgeHXzf4AipQmQtv-OK6nrgmx4wFRj9jwBXrktFVemmrU4oSEdt-Me5y0HF4ILdubMO-oRbxzMtE1JLhSBGMkMYnr1oajEDJZHdRwVzS1Vm556x9KWYQOWkEJUZab4FF3hFCfJ0BsEyNkAF-DPuDHPGwmXf5ulav8PNggzrSZn6UAAVTSyFUHeXG03Lb-8JBwFldrm2jBz_hLVktOsm0xWyxUdGKg-03fHiX_zm0JicG1pzpiN9IfhHCj4eDwSkX4Y4Zxb9I1uhvlHHtPXIAjeOvMhjygCcyZjW_PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=pPTnGCykkEdfJkATlVONWsL3uqTDYHAvPmblABFU6vnbZcebf5wN6A8816Edv_62ygYKUBxLViTY5AH47Ir7UM2g7q9Z88Go-rBhkG1SRGzJZVpJcnov8x7zykgJAdWtzt6nL3i-nlcYekdDM448qBy-hSidH9wkZapetENP82LeAU_TQR66yfTA5pj_-R4FB9U4e4HQaGENg-81Js8lrTyawsNPcrCHrTuFGZexzVfX6cM8fkGeQhZyA_3uXBRD_XtNq_U4y21oxrvFSCcFUUkOIzKKgCjNy-cFRp08AsXUFLyFU3rgtT6HQ-oLdzroRwFuBgda4R6ojsU4v8OsQIjoeEeH2oAQ-S1_Iag9HFJ6JzcFRtY3pdZrzQD2zpPxtVKiCvgeHXzf4AipQmQtv-OK6nrgmx4wFRj9jwBXrktFVemmrU4oSEdt-Me5y0HF4ILdubMO-oRbxzMtE1JLhSBGMkMYnr1oajEDJZHdRwVzS1Vm556x9KWYQOWkEJUZab4FF3hFCfJ0BsEyNkAF-DPuDHPGwmXf5ulav8PNggzrSZn6UAAVTSyFUHeXG03Lb-8JBwFldrm2jBz_hLVktOsm0xWyxUdGKg-03fHiX_zm0JicG1pzpiN9IfhHCj4eDwSkX4Y4Zxb9I1uhvlHHtPXIAjeOvMhjygCcyZjW_PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
🇮🇷
آنالیز فنی جالب تراکتور در بازی مقابل شباب الاهلی امارات که باعث شکست نکونام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106846" target="_blank">📅 10:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106845">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=p9LQQhiTm3uAkP-bmKV5kQV4qTTGhJa996btoHQ85kC3mL0cMMKQC-Fwjv6qSzL01kOXRLBbgSfXyWxj4aaqb36Ale4WuJFqguhV2jSFeHGWR5AbqtD57xCJQt1uRrd1R2OeE5lM5FD5o0DMvP1vf_RQ_IVsGGmr9d_xIYaZHQqvM15D4ZdnGNtdo4ofaJxldhqbEtvJ6VsHj8l-aB7JaWcoV-5czWxNNLdqFPfyXF9P11Rxx5xT-XBO5phIsIq7QeSyTanWaI4-6gZyczw_GM8sR0eMaseJnXSggCtLFq0zTXOfVqh0N1eKs5h9XPMivrHtSdRSGmh0jYokRl3_yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=p9LQQhiTm3uAkP-bmKV5kQV4qTTGhJa996btoHQ85kC3mL0cMMKQC-Fwjv6qSzL01kOXRLBbgSfXyWxj4aaqb36Ale4WuJFqguhV2jSFeHGWR5AbqtD57xCJQt1uRrd1R2OeE5lM5FD5o0DMvP1vf_RQ_IVsGGmr9d_xIYaZHQqvM15D4ZdnGNtdo4ofaJxldhqbEtvJ6VsHj8l-aB7JaWcoV-5czWxNNLdqFPfyXF9P11Rxx5xT-XBO5phIsIq7QeSyTanWaI4-6gZyczw_GM8sR0eMaseJnXSggCtLFq0zTXOfVqh0N1eKs5h9XPMivrHtSdRSGmh0jYokRl3_yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
امباپه: "اگر میتونستم، کریستیانو، زیدان و رونالدو رو به رئال مادرید میاوردم. من فکر می‌کنم آدم کیفیت و مهارتش رو هیچوقت از دست نمیده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106845" target="_blank">📅 09:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106844">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nx7wqlCaqOfNF-gHymowbmCufZ5vN30BCkyQQAGJEoRqUjLjOuUbKw2LEgjIkdNAEWLNveOH4dhzdkqEqIZvra_9GvglVQcus8UQUBYm8A3U7JQoY-rZxp51yK1piqNGOAWMN6CUC1N9L2izi7BgUY_Xk4vxic5hjrFyWZcd_fQ0YwEPm5PIoZ1jrnRTeixTMTs31a7-KvSj7ucBtbr94WmGImexqnTpN97DzYPtc0JqCxT4JHcjEE_PQLQcSmcufOUsAp7E-IQY2FkLIEUJNm2-rJXhZgD96Gyf4-TU6uJVQLh2VMLNwEXjzBE7j0YQkP0vTFOQjWAwnoDkD_yijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👀
از عجایب مملکت؛ یک‌نیسان آبی با ۹۵۲ میلیون تومان خلافی بالاخره توقیف شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106844" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106843">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=d0ZLV74CXAdLII5ERbnaPgvRGXIOhxi7GJIttzd3loKJC50ynnk6tFBsc9ce-CsdLlbSdZtte7P28lhq4KdpxwWDaSm1h0alroFbtR_2f38GAII2a_WdSBxwhX0jMfDH5AlkHFK_pQnYD7cNvMCs7D-JKq2CzWMUvOeB_K7Y-LIyc08GxirH-AdGN58ch893qR6CCLGWPKE4MQJSSVNUQGuNQqOeR92OfXcawGLIwSVKQkRmeCVmrPvjiELcS8tVsZoapI0S2C2BQznwctbO0agDZ1df2QEXFBHbNNmWG94OkhKELhA70_9SPVk1H8YVW6y6nXTw70N59FZpdu6HxTAD6I4Fk7oNzZuTk1YmnSvMe4F95ZSa0-n3u6PX_beKiWX5Yl83Io3muIKbC_7KaQoU3BJEid0F5n2PdSHixMA97sSnNo6xRpLSaDljwqksVazzPojnjDeb6KmKbp3jorELVUcJWaAG1ByC4CajcOtekUFmp1cxTFTVppTZ4rPlnIvhJ3ajf5eDu39l4zBbNV2iPfRniaJnse6Tql2Y_DoqtpI22Q-KH8ej33DyJMecur_UWj2hW-Jud-T3-d0d2WtxAmyKNNLIEmKwK89qkKbfCCPgcWGcNN1U-oDSP5cKdscrdzOJ60nfOABR8Ul22uTkGb-7eKU4Ru2B-751O1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=d0ZLV74CXAdLII5ERbnaPgvRGXIOhxi7GJIttzd3loKJC50ynnk6tFBsc9ce-CsdLlbSdZtte7P28lhq4KdpxwWDaSm1h0alroFbtR_2f38GAII2a_WdSBxwhX0jMfDH5AlkHFK_pQnYD7cNvMCs7D-JKq2CzWMUvOeB_K7Y-LIyc08GxirH-AdGN58ch893qR6CCLGWPKE4MQJSSVNUQGuNQqOeR92OfXcawGLIwSVKQkRmeCVmrPvjiELcS8tVsZoapI0S2C2BQznwctbO0agDZ1df2QEXFBHbNNmWG94OkhKELhA70_9SPVk1H8YVW6y6nXTw70N59FZpdu6HxTAD6I4Fk7oNzZuTk1YmnSvMe4F95ZSa0-n3u6PX_beKiWX5Yl83Io3muIKbC_7KaQoU3BJEid0F5n2PdSHixMA97sSnNo6xRpLSaDljwqksVazzPojnjDeb6KmKbp3jorELVUcJWaAG1ByC4CajcOtekUFmp1cxTFTVppTZ4rPlnIvhJ3ajf5eDu39l4zBbNV2iPfRniaJnse6Tql2Y_DoqtpI22Q-KH8ej33DyJMecur_UWj2hW-Jud-T3-d0d2WtxAmyKNNLIEmKwK89qkKbfCCPgcWGcNN1U-oDSP5cKdscrdzOJ60nfOABR8Ul22uTkGb-7eKU4Ru2B-751O1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پورن‌استار ایرانی که در ایام‌جنگ اخیر با دختران خوشکل و زیبای اسرائیلی رابطه خشن جنسی برقرار می‌کرد، دست به توبه به درگاه خدا زد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106843" target="_blank">📅 09:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106842">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DswcDbWfGULuUXulKAC0G9_gCV5EwzFRj330OmZ1w43Xm3QazCu2egzLgu-cgKcFuIaW_z48FKzPGkzru62repqT4aNDQDuAqkk9yn61z1SxUY1hgVChxSLEmsnOdp-5XEkrPmkHCM6UxuRDB4xUgdDb1ZseQFsszaa3Bi7esiCWGZ5tr_BrfeuLxxmoY1MmrsMaImvHXWYvdb4YLGF-6BU_boA-COCHnP8z_7LIvxrOmiS5jbT7u0lVnyeXqnP8ComH5RgQyNZZdJJ9BHWQSy5R_yO6GD1FVC31NA20bD3gYUPcTFtjVoT1xxw1AskajA8HIzi8Bc2Z5gfkz75FLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔥
فیتیله بعد از ۱۱ سال پخشش رو دوباره از شبکه ماهواره‌ای Fx2، شروع کرد.
هر جمعه ساعت ۱۰ صبح.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106842" target="_blank">📅 08:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106841">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=NHwus-djbeTKHQFYhvaA9bWam1vqjoRuaMEEWr__hvByrjNRO5AKKSI92pPpP4XVvdRQCfjvvdEnsQWSde8fkXe9N9JTuH1HsjQ0AUSogQgdDdn44PrPc6oD584uX43P6BRamM4EC_UIeJKXYaZcd_XppVbVU5TvDSSGJ6ADCKVqYeMCKJFer1yMJauqfeODEMyw3TWmjF66kMdfm1jIY7k7AScQB-pMC3TsJhA7RdJ8O630_J8W4btJ7u0bFNXWihhXVErWnv8D0xTI1GuomAKt8Ar53aXhG9bhPjgm-FpHnwiJGFEo0kXjgaUU0UKAVzspwpx0sOzn5l62Z2ABmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=NHwus-djbeTKHQFYhvaA9bWam1vqjoRuaMEEWr__hvByrjNRO5AKKSI92pPpP4XVvdRQCfjvvdEnsQWSde8fkXe9N9JTuH1HsjQ0AUSogQgdDdn44PrPc6oD584uX43P6BRamM4EC_UIeJKXYaZcd_XppVbVU5TvDSSGJ6ADCKVqYeMCKJFer1yMJauqfeODEMyw3TWmjF66kMdfm1jIY7k7AScQB-pMC3TsJhA7RdJ8O630_J8W4btJ7u0bFNXWihhXVErWnv8D0xTI1GuomAKt8Ar53aXhG9bhPjgm-FpHnwiJGFEo0kXjgaUU0UKAVzspwpx0sOzn5l62Z2ABmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پاس گل جالب دنیس درگاهی با ضربه سر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106841" target="_blank">📅 08:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106840">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106840" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106839">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/106839" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106838">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106838" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106837">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2L15TW6v_Z_u51MIrPBuCJjEOamJ_nMcKJSOaxagVnskuYxJRzksQ3v_mutM8-Qw6vjWv2OkxnvFYRdCHiIgmJVRUXQUZ-XvxWJ1cm8lJYkU1KHg8c0_-Gkg1l0JHFfCqRTEgD7bPb8eYHpqDoZ1TKifNkSTBT-ySxxde8TwfQ5McOKlBqSEIwLgZz6qS-PsJJV-jhZM1YupIIMvJVsHaUATAfyjGBxk97UBrZjy8VvmQikujHCD6bSTS_7qok9OoCXPEHsu6Bx1RiI-eVIzF3yA-gArPEWZYf0FsL2tT2HvuyPRns2_wMrt5IEjuPcjDau4iMENr2y-p3CJOMDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لامین یامال درباره علاقه‌اش به نیمار:
🔻
همیشه سعی کردم بازیکنی باشم که با خوشحالی بازی می‌کند، و نیمار تجسم واقعی شادی در یک فوتبالیست بود.
🔻
نیمار از آن بازیکن‌هایی بود که فقط با دیدن بازی‌اش لذت می‌بردی. نوع بازی‌اش باعث می‌شد تماشایش سرگرم‌کننده باشد.
🔻
تقریباً تمام دوران کودکی‌ام، صبح که بیدار می‌شدم یک کلیپ از دریبل‌های نیمار می‌دیدم، بعد یک کلیپ از گل‌هایش... او واقعاً بازیکن خاصی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106837" target="_blank">📅 00:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106836">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3qxEvhfk8aJ9Wg3Cs9Vg6d8S8-alEW82BygPTiyrTtJfdxqxeFcrhoN6VfvjRoBA_IGB3vpoVn_9ukqlekqyz1eshp-qR_7yMGFo650Ed45G826lfXpK23HQ8ZkM4KlVvoxAEYzSxb-k2wpY5XfQKXAegPQNkjp1Z3OxXOaocKlACUsj2lU2G17Jd9Qh-YGfO33GoIz8gl5s3W6EKQCdPnGrx9wj6pJ-DIHsgghmG0MVBwHk2dfuoCadAFG5T4EPM_eDNgRlXgUDKoYFluYdjFAnT2QCKUHPY9TEK-u8m2W_4ilC05V4ZYPFvR8ctNAk-xVKgx9P8Rae5WVTvgN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
يحیی‌گل‌محمدی و تیمش دهوک در هفته هشتم لیگ‌عراق مقابل حریفشان به تساوی رسیدند. این ششمین تساوی یحیی و تیمش در لیگ‌عراق بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106836" target="_blank">📅 00:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106835">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGOmgahTmEVvAoWiOIZA7JODkNFnv9mg_98qlLwgQ2x9Y8e7WARMZYIgspkzesi4ljakTD2U1-S-1ItpHRNzl632mBzAqSuxCf3BfxTM_8Ce9B28JI126AMeW859YGNurEJRdZk2C8dKg4Odmt78VNM8UMdV1VpB4kWatmqW8uCHIUWJPdxxuX3myGUqtmfyukzg2TCoVtJWxHniIqX5Ff5zuhTEzj5BjRWtvnv_JmU7-q4kxSVUYat-EYYeef1ofxMpD3O8iec-CNPl9K2_ZnCYUmhH4mNHnBShG2vRcpkD1vYr9XpG3AFoxdKs-X0bnoA-P9pF_Km15UynWnzppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
‼️
لامین‌یامال: تا پارسال پاس گل و دریبل زدن را بیشتر دوست داشتم ، اما الان گل زدن از نظرم بهتره ، گل میزنی و تمام، کارت را انجام دادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106835" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106834">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=aEGTUn8gqhw9PPC5VI0RXbtz_6_cG_tCClpnQSik6YvHR1MSBDO-WzWxDNe_9wGvsCsGtcf8peZFlnlZk86A5LXOG5MuLUY9gK1MSWR0Hgyu5dKDxGqzKPOAkbKbx56PMdl4B0h8cVJMOUt3ZhIsfvDAAnrZ5oLRW_Ttu4nRcVrQMrWvQ6LXUiU3Bu3_SGMnB41_vv99Mf45qQuG6DE7x1I_eP84N0h5RRBiclhkattMwMvKZJOkwYJdgN0gdWJT-9KDfEwFQKYxUxQAP7AQ-byZjj1FflzgCJGNLFriDr_0-hbMHLAn9Py1VbdM3yvVtl-9dXXfDwaZ3EQUHYnWzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=aEGTUn8gqhw9PPC5VI0RXbtz_6_cG_tCClpnQSik6YvHR1MSBDO-WzWxDNe_9wGvsCsGtcf8peZFlnlZk86A5LXOG5MuLUY9gK1MSWR0Hgyu5dKDxGqzKPOAkbKbx56PMdl4B0h8cVJMOUt3ZhIsfvDAAnrZ5oLRW_Ttu4nRcVrQMrWvQ6LXUiU3Bu3_SGMnB41_vv99Mf45qQuG6DE7x1I_eP84N0h5RRBiclhkattMwMvKZJOkwYJdgN0gdWJT-9KDfEwFQKYxUxQAP7AQ-byZjj1FflzgCJGNLFriDr_0-hbMHLAn9Py1VbdM3yvVtl-9dXXfDwaZ3EQUHYnWzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمد تقوی، در برنامه هت‌تریک درباره پیروزی استقلال در برابر السد در لیگ نخبگان آسیا گفت: «استقلال نمی‌تواند در لیگ برتر مثل لیگ نخبگان بازی کند، چون نوع بازی تیم‌های ایرانی متفاوت است. دفاع منسجم استقلال اجازه نمی‌داد بازیکنان السد، به راحتی بازی کنند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106834" target="_blank">📅 00:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106833">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=iCMK56kUNs4_T6BaBpznsx3xcZa5D_hG_0brW_ERhc0iepUV5YBz3iLLhbNlnhHi-xOV1PlnDYMbwlCvXRlf5uvoSbbbd4kVbfzNvzGQLwJwI5aNqLHRegBJYBXz48uIk9sdNw8NamEdAALc8e0a7ctn0R7RqEbAfx2Jcj8Df0cRhHzQLktLwDZbcXOSa_lruaB9DHM-0eQXEehV67NrOnKAvjVaFZURsNjjeIwTP5J8dzvP8NVboaV0q70dR4VzUX2cbxPvZSn4-pUgVuI6iBqjMhbG96o_2j1Ba3cY5SpSGbU9piuGoZQ8qzhkOJQ9pVlwaVBwj2VvOEre-EI-eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=iCMK56kUNs4_T6BaBpznsx3xcZa5D_hG_0brW_ERhc0iepUV5YBz3iLLhbNlnhHi-xOV1PlnDYMbwlCvXRlf5uvoSbbbd4kVbfzNvzGQLwJwI5aNqLHRegBJYBXz48uIk9sdNw8NamEdAALc8e0a7ctn0R7RqEbAfx2Jcj8Df0cRhHzQLktLwDZbcXOSa_lruaB9DHM-0eQXEehV67NrOnKAvjVaFZURsNjjeIwTP5J8dzvP8NVboaV0q70dR4VzUX2cbxPvZSn4-pUgVuI6iBqjMhbG96o_2j1Ba3cY5SpSGbU9piuGoZQ8qzhkOJQ9pVlwaVBwj2VvOEre-EI-eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
گل‌های دیدار بایرن مونیخ - بوینیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106833" target="_blank">📅 00:06 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
