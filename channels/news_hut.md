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
<img src="https://cdn4.telesco.pe/file/qHrhrOlJW0Ab8yBq6dj5CaDMG2WCOrGwMTsCnStIBblnmtpFKlb4tVx5X_UREvm12D95-Qm2Zhr6H_m8XqUi94mW8ffk3ux6fBYWFgISoqq8P01jvOA2zfGfXdTAedF05Yqz6H8vG9fHwlynwFQStGRNGEOwLgyP23uJguvMsCMFjWwqPpXcuGPx4dpaYuFgYcpukv6KBTddlkcFgjnic-GMoes9Q-RQK0FwmYlOUruous5t88J_qQ7r6t5GGunADraZm3m0rFtI31fdTDRAwPB2ABtA7LACC_OPcc-S_fRDESWeQJcMDjZ6jRoI7q_8hQ3ALopkwCMfN6cwqP0u8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 220K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 16:38:53</div>
<hr>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=i6ozpXKZ-QOkNUiycIrBbrgrqiCGgxqJCu_ZfTbmDmx5qzT-4mF0JM5k_o3XdIVOMkVc9iyNJWzZOvbmrSvgEDYqw63TUgqSOMPRHLQOpGO9YolnFaQ6z2rgGiXpE0geVkuHU3SCiz8njENQr1shx43Su1WRYvc2wc6aX-ZvWAFTHM7ilwVV06LjHYCUYfanWFCulmwiMNNpMFHyE1OSEIjpaBAUte7yskYBEuw5RvDGmYGUfSxxFQ9A_CiTjqSFVVKVaegOe6OsfSVvB2vyIh81Ukmb8Gg5kXSegxwBNn-mw27mqD_nsa7yK4KeVznVaQ2RfS64CastaJQ6Vr-rDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=i6ozpXKZ-QOkNUiycIrBbrgrqiCGgxqJCu_ZfTbmDmx5qzT-4mF0JM5k_o3XdIVOMkVc9iyNJWzZOvbmrSvgEDYqw63TUgqSOMPRHLQOpGO9YolnFaQ6z2rgGiXpE0geVkuHU3SCiz8njENQr1shx43Su1WRYvc2wc6aX-ZvWAFTHM7ilwVV06LjHYCUYfanWFCulmwiMNNpMFHyE1OSEIjpaBAUte7yskYBEuw5RvDGmYGUfSxxFQ9A_CiTjqSFVVKVaegOe6OsfSVvB2vyIh81Ukmb8Gg5kXSegxwBNn-mw27mqD_nsa7yK4KeVznVaQ2RfS64CastaJQ6Vr-rDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=pZM-6q_arxuUFg0D_xgs_lqWghCEzDvwZ7sWw-2xgrOrYbpWZcZiNWr39LmS5iNrASe_rcDANDz_b01raJh29PpK36odrVDdSTMaZK6iY8xVs6NMapqDjWIMJ2xFOVhnsbTo3ANFP0R-hlbOHJbQ5LcLWvLUeE7wmV58RjB8UCVf9PcSCmqFfIU-W3DogbyBa-Dd2Tz_krh8Z_sAB-BTbU-gk_rWkyHmSF_f1kpC2n_sdSUU7wTJIYAG_ZVHq8F-pFZYPLkw2ubtju8GFCGE1qNTGwTfK9fn2rgL4Y09Mb3fxKePZDm8itxfSK6C28X5N7AAWNkYVurtaL8pMiDnyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=pZM-6q_arxuUFg0D_xgs_lqWghCEzDvwZ7sWw-2xgrOrYbpWZcZiNWr39LmS5iNrASe_rcDANDz_b01raJh29PpK36odrVDdSTMaZK6iY8xVs6NMapqDjWIMJ2xFOVhnsbTo3ANFP0R-hlbOHJbQ5LcLWvLUeE7wmV58RjB8UCVf9PcSCmqFfIU-W3DogbyBa-Dd2Tz_krh8Z_sAB-BTbU-gk_rWkyHmSF_f1kpC2n_sdSUU7wTJIYAG_ZVHq8F-pFZYPLkw2ubtju8GFCGE1qNTGwTfK9fn2rgL4Y09Mb3fxKePZDm8itxfSK6C28X5N7AAWNkYVurtaL8pMiDnyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=bIILyTqek3zwKoD99gxy2ZFyust1ymg8C4FcFm5WkripcWxUj4jzUVzy2AKyS3IqqpFxmaUP3yqoK2WKPahBApcHtEHO-SC1c_lRAOLY79ewmrbAf4IfIWcfGmWX30VjTtuP4C_VqqQaEF7kepDg8LYFrBaz6-fkW7MuGo9IfcucJcETk9EUQrb1GF5-jHla26yUCgXGA-EC9fyyZU1xulSIvTFX8qrU1E5iMe6iw6BeKxMyPchYq04U_zZQ4_6Hqggx-i96mlC_yreumonZWuuMctOrzgACcZYUF6RDjWxW70dbNTnslWLfJD81t_ugOHG2GuRau8sGW-SrC2aBFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=bIILyTqek3zwKoD99gxy2ZFyust1ymg8C4FcFm5WkripcWxUj4jzUVzy2AKyS3IqqpFxmaUP3yqoK2WKPahBApcHtEHO-SC1c_lRAOLY79ewmrbAf4IfIWcfGmWX30VjTtuP4C_VqqQaEF7kepDg8LYFrBaz6-fkW7MuGo9IfcucJcETk9EUQrb1GF5-jHla26yUCgXGA-EC9fyyZU1xulSIvTFX8qrU1E5iMe6iw6BeKxMyPchYq04U_zZQ4_6Hqggx-i96mlC_yreumonZWuuMctOrzgACcZYUF6RDjWxW70dbNTnslWLfJD81t_ugOHG2GuRau8sGW-SrC2aBFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=nMQjJQDOP4LPag3Dy7pC1DzlTGprUF2xtcD-V4DePNAoQaGQ-Kg9-PR4mBdw9djzFutV9V6sxc2KKXghY09MRTZBswaQE6cKB7o9U-4zxG4Exu0eXrYaQgG7y5k1Z2Z_gBRlGaU_gjMglBU94Tnejoyil-f95RBQ_enAkBWYfkruohlVtsrnO_cY6b7hzZ8Yp-J5kFaTEHIL3SVU8wYHlDkkLe-SEcCGgudrUFDhurAcDA9Ojqh0ZcfM9vn7varB2e-MxJP9M-HZX5c50jM_AqMRQIe5ZZT9haVEY7Uu93xMDcEBpXOt-WBFVgQw4wD7Bo_ZXYczC7DuL0e0uR9stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=nMQjJQDOP4LPag3Dy7pC1DzlTGprUF2xtcD-V4DePNAoQaGQ-Kg9-PR4mBdw9djzFutV9V6sxc2KKXghY09MRTZBswaQE6cKB7o9U-4zxG4Exu0eXrYaQgG7y5k1Z2Z_gBRlGaU_gjMglBU94Tnejoyil-f95RBQ_enAkBWYfkruohlVtsrnO_cY6b7hzZ8Yp-J5kFaTEHIL3SVU8wYHlDkkLe-SEcCGgudrUFDhurAcDA9Ojqh0ZcfM9vn7varB2e-MxJP9M-HZX5c50jM_AqMRQIe5ZZT9haVEY7Uu93xMDcEBpXOt-WBFVgQw4wD7Bo_ZXYczC7DuL0e0uR9stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=V-GzgJ-9LiJW95AYIuGLllI98a5tqnbj6RzigVR_yEW67s9MNQdl6cXQm1NorjAW2ClPptKW-yQL6euwyt3yg5zmEojCf0ixNmtRIm1xRCcVesjGGfEmqVt8pmf2E4VpgBAifIaa1zicSUwd0251hwmDdbP6usv4OG16NNg0S3PJpzL8_d2SgtPCp37UNd4PyHumtOkPHYP4Gl8sxKh_TEPekDxoG5BfuxHYJeXN6Gn_4hNwVFaPDQoCVYx4PUZwWjQ-P8ysO46_48oXWA0oY6pQWxTWO-vQtcx4Mz76Qe1ddXt7slFkF8EjwO8s8n_D4Z1W_4X1YeP49jaVEsy3uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=V-GzgJ-9LiJW95AYIuGLllI98a5tqnbj6RzigVR_yEW67s9MNQdl6cXQm1NorjAW2ClPptKW-yQL6euwyt3yg5zmEojCf0ixNmtRIm1xRCcVesjGGfEmqVt8pmf2E4VpgBAifIaa1zicSUwd0251hwmDdbP6usv4OG16NNg0S3PJpzL8_d2SgtPCp37UNd4PyHumtOkPHYP4Gl8sxKh_TEPekDxoG5BfuxHYJeXN6Gn_4hNwVFaPDQoCVYx4PUZwWjQ-P8ysO46_48oXWA0oY6pQWxTWO-vQtcx4Mz76Qe1ddXt7slFkF8EjwO8s8n_D4Z1W_4X1YeP49jaVEsy3uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=rHq24EJf3ipgalO6xtSJZT0_P8-9DWtI5XngGfHdbfyL9J0v8F8V2PAqJPjKU_C0nbIGZEvtolDRkqb3NKQGDswxjbs6e8bhDqfYMXXfPQG_WSKY2ue4if1uNgjfhIEIsOVquYi9A8ex-Ra_vhKfAd7IH3H5qiZvcc6ZIhvfmQJ69zDLQGKTAVpzn46qERgz7h7Mj9gwdYpd452ujNPoLKWTSZOOkZKmhX6M7q938M81IoRGmrwKA-keLiZsmFq-UbPUHwxQos1HiOiu8KOWG2cVAuiKKmUEv5JajiycdOtEDeQLORXz8eY0eR0xhxZufIljoL9Nrtsg1xDgTb0Emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=rHq24EJf3ipgalO6xtSJZT0_P8-9DWtI5XngGfHdbfyL9J0v8F8V2PAqJPjKU_C0nbIGZEvtolDRkqb3NKQGDswxjbs6e8bhDqfYMXXfPQG_WSKY2ue4if1uNgjfhIEIsOVquYi9A8ex-Ra_vhKfAd7IH3H5qiZvcc6ZIhvfmQJ69zDLQGKTAVpzn46qERgz7h7Mj9gwdYpd452ujNPoLKWTSZOOkZKmhX6M7q938M81IoRGmrwKA-keLiZsmFq-UbPUHwxQos1HiOiu8KOWG2cVAuiKKmUEv5JajiycdOtEDeQLORXz8eY0eR0xhxZufIljoL9Nrtsg1xDgTb0Emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=ibio4Mry8UClgB7t0vXGfvTiaZJQOFwgFLhMgX2RNYJIuU_I4kKPI57wjQS7C9HALCZSZZDUPUioDZBnj_OiMiHcSlWLW1kcEtp3R9M-vEMtkTm4aT5On_r3cqjcWojp1dCR2O_SxcS4YNabmTjb0ubYMO5iVmCM7CMj2yX7L788e2M_5vvXCP8rQEmAWBug4J9KMrrwGBemD2Mw-kqgqcDqY_4gt7KZR9x2DmmNaUatkbJ8yBYXpchj4pI3LEIj67xd8tOpHtB4D5gsECHhqcAkhyG4anl3NsresaklGN9x--UkjSEhn-LdXQj3PBFaydn4qg3TV3ZnpfUiBvjs4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=ibio4Mry8UClgB7t0vXGfvTiaZJQOFwgFLhMgX2RNYJIuU_I4kKPI57wjQS7C9HALCZSZZDUPUioDZBnj_OiMiHcSlWLW1kcEtp3R9M-vEMtkTm4aT5On_r3cqjcWojp1dCR2O_SxcS4YNabmTjb0ubYMO5iVmCM7CMj2yX7L788e2M_5vvXCP8rQEmAWBug4J9KMrrwGBemD2Mw-kqgqcDqY_4gt7KZR9x2DmmNaUatkbJ8yBYXpchj4pI3LEIj67xd8tOpHtB4D5gsECHhqcAkhyG4anl3NsresaklGN9x--UkjSEhn-LdXQj3PBFaydn4qg3TV3ZnpfUiBvjs4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=eiswEYGajdrX1ph8dCNQW19v-OCle8qJXNLpily5CKTK6qng27jn9aSx_QdmEngWyQZTf1SgGkAnWuoRdFqV1hxbC2yMAbu0L4HyqWUf3EwaurjVhsMU3xJELUtVchq_oFQ2C85NV5B1PAlAcEkZqoRbh21KXG0RuwS8_m4QZJoNL2WYnjIJZu1eBtfuAvTZInPpWD2L8suRUmf2qYzEvPBjehUPDYy5Ht2RRBHIgCc0_bdv9ntzNtq_Q7Ys_vxD2bucnAkWxhV6eY7_CcM0dEIRSNTe1JfQEzDB8a6yr4nqu0v7puvLl0USw5eSUoN7WDzr1tlpfXnfYvxlF9t70Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=eiswEYGajdrX1ph8dCNQW19v-OCle8qJXNLpily5CKTK6qng27jn9aSx_QdmEngWyQZTf1SgGkAnWuoRdFqV1hxbC2yMAbu0L4HyqWUf3EwaurjVhsMU3xJELUtVchq_oFQ2C85NV5B1PAlAcEkZqoRbh21KXG0RuwS8_m4QZJoNL2WYnjIJZu1eBtfuAvTZInPpWD2L8suRUmf2qYzEvPBjehUPDYy5Ht2RRBHIgCc0_bdv9ntzNtq_Q7Ys_vxD2bucnAkWxhV6eY7_CcM0dEIRSNTe1JfQEzDB8a6yr4nqu0v7puvLl0USw5eSUoN7WDzr1tlpfXnfYvxlF9t70Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=ry8FbTTCY5nC-OWvGSo0u1VOnJ2htcGj5LuqRgI1B7QE6grNDseVWaWHespOLw6tTHOOKu723YhRRTkPHlPWH8kL2gyXQjAjbCWhHPruogMglzgvgpspJ3NrpM5ugwuaVdX0mWaeVvFnea5bIfdnRSTPdhsHp-IwCy378d8tRokMuW7gkhAbfCcXi31JA4z_yBwBnyt2-sdxF8v3m5KCERfL4cHILbA0H60F4HYJol9p_Xk73z-oEMr3WDjlqHm1bwxS7zTS1MnOY28_u8bpqir4TubNCPonIKPK9Lk_S0PbJ0AT__tmK5vzGH7EnR3D1Ef14N7KFOkDHB9dP4BCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=ry8FbTTCY5nC-OWvGSo0u1VOnJ2htcGj5LuqRgI1B7QE6grNDseVWaWHespOLw6tTHOOKu723YhRRTkPHlPWH8kL2gyXQjAjbCWhHPruogMglzgvgpspJ3NrpM5ugwuaVdX0mWaeVvFnea5bIfdnRSTPdhsHp-IwCy378d8tRokMuW7gkhAbfCcXi31JA4z_yBwBnyt2-sdxF8v3m5KCERfL4cHILbA0H60F4HYJol9p_Xk73z-oEMr3WDjlqHm1bwxS7zTS1MnOY28_u8bpqir4TubNCPonIKPK9Lk_S0PbJ0AT__tmK5vzGH7EnR3D1Ef14N7KFOkDHB9dP4BCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=NYnpKYZ1ypc9e_Pqq8awP-DBNYfurGAnZMUM-ml_LgYCcBMEMP5TeRNZYhdtuE3ZPnGgGLzYyXMMgTY21nr_jvU9QHnIA6poxyhh5dahLAW17Cb9zjlEQ43jJvKAIW7pX3zzj7jDzHFjtompOJ_v2ij7ZRpxTUUbIP7yiyKhJV-9i9nFZUAOPvJpTxaC4ezd743IaGLyWJKg0VCR_X_E__tpkR1R6F6bgCWfsbu3PGZqyLZT01ff69096DqyP45Pfw1u8bJlLkJbebS6QTg4v8bzR7M4pLLlb7nOs_3-rdRXj7y7TmmMTCzdiTt87qo36-eh5gFaHWufdnOYgS_R4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=NYnpKYZ1ypc9e_Pqq8awP-DBNYfurGAnZMUM-ml_LgYCcBMEMP5TeRNZYhdtuE3ZPnGgGLzYyXMMgTY21nr_jvU9QHnIA6poxyhh5dahLAW17Cb9zjlEQ43jJvKAIW7pX3zzj7jDzHFjtompOJ_v2ij7ZRpxTUUbIP7yiyKhJV-9i9nFZUAOPvJpTxaC4ezd743IaGLyWJKg0VCR_X_E__tpkR1R6F6bgCWfsbu3PGZqyLZT01ff69096DqyP45Pfw1u8bJlLkJbebS6QTg4v8bzR7M4pLLlb7nOs_3-rdRXj7y7TmmMTCzdiTt87qo36-eh5gFaHWufdnOYgS_R4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymq14t1KU6rftUVtB5W0Yb8TRhs1j8dFBCrSzRIwN5oztsqEE8hzYuue87CnabzoUN2Y6mv2Ty8zij6IBXOp-1oj-pFKgpnNoWVawVz_P_ehwjYVEOB3g6nHM-ssREww4-JBadio5okNJnHlU2hpOWRQYW8cCKxV8v9j9kKaiDT26wDuzwmq2vm4x_549peNlQoSfcWTakMXQGGFhhDrxDBwDwtnHCL9Bdgpfwp0OKdoFN9cK_ccmbTxopL-QqXbcGg7R2HLFsoDtAfjpiEjZNKC--ZonpUvtu4dYjJr_hyKcOs6xn1grsJovSw3FNd9GrzdYCNLvnEyPCtXCORBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=p7gCKhSp1jA8u_-Btz1tbNTRF-B_MiBe-hPxI22p8eFrz1xMgx_oi04jV0gvuUKEyv5MXh4WC90cXL6hgpUlbMtyAOvYbVmq5x-KsaKN42l69J2dLzl7izyp3RJCp_u3Tj8_c-GNxS6plRFb-djFlVxOjIQYadr0b1_np1J7q0C5rnPLj4HCZfqDzGoBCN3bqGz-B8WjOzas7Jeh9FP_WdBYIbOBK6oIFTedYSDh7L3JiDpXiTCeqZ80R5PeRN7KYWdKmsgr0PJmItT6VpufZL3CfcCD2oBPod1_CWtqMQzfX8wasTGygTGvpFtJHlWdZD1gFrX4dnR0XdjqBCatOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=p7gCKhSp1jA8u_-Btz1tbNTRF-B_MiBe-hPxI22p8eFrz1xMgx_oi04jV0gvuUKEyv5MXh4WC90cXL6hgpUlbMtyAOvYbVmq5x-KsaKN42l69J2dLzl7izyp3RJCp_u3Tj8_c-GNxS6plRFb-djFlVxOjIQYadr0b1_np1J7q0C5rnPLj4HCZfqDzGoBCN3bqGz-B8WjOzas7Jeh9FP_WdBYIbOBK6oIFTedYSDh7L3JiDpXiTCeqZ80R5PeRN7KYWdKmsgr0PJmItT6VpufZL3CfcCD2oBPod1_CWtqMQzfX8wasTGygTGvpFtJHlWdZD1gFrX4dnR0XdjqBCatOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=AeKuhotSjI1RNVekMJe9J3UZz54GqHTVpl1mv14ABk-TamUE0y8p-WBt_OuvnP8-8yHjnllBAk5UW5ZwAhpEdQ6Pbze6RJw75D5cf3hKbMr6Z3PrEBGH5x771ruNgQ26aZ8s4VgRCBpVqOZ9K65TsOAq2Ygd_NOjHZ_z3Bh7VWPlCMn-LE4nJW4FxblYX2mrbC4MNYqKkf_TsTU5AN5XgEn5TmMezS3D42e2znjaul9Eu49YhLig5g_lqswPpCx_LDQuFnJzHu6U5O97H8-ROnE4vi41DjhmceB3XOiSUwQr5uH5vwEnbfam6Yd2KlFjDZuoAM5NNMM2ZoKFta8jkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=AeKuhotSjI1RNVekMJe9J3UZz54GqHTVpl1mv14ABk-TamUE0y8p-WBt_OuvnP8-8yHjnllBAk5UW5ZwAhpEdQ6Pbze6RJw75D5cf3hKbMr6Z3PrEBGH5x771ruNgQ26aZ8s4VgRCBpVqOZ9K65TsOAq2Ygd_NOjHZ_z3Bh7VWPlCMn-LE4nJW4FxblYX2mrbC4MNYqKkf_TsTU5AN5XgEn5TmMezS3D42e2znjaul9Eu49YhLig5g_lqswPpCx_LDQuFnJzHu6U5O97H8-ROnE4vi41DjhmceB3XOiSUwQr5uH5vwEnbfam6Yd2KlFjDZuoAM5NNMM2ZoKFta8jkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=I3UNqGH6nZfsaY_S2Iitu4lbMjn_BaXdBR9DDTNV8WRW8r_8gNqlFteNWLi1ypY6pEyKbZ9uLmWuWijjQWrcKiUe0TnH_snOEY-JXqooNfK50PV016V8ZLUmhQW_fzOHsbPXgGHFZED-BBNM3bC9Vbhaa4QEAcltmE03ll7QmNCvhH3g0aDZ-IRUrMDIwYGoaTCwAltdVz2tKlV9W-Q67ZiaXNL7GzFx-bVQFBm-UWX1atxNKo4RROnNio8BAw76wZC8S3BxsX6AWwfLYbOFNi64S4NIMhwMHgsEVHKg0LhyKYwQ9EXtzzsCAF5tUA8Qxa0Hr41hamPzkW6sjCGA_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=I3UNqGH6nZfsaY_S2Iitu4lbMjn_BaXdBR9DDTNV8WRW8r_8gNqlFteNWLi1ypY6pEyKbZ9uLmWuWijjQWrcKiUe0TnH_snOEY-JXqooNfK50PV016V8ZLUmhQW_fzOHsbPXgGHFZED-BBNM3bC9Vbhaa4QEAcltmE03ll7QmNCvhH3g0aDZ-IRUrMDIwYGoaTCwAltdVz2tKlV9W-Q67ZiaXNL7GzFx-bVQFBm-UWX1atxNKo4RROnNio8BAw76wZC8S3BxsX6AWwfLYbOFNi64S4NIMhwMHgsEVHKg0LhyKYwQ9EXtzzsCAF5tUA8Qxa0Hr41hamPzkW6sjCGA_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg9UiFXbmB8Ou1asLFVu5MU9qE_78JWJ_KROgVAz_ecOLskpRhqHQT-7CmMr-ukgFJzqNz7dPED09JXn1RjiwjdUmwFTn8HzNC6xv6iCr6wAElU70CL7dwWEfsIv2uHjlEjiYT-lsFARp2cmrU4HGWAHw3hdlQ2XaeNqrp2Zk5POKAaJIiRDVYeKWWDNkGUHYKvII9uu3_TrZXHYFwPKfKwg5-Lypl0zkDyl6R7yaxyNNAXYssggHmBIcNzrpgzULBkIp6BpHl-u9bZx_pXEsReZqvZT3TatJji4RIS9kFxFNPO_W_xr7eKf1m3xeRtEEpwxTtJOZ0LPjWEebylJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=v89IeH0mYtWD2A8PxmBLTbN-UrF0iONGkyjo_02mwpqSTvXBjgP5XjaQ7PO0JWtq7cZHb67hzHVrjEfVBI_AyEsZwLRca0P6SVWFDQ-IK8PsNsvkf9OhSFViLVrSQWqwq-SMMId-17W9L-qvPehKxDa0A7eLmQYx5nKAypB5t-HTWENuKvmD8xrt1t8aZuljaF06NveQKDXOsIz_e-iJ5v8ECZF_LXkG84ySW4FA4za-E-ZNx97Bi12ShNbFvmSBQhijgjbxhbnMOz17WWqat6y-MFI1JBMzQXv7kSH7eUYPTPsn61XlUFWfVA6vu9a8ShnUomVQo8UYgwPWQh164g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=v89IeH0mYtWD2A8PxmBLTbN-UrF0iONGkyjo_02mwpqSTvXBjgP5XjaQ7PO0JWtq7cZHb67hzHVrjEfVBI_AyEsZwLRca0P6SVWFDQ-IK8PsNsvkf9OhSFViLVrSQWqwq-SMMId-17W9L-qvPehKxDa0A7eLmQYx5nKAypB5t-HTWENuKvmD8xrt1t8aZuljaF06NveQKDXOsIz_e-iJ5v8ECZF_LXkG84ySW4FA4za-E-ZNx97Bi12ShNbFvmSBQhijgjbxhbnMOz17WWqat6y-MFI1JBMzQXv7kSH7eUYPTPsn61XlUFWfVA6vu9a8ShnUomVQo8UYgwPWQh164g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c83xDXYIA21kdReHwriwlAfCE0PNMwVUBqWVZbAEUBKG16ZiTfw06w6ns2Vt9-DNak1Ac6OM5Fz_OaUywSFfwnw8tNoTybBx4hhbRHF1RWNkKeLQUeT4jyify5kwJtlkVU5AmGRIXDxMKLkGYD_daWLS_6Vli1w2OKzVhnYfaVLhneM_qRWIrWZFFkD0kemsXoj0GSmCL1yKXNzNnIaLcQdldhiduqI3qG0b31AvZEXZaUoP-3rFHCU9t0VQvF8FZysTXx7XoSe_lhVuTL_DuuFNLvBY6nRKVibuDCkyhCBV8c3PlGWdkZ3xi_UUXbRPcbzURoprkdW1Go9l8qgPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmbIsIUX1ruFrB2f3vnuPGVtDFthWDmBybEC9RUuAQH5nlPbOF-nm-7KMuvZ8L3V_jSG7Xecx0n71dEvMGIzoF3dLZj4i6wZlRmvntLioaVKzP2dabO2v-WiGoQfmCIhKXr2OJIyXm0B1Gg9zSq7W69bCymY5QUxHIN9aSyAfVGHf-1ZBSh8aKXUbiEiWNKF5vj_1fvLE_Q2Adoj7YXUT5K0jDY8YANOXUQHR1no_op-fyaQ_3ypVcCNOGE_LFEItfJUljMqOGz57W2XX5UBGp9VViidX3z4uZx7eUaZYDE-q2hWBvgf9ouzuqsfNZbcK2qjLYpXLste4P9hkzQFLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bXZ2pfFSYBiWOzWhAXpPV52DwZF4CcrQx7CG5ue-A8g4vTZmt-tn1eYld15UL4is91LVrXDG1-B6IkbUmJjma2HB77ufC5IpXGQE-siTBkqSbPCVahI4s9wGCgHjVYX1625zUtxvEVJiUIpkPn06EZjSJBgZqfbjI9CJ652VDQyd8l3m0GKFk1wMmXUdUJN3D_DI03IoSrj7o5tSCMExw2eXT9r0s08dFs-lTWDFWQolZ9kr55NrLkEwxvw1prQjDs2Exw9Eha1gmyK2VINGJ12t5P3XDpBZnqaaKl_pR-aGgEJit0bo5y8C5q8P0hOd0VL6lchJ1Us6DzWHrmPzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxT9xHgroECRLmhokrrkXcMFsLzz9zmWASbaXhAh5SEaud5WIZgO0dOnvMbc9zgcdkAskbzaWCYmAA50fNVqKNlvKCfkJ1vqQ129Zmplbvq-x7mFevlRRX1BxPy4EFtqK5ytjXIz_E283YJt90xewnwk1Lp-5b76l42JlMy2rAK975DjLPvA7XgInihub6eHWkpJjGHTGaTuF6CFmP7mqlobGaQJtR21VTOsPdogl5ooKSdkJwzrhYf8Hs71fCAl7fVQWclVPl-gAPyJqYMdNdgQV_ySOaOpUUK0EVH5tEybFC6WJlBcEwSF1XTapYlrCNRcOdYwu5LK8DYPBM1WGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwjNRMZrqccY4ATQNLOWknmKFnoT8R3-TWmx5t6dk5hPwbQ4QOk6YJkEq4AqrlHkwzhiqLHrR27GccWdju8SIRJ5jyB87IR1vkAk2xVSfUL6zuWtKNAPTkj2r7opn4kCifkY8LjOMma7IIVGOisXuAiHDjHbArUJrsYcjqGd2y6QVWVeERlGpHkzGhvpfDFUXAeNjH0CRtUHYKWiGurOcEL9es0bYX0XCcl-mm1-IqXng2rC5g9qTDBfsxzU25epAiQhVPC8od7yUdA6Gh9rqea-XAktBCPOKdP0fwXkFZ6_8_G5Fkb_oeQ17kOs0uAI_R8pQjP3vB2GKT9OQNgZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=DowtIvwaJ4vmBCC96I9f2qTQZmmIDQ8dasbMJvUlkDjTFrxWXWMFih2LhFsLk6dHLhjD3SOPEVd7s4FFvEWZnvXU4EOldhMaRgsGidOcJiHgD8de91VFZXQ9swopzB8Fn3RXvDso__qpAGv26nmDF8IvRuEOJtOZgpAYqt1VnzpFntWm5E5XLx46CWf7uvbroBT-zAgx3eVRut1UagqpSe54SqEsVtSdq1BzY6CUC9XFdZIY162m8BO2-UbrlUBF8TVSSl_3Rg5vt_sYf3isb4Q6a4nXenVJpNFvJoYQtI_h6WXBKHwCY1q4sf9L7H7K8zwLxxLlSI-RGv02zSITLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=DowtIvwaJ4vmBCC96I9f2qTQZmmIDQ8dasbMJvUlkDjTFrxWXWMFih2LhFsLk6dHLhjD3SOPEVd7s4FFvEWZnvXU4EOldhMaRgsGidOcJiHgD8de91VFZXQ9swopzB8Fn3RXvDso__qpAGv26nmDF8IvRuEOJtOZgpAYqt1VnzpFntWm5E5XLx46CWf7uvbroBT-zAgx3eVRut1UagqpSe54SqEsVtSdq1BzY6CUC9XFdZIY162m8BO2-UbrlUBF8TVSSl_3Rg5vt_sYf3isb4Q6a4nXenVJpNFvJoYQtI_h6WXBKHwCY1q4sf9L7H7K8zwLxxLlSI-RGv02zSITLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvC89mjNjHBWL6b0vy9acYOsPkSnLXJMexvf_rjkvsEkEXoP85dA_i8iklFuviiEghQSJU2lvl9Gs4QRkETBq_LC5wWY8h51Tq54CHyHJvtk-XXRTFckrtvAqLqE94N-xPSElXluhTwkxWiu1fkaTUYp9Xe8X8LMWt7SO39BJEaVuaXyvrL5IjOt7_JvfhtHrVklgN6sUjqrLNWWjG75kA5mPxi0bOg77-47LfXsRLcwS2e5FLR9GE7fsMr53zEbB0SjmDwYkP4WjA6I6WM1eh4Bz_n7TT-hQkLjbrTfm4p_uZig9-HStjcPx-Nv1GWCkswQormET-kwwwku8GsYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJn23RzxdbUkisbWMftnEoKDBEVObze1VHnMy1Kj90S2Vzhxc6Af2M-4G5iZSM0jvTEoaRiRgssB4G-_8egTrj7Jl9Y_qvsFO9QZUwyiwEXZci1Ar-QSOuVQD8wkE4G3Qg5TWYxPOmhoX5k8yzPBqDBD-CcPGd-oyTxNvlP9nnBcMw4Fx5nhTxGcg69NiqbE87YF6mYjibGLYSRk53YoSAiSQKuo-qlq3OuPuhKhygVxMzTxmGHVQQgaqGGfztxMwi2ikrKYCJVs0JNM1KXyfqKGac_FZel-R_DhfVNc2xdzHQdzgtgOE0vCHyo-KF0Rk_Lp07D3R6xytqsg6v61qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=pYKhS3P7C6NCwtywQq8JjwUIZVNHaR7apUXbrGOaleXWTgaZuViwZwaEfLqcShGX9TxQjWfdIXOnMZQeaDnsii3fYFmAM4uwSrc-KHryzGFC7mLt1P7APfnITuIiMxEEfrtwcoss-84gQiyLq7LUDiyqT3nQx3TYiKGoZKayHTt_8TLZjMRIkhhFz0cyJ-Orrshz6PNSNbw13g9JBBMmWQ1lCMI9UnTLskSCemKHziheZjjl9e9iai0zBd_Ddjbj5zjuBucm3k9Tc0CJWV95duDQTxlrMeGbN4mJfzEnaypvorR_GM1CIdDKnGw1w2n778zWUxcsDSk6BmoWI0ezlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=pYKhS3P7C6NCwtywQq8JjwUIZVNHaR7apUXbrGOaleXWTgaZuViwZwaEfLqcShGX9TxQjWfdIXOnMZQeaDnsii3fYFmAM4uwSrc-KHryzGFC7mLt1P7APfnITuIiMxEEfrtwcoss-84gQiyLq7LUDiyqT3nQx3TYiKGoZKayHTt_8TLZjMRIkhhFz0cyJ-Orrshz6PNSNbw13g9JBBMmWQ1lCMI9UnTLskSCemKHziheZjjl9e9iai0zBd_Ddjbj5zjuBucm3k9Tc0CJWV95duDQTxlrMeGbN4mJfzEnaypvorR_GM1CIdDKnGw1w2n778zWUxcsDSk6BmoWI0ezlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
ایرانیان حاضر در استادیوم لس‌آنجلس
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
سال‌ها به ما می‌گفتند: «شما نمی‌توانید به خاک ایران حمله کنید.»
بله، شما می‌توانید عملیات موساد انجام دهید. ما تعداد زیادی از آنها را انجام دادیم. من به بسیاری از آنها مجوز دادم.
اما شما نمی‌توانید ارتش خود را به ایران بفرستید. ما این را تغییر دادیم.
ما خلبانان شجاع خود را بر فراز آسمان ایران فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66644" target="_blank">📅 22:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66643">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در نشست بین‌المللی سیاستگذاری در اورشلیم اعلام کرد:
در ایالات متحده می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد، و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد انجام می‌دهم. خب، هیچ‌کدام درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66643" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=hB3zGvtfVO3fE6gpNSpw9nlO444pCfWkgp-PWxKvZRiFuBksNyHaHef4FK7H9NwIeNzNh2Zf_O69__WomVMz0REIlTYnb1jfdvq9DQh2oQ2rwME8-SGz2I4tRBBAmz4twNVA4TrBEmVlkkGgCi2mLxb3QhdZqlEs_cDgFx0C9MTNR8GIc-nQPAdDXe01CArc-P1jgrcLc7UEnIpyGAXfd0tSvAH64Wd1goiWyyF3p20v70acaFKB0dbd5Q_NTDV7w_lyoWyjXpItaELutn2s_UsPhwB84gtzHpLxYrXMShHOyfK8PvwwygMqcyGaDGnigAd9J75GmDDeN_Z7syhPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=hB3zGvtfVO3fE6gpNSpw9nlO444pCfWkgp-PWxKvZRiFuBksNyHaHef4FK7H9NwIeNzNh2Zf_O69__WomVMz0REIlTYnb1jfdvq9DQh2oQ2rwME8-SGz2I4tRBBAmz4twNVA4TrBEmVlkkGgCi2mLxb3QhdZqlEs_cDgFx0C9MTNR8GIc-nQPAdDXe01CArc-P1jgrcLc7UEnIpyGAXfd0tSvAH64Wd1goiWyyF3p20v70acaFKB0dbd5Q_NTDV7w_lyoWyjXpItaELutn2s_UsPhwB84gtzHpLxYrXMShHOyfK8PvwwygMqcyGaDGnigAd9J75GmDDeN_Z7syhPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون ایران،جدید در مقابل قدیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea3ncLtzHjueMltImK9Am409XYtgYfti03roztgJz7mm7O6B7BkxVh3RgQsTQKgPZGu_4k1MSpRRQqKPHSq4AXgSksWHLsZh0Bci6Fu46_lFTLhw-5jDTqlDTBIgX4z360YoII_5zJ4f7qB3otoKlMTVqNrm5EixNth5TN_c7pPuQyyDNVmS25Bb8EJJcQqeS5KTOAhtlthkZzWKcAsOTJRCp5jIWK6nGCxpm2ksBnCVVz5EgF9haPJSqi_V0QtoIg61hwbw_OBL4NH-RmVvRlqyNBT9fAY1QkJwP46pBlnwNsyNSQ8LI477B1wsQDPHwiZAUL-Cq6Jl34fjJnvSBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
با صرافی ارز دیجیتال اوربیت از جام جهانی ۲۰۲۶ جایزه بگیر!
⚽️
🔥
سوپرکاپ ۲۰۲۶ با جایزه 4,000,000 دلاری شروع شد!
‼️
بدون واریز یک دلار، رایگان ثبت‌ نام کن:
✅
وارد بخش Super Cup شو
✅
ثبت‌ نام رو بزن
✅
کارت تیم‌ های جام جهانی رو جمع کن
✅
الماس (Gem) رایگان بگیر
✅
توی مارکت پیش‌بینی شرکت کن
✅
جایزه بگیر
🏆
جوایز جذاب برنده شو:
⌚️
رولکس
🏎
پورشه 911
💵
هزاران دلار USDT
🔥
ویژه فوتبالی‌ ها:
با هر گل تیم ملی ایران 2500 جم رایگان دریافت کنید
💥
نکته مهم:
این جوایز با قرعه‌ کشی نیست و هرکس به نسبت پیش‌بینی‌ درستش از جوایز سهم می‌گیره!
توضیحات کامل کمپین سوپرکاپ
همین حالا ثبت‌ نام کن و یکی از برنده‌ های بزرگ جام جهانی ۲۰۲۶ باشی!
🌟
https://www.ourbit.com/register?inviteCode=OurbitIR</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66641" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66639">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Idgeeu6Vx1Xab0GfKOeeO18UNfKvVwex9pZ3erhTNP7-Du0si9yEOM_b_KQttsPzCnyYqWGhi_1PYki0DJ_jAUUGL6A2flSY10gBP_xjy7UGnzvMBl-iWkQhAAD7APR-25pNH-F-DPpRbU07TrM5FUu9xwsE9OkZwt37b11La99Mx49Ol4t-8K9U5buii22TGNmj5fPUyGnp92r-83UjCsofS509o_2HXfbJ9TsK8cVzClItgbulU2HQ9JmQq1LSSwmREfPuuLceUyl13vE6pWqeqNJdtOe7jWa31MYXFup0YcF0LwJuXU3a46XHR4AERvNhTRHSBynrANetj0TMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n05gAbgZ1knWGU20pNu1RdRhAuXJ6K23Qs3z_tqNaT6RsIA4G30cNmX2eTBU-VCWuHH1Oltxprk7B7lSc2dvyEoNVZiTw6VDoygBFr3V4kuS6kgjfs0O0Ah9q0SZrq7KF3-NVH2xfcM024j6cuKUEJ7Vfc3hBYCbQJDV-7sTxk1UCw8g3kp0jJyMMmcVKKC_uiXSqseUVEFti4PzUPpnjaHd1gcJokQbtjCkkNNX35mqp9oa3MtC-nTGE47TcpLIKZHkqwjj9bowdTpALXCGEiYXTVLTCvmoLt4Gmgtefv64lLkytiQIY3X0F1xB_4ncKW96JLTna1wpGgKUslPf9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOqqmH9msn-LrcsiVZ0KeKqP_R4yzuPJZLAfgdvyPFy6OG36CC-IVCudZHQ2f_2c_oBPbvm7lvQNy8NFQ_tbl06B3tn20En6qCq8G1m4zJRrrrw7a2QMoqX7FfUMYW6EOTjfYOQR5Z91y_Zl9d_0ccoguKRMD7h9TS2JPnT7COKMIZrX56XG824ufotC8GPTyRRf3ubg97UR4XhiKurDk6orWUg2C8Hkdn9c1PgBNHm6K2rgIVNHXKaLzVQzBkXrwYK79TfKsYChcnE0wMNOXRivVjWxaTZ-I-ScV0TSgQEZOj57Nsq6dDZQxufg22-mn-2KvRCL8HlxDeo3EERocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن
سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو
بدون سانسور رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
chosefil.com/fa/programs?utm_source=telegram
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66638" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66637">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyJdPmOYAZwxLQkVx_wZNGnEO8rM2Bx9DivwjpAM7kaQmFkeh7Bv75Uw9vVXEVYiDzTSJ7q45EEajXzJDRA3fQZxuIBviHulUnDoQwzQh2zcZBZDxO-jHo6oooNJrkTAXjIW6Q2YQqdcIIBKvBJozYGvHoV3G9eVPEf9Pyj0D7WQBbgR7vLdzHm6Q1xLev-uE4sPNQCC8L0KQFvlM0xGVGonJ5YfXgHl158OuQqmFFaY2mhwUnL4jsrv2qmnNeK1sUoBYcfxxOwPQbG1b03UG-Rrd1hFB73FXE7czT0MgG3UEDhCMWVtwoIlfzNfYHO9s8_7GQh2CgDxMoD9SMHUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66636">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf9kT7Y387oA7ZoqXt6-LAGrA3bbVa7-oycibnr0G5eOOsg8-dS0UxE5NTpcoZm9xVFbVze4qNnBqyuzTOpVfHgd2SPKci6vbwAuf-uVr_kr1LQv6quTIbslss6Zi-lEk0AVA37HaCShEN5SqdTUxltN3W-2W-N2JaTlQ0Zd9g1KIEtA7Z9f4JxtILX9JBvrs9Zrhc7ql18Q3M0lstTtxCK3ZQGg1GMP7u93AGbIOPr1I3pLuYPtuAk7Qv1EjW0eH5LJFw38fERXCnOo7rzB_FE3kdvC5mxO0aveA-0OHdgNUNU5HsHD4xAng9vrQqfY7mbS10EK6dr-ilK3HBu8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
نتانیاهو و صهیونیست‌ها در آستانه نابودی توافق و اقتصاد جهانی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66636" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66632">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PD3qF9cXoBdCEVh4GQANPLvdLivMibvOhiX4AzvwPzRnbD6HatOfhomck8EDdYUBUJoHifRuHNzWSrG3h7-wsdxK3MIGp5EWJdOh7D8XN7P1NU74vt5IYxtsSeJwAhrWwlExxmD2nqu0P9AAQv2BdYJTL8BDXsepkU04sqhk8u8GMGfoXgm82rGlzhfF9yIzQ8O1HC51fUg1z3XJolNrdixoOLoaYRm5DHDKRsL9_ROqUfgX6lG7fJLVqaZ4rL55AjJ5YsUCy6V1UYCLp8H1V89QFppCwcrqtoVWe4XEvsqIpZt9cq7UctKXLAFMnWOKyoSxstxrzbhezcJjFAaLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tD1chynGG1aBw9-yGeU4KBgqqXuKvwfPfpogcieGfTkBopwcsCzYRw2WFkA6UoLBf0tgmSgPAt5L9qqcYB9d_okJ40uJ-4XncOQh-OB6_2zn4z61pP3hd4wEiV82uXEDTUtmmvz5gdy18j-T0Uk-o8mWxa2DvfrBqUXzBdOjLUDmdFcOj8HMXMNpPThShcw0NgxHtDsCJvLcgiZNkbVf3TKUKZchzE6ouYTJeUaF8gWNN9p7vHFwCI4GTDS3kXRLtlhsRIc28h6ucPZ3soUMmmtNHOypbjLRtmWrqtYCUqJmFgAwyG8ZmhKp_KkblE1QDZ7YoRPAcSKi-sedj5M-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwcFBUZ-NgQZwu_5E44rmXpYQQ8IB9UssqBTMXrjudLPSsSd5WHeK7jZa4CsKhLQQgfQLS3Cqmp3YYBiC0G2rl3SD2IXv6bK_g7Ry0XT-ywUAboLMnis1_KOqrbaj5E_PkdjWnB-MgUIQ_y5QJYcRPXMIVb6NS2Ow4b9JrvU8TN2ATmxl5cHEf2Hh47QdNxqFAaFZoGuz7y1d-kX9k_QVmiQGwmKfvX1qGtUjDRna1VvJf4_f6HW59vGBTiZY3flH9WuF1QigsDy9pcdktFkRv68Um9FMgTEylRWg3JaSBlOtIZIzzPUNWiif5UWeM7mTnmo7GBGiJKqg0uu1EbG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ra6-kXXKSMa-j9MRzHd3yGamrqqmUHJgLJrYT1QzF3rFuRKvVakI__nC3JfH-8jYbuZ7gO0P4ORzLE6GT6nGRVYxC02HaTghiYYrXf7t36PMF56tzPz5WcUj81e2hD4OV8RNH4gN2BnJ8XBO1gx2XZ2iyiZ1O2aC9RmTVMYZ1qS_tS10UacMR9bmn0vERR0pnsfsJQhM6zeB3aS72MtNadqFr_qIjETCxS03ur6rljjRbRCJtZ0uGZ8tToB96YIIPcvDHC2YG0p3dm1sAvhH2oVrrAM6ckLu5wQ0tptCl0SwpDQXwm9KVq3Hk7-CY1xkNgNoev_EXYN9m3-Cg1b3YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
گروه تروریستی حزب‌الله که در زیر روستایی در بالای تپه‌ای در جنوب لبنان، تنها چند کیلومتر دورتر از مرز اسرائیل، مدفون شده است، یک «پایگاه هوایی» زیرزمینی برای پهپادها ساخته است که از آن هواپیماهای بدون سرنشین ساخت ایران را به سمت اسرائیل پرتاب می‌کند.
مقامات نظامی اسرائیل در جریان یک بازدید رسانه‌ای سازمان‌یافته از این مکان در هفته گذشته به تایمز اسرائیل گفتند که این تأسیسات زیرزمینی که با درهای فولادی عظیم ضد انفجار محافظت می‌شود، در دهه گذشته با کمک مستقیم ایران، از جمله برنامه‌ریزی و تأمین مالی، ساخته شده است.
به گفته نیروهای دفاعی اسرائیل، این تونل چند صد متر در دل کوه امتداد دارد و به عمق ۲۹ متر (۹۵ فوت) در زیر مجدل زون - از جمله زیر یک مسجد - می‌رسد.
به گفته ارتش، در داخل تونل، که به اندازه کافی پهن بوده که یک وسیله نقلیه استاندارد بتواند از آن عبور کند، حزب‌الله پهپادهای ساخت ایران را با استفاده از قطعات قاچاق شده به لبنان مونتاژ کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66632" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66631">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66631" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66630">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaaPokb_fqBORAbVQ9h2wMAPNYY62LVFyaTZTVABHp1rPC78UxadSb72lg-1bf9cXnsaO6H6LJMuH2-5W13EFZ5MY2z1RHn69dOCVGC5AxF3NDWc4cWQnv41kVqZUfEu3GqS3yJyt4mhPdeRl9_FZI5lX1nPtW2EhAFIum1fkER0u9dia9tZFPMJ43lBy45JQxevtqkXxQEkR4tUfiQ62WfAMmfWH2vik2syCMMT0FVNc6yHyw-K8cwNKCLy_Jv9DC6VoW40zb3NtIUdkZjvmjtuggmVLr7Owc_MkWEXP8Pp6Z4GdxxyvPsnNhdEkGrjOsmujHiSa6Mk3Vxubvfkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66630" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66629">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
یکی از اعضای هیات جمهوری اسلامی به صداوسیما: «اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66629" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66628">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
قالیباف:  خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم. بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66628" target="_blank">📅 20:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66627">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgrLh3BX7hmZ5uwgSrjCKOiy4wGzx_-a3o71uXb3vmC-n3TMtMLXl9CiCI_AKPYjBIr3d2yXhNJvk3TO9ApBIB_8C07WWvYWmjwhtypo9qlJNrUo8rgLunuhDaL1cUgg_9iAdTM29qBV8tdlpg2tnr_QCcrWzUYZonokFjmlSiDPwnZ_-GcRtePuufUeRlgZ7dRQiG-qMfCVf28ZvsUw-k8umMy5kHfosIUa5emhhG8hWf7aFlnPkpyBwZyTNKxn0ltzSzFe5vMn7-mlu5cQXUGNLWWplSg35Nir-Iv15JsZNvpejP9LO0qPYOUmOU76ON4doCQORqdcMW2Zyu5n_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66627" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66626">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛خبرگزاری فارس:
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66626" target="_blank">📅 20:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66625">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75671dee37.mp4?token=EOT4580qnHLM0CIEuFmy6_T3_q76Wx0uE7ifOF9xpyB3hfxE1ag6bBxVrgL5u0VxcKyPY65r2JLyg28QN-4mRps3fWaf9UGwvExblVeLRe_2Z-gYcdLA1Ec_8vkB0axR8oS6n4OSh_0JMfEerihhdJqbaK7WM5lJWVCSKw8tKRP4GUmvj-qhIdJqjlYmpyRboAFZR4RvKZ0wre7yH4Mhpyaz5smI9-x6CnwyJmRRHTf20FY0MS5kW8tUXrFeOxqobieNVm3gPn1LUedKDD40POvygBS_pF-nGzzEd2IL6P430Aa9Hz8yOxe_-bmZ9XftUvQpisDNo7CNAs4iYoR7cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75671dee37.mp4?token=EOT4580qnHLM0CIEuFmy6_T3_q76Wx0uE7ifOF9xpyB3hfxE1ag6bBxVrgL5u0VxcKyPY65r2JLyg28QN-4mRps3fWaf9UGwvExblVeLRe_2Z-gYcdLA1Ec_8vkB0axR8oS6n4OSh_0JMfEerihhdJqbaK7WM5lJWVCSKw8tKRP4GUmvj-qhIdJqjlYmpyRboAFZR4RvKZ0wre7yH4Mhpyaz5smI9-x6CnwyJmRRHTf20FY0MS5kW8tUXrFeOxqobieNVm3gPn1LUedKDD40POvygBS_pF-nGzzEd2IL6P430Aa9Hz8yOxe_-bmZ9XftUvQpisDNo7CNAs4iYoR7cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام:
من روز جمعه چهار ساعت و نیم با رئیس‌جمهور ترامپ گذراندم. این چیزی است که فکر می‌کنم در ادامه اتفاق خواهد افتاد. اگر این توافق شکست بخورد، رئیس‌جمهور ترامپ با زور کنترل تنگه هرمز را در دست خواهد گرفت.
ایالات متحده کنترل تنگه هرمز را به دست خواهد گرفت. ما برای همه کسانی که از آن عبور می‌کنند هزینه‌ای دریافت خواهیم کرد تا هزینه عملیات را تأمین کنیم.
و ما در سال تقویمی ۲۰۲۶ توافق‌های ابراهیم را گسترش خواهیم داد. ما عربستان سعودی را وارد توافق‌های ابراهیم خواهیم کرد.
و اگر ایران کنترل ایالات متحده بر تنگه هرمز را به چالش بکشد، ما آن‌ها را نابود خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66625" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66624">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=Z4UpSRYawL3e7M6t8X8QdKif27-uY8IV4-jcwEzeBwBMPC2c3nCT7jnerrtBko6IoN8EcowtaUdcJk4ixi89LxSUuPvz1zDjvlHmoRSjTclZSmXjEzc-1NrAVV9Fc64DOIp0oR5niaMxsIveAsMH7AjYknRzUqf2ZdwMlmCNTG04xAPDh0o3rRhawDx7AJTtNdnbY38ROQ_neZ0pEvsPPWqbSoAyORdOQniF1_z-P-zvgUUzsmQkWxsii1LdldZqQ9cNRejChZ9KVRh7u8PlupPuKAuElpntDXg2kWK5lNbFiof1VKmN53fFZJSzaeR62tQb8sD5PpeBToqzxpRYAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=Z4UpSRYawL3e7M6t8X8QdKif27-uY8IV4-jcwEzeBwBMPC2c3nCT7jnerrtBko6IoN8EcowtaUdcJk4ixi89LxSUuPvz1zDjvlHmoRSjTclZSmXjEzc-1NrAVV9Fc64DOIp0oR5niaMxsIveAsMH7AjYknRzUqf2ZdwMlmCNTG04xAPDh0o3rRhawDx7AJTtNdnbY38ROQ_neZ0pEvsPPWqbSoAyORdOQniF1_z-P-zvgUUzsmQkWxsii1LdldZqQ9cNRejChZ9KVRh7u8PlupPuKAuElpntDXg2kWK5lNbFiof1VKmN53fFZJSzaeR62tQb8sD5PpeBToqzxpRYAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام ؛به ایرانی‌ها می‌گویم اگر صدای من را می‌شنوید:
وقتی شما از حزب‌الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66624" target="_blank">📅 19:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66623">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqr6s87goDTcNcKrueKqZNBdO50fOUe14cyZFL2JgvLXdnsqT_s9vdsZIr_b-gmMjnxFCtC2BispKcowONv2_EPgKebDVCXB-WbAa6CblzZJPklzAHMFPlGK6ZLbFRgzF3OCd1bE3bhlpc9fzjYE6AogpypZCwOCk8ADRgxu__ZAsaFxA5fp3GAgQNjOQrguXk5uIArX2lLUEWxqGgzICDAlT_xTu0ubMPpQmbndd2ArEiS7jiRDRWxvPEI3cZ5BNp1hqcC5M6y0uLVs0jD9PR3D3kxOvNKG0HusCjGAO5IyWbXE0FqA163rGO-q3g-kxcwrmn75urFPS2H8PsZWfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی اسرائیل مواضع گروه حزب‌الله را در اردوگاه البریج لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66623" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66622">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
رویترز به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد نخستین دور گفت‌وگوها با آمریکا در سوئیس به پایان رسیده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66622" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66621">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇱🇧
حزب‌الله:
بار دیگر رویکرد مذاکره مستقیم با دشمن صهیونیستی و جلسات آن و آنچه از آن ناشی میشود را رد میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66621" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66620">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2adw-RdiUDCKMqRfreOmg3TRA7hvn0BTiKAYqU8bPWwdDoRaijsRV8K4ywSzbDYs0Upt8XFDhaDy78qWT1XNzzJeJBV4ANzujtH4j-SYElqYllpUPBZxj0r5rMm99JZFBO3fL-1EVRsg9-_NeJa-CF5eGgLPh2nFde7Echr6_2IuY0Qi1jfEmFWVKZ324btgtLHp2ZUpd0AF8CQP_N5hIKMjnucKKSuHpP-vDxaH5h3TkBhWnWSDxoOxq6qHevwc5JWhapowf3KJXrAZDdIYGNE1Jr-HgHjoY12_OvNXU8k0MjELHESz0V8JfNpxN29HtSFYSILhbrDICebblcGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بند اول تفاهم‌نامه اسلام‌آباد:
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66620" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66619">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
اسرائیل هیوم؛اسرائیل سه شرط اصلی خود را برای پذیرش مفاد یادداشت تفاهم مربوط به لبنان اعلام کرد:
خروج کامل گروه تروریستی حزب‌الله از شمال رود لیتانی
نابودی کامل زیرساخت‌های این گروه در جنوب لیتانی
اعطای آزادی کامل عملیات زمینی و هوایی به اسرائیل برای مقابله و حذف هرگونه تهدید امنیتی آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66619" target="_blank">📅 17:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66618">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
رئیس ستاد ارتش اسرائیل:
آتش‌بس در لبنان شکننده است و نیروهای ما باید سطح بالایی از آمادگی را برای از سرگیری عملیات رزمی حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66618" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66617">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355294b30f.mp4?token=A_4FzEDvUnWuSsNKClPUqdXsdVkaushyBn5ah59_pY-Cj6uZtY9Q2iUuAYVBu6ig0GnCOQZd3fr1oFgN9QukXLYKOc81ESz1dE0-UOnaVOKZKzF3Gr5t0Nj0ayPKT2kvIJ8T5OQQ86d-BZq7uEMqQ7BSCcUwfOmr8ShOkVzVbuYEn_3mjl0J4UJH4iG7JlQ-AZzo08l6SukN-IUKffVmJXhju1l3mva6pd7WVXMClZ4tpnuneNwrjip-WUE_RPTbj0Y0mnHVOS8zzGdfYKStCZiKyZobNwU3FdxtirqEuE-F-NV0qktLvnONsosKJQee87Dk5aUoDnLMhxc1dCbJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355294b30f.mp4?token=A_4FzEDvUnWuSsNKClPUqdXsdVkaushyBn5ah59_pY-Cj6uZtY9Q2iUuAYVBu6ig0GnCOQZd3fr1oFgN9QukXLYKOc81ESz1dE0-UOnaVOKZKzF3Gr5t0Nj0ayPKT2kvIJ8T5OQQ86d-BZq7uEMqQ7BSCcUwfOmr8ShOkVzVbuYEn_3mjl0J4UJH4iG7JlQ-AZzo08l6SukN-IUKffVmJXhju1l3mva6pd7WVXMClZ4tpnuneNwrjip-WUE_RPTbj0Y0mnHVOS8zzGdfYKStCZiKyZobNwU3FdxtirqEuE-F-NV0qktLvnONsosKJQee87Dk5aUoDnLMhxc1dCbJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منابع داخلی:
هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66617" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66616">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd6gcchLWK11DKQS-3BwCD6qIQ5bcD9HTQPIdzs0AdTjl0OyVk0LIBwJog25lCRtCL1bFYE5yDGR5Uk7w2ii3TbsqnwE7WWEcsHqGW7H3tbNpk806tbvBUQIDygGU1JrfuF8IdnsFw0PuKNSaRQgFrlD6WTrbtxvVfgj6S8pEfW1Xt8u8W9HOTFiG4YIDDbThOnUJdcQqoP1jPTQzBiCtU-4gNyj_uOaUdH9k8y2i74KIiGgW--qURJE4wD5nb9HQQwSv7mmhZ7yzc15RGG0K8PmEKEl0hStc8Il4Fi_NiFRyT8tDSRQbD_TrG1M6Yae-pga7fCTOuDDBlQuX9MsKXjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd6gcchLWK11DKQS-3BwCD6qIQ5bcD9HTQPIdzs0AdTjl0OyVk0LIBwJog25lCRtCL1bFYE5yDGR5Uk7w2ii3TbsqnwE7WWEcsHqGW7H3tbNpk806tbvBUQIDygGU1JrfuF8IdnsFw0PuKNSaRQgFrlD6WTrbtxvVfgj6S8pEfW1Xt8u8W9HOTFiG4YIDDbThOnUJdcQqoP1jPTQzBiCtU-4gNyj_uOaUdH9k8y2i74KIiGgW--qURJE4wD5nb9HQQwSv7mmhZ7yzc15RGG0K8PmEKEl0hStc8Il4Fi_NiFRyT8tDSRQbD_TrG1M6Yae-pga7fCTOuDDBlQuX9MsKXjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66616" target="_blank">📅 17:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66615">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZxRPag1RbkEnjhTMZCphy7iJGCQVntrO2zBTjinS9g6_j2keaaJZqHbzpjpcgDe2jD--oUA_iGcDiv2wxAQzUTEsNAz_iBQWA6Hx2oSADSeAmPTZ_H_kuUhFrtt8-NVv9F7f-EhmaqrCUC3Y5DZtUugqfyikCZzyVmP8AghN7EuuvamMWDuaUs3JeC7EL17ERSSYvvKvhfiepyD5F7LiMM6y6Faz8SL6U06adGJVt1lKxJPx27NcgrELVPvnpy6z_BMgPOUhZIbtxA0P5cGBcdldoQVH1W33PyZd8rK9cgeXbmeK3drJa5gpigAdp6Er6y5rD5KBOQ-CJu0xsctcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66615" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66614">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=vLy1W4qQtHfxuKuDDExsbSDSY1QaT6LsHVq5Ks8BD9iN9RbKvLenLRGTym31Uaax03HdR4XOs4eL8epX7cbLOKaoSNx_FJXCfdRbkxeUpVlnIkHKqEeR9QmKNr2ioubJdcc43cIVGtRxmma9nDp_t8aakLZJ4LVC7qrW45oNQKl1S2g4gS59xiH5dUcqXXKA1U45gZZGuknbZaiKY0bHOqGMvkSKH7IlvAgmaWZRkL9dgEqERsO2Dtd9lzHitPvyPGtEZz_VI0ZnMw4h3uqnfgPblWYqj63w3LnK7swTClnnfX5wYHETRIZYWt2wuiNu8XTnHFvTZwh0-BHN8utq-Bh-6k303wZV9q8Anf_Q4nYGORYFAIzB1A0PUfDKq3LyxomEtdjJOx_uSnp6rPijC9x2YXWws3ak-eznEMA5EfR_oR7cTkIr1QwbXM1JtdF5CbcaS62RY3SC3O-Xp-G_B2VduMm8_v3Ut4cX8aWSZry8agrkuG4HR2FpNxXEo19FHjK8bBgVGlVoqcyYzljjptH85_UC4eCsPUtqMQ_kLXhmoRlgR15kuQj5iiAQGfDbWkGuU4-5bLIKZtjLS_t-cEPsu3D6tSPclys_CqGoczzDOW_8Rp7Mm4aU5uDxVzYy0u7iaqxKL_-QQKOKathhVD2R4I4RWucFzdos2W83gJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=vLy1W4qQtHfxuKuDDExsbSDSY1QaT6LsHVq5Ks8BD9iN9RbKvLenLRGTym31Uaax03HdR4XOs4eL8epX7cbLOKaoSNx_FJXCfdRbkxeUpVlnIkHKqEeR9QmKNr2ioubJdcc43cIVGtRxmma9nDp_t8aakLZJ4LVC7qrW45oNQKl1S2g4gS59xiH5dUcqXXKA1U45gZZGuknbZaiKY0bHOqGMvkSKH7IlvAgmaWZRkL9dgEqERsO2Dtd9lzHitPvyPGtEZz_VI0ZnMw4h3uqnfgPblWYqj63w3LnK7swTClnnfX5wYHETRIZYWt2wuiNu8XTnHFvTZwh0-BHN8utq-Bh-6k303wZV9q8Anf_Q4nYGORYFAIzB1A0PUfDKq3LyxomEtdjJOx_uSnp6rPijC9x2YXWws3ak-eznEMA5EfR_oR7cTkIr1QwbXM1JtdF5CbcaS62RY3SC3O-Xp-G_B2VduMm8_v3Ut4cX8aWSZry8agrkuG4HR2FpNxXEo19FHjK8bBgVGlVoqcyYzljjptH85_UC4eCsPUtqMQ_kLXhmoRlgR15kuQj5iiAQGfDbWkGuU4-5bLIKZtjLS_t-cEPsu3D6tSPclys_CqGoczzDOW_8Rp7Mm4aU5uDxVzYy0u7iaqxKL_-QQKOKathhVD2R4I4RWucFzdos2W83gJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت
:
بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66614" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66613">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در مورد توافق ایران:
من یک گزینه 60 روزه دارم. بعد از آن گزینه می‌توانم هر کاری که می‌خواهم انجام دهم.دیروز در نتیجه این تفاهم‌نامه با ایرانی‌ها، 19 میلیون بشکه نفت خام از خلیج فارس خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66613" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66612">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=JEEOmp-D9M5IYRK99ymbDXJ6OULr0T9sgCzKZTA_p9oSuDWpvmaADvo_WcK9PT_GnLK94yOqNuJQlJJ5-fqn5qJKkqfUBcFnKNoreJ4rH3CE4v2MVXtV9usMp7E0c8jLZtKpBFQ8AWCo86J4YBkkenDGYvC61UVB1T9qpDWjt5EiAUUEI6YSmgFj7NHf8WLGFB_Cr3It85XFwcZzYpy30FL0AgDypJXK3A225IyQbdw0E-EGrXFaRGlwjTa3wcsvdp62ohS2ZIvxUP7LLET-dGc1VkxMOU_maRCBap0CKmkpiluS-TWDwX8K3abNrT-uuDHJzZi3swPiB3z1G3L6LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=JEEOmp-D9M5IYRK99ymbDXJ6OULr0T9sgCzKZTA_p9oSuDWpvmaADvo_WcK9PT_GnLK94yOqNuJQlJJ5-fqn5qJKkqfUBcFnKNoreJ4rH3CE4v2MVXtV9usMp7E0c8jLZtKpBFQ8AWCo86J4YBkkenDGYvC61UVB1T9qpDWjt5EiAUUEI6YSmgFj7NHf8WLGFB_Cr3It85XFwcZzYpy30FL0AgDypJXK3A225IyQbdw0E-EGrXFaRGlwjTa3wcsvdp62ohS2ZIvxUP7LLET-dGc1VkxMOU_maRCBap0CKmkpiluS-TWDwX8K3abNrT-uuDHJzZi3swPiB3z1G3L6LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی‌دی‌ونس:
باز شدن تنگه هرمز، پایان دادن به برنامه هسته‌ای ایران - این کارها قبلاً انجام شده‌اند.
سوال این است که اکنون چقدر می‌توانیم با هم به موفقیت برسیم.
آیا می‌توانیم روابط در خاورمیانه را به طور دائم تغییر دهیم، یا به انجام کارها به روش قدیمی برگردیم، که ترجیح ما نیست، اما مطمئناً چیزی است که می‌تواند اتفاق بیفتد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66612" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66611">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
‏پرزیدنت ترامپ در گفت‌وگو با فاکس‌نیوز:
ایالات متحده می‌تواند به «فرشته نگهبان» تنگه هرمز تبدیل شود و ۲۰ درصد از نفت آن را سهم خود کند. «اگر لازم باشد، کنترل تنگه را در دست می‌گیریم. آن‌ها را به‌شدت در هم می‌کوبیم. اگر به توافق نرسند، از کشتی‌ها عوارض عبور خواهیم گرفت»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66611" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66610">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=G_fAvB9MppUUGAVecI6x7LX6eiA2Xfe4h7_iuzpG7oHd0huj1nHUUyRfw1PuY5MTWfjcUxf4TpADh9NrTSVqfuUypOg5WZB_GXJTgfSnPG38lWNkl_Xl7vFeHKULBbOi476x8yXfveQF0b-ByKbsYTQnH1R1nxnZ-IpqKlkUS7aHBAkn3KtLkJgrRrmuE2kirkX7YmTgcldAWDi19nMeCkpmUt6Nwnc8XMERLp-U3XLk4nDsX5pNwtGD4I-OFfM1q-Z-LMDgIZWvty3E0GP_XWwp-5yIFRtLAcpaAVJ0qMCyqaedtP-Xp0nsvYved21BW3QZ52oRgzW_D6UUUJ_75g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=G_fAvB9MppUUGAVecI6x7LX6eiA2Xfe4h7_iuzpG7oHd0huj1nHUUyRfw1PuY5MTWfjcUxf4TpADh9NrTSVqfuUypOg5WZB_GXJTgfSnPG38lWNkl_Xl7vFeHKULBbOi476x8yXfveQF0b-ByKbsYTQnH1R1nxnZ-IpqKlkUS7aHBAkn3KtLkJgrRrmuE2kirkX7YmTgcldAWDi19nMeCkpmUt6Nwnc8XMERLp-U3XLk4nDsX5pNwtGD4I-OFfM1q-Z-LMDgIZWvty3E0GP_XWwp-5yIFRtLAcpaAVJ0qMCyqaedtP-Xp0nsvYved21BW3QZ52oRgzW_D6UUUJ_75g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره عاصم منیر :
من احتمالاً در سه ماه گذشته بیش از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
بدون سیاستمداری او ما اینجا نبودیم.
او یک رهبر نظامی است، اما فکر می‌کنم خود را به عنوان یک دیپلمات عالی نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66610" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66609">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=pfVDu8VYUkGJbUh7ChdDJOK8vx1kqLZv5iEnQoLgsyyreUMrhpU_WEp1p_uJ9zTX3JTE2sSqzAyfySw7Tcbm7Rjl5-uBzK_Nt2-JYfT9K0EwA6eh8kaOWaCf8emQJUwh3h4LJdutlDpBR3yVoafNWEnwKkna3ylENvF9hKHiw0lTMgUgwjyEse_Vd2JdOeqTuH90OavzTSFDdwIv599nZWHO_mGrn_2xGp7aODe1x8SP0wMOkWfVgq2hM2I7UUfr0BJxakBsPcjUcptfaWRgSaP8LWpJHyOBm8moGNtCOSN_bzllPA_m1I-gAJvKeyak8DO0TCW9bArDLl739396dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=pfVDu8VYUkGJbUh7ChdDJOK8vx1kqLZv5iEnQoLgsyyreUMrhpU_WEp1p_uJ9zTX3JTE2sSqzAyfySw7Tcbm7Rjl5-uBzK_Nt2-JYfT9K0EwA6eh8kaOWaCf8emQJUwh3h4LJdutlDpBR3yVoafNWEnwKkna3ylENvF9hKHiw0lTMgUgwjyEse_Vd2JdOeqTuH90OavzTSFDdwIv599nZWHO_mGrn_2xGp7aODe1x8SP0wMOkWfVgq2hM2I7UUfr0BJxakBsPcjUcptfaWRgSaP8LWpJHyOBm8moGNtCOSN_bzllPA_m1I-gAJvKeyak8DO0TCW9bArDLl739396dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان دارد. مسئله اصلی توقف این است.
جی دی ونس: خانم، من فکر می‌کنم ترامپ و ایالات متحده برای توقف درگیری در لبنان بیش از هر دولتی در هر کجای دنیا تلاش کرده‌اند.
صلح هرگز آسان نیست. صلح همیشه به کمی کار نیاز دارد. همیشه به کمی بده بستان نیاز دارد.
اما ترامپ نه تنها به صلح بین ایالات متحده و ایران متعهد است، بلکه به صلح منطقه‌ای نیز متعهد است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66609" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66608">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66608" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66608" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66607">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAKX8dcjm-2YvQi3BUyNxyUlin-wkuh2zUbRDCrEA-kshVQsCFwCcVuvy_48HSXdjfqCLzfySkMNSCwxMdA6cCXDgdp_KiY95YqeAH6IA8sk0aYB6Qqge3OEvsAxT0gM4FgTE9LiI6LOT9rtJQFP3ps-PKFjfaKvipInS8pSMdUZMeZ3YXuUjnbOdkxxbpKFKhthpql40AEtOIAptlSo5g6RQnLPWd9vOul_pZ_aPUEQz9-aCUCuu-znLgggqzt_ydYbgviGpCVmnAXCyOhAzBzuRhTpEnlwEHh0v23120vORNsZrQyNod7HobrjTM9kA-i4lVkRY8yQ2rzMieVtww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66607" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66605">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDqnSTt4T2GkEm2_R1IrBsHbqmlnps9TKLnw6TuF3laE4cF2oEpyPacq-kHS1DBA7LM3MbnC9frzl9owKjw5k-CDbtRgee2YSLE8nuDq4L-qGi-jDaOwPmGsOhJNW4UZKau2nK2ZuhOew63rO3YgglJEqKzC1JJmUMKSxEwpvwNa10LLq3vyVm8OH70Lrocko-H_ZqpZBlz98p4H-5Sc_rezsn8XDdueW_RkfeDzp4G2XFfRZaO0n_0rbRe0q1uYnfMMM3g6XWUuu5TJy-_vZybBjGDx4BYmfXkRVeHpDTQFMMEVc0Fgx4d1HDmfAP-GZV7YnxjIssEMeibI8kB1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=Om2g1RIetVj6-ejkDdxLg90JlDnVGH7fo5NiMolJyes-o9ZPhL3J3WUJA04va4bXia7NHpEhpxPQYuDAWKSbnJUbxz_xP4pgtwSwptipxOMFdUzpRYe493-sdpYiVJ9djw6OSeEkVktwN_KRjyVcBza88BKoEIbsYX1iwaT6OUHr_6FkU_SqGftoG3oS-MM-YUrBdCuj3NhsS-l69LeIBfODxvEYrvWm8K6Ars8A66HIO24o27K7bCjCTFY89b8pUX4hwl0MTR5_oFZuXfJPWS-IAwCpwVNNmxU_eP-VRZ4E5UOIkGBApS4B_PMAPCnVzT15WUQm7eIs0fq54ST13g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=Om2g1RIetVj6-ejkDdxLg90JlDnVGH7fo5NiMolJyes-o9ZPhL3J3WUJA04va4bXia7NHpEhpxPQYuDAWKSbnJUbxz_xP4pgtwSwptipxOMFdUzpRYe493-sdpYiVJ9djw6OSeEkVktwN_KRjyVcBza88BKoEIbsYX1iwaT6OUHr_6FkU_SqGftoG3oS-MM-YUrBdCuj3NhsS-l69LeIBfODxvEYrvWm8K6Ars8A66HIO24o27K7bCjCTFY89b8pUX4hwl0MTR5_oFZuXfJPWS-IAwCpwVNNmxU_eP-VRZ4E5UOIkGBApS4B_PMAPCnVzT15WUQm7eIs0fq54ST13g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کریمه در طول شب پس از حمله پهپادهای اوکراینی به بندر و سایر زیرساخت‌های حیاتی
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66605" target="_blank">📅 16:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66604">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=KAS2lbPdgSy0Xn3llyzomniEJpm_L3ALN9vpRsa-zZVXmjPmiuyzYAJpuNo9A5C92-dF52Nei1BFt0IIHS57J83_cMpuR3rsIPqRVn4yzF6n9D9hEeJobDzFdSiE5yYaju65gVhxEqjSRLjWlPlgBlb3l_Mu-qkzNo7vR1Sgpnx7GLiNrfgwQwzSXxJtLR5KJ5SXHubcU5587t0TxJ0OjuVz8nqvmhu54A9M2BRLHhE4qoIL4eeHjP_Q7IrSry9-AACw2ztlxM87Jv-ZxH0iCKCReCvQ2llOjUu0OEA27sUxvhqiesyIbilsvSrWdm0Yy4HFGX8QZmC1O5MorBC0Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=KAS2lbPdgSy0Xn3llyzomniEJpm_L3ALN9vpRsa-zZVXmjPmiuyzYAJpuNo9A5C92-dF52Nei1BFt0IIHS57J83_cMpuR3rsIPqRVn4yzF6n9D9hEeJobDzFdSiE5yYaju65gVhxEqjSRLjWlPlgBlb3l_Mu-qkzNo7vR1Sgpnx7GLiNrfgwQwzSXxJtLR5KJ5SXHubcU5587t0TxJ0OjuVz8nqvmhu54A9M2BRLHhE4qoIL4eeHjP_Q7IrSry9-AACw2ztlxM87Jv-ZxH0iCKCReCvQ2llOjUu0OEA27sUxvhqiesyIbilsvSrWdm0Yy4HFGX8QZmC1O5MorBC0Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیستی که صداوسیما از موافقان موضوع مذاکره با آمریکا منتشر کرده و گفتن که این نفرات به مجتبی خامنه‌ای خیانت کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66604" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66603">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
کشور قطر از آغاز مذاکرات میان جمهوری اسلامی و ایالات متحده در سوئیس خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66603" target="_blank">📅 14:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66602">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
خبرنگار صداوسیمای جمهوری اسلامی:
یک دور تبادل پیام با میانجیگری پاکستان میان جمهوری اسلامی و آمریکا انجام شده و هیات جمهوری اسلامی نیز با هیات قطری دیدار کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66602" target="_blank">📅 14:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66601">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXaO1oHCn2313Sft-brD7CNVUYwvE7V6Dln34XtR-c5GZWXlQXBx7jpg32tkVScB2SXbslh_Y5GFC0FhVZuzeOsJa8piIFKr_yuLuHKpFxQtJZheYaoDMmpjvu2V7h7DNEEk_Ytn4eEjRIw8LZlMKg4Sh8Zw-eXlfm9A8V5W923EZvcseGRyHV05x273KzJ7DEsIvyit_ieZu6MJFjbh8YgLANJzZVuwkfna-kcuOTDjJkK4fLHkm8SPwUfVGG-r7-66BEXkyU4A1_t1FdH8QUm1b6L3amgtaIrKTGt2xO0zs-Fn8zTwGyP8jwjm7Fsz6uYmjzrVpUp8_11PtuS8hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است. بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66601" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66600">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:هیچ محدودیتی برای سربازان ارتش اسرائیل که برای رفع تهدیدها در لبنان فعالیت می‌کنند، وجود نداشته و در حال حاضر نیز وجود ندارد.»
پس از حمله به نیروهای ما، ارتش اسرائیل با قدرت زیادی پاسخ داد و تعداد زیادی از تروریست‌های حزب‌الله را از بین برد و به زیرساخت‌های تروریستی متعددی حمله کرد.
حفاظت از جان سربازان و شهروندان ما بالاترین و مطلق‌ترین اولویت ماست.
تمام دستاوردهای ارتش اسرائیل در عملیات لبنان حفظ می‌شود و نیروهای ما در منطقه امنیتی در امتداد خط زرد در لبنان مستقر شده و از آنجا علیه تروریست‌ها و زیرساخت‌های تروریستی عملیات انجام می‌دهند.
آتش‌بس اعلام شده دیروز، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که از جوامع شمال اسرائیل محافظت می‌کند، باقی می‌گذارد.
همانطور که من و بنیامین نتانیاهو، نخست‌وزیر، روشن کرده‌ایم: اسرائیل از منطقه امنیتی لبنان عقب‌نشینی نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66600" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66599">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🇮🇷
پرزیدنت پزشکیان:
«از حق غنی‌سازی خود دست نمیکشیم»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66599" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66598">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=kbki_AanN5hwoqqBh34ZMFEXG5pgLvDHnvOcXMLdXXmhXyWKcoDSnJHjwaxGPhnLpXrzBlyzZ5hLSGkPogZNeynjY0bPN8wTVXPxmeXS0Tl4Pt5SEk7PRjIftW1I7rs8vbQCU3mVtb4OeamepvELFibJ5DSLU12AE3IYgM69Ae9IquRMJ-YtANxGqyeuoifiJ4fr1FItQ9otxwHdaI57OYKst-LxLy1UCwcYLhqeQZkCdRg1nsjCFM6qxS5cc5Sddt3J0dFPWK3aBsjiNsYHhrrfRfRnrI4veZgV9Yrn0q5oohWNbplyqOtikc4-jOSlRr2rX7sp2uM2b37Ah14bxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=kbki_AanN5hwoqqBh34ZMFEXG5pgLvDHnvOcXMLdXXmhXyWKcoDSnJHjwaxGPhnLpXrzBlyzZ5hLSGkPogZNeynjY0bPN8wTVXPxmeXS0Tl4Pt5SEk7PRjIftW1I7rs8vbQCU3mVtb4OeamepvELFibJ5DSLU12AE3IYgM69Ae9IquRMJ-YtANxGqyeuoifiJ4fr1FItQ9otxwHdaI57OYKst-LxLy1UCwcYLhqeQZkCdRg1nsjCFM6qxS5cc5Sddt3J0dFPWK3aBsjiNsYHhrrfRfRnrI4veZgV9Yrn0q5oohWNbplyqOtikc4-jOSlRr2rX7sp2uM2b37Ah14bxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار هیئت آمریکایی و پاکستانی
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66598" target="_blank">📅 13:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66597">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=tD6b65uSDXbAVN15bcaBfSOfRG8E05acDekFBbJc4XmeU_l06BDVhHDzBbyFVBNgPM7N_XA9RwQUCiUVASc_-VFCt8NSoc2g3-YLUqlo8mSDqVqhzEc-evldB3sdR-P-N0U_v6GbnjR7FKpIZnvxVsozHUJDF1HEZ6rCvVDUufBUSNAZ-yYvwYVPKGeT4SdNEuLm4jnZbz5MwW_Rtc0XbTtY3WGrMOTk3chH2Q4J-174aZjGbnoid7yHkfgm777hZojFKtlW74cavy8RuJiM28KEKDkbM7DJggKBJUflzSLk591d2Q9n1ifLosmQBmjdT_nsCirh6wiEHZwWEcJVCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=tD6b65uSDXbAVN15bcaBfSOfRG8E05acDekFBbJc4XmeU_l06BDVhHDzBbyFVBNgPM7N_XA9RwQUCiUVASc_-VFCt8NSoc2g3-YLUqlo8mSDqVqhzEc-evldB3sdR-P-N0U_v6GbnjR7FKpIZnvxVsozHUJDF1HEZ6rCvVDUufBUSNAZ-yYvwYVPKGeT4SdNEuLm4jnZbz5MwW_Rtc0XbTtY3WGrMOTk3chH2Q4J-174aZjGbnoid7yHkfgm777hZojFKtlW74cavy8RuJiM28KEKDkbM7DJggKBJUflzSLk591d2Q9n1ifLosmQBmjdT_nsCirh6wiEHZwWEcJVCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم مذاکره کننده جمهوری اسلامی در محل مذاکرات:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66597" target="_blank">📅 13:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66596">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=SwJb8TdS_QIL2g_qeR6AbooThceJY7AjP3cM1uitzAo8gniF7oP7cYLVumuBRjA4qzoYs9bIUn02Tg9MQ6ONlPre6ChowBQwKUE1ojQcb7lSQj3BkwF8lhFnxPUv5LNaEbJuzNxhXSQRmpRT91ZW7uSzo_izaqBuQwZfyOpSbmHr0R1TmUNF9sAXTzyzdMLzwQNh8-s8rWFnqwVu-7RWEcHroo9IN3DGYvnpU2nW1POpBvjyRESXvf9KsZLcNUKWiFESMHwpSEhUc00qyX33e-xZ4E7Hlsl54tHJprejZ5k4McB3Mk56nXxSeBMgLVOZJnSKKROzyGLbUaZTykP_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=SwJb8TdS_QIL2g_qeR6AbooThceJY7AjP3cM1uitzAo8gniF7oP7cYLVumuBRjA4qzoYs9bIUn02Tg9MQ6ONlPre6ChowBQwKUE1ojQcb7lSQj3BkwF8lhFnxPUv5LNaEbJuzNxhXSQRmpRT91ZW7uSzo_izaqBuQwZfyOpSbmHr0R1TmUNF9sAXTzyzdMLzwQNh8-s8rWFnqwVu-7RWEcHroo9IN3DGYvnpU2nW1POpBvjyRESXvf9KsZLcNUKWiFESMHwpSEhUc00qyX33e-xZ4E7Hlsl54tHJprejZ5k4McB3Mk56nXxSeBMgLVOZJnSKKROzyGLbUaZTykP_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند چینی وارداتی
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66596" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66595">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teD-SwyIyy4M1E1I7Sg2b5R5QUVXKIJcTrRu_LpEwkaWVzpfhsG9dtJX2TIBBXf526mVeUSn3LEyN4khLJEgHGhKYK6XOP2b4DTQDx-xq4N9oJKllXbskaAFpKumyQojMHrLwMCBliIPdlnTfg99Y63KbUTy2aZaFT2KKabN-9y1zE3Jo9ZIo17V8Wxlf0PD7Xy6W3KLmycST_HWXc3m9TOF2X3RMTgj2yVcC0uthtQQxQ4KTqvhq0H2ShbqzAjXay_t8DG5kmL1aC2q_NiqULg66LwsrCuJ89L91HVFmeMIrPf_b3Z5BSVpkzHllL-bOyAKeWdf2J5gyScVDz-mmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند. اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفاده دشمن قرار می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66595" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66593">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3OV27kErkIMzNgnVAZuT7wGJ1PMMuGn91mArXIwKI0-1vrHLDGPKKrrDbF6OvX4r_W_fT7PcZoF5hGilWbHolVfRTJ4zfsf4zWJ93eM79BPZQF3I63OsBC1GqFCE6hW19mloXMhnTJC-Xjh-k32wfDs9hzgrVjTjTGUXwojSk2NsSALtsMfaDOYpNFjl-IgzfgCgNua7bo8F3mqSwRjSN1tmC5S7kP-YrtvSPkayeBA60YemYftFqZt_qPWxNxyfJ9mTkCRbsJlFxZiWkopvOQ3qz6PeLd1rFpx0pejXOae3DRZetyC6phgbPkJlkoLbpDzQ4E7CmIQ0H-Or9R4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=qcn7w-lxJiaPu9LCyHG81r5tNof77a4iJcxxOJA5vPMpq1Z5BXJS6xBORJsxcu0a1TjFrv6Bn3avjbhUN1nIhnV44uqMi1uWn4h0FgnbHmrpn-T0juiLwJ-EhutPLr51WP1IhV7IhqqXCgaoMUUgXt2iemP6ArAZmO6-2-62-HlnqZ2wN-ZHTMy07m3KcY3lQW5kxdGXsX899uYixgZFDrte1uvkdlht3n-GTO0EEeRxoVJz6qmApY20-oTrLr9AhPsEuo2OWTFfU26WWNaVmroB7Q10kA57IgF2ORbETWxBq-73d9ASWrTWAnEB2mHIvMVoRkEzCXaGbSUS2OUDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=qcn7w-lxJiaPu9LCyHG81r5tNof77a4iJcxxOJA5vPMpq1Z5BXJS6xBORJsxcu0a1TjFrv6Bn3avjbhUN1nIhnV44uqMi1uWn4h0FgnbHmrpn-T0juiLwJ-EhutPLr51WP1IhV7IhqqXCgaoMUUgXt2iemP6ArAZmO6-2-62-HlnqZ2wN-ZHTMy07m3KcY3lQW5kxdGXsX899uYixgZFDrte1uvkdlht3n-GTO0EEeRxoVJz6qmApY20-oTrLr9AhPsEuo2OWTFfU26WWNaVmroB7Q10kA57IgF2ORbETWxBq-73d9ASWrTWAnEB2mHIvMVoRkEzCXaGbSUS2OUDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رشته کوه علی طاهر، دژ استراتژیک حزب الله در جنوب لبنان:
طبق نشریات این سازمان، در زیر آن، تأسیسات «عماد ۴» - شبکه ای از تونل ها، انبارهای موشک و مقر جبهه جنوبی حزب الله - قرار دارد.
یک افسر ارشد ارتش اسرائیل فاش کرد که عملیات روز جمعه، افشای یک شبکه زیرزمینی حزب‌الله بود. ارتش اسراییل این تونل را محاصره کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66593" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66592">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBDsLXHufx5ppSyxV5Dint6VJYqvis3HOW4tUx7nARKM4dM2qCipCQDE6WVA4p7bvJ5eAPsAmGQXxRQf85JPiTFWS4-bRebdVhfG-9oCJdaSCUIXSznNcXBGNThM9Bq3ahYi2wg-EKURdFAwS9-Y4u17ZTnMoe3lLZ5mvdlvVrih_G28ODBXB5y-oLqrI9iqdldyfle-hAsAkPFP9m9Pzw7r5d3dYiFb3DmJIwQ1BiqaNSDH8zUFQVl2LOCoR7i6pCObgNkU7e-T6DX4EHQo8MrmHppVfWqxFT-PYhrSr5LNSV8njvgUm8bNDjWXONz2PIROn8DJDKb7x7xMS7IxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پس از وقفه‌ای بیش از یک ماه، صادرات نفت خام از جزیره خارک از سر گرفته شده است.
تصاویر ماهواره‌ای دو نفتکش بزرگ را در پایانه صادراتی نشان می‌دهد که نشان می‌دهد محموله‌های نفت خام ایران بار دیگر در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66592" target="_blank">📅 11:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66591">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=JEuOTPq8ZGbMzkiNpzY9TzX3GNtzn4i7pAk9PaZ7lqgTmBmS7wXLJJwy2YfvACN5GnCCQWT_UztexLu6P9u1sE-vfqug3QuJ1jw-qx4vN2uAz_5uAw6fyirRq3vPLzmCv_H1FrZY-cX1Yd5nUAn5zi59awIc8jCNtYTon1xpMEWHHhxmyrjEnXB4AY2nJSadSRdqiS0nVLdgKoiUM9htefr4ahIcDnpTntDNYPzEu93twY4nQz4LMJ3LzOcAgPVn2NpdQizpQ58olDgoeoTVCJVrowUB-HOF7MiAptO5qyqvd8Cd-54qU1_bwjm2QL8-3HQSvN-sPluSKrpIHP8F4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=JEuOTPq8ZGbMzkiNpzY9TzX3GNtzn4i7pAk9PaZ7lqgTmBmS7wXLJJwy2YfvACN5GnCCQWT_UztexLu6P9u1sE-vfqug3QuJ1jw-qx4vN2uAz_5uAw6fyirRq3vPLzmCv_H1FrZY-cX1Yd5nUAn5zi59awIc8jCNtYTon1xpMEWHHhxmyrjEnXB4AY2nJSadSRdqiS0nVLdgKoiUM9htefr4ahIcDnpTntDNYPzEu93twY4nQz4LMJ3LzOcAgPVn2NpdQizpQ58olDgoeoTVCJVrowUB-HOF7MiAptO5qyqvd8Cd-54qU1_bwjm2QL8-3HQSvN-sPluSKrpIHP8F4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از جام جهانی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66591" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66590">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEtBXNvVna0iJGi3yO71Vp3WdZPTLs7fIE0cKTynoBE4jTeT0zgKkP7LDouLGEl23Oy5PGQeK5diJKl5CBHrBIddF7wupw5bCWdHGepDqnOb36AkPrMjO4-dzoHQ2YkQnDzBptnaO4_t2-6jXqY9yfKX4fEVXEg99CM3ht3hWBcsdcYkMRkRpXI6B94VIm5ydqdL_UOpjYTq139hpmFiidtRYGdV1SJlyH0tk-vX1L6ImXc2KbUWff02EC63cd6uxl5V4ws4RTMlg1RLr_zyoT1oCeBmmtNg8Lr5q34c_d35EK9o3YJ5DGCgwAWUTXoYXqx2kddrF8Vu55SRLeGJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاونت راهبردی پزشکیان :
تجمع کنندگان بهداشت روانی جامعه را برهم زدند  تجمعات باید بعد از تشییع رهبر جمع شود.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66590" target="_blank">📅 10:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66589">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
منابع پاکستانی:
عاصم منیر فرمانده ارتش پاکستان وارد سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66589" target="_blank">📅 09:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66588">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=P4so2mR3U-Q1lQuAK_0KUmlzd7IhhJH8q0TxM6_c59auR76YAn6KsRFxTow_PRL3g-a3xj17w5E3N-a6QLKxnd7qcUO8vsLONOalHte8d2ihYg9mhr7g44oZegtvNt3lcbNqMRmxy3Kmcnq8v8aWy0dcdheyutXp0QBwDJ9i9uCkKcOeL0dgzvm-dOwzD6ZKc7Keu0_RVtgiqgbfzfi6qapdl3rn2gQ26L1uX2tGaKxKmQyBeubhj7fz7QcWC2IrDe3GIF24MzI1ezXavWAnUrwoRbYu9l8c4xW0I47eJdQudhud6ch0emtHP6Fgh0obf6Ft-c2-aI_gS6zYkmgrEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=P4so2mR3U-Q1lQuAK_0KUmlzd7IhhJH8q0TxM6_c59auR76YAn6KsRFxTow_PRL3g-a3xj17w5E3N-a6QLKxnd7qcUO8vsLONOalHte8d2ihYg9mhr7g44oZegtvNt3lcbNqMRmxy3Kmcnq8v8aWy0dcdheyutXp0QBwDJ9i9uCkKcOeL0dgzvm-dOwzD6ZKc7Keu0_RVtgiqgbfzfi6qapdl3rn2gQ26L1uX2tGaKxKmQyBeubhj7fz7QcWC2IrDe3GIF24MzI1ezXavWAnUrwoRbYu9l8c4xW0I47eJdQudhud6ch0emtHP6Fgh0obf6Ft-c2-aI_gS6zYkmgrEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صدا و سیما:
علاوه بر تنگه باید فرودگاه مهرآباد رو هم ببندیم تا مسئولین برا مذاکره نرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66588" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66587">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=OhvE2vz4SZzS1Dz_e8Ap062on6YlbdQyTVIYLFqWfUAwf3caOAndoz_WwWyrFlIyizgj3Sm1-UjUpdO1cOOVp-RxiTbljP9Q1xCmX73FRKYesPg7P1--PevcaSmU5gz-TTrXoJ1IUo6Ob3-FTQeCSVRChdm6rboRrpD_X_NHgYLB7-lcXkolAZNn-zZtqejQHfXvaGp1sVEqqS08tQFfgDWzUmoeqXh6U6YCbWiaK8V3BB0beolVPvPExQ1Qk7yg0Yuj_Epb1ZOzqYiq9oq6HidRD4veMvIFf95hCATV8qAVjyVZQ5BYPmpo4ILw4w1jysUu2D_Xvp65xyxh_LeYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=OhvE2vz4SZzS1Dz_e8Ap062on6YlbdQyTVIYLFqWfUAwf3caOAndoz_WwWyrFlIyizgj3Sm1-UjUpdO1cOOVp-RxiTbljP9Q1xCmX73FRKYesPg7P1--PevcaSmU5gz-TTrXoJ1IUo6Ob3-FTQeCSVRChdm6rboRrpD_X_NHgYLB7-lcXkolAZNn-zZtqejQHfXvaGp1sVEqqS08tQFfgDWzUmoeqXh6U6YCbWiaK8V3BB0beolVPvPExQ1Qk7yg0Yuj_Epb1ZOzqYiq9oq6HidRD4veMvIFf95hCATV8qAVjyVZQ5BYPmpo4ILw4w1jysUu2D_Xvp65xyxh_LeYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خودزنی مداح وسط هیئت:
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66587" target="_blank">📅 09:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66586">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66586" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66585">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kcXZrZpCfdnUrjDwbrYsWVAxAV_Pez4Zl1NgDy1B0a2gZvnaXVkppcdi8E0hGOo3qZHRMf_Pwr8FdmGWGdfVkCK2EHZWui2kct3eWKmss0VZYEk53m__9tyW9mrfj1g1enWA9-oJhfxlgSOkwxvGJZ8W34MLAhClVh7mt5ywQEGPrP34Kho-cAt125tVlktOAGjEr6JtU3rf7xUrmd-FH2quM5dIh_YDTMk6Kwo6YTCu1enby1UA4LZFZbnKEm3mNi74l9nzB_iRa2p_cltFl_x6sDHmiTFVEbHMwN-vl_szfJ9WlusIqG3PdatmGvcUAankjfmrIwsox8OKGYeJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66585" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66584">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUPis-uu3Kv5XkDL_c9HSCvau8E7G9Uap2Czo6QFYhQsRN6RLT2m04TR1Qq9PadLGDHamoaTHBpXP_rwu1y4kF2vYf9B5TUzsbocEFTDBHPpw6sVBPt3TiESSTepC0FemRejS6lE5Xtk1ui_cjEo7XnGcXiH7XkVU0XEIjPbQbz7-4btEu_wipNQSkGM5rtH1rjBWAcKwULhIayNqpRbu8KySoPAGMyfsAFdUn-qaQnLZXSm5nvZy8JD-VEnebGAUXbgj2Xy5WEBK59nVnAOF2iZPob89FnNB6gf7MMwUeavFidw-vUU-wC6k-3NrNCy-QNKWRm1KQggAUeeSu_K0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف بعداز ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66584" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66583">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=RbUX_0ioXiKabQwetjA1fqLXtWyDsDE0HDdw0gknH39gbtvClgO9ToCn1mz5qXPH8JfHrgmoHlWH_EU59YK82IqDey4Y_oyS1V7AHbqzcZGxm8rYWDO1rZ4HDY1ysqHMlg7aNZ-n6nRE77ei78r-dKfq6D_50hkxWMTx0ca-E0bM49U4cjCf7Z18BTBu0FoQxDo4l4QSZ02Nusi24lypUjVX6HTdauaCW4gWinIOr1B7s4dgOaeCnpu_Fg0D9BRyUYnm5Mww4T5dON36bt8yVWHbJm26kGIWx9-zhBzAqkxH_FhJWG96EWycaa9kVB1i2Kp0d48JutrHozRkmc13hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=RbUX_0ioXiKabQwetjA1fqLXtWyDsDE0HDdw0gknH39gbtvClgO9ToCn1mz5qXPH8JfHrgmoHlWH_EU59YK82IqDey4Y_oyS1V7AHbqzcZGxm8rYWDO1rZ4HDY1ysqHMlg7aNZ-n6nRE77ei78r-dKfq6D_50hkxWMTx0ca-E0bM49U4cjCf7Z18BTBu0FoQxDo4l4QSZ02Nusi24lypUjVX6HTdauaCW4gWinIOr1B7s4dgOaeCnpu_Fg0D9BRyUYnm5Mww4T5dON36bt8yVWHbJm26kGIWx9-zhBzAqkxH_FhJWG96EWycaa9kVB1i2Kp0d48JutrHozRkmc13hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی‌ونس معاون رئیس جمهور آمریکا برای شرکت در مذاکرات با ایران عازم سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66583" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66582">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCuOM_SjkJqSEvTPm_Mc2oTJNBDPtHv_YMFGnmLGEw_gCZBGx0oU71mmuVpWwNGTOYSai1E4vH5Dfp1YT0pLGBT0cyVVp7OJPpvLA2hehm5D0P0j4WpK_yzAa7a1ehhaeK83RQad5NUyebxK_KvmzuCtLAevglwZ0pSdxKOzZmYk_TFo0koOczUvxwAdAhlcen_9hQLiPWGsxhs9w04o8jLu9fhgRc4xJEeN-17BOegjKAO7bDWLy4RM8S3oqZUjyQF4CSCZJJoTgctahlDlbfEwRaKhTe-HbcYzySIC8S_0KtJEGjZ53DD0pkDyM7fum73OKNO7pnkOtT7AnAOGHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مرندی عضو تیم مذاکره‌کننده خطاب به ترامپ که گفته بود هیچ هزینه ای در تنگه هرمز نیست نوشته:
«هزینه ای وجود خواهد داشت این قطعی است»
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66582" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66581">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666063795.mp4?token=VW4cXELwjHhp76cPKn8k8iNdkLMvmRoV_F-ijl2ZDbLTyPItVYrwiFKK4BDzSUP404vGl4_moX0hC1qK1-_aMGEN6PZTVxywnCcXnltzHnXcuEy9usnnuRRMVWdPe9mnDfTjapLfBSiK6TCCa2Vnh01Vyh3ewEKIRiak86rreoQdkFHp7XkXHZYdWfJz7L6J0sG8f8G9TSSL39S_6qRbUt4FFALZOg_W4YmVorRLE-6GEfsoEko1qSRsCfeAQZu6P7YlDm0CHviUvOgV-wfQI5OEnHhCFykaKi6Ql17hfTOGc6eBKAgcC_-7kJB31dVnGyLi4eunoh_QTVUs_Y2bNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666063795.mp4?token=VW4cXELwjHhp76cPKn8k8iNdkLMvmRoV_F-ijl2ZDbLTyPItVYrwiFKK4BDzSUP404vGl4_moX0hC1qK1-_aMGEN6PZTVxywnCcXnltzHnXcuEy9usnnuRRMVWdPe9mnDfTjapLfBSiK6TCCa2Vnh01Vyh3ewEKIRiak86rreoQdkFHp7XkXHZYdWfJz7L6J0sG8f8G9TSSL39S_6qRbUt4FFALZOg_W4YmVorRLE-6GEfsoEko1qSRsCfeAQZu6P7YlDm0CHviUvOgV-wfQI5OEnHhCFykaKi6Ql17hfTOGc6eBKAgcC_-7kJB31dVnGyLi4eunoh_QTVUs_Y2bNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری که در شبکه‌های اجتماعی منتشر شده، برگه‌ای تبلیغاتی را نشان می‌دهد که گفته می‌شود به سپاه تروریستی پاسداران تعلق دارد و در آن برای اعزام نیروی داوطلب به لبنان و همکاری با گروه تروریستی حزب‌الله، حقوق ماهانه هزار دلاری وعده داده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66581" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66580">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود. از توجه شما به این موضوع متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66580" target="_blank">📅 23:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66579">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=GGYKHgvIMwB4B5pf9lOnVEeVsNuXt7NSO-S1T2_juq43LMiSMWwawvn-x7ge6d11NtstqTB9SD8W82aNPxM-amKZ77_DU7u7_w6QCGdAuvPSy3rY653RSpouRLwccFxbINxP6XhD8RoUTzuqR_X0mLhFtr-aZzJZRO5_AQM8Cs_9m1jY1SCDqGPxV6crgXP2kH8aKyl0-8cV_WxhW3ur-Ufkw4YGC8mricMxp-69g7jO6Qi8WJ3LsQ9fcgw6XbXqhcIYCIW2TnNzbHTrv1BMA-PfHpL_T3rnjxBWsaGC2pwA6Bq64b8phbpC_rnoGiXS2fu3uPFwxuAMmzo-2eazyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=GGYKHgvIMwB4B5pf9lOnVEeVsNuXt7NSO-S1T2_juq43LMiSMWwawvn-x7ge6d11NtstqTB9SD8W82aNPxM-amKZ77_DU7u7_w6QCGdAuvPSy3rY653RSpouRLwccFxbINxP6XhD8RoUTzuqR_X0mLhFtr-aZzJZRO5_AQM8Cs_9m1jY1SCDqGPxV6crgXP2kH8aKyl0-8cV_WxhW3ur-Ufkw4YGC8mricMxp-69g7jO6Qi8WJ3LsQ9fcgw6XbXqhcIYCIW2TnNzbHTrv1BMA-PfHpL_T3rnjxBWsaGC2pwA6Bq64b8phbpC_rnoGiXS2fu3uPFwxuAMmzo-2eazyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
جدید: مقامات آمریکایی ادعاهای سپاه پاسداران ایران مبنی بر بستن تنگه هرمز به دلیل تنش‌های جاری بین اسرائیل و لبنان را رد می‌کنند.
یک مقام ارشد به فاکس نیوز می‌گوید که ایران نمی‌تواند تنگه هرمز را ببندد زیرا "آنها آن را کنترل نمی‌کنند" و به حجم بالای کشتی‌هایی که اکنون از این آبراه حیاتی عبور می‌کنند اشاره می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66579" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66578">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=f3bbp4-JlEJSUkdbZ8tXwjiDIxQ9fXq9TkGQYssSYHtnm_Ix6haYwZO5WKUpMok-9l0qwxK8oHLDwXvtbPn8_42tD1Vac03QdHsWfFKK4e1wATS4o6zZhQLkZT1VCY6B-mF2GTHFWD9jR16iasLw0-469v2lyKE4PyT_GQZYhevxKZoaeORi5lEYciKi66aA0hwHPwHUJy0201B4zhQDQ26NStnbBSRi-gi8PnOMHBT57sJ1l4frO3N3_7CaY-iJft8h1GdGfdo6z7ajusvyFTV5LvfKTsn7hVJnLDdjznQjm61Oxwv6dmlbuuImLOZFZxrqxa8ub6_fg58OnUoRWBP7cMW9FsEHDlooJmVX-I3F3QoSebOGkzMXKn-a6WBUFrfLuKu077I9qAJwVNHCXauCMD_GCRDtpOcybpFU9cyGJlZ3_tHhSHWl86WpqOs-35La2tks7VbTYAKTHhKAOuYuoc6tY8JZUyX_6u2Pu9bp9O73H2Kdqm6m_MUlj3L1h43DnqsoPIhiwPqSFihb8Y6wyxdk4vEfMR-1rbDg6pkR528raFVYasFX_21C4BmjBRPSCDp_OKNbnX3nw6N4Hw1gsWpkuJlss3PcCyMGua3qE0XwOepTUa5UWa1R9fVBOp86tq5ZrEfRSbn-dUJMIVbCz4eTCN81iwUikJWEbio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=f3bbp4-JlEJSUkdbZ8tXwjiDIxQ9fXq9TkGQYssSYHtnm_Ix6haYwZO5WKUpMok-9l0qwxK8oHLDwXvtbPn8_42tD1Vac03QdHsWfFKK4e1wATS4o6zZhQLkZT1VCY6B-mF2GTHFWD9jR16iasLw0-469v2lyKE4PyT_GQZYhevxKZoaeORi5lEYciKi66aA0hwHPwHUJy0201B4zhQDQ26NStnbBSRi-gi8PnOMHBT57sJ1l4frO3N3_7CaY-iJft8h1GdGfdo6z7ajusvyFTV5LvfKTsn7hVJnLDdjznQjm61Oxwv6dmlbuuImLOZFZxrqxa8ub6_fg58OnUoRWBP7cMW9FsEHDlooJmVX-I3F3QoSebOGkzMXKn-a6WBUFrfLuKu077I9qAJwVNHCXauCMD_GCRDtpOcybpFU9cyGJlZ3_tHhSHWl86WpqOs-35La2tks7VbTYAKTHhKAOuYuoc6tY8JZUyX_6u2Pu9bp9O73H2Kdqm6m_MUlj3L1h43DnqsoPIhiwPqSFihb8Y6wyxdk4vEfMR-1rbDg6pkR528raFVYasFX_21C4BmjBRPSCDp_OKNbnX3nw6N4Hw1gsWpkuJlss3PcCyMGua3qE0XwOepTUa5UWa1R9fVBOp86tq5ZrEfRSbn-dUJMIVbCz4eTCN81iwUikJWEbio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره با ترامپ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
