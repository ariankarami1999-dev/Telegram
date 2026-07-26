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
<img src="https://cdn4.telesco.pe/file/OcA9oU9QPTndMhxsxWOTHCWJ3bZrVdUZ5TrO6Hw4XQysfrmOCnhntcXrMhTkC6Fl8wbodEgL7Y3hExvjtJQ7lbIqUG6pFNOmGNHc6XsEIAB4pwJ5O3BCBAt63X5crSFWwIYWVrRFSaqf4PpuTSsRWEoGEx_-a8P2_8Wds8A3i-NK-5PBaDrUfV_KgBRohoSK3jbOnushSuB2yj-7chp7JqIX5m1UtKsS27Xg7igjtHL3GTk3x8NdAkj3N63LukTd0Uiinz3lSpWvSq1BtPe_2RVkXQhkSs9DeIsSIHX_H76QA9UShyZEQgC3qSLJ2c4_TWAVajQQpAnGxH-QRHMDUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 587K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 17:54:16</div>
<hr>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2VW5LJvz0BUEUutl19NASI6Boupbja26bx5avyWVUEeXIRrVN6G8tVQCaX9aanxLeJ9_YOu6hFTlyofvG_gOM3gW3jWd3dZR0me7wx2f_lwp-LOEsA6DgCxqCfgmzrMh4V1wo-8tyMmXx5QWADxgJn6Vf0axmt11OJF8tPReH1D1nmWOu-9FuW-pBOHRCJPjeolWqlPWTKAmyvATvwFQ3EQVK28Ycnwq3DOjYZQbw6VI6JP0UcNM_7MWlRmXJp2TWiQiY9aIV-QBhfjWiNTjJXTD3yMQfsMN7LRxTs5A_YwlOwnvR0uvf3MyCA0Th-uaRh1nGVDvMD6xR6rujldPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_sbgI_3m5iiuF1qwdZCCWHQJDzRZydvEcz3-rQ_U37iX5Wqs88AaDA7ApNZbGxsZiWe_8iitLuQq0y_d2GCbTyiVMO66kG-mY2sZ1hCbyWpTB6pIoS_si6rMCBlPeElp1K_INKPjKLX6BQAW8SQBS7hyUSQgKtYZsCtqz7lwpNmzMXOL_WqpSsttvHBkzFBX8HN1OUIqB8XNjI2weCRQ0Ml8P9kXf3hPlR3czJ2AimEIyMKtvH3Jcaq4BxXwo1wqEJeQMpIyy06kpvmFUKVKZzvSST-QEFmrQyDr771N-KqkaNTI40WqNPVfL9BfsPIxjBYTWZVZZaGKHjSTzxceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26553">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spAe5Zw4JmryIT7TSxJ4faMuko2ehzuzV_gHzfI1eVeXEZgEkHAv5jRZ5lYH472lDzfXvMbe9YlBFV1vMeDC2g_0BpCiqgitkAYM6cP_CzG7zF-NX8CQ5tGW4MmuK8sHP2pX4GhV9Nvm485w8XxSFPUt1zNhjiQZlNO4oHFQvnIsKJbVPU8u8befCldC45RLnzfyVKqtnBZi4AYZFVGd8R86_duQOFbAs7LpdHcN5gpOlbwIMKlkFagQUa4QFB_3uCBfES4c6alZvj1DQu6tNswQp0IqFzTK5ZXHUx4BFA4qhUqqpWvcqP8kSzH1v_dNYxqSy63pKLMhmEYK2MwqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛همراه‌شب‌های‌فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/persiana_Soccer/26553" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=b-e_2oXw33rXDKWTFH_0ywAYWsd6WzP7Cr_95KNaKYzjpMcbbCP1UDphdQNy6lP7bnK_jp0Z5kFUh7qnUbiyedfrCOSdjb325gaFuMSAWkfSzIh99tj3JlAwIW8gpgUMgpdj4iWZs1Mm2o9G5G5nxxtGyrlV86LqZmZMbot_OqerwNTMjYBwwybu-zKsQTeyFIJSbxgm3xe-UYY9y3lneskU1kZ2QpUC4nJYindVzXHumi3iHs11mOE4ennCIu4lV9cUtZ7ZSl_YC-pDRffpoZ9wZrv0MW6j5PZO37ubwTmfNDlVu4TLyrNgX3OKutrim-I-QrlV9DCSRmb60ICAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=b-e_2oXw33rXDKWTFH_0ywAYWsd6WzP7Cr_95KNaKYzjpMcbbCP1UDphdQNy6lP7bnK_jp0Z5kFUh7qnUbiyedfrCOSdjb325gaFuMSAWkfSzIh99tj3JlAwIW8gpgUMgpdj4iWZs1Mm2o9G5G5nxxtGyrlV86LqZmZMbot_OqerwNTMjYBwwybu-zKsQTeyFIJSbxgm3xe-UYY9y3lneskU1kZ2QpUC4nJYindVzXHumi3iHs11mOE4ennCIu4lV9cUtZ7ZSl_YC-pDRffpoZ9wZrv0MW6j5PZO37ubwTmfNDlVu4TLyrNgX3OKutrim-I-QrlV9DCSRmb60ICAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFyIg9yz0mLAbJarvskX-v6b0-vGO8fs74pidC0m9FfjRMcbS3PGev05929daig8YJUsFFMnKPmbboHp4TvHGhphGbNNP7DIuPoasoSak-LfpYu07GjCAWAmwn2ug1Vmjxebm6enRy55SEsCitBaMnXbglLqic6nsNwMnd8IPlZyTvpPtfI8ehEpMY5xwmUtBTd_lKBEwsb-hKHnirNhZOwPfTnBrtwSDMm5C4WsjsEVAbsJhkFPY8GgkvDgjFV7f8i0l0vG7FycBLYoZ2_lFYbXPxlhakwNaJnX2ZUHYUyhfZ8xQj4EFrZQ-Bge94iRKfHIo3Jxf3FJpKp6LTG15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjkJkh0qjA_6d4vkFa8nhklDpj6-vu5CknE__AK4VkZxn4et3YjOnLEwgNLDNecKj3CwHaHl4cinPKgFPQy_8ivDcZ9xA-60YNiwFLck6ZaMMgwmuVU5BPwzpbwpxI8QphSP3PEdm6yOcPtLJTjdHsZMeXQDOBpHik5N0FML-KOUUBTuFW_ctJLKmXTI3a0jKtbhjaxXGIgNquQNuh-qqoUCT3oAKx28rTMu-ZHrH9fxBm7UbCudMVbSt0sefxk3FvBJiRgM35Td48CBWNAL1vsAyUE7cZRPNGNyZ1DPb_eS4Zmqfoo0Z2VY1XMFFG9jvLyn9jWCFWKFWYQaZPlx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWoPgrCrjqds4K2MQoABNBGV6ivdfKIznpVvNneZnNmdqve7YVYIt71shdCVRadwIa1VFsnQjGuxyK-7svyOHsn5YoRt_WYfLZcqdydZK6YwtPJglGwuitJWXN-iMBfXwMOHboDHtItBp6RecWPpZZpPrSDMLDUuBB2ODyU50_YjP39qVuF7VLKEt5BQ8TajfHXe28FyqaYxzWpu0diL55d2ljO8Czusx4QG6LQBHvix9sGM-qk0i42siYM6ezBqjSGJjodQzTYZqovw0jdOx2alVGYgRuIE-0Uno3MaIttj3PEGoYRx9C8IM9bL2Mf0vvwKKHL-qBth_mAM0DrKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LElJA7r2XpTHYq6qzGDo4YfuKN_aUJTuyBSAmC-XqXYOIZxL6dx7inq2qQ0Y8Y6ubt-jwUNEgzPEmm2fFLPYKROYVAlxOlNgSwL3i3K5ruxrJysN25oznwcUBzrK-gWOVzVfSTPEB-Yh96YUEVMOuhlLjxBAFKzEXd9Tlu-ZPFKOoo3yfgwnnPSVQzLDI35ZGU6XWD8ecy-gGix0E2_lQcK65AvEiwig5eDE8KT2mPB96ehN7fHhnxlTQnqrQpgYyVkIS7MQljcOfwZSmgk5_j2GadpUTiaJl1kKeglxRXX3jUXbR-0PhoEt_nuwGOY0ctxW9lOs-PYFTA9PmM1Jfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOVkt5oWbC11Gtq8YwTWAUq3XmCP1D8_VxYhNGsSIAEXYnuta6Dswv0QojwOqGqdw2gOoLkZCOLY6YSNGTKHOaDripBMiAGw87QfaMelVNghDWeZqqAZOFYwqGG3aHaQDUjiUDCCNalLdA6xeNPZtdHyCGlEU9yPfW-6imxMjjWHwmrtfIs3nbitxc45SGFUJ6kGLhdqovFW7fkkO0aPE4ST7plrAJkHO1Z9JMamDX1GuhxRt1Jh6r1mCqJpx_c6SRa5wEJUDahw1O2mpKLFLNthGyLESSAe0clTVtGjuGnAd9VW8jL3oSvG5z4J_HrqjP9i81NfYh1Wf7mnlMg6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36of68ua5lMn12R2QEpJJfcdDOlHb4evFa_8L8iawR4te7QfV79cHW4ThVM25d60DeY1jT-m4_bOf6pQH9A3xjdTK1UIOHopF3R8FqTycxLR2bni3F8vOX5oyNB0nk4Eb99Q0QpqEEkV8BleoeLazOkdGWMvGTFBxbjnvZH-lCqeQpVHWI2sCOIEhzgnEoMQCa7NXZnvEuXi8eEM6NdXSLxRAYIZqtIRKoJPBTFgBZhcV43ikPvS94tXLnE9utRfu7MYtTlwgmS-qnsR7YjaTTKXFDU5afFcemGwcVscNq5jbXC5TyXLkOdefCO0AXaKodfqqAN-CmFwTN8rlbTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8HVOEFgsqTdh6EGiGM0nhGO_JGjDm3vImg-gyyb8Ac5tAT1lw6x4Hgt9lDvltZxdufEy-0mro-E6gj6rUDvKhYMtTtUUtbGUddymyAMqIJzKpJOSWyDWsz6Fy5eyEc06DfveAuHknXY3UfI5cBfQ45u_YqA9t9K1ejwnhcPGMxgNOEgnXcZkJdLkADLyg2dJ3lax3wAhi_EXe4SInJ9fH3aAZ8-DgLeHzgAFP1ig-xcBNObUpatafKXkKQo3d6Dz0ZUc7tkciOtpTvgvFLc18g3sQJnthy7OTXPqZ1Nl3ypxI0bPpRirQZwR0lfnEfc7UxAFpIuKCb4_6YkR_FIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myEUM4LfVoGAktSpz__EHsRUJGm-jbzTAeaCzIVL_kElalS6SI8qrXSGDalGv5XM76UaGtwqXiLeC_bcmB6JoffKHuoLINqAQ8H3OrF9bULvuOFK_eFibMsRWrakoX4ksok-f44RHDv3NBQanfGVrKDR6FhXXuVe2NsnrBp-nGpYuoihTyXS3iBs8WNSB3eonbMhB0D_v2DDsc57nsa6c4mHyrwN7-2Bne7gQTAb6-KuvxpfAHzEwjTPlRT564mftQ-QEAGKZYPkyh_5r_Uz734xacdV-nXhDpxZU_835oy2f_FNMlhTXQGXeiBvT3QmIOgprLUs5gyO2PgQ91zJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn6a1eYzY7IAMvsK7-_3lQB8CDdM692rqGEBTMlN9MJrUBsqso91MPF_koMSl4Xm1kG1SuAkDBmSUMm_ISKCS7G0TtmF_XvBueiv5ACIzyn5RPy1ZYtv3edgv6sJGCD_na43TUosZmk3gc9IPLqpN3BrPuA-z8vmz8JmZ1x0Nmuc9kttU8SWXJagQS99HuIp5MryEmAp4Y6nFOTnFZilFlDDLNp7RiV0M8oiNarubpRhFjfvkL-28bAt_NG8AKjUoQj25uoySe4M3VJEKwq1dfqx8SOTGRti1T_H-SXqyaBPI-BTOYmf0TKPI5PKjqRRq7TGBKuremOmbUhQJtq1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=uwKqCZ4HfuM-1Vvha_eX4JEMOdLMHTPatNwE6yBifbfS3lhCYqJA6NdILpk3CwWzTj4OE1bpZPjRGylhDVNYHyBSahdEqU4xF4SxdT_7gf-cNnF4bpglUfFohO2HR4pkbcPI9vYDg-Yc-G-CmsvHU34pf2wVKn9oReVCyYDV_1hoHP-b17sVfWRO4TLl9RkAPUrLixiBD9B6ZAq39KQ0xPFjk4J3mf_ijpR3FQuzTYbqt9hguyrA433Z3YvLtjentttnJYwCy5Tg0nPo6chTzYFEocYw_ZQ98RjTzS9cIWqQs6WhEA-kGLFBBxNHT5zUmbrQjAnAgAE3u8zvhlMjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=uwKqCZ4HfuM-1Vvha_eX4JEMOdLMHTPatNwE6yBifbfS3lhCYqJA6NdILpk3CwWzTj4OE1bpZPjRGylhDVNYHyBSahdEqU4xF4SxdT_7gf-cNnF4bpglUfFohO2HR4pkbcPI9vYDg-Yc-G-CmsvHU34pf2wVKn9oReVCyYDV_1hoHP-b17sVfWRO4TLl9RkAPUrLixiBD9B6ZAq39KQ0xPFjk4J3mf_ijpR3FQuzTYbqt9hguyrA433Z3YvLtjentttnJYwCy5Tg0nPo6chTzYFEocYw_ZQ98RjTzS9cIWqQs6WhEA-kGLFBBxNHT5zUmbrQjAnAgAE3u8zvhlMjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYi1qd0y94-tUhZZ_LDlzg9JxOlwB2-qt09RFb0IR-L8r0CfMAl_bP4gObtynSDFG8totKzSTiVR6UTPWpm1aP0s60ZimT_Lv6JB3VJVJBrgxzIFUYGWLlWMD17PUcFfrOFMPqXm4PJqN2jBtz-PKZ_PKTRMRkxGaDsCpatbO0paljPn9aActhnAAI9txAJ4x8MjFvy4EvpjUaY6u5Ih_J8NY2_y6dm9RSfLfX9r-7kZiXVu3Txbrd9MhN2NhkafQN8gshh7pvxwtssnCgYMhPkTEM_lSgr18kotCvwMkwPIFPI169SoNqqc2jR5hUOPTSf9GKQVu2HiOcfhvU3O5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuC6yZ90xYW_VDFyxdjZ_6EVQeoT1titII7-PxI3nCeaBrfiBRZuSKR6L2i5r-zOdUVxsLa2dlY7yj1gNWCb-mX8ohuc1wm7V6Wr53w5g6RTfKv2boGznc8Tdn4p-CHRvAgJ1jKV1J9VPku8f4zyfllVk_s9607WrgKYnwmhutBDdsODHk9vFJR8aV_BrrwNiLOY_V4wH5wHp-Sv1MjG8ZOmyha4XKY8QHc3hB5C3S5VYFFs2HnRBb--upnWj7Tdygwp061HPu4QAWJKC0rpVV8CVjsQI58FIz_qL8Zx5h1bvWmuCxyLGtQzW_tTBHFTDT4r09ZJw8_TW3myefXafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f10IkFTZeAnG0mQW9KqpyZWCcyHI557L3hPbGBSpdaL0hB8Xs5W1KzTb8jvqEfqx4ayPhp9YjkZLSSgHXJt2X3nA1xxL6t2hHmLhraFTkc4131Cv_Xo1HsiWTJX3m02l0-OzYYOnW0wiInvXosq-RQJX4odDkbsx7WvXhtUYVIhGr_lj-FVN81zFz8_zweL9A60905vC_9gdTw-KLBBcL-OAY2GGoQ8bny1XoGk9ExIGXKfkM_Eh5f0N07a0SRZrWc-W4WL3aKDVGFKffwu0BURKJHFnleX0F4svzOnneB70jByud3cySovsdaPJgLHjPdjZHF1gqbFrogGaNj9U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4_2XYAWcZ6-9bsLS50OGFaaQVpEr_QXGe4L8djHhp5jf49KotNjj3xlOb6aduNSfalLai7VfNg9FGXO8d7LTdfqUOVR7MQNBHC7b3MKYsdbX5-Jovz8zNkzvttgcw48R8Xp_aGzlXXFSL71n__COuGxuaoJgPVNafELt2x72N1PgBl31GSLxnXmcygMDNCD4gT-vS7bzfjONF7xeBq0vbaavsGckLG5b2BtZQq5uxHCFVfK8D6QotcIC0NXMlMlcRCJR90SwT_i8PKHiAdR5joMneqft86RJrDtDtY5DQP_jDfTiS_7fgo4EoUhhNTtLG-rvCLfWbupjGu538cmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWwuJTUf98mouHzKY_GVZ_-IvaWVMs5S6bE1iYKjUi1qulLhdGtkLmz7vmIycghjTBAt2tZNIRYx6PeHcbyHAPO32Fu0X81Q56qqGpJuQMk8EiLnq8NRevfwJbVTAsnm58pPVeY5EhKVW_rz19BwPhYV7HCIFkuFILbgGuuG4FrdHvs2Ex8JEz-DdcSL5mXqu1dumDlDUM9H_MwGgKekjjAW-iH5_vPHZOXyeKV_tQHzWWjhS_zIj6UO1pe8kwEbLVBTWCZYq8A3GYupmYG0XFnCsj60NYrLbByMkPKwdqD_fgTF1TFHFlf_Vmf5aZ5gwuk4DSytooypq_pKAPAnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=LwxnxGFrKzPXjFJNzA-PaFTGSEOmfz9TKivi64Hh8yK2SsH_4qqP9b5P7aevZJat5igMqvQeDkteeH-PT-LGnL5Z_ElebWotjzX707UwFawZLBu8MJ-_dZDnpLjVNMQyoMuZM5Y-lPHjI3_82PZJ6dwGcOt6P63ImnyA7jBmdTKB3pJHPTVPvm_2G4BOlmvAm4x7HnaGCtvrC2C-PNTUUCTuPpD3Ahhjv3QQ-Ad9wW9jmb-IBv-EOR4biL9EwpnvhAXvE-3Soq9dGwOtry4UXSZWYYXutDhSkvrkf_7hlvN63loU2CuWjrsVvHnk38OHOYf6DQiuyWInCMKN9pm-NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=LwxnxGFrKzPXjFJNzA-PaFTGSEOmfz9TKivi64Hh8yK2SsH_4qqP9b5P7aevZJat5igMqvQeDkteeH-PT-LGnL5Z_ElebWotjzX707UwFawZLBu8MJ-_dZDnpLjVNMQyoMuZM5Y-lPHjI3_82PZJ6dwGcOt6P63ImnyA7jBmdTKB3pJHPTVPvm_2G4BOlmvAm4x7HnaGCtvrC2C-PNTUUCTuPpD3Ahhjv3QQ-Ad9wW9jmb-IBv-EOR4biL9EwpnvhAXvE-3Soq9dGwOtry4UXSZWYYXutDhSkvrkf_7hlvN63loU2CuWjrsVvHnk38OHOYf6DQiuyWInCMKN9pm-NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Thkp488I5mYhApYmqBMb8MIdmbFaGwlIEgnPRw7VadSEKxiUAR-4el-x4KTR5LeJgNwSudohxCrYvImZCq6qkv39CHdfSRSjitjQ1zz9cNd7A6Wtjh2ys7tIaY0-DAhnmHgifGUd6lI5EC-F68p9FBZ0QoH11_engrTSmMJPsqiaWSn07KwiVkqTltjhEne7MfMoITnbZBCTZlo105wZ2IJGC4cSEH-4RtISXlsTZWc6vJ_n4BdQ3VmwkBAk4D7beWmJqyGTDZx7LlA8zHK-Y8IHp9450Zv8OuLy4FxLBbqegUxVMkJLWp49xkaJiuSo8RC6T11AiB-qRkGUamSqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1cX394acANflFYD0cRYdCRawGpVDP2z_n5p4jF6UzKZ_a-gc5izhAsBwcAZUbyqc7O_BFLU5OYfL2HuXSsaXz0ZrXfpoRv1S92LQTch_DEoFiqfAyiFVSDJS6dYQm3_B_8LSxTCC-E_AaWiLaoyrnnC5F4qtira4u98yQQKBlQgey8xNz4RieWbjgSePjHeJR5CTrS0hlBn-ixJaSKv_SHjlsCFCSV0XvpXenUidg4MNNyJ8OLsp8JU_S3L1FrX_vOVrY5iatPNwXv2n7CMp1EuHzwSUM6eyoMo5EHo2XEcSqOYRtKE3jZK340zPyEB-t74wOX3GJnI6jwIELlMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceF8DgmXLqLbojTMRHpjPj7_5PDauspj_7kknA-ZzvNM2jzze26EtWXjwS-G3GBfITvwK-MyQHLkbjD8dWJORkOYypnnGe3RGoxNzDuZ-AadAcbPWKsqnHKpvT7SHPuZCxXlyPKWvx40jC5YLkjAfAZPKJ3ZW8cEbAdipT58ux4dtWAbl5ImjoC-it19bwG0wSUOZZHssS9VBBML-Ch8bp4QTTEDcxE3tXXN5LADEu0EEUPeI6SC0M8vv8Kwjx7Arxy-1-XhoeV9-OZSSfdjDTHkod-lA6jHMYZy_BotWkZzkG91cE8Fqa-sghmxNaiexejlltAaTgA12hLUlnSa3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csPLNzXPHeRspTrWumq3VHPhTyFTPk39-tvVL2aSCRVlmwvEHcwUbti1Xa8FZ0anxIPALcZC1UibuF-3dggq1E_5BJVNesJSs1BLHfYKhzuaQm4UlxNkYrliUV8-Hlceo8S89yG0ogRCnhcZ0eyUH2cJvOLdw6-pH8MfT-WFHdiwU37-WURQ4sPmtPjsQvmiGfPaG4fuYuAJDa-evrCHu2Vw036nLV_zrx8wFEVi3ikWdz8g7koAmszhhwKjltLd5FYlrW5d8f4tUNCrMFd_mX64pgnaX2BvqyAkQWab5olS7xRaBZpP3Ex0HvuVXcCl3CXxW7nWe5rtmKjlQd1xvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0N8aN097t7LXKPsl1WpziIo3IVnnR4TgK4mYy8OLgYafF8X2rdjO561XIQNCwfOL9nduau2KMmxX3FUn_DjjWxJMyqs1SRwijbrSZ95YvvcFqYek6ABSbV3T09Juf83ECNitWNoAOk-SNIZKH3fzA9qPN_cIgRM__JK-OzutyvZ6RT2KT20lFjq2l0rXFrgT4fEVmvaxSOhtHMGAZSCAakeMoW5BUzWtF_O7gXXXAb53LuxwabqWCDm4iGpXm8876cgMSeFIA50NDSRCu8ngfLc6N7-8JqZHyr_ZTmBMfy8jsVe5v0qrVoKTLogwIZeknPO_2szyhfRCPux36Ck7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1N7nP8TEDc_OsezK4dXeC0YYtQwLgVclfkPsmGyelFp6_DsLVKvbiEAOT6W0Nr-beGf7AFrMWJQkzEZmTXq5c4cRiw-WAutJorVlXghh-8TEpzXHJDWnfkogCYUKGhi9qlW5F6PkqLDxw1hj5P_BtA2lOkY3EP5mdwthR8EBu3egjnZdh-n0gB0xpdsxYGymtWcX75rn4Fx5YKvPgEY-V81m6nViUEPjEmTrI9XEnGjJi57V2cu6Fdb22LGH-0m8EEJG4siVFPQ6pyoWlH_LJP6dUWHWOzdGZdKTNqEVPTKjE-bieWCuhkbesQYkZ6AO6RWIgdFnC8OGSi68wOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=uyFjJKRvWGt0O45edsdvnPoSxD2sKqKgXly5tF07IPhLO_1e09f-HXaUsJU6RqYciCs0A0fOiK0K-NneIa6IheqzZfPVkWf0MpazP1sXZ0lpb-MfxfoPZoaH9A_iuhzZBhFsg5Z0G6Ps3Vqo_SQEDAAv41iPUmaGmWpGG9-JpHBb_EsxnzvH5nY_49YWIq9BuCqb-iUSK6wB3Qrq2GMQ_RN-n8WlxAyyJKA0rTnf2qG0hMs-QPQZtEjfHzSKz7Ct3UOpUCKVOSEs0POo9OfdCleHIRSpCkQwKWq5LZXLx7byElz7ALp_mcpOKZCehPnOBSnhaNtFsL-fI2KDsx0eI4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=uyFjJKRvWGt0O45edsdvnPoSxD2sKqKgXly5tF07IPhLO_1e09f-HXaUsJU6RqYciCs0A0fOiK0K-NneIa6IheqzZfPVkWf0MpazP1sXZ0lpb-MfxfoPZoaH9A_iuhzZBhFsg5Z0G6Ps3Vqo_SQEDAAv41iPUmaGmWpGG9-JpHBb_EsxnzvH5nY_49YWIq9BuCqb-iUSK6wB3Qrq2GMQ_RN-n8WlxAyyJKA0rTnf2qG0hMs-QPQZtEjfHzSKz7Ct3UOpUCKVOSEs0POo9OfdCleHIRSpCkQwKWq5LZXLx7byElz7ALp_mcpOKZCehPnOBSnhaNtFsL-fI2KDsx0eI4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shItn9Vu4SxBTxtbFNwmHJtI4AnWjj6YhI5zOZRmGttOfxe_-jW2NPCxpM322-Qeitx2ZbgskIRdaxMB9aqE52AD8XdvSeInW5EQ9dRSm8GsaAajYn6CvtDzW2eUZsWs6SRlr_gXt5wQgIGmsMGj2_1rGlYc_mbAFTQBbgxMOahUKTxMwVwCdpaBS2Un6ZMlOEizihV92CiqejnQnBELBE_LnepDkqBUNggYhkjtziYxfhmd2IetN9a6wVBrt9FmOxKXyapjdFAmxOm5u9TJ6i_BSfUjyDNIHK4X_W1hYRxutmfUTb_iy0hzNmCr5W5uvGf8cKTgOO6f54psL5vtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuaO5azUhCWWEJNsHPwJXUiqXK2DJjFbJN-dOjRARrqYYjQHOXZ0deEJFJLIgXb5U67hUuGy3PqBPkkE3RAOfUZaZI_e0Hppph5sLwy2Jl-thbjO6OjXTCNtXexZWyBv7Ai1LToKrr-437dTn7XUVrpMdxTRcyqCm7ByDC7FEjd1I9cJZwHtxcTHB8FN0bi-GwFOyvr7eIl2BZ9haPYlgLvBs2pwdaN_ULewVRhtEJOldivhFprFWtwX1KOl9TJiY5XblZOiW9KKeoeD9NFJxvOWmvyHwJNvEunoJNlbzdPeHtu8El4ZBiWPJIBlmL8LDc1IqvqGbLb2aZMws5Ue1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShYRotcilFs-aN0qXzTzp8kMGjOoSUxyxaSTur0IoGUauM6QahAqaTLOQ-UZtIDoq993VjR5k1DXtBMHAOk0GSWRBgUJNdzRK6D4rI6GglSt966DTBM9GeZDnKnB3aO9hlfqS9THE7FrU_B9eMpqqBpaJc_qEVvzFYqphWsofvm2H9YAsn50Cfv9cAeIjDdHioqXwUxfSONbzs3dH28R1FKSABrOpD65Y1e_-twMCewVKgy0XgwDq6jZIrorIgEi-bBvMU8qVbXUAOHy5deuqkqujBSWVruTXTqmyNuFS3Ny5VdQMI6JLPhXC6vqPmOxwZVGaEkAq5TI85apf7gMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM4GEXf_4Rm_CX3g4MtRsUwfmWZSyCncHWeCN8i46mxhTQrqXVzR8yGZIExq0L6eV4YxY2TSougxfagexsVYPFhgorLby_iG9D05Rh-1wA71tHxvZAOAPb8Aj71-MsKxErimxPgQUEDvqr2EsvBme3IfAxMM91lPdF3e-iQE3dJCOMbn3r-f8MObkWQXqpN5B9OGugEltlwhXfIMVCFyGOs9T3ET87rECNCjjr4HP_hn7Nzbo3tb6YoyLF3pnIMmjmX-wEu1HsGRByCzXAg02eFfFZaZ-E1uowqdX80EfQgP7-U2g7OlsoH_h8M6ykUzVt1QLW8u1UooeGtOFG5XGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDUHLBJ3Wm5A3-EKxq4fYPyv1vtVV54HYHG2NkMFq2mhUXQb4B5NdRkjZtisx4Cgs4oVxBwlYVUmE1J5kT7AEJNz4RBtK6ssx2FMVazC3SCz_R_bEOdjY31tB_OthqLVXkmvqxvSsdR2OQ7kEJDjggCpSUHqO_-DiurIonrx9h10yUiFYrJDATNtXd7iA6_PFJEBPzBCTs4rYihPd3IRl3HZvhLckW8rD7k0A_OpH3s5oHdd2W_onB8BX6BBnjXpx_vCNlgh05PJbn4oNgSaAZraCW4yfTdDeVMQgj7blSscydXYr3Pdz7FXHq2_w5KDJt-81vKtca_DAVZD-nnsSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il1z6YHG-7HAyq-PTnHTyGuEjf1OBr4q4xcDQ6PYBLI9AqppAnPtVwJxP6pKS9Qtdxk53h1D7XRCRHnA7Qokf8xfF2lGWEFKNqBeyWuN4pfUqtBAZftaJ4uDHrXqpX5X4CSBeD2Pq6agBDLSdthQIcDCmOCwCEOQEzpDX18P9qGNW03GSy8sn6OiruW54c1fVLf7Apd5W-62thv8T-X4aMMLrIHbQfe9LMLDFbZJ_osGr4vpcSFIKralQy3Hf2bbXJwRoMAv-eOflmI_1DyJE7vs5FXEHXIlfVb8uzAgxlY_ReG7bYZsUQiYwJTwqgRs90CmcszSDcwazn0nDA-IpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtHNVb_3MsSnxs9AHgO5G2q-BInCzOZmr5mybmENYXcOnA1Uk1XBJCQKTKqJsSJ3Xu2Qk_nwzLGSScAYEdp8JQ-YqpBN6nZkZihj_WWRMepAF_25MQDQ34rNoaBjEYApLl9Wa2Y_3UIHehbfrpcDl_LYI3rSak6xGfm4u-uLulIjmbhek6vGrjqCIxoNofFFf305agaVZittOpxPHCEz3lqVv7QX5kHIh1yPDjkq0Ox3JDc59SDFQDSFbfLtHe80ZJ1Js7Lad0jnu9XBypYHDjxHXyK2W7xxEbbvSDY_ZtcVOfFxATJO_oU-cOo2Ri4Z8HnNyprGuIewtbIyPu7LVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYlQWP_9cvD-VxACtSWLDrIRb3Yy4jFg57uxPAQtyo7Aa3gyyq-UhOxx9w8xk4YMyJCdslgOSWpaiNqgdStk06JT0IWuyFknCUDeAygiQ9jDHVVHRJXnasXXcPs2zgofQs2-n06RZ1S5wowxejuFDdlEadsQcWcImuSEJRojqwsg0jdKRbfDZVnARDZwzoYn7jTxCIBVNzLS7HcuKw1QNkLCkVE5Dq6NvEVhmcI1G9NxGezXchsh7qMnwhPJy36knm-wUqtshu3ZwXuvs3lKMaVKh2Z5kHnGehSy2185lLLuuvRPB22qhb52yWT1cqfh3VYkM8Via2XCT-stq9wkWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKNWGBg7UI7HG8R9C-hT-gFQt2tvUOC3tTMCtz0Yu9JHo2L2VnjZg77HLOEKTf32lhbmeWSx4-V068mTTiWCq2T9nMNu5ReX3ixxr7V3yYnzMcuStXknOjcMt_di_yz98_7ncU60QMx1cOKDBaGRJ9SH6qA2bBxpX6CtU4EHzrMI695ZoUPdtelXBo1f3bmQEbzqknJSJqA4qHPMPsYbPBTjwm2FssKIpMuY72m02Ja991LGcWjOYVQa5dceUMcwEzmfcAXWCl6OJnGxxDelswpUSRZOT-8yJ9vOfuwsgRWrZW7kxYG1eMlY4MY65xO7TCdeBPJr-uVdIZwHMu1vpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6ITSslEnxuAtKrqOThRzuBCgFDyfmQixk3g03AgTqfY-0DdTyrB4PSUqbC1z63_2qwoWnajzE_u3n8SZeGkZzEKABlf_XN3UEhgRBOUcZ3q1YqNZZuQbb052CfEA5UVG4GYNWWhvce85n0qIQhk7zm2ri8rYyXRxlKABtNgD_konWFhJYCLgcRRgaN02k1XhDkmxh21E8u5QID-8Rnx75791wyqHdumQPvG4nwtOLF5SmOrmUcl9FMgv5uLk3EQLKs8r0xT30sDQP6BAAkOCIv9N4nv2JgjM7V_YmTpBgvNMGSXM3rswq0lRtIg9Ji2Vk22_YhjkcaN11ehUQccUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRPtzNBY00m47hOXw4rQyMoga5H9VGPDKOavTUZh1CVCBMtZkThUtA8DEsPRBrlyIqqLCGat4EJYU0ywokMlomkRhHrzyPkynY1BolkePj74pBL6kD5l4kZEZxRTC64zxeuJ9Ud6g39JrbZPQ5ZhaUSVOZJc8SJos0XIcG_gt0gVgXYZvaJkyLZTE5BRRNKB3YRT9gHZSGJzBx7IQUnfCURFvEcpO2IP1qpcWQTFyw9SqFVPZJyqVEoUbAaNziOWDwyZlhmVwBNck6HkOOd-eT-AyQhJYNbozETDvZHeoGTScvL-fbhAlo3u1hbMdIYY8ZEYix8SiBiaX1z_hC5iAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfdEh0mqBJ0EPcVFE0lq26ZSwpDKt5RaSqjJcwKQti1gEZPmhXcwxt2O3Z9q3qhahxglXiQ27mSFFoNLSlmC9_SNY4MW3S2LVrJ9nfWcLptVXJTONvXSpnwgPuGuy-CkEAB_aO44ENTbH5eRDc6ufHcXy1A-b2b146O-IpNyHYjfppTu-lFcoLOjc3lq1QsMPyxB0jerl2DAEC3Aa2S7X07EjifjSJ2ei8oXiTyPamAdMS7gFWY6jyy9TMwMh5bKpyR2sxIg-QJGEEOyzgheSx_UWXuskdpEoqjkjyNyL8mhoGgHrt2Q0auNkewoTQVa9mDVIPeyOfYm0dQOG2tlQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kALNPs5CECnbx8bq-FsuhDjDfKC1mufJllcF8VkieSrixUc2aqkWWE_yH7pihMh43x-l556QAYPmXJTM-c0qWd2oy_dqnpuKodaHiSCWGGcVYs3h5UL8KJ_MqEOeCqBXqap4kY4R1NBlBwHVxzR3SLpQc_AZWjpP6ebBW0b5kFcBq8FQ1q7HpRG3VZuOzebZMhsU9TOSqVlA6utvU5mSacJaAfcAErR3p7Qn3InYPbJvk4gPdhDLvnIh06vu_M4XK-rAzOaovmJ3avsSU-6LKEVQ2usfTTh4NfCXpdZDtp7VzCuAC7r4TEIcKPaSCRk4G5XQqpZjLXRQmql2Jpezng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgeCJGUPGZ0B3tZUpsgYJQzZGVjwwll5bBZJ8CA9ODRnZy-DgR8Ss7BvU3uHF-CGtAZGw59UdObCAjeeJCXj6_iy3GhH9c7ZB58dr9ktTUdKp0hFDIVZU-4juZ4M7754w0ye46kIZDzNVjsFpfzXbF8ACxUdncW3nbNJokxmR5CRqrYkF-Pz_qy7ivAcM4TUKQRZSeOcWJT1QukwfSsSf-quN2kHRc71vgFHNt5DiFlQA2sWeLXr4rh2-B4_sag3s2AON3JkquFugkNmqfha3qJQYAnMLMP-DBtCzk70xJaKWjuZC_HjW_-tMf2osML5N2O7kgDBMa3f9ICy5ZWVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UihneyqmcSwDpjToTckLphdC2XFnT3mb77bOB2q3DiOaa3VNl-N8QpGCxGDyPmPI0rhh_ztKUXBBxo_OaxlenOpHmqQnDkBiW8jjAGfiG3Ny7lQCVc3TaiwLoZqW5pg9SHiqLHjwRkvPPoHQRnpkmKvFAM9vcRUwG4llIzHtqVJV06nv_uInnhaIIqVr__jZBzAijF5E9vEjpUVgwyMPLNFSmDHpzjo-Cw5AJ8YMGllz-Aag7Ih6lOL_H18kmrbKo-axnwDQyDKLqx8LauXOpDmtXHfuANVEhQEJeJV1rm0oMPDRwTiFb2fH5YqG5473sp0n90hRdjn3_fSVIRTa_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8lfZTacY4EtB1sAs7sw52L_0D-KZ-_4hcXnXg5BKqGE4QsO9hJNoxfz0aOWJjwfxGRfYfKfxnOL1huXp3Gez_M3qAAWoXalb9ftia1Glp6Ep2ZTWKrFIH07veQ8hcWrVbolTvde7rOsB5AIj6noLKazqlw6pBAXhhmheumhC1Z-2kYc4lIVynVr-CsryToEkmZnO8KBVFno3nIKaiczaRibGu8q3V5E4mshrK83G98Y69DhGTBCs7Mi4Q5T3AmM360mHKxsFW_l9ZIk852Z8UgjFUFrq6A_iqmB-onQa4LLDTHZ8DJZoOz2Yx_Bqm13hTo3p_Jhi7VGYQLWct7LNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjinQ7VcdV1X2qiRBZISUSQpR78qsV5w3soIF3a9ITDHMep628FXumhWnxyvpyaYpsahhnp5Vb7BG0ci0-DlkSnV0qK0-PHAP31X0ML5puvG6H_FXVwrZZza-pJhehIFnrjtB6rEfYZY8_Orql28PVh4IWFV3-vWV54Ws8X2AopyvnFs_lWLuL4oh-5IdAo8qNd372LQ-wAbg5nlbB67cBTl04c6jRKKYcqRa_dp5DivOwUpZ9zFKoLDmsulS5iiG5hdNW_BDnAWaJZDs7q0xcRXuoG1RVUfqZSFQ4-rIXOF7OjbUZXqKJm_UXzi6zm_261WbYlsQr62pPzTvn4xAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=GbFWdVsxQfOSsZahu6ak-YN8MfFvEGv9xfs_LcGjd-VaqFWQimZJnzzfzpBT3-fq4SOrNQzDwnLo16Cl860TmOPzkCmLJQ39Iwdaj_GfMh6Mz5Vy8fwXFO7mZVN3OZZLhmq5bnetG9QzRZ8HTX2I3_FkHrVxdJmb1AoqbUyuekBH6EhR018ctCq-vz0i0bkRuUvjOuq3ZypOnK6y8i2kEYL-4lTmAeIqni5TzcES42Ujs8kjA9toZZaLuJLc_SgMVObVBPx22MjJRyBcs4vbXz3Frs8HLf954N1vhGs4E-RLH--Gj0A_JWRX8xHKXi3PAM1tPCoIWNlhYDFoZin8hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=GbFWdVsxQfOSsZahu6ak-YN8MfFvEGv9xfs_LcGjd-VaqFWQimZJnzzfzpBT3-fq4SOrNQzDwnLo16Cl860TmOPzkCmLJQ39Iwdaj_GfMh6Mz5Vy8fwXFO7mZVN3OZZLhmq5bnetG9QzRZ8HTX2I3_FkHrVxdJmb1AoqbUyuekBH6EhR018ctCq-vz0i0bkRuUvjOuq3ZypOnK6y8i2kEYL-4lTmAeIqni5TzcES42Ujs8kjA9toZZaLuJLc_SgMVObVBPx22MjJRyBcs4vbXz3Frs8HLf954N1vhGs4E-RLH--Gj0A_JWRX8xHKXi3PAM1tPCoIWNlhYDFoZin8hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLCBPiq9eLciXjhfBemxgJtzpl3pOjO2PaHIe4Y1XquMUpEVnsSrjcV2s2fKQzXbtzqolJ4AFYqMqs7JIjGjdXw3aQYWaBQH0xfQkVSOZTOLRuO0PIw72aK4sJ9k9bOWmsq9cmv8RN8qs1B1NakMowQ35N33qJRJ4xNRWuplczoV2ZTapBugchFKnwgkjwdHDpjYK0_Cx44LDzGSE1Rezh0hBFx0HGUQjQi0c-0MDQXYeP6wC392xa2cR9HvvjmjB65N8cOm4_6Zmof0kFfJz7AHWE75gg_8dPKK3XDcLw69t_Ud-D84sNS_f-UdPrIiMCBPMWMasChbgKGC7bKrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc1TZ0LCKAe80KPpWsxCJEXWPKDUpqhuZFHR6XSsIaDCEy06fllFhIFh8iLWgoH7fEK3BfRiaXKEfj_tREpWMCzqRAaAbMQoZ4cv7H-QvU3MIImD4KRnbGycC6q6ZCogwlrfDkwfMJOMB9BScgMYko5AZe_h5NrvjcMxhlzD07zvuyjKUKSqZ-lpt_5NlBBlROlz-uj6QMLFjfQ0BWjC9PtMpP9VH3NJOKFCJx8XrK1SkklAT-18tKMeSi0jUmDoiaQU9Lq8HYQ7ZUsPQh9TBjwdYOExWoUhh6XAW42nzwOCE6bxs6yM8YJFN3Zjw2uMTKuMpmTeZHg26AIL08wMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvg4tddqyzOPgPRzLQfK1Cry-GXPkwXVj9PSR0L9KjVrXpYXaIFRbPff07ODrSEB72X3fwM4uoj5zSwHBt7Tkgg-BV311JRVFrJd9KJHsD40RcrP-f5wqr6uS_tLBC3Uu6KkL6PyJ7K5OlZc_-TqqP3GQaOzZH_IzmnewZjqQrjV1igNqwPUikBfxSUVRmNldbR3EJMdGutxACNPdXevNdnjrm4Dw4gcH6zBsiLXfmxEiXVL71xJnz4YmufhUPXcbBcE5j3bpNDYoxGpfktH-9KXM2b8cZuNqAwP-0Q2MHkCpXA8pTJDFiYq-KlRv59oLBHzFm9uI3UPoPKoim2ZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=eHDwsreYU6ST8Uf4zg2zPBRnjkcVwB6WPxiJF8A6PQyRP-zrAETbiqO2RY94ex9EJ51j4tooxsgVDakl7pcy6rDdPeBFeV-dtm-pf9HAtsduVT64p-oZhsVYLYcLeQppP9oWvNVw0wr7kuUQwukeSka2RSfO_3vqgFbPnkBFNqWgAZ-HtmjuUz3ifDFzrQI9lvOCxxmhhWk6790xhZoKtnAQWqwGYZkP_Bwc6u9EHuphOw8gz6c_rs8KYs7hfXjcA-ujYnHlGacNdeNEjF5Vpk-xlH51AQqY0xcjGFUrDsFDq_CeEsnmUoCB6C2ktjz8HWNbI-dH9PMBmrNGhDep5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=eHDwsreYU6ST8Uf4zg2zPBRnjkcVwB6WPxiJF8A6PQyRP-zrAETbiqO2RY94ex9EJ51j4tooxsgVDakl7pcy6rDdPeBFeV-dtm-pf9HAtsduVT64p-oZhsVYLYcLeQppP9oWvNVw0wr7kuUQwukeSka2RSfO_3vqgFbPnkBFNqWgAZ-HtmjuUz3ifDFzrQI9lvOCxxmhhWk6790xhZoKtnAQWqwGYZkP_Bwc6u9EHuphOw8gz6c_rs8KYs7hfXjcA-ujYnHlGacNdeNEjF5Vpk-xlH51AQqY0xcjGFUrDsFDq_CeEsnmUoCB6C2ktjz8HWNbI-dH9PMBmrNGhDep5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGvUAYU1OUm8jBKGaFy_qIPMpHJ_SX26dzjcv8MRE9OhPvQpubw9zJ53jGLBJcY17Ee43IXzw4HI5XV7Qd41b6PVm6WiTBMfQAdtWgT-NhEO7oIuvJ6-HPbn45o1Zwk4AdzVX-GnbTN3xNfu9NRYgJP8DCyRYuUKWVHvnGkLjJLZlhSAXOSg41MOP5WBR3SEWT0_pC53ZAYJ3_b873G8ZQ-xE2go-ioIQLRNoTIg5M1zl_nE7NHseaD6O9ULeiexG1l1UqLZxo0z4v3ElCcO27YX8dyMUkelFSK5rOJoS3Yyxe1ht8F78ayyT67otTNuQ_VK3HML8JqtB6HnUZpZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=eTJZOkbhPv1b4UV_yp_ZLckr_0VWIQWhlECIAtz7dmvmQGxx1h1vALqp5O1ewnwfsDzreO04il-7CXP7K6r0f19lBwUNF5DaD57RMO_R7Qb2eGwjTb4lB02Q8Mr5GRJZP-pSpMq4VbW4bry8YRl2nh4UeIjE3kU6vEDsR70PQqeNWWVCXi0KbRD585RZ3OZHyObwVHCoqro29GQrCj8PklaJaxUijCOkGgU_cyrwx7eOqylRKTNHdP4xOAJkGBHnK28hzENpwIffQ8CdTORcs-9w1wr6pRXXZmullIEGlDDxWc2wkgWjB270jc-xmota0jvI-LU6QiB1bCdfhqTubg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=eTJZOkbhPv1b4UV_yp_ZLckr_0VWIQWhlECIAtz7dmvmQGxx1h1vALqp5O1ewnwfsDzreO04il-7CXP7K6r0f19lBwUNF5DaD57RMO_R7Qb2eGwjTb4lB02Q8Mr5GRJZP-pSpMq4VbW4bry8YRl2nh4UeIjE3kU6vEDsR70PQqeNWWVCXi0KbRD585RZ3OZHyObwVHCoqro29GQrCj8PklaJaxUijCOkGgU_cyrwx7eOqylRKTNHdP4xOAJkGBHnK28hzENpwIffQ8CdTORcs-9w1wr6pRXXZmullIEGlDDxWc2wkgWjB270jc-xmota0jvI-LU6QiB1bCdfhqTubg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqDUTIKLenogWqNEpCtTMo2nF65ZcGBC7MPL7M9o7JjrR9QsDXoxiOqKrqMfJ14yDls1NOjkMQDKYtSDriG4ZQz4G3zzzhEi1EnzwZwdaj7bFUOLe1aTtbu_EuuTcyNADDQnQ9P9HQpADfASO_JTHt288wztcIuzlWAm7GULczKFZ4fJf1KEzSKzjL8kHM7fz_zcUMzN5Lkp7-duWHUNfU5AsiwMjg8WZhZLpFl5L69koG7el_B-U8JAZa_F4yTl7FrGsr1Ap4491zW99IlkNqftEdqBBOypXHW3SyF4zFCZqG1kfyBnXA9tZad88ONtxEkqt5lW8MTSWLYImEKjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwuimBMgAKW9yWpC_D4uLGG3GCl4FKw6UitMZ2C96XGTYxlLkB5H1B4nF5KKoVf96feDisQIIYGg9TqQP2dpItPdIetqXk7ezfcQOVdJ0p2rfwgZG-aYRSrJdf0TNyzEw-RaKE2sZRZZce8aLv-7otcMevjJC1qIJI2GJVq1KRJw2lznKs5OwhIu6RfTWDB2gSJpJLVcO180GWofNrTVRqrfe4onwFJwvua3Rcv7rZyKlRX-42XR86Hj1adTIown79qzcDCygP8qNepOel0_8N7chLMXko1dr6ye4ATpmZiZFHQEh_Bwjgi65OUlp0QG1peU2D5f55E7hLEr0ki05A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXTUcc-f-spn8zl4fG48pbGxsEufvRn1FlgpfBbl3Z4tMMLLoj9o8JspYx-dt4JIfnTxkf78_2yL0_GlASg6GbMtftEbBcXiLLWTBKGrW8poMON8m-24M72Jv7Ew1ImopOGJqETzQVQqRs5ar4NSXEwPj5cQrlgX_4eBJFmdJSS5GAMs6-0ax7hP39KAlilBsxOG5f8tNxY_esTSz7BeRIJmaXuVDjHkLWiE6hNl2259Z4JA9icGyXRZemiit0XVr687sCnyjiHC-AkB5lHjZRApBjUL8oQLxF1Yw6r0rhjKhLYwvjEO7vYo9WsBJHrKKIpQcQi_QqueubUr1Q623A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq_saONm2N69ZiC2xFBydBx8e9vcbHtzjOjib9npvLTbk2Uoz2-cLslr6I--RMhrNpaa88s1j8hccbbF5Rq3RWkoD59YJ00bhIINO_lQRsFSNsAoR57Gl9I3S6EBk0_94-VHx-ldaZ0-LFLDV6xVgTt-3JBSpeYuuwPIRsIkc4ACkRxX4vXvpn6bNQQWbRzgs9meliQEDKBxVkm7vZS5y1IuXaxOSrl8Xpk6zt8MzJ1zoHT0qYRW2v6fwgru49iFUq7SilQqn_vVvMjYE2djsNZkb45IY8u5J-jltUDMs0lFc__P3jEJ7pV5L_3pfOHRJRlJTiixpfJ9gSOPUp_GCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOAkayE7V-4m-l9Hs_nMiv4_aWp6VoV7kKe76ghHvUr2JZn3qRxaiorIX_VYTJAUU0_L3AW_zKFZqES9XLBDLA0YUlzZB4aZR_USJ7Nxglduk5lO-cp7TSJcAk4EHcO5S3pLRIHiOJEYijDMR6up7CtG0xMIUvISbL_Pg7NKYI6j46QlBoQP2qtaRV3YWjqXzvz3ed40vwc7rJs8b50bKEKCWV3glrn53V9SV9B6djpgT0cdz1FLg25K_KNwKgiOaoEobl7VNNjHrwb7jC8L4TRDbK69S1EeUmYP1wuknGITiue3bEihlvFC7weCoPY_Aycu1DgDjGytaxDCBf_TdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRTn3DaPmqyyj3fCkp0o_DC8_kuKGbut6KHNJ-YU6p5j7xwJNYQEiZ3qjYfrIF8bf4eiiMju733Z3ENqG19lrEOgLp3ulnH8TZwwir9Zl5clpJmAifOLTtR27ASzVimAFT_Vc-qn1GrPQ4OpZgntzDjZ5iY1xYkS_XQntvZWXprzu7NgrB81_jv3js4CaRKE5M3xFZZ5nwK6Qj1i-aO4KmKVWou0n59p4pr6YX57RQ4o9VwmyFQuSVC9sl-btbVYFXnKhhiR6jZ3StnXoNPBJJrQae8BEIsBtdMkBshJ6Y7SSZZukK6mu66g9XmSP0W5or-VnY3lEqLLn1HhPZBVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy4KtghbOKa8jWw6IFJMZIRHvtv2FuwOdl8P99vywMRA-qUnDfq70DK1q2Rvn0jrlgllwS3Xt5XkI9nl-6ggbbSdgDPJNh_aKz55Q1hR3sWKiyBE4iUMKL9Aot2Owp8pEx__6Y9Yjh4tiC3THQfZrGA9l2u8SFiohVetkzQA-JshsSZUyjXhSp0BYzdsVgdkxEspn8SAXAcEj1roWKOatKNAwZyXEcCMMZAjQIpQs2IJBqLzU2nUTFEuo4iVY_wknMCbKYZVRt8_hLYjZx9xc8nY2UOSBosVKEGE-NY_N8qB9smMZG-tuFnncLGHj_2qXtr66knvwsKk3C6h8_d6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4yFvhPv7LILLAYy1oa3oTv-SqY_NEq5bRAeKhYnMaZTYziidJRU29Z-8A-L6D33E3s5YjKChdD1LM7OIwMo6ARbiu9i64f-l6EZqMQ8rI-wTnC3Z1IKn0RPqypJcWudisMCReAipg1pMPrLiBBjzgADUx1uQ9JuptyrBbwXZf-KmKaxibYnZU0jLlmeji_K-_Uka59OwtOagdJOZWZHj92C9xyH_tNIqvZKEhs2vf48Yq19Sg9uiGJeI4OtVtUzQevjDbMAW3i18-72wSqZ6I6u11pSiZ3kMndCUZlGsy1uy306IytXRdsoV11DpUl2yQk55vTNMC3cEBiScVAciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=lWyRNH4sstNMRul_ePaWfxCTlPaR360hfUkX-jXcm-Pf626AAzfwvk2xqx7UZ4uJAqkJnVRszVLgD1ZuNgbl0lIvCeK_ZT9-d8dnVWIDLBNuxKFmnNGSaSc60SG1VfVoXwMQcu1cuv8stC0LIur6GMUNCMhfrMEsH8767wt9CdmPNI3PT-6ir1-xnRp0v2KrNWAm3-4GY2uQ00mhO3h1nkd0oORTJXiTRZZvqXpFsbF-ALRBChyPNl2U_AfAeOGaGZhMYJXEecxr7V--Q9BQGsLmwCrmb4skt6ml_0IO4lrVuBBYjQvkJjKhHlKD4TiPcVZzi4SusHcj1oHGsityW3uEQPYvzGmxJl70gH8E25WZPhfUWGaGeUPXha97myV-K8CefJR1yBcwFKKYW5EiG0rzcRpf8N8Gt8de5SU-yZZuGlmBynrsxLEAMEgNxFPeFZiS-_VtFUek0mtzefC6_v9atf7fPzZUU1nTHCuE9HCvRfFR3Bkl6F8QQiuTj7VgSv7fVhzWhJ_ypJBMj1nWcc8NpxTm6gQc_NbSkDiRQPTuE0lhVB8bFy_tJt038_vTOhmiX7vy5bhkADXl7XFMcipr56DnXc6UOr_vfJ3nGnzWIQi55Hf-nzJb2e2keaT3IRKyOGWz2FyTjLb58Bpat5OIpNIm8n8Kye_lpvhGm2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=lWyRNH4sstNMRul_ePaWfxCTlPaR360hfUkX-jXcm-Pf626AAzfwvk2xqx7UZ4uJAqkJnVRszVLgD1ZuNgbl0lIvCeK_ZT9-d8dnVWIDLBNuxKFmnNGSaSc60SG1VfVoXwMQcu1cuv8stC0LIur6GMUNCMhfrMEsH8767wt9CdmPNI3PT-6ir1-xnRp0v2KrNWAm3-4GY2uQ00mhO3h1nkd0oORTJXiTRZZvqXpFsbF-ALRBChyPNl2U_AfAeOGaGZhMYJXEecxr7V--Q9BQGsLmwCrmb4skt6ml_0IO4lrVuBBYjQvkJjKhHlKD4TiPcVZzi4SusHcj1oHGsityW3uEQPYvzGmxJl70gH8E25WZPhfUWGaGeUPXha97myV-K8CefJR1yBcwFKKYW5EiG0rzcRpf8N8Gt8de5SU-yZZuGlmBynrsxLEAMEgNxFPeFZiS-_VtFUek0mtzefC6_v9atf7fPzZUU1nTHCuE9HCvRfFR3Bkl6F8QQiuTj7VgSv7fVhzWhJ_ypJBMj1nWcc8NpxTm6gQc_NbSkDiRQPTuE0lhVB8bFy_tJt038_vTOhmiX7vy5bhkADXl7XFMcipr56DnXc6UOr_vfJ3nGnzWIQi55Hf-nzJb2e2keaT3IRKyOGWz2FyTjLb58Bpat5OIpNIm8n8Kye_lpvhGm2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j79VTxPG9XXh6yRPP1m70PgNS8_LTeRmJBkxpIPHj-ivkDrriGd2UcI0l2Xd6YY7tcEEyet6XYMfPVKubkpNVMiuBxn2NKJ64ao3kW-_6yYiic0sGMCnoB-G_qeqxl-LRIxM6iQ-_fmniQ8ZzKnveqZKxU8upHZItHTkh6kFvlp-zaH2f1h6r2MxGkOsyIllYCCf8LibwF39hz7XicJSh6BibVcE39K769yRx313nTHt7LeV3mubnJ9waSHmVAWzK-e2mH5oNKmI79fxiC_lDFGUs2DXbyFq-kwHfkyHaJLc9432_TMpzzpas3TrUEbSXWmjrRG-7-_8eKlGSX9xmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdTrK6NnU0k92lWwsHjxp6LbGlf58u3_vmHYLmXKpFabMo0RL4j7WgRrE-0OP1TULdY6OyitCpJCBswcsGJVl4mo0zmjFPFxDV2Zx-QDn5zSvq_lj-V-LY1EwmKKBMAJyO5kWRKxA8MamOqK5d_B7hbcbbPA5uYVy5c_YfMdC-hKcRrvXpLpJS_5wSzeO70JttZtp9VWUIJP4mkYwNDiCbT-Q1K4diIarqNbxrEQXK3ukK1jyrSU-N2me3guqdf9bFAY4wO2QctemXHVZ1pRwGAsLjlZqAb8bAF-ZOhWhxLbUoPnHVPtJ-zNn83zUizQT7MGJ-L8otjRNsJd5u8Mvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9ysrDDqDcKuB9oJrxyMMfyEhjEwLsKFLzjQMGFW447aNHc83iDTmitx4832nocs-MphruFBcjP5f6HLRqEpkTD56y1W0wZvuCGKukLjPaL-68mHh9ZfJU0YoFtq1wPbWvvNwLaZ718nbLEMBpBmrhwwamuO9Ij5KBDB1T2D-E9yZXiakXvWX88YMWp2KRJQ4F5JY9LNgADkKv8fiiSnuJAXVUEk-WkDW1_BdvSZ_qgRb211X7lJYTYT4i9WvN6uVlU-zS_vTWFxXV79pqeV2WSo4AAcMCBK6ogyYSHqwadB4ypTuyr9lrUueUpXAhJNrRRy2LNr9IX_vULnavnIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4yzVoKXOPds_T33m3RfMYgh1aWOim09lr-A_LkRy9u4fE6vHy_XWo3mDWQaQnjQ83eN74qD2JfKATPwjT__0RP1hzgbMlJhKlBPicXxnbdbY59ohlw4F7HrFw4BBzcYa2Iaj7D0-a0XQ8RZfQpDbAXk4EltZnDlQFUmBr-5qNFYMug1hNXqWf71A_qq7Xob78F5jzaWl42qtCHiiz6RJ0qg07kQCaxlhTUYn8FOEA8irHzHxOWnoAzwIM98o6PwAggoxy9tPkRjFChQwQZyQrKBrjnnudjRxkL5w6I4ctT6vl7wzg9t4Mx0z8oRELAhaD6AXWD8riGNIa7R5loUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8LwxVI_ji4h8zmxYwKF0LYVEfCZaHO2GMkm2t_1-DMu-ly9szRWp1VdF3L7G0wFlzkqiPeIBpLYgs4s_9wnSKgeHhdXbImjkRIIdSuqOCVCX3hQvTqNZBWZV8N2ZpF5b4jCLZPcUTbQQTZnYv5N-KgIHRshN0ZtPDTYHQYrfKBHMqj-1qF1Z52B_X03B50D0a-s4zEnaq3q06AScxwRHDeJSex4qi06HQ_Sc5icgq4HnHbKL4wwuv3_J-S4Wl8DyAvu8Ek5YArcr7q0xFhA8fehOr5X7T5ehp_HcoQwiCMR6atajd_6EXe2nXlf9yhvIGGcC7rNEs1eZ3glt0ufXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sd6aegNEhoxv-6VLi9CnBR6cjo4rxUR-a93CA7QdPRaGw_D_4HJdGLrG_vnfisx6sEDCGqsEYvXMSXdzWL1xCovjkLw-xGL4xuvDpt7XHqIC5OIbky_UQYm4vS6bxh3rWfy8yFNLDtYeHKQzOdvGDy-8gQLyeqCcqq5ulJQPP9b4M0LAeZyu_vp69xDTs1q1I5wS48p_KlCdtgaZf77eM3zozRjHx_k7rbFGvs03B-9nP0jBoGLhFn67moCRI2cVCdybivFfANo4gMYr27hVfGiN_MjVe35FsraCvLhLys9zt3zwjdxNidGCompuHZPifdYBn5WPV689RWI0_b9foQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=mqwXpEBEqsWyXrjjlWIYgY--xpUHQoh3jXtGpWWfhjMiRoVBqi0tWu6CeTHoYlS-Mq57c6lUx9esmcAPxFA1WAEykJWS-m1smDN46MbxwfxKO3x0OzaeXPCON-h4LO0vopGgjtE5aA6tBU6aRTlGcf_LAUdyKmMUB4okkI35xHuo8d9rDJVQXCcytCavb-RA03ouw8RrHFTBJnPx_OF1p6-GeEyhgymiNPEdVQQuZi0Xpnf63E2zKFnFuBN8CGeR17Jf5Hrn8OiTrYFzboC8yjGroTn5M88DvNsM8PUm9HZPXffLmEorBLkcF7wnec1Z7VeH-4TlEq5qz0oddPHNcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=mqwXpEBEqsWyXrjjlWIYgY--xpUHQoh3jXtGpWWfhjMiRoVBqi0tWu6CeTHoYlS-Mq57c6lUx9esmcAPxFA1WAEykJWS-m1smDN46MbxwfxKO3x0OzaeXPCON-h4LO0vopGgjtE5aA6tBU6aRTlGcf_LAUdyKmMUB4okkI35xHuo8d9rDJVQXCcytCavb-RA03ouw8RrHFTBJnPx_OF1p6-GeEyhgymiNPEdVQQuZi0Xpnf63E2zKFnFuBN8CGeR17Jf5Hrn8OiTrYFzboC8yjGroTn5M88DvNsM8PUm9HZPXffLmEorBLkcF7wnec1Z7VeH-4TlEq5qz0oddPHNcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuhZtShncYnclt7izurgfiboonUR44RDXUK0FOb61xusw8iTrugUaf6ooKXeCBiHfBISVaeKg2nwpyLs0KSLPYpY8euz8c-TBUJ14_JGTezIX0OeNU9tKOh4DPhf6FF3cwsTWHVkIOX4GpW0LhVyhbE7zmr8rm665CRS5FL2JcubrE-_B4BfiVkJPT0fmkmigrLzXdTBML_X1b69oVH997dLxaPKCzDMuabdaHOsw1NmUwVapT4egLVH0klf1zJ0DdlhqC2hb8nzYKnkUqaOluNBWIkgrcwcV6BJe7euc5Q5mrVMH1YkFbNBoAWatfNthzkXhsWMUx6M9v8ar-JdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwwd0OWkv4EfBOYzXt9XTQCTlGncHNFRJnF1CJt44FRZOR3CtMV9Y-McwAXUsKYFn0YhQaBOBGpo1IwE_h4P4ifDJbj4C5OeuLJYzSWPc4KP1ZyxlX8K6UOBWIYoPQc00NylGO8HqC1GZFZesEgOAjzJrsSMCeVHCZ3j6TxRV9fy__rVzCYqcSPNk3uYiqKR8Vzkr5vdmPsskgWTAJFzpvAmvehXbnoGi8j_YP3ik17BTWg7YuG5etpM1W89IL6PsLZag7z5mPaONMULHMUlaTfqtU0GuwvD8NahaYTQ678KwTRQtMOYKEzFItJYe32Thqb0nUDMZTm3DcYnp689Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPr98YoWlMQmn4OFZ2hggA9aIIfZd4sx87jOS4U7c-dg1qfkafbXHas2uj8aRYp2JLTKCN8I8IbZYASjw6n7UgLpik7CQLFfihh0F-8WxW_YZtxA2z6GAoe06W5RFGaPDJoDZqsf-S4LImv2l5UCh7kXstj9XLUi14g4AIi861r3YQm3lFt9p9iUf799Bz5ZoC2dlqI5f2YwHbOT1EMp1fc72wuCD_OplNpWWG6MbIfAd6CpBQR1AKwSgD-ODHouoyNfiUpWFQ-7uwJXWEhXLW8gB1gInqkZ8C8Q93mLVUQxk2udagaYBn9sux-49fYbhlXpxRObwjCaj6IHVTuARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7H5BETRXjCq-QYs0OhAkTeClubM6LTYEHmknEDfJXDJYeCoCTTXvBSIvpoWip1j5rGy0iEJTJmMtxgmG0NCEJDihMqeVq-ht4lOK3LBcwL7O9ug6t8o7FncNQ2pk_pjcTHiTUgAHbP_WM1o1xnepYjn53uBxIymnyJiKZ6cxjGZIRSaA2mlqmpVKx079_lvQs2NpqiWhWa8ikz66XzeZPeMiVqui0nlI_qqf1WXkDpSRPzpXkZB77BI2GvB8ogEKiA2HneqK2lbgPbtyY4jX7_QpllUJeV4ePWlpfLwuAENOjRqnahnURPQIFd5HSt7cxmmEuPXZMgPXFkH-ZR8BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys3z9iQyoM0zsBjfJdbFCpj-q8wZrN4Gno2fsMQeNjaTm6Cjac56zM8zoy4izTFxqz5w2LiuM4npV5SjKjN5VoC6KbNUfctBGDNzh3qMnrj0QYQdidwnJVoK9Zj0XZ7PMqzR0OR5PGapj4BzKtNVJ8ec9Uhw7497NdomUPOD1rsGfUiQtvRudhGYVDnECyQQVKtTW36imVaVrfyAcALGCjD9auf3W2DDNHfwCGdZ_r2MKmCa8oG6V42VrcJes-q-XwCAw2Rp4tXjD-MFU-ad56KXGsHWpI6V2-6s4Hc-B0iqAK9Zg36zJxo47ZlijPHCvYIr3cg4fTGwsp-UxrINew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuOBam2qI3ycJjVq6OpoyFqJvFIadk7eKmmP0gYbJ5pkFvdFW2IWn6kNOLuV-2m2p_FpArXv09XyYDEJJ0HsavTc0R8kMo0xzzD16QZwLOvFgQ-ntINSWixt9zKWLQK7ljnm3-6_8K8exVFeZE6DFvIvXGjkplkP3qnaJg0fUHFh_q6lbOigozwqbIncodLFTm_JNdsCfEKjzCNkvcr7a7JSTJkONTgNsTx-C7-S6nB_sZp4L6MWX4ghtAJirtAR-6o5bOmLL0xaWLkuFQyHIBet8p1UUzKdOM5Dlk5bYwSeZceFQXIWsle0hUa__dF1TfHEAAC0Zv7tjrXVUAoqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhwL_uuqHcNS_uWu2J2N2uQTJ235XwttFOHSiSUHm_A_TIkdLs4tAnZlIp578kaLdA1P1LDRlX98KV7GAiRJ1YACs7_gpdZsL9dzsSMDYN62IN2KGV5RqneXbokgIzZNGFull2gALZ58uu-iH0ZaACirH7W1QMb0GwDy2cYdL5IMM-5Fn1IA5WiUnb2K3mx3QpgaymymC84IlpE9riQh4i-4dattKwTZmPx45ncPppxjtxiLiq6dbqs147yMWpRH4_fjAjregtPgPWjuKd8zVLkH7p1eO6r88ipsu3KGsWrDDjmyAdk3Eh5JOKElpEl1ZmKFm6KJVaIwQHe359iS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h57wteBm4kWjrYiwVCJ_PFT73datsM6M0Wj06t2nvlYSDgvndaO4NKIZXk9Rimw6AbVkWBM1eTQauXOIeOIOiAPSINsF0QWMkiv7jTHFdkgNZSxKk4zSoEGiuKSRoCUGf9vJ48h3Ks732w1LKzACkAl5sUpKKoRCzw6GTos4WV_do1mk8DRJRN-1y32wqeDKxTmJCr65-uZl2ldH6qH4G3h7-uWyiymjjbw4RceQYKsb5kqYvgNFFENjfV760qHXDH3ioJ9pK9uaUByARvIkOygSp26VLm_PC5VYede5Cfy0zVA7A8V0xKWdr3qJMMi3_hlWtwTHxXjjdybO7DUsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msxYetyncp95ZM-q-vMmo4R3kFmKgVYu52_Ic_GiY7Ym4slaox-cM0r8no4hc3-9YTIcBVyfyq54EJTFhEEuJ9VvFrSjs8A-Cr2MpniuTnnQl4YAynoxmCJo8NHSdFWGfYjGigMP6kNrqdZrfOH4C5II1adhnlrw-Ifq1WB9fjG3R-ORQfeh1e0zUahSpFtG0fxTfC4iNZxsAzr0pxVk7DoBPgOYruqqz-n4qeCCh2OQaoD0rpOKttiIwl_Ijkz-MNJjvWgBGV2p4YmD9JLPl1fUw4qiER3rUHtggnTwi69q3R1PDIQW2kGANxGVFQSBL84wecWLFeACKlIBXWS5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITl6nnj6nnhaeVY33dzICvU0xHf5QzKX9wZfV6e2dssKckGi24532f5m7bnaAbyJ6IvrXpdUf1NaAjtmfAODidZaAWjAmppZGNVRPG_MnnMzoEnoqZU-ZN2AFYzHG9GGs0jvxqVS7tE5nyocDH9E_UjeKSlaCv60AwaGtiju2D0gd-6IKDlfZhn9VCyIsKUdRiAJDInSsHe72vSOFaYvjoyvl5EEMkr6K6fVg8tk7MSdC7bfdNNpolkarUw__dAiqV0xwRG2KBkl0dd2zmUbu9FjCcU0Sh2rBQ0bGTz2r2Av0g6a2culi7QixnX9_DbHXllyeMlDf8Ha-X5u_qrtHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=BlFF7TrgoMUKl84UWo69ELFaoGWYjGAqpVqfz7MFkF0mZJf9GcZRxAPa5fsJFsQXryA6WwL0oAuGL0yukMO2F50NqanhepJeEc6JERi-UFqgS8FMgRPr2gFa4jHjgpFUbJhrC16aM4gsJoXEu7WDRPxjYAI7cZCBLzSak1A_1gtwAb_wYdElTDHNs0sjhBEpS_46R-1Q5ae9gaj5JgDMgjoFq00ecBEYKjDPSQVOo21EfkZyIVvVGvRcJb-uqfzITQAQR3YJa7CMeiyNpXGfrdkIEbJK570N0GMCQSbynUY06Hlo-Xx667rBRMwakNt6faLaBlbs4qVUsDgFVd8z7wFsJZtZdtwLXDem-4dLwn6ows-wHvgTFKSm_lHyYSRk3U5VPKvcHkSEvih5TmEB-DSGNN6HDAHlxsXAD-t2C7s_urEJ9_79EQ7Jb4Y2K73Lx6OrhacszrYJ15p9lZNndWzuo9N04iXgcFzs-8TBB3USggFt-l3OIherypnhljckgxNMYyiQmHSbvhyl1xw7-851W9qRRrRSq_jQD0JL-NCXN35LG7qifMXyxqktE6Nh558kHstC3Q_DOSfqIxx2uJLrKplwettSuYPqAyKQhv2q4zYjjs9oTMdpN4rIma_IzlNx2L1tzMWgiW5qgm3H6akOvXnp-plhXpHLhgvrHEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=BlFF7TrgoMUKl84UWo69ELFaoGWYjGAqpVqfz7MFkF0mZJf9GcZRxAPa5fsJFsQXryA6WwL0oAuGL0yukMO2F50NqanhepJeEc6JERi-UFqgS8FMgRPr2gFa4jHjgpFUbJhrC16aM4gsJoXEu7WDRPxjYAI7cZCBLzSak1A_1gtwAb_wYdElTDHNs0sjhBEpS_46R-1Q5ae9gaj5JgDMgjoFq00ecBEYKjDPSQVOo21EfkZyIVvVGvRcJb-uqfzITQAQR3YJa7CMeiyNpXGfrdkIEbJK570N0GMCQSbynUY06Hlo-Xx667rBRMwakNt6faLaBlbs4qVUsDgFVd8z7wFsJZtZdtwLXDem-4dLwn6ows-wHvgTFKSm_lHyYSRk3U5VPKvcHkSEvih5TmEB-DSGNN6HDAHlxsXAD-t2C7s_urEJ9_79EQ7Jb4Y2K73Lx6OrhacszrYJ15p9lZNndWzuo9N04iXgcFzs-8TBB3USggFt-l3OIherypnhljckgxNMYyiQmHSbvhyl1xw7-851W9qRRrRSq_jQD0JL-NCXN35LG7qifMXyxqktE6Nh558kHstC3Q_DOSfqIxx2uJLrKplwettSuYPqAyKQhv2q4zYjjs9oTMdpN4rIma_IzlNx2L1tzMWgiW5qgm3H6akOvXnp-plhXpHLhgvrHEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOrevN9on39E409HST0ik9m1a9oPJHzS-XJaK-xtOcR8Zv66rPFI3Fk8MbXMkhX-mAW-x3jDBu-4zNzymxofq-LOuI74MuBjOyko4Dh6K8N3MngwxsZJQGVhKd7iaZWMRf4HRQqThHMYWDuSj2a2o599F1SKaLLl7TkC4PyMnI2S3QEINWxNGhv2kksy9dXcOmQuGcZ6qsRI0ez-IzAqnphQLhJws5SqinAYWxFmFg0eL6_Vy3xsSD9kEqfh7F-UwRLqSB6G-zkWoh7DZJgo-kP2jNnzQFQS2pJho1zGCIzsZQru4lh4eo6PtjjKCAy9u8AUZ7P9X18_mNBDlxH6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0vsjxyY8qQQXUBf0wqxcAdt5fGfrg2iLMW9c5d4C2VLJeVlBlULTDK1-qdzzKuPvCnL0SirspU0C4V30Zh13MPeUZrgHQ1vC-2tgaYPTnbnZ8_MydoGc0tYucHLKVyh7cD_0_B7zzY3uAaSK87UQP0XL4ATk4UAidIn2K9ZQ7Ag2vZEB1RsXN9wPv9J9NWiuCsnu9p__-j93XtjOtfIj8Ia_dT4A05_DK9el84-d7fvfNMf7htQBJJwig-gFTp68HfgMWbBivUhlvm4PUBFZDLSVKNV3J0bWBA1H5YdbwLmX3xshHaZ8GKQvDKTnWlo6FQyFcGJnufe8rezTBaXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUu1el4_xsGsQucBJuJwkQUwFLav_Swzs-vsSCeTEgOHe8LdViijRcv-x-OsMVemgmfIRis0lYBKTuQyQ5S4LP87gJdVe7zdkNh4w4c1Ml7si7T02sbIeHGGxFfkeaHFpvBzJtRF6iuphOdRruna1b3lJkIFxTAxbzktEMt8V3aeqALcDd-Lmbc0a7IenA2E58zE6aNNO_9uSoMTQZJ7LuYqKw-PY6knLegm5wNQzUMHgFRJ1_kce2UNwD1pKoih9c3Ul82ATRMLOcCw8vqe9ik6np5h-6uUivrj6KbFAM-zlnyZz3DGKmnPfwsK4WIkL4X8dTjMCnh-wFxpakmuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3k0ThXo74qDbVhmpcZOCmRPEKgcaeRhFW54raZe_v3Lo71Svz9-gghzKrrCjbwSclv5xm2PzriaCZQyYMpBGAOzVfM5lJrzKMno7wPgupE5LFn9-ocn8VSXdk7zuSAk7PI8VSOqA_25QgEVZRxGpWf6buwhtfYNdpEs_OvmQOZSshfdWX-w0wWaF6iT6B7OIx-9L8UkuT7NQY5C2bEZo2YrCTAiKia_bMlwy4m0DJIQcLWzHHgFVndi8jwf3o1_5d35q-MtgA8toOCuXOaPLNjKmVqnL6g8bulnkeN3Eq36q2rHgm-0oUoLCRjSZSipaOr9_XxtnzjizMTj2kP5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
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
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXxv-LWAsYZCUird1tUZlwmaJ88a2vnxVK9Pztn8GHdD1ZJnchH_RYf3SnLCQhj1l_Du7UToFGBMv1remess0s52zaJyNVKwgh6qPUWiVoWiDOy6DLFbQL7rLfOVHN9bqbmWIfvvtpWx09Ow_ut2oK1F47pN4T4k4lBUE-jUfHvgjd51V81L55z6vRtimB34uZVfRC6OJxeiiBcyRIamKT7YmLAOsLsH-6ezFpZJC5TuVnqkYDw7ktcLk8Yvdvg0MrMZe1coGmmxevC0nyLYAgJeXj8RRb5_uDQkw4UWnrY_RK_9lw0AdDoLmVGCJ2Wk9LM-QZ2s5TBh4mHLZvy9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAHJbceIX6V5bZcT5PBCCN7_0QsgAPpMObU_Vz7GiQoQzXi0ypZ4s_Ku_-yaruJw8OSzfaKb8utFTgaTZrPO1UZJ3ngv8419RZwsF9kLVFeaiAvEC6Tnkqb_HQDkFL2JeakQ1VF-Efgaev-5Fv-stpJMj1g0-_pRmy7I4kVl7jEm2TkcDjjBcDL2XEDRovfa_aKFB_QqPQ69fq3Cz3D_OB2thXQT-FT1-JBjqGH-qOa-YGF5Bq07Wj0xo_3yOISAb_9-MnotsDR4iXSWdYEfURfjCw_a4I8FHUS0L9r3jMHU5PRcH19DIYG1II7baoEQJ-7VS_YRtYy9n9K6OlwUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Quj7uiOhR71-BaPLUFxrvEs-f1ZjLMe3h3I-3dbGZgBCfprLhMf55u52VbQKIcLXU-d7Z1SB5Uk9RzMF_8M4qYvLs-gv5qcSQGHFP3DWh7slzXhyTjbDPw1l5stUfiA4SpkQcCJ6iz2FnJ0Pnquok_h6_PYBOXigkTE_FAqUe0SHTO7UCYLf86aXQzrNfKCKpQtiI-nKKhVP8U631RDjoOpqmubOu1sZtv5MoRkyYwkKLU4EBvJUqmxBEYBksM7-xc1yWZ15BivlRyMYJGST86c8kQcz6u4jr6zvhb3tVVqKW8CoWxrvSKfNuUi3l6phFnCEE9ZrqTBsEr_IEAe6hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=b8e_hyqDxh7BPLWUCSPDEzEYQn2ZLv2W9P_dfvHelAnCrCvvAeugjDVeAsaLn9gr2czSw5L1RP9b8Fqoh2yxb7Xyn5808O87roFeAbfcLGbr7ekq4jA9e-i9pdy-tZfbjqxd1NF-0e2PL6c2qo6eTPHoOws54eclWD6_TuZSWKue68ehkSrpmJgi8bQgjQVYN7ukJSlSwcTY4i-Fhylkm7mCTLoKYd6HFz8gyJZu-gW-I3lRFF3q43fBozEzW1eBKDMJ6d4ieHIhcPkOynztORNDv89--X_-GYEOfYBGCgArMso22rIZ4IvSwdnB2pBvXm2CAkoxFIiZjHFHhINsRTecgsrmho2558FtF-G2rnqHs8es-a2tBu0gso-5p1RCn5fzzrB4_UsREDr8Oj5gHxwgauM91tLSeqqhPSe28F5qI5bGqFGGW67plSqWxJ96-eUEOqDnqF7jstLsN_3b9lthjeahyydxgvSbo09277HIBLZy02gArTJ2BwquztEA4NaFnmqsM0CbPjM2RCyENXeF4ngWkrTDSbcxab6GZYAJRwXVZoQLdi2XyimCdgOLXy6D_QbRxCHIEbKE91D-3kXgXTya6tn1Ea3RZDWktq9hcmt_saC7HKxCKPoD6EZLKf4CjoMQq9pkVUiolz0g4VjerEFF-tPS6Gm1tBiQImc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=b8e_hyqDxh7BPLWUCSPDEzEYQn2ZLv2W9P_dfvHelAnCrCvvAeugjDVeAsaLn9gr2czSw5L1RP9b8Fqoh2yxb7Xyn5808O87roFeAbfcLGbr7ekq4jA9e-i9pdy-tZfbjqxd1NF-0e2PL6c2qo6eTPHoOws54eclWD6_TuZSWKue68ehkSrpmJgi8bQgjQVYN7ukJSlSwcTY4i-Fhylkm7mCTLoKYd6HFz8gyJZu-gW-I3lRFF3q43fBozEzW1eBKDMJ6d4ieHIhcPkOynztORNDv89--X_-GYEOfYBGCgArMso22rIZ4IvSwdnB2pBvXm2CAkoxFIiZjHFHhINsRTecgsrmho2558FtF-G2rnqHs8es-a2tBu0gso-5p1RCn5fzzrB4_UsREDr8Oj5gHxwgauM91tLSeqqhPSe28F5qI5bGqFGGW67plSqWxJ96-eUEOqDnqF7jstLsN_3b9lthjeahyydxgvSbo09277HIBLZy02gArTJ2BwquztEA4NaFnmqsM0CbPjM2RCyENXeF4ngWkrTDSbcxab6GZYAJRwXVZoQLdi2XyimCdgOLXy6D_QbRxCHIEbKE91D-3kXgXTya6tn1Ea3RZDWktq9hcmt_saC7HKxCKPoD6EZLKf4CjoMQq9pkVUiolz0g4VjerEFF-tPS6Gm1tBiQImc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHevPVKa8zwY9uuVqaf9GOJ4JnNu76NREuTr_VNf2FBEnWQhtSTNSuDYgpvQW9hUEjb-nEkA4c4RCjTYTvCfaNSVE7q0nGgU8d_dx4xDjkE8Ed2SfMtFjv-Y9trwaatOGh1hfrIq3Z4ExqKOpRNE0F6LtVgz4HUHQitPjjWz2DMbXeIrw1fE8tZQSJMxf-v6qbqyR74b15YMgfkB5_1vyjWD9-KjkOzAoMPV-lukihioy3EmWoF868AcUaPiwfaKA_wwVrjkv-jLs3-ez3R93H4AxxbFAGlssNnj_UWUlmGXWtyqUjYs7EAfB8USZeOOCYR1gkql4kjKvb41NSrxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgjFv-J7ajf-u0PhoBPlExus9h5c2zNHsP-4Yi7SoFv275Zwu6yk82ZiivaC1A0m8JDrRuINCRjMI7mD92PAqeWORExLl5GU1YOqkLqiCLO9wOLSrnNvG2KwiR1rTWctTz8wAysWKBw3DOUxXnPozj6DFTPbNEd0YsyEZZxVizZ3-sfCmiPB4v65LdYUfJ8TP1FaxOlaCkyCUzcrW9wrs5WtfjCyXN782JHugbUSpZDZEQkrebhoOTHxBGa-MIr-9IUXERO0RkROx3ZkgtC2zXDFmkNDs-SIHyJQU33DWw93OD86f06knAKwSQG9bfMKuoysvSXJR6U_DuR1_58u-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYdminVJtQcOIAyJ-RtQtu1ysZvwECx_fRgbcaNtcjeRADBAMHNLESRugsW_jWVBKnBuEr76_3eXoaveY2_niF4leqWsljS41HsF6otJkvamnTHSWQU2yKkVh08nQmFD0ivDYChuZHCU-5WIJSj2He8xetUDItf6ItTQz3PiXfYEhciToq6sGd5-eifmlqU0NOSPmvvqppg6Jar1BQzfDnMoZKUhlgU5ruXaFsoJHN2iy9r6P0LR-naCcnCegsEl_rIVfCcJrP_eIrsr9YGdHpnpZvqt2g20Yo11ZkzEXlywChQkEvbS-e1dXEOaYq2sNT9sjalzU0C2e-Zn7RjDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU1tLc5-CvmD7pNoDuwXkI038MZxCrJdhFNrpF7mrUhuqEWUyE75DmNWi0ySwxGj1UX6XkT1ZtedpaCann05ZLck2_OayCyQzuZ1dOZVOepYeLwjv6Xpf9sHTcvWQjJKb3KwRGuvSXhRT8oOtltRCIrwBFUojU316ID8L1V5T8BprMFXmsC0tz2cNpWMiRodG8krPayFbwXpsQf1wh745ierKn4K3XoCpeGNN3TRRC7KS0jkI3ENEt-inklAOdKuEf9W5XgEsrapNXnlkYVrvFF7PQo_1yD9W_gL4djE8iP8AOwlXS3mDcwitITcTdTlFAwpUeejs9xWFE6tonINhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjNEnz5BoGnfs17yxlH3Dst8TL5OBm2M11MAl5wXL2El9VcGUP4qiXvH9lWIHTQTE6w3mTR68nY9FqLCD3vPRy9B2qJzPzBDbFn_AIyBb07rR6rFEqGFIQ5C-cxdQsIlR07zGWb7QgLfCxeFyyMTr-Ko5BqMyQ_AcOX_4UnrSoM65-GdEpcIAKK_ldQiLC10z34V4i19ThzNtzvoswx0dqiN_p2ewLLVmmOBOKx-2qFVFk6G4Is44LMBbz0gvNXHyFgm_98Hfn5P7_tecRnk9wy6bbbR58VBGiEMK9oYQc6eW1SpghHHJ3Qe5FCgFQFWWW6rx6HSyZnU-b8hjZYhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPTcaft_OdNsDN7R-SmIPV6VkpI1BLzS_KBir5eqsiek2b49qi3tebvkNMdDroo_uBpias0R2V7krhv1lBOEu0JiWRfSet8ynkveOVbIRlJNTyWHJ9LmLaEdClv_0Qgxch3cN8GU7NdZznOzwCKzJyYnjKnfEJrbp3RlOSx1GZKsVKWF6hWWGFop1ZU6lsJi1kprYSzZbw-Zs9cvsVDnWUbbpeOJ1ZIi1emkwvxJIzbC_clSA31lvfrhE2_tdi_20DP3E5u3XumpcYzKytDpcq0bv-w15Mx3eGwlTIg2z4kfA0U98leMTXyUSgmICIDjNWTG5Y8HHCbVRAoagP_Wsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIw0SEKG1sMryTN74foWcMm-I87UlBGbeE-P-piqsZ1VWarh1H0V7UU9KPZCx4x7m984n7IL6BJ31olHfU5d8QNlvC-76aZCkDe5BGaLsgD0FcRBICtSDop_bqkoAUGu0K9oYEjb09iOR7tnYRXUOzb_gUyecX8jGcS_RgDFj_kK0WXDSRsigYg4Co5HNRggkfhRf6esuxU5AuhNGAsStdStaEFsahZn_EaK5SoXzCA9nYF1hGQks8jbH1YtAvaLvjehl2QYkgVy1a7GaOPfWWMbEaIEpKsMIfWrGaKMjHaMf4E15orqz3x1Rg0xj8zyv7e06Je8J2cPBbYAHv7xiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgVp0EggNiWZx-YyWcmUFRiW2UIHEJ_jsXqUzc6pBnvXxz6BvVbmCv9cIQ5lun4oNYz1aWnUUqkBim_bHeGGESGJ_LK0VKfn1t3AfO9MGWVojdJXZyB637Xysjepu6iR-rwZrZFN82xFPrhsV80fqVeoBxVMcMv74UQxCaTeQEA4ZkIp4SrZq5DmWzQ71e8aMcy4sFCw_T5Gybc_j7JEdlI8VYLMbOLOCW0ToSlagb-KwefFQA7PqxXq-C0ZwXsRyxLeowca45xAy_O8JB_qF2b64vGXPIql7LYBgtarWrvcHBKhL_GD9T01g2X7FsbiAi7ZrYPkqaE97Rza5IfBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY-P_HMiZp0vKgrozwlbnHIWBJt7Fcbo1y6BBXfTF-ptkMHNiobuZ_GPK5ZxEOYaSpQ0KLXSHL8a3IQciAfseTx09Of4h_9GCixsvDSFecSyMZEcgEoE9egoKFvMgGMexuUIBsB7Seix0KM01xSqFJk5ExRNL1VX83ODELFhvcUReDaeY47_RZ8oSXScEoQZ8wnftmtHBHtTC3oco0iDnZ0gwa3RnU1ugX2ZorOYGNAtjVbMp3TioMYAg28dIU1LO-cS2okwdgsTQKTZKRtJan4niQ0rEaMrjdk9xnKVG-bKHejJezFTUhu1J516bBGQhlMieu5Sc54B-0G1uShlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
