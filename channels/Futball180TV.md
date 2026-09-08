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
<img src="https://cdn5.telesco.pe/file/V4lToKpjSDviDx3cL2dVUVl_BlVhYAOIAzmvbMWO2IwWQ4ZnQMiV5mPQrKwhdZseFAnRx_Kdyp4qUfDYmaiLuAPef37Wx6oicsKyX8VEGzByvNrWQs-bLlLiOBjPU0zfSdseHBx3wTcmkgrj3zkqZWr9NW6iLlUSIZ0ojH9G6FpIEzIzvff9zxgFt0R7TUmiQMHzGJaPMphIHvuR3b3KsfTftKIrlL4_8KjOONKLGf6gHzhFOQKoNpGSQwKru9VtBcShUFvc9X3HxVGA8w7xQUxs26fY1VwELmJWslRjdqjBWm9w7nSevNID7fHgOrmFTZhsIw0siuBInRdJRYtmYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 422K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 00:16:33</div>
<hr>

<div class="tg-post" id="msg-105942">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c99ae7fc.mp4?token=n4M1I-5l1NlOHxPMKBzcI5w9ZFbviv6to3DyA2dkK9OXRRcBakIr1u5I_ur5ouv3g5dY37wf8mmVvdcf6Z2nd4ge8R5QW-sLIveRSpnXwRYsKl7zzAO1HId0KFGvdffmGwkWh0nz-F5COdPZfnXfp7jlX_gYiI6-_XUORGAeJv8aNAqq1d-apPOvIWL3UXxLe8PPtZW65t5RedX7OC7SGgNVjsdzCbmmvi6PgQS2JKFebOx2dU5aSEfnlm7kjHyCcUAj5Th0PVebBkMUoIRuFGwLC_6sK3K1NSMAJlV2-OnRE44ocr35TO5uRkw0xKhQFXSamYCJdNA15aW4Y7GG8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c99ae7fc.mp4?token=n4M1I-5l1NlOHxPMKBzcI5w9ZFbviv6to3DyA2dkK9OXRRcBakIr1u5I_ur5ouv3g5dY37wf8mmVvdcf6Z2nd4ge8R5QW-sLIveRSpnXwRYsKl7zzAO1HId0KFGvdffmGwkWh0nz-F5COdPZfnXfp7jlX_gYiI6-_XUORGAeJv8aNAqq1d-apPOvIWL3UXxLe8PPtZW65t5RedX7OC7SGgNVjsdzCbmmvi6PgQS2JKFebOx2dU5aSEfnlm7kjHyCcUAj5Th0PVebBkMUoIRuFGwLC_6sK3K1NSMAJlV2-OnRE44ocr35TO5uRkw0xKhQFXSamYCJdNA15aW4Y7GG8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل اول اینتر به رئال مادرید توسط آگوستو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/105942" target="_blank">📅 00:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105941">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رئال کیری بازی در بیاره مساویو میخوره</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/105941" target="_blank">📅 00:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105940">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">لائوتاروووووووو</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/105940" target="_blank">📅 00:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105939">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">لائوتاروووووووو</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/105939" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105938">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینتر یکی زددددددددددددددد</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/105938" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105937">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گلگلگلگلگلللگگلاگا</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/105937" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105936">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
سپاه پاسداران: تا لحظاتی دیگر تمامی بنادر بحرین و کویت هدف حملات قرار می‌گیرد. منتظر باشید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/105936" target="_blank">📅 00:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105935">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رئال بازم نزدددددددد</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/105935" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105934">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/105934" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105933">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گلر اینتر با اینکه کیری بازی در آورد ولی حداقل ۵ تا گل خریده برا تیمش</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/105933" target="_blank">📅 23:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105932">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">امباپه بازم نزدددددد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/105932" target="_blank">📅 23:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105931">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کورتوا نبود الان بازی چهارتا گل بیشتر داشت</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/105931" target="_blank">📅 23:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105930">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFqrrwg2VYZPO1ZYzCJEJFBGDJ5xsNZHv08pNwCGevgvadZEn1-MzAkjZ9lokroHwIiZ674GMtK1JlrBTlIGpha64I2rr2IMrek57lYgTLkb59JdvIhvdTvflj2hKn6gdHip73uTwjM9m8rvlXaF79-0qgmwg0Pd9P1jdOdPlr2S5z4wkyluf_qmjG1urBpc_AnLzTic3sKOhfQ7TVPuQHaOjmMMRDaJj2yF6YvX41konYX3M9zKScLIDzhRW7iASrENtcDmtR_QX1qw0fpQ3sVcz1Q-DNop5cbchlTykBLOKb0_jPatIeJCSBL2gPcVWoghoK14VThUtvcnsk5EBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلینگهام جقییییی
😐
😐</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/Futball180TV/105930" target="_blank">📅 23:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105929">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بلینگهام جقییییی
😐
😐</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/105929" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105928">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چه دروازه خالی نزدددددد
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/105928" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105927">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/105927" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105926">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/105926" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105925">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGYlS9vtvWxziz-ffFLUCra9pYCNlYiiuYhaeROg7sFiiwWhI_CWVd8o0Xp5YG2ze0l3BvMYZHCp0gNtUHIcrD3gSDUErz6GCO2PctPnT-FylIEwwyXGDKq5vXWzdQGn8GMjkNOUO1m7wRXMIVSmNzyuLDtoQQfxKXimZrnPwKHt5z676eqjLWsJlipn0MaZKU2M-DYxxekkiA6wBuamJi73WM35eV6VL9APr1bk4RQJsu64OeDZytjSZF0iDPOetL5tJSIcTeMz1PiLHRx20zNongkDFjTXMVF2VPDUyb-vZELA_cq6LzKCrERAEKpDZlnKSU-z943j4jjcWv4teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
وضعیت نتایج تا دقیقه ۵۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/105925" target="_blank">📅 23:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105924">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کورتوا خداااااسسسستتتتتت</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/105924" target="_blank">📅 23:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105923">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/baae1563dc.mp4?token=nB_14Pc2JilUzlLSXJrqdBDmkrskU0DEC5FjExjRt-IINbTabNVZplRqqghokq_Zj_Hcs9jiVyEodOoLG6i3pG7II6u8fHpoA6QYec5MkEVM5naMT6T7bzohxcPLICKe9eVvVvkpMG_CE-e8gFYxYND53WzPaSsQs9XnwvrYAijYp1iFrsi3ydsMPCZ1O4iEpOfgUQhgomwT2iu9WSJIH81hgA8QDO85_Bkxg6p4fpM-UX0yr-Wg4qLhDPgTwStqZSAe5eDYNjdICkgj86dIbtTwPwkbaGI6h9YoYqxJI9RSw67fNq1cP_s96JT2oeBwt6b11C8rd4RHdBs6ObtMsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/baae1563dc.mp4?token=nB_14Pc2JilUzlLSXJrqdBDmkrskU0DEC5FjExjRt-IINbTabNVZplRqqghokq_Zj_Hcs9jiVyEodOoLG6i3pG7II6u8fHpoA6QYec5MkEVM5naMT6T7bzohxcPLICKe9eVvVvkpMG_CE-e8gFYxYND53WzPaSsQs9XnwvrYAijYp1iFrsi3ydsMPCZ1O4iEpOfgUQhgomwT2iu9WSJIH81hgA8QDO85_Bkxg6p4fpM-UX0yr-Wg4qLhDPgTwStqZSAe5eDYNjdICkgj86dIbtTwPwkbaGI6h9YoYqxJI9RSw67fNq1cP_s96JT2oeBwt6b11C8rd4RHdBs6ObtMsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی به پورتو توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/Futball180TV/105923" target="_blank">📅 23:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105922">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امباپه چه تک به تکی ریددددددددد</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/105922" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105921">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/105921" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105920">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگلگلگگلگل برای سیتی توسط هالنددددد</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/105920" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105919">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
فاکس نیوز: امشب برای سربازان امریکا دعا کنید  نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز  ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/105919" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105918">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/105918" target="_blank">📅 23:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105917">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYQIWHPYGRxMQOsOpgveNE_tGmjKzi9w1Kr5dX-i4atmJJBFNbCvbF_dPPtynaWYVUczoLMRJ_motvgcVK9ZVyZwg629qM2FWlZTM_oIJWXHsI46IEsfIBKmDcXd0lehvoFxRgytoYtW0i6PNmLt1c9im6YgrUxyKWV43CPQpozK2SLxJHrNLMVSwTOzjYs8c_Ohd7JXoet9VElsvFkIExJQUX4lojNIZJvIckt-t0zuJS0Zimr4hoYmjuimYJy0tiuaSDsIUNfOE-vX-DTePWGEDywe1PchXRe6v5DUHbWzm-U6pW0UnEs0b9N3r9cBovEMjkN7wdUlz9vRRMpmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت آخری که رئال‌مادرید گل نزد
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/105917" target="_blank">📅 23:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105916">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کورتوا مصدوم شده</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105916" target="_blank">📅 23:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105915">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کورتوا مصدوم شده</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105915" target="_blank">📅 23:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105914">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105914" target="_blank">📅 23:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105913">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105913" target="_blank">📅 23:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105912">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23f212f578.mp4?token=KyBhxnNfNFZNOHaAShWpms__adZbQKDEFLWSy6Kd5Q1b1AexAipA43EWTXLFVOG08DCdiX2E6k7hGBiKD_6BPvQDKtxs7NA0_DVcadzuvud6w9B_9DNA9eW7NNSTiswCQFHXBW0vhrbmjkAmc6MUflgPss_KE4TxWDa7iJg2yLBkkgtFEAJM45mftFhKFFzsZAlqggYWkuPT4J5_o0FDkmtBbeMR1ZixI6YRW3kcOp4KllHclAZaGNZEQhV6SWEblIA21uWUTVzrucoHmu6hz66jXAHoas8DX__phpUJthbZLXqlIAaZt7JySPDK32DRIH7VDvThSj51srAIJJ_8gg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23f212f578.mp4?token=KyBhxnNfNFZNOHaAShWpms__adZbQKDEFLWSy6Kd5Q1b1AexAipA43EWTXLFVOG08DCdiX2E6k7hGBiKD_6BPvQDKtxs7NA0_DVcadzuvud6w9B_9DNA9eW7NNSTiswCQFHXBW0vhrbmjkAmc6MUflgPss_KE4TxWDa7iJg2yLBkkgtFEAJM45mftFhKFFzsZAlqggYWkuPT4J5_o0FDkmtBbeMR1ZixI6YRW3kcOp4KllHclAZaGNZEQhV6SWEblIA21uWUTVzrucoHmu6hz66jXAHoas8DX__phpUJthbZLXqlIAaZt7JySPDK32DRIH7VDvThSj51srAIJJ_8gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
اشتباه فوق‌العاده کیری گلر اینتر در صحنه گل دوم رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105912" target="_blank">📅 22:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105911">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انتقام بارسا رو قراره مورینیو از اینتر بگیره
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105911" target="_blank">📅 22:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105910">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اشتباه فوق‌العاده کیری گلر اینتر
😂
😂
😂
😂
🤣</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105910" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105909">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رئال‌مادرید دومییییییییییی</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105909" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105908">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105908" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105907">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25403f5ba8.mp4?token=iQXlb7i0qrBWlM8YtIWhPftyIDOb7JKDN_Xf8MxiPci-YAU0wLh9MDs5s9sQpoerAP_UZxPDYBOmNX_VpDeFvbMFrDLcrinVs6v97r29nMZX36ZeCPi8-z_CN0rmj46y-PcxT4AS9aVTCUMfMnsCAa_Jr84K3qxkk1jbbb1tgNmdj-eAL9yc_PqGR__oBWWIfR4pmdQ9OlEtn7m2ymWfz_saK8AujbYab6yFFv4124GObVCVyX0SUZqYXiIV_yl1gcrkJ_27ByZ7doanu6IAs5D1S1_0948NWyIbAxfAFm3mU0vQQ1x2vChDGX0ZbNgaws7g2_7V8U89UMxOv7YaXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25403f5ba8.mp4?token=iQXlb7i0qrBWlM8YtIWhPftyIDOb7JKDN_Xf8MxiPci-YAU0wLh9MDs5s9sQpoerAP_UZxPDYBOmNX_VpDeFvbMFrDLcrinVs6v97r29nMZX36ZeCPi8-z_CN0rmj46y-PcxT4AS9aVTCUMfMnsCAa_Jr84K3qxkk1jbbb1tgNmdj-eAL9yc_PqGR__oBWWIfR4pmdQ9OlEtn7m2ymWfz_saK8AujbYab6yFFv4124GObVCVyX0SUZqYXiIV_yl1gcrkJ_27ByZ7doanu6IAs5D1S1_0948NWyIbAxfAFm3mU0vQQ1x2vChDGX0ZbNgaws7g2_7V8U89UMxOv7YaXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول رئال‌مادرید به اینتر توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105907" target="_blank">📅 22:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105906">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امباپههههههه زدددددددد</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/105906" target="_blank">📅 22:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/105905" target="_blank">📅 22:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDxOqGMGOHzoA97bO-rVCRJr5yH6YLlLyv8K4NTXhzGzir09uLNgKO7g0V4szHyAgMm-Ha2Uty4H03vTt5-mba6KbqYRX8MwgRIh40p76wh8GnRB4IhAv9FS5Px36i_bnZSCPbbp9flnGHFO6iiM_H4uxDwFHTTDD9pWq71YpV7DTY5FPqDjrxXZwu7pR6t2phw8XHV56vGVQnQaHB8A9qYVH3BGmgd-quIDto8hlqJwVWd9GSsJZn1vG2kgK_C325gqtg_ezIAQkCpSzcidYZVMpL7cysh5RQ8CDFkKXlHr0woRMwfzWjQ2RtGKghRMlrYBsycT8QakKy7yWyQ6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتیجه اخلاقی از فوتبال ایران:
فحاشی ناموسی در رکیک ترین حالت ممکن ۴ ماه محرومیت داره.
جمله "شاشیدم تو این فوتبالتون" ۶ جلسه محرومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105904" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105903">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f233f0dc0e.mp4?token=Q_VEloRc4zExFEB68Nfph7ZwTxMzFBZLZiszZK2AUVx85rEWPJ1JI19H5GqG0UNA-C5Scc7y_jAIqntc-QbRSlRLIyS3C8UWJAVd9Y2VLnF8RtH-VLbDo5-HV57X9I-e4ZnC-KynqMq4lOE3hIHY7jkaSfKJjiBu7abSo7XgQrQjDi7uvgr3nen07leVVu47r74e-AP3wLzHowtXtke87G4sq_FRcuwFD_W_tyVa5Im__5oAZg2eYNJvIaO0FBn68EiAurwqEfdxKsgZ-_9-J6n-mh5PnhqBA-5RL2aYUfh4xObqylwgQeoQQOKrsGzJCtP2OeAR9qC-pxOMXq5nhrARhxl1zsivQIvIM55q3uFAtr7lsEh7uecyv_luWNTxzgstLHWpjbs_nR_XWz5WsYPc1w-ysEyIsZpzheIwq9Ci9NzbA1ZAvBnb-XbHcibmdWtiEMJYDEJY6QN4LYHppRqSq1lGGFEaPqfZuRAjuP-YKiZWmmcJOY_SmqettsN56wnXgrYKGCg8TmU6BJUHTjo7xU8a0VZNpqXSp9h8xPEP4YnOFyNQEwObuABgFTCESIz78Ed694PTndn-ImRm7HvvSLQoanTi7O4ONCogZftxyj1SVkPI1KY3OuNbhORIN_2XsPEQJ3nQuXcPsd4JOw-_U3Sb8P6L1EkcYiqU628" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f233f0dc0e.mp4?token=Q_VEloRc4zExFEB68Nfph7ZwTxMzFBZLZiszZK2AUVx85rEWPJ1JI19H5GqG0UNA-C5Scc7y_jAIqntc-QbRSlRLIyS3C8UWJAVd9Y2VLnF8RtH-VLbDo5-HV57X9I-e4ZnC-KynqMq4lOE3hIHY7jkaSfKJjiBu7abSo7XgQrQjDi7uvgr3nen07leVVu47r74e-AP3wLzHowtXtke87G4sq_FRcuwFD_W_tyVa5Im__5oAZg2eYNJvIaO0FBn68EiAurwqEfdxKsgZ-_9-J6n-mh5PnhqBA-5RL2aYUfh4xObqylwgQeoQQOKrsGzJCtP2OeAR9qC-pxOMXq5nhrARhxl1zsivQIvIM55q3uFAtr7lsEh7uecyv_luWNTxzgstLHWpjbs_nR_XWz5WsYPc1w-ysEyIsZpzheIwq9Ci9NzbA1ZAvBnb-XbHcibmdWtiEMJYDEJY6QN4LYHppRqSq1lGGFEaPqfZuRAjuP-YKiZWmmcJOY_SmqettsN56wnXgrYKGCg8TmU6BJUHTjo7xU8a0VZNpqXSp9h8xPEP4YnOFyNQEwObuABgFTCESIz78Ed694PTndn-ImRm7HvvSLQoanTi7O4ONCogZftxyj1SVkPI1KY3OuNbhORIN_2XsPEQJ3nQuXcPsd4JOw-_U3Sb8P6L1EkcYiqU628" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال رئالیا از اتوبوس تیمشون
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105903" target="_blank">📅 21:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105902">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnjqBg4eFNCkDcGUsDrkTX7YF20XzYKm0v3JR8Lp15hctfIV6TfFFq8wyb4XApGxwXlEhYi8rwPgO2voBCZ5iKXJYIKrzhi5JBh6pNwkuWSa_9it85Th6zo2q1qazOTE22t3Ktv6Fnf6GIJowf7Wg5aQcXM3XYzhOAC_zmXmuGgiqvUN7V-jAmvcYrxgDT16ntD6JhSppPP0nLHxY8z5fgr8HRMUMFKmlOVPsgTT34isI4JHjbBnSOZX9cXD5JO9kijsuCmje0iOoA8f0HNSK8PXb9kr2g4zLZ-18J9X1EsaiuHtrj8qJXS_-B00O4h5FCYPCCsPSsdEoJg7gHgUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
🇪🇺
اگر کیلیان امباپه در بازی مقابل اینتر گلزنی کند، به عنوان پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا، هم‌تراز با رائول گونزالس، با [71] گل شناخته خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/105902" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105901">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
‼️
🇮🇷
تاجرنیا: از سازمان لیگ تقاضا دارم قهرمان فصل قبل لیگ برتر را اعلام کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105901" target="_blank">📅 21:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105900">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38f65ddf7.mp4?token=MvUDdQTMXDqDj7L-3QacNkMTmrh_SHuTA94PcLlmOXUxkLNbFEG8I580MDYJGhaNgPa4vs7B-ca_S398IaRX0QdYY-A6v80MTQUdDNSB2wCXN4LmfudOIN6F_mIxZWUT8KZ_OLHfA_qf_Ga1GvUKA13FhG5GyfGBfXUxB0_J2654Mf03MICi5bNqnHSeMF9YD6EWNOWdy0D9zvzvhPSIoiMYjHhX25iUg464CMxfxUzFz7PZ3r7ZdL958_77xYtyEiCWrRah9DQHom30fWxrbBSXF-u1FbLwUoNZS9PXqnXBpGQRbG_4NmwDurJZXytKJ3sLo08QfD13y4mhLzigQ2-ei9KpfBMtSUmFUjXV3zOg04mYgYUuNncud6pAsK5U9rD8NGiGDmjzB3x-6M4m0zb9wU_APmGXyEu6_yZkJ5k94sOnF3ley4e0mP6wgBvuxtG5G_-lkb92He1rYllSmsQZF_7jS9KpcR1JwoGC-p8LRkzDGV9qLkyOej00XJW_zEZmB7y_0ndHODT7hK0MsIixSX99opUR3XOCxFMKOcB0V782HQw7KDuT0mYE73PmGhlPZ9QgjAAvyiPO7E_XkPMjTWT4mSwF24Hd0eadUA_X1i8WNLwdSd_UeU6v9CBW2VP1JC4HUqsQ7j3mguK7opOWLMr7cMIz_m-DKBFMaOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38f65ddf7.mp4?token=MvUDdQTMXDqDj7L-3QacNkMTmrh_SHuTA94PcLlmOXUxkLNbFEG8I580MDYJGhaNgPa4vs7B-ca_S398IaRX0QdYY-A6v80MTQUdDNSB2wCXN4LmfudOIN6F_mIxZWUT8KZ_OLHfA_qf_Ga1GvUKA13FhG5GyfGBfXUxB0_J2654Mf03MICi5bNqnHSeMF9YD6EWNOWdy0D9zvzvhPSIoiMYjHhX25iUg464CMxfxUzFz7PZ3r7ZdL958_77xYtyEiCWrRah9DQHom30fWxrbBSXF-u1FbLwUoNZS9PXqnXBpGQRbG_4NmwDurJZXytKJ3sLo08QfD13y4mhLzigQ2-ei9KpfBMtSUmFUjXV3zOg04mYgYUuNncud6pAsK5U9rD8NGiGDmjzB3x-6M4m0zb9wU_APmGXyEu6_yZkJ5k94sOnF3ley4e0mP6wgBvuxtG5G_-lkb92He1rYllSmsQZF_7jS9KpcR1JwoGC-p8LRkzDGV9qLkyOej00XJW_zEZmB7y_0ndHODT7hK0MsIixSX99opUR3XOCxFMKOcB0V782HQw7KDuT0mYE73PmGhlPZ9QgjAAvyiPO7E_XkPMjTWT4mSwF24Hd0eadUA_X1i8WNLwdSd_UeU6v9CBW2VP1JC4HUqsQ7j3mguK7opOWLMr7cMIz_m-DKBFMaOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
تاجرنیا: خلیفه و گودرزی از نیم فصل بازیکن استقلال هستند. بحث انتقال خلیفه و گودرزی از آلومینیوم با مدیریت باشگاه آلومینیوم توافق شده است. این دو بازیکن از نیم فصل بازیکن استقلال هستند و حتی واریزی هم انجام شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105900" target="_blank">📅 21:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105899">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwfoDyVNySRetp3Pm-OQ4xxrvmpHntW8o8zuRdW3UgySDiIZuhsC-2AGro6sGqYWrdlnq1aMEv3kgrrBlR8-gs3o3FkALuAR0fA269MtqCWt7MnNfPSnNCTGsay_S80OSmN4QRCfh6YKDUmO_x1xeWPKycWrPR9G9ZNMbG_LUJ2HcC4hbkXVzo5cxeVhWWtawYLefc3kavNLVvWLQRfBJxQ9CocqJzA5W1E_OybMOQ3Tqh95MQ1x1O91ditthiO6sh3iYFp_2tmYDCz1pGtkT2EmAvooC8lgSkLnPbS9UVgrIq5z6d-ruSQYQSq8_1Q-KlkPrshLh2RstJgDWBJr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇵🇹
ترکیب منچسترسیتی و پورتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105899" target="_blank">📅 21:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105898">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5hYn6ZK9mcKd2BVFwW2HhI7_ATCskDa_Mmi5WqK87BQiRVzJG5KiOZd_ePB5lG_df93HHKQAD2mjX7qtd-VwAjtVIJ2B7G8OKZj537HHxe3OQDMOH4mjv2EIjrrWgXNtVSfStwErTc5dK2I-XbDkYxDQGKiK_3VJJzvuC7n6sL3SMQujyNIKDJUgbKnasmghrGcyrC3DktuQxjmsR2x_F8wUh1Wrg_ezW0BSSAKxNHJWDEYxouhRxcSYd0sbO5jJR6Ke5jYvbGxDGtL7R0-2GLrx9f8JDD2GCC_ul91o4gBZxTb02wkPvUqbj62JGj9TMjQ6eCveMEaJm1NJV8F_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/105898" target="_blank">📅 21:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105897">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiYPz4_77N4FBzE3yF9ndxmOVfROv9dR2r9cUJrJHKej0lRnlE2VtiLiD0RLi0iyiyirVY96JIVKdmRjYzH6ZjXwzplcWcbs6aNrCcmkxpSH9qXtnJMAKvNIc-SoyjalEiVSh8LRxvVLHKMXLxKIGTU8CeaIDRMMlsfmR7gJppHh6QvYul1zQlUvkj7LsnWMx-2GuRpOqA5HSvShWT60N6cOTWEwukY47dtIIFPpM_OU7WUnvs8EVpPsWnMoqlxLtNMpVvjRM4eR8jswG_by7XDaMEIB0_-zUedr5cE8-f35X-DiKAynGqpzDaiU0wP-UBBS0qkF-Sz1lJ4BHYpLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105897" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105896">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy0hZ5_wcRyasZlfeCAHveS0NOBfnYOdPtanlxiImVK1-3qOhrEsCVShdmaEBSThcNeTevHg4PRZnHkH9gu9Pz1UgmnqSCzx3J5uil_GnDh1CeE1dOwkcxf4lhRALSl0dYBl0JsBSyvW3WxfzzVrYFqNyps_qsCUwRS0rKpQ8CfAwmMhgai58dJ8-0fH3vky4aXur6FHJtVhDBVwrRkBMra7IJ3JVQzXCU9KTCpmxflx7_aZjb5g1C8EXhzKWRrRgmEtDQ2sF0muW20j8hRjLbeSS3bjdd9zD6awBss2DWnsTyMb2BjYniJ9Le_aEcJu6au7YvIIDi41fYeUTNpxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/105896" target="_blank">📅 21:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105895">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-KHLnyIxhRmDbvSWdbKkJcitLJSkN-cfT4sSniXNtU9Xsc7mH7dCrHJU8N4czBrTmFmNwHpnVKi_FHdHMxU2uxlbv9z04rix50kEeAWq_mVBWMFM-irnpneHhAmIKzOCJKmjFfPhwc37C0SxMiyaQre8KavHfqPOUzdNXrxM5h_tJCqTq2x-P_PRdHnG7aAiEsP_eoCjs53NsB5fFuucjsJbN2piaZlZOfAqTG9Zi-ij3hluBTo26YVD_PmaeuJeXhWgpoxusV4eqaTE1fl-ScV1PYkTaqnbCHQTXRmNJ9R9M4mxMcnrtOIbfXWnwG7UBqmGHSWQfdQUMxr584rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
رئال سقف برنابئو رو برای خیس کردن اینتر بسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105895" target="_blank">📅 21:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105894">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBxD-sJOne6wJJF3odaGyXxL6YDsyst8rG_YHcR73ZY3FuTliiiE4dRk3M9dnbqfJdzAT9n-NhcoJatFakoGMvCf0gKNceFeTXxwh39WUwl_Tp9PNsCBPx0J_eDWoNmxexBUxUVRnbS7otK00usBW0stWYPiWH82lw9hMvjCpXoMelMd0WukyZxpVKafeDr-1InL465layeFh3UYtbdQK09qEvHsWHMf5cZ3pv_LdmLgbeAg8OvcaNkIrNdAfekGvSnE-zaDMPwrI1dJzbr1JoH15J877TajE4yqBIiMKF3KQkVFVov9_n4HQP961cPQ1SBleyMY0G8BMJtzkU7pTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇺
دیگو سیمئونه: خولیان آلوارز جایی در ترکیب فرداشب تیمم مقابل لیورپول نداره و باید از روی نیمکت بازی رو ببینه تا شرایط روحی و روانی درستی دست پیدا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/105894" target="_blank">📅 21:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105893">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d57gWs3hVp4Tufsa8rcO9TbwLFEiJ28SMjNJeLH10a3MKde5Dv5pvStJvgFZXR-wQcpaHqDIXceArVhlpVK8fLlL351cdTebwVrQUNsEyfE7z6F_HO55mvvtoco9l4jeUmMB5M7mfsGMVpZiWmwEUcZCACh0HMwn0JX2llK3ti-4mGHW4vYy3F-iTqf5Wu131cHP1vdkzP_RrjXwMSahUnZeOWPXWPSmdtQRBuKZ-UUAR3lXx12SMYt8bA8zA_Ubh06mYAIXU_P_nrSMZ3dGURBlejMkcSgiM83TkvA_n9_xvDkZcifWg-I3Tmi-zD-YgilDU1WCoLw7Xl-uxKJt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار سال ۲۰۲۶ با باشگاه و تیم ملی:
🇧🇷
رافینیا:
بازی: ۴۰
گل: ۲۱
پاس گل: ۸
❌
نامزد توپ طلا نشد
❗️
سادیو مانه:
بازی: ۵۵
گل: ۲۴
پاس گل: ۱۳
✅
نامزد توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105893" target="_blank">📅 21:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105892">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bc3d2a35f.mp4?token=XRTUUj0T-r8MuqifYvRsccdrjhK6LUou9lD67Ew_icGbBTJZNNQkz-SZjcL9fooIT-aWUP4gm1CbyUR2K5p55Jjs5eZZgd8MnkCn-vH6oSGAXzchCEYnhr1mRurSt-njGn14FZCUwNyzsqVzVe-AVf7OXgc0hEjZOjKv5RBpZLBKBsaRa5wiTqdOojHdUNS_FRbL7gOayWYK_Cji6abvt7Crdwi5pvep7ed5JJLsNyXdNiWVnufX-r42kc6SoNLDgJvbjQbMzDQUQxzmpiU5PfoP_WksMA8-PYsxrT4x5aUheFROmiVCULP-sOQbBalbY60-Pbe2xGu4Ig5hPtFivg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bc3d2a35f.mp4?token=XRTUUj0T-r8MuqifYvRsccdrjhK6LUou9lD67Ew_icGbBTJZNNQkz-SZjcL9fooIT-aWUP4gm1CbyUR2K5p55Jjs5eZZgd8MnkCn-vH6oSGAXzchCEYnhr1mRurSt-njGn14FZCUwNyzsqVzVe-AVf7OXgc0hEjZOjKv5RBpZLBKBsaRa5wiTqdOojHdUNS_FRbL7gOayWYK_Cji6abvt7Crdwi5pvep7ed5JJLsNyXdNiWVnufX-r42kc6SoNLDgJvbjQbMzDQUQxzmpiU5PfoP_WksMA8-PYsxrT4x5aUheFROmiVCULP-sOQbBalbY60-Pbe2xGu4Ig5hPtFivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل تماشایی آاک‌یونان به لاسک اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105892" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105891">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a209d7f89d.mp4?token=H0p9s8KaPddUmUB_xCLnLN9e-9FqNxw0ooQes3yNYZ7FDlcGKLTAONkR6ChxO24DMo5Tzi_6c3TF6DIg82EXqPGCJLNukaynK44y_Td6k-ZFsYhJj3IbtK1ihbYj0Yvmi-7iRMb08l_xlDKq6ga0NI_RGSqR8a4n-iCGCnvKfio6Jd5eToiK0S5hWyKiH4WTlz2JeOJhUy7u3Hq8YP3cwRENu55qB5VAsUXVcS-DbEoDS4_lxyOwdCBUgmtNoMDuYqECMUT7RTV9dexe4gVkLl6IESKwxyOjRNqpyEUY-1pc9GCpADsSitM6IOgvTHMSiBN5g7-vgwxOgye3Bd08-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a209d7f89d.mp4?token=H0p9s8KaPddUmUB_xCLnLN9e-9FqNxw0ooQes3yNYZ7FDlcGKLTAONkR6ChxO24DMo5Tzi_6c3TF6DIg82EXqPGCJLNukaynK44y_Td6k-ZFsYhJj3IbtK1ihbYj0Yvmi-7iRMb08l_xlDKq6ga0NI_RGSqR8a4n-iCGCnvKfio6Jd5eToiK0S5hWyKiH4WTlz2JeOJhUy7u3Hq8YP3cwRENu55qB5VAsUXVcS-DbEoDS4_lxyOwdCBUgmtNoMDuYqECMUT7RTV9dexe4gVkLl6IESKwxyOjRNqpyEUY-1pc9GCpADsSitM6IOgvTHMSiBN5g7-vgwxOgye3Bd08-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇺
اولین گل‌فصل لیگ‌قهرمانان اروپا؛ گل اول تیم استون‌ویلا مقابل کلوب‌بروژ بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105891" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105890">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqPGviY1xikDEVtjIbQzIAFNpwTIL4GfolwXH2qUl2nrAVxVNzRHfQPFBFJsylgQOGgxN8B1yiFgIrwN4wc4aiP0bhPxTe98vTnUPcbBmjv1-z6BQUzculQDjp--J4V-YSvQ2LJr8GE8tJMc1AyAnuiu40EyTXiIp7FqVKKSXoHEtEcKicRQQeDYoeGJWfZE4xyHvGoEdXJOjD4N-f4VSDZ6b95d29zk1N0N-005WztjU508mllPIdgAb1jd2Y-gICtf2zWb5J0NJ44_C0SQCBzvJtLalupEDCjTBK2KrOGTL7lO-aIOoCashqirUGOPmjokYKAWFZCPXyfMJASHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
غایبان پرشمار رئال‌مادرید برای بازی با اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105890" target="_blank">📅 20:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105889">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC8PdzKnMskI7OARpVf1q87zKBz_9Vit40w8HDxmNj0zHxynjxzPYtzLwHjHe9xN6_4-oNFzOR8trNMNDINbO8D3u2aHK4HMlV7ZdSorlJUIlAWonpBb5Rpvi5d7Y4zP5ESlS9DaulK_2EPoINkXpxjjiLBMu0EbXNpkraZ7Peyj8pF9Uvux25glH7ZHTLkAFzfp_Oc6HkaGJmnB1rDsg16RT0wIht6MaV_HyV-6Ps2XoHsYfE8pIi5aCMoKUPIEPCvNu4EKDcCUMgYOaRi2UZD9RxMllPglaarmsnZY55dIyhw6kjb8pIqTwW-tzDEBSVKhfjmy_hUDUpvyAj853A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
محمد مهدی زارع مدافع پرسپولیس بدلیل مصدومیت پس از تمرین ریکاوری سرخپوشان در حمام دچار بریدگی پا شده و ۸ بخیه خورده است تا شرایط حضورش در بازی آینده پرسپولیس نامعلوم باشد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105889" target="_blank">📅 19:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105888">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7IgZpxy-zKpklGaDS0hziMfRMpDE792ARifx2_4pNt1uJDjQJ9QTVH5cWVhuG5borWhDy2SFcOz7pZTkcZ_tCiZ_eny0jvLlOHfuYpfC3XTH6--RQk6t7Rw6x5dxyd48g1Sv_wvXIjpoOnFlOLv7Z5WMEecfswb4_B2BtOPNSLS12D_gTBCTtC1m0zkSuUvZ5wYmVC_MAF0Nc5JbYx2Dp-EsvG7kbop15b96zdVJzQdDqLwwc7ou4-ZGY_8rl4ogZGfkPGfsZlzX_nbiekCch-pg3lWeSnSZm5noka9hyDKc3_X-F3Bb2LqlypU3t0W-qv24HVNK0IxCohWq97Y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
برنامه‌مسابقات‌هفته‌اول لیگ‌قهرمانان اروپا؛ از امشب تا پنجشنبه بازیا برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105888" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca32d4904.mp4?token=jnBLmwYY06z1cc3QscZzjZiSh25pCefjOMdvzDL_7-AvrJjIZylqNvlGaxNAXRAV8IYy6mC0ssytkC_Y0UiCIl_NkfJJgAtukWc3E_rI7X9IBY7PPWkTOpfyuyNAsVzrpLC5yk4jeGAjyTD1SaP1TYMzw3HjQa8M1uLLP5qOEwXfxrYK2qfMmj9qkDl1mDEiAegyc8jCYcytIMux-Uw2omW4BPVTC18sf-t13hdyqyw7vL9lkrUFfs_oMdtdjsrMHQNqb8RBNc5Q_zWFs_x8hFCqGFYR_TmT_FGrd8pxCQQIZYzBRd9bsvEdKwvP0FEXt4fXx3-Da5ayVPU7VUt3yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca32d4904.mp4?token=jnBLmwYY06z1cc3QscZzjZiSh25pCefjOMdvzDL_7-AvrJjIZylqNvlGaxNAXRAV8IYy6mC0ssytkC_Y0UiCIl_NkfJJgAtukWc3E_rI7X9IBY7PPWkTOpfyuyNAsVzrpLC5yk4jeGAjyTD1SaP1TYMzw3HjQa8M1uLLP5qOEwXfxrYK2qfMmj9qkDl1mDEiAegyc8jCYcytIMux-Uw2omW4BPVTC18sf-t13hdyqyw7vL9lkrUFfs_oMdtdjsrMHQNqb8RBNc5Q_zWFs_x8hFCqGFYR_TmT_FGrd8pxCQQIZYzBRd9bsvEdKwvP0FEXt4fXx3-Da5ayVPU7VUt3yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خاطره امیرحسین صادقی از شکست استقلال در دربی با گل امید عالیشاه و درگیری شدیدش در رختکن با یک فرد رده بالای فوتبال که منجر به جدا شدنش از آبی‌های تهران شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105887" target="_blank">📅 19:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105886">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59df1af51.mp4?token=J-NhzeiBXIfsrBzVBdMsq1d5sqbuXfIbtTZ8abi9w03_mtf2xr0W6aB6LjQ52t5k9n1FeTSXb8kMZ3U_CvR58utfBNKWzZig8k7V2UDie-RJv0zbwnkge4gQB7Iv7Ywk25XMSCONGO46QX5slQwXu6coTt3BF573z5FRDg8SbZLIwimJmMNWAqawFOzaAQD7q9NHCYe1jXguygbUjICyYK_8U5pdSKqzIxX3oTFgh769_smg0zuhV1fEEERzVulagypBDvbKZpebTZp0L3XkadnbWUjSK2h0kjZBzt06tFiDNydCt0WKuUbMr9A0rOA9Pe3L6Oi-ExNioSIPPKoEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59df1af51.mp4?token=J-NhzeiBXIfsrBzVBdMsq1d5sqbuXfIbtTZ8abi9w03_mtf2xr0W6aB6LjQ52t5k9n1FeTSXb8kMZ3U_CvR58utfBNKWzZig8k7V2UDie-RJv0zbwnkge4gQB7Iv7Ywk25XMSCONGO46QX5slQwXu6coTt3BF573z5FRDg8SbZLIwimJmMNWAqawFOzaAQD7q9NHCYe1jXguygbUjICyYK_8U5pdSKqzIxX3oTFgh769_smg0zuhV1fEEERzVulagypBDvbKZpebTZp0L3XkadnbWUjSK2h0kjZBzt06tFiDNydCt0WKuUbMr9A0rOA9Pe3L6Oi-ExNioSIPPKoEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشتِ یک قاتل خونسرد به لالیگا برای بردن کفش طلا.
☠️
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105886" target="_blank">📅 18:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105885">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyGOy8MNHj6d0MEJJXQczok1vBHZTuaiGkb6kl8igBlyuL87aRSaDm-4-Nz3njJ-rho6twj84rKwGGtvzmkY2m0m0JjwCj6QrCDY7FUcEKfvQ1RKfTvgO3DsGdOqGg7JcZeVpt1HQpofg1Q_gexK9tSWVevWbIf_-_-erXbGK0QrYfsmI0KgaX5w4OlWfBkwv7QF5LxOa6r_6_7XgRPiNfoyylvSsGMzjDGkmJJS66-N9C4PSxo_q65clK_xkZwhOX5eLDvt9YV7OladSp357IMkocYJYz21M2hRGtg5oSzjfjLYZWG7RkcUC2Q5cN5ExVGPD85oRYg2Lm_YVbDysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
فهرست نامزدهای توپ‌طلا مردان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105885" target="_blank">📅 18:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a86823169.mp4?token=iWluwc1Xji224NXXOKUVGEMWPe6IMHOS1FO6aTGfoq0f4BQGvPN93BkCMPdTHUCE6oM8s9c9VAQeW2uSHc0ci3S2h5EsMMBhnvpQcRCM8nERANv3j8Ywj2_x9bOZs_m5nGqCKsqDblQ_St8cKZ6AvgMXPjEouSWdEhx8Av_izANuJR-zV7IeONA6G9sDXehVGerOhkraee7prKFeJNQ1UjvdnP43KLmcE-LSs6Y-5OHT40ZZ9srRCo2Q0gNJgldFhS6zcY5i8UqXUOhDjdqeR4HWZrjNF5ObmEvA9gTFZbVzpJAazjM-aIR6nK8DYY7AsLYXowz6a1jb-ztGCVO-sIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a86823169.mp4?token=iWluwc1Xji224NXXOKUVGEMWPe6IMHOS1FO6aTGfoq0f4BQGvPN93BkCMPdTHUCE6oM8s9c9VAQeW2uSHc0ci3S2h5EsMMBhnvpQcRCM8nERANv3j8Ywj2_x9bOZs_m5nGqCKsqDblQ_St8cKZ6AvgMXPjEouSWdEhx8Av_izANuJR-zV7IeONA6G9sDXehVGerOhkraee7prKFeJNQ1UjvdnP43KLmcE-LSs6Y-5OHT40ZZ9srRCo2Q0gNJgldFhS6zcY5i8UqXUOhDjdqeR4HWZrjNF5ObmEvA9gTFZbVzpJAazjM-aIR6nK8DYY7AsLYXowz6a1jb-ztGCVO-sIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
محمدخلیفه: دبل‌سیو مقابل یاسر‌آسانی با اختلاف بهترین سیو کریر فوتبالی‌ام بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105884" target="_blank">📅 18:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105883">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwKN9smNh7vgP_kjKhgC4SevlvkkZiSLNsuY1J_U1nPWXilnLUh8Uess9yS5VarDdCWmIfMuYX-zBdC_VgJC1rrNx-IkEO_aGKVhhrcvfEmhZassWUAgOCBqM2jspj2G7MuwlQatC6cdH3wnGicJDfRKsyXjVZh646Td5Fl-5MAM39Ybj3fpXIy87mVKgON7Z84T0DLUH8SZTvRwc5dMeiMfB2n_pTw3K7mFPiky0tOF5YnKWLICk1XxXtoFfahUxZ-pkVneyqm4lPz0KcOzuK_JUalyMQ-Ls5svw9N2KG1BmyftYGhhIvWgiUdZ57bs5OSroSzVY6clgChtiSnyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
پادشاه مسی نامزد کسب توپ طلا ۲۰۲۶ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105883" target="_blank">📅 17:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105882">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105882" target="_blank">📅 17:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT9-vF0dzd4hR92gkKy_2F7E5x63NNcScOl-bTUvWXDgvAUFmIz7htGplMh_nKpFtfVXI1PxmN_aTHlVdUHlezfH_fCf-PMHibysb2lUp_5_xGicFH9mr5UZgZZJIDq607zM9aUHJHE1_DXobRePnzGc_gaVw0ed5qdEKEvXDe2CoapA7asOB__i6VzQYien1kGPBqtZVKMsO0LOBnkFQhPGMUw-CimzVGNrAwS_RxlEO81XYIOKMOgVT75cbOpc08jP9Pzr5N1Am16KPfnqVla4DZ8askTrwgO6ts3pT9LyD-6Uf-_AGC-Klr--fkoBCHja1xoCpC8fvxY59wu_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
منچسترسیتی
🆚
پورتو
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
منچسترسیتی: ۴ بازی، ۳ برد و ۱ تساوی، ۹ گل زده
⚽️
پورتو: ۴ بازی، ۳ شکست و ۱ تساوی، ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105881" target="_blank">📅 17:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105880">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG4xPk8nYlVUOldWIh2AX1x83uFc4QVOAZuYwCncDzCTkDyxbhGsMT9J-49t4GWQmn6nNxflKSm-jdT5IuF7lTVjB8o3X1_XIQYYGJwdFjsJUqEFMqdpjia0nDmMNQfVjVGKM5ZjnPm58akBIX7FO21iK1Cemmivmq6IiNKvXGyMBv6_XWeyBPP6PJ0EtqSgFxhddLDVqb8DEke_V6mXm1QpTrZUL10JSmQSiNngZp3IkfO6qDivACACSwEiuCcFUfxgguXr9OO-AN6FHoI10UqExtnKadFlzGo5Kl5Ijq2QhSHmp52NdlCHiPStcYPWkj4E9bVSZ5_ySP-ZfvfDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇮🇹
ترکیب‌احتمالی امشب‌اینتر مقابل رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105880" target="_blank">📅 17:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105879">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqmicQoVY0T6peVmCCFjRe_h7I-e9Zab4WDjQ2aZwd3T8Qvof8ytLjtpDRpaG9j8D8R_fAaiC0sfDVnGBP7Nc_AL2xzWnHxs3TCY6oEJ_FBpHO3cDWqEvcY_kiT7f2Ia7Z_IWXdoA7FP-aS5m49TBbMxa6KjIXEULxmy8hdYOlUb2dAqCIgszNOr3UI3H3RWv9BEfunCVngC6GEzhBS2-DI82o3SNzBMC0nmVhkdN5ff4OyC4CANO75eQJc5C2R967E5d6LgM-vZZDeAeQ0Vjcw1kHTIappWXQVE-ir6yB1vaREIahKmnJo3-UTMmtmRh4knDE8MR_OutECb3es6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🏆
نامزدهای توپ‌طلا ۲۰۲۶ زنان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105879" target="_blank">📅 17:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105878">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTNMoZMJ1yvPvdN8hDOncoDrnqkBvKJ1UeTCXBRKrTSapt7vbLu-Rf1XMxYb6zSQDucKfG8MaDnmvwbgB4blER5kDPDEgB-SbZI3dmcLyPNR0S8wpVKPtmqTcLg2MekWOMM1yqSnkAYmkfaH8W88IvgJwdNyNbZRgalIaG0OTuR1-RUYxA4akKegPGiiQtScH0hRiJ24DG2Rj0JtDEc1Xakx7wyMLOm-phYZetff9x0mhwbUPxiiUUv39oJnUYoLPttJe1AdHiPd-zV6MtXgVt7aaQNkfAvR63fE2gJgMmV3i05SWj5iMpO3ywE_dn75f9DUXtKkWV3GUL5EaQeIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
پیراهن اصلی تیم‌های حاضر در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105878" target="_blank">📅 16:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105877">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8991c045e3.mp4?token=ZBUYtAsJCFFsseT9XCzERDnWcnNh3wimjrNER7lPR3gv6JRDIVtGG4mHsn-vG2XV3DCxMzTywbBXIM59JyaWz9qZ6PdV-SdeODJOAb7y6PR100WGkZ5J0eyoDU9vW2jrJspy3ye3T6urCwCLCp9myeB7ROgEGThEdsSJAq2Bbs5uanEop39PLNMEn5WwVomQD9gbIeN8MuYHNq1nq3d8oPwoF_PXz4iM23wddY2dw4Ir0FY1d7YW9f-R69fbiMHPef4_dOit4EZlAkFOWdv_7ddUFE2uR7vEzvNIgQp9mnbg61TlvohfhbPfTXLCtRSmrXLBnmehbK3_2pDjSUDVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8991c045e3.mp4?token=ZBUYtAsJCFFsseT9XCzERDnWcnNh3wimjrNER7lPR3gv6JRDIVtGG4mHsn-vG2XV3DCxMzTywbBXIM59JyaWz9qZ6PdV-SdeODJOAb7y6PR100WGkZ5J0eyoDU9vW2jrJspy3ye3T6urCwCLCp9myeB7ROgEGThEdsSJAq2Bbs5uanEop39PLNMEn5WwVomQD9gbIeN8MuYHNq1nq3d8oPwoF_PXz4iM23wddY2dw4Ir0FY1d7YW9f-R69fbiMHPef4_dOit4EZlAkFOWdv_7ddUFE2uR7vEzvNIgQp9mnbg61TlvohfhbPfTXLCtRSmrXLBnmehbK3_2pDjSUDVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
پیش‌بینی یک سال پیش خانعلی: تنگه هرمز و باب المندب را ببندیم نفت ۴۰۰ دلار می‌شود
پ‌ن: قیمت فعلی نفت ۹۷ دلاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105877" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105875">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEoGK3PJBa08ScyTsLQu3EHWtQk5vIZqcpbSXjckvYAg9LdjtxrS7m0tWYcd83KUOqHy8RylpNduRpNLe-U4xlhZuRrWinLlPISp0O0Uo-hUADxK3oFxyqDPlpG-uMtFCWtbZ8yfsQsY5bK3xeheB5iyhqc73aJmyMnj7dSyc22oVpJ6JSV6UK_X54X-RzT8he4XaUEApSiC3sb1-Ia5o6_Jw4di7GxYJjeAjRPyCKCoRfk4mIHXsh6JlU9SQItkJbdf2u1rBRyk83Rolrnxe46lqeYpt9DM_XrNdKBlELZh4pQGWTxZodriFvSQbopgRmIG-SB3UehIcrH4lzacGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mbiu_fzaRTNDVNonC2uPOQoCNa1OiIPsAMWbjG1R1kCPElyYNOptbMCkT4bvB8Ec2bDGc4tqoKSUNUFBD0OSz4BYjmSxlmUbtWPPovqtUo94QwpNpAWHWN56UXFtxjDlSWdb3sFBMRknG2Ginq7g_6FPey7q60DmrYAIXs3iLjSlAgFbVsLv_fNO3UCzqrg9VF-fdKmx7P75MoQGQTMDhEuGAWRZTdlSWswUx2mzPkRzNSWkOsWMJgC9aNmlRDWOOnkYjSQ-qPNe_vy7d9V3t3HONdPqUtX3gqd7FxSo2PyEPrsvA_IHHXwE6rFK3rHC5VDdgs7yf6MeAQvm0gWtiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
✅
نامزدهای جایزه بهترین بازیکن جوان سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105875" target="_blank">📅 16:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105874">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325df9d92d.mp4?token=uO5jShSX66XSKdrhDgVsute7PyJb0T1MvaZPhbXEkYHX1elQVwBKOYG8SkwDh-PxwPSmAj8DBi2C99NONcSByOyVZoMdDH03GXU9g2LtE_0SlbaZJ2ktW2PhMthczLtoTQUTjTUmtzLSQiZVlNrWEpz3EGngBct1r08phxwogjdCViIXSEkHiEops0jMSGi1L1yoSmdhEd0BfOg_LjSJN-DkCiAwUV4Opyty_EWU1JARyn4vIEUx1zSg7N5pNVbljyUOxcdsyi7C30z1ng4ljaYjLg9tJb5S8Ii5JEtjjDV1xZdJPss89N2uFMqiqPoh6CWKsehKY_EANm1xN_eDVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325df9d92d.mp4?token=uO5jShSX66XSKdrhDgVsute7PyJb0T1MvaZPhbXEkYHX1elQVwBKOYG8SkwDh-PxwPSmAj8DBi2C99NONcSByOyVZoMdDH03GXU9g2LtE_0SlbaZJ2ktW2PhMthczLtoTQUTjTUmtzLSQiZVlNrWEpz3EGngBct1r08phxwogjdCViIXSEkHiEops0jMSGi1L1yoSmdhEd0BfOg_LjSJN-DkCiAwUV4Opyty_EWU1JARyn4vIEUx1zSg7N5pNVbljyUOxcdsyi7C30z1ng4ljaYjLg9tJb5S8Ii5JEtjjDV1xZdJPss89N2uFMqiqPoh6CWKsehKY_EANm1xN_eDVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
ابوطالب یک‌سال پیش خیلی قشنگ کفت؛ تا سال‌ها مغزمون راحت بود اگه علی دایی اون پاس رو نمی‌داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105874" target="_blank">📅 16:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105873">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
❌
🎙
مجری شبکه‌دو خطاب به خداداد عزیزی: فحش دادن شجاعت نیست؛ و خطرناک‌تر از خودِ توهین، زمانیه که به اون افتخار کنیم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105873" target="_blank">📅 15:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105872">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/218de47812.mp4?token=WR1YyFOhXEAzWAsu1p5-72OqkLyiqXmPL9xcKqOSZnssoF89k411vImpcOx94gB2d56WmsMq2wdboVGfffx4ZaxH69cmWVUcFRSgsAGOOor8krY5ja1yFyyB6-OE95efDSB2mzObdILyPDI_3LvmM_slQSq2IR98o-NSzu2UpWsOONFAJs9IvVFshplRbUnDYGWKQBSZySgN6KFWa_vpiw8N8wO1nIa6AuMigV974dK9kGSP0MI23Jq7xiL9HUEc2yGUBsC-3TIoQp9yvXrHf9tULzjQwktM6QzdrXvxBytw0sWA5VjdHe705b2SJeYHzYlEk7xV5FFW9RrYkJWaQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/218de47812.mp4?token=WR1YyFOhXEAzWAsu1p5-72OqkLyiqXmPL9xcKqOSZnssoF89k411vImpcOx94gB2d56WmsMq2wdboVGfffx4ZaxH69cmWVUcFRSgsAGOOor8krY5ja1yFyyB6-OE95efDSB2mzObdILyPDI_3LvmM_slQSq2IR98o-NSzu2UpWsOONFAJs9IvVFshplRbUnDYGWKQBSZySgN6KFWa_vpiw8N8wO1nIa6AuMigV974dK9kGSP0MI23Jq7xiL9HUEc2yGUBsC-3TIoQp9yvXrHf9tULzjQwktM6QzdrXvxBytw0sWA5VjdHe705b2SJeYHzYlEk7xV5FFW9RrYkJWaQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
یادی‌کنیم از روزی که کل‌ایران به هیبت و بزرگی اسطوره علی‌دایی در جام‌جهانی افتخار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105872" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105871">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ8-3wD_xHaaosK1tNIdzUGea9iRnN3qEiPQGI3gkQ5ujXhIbLNrRzeG7Irj-kHTs2GOv85vS69Dks6hT2Nu6k6ikRyEFGQAILyR3NWfIHTMhht2NvBfCJZWxdIVw6GhNk4RpuuffLvKtO_8oixcU_gexcKp3GKlYjsppVJ-OGMhdcl2PlUYCvnpwbRNdhKEkUrHFIS-pKS76LwdzTdHXNUo7LXcHlWzhlUzXtNrr4pgiqvon9_55o4IMzxN3BfMur3vcFAUAvt4yld0f9dgSIN8eSX7GzSFczA7eXaqQPTDmQYbmm-lCV8w0w7bBQpBgxfWT66WKZLJhuKaNKUNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
🇮🇹
نتایج ۱۱ تقابل اخیر میلان و یووه در سری‌آ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105871" target="_blank">📅 14:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105870">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUwfIwJeLpVK54YvwFA8HKwvWgBWay7ClP80c9F306Gk3DrODfR3RO7Q1pw5wBra7GwUQJfYjAxoSKHmql5Z1ls3ydh7zwb6pPchkhEqzIpE1nFNmMdboScJC9ZGjFcA-KRLGzCz2goQ0U1bbPpv__zEOnRbgaujdnzm8aIGQr6g20h1M1M5d7tAFOLI4SE1wqdt54WPBvj2HH2Y92tJYJnI5hu53m9xp_BjX88Fwx4gkA2c-mCkqTCMj12tByqNKlix30EWKvBm77bHHaCgpPk0mUoELPXXS9Nbsv7goDZPKxukKlr5DfCywBZx_GeV5ZMwLyaN_0JJ9B9s6s0SBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
لیست نامزهای بهترین سرمربی سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105870" target="_blank">📅 14:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105869">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFCLVjcBxyrZYHkppyjneRCswgbCXfz_JOS5frY6QCn7Tg5ISViObgPSs4Jo2aWDJHvYhpikqaij0tHsZ6A1ZH7IM5J_SzJlL6_rUx9oST5UrMG44hhEgf_V8HjWdFo5NGyoEp1cz7F3uncq3hoVoHP2W68llwTi3MgvkdvLLI6mBNxG-WkQHXSU4JctIsI0FSuJlS31-ljbD0fPiziCMxLPlN50i_1clDTL9kre-XI6kyJMf4IBIsE0aGqmuJEQZ3OimYYPDmpb_ye3gFVGJXErXCCXv5GSYn8kiK1TWgKkRDfbvZIOrbAZfB2sM3r0HwCKa3jtELO8Ubg6WAE5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتایج سه‌سرمربی اخیر رئال‌مادرید مقابل بتیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105869" target="_blank">📅 14:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105868">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc23hugvWBvhfBoR8xCxuqFbIuOKYmXbPW21I5iQKRtYEfWFHbKIvW0BRXH93WthbKvl2qu1_Hq1bA27XbUf-v8ClvNHoHWDEtnFeBstgczOCdt5G_7c49M9hfl-NoeYe9jJXND7qB_ALMT1CW4fPkpvzPalfMudI5ET3x9t01STgSHkLTXcvh_o1GNu2DbS6ojLi_kuTbBbyZrYvJHvwJc12azXAB5NObk1uBcpi9IF4WulJvK6EY2G9XZr1Eg93bBl2me0jV-tkCjwQXhy6E_x-WgdzWjdkBjwKSXsUoUGaBmZeLoQRISVZInepXGJCsv6MQQKICC8REkNnLoJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد خط هجوم بارسلونا در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105868" target="_blank">📅 14:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105867">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkX9dqEUAHbiuwmHZUmczWuzvTkO7kId3cYfVA6fWyDkoNSXFy1cF8bFzjdXwxWXbEbOhwJIW3V8IVFCLLXz-7pEWhIbIZPwMp0VXwmNFOTWWkOA--yEyES7ainpoVsTCdcreID1zz44fDUrkJ-LWpRueqgELtCpi3ZFHuwKZo5axjW8KUGaXRFFoGBpxNKxrLYZo0qnA26DZlnD4Od0QchKOXS6vV5UIDoQQV1-A22VbizuQ718JEJaJyDddqBArvIdhe8Ogpp6eY5MujVk6b-nM0Pq7h9yMhPYPhmAsNfT2BEZPCMOwEC1LxhgdyG87Xc3nnn2UJOexljND-76ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
🇪🇺
لیست رئال‌مادرید برای بازی با اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105867" target="_blank">📅 13:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105866">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsS3E34ucbd0d-vQ4D6YMKCiEZOj8-sUmLYKbBxLrFINvLFZL6JRSmgK70uMY-DeopaZkRj7OusKMhTe4xkj3iHSauwbbMkI_KIYF31v8EQtcSG49-3DSnUgH7I9ryDhS1abQ-XN1eoO5FURJbpMQ6yZ93jJaEk8axFTrnRbxaQRQsfsddQ-qvKMPKJlnxukn9FfX89DuiOhQe0jfkBEJJMRL_vim4Fa_uS2ePrjBpLA6oZJIcKZpKFzkESI-IAsNe6VgVBKOps1GnQJCSETTlqLmmuY7FCr1Uy86yJhJejCE5qNvfiVGcmm968sNpzKkOBAoB2owD7NoP9bXDyZQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏆
🇪🇺
در آستانه آغاز لیگ‌قهرمانان اروپا؛ نگاهی بر بهترین ترکیب تاریخ این مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105866" target="_blank">📅 13:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105865">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImTkZUUXmiuY7H68ia_xTnuSzYlJje9gXW8qgMY0NovsVlqoef0tUD6j3EZlGcDbmiN3m8xFeIwqlAeRuEyfHMeVRA1n_XhIu9q2KZOKMOQdR_F8_j8t7vDDWpLeRfD3IyQluSar7rNnvY0EV-clOuaD6vI7TAOcFYKpl3BRKTV_upRitdnIts73IPmImb8sVFmz7qXfgg1DvxAVEI14S55uK38fpekVaQ3RM2Fg6Zt2tzEfKjI3ZOgCs71gR05K2HLth4oc1FmdwkHqJLrgB8nlvxonDOAYW_-Sy617IFhMoZWYhG-Ypjskm4w52P-5oJ2LduphruPRretqJytdjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
نامزدهای بهترین تیم‌مردان فصل‌گذشته:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇳🇴
بودگلیمت نروژ
🇧🇷
فلامینگو برزیل
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105865" target="_blank">📅 12:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105864">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇮🇷
جلسه کمیته‌انضباطی باشگاه استقلال برای رسیدگی به تخلفات صالح‌حردانی فردا برگزار می‌شود. حردانی در بازی مقابل پیکان غایب بوده و احتمالا مقابل السد هم شانسی برای بازگشت به تمرینات استقلال ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105864" target="_blank">📅 12:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105863">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou9FoE_hlUSsRvDMgUmP5f3JpMO-RCN4uiBa38uM8PIZwDPEbQPUqTEeOofTrWb3d1bESSPXDPuCd-_2mf7M-LRnZN58NM-GRFKqT-xFCGNr4Z0G0P4fHGuFevDhkXxnsDbDkKRoGjtzGFwQpKjuKSzG_TFaVmQFhWbWlnIy22MwEZf9F0oColY9mhrRZmhkr_vX0BUcxgbFomCLralfye24NUI7VU0RPWtad6nr2nVNui4cX8Z2impH7jSmFhJGHqYrBTzaVI8IM2MvRjW3XYXgW1qVTIOXmANMx3oJsVxcwVNjBJW5dOXxTorJt-r8TR6k8dXLBGoQs00yBrnBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نامزهای کسب‌عنوان بهترین تیم زنان فصل‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105863" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105862">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🏆
آغاز اعلام اسامی نامزدهای نهایی جایزه توپ‌طلا؛ ابتدا بخش زنان معرفی میشه بعدش مردان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105862" target="_blank">📅 12:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105861">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5n2dW4eeB0uP3ye3apFoxs_uB-t4X_YF-_wLLxE8FOhwochPWSnkMg5kC9SQP_Y2s3vPOL1QmkqJIXMZbcT8QtOh-TsGdenlr0TLSs2Sb2LpZJp5nzKTaOWjgWh5UWKCa4IOVi4UHoY0qZfgvvFWxqsmM37pil75mmdSqI80MFZuq2Tm39jg9IL-jHR9IaMi-YXWb_dzYKxDCjv2Ozqh8CSeOfVEMfnIgwjVqQ_wWWBhQp-ajyh6tOmHFXeBw3vKHh3MnOJdN21T1pVt6mndT3Vs0DLsx0kJjmv_dmWIDdA_vb2IrEbvxiQh6eVYBXaRylxnl2ewtLK3_RJ6BSdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
آرش قادری مدافع ذوب‌آهن ۶ زندانی جرائم مالی و غیرعمد رو با پرداخت بدهیشون آزاد کرد. با این ۶ نفر تعداد نفراتی که این بازیکن طی دو سال اخیر آزاد کرده به ۲۰ نفر رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105861" target="_blank">📅 12:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105860">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3601cd12ba.mp4?token=bJqTXVq-1gAh7WyRkaFuTuSsHLCCJRAQwyekOhRNwuEwEGUyzsTGhrubv3ZLXvsGSy9sp0Fwexbvzx2JLgLjuAnun0VT5AiaFTD4vByl-3PYO-JMaf1CguifldISB-tglaCPdIhsklsEL0S9oPoD-AEVOsjydU8ts_JxqKBd4g7Lq6kemkYx45pX4LDq3-GiECsEQ1ehsQL0iEsYFBBSvykkPU0O799jaahPV5XRbYyYwuNRynuQhxs0zhQU8DKJ0UdjLuyhp0htb4mu1ey1OXZpZWv_j1EPaeREjGj0scLi_a9HwvJczsCRzb1A_FzhE9IcyGY-nrskrt6TIpCzuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3601cd12ba.mp4?token=bJqTXVq-1gAh7WyRkaFuTuSsHLCCJRAQwyekOhRNwuEwEGUyzsTGhrubv3ZLXvsGSy9sp0Fwexbvzx2JLgLjuAnun0VT5AiaFTD4vByl-3PYO-JMaf1CguifldISB-tglaCPdIhsklsEL0S9oPoD-AEVOsjydU8ts_JxqKBd4g7Lq6kemkYx45pX4LDq3-GiECsEQ1ehsQL0iEsYFBBSvykkPU0O799jaahPV5XRbYyYwuNRynuQhxs0zhQU8DKJ0UdjLuyhp0htb4mu1ey1OXZpZWv_j1EPaeREjGj0scLi_a9HwvJczsCRzb1A_FzhE9IcyGY-nrskrt6TIpCzuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سون هیونگ مین در مقایسه مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105860" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105859">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105859" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105859" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105858">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_kncElhPLN_R0oqiBcdpXT5zUSN4MtD75h05qkH7Iyhbj0R3F4UEJI5uxOOF33umyklZNqhRoCt_567VxN485EWKWe3a9_LIC4H5qxW2UwNFAsjMa11t4cmY7A98v6DQGKmBSt7Nr3iFdqoeiadazAFeCwrNWjxENVYXJ0DW1A1UCSOXPqQGgbymRvrpke2DnR1ZnCCmusDF4HX8yVx9DqqRw_xlpP70u3MvthP97Ty0PgS9kKaZFqnhDnWwL1WZwiuxt-6c6d85yg6GEFj4-b8yKOnprkaUo92vM5mpFyDnrP_9kQfTeOvHaPWvqKlsR0idr4YojtGEVuI_MI72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105858" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105857">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxm0HiQhSNV274F9AZab4HT_OHnIitUNsklq3ey4Quea_YWGP8F_YXUsz6lXu_bkU6PdD4OT79jUt6rsR_yE0NSQAWvpPDWjfrbCi2IBI431s69CPelZ5nmB22NdMiL_W30al7GYwPNK8SLxoqOpbHr_equQFMhhjY4zFiLz6rhvk4dIkRKDvVUH49nHehNMQKp1lYwnyGtzccGS6dApuCq3aL9grYq14WklBEkiV0BnrpgEBK-a2s9b-LjGn9PfNoiNdoH47oyGjshGQpK4uwYc4I084F-t4ujQVbyG9_G2W4IQPyzKqXMhAQ5h-1rKT9_c5U25bs4oNPo47jLcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
🇶🇦
🇮🇷
نتایج بازی‌های اخیر السد حریف هفته‌بعدی استقلال در لیگ‌نخبگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105857" target="_blank">📅 11:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105856">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSIVCqwi-hqYt-1cjuJmIKVvZTpWe0T3qfoYwiV5iTVgf10TvDdHPFce7e5N_DXKeH7PBUdSYghhz-bQn104ohucIhdUoAftPLYvNLG7A3-xu7Be-nz9oqXcbiHD9hTRw4w7aIHOmI9TwO-6sMpjiZrGnpedRV5rAsI_jViQ8Fm6X7zY4nLbTVrC--CwAdcxCYVCdlDtiXdzvnvaBMzcJ90NrFZ6fLXGNGTftoAUr3vgD0rzBDoswN-OM3_zISz4xHbKqmyBkqZfLBcusdi531t9S_3oZLOmZUJCFc-ifQnBAb2mi1E1BegbaJGTkD6Z36cwVt2chuqkgcT4LZSIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇺
لیست اتلتیکومادرید مقابل لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105856" target="_blank">📅 11:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105855">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5465076b4d.mp4?token=OMrw5mN612N-sO1qpCvzsfig3RvSqZvfSdpjwPYtnZq-3rfjcgbTvRJ7AqJFDI5OG6jTFTh4H_oJas7q_Tc49q4wqDS0hkT8I0M6XBjnXA-fLqWEhdYlGNyBElha8llxXBcpPByrqWfKO5hPveL7aSLNtY4ezg7JvnkBWWMgji4gisK1Q6KHv4jolgSFogh9dM0F4jGn1EOYtGw4B6dTyBoRajRBU7BA62cQwf8HOKX102T-DMh0eACsulChYNc6TwQj40mMwN8zaj5V_EAGPQ8deEHAU4H-KuASr3lv5OoiJ3N2dY9km1idXrB5P660i5cDkaijnhI2SWwl1Xv_MVsE87QaIobImWfbql3gHc2QVFXOZZNvBC481pSUSl4JPvWBBwv089EU8AiVuP93s1fkaux8ufOjHvaDGE1UJ-uCQCKpMWxILIo4azSxSAgo3epIEAWTkgix896q8i81nt7n1Pxnc2RCT9AIDn2kxV449uumz0RViLV3b02a1CQReUx-Bhl_HNWUQhLxXisPMvrJuoODa6r0XpUMicu74proH8aYGZ6eUdKhyPJJdYFXv5wBE_XX3Lx21ylL4-k9Ase7LiWExxGcrLVwroTmNPD6-O_ZGIE9bKSHbkwMOaQY43jzT9mF3GTyXKW0r-s-X-3iqwZ8KIFekV2-1nLSbVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5465076b4d.mp4?token=OMrw5mN612N-sO1qpCvzsfig3RvSqZvfSdpjwPYtnZq-3rfjcgbTvRJ7AqJFDI5OG6jTFTh4H_oJas7q_Tc49q4wqDS0hkT8I0M6XBjnXA-fLqWEhdYlGNyBElha8llxXBcpPByrqWfKO5hPveL7aSLNtY4ezg7JvnkBWWMgji4gisK1Q6KHv4jolgSFogh9dM0F4jGn1EOYtGw4B6dTyBoRajRBU7BA62cQwf8HOKX102T-DMh0eACsulChYNc6TwQj40mMwN8zaj5V_EAGPQ8deEHAU4H-KuASr3lv5OoiJ3N2dY9km1idXrB5P660i5cDkaijnhI2SWwl1Xv_MVsE87QaIobImWfbql3gHc2QVFXOZZNvBC481pSUSl4JPvWBBwv089EU8AiVuP93s1fkaux8ufOjHvaDGE1UJ-uCQCKpMWxILIo4azSxSAgo3epIEAWTkgix896q8i81nt7n1Pxnc2RCT9AIDn2kxV449uumz0RViLV3b02a1CQReUx-Bhl_HNWUQhLxXisPMvrJuoODa6r0XpUMicu74proH8aYGZ6eUdKhyPJJdYFXv5wBE_XX3Lx21ylL4-k9Ase7LiWExxGcrLVwroTmNPD6-O_ZGIE9bKSHbkwMOaQY43jzT9mF3GTyXKW0r-s-X-3iqwZ8KIFekV2-1nLSbVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فرشید اسماعیلی: داور باید شهامت داشته باشد و از هواداران ذوب آهن عذرخواهی کند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105855" target="_blank">📅 11:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105854">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97326bc667.mp4?token=TG2G30S3kKcbOKAg0JC308kIz3OQBzdZ_bTC4In8HgiMtOhnHhPkF3N9WzUM-qkqd6R8PBZSuNzKH3SJxQJwZq9JwS7Rw87lSGJ5Ls7W3FOEbz99kJ4zXoWbE8uetp3hfSSXNbR34tSnE96xrZHkElh7JkmkHT4-8ogalwRnTp6WPX3pvMAi941VHZiemTny5faDg4lsq1cvWUs64I_DW5kMvojQwhf-W5_5cWMk6-4NSLuiG7EkrqzBxceZHuqJPPZlS91cy481qK2y-M-UuLp8GRxKFUGgL4JNfnZYq1-cSTyYT5hOGttAuUuz_RwNocsGFc6JTlgHMD8862hUmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97326bc667.mp4?token=TG2G30S3kKcbOKAg0JC308kIz3OQBzdZ_bTC4In8HgiMtOhnHhPkF3N9WzUM-qkqd6R8PBZSuNzKH3SJxQJwZq9JwS7Rw87lSGJ5Ls7W3FOEbz99kJ4zXoWbE8uetp3hfSSXNbR34tSnE96xrZHkElh7JkmkHT4-8ogalwRnTp6WPX3pvMAi941VHZiemTny5faDg4lsq1cvWUs64I_DW5kMvojQwhf-W5_5cWMk6-4NSLuiG7EkrqzBxceZHuqJPPZlS91cy481qK2y-M-UuLp8GRxKFUGgL4JNfnZYq1-cSTyYT5hOGttAuUuz_RwNocsGFc6JTlgHMD8862hUmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🧕
مارک‌کلاتنبرگ: گل‌اول پرسپولیس مقابل ذوب‌آهن باید آفساید گرفته می‌شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105854" target="_blank">📅 11:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105853">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
واکنش اینستاگرامی خداداد عزیزی به محرومیت ۴ماهه از حضور در ورزشگاه‌ها
:
چهار ماه محروم شدم و الان دارم میرم مشهد به یه زمین چمن سر بزنم. خواستم اطلاع بدم فردا کسی ویس صدای قدم‌های من در چمن را نگیرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105853" target="_blank">📅 10:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105852">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688084072.mp4?token=S_SP7uzGrGcezSsxDt6v2XqUWzy4nWJG3n2pETfdiWrbj6PKE6c1jvQjTivDA7HSNzBemL6bLQ3gchMWBc7hqI4sfALIY026O_PZ8gyOrVjuBjgY4taieH_ntLvXU183_tlPpQQu0KFuFhbJdGvKimzX-keR0wgOY8xKttzyWWfAUX3jTcruUyK2RFmxgq-DtChtqdxKhsmPEotT7JXLIJc01034bNftWYzrRWXiNdGYEHtZVuHw86yIqTAMF-Do2a2aniyCBoKrCIYR2LAvqrkI9DUvFtdRL9baVYVyMzy16ngDu0Xd_6lA62wBe2v3l-p3JGlDIpHQLf0v8z5uBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688084072.mp4?token=S_SP7uzGrGcezSsxDt6v2XqUWzy4nWJG3n2pETfdiWrbj6PKE6c1jvQjTivDA7HSNzBemL6bLQ3gchMWBc7hqI4sfALIY026O_PZ8gyOrVjuBjgY4taieH_ntLvXU183_tlPpQQu0KFuFhbJdGvKimzX-keR0wgOY8xKttzyWWfAUX3jTcruUyK2RFmxgq-DtChtqdxKhsmPEotT7JXLIJc01034bNftWYzrRWXiNdGYEHtZVuHw86yIqTAMF-Do2a2aniyCBoKrCIYR2LAvqrkI9DUvFtdRL9baVYVyMzy16ngDu0Xd_6lA62wBe2v3l-p3JGlDIpHQLf0v8z5uBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
پست باشگاه بدبخت و خار آلاوس بعد دوم شدن در لالیگا پس از هفته‌چهارم
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105852" target="_blank">📅 10:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7VmAdoheI9aXw02Nq0VqYkSpnz9G3x0ye5D0hKNaSc5NYF70D9gZRuqIFfCijyCLPt2o_R5EOA-4hAie2_s6TR5ZImE-LIVA4wfjKo-wOMs7qwGcTAIgKcwjYMvuja2pHY9-nil764_HtV8UhqFW8tZHTPxev_eVXBlqVvIGJvOqMzfF8Fbf4s42M87R-pWoUQdp8qtYHF3uksAoS_fs9bvTdOEMgxp2j3OmYSRw8PTgSwjMpwRpTUO1tZEg3TsdgGuBpjw8fNOOrsx0TkHohwMVL-edgW62XToLVPPyLVyPnpGOXSzJGVDoXwlAk-Z9m93QPVNo0Z0RaSuaErHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرویز برومند پیشکسوت شریف فوتبال ایران و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105851" target="_blank">📅 10:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105850">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dffcc1103.mp4?token=qvHwlWDRpnfKRlqhpBiO3sf_SCj5MH8_GaKLZGsvWb7T09i5KvfFrTw0vffMSnKynRb9NaiqjzVhiGbRHip4A-heMo6-AuiUeRbU_aAe0Ad9uC2s89a1vEZYnYM41LZM8K01JjhFb7vI4reDrsADdpBaFUO-xKADmVi1ZYFb8zeMSBwT0NcZih4VA_0n7LRFGeGSjtdjNx1GNBGBQOOmxaF22YrocDbMqtmEFOeNbx-oxc_riCIfkeTO88thfOKf_4fDvgJmcmMXZfCWCM23pcHy4LjQMXmPRjQjz0cTvo7UTlwMALSzZon_cgDFzLrrN88xEoH3N1zrb_GEG5RMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dffcc1103.mp4?token=qvHwlWDRpnfKRlqhpBiO3sf_SCj5MH8_GaKLZGsvWb7T09i5KvfFrTw0vffMSnKynRb9NaiqjzVhiGbRHip4A-heMo6-AuiUeRbU_aAe0Ad9uC2s89a1vEZYnYM41LZM8K01JjhFb7vI4reDrsADdpBaFUO-xKADmVi1ZYFb8zeMSBwT0NcZih4VA_0n7LRFGeGSjtdjNx1GNBGBQOOmxaF22YrocDbMqtmEFOeNbx-oxc_riCIfkeTO88thfOKf_4fDvgJmcmMXZfCWCM23pcHy4LjQMXmPRjQjz0cTvo7UTlwMALSzZon_cgDFzLrrN88xEoH3N1zrb_GEG5RMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
کنایه تندادموند اختر بازیکن سابق استقلال به رامین‌رضاییان: فاميل‌هاى ما سه تا جت دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105850" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105849">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7e0021bd.mp4?token=X-D3b-CCoZ_CVQ9zBjcRj3PYi5Wm3FA4XIcJ3QPlDlPFIqXWli3zP-F4KNlcNPrbXh3wBVR4nLSeROiaiWMdobV8_IyEUsuhO20JDOpEM_qjwldgp0x7BllYX3rIuv0euRR4-7xhsR6ayjQFeMVArEGLnb_symXmNeL5nvel2DCDllE5fFMaTbgkpp94HLsytdMpzp9sQ-hnmRfVs7eYkBMUfVfkLjv_dH2i5Aq220VoAGeT_ZJ30u_bmCE7sqnq37Wk5h-2RcB372LtIcoIi-xJYV48M7mgkA4BVO9tA1gf3pKv6BgN2LwwiJJXLEMUXTHeUEFNWL01VbuFtKK3JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7e0021bd.mp4?token=X-D3b-CCoZ_CVQ9zBjcRj3PYi5Wm3FA4XIcJ3QPlDlPFIqXWli3zP-F4KNlcNPrbXh3wBVR4nLSeROiaiWMdobV8_IyEUsuhO20JDOpEM_qjwldgp0x7BllYX3rIuv0euRR4-7xhsR6ayjQFeMVArEGLnb_symXmNeL5nvel2DCDllE5fFMaTbgkpp94HLsytdMpzp9sQ-hnmRfVs7eYkBMUfVfkLjv_dH2i5Aq220VoAGeT_ZJ30u_bmCE7sqnq37Wk5h-2RcB372LtIcoIi-xJYV48M7mgkA4BVO9tA1gf3pKv6BgN2LwwiJJXLEMUXTHeUEFNWL01VbuFtKK3JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ماندگاری مدیر رسانه‌ای استقلال: اگه کنعانی بتونه با شستش گیتار بزنه، واقعاً از نوادر موسیقیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105849" target="_blank">📅 09:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105848">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a78b6b32.mp4?token=IArX5smcGfnJ-NxqmFbKUgLtmhLe6ABzaFZYVmdC0YauYZpbZZlB-eCsCRILhiHWGnib7Cr4CSRYnPwNfpVrE2TsVDqPtZBE84mprebLmAdHlsNGy0Z68vWl3Uz56FPbTinxapwPEqujfDUVrf-XwotfeQ1PgLhsBB7Lx5PKn2wYJwH6nU8NL-QvgxPoIy0pC0v3ENt27W-QcMaREpa5IXIqf0URIXv3qdITLDvJ-uqxFLDg7lRZ8Vh3nR73W1jAy1VNy5hCWUytk_lXFTgT4nY0UqsivkrHeAyQmSurQnsn8kROsGpVKUpSAwjHRpj7-v4jFB_snJDdPjW-v5nSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a78b6b32.mp4?token=IArX5smcGfnJ-NxqmFbKUgLtmhLe6ABzaFZYVmdC0YauYZpbZZlB-eCsCRILhiHWGnib7Cr4CSRYnPwNfpVrE2TsVDqPtZBE84mprebLmAdHlsNGy0Z68vWl3Uz56FPbTinxapwPEqujfDUVrf-XwotfeQ1PgLhsBB7Lx5PKn2wYJwH6nU8NL-QvgxPoIy0pC0v3ENt27W-QcMaREpa5IXIqf0URIXv3qdITLDvJ-uqxFLDg7lRZ8Vh3nR73W1jAy1VNy5hCWUytk_lXFTgT4nY0UqsivkrHeAyQmSurQnsn8kROsGpVKUpSAwjHRpj7-v4jFB_snJDdPjW-v5nSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
تصویری از کنایه امید عالیشاه به داور دیدار تراکتور و گل‌گهر: میخوای بهشون جام بدی
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105848" target="_blank">📅 09:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105847">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12456da477.mp4?token=XC7RxUpsXrOk4bEQCALjZzVKjyRIbn00HHkgBoX_7iKQGwxhiPL4Dl6MujiTURBCf3wQ0BKv_djVI5UNwVbwl0y_yp0vwZahTYUp2RnmldN_rvah4WPGMkF6Lbjr-y27-8LsPjao2rZOm1lHr-T_V61qv2HONRU3iatg39ZGVCUsoINZlEnNxNcGzXo4uykiExDTZZvj7ulF_qVOOoaBEnhfy8Z7yUk7yCvw5CQn3RxNY6JvhuU2Wvvh8pmnBusYHD1Kd-mHAK1DzgtsB_TkqW2HqsWs4nEZNVmjpSjTKMeQtLmTcqC3_XrGx0m-0Mv1ltD_uoYIwM7hI87FWETRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12456da477.mp4?token=XC7RxUpsXrOk4bEQCALjZzVKjyRIbn00HHkgBoX_7iKQGwxhiPL4Dl6MujiTURBCf3wQ0BKv_djVI5UNwVbwl0y_yp0vwZahTYUp2RnmldN_rvah4WPGMkF6Lbjr-y27-8LsPjao2rZOm1lHr-T_V61qv2HONRU3iatg39ZGVCUsoINZlEnNxNcGzXo4uykiExDTZZvj7ulF_qVOOoaBEnhfy8Z7yUk7yCvw5CQn3RxNY6JvhuU2Wvvh8pmnBusYHD1Kd-mHAK1DzgtsB_TkqW2HqsWs4nEZNVmjpSjTKMeQtLmTcqC3_XrGx0m-0Mv1ltD_uoYIwM7hI87FWETRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پیام جدید وحید قلیچ به خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105847" target="_blank">📅 08:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105843">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a89c6058.mp4?token=O_ykgYXqoG6AMzLDPP9D5T_ZYeQMtAgFY4lVEBa8Pm89aRV6sCnj7EPQ9itQqbFtF9rUoA7amIJ0XR9KbJV-HSRH-GBZnyz-e7MMsUEHurBxCtc3_3FYJUvENPIsq4weMruNqFNFEYhUcSULZn2Sw3THVRRpOVKvRykdKPFFGV_pfHh-OZuvrGHSNJFT3-8ecg_mHuXxY-Urk20yYOY-uP_aRIJ0k0DJpTZfWg7l6wWFazlEZrZ_09Gl1nnOAcdYG6CATBJT4svHAg3RxrsKWLlQK3_3CPUaL3lP90wEszXEvkKDBgD4VsEuC8taP1Xc86Y7UPLVeZeYeaXKktT2QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a89c6058.mp4?token=O_ykgYXqoG6AMzLDPP9D5T_ZYeQMtAgFY4lVEBa8Pm89aRV6sCnj7EPQ9itQqbFtF9rUoA7amIJ0XR9KbJV-HSRH-GBZnyz-e7MMsUEHurBxCtc3_3FYJUvENPIsq4weMruNqFNFEYhUcSULZn2Sw3THVRRpOVKvRykdKPFFGV_pfHh-OZuvrGHSNJFT3-8ecg_mHuXxY-Urk20yYOY-uP_aRIJ0k0DJpTZfWg7l6wWFazlEZrZ_09Gl1nnOAcdYG6CATBJT4svHAg3RxrsKWLlQK3_3CPUaL3lP90wEszXEvkKDBgD4VsEuC8taP1Xc86Y7UPLVeZeYeaXKktT2QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💙
میثاقی: با صالح حردانی صحبت کردم او توضیح داد که اصلا قصد حاشیه سازی نداشتم و هیچ قصدی هم برای حاشیه سازی ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105843" target="_blank">📅 01:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105842">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ee6a8989.mp4?token=qXf1bf-eka2GJllT68SmIwj6d6LcBTME1_M7d0q2r1mfYDhiPV7VkTgZHaQboDS4xFt76AhAzPx0wUqBdg4736lxFi6F3ZgNG_WeBh6RBSEH85H4x1itAiVWbZQFoVNY4UQhPBHw5SAOurEEZ3nEPHx4ZJsL5waox8h_Rk3ZB6il1u52JfnnW5iMROS6D6kmqUec6lFUv9shmG3yIRpanpdzeGMHRM5sYRCHz2FRhZyf-RGwJjD1izGSSuRXj_p0Mc9PTd78-MiVwtGFC2D8N7I8lS1B6SJn5pfhUeEY53Z-3QkNAUmmwFPvrdv2jEYTbDtpayy8aTOxzTJtT7Loaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ee6a8989.mp4?token=qXf1bf-eka2GJllT68SmIwj6d6LcBTME1_M7d0q2r1mfYDhiPV7VkTgZHaQboDS4xFt76AhAzPx0wUqBdg4736lxFi6F3ZgNG_WeBh6RBSEH85H4x1itAiVWbZQFoVNY4UQhPBHw5SAOurEEZ3nEPHx4ZJsL5waox8h_Rk3ZB6il1u52JfnnW5iMROS6D6kmqUec6lFUv9shmG3yIRpanpdzeGMHRM5sYRCHz2FRhZyf-RGwJjD1izGSSuRXj_p0Mc9PTd78-MiVwtGFC2D8N7I8lS1B6SJn5pfhUeEY53Z-3QkNAUmmwFPvrdv2jEYTbDtpayy8aTOxzTJtT7Loaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💙
اسفندیارپور مدیرعامل گل‌گهر: سندی بیرون آمده که یک نفر از آن طرف فحش داده ولی از طرف ما اتفاقی نیفتاده است!
💙
میثاقی: پس چطور عالیشاه 4 جلسه محروم شده است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105842" target="_blank">📅 00:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105841">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e01e106d.mp4?token=SA057o2JobfSuV1yYvlUElnY-2JSUkOMlaJH4fIB4njObdWGas-zhlvs4LgiNj1LzHtW9UQb7qm3b9fPp9HiUMcqodkI7HMP5KUztogJWu6GZKmvq_4LpFBE2ljXU6u68I_HyY-6AKjW19DOnYm4lq4QJD6iZiJarRxaW-WiU7Vh6p_taFdADzeaNwSGlC5GiNzOb2BolVflHXkQgX-AzlcY1-vpc8hE4uf_vvCaHPHl-bdBmRDV7ICcWo1qWMeXu-ZBncgkqX7VlpE5i9GkgCN35z6zY29gqx20_CebmU0Xs-ZBoXntBDQYaurFH_cFdqjs3TjIzgD6G0xcwrS3Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e01e106d.mp4?token=SA057o2JobfSuV1yYvlUElnY-2JSUkOMlaJH4fIB4njObdWGas-zhlvs4LgiNj1LzHtW9UQb7qm3b9fPp9HiUMcqodkI7HMP5KUztogJWu6GZKmvq_4LpFBE2ljXU6u68I_HyY-6AKjW19DOnYm4lq4QJD6iZiJarRxaW-WiU7Vh6p_taFdADzeaNwSGlC5GiNzOb2BolVflHXkQgX-AzlcY1-vpc8hE4uf_vvCaHPHl-bdBmRDV7ICcWo1qWMeXu-ZBncgkqX7VlpE5i9GkgCN35z6zY29gqx20_CebmU0Xs-ZBoXntBDQYaurFH_cFdqjs3TjIzgD6G0xcwrS3Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
❤️
حجت کریمی مدیرعامل تراکتور: حالا حکم کمیته انضباطی آمده است آیا واقعا باید خداداد عزیزی را در استادیوم‌ها راه ندهیم؟ آیا این درست است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105841" target="_blank">📅 00:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105840">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca1acab48.mp4?token=Z9x0eV2gvbT4Qx-gNhRIiD60RK4Q2FJY5veMz51aqdUOKeB3rpmnA8NyktuXHGEFI9myPgQ3Mr0dCSKKKyzW_7KzO64qQZ2PKB5XQ2kMVODyJyum2g2ui4MMfr_MltEfw80uu5D06JpQs5VMoNcWcs_-u2zvUCswUxdq9to7T_bv-SvTIPJsvgCmu8QA9tM1r2cNba9lgGvviqGlXVNBQVNu22iLrU1C1hVf_haERqoYGqlOn1LGpfIIw7LZ4tXJJnOFsXssRlz84pd6Q5W-Qa3aLwIvn4AAleeEYiC-V-3UFPtN4EeQmT-sr5GemqxmLhR_nXFVZ-fUu2LvFcx7iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca1acab48.mp4?token=Z9x0eV2gvbT4Qx-gNhRIiD60RK4Q2FJY5veMz51aqdUOKeB3rpmnA8NyktuXHGEFI9myPgQ3Mr0dCSKKKyzW_7KzO64qQZ2PKB5XQ2kMVODyJyum2g2ui4MMfr_MltEfw80uu5D06JpQs5VMoNcWcs_-u2zvUCswUxdq9to7T_bv-SvTIPJsvgCmu8QA9tM1r2cNba9lgGvviqGlXVNBQVNu22iLrU1C1hVf_haERqoYGqlOn1LGpfIIw7LZ4tXJJnOFsXssRlz84pd6Q5W-Qa3aLwIvn4AAleeEYiC-V-3UFPtN4EeQmT-sr5GemqxmLhR_nXFVZ-fUu2LvFcx7iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
گلایه عجیب خلیل‌زاده از حجت کریمی؛
🚨
‼️
چرا به تماشاگرانمان گفتی فحش ندهند!
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105840" target="_blank">📅 00:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105839">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d780e6da8.mp4?token=eGI1HYKwVVLeV-bnK1_HUaQKVIODsgWZbTtOQsP676523MToFVK5OMitEjhaDh31X3hLU9fa2kizqUGsFx1D3VqHps0VyHfeN2fx8TX_2QMBdzmm9pUJVkZwt8iQz-B3BoBQMWekypXk4Q83nQ13IO-t-ckWzJj2BrkzwwzzoIhiUhVNn3z-Lejb_0tUxGYhaYhguYJbZL4WN15Lsi4YZpd5p6oC-_CypnQYzcWoe7Iv7KDm9DjUTUEWwcHIhyIdxJx_eA2MoMZDtkQJ-fcQ2blyDiZyyXIQLv-sPCEWe1yDIQGZ75I4eOK1AOQ2yweqd1dRxjckX0dkp2M7xm0YsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d780e6da8.mp4?token=eGI1HYKwVVLeV-bnK1_HUaQKVIODsgWZbTtOQsP676523MToFVK5OMitEjhaDh31X3hLU9fa2kizqUGsFx1D3VqHps0VyHfeN2fx8TX_2QMBdzmm9pUJVkZwt8iQz-B3BoBQMWekypXk4Q83nQ13IO-t-ckWzJj2BrkzwwzzoIhiUhVNn3z-Lejb_0tUxGYhaYhguYJbZL4WN15Lsi4YZpd5p6oC-_CypnQYzcWoe7Iv7KDm9DjUTUEWwcHIhyIdxJx_eA2MoMZDtkQJ-fcQ2blyDiZyyXIQLv-sPCEWe1yDIQGZ75I4eOK1AOQ2yweqd1dRxjckX0dkp2M7xm0YsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
به‌به آقا مبارک باشه. اولین لحظات بنزین ۱۰ هزار تومانی در ساحت مقدس جمهوری اسلامی
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105839" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
