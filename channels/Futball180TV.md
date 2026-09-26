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
<img src="https://cdn5.telesco.pe/file/uzU0bHE8WD7WLD1RwrUy61HU63NqUuMbybJyaDwe2uMEWy-sY8kJBkNF3wDbNPJlmbjmKYpOMIvSmmjzHwwX0XH6FeII2MwZbr2YgW50TzttE7SKep-pC0Jz8wZPiSDdsvKlAigj6kbmPw09Z42NN9wYTb4jp9es8F7EDBbDmt9bIhbhpJlTArGKpskuqhxmyZXgBU_TZoxZnY-zgtLYoDbEpkqKelZ7Ext0yE9wDoa8PIyTdodov5BmagSUrsTuAMRHNNxbyVoGt5BzLcTSzb1N3s7KqLPTN-aHqUt1N31ZFaMw1fpHCQYhqrcBrk3l0zW_nwIzjdYsq3y_fTt9sA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 400K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 23:30:39</div>
<hr>

<div class="tg-post" id="msg-107337">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/Futball180TV/107337" target="_blank">📅 22:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107336">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=LQmiKNiLjQDTpOeKW21ADsZCljmtP-j32XHhI7l3n6DHFrj6Du1VNjx4MxSxNtzZW0CDj4DVAIxzQulwoT98Rd99IAQV-vjlbMVw0_9lgtHiaK4ffasmZq_8u9ZvEXnMZMVhqFGAB_RSckJ2657myA5tK6PLksY6Tg7F5I5BSb7GrFwKuxzVgs4aLDnmJTapUYPJlZND7o_veB5CKfoSaTOPHudPQKfh5Pk_LupetEx5FW4Lm9keh5zIlnJlLMyq0tEDYhqUseAhFysghhCRRm4ZNHHC4fYkopnvxO1HJ0XN2RUEnop0FSIsR_8dyB9lAdB-o8YbMOxEU9RQFJokKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=LQmiKNiLjQDTpOeKW21ADsZCljmtP-j32XHhI7l3n6DHFrj6Du1VNjx4MxSxNtzZW0CDj4DVAIxzQulwoT98Rd99IAQV-vjlbMVw0_9lgtHiaK4ffasmZq_8u9ZvEXnMZMVhqFGAB_RSckJ2657myA5tK6PLksY6Tg7F5I5BSb7GrFwKuxzVgs4aLDnmJTapUYPJlZND7o_veB5CKfoSaTOPHudPQKfh5Pk_LupetEx5FW4Lm9keh5zIlnJlLMyq0tEDYhqUseAhFysghhCRRm4ZNHHC4fYkopnvxO1HJ0XN2RUEnop0FSIsR_8dyB9lAdB-o8YbMOxEU9RQFJokKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول اسپانیا به انگلیس توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/107336" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107335">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسپانیا ییککککککککک</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/107335" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107334">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">لامین‌یامال زددددددد</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/107334" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107333">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/107333" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107332">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtcNZAI963K7MzrPiPpLdT3qG26a6hTqhujuR4jEHQebgpPGXQuDjw7ZHs7fkMFrizmlHBWmiTZu7CNJ1-rlKyrrSkngp7kbwTR4XPMCaOyc21Spn1UkHkDHt0JafQXfMprk88GLqJjIrx3jTHu1UTT4NCt1hf8f_RI6zuXUq0JB4hlw_2pdqmMeJcnQNAp0oAlak1EqvlAvUjNN-tTxuquEtRFJqWbkZPzC0H0402d82wLynhlsYFZCiHlscXA6a3xzqkJrYUsDphlTPB_cbhVKMzZd66ENlIc0cgO2HGhyPBo-IKgZmZM7h4c2D_FgyYXtPa7pBK7dV5TaBLKduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/Futball180TV/107332" target="_blank">📅 22:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇮🇷
تاجرنیا مدیرعامل استقلال: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا میگویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/107331" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107330">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka0cDNi82DDVPfPiKGyUIOsrg-9DAbvXmEWwPXuF--rn6h26mw44kb8z2AUI9nBved4G3Av2mqys22dmZLo92HsjeKjHoGQhM0Mx5UBR5S__mGbVgzmXyG87a0z8q60oVozZ6dqc2Qr7P_OiGa0Zc0HL8BO7lFht013RJfyUyW6UBcvlbRvwdkPmiV-10_LYwlOp8DnG5XKj_bOSQYYxSPPf92CRXyKE4aaxG8OrftPL6-dMToTSqKKXNqeVPspw8rGBNv0SunShjZFJcEeygKEs-sA8GDHgc7-NpwIENuP9Mb3cv2il4sHle-4S0LU3sVd9LRk01z3f_SEiDHxOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107330" target="_blank">📅 21:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107329">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwIxbrehJEtu5r4ydtTEPZLqSaOYGQLlaMz9-50iMQJ0btbcF9715q466Iv8lOkOwqkI3WS1l-VczskTVEZL5foNENNIZdWIIHBWZUPjfykko0t7jUSSzjR4jAYiAz3sP9o6Lc3NhJaM-nGtvQbgv0qDGgudRltSYUGQJCdSdfbcJSdRDNmVGodRGXFtIX398Jd59c1pmQA3xMNdCH2pzHTbaJJI6BnAHwfVkgmhA25ewIFC9SEyZ12t70VeEBzQvTG9t2rCgJPzgUN8kxl7zQVGfzPRKh9_LoaoUR_OHr8pVXRfntn1-mwKcwX-uIqYjwVAvkwZv0sG_GTRlv4FuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آمار تقابل‌های بین انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/107329" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107328">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV7WHRDf36BDZhmJgbxph6oBHysEIx-Ep8j0Nm9WcKROhJqbZununRezyHQyBEAvZbk4InnFyi-m9P7feJPGGwTH8jtHh5xiB7LsRx9RtzXeJ-baFzcYVU6BNhwXsDMu4sgZdb40kpK12k7qRdmjG1mv1J8pQmqOx3-RwXWFuW5NnP9PJnWfA-3E6sMD4_SHAlKlKQR7S1VPk5HYkoE1tm8o10y6v7pQ-GWzZSzqye3tU1FxmCoHmjnvVS-X4_BVz0oJ9tzfx21MGpzDSuogPegV5rC2D4fS6Ds4fbGj_eyuAuIqhrVPJyTPTQnoILAlSMT4gNpPULKKPCl3NjhaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107328" target="_blank">📅 20:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/591cd9489f.mp4?token=hjWiDxzHJu-UtYwVuWLape1m8UvihnuQjP3qNTkThOERh8btWQY0b7eSDc3qUoDDiUeoRh73moxNIHVj3TIqrsi9jGKvFWhCwIYYwXS05caOxbQjnDHWfU3ZR08vWry57cqOqi19931v2CgJw8EVDqrR-s5Da-VviB84DPSgJoeExznMD-GNriOFrA4i5DGWnpKbesoD_fmW6VpFu85sqvt3JyEDFciHm3s66zDT1YldMo4RvFtqgj-t14rWj8vzfVwxRYj-dS1qV4dGFXHLu7Geww_Ca4c3zQ1O9rr_661LYTw8GIB5Z7NrMOF7_BueaXkvzwFJsSfDlNJST16FRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/591cd9489f.mp4?token=hjWiDxzHJu-UtYwVuWLape1m8UvihnuQjP3qNTkThOERh8btWQY0b7eSDc3qUoDDiUeoRh73moxNIHVj3TIqrsi9jGKvFWhCwIYYwXS05caOxbQjnDHWfU3ZR08vWry57cqOqi19931v2CgJw8EVDqrR-s5Da-VviB84DPSgJoeExznMD-GNriOFrA4i5DGWnpKbesoD_fmW6VpFu85sqvt3JyEDFciHm3s66zDT1YldMo4RvFtqgj-t14rWj8vzfVwxRYj-dS1qV4dGFXHLu7Geww_Ca4c3zQ1O9rr_661LYTw8GIB5Z7NrMOF7_BueaXkvzwFJsSfDlNJST16FRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
توصیه عادل به بچه های کنکوری
😮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107326">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی…</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/107326" target="_blank">📅 20:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDBpM9jX9xOhB8CZPd1vsgk6bsS5-UkPeWcydlsm67bdPZez5xYP06z0-ED0yLhv6DIRcX9GhPUbyu5sYQGlfLcXBCZGaPtE7uRtxEoRTpHVuTvjotkP53lKuDKdMMCETcUOHsdoxiQWD43ceiHV1i61g5-1x1BybTQDascMmNazUNX-ABJoW13Cjz31IyHN1NM3tDfIwAVfXPOeMh1Z7Dq9wRHOdaJEJZDS5kIrDA0PVVUfw4sR-i-3u-Zfi0ODnovWp0l1r37IZMhe_X17MK7TF85sYfcYpZr6qZ9_SgEq4fF8fulcLoeWtNo2evDFvw2X8Nn6yhKGQX4JKnQ-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر!
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/107325" target="_blank">📅 20:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107324">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUSqJduvM2oaAPDiJ2wQ9z-k6u0hrZm3MdqGSDV24d9TpK9p_s6aNlmP573Zmn8Cgkf4zI3x-RH2d7zZq0HGk8PkFixLUIMRCTZfZH4KxZ2F3ASiPk6U_utBzTX0SeLKgyUoODJ1CPhjh4gsaSyVY9qM6srSaH1buquO-39G4nmY8M9fuVdqfLWXd_ZEtIOjsZh_HWvWyiRpg2u4Mb-yuZH5yhj57uPFiJ8zEhNjTFf_Cni2O3yR9xgLzgO-BZ3coFcWE39W-b30jYhA4dAptTDCwor0mEQC8TEVOmubrnpUSJ-IDPb12kLN1HNfdrqcGeO93B7OGQDXEr8vAEvMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👤
علیرضا دبیر: چطور مهدی مهدوی‌کیا با یک گل به آمریکا از سربازی معاف می‌شود؟ حالا هم علیرضا بیرانوند بخاطر مهار پنالتی رونالدو باید از خدمت سربازی معاف شود و هرکاری از دستم بر بیاید برایش انجام خواهد داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/107324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107323">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=KP3FsvcRa_TtDPOKwHWkZOpylWNBhbiRACcPwJaR2E6v8c66feL4Cf08D6nERs0dZKYpgfhrucinKda1Zq8k43JTz_aCnqeAFxBTyr_XsgjDcrW-EkEBvLD1W3dWrwCzTaWdE_7Eu20cAFPBIBXdR88y3fMIoAmErRQIWtM-n6DUd4iy8GYm3YmD2y_Ya1IR-ua9stU61EOmNPim6bWnxhymg3TXZB0y8g5-9EUDJB2ZMUCJss7kwvNjPRXRfUvFn2dUmNYlKPhFhKeSTkgrhuMblfl7Lt15_s6orVvc-k16sG-CPeCH62pjcQ-1Yk60BuJqvvt1-N9N1_aXO-AnNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=KP3FsvcRa_TtDPOKwHWkZOpylWNBhbiRACcPwJaR2E6v8c66feL4Cf08D6nERs0dZKYpgfhrucinKda1Zq8k43JTz_aCnqeAFxBTyr_XsgjDcrW-EkEBvLD1W3dWrwCzTaWdE_7Eu20cAFPBIBXdR88y3fMIoAmErRQIWtM-n6DUd4iy8GYm3YmD2y_Ya1IR-ua9stU61EOmNPim6bWnxhymg3TXZB0y8g5-9EUDJB2ZMUCJss7kwvNjPRXRfUvFn2dUmNYlKPhFhKeSTkgrhuMblfl7Lt15_s6orVvc-k16sG-CPeCH62pjcQ-1Yk60BuJqvvt1-N9N1_aXO-AnNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
عصبانیت‌شدید یاسرجلالی آنالیزور فوتبال از وضعیت وخیم تیم‌ملی با قلعه‌نویی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107323" target="_blank">📅 20:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107322">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🇪🇸
بعد از تست‌های پزشکی مشخص شد که کیلیان‌امباپه حدود دو هفته از میادین دور خواهد بود و مشکل خاصی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107322" target="_blank">📅 20:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107321">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=bJUpfOZbk5Ilm0Qb0i-oHAql415yOcvvwiDFXG_jFoSBzypvKSfSxFkmOjDrZnlYU96rr4UxGaa1n4JSKkjwdMUKZLHrgSmDJqij0bNloxYlxXjO7EO-q8uTJhvKgu5c7v5CuB7dt0n9d-uKcMRUYKI7QypMzJWBk_MiUL3i93xnj0wsCuC0bRiNok4ts8bhAa5ffAtyC3VTOZDzFI50BreCK8pys0-CZLdE6MPBBA2DLSu9AizscHbqRP8r6S8klkyXsn00Jrp_zMNP5Lyk0-p0a0b-mWy_xNOB_HvEjZzsWP234kkHgDKBhLObyO0mFJLXRJ7PXR3K-Dax0orYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=bJUpfOZbk5Ilm0Qb0i-oHAql415yOcvvwiDFXG_jFoSBzypvKSfSxFkmOjDrZnlYU96rr4UxGaa1n4JSKkjwdMUKZLHrgSmDJqij0bNloxYlxXjO7EO-q8uTJhvKgu5c7v5CuB7dt0n9d-uKcMRUYKI7QypMzJWBk_MiUL3i93xnj0wsCuC0bRiNok4ts8bhAa5ffAtyC3VTOZDzFI50BreCK8pys0-CZLdE6MPBBA2DLSu9AizscHbqRP8r6S8klkyXsn00Jrp_zMNP5Lyk0-p0a0b-mWy_xNOB_HvEjZzsWP234kkHgDKBhLObyO0mFJLXRJ7PXR3K-Dax0orYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تو مسابقات کبدی بانوان در ناگویا، کاپیتان ایران حریف رو گرفت عین گوسفند پرت کرد اونور :))
بعدش خودشم زد تو سرش بابت حرکتش
😂
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107321" target="_blank">📅 20:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=Q4WhJMYxl0YD77MjVR9EQ1fxPhRAegxlnEOnIAG7iOjRZQjwCHNpxwCc3DzZIOWtHRt7Y7_PqjYJhULMGzjsJIAKDLdIFKeyProawzc6dqtI3vLmfpfTmY5bDfQwqqy_N-OciqgyXHKIg2ynGue_QpfFGUoox-aBuvCBL7pII0xAcvqMNLzJTjwT-6J9aaPTnuQ8zTdqNpZZw1XeRrYcHGsZQZgbgEuoPz1wSIxxapc1aQVA_ovqnTZytbmEltIRMmPg3xeDMBJDpcPUjUDz-xXoFLKCE3Y4xGH3kcXdHuFWaxoI31ShPS-NYPevONR8wfFuvrOlvgQYWTn8XDUPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=Q4WhJMYxl0YD77MjVR9EQ1fxPhRAegxlnEOnIAG7iOjRZQjwCHNpxwCc3DzZIOWtHRt7Y7_PqjYJhULMGzjsJIAKDLdIFKeyProawzc6dqtI3vLmfpfTmY5bDfQwqqy_N-OciqgyXHKIg2ynGue_QpfFGUoox-aBuvCBL7pII0xAcvqMNLzJTjwT-6J9aaPTnuQ8zTdqNpZZw1XeRrYcHGsZQZgbgEuoPz1wSIxxapc1aQVA_ovqnTZytbmEltIRMmPg3xeDMBJDpcPUjUDz-xXoFLKCE3Y4xGH3kcXdHuFWaxoI31ShPS-NYPevONR8wfFuvrOlvgQYWTn8XDUPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
حمید مطهری سرمربی فولاد خوزستان: دوست دارم یاسر آسانی بازیکن من باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107320" target="_blank">📅 19:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=nc7AuqJ0PeSA6qAiFNKtzhsxv5_-elSSSIwivZmQ3fXUsw9R1I0Ttk1Ugt39ul0vs66VwF3kvOhV9k633sGLaV4nupnLJprFIgNZz78IOmAzNhr_UTwzgRfn6Y3Kj6NDszAkiaixda-rR3XB7dFVphwIqpyGYy0PCiMnF-nYMdCZHvhWaj_GITCQBqD4j5DSmkBWEFGHJ51bxezF0G45-cQAvfl62diKdFsaon5fsQOxN9Y8IlGw7HM74lbXVQXVt8a_OZC7f6bLm6cm-CbI8yNIUlk8eKUMqUM2lpf2kqjQ8KOUyFHbQxlUY57d1zhk4UVcmLk_eNXvKYFY0tLaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=nc7AuqJ0PeSA6qAiFNKtzhsxv5_-elSSSIwivZmQ3fXUsw9R1I0Ttk1Ugt39ul0vs66VwF3kvOhV9k633sGLaV4nupnLJprFIgNZz78IOmAzNhr_UTwzgRfn6Y3Kj6NDszAkiaixda-rR3XB7dFVphwIqpyGYy0PCiMnF-nYMdCZHvhWaj_GITCQBqD4j5DSmkBWEFGHJ51bxezF0G45-cQAvfl62diKdFsaon5fsQOxN9Y8IlGw7HM74lbXVQXVt8a_OZC7f6bLm6cm-CbI8yNIUlk8eKUMqUM2lpf2kqjQ8KOUyFHbQxlUY57d1zhk4UVcmLk_eNXvKYFY0tLaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇧🇷
عصبانیت رافینیا بدلیل عملکرد ضعیف وینیسیوس در بازی مقابل استرالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107319" target="_blank">📅 19:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107318">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO2sTbwt_sv-qrcjTNEkJHkgdFkHt1HJUW-IirgGXlVQnq698vFeWunMIOMjgFYOpWmwnZVcW_58DlGRoreC2vkZzXVvgcWYI7A56XLxkofhSjL19enT1evfkX1OVT4T4ajV4myKG58KcP3YDYXwI9tOfD73GRwgb_899kJJoHXRi8LVJxSp4tbY0IuOWI2Qt-pGIVJsmqY5uq27NYkIZvOJPxCgPTh6ZOlNNIcMv-KOcpxU9_xGvWG7s3-wrcUSNhv6i63vXoBl_emeZ_Nc1FdBCvaBVEzsY72cICGuSfRlbGbXX9lmqVwfajv98DALFEuV7Sh4w0S4UOrbmkFAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پیام‌تبریک مالک باشگاه استقلال به مناسبت سالگرد تاسیس آبی‌پوشان پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107318" target="_blank">📅 19:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aq8cB_xZ9TbuJAbE3_QJIEW4l-0TvJiFYOsl7VqxTh-F8_KTNSfTamanBHnNy2MpBSOqo9CkzZltwANPI6YLn6wlupEnVbC1rkyWqAnmw1IOmlmvWaE7orCsJQyp3s_NaB1LwFSzy0ELT6RW_AzE83MwoSDZozTa4G5nbA3zfnmdtxShLtKkp-qZlAd2zJNLcIMPz-50AzaAXYtsSjynU3K3kSykmJgPI30-JWmfdoCDHfY7RVS1x5ozsR34y9kXv87U6FJgImS6YdBRXL8qYTmloVrnqwS3mZDcfB4EcAVuF76Cu5YwWwB1lX1JR0p_GpeVvZIz91fCr5_rv2kXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چند روز پیش موقع آغاز سال تحصیلی تو تهران، تو یه مهدکودک مربی از بچه ها پرسید شغل باباتون چیه یه پسر ۶ ساله برای اینکه جلوی بقیه بچه ها لاتی پر کنه بلند شد گفت بابام سرقت می‌کنه تو خونمون اسلحه ام داریم
🔻
مربی میره به پلیس میگه پلیس میریزه تو خونه این پسر بچه میبینه چندین اسلحه تو خونه دارن و پدر این بچه، رئیس یک باند سرقت مسلحانه از منازل مسکونیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107317" target="_blank">📅 19:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xcb-6f020xGg4yUh9XrMI816nO_WIbt_PXG0WEFv9TEVvfPXIXKGTGYVnacaMiGy0eje50qrOJSgHNs2Jx5PkvQ1FLXNVx_Lr6VZzxhDiZaDxuBKQxRBGLhgZG5v3W20amzjU6tH00BGSvqUgm_v84o-go5VL1E3ylUo3A-kYUGt-N5NCUnXUyIPVxgucnMriYefVJw7bsZEQZMcXjy3GnlzmKJbz6tQdvAD2Ub2626fIbUZ3sZY7FvmqrJ011VJkJ5nmOpU8G2JJsxQfRrsdR92wRiNeiezIioWTYyEny-3ccr7i1oyg4wIIdJJANejCOKuAdggVUbkBpY_XTC03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
تیم منتخب انگلیس و اسپانیا از دید هو اسکورد به بهانه بازی حساس و دیدنی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107316" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107315">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107315" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107315" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107314">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKSBBY_7KsrtjNizvFOseIR1DI7bgX7PO2zL_V2D8EYr_CruZk_trA7Ohur-GlTOaMt9N7IOVzSGMdx8MaBkjiXzSy3UqJfCjvRFeTv8s0zRDOHfS8QsPB06ZDCYOza_PCn0Z9NnOw85GUpahKhbljNeafyGCghPzpez818on_VBAnVO7AW6ogZtG2m6V_Um6bsQcsnon6RWCS-Xu1Wl3NScjTp7ApKPmcZOUvIkiz1kB47n41zdySsaKRvcVUfL3mdj-ichzFipZE5yOjxn0CVYolqcPA0IZVZyGbuZ5gN4EIlHDXVQcEThbPr3MIfR0b4NP_XjsKzRV4lPLKCzBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107314" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107313">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=clHPZluLud7yn49YsTuGkvF9nThinFwuc8cft-3qeXd-M9iGrVkyYZO7rSqIKu8ripK7_4b5SRrPLtlxYpDTfOjJ0dT1r-17ecUswWjoUGN7B4ff8jFOaSlzinVe63SwTE3yQn6gMjvqFIPiL_l804MLKoVz7kb5E_cZmX9ZHYt1CWeME40h5wvMdZHW4f29r-gZd9wL0up44lKmONd83cIuLtKhTYzdYGzcfXf_St2NXiczLsbo5LJBcZTuNM68wZ0qI2GoRHI88l99N5fDu-N6ZzRQhisyTesSgHNS2GswC7QnD03Un1207RAawXrNiZNQp0QBDJ-Dhhue2TiuXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=clHPZluLud7yn49YsTuGkvF9nThinFwuc8cft-3qeXd-M9iGrVkyYZO7rSqIKu8ripK7_4b5SRrPLtlxYpDTfOjJ0dT1r-17ecUswWjoUGN7B4ff8jFOaSlzinVe63SwTE3yQn6gMjvqFIPiL_l804MLKoVz7kb5E_cZmX9ZHYt1CWeME40h5wvMdZHW4f29r-gZd9wL0up44lKmONd83cIuLtKhTYzdYGzcfXf_St2NXiczLsbo5LJBcZTuNM68wZ0qI2GoRHI88l99N5fDu-N6ZzRQhisyTesSgHNS2GswC7QnD03Un1207RAawXrNiZNQp0QBDJ-Dhhue2TiuXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
گزارش جالب توجه گزارشگر مهمترین مسابقه هفته دوم لیگ زنان بین استقلال و خاتون‌بم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107313" target="_blank">📅 18:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRBj8tc_HF7cfrDI3zeyf3J1CzCH3I9XfgrZS0fTZE0baq7tWcPrce21ryXuwVfyImv5CpRDI2Hcw6_DBIz-SktiRvftsAzgjxzboVvKDFwhKxz8uA6H2hVK5D58lQcSXdcfCOyT2SjdU_zTlfh0uuWDQPrUoHiY-M8XcAxyZjmOsYStejB-XhA1FBkSPMucp_WzAVNf4u6dDtpbrB7TVBPPek0XG3fKltrK-O0ycldg7HWg_-zBCdz4iAylzvJtH0H4CXhO2uvqgi-icCXZI-o8c0lFZ2dBcFgjCRSi_DIjauOMoIjkPgRS08RExFaC2lv4sD7_JruxN421LeQxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودری ستاره سابق سیتیزن‌ها: آنچه ما در این سال‌ها انجام دادیم قابل سلب کردن نیست. قدرت و سیطره تاریخی سیتی در لیگ‌‌برتر هرگز با رای دادگاه از بین نخواهد رفت و قهرمانی‌هایی که کسب کردیم در عین شایستگی بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107312" target="_blank">📅 18:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107311">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRrlcVHzgjKtxCpDHLN6Legf5JXrdD3Yt9eyIm1QtBvo6ivC5mgfkEB0jNe83q9Pe_5yglTisGfkHlX_3Rf3j5ArkyjpDEuxKT0UylBEy2ebmIZKfwVDFdbWOhK3vTQE_jYJElNpbSDGujwGJqAJBsAj8iN_0L9cvX-HHG2-uOwUtq8eV6wuInY_z2fqJqZyb5LS-Tu0llurv5vGPNFS04wKtDRn3HbJ7NXHqEtf1hplS8CzgJ1Bdbxw9ztkDYT8uVI-f034l9ZPcBEgoeZKnCcxFHYmwZjsERE0qVcxOnl5shN7jIGyyJ-dZzdraiWCeoc1g-lUzjh-EvYTs4nRRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
لامین یامال ستاره بارسلونا:
🔻
من برای پول فوتبال بازی نمی‌کنم، چون دوستش دارم بازی می‌کنم!
🔻
بازیکنانی که وسواس گل زدن یا پاس گل دادن دارن از بازی لذت نمی‌برن.
🔻
من برای خوشگذرونی بازی می‌کنم؛ برای دریبل زدن، برای بازی با یک یا دو ضربه، برای اینکه به هم‌تیمی‌ای که هنوز گلی نزده کمک کنم تا گل بزنه؛ من برای شادی بازی می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107311" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107310">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
⭕️
⭕️
🇺🇸
ترامپ: پیشنهاد ۷ بندی ایران را رد کرده و اصلا مورد پسندم نیست
🔻
ایران خواهان توافق است و من هم از توافق خوشم می‌آید، اما این پیشنهاد غیرقابل قبول است. ایران خواهان بازگشایی فوری تنگه هرمز است زیرا متحمل خسارات سنگینی شده است. من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم زیرا متحمل ضررهای بزرگی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107310" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107309">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YB08Fge3tXi_a7fEpAOLQipIlo-S9BHp7G3CGjex9vMiKlZxZ3duSq2eM1nIZ7SzMPFCMHm7aEvx3dBxVdYWSm5q8mgLt_D2kFq_XorcJeBMQcnRdDtrOQIuMSvqcIxO_RVt6DqMY0xll-VIKYi4KFmKfDyUeB60T2b_qUfqIZOmf8UaemzW2OQDT3NDihLFxSkDJjku7S42q7kX29hPo8NakOZVyldjTd3kZFzSi2Etv_eiVCeMcYY63VuMfnVwdJNF9oJYlTbsANXgn5nCSL4DRgz8WpgMrDxvZVX8iwL8rr_ee0rM-bJEhPljzdRscole-npl2CUYKmvMyT_YV2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YB08Fge3tXi_a7fEpAOLQipIlo-S9BHp7G3CGjex9vMiKlZxZ3duSq2eM1nIZ7SzMPFCMHm7aEvx3dBxVdYWSm5q8mgLt_D2kFq_XorcJeBMQcnRdDtrOQIuMSvqcIxO_RVt6DqMY0xll-VIKYi4KFmKfDyUeB60T2b_qUfqIZOmf8UaemzW2OQDT3NDihLFxSkDJjku7S42q7kX29hPo8NakOZVyldjTd3kZFzSi2Etv_eiVCeMcYY63VuMfnVwdJNF9oJYlTbsANXgn5nCSL4DRgz8WpgMrDxvZVX8iwL8rr_ee0rM-bJEhPljzdRscole-npl2CUYKmvMyT_YV2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از روزی که رونالدو نتونست مثل قبل بدوه و هتریک کنه، موتور تیم ملی پرتغال از کار افتاد!⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107309" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107308">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=F5iHJJXbZs2sU8jgsoSMU5P4ZEe0kwgn8ITf8KcHyvBxF7DJpi5cyiEZBFZXoZwJn9MFFQuYuYEs9R_ekAobiFE6PizndbWyvIejjHzRqHjqy8-a2Ulsxp3ZB2FiZ_Y5kq54DL7J6f5g08vFtjBttr1fG4ulCAtvBathfk3bDinC9v6jAZFkooWuZFKskDFHj5vobUVJj0AFctRQenNvZoOnow5yNbDAhRAqoNR-ywASEV629RRHPTVyGxG8XniMsUyJcAQtasQQfjzeE_zVrQ8zOR1XcEVDR6lxEqAA_7F1KbegQzSvsWZfxlOVIiRi7BQW_upk5zJTraDTzmCFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=F5iHJJXbZs2sU8jgsoSMU5P4ZEe0kwgn8ITf8KcHyvBxF7DJpi5cyiEZBFZXoZwJn9MFFQuYuYEs9R_ekAobiFE6PizndbWyvIejjHzRqHjqy8-a2Ulsxp3ZB2FiZ_Y5kq54DL7J6f5g08vFtjBttr1fG4ulCAtvBathfk3bDinC9v6jAZFkooWuZFKskDFHj5vobUVJj0AFctRQenNvZoOnow5yNbDAhRAqoNR-ywASEV629RRHPTVyGxG8XniMsUyJcAQtasQQfjzeE_zVrQ8zOR1XcEVDR6lxEqAA_7F1KbegQzSvsWZfxlOVIiRi7BQW_upk5zJTraDTzmCFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ابراهیم‌شکوری دستیار حسین‌عبدی بعد حذف از آسیا، از ژاپن برای خودش آیفون ۱۸ آورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107308" target="_blank">📅 16:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275c393efd.mp4?token=P7TSUD6Osa_i_kwe2Zb1e1RsjDBZ_tPS4L1tFGiI3WdaWdzogk9DrcDoy55aZQze8pfFqeZIxPFoxDfvzHTw37TTyP-avayhb8vpbSOWWn7MLW3II3hqet4K8fDnLCpgPY24u605-HIn04Ce8mGW0iZSVZ7QNFApSTiDynGS0dx8M___m4U_FwyzzM2dhUKj7kdFKnCJyuo65adT9PXuZxWNscktCKRSSwsieVJ807Zzn1n-4xa3z9hVxkTfGCL5lg3Q0dVEHZng9a0OsUdCX7PflkG6ttRq3_HVFP2GS_elegErF2T-X93dXSd1OszIZ-BBg-Ya5bye_N5gXtBSVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275c393efd.mp4?token=P7TSUD6Osa_i_kwe2Zb1e1RsjDBZ_tPS4L1tFGiI3WdaWdzogk9DrcDoy55aZQze8pfFqeZIxPFoxDfvzHTw37TTyP-avayhb8vpbSOWWn7MLW3II3hqet4K8fDnLCpgPY24u605-HIn04Ce8mGW0iZSVZ7QNFApSTiDynGS0dx8M___m4U_FwyzzM2dhUKj7kdFKnCJyuo65adT9PXuZxWNscktCKRSSwsieVJ807Zzn1n-4xa3z9hVxkTfGCL5lg3Q0dVEHZng9a0OsUdCX7PflkG6ttRq3_HVFP2GS_elegErF2T-X93dXSd1OszIZ-BBg-Ya5bye_N5gXtBSVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❌
آنجلوتی بازهم به رافینیا استراحت نداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107307" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK9CEEEHuraNgX2N3zyTEnBhZg0Grh8prpg6A160_oGp7swY6ocQjXEZ0uUeCv-AiGvrgRUDdP4s6oWAQMGR1WtShZEmswh4kXSPVZkDtgq2uCfDpdGxUV6dscEU-fk-vp-CEhSX9eLgKRsSJl7ORzfzSfGulK-3MwQrJRkeuXFP3e7VQcX2yK2AenJxAgAC_x1X6C_UJ5sMCUmWKltbQk4cUAoZmcNtqPYPphzLV63lq3M82w9ZUIrCNxlDj9revXysU0ZOO1RSwOj3tmHOSXH4TFUCvlsX5NuWbl44pIPtTCuKt1VQGU9VlI8VTalwmM1-m4B9zEFEqbI1om8RtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
🇮🇪
چند بازیکن تیم‌ملی ایرلند از بازی مقابل اسرائیل انصراف دادن و گفتن که مقابل این کشور بازی نمیکنن. در صورتی که این اعتصاب گسترده‌تر بشه و ایرلند وارد زمین نشه، اسرائیل برنده بازی معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107306" target="_blank">📅 16:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=nVYjrJwh-JVke7eeBSDGpQen_AVaiVFvOkcgkTptgBsMQdvt_UPw8uv5IeSn-otxSnu9Yk4xIQpgRGt8L9MEeEcHGX7DKnj3SdbuFCuab4ZLbQmUPC4rH2CNMndlI1vJZGFcR6AVtCAOqpbyVcJOjCwFOz_ZJ4osdFNY51OpB_ZerI30kWOzz74VBQ6sKuP-cMX6x8QvIGDy4YA2lgkva4qW8zJNTNrEcnuaf8glghMnjlKnFlqgk6UmMXKwcVRe8soyokcjPVw8mgd5FoJvjtcJuKpDIaN3etgWxLCVCoguC2a0r6KXohW_BKXm0aIaJBDEkW1fOgR9FTsAOuXiJGCYQZ-jE1TeOkq4K-bKS8RV-i2qSaRff3TQuXZ6FE0lI14MO9SB5M7okTXqsLjmfOVUd3uso7Qaf5uow7wsjytMNZyEdi8xg2AlHIruisfSHkuX-NumImuGr2AUh8s-nmBuuAGKDMrKyBLcxvcOiKYzvI6Fqx1FmPcRFl8--RiEeY0RtcsyC-a12ogvVVubIj8KHggiO8lr7QtX3az4QAmvT4-4V2vVOKsbG0AlH-XbamJuWoqJXaotkt9ekz1ojpXNUk9pJqU4ZxZjVuyusyMNi6JTxFFblQL8nWSiSaCocvzHqfoEj0miDi6dLPzU_39A7NNK1cB6SFMD3MBM8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=nVYjrJwh-JVke7eeBSDGpQen_AVaiVFvOkcgkTptgBsMQdvt_UPw8uv5IeSn-otxSnu9Yk4xIQpgRGt8L9MEeEcHGX7DKnj3SdbuFCuab4ZLbQmUPC4rH2CNMndlI1vJZGFcR6AVtCAOqpbyVcJOjCwFOz_ZJ4osdFNY51OpB_ZerI30kWOzz74VBQ6sKuP-cMX6x8QvIGDy4YA2lgkva4qW8zJNTNrEcnuaf8glghMnjlKnFlqgk6UmMXKwcVRe8soyokcjPVw8mgd5FoJvjtcJuKpDIaN3etgWxLCVCoguC2a0r6KXohW_BKXm0aIaJBDEkW1fOgR9FTsAOuXiJGCYQZ-jE1TeOkq4K-bKS8RV-i2qSaRff3TQuXZ6FE0lI14MO9SB5M7okTXqsLjmfOVUd3uso7Qaf5uow7wsjytMNZyEdi8xg2AlHIruisfSHkuX-NumImuGr2AUh8s-nmBuuAGKDMrKyBLcxvcOiKYzvI6Fqx1FmPcRFl8--RiEeY0RtcsyC-a12ogvVVubIj8KHggiO8lr7QtX3az4QAmvT4-4V2vVOKsbG0AlH-XbamJuWoqJXaotkt9ekz1ojpXNUk9pJqU4ZxZjVuyusyMNi6JTxFFblQL8nWSiSaCocvzHqfoEj0miDi6dLPzU_39A7NNK1cB6SFMD3MBM8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107305" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=gskElv-1WtQzq7itsurCtEGDvTjh9WUoojMqxyCEPDgwJaH1Z2PgBOXwDmIz66sCTiQQ-hlF4zMyWRD1kYBL49ET_IIj_c21XXEH_imiaUmdztIB_F1GTu9rfrzkHE2ntKHRKvazPHQPmq_sJrwAKH9y2LiG5I_I-CKcl3pJQBRwZ12xYoCrUiWqZvdYzHRb6Fzp5YyTSmTonO3aKoRungS-4AH5lhs9tkd3ps65Ma7kMSoA5UPzc9R2UF_RnzfapH1BQpTGjK481DAByIX-iDnRkRE9FZht6aTsdwaI2vVO0pVhNrSuStXifGJQSU1-D2wDTGqruzc0uAsQB1Nz-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=gskElv-1WtQzq7itsurCtEGDvTjh9WUoojMqxyCEPDgwJaH1Z2PgBOXwDmIz66sCTiQQ-hlF4zMyWRD1kYBL49ET_IIj_c21XXEH_imiaUmdztIB_F1GTu9rfrzkHE2ntKHRKvazPHQPmq_sJrwAKH9y2LiG5I_I-CKcl3pJQBRwZ12xYoCrUiWqZvdYzHRb6Fzp5YyTSmTonO3aKoRungS-4AH5lhs9tkd3ps65Ma7kMSoA5UPzc9R2UF_RnzfapH1BQpTGjK481DAByIX-iDnRkRE9FZht6aTsdwaI2vVO0pVhNrSuStXifGJQSU1-D2wDTGqruzc0uAsQB1Nz-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
حسن پاجانی، قهرمان مسابقات ورزش‌های الکترونیک (بازی efootball) بازی‌های آسیایی ۲۰۲۶ ناگویا: دلیل قهرمان شدنم اینه که یه سال و نیمه ایران نیستم و اینترنت بهتری دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107304" target="_blank">📅 15:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=Pmra6-CfstpqxvG1DQFkFEoZyIv8tKeKDUzoV_F34PSr4FXw5DZY2uYsddXeh7QnaLaikfIYstB8ucwVbGRpzWY4vBxhyS1UkXyVJI0CHLkOwqlaWu1colsW6LaEIRB_z99nLalL_KpWE6PsXevyOSJcgcTDmMLkxkGz5_CNXeWCVBwr1j-pao2b4fipw6PmrF4MngfjDwgRyW1b8EvA30qW5lrRnbSHhYDJuGQB92BFYdG0ILTTG-vvZW98hB75xWQbMRtwPsYdGLFifMr4yok3LIIvSgAPkBZX2kYSX79UPQH0z1XPbkEkpxW3JNSRRYMg6Zwp6Kk28tIUZFRglA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=Pmra6-CfstpqxvG1DQFkFEoZyIv8tKeKDUzoV_F34PSr4FXw5DZY2uYsddXeh7QnaLaikfIYstB8ucwVbGRpzWY4vBxhyS1UkXyVJI0CHLkOwqlaWu1colsW6LaEIRB_z99nLalL_KpWE6PsXevyOSJcgcTDmMLkxkGz5_CNXeWCVBwr1j-pao2b4fipw6PmrF4MngfjDwgRyW1b8EvA30qW5lrRnbSHhYDJuGQB92BFYdG0ILTTG-vvZW98hB75xWQbMRtwPsYdGLFifMr4yok3LIIvSgAPkBZX2kYSX79UPQH0z1XPbkEkpxW3JNSRRYMg6Zwp6Kk28tIUZFRglA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
هانی رامبد: امسال سال‌بسیار سختی بود اما برای آینده تمام تلاشم را برای گرفتن ویزا ورزشکاران ایرانی برای حضور در مسترالمپیا انجام می‌دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107303" target="_blank">📅 14:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWDF70e0dLr6pccw7Otq3fA5haopuUWlh65vPhbLNaqwvj9geJ-pZcCgA_ncMrgT4mlwo3dOE7bnRoaMZHzFOfjMFl7klwLIGRWyj47CABaPazL7roe7Rys2wUOjVEVeDS0h3LlRgcSN50FbSZWrPFJ08flNPDetXk-d8mkD-yNe3CIbOfW1wtVc-T7WM16zlklxMhdEOmwUsrwnCAAQSdFJROs_rZGVMla3YcBqilpy7u4dzoCM6ri8YYotu7Q1Vm9jq91OlkrZ1c4HoWmOc07UCm1ggGOwwRPfAVJNq34vzaItpfVErBT7QIhXnFeMYp_O9iH3PFqZyOAAxP7YoAAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWDF70e0dLr6pccw7Otq3fA5haopuUWlh65vPhbLNaqwvj9geJ-pZcCgA_ncMrgT4mlwo3dOE7bnRoaMZHzFOfjMFl7klwLIGRWyj47CABaPazL7roe7Rys2wUOjVEVeDS0h3LlRgcSN50FbSZWrPFJ08flNPDetXk-d8mkD-yNe3CIbOfW1wtVc-T7WM16zlklxMhdEOmwUsrwnCAAQSdFJROs_rZGVMla3YcBqilpy7u4dzoCM6ri8YYotu7Q1Vm9jq91OlkrZ1c4HoWmOc07UCm1ggGOwwRPfAVJNq34vzaItpfVErBT7QIhXnFeMYp_O9iH3PFqZyOAAxP7YoAAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
هری کین یا لامین یامال؟ تفاوت فوتبال انگلیس و اسپانیا؟ وضعیت جود بلینگام؟ مقایسه توخل و فلیک؟⁣
✔️
جواب همه سوالات با آنتونی گوردون در مصاحبه پیش از بازی انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107302" target="_blank">📅 14:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e44add616.mp4?token=gibOLSKfBglfRBPcPs4QqLNfgxY9iMPgg6oDUGq1hhNJgPc_yavv5371NAQwyY2cZu06rQFlUAJaE46341BdyR96yOXNLWkPQIFI2_MNHigoba_dkaF0cLf2SJBaSS0t1QeuBkI_RDTSksudxmTLV1w7UNt955T1009sXLxR4aZiYiPS5cPYxuH4ytMp1VG8vifgyJSh2bJHdbs897ywfgIN1AlXc6WW7Qedw2zm_Ibomo5qh4w9Smyl-deQcrsvwPTCqItbX3rz9Ltm6MdQhWpiHPpsAEGpeizg3smp9-gyPcOepnGOed0ZBjar7yZ3DeWePxQUh5KDwBn-0T31JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e44add616.mp4?token=gibOLSKfBglfRBPcPs4QqLNfgxY9iMPgg6oDUGq1hhNJgPc_yavv5371NAQwyY2cZu06rQFlUAJaE46341BdyR96yOXNLWkPQIFI2_MNHigoba_dkaF0cLf2SJBaSS0t1QeuBkI_RDTSksudxmTLV1w7UNt955T1009sXLxR4aZiYiPS5cPYxuH4ytMp1VG8vifgyJSh2bJHdbs897ywfgIN1AlXc6WW7Qedw2zm_Ibomo5qh4w9Smyl-deQcrsvwPTCqItbX3rz9Ltm6MdQhWpiHPpsAEGpeizg3smp9-gyPcOepnGOed0ZBjar7yZ3DeWePxQUh5KDwBn-0T31JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بیرانوند سر صحنه پنالتی بازی با ازبکستان به چه چیزی داشت فکر میکرد؟
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107301" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=kcPeswaOXgp6xUh9foAt9I7JOEt9Vmp8IotahWcQSrPt5pFAtk7W8gxldon2Ig2ni7aXaaqgDLAWcC1zijmbLQK-j8YsbOqIGYx_0amCAjkoVZrsGEalfUbTTOM4HimfVOVLz29oEQ1rltq_d1-ioZ8YJlocFIrUo1F6YG6CbmWphQ3mVzpvetzD3hdLoJewFAkflCPGP-ALL6CcNjfcYSeVqQl3MRWN_vf938E_GQ24tjJVcBS0D_Z0iCQHe5xHKVsA-nbMUcefR75sNr3wEae6QjjoAuWhogkUHXgvBbSiit1ghWY1NU5kF2OY-rdUnUnXX0Hswaiywma1BTJujA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=kcPeswaOXgp6xUh9foAt9I7JOEt9Vmp8IotahWcQSrPt5pFAtk7W8gxldon2Ig2ni7aXaaqgDLAWcC1zijmbLQK-j8YsbOqIGYx_0amCAjkoVZrsGEalfUbTTOM4HimfVOVLz29oEQ1rltq_d1-ioZ8YJlocFIrUo1F6YG6CbmWphQ3mVzpvetzD3hdLoJewFAkflCPGP-ALL6CcNjfcYSeVqQl3MRWN_vf938E_GQ24tjJVcBS0D_Z0iCQHe5xHKVsA-nbMUcefR75sNr3wEae6QjjoAuWhogkUHXgvBbSiit1ghWY1NU5kF2OY-rdUnUnXX0Hswaiywma1BTJujA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کری خوانی های عجیب هندی‌ها برای ایران؛ لحظات پایانی فینال کبدی مسابقات ناگویا و قهرمانی هند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107300" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0woe22zJH8J78Fh-mt01wktPL9201vXDU_69hHXHMEP_JYuesMEszkWnb2qfCtuEaTNkdW7IlMsqXATeaMZZxUpyo7pVXrC5at0l9wkNyffJfJNZtQKQeGhwLNqmvVR_3EE7jxRTCeZaIdXOCilwsl-6y830eIpANGtjYqPTiIdAm26VGEHw2A92a0Ahy9-IM84y7JQO1BZi3EDCs6-w5ciMbjKvEtQk6uiDpcNfMGyBu4wiyi7gjiciVM4Zp0IEQxIQ3iI04NDDOZM4-B-k0TV8r8f8Y-oMQGYTQY8JWv872NZnUcOmRvaDV9bpy-ne3Xvl90WcpC5HEnIwYQDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
تو حرم مشهد این آقا صد میلیون چک نذر کرد و انداخته تو ضریح واسه شفای زنش؛ حالا بعد یه مدت اومده رفته بالای ضریح میگه زنم مرده تا پولم رو پس ندید پایین نمیام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107299" target="_blank">📅 13:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=UuhBzoqR_B9BNqGav-cv42VStsbNmPcyD-Ih4PAPqShIsGVWYsW5dnb044cVJ1moyGIGO0x-4pevW3o9DEepFU80v2yxb47b3dHR4rVExAe97-hQb8M19JZA7creVwUZ91LaNNhfLyFH5AUpi8F4TYVaOcwLr6vAcROkcohNc8wpRHwqAdskN1VybjQfgoRB6CfwbT8nfsitCVvl3VYn-y8fO0Sie_qyNLL3pT0WNB5EX-SmSyrLCcV23oINRcc05DA42dxdVBVS00-H0dSki4y-cJszkMyZe_c9sedtbUr0l_l3XNBtBwNXRyYR3NHft6ZiRJRy3vEDEpT9UmtxNxYmBkHhtCAEa3Wit0LPbZ4_uUme80xahiMUyiYs7ww5R7QxyggIXMXDdEWWXRLWU57_r3V7afqDia6KhKM72SpoyMq3XaZNU-GqIY6ZnhrvKS_TV801Q7vPsKLefZRJokl4wOUB8xKaXJzyarMKiP3ay8F-SqAZzeRbp1yuF5HvHWjN2rvWk66m4N4YM5V0oGCgUen6D_t0eDI26ADpjdud2LGzqCk6XX0w7bTugsIFoej7oQlPcLHvxzgQgNeWFn7LL5riyjdOnoq6AcIid0ZzEwpzwmX66G9EIC1namPvSDPC3M-zsrlS05gF5GIoAtJ5p-xRIQMK6Ed3PWhMBF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=UuhBzoqR_B9BNqGav-cv42VStsbNmPcyD-Ih4PAPqShIsGVWYsW5dnb044cVJ1moyGIGO0x-4pevW3o9DEepFU80v2yxb47b3dHR4rVExAe97-hQb8M19JZA7creVwUZ91LaNNhfLyFH5AUpi8F4TYVaOcwLr6vAcROkcohNc8wpRHwqAdskN1VybjQfgoRB6CfwbT8nfsitCVvl3VYn-y8fO0Sie_qyNLL3pT0WNB5EX-SmSyrLCcV23oINRcc05DA42dxdVBVS00-H0dSki4y-cJszkMyZe_c9sedtbUr0l_l3XNBtBwNXRyYR3NHft6ZiRJRy3vEDEpT9UmtxNxYmBkHhtCAEa3Wit0LPbZ4_uUme80xahiMUyiYs7ww5R7QxyggIXMXDdEWWXRLWU57_r3V7afqDia6KhKM72SpoyMq3XaZNU-GqIY6ZnhrvKS_TV801Q7vPsKLefZRJokl4wOUB8xKaXJzyarMKiP3ay8F-SqAZzeRbp1yuF5HvHWjN2rvWk66m4N4YM5V0oGCgUen6D_t0eDI26ADpjdud2LGzqCk6XX0w7bTugsIFoej7oQlPcLHvxzgQgNeWFn7LL5riyjdOnoq6AcIid0ZzEwpzwmX66G9EIC1namPvSDPC3M-zsrlS05gF5GIoAtJ5p-xRIQMK6Ed3PWhMBF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیز دربی مادرید: چرا رئال به گل نرسید؟
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107298" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=A3l5yp16JnCU6TDGOKBs0R4nd_hI-iaFSDXs6mm2jGcEA_QsjHTOnYV7Df-Drf_xyvceOSWy9y4pBkS1iqNOucX5ZNBPrjxpeUiDeIfqW3MB0LgvjIDv8ZAsEg7DwoMMcnXFcS0-_71KlKO_ZGexngtiNSGw-1AyaoZcOyaFz0JOUXR8VIGbY-Zd4GPWFQpfQ5dtAzThai7LhMLIohvonp_Rpg-ft2Zyy70jvjZy13cehiMXHstF_cdnWlzEwykQOpLR3LjD6zcxszP86k7SFoGmtj_yT8sttA9NDWXzATUnAj1f9T1k7oCcDOA6QI3mIbTxeUBXuL76UdW2oPMKOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=A3l5yp16JnCU6TDGOKBs0R4nd_hI-iaFSDXs6mm2jGcEA_QsjHTOnYV7Df-Drf_xyvceOSWy9y4pBkS1iqNOucX5ZNBPrjxpeUiDeIfqW3MB0LgvjIDv8ZAsEg7DwoMMcnXFcS0-_71KlKO_ZGexngtiNSGw-1AyaoZcOyaFz0JOUXR8VIGbY-Zd4GPWFQpfQ5dtAzThai7LhMLIohvonp_Rpg-ft2Zyy70jvjZy13cehiMXHstF_cdnWlzEwykQOpLR3LjD6zcxszP86k7SFoGmtj_yT8sttA9NDWXzATUnAj1f9T1k7oCcDOA6QI3mIbTxeUBXuL76UdW2oPMKOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
دبیر: تراکتور برای من هیچ فرقی با استقلال و پرسپولیس ندارد
مراسم امضای تفاهم‌نامه همکاری باشگاه تراکتور و فدراسیون کشتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107297" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgzraEbxAm0ZzKO5viLq09yOr1BXx5eAz7rPk976DqxmYQiP_gH2bZcaP0dkMofjGfRdzPS6oo5xBbzuw6EFjn0-tkjRBk9SGt5IH8tL_Im_sH7MBZiXEDWRmZTsLkY_nQasmrXYAFs5o006IFeWSeViAxnrwII0dpUMreQ4OaJcg5TM0XrT3PlJLve2HSOfwlpKz4E7L9afrhN9JJl25QjMC0Rj2qBTRB94JLup9CsgxSC-wE8nl0D_wed5305TwxyzyKkq6Do9vZLbMIldd6tZwMuTAKYc4aeDxnBrfquKLWSJIUgYZlI6gZ3WQN1dRK7NJzmU57JJfxjVIe9Q3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
👀
همسر سابق سپهر حیدری درباره رامین رضاییان: ایشون بااختلاف چه از نظر فنی چه ازنظر اخلاقی‌بهترین‌بازیکن حال حاضر فوتبال ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107296" target="_blank">📅 13:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJBUz01LVO8Q9kuFB7U74LKgO21HhQC5oynMOUgojdUnypOy8cK8EiDj1aJfUuxWs9FFPujRZOrnvOe0YTwt_vt6cU1B-t8oyuTgm2oSj4anSE3gMIRP91kktSImKb8BtVQELesLpNE1yxFKAzJl3j_Gj1QlhpK3B0qdHgC9R5xpEA-w50kboEqbqMD9CcbqUgO6L3isvd-fPcAHWYfEE3OQjXz-x0KFjneUxQfA_daINn8g3pUVIUITBuzjA13fo6FUAFTJ6_EdB_UTXvuU_Nb2JMIO8rD-mSBxcJU7ICTn38w_Ai2KdMDx3uudjdtMU474ERVB9CnQjqL_2svXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر قهرمانی‌های‌سیتی گرفته بشه نتیجش میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107295" target="_blank">📅 13:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107294" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107294" target="_blank">📅 13:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLZo_hgBxoD2_quLX9o2zRGMHRLOFUertLAxyHeIVpomnqcxNulgse4HgbavfzzcoDplCsbKnQn1-mIAKsEznRvmZvVw4obzHPM0vjuA3QBdeoA6kh0-fkHjliLdlmsCYzXv4KJY7hyRS4T8azoTYKA1qE96uKftkYphWcV2skkRzY9wmuGyOp8FSuIT--ruzSDt7m-x_mINm4DovJLLhaCXTiHBl8pJIYDYH2pHFNJ4fAAUAGTlTmwOjISiLd67_X5oUjk1rmMh1t9BO8TfHLlRCgqlcoZZ3GtLVeWiINorHOYLTE6JtiCbP9HGMyZKhConba5tmJunHEUCL0oZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107293" target="_blank">📅 13:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=olwWVNX50upcFlkBjGYV1fYRuG8N2l3cu87bRqBepE2khqdpFu1ky53nP2ZZya4RfZrYxlaLwptmnL7LHc8iZwgEs3HtBj5FX3FwetoPZbcU0lgDORTtuM4jX2qG_-NLRXvkyyD6E6aixrcUiuGBw-_a8lOz56IKZ8G8wN6LjMHBvGaBqucG46qz4JHpSQnEKsZbjTXDqzPY0F19B5WXxI3LHzef4Z3j7zcG9vZr5MJeCNKZw2J2R56VF20Dwuij9LEiMmX5Wkfe3h1B_d1P3tA_CdxmWFqxL0_SbQZDRKcN2ktMq0zpuQ2VwN8vcIUjtV7gdNN4s7amE0B21CljrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=olwWVNX50upcFlkBjGYV1fYRuG8N2l3cu87bRqBepE2khqdpFu1ky53nP2ZZya4RfZrYxlaLwptmnL7LHc8iZwgEs3HtBj5FX3FwetoPZbcU0lgDORTtuM4jX2qG_-NLRXvkyyD6E6aixrcUiuGBw-_a8lOz56IKZ8G8wN6LjMHBvGaBqucG46qz4JHpSQnEKsZbjTXDqzPY0F19B5WXxI3LHzef4Z3j7zcG9vZr5MJeCNKZw2J2R56VF20Dwuij9LEiMmX5Wkfe3h1B_d1P3tA_CdxmWFqxL0_SbQZDRKcN2ktMq0zpuQ2VwN8vcIUjtV7gdNN4s7amE0B21CljrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
👀
بهزاد داداش‌زاده بازهم یک ادعای جنجالی داشته و گفته که مجید جلالی جادوگر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107292" target="_blank">📅 12:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=RIsdBalpPWFkFRQinAzbA0LpfIcL57i4zb5VDEoacPpIlKqVaK_-pRQ4sJElC13iVRFPCV6Gd8mgHxYiU2xtUkUV160J3bYI7eczmWGmfC_uy1rO0Lrxrg2hxY0pczH_r213HtQXeQePB2Yt4H9pcfsPVp1yFevzsjvmcNnnEeycARCaLLIByCj5Y8N2h0C3nFlNSZ_vfi5NsKWi-X9dXuDIt9msURICOtDWRHPDZrR3I7hpB5n-vURwLR-fE6taBxLZJLiJznae4kC_ZRAJ_AUPwGKAJYnMhTm6NQ9DD6sPxlKMbKe7UO_p54YEhEX1tlh3XGcWTLVRlipFHgh6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=RIsdBalpPWFkFRQinAzbA0LpfIcL57i4zb5VDEoacPpIlKqVaK_-pRQ4sJElC13iVRFPCV6Gd8mgHxYiU2xtUkUV160J3bYI7eczmWGmfC_uy1rO0Lrxrg2hxY0pczH_r213HtQXeQePB2Yt4H9pcfsPVp1yFevzsjvmcNnnEeycARCaLLIByCj5Y8N2h0C3nFlNSZ_vfi5NsKWi-X9dXuDIt9msURICOtDWRHPDZrR3I7hpB5n-vURwLR-fE6taBxLZJLiJznae4kC_ZRAJ_AUPwGKAJYnMhTm6NQ9DD6sPxlKMbKe7UO_p54YEhEX1tlh3XGcWTLVRlipFHgh6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
گوشه‌ای از نمایش‌جذاب هلند زیر نظر ژاوی در اولین مسابقه رسمی مقابل آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107291" target="_blank">📅 12:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b671734a24.mp4?token=EGdjExZBX4mIThLdLpImX-iBCeHllc2ec9RULskratgNqwKRh3_mmLEiTpsxYEYEH5rnGed2znz3ody1FN-xXHvV-4Vm2ZR6r2wXwyAJD-m6_RdyxkknSBQNHCKFsDPm-cXhvYVO7a9QIYeYn0upWNh3YMH1mYfOCwmE3rl8pEHJ7IhWRkWgaTpkMBuiVJYbN-UKZ_vZXC9Kv5YSTjpidPthLpt0OStrgiQCqqE5ofm033HSJvvbHxddVsjd02IzHZ4wq_nWIrTx_ZSbNjLjgGvnIDLIjqAivNk79uSFbiDM1DKK8g_vVCSrjal8vbiN5O55Lz-vJQ1to3gvf4IV5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b671734a24.mp4?token=EGdjExZBX4mIThLdLpImX-iBCeHllc2ec9RULskratgNqwKRh3_mmLEiTpsxYEYEH5rnGed2znz3ody1FN-xXHvV-4Vm2ZR6r2wXwyAJD-m6_RdyxkknSBQNHCKFsDPm-cXhvYVO7a9QIYeYn0upWNh3YMH1mYfOCwmE3rl8pEHJ7IhWRkWgaTpkMBuiVJYbN-UKZ_vZXC9Kv5YSTjpidPthLpt0OStrgiQCqqE5ofm033HSJvvbHxddVsjd02IzHZ4wq_nWIrTx_ZSbNjLjgGvnIDLIjqAivNk79uSFbiDM1DKK8g_vVCSrjal8vbiN5O55Lz-vJQ1to3gvf4IV5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت ریدمان کریم‌آدیمی در بازی مقابل هلند که حسابی اعصاب کلوپ بهم ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107290" target="_blank">📅 11:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107289" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=kG4UcKxdPE_GT4WthJaDEjGSZ5NS4YI5QHF9Tlk0t0CztIZ5vYJHlV70nhlL7Mce7uiTY0KdWlClwcQcJFp3iNlBLYci9X08D6xeAN2Vsr1bxmAq9fe81ds7zatYD5Wdnm467I19BwmwCBiNORlHJEG6sxD4nVDF05fZzW0owzvW8sJ9H9Y5qCldhvVjUtcZdfMQNwleW988lEHLz6nJdW4oX_urHMHKznL_zWzgAYlfYKee9MbSGEFc8cCDhLDx6ZvAEDTSKt5yLMtgAcg9V656qqMhDTYD5erQJ-tWohSakNu739XbItRP3EcdCsFhrnoGcpJ0fxHTaaEvb2s5Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=kG4UcKxdPE_GT4WthJaDEjGSZ5NS4YI5QHF9Tlk0t0CztIZ5vYJHlV70nhlL7Mce7uiTY0KdWlClwcQcJFp3iNlBLYci9X08D6xeAN2Vsr1bxmAq9fe81ds7zatYD5Wdnm467I19BwmwCBiNORlHJEG6sxD4nVDF05fZzW0owzvW8sJ9H9Y5qCldhvVjUtcZdfMQNwleW988lEHLz6nJdW4oX_urHMHKznL_zWzgAYlfYKee9MbSGEFc8cCDhLDx6ZvAEDTSKt5yLMtgAcg9V656qqMhDTYD5erQJ-tWohSakNu739XbItRP3EcdCsFhrnoGcpJ0fxHTaaEvb2s5Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
کنایه حسین‌گودرزی بازیکن استقلال به ماجرای سربازی نرفتن علیرضا بیرانوند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107288" target="_blank">📅 11:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107287">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=WeONTyFB-KZ7Ouka9Dq40yMrm7rPv6nNpKHD59oXaRDYdh5jlt_coE-jzof0YURBL1YLW3I9m-7dNZRXQaFdrZWQayqIR_vzEkQTayvxlNYo35pZeZWQ7rve2gqEbMAQFNdldpBazbJ0GL_ErS_czMT1W3mvYO5WikF4cwJAcDIj6V6Yq3Q8Z8pHbxrXIfypVusbbgMa1g9I10KcV9lQuEGSTe6mc9D-mmLFV4__16t90dVGhvOUiY_LynmBPFNrUrBCRTmt0ZR6KE7gLegQ8breGvOIo2MUyY_tjvz0JiOwzDM8tBRdRUzz_4hc1cpahmY9lle9CBDF_nbBmlfPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=WeONTyFB-KZ7Ouka9Dq40yMrm7rPv6nNpKHD59oXaRDYdh5jlt_coE-jzof0YURBL1YLW3I9m-7dNZRXQaFdrZWQayqIR_vzEkQTayvxlNYo35pZeZWQ7rve2gqEbMAQFNdldpBazbJ0GL_ErS_czMT1W3mvYO5WikF4cwJAcDIj6V6Yq3Q8Z8pHbxrXIfypVusbbgMa1g9I10KcV9lQuEGSTe6mc9D-mmLFV4__16t90dVGhvOUiY_LynmBPFNrUrBCRTmt0ZR6KE7gLegQ8breGvOIo2MUyY_tjvz0JiOwzDM8tBRdRUzz_4hc1cpahmY9lle9CBDF_nbBmlfPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب کریستیانو از تاریخ تولد هم‌تیمییش در تیم ملی پرتغال
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107287" target="_blank">📅 11:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=OYziJtLtHdnNfJ8sFSKQo4KyVopnKB6dtaVhicZCi9cIdUcLebVFtS9jDf1NdMtEuM8ZNQ3aV7os5d5kxorl3PWUPQkdj4eapssZDcgY4OA3XB9JKUshXs2H81W_VV3wveEjAsg_b2Jfree_RIX592ZCPKOCUGOv91LGiw_oy6e0qfIK5yK_eM9Qa7AExQQCG6JG1kMTSgeqzE66oZxKyixReguYKYO2Vr_HZdSnkhUY3iyvS1wIDqziESsy_zKXMiApZ-roJqWwZA_8Pye38I0mXTx6A47FmnvHQjIpZeoEq6WKwxBTJHMbTpxRsTqbomOCi-QeCOresoh8WkDyuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=OYziJtLtHdnNfJ8sFSKQo4KyVopnKB6dtaVhicZCi9cIdUcLebVFtS9jDf1NdMtEuM8ZNQ3aV7os5d5kxorl3PWUPQkdj4eapssZDcgY4OA3XB9JKUshXs2H81W_VV3wveEjAsg_b2Jfree_RIX592ZCPKOCUGOv91LGiw_oy6e0qfIK5yK_eM9Qa7AExQQCG6JG1kMTSgeqzE66oZxKyixReguYKYO2Vr_HZdSnkhUY3iyvS1wIDqziESsy_zKXMiApZ-roJqWwZA_8Pye38I0mXTx6A47FmnvHQjIpZeoEq6WKwxBTJHMbTpxRsTqbomOCi-QeCOresoh8WkDyuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
محمدصلاح رفته تو کوه‌های ترابوزان رو یه سنگ نشسته و حالا شهردار اون منطقه اومده سنگ مورد نظر رو جاذبه گردشگری کرده‌ تا مردم از نشیمنگاه صلاح دیدن کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107286" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=RFnVpdsMHcz4qQr2zqlVMTrtQ8d8x_Zw7UtuY63PA32oGis6YVFqB9lY52YWoq5pJllYTWWZByuU9E_T1YxV2ZWBLvcb0UnHLrPxSYB1oUnt3FYp5ymZRpvFLhWV2jMZUFkauJM7555myV_uds96pBrSv9ZnQh_DIg8q2Gqj6Nd95Wv6Hj4bDKVtkUEfz-y-wM74l_0EYrPR9H_n0n-D-5-wd510MXjmOlXfCeakH4IeE6KwCXiCTIcuqV7kwUzsSdTxjbV8ldZcSZW1OA7IFJ594UJgRkXGCE_vR1iL2BjCP0Ukmn9dUd6qzN6q4MzWrpdh2FeUGO2DB667us8KsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=RFnVpdsMHcz4qQr2zqlVMTrtQ8d8x_Zw7UtuY63PA32oGis6YVFqB9lY52YWoq5pJllYTWWZByuU9E_T1YxV2ZWBLvcb0UnHLrPxSYB1oUnt3FYp5ymZRpvFLhWV2jMZUFkauJM7555myV_uds96pBrSv9ZnQh_DIg8q2Gqj6Nd95Wv6Hj4bDKVtkUEfz-y-wM74l_0EYrPR9H_n0n-D-5-wd510MXjmOlXfCeakH4IeE6KwCXiCTIcuqV7kwUzsSdTxjbV8ldZcSZW1OA7IFJ594UJgRkXGCE_vR1iL2BjCP0Ukmn9dUd6qzN6q4MzWrpdh2FeUGO2DB667us8KsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
کنایه گودرزی به ابوالفضل‌جلالی مدافع فعلی پرسپولیس: زمان مشخص میکنه کی استقلالیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107285" target="_blank">📅 10:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=NDkL9XIgqBOLs9MtWdyzDtaKtULjRI-e5L83fXxkC9VqsIIlbB4C8857ECS-0aa4A4haTnO9eERKd3XquIwhRyDJ5IdAJXPABu2UPgFag_tOyts5rt8Jaz6B2o0eEDgLqOabI7QFL1MRQcR-0qRoM0-qXMydm3JERoAgTaDjvrIXpLp5Om23N_cHpdH09wyeqRTgVhU49-ngYYhHbsiYCwXS5bquT1UUFLpXumkGP5LbQdHXjzt0OIRcL7-fAbSsta-n5fJFOUjn_7MMuYLxN78_fur_KXX8S8bVjnmj5Tko84d_VgHRx_yRMENi-s5VWGfCoRF9j0S0JuMYvIJo1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=NDkL9XIgqBOLs9MtWdyzDtaKtULjRI-e5L83fXxkC9VqsIIlbB4C8857ECS-0aa4A4haTnO9eERKd3XquIwhRyDJ5IdAJXPABu2UPgFag_tOyts5rt8Jaz6B2o0eEDgLqOabI7QFL1MRQcR-0qRoM0-qXMydm3JERoAgTaDjvrIXpLp5Om23N_cHpdH09wyeqRTgVhU49-ngYYhHbsiYCwXS5bquT1UUFLpXumkGP5LbQdHXjzt0OIRcL7-fAbSsta-n5fJFOUjn_7MMuYLxN78_fur_KXX8S8bVjnmj5Tko84d_VgHRx_yRMENi-s5VWGfCoRF9j0S0JuMYvIJo1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت روحی مورینیو، هم اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107284" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02c187832.mp4?token=i62g5bYnBbWUDEriKLRjzDKEmlvUmA5UH_7T43mmGOPjnaYgvGPMImQ6vM1McIRq2TiXOVa0ZRA3zz3yZAMfmwLKOwV2a-8wFjU1vemA2oiO0t3G4NKMUcJu2rIqW_spMx6T9gK4aqTXiH6g7nMFnZIIDLgVGjF2FebWO8j3VR7fTVqXAXct3Rx7QxBBACTU0u0s09KZK9rdz-apQJqNOFYhOz_xVzdtJEps3zfXKmEBn4nyAYcmrORlT38UICvtnOuOtZvg8uZSPXfXj9ldulQVOp6QB2Q08wk17GsId8wGxTsM287cTPZ5aX3Fe4ic9SYnDR4uhOYd8vxyEl5OYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02c187832.mp4?token=i62g5bYnBbWUDEriKLRjzDKEmlvUmA5UH_7T43mmGOPjnaYgvGPMImQ6vM1McIRq2TiXOVa0ZRA3zz3yZAMfmwLKOwV2a-8wFjU1vemA2oiO0t3G4NKMUcJu2rIqW_spMx6T9gK4aqTXiH6g7nMFnZIIDLgVGjF2FebWO8j3VR7fTVqXAXct3Rx7QxBBACTU0u0s09KZK9rdz-apQJqNOFYhOz_xVzdtJEps3zfXKmEBn4nyAYcmrORlT38UICvtnOuOtZvg8uZSPXfXj9ldulQVOp6QB2Q08wk17GsId8wGxTsM287cTPZ5aX3Fe4ic9SYnDR4uhOYd8vxyEl5OYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
کنایه توتونچی به ابوالفضل جلالی: یادش رفته بود، که گفته استقلالیه!
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107283" target="_blank">📅 09:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGf-xqvpSMbbhqNZWR1yRLi9s-cMed6nko_thHteXW0XcAqejsNQqzs_9lU0V24yihQ7VG37lwAKBUdI_Wa80HP4MK3YSvlNQaGK-Lpyhi2VAZCyyNY_ieti032LANrVO11uJleiwQ9VZU_GKrVOnhhDUbhjAXQxXJFnWMKuRw6yhcOqRwmaILwKww58vkRB-828Pnyw_SyGrjAcyjE2SDrSKWoskvN1XGZ1rlmjlLP4l53as20gr_YGg245uX-YZFJ_kRlvi_YOdGILrPZMyby5Dp0jYVSWwQeUbKtHH9wvhW6xegNFZjLSE57D67KNV9YPdiHH4xPl1JXsx5EJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🇪🇸
آخرین آپدیت از بیمارستان شلوغ رئال که کیلیان امباپه هم به این لیست اضافه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107282" target="_blank">📅 09:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEnJThVaxbOkDPDNl_8lPFXnxUjrrOhtOlotfZnZ4ao9AmHNN1gADi-Xliqjcz1D4ESM9JNf9aZPhdeuEVEw2IpRYo5jmo0fIazJR3k3-_VKkFtPFBtsXlRBH9ADje7SbrzeWWQbWLCZ5t3Ui4i9jKlAcknLGMF4oOWJNuQ6gh-UIU3Jlp7NgHrshJgu_UrVZS7Wx3bvI4vyQAKvLs-Q0XG5oBCGURMMAvHrNv-XN_AI1vHDBbiApnqJrjqyuzS6SLnTa4le-eGISrsD_xaAHjX82GAMiOYEjXSdCcLrWHPFWSRMaSr4zCJUXU_HgWdirryoT7UoL-xU9d3fvLe18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
تیم‌ملی کبدی بانوان ایران با شکست مقابل هند به نایب‌قهرمانی مسابقات ناگویا دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107281" target="_blank">📅 08:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107280">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=GaaUyaKqauMD4uPEqBkjIK3ssizD9r3zrHdipL8Kfumx0RSgPXhyWxnUUM7kiRAvHZ5RVgaAVUkD4iB1qqNP547vdix1a4BxzEeSrJci4Dj3Ruz9wdtGwQ7O_cg__Wi8cNqhzRp4swaSklCOM0yWoVIQPgjTzQt10WfIOPEj0mUl7UPEqNWyBdgAJ8V4WCSCuEgDUFoS8nR12ZCaAXMDlxNF-8Inv-IBY7P9c5g776OVCXPKLwXI3Rw-NMs0mDrYcO5aFIoCXytiLLv2kuti5W9GnFK8R60-m8LmvHqoRYI0CqskWvgUEF6EPP7rOPOVjTn9JvZW-2PEkoBV2VPonQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=GaaUyaKqauMD4uPEqBkjIK3ssizD9r3zrHdipL8Kfumx0RSgPXhyWxnUUM7kiRAvHZ5RVgaAVUkD4iB1qqNP547vdix1a4BxzEeSrJci4Dj3Ruz9wdtGwQ7O_cg__Wi8cNqhzRp4swaSklCOM0yWoVIQPgjTzQt10WfIOPEj0mUl7UPEqNWyBdgAJ8V4WCSCuEgDUFoS8nR12ZCaAXMDlxNF-8Inv-IBY7P9c5g776OVCXPKLwXI3Rw-NMs0mDrYcO5aFIoCXytiLLv2kuti5W9GnFK8R60-m8LmvHqoRYI0CqskWvgUEF6EPP7rOPOVjTn9JvZW-2PEkoBV2VPonQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وضعیت دیشب امباپه که شرایط نهایی این بازیکن تا ساعاتی‌دیگه مشخص میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107280" target="_blank">📅 08:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107279">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107279" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107279" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107278">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvIP3aT1E0QarzO9XZZqIYvHywEoo17N59Ot7Z69xa7tjpukpdmGvz94RJiGEjOHurI1ckqi4pG6oZbev6SaM9ms7xbwPpt3B298hRwfFYWYCURJMcXcVjd02FWCCK2ixrlk7zfSNPRbGeMfF5lqG1Ig1V1AF4d2PZuP33KlfTuGMla49YNQTpswh3iZyThJFbhUvlnOpA2DF3NHlx5552VFw57zzdbwYtbLFzLVZdh00H9lkagIJ0Q4Z_-aIRb9tdBhHdrEVqU9MlfGm2fe8Ptfxzacp8SfXYpKEv1yJdpKShAyqtw6r4h7BIbWG_I3l10hNNYRfDZtsQ1WIU9Xdw.jpg" alt="photo" loading="lazy"/></div>
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
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107278" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfo2YaF_d-5bAeHuUHZxHb5xDHDkE3it8DNxNWdVCEJ8fJEiIyRTmoe7ypFMWK8gGHap6SyMpnCdUCaxwphVudXqRKmgfcZve0P7fUleLLzE4p1ZnMaKoWPWXCmPfAc7K-eKE9whxyRAN51CMC9yxTHQt-EbBteHDSEmGczgHeu_UNOhWqKSMvQh4ImgGgfJh2OPtb_N-PFyIlVwGOpjPfOoDnT8sCj2VhaUAUtCnj-YQ9LhAJQCRpDhensTUx1dJM06qiPpeVUx9il06wsMJQX4BacqxcYS3VRHDf2ZkuoGqZ578UXVAshzA3BY6SkKJBM9MPI5KYgZ5xNG-gL_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
©️
با اعلام سرمربی تیم‌ملی آرژانتین، کوتی رومرو کاپیتان اول تیم‌ملی آرژانتین پس از خداحافظی لیونل‌مسی افسانه‌ای شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107277" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107276">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVxJsQrxUKbHcuiRn2qqfm3hfUkdvkO8o9BUYdMAuVO8-3bEAejRppBcuWVSORodjMq5trd9QFvfHrx1ybAf3VlchbdV5poNVFjmgVI_baTbGYskg3_Aq8IZmuwBdsL9ISx5nJSOgDU2JUFAvI2PeqevvZDAboGuVnNLU2PMh6KCSYzNS2sdhMX3z3nBqlxUkQhzA4qRPHKKp7IKdI8W0U-i_c-5IHrMx_Hr0swCnQcGtngAZvs198tZmgO0EtO37l8dFdIjsNyP8Wyxr_Cbk6yJFbGnacV_xdrn2TU3RAOSXHZjZU3BGq6yiAhEBIQ5EY6ar8LTcwuDh3-fcz99Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107276" target="_blank">📅 01:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107275">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiMoSN131o0Op5fpXqipvr78R0AMG6_r4PiNmlq_yWeheFUpTkU2NFsjVguUpH53ATbwwZ96GS9yf0oMAw4s1yICc9udBFq_HTyzS-sZbNkmRGMSsLu_A-lcshnnKLOkhbOyF6ib3RHkk9IQYGbPAuA1xSpELZy0Vk8izIRA8euB_SDst047oRf1oF4awALZHH6L033yYiljpQkTBh8EHyl5a_LJAop8kms5OBqbJMyICcMxuSdpKyg1MQQUEHl3asx-8STPel8tT71zKOCo-CFkWGwfcUV5HiXsTkn-oPh5ZukvGsQgxvB7AErIZSl369lDYcG1PCvduxmRw9_u_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107275" target="_blank">📅 01:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107274">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcF-SXIRt72KGiXP7Vw9RB3x7A4HAuywURx54B7fQlZaAjI6GBioCuw_PIo_DS8WFfkm3WbtdDjhv64ihods4Ty6-HPN9Rb9D_yFGTUGcL6B5SaTVdszU51TlBgGuCbNFnJMdjEMEKaHGaSpwezRo6zE7N_mvG8yUM9ERxzwC6ceyhu0DE132pTMVG_Fk3x1ZgRrbAPgFYx-ZccTDdJSGsY_yJUsRBvpJJOWCiOESGdsuMCF8Rppmv2QdsB8ezL5HarJmcDzJ3J0PUQ71NZCzjQF-rs3nCzf3GS8YVWj31107Kp6EuXKGlOHQ_92B2xy-5ws1hagJeEeTkBXJbFeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
• امباپه به 107 بازی ملی رسید و رکوردی را که قبلاً باتریک ویرا ثبت کرده بود، شکست.
• او هشتمین بازیکنی در تاریخ تیم ملی فرانسه است که بیشترین تعداد بازی را در این تیم داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107274" target="_blank">📅 00:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107273">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdlAXmAfLMlEYgRFgZ0FeA4h41b90kw7Qb3kQaUXGRhV-eq2yu7FF7Cj9tgY9mjcajMFp4t4qbNCSmuryUBrnu2kC1nI17hF1_IIgEBqbW6PcVxOGsUWzv_vphTnw9db4HUXZ88EZp3MJTU1sJVu1oAPO18TLf286f2oSOrRFoQcG3NarAzysaaCH-UWdeKQFTfYPALrWfzrv-RhxLMorCMg9xyEgVcr3oWRukjXMjDUbKl7IysE_7EGWjXB81cnLuul2aWp3PfILkDCPri9yUtabaq--m6kQadU_T4FplnzKJ-1JEYHwsnxtDU0z6cexoi0J-ZkBThqMmoZ2yIVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گل‌اول فرانسه به ترکیه توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107273" target="_blank">📅 00:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107272">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvEy9h4rlQVCvvpACSFGaZhBSz-3PjI8trjzHS1qIg4lq2lkPMEuoOZPuD_aDSJkRZj3IBParDnBjdHu2e7IV9evdY8Gdg32YTb0Yvb1RsD2FMpygqASmnbXHDCNSpdjCkoY3hAS9NoVwky9lO817qown7NCuO_qYmoJg8K4WU9LGeUccVINjtF5IYuaaozRD0VoBPvB4m3SFVvB1dXawHajmmf7ErAA6albWYT-x00MjXcq9BMiZJNPUooL4VPBDWq1j7KfGy6dHkpdR1QN4jWiFKRKnmUcRHGOZVzISLUArFiD8bDWqJTbjoEqlH86Qw03iFbXyTmhw9T7LWhdgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
گل‌دوم بلژیک به ایتالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107272" target="_blank">📅 00:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107271">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6892ba52e.mp4?token=WLR4DjfYlpbe5j4FM6Z77F70xw8QQvQ07tkRGk-KJxQs52KqcOsX_7tOfAupgw036F7YE7qIP5E6oY-m2EOnODPltW2g8b_-nYh8AmIdkqjcyHk7XMe5bMc5C_V7ggOCK8abD3BpBz2iwysuEVUPfS4tKXQE_k-2mFcKouPyyrLU_LV3XH4Qg7-9pfmiZIl5eBTBerMEgcPdGyGBM7lY4rIOHeSUHKk6USeSasVDnWMZ4u9dCv3MJMOtRtMId33_-U9xz6p4pcmD27acMjbBmwERxhfureNcef3jZhEWQ4cZammTwlpKb9snh9bejHyMfw3jx2ZUyrBtzbb7OEMMvwFTLUcwqPH9X3Szm3pL8tLo2VvdDFZKRislu6GY5KXKVeI2Ua84c6beGR54WlAR6N_R-MWfuvCOlLxgnHJ7xe7l-eBt91Pxk3T_wRmNBYOK8Mmcb6NFhRZKbXrCK9N-j2ytzw1uEmkdnD_DDQEwRwc5IvLpAnvDZtYOsJut4chgVojyOCrdSej8qMJTZmELQFl2EAprpPaxt9NumuehJkIaPi_e0V-ZdtKQH2kSEzASWW4D7iFSzWDZe-jLUrJ_aieNxe0aIZRv7f0yxkGSvLRZHTmwMwlEZ4grO9jk50hfeML4miI3p_iZF_mnX-nleP6dN0qsiSFmppjG6uerj3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6892ba52e.mp4?token=WLR4DjfYlpbe5j4FM6Z77F70xw8QQvQ07tkRGk-KJxQs52KqcOsX_7tOfAupgw036F7YE7qIP5E6oY-m2EOnODPltW2g8b_-nYh8AmIdkqjcyHk7XMe5bMc5C_V7ggOCK8abD3BpBz2iwysuEVUPfS4tKXQE_k-2mFcKouPyyrLU_LV3XH4Qg7-9pfmiZIl5eBTBerMEgcPdGyGBM7lY4rIOHeSUHKk6USeSasVDnWMZ4u9dCv3MJMOtRtMId33_-U9xz6p4pcmD27acMjbBmwERxhfureNcef3jZhEWQ4cZammTwlpKb9snh9bejHyMfw3jx2ZUyrBtzbb7OEMMvwFTLUcwqPH9X3Szm3pL8tLo2VvdDFZKRislu6GY5KXKVeI2Ua84c6beGR54WlAR6N_R-MWfuvCOlLxgnHJ7xe7l-eBt91Pxk3T_wRmNBYOK8Mmcb6NFhRZKbXrCK9N-j2ytzw1uEmkdnD_DDQEwRwc5IvLpAnvDZtYOsJut4chgVojyOCrdSej8qMJTZmELQFl2EAprpPaxt9NumuehJkIaPi_e0V-ZdtKQH2kSEzASWW4D7iFSzWDZe-jLUrJ_aieNxe0aIZRv7f0yxkGSvLRZHTmwMwlEZ4grO9jk50hfeML4miI3p_iZF_mnX-nleP6dN0qsiSFmppjG6uerj3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گل‌دوم بلژیک به ایتالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107271" target="_blank">📅 00:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107270">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcef0287f9.mp4?token=IOtG0BAdQbjpwkRE9XckNpR5-f-or2GL-T88hApyEU-iGj24w_G08TD5fgvvE8yBaXzGvGC1UnzW5125Pt-4cvpQf9yQGIXI0swO0B9ZaxgRpy6uFAq-I4ld9Lu1oOuGI0qe3H9YhT67onLNkeXBTHpIGAH25mI59GjmZmFYh00r06Be0I8Dp3UAy6MBJeyU0riDSi0fkjgDlSRyO4qDuKBGZcFKmjNK_TOW2t8yF2N_7qx5nLPiz3prQdyZ7XOkqP0y-f2qHIU60s5Mo8cAH0LZ_79xjnatlIeiuEaQMuvyMqp9V4tWTYuzWLSniIqE9FkR43HrNIMq_TD7flM7yU0pXQMkfGd74UvX27u35nRMBtn5_i3AfuRCYW56vDY802g_x8k6Bc4fwQGa6l8yrPj-KHfrQgIO46ZZELHiWEqYxpM1mAGBM4_M-G1bengDxQlsubsT5G3e5FyzqwlDslm3buhq6RQklftkaGTIf-QqHmrkki2bfVrhKwUgXTLLubX-K7x0_9MYfjI5L2uz7UzCRvtA5tth5g4NhjmwpvHsofqFigcxWgFG-xI_N1koVT7AfuiDKh8BxdhKBlfoVXTz8f2lkCSXxplJFOmUHu_-Lck9wkVQ5O9HOq307au77pqLjLeOboB6KSUjNamqNIT_g2F6NCXoN1qYf87rYD8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcef0287f9.mp4?token=IOtG0BAdQbjpwkRE9XckNpR5-f-or2GL-T88hApyEU-iGj24w_G08TD5fgvvE8yBaXzGvGC1UnzW5125Pt-4cvpQf9yQGIXI0swO0B9ZaxgRpy6uFAq-I4ld9Lu1oOuGI0qe3H9YhT67onLNkeXBTHpIGAH25mI59GjmZmFYh00r06Be0I8Dp3UAy6MBJeyU0riDSi0fkjgDlSRyO4qDuKBGZcFKmjNK_TOW2t8yF2N_7qx5nLPiz3prQdyZ7XOkqP0y-f2qHIU60s5Mo8cAH0LZ_79xjnatlIeiuEaQMuvyMqp9V4tWTYuzWLSniIqE9FkR43HrNIMq_TD7flM7yU0pXQMkfGd74UvX27u35nRMBtn5_i3AfuRCYW56vDY802g_x8k6Bc4fwQGa6l8yrPj-KHfrQgIO46ZZELHiWEqYxpM1mAGBM4_M-G1bengDxQlsubsT5G3e5FyzqwlDslm3buhq6RQklftkaGTIf-QqHmrkki2bfVrhKwUgXTLLubX-K7x0_9MYfjI5L2uz7UzCRvtA5tth5g4NhjmwpvHsofqFigcxWgFG-xI_N1koVT7AfuiDKh8BxdhKBlfoVXTz8f2lkCSXxplJFOmUHu_-Lck9wkVQ5O9HOq307au77pqLjLeOboB6KSUjNamqNIT_g2F6NCXoN1qYf87rYD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول فرانسه به ترکیه توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107270" target="_blank">📅 23:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107269">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107269" target="_blank">📅 22:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107268">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a64700b02a.mp4?token=C-bmgRgxNOthWufdGFT4IHQ9kIQwl_9TKGdaZSVPMCvEG_fqPMndUpEYsY4tcw5SjsKbHMxpUk1JuO_9V_ctZlYWVKalD_tx1u_orvZQX6mii5RCeZwzIp5nEmMDp8miShNV5SmzXBBEX21XKxvxRoTjpneob4Q76bwfQ5qM3tr9fjFC5E8F56BMiy9uCWZyNVDXuHHiOsGpZKQYXRupHILGHp3fI888GQJJW7UcNa6Af34LUz6-qZH4QxPteyQYiq7rcJpVXBWTiH3h0LNQPx7xjU3TdMS7BbgdpDxywhwYd0XYz-cceEcE24IU6VIQ2ellNBVOqoO4GWK4RLB2BTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a64700b02a.mp4?token=C-bmgRgxNOthWufdGFT4IHQ9kIQwl_9TKGdaZSVPMCvEG_fqPMndUpEYsY4tcw5SjsKbHMxpUk1JuO_9V_ctZlYWVKalD_tx1u_orvZQX6mii5RCeZwzIp5nEmMDp8miShNV5SmzXBBEX21XKxvxRoTjpneob4Q76bwfQ5qM3tr9fjFC5E8F56BMiy9uCWZyNVDXuHHiOsGpZKQYXRupHILGHp3fI888GQJJW7UcNa6Af34LUz6-qZH4QxPteyQYiq7rcJpVXBWTiH3h0LNQPx7xjU3TdMS7BbgdpDxywhwYd0XYz-cceEcE24IU6VIQ2ellNBVOqoO4GWK4RLB2BTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بلژیک به ایتالیا توسط میکا گودتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107268" target="_blank">📅 22:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107267">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ایتالیا یکی از بلژیک خورد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107267" target="_blank">📅 22:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107266">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plUH84qGF77Cv-y6pfBegadKyp0rYGuZoTgeCqup8S6d0eAVPUlGdsxJwKny2omjDlyZgxyXS0k9DOjQ5unIRckz04m32DFIexbScKrEi-vvq1rWUkBWUOgNFTesKne3pv1HT2mIk0EWEP0qoKFDHxLjLER6nttNeJncOpsD_dc_ofTjeoIZoGpHOZoGir7kBuTHc8FVwFjQoAmxd7LsJwCewif-J6AgGeXKHBgGAO5V9-pIdysgtXksGIAf6P2bHGNnuW-fixD12Z2OrF7kVVJKxXjzU2R_u9yc-ZYz0MwGr8LJM5DbcjoV0jYBKzUid9AAZkdSettHFDJHuplKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107266" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107265">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeUyzaSLjysDkHM4KNHpJBkO3tqeadtw_eUoTjWs2bn4VEyUAbuwMXPTE-_pCTJHq7aokSyMthXxY7oI-vSFwe_VD9ToyI4kH6vSnR1RJeksS02-m0_5ZCzkrgqvNmi17n9ZjRot2C_7FE_ygAnQOQxMFJr2gAOwObub8i2V462COo3q8DvdVcSF5MWU50kvnNckUZgvbWXaPtXT5FiluA3-v7F8nECe7pQ1IgR9vTjOj5sb5yCWu1PlL0k2pNw83tEDC6k5m7lhbjmKHH3bEXtwHbl2gE6NwWfd93vZjZ5Y9t19qWN6XhV09HYzCA2C-KtrTCxC4qEn0JnHWb2oZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب ایتالیا و بلژیک | لیگ ملت‌های اروپا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107265" target="_blank">📅 21:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107264">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjZ2aPi6Jjm2Bh0gn0Z9mBersOLN4GzMQYBE0zgSX3N4-HmV3h8iNkPj9XpUPCWMcKUNOVTvjmhzE34OgOlP_8UYTKqUynVxMpdKjHM0QF1nuCxFmNqbIOME-oVJmPu7ySuJXAMtzUnA12a_gIL5pei4Jb--Ls9naoGBCC7hngKmotFLT7uoY4YHrlD3mhJRT5lYmxqzqX0btoPMjDz8TRYw8XHcNBaP1K_VJsNutcDdg608ebXOCNZQHYR-C8fVCAHWfwDD1BNgwmT2nQ2sxomY2S1qP97X1eoiBSb23aj1-NYZO_88859-vfYD4R__OOZER4GgDKJ2pL01cuXcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب فرانسه و ترکیه؛ لیگ ملت‌های اروپا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107264" target="_blank">📅 21:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107263">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=mLwbZ3nLUY698j9VzYMMJTil-pL13FFOXif95JCSx9XKpAft7btl1ZOuCBA-q4jjOgcfNOrNspPc75qj9C2U8WGXxCWe0xqxYEKL95aAhCDszznAh2U9qkhGrs88e3IRX4geen62DedJkfNLuW4p7W42rP5ftnI8M3tVLUKKQFPZSym_OHJ0Tvv9zSUc_bYiGhlWG5nxriMHWJ86YB0dSVB63TdVII4LXUVnNpqZtTuJ1Zc2yPJbo5mOCKg2ljhqLNikJdbqaPXXBxH99fsy64HnOnpuTTCG2dE0Qc9-r8a2vRDLUHvRWFh4dOvZi9UrzZuHu0MyY3Cw8HtE01-d5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=mLwbZ3nLUY698j9VzYMMJTil-pL13FFOXif95JCSx9XKpAft7btl1ZOuCBA-q4jjOgcfNOrNspPc75qj9C2U8WGXxCWe0xqxYEKL95aAhCDszznAh2U9qkhGrs88e3IRX4geen62DedJkfNLuW4p7W42rP5ftnI8M3tVLUKKQFPZSym_OHJ0Tvv9zSUc_bYiGhlWG5nxriMHWJ86YB0dSVB63TdVII4LXUVnNpqZtTuJ1Zc2yPJbo5mOCKg2ljhqLNikJdbqaPXXBxH99fsy64HnOnpuTTCG2dE0Qc9-r8a2vRDLUHvRWFh4dOvZi9UrzZuHu0MyY3Cw8HtE01-d5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقلید صدای جالب یاسر آسانی توسط حسین گودرزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107263" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107262">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔺
✅
🇬🇷
روایت شنیدنی نوید استادرحیمی از تیم‌رویایی یونان که در سال ۲۰۰۴ قهرمان یورو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107262" target="_blank">📅 20:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107261">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=G4ftMtzovNLuoRqwuWInXzAQJaGxbumeTJEuvZqTtW4fTWIVikUIrdyof-kOG_4SA6SA-51eKX1AC1QKY93sIxAdeQlCoNlcJNMb9xT3_aUZx_oT5zbWBRhQGE526Ef-CXGqJW7bTRJu2ZCPcJuOycjZBXHSQuZBR6hNOuif5YXqO9gxnX_pPaMVKa33mjCnjKsnqWXm1nWh-LllN2OFoBKZF944d1BhT7IdWJlwOblexDDhvLppVscuCFONWYRNXo1AcEpDqno78aA-66X33naAn84g0GdYrHaMPw_QTaNBXb_jwg2D-JEQY2SCBscHQk5FSl5YtRLaVH9WTVu1mUk3SVh36o6C1GI2EplWsWUFT1chM-kYlow9y78qo9lbUNaZBOL2LFJqqC6TM8QvDNygWDOcwwzjpQnCimhREfDlNsRSRn_PIsEADUdIctyptPYjdIPRpBH6UvRnBaKiq5qKPZYsZe1d8-xjBA-iXRxhuf_s57bSAMe5TnRb0m8ETghXgW90XxqWXzuIY1XYepu4USJlhWzntAb90hxWmmaKKf8L9uUTyJU5oBfi0qoXwplBTQjL-8xU86Ls4vwsGBIHWL8uY9vxg3eBPshcgxezltkjTTnQag6llDb62Fj2jJd_gdHnEWQKATGyjduYaFMZlQxuA-YyvirgYCWpu4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=G4ftMtzovNLuoRqwuWInXzAQJaGxbumeTJEuvZqTtW4fTWIVikUIrdyof-kOG_4SA6SA-51eKX1AC1QKY93sIxAdeQlCoNlcJNMb9xT3_aUZx_oT5zbWBRhQGE526Ef-CXGqJW7bTRJu2ZCPcJuOycjZBXHSQuZBR6hNOuif5YXqO9gxnX_pPaMVKa33mjCnjKsnqWXm1nWh-LllN2OFoBKZF944d1BhT7IdWJlwOblexDDhvLppVscuCFONWYRNXo1AcEpDqno78aA-66X33naAn84g0GdYrHaMPw_QTaNBXb_jwg2D-JEQY2SCBscHQk5FSl5YtRLaVH9WTVu1mUk3SVh36o6C1GI2EplWsWUFT1chM-kYlow9y78qo9lbUNaZBOL2LFJqqC6TM8QvDNygWDOcwwzjpQnCimhREfDlNsRSRn_PIsEADUdIctyptPYjdIPRpBH6UvRnBaKiq5qKPZYsZe1d8-xjBA-iXRxhuf_s57bSAMe5TnRb0m8ETghXgW90XxqWXzuIY1XYepu4USJlhWzntAb90hxWmmaKKf8L9uUTyJU5oBfi0qoXwplBTQjL-8xU86Ls4vwsGBIHWL8uY9vxg3eBPshcgxezltkjTTnQag6llDb62Fj2jJd_gdHnEWQKATGyjduYaFMZlQxuA-YyvirgYCWpu4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی بازیکن سابق استقلال:
🔺
به ولله برای خودم اشک نمی‌ریزم. مگه میشه ایرانی باشی و با این همه ثروت کشور از گرسنگی بمیری؟ وطن مثل ناموسه، برایش جان هم میدهم اما الان شرایط اصلا خوب نیست
🔺
در مراسم عروسی‌ام چهار هزار تا مهمان داشتم و پول یک خانه را خرج کردم اما فدای سر همسرم چون به عشق اون عروسی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107261" target="_blank">📅 20:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107260">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=JpdpycB0V_REkqcx9hvhZfsruZYje8Q5l3xGxK1IkTbJidOK0XNUyJYde_uJFdqFYZWiFGZ_q3wYGUG7eICd31r0jqMq7tJlLLRPqmXTEuveytbl2yVyve73CHnlAdO2kflrjRd5Mc7Jz2-eeLzgSI5FvIU3gS3JkUAFQqh53yAi0IUpl-KLDqj8A_g-eUoEP-Hp-i-9upSNHjPiBODEOmFwMqGkf5lCIGMxUpXr0C_TlXTk2lGzx5BRIk88VRz4Jm8aKXkYCcFS2JSA-cvM1vgT9mWghL1uAqyNQ1RAYm-oBrPbpEG1aU8_UuVa-bDDSUMeyPeCYvldcN8URtBFwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=JpdpycB0V_REkqcx9hvhZfsruZYje8Q5l3xGxK1IkTbJidOK0XNUyJYde_uJFdqFYZWiFGZ_q3wYGUG7eICd31r0jqMq7tJlLLRPqmXTEuveytbl2yVyve73CHnlAdO2kflrjRd5Mc7Jz2-eeLzgSI5FvIU3gS3JkUAFQqh53yAi0IUpl-KLDqj8A_g-eUoEP-Hp-i-9upSNHjPiBODEOmFwMqGkf5lCIGMxUpXr0C_TlXTk2lGzx5BRIk88VRz4Jm8aKXkYCcFS2JSA-cvM1vgT9mWghL1uAqyNQ1RAYm-oBrPbpEG1aU8_UuVa-bDDSUMeyPeCYvldcN8URtBFwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
👀
مورگان راجرز: رونالدو بازیکن مورد علاقه منه اما من در نیمه‌نهایی جام‌مهانی در برابر مسی ۳۹ ساله بازی کردم و باورنکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107260" target="_blank">📅 19:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107259">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=HyZNRpvFS2NThfxjgAp4_mBPJaVOBIAntiFVKKHPjFgJmJ8rzTPId88F3vCnUex0O2EPyGsfAf80Xrd8OyOsKutPIMy-0_iTBUwPC0lvDbi0Qgs_wAQhE06AwuQQC10Y7dfnveGyoFyFxnxq7xOIn4R1r22goaS6fdQ-MUih82-vjcv27aYPQTui8iuFDBiEXPnjJtHoGTDkmfgArxRnJP69RLaRpKA-VIR0dSlfS-K5EQsauhdfYIraunl7yZSnsg8L-S_ickSPXej4qtl-t_geTpiWtuKkC6XGgeZiJVe6jA_QBNRrcY0WbYXXnQb9xxq8u9E2PWy3l43F5R4yqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=HyZNRpvFS2NThfxjgAp4_mBPJaVOBIAntiFVKKHPjFgJmJ8rzTPId88F3vCnUex0O2EPyGsfAf80Xrd8OyOsKutPIMy-0_iTBUwPC0lvDbi0Qgs_wAQhE06AwuQQC10Y7dfnveGyoFyFxnxq7xOIn4R1r22goaS6fdQ-MUih82-vjcv27aYPQTui8iuFDBiEXPnjJtHoGTDkmfgArxRnJP69RLaRpKA-VIR0dSlfS-K5EQsauhdfYIraunl7yZSnsg8L-S_ickSPXej4qtl-t_geTpiWtuKkC6XGgeZiJVe6jA_QBNRrcY0WbYXXnQb9xxq8u9E2PWy3l43F5R4yqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه‌کردن ترامپ از پرواز جنگنده‌های آمریکا در مراسم استقبال از رییس‌جمهور چین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107259" target="_blank">📅 19:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107258">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=sXbldr_0QlrAdA5TeWn4ZRK-47Xzwnx7RHdwtSoqnqNsIwzK1lN59yrCXKKB450g7PKBXusWeML0ZBGfbYkUkI9HfheblRVY3U4kVtfzna2K5CoP1Usd7vRhVFp7vLZIA7LE7-ivGlU8yAR9BX0TBWd46_1TxA3BHr4CZ-bLwbMhRe8e_RbjGm4f0i_7Lyogvb_tGsrHuO8oxNIG4GngZbsPRrWHIPdHgfNAlvcc4r2KltScrxDJVwq7wGzEtgHqzNXfrHHuXR38NlzMAIKbezaQ4P9OffeoOpeUSDnv14ggtGQtbQu0gL0mzt_c2uOQ6qmAPfMGirM_j6cvNRwpwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=sXbldr_0QlrAdA5TeWn4ZRK-47Xzwnx7RHdwtSoqnqNsIwzK1lN59yrCXKKB450g7PKBXusWeML0ZBGfbYkUkI9HfheblRVY3U4kVtfzna2K5CoP1Usd7vRhVFp7vLZIA7LE7-ivGlU8yAR9BX0TBWd46_1TxA3BHr4CZ-bLwbMhRe8e_RbjGm4f0i_7Lyogvb_tGsrHuO8oxNIG4GngZbsPRrWHIPdHgfNAlvcc4r2KltScrxDJVwq7wGzEtgHqzNXfrHHuXR38NlzMAIKbezaQ4P9OffeoOpeUSDnv14ggtGQtbQu0gL0mzt_c2uOQ6qmAPfMGirM_j6cvNRwpwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇳🇱
در بازی هلند-آلمان چه گذشت؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107258" target="_blank">📅 18:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107257">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-Ouprj5r_lcUE0I5DGJSFLGndUuGfLfx3mQrzvLQsROYCbyFIJerg38osHiT1iRYWdcFD5FDVJo8AN3iBNdTteZAJ6mm7-7T26-ftKJps1x5W57DSuADPzMq1_OPiPtZuPzbvKdluyMkiNeN88LmiVOAYW_2aVr-zrS-vJem4p6hZzTvzwwtl2lqVwi9csl4NLh3IAkouJvNJAIaF66F8jWJPCO6uTixVMaUxKjTytQVkrJGCz3-lQFIrLX1EXttLq3NTrMgc0GjIVONQ_zcpix-e4znWUmpoZeQwrxxBJihT9Nf3JaC1AHudZmQ8WLTLRFiCAelk8QBqFDfM8aFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
پرسپولیس در دیداری تدارکاتی مقابل چادرملو با یک گل شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107257" target="_blank">📅 18:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107256">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=FU5v--K2AYMe4_btPPuEPe832Jz4yF-la9sWczivt9EAA-Cw-l3BCycXUfIR-5c2_MlBAL2U49Q4VNIgtTNhnPEuSWTlwUMGIw_Zbe8wDC8wv90j1ZIRY0ZJWQyzlJ4ShuNOZOMWatGvV5M4jkjSbNfaWtuVladI0ReAChlct0_BN4awObL02FEZjH7orYXiDi5zWuNarQx5TH9_v91htAQsF0drMGEQ5cQf8U6yNl3qwF-EDZfbT69ig4AyVzgIhs1kUGp1OzX4PQoEj1C5qtz_82bg7h1KrqozjQuVE7tKhLbZLdA7nZKKRs-LgKw_7y5yh440T0KAvOkyF4t9PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=FU5v--K2AYMe4_btPPuEPe832Jz4yF-la9sWczivt9EAA-Cw-l3BCycXUfIR-5c2_MlBAL2U49Q4VNIgtTNhnPEuSWTlwUMGIw_Zbe8wDC8wv90j1ZIRY0ZJWQyzlJ4ShuNOZOMWatGvV5M4jkjSbNfaWtuVladI0ReAChlct0_BN4awObL02FEZjH7orYXiDi5zWuNarQx5TH9_v91htAQsF0drMGEQ5cQf8U6yNl3qwF-EDZfbT69ig4AyVzgIhs1kUGp1OzX4PQoEj1C5qtz_82bg7h1KrqozjQuVE7tKhLbZLdA7nZKKRs-LgKw_7y5yh440T0KAvOkyF4t9PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
واکنش رسول‌مجیدی به شکست عجیب روز گذشته تیم‌ملی ایران در مقابل ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107256" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107255">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107255" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107255" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107254">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlWG0morw_B_JvkMZrdCo4363Feyn50FdagQ60_UwRa8FO5XXEbqU5RLpNK1ibp7Y1dvWLeHCxVkNmGbZxmpT0ccD2VYSCxE_6l4CQWQs3NPlyAVbs8_5oIaKhQEYHtdZyHCkrMJKLZDfiaIZnqac6P97HfToU3ofGaaeCtyP_CGPM5Vjzkur5bWcZqZjFgu8oZhU0oJwBMRcdXdN9NkLxUX9_PNQcNtXHGCen6_FeK5ULnQ2lk2YnfXxbTsGxpePKncIfnJDMWNzgid06vjgbqwrOqSGTYCFkaDA7cORKJEW8riTuycqj-0SCiEviDcsG6kbbu7AkuG8RkXPKgrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107254" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107253">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
🇮🇷
اشتباه عجیب مریم‌یکتایی گلر بانوان استقلال در بازی مقابل خاتون‌بم که‌دروازه‌اش باز شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107253" target="_blank">📅 17:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107252">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H02LdSlf2d6JqymSKeA-ZO2Hs6MRyPCnRf1vL37qORIzzGJk5B0nqonu2o-K-fDsMUWLw-nXz8zG69J-lz_2MFe7sRHIoLyEhUqUMqkgSDcnWpatqHTUpNKIml6zTqscifYFt39Kxrfb5ksROw5QD8757n2LD4YmKL2sa2ZGvAESd8ExlcRh90JccI28ZqRPqcMXTfJdkJokYpVdGPh7LJfWNc9Yt5ZsnasUwS8cQSWbM8MSjvtCc6r96AFyETLZgrnWi0peOZflsepvo3iW4EUXmv1VYIDE6C4fEusK3xjTx6pRqiYRUubj6_7WcfY5c-7MuldMhQ1uVEO6h5DROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107252" target="_blank">📅 17:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107251">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRia9D5go9WhBB40RcaLdBpadCnhJ1zplP-i-IQZpmI0YwfW4arbPcQlCjAnacOoK3GCkTY2vZbxtfk4JNEdGKQso82EWMS-SSDascsrt3EmeWETSfN1p3EFPRA0yU6yyJk3qe2I31oemjGTbOqw7mZ3HGZMEU1ysHKqwuj5YQt4wme7WIzGyWMHrJkO2hw0Pvg43Ri_3zg8u3Ne8LamvaNPvVjSwtQytI6ciDSJnk1rZ7tbSIENjVnPtOG2sNJyR-FJFULw3ciZaQWXHpQpDVKnBp13JnK4eI2wW-QqJZA-kwJuHlplPiQKFpip4szy_T-CHL5GB0QLYNLWXhs8fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
منچسترسیتی در پرونده ۱۱۵ اتهام مالی مقصر شناخته شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از اورنشتین، منچستر سیتی تقریباً در تمامی موارد اتهامی مربوط به نقض مقررات مالی لیگ برتر انگلیس مقصر شناخته شد. انتظار می‌رود این باشگاه به حکم صادره از سوی کمیسیون مستقل اعتراض کند. هنوز…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107251" target="_blank">📅 17:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107250">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKn2ax9Zrwc5S4lqEpKYxyc4KE-aX-G03hGx8XkqWiYv4DqAmWxIeuBrYefGS3dmbnCkwq_d05_DbUUoY15qE3ktbD3MxTCKk-XCXO2JWlP3ModL6GG36r2XAHq6Z9hhX-Gs8zsdl4TRuSky1GybyuZF7XURr7Rt0mUY5Jk8QxEuqiDVIvY-qR8vEfUpmS8eLJsUVp67FwjMalvckAd7os6KWc4gpTODDmKRSOEVkqoAwJmMB_0zck5BHIwd3ob-lEHrkYKffXbnSZpSEBdBvHfsD_hxdRs3w6TsnSToYmsLySIZdMD5EIIswmLunnrJls1Y7jhZF-oSgjmnRvd_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
منچسترسیتی در پرونده ۱۱۵ اتهام مالی مقصر شناخته شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از اورنشتین، منچستر سیتی تقریباً در تمامی موارد اتهامی مربوط به نقض مقررات مالی لیگ برتر انگلیس مقصر شناخته شد. انتظار می‌رود این باشگاه به حکم صادره از سوی کمیسیون مستقل اعتراض کند. هنوز در مورد تحریم‌ها تصمیمی گرفته نشده و روند رسیدگی ادامه دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107250" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107249">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638e170672.mp4?token=nIfCdz-VnLqtNqpU7JzaJ5O8pIDYA8YD_cp74acNQTdgm1_sl0D0QXbYFHWCE18j5yucK3GUJxnoYuhwIEhTsSEoctWGvrNh-NukqDI5Cvc-Hyhmi2jghEzkQvF1F-z6hntr7aoGNc4X_yacDrs5iHBKMuo3gFry73EMJkkE8LEq77GBGLw4pkdXLlQJ2UZ1uSqnSi07UwnXsRISaQi4NHTR1tvgM-Dyh_eBRsWisYnn0TPxnuptg4fhVcXpXFePqY9w-tuididMx1RhNondAcaZxLa4iQQWt2zzKBotltpiB8DbnpdCwYoLrPfItcUJJlVKCDcrNNFwFQ-mxfa04Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638e170672.mp4?token=nIfCdz-VnLqtNqpU7JzaJ5O8pIDYA8YD_cp74acNQTdgm1_sl0D0QXbYFHWCE18j5yucK3GUJxnoYuhwIEhTsSEoctWGvrNh-NukqDI5Cvc-Hyhmi2jghEzkQvF1F-z6hntr7aoGNc4X_yacDrs5iHBKMuo3gFry73EMJkkE8LEq77GBGLw4pkdXLlQJ2UZ1uSqnSi07UwnXsRISaQi4NHTR1tvgM-Dyh_eBRsWisYnn0TPxnuptg4fhVcXpXFePqY9w-tuididMx1RhNondAcaZxLa4iQQWt2zzKBotltpiB8DbnpdCwYoLrPfItcUJJlVKCDcrNNFwFQ-mxfa04Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
هادی چوپان: من حکومتی نیستم هنوز فکر میکنم دارم خواب می‌بینم؛ وطن‌پرستی دلیل حکومتی بودن نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107249" target="_blank">📅 16:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107248">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e4e43dca.mp4?token=mb-2UY0f9abhWXow8eai8UyAxPghhbvZM8Vbliqa2QCe5KbJFtCMQi5Swj3CWUSQo1gFkovqD2Jx-E9Zm3m7WLgAnwZ-gDuw_YT8G6Fm1pPY-ofy-gVbZP3BwTzkxWCDmMcuDTVWpgn64Vj5YmW8XvThl5lYx9fMOFy_MiZ-DqHsFWlADuzATfYyeh3p__U7AT1_NSrpJ-o6kkQYx422HT2aQrMrhZkfPXDrFqM3GXFLQs6KZL8hi1j9KPn0dxZB4qKmmrTPA1on5F96D7lRHdCh75zVbEDcI8Sa80ulHKNRkso5GofGOyjO25pSmLmyKV_3NQT1TePxHh5vaDDxmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e4e43dca.mp4?token=mb-2UY0f9abhWXow8eai8UyAxPghhbvZM8Vbliqa2QCe5KbJFtCMQi5Swj3CWUSQo1gFkovqD2Jx-E9Zm3m7WLgAnwZ-gDuw_YT8G6Fm1pPY-ofy-gVbZP3BwTzkxWCDmMcuDTVWpgn64Vj5YmW8XvThl5lYx9fMOFy_MiZ-DqHsFWlADuzATfYyeh3p__U7AT1_NSrpJ-o6kkQYx422HT2aQrMrhZkfPXDrFqM3GXFLQs6KZL8hi1j9KPn0dxZB4qKmmrTPA1on5F96D7lRHdCh75zVbEDcI8Sa80ulHKNRkso5GofGOyjO25pSmLmyKV_3NQT1TePxHh5vaDDxmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇪🇸
عادل فردوسی‌پور: کاش زلاتان ابراهیموویچ یه روزی برای تیم دیگو سیمئونه فوتبال بازی می‌کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107248" target="_blank">📅 16:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107247">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c917893c10.mp4?token=mjYgHA7Xncx1MAbZNeLfULPSArURaZvVpFbIzRibCUxfOpA1dYgSMxxjZHWuGXNfcNCfLIpGbiPyZ_mb7vMdCLFRSy77bWcxD3wqkE2aVi5dq0-7HK3173UOY_OUMJp4EXGE1zM20Ahp8Gl5JC2bASbBUG7vYG_jsUW7FbhDRRxhaP1U4qr9EtoHbclralA-rcVrmwnxt7PGkwnF_qMTCUniLrTp5fgBTObBaF5v9H4NqWsyJUFlurvb74UNw5fwttJvAdqRsKxl9UoWhLnCxjR2rvvM5t_Jo4UOCFGQCwkVxRzEY7Pk8jck9VzaDTT6-0QG4cgad6gQdUYzedhvGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c917893c10.mp4?token=mjYgHA7Xncx1MAbZNeLfULPSArURaZvVpFbIzRibCUxfOpA1dYgSMxxjZHWuGXNfcNCfLIpGbiPyZ_mb7vMdCLFRSy77bWcxD3wqkE2aVi5dq0-7HK3173UOY_OUMJp4EXGE1zM20Ahp8Gl5JC2bASbBUG7vYG_jsUW7FbhDRRxhaP1U4qr9EtoHbclralA-rcVrmwnxt7PGkwnF_qMTCUniLrTp5fgBTObBaF5v9H4NqWsyJUFlurvb74UNw5fwttJvAdqRsKxl9UoWhLnCxjR2rvvM5t_Jo4UOCFGQCwkVxRzEY7Pk8jck9VzaDTT6-0QG4cgad6gQdUYzedhvGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇪🇸
صحبت‌های شنیدنی رودری درباره تفاوت‌های اساسی فلیک‌ و پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107247" target="_blank">📅 16:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107246">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6854f7f8.mp4?token=qOoteL4RCbC-0zD6a2xQEDRG8zLj1r6rNiDXUm0orFLUyBb99Ar1mGZU-AlRsYtz8lGN0eBMGwSMExHRihbMU7zd8KKJIOS0joE6CnWdtBzmaphyqIwWkzSo5yhnZGG8kOBGbC8rTD5untBMakET1aFtJZNl8cJlIHubSJkxYnkEUQUe0sLxeHDArli9rCOFGifEXOF1Yz2_EqDEw71agOVNEJVDk5Ow2HDtIJ1IbCb92K0MMmUX22RGMe2hEgh6gWh42SDtXIFo0psUhATTwOTSPJkE7iGXULp6UkE7-ffB-fd9BTb1DGkqvlRJZAxMFXEwEODk0tTpKdYINxEFgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6854f7f8.mp4?token=qOoteL4RCbC-0zD6a2xQEDRG8zLj1r6rNiDXUm0orFLUyBb99Ar1mGZU-AlRsYtz8lGN0eBMGwSMExHRihbMU7zd8KKJIOS0joE6CnWdtBzmaphyqIwWkzSo5yhnZGG8kOBGbC8rTD5untBMakET1aFtJZNl8cJlIHubSJkxYnkEUQUe0sLxeHDArli9rCOFGifEXOF1Yz2_EqDEw71agOVNEJVDk5Ow2HDtIJ1IbCb92K0MMmUX22RGMe2hEgh6gWh42SDtXIFo0psUhATTwOTSPJkE7iGXULp6UkE7-ffB-fd9BTb1DGkqvlRJZAxMFXEwEODk0tTpKdYINxEFgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آندره‌اونانا گلر ترابوزان‌اسپور از روزهای خودش در فیفادی؛ معلوم نیست چه غلطی‌میکنه
🥸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107246" target="_blank">📅 15:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107245">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=TpITcxb3d5Jn8Qr6cARymlUIJqMpapo43uiL_Pi6-w31EnRtspYF8HMXm7iHYu0cgfeI0jN4dl-d5tvcZJqjbVLpqKJCcSpYF4ZhqcUXmG51zcmUgDe8NFV6sy3-Hh48VBrL85tsUj90G0YlKRj6PFePztP_pzXVUNvJ-qG4ioEp5sxzKD87RdeKnflZfUxz488Ypl0hiuuFOx6UkiLUltZCpZTtZ7ANSW4qZQXC7X011ihhyLHI-jfhaqNKgHdEvONWkCyYGS_CPhpuMa1069OIDgBLklJdmp3Zvc7f2hXxD9IRtRApBShN5Qkhupw58LVhCYtyCB7LzAcUX-2xQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=TpITcxb3d5Jn8Qr6cARymlUIJqMpapo43uiL_Pi6-w31EnRtspYF8HMXm7iHYu0cgfeI0jN4dl-d5tvcZJqjbVLpqKJCcSpYF4ZhqcUXmG51zcmUgDe8NFV6sy3-Hh48VBrL85tsUj90G0YlKRj6PFePztP_pzXVUNvJ-qG4ioEp5sxzKD87RdeKnflZfUxz488Ypl0hiuuFOx6UkiLUltZCpZTtZ7ANSW4qZQXC7X011ihhyLHI-jfhaqNKgHdEvONWkCyYGS_CPhpuMa1069OIDgBLklJdmp3Zvc7f2hXxD9IRtRApBShN5Qkhupw58LVhCYtyCB7LzAcUX-2xQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گل‌خوشکل سون‌هیونگ‌مین مقابل اکوادور که تنها با یک‌گل دیگر به بهترین گلزن تاریخ کره تبدیل میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107245" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107244">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=EZL03DYikQYeuV5MV8eg8A2hs-87jt15wLCdtS9fa5X2xfebIkL234g20YdwpQtXpbuiI8AgaCq5H5L9IUlMgXsjH9VvzbAVPrT1duFLEPwOyp_EJxm-h0J9fuzRzh9h51DkPhOyMbP52XvYKsJSi3qGS4Wa5DejrxY0XLKIQ1LXjZyGjdagSC4NJ-ZKrKJvQiFqLNWfJ27_C4PVZkmTVLqkdeUM-zRmHt52qsnZLc4UsoLnl8Ee-wc0jhva6wgg6rCoLPmKYToD920mN8wUS8fNQ0e1t-cNnFu7d5UJHMPafysXDuxowGFw6IR-eLosKry5SXsiKBUtG9wKE2z1x26r6cDFXhdlY7bXA6JN1zDKpQsU1DVGzIwmuFTBynVm5pCz3hknukQldw2dAez-3jMPGm5Rk4wk8Bd0PEcEXHM-Pkxfa3YPQ-weqHFrDD3DEJhmKngIbMUzLrsWTHNOwoiEhmMxdd53xXmewHWmTnCpKderM5WbClfb_tRPr1ps50XiH2-hvofi38THqXCvNUCUsUuBhuEGOsHrH82pWyM1zVgMeexj6RZRKDSFiZYCqsF9z6kSmeaWZ-zH4dH37yPKwX349TfoWteuMOt3xqRo2-ZZw2yu-K0xkTO2pl6bC4XkEIC_9h74dZ01DbJ72psBgRn1QUtxwz2N9tUx_3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=EZL03DYikQYeuV5MV8eg8A2hs-87jt15wLCdtS9fa5X2xfebIkL234g20YdwpQtXpbuiI8AgaCq5H5L9IUlMgXsjH9VvzbAVPrT1duFLEPwOyp_EJxm-h0J9fuzRzh9h51DkPhOyMbP52XvYKsJSi3qGS4Wa5DejrxY0XLKIQ1LXjZyGjdagSC4NJ-ZKrKJvQiFqLNWfJ27_C4PVZkmTVLqkdeUM-zRmHt52qsnZLc4UsoLnl8Ee-wc0jhva6wgg6rCoLPmKYToD920mN8wUS8fNQ0e1t-cNnFu7d5UJHMPafysXDuxowGFw6IR-eLosKry5SXsiKBUtG9wKE2z1x26r6cDFXhdlY7bXA6JN1zDKpQsU1DVGzIwmuFTBynVm5pCz3hknukQldw2dAez-3jMPGm5Rk4wk8Bd0PEcEXHM-Pkxfa3YPQ-weqHFrDD3DEJhmKngIbMUzLrsWTHNOwoiEhmMxdd53xXmewHWmTnCpKderM5WbClfb_tRPr1ps50XiH2-hvofi38THqXCvNUCUsUuBhuEGOsHrH82pWyM1zVgMeexj6RZRKDSFiZYCqsF9z6kSmeaWZ-zH4dH37yPKwX349TfoWteuMOt3xqRo2-ZZw2yu-K0xkTO2pl6bC4XkEIC_9h74dZ01DbJ72psBgRn1QUtxwz2N9tUx_3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های جنجالی هادی‌چوپان درباره جاویدنام مسعود ذات پرور: منو شیر شاه، سلطان و شاه خطاب میکرد! عکس منو از باشگاه ها پایین میکشن؛ ولی من بخیل نیستم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107244" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107243">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=rxiyOIvK5m8JCd-8D_HNGdzPiKswCg3zFkBFYwH7RwCJXNfO8EAZcSpliYzMO3g1qRHPq-qGwxr91Z1R4EKGbfHK01nVJcJDtkgDXNU9YS5tHcRNI9li6lTviTzCcNpGWSkrkEoiekXwB-rgTgOW8Kf_VMYlO2Xs6CB81NJLW-txWorXOTwvjgqXeo8QmK2fuZRFWVfQzoFy0jWFjRtf-7yKrpC-GzaJKTmTVfubE0x2TcD9mqmxPevRd40R6AdlqTBtf-XDoUdLjitRAelI-ODeuEO-BtxbixfqCRna4Z1JkYb5dVh95lvjoOOjmSFNYwHpO8obZfpT9AQhvvnajhwVz_9JLYrqJePAtxpGIwIfmk8yFQpeY1e5IsDh_ooDziRjOWXXnwWjizWFyC_McNKPo9Jl2Gh_H2PXK97MxbsZdMuHMKQbCezd6z8Z0x4Nzm_X08RHpOE-37_DoXn83UTGPcLds7qkAqvKMjjPTDMwO9UeDunulZwWMo7sj-3Ho8t4czfZef87yveRvkcsyzbx5oRGenHHqOIMEDShqbcI8kaGDU-tV0YDcYhs_inIpSCgfQC9y0H9FFJk537bCIikpp2Y5-98nJqpqqNZtpu0HcgDQYHJH8l_VCsD-A52B6WFelsAJ6aT5yBAgobt4FhcT3t8EyeZdSNpETkUCqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=rxiyOIvK5m8JCd-8D_HNGdzPiKswCg3zFkBFYwH7RwCJXNfO8EAZcSpliYzMO3g1qRHPq-qGwxr91Z1R4EKGbfHK01nVJcJDtkgDXNU9YS5tHcRNI9li6lTviTzCcNpGWSkrkEoiekXwB-rgTgOW8Kf_VMYlO2Xs6CB81NJLW-txWorXOTwvjgqXeo8QmK2fuZRFWVfQzoFy0jWFjRtf-7yKrpC-GzaJKTmTVfubE0x2TcD9mqmxPevRd40R6AdlqTBtf-XDoUdLjitRAelI-ODeuEO-BtxbixfqCRna4Z1JkYb5dVh95lvjoOOjmSFNYwHpO8obZfpT9AQhvvnajhwVz_9JLYrqJePAtxpGIwIfmk8yFQpeY1e5IsDh_ooDziRjOWXXnwWjizWFyC_McNKPo9Jl2Gh_H2PXK97MxbsZdMuHMKQbCezd6z8Z0x4Nzm_X08RHpOE-37_DoXn83UTGPcLds7qkAqvKMjjPTDMwO9UeDunulZwWMo7sj-3Ho8t4czfZef87yveRvkcsyzbx5oRGenHHqOIMEDShqbcI8kaGDU-tV0YDcYhs_inIpSCgfQC9y0H9FFJk537bCIikpp2Y5-98nJqpqqNZtpu0HcgDQYHJH8l_VCsD-A52B6WFelsAJ6aT5yBAgobt4FhcT3t8EyeZdSNpETkUCqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
به‌مناسبت بازگشت زیدان به فرانسه یادی‌کنیم از این عملکرد تاریخی اسطوره مقابل برزیل در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107243" target="_blank">📅 14:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107242">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎙
👍
احمدزاده سرمربی سابق ملوان از کمک‌های اسطوره احمدرضا عابدزاده می‌گوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107242" target="_blank">📅 14:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107241">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=ZJdtoPHAGUqTV-dj7vMyaEFbC_QExjonk0S3W0g4_t_viXn88CrP47MtqaQV5Ey0mm0kOZsngseuV0Bc8J1A7gInndt9l1QZo4-caxOH14mYQ3Zr-OPnY04ASWDBRVX2Su33rG7FOkoqdnC6hWksa1zD6eZg_TAYOtG67J7A-WRBjo5ujuq7A3dBC2xSF6tCies7nfeVe8OYh5-qAZOVNboR8Wa7SdQqnlMT0G7n4MKvyAoZFO82ji3S7CfGM1kezEeVYXH63ftFU90OIOWRUSGx7h0OW13n4z_oVZVtudNaNBgIAfzkWiebQv5Ltj6Kur8Gl1J6Zt8SuJLD1MIeta5wKkuhifTlau3xc4D9YVQvGCAgzSOrVXOb37ThcbxkzOkV8kPvYfEID5At8zTjnzUClvcqK2C-eQ1t_RCz1VW94e9sxsGodc_o9OgYtlboElclUy2qNKft140apJS5VJkzPN9hEw4273k0f3fbrxN4-drbKHlhX7-1a_TXXdR_3Fntk53pElY_5ZpJo-NLg-I7kbNisTz3cTMMX-B6bAGCFfCk0PmYI91CNox4YnbpQYDQQatH92_0gBfyo3KvnBMqmoeAmmZPPLbQ1rjGlXjPNKgtkTjsGdULBfupOh2EGpF3plYvMGf3WS9O-V-zuqEA4_auSr_Qs-ckCWzPJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=ZJdtoPHAGUqTV-dj7vMyaEFbC_QExjonk0S3W0g4_t_viXn88CrP47MtqaQV5Ey0mm0kOZsngseuV0Bc8J1A7gInndt9l1QZo4-caxOH14mYQ3Zr-OPnY04ASWDBRVX2Su33rG7FOkoqdnC6hWksa1zD6eZg_TAYOtG67J7A-WRBjo5ujuq7A3dBC2xSF6tCies7nfeVe8OYh5-qAZOVNboR8Wa7SdQqnlMT0G7n4MKvyAoZFO82ji3S7CfGM1kezEeVYXH63ftFU90OIOWRUSGx7h0OW13n4z_oVZVtudNaNBgIAfzkWiebQv5Ltj6Kur8Gl1J6Zt8SuJLD1MIeta5wKkuhifTlau3xc4D9YVQvGCAgzSOrVXOb37ThcbxkzOkV8kPvYfEID5At8zTjnzUClvcqK2C-eQ1t_RCz1VW94e9sxsGodc_o9OgYtlboElclUy2qNKft140apJS5VJkzPN9hEw4273k0f3fbrxN4-drbKHlhX7-1a_TXXdR_3Fntk53pElY_5ZpJo-NLg-I7kbNisTz3cTMMX-B6bAGCFfCk0PmYI91CNox4YnbpQYDQQatH92_0gBfyo3KvnBMqmoeAmmZPPLbQ1rjGlXjPNKgtkTjsGdULBfupOh2EGpF3plYvMGf3WS9O-V-zuqEA4_auSr_Qs-ckCWzPJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اولین‌گزارش نیما‌تاجیک پس از ترک صداوسیما و پیوستن به پلتفرم اینترنتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107241" target="_blank">📅 13:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107240">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=W_HwnjzEJYBhH9yiwrbD79LqivtVzRynYfHTkEEXdMreaviYM9OLst94_h7IFiL0MzJTrEYiiFzsIIEgQZacUZ3JhfizjrJ8HSRR_SbKKr919kBgVj0NFAydiyYIfG9iA2WZRlYA7SE5_gKry_bcRIyqA8a_0pl9mhl350wZp0djbjMNSsk-9TFFT57MjZu9tsU8x3bhWw0KiVPF8a2riqyuf1Tfmh9QeXH7y8ImHKFBfuGUmMYRpIenJS3jgLvucVX7OosuuwNm56_LV39OUZRw0AhaG3VzwTqzDaa_4PmddwHys-C0-Knc64O6paN-6X7hrGN2WZWzDxZhfiPcRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=W_HwnjzEJYBhH9yiwrbD79LqivtVzRynYfHTkEEXdMreaviYM9OLst94_h7IFiL0MzJTrEYiiFzsIIEgQZacUZ3JhfizjrJ8HSRR_SbKKr919kBgVj0NFAydiyYIfG9iA2WZRlYA7SE5_gKry_bcRIyqA8a_0pl9mhl350wZp0djbjMNSsk-9TFFT57MjZu9tsU8x3bhWw0KiVPF8a2riqyuf1Tfmh9QeXH7y8ImHKFBfuGUmMYRpIenJS3jgLvucVX7OosuuwNm56_LV39OUZRw0AhaG3VzwTqzDaa_4PmddwHys-C0-Knc64O6paN-6X7hrGN2WZWzDxZhfiPcRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
رد رشوه میلیونی برای امتیاز دادن به استقلال
🔻
اتفاقات هفته آخر فصل ۸۱-۸۰ لیگ برتر؛ قهرمانی پرسپولیس بعد از شکست باورنکردنی استقلال به ملوانِ محمد احمدزاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107240" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107237">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCxGKnw_7Cx8WuV2DUdyEEbWV_5LW1v_T-ccmC21Uh56XYTCpNCTy7cxp-nyOQnID6yYxbiesoWoJRGhXr1DQc0pnxN1NmFW3c7hnoz0U3sDXXS_xccksrByGBOyRKASx-lwqQpXEtbU7WkMh2R7nhnFZWlteWzN5OFxvNbj-k3NsTppyyEXAA93VyqOicv3RmMHoShGQRxLIAPDxjZ2ws5UuwH2E2VUrRUO80mlrhP5LpVsMxVJoclzqw13Dlcrw-W7oV3BjcMJNffSWRi9ju-S21MpZVEhDcxujE0DpeLm5V4yPKP3BWl3HJA7gO1rIydre1sPR1_7eFkslZwASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4OrgS3BiNZ4CwosESqclGTHFyqRg1masaHAwxjzk1CgFeI4FsljoPNjjCB0vL6thWrafACGFNEof_5RiGXfdPIQmvLNnJtqYHG8CcaZDekVAwN0ptbQj_NIGA0jRojnmsc39pXaKX8ESd53dKRDwxRaD1l8RG0vWw_n9GLYvHXyWt5GK_Wg6MDo4uLwVdB0r6rWdMYgcmUuTI4mmBs_6E_UYtczxS2_nSREhCZ6KcScj0Xe8GwClJJPwjazSMaMJ28s5Kk4oSAk5TuKMO8SGeKxygb4vY4vWV3xtjpQhZ8MnEDNcMLoJ5gvesiA0CROGlezwVowWrL46krbDHae7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bo74jNXN6oyIL26uh1VtnNbFsKkSOdz7wwCa-ZareXjXdMuKosYm5PrbTY2dZhPOajF05lyU7VLbYKzsWTaByLoXHRd6rNPfxFrn-r0vOVQO9X_8ue8AbpClDLALjNnN419Pr72k5ztbtV-ooTUbg4eDRGhfOiY_pkgwz9NesZuif-zJZHYD2C56Kpd32X_TqzftXNrLE6MmFN-Yk9-uCpMesYgGMFlARK07WMMhrY2Sr-t_lI5lxyEY4OhttcNOmjBApTY6oF8X9Iq7sJC64WJcKEiQKocEBxu45Fzi-nRw-iqXuXE7439-MFC5P76_I76O5anPB2GEhAVA4D865w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🐐
🇦🇷
تصاویر اسطوره لیونل‌مسی در آخرین جلسه عکاسی با تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107237" target="_blank">📅 12:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107236">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAOvkcs6NHAUUyWqo2-dM4JDtE-A9fvEeLb6bWm-AeVUhKvdHCeSLW8OxXZvbY7C_g1kjsgfDNdxSZ4guZTobyKBQW7Ze6ydizO63vUe0n5qZHpZq3sklrLMjay7sFZ2fopYhkh4uvjHq9LSucMs52iLSY-mJV-7kiKlqY_KxDjABFOURqMO7vB_hpPcmpDWhWfaOXcQvgA-Rq_4UN4yutyO1nGnQS9ukPfesqtSII3gj5s-4eYkLVQnZZZ6v54oFeR0elgHCDLahj1_lTCAry9b-aMgTpo0-aQDqu-yFJvoLDFyODwxLBP8dw6ZCBQTS0-DTGJ5yIrS3PnF3GF2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107236" target="_blank">📅 12:39 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
