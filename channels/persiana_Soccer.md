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
<img src="https://cdn4.telesco.pe/file/uyYRkaWMvZu9kuh9YKWQL5nHcb_Gx-4OVgOUQ4zAC0hKUVaIYCf5jyB20HKE06Fd_YX8_LHo_VWR2hLh4eC7OJV24LMZ5MLg42CwgotgtjyogtG5qXshHvE3k0Avj-NMNHf2KP8lRZhZ1fzpbBPzp5sOIj7zBq-1yjzycgcFCiee_EyHbIv9AELSDVVPcEDrV5LvLKbmkAvJb3Q3-oVJrkLd0D2lT9ryPRiGGXNYAP-jGbZ56JB20iEliCiUH0qrUumqmRHNs6VH6fXQaUcb8VACa8MD7sxYjsCQ_MuxEpkV-6FusoYv67uw4Xr9ftv1znVYa2Ou9XI-AXEGNqEUSA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 626K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 20:18:18</div>
<hr>

<div class="tg-post" id="msg-27541">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU5LjVxZKMs3CVN8nQoTsU6tSG7XpqmAaguLiATVl5ponkvN8zm66KmSLrdm_57rPCJO9a8jDjTS7v1XPSjLemvSlX5ok63KNBsqceX6de-VwQdfsY2snCB8Zc1u1-MH1AP0bJ4_q-gJl1hwVXzL2Jm943bzSM7uCSPcKP1P8J0iACyo1hWGiN_-yuMLHUoQQopEw4Z9v8jZdLc_clBAQrW5St14Ei7S0JQA6G_VKx-LxC_SjlaPUPSX3PhmWRTmiV_A3tf1dKD-CYI2qkePc5avNANm8CRGa1TkrIVVT0sTV88yusVasuCyps3RI-1cgYd-_B_eaqmrOmWkSwkmwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال تخفیف است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/27541" target="_blank">📅 19:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27540">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHAf7PuqAyEs3j7nLMGExFhIwHcfHgZ8BNJF0-ln9DV3cQxr-v-E2elOYh8Ty5HurSjDcY-t8wMkkbytVS-dHb-EUGnMXBVjatbXAoCLlShe7Y-yPrOdV47pAC9RNKeQHmvmUe9eP18m9TNMXPwPiemZlFx5GWNUw1R9cliR1N9aK10Vw7Oga_gYT6CuWm2R8OGotYBtUWzbKcn-NGH0nuuwJoowG8N3o4kdq3Yb5n3U2UIdaFqZ3Ch2w8xBtTLlUDTi6XT0UdJ7260tb_d6MxOXy80JlNiMs1-C1pxcsNr4ebl1-m1qv4WaaWkBucz1Pdh2m8qW85eqkNavmr74dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/27540" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27539">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O57Aw0qXC6wxngR9FP779GuAtR5PXaO12aSdo1FIXSIqGlY3pkjwIoxomOn9x4TpycIDPRYcPBUVcF-55rroogJLgQ7Kvi4ZEPH4xXP6klXFGxMFeewkOntMl5OPtMPHASb8U4IP7zsio-P6nNhGWzngGmhYg4fMqJ7i0nGwUxcReVbaKUVWKmCp3aaBGhrHE1GIYh0kf21wm80XerXvsvwRrNsbGJIXLtEJjIxDSi43BizIK5s4F2HJukiLfDsxQAp17X6aHuM9m0sU0hvoMcS-BpTTEKLtMpvceDKUGPIO3EOY64CIzhBAUMap09m3apnwOj5svGK0GyGrFXhzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/27539" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27538">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGloovSskvzaluHcF47PUOraKFwEeQZyP_ffBUhJQ-i3TMBlprBG9KhErT3fc-bISfRME_Ghv1t21olYrVCnektEsE4Vd8QRUZACKu184Owkqwppm8yCNX0dz8xF4VnWSQUoulf0HTd_hR1HEOWXhJte-Nf5C9_IyXUo0gSKv-L1TxnUSd-M5akR5hRGwtkqUSPTqszO8jqoavBVX6e6fFbz9rH1z8sUOmMfXc6p7KGMTYXy3FIG4cUSXUv7MHci5Ki8Jav4POPgQhQAvx3mZv_Bbr-QIUi3a95qF9nW_YDKQFvLDopHv6Ieu5Rotskjig4R7w86KxEkZoFJKyiaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
سه‌روزتاشروع‌لیگ‌برتر
؛نگاهی‌ به‌ ترکیب احتمالی چهار باشگاه بزرگ ایران در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/27538" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1YI0XWB_JEtpE_RooFS3ehofuAJ3rRXg2bMrQt3VkHSImmW3gb9Rx2nX_3x99oKT_QMNsp8KrQ0h11Y3CF3HxvWcYZFfmRURRw8QIn-FoYYpzYKcx7_kFtm8eeGHwfwKE_9_xHLk742mWtjHLLOdmZkInVW_XFm0sZu_tOtgrporHTEszfuEwcrnd1XW6xZDnrsM6lT8Ju_E0LqrlIR64f7BNmyHSz1HOusEVLRaL-hPTxeJZkHBFfLcAp4ApS7JbRu7QGq36tAZH4JpY2x9saQ6yFom9GlO8qCx_jyfaiDjHJStAPkQz2dtXQ-3XKqNu72wYbbvIC01nDjh4L6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
آنتونیو گالیاردی مربی‌جوان‌ایتالیایی‌که چند هفته ای دستیار امیر قلعه نویی در تیم ایران بود به عنوان دستیار روبرتو مانچینی درتیم‌ملی‌ایتالیاانتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/27537" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=cEv8_r8_zzNqrCJQ2OtY9yimc6OGmE9sH4ajsJr-mkl6fO8byHAMSGUBAvg5TPuNTChJJS9Pb_E_hZSJHOiCx8qBJ5M3jR7x1Pz8N44bJUVcbGP9Jl1x4HBtd3Ur_Aib9Z7ZLn5gp2ABsiL7IxgLXyqlrNTeUEPU-OXZ4FJhWwy7AfgeTEbza0GQTYEmvYAtTvAYcsVgFN2hTDJKvJqq9EaRIIDLonbmHthDynKZ2WMBXNVRXkXIIp5BEOYANkLG7epVgNLdw0nwy22BOsgUOkzGp5e4Oai0e6EeQWj4eb5uLXZfFsPpeAsojZe4wNqHJGLkHbfIdm2mxTZWD1l7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=cEv8_r8_zzNqrCJQ2OtY9yimc6OGmE9sH4ajsJr-mkl6fO8byHAMSGUBAvg5TPuNTChJJS9Pb_E_hZSJHOiCx8qBJ5M3jR7x1Pz8N44bJUVcbGP9Jl1x4HBtd3Ur_Aib9Z7ZLn5gp2ABsiL7IxgLXyqlrNTeUEPU-OXZ4FJhWwy7AfgeTEbza0GQTYEmvYAtTvAYcsVgFN2hTDJKvJqq9EaRIIDLonbmHthDynKZ2WMBXNVRXkXIIp5BEOYANkLG7epVgNLdw0nwy22BOsgUOkzGp5e4Oai0e6EeQWj4eb5uLXZfFsPpeAsojZe4wNqHJGLkHbfIdm2mxTZWD1l7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/27536" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaOb43imQyorzrgnWJ49TQy6vBp6HGOO6qxWldqQoi2l3M_Zh-mLFROlf61DGsyfhqtnJALMErsgPAouXXvTwqF0h3rs7cWj-jt7DEbg4vrJIpNm2-JQTw-_3J9nVkCdrGyP7L82mSTJKsYK1PKaSMFydP4VA9LBSTzsvN0CYkm3YPzM0Uri1GSs6eBlJQgc5U2KCPxyIqf2K2TJdyq5qTjebRSutEv4NhH5ZphIuIJw_5ZkE8wjlFtQVsQb5AEc00fEbabZoBS10bWMwyEyvyG7L-RfMiQhDK1CRlKWdmPTkGKDtUS7Pvo-wKvncsKVOLdnmDeVxLtHQQ_5JZqTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
هنوز شانسی بت می‌زنی؟ حرفه ای ها قبلش تحلیل می‌بینن.
هرشب بالای ۸۰درصد آمار بردمونه
میگی نه؟ یه شب
بیا آمار چک کن
🫡
🔻
اگه میخوای فقط تماشاچی نباشی و از فوتبال دیدن سود کنی فرصتو از دست نده همین الان عضو کانال VIP زیر شو
⬇️
👇
🅰
g20
https://t.me/+OSLrSo8D0ck4YTZk
https://t.me/+OSLrSo8D0ck4YTZk</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/27535" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27534">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTm7pbjkAUvnOz-wr2Hwh4BMkhNGXD_uHdfVctDdvmGbaXWrgo1tnDH1YisV_e9aMLPaCvP2y3zYgg3-hUZXDiXdf5kczgL3ZHaSLWKeNPapHgAtF5ijztktx6wjTTuzzYv-o57Phrb1bQuKqEJvW1ul3QAKTLEKFxnKe-T4b5QgyT3fZdK5aQxhyoGplhchkwViTlU7g6w710BtzZg2zP7quG3r_piKj97LHC1K8mF0LRSbV9rLYPHSYRnVCyIzMGRrQhKu6nGzJI1Zbbty13NF6WA3VlUHTsDZL4fPdU0ye_8QI6QlGdq25e10e51l0MqtIfQ1HIt3shCoFYHPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/27534" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqrbbuIS0eFlYGKIc5RJWnJYzmPgPmqHUL3UaY1Dz3u7HmvkGp0pUkQMWapOxGnUQn61czPvSmAY9BL719fokLtnYLuNNzxolqHQgbozie5omHhA3J8CCYw8J5o-z4g-2G5DR8C8R-Dj7b4Qclb5S6Ia8uGfmh6BAMUmyKQKrb_-ErWjOzomEts8u3qqAiFzyuX6g5AHUQpng_XVzuxTI7eSE3ZCTTmGNJV1AIrne8CtXJMhV8QfPEr_YMI0lMZsdAFh9AtiDx9_F0EG88r_zng81oQXU53sXc6hs-sgLrN1VDwUUdC5ApAVevdhrE7dO2gVdBchs3stDu3dtHsdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/27533" target="_blank">📅 18:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e61nFTOXuevQrnPDApwNu4_0o3bVTnmWkCQH-74iciaS5Nc7YI8ITKgfMJrbnLAdHxUOZY-tZuur-QNol4DkWBxvB8unowCX22bGEFBSx742USbV5Cxun4VLa7ZpAYzs2f8FxgaqNof4I3g2jkaY9DwZLwaHqbz5td__Wsy1lnZj7N2ZPk5-DfW4Ax_hJkCoSlJlt44DN-UbE7AUY6CCxr_XcTf59rau-IA0UuipuISiQe8MAh93baxuXTaCW-YZYKetnBhnVuWIzmB1m43dXpbnZFwtXJ9x5SHKsqJtwGYAOi1-h7-cio5wSkU2i6LWlAgu2wUtptaemP5l2pQEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا:
به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش گفتم، ازدست‌دادن کسی که دوستش داری میتونه آدم رو کاملاً نابود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/27532" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/27531" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0uj_KN8AD3M1YqvDhdS6ME4d5qQTv2FkFpGnZdc3_Z58jgiuXdOuaEk_UYonEPn3vgczi55z2ZKUis1qjapre5U2NCA4WGrFjoH9NQ-MmiufXmZGDcRL_E4DmnMTnWDCxGgvVtVfbLJZ1do4oF0ARAWH8slQUHTqZVa-1GuIks2nJlYWlOdSV8FaTxh--N3Ol24Zy-alOkNNad0iTkXSY5ZxHvgKP14puhw60WWXXtYQZAcSSTD6KXv3UwwmFAmIwYGBFs496GOtexLebh8JS3NOTBkr5InJKPXwWtY5qDKdMPoGOAQpDDMR7D9LJdg0w9jPyLbbeO5n3D7Vwg5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی برای عقد قراردادی یک ساله با سپاهان به‌توافق‌نهایی‌رسید و اگر اتفاق خاصی رخ ندهد فردا قراردادش رو باطلایی‌پوشان‌امضا خواهد شد. ارزش قرارداد واسعی در سپاهان 10 میلیارد تومان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/27530" target="_blank">📅 17:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqIGVvjV8rk11gWKoAcz0mDHTg82nII8dTN41zSTTPiwlBpDir4wByXQcwpo6t3jqrsmyUNKk0SpJyGUuTHUMFaG_So7r2SlswVwNoBFFQVw5Bs3OX9qmxy-Gae5Gsco7GEiAUEk30P_6YnvCU9b26iAc6ZkRSZMvK2uWlduxdMqN3AO5G8KIZdElhojZkmoi4dS7-wXSaH4CvRvRqiSVB7aFtMveWFKODJbOODDEOqjeyinqlqmhA8ZibXy9UUdHK1aihrCQHcl5e2a3u32PuqVjGKgBB2zqo4FDyG0r5whljjR4s6NnlNosD9j8U9qoLfQtVpcXtdtK0-WAKLKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/27529" target="_blank">📅 17:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcCoE78pJNNVokLqnTqw7KNKp3tbMLE3eXkqQRNnTWnB09w2N_qbzdgjlvYLKEBrKTlgL8g-bM9g5kxtdm3M86KOh8QR_doX7X7_CvtT9lj9vXZK2UNhNB2DtFKA6bIvp3M-IXQU-w3cWIi9PbjwqfDD_0QQgq44A2XxMkOS-ub_xiRPvG4-Lsv_BYQpQyB43ir56yNjbaptjRDHr4ioPpRkb-YBGrk3tJnXdcSJ2WeCKxBwNfWo0zyGw9kk-JFUxlj5OsEFL2-x5nPtafT-RgjgOJ8Z3m4qzxJIMGo1Kjx9LjH76YF1ydoujkofL2mBkr1uHRg6Df-N0HxBX7B8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔵
بیانیه حسین زاده رییس هیات مدیره هلدینگ خلیج‌فارس خطاب‌به‌هوادران استقلال: استقلال تحت حمایت کامل مالی هلدینگ خلیج فارسه. در نیم فصل و با باز شدن پنجره قطعا تیم رو تقویت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/27528" target="_blank">📅 17:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V67aP1a_U3k173OfqWWGeZ9w3G_brTVtK3iL3ULt2ZHqo2VX0kbv1Vf2R73DIto3FrKHpmBhfGISrEV9cuAVmRgsMMglq5fNZ8qqeFGbuA41Hl4m5WLC4HvnLDk03zLUSlLZ_uuCjmEx2mWEYbi650I502uj9ZCF9mWtgR4_4IqZJYCCtNGRkd6f3DcHNm0a8MuGnSV0Epo5F1VXtbEFrxArr5L3uHWfTHvMx8hun1ELsT4TzdEDDpKgckE5D7Ypabe-HaEAVHkXJCHJVuSu3aHIWiS-krGd1kAwnbZFlwFlbUWHyI3ZnMa6GbDv9cee-0ko9rzrfABqcq-77AgjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌های انجام شده مشخص شد؛
باشگاه‌جنوا ایتالیا باارسال‌آفری 1.2 میلیون یورویی خواستار جذب آریا یوسفی ستاره 24 ساله سپاهان شده و این آفر روی میز مدیران این باشگاه است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/27527" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27526">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ_xM4MKk_wcx7guv7_FFspK9If7Akc4PjmA0sYmQY4xjziYPtvtPZKx3kOZMS58Fo57c3ABzqaeJfKkZuZZEDA0FrEzaGCNz-gCZPD3Ac8v-Rg_RT21yCEh4Dh_nMsj3H70uc6wIelJY8-4-6UVCszlvnTjP715IqLtyYTxQbEVdjhzchzISHCDZAUXenwTI87wY-VEs4S8z1BqYY-_OGbO19lcKPHx_Ji8rysdELSMAmWkxnVXrJT0qh4MEyAhrVXeidq4cgqAW2dj_FZ9H4GmjTVQ8GoSwpxp98lVN2F8TYPYKy_Ew-U8QKMHwNg0pICC72DKd1DfrhjWqKdxBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇪
#تکمیلی؛روملو لوکاکو مهاجم 33 ساله سابق منچستریونایتد و اینترمیلان با عقدقراردادی دو ساله‌ به‌ارزش‌هفت میلیون یورو به فنرباغچه ترکیه پیوست و شاگرد اسماعیل کارتال دراین تیم شد. کارتال دست گذاشته رو هر بازیکنی مدیریت فنرباغچه نه نگفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/27526" target="_blank">📅 16:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=n1Me4pJTQjVDWnc9ah1rj42wJjHxZDIm1zpmG68AOiD0ZZ8TmnE1pin_0nZcgJvKQLNIsg3tpJO9Pg3_avGQSlU5K2fVmWq93cgTEqVWmJ2NBV4MP9Omo0z5jW_47yIFUBIlkdDSHqpTZL0NQMsyHYrsLTiblWNCcXWTyoG1lB0RRRMnuY9mBw5vpk5ek04rQXxtSTVtK6Ggo8uAj2OKog7cUhs0Greq7VhQU2nhwS3Kw-pNHgNhesj-wSs1WLFxKxRDDt2bNRrxZX_OmVF7IJNUk9XPxbU6WqqmAjIXHrz6bSnDq-tPqcsWdQfmp-cddRu2Ko8XrGdpk3Nz6Rmyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=n1Me4pJTQjVDWnc9ah1rj42wJjHxZDIm1zpmG68AOiD0ZZ8TmnE1pin_0nZcgJvKQLNIsg3tpJO9Pg3_avGQSlU5K2fVmWq93cgTEqVWmJ2NBV4MP9Omo0z5jW_47yIFUBIlkdDSHqpTZL0NQMsyHYrsLTiblWNCcXWTyoG1lB0RRRMnuY9mBw5vpk5ek04rQXxtSTVtK6Ggo8uAj2OKog7cUhs0Greq7VhQU2nhwS3Kw-pNHgNhesj-wSs1WLFxKxRDDt2bNRrxZX_OmVF7IJNUk9XPxbU6WqqmAjIXHrz6bSnDq-tPqcsWdQfmp-cddRu2Ko8XrGdpk3Nz6Rmyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دخترخانوم‌رضارشیدپور مجری‌سابق‌ برنامه حالا خورشید شبکه سه به این شکل که در ویدیو میبینید پدرش رو به مناسبت روز تولدش سورپرایز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/27525" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U156W-p9QxzxVp_ytHA9cy5LyHgKbRXj3oazYe9D8qhkSohibheBqb8lBrrIrodzvrWG6Jd653We0MHugtQ-FEfKR7HMOInruinFUgxQAV2gNQKbAdu8xAFB-_4ixVwytCFjpDxHPDB-gmKGqisNyZr1a66rt-3q6BP-JowDfNzzaZfiWfFtu7jW6BjV2oVujAjXhvv-_T0zgYMQk99rjJiGOgozwsqs-t6t45QC3P4K_MQjQQP9K44Zgq6yrxBsBHuoAd680olw8EgPVcdddCjVXvxfNbZLlG458_wiIo7RPDEv5nK9z0n9vdRSRjyPdtwwKVj50ldsihq3-lZo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/27524" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
بااختلاف‌بهترین‌ویدیووترولی‌که‌میتونیداز دعوای علی دایی و کاشانی تو برنامه نود ببینید؛ شاهکاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/27523" target="_blank">📅 15:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-yA198ZPnX9EklAdHbhtos_NQ27QEqobeYPABnuz9wPKYT_LgMPy6hRJKE5177aT3Qnu0HyWWXb-DTa8g5lsOXhw61ZYjx-ziWrUrXeImG6srRJUWP3szcMoSEqLr3iKPvf1HIxxhgSGS0fZJsCAW5uGgU5XFRRFIq4yQilOqmXuEE4PvME59VG-0wVJgSo6-lfS6HVlnQ4y_60G3lkVG2o7w4KvMRGegwz5L6U7RZ3qf49yJbVJ66sRrnOUzWT37wwjfrWGwVI-pTg92tgZCvbQ4juITX4PUCIzsXDbL97ql7SkruRFUcI9wOTdNcAyt7FhoynY_Mq1gzmAHuIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
وینیسیوس جونیور بعد از 9 فصل حضور در تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/27522" target="_blank">📅 15:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxYOBbUMgl6xcTGjDaKWoiyFtVHZFUXAkFzvFKwBBodjm_Y1kyb60zqdNcSd_rRIxd21cn4hhHfGxh-P2SzZigZLSZvscAPwhZ2nYsLMaA1AYdMV-UYyOxn4aQIne8kW4xIJSfVMNx-tVC4iCiOLRL6IdopFPZDTS4jXHKGVRVca3oA5M4Clwl6cuOEZJk58nvr6NttoXSyP0dVLME52Tx9pdGDneUwJrZt4EfLgupnWlLBnk_ZrvZzpXF-KYpoi1VQHiZ9NFTkPR177CCRtiGKHbddx7FALrqEumRr6Z213m8G7y3CWYLPf1kiTc28ullYJui07fDYAnzFV2l-CkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/27521" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RScRuEFgJu_LLuu_gXBsCKtQw26LEe7kbhj_g29XAJxQ7cELIhiIZKdxgX02iaYdmOKe3AT8Oi9qBVqfkkgSU-hIUJ9rvgo6XFfMCfbqiz2_LKR2PUeVvSrcp_zyeRJAtGfchYzpLC0PvwY-5XvdCVWC_xJ9ybdPPvSQHBfkhya9zs-YP3SyFP2dhJ5LE5hZ4BoQEx_uKKNB-tBGSa34R6r1q5m4ScCuIbgCvlt3GCZu2rLSElYENT8DopJBWYTJPBEBiR8A_-KT6T9_D1J7gRs-90eOk7XBs2cwbhDBf9r4DuGEomYDhm5Qoecvzvv5RzvaCOb6C8gqmYrreQXqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال تنها 10 روز فرصت داره تا طلب پنجاه هزار دلاری زیلیکیچ وینگر سابق خود که یک دقیقه هم برای آبی‌‌ها بازی نکرد و احمد شهریاری اون رو به استقلال اورد پرداخت‌کنه درغیر اینصورت آبی‌ها از چهار پنجره پیش‌رو نیز محروم خواهند کرد. پرونده های ساپینتو،…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/27520" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=qCaV-r98Prs61XACggSbmvQQARzIKCsRyNl9LibyGfxgxhp8uMbhzNbG-ox3HtEYM5CQ9Y1OiD1nBXFhq8zYvHxL2jk1asJh-ofRTlfDOTrarKF2p7chaXg_DbEVA4jyiiY4AwsPhWisYmocMd33ptTIHjUdnxeeEBuhZ3vLVntyJwyaiGLk4CR3FzgO4gtJmsCRc9W6ZbbH2VtJ1ADD8sMGzhSrzPOgevFPWsfT_ldmiWFem0Ziy8zMdPRqL5WNL99Cc8s2ES5n2C3nNXQvETzTUD2EL4WnJzd4vbBiE8sBu7xuN4LyPsm3SVkbJTH1c-bqEIv31vLAt7rLNNk7zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=qCaV-r98Prs61XACggSbmvQQARzIKCsRyNl9LibyGfxgxhp8uMbhzNbG-ox3HtEYM5CQ9Y1OiD1nBXFhq8zYvHxL2jk1asJh-ofRTlfDOTrarKF2p7chaXg_DbEVA4jyiiY4AwsPhWisYmocMd33ptTIHjUdnxeeEBuhZ3vLVntyJwyaiGLk4CR3FzgO4gtJmsCRc9W6ZbbH2VtJ1ADD8sMGzhSrzPOgevFPWsfT_ldmiWFem0Ziy8zMdPRqL5WNL99Cc8s2ES5n2C3nNXQvETzTUD2EL4WnJzd4vbBiE8sBu7xuN4LyPsm3SVkbJTH1c-bqEIv31vLAt7rLNNk7zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇵🇹
ژوزه‌مورینیو سرمربی تیم رئال مادرید:
هر کاپیتانی نمیتونه‌رهبرتیم باشه. رهبر تیم رو نه میشه خرید نه میشه ساخت، اگه یکی از این بازیکنان توی تیمتون باشه، همیشه یه گام از حریف جلو ترید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/27519" target="_blank">📅 14:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27518">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtYFOH7RE7tkCyGb3JvP4WClXqKsGSvP5WP1bw_QH5E9Akka2enfM-O989M4Z4ymOLCAfkr9zlUzd6BiAfyRkglLHWWVWWGgwKylbl4PqOBqVof3gE3-SzQuQDB1YVfnTB84lpL7a7P8p7lGK3YkAjjKlwka5PuboNByDH3L7R0hbNsZOr0WdRbb4Lj38Hi98dBLYC5RCH-rHk4keAKWTHO2MFcIwfo2XV1kLBGEVHwDLQAeD0TLn6sM_3vyiK2InZerlZS4cZp9-MOQxcKPwV4Xl3Qp1iP8xBQeD8xK9A52hs4Xy58gtlzwRx-kJ6o5_O-cPPgJvU9DK1BMi20jRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/27518" target="_blank">📅 13:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27517">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrwZkhwZXvA95_bCL9ySvE_McvdPEVp1RBVzcQ2hbV_GBThWNnvzBNLdpgJZCiVnzqLEX4Hq_FvTGDsKJR7adttWF8Yr00yxrSWs0NrwDKDD4e6AcdaWh9GoLNw9SMy7zEQC6EiZH8Fw3OuPqpXyqp0qy5IyuXX_EMRoz837gOe_dSe3xFi8ACfMlh-6OE4OXUUfaWskveMJjTQkdJ6E-w_lFWSqnqGBUAZ8c3dZkSl082-rfS-P_RiU_l3n76xXRa6I4Fa7LfYQ1eCLf9aDH89PC89ClgRDwepmO-lHCa33Mh-zRhxHVDU7ImjG980gWl_RUNEXT6BQaz3kUXHrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
مورد جالب دروازه‌بان سامورائی‌ها؛ سوزوکی دروازه‌بان تیم‌ملی‌ژاپن‌پدربزرگش نیجریه‌ایه، پدرش غناییه، مادرش کلمبیاییه، تو آمریکا متولد شده، تو پارمای ایتالیا بازی میکنه، تیم ملیش هم ژاپن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/27517" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27516">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/27516" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27515">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J35B3tTN7OITlJfXrelHsNLpAEbV3dMjiA9Tb1KXx0Gt5TzpTZjepy8_cdZW5nlSNqfy2XcQX9XhW6Ie_W_qcYXRFoBkSv5w8Wa-yjyYB0ACqHhXK490-SsX1EGYkBhux2iH_ZZOOc2jafeZEeSqq7dmDyC5BBqlwrIGLmhrhUO9_RH1Wb8kQp1U0PCSKk76OukLemyqzLG9KvbhuDI2No-zCbuW-F32Dr9roKRYeQ3LkxExWLeS10yvUf3fP-0AsQkreHQLWtJLz0tlBdkrqW0gjFikdBlRPeifdognuEdwJuK_CBg2fELPR5g2bruDr_DH14qOiI2KUmIIDL7yBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🇧🇪
باشگاه‌‌فنرباغچه که سرمربی‌آن اسماعیل کارتال سرمربی‌سابق پرسپولیسه برای عقد قراردادی سه ساله با روملو لوکاکو به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/27515" target="_blank">📅 12:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27514">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX2myvtfnrdStmaLD5_kX0sZvD5Rh6IguOVgTY0hkpsXrZYFFS06Wnt3dhu6ydfnsOWvROlUOq6vAK1oxO18JeXpSOtYXF_AQ0kfybQjH4B3TCnVh_jGhysTdznPPcHBPhwtfe0WYX8Nn9pwrdaktRacfaUk7AJlMljk4msdhAykQzPF3ApLYP1OMTEuXy6Rk_pvR6pDbZJW4KIi8FW9knJI7dGwZwKBgcQupMGJadTuxyVIkH9EMKKhh91ViU_ypX-sDpQ8QmtF05hFM-23UyEJgUgdytccrHJIOGsD51SizcBnhENruljfHssl5M7sGHXgupo2coOy-MWH56uXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27514" target="_blank">📅 12:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27513">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWHO341BQnB6oaIU-_dbfb2rAT3d_LljdRdx_olmD45DExUNjF_2UpzX7U5F0zg0DN0QH-kYrp8qw1z0u4_btI9k56Vm9Axu2iSqIwxi-a9HdOkLdiDmeGbdwpKsmTSQca2EaSM7kXHkU_xXXbGSg9Ul1AIjEgE8-Q8OMMgrYUGPdcx7_Ez_osiHAXLLgiKbYPFUjJ9q0PhxQT00ogxf3h2kBjU0FFuOpwVKEh6Ct8Z61EikhIqvoQvI55T6HmCVNwetIGrN1jMQ4RkMw1sFpeQFOx7BGVmIai8MS4HEUpDQj6nq5kcaP_YHdQUUjUCtCuM8-QOMFAiD7sRRmqhK4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
باشگاه المپیاکوس ظرف 48 ساعت آینده با مهدی‌طارمی و مدیربرنامه‌هاش جلسه‌ای مهم برگزار خواهد کرد تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27513" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27512">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2wCyRNswqiAFs_O-vnSkVEkcPik5btmvdoGMMFbt5Iu3AorApfEvyxL8hT5YNOT08NA7Cem4KwhX3unAeGodBb8R8Oqa0cySme2htyRZ8elEbAzNz6oZrStNCwLvkq9JddzV0HKvsK8YMBVtzBvUQBNJZuft9OBzbNcKA5_xstyp15DGaMar1XZXzq_H-Xo1eQ3vJhJcmyZlQQC6pBMzMc73Mq8VvE7AMHYiCpeR7yJtE6Qn9-gYz3WwX1QR_FYeOYbcL8ayJA4MVQ5uR-TFUF2Pg0ugWgtU_4NHRzftU1kdP0Lnnnraf0LKjbK90zMytmJwkiayh1h9r2i84m4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
رامین رضاییان فوق‌ستاره‌فوتبال‌ایران امشب ابتدا به‌این‌شکل‌وارد برنامه فوتبال‌برتر شد که یکی از دکمه‌‌‌های پیراهن بازبود که با تذکر عجیب اتاق فرمان مجبور به‌بسته‌شدن دکمه پیراهن شد. داشتیم تحریک میشدیم که خیلی سریع دگمه لباس رامین رو بستن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/27512" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27511">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=jrOtY4oyZ3FsoXL0NRWh9Py0vEOVlcMu-NiRE3zqaYOI4_eKouTGBCVqmvckfTr_W0u8Jxpk_n2r9Mdg1r9cegGGJ6e2KOw6ZiRCO86ocdZBNwExrcsDjl6opZmhgb-sgzRB3rEylhPjYsRDZ06uwE7nmxHb4_-Bxs7IO28MHme1pHaj_AltzCcTE237fMDfrCMnIJQUxDgX4751lw49D7HLkPF7cmrrYXfTzAdVGrl4JuYg7-w_4qMPyXUbbC5ljPk-eoApidsVzktDKhhKzsephYeXTjcnJALPdUZkMK3NJRRvGWaWjKO7BrtTCVXWQxVr9djh9bXZK-lHFve1DCshaN1sJPcx8vT6h57M3V35dxVSe0RTDKGOnn9WeW4dZM8CLofjRrqtJFemfzI9FHDFZ9V3qUOAHGivDiWpINGMfiY2hOSAsv92rwoL5wtLriES5nwHW1dbCigxtnLlmuSqOIIyulVlG_RGHAG6r791ewwPJvfplbqLaFyRYghwI27ielryr3lJli_iwIwI2HXD4KrazVK2K93DEXoKMqKj9PXGD6Q3UcNC4dMBs0iMtIw1i0mCyY3INvLIAQBBoW0RUZLZztMsdJSVhae5gmBLFY656laQCEXS5lAWVv6r6nt8Gy6Nr1wiyuTQ-XZay09TO7YSbVKKVGO7OpKz5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=jrOtY4oyZ3FsoXL0NRWh9Py0vEOVlcMu-NiRE3zqaYOI4_eKouTGBCVqmvckfTr_W0u8Jxpk_n2r9Mdg1r9cegGGJ6e2KOw6ZiRCO86ocdZBNwExrcsDjl6opZmhgb-sgzRB3rEylhPjYsRDZ06uwE7nmxHb4_-Bxs7IO28MHme1pHaj_AltzCcTE237fMDfrCMnIJQUxDgX4751lw49D7HLkPF7cmrrYXfTzAdVGrl4JuYg7-w_4qMPyXUbbC5ljPk-eoApidsVzktDKhhKzsephYeXTjcnJALPdUZkMK3NJRRvGWaWjKO7BrtTCVXWQxVr9djh9bXZK-lHFve1DCshaN1sJPcx8vT6h57M3V35dxVSe0RTDKGOnn9WeW4dZM8CLofjRrqtJFemfzI9FHDFZ9V3qUOAHGivDiWpINGMfiY2hOSAsv92rwoL5wtLriES5nwHW1dbCigxtnLlmuSqOIIyulVlG_RGHAG6r791ewwPJvfplbqLaFyRYghwI27ielryr3lJli_iwIwI2HXD4KrazVK2K93DEXoKMqKj9PXGD6Q3UcNC4dMBs0iMtIw1i0mCyY3INvLIAQBBoW0RUZLZztMsdJSVhae5gmBLFY656laQCEXS5lAWVv6r6nt8Gy6Nr1wiyuTQ-XZay09TO7YSbVKKVGO7OpKz5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
5 سال‌پیش درچنین‌روزی؛ لیونل مسی فوق ستاره آرژانتینی درانتقالی‌آزاد و با قراردادی دو ساله ازبارسلونا به پاریسن‌ژرمن پیوست. عملکرد لئو مسی درپاریسن‌ژرمن: 75 بازی، 32 گل‌زده و 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/27511" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27510">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSqqxO5ZNv_j9jRHqzOZX-tWeYXRy2RObSxSsBPNUOrWZpB5Rq1XrhMJhYONLNytyGUd-Wzp5ccFA5lvYVvmG2dQC4NT6uF6isszox6gp993zx9BFHeifFNhSf09uGBtdBLijBcdcJJgWR-yvI4L0xh2YJHr_v9uNF7jTpMnAdeiLXJEsYMZ95ZjHkrdM7xEsqtQG8-pKvlPHUpzaJJy1ruO3iYIQSpAiYcxdD_vsg5P6wWIH6zjmvds6m-RpfwA_btABk4z5NMigTp4Ajxx23semKzddzRnDfAqeoRCTCuHthgtPRmpjmDR_4pEIX84Q86HFn1ji3A2jn3tqeOjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑
️
2.5 میلیون شارژ کن 10 میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای 3  واریز اول در وینرو به ترتیب 300 150 ، 75 درصد بیشتر شارژ شوید
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن.
🎲
ثبت نام آسان و سریع کلیک کنید
✅
درگاه اختصاصی برای کاربران
💰
✅
پخش زنده ی تمام مسابقات
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/27510" target="_blank">📅 11:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27509">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3C9U5pfLlI_N01DL1SDOaP4F3dP6qsyKzPd9Ze-Ohb4BIXOS1xZ-LPUfH0gRDqGhtzd8F7mKBLB_YYt1LY89Ya6OI9GHH6mbUR4QM-WHqjx0axrbyyEmVpFCDnU0Hm9MmyjrqTyNwX_-fQUq4HXlRfquUPQv3QKkdxLf_JEx7lc4ASwnoIZEuovBlXjQJJKMh7aZ8NSC0ZWgMZxeiBFtQR0MNw_2vGzDf1SC2NA6kwaifMdO3KvdFsxSCRFn8d91Qy8JYbmTvHjGdHDL9eV7y4CxwF1ZaqFNa1TqGmLyZ31iMue8sO75N4t8Uc2o8d8wOQPWh_9dYfy6J2Y-vINMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی تا روزچهارشنبه به‌باشگاه پرسپولیس فرصت داده تا رقم رضایت‌نامه دانیال ایری رو پرداخت کند. درصورتی‌ که ظرف این 48 ساعت مبلغ 120 میلیارد تومان به حساب‌باشگاه‌نساجی واریز نشود این انتقال منتفی خواهدشد و این‌جابجایی…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/27509" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27508">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETCA3FTH4-HBK4YxwGxcBx5l73zZU8TRZU04z1Y0DJeBfvawI3yoJQuMQGH9MQ7EvpY-bwrjVu6pWCg_Js-R5vh42Wyp6N7QFH52G34g7yJ3bGpCLcdOqo75-cPlhd1jV86_L0ep5LWGycXfY_9a3n2rr4aQzj44JN0Vy44pdHl2sstmpPjDLy4iVAG-vquOHa1QW5roxGzYlXwCftwxV3lJtIxqzMkU3PeC14JaR7Q_LF4-pwPd-W6lxegsPjctvcf1uqjzMxr8IFjmD0Wx9RPcdm5z_4p3ety82OJNTHvXDvbL7BRVApWIw8-c1LtTRpa15kajZ8Xojl-Aq0DsBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مسئولان تیم نساجی: دلیل نهایی نشدن انتقال دانیال ایری به‌پرسپولیس‌کوتاهی مدیریت این باشگاه است. برای چندمین بار با ما تماس گرفتند و برای پرداخت رضایت‌نامه 120 میلیارد تومانی ایری اعلام امادگی کردند اما موقع پرداخت تعلل میکنند. بانک شهر و مدیریت‌باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/27508" target="_blank">📅 10:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27507">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=XTJyCF6tVW1EV5oNp6noyUZ9NofBr6bQp3HmkL2F0U5r0D0qLwNg9kQzXRHzenBnhuDYl9n6yMJety9AUfOsq5AjDaCPynsqrB_hNSJ9ZDKy0ifD1OoRx0K9mPEclfyUqEteeRI-U4und7zTsUUaLbUbOJEXOAv8o-oYwmc5YSPOpwuJmdbk6HMbJ4xA4WEYyjNct0_tNkG9-G8TI1UVIfukobxy7UEue8hxZmAPVWWaLrCDUTQ_eD9uJfNmeBXEafXjETcsuDd2SFKlxam2PQ6QtSyJ5QF_Zpe7W5qG66YDj0gcrL9fMRe28Tdo1k8h7qkCc6YYjl54xN6Ha4oQIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=XTJyCF6tVW1EV5oNp6noyUZ9NofBr6bQp3HmkL2F0U5r0D0qLwNg9kQzXRHzenBnhuDYl9n6yMJety9AUfOsq5AjDaCPynsqrB_hNSJ9ZDKy0ifD1OoRx0K9mPEclfyUqEteeRI-U4und7zTsUUaLbUbOJEXOAv8o-oYwmc5YSPOpwuJmdbk6HMbJ4xA4WEYyjNct0_tNkG9-G8TI1UVIfukobxy7UEue8hxZmAPVWWaLrCDUTQ_eD9uJfNmeBXEafXjETcsuDd2SFKlxam2PQ6QtSyJ5QF_Zpe7W5qG66YDj0gcrL9fMRe28Tdo1k8h7qkCc6YYjl54xN6Ha4oQIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شماره تمام بازیکنان رئال مادرید در فصل جدید رقابت‌ها مشخص شد؛ دیومانده 25، اندریک 9.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/27507" target="_blank">📅 10:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27506">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL4toWHtVMUdcJM799QBiPGPhJ0OgLPNXfUulPWqZeoD62P2oi66EbPPEB8rhbSn1y_DqcLWNZEW2OcbskjUWuzpuf9cIa7kk0_ebAhEpV3bAWLdxqi2SyhVCLabQ5Hb17qixeEi8pvkF-xJlmU9rIJEsa78we6gs8IQK87S0RL1gLoJVBpsEm9-94PESCGm78JU5o_xNviSpKEhPaSfjhMDf2NAi6QH7fdxRYEx6El3V95mgVp93xQMid7k-oYvo6QY8yrD8u08X7Q7REdUBQRD3AsKafHnZzVGXc6BcjqpWG2nbpT30zPGoefIEgLdi-VWWHdd50TqEmqmyv6kPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته اول لیگ:
موعود داور دیدار استقلال شد. بیژن هم قاضی دیدار پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27506" target="_blank">📅 09:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27505">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKEc84rLIyhEmx7grXv9oTyFFgE-_WmjDq8fdw9Tm_AXY3EwD5JkTLU7CJafgfRN_iH6DExReUm7zDE6b7HNcbpuJ80dh4MuFBhphXfkDHVTR6RMLMmi7b981E_sl6qEZOk52lGbLCpRN8z0fEtKIbRePcxN4M-dZI4BOFWMtspFYprWWjx-bIBBr27eXYeD-94OInewRSQnqN5ccBjT5jHj0UbItUCuEFmWcDmms1ImofH4qDejEYg3qUbmoL5bAGLztuSS03z0zesTtUFhAfY7tEfznitaK8I1vj-I1k7aCHp5zthye9HaQEdAj4ilCIoaoNtez1URcFEThdmxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی بازهم‌ازلیست المپیاکوس یونان خط خورد تا در آستانه جدایی از این تیم قرار بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27505" target="_blank">📅 09:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27504">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=LsZyxqBGdj7FZHLGoxyus9AzPLjRXi8kvJkABE1cbToYhKwIE9gvZvB3zSSYNKoF0VSuQCfL1_aesLJK9cqEF3SqLN71S9GbDIhhQ0hZ3vSBucpyqoFhzu6-UBJgoifQKhqgS1Aezf8luXHedNjRDjXgRVuTpp9bMrVMSG9m3tkpRPh7AWj781Y8dxeRCH8faeFb5jS92KmM-ekChu00gtWzyK3WJDtNU5vImGzZWmLj0ZZtERPWbw5kW5WDMJzHHZdrFyQVvSrqWmGbBud0PV0QStS4aZIKTbAehzsspxaMaoRMCJT_KvdS94dMATS7DGT6g53c6zRof1eYFUEpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=LsZyxqBGdj7FZHLGoxyus9AzPLjRXi8kvJkABE1cbToYhKwIE9gvZvB3zSSYNKoF0VSuQCfL1_aesLJK9cqEF3SqLN71S9GbDIhhQ0hZ3vSBucpyqoFhzu6-UBJgoifQKhqgS1Aezf8luXHedNjRDjXgRVuTpp9bMrVMSG9m3tkpRPh7AWj781Y8dxeRCH8faeFb5jS92KmM-ekChu00gtWzyK3WJDtNU5vImGzZWmLj0ZZtERPWbw5kW5WDMJzHHZdrFyQVvSrqWmGbBud0PV0QStS4aZIKTbAehzsspxaMaoRMCJT_KvdS94dMATS7DGT6g53c6zRof1eYFUEpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسه‌درامدبرخی‌ازشغل‌هادرمملکت؛قلعه نویی یه‌زمانی حرف خوبی زد گفت 40 ساله هیچ عدالتی تو این مملکت نبوده از این به بعدم نخواهیم دید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27504" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27503">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unTtPf5-6rWSMXOudx5_KwDcXlsCi8Q1t_p6V5MbCBkriFip0lV65H-YCflpMH3jqOHn5OERbvN3NH_jzqmCxTUYcRI-CiPp3HgTpP6rGDTM0FMq2QDCQS8ksFEGvvOsHofCwWdz9YqXS4zhPnzUhEhhKGGh0bVBAy3b2LcC-3DO8jhDJJf9pIk43CEyWm7WfmYI9zL7YR3KK0s9jgtjfEqLrns1s3B104xXhVYVrzW_S4pFKdEQp-WoK1YhF2uJCqEcNrRp1wGOi9ZkY4oAMRiMYSZyB88X3lV6RMxsQI5prHqhbUZePNlMjsK2ZtS0XdFecu8wB9aYpWqd0kHAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الکسیس سانچز ستاره شیلیایی سابق آرسنال و بارسلونا: من‌درجریان‌اعتراضات مردم ایران علیه حکومت کشورشون هستم. میخواهم به مردم ایران بگویم که جهان صدای شما رو شنیده است و قطعا پیروزی نهایی از آن مردم مظلوم ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27503" target="_blank">📅 02:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27502">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=btQffqrMknvxQDvHWhYecBtT39tOGrftNX7i9aXSycuGHd7m-ZwHt3My9jvvPajk5znqCUna5XCxVcJBQsApB_Lj69WTKCCVE3E8YWe0g4AMiGvfKdA5gexIanMFSPy-NKDnjLsjqdKyHVHRqQMqfK4nzUsh1rDwCKOBsBLHr8MEauBdNJlHyfG-a5ovoK-yRAEy6gfB_W9cVDqlDd6eCuUnCPA8q_uNltz6JKSDLBaq5p6oC72JDPKRspzSSnEU_NTyC51_TIDQBOAurtwpF3wrXqALfbMOqQyfIAPId20SUvxU5Pzld3ndhBX8RlmUbW2FmGkKU7gn_mrvEnUECQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=btQffqrMknvxQDvHWhYecBtT39tOGrftNX7i9aXSycuGHd7m-ZwHt3My9jvvPajk5znqCUna5XCxVcJBQsApB_Lj69WTKCCVE3E8YWe0g4AMiGvfKdA5gexIanMFSPy-NKDnjLsjqdKyHVHRqQMqfK4nzUsh1rDwCKOBsBLHr8MEauBdNJlHyfG-a5ovoK-yRAEy6gfB_W9cVDqlDd6eCuUnCPA8q_uNltz6JKSDLBaq5p6oC72JDPKRspzSSnEU_NTyC51_TIDQBOAurtwpF3wrXqALfbMOqQyfIAPId20SUvxU5Pzld3ndhBX8RlmUbW2FmGkKU7gn_mrvEnUECQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلندشدن رامین‌رضاییان‌از روی‌صندلی روی آنتن زنده: بخدا منم‌فقروبدبختی رو یه روزی کشیدم. الانم نه ساعت دستم کردم نه گردنبند گردنمه. همه لباسامم ایرانیه و معمولیه. از مسئولین میخوام هوای مردم رو داشته باشند که با این فوتبال "تیم ملی" آشتی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27502" target="_blank">📅 02:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27501">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMmq2Hx2jWUh0-gYnM3W49LUwYZVy655GLj4XM-aQYdRA99xmR4XP4tA-jl4lu60S_b7QEu84t16N2Q95_1_4dIcv00QerN875sHTa-AwfAKEsV0IWkHTeDVGAnrAs9B0DVrzDSVNqL7m-1fIBbyBh9c5B4UoDB1fzrUv_zr511UzPIABVf8labIT_6poLehNytBw84i37UCNcvfBD9beDwpS4B6up5F20VhDcQHpEgJ2p-U551bxIlkc56fv4LEhbjv-9hfl_SQWoOI7Q0nnWYFzmeUlUiUiuAGOPQYKTwnQVTI_pSZt-6E9ZqTTz1HD8jkgQQPGUZCXBg66o2LjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
روزنامه AS: با صلاح دید ژوزه مورینیو اندریک مهاجم‌برزیلی رئال‌مادرید در این تیم موندنی شد و شماره9کهکشانی‌ها درفصل جدید برتن خواهد داشت. آلونسو بشدت علاقمند بود اندریک رو برای چلسی به خدمت بگیره که مورینیو مخالفت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27501" target="_blank">📅 02:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27500">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwp3K1l_oHlfoJEPbCfkKW1SBXewk9CpCDbnK2KZD7u_iau8haH-4vec4uuB35VoLbYySKwl5XqqWMKeEDUXNNPHIruXiQ0RdowGpai6cdzDWpIsj6n2Vn5WSy4Cy9bC07BqKF9_20wU2JiXRhdbpatwPz4cdGzZnspc6Usz_ImdxFfC-0mXj4mt7T4uYhJ0eTYrQsTCWsoh03a305BN_-boypY5Zc5o1oRv6X_hILtoUakTeDZwoFgcaLsGLFG163jFMWU91oAIP2v4XabwjQ5Irx_h3mB3csYy-smoqaypS5KtHOwuGrnGamsloiob_EmwZO6iExKJIvPBTOT5kSEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwp3K1l_oHlfoJEPbCfkKW1SBXewk9CpCDbnK2KZD7u_iau8haH-4vec4uuB35VoLbYySKwl5XqqWMKeEDUXNNPHIruXiQ0RdowGpai6cdzDWpIsj6n2Vn5WSy4Cy9bC07BqKF9_20wU2JiXRhdbpatwPz4cdGzZnspc6Usz_ImdxFfC-0mXj4mt7T4uYhJ0eTYrQsTCWsoh03a305BN_-boypY5Zc5o1oRv6X_hILtoUakTeDZwoFgcaLsGLFG163jFMWU91oAIP2v4XabwjQ5Irx_h3mB3csYy-smoqaypS5KtHOwuGrnGamsloiob_EmwZO6iExKJIvPBTOT5kSEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده: ما با پرواز زمینی اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27500" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27498">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=l5CU8nnFWSCsmrJbs7CLkiXAiIcX8DFzlWjjFvFzf0a0RKYRoMdtFPn-wkaTzTvQclUqtiNsZdoE3LKsEtzCz9LFKaPtywIOtUkBOY81jo4n-UybT6fBfU0qt6k1ElPF9kAAY2w9O0NVTtqKKW79_071jrXCAlMh0RG8RbppjM44AoemA7jp4hOaxyV7qdsuNgeSRgVaVJCSRvv4vJk8Xb0Yl_Jqxye2HPjE9m3geJLwQA--wjQyytlQVUvo1vg54EE0nUT1uWiXJqWgfGCH1KZcr_YloyATIfIctlca3HEzgdYBS3X-IStqS1dXkRonxFfAtjYw9S0itXzK1ugBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=l5CU8nnFWSCsmrJbs7CLkiXAiIcX8DFzlWjjFvFzf0a0RKYRoMdtFPn-wkaTzTvQclUqtiNsZdoE3LKsEtzCz9LFKaPtywIOtUkBOY81jo4n-UybT6fBfU0qt6k1ElPF9kAAY2w9O0NVTtqKKW79_071jrXCAlMh0RG8RbppjM44AoemA7jp4hOaxyV7qdsuNgeSRgVaVJCSRvv4vJk8Xb0Yl_Jqxye2HPjE9m3geJLwQA--wjQyytlQVUvo1vg54EE0nUT1uWiXJqWgfGCH1KZcr_YloyATIfIctlca3HEzgdYBS3X-IStqS1dXkRonxFfAtjYw9S0itXzK1ugBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
با اعلام باشگاه آژاکس؛ مارک آندره‌ ترشتگن گلر 34 ساله بارسا با قراردادی قرضی یکساله به این تیم پیوست.ترشتگن‌اول ناراضی‌بود بعد راضیش کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27498" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27497">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxjU52wYYXvr4a5WRgyjX-r8RbjByyQEICGuWzJLfvoAN7eBuxDztP_1w6Erjyqca8oNffX6sf79GCqIdprviXYXq-cyXXZTDjgsIW0ZKeJ3Im1t5NeuSL2EOSGWtCKwUUgs3c7IVp4eeSOsf6FXUWJ8QBLQy5Spo61mrnA78T1ZHpK8TutZRXxx6FzR06biMWeV9y5HUE0R0UaUFXUVuNrEBlRRS9N_rPIrwKHBc5eYv-0zbhWG_YJ1ch8GbljwfiTJvTLXNh9byve6rC89G7Z-lmDIvwHMjKOLjBcU8O8sdamXKo4c9842kZ-m-3-D93anxRybr7idedO-dOnSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌ امروز؛
از بازی دوستانه یووه با پالرمو تا بازی پلی‌اف لیگ نخبگان و چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27497" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27495">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c2114992.mp4?token=ncO3K7lDAOeCM0pA6URhVxKhHJeGDh8ULT_KB55_o7WF9h4kXJLsBfXytfofPO4Oy7KfzNJycWq76E5DEOMq_6FZhLpYxg8T4vpLm4hxuiO2B7qpbu8yjFqLs-ycoJj3mogTVfcy4IjyFEA2X0A049Y71Z1rTm3DVohiuz1QjPpq8MuH3KZE8A0LI-uacwvGgd70e7Z2vmEImU1QTX8TQAnEFaGb9mP9KCMVQY7AFioriPt0JK0wvlWDbgpoTgKeYqOQ7G3yD-a-vGHawVtTyTnepJ7sYJHf_OTmFHagUTE2vb6rqt8s-EH_wgBzgAfANKMrhVciwDt9mTkVukNc_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c2114992.mp4?token=ncO3K7lDAOeCM0pA6URhVxKhHJeGDh8ULT_KB55_o7WF9h4kXJLsBfXytfofPO4Oy7KfzNJycWq76E5DEOMq_6FZhLpYxg8T4vpLm4hxuiO2B7qpbu8yjFqLs-ycoJj3mogTVfcy4IjyFEA2X0A049Y71Z1rTm3DVohiuz1QjPpq8MuH3KZE8A0LI-uacwvGgd70e7Z2vmEImU1QTX8TQAnEFaGb9mP9KCMVQY7AFioriPt0JK0wvlWDbgpoTgKeYqOQ7G3yD-a-vGHawVtTyTnepJ7sYJHf_OTmFHagUTE2vb6rqt8s-EH_wgBzgAfANKMrhVciwDt9mTkVukNc_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده:
ما با
پرواز زمینی
اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27495" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27493">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxObMQPYCg9m1qBO0hmJ8ER_VtQRqQD8Gxrsy8eZy4MBCLacKE5XwGJlyM2Gss6xT256s8jUzGo2ljQMA4kz4QsFLXV-5yAgvyzmQK5PuL2twJmaOZytRjfn-IsjX_-LDLFy9Reg0_ZtTRZ2Ymx6Yi7etaFO0fqbGwX5fW_wU1LrisYM-nVThC9EB9ZS3ReYKUhruJvxY_HbQR2ZasALXzXHdrbHOvbeh4y4i-F47HVbaPnBbSsSI3Ph8N_N_XC4pQ9QgZhYqs54LVc8GsdAEdtPejNpF8QjLD5sxJ-r9xn8VL26i-AwDwSUet2sZBVCoXY-I0l7gCjYKOE-uGIgKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رامین رضاییان: قرار شد ۵ تا ۱۰ میلیارد بند فسخ قرارداد من‌باشد امامدیران استقلال به جز علی تاجرنیا گفتندنیازی‌نیست و مبلغ روکردن ۱۰۰ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27493" target="_blank">📅 00:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27492">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb8tXM-TQZLqIuC_kGrQVgtx-B63jA5t5j6REUsvGb6vwEW9Vw2sE-cnGAYRx1s9MwGMkDnDUsp3b4UruD7cUtu-V5KHmvl0rusf4yfP0BN8TvcyVN91UaoclDXeZt5OWXEPAqoDXvcmB2SPRNOpCOinvQe7Seu8MhsJPaBgU3dITYFXV0gLmG4Pq4KF34m1GeOEElMmalBHUui78FpiTCb9Gy6z8m9xqwx-055RgHeJiGjnizeKT-NMJ0aObEo36EFfZbGKH-M3UpbmzOCktDmuSDoknlaMIbRBIoABwopDxeQlWpdGrQcYke55vmVN02O2Jgf0qT0wRus3P_Hy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج‌رئیس‌فدراسیون‌فوتبال:درروزهای آینده جشن برترین‌های فصل گذشته لیگ برتر برگزار میشود و ممکنه جام‌قهرمانی‌لیگ‌برتر به باشگاه استقلال اهدا شود و این تیم رسما قهرمان لیگ معرفی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27492" target="_blank">📅 00:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27491">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4ApDb2srHiHMur9xMCtiWjC6Au1QYNJ3g0iJ_sMhv9abYrrb8MaZyAo8SWandaBc9HDmwa08PHl1V2mvirfbn-z70NUs1diWAzNcwdp5L1FSsZ_k_UKVIucFVCA_Ed79fGT4T0r2MgNncp7ihL9Ov6BHTorJaKJk97cLjvM5fddkBCVFwtgm2M85V6BRHvioVYQhamx2j6oEqMZZLzS093kww8g8oIPobwfHHNP4v8Blvf6zikkKWEECezGGOe3lscbqpwz5CrtCa4jFZLw5pVSozEIySXuhUS7Ym_YcDYvplKoBL8ulMdwP2yP5uicXrXvi7KJBDGw9OySQK4zWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27491" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27490">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK4iUMxZs4wwxkJEeN4zOwnTutDb64qKodC4kY8ADkZEVc1Q8w1ixiRDSfKV1N3_aYFw0lwpKAdZuhQf6h-j4EsfpLxaCPAJVBvlKrBqG4AE2mZDs-vFZBJkfF1tItWbG11zYSzJpAmPo3MJpuKVVsFKMSIZg_1xxSFD_X71NSzf1mfcTWEKJ5sF5JXIn8xpz0K5Lh_mcMpSzCB2IzzNjPLvS28EKaGrfIDK5yu_qG1xgNcAx14GjhDENqnZb6Iz2nxZu9bbnJKhIey9HQDsbPfj0X_-66Ycb5Qaa9gjwqNU0xpqSvxRy8HeMXNncuR09RSP119IapeNFFMhbgFlww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27490" target="_blank">📅 23:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27489">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifk9nA9rC8Fk9nkVUKRb1f2I1MuITo4UTluJMsyAns8mCaxSYrEFQHNUnFB3P-NIQ6RCiYmKQGfLzrOaa4NCoHFWaUOokWaj5xq2S2QJNjITe3353Xrnd1fR3ohLgV1tJ8dlDUGcbW5PYrmBy1D_SytIYLKXNfSfYpUkaSA3aY2hCRokX-t51480uP_pIoWJMx8xX47CJRZG2qQBwIYEPQxH2egddCJ2Q9vz4fDHF8upqniE1t0GjwZLZB4vo4uY18isbBZKYYYhB9PtYeDYmeUwKJ1zKdhUssnpdoR9XUFOLnXgWaRT7lrjdXOj8qr0U2zuEQMu_e6Ululxts2CvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سعید مهری هافبک‌سابق‌استقلال و پرسپولیس با عقد قراردادی دو ساله به فجر پیوست. رقم قرارداد مهری برای دو فصل 30 میلیارد تومان ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27489" target="_blank">📅 23:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27488">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8nd4Cn8bdBrRqsfNS3YKflqU5R9c6-SclyMs8lgLDOrqgcaZvJw_634GEWaFucew1Dj0bOy67S7K9fLiONO8BrIovpq-lOxiZj3jC3WWhg5dB2pqf-T81fMUqXFTCViw7IX46hVBqaR4wyoNS2hthOvhppTWI8L1PvkFqolo4EEN0mV2Xh9wzGISUXqZyEmBZQj9D7IG852KDe1yo1e88puHiyV-4Ht4sNGDkRzUqlSY-m3fq-5mGg_uq5BCgdhEYqSRhMrZtqVQnGTFrf1P67UM9iI-VJf7xRjyQ2nMp-PQd6Yf97IWS6M3iorH6-iK6nX3UnkKrr1A0AyqxuAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27488" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27487">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2M4DnEPCYE1twIj6RcOLXeN69Yr7Pdvm1oAKTKfBRB4AOs-09XxHLA_si3K801MPtAZqLQs_zHGxEYzN0jKBIqCNNn5r1Ii_3ftds_88Cm7LsrMzy5jcozXJ_5On726viax2_YLvx8oEV_yvuRlmjqYP7KLqdUGAuI-zRVj8f6fyR0t4icgr0JGYQ_4FZFu-TN5ViHCe1E3nr18pWO8i5Dk9Vd3nyXNBrXMWVhkAXCp-0U5nNPLxNY5j0RNhGHigepGLXEqcTpFXwRaHTulpzp5g3S-Kmwv7SQWRdrR52nE3Vxo3m-cs9iI2Ze2MGbKEqzn4_lp5A7UwRUdmSbZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27487" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27486">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czLDJU4I1eCZeTunqw9GGMWbAMTa6_wdwJ6W-P55FC-dQTzppNyUgk4brRFZJWvTdoGn4k5fcwuPVt48lhwkSWMsRcJy6CS5eFMQG3mWAmOs_Q4M7Oqm55U7PGq5DZiQ-ZKfhTYnJI-5w-Xh6fM0377atHryA034fEcC4EL4kuWOt9AvAxPqMKS592j2PdsgLIGbY9hBjLlwD-W-tp9jeUhC-799FjnvEcgrnp6kdWkJc9TrcF86B2X436HI6F5jtXFboYEaP6V3CTaKxQ7u0itKuLvdshZYuZAJEpaa2kALBx3S-XTKWLaqfviVOEj7wQkFJ8F0Ym7OTSzybF2J5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
ژابی آلونسو بعد از اینکه با جذب دنی ولبک و هندرسون تجربه تیمش روبالا برد حالا طبق ادعای اسکای‌اسپورت ازمدیران چلسی خواسته اندریک رو جذب کنن که پرز گفته فقط قرضی بهتون میدمش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27486" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27485">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZGn-YOBbGfkn97fRMjAPCEcyJllqzjXAjaNS2z6kgMonEjNpq7isC0-gQuIW9oRCH74UUcQ85RuM6C7BjQfttU_3AeRcCKQeNYNTQEeiaAICo19tPBFonmcPRweV-uz2V_mWKT8QV-OrmXBR29vQtib2Mhk3ttSTCsjgdSAUM-WhkSGjP9PGlsHa0ExVZCYB0TFPcUaXexD4Yjuzwx50Q20_Oq6gTEbY9f0oSLqx_bNu06m3kwxgni09REmFwNC3YZZbmJJZbyjUCtrMCJyETD3jgLITdo24eaVIkGTHA0y-5dPJIMc51aQDAIs4vpLlmbqbH9Dta_V7207j37KIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27485" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27482">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6mlw7U1jnJN9gGakrwhp9OVJD1dz07ei2ymqiWjjMbgMiuWMZp5VHM28FotiGK4-TC_ZekFCS2F3D_ssiMDXnrA_SVNeS_jArNm3BPd_O_T3kfiYAz3TfGbb3zTcnPrmXpGnpYYc37XnBlg5zFM4DqdKvRw1sBwOwY0PYyilTrAzRDn-xagiNID1f8FICB6bEkOslng-ZEM02u2B5tRwPzxqViHbiI5PmhPGm_heIj7U-ELqN1cdNnfmjJwydfG8WuV-VZF8qZQbkTfviCPSvrZM4HcR3jwG2CuGcpHWgPhLx430H4B4YsEbAxWKRM7S9uUazl_P8zzmJ-sE4hYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dn7skqo7h4qhkaWIVkt7ASxkPsxeAbK91U1EXoWsJogXImERuktDym28gRTh9ECXz6BuL1YT599dWNwcgWSSctIUd7BlMGX0ixY21Hw6uUJ_lJOi2_cm8AUD04z5R9E3zqLDMdgw4gamvBD1oMuJ8pv9YE9OAjZ-8CVBA7bW-VQGCRERpq8xjmv3pLVS5qw4504DW-oOedEt4uutRp_2QDix9FwUPZk84PJt7tAqIl6XzMyPYCWTQKeRQ1d7XtIhTG3xBdTMkqncut9UnLZKPbx-eWMjR1yxWQQjvP31w3l75gSz_psVOSncJC1aaw95Zir2jAoPzzCmaoqdBz8Ocg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
پدرو پورو مدافع 26 ساله تیم ملی اسپانیا که بهترین مدافع راست جام جهانی شد اخیرا به این شکل از دوست دخترش خواستگاری کرد و پاسخ مثبت نیز از او گرفت. دوس دخترش سه سال از پدرو پورو اسپانیایی کوچیک تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27482" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27481">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bvl-TCB4KedPl5r97Tgi8t3ciJ_iMkPsYBGMZb6zyH3yubPam8GZJae6f3ZZyd0KtG7R2LwPfJGr3gbp2TbR43OJaAxFOEvoH_i9MWBTYzR2a-puqJaKFldhXgJFzMBkZvJr62rV8vHm385D6A6XM_CI8luoVnuSWri57Q6Sj_3JNzgDmHTjtxpgSjoZ9YxgSQsZoEl1NJs4WVD3hzU2wgWieC8W6qCpfBH_RSCZroVUbmPGZxyBHwSMAefFmdCgE6r-AIATmEcC_T-l4DDopJMxX5UABgew1eN5Nh3VOwI0uy-QGvNqYOY8mSjrLDZ6tsaKyNTAzjsxuBM5MQnOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27481" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27480">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSqXaMB9y2Mf_WDnpD-lxie0HfV_Jw9RSKL1vtC6XGB2qrCuMHdTBfVlgdgvCXEQpx2v40Lfp2PBO9oUZFpwgOtLGSvFQCZ0sOLXcY4tuHwQ_IKqrJbkUnhC_QKInYTI198sto0kE9kY5S9txxdXJQRXtHIJ4jVSVXSOLJ9SO7yMQnaKzGriGsI_GmL59TE4zeuTBHK6Mb7ebwiXovNHhtNGQjPJ0wea_5VcUGlqzCDOx6yhRsP6MXhRyBkF7Ca8wWdnwkwpiHGD8oSMKrnzGskXddlJaIzAqicD2OgyxXIwBE8i5dFendy_Hwq3JdrSprkbOJzqD40Xp64SWqD5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه استقلال؛ استعلام فیفادرخصوص‌قرارداد یاسر آسانی صادر شده و این بازیکن هیچ مشکلی برای همراهی آبی‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27480" target="_blank">📅 21:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27479">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bceG_3mH-yMDMbou2JHqxo9bxhwkwwn-jywVdAj8h7VtYlkbtK8FyRJlhS5x5FyXwDHKuw2fC-iiMfT5IaN3KWQpmdH7Fd7A3RuW4d6Pym9Ygx8-YsHILu2aDXLgsGghjbvDyLLGM-ZBxx-pzbaK-sF7T5mR-AGn-ix-DcJ1RDAXUKNO6d0XnTX_1BLqPaqYFk0L_tshRAG_xCcBO21QWi8ubVuM_IgBFBwOQHhYF335HTd2thFECOqv5Q8znDPWXkLCy8j-WFBPPsPjTaisWlIF0J_6_pp97-D4Nzmh3kORheGzkR4Ll_oZ0lhRT5hnZmnfT7eQ88q-QUpew1XxoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27479" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27478">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnVWeiSnCUNyGUBy9SI7-uOO_BM5I-IXUtP-bnNMP4sS9oItoI6BV9CMFrLgn_rsrB_yN9eA4Mj4dQSb9XUVuIDFQy52_okjD1Cjc02eukjuREQhFWO0lAhAYccktlPrJ_sTHK3-PUY11KZ9bLG49wEQe5flD3zERQnjhDpEWeaLqjOi76MpKx6LiZFRoGEsI9sz1lZBH7Lv69tfOAT0bsg_Co5jK-QmI-9sj9Q20rjAE_jSfDC8lGr2aNHSn7InJWJr-13CXJPRYxwgnrZVOyqU-zZf8kSDTOEkbYfV0o30mCMKuqcxEwz45B6ONl7ChTqBDfomMxh_IKRnPTlyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27478" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27476">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edtf4-zZmBW-4pixpXKm5L0I73MRxd4i6goceKvqwrzrho36tJlsFXuGaY6r3bmbwWJDHiHpzJRTUWgJIsdZN6xRXhbvCvfjymviyFdwCTMtF7_lQ9KGpFWH61nWr4McfJDRwJWwn4Tlkqtmk1oDCvZmSiXUOI1PH5J10fWiQhth1yG5L5S_JT9GoiwngkQNafm87E42zU-d_OQOcRb4dsc8LbKsH5NX5Qy97Z6IT_7Yrb4JLPQovy6Ot0PiNShbtCJBoPLA8kyQh7XAB_haOEyAqfgj-JJsqGMphXCotEGMhgi6GBcsBpnMHU8YcWzYuIcmyBFkQJYFewpojZOBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از جوزپه رینا ستاره‌سابق دورتموند که رفت آرمینیابیله‌‌فیلد و ازباشگاه خواست که در طول فصل براش یه خونه خوشکل بسازن، این درخواست رو بیله‌ فیلد قبول کرد و چون رینا توضیح نداده بود که چه خونه‌ای‌میخواسته درپایان فصل باشگاه بهش گفت که خونه‌ت آمادست و با این شاهکار روبرو شد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27476" target="_blank">📅 20:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27474">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNPOvrPJwfBSsZMolEQ6N_snkbAjMJRGI_5x2LFUJ1sKXVLd4R0g8akhvDJcLjeC2I1phYUKFgn4uKjXbv61pakSiQEz5m_mvb6ltelRfBBWucf9yJAP8xnG-3FNTEWrqHK9cOCVug4qtIvt7lcmtvwx3XEhOUp9OYNiHhN3JNUx1sAX-VUezHxJG-MO1YGdH4vJ-kc76v7eMR4bZqiYJ3_cFEpAbWm1fKjcpEHc56yXsvFQzjpv5INam4bZvDPR13ro4OnJXZrZ3z0Y9Opaej4u40NXsuIFB4ii-_a1IRD6kIIFkSYLb6Oty419ThYmgA_SmftNNmngcT8PRNQqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzbGG_JACFcce8ix5A3D6Q4aMPWQpvT_KXBjvcHKe_3tt_MsLjncSigj418yy_X2uekJUwwtc4w9nejXdVslyjGgnRh-IlW5vK78pzP3_fCGLSeImLdt9cSJMMulgaKb6HxlLit3w_2gGrsGCQVL5dzT9pCL4Ii2WPfTVs-y2cpjLGJf47Yvq4ZusFoH464IloOlMN6wVjlk4kUtcJ8Hyq2BqZmgSYgTx6PWHpmQLcVU9jaF0hcxdZtrXr4_i0u_UPor6sezC4eg18PnXJpYASXrIdJ22PGmuTkTj77UOBDcb9o-0Df4n6ApEIFLh4TAydOYr3Qc5k8iwAZEk3-VJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27474" target="_blank">📅 20:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27473">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZUGL4uUGHxCUJvVdLeLrlECQ05AjRxJM3w_T9lW6--PcmthTFseKwyFBhSbhkAtXNUvmZcYVo3bSef73n-dCL_zVP-LcU-wr2cJi9AHb35HcgBMYvdukma0SapaAqTpnX6Uagn0VwxJMcaSdob1HcpUc0Oi_HcHl9mLD0q3nAmeFj3MBfZKeE3GKLb7kpTZzVrXvpsfrVixT8vXRSi_090x_JeH0-EQzkR82Cz75x7S3VedEPDcLuSWEV1FCWt-Wm3u96jf1SDHBEh8prr8JnvIYRLdA9xpl-1CgnsXmME-znfO16qbD0X5cne2jLbYvVa43Zrrqd5NpOuL5G2CvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27473" target="_blank">📅 19:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27472">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljMWQcKTUmwBWg5CWMBs5heUg0ioL_8CQ9Vpcbi5vbfPkzQpR7iiEe4xBwBI5R1vVLWPbUrEm70EfHEjX8bDZf5_NbnO_8bstHDr1FVmOLmjFW9CwicmKS59z9nSYE1YP2YWvNBN_PhC90ApUtFDlJ04wPSXkVwHBfJ70aW-kOkzOXpuaSr5zrhx7q9w4kqcKDcEHNXBYrZwve3SoaGmQuDXOf_THd7GPPhsXCAzfLpoUq3C2SBuJJBruMpAJ6OnCaIjPw8-9Y3fmTuvCVXjtbw7bQFAyNrIazoj2Bu4delMLOtGN4Gca5trVmNqb8ldeZ-0UtQWlHfzkBVUek8zEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
ایفمارک و زهره هراتیان درحال‌برسی پرونده مصدومیت‌آلمدین‌زیلیکیچ‌بازیکن‌خارجی فصل‌گذشته استقلاله. درصورتی تاییدیه ایفمارک؛ سهمیه هشتم و سوخته استقلال تا پایان هفته احیا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27472" target="_blank">📅 19:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27471">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=pR1loBpG4Vynu9qtyYlW598tGQ-nfCLXuPhlRJh-roR877Zg8FU_9Vr2wLRgc1flKyvy1biiAHpwAQtuOBroHoOsZdRjZWSFMdrLBfUleDdWmC2NVNr1Z1HTCemDSLB1uZKUX-nth-zmpJ9BPexLMJ5ipGSpRefWIU6oIC7DbrvcHfZSJ8WWZxud1NSo0p0GJSik_ssN0MmW18dt1ITsBnHPTpbryBy5i-kK__LQ1cVGgJf3l0Rr14OzggKiaMsszSEYts36srQxdwg6Uj8a17Pb1Nz8_cDtFRJ_leTYpMU6J3CjMvkbKd17DMwVi7hQA2A5sna_E3sq9wtPa7DgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=pR1loBpG4Vynu9qtyYlW598tGQ-nfCLXuPhlRJh-roR877Zg8FU_9Vr2wLRgc1flKyvy1biiAHpwAQtuOBroHoOsZdRjZWSFMdrLBfUleDdWmC2NVNr1Z1HTCemDSLB1uZKUX-nth-zmpJ9BPexLMJ5ipGSpRefWIU6oIC7DbrvcHfZSJ8WWZxud1NSo0p0GJSik_ssN0MmW18dt1ITsBnHPTpbryBy5i-kK__LQ1cVGgJf3l0Rr14OzggKiaMsszSEYts36srQxdwg6Uj8a17Pb1Nz8_cDtFRJ_leTYpMU6J3CjMvkbKd17DMwVi7hQA2A5sna_E3sq9wtPa7DgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
عمق اسکواد رئال مادرید درفصل‌جدید رقابت‌ها؛ کنجکاوم‌ببینم‌مورینیو با این اسکواد جام میاره یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27471" target="_blank">📅 19:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27470">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=vmA02NBdNz2JsJZbzpJmIyRRiFEvnvvxXLax296l5xcfhhH3Jap8Mz4bAPJu1oStX6hEUZkoBdPi55c4qDVs1cWzkWUKxOUC_r1vzejB1b1MqevuI_KOooHzyfoJFWSYTB-ikFilMS0LaVFxtQ5HM6TZQi_sGWP5kMUxkNp7nAgLh9gbodCN2TnsoIO_Lh5uoTj9bJFQdrvWEYKAbrYunbiXnLh4i508Q0_Gw2LWLERnttRXKqs04BXmJJHHVmFxhSlPu0yhD5h4nMfs4QcTyG7a84hQfJKBdupE7ru38SmHOOtBuoPkzcUFgf6xo6xLcEjvXisryje1pFknABq8EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=vmA02NBdNz2JsJZbzpJmIyRRiFEvnvvxXLax296l5xcfhhH3Jap8Mz4bAPJu1oStX6hEUZkoBdPi55c4qDVs1cWzkWUKxOUC_r1vzejB1b1MqevuI_KOooHzyfoJFWSYTB-ikFilMS0LaVFxtQ5HM6TZQi_sGWP5kMUxkNp7nAgLh9gbodCN2TnsoIO_Lh5uoTj9bJFQdrvWEYKAbrYunbiXnLh4i508Q0_Gw2LWLERnttRXKqs04BXmJJHHVmFxhSlPu0yhD5h4nMfs4QcTyG7a84hQfJKBdupE7ru38SmHOOtBuoPkzcUFgf6xo6xLcEjvXisryje1pFknABq8EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیتر ورزش 3: کاپیتان‌تیم‌ملی به صدرنشین هلند پیوست. واقعیت: کلا یه‌هفته‌ از لیگ‌برتر هلند گذشته و جهانبخش رفته تیمی که پارسال سیزدهم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27470" target="_blank">📅 18:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27469">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffk55295cw2_4VRSsHGkl2ibwRS-mIvEJfvPDgRtAOui_9rvx3tvFQlLBLhrW8woA-tvXW8dmaTPT9-fadE3zhv0hjj1uOVgsWHHsQcY4RFV7vD9z7VX4HT5ROWthLZamtCYlGqdxu2p3Jn-f0A5zB1DkzKz9V93jiDtxUJHFWq6wcmPvLKqiUBTE3C5ZbvKfVvWpU-LxR6bROHGvlOVrm3wRcO7tqdtxonujNpqZ9bEr_uG_DqmSfpF0RtZFaHLetAhWec3Tx5w4gpZw1_7jdlfKIRKlT9MztO3Fgry-QZiX_VCvnxWU_w-cmSH1CSjUp9vcMfwPvWCsk-4NkCsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجتبی‌جباری اخیرا باقراردادی یکساله سرمربی تیم لیگ یکی شناور سازی قشم شده؛ و بعدش سریع مرتضی‌تبریزی، امین‌قاسمی‌نژاد و داریوش شجاعیان رو با خودش به این‌تیم برده؛ جالبه هر ۳ خرید روزی به عنوان بمب نقل و انتقالاتی به استقلال آمدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27469" target="_blank">📅 18:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27468">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDcew0OSWCwpUSYVqoU3cKOfqjnHDtEi1sK3fsiknrI4rMLJLPRqcX0BMfqZhoc7W-uIullbPbu8FXWRqrWmcqMOw1SIOZ3HQZKTsQa39w93oaeA46eeVI7vf9QiEhO1XYxZ-FRMpqX7M8F5ufT_gyaxZsLTDf-Bs5PdA07ivFZVTgN8CAaBAVi-TgfwqmItkLhNUdq3iMpMPFvtJV3XXba-BdhL5SewlhCbgT1wBfIj6YoPJ-VQlda56X2cjtt5wPnWhH75zCrMjc09fDpyUxWPAxk4f7by_Am_PKHATLZsf5VAZUC7G2kmA2uttQBf-ZwpQxw_M8fqJTl8yiSnOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🤩
برترین عناوین تاریخ‌فوتبال‌جهان در تصاحب کریس رونالدو و لیونل مسی دو اسطوره تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27468" target="_blank">📅 18:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27467">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7lFZsCFyLyVgieoL_PTs7h500UTwApvdSCjkELiBYvESr0yfIdRinmrIdfzDdNiN9DPsgfCVXFoC6Wf3vDkTgnkLsKSrcB4xskq0CtIZmExLrG1fIqXwCfL1lR7TcTAEpUJegJF1BrtWJkNT1n4GRMh2YEyFFpca6VcFTvJPHiD_eyv4TYI-nAyAheEPR3cGrR5asrAB672VDAsOqAxvdFdQIDk9RshFV9QjYaU4C8bAVj_z4ywC0zbIRSnbNRpEsh21cbWDJAQD-_hTx6Cuj5Wgiq_kKcI4bZjg5FdUMi6L96-9XCWnA_BxAfrNzFlfu4LpIZNie_cmsqAoFWLnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27467" target="_blank">📅 17:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27466">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz7kyV5rKwFAzSBl1SmvylEXB-4PIxY_pzb1eLeV_THSK3JJd-p8c3_lDwMyZuOgjefZaWIZZPdBjW8qlreorVN9IjaUrTOsVRUpmgnZyVVdMh0LNLYHS6SZWVYDTNXKmZgV2t5SifXRhwVbcUnwCMoJhwnhauXXsnFvte2qlf02WRqjNW20c3WvVs6l9te3gdDhVUdBZtvfxUPAxP6P7Q1dYF_zA6nmflPs-3EbN4p5kg0PwqAmwo3jiSgJNIgft9KZ8zrS5wo2MceEQr9vHjFbZwc0984ZcqLXiWhw81w3UXeJQPEjE58Pp3vQ0i0L-5ecfMYcxSxKBYg0xv7vPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه‌دیدارهای هفته‌اول رقابت‌های فصل جدید لیگ برتر؛ تنها چهار روز تا آغاز دوره جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27466" target="_blank">📅 17:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27465">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB75ww_URJu4YuyJqBh9i0VusQGWel2OM4aYFunc45SkTePetrLc6AbkoqK0MoWr39XVoR_NOwIw4InMSDQryt0CbAoZEW_9wuMc_JtzH5v-Cp8VPiCs98UCDZtModJIb6DOrUnmDWoDZWP8nGJbBar_hjNIrLPZRoASbL73EeA1ienkrgu-9dqz9PUpRixvRhiiV-g1PQbQb0DKf1dnl_MkOdwugEY1lrXPumsBiGjDFds_l-wwY4mqRlNwnCiyxVhjN4ogHvwOOTtWT30s04rvtGPS6xZQKNA_KRSYvBAriiA99vLBhjmkYUxMAlIBxCUEP4gvQ4GFcUYh8WL81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27465" target="_blank">📅 17:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27464">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=AEGkwlWEYqzuJeULwxGt9_E0jKnwf-JwhVS_d5p6FaGaRivxSTP3hUt-CrN6lGMbq-n8okf-RLZqtNVTMJPp36bRy0vVLJ1oeSJjnWFNXrfhnCs6ctPtRTbg7ZYursoBXg1pX2rL4TCslHNz4z-vaMpLVX42aG3wTUQAmRME5qZqTmV5q9nzFQLqyAwqzgnbiOwys3fJ2KPp_RoyUaYfdFLEvvUMrK6-7Is-_1pgVcUgko_z4QoGRWHCoed5W93QCmdZRO-UlyVMO8KXXV7KntXesORNnLf54CfxoNC2IBbV-eqhHnoz-4ECrbwClwhV-6DS7ukudYSt3O6gJg2XHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=AEGkwlWEYqzuJeULwxGt9_E0jKnwf-JwhVS_d5p6FaGaRivxSTP3hUt-CrN6lGMbq-n8okf-RLZqtNVTMJPp36bRy0vVLJ1oeSJjnWFNXrfhnCs6ctPtRTbg7ZYursoBXg1pX2rL4TCslHNz4z-vaMpLVX42aG3wTUQAmRME5qZqTmV5q9nzFQLqyAwqzgnbiOwys3fJ2KPp_RoyUaYfdFLEvvUMrK6-7Is-_1pgVcUgko_z4QoGRWHCoed5W93QCmdZRO-UlyVMO8KXXV7KntXesORNnLf54CfxoNC2IBbV-eqhHnoz-4ECrbwClwhV-6DS7ukudYSt3O6gJg2XHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
توضیحاتی درباره کودتا شبانه بزرگان تراکتور که منجر به برکناری محمد ربیعی و آوردن نکونام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27464" target="_blank">📅 16:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27463">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVgvj1X2vIqaL-AXz9VxST5XPGuczsOX5JQT-94iMroOsJoUj27Lcfp4L3sSklcQ1Sx8_NZIsEGHQdvSCkDz-Jow-N91ZwrBi2HI_IHuR0gm1TAecqUK1PSQQL1aJUHrcFz_Utr9vMyXFhYgfQZshECv3iNUcDz8P-QTkGX4LClZhRPEUCCqh_BNcx0dgG34l80Un7V6BSyQr32_rhBz1lFLM909BolRcxrkQeWtYlsQ6FfszZFc5IXqJOAUeZ-uP0vhfDoHmKSKLgdCpCzQuu-XFYYbrp5sffWrsx3MXVoFqUnNae_V6HbwcMKcJl-HOzuy63JXKigJeL9LfN6Iew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پاسخ علیرضا جهانبخش به سوال قیاسی به اینکه در آینده به کدوم تیم استقلال یا پرسپولیس میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27463" target="_blank">📅 16:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27462">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_5jdofcXZ7ymy3Z97usPLc5W2lBfec3GoL5w1lXslSlqvebM0ifmVvFkQrt0xXy_ESE6TRWTUeIel5eZg7vAL-y6qdkdWjCS_g0tuYVEtessU3XEfYG2lsuTsjmsCnqBmQneQrN50YoUL_ArYu6bU2kWqVFqjspsyGtUntrQ8enPy127nY0Pml8ZlJk4ECpcZxNQ99eQ9xQBHsZsA5ZIG1MVLYBHqgE_w1qmv6efusu0AuDge6QvVSJGJaEze0slC-HjkkXPDehFx0wXZZYPhwQrMuMyGeYJqq8Ca-UWdiC6wl9TqVBrYTn67dP18Pp1K1uBq6ODJ2mYtUMNMk9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب احتمالی بارسلونا برای فصل جدید رقابت ها در صورت جذب قطعی رودری و خولیان آلوارز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27462" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27461">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8AvpLx6vtib87jAPkpYGDiUtSHZm3_A3jYWm_LkEqQlfWgES2AtZTeBzxWQdFle977bgHPwJHNK_UwiZaItd6YPwISnyot84t3fG70YFFlc8wx9HbAxii-_7VM_lc9WkHFgHllprpeYuwV32uXocH23TZQPqgixQR--w2gM79ZSZ4koZgYIqus7n5oo9oprA24QxHlSDc6yYO8uZdifQRHHACXsZM33rhTXodX652m7_1-T3kH0nQZSeZACEFAHKzf3Jcd9LoTGb6DfmAilu-wqiD_in5E6GzK27shWz13wNgo0oAM5x9tkA0X-OFPOepy2Pwty2KoTr9sL1VsxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باتاییدیه مایکل کریک؛ مارکوس رشفورد در تیم منچستریونایتد ماندنی‌شد و شماره 14 شیاطین سرخ درفصل آینده رقایت‌ها نیز برتن خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27461" target="_blank">📅 15:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27460">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwmi0BaBNqCQ9bY9HzcBvM7n6x7oeJ-gy3hlhOsodt_DKMRYm1aEWFH6442bdE1Y8LUuVtalZaUnruadczDNcq3U8hYxJQutaYCFMxVWrxjMt5GaCnufLyKoXZTRj1FJv6kmkDNdvXLgJm_mwVWAAGIq99ERrji9Qj-By0FSctZYgAhtMUT4QMNozfGpN07QZaJw7tNzoJtf5pTS-dPluTnA6nRe_KyJRGe2qH2BN0rAbmwpf2pOv1fc29hu8H3VBrRTZFSF8IfGJRKGwhqhjUI9hTf1OyQVAxFCXjeJQxee3-lr74daMPRx2A0Jt5AaQfCTGrkGj3HwEq7YHYrheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خواکین گیل مربی اسپانیایی جدید تیم استقلال فرداظهر برای‌ عقدقرارداد و رونمایی باپیراهن آبی‌ها وارد تهران‌خواهدشد. خواکین‌اسپانیایی دستیار دوم بختیاری‌زاده و مربی تمرین‌دهنده آبی‌ها خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27460" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27459">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLD7zjXobBGb0Z_MNhn13_T7VqGglCWS16qx_-sQa3AI7eVHe1Oo-AwSMUiOWJxaD7p9-RnkpaLICpr7H0eJ3gD4KAw5VwXGLjPHSfqJI-6I8FBViont5iZ0h_X3E02Gvlk7X9z8KKRGLvduj_uPNumuHgnHzd7pd4gD7AjK2zdAc1O0pHmjE6uWOFRiiKwxuwljQdNgcG9Ex3aTSz1QpDCrgCMLAKZdlhiu17CZuF6GyseZjqqOYflf9WtSywm4rfvKyzXTNTYPmtMvYZMIKwPWy0ReABU5gB8w9_IKJ4sEu-6SUVW1msHRW__Zo07Ep7FbbrVMOt2rUd1uJv1F_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27459" target="_blank">📅 15:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27458">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643163ded4.mp4?token=IyeZc9X2lngaCcUq0b5a-wkP0RN-QazQQfl1NaKlneh_FJFdeyig3XpPcpxo2AJrTroz6fDCBTs8bGrnxAIBn8A8WAv2Rraq4aY4ao1UkbMIH90u0ckVMDY5aZqaqWL9GpWWlrKuKeXu2-fu4gvo9EWvKtIWsRjDWgaciRKwndJP94jxdQrqmAjNRfYSOZbx_xSlob8o5h0Ag-0jBhV_Myoy52edZ7kxYjyllmt4qEFGrBCOJPCyU2j_I7oRpm2Tjla4eLBLhz8BBK9CbSzzpNTSoXarKro6t1sYK_290KU50htyx96EBtDqVWXbLp6G5rzuvYRFEs1WnEqkzAaOZxrrdoV0oLFna2bjuwUUpkc0lAu7Co5H6rrxm_i-39sv4Z00kJ_2Hch5HFK6p9WkvUwgurDY4wCURRYRjZ4pfabOrh8fSM5b1AJhCa2stg1OaD8Mssi0wfFsELwAi5t5u1EhB0JTCDdwR7YucC9PO93TpVHMG0Mz8VrAIFkKNJlapMCQVkTUoR_jCMu_C8puSiWtn7-b6K7lxR5ryW4hWyeUcilUIKjTxr8SZDIXExP7arvNDKcuvxVbjNLWEUMWMXlGsmuTrUCsJ3B04UzxaPWp7TBwDKvrUjMbMybcRByRtfwPT3VqCeCJ6R8TabEOgOVLrPFQ_DV6cXnNeNflnYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643163ded4.mp4?token=IyeZc9X2lngaCcUq0b5a-wkP0RN-QazQQfl1NaKlneh_FJFdeyig3XpPcpxo2AJrTroz6fDCBTs8bGrnxAIBn8A8WAv2Rraq4aY4ao1UkbMIH90u0ckVMDY5aZqaqWL9GpWWlrKuKeXu2-fu4gvo9EWvKtIWsRjDWgaciRKwndJP94jxdQrqmAjNRfYSOZbx_xSlob8o5h0Ag-0jBhV_Myoy52edZ7kxYjyllmt4qEFGrBCOJPCyU2j_I7oRpm2Tjla4eLBLhz8BBK9CbSzzpNTSoXarKro6t1sYK_290KU50htyx96EBtDqVWXbLp6G5rzuvYRFEs1WnEqkzAaOZxrrdoV0oLFna2bjuwUUpkc0lAu7Co5H6rrxm_i-39sv4Z00kJ_2Hch5HFK6p9WkvUwgurDY4wCURRYRjZ4pfabOrh8fSM5b1AJhCa2stg1OaD8Mssi0wfFsELwAi5t5u1EhB0JTCDdwR7YucC9PO93TpVHMG0Mz8VrAIFkKNJlapMCQVkTUoR_jCMu_C8puSiWtn7-b6K7lxR5ryW4hWyeUcilUIKjTxr8SZDIXExP7arvNDKcuvxVbjNLWEUMWMXlGsmuTrUCsJ3B04UzxaPWp7TBwDKvrUjMbMybcRByRtfwPT3VqCeCJ6R8TabEOgOVLrPFQ_DV6cXnNeNflnYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک در یک برنامه دوست‌یابی با حضور ۲۰ دختر شرکت کرد؛ اون در نهایت از بین این ۲۰ نفر، یک‌دخترروانتخاب‌کرد و حسابی ازش خوشش اومد و حتی براش واق واق کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27458" target="_blank">📅 14:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27457">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e350019bc.mp4?token=dmu5dTBcq38dVG8ocEth0FtOgp6z7uL2DZnIoJ59VPiYxtcJ9-up8c7GpMNVTneIweoVxnRStJKVI9KS5EmR5S1_IqAT1a_DDZ-uZLZrjrNKLCoq1yvS2EUh_tJbjTlW2fKZQLI45bw-BjSeh5TW_8epclrvY4ZFctgdyKgB2r6naECYR3lXfW16fTVeZvqWvmUrCz7L02zvt_QSojQgigb4hf-rORXpaIjlr1qqnokNy9nwGeAanwDRqFHD-EaEyIJQy3gOVn3Ro7bZIM1FaJ_ZZaQeCF1zE5KaMXDoWqCy5W6YKTi4efHXR0oic1gbuPj2kcJiWjJQKlR4sDIMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e350019bc.mp4?token=dmu5dTBcq38dVG8ocEth0FtOgp6z7uL2DZnIoJ59VPiYxtcJ9-up8c7GpMNVTneIweoVxnRStJKVI9KS5EmR5S1_IqAT1a_DDZ-uZLZrjrNKLCoq1yvS2EUh_tJbjTlW2fKZQLI45bw-BjSeh5TW_8epclrvY4ZFctgdyKgB2r6naECYR3lXfW16fTVeZvqWvmUrCz7L02zvt_QSojQgigb4hf-rORXpaIjlr1qqnokNy9nwGeAanwDRqFHD-EaEyIJQy3gOVn3Ro7bZIM1FaJ_ZZaQeCF1zE5KaMXDoWqCy5W6YKTi4efHXR0oic1gbuPj2kcJiWjJQKlR4sDIMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
«رودریگو دی‌پائول»ستاره‌آرژانتینی در بازی بامداد امروز اینترمیامی‌روی‌یک‌شوت تماشایی موفق به باز کردن دروازه حریف‌شد و به این شکل گلش رو به لیونل مسی و پدر از دست رفته او تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27457" target="_blank">📅 14:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27456">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd69k4alPeEZeTW2cEwXrVmmH8QsFQTf5exbvFE6NTlNturBy2aznjy7joZoJcZ-qSc_eHuFMqG4v1qpF4SqYK8k5JFfJ9hWufFrWqTkEX0_Pu-6vDsR6bKrpbsmHrBgUwSsl2Yzt-cfAR_1JdS-fIdbouxKO9PlQrmcBOWAr1QIGcnIhxUhXVvskK-7WjCc8fyOhFs7sy0ip7aBrmw9Yh0YohJBiPP1DPOBG-Ovpa1ObMwzysYofNBAlyLBUklXBBEfOCPFpo7tdUGuexSfboinUTF6ne1b0QwsvG77-Fzv5KQ8ITeH_3t2VvZGzNQ_7XtQjrwZMyoEwm4kxRAjfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
کار انتقال فران تورس به باشگاه پاری سن ژرمن نهایی شده و این باشگاه بزودی با فعال کردن بندفسخ قراردادش از او رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27456" target="_blank">📅 14:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27455">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAscwcK3D4hhGy83TCA5CgzE0CcUgtShLPvf1dPe6HG5yFQIf2JNyWWqKtmYPCgXc_mePz15Su742plZSQPzOt3Ofwq2iWZu0X2BCsNQX-5RnRTxVQFg6704PcP3DABJu5jQaWwIqV6fHTvRfcpNUsbIj1o_mQ1QM8mKsvraS2MtL9ZcXlckdKe5Q_8C6CK3RH1M6Fci6J8yAQoje2F2GMshp6cz-04HAr010rGkB3AXXmPSeWFZ18nVYi0LImrB6_93thUmSTN18SyVTkH7DNJduZDjU85fMS12SY6Uo6vG0cwW1E4-KupXDkyIzLDTrTiE9XWa0SHvfprT03mSBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🟡
#تکمیلی #اختصاصی_پرشیانا؛ فردا جلسه‌ای مهم بین مدیران دوباشگاه تراکتور و سپاهان بر سر انتقال آرش رضاوند به‌جمع پرشورها و پیوستن تومیسلاو اشتراکال به سپاهان برگزارخواهدشد. طبق شنیده های پرشیانا این انتقال فردا نهایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27455" target="_blank">📅 14:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27454">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e058bdf5.mp4?token=NQ5Z3W5jKM3wf9kV4Ln9umeIHJ4N7iGbQ8HRkuUAM5UCusOoa7F5xMfd6Gjs7F0AyzachALo7kqP9LjhI-SGq8IqEhgL-F7ueUwmPqn4z1x87a4gsDi9ZPNxktvg197WFq4p11uC_6cxHZktTI-mHMo8MXwRAudilyPQivRJRnPgIfY49JyAy_hznEbb9N5jOuUYw00QbcGX5-bczLofep1zKAUc7vaBwPDWxcbimqLIwbq4XWTQD7I5uQhfgaUUptcurBlRw3MsU4VWmXFpitGRy4KlsxEc6Abx01p2EPNFaZAS_60li3Fy5V-DBDpocl-HoWuOB1RL--Xzfdd_94-dWzCTVmAhnjqDgegUB5NK1VaPjBGCmURAkgAb1hIbvMAESoumrVe18lFElE4rYlvvFa-dmMkiN8Cw07Nwd5lQDXLJsqnY20w2Kz2QJ6pfADywTYIXBLprwQuOVzg6JbzsdDxdWJBCsj4dHh5uCRCVIvQlaVLSdIhxPTXWC9BNAslTryBpUfaurz7EyDwyfhuLoEViLCtGViaDISTOIIjnLvQl_vOmraTaha5aVQK4IIdQJRoY9A_Y7SHwvWQ7To_Z7tPXrbbtnX95CaV_M6KUfVF-onmPjzQWs9qdA03U8oXIR2CAdn9EL8K9wrfanoA8NRLkokhhuGdKj6r4NgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e058bdf5.mp4?token=NQ5Z3W5jKM3wf9kV4Ln9umeIHJ4N7iGbQ8HRkuUAM5UCusOoa7F5xMfd6Gjs7F0AyzachALo7kqP9LjhI-SGq8IqEhgL-F7ueUwmPqn4z1x87a4gsDi9ZPNxktvg197WFq4p11uC_6cxHZktTI-mHMo8MXwRAudilyPQivRJRnPgIfY49JyAy_hznEbb9N5jOuUYw00QbcGX5-bczLofep1zKAUc7vaBwPDWxcbimqLIwbq4XWTQD7I5uQhfgaUUptcurBlRw3MsU4VWmXFpitGRy4KlsxEc6Abx01p2EPNFaZAS_60li3Fy5V-DBDpocl-HoWuOB1RL--Xzfdd_94-dWzCTVmAhnjqDgegUB5NK1VaPjBGCmURAkgAb1hIbvMAESoumrVe18lFElE4rYlvvFa-dmMkiN8Cw07Nwd5lQDXLJsqnY20w2Kz2QJ6pfADywTYIXBLprwQuOVzg6JbzsdDxdWJBCsj4dHh5uCRCVIvQlaVLSdIhxPTXWC9BNAslTryBpUfaurz7EyDwyfhuLoEViLCtGViaDISTOIIjnLvQl_vOmraTaha5aVQK4IIdQJRoY9A_Y7SHwvWQ7To_Z7tPXrbbtnX95CaV_M6KUfVF-onmPjzQWs9qdA03U8oXIR2CAdn9EL8K9wrfanoA8NRLkokhhuGdKj6r4NgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛ یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27454" target="_blank">📅 14:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27453">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454a762bef.mp4?token=PXsiddO_V7yHA9rd-t9RLObPTHg0gAEDceBKX4mNpyNhZhdIXwWr8RH4P8NduKEI6yLyNkJdYbhpQMQYPx3LAcy_SLePJ1K3Wjm0IGHT1PKGTMpFRvRYQy2h4bw2v7RIumSdxrzLBJh7gr4YqPMWKprjPTA_jcoBuehtzcTOBY1NPjQmKbzFReh8WRsNNAMXJO4ItIJWyPEZnXhjORGboSnwWMOEI4DTbxvUZYIbN9WSvHW1HwOSUJisxV44-u6Q7Xtw9ecV1HZz2oOk_YolY7PUDX8vUnGLTSeRJOGKfbU1whAoSR7lDQxur4bmxvnquxficbgoOyJTOl2p0XFbKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454a762bef.mp4?token=PXsiddO_V7yHA9rd-t9RLObPTHg0gAEDceBKX4mNpyNhZhdIXwWr8RH4P8NduKEI6yLyNkJdYbhpQMQYPx3LAcy_SLePJ1K3Wjm0IGHT1PKGTMpFRvRYQy2h4bw2v7RIumSdxrzLBJh7gr4YqPMWKprjPTA_jcoBuehtzcTOBY1NPjQmKbzFReh8WRsNNAMXJO4ItIJWyPEZnXhjORGboSnwWMOEI4DTbxvUZYIbN9WSvHW1HwOSUJisxV44-u6Q7Xtw9ecV1HZz2oOk_YolY7PUDX8vUnGLTSeRJOGKfbU1whAoSR7lDQxur4bmxvnquxficbgoOyJTOl2p0XFbKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27453" target="_blank">📅 14:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27451">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5vtiDp41kQVgFa16kmRvTZchb0tqJPo1LCTCzxukppcwcNJcjhXQw8j-LROCS0isTsyeB8yIOhQ13MR6iAeDaYHUn9B0bR3T58y0fQCZbKiBOc4-0TijR9I-0ha8B14zh-yaVpAi7JLMFrOQpmfigWyQqriuTIoPcR2sUj-iPHqpNWwsdH4ROI6cOVtpxexhfZHoysDq9LOZOgChbNAOIqy8Jv9rrHWclIeadfpr_UNFSsAJZJ1Fe7X-zE-sM2TplmdoPfZ5r1rkiHgPf3kKz4aRb7m2j1H7jbSXOS-PVgRkqX9vV54fXEf7s8IfWp340O1JnFJV1VgWwbC-lJ-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ تنهامانع بازگشت مونیر الحدادی به تیم استقلال مخالفت همسرش‌بابت‌جنگ اخیر هست. منیر الحدادی تا حالا سه پیشنهاد رو بدلیل پایین بودن رقم قرارداد رد کرده. در حال حاضر دو پیشنهاد داره یکی از تیم‌های ترکیه‌ای یکی هم بازگشت به استقلال.
🔵
طبق‌صحبتی‌که باایجنت…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27451" target="_blank">📅 13:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27450">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQLT7lq_zvTa8MMTPspwOz-9RRUN3FsbT9SLNI4E6-PXwy_cMmKeNpxGNZsL3Zx0kswjeW4X6-gA8mIT6772jlk7yjeFHNXyEMf-nfa6XAJWxm5cOgtcp11W2LwEKhqhlbDaKRDUJ5N2RqrL0J_3MTTKdfgSh20F5OepITlp14jbI09zZ5MKAtmidXBUYyhMNUMic7S5bmRF8Pv-8MwWhvRDU3daFblVoDa1-ecKHXwuawlLh_CrZCeDxqhi-pXjCH8kOqCkq-QeCa1zVfgVuuivwulXVFxr_iqYBINcOTG8rVfAt0mSEj1WkW4l-9UgmLfi274sga9Cxs2XPvluyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
تنها دو روز تا فینال سوپرجام اروپا بین دو تیم پاری سن ژرمن قهرمان لیگ‌قهرمانان‌اروپا
🆚
آستون ویلا قهرمان لیگ اروپا؛ چهارشنبه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27450" target="_blank">📅 13:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27449">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-CUlKYLEo-XCwkdljWL-tonI_FLD4O9crqNm-zeIh42Qt-V0ml_UP1b4_TNZxuD5W1WGDNQ9isA2pPKJ4nUO1Dp876qtxHpc-9P4puk2vKIXHFIncrJMA5rxlFhdIh71PUwZOecouh4kZ_jBE30oUL45sc-mkQe173Q1UBBQANX322j9VyYPzgtlyi3VYeU9U5oWq-MsXxNh9PVzrJHsWaP4_2yY_Y8DKGgHGy3PnY1PAwmMk42nCUwdoBs6RqcKr-_FXHqnCP8DwrV1AgHQjcqQIrZDU4hG8KAyESkvMvc7OrTpvuFjngzzhDp6vgGIRSLYdrKGdmIdUGwFyZnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
عکس های جدید از مراسم ازدواج مرتضی پورعلی‌گنجی؛ مدافع باتجربه سابق پرسپولیس وارد فصل جدیدی از زندگی‌ اش شد و با برگزاری مراسم ازدواج، «بله» را به‌عشق گفت. همسر پورعلی گنجی اصالتا کرمانشاهی است و گویا پزشک هم هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27449" target="_blank">📅 12:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27447">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EpQcXCsNd4ZuzngXdTOleudTvCETmu8IPBX87edNMG9MMJd-FSaTnjcN_tEbFMWLWE851cpnDrGnLCmL5GORyBnxiarIqRefC1GcW8PzkU-Xfj8UMFAr-fBTbm_y5pfrcNFkHysCV43WltZb-rXAECuP9a2aq1kg8ihnaPvZ9Ns7GzmgkCHnPRhFfH7sQ--ZpohMB8H-fBvI-vUAS4J7jBPZPi1VTF1XN-o-AMwDpV_D_7-CGZMeyJKkJoT3AAYCERFobISa0FobHeDVbgde2ePdI8YHQ0ppu2p6JL8VB1hbVyQa-H70ASmOK4_hOiIVW6jl8tLthZnT83IWmSWAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oy3JHasqulW_kbhCCVslvMwTNtS0gBjwy0mtsOHcZVlVYPVuuA0CLG4gLdLZ9xxHlWBgAqhPoMceG7oHfqHU0LKKhAMv2zCPVhWh77fYWQQ1A4kjfgwl9043QaLqOP5jRNwKexk8zQIR1_9qRxKDRj8kXj0oOisN5wWudcaW7VkgGwEIt4fQOrO0dMMCNFowuaJp4LNIyEHSOO7yANFzEhN93oDnIvTE1hKEtje8Bs9VUuksuEi6UzUaiXvIdzQZHcZrQ7WULJ3r49GNBaqiIrNmM8LgPdYEEsP9d_pPXz8hYxOvCiCEBDLNH99LIS0_MRepM-yIDNogqMum9HwCSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لوئیس همیلتون در کنار دوس دخترش؛ حالا مشخص‌شدکه همیلتون چجوری به اوج برگشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27447" target="_blank">📅 11:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27446">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPM3wOG0S7e9EOpYKIYdD9CvtHJq-QWXzwb3iHSNRt4VbmrLjTxOzfF-oQkdfKfiia_2YAnUL5_QxbbE-QPK50PncRHu6tBdz8kzRXZa309b_jI4pSMCrIQ544rjfarBt_6P7uxp1ECh5QyhjeaVuiPN-PbtpbJhQxHLFZxCozPY0mha-TVQ0Ti0qtG_ieHze3-0aExGTTdGeG3PvyQroLQNCQJQZR7Z4Tast79HHofgghcFmhSaeJCjF_amItOHITCC1nrEggzDXdnYBfFl49AZ6x04WlmbPUV6Mli8iemvWo-sgZq3WKx0LKM6bFIU8Xog2D0yNYERm1QkJkLujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛جرارد رومرو خبرنگارنزدیک بارسا و از مامورهای FBI: الان ده‌ها دوربین در سطح شهر مادرید رو زیرنظرگرفتم تا بفهمم خولیان آلوارز دقیقا کجاست. یکی از اعضای تیمم هم با استفاده از هوش مصنوعی درحال‌بررسی پلاک‌خودرو جولیان آلوارزه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27446" target="_blank">📅 11:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27445">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2O_sDlL4-3eF55lJ3zIjhniMfIFJ2IZwD3CTvag1nvOIMwpPOWKx6PpiczKKZLoAdXI7dY7cLGhj-n6gfu2j9hiXpn-m1rPq8XWoGI9PjclFiHq9KVGMHEkFKVkHGwKho_WGUEF5G2ldpXjPsSC0B3ABNk6kcxwEFcF9oIz8yLA9gCAYEbQeZVa-Ziwy9KrxYVw0W72ajIcSiTVxWurAr7YSkBWOF3mWPXC6juaWLZMQWxeS1QSsyjFNEBk7zmT5aEnle5HfFmdK53AUDSltdQIGOeQOWJl4Nvvu0YaTtyYl8EgyeZ4tGcq-XAsooeOs7bvKexQGOd3eKjzK-s6yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
دوباشگاه‌پرسپولیس‌وتراکتور توافق کردند که محمدقربانی راهی تراکتور شود و محمد مهدی محبی نیزپرسپولیسی‌شود. حالا باشگاه تراکتور هم بزودی از محمد قربانی خرید جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27445" target="_blank">📅 11:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27444">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCI1N3g2N6QE1RCEzPB7dEq8hFnkLaruPyOvT937det__1gYRe8vEfKJYjz75lFTPvYAQ4Jda_VXb5B3csG3LlBzORmmZzwrHvzFVHzbeQ273gvW-nQiWkVUFNvpPoE48lKyYoJsBfS_rFPK2P3EZ-Ee5YR7e8XTb813qWp6efVpIllHKJjV9jmGHs4U6cRM7gvE7z9FX8gp0e7kRu1l03cN_HR8giVRgvnSNPuFVRkx8CFh7y_Yl-QA__xj83bUAvgrKum3BXs6rK3rYHegMB44V0sfsfQxNBuLR7LX90o4i7RAjkuRMEj7IYvI6CA8ffoy98E8CPIziyoriNvuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
🤩
#تکمیلی؛ خولیان آلوارز امروز بار دیگر به مدیریت اتلتیکو گفته هییچ علاقه ای به ماندن در این تیم نداره و از آن‌هاخواهش‌کرده تا با انتقالش به بارسلونا موافقت‌کنند‌. سران بارسا بعد از رونمایی از رودری سراغ نهایی کردن انتقال آلورز خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27444" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27443">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G355Z1ZqH9lgm3xY0ovDQh0TR0mXAf1I0EvAKH-243EzyZsjqBUW9qxWbYIhHd9W1nN3EmkUuvroY0mNu3G7m7-yTiCVLSWH1a6-kIcawHgOCXMX-Uan2y16Jnqb7a3XYKZMoSPEKV20WmaTJE5PcrdJLFzqiOjBQDasDn3-aNkUAY_SQZPZMRX3dvPkBH_uOqtmSHPM1Fw7BVTCxa447Wf6jTx0uOCu0DDeN_LyDcyJAybmlkCTSHJygwvMMT-5TBEPkLAdmTYA5oLSxW68lRoSrD5SUU38vMWlcn-j39bRM1YRkAK_4Kp1OdB4u9KPwZ28hpSpDJzi_yB0lzqTIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترابزون‌اسپورقراره‌دستمزد ۱۷ میلیون یورویی به محمد صلاح توی این‌سن و سال بده. صلاح این سالها پیشنهادهای زیادی از سعودی داشت. الاتحاد تابستون ۲۰۲۳ بهش حقوق‌هفتگی عجیب و غریب ۲.۴۵ میلیون پوند پیشنهاد داده بود. سال‌گذشته هم یکی دو تا تیم عربستانی دیگه بهش مبالغ…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27443" target="_blank">📅 10:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27442">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPajVAJqA5GnXpR6VK1Um7oTHGafEF1wkcR8PoBGgnB2vIL-L9X55m8k5sYlHiPUhqiNniCxp63oyUht9Wmym8FX8DX-JJpcMpylE0KLMTGoRepH7As-BTwc1YkXJPo_h9lhzXUUhHjMvP6bXxPBtoPDaJzaDauBit5PWjO8zNDYKo8r__LANt2r1v8GL6pt3bYw_EKmaOrkOiLn-5pQH3e-EnQlomiHq30iNV_rm02V5BevnGqOQIjisBzcazXLcgd-esgEzQ-ida5kFY0wrNWJVkeVq8WThToUehdUJuP8eG3QB4T9KfUiAGGak6ino8Uz0qOASD6ej_WF70hAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست بازیکنان المپیاکوس برای دیدار با نایمخن هلند درپلی‌آف UCL؛ مهدی طارمی بازم خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27442" target="_blank">📅 10:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27441">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e83727b1e8.mp4?token=ULrlPOvgN2kjT3HsK-xMdED9U18yyMTaPRcgJn-xBTrBGtYYVbAhWSHFAz6G9M-rVuXX3T3qYH7k0O45FVkYnkqsrtjuZnd9tPluG8w7KIb8JWn8F4KGKttui64lVugULT9o8xTgsm_SmTC1cDRKaZX8KZa_4jncs5rQw3kcNG8zJZDAMUucAM8GzjRghwLjRkCiY5kOLbhZAq0Ak_HiPTrc6xn16DlN2N0zZvtZ8gyBFDov9BwhRrAEfU63qs8cqxFNpFLUI8O6QzAlJH1pdtXn5QkY7Bd6QJwaqSm0G_3GqIh2_eHVetb8FY3i5uWSfSJJeR7712d4JW0p6kAk6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e83727b1e8.mp4?token=ULrlPOvgN2kjT3HsK-xMdED9U18yyMTaPRcgJn-xBTrBGtYYVbAhWSHFAz6G9M-rVuXX3T3qYH7k0O45FVkYnkqsrtjuZnd9tPluG8w7KIb8JWn8F4KGKttui64lVugULT9o8xTgsm_SmTC1cDRKaZX8KZa_4jncs5rQw3kcNG8zJZDAMUucAM8GzjRghwLjRkCiY5kOLbhZAq0Ak_HiPTrc6xn16DlN2N0zZvtZ8gyBFDov9BwhRrAEfU63qs8cqxFNpFLUI8O6QzAlJH1pdtXn5QkY7Bd6QJwaqSm0G_3GqIh2_eHVetb8FY3i5uWSfSJJeR7712d4JW0p6kAk6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ علت اینکه یه عده میان فحش میدن و گارد میگیرن نمیدونم‌واقعا. تو خبر گفتیم بانک شهر و باشگاه‌پرسپولیس گفته ماحاضریم این دومیلیون دلار رو بدیم. همین. هرباشگاهی‌حق داره به هربازیکنی که دوست داره آفربده. دیگه‌بایدمنتظر پاسخ حسین نژاد باشیم ولی میدونیم…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27441" target="_blank">📅 10:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27440">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65599dd5ce.mp4?token=RMB9aJX27P6LMKFHA3tZteADgPdWbIOcjVsdZlfBEOe1GqN93WV5I7PtmYlQnGtYp55vyplD2cZBCSIPwpc5FVmbrD38oUNASnRCnvMFAIWRttVYlQbn_uKS3xfJ9jN8KR18If406M_o8nZpY04YfwgJz7L2JAyRGOaOPGv2G7Eidrd1nOqLbXL3JicTrslCwrfMwArTkw1_fLGCSx1Ui288x0yvI0CnNWoH3ZpVPYmgwt8uGuSAy-ookxjUJcTU4I0sfmVOs34_6jVNWpUdMScr8B5SRuDKhxT4Zgs7jQs_avl3zlFH1V5UnaCSyhPPCrXGbHo8d9FPAq1gCSDEjEd1pVX3Q9-us61vSUAigFaDGmgSKxcWtOoSY_c7USpy9u1DqKgGfqIzOmrUg5VWOeEO33LEbNq701gZ9hZhzZIGIdWfv3kszn85V1v2y8PU5qtD7_LXBESTx5wiq6YaUsAWwzpD_y_ZccDq5JihGquWvSw-DOqdU3_P90oaDZYTpEJZ4P5tt_aAV-8fXfouaPueCG867hDc6og1SKby48TUcK028hoq7amJh97ZecE_ACIjVvw9MLQiT4c82r6iZjd7TiXAWhMD_l1QWprXL29NHrES0pviLw8Bkq5UoLWoJhI9Ix78Wgu6o1YLSAbqeKO3wO9y2NP-TF-3fu1zBJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65599dd5ce.mp4?token=RMB9aJX27P6LMKFHA3tZteADgPdWbIOcjVsdZlfBEOe1GqN93WV5I7PtmYlQnGtYp55vyplD2cZBCSIPwpc5FVmbrD38oUNASnRCnvMFAIWRttVYlQbn_uKS3xfJ9jN8KR18If406M_o8nZpY04YfwgJz7L2JAyRGOaOPGv2G7Eidrd1nOqLbXL3JicTrslCwrfMwArTkw1_fLGCSx1Ui288x0yvI0CnNWoH3ZpVPYmgwt8uGuSAy-ookxjUJcTU4I0sfmVOs34_6jVNWpUdMScr8B5SRuDKhxT4Zgs7jQs_avl3zlFH1V5UnaCSyhPPCrXGbHo8d9FPAq1gCSDEjEd1pVX3Q9-us61vSUAigFaDGmgSKxcWtOoSY_c7USpy9u1DqKgGfqIzOmrUg5VWOeEO33LEbNq701gZ9hZhzZIGIdWfv3kszn85V1v2y8PU5qtD7_LXBESTx5wiq6YaUsAWwzpD_y_ZccDq5JihGquWvSw-DOqdU3_P90oaDZYTpEJZ4P5tt_aAV-8fXfouaPueCG867hDc6og1SKby48TUcK028hoq7amJh97ZecE_ACIjVvw9MLQiT4c82r6iZjd7TiXAWhMD_l1QWprXL29NHrES0pviLw8Bkq5UoLWoJhI9Ix78Wgu6o1YLSAbqeKO3wO9y2NP-TF-3fu1zBJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
تموم رسانه ها؛ خبر از رونمایی باشگاه بارسلونا از رودری ظرف 72 ساعت آینده میدهند.
‼️
تموم توافقات بین سه‌طرف انجام شده و انتشار خبر پیوستن رودری به بارسلونا باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27440" target="_blank">📅 09:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27439">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU87oTqGYaeAlDBT5nKqKWYZjEHPnxwNWxTaE9eRq4WRbtf7fTtwzTgtfHdVovBxsBmO7yQHznalGkg6RZTnUIeb0jwdQNi0MsARY6aGNXXTNdjTLsNUGxMHp5NZ5Lv_Ewqp105OzV_RRhbRTzeKoOvdtVE6RyfsrgwVrR2BVpeaTXCuWJz3nsm3VOj6fQALZLQSwsrT4Hb0KsKPNVYfV5NEqaGGntxLCzuiHQpsO2BnpaQA7XHWkckaWc8r_aIRe4DsbldmFTEhegfyUVjAzLg7Shx-CJ4melLTl2a42FmRgYlwH0QFTGsr-EyCT9BYnzxcFCWWLHqgdt5Kmk3fJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شنیده‌ میشه باشگاه سپاهان در روزهای اخیر مذاکراتی‌ باخوزه‌مورایس‌ سرمربی‌پرتغالی سابق خود داشته که بامخالفت‌همسر ایرانی‌‌اش برای بازگشت به اصفهان این مذاکرات بی نتیجه ماند. مورایس بعد از جدایی‌سپاهان نتایج‌خیره‌کننده‌ای با الوحده درلیگ و آسیا داشت که با…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27439" target="_blank">📅 09:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27438">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxyyX2hWQvuhw5GX0KSz_CweQpSRuOlrlujHEiYnNVme8WA0xWaDR5qIJRKBokpfXZ2I36Pw40Cy08ch807kHOiHvEev53c-r5XWciR8oJLizK8Z56UPLVU-LiHHjf7iwv8QJZ8kYDH4Gh1jTs4VNCHDUFsMUmDnVfWaQDh_kMRQNz9V5gyIkK35T-4tmLOhJZY_0zgTjoTSnuNaFe6nUmjiiov4gcMFyIkLlJOAQU4LHbsfaTKlSFr-FjlV9rjp5WXHmM4LQK2o_z7ceZj92IxPxcbxuOF5N2DvZI9tGWjsQp-I_Jl-SscEbCR-7prBzSYpmEcxrUGxxs07zI3UrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنخل
دی‌ماریا:
اولین چیزی که من با حقوقم خریدم 206 بود، اون‌آرزوی اونموقع من بود و بخاطر همین باتلاشی که کردم بهش رسیدم، شاید میتونستم ماشین بهتر هم بخرم ولی قبلش میخواستم اون رو تجربه کنم و بعدش برم سراغ ماشین‌های بهتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27438" target="_blank">📅 09:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27437">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epAADaaR5rZ4aG58hYrSKCGV7BqKi0q_7ISljHdOWhNXKJjGV6Rt59vQPbVl-4SRhcD5QCajwsZI0wKFh-XPUzB1AX1b5Nefz6K3iUE9TjKaleUm-xT_h2841gG1Vy7QSVXdygLvgw4DcHneL2oInihx9OKfmepfWdEDXO7eF33pJMW3wsGUJksitS5IL-zMttK_LgciTfwVy4Ma28TopY-b72ffkfhOLLvI32c4K0lr92vnSZWUKTkGAUo13PH70yQwdr_mfBPAcEuqE-HCpoW-_M8-zmE6s9jW3HYtJrrJeIMBNkd1dJdozkRP_qxTxEYpOy4rI_824X_ziYbtOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فنرباغچه به درخواست اسماعیل کارتال سریعا میسون گرینوود وینگر سابق‌ باشگاه منچستریونایتد رو به خدمت گرفت. از فرشاد احمد زاده به میسون گرینوود رسیدن اگه پیشرفت نیست پس چیه؟!:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27437" target="_blank">📅 01:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27436">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCerAkAdSLQ-_M9N1H5ws8zEGHs_XjJL_5bk-Qi907Nj5LqB1PO_koYntb6d29wJ219xt438-3bmUF9mzMQaf7LK-d5vYv-Ed8XkR-xkqUs5yegkhnXJ27xmc72ap88MkkhgWaZRvEVKSMyI_yi-TnMo5bbEJUuDTKGqKKk8K4mX3Q5AwQJ3UP-pHi0JB75RU1MwXt4wf3a1s65C18217sToYNha8LArX-YAdtqVGVLfeGDb8J7J8-5xZQMDgLlwGDN7L6YZe7f3d24hCgIRCKvyNIEZQi9blOkveB1KWbbTg3l9lXL1yjqpR-UkmP5YcLuF7A-f03JcotyqwAhTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر ایرانی خوزه‌مورایس‌پرتغالی اعلام کرد که بزودی‌ موزیک‌ جدید او منتشر خواهد شد. یه‌ بخشی ازویدیوش رو درکانال دوم گذاشتیم! دوست داشتین اونجا هم‌داشته‌باشید محتوای جذابی توش میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27436" target="_blank">📅 00:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27435">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da4d4aa52.mp4?token=E4lNEbA4zgIaf516RErtRVQwbMxdq7lKqJ9ukgTzodYINmp-j70mtpNFtu9_UyYBc3cN3eGnfk6ZGVljbaBLMdZMQ4TrJe2PtZBgt30cgnQE3M3vzIqko8L_V1uVs8TGh7fpsFwwYapJikYqwY4uh6ALVBHMGR2x3Zi47rSzvbcqKxZb7BzTSghDV_nxriCxqIUgxlYEipVXz_uNs5WYLB5XhZlIt73vC6ukT8PzjTlF_8uCbLX2BvXjBf3bSn78lKH-L1FuA7nwnfyW-JkPAnKhPldmovQF5gU98iAjHnCHNnpryXT5WRLGyyf341h0oEcwycP7kDgQDVJckXa3WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da4d4aa52.mp4?token=E4lNEbA4zgIaf516RErtRVQwbMxdq7lKqJ9ukgTzodYINmp-j70mtpNFtu9_UyYBc3cN3eGnfk6ZGVljbaBLMdZMQ4TrJe2PtZBgt30cgnQE3M3vzIqko8L_V1uVs8TGh7fpsFwwYapJikYqwY4uh6ALVBHMGR2x3Zi47rSzvbcqKxZb7BzTSghDV_nxriCxqIUgxlYEipVXz_uNs5WYLB5XhZlIt73vC6ukT8PzjTlF_8uCbLX2BvXjBf3bSn78lKH-L1FuA7nwnfyW-JkPAnKhPldmovQF5gU98iAjHnCHNnpryXT5WRLGyyf341h0oEcwycP7kDgQDVJckXa3WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی که اخیرا به لیگ دو روسیه رفت تو بازی این هفته‌تیمش به این شکل با پرتاب دست توپ رو گذاشت رو سر هم‌تیمی‌اش تا دروازه رو باز کنه‌. خنده های گزارشگر رو ببینید که برگاش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27435" target="_blank">📅 00:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27434">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgOkdRriBQmlWgmksy8eTbUZ3sNUEbBWaDEVGUHhvGTcVr-z1vxn0Mtq_eD15IgTYfqI4fnHaNlj5-ZADRU4r_Zclp_Le6lRF4XOot-FKKN82IpsRYvZMFW55oOuGyKDHFY30NEDz01c8pzONLjRZJ2ouZ_B1L0Jt8lD8fcOX-lU-BLryaa9jKEjSwTWZ_i3arJ8AyBGvW3IKpHnjdbhlzMepRG7vtjWjTtDDADSQFSaqD9-oux88few6vI3-Xj4Om3HuF3YmqbpsY4uxpVzg0MmfnQfQlja-bfbxpYm3TBuE_MaMvi91zhSPQ6RrAgEdNa-crcm-cQLuxaj54rIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
‌از باخت عجیب آرسنالی‌ها در امارات‌ کاپ تا گلزنی اللهیار بعنوان یار تعویضی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27434" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27433">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKK6OgRf69_jSbkS8_qjGzlN45Me8fezDBdQBEPBb_Yza5RXhsc-EVdPMWFxfMMF4U_OqNH0qq3ScJlbjgJbuvGZY5Be0CJZAgj7ikgPUWRx7sDHNVRV0N2Nm5bLwA6j_REX-I3ODDMWSB5Qlrtg5r6z8nh_wWAV4t5kVPkzh2jY598Mdc-q_i1O_MeJsg_wcAfZgs_UXZBCwKSmjhq89Jros6VaMXmb5_khLwP9V9-nGZK9Lv1WoUqCbguBx1F9II0d6YTTXP-yX_wxoNtBZYZIJdAvgWhlZNUU7nq-z1MCfVdcNz-TYBQLTxmROs4uiW7mWWVN7NLug8VAQ9PRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وینی‌به‌رکوردرونالدو رسید؛وینیسیوس جونیور درفصل‌جدید نهمین سال‌حضورش در رئال مادرید را آغاز خواهدکرد و از این نظر با رونالدو برابری میکند. رونالدو ازسال ۲۰۰۹ تا ۲۰۱۸، ۹ فصل برای رئال مادرید بازی کرد. وینیسیوس که‌ازسال ۲۰۱۸ به رئال پیوست، حالا وارد نهمین‌فصل‌حضورش‌دراین…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27433" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
