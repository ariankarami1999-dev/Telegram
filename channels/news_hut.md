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
<img src="https://cdn4.telesco.pe/file/gTOIanrsI1ly7AImjH5l-r6-FiuqlGSWtyUP-KWSmLmpESTfDeIUU_WzlR_MvKBmvBBmBwBy9xFJ7v71dLMMexw5kA9HTQRqfXcEf0BNjETyOWpYgIFhpX4tMMySIxYbfuzBh6jgtnVgCHIhVkJo0sKI3CT_Sy1hj2K7D7VIQEK0o9TdJZ21y67VmWlwW0GrlS9arBAT4R4yGtrcC3RHzDpxXoIIFC86RQhfcw3YzIZ8VwOuEEhgKeXbqiGeO3eS6ASTD2-VxXfY_fQfjmWwG9jOM4qGMSlZjMSfkzXMhBoERHPML90RNP8K4gpXV3MSwrpvNaQdTYCwwmjUBBMGnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 125K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 18:58:28</div>
<hr>

<div class="tg-post" id="msg-69993">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd8b0a970.mp4?token=ZDaK4ZOKFPpuyfivpgutrb-PMNWMXBWeiP3L4Mfctd9oSDwYPCRToau6xD3AlYEh2fTbegy_5dFXOEOhpE4fO846vQ-C37IKAtkkc6zwNQZ7UdczVwFfCzJfeIdt0TdtI02ZqpAvp9L87IV98iZR1bMfVLbfDH2LjOJ_lmB7HJOlc21QceXKd77uaUu5lAlriMSxUw3ZEp8wIz0Md2YkX9B7AvLsqvcx5_FPXanPEqQz5xFxqHMgT3FDzQ5nxWOj5l76ylgr5DiNZFTe66CixVHCs77fv6hIBzkQxCHkrZGvvdNv-BK0TsHEatcoa1ypATNyLklcS3XiVI-7r26EfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd8b0a970.mp4?token=ZDaK4ZOKFPpuyfivpgutrb-PMNWMXBWeiP3L4Mfctd9oSDwYPCRToau6xD3AlYEh2fTbegy_5dFXOEOhpE4fO846vQ-C37IKAtkkc6zwNQZ7UdczVwFfCzJfeIdt0TdtI02ZqpAvp9L87IV98iZR1bMfVLbfDH2LjOJ_lmB7HJOlc21QceXKd77uaUu5lAlriMSxUw3ZEp8wIz0Md2YkX9B7AvLsqvcx5_FPXanPEqQz5xFxqHMgT3FDzQ5nxWOj5l76ylgr5DiNZFTe66CixVHCs77fv6hIBzkQxCHkrZGvvdNv-BK0TsHEatcoa1ypATNyLklcS3XiVI-7r26EfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طغیان آتشفشان در جزیره سیسیل: بسته شدن دوباره فرودگاه کاتانیا به دلیل خاکسترپراکنی آتشفشان اتنا
@News_Hut</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/news_hut/69993" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69992">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
تو برنامه عشق ابدی ورژن صربستان یه پسر بعد از اینکه توسط ی دختر رد شد سعی کرد دختره رو خفه کنه و بکشه که در نهایت نیروهای امنیتی دستگیرش کردن،بعد از وایرال شدن این حرکتش الان مردم سراسر جهان خواستار این هستن که برنامه ی عشق ابدی بصورت کامل جمع بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/news_hut/69992" target="_blank">📅 17:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69991">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766cf940aa.mp4?token=ehNHtC1BjmPS47JkS0lCLZxV_O4VcPBtAs7t_72ua40vNaXV5GWp61QEKSz3nDShb3aiFT9HCrDHzNzQIAYWK6PzCdk_Hw4ScKqdo71hqqTfwVmUu4VsZSV6hhFVF__iM4bUGKctKX3Ay-4qhN88U6M93zuqrlgeAhSnPx6oeIqFAhbOAvtw5CLfee4oK8orUgheTkODCFdH3MVSyh9oKl2d63rMSOA_sbOCq9D4MSdgz6t_XVNOQqLaO6jpllWwz2j1rL0DctiNrzu0xrTKaQjugL60ooauNBDDMDpuruYFNPoSBcfh0igKZr90BLzofDZxJ9PTFoqThU2BovM77Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766cf940aa.mp4?token=ehNHtC1BjmPS47JkS0lCLZxV_O4VcPBtAs7t_72ua40vNaXV5GWp61QEKSz3nDShb3aiFT9HCrDHzNzQIAYWK6PzCdk_Hw4ScKqdo71hqqTfwVmUu4VsZSV6hhFVF__iM4bUGKctKX3Ay-4qhN88U6M93zuqrlgeAhSnPx6oeIqFAhbOAvtw5CLfee4oK8orUgheTkODCFdH3MVSyh9oKl2d63rMSOA_sbOCq9D4MSdgz6t_XVNOQqLaO6jpllWwz2j1rL0DctiNrzu0xrTKaQjugL60ooauNBDDMDpuruYFNPoSBcfh0igKZr90BLzofDZxJ9PTFoqThU2BovM77Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
تهران نوروز 1356:
@News_Hut</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/news_hut/69991" target="_blank">📅 17:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69990">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f015c6551e.mp4?token=u2T4Obxv79ZxSbcq8dQ56ZQrQJTX4bgCcNH6Mf8cr8RHEy-DOXMk1VCzsPM2Vpk_bp2q_X_DLxYK_l0mKl6wf8Xl3fZdYQVvWnR2AbkW0BcNHC1McMz_NaJVbVM0sl3ud-IC0cB_ie1FvapP2P_WDs5WgQXWwzTXjilrP3sr3JrIkCtpoCGtgJCg1iN5hduI20Is0_zyH2ywJHgOtfXFBrJTB7Du8m00_V09RqaOLeXdj9g31XVFffzoAkGb4hdw53cwx2P3TP3DvS47zZWUTCIPd4-ccgo5GNmLV3T9Run77Jt5DveLJTQKThkMM_qc6clnbFlEROS37hYQlROqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f015c6551e.mp4?token=u2T4Obxv79ZxSbcq8dQ56ZQrQJTX4bgCcNH6Mf8cr8RHEy-DOXMk1VCzsPM2Vpk_bp2q_X_DLxYK_l0mKl6wf8Xl3fZdYQVvWnR2AbkW0BcNHC1McMz_NaJVbVM0sl3ud-IC0cB_ie1FvapP2P_WDs5WgQXWwzTXjilrP3sr3JrIkCtpoCGtgJCg1iN5hduI20Is0_zyH2ywJHgOtfXFBrJTB7Du8m00_V09RqaOLeXdj9g31XVFffzoAkGb4hdw53cwx2P3TP3DvS47zZWUTCIPd4-ccgo5GNmLV3T9Run77Jt5DveLJTQKThkMM_qc6clnbFlEROS37hYQlROqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سامانه پدافند هوایی خودکششی بسیار کوتاه‌برد گیبکا-اس، که بر اساس یک خودروی زرهی اصلاح‌شده تیگر ۴×۴ ساخته شده است، در حال انجام تمرینات آتش واقعی دیده شد و پهپادها به عنوان اهداف اصلی در آن خدمت می‌کردند.
این سامانه از لانچرهای سقفی استفاده می‌کند که قادر به شلیک موشک‌های دوش‌پرتاب ایگلا-اس یا ۹K333 وربا هستند و از موشک‌های زمین به هوای ۹M336، ۹M342 یا ۹M39 استفاده می‌کنند. این خودرو می‌تواند چهار موشک اضافی را در داخل خود حمل کند. لانچر آن دارای قابلیت چرخش ۳۶۰ درجه و برد ارتفاعی از ۵- تا ۸۰+ درجه است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/news_hut/69990" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69989">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">📌
فقط ۲۴ ساعت عضویت رایگان باز شده از همین امشب چک کن ببین چجوری میشه پول دراورد
💵
💸
🛒
این فرصت محدود رو از دست ندید
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/news_hut/69989" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69988">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=Wq5U8hsquDI-u7VdiLCP1eTI0H2FfQ5-YgpJO4ggxhQezmblp_f_V0Z9Wwf3LbNugDqqWJVx7EMY5ERYoCxv3CtiQ__MyjoMFFBYzRvbYfF514VxIr2k3k99dAydamdC90BkP4HW6IPq395aCEzze9B2oCRoxdepjDKc9XLQPuS2Mmn8lPA00YMIgvX_pbGEB5erAoTS7fUgQ5E-QQjIx9E-oPFs5-i0adHfrhyvfrClOwLUMIVO4S05_MA0g3PHwuWlEAqOZDrZ8aOGG0c789BGSEEk-EPKGCmIb022T6hFpxjDTi86sKQg0iuh1gWyz_eYWQj7k1moCLH3_V5ZWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=Wq5U8hsquDI-u7VdiLCP1eTI0H2FfQ5-YgpJO4ggxhQezmblp_f_V0Z9Wwf3LbNugDqqWJVx7EMY5ERYoCxv3CtiQ__MyjoMFFBYzRvbYfF514VxIr2k3k99dAydamdC90BkP4HW6IPq395aCEzze9B2oCRoxdepjDKc9XLQPuS2Mmn8lPA00YMIgvX_pbGEB5erAoTS7fUgQ5E-QQjIx9E-oPFs5-i0adHfrhyvfrClOwLUMIVO4S05_MA0g3PHwuWlEAqOZDrZ8aOGG0c789BGSEEk-EPKGCmIb022T6hFpxjDTi86sKQg0iuh1gWyz_eYWQj7k1moCLH3_V5ZWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💯
تنها کانالی که حتما باید توش عضو باشی
✅
چون راه پول
درآوردن رو بهت نشون میده
📝
حتما آمار کانالشو ببینید فعلا به مدت محدود عضویت رایگان باز شده فقط تا پایان فردا شب
🚫
⚠️
نمونه آموزش بازی Apple of Furtuneکه سودش تضمینیه رو براتون گذاشتیم پیش بینی های معتبر فوتبالی هم دارن
z22
:
📶
https://t.me/+MT03hkV78q9kMTc0
📶
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/news_hut/69988" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69985">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcmagH-lRxxRIzXaBUeFnmvYSVcJXHxQpTYYqYqD8h8dLz_VhAFKP1rK4TTk5bwuSUSZ9zTUFCDNfOiJVRj2tUp29vM3gDK6TWAtUOOFFsa99zlJfAjBva7X5Pu1bW8Z3u8uF9GPbSpu5lHY4hzQiFiiU0zO5du0npCdaFcj6Sj656iQLO0QAaNaohkAoPFsXmA08IUvlQ8AgE2E0Lv_XUeY0B43-nWWmuMORKmxVrKEKi_kUuRDjk6gNPttWPXiWgRMVS7eEtOZKiOtBrvUkTQ1ik9qqnMnHgz0_lTBG9cdtY4fNESWxe-Tfl1EJSrN5ABM9VicRXAIKvvce-r67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKVc7WUlW5pNAtLXCWu6dRBFCDqZaRPEziUd4HyTs4a6fRALj2V5gcmaiMbXdEBq5MkQyKG-iiTTub3D7nK6D0_N_ofOUVNBsythzfH_XrFCvUvlddMQnscWIOCrH-LEkINUC7QlFGd6xca-IxB1OnXf_49HGKyZvEYheQkCjbvpLIu4VEcJCEqi4Cf3tFgcO6ISlIwKiSvEr_qZtuTgkBncXsyWXh9jXCty-Zm6Jx7Bdruk3neSu4m5AY7C9_iqyWFpxWeevp9aaPL20In_-NNhTJagyyHSbaPZUM8JXcpLwJ8kPNpaHpAY-Qq33uQbh_s5dk-liB6z_CE20JEeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWUg_NKvR8EiV9oDsAnTtPLJB5Wq6O_o6EZYYrz9TomxDZJFCAXqNcYx9xgsjhcsAITga4hnEDy6H4uBfLx4xW7IyhNLzzGE7UlmNjFrefNWAUHSxg5KG73484abzXGLFLB4d1pcLXSHYcQjzRedKWNptCwbdiLpBZkYFQ9PONumNUmelzOy3nSHKdVTr2AwAtkNOswb0EWxihvKtfRLtcxqs42kKe-odLXj4zTtSTsgjybo0h9ahmGlfOae0Kt6dNbobbAnE5gWtfsmLg1Y6qrE6TGm3qUgkR7skE69-7vp0_wcLNJJZQiUfBbwBkhHccsAWMA6hwDZtZgJ2brDYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
❌
#فوری
؛ناوهای جنگی یو اس اس جورج واشنگتن (CVN-73)، یو اس اس شوپ (DDG-86) و یو اس اس رابرت اسمالز (CG-62) از تنگه سنگاپور عبور کرده و در حال حرکت به سمت خاورمیانه هستند.
ناو جنگی واشنگتن، ناو اصلی گروه ضربت ۵ نیروی دریایی ایالات متحده است که به طور دائم در منطقه هند و اقیانوس آرام مستقر است.
عبور از سنگاپور به سمت غرب، این گروه را به اقیانوس هند می‌رساند و مسیری بالقوه به سمت خاورمیانه را بدون نیاز به عبور از شرق تنگه مالاکا در جهت مخالف فراهم می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/69985" target="_blank">📅 16:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69984">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961a7bc8c4.mp4?token=b0EB1lpubpyGr_L_ssXlhpTEkMdmd5Aw8iIlqxDsIx48OLgfUTFANWimhlQn5ixOYhanBIE5aqTDlmZgWTLw6oI0cNqx8OUIdk_JusRa4mch8XAG4cFP26qDuocN8UekpaVe5UMhrcgTYqIE8zDV5JO2mx-IiUPWedvJw8h-Uy7258sTAbR2sqDepSNlx8pV62f0JIvxBrcdVpWrt_klAKxKv-JjAWowP9G8YgBMZUVkYhM-OAdX54ASAzQY6WhzoB8GViQPl3-8WZtYjujbH7wkR2PeGBx-FO6qea-ZIPGbL5k3RlJrNJ_gMxD816LYQIx1KMFN-NaOCthGfVXGDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961a7bc8c4.mp4?token=b0EB1lpubpyGr_L_ssXlhpTEkMdmd5Aw8iIlqxDsIx48OLgfUTFANWimhlQn5ixOYhanBIE5aqTDlmZgWTLw6oI0cNqx8OUIdk_JusRa4mch8XAG4cFP26qDuocN8UekpaVe5UMhrcgTYqIE8zDV5JO2mx-IiUPWedvJw8h-Uy7258sTAbR2sqDepSNlx8pV62f0JIvxBrcdVpWrt_klAKxKv-JjAWowP9G8YgBMZUVkYhM-OAdX54ASAzQY6WhzoB8GViQPl3-8WZtYjujbH7wkR2PeGBx-FO6qea-ZIPGbL5k3RlJrNJ_gMxD816LYQIx1KMFN-NaOCthGfVXGDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد آپاچی ۶۴ در تگزاس آمریکا سقوط کرد و خلبانان کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69984" target="_blank">📅 15:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69983">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b49c38bef.mp4?token=k93NLyokREnYbbFyvUPUMT8nAD7wdSOrqqU37034RC6y0YkA8752yMvDxIzDy9Z5Upyq3vIb6NNkvRzw0k9B2E44HhyafnNu4jyKKPr2wTgtt9YfrzWCUKQQVRL3CBCowqhx5v9XDjG3bTK-XmujQuo9OAbkpIXvSaGZPybRceoOHKptosT2cRLNKkD7rQxN1EXvNFQ4QC9ayFD28mcHpQWZG5D4B8JE2fqX6KpRgBzVY0MLEuAwCqBnFm0sacd8RAAMlaHzKWz1awJSU0ONnIYWOMBped96jeA5KdikAD3qapK94HwcJsn0ASuV_LzeWo70qKQrJY2c5PZU54a-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b49c38bef.mp4?token=k93NLyokREnYbbFyvUPUMT8nAD7wdSOrqqU37034RC6y0YkA8752yMvDxIzDy9Z5Upyq3vIb6NNkvRzw0k9B2E44HhyafnNu4jyKKPr2wTgtt9YfrzWCUKQQVRL3CBCowqhx5v9XDjG3bTK-XmujQuo9OAbkpIXvSaGZPybRceoOHKptosT2cRLNKkD7rQxN1EXvNFQ4QC9ayFD28mcHpQWZG5D4B8JE2fqX6KpRgBzVY0MLEuAwCqBnFm0sacd8RAAMlaHzKWz1awJSU0ONnIYWOMBped96jeA5KdikAD3qapK94HwcJsn0ASuV_LzeWo70qKQrJY2c5PZU54a-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیکی که قراره برای بنزین اجرا بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69983" target="_blank">📅 15:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69982">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cea94911.mp4?token=v7wWXJFkCf735lNmQqIlUirBpQITuTvmxmb0HSvMuYtDMwhwGPyG0I-nMsZqrom2ykSsSZAgdfAd6Kd142VS-CwSm72C50T7aqqhmH_bBPc4ujcsHnTa6Co_V_43fOXPVr7AILNAWH-nM_OzQXVCSIXyDHYfpH4uRbR80pXY3_DVANpAai5GMJyNX7iBhfUYLC27LVSzHq7rWY__NousbLcQmwfEVNECzbmF_E2LJaIW4vBkczi_s9sXIIGO3LWAVX4b3Bpl0_gaTOby-e5aMKCHqKxOIqbsq9bzxfsgzf29MX-C1iJUItWSytgSZVFylLCsf5EirdhXAyU-6c8DRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cea94911.mp4?token=v7wWXJFkCf735lNmQqIlUirBpQITuTvmxmb0HSvMuYtDMwhwGPyG0I-nMsZqrom2ykSsSZAgdfAd6Kd142VS-CwSm72C50T7aqqhmH_bBPc4ujcsHnTa6Co_V_43fOXPVr7AILNAWH-nM_OzQXVCSIXyDHYfpH4uRbR80pXY3_DVANpAai5GMJyNX7iBhfUYLC27LVSzHq7rWY__NousbLcQmwfEVNECzbmF_E2LJaIW4vBkczi_s9sXIIGO3LWAVX4b3Bpl0_gaTOby-e5aMKCHqKxOIqbsq9bzxfsgzf29MX-C1iJUItWSytgSZVFylLCsf5EirdhXAyU-6c8DRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره بریتانیا:شاید بتوان بریتانیا را «جمهوری اسلامی بریتانیا» نامید.
کسی گفته بود که نخستین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
ما اطمینان حاصل می‌کنیم که مورد دیگری وجود نداشته باشد؛ می‌دانید، در ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69982" target="_blank">📅 14:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69979">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2XH_lCAApFhQXOZ-z3_3xipA7IYIKRSzal_7EmAh0LzYU5UDMwEqDKsg-QEPEB4ktFrlN19NvQ_NL203rDZbfdcNMpFN91AgiQKn50IVQZZZnuqrOF8spI4BoZAcWxWBBRM2QccNGu3kCKvMEKtC80OShu7K36x874Qs0Lg44RtOnF682L6ugVymyoPs1vgMdg8voJsw5h9J9koW9qGSbV4nTf8KaVoslgjL4F5PkSG0_vx4sj1-WEdXrTSxSAl6Bo7jfc6zE30FlX74BT73pK1JkydiqbpCMRSadFgTJjsuM4gEC-Mfzh_XgV11SnJx5RGfirqGiJuRwXnYTm5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohuBpCvW2IfxdCgC-w9-AVJdCsBA5ijutWN8yFScQu_OI01FnI9wGeo9IqKLHsK7qOTPC0EGix1TGYXvt2d8U2HpUBiK6brsJH98WfiDXf0FP3JqyW2KLV8HvWm5ZY-W0Hy6JG4OdIMA8HS8IU-JMNE42jWQBSJBMJ5M1F0CzQJ4CnaWsqQKUrqWumJNXplD7EdlkYWH7qv90nHhFYonW_iWTVQ0ToKdwQxmDPsvgQ7pXT0YCd_HKr9C7v2YvCSs0HBGtpMvJSOseGXsoiGhlytvcxHSyM8D17hQ_6iWynxMIQTAk5fHDg7HElmx_JtPNrvPlBjBZcOOXVBi2LRTeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=FXZuK87lSP5UOHyfAPKcx9tBsDhEU9xmK5zrucIAAJV2vHvPQKh1hZXodh87Etk3UKZFBm5tNKnqa5pDrEwz-EXwGCh5JCFDtXSpQQm3v2UpiTpFjyAZm1AibXPi-hjPOhTu381MNXa1uFoGTitxLDQgzdLFGOON8OpYK9RG0qvxzNnrYzBZ3-5wzGMAYRti4cW-cMYSdXjIG3DkAztvC3pbwxKtG7ADRZ9NGDqrt24eSUuWU4vDbVD4c8rgZPvRnTrf8ZwZWE483L8A1MYi4_HkoUcx1f6EFWXMB8w3NXzfzyj8dOf75O-ERAsCqMCbIGXFOA9JmOE08uS7jNoEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=FXZuK87lSP5UOHyfAPKcx9tBsDhEU9xmK5zrucIAAJV2vHvPQKh1hZXodh87Etk3UKZFBm5tNKnqa5pDrEwz-EXwGCh5JCFDtXSpQQm3v2UpiTpFjyAZm1AibXPi-hjPOhTu381MNXa1uFoGTitxLDQgzdLFGOON8OpYK9RG0qvxzNnrYzBZ3-5wzGMAYRti4cW-cMYSdXjIG3DkAztvC3pbwxKtG7ADRZ9NGDqrt24eSUuWU4vDbVD4c8rgZPvRnTrf8ZwZWE483L8A1MYi4_HkoUcx1f6EFWXMB8w3NXzfzyj8dOf75O-ERAsCqMCbIGXFOA9JmOE08uS7jNoEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
صحنه‌ زیبای خورشید گرفتگی که امروز در اسپانیا و آلمان رخ داد و لحظات زیبایی رو رقم زد:
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/69979" target="_blank">📅 14:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69978">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b397a0c033.mp4?token=qb7llvrpUDrA6QJml6vvbWWeVeRKtuqSa7guM8akvxvbVaCNNzJOudoEVVVundhar9YYAboimpQ3JpCY0uJgziBZyRBga9oFVmTMeEsqRSSdH8szifJjA8D6a7erEhBj00fTzoh4DuACWjWAEUOhsQS3Mj7tSALDHI9Ob-so0wsCO8RAoJEZoBChog8uhamcaVBMevuDGwNyoDy5knc_mQP7hMxuEBeuQ_fqCqXwKX3Bb0fIqoGiSrOjlOTa73FKoLpDGc3xm5TggQdwHCZErJDSFLF2z2_Q1ScP12AgaR3PofPdk4PkoanYZbCw659HFaM_eGSi99mmHKhZPeUcMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b397a0c033.mp4?token=qb7llvrpUDrA6QJml6vvbWWeVeRKtuqSa7guM8akvxvbVaCNNzJOudoEVVVundhar9YYAboimpQ3JpCY0uJgziBZyRBga9oFVmTMeEsqRSSdH8szifJjA8D6a7erEhBj00fTzoh4DuACWjWAEUOhsQS3Mj7tSALDHI9Ob-so0wsCO8RAoJEZoBChog8uhamcaVBMevuDGwNyoDy5knc_mQP7hMxuEBeuQ_fqCqXwKX3Bb0fIqoGiSrOjlOTa73FKoLpDGc3xm5TggQdwHCZErJDSFLF2z2_Q1ScP12AgaR3PofPdk4PkoanYZbCw659HFaM_eGSi99mmHKhZPeUcMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی اصفهان، چند تا مرد عرزشی، یه دختر تنها رو نیمه شب خفت میکنن گوشه دیوار، و اونو مورد آزار و اذیت قرار میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69978" target="_blank">📅 13:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69977">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo4kcRBf3Qs60g7rp_1Wx8oVop-L3e6x-AZLsxDaORlbNmAAZKO3BqxDGA10p_XCCI4QoIisti7scTv2NnMvRWRX54HB7IA6DmpJHgxLIyKZFo2cJ31OTexu9T-zIX7vWfY0y2uWwVGGjL64njN92NcXFxEp9YJgFTbQXgpotdvs7dbVkmCu6YZuh_gNTtoeN7AdfET1KQSunOe9tTHYt2ZMdFSgmA4TlABUNjdpc5rEzBBBOEjRct7lxiveZ9tjqLn4KprG9pePfy1HwhbNwYOqIWxREgi8264L6FaND9iSoLACblXRklt_PAUtQlHmIAu6XIu877ycmR-Wq50FqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
به گزارش نشریه "آتلانتیک"،
دونالد ترامپ، رئیس‌جمهور آمریکا، رویکرد خود را در قبال ایران تغییر داده و به سمت یک استراتژی "منتظر و مشاهده" حرکت می‌کند. او به طور فزاینده‌ای به تحریم‌های اقتصادی و محاصره دریایی توسط نیروی دریایی آمریکا متکی است تا تهران را تحت فشار قرار دهد و آن را به سمت مذاکره سوق دهد. این در حالی است که تهدیدات و حملات نظامی نتوانستند به پایان جنگ منجر شوند.
اسکات بَسِنت، وزیر خزانه‌داری، استدلال کرده است که تشدید تحریم‌ها می‌تواند در نهایت ایران را مجبور به سازش کند. در عین حال، کاهش ذخایر موشکی دفاعی آمریکا، گزینه‌های نظامی ترامپ را بیشتر محدود کرده است.
بَسِنت همچنین به ترامپ گفته است که تنگه هرمز ممکن است ظرف دو سال آینده اهمیت خود را تا حد زیادی از دست بدهد. او ادعا کرده است که تا 70 درصد از انرژی که در حال حاضر از این آبراه عبور می‌کند، می‌تواند در نهایت از طریق خطوط لوله زیرزمینی به مسیرهای دیگری هدایت شود.
در حال حاضر، دولت آمریکا بر این باور است که فشار اقتصادی مداوم می‌تواند به دستاوردهایی برسد که تاکنون اقدامات نظامی و دیپلماتیک نتوانسته‌اند به آن دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69977" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69976">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e944d4e8ac.mp4?token=GUum3lt-hCK498YdJrR5linZb4VrE3qCaaImzHtHDECHRwbWizjgMeKUNTq_viWOT5Q6uFGwwZMS7y1tAUcic8YSEo-fM6uGsc0hDDeXE_9UQE5UnoGnM1W6hhznqO7znBqn7OWEuoXsetm9qpRCMBQuQTqvRzhyuZpJB5lmG7uG_kw3uWatoOLeuRubPrbTjbuPHTEjYnI-yeia9sX4_UyQoipsMXR9oZhfxfxR6O-3kWP8XBhKFjd7priet4pX0RHtJyn-OlWNnjIdiA0kAX4Ej9AnlkhZBrAOTKyCIKQi2Jm4wBppNidnMHXdK0Jn1a8W-bqOUba-FkWsWhacVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e944d4e8ac.mp4?token=GUum3lt-hCK498YdJrR5linZb4VrE3qCaaImzHtHDECHRwbWizjgMeKUNTq_viWOT5Q6uFGwwZMS7y1tAUcic8YSEo-fM6uGsc0hDDeXE_9UQE5UnoGnM1W6hhznqO7znBqn7OWEuoXsetm9qpRCMBQuQTqvRzhyuZpJB5lmG7uG_kw3uWatoOLeuRubPrbTjbuPHTEjYnI-yeia9sX4_UyQoipsMXR9oZhfxfxR6O-3kWP8XBhKFjd7priet4pX0RHtJyn-OlWNnjIdiA0kAX4Ej9AnlkhZBrAOTKyCIKQi2Jm4wBppNidnMHXdK0Jn1a8W-bqOUba-FkWsWhacVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال های اخیر با ۵۰ هزار تومن چقدر گوشت قرمز میشد خرید؟
سال 1390 ؛ 5 کیلوگرم
سال 1395 ؛ 1.26 کیلوگرم
سال 1400 ؛ 355 گرم
سال 1404 ؛ 64 گرم
سال 1405 ؛ 28 گرم
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69976" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69975">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f12d9ffb23.mp4?token=YVQrQoVQT1VSxZlkESbUHbLjk2mCn3zPKEt7s3xWCdHoiEiYA9Sds3woyNxvRWWHlRZFSWw7fkQJzYQ6EWIB6yVB_qYJmIoXAq-txWV2qWwjLe16GxkhUJaJWWiw7mZdhrB6jVRMTEFG08Er13ORzI73lrQRG3PB-8beXQaUYmr8Z61hSSX1kpZJRAg0SbHxUuib7uuA_vudg9Y9gtHgNxSRMV_Io4Wb9wrzR3LMAHj1ckSc2rOlcD-XsQKr1QD28UmWvsb47RKv8g8-np2legCjLf8lhlmDC9nMpnoQBOnjdpCom0e2Gkm5S4C867nm1jNzbDPelINpiReGBvXTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f12d9ffb23.mp4?token=YVQrQoVQT1VSxZlkESbUHbLjk2mCn3zPKEt7s3xWCdHoiEiYA9Sds3woyNxvRWWHlRZFSWw7fkQJzYQ6EWIB6yVB_qYJmIoXAq-txWV2qWwjLe16GxkhUJaJWWiw7mZdhrB6jVRMTEFG08Er13ORzI73lrQRG3PB-8beXQaUYmr8Z61hSSX1kpZJRAg0SbHxUuib7uuA_vudg9Y9gtHgNxSRMV_Io4Wb9wrzR3LMAHj1ckSc2rOlcD-XsQKr1QD28UmWvsb47RKv8g8-np2legCjLf8lhlmDC9nMpnoQBOnjdpCom0e2Gkm5S4C867nm1jNzbDPelINpiReGBvXTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لعیا زنگنه، بازیگر:
سال ۱۳۷۴ که سریالِ «در پناه تو» در حال ساخت بود، آخوندا و مسئولین میگفتن که دخترا با زیبایی پارسا پیروزفر به فساد کشیده میشن و کارای بد میکنن!
برای همین دستور دادن با گریم زشت ترش کنن و آخرشم ۹۰ درصد سکانس ها رو حذف کردن!
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69975" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69974">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNcWq1hROnGpAF9ez7FfW8qUp1WJjVE-Etipqg0EYSX9Dlc32AEC75kUIL4MdZyzGjya_n1YO_VVptoPvOIhhzglvNNGwfhs4rngVUdCpq2AIlQo6gwXWug7mkCUfezJa6pycveJ07Pr5DHjPBGdarrZ0sU1N5JPGKR3NNY3gYGu1Z_PvZGHmLQw9uoShRPkndh6zqm29w_KnB_Iz_sy6uAMw35ltfr2zv-PbLHgIEj3OINNFSvOQsWsov6aXlwmnl5JkQuu8kfWRG1GmbfhHwcP6w-hFUb7OtavEEWd6wmrrE4t_qaEf72nHi9GFH3-U-7Qw8CNk_YjyFlC_4IkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
ایالات متحده مدت‌هاست که به دلیل ناکامی‌های اطلاعاتی، محاسبات نادرستی انجام داده است.
مثالی واضح: جنگ علیه ایران. حالا، یک محاسبه نادرست حتی بزرگ‌تر در مورد تنگه هرمز.
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باش.
الله بزرگ است، بزرگ‌تر از هر قدرتی روی زمین. ما به الله اعتماد داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69974" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69973">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69973" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/69973" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69972">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1IKHhLpFzB1JHO8qE-909b5SYVF5AvXvXH2ryqOlCl7JUxLq9CQvcr4cVwhu54TRvGP2FS8TTFnBPoGVWanOH_Z_DIkR3XEMEwFUbfrdLjQV-9AAOF0zHmJE4zDuHi8kRMx1ZPhP6l30H8m1tEm8HfbpA4jMKVEp62OG-XHJl69z84R_8gVEfVO_1BtEOB5q3Lox97V7toMJngitPakVJQ5z9ZEIiyHfKNgwf3wtbOkeWmcKWRFb1Nnix0nrc8nFMwDvBi_KryisRn-2GbhA95s1fWNqfXqgxNP9QQ9puXHjwxTUfePOBtF0BGaYBR7Sla4uC1gqgtYtSb0sIw2Ww.jpg" alt="photo" loading="lazy"/></div>
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
r22
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69972" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69971">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c4997c0d.mp4?token=QG9oCgz_7ES11IwRfq-8AcHzKGENjY0OyRjJUJtLxKGWTMbSKHYVq11rbj9GoHBIvE89E9k-BlYFwVzTTL9W8EjSkIKN4FW6JvydBMSr4W6YBz-AkSBqmBfTWtApQ07Hhz5hFKoCGPwNvfcELe-WNalQn6cHj2D9uGA4R_dWMVek4enaELqcE-fqrC9UQEyo30zzjpOiIhB7rl1ZqHxNbuN73NcjeOR7kR0I4d-1Ptg2Vv8oy8J7Wi-mXmx7o_544xBEhXriVkzol_UMlV0UWdVBguN2Z4xYx7IEbdtsR67YkPu_qYxCcC8iDev8ccsQI1k-LwgvSMv8wIWWZ3t5GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c4997c0d.mp4?token=QG9oCgz_7ES11IwRfq-8AcHzKGENjY0OyRjJUJtLxKGWTMbSKHYVq11rbj9GoHBIvE89E9k-BlYFwVzTTL9W8EjSkIKN4FW6JvydBMSr4W6YBz-AkSBqmBfTWtApQ07Hhz5hFKoCGPwNvfcELe-WNalQn6cHj2D9uGA4R_dWMVek4enaELqcE-fqrC9UQEyo30zzjpOiIhB7rl1ZqHxNbuN73NcjeOR7kR0I4d-1Ptg2Vv8oy8J7Wi-mXmx7o_544xBEhXriVkzol_UMlV0UWdVBguN2Z4xYx7IEbdtsR67YkPu_qYxCcC8iDev8ccsQI1k-LwgvSMv8wIWWZ3t5GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی کره شمالی اینترنت قطعه و مردم فکر میکنن رهبرشون خودش میره با قطار براشون غذا میاره و تیم ملی فوتبالشونم هر دوره قهرمان جام جهانی میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69971" target="_blank">📅 11:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69970">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXL0olgyLijSdR2lRWFJZG3JG_H_gw1qd32CzqsTUZK4FAvD22ke72iucugPltPUkhvKCXqPsSEyR0a9HRMv89d43VIFyrAORnYBiYQu36Xxj6np0JnK0rfrIdkG9UZMQR0SR9MboqIM0mc-h_hYEke_xTOQv_yaKaQXZzEUpkyE397PBCeat-Uhqzbifc4ec2t_tGpkZ9gzbLdX_Aa0GbMWklCom3iVPWfG8nXwwE8vV1xwqINect8vVaLF2JSNZOeSuX79pULxpPq2Zdfv_YilePHnZdduQlMba8G5nZ599d11mvJ0O07mmPtEBNFD6Txy5pO71X9xJkvBZBG8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نشریه گاردین: چندین ملوان حاضر در ناو جنگی "آبراهام لینکلن" تلاش کرده‌اند تا از عرشه به دریا بپرند، زیرا خدمه این ناو با فشارهای روانی فزاینده‌ای در طول این ماموریت طولانی که برای پشتیبانی از عملیات‌ها علیه ایران انجام می‌شود، مواجه هستند.
حدود ۵۰۰۰ ملوان و تفنگدار دریایی حاضر در این ناو، در ماه نهم حضور خود در دریا هستند و رکورد ۲۵۰ روز متوالی بدون توقف در خشکی را ثبت کرده‌اند. خانواده‌های این افراد نگرانی‌هایی را در مورد فرسودگی شدید، شرایط زندگی رو به وخامت و حمایت ناکافی در داخل این ناو ابراز کرده‌اند.
گزارش‌ها حاکی از وجود مشکلاتی مانند سرویس‌های بهداشتی کپک‌زده، توالت‌های خراب و امکانات شستشو، کمبود آب گرم و محصولات بهداشتی اولیه، و محدودیت در تنوع غذایی است.
چندین تلاش برای خودکشی در این ناو جنگی خنثی شده است. یکی از همسران گفت که شوهرش پس از تمدید مکرر ماموریت دریایی خود، تلاش کرده است تا از عرشه به دریا بپرد و افزود: "او می‌ترسد." او پس از اینکه شوهرش از عرشه به دریا پرید، با او تماس گرفت، اما از آن زمان تا کنون هیچ تماسی از طرف نیروی دریایی نداشته است.
در یکی از حوادث متعدد، یک ملوان که در حال نگهبانی بود، متوجه شد که یکی از همکارانش قصد دارد از عرشه به دریا بپرد و با مداخله، او را به عقب کشید. در حادثه دیگری، نگهبانان از پرش یک عضو خدمه از عرشه جلوگیری کردند.
این ناو جنگی در اصل در نوامبر ۲۰۲۵ برای انجام عملیات در اقیانوس آرام اعزام شد، اما پس از آغاز جنگ با ایران، مسیر آن به سمت خاورمیانه تغییر یافت و زمان بازگشت برنامه‌ریزی شده آن بارها به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69970" target="_blank">📅 11:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a118468ed9.mp4?token=ndCl6IIdu8BlcU07A_fqpR8lN0EOxBUSzG0bznwSsQTzy4c-bTfEjr7yWTxqZa4xD22e5C4UBbBMujhPUHiKurY1ydoEMs5ikPp31vGMKKortWvkEzhV84dfoDwIt3r1T6SmQ1C5Gj1Sp6GeZhHrO4Rx5PL-EpZz8c76CI6xP87wnWbeAzNnZf8kTlSzr6ML_6WnSm3uqQ-gk9PsF4cQM3zsB09Dl3UVZJWiw-cDNMdZfWByfsyvfcTUvjSk3Dym0f56YeVKn9jeG9WJ8RnMT7kEJHkr18ZlVX7Mcltnff-2OMpJLT-W3NZOIslnRfrMwDuWT8CzfM7teU7Wq0MEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a118468ed9.mp4?token=ndCl6IIdu8BlcU07A_fqpR8lN0EOxBUSzG0bznwSsQTzy4c-bTfEjr7yWTxqZa4xD22e5C4UBbBMujhPUHiKurY1ydoEMs5ikPp31vGMKKortWvkEzhV84dfoDwIt3r1T6SmQ1C5Gj1Sp6GeZhHrO4Rx5PL-EpZz8c76CI6xP87wnWbeAzNnZf8kTlSzr6ML_6WnSm3uqQ-gk9PsF4cQM3zsB09Dl3UVZJWiw-cDNMdZfWByfsyvfcTUvjSk3Dym0f56YeVKn9jeG9WJ8RnMT7kEJHkr18ZlVX7Mcltnff-2OMpJLT-W3NZOIslnRfrMwDuWT8CzfM7teU7Wq0MEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستانی از زبان یه دانشجو-معلم در زمان پهلوی، که برای اینکه مخارج تحصیلش رو بده، شب‌ها مسافرکشی میکرده، تا اینکه به محمدرضا شاه برخورد میکنه و...
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69969" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69968">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=IU-KL0qoe2_-7fRmDHXSVQG89vVSqSmZJUDoeX5_Tv6v8CTfG9EJUsuz4aLdoPHPawPPfNc9RRgCOVvn6uqoX3PS-j_6q4MeFsnROzzGAFQoN4817d6lxd98680S69ie7bczhQFWRW9tz7kl47TEzngqHHiE0QdXU8-mQC5twSjy8bwdfOWCCStPLyMurg3ZD1XAoAxNgV24HMGVDyle-ade96MQuT-ro9Ojy5rkNg_x-h-d9Gxsw6IZxxB_Hof5tQggkCNi4n35pCdqlQsHZPXgZa0c9Y-A2N948g5ftQJGkbf5MNkCP34ze4VvwxLNl2rwjpwieTtJdQwo1q4u5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=IU-KL0qoe2_-7fRmDHXSVQG89vVSqSmZJUDoeX5_Tv6v8CTfG9EJUsuz4aLdoPHPawPPfNc9RRgCOVvn6uqoX3PS-j_6q4MeFsnROzzGAFQoN4817d6lxd98680S69ie7bczhQFWRW9tz7kl47TEzngqHHiE0QdXU8-mQC5twSjy8bwdfOWCCStPLyMurg3ZD1XAoAxNgV24HMGVDyle-ade96MQuT-ro9Ojy5rkNg_x-h-d9Gxsw6IZxxB_Hof5tQggkCNi4n35pCdqlQsHZPXgZa0c9Y-A2N948g5ftQJGkbf5MNkCP34ze4VvwxLNl2rwjpwieTtJdQwo1q4u5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زاکانی:
موشک دقیقا خورد تو خونه مجتبی خامنه‌ای. زنش که معلم بوده اون روز سردرد داشته نرفته مدرسه که اونم شهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69968" target="_blank">📅 10:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69967">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcec26005.mp4?token=dLXA4XCQPFKob_d-SUGq72llxlkz6UvmqcaDCGLV5SAfY1zairf3vme_HH5VjhCu8EV_RQjaCHCTElbFSOW1m0pwxTmPOgD1H-Rdxey10_tMGujFrYsLVKpgznYFyL9axVkDS1SYKYUP_01mEe8caWWePKNsGFrPyBBu23fMMr5v1wT9oQjjSQiYaci3E1S-rUFK-k1GcWJ6U7fhAFEbN4l3QiJgUwc4tkkOdM19aTVx8JY7vpXga9fIk1Lei8fH-xmKIelPDBf7Mu8EBMBBIbpUCEBpBS0fdh2kNE7yMlzPbfzL_h1SQEFCLDxN8eJrXcDYT5RBySU8J5RkRH0MPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcec26005.mp4?token=dLXA4XCQPFKob_d-SUGq72llxlkz6UvmqcaDCGLV5SAfY1zairf3vme_HH5VjhCu8EV_RQjaCHCTElbFSOW1m0pwxTmPOgD1H-Rdxey10_tMGujFrYsLVKpgznYFyL9axVkDS1SYKYUP_01mEe8caWWePKNsGFrPyBBu23fMMr5v1wT9oQjjSQiYaci3E1S-rUFK-k1GcWJ6U7fhAFEbN4l3QiJgUwc4tkkOdM19aTVx8JY7vpXga9fIk1Lei8fH-xmKIelPDBf7Mu8EBMBBIbpUCEBpBS0fdh2kNE7yMlzPbfzL_h1SQEFCLDxN8eJrXcDYT5RBySU8J5RkRH0MPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید فک کنید هوش مصنوعیه ولی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69967" target="_blank">📅 09:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69966">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39fe0991d.mp4?token=DwBxCnhSIWFuYYMaRtl4vj6GMDuWjtJdf0uEttd-Kf4iYPJeyLDpDoz4Qepj-t2PFq-YrFxNUJ1FrRJ2lY2WBiPt4l4-EP6V0yscAYvXrRbV8uiqk_YshoZ-ROIMsY_9d8HJ2oKPc3g3hv-AogQNPXDVTUdfQZeAu0GhTj1TTSDaHeeJAlnK6KlRsmrx8dwfbW4LAdFWK387pPSngayWqAcEC9gKombgxNFFj16d7aOOMj5e4N1w6WIDKgEEkGjPujWARXYpTb-o1i0GhWDPFufA_OzWJs254VW6a-JSjWQCxYEkZg90BBiD6oC2RN7_5jMSb7ahfDFxhB-BK8m-3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39fe0991d.mp4?token=DwBxCnhSIWFuYYMaRtl4vj6GMDuWjtJdf0uEttd-Kf4iYPJeyLDpDoz4Qepj-t2PFq-YrFxNUJ1FrRJ2lY2WBiPt4l4-EP6V0yscAYvXrRbV8uiqk_YshoZ-ROIMsY_9d8HJ2oKPc3g3hv-AogQNPXDVTUdfQZeAu0GhTj1TTSDaHeeJAlnK6KlRsmrx8dwfbW4LAdFWK387pPSngayWqAcEC9gKombgxNFFj16d7aOOMj5e4N1w6WIDKgEEkGjPujWARXYpTb-o1i0GhWDPFufA_OzWJs254VW6a-JSjWQCxYEkZg90BBiD6oC2RN7_5jMSb7ahfDFxhB-BK8m-3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های داخلی با انتشار این پست اعلام کردن که کامنت گذاشتن و لایک کردن پستای رضا پهلوی و اینترنشنال و... جرمه و کسایی که اینکارو بکنن دستگیر میشن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69966" target="_blank">📅 09:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69965">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69965" target="_blank">📅 01:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Tl919HmpdevcSjh2xs8RwfrLPgIVl8fZ8cCkW_c8MlOQGmjNEHqwMGEEYUb3RmzQLXNOTyxA0DZXwYrIbGE7clEl3nI8WpN1jXibMnbSFqgN-EkMmRb8tCMIap-92qh6kTz1i9aYw774bTDYEunE005l7BxTOfGCcuaXgEs57GIe6P9fz9xUWVpMEKTRmEdVV2DgQngZwO7uKcc9t55Dfd4CZLtHSR6-_AX82a8JDCuSYrEYw83YqkUDlvXNg4Un1MFzzkVwYTP4Y4cQHbKtrpbSQbPUvxPTjupwfqXuH0CL6k8cL55JGuL8dXGQn-yUbwSE0JiYv7gS0WXBWbk8pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Tl919HmpdevcSjh2xs8RwfrLPgIVl8fZ8cCkW_c8MlOQGmjNEHqwMGEEYUb3RmzQLXNOTyxA0DZXwYrIbGE7clEl3nI8WpN1jXibMnbSFqgN-EkMmRb8tCMIap-92qh6kTz1i9aYw774bTDYEunE005l7BxTOfGCcuaXgEs57GIe6P9fz9xUWVpMEKTRmEdVV2DgQngZwO7uKcc9t55Dfd4CZLtHSR6-_AX82a8JDCuSYrEYw83YqkUDlvXNg4Un1MFzzkVwYTP4Y4cQHbKtrpbSQbPUvxPTjupwfqXuH0CL6k8cL55JGuL8dXGQn-yUbwSE0JiYv7gS0WXBWbk8pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a21
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69964" target="_blank">📅 01:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69963">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=WPiTORhrrej3zwQVMCg4OC9IrnkcyHVouNc77EbF_fo9CQaO_ywvDgV9v_IzlHl6-ZQa5FaknncmvmnixS17oC9A35eQ83-uvNn4Rg8Bb0ZlA136KnyqrMKOIlNQyt4bZiQ7W_cpTifGdYP38_w3MBG_K-0tVou0So3cEbHYf0org-WYfFV-N0XQH74IiOdd94ybTjBE_JHeqoXC_bbnKTz6DS3xRAhenKdLzIWf5LawV2GLAntKby0idQj1_u1sI-K9wmR4-HQceCV2OZA26bLDflMUeHVeVIBrlPDKqI31GeX8ATsn0M3bjqbvXHiN4VdczjhnaxZWv_pTFsQXNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=WPiTORhrrej3zwQVMCg4OC9IrnkcyHVouNc77EbF_fo9CQaO_ywvDgV9v_IzlHl6-ZQa5FaknncmvmnixS17oC9A35eQ83-uvNn4Rg8Bb0ZlA136KnyqrMKOIlNQyt4bZiQ7W_cpTifGdYP38_w3MBG_K-0tVou0So3cEbHYf0org-WYfFV-N0XQH74IiOdd94ybTjBE_JHeqoXC_bbnKTz6DS3xRAhenKdLzIWf5LawV2GLAntKby0idQj1_u1sI-K9wmR4-HQceCV2OZA26bLDflMUeHVeVIBrlPDKqI31GeX8ATsn0M3bjqbvXHiN4VdczjhnaxZWv_pTFsQXNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنر نصب شده در تهران:
پزشکیان راستشو بگو، مجتبی دیگه نیست و فقط وحیدی بهت دستور میده؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69963" target="_blank">📅 01:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69962">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
#فوری
؛خبرگزاری فارس:توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان
مدیر شرکت پخش فراورده های نفتی کرمان: پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
تا اطلاع ثانوی، فرآیند عرضۀ بنزین در جایگاه‌های سوخت استان مطابق روال پیشین ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69962" target="_blank">📅 00:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69961">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184379545b.mp4?token=LmUdyhspnOp7Fj2vuZwvEPXesW6ONTzsNvJySy833ZGhrt-GCoeEvK5vBZ4KtHBkOIofTaqrSVtm50imqK4-Yk5cmTKAKrin3dbfWMAN5peKkMNZsQdTPnKsT2tK8rTTUmYBLLOJG2lixkUL7i9rf6768R3Vt7sPt5NZwfheVzIKkBiuWtV95eUPA-F9g36aLvH72TdMpevcGy6mdmoeaT-ln1Bmo4CKJ4s_XML0-T4VoNW1fLiLDoUFu6vKmEMM33t8TSPvOvW5ZOB1FRkQx5vnLhyih0huMZ6bM1FQyf5yzL3WMyoEA0LstEP3g35r6y2hFlAwOML3awF2ZqB74Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184379545b.mp4?token=LmUdyhspnOp7Fj2vuZwvEPXesW6ONTzsNvJySy833ZGhrt-GCoeEvK5vBZ4KtHBkOIofTaqrSVtm50imqK4-Yk5cmTKAKrin3dbfWMAN5peKkMNZsQdTPnKsT2tK8rTTUmYBLLOJG2lixkUL7i9rf6768R3Vt7sPt5NZwfheVzIKkBiuWtV95eUPA-F9g36aLvH72TdMpevcGy6mdmoeaT-ln1Bmo4CKJ4s_XML0-T4VoNW1fLiLDoUFu6vKmEMM33t8TSPvOvW5ZOB1FRkQx5vnLhyih0huMZ6bM1FQyf5yzL3WMyoEA0LstEP3g35r6y2hFlAwOML3awF2ZqB74Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خانعلی زاده کارشناس صداوسیما:
افزایش نرخ بنزین و گازوئیل بالای ۵۰ درصد مردم آمریکا رو شوکه کرده
زندگی اونا فیکس هس یعنی پس انداز ندارن وقتی بنزین یهویی از ۵۰ دلار میشه ۱۵۰ دلار ورشکست میشن
مردم آمریکا مجبور شده ماشینش رو بفروشه خونه اش رو بفروشه بی خانمان شدن از گرونی
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69961" target="_blank">📅 00:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69959">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7326381213.mp4?token=U7H5Xht-PnTp3Umq-AMJjDWJUq_mW3_thv8COUbam8cjdDYzRFi3JKzrrtyFei4PdF2sfdPQLF34_CX4fdzd6CJwcHyAfUUVVXtRI005z-Og2EgF9TvFyTOPqSvt3KOo74w9ONlbteGlwq8lcBR6NDhsYeLebeyXDSszDME2Abv4xt0RcG_0fZJJNYH9et796-5oFEm1qzODVLpMuuPC0qocwWL6faZjez1GWyvKK8pQ-TiEZcKuCT9mjXJ6Su_rzCDovqUL602mDtkdRAIgvC4hltPrEzCClLlSdRfaiMWW7ghLG5eov57_Y9tKqS0xW-Uzw6j2sHiWD2QuuFDTgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7326381213.mp4?token=U7H5Xht-PnTp3Umq-AMJjDWJUq_mW3_thv8COUbam8cjdDYzRFi3JKzrrtyFei4PdF2sfdPQLF34_CX4fdzd6CJwcHyAfUUVVXtRI005z-Og2EgF9TvFyTOPqSvt3KOo74w9ONlbteGlwq8lcBR6NDhsYeLebeyXDSszDME2Abv4xt0RcG_0fZJJNYH9et796-5oFEm1qzODVLpMuuPC0qocwWL6faZjez1GWyvKK8pQ-TiEZcKuCT9mjXJ6Su_rzCDovqUL602mDtkdRAIgvC4hltPrEzCClLlSdRfaiMWW7ghLG5eov57_Y9tKqS0xW-Uzw6j2sHiWD2QuuFDTgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🌓
لحظه زیبای خورشید گرفتگی در اسپانیا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69959" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69957">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAh2tS-sz56dnkjvHkpL9hHqJFLIPT-u1CPbemsg1M40dQD3KwnJ1lxcnXPhOnldFNnlwkoVXXplMgXFueJ6Wu8X7AtUJgKWhqQvJ7sPNKD74t-1C7XdV6_FBzvc0FzdKW3jTqlrvCcH4f4Y3uBhbm-B0aArj-3rejnW_dRSO35U6VfgLaOG96F48CYjCThSOqCklVExlkMGBdQHB7Kh0dv6gRYzT0Qb58clHrIp5TGY5fNUYdCH76mgBXorn5I5Zi0O78cKuVHchLfbOog_B35D0AmzJdkCoE8vpP8es2CbviAhMYgHCacy4FlI-tEK7mnMlRMlnG0rhLflQLrOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJ05E4FoG7NDRIKeIt35T5jI3z9lBXWw4gbLeHPMS9AFwt-y1YXKZRBxsHncMr5xsFW0tljJN4kPD9VZpFdO5rVNwIOP2azOYjxPrBcNQoxdHLQDp8eik5mqGZZyHARLc9M7x9NwNGJc_iBMJhlkNdwKDlk7HJYIrRgYq9AFQvaU331dbJJhD8UwaaNCHanvThKgnERjs9xTmGpe1HUaIVgMkO_na9K34kIabeOBpMtDpTmtjp8twfCERFuqUk-eZ5zIJCkH2e0V5-xM2gb6OEs821GYrVJmEaFr_uVIewh7P6zVM97c7opnl2Ds1khQWFjIcEQ19RzM4GFcJSNmhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇺🇸
🇺🇸
با اعلام ترامپ کارولین لیویت سخنگوی سفید کاخ سفید این ماه بازنشسته میشه تا با خونواده و بچه هاش وقت بیشتری بگذرونه
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69957" target="_blank">📅 23:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69954">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUK5bGKadc4ZMBNZFZshFSYrhTm8_g2AI8lbYYj1dNr5ksKgPVDr3Kv7HlSEfm2xcbjepuXrNFOp72BfTWwy2FqLNo95TRrUif5M9LnLjrJZ9bDHh7j5zEtfqHoYoaZw1MyXnVTEsvisLovdjSL9U4xm1aIAm7jOjVFPfb5WQJnl9zxEJPe28iYYgjFIU6_ykOjmmFa5d3a4H7dCrMkStKZsXc_5C3zna-LtOk3g6FRBTRUm35a4zfvjTAsRvuKV6AifHzaIRQJTT-Qd0hAX0d0M8-sFH0llxpLk2tdVc62eW8eLsdFOA4utzgAo3cpwNADBJMuCSDWd2QT0BhBtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRo7CbM-x3BVMB12PAsnV56yLGG_RGYxxEFHJd-xMeLR1-uOWZzn68MbGfM_6R3r-CtSKbfZtDkh08wg85Px_JiG9DFkplKvfaCrIZoktvPV7KQPEzgWlfp6mmVn9rY3PRuQQIrqrD8cFDRYJryTGbdSLJVjZeF0LTq7A05Z34hWsNPC-2Nzci2m3LsVxI0muob3Xsiwbh15Zb1FfMLGqSGhDTDTOKe-ud5LXZHV7GvkBYxgnt51IbaQbGV9SGYGcZcbWZFDIRBDHRxl4avZGmuEf6BffAg1U2q7Y7Jfr-JHEZn2qQkkie3sizE1aXx9X9NIxCEOTxbhdkDGz8JPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOaD_AkkMhUwgvfF1sR-CqQYqCRkLDOTIa6iFx7jSsMTT5P7hIeoKvbMvzt2DgaLVovQDpyt7Wq9hIsGupLCCdENeqe9GXyfZfzB574-jo_9exCeQCeYhR3qqritwHBrFFY0Msr9wQBT9yZ18oUJ8zyMXwp_G7P9sVS4OUtcoR_PyUt9iYpVIlbExXEGiKVqkKL2ps1raWj2UzAIIZCnUqsE3CGOSe4bGsWDIClrHYMDM_8sTvYnGWW5x0p6S1-vE95bBI6PYgADbxvO8FTEbKoAyAWGNF8ltAtLow2EO6Z52-_YOTblhsiTjkMAQrmz3qmhlGQwX8DEiFTNqLcYsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69954" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69953">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LW2_BQ7qgc3DhRGumID3RJ1PHXXWov_cZpJ2URPQWnnST-5icDSevcO9Ha_PzLSKDF8BO3egInYGMgTTdce2gXg9szK3t7PkBkSU2fOWhtZN54-C59zP1D2GW2V3DPI8FpFGlzi9mFSB4A4nOFfwGlyqLdTr2qe1RMLLaaNjsFh6mPx10mYUX2FyWDDm8ee--_adNm2AlbQ3tc4ZycHLUb3Q9R32FbJOZD8tEWViB0R_MI_iKiKSEDzn-74OnHl4BOWwzllSVnBicKnbrWyo1nS2gZzCi8_9P9ubqPSkl-1dk66bjYpOHewvDZqv26CJ-VCRxk5jUfG7rQYKgHiOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
یه اکانت تو ایکس:
ایلان ماسک باید بریتانیا رو بخره و آزادی بیان رو به اونجا بیاره.
🏴
ایلان ماسک خیلی جدی:
[بریتانیا] چند
؟
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69953" target="_blank">📅 23:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69952">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر منتشر شده، مجموعه‌ای از حملات هوایی انجام‌شده توسط نیروی هوایی و پدافند هوایی روسیه (VKS) را نشان می‌دهند، که به شرح زیر است:
• پنج بمب FAB-500 علیه یک پایگاه نظامی ارتش اوکراین در منطقه نووژوینکا، استان خارکف؛
• چهار بمب FAB-500 علیه یک گذرگاه خاکی در منطقه مایاکی، استان دونتسک؛
• پنج بمب FAB-500 علیه یک پایگاه موقت نیروهای گارد ملی اوکراین (NGU) در شهر دوبروپیلیه، استان دونتسک.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69952" target="_blank">📅 22:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69951">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69951" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69950">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LleA7F26tngJJsXT4NO8V0CQToxfh70C-i0oC3y7rrpSwip0BcuFCGLFBu5LlfyDnTRReLnRH7trLPYCSlW6nwqvd4JlfGwIVkg8J1vLdCdD_VexHWjIZXpJRLdJoZ3CfIiHebI1zXsi3hC5uIaPxkistUZrLKT7F1QL0D4mxqzo0rH5V17X21KhBsdDHNGys-_5fnoODCNlQHL_nPZ8OGqrIdvwD_ppEI3-UklbiHgfZY3TKTOnHcnyWIfzCqAuMDQMvYfXtG4exSm_O4lS_zLvLvVlI0S9YTpPn0QGoqv049HHZ5zYLT2d-Q8vp0RTQhXYLhQbY0Q8AfVmmTR4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69950" target="_blank">📅 20:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69949">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=CjRTLuhLMTfBpjdhhbpFaoYOzVe54GGIP3dF-KyOV0DFn4VhqHjUa2HxP9uK82ERv8rv8R-raFTyOTV0fGsNaWM82UgdOtFThKrAauRObhXEGT30mECjzhb74sdR00TcUyFDj2RIyrmWZ98KhhNBhDyRIisYRG6QdSyp8ffuQp9ydTvMIzpfV2qZdcrHUzbwhI0XnUMNCyvUcujgY_rj6T9YNJfyFX9D3hZ_4hoLGpoFXB9fcZq7oOCb-ShoqlO-zD_5DEgiJLtjavG7qi8nQSGWsu5rLKHe23y7FlR2PGkUsQDA6jvsM3Uh3YUukuH6mVxVovyrSNkf2Rt_Nf1rEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=CjRTLuhLMTfBpjdhhbpFaoYOzVe54GGIP3dF-KyOV0DFn4VhqHjUa2HxP9uK82ERv8rv8R-raFTyOTV0fGsNaWM82UgdOtFThKrAauRObhXEGT30mECjzhb74sdR00TcUyFDj2RIyrmWZ98KhhNBhDyRIisYRG6QdSyp8ffuQp9ydTvMIzpfV2qZdcrHUzbwhI0XnUMNCyvUcujgY_rj6T9YNJfyFX9D3hZ_4hoLGpoFXB9fcZq7oOCb-ShoqlO-zD_5DEgiJLtjavG7qi8nQSGWsu5rLKHe23y7FlR2PGkUsQDA6jvsM3Uh3YUukuH6mVxVovyrSNkf2Rt_Nf1rEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمود احمدی‌نژاد درباره حسین طائب(شهریور1392)؛ «مشکل روحی روانی دارد»
ایشان [طائب] تعادل ندارد؛ همه مقامات کشور می‌دانند.
اصلاً کارش پرونده‌سازی است. از وزارت اطلاعات انداختنش بیرون چون دوبهم‌زنی می‌کرد. باید معلوم شود ایشان بر چه مبنایی در این کشور کار می‌کند.»
❌
حسین طائب به دستور مجتبی خامنه‌ای به فرماندهی بسیج گذاشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69949" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69948">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=uadUvIq8t0YjiADglF8ghWaodTdD6Tl2Hg_SjHM_sb0r4kE3aeN4ns7wFhYlTnOvXA2hEo0w-NDOpfHLEfSf2pgdI4lZCs2NU2pbsO8yDNCrQYLhBtwh_7DsHh8uws0PIYFJl4Epkoo6jdM2gETvayouo-V05WqFWTGYS_RaT-NjcNnVzClfj9JHbXu-jDr9HuS2AAkxLNsdUQzNxhgpohwYoukdGhHajvLuArxgUbzfbO-3-rZzc4XsY5YuUTdkTjFy5zsMP-3As7-tOSJj1QugvS35JUxhbEdOzXNrPVDepRY03FeglAlYNsGxUf2RADumbFZi1JVSkw8KjjsbXGWmiaZF6PAaT6Y6ElR2hxPHoLIpdYfFiy5NY6SXDOqd4H6L0stA-AWrq8HrP9YxaQdTW3b06pXiZvzrSxfdfhrNPKVERvK-4qVgEB-Ih7B5VQDhJdx6nW4H2TytJdzNc56nVUNDuVwhHAQRsAvO4zsdxlemavJ4sJBYbL81fUOvP_j8nCwACA_UkVLqBaEp4yrBeCaMLDM6lU_JRXlNxMrgDTSPqv9HhNvbFc5Ri9ylpw5pcAxbcwc1mwneVaEKaGDAWLp1xDA3UUyy58Rm8aZwdkPoKZQWsxTBEteFPQbTy5Ud3MvMROzDydcPpNxpoprlgh_bQHPcRj8JO5QkA60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=uadUvIq8t0YjiADglF8ghWaodTdD6Tl2Hg_SjHM_sb0r4kE3aeN4ns7wFhYlTnOvXA2hEo0w-NDOpfHLEfSf2pgdI4lZCs2NU2pbsO8yDNCrQYLhBtwh_7DsHh8uws0PIYFJl4Epkoo6jdM2gETvayouo-V05WqFWTGYS_RaT-NjcNnVzClfj9JHbXu-jDr9HuS2AAkxLNsdUQzNxhgpohwYoukdGhHajvLuArxgUbzfbO-3-rZzc4XsY5YuUTdkTjFy5zsMP-3As7-tOSJj1QugvS35JUxhbEdOzXNrPVDepRY03FeglAlYNsGxUf2RADumbFZi1JVSkw8KjjsbXGWmiaZF6PAaT6Y6ElR2hxPHoLIpdYfFiy5NY6SXDOqd4H6L0stA-AWrq8HrP9YxaQdTW3b06pXiZvzrSxfdfhrNPKVERvK-4qVgEB-Ih7B5VQDhJdx6nW4H2TytJdzNc56nVUNDuVwhHAQRsAvO4zsdxlemavJ4sJBYbL81fUOvP_j8nCwACA_UkVLqBaEp4yrBeCaMLDM6lU_JRXlNxMrgDTSPqv9HhNvbFc5Ri9ylpw5pcAxbcwc1mwneVaEKaGDAWLp1xDA3UUyy58Rm8aZwdkPoKZQWsxTBEteFPQbTy5Ud3MvMROzDydcPpNxpoprlgh_bQHPcRj8JO5QkA60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش شهروند اماراتی به شلیک به پرچم امارات توسط مجری صداوسیما در پخش زنده:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69948" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69947">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=qPAqOwmqoxJ1G8NHqWdeYZCe8z8earUTIwjfOvUji0U9lQHM-tkJgFeLhv9t9XwjtOLT5p5DwRFNzTAMYBphEoF9DBHe3AAZ9J6yvYdA9fyvlDbFIqOtmDZjvB_JICjyj7LQNHK4ZzhujblPSUV1O7AHnEVR2plRAgH_6FJrAj324J3e1UOrSUFn8rF7qZykYL6eEq5vxaWCmnETS5jEEUoOJnOrkwYpXjJUsH5DUnWnQM8xQdy3tlh1RTYX2w4QdP-34AJn6xA0rPxBQ-38FkXFUjdCvasNqgrVyrdSBFHZTjNB9THEb68OjAQaE67MEbK24lys_XikJ2Lc1Lxa8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=qPAqOwmqoxJ1G8NHqWdeYZCe8z8earUTIwjfOvUji0U9lQHM-tkJgFeLhv9t9XwjtOLT5p5DwRFNzTAMYBphEoF9DBHe3AAZ9J6yvYdA9fyvlDbFIqOtmDZjvB_JICjyj7LQNHK4ZzhujblPSUV1O7AHnEVR2plRAgH_6FJrAj324J3e1UOrSUFn8rF7qZykYL6eEq5vxaWCmnETS5jEEUoOJnOrkwYpXjJUsH5DUnWnQM8xQdy3tlh1RTYX2w4QdP-34AJn6xA0rPxBQ-38FkXFUjdCvasNqgrVyrdSBFHZTjNB9THEb68OjAQaE67MEbK24lys_XikJ2Lc1Lxa8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69947" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69946">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69946" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69945">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB25KsYC4G9KD3AV104U2UnXXDy4ABQxFpt3W89vUySqieLPSYlylfPp5GjYZVxkmuS143AXvzwkUVC0-grFSVW0ZaZl6ojN12cXTQpmQId0Yb_FiBZYFM6q3ixFuGKDdrpdwa50gDn3Di4yi4P36bYlQc6HPAFBwGj17cko_xF2NpFsr0txn2Yv8f7afEWZnBA_JgFNAjjPxlrH16O8QHPQuO5U5ULkRDFfFqGx7W_xm_-G93B1gQe_I-grqSwOMJE9dIydJmiAHNH4DqOnzDnMGT69VZjbsQDwFNAL2vkLNg5qzQTD3CvYpsuzh_LIFWDk_Lzha50igCrAPZM8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g21
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69945" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69944">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq-RTAoL-1WVNY_1Wzoxa-nbIYjUSsrm5eF_ONoC5NKlwpLqgbCiSCIyWtvCFx8pCQVnwG2qqLlAEijrUeVB8UDWqOIcO4MfX7r6h42SbwPbkFMoWH05lxrkVS6q5b-y2uOxN7UBBeiUtKU9V3Vt_MGfo4IhZ74T43jB9YPvyY1etkAxOWt2u6a6ATPxQmWO_hh6gWxi-A0ft9MLhyMvEdcZOQJL7sJncuDB-pRFEjKXDLGhBgNo2YsOleqFAxzLMd49ACpHZ4klKrMrzUZrRW26ba1tn4QD0ae1DtZZPkWltnTygqy46H9_WtyloK3rn5YZZd-ZqzT_MUkxIi1H2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
همه، محاصره دریایی ما را «دیواری از فولاد» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد.
آن‌ها نه نیروی دریایی دارند و نه نیروی هوایی؛ سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران درهم‌شکسته و در حال فرار است و وضعیت «رهبری» آن‌ها در بهترین حالت، نامعلوم است!
آن‌ها پولی ندارند؛ کشورشان «از هم پاشیده» است. تنها چیزی که دارند «اخبار جعلی» و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر هم می‌شود!
ایران فقط حرف است و عمل ندارد؛
دیگر خبری از آن قلدرِ خاورمیانه نیست.
ستایش از آنِ خداست!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69944" target="_blank">📅 18:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69943">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=hZFDnJASfVNJztuyP1NYz9DwQIrPZ7JyW2m-RAo4dop-7L4aGftalBm72Bs_b0Q7IQaszbVvCycAqXYMwhzZyHBp9bZKb8nF_kR0UA18WL_O6uaklGXV5lXO1fECGlCbTxDbLcW6jOY3qyoNeTvlHnJtmL4zH8C5FN8X1oCoRfPshEdatA1BLPV3pVQlDcppYILQnC1nANvco3zq-tLya7c4B_B5rN6_4O0vKUxZgwMHvp-SCTqpBBMU_gmImnhySLqlcrsKFblzUymXCV6TZtGX_py5_lMAAuwHnSxjd34NtoW_yXx_2h8QyXUtuaNgeI3U4Ntd2CINFTb3X6BQMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=hZFDnJASfVNJztuyP1NYz9DwQIrPZ7JyW2m-RAo4dop-7L4aGftalBm72Bs_b0Q7IQaszbVvCycAqXYMwhzZyHBp9bZKb8nF_kR0UA18WL_O6uaklGXV5lXO1fECGlCbTxDbLcW6jOY3qyoNeTvlHnJtmL4zH8C5FN8X1oCoRfPshEdatA1BLPV3pVQlDcppYILQnC1nANvco3zq-tLya7c4B_B5rN6_4O0vKUxZgwMHvp-SCTqpBBMU_gmImnhySLqlcrsKFblzUymXCV6TZtGX_py5_lMAAuwHnSxjd34NtoW_yXx_2h8QyXUtuaNgeI3U4Ntd2CINFTb3X6BQMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
روایت دختری که در 13سالگی به همراه مادرش از کره شمالی فرار کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69943" target="_blank">📅 18:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69942">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=U8eSdcOVOjKkTzG9Iuo6i-Z7YBRlxS6uccLvB2CwhewrK-1HUS7xGJRt4Z8Sp7-oWBZs4do4tQ55oexjcskZSh52FrRyc6dJM6PPU7uOV-3PRWzMsBjNUdah290CPegalnf88YIizZOCyQjM0lKsGUB8SC0IKyvF_N10lXU2UjbYdaGbx8PuFuhmVG5y3HM_9hYTFKLVq5tYItcT26jaJZBi-d9aNh5eV47gLTt9_9293xnK_RRwdSF8vKZKpB-3fh45sZeLwTsAkeeAPGtWNjUOvwDok_qXzf5T8plBLiHamziYnnU4C4-_jcbfDt4PXUVCBdJdrhb6WjrRWtkkNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=U8eSdcOVOjKkTzG9Iuo6i-Z7YBRlxS6uccLvB2CwhewrK-1HUS7xGJRt4Z8Sp7-oWBZs4do4tQ55oexjcskZSh52FrRyc6dJM6PPU7uOV-3PRWzMsBjNUdah290CPegalnf88YIizZOCyQjM0lKsGUB8SC0IKyvF_N10lXU2UjbYdaGbx8PuFuhmVG5y3HM_9hYTFKLVq5tYItcT26jaJZBi-d9aNh5eV47gLTt9_9293xnK_RRwdSF8vKZKpB-3fh45sZeLwTsAkeeAPGtWNjUOvwDok_qXzf5T8plBLiHamziYnnU4C4-_jcbfDt4PXUVCBdJdrhb6WjrRWtkkNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه روش فوق العاده برا تقلب در صورت آموزش تصویری
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69942" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69941">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⏸
صحبتای یه فرد رندوم:
سوال من اینه؛ چرا بعد جنگ 12 روزه خبری از این تجمع‌های شبانه نبود، ولی بعد جنگ 40 روزه شروع شد؟ دشمن که همونه؛ پس چی عوض شده؟
دلیل این تجمعات شبانه مخالفای داخلی‌ان یعنی مردم خودمون؛
مخالفای حکومت هم مردم همین کشورن، وطن‌فروش نیستن. ممکنه با حکومت مشکل داشته باشن یا طرفدار یه مدل دیگه حکومت باشن؛ خب حق دارن نظر خودشونو داشته باشن.
اگه واقعاً می‌خوایم بدونیم مردم چی می‌خوان، یه رفراندوم برگزار بشه تا نظر اکثریت مشخص بشه.
سال 57 یکی از اعتراض‌ها این بود که مردم آزادی بیان ندارن و مخالفا سرکوب میشن، اگه الانم مخالف نتونه حرفشو بزنه، پس دقیقاً چی تغییر کرده؟ مخصوصاً وقتی وضعیت اقتصاد، روابط خارجی و خیلی چیزای دیگه هم بدتر شده.
در نهایت هر ایرانی می‌تونه کشورشو دوست داشته باشه، ولی در عین حال منتقد یا مخالف حکومت هم باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69941" target="_blank">📅 17:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69940">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udNMu-fqzEs6Ts3Hs9NMmqACBBHTPjMkil_TEEO6ihCQK-JEvfG6unTtCHo5l31vtdwV1nNWCTF9WMjwnQoqsHa7jc_4VTncWiTzZ7mSr3qesSBv_HsoF4WolAqlwQTsDsbFnwRnqcY6s5MctQkpQacrXii8LKqdBqWvbBXJjrPd1rOEClRyiqtdfbb-fQz9sVMITCi4d8MBC1a2Y-IpSNj7xKq04_Zwe9T5BRKOEPCMT4AIcTtoNMUN8CryGJdJR1B8p5PD5sSnygFDrzcn95Ln1hwQho2g9mAPmQL5_Alo6tpfLf3Aol3ugvsU2zlO9wuPLTsmvaEWbPvtlt4c2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا، یه آخوند به اسم  "شیخ ‌احمد " چنل آموزشی با موضوع مقابله با غریزه جنسی فرزندان راه انداخته
😶
مادری که پسر جوان تو خونه داره، نباید با آرایش و لباس آزاد تو خونه راه بره، باید چادر بپوشه چون باعث تحریک شدن فرزند و راست شدن شومبول وی میشود!
همچنین پدر نباید با شورت جلوی فرزند دخترش راه بره، باید حیا داشته باشید.
پدر مادرا جلو فرزندانشون همو بغل نکنن، وگرنه میرن جهنم
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69940" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69939">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oFk3SLm1P3IiPkCLw7RtL6LoTzrjq7Q9vekMiVjc1_OH52gZ7D5tjyvniHHuh68ERVF-l39A8j1C9ZGRXi9D7yH2MvSSOwhRqIYYATItuP7bLyzpng9vDsqx_RDeZljVAaItas7bABXG-jlglOxXoG4K0IKxND4IWn4f78QNQyOnRO2bJ5OgK9ALhQehnmYst3OhuWKsCMJctYLxMoXUygv3uI0UgJJcslDa2YswIHHXyhBUQT4hdiLxQ5RdXVAudGJdxyp_oqNiYsJv8qH4QNt3VEWORBKsZTUVHPC6C8UZCvUt481DgJ7IB9qH3LiQ67UsOf7mo4vk1wCVB3d3KY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oFk3SLm1P3IiPkCLw7RtL6LoTzrjq7Q9vekMiVjc1_OH52gZ7D5tjyvniHHuh68ERVF-l39A8j1C9ZGRXi9D7yH2MvSSOwhRqIYYATItuP7bLyzpng9vDsqx_RDeZljVAaItas7bABXG-jlglOxXoG4K0IKxND4IWn4f78QNQyOnRO2bJ5OgK9ALhQehnmYst3OhuWKsCMJctYLxMoXUygv3uI0UgJJcslDa2YswIHHXyhBUQT4hdiLxQ5RdXVAudGJdxyp_oqNiYsJv8qH4QNt3VEWORBKsZTUVHPC6C8UZCvUt481DgJ7IB9qH3LiQ67UsOf7mo4vk1wCVB3d3KY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کلاس درس «ریاضی ولایی» با تدریس محمدباقر خرازی:
«شما اگر ولایت داشته باشی می‌ری زیر خط کسر...
اگه شما به این دکترای ریاضیات رو بخونید اصلاً این‌طوری نمی‌فهمن...
حروف قرآن از راست به چپه اما انگلیسی که زبان شیطانی‌ست از چپ به راسته...»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69939" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69938">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
🗞
رویترز به نقل از یک مقام ایرانی:تهران و واشنگتن در مورد تمدید آتش‌بس گفتگو نمی‌کنند.
این منبع افزود که از دیدگاه ایران، هرگز تاریخ رسمی آغاز آتش‌بس وجود نداشته است و بنابراین، چیزی برای تمدید وجود ندارد.
این منبع ایرانی، ایالات متحده را به نقض توافق‌نامه همکاری متهم کرد، این در حالی است که این توافق‌نامه تنها ۴۸ ساعت پس از امضای آن نقض شده است.
این منبع همچنین گفت که مذاکرات فعلی بر بازگشت واشنگتن به توافق و تعیین یک جدول زمانی برای انجام تعهداتش متمرکز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69938" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69937">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e246580c.mp4?token=m1NHS7AypvnrjNFervCvnFj52XX3kArYJZgkTaH5yc_1_0eDUWrxePDHFe3bpjbziGlPFZquGbeqAIHreeFwvQD_vUkPQvmJGQSk_6uwDqZNVh5hb1SnMAWwCljKVicRHr7oVRIMSQh2GjZYHylT0fcgjoxfp2cYUBtRs6hjItM246SjllhUUsjZ5ZQIF1qbLA_l5G17wyGxb2V1ACWMtHtui5CB_pPpW7PPFjlsr-j1ZpnMvom49DvgPLZM5_SsmTb6N3Q0PLU6witjUOZK8o24r83Jccpotod6C09B-r9VwawjyKp6fIZ9My2vCxk_SSz1_rmB5o8l9-3Gbk9IdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e246580c.mp4?token=m1NHS7AypvnrjNFervCvnFj52XX3kArYJZgkTaH5yc_1_0eDUWrxePDHFe3bpjbziGlPFZquGbeqAIHreeFwvQD_vUkPQvmJGQSk_6uwDqZNVh5hb1SnMAWwCljKVicRHr7oVRIMSQh2GjZYHylT0fcgjoxfp2cYUBtRs6hjItM246SjllhUUsjZ5ZQIF1qbLA_l5G17wyGxb2V1ACWMtHtui5CB_pPpW7PPFjlsr-j1ZpnMvom49DvgPLZM5_SsmTb6N3Q0PLU6witjUOZK8o24r83Jccpotod6C09B-r9VwawjyKp6fIZ9My2vCxk_SSz1_rmB5o8l9-3Gbk9IdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حرکت عجیب مجری در پخش زنده
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69937" target="_blank">📅 15:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69936">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMo031n12AHsRO78pIvDlLta1CDdlvWSXp3kSz5wp2YywxV8gT8_0NcHI4L_gxSPHiLZ9tuvRYFG3PzhVwJqo2nZasxaf3Qr1KU_Ak4RGccV2ioiinWGrHVN9t0eBW-lYuuWkGBnN3A_4us38lX13v400HBRG19CQYkvFqUXhEj2okAHBra-QkshAMN_LsqmhSGqHM5vj8dZkxKGOiKawcRa5fWXuAgC0dIwA-ACovNPpFND6tWroelo63T6pzcXfCm_ivPULnLcxSGmI4Duio8PuUZFM9fU-0B6yA1eixg1wFi9NZiHnLob5Ra9Wl2_XvZLZxKa5Y6cToCRrZNdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
🇹🇷
🇺🇸
نیویورک تایمز:تهدیدی که از سوی ایران مطرح شد و باعث شد رئیس‌جمهور ترامپ ماه گذشته به طور مخفی هواپیمای "ایرفورس وان" خود را تغییر دهد، زمانی آشکار شد که او در آخرین روز حضور خود در اجلاس ناتو در آنکارا، ترکیه، در تاریخ ۸ جولای، در حال عزیمت بود.
اطلاعاتی که توسط سازمان‌های اطلاعاتی آمریکا جمع‌آوری شد، نشان می‌داد که یک تهدید خاص از نوع موشک‌های زمین به هوا علیه هواپیمای "ایرفورس وان" وجود دارد، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد.
همچنین، فردی که در نزدیکی محل برگزاری اجلاس ناتو حضور داشت، در حالی که یک موشک قابل حمل روی شان خود داشت، مشاهده شد. در همین حال، عوامل ایرانی دقیقاً می‌دانستند که ترامپ در آنکارا در کدام محل اقامت دارد، از جمله طبقه محل اقامت او در ساختمان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69936" target="_blank">📅 14:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69935">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=JTrb9HSHLKU3jV1zTIpXAC8-iCSaK6jrrEnPNz-oIE_iEeSKDPxUYEjZiq_76r5GSdsFD1fP558FGzMUdyd_0RYnUt8gPuUgaCbfy3ENOC1CT7tb5VkNQ0cRC_kSbpNkSmT4cY0tZKd_o2iQq9EO06CLnHjnnsXFec-P6JJHVI7RKpJrrJmoZfw05tsRTMURYEI1aP2X8wDojfPnmZgQtUMHKmGyNH2Ep3ju3JwbtrBx6iEq0iXDy3qqIr_23MJ7Pi7wiPcXTBBOOC7KwQbq5ZXx5BBbr-XJfY9xwiFeTfDEc66utPB8MNXcnyFOu2OpRfAWUBB2NJkATobHuxMiU7DKBrDRVKK7_RZDgtX8pANF8d6L6gIlBwpwELaRYvyLkWDGl94xJjHqQzNzWlMAyN632lXvA16NsD4lpwfNRH9a6f8tHLMPc8YLy8aQMWVubn9wognfUPMFypxji0F4wtLApVxayb7NVdPqEG4Iuw_lSg-vUfy2C31BXsxUGfQaJjJlVmH5lv9VNeeBWRIAJOhNct6GYivxKWk9DJp6sGHMc05YX1Yq16K8fsNnhkcIaFjNsm4GJttMg6-1ziRDzdYRkOvduvd8iwOY8n6rK6OSi9ay_VBPj-C9DDL7UnIRZhvYgqx8pUwQ6sghuIdtWZzoqOWxN_68q7bUNRfoSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=JTrb9HSHLKU3jV1zTIpXAC8-iCSaK6jrrEnPNz-oIE_iEeSKDPxUYEjZiq_76r5GSdsFD1fP558FGzMUdyd_0RYnUt8gPuUgaCbfy3ENOC1CT7tb5VkNQ0cRC_kSbpNkSmT4cY0tZKd_o2iQq9EO06CLnHjnnsXFec-P6JJHVI7RKpJrrJmoZfw05tsRTMURYEI1aP2X8wDojfPnmZgQtUMHKmGyNH2Ep3ju3JwbtrBx6iEq0iXDy3qqIr_23MJ7Pi7wiPcXTBBOOC7KwQbq5ZXx5BBbr-XJfY9xwiFeTfDEc66utPB8MNXcnyFOu2OpRfAWUBB2NJkATobHuxMiU7DKBrDRVKK7_RZDgtX8pANF8d6L6gIlBwpwELaRYvyLkWDGl94xJjHqQzNzWlMAyN632lXvA16NsD4lpwfNRH9a6f8tHLMPc8YLy8aQMWVubn9wognfUPMFypxji0F4wtLApVxayb7NVdPqEG4Iuw_lSg-vUfy2C31BXsxUGfQaJjJlVmH5lv9VNeeBWRIAJOhNct6GYivxKWk9DJp6sGHMc05YX1Yq16K8fsNnhkcIaFjNsm4GJttMg6-1ziRDzdYRkOvduvd8iwOY8n6rK6OSi9ay_VBPj-C9DDL7UnIRZhvYgqx8pUwQ6sghuIdtWZzoqOWxN_68q7bUNRfoSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران:
«ما بیش از نواخت شلیک موشک‌های بالستیک، در حال تولید و تحویل آن‌ها به رزمندگان هستیم.»
«ما فقط ۹۵۰ شهرک صنعتی داریم به علاوه صدها مجتمع صنعتی که خارج از این شهرک‌ها هستند.
اگر روزی برسد که ما هیچ موشکی هم نداشته باشیم، ما خطرناک‌تر می‌شویم چرا که دشمن با تاکتیک های ناشناخته ای مواجه می‌شود که می‌توانند منافع آمریکا در جهان را به آتش بکشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69935" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69934">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TholqMOu9FC3VQvZKKVNN9NPiPW6wxkAcjt3nLS6knMCseWJrkM_Tua8eNkdOyTbe6QjKzq984HOLDBqnL2O4h1lRxQlJ8FKpXnVoemLmTcg1b5imZ0FoMzDBTEzJzLj4R5TPxqwhESLixuSFwyl54igNWHG8xX83mi1XzRlAzE4DMcBhhaazdTzAkkIeJKRxZFPmo_WJRRrlGwtrf1cQv7Ywr3QmiWNd0h1DXofGO4scK8YzWoxiMZUNyykuQoAqY6aP3HuFBrA-Zi9Ubg-W1h6_E8jg583E4uLg56jAqTKUZqPdnmz0QDDkzB2VoNCpWAcUVsjeXEKXK7dFWoivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69934" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69933">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=XCqwvx9qlTV2uv6MDBaBnXnPwCzfKn53oaiYnacMx5LZ8o6bqdlDkoa5DYFIx58P8JtmfgPZ_WFmPQhcUQxjVr70BgzGMlFY3-Z0cOXwP6qc_LJD7_rZIRW_PYp1PwevnrQIwtzLnySPSJV5F14xDOmJGG2fzcTI1_xSgxuyXqdvFnQKl7tGJvCtgCtpFZCTV4tBDV_xX8ORP3kPbQY_tLqHGGWTlNQ5I27WDKbX8A8Z3nhDWje4eL2ztaZkEW3Njbl1X_Zc7I30zk-QCDYvOpdmWi2gxRTd5V69ztjUvAnaneStoCOLMhMk3xOycM0SgaT5USOtTXAQkNQaXFuNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=XCqwvx9qlTV2uv6MDBaBnXnPwCzfKn53oaiYnacMx5LZ8o6bqdlDkoa5DYFIx58P8JtmfgPZ_WFmPQhcUQxjVr70BgzGMlFY3-Z0cOXwP6qc_LJD7_rZIRW_PYp1PwevnrQIwtzLnySPSJV5F14xDOmJGG2fzcTI1_xSgxuyXqdvFnQKl7tGJvCtgCtpFZCTV4tBDV_xX8ORP3kPbQY_tLqHGGWTlNQ5I27WDKbX8A8Z3nhDWje4eL2ztaZkEW3Njbl1X_Zc7I30zk-QCDYvOpdmWi2gxRTd5V69ztjUvAnaneStoCOLMhMk3xOycM0SgaT5USOtTXAQkNQaXFuNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سفره‌ای که واسه عرق‌خوری تو زندان پهن کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69933" target="_blank">📅 12:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69932">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=CXH-wJZeguasAfk0kiuPg126yFnYu-D0pkvSOkU1b8NVSzoQDZZO9ds1Ja74yfroo7hHWE1YMLSfwwh24vgNyWN3_mXIwXCugizhA7u2o8IstJzgXQgRDTOiLZxejUZAIks_PRJA_bJNaQ7wRO_a8b28lfXFme5i_o31PQZufvf7DREe2tj37t-ZGWxNvJ-Tg05Jd4mgYtVKeINizt7dBrMOX9pY0hCl4JPA_IOpQyKTzyqT1dAklUcbNDaIvn0_SBrHa1uw6NVy31TLsj7XKvFa8Sjcavd9hpRPz3w3Dh9u9V7hBB-TY6Jg8UNQN__VpoMWQ6DfORpPn4M4mKbmzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=CXH-wJZeguasAfk0kiuPg126yFnYu-D0pkvSOkU1b8NVSzoQDZZO9ds1Ja74yfroo7hHWE1YMLSfwwh24vgNyWN3_mXIwXCugizhA7u2o8IstJzgXQgRDTOiLZxejUZAIks_PRJA_bJNaQ7wRO_a8b28lfXFme5i_o31PQZufvf7DREe2tj37t-ZGWxNvJ-Tg05Jd4mgYtVKeINizt7dBrMOX9pY0hCl4JPA_IOpQyKTzyqT1dAklUcbNDaIvn0_SBrHa1uw6NVy31TLsj7XKvFa8Sjcavd9hpRPz3w3Dh9u9V7hBB-TY6Jg8UNQN__VpoMWQ6DfORpPn4M4mKbmzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تصاویری جالب ، از تلاش ناموفق یک تیم آتشبار سیار روسی برای رهگیری یک پهپاد انتحاری (کامیکازه) در حال عبور را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69932" target="_blank">📅 12:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69931">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=gsYNI-SgTM3Ea0jc3C8spTU2efQZ_Wo-9CLgZdYQ1YNRSboN34lfh3HETheTub9gWqUGGn2caliz__bT14wp9XAm6yr23LATgohlnloqGlcHS-1o5eQmSTYtq7NhLM-cOH-JlLYfBp9d9jd__ejg155DhGis5fPc72-v0uJJmR7I18ENpp3MCI2Z7pNElPgbb3AkygCCVpsDOTHayUcTs8u-SOdMD6sMn_mZAAv09fg9JOXpz9OAfEIaO906T2_yHUS30_OniHTzhTs6nB922FFBYHhsMGLdybVwcPJe5jFiSRan6vDj63GPBHfzO-ddh0uiKLwv2pRthNaUuoNCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=gsYNI-SgTM3Ea0jc3C8spTU2efQZ_Wo-9CLgZdYQ1YNRSboN34lfh3HETheTub9gWqUGGn2caliz__bT14wp9XAm6yr23LATgohlnloqGlcHS-1o5eQmSTYtq7NhLM-cOH-JlLYfBp9d9jd__ejg155DhGis5fPc72-v0uJJmR7I18ENpp3MCI2Z7pNElPgbb3AkygCCVpsDOTHayUcTs8u-SOdMD6sMn_mZAAv09fg9JOXpz9OAfEIaO906T2_yHUS30_OniHTzhTs6nB922FFBYHhsMGLdybVwcPJe5jFiSRan6vDj63GPBHfzO-ddh0uiKLwv2pRthNaUuoNCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از هجوم انقلابیون به کاباره های تهران و نابودی هزاران لیتر مشروبات الکلی، در سال 1358
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69931" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69930">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/69930" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69930" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69929">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAlhFF0NBPL3YzqknkaKm46AkBhIsIYMQ1vJyUlr58_Wiz3vr5lBsewITtTu9YVXeLE5lkaeZf-yWjR_5BJx_ULErkqHKQbcNZV1DSl7rUuJAjsTQQktQNIve6utpY26XjGJFjLOwsO46-nRUGoX6XexsFUFTBhuM93z4hM2x-5mYaCaD_mhx8uK_pfcxwSZcLZJ8BNi7AqnaPeA-h88Zj_3jMzVpbj_doIkZ1crN5y2wfUEL5l556B0DQBVrRfmxrsCtnaTWpO2ol35GYf9hYMAgQDpMEohHhjwhulirBtAAXAQvOpclv6vC9fckyMVkjh3zKptXi7F6DxzeW_nog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69929" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69928">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=Ht039rlGj66RWn6a9v_zTIVpLU44iIu_aqnCih7u39EaK5QxmxJ_jga6wFFSkvyh116clKkL0eYSzDCkSO4C8-qEVODUWcn5KQRVqAadPD14JMcg7CEQLVMvvEucsorjGgsFFmkKpeJQp8HArfkKjY4ge5EYo_UlBb4YEIEC6V7j7SeLWEfCf6e-OREgqr6GWzE2DEP-4bNLhPE9_1TxqNhOrUMIXY7rDJE-GcHtxTx77fOkzH2Xf8SQv9oHwO3veSyOxDuU4W5xTr3BgATGyAdEaYbwBpEgVddTPZutVXs56wkH30Lv9mVTN6r2iNXM6nMrDc_jPIVvYEb6XrSYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=Ht039rlGj66RWn6a9v_zTIVpLU44iIu_aqnCih7u39EaK5QxmxJ_jga6wFFSkvyh116clKkL0eYSzDCkSO4C8-qEVODUWcn5KQRVqAadPD14JMcg7CEQLVMvvEucsorjGgsFFmkKpeJQp8HArfkKjY4ge5EYo_UlBb4YEIEC6V7j7SeLWEfCf6e-OREgqr6GWzE2DEP-4bNLhPE9_1TxqNhOrUMIXY7rDJE-GcHtxTx77fOkzH2Xf8SQv9oHwO3veSyOxDuU4W5xTr3BgATGyAdEaYbwBpEgVddTPZutVXs56wkH30Lv9mVTN6r2iNXM6nMrDc_jPIVvYEb6XrSYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قیمت های پشم افکن خونه و برج توی فرشته تهران بعد از جنگ که به متری 2 میلیارد تومن هم رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69928" target="_blank">📅 11:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69927">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=Touz0T4P2yeEYHYeN4CCl0AIk159RACmpkE2PFZXD5l_N_9AZFWdp0sUVb--irA53e-gYpWZo8QXOYjrxWE1PVoHmfjPJdWGbSdjZuBjkZNrgD3383rQ-xDKdAvudwtOZoRIOsfiEir2jw1aNn1oo71yy26p1TSzA9I-FY3GuRKmvFnnzCjLTf6FowRRN0xtWKxnCSmn2ZutFCL0WkQPzFDOgKFsVSMnPzJ6jXZWqdEylhPAEGg9jtnGg9TvCiVJb0AOXj9rFqvXkiqxmZ_bu1FCx9Pkmv1zUxQeIdjzjHxAI28HVEp5TQXeF165MmdK2xNd-WxR3DQ7dx_CS3ne_TRGYDOz0JKVubeNl7MhEZiWx2emkeKK-eANFpiQb2bRJp--zf49IBttC4QztueUuxDVDf7bKhWYi12RaXXHC2VUpW48lmOou2uMcHIs5_oOYgOnyL2Zf9EmLOtJBChpermzxwM2Ms3-dzclokVyR-9rKqQO3ab41YHP_t0x7hUNO7gsp3dZ7jp7f1wCjpkb_OTctAiISpHa_VhkVw84Zy3fsaTeBmHUq2M9CiXFt2fj_myZbMymFWfB23-_67F5ECSVx58S0RvJffPAJi4G9IrjKRJpiMd4oRgYEYn12dbpUW22viMQY539WbqvtudrMtjLNy58Er1xJaRlV-Fcarw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=Touz0T4P2yeEYHYeN4CCl0AIk159RACmpkE2PFZXD5l_N_9AZFWdp0sUVb--irA53e-gYpWZo8QXOYjrxWE1PVoHmfjPJdWGbSdjZuBjkZNrgD3383rQ-xDKdAvudwtOZoRIOsfiEir2jw1aNn1oo71yy26p1TSzA9I-FY3GuRKmvFnnzCjLTf6FowRRN0xtWKxnCSmn2ZutFCL0WkQPzFDOgKFsVSMnPzJ6jXZWqdEylhPAEGg9jtnGg9TvCiVJb0AOXj9rFqvXkiqxmZ_bu1FCx9Pkmv1zUxQeIdjzjHxAI28HVEp5TQXeF165MmdK2xNd-WxR3DQ7dx_CS3ne_TRGYDOz0JKVubeNl7MhEZiWx2emkeKK-eANFpiQb2bRJp--zf49IBttC4QztueUuxDVDf7bKhWYi12RaXXHC2VUpW48lmOou2uMcHIs5_oOYgOnyL2Zf9EmLOtJBChpermzxwM2Ms3-dzclokVyR-9rKqQO3ab41YHP_t0x7hUNO7gsp3dZ7jp7f1wCjpkb_OTctAiISpHa_VhkVw84Zy3fsaTeBmHUq2M9CiXFt2fj_myZbMymFWfB23-_67F5ECSVx58S0RvJffPAJi4G9IrjKRJpiMd4oRgYEYn12dbpUW22viMQY539WbqvtudrMtjLNy58Er1xJaRlV-Fcarw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداشمون در یک دقیقه به ۱۳ نفر پیشنهاد رابطه داد و  همشون هم ریجکت کردن و تونست رکورد ریجکت شدن زیر یک دقیقه دنیا رو بزنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69927" target="_blank">📅 11:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69926">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
لحظه نابودن شدن خونه های مستحکم و نوساز توی کلمبیا بر اثر زلزله!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69926" target="_blank">📅 10:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69925">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=tZy7tTT4XWAkpxFHIYKeha2jEfhyv6_qqxiFRokN181d0moPkFhrY5w9MNkxKHti5bAsVW46psESn0Lgw_Yy1DDMRtlNTpzaE6kNs7nnfMZYT2WcnOiEDRkNS7ykD8xlK1OAon_zJN4Ox2xj5iJL1uckP6BBmlWWITt4Gb5PFVMZlzkmUSt8pneXolsty3M4PGJRY813id2Tdt3A90yngB1N6oUtU6wrcVJC4hWl6DEtG8lpcPwwBA9qP9TVE7BLrQ1hSPaPhxag9yPj2vU6lIupZPnVcGCiXyzCTgYs6caOYkCMBL1ANA8qHPaw0tyzuUBH-j8w2oyxnUtUNDjXsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=tZy7tTT4XWAkpxFHIYKeha2jEfhyv6_qqxiFRokN181d0moPkFhrY5w9MNkxKHti5bAsVW46psESn0Lgw_Yy1DDMRtlNTpzaE6kNs7nnfMZYT2WcnOiEDRkNS7ykD8xlK1OAon_zJN4Ox2xj5iJL1uckP6BBmlWWITt4Gb5PFVMZlzkmUSt8pneXolsty3M4PGJRY813id2Tdt3A90yngB1N6oUtU6wrcVJC4hWl6DEtG8lpcPwwBA9qP9TVE7BLrQ1hSPaPhxag9yPj2vU6lIupZPnVcGCiXyzCTgYs6caOYkCMBL1ANA8qHPaw0tyzuUBH-j8w2oyxnUtUNDjXsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های یک مقام حکومتی رو ببینید که باخنده درمورد شلیک به سر معترضا صحبت میکنه:
ما به پای معترضین شلیک میکردیم ولی میخوابیدن میخورد به سرشون
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69925" target="_blank">📅 10:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69924">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tiaxcKyIpUM57JYVcxMbbD6S4HL9VWaWLZMPnVk-Ms0-PSLRUVU6uUBafICxgmysvi-juavJLQ-8GdLvygc78eCfbiOCzk71-zed1E4f83JsjDdMqfe8znHmsWAWNQdFKOIpz44jwy8riusHPxyl7IkRYAaEPYv8LNYB3EDHs-bvrwncnFAfQCr9pW1IlK6Io-R5pEIEBsxMMqzLCacJiHexSLgq5bdhZffII8AJ6gzvPpHxeRV_qAef3uhUf6bXbygv2fRekQ3Oobc8bKKnraH7FNt6TK3MlZ_W3tY5C3XYUPDQUJCr7ivuSla13LSnhrTFxMAjlDcIkAjVnBcb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tiaxcKyIpUM57JYVcxMbbD6S4HL9VWaWLZMPnVk-Ms0-PSLRUVU6uUBafICxgmysvi-juavJLQ-8GdLvygc78eCfbiOCzk71-zed1E4f83JsjDdMqfe8znHmsWAWNQdFKOIpz44jwy8riusHPxyl7IkRYAaEPYv8LNYB3EDHs-bvrwncnFAfQCr9pW1IlK6Io-R5pEIEBsxMMqzLCacJiHexSLgq5bdhZffII8AJ6gzvPpHxeRV_qAef3uhUf6bXbygv2fRekQ3Oobc8bKKnraH7FNt6TK3MlZ_W3tY5C3XYUPDQUJCr7ivuSla13LSnhrTFxMAjlDcIkAjVnBcb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:«بازندگان و برندگان انتصابات جدید در جمهوری اسلامی چه کسانی‌اند و آرایش جدید قدرت چه چیزی به ما می‌گوید؟
🔴
انتصاب محسن رضایی به دبیری شورای عالی امنیت ملی و حسین طائب به فرماندهی بسیج، دو پیام مهم دارد؛
یکی رو به بیرون، درباره مذاکره، جنگ و رویارویی با آمریکا
دیگری رو به داخل، درباره مهم‌ترین نگرانی حکومت: خطر خیزش دوباره مردم ایران.
در حالی که هنوز درباره زنده یا مرده بودن مجتبی خامنه‌ای و میزان سلامت او تردید وجود دارد، سپردن بسیج به حسین طائب، یکی از نزدیک‌ترین افراد به مجتبی، یک پیام روشن دارد:
نگرانی اصلی حکومت، خیابان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69924" target="_blank">📅 09:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69923">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=eazNROgSt1opMgwK7Lmh1vtUbqSQyhhl5b-j9bobtf7AOg1iirv-lh0metgM1NYV8MbOmJTKHmh-0d-sRCzd-V5l_4jl034i0iu9XUhbFZ2Sh8KADMpT-GFKKYXu2-fqWLyzT7IZg4woQ4i0RLsbI99zznDNvYOepasvOMS2LYeVqWy-Te5yUsYc3RUj1mXhpTcyWGyc_St1F5ATdKRXOXVT_3-Ue2KsbH0yF_QhAUBH5fZw-pFO98V-aj6qa88tA6AiFra8j7FLlBwPF7HQlty2pJAhc3DEvGOlgPIXSBSzTkvWqMSv8yqCtBmn_5jzcP2mrB6D-3G3vJ3-H2PwCxA_tqaZKiqH2-JMZgRqlE7sJSzM0SUV2RPsQ4FSnQ2G94-Y2MotVoceTJe0Q4jwz7jS6xnvg9pvntu5cC1K8-4LTmk1RlKjGSf8nhbf26cxGnxX-hxzF_gT7e-Q8NQMuF6_9vUkj03jX77DsrfoV5fVAXbsY63k03-VnhOyqu9XpsX_d3PwlNVS3s1J9i-bxRz9jizl6CtkYhPevzGOVnOQ7NlQ4G4Dqr86NeM_VPmfdMtvhDYhXOvvGEkaVT4cnObo2W82P5RmhJeqzIO_iYsVt6NxI1hz_rm0UFsyZ3yaJEmSZnXM038kJZfWJh0HcaKT3hzhAE5plgtwH8E6nrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=eazNROgSt1opMgwK7Lmh1vtUbqSQyhhl5b-j9bobtf7AOg1iirv-lh0metgM1NYV8MbOmJTKHmh-0d-sRCzd-V5l_4jl034i0iu9XUhbFZ2Sh8KADMpT-GFKKYXu2-fqWLyzT7IZg4woQ4i0RLsbI99zznDNvYOepasvOMS2LYeVqWy-Te5yUsYc3RUj1mXhpTcyWGyc_St1F5ATdKRXOXVT_3-Ue2KsbH0yF_QhAUBH5fZw-pFO98V-aj6qa88tA6AiFra8j7FLlBwPF7HQlty2pJAhc3DEvGOlgPIXSBSzTkvWqMSv8yqCtBmn_5jzcP2mrB6D-3G3vJ3-H2PwCxA_tqaZKiqH2-JMZgRqlE7sJSzM0SUV2RPsQ4FSnQ2G94-Y2MotVoceTJe0Q4jwz7jS6xnvg9pvntu5cC1K8-4LTmk1RlKjGSf8nhbf26cxGnxX-hxzF_gT7e-Q8NQMuF6_9vUkj03jX77DsrfoV5fVAXbsY63k03-VnhOyqu9XpsX_d3PwlNVS3s1J9i-bxRz9jizl6CtkYhPevzGOVnOQ7NlQ4G4Dqr86NeM_VPmfdMtvhDYhXOvvGEkaVT4cnObo2W82P5RmhJeqzIO_iYsVt6NxI1hz_rm0UFsyZ3yaJEmSZnXM038kJZfWJh0HcaKT3hzhAE5plgtwH8E6nrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
من به ایران اعتماد ندارم. من آخرین کسی هستم که به ایران اعتماد می‌کند. آن‌ها مدام به من دروغ گفته‌اند.
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آن‌ها کنترلی ندارند؛ ما کنترل کامل داریم. آنجا در اختیار ماست.
و شاید زمانی آن‌ها دست به کاری بزنند و آن‌وقت نابود خواهند شد. اما فعلاً در موقعیت بسیار خوبی قرار داریم.
ما با کشوری سروکار داریم که ۵۰ سال قلدرِ خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال می‌شود، مگر نه؟ ما چهار سال بود که می‌گفتیم ۴۷ سال؛ و حالا دیگر آن‌ها قلدرِ خاورمیانه نیستند.
🔴
ترامپ درباره تغییر هواپیما در آنکارا:
این موضوع صرفاً به «سرویس مخفی» (تیم حفاظت) مربوط می‌شود. من فقط از تصمیم آن‌ها پیروی می‌کنم؛ بنابراین تابع نظر سرویس مخفی و ارتش هستم.
آن‌ها می‌خواستند که من با پروازی دیگر و هواپیمایی متفاوت سفر کنم ــ که از نظر ایمنی تفاوتی نداشت ــ اما چون خواستار انجام این کار بودند، من هم پذیرفتم. من هر چه آن‌ها بگویند را انجام می‌دهم.
گمان می‌کنم تهدیدی وجود داشت؛ البته من خیلی پیگیر جزئیات آن نشدم. من با تهدیدهای زیادی مواجه می‌شوم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69923" target="_blank">📅 09:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=TJG1qV2y-bcmQKmOx0FGaIPnzWKEH8tmtMzZ_5oJOcaafk7cTAgseDz8JDInHSxEgOlqISft2fyxXeTcFrg5f7Dl83psUu0oP2eH7q0VTqvZAjwNLjbcTu8fzjYS3XCEdCdvyd5h9ohuEKJNOdSF3zlnsC3-l9iCdOy0mM3takyPGWJY1nIouC4UlnO8YdzWb4LGo1-YdwEuvWCILVTQ4HLa6LmD2GO82RvOtp4gtrJZE0Pw0nVGMXoa_frna-xeZC4XttlJKti0qnFqIUAnbgbM8QXpJqqQol3S6QaTrgbcpFE_3O5ULMp1tb4MiRM0NusXpfP3Kw-o9Mbh21u5wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=TJG1qV2y-bcmQKmOx0FGaIPnzWKEH8tmtMzZ_5oJOcaafk7cTAgseDz8JDInHSxEgOlqISft2fyxXeTcFrg5f7Dl83psUu0oP2eH7q0VTqvZAjwNLjbcTu8fzjYS3XCEdCdvyd5h9ohuEKJNOdSF3zlnsC3-l9iCdOy0mM3takyPGWJY1nIouC4UlnO8YdzWb4LGo1-YdwEuvWCILVTQ4HLa6LmD2GO82RvOtp4gtrJZE0Pw0nVGMXoa_frna-xeZC4XttlJKti0qnFqIUAnbgbM8QXpJqqQol3S6QaTrgbcpFE_3O5ULMp1tb4MiRM0NusXpfP3Kw-o9Mbh21u5wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=alb-H6dCwME6OH-1n5BwN7ZeusGTBroDKqsJVv7eeB6d1xL9yXyUR7hoB7UBhYrp9HEeh3QRTh2fVTLs6KrJ3t3o8zXExgUds2qXRVoiqQN8IZtr-gau16YMgUAjyTKn40TNpbvNmGDV3nlDvZNZdhKDk5fCcjEpFcJdiHfEBkUgUAUodBOFkjYwGkhHMvNb2JCxXF3eVHjcor3KxKLqVaPXQINWMw_Evei7bkRTJZaFlQh3bDvIK1d5frhiyu9GMdjGeMSt-IXRkIU8JTgcXbtlM2e5y-FFL48dxElea1X88BHfE1v8qWuYL2uU1MXp6HGI9Qv14IHOWI6YYvkskw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=alb-H6dCwME6OH-1n5BwN7ZeusGTBroDKqsJVv7eeB6d1xL9yXyUR7hoB7UBhYrp9HEeh3QRTh2fVTLs6KrJ3t3o8zXExgUds2qXRVoiqQN8IZtr-gau16YMgUAjyTKn40TNpbvNmGDV3nlDvZNZdhKDk5fCcjEpFcJdiHfEBkUgUAUodBOFkjYwGkhHMvNb2JCxXF3eVHjcor3KxKLqVaPXQINWMw_Evei7bkRTJZaFlQh3bDvIK1d5frhiyu9GMdjGeMSt-IXRkIU8JTgcXbtlM2e5y-FFL48dxElea1X88BHfE1v8qWuYL2uU1MXp6HGI9Qv14IHOWI6YYvkskw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=ol8tHbyG7LFlN-uQmBi7Z7RdrkRvu43AYQ9dfn38to-ND5-LIIStZ8KrgLfp-Fv5mLTTifUulIqhPFiJqeaosGkr5VQv6Y-OLt3Leyj3osBpDNyO_uLtI61CH3Ywgvx-1If9EK-m4mppgq4G5a2lZtam14pF6vQ1kUQttldBErQtdUPG2jYtanwaBjnvLkTepVGbTb2fdGBPrY09NMRS_xDMbSfni4FYqdonsOg2mSshfcCt6w1784LKYA073fgoLK8qU05K2E0L3ugsBnzeTKNNratGF4mkBsVrisKTjV8yJIFiuVPdFzHZFuv2w01l0CEovU9LYR3U36recK-aYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=ol8tHbyG7LFlN-uQmBi7Z7RdrkRvu43AYQ9dfn38to-ND5-LIIStZ8KrgLfp-Fv5mLTTifUulIqhPFiJqeaosGkr5VQv6Y-OLt3Leyj3osBpDNyO_uLtI61CH3Ywgvx-1If9EK-m4mppgq4G5a2lZtam14pF6vQ1kUQttldBErQtdUPG2jYtanwaBjnvLkTepVGbTb2fdGBPrY09NMRS_xDMbSfni4FYqdonsOg2mSshfcCt6w1784LKYA073fgoLK8qU05K2E0L3ugsBnzeTKNNratGF4mkBsVrisKTjV8yJIFiuVPdFzHZFuv2w01l0CEovU9LYR3U36recK-aYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=Uxwuf6mbjSUTJ2ms8sL9mUxR6rVoP5YmIZqMGOqnvCEYja2vu1NpO_0sr1pPY0DZMadEocEdzzDKXh4H1IVtH06ykjsv2_xhi3hvGLQ76P96pXdJPu2WrV7CJSNly-tfqego3U1qnt28jXKlL3HQRir1jjXbAFCI1OcjEVqP6Lu7T3dVY7rCq1__BLibrLkDVrGd4ftwFYhafUzY-CtCHrNuv8-pMwbBhLz_5yWXHQu5ZMmJ31SkZYiFs5RmXJo0TmxMYPgi7KqnX0ACchDaKZVSVU2B11tKYjkXDiWbPOFrRh8vxj7wH7bwViYZkb7RZnyJGiRgAtbO7ZsDLy-B1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=Uxwuf6mbjSUTJ2ms8sL9mUxR6rVoP5YmIZqMGOqnvCEYja2vu1NpO_0sr1pPY0DZMadEocEdzzDKXh4H1IVtH06ykjsv2_xhi3hvGLQ76P96pXdJPu2WrV7CJSNly-tfqego3U1qnt28jXKlL3HQRir1jjXbAFCI1OcjEVqP6Lu7T3dVY7rCq1__BLibrLkDVrGd4ftwFYhafUzY-CtCHrNuv8-pMwbBhLz_5yWXHQu5ZMmJ31SkZYiFs5RmXJo0TmxMYPgi7KqnX0ACchDaKZVSVU2B11tKYjkXDiWbPOFrRh8vxj7wH7bwViYZkb7RZnyJGiRgAtbO7ZsDLy-B1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUtipQmvMEp2hKlKETTSRrymJiyMbXwyEql8aVflfGFoAlIe6Ks73miGC6R0jyuLjJAUx19EiDLgbtXgEec1QrB-8FOxo8bxHYDdfS3_6wQmaCQDcWjzQjd1eCcGYqbW5wU-JzJ_wivf6h31wunyn0rCMxazePYuM-16IAXDZxhOo3_GkYakaShVYOTULDUcd_owel5Bkl0wrRasxjzOlaxr5Tb3v95DOKsq3yqYogzDQEllJ-y2tdCLwjOvYENxKtQkim57RbFCFoWrerHXBOZCvYq2pC0TgCYnSN9VIc1gFeNrqS4tS7Y3cB4s8nn1qGQtS24EKuF-t9BoUviwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=DVgqEK0Sn1reMqf5OcwNDH1ZvjFAqdmPd7H_VszQKSogiiPzx9Lo4Veo--nfo8PzOox-KVpq9nNjuWOiUSTyKVmxTvvSOTg-11k1TZVWczLjpU72HxYtkJyI0oyWE98OxD-_4o4ROz8i3UDNLcbDrf3facyRrF7y0R_Y5EtDhgdy5kyOzW3ttVlefQE5uZk7o9fsvQYUb27vd8uP4pw_h7U4UKtHQzWwjCLdAU6XbHETR7aOnPc16p59RydNG0BC7hD--n1BT9xkowUA1od5pi0FcTH27JRgX0K3jHqWXKi0LdT8IqLCSFRSuaaQT03HER7ReOyegH1bbgKhgzGpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=DVgqEK0Sn1reMqf5OcwNDH1ZvjFAqdmPd7H_VszQKSogiiPzx9Lo4Veo--nfo8PzOox-KVpq9nNjuWOiUSTyKVmxTvvSOTg-11k1TZVWczLjpU72HxYtkJyI0oyWE98OxD-_4o4ROz8i3UDNLcbDrf3facyRrF7y0R_Y5EtDhgdy5kyOzW3ttVlefQE5uZk7o9fsvQYUb27vd8uP4pw_h7U4UKtHQzWwjCLdAU6XbHETR7aOnPc16p59RydNG0BC7hD--n1BT9xkowUA1od5pi0FcTH27JRgX0K3jHqWXKi0LdT8IqLCSFRSuaaQT03HER7ReOyegH1bbgKhgzGpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69913">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rh04KvUxpWd0m8Nyfi7LthaWi4g_-rjQYnaQ4Uy-lV3mPi34Bur_xQgXAoAZvcZlddOu-9RjBnbLEiTMptzbMYnzeIAmtHDDTkp-CsehXRa4iv8OXNr6n8N2Rd9fFSfnz9zkrjmSvshKpAlyY_aPRLkB4kI3qveI9Y7Rb2G8HH5egwVg7bPBzCli0a3RIaiXzTF0hB0eFeeNpC6PIhX1kn1kv65CCpe1TGgpXGtfZATE7_aZzx7WyFSlpX77AVl4zij4_3Mq8V9DrcHX3fa38yI7idQnvVqt91C3GAyRzhvE4UtUcsKIRZ9eXhtNYV60gQNJKS5s1GET0K7_VKgnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
وال استریت ژورنال:اسرائیل دولت ترامپ را در جریان اطلاعاتی قرار داد که نشان می‌داد توطئه‌ای احتمالی برای هدف قرار دادن هواپیمای ریاست جمهوری با موشک‌های زمین به هوای دوش‌پرتاب وجود دارد.
مقامات امنیتی ایالات متحده متعاقباً پس از اجلاس ناتو، رئیس جمهور ترامپ را با استفاده از یک کامیون پذیرایی فرودگاهی در آنکارا به یک هواپیمای نظامی جداگانه منتقل کردند، در حالی که مارکو روبیو، وزیر امور خارجه، دیگر مقامات ارشد و خبرنگاران به عنوان بخشی از یک عملیات فریب در هواپیمای ریاست جمهوری باقی ماندند.
در نهایت هیچ موشکی شلیک نشد و هنوز مشخص نیست که تهدید گزارش شده چقدر معتبر بوده است. این عملیات اولین باری بود که چنین اقدام فریب‌آمیزی در دوران ریاست جمهوری ترامپ استفاده می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69913" target="_blank">📅 22:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69912">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=Hl__hwqGUtjjP56QeDMKr6a2ydm-fj2w_l2wUOGZ5CUFq4Pm6I5JtyAqqbP6qCnYw5qh9IGFdeNSMtmEnuDEuaWbT6ZjRw7rrIq8-Xwu3TBhU62btKBQBjM9fdfBElq1sUCkWT7HMw2bjhr1Dz-alhBbqGASlm2fztQ8a-A4_LnYJXOXFwK8Dev9VbA3go4PnnIZHtSlcdpLx7K1KRk4QnnGOoSpn_Q4F5bby8TSfRE0OTW12LVESm6xMnkIDP2jW1hAA7lN06wkQNBp8i7xHh-WLVun-K_Zis48TIOYtHQq7uAufyPPzA-GPCDMNpJyrKrvxR1TT2pgMifsHWCrBzE8eN7OwIdbBLpvydlQLZf6EIkc2oyWAZ14gYz7m5EYUMn4sqGqqEFAnIHXfDq3orrw0pN05TMWKT6hE-h6YghzGy1p1urM3BdTSBQaQEJMZfsHw6FX2cDPpELEoL74QUdc8AL8_RLeJQgwV8qvRfXzm_xZAQUd7hEk8gLDnI5kDGUuZiUEJYqVGtQmYG5nyYx_cZC361Eq5MYbl6HN_iUfaQ2qpS1XsHlxfe_nau1B2VI8TTeJr_ve8UpKHoJ70oA1obQ9zEKwPZDj9j7sJoLam_48jECKo29zGfEPZUBSmDZquAwAagAb3V-Ny83CrO0y5NacCYnHT2CXI_ULW7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=Hl__hwqGUtjjP56QeDMKr6a2ydm-fj2w_l2wUOGZ5CUFq4Pm6I5JtyAqqbP6qCnYw5qh9IGFdeNSMtmEnuDEuaWbT6ZjRw7rrIq8-Xwu3TBhU62btKBQBjM9fdfBElq1sUCkWT7HMw2bjhr1Dz-alhBbqGASlm2fztQ8a-A4_LnYJXOXFwK8Dev9VbA3go4PnnIZHtSlcdpLx7K1KRk4QnnGOoSpn_Q4F5bby8TSfRE0OTW12LVESm6xMnkIDP2jW1hAA7lN06wkQNBp8i7xHh-WLVun-K_Zis48TIOYtHQq7uAufyPPzA-GPCDMNpJyrKrvxR1TT2pgMifsHWCrBzE8eN7OwIdbBLpvydlQLZf6EIkc2oyWAZ14gYz7m5EYUMn4sqGqqEFAnIHXfDq3orrw0pN05TMWKT6hE-h6YghzGy1p1urM3BdTSBQaQEJMZfsHw6FX2cDPpELEoL74QUdc8AL8_RLeJQgwV8qvRfXzm_xZAQUd7hEk8gLDnI5kDGUuZiUEJYqVGtQmYG5nyYx_cZC361Eq5MYbl6HN_iUfaQ2qpS1XsHlxfe_nau1B2VI8TTeJr_ve8UpKHoJ70oA1obQ9zEKwPZDj9j7sJoLam_48jECKo29zGfEPZUBSmDZquAwAagAb3V-Ny83CrO0y5NacCYnHT2CXI_ULW7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
پرواز بالگرد آپاچی۶۴ آمریکایی در نزدیکی قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69912" target="_blank">📅 21:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69908">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8Mv8dX-CDEcKHFbMZlxExsFmY-SZR0bYA__MMfvWSwPhB2zKIqPPiYTNde2KMlJ0a63hDh51r2sQx3xvx3SOAgT3eHAPr0O7t42dqxDW1o16XLLEnDboDQJlaEDMfgwezcw9VnO0XiH38T_NMtJJ8dLnt5eHTusVI2N7u5yKYVj7cfCwXUjNyhLxa-LhyDy429oq3Ex4sWDLlmTyjIkPqpl5rgBOiKzk964eCTR_O_kOe5YIxaApNYD4284a-abhLNi-TP5J3RsH0oFfOzkTxqL3t5dUdXQkZINUIh0j5OPsBTwKLN5i54MUyFdCZtNgVXFFc8N3mDKa-vzGw_N3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLYE6454VuX8BTyGaLpbVDPyDosiKCwnGVIvT6kF4jbuTjW0Rd1CYyTlfjaecypK103hgThBNCaAS57cy4HDjM-L0g5YQCNB4PJMPXtCUy7BvAI8wV_o5wNoQa2j7yIlAjs65ztFwMcUpPm9d3W2f0CEXGMQLwAgycaEjOitqo_-Qiwa7P4tXe2xrNoScLVOSQPYKFWJ86AqBQ_EDxtizAgusrrtznxSKzVgb8wqpI8d4NX0GW_72tm0koHlumjiOVJn4ScKDN0GlhmLBGnpNc-SmCGNVFG5XEQvpyrb4QS_5DaaMpH3ScMwmPYP53aXkpnOq93e8GfWtw0IdgbwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2c2yrYQ05g4aoV0Kosei0t_q--sp93HzlMJE8g7YOghI2geAvsywzozRMYXtIx-sEAdJW-8B26R_KCbahTv63SmjTL7_VZmnt9M_gKiTEhMYYzcX1qxLiMdN4vwOnJIFC1nsKKbw37kIlfQnorhgj-5DZoGYgEeGwom1YUfakyxrTtgGOhKP_VkT_iOpcLRiPGcdA0bnf_kI1s2EGhZK49PQk7yZ2JyIQ_JaUtif4022LOWVPyi4cevwQywFmpbWCExorMZKrEEu2kvHgElPznP0h6dGhIExMewLvy73ZiqxmHP-IaP_hsl0sjImFXpjRqkOd7tZN_iDgFaiyQc5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=kYw4pmA02q64KRTnYSsoP1EY5Zs3SKqIaungPVBo81BskowsegP-yobdWpa89K9oriqVaSKL7LlkLIAztyC2Mvu1ZFsfOfabFY7bjONtkFyyYicCrPnPNqk2pQVAtl5u7KCeU3FAsFG8L3ndvipOaNfVxbH0qrUQ98HGklIw9pQwNZmDpUrkGfh6pqYeAIhPzhtCC8KOKxfF0iUk0RBHZCh2TnakFJzZjpPSIcntQJLIdjf3kUhNVofxvur_kWcHZMOCPdo70hdnfEUFINwGATEiCWRy7oeHbCXdX2clpc8S2QSbZd4O7va00Nrj7O3I_YqWpnsYioXjzafLjvzzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=kYw4pmA02q64KRTnYSsoP1EY5Zs3SKqIaungPVBo81BskowsegP-yobdWpa89K9oriqVaSKL7LlkLIAztyC2Mvu1ZFsfOfabFY7bjONtkFyyYicCrPnPNqk2pQVAtl5u7KCeU3FAsFG8L3ndvipOaNfVxbH0qrUQ98HGklIw9pQwNZmDpUrkGfh6pqYeAIhPzhtCC8KOKxfF0iUk0RBHZCh2TnakFJzZjpPSIcntQJLIdjf3kUhNVofxvur_kWcHZMOCPdo70hdnfEUFINwGATEiCWRy7oeHbCXdX2clpc8S2QSbZd4O7va00Nrj7O3I_YqWpnsYioXjzafLjvzzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛  با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]  وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد  @News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69908" target="_blank">📅 20:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=idl89F6yp6w-nwL47tHBPlg9XQJl8dLc-P4nDQE5uViFCzLLDblC953fsMktpasbE9MlyS3cR36o4vYoYGbtIz2rM5XVcDh8TDQmUqs8GlMohjz8Y6zSvsWiRjjtbstyS07KYyw4uDgbO-55BYJM2C4ION9SHmRao-HSGEqhbmaBvh53Pw_6CUG6eThivHyypPgT5G1b94DqrVEnZt20lSwVJBHsufXzbQ2W8lNT2C0sq-oUzaP57zwIkIGqCZIspygJMytxkpGEES35sRAHjzd-7I2sok9Vq1p5taQJq1k3FwYOirRkulKVxyWSjLdKVY0eT8z2Wcw-y0eJmgK7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=idl89F6yp6w-nwL47tHBPlg9XQJl8dLc-P4nDQE5uViFCzLLDblC953fsMktpasbE9MlyS3cR36o4vYoYGbtIz2rM5XVcDh8TDQmUqs8GlMohjz8Y6zSvsWiRjjtbstyS07KYyw4uDgbO-55BYJM2C4ION9SHmRao-HSGEqhbmaBvh53Pw_6CUG6eThivHyypPgT5G1b94DqrVEnZt20lSwVJBHsufXzbQ2W8lNT2C0sq-oUzaP57zwIkIGqCZIspygJMytxkpGEES35sRAHjzd-7I2sok9Vq1p5taQJq1k3FwYOirRkulKVxyWSjLdKVY0eT8z2Wcw-y0eJmgK7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PscLmmb2l7O0atTMjicCj3mZ1DmbQ_L5gQmSJfrvDkEncVVEmfzjTOafu1emeYFYWulZsuR6Vmk1eO075Ru36PU8-ma8grTYeioEqStsA4Rd5eZSCdTJjUMDGs5HydG0FjALbIIR0Yo9XCRVwXrPfvYfHIeas7Mmuua0BqSYEYEVa7K83OwXQWLIrgWOqLdYeAHFX9cahqTBTJcT7_6JVX9B8k8zlhmR4bftKH_hTKpVeRh9H4ZCYVLNTif4CNJLEe7JfVpdB12XZfZ0T4B_JbdlDPcTRwk5IKokTrCdhFMxFNMCUayIU838mxFdx3WR99kVJxIWCltB5dnB9hyKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=DrxGVFJtNomsmiVGcSSP1ffSyYIlnZbnLvKWqTNG8Hhda2NH6Gj6Eebwsq4rLvpKPr9a4JoAJGPFB6DvW1FXuwyDlYZJXHHPPqubzyDkY64e04Ea7qJ1TOEH-ysY3-hJWy2F30zBG8rBSU0brFnCP0mKdzOvG2UJfgPlRM_nNv0NWS-N0EnuQmKVloziml14tmvM6mzdb7RcHfMekgVdrBRRUZBX09npXW_rN9eAJwM1NaFCUWXWwXdiAo-4RSFp5WHO0bMLT0aRDireQ5hEEZbosBFuu4u7aIQWV_6VdVdOChrSwutc0CxMClPdDvGafNx1lqZdd_p2vtFnFG0T_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=DrxGVFJtNomsmiVGcSSP1ffSyYIlnZbnLvKWqTNG8Hhda2NH6Gj6Eebwsq4rLvpKPr9a4JoAJGPFB6DvW1FXuwyDlYZJXHHPPqubzyDkY64e04Ea7qJ1TOEH-ysY3-hJWy2F30zBG8rBSU0brFnCP0mKdzOvG2UJfgPlRM_nNv0NWS-N0EnuQmKVloziml14tmvM6mzdb7RcHfMekgVdrBRRUZBX09npXW_rN9eAJwM1NaFCUWXWwXdiAo-4RSFp5WHO0bMLT0aRDireQ5hEEZbosBFuu4u7aIQWV_6VdVdOChrSwutc0CxMClPdDvGafNx1lqZdd_p2vtFnFG0T_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=Pj4Z2gx2PmlBFI0_nKxPOiz2klqVAdw1cgnM1fZs5aloqDN1PaUw3qLtVl6q1JC_NjZhkZDlNj54s2BCC3jXwzU22fZNqHlTBJFNepFLSYHcmzBZ_MUarLYZxkUFSlYpCiI3CThmHH7vaZgtgTjRqQiGOFc6DnqGqCn6U7T72ZTWCjRSYfb7NqNh1QND8ls4L0RsvxTfcb5-jwqdLYjkUxO9pSYBQQxoUES6qGhdmTl-wU7sUWWZss9UqlBdCWeNrbxa1grz7Nfno1EmRSfTH0aSk5BYtV1-YhopmlkdaQKjhgaXQPIt0MpgCCWUyhK7yz82KccU5lo3gCxbtRJMdH8JbbSK2zzne8eikXihK3gFvxrcdaNOH95MXmXozBsnttDut6mBn6I761HhYwUVM933T-q2rymxlJgQx49021MBbX6bTHl9x3HSlEPg2rs-DyIMyEJpEff1zHzA-v7Azlg85HwawdXOVSTmb24uq5gSGqFxOSPcBlUepjq5Kktl2S9zUHKiEfgsuf3Xe8oJysC0ZKYk92IvoE18AUjWqmrQzlr4cChE5rKR2KHiDhMpjakpmXTtUQBO4HR9r7PU88vzO1Lt2nFvE5tZWnAd7RJKN81mDWA_pbc_PR2WP6uhCBXPxzXlXvKK2lMnjbfZXX1B4reQN4Ewdmip02DAvuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=Pj4Z2gx2PmlBFI0_nKxPOiz2klqVAdw1cgnM1fZs5aloqDN1PaUw3qLtVl6q1JC_NjZhkZDlNj54s2BCC3jXwzU22fZNqHlTBJFNepFLSYHcmzBZ_MUarLYZxkUFSlYpCiI3CThmHH7vaZgtgTjRqQiGOFc6DnqGqCn6U7T72ZTWCjRSYfb7NqNh1QND8ls4L0RsvxTfcb5-jwqdLYjkUxO9pSYBQQxoUES6qGhdmTl-wU7sUWWZss9UqlBdCWeNrbxa1grz7Nfno1EmRSfTH0aSk5BYtV1-YhopmlkdaQKjhgaXQPIt0MpgCCWUyhK7yz82KccU5lo3gCxbtRJMdH8JbbSK2zzne8eikXihK3gFvxrcdaNOH95MXmXozBsnttDut6mBn6I761HhYwUVM933T-q2rymxlJgQx49021MBbX6bTHl9x3HSlEPg2rs-DyIMyEJpEff1zHzA-v7Azlg85HwawdXOVSTmb24uq5gSGqFxOSPcBlUepjq5Kktl2S9zUHKiEfgsuf3Xe8oJysC0ZKYk92IvoE18AUjWqmrQzlr4cChE5rKR2KHiDhMpjakpmXTtUQBO4HR9r7PU88vzO1Lt2nFvE5tZWnAd7RJKN81mDWA_pbc_PR2WP6uhCBXPxzXlXvKK2lMnjbfZXX1B4reQN4Ewdmip02DAvuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=DKht-ztE-UU4lnbeW0rhLVJw_LxdxgiNXD15APPy0w9Gv5uatPxA5sa8bUpnriXpG1wtYIUR_NAuN_92JX5VhSSfmMkX3eynY97K0u48_SDw2K8IPHRo_lPmFRcLTDNRHHuk7TXPidvnhIpH8H-uIbiV4EJOqrpQzhOF8u2kVR2MxN6SZY8z7kfQw7SXrMtqz6DxaK2q1QMwTExFbejdu53pXEyKiMHQZT0aJOTkSI0Fh5aNIK7kgStbOUzkKHCxgPsWV8qxETk7_7vQSnb4XO0OVOCz5kCkB8ko1z1X5PXkerjcLaIqTny99OcsDNtzC1i2PSVs_wl2jFV1Y5vtoUl62Wm1dOldWBU1NjyIUllr2x5OiofKzxXxRiHnBQg41w8zIGPmLpMxyLGwnuAA9nNQRQSgf9EZlt2b4PJvU0FlOivKhxxZNkqbxNVYZmud-CtIpSAsZD4hy0oeVzSi3fQCOMZhXzyj7XxI_CmiIXRUCEXciWCvZ622idbIaEG1pWz7zwSs7tPWOujRaNKz_iv80jwQn7MZEFtjdV4xQhvwlGGtKzzrL-1BdG0ojSaAMdFB7bs5x12ku29ztUiQhLA0loIrJfVGDm65c7d38E-CBg9a2T3X-KKBQJDrQgoftL9aWq284Q2qKqqN2qRxWYmDCUKzeZq-KmXs1bsXf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=DKht-ztE-UU4lnbeW0rhLVJw_LxdxgiNXD15APPy0w9Gv5uatPxA5sa8bUpnriXpG1wtYIUR_NAuN_92JX5VhSSfmMkX3eynY97K0u48_SDw2K8IPHRo_lPmFRcLTDNRHHuk7TXPidvnhIpH8H-uIbiV4EJOqrpQzhOF8u2kVR2MxN6SZY8z7kfQw7SXrMtqz6DxaK2q1QMwTExFbejdu53pXEyKiMHQZT0aJOTkSI0Fh5aNIK7kgStbOUzkKHCxgPsWV8qxETk7_7vQSnb4XO0OVOCz5kCkB8ko1z1X5PXkerjcLaIqTny99OcsDNtzC1i2PSVs_wl2jFV1Y5vtoUl62Wm1dOldWBU1NjyIUllr2x5OiofKzxXxRiHnBQg41w8zIGPmLpMxyLGwnuAA9nNQRQSgf9EZlt2b4PJvU0FlOivKhxxZNkqbxNVYZmud-CtIpSAsZD4hy0oeVzSi3fQCOMZhXzyj7XxI_CmiIXRUCEXciWCvZ622idbIaEG1pWz7zwSs7tPWOujRaNKz_iv80jwQn7MZEFtjdV4xQhvwlGGtKzzrL-1BdG0ojSaAMdFB7bs5x12ku29ztUiQhLA0loIrJfVGDm65c7d38E-CBg9a2T3X-KKBQJDrQgoftL9aWq284Q2qKqqN2qRxWYmDCUKzeZq-KmXs1bsXf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=l_btcotVq-5B0T7Lvlv2uiqe0ytzc65k1MxHGcWZbwvlwe7qXfCg7lXnXXcHAUwwf0QIgSmfh_Ytb99M2KQhG6t6NTPoUVS5RTHOrhRqrSOARsCPYD44JwCwkYzZeyTyw4eBPDgQIicHvRoxngVwuDSTQPF2i9jrYunChFsJ7yeehK1rdHE7NcUzWgx7Una6CYHxON3DfnUH_2-W8MMGk8ZG2gVQqIaJtGf_bKrsaLFn-sWLQW0TCzG6wupYqkWsJLsjkz34TKZWI4hjOFHDNJj9T9rREb8JS1vTRX8OyJ6OO-HCPgyluKNs-UmZ_0tAxFmUB4DjqC8Fp0JN-NLraA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=l_btcotVq-5B0T7Lvlv2uiqe0ytzc65k1MxHGcWZbwvlwe7qXfCg7lXnXXcHAUwwf0QIgSmfh_Ytb99M2KQhG6t6NTPoUVS5RTHOrhRqrSOARsCPYD44JwCwkYzZeyTyw4eBPDgQIicHvRoxngVwuDSTQPF2i9jrYunChFsJ7yeehK1rdHE7NcUzWgx7Una6CYHxON3DfnUH_2-W8MMGk8ZG2gVQqIaJtGf_bKrsaLFn-sWLQW0TCzG6wupYqkWsJLsjkz34TKZWI4hjOFHDNJj9T9rREb8JS1vTRX8OyJ6OO-HCPgyluKNs-UmZ_0tAxFmUB4DjqC8Fp0JN-NLraA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69898">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=otficuWyve8pLvFiD9JTYSYXQ3WzYoVht9TLeIqg6pH0tJZC0ChlOFQbi212UVQ9vD7vcVM_zZOZbej5Z6Dazs2E7SQGT8OqhvZ8Px2LlPXu6nfGp2_DzBkC-jh3vtNG12IcosRJJPfeqwL6kVXBX36FX0-KMiED1MhdK8D5eloluMHZpUqYLLRlL3NZLgtM4FH-ifly7mKGalWbeh2K_T56fV9F0MtI2leacMA9-QpDS0elv_Ap1xE5nbepbt8gwJCfpcsOUU0bhB2_KPeesxG9--8IVB-A5iNPM7nLBQoe4IiihY1TYUCOWlCMxaTlblRCGsiwiJ7j30tQS9PODg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=otficuWyve8pLvFiD9JTYSYXQ3WzYoVht9TLeIqg6pH0tJZC0ChlOFQbi212UVQ9vD7vcVM_zZOZbej5Z6Dazs2E7SQGT8OqhvZ8Px2LlPXu6nfGp2_DzBkC-jh3vtNG12IcosRJJPfeqwL6kVXBX36FX0-KMiED1MhdK8D5eloluMHZpUqYLLRlL3NZLgtM4FH-ifly7mKGalWbeh2K_T56fV9F0MtI2leacMA9-QpDS0elv_Ap1xE5nbepbt8gwJCfpcsOUU0bhB2_KPeesxG9--8IVB-A5iNPM7nLBQoe4IiihY1TYUCOWlCMxaTlblRCGsiwiJ7j30tQS9PODg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی تلاش کردند تا یک گروه بزرگ از خودروهای سبک را در یک نقطه تجمع، تقریباً 20 کیلومتر پشت خط مقدم در منطقه دونتسک، مستقر کنند.
همانطور که در اینجا مشاهده می‌شود، پهپادهای تهاجمی کوچک اوکراینی این گروه را مورد حمله قرار دادند و ضربات متعددی به آن وارد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69898" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69895">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=t4M76t5PNcuc1wWdABtFiFQw2q8uh9Y3fkJ4PG7M5caRPcPmBlHH2948UvHWcjkYzJY2yCssg4vnWipVLpFEMn56bBFkdY7zMC7zqUJg3sCYMKnj_9Tv-i2Jts6FXdGNHn-dS6xTx5l4AusRAGKvwAVRLmjoxabN0knBVPkWZXO4MNycBjyxSQrOZ9Mj49EvnUKLcyB7ydG0WbABK7FEaY3a8Y3pyZ1wNgIJdWty-Q29gxtym-cOLJuzVLxDqT1oKbM0QlT3_05RH27ovGwalDxtrmQCH1V4P9CcWOsBGNtVyLJU-RbP4YBZI6NV8hao8RKIZec6axVU6Be8wZOqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=t4M76t5PNcuc1wWdABtFiFQw2q8uh9Y3fkJ4PG7M5caRPcPmBlHH2948UvHWcjkYzJY2yCssg4vnWipVLpFEMn56bBFkdY7zMC7zqUJg3sCYMKnj_9Tv-i2Jts6FXdGNHn-dS6xTx5l4AusRAGKvwAVRLmjoxabN0knBVPkWZXO4MNycBjyxSQrOZ9Mj49EvnUKLcyB7ydG0WbABK7FEaY3a8Y3pyZ1wNgIJdWty-Q29gxtym-cOLJuzVLxDqT1oKbM0QlT3_05RH27ovGwalDxtrmQCH1V4P9CcWOsBGNtVyLJU-RbP4YBZI6NV8hao8RKIZec6axVU6Be8wZOqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سامانه‌های پدافند هوایی «اونجر» (Avenger) و رادارهای «سنتینل» (Sentinel) ارتش ایالات متحده در نزدیکی محل بازی گلف ترامپ مستقر شدند تا پوشش حفاظتی کوتاه‌بردی در برابر پهپادها، هواپیماها و موشک‌های کروز فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69895" target="_blank">📅 17:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69894">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=ahh94oMl2ZZ9DXS8b3na2ScABRtx9k6FuA-tY_s8Sb2LwTMd_oUE4_652OQe5bcpTytiL7zneGniYCkDeRCKa-YfwEIHFY1E4ZGHzV9U2UPVdCBBCiglMr8mxmoTXeIVJowM8ahzrSBSUTZPIuex7Uukza8xSIlHAq1VeHprjVQN_lqhZbKen4K7zMxeVvI103HaDP4jQtzBuSFlVXMI-WFDlnaMtMhnTHM9xdAouFQ-XsuDhHlXyqxMadFjW0ZmeYLZtSN_GhAMIstvesWzgH4utY2gV9s7NYHcbaJNokXiYc4o2-RXffa270noTSId3UviMLgKWLObXQREfjzPeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=ahh94oMl2ZZ9DXS8b3na2ScABRtx9k6FuA-tY_s8Sb2LwTMd_oUE4_652OQe5bcpTytiL7zneGniYCkDeRCKa-YfwEIHFY1E4ZGHzV9U2UPVdCBBCiglMr8mxmoTXeIVJowM8ahzrSBSUTZPIuex7Uukza8xSIlHAq1VeHprjVQN_lqhZbKen4K7zMxeVvI103HaDP4jQtzBuSFlVXMI-WFDlnaMtMhnTHM9xdAouFQ-XsuDhHlXyqxMadFjW0ZmeYLZtSN_GhAMIstvesWzgH4utY2gV9s7NYHcbaJNokXiYc4o2-RXffa270noTSId3UviMLgKWLObXQREfjzPeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیشب توی تهران، یه نفر با یه دست رانندگی میکرد و با یه دست فیلم سوپر میدید
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69894" target="_blank">📅 17:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69893">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUWPHXXVV_gzNhaF1R7afV0LgSB-j0r-Afm2grMrl9E5q0bqPLIPdAeu_lUTV8HfyJULkOT7eqnt3YMC7PxRzCZWh2_g0iwgvp-xAXp36kVOu6YUpwD9QHZ3dPprOu1s_jolTmDYecsDVdvT5LZG-_Qnnh8SuTpxxjQpOpvmOKPsvnYRV4NF4WoaTOKr1duaeYXGJay1WiQGFFZsyIPZk5jl4KJHM0g4Fg-92gx7oGjV4DdNSi1zWjkcUvgcEJpkGn0gLtEWy-JJbuH8rBkQgTpH3yQOG3RLi1K3enu5kG6jd6YNxmp88FD9zhmmMqdo4PsGXZEiKglzzNtMUVGPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال:نیروهای آمریکایی بامداد سه‌شنبه به سوی شناوری با پرچم پاناما آتش گشودند؛ این اقدام پس از آن صورت گرفت که شناور مذکور ظاهراً تلاش کرد محاصره دریایی بنادر ایران توسط آمریکا را بشکند.
پس از آنکه خدمه این شناور هشدارهای مکرر نیروهای مسئولِ اعمالِ محاصره را نادیده گرفتند، یک بالگرد نظامی آمریکایی سکان کشتی را هدف قرار داد.
خدمه شناور در حال تلاش برای انتقال به یک کشتی غیرنظامی دیگر مشاهده شدند.
در نهایت گزارش شد که هر ۱۷ خدمه کشتی در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69893" target="_blank">📅 16:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69892">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssuB2ooNjLJba12i8q138qq68E6IcDLEFKkS_VrS_Huha0w30N3hUC1_QP0v6YcVK47-qf4HucQlmYfqqilgANcBV35pqjF4tBY9uK-1veZ4Pqs3ITY2JyPgqv1-5-olS-bfvZ7rP8rzbPzqvGRZBD7LpaKMFLR3r6ItZDQ-vK5cgB5vrU8IzwVhx3AYii9EF8riqu01q1mWGeK-AWd8O4d---r2QQ-NSW47bG7vjEMxJ8Y_aDfPPtFydDet97jEJmEdaG6QUzkZkVTCNMu1xKJVhuBqUizM618vwahLjnc-mzt-zPaYg8TrIhPSyPp1kBv3jQn2OTVxF6c_eEGrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📚
#فوری
؛ زمان برگزاری کنکور مشخص شد!
صبح پنجشنبه ۲۹ مرداد : کنکور تجربی
عصر پنجشنبه ۲۹ مرداد : کنکور زبان و هنر
صبح جمعه ۳۰ مرداد : کنکور ریاضی و انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69892" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69891">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=Pl16_XqkhxOmk75Oc9RLAe0F2qQLpQnMPL_mKgVBc8KxYBY9_llHJ-mYC7_FRmHbFn4Tco7OqyHNtA8bmo2biKWg1b8WQ17ak62ulLmQITY9ehTlUQ5-LhNYfMtkxbmBbsmrYv1TSkYOJn4AsNaOtPOzAWVIaXHN4tyhIN-qjG4Mz7zMuk7_EM1Te3FjxBVX9CbpyC-DfmYlUOnXhCf71C46_YabVsJC9hI1GP1jAZkLa2Nx1E9P9Wlh0oE1wY70FpxaNHtlmmzc1ySjpOMvAHlWUpYmJnfPVyFu-tXy9mKxevPye9mGOc5118YdfNyLypUVjwBX3ZvwcFq0aWT1Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=Pl16_XqkhxOmk75Oc9RLAe0F2qQLpQnMPL_mKgVBc8KxYBY9_llHJ-mYC7_FRmHbFn4Tco7OqyHNtA8bmo2biKWg1b8WQ17ak62ulLmQITY9ehTlUQ5-LhNYfMtkxbmBbsmrYv1TSkYOJn4AsNaOtPOzAWVIaXHN4tyhIN-qjG4Mz7zMuk7_EM1Te3FjxBVX9CbpyC-DfmYlUOnXhCf71C46_YabVsJC9hI1GP1jAZkLa2Nx1E9P9Wlh0oE1wY70FpxaNHtlmmzc1ySjpOMvAHlWUpYmJnfPVyFu-tXy9mKxevPye9mGOc5118YdfNyLypUVjwBX3ZvwcFq0aWT1Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یه آخوند توی برنامه زنده داشت به اجرا نشدن قانون حجاب اعتراض میکرد و میگفت ملت بالای ۴هزار تا پیام دادن برام؛
بعدش گفت بزارید یکیشو رندوم براتون بخونم:
چیزی که خوند
😔
:
«آقای پفیوز احمق بیشعور حرف دهنتو بفهم»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69891" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69888">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=RuJPSqw3s1tuClMAj1FJ6TF7yXRiP6QI9plyvcMLDrKX2ijkJ_U-b35JsodC8_kUYCf6aQPtOVCs35KPIQAmwwQh2izfxbTJS3F8JFEnuZD-oQjzbrw74JmOjCMSjQcVSNK4xIu6MHl9KVDHeFzm7KO7KGjPYvOBe0xQYgh0_qkilOhYpLHccnRKYi1GA6-q5omxWXZ25Mo8k05ijQ6Ngn8GnN76qccqt1tQ_Z-hU7yQKXyQpA80_HuLwoZBfEH3HCf_Aw5j2AWUUFnB1jOPL1G27K0sfh90zGzGgtHQZet_1uKqrFdzr79d7BqCxexswRSu8FYtjialb2fAZ_0vlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=RuJPSqw3s1tuClMAj1FJ6TF7yXRiP6QI9plyvcMLDrKX2ijkJ_U-b35JsodC8_kUYCf6aQPtOVCs35KPIQAmwwQh2izfxbTJS3F8JFEnuZD-oQjzbrw74JmOjCMSjQcVSNK4xIu6MHl9KVDHeFzm7KO7KGjPYvOBe0xQYgh0_qkilOhYpLHccnRKYi1GA6-q5omxWXZ25Mo8k05ijQ6Ngn8GnN76qccqt1tQ_Z-hU7yQKXyQpA80_HuLwoZBfEH3HCf_Aw5j2AWUUFnB1jOPL1G27K0sfh90zGzGgtHQZet_1uKqrFdzr79d7BqCxexswRSu8FYtjialb2fAZ_0vlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه توی آخرین مصاحبه‌ش گفته رابطه‌ش با شروین حاجی‌پور یه اعتماد اشتباه بوده و این رابطه تموم شده.
بعد از این مصاحبه هم شروین یه موزیک منتشر کرده که خیلی‌ها معتقدن حال‌وهوای بعد از جدایی رو داره.
جالب اینجاست که اوایل رابطه‌شون شروین توی یکی از موزیک‌هاش گفته بود قراره تا به دنیا اومدن نوه‌هاشون کنار هم بمونن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69888" target="_blank">📅 15:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69887">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=QSkdiQLHWxCX4zw1Fr-MSjkQFZP2BpkMsTlCDWOxzb5SXR2TQlpmhQ8_0Nuep72SiDe_TOdM4IjuBUH8-sEcRpL2maNWsiw645YW58BoqBs7wr8LdOKReYD3ba33EZk5vVRlrYwKbzOyggZRJo-STo3Y6tKvQFfc4rQJBUXEu-8j5weQKpOeiC_LJ5LQ-mGwh5NEZTjJdlNBOw2-G51xlg9Kox8M2HEFimG2jPEhaNu70MWjeX_7VbHdFzl-ybHHjvYzoGCqdDbGbdEuaozpZFd0kABMfoWfaToibiKWzxc7ApBax6E0bMIzUSvPOTKJSJTTJzEorAUt2UmrUmdpKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=QSkdiQLHWxCX4zw1Fr-MSjkQFZP2BpkMsTlCDWOxzb5SXR2TQlpmhQ8_0Nuep72SiDe_TOdM4IjuBUH8-sEcRpL2maNWsiw645YW58BoqBs7wr8LdOKReYD3ba33EZk5vVRlrYwKbzOyggZRJo-STo3Y6tKvQFfc4rQJBUXEu-8j5weQKpOeiC_LJ5LQ-mGwh5NEZTjJdlNBOw2-G51xlg9Kox8M2HEFimG2jPEhaNu70MWjeX_7VbHdFzl-ybHHjvYzoGCqdDbGbdEuaozpZFd0kABMfoWfaToibiKWzxc7ApBax6E0bMIzUSvPOTKJSJTTJzEorAUt2UmrUmdpKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود هواپیمای F-18 بر روی ناو هواپیمابر در هوای بارانی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69887" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=I9rFzuUt82PO8Foyh11PiwSWVrvmXxw3201MXT5gtEdnf5rGX3M4_IbomxyU1mza5b_MHGwfGZBctsr7XvVzDx0IKGTVc97Ll9ANSsQ4yiFMltiGwYlR9OHhwAC-qAXx5KNOKUv9lvpfyd6NZYHjOnDGLqNlGoiwOiToTD_vZyPiXL08Ll5V7OvfVOEbOyAPzwGsrqMteNac9Nno9TEbnzAHybkGuWcnBaIDO3Nh6wcZXl5sJmo2lxE0t1iwPtugqWcm3xNbqwi9_fRlcBDscRzu9qjQluxPzfJo3AFx4b_6gXG1guYX9DMVR85o7GwQnNfigofumEEMVqQf7tgudg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=I9rFzuUt82PO8Foyh11PiwSWVrvmXxw3201MXT5gtEdnf5rGX3M4_IbomxyU1mza5b_MHGwfGZBctsr7XvVzDx0IKGTVc97Ll9ANSsQ4yiFMltiGwYlR9OHhwAC-qAXx5KNOKUv9lvpfyd6NZYHjOnDGLqNlGoiwOiToTD_vZyPiXL08Ll5V7OvfVOEbOyAPzwGsrqMteNac9Nno9TEbnzAHybkGuWcnBaIDO3Nh6wcZXl5sJmo2lxE0t1iwPtugqWcm3xNbqwi9_fRlcBDscRzu9qjQluxPzfJo3AFx4b_6gXG1guYX9DMVR85o7GwQnNfigofumEEMVqQf7tgudg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=rfndh86soboguEjftV8taIZ0Ae2HTsyVG4_7XRnxIuI4qDFrPv1F5YG-PMlUFyMYw6d3rmqCWG8CAiOMTde4_fEL7KC5TKRMvnYgILYU9vwAe_pPgpQTlgOQx3go8qlCjfYI5K0elZMwquUyEbxDVJevFVTnPOxmym0p72NckA_D3JwJktaU3GMBdWd7xKswP9sTAmNgiD7J2zOuhPiPSyVP8zb2e9xxIiYtKVZ0f6t9OYSVbx0nrA8nXLE8NorM6otHtdJRBNtfO2mYPWM_zd5erwPcGE_BxTAYS17_nvIcXdUAQhDLQkW2gZ6z7phSgzIfozP7AQBqRnBs4x18qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=rfndh86soboguEjftV8taIZ0Ae2HTsyVG4_7XRnxIuI4qDFrPv1F5YG-PMlUFyMYw6d3rmqCWG8CAiOMTde4_fEL7KC5TKRMvnYgILYU9vwAe_pPgpQTlgOQx3go8qlCjfYI5K0elZMwquUyEbxDVJevFVTnPOxmym0p72NckA_D3JwJktaU3GMBdWd7xKswP9sTAmNgiD7J2zOuhPiPSyVP8zb2e9xxIiYtKVZ0f6t9OYSVbx0nrA8nXLE8NorM6otHtdJRBNtfO2mYPWM_zd5erwPcGE_BxTAYS17_nvIcXdUAQhDLQkW2gZ6z7phSgzIfozP7AQBqRnBs4x18qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVK6eJPNG1oLUYd0qdw4Sng3BPEHvtt0A7AjcMMx1zauTuTr9ferEaoT5Mx0Q6zNdzv-_FU2X_t94rKdv0QYS0sSsIo2l_l2jutgSir3VA1go_ZdxPPGBFL5q7nz30BPAl1ACeR3MItpfp6asuhAAVS5TNoB6T4QGjJ8j8MCmLT-lK2WG0VTqBDbI0Qd3GA2uinC93_GHZu2ZD51HeOvUrOnEKHTNCOTK5sbkNYgBwaqYzr9CPC9hCQh3Ov8sWyDNcejs9IimvneU1Csm2OPhebrNFrlqVctcaBgLPZsqxpDSjzKfoLtylXt24BGf0q_dWjoD_R7zVOu3AAT7hO8lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=kzziaO6Wg1PNENNWRr10so2bVgpP1_U1LYxn2fsXoLIaYrviTu477L_X0WhYPkmeYBbkOkvCJVL1eoFdLuXZavuNHZbRuCoj7cN3R7_U63ZOChb1BALpn3mkelgEtUrGyMjb7RTqmS9O7TwyczjMbki4Yoj8CxdVFSf8VGktnioQBMxq-A9a36H1j-wAzunZBTsiNPyRAm06LgEwTQbF8KqovJDuIKSosrO_pxYsI5-lDoLHSrdFugFWnfN_dQ8S2-9W4xXsG98gjMI-LR7qkUiStpoYhE2Bod8fAdOD-CaWZsogMnqrp3zYs_D6RbVojqcbu25GqaiGHr-_FzChaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=kzziaO6Wg1PNENNWRr10so2bVgpP1_U1LYxn2fsXoLIaYrviTu477L_X0WhYPkmeYBbkOkvCJVL1eoFdLuXZavuNHZbRuCoj7cN3R7_U63ZOChb1BALpn3mkelgEtUrGyMjb7RTqmS9O7TwyczjMbki4Yoj8CxdVFSf8VGktnioQBMxq-A9a36H1j-wAzunZBTsiNPyRAm06LgEwTQbF8KqovJDuIKSosrO_pxYsI5-lDoLHSrdFugFWnfN_dQ8S2-9W4xXsG98gjMI-LR7qkUiStpoYhE2Bod8fAdOD-CaWZsogMnqrp3zYs_D6RbVojqcbu25GqaiGHr-_FzChaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=Qkqb9KMk_l7iWU9lqzsGEdrEvAvopI5RJtz1LJkVzGmN8mpGR3lQGVGZB4YG1Kv4zs6_XUzO8Qvd6U-MEtJplS6PPbjCGmqUJq0MJuuXyFW9HAZcU_xjBJTfsxrCmudt8_pF3C9Xo_jQOX5YXbjSi4QrUIIcbwof3xu6r38dko-K65Yssw7wGiNVZTtN7cXLPZrg7dUF1zicDP2qz7HBt6bL3r-I9GJXg_gTYRCg0a5P2JcLLX5u93ScT6a6JAw4yxgtRiYqbNZu9reU8IgJROJtRq3qW8-uUUPin7lpTQBO_8z5kb5qasXQynEBv-bGoKvAqoTbjb3OOZeB9cTmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=Qkqb9KMk_l7iWU9lqzsGEdrEvAvopI5RJtz1LJkVzGmN8mpGR3lQGVGZB4YG1Kv4zs6_XUzO8Qvd6U-MEtJplS6PPbjCGmqUJq0MJuuXyFW9HAZcU_xjBJTfsxrCmudt8_pF3C9Xo_jQOX5YXbjSi4QrUIIcbwof3xu6r38dko-K65Yssw7wGiNVZTtN7cXLPZrg7dUF1zicDP2qz7HBt6bL3r-I9GJXg_gTYRCg0a5P2JcLLX5u93ScT6a6JAw4yxgtRiYqbNZu9reU8IgJROJtRq3qW8-uUUPin7lpTQBO_8z5kb5qasXQynEBv-bGoKvAqoTbjb3OOZeB9cTmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=rEZsqez81aikZpyRC0p5SjXc0ck-SfOfRzNwo1tuiN4qLS3YPs8ArtTNxbpAwIbAV2R6FflC4pOYgIBtCGbGBAR9QJ2guJ9pzIhpJM-NwSQsUHpJOrK10gz6_Q6soVJr9fHNkU28Ad23xbZA9doDLtVamg70dI4n0HQ3Yi4KYeid30NnUjFNLrIlNlpIrea1aRIRTx0S6wKVKnctWmhvaMjNRqmwwCGLJHpdNelSDLCYpRm4Xv6FmUFKhlegqjiLjTF6LeQmaXRr6hi6C3rf3OY2EGHs-NkjsVI7SDocA-q3JNK7PQ4rESZOzxdMtuu-EmNIn6HesYSQYiLJcfwC5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=rEZsqez81aikZpyRC0p5SjXc0ck-SfOfRzNwo1tuiN4qLS3YPs8ArtTNxbpAwIbAV2R6FflC4pOYgIBtCGbGBAR9QJ2guJ9pzIhpJM-NwSQsUHpJOrK10gz6_Q6soVJr9fHNkU28Ad23xbZA9doDLtVamg70dI4n0HQ3Yi4KYeid30NnUjFNLrIlNlpIrea1aRIRTx0S6wKVKnctWmhvaMjNRqmwwCGLJHpdNelSDLCYpRm4Xv6FmUFKhlegqjiLjTF6LeQmaXRr6hi6C3rf3OY2EGHs-NkjsVI7SDocA-q3JNK7PQ4rESZOzxdMtuu-EmNIn6HesYSQYiLJcfwC5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=vwqyGOWC1XjmQF-2xJygGankrXeG8M40vqRw2Vw6V6HNtHhTGHw2ddQ3e439c60270G1MVKQmAfjTaCfVa05WvPDkgm1YYoRBt3xooXFmYqg69s7sKKnPKfYYEieksJ5DZiQgMAilNrH71jvdMO-OpUUJOYr2Si_Sb0CXp6h0oSVSUGG8AfvZvIOxE7-SMH85k8GiaB2_1KMtJUY4Y8g8OPjLcl8NiKhD4Y4uU_aZVDPte1EqqaL95nXtR0I6DvyT1i9PcNeN1kH6MZUTR0FCVyyKyHgYw5E7_VTApN_fcijniOvVLwCnwLWcVZVJSqvKobeGMYXqAaNJ3dsS24QVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=vwqyGOWC1XjmQF-2xJygGankrXeG8M40vqRw2Vw6V6HNtHhTGHw2ddQ3e439c60270G1MVKQmAfjTaCfVa05WvPDkgm1YYoRBt3xooXFmYqg69s7sKKnPKfYYEieksJ5DZiQgMAilNrH71jvdMO-OpUUJOYr2Si_Sb0CXp6h0oSVSUGG8AfvZvIOxE7-SMH85k8GiaB2_1KMtJUY4Y8g8OPjLcl8NiKhD4Y4uU_aZVDPte1EqqaL95nXtR0I6DvyT1i9PcNeN1kH6MZUTR0FCVyyKyHgYw5E7_VTApN_fcijniOvVLwCnwLWcVZVJSqvKobeGMYXqAaNJ3dsS24QVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
