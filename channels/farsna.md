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
<img src="https://cdn4.telesco.pe/file/brXB60FjS3BZY9TZbHFrX1raRACsh4KzFgryTQ7uGkFymfjfxs2WaJ3vOIX-uoplUtjIPWCtFf8EVNsWDvdPOcC6MNGN_pO2ScWWVV79AtemOhAvSLMt6faPuqZ-evioaXDdU-zI9nGHI-r40k-7cyYOXGbDZ5Yf6qVxTmGxyCN-2x_m2dEO_zgt9QhUrT8x6O39Oov0v7DqNaDlCAJKc8yHob-UEO3wRFfsW28_8k4yKFIUywn4rdiuVj2GMLayYZOzo5VizwU1ps6puqTZz5EEft_VPNghJ2jO_haEy-6mCr-CbLALCZK2HhSL2Lqfx3kZhRyifEHREvjRmgymZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.86M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-461094">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7391170a.mp4?token=uWHsxYEvcsj1J1iVxkqxAx-8Dh7SRUK0GaojpP1Vdf2jf4p22VLnCyhQo_Ay2XpRcieyDkJ7te7RWYvUnJNx9t8BS02GGWKbzoahuutdphluO3WabNgD4K2hl7QCFUlCE5VHyRZH3xX5wYvKqwocvASqrXCcygOx6GxYZlOZsGgPX-LhouCudkTSwdhDX64tXC3iii2ctJy21THxbo3aGxck4vQbOYbcu99fkHo1A7aOJViFyyD-4WhK5gYWYEkTd-WHxSc1Lib6uAasERC3vHQ28YP4p9kQrJOl2-sw9GLXqNpCMLrgjs2IrbuhffKG6CnnoVOhCAYVwTiGKkyT-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7391170a.mp4?token=uWHsxYEvcsj1J1iVxkqxAx-8Dh7SRUK0GaojpP1Vdf2jf4p22VLnCyhQo_Ay2XpRcieyDkJ7te7RWYvUnJNx9t8BS02GGWKbzoahuutdphluO3WabNgD4K2hl7QCFUlCE5VHyRZH3xX5wYvKqwocvASqrXCcygOx6GxYZlOZsGgPX-LhouCudkTSwdhDX64tXC3iii2ctJy21THxbo3aGxck4vQbOYbcu99fkHo1A7aOJViFyyD-4WhK5gYWYEkTd-WHxSc1Lib6uAasERC3vHQ28YP4p9kQrJOl2-sw9GLXqNpCMLrgjs2IrbuhffKG6CnnoVOhCAYVwTiGKkyT-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشرفت ۹۷ درصدی بخشی‌از جادهٔ الموت-قزوین-تنکابن
🔸
این طرح با طول ۱۶۴ کیلومتر، زمان سفر به شمال کشور را نصف می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 429 · <a href="https://t.me/farsna/461094" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461093">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fe26b148.mp4?token=On4e5twa0FLTBQQbPG2rwsZ0xuHjJeB1D1a5GOsD0GUak4X7PutvIB3rZk1Z9dPIlxeXxtE8JDgkHF9I_vX32Wu6QVRycbePZsGVADEOeXV5srgEm-IEeLVoxWZMsXvlhlEkox3YQpbX5SL6XVLkqxLgQsmZMFFoJOeYIahXaUt7i3rvdz-EA5lWjZYLQwSXjXYb2luF-kmLODAky-lg6QeAfJD1wN17y_3lKOfAH7obPB36LLIhsc8pWrQckKknM8efx4oAnClXOMaCOu6zA95IAzZckxDcW9JqB-ouDWamocrziKiiLSKjXspkcHa8x1WWoGqfvK4WPXKUiTtZtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fe26b148.mp4?token=On4e5twa0FLTBQQbPG2rwsZ0xuHjJeB1D1a5GOsD0GUak4X7PutvIB3rZk1Z9dPIlxeXxtE8JDgkHF9I_vX32Wu6QVRycbePZsGVADEOeXV5srgEm-IEeLVoxWZMsXvlhlEkox3YQpbX5SL6XVLkqxLgQsmZMFFoJOeYIahXaUt7i3rvdz-EA5lWjZYLQwSXjXYb2luF-kmLODAky-lg6QeAfJD1wN17y_3lKOfAH7obPB36LLIhsc8pWrQckKknM8efx4oAnClXOMaCOu6zA95IAzZckxDcW9JqB-ouDWamocrziKiiLSKjXspkcHa8x1WWoGqfvK4WPXKUiTtZtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری طرح میدان گازی پارس شمالی: به‌اندازهٔ ۲ فاز پارس جنوبی از ۱۴ چاه میدان گازی پارس شمالی، گاز تولید می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/farsna/461093" target="_blank">📅 15:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461092">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2b194c0e.mp4?token=jk4ljaSSi_eL1HSWm9t9Lj_jGSCmLNkAxUSViSscGLOebSFXLdyNBeKQA7FZnsbI5XGQ7asf643SHs6R2GLG9_xPXeoebmm1XBKKadOSrp24L4XhdMx_MFXXQAl11duWxsDbs2DgmPY9CT4vHKCSm4H73gRzy5kHJc6PFg6awBxAzK7-gHQrdG-5aPgC5QprFIQMqPX2fq6Tj-HiX9oD-G7KRxX74VAGKOCvQaAHMYX8kTXLt15QCMyS4cVyvr9kHlc9UdFxkfz0DKQO2-E09AFgq6qR_-3TL_awNQ4EfcY-Phher6LsQ0qCcZR6CENSCOwOI2oZEcJ4_8HFlBbIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2b194c0e.mp4?token=jk4ljaSSi_eL1HSWm9t9Lj_jGSCmLNkAxUSViSscGLOebSFXLdyNBeKQA7FZnsbI5XGQ7asf643SHs6R2GLG9_xPXeoebmm1XBKKadOSrp24L4XhdMx_MFXXQAl11duWxsDbs2DgmPY9CT4vHKCSm4H73gRzy5kHJc6PFg6awBxAzK7-gHQrdG-5aPgC5QprFIQMqPX2fq6Tj-HiX9oD-G7KRxX74VAGKOCvQaAHMYX8kTXLt15QCMyS4cVyvr9kHlc9UdFxkfz0DKQO2-E09AFgq6qR_-3TL_awNQ4EfcY-Phher6LsQ0qCcZR6CENSCOwOI2oZEcJ4_8HFlBbIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازار گرانفروشان لوازم‌التحریر در آستانهٔ مهر گرم شد
@Farsna</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/farsna/461092" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461091">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f256a249.mp4?token=bqx3-xAFAhJ8aT3VhP92XZ6wiB4uQB7PrIEl4sQOtkJ9gAZZ-QmRpXPCy99LJfFvOb2X3k-7Z4e0zzvLAvJBy07obEwN75CLYhqjsTa1TahZTrbcTvEX-lHNyDMxgn8Ls0Jx60FwKNY48mIkuJABy_IDBNRkXKEGdKe3seZcAfPt9jdQ-jRlOapkuA6j3G7V4z9Lo50JueXQSU_C9Qe4E7ZAIea8AAMEHTMl52HFAqVL74zJs4h85sBC9PFg-kY241Od0YLipJ2XFL-lVMNprUSRsJpq-ya-knt66ObYtD5xj1jwQMg9yxrq9PtPoUO5U8qBJQz6YidqyPRGdCN3nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f256a249.mp4?token=bqx3-xAFAhJ8aT3VhP92XZ6wiB4uQB7PrIEl4sQOtkJ9gAZZ-QmRpXPCy99LJfFvOb2X3k-7Z4e0zzvLAvJBy07obEwN75CLYhqjsTa1TahZTrbcTvEX-lHNyDMxgn8Ls0Jx60FwKNY48mIkuJABy_IDBNRkXKEGdKe3seZcAfPt9jdQ-jRlOapkuA6j3G7V4z9Lo50JueXQSU_C9Qe4E7ZAIea8AAMEHTMl52HFAqVL74zJs4h85sBC9PFg-kY241Od0YLipJ2XFL-lVMNprUSRsJpq-ya-knt66ObYtD5xj1jwQMg9yxrq9PtPoUO5U8qBJQz6YidqyPRGdCN3nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب گستردهٔ شکار زیردریایی آمریکا توسط ایران در رسانه‌های دنیا
🔹
کارولوسکی، تحلیل‌گر آمریکایی، شکار این زیردریایی پیشرفته را تحقیر آمریکا دانست.
@Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/461091" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461090">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E28sS-a_ooC6sKffZtrnGo5TjKMd68jL3msycW2j5zCmYNrJh3i-BRDVGvTpUmv-khFIDNHAIgHBU_Cib8zQp8x6VudK5JIav-Us9p_KwbGJbsu8POIJMp5gLT6zeQJWkO7QlLP4B6gsDzldNe_qTE9o4kQW929HWP45F9RTXwq_oezYcTXXP-WryuzTI2DTivDy5YEEi7pqd8IfUsGvdNKKwjPRyiwPlAB2zfNcBG9AK2tXyoLrMBySUAAJNwZFpWtRwNVWrs87Co1s_oPOMhEOav2PE_oDyzZvc61MsyJZRy5GWDSKBgJLMx561Knu1bM1yF-beoojsYFv_fnx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم
🔹
جنگ تحمیلی با بزرگ‌ترین قدرت‌های ظاهری جهان در مقاطعی به‌پایان رسیده، اما ماهیت جنگ همچنان ادامه دارد.
🔹
این جنگ برای اولین‌بار، آسیب‌های راهبردی را مستقیماً به خود آمریکا منتقل کرده و معادلات امنیتی و اقتصادی این کشور را تحت تأثیر قرار داده است.
🔹
اگر دشمن خواهان پایان این وضعیت است، باید ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد، ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند، محاصرهٔ یمن پایان یابد، ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
🔹
به‌جایی رسیده‌ایم که اگر دشمن ۲ یا ۳ هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/461090" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461089">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad5910e1c.mp4?token=ssN87vkZNl0icDGd7Hwm2JlwMe0tE2q1Z-WJ9DT_92E3v0LsRUkeYCwdO24XkWibBYwKgdlVg_Ey_V3rFO1BVA5lnUKHh9mq0d6Fclfq8h4y6qByH2_M8BbFGOHKIfYnU6QKBCqt81lIg8qO_yMnd3j51ubT4cbvIajnvWbeDk0U4h-27O4owdIjXptAurIixeoJ554ioQZL6LnQ2BUyKhObp5VWZen0AM-d2cW2ly1j6mh0dU9_TwA49JeTljt4pHIBNcfJMzEtfPCO0B0GKQouHpZ3_RKhvZzhgOTI-9HH5JrxbBPbimsU6xfr0DONI54HDA3FMxKrMPNYEEpszw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad5910e1c.mp4?token=ssN87vkZNl0icDGd7Hwm2JlwMe0tE2q1Z-WJ9DT_92E3v0LsRUkeYCwdO24XkWibBYwKgdlVg_Ey_V3rFO1BVA5lnUKHh9mq0d6Fclfq8h4y6qByH2_M8BbFGOHKIfYnU6QKBCqt81lIg8qO_yMnd3j51ubT4cbvIajnvWbeDk0U4h-27O4owdIjXptAurIixeoJ554ioQZL6LnQ2BUyKhObp5VWZen0AM-d2cW2ly1j6mh0dU9_TwA49JeTljt4pHIBNcfJMzEtfPCO0B0GKQouHpZ3_RKhvZzhgOTI-9HH5JrxbBPbimsU6xfr0DONI54HDA3FMxKrMPNYEEpszw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: ۲ شناور آمریکایی، ۸ نفتکش و ۱۰ کشتی متخلف هدف قرار گرفتند
🔹
روابط‌عمومی سپاه: نیروی دریایی قهرمان سپاه در پاسخ به تجاوز و شرارت ارتش تروریست آمریکا در حمله به ۵ نفتکش ایرانی در خلیج همیشه فارس، تعداد ۲ فروند شناور آمریکایی و تعداد ۸ نفتکش را در این…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/461089" target="_blank">📅 14:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461088">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClCSNu01Lc-PSafPyAqpecbNP6Aa7ROIfWj2CFMTGH7A1QcOZhtyUGYu5Cxzkmv6-RvD9nh_72LvMEI6iiTtTG06jCKbdj4wwsg55QO0iGA6pFuzpARY98xNimSnwsaGLcy5_PGIVbvdvNpFFYYk2iD4Jat4mRNCdNKADxdrVu6HscgvGKyXkw5V7irfA50dwzBNK3zyqIIQk4oO1dwXeHMBinWm7cCJom6AgbQ-9r-agXio7sFmixwrErdJRNYkJpKZ4_p3A3rNTBMdaKL4iXKtcELWD-WSpBkxi7PKJ8RKn16KHvQL7SnDkE0i0IPgrwgsAjNsCrBdMxWIbWkR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
گویندگی؛ هنر نفس‌ها و مکث‌ها
مهدیقلی، گوینده و مجری تلویزیون: «گویندگی فقط صدای خوب نیست؛ صدای کنترل‌شده‌ای است که با معنا و موقعیت هماهنگ شود.»
گوینده کسی است که نفس‌هایش را می‌شناسد، مکث‌ها را اندازه می‌گیرد و می‌داند هر کلمه را با چه انرژی ادا کند.
انتخاب لحن، مثل قاب‌بندی در عکاسی است؛ بعضی کلمات را برجسته می‌کنی و بعضی را آرام می‌گویی تا مفهوم درست به گوش برسد.
📢
دانشکده رسانه خبرگزاری فارس، تو را به دنیای حرفه‌ای گویندگی می‌برد.
آموزش همراه با تجربه‌ی عملی در باشگاه خبرنگاران «توانا».
🔹
بدون کنکور | مدرک معتبر | اساتید باتجربه | معرفی به بازار کار
⚠️
ظرفیت محدود
📲
عدد ۱۴ را به ۵۰۰۰۱۰۱۴ ارسال کن
🌐
یا ثبت‌نام در:
futurix.ir/go/rxDxXO
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/461088" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461087">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cebd3b25.mp4?token=KTZKC-06NifEq29LT6oS0McBAebiBsotkuaXo_M_82XrMDn0BanTdnU0wQ4eVRydTYgax58V1oxipUvbTX3TQg--KTkO5uv6iaLRYdLCjLP_fLt8jOC64Ayk2ArcdWZomE-c5Hd4oiQ9ci9lhCEFgmUT6j0RCrAPG8gNjK2TrWGvrR2X1_aQZiGcfJa8AO1iUjvL4ocWdqX02wcXRqq8q7Y0PGuPNLtOy9lgZd-YAl9PhSE44UF6c8l8kPMZ7YKTX5ZzPL9JSe8Cpt0iBEQNZ77zdIhzR-dgEe9QcVR0_r05l_Bg_QwORaurRTsGNL9wFVCG13fPBVC92PQHLfbvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cebd3b25.mp4?token=KTZKC-06NifEq29LT6oS0McBAebiBsotkuaXo_M_82XrMDn0BanTdnU0wQ4eVRydTYgax58V1oxipUvbTX3TQg--KTkO5uv6iaLRYdLCjLP_fLt8jOC64Ayk2ArcdWZomE-c5Hd4oiQ9ci9lhCEFgmUT6j0RCrAPG8gNjK2TrWGvrR2X1_aQZiGcfJa8AO1iUjvL4ocWdqX02wcXRqq8q7Y0PGuPNLtOy9lgZd-YAl9PhSE44UF6c8l8kPMZ7YKTX5ZzPL9JSe8Cpt0iBEQNZ77zdIhzR-dgEe9QcVR0_r05l_Bg_QwORaurRTsGNL9wFVCG13fPBVC92PQHLfbvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: هر کشتی که از منطقهٔ ممنوعهٔ تنگهٔ هرمز عبور کند تحریم می‌شود
🔹
در صورت عبور هر شناوری از محدودهٔ تحریمی تنگهٔ هرمز که مختصات دقیق آن اعلام خواهد شد، ارائهٔ هرگونه خدمات دریایی، بیمه‌ای و پشتیبانی به آن شناور متوقف می‌شود؛ به‌گونه‌ای که حتی در صورت تردد بعدی در تنگهٔ هرمز نیز از دریافت این خدمات محروم خواهد شد.
🔹
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/461087" target="_blank">📅 14:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461085">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lX_cF-ErM-khMGrg__n0x7hPLiFSJGZ5E8xzq59Kn3D7PO-GVOSpmPw16tYTf8EdpmSvtfCPZ3yLXP-v5uf2LEP7T4g75SAxt2AxEO5gQPgNRK5HdLW5RRbyRiXQSqnEi7Q6lUyS1Gtm9BcKgsRla6KY7bk5r9w3rJD-PdZfJjEbzon7N-pLVX4GNvGLVD-vcUiKGDi6GZ7M9tImc3UxGVLFWvXvT4GHp0R7Q-iN5RZlL-2mhzXHkd92fcZ-IolT_N85_lF8I-04tDgUHSWx8iM7JgBppXr19y3HFnOic3Y7wk_-N66y4vPZWR47Szmjj0O4SqXD16oXwjw_T0SeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FaX1_Us3G_7Nuw6-EseG1mFw9_U31Wx-WGkYdDNLX_-RHlgjPE3ij8kT2OjGFreSYDn0saKWAdIuBi6zh0swsxooqirt49zy2M8HEYHWmzawMEK7L8m0-AyBfuomAygOXo5l-Iz3uw4fTqxO7uSI4d6xsdoyrgNWpdGVeeC_RK8jKhR92SR_TUwUPgu3cknVyD54xmz7JOkrqPaaIHZmh1gyCpwuQYjcOSPnbA-9PnwKa0ZrX48AmabUwqherEk8zc53lo3gUeoPeTeWJ9PVSfh9Q-QQOL-OON8zdzg4WOEq_NdbVXYPN-sGrr5tyhJCKuVLNoZkTXBFSRQBi4pwXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما با کره‌جنوبی روابط خوبی داشته‌ایم اما هر مشارکتی در اقدامات تجاوزکارانهٔ آمریکا برابر با هم‌دستی در تجاوز خواهد بود.  @Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/461085" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461084">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrO8iXxOyWNbmhl8vh6jzb4Xc5PJqIoZSfWpTkzGCCvbCYaJYnNIXixLCveDr_nGhVAo2A2lxG2pPNuBofKsTszI6ye04V_Wc-pW1i6VcIQywgE893H9ScTUMpi26sEThWcY_fF3KRGy8RpQQWelRhjllxCyz4ahItEkx3P3-OzKorA4KMFi2wsm-Cai9PjxHdCIQnxKckBNWMKL9CK37MLUFHEFvGAFAZUGP97JS00-uDF2NocxV5TxGWaQY7ykfR-4N0GW4ZVg8NKevUYV9z2rpYyIW0B7na-a_neAQ2C7OY1OYpyhUVsRZLNz1wRoc3AyJdvEYTi4SfGu1prp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نرخ سوم بنزین رسما ۱۰ هزار تومان شد
🔸
از راس ساعت ۰۰:۰۰ بامداد ۱۷ شهریور، نرخ سوخت سهمیۀ جایگاه‌ها از ۵ هزار تومان به ۱۰ هزار تومان افزایش یافت.
🔹
نرخ ۱۵۰۰ تومانی سهمیۀ اول و ۳۰۰۰ تومانی سهمیۀ دوم تغییر نکرده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/461084" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461083">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6mqYma6l-gSUi9P-Ys4tR30P2rzTo9KvSoWN5DNfxiHcvy1gTFuRkGlgNM-XAZlQQhKjvIIHr_65xBGY1zcbjX-yIuiPjTJ_6GAcGs7SXKp23eEQMQ2s5tBN_BaH8nlZ5rBKPh_Dil7ohdM3dP6FfYAZR_r8c-9Q5rizck0CC1frRG-wyxqiyxY1sfJVqEj_oEtUnR9mg65ARqrzKl9YmQ62Jrv1lNfhnxcvdeN3gsCww8NBRJEKAx7iLIha6PKM564FuUVejCS5_5aVdL1VKGeDgvpVmfcDSpG7IeAp1kgOvoK5_2GCH5Xv0zI7aQA5Tn3gx7Lklk7urM_m9cF7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: ۲ شناور آمریکایی، ۸ نفتکش و ۱۰ کشتی متخلف هدف قرار گرفتند
🔹
روابط‌عمومی سپاه: نیروی دریایی قهرمان سپاه در پاسخ به تجاوز و شرارت ارتش تروریست آمریکا در حمله به ۵ نفتکش ایرانی در خلیج همیشه فارس، تعداد ۲ فروند شناور آمریکایی و تعداد ۸ نفتکش را در این…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/461083" target="_blank">📅 14:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461082">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81ccdbf695.mp4?token=gxk_ggnVi59MEKBlry18orkcmDztGwsAYupLf22h7xGB4tN9DaPB2cbIj5kHE7i6D-82NvEy-nwzh4Jj1qFHf4qj-ifwZtrvdTPaoywHLMMtx8K-4z-dsgavWk-pO71RyaMRJImjQyUs7DVE0-8lVLZh6mCs22-rJtQuAVX1xv9LVplZ8xfp0w20cS430GsE1TC2rrwz_Gfhl0pPx-j-tqlOnOAKz6xc2DYIWi2frIeaFnM_p4QFSHUzzVL9k4Ba3NkU4sXlt9w_9_hKPTIQXKQWvukNyqWVh1LzEwmxizozZVt2i_OljyI2sIlwszSdazm3s4UfrMZ_KOgzShEdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81ccdbf695.mp4?token=gxk_ggnVi59MEKBlry18orkcmDztGwsAYupLf22h7xGB4tN9DaPB2cbIj5kHE7i6D-82NvEy-nwzh4Jj1qFHf4qj-ifwZtrvdTPaoywHLMMtx8K-4z-dsgavWk-pO71RyaMRJImjQyUs7DVE0-8lVLZh6mCs22-rJtQuAVX1xv9LVplZ8xfp0w20cS430GsE1TC2rrwz_Gfhl0pPx-j-tqlOnOAKz6xc2DYIWi2frIeaFnM_p4QFSHUzzVL9k4Ba3NkU4sXlt9w_9_hKPTIQXKQWvukNyqWVh1LzEwmxizozZVt2i_OljyI2sIlwszSdazm3s4UfrMZ_KOgzShEdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوشحالیِ مردم از شکار زیردریایی آمریکا توسط سپاه  @Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/461082" target="_blank">📅 13:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461081">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سپاه استان تهران: صدایی که دقایقی پیش در ملارد شنیده شد، ناشی‌از خنثی‌سازی مهمات بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/461081" target="_blank">📅 13:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461080">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">پاداش جام جهانی برای هیئت‌رئیسه گران تمام شد
خبری از نام تاج نیست
🔹
«شکایت سازمان بازرسی از برخی مدیران فدراسیون فوتبال ظاهراً در دادسرا منجر به صدور کیفرخواست شده و این تصمیم قضایی مقدماتی است». رئیس دپارتمان حقوقی فدراسیون این را چهارشنبه ظهر گفته.
🔹
برخی فعالان رسانه چهارشنبه مدعی شده‌اند در «پرونده فساد فوتبال» نام مهدی تاج، رئیس فدراسیون هم در این کیفرخواست آمده.
🔹
بااین‌حال پیگیری خبرنگار فارس نشان می‌دهد موضوع شکایت سازمان بازرسی کل کشور پاداش ۲۰ هزاردلاری به اعضای هیئت‌رئیسه فدراسیون پس از برد برابر ولز در جام جهانی ۲۰۲۲ قطر است و مهدی تاج، منصور قنبرزاده، احمدرضا براتی، بهرام رضاییان و میرشاد ماجدی از دریافت این مبلغ خودداری کردند یا همان زمان آن را برگرداندند
🔹
مهدی محمد نبی، طهمورث حیدری، احسان اصولی و خداداد افشاریان دیگر اعضای هیئت‌رئیسه در آن زمان بودند.
🔹
حالا رئیس دپارتمان حقوقی فدراسیون مدعی شده تشریفات اداری پرداخت پاداش در آن زمان به‌دقت انجام شد. دیوان محاسبات این موضوع را بررسی کرده و اقناع شده و تخلفی را احراز نکرده است.
@Sportfars</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/461080" target="_blank">📅 13:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461079">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-dhLPVetX12KraZ0hn-IUfFB9GPUZZVQr2WDFyq7bpYF-Sdisozm_Iq0d2h4Z8xxyOMXo0vp6eHptykuVF1jwgEhEQLF2H4BwowHrMz8p9FGSrFwoP9ledIjrTRFGQNEye9TLZ-2z0Z9rJJpQtUw2NHW-kEDucEtQ7xz0AqT50MWSZBfQUypUuHZqTPK1urhVO3ZrOrtEyEk6eW2sEpuZAdgCf_zWjKa3ZRi6uAhseomIGWIHqv9SBKcvFSZIlDg1wZYsOu0exG-d0tf6oM87WKrAG4kFRHqAPA2SBosK6LDlyh_mEGcnqHCCiUyV0Z8sIenh7nvvGnjpYQ9vsIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی شاگردان پیاتزا مقابل چشم‌بادامی‌ها
🔹
تیم ملی والیبال کشورمان در آخرین مسابقهٔ مرحلهٔ گروهی مسابقات قهرمانی آسیا با نتیجه ۳ بر یک مقابل چین به برتری رسید و به‌عنوان صدرنشین راهی مرحلهٔ حذفی شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/461079" target="_blank">📅 13:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrazUUi3DJdQqEJGu7O8oPy4Y7t3lwKdiPzkrnGDLDy7zkDLNz-nKEh1He_hFhKVqR8QlWOj6R6jr0zuIQCuk8e0ksoUeWHSnMKX0xcw5OywRQzxHgI9_nVnUmBIZWD4rBo43abJpqNP-FpRpQeL4xDSmlW_12dd2pwlqPG4CfcihczTk2nrcIMLvkAifWWP-CgMVkOcT-RhzRjRuikC_a-lkqJg9GFVsGGRlF8pzpASN0lNEngsZV8MHr9iSJELE4RSG9c8iSN3ymYzdvWqJFr0YWc3ZNdaaf1IaL2imBefO_GGn9r6Px9Ubk0bykDPb5AFydT9pk4mT4fi8p8vxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش‌ها از هدف‌قرار‌گرفتن چندین کشتی در خلیج فارس
🔹
سازمان تجارت دریایی انگلیس: چند کشتی تجاری در شمال خلیج فارس و دریای عمان در جریان فعالیت‌های نظامی منطقه هدف شلیک قرار گرفته و از کار افتاده‌اند.
🔹
همچنین یک شناور لنگرانداخته در ۲۴ مایل دریایی شمال غربی بندر راشد امارات، احتمالاً پس از اصابت پرتابه‌ای ناشناس و ورود آب دچار کج‌شدگی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/461078" target="_blank">📅 13:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e1466598.mp4?token=AapEv4YFg3AFQev7fE91ml0PfCOmmQIPa1iasiHU6On9uCOJjV-8sGbU3QT10bTS4w-UkJAOjhGi4pU7d0YBXT2U3iM0Mix-WItWDN1qkLHlt1pZ_prMybqrPDRaf-C7xomAQQDoOyM36OkGjaSpaqRHBHIu_JpJmgKBF6fn0xRlT7k0F-c8WiV_2ldsMfLlaiWnW3xkU681_X0KYx6IJzQobRKPhlf1OYy99ZDHAQTHr4DoXiKanY6-nQyhg4r200NphWmRmq6Rju4in2itNalUAsE2ZOAmWZe7npasoMBCsa-Ya5mgGyuviTBhP71TfRVwtSwsCKdfBMPyV-O7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e1466598.mp4?token=AapEv4YFg3AFQev7fE91ml0PfCOmmQIPa1iasiHU6On9uCOJjV-8sGbU3QT10bTS4w-UkJAOjhGi4pU7d0YBXT2U3iM0Mix-WItWDN1qkLHlt1pZ_prMybqrPDRaf-C7xomAQQDoOyM36OkGjaSpaqRHBHIu_JpJmgKBF6fn0xRlT7k0F-c8WiV_2ldsMfLlaiWnW3xkU681_X0KYx6IJzQobRKPhlf1OYy99ZDHAQTHr4DoXiKanY6-nQyhg4r200NphWmRmq6Rju4in2itNalUAsE2ZOAmWZe7npasoMBCsa-Ya5mgGyuviTBhP71TfRVwtSwsCKdfBMPyV-O7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی امید راهی بازی‌های آسیایی ناگویا شد
⚽️
از میان ۲۳ بازیکنی که عبدی، سرمربی تیم امید از آن‌ها دعوت کرده فعلا تنها ۱۵ بازیکن در کنار تیم حضور دارند.
🔸
استقلال و تراکتور فعلا از تحویل بازیکن به تیم ملی امید خودداری کرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/461077" target="_blank">📅 13:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461075">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPyQvhSXY7eGF-Pwa84M6hFpzF_bZMMxWi8xFhLiHOpxgldAMXpPKD_uQqWGYngr6dYjdKGUmNXyDpMvN8PxUMCcpmXh-t_b97X1_6PTE6vEHfl6VS6xdr4cNpBAH4vGVRG_3836PxsB7p26TRqvyzI0XfZkqVtQD3Pfhu1guDjXhOf0gyllBXMA-8unw-selcm1XNjc95XPRgEl0zRGc2V8c8a0pbv342QX2ZqsAY1HPJQ55dro7zP8BmzJozpvFWpD4siOQFNNnRqQAIBOJUfhgc1OtSZLgrokZgsN_9HPGq_8kdj4WmTVIDNUR3TrUd5MUw1lYtAR4MmWzlBqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه عجیب ترامپ به دستیار زن خود؛ ۴۵ هزار دلار نقد!
🔹
هدیه کریسمس دونالد ترامپ به یکی از نزدیک‌ترین دستیارانش خبرساز شده است؛ رئیس‌جمهور آمریکا ۴۵ هزار دلار پول نقد به ناتالی هارپ پرداخت کرده؛ رقمی که تقریباً یک‌سوم حقوق سالانه اوست.
🔹
این مبلغ در اسناد افشای مالی کاخ سفید فاش شده است؛ اسنادی که نشان می‌دهد ترامپ در مجموع به چهار نفر از کارکنان نزدیک خود ده‌ها هزار دلار هدیه نقدی داده است.
🔸
هارپ ۳۵ ساله از نزدیک‌ترین دستیاران ترامپ محسوب می‌شود و تقریباً همواره در کنار رئیس‌جمهور دیده می‌شود. او به دلیل اینکه معمولاً یک چاپگر قابل‌حمل همراه خود دارد و مطالب رسانه‌ای مطلوب ترامپ و پست‌های شبکه‌های اجتماعی را برای او چاپ می‌کند، به لقب «چاپگر انسانی» معروف شده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/461075" target="_blank">📅 12:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461074">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaBerpwsfndxgC4uCtif_voPc41xia51BDE2yD6ekMZpfzIAQktbha5bMJ1VNHJw8a_ltuJCvZQUI7HIFhFgyPfa8GzuDdsh2A2kGLVLfq35onZ4UGS60cwpKxPL8KR07TUcga2oS6Yba3hCeT-fvuoQndWv-3r_1n8bhPJrqHEo_qtpl95QNe28vQWFpB1Gm7UmW9F3rpKZRTlv5r6-TP4YMWSU0Vo7zKGonbjbhWRS3xUwP3taOotMpLLh6XxpQvee7o1cR_MZRAPpJw-ug_w1nt31ExNhmL-FA5QVvCGSVOZJSEj4MrGxMVgXf8mZSW9dL44Mx9vMDmQ5KO7uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس همچنان رکورد می‌زند
🔹
شاخص کل بورس در پایان معاملات امروز با افزایش ۴۷ هزار واحدی به ۷ میلیون و ۱۲۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461074" target="_blank">📅 12:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461073">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE0zAHYu8y-XJREzOQRechHuZ25cybRv1EovkAaRTNIeVytWqDKPZ3qkkZM12Zz3FCkgvO7t3vr_PSVdd6G1J-6_xIqTaWOnD3ilwSBrRAs5XXzJoazjcjvGK-fKPKr84ZGbBSEH7vdWLmVVhf6Z8DvjT2abYROK3oQeF4LpnobCf88AxXvMelLBn1QF9BtfuHAF47Gpmyc6soDuIV2G6z86b_jHkpVccZcqhLaN1O5FB-lW2DEMaNDu_LuYhSE-adx8ZlEy-qYn1wrScLNijdK8VZoJ5hpPREjHTBlf-77YNHbl6WOWoxinY8dhtfd47iFEhsbcWKC06I5Z4tLwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک بسیجی توسط گروهک‌های تجزیه‌طلب کردی
🔹
سپاه آذربایجان‌غربی: ماموستا محمدنزهتی که سوابق طولانی با بسیج اساتید، طلاب و روحانیون داشت، توسط گروهک‌های تجزیه‌طلب صهیونیستی-آمریکایی به‌شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461073" target="_blank">📅 11:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461072">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfLl-6pHKFlu_zM4Fj14y6VZZ3azrkXXGNRL3J07SD9PFoGKDANs5qYOaahKVoVXMJStD324MZsSV5cDuroozU3flGpDknkiQ8FroqTbyEmUcJEjGyQHbEvG2GTB6zThnPNi9gnmE6ueU8ENIfA9vDcae_Qo2DrRoNphSWZ4fBNxfkbtg7PMYQ_6V3RpVs0LR3dmVU9yn7fLTjcsfe1Z22Tjl6iQkspgsoLp2Y7Ujfg3cnBX8ZgoSvvqjMY2o_0sQgVVVy7HbDbUgSWjGqtfE5kHZfxkZCw_apZ3RLydauQSSyE_yMKZg2wOWwNNYadNCUx_vxnw8zL8obx2iSas3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۵۶ کيلو مواد مخدر در سیستان‌وبلوچستان
🔹
فرمانده انتظامی سیستان‌وبلوچستان: در چند عمليات ۲۰۰ کیلوگرم تریاک و ۱۵۶ کیلوگرم شیشه کشف شد؛ در این راستا ۱۱ خودرو توقیف و ۱۰ نفر دستگیر شدند.
عکس: مجتبی گرجی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461072" target="_blank">📅 11:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461071">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZmUrwT-h4_CD5E5lVHfqLorDgdFX68vtE5O-vHIuuDGTMzgjCtG12PVrOl_FYZLCyZz2tYqTK0VuHIq2HU4F8dNo33vgtIIHCp8rwOojfrm65VkmNmhKI-PTz2iR94KSSNj_lxDt7QTEwMjs6bgupDuKGUL0CuDCueLvQm6tvMq85pVSbEivfGspVnakWd1nfRFjC4YmzcithskT4KIH8ILlrd8YStnQU3N08tkZgz9eD5vX67R6nGG4-7vCvzZp3S2QRdY54crIANwuALb8BHxPLuyw2SCFFwCzfEcxQCCFc6gJoObt8J-F8c2iK284MLdr5xmbFf2pywiRXutkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ آمریکایی: وقت اخراج هگزث رسیده
🔹
نشریهٔ آمریکایی سالون با اشاره به استعفای وزیر ارتش آمریکا و انتقادهای فزاینده از عملکرد وزیر جنگ ترامپ، هشدار داد: «وقت آن رسیده که ترامپ، هگزث را اخراج کند».
🔹
یکی از صریح‌ترین انتقادها از عملکرد هگزث از سوی تام تیلیس، سناتور جمهوری‌خواه مطرح شده که نوشت: «من هرگز چنین مدیریت نالایقی را ندیده‌ام.»
🔹
این سناتور جمهوری‌خواه اقدامات مدیریتی هگزث را در بهترین حالت «کار آماتوری» و در بدترین حالت «مرگبار» توصیف کرده و پیش‌تر هم خواستار برکناری وزیر دفاع شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461071" target="_blank">📅 11:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461070">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec5df6375.mp4?token=rhh8XID0zngXbBcl5ayDoe3tc3kAQj7x1Wrh_E2XrCHX_uTjXhBzQHv8njYc793sNOKkAXfZkPTOAYpWhR-VixUzHoftu3tW_TbBpHDmPapnsgvKEuIQZofpmMw19zfBzdLcI4P9qSfWMMPYwkzxS4Rdb-BxmIM95-54hoqUJztvyX1ws0kpXjSYW3TjFYvOEh-P_ueQDJPnI90XC1JctFbCREdvDfp7AMUIpA9qCULo2ZCsbYbUElYlKgMl8pGA9CFSR-QUGUrQ2DvYTB5vdsCgX2vm8ND2NLejB6N5zSOpD7iBYyfZ8lgG2qPCid6PmizYk_5xW-cM3Ekks-LLzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec5df6375.mp4?token=rhh8XID0zngXbBcl5ayDoe3tc3kAQj7x1Wrh_E2XrCHX_uTjXhBzQHv8njYc793sNOKkAXfZkPTOAYpWhR-VixUzHoftu3tW_TbBpHDmPapnsgvKEuIQZofpmMw19zfBzdLcI4P9qSfWMMPYwkzxS4Rdb-BxmIM95-54hoqUJztvyX1ws0kpXjSYW3TjFYvOEh-P_ueQDJPnI90XC1JctFbCREdvDfp7AMUIpA9qCULo2ZCsbYbUElYlKgMl8pGA9CFSR-QUGUrQ2DvYTB5vdsCgX2vm8ND2NLejB6N5zSOpD7iBYyfZ8lgG2qPCid6PmizYk_5xW-cM3Ekks-LLzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بسیج اساتید: از ما نخواهید که بسیج ساکت باشد
🔹
هر مسئول اجرایی که در راستای اهداف انقلاب حرکت کند، باید بسیج را «نِعمَ‌العَون» بداند؛ ما حاضریم برای مسئولی که در راستای اهداف نظام حرکت می‌کند، پادویی کنیم و به او کمک کنیم، اما اگر مسئولی در این مسیر حرکت…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461070" target="_blank">📅 11:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461069">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49cc49bb7.mp4?token=a5De2eo5lhh13MFbkPAUzaa_Bee5okUrFeXNlWnFYQAoyO_VGnhsnc8cd6qZSo5UjD5R4Q1_BcPG9-Vjer0gXri8mDvZ01y7rY1bPvC2Bf_Xb9eXk9DxO-w2Q7EjyAXOGB1ydJXIYfZ_QTuUxGQoPEpXiNFNUKr8Psup_AJGF_kP6iSniYjObqhp0Xh9Vf_298TXXhMfM3WFW64LPnvKP1oyDuQOouJzN5vrOVWq4q_Wf-9xcepH7cA8I8XXPEEhxlxN3HhNGGL7gM4gvFtZMdrEAIET0eIW7VSa_eLP4ELbkgOOcvadWO-i3jcraGhCsgBWPJYtExZcUhPZnNgtHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49cc49bb7.mp4?token=a5De2eo5lhh13MFbkPAUzaa_Bee5okUrFeXNlWnFYQAoyO_VGnhsnc8cd6qZSo5UjD5R4Q1_BcPG9-Vjer0gXri8mDvZ01y7rY1bPvC2Bf_Xb9eXk9DxO-w2Q7EjyAXOGB1ydJXIYfZ_QTuUxGQoPEpXiNFNUKr8Psup_AJGF_kP6iSniYjObqhp0Xh9Vf_298TXXhMfM3WFW64LPnvKP1oyDuQOouJzN5vrOVWq4q_Wf-9xcepH7cA8I8XXPEEhxlxN3HhNGGL7gM4gvFtZMdrEAIET0eIW7VSa_eLP4ELbkgOOcvadWO-i3jcraGhCsgBWPJYtExZcUhPZnNgtHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مالکان
ماینرهای غیرمجاز یک سال برق یارانه‌ای ندارند
🔹
مدیرعامل توانیر: با دستور وزیر نیرو از ۴ شهریور امسال، دارندگان دستگاه‌های غیرمجاز استخراج رمزارز تا یک سال از برق یارانه‌ای محروم و تعرفۀ برق آنها تا یک سال با هزینۀ واقعی برق محاسبه می‌شود.
🔹
مردم قبل از نقل‌وانتقال به واحدهای مسکونی و صنعتی جدید از شرکت‌های توزیع برق استعلام بگیرند که برق آن واحد به‌دلیل کشف رمزارز غیرمجاز غیریارانه‌ای نشده باشد.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/461069" target="_blank">📅 11:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461068">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp2UvO76kp-bJlNIjfdKlxquKNEP9uFbRkklJLwS3LKQI4YkJsexTLBkcNQJz4EA_VNtzs04mYzbXRouoL72AVAW6CjPs2zdJD2CTcJytIkP1QsVt6GK2BFBdBSASSN6Gk-0Lze6n_kFO3tWMlGpeKbN5dassWpRmHufbhELqb5aCSOUJVl2IkLbrilCewJOiC7iNE1wsLfJjCUb6oeFg-kPVjkjH20Z2HtozWmNaoXMBwc4g9_Iz3NevKLRUruvixL9S1rONQRIxhXkrYCmWawJ3pQaNbhn-6fTBGM7OR2f8rrfLmotD5STP8cLWtv_D7mLTzv13I8ZxJ2pU3UIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیر بانوی ایرانی، طلای هند را شکار کرد
🥇
در ادامه مسابقات سری جهانی پاراتیروکمان ۲۰۲۶ هند، امروز چهارشنبه هجدهم شهریورماه، سمیه رحیمی در فینال ریکرو انفرادی بانوان به مصاف حریفی از چین رفت و با نتیجه ۶ بر ۲ به پیروزی رسید و با ایستادن در جایگاه نخست مسابقات عنوان قهرمانی و مدال طلا این رقابت‌ها را از آن خود کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/461068" target="_blank">📅 11:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461067">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA4JoM7453qBrKsfxQYyeezbkQLxzc--SBF9LxWCgZsn7XkYnfOo41-O14qwwS7GgkunEnwJVucdcffp77oheyOZZxgvzOu1kesCKONUYnZr2Os9Ds7QnLrTXgbsJA6SOigEkkoZhYn74pQKV6cfmxTNT6Y5UdOKu3lwc9hm1LfzzzWA3lmjuBxVvpyxt5313RbGdPEkCnqppA7_aGRU4IW6qrU-GHsWUNXfQVkwCj785M0M2b_tBAFFZS7pAE3ino4Ay9rfk68mwRzku3feBXmNt-kEApDkVcKLWN5sQkrRoIneBzTgDRQR9PGvO4QykYIXuVi3OI0xX99mSeFGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت نفت برنت به ۱۰۰ دلار رسید
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461067" target="_blank">📅 10:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461066">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19139f9901.mp4?token=lPh3a3ccJ3avq4am4gnn9evoOxvTzpaU7mmqsxf_Q1t00Zd6Cls_-Q9jG-V5_P2sPGvOhvzE78GxUaymvjkDGHpToO0NmAr0XXa9gNLuCTOFA7W3eoBiqV2KIvAnManyCFgr28sLntTq9R-zix6Tz6pd3g2NggZkHU6QCmNcgwiqNTCmwihuIpEpttqsBY0zH8fXfTwi0AQZI9Fy2IEk3syxoXbf4QZx5r92W3r3XHJRnpyykL1YmhLwsWGzaVH3_TUSRa5eBMxv3hv2tQ9Lr7VNyEJ_3xTnXYUaqvyVvVWWoRPGVrI_19b7FqNNg7HTxoKEUpIeIlqIZYT2C257IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19139f9901.mp4?token=lPh3a3ccJ3avq4am4gnn9evoOxvTzpaU7mmqsxf_Q1t00Zd6Cls_-Q9jG-V5_P2sPGvOhvzE78GxUaymvjkDGHpToO0NmAr0XXa9gNLuCTOFA7W3eoBiqV2KIvAnManyCFgr28sLntTq9R-zix6Tz6pd3g2NggZkHU6QCmNcgwiqNTCmwihuIpEpttqsBY0zH8fXfTwi0AQZI9Fy2IEk3syxoXbf4QZx5r92W3r3XHJRnpyykL1YmhLwsWGzaVH3_TUSRa5eBMxv3hv2tQ9Lr7VNyEJ_3xTnXYUaqvyVvVWWoRPGVrI_19b7FqNNg7HTxoKEUpIeIlqIZYT2C257IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ انفجار تانکر سوخت در سنندج  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461066" target="_blank">📅 10:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461065">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجار کنترل‌شده در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461065" target="_blank">📅 10:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461064">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxkDQl10KNVzVcxDoMvQyIN-Jex83ipXJQiJ9ARM29JBALUdddvpt4bkiIoJbWMNu8O58NumS5Fq4PRZ41MLduUhtpRjk1Y7XFl1-xf3uYwQjHuD7FI4tuz1gCXd83aHHxWmpDj_wnKJYu9rhXmjjHbf4yY72T3yaGn6YYMOCDuaqJYNGirpd3TUXpI64lLbrCeEG1qkRWSkg3l3xIIOO1VxitIn1pHbt4EC1j5HNFEnGm942rXxZhsCGsb3JPlNFYsfjuP_JdPiGHjURULwaqn3ei2nw-435iIR4zlPZuII52wSZNrUObwpksIxVlIzcK23wOxauljisXYK6C4G9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار اراک با ۸ رای موافق شورای‌شهر برکنار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461064" target="_blank">📅 10:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461063">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAd-0efagcS0-tdECOg-6rtDBPQsQQZu5EdvntQUbFrYx6JY7C4ofZFH7qufoeDU9uxZ9VGMyu6L27xNKm6U4TRPtIMMW5sXFl087aS28L6-ZUvOhyfZSvQuJ_nTDaCNZvM6eNyx5twhqxAQW-fvXDvBXvEDE3wJl2fc3HH3ZD_95wX0pqFkMuKi7tZAxHKPbUB2pU83SYGwx-oYM4bxwzxpMvpwpaL1IDFeNw1hmEhYDwsXm3vt88QaqTt1_cGKmsGasvE-PDnsRBL_lLkPlW8ykL5YdGDxRt4kynwjQoDf0S7TNKSGWHzl3TdRb3tfxlI00KKvSDjAUlgbKwKDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازندهٔ چت‌جی‌پی‌تی معمای ۱۰۰ ساله را حل کرد
🔹
شرکت OpenAI، سازنده ChatGPT، مدعی حل مسئلهٔ مشهور  ریاضیات «ناویر–استوکس» یک قرن حل‌نشده باقی مانده بود، شده است.
🔹
این شرکت می‌گوید حدود ۱۰ هزار عامل هوش مصنوعی به‌طور هم‌زمان روی این مسئله کار کردند و در ۸۸ ساعت به راه‌حل رسیدند.
🔹
با این حال، این ادعا با واکنش و تردید برخی پژوهشگران روبه‌رو شده و دربارهٔ دسترسی احتمالی OpenAI به تحقیقات مشابه نیز بحث‌هایی مطرح شده است.
🔹
برای حل این مسئلهٔ ریاضی یک میلیون دلار جایزه در نظر گرفته شده بود که OpenAI اعلام کرده قصد دریافت این جایزه را ندارد.
🔸
این مسئله دربارهٔ معادلاتی است که حرکت سیالاتی مثل آب‌وهوا را توصیف می‌کنند؛ معمای اصلی این است که آیا حرکت یک سیال می‌تواند در شرایط خاص به وضعیتی برسد که سرعت آن در یک نقطه بی‌نهایت یا غیرقابل‌کنترل شود یا نه.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461063" target="_blank">📅 10:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461062">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی از هفتهٔ آینده
🔹
رئیس‌ بانک مرکزی: ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی با هدف جذب منابع ارزی، تأمین مالی پروژه‌های ارزآور و توسعهٔ ابزارهای مالی ارزی از هفتهٔ آینده آغاز خواهد شد.
🔹
براساس این طرح، دارندگان ارز می‌توانند بدون تبدیل ارز به ریال، منابع خود را در صندوق سرمایه‌گذاری کنند و واحدهای ارزی دریافت کنند.
🔹
سرمایه‌گذاران هنگام خروج نیز معادل ارزش سرمایهٔ خود را به‌صورت ارزی دریافت خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461062" target="_blank">📅 10:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461061">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5425e82eed.mp4?token=AbuNoWSm-dOpoYcB_5H3FdjyebO98pnlNVsH4eJBxIXxjkE0sHCGDdv5j2kY_ALN4aX-tZChRhOeZfg5LQThGy9jf2po_4y9dtMvBZpi64lc5Wwj2uF2Y654xmfcWq8JtVUozOpJWJZXUrwy4OQWUNkhu3zpsDcqSqxDtnVYfc0EhcJjxB7qhGRjoMZDFqheHlMgSifOk7gJwX6NoLFCqVbXKp3i0mM8K8QT23b49gqKAwKHxnjPKjwiHik2s3Ln1mS80bT1J26LuzMK9etPOONw8qXxsvxDPxXsBnmuMbqcrf9YGaTcs3qRKqSpOdAaeUGAMsG5AXHa_weKQ_TZXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5425e82eed.mp4?token=AbuNoWSm-dOpoYcB_5H3FdjyebO98pnlNVsH4eJBxIXxjkE0sHCGDdv5j2kY_ALN4aX-tZChRhOeZfg5LQThGy9jf2po_4y9dtMvBZpi64lc5Wwj2uF2Y654xmfcWq8JtVUozOpJWJZXUrwy4OQWUNkhu3zpsDcqSqxDtnVYfc0EhcJjxB7qhGRjoMZDFqheHlMgSifOk7gJwX6NoLFCqVbXKp3i0mM8K8QT23b49gqKAwKHxnjPKjwiHik2s3Ln1mS80bT1J26LuzMK9etPOONw8qXxsvxDPxXsBnmuMbqcrf9YGaTcs3qRKqSpOdAaeUGAMsG5AXHa_weKQ_TZXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام اشتغال‌زایی ۲ میلیاردی برای جوانان بیکار
🔹
مدیرکل طرح‌های ملی وزارت ورزش: جوانان ۱۸ تا ۴۰ ساله دارای ایده در حوزۀ تولید و خدمات، برای وام با سود ۱۵ درصد می‌توانند از طریق پنجره‌واحد دولت الکترونیک یا سامانۀ جوان‌پلاس ثبت‌نام کنند..
🔹
اعتبار از محل وجوه…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461061" target="_blank">📅 10:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461056">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaFP0nJB4j-_nbH4wPmjvmF_LFOxF82zPupyxG0ao1t-KWS41Q83KYtlcIQhphjVLCub2mtfq9m3ROD-_UVWnzNM-O46A5Mvfi3mt69DFISwDON9z7qfpLlzySryzX2HwbbPxRO-eNkqORAaRPgy07P_5LgDEi9cDRzRHoHYCI1OVXH0si27PuawvWh6G3j-AYCQzniKJDzIKhcvh8lNiwORhnix4sMPNpPuCy2Ws4pgf8GNBRoD9dKGa2OzKVaKMjWkJUdTu_FqKyia6hGhtB9Sq1SErsKAs0o-hJSJxbeKpIbKGClIODjp0u3QYnjECf75_Y_eTOg_lR7ybuEUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQT5VeVcfxsP2LyvtxoqHMgeRBPOSVUkgl9up_62LuY1tkl7HhpOK8-AUYpHdwV6CDBrgpapCgw7XUmfxrua3NUEknsS4TNUkgMpt_03ZvhAmoCGPj4o2gUgPot-DnNo1yMf2j-yzRYawhvzx2rrEayQUdIbAn8E5wCaoByADjT6ZOtzpZEbkUA_ns9uqvjgXzSZ1VcKUxU6Iv0j25NAaWpWNbtgys-2SdES0wPmqBexCJimyNcnIedQrT_91CY59fXkip_RxQSOfcfLGViqzlvMfdS9mfYwD1ka23F21vCaSJYMLJwxBh1sgBjT-z6jdyc_do9lP0J1eOTR43Wa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3350ssxkwsr_q8hKdJ3zDLsYO9MFkhpVQjzu612UV-ygetgvkeKSqp5SCbfJQmrzWXw_MBldxpxBpZQ88DXt5C97h8KtwFpBlnMUToEZYweAHrzI83-oQoNUmj-34clvs18hzcF85TpxftLMbgO4o9RQBI6n9PDVOhallwuZMN71w_rLO6eovIHsRgyAlW51xCeO09hCg6618LgBunVWPQOG6T7J2qV1M6SP4QA3334sFejUvhYzeap_IfARlHeAwI0n045dHfRmu6H7YQ0ykwRYWKCgXermPnFRBeOVa1A8Jy-JFbvoZX5t0w6mo9irA7_s1LLx6RXv-CMPp4o3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7QrY4Viu08C6XeiOyCh8jFlBt048xd7-oFMVcXhlt1sN81cuJlJosq_k3cNJFcfU_g35FRfJiOXox1-W7LKfGC3w_JffDE-FAoJixK-691u-ttjLxeHRoPhAMWfABnhgwvsF3brl5TsuUcfupQwxXgDMZbYd6cf2jX1dhhSTp4-AS2MQT0qanDk4sAOyIzr28DJGz9qInecb7a5NfnO4A4TVc-pyJo4LPQjOc6N97nsm20drDrAj1IHL_xXlQKvjj6EF5SH_ENkVNYsajSM43p8cPBbf1vdfXF-FFZvVQdQ-H2QFczsW9Ldn4bhzwFWvTEyqVwLQ19TYB-d7ijcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzaFm6qF5QTF2t0259fqy03Ve1W94h13NzGzvbUd8UphDsBqoXa6zPIgWPKcCYI55KRVs_9fJkuLRvlfJfFjr14cmb7lF0K45RHUeww8Ql3zZWiN9RW-cnlbDR2_frUirEsVCmHJpyJBg-eFkMEQghqAR_qmjTXoBHc8gGXg2SUVrPkErZwzMU1YWobQPGU64Ojbea-UFAJKL192TRQKLfjQD1EKW7XGlVEU61mWQLOr6zBrCclCf6Xg_fn5y5gsPPTO7cIvcEsOZan7EMcELRnXV9Y5_8kRh3Sic4M1rqcAHMdKTiGktSl-OQJOs4F6ws85_K_AAyzmv2Pbk9ODsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شور کتاب‌خوانی در نمایشگاه کتاب کردستان
عکس:
بختیارصمدی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/461056" target="_blank">📅 10:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461055">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43f6f01e8.mp4?token=H7OYqfBD-V6lS5U9AC7SEzux-lEcbhLcVRL9XPxFtS_OeJbalQXhsnKb9B4yhSO3In_D_yjueXYOC5xCMdnwgzat1UDCv0WpL6anqJOraE1mYWFz7u_sqR4mk4z9YcpFNWIN7wD_fN9WKOUlzjdf3rVtjuWyOZUy2egiaHetKLvgBcdO1xIarVc4V4zn5RMCTt-AJnw3tSeGJkmonoU3i-R5wsY-_9baztc34QJcOmu9WCWJpSxiGJ-Di7fWeFFK0dgpwYISeNsqyHtADCFA5bjFwpLBFwwQ75c8-rx5gBpocRk3-_VWLzH99THasJDpNVBsZXq99tAapENEpvU0yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43f6f01e8.mp4?token=H7OYqfBD-V6lS5U9AC7SEzux-lEcbhLcVRL9XPxFtS_OeJbalQXhsnKb9B4yhSO3In_D_yjueXYOC5xCMdnwgzat1UDCv0WpL6anqJOraE1mYWFz7u_sqR4mk4z9YcpFNWIN7wD_fN9WKOUlzjdf3rVtjuWyOZUy2egiaHetKLvgBcdO1xIarVc4V4zn5RMCTt-AJnw3tSeGJkmonoU3i-R5wsY-_9baztc34QJcOmu9WCWJpSxiGJ-Di7fWeFFK0dgpwYISeNsqyHtADCFA5bjFwpLBFwwQ75c8-rx5gBpocRk3-_VWLzH99THasJDpNVBsZXq99tAapENEpvU0yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترمینال نفتی روسیه در دریای سیاه هدف قرار گرفت
🔹
پهپادهای اوکراینی دیشب به یک ترمینال نفتی در شهر «نووروسیسک» که یکی از بزرگ‌ترین بنادر روسیه در دریای سیاه است، حمله کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/461055" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461054">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انهدام باند فساد اداری در کلاردشت
🔹
رئیس دادگستری مازندران: پس‌از انجام تحقیقات در پرونده‌ای با موضوع فساد اداری در ادارهٔ جهاد کشاورزی کلاردشت، ۲ نفر از کارکنان و ۲ فرد مرتبط با پروندهٔ به‌اتهام رشا، ارتشا و سوءاستفاده از موقعیت شغلی دستگیر شدند.
🔹
بخش عمدهٔ جرائم افراد مذکور، موجبات ساخت‌وساز غیرمجاز در اراضی کشاورزی کلاردشت به‌عنوان پایتخت اکوتوریسم ایران را فراهم کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/461054" target="_blank">📅 09:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461053">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kV4K7QkJqTjltft4XTAe3wRmR6vpahrr3YL89XW_28mFOObMK3OCFjr5uHZVxdTy2Z4VhGL8aKbACGdhqbc52WKaGYp0J4nAq-DHYHkc3U6PhScqQhLzHR3zCw4Al7Fu7Zw7EuX5WHNPl0aDI4msAegtmD8QnUnZWlruj30DwPARbNO0cASzVFV6llc8MM8EYC_FXeYf7qofvvZlgYp38emUBWc2VBTS4aJTqYSdXsluhUYEkZcN1mnmWAMqdJS8-HbNiBQC0FU6ZI_mEmgKiu7bkIoijEQUBGlZwMXGOePE47esvHC-KB0e9A30oMtyhaBflCfuR_TjUkv3hMmpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/461053" target="_blank">📅 09:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461052">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tns9U7-8NkwK318n3Ne5HFW9Uoha3C_tbrgr1RO1tBBIAZxIy-elt7BHyb8U3ELkE1VdORokAdVG4x1ZtX2OtabzFalvTsYLDG3zf1gnRybLWTKTfzAZb3yMbg_HPV_TPUhL8Xpwnapk7G5gtbtSSVGsJiiTJyKxnfQmxOIN3GPWWzQJQuEya2z3DS9HtRN58A7irgnw5QFFdin_S-l63EWt80JSMbboRWthZJ-J4x1jur3CDYyTfEY_6lWe8Ji5AtpVLSyoDjp3PqSQtOF0o2JaOq4vsox6ORnBPkc0p-8GL70Xm9JBqUMbl0Vry_pGxHRQKEU7Qh33E6DSpN-REA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت کندی اینترنت در ساعات گذشته
🔹
مدیرعامل شرکت ارتباطات زیرساخت، علت کندی و اختلال اینترنت در چند ساعت گذشته را «قطع فیبر نوری در ارمنستان» اعلام کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461052" target="_blank">📅 09:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461051">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کندوان مسدود می‌شود
🔹
پلیس‌راه مازندران: از ساعت ۱۳:۴۵ مسیر شمال به جنوب جادهٔ کندوان مسدود شده و از ساعت ۱۷ به‌دلیل وقوع بارش سیل‌آسا و احتمال ریزش تخته‌سنگ‌ها به‌طور کامل بسته خواهد شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461051" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461050">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09b7c06c0.mp4?token=koIJG7DK-Brj7nz-YqQUEalrxHZ-ZRBevVL05bDnwRVpNEH3eNnSFMxx5DlD7R1GCyj5xT5cXe4oI8Npifwln06WG0hLNY3sYx1m1Vw8kDf7moXgFEixnIevISBLPDBOlMkuTW3DNw2_JG7TQJrjTkaCWvN8LGtAkye2eas5r5bFIUjskA3IUTbzyNq-A9gs5ocRPwGSdSq9Q50e9QWeLVaZ9_TDupyRIkr3VB8letSklkakaqsj6ydWJg_jU5-wwUfqioyo3ehOtc_yPoKNcahynhFfhs-m7hcENjBuQ1GeU0z3_ukp6DFiRhM6ZCpiEz-bEZvw_ybDDti-JmUOtWNumbigQfD3hCX2PaJyH2GxOZ0QIIzcigfjkpiWEi_CiFKgyAD-ydgp8alw9FIzJdnW26DCHAT8riCwFsH9bebxL3ESpgFlfBtHRQ3w0fkaQPw6m92CGMd7EGgsZ1q7xCKmwRPV0aFZFDRRbuRcc5bdTS2DK790fmsu_cAYam32eEtiknh99z_5neV-NcDCr3vgUNjYKg-hpLDx2kBuVpgTzuT4h9SEughMItdnyqsg_7_mAKkL_sMbVhktEmClicFx_1B2LK-ULAHfRnzoskiAGg29zCPU6znd6jvaB9CZbTzyvU8zkxAwPXx8u47TNmzOjKcKXEOln2OnuGYxr0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09b7c06c0.mp4?token=koIJG7DK-Brj7nz-YqQUEalrxHZ-ZRBevVL05bDnwRVpNEH3eNnSFMxx5DlD7R1GCyj5xT5cXe4oI8Npifwln06WG0hLNY3sYx1m1Vw8kDf7moXgFEixnIevISBLPDBOlMkuTW3DNw2_JG7TQJrjTkaCWvN8LGtAkye2eas5r5bFIUjskA3IUTbzyNq-A9gs5ocRPwGSdSq9Q50e9QWeLVaZ9_TDupyRIkr3VB8letSklkakaqsj6ydWJg_jU5-wwUfqioyo3ehOtc_yPoKNcahynhFfhs-m7hcENjBuQ1GeU0z3_ukp6DFiRhM6ZCpiEz-bEZvw_ybDDti-JmUOtWNumbigQfD3hCX2PaJyH2GxOZ0QIIzcigfjkpiWEi_CiFKgyAD-ydgp8alw9FIzJdnW26DCHAT8riCwFsH9bebxL3ESpgFlfBtHRQ3w0fkaQPw6m92CGMd7EGgsZ1q7xCKmwRPV0aFZFDRRbuRcc5bdTS2DK790fmsu_cAYam32eEtiknh99z_5neV-NcDCr3vgUNjYKg-hpLDx2kBuVpgTzuT4h9SEughMItdnyqsg_7_mAKkL_sMbVhktEmClicFx_1B2LK-ULAHfRnzoskiAGg29zCPU6znd6jvaB9CZbTzyvU8zkxAwPXx8u47TNmzOjKcKXEOln2OnuGYxr0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام اشتغال‌زایی ۲ میلیاردی برای جوانان بیکار
🔹
مدیرکل طرح‌های ملی وزارت ورزش: جوانان ۱۸ تا ۴۰ ساله دارای ایده در حوزۀ تولید و خدمات، برای وام با سود ۱۵ درصد می‌توانند از طریق پنجره‌واحد دولت الکترونیک یا سامانۀ جوان‌پلاس ثبت‌نام کنند..
🔹
اعتبار از محل وجوه اداره‌شده وزارت ورزش و جوانان تأمین و با همکاری صندوق کارآفرینی امید، بودجۀ ۱.۵ همت به استان‌ها پرداخت می‌شود. اولویت با استان‌هایی با بیکاری بیشتر است.
🔹
شرط دریافت تسهیلات، تأمین ۲۰ درصد آورده (نقدی یا غیرنقدی) نزد صندوق کارآفرینی امید است.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461050" target="_blank">📅 09:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461049">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac68404.mp4?token=QKaOa9JGvOLD6-mokoj0jtVutrm_gfuKQirbLf7zQKIyWuaa4aMrhHtdZtRUbNkyXm3409u8faCsXTx3Ai9U8bbDbiKoCJ2hwky8E3n32hN9N8XvKEURmA3-aPQDqDFe7UMREidsI6Nq5GunDXi7a_dZMnAtb7RY8eRmPMXeZtgOijl4-dsHUYkiUyVfjENYdfuHQymU_NbB3eIYJy3Wa7ZRGF4LKUPFLwPY4qDlRyXm0j4XhFX6qHcN1pwpj1hVvDGMm4cTpSarI4tUJXEaIJkamRgCYwxPo3pAvCXmnYUqCgL5Kr1-nE18QSKCm1M3io4tMb6v0GeUfVkhCuGnug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac68404.mp4?token=QKaOa9JGvOLD6-mokoj0jtVutrm_gfuKQirbLf7zQKIyWuaa4aMrhHtdZtRUbNkyXm3409u8faCsXTx3Ai9U8bbDbiKoCJ2hwky8E3n32hN9N8XvKEURmA3-aPQDqDFe7UMREidsI6Nq5GunDXi7a_dZMnAtb7RY8eRmPMXeZtgOijl4-dsHUYkiUyVfjENYdfuHQymU_NbB3eIYJy3Wa7ZRGF4LKUPFLwPY4qDlRyXm0j4XhFX6qHcN1pwpj1hVvDGMm4cTpSarI4tUJXEaIJkamRgCYwxPo3pAvCXmnYUqCgL5Kr1-nE18QSKCm1M3io4tMb6v0GeUfVkhCuGnug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز هم سامانۀ بارش‌زا به‌کار خودش ادامه می‌دهد
🔹
سامانۀ بارشی جدیدی روز جمعه وارد کشور می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461049" target="_blank">📅 08:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461047">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d41b703ea.mp4?token=E6vCfVW-reYN3xbj_NYWmDy-_SuS7QiQNMZb4DG_ieUwYq-frVGBuj8qYse290whmimcsrVb6al8WFC49Tujr4-8sW1gTONcxD0GwdYAAAot_jOm9RUazhdGmJgK4iRwog3eXo5SoAGI1C6sO--1Hk3Hsh_X_723x2SItKdlFTkr-_9NPVLMBoFRVADA-sy-MyLSJcnIqpMYHL2KXfYPz4rwGZ90Otk7D2nqeifpllDZCdx86opjgojz276L_JZyXBbldkrKNHZ2lTro9eMulkKoyGAY4hC-Hj6RPvevd1ynfc2cCFjGzfs2Sf1v0nOZ2NDPF75MMu5raELP7dQpHkRGBapOje9r_xq2N0jvmEC0zKzWGdeVNXb8Gx5ECYdqKTkhCWCDX-ePNFDxsUTtVy9Ic9X4moo0yh5EizaSDWWsjtioAzRXhW2u0Wj0k6qs5dkcvgRQg-lG0dmZ0gq1GL2qtjy-aSxuzXQhtcuPSVTLmb-hoc9u320khXXaxm-PqkvbJu6E0lsIkjrTKjZS8R0OgmEcq95LssVlYLpONwaGon6F0Xulay1u5LoMaZtFemexCr2R-Ld-Lz2StnRc9v1I0G0qM_nkXYzw_dNTr714fy3GrJNezeylltRQTMHuVj6RWrcnF7BB8Wi_gPsTiDt6o8IYcSgT40XF_Pd9KBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d41b703ea.mp4?token=E6vCfVW-reYN3xbj_NYWmDy-_SuS7QiQNMZb4DG_ieUwYq-frVGBuj8qYse290whmimcsrVb6al8WFC49Tujr4-8sW1gTONcxD0GwdYAAAot_jOm9RUazhdGmJgK4iRwog3eXo5SoAGI1C6sO--1Hk3Hsh_X_723x2SItKdlFTkr-_9NPVLMBoFRVADA-sy-MyLSJcnIqpMYHL2KXfYPz4rwGZ90Otk7D2nqeifpllDZCdx86opjgojz276L_JZyXBbldkrKNHZ2lTro9eMulkKoyGAY4hC-Hj6RPvevd1ynfc2cCFjGzfs2Sf1v0nOZ2NDPF75MMu5raELP7dQpHkRGBapOje9r_xq2N0jvmEC0zKzWGdeVNXb8Gx5ECYdqKTkhCWCDX-ePNFDxsUTtVy9Ic9X4moo0yh5EizaSDWWsjtioAzRXhW2u0Wj0k6qs5dkcvgRQg-lG0dmZ0gq1GL2qtjy-aSxuzXQhtcuPSVTLmb-hoc9u320khXXaxm-PqkvbJu6E0lsIkjrTKjZS8R0OgmEcq95LssVlYLpONwaGon6F0Xulay1u5LoMaZtFemexCr2R-Ld-Lz2StnRc9v1I0G0qM_nkXYzw_dNTr714fy3GrJNezeylltRQTMHuVj6RWrcnF7BB8Wi_gPsTiDt6o8IYcSgT40XF_Pd9KBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
اولین تصاویر از زیردریایی بدون‌سرنشین Dive-LD آمریکا که امروز توسط سپاه پاسداران به‌غنیمت گرفته شد  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/461047" target="_blank">📅 08:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461046">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آتش‌گرفتن یک کشتی در قطر
🔹
قطر از وقوع آتش‌سوزی در یک کشتی در بندر «الوکره» و مهار آن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461046" target="_blank">📅 08:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461045" target="_blank">📅 08:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هوای «قابل‌قبول» در پایتخت
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۹، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/461044" target="_blank">📅 07:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWpxTha7uIXP3INWntIassnRZnvGlKa-03zV2a6QvqTplSLV3916V6U7xyRMbecdrlZaBBRYaSkOYZZdkNoEx-drCI1przGHJRYjEToikc6bjIAlq5Xfk3PThurH3Rm-934xkVFasX6zO6eSIt-zGKhx93iWs72zCGRNe0zD5DBVHcZO-DkDIk7Y20Swl9_DdlgxNz1-1ZYLBOD7Qx-X2WV600KGc6K1vBXJTdz-AIDDsiIJihfSN0SFh1zGP7iXButxSjKiZBpDikbyK5UhwkjxYbAvGHrgB_w0QnzByX5u5krVvlYMr2BzERdtnfbdOuo0Anqvkz5T0eYPswqYdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن به بهانۀ ایران سراغ هوآوی رفت
🔹
دادگاه فدرال بروکلین میزبان محاکمه‌ای است که با بهانۀ روابط تجاری هوآوی با ایران سناریویی تازه برای مهار پیشرفت فناورانۀ چین طراحی کرده است.
🔹
محور اصلی پرونده، ادعای همکاری هوآوی با شرکت «اسکای‌کام» در ایران و فروش تجهیزات تحریم‌شده به یک اپراتور تلفن همراه است؛ اتهاماتی که هوآوی آن‌ها را رد کرده است.
🔹
این پرونده از سال ۲۰۱۸ و پس از بازداشت «مِنگ وُن‌جو»، مدیر مالی هوآوی، به یکی از حساس‌ترین مناقشه‌های حقوقی و سیاسی میان چین و آمریکا تبدیل شد.
🔹
محاکمه در شرایطی برگزار می‌شود که رقابت واشنگتن و پکن بر سر هوش مصنوعی، تراشه‌ها و زیرساخت‌های مخابراتی شدت گرفته و هوآوی نیز یکی از بازیگران اصلی برنامه چین برای خودکفایی فناورانه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/461043" target="_blank">📅 07:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQW5x8TIRL5PApw7XaOyETVcJ-N3CZ3I4TRcOQc11Cr7Cu-H2Ek3tOBi7NnFZYKQTzgjgSWJ7UwIdcrfvF8sqn0Wh6ov4uOeH6HqBLHW5RGpT-kHCYj8_AOMbccNkt5pBOJvlVIPQ6bucGL6dHIG4I-mjcN5hAUVN_FMYBWBV3cLOZTJ5AuebmnUBmpefqOXUq1UrRs2ETz2C2KIEx6p9f0RJMXPylzUkeRiblMEFafasCH94ReVnpS3JMM-bBcyPi0CGBfz4XJhuM7eOhPFpssWKc2qwGeSiQVAy8GuGzMnGeX3B9bgotlib7w_2G1NN68xj-RzHLpT1JQ3NxNRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم انگلیس و فرانسه علیه رژیم صهیونیستی
🔹
وزرای خارجه ۱۲ کشور غربی با صدور بیانیه‌ای مشترک اعمال محدودیت‌های تجاری بر کالاهای تولیدشده در شهرک‌های غیرقانونی اسرائیل در کرانهٔ باختری را اعلام کردند.
🔹
این کشورها شامل انگلیس، کانادا، فرانسه، دانمارک، فنلاند،…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/461042" target="_blank">📅 06:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqYC3dB2SxrFDFCfnzYWlMvodrtl6ZQYQNQ3GryaBcIjBfpWLo5B8J6a4w83xDC0hhRRYg7LtKLBgJ4uWOFbX1sfdmyca2_MWhWSlfLyrulB6rPtBvxZuvkAryLSl07ZVheru-jtT_h97kWBVbwHqErmsZsu-L5UxRgOC8ajweWIOKfRbVwvomCUPXbkTVKy6ebnFkS2vO5G9XYk5Wi8DY_hN7w9nmTU8VyuC5IdB-67mXlhHWj5Fg_IJw8TExnHDIJ7XPNWPavVJzIs8gFB6RU-l53UZg8e3jd6TVgjIiCA7JPOFAKU9gx1Q7Nsm0GHWKtcZ0Jlsoe3MLQft7YZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vU4j8kpNtbkXoHKm0SCjzTPgQur9_LiiAirk3N1JiOswbgzrAElc0vB9FcL9fbqQwQ3e59VYTWuf37twXW6zHpcj81u1mFRJcIZFd3Rbk2Vcuq91MXYO3rtJz2EFoV6Br1P65vhSamHBNdRK7_l3uiZPhHdR8uod-cNaCf7TLFhZJb_U3Lj0y7UL8qI3tuYQCrVHsEFMCM2lnM3d0pOOXUQ619A3NHC4SnJ8RqttUwBnSuCJrDaDRpJnDolzLK72tPdryNP3Cqa-yhbnlQCz5ZftT-HH-niBCgaQfyKNeSVtFZ2MjdmdHALES8V6eKUFikRxLNshaVZq0wVC85tVyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkKEeMG-P3RuLwgy6SASIfdzLTPHqAEdC4ke0zdHJr4e8Ekaneb4Atr_rbWt3AlK8NTgjgikJayPW3yEkYAsJBETVcdjGtE4uy9-vQkq9ltu14RZdpZDX-RiPDZh_M3m6Mk_Ni91cV0g_1ApV1op0AH3o6qfLFrpcdweDYK97omrUB6SMcKwmPUVdAC9zXhagaPD9Km9H_rp1OnXnrCbg6atIUHHkuT2NO4UNVHTBBK3jAhjyJXh7RX9J44y3g1DpqegW1AWPM-7-01DqF2zrNUFsiknKjIe8r2IExWAZ-oRqBLM5EnOGSEvF_C2GxXPOwToICiKCLLu44TXF2b9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDOaU5_ryJhvfJCeEc9_D8Pe3MH_696d2e1NzpC0UXzeEMsnlUxXhk3aL0udiFDd_sq4atKP4GhEF-oN0UXzP5uWI3j1npTStQCtfvQifgos2kOXqXLRN2BHFGqdPlpjlgaMSqshMozLXwxnzOSTsozOH8M4N120MxvDYF3JnyYLJVRlyuxR9UWyYCSWP9B5qmTUBySow2JykNjQISLt4MdbmuRWk3l2QLbIv-HsM-3lhKkfFuglcKjXFDqqXOZPjizAFBquS_mzwyuh33nPQ8okXqx92efmDf-LwOTcrlsQBy1P88GoIWR2LRkyCXcpRLoeQStmLUGj_HZgo4BWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJ0DJ8_UCkYpE4gCewPxax9mLxjIUYu1tREpPSCSzm1VTuCz7yBuwt-GvhgxX825hzA28MqQZUzolJ5K0U2-fTHyhRoq6gsETGpnz9YcIAwBidngaeryNiwKH3l4o9PCS7IdyH4b-hqvxwM24j-IlVZVmqELS_N-kgs7is3la13I_2fFJhg9WF16rip2D0pmtdjhvDyyvFfVte3a84MALwFnIp6yeHRVG67wBudgvAtq_wnthDPGj496HJPSbpN5kCu883ED9yyztA2KPcsfOSLUylb6_hmWpeyQZJc37HiXbcQVO4rSBeHoqSYxzwlETPPO6iAZfZNILzZHku_H0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tex8jSkHZ5nly4bKe9YmAOGTJ30Pj-ThdN7OMP-I45Zk8I6hdCBd1P_98QEuNRaMWyu-i1LySgVi93F4EGZhcd0D94gwo1mZuiGAmQsCiInzSG54X88lI-So8vQO0ESgTwD3Sf7wl1SOQITW5ak51I7PHmOUCTUHWw6PfNFvQCvRowddZ_kLCqlaH54ev0LVfDgr8kKHXHbapU80cHP3Q7zrObsnQGcI-_fLTwa-Xz2zT4Cc0upJ_taeSuHPqFzLKd0LsojI6MvlCqi4bcFwC3RCEVzoz3NWwY_Zy3QwetWU44S5s9PjPT1GAcccV2KFFs8QW8Vjzk8hivodSlzzog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZVX7W1vLDLl2qFuvdjwsrg6qnjDXcfG7fuAk7d2pBzva1YvHvvYNl5Xc23-g4TK1sA5RpccnaD0R-Yopa84srRS3W9cWahHnl5hVHvUcKVSr3pMh0IA6zKJWxTxP5E_UucoQnfg0_INrQmWNp-xXg-Ali6SXqmOeQka0Ck0TL52KdT8PJeyQ1v76WbQe1S3fwnRvUpoZ70BmXKU_hN1Vo09MLDr2XmHuhNZwGANgCOpSJ4-qKGtaMAR0nAC_bw5oqY7uTOccXVDnOqH3C-xtRD6krVj68JkmjJFih4JDdl6E4MYcre0t41LTs8aK_MH3mGm0VysCEmA_TBuEeqWtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
مسابقات اسکیت سرعت آماتور
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/461035" target="_blank">📅 06:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa-NtQmTdLbla9LF5zANoo_hGiU0CDvyYLMHgaS7wFWbFwIrT-vMTqShfK-TBpso8ch-ve6X7OSVdPjjromhQ3Ej6embL66wOkgbfl0nbjlmNJw6GUWbGvmXbqwALcy6dGlmDoVnzxNk44H3BvClefLp2tmNXRCckozwSkO7CoS7SWIQ01VIe5TO5Ge6g9g81ITewSvWcinHiZuIjrW_hwmRwnTsVlFp44Dm787CzmF91qIPNF75SYjrnQgmw2HgAsM8NDJGBkDjqmOOJenZH1Nw_4VKk8ZztjW7knF2V-ajpwtj7RFhpdDr3irvIz8WWUxuYRNzNCjDK1lGldJmJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استخراج اورانیوم از آب دریا سریع‌تر می‌شود
🔹
پژوهشگران چینی ماده‌ای متخلخل به نام «فوس‌کیج» ساخته‌اند که در آزمایش با نمونه‌های واقعی آب دریا توانسته تا ۵۰.۴ میلی‌گرم اورانیوم به ازای هر گرم جاذب جذب کند.
🔹
این میزان حدود ۸.۴ برابر معیار تعیین‌شده توسط وزارت انرژی آمریکا است. پژوهشگران می‌گویند ماده در شرایط آزمایشگاهی تنها حدود پنج دقیقه برای رسیدن به تعادل جذب نیاز داشته است.
🔹
غلظت اورانیوم در آب دریا بسیار پایین است و وجود یون‌های دیگر، رشد میکروارگانیسم‌ها و دشواری جمع‌آوری جاذب از محیط دریا همچنان چالش‌های مهمی محسوب می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/461034" target="_blank">📅 06:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643cb9a38f.mp4?token=GedYedAR96msWwYaxXw4qLTVRi5qpq0-803fmk-FO5CSwohwclycjJKLXZPQrBKyE_H4qdVOr1vTQbEyA_1tpLD6GpLK1kTOUODRSdEkL7bzhbbkW5KnLk_FVOr27asp04kKZwPqN7WJ-Efpazy1lz84FXY6pn4-gg4EEl0SAk9sQp-8Yx0xn1J-X_J-vB-JjVqm8EPC7djE1BFdqppzCfxZ7NVmd0m7JfOvQyEij9Ubk28ERG-S4yez9j-kXjbMsS1agkQ5yN3iJelmTUcPXaDVS_erbwtFdTF7fso6vsrOeM4AysVN9KoJrrRb6GFrJWLCKMFH8rl6Ij3rWhU0PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643cb9a38f.mp4?token=GedYedAR96msWwYaxXw4qLTVRi5qpq0-803fmk-FO5CSwohwclycjJKLXZPQrBKyE_H4qdVOr1vTQbEyA_1tpLD6GpLK1kTOUODRSdEkL7bzhbbkW5KnLk_FVOr27asp04kKZwPqN7WJ-Efpazy1lz84FXY6pn4-gg4EEl0SAk9sQp-8Yx0xn1J-X_J-vB-JjVqm8EPC7djE1BFdqppzCfxZ7NVmd0m7JfOvQyEij9Ubk28ERG-S4yez9j-kXjbMsS1agkQ5yN3iJelmTUcPXaDVS_erbwtFdTF7fso6vsrOeM4AysVN9KoJrrRb6GFrJWLCKMFH8rl6Ij3rWhU0PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: ۲ شناور آمریکایی، ۸ نفتکش و ۱۰ کشتی متخلف هدف قرار گرفتند
🔹
روابط‌عمومی سپاه: نیروی دریایی قهرمان سپاه در پاسخ به تجاوز و شرارت ارتش تروریست آمریکا در حمله به ۵ نفتکش ایرانی در خلیج همیشه فارس، تعداد ۲ فروند شناور آمریکایی و تعداد ۸ نفتکش را در این منطقه مورد هدف قرار داد و خسارت‌های زیادی به آنها وارد کرد.
🔹
همچنین تعداد ۱۰ فروند کشتی متخلف که با تحریک و حمایت ارتش تروریستی متجاوز آمریکا قصد عبور از منطقۀ ممنوعه و ناایمن تنگۀ هرمز را داشتند، مورد هدف قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461033" target="_blank">📅 05:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21aa83f910.mp4?token=ndrQzURGFrR91qz2azrMSlnF9oWE5CQrAPr-jvSvs1IH6w0JVjtu874rNH_y_XdvsnumHr0hxaw66zuQAQUdycym1py1TXyDN0lMxUr6I_4KD1pi9JMcxn_JdE2oQGUHiT9zJOpryk70M1xs5lyvcQsvip3RXRUN3IrBmxv_ihVGe-kU3fzGHM44xh63kKOyjfPPTDoGjPd240p9ArsDmvoLjpPLdDgNLAPSoh1uZNEu2W7oEl1BskxOSbHshasH-JiBNigBw_iBBCDFs7qyRp-QbImgdX_H1Dg_jqMiCtgpBko9b5HnZFMEnEL2k6Sa-Ds_9sfcf7RXthOUR-20Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21aa83f910.mp4?token=ndrQzURGFrR91qz2azrMSlnF9oWE5CQrAPr-jvSvs1IH6w0JVjtu874rNH_y_XdvsnumHr0hxaw66zuQAQUdycym1py1TXyDN0lMxUr6I_4KD1pi9JMcxn_JdE2oQGUHiT9zJOpryk70M1xs5lyvcQsvip3RXRUN3IrBmxv_ihVGe-kU3fzGHM44xh63kKOyjfPPTDoGjPd240p9ArsDmvoLjpPLdDgNLAPSoh1uZNEu2W7oEl1BskxOSbHshasH-JiBNigBw_iBBCDFs7qyRp-QbImgdX_H1Dg_jqMiCtgpBko9b5HnZFMEnEL2k6Sa-Ds_9sfcf7RXthOUR-20Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار تصاویری از اصابت موشک‌های ایرانی به پالایشگاه «حیفا»
🔹
ارتش رژیم صهیونیستی بامداد چهارشنبه اجازه داد بعد از نزدیک به ۱۴ ماه، تصاویر اصابت دو موشک بالستیک ایرانی به پالایشگاه حیفا در تاریخ ۱۶ ژوئن ۲۰۲۵، در جریان جنگ ۱۲ روزه، منتشر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/461032" target="_blank">📅 05:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8fe88c4c.mp4?token=Kr3EGGCRsA0q2xHIsk0ECzu5T8g33lYtK9h82XXtZvvhG1D_wvqfzsQhM0jkoRxoD5PFFJmb0jJeas-0ICpNj3ye9X1Z2c7EZlBALwHf4jHbIh4Zzc4FXbmMUdD9AgnW1j5IZsE3-9_DeKKb0nB5wCiT917VlhdOBzSdrp_13wRnWputdze82_Xa3LCMAlkNWGauShjVOy27wTyHAgFLG33o6wPIGz-OkqUanCYMaS_LJ1syelF4Icxpmuo0i5J5L8vgmKs_3Hi7f4hJJUGubaYlR6HCs8BDGhWpKpAZWahLcajXpMlfus6Oa0VbQlfUE2aftKSqkE3M-fPs6dq5eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8fe88c4c.mp4?token=Kr3EGGCRsA0q2xHIsk0ECzu5T8g33lYtK9h82XXtZvvhG1D_wvqfzsQhM0jkoRxoD5PFFJmb0jJeas-0ICpNj3ye9X1Z2c7EZlBALwHf4jHbIh4Zzc4FXbmMUdD9AgnW1j5IZsE3-9_DeKKb0nB5wCiT917VlhdOBzSdrp_13wRnWputdze82_Xa3LCMAlkNWGauShjVOy27wTyHAgFLG33o6wPIGz-OkqUanCYMaS_LJ1syelF4Icxpmuo0i5J5L8vgmKs_3Hi7f4hJJUGubaYlR6HCs8BDGhWpKpAZWahLcajXpMlfus6Oa0VbQlfUE2aftKSqkE3M-fPs6dq5eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با این کار خودت را بدبخت نکن
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/461031" target="_blank">📅 04:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASDe1M_xcwyp3tEJo51ohNOvF9Y80f3R8xhzoCOtcJDQxBdcA1yVkj0a9d2-85u8ow-9O2jb6rdaa-0h5XWetbraidoI2dq9yXJ7luVVldXCCTTtDrkg852QlbgBfudfHGBRfvgxxOOw2BNDAUo3V3QBnceLQ0QdTo5fj9bRP2ItbdqXhJBY6CIb1J6-G9aUYh-2GbKDy8BgPQEef73mvGuhgB5TUJRCmU7_E-tom81XLgMtMPuxBd9lpRJ7fsfRY057WiLJaPSF6xuOzMPj2peBZ8McQozP08vptublvgL0L8UcW6rJyZq7Nz_PnbxAloteSIXJZ5Tf8vohTZL3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارچ نتانیاهو لجن‌مال شد
🔹
دقیقاً یک‌سال پیش، بنیامین نتانیاهو پارچ آبی به دست گرفت و در یک پیام ویدئویی خطاب به مردم ایران ادعا کرد که «به محض آزادی ایران، کارشناسان برتر آب اسرائیل به شهرهای ایران سرازیر خواهند شد تا فناوری‌های پیشرفته را در اختیار شما بگذارند.» او حتی از کانال تلگرامی فارسی‌زبانی یاد کرد که سال‌ها پیش برای آموزش مدیریت آب به ایرانیان راه‌اندازی کرده بود.
🔹
اما در سالگرد این سخنان پرطمطراق، رسانه‌ها و شبکه‌های خبری جهانی از یک فاجعۀ زیست‌محیطی خبر داده‌اند که حالا خود اسرائیل را با بحرانی جدی در تأمین آب شرب مواجه کرده است.
🔹
بر اساس گزارش‌ها، یک شکوفایی عظیم و کیلومترها گسترده از جلبک‌های میکروسکوپی در دریای مدیترانه، ۵ کارخانه از ۶ کارخانۀ بزرگ آب‌شیرین‌کن این رژیم را به‌طور موقت از مدار خارج کرده است.
🔹
از آنجایی که اراضی اشغالی حداقل ۶۵ درصد از آب آشامیدنی خود را از طریق شیرین‌سازی آب دریا تأمین می‌کند، تعطیلی هم‌زمان این کارخانه‌ها یک وضعیت شکننده و خطرناک ایجاد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/461030" target="_blank">📅 04:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6486ad58fc.mp4?token=BNQ5rPTIvrER0KoOZwBglX8jKOAykRIeBNm1-71altC7SVCWGRpCYbNIHZNikgBgu-33RX7utijGKrwHMP405mE8sgx_paJMo1LWJF23_xpk1qL5sQ9KAGOK3W-GEDiMzdW6xqkCpbCejEO-U_v4bQqdm2ANTYoihaMqnWDnnTKRPVgDE8TBpAeLmkNxOb1cqAhaASqPnyf9uUQ5RKnLUQq1Aj-ImxEumVKhY0RmQW3PsyqwgqiAh7p3ZxTWZBd_oDsfkTfvg1ZZw8BrOIwaB8xQMghlDRRhBgqY-zpU3zSnjHmBROziSDrWyoKf7gH4Y7-UtPuxkfXDmCO8c68IyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6486ad58fc.mp4?token=BNQ5rPTIvrER0KoOZwBglX8jKOAykRIeBNm1-71altC7SVCWGRpCYbNIHZNikgBgu-33RX7utijGKrwHMP405mE8sgx_paJMo1LWJF23_xpk1qL5sQ9KAGOK3W-GEDiMzdW6xqkCpbCejEO-U_v4bQqdm2ANTYoihaMqnWDnnTKRPVgDE8TBpAeLmkNxOb1cqAhaASqPnyf9uUQ5RKnLUQq1Aj-ImxEumVKhY0RmQW3PsyqwgqiAh7p3ZxTWZBd_oDsfkTfvg1ZZw8BrOIwaB8xQMghlDRRhBgqY-zpU3zSnjHmBROziSDrWyoKf7gH4Y7-UtPuxkfXDmCO8c68IyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از آماده‌سازی و پرتاب موشک‌های سپاه برای هدف قراردادن ناوشکن‌های آمریکا   @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/461029" target="_blank">📅 03:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461028">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a902bd19b.mp4?token=IOOfovuHBOdrb1OsGPsERuoLIvcqbbB3y7rLkatmxYmhP3kMmQGW794YG2ZkiSou01sJfSuJvPdtGogl_gAGXRO-HCHkUYxCGvtEgn5Hinm0Ze7B-dsnB8GHphuTnna1cPmaE053nM6Ta23nC8d0rSTw0LDHFUZh9vCmyPHrSjH8_XyLTWAeOzv8h2d-jnt-hMKjoMLiPMXJ_MGjg9iRQYtV81mZ6Kf7CnuwPBZTdjZN4aEZIKv25UCactwq0zNTVNknuMQsLTnrAzPe-54JRMA7yaD5wTZIRW1mX1E6P-mCKc7SKYyrjIzVyPYYOR23Aq8i2arNX6GFDtRHNxMswg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a902bd19b.mp4?token=IOOfovuHBOdrb1OsGPsERuoLIvcqbbB3y7rLkatmxYmhP3kMmQGW794YG2ZkiSou01sJfSuJvPdtGogl_gAGXRO-HCHkUYxCGvtEgn5Hinm0Ze7B-dsnB8GHphuTnna1cPmaE053nM6Ta23nC8d0rSTw0LDHFUZh9vCmyPHrSjH8_XyLTWAeOzv8h2d-jnt-hMKjoMLiPMXJ_MGjg9iRQYtV81mZ6Kf7CnuwPBZTdjZN4aEZIKv25UCactwq0zNTVNknuMQsLTnrAzPe-54JRMA7yaD5wTZIRW1mX1E6P-mCKc7SKYyrjIzVyPYYOR23Aq8i2arNX6GFDtRHNxMswg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: ناوشکن‌های رزمی دشمن حامل موشک‌های کروز و ایجیس مورد حمله قرار گرفتند
🔹
روابط‌عمومی سپاه: در پاسخ به اقدامات تجاوزکارانه و ایجاد مزاحمت شرورانۀ ارتش تروریستی شیطان بزرگ برای نفت‌کش‌ها وشناورهای ایرانی، نیروی هوافضای مقتدر سپاه پاسداران انقلاب اسلامی…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/461028" target="_blank">📅 03:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4752a39be.mp4?token=jxuVRocjd6MyHBJMVBtE6CIIyYnVNCD1g_05yJWxSSc2oKQLZN5YvmLih8Q8T827Waxek2DQgrd7cOXqKO618fefLS0QTSVfldU1Y4NrD9b3Zh0KN3X7UODBayael9Vet-JuOUBeL9-0gU-bGB-9sJ2TGXIO9yu-jBEWQjvUxj6ibaQL-JZuy7EB7oVdRHSzko5RgJy6J2uuY1JwnHcy2UFeCuI1LUOFwTQqq5haZY-ql5yJii9TKWHC7aIedBJ5fz2Z_JVb_OoW8lbhhwPkIjhwhSeZGpgU-OCwXHzNDlAraOyipjA6OLOlxmYCMpAt2AlKQQWelA0YJayBEL0JdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4752a39be.mp4?token=jxuVRocjd6MyHBJMVBtE6CIIyYnVNCD1g_05yJWxSSc2oKQLZN5YvmLih8Q8T827Waxek2DQgrd7cOXqKO618fefLS0QTSVfldU1Y4NrD9b3Zh0KN3X7UODBayael9Vet-JuOUBeL9-0gU-bGB-9sJ2TGXIO9yu-jBEWQjvUxj6ibaQL-JZuy7EB7oVdRHSzko5RgJy6J2uuY1JwnHcy2UFeCuI1LUOFwTQqq5haZY-ql5yJii9TKWHC7aIedBJ5fz2Z_JVb_OoW8lbhhwPkIjhwhSeZGpgU-OCwXHzNDlAraOyipjA6OLOlxmYCMpAt2AlKQQWelA0YJayBEL0JdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام صریح ایران که روی موشک‌های شلیک شدۀ امروز نوشته شد: ایران سر سوزنی بر سر تنگۀ هرمز کوتاه نخواهد آمد. @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/461026" target="_blank">📅 03:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7f2c8daff.mp4?token=qrgK98DM5N6gFkVWVveY9eETqycYPnHn4H8i5S4yfBpD_5EOYb8ONlU5QMIACt7DZ3tzEeeGtJ5S_VuWnYYUHRYmG13pORwhs3KYnEX5CQrJcY_1OJhNvt2Pikl0Gphad5sD25A6srdUrB5-KuJK1XISe6hz2VGi95cAKRp0DA3fmrFUUfFg4q9NhUHd06FfFcu639XZhHNm56NpE04ce7eZBfCZMbsUs0Dc_z-6twdySZjz2yB4IvSVto3jrRPGyIf14tV-jhBVHBPuxzH7rpayt9B_ZQciNTRWtBnma_mP9gX6V3E-QnmsG3WxxtL0-vqPF88A_0gbNMQq1uyz2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7f2c8daff.mp4?token=qrgK98DM5N6gFkVWVveY9eETqycYPnHn4H8i5S4yfBpD_5EOYb8ONlU5QMIACt7DZ3tzEeeGtJ5S_VuWnYYUHRYmG13pORwhs3KYnEX5CQrJcY_1OJhNvt2Pikl0Gphad5sD25A6srdUrB5-KuJK1XISe6hz2VGi95cAKRp0DA3fmrFUUfFg4q9NhUHd06FfFcu639XZhHNm56NpE04ce7eZBfCZMbsUs0Dc_z-6twdySZjz2yB4IvSVto3jrRPGyIf14tV-jhBVHBPuxzH7rpayt9B_ZQciNTRWtBnma_mP9gX6V3E-QnmsG3WxxtL0-vqPF88A_0gbNMQq1uyz2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک انبوه موشک‌های ایرانی به پایگاه‌ الازرق اردن، محل استقرار نظامیان تروریست آمریکایی   @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/461025" target="_blank">📅 03:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
شلیک انبوه موشک‌های ایرانی به پایگاه‌ الازرق اردن، محل استقرار نظامیان تروریست آمریکایی   @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/461024" target="_blank">📅 02:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">🎥
چه کسانی می‌ترسند نام متجاوز را به زبان بیاورند؟
انگار این موشک‌ها از یک آسمان بی‌صاحب آمده.
@Fars_plus</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/461023" target="_blank">📅 02:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRsHeGvlKwPcNVhYyShZU-2F4NYPUqTRco4LR6yFF6e4CviNpacg5oO2MSytPcQmyTcTF3ina8lwEO27XcDy-bxhoEi6VT6mNSSWw4p46xgZn4Q4khQUGqZL9pej7vPbwEpMQTh8VgzhqqbyGr5zNqeaKHWOjXSwpl9CKgtSnoT6oQ_SFNkWpf_xDaoqUVEDYGinvsM25IfB1XImcuUdejrn0o-rbNTFf5bxID9JKLY2fN7Z9JqYfBddMg_BtMsIvntdKmNBiUO7lLLFj2m9jNoglPZVnipgfSf5jzVB_O_khcR2OWdvNSdLnNl3ewO87XBRlMLOaD6fRvQOW9I5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقوع حادثه برای یک کشتی تجاری در تنگۀ هرمز
🔹
سازمان عملیات دریایی انگلیس: یک کشتی تجاری در بحبوحۀ فعالیت‌های نظامی جاری در منطقه، در آب‌های شمال عمان مورد اصابت قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/461022" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
سپاه: آشیانۀ تعمیر و نگهداری، آماده‌سازی و محل استقرار جنگنده‌های F-35 ،F-16 ،F-15 و شلتر جنگنده‌ها مورد هدف قرارگرفت
🔹
روابط‌عمومی سپاه: ارتش تروریستی و متجاوز  شکست خوردۀ آمریکا از روی استیصال چند کشتی تجاری-نفتی ایران اسلامی را مورد حمله قرار داد.
🔹
به…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461021" target="_blank">📅 02:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
سپاه: آشیانۀ تعمیر و نگهداری، آماده‌سازی و محل استقرار جنگنده‌های F-35 ،F-16 ،F-15 و شلتر جنگنده‌ها مورد هدف قرارگرفت
🔹
روابط‌عمومی سپاه: ارتش تروریستی و متجاوز  شکست خوردۀ آمریکا از روی استیصال چند کشتی تجاری-نفتی ایران اسلامی را مورد حمله قرار داد.
🔹
به تلافی حملۀ متجاوزانۀ رژیم آمریکا به نفتکش‌های ایرانی، رزمندگان قدرتمند دلاور و جان برکف نیروی هوافضای سپاه پاسداران انقلاب اسلامی در عملیات تنبیه متجاوز پایگاه آمریکائی الازرق اردن را زیر ضربات سهمگین موشکی خود قرار دادند.
🔹
در این عملیات، با حملۀ سنگین موشک های بالستیک سوخت جامد و مایع آشیانۀ تعمیر و نگهداری، آماده‌سازی و محل استقرار جنگنده‌های F-35 ،F-16 ،F-15 وشلتر جنگنده‌ها مورد اصابت قرارگرفته و خسارات سنگینی به دشمن عنود وارد آمده است.
🔹
دشمن در مواجهه با نیروی دریائی قهرمان و مقتدر سپاه پاسداران انقلاب اسلامی در تنگۀ هرمز از موضع ناتوانی و عجز و ضعف، دست به حرکت‌های مذبوحانه زده و بلافاصله پاسخ قاطع را دریافت نمود.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/461020" target="_blank">📅 02:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ادعای ارتش تروریست آمریکا دربارۀ حمله به ۵ نفتکش ایرانی
🔹
سازمان تروریستی سنتکام مدعی شد که پنج نفتکش ایرانی را در روز سه‌شنبه هدف قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/461019" target="_blank">📅 01:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461018">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsrB9Xz1p9SAGkKUWcesOLnYkd3gkwmp-fminVol9quZU9ktYDxY49CFbygJlb-ovbxmtiBbtBFZJIJxVzJd1a_I2rrgEMHG3jGahkJM51rUEDE7wHqUL21KrUidX_ZQW8HnTvjHeAc5ac0Axu2xzu8UDJ7v396RZihq1VmWZaRZgpkwj2FJmLKjXWaeAX0yIKedw4DgL-9Ol2k_I2_dLCzlxAlKGgvEI-lLLaLsV57Djrdc6jtZVBSXEPaWyRosZt6mV7gBF2xMKIdwk11skYZaMd1JjKxuaiFiy_mX0NufAvH0ttOENT7cOfcx3p0LDM-pzsni6iBQZUWF2mlVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداداد عزیزی ۴ ماه و عالیشاه ۴ جلسه محروم شد
⚽️
کمیتۀ انضباطی فدراسیون آرای مربوط به حواشی دیدار تراکتور-گل‌کهر را به شرح زیر اعلام کرد:
🔹
خداداد عزیزی ۴ ماه محرومیت از ورود به ورزشگاه‌ها و ۲ میلیارد تومان جریمه
🔹
امید عالیشاه ۴ جلسه محرومیت از مسابقات و ۵۰۰…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/461018" target="_blank">📅 01:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در بحرین
🔹
منابع عربی گزارش دادند در پی حملۀ موشک‌های ایرانی، انفجارهایی در بحرین رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/461016" target="_blank">📅 01:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cbdfc4f17.mp4?token=HF-eV8L7skjHxxn6YMEBEVZM9g1sLYe0MD-Vql__gTBiqmrrID6kfBHggvHmEB0MFBQp3TqN-BCG51bhmaN8d9PJQVSzLuh7JRtFH2Oia_cmO7Re30E6bV73KWXjnnBaJNgIbae1f9ghql4xrU8oWnFTngU0ojVXggFUdBtU7JA6et4JraN6z08sVf1MHhfH0EMmyq6ftGKuhzuFRy-8la8Gd95H5UkMQM_5CKkv0-w9xTkZ8D0vpFPXII-iAhH3V2xSiH52ugG0JUX52FUZGbqkOOWq7SywD0r3nZxwksKpHxqtZCvibNr6Wg2aFtsLGuTVzkvvgQkFOaHPcFjydg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cbdfc4f17.mp4?token=HF-eV8L7skjHxxn6YMEBEVZM9g1sLYe0MD-Vql__gTBiqmrrID6kfBHggvHmEB0MFBQp3TqN-BCG51bhmaN8d9PJQVSzLuh7JRtFH2Oia_cmO7Re30E6bV73KWXjnnBaJNgIbae1f9ghql4xrU8oWnFTngU0ojVXggFUdBtU7JA6et4JraN6z08sVf1MHhfH0EMmyq6ftGKuhzuFRy-8la8Gd95H5UkMQM_5CKkv0-w9xTkZ8D0vpFPXII-iAhH3V2xSiH52ugG0JUX52FUZGbqkOOWq7SywD0r3nZxwksKpHxqtZCvibNr6Wg2aFtsLGuTVzkvvgQkFOaHPcFjydg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
موشک بارشی ایرانی در آسمان «العقبه»، از دید دوربین صهیونیست‌ها در بندر اشغالی «ایلات» @Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/461015" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHt6rFO07ytbogT03nADjxJLcqt62DdYAas29081AiRz6xIhaKA1S90kkWuD5wLWwVRvy_dUoXA-TLXkwx-qNHMTZSnjdPdvoJGPMAQp4Ilp-By3hQPmy4MCfywRxnAf0cczHvqcEtxJRDZTiDuXXZwaUN3tAuR7cJjNvBNLyNz6dFTU07-bBHtI9de9LOZks2QReAYkvloXzqRhWGbpn2iURaDx3Fi8ngAqaICuvQyCMN8tO8D7iNUL2wLIQ_Sw3agB1X20tUisQ5FbsA_yjUQM4M148Yoco_bnBtc2zi-DIBhZRNWCJTwwyfCfC2bDbGTQUlcVM4E6whDcPF1NEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
فرود موشک‌های ایرانی با کلاهک‌های بارشی بر سر تروریست‌های آمریکایی در منطقه «العقبه» در اردن و ناتوانی سامانه‌های پدافندی در رهگیری آنها  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/461014" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77db0c15f.mp4?token=o76t4xtIuabH2eGwCUMOxhfQSs7IiYSJuv75OZbSX4cccKxjk4posMAcpGQvZ8JcNRu5i8qjvktrPYAEpjC0vptqwMN17WqrMkcpDswyuJdYuOj_xyNidvuSUdPd4cc0XNFUiOTmxEa1FHUiVc3G_eO1GT1afd6-OVxJiOmgBld_PKOTC5q7Yt0yvnoX6F4x_PuIu9_27Y1nheAFQifEcww6k6yKhmq9RcqI3lYFXdbncK0N8MCTZMfp2BbS3z8WEcO8fUxqI0HJIfWc3B_mqlhdb-HLSiqMt9CWUDNG9gtVOdcF8DEgXCHzWLQWhQGEN4lSsNNv_trNId58URUlAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77db0c15f.mp4?token=o76t4xtIuabH2eGwCUMOxhfQSs7IiYSJuv75OZbSX4cccKxjk4posMAcpGQvZ8JcNRu5i8qjvktrPYAEpjC0vptqwMN17WqrMkcpDswyuJdYuOj_xyNidvuSUdPd4cc0XNFUiOTmxEa1FHUiVc3G_eO1GT1afd6-OVxJiOmgBld_PKOTC5q7Yt0yvnoX6F4x_PuIu9_27Y1nheAFQifEcww6k6yKhmq9RcqI3lYFXdbncK0N8MCTZMfp2BbS3z8WEcO8fUxqI0HJIfWc3B_mqlhdb-HLSiqMt9CWUDNG9gtVOdcF8DEgXCHzWLQWhQGEN4lSsNNv_trNId58URUlAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
فرود موشک‌های ایرانی با کلاهک‌های بارشی بر سر تروریست‌های آمریکایی در منطقه «العقبه» در اردن
و ناتوانی سامانه‌های پدافندی در رهگیری آنها
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/461013" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌ منابع عربی از حملۀ موشکی به پایگاه الازرق، متعلق به نظامیان تروریست آمریکا در اردن خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/461012" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
شنیده‌شدن انفجار در اردن
🔹
منابع عربی گزارش دادند در پی حملۀ موشک‌های ایرانی، انفجارهایی در اردن رخ داده است. @Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/461011" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461010">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
شنیده‌شدن انفجار در اردن
🔹
منابع عربی گزارش دادند در پی حملۀ موشک‌های ایرانی، انفجارهایی در اردن رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/461010" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461009">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGJmv11AhoctH4x3TXaLKCILMAW84ly4x3VGtC2d6adMHeQIV489wKI54d89KdP9Z1JQBk_oWeAunWTJBrt2g_VccP_je1HdmAr-nHx8DEFSExRX67fGA_II4Ep7XpO0ZfcC5xvRaHp4thOJ8WdielkyKaRtoSQ7oA54LZadQDJJirxpIqrdEc4RfONp8iTbqCBFU52WaAvY1kflayWeEky0FnEK3QCyP6g0Ab8c5wlkWHrzG_z0asN2wwhHYjcJmQjQdtopa4u_EdKI7duS7W8QqFOEG6j0KBpVSEH7-PW5c2p2XpP0VpNogpn230F8H3Gh-0XT27OtOrVZOHeB6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران چشم پنهان آمریکا در اعماق دریا را هم کور کرد
🔹
آمریکا طی سال‌های گذشته سرمایه‌گذاری گسترده‌ای روی سامانه‌های بدون سرنشین انجام داده، بر همین اساس کارشناسان معتقدند رهگیری و یه دام انداختن سامانه زیرسطحی هوشمند آمریکا، شکست سنگینی برای این کشور است.
چرا به دام افتادن چنین سامانه‌ای اهمیت دارد؟
🔹
محمدی، کارشناس مسائل نظامی گفت: اگر یک سامانه با قابلیت پنهان‌کاری، خودمختاری و ماندگاری بالا در محدوده‌ای مانند ورودی تنگۀ هرمز شناسایی و سالم به دست آمده باشد، از منظر جنگ اطلاعاتی و ضدشناسایی، اهمیت بیشتری از یک انهدام صرف دارد. درواقع مقابلۀ موفق با این سامانه‌ها به معنای مقابله با یکی از مهم‌ترین روندهای جنگ مدرن است.
به گفتۀ وی، ماجرا در سه لایه اتفاق افتاده است؛
🔸
۱- شناسایی سامانه‌ای که برای شناسایی طراحی شده است.
🔸
۲- نفوذ یا غلبه بر سازوکارهای حفاظتی آن
🔸
۳- و در نهایت تصرف سالم آن.
واکنش آمریکا پس از کشف این زیرسطحی
🔹
پس از آنکه موقعیت زیرسطحی آمریکایی شناسایی شد، طرف مقابل برای پیدا کردن محل آن و بررسی وضعیت سامانه، از پرنده‌های بدون سرنشین استفاده کرد و یک فروند پهپاد آمریکایی از نوع MQ-9 نیز در این فرآیند وارد منطقه شد که هدف قرار گرفت.
شکست فناوری پنهانکار آمریکا در برابر توان اطلاعاتی ایران
🔹
این کارشناس مسائل نظامی گفت، اهمیت این عملیات فقط در شکار یک سامانۀ زیرسطحی نیست؛ بلکه مسئلۀ مهم‌تر، شکست یک سامانۀ پیشرفتۀ آمریکایی در برابر توان شناسایی، نفوذ و کنترل نیروهای مسلح جمهوری اسلامی ایران است.
🔹
بنابراین، عملیات اخیر را نباید صرفاً یک حادثه تاکتیکی دید. این اتفاق یک موضوع مهم در جنگ فناوری، جنگ الکترونیک و نبرد اطلاعاتی است و می‌تواند نشان دهد جمهوری اسلامی ایران در برابر استفاده آمریکا از نسل جدید سامانه‌های بدون سرنشین، صرفاً در موضع دفاع قرار ندارد، بلکه قادر است این سامانه‌ها را شناسایی، مورد نفوذ قرار داده و در صورت فراهم شدن شرایط، آنها را به کنترل خود درآورد.
🔗
شرح کامل گزارش دربارۀ غنیمت جدید ایران در جنگ فناوری را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/461009" target="_blank">📅 00:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461008">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110775d818.mp4?token=TTG52xTbUOp2-Mh42AJCtf3HVTnAivoLx8I2zw63EmUUUH6stUmqVgRF8b4IM0qm07kr3XLm65b_WFE3sneNgaVlfMrU8rgDwr9a7cKxmLz_oCvvquhseDKGLZ8pJecfSDefdQ8S9kBicvWvYHzWld27Rc9rYFVAusgfYFENyLod6KW96JEMhiWSOsxhXGCWTVsrj73eouLxRvxwo3s_tYWNjYtnpq0sgsQQ3mYhY22tqqGFRD_UVsoswofoPiUWDLE2JP0recrqg-2iOffJYzl9Z45aPK5n1pKWnBssAKtw6JWFZFYUyd0ew1Q7T_t6tKFz9mZTyGBtJoFxNznB1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110775d818.mp4?token=TTG52xTbUOp2-Mh42AJCtf3HVTnAivoLx8I2zw63EmUUUH6stUmqVgRF8b4IM0qm07kr3XLm65b_WFE3sneNgaVlfMrU8rgDwr9a7cKxmLz_oCvvquhseDKGLZ8pJecfSDefdQ8S9kBicvWvYHzWld27Rc9rYFVAusgfYFENyLod6KW96JEMhiWSOsxhXGCWTVsrj73eouLxRvxwo3s_tYWNjYtnpq0sgsQQ3mYhY22tqqGFRD_UVsoswofoPiUWDLE2JP0recrqg-2iOffJYzl9Z45aPK5n1pKWnBssAKtw6JWFZFYUyd0ew1Q7T_t6tKFz9mZTyGBtJoFxNznB1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نهنگ هوشمند شما اکنون با ماست، به خوبی همکاری می‌کند و به تمام سوالات ما پاسخ می‌دهد. از هدیۀ شما سپاسگزاریم!
🔸
لگو انیمیشن جدید ایرانی، از غنیمت گرفتن زیردریایی هوشمند آمریکایی در تنگۀ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/461008" target="_blank">📅 00:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461007">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9fzAA4iP4eecOuPNHs08K9w_BQgnujGhgJNOT3lSnr6DMJqlc_KyeN2vumhr_soZ58H11rrO__5YBx_1aLOno0NebpzZsbxDy7Bw4pl9e2TcgThT4F4dafFBp0-vSc-tJWK4ZutRpysrbDSLoJHkXKJsquW78zfIfLtFd6RCvz7YNQjERnhI3skqQ-5bd7eukrz9NCJUjOQbGF2xnOesuRpKFg3n9ym2Ke_GQuL67wb6O5PzIA4cRl21KmUQKhiGNLXBip2tXLK3Eb2x_8wmbJTTBpl-0Zw88ddUGzQBM7RZqOewHt2LQexPRqyhc_b6CN4cgDCFRAed6XhWloC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
این قرار بین ما و ناوهای دشمن است
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/461007" target="_blank">📅 00:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461006">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbFKcETQVLaZamenPZaYReOLgVGvW2Xo7XVxq288wzYBg1Ur1R7fKOhTejciT6DnSqphDH1ImyZHt3cmsLxgq0EWApKgLFItXjDpAGdvUqRpfpfceQ8YPA-OVXI7HkCnOjSC04BYWkFo9rYTDjVSIeBaDv75Oy7hMgVT5UPYC2akG1ohVhmg2LvhyLDsUlzA7KMFdXIv2Rf5c0YI_ubLYq__aRYPmyuTAj69ksZRT47sjw5G0quZbosoBaOtcouC_Fszn1oos3EyANkKSyTtPUjCZS3x0hOXY-WQuFqLMFjXke82TTUKjXKCVxSB2qN4uPS2kI_oMDE5uk2ySQ6B7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر گردشگری: در ۵ ماه نخست امسال باوجود جنگ، ۲ میلیون گردشگر خارجی وارد ایران شده است.
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/461006" target="_blank">📅 23:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLubT-P9fRWjtvc_4pMQvXkxnBQnq0PFbWbabvBArPJciPymBqvtppeLygOmvlJdCfQPI5yxX05f07IAh8uFsiSIgt4LGKPTGkZVh4TFJntDlYamQP-SH2dG3cMxafGUsmO0rQyUdtVprhUnhhLqNNdA-8wCcyFzxSW4X_ubJOLJHlBd9kDPcfR2cjjj1oJDFGLf37CdkYPsW-Po5RfJSPktJVvQx99Zm9l_BABdGcK84bwj0_snhgqBjhYdplSNy4FNhFMgNAVA9CEJV7LXZ6zurWfho7uG7u_lZN33KF1IEBuiQS9McbEBucaL-KW23R45sYnyGVuDmWv1J8z8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKbajrzIkzwTfmZLE1S-hhNyrL8DyJsGQ2yVmL7DHbs3OZDsAJP3UZhQ3BwDcMawrl29C_0lBALFe6L_Zfknt6sAqZSSUHXm7kkjMgYnl-dnZcMQQ_wI4qlI8Y8WSSFli7uT9xil3r8wfYb2KS8fBqLx5IrF0zMhOht8Pekimmx_vaU4uw9m9km8nkxTb6E853KWBYGFmemlCO_KIyl84A_WU0TIw3wX7k_jS5kgXhiHxmQa4kNrM1mLcF5cG9I8HfwucjsMLhY8W0rvPW1gfT3h0BIBxkSOvAlZ-KaXiBewH07DBGYoMbCUSs37pvqsjXsT-SccjYHcCdF6j2MMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGocNbaxVHHkAqI90LO2CdiDQq9C6I78mVnLdsNGzQs7Q2iYA7zBfYwRRRDyL9M-lXbnqHXsdNGzKsnMs7tlXObGBeWrGsRhvS16s9YZ_tkx7k3ChnuCQ_MFojVgb8Ax68DumH3m4bmhq5kzhD8QVicqdjbt8RygToDUEypeze2AZvVfM38wz7QQlrTSovVRXSTfDQcBRGvAEA9KyYQnqK5MQuI8v8zF_MoAmFbxr4hWxSj7KxUxoKi6uxZmKRG8_pBf_Zsy1JAt-4NpUmEcHx-T_Q28HiP8qj5oXfl__br99Vp1wbV6-7zIkRptl0SWqAYcamJ00EWdKlUv0iJlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MH938Pub2c6vBrTGV7KVb7EG2dWjQ9OdbGEydLYfvjMI_bI3q2G236W9lONUK_tze5eMLePlHfTB6xci-P4MrucyAbplEGEQAm3HON6qR323fyDnllExyMmquDnQYQJNgie9w5i2zy7jgUufX3g5e3qc1hV-0oF2KcjCL3F4f7Sm04wpd-yVuzMxYFzZP3ZvemiT6_FgeS_oiVGIMicYncvNM_pS7ARbWPfoWCIqmtZmIw6k0GZJY1COKzN9spteIAE5Zr1R14EMDwdRulzJcA140OiAzJmJ90tz17ct71eU-Nq0x6FrPNh4opj9EmzTHT4t1nxB0ZzCdzSALRUkLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKUerNY_rYy5ST7CQxNzc_l8rCHjxIbAW6WDS1zDenU3MQrt1IY4vJOWUej584fmxyexdax23EgLbfmgIcAo0mWvs3NP8TNw5Yx95R8xLayuW62VovIKmExA1xfbWe17XCqixUIuUSLe3jnjpPJlqz8LH4gk3Lq-39NeZOSzyWxuO6iRM6Kji3Ti6azbFPpf3JhmMYcaKu8C8XA_lJNBdco_AMUndFYq-jiGZA082wEzLCEPFKSPCZmJVVnl5nVna9ya_A8lsGBdrvRnRrf5xqHeYodhL2j3TYo8J1oviJkdvRcZ_2nG6MMc07yNuELvDJJmDZRgea6DZBw5G0Nreg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZYuQP0TMPPQNpaSLpbnGaXt8lZ2y_BMHbcCKIr8OBkwoSZCv6pJxEhti34cBmCMEJDHn6ETF43_piPw-ryCuAd09y34I33uUny1NsObuAhcoyZ4bY7zvt9sZShHuV4M8vhiewSz9ZYcTW9hDPVEKTnuMMAk-Xm7RT1AuUTHfDM2J4T2Orm4gM3FND-_RAHRYntXou7I0eROyBQTCy7xqfHDoLxAluLG1l3mTdC6F1lJQ7VwW_w6SDzbCjlp2BCUByXR4m2iaoxTpBvV98IyWZRToZDdcAr9r342104UlDDRZBasUR7__qERNFlzN71B9cUBqDlCrOa2SwjWvancqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jg5c4-zovuNuLtrIO8lP_EK6sX1aUeIvx_p6t1KOz2-gwplagm6VdnXs_W3Npj3GfwkBCGM4BE3dHsrkN5nO23yoBSviCBOijPXWIOi9mPvhnu_fRAUoFu-lJRaLT198-NSBezx9Ptflmz8cfcUIelnkJGdMdnojRgeHJI7xxc9S8C4jz3b0u7v7SF4sRxIoWtnoDkA_vtmtlCWIVveocjxs7Tbf3Mr75y9xo76Cgf-MREJl994wz0ssOSJcIPpC28Fc7q7HQtQwm8NJQH-TnzMao1sosCiyUMflwbV-mmJ-V6dpBoFURLTQjGqkwGzOaYc9x7MO8AJicVVL8KvJ4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقه میدان‌یار در همدان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/460999" target="_blank">📅 23:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460997">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtJIjt_BOcGeSBtnidQ76co5m_wJcWkl0oJfOsHmXe44ZkV-VzNkkszWb1UIyi825Rs2ncXtyk5qfT0t2-A6hFMt_1p1PWXr206Jbh-lUwnulnpugcHlVE4Wqax-JgXHj21PCr2SW_3H_hkU5txKriplgDUSfuCwBSy5dIVAfeEX8AL_1dFh6gI-7PKvCIcr9GbatWcV2S9riSCCQOqOvC7-ZanIeQtQ6vuVIe5iv0FToZXWbevAy2CtRW8Il4_sx2koIHNEbmXZ764E6o3G0Oc9kRuAlzNCw6671Ee4ts4nsjxpvuiok8dnB4K5lPWC_MlCnEDiWPR83rnFoMEr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی سپاه: تمامی نفتکش‌ها در محدودۀ کویت و بحرین سریعا تخلیه شوند
🔹
با توجه به شرارت‌های ارتش تروریست امریکا در هدف‌قراردادن چند فروند از نفتکش‌های ایران، به تمامی خدمه نفتکش‌ها در محدودۀ اسکله‌های کویت و بحرین که میزبان این تروریست‌ها و شریک در شرارت آنان هستند اخطار می‌دهیم شناور خود را چه در لنگرگاه و چه در اسکله‌ها سریعا ترک کنند چراکه هدف قرار خواهند گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/460997" target="_blank">📅 23:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460996">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c423b150c.mp4?token=JtE09HIOntmQHY5zc2wjpjbkXjOie7RcRuRy7j3RfnXO-8EovMTb_n8F2_Ue7K2zLaVGE8ili3wt1lpCPzbl_xRyZ9jxdq02mBGuNyhXZe2FwqAEZcyG3RT-LhNtvj13jHlbe20hnGnsF_WXXW-V9CZ-XNGlR5vsQXAq3ZQ2NoDGj4i5lgYYk-a-1HtmBzM-v_UCi_5Xbk5U3t0JVEsyMkXgQ3iWR2C_Ts1ee0BQ-o-d0z_Hum014BuZKVFq2-_RN0YXEoKNbJChco7eiCG6dOWbZgtNGK_PSF3cMlQNdQwnDEk07GQLbP7OW2jrt4KUqYulkJkVXOY28QJ5iTBTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c423b150c.mp4?token=JtE09HIOntmQHY5zc2wjpjbkXjOie7RcRuRy7j3RfnXO-8EovMTb_n8F2_Ue7K2zLaVGE8ili3wt1lpCPzbl_xRyZ9jxdq02mBGuNyhXZe2FwqAEZcyG3RT-LhNtvj13jHlbe20hnGnsF_WXXW-V9CZ-XNGlR5vsQXAq3ZQ2NoDGj4i5lgYYk-a-1HtmBzM-v_UCi_5Xbk5U3t0JVEsyMkXgQ3iWR2C_Ts1ee0BQ-o-d0z_Hum014BuZKVFq2-_RN0YXEoKNbJChco7eiCG6dOWbZgtNGK_PSF3cMlQNdQwnDEk07GQLbP7OW2jrt4KUqYulkJkVXOY28QJ5iTBTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از هلیا و توله‌هایش در پناهگاه میاندشت خراسا‌ن‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/460996" target="_blank">📅 23:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460995">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBfjP2mFYqDO483YeI7DO1saLSXOfJnHYJnS8HA9E62gQEEGhFcw4TW0iRof7-KWUkxvqgqBooQo0LwUFW7g_IxBMBz2IJ_Fwlhnx4682nrJLJZ29-hVw0tZLLyIqZpZM84qs3g3e8F22HCjs6FMoF-WfbNb2vnetFWA_Ac1Vl89fgIdFVKWwOpzIVQCe1MnH5_3pLaJbUctqHG7waMP7nGCCC1MbC1vGy-7T8wcrKplBY2cZkfx19IFcdZ-Yrk0wmH32SGlfXeitMHo1KSz9xFFDW2WEnw3CdBGpSNOnPibJE8Cp6PPm5yc5SNs38XzPJoQzblQ1Hf0lcMswXZmiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کاریکاتور کنایه آمیز کمال شرف درپی حملات یمن به تأسیسات نفتی سعودی
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/460995" target="_blank">📅 23:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5901e88f9.mp4?token=TzjhsueIKJDK8KWSmzb03XggoW0eK_oPghfiNytyOs6TQ42JrennE5Y4brefsuMrJYIXLDkqrOjuFIJOivSFIT5BhRwog9ywumUx_egqEIpiAdJQfkG8j8t_B1wyBHXBC4rTvkFelAUFgCHhrOpxd742iCpYMjaJk0ktLlQhwGsiE_gmC9tpc7aVQc8JT-niYwy1-dLyS1O4-iGGqs-BTeEeywi8d9Oss8a4-N3-EveS4RqkzVwHFGEllXqWw_vQiN3_lUTO0qH4FqiLY_e8rhYnbEK3U76X8FM6mtuyeWcm4Vv5vdsiU5_ruBCpLYHkGDl00X0MMgF1BYf0EfwFuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5901e88f9.mp4?token=TzjhsueIKJDK8KWSmzb03XggoW0eK_oPghfiNytyOs6TQ42JrennE5Y4brefsuMrJYIXLDkqrOjuFIJOivSFIT5BhRwog9ywumUx_egqEIpiAdJQfkG8j8t_B1wyBHXBC4rTvkFelAUFgCHhrOpxd742iCpYMjaJk0ktLlQhwGsiE_gmC9tpc7aVQc8JT-niYwy1-dLyS1O4-iGGqs-BTeEeywi8d9Oss8a4-N3-EveS4RqkzVwHFGEllXqWw_vQiN3_lUTO0qH4FqiLY_e8rhYnbEK3U76X8FM6mtuyeWcm4Vv5vdsiU5_ruBCpLYHkGDl00X0MMgF1BYf0EfwFuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۹۲؛ ادامه پرشور قرار عاشقی گنابادی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/460994" target="_blank">📅 22:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460993">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP_O2weK0_UONOpBB6FIy_kxeS8tIgXHU4kPYydTD_GGJ4c-N1Yfv-2hIFOwC8_zruYYoli5EYm5WsILJtcBAZsc0b3Ha7bzhrWk3bx48sqIjeWJfBbBQSQVu9YdtXM1zEGuIWIhq7lml0RKqAx8PWBGLA5lLL7DILVmtcXToaMOFXSP8C5Os6Htr7wTs9xakVSoNA3SeJyKKO-7XT6z4MvK0KDKWNjjX5maNZ-IvSa0h1Ha2H2wSMomB5S4rO3RtpdHv3OeJuM6duCbz8ue1WgAryqs-Oyw_CGboO1mHheYDXzDJej4Yv5ILKYr8nwyV2ixEZbiglTjMFBNj_lokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی امید راهی بازی‌های آسیایی ناگویا شد
⚽️
از میان ۲۳ بازیکنی که عبدی، سرمربی تیم امید از آن‌ها دعوت کرده فعلا تنها ۱۵ بازیکن در کنار تیم حضور دارند.
🔸
استقلال و تراکتور فعلا از تحویل بازیکن به تیم ملی امید خودداری کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/460993" target="_blank">📅 22:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7X5BOh9txVnGB3HSgD8geDfK9sd6jjc2HaPJIrKWnvFUPZBuWjfSXyEAkJ9s09jvtWcugUzL7vc7UMyAHhbBqO7HeKP9LSPIGKj_ZKpgLXf_L-6xSR8ivENrtfe045wpYWuDOoG_sy9Sh_1Ycg8aH7xvGWNDpMTb7E2L4jjuadV87ub56TUAK7rpwuE8UaxcNLwPkQSbqFmUUsDQvZFVYacz8vnQUD9oOUWwCJ5AgLK51-QecJ2JKfHc_mB0cS7rnwblWrb9T8WWCBj6gYNJxhWKdE_FtsxS6jhf-5AI_t5vwouUHhQ7bXCC0AxqIBU6bMfwbesZeLlV_Xm3dUDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: هیچ فناوری پیشرفته‌ای توان عبور از رصد ما در تنگه هرمز را ندارد
🔹
سردار محبی: شکار سحرگاهی پیشرفته‌ترین زیردریایی بدون‌سرنشین ۲۰۲۵ ارتش آمریکا یعنی هیچ فناوری پیشرفته‌ای توان عبور از لایه‌های رصدی ما در تنگه هرمز را ندارد.
🔹
آقایی بر خلیج‌فارس، متعلق به جوانان فناور ماست؛ به خلیج خوک‌ها بازگردید.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/460992" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
صدای ۲ انفجار در اطراف جزیرۀ خارگ شنیده شد
🔹
لحظاتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد.
🔹
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدوده خلیج فارس به گوش رسیده اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/460991" target="_blank">📅 22:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drVFMYh-tuendh_UUlMem_4QaRs6KKrnkA460qzrjz9aLJpYPbCNc_o4UY-T5C1kq-K1fWYzlVdlwNtQp18fWqpMWKj_y_7R2vfZKUeMFMadz2KeKFi_BFAVa2OaZp5GRsJCiyM4MTm32QRY0jspVcS6ORJi0H8O0sjM-u6dMSGDkukSoU7N0DBWzSYd8S1TmtlWFIgfvj1quItrErdL6L8AMknca0Hzqh4oHTqllj7sV0Y1xgURASCCDFHXjYxfJt2sGA8sYNns8BZJINxIWUIV0qkVMLBnFCBZcr81HiRmACpCuFKqfxNHnXwXk2ztYXV6LuvpiuC2zlR2z69pOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل نیروهای مسلح: هرگونه تعرض به نفتکش‌های ایران موجب هدف قرار گرفتن پایگاه های آمریکا در منطقه خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/460990" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
صدای ۲ انفجار در اطراف جزیرۀ خارگ شنیده شد
🔹
لحظاتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد.
🔹
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدوده خلیج فارس به گوش رسیده اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/460989" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460987">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
هشدار ایران دربارۀ تهدید نفتکش‌های ایرانی
🔸
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: ارتش آمریکا تهدید کرده است که ۳ نفتکش ایرانی را هدف قرار خواهد داد.
🔸
در صورت هرگونه تعرض به کشتی‌های ایرانی، نیروهای مسلح جمهوری اسلامی ایران پایگاه‌ها و منافع آمریکا در منطقه را به‌شدت هدف قرار خواهند داد
.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/460987" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460986">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1wBOJqRVrLZ3qeswkfc5Cdqslviuz5Mjbb6toJgLlU5hR4wX6vZlp0iAtlc4yazGKCoaY2G6mSdX9phlu7y7i4fgS5rKaHo4kVn1rpfNWPNOTHSC4vSvnIDtBWAzHjn3nbaxNpIkYq3bez37kcyW_C5rO0h7p31FG1iietB7lYbiYoNnww7DQsTOefEFMrqYcpG3b9Up1apfG7t615JGpr8qYrz0nLck7-m6cLmkrX3PkiA5cJ_a7WzMcWh0NgW9KST_v830s8wCnwxCPWOlPc_SdgAwva6JvtF2_lAlsr7scI52a-_yMNE8MlsV68prr6lgT2vPsK6tdQKg4-NtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: رئیس‌جمهور برای شرکت در اجلاس بریکس جمعه یا شنبه به هند سفر می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/460986" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460979">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvxm6Ie9T7JSc9TbE9PXCFASDGkaG-OqcvyUMNM9A1k9poY1zx3bdKGylJEFSsT5ml412VNHKD2ku6NpuOtLKdn95xjSOZX6BMBu6DWDk8_Z48EYAMwYmrLNzj7QHuV7wUsVSvLTVhz-38B75CCNRMCH4wOztoRIMdry4PRUl49noy8quqctRAK9CWKJfCO3iIDGBTWmK04iwulxNsca5ymeMEjwELoBdhrCoYzEqhTEmK22C7pU_jVXcc9BHRLvOTunTHJeswkC_xxQQcnU1shUgHY0fd8_bvkFlgOn5zFMr2e-3AalYoaWG7q69vscBrdPEwKz0qmTQPQBt7YPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTmpAd7zO5Pe3NuQbW7jipI39XB1sAQ4IaSj3lQ6yvYOq0UjSUVQC408m6c5HqQK3XMIcNePNfTDuK2c7nsCPN9Hv3kgEvmKNDIinyqfCY82BSH2AaFAG6Ww0-TeTSn8LERCNzQaKEANt7R4ks78eWCj3k37bRUkYpUlOKiq84iNc90HFN2W5q1VMTQPxmTWlTOFZaU0Km2Gjmtw0F0RaDakm_fnrgO5zWEJcztZfB3yogqpV8scMRzv_rLmmvgxl6HDtgfuesZkw3TmYEQQjVoxWFhkmHeTXiXe4foxGQi7_8i4c1Xi6WeF4tgcAIHiLeqTefOVPA-TvE_5K2J2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFh2LbhuFDMoQHvKRqaCL7jZ0N-OKmTf7nQSRMobzA47aTdb17PYeVAJhmj9j-aSAHvD-D1vWr381vj3OSLTgG_uUsk8GW9vy1iM3NXvA-ZQcOd1kXc61zT9wFksC38iqRe5YvmxMWOxatG6luJUaO3f34CIqZLvuCE30q85tCZLjGOXHuLx7zjS7DiXZ_l4cFGLDHW4YfagGm9pcyhCqUhWwunUFPG50Zv9ed5OIXn7JTEA4cOe-mDm-3eTWpcji0rswhXURMZblpCH7wzjD7QulPPIgcJirQBRuUv9kV2Qs3XiBl4cA_JDmI19ANexlEoIqudRG8Ar6wzv2CcPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXly8LXisft1VSlLGJi0eEtdXn1LDzZyPzHA_fi_fYmdJ9FrkdVbWuY8iYo2O1-IapNE6wv7v6COdmSfcbxhsW7ffS7LtpOogImxXIDI1PQEVFdL3zKfmutKs2rnzK7zf-P1HA0RMKBlM0X2Fv1vlQHSomQumD9_dkHQKNyVJFg1rPL4QjJ1e37OO8-IXats9NMtBlwRR7PDaAyaxAN-w554rouu6bOEyXFF26ooqG1loNxuQU5YGm1kz2dWHAh8_84EV0C02a0nw4K72ILug2fV4gd1_hAl_GtT8t04ok_ab_UqYRrdZOkI8NhRw5XpeRLuLDdW4tWvEd4VVJYQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GO_WcTguu9337bhPQKf3puT7bRusp8eXkD_skWktQtj7z3nxL6ab0DJqqHGuenauA6fIjWRoTotm5tQobenEugpZqoorz5ohsGC0zgLFPKcUdSb0ojkAsVKHvptl_6IU3FFiEwATlki7wLbEXDAXXtco91EjUQ5BdQv0FFCzZsmc3PkDzjTy8FMn0lXFLhpvV8m9ZXv3BHPzt5mr6j797Jrm7B8LIrtLb5kVfyHY2gXKNJvefC7kwX9-BU_5Jp3h_cXhYS1M8j3Gz-Xr64qeM7v-V-k-5QnQJy-rgQZUJGwMVS3ygyQRjvGMgxl101_LEb0jUfkVCuvGKxfGXNFH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Awzblc2T2Rn8ajXuxuYd2M20ZVW30PO-mlJfOLRCUpxQ1DN0u40BbYRuQOPOjvzLJQ4NhhOxDbCIYQjDNxd_8F2e8SDXQqWKAjnoIir81CE0iW3T9Ie4s2WvFrH2mcq4c4z3sp2NWPDcIlpB_7LR4ja1YFKiiaKsl3morPwkBoYVa4iYMGcNQxLxGmRffN49K7gZd0XNtwfCLcg1x1nQ0uPl1-2eUt3xvV_Vkooi6TW4Ohq9RHKun08ItDxrybpR3jSfbYVrwHoNneTphvREnYS8j6pVfW2O0DwQfIR4XhEEWUKiB4vOQns7RGFWZAy4QTSibd744LgG-1a1kUt0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8VFrciRaKy56gtZOSvWc4DL7uZXb7Syhw04nlo3gNHQWQD9dtF7Pzwlj9HdBnOAbuAD_j5ueVu4qJHdSukRqH85FiZ7kKNL-1ijryhQllEy-DtK4_ndRYDUlCs11r-FeD5yKwNOBFLrccCmFNdb6RQIEUcJdSnH6Vl19FT68-HcVpud1gpdv1elG6F3--3hX2MGfcw03S19BYNG4DMnmAjf_6O-Bis5aPWQYqo-3lE_XWyY_1LhjGhzhnJpOyKvbBI5rST8monV7xnGxfhxgsmgIBqWyLyKScPhHqvJV7F3kru8raESR0yZVvTY9Izrz4S0g4L-5hEnakGGRPqbLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفر معاون اول رئیس‌جمهور به قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/460979" target="_blank">📅 22:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460978">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYW_d0WiF_xAWnFpOgXk4x9nfek8a1x4DRpd9IgPXUEsxYdlK-r7GbIJdrJd1ywAvd4Fhl8Gbm7Uslr2fhrKvQ2wfGEjgAl6Hcx4SIidX09VKOOSHc-WV5cdcGzMCEhHZQCCiRlh2W2XPj9zGAPe3XUaPslfh2CaApoqODq8JA7PcZvx9G6Jtmqpi7bDAZmeo-P-esgWoya03cGV6dLGEN0qoqTKXsJi5W14OZ8xe2b5Qhd5Nvl8_H6cMIKYBjcV258oavDSZR593fCwhweOjMjGAhJi8A5iPD4klYy9WOPHY93MijgTQHlyE6wBIZM2BgN8gSslVL4BF9l-fs3D1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: برنامهٔ زیردریایی‌های هوشمند آمریکا ناک‌اوت شد!
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460978" target="_blank">📅 22:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شکار یک زیرسطحی هوشمند آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه : یکی از مدرن ترین زیردریایی‌های هوشمند و بدون سرنشین ارتش تروریست آمریکا را در ورودی تنگه هرمز به دام انداختیم.
🔸
این زیر سطحی هوشمند از جدیدترین تکنولوژی‌ها در حوزۀ زیرسطحی در دنیا برخوردار…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/460977" target="_blank">📅 22:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANDrHocv_aHMbAWdkAaA9CI43YcdUHmJ1SuDeC8dFUCgRcKx2Qv6wFu-6xyQ0PrtHOG3BtoE7unSUAOw-85561hhdoj1J8ept0oUz3UJIlUBVBJW4TEP1wZpUl6Hz-ef-w9ZKkNp-rKURckhyKRJJNsA5ALJghf4EEbrOSruOwLZ2XZh_6AC60uRacZmEFr_QhcAsN0V5O3RZv7H_0UuwzSEiYBQdNPVaHTN8RyAtOBvuZ89uYqg04Ew-tAd9OdWnX7P7XhN5Sb9JGi6UgbalyBvSwCTqwRRTnXjdLepIZGiLB_Wy_1fBwPuRbSjhGX0y9ziOHdPaVSTFreNsKXkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان صریح امارات به هماهنگی‌های امنیتی با صهیونیست‌ها
🔹
وزارت خارجه امارات در واکنش به گزارش‌ها درباره هشدار ابوظبی به رژیم صهیونیستی پیش از آغاز عملیات طوفان الاقصی، ضمن عدم تکذیب این گزارش‌ها، با افتخار از تبادل اطلاعات امنیتی با این رژیم سخن گفت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460976" target="_blank">📅 22:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460974">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBAqB1zwJ29a__B9xLoD_Xbqq7RuVfPPrSVMzh-ulA4EQr0-sVEDB4FHO5v07yueOCVW9AdPUvMLZ368VfRFI2f0ptNS4NE-QKgu1olkUi3UHx83b98vYXu9d-bs0Asn38e8Rt08MYH8MpfIjNADoy3IfAEl7tawplz_wNDxO38nJweo4s4N9oPTqgqfum8tiaWN720w3rZHKvZHS3Y6WXWfqr3gGqzgFgO2PKramLGrb6FTRtB05_XarKiAgumrULE58Mr_9c1ObDEc0iocbewYZ3T6c0cpgvhiZesMoBscqO0smlFB2mWMcH72u1YPhMKaw5T4TtwmnKAfZTFYcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنایۀ عراقچی به «راه‌حل خلاقانه» آمریکا پس از ۴۷ سال تحریم: جدی می‌فرمایید؟
🔹
وزیر خارجه در شبکۀ ایکس نوشت: پس از ۴۷ سال تحریم، آمریکا به نیابت از اسرائیل وارد جنگ با ایران شد؛ جنگی که پیامدهای فاجعه‌باری برای آمریکا، از جمله برای جایگاه و اعتبار این کشور در جهان، به همراه داشته است.
🔹
پس از آنکه واشنگتن نتوانست با تحریم یا جنگ به اهداف خود دست یابد، راه‌حل ابتکاری‌اش این است: تحریم‌های بیشتر! جدی می‌فرمایید؟!
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460974" target="_blank">📅 21:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460973">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۸.pdf</div>
  <div class="tg-doc-extra">3.8 MB</div>
</div>
<a href="https://t.me/farsna/460973" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۷.pdf</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460973" target="_blank">📅 21:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460972">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569380b929.mp4?token=XK3QqAAJSz9c4dhqJyugPZ5XL68NNjqZsyUIrRsAlqqisUs_eu_qQkdw0gvvRYyAcCnvbDrEoHyp0m_DmWtnWQaZ_W3K1IKmA2pOFyOl2urUphT-ZdDgSqSKl0X0JsbvcyRmWC7eH-DU7YtlXLTssXcBmCTipyLBiGqEuaEMgbxHBESLM-fIUKPKpazX_AhPBWgD7IrveVW9ejObcAJYleczEmUPNAoXMoAwADnlCpHWdD4rPPa5sXbrxvLZ9Qc7s5vwOQx8DKDxUdQ7UYyXNdg1AHrgS8A9OYTkJmLJhvjKuClBA5s4cY1Y-GwrKHju-Q6Qj1dRYLz5Fe462XBygA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569380b929.mp4?token=XK3QqAAJSz9c4dhqJyugPZ5XL68NNjqZsyUIrRsAlqqisUs_eu_qQkdw0gvvRYyAcCnvbDrEoHyp0m_DmWtnWQaZ_W3K1IKmA2pOFyOl2urUphT-ZdDgSqSKl0X0JsbvcyRmWC7eH-DU7YtlXLTssXcBmCTipyLBiGqEuaEMgbxHBESLM-fIUKPKpazX_AhPBWgD7IrveVW9ejObcAJYleczEmUPNAoXMoAwADnlCpHWdD4rPPa5sXbrxvLZ9Qc7s5vwOQx8DKDxUdQ7UYyXNdg1AHrgS8A9OYTkJmLJhvjKuClBA5s4cY1Y-GwrKHju-Q6Qj1dRYLz5Fe462XBygA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم شهرکرد در شب ۱۹۲ تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460972" target="_blank">📅 21:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460966">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgMPl5puFFMiwKGK3weRufdI7n6Fh4NlZ1FIT4HrNufnTullEifCoahFOJPLYJBCI3IGzb2CJs592pEW2gxkc7v1h0hNaDcRpsEtppoap8EL-nWot68c4xd69WN91eAPCsk-eeYnnwJcOu9u3n2r3DoC4G6uMBS9dEoD7Q4YuQBN04_kG4KIRiDvW8K5F36kBm1OWgHJGNweixJ1NlHHdH4srsbbVdDq-M_98fibcpkK4wYaITaiPZvPj-l_IMHQ_QOnZEbyNtCr9rwXENGcjarD498OC83EHx3wpS77yidsv7M1rcUQk73d-yApzuxKo96Gxsp6NWzFlHI7a0Aw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pavNF07uhBM8E1oOmYwVMQDXPrnzHpW79leDW6hL1k55jRCZaPN7s20gr4a2wWpslQPanz44OX4ChRJdeYX1rr-DvOVW9gkuUUuBv8atpDynjU7TJm2nGjtYXma0EDhIaKP9qnDIkd4Vmp9eYMQ-aGViG-YeaZIWCdm68EMap5RyO8ogHB8cLcDOHGw9HoACuwN6DrbdkZ1UzwLYmg6A5XI_GTBt_1f_zu_iSPdbAkDvVo2ZNbgUQNBxhll0qMPSmzLUcUAyMbSMRbdGESKp0iTzKsfT2mD8vde7_JeYwNKw39TqqJ9fz9ne_nWG1JV5QaXhHa8nElhSh63tH1Q6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3EvANbLfVXJIok32EmdPm3JkanqF5ESg-PVxyYdWJv9bULBe9a62MUkJn5x1UqWpWKmHF0KJtSrEzmwuZAgUa7LH5hklPlkvW3q9DBxy9z_PcAoroQy0xlGLH6lzROzEkkhjTh72tcBjZYh0roGacQVDbcTFH91XUDkt3hqu5oZtBUPavSpOc5mbv74NtHNXi8h3qu0WxKL3WjBDg2miaHiFSowvPiqscu-lnD7epnkFRdGa3KyhHLrcCgfixT2nCU6jWu3WArZrAUWfqAFSgcPRNawxekkTpsdyBGGO6g6pnQ7ZDhIfVPEZqMJqBycDeimUZwFt-DOYWNWEzpapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CsAbDJGeiuPInwK8A20vlbw6H3Z0VBZtTXgsqkEvEhs33yRVMFxCQKmlHiqfSt2ElyE4uKSnQR5HCoBSuvYXa9euznlObAyyafY9341J-O8k3izksQfyAIQlwDyk07pOfAcFCrNvsPoz-FBlgD23CYhZ8Xs0DeJVphLh3aYK0o4gILfBa_ke09bxLWuD10G4VWdo0Nta3XHkYqh4oYG8Fw9SwgfcuDgAIrL1cSYOAfo8aCkKwB_Ewcct_sfIwglcobM1fiftVkHegoVKK14_QzV4ZkRYSz5eiGGOWiB6_BdJJgOo4gYaTFruW6ajKBXqEH5Cvz8Rs-1bEIXAkh96qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzJ9_SH0Q9o5zKYHol23QKf1zLfCc0EA5L4mPPLkK2FaexjVPSP4YcMMHgQ8fcuEgVyhygq8kJ8PQr25QURPByZyDBnaBh2sXklgTDHuPNWqfjUoqULJ6B75wZn7zkCnLiMPEU3RsYZjpUDyq2sPbNKsNbY_NKsHFnzPOeVGGqF8siksfg6z7QEqHnKxt0ujvEBGBO_ECMoolKcVfNBJV_8eeknZW1kI-HcODkpLmmDsKkdk2QUVvMwI5fp-czbvEQIGIl9ADengi_R19HuyXDHT6KawgpulU6ht3m_0EADrWQgcCOlKDB3zVbCkqU4-IvoZfA6ClFn1L8soBmzXPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbK8yt-u6iFIUe6hfg-yRaNaifROdVKw6VCfk-5Zdw_PPg4CmPj6DCqpljnRF_dn7w_E2fy1AUwAMTMKmmJ-yhw8BvRyL5T4HiliYk3Mmajc3va9sPq7cdUHP75lmI_BmKYpNyGcNDxTi4LxXxZ7qmeBX1aDYbUghfvyRGHjVzpT0nvjJpflyqU-yQh1s-EP_qf_maBMu4t-9qCvFjTDqS0rWmJurDfexBDigmNmKMauLq5AwovcX9Grls0ANKZdystR4ZA_2Nw2hcgxI2cD0L_2s2JuCTuuCVCB-n1UTDddbCfq0j3jgvh3rv4SxcuObjPRzjNlGaeSkkfXjuAKag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
اولین تصاویر از زیرسطحی غنیمت‌گرفته‌شدۀ آمریکایی در تنگۀ هرمز  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460966" target="_blank">📅 21:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460965">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f351d7a56.mp4?token=G8bCNlyJkBtdXxX419EmWzLpEdE6JlbHPTj6kZA6QISf7nu49OjVAI02EubTNFLK4-dVs2t6vEgFwFKKvRRUIXF2yNMuW57CDUxCCIQ5cMfsYQW5Hmjn34UFUHHpBkcGuv_QMqtwY5-mwgwL39xi2x1X2RWuUYxenmPaXna1mK8EJQ35BdxG6NVnTzJgMg3sM9Pl2641OWQOiJlcfUMe7juy7yEH6aGUNG86y9a9LyJzXnxiWCszlC6Cay4xXJVREKKLSwN5XrkGAziVkYEMAb1mk7AZYA5dPilXmsbzILXKPjXhDSMEOy2V7VpxiXqLWKJrGdojQoNQjYM2M0Nflw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f351d7a56.mp4?token=G8bCNlyJkBtdXxX419EmWzLpEdE6JlbHPTj6kZA6QISf7nu49OjVAI02EubTNFLK4-dVs2t6vEgFwFKKvRRUIXF2yNMuW57CDUxCCIQ5cMfsYQW5Hmjn34UFUHHpBkcGuv_QMqtwY5-mwgwL39xi2x1X2RWuUYxenmPaXna1mK8EJQ35BdxG6NVnTzJgMg3sM9Pl2641OWQOiJlcfUMe7juy7yEH6aGUNG86y9a9LyJzXnxiWCszlC6Cay4xXJVREKKLSwN5XrkGAziVkYEMAb1mk7AZYA5dPilXmsbzILXKPjXhDSMEOy2V7VpxiXqLWKJrGdojQoNQjYM2M0Nflw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار جدید سپاه را بشناسید
🔹
زهپاد Dive‑LD یک وسیلۀ زیرسطحی خودکار بزرگ یا Large-Displacement AUV است.
🔹
این زیردریایی حدود ۵٫۸ متر طول و نزدیک به ۳ تن وزن دارد و برای انجام مستقل مأموریت‌های طولانی در آب‌های عمیق طراحی شده است.
🔹
این زیردریایی هوشمند می‌تواند…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460965" target="_blank">📅 21:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460964">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206796ec3e.mp4?token=OfreUamycP4Ma2x2d4CCVMgC3nAfuImZ6clgspGVOpCMkTwEPdFfdS-gAjgC6_BSTWpBUcUGm5VTuJ0wLidzzPF8HVOF435f9b6H4VGpvl3lVu6dwJah-SdvwMjSHZTmIhSnweTRM4W1j58tzsuQL8nTFnPM91tpiBZ7Vhfu9tuShqkqfdtaVUELMva64tzQSPluifP0UO8X_VZ0NzWB8Gys-IpNsVKj9J5vCeew3ZCgPDMzRJMoeiyoA7JLpcSUg7BlW8SWReWNlGtUAb-sqZWL6n_59QIvLTkVQa6s0tbbDtYSQk1-Z6iIbUGdfzkv1kDYNgNXL0uzoUpdtslRJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206796ec3e.mp4?token=OfreUamycP4Ma2x2d4CCVMgC3nAfuImZ6clgspGVOpCMkTwEPdFfdS-gAjgC6_BSTWpBUcUGm5VTuJ0wLidzzPF8HVOF435f9b6H4VGpvl3lVu6dwJah-SdvwMjSHZTmIhSnweTRM4W1j58tzsuQL8nTFnPM91tpiBZ7Vhfu9tuShqkqfdtaVUELMva64tzQSPluifP0UO8X_VZ0NzWB8Gys-IpNsVKj9J5vCeew3ZCgPDMzRJMoeiyoA7JLpcSUg7BlW8SWReWNlGtUAb-sqZWL6n_59QIvLTkVQa6s0tbbDtYSQk1-Z6iIbUGdfzkv1kDYNgNXL0uzoUpdtslRJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات عرضه اولیه اوراق سلف موازی استاندارد سکه
🔹
عرضه اولیه اوراق سلف موازی استاندارد سکه بانک مرکزی با نماد «عسکه ۲» از ۱۸ شهریور در بورس کالا انجام می‌شود. این عرضه شامل معادل ۱۰۰ هزار قطعه سکه تمام بهار آزادی در قالب ۱۰۰ میلیون ورقه است و به روش حراج تک‌قیمتی انجام خواهد شد.
🔹
دامنه نوسان روز عرضه ۵ درصد و دامنه نوسان معاملات ثانویه ۱۰ درصد است. معاملات ثانویه نیز از ۲۱ شهریور تا ۱۸ آذر ادامه خواهد داشت. خریداران می‌توانند با کد بورسی در این عرضه مشارکت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/460964" target="_blank">📅 21:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460963">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
العربیه: اسرائیل در ۲ حملۀ هوایی، مجددا منطقۀ نبطیه‌فوقا در جنوب لبنان را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460963" target="_blank">📅 21:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460962">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRSa0rbGbRyzzVm9-GDvMcvNOFNARFpgkboFG0hc1kMfGyZnEKQ5WkSc6X5-xLVYO9Fba3p7CQREtl4U3T1XJv4vWwuzPNGjwfShWCURof_Ri7lfwn9wfPexSrXeDoSKh7TR8VdtmILc7qpVaREJaLu5Q4ZIitXGSdLCEkPaSs_gqbPZpz-CSmAWLYjLidhSFtsOE0Iodc0D0nsWA3Dr_wMSr5EgLn0KoTijPT0GUlKaj_K1gQ9n79AtqoFKIt-Ghppg7fbL3STzI5-q6si_83_5kxC-XKVTt--RAo9tDzArwEnwKQXstZ8i-jPjp6SEhZyqLlAL9jb9xds0Luz3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت کندی اینترنت در ساعات گذشته
🔹
مدیرعامل شرکت ارتباطات زیرساخت، علت کندی و اختلال اینترنت در چند ساعت گذشته را «قطع فیبر نوری در ارمنستان» اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/460962" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460961">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تحریم انگلیس و فرانسه علیه رژیم صهیونیستی
🔹
وزرای خارجه ۱۲ کشور غربی با صدور بیانیه‌ای مشترک اعمال محدودیت‌های تجاری بر کالاهای تولیدشده در شهرک‌های غیرقانونی اسرائیل در کرانهٔ باختری را اعلام کردند.
🔹
این کشورها شامل انگلیس، کانادا، فرانسه، دانمارک، فنلاند، ایسلند، ایرلند، نروژ، لهستان، پرتغال، اسپانیا و سوئد هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460961" target="_blank">📅 21:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460960">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
مردم به امر رهبر خود همچنان در میدان حاضر هستند
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460960" target="_blank">📅 21:06 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
