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
<img src="https://cdn5.telesco.pe/file/YY4PXxtnkFfUcBm438lPy88QxJ3ZB-XJtLVlCG_lRKQSEBd2FqDRQcc-sUXUprEtIgE3MPjP0iwB9cN8eDkvkwCzqFeArgeuUOnYLwvzOi6YEDTSjuj4SPH50psm_53PwGglGnnpbSH8ohTwHkmMrMP02yMWvr_BLHtnjeoaqL9fptQo6W4XhdQBz_xVMYlEPODUDd4qYDYOyEZUm2_CSVAd8NkmRKga-_tnE7fcZ8BSOoDbd6nekoCjqABj7ziGRuUxQvizQvjK0BXixec0B73jzrED1j8WbdybKgOYetKlH04szBqXt_Z-x9EEeNQpBaHjKN5TKwAMw0tjzp2xZg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 516K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 14:29:53</div>
<hr>

<div class="tg-post" id="msg-102242">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=Q0rNQeB0vpheGkrHJCbJe0I553gOe080Hz1bDQd5cJwP45iexHDJEi1t1YRHIpgc8SOogW-3Aviowgdn6RxEq1RGoRW3j5_m9E8caGdVqwTr-BuxCAtthysoNAGfhcxukR_DiM4r6bixPFi-nzzWV6nWPsZ7OurGakCDjvygz0JltJ3XdIPZfwd6SGNfuzcsh3DfqU8le3MHfNar2Wxk-ufBeI9F0AXmwj_PiExwCWihWYYGNbTgoFjBS65gntRfeRH2TqEJnj6_ajg5yzutLs2D6zcb7ba-POCXIFZdxOGQPWKojT7KO6CJttpT8SCjoMe0lRF53c6H9mXAcxOUkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=Q0rNQeB0vpheGkrHJCbJe0I553gOe080Hz1bDQd5cJwP45iexHDJEi1t1YRHIpgc8SOogW-3Aviowgdn6RxEq1RGoRW3j5_m9E8caGdVqwTr-BuxCAtthysoNAGfhcxukR_DiM4r6bixPFi-nzzWV6nWPsZ7OurGakCDjvygz0JltJ3XdIPZfwd6SGNfuzcsh3DfqU8le3MHfNar2Wxk-ufBeI9F0AXmwj_PiExwCWihWYYGNbTgoFjBS65gntRfeRH2TqEJnj6_ajg5yzutLs2D6zcb7ba-POCXIFZdxOGQPWKojT7KO6CJttpT8SCjoMe0lRF53c6H9mXAcxOUkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوازده‌سال پیش در چنین روزی اوریگی زننده گل تاریخی لیورپول به بارسلونا، به جمع لک‌لک ها پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/102242" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102241">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=LTQ2a4LMVDFqXkSVUdDqUxSI4M-6VWqVcrl9to2aKM3kFW8SgCi87364exmK8QR9V8z6PDZAA2L5HinR7W_mR_Yt9FIZzpluOcb6xmspf6hJvmvaEc8JkbOthvnBHjDYVravojPzNOyA5J0iiWsH9lB0TuvgXSq_xUX0BdKG4hOA_7wBPRPHwCG6jZsAMypl61jH8zev7eDT46oQdTAUWQFZae_D3THFhDl5KhZHJjZDPeeMYvyBLS7quRJpx-YzcRrPntTjlI1388J_8dugJBs_4k9Bp0X7PtuiSztZT3YwaZUs2D85QDUxYerb1rffT8WoQ2FwXeju_-XapMM1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=LTQ2a4LMVDFqXkSVUdDqUxSI4M-6VWqVcrl9to2aKM3kFW8SgCi87364exmK8QR9V8z6PDZAA2L5HinR7W_mR_Yt9FIZzpluOcb6xmspf6hJvmvaEc8JkbOthvnBHjDYVravojPzNOyA5J0iiWsH9lB0TuvgXSq_xUX0BdKG4hOA_7wBPRPHwCG6jZsAMypl61jH8zev7eDT46oQdTAUWQFZae_D3THFhDl5KhZHJjZDPeeMYvyBLS7quRJpx-YzcRrPntTjlI1388J_8dugJBs_4k9Bp0X7PtuiSztZT3YwaZUs2D85QDUxYerb1rffT8WoQ2FwXeju_-XapMM1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو انگیزشی با روایتی‌از زندگی مایکل جردن
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/102241" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102240">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_-ROEaU9hJfHo6Mi39lkj0RsxtmxlsyX9TZhFXpqBsvIQj7jWiOilzJCL6rzkBmosTwwTsp9dxy9dV-IMpoOXYwjhZfIjtduLvEgVhHJrEnHR1AM4kYQOUyDcVkMucaKY-M0KgSfXeYwo7hFQVbfdceirUFyvRdfR3r4EvVrviTMfxAg4mqGRt60tWZErI1zoqnRxSAzbqQrzUmp2_aLXZfOmGIrqzm8lxJCUxC8Ah1FkpQbW2tgQ5jsjgGFukqIgfvvPW-6dR_Icvf5HQOpZOZcsYr0DUE7psCZ9o9RHg9q1zGX4n_LVvuKQKPRnCU1kKCjF_mHWImFpylFV1D-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🚨
‼️
پاول دورف مدیر تلگرام، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفت!
و اما واکنش اکانت رسمی تلگرام توی توییتر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/102240" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102239">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴󠁧󠁢󠁷󠁬󠁳󠁿
همراه باشیم با بهترین نسخه گرت‌بیل در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/102239" target="_blank">📅 13:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102237">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KxuOi-iRHNK2hYvec_yOxonjXvsFg9cQWCmGyMWgz7ZwNqZ_LvTndQfisDsCR_SZy4itFIL54z1hUxicRgUvEQqpdcHOBYjfcf6qun7O7MW8ArlN7A4EiVbqWvCQRhpV_O_2xa8QfzCay5qdY7XIaHzFI0tJ-GDV72jZKp9i0tNPQcDFEpj93KxfeGYwBfm3cfN1oz4UCgoKJYNzRjec4DcH7a4b78uV9FAOWylwG8uF-ilV6AZNTB4ULMj7Fsw-5HFCkEJwAr5jhz-I_INy_r3xf4y9dFpkd-2Y0kCjnPSkY1Rsgj5zjnpYFOP3VA_PyPKtYZIlzOvdah8QGlQCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWTP5x2PZ5MPm1QZ7W2xZoyrqAAaaczL1pqrkkxii4zqcDut56F2Qj1jZ4LsumQcaVLjXAEw92NwcukbrxkBE6PblLOnTfkn3xl8dYFIPu3yILyg3UCItBOPYTH068gQ7jJZd5CxKBv99CVNsvBGe9zuahRoB6vERHVra-ShwVaL4rA0f02TNQ24CBJOvM9JltBFgTDShOblCEdsnHNX8kr_6ODHizU6sU_zrD7Ez-1t01qpjlrGIi73Yr3tmLfbRJ6YnYbpMWq4fM3dMcJbEcYqVwYv80toc2WIOd5fE_9kdtWVU5oos7unMtcR-orQKCvDxBJBQTjkWF3-K6-nHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گابریل مارتینلی هم ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/Futball180TV/102237" target="_blank">📅 13:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102236">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxZ50GBxrOAub7attGb8wiUBPIyDX91D1cZaqW_JolU1kzQmvN1mtIyDNExCkK2IA38Fb7uBJvxfObmtONIYMLKyW42S91m4lM28WYTOK3obeaCz1p9oZBfuCfF6ekdWElC9pIUomZcnxcRyRxmv62ViPYBaT7bFA83rxuQ2CzvNYiOOGJveY1Ad9SwFOyr4cWkp1XPYz9jZ-9lyeZgTtN2v15O5pXSR8LMM_zzPHdrdWZ1E8KKwo07THTfRGnTGwlMtYXxIVwwqae0-iNufTYJCShRYHdJFoKGd0iWdNur4HJ1ZPLbqbDM2UM_5DxWaSRs27_QfMsKNrDlIujXx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚽️
#فوووووری
🔺
اینفانتینو به فدراسیون‌های فوتبال اعلام کرده است که در صورت موافقت آن‌ها با فروش سهام جام جهانی، هر فدراسیون 40 میلیون دلار دریافت خواهد کرد.
🔺
در صورتی که فروش سهام رد شود، هر فدراسیون 10 میلیون دلار دریافت خواهد کرد. یکی از منابع گفت که…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/Futball180TV/102236" target="_blank">📅 13:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102235">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjW4lfxM42BZoaVZ_fhqfxEn1vI9wfgtoRxX_Z82xKiCQhXa8v6IK4ObG_FdWmeJroymw_WbMZ_o1lfWNyfNMV4QGDoZde2zwNPgJtJZEo_4rp6AkjeNb81jpTYityMiBT4YML3uhrcnBF3hYwLHYzgZjKKEIcAhjrviS678JmqvrvmY1LXloenVtTDJzT5SYIwGJhKJYxkBuU7lg4VKP3MRvVO_Mjma0n0iZGeYkAG74poCUoVZYWOM6hHvwL6jetBMsBi5KfxPIT7uqgJZprYIJn18te1M_c1w-4e3x6JDKuo5w-FK7da9PJ8asUwUS4b0T2Rb-lor0rJ0FoA_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
موندو: باشگاه تاتنهام انگلیس رویای جذب کونده مدافع بارسلونا رو داره اما کاتالان‌ها فقط با پیشنهاد بالای ۵۰ میلیون یورو امکان فروش این بازیکن رو بررسی می‌کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/Futball180TV/102235" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102234">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjImJ9oNJ2K0_YnAnOBEP5Fgz2IL8RVE8OiQ2Ixox0VFxwy64i6XF7Ih1SxF1g4jVbcbnK-x1O1HdRazEE4dUvvwWRT-zEpjwgOVO9sj0DwnyQqEUh5VEcx3kJBYI9lx2rUJqFUGwhGJzJRdqGP60z8RpCgvbwMg55gmNB2RbkM2q5iSTH7hHXFm1zQL0qHaUAMnlzS5NjD2x10oT-hLCwF-JjP6VkUMbAcVkNIJMRFGoSFPeUiVEeVGYTWY_cLzKYAirke436rUuIA1MzTXwMaEz_nkOjXibpgi-YdraFgjvRrWZPs65P5lyoN9TvJvORluV839rPMLVVG_nGpvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری از اسکای اسپورت:
🔺
🇪🇺
یوفا به کشورهای عضو این اتحادیه در اروپا اعلام آماده‌باش کرده که اگر اینفانتینو بخواهد جام‌جهانی را به سرمایه‌گذاران خصوصی بفروشد، از حضور در دوره‌های آتی این‌رقابت‌ها انصراف دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/102234" target="_blank">📅 13:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102233">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=bBJrik2f2REihgWNZ-eYxaIk2VpmkUrnWjrLKxW8pQRaxNmtbj8C97k8-6HeLY0v6VNnfC-YK87v8SO8qd3dGN8yuiSQTQEI8uuG-6HVxrkDUq5xhay4Iy_oVnSQXkjfCVoUPL0pJjNaEDzR8Si4smM8hJa5hbi1KceB3MsE3v6P7SYkCqtYWhygIWfCITYuklsssQ16Elc5yW1rQXjePiqWtHN6JeKxYe1PQmCXXERmIAawRjBrzn7qmRUfgLMBNYONPDiTe9rQfrXgP0KjaHWzi3LPKIF75Ap4dj0bQ4U_mhezD7_gBbFBaRQ6iwlLeLEXRzd1SmuqzZYuSxLUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=bBJrik2f2REihgWNZ-eYxaIk2VpmkUrnWjrLKxW8pQRaxNmtbj8C97k8-6HeLY0v6VNnfC-YK87v8SO8qd3dGN8yuiSQTQEI8uuG-6HVxrkDUq5xhay4Iy_oVnSQXkjfCVoUPL0pJjNaEDzR8Si4smM8hJa5hbi1KceB3MsE3v6P7SYkCqtYWhygIWfCITYuklsssQ16Elc5yW1rQXjePiqWtHN6JeKxYe1PQmCXXERmIAawRjBrzn7qmRUfgLMBNYONPDiTe9rQfrXgP0KjaHWzi3LPKIF75Ap4dj0bQ4U_mhezD7_gBbFBaRQ6iwlLeLEXRzd1SmuqzZYuSxLUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
دوران prime مردم ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/102233" target="_blank">📅 13:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102232">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=mG7bekTQdV1J8VVQJxfNDn9BvztFR-nUK51sME0TAYyOW2E5vnewdFMHJbXA_va173HgATcWJB4OQymV6tl4as0k5QFu1zTWKTbFDzAcShSWFPaXSMJcgJRPokl6VHm8g8zOK9LpKx6m635TdyHq7mUFOYjC9DmtaT6WoA_eTXVxp7JojW5rIii2oSCWybfjDCzEJTv8SssFaTlFYIptgGb_C9gCs-VqAp9qLzO3_aYVYXJoDf4xuKPYCqnxPGiULho7vcJb3hvJq5cub9fZ3FL56iuzPSPAGDDwqhdnDDch9UnL9G-el2m_tosch6v6e7l9Rz6s0tNH3j-jlo84eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=mG7bekTQdV1J8VVQJxfNDn9BvztFR-nUK51sME0TAYyOW2E5vnewdFMHJbXA_va173HgATcWJB4OQymV6tl4as0k5QFu1zTWKTbFDzAcShSWFPaXSMJcgJRPokl6VHm8g8zOK9LpKx6m635TdyHq7mUFOYjC9DmtaT6WoA_eTXVxp7JojW5rIii2oSCWybfjDCzEJTv8SssFaTlFYIptgGb_C9gCs-VqAp9qLzO3_aYVYXJoDf4xuKPYCqnxPGiULho7vcJb3hvJq5cub9fZ3FL56iuzPSPAGDDwqhdnDDch9UnL9G-el2m_tosch6v6e7l9Rz6s0tNH3j-jlo84eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دنی آلوز به روایت عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102232" target="_blank">📅 12:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102231">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=ehx72lYF1CagT_j_wpwEWhl0o3AWrZLqHGQnhMVk0sYOS0O4HYxMAl7n0QDhLkQBKP3Sy3QYQqUPhK0Z6Oql62O4nwYj2b3rC2y8KqUewyt5pme2YHxSBpL0ylUiGzez8XzbKsJqmu3A4Ag_7ns59UWEQfhsx56pPFN9IfrWksEZJdXZFmxKvdbZPSo1mrY31jSNd-ZdrseABIHvQvTbaW-73U367G_I58T3PSR3ro-66DNdnk37faGfXTJk9eHYu5B00wHnGl6Q-9JOmjjNhLduJMOsIh2CFo-uebYJFFEnWgWgNUpwzZVFq3--tH5jgnaOFl4XkMG3Ysz-W1_cgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=ehx72lYF1CagT_j_wpwEWhl0o3AWrZLqHGQnhMVk0sYOS0O4HYxMAl7n0QDhLkQBKP3Sy3QYQqUPhK0Z6Oql62O4nwYj2b3rC2y8KqUewyt5pme2YHxSBpL0ylUiGzez8XzbKsJqmu3A4Ag_7ns59UWEQfhsx56pPFN9IfrWksEZJdXZFmxKvdbZPSo1mrY31jSNd-ZdrseABIHvQvTbaW-73U367G_I58T3PSR3ro-66DNdnk37faGfXTJk9eHYu5B00wHnGl6Q-9JOmjjNhLduJMOsIh2CFo-uebYJFFEnWgWgNUpwzZVFq3--tH5jgnaOFl4XkMG3Ysz-W1_cgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانسور کردن در صداوسیما این‌شکلیه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102231" target="_blank">📅 12:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102230">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B35z1mEqM5rIRtsJ9dPhEu_0ARAEAdZHYHJDgnTvFLZRvCvXVs90tNvqPGYr6GqVv-OWeFXOnIdGJrJNqHeNkzb25YVE4NOtBvVNpe1jBsVEQQAp5u6ZR27WcN94--wZO5I9cAqpiEvHyncrvUbn3gdeY3rUPGMcEskX0Lebi5AZQuDpDdlefB0-WtXh_Mu_d3IoI52HirTmo2g26fo3zd9lQ_try9B3ZXYevCevvAjbiBfqRqX5DgDkQt_bSOwj4mhpEA1sxGHRHUYkwU-AJC5wIWFUph_vXGQ9LZmPXpSsCs-4X2WCCCHg2P7eVOWF66U3DHjx3i9HWT3CBeW5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی با مالکیت تادبولی تصمیم‌گرفته که برای چهارمین‌فصل متوالی نام هیچ اسپانسری روی پیراهنش قرار نده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102230" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102229">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102229" target="_blank">📅 11:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102226">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3hcuTbRMmsF6Q3gm2I2pg_ut_Raxm2L9yfmNWHVhTeWY4nixLmHjtVTep-rD0jfufyOtMfUMq0Pq2v_f-dPmhloNI_Zqyxz3j9NxWkBy3c5d-p_tZ1Z3cgizhp5qqlRdhodyOcxLejj8GMMpGy0X1NXN3aQsQXBS3fsAMtgkAy6uSnw-p1erXnFZPbzA0__XXRQbC1oKsXf_6ilSnLJTEnAHTCCgpYsK8fznCJmwg6oAUj4ODgBosH02aKBG8RKjgEHagFVbeQ-_NBSoG6YNwl0D-oFbwdKbCDlEuhtpj4-L8cMro72LjWinA5xGXx5XBbdpXMdEuknSDdrWcse8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rris8FS2PfTbKn94LxJOsTE4LL95mTaMfSkZn0fhvNe7wnArSJV5vC3PNaR4-NS-bCQim4fyFBCgWjEallKUjfEm5mIUoeRnbhNEB9re_aHXfyS-pgTxuMexHMX-dAGLOWb3-ck0DYEXdDWjNkBxHBVy9VvKZqZHoUFeVeqHE0fNo3GOw-QkmLapo-zZv6MBrBxXvuYJcy6SyWAqT8yU9KtUV2fqUBVNTccwRDY3uIxTbySpD5I1nosZmy79D1Nb4mClKn1Uvj3sVpXBjrp6WWLa8pZlqhdMRjbz2VXmty0f1f5S7ArZr8t7DJHNdR8Y-WoXwXgTU2vQurRD7sV4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6yojmItXhwqmN0m33gpVsbPPGc6P0oHOidUUikubgYUV03fqXzxIbfCogxJhUaxzWMG-1KDNvDLKSnTzVAbFVoxykKhaCrRFEHTm8o91-9AXhyxKqCChKSEuULFK4OWP7ma8cWatpZWcwisxjESzKVGcryXwtlB3Hp-0QULYkVQdm-QbCq5KZ81s15HgsH1Dg5Wl_TbHD-9xt9EUh55y5yNgql7iKe6vQyRG2h9MDlxe6DJHVajbgqmi9h6LHlrZNqxM8DMjGCoOZ9OvrxW5W33sCMEwsXzksQbtKTehz-K4k2SnCVdpvRxsqXGHWnXlOBqIZK0EZLpxaBHmwlP6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⁉️
وضعیت سرمربیان تیم‌های حاضر در جام‌جهانی بعد از پایان مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102226" target="_blank">📅 11:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102225">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if7OArxvbxdfyf09eq-zoCgCpPfQTtIlRlqHtesszyQxSKEDJZMxv6_muof-40UQmhAUUlC3rFu3y13hQPN8xqFSgh24h03jGpsMPRtd-auhtbKybQ_96n5hhzbmLPYJ214VB0l8e292xf5kY3x52qd6Y0UFQ9Yx8lRgmE1oOzwMS5HtpytpT6ph3qR-_d62vVM3rN6caevaEBAph4ALf6_kRgppCLv9_zfPsJOfSfcJPRaDWekxiFJs72EHjANj2_aOaWP4PPljBkIg7Et3bg7QHEvs05WKI5bzeB84w8bhJUrsDjX3V4Kqm8GhCY1YyF5aeDYhIre3UYsG_ozaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
▶️
رونالدو داره یه سریال به اسم "Day 1s" درباره پشت‌پرده زندگی و کار ایجنت‌های فوتبال می‌سازه.
غیر از خود رونالدو، چهره‌های معروفی مثل تیری آنری، دیمین لوئیس و یه رپر به اسم دیو تو این سریال بازی می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102225" target="_blank">📅 11:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102224">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s24POu1p364Fld25Gkpv31nag6jbOf5mA3wAktmghrf-XZcbF0vtkFUP2WUMcZkKhgEN3oUVEbbkboWw1ivOwrgrGB3R0EAHTSRaFJ-EayIalkq5khW83XmWnRX9lb0pnLZ1rDwwy6SYQ5rR8pDpUieNi5EA9Tb--eaE0fvS2gr4UuBCNBLngPu0kRjiBHmnyRWmA1KFDGsTpF0oY8DGTB-pZF8ZIdpuaGeZmoysApjES-bLPtScsrC6WeArJNc9K5iggC_x1BUYilglDqkGLbHfT0cixxb27jR3K29Pa2u-j98uz0kavQBp00X26-aFMwHB8bTGZO_-E1vYcWriNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی فصل‌آینده لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102224" target="_blank">📅 11:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102223">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbgR0yK_UQq1pkMwkp2xltZUhOZ-3tY13-4gQbRWpfOxCDfnPVqFRXjr7Nb2hyqwCHJURT1QQDj0S5BRTa6Ue77lYKy6y-VNcWOtESgqmlI9gA6vjfLszc7oRn9mBGALKpQuPrnT1F_r18-aA93TJ1QtvK1d9FtopFcL5yCZAIZAIbVr8kwe9lhw6lRNqR2SF-n-gx33HwZ4OLBA0Vk2DofJVSnl0mOOKXiaENk0uSXobAc331mBzmz8K-8fiIMZ61_g7wMsgxV2hhPvxgp8epq51kkEl3cW42xLhriIjKKkGKZqGyiJ04yeXbaGmYbUFSy-NbbwQvoPtjX2MnjNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102223" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102222">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEdl9lTkuG0F0OMpka0GxT0O8KRRz_XvPoPb6pX84wy1ZzuQ3JaelnGC3MjDnZlcRV5mcATLAhhfGmBVVNsZzosv9XjTb1WRoglpTuJhRgp_-lhxR_QEe7Dqo3Ldlyiye3DLJ4IVRYJqp28529s9btZtFXQmIeXE6YbQ5ydUVsMa-6wBQf_rdpuZuhkSZWntwOmXrd-vQd99vifIa2mmC7R9k83CH70llXCJWON16EWelQushbEbxClQybyTBHNLZTikN7AsuzAGlS_xRzdfa2TWMkxTQ5FZQ8G_0Jwr67VMmDZ-EUGdBvKx7kZSgdUxpkcMLAR-IfcL2--HNJY2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
💥
تعطیلات امباپه در کنار اکسپوزیتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102222" target="_blank">📅 10:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102221">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrQmflOXsXYL7rORrqGkv435A4QCEhey6U2q08qIzrcAcis7tRHIBdEyiHXOy8F8ONVFhDVmoxKxtIXNdDhkHXwQt5Smj1PLuXLm6ko-4K4eUsbNBF_4xFtd6jfrKcXbVfQ-2O14VBd0oFEdGZf4EkjkDwn_nPx-y8tGqyVRVCXL44Fj7giQ6bMuk9n7qLKko2o8f7T8l8i6FPCNX9zAoHc2V16qN-uHH9s8dzGO5XaiJdRtSaCvI52umSg0kXAuC3i7dqoS2l3E2egtznQNmy0dZJBEWR5f-qgDmDDjlN6GYQsArocFK1fgeNH_NeEVtpLj7kHKIPbP4NCKWqCgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
6 سال پیش، هالند 20 ساله تنها 71 گل به ثمر رسانده بود، در حالی که در مقابل نیمار افسانه‌ای قرار می‌گرفت که در آن زمان 375 گل زده بود. این اختلاف 304 گلی، مانند یک پرتگاه غیرقابل عبور به نظر می‌رسید.
🤦
🗓
6 سال بعد، هالند 290 گل دیگر به ثمر رسانده و به رکورد 361 گل رسیده است. در همین مدت، نیمار تنها 84 گل دیگر به مجموع خود اضافه کرده است.
😳
یک ماشین گلزنی که به طور متوسط بیش از 48 گل در سال به ثمر می‌رساند، در مقایسه با یک نابغه که به نظر می‌رسد سرعت گلزنی‌اش به طور قابل توجهی کاهش یافته و دقیقاً 14 گل در سال است...
😭
و اکنون، در سن 26 سالگی، هالند کمتر از 100 گل با مجموع گل‌های دوران حرفه‌ای نیمار جونیور فاصله دارد – یکی از نمادهای بزرگ فوتبال.
🤯
واقعاً باورنکردنی است که هالند با چه سرعتی و ثبات فوق‌العاده‌ای گل به ثمر می‌رساند.
⚠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102221" target="_blank">📅 10:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102220">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=qUvjwjW6rhviE7NQ_jGpYCFHD2CeFbVa-avLc2hgN9La-A5ZNV7y2WiMxppZ1LGcVDgLcPKzk2XgEOIbSjdIu9igvuWjk9cBn3Pbgy58Y1laTuOV7fFQtDXFB5V7vW2Wl-7gIOgbUkOu0NUW5T9KAs8V97niabiN33WkeRghqQzRZ3gBRgmN9ZpvtFAvtrSrP2UcDQi9Gll3KE-F2lB4pVX0snPbfpI5_9kFPeBCFsoFlSE1Uzu4-L8mDV7xlXZkSYKnkEiFUR9yJhKdAvam5R_C_aMUhZ-1NJc7pfEM0xsoYhW2XjHvV0HKlAWXmlIyqlHT-UpAQ5YbWuXQjp3oqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=qUvjwjW6rhviE7NQ_jGpYCFHD2CeFbVa-avLc2hgN9La-A5ZNV7y2WiMxppZ1LGcVDgLcPKzk2XgEOIbSjdIu9igvuWjk9cBn3Pbgy58Y1laTuOV7fFQtDXFB5V7vW2Wl-7gIOgbUkOu0NUW5T9KAs8V97niabiN33WkeRghqQzRZ3gBRgmN9ZpvtFAvtrSrP2UcDQi9Gll3KE-F2lB4pVX0snPbfpI5_9kFPeBCFsoFlSE1Uzu4-L8mDV7xlXZkSYKnkEiFUR9yJhKdAvam5R_C_aMUhZ-1NJc7pfEM0xsoYhW2XjHvV0HKlAWXmlIyqlHT-UpAQ5YbWuXQjp3oqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مروری بر برخی گل‌های اسطوره کون برای سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102220" target="_blank">📅 10:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102219">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=a3iS1LQ-ASaZEiytHQB4G6o_LKjoMK7yqkPNIccJFSAGKf36rbWsf_zJVitEusNLpxXuXn1xwVMqgUTCd6Djuki4FwBXT8C44u_djAgf4p7g3TmIN748CzWeeA391RRQF4R4ywmbJ37zCE75zc82nJ86evm6m3cSpUWvyTZoSBYyIucoBjIjfr2iUTOCPVOiDU8NzmEneKi9o8A59uR2YKaBHZgxVAsA99Xb47lLE5jY3eSZAloZf2PV9Se_N4oSTiqXQxDN3H_pRr32O_bJhrC2msBZ_9exbPJzsavaylZUL47tfCmjBrNsyg17hMMedoPg8R5vcj6ufiycIBSyag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=a3iS1LQ-ASaZEiytHQB4G6o_LKjoMK7yqkPNIccJFSAGKf36rbWsf_zJVitEusNLpxXuXn1xwVMqgUTCd6Djuki4FwBXT8C44u_djAgf4p7g3TmIN748CzWeeA391RRQF4R4ywmbJ37zCE75zc82nJ86evm6m3cSpUWvyTZoSBYyIucoBjIjfr2iUTOCPVOiDU8NzmEneKi9o8A59uR2YKaBHZgxVAsA99Xb47lLE5jY3eSZAloZf2PV9Se_N4oSTiqXQxDN3H_pRr32O_bJhrC2msBZ_9exbPJzsavaylZUL47tfCmjBrNsyg17hMMedoPg8R5vcj6ufiycIBSyag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا همه رو شکست داد جز ...
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102219" target="_blank">📅 10:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102218">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaW3RtUSN1vVrn-OXQkSxHYCRyGhw06O1cmjhc_4xID77rijl6j-SDOa5kW1Iqx7hBRrO3FxSUQO0jBwUkR1Mu-tV0xfgxpIGFDVTKfGQI4Q11GCKcxii_SAeYnFSZlY8dRmStTLXOrg7ge-5SzcPbSEfC8z9J7DrfU5JRu9Lb2-2Hj6CxCU3jmhGaZ9wnMfsvFG-BLF4PoAhAESxBJlc3bDZnQtZEKaYj_mnKmSwQ0mUQB3ALrb0IiF_inT0peFtsSvyFlU13Bc79GCoTT7isYcWG4jy2sm9zHf7WBjsBq4JqDGFgJpIFC1DCfsJPbJzzJ_gJyPXAdBnTh7oCJrMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✍️
فابریزیو رومانو:
بایرن مونیخ در حال بررسی تمدید قرارداد با هری کین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/102218" target="_blank">📅 09:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102217">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=KAjZwB6Vp1mOhWHR-AxwLey0LSgM2AM5kW-SyqWGA8AI81o_9HIJ6soEwM8JFLFqgZCdl614VbM2Zy_ubo9BbklWAny0k1Dvw85YGzUtS_S9qCrkO1fSVvDjlr2VBDZy5_SrrfgURARLREboKdxNEhjCJ5Rs4Jr20CBVLLWy3BHmtCwvSSVEHqfIvLpIUHwcFGnD8EBViWq5a7P5X2Jhs84uHv-5hrfchWL6P1nqBmH5-kTHsYwaBEroIJxeycZJ15jLukXHVno9yVo0mQc47Ooh3IaoogXLy9rAU1A7k0iS1nrjJJ78bwH_5cNmYCw9KsJ1MTXgf-EnAY_rjFSx7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=KAjZwB6Vp1mOhWHR-AxwLey0LSgM2AM5kW-SyqWGA8AI81o_9HIJ6soEwM8JFLFqgZCdl614VbM2Zy_ubo9BbklWAny0k1Dvw85YGzUtS_S9qCrkO1fSVvDjlr2VBDZy5_SrrfgURARLREboKdxNEhjCJ5Rs4Jr20CBVLLWy3BHmtCwvSSVEHqfIvLpIUHwcFGnD8EBViWq5a7P5X2Jhs84uHv-5hrfchWL6P1nqBmH5-kTHsYwaBEroIJxeycZJ15jLukXHVno9yVo0mQc47Ooh3IaoogXLy9rAU1A7k0iS1nrjJJ78bwH_5cNmYCw9KsJ1MTXgf-EnAY_rjFSx7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
کاماوینگا بخاطر همین سطح عقلیشه که مورینیو میخواد دکمشو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102217" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102216">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA8qm_YBVhiJDYwwt6RnLaAFkZSkjyPlQq3A_OAxRCCEJAskILLRwxVrH_wPkVg1d6JMzdw7mY4-5iO3qZmIqpfgOcMco9LaZ7ZY6DURB-gE4nEXu-muNeOTO695uWoVsw04KGy4kb7f0CuPlLkbqQTlLIyeN80V-_Gq1uooNpamMcBDhU69nNEVoRa6zIDWyRByJb4NEywwIbsECu8K0NYCjQrwpB9ccszyTfahnY-X9xb_yFKd3SpP0yY0uYP758c75QWD_gx8f8UjMaJsnuJ5bvPqxO5lk7jTig5DhFmfk7EN9RaaM--Sdsqe5yUQWkGqlaHabSJPIoRmNa0n2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف رفته زیر پست ویتینیا کامنت گذاشته که ناموسا تو جام‌جهانی 2030 به رونالدو جونیور (پسر رونالدو) پاس بده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102216" target="_blank">📅 09:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102215">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=be4_0hKImKx8PahTfY47oeeBSoZ8C5CjIiL7AWEr7c5yKChpzgMXXQp8GNNMYmLPsU__AKw3rhSd8R4c2PChOGN75hReqGQM0WIbIowOdBsx0_jdGGRrmb5dFNBYWeIPec0hFzSfLOqLBPPEuW_1ePnTlEEaQeuoBpgFZBswXABV1R3DDoreCDVqRgLIDCWo351on0Mc3bGPh-Sqri-xUhkyHuQFolHwdmDx1tIK4L1RVrpCQNfBAzMxcGuDtrnP9z4D3M5vdSPfY2wvFy_D4EwfQrpsrXhn8INk_YUM1KHSixv40GeGBBklprGsT-bGov048V13tk3iaip74YX_Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=be4_0hKImKx8PahTfY47oeeBSoZ8C5CjIiL7AWEr7c5yKChpzgMXXQp8GNNMYmLPsU__AKw3rhSd8R4c2PChOGN75hReqGQM0WIbIowOdBsx0_jdGGRrmb5dFNBYWeIPec0hFzSfLOqLBPPEuW_1ePnTlEEaQeuoBpgFZBswXABV1R3DDoreCDVqRgLIDCWo351on0Mc3bGPh-Sqri-xUhkyHuQFolHwdmDx1tIK4L1RVrpCQNfBAzMxcGuDtrnP9z4D3M5vdSPfY2wvFy_D4EwfQrpsrXhn8INk_YUM1KHSixv40GeGBBklprGsT-bGov048V13tk3iaip74YX_Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
جانفداهای عزیز درحال حرکت به سمت مرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102215" target="_blank">📅 09:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102214">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=b9flY244_rHRnlspL_H-uuRCblrYLKT4Qjt3MRA8D-xQjXN0HXE1Y6YD5xO9e5tRvdtRiK7ZhFnXJe49GwdJK9ZsI_HyIU-wWsJJClUQHSFjHOgXUZ6YaGV8g689wjFosr8LOkLMaKjnW6KVmeD6Nw6-lI2PNeqnwOFnsDdGFb-XxseSCsaXnR-QMusKuZLxaoQFuK1W5ii1Ait-VJ56IgXn7YVnaxtSAITM738YLdHMuNOfOQR-X1EsiJ4jTOO58kG4XjRUq54lYxSqCyKjKQPCsWR2XMsx6XDir_04JleDkjCx-OW0veNTRTQ7l4uC-pXJBdDyTe_fwLwRz2NFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=b9flY244_rHRnlspL_H-uuRCblrYLKT4Qjt3MRA8D-xQjXN0HXE1Y6YD5xO9e5tRvdtRiK7ZhFnXJe49GwdJK9ZsI_HyIU-wWsJJClUQHSFjHOgXUZ6YaGV8g689wjFosr8LOkLMaKjnW6KVmeD6Nw6-lI2PNeqnwOFnsDdGFb-XxseSCsaXnR-QMusKuZLxaoQFuK1W5ii1Ait-VJ56IgXn7YVnaxtSAITM738YLdHMuNOfOQR-X1EsiJ4jTOO58kG4XjRUq54lYxSqCyKjKQPCsWR2XMsx6XDir_04JleDkjCx-OW0veNTRTQ7l4uC-pXJBdDyTe_fwLwRz2NFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
پپ گواردیولا: "وقتی به بارسلونا رفتم، یه نظرسنجی گذاشته بودن که حدود ۸۶ یا ۸۷ درصد اصلاً منو نمیخواستن! نه هوادارا، نه رسانه‌ها... چون اون موقع از دسته چهارم اومده بودم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102214" target="_blank">📅 09:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ6cRKmXTlO-40eaYo3LnUu4SqHnuSG_4htMjmMM0jl5YOhEVDJ3Aq8C3PsKYELmMyCguPslhWudml4kUQU0Qfg13XnQJdU2u3xY-1paIvFQx9rEQBYr8l74LB32kfLxp8VY6ULYL0LPdy2HMkzAp-XYSV6PTAsIPJcf1cmtsvKl4swqEHHoliWaxq1djX0RIbNBUXNC3UhGK7GYXsd5JcSgcs8tOqJ9AGokdyKKhFGOEnQG-EL73Wt93UDP2JxsAmBtg4zT5G4wCspXSrZpZlbiSmJtUxZtGdcMTmFm_HF7EgDZSB3z7vDuUbXqzIg6UteHMAg3KIlcrfuw6N0fJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی‌ولبک از برایتون به چلسی
Here We Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102213" target="_blank">📅 08:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102210">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-Gaghc-axHIFpW-T5kw5p2grAlnafSPQ4BQRcRa3HWhEj7-eTCDRstHZPHVBSgE8FuivToSA1g_9VojXnoy8oezZOBwE0Xw6xv7JkC7OVNXfQlY2XUxUapt6-okYcBR5L96Nv9KCyplAI4Ifp2RUgaLQf041cjUYuCVz6uyNc4Y5C31DzXEu6a-IM_aXjsAYu52C6bsIeE6WF62f9BpTzvcZeYcefOFmyNeX47xMFtAWhAzw5b4cMtq2Mg0oBhhElMpJdFcWOVSlwt34UwX5OSakUDZFNZ7xlxz4MQKGY-lKE2lSIEh8zGoRQEpe9w-33bizjDs1tEEsGQ_TW5opg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJZ7D4OwIeHmvyvkm8rLI6jgY0pn-q8Q8DST3rSHt-9CG-5yrW1C-UpSzB57cOYiG88olJbygA-Rhk3DZaVYScJOJXCHc22N4i8K3SNHXDmsMiC7q267v9FHMwZmkxo9lqOTZBiXLF2UcICyAXJkLRHFeLw3S_QQKnBdA86LxU5D4Ui35w36U4_zbVKEmUeRJr24adqGwEvfdP6MQYUhrSVBTAfIR3LM9xEcCzwNFEKIgJaXQ2K2k-D_yDdfsOKDMXHWSwntq5kD9pCmlRqyrZEctedUybUAoeWmihHNDooO5PqFqh7k0m1ruvytZIR54I1dCVgZKUMUSznk686Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oP1PRC8o6UzS-GWHGUE2t66YLCoU7lHA1Pi08TMl86cwVyg0L3BkakogBDLJo1OJ_9e1kZe1d-ksfLQdXsqhaITuBsi3ALlhVBj7zah-Xjn2fIjpR1GHLsN21YtG_R4MJcDBhBBTxPEAznU7g9W-95dbKyaL1k8pzEaxFJcGAdEo-hE_QLaZZwpgz8fGzQgib9FTv4m0s7YnREArkGBDq53BZBApWtsfA1dBOy5DkD0F2keX4-_gPFYhMTeF-8x6skOKbKGkaWx362j0i1OV89oibzHeExaH2Ct1n_pvOwQqGXBlC_iQWLpjNdULd5B1pXEevL_h8_HPqTY1dvrgng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
- کیت دوم فصل 2026/2027 باشگاه لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102210" target="_blank">📅 03:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102209">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPpWjYqlfN886R4_0zc4R6xWBzgATAlgQXBxi4p7d1KuUZQoqXTBQiULXfbSq_Jcklq4ZBJtN6tHlqibk60Gosow3ppiz5hOLhL71owc8xFREollN0DTsjbBF1yu3UWedTW7O3W8Vyi05ghncg-D2J-4Et7atBCrAw2CWoqOf154Gs23UtChRbLpkwino7XsXB1rHEXrV4Ba1Rl3NWk1EQ1KX3Y8bexRDuPJ6r4O4ESOXdV9nkjkJhy8x3104FevKATurtIADa_ygUR8EMK-GshENrR4hm4-7XAVi2b0yF26xKIGVBQd0IHfuPudPH7YHm041loKzqfDkrkxbo_CbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ سنتکام: سپاه قصد انجام عملیات غافلگیرکننده رو داشت که همه‌ی موشک هاشون رو رهگیری کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102209" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102208">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb_woRtMxNeO8IzlC79lqc2nQBCTm5ugo-YaExyuy_sh6FrAeR3HfqOW1NbwmNng1JsqG74TsVojKai639_KNb8XMNtk67MoKM8GXeF9BsgCr9r2J_nFvTlpoplRAo7-ILpus5twfar1pqfvRua-ZDL463pT46SuayXPBk1fFQLeHxJC8Sig9NixfC3FJt2q_Pa36iqGu813XRIGhTPDmdT6ck4d98cTA6Nv8z1IdfxKlzvuqfKgkG-KX1idKpzMbxjSkd7lEuNLtz0qEEkiUuBqYEhY6Li3SQtFXgRCB4UZf3MpOwmmqsu8x1TTdbGG1QUHm9rEPge9yMKlIDbrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: هواداران رئال‌مادرید آروم باشید. روند تکمیل قرارداد دیومانده با سرعت داره جلو میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102208" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102207">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=gY8nydnIp8kRvbyovh3HdfcJ03R00e7OoYYATAMFTFThyRgn5iMojusH0QVViu99v1n6MASFft84zBM7ASkLIdxUTAIiLL6gPsol7AYoRi_LYWEje4LcAsScBVOxjHaB20cWPk791POi4HplEfhPTmfEYMDVoTcbV3pA4BAWSXvLpZ9wZ75aCYBZArVt3dVaMyxeyDoxrV5_GxfPglwtzCFwZcscT4u7MkGFGVhBkyOBQCfWkvgK1HTn2_Db-YSj78NuV2NhYSwU_08ohh9TjpC1PS5Swehw70sS9tHXNsZv7ifdLk5POEUP9FSUm6WPTFI6Opz_cvzzDeZWWNQg_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=gY8nydnIp8kRvbyovh3HdfcJ03R00e7OoYYATAMFTFThyRgn5iMojusH0QVViu99v1n6MASFft84zBM7ASkLIdxUTAIiLL6gPsol7AYoRi_LYWEje4LcAsScBVOxjHaB20cWPk791POi4HplEfhPTmfEYMDVoTcbV3pA4BAWSXvLpZ9wZ75aCYBZArVt3dVaMyxeyDoxrV5_GxfPglwtzCFwZcscT4u7MkGFGVhBkyOBQCfWkvgK1HTn2_Db-YSj78NuV2NhYSwU_08ohh9TjpC1PS5Swehw70sS9tHXNsZv7ifdLk5POEUP9FSUm6WPTFI6Opz_cvzzDeZWWNQg_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
انفجارهای شدید در اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102207" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102206">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebFcqyT1HBpsUCPWPVxfaEYipPB_1jollD5myaXnWEj_CdWxS8YgCHjRXQO7C9Hiyn69fYpo4Wr8nme97rFBYikR2cw3unags0pJn84PBtge5vCoQ-OnWZsuyj17nmWxg5oB5YIz9QSudkCPTyz59koVU2RyVmtGjCMxy4Mx8qMifZ1RKeyaEvulI5zIw9kCdGZapFl8g6nsvTdPJMzzQnfldcIAPswNQ3x4Am_MabLihPR_DMrZX2qGAuHJQgw9Nob7gUbvp8yvxShmzW3Y_lFGEjBSFNI6xmTVsQtZBXpCM6l0DKEu02NOLZKyNdizmglc_k5P66xAVlEWnc4yKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102206" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102205">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYLSIlkTW7x8G-q_MFkvIQQ5L_VZ7SYCukWCuLSG639wihnzS3egJ6EzNGntk6JO2o5-BRJ9BZPXE-AFMsZwXDHEVnS5X1fjsk52BL_lWKFVlHH-QliFW43R5_qH0KP8UCuxK9gphrzhRTC19knoZUsZE3yNh6lapN4jMRVDDYA_RoLDjHD-l4JoGj-KpQP0SoBYR4BygshbLjGWBZSUK8wqcYGLa4vspaKPDyA5cyuKv1P7xMKj1a_wYzGAS1oRFRa973RQTgZkAKo4agMCqPgFS9eZ0JgBZbeTlpDMcCaSdQob03Stis5Hh_Wwsm9j3VF5W3ZYumbT3Jmy_DjbFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102205" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102204">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnOtMRuUazlIND2Nfe1n8Ik519f475isE_8wqJuk3feolsYCpmFiAPMAq7gzlC2vKbpfDhQVtKIFkv31mS_KN1xGnoeJBWB14qqXC94DSJ20Hmc_gW2hE4eKS7kfcwAzCppBHB_ILbL4UUkVJ5EkO1BUJ2TCuB2sX6eQFCHA_FCjeazNJcYBVSNvnN7wiUiqPcjfXoZpkk6fxIdFsEUyHmtfqpTd6YduUmxVFdvclI3GKey8pIb6B5vLT0eTcz71hG8Lk_wCM6nmS9mzv1XOWRA1tWNoMK9oXPZ9YJK9hbfvJ0S4M68nx3AIS2Qf0DSw7DWuZqYDbqQLDA8xwyIzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🙂
👤
تعطیلات علیرضا فغانی بعد WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102204" target="_blank">📅 01:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102203">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=Yg1Se6m7dHMdiVq2-hOifCeR_SSfz9vU7m6vHOlvBioE-hXj9gq7b4ZqUbb5aMhHXOD_DdnTsikIz7tETZipfn8VCzTTQBe6zbVpi-nD8R1qqw4HHTvg5EqkzH2zgo5b2zGfqO6obluUVokKzBcC1UE4hsTRcrqG3U_Zkj1ti8pyGhy7szyn55h_-r76xdOOL1qBqdNO60ck-GWhqHKdZfMQIPlfnUUNOXLlawFrpwFnhsNZ4H6MbgDgqSgA5U_kkzvjCjuuTCq1ZynPUEEXSvdoWL702Qpw2npJ97DyRmztfSxt1eSE3VnPlGpxJDWFUwh9umF5jbv8tbt7pCe9Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=Yg1Se6m7dHMdiVq2-hOifCeR_SSfz9vU7m6vHOlvBioE-hXj9gq7b4ZqUbb5aMhHXOD_DdnTsikIz7tETZipfn8VCzTTQBe6zbVpi-nD8R1qqw4HHTvg5EqkzH2zgo5b2zGfqO6obluUVokKzBcC1UE4hsTRcrqG3U_Zkj1ti8pyGhy7szyn55h_-r76xdOOL1qBqdNO60ck-GWhqHKdZfMQIPlfnUUNOXLlawFrpwFnhsNZ4H6MbgDgqSgA5U_kkzvjCjuuTCq1ZynPUEEXSvdoWL702Qpw2npJ97DyRmztfSxt1eSE3VnPlGpxJDWFUwh9umF5jbv8tbt7pCe9Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بترسید از خونی که به ناحق ریخته شود
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102203" target="_blank">📅 01:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102202">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsL-b_CktLbfDSH7raj_E-DxZvWQchwTZZgM74xwxM8MF-NrheTburzUO4gLh2xa_APsjOZigI5kwhq6eq143M6S9b09QVT28bwfZbZ990yBUQFopmOhJxNJ8YhJ0uAnqsueCe3xN_Ws7IreJ_5zrEnZvD8yZjOUtUwEwxd8jUAWhAejbSSXLtbGa2pGsKbumsf6rmS_2UGd8WbQELoi3CpG4_mxpOPOEa1DeseSwkiyg60ine1RjdybCFgMlqJjN3JluV_PqmZD4ZsTPyWMRciGyEWkNzt8fOQYsFnKM5IOgXTDyvEV7ki4I3esKOftZVp32eP9KriH8emvyQlaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس جدید بوکایو ساکا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102202" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102201">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102201" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102200">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=dYdyQknXqrHPrdJ-mtILbZ2GIg6bJCzO58oMwIeCPDTl1nT49B4s8gl7XffF0XGGQoK3vYUgMNo-LkPSCypxkOygdiEN77p6yfTEcmFC8IquS-rFMMQWj7AkF4sSggcLeQbc5vz730-Af7kWMYHcko_CdDy1JKT1M3gBHrXofSj7SntH1Qc8Q3ejyPaQNwzPksgwLzS8Tojzai87ljsXl0nbQwUkJhx-CdDkZE3jcrg0cC9axuT7TQ0_6oRURIvqef5D6SfMpdFChTUYsGeRt9ASOP5nkofs0gcYXN417U8FbCGsy-Sq3UXVYSUZPAjJZG6l1ke4TXKsoJf1kOgsTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=dYdyQknXqrHPrdJ-mtILbZ2GIg6bJCzO58oMwIeCPDTl1nT49B4s8gl7XffF0XGGQoK3vYUgMNo-LkPSCypxkOygdiEN77p6yfTEcmFC8IquS-rFMMQWj7AkF4sSggcLeQbc5vz730-Af7kWMYHcko_CdDy1JKT1M3gBHrXofSj7SntH1Qc8Q3ejyPaQNwzPksgwLzS8Tojzai87ljsXl0nbQwUkJhx-CdDkZE3jcrg0cC9axuT7TQ0_6oRURIvqef5D6SfMpdFChTUYsGeRt9ASOP5nkofs0gcYXN417U8FbCGsy-Sq3UXVYSUZPAjJZG6l1ke4TXKsoJf1kOgsTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102200" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102199">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neRFup4ySqbFedhI5h9oyC-IUfKnOG1oSE1OxZ3r16VrqLUdgHU_RND9ItiDBY5MpisaxukWfsrktXsKqoY4coHuHcFd6hev1EC7COqlbgGEfXp6xKfHXQmo69zl5cbYhJBkb4boCTCg_iglKhpoewOFEvHopDjsMLYfD9h6DxqFGr5NgZm65THstxxST_9qTuC8wLfjWxyhEL9-DBk2NzNdk-gaHxxVThz448F5NnsRnqDcmYFA0KESNFqyyi-eH68uJG6jEBJry2BvHKxwil9HiijSubvOgx75Uvnzj9HzvsFwkDyzU_-glVMkSDP4mP27K-t076PXo1LiovXKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
رامون‌آلوارز: آسنسیو به سران رئال گفته تنها در صورتی جدا میشه که تیمی پیدا بشه و معادل حقوق‌فعلی خودش در رئال بهش دستمزد بده وگرنه تا آخر قراردادش قصدی برای جدایی از کهکشانی‌ها نداره
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102199" target="_blank">📅 00:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102198">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcnwMyhcOHi9s5dr3ZTqWTnMhUcP0WM_IARQRDSodWiHwxAHQxT5QoZkVRb_AI5ls5q7vSU8engF1X6wS-4A1PI8IthgLpaGh9DABVpFGJm7auj3lT6cGTRvTTI1-mrpUbZ0vDwW5y_VVDodT657d3o0SdVP2oDz3Z4b7A_wWAbthXda_wB6DWIpCBraYwLGi5Vbb79fnD311ilYB01rlj-PEUTHdgJDtL5aErstYxzpeU-llE032bWNPTo2X1jQ-3fys2A-oW_hFCOkOey3Bje4BhUmmsAncbNuagS4c8IUxJzJgxRoziAfIV2sUaHc-imoxlRB6YtsrwbpQIkZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
😍
دلیل آرامش‌خیال بارسایی‌ها در تمرینات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102198" target="_blank">📅 00:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔵
▶️
ویدیو باشگاه استقلال به مناسب سالگرد دومین قهرمانی آبی‌پوشان در رقابت‌های آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102197" target="_blank">📅 00:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102196">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtQSvjKzxUm-MaTMTOsy3JnfzKKC2EPTKdrtN-CoDB5Go4fO427w9gpWyg_1hjU933m3AqJPQEJNI6vmxsShWu3ti_YuCfmyjuz1WJsYZoHwIB6ghv42qi8kWWViuX_WeYeMZ-IOJtso3G0gntyFKi2H-tZn77GMzhKr8YQ3iuAG7CIIiy0CyiA8GHvAhm7FMz5TyczWZGtDWDkBSLhrplfJsnjE7wyl-Ftilm-XtL4vQEv49Yx4w0kawwJNwOS1H3RfOD-q58KQ-aN0v5sL1H78QpaSLTmUwPisXkJYtLNpR3mXbBD0hegewf6zJYYDlF_0O6XkUWjqcPjLJebvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102196" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102195">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX3QnPgBXY0Lc8ilBAIF0H3f4tJfv-gfDBNcuj-LmZbjx_jayzh7TcgZwkWFxjcVQEHJyeJCvFwO7ZKASvtER6h7acxRnJOHsYGrF3eQd81AQXYWELjSnkd78JIJG_6MCZs-DHi9vQtLDoP8FoAKdQIRsM1IL_IOdu-vNOvTAVOYrd5qIVkMwtsbuwcqJXHkZIOvt23o4z7qIam1iaV4WA3BYVM-K2U_jg69PBNJezk-13G76mO-dx8j1Kv9JQ9mo-UxaPVkUfsuHT5xjmY6HlCt9VWGYnDp4q1WKknUfnthV1Ck11-c91Q6PplAn4VkXPID3UvE1XWcanxYIyyQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد:
نویر پایان فصل از فوتبال خداحافظی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102195" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102194">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIqenKWIzIkAU1pzF6fI_oVenasn314IN7-5vgoOJ9Y7uAwpHBo72iFloVZuXX02qgGnGi8JQ8JzPHLRbQRmSIN1KXRUtJEX-xSUSV9-klupcxbN29Qwle43OFUYRvZANGdhk5eufK-Wd-9t_b_fAyO53QRpMECjr0gxugAR5nK-A8wvSLQQKoAi_ZZgefFjDkwUp6QM3B0rfMYIO53iDnk3Jhny_F-rna3M-JP5oUIjCaND_Ihm5YUhJfcpUdkdF-Sf_cqZZMnD4f3S06mz6Ce6OZZ9EtsbXYaUj9-wTDRKH8qzHrRaJf2Ffc3Dl5O-TxyknSJs4mFJNyTH4Eh7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا یکی جلوی گذر زمانو بگیره
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102194" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102192">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=Pz7ZO2jenldDJRqtZr7I8N8uMAR8m5vw2jSxlcJbAGBy5bUX_mEdaSYg9RvghLlRErhvozXipDgGiGX_hnoqyjbvJZco-CfYFcfthqzs706Jh39BZt-u2SQE2Wlupm-4yRLWI0esCLskdr9zIlU9rc9_AGXZfPL24JozlVZ5jHXKQNjZ-mBS0WXj_FJMa0Qg2rTNdlCp6t4ai1AEjtvWsvarUm4hkf4vd6hKAx193U48ixrHS4MkoP-5bVMBpVmkd3xtqsz-z2bvsAvURLd6qvlTZKrKXApwGD9YJveqoE8Pglm7nStKs1r4cw4muu-5_0lgFgUjkCMUuPa45R3fRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=Pz7ZO2jenldDJRqtZr7I8N8uMAR8m5vw2jSxlcJbAGBy5bUX_mEdaSYg9RvghLlRErhvozXipDgGiGX_hnoqyjbvJZco-CfYFcfthqzs706Jh39BZt-u2SQE2Wlupm-4yRLWI0esCLskdr9zIlU9rc9_AGXZfPL24JozlVZ5jHXKQNjZ-mBS0WXj_FJMa0Qg2rTNdlCp6t4ai1AEjtvWsvarUm4hkf4vd6hKAx193U48ixrHS4MkoP-5bVMBpVmkd3xtqsz-z2bvsAvURLd6qvlTZKrKXApwGD9YJveqoE8Pglm7nStKs1r4cw4muu-5_0lgFgUjkCMUuPa45R3fRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
کافو: وقتی پاتو اومد هیچکس نمی‌تونست تو تمرینات اونو بگیره؛ کالادزه، مالدینی، نستا، هیچکس نمی‌خواست اونو مهار کنه، دیگه ببینید چه سگی بود که می‌تونست به راست بره، به چپ، سر بزنه، با هر دو پا شوت بزنه، سرعتش به طور دیوانه‌واری تغییر میکرد، به سرژینیو گفتم یکی از بزرگ‌ترین مهاجمان تمام دوران‌ها به میلان اومده اما یهو همه چیز عوض شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102192" target="_blank">📅 22:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102191">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6KfjnL6fczr1z8OutQ7Fcyem4UvuzuLpBR9Dqk7ziEamUadjkTuj8APgJyLISLKiRdTSa5wuFQ_kZgUKacTw8C1s6uWis06F6V1Vzvw5DhrGm_4DszucwHhfDTXKdcGDhd-ZlwEyfbXytanEl0P5okLhi2-XmJjDeIrxiGGurYlsFCgkFO3TlIzzScyvtawa_Q06ftw-xgjvLRCdaR7_Ov85L-HRNqnPvYKEKyz0IFkN3VEHAAGWdbcyTaq6JeI4AVJ4Y66RrlSiEtB_GF1zcIFc7LJ2Y-OWDK5I7YgpdsPvBjxEuRtj8metTZth-thLPmT0Unhbv_Lsjyggcv9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستیان دریسن، مدیرعامل باشگاه بایرن مونیخ، درباره اولیسه:
هیچگونه ارتباطی از سوی باشگاه رئال مادرید وجود نداشته است، نه تماس تلفنی، نه نامه، نه فکس و نه ایمیل. بسیار شگفت‌انگیز است که چه چیزهایی منتشر می‌شود، در حالی که خودتان حقیقت را می‌دانید. این واقعاً حیرت‌انگیز است. او هنوز سه سال از قراردادش باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102191" target="_blank">📅 22:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102190">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=p1K4_-zabxe1nJDTmyKo_Nl2IBhlz_V8dWyayjO59LR1hmMBJ8OD6f2op4AYl3eXFHSYTi_kY2aHjX-GDwAmxTUIcC-9s4uzu9xM9qSXJ4rCmS4h-stW3ATE90lPrSvO-5t31pVKjg4VfFUfCqbukRtusoGkkHFYF2dQsIu3dQ9IqQUA7a9ojFYny1R2pYYR16C-ou0BXP88KocdsS-2aF2M0tOIdscYqKY5WZ1Z8ZLIaYHsWdR2CisyGWuS5rkhCz6MRwVupecS0CrLm9Ug63nZk2bKW_hyTpdhv8GA4Sehn84I6X1Hv0mc9SzYOZuJ6ctZaR-JZR_7M6a7qgWSki0qddCwJdVUMJhl9Hw29J5J8zvFL5OGyN0tQHb_rd2Mn_xLuecp_B1oZShaw7-mRGp_M0yMNhvqQoiRPiccAkAXghDOK_A8xuC_jg1Qsj7ob-9gjs87L124PpKoxve6h6q-9W0l4pUNhhW0feB3KPQANL2IbcmjOVKTzzaK88nGWaAlLawC68UYV-F7TcA5gK2RZvaXhnFqvZnZbgNb2Vy0t-0H2WkLTYaaAGRRAQBHBXqB_IPZ-wmzOWIKf9Vc0dqjeYkQ427o3gBd-RoQBq19YiWn3wDLKeBhPEoZ1ByW_lSe5hcDUaPDMA_LSewtjr41mJw5etAjM3mFebYcf30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=p1K4_-zabxe1nJDTmyKo_Nl2IBhlz_V8dWyayjO59LR1hmMBJ8OD6f2op4AYl3eXFHSYTi_kY2aHjX-GDwAmxTUIcC-9s4uzu9xM9qSXJ4rCmS4h-stW3ATE90lPrSvO-5t31pVKjg4VfFUfCqbukRtusoGkkHFYF2dQsIu3dQ9IqQUA7a9ojFYny1R2pYYR16C-ou0BXP88KocdsS-2aF2M0tOIdscYqKY5WZ1Z8ZLIaYHsWdR2CisyGWuS5rkhCz6MRwVupecS0CrLm9Ug63nZk2bKW_hyTpdhv8GA4Sehn84I6X1Hv0mc9SzYOZuJ6ctZaR-JZR_7M6a7qgWSki0qddCwJdVUMJhl9Hw29J5J8zvFL5OGyN0tQHb_rd2Mn_xLuecp_B1oZShaw7-mRGp_M0yMNhvqQoiRPiccAkAXghDOK_A8xuC_jg1Qsj7ob-9gjs87L124PpKoxve6h6q-9W0l4pUNhhW0feB3KPQANL2IbcmjOVKTzzaK88nGWaAlLawC68UYV-F7TcA5gK2RZvaXhnFqvZnZbgNb2Vy0t-0H2WkLTYaaAGRRAQBHBXqB_IPZ-wmzOWIKf9Vc0dqjeYkQ427o3gBd-RoQBq19YiWn3wDLKeBhPEoZ1ByW_lSe5hcDUaPDMA_LSewtjr41mJw5etAjM3mFebYcf30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
یادی‌کنیم از هافبک‌خلاق دهه گذشته بارسلونا ایوان راکیتیچ کروات که زیر سایه مودریچ دیده نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102190" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102189">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ-xIvGh_0ZCc1aYujaqANm3bUXHfuj2sPMTDLF26dQZVaefwZj3TCKJf_h9xThxbZCPJq9muVvZB3KgBy0lJ9kaDf3t8-kSD0gPc9jbRpXYOhQ59HUhkT9EYeWsE_2eaqghFfu3qJ_d6Mn2iuw0O_ggpN046n9EEju33KOTIlYlWx6LjFM2LOqr1EohxELVnDN0086qhpmFNEQnVZWOfx7TVn0xZjI-i4T-GJUihmKh8ZihEaWivn_6WRLR67q0Nzdm6KPr8qo11xNHWaGPaEqcd5Q4-gqGC2ufV1UQtFTGoBTK2XM19dcA9098N3cWswX0QpHb1vwu-WqOF7bjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم‌ملی آلمان قصد داره درخواست میزبانی جام‌جهانی ۲۰۳۸ یا ۲۰۴۲ رو به فیفا ارائه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102189" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102188">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laOVYyDqNxCvrA_FRMWCeQW55KubQQ_Ty6fb2TIrcygAVoC7IRPd0EhaGFyinLBObq_rUuDCWt2uxcDnCFzGGgC1u1WaNsZs7Ju04uOvzOKfN6C5WjdYqgm9Oh_p5WQIGR0p77gm3cR3noYq6UfpOUmVh3kQbD7wEKgjoGqvVyFAKmSn6lazim-gsqOC1qIK50ogj0h0OR3Vkw8DTrSgHBjh0HyZvNydPm8l08jHzaWJHHfDHqEKeMH-CFDlPAj29AexhzqEk9swBvE-s-a7rE3TxUcUxbT0AH2ZnhZPvhgkawL5-wI4jAa4inA5_fS_VkbGjWo4jkks349Vl5_Eag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102188" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102187">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzNhb7DqR_VgR_xxMysTMk3xsEKYJq_kKb4x51kGY20IiB0hq7FJruu6CFodKaAPkqjgXMwEqWFI--p_B7W4L2Ky6vBWk2G7Dfh9Y3jffev9uEjK6ZwFlX2DMAL5UGsmVt8Wri5dXOHVxOVnZwh1et_JkCicIXSNaaZF32CLxMii42-mnN4dFGq-0jLtZw-rJzKit5q_Aj-TnbaA3Zb3g5WzRVNh0oTSUmiBKHY_RTQM--8Nl7zvANTrve-W0qjczvypi163AXBIP_r4iih_ld7IQDB8t4ecdYxsk9fx6FNeHYoYfJAavdyCCmGa1aBk9rgEs00d4G7thojQYfXKVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
زیدان و بازدید از افتخارات تیم ملی فرانسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102187" target="_blank">📅 22:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102186">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS_ut0t1ocxwnTGp14zGGtPbTuBfAbmyKmgjYR6HLp0wppjUQFTj0K3-zdUrUdKWi3mSwGX3kSZx8YS5pNP48c54p3SDP4KndD9N6-FIXYjVofTKSCjgoHH8ZZ-vkg4kp3h7Gp4NWB1606LLaOzandz45rAI0XL9XvjKIVPNFZ45WP20RoYclXDQXGwu72GIqPv8SUymrZH6lbtKJZpa2vcWeQABh0KUcXnF8jj4WkPwFUHo3fcDxB8OBN8DxvInBrODKb4UFOH7pJzqjdTLl_E0pFLctYuuB2FXGVNyyybV-y56bUvMvhnRX0uv-PvpaXIlz1rFtqJq8IdRDSajWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
در سال 2020، بارسلونا تصمیم گرفت که دیگر به لوئیس سوارز نیازی ندارد و او را تنها با 6.5 میلیون به اتلتیکو مادرید فروختند.
🎙
سوارز : «تماس کومان برای گفتن اینکه روی من حساب نمی‌کند، 40 ثانیه طول کشید. این روش خداحافظی با یک اسطوره نیست. اول گفت در برنامه‌هایش نیستم، بعد گفت اگر قراردادم را حل نکنم، مقابل ویارئال بازی خواهم کرد. شخصیت کافی نداشت که واضح بگوید خودش مرا نمی‌خواهد یا تصمیم باشگاه است.
🔺
سوارز رفت،21 گل زد و اتلتیکو رو بعد از 7 سال قهرمان لالیگا کرد.
🔺
و وقتی مقابل بارسلونا گل زد، اون تماس 40 ثانیه‌ای رو فراموش نکرد. نه جشن گرفت، نه ذوق کرد. فقط نگاهش رو کرد به جایگاه مدیران باشگاه و با دست گوشی رو گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102186" target="_blank">📅 21:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102185">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSVRX01ONPfYEKuDA4S8FcexpbfmjoukP4KbYprIq3doZYry1uS1iXmtqoTmhH5S1i7NnuHJQU_KGCTyh3GzMVDMe9RdT4jZM5qU3ZwHNnUX4kio1E3C6rsJW6oLvZe-tgaUlhrSChpFfDgVINAVlkRWcUFvd5rOu8wcj-3CXtnINqCzGE8K0aC8z7W44L0_xr90L-oIzmS_t860-frtvjM6poMrQjRQuVwGbu7BRc3jYVd_gAp4CGxDGn-qS7iPNwUXpVZAd5kuaHHvVIJkABXjdwihS-ck-bPELTyuTC45Cyb8Bv_KKt8W4oA1geUdNEeoZbIzdjdqs5lOe70YJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102185" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102184">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4WIg_X3-eTXG2mB_jJlD9yiGQnfRIbKxL2VI9NfVJ0hSWHqZJsa5iQo6xFT8kKA1gQGORZbjD7z21MKUJlSg7pKSE7UKbIiWU3zn7iXi_fSLcSiJifKGKtlxW6y-OnB7JGIWibTw_TsNY75IQRyNHp-_0ivZloJaMYorzszGLINkPVPvYNl6giBw2fvTEEI881lT44kOlHFQvQjMC_OHulW0yFI_uUC-EuX7H1mx_Nt3PiVZSzm0cq9uXJ7vUARyvLPiSOcjPpRXeJGLQBTzu6lrSISdfJ8nyB9k34_owPkV0i-gMbFG0U7gkNneuw0taCpxWa1ELq8Ya83znpvXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ کسری‌طاهری هم پس از مذاکرات ناموفق با پرسپولیس راهی نساجی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102184" target="_blank">📅 21:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102183">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7ZfoX4iyKLrVAoLZuU6qdisa1umpeEdd2888WXDeNds6OcM9WoGSF7v5TgiCVLXgz_Nnr112uuB1hksOmvGyzA_HOYNnVWUQArZ4T1Zl5-9ZWCLeyCIpojIuN1ZmLbIpIasHTf-n22y9KYnX6DBzvFdNKE35zOw7kOa2nwrR2wBR5iHiQo-QVKvML_bGuv_h8dD1vf0-NMpLOFeKC1DMiG1E1Unod5Oooos8dTbDEl6ES0HCcTZMnFV-KCxoKNl0rL_e9gmPDESfjNQoYuX4K3d3WBV5PBNps8OdT2dwdgTg53IVdubTZCVEpqoZTspVmR_NZpGhp6WCflhDz1Wpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست منچسترسیتی برای تور آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102183" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102182">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=BasZgd79b05APcKlBhWeRIHrilcd0ioxpoUyhctVbujRaK4Z_fpogH9EIC9KNynR4HdU5HZIceJTxOkvBUBjnN71Qp6nQsbnLsCK2Y-R2_LDruY3sOl0DeZysg8jrQCog6NE9i0PoquyBAMa3wcyPSqKFXLAJuFxI-KAGg68BFm1WjfhpT9hljwummpYDgrg1BHgmMQVfTMn1zu7atVPcmTwlZA4ZN6UgUuDDLEd63peCnRmnBAJzy1z_ZvZdQmOw62-cE2tyMR_u10MMRXsOQsCrFatZb9vDNlESRFohv_Cm8VXtu65W61d0-DTb0IcngNABIuRU8lrJfwPLR6JEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=BasZgd79b05APcKlBhWeRIHrilcd0ioxpoUyhctVbujRaK4Z_fpogH9EIC9KNynR4HdU5HZIceJTxOkvBUBjnN71Qp6nQsbnLsCK2Y-R2_LDruY3sOl0DeZysg8jrQCog6NE9i0PoquyBAMa3wcyPSqKFXLAJuFxI-KAGg68BFm1WjfhpT9hljwummpYDgrg1BHgmMQVfTMn1zu7atVPcmTwlZA4ZN6UgUuDDLEd63peCnRmnBAJzy1z_ZvZdQmOw62-cE2tyMR_u10MMRXsOQsCrFatZb9vDNlESRFohv_Cm8VXtu65W61d0-DTb0IcngNABIuRU8lrJfwPLR6JEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
وضعیت صداوسیما رو؛ چهره شرکت کننده در برنامه عشق ابدی، مهمان برنامه صداوسیما شده و به ژیلا صادقی میگه شما همیشه با معلومات صحبت می‌کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102182" target="_blank">📅 20:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102181">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSejDzrE3qpcvmzLsnWUGb9Td9bpudbznUEdte5CApUokgDQQrFgKT7bFSr0qCjjThZLTjb3Asg9tmfL3WzGqq0BXb_k0Lj-jcHhLOltsKperIhMj9_wesWxBwMwi75Y_McW0bnbZONYFQZ5mnwC8HgezYoMosGqtIxy2ANGJfpl0ABXOqt1NA4fTtl5akZcCLuPXQ2dfpF8XzlRVR_nPRlgcVLqs02uYoeQbt2w1a-FdtkJFQFFuRx9iiQwnxi6nEhnP6vxnn81BBEC3dnCFtx7tFPGRh4mynCifTNEI8rFT7Z0PGZREUHwkP9xO6vtYuFffZvVGzAuS5JChTKjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری
🚨
🚨
🚨
🔴
🔻
باشگاه لیورپول در حال آماده‌سازی پیشنهادی به ارزش 94 میلیون پوند + 35 میلیون اضافات برای جذب بردلی بارکولا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102181" target="_blank">📅 20:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102180">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=JlQYd-fObJERsRIp7foHKSzvwbttJoqiZmEUqYEdi3tFSfWum2kl6qjv9FvpCk6DmuIEOfG9W8baoVUi16d51BSLCgRHB01cGdPUm--CjrBDDXCFuqMtWXc8OKhP_8XNt9IW7DzHt3HPsRGeLcb2AEJ0q9Z7qWCtbNPR_5mBUSdkB96C_vzkrS84bohfoyboNJjUBsm7gEvD-FF4kUX035Ivw3iuxngCnKgUE4UIA8CmM1QFK0aWz3if19KkrXQhfiM1n9AZ_pFAlvWUCehggU44o6UVOIb3Xx95QG5YKAMgDEPULVyfBLakyRFeKcTHweilhAPK02qHxpl8a98eyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=JlQYd-fObJERsRIp7foHKSzvwbttJoqiZmEUqYEdi3tFSfWum2kl6qjv9FvpCk6DmuIEOfG9W8baoVUi16d51BSLCgRHB01cGdPUm--CjrBDDXCFuqMtWXc8OKhP_8XNt9IW7DzHt3HPsRGeLcb2AEJ0q9Z7qWCtbNPR_5mBUSdkB96C_vzkrS84bohfoyboNJjUBsm7gEvD-FF4kUX035Ivw3iuxngCnKgUE4UIA8CmM1QFK0aWz3if19KkrXQhfiM1n9AZ_pFAlvWUCehggU44o6UVOIb3Xx95QG5YKAMgDEPULVyfBLakyRFeKcTHweilhAPK02qHxpl8a98eyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای انگلیس با هر پاس گلی که آرنولد بده قطعا یه فحش حواله توخل میکنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102180" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102179">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=tWVzfycu5nZjcOf3uu-vOVm8ZQIrM0fX8F1m21XxsmgQ5ShtZDzENXBpGjRQmUFd6ogXAN2QeTVJuSgWQET_LL-Rq8gelN8kZbeWBmN2PQ_hBwh3lMSltGFRz8RRTvP2cJiyF3DGtWxUG1vAPB4RsZgumHnoM7tyEzTpsvthXC2pdde9-5c_iXCkPRCxTQXkoJ_-I0_DCR0Y7EB54qdxvUv5-0QlVaCF8jw9-aLUMtHZlX7gxeBMqZhjRGnhrKtnkJ_lJa8tD-yH4WA4o48clfHiyBaI5Yt8mhCqsOMLyrH3Y9qnatbxKhbFLlTaPBG1dm76Crz1ci4Bf0093dgHgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=tWVzfycu5nZjcOf3uu-vOVm8ZQIrM0fX8F1m21XxsmgQ5ShtZDzENXBpGjRQmUFd6ogXAN2QeTVJuSgWQET_LL-Rq8gelN8kZbeWBmN2PQ_hBwh3lMSltGFRz8RRTvP2cJiyF3DGtWxUG1vAPB4RsZgumHnoM7tyEzTpsvthXC2pdde9-5c_iXCkPRCxTQXkoJ_-I0_DCR0Y7EB54qdxvUv5-0QlVaCF8jw9-aLUMtHZlX7gxeBMqZhjRGnhrKtnkJ_lJa8tD-yH4WA4o48clfHiyBaI5Yt8mhCqsOMLyrH3Y9qnatbxKhbFLlTaPBG1dm76Crz1ci4Bf0093dgHgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
کصنمک‌بازی مجری تلویزیون با تاریخ ۰۵/۰۵/۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102179" target="_blank">📅 20:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102177">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZH_9qwQfImAU3yLnxjMk5Ewq9E1UlZ-BB894jHWQXpgLkytxPW4TucJxVGm6v8eZjOar9zQVswZ6UlLLjBfjn5RsNg2S_u8fnO6ZJ0pSc4HnmZxgsWJghLjGHGPzLWOcZYB202-Mdt5Cw04gu8lpBfSeUUosEbdYsaDVsQ64-m-6lvjkJT9vCc0BqnWw8Fl6SRnP1nhK9MvPoMdUAZTMU-yD0kLFCwQEpO-wqv2gslP3hzd200FxLIR_t5exZ7yEt3t4vrwnkWH5HsWOxsaD8-3TfvpS0KTlyWoJ0pjWBucHVH0drrc4DqFLeTVOfOmNeelg8SxCnEiDaieyy4ZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsMWwgTqPQ6GLcXdghPg_SjthKHb2s_xA6UBxdoiX-9JRGXz0RmKK4OwyGCgZafd06T7Vo1VtE6ml-jN9WPjp4hWz3zWbLJ7vZrT-O5MTzJMhXXK2n-0C0gyKtJWdoXntumGOPGYFRbF6bK32ShR2abaN6ZG9mKzLT8u3QtV3FVMAmyszx35kdlpTBa-auXTD2-i9et0WVsn0W16ZXRFCTZQw_DZcEVyG38Udg7X70ukQrMT_Z3o_AQxc7NIyN-P9-vsTAwGfN_18r84644y1GyD6gYm4uE4urTtDwjoGJtnujBoNiKM3fLFrWJCrBtaJ57TjMTYnIUyB3AyFV9I2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🇪🇸
فکت جالب: چلسی برای قهرمانی در جام جهانی باشگاه‌ها پول بیشتری از اسپانیا برای قهرمانی در جام جهانی گرفت!
💰
🏆
قهرمانی جام جهانی باشگاه‌ها: ۱۲۰ میلیون دلار
🏆
قهرمانی جام جهانی: ۵۰ میلیون دلار
یعنی قهرمانی چلسی در یک تورنمنت باشگاهی، بیش از دو برابر قهرمانی یک تیم ملی در بزرگ‌ترین تورنمنت فوتبال پاداش داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102177" target="_blank">📅 20:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102176">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiuXZAj6sB3Zknkk_x8XtC5MB9UIWjIGIgCNntdHpw7ybWI52_-EPtyHhwH4SqUTEOvifEWDfFeukj7cJiF-DJB2u_6Efa87Dfz10ABRyaUCNh9kQORV8C_tcK0I-qhOvQEz1z_ZYiIzOFknjGtfTJhuAJl9irQ27A9xccn-eHGj8o8ryRrEvrzNpolSoTbuahnDEnnqPh1BZarlfUCC9MzpuCme_2YRTgvFrrWRBd8C_gJpDCtlV3sfklzvtxV-pEkuuVuQ9BR1VTk_Y1LyGvr_QBNPVixlFgzNPcmRnVvPMWk1j4BzjET3Uaw_nUrv4ffyU4OByoHaNW0VI-5u9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ با اعلام باشگاه نساجی، دانیال ایری، مدافع سابق ذوب‌آهن و ملوان به جمع شاگردان مجتبی حسینی اضافه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102176" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102175">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnDc-PSxWtzApUnWBSYBTk_FHzQjX3xAywbIgDJtptz-YSd3cbfgTUbk54GlN7OUOL-N8c6Hl7QHe85TUFR-zRZMhIDN94ygVHFr3PCiGopZjUhf0z0Jh5aVgbaFOe5Qw5TDPp70ql5oKZPv-hIJwHoYzAJjedjIHdhur0dXLXUoWnR9jUr5cmrDGq5ccWVZNhdrEsXPPOSdDmjtYg9QDP1iwykL-jLYVL6pyQ4kViF7kby1AGwkb2eTUytU0VZ2UZ_Cvr44gxiQ6cJZBT5KAwLhjLXPx_i8s2iV-xIoqrTexm6Rv_GroIYryHynsqVkt092YbXzD-bR6vSUQ7kpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری
؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری فوتبال هست و باید به صورت جدی با عوامل این تصمیم برخورد بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102175" target="_blank">📅 19:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102174">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDy30Z7IQQsVKIgDFQjsJPiT7jhlG-vv6lHUlOh6_Vd4nq4aOWzmU7f3hruw3XlmRYipvRtbCDnjAjXgUNgAWgzMdGOL87wakMcNgS4oghfn9pClbR9mxxfGMIb7aqyz0f3qJG41DTv0uyKHfljk21ACWNg6F0xX9ZkTgMQlkH1abztfHnoAOV3WcZQXfz4Tg8VIk0BRL3jJm5jyOXD0AVeiwGO6h6J62rtA6CaXQ7-cNrrVqzs8boKsMXAcA4baI-FgPxq8tjzHTezQK4b8MWlC-2ygpn_dbYPp9giu-bLlJI3dA5NfbYghzpvZh-Qd8O9vYrrpqj6Ai4N2a32ZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
اسکای‌اسپورت: رئال‌مادرید به پیشنهاد آرسنال برای جذب وینیسیوس جواب رد میده و هرگز اجازه خروج ستاره برزیلی تیمش رو‌ نمیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102174" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102173">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=B3iYuLMkqH6gTD-e1COHONT_erji92zPxlrBAGGzjiqlguYdsbANLJPtur9ix_CqNHzry7Hyk4t-hSj8bbrGfhqdLw8xD1Feo4Ym2btJuEMTuMViLL14Q5p-ssJNZNVRVfKpfhY9gm4Rh7RZ6idBE-xngDwZ1_MTXk67oDTBvqBVPbqiPvQtsptXUojSQJvzy1pGODc9PaHxcktGEG6OnYYPH3l_LyHMRTqAervflmiWQw1qtmaPnvjoPgzb9PyARI_UyI8GfkreJaE1tpxvWcJSFdocRgyIWFrApXiAKi10kZWxSZxtQuVMOWIWecvyrjeuwoe_GAr7TRCHvWgjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=B3iYuLMkqH6gTD-e1COHONT_erji92zPxlrBAGGzjiqlguYdsbANLJPtur9ix_CqNHzry7Hyk4t-hSj8bbrGfhqdLw8xD1Feo4Ym2btJuEMTuMViLL14Q5p-ssJNZNVRVfKpfhY9gm4Rh7RZ6idBE-xngDwZ1_MTXk67oDTBvqBVPbqiPvQtsptXUojSQJvzy1pGODc9PaHxcktGEG6OnYYPH3l_LyHMRTqAervflmiWQw1qtmaPnvjoPgzb9PyARI_UyI8GfkreJaE1tpxvWcJSFdocRgyIWFrApXiAKi10kZWxSZxtQuVMOWIWecvyrjeuwoe_GAr7TRCHvWgjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😆
تتو دلافوئنته روی بدن کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102173" target="_blank">📅 19:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102172">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te4pMbpD4pf7IZO45DOYMfuhroAx-GXdf6iREVeZ0EwtTJILYFsPflg7OQxAdQp8ur_-3n6vo9xb40id1-GL9YWiK80qE2UV7VS-RMQNIEJi0BjOFvX3FgW24ORE0G3DCy6gJN3L_emxJm8fyABPFq9mAH3Sjvk87zhTac1tFahxn9us0QA3UCyPX-hEOHOHRDJokiJEGvyXBAxZfVeAsqEgZhcBk0tk-vEv3zSQcFNly88LfLQdlDhQGbXXelG0h2BL546c1nHiY2nthrNdmQYeBGSKc2yZSwbNi1vCPz40nm9NZ0i9JB9BGEZz5xH4jaE7TYKbwvHuEQIru5zkMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102172" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102171">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkirsFp0cz6zyB7oKBX9yyZk2qHnuh-HKZgtWun55dOSac3GlYg0H4j8K9NNxbPLCn4fiyHLi26Cwye10uIXGB6Wxd4rs5iMV2B8qSrGIDb1teyniRpLZCuU8UiJYDA7sq0BsCvB2LjeqULrc2ztfjply_xr0iduoHxN4jxBPx-adSk-HEfTGktjqlDh7h42I4-ZDKZzYslWhNO9UxQRHO8seRkM7q7vGCxPp9fYu2TjibFd7fKLot1AkuOB4FDxfBjLbqbEJHAb0aSOu9TBpSclp0rJveRWMQ36jxSFoKRblbJ6HN3eagvsOAqk-RqK9K9vn-0g5k_WEPPY9_bsNWtdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkirsFp0cz6zyB7oKBX9yyZk2qHnuh-HKZgtWun55dOSac3GlYg0H4j8K9NNxbPLCn4fiyHLi26Cwye10uIXGB6Wxd4rs5iMV2B8qSrGIDb1teyniRpLZCuU8UiJYDA7sq0BsCvB2LjeqULrc2ztfjply_xr0iduoHxN4jxBPx-adSk-HEfTGktjqlDh7h42I4-ZDKZzYslWhNO9UxQRHO8seRkM7q7vGCxPp9fYu2TjibFd7fKLot1AkuOB4FDxfBjLbqbEJHAb0aSOu9TBpSclp0rJveRWMQ36jxSFoKRblbJ6HN3eagvsOAqk-RqK9K9vn-0g5k_WEPPY9_bsNWtdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
برخی از سوپرگل‌های بیرون‌پا رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102171" target="_blank">📅 19:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102170">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnhAUC0TiyaBABRoDqRPcdKThtgW_2KRsK-FGYa-ULj-936y6dDTJsrmYbD6PUdpvVtLu7v6eJaCqsd3xFg7zbZbI7JW-AuHBR72i8_cQ1LG0ViecJZFxHLuEnkC1yh5MstFuG7P6ZwkHFSgWu8xBaj9YjIPxARFWZLHOXyuKK__yHYRnSb_yl87UsPIZ3-QuppRQWD9sEdsaopuiMHNh7FQ0NmCFiLNMVRRRw0v6-r5iC4mFWY3QN5ugBR1OjOVqpYPzaKjeMQrnfWTy4CD21gPfriYiy3bUhhn2uUVfRghzdXfKZ4qCqbWa5vr3uZrmvUQqLg-bIWey1XpqpHpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
‼️
منتخب بازیکنانی که در پایان‌فصل‌آینده بازیکن آزاد می‌شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102170" target="_blank">📅 18:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102169">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_O2Ox0aPnZIZiQGEPJqyqzR3gPiupGSmXBkhJ4Ks6Wur5-y0PeBV3RgThGyNrdrF3sthgEVOIu_MypnexwTe9jACjTighXQeA0urNgwLC24v_2Y8UQjlodeZGdpH1ms8FLzTjMPxWi-ThFw1voQal4H6HJgWu7OcS1nsgTo7KHfjs0MW_Xc7XP5LLYsY6cE2630KEuCwJAwH1y4Eq3_dFRD3tq7813P9j91Crodn-gQxZf7tYM-AcR7CBP_-Q6ZtLhRTp6Ip1ZpE2VTor_QeZ8tJ-ypkVi7-PHBdhSsCyETEiBfbWni9lQIGJ5MuLL_bxZZq46HnuLzhm4JxtfzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
🔵
ژابی آلونسو بعد از دو هفته حضور در چلسی سریع متوجه شده که تیمش برای قهرمانی خیلی جوان و کم‌تجربه‌ست.
‼️
اون گفته به بازیکن‌هایی نیاز داره که تجربه و شخصیت برنده داشته باشن.
🔺
جردن هندرسون — ۳۶ ساله
✅
۴۶۳ بازی در لیگ برتر
🔺
دنی ولبک — ۳۵ ساله
✅
۴۰۰ بازی در لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102169" target="_blank">📅 18:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102168">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-NO_3NlkvsDjMcWbkFfXuSASEzVkuKKrVVHXowjp6l6L2Z63qVgjd59idl1sSxNBcjwqFfa0jVC8OrFlEp2jszJCCNXTIR00ouQcM1Z9OdGr_w6kkZig7cANBuVtXyC-055MtvK42HwjSi-1D7wq5nkYprUKjlmqEIxAkxqXN5s6bP9TVGh3vbtlPGHC78ZGwDKKKcNfJM5eTYAsN16s5lsHKH9SPbXelhSRVYzV-5k0aRp5bfXdRwSoVzVlYBxzR45UXA8J4s-Rzfec92cSHTWuB2cF-ttf7YoA9UzTiHHoLSOM5K8nAYIY5XoIyY3Uj96g7NxRdIDowlt0eu4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ساوینیو به منچسترسیتی گفته که میخواد تابستون از این تیم جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102168" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102167">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWWPEiKQ3SDFkak-TAPxEiEBK_3yYDglf3uQTGeAY8GF6MYGjPXp6FLJ9Z9ArI5sClDC8JLkC9YJQMaoXiLlyRcb45m57aEY7UwuW2N6tnIgRekMgkTxVp9GNIt1CGg1DDXvvn9Ax9SQLW8M6FS4SoSR1wzv1OdoLXzABh9QmIySxDl7y8YqM6mmH2jtFG2pn_LRTWLwQ3OTLNitcvEvsU_dLV5XleLbJM8eHIyyFR_pHV7BLCfFaxLSEONr9dV5wOxHiAsYqHlhHmNjQupnEFdUW8KuXi-KQXtX_lNUN8opwUCnAr8xxiCM56IoydB2fYX5BLvVQ5-y3-odInoHug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار جونیور درباره لیونل مسی:
من کنار مسی بازی کردم، مقابلش بازی کردم و باهاش تمرین کردم. باور کنید تلویزیون همه‌چیز رو نشون نمیده. سخت‌ترین بخشِ مهار مسی این نیست که جلوشو بگیری؛ سخت‌ترین بخش اینه که قبول کنی بعضی وقت‌ها واقعا هیچ کاری از دستت برنمیاد. از زمین بیرون میای و فکر میکنی خوب دفاع کردی، اما وقتی صحنه‌ها رو دوباره می‌بینی، متوجه میشی که اون کل بازی رو کنترل کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102167" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102165">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYi2SJ42wMK-ma9pOBn2Ca1CVL9TnORjB15BnqDgnnbJ0T6ri9SSW-WNv6Eb-d1iipwxAolP4RIs57DWr3wGKVzN1v3ml5MJd_6eS9tzy9cnIbWf4JRigHCEN3A9YH_HMOu4q31urcqvrmqUZuXpkyM8_7vzWESVm_6sC01mfLtrtUhaJccJ9Qsrs0tvWizO2Hmtga0_6w1-96Jo5jEZvwAoTwSt0RSSSCGG_f6D-Iq7fSKXTTQSQnPBRom_EAsUyB_du7Yjg9u_BPUml4itR9AFX6wEiBFs74e9kCc4_xv-OHlfz2JFIh48pAtZ5g4_V58WNKmZwRaWFqElgh1oTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fo-cSDoukiwgEBAswnpvCzQM-0HipJUslfIcbJALtPlU17LsENOStDohzwjR_698jDCFcUCGQ2fxb_MlUdRwtZUIhhnuWYp0ZEPW-NvmMWhqhRy2K-w2kfTeOA6W1eOj219STXBtCxTWlWJb6_qKP305QGmWg-tqoR04wATVKFUou9I4k8NDYBqQ0BuyDVto6OecbN63egsPVpfyFBnLBFTN522YaGC6TgvpmVmJFvr-KP6CjbNkB02EL8aYQ-o3GhrD33jJ7tNaJHf1UgOmR_GVW37ivH3dV9QacTkhy0qeCqZgQVz8qJX6aakjUKSRHO0Qgms_JwFsJj9qrMuqwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇦🇷
رودریگو دی‌پائول درباره اینکه کریستیانو رونالدو خودش رو بهترین بازیکن تاریخ میدونه:
این نظر خودشه! برای من، لئو مسی هنره. کریستیانو رونالدو یه ماشین گلزنی فوق‌العاده‌ست. اما شماره ۱۰، هنره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102165" target="_blank">📅 17:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102164">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hStnPszUtFopEmZrKQzOyo-squw1-nwhb19wJHWkV_lrUR78YL03vND8nWP-68ZEPrTAIFPbu8kRBgaJ6i_nBv5E7kIo8Xgs0x5LQ32-dOZCegbJqzp7CreshCTQq4XzADJYHFUgZoZzV6WD5ZSL9fkpk25JKo9XfTbSNEzy0f4-YP4dyy0a8f6c48K0xbRRyDncc4Y1KM4i2koAqlCF0qe8BLpsIobtkEAFtDo8acJJLr5zpoyuOQz_Q3bhT-bnRKxfikHrDQ3Jjjeh64xU1uu4Elvupt3nMenx9YwupU54hCTGrePpdAEX6jXdiauKSMQWSCsYd0ncK3S-uj5PzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102164" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102163">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/Futball180TV/102163" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
✔️
🏆
برنامه کامل فصل جدید لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102163" target="_blank">📅 17:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102162">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🔵
برنامه بازی‌های استقلال در نیم‌فصل اول:
🟠
🏘
هفته اول: مس شهر بابک
🤩
✈️
هفته دوم: نساجی
🟡
🏘
هفته سوم: سپاهان
🟠
✈️
هفته چهارم: فولاد
🔴
🏘
هفته پنجم: پرسپولیس
🟢
✈️
هفته ششم: آلومینیوم
🟢
🏘
هفته هفتم: پیکان
🔴
✈️
هفته هشتم: تراکتور
🔵
🏘
هفته نهم: گل گهر
🔵
✈️
هفته دهم: چادرملو
🟢
🏘
هفته یازدهم: شمس آذر
🔵
✈️
هفته دوازدهم: استقلال خوزستان
🟢
✈️
هفته سیزدهم: خیبر
🔴
🏘
هفته چهاردهم: صنعت نفت
🟢
✈️
هفته پانزدهم: ذوب آهن
🟡
🏘
هفته شانزدهم: فجر
⚪️
✈️
هفته هفدهم: ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102162" target="_blank">📅 17:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102161">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🔴
📊
حریفان پرسپولیس در نیم فصل اول:
🟣
هفته اول: شمس‌آذر
🔵
هفته دوم: اس‌خوزستان
🔴
هفته سوم: تراکتور
⚪️
هفته چهارم: ملوان
🔵
هفته پنجم: استقلال
🟢
هفته ششم: ذوب‌آهن
🟢
هفته هفتم: خیبر
🔴
هفته هشتم: صنعت نفت
🟠
هفته نهم: مس شهر بابک
🟠
هفته دهم: فولاد
🔴
هفته یازدهم: نساجی
🟡
هفته دوازدهم: فجر
🔴
هفته سیزدهم: پیکان
🔴
هفته چهاردهم: آلومینیوم
🔴
هفته پانزدهم: سپاهان
🔴
هفته شانزدهم: گلگهر
🤩
هفته هفدهم: چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102161" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102160">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwXvDPRclI2Ho75qmBHisp_3viUY-6pjnwk0HMsve-lqe0eKZazBGdVW2JwGIJIKxeL_zz6fajvSw-tXKUARCvC2ePjWlmW9PzBRPQb4oZx4Eqoy_6VlpvQ06kP0VRETBbkBdlXPEuGyiPYRPhOYSQyYFjMPP-m8gVlLHWRgC7cMJM3sGoDLU_CerGIyczE_wcuL4-E6pEa-tILU1cpJ6qaGmRvhodTLAKoAL9yRvbbMgiIHnMXdoutvScr3pi05hAwF_SGhH_BjLI-W7tHZu6pXbQ66ncvnreeBFu0wUxB733yqwhLQ2tgeMjI6i1QvwyWXzscamR362iT-d9dpYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مانچینی رسما به عنوان سرمربی تیم ملی ایتالیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102160" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102159">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfDJ6lmWv4BS7j1OfNo2MuCnxKyE816aby7lylSkb4s70gXP-nvRsBDH9MDHR4NX5aKFEJpP6WznaG1Jd8IuT7ztOGnDxs0LYH_KyQSS9Wu93FfxK3kESrRg8aL4dBHTpVPwGTpgFJD5KHgZixM3izyy944ZYCOESJEY2TdEsHttNAb9qby0zfZBkkufTvY8CiAZMm-_7IpkppIdxqC5QIudp9cHpJl4ofTW77D6Y9XJ9x4ImE5VS7Y9EENnZqX14Gv9_tRywN-G0SI3eOaj7ZissBQovi4ib4l9hv3tiyDZVyuBIeyi0LiVJ9qtWgXyLPylKm1tyNtiW4ELdIk3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗓
برنامه هفته‌اول لیگ‌برتر فوتبال ایران
🔵
استقلال - مس‌شهربابک
🔴
پرسپولیس - شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102159" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102157">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy4l_rqSIqWPo0cyVrST4EPxBc7MzS7GBQEQchfSNzcoXlP01xCK-DkwweXDytxg0HwXc8Gkr6d6mYjF9Du6zjyKURFV53mbh4HdZIJ6lppwwzwbTZdEPNCT0LVY7aJL2ykAFvUVmF_V5KcQL8aWA-IeZnv2TQtiAeXrMlrIiQNoIerlzC3acwicNRG7gpURIan17e66fOfQ6kKME_dGjVLsACpeyRZnRmMqsPb9caiIYu9OpYQtpCRdFekxcE9S9Q4eqYXfOrdSXA3JYu75HlvuEIKDidxS2fCXi03rCqGzh4mfT5QGLxHpaLgfVH4hYo3cV9IoKQQBmzdsaQlhQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=o95l3_oFOWIrCbZbaIvmC4baNC1wY69E4QsT6SoawP4pH00fRKjP2elxHyPRBl90hPNX-2wLlgiS2jrY1LPoBklqsWGvmL2dt0Q_vkMjzr5uxJyykn-R56l01Vb722fPMfntlXzBHpjfjPoB4zRlgMNMUDMcfUmHhavkEkGxez4gOppR8Dv76XsRkl5jWRCDMv75qDK_XcrsfDQcgj2gfXTd2S3G6WDihzy00M4H3XAvHUnGq_ViGi3w5TCqlDrf3r4qnomxOibCSh-SBwXi7O37J_QVCkUEHp-eJv8_jlNtReIT9PvT2kpRMLN-YIcncvGCM2ZyRn_uVPRKmEUxXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=o95l3_oFOWIrCbZbaIvmC4baNC1wY69E4QsT6SoawP4pH00fRKjP2elxHyPRBl90hPNX-2wLlgiS2jrY1LPoBklqsWGvmL2dt0Q_vkMjzr5uxJyykn-R56l01Vb722fPMfntlXzBHpjfjPoB4zRlgMNMUDMcfUmHhavkEkGxez4gOppR8Dv76XsRkl5jWRCDMv75qDK_XcrsfDQcgj2gfXTd2S3G6WDihzy00M4H3XAvHUnGq_ViGi3w5TCqlDrf3r4qnomxOibCSh-SBwXi7O37J_QVCkUEHp-eJv8_jlNtReIT9PvT2kpRMLN-YIcncvGCM2ZyRn_uVPRKmEUxXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول درباره جدایی از لامین یامال گفت:
من قبل از لامین هم توی کار خودم موفق بودم. این لامین بود که اول بهم پیام داد و با وجود اختلاف سنی ازم خواست وارد رابطه بشیم. حتی گفت ازم حمایت مالی میکنه و هفته‌ای ۲۰ هزار دلار بهم میده. همه‌چیز خوب پیش رفت، اما بعد از مدتی دیگه پیام نداد و منو بلاک کرد. الان با مدارکی که دارم، میخوام این موضوع رو از راه قانونی پیگیری کنم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102157" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102156">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102156" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102155">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIMrtwLzFRE_iGSH-ZbM45Ld7PuwEOS4dEsMqa6BdYr5ul1ZUU_g7FuxiXQGDdfrU7VW0rPr7iY5dHjrXwmHFAWEET9W1cbHP1tf4EWsvY0Tmr7Qoga4wRlqSqa5Wdyto47-6HqpRrQuILpWJVZedfGRmCGniGBHDhsVOK2wRqUxJmWSxYFl500YAlzdJz0HFwKwUgO3pRNEqq89AZPr9rGsTQPEjZJ6X0DEXlVWV_fC2ejn2m1vKBrl4KtlHyk8WNtiZkl_Wxzo_g37u_22Do0gI9Lls_k0zYVwVFp8K0dRotQcniMYlPZGFb8aSBEAFDMBh2AnQzuP9t_4DVaLmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه لکیپ فرانسه: لیورپول با بردلی‌بارکولا به توافق اولیه رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102155" target="_blank">📅 16:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102154">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txBhTTlQnreethy9nNELijuhQm36xnINjTwv_TZon_MC4xqX-zxV6YutqcdPN39RirDYA69JyA67ljQ3DjETNj5zwoagZrBL16Z5elf6uK7PUF8fkuJgi4wpkBLkjPZPYgT7JVOVgnZoTGaU4CBbGEZTI7QeIlFTR7InOFWePcsNGxzDkwJRB6lGVfOKUsCHqW_FvbbmS0JqsPG9EOUnbmM-4xuhwTjzZo4wOugtnaZ8DG9tJWVxCxHGjD8ANDdHibwimQTlhpTcmc2pPVHfHWKBdnPrrD_f8O5xeDRVZnocLsH1y1Paq3CzdlYLT0lhlcZTDItpkSWLgQCICfw9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102154" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL82x3Dwj4JqdPovBRnK4c3hFsyqGnaPPf8nMSFIdh9M_GyFrmJLtrMdueRlPl4eDDsrIjY7PIkDbdy3Y4oS_0QNUWms7pBzV7K0QJVeGPfCmvByR9M7Oynpc_42_wMEY9ORj_ZFtR_NNmfd6lCk2uRz5GQHRQwPWgbdUOEDPzLI84wNZcw9a_kaycCriHYn3wPsMhbWXWrsE-KGF1O8fz-r8B9uDY--4yWfUQ7tcwGSAH-q-uTwQhB4Ye8FPbhJLG1ln49OjVQbtAf_JAN7MImmohOwEaTgunbaUfexecjNy64s4WJPeF5i8iTXIYkdK0_aFQMEMEw3DaBuVrtC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102153" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102152">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9Mw3j_dvPfcVQBt9haZuiYYUk568OGJ0qlOvt8oggR-9SOtEm36TlDBUyiqDozhsbAE449SXet_5kXrD36Y1aaw6coLTT0Jr6hbHLzosqJBPtw61GNq6pIBSQGV39lusr1y-GgZN-7RFcVfO8Dck5YhmCgfnisb417pzP27axPxm5kOFM9DMkjcgqZiMZyaWzZvny6zmZhr7q-f2K_pZq3wI9h0qu_zQy1wq1ddmfVPpU1Zh_F2fu44KCX_WPeWhaWoVzE5N4EIhqIJfJ4QOqtBjLtao2l-kZg_1TpKEV887Mv0o6Y7zVEDfvnc_jE5TUf2i8vTgZvAnzp45gkyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102152" target="_blank">📅 16:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102151">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvI3Bui6u-MlyUEIK6y39YV-sa_hcYVFgR7WAuzadz2XpK-2l2xX3sr-2PoVSsMagSwDUhjPWP-QztPzf8swCcGGvoX1RiQNtryXiC5wuvn-HWeL0xNdmEJXnFuHgtUeFMjyAE16ZybK5IMSkuaw3dTsk-hIHMg21HbEwAEalvDe_Rh2Tqzex3Qp6duo7fKIOXzW01LBUa1je00oSvOHNMIlyrLHDLKJrjJsbctP8r41qBl-7c754mpMLNiQgP_RVp3ILR-dBdC-SA1-CD5AIQIiPNnD7l_CdY80fJ3fc9fUrEDDcCf1E5vebAKpv_oEtThtnq8aJf9HDo-qOdwmUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینترنت سیم‌کارتتون زود تموم‌ میشه؟
چون ایرانسل و همراه اول اومدن روی اینترنت بین الملل ضریب 4 اعمال کردن! یعنی شما 1 گیگ استفاده کنی 4 گیگ از حجمت میره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102151" target="_blank">📅 16:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=YkEbMU7qYc52JxWFMB-UOAIBYt2pDEIabsscLOqiSUfgAc-4ep3L777IQDDUDoUsq9Jqdv-nLTpuuLbyZ3J45qAYcEB9q2aiyLvRTGK3b3UinIgiUQmNzM5F1wWaDdqh-7LcDi7_LZ5ZxCQNxDPFE21WSLsVZxzRtvx1MTDUDBwSauF_fvUDjoUYt0uZ52nanp6guMOwMDNfoA63mUNKBm2FDC_ao0fWMqGtbrebSclu4FsAmgEz6FovcQwwc5ywzUdHkhTi4hef6gxEA5d_toM-5D1uTLUomEWud_WKI3fbRW8-eVQyvLO6WNsoafbre9zoQkEvL4IlaazcQbsJVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=YkEbMU7qYc52JxWFMB-UOAIBYt2pDEIabsscLOqiSUfgAc-4ep3L777IQDDUDoUsq9Jqdv-nLTpuuLbyZ3J45qAYcEB9q2aiyLvRTGK3b3UinIgiUQmNzM5F1wWaDdqh-7LcDi7_LZ5ZxCQNxDPFE21WSLsVZxzRtvx1MTDUDBwSauF_fvUDjoUYt0uZ52nanp6guMOwMDNfoA63mUNKBm2FDC_ao0fWMqGtbrebSclu4FsAmgEz6FovcQwwc5ywzUdHkhTi4hef6gxEA5d_toM-5D1uTLUomEWud_WKI3fbRW8-eVQyvLO6WNsoafbre9zoQkEvL4IlaazcQbsJVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
من بعد از اینکه توی مستر لیگ PES برای دهمین فصل پیاپی بدون باخت قهرمان چمپیونزلیگ شدم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102150" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102149">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6pCIVS_OSaWUGHMqhxPpFgk4r0Np5DbqHy4K4iT5etvWqYO62_tYsaAeKsJ-yvD_vfjBG8fnXEQroYCJbkk2wQhOywjx8QoDGoA5Fb52kkMsc0R8rG2UmoVNESy7GFOav9J4z-xVsP5PPYpVu5dF1aeH_YLlZXDNeiEBqwNOFiHRmzTKDZfX2ZsME9IAFtqzLajmBHA7w8HDDC-cfSwJane2TYwaB52AbsWpH7FK7N-jVuYOp4aZJb3k9S22CPae4nS9VmzYaowrHuNNPdK71IlysX7pTZGlFWsXJef3_tjw0VZFcxvE15uxSlxe1LciBmMkNRQV2hcU0loGmbVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
✅
کوکوریا به قول خودش عمل کرد و بالاخره عکس دلافوئنته رو رو بدنش تتو زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102149" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102148">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbysM0AZ9PYLf0Aw50AWh8775k5VxJPRzBFQ9p3TYGe4tAH-TtsEUEJBxW843dfQVDfJISxDnqWP9SuIKBO-JneGxDoJ1Guy1rHm2ebfueYahLLEngcl4qgG7b6cxbVKmBb-yrQUMB9RaSILwUQeLgPELc_dtWVhNNXSYz2yNQJ1Qyft_ffuh-ExtTsFXcfjbEbaqGdptWQ9oW8ewVw-fNYEsi3qJL0WQTQzbLIPas-aH-E0CVPFxT4SIemTr9HqyXCrRLcFEbEgueF8cma-tstXF2NJsiw4AsY1MDqIzyvEsFtUauqSgvDdg02qGfIkiaO8e59Ci9V5l55DFB45Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🔵
رسمی؛ قرارداد یوشکو گواردیول با منچسترسیتی تا 2031 تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102148" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102147">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=gJIkXG4QCEundt9uqsud58b26r4Sx3ucprSxn_mRqAZWL5J_RU3goxP8aNfElNBnNoOp5SECNMt0cMM3deP6Vqr2wXBTWXKBi6IXsSkB8SiDFPFXGCVp-l6wJg_Lw3Fx5VsfvQgtiUE8NA1mQBza8v7t-kpUzJYip3l-1XBLUK8GKACPDHMyVaeb5RdN7osVF9nfyup0XCVSJGEDQ3YA9SBUl0odXdY9x2dEPeG8l4FKvNkA_Kz5URhBLc945HNQ1yl51JuWL62NmIFKi-FODUjkyoWhVHo6J-V5MINNanWBIMds7x4asoErQCMVU9EMg2feHu4bd-jNkusquiSn3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=gJIkXG4QCEundt9uqsud58b26r4Sx3ucprSxn_mRqAZWL5J_RU3goxP8aNfElNBnNoOp5SECNMt0cMM3deP6Vqr2wXBTWXKBi6IXsSkB8SiDFPFXGCVp-l6wJg_Lw3Fx5VsfvQgtiUE8NA1mQBza8v7t-kpUzJYip3l-1XBLUK8GKACPDHMyVaeb5RdN7osVF9nfyup0XCVSJGEDQ3YA9SBUl0odXdY9x2dEPeG8l4FKvNkA_Kz5URhBLc945HNQ1yl51JuWL62NmIFKi-FODUjkyoWhVHo6J-V5MINNanWBIMds7x4asoErQCMVU9EMg2feHu4bd-jNkusquiSn3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به دنبال جذب وینی.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102147" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102146">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=LZufB41dTSjjkKZLDv89vHKVdKPrL4hlCy_MAMszWI32I8G-z2pe13xXsRCqtwDvsk0VRorMysr2xWQIUrSTI9REtD4vq4oIM9rsCzuITisoiCv4uJRCl_2KQ-I6RUJIwLk8xcRkSlbgymXPe0dFWd5r8mYhUHFCN-DBuPPX_5zXsXUWxdiHYu-Rrm-Vf47O2BDHFBOP9jo15UBEcodqLsoA3ysy5rb9Wkzp_-r8zkr-UO9LGHtqpvo8ye52jFDcTbJ7KzKu7dhR-NQPZYtlvgmSx_FvN-a_XZl95aphd1cG0x58WNSnKFscyDwhV9_vWbGq97WpHdWQ-UwZx8NvRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=LZufB41dTSjjkKZLDv89vHKVdKPrL4hlCy_MAMszWI32I8G-z2pe13xXsRCqtwDvsk0VRorMysr2xWQIUrSTI9REtD4vq4oIM9rsCzuITisoiCv4uJRCl_2KQ-I6RUJIwLk8xcRkSlbgymXPe0dFWd5r8mYhUHFCN-DBuPPX_5zXsXUWxdiHYu-Rrm-Vf47O2BDHFBOP9jo15UBEcodqLsoA3ysy5rb9Wkzp_-r8zkr-UO9LGHtqpvo8ye52jFDcTbJ7KzKu7dhR-NQPZYtlvgmSx_FvN-a_XZl95aphd1cG0x58WNSnKFscyDwhV9_vWbGq97WpHdWQ-UwZx8NvRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
اولین‌بازی روبن‌آموریم با آث‌میلان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102146" target="_blank">📅 15:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz6aoqMzS2wuBEupjy2SIh3iv3h2Bb0ZAomeWLer6onQsmYLNDDflN_i8iiPUCGkgYUc-K081mhXOvaVw9gTh3iFUpiSPaggbGriwAIgKrS_5742iNb_ekcxnne2vejFjsriKmD2u6daP8BDn_5_DFQleY5el4nkMuFvs9lsDan5GJBSZjIA-Yu9l6fLpCudJ8-SxldSlkgqY5kNbVt9tIDsbJFGgY7LbNzU_Kz7YaMdtXAnGfjaZxIK7XCvTo4Nzu7nuQtkGMRkJw3rnz5ohyfCDzs1mEj9x6OaEdxyKkDZXWWSaEoOiAW_noc5HNu_TXIz2Rx8uh9y1e10aOYF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102145" target="_blank">📅 15:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102143">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvDqXlBipnqngly_TXD52MYszBXRbn4PeXKs2sBvof-ODdUJtP5gqPfNCuQ2OtVtp-jwLzztaQF0_1_hDmDBWweXirrrZqcHkQNe5f--lJhNSoP5LKIxExEZAuXf_QaYC5QP9SEadXqkOvfBwmC4PHb4sPYy3bwQ6sa_W_NOJ5AWU2AJsDu9MHnzd6PV2sl55VlDzDCDV_vey4oVllpsnThCGNs7v4YqDf1N_gNpn5r8t7H7kdb7v3BwcLb-mj73T05Uy2D7ASvQPxCJhdNPjKNKIKCxnJCyS8JcgS-_Scf7Tx0I9fRc0Dr2mGMycT8gVNINMaW-qteQuP2MCLO_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o07bJu5AacgFhyYYLlznOITNaPu9SlLZ4TtSCVAjnK7t8nX2ZOOouElov_CNcGJ6rIvilE4Etiq3Nd-RI27qkSbCYwDTz4yaKmtbhxOwvcaMIoreCKE34enKqv53zvDg8xCZl6fdnYfmekZVFrd5vtGX1Fzvm34XAbXsbXIclRRk0Ie8GoQdIVF_TO0b-__yNnhgpL1jjrODA--ZXvYABy8hr51eEw1G8-9iZj7Pn_GmFqlM1wjlER-gAFf2YcoqTx87ERvzmKL4zjsOQ7Wehp0O7R-4wME_c7n_2LBs24Z7-xzmEHodlJEQoNaaqHrTG2H1qCdYh-ltzEgfAEWRHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
مائورو ایکاردی گفت همسر سابقش در جریان طلاق درخواست کرده بود:
💰
۲۵۰ هزار یورو در ماه برای خودش
💰
۶۵ هزار یورو در ماه برای فرزندانش
💰
۱۰۰ هزار یورو هم به‌عنوان غرامت طلاق
اما قاضی این درخواست‌ها را رد کرد و سیستم قضایی ایتالیا هم درخواست تجدیدنظر را نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102143" target="_blank">📅 15:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102142">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBfSxCCCZOuAAJL3Ozi786RSejmu85P0eBzpWQj0gCF-GPdXNf91JX3U7HgrTK76TnWg8BsRQp16JsHsO-mFwBGcxgog1Tz2m_mvGGkdAwClnMdXnMzDXlwc7___Rrg_Vs8OOpW9L1SjgOwaZnMZn-1rw8_sIxjrYxB5tCLD77iy1wsyJUpTPYj3kIPA2dg1FLeqL_s_MfItDKfIgn1_O8gr1Nu3nN__fqWSEeZETIVDrFYZKsnvm9cQcyQlrWgA5DG0l4BnKhBsZTxIH0B4nIhoyMNpLq-l3u92m5q-hb3Ip-Y8Wwb9mJL_Lyp6iXQwQkRTJCJvLXG4RJ_N9-iqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
نیکولو شیرا
🚨
🚨
🚨
توافق حاصل شد: کلودیو رانیری، مدیر فنی جدید تیم ملی ایتالیا خواهد بود.
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102142" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102141">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGW_eTaqQcuJhzMtJRkRzOB50_ktFs5A9Ot8Z-iXMYIPrxzI1gd0_XvMmXytFWKExUdP1Fz8OWaSAB0DDiTdftxRZiv-f1r_JerZgow5W3q6bmBeUWppUouIZ088G_7FS_2UnfWW3F8i2YwJgxeo5IjNVZglc9-KzrizxNTzfYwWKliOiryHlfwbjGSDdbKkAEVpwJ6OH66rQJe7rq8UIgES5v7ijlHb8mAiknPF0os4Rf-V5r--eGUbcsMLJD3fSmtjljkPP-cvMc_h_wRuluzPM_Y7lZQuDRjuxqjsW8na9uEURlA8FJEGZmT2xjonhiSCdRRKqpXJsX--9A-U3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی
از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102141" target="_blank">📅 14:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102140">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922dff29be.mp4?token=JYBiBwBP2uWTjn2FeaIGRnS8usC3GD0KqF9_4AOn_VWV3bEtC9j-pKBUWh_pp3bEuhgugh0bzyqOJZX82gUMcQTdi6tWt5E3GI4d-Tmus5_HaeMR16GPwhKQ5L0Mf5Fjq4-cmrVRmVQ5orUP-mXJjY2vQVy2jSPlwIST6oA1ael68JDs1upjYgiMPMhUJJ8ayZtKieVgMcEpcvRLtmWYp-4bt0sFNT1YXUQHMlh_tIwjYmmC_n42wPzbrXcq61doBDSOQ_Ixe-yJmU0mHBnVr4v8SUNI0ngOpZ_7412cN0f4eCc7VzsGeukttTKQHyolpJEqBvQJRCS61CdTb0dwmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922dff29be.mp4?token=JYBiBwBP2uWTjn2FeaIGRnS8usC3GD0KqF9_4AOn_VWV3bEtC9j-pKBUWh_pp3bEuhgugh0bzyqOJZX82gUMcQTdi6tWt5E3GI4d-Tmus5_HaeMR16GPwhKQ5L0Mf5Fjq4-cmrVRmVQ5orUP-mXJjY2vQVy2jSPlwIST6oA1ael68JDs1upjYgiMPMhUJJ8ayZtKieVgMcEpcvRLtmWYp-4bt0sFNT1YXUQHMlh_tIwjYmmC_n42wPzbrXcq61doBDSOQ_Ixe-yJmU0mHBnVr4v8SUNI0ngOpZ_7412cN0f4eCc7VzsGeukttTKQHyolpJEqBvQJRCS61CdTb0dwmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⭐️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از سوپر‌گل‌های معرکه استیون‌جرارد اسطوره فوتبال انگلیس و لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102140" target="_blank">📅 14:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102139">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👀
▶️
💥
هایلایتی‌از تقابل تماشایی سه‌فصل پیش نیوکاسل و پاری‌سن‌ژرمن در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102139" target="_blank">📅 14:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102138">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=TpqziRkGXhJRHoQ3cx0BsW50eHW1qJ8CzuhHQetJJK9UUnLA2Uo9kZvNZESgaxiAs3fE284CG159ka0B61U1QAjAemKRaVgPGYjUdFkvbTfDaKjQAHwhrQX1YUzvP5w5MwYQbpfe8O5I7TDzjXTWQ4jJvdx90oXHV1RVooZVuPuxp27lg_vjyrvbZbfGVUb7eyrJeJ5M-q5m9aGE8T28Pcr_W3CG1S3sk3RLOUKBp7D3Es3MHED-OY_Y0JXki2YmRqRjcxQJalQdqNPIjCQS6SgbVDY-juE5l6kWtdt2n-xfLyRpLyvOsAEWtpzTkzYtWoUR8h-Mei_j6M7ZMlArA4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=TpqziRkGXhJRHoQ3cx0BsW50eHW1qJ8CzuhHQetJJK9UUnLA2Uo9kZvNZESgaxiAs3fE284CG159ka0B61U1QAjAemKRaVgPGYjUdFkvbTfDaKjQAHwhrQX1YUzvP5w5MwYQbpfe8O5I7TDzjXTWQ4jJvdx90oXHV1RVooZVuPuxp27lg_vjyrvbZbfGVUb7eyrJeJ5M-q5m9aGE8T28Pcr_W3CG1S3sk3RLOUKBp7D3Es3MHED-OY_Y0JXki2YmRqRjcxQJalQdqNPIjCQS6SgbVDY-juE5l6kWtdt2n-xfLyRpLyvOsAEWtpzTkzYtWoUR8h-Mei_j6M7ZMlArA4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
امیرحسین صادقی: از وزیر انتقاد کردم، به دادسرا احضار شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102138" target="_blank">📅 14:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102137">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AnlDvk0gJyMM6PjKwigY_NRTQxv6FAVhQpfaNHA_cg83S6bZx9evRQxOEIg3utLAVuQfr30gP3uC2yaUkZeShX8NUgfCr6q_WnoMRefHC8BO0nR_SnmpGJ42NiE5KHleH1hbbI4sW1YamKuxNQbV8e4-_plBTS3J09aj6PJziJUiT5MtRdESQrusHTVm064qNoSru36RL1cufBWbv2A3uho0kJNbV61cQbn-FIDEVQ-crgb7O6WdGIlKIqeRPgirtk7Ib83lMqKs-aRIlJbg3kCSFNDa36RPy2Q1ghVmgJgricRKF-QUVW47hzguD8dz4LxGo3mXdWwmp3cVLy7Tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: وولتماده مهاجم نیوکاسل مورد توجه بارسا قرار گرفته و به صورت قرضی در دسترس کاتالان‌هاست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102137" target="_blank">📅 13:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102136">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔥
کنترل‌‌توپ‌های ستارگان که منجر به گلزنی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102136" target="_blank">📅 13:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102135">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQ3gC-XHYszmxBSpfG9ZlQ5vNqCifqolypBkkKobHm5fDCWdHSWnDGSAHUPhC1kOvDM9LT38VEFB9nVwVTwZa3PyHiG0YLj8ztXrlSTH_GZxGDA7v_BgrFxhgLxmwIYPNYYT1X77pAA9PHqGIgTinHNkdl-4eC9_1GMMHhQAwF-Fl8UL29Io1wiphoATja6_I_m5loCrXGNfoUzaRHeamYfBPVA1Us4kEky3Tv6rzcAbG7i91zmUK8azOqUqKS3vpCoBvTF44zO65Bfh7Ef0NBMpqLRl9I0SyuFCDQriWnCyad4vWFiwcpX9zL3lgBRZm6YFe-_H6MRDprthQfrw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه بورنموث علاقه‌ای به فورش جونیور کروپی به بارسلونا ندارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102135" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102134">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_ejjdo6JvZfzTK5L2wdM9ceZ5YRn_3zyFTtbC_g0QKVUFFe5M69_jP7yFpQ3VkeIAqzeMmFepkax8NilTx15pUqC4BDHI0BEorIydF7tF63DWZAe81K6GAQKk_4swx_tAgCgB9fXAsg_5qIQGRYisdWCWfiUV2rs9CNDxN3avmjE8UaglSeFoVw-Hbjv-K7Y32ak4Tto8kilzH9C_6PHn14k72HKtYElCsLxfTMKdCMvM1SP62Oryp6oOBQyAa1e0f0PUwBrmEr8ZKE4eOg3p9tHrSd-nKwEiCbNQE1h-630B-iywwfRB1YjFrv6Nsi67A6mcOyN7rJs61_478tm9RNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_ejjdo6JvZfzTK5L2wdM9ceZ5YRn_3zyFTtbC_g0QKVUFFe5M69_jP7yFpQ3VkeIAqzeMmFepkax8NilTx15pUqC4BDHI0BEorIydF7tF63DWZAe81K6GAQKk_4swx_tAgCgB9fXAsg_5qIQGRYisdWCWfiUV2rs9CNDxN3avmjE8UaglSeFoVw-Hbjv-K7Y32ak4Tto8kilzH9C_6PHn14k72HKtYElCsLxfTMKdCMvM1SP62Oryp6oOBQyAa1e0f0PUwBrmEr8ZKE4eOg3p9tHrSd-nKwEiCbNQE1h-630B-iywwfRB1YjFrv6Nsi67A6mcOyN7rJs61_478tm9RNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیر حسین صادقی: قلعه‌نویی هم مثل علی دایی جر زن است؛ کاش آن حرف را نمی زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102134" target="_blank">📅 13:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102133">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Zxe9SNByP9nItAPwFeHLUzr__GwOTIFKj04JtPYk4J6G-rGqFnIOpRCQgz6mCjgH7RjzDkdgJq9FeLR0e6Jdo0XB4FY5M05zClens-YE6YSICE8wVYa-11IYj1za3QKvmo9sXeIP3fiAfmBpQBCt_vwaVUthXaD-WVUkbJ1lAnVCkbZy1I_4JpB-Tbwb69Hd57hMzy4p33SnwfrW2za8evY3QLonMwSOPBtDFWohcueC9w-CDZw5tMg4rSz-2PtzW9dl69eAxyZ58E3ZKk0x8mnzOmYhdUHRFAHxH7uqbb2gML0P2JbhVF0dE43bqtjVOxoWdI3ybY7K8qAL-XDeqVL5cvZ7qiF2d7omwEec7lOWZqRyAddYopLPxS6a9SLdslQ62OwQokyyGn3Sdhbjn1O1mAY4OoHZIdMJGaWE2wdSpIF3XOITkwfhVi_YWk1WLMMbuE7EKhEiaFSGFGXD1n86Tc1mvGtZHLYkW4NYMGiJwperxoHoVBExeiunvdoMFDhDLQKRGpYmSnp_mxXdev6NWhkCAlKrTIwroCbcIYZeyCYJNzvKSELjz2iK2ZpWQ5ZrCVMlA-plBab3T2krxxHmm2ZFQ672o3SUrx4u3KfotFHP_I6KN5G275_bJ7BRTOOoHYIo2g8DQQd8px9c_1fdP_dxrYY8DE5TzXiqQ-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Zxe9SNByP9nItAPwFeHLUzr__GwOTIFKj04JtPYk4J6G-rGqFnIOpRCQgz6mCjgH7RjzDkdgJq9FeLR0e6Jdo0XB4FY5M05zClens-YE6YSICE8wVYa-11IYj1za3QKvmo9sXeIP3fiAfmBpQBCt_vwaVUthXaD-WVUkbJ1lAnVCkbZy1I_4JpB-Tbwb69Hd57hMzy4p33SnwfrW2za8evY3QLonMwSOPBtDFWohcueC9w-CDZw5tMg4rSz-2PtzW9dl69eAxyZ58E3ZKk0x8mnzOmYhdUHRFAHxH7uqbb2gML0P2JbhVF0dE43bqtjVOxoWdI3ybY7K8qAL-XDeqVL5cvZ7qiF2d7omwEec7lOWZqRyAddYopLPxS6a9SLdslQ62OwQokyyGn3Sdhbjn1O1mAY4OoHZIdMJGaWE2wdSpIF3XOITkwfhVi_YWk1WLMMbuE7EKhEiaFSGFGXD1n86Tc1mvGtZHLYkW4NYMGiJwperxoHoVBExeiunvdoMFDhDLQKRGpYmSnp_mxXdev6NWhkCAlKrTIwroCbcIYZeyCYJNzvKSELjz2iK2ZpWQ5ZrCVMlA-plBab3T2krxxHmm2ZFQ672o3SUrx4u3KfotFHP_I6KN5G275_bJ7BRTOOoHYIo2g8DQQd8px9c_1fdP_dxrYY8DE5TzXiqQ-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
چند ضربه کاشته تمرین‌شده و تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102133" target="_blank">📅 13:03 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
