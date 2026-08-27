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
<img src="https://cdn4.telesco.pe/file/IrqY-hBrIozaRRJ_awMicG7B3J-DiSl20Kq-jgaV_nQGen9fYzsdQsiLiA3uMF2cruf_RjZWeY82fgpYbSfmc5_oNiVWmlPLXjc3dLU35ZTPy1MD78LygHDPf-eMcPK17Ap8ZYq3xyJ414dkTE16DQd-S7oQofuh9idjssbdCwkFLGcsQu1JF0eD9EyVinwW6urUcckXnZnIYqsxnlM82UmaIrFnV0pX-0N67zBw6D5DXFGGP8NVfBVTBJ0n4UZhf6dfOGO7uSgH9Drrj3k5Mqi4ZnKsb1TCl4gjsfYgzEckYS9CJgVoQunBCKjAwreFOJoCzeAgIgrRWIuE0zxG1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 117K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 09:25:37</div>
<hr>

<div class="tg-post" id="msg-70650">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=cX9kNmPVYGBdCkqFzT6A4k3kPsftIj9J-P2QoqOPWkqueEk6quc3D7pHASngP0fYCSPsEGw7my2z1AJkntTVRaVT4A-q-k5_eyIny2bxkcusfIq5zdcQ1WmhQf2U7_3ggXZtpp2ZiVzaRjKB9aZLkv7Oc01VMZIGIpsa_9iWFaxHc6Wlge19FZ_hIBvQfU6KrTvRx0oiRGHxb1ZZiUPZJGiwvv0RxPhaL68eAJkNVDytLbf_8gMyn4zLhRZJknwVZg3XXTIQ7enHxwu2JZyWl6uPIKaMUz35t4SVFlV72u8Uk9XB8TdSj8ulUmSyc4YlQorlZWjFtY-cEEB-AGEqgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=cX9kNmPVYGBdCkqFzT6A4k3kPsftIj9J-P2QoqOPWkqueEk6quc3D7pHASngP0fYCSPsEGw7my2z1AJkntTVRaVT4A-q-k5_eyIny2bxkcusfIq5zdcQ1WmhQf2U7_3ggXZtpp2ZiVzaRjKB9aZLkv7Oc01VMZIGIpsa_9iWFaxHc6Wlge19FZ_hIBvQfU6KrTvRx0oiRGHxb1ZZiUPZJGiwvv0RxPhaL68eAJkNVDytLbf_8gMyn4zLhRZJknwVZg3XXTIQ7enHxwu2JZyWl6uPIKaMUz35t4SVFlV72u8Uk9XB8TdSj8ulUmSyc4YlQorlZWjFtY-cEEB-AGEqgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
یکی از زیباترین سخنرانی‌های محمدرضا شاه:
هیچوقت به زندگی فعلی خود قانع نباشیم و دنبال بهتر کردنش باشیم.
برای بهتر کردن شرایط زندگی، اولین شرط خونه و سقف بالاسر هست و بعدش قدرت خرید مردم.
محیطی که در آن زندگی میکنید باید شاد باشه، غذایی که میخورید لذیذ باشه و لباسی که می‌پوشید تمیز و لطیف باشه‌.
@News_Hut</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/news_hut/70650" target="_blank">📅 09:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70649">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/news_hut/70649" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70648">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=PJxtQwm_wlpd91ln3soqX93z8J-YhNzzAuEObg_KB_GGskvv69s7FEFY4ICdguaS1RZ-BEjzqjb5A18yOF0fErJ8mVbJWnwXsc9w383ctALnv0sHFddA6lIV3T7tPfn_JLi6Tk6Vnt2vhpa1mI73U5KNEdjtYK7weUZBoyA94eYm2oZUm74V_HIjP5tGAp4KH_hXNqx8eXBfsSfBdZKve8lHPhgmrMKsGwY8ajTMnrlCKXldIO1SrqewRIl8wP4EoIBxC8CQ70rWk9-CpJeQjjBkgKaI5Q8WIMlRSu-Izsa9tMZu7Xzh_q4rW3iCsTOf1uAEmMZcLvaSKLkAgAJFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=PJxtQwm_wlpd91ln3soqX93z8J-YhNzzAuEObg_KB_GGskvv69s7FEFY4ICdguaS1RZ-BEjzqjb5A18yOF0fErJ8mVbJWnwXsc9w383ctALnv0sHFddA6lIV3T7tPfn_JLi6Tk6Vnt2vhpa1mI73U5KNEdjtYK7weUZBoyA94eYm2oZUm74V_HIjP5tGAp4KH_hXNqx8eXBfsSfBdZKve8lHPhgmrMKsGwY8ajTMnrlCKXldIO1SrqewRIl8wP4EoIBxC8CQ70rWk9-CpJeQjjBkgKaI5Q8WIMlRSu-Izsa9tMZu7Xzh_q4rW3iCsTOf1uAEmMZcLvaSKLkAgAJFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a4
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/news_hut/70648" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70645">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff574e553.mp4?token=DqUtLoOTdAJMPqGFYOlqDCogYmAMAxMHPMlwlg-FNfEHQ5q4DPR4xsHTc3kZAVMMXhKZWDIRB_49pPAg0IMtdEZUYrexjNhiphcV5BK7UGMVPkdln2tF3PQpiVj60OoZXn4nkV3bgYPisRpLjQ6kxb3RkmF6EvDx0cKAFw82Fw18ai1NxKlP3Lxgxpg-8OdT57ikclKfEyNx2PKHGW_zBQqvm9nQJblnXytO75jNCBL-BcnRjoXHbxW5Ns98KnY0qLtZU4s1_8oRCCtFQqcKKm0bKuZTgIW0wDBvPk6b3UdHVoKLc6m0zVuBegEUbP_TjzzxtdfZLONsXVz4MliAjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff574e553.mp4?token=DqUtLoOTdAJMPqGFYOlqDCogYmAMAxMHPMlwlg-FNfEHQ5q4DPR4xsHTc3kZAVMMXhKZWDIRB_49pPAg0IMtdEZUYrexjNhiphcV5BK7UGMVPkdln2tF3PQpiVj60OoZXn4nkV3bgYPisRpLjQ6kxb3RkmF6EvDx0cKAFw82Fw18ai1NxKlP3Lxgxpg-8OdT57ikclKfEyNx2PKHGW_zBQqvm9nQJblnXytO75jNCBL-BcnRjoXHbxW5Ns98KnY0qLtZU4s1_8oRCCtFQqcKKm0bKuZTgIW0wDBvPk6b3UdHVoKLc6m0zVuBegEUbP_TjzzxtdfZLONsXVz4MliAjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهروندان اسپانیایی ساکن منطقه "سئوتا" به ساحل "ترامپولین" حمله کردند تا مهاجران را بیرون کنند و اقامتگاه‌های موقت آن‌ها را تخریب کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/news_hut/70645" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70644">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr1uNfFrjx7PXK2ssdlDsVPh5O20TaYIeXR_q2D4jE8ljXZVjP8-kue3nmrutTn32fZ9-f1I8iTVEaZ7nQrL51cPaf0zuPBquvz55m6Lw-qct89aVI5GxBL8eOvhZTlMhVJeHn1kRLycUkqxGq8N9cInR4c6UUPxgv8Oc_lyxE9DaQZty9rzEDzyUY6iVk23_PEocHfn0cuT9tGHQUb37ISqo-KotDqkjvODzrseur0AyMxd6welZOgt5apc1Fq-gsRTx8cTXZ6ZKtppBpGQm09OZ9j_bZitn-5y9Ip0QauHtTH6hiw2iHP1DUzBTujAYfe5FAhZ2IKss6tzvjMVDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا ناو «یو‌اس‌اس آبراهام لینکلن» را برای نمایش قدرت به منطقه اعزام کرد.
پس از ماه‌ها جنگ — و بیش از ۲۰۰ روز بدون حتی یک بار پهلو گرفتن در بندر — این ناو اکنون برای استراحت و تجدید قوای خدمه، راهی تایلند است.
مأموریت: نمایش قدرت.
مأموریت فعلی: نمایش تعطیلات.
«خسته‌ام، رئیس.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/70644" target="_blank">📅 01:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70643">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3143921715.mp4?token=ZrnE0kxRC_F_CJvVmo7kmaOaK5HROUhRLD1f50pzrH-blYdGMUOu837Jz44UYBeqhwcVKeYWA_OTq8ZmhRqPTDOSHjdYv75SYJ4ogJ87zY1qLz8zf4k_Ua6QqJTZjlMNWwxpRHLC2vYxnmv_ljsMyz45pwsdtm4iP5bxWKcIZ7udHY6MDNyetGMEj0MeiJWGa7nJgz0b9t-9o92NuqoMtUXeHi6YV2bsHvJLpvoUDer9DkTv1TAaQEWlHsuUqkLd68Xdy8qPGkhABgXl4zCgsG2Vqr9i74BADJTpClFBRul-CGzxmt4GO2Lcuj_vrXllJ-y46ipVEiUdCE8ciaT1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3143921715.mp4?token=ZrnE0kxRC_F_CJvVmo7kmaOaK5HROUhRLD1f50pzrH-blYdGMUOu837Jz44UYBeqhwcVKeYWA_OTq8ZmhRqPTDOSHjdYv75SYJ4ogJ87zY1qLz8zf4k_Ua6QqJTZjlMNWwxpRHLC2vYxnmv_ljsMyz45pwsdtm4iP5bxWKcIZ7udHY6MDNyetGMEj0MeiJWGa7nJgz0b9t-9o92NuqoMtUXeHi6YV2bsHvJLpvoUDer9DkTv1TAaQEWlHsuUqkLd68Xdy8qPGkhABgXl4zCgsG2Vqr9i74BADJTpClFBRul-CGzxmt4GO2Lcuj_vrXllJ-y46ipVEiUdCE8ciaT1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شکار شکارچی
اپراتور پهپادی روسیه توسط یک پهپاد FPV اوکراینی کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/70643" target="_blank">📅 00:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70640">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiEGxgRBV1-mMC9FeeK8t88QQbHUT8SB9DcWKol1Ne_omZZNTXxJlPIFXkIfF2-V1zLNGaGasos3sQn8tuOGWf5wzlxwu7xpSWclFT3SiAeVoaUi6gyvPbHpdkIb-yyHejtUTkEWfhQXZ9D3Jyu2REQa69B-6V9CSZe9fGD_VugI076YpCwb1kfaw_qC6Rg6kNrjD8IHe_Dr2cyz5e8ZiwNm-j1D0ZbWYY3PlpUAbd6Nr93EHpaLwL2uXW9TJ3dmVXNerT1L7ux_89ej0f_qpgD1SlvL1UbjWmkKMT0el70rUQDAZ323YHysDs6l8maqq4m3F04N1Xu_HDeW8hWsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=sBQARAegDceZMrKEPwr7IOON972ojT2xTSYgN6TZ413JnEyQXJItFWYxcg1xnzWP5PHxZDFY-e3ZYc4LtKqTjWFXIQeYNTFJPiXd_4Xn_21TESwq6Pq_tBr0e38lknfAk96AzsItKHlwZX5NQD-uGPriuRZjyABfpox4JFCuxuYUMB8ZYDYo5osDFGuMG5BLBpdE1Mp65gGD1OkAaupHc0_GTzh25WIXduNU0tscOZYyIIAhnU4ubmW-xIqELjy7bAG8Yl93qUk_ZYB0Eo3jcK-PxOrHhuFJC8ljATgl6nBDcWYMLzJO9tUs5IcPowbijljq1MCY0avKSmRUSwV6AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=sBQARAegDceZMrKEPwr7IOON972ojT2xTSYgN6TZ413JnEyQXJItFWYxcg1xnzWP5PHxZDFY-e3ZYc4LtKqTjWFXIQeYNTFJPiXd_4Xn_21TESwq6Pq_tBr0e38lknfAk96AzsItKHlwZX5NQD-uGPriuRZjyABfpox4JFCuxuYUMB8ZYDYo5osDFGuMG5BLBpdE1Mp65gGD1OkAaupHc0_GTzh25WIXduNU0tscOZYyIIAhnU4ubmW-xIqELjy7bAG8Yl93qUk_ZYB0Eo3jcK-PxOrHhuFJC8ljATgl6nBDcWYMLzJO9tUs5IcPowbijljq1MCY0avKSmRUSwV6AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇳🇵
ویدیو هایی از سیل آخرالزمانی و وحشتناک امروز نپال که باعث شد صدها نفر کشته و ناپدید بشن!
ویدیوها عمق فاجعه رو به خوبی نشون میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/70640" target="_blank">📅 23:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70639">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=pzHC8awCvuuNlAms9dIh5NW-GG3sfliSJ6l5bcAGd_0EyI7DQm0AOmP-MrXAKjPwqC4LYyi4Ie5W10wwM5IBHBJOmYxZYUxwK7K28_Kdnau8a7bE7M8u1PIW7W3kRmneskHDbctKP7srCadpXIbxNxvf2bzAn9-J4Avfx3aXLPzNho4WhbOGYA8K4ypGK2KrE3OhRe1rFT1XxMtd9-jqrNOavvfLCpYTePCnMhTHLZ8E-WH_ADrSeR5zH7B0_xzB0TUYcJtXLIHEZIKIgS_RpmAJdD8eMurGcOQ2O_Bb8lfV7l808HANPGn1VPmhXdIUYGKTh6xQqfZ7sRIOxRTyPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=pzHC8awCvuuNlAms9dIh5NW-GG3sfliSJ6l5bcAGd_0EyI7DQm0AOmP-MrXAKjPwqC4LYyi4Ie5W10wwM5IBHBJOmYxZYUxwK7K28_Kdnau8a7bE7M8u1PIW7W3kRmneskHDbctKP7srCadpXIbxNxvf2bzAn9-J4Avfx3aXLPzNho4WhbOGYA8K4ypGK2KrE3OhRe1rFT1XxMtd9-jqrNOavvfLCpYTePCnMhTHLZ8E-WH_ADrSeR5zH7B0_xzB0TUYcJtXLIHEZIKIgS_RpmAJdD8eMurGcOQ2O_Bb8lfV7l808HANPGn1VPmhXdIUYGKTh6xQqfZ7sRIOxRTyPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالملکی، وزیر سابق کار:
دولت دروغ می‌گوید که پول ندارد و نتوانسته نفت بفروشد. در طول جنگ ۴۰روزه، فروش نفت ایران افزایش قابل‌توجهی داشت و درآمدهای نفتی کشور حدود سه برابر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/70639" target="_blank">📅 23:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07429c6dd.mp4?token=hDxaqN-h7sb0uHA5hFfRNKotEw0U4pVRmPkH-SUEA5btzKqk5Dbdt_zdpnd5MEyam4we2ly1QQgKzRSIaBapg-iHfl1OflCtvobb38rZVbOwOC-Njvj3LxG3dEqVceWndagnMOhV43U_aZ9Wiacl1OupusA52Z37YLsTTkV9vkFklC4Hg_SdH3Rs6cgJRYWvdD2j2S7B2L1ct4KjrAbo47-SZTYnmDedY6-KDU0kt9RYRUqpHXLqCobzNM0JxhpQE5IpFucwkPYw4cHuPMBP8MI7Mu_pcpeI2J0Th6Jan4SG42Aj9Kp5CZRY1TRQMNsUgDgHmRpbb9Czh7a7eAYRVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07429c6dd.mp4?token=hDxaqN-h7sb0uHA5hFfRNKotEw0U4pVRmPkH-SUEA5btzKqk5Dbdt_zdpnd5MEyam4we2ly1QQgKzRSIaBapg-iHfl1OflCtvobb38rZVbOwOC-Njvj3LxG3dEqVceWndagnMOhV43U_aZ9Wiacl1OupusA52Z37YLsTTkV9vkFklC4Hg_SdH3Rs6cgJRYWvdD2j2S7B2L1ct4KjrAbo47-SZTYnmDedY6-KDU0kt9RYRUqpHXLqCobzNM0JxhpQE5IpFucwkPYw4cHuPMBP8MI7Mu_pcpeI2J0Th6Jan4SG42Aj9Kp5CZRY1TRQMNsUgDgHmRpbb9Czh7a7eAYRVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دادگاه محاکمه اندروتیت اعلام کرد ماشین های بوگاتی و استون مارتین اندروتیت اجاره ای هستن(یعنی مال خودش نبودن)
اندروتیت یه مدت بخاطر ویدیوهای انگیزشی و سیگما طور که میداد بیرون؛ حسابی معروف شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70636" target="_blank">📅 22:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEktIVFFqmruNEpdmummdO0TT2C_6PdhDG4I6bUmF9ccJCEckWXavvwzitIkVvBbKwJqlanXodbCzUn5I2UrpRK-nVVhk0C4YFWLl9dMIeE7564bLoKCNmwFrFNTcUyjOgaEh-L3T5D15PoZ3bmu6SzWhVotdBLPkJ2Wdj39wLvd8X564MWwN6KzKvFWR9OrCQZ6pCZCmjUfmCGVL4XNycil86mYJ_JjZyZJUN0lz88EQCWv9AjuDzRLJ5OLZXJv8NsDyIl6QmRbMqwXOeOaqmo9W0391kmQUwT2w3oRkusAzyb-aFYiL8rQs4CxB_nNSu_1BFZtzskH-YVMmkDcaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
ما از بیانیه اولیه چین حمایت می‌کنیم که تحریم های غیرقانونی علیه ما رو رد کردن
مشارکت استراتژیک ایران و چین بر پایه احترامه و سازندگی و یک دیدگاه چند قطبی استوار وجود داره
این رابطه نیاز به تایید هیچکس نداره
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70635" target="_blank">📅 22:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70634">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66110614c2.mp4?token=Qawc9RlFNQuTj4QDuwzUNnWA5tx2B4k4y8gZK6Jjb_R3X3jHriVuiZD25oPTfuf4rr7FEX1pCqz3YABkWtDTOoEyOCoYrFYU7rPeHVyVC9aIZWAP_1PBLW5dHBLdWZ7GykVeNM7OIIT44jXUp9oOQUSVcBKbO_7iGia656lamzXS6RyD6MkGBnnD4oDhmvdcRBRs4OjP7jFGYZWjiS_eFQZnTqHpo3oQaRvYAJ9PbLcacEAXl8fkZAFMXNU6ETCDIgtHhumgvElkEeS7hUR6pQdBF2ggrQ-WTEMGf8T_dJb6sH--d46ML1XF0OiutAoory0nwLaluUuTbpkWBybs4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66110614c2.mp4?token=Qawc9RlFNQuTj4QDuwzUNnWA5tx2B4k4y8gZK6Jjb_R3X3jHriVuiZD25oPTfuf4rr7FEX1pCqz3YABkWtDTOoEyOCoYrFYU7rPeHVyVC9aIZWAP_1PBLW5dHBLdWZ7GykVeNM7OIIT44jXUp9oOQUSVcBKbO_7iGia656lamzXS6RyD6MkGBnnD4oDhmvdcRBRs4OjP7jFGYZWjiS_eFQZnTqHpo3oQaRvYAJ9PbLcacEAXl8fkZAFMXNU6ETCDIgtHhumgvElkEeS7hUR6pQdBF2ggrQ-WTEMGf8T_dJb6sH--d46ML1XF0OiutAoory0nwLaluUuTbpkWBybs4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو‌ ارومیه یه پسره واسه دوست دخترش یه لندکوروز سری 300 که قیمتش بیش از 70 میلیارد تومن هست رو خرید تا سوپرایزش کنه.
تازه، زیرش میدونین چی نوشت؟
ایشون نوشتن، تقدیم به زیباترین دختر ارومیه...
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70634" target="_blank">📅 21:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70633">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaNAZVM0hkpEEXaIkxwFRJrGVYfsX9SdF-xlHus9q0yTglIFy3B5NzeMS-WwIrPU6V-RDza-8YHpwqePZIVprSCu8A0C2XaQuvX-epkFvk5XXcm0HV8fMHhmu4LSRWucGy9RuqB_HDr1AzbvP6UyuHKCW5jmzO-97Gs9Om-EeChC64krenFeTSbIriFp7rbYopIzc0KmYgDz8H5CUy-i_bHRnUN1tgeAEGOERIJrc7g61w5DP_sE686O_KrI26W3l1m34p0-CrwBu_aT68EKTfrZFBYf8cVN2VSbCkWWK6dsdNO_wY-v7xAT3MnpKa60KyHfrNfJs_Xx91DfFzc70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فارس:ایست بزرگ مقابل کشتی هندی در تنگهٔ هرمز
یک نفتکش هندی به نام «HAANA» لحظاتی پیش قصد داشت تا از مسیر جنوبی تنگهٔ هرمز موسوم به کریدور عمان عبور کند اما با هشدار داده شده از این کار منصرف شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70633" target="_blank">📅 20:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZS1dL-fDiRTEI7_siyrKj_q8YmuSYmmwdehkfxf85pv-HY-z89a9tO08qZaBIlQ5m5DBF-El62WZxa3Nv4XrC7NW8CFUGRHN8CWihRjCKF8rOLH6vIfTr8e_uw6qKCHOp5fwR-u2F5IAtSvgUrYc0eDnYwc78ETYr0vFkjZ1rzDMBGokWxa8WO5yZ4YS74IscRnlT3m3pzom94VIxdWQo6Y2Grz1JnPFHI-ZARowi1R25bqmsermivAAtFh8RIqitBpGBaGpDQZoqAFX7lYkmj0MZ00sf2dO9m1GvtHGobPthPu5RFkgqXZEp5R224QxC5miX9--oAUNxppkfgvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70632" target="_blank">📅 20:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ℹ️
صحبتای امیرمحمدزند بازیگر صداوسیما:
حرفم با مسئولین اون وره چون این ور اگه حرف بزنیم احضار میکنن و تعهد میگیرن اخرشم‌ممنوع الکار میشی
قبلا حدقل زنگ میزدن میگفتن ممنوع الکار شدی ولی الان زنگ هم نمیزنن خودت باید بفهمی جلوی نون تورو گرفتن
ما ایرانیا با دلار ۲۰۰ تومنی و طلای بیست چند میلیونی و مرغ و گوشت و .... خیلی مردم شاکری بودیم
هرچقدر هم اقتصاد بد باشه گرونی باشه جنگ باشه میگن باز شکر کن سالمی حدقل
بعد که مریض میشی میری بیمارستان با هزینه هنگفت میگن شکر کن حداقل زنده ای
طرف میمیره بهش میگیم خدارو شکر بابا مرد و راحت شد
ما ملت ایران انقدر شاکریم خدایا یه امتیاز ویژه برامون قائل شو
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70631" target="_blank">📅 19:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
مهاجرانی سخنگوی دولت: در میدان ولی‌عصر یک خانمی به من گفت الهی بمیری!
رسایی سرباز نظام نیست؛ ظریف سرباز نظام است
رسایی منافع ملی کشور را نمی‌فهمد!
جریان پایداری خلاف منافع ملی حرکت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/70630" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70629">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=l7CSWDDg1rB3gQiT706Cvv1EQqr7NkTHVxg3PJ-faHzDo7-KntlhQDmFJsc5U5emLfTh83_VzeHPQA4pchc0FAJTAPThY8mVTSEQ_u_yTIwWVMMw71MEewTtaaSz19NmUNsdZRhLiZs1Uzo0o0eW6lkGiHwrbYSNttUoYSXID43llqB4UMX7TEcQwzu-wLDuyIujKF6OX9j3nWWBrBwOWvd4vLeIMdzZysLn7YPNrb310t20_Q8UeO5PKlUWYywveOWT9FzEosylzhXmGEsT6SKBRJrMbCLrlwueacMSij4onJ5uAdKeicHjf2TE-ORcMD2fSUwG_orf7Jw4DbzE8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=l7CSWDDg1rB3gQiT706Cvv1EQqr7NkTHVxg3PJ-faHzDo7-KntlhQDmFJsc5U5emLfTh83_VzeHPQA4pchc0FAJTAPThY8mVTSEQ_u_yTIwWVMMw71MEewTtaaSz19NmUNsdZRhLiZs1Uzo0o0eW6lkGiHwrbYSNttUoYSXID43llqB4UMX7TEcQwzu-wLDuyIujKF6OX9j3nWWBrBwOWvd4vLeIMdzZysLn7YPNrb310t20_Q8UeO5PKlUWYywveOWT9FzEosylzhXmGEsT6SKBRJrMbCLrlwueacMSij4onJ5uAdKeicHjf2TE-ORcMD2fSUwG_orf7Jw4DbzE8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای این دختر در مورد اینکه تو این جامعه، سخت‌ترین کار پسر بودنه، به سرعت در حال وایرال شدنه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/70629" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70628">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70628" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70627">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6kQjqoqkym4Pym46wq5zfKV9sJmEDhya-4nm9VWsj3aw7rXyBQGY-1SrOpnmFRfcSun9NA7q69l6SxlWhEyoWsni8pnyrKb3uGRzsmbmy7fYCcG91bWnJwG9x52Wze__wNNkPPHD-E22Whv9XqgMrC8mF7_pMmp79tEgsnHgePh5J5ZrKcZrh-eaqzn9XTCSIEooH47_ET1aRAaIkGBJ_OKJ3Dw_n8Ys2c5zSkUxGv8wcc6zag0ygxhpAEtKNrfZZCys-VBB611XU94QLr_QMm7S9Eznh2dFhCBdSWND_6TJRmTGJGQAEKCGOIIgWv6sBt2de5WdWkvvSdevk-hfsgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6kQjqoqkym4Pym46wq5zfKV9sJmEDhya-4nm9VWsj3aw7rXyBQGY-1SrOpnmFRfcSun9NA7q69l6SxlWhEyoWsni8pnyrKb3uGRzsmbmy7fYCcG91bWnJwG9x52Wze__wNNkPPHD-E22Whv9XqgMrC8mF7_pMmp79tEgsnHgePh5J5ZrKcZrh-eaqzn9XTCSIEooH47_ET1aRAaIkGBJ_OKJ3Dw_n8Ys2c5zSkUxGv8wcc6zag0ygxhpAEtKNrfZZCys-VBB611XU94QLr_QMm7S9Eznh2dFhCBdSWND_6TJRmTGJGQAEKCGOIIgWv6sBt2de5WdWkvvSdevk-hfsgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g4
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70627" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=GrSjJj0E1gDB9YDJKAD8Mo7xEQsOnQkbIrjKGe16E2BX1xSQzb69-31asohfg0jfpsb4h83ILbyWD4gnBy51TAjIggbYvBdgINyGAjYlyUIYY1hjrwYfJx6Jpu6b8rqdoopy3Xincm0jUoCeYAe4VElXBTjkHz6TVqefLKuOfQ10Aeki2-no4WfU3btMVwDn-YPqkL5UvFQ7tOgqzfXN-fSdxxKhuULfd3X8eylELdcc0hy0wNTEMvWC7F-d0Rhq6EdA4tHq_2QNkE8BwnYA6snRDJfwyvWjlT5lArVrEMvx2ykJFnBIF5dIsVi_ciVsY5n8WrQgpdF2ppQ-sAUIubK21h41b2v76wqcm6oeA6Y5KC4UQ94iaCfTsQAZ8MtpHS0LfmbNDRu7U0OS0-AX-vML4eEzujqWz2G5gPKccGCfnxJ4GhyOlSEU9XmzCfXpk441Hk-fLokIZVWm2C1YJRGnuzJlX5GSwtcJq7879EkLg4bUKeCLGy_vx1VeqIcaquFOZXcgjopaBG9LsymHJ8ciwSEjc-hwXCDGvQsDrVziuArayLiVRXNFdGAI00Njm50taaXcM5MPFe7MOYt-knYEVZgIdEwxwDQ1NLD4wBm-XpN7qI6J0b7HCOEbSdQtuTBDpJPp_Cyhr1wHGfBWgT8_LNcM0-s6IDrVQnRHND8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=GrSjJj0E1gDB9YDJKAD8Mo7xEQsOnQkbIrjKGe16E2BX1xSQzb69-31asohfg0jfpsb4h83ILbyWD4gnBy51TAjIggbYvBdgINyGAjYlyUIYY1hjrwYfJx6Jpu6b8rqdoopy3Xincm0jUoCeYAe4VElXBTjkHz6TVqefLKuOfQ10Aeki2-no4WfU3btMVwDn-YPqkL5UvFQ7tOgqzfXN-fSdxxKhuULfd3X8eylELdcc0hy0wNTEMvWC7F-d0Rhq6EdA4tHq_2QNkE8BwnYA6snRDJfwyvWjlT5lArVrEMvx2ykJFnBIF5dIsVi_ciVsY5n8WrQgpdF2ppQ-sAUIubK21h41b2v76wqcm6oeA6Y5KC4UQ94iaCfTsQAZ8MtpHS0LfmbNDRu7U0OS0-AX-vML4eEzujqWz2G5gPKccGCfnxJ4GhyOlSEU9XmzCfXpk441Hk-fLokIZVWm2C1YJRGnuzJlX5GSwtcJq7879EkLg4bUKeCLGy_vx1VeqIcaquFOZXcgjopaBG9LsymHJ8ciwSEjc-hwXCDGvQsDrVziuArayLiVRXNFdGAI00Njm50taaXcM5MPFe7MOYt-knYEVZgIdEwxwDQ1NLD4wBm-XpN7qI6J0b7HCOEbSdQtuTBDpJPp_Cyhr1wHGfBWgT8_LNcM0-s6IDrVQnRHND8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
وقوع یک سیل ناگهانی و شدید در منطقه مرزی میان نپال و منطقه تبتِ چین، خسارات سنگینی به بار آورد.
گزارش‌ها حاکی از آن است که در پی این فاجعه، تاکنون صدها نفر از غیرنظامیان و نیروهای نظامی و پلیس مفقود شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70622" target="_blank">📅 18:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
فکر می‌کنم ۳۰۰ [درصد] باشد. شنیده بودم ۹۰ درصد؛ اما به نظرم تورم ۳۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70621" target="_blank">📅 17:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=TCEbeqvXVU0cj8tUdhx-CSVIwK42zs4w6SolS9hB-JmBSg788r-AKGLnw8Hz4WWRRuxc_LrEQFE1SOPQ1tI1hIZVR3BxIc3O7NrYXbatmuEU5pi1RdyzfRh44GT6cDx_BvRpFm_SaNRtRm0rRpSAvIecb12O1o25YAmv4uDHi2yiKYcW09vht0hZ9R5pesfyA9PbTAdJnSQeIQzm2dEUD3LuW_OTMyMRTisZaqDCg0g7_9DoOs-cWMaJuRnrSWgHFqyygBrV2Jd-yESCzvoTarsRW9LWF4wFNWllyyEVh71xYrR8dA6O6A00s-eaorT50w6rkDFwgG8kYJOHUlj3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=TCEbeqvXVU0cj8tUdhx-CSVIwK42zs4w6SolS9hB-JmBSg788r-AKGLnw8Hz4WWRRuxc_LrEQFE1SOPQ1tI1hIZVR3BxIc3O7NrYXbatmuEU5pi1RdyzfRh44GT6cDx_BvRpFm_SaNRtRm0rRpSAvIecb12O1o25YAmv4uDHi2yiKYcW09vht0hZ9R5pesfyA9PbTAdJnSQeIQzm2dEUD3LuW_OTMyMRTisZaqDCg0g7_9DoOs-cWMaJuRnrSWgHFqyygBrV2Jd-yESCzvoTarsRW9LWF4wFNWllyyEVh71xYrR8dA6O6A00s-eaorT50w6rkDFwgG8kYJOHUlj3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
وقتی کسانی هستند که حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است؛ به همین دلیل است که آن‌ها اعتراض نمی‌کنند.
و البته احتمالی هم وجود دارد، چرا که آن‌ها بسیار تضعیف شده‌اند... به بسیاری از سربازانشان حقوق پرداخت نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70620" target="_blank">📅 17:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7effdb513d.mp4?token=es5FcT7xeCfRxAy3W9cfYYOUtSTO3MmqSWSs3C6x0rSToSJUJOr25eAnjRYEhQrlJK4pskxvZNTqP4M3bX436Hxd2gpwvIFO18di8QK_SJmCX8La3y2UiT-7pb1GcdBwONskq5nFJJnxblffe-5xfKNWI7RPmBvOfqZtEyIrjfHeQE7m0CmmURTX0jZdB2fUbjXD87PKuc8XrSEOmeA3aJje8AHrG-I33IUBjufkCLro2uUqJe1v_E056jCx8CfKOrgIUGqC4RQaTXmY_pszq4hnW_xeHwt3o6t-ZvveZ2KaJFC5SaxV_CEWDDDh0EO0aYWW2qcRqoUWlGEnlomb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7effdb513d.mp4?token=es5FcT7xeCfRxAy3W9cfYYOUtSTO3MmqSWSs3C6x0rSToSJUJOr25eAnjRYEhQrlJK4pskxvZNTqP4M3bX436Hxd2gpwvIFO18di8QK_SJmCX8La3y2UiT-7pb1GcdBwONskq5nFJJnxblffe-5xfKNWI7RPmBvOfqZtEyIrjfHeQE7m0CmmURTX0jZdB2fUbjXD87PKuc8XrSEOmeA3aJje8AHrG-I33IUBjufkCLro2uUqJe1v_E056jCx8CfKOrgIUGqC4RQaTXmY_pszq4hnW_xeHwt3o6t-ZvveZ2KaJFC5SaxV_CEWDDDh0EO0aYWW2qcRqoUWlGEnlomb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما از شر مین‌ها خلاص شدیم. اما تنگه هرمز... تنگه فعال است؛ یک تنگه فعال.
بله، هر از گاهی پهپاد یا راکتی یا چیزی شلیک می‌شود، اما این تنگه کاملاً فعال است.
مقدار زیادی نفت از آنجا جریان دارد.
دیروز ۱۰ میلیون بشکه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70619" target="_blank">📅 17:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70618">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ce2d5dc6.mp4?token=OOkqqFF7XcCW-tjlfLFIePeIt_rtKyBDzF1LA-5cWtHlBInJvMMzmP0igblsKaW4-AQ4Mi1RPqKizPbkYMU11f-lIi4bGvj2p-n0-OZgi_wvL8nFBuUwVklV-AVzQVgNyCVTbbAZvw-tuJdjJ3zjV74pxLhfuGEDiv5ySrSy1FBIhBEZFMhw4oy48JZES-VgaDEs7DTP7dvClJP3nOd8_ox2zVyC_2TN7fbI1znRMOfdZVw4IFiCIxErEIaBuauh2vX4DGog9T-zmyuapShtelHIeK8D1AoFsWdkNGvZyezFh7hvlVfCvxRM32MJC7gRg6gOAU_3T91FdYtnHVp7SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ce2d5dc6.mp4?token=OOkqqFF7XcCW-tjlfLFIePeIt_rtKyBDzF1LA-5cWtHlBInJvMMzmP0igblsKaW4-AQ4Mi1RPqKizPbkYMU11f-lIi4bGvj2p-n0-OZgi_wvL8nFBuUwVklV-AVzQVgNyCVTbbAZvw-tuJdjJ3zjV74pxLhfuGEDiv5ySrSy1FBIhBEZFMhw4oy48JZES-VgaDEs7DTP7dvClJP3nOd8_ox2zVyC_2TN7fbI1znRMOfdZVw4IFiCIxErEIaBuauh2vX4DGog9T-zmyuapShtelHIeK8D1AoFsWdkNGvZyezFh7hvlVfCvxRM32MJC7gRg6gOAU_3T91FdYtnHVp7SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«باید بگویم که آن‌ها اصلاً گروه شرافتمندی نیستند. و می‌دانید، ما کاملاً قاطع عمل می‌کنیم؛
دیشب ۲۲ فروند از قایق‌هایشان را نابود کردیم.
آن‌ها سعی دارند محاصره را بشکنند و وارد شوند.
نیروی دریایی و ارتش ما عملکردی فوق‌العاده داشته‌اند.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70618" target="_blank">📅 17:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70617">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecc2b192.mp4?token=liF51rtqgLNWp2RHIHmPnz86YY42kwP5S_BuM6ZXgc_O9ah_DKD1tkUJn6S_WhcOYhHae8N0wSomeYjmPbaR0QnQHs2AWboC7PfK0v4P9iISTRNFWGK2sNoKLOFwGGz9kcabIZ7OjhWZAOyAdw8Zh7zUvzclcF5FYCobKqWxQdiNB7vuNaOB3uY_oWjOR1UByyxqf7vrk4q_ScoTv3xJdfrXtY2Pz6HYEMBVDVVU0hWnRp_-4E993pVCyLFvGBvgm5RJZ8Yl7dqPzgzkXfMkqPxx2yH2MEkDgRs8iBtP4sbA3SbrsfLfcDxw73s4k-YipseEXb1RfvvEcOV0Rk7CUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecc2b192.mp4?token=liF51rtqgLNWp2RHIHmPnz86YY42kwP5S_BuM6ZXgc_O9ah_DKD1tkUJn6S_WhcOYhHae8N0wSomeYjmPbaR0QnQHs2AWboC7PfK0v4P9iISTRNFWGK2sNoKLOFwGGz9kcabIZ7OjhWZAOyAdw8Zh7zUvzclcF5FYCobKqWxQdiNB7vuNaOB3uY_oWjOR1UByyxqf7vrk4q_ScoTv3xJdfrXtY2Pz6HYEMBVDVVU0hWnRp_-4E993pVCyLFvGBvgm5RJZ8Yl7dqPzgzkXfMkqPxx2yH2MEkDgRs8iBtP4sbA3SbrsfLfcDxw73s4k-YipseEXb1RfvvEcOV0Rk7CUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره مجتبی خامنه‌ای:
فکر نمی‌کنم مجتبی خامنه‌ای مرده باشد.
او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دست و پایش، و تمام آن ناحیه آسیب جدی دیده بود.
اما گمان نمی‌کنم که مرده باشد.
اگر هم مرده باشد، دارند نمایش خیلی خوبی اجرا می‌کنند؛ چون مدام صحبت از این است که باید برای گرفتن تأیید نهایی‌اش با او گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70617" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70616">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/852e6e635a.mp4?token=OUi0E-P5WVYwHCG1I7uBKTXYc53vNcsNjFWVILPCIBsH5zWstiOs-W-e9o6y26khffvD0XOSkML7XyTtuTGLNmJhGz6ohjCFvKeEM64jttUl_7u34_ziiedsjamavrMXzyRhD-O-AUE0Eyz38DRik4nQvlJJawTUC5zDFyqJtQLaiKThEL_jtmwqvc8l4d49sFL1phOWp__3wCQCAzYPfVnc4LVBHtJeXosus7O8lY4qTu4UOzjlzaNh5Q2BjZGRneej54zMjTN48OnNkoUYA2cefph5wLslBK6UcmNTuTyOuynj3PfrXfT1w5b2eIugkvc6zEeTJoqkp3uVqGf5tg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/852e6e635a.mp4?token=OUi0E-P5WVYwHCG1I7uBKTXYc53vNcsNjFWVILPCIBsH5zWstiOs-W-e9o6y26khffvD0XOSkML7XyTtuTGLNmJhGz6ohjCFvKeEM64jttUl_7u34_ziiedsjamavrMXzyRhD-O-AUE0Eyz38DRik4nQvlJJawTUC5zDFyqJtQLaiKThEL_jtmwqvc8l4d49sFL1phOWp__3wCQCAzYPfVnc4LVBHtJeXosus7O8lY4qTu4UOzjlzaNh5Q2BjZGRneej54zMjTN48OnNkoUYA2cefph5wLslBK6UcmNTuTyOuynj3PfrXfT1w5b2eIugkvc6zEeTJoqkp3uVqGf5tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز 4 شهریور ماه، زادروز شاهِ شاهان؛ کوروش بزرگه
.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70616" target="_blank">📅 16:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70615">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b4425472.mp4?token=hj8PJ3j6zbgpUzIC2RSPHifJxVMRpJW68GD2UYNB3iDBwBuyNOeW4z-j-RlbQzHeJw-epwiKLf7L_rvw-ugIT15E-K9Uo2PsB0a6y2w4Oxi3Y2W3sTBAe-oTzNuHPOP9_CfL36jbJHDqoljCTA32cJfU7M5evIu_fPr1NMCteGcikh5aN0ygY_pG7cBWYjTzE402Qt2yxD2PvjEOZNc2h88NoTWol09pMPRHwK56nre_XmaDx1BBWdojf6t3OkiWy7sOa6lUneMs646q6uCEkn1KlAkDzZ_Sj8rrLs5ttnanza1tJ4q8X_onTUkd1gnPky_xizCN_1W24qdR5nF5dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b4425472.mp4?token=hj8PJ3j6zbgpUzIC2RSPHifJxVMRpJW68GD2UYNB3iDBwBuyNOeW4z-j-RlbQzHeJw-epwiKLf7L_rvw-ugIT15E-K9Uo2PsB0a6y2w4Oxi3Y2W3sTBAe-oTzNuHPOP9_CfL36jbJHDqoljCTA32cJfU7M5evIu_fPr1NMCteGcikh5aN0ygY_pG7cBWYjTzE402Qt2yxD2PvjEOZNc2h88NoTWol09pMPRHwK56nre_XmaDx1BBWdojf6t3OkiWy7sOa6lUneMs646q6uCEkn1KlAkDzZ_Sj8rrLs5ttnanza1tJ4q8X_onTUkd1gnPky_xizCN_1W24qdR5nF5dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کوهنوردای ایرانی موقع صعود تو کوه های آرارات، آیفون17 این دختر آرژانتینی رو پیدا کردن و بهش تحویل دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70615" target="_blank">📅 16:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70614">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662dd7f509.mp4?token=m6IwxS9ZcB9Dr62oUl56WUxvyDy2AZY_ekvRZM2MtwFiq-94SSkr84LPrTqdaUez3NrIZepRP0xxSGvf9aI46Qn-cqP9463lwIglt7cf--qtGT9wzkbQoEAXPlYoSsyhCkn3CGNTJY_AlcKeAI96eM8MIIV7DOXnByC1Iqh5BUsq0njLxJ939HTHO_s1lBtGYzSEIU1b9wgCt6u4tWAqVW5vm5J8pROASGuVWgR30Y-jqANYoh-4Tt6NjEFiBpRhFjYbu3RDX3HBTI2PtTCqYCyHKiZNW4D9zUaomDsXnmjHo4lCcfA6sEX1ZyFaEhgtjOYWBzkGNnsCAQe0ktO4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662dd7f509.mp4?token=m6IwxS9ZcB9Dr62oUl56WUxvyDy2AZY_ekvRZM2MtwFiq-94SSkr84LPrTqdaUez3NrIZepRP0xxSGvf9aI46Qn-cqP9463lwIglt7cf--qtGT9wzkbQoEAXPlYoSsyhCkn3CGNTJY_AlcKeAI96eM8MIIV7DOXnByC1Iqh5BUsq0njLxJ939HTHO_s1lBtGYzSEIU1b9wgCt6u4tWAqVW5vm5J8pROASGuVWgR30Y-jqANYoh-4Tt6NjEFiBpRhFjYbu3RDX3HBTI2PtTCqYCyHKiZNW4D9zUaomDsXnmjHo4lCcfA6sEX1ZyFaEhgtjOYWBzkGNnsCAQe0ktO4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی وایرال شده از نوجوونِ 18 ساله‌ای که با موتور کار می‌کنه:
من روزانه 8 الی 10 ساعت کار میکنم!
امروز یکی ازم پرسید چِتی میزنی یا نعشه بازی؟ گفتم هیچکدوم.
با خودم گفتم من باشگاه‌ام رو میرم، خرجی خونه رو کمک میکنم، اهل دود و دَم و دختربازی هم نيستم.
به خودم اومدم دیدم از خیلی از هم‌سن‌هام جلوترم واقعا
تویی که از این روتین خوشت میاد و سالم زندگی میکنی، به خودت افتخار کن، چون مثل تو خیلی کم شده..
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70614" target="_blank">📅 16:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70613">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/91fcce4d61.mp4?token=mC6r4UY9Yog_5Q3Vg9pfHyqpEWO5LYjANro8_0xEei16TlOK5sXp6Ei-RoGZG9pZ0WD3o9G5ZGnJmeSga6bLj_uUHo_eONQH42prA1N4miYmmnwM1sW99AQnkRScD479k-FasnliZbhLMsj3PawuJOedNJbAwYc2il1qvw8pR-uYy683L_dmEL8G0itakGGHFBOVR-RJicSwaUrLpbjZvuoQo7ChXbfStEPjbOv72VHiVCzYIh7pt0Q1mdeyYkRpr5rUaP6yKxBfEyh3KHB9GLFOnoo2wzCJQv9sLihBHRU7QIY-8nB98nJz-Q0po1TyEpzBWlA9mLrVb0e_TC_eYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/91fcce4d61.mp4?token=mC6r4UY9Yog_5Q3Vg9pfHyqpEWO5LYjANro8_0xEei16TlOK5sXp6Ei-RoGZG9pZ0WD3o9G5ZGnJmeSga6bLj_uUHo_eONQH42prA1N4miYmmnwM1sW99AQnkRScD479k-FasnliZbhLMsj3PawuJOedNJbAwYc2il1qvw8pR-uYy683L_dmEL8G0itakGGHFBOVR-RJicSwaUrLpbjZvuoQo7ChXbfStEPjbOv72VHiVCzYIh7pt0Q1mdeyYkRpr5rUaP6yKxBfEyh3KHB9GLFOnoo2wzCJQv9sLihBHRU7QIY-8nB98nJz-Q0po1TyEpzBWlA9mLrVb0e_TC_eYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ هر ثانیه بیشتر سورپرایزت میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70613" target="_blank">📅 15:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70612">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee1652504.mp4?token=lyWtm8z83Uu2zOon0zv18xa8O5Y1U944dMYbRrlmvnHu2B8ehGCAxA-31dgrx_pVOo3Q8nSBkfhmyd_j-9LknaOSKwLLjFnmiHaOXK_0180LlB7q4a4xtbRH7y0dphy5tciHShM9xurEMK0TzZga4myXg9bjV9jGAbVu6DudhjZhLiD5r33AS5DmsaiVizNt5Bwu3QJL_7b5vN1Fd-fi51IC802DR3kU6iywmKw19IHQjhRhP2f9b_TnGD1iOjB5q5x2TSLtocgvMOtlkRWbPD7adg-9S5pVZZwF6QC3hPO3mAD77aEalsuACat3RzzZ-AT6sWuFRYFwEQD6AC2z8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee1652504.mp4?token=lyWtm8z83Uu2zOon0zv18xa8O5Y1U944dMYbRrlmvnHu2B8ehGCAxA-31dgrx_pVOo3Q8nSBkfhmyd_j-9LknaOSKwLLjFnmiHaOXK_0180LlB7q4a4xtbRH7y0dphy5tciHShM9xurEMK0TzZga4myXg9bjV9jGAbVu6DudhjZhLiD5r33AS5DmsaiVizNt5Bwu3QJL_7b5vN1Fd-fi51IC802DR3kU6iywmKw19IHQjhRhP2f9b_TnGD1iOjB5q5x2TSLtocgvMOtlkRWbPD7adg-9S5pVZZwF6QC3hPO3mAD77aEalsuACat3RzzZ-AT6sWuFRYFwEQD6AC2z8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
لحظه شلیک RPG توسط سرباز روسی که جلوی پاش میزنه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70612" target="_blank">📅 15:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70610">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/378122b9f3.mp4?token=lRvcVJ6k4rO-IRhlL0OzjPspLbY5KWIfuPHYsFH5vuBJLh09LIsibOHHfowKInVjg_OUUmMj-awYt6fhz-KoP2FoBBgVFz109-qJldqaHFfglC26WVEoS-x6DRogDSYVKWhq8O9RPc_ElHHyABtEVp0XWxwGjdkFzGB3JkYKqRoofgYWO3xxUP3LRGzxDvq_JNzs0axIswJY2H7VBGXSvfKMT6a783n5e88jLc7fXoa5A-9TDzEfkBQmDUcfMw7G42GEsqC8UE5z7ma0Qf4p7sI7GdZd8jwnyjwfTaAyDcgPMWkY8YUaJlz-nOn4TfJmdmXbh7Gp_By4WIbzWcI0GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/378122b9f3.mp4?token=lRvcVJ6k4rO-IRhlL0OzjPspLbY5KWIfuPHYsFH5vuBJLh09LIsibOHHfowKInVjg_OUUmMj-awYt6fhz-KoP2FoBBgVFz109-qJldqaHFfglC26WVEoS-x6DRogDSYVKWhq8O9RPc_ElHHyABtEVp0XWxwGjdkFzGB3JkYKqRoofgYWO3xxUP3LRGzxDvq_JNzs0axIswJY2H7VBGXSvfKMT6a783n5e88jLc7fXoa5A-9TDzEfkBQmDUcfMw7G42GEsqC8UE5z7ma0Qf4p7sI7GdZd8jwnyjwfTaAyDcgPMWkY8YUaJlz-nOn4TfJmdmXbh7Gp_By4WIbzWcI0GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این زوج به اسم مینا و رضا بعد از پنجاه سال هنوزم عاشقانه همدیگرو دوست دارن و پنجاهمین سالگرد ازدواجشون رو به زیباترین شکل جشن گرفتن و رقصیدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70610" target="_blank">📅 14:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70609">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJgQKNZp42lPrkkj4hNK-3eauC4r6EFmwf0z0h6v3pk_eQ1VuTjouAHSdHdTM7e7ExA1andi5IeFCqneg5bgFveoUm5gAq9Br8pFdlLwfSWyUWZ35Qxxgry8rXn17eO3M1tj2jsPyfTA8gZ3L2ilw3K69_OOhS4LHzVYwM0bdEdsWBdPaCYhohL5cyNPGIkMcWHZK-dLRlBku_LyV2wPMqldr-1ZS0fSC_aslvDtoW0gZ5WDNY-D8M9JfzB58pBM7kJR1jn1qcNUvZP4ZCwvzssh0HiUiy8MtLbxEEvWtUmfpxTPaQireJC_ayfQjIMAcaQgeDMOxLu_Y3slxNMDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زمان شاه هر اسکناس هزار تومنی، معادل ۱۴۲ دلار بود!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70609" target="_blank">📅 13:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70608">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=DQv9IOswWGSCcbPG-xB6n7D3WOB1mfdgtiR9LtOTfZYaiOub6H7NWTX-s7GNjQOfOxGturTwB5iWLLl_kA8EcptcKvm1vLGl9q1EHMAcu78ZEETNDvqmBPpcV97NWRbgh--ud6LSfgMJUdF8vdHfKzXLjUnQzBW6kXAWbiJ75ObE7rJ9BUfgxEysYk26LUyuqATxHIYAlwhRTA2xEqusCioi_teNeoYPuPLFCPV12UFhu-VHtxBcBKDenSRBk6zyIIqLCQiwGdLyCoxe3CKd6AKfyipYDdwzMQPejxH4708WtPMmQqyECTfHExPxUK0mV73HYuNRf4tYLHlc1yc4kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=DQv9IOswWGSCcbPG-xB6n7D3WOB1mfdgtiR9LtOTfZYaiOub6H7NWTX-s7GNjQOfOxGturTwB5iWLLl_kA8EcptcKvm1vLGl9q1EHMAcu78ZEETNDvqmBPpcV97NWRbgh--ud6LSfgMJUdF8vdHfKzXLjUnQzBW6kXAWbiJ75ObE7rJ9BUfgxEysYk26LUyuqATxHIYAlwhRTA2xEqusCioi_teNeoYPuPLFCPV12UFhu-VHtxBcBKDenSRBk6zyIIqLCQiwGdLyCoxe3CKd6AKfyipYDdwzMQPejxH4708WtPMmQqyECTfHExPxUK0mV73HYuNRf4tYLHlc1yc4kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تا آخر شهریور هیچگونه تغییری در بنزین 1500 و 3000 تومانی نخواهیم داشت
‏مهاجرانی: تولید داخل و ذخائر استراتژیک بنزین مناسبی داریم و جای نگرانی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70608" target="_blank">📅 13:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70607">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=QaPZasNMp2aH90awUqrSXwzObk2m1vARq8ms-UI6o5GGMaWttZmEr6GNbG2gE6BXP6lYnS-MSAyaiRC4XdJUHgYifbn2fNxaw7ii_3KNBiv1EaTSIwPaE7MEWk8MG1Vw5rpftn4OYvuv3upXq1ScxoOF3dpp5QoaNGvZ9wQW7XlmViLKCh6AZsGzK6Fll3By8C7iCuqbOjh0YbbrmspJbRkJYLQuRzsEO0eYqeZumhi1YGyzTwz2eBmJnrTKRozFQMAtORwKBpBWLBBRF02DFNv2UrujTzScGwtpDx2X0InL5P2vzXlSIkOGW3jk7UJPZPJdWClNDyOGHenDkzxckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=QaPZasNMp2aH90awUqrSXwzObk2m1vARq8ms-UI6o5GGMaWttZmEr6GNbG2gE6BXP6lYnS-MSAyaiRC4XdJUHgYifbn2fNxaw7ii_3KNBiv1EaTSIwPaE7MEWk8MG1Vw5rpftn4OYvuv3upXq1ScxoOF3dpp5QoaNGvZ9wQW7XlmViLKCh6AZsGzK6Fll3By8C7iCuqbOjh0YbbrmspJbRkJYLQuRzsEO0eYqeZumhi1YGyzTwz2eBmJnrTKRozFQMAtORwKBpBWLBBRF02DFNv2UrujTzScGwtpDx2X0InL5P2vzXlSIkOGW3jk7UJPZPJdWClNDyOGHenDkzxckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
می‌خواهم به شما بگویم: ما همچنان با چالش‌هایی روبرو هستیم.
چالش ایران پایان نیافته است.
ما همچنین باید کار را در غزه، لبنان و سایر عرصه‌ها به سرانجام برسانیم و برای انجام آن مصمم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70607" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70606">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=e2e7ML4kAvgTmBRIT47lldtpcBY5ATdfMAwdGb29I-4ehumgY0kjM0_PFmxRzyEjsqL_9A4F7ZuiQXFjRK3WDfWQ6i5Odn0islh3jLeehU_dAx9XDAIBOMW1Ar1DK9hwcCiYG5Xxp_2bH-JEvg42-G0FQkq1nAqrWGjjC0ICpOhBdgpHn221VgX5neEGwhNiy_iek2JxUcI9z0G1Xpo75lf6Lt1FSe1iSc5grcmmp6YXGEjdDSmOwRiTMfRRxyf2gFnlQogJUqj4-JuaUsmSG_y5cd5peWpGf88ANzornwGcQn58p7wffSYA93zZL3w9xamc9-mduZ_Wo_2KU08YfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=e2e7ML4kAvgTmBRIT47lldtpcBY5ATdfMAwdGb29I-4ehumgY0kjM0_PFmxRzyEjsqL_9A4F7ZuiQXFjRK3WDfWQ6i5Odn0islh3jLeehU_dAx9XDAIBOMW1Ar1DK9hwcCiYG5Xxp_2bH-JEvg42-G0FQkq1nAqrWGjjC0ICpOhBdgpHn221VgX5neEGwhNiy_iek2JxUcI9z0G1Xpo75lf6Lt1FSe1iSc5grcmmp6YXGEjdDSmOwRiTMfRRxyf2gFnlQogJUqj4-JuaUsmSG_y5cd5peWpGf88ANzornwGcQn58p7wffSYA93zZL3w9xamc9-mduZ_Wo_2KU08YfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
⏺
و من به ترامپ گفتم که احتمال سومی هم وجود دارد: تشدید محاصره.
او دیروز آن تصمیم را به شیوه‌ای بسیار بسیار قاطع تأیید کرد.
اقدام دیروز رئیس‌جمهور ترامپ، تشدید محاصره ایران بود؛ نه از طریق تنگ‌تر کردن حلقه محاصره خودِ ایران، بلکه با تشدید فشار و محاصره بر کسانی که به این رژیم — این دیکتاتوری هولناک — کمک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70606" target="_blank">📅 12:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70605">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c258982c.mp4?token=LgpU1NWs-SPE3c0ffUCITxpb2_ayaxE033B307bM2BdWMUok0lIQ1k22dPn0s4hYKZmMbeKtLYMAYwP51LGQ2ikDR-NizVAiPvNMhaMxVU3IqYwmiXcS_sNts9UJ98R4nvk1WEj9uotCk-FyHngTod8sOYG9fJqki6znB8lv5dH7eflT7fBrfGm1nfz7OArfQYrDDWRlRKxBpZG4YuHl2Rlho61-kHM7n2PubrWLfVlRGLTxnFFi4F_Plb_3KFBrta8XivtbMI5nsol7T6StkUJpbzcaugC-og98B3vZ0oRnlIutrmQh_OUz9z5RkeVtK5CzG5JfMn5HwyK6qXG-Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c258982c.mp4?token=LgpU1NWs-SPE3c0ffUCITxpb2_ayaxE033B307bM2BdWMUok0lIQ1k22dPn0s4hYKZmMbeKtLYMAYwP51LGQ2ikDR-NizVAiPvNMhaMxVU3IqYwmiXcS_sNts9UJ98R4nvk1WEj9uotCk-FyHngTod8sOYG9fJqki6znB8lv5dH7eflT7fBrfGm1nfz7OArfQYrDDWRlRKxBpZG4YuHl2Rlho61-kHM7n2PubrWLfVlRGLTxnFFi4F_Plb_3KFBrta8XivtbMI5nsol7T6StkUJpbzcaugC-og98B3vZ0oRnlIutrmQh_OUz9z5RkeVtK5CzG5JfMn5HwyK6qXG-Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
⏺
به ترامپ گفتم:
البته یک احتمال این است که شما با ایران به توافق برسید؛ یک توافق خوب. ما هیچ مخالفتی با آن نداریم.
اما تردید دارم که بتوانید با آن گروهی که آنجا هستند — با آن وحشی‌ها — به توافق برسید.
🔴
به شما می‌گویم: نمی‌توانید با آن‌ها توافق کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70605" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70604">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=uQifEj-KVP9oNyLwxUBXvIU584p3Cu4Kdfg8hvbvZMCrskMQ7RBgU5UbKuUXq1rqQWyruClghHHOb3AdSuwNj2oW8oFE_MHmMPCR6RrjbOVQ6N1Ynep1TWpOAbWOis9v3MvdtlQc_nnPEzYDvo8z52UhphdO-VrQchsMRRV6oB_b1OgMDIaYSkLLn4cAuBA1nNsXKRI7OVfERcJ6EcaKM-0hAE1TZRhHCevwyzAyX3zJZsiCnbsZq2k3wl4mkOA6zJg7W4Jg3dxYXzA90rkywDS-cBFIlFr5fRptMGwqFAi3IK9IDFafryl22S7sDjADqAO3D_bz76LPe4-UiDdogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=uQifEj-KVP9oNyLwxUBXvIU584p3Cu4Kdfg8hvbvZMCrskMQ7RBgU5UbKuUXq1rqQWyruClghHHOb3AdSuwNj2oW8oFE_MHmMPCR6RrjbOVQ6N1Ynep1TWpOAbWOis9v3MvdtlQc_nnPEzYDvo8z52UhphdO-VrQchsMRRV6oB_b1OgMDIaYSkLLn4cAuBA1nNsXKRI7OVfERcJ6EcaKM-0hAE1TZRhHCevwyzAyX3zJZsiCnbsZq2k3wl4mkOA6zJg7W4Jg3dxYXzA90rkywDS-cBFIlFr5fRptMGwqFAi3IK9IDFafryl22S7sDjADqAO3D_bz76LPe4-UiDdogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رفسنجانی سال ۱۳۶۰:
پهلوی همه همت و دغدغه ش این بود که مردم خونه و ماشین خوب داشته باشن؛ زندگی خوبی داشته باشن و ارتباط ایران با کشورهای جهان خوب باشه ولی الان دیگه اینا ارزش نیست و برای کسی مهم نیست .
الان دیگه مردم دنبال معنویاتن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70604" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=a_eYgzkJHrOkh1I6LT27XBioEMB-YnqYBlIqXwySGEiRzSZNxIOsIVNrsZivNu_AMbloodnAauMOgY5uNezjC_fK7H9jvbhgX4pD7pipjKxqTDc5cIdJSuYCEMob6W39mI0g1-3tXuf3SlFUKLiFJI-cDlMVLFDvfKmshOE8mR4rgUGdtN5V0iamYfcHaCL82OburL4Wfxube3Zs6SDxwYXpy09XDrkL12eQmaR9xDPkITlLnyTaJRvnuhck0n8MFeIuO4QgK7f6K7ibP0KAsdV4NjT6vbdNjuaQTkr6060h46PQiVnlbW5glSPFzWc89dI_GHA3P5gITwcd-1BOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=a_eYgzkJHrOkh1I6LT27XBioEMB-YnqYBlIqXwySGEiRzSZNxIOsIVNrsZivNu_AMbloodnAauMOgY5uNezjC_fK7H9jvbhgX4pD7pipjKxqTDc5cIdJSuYCEMob6W39mI0g1-3tXuf3SlFUKLiFJI-cDlMVLFDvfKmshOE8mR4rgUGdtN5V0iamYfcHaCL82OburL4Wfxube3Zs6SDxwYXpy09XDrkL12eQmaR9xDPkITlLnyTaJRvnuhck0n8MFeIuO4QgK7f6K7ibP0KAsdV4NjT6vbdNjuaQTkr6060h46PQiVnlbW5glSPFzWc89dI_GHA3P5gITwcd-1BOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مدیر شرکت «فردا موتور» داشت واسه ثبت نام کنندگان خودرو توضیح میداد که ماشین نداریم. دو سال و نیم صبر کردید؛ باید چند ماه دیگه‌ هم صبر کنید که مردم گفتن «سیشتیر بابا همتون همینو میگید» و ریختن سرش.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70602" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70601" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70601" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_YINNULRupLL0mIi_IbjL33VtZprRnNXHiLmoaxQY3gisjo0Ob6eTS0fay-V1skEPFQPMmtZlsIzL2fhdFRAW1CE9hyGUlGB0A8gQXfFYhEXbFHJNGGs05GqGW0YuI_ruvPUFKL4pEkhETTAaZKc3F-IQlCycRavKvOAh_YS6Z9Kp4dCEnKZy-xqpAxOqgMow08UxnD7tnnBeVt_Ca0exEDd6boWiJQvjQh8y4JbH74FqGzBPTkWAy71ixG5OxoYE5_WmOZXOsFRL_fVYrbxHOLeZzW_ZTTYQHL0FWp6Zsei-_VF_Y0A0tpk0MZiGcldfcyYPh1JfDFifx4QIMEGg.jpg" alt="photo" loading="lazy"/></div>
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
r4
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70600" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=pFPipaB6P9uhSNKgT1K_w5NEfz1maSjuHiPhq8ytYDQq_JmhLOs__78_nB3QCOKULkrQia-Ky6VPDtXiaX98W4RVQS1xenk555PUZkCzsjK3wih7vJZslGrEGXbdgyTGA0NcljwuOLrg0MCNJwpZoGy_JinmjSFe28pdffNnmpxWC2Y0e-BDe0T8JCD-JR9ElThTJqzr8P3m7OZof1M-S0AwrJIh4Fq0qCaNrkme9jPWllrLRqluwlo4NF95-gjOQBKqdudlTi__noxer_vOiqQjBpyIsizr1mPKmO47uPffyDCuwzZoLLihZMTCo0NvGvr3_mwuymajl6XJAVHz5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=pFPipaB6P9uhSNKgT1K_w5NEfz1maSjuHiPhq8ytYDQq_JmhLOs__78_nB3QCOKULkrQia-Ky6VPDtXiaX98W4RVQS1xenk555PUZkCzsjK3wih7vJZslGrEGXbdgyTGA0NcljwuOLrg0MCNJwpZoGy_JinmjSFe28pdffNnmpxWC2Y0e-BDe0T8JCD-JR9ElThTJqzr8P3m7OZof1M-S0AwrJIh4Fq0qCaNrkme9jPWllrLRqluwlo4NF95-gjOQBKqdudlTi__noxer_vOiqQjBpyIsizr1mPKmO47uPffyDCuwzZoLLihZMTCo0NvGvr3_mwuymajl6XJAVHz5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای یه آخوند طرفدار حکومت راجب حجاب
:
اگه شما آزادی پوشش داری، ما هم آزادی تجاوز به شما رو داریم
چرا اون کسی که میخواد به زن ها تجاوز کنه آزادی بهش نمیدید؟ آزادی باید بهش بدیم دیگه خودش انتخاب کرده که مزاحم همه بشه
اگه مردم آزاد باشن که هرجور دلشون خواست بیان بیرون پس باید متجاوز ها هم آزاد باشن
چطور میگی قانون باید جلوی متجاوز رو بگیره اما قانونی که باعث بشه لخت و پتی نیای بیرون نباید جلوتو بگیره؟
چطور تو آزاد باشی اون آزاد نباشه
هرکی لخت بیاد بیرون حقش اینه که سرش بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70599" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=I7Nm5bSRmj0ZsGFaAXRGGKqK7rqb-YstUpFisWKX05zJToqLh9UkmXJOjiTfXEmMBsJ1upBJEZrFxe0PepJFFb_qHBTDsK0BiPAUPQe5rXXwlIu2NtzjZr1EbW2_oZkTi-HZS0ZGW7xUfGHcT273OrppX8V9wFDgCp1Ca2EO301gAQ--WTLxJbuNdV-tSA_IWLf2wBA6nD3MN-Ox-f31yEqScNtDPmnj17ZL5ZGCV39kcvVU1MwbCByYp7gVCWCYJadVtlsZE3QiGh2h1VqzoSXfwJOY0ShX1Yn0WnS-pN9Y_qZYn6jFnoAl8ZcS7-_Y5DifUO9VnWurB_Wc-poYrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=I7Nm5bSRmj0ZsGFaAXRGGKqK7rqb-YstUpFisWKX05zJToqLh9UkmXJOjiTfXEmMBsJ1upBJEZrFxe0PepJFFb_qHBTDsK0BiPAUPQe5rXXwlIu2NtzjZr1EbW2_oZkTi-HZS0ZGW7xUfGHcT273OrppX8V9wFDgCp1Ca2EO301gAQ--WTLxJbuNdV-tSA_IWLf2wBA6nD3MN-Ox-f31yEqScNtDPmnj17ZL5ZGCV39kcvVU1MwbCByYp7gVCWCYJadVtlsZE3QiGh2h1VqzoSXfwJOY0ShX1Yn0WnS-pN9Y_qZYn6jFnoAl8ZcS7-_Y5DifUO9VnWurB_Wc-poYrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این خانمه داره مشاوره میده یک فرد چطوری با رابطه تریسام کنار بیاد
😐
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70598" target="_blank">📅 10:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=rabd8qor8MVV9E01oPhetU8kxrwRCMBmCBO0ZC4i3cvrXXCHY8Tdpvudynwjig4dpZPeTN1IRfb8O0WfqfptoX6Jn-_rJoy0hlDHpBqaxXQJuPsw74Rz_zQo1M27FcIuHlKaid4KrzcocVwfC-CbosEWiIb-a-raeOhOrPBREsrcm7q4hKz9jPggvl9J2ulE-YFRNn82LaVX7PAY8fjy40evtt5D8NmX1L32TXwmd4iPFlDHTPuNf9rRaPws0fep-xnEOLvmkW4raftqqtGqh9YDG9xHwmHchk2O1id2upGyFGJXlNF-rZrS1Mnp0ljmTnVydEFOsFfl8jLmBhmnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=rabd8qor8MVV9E01oPhetU8kxrwRCMBmCBO0ZC4i3cvrXXCHY8Tdpvudynwjig4dpZPeTN1IRfb8O0WfqfptoX6Jn-_rJoy0hlDHpBqaxXQJuPsw74Rz_zQo1M27FcIuHlKaid4KrzcocVwfC-CbosEWiIb-a-raeOhOrPBREsrcm7q4hKz9jPggvl9J2ulE-YFRNn82LaVX7PAY8fjy40evtt5D8NmX1L32TXwmd4iPFlDHTPuNf9rRaPws0fep-xnEOLvmkW4raftqqtGqh9YDG9xHwmHchk2O1id2upGyFGJXlNF-rZrS1Mnp0ljmTnVydEFOsFfl8jLmBhmnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
همتی رئیس بانک مرکزی :
علت بالا رفتن قیمت دلار طبیعیه و نوسان های خاص خودشه
ما نمیتونیم بخاطر یک نوسان بیایم مسیرمون عوض کنیم
مسیر ما درسته و خوب جلو میره
اگه این مسیر ما طوری باشه که میان مدت دیدیم درست نشد اصلاحش میکنیم
ولی من معتقدم که این شوک هایی که ایجاد شده جوسازی امریکا هست و شرایط مطمئنن درست میشه و رفع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70597" target="_blank">📅 10:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70596">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
ویدیو وایرال شده از یه جوون ایرانی خطاب به مسئولین جمهوری اسلامی
تراپی خالص :
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70596" target="_blank">📅 09:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0e780a212.mp4?token=jVy6SiifaCdR8aYodLGCAmJAPJzR52IkNrTqgYvTgviyyzrgqcQoPE0H8cnd41Avu1UhY3iVwFqfzhuDphh0pbPf8j0vsDmpWCjmCvDYg8kUxCrEVHaa8G_GKMVZ2GqtH4kBJMii74rS0iWZNXpdUZMIVSQDw6Zbprp3GgBwwjKWFdhsizU4xe4dPueKgYHpcDqaxf9nrzJgyTT9WegvNCzU5QRo0vBD9zADj43Ch0w7etXjgNPtiZVfx_amOKgvg-CrfBezz9LBIhvHlF0xGJSN58aEIcV272xj4h9uoSl43gj8E6bF-nPuRPs3LkoQH94hZdCNRDGJOCC-hpgbLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0e780a212.mp4?token=jVy6SiifaCdR8aYodLGCAmJAPJzR52IkNrTqgYvTgviyyzrgqcQoPE0H8cnd41Avu1UhY3iVwFqfzhuDphh0pbPf8j0vsDmpWCjmCvDYg8kUxCrEVHaa8G_GKMVZ2GqtH4kBJMii74rS0iWZNXpdUZMIVSQDw6Zbprp3GgBwwjKWFdhsizU4xe4dPueKgYHpcDqaxf9nrzJgyTT9WegvNCzU5QRo0vBD9zADj43Ch0w7etXjgNPtiZVfx_amOKgvg-CrfBezz9LBIhvHlF0xGJSN58aEIcV272xj4h9uoSl43gj8E6bF-nPuRPs3LkoQH94hZdCNRDGJOCC-hpgbLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
غریب‌آبادی، معاون وزیر خارجه جمهوری اسلامی:
چرا باید همیشه منتظر حمله آمریکا باشیم؟ ما میتونیم پیش‌دستانه اقدام کنیم
بازگشایی تنگه هرمز فقط در صورتی انجام میشه که جنگ در همه جبهه‌ها تموم بشه، محاصره برداشته بشه و وضعیت یمن حل‌وفصل بشه
به فرمانده ارتش پاکستان گفتیم ما توافق رو نقض نکردیم
اگه آمریکا میخواد تنگه هرمز دوباره باز بشه، باید همه شرط‌هایی که ایران توی توافق گذاشته رو قبول و اجرا کنه
ما هنوز در وضعیت جنگی هستیم و تا وقتی این شرایط ادامه داشته باشه، تنگه هرمز هم بسته می‌مونه.
اگه آمریکا به اقداماتش ادامه بده، ممکنه قابلیت‌های نظامی جدیدمون رو هم رو کنیم.
تنگه هرمز تنها ابزاری نیست که ما در برابر آمریکا داریم. آمریکا نباید فکر کنه فقط خودش می‌تونه به اقتصاد طرف مقابل ضربه بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70595" target="_blank">📅 09:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70594">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70594" target="_blank">📅 02:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70593">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IgVCdyGQe_Lz-dJuN2cCnGIz3Zmxr09iuYywh744cQIT8hiZlxycWlrB5ce3YTTLBkwvB27hco4rc94RxdVYRRBK0QG_jfx-8BNIOILzi2Dt5UZodUenqqgF-CmK5Fk0GJdyAQDcoTv2XgCgYV1DjZ34PkCbhf86A4yb7AtJnOp1irhQCnupMf3QB0bc0FYKsN_74uolbr0V7AL41eMWloJl-UR_qsZno7JwgOwbDJbbc8Vu8Vmj2XH7UmqTUcXNca1bIxsXgIJ12XdKOyk7O4AU6v4-lIBtrCvEngTB6yRFfapUpujYHm8iHVhX9TvquUBasvzFFMs8kdLcImm7NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IgVCdyGQe_Lz-dJuN2cCnGIz3Zmxr09iuYywh744cQIT8hiZlxycWlrB5ce3YTTLBkwvB27hco4rc94RxdVYRRBK0QG_jfx-8BNIOILzi2Dt5UZodUenqqgF-CmK5Fk0GJdyAQDcoTv2XgCgYV1DjZ34PkCbhf86A4yb7AtJnOp1irhQCnupMf3QB0bc0FYKsN_74uolbr0V7AL41eMWloJl-UR_qsZno7JwgOwbDJbbc8Vu8Vmj2XH7UmqTUcXNca1bIxsXgIJ12XdKOyk7O4AU6v4-lIBtrCvEngTB6yRFfapUpujYHm8iHVhX9TvquUBasvzFFMs8kdLcImm7NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a3
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70593" target="_blank">📅 02:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3eP00gjcImjDS54k_KCghN3WPFhxOAY28nIohnMaz_D3NFe04i7UnbCEY47imezS9stLp0mXG06dciOUTGUlKviRg_an8Lur2yTSGMSqktzEi5bMC0O6jOamgIERloWt7q9T6hbbv3E7KMOXUjbZOfWwZv4fwoCN6YIi4xdIxCoDAJSkuOyGLjJmPZtX441sWix8uGUCDaIJWpvRTqR8gsSTVnFK8XhUACdVJRNNm1KfeUnoWOtkago03KIbEFs39QFZjWQjF8vtg17Uet6Bg5zIkhOTcJlNS9SuBBAkGB86stge7HE2DkaKuxNuHycJnRAlbHLIesWue5Hc61qhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وام ازدواج برای یک زوج ۶۰۰میلیون
⏺
یخچال ساید ۵۰۰میلیون
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70592" target="_blank">📅 01:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8FTdugQD-1M2rmJZjlzbRtPoP9ozvAT0qaW5uaN_vNrBdEy6WIPFj5kbTg_WPKdnjJ_WooQTHLnUC6-oARsOpb2sWcfjVuaRZagy3MGmbb9brKhPOrcxOWNyozNnnbcHbjySxzNbrf8jIaRkby3-VGclYYm9-ZY8kCEETSLkvDVDR_IoQ6lPW7dXBFboRCUeUszk10pmgUjTXEqayC6kOYuzkFgJ4Zgpdk7ZAdsc9T2KfqfBGbZ3CdTxRIc1HNeWUyS3x7v0DXS9P--3WPp_Mm-gm9cMdUsVUJe3eU22u0xl0ixfKBDI8XUE0W9JNC63P7lPp1nsy7dGFkzjZ95hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
اکسیوس:مارکو روبیو، وزیر امور خارجه، به چندین تن از همتایان خارجی خود گفته است که ایالات متحده «در حال حاضر» برنامه‌ای برای انجام حملات جدید علیه ایران ندارد.
در عوض، دولت ترامپ بر اشکال دیگر فشار، از جمله محاصره دریایی و کارزار تحریم‌های تازه اعلام‌شده، تمرکز کرده است.
روبیو اظهار داشت که اگرچه واشنگتن برای بازگشت به عملیات‌های رزمی گسترده آماده نمی‌شود، اما در صورت حمله نخستِ ایران، همچنان امکان انجام حملات متقابل وجود دارد.
انتظار می‌رود این سیاست دست‌کم تا پس از انتخابات میان‌دوره‌ای حفظ شود؛ زمانی که ممکن است انجام یک عملیات نظامی دیگر مورد بررسی قرار گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70591" target="_blank">📅 01:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70590">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llf1RrPBx0xtk1KlaYdFbd2ERB-fbVPxR1H3174kkwQI6Wj3myFQL1br-_qi32KUhF6i-RuxhAO5_1GBWu1nnwTQL_9uYbQhfP3EG2Xr2GBbZIPK66Y4G-PTxeljO1AwhkYs3iaEPVNZ3UEd9i8wpHaoMdlvu0gq4vc6SpoPPk9QXed8QAm9vp8JUvq-41BaX9j5ztfa_jgMECdWh4IiJ-VBhXrByfXCDyOT9TtTYLwFm1745GlKSSOHk6S_rT4V-xj_CqvQ5BNe6drcDSXXQJ5NNvahnKucB2E4RE8TkS8spZnpcqalvQORYLGGCdW0HqpvmGE6-lWGDKBPa3cjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خروج یک هواپیما از باند فرودگاه مشهد
روابط عمومی فرودگاه مشهد: پرواز تهران به مشهد هواپیمایی سپهران هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70590" target="_blank">📅 00:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⏺
🎙
وزیر نیرو :
تا دو هفته دیگه شرایط آب هوایی به حالت عادی برمیگرده و خاموشی ها تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70589" target="_blank">📅 23:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1XZyFeK0_Gc4_u-BccM-E0cRyWzNfByCOuNHOmMpMCu1S3ZsItpZgAO2N-o-r4pX7QmSrt-YSY1juLR3mK0qyiJNHiN95qAgrJ87I_8qb91RI8-HMO6afGga02NcRn826gehGXmOmhBou6RuXtE0ycVjkwa2TT13-159XjDpyPDtdQ1zhiW-CzRdttwYAmw4kNcJlql13zHwUoFm4pzPDqhDefLXlaDUmOrOIA0MlFQn4Z1pULhiughSSRsAS6VpojvzTsuVdQ9-V1ShlfQaKR43GQQzbdtuZcpsXPs-s63WfeObgF2pwEaqcCBFlIYBp97VNbOuXvDhnmoiZqsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇴🇲
بیانیه مشترک ایران و عمان: دربارۀ چهارچوب ادارۀ تنگه هرمز گفت‌وگو کردیم
رایزنی وزرای امورخارجۀ ۲ کشور بر ازسرگیری دریانوردی ایمن در تنگۀ هرمز با حفظ حاکمیت خود متمرکز بود.
🗣️
چهارچوب پیشنهادی شامل این موارد بود:
ایجاد یک کریدور مشترک از طریق تنگۀ هرمز
اجرای پروژۀ مشترک برای مین‌زدایی از تنگه
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70588" target="_blank">📅 23:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70585">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=OBHRQuxX-Vg9YXO2CqZJuHK3AOL91RTV0vXKc3az9PQPQMw-etWbeyCaRemV25yGmZ9paFnAkGEEDwmxROx5REm_BFSBvArpLfr7tAxQkGxv74gqFD9TAFOUTigK75_qMNBNhLsy60UJzGs14P0BseCCWUCjKdoKtySMmv3Usw6CDo1k9b9mRMaMBZCra3vrdylrmWxOiJxHW2hfvJstSRAs2I08QjCVd-AT1hdt5AlJIDvpvBndXoNdmxsTmH5MtLWIfzo2InIoCPyIBittHeT9hWJJbT3IgDrTMtuDWvFxo3aUeQDD6QiIes0SzajaT8fOpG99u6NiT7crCZyS5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=OBHRQuxX-Vg9YXO2CqZJuHK3AOL91RTV0vXKc3az9PQPQMw-etWbeyCaRemV25yGmZ9paFnAkGEEDwmxROx5REm_BFSBvArpLfr7tAxQkGxv74gqFD9TAFOUTigK75_qMNBNhLsy60UJzGs14P0BseCCWUCjKdoKtySMmv3Usw6CDo1k9b9mRMaMBZCra3vrdylrmWxOiJxHW2hfvJstSRAs2I08QjCVd-AT1hdt5AlJIDvpvBndXoNdmxsTmH5MtLWIfzo2InIoCPyIBittHeT9hWJJbT3IgDrTMtuDWvFxo3aUeQDD6QiIes0SzajaT8fOpG99u6NiT7crCZyS5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به پالایشگاه نفت آفپسکی در منطقه کراسنودار روسیه حمله کردند.
در پی این حمله، آتش‌سوزی در پالایشگاه مشاهده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70585" target="_blank">📅 22:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70584">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=rgiuWkHanuAnki3Bl3-NVJMxWrDZ2OnuuqhB2suG9WMGpOzPEBoY3DQmJo6vt_z6dXm8XL41EJsThOZLc9D4JhCCiC3b3YuSMTeQkEyjqs-Pmx9lubSwZ7DK9Y6LxGST21yANguD59mZG0P6GXKCqQ7-SNB5dkT2_FzSI-DOjoemt2MzHLWwdgWqYadBFFyFLCUyHn02_nMfOW2LxEZQhLNXXn3_OWKWLxIbJTy950SyplG9j_NvtfgHtc5kZpHMgAlmKc5l9zVGRFhC4gavexcuf-NWVMxPJ_1DYBJNfhZEQhjQN3QKOcyJMfkfWdL6zyeINvywdsvtKq81wYoy1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=rgiuWkHanuAnki3Bl3-NVJMxWrDZ2OnuuqhB2suG9WMGpOzPEBoY3DQmJo6vt_z6dXm8XL41EJsThOZLc9D4JhCCiC3b3YuSMTeQkEyjqs-Pmx9lubSwZ7DK9Y6LxGST21yANguD59mZG0P6GXKCqQ7-SNB5dkT2_FzSI-DOjoemt2MzHLWwdgWqYadBFFyFLCUyHn02_nMfOW2LxEZQhLNXXn3_OWKWLxIbJTy950SyplG9j_NvtfgHtc5kZpHMgAlmKc5l9zVGRFhC4gavexcuf-NWVMxPJ_1DYBJNfhZEQhjQN3QKOcyJMfkfWdL6zyeINvywdsvtKq81wYoy1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مستر‌بیست(یوتیوبر معروف) یه چالش خفن اجرا کرده که باید خودش و دوستاش از دست 100 تا نیروی پلیس به مدت 12 ساعت فرار میکردن؛
برای اجرای این چالش ماه‌ها زمان صرف آماده‌سازی تله‌ها، دوربینا و مسیرهای مخفی شد و حتی یک شهر رو به‌صورت کامل اجاره کردن.
خود جیمی (مستر بیست) و دوستاش به مدت چندماه تو یه شهرک نظامی، آموزش‌های نظامی و امدادی دیدن و جالبی این موضوع اینه که مستر بیست برای خودش 50 تا بدل درست کرده بود تا پلیس‌هارو کصخل کنه.
این ویدیو یکی از پرهزینه‌ترین و پرچالش‌ترین ویدئوهای یوتیوب مستر بیست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70584" target="_blank">📅 21:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70583">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=gOQSUTH9iQrW1TWyrd-LKjqiu7Eol1Ol7xhRPp55eJpSLEyC2RTZaL9Q6jRovzRITDZdIxAJ9szywBZ-wRWNKMFsK4-o4EZuwAkWMCnkHBLOfcOAYB3GrKhlb7c3cHlf6ZP032nyk02jguYjT7udiW8sZimPMXEnCyCAAwAIa5_PjLTsWy7bZjRe293KLJrU4HwUsQFp-ZODDYS-gXx8abbUCNwVzztTDLa6P9AZup5VfYFJVzsG_ub7Jh284TElnEDps0Q1pEkPv2HndEf-tQEO50cZGPRNtTdshAz3ICVmRtqPzv7mx_datLTk4CP1zpStBzW_wZ0vD_O2HgF2mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=gOQSUTH9iQrW1TWyrd-LKjqiu7Eol1Ol7xhRPp55eJpSLEyC2RTZaL9Q6jRovzRITDZdIxAJ9szywBZ-wRWNKMFsK4-o4EZuwAkWMCnkHBLOfcOAYB3GrKhlb7c3cHlf6ZP032nyk02jguYjT7udiW8sZimPMXEnCyCAAwAIa5_PjLTsWy7bZjRe293KLJrU4HwUsQFp-ZODDYS-gXx8abbUCNwVzztTDLa6P9AZup5VfYFJVzsG_ub7Jh284TElnEDps0Q1pEkPv2HndEf-tQEO50cZGPRNtTdshAz3ICVmRtqPzv7mx_datLTk4CP1zpStBzW_wZ0vD_O2HgF2mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
سوال خبرنگار از شاهنشاه آریامهر:
فکر می‌کنید در کشور شما کدام‌یک تاثیر بیشتری روی زندگی مردم داره؟مذهب یا پادشاهی؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70583" target="_blank">📅 21:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70580">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOQfcwm3hxi1Jysl9CeNql_v6MVAhP-ufmBQzoI5xDYcQWSfmVy6nvIjtca-76EXulGEzTA8woyAjNShAPD9EWSp3BMZ4choarJchO7r-nbicM9XIS8p99pi5fnDLcL67DuT6D8xICEyKkabhh-6eyLxsiwi92V96SzvmKD3l2Yw40HILSSUDZIFiZACu9kAWUQFeIcGBga2LNHsogv-CpeIaaMwZjoZ6S_KHZBXv8qBHZOc4pEnIcoKxaV201Cp0Ggk0oqZvdkHZSaSq6g3xnkcFBkw2cMG604UHp_NT8pI32xOpl7uYmQnr1Nw4vsR7dTvwkHOuAZDbKibYw0SAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IkqAHA0UhwZDICp-i15HBieztfMPfC9RtxdwBiEAaSY1cbDbjcYz5Q109LHP4poFPWTcK_1iy4LfwpwJy2rQ9pBPpJ9_MkOyUDc6cKjTuIAJ9aJskMD1PCsHlG5KAdUaQ5gw9F8imfPby-8LoMQVgUDxEHUBwTY13j8xgZU7bQY9DsIOk0Fq-ltPscESBPS-JRHhHZkPYw7tpbNphXMVAhiMV546MSNir09qtNWEogJFf5rXb-UAG140D2SSi1r3tmTeUGqyoYSeQ5qeSLHwU3FmmoUPRVqNlGPIn24ZyhnZg37ShPR6TupPO1DihqCMp-ET0QZp_bXo-Cawx22yEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EybFZJXCsh-i7uzOddkcMJIfp9nmM9-PpjG4eP8k9OwQp7FcLdEMf2Oo4Pr3hR1wssmhUnxjhmdCN17-OeANwQN35WxNFNFEfBk0N9hPZGyobyerecqyrLPt30nGNtoRSnUKVwzBpKB5JJMHZkTAktEU6MPqET6IbycpyifuyAN5rj4m_pWCLMDUfHuLIajBIxPQwzLducvmb7VKejiov7JqR-KPOkQka7KtpbDjayNPuRcU1C3y6O-gSQDGRW6E5aOdQ8iiT4VSTMLRwC0u3QO7Yipr5LuHxALflhwg-mP6lMtCFBWZDL2wyQOW8LKJix02wozPzHZBZdNF19qlhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
〰️
🇺🇸
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
🔴
رهبری ایران به واقعیتی اذعان می‌کند که اکنون برای جهانیان آشکار است:
فشارها کارساز واقع شده‌اند.
🇮🇷
مسعود پزشکیان، رئیس‌جمهور ایران، ضمن اذعان به کمبودهای اقتصادی کشور، اظهار داشت: «جنگ باید بالاخره روزی به پایان برسد.»
🇮🇷
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر سخن گفت: «هر چقدر هم که قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و خبری از گردش مالی، رشد اقتصادی و تولید داخلی نباشد، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری همچنان به قطع تمامی شریان‌های حیاتی اقتصادی که این رژیم را سرپا نگه داشته‌اند، ادامه خواهد داد تا زمانی که تهران کاملاً منزوی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70580" target="_blank">📅 20:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70579">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BSU9BEGjTbg_IQGw2JbIXFRBmk5Yr_lua-BLKMaF5f6ASf2qrPxx57MDXHFJhvI4M_az1OBG0zmz5_Vj9fsgeOmeGXzheI-_yK_8NMv0tH5J1yngxKmgXyBVRaC84im8nDWC2be8NXJJzfPxrSKnTvVCIolA4G7R1iSsQXZFmLutoY9cF7y0BqlVSniFOhd0IxTEf_sXbBmylcxccnbbQQ5R0w65xWjKsQduLJ2tTbdlbjU-vuC1PhQOz3xWNYTlAg0iCY69dYM5CoEifAS9tA17PuZStBVfrnTUTcqZKuLoPacgO0k0F-awe8s08g35TR2oEx9f1iGKFHbYMBr4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
اکانت رسمی تلگرام در پلتفرم ایکس :
امروز به کراشت پیام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70579" target="_blank">📅 20:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70577">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=mlbHud4RZz-1lzrPAnfA1oY4H9uB4WQkmXc8tsY4nrsZCYPP3QtYSkWcTc_jpvcuV1H7Z5-2-5DG_ifWouCH4vzUghZVqGtBDu1ebXjkJi6DkRMNKQpx3o68ytiHncsEdyYskymW6u7qQzW7R3juhcAh92DWykgT1iKDa6WJ817WgUUILXZ5BAo6ORVDoQ8Z9woi2Yp1ENouM2OPeX9_kZ3GzRBiv9GtHm6whUjrhlFEaStFauon6GMlAsDoBr1Yc7ksMiayH4NLFkda8kW2FzAKNR9QaxHTGsP8pYN9khOiCN7uJMzS7NAWbBWPn6Hmx6LscZ63DGTToMyOF3hzLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=mlbHud4RZz-1lzrPAnfA1oY4H9uB4WQkmXc8tsY4nrsZCYPP3QtYSkWcTc_jpvcuV1H7Z5-2-5DG_ifWouCH4vzUghZVqGtBDu1ebXjkJi6DkRMNKQpx3o68ytiHncsEdyYskymW6u7qQzW7R3juhcAh92DWykgT1iKDa6WJ817WgUUILXZ5BAo6ORVDoQ8Z9woi2Yp1ENouM2OPeX9_kZ3GzRBiv9GtHm6whUjrhlFEaStFauon6GMlAsDoBr1Yc7ksMiayH4NLFkda8kW2FzAKNR9QaxHTGsP8pYN9khOiCN7uJMzS7NAWbBWPn6Hmx6LscZ63DGTToMyOF3hzLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر ۱۶ ساله رونالدو و دوست دختر خوشگلش:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70577" target="_blank">📅 19:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70576">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=UZkAdCGV-E0Cwq7b0WPr80-hzcFpemq6clrhkD5CvUwgQP7wroV2pNksg5EWCeqPgRWzrT3MpolDhjb-NjBcjubWGXrrunbc2mqaFCkr08W1F3Y8HM5eInnd5fslbUvnWm4Lh7CEcP55JtAyD3sk9bqwiYgrxUpgfQtdOVc4OCTMUB5rkdvs5ukJ2sUGkK5xnNF59iL53rh_R2AQs2kQ5OeKb8k0WuvxPATjfei4m2WQo5x3-Th-PyTj45NmI0dud-kBE6ljwNNX8BWeVmZtK-wt-0OkjTZ_CC0qqNT_4GMJ1fj480h3Ub_EJtJ5zBXxTt_7NVjJGqv2jdJI_RdjFg0t5ny_lg26UQIj6jFQ6Ccu0IGmz3HKTh2wM5qYmeQosiaM2JtkbXx0SdSMYj_BGy7o6eH46JrSTICebUlLpYPRsmecdtO15U54G6wDV28U16r1ZfZhz4WCq_EfAC_mb6uSyIF9GN8zs3qf4BINpEXYF-nJQhPRMZjHpPdxGVxIgiZ4K5_0Dqu9wI8c3DycyI1cxzS4ULRJBFTRCIPxWmywMMinZVbgHzMBkHy0pmkFpCbSMsbIIS8C4JG_i7tQVajupZdMsntFIgN8_g2I2xIQRmKg-T6GQc-elJYqCdkcinTlAaFjqk-KLBSqBFGyBsmV-wrb0VEKmZ93-XPS58Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=UZkAdCGV-E0Cwq7b0WPr80-hzcFpemq6clrhkD5CvUwgQP7wroV2pNksg5EWCeqPgRWzrT3MpolDhjb-NjBcjubWGXrrunbc2mqaFCkr08W1F3Y8HM5eInnd5fslbUvnWm4Lh7CEcP55JtAyD3sk9bqwiYgrxUpgfQtdOVc4OCTMUB5rkdvs5ukJ2sUGkK5xnNF59iL53rh_R2AQs2kQ5OeKb8k0WuvxPATjfei4m2WQo5x3-Th-PyTj45NmI0dud-kBE6ljwNNX8BWeVmZtK-wt-0OkjTZ_CC0qqNT_4GMJ1fj480h3Ub_EJtJ5zBXxTt_7NVjJGqv2jdJI_RdjFg0t5ny_lg26UQIj6jFQ6Ccu0IGmz3HKTh2wM5qYmeQosiaM2JtkbXx0SdSMYj_BGy7o6eH46JrSTICebUlLpYPRsmecdtO15U54G6wDV28U16r1ZfZhz4WCq_EfAC_mb6uSyIF9GN8zs3qf4BINpEXYF-nJQhPRMZjHpPdxGVxIgiZ4K5_0Dqu9wI8c3DycyI1cxzS4ULRJBFTRCIPxWmywMMinZVbgHzMBkHy0pmkFpCbSMsbIIS8C4JG_i7tQVajupZdMsntFIgN8_g2I2xIQRmKg-T6GQc-elJYqCdkcinTlAaFjqk-KLBSqBFGyBsmV-wrb0VEKmZ93-XPS58Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صادق خرازی:
به آمریکا در افغانستان کمک کردم و حتی فرودگاه در اختیارشان گذاشتیم اما جرج بوش ایران را محور شرارت نامید!
بیشترین خدمات را به آمریکایی ها دادیم و حتی خون دادیم
این نشان میدهد یک جایی در پشت پرده محاسبات دو کشور نمیخواهد رابطه ایران و آمریکا به جایی برسد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70576" target="_blank">📅 18:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70575">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=JkCo_xWipl9nN2m2icdDSYtCPlsar-SIgnTpF_EcABT8OMAxMg-AbsnScR5y2Ywet6voGVUkbW0KA2pNge96vSTBGJ2VVxumaoi35tNrWcHGOgSPg2wpyLHdA6xtPaJqv48e1HJezLkj3rppMA9beSN0kKSkEKGBn1rUWS4gy7QQ4wjMNyumyZw_cTwvp2aU_0cGr7OqIxPH_gX8vUfd_tSoxHqNoE8KmEYw7x6xaFXBAneF4lbSBqIm0-_R8dLe3Z0Rc-xlJLPMMqdeti5htdf-2rLjhfhJyBZyLcAD5ABl2B_ppcAXMdxKbrG_hIVdYqDVxCk4d7si_LfAk4WlCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=JkCo_xWipl9nN2m2icdDSYtCPlsar-SIgnTpF_EcABT8OMAxMg-AbsnScR5y2Ywet6voGVUkbW0KA2pNge96vSTBGJ2VVxumaoi35tNrWcHGOgSPg2wpyLHdA6xtPaJqv48e1HJezLkj3rppMA9beSN0kKSkEKGBn1rUWS4gy7QQ4wjMNyumyZw_cTwvp2aU_0cGr7OqIxPH_gX8vUfd_tSoxHqNoE8KmEYw7x6xaFXBAneF4lbSBqIm0-_R8dLe3Z0Rc-xlJLPMMqdeti5htdf-2rLjhfhJyBZyLcAD5ABl2B_ppcAXMdxKbrG_hIVdYqDVxCk4d7si_LfAk4WlCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
نگاه هویدا به یکی از بی‌شعورترین و بی‌سوادترین مخلوقات زمین
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70575" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70574">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70574" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70573">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6k5oZbGYs8L-HxLZwQw2UK1PJxOUPtOAb-XTQyP_HyTtWWFwOM2fjKwlMtfnEHpi8c56DJ-IKSAtBiaCkKZF3ODx8CL3gOTuM_AbsfIY6xemAMlzDNM_R5RKQe9TIatrCSFhLz6MjYB3DLx98jt-4ugdZXPjBLpMEXHjuLV5L5CBDP4fWJvoB1KlvKvK2gK0hUR7gVK57WLHBetU11-RTYXljmU94kFlhIFxeaf1tRGb_HubOjzBY4Aq4oJYOayNBb1JiehdohVHwwPiUmpkjLsSnZwyy6thtrgGonLY8NAnRO5Kcu8TDYXUVtWY28ki0YAUmltLPgHNutoESvOyW_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6k5oZbGYs8L-HxLZwQw2UK1PJxOUPtOAb-XTQyP_HyTtWWFwOM2fjKwlMtfnEHpi8c56DJ-IKSAtBiaCkKZF3ODx8CL3gOTuM_AbsfIY6xemAMlzDNM_R5RKQe9TIatrCSFhLz6MjYB3DLx98jt-4ugdZXPjBLpMEXHjuLV5L5CBDP4fWJvoB1KlvKvK2gK0hUR7gVK57WLHBetU11-RTYXljmU94kFlhIFxeaf1tRGb_HubOjzBY4Aq4oJYOayNBb1JiehdohVHwwPiUmpkjLsSnZwyy6thtrgGonLY8NAnRO5Kcu8TDYXUVtWY28ki0YAUmltLPgHNutoESvOyW_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g3
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70573" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBdZNPI-5zoVPj8tKyy_w22tChaSaWx3gr8OC1oIGP2w0WX_0sjshE-LhyLskH03Jw2gMTES-lqjxcnLd1tc3OX3eNWEq_bY9YUhjHJ14IAgwvx0hWiTeVYsJTdMj06DPCEZlOgwB_kCj3nUY2Ksjf8Ucx-_Fg8ez6t1XHPx9PF20fX5G5-X88xU1Y1UlSplrLiZMOTYyjCZslwOYJsQ4YJ7ggUp18g7J6z0auJ_8XsKZpYxSChFPc9Lq0Vq6O6XcUe5cFJVHFTCzhUxlMtIzC22kwiX8w7gnjwLmsgBtd2a5wSzmbXCK5FKsFZCSdrLU1CNfKu86qeTJrpBIS1yrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
نیروی دریایی ایالات متحده به من اطلاع داده است که تمام مین‌ها از داخل آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدیدی را در آن کار بگذارد، فوراً و به طور سیستماتیک منهدم خواهد شد.
ما از طریق نیروی فضایی، هر اینچ مربع از تنگه را زیر نظر داریم، همانطور که در مورد کوه پیکاکس و سه سایت هسته‌ای دیگر که قبلاً نابود شده‌اند نیز همین کار را می‌کنیم.
سیاست عدم تحمل در مورد مین‌گذاری با تمام قوا و به طور مؤثر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70572" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=Gf0sXCozMaos05o_wTrhdgrE1DHLlS7AD_ST9rOQ3o30zWWEYSKVstVdrGFqlzcwBFFaCCdFQpc3z58SR6zKNd2kyBJroQSyFwhenz_O5Fm6rBm8r3Wdy3ycp1FMIAQdUS9SajLaEFvIZdY88NiBPQTvUuutQNos-M6-IaP4wcL8v8cYdydZvo2caxxqwk-_a-rjha7VOph4X1EKjgtWs3M-FANqxhb9L0c7fn6o13IsgMQ6U1vCQhMNJO5fULwy-HcTdWIPsAQi2IizrbT7y9K2dV6uxZe-E3Pe3TcXAIh34ncAi7BWNkrNKKF5cwDXf6cD9LUb9W0bn5g54Ziadg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=Gf0sXCozMaos05o_wTrhdgrE1DHLlS7AD_ST9rOQ3o30zWWEYSKVstVdrGFqlzcwBFFaCCdFQpc3z58SR6zKNd2kyBJroQSyFwhenz_O5Fm6rBm8r3Wdy3ycp1FMIAQdUS9SajLaEFvIZdY88NiBPQTvUuutQNos-M6-IaP4wcL8v8cYdydZvo2caxxqwk-_a-rjha7VOph4X1EKjgtWs3M-FANqxhb9L0c7fn6o13IsgMQ6U1vCQhMNJO5fULwy-HcTdWIPsAQi2IizrbT7y9K2dV6uxZe-E3Pe3TcXAIh34ncAi7BWNkrNKKF5cwDXf6cD9LUb9W0bn5g54Ziadg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید باورتون نشه ولی ایشون بخاطر اینکه آلت تناسلی بزرگی که داره، گریه میکنه! میگه تا میخوام با دخترا رابطه برقرار کنم، جیغ میزنن وای هیولا، چه مار بزرگی و فرار میکنن
😢
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70571" target="_blank">📅 17:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70570">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb0dbc493.mp4?token=vSL6hiSCGIQC_6trZDSKLltosm2QzklNTwUqBxPMOmoPwEjYjacxdDRtXXnZ-Hxa8NGXSNZq1rB3Pu95ArqxuIPUDKcLeCHOvYyxqB7g5FeNGmhsJVfv5qAej46ENnp3zoEYcgwVAAHdxiq35VJbi3zxnuNGVjsLZtu2Rxv9XlxfiZIh3JcqVBof8xrwjjeFreymWqQnM3uGCYkP5K7J9ZY2cQXNWIv3ADJ1l4Y_LwmyD8Nhh1D46Qxw9pw8jCVWMRTJF2GeuHPaZx-f9sPsJCb3L2gJ0Oe1CGUXxXQPtNibVrvl_AfSjdQV7xKkbtnilgT52M53_M800OAaRUKXPzq4BcZGncdXXC6kzLHcgHPes6qeWks5JKcXbVeB0NARPDS02rMgZ-shwvaqkbOUz3IA8oG7JfCeXG7FSbGgIM8k1LhGHrauiPwyCvyGzM3IAJTi1H_CPXk_ydeI5XAloqy2WmU_3B_JqPT1BN10cqseqV8ma2X4qYEkK_68_ZYL2Y45OF5BhrTtjNVzGgqz_VfrfMd5w4mKmmUH-QvTUjKEy0i4Pll5uF1a2glVP0Ib6Nkf-9iB38_LlIMBVJcgpOn9Kv9UcJT9FQVx8IO4EBmqtZqpUYsKkxYhrTeeWgb7FLTRoWbYo4lpxAqQjasKmFsU5-i55qVkrwbUcCN48Ss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb0dbc493.mp4?token=vSL6hiSCGIQC_6trZDSKLltosm2QzklNTwUqBxPMOmoPwEjYjacxdDRtXXnZ-Hxa8NGXSNZq1rB3Pu95ArqxuIPUDKcLeCHOvYyxqB7g5FeNGmhsJVfv5qAej46ENnp3zoEYcgwVAAHdxiq35VJbi3zxnuNGVjsLZtu2Rxv9XlxfiZIh3JcqVBof8xrwjjeFreymWqQnM3uGCYkP5K7J9ZY2cQXNWIv3ADJ1l4Y_LwmyD8Nhh1D46Qxw9pw8jCVWMRTJF2GeuHPaZx-f9sPsJCb3L2gJ0Oe1CGUXxXQPtNibVrvl_AfSjdQV7xKkbtnilgT52M53_M800OAaRUKXPzq4BcZGncdXXC6kzLHcgHPes6qeWks5JKcXbVeB0NARPDS02rMgZ-shwvaqkbOUz3IA8oG7JfCeXG7FSbGgIM8k1LhGHrauiPwyCvyGzM3IAJTi1H_CPXk_ydeI5XAloqy2WmU_3B_JqPT1BN10cqseqV8ma2X4qYEkK_68_ZYL2Y45OF5BhrTtjNVzGgqz_VfrfMd5w4mKmmUH-QvTUjKEy0i4Pll5uF1a2glVP0Ib6Nkf-9iB38_LlIMBVJcgpOn9Kv9UcJT9FQVx8IO4EBmqtZqpUYsKkxYhrTeeWgb7FLTRoWbYo4lpxAqQjasKmFsU5-i55qVkrwbUcCN48Ss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ارزش پول مملکت رقابت شدیدی با گوه داره؛
یه مادربزرگی گوشی نوه‌ش خراب میشه و میاد این پولارو میده به طرف که گوشی جدید واسه نوه خودش بخره.
به گفته‌ی خودش این پولا حاصل 6,7 سال پس‌اندازه. از دو هزاری بگیر تا ده هزاری جمع کرده که تا موقع نیاز ازشون استفاده کنه.
حالا طرف اومده پولا شمرده و مبلغی که به دست اومده خیلی جالبه‌:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70570" target="_blank">📅 17:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70569">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439a914edd.mp4?token=sxWrjBavPqSjlhP9tqyFe34pZD8cie3JSYNfspXzhO_abd1QmFtBfMWRrFYvJ9wCz-iYCHdT6Jkp3j114XVSiMc6ucQnMiop_iW4AOAlC_fzAfMjAgZvX11ftCw6mCdnd4fpQ7DB7HPsIXhFb-sSeNXfUn5yxJGH8pi6RS7ewTPoef-zVGTQU0opWTTXzYZDHhNFaaCTBr-sbVZ2P5O2vLqhfIlV7ww96V1llzhbqjt3Hhvd4BkjluyUqRnWKMoxboYbyMy4sfUW0WzPKxXMmo0JoQRk2aq__frXUlDjXlC2cL8Z2eEx2CVBdVkrdMGGk11wMMvYLpjhQb7pHW2Olg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439a914edd.mp4?token=sxWrjBavPqSjlhP9tqyFe34pZD8cie3JSYNfspXzhO_abd1QmFtBfMWRrFYvJ9wCz-iYCHdT6Jkp3j114XVSiMc6ucQnMiop_iW4AOAlC_fzAfMjAgZvX11ftCw6mCdnd4fpQ7DB7HPsIXhFb-sSeNXfUn5yxJGH8pi6RS7ewTPoef-zVGTQU0opWTTXzYZDHhNFaaCTBr-sbVZ2P5O2vLqhfIlV7ww96V1llzhbqjt3Hhvd4BkjluyUqRnWKMoxboYbyMy4sfUW0WzPKxXMmo0JoQRk2aq__frXUlDjXlC2cL8Z2eEx2CVBdVkrdMGGk11wMMvYLpjhQb7pHW2Olg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70569" target="_blank">📅 16:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3XNRD3DZN6LuvAnVckzk8KWw8wH4gtkQRBY-_kaQg1BiSt0E7qsSdxPY3rHpOZPd5OrrJsBubJ2ftdgI05zklu95ruXEnWED4PJV9dk1VUiO6szRfn7k3vOQGGTts05W_AgY2PtP7SYRhtmIjsgcpMYaVGAf7WHyE4hxeDu6L4Ig_OzdYvmRQNJvf0qvuiJEcpY0dDcglkrwbj9k46qsZeztaflAES5GsZkJalERgwhJRmlPe0eRuu0YvQKWuowIzB_nfSTI5CULBrYzuiV1zQL5GV_tyabUI5HCZtr4RMzyb4hvut97ZLCRHNO-djSiSNX-72aJ5VJsyycXrEx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGkW1GOFpfFEFRVgqP9fwULz-7NnEtDcvg_dhHlBqE9OI4TXuaoIr3axXglx7TTjlpuFIrmXZq56Y1Docf495v83p3FHVKq8I1oierZKu4093hdc7MUPFMh5ZbG2Fw_rkd-FW2a6wfwa3xwm9NLctFjkW7waPJ4sXuM7H_Np536asKy9fheT3C5KkRcQ3sqvLa4qE7gqEJGIYfLmxK2TTvKLbNbtJVEzW2UeJrIZljQJ_9Ppc1cBAS3HV9aiI6Od6mvubWzzaRejMuaOh4Fg_CyV5PZK_ayxrEbRhQnRc9uh088nUHunjUGouJopuKL-LEK944uAgUy_X4nocJlxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3MbZ6GXtOLx7BPkjtxp4b7C9IxIZQsShC9nEB7MxTx4QxnDDszOWXrOrv92TYY4XZGvRten8cdHXDzuCWmoMFl4YpCdJDKNyOxxBis6X7QJPFoIkzs7Ll7XqfzvjRFsbdIxzgBLKHd30H84Ria7vbKwWY0-KkK1nlj5kBRUaDfdV6ZjykbubMNzzqpdPES-mUxpASXitLDQvRzqfrJcfoFG-_qYxwTAdQE0IWOP_5gq1ipumliEKiaJ04YYQaQvg-3morAS5cklxQXqozbkirgp75ZXV7Oc7E98W47Siruj53x7wdCxLsrsSXnm94lI27CPg4qNIUoy5_61fBB6dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇴🇲
🇮🇷
وزیر امور خارجه عمان، بدر البوسعیدی، با عباس عراقچی در تهران دیدار و گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70566" target="_blank">📅 15:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKYR7v5M_ZFu4dPaz-FWuqKPhXZ-iqBXkdazYLA_Vrsq3J0O_jYxQtGZ9YYn8eD6wQdIEZpSzVM--8fNbNIXQMKP4F5DrQn_g-GDdjUrleM8kuJcZ8KveAvd3Jw-rjeBbdUl906DOoEx-ngi59_IhhVgu45aKtY093auytq1YdWdXBhJnrnis56aTrb7BBDgAeffpdli1G7i3-sKAf9A19rSNQ4MohIAEfHL_rcS3havS-ScYEO03tF5s6Fp5GICqyBdEf2vlhcqCcxzoeI6tPBxqDXyzhRJkiO7n_WNQros65StvOQrnwSlJGDYeU9GAzAlWTiClvwcV1-eLRlIRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
بانک ملی ایران در سال ۲۰۱۸ به دلیل حمایت از تروریسم توسط وزارت خزانه‌داری آمریکا تحریم شد، با این حال همچنان در سراسر جهان شعبه دارد. اسکات بسنت (SecScottBessent) وزیر خزانه‌داری آمریکا به‌تازگی اعلام کرد که تمامی این شعب باید تعطیل شوند.
🚫
مکان شعب بانک ملی به شرح زیر است:
۱. امارات متحده عربی — ۷ شعبه (دبی [۲ شعبه]، شارجه، رأس‌الخیمه، فجیره، ابوظبی، العین)
۲. عراق — ۳ شعبه (بغداد، نجف، بصره)
۳. عمان — ۱ شعبه (مسقط)
۴. آذربایجان — ۱ شعبه (باکو)
۵. آلمان — ۱ شعبه (هامبورگ)
۶. فرانسه — ۱ شعبه (پاریس)
🚫
بانک‌های تابعه / سرمایه‌گذاری مشترک (در ۴ حوزه قضایی)
۷. بریتانیا — بانک ملی پی‌ال‌سی (لندن)
۸. هنگ‌کنگ — شعبه بانک ملی پی‌ال‌سی
۹. روسیه — بانک میر بیزینس (مسکو، کازان، آستراخان)
۱۰. افغانستان — بانک آرین (کابل؛ سرمایه‌گذاری مشترک با بانک صادرات؛ وضعیت تأییدنشده)
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70565" target="_blank">📅 15:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzpDYyvvS_o60uf9xqUS5AlhMTpCLwNIOx-KabdnPftXqNwB5wAOlfJxBt6AmMFKPP2HQNipzzWmLe2DkbXKNGw2HUuW3CaLIorDuYt5oYVCBDWd7DtlV44w4tvOATZBXFB6HqPqjdajd7Iu3PuBcGQ4jLNkhc5kaYIGjwxs9ucXcC58hz4tQkngU_ddi2olqp0LhTQ8EXb2Dwj_FuWpMGv04i_CBviSuOydxyvvG2ZpkZWe5cUO9t9L2I3sA8EjmlF6B4YGU-tqZTtbcmhI38DXU5kj9_SUB-Ye1JxGhKepUYssDXnUvdINzRGiUNdi_NkOkQuD_xE5jNlCus_TQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی ایران که در حال فروپاشی است، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را — حتی زمانی که مشغول اعتراض نیستند — با شدتی بی‌سابقه به قتل می‌رساند. این یک بحران انسانی با ابعادی عظیم است و باید همین حالا متوقف شود. رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70564" target="_blank">📅 14:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=pCMgWN00XJZ3whTIuAMt-HphdQamWejzZLLlC4097VRFdOsJ8vij6itiEXyJP50RWB1LnHLoDrbvz03KZit7YPrQJMiWYt_8Hm15SeT7fYYlxbB1e35vF6LnB4TX-yR9rUD0D0yQL0OYmXMXB5r-XsJXskl1nmPCMgd-2VVJwz61L9eTq4S6hG1VU_kRszQDIK9WBK-hiQ4L_XSvOXDLbnwQ45mcLh6NeSe_b_5PtofLenzwBhkwyewHlBNMf-6kXkvTG6_WFfs8N6nk4BmRdCvQE-vfW1hreb4Vjp4yD5MDot7egc8CRHOHkV5bMvn6BQgoW91sXx5E-NvIJiTMO3LUkKLAsstnPiuTbzFTkyxbTwiKJjNvCPGJ5OBJLK4S0nkco7zfCPCppIolrlX55ZwxGpF9Md5XEOg4HJMFz43uuwlZaEKAGGQo-gwaL-8M8mteNTuqC7joIRJxBAK3M7wZXjjYaU350TALy8SVu28vkyVxm32TcVThhScKviyF1FzZ-g_hadI3posfzCbvBw7AmeyY5DbqiKlITQD7rRD51eg5t-M1NXQy4v4_2bWJ5qkPzLOTcXhGI735OJfCsUrxogyJ5QAE8SVcaw2itoP2y221QzdEO6dP4UzRiSM5U2lU0sgWWniXpkoKlhNjjjWSM4ilaCy_9AGhWYo2VVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=pCMgWN00XJZ3whTIuAMt-HphdQamWejzZLLlC4097VRFdOsJ8vij6itiEXyJP50RWB1LnHLoDrbvz03KZit7YPrQJMiWYt_8Hm15SeT7fYYlxbB1e35vF6LnB4TX-yR9rUD0D0yQL0OYmXMXB5r-XsJXskl1nmPCMgd-2VVJwz61L9eTq4S6hG1VU_kRszQDIK9WBK-hiQ4L_XSvOXDLbnwQ45mcLh6NeSe_b_5PtofLenzwBhkwyewHlBNMf-6kXkvTG6_WFfs8N6nk4BmRdCvQE-vfW1hreb4Vjp4yD5MDot7egc8CRHOHkV5bMvn6BQgoW91sXx5E-NvIJiTMO3LUkKLAsstnPiuTbzFTkyxbTwiKJjNvCPGJ5OBJLK4S0nkco7zfCPCppIolrlX55ZwxGpF9Md5XEOg4HJMFz43uuwlZaEKAGGQo-gwaL-8M8mteNTuqC7joIRJxBAK3M7wZXjjYaU350TALy8SVu28vkyVxm32TcVThhScKviyF1FzZ-g_hadI3posfzCbvBw7AmeyY5DbqiKlITQD7rRD51eg5t-M1NXQy4v4_2bWJ5qkPzLOTcXhGI735OJfCsUrxogyJ5QAE8SVcaw2itoP2y221QzdEO6dP4UzRiSM5U2lU0sgWWniXpkoKlhNjjjWSM4ilaCy_9AGhWYo2VVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر اقتصاد:
تفاهم‌نامۀ اسلام‌آباد روی کاغذ نکات مثبتی برای ما داشت اما اسرائیل و تندروهای آمریکا نتوانستند آن را تحمل کنند
امید داریم همان تفاهم‌نامه یا بهتر از آن احیا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70563" target="_blank">📅 14:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHTXCl7DUt7-t8aG_zDb32vzvR5Fga23Mq6t8y6g3HUkgDUV27w5vtVgw0oGSYYnc6p3CmnM8RoN1U7uhIARZUTZz_V0txQQp014zHGMAa30nslW99EujEz0r8sxKqjCj4Ktf4sJtSqGcbzQDjfiOe6Jcl9e3jJPYueWVp-ebb2sSU8E6cXexC8a0z22VLm700iN23Igsdony99iU2wUfSds_V4Icx1NsvDReE9EgJNXUOYxOZsWT3s2dgW-oc2G9qKsr7OIbR7xy6soTNfJ4xm_z9WOj5MYnv2qveGY5S7H1l0oAVbqwMg5-ETmRJkJrKb4m6utUrpYGxVkGAwYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
حساب اسرائیل به فارسی:
درباره ماجرای دایناسور خراسان، احتمالا فردا امام جمعه مشهد می‌گوید: «این دایناسور از برکات نظام و نشانه پایداری ما از عصر تیرانوزاروس تا کنون است!»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70562" target="_blank">📅 13:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
📰
اکسیوس:۵ نشونه فروپاشی اقتصاد ایران زیر فشارهای ترامپ:
⚪️
سقوط ریال؛ دلار به حدود ۲۰۲ هزار تومن رسیده
⚪️
تورم شدید؛ پیش‌بینی تورم ۲۰۲۶ به حدود ۶۹٪ رسیده.
⚪️
فشار معیشتی؛ گرونی و افت ارزش پول، خرید مایحتاج روزمره رو برای مردم سخت‌تر کرده.
⚪️
سقوط صادرات نفت؛ محاصره و فشار آمریکا درآمد نفتی ایران رو به‌شدت کاهش داده.
⚪️
رکود و بیکاری؛ فعالیت اقتصادی و اشتغال افت کرده و پیش‌بینی میشه اقتصاد ایران امسال حدود ۵.۴٪ کوچک‌تر بشه.
با این حال تهران قصد تسلیم شدن نداره و ممکنه دست به اقدام نظامی بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70561" target="_blank">📅 13:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a518ac30e.mp4?token=PK41yVo-IrMkUblIFwPwBOxhgosLSrof7TOwU-N-kVfzfgBsSBd4kZ9S4oBg7m1jtGbgh36PNVhtaiKUkyAYRDnefRDfHfmnFPVWjzZkzrDyi2UqGIiGqResD2zZ-a8qViPEj7GgQdEpCqB-Dq5nogYz1VbtGzfZOGoi8k3_kEtnAxLFKRwdoqupIX-O03jTB3OLUhzkmjl_8BltWg4PUFquGA-fQ2jFG6O2laOZ1OkQ5W7k0qqw1lUdhRd1uB3RCTn0uZQyOs05AYiiCxVBAun4aqkirzQ4KNwP91G-jRl09aGBQYtPx-JTSTGO4idreMCSSc03arlR6EhTz8ngkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a518ac30e.mp4?token=PK41yVo-IrMkUblIFwPwBOxhgosLSrof7TOwU-N-kVfzfgBsSBd4kZ9S4oBg7m1jtGbgh36PNVhtaiKUkyAYRDnefRDfHfmnFPVWjzZkzrDyi2UqGIiGqResD2zZ-a8qViPEj7GgQdEpCqB-Dq5nogYz1VbtGzfZOGoi8k3_kEtnAxLFKRwdoqupIX-O03jTB3OLUhzkmjl_8BltWg4PUFquGA-fQ2jFG6O2laOZ1OkQ5W7k0qqw1lUdhRd1uB3RCTn0uZQyOs05AYiiCxVBAun4aqkirzQ4KNwP91G-jRl09aGBQYtPx-JTSTGO4idreMCSSc03arlR6EhTz8ngkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما یه ویدیوی جدید با هوش مصنوعی درباره پسر ترامپ ساخته و اونو تهدید به ترور کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70560" target="_blank">📅 12:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70559">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/377055b126.mp4?token=Sp9Y4Q1Jszwq1mMZiWm7a9p9ip1brxEhSihBSiM7kLZ9WFzZX0rVcuY5A9nsU4_mxPCaqFJ-g9JNrtnYtTZOuc7mATCVJuaTSpagbrQf3Z-1QScUbXj_mB54E-6RXHrSx7lDseUSg-hgj4tw5j2EEk8w_7nCKBCYUj2j9q2uG-USbxCG7DJ7fRZz_w4AjMdXcER3ckdePhEIOQNJ0YvUyc9jcJnlmq4FZHhu_vgf3nXDRMVxKdiPTXItGHvjgXIEVhCpjQxaDEKGJtbYYOlkf28sP6i5P0fwLed2LjGii8CDE9RZGNqK-AieW3iBJ-KJx8BsYOtLzGDJNXCQMJ9Lcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/377055b126.mp4?token=Sp9Y4Q1Jszwq1mMZiWm7a9p9ip1brxEhSihBSiM7kLZ9WFzZX0rVcuY5A9nsU4_mxPCaqFJ-g9JNrtnYtTZOuc7mATCVJuaTSpagbrQf3Z-1QScUbXj_mB54E-6RXHrSx7lDseUSg-hgj4tw5j2EEk8w_7nCKBCYUj2j9q2uG-USbxCG7DJ7fRZz_w4AjMdXcER3ckdePhEIOQNJ0YvUyc9jcJnlmq4FZHhu_vgf3nXDRMVxKdiPTXItGHvjgXIEVhCpjQxaDEKGJtbYYOlkf28sP6i5P0fwLed2LjGii8CDE9RZGNqK-AieW3iBJ-KJx8BsYOtLzGDJNXCQMJ9Lcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این شما و این برج زنبق واقع در منطقه ۱ تهران:
۲۸۰۰ متر پارک و فضای سبز اختصاصی.
هلیپد برای هلیکوپترِ اختصاصی شما.
بیلیارد، سینما، سالن اسکواش، باشگاه، مجموعه آبی، کنسول PS5 و سالن ماساژ.
اتاق بازی کودکان، فضای اختصاصی برای جلسات کاری، غذاخوری و...
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70559" target="_blank">📅 12:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70558">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e23f896bb9.mp4?token=ZVAzxLa2syOmcNQ0Nda_rcMVyryzLsIxr_MbXyp9lg_79M-IepMO3_uwtFPfqu9tkQUtEyUSCmKV8vdEA6kT0sOwP_rgh-Q8mC5psYHQUcNzE9RchHVwCB4ECo33Am-Y-QRX6YDN46oF_vgxTNtfAjXsrwvRtXm5f8-OdbVqbovfcNvj1JZ5LkHc_9EFGvNc3kjrZFrWRToQWGEPnE2PY9S_BTsvsewrXGpFAA6zlO-si-CNB9L4kWq0KaJk0hjCyl8jrOHnLtQv1b9n8HDIUQ5TLkCntmSfs5zuGL20hDPcpEAl65wkTGC0Z8OA2FO5VzaVsyeTDetmYcUsuAJJxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e23f896bb9.mp4?token=ZVAzxLa2syOmcNQ0Nda_rcMVyryzLsIxr_MbXyp9lg_79M-IepMO3_uwtFPfqu9tkQUtEyUSCmKV8vdEA6kT0sOwP_rgh-Q8mC5psYHQUcNzE9RchHVwCB4ECo33Am-Y-QRX6YDN46oF_vgxTNtfAjXsrwvRtXm5f8-OdbVqbovfcNvj1JZ5LkHc_9EFGvNc3kjrZFrWRToQWGEPnE2PY9S_BTsvsewrXGpFAA6zlO-si-CNB9L4kWq0KaJk0hjCyl8jrOHnLtQv1b9n8HDIUQ5TLkCntmSfs5zuGL20hDPcpEAl65wkTGC0Z8OA2FO5VzaVsyeTDetmYcUsuAJJxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه دختر برای پارتنرش شرط گذاشته که هر بار دعوا کردیم، برای اینکه باهات آشتی کنم، باید برام طلا و سکه بخری و پول بدی.
بعد از یه مدت رابطه، این صحنه خلق شده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70558" target="_blank">📅 11:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70557">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWAnT_LWC0mXKVSYUehPCnmZIoRHvs8PhqHUh28FsOVNnrrbTTr87fSoYoEzar1DvbSqt1V5ott1t0A6edcrzIY6U502zu0l6Q92hQUk1y6wgnUQs1luWZog3LSwAPA79npgC5zbti4lyq16KWOcyWCtjGRgeRuUY8mhqaq7wmMowpb0zClN2m_M5ZmYRxhH2hpxnP-vkkyDznE7Au4tr1NHSm41HnQ-juqY0K8ArKA1y0W88OGGVndV0EC2UVP8fmZsqt-F3EwggDtwFBc8pIdxEnpKyqYFLOTpnebIYVQmVVdl9TXI6bp9iDsm6ATdmOc_lIZYmcaLIvsCgWNhig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی از زمان دلار ۳٠ تومن تا امروز که هر دلار بیش از ۲٠٠ تومن رد کرده به آینده اقتصاد خوشیبینه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70557" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70554">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=c36k8j_ME-EC4x7OdVGDyqutsn7qOfoXYvVGToMKmdsnp66QYMPOpiBkon1C5dNuepy6zNj5sDZ4WtPQe-Us60WS8o85W8NMOOeMmT8K3GgVyBWJ4G0PI35Zw4keRUF_9I1HN2M0GlPI8lLo0YhyRg38aod37mJdJ2flm_WXkbDEfQ79u9tN6oiiYzOJVFyWdq_3fYFB5L03ePnvJeIHG73sdfM0S_UMXOJLV2ZYQjYve7zB63_IKF9I-WxOsvzYJCr1FRb7OupuXgzeQfAohuFQgqIJIiB_wG1pPaQrv03vdCbvZMddC2zt23rqz76xj4iH2bme0cJyj2ONZmIWNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=c36k8j_ME-EC4x7OdVGDyqutsn7qOfoXYvVGToMKmdsnp66QYMPOpiBkon1C5dNuepy6zNj5sDZ4WtPQe-Us60WS8o85W8NMOOeMmT8K3GgVyBWJ4G0PI35Zw4keRUF_9I1HN2M0GlPI8lLo0YhyRg38aod37mJdJ2flm_WXkbDEfQ79u9tN6oiiYzOJVFyWdq_3fYFB5L03ePnvJeIHG73sdfM0S_UMXOJLV2ZYQjYve7zB63_IKF9I-WxOsvzYJCr1FRb7OupuXgzeQfAohuFQgqIJIiB_wG1pPaQrv03vdCbvZMddC2zt23rqz76xj4iH2bme0cJyj2ONZmIWNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی در طول شب سه مرکز لجستیکی اوزون را در سراسر روسیه هدف قرار دادند و تأسیساتی در آدیجیا، استان استاوروپل و داغستان تحت تأثیر قرار گرفتند.
این حملات در میان مجموعه‌ای گسترده‌تر از حملات به مراکز توزیع بزرگ روسیه، از جمله سایت‌هایی که توسط اوزون و رقیب آن، ویلدربری‌ز، اداره می‌شوند، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70554" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70553">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70553" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70553" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70552">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOfC26sct2d7SvVYnfQVKDP9S0ivhC9cJTGFazTsNsDyOMNRQTKZXBRKuqmBIg5i3a1MY4mdJ15eab7ZPkC6MIM2NrdMQTKNgHoKNM-8LKnStQgnjG3NcwcdSaWa_VZmZmydVUj47QUMZ0MfHD7TpdhcwuPuYHKvqF8EjfWe8paVCGmwOlaL0QL23zjVDsrxFg5JflWoL-A4v_kQze8wYUUmC3EinUDl7E8g-WKp4YM1ydg5KSvHmcFMB5RgSiQIMxhgbLwilZUV2rbAH1UTCmOxirzsHL76PAPrF1k1yEJoZrzc_hWL3jU9HmtofdBRaSg1eFprcRBlef9seE69xg.jpg" alt="photo" loading="lazy"/></div>
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
r3
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70552" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70551">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇵🇰
وزیر کشور پاکستان: پیشرفت قابل توجهی در گفتگوها با ایران حاصل شد
⏺
📰
خبرگزاری رویترز به نقل از وزیر کشور پاکستان:
پیشرفت قابل توجهی در گفتگوها با رهبری ایران حاصل شده است.
ما در حال گفتگو با ایران برای فعال‌سازی مجدد «تفاهم‌نامه اسلام‌آباد» جهت حل و فصل اختلافات هستیم.
محور گفتگوها با ایران، تمرکز بر تنش‌های منطقه خاورمیانه(غرب آسیا) و یافتن راه‌هایی برای گشودن مسیر صلح است.
دیدار با رئیس‌جمهور ایران با نتایج بسیار مثبت به پایان رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70551" target="_blank">📅 10:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70550">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b422bdb1ee.mp4?token=r5f018uNmJ7zww30m2bDC3FfMlfkg_b7pOwUN9Fq8JUBE-IB-zAHyDjRZywVeUOKLgiMjTgY0MwyCYpiAnqOnH8Ke_QaF7O48n0y_YPu0l5kznRD0xDvxF66E7gTF_04rZStUyyEO3iNJLHKeojwe_LWOuYqA3x7ggC2RW2MJcgX64JTtp3NqZBY0Tp6IMp4rfythYjGfdZsobt4iAZ7ycaTv8gW2MZlJMBucTrEeIEDeczIgs7wiVTPdShjvahNz2IQZ68tUf9hVOTq3W1twlmvBx0PCdigqrj2jkBvZGqMx5z9dt9XxdKDcX64URoDRdjKnsemkWusyYCUzwbaBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b422bdb1ee.mp4?token=r5f018uNmJ7zww30m2bDC3FfMlfkg_b7pOwUN9Fq8JUBE-IB-zAHyDjRZywVeUOKLgiMjTgY0MwyCYpiAnqOnH8Ke_QaF7O48n0y_YPu0l5kznRD0xDvxF66E7gTF_04rZStUyyEO3iNJLHKeojwe_LWOuYqA3x7ggC2RW2MJcgX64JTtp3NqZBY0Tp6IMp4rfythYjGfdZsobt4iAZ7ycaTv8gW2MZlJMBucTrEeIEDeczIgs7wiVTPdShjvahNz2IQZ68tUf9hVOTq3W1twlmvBx0PCdigqrj2jkBvZGqMx5z9dt9XxdKDcX64URoDRdjKnsemkWusyYCUzwbaBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو به تازگی وایرال شده از یک گروهی که رفتن کرمان و در مکانی بنام قلعه دختر مثلا جن احضار کردن
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70550" target="_blank">📅 10:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70549">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a52e52e69f.mp4?token=lrKowoc8pbnacXaihl1qBpq-0TL4CPKk-V7bWc9KgeyYE4JA135ETA9PwSB6h9Gq59IPABtg3dZ-eEeMWJ8DFh5RnL09cegZGGwpHov1XOnVldPiZ04RRxD33fUBEwGDbuwASa1FmrgjqjB0mssFEV-NPlLN1VcQCAubzwbcMQnrmHEFxPquJQ9JL84N3GP8YFP63qYdHrP-agRpxmRxFUoU94c-gSj0cPEaE5C05_RES8GKhJRt614PK3NhvhywA29wkBchpXKJrOwtufAQoOzA5GN2SrhaW4kBo3kiGXPqK37exnB2d6BxQsZp5_UZAtWKOsxecb-Ec9WykzYAibSHl9C4FH2OhClRUOQiVQ2IyrC_zYvwQvgCcaFgH5oG2tP6KfxHIb5lopDYnHPxXgkP-nHhsRcNKCSG5P_s2FOCYd5eL0WBoEYozJOyRBnOzNpirpmWJ8VKj3nKTj5HNikKtHcXdnAObm2D4WUPpMkc72eXL5foUJdbiszgHStWsG4KK1M6DNNpP6Wv4dbQk-YvSUEsNv6FQazMqQVveAeRDtG3rQZirnjDURqHxk7JMFqleBk03VwbvEEpTMm2-WjhsC2w4cQVB7C0sbxevbaD4yYV5cEHosQNCq56CEVpHheeiaC_OHapi3s-U5utoOwkO3HUiLE0SGd4QntAQPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a52e52e69f.mp4?token=lrKowoc8pbnacXaihl1qBpq-0TL4CPKk-V7bWc9KgeyYE4JA135ETA9PwSB6h9Gq59IPABtg3dZ-eEeMWJ8DFh5RnL09cegZGGwpHov1XOnVldPiZ04RRxD33fUBEwGDbuwASa1FmrgjqjB0mssFEV-NPlLN1VcQCAubzwbcMQnrmHEFxPquJQ9JL84N3GP8YFP63qYdHrP-agRpxmRxFUoU94c-gSj0cPEaE5C05_RES8GKhJRt614PK3NhvhywA29wkBchpXKJrOwtufAQoOzA5GN2SrhaW4kBo3kiGXPqK37exnB2d6BxQsZp5_UZAtWKOsxecb-Ec9WykzYAibSHl9C4FH2OhClRUOQiVQ2IyrC_zYvwQvgCcaFgH5oG2tP6KfxHIb5lopDYnHPxXgkP-nHhsRcNKCSG5P_s2FOCYd5eL0WBoEYozJOyRBnOzNpirpmWJ8VKj3nKTj5HNikKtHcXdnAObm2D4WUPpMkc72eXL5foUJdbiszgHStWsG4KK1M6DNNpP6Wv4dbQk-YvSUEsNv6FQazMqQVveAeRDtG3rQZirnjDURqHxk7JMFqleBk03VwbvEEpTMm2-WjhsC2w4cQVB7C0sbxevbaD4yYV5cEHosQNCq56CEVpHheeiaC_OHapi3s-U5utoOwkO3HUiLE0SGd4QntAQPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیوی جدید از حمله هوایی و پشم ریزون آمریکا و اسراییل به خرم آباد در جنگ ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70549" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70548">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10dcd43f2.mp4?token=eNr3T-Tk7wncZSWKYvZrTV6xycTPasqJ1sVz-fZX4qkZ5q5gJ2r3IMMdCLWrRpzw0EJuXdQr2YKufym13ce-KbrpTMyR2ssboWA8oQR9aonFxSnkS-IW0OSBESdsx8d7zylJiGhZzWM211AJQQRPUkMb383ytaBG5PGrutNcS3H1SskkeckLE0Zc0MPsibwqsV64t405EKja661IQmdUDyA4PcTZ3yQKL6Yo2ZEqG4Xqq_XBpW0UaX7tv5Th2qC8LwxvxP2iTQKbVngplVejjAWBUPnmKjIgBVcXe1mtb6iQ3Xd5nBw8iUIFdWiYONnYMyO2G_svR5qhf8YrRA1qxp3KSgzq1JfqLFwfJVqR_Npj87dcRUTfk8Uw2wU_C8AazE2hlj-tE6K8v6fwxz4bmhRecuZrjJCl814xLADydwlGw30UlDPLl1L2_pqT4NRXeLzD2A8THse7OGU0GHWg2NmOkXB0cnEw5zzEXE8ErHo3uW8b6onru-v-9PvJfGFJSB4V-x9Lua3AR5fMeWKz9W7weti6A9o9YUBj_9i9a7CXjm92Bsyxc9xwGxD9xxULlG6GzEl31_ZIEbuTz1E0mlwEixdnY7fpptETrIFw0n4hWUSPf7fT6vU9xYMW-mJgJNv0UBqKIe7047Ps7rPq4nQHxIa5jmedInDpzhsFwBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10dcd43f2.mp4?token=eNr3T-Tk7wncZSWKYvZrTV6xycTPasqJ1sVz-fZX4qkZ5q5gJ2r3IMMdCLWrRpzw0EJuXdQr2YKufym13ce-KbrpTMyR2ssboWA8oQR9aonFxSnkS-IW0OSBESdsx8d7zylJiGhZzWM211AJQQRPUkMb383ytaBG5PGrutNcS3H1SskkeckLE0Zc0MPsibwqsV64t405EKja661IQmdUDyA4PcTZ3yQKL6Yo2ZEqG4Xqq_XBpW0UaX7tv5Th2qC8LwxvxP2iTQKbVngplVejjAWBUPnmKjIgBVcXe1mtb6iQ3Xd5nBw8iUIFdWiYONnYMyO2G_svR5qhf8YrRA1qxp3KSgzq1JfqLFwfJVqR_Npj87dcRUTfk8Uw2wU_C8AazE2hlj-tE6K8v6fwxz4bmhRecuZrjJCl814xLADydwlGw30UlDPLl1L2_pqT4NRXeLzD2A8THse7OGU0GHWg2NmOkXB0cnEw5zzEXE8ErHo3uW8b6onru-v-9PvJfGFJSB4V-x9Lua3AR5fMeWKz9W7weti6A9o9YUBj_9i9a7CXjm92Bsyxc9xwGxD9xxULlG6GzEl31_ZIEbuTz1E0mlwEixdnY7fpptETrIFw0n4hWUSPf7fT6vU9xYMW-mJgJNv0UBqKIe7047Ps7rPq4nQHxIa5jmedInDpzhsFwBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان تحلیل‌گر ارشد سیاسی در مورد فشار اقتصادی آمریکا؛
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70548" target="_blank">📅 09:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70547">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70547" target="_blank">📅 02:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70546">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAoJB1EJhRsF0FVz3oJ-aTF1cEq0SJMz-e-a3Y_TkMaeKEbhVM31PsJH5OF6r2jA4jQL6-HUl6zbukOcyBc4GWNy4QUfcI7XAAxHNe1tU0nTqe0fetitQWPAlJ_EfEoAbK-K18QGMq2H1PAzjmlW_AraPxXJGGW0F8Xurl8PDcaOAnFDZsBFAA3OFGGWtgaBBBO8jcuKXAa6GC-cYOZ6yw6NYvsPHi7uX910ZaLJ7oIfDDB_Ca-OYSFsQmY2f2LVO3az1k_SgtRGpmczqUU5SSmzcbJnKmAgNPcF1odbbezAU6PjgpZZZwhgEr89G8Oqg_v2QvLJUXIaM8I_9fCV2-no" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAoJB1EJhRsF0FVz3oJ-aTF1cEq0SJMz-e-a3Y_TkMaeKEbhVM31PsJH5OF6r2jA4jQL6-HUl6zbukOcyBc4GWNy4QUfcI7XAAxHNe1tU0nTqe0fetitQWPAlJ_EfEoAbK-K18QGMq2H1PAzjmlW_AraPxXJGGW0F8Xurl8PDcaOAnFDZsBFAA3OFGGWtgaBBBO8jcuKXAa6GC-cYOZ6yw6NYvsPHi7uX910ZaLJ7oIfDDB_Ca-OYSFsQmY2f2LVO3az1k_SgtRGpmczqUU5SSmzcbJnKmAgNPcF1odbbezAU6PjgpZZZwhgEr89G8Oqg_v2QvLJUXIaM8I_9fCV2-no" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
⭐
کانال اطلاع رسانی سایت:a2
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70546" target="_blank">📅 02:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70544">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXI8ahlEObrzTWiO0GWSbtGJLbdZQx1OocRFtTb3ti3gvbMknPApvV_F3pbWMtsCLV_Atzsg2NlcRAe2k1uwyM9WlGZaFmNIgVm0aTM3TNAyQuIrj9lwke5dU8-nWqH0bwATZqle1TUzLuhnbGU2bWVs2bzh6nwoZo3Zx8CEGLpdJo8hOWu4bxjt516ENcIkTij54YGxXSTkF3fgQPtZJIPDlGqfWu3W7AodUDqcR-kUF5EMBtBBOsjzQiyLv3XsCsm4wJm_e3vyzxVexjhCLOWRzF8Ba1eHR82DmJ7FDk1At9ThmkqGUVDj_PXC4tUloVhAOygxuxLIhwJrh3Un_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujbN4UJVMRGZvE24iL1OltyXtr1vfkI5GlmoqTI-lqPqDPpuvTOA5ADpUuGWYNtjEhhIut-i4rLEU_yKs-NyGAU0lrRBGS6o0ONjC247fYcGbKUm0AGdAfz-uhEvbKtAbSLVg67b5wfbJnddp9S3nB7fWJB-uo0c7JJgoDVacTNv7V3j9Vja99b1kzgsgOTJodF_lsEkVJTV9UjjdiI6BJHUN5pnfRWJ5uCnHawk5FtsSnEUnt-XjwRUN---X_2EI4pcQzheAjM5PdhJdsF4epqsgWLjVExDdphuMJDPLMdNsTAjObZxcUi4-V51MwvNvMnvxjg99RlXPasnQK7z2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
#فوری
؛وزارت امور خارجه ایالات متحده:ده میلیون دلار برای کسی که اطلاعاتی درباره رهبران سپاه پاسداران انقلاب اسلامی ایران ارائه می دهد
احمد وحیدی/ فرمانده سپاه پاسداران
علی عبدالله/ فرمانده نیروهای مسلح (خاتم‌الانبیاء)
سعید آقاجانی/ فرمانده واحد پهپادها در ستاد هوافضای سپاه پاسداران
حامد لشگریان/ فرمانده واحد سایبری در سپاه پاسداران
مجید خادمی/ فرمانده اطلاعات سپاه پاسداران
⭕️
خبر واقعاً دوباره در ۲۴ اوت ۲۰۲۶ در حساب (Rewards for Justice)منتشر شده است اما تصویر قدیمی است و بروز نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70544" target="_blank">📅 02:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70541">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=UIgZuYwz618Kog4c52UBeIQVWulr8SByrEz3S3ZC7TFgw7LXIMJLlqommU-NwGVbWd-aTHr8MAu3gsPeEPZu9zjGiVGrPAHQ_siqeiJ8B0rIHAYeA-Gn5vUHJ5ypyZ_mcSUob5Gr0jnCOfdRWlmLeyjKtACbQNTDObUMGevZTr1opISTJjlSNdXcxzyplWmZe_HxaFVVMFZU_rC9jvpaFa5D40KuVAfwJNhYb9zvd0Zxa7QOPtRxOCkPM6eOiOpZOCSdixYuKIUFZxHQvYFPxkkOBuVmMYuEYNnN9UMxv6G73kRXiT-hyAdRxZlEz-14kHcNusUVB7wylXaeXoaKfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=UIgZuYwz618Kog4c52UBeIQVWulr8SByrEz3S3ZC7TFgw7LXIMJLlqommU-NwGVbWd-aTHr8MAu3gsPeEPZu9zjGiVGrPAHQ_siqeiJ8B0rIHAYeA-Gn5vUHJ5ypyZ_mcSUob5Gr0jnCOfdRWlmLeyjKtACbQNTDObUMGevZTr1opISTJjlSNdXcxzyplWmZe_HxaFVVMFZU_rC9jvpaFa5D40KuVAfwJNhYb9zvd0Zxa7QOPtRxOCkPM6eOiOpZOCSdixYuKIUFZxHQvYFPxkkOBuVmMYuEYNnN9UMxv6G73kRXiT-hyAdRxZlEz-14kHcNusUVB7wylXaeXoaKfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم تکون دادن ترامپ در رویداد «Freedom 250 Grand Prix» در واشنگتن دی‌سی، برای آغاز مسابقه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70541" target="_blank">📅 02:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70540">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH103GeNOvBe-c_oMSbsYdXeTf8VAteBZqoNgyt2gVhvLLfnmVsR0aIT70-0USxweC1oCMRhAn2NeB_SDu-1_pWYYPVONyAJgfdYV0nh7GJ9l21SqDRJ7Nu5WBhe_OadtaBBHKcG95lbwcddO9RZRYaFXzQZk_nH9uh-_kYMJF1Xa_6nKUb_s_iQ-IpfQd9IQbVKDaG9w5VslrWUqz4NbfpU_ZBBG9QVgG0VScEgMkWVXXvdSPGv1pgs8OpvPy39FEUMN3vgTcQrtOy3aKlo7Vke3yAf2m7RvMsUMAw_IAqGN-DLKZEV8LYF0GKFiszTLdMm2wpU-VYyit5bY3nCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا:
ما گزارشی درباره وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرق منطقه الشیشه در عمان دریافت کرده‌ایم.
یک نفتکش مورد اصابت پرتابه ای ناشناس قرار گرفته، بخش موتور آسیب دیده و کشتی از کار افتاده.
خدمه سالم هستند و تاکنون میزان تاثیرات زیست محیطی این اتفاق مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70540" target="_blank">📅 02:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70538">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6611759db.mp4?token=qwtgwLdkwD1sxE3mnJQBoWjIaOjSekhzVBm_-QfJjzKWBgw-Wmtdzhucp1uHHkqUTqTeiDQIBo0AqZVDNztzym0yUl2QQCoCkDTG3TzHSLIvvxIk49HJ_jqmoaD9GitFTFjtgSv_RO-cy9QaB5U7-gl3Pg3RLtJ1Ag7ULaNpckdkOi4EXa3EUjFWg-B0B2YDh6eT0AYRNu22Zg49YB1UFcgQhHyOjXAYXJP70Z5XYb59M-bvv3Ux_oPB0WIeW_1yed1__lcxV6UWKKHzRpGMaIh_Yf3xL08z2LRqS-_vDJNMnRKTtW2YQkFLDkH80LMmuNjLvgHJMO1Urs5Dcpz5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6611759db.mp4?token=qwtgwLdkwD1sxE3mnJQBoWjIaOjSekhzVBm_-QfJjzKWBgw-Wmtdzhucp1uHHkqUTqTeiDQIBo0AqZVDNztzym0yUl2QQCoCkDTG3TzHSLIvvxIk49HJ_jqmoaD9GitFTFjtgSv_RO-cy9QaB5U7-gl3Pg3RLtJ1Ag7ULaNpckdkOi4EXa3EUjFWg-B0B2YDh6eT0AYRNu22Zg49YB1UFcgQhHyOjXAYXJP70Z5XYb59M-bvv3Ux_oPB0WIeW_1yed1__lcxV6UWKKHzRpGMaIh_Yf3xL08z2LRqS-_vDJNMnRKTtW2YQkFLDkH80LMmuNjLvgHJMO1Urs5Dcpz5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
برخی از کاربران فضای مجازی مدعی شدن امروز برای اولین‌ بار جایگاه های بنزین تهران با کمبود بنزین مواجه شدن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70538" target="_blank">📅 00:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70534">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9tZ0EDijZhr-lco3u9m6dxgdT_9FQanxxcRtaa3tkBSzXA8tBlsf-DMeiQjtKppMa7Dtn3D2ZT3wO16IUdIMwoLc6D5mwSDIlDmj2NwUy22-GZcmCZ9XUzt_2fx2s5rKsK_P-q97o8whWXJ4kuZ-egx8X1YPlFv8i-qkG5Bc8FXj4ezPXE8vcdotrl2BmC4c1GPGIHO13_Pw3VFlE_KwA_9TpYvPGrJGWGvjRmOON2FMMvKaaZ_alvIcLqeCUA8Sv69-E0T0d_Mau4qGm39Pisb6nBVyhXICcdac1hq6EzOs51_udWlpWq71A7fVbYVsK2pNM2zcC-N1ptBQ6T10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a3f2ccf.mp4?token=j2na5N515ueRtq9S20iIZVoZyxisuBtd39Lihx_N7o_sHirsH1RVzocftQ0mNCZS3onaRl5ex5_6Wu48mZQuT-1oKeknKGf97SIFCH3Oyz-ngVrP30lOF9IdnBrY4cDsFay0aTqoIRvQtTAW5-vxzXz6rQ_Q4lum9-9zfeYJPPKST0JyuqQN3lFIPtJLEjS-bLZaJqr0482U1CRS1MlJ4Qrk4eBeGkQ89qx_7n1_RO6tOyJ7HhdkIqr3Ll60_Fq51CYLMJhVM4Vxc4qnTVLpwFLMCSY8C7kz94bR9m_XFEXz1_3cGpBrdXPV7B8O1LQ96L5OwC68RqgK95CPifzxvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a3f2ccf.mp4?token=j2na5N515ueRtq9S20iIZVoZyxisuBtd39Lihx_N7o_sHirsH1RVzocftQ0mNCZS3onaRl5ex5_6Wu48mZQuT-1oKeknKGf97SIFCH3Oyz-ngVrP30lOF9IdnBrY4cDsFay0aTqoIRvQtTAW5-vxzXz6rQ_Q4lum9-9zfeYJPPKST0JyuqQN3lFIPtJLEjS-bLZaJqr0482U1CRS1MlJ4Qrk4eBeGkQ89qx_7n1_RO6tOyJ7HhdkIqr3Ll60_Fq51CYLMJhVM4Vxc4qnTVLpwFLMCSY8C7kz94bR9m_XFEXz1_3cGpBrdXPV7B8O1LQ96L5OwC68RqgK95CPifzxvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خرسی که وایرال شده بود مهمون سفره کوهنوردا میشه
متاسفانه رئیس محیط زیست مشکین‌شهر از شکار شدن این خرس خبر داد
💔
شکارچی هم همراه ۴ لاشه از حیوانات کوهی دیگه دستیگر شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70534" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70533">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgrI-dard7f9EfbsMUcdNkcuTva96C58Ek5c_rIzuHhqjHX32IXwvIX80ro9f0NJ1f6VaMxB5TXd-fdZl1NEkyZjrjx4SgUv0AVv04WzqWhvKVZDkltxLRyn8_CtR0QyYYhseTa_Iw58XpnvEBh0y0oMdasc0w7hUiNB7w5bez_sEJcN2AX-aFy_wA2BY_iOaKi0LnxTluPiOBIeu9GCZPSG_WuhzBOZup1_VvXd6-fmpuKwt0GDvw-BYa4mTxwbYwHvViWoMHQirgVYmANjo-a2fW1vQ0WgkhvGCvnppPNOlnI6wEB9qfUwkAq2_qwef_t2HnCrgw5ZLGkIddeo-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
به دونالد ترامپ، رئیس‌جمهور آمریکا، و اسکات بسنت، وزیر خزانه‌داری آمریکا، بابت تحریم‌های جدید علیه جمهوری اسلامی تبریک میگم.
شما کاملاً حق دارید از این دیکتاتوری سرکوبگر و کسانی که به ادامه اقدامات تهاجمی اون کمک می‌کنن، هزینه سنگینی بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70533" target="_blank">📅 23:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70532">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=mpZMze9BjTzV2EF2Dv9qWW57EyVKhTjd0qf1X8Na5KFKF3UvxZLKhIy6uvGeeej3OTPRVL7iXInl924iadRkau7Kl923qOqiQF0q1ZOTvWTowua7eAm4gh3_S_1xs4roAqOqZmOfhDDItLWDXGLeL42l0YKHrQr_hFjGeewYvmgMtoBzLCXAqEaUove4kYwp6mLADCOin_C9p4HaEbGLX267vfbiwvuyWH_JrsCW_NdgHTx9MCRedYGMkYmQHA9OO5eZ4C7nKPkkJ5VHSIqFvRKkUgAqGblerl2O_tcQesJK43_mImDd1uGEYRyxyBnvYmvBhIlBTefVq6p19Wo9tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=mpZMze9BjTzV2EF2Dv9qWW57EyVKhTjd0qf1X8Na5KFKF3UvxZLKhIy6uvGeeej3OTPRVL7iXInl924iadRkau7Kl923qOqiQF0q1ZOTvWTowua7eAm4gh3_S_1xs4roAqOqZmOfhDDItLWDXGLeL42l0YKHrQr_hFjGeewYvmgMtoBzLCXAqEaUove4kYwp6mLADCOin_C9p4HaEbGLX267vfbiwvuyWH_JrsCW_NdgHTx9MCRedYGMkYmQHA9OO5eZ4C7nKPkkJ5VHSIqFvRKkUgAqGblerl2O_tcQesJK43_mImDd1uGEYRyxyBnvYmvBhIlBTefVq6p19Wo9tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اوستاد خوش‌چشم :
جنگ بعدی تو آبان و آذر با بمب باران شدید آمریکا شروع می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70532" target="_blank">📅 22:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70531">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">با این کیر شق شده‌ای که من از اسکات بسنت و ترامپ می‌بینم، مطمئنم خیلی زود دلمون برا دلار 200 هزار تومنی هم تنگ می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70531" target="_blank">📅 22:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70530">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=nDSrBdPnvP7NYtCnquCEhIOT3qM57yeoXAu_1GTwjWobkJ8IFshP-lS7OqZM7Ci3vuKT_dWAfnoG_29q-s7Beu6Zbayr_TI3axZPsDEXEGp_nPuC-55Bbq3HbPejRCkaEMwqxDipWUcUBbRoIS_Hub3b4KadjQNTURZw742NcEK8Lw-A6vR4-YjZR6rZ6chJZN329sR3HLEJeUsp5Fm11zH4qnMiaC-SawFUw6onANr_JrBWtSDHwX04acn1w6Dq2EWpFfCC37sYLl8SjJ76Nzj8Xo1gRtPA0MMhHMuXlMvhhBEIGMglPhmvm01js3qopMoWjpk8sIuhFu8DiOQY4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=nDSrBdPnvP7NYtCnquCEhIOT3qM57yeoXAu_1GTwjWobkJ8IFshP-lS7OqZM7Ci3vuKT_dWAfnoG_29q-s7Beu6Zbayr_TI3axZPsDEXEGp_nPuC-55Bbq3HbPejRCkaEMwqxDipWUcUBbRoIS_Hub3b4KadjQNTURZw742NcEK8Lw-A6vR4-YjZR6rZ6chJZN329sR3HLEJeUsp5Fm11zH4qnMiaC-SawFUw6onANr_JrBWtSDHwX04acn1w6Dq2EWpFfCC37sYLl8SjJ76Nzj8Xo1gRtPA0MMhHMuXlMvhhBEIGMglPhmvm01js3qopMoWjpk8sIuhFu8DiOQY4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیوی وایرال شده از یه پیرمردِ حامی حکومت که به طرز سنگین و عجیبی داره پرچم تکون میده:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70530" target="_blank">📅 21:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70529">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9839729319.mp4?token=VHKI_Yu5xaHxqnI2TGyPep8EjcnKYPDZrPO2NtdZqPjioo4xVbHXELIh1z_5A4veKnOOi8SWbTvbdT0JLBYUS64FFRB6vvsItPNMJVkuEzWpX_YO6zmFhKQ40aLphQiw0Lt7ueMo-4MbydUz31pjTHofzBbSVUnSyGhOv0BVv4y4JO8l9oinantgfCB3oMbd8YxFNHPQr-ni2ABVdmMqUxgdgshFXrnc6N7PN1hC74xj85QWxvny5XI_WJcP3Tr6jjkUSkOeMz8TKdnKZNK2isijHgXmQ5YamDfFp1HDWqtjXo9KxyKjzH_pt-QBpo5fxtf_BjOJrC1MMZIQGeNUnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9839729319.mp4?token=VHKI_Yu5xaHxqnI2TGyPep8EjcnKYPDZrPO2NtdZqPjioo4xVbHXELIh1z_5A4veKnOOi8SWbTvbdT0JLBYUS64FFRB6vvsItPNMJVkuEzWpX_YO6zmFhKQ40aLphQiw0Lt7ueMo-4MbydUz31pjTHofzBbSVUnSyGhOv0BVv4y4JO8l9oinantgfCB3oMbd8YxFNHPQr-ni2ABVdmMqUxgdgshFXrnc6N7PN1hC74xj85QWxvny5XI_WJcP3Tr6jjkUSkOeMz8TKdnKZNK2isijHgXmQ5YamDfFp1HDWqtjXo9KxyKjzH_pt-QBpo5fxtf_BjOJrC1MMZIQGeNUnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
«بِسِنت» درباره ایران:
کشورهای حوزه خلیج فارس در طول سال‌ها از سیاست مماشات با ایران چه چیزی به دست آورده‌اند؟
زمانی که ما ایران را بمباران می‌کردیم، ایران کشورهای حوزه خلیج فارس را بمباران می‌کرد.
سیاست مماشات در قبال این رژیم کارساز نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70529" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70528">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fd4a88095.mp4?token=vE9feu8oa0mhXFWZdr7R75QSL9iLzs_zjdn2sK3m-cSibULu2uaXyUCsQSqjht4pDJcdFNySjuANiVCiQAhuE5WONpZtU1R1lfL4k4mVDh1I249wMxSymqgv1WdyfwOXol-5ruwt0fYeFw788n6isMaeoJ-beqZn9cg1GDkrXANh58OB-ACw9nTZqo8CoDSqsPT25YC7rSNNMEOKbKn9tNzmgD8rJUQdnqhASrP_N-mHFYdHn8n0tecmfSpEDcTN8Ira16CqHqx84w76mQpHffDFJEXozTFS7cRDwmnuFAm1Jxotbiuk-EviXivpxzEWISM6iVl7J_BvlrNkOoz4LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fd4a88095.mp4?token=vE9feu8oa0mhXFWZdr7R75QSL9iLzs_zjdn2sK3m-cSibULu2uaXyUCsQSqjht4pDJcdFNySjuANiVCiQAhuE5WONpZtU1R1lfL4k4mVDh1I249wMxSymqgv1WdyfwOXol-5ruwt0fYeFw788n6isMaeoJ-beqZn9cg1GDkrXANh58OB-ACw9nTZqo8CoDSqsPT25YC7rSNNMEOKbKn9tNzmgD8rJUQdnqhASrP_N-mHFYdHn8n0tecmfSpEDcTN8Ira16CqHqx84w76mQpHffDFJEXozTFS7cRDwmnuFAm1Jxotbiuk-EviXivpxzEWISM6iVl7J_BvlrNkOoz4LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
بِسِنت درباره ایران:
کسانی که در کنار ایالات متحده می‌ایستند، از مزایای شراکت ما بهره‌مند خواهند شد.
تمام شعبه‌های بانک ملی(ایران) باید تعطیل شوند.
🎙
خبرنگار:
گفتید ترامپ با رهبران جهان تماس می‌گیرد. او با چه کسانی تماس می‌گیرد؟
🇺🇸
بِسِنت:
ما نامی از افراد نخواهیم برد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70528" target="_blank">📅 21:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70527">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d89159ae.mp4?token=XSdsrmO-w09n7eNIu_QWZFoSq5vMEVmJgsnB1Zoq0mqJ8KWwnpvuJLynD99H43Dcq1vWrP9bM-pWNnMvroLpqGqkoAxSTugjDQdPbuBScwe7fjO1znW62mwuc2B6zBrdZzMpshXCwdKPpqKn8iZW6hOGg-XymUeMpk_mgUOcFBGJiFDxDZbr0j-shEhLnOEuchOQTFzkdfH0Q16OoAZ2K9zoA-hMcnxv1_92X93a_iCdDA3UTKDObQ5yEea5Y9zotzfdgS3ebszYZPWSf842A1wd9XsfkgD2jDcf4PvIGVYov1eIhTAM6y9-YJ0OaMmz1t3XTanT3ZxJvEMdz0KW4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d89159ae.mp4?token=XSdsrmO-w09n7eNIu_QWZFoSq5vMEVmJgsnB1Zoq0mqJ8KWwnpvuJLynD99H43Dcq1vWrP9bM-pWNnMvroLpqGqkoAxSTugjDQdPbuBScwe7fjO1znW62mwuc2B6zBrdZzMpshXCwdKPpqKn8iZW6hOGg-XymUeMpk_mgUOcFBGJiFDxDZbr0j-shEhLnOEuchOQTFzkdfH0Q16OoAZ2K9zoA-hMcnxv1_92X93a_iCdDA3UTKDObQ5yEea5Y9zotzfdgS3ebszYZPWSf842A1wd9XsfkgD2jDcf4PvIGVYov1eIhTAM6y9-YJ0OaMmz1t3XTanT3ZxJvEMdz0KW4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اظهارات «بِسِنت» درباره چین و ایران:
امروز می‌خواهیم به صراحت اعلام کنیم که هیچ‌کس از دسترس تحریم‌های ایالات متحده مصون نیست.
اگر آن‌ها تراکنش‌هایی را تسهیل کنند و بخشی از آن چرخه‌ای باشند که نفت ایران را به پول و ابزار سرکوب تبدیل می‌کند، هدف تحریم‌ها قرار خواهند گرفت.
⭕️
اکنون زمان آن فرا رسیده است که رهبران جهان میان آمریکا و ایران تصمیم بگیرند.
انتظار دارم تا پایان همین هفته شاهد اعلام خبر مهمی مبنی بر اعمال تحریم علیه یک مؤسسه مالی باشید.
🎙
خبرنگار:
شما این وضعیت را یک «روز دی» (D-Day) اقتصادی توصیف می‌کنید، اما «روز دی» صرفاً تهدید به تهاجم نبود و ایالات متحده هم برای آلمان ضرب‌الاجل تعیین نکرد. چرا تحریم‌ها همین امروز اعمال نمی‌شوند؟
🇺🇸
بِسِنت:
چرا باید بخواهم نظام مالی جهانی را منفجر کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70527" target="_blank">📅 21:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70526">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155ae6e1ec.mp4?token=m5Jk5VBfcsUJF7K5z7qXbeSqtvXx4y8XHrizSsSMaJK5RfOUckjyIrd5zY1h-6hkuCg0whZFqGgcfAKvDOgrfXx2jhBFf-k_4amXhLUidr_WMPrqchnl29VB1mqiH1avPEEucZ-4sCpcwSlKBb7ODDRHvk7PBPiZ8QIWGHb5VHcf-ZbY73pIm7z2WyQ6gL2IbM5N28O33KxWXp7qJ-wD79tm2u9hiHjy2PYR9aADEq135Ub2380rpoEG9WVrezg9UkV-B53pzflSv7psaOcsrTv2J_Ni7Tm5j9L-LZ7PoyVbo_qyuJqIqA7iouoeGMrDll_qaA1sEGoLfikM3nulgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155ae6e1ec.mp4?token=m5Jk5VBfcsUJF7K5z7qXbeSqtvXx4y8XHrizSsSMaJK5RfOUckjyIrd5zY1h-6hkuCg0whZFqGgcfAKvDOgrfXx2jhBFf-k_4amXhLUidr_WMPrqchnl29VB1mqiH1avPEEucZ-4sCpcwSlKBb7ODDRHvk7PBPiZ8QIWGHb5VHcf-ZbY73pIm7z2WyQ6gL2IbM5N28O33KxWXp7qJ-wD79tm2u9hiHjy2PYR9aADEq135Ub2380rpoEG9WVrezg9UkV-B53pzflSv7psaOcsrTv2J_Ni7Tm5j9L-LZ7PoyVbo_qyuJqIqA7iouoeGMrDll_qaA1sEGoLfikM3nulgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
«بِسِنت» درباره ایران:
⭕️
خطاب به سربازان عادی حامی این رژیم:
در شرایطی که پرداخت حقوق‌هایتان بیش از پیش متوقف شده یا به بهانه تأخیر به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشور را به سوی پیروزی می‌برند یا نابودی؛ و به یاد داشته باشید که دیوار برلین زمانی فرو ریخت که سربازان عادی تصمیم گرفتند به سوی مردم خود شلیک نکنند.
⭕️
و خطاب به کسانی که راه را برای تهران هموار کردند:
بهای آزمودن عزم و اراده واشنگتن را دست‌کم نگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70526" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70525">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91fbf3e30.mp4?token=j6khh8vpkDt_M-WFuf7fI0v16EY6Z9CQydmwBgbSb3SBpXG3UhUn7blTjlYLs0B3MTTBIQLF593Upb-H0ZWt_uLbCPHCGzyJg2kBYBZZfzGIiax6VqgCnvWOPpJLSeS1m2G3HIAcbZKr9Uk6-cxoofkmOHuMg9FhkeEpfEsJeF45evyz1lZA5F2hnOMb48v7T1EiWPvO6VcUm-vhdCE59JaqIcYtCE4Njy7Mh_Af_B7zhRwSnQEOuYcttygLQEDUCXIMGHI5oyd_uMqKiMVTj6NS27tTqHHvJdHm_BSI1v_TvVn8Kd5ZWNOl-btz5SY78B_TC0YKLGq8nBnRJ-qFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91fbf3e30.mp4?token=j6khh8vpkDt_M-WFuf7fI0v16EY6Z9CQydmwBgbSb3SBpXG3UhUn7blTjlYLs0B3MTTBIQLF593Upb-H0ZWt_uLbCPHCGzyJg2kBYBZZfzGIiax6VqgCnvWOPpJLSeS1m2G3HIAcbZKr9Uk6-cxoofkmOHuMg9FhkeEpfEsJeF45evyz1lZA5F2hnOMb48v7T1EiWPvO6VcUm-vhdCE59JaqIcYtCE4Njy7Mh_Af_B7zhRwSnQEOuYcttygLQEDUCXIMGHI5oyd_uMqKiMVTj6NS27tTqHHvJdHm_BSI1v_TvVn8Kd5ZWNOl-btz5SY78B_TC0YKLGq8nBnRJ-qFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اظهارات بسنت درباره ایران:
از امروز، حلقه محاصره را تنگ‌تر خواهیم کرد و تمامی منابع درآمدی احتمالی را که بودجه سپاه پاسداران و رژیم ایران را تأمین می‌کنند، مسدود خواهیم ساخت.
ما رویکردی را با هدف جلوگیری از هرگونه نشت (دور زدن تحریم‌ها) به اجرا می‌گذاریم.
ترامپ با رهبران جهان تماس می‌گیرد و مشخصاً از آن‌ها می‌خواهد که تعاملات خود را با رژیم ایران متوقف کنند.
هر نهادی که به نمایندگی از ایران پولشویی را تسهیل کند، از سیستم دلار آمریکا حذف خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70525" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70524">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75070defdc.mp4?token=cBIp1D6wYqRCf67qU_xBozA8YgNjCrszSdDc_ObJsPxzcLnTv3vpZJcgb_n9Rg_vEE6GYTCoLVsdPvkyWUWl03L-Rk28Ya3w26sUkCz2vDBtXoTIKvVnzU4UjcInEstZNf4kQNJsSFMF7Trb9NFbNhjXlaSbvCupdqrN15NKSgtUj5tuwfKISTm7loR63ifvn7pO8jh7XFB3JMODduXQlVe0mq3x98HUGg1nmIrUsuclkDFe5mqjf1ikP86fIFgUfQ2PqRQLL0nkT5xEzcAHo_PcflUDwlEhD9ILBt7PMo0s2MzYRFgpvDgf_0cKRmGzMRXL0z-4wBE7GHE48v61eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75070defdc.mp4?token=cBIp1D6wYqRCf67qU_xBozA8YgNjCrszSdDc_ObJsPxzcLnTv3vpZJcgb_n9Rg_vEE6GYTCoLVsdPvkyWUWl03L-Rk28Ya3w26sUkCz2vDBtXoTIKvVnzU4UjcInEstZNf4kQNJsSFMF7Trb9NFbNhjXlaSbvCupdqrN15NKSgtUj5tuwfKISTm7loR63ifvn7pO8jh7XFB3JMODduXQlVe0mq3x98HUGg1nmIrUsuclkDFe5mqjf1ikP86fIFgUfQ2PqRQLL0nkT5xEzcAHo_PcflUDwlEhD9ILBt7PMo0s2MzYRFgpvDgf_0cKRmGzMRXL0z-4wBE7GHE48v61eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
اسکات بِسِنت:
ما در حال آغاز یورش اقتصادی علیه پیوندهای مالی ایران در سراسر جهان هستیم.
هدف ما قطع تمامی شریان‌های حیاتی اقتصادی است که این رژیم ستمگر را سرپا نگه داشته‌اند؛ تا زمانی که تهران کاملاً تنها بماند.
🔴
در دوران ترامپ، آمریکا دیگر صرفاً تهدید ایران را مدیریت نمی‌کند.
ما در حال پایان دادن به آن هستیم.
ایران دو مسیر پیش رو دارد: انزوای کامل جهانی یا مسیری به سوی بازگشت به وضعیت عادی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70524" target="_blank">📅 20:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70523">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b43c7e4e6.mp4?token=elXCsdQ2DDILmzcm3DaLKnkTSps4HQ7lUTKMfY9WY4AcxhWpJzC1VP5MfgMzhqjBNsSS-OFYqRM5dqhgCLI79CqcrnZDFrh2IK3Gei_m5ee6sgJh4uLxc2tViCrHfUsX5hbX0Qjt4TpH2MkNnGrB30L07u_nQ7F2X4N0W_ivyrm0qRJPizB_DcqwWJV_QMUUtTL1XHn0d2TV6PPpmSTT9_W0PtQQnO4w9AkTfJrVBAesxCt4C3FJ_Mo52XrJ4W0vEsh1v0Tj3e-P2e8mCQ3ugH4xKULY7b00MxR7fGAOMHfaLkgDMRMB1gQAbyXy40QEhkSt9g1vAx_F9v6Y7tjVMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b43c7e4e6.mp4?token=elXCsdQ2DDILmzcm3DaLKnkTSps4HQ7lUTKMfY9WY4AcxhWpJzC1VP5MfgMzhqjBNsSS-OFYqRM5dqhgCLI79CqcrnZDFrh2IK3Gei_m5ee6sgJh4uLxc2tViCrHfUsX5hbX0Qjt4TpH2MkNnGrB30L07u_nQ7F2X4N0W_ivyrm0qRJPizB_DcqwWJV_QMUUtTL1XHn0d2TV6PPpmSTT9_W0PtQQnO4w9AkTfJrVBAesxCt4C3FJ_Mo52XrJ4W0vEsh1v0Tj3e-P2e8mCQ3ugH4xKULY7b00MxR7fGAOMHfaLkgDMRMB1gQAbyXy40QEhkSt9g1vAx_F9v6Y7tjVMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
اسکات بِسِنت وزیر خزانه‌داری آمریکا:
امروز، وزارت خزانه‌داری ایالات متحده «عملیات طرد اقتصادی» را آغاز کرد؛ کارزاری بی‌سابقه علیه جمهوری اسلامی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70523" target="_blank">📅 20:41 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
