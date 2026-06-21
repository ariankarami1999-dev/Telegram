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
<img src="https://cdn5.telesco.pe/file/EnJBuxfszWoaL-HsYuzSU6FxouckcfnR32clTw_UVdRzcM484bijDWNd2ZDEaZp2RJDQQhVWs5ZfgXOyLQVMzoTUc37SJNRE5iaqIxaqny37-6HSCL8ff_McrZedigrzlwErL1nTS72WFuP1rA1oKn3cmDYQt_5WKQo1819cxEMCyF-enUOxtiK7bglya_EgJKub8oKsfcaKaZOMv5vebAHrUcEX-6HWLoFA-8qQuLYm2yxJmStgT62An13BSy2KurbqFBveMQtdepEqHvuPJGuyFHVliG4O3pmJI5BoYz0AFvVJtyUYPcvf-54wckA-tExxpjOt-XAGCDlR4I7Q1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 707K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 02:32:20</div>
<hr>

<div class="tg-post" id="msg-95116">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK9Y2fRIFwHkjBFE4SXUw_KEqSp1d_9_GbuMSK_0fxSqeTiwHbrwWhhQ6D-jdGpCMyFbhT8f6MUE1df5ayOXLVLEw3Of5yFwoilX9c3ZfuCYZwWZrONGrECCk34KVTq93gRwcvlQq1JSK2isTyrbuPvtbIMMt-6dYmAgu-eBNdJNQ4IPsXZKW0Y3KwY4-MACNcTvV5_xhaDIFxKmRxuE3CJWQZnikqA-XM-96pDQdrItGEFKz2OtKLEjnULxJrXxdhvsk0dOudHZzTm30O4NAiBxSVf0nUWtsQbR0sK96qSiGylb8Li6Ifl43MGzZgeDEk3y7XxnNtpHIguzG47dZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید جورجینا خانوم کریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/95116" target="_blank">📅 02:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95115">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پایان نیمه اول
🇺🇾
اروگوئه 2 -
🇨🇻
کیپ ورد 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/95115" target="_blank">📅 02:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95114">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/508a2a45bd.mp4?token=jvYU6yZw_7DFFvyqYpgu9g2EzcNp12aco_pMA8lh77RsyfporqTwYmOMIajl0Mpmzpo7RssLSq_f_asI4zBehztq6RmjK4iVJNS1FJTNON47WkGgvF0RTmMjLEw71Xx9Wn5tRDfEgQBLYHm767c_Ot0z71HNHoY7ZTz7HxEhcBLgY5doJ5L_6rocm0usTYvHCFbTPts5qt0hOe-HlaurrdUuJwkngfSuIgz95DM8c_FlH-oEe_zcHngw6V_qnsSqKgBfHJkDQnYKF0kONdxxgDFSzj16mF4ESv2oDbn-LCUVeplDrPgWCekbjuyC1f_tCmnpevQx4Yws-Z1fF87irg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/508a2a45bd.mp4?token=jvYU6yZw_7DFFvyqYpgu9g2EzcNp12aco_pMA8lh77RsyfporqTwYmOMIajl0Mpmzpo7RssLSq_f_asI4zBehztq6RmjK4iVJNS1FJTNON47WkGgvF0RTmMjLEw71Xx9Wn5tRDfEgQBLYHm767c_Ot0z71HNHoY7ZTz7HxEhcBLgY5doJ5L_6rocm0usTYvHCFbTPts5qt0hOe-HlaurrdUuJwkngfSuIgz95DM8c_FlH-oEe_zcHngw6V_qnsSqKgBfHJkDQnYKF0kONdxxgDFSzj16mF4ESv2oDbn-LCUVeplDrPgWCekbjuyC1f_tCmnpevQx4Yws-Z1fF87irg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇾
گل دوم اروگوئه به کیپ ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/95114" target="_blank">📅 02:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95113">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اروگوئه دومی هم زد</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/95113" target="_blank">📅 02:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95112">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/95112" target="_blank">📅 02:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95111">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cdc8088ef7.mp4?token=lRj8wWAiCSmEmduQuzFpoNHYoTVM7m5rCvcJxRhcf1KgVVWioDXyJ3UT6qwbsns4Fh6H-bZOnV9WyKxcZrvZ6Ij4SLRfSbAr8XiMufOUMSqsSz4_Z-gUPeWu0wh3lJhrSxmdovyWCBLULj2JqBgJ6OBMhclwVLiBbvdtMm2NA6Ry5Hdh7erfgxdVbJUXI6IBHNiBU2atYTN86mKMuWK91PeXQEg6mCrw-VKk--XMX6T4oIbIRV4RIePTV913QbHR9UiVra2AskKnJFjcvNJkzfmvv516Xw2fBXUYcRiQMtfJ94iVWeDyNnaZlAND2YSAv9qkkkV61600hgx90959lg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cdc8088ef7.mp4?token=lRj8wWAiCSmEmduQuzFpoNHYoTVM7m5rCvcJxRhcf1KgVVWioDXyJ3UT6qwbsns4Fh6H-bZOnV9WyKxcZrvZ6Ij4SLRfSbAr8XiMufOUMSqsSz4_Z-gUPeWu0wh3lJhrSxmdovyWCBLULj2JqBgJ6OBMhclwVLiBbvdtMm2NA6Ry5Hdh7erfgxdVbJUXI6IBHNiBU2atYTN86mKMuWK91PeXQEg6mCrw-VKk--XMX6T4oIbIRV4RIePTV913QbHR9UiVra2AskKnJFjcvNJkzfmvv516Xw2fBXUYcRiQMtfJ94iVWeDyNnaZlAND2YSAv9qkkkV61600hgx90959lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇾
گل اول اروگوئه به کیپ ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/95111" target="_blank">📅 02:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95110">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اروگوئه گل مساوی رو زد</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/95110" target="_blank">📅 02:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95109">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
قلعه‌نویی: معادلات گروه را بهم زده ایم و به دنبال صعود به عنوان صدرنشین هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/95109" target="_blank">📅 02:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95108">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pb-MI_mU90jsY3Ka7uEVr7mDNWufq2eSUPgOoE7ruZ3SYX1OmJUEhJi3me4_Pr--qWO-vCPmhMTs89vlyALyNZAsmO1u650--R601bR7rYWV7ztsNrdKMroiZKVOO50Jy5sv_eNKREGq9QTbYIiAyT2d2WlbEyQ3o-lfhHh8B-_50oUDArx7xH0Pt8_rONGkoBjrEJO_SBvHAvPJGKWgtgLH9RdkIZQWkVMYnFy-tFzunBIMl9on6XKDyEQn-XkIvx_-tjyrHVGoOlW7kptnA_LVh4jbHhk3YwjfRG2iPJV6sEskGAoa991iHTJ1MvnSrGr83WOfR2yKDQxTYUAszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کنسیسائو : وقتی صحبت از توانایی گلزنی میشه هیچ کس بهتر از رونالدو نیست ، هیچ اجبار یا ضرورتی نداریم که همیشه توپ رو به کریستیانو پاس بدیم، من توپ رو به هر کسی که تو موقعیت بهتری باشه پاس میدم، رونالدو هم اینجاست تا مثل هر بازیکن دیگه ای به تیم ملی کمک کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/95108" target="_blank">📅 02:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95107">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/95107" target="_blank">📅 02:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95106">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l3oBI-S6bF9WGpliKDva0MS8tEh5EoCBWF_shE4jPKQjSpiL7PH6k43_5IxbOMBp3frXg25Tsp6ozLEW6rogonQVJxs5_Af0hxMXOXvjIHwXLjklHdoDzS4ASE7L_kACAzE9cpKLoDxQYmnXug5j9DhdpLF2nrhQvtWMHoCuTEJ4PANkceiEasIOtMAdQBa2ZagqF_aie6vC1rsbPeX7vvo5PVaOW9WjKXEUvLjWVJwr80HT2ClxsQFG4e2IbdIXQ2YSO2aZymvuiWHCoYNuped09crUwXN5P1g0P-Y8gFs8SvjAH0wdFK8fwtR06LYz8e5sfzsHiXCTBd5LDJ89pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/95106" target="_blank">📅 02:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95105">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca2c51a18c.mp4?token=KOpAoPflID9C-tw62x-73SWB6ChBhKaS2j4nXEPD0kWnR5N8Cdlqt5AaJ3UlyH204ptd8KK5gzUE0IdxrSTgDMTx2G2j6YSA3Ni4DcxPSZyGeaxaS7VoSgGfB0OdyrfGsVj26DF2bQNBLQySagi8The-f084APZ2cVPpzQjuJd5A7aumxjUzEHDmv-eLZT0pJgblzXuMAxR1Xi8VFamT2sMt9rW6wNhTTYFH_m9TStiK7YtHYxEbe0NnJdqGeIrp1la7y7vGVoSk2ZKKAW05gMQ4MICe-WM8VHu0va2KXgLKzIxG6C8bXntmKPkoX5ANPo84X-b8N7hLIYojtmbFVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca2c51a18c.mp4?token=KOpAoPflID9C-tw62x-73SWB6ChBhKaS2j4nXEPD0kWnR5N8Cdlqt5AaJ3UlyH204ptd8KK5gzUE0IdxrSTgDMTx2G2j6YSA3Ni4DcxPSZyGeaxaS7VoSgGfB0OdyrfGsVj26DF2bQNBLQySagi8The-f084APZ2cVPpzQjuJd5A7aumxjUzEHDmv-eLZT0pJgblzXuMAxR1Xi8VFamT2sMt9rW6wNhTTYFH_m9TStiK7YtHYxEbe0NnJdqGeIrp1la7y7vGVoSk2ZKKAW05gMQ4MICe-WM8VHu0va2KXgLKzIxG6C8bXntmKPkoX5ANPo84X-b8N7hLIYojtmbFVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول کیپ ورد به اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/95105" target="_blank">📅 01:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95104">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چه سوپرگلی</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95104" target="_blank">📅 01:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95103">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کیپ ورد زدددد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95103" target="_blank">📅 01:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95101">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95101" target="_blank">📅 01:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95100">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJTdnISWDjq0f0ykgwWwQS7KKE8FgvYk4sJs2OQF0t8sZy1wBAu2_RjwblXjMu5hIWTQKCbzLJm4OzCWy9g7EK0QD6O3ySDZtZhkJ9mK5hMgysH9K2eoIljirAjCKMFADTuYkUWaT_ZXUUov0P4dJJca_7fVtpJJ9npawcwXrZrgY8_VyorLh_6tYVidaF2gfc41_WilGZZCBeHXivqlByCeuhx_Pe39eK9_gZCKk0t0R1bJGsKUj97AgzNiJoPv1W2N0mK4y_QuWMZ9OTERNLKaRM_V4Qcw4_WLl5kfJi7v9QsEVSphWEw3ThLSZx9c4XruDosfQqtpjct_Q9op3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوارز تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/95100" target="_blank">📅 01:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95099">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4516eab25c.mp4?token=HMteqNFq3X_rsg8ie0Zfz60gPGYkX_9QauHWS5nlUp54jTj7-NNdcRCUnjJjSMp9tUNEGjbD9GmWoryj0NHoVgbx80wbHtIR8TIKYyVu5iJXnLKB7DK1kzJY65sdiBolwjJmPTo8s9vJG7MObNIv3ZVber4WKZizxaZsHhxnn-uxr_a3F9JHQJ1WjgyLqA3-VR_1xb_M2UOkjzZMq8RHkktFIhUSy4V47wd_XF6Ls8Daqj9yfYmvSZ9RO70SnAjk596Dj0JcpXS8KIJi2PsYvkMSNvtxzKQdvFKmjfBHWVYl5bmbpmNzMywpqQe3PGzpIUpIAcnyi1cMn23s4wiQtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4516eab25c.mp4?token=HMteqNFq3X_rsg8ie0Zfz60gPGYkX_9QauHWS5nlUp54jTj7-NNdcRCUnjJjSMp9tUNEGjbD9GmWoryj0NHoVgbx80wbHtIR8TIKYyVu5iJXnLKB7DK1kzJY65sdiBolwjJmPTo8s9vJG7MObNIv3ZVber4WKZizxaZsHhxnn-uxr_a3F9JHQJ1WjgyLqA3-VR_1xb_M2UOkjzZMq8RHkktFIhUSy4V47wd_XF6Ls8Daqj9yfYmvSZ9RO70SnAjk596Dj0JcpXS8KIJi2PsYvkMSNvtxzKQdvFKmjfBHWVYl5bmbpmNzMywpqQe3PGzpIUpIAcnyi1cMn23s4wiQtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
💥
دلیل موفقیت امشب تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95099" target="_blank">📅 01:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95098">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fya9C4NsYJzU0wYwJc5akFYyTJliHgdAQhxlxpA8nMGw8hQkofTFe-353O7CE9rQP4RQ-n3m6h1fexGsYALxWENel4tL3Zn-P0Ni82q9XZVUTpeRHIQwSTQYcaIWT0nfmbA0A1tR8fucMVNiQzCo3-axB5xlYK7MJ8ClsUNFxCMVaUGYHb7aq4hC6aySL9v0YsOHusvk3cQXhd18UM1KS5uB5LSZ47YyxsNcvFYSPrllHYWjq16zxoFlwo5H_eXWB3DuyA34zlPoTbjp-l6P92Yn_kam26AixoXKRwrUYTfFiWNQPUc-dpc8LhP1-QUMvnOQQGr_TcrCkG6olLTH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
با تساوی مقابل منتخب ایران، بلژیک در رنکینگ فیفا به رده دهم سقوط کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95098" target="_blank">📅 01:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95097">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0036204705.mp4?token=VOrY0Al3HkrFKi1FyHDsN2Xr1Xu5gXWykZ-965sRchTI3uTnghTfGJvaK_VpRkBA0upOIoFHTZQeGt6bmFzbM_ng6-Hcu0nYhAWjnRB2Rn0YATlWxJ2oP7KrU0JmeCfdHLyk9ZzHV2R08kj8Pzy43JrHzswe9DfHsJ4t1pSLO35SKEANaldYeo8QuReNXJxQwG5g_J5JVYHciiOLcTtrdXNkYiQQVq870Mk54JoMVPdBY1-YwylzKV1e9gL4OwONs9-fghAlssBvwsbZH1D19bDCIp48hkZLygfGK5-PNfXO-p9_k43No8kvPZgx9kR1DsQ2gQ2SMdIEEJ3kSiOvUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0036204705.mp4?token=VOrY0Al3HkrFKi1FyHDsN2Xr1Xu5gXWykZ-965sRchTI3uTnghTfGJvaK_VpRkBA0upOIoFHTZQeGt6bmFzbM_ng6-Hcu0nYhAWjnRB2Rn0YATlWxJ2oP7KrU0JmeCfdHLyk9ZzHV2R08kj8Pzy43JrHzswe9DfHsJ4t1pSLO35SKEANaldYeo8QuReNXJxQwG5g_J5JVYHciiOLcTtrdXNkYiQQVq870Mk54JoMVPdBY1-YwylzKV1e9gL4OwONs9-fghAlssBvwsbZH1D19bDCIp48hkZLygfGK5-PNfXO-p9_k43No8kvPZgx9kR1DsQ2gQ2SMdIEEJ3kSiOvUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ریدممممم حرکات دست قلعه‌نوییوووو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95097" target="_blank">📅 01:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95096">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssZzmC1yCsFlKOZ_DcrixSxPEntzuN6w4TA9lcsJ7i9x1ZRAHCb5LQOLgAnM2wqVa_-tSBCqnm9p4EL3WZv7fbNgTHFCrBzXpzFMmbg6m9nujx820t6HxaSjRsfhd3zmTCxchXuarhr1Sv8fG0u2vXJVe2mwH9PO5FzI8t3FmpXgB4pVH4r5g7G7QdipVojKFBp9SM0Jt0vsAaOFLfMzmwWX6KpVgnYiXkaXXU_nW5WCcpigVu6E4yBnAQSK4NcyPBjOuYdlm3oqpqKB5-IJIY5Ex7iYQ8A9BJZfSpR4LISFkH1gUuggbNyOhxh0UTZtVbxn09s_gDlWF0kkObj0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
آمار پشم ریزون؛
دروازبان‌هایی که تو تاریخ جام جهانی نمره کامل 10 رو گرفتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95096" target="_blank">📅 01:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95095">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c180e5c8f.mp4?token=q5n_-J1CvcWt2Lzi9cYdko1nT6JX-K91ykSvtD0Fc6jEHWnlyj0HPc_6mZW5rQefwIUqUfkopDaL6RslqvJoabYpcg2NuAzEcRKN20IOVAY6KqIs92Jb0tBO6WIk31Jm6_gW2v_Fjw89fqIGaW11lOASfAUFLK6g3kcDR_MDjwGcscEZifdxJi7-9WNvysB0BtrMATHi21-3akp3Qn8J_RK7RzkqHW3Gb2trNpWc5jd_0BddPDU6Dh0dnWL81JB2bm-Cquwmqo3goT7iY6ylxBXOTPqm9Pwq3O4jgjqLZT4fhqiO8xVbGvdUUPAWEe462GJHMCEWREU99BKo8cw17l29I9HVQpEjlBtvHYwE_tw1LoSzD7Wlq8TyB4fLHxbgdDuRnTu2-FeqvSzFUl-OPhiWpg2zOlMhq1BBT_X02qALneed_gayXeAOBT0w9oQsnpBAwKj2svvaG9BwSSuni4cvr1Q1crh4obZ1-6zyagcUi54hUdtac-gdwTxGTCNlYFkIodk95fRJpwdDfvhqkKXVBWmKWgwreb8HUnss6dvAHKamXCuVklBFP-Ti10ScuuikEgNsJ2unm5VnvE-saF7vQO29uxTVS0K2pu3AMn_hy_Szm1eqTBtRBac_it1Ve9bnqXAjOmVLS1unDrT1TU6Fg-1moLUSqZRgDyBt8uU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c180e5c8f.mp4?token=q5n_-J1CvcWt2Lzi9cYdko1nT6JX-K91ykSvtD0Fc6jEHWnlyj0HPc_6mZW5rQefwIUqUfkopDaL6RslqvJoabYpcg2NuAzEcRKN20IOVAY6KqIs92Jb0tBO6WIk31Jm6_gW2v_Fjw89fqIGaW11lOASfAUFLK6g3kcDR_MDjwGcscEZifdxJi7-9WNvysB0BtrMATHi21-3akp3Qn8J_RK7RzkqHW3Gb2trNpWc5jd_0BddPDU6Dh0dnWL81JB2bm-Cquwmqo3goT7iY6ylxBXOTPqm9Pwq3O4jgjqLZT4fhqiO8xVbGvdUUPAWEe462GJHMCEWREU99BKo8cw17l29I9HVQpEjlBtvHYwE_tw1LoSzD7Wlq8TyB4fLHxbgdDuRnTu2-FeqvSzFUl-OPhiWpg2zOlMhq1BBT_X02qALneed_gayXeAOBT0w9oQsnpBAwKj2svvaG9BwSSuni4cvr1Q1crh4obZ1-6zyagcUi54hUdtac-gdwTxGTCNlYFkIodk95fRJpwdDfvhqkKXVBWmKWgwreb8HUnss6dvAHKamXCuVklBFP-Ti10ScuuikEgNsJ2unm5VnvE-saF7vQO29uxTVS0K2pu3AMn_hy_Szm1eqTBtRBac_it1Ve9bnqXAjOmVLS1unDrT1TU6Fg-1moLUSqZRgDyBt8uU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
👀
سیو خایه‌افکن بیرانوند از این‌زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95095" target="_blank">📅 01:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95094">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccbcf146d.mp4?token=VckpsSJF6i6aJdyVX_MgEi8M6_GZuY6NrNsbJ-PmlDThb7UUMFurxJASKzRnO4eZVEj8I8LXXmi6t-Prc-P0dzOLKP64BIWIhy5nLgdlmzQrN0ceoA99bzlBTdx1VThHXA-fXFJLzFpBvP2KAEWj9PoSsla9CoKmL_KqEiLY3WXVbAk5sFUguuCC-T7XhbgV_x8RN4lJvp3E10UQy6wa5WzctnLV7uH1FeAv62O-JdFvbPBsifPy20Izyx2K4ljr9Y1Y-LN_DS74fAxh_95w4NSJK-d-RbMy8_zkjNzKcj5Q5SFEe0tzcYbTP4Z3ktmGMseyfP_kiTDgzk9PFJ7O9ii1wGE3Tve7rOYMJiAFUlaz38zMqCzXnHIj1C1FhLLCBPxu6fPop13Z5mIrpntoFHfUgX4sCBKwtPRAbwUkxZ7WApX2ARpj4n8tg8I574QZbKX5SeU1AiRnDWecMWnljNB-4KBefoQ5bn388fB9ONXFsfolMKD22nAzvqrZBAq0KnskEk6fil2ufUs33HGScaNQ7Oa261SK1aWA7kDRiU-7QbaVxZYAkU14O1NGOLvAb32_KRFyqJ8EqpUwITbKu4jHakRzdG9JoUlMdX-AewA64nl-eSPFo6HPAX1YK2QgLTyNXcRh4K4_yR9N4cKN5tlBNLdlFRvjCtrz7J65YDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccbcf146d.mp4?token=VckpsSJF6i6aJdyVX_MgEi8M6_GZuY6NrNsbJ-PmlDThb7UUMFurxJASKzRnO4eZVEj8I8LXXmi6t-Prc-P0dzOLKP64BIWIhy5nLgdlmzQrN0ceoA99bzlBTdx1VThHXA-fXFJLzFpBvP2KAEWj9PoSsla9CoKmL_KqEiLY3WXVbAk5sFUguuCC-T7XhbgV_x8RN4lJvp3E10UQy6wa5WzctnLV7uH1FeAv62O-JdFvbPBsifPy20Izyx2K4ljr9Y1Y-LN_DS74fAxh_95w4NSJK-d-RbMy8_zkjNzKcj5Q5SFEe0tzcYbTP4Z3ktmGMseyfP_kiTDgzk9PFJ7O9ii1wGE3Tve7rOYMJiAFUlaz38zMqCzXnHIj1C1FhLLCBPxu6fPop13Z5mIrpntoFHfUgX4sCBKwtPRAbwUkxZ7WApX2ARpj4n8tg8I574QZbKX5SeU1AiRnDWecMWnljNB-4KBefoQ5bn388fB9ONXFsfolMKD22nAzvqrZBAq0KnskEk6fil2ufUs33HGScaNQ7Oa261SK1aWA7kDRiU-7QbaVxZYAkU14O1NGOLvAb32_KRFyqJ8EqpUwITbKu4jHakRzdG9JoUlMdX-AewA64nl-eSPFo6HPAX1YK2QgLTyNXcRh4K4_yR9N4cKN5tlBNLdlFRvjCtrz7J65YDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امید نورافکن: بازی با بلژیک، بازی تاریخی برای ما بود/از لحاظ بدنی در مقابل مصر، تیم آماده تر به زمین خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95094" target="_blank">📅 01:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95093">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d8e1f59.mp4?token=oMO9ymQ5Mb1ykNflMH85GxDo-3w10Xw6jFOf0vUlloRZ8XmemfDrpNdiswM56cT8G8h3xZG8_8rAgFD2Jag4swIpk0LyZ6D5fzG5JA1W-8e7AqNmksXXCvqRqhy1-2FieCpXd-4zL8DsFgEywHfgkxdLdFwkVmXeycT4Sn_Sk2_roP3SNBqh5EGYNRp9_Qdl7TiIbf8dyTyprd48jVpqnhImMrs_HHcYApeEJ_p1M8ZTi4JnChLtF32fAAWO0ZE1vHOOW_lhyvXoIXtof7oDnY6YS-671rSF-WJ4yCQFpw7AWNNhu96sek_qhN8Gqo9kNP1QciuwNpy1r_sA5me3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d8e1f59.mp4?token=oMO9ymQ5Mb1ykNflMH85GxDo-3w10Xw6jFOf0vUlloRZ8XmemfDrpNdiswM56cT8G8h3xZG8_8rAgFD2Jag4swIpk0LyZ6D5fzG5JA1W-8e7AqNmksXXCvqRqhy1-2FieCpXd-4zL8DsFgEywHfgkxdLdFwkVmXeycT4Sn_Sk2_roP3SNBqh5EGYNRp9_Qdl7TiIbf8dyTyprd48jVpqnhImMrs_HHcYApeEJ_p1M8ZTi4JnChLtF32fAAWO0ZE1vHOOW_lhyvXoIXtof7oDnY6YS-671rSF-WJ4yCQFpw7AWNNhu96sek_qhN8Gqo9kNP1QciuwNpy1r_sA5me3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استراتژی امشب قلعه‌نویی که عالی بود
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95093" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95092">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95092" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95091">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vTSCCCCsIm2uGCfGJmTbCLrt-63vpnu4z5p8Ef4n3lJghxgpjxsi3w5Jym18uJlXiI5Ti05ZAtaGU7uK_Nn-onYa1JP7FQXqM-1UUOCG_BdXFZZgui4drR-lu52_onz779t7yzw5yxdz1ZzQD2f6SKTigiVlCN4SmDE6XFiDkoc760EeVqbjZpVXzUQ9o7SckZ71P4P73-W-QT7UTSxpRr8y1K5gtPRTTR9Qs7FGAFNrLzf2cM1ilrQ5nj2KDaNyUlUJd2l8CcRe75-bJnxznwVhKLqrUngCVqcQbcipqX-msCrxwSwlL40jVvIpAxIlCSalwN4NqUKfL6-jmLAZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95091" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95090">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوری از رومانو   بیرانوند به رئال مادرید  here we goooooooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95090" target="_blank">📅 01:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95089">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RkkzD1Yqmp37DMnFhjFKeedduhtCdU40uPMm8VCLdqCpw9UjCHs4dTeJv58nVa9E3SMQMwbMNqYo_aAJAWLDcntHJkUMlSp72xYP6Y34VrJCGk3JvQSDsUYCNPoa9Xq6UGiiQPqXYNRfinHyiJ7C5IpVE7ZrGvoSBN0oJXvNeuXA9wh16XSWkARZC3PKVtP45ac2qDOSt3n_Vdugf8esyIFgBusgla45SK7kisZc1gw6QzRfCBXeGXli91LqgOaQoUKNgF1FJornhD5itBuPScm7lgVbxIMCk0ko6ZYDxyzhL6pINjr1t4DKyJU4yx33-K586dI-dOZerxciV2Ai5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوری از رومانو
بیرانوند به رئال مادرید
here we goooooooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95089" target="_blank">📅 00:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95088">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csUhcNeVNfxP1-4Z_7FuNRJRVSjp1v7QHNZBhx-dwlHrLNJpXJiF3GEezNqvig8lOhxHFOdscOMdoURZO_wqtaxf8GEmhk7cYb8wqIXwGqyAkE6CrDDoPH_iumowtvlllpd0q6paIqIcMKGi02fHIBtE1PxVPuuhOWDTVTUdeSbEgHUioSMZC0ugEGkpt6EjbuBHf0sykUU_1k5sN5odEnazTdgGbl2kcQcUU5dATtnmrtoaXNvOgy8UNp0rFOqLKXf9yYKuUBsuKE1_0JM2gSBC6vNX3Mk3RNtiJIx6LkUky17956WRW-gPm6fpGB_I6hG-wYcsx_rTfzONMFfOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بیرانوند و جایزه‌اش بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95088" target="_blank">📅 00:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95087">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a4d65e8d.mp4?token=LNRpI5qAeh1lc8wHnM8gRnnl4HcJOc5uhNKOl-Zi_Ch_uUpz92GzB4GwHNpRO2o-rChNmC6K4orq4hC56Q8DJExPlrGqt3ltO-pOvR1mK6G2GPjpYR3EsLStLCnuIkRdptMuYvOgyoHCkXeeMQBkxUnhaeVfPHHM8wvOTFgiKjax5satkjLosr5hUec9zR_jskBpmFyMXd-rPmiNxj6pY9W7yC5xe1f6N-rimbXZGDN-R8xvzZgz5nLsoV27pRx91EtrEmuTEg-TGoVblgop903SPBfTphr43kX-DYgb_PhfqG9Mnlx1rMyA0W9qfjCYUPh2ooPfvR_CmfGDDxnfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a4d65e8d.mp4?token=LNRpI5qAeh1lc8wHnM8gRnnl4HcJOc5uhNKOl-Zi_Ch_uUpz92GzB4GwHNpRO2o-rChNmC6K4orq4hC56Q8DJExPlrGqt3ltO-pOvR1mK6G2GPjpYR3EsLStLCnuIkRdptMuYvOgyoHCkXeeMQBkxUnhaeVfPHHM8wvOTFgiKjax5satkjLosr5hUec9zR_jskBpmFyMXd-rPmiNxj6pY9W7yC5xe1f6N-rimbXZGDN-R8xvzZgz5nLsoV27pRx91EtrEmuTEg-TGoVblgop903SPBfTphr43kX-DYgb_PhfqG9Mnlx1rMyA0W9qfjCYUPh2ooPfvR_CmfGDDxnfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
💥
واکنش فیروز کریمی به سیو بیرانوند: خدایی خیلی تنگ بود
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95087" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95086">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjS-BPLyROQy2duslJBTsd3kvoc3KlNQ44uMvxed1zGTJetRZ6Tt1zMBunjdRdAdl08K9-_KHBbwWZSZUfXJbZ-iNpEH19e2Ez8R_L1K686y84rF94nBs4pzD1hJ1mu_VB_KlLFKLYZ_nLbhbwrINB3lCuqWgUgd797MmO0qaIRByT-YU04N__zI5ZZF2Jo1poO7J0HGtW4rvK-sKfu4cfR4kM4MFHJxcAmm94vYomjwo_UxRytRNeSm38fsbdgKMZJKr3CgvbQ4reZyWHTR4q71B354FbdpMRf1NC-efVlsQyUDmRfmmmIBPfegWmjIC1Kd6hStCkxgCZ1hbfciiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🇮🇷
زلاتان ابراهیموویچ: در نیمه اول خواب‌آلود بودم و در نیمه دوم چرت زدم، بدترین بازی‌ای که چشمم دیده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/95086" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95085">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD8TmTUqp5Vua_sSrw8t7vLLRz3vezAsGOICmEYMxhHEs587-dbXSOjwhPBd0E77FaEvzXBJ-hB41mqf8gXTNk9qxBVj6KPPukD13b77iEPKCgIGwwREFuRHBIJSaGXJbckCmYyCUGs8hPmNpLpW9MNweJIwghBZZ1fmR855AnvklG9SsWsfi9WFbQlU612aoD7QYPcH6uOhqxnT6uSdLjfUvttnQYOFuuA58v_GlaDpkJ3TdoQlKrseZuzpwWbl9yT4veKssrdAqjI5UNiu-nNr0kYc3N572JXAPN2ZGUzft1eN1GhCch3nMhhjwhEOClKEtxYqAAGvwHhI0jrr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🤣
تا اینجای جام جهانی کلا سه تا بازیکن نمره کامل 10 گرفتن که یکیش مسیه یکیش بیرانوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/95085" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95084">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-5v7t1aq08ZvKp2_EZxZ8xyLPavCVewZ7cdi1v--t6vHzCn5PExduglusEwaaYkG7oyAlKuskbRAVG_VhLAMNfIrpfjzo78OCU-dUydCNnCVQJQ1XGOmYAkjqlRwGLB9Z-OraLjFyn3pO1QlfDLDtxS0QsD6FtXNDOdrcso-xTQM1rdB6VltwuNa-xmsY3cjoI0rHknQ0E-dZapfTUyqp5tXHZyDlxBGYOkojL7nHE3RLqWYeNdT-5A2voglEik303pv2bicAAstv0VwhTCb_eTlk6ftTqczxmWHgIiMdxn_4AYHl2zx82ijxpkrsfU4wnkpk0xRVGOhhMo11UBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو محرم وسط خاک امریکا در حالی که داغدار رهبر شهیدمون هستیم رقص بندری میرید؟ ما ملت ایران خواهان اعدام تک تک این بی‌غیرت‌ها هستیم که داخل ایام عزیز محرم بندری میرقصن
😆
😆
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/95084" target="_blank">📅 00:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/95083" target="_blank">📅 00:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95082">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evYcWf0zJxhITQprB02JL9iQ12iYAX3EcuWBTp9_I-r59yYFQn9I9uO3aAUaYDMd4yIVI59Fdfu2EsM419PSNqgQPrnZ-EOZ6p9coz9T-Vl6cx3Hffj1uWng_ENw7aPtjV9N8mkU0Z5-Q_HOSGBfezM9fw3qVo9krx0jvOjnq9bHVL2Eq0S8AAtcRAS4HiiYJ0YnZYne-B4GIFFsGMYetFiQ1BtI8IXqB2ffMQoPGfhySOUvkugzXdT20JeqJjfrPFsOoZ7rjx3kpoxQx9eGTz_SlUG6KSQHDo_wrjsa7otnjvDaiA0I0rJ44gSmSIEwlHJRw9EMAXqjzlwoUIhCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🙂
استوری سردار آزمون بعد تساوی منتخب ایران مقابل بلژیک ده‌نفره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/95082" target="_blank">📅 00:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95081">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پرزدینت پزشکیان شییییره</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/95081" target="_blank">📅 00:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95080">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVZppffQVzSptH-SBznow6armIX-FQgC5NLmNM0Nl96DqupUAVJClIUozDuF1El6RJ03Vr_n0wuS4_RIU3pn07w4MCHY9iyqPmqRkRJgNzhw1rRYuAnJm6_cXwyU9G2klswwZ5oIMgJAF1Qtg2jWDZBCyCa6Qg6vt_C3HL9x_SptXKFdc58AnF31I_vF5JF2Rw3sA_YGlgRuyoPO9vt1k-tnZaEJ1STbVfF-9n8-c7MbKM_hxsO7iSCPrqScEKdO1veT-3UI_kGMOLGIbZ15RuNFXXJJ9aReQ6qhKoXDsoDb8ADJ02b7ijelJlMiImIuEeynduMBx67xuO71x4PFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آمار روملو لوکاکو مقابل ایران:
- دریافت کارت زرد
- 0 شوت به سمت دروازه
- 0 فرار موفق
- 10 بار توپ را از دست داد
- او تمام درگیری های زمینی را از دست داد
- بدترین امتیاز (5.7)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/95080" target="_blank">📅 00:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95079">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/95079" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95078">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/95078" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d7eb4f82.mp4?token=tXfqL32P1OCKO6mfrWpCEWWQ3G_0j-fgYlzSCHBvcyjhS2AVhkBhv9-nxz0tY3ttcUhuqPp9AJx3bx8ahzvbeKy_S5AepbIYkDIqcdzWBW6lY1MB_WxKwpDcqCchVHlF3Q1LUpiuaRYHMjdC1TvFKVE_rUOijCn-n2U4uCAzp_dN0hRUXtxDC8CDnaUM62yclpTWzVjDLxHJ01eVhnOSOw-pfd7hLu0B4enT4hnbcXPEykz2nbNlyndwN2tFJ8Pd-flzS4AJzKjXUeo_B8IzebqCU1TdJnVb6W8O2BZXPquhYY30nRU_rujX1U4wfInxE1Un080caY9m2XDdWgbLQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d7eb4f82.mp4?token=tXfqL32P1OCKO6mfrWpCEWWQ3G_0j-fgYlzSCHBvcyjhS2AVhkBhv9-nxz0tY3ttcUhuqPp9AJx3bx8ahzvbeKy_S5AepbIYkDIqcdzWBW6lY1MB_WxKwpDcqCchVHlF3Q1LUpiuaRYHMjdC1TvFKVE_rUOijCn-n2U4uCAzp_dN0hRUXtxDC8CDnaUM62yclpTWzVjDLxHJ01eVhnOSOw-pfd7hLu0B4enT4hnbcXPEykz2nbNlyndwN2tFJ8Pd-flzS4AJzKjXUeo_B8IzebqCU1TdJnVb6W8O2BZXPquhYY30nRU_rujX1U4wfInxE1Un080caY9m2XDdWgbLQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/95077" target="_blank">📅 00:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95076">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ دشت یک‌امتیازی منتخب ایران مقابل بلژیک سردرگم و بی‌دقت؛ قلعه‌نویی با بلژیک ده نفره هم موفق به گلزنی نشد
🇧🇪
بلژیک
😏
😏
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/95076" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95075">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خب کم کم بریم برا پلی سالار عقیلی تو تلویزیون برا مساوی</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/95075" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q67j-J-6uVMUu9ZnS32eWTB0TF6GdbbGqAi648pvb6SJ7LFxlL27nR-9lNcRQG3SHlGtJrI4-EJHvDhr1vJ90qXRChplEi83YbXGHo_32JrpBBLk-RF4MV7dcsX_R7q26bz9ZlMp-vyxQ8UKYjHX-zwIKPcguMWni7CkkSsrXwRNt5VCMquGYpJhbCf2SBrg2MuOcMGaNDnJ3VHOrZzNYvuGLKZvgMbWsyqsuKjgb2YffK-LZszXMCwriWjo2ioiGSNXqcp15aZE118u_xX_VnYRdi1FWfV6Le4HfuBVQQti_xAzxA0qh0yCeDQ9rcSpmpte6t0isYt_YYIWgHBwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ دشت یک‌امتیازی منتخب ایران مقابل بلژیک سردرگم و بی‌دقت؛ قلعه‌نویی با بلژیک ده نفره هم موفق به گلزنی نشد
🇧🇪
بلژیک
😏
😏
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/95074" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قلعه‌نویی از کوووون آوردددد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/95073" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/95072" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95071">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/95071" target="_blank">📅 00:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95070">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">علی نعمتی واقعا کسمغزه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/95070" target="_blank">📅 00:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95069">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">۵ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/95069" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95068">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چرا دفاع میکنه تیم قلعه‌نویی
😐
😐
😂</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/95068" target="_blank">📅 00:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترابی جقی نزدددد</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/95067" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/95066" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95065">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دیبروینه هم کشید بیرون</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/95065" target="_blank">📅 00:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">از کون آورد قلعه‌نویی</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/95064" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیرانوند چی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/95063" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/95062" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95061" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قایدی رو واسه دکوری برده اصلا بازی نمیده</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95060" target="_blank">📅 00:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عزت‌اللهی رفت بیرون
حسین زاده اومد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95059" target="_blank">📅 00:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">موقعیت بلژیکککک از دست رفت</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95058" target="_blank">📅 00:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95057" target="_blank">📅 00:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95056">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کورتوااااا چی گرفتتتتتت</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95056" target="_blank">📅 00:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95055" target="_blank">📅 00:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بلژیک تو دفاعه کامل</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95054" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فردیناند هم تو ورزشگاهه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95053" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سناریو صدرنشینی تیم قلعه‌نویی عذابم ميده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95052" target="_blank">📅 00:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECOck7h-vNJHgA1auy-ZieWIQQcdG76iy1_fNRPEDSWVdtPALAVX8mBA0Wm0bAiMYramfYPotzj4sDPo0o_q91P4yxoBZeMIFY327FgLsioVQj68h1BdWRaVqhTc3jw_ahhIkHk2aDaG77GIxQLqD6J8F5fJfYQJF2OUzTGrGEbMRdgajJcyXwa_dJJGj5EXExCbqwJ9x_m6yO1bze3P0LWyl1utRliVNQLeW7YKDHjraDI4qKvIUwQZw-pC44zyCAioPRRjsfcfOBTPh8YIT-ffsuWddUwOctBSFAqSD64uHGESDfpOgj1UJl9ovvg13rS9KB5QHpV35WK9NMeIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🏆
🇺🇾
ترکیب اروگوئه و کیپ‌ورد؛ ۰۱:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95051" target="_blank">📅 00:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فقط و چوب بهتر از بازیکنای بلژیک بازی کردن
😂</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95050" target="_blank">📅 00:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95049">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">لوکاکو تعویض شد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95049" target="_blank">📅 00:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr7-RrTar-SFrpRpWTil2pBm6PjiQ5S4KLgMz94tWezxZpo0WWpC5FskTDOFOVlTzP6SYN1Ob-V22QAd_sKQM1SHFQMxDBAqE1Z6H_8RBmc4nfbae6d4u6iSGteXTIF7oOSv18exiwpAgu3wBKf9CEBa7UKxyoUUDbCU1OR9crbQecR8A3yLxGB2Kbf1qUdpqfx3_tXN56DK94akRqGQ9xHCcFkYyyK0Vi1VVq5dEHQspeIXBDpPUUXoy-iKMe9duhHMPFZI7kRkuINuGczCwcM9yYKODiWkywo8CQRlOkQeweX4P1FOMkEQ3fq6LIKLunYs3fsR4g7YOotu4jZ7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفاع بلژیککککککک اخراج شدددددددد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95048" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حاجی چی داری میشه امشببببب
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95047" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95046">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دفاع بلژیککککککک اخراج شدددددددد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95046" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95045">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کارت قرمزززززز</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95045" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95044">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">منتخب قلعه داشت میزد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95044" target="_blank">📅 00:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95043">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95043" target="_blank">📅 00:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95042">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c120acd1cb.mp4?token=k80cSbYhKXKUm4J81GHcfkzB4YnH_ZQMU43O_C2qC32az2IwsU1IPtV5pnZMhxkMWqQf1K1HmqYvYz8dGcoJZJ137u63pzpB1MNRAlMkCYj_1A0wPIrt0Y6m_Nvpk4uqSY-h5LVhSE15MY-vU1CXijjOdJGDU_ucpnlC4xaNvAp7qEnpoPPak5tROzGbAZ0YrTqHsDeCROouLtkjvexWcXZ-VObuVQBueGNCR-vp4uXz9F_RC4iYtQR70fDuNtCF48WZ1ZgH8noHwjhGK0QJlgTBhucw7sotJR9Z2jaXnHFnTKACjMvlcZBKw9-GF-s0s85hr4cUqM3Vw2q-RCsE7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c120acd1cb.mp4?token=k80cSbYhKXKUm4J81GHcfkzB4YnH_ZQMU43O_C2qC32az2IwsU1IPtV5pnZMhxkMWqQf1K1HmqYvYz8dGcoJZJ137u63pzpB1MNRAlMkCYj_1A0wPIrt0Y6m_Nvpk4uqSY-h5LVhSE15MY-vU1CXijjOdJGDU_ucpnlC4xaNvAp7qEnpoPPak5tROzGbAZ0YrTqHsDeCROouLtkjvexWcXZ-VObuVQBueGNCR-vp4uXz9F_RC4iYtQR70fDuNtCF48WZ1ZgH8noHwjhGK0QJlgTBhucw7sotJR9Z2jaXnHFnTKACjMvlcZBKw9-GF-s0s85hr4cUqM3Vw2q-RCsE7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😐
😐
علی مولا چی گرفت عمو بهتاش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95042" target="_blank">📅 23:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95041">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اوه اوه طارمی داشت میزد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95041" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95040">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بازمممم گرفتتتتت بیرانوند</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95040" target="_blank">📅 23:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95039">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95039" target="_blank">📅 23:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95038">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b0f8f952.mp4?token=K8fsbev5UBTmBX8Vj5oH4Z9w5KehDHnEbDuZgu7uA_Sa0zpdl39_Stz0ER_g1tZvU5nt6xEW9kiLq2iA0PKUh89JHp4leur8M7Ie5yuU1GXrJwxYjknLgkKO8aenj9y3MxL-kpUT-n93f3uvRBcO2hobFlWgq8igcD1uXrZ0ew-73fIoJ2Ii1ktNoluuVjz9y-l2JMg8Il9QrjiRlVpjgxjL8thF4rBjSi4DKhy7K1rH_0cFSn-un4C9e-vJNdhLMoTPmwzoJoK0u4yn6OfVo4d4cVfPp3IS7ehQgUED52vO-oMSe4RnZtnSrSEQybanS0pvnyBZUJ6eJtQNTsdemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b0f8f952.mp4?token=K8fsbev5UBTmBX8Vj5oH4Z9w5KehDHnEbDuZgu7uA_Sa0zpdl39_Stz0ER_g1tZvU5nt6xEW9kiLq2iA0PKUh89JHp4leur8M7Ie5yuU1GXrJwxYjknLgkKO8aenj9y3MxL-kpUT-n93f3uvRBcO2hobFlWgq8igcD1uXrZ0ew-73fIoJ2Ii1ktNoluuVjz9y-l2JMg8Il9QrjiRlVpjgxjL8thF4rBjSi4DKhy7K1rH_0cFSn-un4C9e-vJNdhLMoTPmwzoJoK0u4yn6OfVo4d4cVfPp3IS7ehQgUED52vO-oMSe4RnZtnSrSEQybanS0pvnyBZUJ6eJtQNTsdemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم بیرانوند اینو گرفت
😐
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95038" target="_blank">📅 23:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95037">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">امشب همزمان تنگه هرمز و تنگه بیرو بستس</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95037" target="_blank">📅 23:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95036">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این چی بودددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95036" target="_blank">📅 23:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95035">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یا علیییی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95035" target="_blank">📅 23:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95034">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چه توپییی گرفتتتت بیرانوند
😐
😐</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95034" target="_blank">📅 23:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95033">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پسماممممممم</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95033" target="_blank">📅 23:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95032">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95032" target="_blank">📅 23:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95031">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bb775b09.mp4?token=eCTkLZEkKNbR8JKLoPqPs7_88Nuk_7TJT3scKHQpwd_C7lRlgTAtrIfjelQ75DrB5B7DDdGH5bHRXkH-b78vMDldKt0VWcmG_EsQf3s9c2rVAoQ6kJ5_ukmee7O4qs8RmoctmkwD_wCBYSA0ynCmmYTrEz-HyADg-rQ48xygD0mA5CmAn-RCjak5G7qiAKRP_lmowuP_o9mxjCV4JsP9Mwj5U7mweGIv87iVR0WD5-Axs0oxORoSdM21BoXzLXvFvjbV3sz-T9ldpQG0yLUL05dFyfce4aTrucgf9eel1foTiXTqv7ScYcG8S9S5V65Qc3zU1DTw94yykgEOZpy-PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bb775b09.mp4?token=eCTkLZEkKNbR8JKLoPqPs7_88Nuk_7TJT3scKHQpwd_C7lRlgTAtrIfjelQ75DrB5B7DDdGH5bHRXkH-b78vMDldKt0VWcmG_EsQf3s9c2rVAoQ6kJ5_ukmee7O4qs8RmoctmkwD_wCBYSA0ynCmmYTrEz-HyADg-rQ48xygD0mA5CmAn-RCjak5G7qiAKRP_lmowuP_o9mxjCV4JsP9Mwj5U7mweGIv87iVR0WD5-Axs0oxORoSdM21BoXzLXvFvjbV3sz-T9ldpQG0yLUL05dFyfce4aTrucgf9eel1foTiXTqv7ScYcG8S9S5V65Qc3zU1DTw94yykgEOZpy-PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مشورت قلعه‌نویی با چت جی‌پی‌تی بین نیمه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95031" target="_blank">📅 23:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95030">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قلعه‌نویی تریلی پارک کردهههه
😂
😂
🤣</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95030" target="_blank">📅 23:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95029">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پشماممممم از کورتواااا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95029" target="_blank">📅 23:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95028">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کورتوااااا چی گرفتتتت</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95028" target="_blank">📅 23:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95027">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95027" target="_blank">📅 23:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95026">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بلژیک نزددددد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95026" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95025">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95025" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95024">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3oONW4ZEq6tTPUsQFJiR-1Z-0o_q9VhAiybX2-l-U0wDzRzg3UcX0hgtYotzxJXClD6mrxFwYfQB50ydIghuFIHbqxvAi3QJco3qDpKXPn7dByGo5x1_suVTX9OwPN4TFTnmJcKioP6N5nJIyeD6OLRf8QaNFxSXejiEYEC9pjopzovkxP1QpXIeAShLxX0mvjr1m45mjpUUFhdPkRcbpo_VKGMrYq6nXwKTosoV4STlgNJNJbsIHaDeRNFApTWOVyVJIhp0tbDft772HIt53MlW_YYgCzVyiv4HXRtdYJBl7Hcg-5atZlH2oPbDcYx_mkyKPh7ytE26DL647kx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تروسارد بعد خطای جهانبخش</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95024" target="_blank">📅 23:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95023">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تروسارد مصدوم شده</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95023" target="_blank">📅 23:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95022">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارشگر فوتبال عباس قانع نیمه اول:
پرچم شیروخورشید پرچم فیک است که هواداران در ورزشگاه در دست دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95022" target="_blank">📅 23:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95020">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_P0nxGAdwSYuAERjbeJtWdUb0WvonOmqfBcmFnUvhfqyHDC6gjJ17Fjf-i1h_6f_0344uofYiSkCBTgyTHDlZ6GIZ_fhisBmCRptycGzfPDyL_EhMP6DgRnYVSgBp_SMFh0yfnCAT5HjKIdLdDC5BrHS_CaGvOMe9JsCBfF8wnk_qY5SSCbfk3jCmakfsF9LWIOkFfoNLHNkXEhTtn6_-TTG3m70CxFuNUPKxdK7QKozzA_a9Q1AdF_PBcPssgAPiDVFh05Ek7CrbwlvtiBZQ-PG2xmNWbJGjho2X-sWGMYnoM_CEC5msyNsruNXTo7hBfgAnYQnkc7wyMi21sq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BksyXm1pA9TpL90A2AUOgXV5J4smwseFgPJF93dSzGEz5Cj630rMEGkXGDOHMQQ2ojAi1syhlpj8OYUPNFpBaC4t23hVduoA59MTPIuZtAUx_bvHGzjCocInNQWPwLhkrCmgmcuEr_FzOOqrFJDGBdWOevf_4Mvb4R-KZMQH_Rt4fmHfUzyUaFDm67H7Er1peJsjfMwxHoynN9-HMfzDfxXa-8k3AOgcXZtpm0zApKshJ4L0O0F6vgzU-dzl4isF97M_OI0qEfjGQzC-xvmeJPMmgo9x_8cyzSvgZdNeLFP5d3nIY06lCdiWkdOI4kvPY-09bgHMrPoitb2PuSsFkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مثبت فکر کن، اونی که حدس میزنی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95020" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95019">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95019" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95018">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8lCcj1jNuBHOFL0Yn_6FmkrEhMliYKJ8_U1jpRWegbE4WUMwzJZp2r-8iLAJCcnPN6Gr92FJYOOSd-G-cnm9xkFLUWfe6oJdTdMBvTAircWC9yakQerSzoNC1gS25s_yYcYFBHH-dMWFiUpu2q4Dx6W_xx0a3lL2wYKGhjbcwDTz5zL-yHp56JJ2vt5NqDQ_R4VyrWMyFFjp5Y6xoUW5ScWSU3lwChtrNI3xz62z4YmbyU5aofgdpMrsAUFhFn-0xXcWQIuv5v8RvWPqX29hxUaqZ8rSl7qTuSfde3puNlM8z_Mc3sQawEgMIemjJgGwDmg2PVhFngpbX_W83CJGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیجای ترول خارجی این عکسو با کپشن ادای احترام طارمی به اسطوره ادن هازارد پخش کردن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95018" target="_blank">📅 23:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95017">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIYmDYYPqSejiofvYCjahLyPAokmvb9a1xLGZ8Ii08Ssb2j4LB--J6cUP4QbXWQAthjlFNtjHPUWnCvSjFkBRKePr_1dUDHvITlRjD5YgBTBcTsKtfzesUurn2gAEmtIsGszYUIRpUmxNLD8BmcJgeLQucUCkQqaBczNcM7C4nqItQ5i_SWkCVrDZx1y08pN6thSBITQ8nTVxIIUk6XcnJYoksByRlioDfdx3dcDmFkkiqqbCQ9MBBlF5PuSb0e1mqcVw_rWziYM1mIYNuuBfykJn7FLjB3WEnd_V6jcKuwEpDEAq5A2Uba0SPxaooB2C1sRZSJu-4tikjT9GSc1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیجای ترول خارجی این عکسو با کپشن ادای احترام طارمی به اسطوره ادن هازارد پخش کردن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95017" target="_blank">📅 23:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95016">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoMBheFKnU-0g3BczWumhEPeWOqHF6xxEghCjBhy8ybO5BfHCrqil1P2eHS_TbwChPlgl2BXj-WR4ThlpjjU5pXIxm_t7Lsg93zBkVJOL16LsExuriy19n6gEchgYhs9dR7djzPM-w0hPCT123xucOpAEcfXBXkMaVFR1bpP_mGa0g307LRB9gRe4gCAgPqoLvNv9A2hRBwSz_MCPELggPsKOxvqiHKsaNAmYT9czqqbHfLD_c0pI5tBIoHIbfC90NogVnZleWIFduxX1-DILgwAxjCIMA0QA1d0c2-Nrtr0Ir-y-KbEnIHzb5FkZ6mdTNsjU_POcSWT30IEM3-huA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نیمه اول؛ توپو میدادین ما هم بازی میکردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95016" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95015">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUSYKrlvLUlAmybby9nwoQKUToQ0b7ZkvFVwasV4PlHRz0ZD0IM0kWKeqmJAREl-I8WZ8E23-VkAFY82FFtfi2-uoBdWg_KsqvO3-cKdxvF2Noaamyna1fddAGVqWsBxx9jvaQWVeG4CGqlbWauiquN4dUUfJq_ByImoxIUCJH3e_RFgxfbgbcfrWjh99r7l63p9iW2YMhXkfS870ul8jr7XFZ-ZwtkPL2mqMdQ6qjphmFdjxVPM6ArWVSyYwRgiJomLJIf43r3ROlu4mdvfFLNZ7JFHKB_7tChSqCWUyAMwsC5D8womeFHf0x77dh0GGx034tk1_AUk1klw9lXRWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب سپهری اگه نوک حمله بود همه چی عوض میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95015" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
