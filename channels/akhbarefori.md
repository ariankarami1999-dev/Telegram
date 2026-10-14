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
<img src="https://cdn4.telesco.pe/file/symKfrijcFxG8zN2dWOabAN-U7IFwZ-4dEsPi2Dr3P3ujuMrLTILq7Ol3Tf1TnGCOfs1izT-iU258h9vkp_UWGWbDiZCsuWHoeo2FlmaYRy5Y5toL8V-68tFLKLrblbrqqfy6wghxAMcs1UcFWGdIOVI1IscUBMtg1vv4S9iTwzKcRUONiLYIOhKlOqz07kNSJd9SPBWhjSib7Ipuxa1AuzD9FZIRhij_ccUwkuow2h-jSU8YVFsudC38guFkyd0ASE2suunN8oKoDQaQRl6YmLHsFc6BrePwhfwvaplZHNAVxcKIJxkNiwOMjwTPD54kmdDym-CKCl8WU43pfZ6Jg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 11:20:30</div>
<hr>

<div class="tg-post" id="msg-698332">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMj-kgLR1BqsIpbIlAt5Ir7po0p7jpTlBKLd4pIjL3M3OKsqK0bbQdzNM5Fp-6CErZS2gu_9n-RXEZi55FYIPus7C1Odify14MlSUNUQloeMY9R1gTvqrTwE0LYw_TQhN0xy42zWl-_wavxlxofi4uz5LTg7zrvWyIMz5WW9EYKglGYY9z8baziKaYsUE1sWCzBeqq7nNygv8PuJWAR5lRb3lKONRe7KDlVIh4k6uCzIbexXQAlOIGAsdOdeSQDwmkwD945cMQxWcrGvfeYBWCs3kvqEb7S3xyeTRKuWKqFNsEy88hfdEgG3tcWzcoK6PAjut6-RHld0Y6Labi8bbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ تب عفونی مهم که باید بشناسید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/698332" target="_blank">📅 11:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698331">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قانون انتقال سهمیه از کارت سوخت به کارت بانکی در پنج استان اجرا می‌شود
رضا نواز، سخنگوی جایگاه‌داران سوخت در
#گفتگو
با خبرفوری:
🔹
از زمان اجرای نرخ ۱۰ هزار تومانی بنزین مصرف بنزین در برخی روزها حتی بیش از ۷ درصد کاهش داشته است.
🔹
مشکلات مردم و جایگاه‌داران از جمله اختلال در پرداخت با برخی کارت‌های بانکی و مسائل مربوط به سوخت‌گیری موتورسیکلت‌ها در طرح شناسه‌دار کردن کارت‌های جایگاه‌ها درحال پیگیری است.
🔹
طرح انتقال سهمیه سوخت به کارت بانکی پس از حدود ۶ تا ۷ ماه تأخیر در تصویب آیین‌نامه، ابتدا در دو جایگاه تهران به‌صورت آزمایشی اجرا شد و اکنون اجرای آزمایشی گسترده‌تر آن در پنج استان البرز، سمنان، قم، قزوین و همدان دنبال می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/698331" target="_blank">📅 11:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698330">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به صیادان سیریک ۳ مصدوم برجا گذاشت  استانداری هرمزگان:
🔹
یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدودهٔ بندر کلاهی برخورد کرد؛ براساس اطلاعات اولیه، درپی این حادثه ۳ نفر مصدوم شدند؛ مصدومان درحال انتقال به ساحل هستند.  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/698330" target="_blank">📅 11:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698329">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnKN9SrKD7AM16iajmKFnuFBcBakwvKKEX_GPYhRQREV1bcvV81DyN41uVOJ_2b0BTGL8XyBJ1AIslJPYyE7DQxkZ3HZFLbIawoq25EBm4Dx7QJC35IRsqmfBkbTVs5zBkGSHS_ojPwOEXAS5kLPrTH79RDqlJs5maquneLQEKyoskLDK7Mxj4HdNI9wbo9HHZrk0RUIlE7QLRSCCurZ4jmq195YOaOyhgLyXYw_vblVAcr4iKZV6S5ImCiiAD75G_jXyawwX1P1gMqB1WmAKwSOm_j2eMPL1pHssgZ2YLz4gXVn0pcZ1mu_ITZTNZgpN0bx5XSquroYALn27bqBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دمنوش میخک؛ نوشیدنی خوش‌عطر پاییزی برای روزهای سرد سال!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/698329" target="_blank">📅 11:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698328">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ترامپ ازدواج پسرش با سفیر آمریکا در یونان را تکذیب کرد
🔹
کیمبرلی گیلفویل عضو خانواده من نبود. گمان می‌کنم مدت‌ها پیش با پسرم رابطه داشت، اما [عضو خانواده] نبود. #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/698328" target="_blank">📅 10:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698327">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSeQl6zGUTBw0_a8Mo2ljCVgFNhK19E7-OuN20jn_VaVBOmNYW-9_Fu_v8QtXqx8HWxztlyAjwv__LbHb3wyQpFe5uR7-dMfHopvlimOrz5h6ZCsqUFKLeXyazmlUM8W3cF9hDUCCAfk_8TwCYlu33TbbIDV1HQ6rnNZfrhb2N2SJtiv37A_QbxqhaA9EMvyy89JogZ6rHbxKPvD2CwqKIdqwctUNEMvPpN9YkcIX-h_KsTqD38luGd7X0y4bFnN0txAWeP8SYfQ3P3O3E9IolnPYVN2sy7dYBXBf_ojeFbmy3Zl2iLqhRxGBGpX2v1onwgNuHrx17jtGML6eWfbIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقایسه دو فاکتور خرید با فاصله ۲۴ سال؛ شهروند آمریکایی: قیمت اجناس ۳ برابر شده، داریم بدبخت می‌شیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/698327" target="_blank">📅 10:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698326">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4429aa44cc.mp4?token=nXPdpwSpsnfEIPr99FJPq9r8Q1tjKt-pufQ2a1UWXLCTPi7dNsCKEQwdA-40sSrNfIZS0wVGZkPz1U5rTuYQZUjNvqu0w4apyqZrCqVLHkCuaAwbkJIAUHVFtRfkEEP-rt1KHLY8m_9vZsEO5eYvqAz-ayl2ZKOFODAA0HibfJ2W8uHdHMQswpFU9YN92EJ4FMPBHSQTcwqw4jc44j-ZMqFHAP0UOIFmE7ZJfFJSBH9GSBrNE1HAJj-Q1DobqCk7hKIe6cBNNltDdm9AaTOgH2Foba0QbGAtzAdgS1kbfFFpbSmyPhLA0F3XJK2tSYwfkAY2VVujrU9cWPAdv6mJrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4429aa44cc.mp4?token=nXPdpwSpsnfEIPr99FJPq9r8Q1tjKt-pufQ2a1UWXLCTPi7dNsCKEQwdA-40sSrNfIZS0wVGZkPz1U5rTuYQZUjNvqu0w4apyqZrCqVLHkCuaAwbkJIAUHVFtRfkEEP-rt1KHLY8m_9vZsEO5eYvqAz-ayl2ZKOFODAA0HibfJ2W8uHdHMQswpFU9YN92EJ4FMPBHSQTcwqw4jc44j-ZMqFHAP0UOIFmE7ZJfFJSBH9GSBrNE1HAJj-Q1DobqCk7hKIe6cBNNltDdm9AaTOgH2Foba0QbGAtzAdgS1kbfFFpbSmyPhLA0F3XJK2tSYwfkAY2VVujrU9cWPAdv6mJrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به صیادان سیریک ۳ مصدوم برجا گذاشت
استانداری هرمزگان:
🔹
یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدودهٔ بندر کلاهی برخورد کرد؛ براساس اطلاعات اولیه، درپی این حادثه ۳ نفر مصدوم شدند؛ مصدومان درحال انتقال به ساحل هستند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/698326" target="_blank">📅 10:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698325">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ملاک‌های جدید تعیین وسع اقتصادی برای دریافت کالابرگ چیست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/698325" target="_blank">📅 10:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698324">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سازمان تأمین اجتماعی و صندوق بازنشستگی کشوری خبر منتشرشده در فضای مجازی مبنی بر «آغاز پرداخت وام فوری ۱۲۰ میلیون تومانی به بازنشستگان و مستمری‌بگیران» را تکذیب کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/698324" target="_blank">📅 10:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698323">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrrGyh1doJ2Gv2PJJdvvsRBJ3H9BAne3D_KiW63Y7n8s0YjPEqTFAOqJHSK-yEpxTlLQodYnAJ6DzgWSKCe-nIYdcB9AYPbco0hQh3OeHML3vPaBuX7zzgZAEuFs1Pk-GLTEgqiYnNpvkrB4QVMi4xJwnYZ7WvRRuNn1tQfXpIgxoqwUhGFu2MmU22l7k_gC8oqfi84mhJcHhN9w0J-pIO2YOlz7pjYjYE2iYCf6R24FIvBPi5IuqimLJ-LP55ZnQVqsEqhXRQ1-JHVHGQKq7emAJ-i7xGqvnkKK6zwbcOc1mI_qeTN5ROHuNgKO6_bTL8qxDZBQiWclE_F09k_H1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناریوهای مواجهه ایران و آمریکا در آستانه انتخابات کنگره/ چرا کوه‌های اصفهان هدف جذاب‌تری از عملیات زمینی است؟
جنگ در منطقه به کجا می‌رسد؟ تحلیلی درباره محاسبات واشنگتن، تل‌آویو و پایتخت‌های عربی را در ادامه بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3252254</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/698323" target="_blank">📅 10:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698322">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81452d05f8.mp4?token=f5RhYo0BSkpuFvbmotsZU29ZvkkDEnp4G4KFwu8GnIWU46mStgSk2flsJJ-cSpKke26Q8U7YIv0j62-wwUKdU7lprasoFXx0VYISI43WzLa432cW-CnwHOERUIetCMaUO-1lpS_FMiwSSlUPBxgZqLsjMSNi0xTxpefaKJ3ls8AehtL3ITQlDlKowMS-9GyWWw3Fz_MQbzd1vLnR-MYrzxZQwnriZirku08JFhlc75USj5C411iuvV1CzZqsLne2cZxNYUs5Z3tUIXiqMKWzqYh332I-qSc08a036bLvdT5boLG40eRCcTsZyiM_XSY4CZ_rQM0VMvrn0w85Bmd_jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81452d05f8.mp4?token=f5RhYo0BSkpuFvbmotsZU29ZvkkDEnp4G4KFwu8GnIWU46mStgSk2flsJJ-cSpKke26Q8U7YIv0j62-wwUKdU7lprasoFXx0VYISI43WzLa432cW-CnwHOERUIetCMaUO-1lpS_FMiwSSlUPBxgZqLsjMSNi0xTxpefaKJ3ls8AehtL3ITQlDlKowMS-9GyWWw3Fz_MQbzd1vLnR-MYrzxZQwnriZirku08JFhlc75USj5C411iuvV1CzZqsLne2cZxNYUs5Z3tUIXiqMKWzqYh332I-qSc08a036bLvdT5boLG40eRCcTsZyiM_XSY4CZ_rQM0VMvrn0w85Bmd_jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سحرگاه پلور و منظره زیبای دماوند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/698322" target="_blank">📅 10:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698321">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای نتانیاهو کودک‌کش: اگر مخالفان [من] در انتخابات پیروز شوند، هیچ اقدامی علیه ایران انجام نخواهند داد
🔹
آن‌ها از لبنان و غزه هم عقب‌نشینی خواهند کرد.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/698321" target="_blank">📅 10:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698320">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سخنگوی وزارت صمت: میانگین مصرف سوخت خودروها در هر ۱۰۰ کیلومتر، ۷.۲ لیتر است/ نسبت به آمار جهانی بالاست اما نسبت به آمار گذشته خودمان کاهش یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/698320" target="_blank">📅 10:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698319">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCFb1VNsIPnCyBVzGpI-UU7GKH8A1yde1xky_ag_5VTFRIwLAz3v3EHI3i__0_vja_CiYqXhuMPNIEIxyZGuA3hBW34OoiMjD1eB7h4Mp3P7e_k5ZvAiHs-J2GHf1IMn4uJ3DOf72-qbJwC0YIE8SgR7xCu7VZ2X21YJjsi9_wDPLKmCyhg-OzvP-Gomdv-wpUVzD_FhJ41viSpH-OXkMDhx9UEDJYIUHhf5jKwA5GNIz4zfnnpXhFwsti9x0ZJSPPUnS2fT3y9NehItvgSundh07ExgipuhoNWXuu4c8oQbVIGtsfXsH0qe-LT3SG_RJTADQfZDs1OA7MCnv2PMIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس دادگستری کرمان: تروریست اعدام‌ شده در کرمان قصد تسخیر فرودگاه برای ورود رضا پهلوی را داشت
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/698319" target="_blank">📅 10:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698318">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9c88c1e6.mp4?token=FKpJY38WGBUN_pbyrRHez_vSQ2-Vv0ArWPtibTUQZi9DbentrQWh9NlGKImEtZBZYzbDBrPWrBzanGy_eaLHCSP-HSo9UnPu9f0DhI266F__L8689efpcGC-iCXUOkb-3LqXNPExlThI8hJRauOLHKxzvAYCLtnMb2lQbV7gLTUja8VfwEpFc41zZ8Rp0lK_W7JERNGbfsyhXC2BVGIETkaUcH8H_AqTFnHL-bTpW3APekxiLZ71X6Vx0UnX_1yb5v5KhtFVuhbxpEmApWJHgHFwxlqJmq2uwCcJh9WnRZIDukF2JIhUBYemMFx4H-vtEhTuPFVSWMEJ8gM4xszclw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9c88c1e6.mp4?token=FKpJY38WGBUN_pbyrRHez_vSQ2-Vv0ArWPtibTUQZi9DbentrQWh9NlGKImEtZBZYzbDBrPWrBzanGy_eaLHCSP-HSo9UnPu9f0DhI266F__L8689efpcGC-iCXUOkb-3LqXNPExlThI8hJRauOLHKxzvAYCLtnMb2lQbV7gLTUja8VfwEpFc41zZ8Rp0lK_W7JERNGbfsyhXC2BVGIETkaUcH8H_AqTFnHL-bTpW3APekxiLZ71X6Vx0UnX_1yb5v5KhtFVuhbxpEmApWJHgHFwxlqJmq2uwCcJh9WnRZIDukF2JIhUBYemMFx4H-vtEhTuPFVSWMEJ8gM4xszclw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چیز کیک تام و جری/ بیاین پنیرهای خوشمزه‌ی تام و جری رو با هم درست کنیم!
🧀
🐭
مواد لازم:
🔹
۱ پاکت خامه
🔹
۳۰۰ گرم پنیر خامه‌ای
🔹
نصف قوطی شیر عسلی
🔹
زعفران یا رنگ خوراکی زرد‌ به مقدار لازم
🔹
۲ قاشق غذاخوری پودر ژلاتین ﻿#آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/698318" target="_blank">📅 10:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5dut7LA08kLgMTPeG9SdKUb_IgTAVaucMtBvzH8QEOc9AqiHNvO5tTAeiEs0LEdZK0sObhlF75b9vU6NY55GMIm0-rnGyMxgyi5QHrLftHmjB5LeJq7Q-QZWFz-Tm1Xn8S0yNGWFsyJEVbH2zdBknhQ0jelMtAp-d3zpgTMxp_eJBd0u13bAn67fHZbW22dqtjSZQehJDB6kAZJ66UILQtWJ8WGWWDXBYn4PC0Z1Tq32dgral9ZZBXu68vdDBDlh8S7l5XF3hnRjrR3XBLe8NmaZNoc_S6G0yq8SkBAurEYBz66EAXZUSfKDMpbNQ8TSSZ8p3rC_Wbknd1eGTfBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDdBFtlO2AdCEIzTY41pfM008kI6esLxkv9hsX_xvPRxTDppnDe4vQosIUnc_gtxqYKoYkdG7I5QH5WZNAiVIdgt-okyqSCFBC5prkQVnj1hdJINe80EcAzbXQ2fZ3HZpQPSEZk2npE3UjVr_l8vQjF3v-WaaZKkCFEAIqQbdtqIY8sTmfw_FEIGkiHHaAmrWG0CHjGtFJicwEuPAqc_aEfFGMNboclHhE18KJKdXdH8qeB6SE1cJEJkKgqE3LoFhEZ9YMh1hQ77UlmvPNJKKB697HHlSmXx6Rq_aUbmASlFkJo9oyWBfBgCFnaMXHbUkOH6DUyt_NTi4c7EYs24eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E6IYmMNhIFRbEVvOgcet2v6KGwYDP3oP9iKFGms-bf6BcNlidbW5hCZi25XvUO7FbRZ0PEklxBzP9qa_1LbncJhKTe-Fe4UioEjua2ILPG4Bp2awU76M3hrH17j43JlpqHb7fiuB8BL_nRrz8UD8Pb6CYKdTNhvnpOQP4mIpEgiAhlQuOt6X8iVf1Q5XQ8JN2fBKiF9eGkhQMHkhTLhp8-3WaLEIJFJWpDJp91c3hflMm9Y9zDfFClYjqYnzo3zhHvOJiZrckmKB6FkO5KmGLSJ1J4Wl3mqLP23bo1KrjsSo4GxusX7zkD2WSvInpJAc9HP5EzCEUlQtxDbkWOEVuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اعدام تروریست مسلح در کرمان
🔹
حکم اعدام علی‌سینا مصطفوی، تروریست مسلح و عامل دشمن آمریکایی‌ـ‌صهیونیستی در جنگ تحمیلی اخیر که در چند عملیات تروریستی مسلحانه موجب مجروحیت شماری از شهروندان کرمانی شده بود، اجرا شد.  #اخبار_کرمان در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/698315" target="_blank">📅 10:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی یمن به تأسیسات نفتی آرامکو
🔹
گزارش‌ها از حملات موشکی و پهپادهای انتحاری یمن به پالایشگاه نفت آرامکو در شهر جده عربستان سعودی حکایت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/698314" target="_blank">📅 09:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
مبالغ جدید وام‌های دانشجویی اعلام شد
🔹
وام تحصیلی، در مقاطع کاردانی و کارشناسی ۷ میلیون تومان و در مقاطع کارشناسی ارشد و دکتری حرفه‌ای ۱۰ میلیون تومان است و در مقطع دکتری تخصصی، دکتری مستقیم و دستیاری ۱۵ میلیون تومان اعلام شده است. این مبالغ برای متأهلین نیز به ترتیب ۱۴ میلیون تومان، ۲۰ میلیون تومان و ۳۰ میلیون تومان اعلام شده است.
🔹
وام شهریه نیز برای مقاطع کاردانی و کارشناسی ۵ میلیون تومان، کارشناسی ارشد و دکتری حرفه‌ای ۷ میلیون تومان و دکتری تخصصی ناپیوسته ۱۰ میلیون تومان خواهد بود.
🔹
همچنین وام ضروری نیز برای تولد فرزند و ازدواج ۲۰ میلیون تومان و برای حادثه‌دیدگان، بیماری خاص، لوازم کمک‌آموزشی و بلایای طبیعی ۱۵ میلیون تومان تعیین شده است. وام عتبات عالیات نیز ۵ میلیون تومان و با تشخیص رئیس صندوق ۲۰ میلیون تومان اعلام گردیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/698313" target="_blank">📅 09:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698312">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f845fba2a2.mp4?token=sKRL5QwLKCoKlHTQFBs7Xlfj8Y7uajVsmQR53hLgMASih0g_gWj6atO68HD2z54bGmmb0OkWjq57AQtRz1zQxY30BNfTpp6gWM261fjBQekPQrH6r5ZDkqxLrhMKiNKFgneWDlJlC1o_TSGRmFSbrTxWtw11c14i2t0lZTd15J5C2xdGziSCaRldVUOm3rF8djurpRX1dfdFImycsGX8i-fjKEAWY5EGqrBzXmbvnlcEWb1D0vXsyCUrQ733yS55V5XyPtkgLueLb5MrgJXTmPF6_HyYYw0k63vhd1xBaI9DX8krNQGKRUoVjh8_Jb5ecC1kD5k-lIqbo1dFUBSgOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f845fba2a2.mp4?token=sKRL5QwLKCoKlHTQFBs7Xlfj8Y7uajVsmQR53hLgMASih0g_gWj6atO68HD2z54bGmmb0OkWjq57AQtRz1zQxY30BNfTpp6gWM261fjBQekPQrH6r5ZDkqxLrhMKiNKFgneWDlJlC1o_TSGRmFSbrTxWtw11c14i2t0lZTd15J5C2xdGziSCaRldVUOm3rF8djurpRX1dfdFImycsGX8i-fjKEAWY5EGqrBzXmbvnlcEWb1D0vXsyCUrQ733yS55V5XyPtkgLueLb5MrgJXTmPF6_HyYYw0k63vhd1xBaI9DX8krNQGKRUoVjh8_Jb5ecC1kD5k-lIqbo1dFUBSgOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش عجیب ترامپ به ماجرای کشته شدن یک فرد در باغ‌وحش یورک‌شر انگلیس توسط ببر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/698312" target="_blank">📅 09:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698311">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
حنظله کابوس شبانۀ مقامات صهیونیستی
🔹
گروه هکری حنظله در پیامی با اشاره به باقی‌ماندن ۱۳ روز تا انتخابات رژیم صهیونیستی، از آغاز مرحلۀ جدید فعالیت‌های خود با محوریت انتشار اطلاعات و افشاگری دربارۀ مقامات و شبکه‌های صهیونیستی خبر داد.
🔹
حنظله در این پیام، انتخابات اسرائیل را «روز بزرگ دروغ دموکراسی» خواند و اعلام کرد که از این پس، فعالیت‌های این گروه با تمرکز بر انتخابات و انتشار اطلاعات مربوط به مقامات و ساختارهای رژیم صهیونیستی ادامه خواهد یافت.
🔹
این گروه همچنین اعلام کرد که به‌دلیل محدودیت‌های موجود، اطلاعات و مطالب موردنظر خود را از طریق دو وب‌سایت Distributed Denial of Secrets و Drop Site News منتشر خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/698311" target="_blank">📅 09:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698309">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی یمن به تأسیسات نفتی آرامکو
🔹
گزارش‌ها از حملات موشکی و پهپادهای انتحاری یمن به پالایشگاه نفت آرامکو در شهر جده عربستان سعودی حکایت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/698309" target="_blank">📅 09:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698308">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رویترز به نقل از مقامات ارشد ایرانی: ایران در حال به‌کارگیری تاکتیک‌های جدید برای حمله به کشتی‌های عبوری متخلف از تنگه هرمز است تا قیمت نفت پیش از انتخابات میان دوره‌ای آمریکا، کاهش پیدا نکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/698308" target="_blank">📅 09:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698307">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: حوثی‌ها با استفاده از قطعات وارداتی از چین، در حال ساخت موشک‌های بالستیک میان‌برد پیشرفته است
🔹
این گروه قطعات تخصصی جهت ساخت نسخه‌ای از موشک ایرانی «خیبرشکن» را وارد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/698307" target="_blank">📅 09:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698306">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVRl8OKHoG9ie2-YGCwXoECkhcUH7Bu2DUdkgOcYj9SbSsaf30l1AtelaUUOCOX0eo-wAWWWQny-S31zwat7yizBUJOp15pMro8knSrV3cXZAtYfZrRY7pJWDyW5uKIeKv_x1PKKmWR-DFi2rGSQVNzT0cxLMWVWOFHj4EHirsVO6P-9NnCJr_FaSG4eR6Ki8YHtlyNLCaDgalmCUsNIEsZ7uRMQOyrTywS_a-eDrzHX6EbjlUbw52p4woiUDagSLH34CxsHaTMChovgaBk5AdDFG_M1jXloV7DrR5aFWmo6IWmHnW41YCz-WYrSJ8pQNhnoodjcXlmo0ulTlutcZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری تماشایی از کاخ فتح‌آباد، کرمان
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/698306" target="_blank">📅 09:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698305">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a696a0da2.mp4?token=Oh5vS2xFKUB-VgROPypDV6nYybYZ5vlx-lcl33kebevgHKKR6Z2ZFxyMKKd3fYb6SCqjuiEf5ErISS3z6noIUlYNnE3_TPOWGxL1EbMA4kKE5KFdpURVFaeBIjdhea_E3_9k3TbQa7kYtufrf3l6I5Qq0LikpmnGtW7kvwaYFA8i-teanGvZY5Ot-1JxYxa9vp_AyBZDjT3IL6JDzP5hKQEYDl1XGMc_lpqlhnKxm5zeDyzrfaWAXRMUd8KEutgZCEmL0UC6x9LZ1tQn0bP3HVQZMZt7yIBDQ53yR7aZmFmQmqK3DVO55n2twCIl9ZNtEojnbR-hs5emPdI0SZtJQERbUXPBNN5vsUaI4co1hDiJ00Xopf6osZDgtcFpZVdQGWlAjEhGA2TSGU_DM31LrWqYiUMWiRIPfdyd6hHeypHXmwxTuc2dVzaREhAowJy9YGeAAZFfyIjrmYfcWrifudWRyxGcNk0x-iRMgXQsYxJx0vDJEvsuslpfkJhkTYrU8tCVPEqul9yj1muYtyvbLjQc9qPgRSlkqqHCzMooQkhF99JaUstB2kGGv0VQrloBRfVqLkK4crgPFh9GDef-O3KPby5zB5cFvw0zQukSnaKCM34bjtOH1Zh9otyzCXawkkUOcrUA6vb3R1CFrWmvSZkGli_Ga9n4Q0vEkcm13rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a696a0da2.mp4?token=Oh5vS2xFKUB-VgROPypDV6nYybYZ5vlx-lcl33kebevgHKKR6Z2ZFxyMKKd3fYb6SCqjuiEf5ErISS3z6noIUlYNnE3_TPOWGxL1EbMA4kKE5KFdpURVFaeBIjdhea_E3_9k3TbQa7kYtufrf3l6I5Qq0LikpmnGtW7kvwaYFA8i-teanGvZY5Ot-1JxYxa9vp_AyBZDjT3IL6JDzP5hKQEYDl1XGMc_lpqlhnKxm5zeDyzrfaWAXRMUd8KEutgZCEmL0UC6x9LZ1tQn0bP3HVQZMZt7yIBDQ53yR7aZmFmQmqK3DVO55n2twCIl9ZNtEojnbR-hs5emPdI0SZtJQERbUXPBNN5vsUaI4co1hDiJ00Xopf6osZDgtcFpZVdQGWlAjEhGA2TSGU_DM31LrWqYiUMWiRIPfdyd6hHeypHXmwxTuc2dVzaREhAowJy9YGeAAZFfyIjrmYfcWrifudWRyxGcNk0x-iRMgXQsYxJx0vDJEvsuslpfkJhkTYrU8tCVPEqul9yj1muYtyvbLjQc9qPgRSlkqqHCzMooQkhF99JaUstB2kGGv0VQrloBRfVqLkK4crgPFh9GDef-O3KPby5zB5cFvw0zQukSnaKCM34bjtOH1Zh9otyzCXawkkUOcrUA6vb3R1CFrWmvSZkGli_Ga9n4Q0vEkcm13rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعت آبی مسجد همت تجریش؛ سازه خلاقانه و جذاب که بدون نیاز به برق یا باتری کار میکنه
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/698305" target="_blank">📅 09:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698304">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
سخنگوی وزارت صمت :صنایعی که اقلام غذایی، دارویی و بهداشتی تولید می‌کنند، شامل محدودیت گاز در زمستان نمی‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/698304" target="_blank">📅 09:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698302">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89d54b2c37.mp4?token=mPdZ4Ii1KTAP4fPblQupyhrGUWJVC1uFgWQQ9-2cEPtCFN6dEaMlYmFQ6yEC_0Dr23QL3IcSOnZdnNNV7lNCn4c8f3whvfRX3YoD2HON75IxsgHo7sd8bF7Mnde4q4zbjnVilj4EIxkCSZyUwRllDdLznUXEJErcz09s1lGOBRXoTSyUL5WOqmDAuEDCjWO_JGLxGY9PhNd_jFbp9LQrcHjet8RijZ8ikAD4832jA1BsBGoCYFpJDtu9ePB78SXC6wqR113HKzQEW_Ca4T3sptq1qrO2wxMq0Urv__UDi04GOAlm_IppQQk2vdzRWG593sPQsDfdmbQYq0dw0vNA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89d54b2c37.mp4?token=mPdZ4Ii1KTAP4fPblQupyhrGUWJVC1uFgWQQ9-2cEPtCFN6dEaMlYmFQ6yEC_0Dr23QL3IcSOnZdnNNV7lNCn4c8f3whvfRX3YoD2HON75IxsgHo7sd8bF7Mnde4q4zbjnVilj4EIxkCSZyUwRllDdLznUXEJErcz09s1lGOBRXoTSyUL5WOqmDAuEDCjWO_JGLxGY9PhNd_jFbp9LQrcHjet8RijZ8ikAD4832jA1BsBGoCYFpJDtu9ePB78SXC6wqR113HKzQEW_Ca4T3sptq1qrO2wxMq0Urv__UDi04GOAlm_IppQQk2vdzRWG593sPQsDfdmbQYq0dw0vNA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوش مصنوعی جدید انویدیا؛ گفتگو با ربات، درست مثل حرف زدن با یک انسان
!
🔹
با PersonaPlex-7B، یه مدل رایگان و متن‌باز که هم‌زمان گوش می‌ده و جواب می‌ده، مکالمه با هوش مصنوعی دیگه شبیه چت کردن نیست؛ انگار واقعاً داری با یکی حرف می‌زنی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/698302" target="_blank">📅 09:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698301">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b835bc2e1c.mp4?token=pfLLW8VhdAVHGju-KewYhizuJXoiPqL8z_pwdciRz_T83A5YrcFdhzWl4K7dMvgz-FEzBc-IaUSr9kQEuY2cwlDEnYa4WDdWPCZaiBHr-RFzaaErePDTgfXttYgykyHp0S_c6twjBfG394Xhn4N8C-2hSw7u9z8j4AUlfH-1U1f7n88QpWZAikBEmhB5hRF0cAnaR6QEZXodXMQxljS_3lxSsxHVREjl-soKmf5EYhU4Sn8RbIXOrVwDBt1X57ELD4jScRYhvRrvYwyGWHcI4wXKhEnjfky2CWr_vpdD_cJkHzAfw0j_sGw4gvjVoHbEr2eDYT2iztdGyZjXk2lxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b835bc2e1c.mp4?token=pfLLW8VhdAVHGju-KewYhizuJXoiPqL8z_pwdciRz_T83A5YrcFdhzWl4K7dMvgz-FEzBc-IaUSr9kQEuY2cwlDEnYa4WDdWPCZaiBHr-RFzaaErePDTgfXttYgykyHp0S_c6twjBfG394Xhn4N8C-2hSw7u9z8j4AUlfH-1U1f7n88QpWZAikBEmhB5hRF0cAnaR6QEZXodXMQxljS_3lxSsxHVREjl-soKmf5EYhU4Sn8RbIXOrVwDBt1X57ELD4jScRYhvRrvYwyGWHcI4wXKhEnjfky2CWr_vpdD_cJkHzAfw0j_sGw4gvjVoHbEr2eDYT2iztdGyZjXk2lxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری وحشتناک از سیل ناگهانی در منطقه گورخا، نپال، خانه‌ها و پل‌ها را با خود برده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/698301" target="_blank">📅 09:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698300">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه بیست و سوم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/698300" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه بیست‌وسوم؛ فرصت عافیت
🔹
در میانه‌ی نام المنتقم حق، عده‌ای آگاه شده، خوف پروردگار در دلشان جاری می‌شود و در نور عفو الهی، مسیر بازگشت برای آن‌ها مهیا می‌گردد.
🔹
در شرایط بحرانی، انسان‌ها باید با یکدیگر همدل و مهربان باشند، و با هم به انصاف و بر محور اخلاق کریمانه رفتار کنند.
🔹
در این زمان، افراد باید با باور قلبی و مهربانی و شفقت، اجازه ندهند شیطان با مجادله‌های فلسفی، فضای جامعه را به سمت تاریکی  پیش ببرد‌.
🔹
نور عفو الهی، عافیت را به خاک و آب و هوا و نور سرزمین ایران ارزانی می‌دارد و بزودی با احترام و نیتی عظیم یک‌دست می‌شوند و با شکوه و اقتدار به سمت افق روشن حرکت می‌کنند.
🔹
هرگونه خدمت به سرزمین ایران، خدمت به نور الهی است. در فرصت جهادگری، انسان باید حق و درستی را بشناسد و در حمایت و خدمت خلق با‌شد تا به امنیت روانی برسد.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/698300" target="_blank">📅 09:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698299">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8aj_JB-rN5S2CbA-_CekHmHQmbov6TxE40tC44PiN2B0L3H1Pyd6FvkOOETedN_9Zoxn0f3cMB_BLLXxg0k9soFpNdxIUyrajeuUY_w3gObXjmQljA6B-5vabOArnFIV8fuomfgM_aZ4bHn11Hvd9oiQbfQgTbRubGbN4HGuRbeJb1oEC2gFWnIJmbq79YiKw2Udh1wbF2Y3PbgSEcJ6pl-ZA0CfkOu50sEuU6JmFiOREpiGg0c90QCTpcHcg_4-NNuCsYp1ozH0Sm6BfnkLsXQ9Y2xiPNcJRwVBxcQ1gNclptEKlGdyBmlnfeRd9uzTATd_Ey7rKJWBVUn5LTv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان‌بندی مراجعه به سامانهٔ درخواست افزایش کالابرگ   رقم انتهایی کد ملی:
🔹
چهارشنبه:  ۰ ، ۱
🔹
پنجشنبه: ۲، ۳، ۴
🔹
جمعه: ۵، ۶، ۷، ۸، ۹
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/698299" target="_blank">📅 09:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698298">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1211f84ae.mp4?token=JsUrDXzAvTlKlj-QqMFZbm_5to0KyRPArFIOz_VO06Hj9SFcnDUDcQLBAi49NLlP0kQs8EvvO9xEUY7DkEWuEkzQk0MhNCDn6DFCiuQd9lnAh_mLIJOt-v6COXCFP7jiCEjZHsmIIJXFlyK5hdblnFlwYJRh_v0G_-KdWbH0dzXLstFpXHZrLHVAS-z060kF9lbtlFgICgrEckKlfuj5H81nBPTHj3VNebzKvMWxj5FMZT-dv5d0c1PWK8VQ7Dw23U5k71JZmBDY9TKTp6GJwXBK2E9PJN6ajNyE6MpTA7FrygWwXo72iWOabKtidXlL3iA2Vplj101FFe4yHhnQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1211f84ae.mp4?token=JsUrDXzAvTlKlj-QqMFZbm_5to0KyRPArFIOz_VO06Hj9SFcnDUDcQLBAi49NLlP0kQs8EvvO9xEUY7DkEWuEkzQk0MhNCDn6DFCiuQd9lnAh_mLIJOt-v6COXCFP7jiCEjZHsmIIJXFlyK5hdblnFlwYJRh_v0G_-KdWbH0dzXLstFpXHZrLHVAS-z060kF9lbtlFgICgrEckKlfuj5H81nBPTHj3VNebzKvMWxj5FMZT-dv5d0c1PWK8VQ7Dw23U5k71JZmBDY9TKTp6GJwXBK2E9PJN6ajNyE6MpTA7FrygWwXo72iWOabKtidXlL3iA2Vplj101FFe4yHhnQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روش ساده و کاربردی برای از بین بردن خط‌وخش‌های سطحی خودرو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/698298" target="_blank">📅 08:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698297">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
زمان‌بندی مراجعه به سامانهٔ درخواست افزایش کالابرگ
رقم انتهایی کد ملی:
🔹
چهارشنبه:  ۰ ، ۱
🔹
پنجشنبه: ۲، ۳، ۴
🔹
جمعه: ۵، ۶، ۷، ۸، ۹
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/698297" target="_blank">📅 08:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698296">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658a666e94.mp4?token=CSUa0mVlVpCqc5X6uhqccLhy6I4g3LQ7DhB9Wi3h6H2DiX44MJ9KDqB9h80EQKmuZG_4Sl_aGPVI_MRP2w1XsOCGxmw6s-B7X0hx7W4XYNZk8Vh3PUCWMFNknHC4yULcUjBy1CGvnDfaOICG2oI0GnKDxuhJNfhOmP5GFJIC9WeadpEL--Rw4-6zMf6JlKpBDHvb_uGL2zxZztYoPISzbGYvTu2nT44WiX5vrkW05z6Vv6D1CA2xPlKswX8vY0e-69AbJZAICFEMDC00ucFhUlGPVWFwvJAOjaxL1lweKtM5mfc75s2udEGAV4RGRxFGwXFTytk6ptCmiERuKvM-WxKAsJdzsMNYAHROX4350za7NoW__vYwAjJeiuni6kNyDdHxT7G9yhpHMJJQLnbQZch2XY2dsFzClIFVwRMnYjSk12WR8al6X-Z3FQVyHD83wBOmtF2TXJHgwaF2nx0H_R5SisiXOo5Ez_QxJhxzFt1FNrUgmO41h8ef8ECcN6ZHQRL9WPFPpftTpg1nM_yvY1w9XIABXkEtGcEtjWZsk95rD-wdOWgSkBNbGDhKYlqD1TYDuQCNy_B3e3E9Po3zrJSlqjCcleVD4HRA8Iz14WLNTT7MZoV9nRGtEKBEg8Nok5GbUX7k1a9iw2rozq5R2nPgmGvGI9HPREEVFLGKiY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658a666e94.mp4?token=CSUa0mVlVpCqc5X6uhqccLhy6I4g3LQ7DhB9Wi3h6H2DiX44MJ9KDqB9h80EQKmuZG_4Sl_aGPVI_MRP2w1XsOCGxmw6s-B7X0hx7W4XYNZk8Vh3PUCWMFNknHC4yULcUjBy1CGvnDfaOICG2oI0GnKDxuhJNfhOmP5GFJIC9WeadpEL--Rw4-6zMf6JlKpBDHvb_uGL2zxZztYoPISzbGYvTu2nT44WiX5vrkW05z6Vv6D1CA2xPlKswX8vY0e-69AbJZAICFEMDC00ucFhUlGPVWFwvJAOjaxL1lweKtM5mfc75s2udEGAV4RGRxFGwXFTytk6ptCmiERuKvM-WxKAsJdzsMNYAHROX4350za7NoW__vYwAjJeiuni6kNyDdHxT7G9yhpHMJJQLnbQZch2XY2dsFzClIFVwRMnYjSk12WR8al6X-Z3FQVyHD83wBOmtF2TXJHgwaF2nx0H_R5SisiXOo5Ez_QxJhxzFt1FNrUgmO41h8ef8ECcN6ZHQRL9WPFPpftTpg1nM_yvY1w9XIABXkEtGcEtjWZsk95rD-wdOWgSkBNbGDhKYlqD1TYDuQCNy_B3e3E9Po3zrJSlqjCcleVD4HRA8Iz14WLNTT7MZoV9nRGtEKBEg8Nok5GbUX7k1a9iw2rozq5R2nPgmGvGI9HPREEVFLGKiY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرینی برای حرکت انعطاف‌‌پذیری شانه‌ها و کم‌کردن درد سرشانه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/698296" target="_blank">📅 08:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698295">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
اطلاعیه دادستانی هویزه: شایعه اجرای حکم شلاق برای کارکنان پتروپارس در هویزه کذب است
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/698295" target="_blank">📅 08:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698294">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادامه بارش‌ها در شمال‌غرب و دامنه‌های زاگرس/ هشدار هواشناسی درباره وزش باد شدید در شرق کشور
🔹
هواشناسی از تداوم بارش باران گاهی همراه با رعدوبرق در بخش‌هایی از شمال‌غرب، ارتفاعات البرز و دامنه‌های مرکزی و جنوبی زاگرس طی امروز و فردا خبر داد و اعلام کرد از روز جمعه و شنبه از شدت بارش‌ها کاسته می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/698294" target="_blank">📅 08:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698293">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa4581b6c.mp4?token=i00MM3hDZCkH7Q45INIEcrIK-BGj28L5wLm0s7aMlqyV-leQo7RDtgb7I2wP0ly1p-GI4GFRvDqpTCwXN6bhMcwUJJ8DfAsKwPj3HrKgxtAxs33DgKtU_PeNz8ROCSjZeKorsDPuQsCnTj05KYzEmGkv7fcavxl30aVIhkVRg5w6tf1R4l57sZ8ZMSX5X3K_cgMKFN71P6H5EGUWEkI9x_QU93DJQuVVe6e0grqC9zNkWhIYgCYPcgTpOcyAKQpWk3jRw38T-yn4Iob3V-52naPPCTlKTy40E5BSif6XdUipuwbx-XzSkLJNHvD2ZnfZNE8gpqkv7uyM90cDnYielQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa4581b6c.mp4?token=i00MM3hDZCkH7Q45INIEcrIK-BGj28L5wLm0s7aMlqyV-leQo7RDtgb7I2wP0ly1p-GI4GFRvDqpTCwXN6bhMcwUJJ8DfAsKwPj3HrKgxtAxs33DgKtU_PeNz8ROCSjZeKorsDPuQsCnTj05KYzEmGkv7fcavxl30aVIhkVRg5w6tf1R4l57sZ8ZMSX5X3K_cgMKFN71P6H5EGUWEkI9x_QU93DJQuVVe6e0grqC9zNkWhIYgCYPcgTpOcyAKQpWk3jRw38T-yn4Iob3V-52naPPCTlKTy40E5BSif6XdUipuwbx-XzSkLJNHvD2ZnfZNE8gpqkv7uyM90cDnYielQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در میانه اعتراض‌های مخالفان؛ ترامپ باز هم مدعی پایان سریع جنگ علیه ایران شد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/698293" target="_blank">📅 08:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a06b63dbb1.mp4?token=lpSg7tqGb612W9pEcLVp_Q5sQAhZHSxOy7JU-e6Jr1sNIwQUM4xwjfVkDDawbz0xCO51d3YTMoguvUyfbLj4mbWuSOggqO6mbzEtr9I-I9xHOSiz1XaP1AKjmxxE0Q_8kdWGsmAn0xV_DsG8LrwyabQn1wzV3n25Z46RDtld6E0Z4y8r3QMnDwNGVZYChoTP-p9xv7DxN78U7nXVOqko3kdUXb1pdakqijwe38biFnPUiZr_Gg1jLXk7BSHz6jYe5gBmYmnbm4h-ICH-TH-BoS8lj7kiRiPCl0UGcaMJsuD-LZmxhgXmHo-L_v02dKFZxFqpZdTnsDLDoYQNocyTq5x-A6fV_9vd1z-0uj6qNieLqyKwZX8ToXTjVdDqT8mI1bArGMS10De_Rfwyvvi0brS4jHC6YCjeMkud-676CyrmaauCALpiqfbKvS77ej1hdmIN3DOVTX2pOuRjtfPPV6-iYuQstx54UF36WSfR5kdyvwa3K261ojt2PYGbe8ItpEnaOoSu7Qk_HldmgU6NJ9PVFLSfPfWjbZ5gOafjAI9pRhdwM4VPxE4PL-l3cwZc1hVOSRV3LPM0zlRUkLGZHUft91gqPkpSDTHzHf3TyX3wQv-UQG-_Xf82Q3LIgsp_9obLzSMGv4LM7S5Ytbq5XPkifLOYX51Wcy4a4l08CjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a06b63dbb1.mp4?token=lpSg7tqGb612W9pEcLVp_Q5sQAhZHSxOy7JU-e6Jr1sNIwQUM4xwjfVkDDawbz0xCO51d3YTMoguvUyfbLj4mbWuSOggqO6mbzEtr9I-I9xHOSiz1XaP1AKjmxxE0Q_8kdWGsmAn0xV_DsG8LrwyabQn1wzV3n25Z46RDtld6E0Z4y8r3QMnDwNGVZYChoTP-p9xv7DxN78U7nXVOqko3kdUXb1pdakqijwe38biFnPUiZr_Gg1jLXk7BSHz6jYe5gBmYmnbm4h-ICH-TH-BoS8lj7kiRiPCl0UGcaMJsuD-LZmxhgXmHo-L_v02dKFZxFqpZdTnsDLDoYQNocyTq5x-A6fV_9vd1z-0uj6qNieLqyKwZX8ToXTjVdDqT8mI1bArGMS10De_Rfwyvvi0brS4jHC6YCjeMkud-676CyrmaauCALpiqfbKvS77ej1hdmIN3DOVTX2pOuRjtfPPV6-iYuQstx54UF36WSfR5kdyvwa3K261ojt2PYGbe8ItpEnaOoSu7Qk_HldmgU6NJ9PVFLSfPfWjbZ5gOafjAI9pRhdwM4VPxE4PL-l3cwZc1hVOSRV3LPM0zlRUkLGZHUft91gqPkpSDTHzHf3TyX3wQv-UQG-_Xf82Q3LIgsp_9obLzSMGv4LM7S5Ytbq5XPkifLOYX51Wcy4a4l08CjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت اولین امدادگری که وارد بیت رهبری شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/698292" target="_blank">📅 08:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698287">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dlKkRMqyh2nnCAXFQsvJF2BijyAHD08m08U7DypJHqqgAJUFlr9KEKsrQS__T0yyfD-ShVgIteoL4jRJioeOb9mLtK4iOWXPFqHlm_UhT0U9zTmzi2B5G5Et3t1B5X-zVU11C8UDFgAfbmKmL27uIcsOXo3FXT0H8DFpqezaCtOLomyWOct3Q_Km0GaCk_ENBbh-x9HgbvdKCvIQFyXZyujEv29HzsaE4f4b-m-gux6goyV0a6iUJ0J6-j75BT8d9A8tQWnn6DVqnCEFhNLR2MDc98sZ6JCYbXNHG9NEySrIftsTMS4SXf9472v-diJgPu6Y43pN1hko11FjQRoX3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eNH8iHwMI8CmiJDZrylRhzb5sDOxnnekHAVXJO7D3Q-Rj2GPCiRUkDh4E9edTBaoIy3ax-jJg1ZxXbgc9NSeKhWspN4mGOOg5IPnXnqlqdZcPHbzAarg2oB6hO1faStBVcVMkr2Q3CkE5ECzLECSmaQZdHzVCD9u5ZdwqRzC1Iw0wVxUO-1eoE0vSIHeCQpvpN36_sFbH9hH_0bE96C5albvcnpxv_vZ3qMoeo-Z8un0gN2rSMtUbzJ6r4KfOYpuNBwApe2C_IIGpxcFpvpmFpwcbwVlGPE9fgtj35e_7PMAoE_jMaK_5GebooGR_WCwtMzvNQowdP7DOSI3q7YheA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MNzgEYBnjtNwZIV6VSHavg6uf1ictT2xTpFTQE7Jr7I8WUvBtmbjervb5pFYxfx1wm-JsmZKXCn4fLz3poNE3Ivgd0Io-p4vnE7_kpuEvUJ8h705SZLxJizTZ-8ElnzlueNuEEfGCMwn6qRuuJk000Q1TerrU4LtBcSj78ifJrk_FljMgEMJohYLH-svSbgaLiUJ44J_oWdxSHu-yAPfuoA_N2jj7ukeVdCHnRLbo6c92QCQ1NOUGYgnCvFPAAAVbAPf4wv71XIVRiSq2iRGPVkZoFyrzNOuqS0KlqbD38a0PhWiTucXD668byqAIEFP-22F300Ns7eF527KrLMB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GJzX7vnDE2PPjZdM7oEufoey8_awYdptZjNYn7r2fqIRI9f62DyBJX3W3Lx1gvR3TaL-DwEekAWp3vw6pw14gt4DYfPbcHU9euSFWIrxsyaKXjXvms97c-ReoSNOstaHTKrfdrLzDWMH7LxMe1ZScDf2pB4skw3BxY343-cTFMu5ObgrF17vC3ZzW1ct-ssr9jwo3rY871sskiw0OQaJ2myPazZmLS1Q-mhwNbWmP20u50L6oexnKL3hQqxQBMTtDgUK_PD6iqJ0NCbD-OLCwozfDZTRcoRTz0Dt6w-79DN-gdcLxIN8gq462Z0v-nCeLx4Dte9M-zc2U67Dsb0k0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uk5wA-FHyXaUzioGzXVri48C-UCtDmIcwf3b6Zg8J0Zzg2VepY40-776jmdzvVNHWE7t-o3dJIjjHf3JrPfLZsdroxuZEO_BGjBiMcWvf64l3y_x4Mg8c4HXBn9dQUBrLQpRhfQti-eMhl7Xljk1f6_G1lO5nIfyEy0bHQU04rUhmo6VmUouhbWEKzQqh6wZsUmhrzdqUZDwc9uTZ3PzKZkV9xI0RtdjTZSwM8aoMlO2i79lKshvJpJ1BhR-NxIHGWyaYIJnbcEss4McJYZx1Kz4aH2DDxjMM1qG0BHyKjHZkwRYl_B8K0dM8mHYWgvmSqUFn0Elo4qWIRLq79i8_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ ایده خوشمزه برای اوتمیل گرم
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/698287" target="_blank">📅 08:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698285">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سی‌ان‌ان: ۸۳ میلیارد دلار هزینه دفاعی عربستان هم نتوانست امنیت این کشور را در برابر حملات یمن تضمین کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/698285" target="_blank">📅 08:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698284">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
اعدام تروریست مسلح در کرمان
🔹
حکم اعدام علی‌سینا مصطفوی، تروریست مسلح و عامل دشمن آمریکایی‌ـ‌صهیونیستی در جنگ تحمیلی اخیر که در چند عملیات تروریستی مسلحانه موجب مجروحیت شماری از شهروندان کرمانی شده بود، اجرا شد.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/698284" target="_blank">📅 08:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698283">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=KDRxZNHV3KpjPAES2EdV9peRym0krjd6XxpXOMOw7ffaOuc9u0FAjCcGooZAAO-msPvnDeeXfOvr2s-MHfWtUklm7N1ykco6P64k3hZ30oCk4T02yommsVLOiENYOFyp7qgXmivz8iY8ezPyfPPldf_c0LhrCWUFBcGw6ira5njK1ranSBx08GgRr0CosgcqDDtK7k5XFroXNPwhviv7QfZdT2vTTmlwRzX3bUvXXiFF71JCQmxpI9XwG5Tjk66WzlRh6M5Q9FQoiiqOwRXhtwGKPUTH3jwwXHMK8bXOSYZKed76ztbKBEYnn-9PrENsDcC_9LhQ9yzX044DsPQBRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=KDRxZNHV3KpjPAES2EdV9peRym0krjd6XxpXOMOw7ffaOuc9u0FAjCcGooZAAO-msPvnDeeXfOvr2s-MHfWtUklm7N1ykco6P64k3hZ30oCk4T02yommsVLOiENYOFyp7qgXmivz8iY8ezPyfPPldf_c0LhrCWUFBcGw6ira5njK1ranSBx08GgRr0CosgcqDDtK7k5XFroXNPwhviv7QfZdT2vTTmlwRzX3bUvXXiFF71JCQmxpI9XwG5Tjk66WzlRh6M5Q9FQoiiqOwRXhtwGKPUTH3jwwXHMK8bXOSYZKed76ztbKBEYnn-9PrENsDcC_9LhQ9yzX044DsPQBRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابوالفضل ظهره‌وند، نماینده مجلس: پیش‌بینی می‌کنم ظرف یک هفته تا ده روز آینده جنگ از سر گرفته شود
🔹
نتانیاهو بدون جنگ باید به زندان برود، برای همین چه با ترامپ و چه بدون ترامپ، جنگ را شروع میکند!
🔹
برای زدن زیرساخت‌های ایران ۳ روز برنامه ریختن، با این‌ کار نتانیاهو انتخابات را به تأخیر میندازد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/698283" target="_blank">📅 08:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698282">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
رویترز: قیمت قراردادهای آتی نفت برنت بیش از یک دلار افزایش یافت و به ۱۰۶.۷ دلار برای هر بشکه رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/698282" target="_blank">📅 08:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698281">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
بامداد امروز؛ وزارت انرژی عربستان از حمله به تاسیسات آرامکو خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/698281" target="_blank">📅 08:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698280">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
بازداشت مهندس سعودی در شرکت سازنده چت جی پی تی به اتهام جاسوسی
🔹
پلیس فدرال آمریکا یک مهندس ۳۵ ساله سعودی به نام «عبدالرحمن الفوزان» را به اتهام نصب دستگاه مخفی ضبط صدا در یکی از اتاق‌های جلسات محرمانه شرکت اوپن‌ای‌آی، سازنده چت‌جی‌پی‌تی، بازداشت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/698280" target="_blank">📅 08:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698279">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0851e2c3f.mp4?token=MheE0QfeF1vCi5XbQ9ZqCFb9vnDGSBe7lhi6B-kt17wTgA-swIjTca0yoZHzDgkEdLoo-WG3qgSMzu9aH3TdcrdN9aQxn531PV9w3AxBfeC7zO1q4gFOBLoAYQdFgKYBdsGlFu4h6d8S3o8lwCTyXU23qKeaoqAchMcfohW85yweXItapuLMa2UnoOfR97EJdhUc7owUWk_E4YF-KZwKd9a3VAFYZ6Rld88zUpPbO09n_Ra404_iZCT1uHbgbJ-kZxTOlLysKVGFGuQoja2H2ZHES7e4SsY6SZZkB9JxHxZnrMCf8NVT0bqumT3LtswE1OoULwWewuxqNLi5k4o4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0851e2c3f.mp4?token=MheE0QfeF1vCi5XbQ9ZqCFb9vnDGSBe7lhi6B-kt17wTgA-swIjTca0yoZHzDgkEdLoo-WG3qgSMzu9aH3TdcrdN9aQxn531PV9w3AxBfeC7zO1q4gFOBLoAYQdFgKYBdsGlFu4h6d8S3o8lwCTyXU23qKeaoqAchMcfohW85yweXItapuLMa2UnoOfR97EJdhUc7owUWk_E4YF-KZwKd9a3VAFYZ6Rld88zUpPbO09n_Ra404_iZCT1uHbgbJ-kZxTOlLysKVGFGuQoja2H2ZHES7e4SsY6SZZkB9JxHxZnrMCf8NVT0bqumT3LtswE1OoULwWewuxqNLi5k4o4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در میانه اعتراض‌های مخالفان؛ ترامپ باز هم مدعی پایان سریع جنگ علیه ایران شد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/698279" target="_blank">📅 08:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698278">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc1522c5fc.mp4?token=VxAZJLvytT1UQd9dvhm7HOZ46YaRWx8xb7RUmj-3xMF8KYodzubsIKkuWWIz1odnj62hKqPWH7LKnJ8oC0605IpYdaWGMqwYresKx53jnJTz9A4iYkeM0X2HtxY4BNse7miwhFApTlK7Q1MxhFYem-e8nrfe6mM-Sln0bYhFX_-VUZrb4DR5V2UQVz21bwBdutz7ei5Pm1qNlIHLTw43llM9q2leCzXzLFRQKAdQ1pPITbpYmNnBsWLt4K8qn5iVf7ptykv-O0Qngp4Ez33ioxYnULLDWNvypfn0PQN-J5I_hrepJ8GHqCygtuZ4nkHPIAsR5_Z4Vccpd0A6s5PoIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc1522c5fc.mp4?token=VxAZJLvytT1UQd9dvhm7HOZ46YaRWx8xb7RUmj-3xMF8KYodzubsIKkuWWIz1odnj62hKqPWH7LKnJ8oC0605IpYdaWGMqwYresKx53jnJTz9A4iYkeM0X2HtxY4BNse7miwhFApTlK7Q1MxhFYem-e8nrfe6mM-Sln0bYhFX_-VUZrb4DR5V2UQVz21bwBdutz7ei5Pm1qNlIHLTw43llM9q2leCzXzLFRQKAdQ1pPITbpYmNnBsWLt4K8qn5iVf7ptykv-O0Qngp4Ez33ioxYnULLDWNvypfn0PQN-J5I_hrepJ8GHqCygtuZ4nkHPIAsR5_Z4Vccpd0A6s5PoIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابوالفضل مهمدی اولین طلای ایران را ضرب کرد
🥇
🔹
ابوالفضل مهمدی در دیدار فینال با نتیجه ۲ بر ۱ مقابل حریف ارمنستانی خود به پیروزی رسید و با کسب عنوان قهرمانی، نخستین مدال طلای کاروان ایران را به ارمغان آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/698278" target="_blank">📅 08:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698277">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین - خشایارشا</div>
  <div class="tg-doc-extra">خشایارشا</div>
</div>
<a href="https://t.me/akhbarefori/698277" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
خشایارشا (تقابل سنگ و شمشیر؛ بازتعریفِ مفهوم قدرت)
⚔️
🏛️
🔹
در این قسمت، بزرگترین کلاس درس تاریخ
📚
را برای «مدیریت و سازماندهی منابع در مقیاس کلان»، «تفاوت بنیادینِ تصاحب با ساختن»
🏗️
و «سیستم‌سازی پایدار فراتر از عناوین فردی» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/698277" target="_blank">📅 08:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698276">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d471191d10.mp4?token=vcusHjIhmIDNJwiDJEUUd_mKHKd90Si1ZFxXEDcX8V1i7WA5XmJbqjMJcYrkunhtnG05QJiwUigpw9hxX9etBdgbeBzE4O2RU-c7Bk3M-0aJOgsiGJCX7-rYGBLyIBoi9mCLeVSfwSQUC_paSaXGaLzelG2ugAG6EtY8fuShqR2Q6JWXvCIvcFtmCToqEmvJF0S4DWUd6tgpxdsc59to_eF_TeW7EghXJRJOK6ms0F5F0LobW-XwtPCQokWiqyDqCazdgEj5CTCfGIV-hi1mOLCdQ-bqyD6d559N0QMAKcJjHq0nwv2_mvGtxr5tW8wKnG3-NvU_0eNHMOzWe1BS8oDoLkel-lLwACY0eC02G8FvKdY1i6iIUFLITn2I-Lsf9kbSZucyUW0oSZCzUo1ui3dT6c9UU5lta-eNFmNiI9rP1P033pzbHi4vIwTi0Kq33KyAuJoxIlahuExavlPVWP2Z3Q3Ft067qyixf2xI9HQX-_8OIMgNbFDLsYpFnK3iQHEg4IGJv_PGm2qw919hVSWAptn9Wl2hkVt56kC5PkejF5LuGIDOjhAnm_xEEfmsZcowfsDKVoMaSZqIl8mNvgTeNkCxlRGHz2Hnjf90VGgCE0HSzPd4gAfRanFbKdtJyJmJkblclwxFh1hJujMkpTcGGIFz7GWL0jwKa_9zIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d471191d10.mp4?token=vcusHjIhmIDNJwiDJEUUd_mKHKd90Si1ZFxXEDcX8V1i7WA5XmJbqjMJcYrkunhtnG05QJiwUigpw9hxX9etBdgbeBzE4O2RU-c7Bk3M-0aJOgsiGJCX7-rYGBLyIBoi9mCLeVSfwSQUC_paSaXGaLzelG2ugAG6EtY8fuShqR2Q6JWXvCIvcFtmCToqEmvJF0S4DWUd6tgpxdsc59to_eF_TeW7EghXJRJOK6ms0F5F0LobW-XwtPCQokWiqyDqCazdgEj5CTCfGIV-hi1mOLCdQ-bqyD6d559N0QMAKcJjHq0nwv2_mvGtxr5tW8wKnG3-NvU_0eNHMOzWe1BS8oDoLkel-lLwACY0eC02G8FvKdY1i6iIUFLITn2I-Lsf9kbSZucyUW0oSZCzUo1ui3dT6c9UU5lta-eNFmNiI9rP1P033pzbHi4vIwTi0Kq33KyAuJoxIlahuExavlPVWP2Z3Q3Ft067qyixf2xI9HQX-_8OIMgNbFDLsYpFnK3iQHEg4IGJv_PGm2qw919hVSWAptn9Wl2hkVt56kC5PkejF5LuGIDOjhAnm_xEEfmsZcowfsDKVoMaSZqIl8mNvgTeNkCxlRGHz2Hnjf90VGgCE0HSzPd4gAfRanFbKdtJyJmJkblclwxFh1hJujMkpTcGGIFz7GWL0jwKa_9zIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خشایارشا، علیه شمشیرِ تصاحب
🏛
⚔️
#پادکست_کافئین
☕️
🔹
شاهنشاهی که نشان داد قدرت واقعی در تعداد سربازها نیست، بلکه در به حرکت درآوردن منابع، پیوند دادن قاره‌ها و خلق شاهکارهای مهندسی است.
🌍
🏗
روایتی ناگفته از پل تاریخی داردانل، شکافتن دل کوه‌ها و رموزی از تخت‌جمشید که معنای جاودانگی تمدن را تغییر داد.
🏺
🔹
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
⏰
📜
از اینجا ببینید و بشنوید
👇
https://youtu.be/P6ySUoLgQ2c
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/698276" target="_blank">📅 08:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsvmHbm-X_UPWoWwfHbrjh42UDE1Psi4hXy3QESseuqWP8dlpe8teS2r742n-XTrL41LA-c1o6dzS8NAFobgyW0Vol_4y2VfjfGOXfJZkLs8-fQwpaCsVB2GywV9iglRrL1aSpDwwzs8e0P2KXX9dX4-ZJ8tDiWlrb5kSBR97P4fRb8QOZn8JM1AZObupfHNOG7NpdI_CZySR9AIXPG757ilwaTYEgUI_6yEmLPLtpWS7t_8I_d9BFGcjA1Is5EYolEWPXaWcSaFbUMeCYr4PSTBO00hm5fy2FVldB2wG3FCgknkCCeWxdPelYorvyBou_UrHnTU2TWgQGg6M16ffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۲ مهر ماه
۳ جمادی‌الاول ۱۴۴۸
۱۴ اکتبر ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/698275" target="_blank">📅 08:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698273">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfURSsCal9Uwb-VSUJpz1ELLba7nCJrYlakIwsZh-PRwH058f_oXsBSF7DU4kdIxBQNrkvGI7VNlWx-DxkPJ9Fx7-Nj-567XYctms9kz7hvUKrx-ntIcXObGLzx4-ebS24SOFMP1gu2HDKST3J1tb6IqgKvTNLtlniple61edayEw58uRRAviz6UtTmTLSF8QjmxBxr2atv88o10LrQBRVdOhVr80dYG_5rpZ5PaP84ay0J6qkB5FpPj790dcV3izd3KsvY42jxROnsRsQ0F-WIDPFcXfwN6VjbNGJ5AxGTRb9EcZ5M5npRgG05aKQt_XiDdfpkPd6lc133a7sh4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین بلاکچین عمومی ایران،خدمتی نوآورانه و کاربردی برای صرافی‌های دیجیتال و بانکهای ایرانی و راهی برای فریزر نشدن دارایی‌های دیجیتال!
ادامه مطلب؛
🌐
https://www.zoomit.ir/pr/467710-novachain-cross-border-value-transfer-infrastructure/
nowachain.com</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/698273" target="_blank">📅 00:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698272">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbYGF4-hEODAHC0Vm777SMuBFGP9k71r6zMS5RU641O6XWHdsSDzDkLL9DkMFzlBZpb8wxAjuv9ylF_2u3NMknrbLX3I3xUtnlNLKAePYOfj7ka7UkLhc-yVY9oN1SkoEvDJLIxOG3lZKTLf27A7x2db2bd_7xz64B4ONcXUB5VvoNQtUIjEQ_hxXF2Zlcz9-Djn2v90Dgn7Vs7hG_G3n4XCuH4tccQ2iSFCn1EE0uLi8u8A2FZcBSRID9gSuyn7X5ilGU2UyaqMBMKjtYCPSeRWIvuoLCBhXFR41aPVa-Zy80QkLL3v_w-apW0B9dzbM94qu8LJevrkhAyjCCsLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرفروش‌ترین کفش جردن در حراج به علت انبارگردانی
💯
رفقایی که توی کمپین حراج آخر فصل خریدن، 1.1 میلیون تومن سود کردن
❗️
پرداخت درب منزل شما
✅
موجودی محدوده، قبل از تموم شدن سایزت سفارشتو ثبت کن.
👇🏻
مشاهده و ثبت سفارش
👇🏻
مشکی
🖤
👇
https://memarket24.ir/product/fast/46467/180124/
سفید
🤍
👇
https://memarket24.ir/product/fast/46468/180124/</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/698272" target="_blank">📅 00:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698270">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a16c38eef.mp4?token=qCrCwZf1vgLGbh_j1T_tNX2FkvEEaDFkRFgxEcxPNaPuNcqwGXGyAqtcxIvg2DxeCLpEnHyg63yWPtpY2gk1awdfRgOUyFZesXUwGc83-SC8n_uR-xTgROn0uXzzls3FJvQI3mLKfmI78OEhL99qfGMl_5kxCn3r2LPdsDUIMB9_YZut3b00YC-vLTv5OlYEGUNxYmZ6lOhW7bzSxJU1LmpFvQD-x3S3rXbNHFIFXm_joyuTcydDei75boIN2Jl0UC8M7iOVGLO0CN5BX8dB0G6vO07GTxQ8eSyRsTQc2xAeUqb6a3XgMUokzzCsVHSTESIfztKUySfBuuwfTjtzxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a16c38eef.mp4?token=qCrCwZf1vgLGbh_j1T_tNX2FkvEEaDFkRFgxEcxPNaPuNcqwGXGyAqtcxIvg2DxeCLpEnHyg63yWPtpY2gk1awdfRgOUyFZesXUwGc83-SC8n_uR-xTgROn0uXzzls3FJvQI3mLKfmI78OEhL99qfGMl_5kxCn3r2LPdsDUIMB9_YZut3b00YC-vLTv5OlYEGUNxYmZ6lOhW7bzSxJU1LmpFvQD-x3S3rXbNHFIFXm_joyuTcydDei75boIN2Jl0UC8M7iOVGLO0CN5BX8dB0G6vO07GTxQ8eSyRsTQc2xAeUqb6a3XgMUokzzCsVHSTESIfztKUySfBuuwfTjtzxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین چیزهایی که از ایران صادر می‌شود، چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/698270" target="_blank">📅 00:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698269">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ارتش سعودی از حمله پهپادی نیروهای مسلح یمن به ریاض خبر داد
🔹
همزمان منابع غیر رسمی از شلیک موشک‌های بالستیک یمنی به سمت اهدافی در عربستان خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/698269" target="_blank">📅 00:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698268">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل به نقل از یک مقام اسرائیلی: نتانیاهو هفته گذشته با ترامپ صحبت کرد و پیشنهاد عملیات گسترده علیه ایران قبل از انتخابات را داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/698268" target="_blank">📅 00:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5fl2izKeGY2uY664xbTioZlNyeqvrevax0LOsF0FoPh8H6_VaGHm7UDjC7Tn0UXaha5ZyaAZJ87seGm1Y-rojR2MyyXV-hW3qp3coJ2iFtF-0ddIYYB4CLhE5NCbj9avlRXfFuble9Q0VeBfc79zuWTEfw-30QrkWt2dM-tSYnJG1ic92x-Lx7vASgC8TXCD-KF5S1iMe5ebnRHiG4Q3BoYZajQTbIknJwbRt383iUWXjq7GWAY1jh4XXyIBpl8_BfR-qkYQO93UlnfEqeIFtvkCTdYpdGK9TnC3ZHl25bl9Q8ChTTy-ZS-lwn_gjPsmDm4ECT9SDpbYr8-aLFTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/698266" target="_blank">📅 00:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698265">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuSTxt0JsGYrtLYPc50g5yDAuzDcyZh6CyEC7J57nzXNkBdM7XTG-ADPPMzAaPCYg7_yVuX9D9fPZUx4UgTx22RAPSRvXTMrMvXwrH3CiuqFBPLGwzTLNLL5JSNPRtlKKROgXBIyb5hiLTUF9wXbd7UO8oNrIXHYMjvois7JyMAuJfh6RPKGva1X4ND-o-TmXk1L8zkEZAgE9oIMJZLrsu5dXZQJXeIZ1MhcthVJ5rLcFJOlqjRch2oQveHExBd5Q63qJ7Im7x-aRGyUmVM-QcIFFhBoU83d3h_Z1Stq0JbtNx1_9WA-UFADTKeHjeYwC7KqW39VQ_9lpi8w8tQTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/698265" target="_blank">📅 23:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698264">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
کودکی از غزه که دل‌ها را به یاد علمدار کربلا انداخت...
🔹
گزارش اختصاصی شبکه سه از وضعیت نابسامان کمبود آب و غذا در غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/698264" target="_blank">📅 23:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698263">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3b948062.mp4?token=BgisIfO5ObTIikdXLQ0cGOV-kzlvQ42ungQnijgALdNNcc3mtdNwkyz6mtlxmL2WyH7IX2bfMRhsanRWM9X4IQuy3aeiOimm-aSecsOOqUjoiA0FHAu6FgAAWW15qyTv2w5M691pNCSF2ACZF_Adgd0H8snsTH1RbfQMU9OlJCf3BWJtFuigwTIma5MtKzX0VSVwey2lN15mVn5PS_Ts0U-UD-rC4YECnppKMR7etZc8sleqL-dJnqeD5wWeJO3AMT_jwQOgqvmYPEkN2_8PthK75Y5j2SoZ10-waihjloHvp60zOROP6_1n_LE_jxA7IKvF_QP3LL6azTfVgmRMCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3b948062.mp4?token=BgisIfO5ObTIikdXLQ0cGOV-kzlvQ42ungQnijgALdNNcc3mtdNwkyz6mtlxmL2WyH7IX2bfMRhsanRWM9X4IQuy3aeiOimm-aSecsOOqUjoiA0FHAu6FgAAWW15qyTv2w5M691pNCSF2ACZF_Adgd0H8snsTH1RbfQMU9OlJCf3BWJtFuigwTIma5MtKzX0VSVwey2lN15mVn5PS_Ts0U-UD-rC4YECnppKMR7etZc8sleqL-dJnqeD5wWeJO3AMT_jwQOgqvmYPEkN2_8PthK75Y5j2SoZ10-waihjloHvp60zOROP6_1n_LE_jxA7IKvF_QP3LL6azTfVgmRMCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای یکی از سردترین شهرهای جهان در نوریلسک شمالیگ؛ روسیه
🔹
این شهر در شمال سیبری در روسیه و بالای مدار قطب شمال است که به عنوان یکی از سردترین شهرهای جهان شناخته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/698263" target="_blank">📅 23:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698262">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zoi2mONLWz6zpVO-khcAhaJXwV3SyfA3vpTujGybMjLwW80Ux9f1h_Em4KyW_g0SybuPkeuInihdP_8Mx5F2DYxnqkSDzuCu2E8RneLywJAdNRmH_PveQEOQZDzX-cI6XPDmfw2MqtGxcK6d__9jd2-_2vvxdfdJo1m0IFRqIscPCyFbEeLmXK_0IcBuYlzVCAt83EoYCShEqHD0iG-gZlDhuQAg_q_DNjdBZBEBkIhvsvIFMWCu63fqZK2BuHiOYByHrxVp5mwlS0AIRdinVLE_8_G15AQvIb0cym4fNCRBMeaBxP6Cfk5BDx3kKBtuNln7inMeZX9iTvTXNvm53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از جاده چابهار
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/698262" target="_blank">📅 23:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698261">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را ا دست ندهید
🔹
🔹
فوری؛ نتانیاهو می خواهد در این زمان به ایران حمله کند
👇
khabarfoori.com/fa/tiny/news-3252237
🔹
حمله یمن به آرامکو/ ریاض هم هدف قرار گرفت
👇
khabarfoori.com/fa/tiny/news-3252235
🔹
پاسخ ناقص واشنگتن به شروط تهران | چرا توافق موقت هم دشوار شده است؟
👇
khabarfoori.com/fa/tiny/news-3252073
🔹
دختر ایرانی ملکه زیبایی خاورمیانه شد | حدیث ستاری یک دندانپزشک بود
👇
khabarfoori.com/fa/tiny/news-3252130
🔹
خاتمی عصا به دست شد
👇
khabarfoori.com/fa/tiny/news-3252013
🔹
خبرهای جذاب را در خبرفوری کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/698261" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698260">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ25dnoeOcAyMeYGTLDU8ygCa4VB2-uOErl3nK4BsP7fCS-dlaVB5QzcTlJBvNuogt2uO18W2BLCzTDVPcbR92h2PCjK8L138giKI9SEOBqzSpS4CCd9N92QLdE3vay0dVlKs5yWtmebFRXNHtNBAaUwwJnRWisKzEmgLOtgHlMNllm_3XXaTN271degXP6we0rDBPbuf9sZfo0fRxQbrhY6OglXt2_1KOWzmN0NqNZ49sPV2lAzrrDN_Y1Se7WaqQQ5pt45FJi9KHHKtgKRi7_QQWMZX0_f-ZPsUHw4VnQIcWaoopUp6HGCcJQxxiBMFL8eWTF1ADsNR0oHTfYsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تمثال قمر بنی‌هاشم، حضرت ابوالفضل العباس (ع)
اثری فاخر و حماسی، با الهام از رشادت، وفاداری و علمداری حضرت ابوالفضل العباس (ع).
ترکیب اسب سپید، پرچم سبز و طراحی پرجزئیات این اثر، آن را به انتخابی خاص برای دکور مذهبی و هدیه‌ای ارزشمند و ماندگار تبدیل کرده است.
✨
مشخصات محصول:
▫️
ابعاد:
۳۱ × ۲۵ × ۱۴ سانتی‌متر
▫️
وزن:
۱۳۰۰ گرم
▫️
متریال:
پلی‌استر
▫️
طرح:
تمثال قمر بنی‌هاشم حضرت ابوالفضل العباس (ع)
▫️
کاربرد:
تندیس دکوراتیو فاخر، هدیه مذهبی خاص و یادگاری ماندگار
💰
قیمت: ۱۵ میلیون و ۹۷۰ هزار تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/698260" target="_blank">📅 23:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698259">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c7c193b7.mp4?token=epq__jFFViO4srHUHSW5RqBD6YZ6oX9FMZbSZREOhmIP_Py5MFBPJowrox8SLGm1fTeZEqVKAJSU0ev6gtsT9IemtlR_7Se9roJN2XZBUe_fsWmuv2Mv_iVMHU42h1L9qyLPlMnidV6wrfqd4d30L8naV6IqIygSHJqLTmWm8v8BxiaUCam2UK1psVjKyAUmHN9UtGV2kWcmiUAgiJuonczJb-HXAcNgr1tl1jZxq3r1ZLXfS5xUq-bHASWjIYk72mrZcu6PT5BOq_j23FvB2L_6ZS9wFUwIb-1s1nlcvZScGy-bUZETZ-p9PsbnX0HSUw1OLMc-NM65NVgNCAbShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c7c193b7.mp4?token=epq__jFFViO4srHUHSW5RqBD6YZ6oX9FMZbSZREOhmIP_Py5MFBPJowrox8SLGm1fTeZEqVKAJSU0ev6gtsT9IemtlR_7Se9roJN2XZBUe_fsWmuv2Mv_iVMHU42h1L9qyLPlMnidV6wrfqd4d30L8naV6IqIygSHJqLTmWm8v8BxiaUCam2UK1psVjKyAUmHN9UtGV2kWcmiUAgiJuonczJb-HXAcNgr1tl1jZxq3r1ZLXfS5xUq-bHASWjIYk72mrZcu6PT5BOq_j23FvB2L_6ZS9wFUwIb-1s1nlcvZScGy-bUZETZ-p9PsbnX0HSUw1OLMc-NM65NVgNCAbShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر این ۴ ویژگی رو در خودتون پرورش بدین؛ موفق میشین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/698259" target="_blank">📅 23:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698258">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
قیمت گاز در اروپا به بالاترین حد ۴ سال اخیر رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/698258" target="_blank">📅 23:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698252">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDeWja0DbmYE29h4m7dUOX31aj7yBSHLAEjTSZNtBiRXXc2QcyTeNBsnnkYIgqRsi-tPrDN46RCnwr3GB1rATPvZZt4z0RakMOVNNN3GtVEVNTRqub7WzcWznJI1_9aRFACoCX8lqyN5AvmO7JTA7bBkqUgNsY8VCH8RJMcbFifP7ZZ64fuJyXJFybqSRbo4mG4wHTzREk4WkEH2edhJOkmB6upPPASTt_Ft1uUgTFdp5pMOI4jKut7irtt_Ag35WRjrX0qlkGZeVZojJPE9epu2QHGvNqDvjGKTd3rui1jSr_5AwEgcklML0J0JaZEmp2jGZyfkV6bzrtDcbxs6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله زمینی به کشورهای همسایه | برگ تازه ایران در برابر حمله احتمالی آمریکا؟ | پیام محرمانه تهران به کشورهای منطقه
🔹
گزارش تازه وال‌استریت ژورنال از تقویت استحکامات هسته‌ای و مرزی ایران، بازسازی توان موشکی و پهپادی و آماده‌سازی برای احتمال ازسرگیری جنگ حکایت دارد.
ادعای وال استریت ژورنال چقدر شدنی است؟ بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3252180</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/698252" target="_blank">📅 23:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698251">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رویترز به نقل از منابع محلی: صدای انفجار شدیدی در نزدیکی تأسیسات و مقر اصلی غول نفتی «آرامکو» در شرق عربستان شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/698251" target="_blank">📅 23:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698241">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTKumu1BLRECPFK9PgVYh4gipcPd6SZyaAUXeJ0ZuVYE9WKxGaD2NyfDjbvJLNsd0mB2FjlsM1W0bUyPwU_XHhhAVL65RiB8azKwNEJtF8sZ2jiGeUOc7bhceCE2qv2oheTYtmq4HaYYBDKCp6XefWZtMw24AbgAzl9fWLaLRug4Bo_z-ZoLLeoy_WWaBdZxpsNQxkZgyMvyvOKFpqww8Mrp-WEY_7sQsukbfajTncG8EG6INX72GNScWHYL14uikqkaIVmt0g3a-tm_42cCbY3D6bNiAQ8qy_u8EDOv00mKUpZasCyK0jWJ6CwSrwW-Tbrt-DBX99JdgXgINrLEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faK_skCi4eVNCqGgNlRAWnPOf32koUVTnUO-v9oiivqmI0-P1YDOwbM2fGnCM9X4H4CXZBx33rJkmGFHuixHhB6i3QFNMUqegss0ljrAGpMF1qxAowwIExxyZQhOzlJq7TKHQolV9vnWAzFCmbyBPMLEo8la0EjhwmyFyNLXRDTsqQmvxUr7dpaVzpEzs_e7ZAHxFWA9-Y5IikXkwleFhzvY8ILENWrGF6CYc21vw5awfC-PE5j58eAVtr6uBg-q35fuz2jx1IPdfzLwb2AkWLuEQl8-Fks0uy3pqlbOynwIMTfuRPXQBXBMZk9RdiTkZBr-l-K-C-st9L2xJBHDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqW8LFXCn_4PL75pT8PiaAsRFtyexwb_qOmM6m7rrZab1KQnlCzqjiDN4pTwUAuIRcvFOAiAzW6Gu9tkV8N4X4G5T9GOVyE2Jt3E_s2gKVNBiMHwOZKaCn0-Q1Ui96e0VTgplrvvNlyfmoe2rNkNXp29jWcjac6lPABnv16TnPQGlQK6V72iLUbuYL9NT0k73dOlBrQesgX_qAtfcyQQK5zRCmatBqYpCjwrgRjNt21WQCIZ88-yQKDFj8OGfdHK9PUX-5-zNS3qpu-L6uJlw18tFsUpAk1PVbeYYX6-rQmTyYbtPhCi3_mQitjTGy9QL6dK--uQx97Pl0K38AdS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7bFKR4-iu6pZN6ug487ePmAvVXD8PS50HLaGHnaBJ8CkpSUkhCcia4xEj0uGxYTpAcBrwwvWmi-LlqxUvKDtWLltwWVV0Uca7x5HVUDQBTf4F4aoJ55TnzD2bvEzZWkDuV_qTlQXhE21CTf1EiL9ZFqwG0EZxShRuRKegV2f9Y8IiG8cnU86mNbRljmLT7JmiSEjlSemZLAgwyAZuIF8qrT1RfrvrhWc87g8276yChoWGkqUMCq3Bk9BYxJkdKWEUOJfdoJzKY3MZ2kb9w9p0SYkQKU3nYXZ-NhMCAgZIKrMxTAqIog9epZi1RBUf7VTg87JiPwNl8u5v8mY05lmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYFHsZciOJJND_hU6IIHJb_eCgMH9WqxARIL7YI_3MQqGonMlWMTfb0G9A6f9z29_eqjw55_WAhsHc3USwJAD7AXH700eS5qsB8arUWXz0AVwGJplTAYOfCRCRfOlH9qIM3JuNnLOO_51NMv9RoaIq8ZAcgGVv1rXKdyMOCh4SgF2mbQRPP6g0gNPN2HRxW5NonGyPjtvhTxyzBlLG4Yle89XlNwjl-0Zi7JXpHiDv4nPfuh59bZs6Rt2e7hxOQ0mr451cEuWJ0QD7OnEAe0dXqS_lxXB8gdJ7XenTTWCSZyvuLdtR5VYqzUHEmM8yb70Uzy_flqy9lrigRcEaeZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F43CCmMFIXw2OzM4NFR8YGjTDLZVSLc3itJ2MjYcGD9U_nsG1dUdz8rnCEsmRnQ8SrtWlPNEAfLxRzaF73fwJx4PvJgxAO6vt0DP_ywch9rmQ1EnnKmn7hFduC64xYAW-u-Zv5vVUMWOPuDsz2DdalOQ6oWlcc9A2awapdwrwmhEBOSA_ZS0yqxUSU9jH8d_iqLbZRO2lFfz6dOhknL9EfW20Pg3UWZ9oPsEkDiFs5OASkR9q4VSRpC1vjW17Ekz6EWh5IpaV7njA_0AUIWNCm8X-b3k6AR21OMdHL6k6Wi3fHAotc8DZKz4oPZeXzVSmrHhP_HTHx52xdFKiFF8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iploKfqj_B8RACrz57DgMcMq9dom71EXtPLl9jMII3TKbB73vQ_pvFKHHhg6Fgb0hlpE_jsmI6k2Q76RyWiXd_JGkyyrT5Et37A31ZW8r71rfisF7MQb-Ern3KC__M6U0nNzYgbgDLqutrtJdHh0DG_mjqHwxosLiC8wvpAV8AUrU2M7aCSu7ojA69W_gN91BAFUHZo2Lg-ygqtQBi6ZEeLm9NYPuiChqYmJwk7dqlt_gDRF10EzgeH1eHnOib5boFY0loPDWCFJ2VvtOBDfEyhbaxMGFYp8f24tOceE4Q3DORWGq88L1xN1Uketg2kaZqZrhB0KohcaTiGzACe_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZJmg3pCwVufOcic_b0RyTtLPe8yRtXZrXQs-TSbjVc533BHWTO6BNXZJyAErIrXAJBdq_kq4rwmjpm-PffQa0e6ehOdWWGrInJspPkgvXGMxkEAQPhMOMelC6qAOPGjfeL3A3HGNJZXVeujWUQUuOH9oaUhKQyTLKwhdV8XhPExy2f8OucrHaTI0izoRuaSYDUHwPNUWLKmq1EBfPnZfghHFtsiUqwdmr_snyxWbbDM341_0g3NT9N_R9zYvn5NLEGrKtJeCX5Awy0nHgu9YO7WvY7xTQB0D75QPR2XGpDXXGHHoWrqmlWb7ZOq5ciLpGB65LUQGGpqYrr-vs1rPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoujXCegmTqRr0svGTszvsNGVu4etzWm4XfzVUjFFOwq_dzpjB7N_LJs624xD16EVZUpKbkeyjhuaiC9_6mu-KSaJgS865GEzGTd72w4C0u_JrkyuJdr-DY47ik7AvKDB_CQqVOvJewF1D3At762l-VyyqGGBw-AeK5VOtHLtANkmkyCI63Ug0m9hpK1y73xxqz5c-1Y9v7pUO0qGMPXg4q5cSYv1Jl53AklijUrMi3dlI7PAFwP4vW06m9JuL1848g5kTr6ZB6-ckFA8rMvLMIOce0p3o4L_U1-5lHFDDPOsFu8M4eSmqDGiG1VwaJIhwQR4QWMgkmOPgPSYZmqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7HM4j9OJJ0MapvRhlgdqfvf0P1RRKlrMfH0M5eMUIqIsvSZQTHA8ARBjzR2EdOm54gmUsRFfUIPnHl5X5QpZA_FhhwOeugAYZc4UsNPdk2Z9GLPVWE_zzkKkjBgjCUrQyZEOnPLIEX_SbVDdAaXc4PXRs5k4GUZckQTT08VLIAfHLQMs6NL-4JOcFA5tA69mwyhz2mujYA5M2L7xrs342Vj_c8YDjmoHS8rbUnqIal-DFuhWEj9Amy667HC2N3san9P6q5z4zPdWoNtlKk4jcBLzE8RwFgAiBN7hp1Wy8loeiy_yCk2tzvRDFafAEgrQZ9rtNEpQghG7gze_xQkBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صف وام
🔹
طولانی شدن فرآیند  در واریز وام‌های ازدواج و فرزند آوری ، به چالشی بزرگ برای شهروندان تبدیل شده است.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#صف_وام
@Alo_fori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/698241" target="_blank">📅 23:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698240">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
نتانیاهو جنایکار: نگران انتخابات هستم؛ ایران به دنبال شکست من در انتخابات است
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/698240" target="_blank">📅 23:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60a55b261.mp4?token=QVDWYJkPRLniKgUZfidoSU1_bVtkYjbqIQFyFesIoVbzEo1CFcwjfMNurIFQIpdENr7F6B8XwEa0P65C41BrcWlk_NNCXoM6PfNqMOylgxvLoypQfsipSO9-wp3OYPSEegfa_BzLnb9O3qvd70G4z5w7-PDg-AfbX9BegrKKSgJ1nEpFP1lYlLDzy43sa5WLlSuuhi_M265ET5Ncw_C9XDODArVzQx4AX8MbiWPWdIBkLg3xmTGZRKBbEOTFfQBBGH4Q6MnyR0gCPqp7c8k7KqcuK7gjYBvubnPvQ6tf6MXlct2QOlC3nYlNTm6xocm9Fww5fHC4ynaSlnQRuwk87kWpgyXygboGIMsJt7zj4zW7AKHAe2ehtlM_pH-hOMdJm1aH4Ut-k90kjZx91rWlKFFwGO2Lev4B20fKjzAg1z6jJcGjS17J01E68ucdP1MoSvLTVIcTgiYcvac1chjzpvnFze-lbC8qG2RSKSRJKbD2_AR-hCVkrJXpW8Vwxzsu_-3Rrjs_JqAQBBFKq_h_RPcfnzSFmYYfB-ZeHEVK9cusj2n4FjHd4VhvU09iJm4ORktk8zgk24raS-L6Tqn4wcMNxLnluXQMfDN8FEL6HUJFcCIVrM_H2Sg7F6vsOGAsZAqWvEJzOnWjeh49DyTIaF5FDXJzRJLckFYuhZkUFpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60a55b261.mp4?token=QVDWYJkPRLniKgUZfidoSU1_bVtkYjbqIQFyFesIoVbzEo1CFcwjfMNurIFQIpdENr7F6B8XwEa0P65C41BrcWlk_NNCXoM6PfNqMOylgxvLoypQfsipSO9-wp3OYPSEegfa_BzLnb9O3qvd70G4z5w7-PDg-AfbX9BegrKKSgJ1nEpFP1lYlLDzy43sa5WLlSuuhi_M265ET5Ncw_C9XDODArVzQx4AX8MbiWPWdIBkLg3xmTGZRKBbEOTFfQBBGH4Q6MnyR0gCPqp7c8k7KqcuK7gjYBvubnPvQ6tf6MXlct2QOlC3nYlNTm6xocm9Fww5fHC4ynaSlnQRuwk87kWpgyXygboGIMsJt7zj4zW7AKHAe2ehtlM_pH-hOMdJm1aH4Ut-k90kjZx91rWlKFFwGO2Lev4B20fKjzAg1z6jJcGjS17J01E68ucdP1MoSvLTVIcTgiYcvac1chjzpvnFze-lbC8qG2RSKSRJKbD2_AR-hCVkrJXpW8Vwxzsu_-3Rrjs_JqAQBBFKq_h_RPcfnzSFmYYfB-ZeHEVK9cusj2n4FjHd4VhvU09iJm4ORktk8zgk24raS-L6Tqn4wcMNxLnluXQMfDN8FEL6HUJFcCIVrM_H2Sg7F6vsOGAsZAqWvEJzOnWjeh49DyTIaF5FDXJzRJLckFYuhZkUFpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابزارهای کاربردی و جالب گروه‌های امدادی برای نجات جان انسان‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/698239" target="_blank">📅 23:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698233">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjhnvlZNho4h3YgKrdoND-DHCYuKKTaKif6OKR9pLnPepiu-vjGrZ1MMZfpZ_7hG1Sk4KhAoXZhMVpRtcbDcx4Y4qLO9P_JO840XpkO9NyKl2WfvR_6zpRtDKh2Ew9syYFuS0j5sMWnARSqP1sFhTO2wcMAn2dkKmrBIBNMOWO48EJR9Grabjd8zWx_povSpzfmu7t0h1Imgl-ERlS80dhFwxMqJhoxwtTJBDgWBhSnVEbyjz0rOLcEVF9r2WrKoJslQlHdIf21kuwUpikWXA5Q9MG35XICV46-J0n91RsP3nsgZspkmKW78C1ei0P1yJM4NO10A_AUIVZzaHBbWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4Z5sK-3U1VbNkwt73r64Wq27o6J37zAfRyj4tENiafqHFUPt4HjgSzT1xPVG_IKI4Wx4uX5xmDa68KcDCCgRXUEYfUNDacRbxliDjKu88sGVkoRbf0ZZhty5G-KgMHTt87LhFKK1yGMJNDb71LIzXi1iIDcDO3yoziGDDpXz4D6mxg7vLl6FnvrIHrAJNBf-ukSWOTelkvwqSVicsYxtTLzu5357nWrA9YljhfV9G8qNmvXo4JBShQ7-y0_et44puvLZ4C6BomKJqOWEhDcgYemw3hmhVqZRSoRlDMW2f1yf1kmQQCTYLKHhPzcx_G6aMsft6GM2D75kD3UOz_vIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qhf8o7so5yIN9hpyE5hOva-94JDREoOhAt7sPUoiBPmgQj-bQies6ELg-7sHA4wuF_AgGctV9py33IqDKCPbfMdktPTQ6Eq-6jAeIVUX2IYghvwov7xa3HzavnOvJbwZu_TlRc7AhR01-SRJUacuhzoDpxRcBc3dx1J8GF4MIO_u3E4KG9vKIwjkQIiYGqwaIT8f1DY_nqiarjub-QNf3ymYHae4ZwtCqanGUl1i29lNA3DhlNjdVnZzCGKy4rJbMMd-IWFiJjLukhf86pSUd1z4B4DciWw1whzuhZwI_Qx7F_SlNf2VdZ2gQR2HBZkS59P_AW4OrkoCvGD9vo1yUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kt_pJDk7MdjoFYX12KSIcOEEnEawGg5DcTt0JNQbe0jdMfR5h4j_rORqb6YycWh2WPt9-nIo6GFHtOQ4yV0l_kiIGIaC-l-d-ovlwZuzfLHzff-YRYmylliGTLtZYwnKiFsrhzNHNWA3FIEb39UebdSATD-hW6ewtt4pKzYgC_26fiFFfFGQI45pFeFW2iOMZt4oUL5GZSJI5roqGDcDQ6IL7nqORhZ-c9Q9rRzJHHZ_DtyfhuBPs2svzU-GPmdCtzOhx1M7oUzxKDeSa4sp1KFNunXMDaU1xKjTJwr7AtiUA1az6OKZqr65FrCNF3SOpQ8bZh5eTT3vWGZIeS2h-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBIAjNgv-gbnnFRhYBSNevmhe64q9huSnUaBo-hPyBeShiYDQfLAS0mnUjhuNDFzAa03dXqdbJJCkvlanN2bGXb4w5M7bclVPcKs5IaznYpy_Uu2U0M8sV3WVelDK0M6Xky_bDSgVe__j-XeojIoQFXIILCyT_j6ndV52crQFMfxtzP7Sm0JXqwTJDnAsGJ9KCKSNcRRDRwJzP8rDHLNyqJQbRz4cK5Rel9Tm0Sdxdjf-FDrHu-gbosdAvcHuEMmq6bW8kSgXFcLR2fRMfHw0yNoBHC_zNDlal8vxJhkCsawA9Ek-86rg4yYRM08bHJsokghSfAnl1QkRb-iIt0ZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csBoM2cHdyjKwkaPhv9NAyHw9Zp8Erd9DR58E1YPjHudSbHS3PGGph4Z1dh0hocykrab8cCKhDGr2QBk4RmTPjrRiwPTBXTuIh6W70dCCSYSw_cKIKyJJHM1n0JsZqjYvUlas48jeryaGVTvSEb0MxrF4JH1qxT3xVG6Ysebij02IQJx1EVikpj0Wtyr-queris4R0kkHmo0C6oE-Ogpyni-b2aG7F7aoBrk7zi2J3bscP6CrUeUQ3FrY293VV1unqRBGGXRewGiOJvwgY762MyzB-WSMhCurnCaBxVWy_YPZhMYfRBBJuKunUvsylX7zj4J-Dh8J7eN8fPTzXULaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با پول تیبا ۲ و سمند سورن، چه خودروهای لوکس خارجی می‌توان خرید؟
🔹
با پول یک تیبا یا سمند در ایران، می‌توان پشت فرمان کدام خودروهای لوکس خارجی نشست؟ مقایسه‌ای عجیب از قیمت خودرو در دو بازار!
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/698233" target="_blank">📅 23:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698232">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 14- میدان چهاردهم، تجرید</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/698232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح کتاب صد میدان خواجه عبدالله انصاری
🔹
میدان چهاردهم، تجرید
🔹
تجرید به معنای برهنه شدن از نفس و وابستگی‌ها و بندهاست
🔹
تجرید در سه چیز است: تن، دل، سر
🔹
زندگی را معناگرایانه ببینید و از شکست و پیروزی‌های زندگی درس بگیرید و رشد کنید
🔹
این دنیا کلاس درس است و بایستی تسلیم‌وار درس شکست و اتفاقات ناگوار و پیروزی‌های زندگی را بگیریم
🔹
چشم امیدتان را به غیر از خدا و هیچکس نباشد
🔹
هرگاه در هر موقعیتی گفتید که من بهترینم همان جا سقف رشد شما خواهد بود
🔹
به آن چیزی که ندارید دل نبندید و هر چیزی را که داری راقدر بدانید و شکر کامل کنید و در ترک کردن دارایی‌هایتان نترسید که رشد شما در همین جاست همچون تفکر، اموال و...
🔹
در مسیر الهی اگر به جایگاهی رسیدید که فکر کردید حق هستید در تعصب خودتان هستید و هیچ انتقادی را قبول نخواهید کرد و این نقطه سکون شماست
🔹
در کمک کردن به دیگران و در مسیرهای معنوی، رد پای خودتان را پاک کنید و از ریا دوری کنید(حذف منیت در درون)
🔹
سیر سلوک از حق به حق است یعنی وجودمان روح الهیست و به سوی روح قدم بر میداریم
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/698232" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698228">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02f6abdd7.mp4?token=BHAxAMKDIqBsEyuB3CEDggrowJyxYYFEoj3K9fQtzqTlLsQ_WzLW5nT-Hgk_KSM0HEGgyyPdkNd7REOjKuT8Fum0C3e22VJZJg45AQz-f-nhKMDb2-p0JniJU-eXfzQCn3gXAq85lGaW-TAhpKyJBu09jvwndD5EsAlWsGDW5Pb25ACIHEnHUnKnazE2Fdy1j9uxosODfOetafSY2jIN2y4C_9Lsn9lKAerxb0FuXpn-cERScvMtRkVTp5KCleppYuAOtytzCwElQGT4WUHmMf0Ckq9MG3O6fcIr9fk2VX1N2z-msfwVqfawVYdY_8N08mvd-y4mUO4ZT1F1yhZAuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02f6abdd7.mp4?token=BHAxAMKDIqBsEyuB3CEDggrowJyxYYFEoj3K9fQtzqTlLsQ_WzLW5nT-Hgk_KSM0HEGgyyPdkNd7REOjKuT8Fum0C3e22VJZJg45AQz-f-nhKMDb2-p0JniJU-eXfzQCn3gXAq85lGaW-TAhpKyJBu09jvwndD5EsAlWsGDW5Pb25ACIHEnHUnKnazE2Fdy1j9uxosODfOetafSY2jIN2y4C_9Lsn9lKAerxb0FuXpn-cERScvMtRkVTp5KCleppYuAOtytzCwElQGT4WUHmMf0Ckq9MG3O6fcIr9fk2VX1N2z-msfwVqfawVYdY_8N08mvd-y4mUO4ZT1F1yhZAuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله موشکی بالستیک یمن به ریاض که بیش از یک ساعت است که ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/698228" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698218">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9902025f50.mp4?token=GyXkQ2XTVE7-R-JYizCsh4J_5gz2kMmtY9hAXus6IvgFO19aQmaBq5NmHVaoM0f4nE7tDa8geijBNTw00KFY_86tnh018wmZ-zBl3xFgnLR2O8JjT3p04orMtrEC5kIUhm2G5BwYPlxwxxNKR9h5K-LichXXKctiGIQhGUWH6ESVp4Ao3PxPQkxor623XswikQwIgPGeUW4pISjCFpfoCUMdNEEUixI4UtPcEU7rZP8KAzbOOcr6NMQVDMcv4_9IrYRXwG2IeRfYWChYKMxFmzMFHbyLuXMyy1YesRTkxgtCiGbM1ciMo14uTpwhUcCxtiWcIxIiZj6jBH6FPnrJOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9902025f50.mp4?token=GyXkQ2XTVE7-R-JYizCsh4J_5gz2kMmtY9hAXus6IvgFO19aQmaBq5NmHVaoM0f4nE7tDa8geijBNTw00KFY_86tnh018wmZ-zBl3xFgnLR2O8JjT3p04orMtrEC5kIUhm2G5BwYPlxwxxNKR9h5K-LichXXKctiGIQhGUWH6ESVp4Ao3PxPQkxor623XswikQwIgPGeUW4pISjCFpfoCUMdNEEUixI4UtPcEU7rZP8KAzbOOcr6NMQVDMcv4_9IrYRXwG2IeRfYWChYKMxFmzMFHbyLuXMyy1YesRTkxgtCiGbM1ciMo14uTpwhUcCxtiWcIxIiZj6jBH6FPnrJOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا فرانسه هست؛ ۱۰ تصویر از پاریس که رسانه‌ها نشان نمی‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/698218" target="_blank">📅 23:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698217">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
منابع خبری از حمله موشکی نیروهای مسلح یمن به ریاض گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/698217" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698216">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUcy7qZsXY6cr4958IWi4MFMymhqTx9fHdT5Zg_Zs2h59sihaM3a6T3ikQr664sC4XUTcwGwJn8kMlYUDZLtzr5sPkTp2JDbauymWhEFU8iqHUftb2xs0U8ZFnxuwhIcge6Pwgb30VJjXc5RNn8qux9sqPYGJGVl2EiA1yUaQftc6QVYpD6ytUbAg0Ohrn6dlg2JA7wZk2pyq7BduBMfCHYrFWlxDjWWFxBO539-1Ef2P5S7fhOku1uCQ5CgMVUxoylTVdBmHPGgBc1FS7yb5UxW6nWn8KByrk2L8yENrBEW3BG_GMtVuMQDKdH9gWpgF5MLcVrBRUCnRv9dQLlV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر قیمت، بدون هزینه چاپ!
هنوز برای کمپین‌ها و تغییر منو، بنر و استند چاپ می‌کنید؟
با استندهای دیجیتال و کیوسک‌های لمسی فرانکس، ویترین و فضای فروشگاهتان را متحول کنید:
▪️
حذف ۱۰۰٪ هزینه‌های مکرر چاپ
▪️
مدیریت و تغییر محتوای تمام شعب از راه دور
▪️
ثبت سفارش و نوبت‌دهی خودکار بدون درگیر شدن پرسنل
▪️
بدنه تمام‌فلزی صنعتی با گارانتی ۱۲ ماهه تعویض قطعات
📞
مشاوره تخصصی و استعلام قیمت:
۰۲۱-۹۱۰۳۰۹۹۴
🌐
faranex.com</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/698216" target="_blank">📅 23:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698215">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvHTVc6aeKqljK6Gn6NfsR8kugJXsW6mKoewqn7Q-19YlN622ZqFJFaV9QNnqeltipup5DmsKDy8Z_KB75abmv6v2S1vqGYLfLUxJmlq5a6sqVQUBt8XGZrnpyafj-UN-J8RFW3Oz95cRf8ZA6Quhqy9feEJKTQOcce7GAv0bEBwG7gJTFHMc5Q8Ol6p-krYyiDHMTmowCQmCcXBYzYR68efBDtrdGsdKvKq23da9IJXEJAI5gFP7vksocqAu31Rpy5cW49CIHRu6u1J7TpMYCWvuNA17VRPhvru8iQHdyCMIW7Sj8ptQOmtnWvat140FDBa3a2JNQzss2Urgz3fFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنادر راهبردی اسرائیل و ۵ کشور منطقه در بانک اهداف احتمالی ایران  رسانه جریان به نقل از منابع آگاه:
🔹
بر اساس اسناد و نقشه‌های منتشرشده از سناریوی پاسخ متقابل که توسط رسانه امنیتی جریان منتشر شده، فهرستی از مهم‌ترین بنادر راهبردی منطقه به‌عنوان اهداف احتمالی…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/698215" target="_blank">📅 22:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698214">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای کانال
۱۲ اسرائیل به نقل از یک مقام اسرائیلی:
نتانیاهو هفته گذشته با ترامپ صحبت کرد و پیشنهاد عملیات گسترده علیه ایران قبل از انتخابات را داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/698214" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698213">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpZSQgb39kWFR74DqoPPPNp4WX88o4uqTmQGvslnxdHGAitUr8HafPGM-UD889az9wBtUJeUzIWa60ac7JkxSD-TNDcIPWLWr32kmIPeJfc4qEOPEWVaNm8_1SpsE8pHxJkcZ5myarxddE1OBiX22wGgrTQh8VyNU9cz4eEdtSkb2toOCcKqUVz3k862GUSOvJu8rZDkcV8Y5ECeRhmjkPVVyneQvyH-UN_hFEYtabmuJ44D5os1XvewAFyofeGDthWzNe8b_P23ml4gWUvopskIyFIR6m9JeDKfOvy1aeiAqouTQcQkotq4zBYMPJKqQpMcY8dxh3ZlXQ4wtPMjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هفت خان کالابرگ
🔹
۹ ماه پس از اجرای طرح کالابرگ و جنگ و جدل‌ها برای افزایش اعتبار این طرح، سخنگوی دولت اعلام  کرد که در مرحله نخست تنها برای سه گروه از افراد کمیته امداد، بهزیستی و خانوارهای سه‌نفره فاقد خودرو و مسکن با درآمد کمتر از ۲۰ میلیون تومان اعمال شده است. این افزایش در حالی اعمال می‌شود که رشد قیمت کالاهای اساسی، اثرگذاری اعتبار اضافه‌شده را با ابهام مواجه کرده و شروط تعیین‌شده نیز دامنه مشمولان را محدود کرده است. همچنین سازمان برنامه و بودجه با تصمیم دولت، متولی اصلی طرح کالابرگ الکترونیک شد.
🔹
هشتصدوهشتادوپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/698213" target="_blank">📅 22:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698212">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm3lZQ5H7c-p77xYRCBtLbqlCtVXPLDEPvx9UIkvg2R91ulvdXLbFs3GmTCQrC6rIiytslR9XJEHDuxqUt83EMShCqENGU9SkezqoMP7qhdWf3SzArffbsIOFCZQ1wmFQGtL_uPMgmtM3QDT6QtKqY-vYjrPwWUdAL7WIY0NUu-Prtn5Bm5eEnnpviqsN8UAWTAutNul1ap70KWV1EaW5OUPhP5uPY5WL2cJzBG6pwfcBc0jfbS0Eakp6WzdKnVYEAfvv43EtL7xEQLQ7FoPjU8phacsTS3jaRfreYitUHeS8mZCnwihJHibDQsGZ3pNAKZIODKpC9hLvvsIjAKwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش و یک کشتی کانتینری در تنگۀ هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/698212" target="_blank">📅 22:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698211">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
وزارت راه و شهرسازی در موضوع الحاق زمین به شهرها، ترک فعل کرده است
پژمانفر، رئیس کمیسیون اصل نود مجلس:
🔹
امروز وزارت راه و شهرسازی در ارتباط با کاهش هزینه مسکن مردم کوتاهی می‌کند و این موضوعی است که قابل دفاع نیست و ظلم به مردم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/698211" target="_blank">📅 22:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698210">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a2aff38f.mp4?token=gfvmaRD36EdBSezyYo4DdXkkwj2T-RrWbWTk_TbHubU9gOhAlQYscnPitSLGimiafnrKlKeNtYf-PEUnUt-8q_WllcPiWz3vuCRH9xKSPFV0dL2QJ9dhumwjI2Q8sJvORE4WKZibWD6IOcUB8hvnk3gnLxBnLGdSPh10UspxlbCByaAO7Ypw4a_I_IO1r7EmER6OXMrdf77aukX0zFbe9gSCqNLG5e3Z0SFOrAoHxnCqYZ6DYWDtvxXxLNkzITspE6DRGY2rtlhfsblu8lX0VTAT-vp9l30BIq3lVyuOmmH5-Cvrd1BR67O_QYxzvCECbiXJjnn8ve3-HjaaQp-9hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a2aff38f.mp4?token=gfvmaRD36EdBSezyYo4DdXkkwj2T-RrWbWTk_TbHubU9gOhAlQYscnPitSLGimiafnrKlKeNtYf-PEUnUt-8q_WllcPiWz3vuCRH9xKSPFV0dL2QJ9dhumwjI2Q8sJvORE4WKZibWD6IOcUB8hvnk3gnLxBnLGdSPh10UspxlbCByaAO7Ypw4a_I_IO1r7EmER6OXMrdf77aukX0zFbe9gSCqNLG5e3Z0SFOrAoHxnCqYZ6DYWDtvxXxLNkzITspE6DRGY2rtlhfsblu8lX0VTAT-vp9l30BIq3lVyuOmmH5-Cvrd1BR67O_QYxzvCECbiXJjnn8ve3-HjaaQp-9hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پژمانفر؛ رئیس کمیسیون اصل نود مجلس: خانه‌دار شدن دهک یک تا ۳، ۷۰ سال طول می‌‌کشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/698210" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698209">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd70803b81.mp4?token=nQa7yMWpo9I19qiGkxGXii81GYHkGg2pNitopp6DscLrfv8fL5J_5GBMIE0ppy6QRwTJP2_LyZ1u2mUYLTPKFQBfaTmmXWM3Gla8RdTSOmxLjwDeJyiO4sVYyt6oeBQZU1udLcDIPQCVlWmVEBmECLDkGbzIf-hUgX0e2TthIef0RQckL8XUFIIIDKTzVW1O-x1pP2-U50o0B7YqheP3VpVJTbliuKfyeiYTjxKX-FQq4qcyhgm8SrV_03H_es4ueuMkQ0-vsbuADd34IUL_vO57YyYZURffC2BoHWqnnvxBbpdqh-SrwgQqtwyl5OEkhnC1IrMGDBkYeJhDq-PvHCcs7536_7jq5Ur2OZ_UyeiKTHLg3JNp8WpLutyE3_bL5LuKO3lt7SrBiEvBM2RmLsCEQwDB9zhGhhJrZSOcCYLQVJG5izikwB_bhEDs6nkUyG08BDK2ovC6zWkl4ED6hDkDVOroInO5DlMgXip5HaP9qvrCS204crqbB1NF6gbGX6G5PSBwn5VBFJSX7Kco0Qw2-exzAQyCz6M9WjxWG8Bekcg9RztRGy6somqOy73ECGj5VUZ7IXO8lVYotsJmZzdgIb_kc1jKN61-VSrmxoh4Xdb5z3O3mkca67KoQo9e6VkHw4gkYxsCxCKhMEJ0N-ruxomPwOF7yG0mtVOQRqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd70803b81.mp4?token=nQa7yMWpo9I19qiGkxGXii81GYHkGg2pNitopp6DscLrfv8fL5J_5GBMIE0ppy6QRwTJP2_LyZ1u2mUYLTPKFQBfaTmmXWM3Gla8RdTSOmxLjwDeJyiO4sVYyt6oeBQZU1udLcDIPQCVlWmVEBmECLDkGbzIf-hUgX0e2TthIef0RQckL8XUFIIIDKTzVW1O-x1pP2-U50o0B7YqheP3VpVJTbliuKfyeiYTjxKX-FQq4qcyhgm8SrV_03H_es4ueuMkQ0-vsbuADd34IUL_vO57YyYZURffC2BoHWqnnvxBbpdqh-SrwgQqtwyl5OEkhnC1IrMGDBkYeJhDq-PvHCcs7536_7jq5Ur2OZ_UyeiKTHLg3JNp8WpLutyE3_bL5LuKO3lt7SrBiEvBM2RmLsCEQwDB9zhGhhJrZSOcCYLQVJG5izikwB_bhEDs6nkUyG08BDK2ovC6zWkl4ED6hDkDVOroInO5DlMgXip5HaP9qvrCS204crqbB1NF6gbGX6G5PSBwn5VBFJSX7Kco0Qw2-exzAQyCz6M9WjxWG8Bekcg9RztRGy6somqOy73ECGj5VUZ7IXO8lVYotsJmZzdgIb_kc1jKN61-VSrmxoh4Xdb5z3O3mkca67KoQo9e6VkHw4gkYxsCxCKhMEJ0N-ruxomPwOF7yG0mtVOQRqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوچک‌ترین استخوان بدن انسان با گذشته‌ای شگفت‌انگیز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/698209" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698208">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
منابع خبری از حمله موشکی نیروهای مسلح یمن به ریاض گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/698208" target="_blank">📅 22:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698207">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G5xOyW4Z6nLHBpcvgsQBX04xjiYEhp6VjB39pghPTOVcExmalW0osFMKMpemgJeS10KZSTbsnRGvG_CRPMQz3P4-VEuB6m2Ns5upeHtFlYJMbDcyeJFUfpjod5U6biYfbeNHkW0aYs08pC7wPHkPdp7aOSwdaKTJe8u4ptjwUWsNVVAh5MOkhbKp-CW6OG90X8Tob-cWGp9ppm1oWYzoevkP9yj1B5z3I2g1YYJTVW4HKgtkYS-zMctA4WGKvByVsP9A_e8hf2z2X6_QMhNzllfAh68yeQy5Xym4Qe_SAs2Dmk1oIN7POFSvon_vf2QVpJqZhwWpU7ANoSUIkJhIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حسینیون آذربایجان: الهام علیف دیکتاتور و سگ صهیونیسم است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/698207" target="_blank">📅 22:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6377634077.mp4?token=deuWWOVeSKFzqcArVd9FjG2XxT5qv9X_NvABe66_YtLV9Z6yIG_HMhbI1ihy3wmcy8q8CN2bxiSA0VNcuv8_ucof6MQ7CL2k68lRcfJTx6ATi30eUFJdubwayX2ma0nHXXD6hiargqElp_Na9jKB6_pIZsPEIagYAhnpTvNnq9F5kFMvXgFX4_tvsXkpUhHRALZ0RVl9CQMPvF6jWGsYpUDj2leFe19e2Z0Mj1RENpCcsCV71f6A5XUYRe79snE26GDPzSgkYtvceczMOzYFHR7wTzrO-6HA_-OpKqdmrF3ehKC5hK_uDTmh1zfmWLCXldRNHNJWMqEiv6hQ-IHhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6377634077.mp4?token=deuWWOVeSKFzqcArVd9FjG2XxT5qv9X_NvABe66_YtLV9Z6yIG_HMhbI1ihy3wmcy8q8CN2bxiSA0VNcuv8_ucof6MQ7CL2k68lRcfJTx6ATi30eUFJdubwayX2ma0nHXXD6hiargqElp_Na9jKB6_pIZsPEIagYAhnpTvNnq9F5kFMvXgFX4_tvsXkpUhHRALZ0RVl9CQMPvF6jWGsYpUDj2leFe19e2Z0Mj1RENpCcsCV71f6A5XUYRe79snE26GDPzSgkYtvceczMOzYFHR7wTzrO-6HA_-OpKqdmrF3ehKC5hK_uDTmh1zfmWLCXldRNHNJWMqEiv6hQ-IHhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی ترامپ و پوتین برای زلنسکی تصمیم می‌گیرند!
🔹
ویدیوهای کنایه‌آمیز هوش مصنوعی از بازی قدرت‌ها با سرنوشت اوکراین در فضای مجازی وایرال شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/698205" target="_blank">📅 22:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/698204" target="_blank">📅 22:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/698203" target="_blank">📅 22:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698201">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alF__fHk_l_edajdosFKim3GhFBW2TphjQmSi9pAe_J6cHhYdzUUkVTvasyzNCq-H3ZGCuyMcdaKOFHD-RJBMYIpdRiP9pmNqsRQL_MigYorNOYbJMifsoAlEzxcKxsimfaj9Ub7RNYPAJTfIcJts0sew5DbaSGbh6MGb5hoBMtnC21EJQTOu-sFEZwB55z-d6C7HcqrAj-cW0QGx9aNxepIYzNUaTHmbgCcvFF_nVxqgTCzCn233gvqJiJnPMODNFFPRdcJ8G4nwmsUyBH8znGXd4ABMtF7nkgWUK3JLxBV6E1MCyTLIfQdAe0WHbpS_ZKogdEXLnD5s4Uqz5TsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: حوثی‌ها به درخواست ایران به عربستان حمله کردند
رئیس‌جمهور آمریکا:
🔹
حوثی‌ها رفتار بسیار بدی دارند. فکر می‌کردم یک سال پیش، وقتی آن‌ها را به‌شدت بمباران کردیم و به درخواست خودشان حملات را متوقف کردیم، درسشان را گرفته‌اند.
🔹
آنها مدت طولانی سکوت کرده بودند، اما حالا دوباره ظاهر شده‌اند؛ احتمالا به دستور ایران. آنها به‌شکلی بسیار شرورانه به عربستان سعودی حمله می‌کنند و عمداً تلاش دارند قیمت نفت را بالا ببرند؛ احتمالا پیش از انتخابات آمریکا. این رفتار خوبی نیست.
🔹
باید کسی برای آن‌ها توضیح دهد که من در انتخابات شرکت نمی‌کنم؛ چون پیش‌تر با اختلافی بسیار زیاد پیروز شده‌ام. اما پس از انتخابات به سراغشان خواهم آمد و هرگز فراموش نخواهم کرد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/698201" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698200">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfzVzEFuZOKoL3psnNbkdB04pdl7gfj72Qu71JopIx9fHwOjRhKLcIj1Xxmy-Kj2bSbGxdqoXV07G6-ukmCoIZBdCuNcjZL3GbX3GBxvsHepYzV5_tms_ZjOAzAHbphZDKVKGfVMDpMngxLGErSEZni8xgto1xTAe-dNGeiEwYG8_qld7S8pqSwK7hSrSfpoAs9pHbu3r6MDXQ82boPjmQT2tBYmIoZ9Gyc88izJraTN7AjkxFi09awkVLrwDkwSaH1lS1sKE2BGzU0-J1acHZ8DHKeX50x1REC1DDzZBzbZz3SHCfUCMB4x6VgMTijH4RzePJCyKUYzIzVU1McDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش مقاومت عراق از پرواز هواگردهای ناشناس در حریم هوایی این کشور
🔹
رسانه جنگی مقاومت عراق در گزارش روزانه خود از تداوم تجاوزات و نقض آشکار حریم هوایی این کشور توسط پرنده‌های نظامی متخاصم خبر داد.
🔹
هواگردهای دشمن با استفاده از پایگاه‌های نظامی خود در اردن و اراضی اشغالی، حریم هوایی عراق را نقض کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/698200" target="_blank">📅 22:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff51b864e1.mp4?token=bk0n7KGfsrMHK2zU76lSs00FeU1YBT1mODR2jzAzxKO-A7Ojdxcth7oJHC5E8OTKHU3rHupVIR5jKlUSVCzqD0OeavVo4l6f-fK2e0cdVNvtMe_tHRmZ7QXDmhs-fGPgxgnGLjdrf3fp4GhbmOTYXQ7h2_b79_LIT2dc8Z4172JR6y_sG7ye1XPFnRnE7S1vNsD2FeeVNhg9NEa4Rc7u8oRvDZGUIm1zwwMA-eJxivzd0aTLIauIVztq0AnmEkwftEjg16RNBwg13fFisLDeRZitqn9MWKEndo9oAveLFdzM0ZLextWkgow0gK5tNHNECKfkMdIbRoaS-pJmnav8TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff51b864e1.mp4?token=bk0n7KGfsrMHK2zU76lSs00FeU1YBT1mODR2jzAzxKO-A7Ojdxcth7oJHC5E8OTKHU3rHupVIR5jKlUSVCzqD0OeavVo4l6f-fK2e0cdVNvtMe_tHRmZ7QXDmhs-fGPgxgnGLjdrf3fp4GhbmOTYXQ7h2_b79_LIT2dc8Z4172JR6y_sG7ye1XPFnRnE7S1vNsD2FeeVNhg9NEa4Rc7u8oRvDZGUIm1zwwMA-eJxivzd0aTLIauIVztq0AnmEkwftEjg16RNBwg13fFisLDeRZitqn9MWKEndo9oAveLFdzM0ZLextWkgow0gK5tNHNECKfkMdIbRoaS-pJmnav8TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/698199" target="_blank">📅 21:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698198">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee41d205c6.mp4?token=HuTtOyBQsoSxijwn7ugbsJhv3JAIRRsavXs-Fs2ESJG_JLn-8-8zI8MCdvaqt5Fdv8-3WQWqBtF3pcxMCDzAIjbw6xAfq1vLi8ib8rRdZsYgsozDHNWlKwWCOcDc1FzlnMB6-RqWF-6FM9320e2v2bncc43ozkEADNMlkg1GVQGRfxqK0jvoTjX8qQfzFt3uFWGSEbKx-afo64UHYgTNcTEjBiNo41MADl4UrwtS9bDBgRUn0phxqqspzPfoHU90k2dNieVrdEZVokO-aS9iaBWuLNEHxKynxvOoGg2ZfDcd1h5Hy8QhucYvZbFuKp-ujIQwBti7ZBJQ_KRl9Ou-Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee41d205c6.mp4?token=HuTtOyBQsoSxijwn7ugbsJhv3JAIRRsavXs-Fs2ESJG_JLn-8-8zI8MCdvaqt5Fdv8-3WQWqBtF3pcxMCDzAIjbw6xAfq1vLi8ib8rRdZsYgsozDHNWlKwWCOcDc1FzlnMB6-RqWF-6FM9320e2v2bncc43ozkEADNMlkg1GVQGRfxqK0jvoTjX8qQfzFt3uFWGSEbKx-afo64UHYgTNcTEjBiNo41MADl4UrwtS9bDBgRUn0phxqqspzPfoHU90k2dNieVrdEZVokO-aS9iaBWuLNEHxKynxvOoGg2ZfDcd1h5Hy8QhucYvZbFuKp-ujIQwBti7ZBJQ_KRl9Ou-Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین روش برای جلوگیری از حشره گذاشتن برنج
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/698198" target="_blank">📅 21:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
چرا سازمان هواپیمایی کشوری مسئولیت زمینگیر شدن هواپیماها را نمی‌پذیرد؟
دکتر کامبیز بابایی، مدیرعامل پیشین هواپیمایی آسمان:
🔹
درحالی که متولی صلاحیت و ایمنی پروازها، دفتر صلاحیت پرواز است و مدیرکل آن بر ایمن‌بودن هواپیماهای MD تاکید داشته است، چرا نظر سازمان هواپیمایی کشوری با آن مرجع مغایر است؟
🔹
چرا همزمان با اعلام اینکه برای پرواز MDها منتظر نظر شورای‌عالی امنیت ملی هستید، به نهادهای بالادستی نامه زده‌اید که مسئولیت این تصمیم را نمی‌پذیرید؟!
🔹
چرا ایرلاین‌ها را مجبور به خرید قطعات آمریکایی کردید، نه محصول ایمن داخلی؟
🔹
چه دست‌هایی پشت پرده زمینگیر شدن ناوگان عملیاتی پرواز کشور همزمان با تحریم‌های آمریکا است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/698197" target="_blank">📅 21:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92c7c633a.mp4?token=NjeAukmj0k-BpfvF4oRAMHdjIJPPMFe6_SsJXHjjmGc7qUgbV12gyo0uBAkeaRiwSCzmYv0j7MLHCc0OjBHH8B07YQVeHFqxr9jvnB6Cb6fFOpF_4TCulYQEE2HSG7uJn0WCXdvE6BcZSqFOj0avDKKgoZ8bZnTa_a-mDsDcjDpxJcigAZIhp8aG5uXHLZmrUWfhJUSsgbMXI1t6_lFwbXmUCj_8Lncmbk7sf8NNpAY2uMUCFxVFxFDl_78tFW2DXAzfHvvxI__pIfqextAwYxa-QrreyQ-vxz6m80LBW4tic0ios26tBgtPiAtUSmgljZTDnILN8SE5TXeAdJvzOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92c7c633a.mp4?token=NjeAukmj0k-BpfvF4oRAMHdjIJPPMFe6_SsJXHjjmGc7qUgbV12gyo0uBAkeaRiwSCzmYv0j7MLHCc0OjBHH8B07YQVeHFqxr9jvnB6Cb6fFOpF_4TCulYQEE2HSG7uJn0WCXdvE6BcZSqFOj0avDKKgoZ8bZnTa_a-mDsDcjDpxJcigAZIhp8aG5uXHLZmrUWfhJUSsgbMXI1t6_lFwbXmUCj_8Lncmbk7sf8NNpAY2uMUCFxVFxFDl_78tFW2DXAzfHvvxI__pIfqextAwYxa-QrreyQ-vxz6m80LBW4tic0ios26tBgtPiAtUSmgljZTDnILN8SE5TXeAdJvzOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله مروی: دو بار با رهبر انقلاب دیدار کردیم/ حالشان بسیار خوب بود
تولیت آستان قدس رضوی:
🔹
هم پیش از تدفین و هم پس از دفن رهبر شهید، رهبر انقلاب در مشهد حضور داشتند. دو بار توفیق دیدار با ایشان و اقامه نماز با ایشان را داشتیم. الحمدالله حال ایشان بسیار خوب بود و هیچ جای نگرانی وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/698196" target="_blank">📅 21:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuAzSj-jji6QDE-3iwKTz1kp78am-Uuxdn3ob_68aw-4ey2eY6c-xsdYxbXq8r21QFd1lOa_l3IYW1Y26KQhO3LPbtBHFJTu5TPCXN3Xlh1u7-r0HAAhbYDXh0e5bRo1lYoBB8GzCkNnRK_A_gzexCGwLdQ6kWu0jpE--R3bzuaFlEjodRJYfPrlD1nPy55WhLubBo4IzBeOeBF70BflVAcWt1HhTRM_A6OJoEzb0VeH7JhD85MOdcOolaoyv_gLfQp8jj6htD_WkfyJ_TtI8mysYg-d1uKVUec0oUBXEIGmFfFqtMfP7iNArAhkdPGLDL5azIhze0xt5sIsxnI9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال حمله آمریکا به مراکز هسته‌ای ایران در جنگ جدید / پاسخ ایران به حمله آمریکا به کوه کلنگ چه خواهد بود؟
🔹
اکسیوس در گزارشی به نقل از مقامات آمریکایی اعلام کرد که پنتاگون به فرماندهی مرکزی ایالات متحده دستور داده مقدمات ازسرگیری عملیات جنگی در ایران را به پایان برساند. بر اساس این گزارش، اگر عملیات‌های رزمی عمده از سر گرفته شوند، انتظار می‌رود شامل حملات به اهداف انرژی، زیرساخت‌ها یا سایت‌های هسته‌ای ایران باشند.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3252213</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/698195" target="_blank">📅 21:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/698194" target="_blank">📅 21:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698193">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl7j05Srh9nmj3eQXJJWKCkIWvFpF14huvY6MBs1COBPVeCb4uOVv86u4z7VgZOX9b6WE83NYkX6_E3GjQ2-YPPFWSE37sZ8IGWgKnq6R6kx4u5ghBVrW3XLwFPRJEIGQGXWPFc8JsAULAevtg87c1z8XkHZv9Lv6H8ANU54gJhEwvnOtaDd0ge-iC6xETO3prpY8c6pU9a6HyvRg8o8hl4nkXkFs0pTIoADE1nsUIBu5CfaqhWAhIM2-v3UVNfTAjFI6jq6OoxhWjs2h2D0OAVLrMuN9yBlOJ8enRt6CNsQSAvi0GUcNAZkS0YO4mE9jPpwKBoYjWw510jxcyq8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف پروازها در فرودگاه بین‌المللی ملک فهد در الدمام‌ عربستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/698193" target="_blank">📅 21:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6KdBG1SSMDtqZjPCxngG2cSxxQ_k7M6-OWzgiVIbolxCpHhkf8VFqLMFla8lku9-pB3L2yZoMO1XXYJf4TqzdfHEUvVd8QscU3MzjvZS1T8dmeVr4UHuGOWJX5cCaX_xPwAYYa0nxoxtEmFqMluAnobe7kuux-sGRTzXDD0jHv5J3Xfn4KQdnYFZ2stV-RyqTULnHdvAwuR3iUZR88MbZEIlrWg6hChZ6QqTq4l1wsJKzTiznG0zZfUhJ63Qi-JfphG4HN_GdVKCnPgDvBfvVfNqHJYYVZ5rDedAxfDH7krtHalTr-cG7rNu0-Ii_rcyvp1hdKFkFSPJUpBRa2jkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ خوراکی مفید برای سلامت میکروبی روده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/698192" target="_blank">📅 21:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO5PQZkOy2WJVP-Yd17vpM-i8UgF4nHNyqUbW4cz8Dgycurp1LYaqTqJEdRWPqhwnOF3b3vWsDUmCmtz9554UnHnStO8PpT-3rcRtxyRXkdvDJQKii904b4TxXp7aa1huB0QCeVb4-n07v0o4PxXvLTAMy70djXVUuZ6Xg9KJguyZDAcBhHjyRRkIlccPElAhNTD3vUxQP05Bkge3ISS4vmXAkOkx-Jvo6LhzJOXQ_cVlAADE3PJr0IFs8Z4nLhcEBgwxwe4D8lJY-IZYXN-liIdkPsjpezRAKFzbxPRse90b9PClV3MBpb3S9j42wioH3MOsgFtW55YVhoRvnRi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
افتخارآفرینی‌های پیاپی «ونوین» در بازار سهام
🔹
بانک اقتصادنوین در بازار سرمایه دستاوردهای چشمگیری را طی نیمه نخست امسال از آن خود کرده است.
🔻
اطلاعات بیشتر:
🔗
https://enbank.ir/s/mfabbXL
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/698191" target="_blank">📅 21:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe6fa0a8a.mp4?token=M2yEstqu84CQLWX-C2dxZ4kMs0MTN6UVgJl8xGXdvcscu5QTvrb-ujdrLYBOwQF_xgHMxjRKLzIx2kEja41IWm7zFDb-zVKmN0IQk5ppZ6ft7mI4b4-T1-reCIW5FIQuopDH7us42epi89RsWT-AGDKxsFNIpAnNpdGR7BeQg0f08C1oeEcK85_pSuMqbmSvWCsfeHoqosD3rVrUdPUaysYArYkweOCwdP1AixfHWKoUHrosALj_9xvlQEUmoz3CliulyNzJxJpsbYavY01f0KX56XgSuj4eW1rBQ6jm2CcBNSXktjHR1BaA_7FROOsOE127oYbQ6nO-TMWlRqgyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe6fa0a8a.mp4?token=M2yEstqu84CQLWX-C2dxZ4kMs0MTN6UVgJl8xGXdvcscu5QTvrb-ujdrLYBOwQF_xgHMxjRKLzIx2kEja41IWm7zFDb-zVKmN0IQk5ppZ6ft7mI4b4-T1-reCIW5FIQuopDH7us42epi89RsWT-AGDKxsFNIpAnNpdGR7BeQg0f08C1oeEcK85_pSuMqbmSvWCsfeHoqosD3rVrUdPUaysYArYkweOCwdP1AixfHWKoUHrosALj_9xvlQEUmoz3CliulyNzJxJpsbYavY01f0KX56XgSuj4eW1rBQ6jm2CcBNSXktjHR1BaA_7FROOsOE127oYbQ6nO-TMWlRqgyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ تست سریع برای تشخیص گوشت خالص کوبیده
🍢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/698190" target="_blank">📅 21:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
فرمانده نیروی دریایی سپاه: ما فقط یکی دو نمونه از تنبیه کشتی‌های متجاوز را نشان دادیم
🔹
آمریکایی‌ها و همکارانشان در منطقه یک سکوت رسانه‌ای ایجاد کرده‌اند که مردم دنیا نفهمند کشتی‌های متخلف تنبیه می‌شود؛ برای همین ما ۲ نمونه از تبیه کشتی‌های متخلف را منتشر کردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/698188" target="_blank">📅 21:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698187">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4410ea68.mp4?token=jDbYMuv5tH8OzQ-KgAjzSmzfBvmQ7CzpR-x6Yz1TklA0nkgUm611cg1Dmejpr2ZRiT9iGoV4iM53mViEkv4QVxSAFa2hpgwkDeFobFCJfTBa3JG72JzBNk-bwYCEsMSEC74o3iRUB9eTWUCZOFhGqJPHvEawzVZ4fvzZ51gdiAM7hGRsBcHzcY3k2N-Ma1o0feaX4bQyu5kgAhRZvHO5fydKQ3YUVfxQg16VLhvvoasV-fG-qqDh3DDlafj9QB075TleWF0T-E9Yxf_5rhBVNPnQNgFt3a-LVB-y4slL3K5SZR4z_bHYvoBy6lyCIjXFyNhRzGq5zfORwJgyvASJzFg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4410ea68.mp4?token=jDbYMuv5tH8OzQ-KgAjzSmzfBvmQ7CzpR-x6Yz1TklA0nkgUm611cg1Dmejpr2ZRiT9iGoV4iM53mViEkv4QVxSAFa2hpgwkDeFobFCJfTBa3JG72JzBNk-bwYCEsMSEC74o3iRUB9eTWUCZOFhGqJPHvEawzVZ4fvzZ51gdiAM7hGRsBcHzcY3k2N-Ma1o0feaX4bQyu5kgAhRZvHO5fydKQ3YUVfxQg16VLhvvoasV-fG-qqDh3DDlafj9QB075TleWF0T-E9Yxf_5rhBVNPnQNgFt3a-LVB-y4slL3K5SZR4z_bHYvoBy6lyCIjXFyNhRzGq5zfORwJgyvASJzFg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مشاور عالی سپاه به ادعای ترامپ مبنی بر کنترل تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/698187" target="_blank">📅 21:17 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
