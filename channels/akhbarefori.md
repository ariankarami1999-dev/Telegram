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
<img src="https://cdn4.telesco.pe/file/Zeyo_gw63NrJL-D2cnB-jjsLj0E_jYIiqwWYjV1n2lYABGDW4rHIMGYl9qsKaEcqQ_25sGlbMBvx0oVl5lpN70s3vg4bJrW2XNS4vk5wOYYo28qhH9mPx8JqkKchdvmZiF82rL1QzTpnDB-ISjmLBWEklv-DTHowhV-boUEo9VoDV6gq9n_ONI15HgudInbpRALQT3Aa9W8RV0hu3cUx8alCePVOphzIcPCMVK42ppU4Rss0V-MD5MCCFRu-lg2fYiOTbHnbTZS5MZAxHs6yuL2NFk-Ab7mysuOHa7dejp0NFyWjJxC2CzsEgzmljgxNGLN35Q0R1VYiWyORMqNVEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 12:02:17</div>
<hr>

<div class="tg-post" id="msg-672048">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dr7R3WM4XGK-kq40X6KuJgy4WFISQmMck9zRp9YaOrKW1omY1TUd-ZIJG5AWCeA8gtQBCLZcMp7v2rzU9KxIjcmmWN3am_9Pnb7RbNock2Z1Gy8V3t71XQotE-LQKZiXZAjfXj3OU0TceDN22AQgMXRNi5ZEf--owQ9aU3WBi02y-km-_sHrggZdyF5KC86mBCaoYpSUtjujOypLvuOZCH7nXNxB2CQ_DuAvLB5-e08NbUb9R-bVw3RhrmCYjt6OYv9s3nC6riZmBJcjj7Nlxt_PgIuQF0UEoOyVXntg1Jb_mUcr52ww9geS0ZgpQPJukPLyxI7SgmqJL5L47RWm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYM04zD5XPSIUZGr_ZjwfzoH37bXt4ZfIksjvLYd6kTQRJ9K8A93o3N_IUhyEYwtW2kyYd9UL9ZNP5JXRzkmluj7n5npKgrHC50GbA0dNn_lrDA9bG7lp8L94z7G_1NgmoKbDMfAuKTwOHIlJ1iP701suMtRDQcSBzcO2gVChtFx3WEeeB21ESgU7gGcAVY8xvo8XBj6iDv0FsyQHPJQgI5wyg4Kf7wy1hOm7tHkNlX6EZrpUWEWI20Xt8l1bLdxqQSSdnX-B0u_5CTGALDerJ00K7imrjo6YuigxMm7TQWZuMoLFO3jYEII4omwswlMWHjXVCE7pjCvbhApzYRjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0vtZrQIkzZa9ahfCOm6_w8srsqw4LhqFdPxcJrBUxSEggAu9VK0l7a9AzzhRMOQpFiyi9oBbnCGxhq0rjSEVGqEMJWScVVS_-lZzKhZzFv1Uv13nQU1ti5QNjh7N491XUliRMHftdoUC5hdWGtpLGEcM3a4PDphKpXDQLcYvQvdfOiEX7DHv_lzx6UHl7HmPvAJFLKjUa90Cv8e0tl4-peL4H2TH8fnJHfJQS1CqJW7-2lVJU2hEKpoV7WVvRkY1qjrmYlu8NLpuxG_YkqfSvF5CUZd62GRprYjuEbd4pPECrr2y4ns4TqSEaMx1-DXSqAmjiNzLGevwOGmF8n2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjjS71GHEWN_QtI-UmE2ap_AoFtzPUYp5Aj3_w88WGRCb682T1phRVdReSbQJjfQdDP_fF3k2I55AmdQexOd8cwVqjpANCFQms7UsvzD0qBFKAy5B3gxcmi6aWVvcseX_9PMVPyWTEUNGqUSdEq3LDK6Vu1wz2CGf7v5yqaT995wC0xzf4yiPFmZ22oQ2T9WiuQFeVpeNPqCzWDuZz62pa9m7I4_fyRjsbvZRWyZr3Q-V9CH9aEvHweY07C5occOyEFjGn3u-C6HpLPDtULftjWdayQhW3KDWSWPvl8cLthe9RaCNg1PxJGEL6id723N4fR-i02yWSchfe6eXosUwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زیبایی کوههای مریخيِ چابهارِ ایران
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/672048" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672047">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7965901c30.mp4?token=s-nukAFs72NGnK5ob1oLj6aiDG1o6KL4_eSxueDmTRShmMMxT2AHfKo2JHqN9WwMx-MDrK19sXsuV7P_sbd59vQqZ-ELc8CVx240lEIeWvIF51spz631oho86uHqngjtTDnUCHCMKmTnfOsVE4Y8VSZkJPjkbbQ6JS1yXts1Rfe3ksFXLT1D6K8SaTD3wwg7O8Xl-ZF_MU_i86brVNOT-wgD6j2IGdEC8gC6ADm6p_7sUS_9g56Ku_62E1wXAFQbAqtDgiB1nPbqBLDS-5MiFd-rw1RJT476f-XyML18fbcGesnu9YeyambrWCD0eX-pjajHn7NS-395-LWXCZFPgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7965901c30.mp4?token=s-nukAFs72NGnK5ob1oLj6aiDG1o6KL4_eSxueDmTRShmMMxT2AHfKo2JHqN9WwMx-MDrK19sXsuV7P_sbd59vQqZ-ELc8CVx240lEIeWvIF51spz631oho86uHqngjtTDnUCHCMKmTnfOsVE4Y8VSZkJPjkbbQ6JS1yXts1Rfe3ksFXLT1D6K8SaTD3wwg7O8Xl-ZF_MU_i86brVNOT-wgD6j2IGdEC8gC6ADm6p_7sUS_9g56Ku_62E1wXAFQbAqtDgiB1nPbqBLDS-5MiFd-rw1RJT476f-XyML18fbcGesnu9YeyambrWCD0eX-pjajHn7NS-395-LWXCZFPgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امنیت خونه و محل کارت رو همیشه زیر نظر داشته باش!
🎥
💡
دوربین مداربسته لامپی V380؛ یک دوربین هوشمند در ظاهر یک لامپ معمولی!
✅
نصب آسان بدون نیاز به سیم‌کشی پیچیده
✅
اتصال به وای‌فای و مشاهده تصاویر با موبایل
✅
مناسب منزل، مغازه، دفتر کار و پارکینگ
✅
دید بهتر برای کنترل محیط در هر زمان
✅
طراحی لامپی و کم‌جا، بدون اشغال فضای اضافی
🏠
با این دوربین، هر لحظه از محیط اطرافت باخبر باش!
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۱,۷۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
همین حالا سفارش بده و امنیت محیطت رو بیشتر کن.
http://memarket24.ir/briefcart/180124/g-en50734</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/akhbarefori/672047" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672046">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
♦️
سپاه: سکو و موشک‌های هی‌مارس در کویت و محل استقرار نیروهای آمریکایی و ضدانقلاب درهم‌کوبیده شدند
🔹
در تداوم عملیات مقابله به مثل و پاسخ به جنایات جنگی شب گذشته، رزمندگان غیور نیروی زمینی سپاه در موج ۱۵ عملیات نصر ۲ با رمز مبارک "یامهدی ادرکنی" علاوه بر انهدام سکو و موشک‌های هی‌مارس در کویت، طی یک عملیات ضربتی پهپادی و موشکی چندین محل استقرار نیروهای آمریکایی و ضدانقلاب مزدور آمریکا و اسرائیل را درهم کوبیدند و تعداد زیادی از ضد انقلابیون و نیروهای ویژه آمریکایی را به درک واصل کردند. عملیات مقابله به مثل ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/672046" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672045">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw6Ks5DTIG3ibACpHCoertmTSyaJJj7hm_Dx0dXki9KqzBr_dxVhYycAtZXNy9HLjRZzmcFVXKgNYIAZWmZv0isr20q4MJHlXwZZD6DCvMufkOy8sTLJHQOz46P6pXt_7t5M8kwnPZjgtIoTBoyf94SCgj9lZfHcsuIwAAK_-qkBNOmycZk4UObYp956nswmGKOZ7s4_ORvR08jftAe5qv7JvWDFTYEUNsFGmlQWjjFdQKxOoJSS9Sxq8H60Weyd2ecDBSLo7XdMG1EB-0l_g6zcDzl1I_OpIWJOO0eO_FTJaghRb3J399_sprL-0ggELR9QgAvzbWWW0NZiJPfQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر توییتر: آمریکا شب گذشته وقت خود را صرف بمباران پل‌ها، بیمارستان‌ها و نیروگاه‌های برق در ایران کرد
🔹
در تهران باید این پرسش مطرح شود که چرا این پل هنوز پابرجاست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/672045" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672044">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mgfqhw1qyNVnB7_eRwJ6CqKUZ6u64-QOakqUM2FcY4BxWSpOvkzrZAHp1yDALMsBGvTVRpP74IMJywEToVyq_9kNhIxA8JkDgpWRVd0kk1HpFXnAAU58VAhz4jCJ0B5wDhVW-WhAXkPEHkkOeI9KRIM3rn7__EBh0sBuhfhNatcANKt27MhOmJWI59IV8K4WArRW6x3YOpAb_rBhjHpRPB_Trup17gGKJSKM1HjbQViGmbuJC9-SrfwKsF_gw4FETImMQy-RGqHQzwnFwW5fx9JQfpHRM705btdvuQrPt7pYlQym-mzEuNzx2eIcCefH0bWLsadqO5tnVi8k7k8p_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای: تخریب سه ساختمان در شهر نظامی زاید ابوظبی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/672044" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672043">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9321113987.mp4?token=T4rnJG_bP6Q-5wjwFxiemjSG3oTvd5pbHy3ckiH1kUGxHYjfiAXGmvaB48ZQNKpD5n1wQaCe8eiLNzDmPugkjj1aqV1yBoVs3Zs77eBvTZTH395f4n-ITwdo00ztG3s8Pb-8bHAtPg8IQHIvIeM7ED71TAZzK0OlU1IDjq3UaBxJLzsSY7HqZV9ulXCfvJZ4sgn2URsdH3ZwyWEgpuMg9Zu8RaeWd3j8BXx-7d6WvCSqpmwc7pmSbiSslr7FniR4_TmzqP0QVPLWriy_EBK4DFwju1XAPAlZWWG368FRDAcHPI2GVSJygeEOBs39ypVrHV4yoW0JvjrC0UbsMbJ82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9321113987.mp4?token=T4rnJG_bP6Q-5wjwFxiemjSG3oTvd5pbHy3ckiH1kUGxHYjfiAXGmvaB48ZQNKpD5n1wQaCe8eiLNzDmPugkjj1aqV1yBoVs3Zs77eBvTZTH395f4n-ITwdo00ztG3s8Pb-8bHAtPg8IQHIvIeM7ED71TAZzK0OlU1IDjq3UaBxJLzsSY7HqZV9ulXCfvJZ4sgn2URsdH3ZwyWEgpuMg9Zu8RaeWd3j8BXx-7d6WvCSqpmwc7pmSbiSslr7FniR4_TmzqP0QVPLWriy_EBK4DFwju1XAPAlZWWG368FRDAcHPI2GVSJygeEOBs39ypVrHV4yoW0JvjrC0UbsMbJ82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از اصابت به سامانه پاتریوت آمریکا در نزدیکی اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/672043" target="_blank">📅 11:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672042">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سپاه پاسداران: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن را هدف قرار دادیم  روابط عمومی سپاه پاسداران:
🔹
در واکنش به حمله اخیر آمریکا به زیرساخت‌های بندرعباس، در «عملیات نصر ۲»، پایگاه‌های هوایی آمریکا در اردن را با موشک‌های بالستیک و پهپاد هدف قرار داده…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/672042" target="_blank">📅 11:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672041">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سپاه پاسداران: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن را هدف قرار دادیم
روابط عمومی سپاه پاسداران:
🔹
در واکنش به حمله اخیر آمریکا به زیرساخت‌های بندرعباس، در «عملیات نصر ۲»، پایگاه‌های هوایی آمریکا در اردن را با موشک‌های بالستیک و پهپاد هدف قرار داده و چندین جنگنده و سوخت‌رسان آمریکایی را منهدم کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/672041" target="_blank">📅 11:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672040">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
‏ خوک زرد: باید مجوز فعالیت شبکه‌های تلویزیونی که سخنرانی‌های من را پخش نمی‌کنند، باطل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/672040" target="_blank">📅 11:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672039">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
راهپیمایی عظیم شهروندان یمنی در صعده
🔹
همزمان با اوج‌گیری تنش‌ها در منطقه و تشدید حملات ائتلاف آمریکایی سعودی به خاک یمن، شهر صعده امروز راهپیمایی باشکوهی برگزار کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/672039" target="_blank">📅 11:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672038">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
قیمت بلیت اتوبوس‌های اربعین اعلام شد
مسیر تهران ـ مهران
🔹
اتوبوس ۴۴ نفره؛ ۱۲۵۰ هزارتومان
🔹
۳۲ نفره؛ ۱۷۰۰هزارتومان
🔹
۲۵ تا ۲۷ نفره؛ ۲۲۰۰ هزارتومان
مسیر تهران ـ شلمچه
🔹
اتوبوس ۴۴ نفره؛ ۱۳۵۰ هزارتومان
🔹
۳۲ نفره؛ ۱۸۵۰ هزارتومان
🔹
۲۵ تا ۲۷ نفره؛  ۲۳۵۰ هزارتومان
مسیر تهران ـ خسروی
🔹
اتوبوس ۴۴ نفره؛ ۱۱۰۰ هزارتومان
🔹
۳۲ نفره؛ ۱۵۵۰ هزارتومان
🔹
۲۵ تا ۲۷ نفره؛  ۱۹۵۰ هزارتومان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/672038" target="_blank">📅 11:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672037">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0cedef3b.mp4?token=s6RSaBDZ10LohfPjKSZBOp9FTXwxSD2LOAPxGiVFRRWts17QjXhvOodiC9WF1HpjH0Q2Tl_nRiWM5GpT-GSYG8KyXP9-b_Ve3S6DZ_3y8xp6DPMtfPBPGL7IYxkZYV-_nm0W63SYyHVHfWgkVDZx3mxTOAVHp6lb7N3VQv0gq6TXjFb4KONS7nSr8MOQryDDsJ4J98EfO1I64yYVdaD2f9ZJ92mfVZyC3C73RC5hjVrgTXG0FLgkwyF7yp9SqzFSOfZGtmEseRos7Gg88ceK4GpHtTQLp8w8P8BMSlks9aZIy1kbBPYFpgbdLHzjEuqiV9Sa2ualk7C5nF6gG9Uznig5jxop_148KIbdb68ZI27F89BHeuGKHK_CJF7ZjZuoH21lDdgVFegaLKg4unKxehJ8ofXayrnypndhJ0BJcD5nRaGHyyW7ZQbghLySJQJmhs1Jiroy_OawEBKNgRlNO1BMr8gjlCb3l4Osu_eb8DQXVGwlvqWbIBMEjMMvoOo1HQ7WVO1Tku0T62LER2UYUFo31Jmpjq8wLobBkL2N3hTKB9U77ipzqOdOzT_28vXj68rER966JAAfE92C80_Bf6Mbq5nPg7LbgtdkGb2xSm3JX6g3EBWgsDyovnCGThYIHXBBiK41sb4JlF6EXunBiNi-kVnkJgC69M3sgcByAec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0cedef3b.mp4?token=s6RSaBDZ10LohfPjKSZBOp9FTXwxSD2LOAPxGiVFRRWts17QjXhvOodiC9WF1HpjH0Q2Tl_nRiWM5GpT-GSYG8KyXP9-b_Ve3S6DZ_3y8xp6DPMtfPBPGL7IYxkZYV-_nm0W63SYyHVHfWgkVDZx3mxTOAVHp6lb7N3VQv0gq6TXjFb4KONS7nSr8MOQryDDsJ4J98EfO1I64yYVdaD2f9ZJ92mfVZyC3C73RC5hjVrgTXG0FLgkwyF7yp9SqzFSOfZGtmEseRos7Gg88ceK4GpHtTQLp8w8P8BMSlks9aZIy1kbBPYFpgbdLHzjEuqiV9Sa2ualk7C5nF6gG9Uznig5jxop_148KIbdb68ZI27F89BHeuGKHK_CJF7ZjZuoH21lDdgVFegaLKg4unKxehJ8ofXayrnypndhJ0BJcD5nRaGHyyW7ZQbghLySJQJmhs1Jiroy_OawEBKNgRlNO1BMr8gjlCb3l4Osu_eb8DQXVGwlvqWbIBMEjMMvoOo1HQ7WVO1Tku0T62LER2UYUFo31Jmpjq8wLobBkL2N3hTKB9U77ipzqOdOzT_28vXj68rER966JAAfE92C80_Bf6Mbq5nPg7LbgtdkGb2xSm3JX6g3EBWgsDyovnCGThYIHXBBiK41sb4JlF6EXunBiNi-kVnkJgC69M3sgcByAec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه فیک را از اصل تشخیص دهیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/672037" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672033">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kU66h9au4Dmq5VGpMjuqfTEzWJjj91Q9FH-s85cHAuPC5JeOFkG7sm9p0ZJksBkEW1xwGKykhU2CcsmNzRFFPs5VnXwX3CETPCG022Xtsy1u8GewmdkeWVqCAbSML13JjKZsvWmPVNGsy_de11Sl8W37wfYnK-DUpi15UWjeRvPzpZoV5ffNk4iP2Nb8IjPkxTuSzwz8Z2p29yAafN6uqhtEzhoCun8oVnK9siviu6NS-wz5WKWQE18gmkU28ax7IpHNz4iVhDA3_YWamsv4Jy_u1IuQ9r4fnV5SdIpxiJr_QUYgi40bTfAS5FpG7mdZGvFZ4_b-Q6uifyh8_I-FtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYdnfLLa9LtwFVxDMm-c5GWuEPF8oeEwKNcimv6kSXwDYlRse2hwCST0nsTHlYV4k8xVYPUZbO8rEi5fXemf2dZl_dTLgoh3lUDXxG_JyWvXMOnFGv9-f9-KWSR5X_5tt1q1EIu12fjqaMd7drKe6CFbKDfl7rFTjstTkZ-exiwW5m_W9gtkD2fMaGVKxxG8ER17b6MaLAsrD8wvptJAY3sKOP_A9_8hx0BTJIUg4Xp6pY2DsUiK0t5HZbvOe_f6xnNbMBVZ36E630EorWbqeD7vbuSftOx-fC7t_RRcFrWpfkc7vBGCda1X-xr_XcyNdnDilib_vA0-thYCh-YrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4Uvtu1E5WL-r7uUyw0G7r3WhwEw7q8Sik_Ls-7B6GstkY6J_FW_65ojy2rXWH1KfjHjlDy6O6o4HbJg67o94ROZu7qQOJKPZu1CwVvCpk5TdBfix97-KIagov2qUSVJs3CgwQbUmauJC81ZSMCY2SrEmYQfhJ6z1ChKhfo3PkYf84w8s8j80sK_tRJcFJVxSPsLPgvMoysevA92g449YSVxzD0WMFy8EYxOHXQ9iMt8t4P8aPVV5aKPlW5zidbLTaXCOjx291licDZFgSsNdwMaCbyzaawbCebX-ISDntj-D7bFoGxtZ8m8R_xMsr0jAa8fo58HvhHxiHsQF2VF1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4e6qTOoDBmegQGgYZPK9OnCIlonXdG-04xvdWshIYKODla7UIkPbEjq91VA7QnEdI23Ls8NtCfm_S7nxN9OdPWgRVNEUN2ACMmSghUbucTD_H4XCtUtw60N1mAHij03nfef-k3Gl4yn_pWiVVQIm2XCnqe54BAJIdNQzixidQuZw_hqKDKJqJpCNGaJJMbCcBPmSYeb_0RUGnOoe-3ajKCO9eVXmhqDooHHcvH_hZrBcve64ayVnKhZWieNMDMIfAb2CfgUMwjiRoXQ2kh4h-fCxEaxgs_4kmdbcfmiLzTWGH2vPhiltpjqSfIahtmPQLvDI_1ZCxJm7eOUZ1tIGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افزایش پروازهای نظامی آمریکا به
غرب آسیا
🔹
داده‌های منابع باز (OSINT) از اعزام دست‌کم ۱۰ هواپیمای ترابری C-17A از آلمان به پایگاه‌های آمریکا در خاورمیانه خبر می‌دهند؛ هواپیماهای اطلاعاتی و سوخت‌رسان نیز در حال حرکت به این منطقه‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/672033" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672032">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تجاوز زمینی صهیونیست‌ها به جنوب سوریه
🔹
نظامیان اسرائیلی متشکل از چند خودروی نظامی وارد روستاهای «معریه» و  «عابدین» در حومه استان درعا در جنوب سوریه شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/672032" target="_blank">📅 10:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672031">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
به کدام نقطه راه آهن بندرعباس حمله شده است؟
🔹
ایستگاه انشعاب ۱۰ کیلومتری غرب بندرعباس واقع شده و محل انشعاب ریل به خط مسافری و باری، اسکله شهید رجایی و راه آهن بندرعباس است./ صداوسیما  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/672031" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672030">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7GAZInypPYfZXkkC95iZVJG7GQqhjucVOuTeoCIzPA3yFvvs_O9SLwgKzYCcHOnd1cT6KvN7w_Q_MffWnsgcban-SE2I3IuJTl42Dj89oTdmfR0XYLS8qwoophgtIEHThF4FIqKPOlthDRbzIHcGLpnvAcwavObNqk_8M-21sbmgfIm6DVa3fbC4Ae9UvNIEIAhZEJhlVnIf3glcUMofgpdaGrq3cdC2aBY9u2kea-jHVPGYnqvqcL7LslMnZtfmJUIX20GgFU3YkuSGEmKN9Mr_FbiYLElK6PHH0-nTLqa6zQUMs10CbImWcMbtPKyKqco7wWX9MX36PEDCSg1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن شهید شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/672030" target="_blank">📅 10:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672029">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ایکس درآمد بازدید پست‌های کپی را به سازنده اصلی می‌دهد
🔹
این پلتفرم با استفاده از هوش مصنوعی «گروک»، مانع کسب درآمد بازنشرکنندگان از محتوای دیگران می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/672029" target="_blank">📅 10:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672028">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پکن ادعای ترامپ درباره مداخله در انتخابات آمریکا را رد کرد
🔹
هاآرتص: هژمونی آمریکا و دوران نتانیاهو به پایان رسیده است
🔹
پاکستان و چین خواستار از سرگیری مذاکرات بین آمریکا و ایران شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/672028" target="_blank">📅 10:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672025">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
حمله به نفتکش در شرق خصب؛ خسارت ساختاری به بدنه و سلامت خدمه
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از حمله به یک نفتکش در شرق بندر خصب عمان خبر داد که منجر به آسیب ساختاری شد؛ تمامی خدمه در سلامت هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672025" target="_blank">📅 10:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672023">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e619c6daa5.mp4?token=Y2RZnsilN0mB7pjS9tXM2mmZaBD1gxS87cjMhgAMDqiDhLuh6d4lB8HJhppdM9jEh9Se71Bz1mOmvNOgicQaZp5qU4VpWV4bopHRx1UduozdS1YqUniQB5QtgJDoxRBKWhKIikyeVzLngccWHDCdvZC9H8eCWY_N9v9FUH09x9bulb7hH3ZJ8HDmidP3b1dtpPQsr8NLM4YVr6OL-UktT5zb1D1UfjKe8jVWdkzovIur-F3-bY3QKT5PwILdJ_B82uzT8K1iL2jpC9lE9DUW30Szv4tIsxkO2l7wzFBsTkrABfjNnSW7D9tbAeyq84KBCKl8QjqIuyUGrTVjb8r8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e619c6daa5.mp4?token=Y2RZnsilN0mB7pjS9tXM2mmZaBD1gxS87cjMhgAMDqiDhLuh6d4lB8HJhppdM9jEh9Se71Bz1mOmvNOgicQaZp5qU4VpWV4bopHRx1UduozdS1YqUniQB5QtgJDoxRBKWhKIikyeVzLngccWHDCdvZC9H8eCWY_N9v9FUH09x9bulb7hH3ZJ8HDmidP3b1dtpPQsr8NLM4YVr6OL-UktT5zb1D1UfjKe8jVWdkzovIur-F3-bY3QKT5PwILdJ_B82uzT8K1iL2jpC9lE9DUW30Szv4tIsxkO2l7wzFBsTkrABfjNnSW7D9tbAeyq84KBCKl8QjqIuyUGrTVjb8r8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلودگی شدید هوا در نیویورک بر اثر دود جنگل‌های کانادا
🔹
دود ناشی از آتش‌سوزی‌های گسترده جنگلی در کانادا آسمان شهر نیویورک را در آستانه فینال جام جهانی پوشاند و کیفیت هوا را به شدت کاهش داد.
🔹
رسانه‌ها با اشاره به غلظت بالای دود گزارش دادند که تنفس در این شرایط «معادل کشیدن ۱۰ نخ سیگار» توصیف شده است. این دود پس از دربرگرفتن بخش‌هایی از کانادا، به شمال‌ شرق آمریکا نیز گسترش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/672023" target="_blank">📅 10:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672022">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaDm_XFydquA72RPeLIjzH8IlkQ-1DJ6-x_GzMr8A2g9kok-wRej0QPxH-T01oviP7C4Pw59I0tgYnIhW88UYakk1bAqPYsXpbN_-Y8t9JPhmhAv9tSvKuO-vhZSR0nKpXUp4E5iKjxB_oecpzBxxz1gac8qwoV48J5jCvfATEh55hKax-IdY4rUwLfF1f5Ft5bzLjqXZjeKcrIGMWXpGHYUnZiw6gJ2V_swKw6PTIubcCbdpbK13A-xQMEAQuZm0uTnW0GVRUQKaoVwoEH77dpEXEj4JezwZ-1RUaFCEcKP7PbrrkXocZcNvaDOG62acsLE4vWs8s6C9y_NY5nnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شب‌نشینی ماه و زهره در آسمان امشب ایران
🔹
ماه از غروب امشب در کنار پرنورترین سیارۀ آسمان یعنی زهره، مقارنه‌ای را با یکدیگر خواهند داشت که در آن تقریباً ۲.۶ درجه از هم فاصله دارند.
🔹
این مقارنه از حدود ۱۵ تا ۲۰ دقیقه پس‌ از غروب خورشید تا ساعت ۲۱ در قابل دیدن است و ستاره قلب‌الاسد را نیز می‌توان درست کمی پایین‌تر از ماه و زهره دید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/672022" target="_blank">📅 10:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672021">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
هشت شهید و ۲۰ مجروح، در حملات دیشب آمریکا به زیرساخت‌های برخی استان‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/672021" target="_blank">📅 10:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672020">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufITZQWwVuQq1uTsW6dLDEB9Qya9Twm0l2VMQVWeQq-JwBV8vM2AXfAe1zvoXY2ygo2ZDD8d8gmXV7hcZNJ5YryV6YSEy-PTZC0FdzH_fREi1jkQo9LTFRlfTWCnqjLtRV_5uns6fx7UXhprm4i3iBl-w_eaIjfkoYsovus7qTKMLMESRUbw9TyW5EzYHwpRYecN3A_bm8oKbS83zhP_s-l2tyTxg0jC4XqG0wltuvWJYKj0MPsUnAFW_RwLEXLj552_RiwXvf8FgkW5uICo6VEIUpvNZnEepLxqpOuOWAZ7m_oZJtk6k7BpBrtYGpVO6BMgW0vPlLGw7X9EbuoRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما نفت کش تصرف کنید
ما جزایر قبلی مونُ رو ان شاالله</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/672020" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672019">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hll5YJhHLfeRHaB3G-bW7CYp_TdGhEPKpipy8Y0kpo_vK_say0VkkfEoV0kbG8haOTjvBZRmKhqlIgkn1zkO8hqeTFDAy1JYclJ8aWr6IlObT8d4JR1YsQPm0jxTIQRnNYSkijI_4MwPD0qH8zy8S6rEihLoSIRtB2h-59-XFuHRP6oe4leFY3sxNkcn01nYyQayw8GCPkcQdUih60-ESJ8yo5w72x0p7Egse323Bg_vNObOmyjZy9eWjqBfgOKreGZmQ6GKfwBStMQd6APgtSDWF5bP0_98bixW8qKcdzIiBiQ8ADDsnZb1SdbcnMzeOsf6h_CxLGTcMHRMy66aQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش رئیس کمیسیون امنیت ملی مجلس به حملات به جنوب کشور: روزگارتان را سیاه می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/672019" target="_blank">📅 10:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672018">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaQdHXeZfB8Q6OOI2-QSha_5TfFe0J-vOMjiIBSoilLoL3ugnbdEPYWyL8Mf6MGoSi86TuZr_UR-f28afzMTNeAgQMieudTT-H0ApvcXGfP8OhSAbmO3g4CWHIN80f9AY4zGscS7tIbn6D2gE4qhp63ompZ3J5MHF8MNAhXFoLFVw5gf_KTDxe64P-_4yjf3zAZV8fmaY11Jznx6bSYOs1zSaDWMBfXsGSJJdJ32aA28G4syRcRD8bSiusNKcd6nuNFWh5gj2eNWb2pAaxNlw68iEgnbE8SlSX0KlgHFwNAE_DIlwHkQcOSxodPjHbv61KTlxLHnavbodt0WKcsp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدیه ویژه فیفا به قهرمان جام جهانی
🔹
برای نخستین‌بار در تاریخ، قهرمان جام جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود و انگشترهایی با تعداد محدود هم برای هواداران در سراسر جهان عرضه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/672018" target="_blank">📅 09:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672017">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حمله مجدد جنگنده‌های آمریکایی به برج مراقبت دریایی چابهار
🔹
صبح امروز ۳ انفجار شدید باعث وحشت مردم منطقه شد، اما منطقه مورد انفجار مشخص نبود. جنگنده‌های ارتش متخاصم آمریکا ‌برای سومین بار طی روزهای اخیر، برج‌ مراقبت دریایی بندر چابهار را با شلیک سه موشک هدف قرار دادند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/672017" target="_blank">📅 09:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672016">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfv7sQSJgi24bFbSzaaJahTBOHef1mDBD_Hk0o78Dj7BLFontpUohlBL_iMBCnsHj7Tb4DFoTYYGL552qfPUXnmtrJ0qYGg4yJzHvtcYth88McsUzFAxmY4nXhsdugiXMYJRk8ouqyNRt7FmzH3EycoASpiKIXgd4etRuCRqNhWx-md1z7T88B9xa265pNZwZZbDkbOclbJRTCzTAZM_JVa1wSv5Pj5WUeb2WPoamsuOEa6WVGlKHCpUSvsnWinBV_pFCcbFLcZA8kNu0W-z52v6ItsDFNgfDWrTNfCICpNWgc5yP5SOD8us8ZvWN_WKqXoYu_Mxl9i4zsWLNslgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط قیمت طلا به زیر ۴۰۰۰ دلار
🔹
قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۲ درصد کاهش، به ۳۹۸۸ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/672016" target="_blank">📅 09:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672010">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6lFLE4ThOL2uolHdoVCVbaCL0E3cwdIWTPhCkOsQ5W_aBRhVIqGvGF3erLDa1YNJJ6UJwQ3_yFRwtqyu-Nip5Tkc-WFoT9A5DyyHx9i75CJlGRcjvinohOnFBM_fd6TML4k7LkoCm68fLZ7_q8oGSDETYNUtSSXWd6wrgIE8yELKlPlZTLPIAXhdcpfhzPypQIjWp5sTbsR5UHrxkDUCC2RaS__bRRGLGLK7fbk3ZidEKDdVsCiZpXladBOy_ApevYcCcnFURyeA_P0VBCbzzBIJh-m4E9gxL68YIzFW_BWN7jto90SWp8PtF6FAvwqBv6O3LWPAFJhf8b4ujmr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHYxEShxjQUeumfPSh3TVSi2pMZPnLql2oAliCvLrYPCfas4qs38abf1KZL1-LVhulohfqISVmAQHLNd5EyJrtXV12htdQnOiUUajMVcK0s3_-hWvc3cpn1YTsGoH1TQs-JPhrPljPPzomRb936aTZh5gZa7SsNOuSi8WrU3YOSstOK5-XILuzl2KruoEIebSxzTyCIIwWOlRc_KweR_Z4JaY2O1mRFE4wR3TPbbga3mFpTACD3z4eW9Zh-WAcpzzt70E6Rab9-sDPGgsuT9F8JDs4U4AfCvG_Og-4L6HhK5PMYJF7D-tbn3bIcE_Ve3t2F4lCuXrpa7__4GSvrMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPIofuAMUqU2pFYZHHovNZv6kjlrXZ-3Px6jc6FXCWpl1gEuBZo6JqPrBK98z6vF_39tlKXLcEtEjxHiduXT46vUCNxyseqc_HXUwo1l2Zww2O42Y0O7GFjlNrMdDLW9kNB36QAEl03nQWhlJ2ibKPcagIM1HaiSgzMYOYwETTmLs6d2ota3VjXog2O4vClJ2bAXqpN3fAUqSZlk-1150ItIMesmf4iBIDJ2vJSFIQ_7eQNNlb6hLmAVyxB-wevMiO7HsAVbx4ZeFeIce1P94mA771-lO4sebkxeB0iG0i2xH7lbIdF4VfMSuVxGti5vUd3f2F7BI_4jTUYB1-l3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOoAGLF2F-tloruCVl_QH37Vpf0bvmmvjdVQp_NuQZn2ZG0jRw5vG1WU99ONL3tgmHNC8ute8DytHeKNDqukhpJyewH3uqC_vK2WrNulLd97FLsmShlAPSyStjWyXOFmXyJfzfdN9NaF4ck5fbpR0KdVUYqRTU0kU-0pQFdgahD9qzrh1uZEJZ9SIhc9s3kXLmirLPzBI2AQICeLelmCgxQqy4BfEQcvc0vFQBXz79X6BNyapUL7UCJ-5eBQqFjpPaC1urvb6zhIlUvbH66foxZ1OQdShHaaRm1Z3WZ_PqmoWEdqRkifQKGsf8kwi8Im6mFj7xvw8prDvgPDje6gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcfEwaH_eurUs33M67jt9yMZEKxOc7RLrs0gWk21qWs-f53I5XRjDLGGnKs1NJPpsJHVsuhmReauY4c89TTcA2FzZyDcdQPaXa8GJaUQFjW_xMb7zdxK8qx-kJIo_S4t_3R9D4zzUcVqEJYNm99TL0pfkcmvvS7pAZFneHWhNedsX90G4jn_K-rQxzwloLQHUjAEBpjECfgleZOHY3xSjMLG56nC3nKLyvhKJrHeh94aF2kh63vbIUU5yapYY26jfIa4zPgTMaO0gohoOoQCf8ovJsTxoY1zePN4eKyhRPG-OKNAVGm9etYKHxi1LxJllPQIbTvVWvQ3EXEIkIThhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/husns5CDeT0exdyrpbmFECj7YysYmev2p5jr8pc0onv_lm4pWkCZ9Zdb-A4OJygnMeGbkPRoQgpyh3KyTybmLVQecisJYZfCrHVk8nqPzLRXBIfBgp6rfpFVhwsSKYPwWfkYRM-SdOKRTMadqqAmm8qbk7V5NfQzmJJTPXWJDvQp8DIztXSlNQCtqAuopH_yN05iVxZVocaXU0P_JltiW6URT0js7ctYMuDbBPSiYcmbGRzJRn7ujf3S84-_fDY2hy19LLR5uEtXeDpb6C3fCuRkUqRfMh5JG3erUMMhDJqMIpSGkY_JJ_f93Fqxuu1qBhYlfzVNabzCcnMHS5RK4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۰۰ ایده خوشمزه آشپزی که شما را از تکرار غذاهای همیشگی نجات می‌دهد
🍽
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/672010" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672009">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پایگاه دشمن در کویت در پاسخ به جنایت ارتش آمریکا، در به شهادت رساندن مردم غیرنظامی به آتش کشیده شد  سپاه پاسداران:
🔹
شیطان بزرگ، شب گذشته باز هم به جنایت جنگی روی آورد و با حمله به مراکز غیرنظامی، خدمتگزاران مردم در مخابرات و راه‌آهن و خودروهای عبوری، تعدادی…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/672009" target="_blank">📅 09:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672008">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی به وال استریت ژورنال: حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند
/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/672008" target="_blank">📅 09:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672007">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
حملات موشکی ایران به پایگاه آمریکا در اردن
🔹
منابع عربی از شلیک موشک‌های ایرانی به سمت پایگاه موفق السلطی در شرق اردن که از اصلی‌ترین پایگاه‌های آمریکا در منطقه است، خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/672007" target="_blank">📅 09:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
رویترز: قیمت نفت خام بار دیگر افزایش یافت و قیمت نفت خام برنت به ۸۵ دلار به ازای هر بشکه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/672006" target="_blank">📅 08:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917fba8769.mp4?token=Gj3KmdByzSiI_Po3Qy_5Y31xREEmiukc64QQwGCoMyKldN0iA2B0qgxycfPrxO772i-FPiELQS8hb6reUPytfCx_P9FSD4v8zB56Fq-X2-67KVoAHesnL2T4vACETc5pZ1JcB5U-x-_zRvr115O9BsMiiQABCv2oGPG5O2N_kCc4bLnmZPYwY1mF-l-nJt01cSRXqVWYjT04uH1n0W3af3uQuJWBed1UnS2kKojpfHJcRrIF2QoIAqIlmtOZZIizTLK2QbqxkZYafVZFcvfZaNuVox2suAEhCwka0QzhvFw_hUmeQRQe1563KxpbycXRMTynkgg_TVCR36EBFpHuVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917fba8769.mp4?token=Gj3KmdByzSiI_Po3Qy_5Y31xREEmiukc64QQwGCoMyKldN0iA2B0qgxycfPrxO772i-FPiELQS8hb6reUPytfCx_P9FSD4v8zB56Fq-X2-67KVoAHesnL2T4vACETc5pZ1JcB5U-x-_zRvr115O9BsMiiQABCv2oGPG5O2N_kCc4bLnmZPYwY1mF-l-nJt01cSRXqVWYjT04uH1n0W3af3uQuJWBed1UnS2kKojpfHJcRrIF2QoIAqIlmtOZZIizTLK2QbqxkZYafVZFcvfZaNuVox2suAEhCwka0QzhvFw_hUmeQRQe1563KxpbycXRMTynkgg_TVCR36EBFpHuVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از اصابت موفق موشک‌های سپاه به امارات
🔹
در تصاویر ماهواره‌ای منتشر شده از پایگاه الظفره در ابوظبی امارات انهدام چهار سوله نیروهای تروریست آمریکایی به‌ خوبی قابل مشاهده است.
🔹
این خسارات در نتیجه عملیات موفق‌ موشکی روز گذشته سپاه پاسداران انقلاب اسلامی رخ داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/672005" target="_blank">📅 08:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438027df0a.mp4?token=T2nIFf_1BvMh992V9Hrb9lxOR7UxR6LRLTHZwH3Wx9aGj5J-xfK6AdNO_zK91jfgwZ1WxOpTHqAVayuy92PWvRy6m0SVjLXHWntq4qxG8E5vrcbWhbKCSsJU7H_vLCe4RLktSzBHiQK7VZI5RsQeTyUjiwDwYpuU4mz9XBN1vLuTKrDclsUe1VEqqqHYq3JuAKuSbnPq9QT03BkcBqvHpgzp3oLh7wg87nEoydD_gks7JoNCy__PE69N4gc1R8gQggnGQtL1-prMs50YhHVnDHIP3_lRW6jEjuwwEsZQb2ANgYJhzGO7IhsxdfT3EwLjwskTl-HnSw6wFuzJtaFwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438027df0a.mp4?token=T2nIFf_1BvMh992V9Hrb9lxOR7UxR6LRLTHZwH3Wx9aGj5J-xfK6AdNO_zK91jfgwZ1WxOpTHqAVayuy92PWvRy6m0SVjLXHWntq4qxG8E5vrcbWhbKCSsJU7H_vLCe4RLktSzBHiQK7VZI5RsQeTyUjiwDwYpuU4mz9XBN1vLuTKrDclsUe1VEqqqHYq3JuAKuSbnPq9QT03BkcBqvHpgzp3oLh7wg87nEoydD_gks7JoNCy__PE69N4gc1R8gQggnGQtL1-prMs50YhHVnDHIP3_lRW6jEjuwwEsZQb2ANgYJhzGO7IhsxdfT3EwLjwskTl-HnSw6wFuzJtaFwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ستون دود برخاسته از مقر تروریست‌های تجزیه‌طلب در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/672004" target="_blank">📅 08:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سنتکام مدعی تغییر مسیر سه کشتی در راه ایران شد
ادعای سنتکام:
🔹
مسیر سه کشتی تجاری را که قصد حرکت به سوی ایران را داشتند، تغییر دادیم. یکی از کشتی‌ها که از دستورات نیروهای آمریکایی تبعیت نکرد «از کار انداخته شد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/672003" target="_blank">📅 08:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
دوحه از شهروندان خواست در منازل و اماکن امن بمانند
🔹
وزارت کشور قطر با صدور هشدار امنیتی اعلام کرد سطح تهدید در کشور بالا است و از همه شهروندان و ساکنان خواست تا اطلاع بعدی در منازل و اماکن امن باقی بمانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/672002" target="_blank">📅 08:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۹/ حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر  روابط عمومی سپاه پاسداران: بسم الله قاصم الجبارین و قاتلوهم حتی لاتکون فتنه مردم حماسه آفرین و شجاع و بصیر ایران اسلامی؛
🔹
در پاسخ…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/672001" target="_blank">📅 08:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671999">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f019c4e8a4.mp4?token=BOscTVyBGbhmM7SdUz-J7zruBpUPlK5LJlRyMCiVIBEdlSur-YnaeVYBLd_1JgGk-T7xdnTMDROmSYX8Qd6pJcAZ3Y4nmIyyXhi1V9Ok-iJl5tB_eDDn8a5WiaXkJtEnX36obXXNW4iIX-fuRasy6eUOhKBYwjH4n0yx7IueL9VXt2XtpUDfwQ4Ch7kUXJtvZSOZlItZu9SI7OtlU0R9zCuRbySFt_uj-MovPWoNTlFZQmfa5ZLsTD_g8GrLfU1u_E5tpHtBASqjA6SXcILWJWtAsFwwhyTMU-y6gFvIALVZyVDj3W8SCtgz9wOnjhwT7XIUMGAc_BMmlZWAzn0ijg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f019c4e8a4.mp4?token=BOscTVyBGbhmM7SdUz-J7zruBpUPlK5LJlRyMCiVIBEdlSur-YnaeVYBLd_1JgGk-T7xdnTMDROmSYX8Qd6pJcAZ3Y4nmIyyXhi1V9Ok-iJl5tB_eDDn8a5WiaXkJtEnX36obXXNW4iIX-fuRasy6eUOhKBYwjH4n0yx7IueL9VXt2XtpUDfwQ4Ch7kUXJtvZSOZlItZu9SI7OtlU0R9zCuRbySFt_uj-MovPWoNTlFZQmfa5ZLsTD_g8GrLfU1u_E5tpHtBASqjA6SXcILWJWtAsFwwhyTMU-y6gFvIALVZyVDj3W8SCtgz9wOnjhwT7XIUMGAc_BMmlZWAzn0ijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهایی درباره حمله به مقر عناصر تجزیه‌طلب در شمال عراق
🔹
در پی این حملات، ستون‌های دود از این مقرها در سلیمانیه عراق، به هوا برخاسته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/671999" target="_blank">📅 08:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671998">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رگبار باران برای شمال غرب کشور و استان‌های ساحلی خزر، امروز
🔹
رسانه‌های عبری: کنست با رأی نهایی به انحلال خود، راه را برای برگزاری انتخابات زودهنگام در اسرائیل هموار کرد
🔹
وزرای خارجه چین و پاکستان، روز پنجشنبه دیدار کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/671998" target="_blank">📅 08:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671995">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۹/ حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر
روابط عمومی سپاه پاسداران:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
مردم حماسه آفرین و شجاع و بصیر ایران اسلامی؛
🔹
در پاسخ به شرارت‌های ارتش کودک‌کش آمریکا، رزمندگان نیروهای هوافضای سپاه در موج یازدهم عملیات نصر ۲، با رمز مبارک یا اباعبدالحسین (ع) و تقدیم به سربازان مظلوم شهید بمپور ایرانشهر، با حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه تنف سوریه، علاوه بر انهدام یک سامانه راداری، چند فروند بالگرد خاص عملیات ویژه، در قصاص خون سربازان شهید شب قبل در ایرانشهر، تعداد زیادی از نیروهای جنایتکار آمریکایی را به درک واصل کردند.
🔹
کنترل کامل تنگه هرمز کماکان در اختیار رزمندگان شجاع ماست و تا زمانی که شرارت‌های آمریکا ادامه داشته باشد، یک قطره نفت و گاز از این منطقه صادر نخواهد شد.
و ماالنصر الا من عندالله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/671995" target="_blank">📅 07:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671994">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsN1btqSXzNzAZJJ0u0Vpqanqsylyv_FXiYmb_TPnx9-HNnjlldwFDuuJIpXk7zathuSlw_bROzR20gqjT0E_PABDHb4o8YBFQOANUIBzvBGcqa4IKYDhjwtCU4H_3Sm5x3hsq9swBbFld3UjPbDM_uH4GyHuoNgRgXRmN1z1qPTK8DSp9c2OKuQX2-biei6zFyB9t51txIJBN9KHgy6KZEUBpeVoWhaNagZEDGZWrc-k_Rg89XYjfckVtqiEVeJu8UttJsalDcqtBD7TPnc1WuWeX4Ukhh8cwWDt8HrsPaKiiF6gWLrM1SOdozWao75lWLZBQ0FcS7VjLwiqdFVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۶ تیر ماه
۲ صفر ۱۴۴۸
۱۷ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/671994" target="_blank">📅 07:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671993">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
منابع عراقی از شنیده شدن صدای چندین انفجار در اربیل خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/671993" target="_blank">📅 07:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
🔹
پل گریوه؛ مسیر بندرعباس، خمیر، لار
🔹
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
🔹
دو پل مسیر کهورستان، لار
🔹
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
🔹
پل روستای مارو شهرستان خمیر
🔹
از مردم تقاضا می‌شود با عدم تردد در محورهای ذکر شده و مناطق مجاور آن، راه را برای تیم‌های امدادی و انتظامی باز نگه دارند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/671992" target="_blank">📅 06:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
صدای سه انفجار در چابهار شنیده شد
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/671991" target="_blank">📅 06:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
وقوع انفجار دوباره در بحرین و قطر
🔹
منابع محلی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکا در بحرین و قطر خبر می‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/671990" target="_blank">📅 06:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwjM_UkNgB8bntpHKLcnsYdABqFdGHztTspHVigHSW69-zxyuwhn7DRz7gr1pU54CKLHKwc32IU24UV9ybz_Rh_sAmJOT7_B2jJehwySmQhGDyN2JjCmyuT5z9_2JRZaUnKEPReEGUdCVEuG8_LF_nuP-zQk2geH0kVAOb2tNIjf9UwTWg-d-RiOCwZ2Jt7Dq_cZRulfSN5-nh3_xz-jMyHspyiv48iH9awuWumrvEWWUoKIHMkV7qrRbpTglmkYLOjwN21qwtaBt_3RJaIJHOGrGU9wZXOxLK5rtNLZ6ejJwb8HPM3V8Q01Djd5fIWAgmbU_gu2Xmk4OAQZVRNqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی: پالایشگاه‌های نفت و پایگاه‌های نظامی آمریکا در بحرین مورد حملۀ مستقیم پهپادی قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/671989" target="_blank">📅 06:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وقوع انفجار دوباره در بحرین و قطر
🔹
منابع محلی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکا در بحرین و قطر خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/671988" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd3bf9fd9.mp4?token=dbDS0wkJLrpHHmM6le6WY3p62H2d9kjswfaiksS0YccaneL2Jxn_zOhWxGK6Ljm_0NZNyTyWyeqcWEDf7tP_BMKzw4kVQTaHxxOnq8XSpQiei_VvxFzci_q9aFwgV0xgU5ISL-xFc9cDGSe6kL1GsVfQncxjGMsQSYSACDREHGHeYXbvUF-knvmxisIleueNIfC4zBRxMLge4nNfOoFUIJG5A_Dy-k4sc9pcr6olS_1IOczEEa9xf-EaR9G8s379qxPm9m2V5j8ds0Mhovlg4Ffrwyt0sANbnJv6hoGWZ4LRdz93vl2wCKfhdJcOSOj2bW-NR388S06ygI8WoZs6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd3bf9fd9.mp4?token=dbDS0wkJLrpHHmM6le6WY3p62H2d9kjswfaiksS0YccaneL2Jxn_zOhWxGK6Ljm_0NZNyTyWyeqcWEDf7tP_BMKzw4kVQTaHxxOnq8XSpQiei_VvxFzci_q9aFwgV0xgU5ISL-xFc9cDGSe6kL1GsVfQncxjGMsQSYSACDREHGHeYXbvUF-knvmxisIleueNIfC4zBRxMLge4nNfOoFUIJG5A_Dy-k4sc9pcr6olS_1IOczEEa9xf-EaR9G8s379qxPm9m2V5j8ds0Mhovlg4Ffrwyt0sANbnJv6hoGWZ4LRdz93vl2wCKfhdJcOSOj2bW-NR388S06ygI8WoZs6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحلۀ دوازدهم عملیات صاعقۀ ارتش؛ حملات پهپادی به مراکز پشتیبانی ارتش جنایتکار آمریکا در کویت
روابط عمومی ارتش:
🔹
در پاسخ به جنایت‌های دشمن مستکبر و انتقام خون پاک شهیدان این مرزوبوم، ساعاتی قبل و در مرحلۀ دوازدهم عملیات صاعقه، پهپادهای انهدامی آرش ارتش جمهوری اسلامی ایران، محل استقرار نیروها و مراکز پشتیبانی لجستیکی ارتش تروریستی و کودک‌کش آمریکا در کویت را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/671987" target="_blank">📅 06:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
دشمن آمریکایی برج مراقبت دریایی چابهار را برای سومین‌بار در یک هفته گذشته مورد حمله موشکی خود قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/671986" target="_blank">📅 05:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671985">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام: تازه‌ترین موج گسترده حملات خود علیه ایران را به پایان رساندیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/671985" target="_blank">📅 05:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671984">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe012d6dda.mp4?token=bd5Ky20B6EXCayrzC0sRjpS_7WERF0-8064CR5TuuN6CY08KiEN4lWEo4LlMTlJa7NCRKinXalDvfR4j8ujUveFHy2dt1885Mitl5-5W-9FbG6Wjo0g_xQTe_dtaZYVY1djVny1cWsQz2KZvWRSwLD6nIxvzsvAx5uIDYy6BVvQ_wuMPxHCYVkxjW-s9ckF-vI7UK38exuRg6U9NSHM6ml9mUd0VStzoFqn_j0yZ6Z1OkEzkuH2tq4XlzPq4ez5v_hz-lH-yxbzxauE_5KLyg8e1cnSkcyQvu8cCFL_5YSaGGSnquwDJR3bHseOTOZ6aDyvac1XYICJzUDS84XU8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe012d6dda.mp4?token=bd5Ky20B6EXCayrzC0sRjpS_7WERF0-8064CR5TuuN6CY08KiEN4lWEo4LlMTlJa7NCRKinXalDvfR4j8ujUveFHy2dt1885Mitl5-5W-9FbG6Wjo0g_xQTe_dtaZYVY1djVny1cWsQz2KZvWRSwLD6nIxvzsvAx5uIDYy6BVvQ_wuMPxHCYVkxjW-s9ckF-vI7UK38exuRg6U9NSHM6ml9mUd0VStzoFqn_j0yZ6Z1OkEzkuH2tq4XlzPq4ez5v_hz-lH-yxbzxauE_5KLyg8e1cnSkcyQvu8cCFL_5YSaGGSnquwDJR3bHseOTOZ6aDyvac1XYICJzUDS84XU8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: "روسیه، چین، ایران، کره شمالی و همچنین گروه‌های غیردولتی، توانایی آسیب رساندن به زیرساخت‌های انتخاباتی ایالات متحده را دارند."
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/671984" target="_blank">📅 05:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671983">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
‏ خوک زرد: باید مجوز فعالیت شبکه‌های تلویزیونی که سخنرانی‌های من را پخش نمی‌کنند، باطل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/671983" target="_blank">📅 05:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671982">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای خوک هار: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/671982" target="_blank">📅 04:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671981">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38775e5358.mp4?token=TrPRlXD54G9_OXPcg-VwXXIQDiMUESgU5vkvx4YHn70crRiLgzNmbh2-UQDE_fd1dcdCMo2CYt5qIwhrYh3Cnf6PfMPw7g1Tgj8CW6Z8LPAoIz_ek84SGPGuPGFUtrim03zE8btFS23cV8PGpr-i6jA2609YSpNTnmelIh314G4B1xs6WvmEdVd5_WJXO0aB9gIr1DI20f_0J01BC5dMlzZWoCcUqow-EMLhsCbgURTQMa83UlRErzjTXYRJhsW2s0t_AfFVwnBZ-QwjJBcL6uED1cH7m-qu9OSxC1Wxc6tXXWF8gDQ_YyzISviEsLPgBQi39Dnz99nbQnqntNTOFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38775e5358.mp4?token=TrPRlXD54G9_OXPcg-VwXXIQDiMUESgU5vkvx4YHn70crRiLgzNmbh2-UQDE_fd1dcdCMo2CYt5qIwhrYh3Cnf6PfMPw7g1Tgj8CW6Z8LPAoIz_ek84SGPGuPGFUtrim03zE8btFS23cV8PGpr-i6jA2609YSpNTnmelIh314G4B1xs6WvmEdVd5_WJXO0aB9gIr1DI20f_0J01BC5dMlzZWoCcUqow-EMLhsCbgURTQMa83UlRErzjTXYRJhsW2s0t_AfFVwnBZ-QwjJBcL6uED1cH7m-qu9OSxC1Wxc6tXXWF8gDQ_YyzISviEsLPgBQi39Dnz99nbQnqntNTOFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
خوک هار: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/671981" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671980">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
حزب‌الله: این حزب در انتشار فهرست متهمان همکاری با اسرائیل هیچ دخالتی ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/671980" target="_blank">📅 04:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671979">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZO_4N4-OXAJZViwdk2EJF4IDt9B_pjPMd1QCvw5BJopJaAludwz84OpelVWvbw2UBkQV41YfW3wDZmMxPiL5eo86dMIL1ZSc3Gw4EaqexFZ3pDvoNZUILYlM09hZ0kat2d_4Lak1LySx-Kqm8QGmENjGinudFqqtzYx1_KoiArOufW-qirNMhnIUas8PPSkTpPiWhJg5N_qV5OFLv8byyOhFdphN54ptUyNXM2auzIm4lKD-dgvUDAwXf4fNei4Idxxrd7jJkV-T0x5OAmhjYikM5Nv9nD_IPsCGYGNIWeSxUuw8ah4YDiTD9fmqdRz31kS8vg4FlIp8J_b9MbibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییر مسیرها از دوحه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/671979" target="_blank">📅 04:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671978">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f6f7102a.mp4?token=Yd2dxcC88wGXr3M7RrE_XMWkIbZQgLyzXFh4PCmpvn11iUFNOS7Lj8fLFAB38oalyXJE0a2emBF84ddoq7wz3hFIjnqjUEwNBZMHPtFfL7K0jMzu7l_ACM6TwBgOLZglxubCC5r6Ckqm2uVky2E7EItJohpfV1zIQOR7NJpkLFtS_D6jKYfyvsu_zRu-S2S31-8186SaqOu9ZsHCMEbPEAE3aB189-wxay7v97OTsk7lCT0v-8quHCA7tx1hAar6rAta4fRukHVMFcgWX3PMfJ79EAe1zWkZrEKlazab2BB1ykuO4NdkYAUKUoKjwLl7ReaLIUypoK9INngqzJaf6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f6f7102a.mp4?token=Yd2dxcC88wGXr3M7RrE_XMWkIbZQgLyzXFh4PCmpvn11iUFNOS7Lj8fLFAB38oalyXJE0a2emBF84ddoq7wz3hFIjnqjUEwNBZMHPtFfL7K0jMzu7l_ACM6TwBgOLZglxubCC5r6Ckqm2uVky2E7EItJohpfV1zIQOR7NJpkLFtS_D6jKYfyvsu_zRu-S2S31-8186SaqOu9ZsHCMEbPEAE3aB189-wxay7v97OTsk7lCT0v-8quHCA7tx1hAar6rAta4fRukHVMFcgWX3PMfJ79EAe1zWkZrEKlazab2BB1ykuO4NdkYAUKUoKjwLl7ReaLIUypoK9INngqzJaf6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شیرجه موشک‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/671978" target="_blank">📅 04:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671977">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6552de3ed9.mp4?token=Sp9B3m8IDjAdZXK2OOvnanjRbyzH9SzU0oh7F__5s5FjWpeieeQQmjMiE1pAxIm6d-H1Gl_kcI9GUfCCbKX0jeerZqQoNRt2J8B6_QMd3CBhsHXyBFoMcHqGcoxlMTjBU6hEVrIu51DXyQ_1Cn7L4Do_w5qO1rxIAxIHcyzEyM7y4BgabBJC14c5Qa9kj83RbWHvLdGfn44gkAdtZf6QRMsC10Wi85YfO7-Al7M4-Aw9gYv5elF0OTve6yohUH-Y9NC7gmjU5EFlUKW4bwrZD4CoVdYI-6_wHPTYV1Lg2WI6dVrkEMamyQq9_MiO_Xp0xAUhwolkOZUPyLGsDuaN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6552de3ed9.mp4?token=Sp9B3m8IDjAdZXK2OOvnanjRbyzH9SzU0oh7F__5s5FjWpeieeQQmjMiE1pAxIm6d-H1Gl_kcI9GUfCCbKX0jeerZqQoNRt2J8B6_QMd3CBhsHXyBFoMcHqGcoxlMTjBU6hEVrIu51DXyQ_1Cn7L4Do_w5qO1rxIAxIHcyzEyM7y4BgabBJC14c5Qa9kj83RbWHvLdGfn44gkAdtZf6QRMsC10Wi85YfO7-Al7M4-Aw9gYv5elF0OTve6yohUH-Y9NC7gmjU5EFlUKW4bwrZD4CoVdYI-6_wHPTYV1Lg2WI6dVrkEMamyQq9_MiO_Xp0xAUhwolkOZUPyLGsDuaN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توقف پروازها در فرودگاه قطر
🔹
وزارت کشور قطر: در خانه‌ها و مکان‌های امن بمانید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/671977" target="_blank">📅 04:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671976">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
خوک زرد: ما در حال حاضر برترین کشور در سراسر جهان هستیم
🔹
ما اکنون در ایالات متحده بیش از هر زمان دیگری سرمایه‌گذاری داریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/671976" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671975">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
منابع عربی: یک موشک ایرانی به‌طور مستقیم به یک پایگاه نظامی آمریکایی در بحرین اصابت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/671975" target="_blank">📅 04:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671974">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
منابع عربی از وقوع انفجار در پایگاه آمریکایی العدید قطر گزارش دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/671974" target="_blank">📅 04:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671973">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
منابع عربی: یک موشک ایرانی به‌طور مستقیم به یک پایگاه نظامی آمریکایی در بحرین اصابت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/671973" target="_blank">📅 04:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671972">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq8fzTHh9nE41X5gO_cR1Qh8RQ7nuq3j5hSsLLNhM-w0hmwoXkO8qAoT3S2aDhoHHYRvgne_SNS-Wa_USxPXQBvdQemX7eY-pe95sZapkNY9YewHMZDmFs3-jg37j9lAZvYh2T-0-XDE5SbaRiw157R8SFWnI_rnWAhjPf9iA5aHt-XfbeJ0H-VK2l5kAnzmdCXHDCeKzfc0dLTdE_1SEhdzHW-qjbFtr2zcXiP0L_CAhwU0h4-Zn-hvZhXu_lylsBx_anADQaE6i2nmQlANN_6CznInPpJndoonLy3VzVnEBgB7yYPrGuAQ2lrB4YU6OxaWeRvKcLV-6gIMzpTEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از آتش‌سوزی در یک نقطه از کویت در نزدیکی مرز عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/671972" target="_blank">📅 04:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671971">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
شمار شهدای حمله به پل‌های بندرخمیر به ۳ نفر رسید؛ ۹ نفر مجروح شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/671971" target="_blank">📅 04:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671970">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
منابع عربی از وقوع انفجار در پایگاه آمریکایی العدید قطر گزارش دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/671970" target="_blank">📅 04:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671969">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
حادثه در پل بحرین-عربستان
رسانه‌های عربی:
🔹
صدای آژیر آمبولانس‌ها و ماشین‌های آتش‌نشانی که به‌سوی پل متصل‌کنندۀ بحرین و عربستان سعودی در حرکت هستند، به گوش می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/671969" target="_blank">📅 03:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671968">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b757177081.mp4?token=oKiP0JwuqyowpmI3uqg-_WX1o5ysBmtZc3_7IM_cO-437RqnnjsSKElU63OLisKQQr5fNetCDOLS67dXTxHWTZNV5Qy2r4wVnGqx6nxHv0w7FDssmhRO9_NMu8MALLaHdnSQ0-HFp_AGmAC8HvKUINbAiWFS209nuNKAY-OgjSgfoYkOjn0EzjwHKxJ80N_vJ4i7LNAXbFHScWuFSw-zF9rwCLUz5Dr-4u1WHrWSNwUEfCkvA9zr0-FfQGgucojMd-Mg0gbtOnZuidoVPzq5vOGW0m9LljirAm2618Iom8PPC5Ad4DdiY6sqN293q6fQtXXDPxzWBRGgPCefNOEXYJ0MALgQbHBzYGe04XVrD8_i3PUF2J906lZFqM66t0mlRqvr8Uu-sJpmRc3qaTO-DYNgfRbbwuks5MUBTDWAeZ-yFju5MtXifNv8rCAGHA_le9ITGhoFVGSEzVFAQ7kxIDOEgB3X6Eisq4tnvQdjPcAr4GRHSu-OTX53DP_6IWe8Del8TYrIQHF0564bHFi-L0BClgI-xBIeMw1cnBOPhAsZ3qZ7hpxlxE-UDvGjSs9SFMfXFAhAJFssR4Pbgo1rHl5KfcS2efvlv3PgUhDbOEBel_blRQA90h66xtRvyMSzLzlribJCaLrDKKiBl-2lOHNiPaSRYbbToS1twvZVC3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b757177081.mp4?token=oKiP0JwuqyowpmI3uqg-_WX1o5ysBmtZc3_7IM_cO-437RqnnjsSKElU63OLisKQQr5fNetCDOLS67dXTxHWTZNV5Qy2r4wVnGqx6nxHv0w7FDssmhRO9_NMu8MALLaHdnSQ0-HFp_AGmAC8HvKUINbAiWFS209nuNKAY-OgjSgfoYkOjn0EzjwHKxJ80N_vJ4i7LNAXbFHScWuFSw-zF9rwCLUz5Dr-4u1WHrWSNwUEfCkvA9zr0-FfQGgucojMd-Mg0gbtOnZuidoVPzq5vOGW0m9LljirAm2618Iom8PPC5Ad4DdiY6sqN293q6fQtXXDPxzWBRGgPCefNOEXYJ0MALgQbHBzYGe04XVrD8_i3PUF2J906lZFqM66t0mlRqvr8Uu-sJpmRc3qaTO-DYNgfRbbwuks5MUBTDWAeZ-yFju5MtXifNv8rCAGHA_le9ITGhoFVGSEzVFAQ7kxIDOEgB3X6Eisq4tnvQdjPcAr4GRHSu-OTX53DP_6IWe8Del8TYrIQHF0564bHFi-L0BClgI-xBIeMw1cnBOPhAsZ3qZ7hpxlxE-UDvGjSs9SFMfXFAhAJFssR4Pbgo1rHl5KfcS2efvlv3PgUhDbOEBel_blRQA90h66xtRvyMSzLzlribJCaLrDKKiBl-2lOHNiPaSRYbbToS1twvZVC3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مروری ساده بر آنچه گذشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/671968" target="_blank">📅 03:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671967">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Lh2JsJRCo7uID8a8T7BJHcaJNsVfFx0b2MEQYxZi_yBpShUJwBcuORd785yfBdpRTBbh6UcjrMLdbRDxNKRFm2FvllOZcEqTGTUwoYiMLPCdBe3slryfQHuskg9Flcxy8LoieVRu4WGurRSEPGVDyJKslljia8wB2cMjorCqgyyCDqePOzkMBaoQOrE8cd_FhaUmTxUJA_tnKtPK4SZf1fNs3hZmJgwNKckqZMZw_0DonWSR8q-W5Iqgu4vmU-mhWJYlHn39tw96kF1iVMwOjN9x_Vwmu7AvK1szpsq0UjWdWSEJG7UsvC253rly_bM9lteT7il17T8RVM7yVd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت‌الله اعرافی: تفاهم‌نامه تمام شد؛ مذاکرات را ادامه ندهید
🔹
اکنون که رئیس جمهور آمریکا با صراحت و وقاحت تمام، پایان‌ تفاهم‌نامه را اعلام کرده و جنگ را آغاز نموده است، وجهی برای پایبندی به تفاهم‌نامه و ادامه مذاکرات باقی نمی‌ماند.
🔹
رئیس جمهور و سایر اعضای شعام و فرماندهان و مسئولین دیپلماسی کشور باید تفاهم‌نامه با اطاعت تام از رهبر معظم انقلاب به همان مسیری که ایشان تشخیص داده‌اند، بازگردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/671967" target="_blank">📅 03:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671966">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf85bb926d.mp4?token=WS4CswCzCSBsP_xVEfoh5wtKDtgBViK5SXoqioaN4UMpV3dLCs3sFBBfx1UgyOel7UZGOJuhEiARAnVqZItCB58Jx4bCfLv2gGMU2NVunaLfuB-7mG0ymMA8qKxskqPbFV49ckKUgcxsiBsNoQ-IN6IdRUO6MweToKOu8_AkWAyRblpJSLvW-DRO6udZISPYBaZvuuNLt6FYog6YugeHQSelAsRY2I3Atb3_f9rbSGwCkJPlDLz37_SKtdQM89KOO47inX_DcjBONASDsCTPCpoz_W6z249pssCsBYuS4aRWCyeTEOE31s6n7vUrEvzBZk-Xy8OlRp7F48uoHjZmrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf85bb926d.mp4?token=WS4CswCzCSBsP_xVEfoh5wtKDtgBViK5SXoqioaN4UMpV3dLCs3sFBBfx1UgyOel7UZGOJuhEiARAnVqZItCB58Jx4bCfLv2gGMU2NVunaLfuB-7mG0ymMA8qKxskqPbFV49ckKUgcxsiBsNoQ-IN6IdRUO6MweToKOu8_AkWAyRblpJSLvW-DRO6udZISPYBaZvuuNLt6FYog6YugeHQSelAsRY2I3Atb3_f9rbSGwCkJPlDLz37_SKtdQM89KOO47inX_DcjBONASDsCTPCpoz_W6z249pssCsBYuS4aRWCyeTEOE31s6n7vUrEvzBZk-Xy8OlRp7F48uoHjZmrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد در مصاحبه با فاکس نیوز: اگر ایران به بازدارندگی اتمی برسد، مجبوریم آنها را با احترام آقا (سِر) خطاب کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/671966" target="_blank">📅 03:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fdadf1c.mp4?token=JZzUWR0wRURkYY16X5rD2iaz5xRZikPC7wwNqBXoqeMoVff8JEo5CClcSgzStyeOVM41nLQOTuLOAZ8UXmPrlNjiDxUReYjN1hfBlLVn-P6dmgMU_FcbbPi_vFQChayQ3LM4zHUkzysLsBZJwbecYMCLX4iSKBz3rLT65WqV-H7Od7JcIsZU35Zcpx1hpa4sB69Hwj939ulZtzBeyHD_tC8TDYr7K-kSL4yqyNvI8gT6_sbUL0gCVKQqnG7XOVGReGyiwoaR5cIXkvsn9_mrZvPLHlvfkKJ9fIIplXV_dy620WfGJjRLNsS33O63PZfLXQzJYSn8_CcqdtscDUGeDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fdadf1c.mp4?token=JZzUWR0wRURkYY16X5rD2iaz5xRZikPC7wwNqBXoqeMoVff8JEo5CClcSgzStyeOVM41nLQOTuLOAZ8UXmPrlNjiDxUReYjN1hfBlLVn-P6dmgMU_FcbbPi_vFQChayQ3LM4zHUkzysLsBZJwbecYMCLX4iSKBz3rLT65WqV-H7Od7JcIsZU35Zcpx1hpa4sB69Hwj939ulZtzBeyHD_tC8TDYr7K-kSL4yqyNvI8gT6_sbUL0gCVKQqnG7XOVGReGyiwoaR5cIXkvsn9_mrZvPLHlvfkKJ9fIIplXV_dy620WfGJjRLNsS33O63PZfLXQzJYSn8_CcqdtscDUGeDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشی از وضعیت پل بندرعباس به لار پس از حمله آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/671965" target="_blank">📅 03:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
حملات موشکی ایران به پایگاه آمریکا در اردن
🔹
منابع عربی از شلیک موشک‌های ایرانی به سمت پایگاه موفق السلطی در شرق اردن که از اصلی‌ترین پایگاه‌های آمریکا در منطقه است، خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/671964" target="_blank">📅 03:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671962">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VmWyhlE68M0dKEGX1B6MukcgmjHXOndN8hhpp7WmfJhmvPf7pt5BhUsUvVmXyTTCpj_8WlmDXawVXeycEyERwO2QKkAFXk9iMRkj_GosLGaaIYmN6xmWZFO5XWxyAARB5pUjX5qr8fCGCVzNTHxoYsZ1A1XILzcTVCYqWei4ToqjlU09RI5X_RHPIgcCOTsZaB0RRVRuR7IefoDiGSNMAFC90nKzgW-7fSFfQuSOzEHbO4QnLyAAeSfnkfixPRJY8rvQot0F9Ftd7HvgE0EIiYIqze-mJ5vilHxqhy7JmVOeNZtRtsKVJ8tGZkGowW_zD5xFMTI2qWo6-Wm6ESD_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jkj_w7Ux8qTVMruNjrbpDc8Q3HtY9ViiSrj6sFLDjhD7B9XtYCuJ2ZKskQxprD4MS8DKq4LDkpDQV48LDO_lFSRg2Vq2Rk42en_NmI41sXMiWpOXxOCTkyDfj9LDGoPNViHypo6VFqotEDMMLhVCEmBaPLZ6gBPNOwAfyMKE6rRHxcaV3m9e814azrerl-xt6K8KBlzsU7tdsTuIpxFQP2nvhoXF50ndYO0SAeAnMbjjZ-oiUJF-nBDxixAsDOAgSdjX2vpPQXq_VpwEFsHaqAQKusWvNAcH-JWVE_wzQrUpMEezYubbtKPP0miuXswqqWGxgz0vtvCFUVH0Tu2FyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
داور فینال و رده‌بندی جام جهانی ۲۰۲۶
🔹
با اعلام فیفا؛ اسلاوکو وینچیچ از کشور اسلوونی دیدار فینال جام جهانی ۲۰۲۶ که یکشنبه ۲۸ تیر ساعت ۲۲:۳۰ در استادیوم مت‌لایف نیوجرسی بین اسپانیا و آرژانتین برگزار می‌شود را قضاوت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/671962" target="_blank">📅 03:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671961">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0322523c15.mp4?token=EBvzeIZ0K5a1llLbv3tqodLwTAP9d6luVD4K1_MxqkU7wAJf8JD-C7nKddFUnKkxvZ7-ZHwjPi6pjlIU_n7AqpWOt-uhHFqje35BZSduPIr-FebEUiRuDIOlisoyK3yYwpibOpuKmXvLKszTVi5AhaTMgmwxjiSm2fRa7tywDNHTVMLdx4DjDsx54Bzq8sHOAuljKLDKt1w0o2a8-0CVy3Rp35tRCntukfR2P548bZh_TDL_-lHN1C8292me2L0foqaQdfk-zUwgXurWMn6Lc4B6R-rpOVxrCGqdxFYHtA_wVwPbGJKQS41ibTHnZYQCXZ94bE8eEuzcX7BQ2x-tTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0322523c15.mp4?token=EBvzeIZ0K5a1llLbv3tqodLwTAP9d6luVD4K1_MxqkU7wAJf8JD-C7nKddFUnKkxvZ7-ZHwjPi6pjlIU_n7AqpWOt-uhHFqje35BZSduPIr-FebEUiRuDIOlisoyK3yYwpibOpuKmXvLKszTVi5AhaTMgmwxjiSm2fRa7tywDNHTVMLdx4DjDsx54Bzq8sHOAuljKLDKt1w0o2a8-0CVy3Rp35tRCntukfR2P548bZh_TDL_-lHN1C8292me2L0foqaQdfk-zUwgXurWMn6Lc4B6R-rpOVxrCGqdxFYHtA_wVwPbGJKQS41ibTHnZYQCXZ94bE8eEuzcX7BQ2x-tTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج جدید حمله موشکی از ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/671961" target="_blank">📅 03:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671960">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4360f9a1c.mp4?token=ZdMY5LilxMqoBprq4jUcR40ewMP74pFk72Om0BKsfDzN2UyNtm_L0a2H_-MxiF5avEpLqNq5hsN_Ffuhzp7JOWnZTwlO-f7gOSJvEue3iwlG19_HeBw6LwBNSC7p6I2My9DA1UGbxQ8tkYX6niywvsHIKRMxZCpYQQMLViHGIzfOOnnWLVZmEBBJPSKF17Ls4S5stRiFGZyPCOGeoialW-wo6Ah7MjAaC7df9uZh3HTSAGdjknD2pb273muKmnIWhoBJ1tR8sy4Eh2EpC_kfF_nG2qnB8zGBPHuWd-Ig9PbLC1za41AQbwDZufOC3XScEF6seRHFCs4Ity-be5JEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4360f9a1c.mp4?token=ZdMY5LilxMqoBprq4jUcR40ewMP74pFk72Om0BKsfDzN2UyNtm_L0a2H_-MxiF5avEpLqNq5hsN_Ffuhzp7JOWnZTwlO-f7gOSJvEue3iwlG19_HeBw6LwBNSC7p6I2My9DA1UGbxQ8tkYX6niywvsHIKRMxZCpYQQMLViHGIzfOOnnWLVZmEBBJPSKF17Ls4S5stRiFGZyPCOGeoialW-wo6Ah7MjAaC7df9uZh3HTSAGdjknD2pb273muKmnIWhoBJ1tR8sy4Eh2EpC_kfF_nG2qnB8zGBPHuWd-Ig9PbLC1za41AQbwDZufOC3XScEF6seRHFCs4Ity-be5JEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ادعایی از فعالیت پدافند در بحرین
🔹
فیلمی که برخی از کاربران منتشر کرده‌اند فعال شدن پدافند هوایی بحرین را نشان می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/671960" target="_blank">📅 03:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671959">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
کویت: در حال مقابله با حملات پهپادی و موشکی هستیم
🔹
ارتش کویت اعلام کرده پدافند هوایی این کشور در حال تلاش برای مقابله با حملات موشکی و پهپادی از سوی ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/671959" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671958">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
منابع عربی از شنیده شدن صدای انفجار در اردن، بحرین و کویت خبر می دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/671958" target="_blank">📅 03:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671957">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وال استریت ژورنال به نقل از یک مقام آمریکایی: حملات هوایی آمریکا روز پنجشنبه چندین پل در ایران را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/671957" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671956">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در بحرین
🔹
منابع خبری از فعال شدن آژیرهای هشدار در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/671956" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671955">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
حمله هوایی آمریکا به دو پل در بندر خمیر
🔹
به گفته شاهدان عینی دو  پل حوالی روستای کهورستان و رودخانه شور شهرستان بندرخمیر مورد اصابت قرار گرفته است.
🔹
راننده یک خودرو شخصی، روی یکی از پل‌ها شهید شده است/ صداوسیما  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/671955" target="_blank">📅 02:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671954">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa01daef0f.mp4?token=H5GZbtf-b06QVy-sRu2lONCWIX3EZB6Ui9DiPy1sHTvTIbpFnTkuQVY4EQKoJ6VaEm_1AdqUNBldg4DcEUiz-Ax9LwQPdrHvq1MiOsL15Qd5CLRloLk7bfukC-P44ciASIu6zESbFik0xvU5Ns76jboOuH2yRVFmjcFe7dN4SEsly6M-ddudTnflYbSob0us4YHHuROHb1UQ4Ss4HaAKGrZCJRUXP75k3hbI1iTMz7Mzsym6TQHlpqwNA0ndvAXyHsA-N8e0R8orQHOhwY1xtYV88RE_5SWUF3c-UGwKf_yyWUaDcg04Yv6aE7Debr7_AubD4DWbM_nTIizfZ826eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa01daef0f.mp4?token=H5GZbtf-b06QVy-sRu2lONCWIX3EZB6Ui9DiPy1sHTvTIbpFnTkuQVY4EQKoJ6VaEm_1AdqUNBldg4DcEUiz-Ax9LwQPdrHvq1MiOsL15Qd5CLRloLk7bfukC-P44ciASIu6zESbFik0xvU5Ns76jboOuH2yRVFmjcFe7dN4SEsly6M-ddudTnflYbSob0us4YHHuROHb1UQ4Ss4HaAKGrZCJRUXP75k3hbI1iTMz7Mzsym6TQHlpqwNA0ndvAXyHsA-N8e0R8orQHOhwY1xtYV88RE_5SWUF3c-UGwKf_yyWUaDcg04Yv6aE7Debr7_AubD4DWbM_nTIizfZ826eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشی از وضعیت پل بندرعباس به لار پس از حمله آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/671954" target="_blank">📅 02:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671953">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
وال استریت ژورنال به نقل از یک مقام آمریکایی: حملات هوایی آمریکا روز پنجشنبه چندین پل در ایران را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/671953" target="_blank">📅 02:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
منابع عربی از وقوع چندین انفجار در پایگاه‌های نظامی آمریکایی در کویت گزارش دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/671952" target="_blank">📅 02:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671951">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
آژانس بین‌المللی انرژی: اگر جریان نفت و گاز از طریق تنگه هرمز ظرف چند هفته بهبود نیابد، باید نگران آن باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/671951" target="_blank">📅 02:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671950">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
دروغ سازی جدید آکسیوس و اسرائیل در مورد طرح ایران برای ترور ترامپ در ترکیه
رسانه آمریکایی - صهیونیستی آکسیوس مدعی شد:
🔹
در جریان سفر دونالد ترامپ به ترکیه، اسرائیل اطلاعاتی را در اختیار ایالات متحده قرار داد که بر اساس آن، یک مقام ارشد ایرانی به یکی از همکارانش گفته بود ایران باید تلاش کند رئیس‌جمهور آمریکا را زمانی که در آنکارا حضور دارد، ترور کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/671950" target="_blank">📅 02:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671949">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b2cff3a5c.mp4?token=U3ibehVTzsh0VvEwT3UJ3Y3PmkrH2DySVTK_WfgLwzsccj1XO8Yq0c6kduZOIdQXMfKX628V_M3pv9L0N3VJpFJAWfYRIZK-JpVY9qYM82qN-LEt8ou-EnUv0ui5-BYb4L9zkA_azmeJWKHogBOvo1uJgdwCL-yofa2tGAbB5Ho3wv-2uzcY-_jvxWZnhfg45lD__ZgBURS5t9zy2xK8qBKmMog6JQO-t2XE8CODyackInVnrLms-cUAVshhKLoXG4OdA-uexnEyKqc5scQ_AySSEYpYkgFxuOFg60d8nRNFPIpMNDOahBAiqIIX_VLtOnxSINVpAq__Zw_slLq64w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b2cff3a5c.mp4?token=U3ibehVTzsh0VvEwT3UJ3Y3PmkrH2DySVTK_WfgLwzsccj1XO8Yq0c6kduZOIdQXMfKX628V_M3pv9L0N3VJpFJAWfYRIZK-JpVY9qYM82qN-LEt8ou-EnUv0ui5-BYb4L9zkA_azmeJWKHogBOvo1uJgdwCL-yofa2tGAbB5Ho3wv-2uzcY-_jvxWZnhfg45lD__ZgBURS5t9zy2xK8qBKmMog6JQO-t2XE8CODyackInVnrLms-cUAVshhKLoXG4OdA-uexnEyKqc5scQ_AySSEYpYkgFxuOFg60d8nRNFPIpMNDOahBAiqIIX_VLtOnxSINVpAq__Zw_slLq64w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی دیگر از آتش‌سوزی گسترده در زیرساخت‌های شلیک موشک در خاک کویت
🔹
برخی منابع می‌گویند جاده‌ای که تروریست‌های آمریکایی از آن برای انتقال سامانه‌های موشکی خود به نزدیک مرز عراق و از آنجا شلیک به داخل کشورمان استفاده می‌کردند، به شدت مورد حمله ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/671949" target="_blank">📅 02:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671948">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e155b8e5e.mp4?token=iVYVqZeQDmi3AnwlKX2AJ9Xt0-qNlmAlhogyRtg-Ce-4V-k2kii0GRy6vF-BG63jkMXYZzurXreO5QBy59YGnbTqMWn5zia32FkRtKWNYIBdSIOKQ2ISK4VbDdmk7suZ-rLl8vCKV1zEskI-yH2-I4Emsf01Ge41o52Nm95_RbuOwcoi4HDoOttOWnb3GQX6hHhZHfirM4w9EkSxuFFgUAJVs19rwVLLEgzMTUdk7cvj_Ivzv_EsyESpLSbrHq_hFkFddiCD5URWRcU5Lc4gUEEqox0_eXhUygBSlPrTG3ts-02WOj1MXgMKp9aodsTOyuqe3M2K4NzRdY-wkRLYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e155b8e5e.mp4?token=iVYVqZeQDmi3AnwlKX2AJ9Xt0-qNlmAlhogyRtg-Ce-4V-k2kii0GRy6vF-BG63jkMXYZzurXreO5QBy59YGnbTqMWn5zia32FkRtKWNYIBdSIOKQ2ISK4VbDdmk7suZ-rLl8vCKV1zEskI-yH2-I4Emsf01Ge41o52Nm95_RbuOwcoi4HDoOttOWnb3GQX6hHhZHfirM4w9EkSxuFFgUAJVs19rwVLLEgzMTUdk7cvj_Ivzv_EsyESpLSbrHq_hFkFddiCD5URWRcU5Lc4gUEEqox0_eXhUygBSlPrTG3ts-02WOj1MXgMKp9aodsTOyuqe3M2K4NzRdY-wkRLYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله یازدهم عملیات صاعقه ارتش؛ مراکز و پایگاه آمریکا در بحرین آماج حملات پهپادی ارتش
روابط عمومی ارتش:
🔹
در پاسخ به اقدام خصمانه دشمن در هدف قرار دادن زیرساخت‌های شهری و مردم بی‌گناه، ساعاتی قبل، ارتش جمهوری اسلامی ایران در مرحله یازدهم عملیات صاعقه، محل استقرار بالگردها و هواپیماهای شناسایی P8 ارتش تروریستی آمریکا در پایگاه الصخیر بحرین را هدف حملات پهپادهای انهدامی آرش قرار داد.
🔹
امنیت و استقلال این میهن خدایی خط قرمز ماست و متناسب با شرارت‌های دشمن خبیث، سریع و قاطع پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/671948" target="_blank">📅 02:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671947">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
فرماندار بوشهر:
حمله آمریکا به بوشهر یک مجروح بر
جا گذاشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/671947" target="_blank">📅 02:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671946">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd9be4b95.mp4?token=DaD0w-iQDW9zlSt_CZoRcxhUtsR-2z_9Pxg2iXsOErlsSqzG6HOVDVRWTagyJQKz4UhVyJhTgJXBEukSA8SC98TB_DbefAIzPvCBXYsRc9QlZwvGS8848GHW3n0J7QPXoAO1zNj9KPh-NslHODsuG8cDfpRkkDN5OLd6N7mfAcuERd1oUCWn2P8Q1urXN_ynDhT577fmx1Ugy4p0nRoj5eo47-zHkaoCbI6FIsyoxJondPBzcAz_s6qmotur-bvhFKih2R9du9J9iX3qjSQfp3KV8me6DvYTtLQOm1g3zZPqQMhn8KfTaBHT0ZtJCbEGT03L7J8tbPBAo0f2aS0Efw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd9be4b95.mp4?token=DaD0w-iQDW9zlSt_CZoRcxhUtsR-2z_9Pxg2iXsOErlsSqzG6HOVDVRWTagyJQKz4UhVyJhTgJXBEukSA8SC98TB_DbefAIzPvCBXYsRc9QlZwvGS8848GHW3n0J7QPXoAO1zNj9KPh-NslHODsuG8cDfpRkkDN5OLd6N7mfAcuERd1oUCWn2P8Q1urXN_ynDhT577fmx1Ugy4p0nRoj5eo47-zHkaoCbI6FIsyoxJondPBzcAz_s6qmotur-bvhFKih2R9du9J9iX3qjSQfp3KV8me6DvYTtLQOm1g3zZPqQMhn8KfTaBHT0ZtJCbEGT03L7J8tbPBAo0f2aS0Efw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور خودروهای اتش نشان و امدادی در مناطق نظامی پایگاه امریکا در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/671946" target="_blank">📅 02:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671945">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2p0Sm3KBKMaGKUfVBuat-o3GPgGkKWQWD4c0zMueAZ82rQXI3Fu-ndoz8prqsAD_i1nNPE8D6e7RVf93MmnNhPANPQjL-g5P4UbtDfdxKoqoTuli6JpZXjx5U2L-gtKliMlIyuJBKz434WaZt7AWH63tQmOYSNGGCCTzLwS2OHhFIl3XtbSLZmHAH1WzDCp1LudSj8OHYiH-o18wuRnPjMyApc9UZ83Qm8yacrrLf762e2wwrjj7NkfctjZjgdQFx3Ls6ihOzXTtMvTqytV2x93y0xiTASRhdi7_9FyyigK4Waw6FjaczdTcUgcJJjDuq2xRJ7mf8B7PyMJgu5EeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش سوزی گسترده و دود غلیظ در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/671945" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671944">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
یک نقطه در شهرستان دشتی بوشهر مورد حمله دشمن قرار گرفت
معاون سیاسی و امنیتی استاندار بوشهر
:
🔹
بامداد امروز یک نقطه در شهرستان دشتی مورد اصابت حملات دشمن قرار گرفت./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/671944" target="_blank">📅 02:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671943">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/671943" target="_blank">📅 02:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671942">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7df7ba20.mp4?token=WHnEw-aHqNgcnA0vfXIUVDeO7TT7h8qcNutD2LFfXkR_6-WyOCvsxnQUcdP_rvKjDQR8P3EONeu5gdFxcK847hxD90hI-7xEoi3kBDnJwlP-G746RYlNNeCSg6jQYzpKf9fUNQhnxKwTsQNT7Nj6TSg7UK_dZUHWjc6z6RKJw_4yYS6saS95rScl1sL5jhb7Bpxvn5VHGQ5Igpn55KaaenZKHX509jEqZ7iiohLBOJazg69y9iIm_DFjQL21R5Tq7mh8s55ekv0LWyoflTvOMYQ1zWIC5Y21jR2wq8eNuwNlf_uLv2F5uaOgRWrX6gDuKZQaeO4RR7I2d9a2sEfNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7df7ba20.mp4?token=WHnEw-aHqNgcnA0vfXIUVDeO7TT7h8qcNutD2LFfXkR_6-WyOCvsxnQUcdP_rvKjDQR8P3EONeu5gdFxcK847hxD90hI-7xEoi3kBDnJwlP-G746RYlNNeCSg6jQYzpKf9fUNQhnxKwTsQNT7Nj6TSg7UK_dZUHWjc6z6RKJw_4yYS6saS95rScl1sL5jhb7Bpxvn5VHGQ5Igpn55KaaenZKHX509jEqZ7iiohLBOJazg69y9iIm_DFjQL21R5Tq7mh8s55ekv0LWyoflTvOMYQ1zWIC5Y21jR2wq8eNuwNlf_uLv2F5uaOgRWrX6gDuKZQaeO4RR7I2d9a2sEfNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/671942" target="_blank">📅 02:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671941">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f84b37246.mp4?token=h5PbRZQAE2avKupeVQOYpS2E87IMOsgGV8lrLrSruWyg1zKSP-cOQ_WlHdZS5bmNJN6QzfS_fiQ8fETuadad3tbaYdunDRCbQydhlUcpKxM7ODYpmINjTDwsTh0vHy-j6baJDtDoyOfUlJfy_fdJ1GICGuUYOzqrzChMuzUZ9myouElB3pYka2bMBr6-kTe6exSEI49qQaQ6x1uVJ7DPzynSbSIvYUOx_-a99QelGCN_6SCCYdphmqFxUA_nJwqUYxmnRxx7F2LMtFGZF5GsjBWksooLT8O7UuImnAbqzmqmT-PoyU1QTHl2oNjaVaBy1NDqUPvALKVnFY8jjZrhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f84b37246.mp4?token=h5PbRZQAE2avKupeVQOYpS2E87IMOsgGV8lrLrSruWyg1zKSP-cOQ_WlHdZS5bmNJN6QzfS_fiQ8fETuadad3tbaYdunDRCbQydhlUcpKxM7ODYpmINjTDwsTh0vHy-j6baJDtDoyOfUlJfy_fdJ1GICGuUYOzqrzChMuzUZ9myouElB3pYka2bMBr6-kTe6exSEI49qQaQ6x1uVJ7DPzynSbSIvYUOx_-a99QelGCN_6SCCYdphmqFxUA_nJwqUYxmnRxx7F2LMtFGZF5GsjBWksooLT8O7UuImnAbqzmqmT-PoyU1QTHl2oNjaVaBy1NDqUPvALKVnFY8jjZrhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رادارهای آمریکایی در کویت، دوباره مورد حمله قرار گرفت./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/671941" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671940">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f67eb572.mp4?token=XT_xjMDLVWBdKqhhB7v3gYHYU7d-VuD4u6_TY8BH2R0x8INigKZZrCIZ3ISCeImfgBIyQWvC6Hf2usm_ePKOYVJglZo86NCq_XoW9i3J9NtL1LC6jEIYI6aBZrCM0fTSrlDsd9tn551dXg_hjyFsIhSYx_ixKwEk5i2acWYJW0OxxUPDSgNMCQk5w8XXc_RN1V573--io1J6C_FfShq0xo-JjxGKWglLNetLZm5L0cEBT37scRzeFP1VGJTylUdHZVL_uCvDhaXAHEugX3rHnpumu9j5pcW-ciagqCYHHuJRu_UBo4W7aMudaQBCYc719GUns0i1LbAo1GfZDUK2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f67eb572.mp4?token=XT_xjMDLVWBdKqhhB7v3gYHYU7d-VuD4u6_TY8BH2R0x8INigKZZrCIZ3ISCeImfgBIyQWvC6Hf2usm_ePKOYVJglZo86NCq_XoW9i3J9NtL1LC6jEIYI6aBZrCM0fTSrlDsd9tn551dXg_hjyFsIhSYx_ixKwEk5i2acWYJW0OxxUPDSgNMCQk5w8XXc_RN1V573--io1J6C_FfShq0xo-JjxGKWglLNetLZm5L0cEBT37scRzeFP1VGJTylUdHZVL_uCvDhaXAHEugX3rHnpumu9j5pcW-ciagqCYHHuJRu_UBo4W7aMudaQBCYc719GUns0i1LbAo1GfZDUK2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش فعال رسانه‌ای آمریکایی به تهدیدات ایلان ماسک: من در بزرگ‌ترین مراسم تشییع تاریخ شرکت کردم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/671940" target="_blank">📅 02:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671939">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=Qgy1fXpAZIQ0B_w04JAsIz6v1vbpPRbdTdE7IKMeC7Qm9fSHvp7lMUDmrf3nQZa2NnNDbHUT9itLVUayRcTbtDZYgmRgBY3g6JaNwLBMt32HBdu5_3XJ2TNf-VxqsyuqZEeJsQHiAcHNdK5qfCOaq4EViJNklNt-6lRoVqqqf4oYATAD4yeW9Ls84pRhm6nz89wVNP_HgoqTVi8PO_g8l9UIQyjMJytNvrnIgyFG8C5ox6WH2TK38m-5tHufIhYclOp8b8T4bCTSywg9Wx_MM0Tu8OwZJVI8uWXTf1zy_nNFwAuNkfnLk5RYe_HlXErvQqDNFgyqBuT-4Hh45sC0imnb3auf_oDC5Rtb1I6cgoa89-N2SHszIRYh4lv7mrJktwcRgOY7PrgrbRHGw8m8hrWpmajRTvib598oKCETSH7f8m2fIjs4tPL9BSb7TQzpQDlw1rhXw3egI5IQVYsgCJuF7DGYwSPKRaCzcnaSWeocz_4SzQ22Hd4B4TkrrkbwRtqUy6GOWMf7ZjxT9_oOkgm_BXW4EJ-rnN7CJ6bAQnDBnPi4bjUIbvumqkgwe1a1Bl_qAcXyUiEcwYVbvZMDw2dds2LlVjrEj5O-rvT6OcGe8udg0UNrdhN93nprj8xhZmDr28YCuywOMVLasW4epMHBzkaZdq-G2DWTHqVxav4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=Qgy1fXpAZIQ0B_w04JAsIz6v1vbpPRbdTdE7IKMeC7Qm9fSHvp7lMUDmrf3nQZa2NnNDbHUT9itLVUayRcTbtDZYgmRgBY3g6JaNwLBMt32HBdu5_3XJ2TNf-VxqsyuqZEeJsQHiAcHNdK5qfCOaq4EViJNklNt-6lRoVqqqf4oYATAD4yeW9Ls84pRhm6nz89wVNP_HgoqTVi8PO_g8l9UIQyjMJytNvrnIgyFG8C5ox6WH2TK38m-5tHufIhYclOp8b8T4bCTSywg9Wx_MM0Tu8OwZJVI8uWXTf1zy_nNFwAuNkfnLk5RYe_HlXErvQqDNFgyqBuT-4Hh45sC0imnb3auf_oDC5Rtb1I6cgoa89-N2SHszIRYh4lv7mrJktwcRgOY7PrgrbRHGw8m8hrWpmajRTvib598oKCETSH7f8m2fIjs4tPL9BSb7TQzpQDlw1rhXw3egI5IQVYsgCJuF7DGYwSPKRaCzcnaSWeocz_4SzQ22Hd4B4TkrrkbwRtqUy6GOWMf7ZjxT9_oOkgm_BXW4EJ-rnN7CJ6bAQnDBnPi4bjUIbvumqkgwe1a1Bl_qAcXyUiEcwYVbvZMDw2dds2LlVjrEj5O-rvT6OcGe8udg0UNrdhN93nprj8xhZmDr28YCuywOMVLasW4epMHBzkaZdq-G2DWTHqVxav4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت شبکۀ برق شهرهای مورد حمله از زبان روابط‌عمومی وزارت نیرو
🔹
مردم با مدیریت مصرف برق، به برق‌رسانی پایدار به جنوب کشور کمک کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/671939" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671938">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای پی‌درپی در بندرلنگه
🔹
بامداد جمعه، صدای چندین انفجار در نقاطی از بندرلنگه شنیده شد که موجب نگرانی شهروندان این شهرستان شد.
🔹
تاکنون جزئیات رسمی درباره علت وقوع آن، محل دقیق حادثه و احتمال خسارات یا تلفات احتمالی منتشر نشده است./ مهر…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/671938" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671937">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
قطع برق نقاطی از کیش ناشی از مشکل پست برق است  استانداری هرمزگان:
🔹
در جزیرۀ کیش یک پست برق با مشکل مواجه شده است و باعث قطع برق یک منطقه کوچک شده که به‌زودی وصل می‌شود.
🔹
حمله‌ای به جزیرۀ کیش صورت نگرفته و برق دیگر مناطق کیش پایدار و مشکلی در این زمینه وجود…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/671937" target="_blank">📅 01:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671936">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
معاون استاندار: بوشهر مجدد مورد حمله دشمن قرار گرفت  استانداری بوشهر:
🔹
دقایقی پیش برای دومین بار متوالی در چند ساعت گذشته، شهر بوشهر مورد هجوم دشمن آمریکایی قرار گرفت.
🔹
ابعاد و جزئیات بیشتر این حادثه همچنان در دست بررسی بوده و در صورت نیاز به طور مجدد اطلاع‌رسانی…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/671936" target="_blank">📅 01:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671935">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
اربیل عراق در تاریکی فرو رفت
🔹
بر اساس گزارش‌های اولیه، برق در بخش عمده‌ای از شهرستان‌ها و نواحی استان اربیل اقلیم کردستان عراق به‌طور کامل قطع شده و هم‌زمان پرواز جنگنده‌های آمریکایی بر فراز این منطقه ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/671935" target="_blank">📅 01:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671934">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
وقوع چندین انفجار در کویت
🔹
منابع محلی از شنیده شدن صدای چندین انفجار در کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/671934" target="_blank">📅 01:45 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
