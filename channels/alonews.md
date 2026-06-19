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
<img src="https://cdn4.telesco.pe/file/cWt925GrnxF4zF43HIMG6F-JqYuH6Z0sAzTmmTaqoXb4CrSNVDqz5amntQOmdLjz8xuCtyorfO32Zl5AeadZ-YmkYx1u3hvpTzKepk0xB33qSgIOc3irTnE9qRIkWZu-obe-qOG0HFTxtncJaoL7xbbg0UxPZg8GXqOYjmtGIVjLr-XUMi-Z5LKqhR319AyEnDJogkFJJfV-BEmEoaF7thlVpR2AYrmGaJVf8hU9MJ7SSBjXQlxEkNs_6Gm0FbiERGkdnQAyapB7PdtdH3kqfV773y9Hh2snooNJVSDAuJ1Atjjak2Rz61WYxxmz_diX-EKUNPCbd5cghMbUib9iLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 960K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 02:15:05</div>
<hr>

<div class="tg-post" id="msg-129267">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5hysvJ0k5tZ2YA8r_T4YYPFIc9eiPIUkThzQHzuagyFzZL7Tsl2tuUSKyt7sMUsW67WtJgOqrihsITR5bx-dJ8A7PfnwpcXcjAD_6oRPGpxPBNZDSlSeMXh-6te2H7WiyhqJeRI2JupUm8H7dlKiInmkq7jytEpJG-KwUii7Qru49EDI6KpVz9pDLRpp8ZAr0qCsJd3JWweH1qRwKzBbtACY23GZojLeEYxOLLPG-tkGP3rLhNyZB7_3UI0ZdYyfIPWZca5VITrsELTK5AkUyQ5gsbVsoDc6tU6Uwao6uWhJvDhn7wEVNnRdDlpTwXuS_Ns2eRlYARz1YJjt8CluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرکت 10 نفتکش ایرانی به نام های؛ دیونا، قهرمان، سونیا، دورنا، آمبر، خندان، برف، هدی، استارلا و دریا عمیق به طرف چین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/129267" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129266">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZypzbCpD05amA8i33YSDSi2V0p5nVxazSJtlaze4TWv1vY2jY41QegE2T2m2BROQcTTzV6xIB9wO98UIgdSteV-MKptgNNUB1ZFWMrz-Tqjp8lucN7gyjKv0CcjFJAGG7-aW1AbT8UypnM70s67otwCpO57iHUOWB9XRVz_Ac0ooFyIJmKgQ7Lk8zYiy8sTf-zEegfIWCXrncnoY28F3JpKOTlsGoJC2_ZLhy_KQeVsBGufV_OftlSX8_vlsZE6EK5J65cA1Y7QoyMQyuikd2S8m5bg3O819ufsZo9UQriCupfF-6291gP9HOMR4ReFUUNRcoRwH8hEwJZwX9D9R-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی :
دشمن اگه غلطی کرد باید تنگه رو ببندیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/129266" target="_blank">📅 01:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129265">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfVj78LQFrA2OBV9_fjX9V44SLUq2PNKcEGdXkaKnP7ttReuUUIdWIbVSU6qAk1YEMn2PpAPJFe8KdVMg_zEtgtOv3Y_nqW8fnFR4gh8pMzjsYCJ2lnqPIvmzD432PXoAF5dnt0Ngb2RfhMVYclJ_zoKXkD8hNmdsViWUQOSLnU6Xe7auh8AB7noyJqV0xKEvwHchApiAqxU5yzNXOACKJ8x503DZC_BnnLxIJuZs50fT1rp-HiJY208eO5Ix1Kw8sKlvH4NGHC2wzxzbViYeJe-DErMlZpVWRPz7TxwaWDG1dTl5EW9BF21gjkBzhseeUp4LyeTze9pCO0UiGOp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی آمریکا هم به عنوان دومین تیم به مرحله حذفی جام جهانی ۲۰۲۶ صعود کرد!
آمریکا 2_ استرالیا 0
@AloSport</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/129265" target="_blank">📅 01:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129263">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dda595df5.mp4?token=GTJiiOXftFwWJWoQ6awJPDOLAZSC5nnsgR6MucDRIG8WC5Bthrlh8GdcXVucE55yxfWZi1-4OqkZoARj9k5Miqnghhkr8-a-xLOCxxEtLGxwmhN7ZbmK63HEKd_QL1wSxc1R1RMDPA9HgEw6WcrEtwPvWTjt90wGUN6BzEQmhpEhcDFso69Tn-ztve8MPvJeS2hKStDnqVDtNm-cLB5cp2YiMHrMklK4urb7VL3Mo1rIn5_qBODkx0HsAaByuuseMK4PwN43Xb6XtM0WnCWuG6re5DQtZB5Vs6_kC-ZvmBvgJGf0xd_5ueCDXK-sLJM0lD78wFxeD8rNHmOT7z9mag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dda595df5.mp4?token=GTJiiOXftFwWJWoQ6awJPDOLAZSC5nnsgR6MucDRIG8WC5Bthrlh8GdcXVucE55yxfWZi1-4OqkZoARj9k5Miqnghhkr8-a-xLOCxxEtLGxwmhN7ZbmK63HEKd_QL1wSxc1R1RMDPA9HgEw6WcrEtwPvWTjt90wGUN6BzEQmhpEhcDFso69Tn-ztve8MPvJeS2hKStDnqVDtNm-cLB5cp2YiMHrMklK4urb7VL3Mo1rIn5_qBODkx0HsAaByuuseMK4PwN43Xb6XtM0WnCWuG6re5DQtZB5Vs6_kC-ZvmBvgJGf0xd_5ueCDXK-sLJM0lD78wFxeD8rNHmOT7z9mag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون درگیری‌های سنگین بین نیروهای اسرائیل و حزب‌الله تو لُبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/129263" target="_blank">📅 00:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129262">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78535e623.mp4?token=CoUxV78672lQp0UMLXD1ceq0S7nPFHYLBkF12m7n70OAkH2OTKjwe5fd2KYS2CIkJNubY33n35TWwpNEBmOh30M7pbz-AEJqXnq1VydAERbTATE1-odqq-dul54gGHhsXIFX7BpjPlGZfSRKYNdCAbiqlRxovcrgrjz28gND4ww_YmYx6G5wI5u_Xkty8D9q-nHI2SfvnhHuzIH-cXq_VQjXSuBAHoIsULTX4tEnv2ZcRGGqMIrgkgyVeT9Yc3XngB6arak6DPJbdVkedQomGxKbztZEoMbBWWY1af39h6qCiu9LfFPMQVpP4FXC_84Eyf7t329kmtVwzBuenr3ECA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78535e623.mp4?token=CoUxV78672lQp0UMLXD1ceq0S7nPFHYLBkF12m7n70OAkH2OTKjwe5fd2KYS2CIkJNubY33n35TWwpNEBmOh30M7pbz-AEJqXnq1VydAERbTATE1-odqq-dul54gGHhsXIFX7BpjPlGZfSRKYNdCAbiqlRxovcrgrjz28gND4ww_YmYx6G5wI5u_Xkty8D9q-nHI2SfvnhHuzIH-cXq_VQjXSuBAHoIsULTX4tEnv2ZcRGGqMIrgkgyVeT9Yc3XngB6arak6DPJbdVkedQomGxKbztZEoMbBWWY1af39h6qCiu9LfFPMQVpP4FXC_84Eyf7t329kmtVwzBuenr3ECA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مداح دوزاری، پزشکیان را تهدید کرد
🔴
پ.ن: مداح‌های بیسواد و کودن چندسالی هست که تو تمام مسائل اعم از سیاسی، اقتصادی و اجتماعی نظر میدهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/129262" target="_blank">📅 00:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129261">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c909e237b.mp4?token=qltdHlZihCqz3RdzwfayzmDaJHVPFSp-4C-q12aiAwFMTqo1_6eMUZRpQkdZzfcF7iIbmfP_Ist0U3ZmG2fqfRQnm8NQDOS0AkjJ6-s2VIIkwpUsW0jIgscrBe2L3213qlRuJDF89LTa_PBVrGglPG7kLiY6DgrJC4A_QBVIJTQ2L9qMNb7r4bE7SrhcNAc7IgwaHuROfOPmfKVF8p82c9JlD0qBWB5T2_8bHB8EEi6uYgxPElqmJNURMNpN9YgJx0BJ6juXDtTlD0EFBWl6je1OhcG2ziutirLlBiJI4iNBIMRG1UiiE-TaYjtBmE0WsY6jMnidZTXPJrt7OZ6tiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c909e237b.mp4?token=qltdHlZihCqz3RdzwfayzmDaJHVPFSp-4C-q12aiAwFMTqo1_6eMUZRpQkdZzfcF7iIbmfP_Ist0U3ZmG2fqfRQnm8NQDOS0AkjJ6-s2VIIkwpUsW0jIgscrBe2L3213qlRuJDF89LTa_PBVrGglPG7kLiY6DgrJC4A_QBVIJTQ2L9qMNb7r4bE7SrhcNAc7IgwaHuROfOPmfKVF8p82c9JlD0qBWB5T2_8bHB8EEi6uYgxPElqmJNURMNpN9YgJx0BJ6juXDtTlD0EFBWl6je1OhcG2ziutirLlBiJI4iNBIMRG1UiiE-TaYjtBmE0WsY6jMnidZTXPJrt7OZ6tiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنی مورنو، سناتور آمریکایی: لغو تحریم نفت ایران به نفع آمریکاست چون چین پول بیشتری می‌پردازد
🔴
«ما اکنون به آنها اجازه می‌دهیم که نفت خود را بفروشند. این چه فایده‌ای دارد؟ این به نفع آمریکایی‌ها خواهد بود. این باعث کاهش قیمت نفت می‌شود.
🔴
و چین را مجبور به پرداخت هزینه بیشتر برای نفت می‌کند! و همچنین متوجه می‌شود چه کسانی نفت چین را می‌خرند. بنابراین ما را در موقعیت عالی، یک مذاکره عالی قرار می‌دهد و در نهایت، من به رئیس‌جمهور ترامپ اعتماد دارم که تصمیمات درست را می‌گیرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/129261" target="_blank">📅 00:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129260">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: ما رابطهٔ بسیار خوبی با اسرائیل داریم؛ نتانیاهو یک جنگجو است
🔴
اسرائیلی‌ها باید از نتانیاهو قدردانی کنند، چون او واقعا کارش را انجام داد. ما واقعا در کنار اسرائیل به سختی مبارزه کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/129260" target="_blank">📅 00:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129258">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ درباره اوکراین: خیلی چیزها توسط بایدن به اوکراین داده شد. آنها باید هزینه‌اش را بپردازند، اما این در برنامه‌هایشان نبود.
🔴
هیچ‌کس از آنها نخواست که پرداخت کنند. من گفتم، چرا پرداخت نکردید؟ آنها گفتند، هیچ‌کس از ما نخواست، آقا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/129258" target="_blank">📅 00:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129257">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ درباره حمله دوباره به ایران:
به یاد داشته باشید، اگر این کار را انجام دهیم، ناگهان نفت به سرعت از تنگه خارج نخواهد شد.
🔴
افرادی که مالک کشتی‌های میلیارد دلاری هستند، دوست ندارند موشک‌ها بالای سرشان پرواز کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/129257" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129256">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd6c2692d6.mp4?token=NUZn9qIWdlr4-FzT7aV9Hne3NQlmt1UU7ueRIbjo-pAdEfiT--dcsZHv4pAQvqNYTp8kE1kTzq1W1Pyak2_UJioQVg4rDKWhLY67oFEkOE57QB3ozbBSXqivnMHSYq2ak0WZBMAGk6BAXvbTB4OPJM5SRzwBU9O1dB5X3OWcALDpjdABUo_wBIWbQkssH-fqPGHFvIKsXsoGCNlA7HXLGV6oMKxRR4ArYfr6IkKn24zYJS-oPOOFXlsdpyJZWc7pOvat8jKpjCYYoBsQbD0OYhMlCPME7hbJvJiKuFALCfybjuV3C3OQeLf7_wt56B8Q7e7w8kI0pXoVb8bAvMcKPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd6c2692d6.mp4?token=NUZn9qIWdlr4-FzT7aV9Hne3NQlmt1UU7ueRIbjo-pAdEfiT--dcsZHv4pAQvqNYTp8kE1kTzq1W1Pyak2_UJioQVg4rDKWhLY67oFEkOE57QB3ozbBSXqivnMHSYq2ak0WZBMAGk6BAXvbTB4OPJM5SRzwBU9O1dB5X3OWcALDpjdABUo_wBIWbQkssH-fqPGHFvIKsXsoGCNlA7HXLGV6oMKxRR4ArYfr6IkKn24zYJS-oPOOFXlsdpyJZWc7pOvat8jKpjCYYoBsQbD0OYhMlCPME7hbJvJiKuFALCfybjuV3C3OQeLf7_wt56B8Q7e7w8kI0pXoVb8bAvMcKPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: پیت هگستث یک فرد ذاتاً بااستعداد است. او نمی‌داند چگونه ببازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/129256" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129255">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5mPcz5Ov_7f8NdqKq28gZLgiFCP4i2uKk_7jPf7uNRCFI6pmN7eRf2ODKsnGJY0rIMV0wbR1XWic7OdswwYngqfYLUGhOt0nDLedD8xCiZB12BN0AWX1KOp2RJF7CHNg9NosExecpqzGhPXCHLDJAx-GuO3fiBEV58uBa6XzO1Hl7IlzE3Y6YgpUVQPzYZUKc1X0n8FyvbtG8xhmF4jHatjdAH78mcKe7iiOaEaOHyjIqwqObAgZxsierm4337_Je4Ren95afPu8Hjj8kw7Kt6PQXkILzPsViJIbCZ9QwT8Z8mTsVNpxku09jMfMUEcZvLXygRDaJ_kOXha-gaDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: ایران به نقض تفاهمنامه پاسخی بازدارنده خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/129255" target="_blank">📅 23:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129254">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ اعلام کرد: جنگنده فوق پیشرفته F47 برای ارتش آمریکا در حال ساخت است، پیشرفته ترین هواپیمای جنگی در تاریخ بشر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/129254" target="_blank">📅 23:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129253">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
صدای چندین انفجار در استان ادلب سوریه شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/129253" target="_blank">📅 23:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129252">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYFS9q6D_ovsLvZjHuROwRl7GowJc2pQx1NTzoR929u5fplxmV6_KKgiY73Lk9AXVgJ7TYpKbl_YUV1ekLvlLLRpRYN324cFbmnSTjAwsSlOYSL2CkAfuCoB_aq4SzyGcs_Lec-Kb4fQMjEqQs10rGDsff5pEd8qsQtzJNlkii8YA0kgMg4PsSyR-CWu8hKqchwsw_L1wGDN8dnRL8ocr5WM0rLOu43dPSAl5LVtubThFzgMjnuWpYaz_av2glFksfR63DnVYrFVHLs_zBNfx1p5CifpbSgmBv9bYUogprt4bkdX7TDmMtrJIdR9GnS3bAX6F3Ph58KvURrOSsk26w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای زمینی ارتش دفاعی اسرائیل بار دیگر در تلاش برای پیشروی به سمت علی الطاهر، جنوب شرقی نابتیه هستند. حزب‌الله یک بمب کنار جاده‌ای را علیه نیروهای اسرائیلی که قصد نفوذ به این منطقه را داشتند، منفجر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/129252" target="_blank">📅 23:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129251">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d97f24c8e.mp4?token=Bwg9Y6q9b1XLyvJvwBCQKLbW6AoBUn7elNvUBcaO7E9--Z5oiHeg6UAwYkDw4RL37MIHKdzp9NjSosRMI09HzcFm-06Dy1pgY57dfPjEFB1wPtNF6Fs6BZaAgICOCVMyrrRjl--BO4sqyFwlwooPFEQazk5toYAzGkBIOUoi2CSnzkxz6LR9eAlqhv8GDnLfdGMmt4OhMwN5DU_SyrPJAvcr-0TQ18tJ2Yy_-wcDSTOWEJYbUZtAhzaU_h98R9N92KCngp_Aizit8NyL2ts0YoJCe8nE8Ew66-D4MkuqSSR7MYcpKQs3gYTAhrjP2oKiR90zpvREZzMPQvp9FbLtSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d97f24c8e.mp4?token=Bwg9Y6q9b1XLyvJvwBCQKLbW6AoBUn7elNvUBcaO7E9--Z5oiHeg6UAwYkDw4RL37MIHKdzp9NjSosRMI09HzcFm-06Dy1pgY57dfPjEFB1wPtNF6Fs6BZaAgICOCVMyrrRjl--BO4sqyFwlwooPFEQazk5toYAzGkBIOUoi2CSnzkxz6LR9eAlqhv8GDnLfdGMmt4OhMwN5DU_SyrPJAvcr-0TQ18tJ2Yy_-wcDSTOWEJYbUZtAhzaU_h98R9N92KCngp_Aizit8NyL2ts0YoJCe8nE8Ew66-D4MkuqSSR7MYcpKQs3gYTAhrjP2oKiR90zpvREZzMPQvp9FbLtSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما سفرهای زیادی انجام می‌دهیم. به ترکیه خواهیم رفت.
🔴
در مقطعی، برای یک کنفرانس بزرگ به چین باز خواهیم گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/129251" target="_blank">📅 23:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129250">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
شورای اروپا: آماده حمایت از اجرای توافق ایران و آمریکا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/129250" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129249">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: اگر با ایران به توافق نرسیم، کارهایی خواهیم کرد که آنها را خوشحال نکند، اما فکر نمی‌کنم این کار را بکنیم.
🔴
توافق هسته‌ای ۲۰۱۵ با ایران یک فاجعه بود
🔴
من با رهبر جدید ایران صحبت نکرده‌ام، اما او شجاعت خاصی دارد.
🔴
من از موضع قدرت مذاکره کردم چون نیروی دریایی و هوایی ایران نابود شده است.
🔴
کشتی‌ها به طور بی‌سابقه‌ای در حال عبور از تنگه هرمز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/129249" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129248">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: حدود ۷۰۰ کشتی از تنگه هرمز عبور می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/129248" target="_blank">📅 23:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129247">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv_DbSdEu06fQKqf-F40NbPP3fs9PhxdAelm42YWMAKb6Ts4pXqJGRJtnY6xFYPB_Q-IFodT41UZ22Rj0nL1k2zeOcpjm5n4qx6CP1SOmqIjQHYPf3LZtyYTMgBry53tK1PoVb6oRId6uePDCq4QP0mhCneu9_Es8uuw3ogL0aGf7RirYHUWf8GMjnqFkmK5um7QYDUhReSa1d_emcH3dELjiZvDcEH9Vn_nbd3r0moqv-XnHn6yzyMHrJogd-hZ3IgfYhhMBdBM90GWBjJ2qhxCNYUekWVi6yx0BqZ5ggybcL_FkfFUqYUxnWpXkPUKWefo70msni3w_A4yUPHqXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از هدیه قطر رونمایی کرد!
🔴
ترامپ در پایگاه نیروی هوایی اندروز از یک هواپیمای موقت جدید ریاست‌جمهوری رونمایی کرد؛ یک جت لوکس که توسط قطر اهدا و عبارت «ایالات متحده آمریکا» بر روی آن درج شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/129247" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129246">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: کشتی‌ها دارند از تنگه هرمز خارج می‌شوند و نفت صادر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/129246" target="_blank">📅 23:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129245">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رئیس اتحادیه املاک: نرخ مجاز افزایش اجاره ۲۷ درصد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/129245" target="_blank">📅 23:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129244">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سناتور آمریکایی تد کروز: دادن میلیاردها دلار به حکومت ایران که شعار مرگ بر آمریکا سر می‌دهد، ایده بدی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/129244" target="_blank">📅 23:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129243">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b39ccf54.mp4?token=TxRx58oxgQ5qaNSxMCGszqtYPG7ItMQl0JeTdoA3_CnAnAPIthRYv8yyf-kisUwN4nCdQpF8hjH9NgB5qn0a9NXUDd1eTfT63QfDHnXlH39Co2sJjXsjNXoiyvw7OLzJZuDX30vqkTHpCUU8f7n_2rbk5oTEfjwinOqb2VtpGu06eBKm1UcEXUruF-yj4axTF6skdjRdCuoHY314mGB5Ymw-RA-4ZY_-Oia5fP0U_IKrZRUXAwAoj7QUOIccq2XUSIDEomKwc8bgtgG90StWUAGVc1OYUS-UzLGkoi5Ah526U3M2trxU0jh-qMOnuXB4D98DfnZ__mcuq_6894UEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b39ccf54.mp4?token=TxRx58oxgQ5qaNSxMCGszqtYPG7ItMQl0JeTdoA3_CnAnAPIthRYv8yyf-kisUwN4nCdQpF8hjH9NgB5qn0a9NXUDd1eTfT63QfDHnXlH39Co2sJjXsjNXoiyvw7OLzJZuDX30vqkTHpCUU8f7n_2rbk5oTEfjwinOqb2VtpGu06eBKm1UcEXUruF-yj4axTF6skdjRdCuoHY314mGB5Ymw-RA-4ZY_-Oia5fP0U_IKrZRUXAwAoj7QUOIccq2XUSIDEomKwc8bgtgG90StWUAGVc1OYUS-UzLGkoi5Ah526U3M2trxU0jh-qMOnuXB4D98DfnZ__mcuq_6894UEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ای که ترامپ وارد نشست گروه هفت شد و با شوخی خود "من رئیس هستم" جو سنگین نشست رو شکست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/129243" target="_blank">📅 23:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129242">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc24435ec.mp4?token=pt9dKpZiISwVgAyF-Vt0Us_a4grefyPXQ0cK-iHgJ0EckxPdUXFEN-FytkYqNqq7Mv7FZcp1pP3Dr-z7NTUrIV2itBKaQSUhGphGWB4t4N0HFyVxzrxkArt4PKUcdyRTmoMKeoLfGxPekz52RYSyS3WWItUspis6D6Tdx2CddlW4NlZnRbEaQaxMokZMBBEDDvZT-Kpf2MtTCgmCNa0hWymK8yRg1WNdRmIbrsyn9dSMTEzNnVh4KvuS7tN8JHtkLSg9hEeopk1qrEMGlR8v_pHKCWFJ3Xawe0JW4lOsl1a-d1zQ0NRl6jlP2SolNgTNx3GriZeaFOfxDt-T1N1vIUlgQ9S3S5WWFrrEHDxA_j_xglOPxBV0CuuwK6j7aztO1V_p-8T0lJBhJFGE_JydyZMEOqDonW_mFV-kWd4UuG2_3in5l4po8DVxXloWdeONiFKGZoCg8GYp0Mi-mQPA1Aw4BylOP8F6OoswATf2JVzkFve0zR0MS0_ZQAowPaWxz7pMqXHj4LfH4UN3Np8tLAhuFRSWP5PfCUQ2Lz2WZnOc_eBMPLfGE-LS212054VdMwM9_J-KMfeLGswoFxXGZgmGVzWICmpz3_XJtkB4CWQoDTyZAiWU6kBFHenRhCyHirT1bDOQGK58nJDPNz1e-JqPmSoqchr8FapXO3dcLIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc24435ec.mp4?token=pt9dKpZiISwVgAyF-Vt0Us_a4grefyPXQ0cK-iHgJ0EckxPdUXFEN-FytkYqNqq7Mv7FZcp1pP3Dr-z7NTUrIV2itBKaQSUhGphGWB4t4N0HFyVxzrxkArt4PKUcdyRTmoMKeoLfGxPekz52RYSyS3WWItUspis6D6Tdx2CddlW4NlZnRbEaQaxMokZMBBEDDvZT-Kpf2MtTCgmCNa0hWymK8yRg1WNdRmIbrsyn9dSMTEzNnVh4KvuS7tN8JHtkLSg9hEeopk1qrEMGlR8v_pHKCWFJ3Xawe0JW4lOsl1a-d1zQ0NRl6jlP2SolNgTNx3GriZeaFOfxDt-T1N1vIUlgQ9S3S5WWFrrEHDxA_j_xglOPxBV0CuuwK6j7aztO1V_p-8T0lJBhJFGE_JydyZMEOqDonW_mFV-kWd4UuG2_3in5l4po8DVxXloWdeONiFKGZoCg8GYp0Mi-mQPA1Aw4BylOP8F6OoswATf2JVzkFve0zR0MS0_ZQAowPaWxz7pMqXHj4LfH4UN3Np8tLAhuFRSWP5PfCUQ2Lz2WZnOc_eBMPLfGE-LS212054VdMwM9_J-KMfeLGswoFxXGZgmGVzWICmpz3_XJtkB4CWQoDTyZAiWU6kBFHenRhCyHirT1bDOQGK58nJDPNz1e-JqPmSoqchr8FapXO3dcLIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: اگر لوکاشنکو می‌گوید که نمی‌خواهد به این جنگ کشیده شود، باید حداقل با مردم خودش صادق باشد.
🔴
زیرا او کسی نیست که بتواند به جنگ کشیده شود. کشوری است که او در آن زندگی می‌کند که می‌تواند توسط روسیه به جنگ کشیده شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/129242" target="_blank">📅 23:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129241">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofAvs6W1E7Au4n02iPnswg_agg7b_9548nsoyZzg8ItXFEsikb_xU3Ol3pdGqmSlu6w3LdQRR06Mh-B1mJdEXO9mb9Gj6OWDz_4dVLCkRoB0fP3M_EEUJJmzfgaFB9_1Gk0EUBOKaYFpOptBOa3HziT2pW7Ju0lBWO5n7-XmPaos5CZSPSHd5I-_EJ070iIh7xHmJM22Yv1Mlf0nYkZgaK72U_mwEk06PJ7jNuyYp3oFZddaNqBdU5ydItLsg11fY-DT8d9WaFNj4GOgUyQJ4-QZ_uWqLNGgW2WPD9tAmdOaPPZxQbZhtoHw0VgVH_3SCzBLqSJbZAoIEyZq6AhgBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت ترامپ با انتشار نظرسنجی ای نوشت: توافقی بسیار محبوب، به جز برایِ فیک نیوز ها و شریک آنها، دوموکرات ها!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/129241" target="_blank">📅 23:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129240">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
العربیه: ولیعهد عربستان سعودی یک تماس تلفنی از سوی نخست‌وزیر پاکستان دریافت کرد.
🔴
شهباز شریف از محمد بن سلمان، ولیعهد عربستان سعودی، به‌خاطر تلاش‌هایش برای حمایت از دستیابی به یک یادداشت تفاهم میان آمریکا و ایران تشکر کرد.
🔴
ولیعهد عربستان سعودی از دستیابی به توافق میان آمریکا و ایران استقبال کرد
🔴
شاهزاده محمد بن سلمان به شهباز شریف تأکید کرد که عربستان سعودی امیدوار است آمریکا و ایران به یک توافق دائمی دست یابند
🔴
ولیعهد عربستان سعودی تأکید کرد که این کشور خواهان دستیابی آمریکا و ایران به توافقی دائمی است که ثبات منطقه را تقویت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/129240" target="_blank">📅 22:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129239">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/As1lfrRL5XfUaz0m3W9J_y255vm0zFahMYzXnFv7JxjyttLFVvc_VTtalvCw9sA6DOnL_XflUfiGaSF1zfzhlm73_dPBuR2I9BV-eBSIwhHfMDUD0DAeP7st4bH_8p4uPZ0t7_OvTeXp_iYqVAVk840lwQeWmzGoQuDtTCLlbvNzn30hEaM72VECe6vLNLPOWDa12Sl33fbFqQNoerUZKxjbpC3C4yAQMOu-pghBYCqvQ2GS8rFzd5luFMFT1v2VjYLXBKkzVFtUMyv33mUOeG50TeP5kXPkH8YPBZvUySOj3JjJqMnnB0Tb3dLKe-5wn5qwL5VU2t5SzIzs6gj2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه انگلیس: درخواست "به آتش کشیدن تمام لبنان" یک بیانیه وحشتناک و نفرت‌انگیز از یک وزیر اسرائیلی (بن‌گویر) است که به درستی توسط دولت بریتانیا تحریم شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/129239" target="_blank">📅 22:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129238">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فیلد  مارشال ، محسن رضایی: جبهه مقاومت از همه کشورهای منطقه دفاع می‌کند علی الخصوص کشورهای همسایه فلسطین و اگر جبهه مقاومت نبود این کشورها به اشغال اسرائیل در می‌آمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/129238" target="_blank">📅 22:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129237">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8ef44e0f4.mp4?token=QIpnX6ticzMmex7XNfWu_OIjy-2qPWxr1ik9SbX7xwF8IJxubIUgkkEBJaPd9vNb4z1Mp0K-RTMC3M5JAI6ecJWNUQtMdtGUv4hy_99A_nch60AwbwoDUHgHSnrJOT2RNLhd1493fASB9aMHoK-Rm7kjoUNtFcgtOPdIX1f2u46eyaeuGCSC66_wDj6Q5WpqSNHS62S2MDJv0Me0zCPq4CDnRzQ2L6-BcYpaoCyVVdCUHLnafWvEWR-20GxstH-vaTQVWoEwt3lqFOPIURjUrIKDfruC32kEET-mnAdj2_gHPN1hzDXbianyN7pZ_APeY66XfDdp2QZCB9aplQQPOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8ef44e0f4.mp4?token=QIpnX6ticzMmex7XNfWu_OIjy-2qPWxr1ik9SbX7xwF8IJxubIUgkkEBJaPd9vNb4z1Mp0K-RTMC3M5JAI6ecJWNUQtMdtGUv4hy_99A_nch60AwbwoDUHgHSnrJOT2RNLhd1493fASB9aMHoK-Rm7kjoUNtFcgtOPdIX1f2u46eyaeuGCSC66_wDj6Q5WpqSNHS62S2MDJv0Me0zCPq4CDnRzQ2L6-BcYpaoCyVVdCUHLnafWvEWR-20GxstH-vaTQVWoEwt3lqFOPIURjUrIKDfruC32kEET-mnAdj2_gHPN1hzDXbianyN7pZ_APeY66XfDdp2QZCB9aplQQPOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره ونزوئلا و کوبا: ونزوئلا نفت دارد. کوبا ندارد. کوبا املاک زیبایی و سواحل خوبی دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/129237" target="_blank">📅 22:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129236">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c77fc55c.mp4?token=GhZbvLrsJspwGnwgwBkFV4YxIk1NJ8mnjIpopO0-92_2zgx3T_6KOxqF1p78OxWvJkav8BUW7We_eq6RRK62RxAKHMUmBXmSQdbcFjLmydxdz4fk-M2Blf0L440fBuuzkQZst6HYewMJp69KxTyqZbUK7JQjJOM8vPJvPfIfSi9A1xEFvPmMLxAxQCePX-mnfyAhySafuo8RC-0_X9A_17omWWxhMskOzGbB-iA9O4V2yPslhvIxN626nQ9tFfzhNovjS887DV8w9Js3-pK-3njzxzIJgF_u4CvQCeLZf8rEYfyN4FNbkRPBnn18D8Eo7KK0oHKJcu_gQzkmU1M3Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c77fc55c.mp4?token=GhZbvLrsJspwGnwgwBkFV4YxIk1NJ8mnjIpopO0-92_2zgx3T_6KOxqF1p78OxWvJkav8BUW7We_eq6RRK62RxAKHMUmBXmSQdbcFjLmydxdz4fk-M2Blf0L440fBuuzkQZst6HYewMJp69KxTyqZbUK7JQjJOM8vPJvPfIfSi9A1xEFvPmMLxAxQCePX-mnfyAhySafuo8RC-0_X9A_17omWWxhMskOzGbB-iA9O4V2yPslhvIxN626nQ9tFfzhNovjS887DV8w9Js3-pK-3njzxzIJgF_u4CvQCeLZf8rEYfyN4FNbkRPBnn18D8Eo7KK0oHKJcu_gQzkmU1M3Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: من اعداد نظرسنجی عالی دارم.
🔴
من هر نامزدی که دارند را با ۲۵ امتیاز شکست می‌دهم
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/129236" target="_blank">📅 22:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129235">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده می‌گوید که «گفت و گوهایی» درباره برگزاری مذاکرات با ایران در واشنگتن دی‌سی از ۲۳ تا ۲۵ ژوئن داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/129235" target="_blank">📅 22:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129234">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ : تجهیزات دفاعی و این چیزها رو داشتن
🔴
ولی هفته قبل نمی‌تونستن ببینن، یه شب ۲۵ تا کشتی داشتیم، یه شب ۲۲ تا، یه شب ۱۹ تا
🔴
یه شب ۲۱ تا هر شب همین‌طور… همه اینا. برای همین مردم می‌گفتن : این نفت از کجا میاد؟ کسی خبر نداشت
🔴
ما ساعت ۱ نصف شب حرکت می‌کردیم، همه‌جا چراغ خاموش. و نیروی دریایی‌مون هم فقط نفت می اورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/129234" target="_blank">📅 22:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129233">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507cc3233d.mp4?token=TALSXqNbuj-SK9PiX6OJzc482L-Q1PLXHEA7apySfaYtSw0EdGlnKao87t4WZUp6NvC2cRsQ-ambukJwdg1t0uv_2DLnspaye5PjJ4doO3rnX0MUV_HVndPkRvehWM92pCLDx7D7mRUT-Kv4W1h5WV9qxc65-SZ0NQFyPFJoa51qKTo1uLcQLX4iLWUu0mXhtgxIlQkzUPlyzQ1eGn7HgO7zU8Vg7EW8IBWDIScif7TNxdFWF3YJg1mss97hR_biPM-Dv-2h4zw1tHGjTcKxJevE2kMvOL3GY6lC0Ie6MBcUQkcG9-kl-jjMKZxD2T4fNP3kvkIlrRNZJvn9qdfuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507cc3233d.mp4?token=TALSXqNbuj-SK9PiX6OJzc482L-Q1PLXHEA7apySfaYtSw0EdGlnKao87t4WZUp6NvC2cRsQ-ambukJwdg1t0uv_2DLnspaye5PjJ4doO3rnX0MUV_HVndPkRvehWM92pCLDx7D7mRUT-Kv4W1h5WV9qxc65-SZ0NQFyPFJoa51qKTo1uLcQLX4iLWUu0mXhtgxIlQkzUPlyzQ1eGn7HgO7zU8Vg7EW8IBWDIScif7TNxdFWF3YJg1mss97hR_biPM-Dv-2h4zw1tHGjTcKxJevE2kMvOL3GY6lC0Ie6MBcUQkcG9-kl-jjMKZxD2T4fNP3kvkIlrRNZJvn9qdfuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بایدن: مردی داشتیم که نمی‌توانست از یک پله هواپیما بالا برود و من نمی‌خواهم در این مورد صحبت کنم، زیرا اگر کمی لنگ بزنم، خواهند گفت: «آها، این فاجعه است.»
🔴
خوب، ممکن است اتفاق بیفتد.
🔴
اما نمی‌توانید هر بار که روی صحنه می‌روید لنگ بزنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/129233" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129232">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: روبیو به جوزف عون تأکید کرد که ضروری است حزب‌الله خلع سلاح شود و دولت کنترل خود را گسترش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/129232" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129231">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ درباره تنگه هرمز: ما الان تنگه هرمز را کاملاً بسته داشتیم.
🔴
همه جای آن مین‌گذاری می‌شد، و موشک‌هایی بر فراز کشتی‌های میلیارد دلاری پرواز می‌کردند. آن کشتی‌ها هرگز حرکت نمی‌کردند.
🔴
ما برای ماه‌ها نفت نداشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/129231" target="_blank">📅 22:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129230">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
هم اکنون پرواز بیش از 9 هواپیمای سوخت رسان آمریکایی بر فراز تنگه هرمز و خلیج فارس.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/129230" target="_blank">📅 22:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129229">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: طولانی‌ شدن جنگ علیه ایران، جهان را با رکود مواجه می‌ساخت
🔴
طولانی شدن جنگ علیه ایران برای جلب رضایت تندروها در آمریکا، ممکن بود به رکود جهانی منجر شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/129229" target="_blank">📅 22:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129228">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a5d29a6e.mp4?token=OIbDQxoW2U3WGhnyopBb2KXpWlIFvh7bnm6HjRst6yma-mBt8tdeRaNhNdrEXlF_TT1fGyPlRkd1COxsIBCmUEPPFo_WoIjW2wCqAB_K4cTjMK00WDmB4pgXFPwiYT-8X6JZbXku_rkYUYRUc1HMVVLce-HJLkGg-GA6PV7HVhVloqNR4B-AOL0EUZq5sne_sesR5pSQpd0c7XWPrTICKl1tWU7OzmHPcsM8Sxa6-7ntL_UZVKsL2uyTI2R70ZtcyXqQjHI8X_9cm8OM-PjctVpSQenc4bjQKHIpXiA4aCdziIcmdso-uhg7mX_j1v8G4_Hj54YOAUhOXlqj738-9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a5d29a6e.mp4?token=OIbDQxoW2U3WGhnyopBb2KXpWlIFvh7bnm6HjRst6yma-mBt8tdeRaNhNdrEXlF_TT1fGyPlRkd1COxsIBCmUEPPFo_WoIjW2wCqAB_K4cTjMK00WDmB4pgXFPwiYT-8X6JZbXku_rkYUYRUc1HMVVLce-HJLkGg-GA6PV7HVhVloqNR4B-AOL0EUZq5sne_sesR5pSQpd0c7XWPrTICKl1tWU7OzmHPcsM8Sxa6-7ntL_UZVKsL2uyTI2R70ZtcyXqQjHI8X_9cm8OM-PjctVpSQenc4bjQKHIpXiA4aCdziIcmdso-uhg7mX_j1v8G4_Hj54YOAUhOXlqj738-9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک کاپوتو از اکسیوس: این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
🔴
ترامپ
: خامنه‌ای جونیور با پدرش متفاوت است. آن‌ها افراد متفاوتی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129228" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129227">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8850d1df.mp4?token=a1y0K3XPuv9b2A4tRUh0LI709I1LyiW4XNvSKbzLxhaZufx0extYn7JcR2tnTYOenFLpERtGzPBU1K5G466dIKkUceH0fssJF36xlvs5hGi1dSGLlyfq3FUN5OabEJDCKlpsDVxvedjoZcHFLUU1L_dgbJfRkKijZQBCPnsTSfrf12QaHF4U17d_eo8sxFQNtXzEQtLYON8R-GquL0qNfRyrMQwsfTmZFEAX06HbM-W_OexBXoQ8YnkFGXkZs5Abd61twJh8eH4zLXaUFzWW9YkTLIeBNc4GZhaPMO4ToNyrDMbtqFZA7q1bq4od65Q6jejjRgm-PEq26YjPvpT4Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8850d1df.mp4?token=a1y0K3XPuv9b2A4tRUh0LI709I1LyiW4XNvSKbzLxhaZufx0extYn7JcR2tnTYOenFLpERtGzPBU1K5G466dIKkUceH0fssJF36xlvs5hGi1dSGLlyfq3FUN5OabEJDCKlpsDVxvedjoZcHFLUU1L_dgbJfRkKijZQBCPnsTSfrf12QaHF4U17d_eo8sxFQNtXzEQtLYON8R-GquL0qNfRyrMQwsfTmZFEAX06HbM-W_OexBXoQ8YnkFGXkZs5Abd61twJh8eH4zLXaUFzWW9YkTLIeBNc4GZhaPMO4ToNyrDMbtqFZA7q1bq4od65Q6jejjRgm-PEq26YjPvpT4Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حمله به پل B1: من بزرگترین پل آن‌ها را نابود کردم چون دیر در یک جلسه حاضر شدند. آن‌ها گفتند که کار خیلی خوبی نبود.
🔴
آن پل، [همانند] پل جورج واشنگتن آن‌ها بود. آن را در سه دقیقه پاک کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/129227" target="_blank">📅 22:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129226">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938ae8cd57.mp4?token=EE0OoXyyRtqNgIt026iZlRL2MwZ8mxZg8i_VO7RTC577GeIkiu2avCZVdsuma_F3IRd3VPZ6qydFMeGxT3raB9ru8YqsN1q4OsVkrNa-jXFB-KgAGm5pICywEq8wP5hpVOXJCD3tIXoFQ6m7z7o0RiuD6no5HXSBAgpY6RqrKxaZH1HwWp6g7adSdDYNDb0o3U-ZnBBC4fca4wqO1ZjgSUfjXCuvZtRPzuM6pRlsSf0-yp-ZBlJZDK8dfj0ekzAy--51pSV6JgKnNzemGhfvNLWdfrlfB5Eq29FIY8ToXlh_sHGBDBzDxEsAbNpYYdNOwJPsg1q3WizIK5l2ePjqWLNylm9QFGcJ3Wt1LwisE65_QfCeps7yNiNoreK-Gf9B4Swu41rj19fhduJ0xgVOprajD8EtmQz6ht217ncyZ4nqcX2Ro3WshWWyASwDlYYBCkWIBSrfejzL0gBa0ZPZPu0Fj8Suh6oGJp8g2yjkvyrL6KJdX4vF_Pz6QlfL3W7kM_TWbxylKo8MgZny3HNyXkPiGSA_vwuuSYMbgqakXX4IYdvK61Yot6M6fYDyaErpsK8zaDxRcwwc2egHTqcL0G_3j3qQV7zYP3CRUWCnMKg2v4nBecbN_0eveJKlPnLujMh46WC2VdqnKGyO_wOeZ6YOssZUeMMftPK8cTz5yXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938ae8cd57.mp4?token=EE0OoXyyRtqNgIt026iZlRL2MwZ8mxZg8i_VO7RTC577GeIkiu2avCZVdsuma_F3IRd3VPZ6qydFMeGxT3raB9ru8YqsN1q4OsVkrNa-jXFB-KgAGm5pICywEq8wP5hpVOXJCD3tIXoFQ6m7z7o0RiuD6no5HXSBAgpY6RqrKxaZH1HwWp6g7adSdDYNDb0o3U-ZnBBC4fca4wqO1ZjgSUfjXCuvZtRPzuM6pRlsSf0-yp-ZBlJZDK8dfj0ekzAy--51pSV6JgKnNzemGhfvNLWdfrlfB5Eq29FIY8ToXlh_sHGBDBzDxEsAbNpYYdNOwJPsg1q3WizIK5l2ePjqWLNylm9QFGcJ3Wt1LwisE65_QfCeps7yNiNoreK-Gf9B4Swu41rj19fhduJ0xgVOprajD8EtmQz6ht217ncyZ4nqcX2Ro3WshWWyASwDlYYBCkWIBSrfejzL0gBa0ZPZPu0Fj8Suh6oGJp8g2yjkvyrL6KJdX4vF_Pz6QlfL3W7kM_TWbxylKo8MgZny3HNyXkPiGSA_vwuuSYMbgqakXX4IYdvK61Yot6M6fYDyaErpsK8zaDxRcwwc2egHTqcL0G_3j3qQV7zYP3CRUWCnMKg2v4nBecbN_0eveJKlPnLujMh46WC2VdqnKGyO_wOeZ6YOssZUeMMftPK8cTz5yXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره آیت‌الله مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
🔴
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
🔴
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/129226" target="_blank">📅 22:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129225">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ درباره گروه هفت: باید گروه هشت را حفظ می‌کردند.
🔴
اگر این کار را می‌کردند، احتمالاً جنگی بین روسیه و اوکراین وجود نداشت، اما اوباما نمی‌خواست پوتین آنجا باشد.
🔴
قبلاً گروه هشت بود. اگر آن را همان‌طور حفظ می‌کردند، بسیار بهتر می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/129225" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129224">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b68770a38.mp4?token=SevNpvJn6gKZfjlwOkMsPWOrhZV8pToUBmJFfS9LdI8IBx0L5awEuglSrIaw3hVFedpGHywmZzcSI9V1-7j12I6EeYb4vPRL2b7hwVyup2w9lWvdvEUFXmZrMHJCDNTTgnxxGhWC95umiPP9V9bf-Rrccz0KKRoHfHrQCjdDyf5HvqGDIbeTKxRMg9Yhn7wNiY6JIG4MeNHDM0elH8nLDLap3vdDJaS0sURJqD2Rm6-79v-SEu2L2NZIEeieSlM4TfgJtG-uS8TOcL1NyolJG14NDx1Os6BCgOanDFcMgNquBT_xiVlZk7-E0WjXrOO2AxYI_MmsvXILzNsbSaUEpjnpoYlP85EW_WoqHEGpw8ERWeg4-Yi1HZGJpO9O2un05Qw4GbaipfhFdG8OI7BOpDlq7Ad_U6QvDSSbtYp_vooDUY87aGA6mBnpE-TkvZYh4SCGG7dsGfF_8Cb0W7Lz_Ik_t42W3OcarAOkDFlzHeEgQoPXMiJNUEUjHXRJ3e9cWayiq5mazcPGZaJ5SZfswF6pA-6puKr4kaqPk-0a6Mwac9c4bJUcYctpIcxnnn7_n0momoFy8ud9eZ-J2I2sGiL0dkTSuTYXUPb1HQdLDbXNuljUI2DgWCOsdbmqeZiM03k9V25Gyftm67KxGdOUx23byiaf0-hiTyKVtB5_3fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b68770a38.mp4?token=SevNpvJn6gKZfjlwOkMsPWOrhZV8pToUBmJFfS9LdI8IBx0L5awEuglSrIaw3hVFedpGHywmZzcSI9V1-7j12I6EeYb4vPRL2b7hwVyup2w9lWvdvEUFXmZrMHJCDNTTgnxxGhWC95umiPP9V9bf-Rrccz0KKRoHfHrQCjdDyf5HvqGDIbeTKxRMg9Yhn7wNiY6JIG4MeNHDM0elH8nLDLap3vdDJaS0sURJqD2Rm6-79v-SEu2L2NZIEeieSlM4TfgJtG-uS8TOcL1NyolJG14NDx1Os6BCgOanDFcMgNquBT_xiVlZk7-E0WjXrOO2AxYI_MmsvXILzNsbSaUEpjnpoYlP85EW_WoqHEGpw8ERWeg4-Yi1HZGJpO9O2un05Qw4GbaipfhFdG8OI7BOpDlq7Ad_U6QvDSSbtYp_vooDUY87aGA6mBnpE-TkvZYh4SCGG7dsGfF_8Cb0W7Lz_Ik_t42W3OcarAOkDFlzHeEgQoPXMiJNUEUjHXRJ3e9cWayiq5mazcPGZaJ5SZfswF6pA-6puKr4kaqPk-0a6Mwac9c4bJUcYctpIcxnnn7_n0momoFy8ud9eZ-J2I2sGiL0dkTSuTYXUPb1HQdLDbXNuljUI2DgWCOsdbmqeZiM03k9V25Gyftm67KxGdOUx23byiaf0-hiTyKVtB5_3fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مکرون: مکرون کار عالی در میزبانی از گروه هفت انجام داد. واقعاً خوب. بازی‌های خوبی بود.
🔴
او حدود یک هفته قبل از من دعوت کرد. گفت، «آیا می‌توانی به من لطفی کنی؟ آیا به پاریس می‌آیی؟ ما دوست داریم تو را گرامی بداریم.»
🔴
من آن را به عنوان احترام به کشور در نظر گرفتم. اما او گفت، «من دوست دارم تو را گرامی بدارم.»
🔴
و او برخی از بزرگترین افراد اروپا و فراتر از آن را آنجا داشت و ما در ورسای بودیم و من نوعی قصد انجام آن را نداشتم، اما او ضعف من را می‌دانست.
🔴
آن‌ها شام‌هایی در ورسای برگزار می‌کنند.
🔴
ما شام فوق‌العاده‌ای داشتیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129224" target="_blank">📅 22:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129223">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7148359604.mp4?token=W_j_kkLGdG0IPp_ihAbENClZ9uI4IFDF_-Av-j_emvZPI7fMzPaGrO_VlI_d8rwONv1yJTbNK_cn0dSwwMFHpu6CNSgdDTQQ_RfQBWbIISGi7nn4p2JhVQkQeBNERJ-mKNA8Sf_QKrbtKj87lTWDYwdwaOBowcRx9gzbRZL_hFvWSLHSIb4TlN90I_hkJ1_cSNOp22Vc8wyvGzs_PIsRqElqx6dkaAarYv2dJslPlGec1Iz0ZMlQwhPyFy6ae913ZT1XP2vXe0GQB2-oEiJdtuoVqbcSm718X3BubYWbE15lTI2dxBEpaRlzAAe8T0r_pyqaTTzBHOBubYO7pDRmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7148359604.mp4?token=W_j_kkLGdG0IPp_ihAbENClZ9uI4IFDF_-Av-j_emvZPI7fMzPaGrO_VlI_d8rwONv1yJTbNK_cn0dSwwMFHpu6CNSgdDTQQ_RfQBWbIISGi7nn4p2JhVQkQeBNERJ-mKNA8Sf_QKrbtKj87lTWDYwdwaOBowcRx9gzbRZL_hFvWSLHSIb4TlN90I_hkJ1_cSNOp22Vc8wyvGzs_PIsRqElqx6dkaAarYv2dJslPlGec1Iz0ZMlQwhPyFy6ae913ZT1XP2vXe0GQB2-oEiJdtuoVqbcSm718X3BubYWbE15lTI2dxBEpaRlzAAe8T0r_pyqaTTzBHOBubYO7pDRmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره پاکستان: در پاکستان، شما فرمانده کل قوا را دارید که عالی است. و نخست‌وزیر را دارید و آن‌ها با هم بسیار خوب کنار می‌آیند.
🔴
مرد نظامی کاملاً به نخست‌وزیر احترام می‌گذارد.
🔴
دیدن این موضوع زیباست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/129223" target="_blank">📅 22:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129222">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: روبیو به جوزف عون تأکید کرد که ضروری است حزب‌الله خلع سلاح شود و دولت کنترل خود را گسترش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/129222" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129221">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9501f33214.mp4?token=X5Fi9UuksUKMVinzfSx9KgXvwnzcy-GY8bl1sGEyuRKm8xJ6OKbI9egD4JoQNtxT0vb9-3440PswmvR7GRPeYHjyHr0JTUIFohhZUfpBWFkItrQxGS0LSkxavO6PNhT45gKfveQ3BhALAVC6iwAImnZZAku5wp1K8Gap83zUYewH9pQJWx650tzLr-djB2DDj3ZcDXS88F6FRweP_qxGVmGfGCIEjSPpjx3jPztNX101GuW_M6xewfpcGeypGSaDAU8xz_1-XawHOwB6WzS0ULGPoOICC53CJ2cR7JSPRcTlUbTzR8dWVuWaPg4DTAccYktzi4t0MFkkWvq2czMbWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9501f33214.mp4?token=X5Fi9UuksUKMVinzfSx9KgXvwnzcy-GY8bl1sGEyuRKm8xJ6OKbI9egD4JoQNtxT0vb9-3440PswmvR7GRPeYHjyHr0JTUIFohhZUfpBWFkItrQxGS0LSkxavO6PNhT45gKfveQ3BhALAVC6iwAImnZZAku5wp1K8Gap83zUYewH9pQJWx650tzLr-djB2DDj3ZcDXS88F6FRweP_qxGVmGfGCIEjSPpjx3jPztNX101GuW_M6xewfpcGeypGSaDAU8xz_1-XawHOwB6WzS0ULGPoOICC53CJ2cR7JSPRcTlUbTzR8dWVuWaPg4DTAccYktzi4t0MFkkWvq2czMbWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من برزیل را تماشا کردم، رهبری که کمی او را می‌شناسم. او فردی بسیار ناپایدار است.
🔴
کاپوتو: شما طرفدار لولا نیستید، اگر اشتباه نکنم.
🔴
ترامپ: فکر نمی‌کنم درباره او فکر کنم، صادقانه با شما بگویم. واقعاً درباره او فکر نمی‌کنم. برام مهم نیست.
🔴
اما او اکنون نوع متفاوتی از فرد است. بسیار ناپایدار. تماشا کردم که او سخنرانی کرد. بسیار ناپایدار بود و اشکالی ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129221" target="_blank">📅 22:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129220">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ : کار فوق‌العاده‌ای کردم؛تو دوره اول ریاست‌جمهوریم
🔴
ارتش رو از نو ساختم و حسابی تقویتش کردم. یه نگاهی هم به ونزوئلا بندازید؛ کل ماجرا تو ۴۸ دقیقه جمع شد
🔴
روابطه‌هاشون این‌طوریه، و ما هزینه‌ی اون جنگ با ونزوئلا رو چندین و چند بار دادیم
🔴
الان هم داریم میلیون‌ها بشکه نفت ازشون درمیاریم و حتی داریم کاری می‌کنیم که بیشتر از قبل براشون پول دربیاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129220" target="_blank">📅 21:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129219">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2593101003.mp4?token=kLpoXAwy8NgrIgiR7ddC1O5WK2ZJ7cRIkoHUmL2HLXkF8r1XwdQh4KQm_Nrtco8uVPXEcVPDIidiiFkuY0f-U-BNU58UsWjfIv9TLp8bXB3lj0MbCkD5_Gf5ngjNb_sciGw97zqnFJhquTzezHGQz6Ayk96A1Z8_3mgx-CV3Tw7JanISooCuzy_HvXypG34ctr9LqWyZ0nmR2XX8WcnCTBZd_Cm0XdK-VQ6AmA-nIYh3YFfzZaVfGgptjoo_EOdtdJJliaR5s5j5cf6ZM6bzFWh3mmRx9kjYw6gDTULOdWTcWqVCbbYJulGLyktWSLCpeM-MOwl3__RfN3sVnjAHwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2593101003.mp4?token=kLpoXAwy8NgrIgiR7ddC1O5WK2ZJ7cRIkoHUmL2HLXkF8r1XwdQh4KQm_Nrtco8uVPXEcVPDIidiiFkuY0f-U-BNU58UsWjfIv9TLp8bXB3lj0MbCkD5_Gf5ngjNb_sciGw97zqnFJhquTzezHGQz6Ayk96A1Z8_3mgx-CV3Tw7JanISooCuzy_HvXypG34ctr9LqWyZ0nmR2XX8WcnCTBZd_Cm0XdK-VQ6AmA-nIYh3YFfzZaVfGgptjoo_EOdtdJJliaR5s5j5cf6ZM6bzFWh3mmRx9kjYw6gDTULOdWTcWqVCbbYJulGLyktWSLCpeM-MOwl3__RfN3sVnjAHwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره نیویورک‌تایمز : کمی پیش حقیقتی را بیان کردم. گفتم: «اگر (مقامات ایران) پرچم سفید تسلیم را بالا می‌بردند و می‌گفتند: "سپاس خداوند را، ترامپ بزرگترین رئیس‌جمهور است، ما در اینجا تسلیم می‌شویم"،» نیویورک تایمز می‌نوشت که آن‌ها جنگ را برده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/129219" target="_blank">📅 21:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129218">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d60f7b5da.mp4?token=JA9KpakMXpOpZH_r7tUztSEe44pizdc9qup_3wffta0fUEFT9BdYQD5AjCcllPUhEF3Tt_e3ZeclpWaxkc4QcWlmN4dD_sSDFdjXGiQF-zk8E99N6OxnBJzbchewTo0vy6PfkV1EG8uHv8g-dTJRVpYwAlTdIvZbGKS4tCEUmQbn2Qq29FaZjLCCoXKD96NTf_cD01ygu97KpbFx8WG-1vBpGk2o--OQ15aYaJkzXVW9ZIOZRVqMIFQWqpgznkQpp-iEiLXCjMzDKcBEvlk5SKX8B0a7x2bW6F6O799uOGAM-bJJFGsqW59ZHjlcklEEj9MPDeWwrLqDnxJ-AojTAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d60f7b5da.mp4?token=JA9KpakMXpOpZH_r7tUztSEe44pizdc9qup_3wffta0fUEFT9BdYQD5AjCcllPUhEF3Tt_e3ZeclpWaxkc4QcWlmN4dD_sSDFdjXGiQF-zk8E99N6OxnBJzbchewTo0vy6PfkV1EG8uHv8g-dTJRVpYwAlTdIvZbGKS4tCEUmQbn2Qq29FaZjLCCoXKD96NTf_cD01ygu97KpbFx8WG-1vBpGk2o--OQ15aYaJkzXVW9ZIOZRVqMIFQWqpgznkQpp-iEiLXCjMzDKcBEvlk5SKX8B0a7x2bW6F6O799uOGAM-bJJFGsqW59ZHjlcklEEj9MPDeWwrLqDnxJ-AojTAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره رسانه‌های داخلی جمهوری اسلامی ایران
:
اگر به ایران نگاه کنید، آن‌ها ۴۷ سال است که این کارها را انجام می‌دهند.
🔴
آن‌ها شما و همه دیگران را تحقیر کرده‌اند، تمام رسانه‌ها و همه چیز.
🔴
آن‌ها در برخورد با مطبوعات بسیار خوب عمل می‌کنند. آن‌ها رسانه‌ای جعلی(فیک) و عالی دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/129218" target="_blank">📅 21:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129217">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5a6eab44.mp4?token=UoGI0cjKxrQrdFEWmIf-jVdl9iNgpeSF3KyzuARw4TkCGRhB-UzjxdNvH6AgWAYxxJkNmUCIfFbpRsrswc0ZzSdVLfTQSdxtSszSPPEEAs7bxE_GzeA-x1sEHCme-jJ_MlptTJK-vCG11Rzf-x4fN9gZiF03jdg-qdB5GYA8VZf_eXu8d3O2QMhR1W8vxpZI-dwRU-9MTiqczl3wrQPNKF54o17l0Gr3Pot6ZnQ9-hMW0-7TiNgCs5kx5kyuLs4sRb1ZEU9xaI8Ym-BtXaPYmMZXkNvdlkKE2yV5aijPp-3vyCpiafrTb2lscmqWw0Yg1o1cOiQoCyX4X2Ml1ITAUwgXUQvyw7ISvpgGzRGhQ5dUXnTT2Mw0Za1WjlcE5wJSuaWAjG75QhaQ9DfN0OjKIgrE0v2ErWdfbAfnQ11NLn09oxwpk0Rn7yOW96TB2sXm1wxKZl5hUVFTtHYi7Ujzr03lGbJLnzAntHU-Ql2HC2wDES1XW7ibSMFnjy488N8bQuwakwpmXC1w74YIqjH1Qd7pf-NVNoGF-zC93FJWIlcByF-Cmxts-9rnyWTEpS0fX5MlMFSt68aHYduSnoawB3jfVcv3rs_X9We9TDhTt75-3PmUdESDM1xLIdOKLGr7xj0pmv6mylBOHZOeSuw2JfCc0Rk5zNZbrMN13Z3twO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5a6eab44.mp4?token=UoGI0cjKxrQrdFEWmIf-jVdl9iNgpeSF3KyzuARw4TkCGRhB-UzjxdNvH6AgWAYxxJkNmUCIfFbpRsrswc0ZzSdVLfTQSdxtSszSPPEEAs7bxE_GzeA-x1sEHCme-jJ_MlptTJK-vCG11Rzf-x4fN9gZiF03jdg-qdB5GYA8VZf_eXu8d3O2QMhR1W8vxpZI-dwRU-9MTiqczl3wrQPNKF54o17l0Gr3Pot6ZnQ9-hMW0-7TiNgCs5kx5kyuLs4sRb1ZEU9xaI8Ym-BtXaPYmMZXkNvdlkKE2yV5aijPp-3vyCpiafrTb2lscmqWw0Yg1o1cOiQoCyX4X2Ml1ITAUwgXUQvyw7ISvpgGzRGhQ5dUXnTT2Mw0Za1WjlcE5wJSuaWAjG75QhaQ9DfN0OjKIgrE0v2ErWdfbAfnQ11NLn09oxwpk0Rn7yOW96TB2sXm1wxKZl5hUVFTtHYi7Ujzr03lGbJLnzAntHU-Ql2HC2wDES1XW7ibSMFnjy488N8bQuwakwpmXC1w74YIqjH1Qd7pf-NVNoGF-zC93FJWIlcByF-Cmxts-9rnyWTEpS0fX5MlMFSt68aHYduSnoawB3jfVcv3rs_X9We9TDhTt75-3PmUdESDM1xLIdOKLGr7xj0pmv6mylBOHZOeSuw2JfCc0Rk5zNZbrMN13Z3twO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به اکسیوس: اگر دونالد ترامپ نبود، اسرائیل کاملاً نابود می‌شد.
🔴
ما کسانی هستیم که اسلحه‌ها را داریم. ما کسانی هستیم که کل توافق را داریم. ما کسانی هستیم که بمب‌افکن‌های بی-۲ و غیره را داریم.
🔴
رابطه با نتانیاهو... خوب است، اما باید او را کمی عاقل‌تر نگه داریم.
🔴
سوال
: آیا می‌توانید از حمله اسرائیل به لبنان جلوگیری کنید؟
🔴
ترامپ:  بله، من می‌توانم. آن‌ها برای من احترام زیادی قائل هستند و همان‌طور که من می‌گویم عمل می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/129217" target="_blank">📅 21:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129216">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76380d5ba7.mp4?token=RZ7xBTut66oKdmZsMulaa8HMyri5ONuETSFZNR-s-SIN3ZlnjWcfihYIPHNV6R0E7D38NQxzTnAJrDuq2wWyyo7og1WqvlNfYkwY5Qx6vBWd1o09Sghyu-XmWKbIB8pZq_YL8PsvH3FkQgBGs4esWMv_PmL6HQXx77FxXZZ5TIxw63ixq_XuBQaBnfjb7N3Hv6VmeVLBuloEgmfxQ9mWVtLUNVJ0rZy0PWzNHYtXIgi-BhY_jgcf2mD9wq1ADXbNlda53st7O2JoIMvudz1HROhsXO32bcY7GHcQ-cJ4gMRilaDyfYC-zi5j99ddOPgUbsVkeRWALvek_C7ZgY213A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76380d5ba7.mp4?token=RZ7xBTut66oKdmZsMulaa8HMyri5ONuETSFZNR-s-SIN3ZlnjWcfihYIPHNV6R0E7D38NQxzTnAJrDuq2wWyyo7og1WqvlNfYkwY5Qx6vBWd1o09Sghyu-XmWKbIB8pZq_YL8PsvH3FkQgBGs4esWMv_PmL6HQXx77FxXZZ5TIxw63ixq_XuBQaBnfjb7N3Hv6VmeVLBuloEgmfxQ9mWVtLUNVJ0rZy0PWzNHYtXIgi-BhY_jgcf2mD9wq1ADXbNlda53st7O2JoIMvudz1HROhsXO32bcY7GHcQ-cJ4gMRilaDyfYC-zi5j99ddOPgUbsVkeRWALvek_C7ZgY213A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره شی: او مردی قوی است. او بازی نمی‌کند. او نمی‌نشیند و نمی‌گوید: «آها، چه روز زیبایی. به خورشید نگاه کنید.»
🔴
هیچ‌کدام از آن چیزها وجود ندارد. همه چیز جدی و کاری است که من دوست دارم. فکر می‌کنم عالی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/129216" target="_blank">📅 21:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129215">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427ccd23df.mp4?token=RWFE7rKLA-r_vVdxK-t7i1HNMWhdeZKhTMhXe1tRQKFWv7vydZVSkIJDAHxzBonFqAITq5l_7ozBo9XPysc_C6G7nlm8hHAcMUUhFxkRyFst_OKtfeX2VhbOjLozS8sxnlXyhrBkPhfPlyzJOUUpUMIQErTQlPHWPCTLMv6VB7NHgIFUyPcrkjUHT01DBLCKSnH_OugE0q2KMQn4I6QRrUNypWkPXetkQh0tZBghOJOV5L56L5_lbcA7jogZk5TQ_y_bJXbsAUk1HCxBC0ibOnUIYB38m8M2w2ovJNB-rsGf31lwO2oRyCSaMOd2NBnoSt_1yEfm3sErBIASJ-aLQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427ccd23df.mp4?token=RWFE7rKLA-r_vVdxK-t7i1HNMWhdeZKhTMhXe1tRQKFWv7vydZVSkIJDAHxzBonFqAITq5l_7ozBo9XPysc_C6G7nlm8hHAcMUUhFxkRyFst_OKtfeX2VhbOjLozS8sxnlXyhrBkPhfPlyzJOUUpUMIQErTQlPHWPCTLMv6VB7NHgIFUyPcrkjUHT01DBLCKSnH_OugE0q2KMQn4I6QRrUNypWkPXetkQh0tZBghOJOV5L56L5_lbcA7jogZk5TQ_y_bJXbsAUk1HCxBC0ibOnUIYB38m8M2w2ovJNB-rsGf31lwO2oRyCSaMOd2NBnoSt_1yEfm3sErBIASJ-aLQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
اگر ما آنها را نمی زدیم، آنها یک سلاح هسته ای داشتند.
🔴
آنها از آن برای اسرائیل استفاده می کردند.  شما از آن در عربستان سعودی نیز استفاده می کردید.
🔴
تقریباً بلافاصله موشک ها به سمت این پنج کشور دیگر (قطر، امارات، کویت، بحرین) پرواز کردند.
🔴
گفتم چرا این کار را می کند؟
🔴
و میدونی چیکار کرد؟
🔴
این پنج کشور را به دامان من آورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/129215" target="_blank">📅 21:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129214">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a75bf31b4.mp4?token=q_f3-FEzSB7JrRoPVcnWEuCPfrLm_zHP0eL68WUBpVMm7SbrC4CioLlvG65M39S4r0VL2KGm4Uu_Hcbd1jIrKGwjNhPyduUhuUPwMf4zpSAk0sXm5tvKXth8l22BYmCsAuFrlA1UDzcYGiYS-NOn-CpRBP1xscqBG4SHIEdIFykIJK6XMI91H3voUmnGLbYGuS1zImW1C6aB3ihBc31i-bdhUK7PvQpyqvDgL4DOF-SrA5y5J69_i9j6gCkdRQ42av1JH6hMHs1UVvRBKl44o62EPQgV_TeQd_Qh7c9l17Wwv2Ze6V-lxlFF9b1q4yuzzO3V1Txuc8kumUFbkoHOQWMZvajPvruweu0GK6du8OQePWGr4sq-1pFYC6ST9Y4VumAZaMmXxJYJK4Qki5J-DPKdCj8TxqHE2bdRU3jnKRh5TezAk9Hdm8Cz4y8lzYayuG4YUV4nDU_v8DWilUp_HhOsu0gcIQSG0hzWmYLC_VzXgCg8Y6q8xFGlXsUPIP5XYI4f-1z_0K_y4Dmx7r6hXGcvTrlNNvyDhnkbIN8U-LZOVK5aCCYoKjzqEgcVBdk_IMmYTBPACFY1SLe4_N6aN56FTrDjy7VO_8AVw-XTBDwtg5RCqJ3AOzoSYlhfg6vylqr09321HwFF3L8V7EQvhsvlAWReCiN7iiu_BUndj68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a75bf31b4.mp4?token=q_f3-FEzSB7JrRoPVcnWEuCPfrLm_zHP0eL68WUBpVMm7SbrC4CioLlvG65M39S4r0VL2KGm4Uu_Hcbd1jIrKGwjNhPyduUhuUPwMf4zpSAk0sXm5tvKXth8l22BYmCsAuFrlA1UDzcYGiYS-NOn-CpRBP1xscqBG4SHIEdIFykIJK6XMI91H3voUmnGLbYGuS1zImW1C6aB3ihBc31i-bdhUK7PvQpyqvDgL4DOF-SrA5y5J69_i9j6gCkdRQ42av1JH6hMHs1UVvRBKl44o62EPQgV_TeQd_Qh7c9l17Wwv2Ze6V-lxlFF9b1q4yuzzO3V1Txuc8kumUFbkoHOQWMZvajPvruweu0GK6du8OQePWGr4sq-1pFYC6ST9Y4VumAZaMmXxJYJK4Qki5J-DPKdCj8TxqHE2bdRU3jnKRh5TezAk9Hdm8Cz4y8lzYayuG4YUV4nDU_v8DWilUp_HhOsu0gcIQSG0hzWmYLC_VzXgCg8Y6q8xFGlXsUPIP5XYI4f-1z_0K_y4Dmx7r6hXGcvTrlNNvyDhnkbIN8U-LZOVK5aCCYoKjzqEgcVBdk_IMmYTBPACFY1SLe4_N6aN56FTrDjy7VO_8AVw-XTBDwtg5RCqJ3AOzoSYlhfg6vylqr09321HwFF3L8V7EQvhsvlAWReCiN7iiu_BUndj68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ مجدداً از شی تشکر کرد: شی در کل ماجرای ایران دخالت نکرد. می‌توانست دخالت کند. می‌توانست یک کشتی نفتی را که توسط ۱۲ ناوشکن احاطه شده بود بفرستد و ببیند آیا می‌تواند راهی برای شکستن محاصره پیدا کند یا خیر.
🔴
اما رئیس‌جمهور شی، از او پرسیدم و گفتم: «واقعاً ممنون می‌شوم اگر دخالت نکنید.» و او عالی بود. دخالت نکرد.
🔴
و فکر می‌کنم اگر شخص دیگری این را می‌گفت، فکر نمی‌کنم کسی حتی از او چنین درخواستی می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/129214" target="_blank">📅 21:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129213">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ
:
ایرانی ها، مردم بسیار باهوشی هستند. آنها نوعی نابغه ابتدایی هستند، اما باهوش هستند.
🔴
آنها اسرائیل را منفجر می کردند.
🔴
اگر من نبودم، امروز اسرائیل وجود نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/129213" target="_blank">📅 21:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129212">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/821720cf8d.mp4?token=gR07FM1ovo0_P_fDNytoJS89FUNXPlC74m7-W4O-nKdUGyijqgH0-LSYo0ZBt5mYIufNxJSxfrM0Qrejf6px9odNuuPY2c4pUv4TMQNPaYRO3-pfm5LdKPDtF6QrsZpJQdz57KDF8IJ66pPJrE-YVjAVhrO6fFMkZ6wtMWMiWRuQUtvvUZZh_L9lT7Ld6ocSuclFqAHDye4K5z2rnquFDLoRP8ZM-irSEjJEB1NmqWeoJIXQ1Bf3og8QtoV-FSBY3p8qRHEa0iml7wslnuNQmSrjeYTk0hyWIR5NoeE6oLLmGoQtJb8QCzEGIFkaa0L8RzxpTw-zHh4kv6MipT8CYYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/821720cf8d.mp4?token=gR07FM1ovo0_P_fDNytoJS89FUNXPlC74m7-W4O-nKdUGyijqgH0-LSYo0ZBt5mYIufNxJSxfrM0Qrejf6px9odNuuPY2c4pUv4TMQNPaYRO3-pfm5LdKPDtF6QrsZpJQdz57KDF8IJ66pPJrE-YVjAVhrO6fFMkZ6wtMWMiWRuQUtvvUZZh_L9lT7Ld6ocSuclFqAHDye4K5z2rnquFDLoRP8ZM-irSEjJEB1NmqWeoJIXQ1Bf3og8QtoV-FSBY3p8qRHEa0iml7wslnuNQmSrjeYTk0hyWIR5NoeE6oLLmGoQtJb8QCzEGIFkaa0L8RzxpTw-zHh4kv6MipT8CYYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مودی: مودی بسیار خوب است. او از جنگ‌ها دوری می‌کند که هوشمندانه است. ۱.۵ میلیارد جمعیت دارند. هند در واقع بزرگترین است. مودی رهبر بزرگی است و ما تجارت زیادی با آن‌ها داریم، اما اکنون تجارت عادلانه انجام می‌دهیم.
🔴
آن‌ها قبلاً واقعاً ما را کلاهبرداری می‌کردند. من آن‌ها را به خاطر این مورد سرزنش نمی‌کنم. ما سیاستمداران احمقی داشتیم که اجازه دادند این اتفاق بیفتد.
🔴
اما اکنون تجارت زیادی انجام می‌دهیم. آن‌ها از این موضوع آن‌قدرها خوشحال نیستند. آن‌ها قبلاً خیلی بهتر عمل می‌کردند. اما مودی عالی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129212" target="_blank">📅 21:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129211">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سلام، نخست وزیر لبنان: ایران زور اتش بس آوردن برای لبنان را ندارد. این امر فقط توسط دولت و با خلع سلاح حزب الله محقق می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129211" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129210">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4536cbb7a0.mp4?token=FLd3oETJBfy6kmqcj6mC88CYbb-VSp0Q00N4xSKLkhKHJEkLEl3994IA1DZ2nDSgK3D7YXfS5N-Jz5UzhbRi3MnUciVxk6tBKu5cmfC2eRBr0-cK9w9BK9HKHeWzLnQ965sxpFRdeqiOx9PmvX078G7sCAWAqV507VMyzCpRZhRbEdFcCNpVlePUbgsocIxg1Y__irF9A8a3gA51dPs73-d2EdzV6ie80yiGMZlpVffsnbQFF8mEZBM1MZgOrCeJhpbMX87etg5vpdqcgLWgFavAYdfKZgAu3VWAYxgIHRyUco6IQuEIR3va76p-WiBx5f-Ei2voFBiXMFEz2IPeQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4536cbb7a0.mp4?token=FLd3oETJBfy6kmqcj6mC88CYbb-VSp0Q00N4xSKLkhKHJEkLEl3994IA1DZ2nDSgK3D7YXfS5N-Jz5UzhbRi3MnUciVxk6tBKu5cmfC2eRBr0-cK9w9BK9HKHeWzLnQ965sxpFRdeqiOx9PmvX078G7sCAWAqV507VMyzCpRZhRbEdFcCNpVlePUbgsocIxg1Y__irF9A8a3gA51dPs73-d2EdzV6ie80yiGMZlpVffsnbQFF8mEZBM1MZgOrCeJhpbMX87etg5vpdqcgLWgFavAYdfKZgAu3VWAYxgIHRyUco6IQuEIR3va76p-WiBx5f-Ei2voFBiXMFEz2IPeQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس در مورد توافق ایران:
منتقدانی از این توافق بودند که می‌گفتند ایرانی‌ها هرگز اجازه نمی‌دهند تنگه‌ها بدون عوارض باز باشند.
🔴
در دو روز گذشته، ایرانی‌ها به هیچ کشتی شلیک نکرده‌اند.
🔴
دیروز، ما از تنگه هرمز نفت بیشتری نسبت به هر زمان دیگری از آغاز درگیری خارج کردیم. و حتی یکی از این کشتی‌ها عوارض پرداخت نکرد.
🔴
بنابراین، منتقدان این توافق در مورد برخی از آنچه می‌گویند ایرانی‌ها به دست آورده‌اند، و همچنین در مورد آنچه ایالات متحده به دست آورده است، اشتباه می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129210" target="_blank">📅 21:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اوباما در مورد توافق: توافقی در حال اجرا بود که در آن ایران توافق کرده بود که سلاح‌های هسته‌ای توسعه ندهد.
🔴
این دولت — یا نسخه‌ای قبلی از این دولت — از آن خارج شد، که باعث شد ایران در آن زمان ظرفیت هسته‌ای بیشتری توسعه دهد.
🔴
ما اکنون جنگیده‌ایم، میلیاردها و میلیاردها دلار هزینه کرده‌ایم، فشار عظیمی بر ارتش خود وارد کرده‌ایم، بسیاری از مردم کشته شده‌اند و به نظر می‌رسد که به جایی که قبل از شروع جنگ بودیم بازگشته‌ایم، شاید حتی کمی بدتر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/129209" target="_blank">📅 21:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e467c88758.mp4?token=IG3asSTBZbeoibjv4-rmJblSTBv0Duevd3Yr3II09bEZ1yI9PzZgXTy7IKVs0tC0i2Wut17VCJn7X96IpPWg9eROXT30BHjjrhJoJhte_kIomN6Rm2ktgKjwNqvxF4kYHJfQowF5RgupU4o_4y2ICiMggXHDg-c69_YbWmmjF5j1nN0RB4wMoeB3q5NwXG9NQH4FajlKSgV7oBdC1Y4JGv4S9_z3HkO4pM1wpn5Gs-QKI9_khgoMTs1mKLIfVT61v5INmR7XQV4iQ9ckCBg2Iufe9rhJzYmtQPKYOm3zuZr_dA5_RtY1VHkLbnenBCihd41Yenjl2IELwLRQEdcrMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e467c88758.mp4?token=IG3asSTBZbeoibjv4-rmJblSTBv0Duevd3Yr3II09bEZ1yI9PzZgXTy7IKVs0tC0i2Wut17VCJn7X96IpPWg9eROXT30BHjjrhJoJhte_kIomN6Rm2ktgKjwNqvxF4kYHJfQowF5RgupU4o_4y2ICiMggXHDg-c69_YbWmmjF5j1nN0RB4wMoeB3q5NwXG9NQH4FajlKSgV7oBdC1Y4JGv4S9_z3HkO4pM1wpn5Gs-QKI9_khgoMTs1mKLIfVT61v5INmR7XQV4iQ9ckCBg2Iufe9rhJzYmtQPKYOm3zuZr_dA5_RtY1VHkLbnenBCihd41Yenjl2IELwLRQEdcrMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس : باز شدن تنگه هرمز دلیل این است که قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار امروز کاهش یافت.
🔴
و همچنین دلیل این است که قیمت بنزین، همان‌طور که صحبت می‌کنیم، برای اولین بار از مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، زیر ۴ دلار است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/129208" target="_blank">📅 21:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129207">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
دبیر سرویس امنیت ملی اکسیوس:
یک دستاورد آشکار ایران در جنگ و مذاکرات این بود که بار مسئولیت مهار فعالیت‌های نظامی اسرائیل در منطقه را بر دوش ترامپ انداخت؛ این خود به روابط آمریکا و اسرائیل آسیب زده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/129207" target="_blank">📅 21:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129206">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
جی‌دی ونس: ایده اینکه اماراتی‌ها قرار است یک میلیارد دلار سرمایه‌گذاری کنند تا یک نیروگاه در ایران بسازند اگر ایرانی‌ها رفتارشان را تغییر نداده باشند، کاملاً مضحک است
🔴
آنها این کار را نخواهند کرد. ما اجازه نخواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/129206" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129205">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65e2d930f.mp4?token=fa5Wm2wslQIsbBjbKVWpeBG_U0oq5SDzJR4mkhK7K2qpMjLx7w58Yw50yHTP-htK8JE7_wg-x19qIrGq4xTnh1IuH4Q6KHSRT86545_Bmsr8LpK3hNDIm-OcaZ75ZQe80smIT2MPa-LOcU_o7p3lRDIwgRfiokfN3d_wUrGmIsHwOGGWMiEaR5Juc8eI4Iq1iaM5ZUSLzHTCNsBQmzyiYkLg-EEkI4R7Mri04QR6YY9viETRti7Cvz2jWMg0Rg_0VWpEDrRhNNwEUoyLsYx2oOZm37l8zNHenFI6dhCuBogRBxsmCP3LuTnm2UwhzqTnMYxvHLnB2d1PjUgAh0XKogXH2FrK5uUsUSNynqU9eWvTaEY-PlRWA7mMGzbd28C63B0PqVpmygx0HCk63OVnPVR0LnYTxnyMLb5hbf6tE2n7DqW4yMv0J9F1OBBP6GU9GtZ18cuOamNny0hc3J9dxQ4SXxdlRZrNHSK7SfAIZMzcBnqq4O7FXyM9GRpaFCREsGFpZytcoOESmqTuwZKEdc2V19YegLkUBz0rCTStYyeifuWHapx9W0V7hpjT1Po12U8lf_3Nczf9veEbIeVbwYlAkS5MVZfgWulPZS7Mon_YERNxppZpLbW7ESfytO3cHoNkJLqxynFwVFp7SOdsIlsInkmA-z46e4tIJ3sI4mE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65e2d930f.mp4?token=fa5Wm2wslQIsbBjbKVWpeBG_U0oq5SDzJR4mkhK7K2qpMjLx7w58Yw50yHTP-htK8JE7_wg-x19qIrGq4xTnh1IuH4Q6KHSRT86545_Bmsr8LpK3hNDIm-OcaZ75ZQe80smIT2MPa-LOcU_o7p3lRDIwgRfiokfN3d_wUrGmIsHwOGGWMiEaR5Juc8eI4Iq1iaM5ZUSLzHTCNsBQmzyiYkLg-EEkI4R7Mri04QR6YY9viETRti7Cvz2jWMg0Rg_0VWpEDrRhNNwEUoyLsYx2oOZm37l8zNHenFI6dhCuBogRBxsmCP3LuTnm2UwhzqTnMYxvHLnB2d1PjUgAh0XKogXH2FrK5uUsUSNynqU9eWvTaEY-PlRWA7mMGzbd28C63B0PqVpmygx0HCk63OVnPVR0LnYTxnyMLb5hbf6tE2n7DqW4yMv0J9F1OBBP6GU9GtZ18cuOamNny0hc3J9dxQ4SXxdlRZrNHSK7SfAIZMzcBnqq4O7FXyM9GRpaFCREsGFpZytcoOESmqTuwZKEdc2V19YegLkUBz0rCTStYyeifuWHapx9W0V7hpjT1Po12U8lf_3Nczf9veEbIeVbwYlAkS5MVZfgWulPZS7Mon_YERNxppZpLbW7ESfytO3cHoNkJLqxynFwVFp7SOdsIlsInkmA-z46e4tIJ3sI4mE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره تنگه هرمز: آنچه ایالات متحده توانسته با موفقیت انجام دهد – و به همین دلیل است که قیمت‌ها شروع به کاهش کرده‌اند – خارج کردن مقدار زیادی نفت از خلیج فارس با محافظت از کشتی‌هایی بوده است که در حال حرکت بودند.
🔴
در بلندمدت، ما نمی‌خواهیم حضور نظامی داشته باشیم که از تمام این کشتی‌های در حال حرکت محافظت کند.
🔴
ما فقط می‌خواهیم ایرانیان مانند یک کشور عادی رفتار کنند و از شلیک به آن کشتی‌ها دست بردارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129205" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129204">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی گفت: من همیشه با نتانیاهو خوب رفتار کرده‌ام، او فقط باید گاهی اوقات آرام باشد و از عقلش استفاده کند.
🔴
من امروز با طرف اسرائیلی صحبت کردم و از آنها خواستم آتش‌بس با حزب‌الله را تأیید کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129204" target="_blank">📅 21:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129203">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a782c50045.mp4?token=LHKqBH1T7A3JKyc2taUwCxPWoJc2jza08mssVj7hoE7FaV1Fs0rRLupqQIYJz_uAynJOzQhgd5elFLxLkvnivwho1zS3gvvbWrbLsBox4Zg-KoX7kwIFDU5905mSYUeh9TxuOlx3ADEmN4jBhR0rF8fOsuGnm7PkZGnVLmTJoYbpf3Qtth-bONnT9U2HbtnqDEI_mHu7xrb74KMlxlcg1P6kATqGrpygDgnf0EEZI4vyywSllw49GoEIbItpEylEfG8_wGfngALvL5upCJOnbAXdEPOpbvm_6IL_d07x4iiqkGj9dhX3Ssh5JAdPAvISQ2ehsxSbKy96CF8S259DGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a782c50045.mp4?token=LHKqBH1T7A3JKyc2taUwCxPWoJc2jza08mssVj7hoE7FaV1Fs0rRLupqQIYJz_uAynJOzQhgd5elFLxLkvnivwho1zS3gvvbWrbLsBox4Zg-KoX7kwIFDU5905mSYUeh9TxuOlx3ADEmN4jBhR0rF8fOsuGnm7PkZGnVLmTJoYbpf3Qtth-bONnT9U2HbtnqDEI_mHu7xrb74KMlxlcg1P6kATqGrpygDgnf0EEZI4vyywSllw49GoEIbItpEylEfG8_wGfngALvL5upCJOnbAXdEPOpbvm_6IL_d07x4iiqkGj9dhX3Ssh5JAdPAvISQ2ehsxSbKy96CF8S259DGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیشنهاد جی‌دی ونس به تهران: گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، در این صورت شما به طور حرفه‌ای هیچ چیز دریافت نمی‌کنید.
🔴
گزینه ب این است که مانند یک رژیم عادی رفتار کنید، و ایالات متحده در واقع، برای مثال، به قطر یا امارات اجازه خواهد داد اگر این خواسته آن‌ها بود که در کشور شما سرمایه‌گذاری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129203" target="_blank">📅 21:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129202">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaf2cc7fa7.mp4?token=CfDKrBR2qwc6aB6VQonYIJrs1QL9Gr9CUROCQi9Q7ikUv_kZkxFMaRDOVJSXjdlVC4o1P-ivjvcXaDKemHYXdPq0nz1cYEFyZtMKdzK_t6UgxmzEyIQomCu2MyvJfuyb05F05t3H_uiRtHfVT26L9BCHqnJ37M89iPyVaukoCLUV8j3d7d3hQ823P-TxFfJvdq_YuB_dou8wItw2jxyn-zeA_Zk0adLmR3-_EA2hoWOZa0EYtAPsBWWznndvRQpOb1zPgHQvtdhIxOQPMXa6-EUlytdEDXNkB4oYkBKAgp-Jwxpxkxkv4sXZOfpc2VYROMOhyC0t3Dxof95lWimYVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaf2cc7fa7.mp4?token=CfDKrBR2qwc6aB6VQonYIJrs1QL9Gr9CUROCQi9Q7ikUv_kZkxFMaRDOVJSXjdlVC4o1P-ivjvcXaDKemHYXdPq0nz1cYEFyZtMKdzK_t6UgxmzEyIQomCu2MyvJfuyb05F05t3H_uiRtHfVT26L9BCHqnJ37M89iPyVaukoCLUV8j3d7d3hQ823P-TxFfJvdq_YuB_dou8wItw2jxyn-zeA_Zk0adLmR3-_EA2hoWOZa0EYtAPsBWWznndvRQpOb1zPgHQvtdhIxOQPMXa6-EUlytdEDXNkB4oYkBKAgp-Jwxpxkxkv4sXZOfpc2VYROMOhyC0t3Dxof95lWimYVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره اسرائیل: من همواره از تصمیم ترامپ برای پایان دادن به توافق هسته‌ای با ایران دفاع کرده‌ام و اغلب با استدلالی مواجه می‌شوم که می‌گوید: «اسرائیل فکر نمی‌کند این کار خوب است، پس بد است.»
🔴
واکنش من این است: نظرات اسرائیل اهمیت دارند، اما در اصل مستقل هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129202" target="_blank">📅 21:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129201">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a172117b9.mp4?token=Dl8sxOuHKywVLU7IMJUFyX1aKlJXnGCwooYZxLbrXYCnmWzH4M_vI7nqjvX5earBR3LoxDhj3P3x0Rf42WOWc9rcPiKDds20OJBRfX2JU0HsGGjLiHRmfnANyBW1ugadNKWDuiAlL0w5_i9LCHNwidqkFjmMHC7_RdFfjcTjn1onOuKElchQnvotoJM3GobwL_RdrelIvxui0Fklfi1K9tadYLLt9RHBJ_p3bXn6h22oPLv7N0gmYnrhJXV8v8jkBL5LkwYakhrhjZPm_XHNN7-ttADC4ROiE5i2K7udoOkHz6DmoOEqyQuMiwtmKkhl2ThwleuIDSCECM3oL9pWLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a172117b9.mp4?token=Dl8sxOuHKywVLU7IMJUFyX1aKlJXnGCwooYZxLbrXYCnmWzH4M_vI7nqjvX5earBR3LoxDhj3P3x0Rf42WOWc9rcPiKDds20OJBRfX2JU0HsGGjLiHRmfnANyBW1ugadNKWDuiAlL0w5_i9LCHNwidqkFjmMHC7_RdFfjcTjn1onOuKElchQnvotoJM3GobwL_RdrelIvxui0Fklfi1K9tadYLLt9RHBJ_p3bXn6h22oPLv7N0gmYnrhJXV8v8jkBL5LkwYakhrhjZPm_XHNN7-ttADC4ROiE5i2K7udoOkHz6DmoOEqyQuMiwtmKkhl2ThwleuIDSCECM3oL9pWLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره اسرائیل: اسرائیل شریکی خوب است، درست همان‌طور که بریتانیا یا فرانسه شرکای خوبی هستند.
🔴
این به این معنی نیست که همیشه منافع ما همسو خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129201" target="_blank">📅 21:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89d64d2b17.mp4?token=Y8UF5ir-IWXlklirde37Y0uCL90v1PHhX7KwwdlZCxElOfuzuHaXdYro7UjW31KF2YhX8ATbwJdGeo8tbaDw03HWtv2jYnHywEdC8SHtAGINAvNkrwwHUSyopxGFgUHNRpLGIN0YfChssAFgYSsVz-H6JpaP2R0AScX4b1yWxkQqNaI1EKV9XEhW-QVmniF4mUXPFQvOafCRfWmpbgcAEPkCTxnvWR0VpcggweVf8Uk5K1owTK1JO6C9Q8vgdKV0I38_5eormGcyPVZ-meieCLUidX_1geQPe-RWWGDRPS6SZeu5LtlF-H9KzPTBsFEtfWN4qVM81GyJ1FargJ4RvYWlTV_bBcNLDydyeAhhVDhXsCA_JHFQSSPGOryR91zvrwdifsoVasTzLzHqvDgxrhXGABWqTypQ5U0PZzpBKLErVMTp3qkM1i8igUJSuZt68l9bMHZuFFMVA5masQ8xRrlITcD0cd52c9BoDWVapXzGBUGDu1c5lGsTrI1R0bmgR5uqmmPZaePAYwKAAVo8AIz4suR5PLOGs1FjVL4lxjrJIr63h4YEupPORJ9hzDHtFn2SxHB2Q2HAVSuDv0d2tZCqpTARFoW1E3LZd_l_dFpaJ-VQnT1w3wbrqQih2aG0J7HXbUX7cZXyZxUjgMnSCifklIYdh5nWiUBpj7d0u78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89d64d2b17.mp4?token=Y8UF5ir-IWXlklirde37Y0uCL90v1PHhX7KwwdlZCxElOfuzuHaXdYro7UjW31KF2YhX8ATbwJdGeo8tbaDw03HWtv2jYnHywEdC8SHtAGINAvNkrwwHUSyopxGFgUHNRpLGIN0YfChssAFgYSsVz-H6JpaP2R0AScX4b1yWxkQqNaI1EKV9XEhW-QVmniF4mUXPFQvOafCRfWmpbgcAEPkCTxnvWR0VpcggweVf8Uk5K1owTK1JO6C9Q8vgdKV0I38_5eormGcyPVZ-meieCLUidX_1geQPe-RWWGDRPS6SZeu5LtlF-H9KzPTBsFEtfWN4qVM81GyJ1FargJ4RvYWlTV_bBcNLDydyeAhhVDhXsCA_JHFQSSPGOryR91zvrwdifsoVasTzLzHqvDgxrhXGABWqTypQ5U0PZzpBKLErVMTp3qkM1i8igUJSuZt68l9bMHZuFFMVA5masQ8xRrlITcD0cd52c9BoDWVapXzGBUGDu1c5lGsTrI1R0bmgR5uqmmPZaePAYwKAAVo8AIz4suR5PLOGs1FjVL4lxjrJIr63h4YEupPORJ9hzDHtFn2SxHB2Q2HAVSuDv0d2tZCqpTARFoW1E3LZd_l_dFpaJ-VQnT1w3wbrqQih2aG0J7HXbUX7cZXyZxUjgMnSCifklIYdh5nWiUBpj7d0u78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره اسرائیل: چارلی (کرک) بسیار نگران نفوذ اسرائیل در سیاست‌های آمریکایی بود.
🔴
او همچنین از یهودی‌ستیزی بیزار بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129200" target="_blank">📅 21:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129199">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e295b5be.mp4?token=HKBu5AUaNiNtdpNZoddDaeC_vydLXEM01y0jeD7Tan5vQarjp2SbNtaczb_uBqDbKU_teorO_Y3HUH3okWBbNR4eXhzNtSRWIbp1HrwV7jTlTuP6RFGQ2o6m02wursE7tkI4BMsf-M_ku9z0xO-XlA6yI0-9UMgZyQtD3A7O8kDzhoWPhkyku0SpSruF6ycfco5Nl34hMuxxjPiQKyPQQpygRE8Z_8_HpsO0RAUkXQnp2jn-XYpCtjr1ZOq8oulBJynPng3DaZ81xHdmGQil_Xv2kyHmLdoOKS-0MGO9RPWCM-QkEzHT1jdAeOTD4Kzp3d4u0k4NloBBpw55MqlqYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e295b5be.mp4?token=HKBu5AUaNiNtdpNZoddDaeC_vydLXEM01y0jeD7Tan5vQarjp2SbNtaczb_uBqDbKU_teorO_Y3HUH3okWBbNR4eXhzNtSRWIbp1HrwV7jTlTuP6RFGQ2o6m02wursE7tkI4BMsf-M_ku9z0xO-XlA6yI0-9UMgZyQtD3A7O8kDzhoWPhkyku0SpSruF6ycfco5Nl34hMuxxjPiQKyPQQpygRE8Z_8_HpsO0RAUkXQnp2jn-XYpCtjr1ZOq8oulBJynPng3DaZ81xHdmGQil_Xv2kyHmLdoOKS-0MGO9RPWCM-QkEzHT1jdAeOTD4Kzp3d4u0k4NloBBpw55MqlqYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره اسرائیل
:
اسرائیل، مانند بسیاری از کشورهای دیگر، سعی در تأثیرگذاری بر سیاست‌های آمریکا دارد. من این را به عنوان یک واقعیت پذیرفته‌شده می‌دانم.
🔴
رهبران آمریکایی باید بسیار محتاط باشند که وقتی کاری را دنبال می‌کنند، این کار را در بهترین منافع آمریکا انجام دهند، نه در منافع هیچ کشور دیگری.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129199" target="_blank">📅 20:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129198">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc375717ed.mp4?token=oYqIdPa_yDsYw711aevhXpA2Z59VZGZtol_UOI27atNa8U7WgnA7yanMF7si_9nMqYN4B_jyxWg3iDoxHd2G3ahE1wo8pN8PdIUaI8sFkuvRbvR0WEtUtbHk20IYoB5S9-xzSBCBLvvVFzs3recjVmjzbcEs5sEdRcGhcufxx6S1MpnivZj9FE7HaVHhIzkuWR0MytjQGNa86SfokA2AUhZ1JVDQmYg2x95ikROokxYwf19RBL41q94enkCCyjaE2UVtCdhJKZesZXu1fOLA_LDHkBoDQ7czDdE35lpES0C-n5i8_K862BtvHXu-_eYlFUVWQKFricDcfTOAOKKtAL0gZmDdXnS_9wAAmNnjrfP_3G4uYtlmty_XIq8MXG-7eid2IBZuvQsyL4fqipbuhNUjP7z0QLURJL5P-b2YzynOpNUvyhP96HeJnjsXW9rSL330DvlMHmX0OlvIl6EFWTR5uhNz6AhvCwCC5Lq2fL-si--DR_ppvlNBm5eh5oDfmzfO0-mwCdnX0UjlFhC_Kdi76VuZt3f8-4zdUUGhQG9dzZyiHuTucd_j-51uJeB8OuiOp3HFj2cTOEnlZXqIDKtMmnuEb5H5DjgkDoTaQKioL-RHLYJTc2e9C1OytPs8cq0nSkW0gM6eHiQjDeFTg6WrdFksjduoyIAcmFxUb2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc375717ed.mp4?token=oYqIdPa_yDsYw711aevhXpA2Z59VZGZtol_UOI27atNa8U7WgnA7yanMF7si_9nMqYN4B_jyxWg3iDoxHd2G3ahE1wo8pN8PdIUaI8sFkuvRbvR0WEtUtbHk20IYoB5S9-xzSBCBLvvVFzs3recjVmjzbcEs5sEdRcGhcufxx6S1MpnivZj9FE7HaVHhIzkuWR0MytjQGNa86SfokA2AUhZ1JVDQmYg2x95ikROokxYwf19RBL41q94enkCCyjaE2UVtCdhJKZesZXu1fOLA_LDHkBoDQ7czDdE35lpES0C-n5i8_K862BtvHXu-_eYlFUVWQKFricDcfTOAOKKtAL0gZmDdXnS_9wAAmNnjrfP_3G4uYtlmty_XIq8MXG-7eid2IBZuvQsyL4fqipbuhNUjP7z0QLURJL5P-b2YzynOpNUvyhP96HeJnjsXW9rSL330DvlMHmX0OlvIl6EFWTR5uhNz6AhvCwCC5Lq2fL-si--DR_ppvlNBm5eh5oDfmzfO0-mwCdnX0UjlFhC_Kdi76VuZt3f8-4zdUUGhQG9dzZyiHuTucd_j-51uJeB8OuiOp3HFj2cTOEnlZXqIDKtMmnuEb5H5DjgkDoTaQKioL-RHLYJTc2e9C1OytPs8cq0nSkW0gM6eHiQjDeFTg6WrdFksjduoyIAcmFxUb2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: اگر همه چیز کینه‌ورزی به یهودیان باشد، پس هیچ چیز کینه‌ورزی به یهودیان نیست.
🔴
من واقعاً فکر می‌کنم کینه‌ورزی به یهودیان بسیار بد است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129198" target="_blank">📅 20:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129197">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFA4yPTiuVfjsqp3XViZTtn_UAZlFRhNSdv7xF9yuiu3gESVVqkbSQcA-4ahBvocL-TWyBoODMabdDMhCDcKKd6IT2DdG9GgoGXC80w67wgeyKmdvei9vYVstKYTdA0KLdT3eNs0N3zRiBP7po1o5uoW43VfG2Lxnct85z3LWzytg0L89hFNK_jK-uOwufR9Iy9bFNfrCig2EoUOOLtnP8-yivZElgPGImSft469YHMCNGFYdzf5SYXteQAgpDnYZSVYXU4KK-a_eCNchuQoiippfwaCUhZtjhnKn1AjD6PEVVGujLY8un0GEyzh6VBRMSZRxDgGDCDZd4TUNiPR5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه اسرائیل هیوم به ترامپ: می‌توانستی بزرگترین رئیس جمهور تاریخ آمریکا باشی اما رفوزه شدی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129197" target="_blank">📅 20:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129196">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
تماس تلفنی ترامپ و نتانیاهو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129196" target="_blank">📅 20:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129195">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
شبکه NBC: در تماس تلفنی میان ترامپ و نتانیاهو، ترامپ بر توقف حملات اسرائیل به لبنان تاکید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129195" target="_blank">📅 20:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129193">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ان‌بی‌سی: ترامپ اوایل امروز با اسرائیل صحبت کرد و از مقامات اسرائیلی خواست که آتش‌بس با حزب‌الله را بپذیرند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129193" target="_blank">📅 20:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129192">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
حمله پهپادی نیروی هوایی اسرائیل علیه یک موتورسیکلت (حزب الله) در حال عبور از جاده‌ای بین زبدین و حروف، غرب النبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129192" target="_blank">📅 20:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129189">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjiOVd7IXlSyjVTPOd4yp8X0CwQj7M6O31L3wpYNSwCnN5J6Piy2xCiQYSnOmMg6IjFWzePRDJwVb2NtvaofvcA1fEJXTJHfjC6qXmzv_mRD4ZvA4wziHFVViUuaMZnj9Q_ajQeXuIEuSg0EoGUysC3Qw7RvZybdABrp9wwPFieW5QFxb51nm94d7FjD_p4TdKn5iizSmKD6PnmIX9ro1_xLhyN3Bf9F3o9YHbpURN6lz5zdXAfPyebAKOrNRjoEvQCcBOII6YhbmidkKlpoqwFA4fNM1P9B6kdyoygw8hpQBRyR2ZUFo40ASH1uuvjHHmvm9qKWdQfU4Bhls2aZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3lEbRviw3I8_k9Xw7FHmI51lEpZIfnaMqXwaZnWKWGXydza2_AaqZEe9S6vkCbYdBpdPVaS_LIo6IYHXDfivY3V8G5mZhit6joWiU475RXqboSATyBioEXl7rhnI7cyFuodO0KvQEIpfP8km5xEUqBCotCMnzTKbbKQEwNdgzyG_mPLujqmrJXMEAwyIhFXewsZeddBHQ_c1PPYHAi-1RQdLp6rmaAv1U4EpS8Hco-AnZfCGhc7Ar6r8pwELf3vPZ_8XFErz5gmfbHVPciUOM2YD6r27X_274Tj1bzlFRHgNOwzXci7FPmSvtEqTIlrljxvDcouxsg69SNFGU-HbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOC63WLTWU91jg82YPSonRK2n9OAF9bvmO_qWrVyC0LwMzhPwGw1uCxhseyitcUOHEpyU4Nn1twCCcYB2JFduwf0-tqpMMvnkk9WkT6PY8_HrGa4_qkerdD7ThTsjOQh1uPehGaWIJI8bQ_3BhamklFiXkrJIe3dBFA6irceH-SOUS1xc-kxLsrOx8MbgvY20XbC2D_O4xL6jmiI8jeBt5fwjCveSgjg0mvYL5QocyLmv3ydDOc6-SNkOVNAgx98CFKzHZuH2RAKmZ3eF5u82bab4XyMJneLwBkVkhN0hisXHmmCQxhuvJGRb34-LxDZ4qBmfosNXiNNsR4bF07O1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
موج توئیتری راه افتاده که نامه دیروز مجتبی رو خودش ننوشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129189" target="_blank">📅 20:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129188">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزارت خارجه روسیه: با تثبیت اوضاع غرب آسیا، توصیه قبلی برای خودداری از سفر به کشورهای عرب حاشیه خلیج فارس لغو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129188" target="_blank">📅 20:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129187">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a855bb7c.webm?token=EHEpyTzvGM5VW9GFizp9itoKySq4LAtcGg7lMdUIUagiEIPt3ex7J3biNta2u7K5TTWRLx-Z4PIT8s0fA8_pce3XZUwMnWov_vCiO6mGaj06jrhzJTPL-nQr6fre6S-_AUvxCabbBWOrB6hm0jXYBf7FFPZPi9ZcuxyqQwv6-y_hnP34WWRFHB64Yfb5q2spPcQUFY0epWKI9-NteMCs5syfHFpY0_Qak70HMaGgBCS-_qgNjBtwQHi8c7hkC1XgyyTs067x-snX6ydzyWsAU6tt86EMC2uotqAg7QjFVosylEsrX_y6pg5BUClX6r2-gP-COSAT939jo_VqYUGebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a855bb7c.webm?token=EHEpyTzvGM5VW9GFizp9itoKySq4LAtcGg7lMdUIUagiEIPt3ex7J3biNta2u7K5TTWRLx-Z4PIT8s0fA8_pce3XZUwMnWov_vCiO6mGaj06jrhzJTPL-nQr6fre6S-_AUvxCabbBWOrB6hm0jXYBf7FFPZPi9ZcuxyqQwv6-y_hnP34WWRFHB64Yfb5q2spPcQUFY0epWKI9-NteMCs5syfHFpY0_Qak70HMaGgBCS-_qgNjBtwQHi8c7hkC1XgyyTs067x-snX6ydzyWsAU6tt86EMC2uotqAg7QjFVosylEsrX_y6pg5BUClX6r2-gP-COSAT939jo_VqYUGebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/رهبر حزب الله، نعیم قاسم با آتش بس با اسرائیل مخالفت کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129187" target="_blank">📅 20:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129186">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/رهبر حزب الله، نعیم قاسم با آتش بس با اسرائیل مخالفت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129186" target="_blank">📅 20:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129185">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
خطیب‌زاده به الجزیره گفت: بدون پایان دادن به اشغالگری و پایبندی اسرائیل به قوانین بین‌المللی، صلح و ثباتی در لبنان و منطقه برقرار نخواهد شد.
🔴
«هرگونه توافق آتی باید شامل آزادسازی تمام دارایی‌های مسدود شده ایران باشد.»
🔴
«ما پس از ۶۰ روز سازوکار جدیدی برای مدیریت تنگه هرمز اتخاذ خواهیم کرد و ابتکار ویژه‌ای را به کشورهای منطقه ارائه خواهیم داد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129185" target="_blank">📅 20:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129184">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEGmYx_3xuOVFgPAHGPlaqrN-AFiDXlIbO3enGr613yCFFoZQ7K2hGKHEa6DcfNFTFDxbkPo8BGgh8O_PkM-Hr1AwFkjTJBvPuLb5tqBxf-0n83D8lhcSOgkgl165W0GBQiwzTfOA4w6X1TJHE7Cg4_wJO1F4uszida9OGX4gAsEWtN0UJ-8zNmdKGOZ50iFW5eFe-osm7k-MTFEvnnwg8xB1F1yk_szVSe4aKUu1QiyubZ5vZex7-yq01NwvwGaH2FWvaE17x29Zy0q_Ko3HLzaxrY4zMBkHCMXZIRi47bIMmb54Fi-UN3zgV8W9ggpqOVf6eLIC3eWnGQj6EjTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: یک هواپیمای ایر فورس دو سوخت‌گیری شده در فرودگاه مریلند روی باند فرودگاه بود. میزها در یک تفرجگاه مجلل سوئیس چیده شده بودند. تدارکات آماده بود. مطبوعات در راه بودند.
🔴
اما مذاکرات هسته‌ای مورد انتظار بین ایالات متحده و ایران روز جمعه برگزار نشد، که یک شکست زودهنگام برای مرحله بعدی مذاکرات هسته‌ای بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129184" target="_blank">📅 20:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129183">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ولادمیر زلنسکی: من به لوکاشنکو یک هفته مهلت می‌دهم تا تجهیزات نظامی را از مرز اوکراین که برای تنظیم آتش توپخانه علیه جمعیت اوکراینی استفاده می‌شود، پس بگیرد.
🔴
در غیر این صورت، ما خودمان این کار را انجام خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129183" target="_blank">📅 20:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129182">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg5b_hoC-o8M6MdZfk9VSZY9fLGDqIPQ38HmFOKeur01_fSB0rIPRFz9GG8YPoPZn_VX5N94STuzOnc5CC5D9eb-Hrx9VMAlGPQYKMTAAHmenmAL-h7BKyYHjChZf8uwhzrubzUU5ZADZ_6YvDx56PQbkOfAEBV2fjMgl9YslQ8q0OybCd6tpdYOmSTer5-wgVCE8J9h_jwG4j1kLkXJwrYRpNe4h57p7vKVCpFo-XujzEP3ep9XvpQYdtafVbzz3j-lLD3jPgglkm24pmHmGRqdlZ3HUfyqNPbWq-BnkMH7nbvmgea9x4cPrzzS1pgB--LsmgfoqLKEznmwotw4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیر استارمر، نخست‌وزیر بریتانیا، پس از افزایش درخواست‌ها از سوی وزرای کابینه و نمایندگان حزب کارگر برای کناره‌گیری، در حال بررسی آینده خود است، طبق گزارش تایمز.
🔴
استارمر فشارهای فزاینده را درک می‌کند و انتظار می‌رود در طول آخر هفته با همسر و خانواده‌اش گزینه‌های خود را بررسی کند و سپس تصمیم بگیرد که در سمت خود باقی بماند یا استعفا دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129182" target="_blank">📅 19:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129181">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: تماس بین نتانیاهو و روبیو، وزیر خارجه، به زودی، درباره لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129181" target="_blank">📅 19:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129180">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667c0e662b.mp4?token=e9XJmvLNqip2uitPNmQwpP6OHxEKelj5TL-1KOnYo2efqVxBqpQ4bSKD8s8VSZj2KqLockU0RK2s8elv2q5REX283CUIFvgq0gc-Tfd0c5bYoLZ6e3whd5u2wchFuxFdl0cfn0_TZopxZq-Lws_nKgnja9u_ILSjQEZW1vCVHpEDCDuIDBtq5m8Kgh2FWH6dEa2kqPRsPpwgacIc-ADHbh6Rf_ADezJSvEUEwb9DO-WUQLJDQYVRrQpmPfI4KbAX-aONW9Pe9nEl_wvizpPvihQLHCLFGpDpaZar0YAYC2NwNr6D8IY0dUSpRgjrfUIcXV0j7nOVHaR5pJOhD24gsEw4rNCczSELlPrTS_cH9FqFoZNxbrtWlOJuhqHLMyRh1hhw8KVWEMm2hVUv04Vh4SxDlNhj070gBbnP29jMgguSlKez2Z3U_7ZztlG3VRxUWOGc49LqzxxBnksd1PMrqvbJQECkDoToqV4kjHCMynhB88Q6aubzVl__TjKPzUWt6MevXbhFbNZYSgCxwBDi2vCEHohbX4b5GXUp5Be4NFDcOTrjmk-LCu4-zCEZnPl5z2lP-sfpEl90RkbzPmB76tGe28Vsp7Kt_4gUfYBKZvDSwHu8fhCPzH2DFQsEjAozmSxq1DVYkz5yLs1s8lkrZDhhCJTP35iAG3GF7wqzuzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667c0e662b.mp4?token=e9XJmvLNqip2uitPNmQwpP6OHxEKelj5TL-1KOnYo2efqVxBqpQ4bSKD8s8VSZj2KqLockU0RK2s8elv2q5REX283CUIFvgq0gc-Tfd0c5bYoLZ6e3whd5u2wchFuxFdl0cfn0_TZopxZq-Lws_nKgnja9u_ILSjQEZW1vCVHpEDCDuIDBtq5m8Kgh2FWH6dEa2kqPRsPpwgacIc-ADHbh6Rf_ADezJSvEUEwb9DO-WUQLJDQYVRrQpmPfI4KbAX-aONW9Pe9nEl_wvizpPvihQLHCLFGpDpaZar0YAYC2NwNr6D8IY0dUSpRgjrfUIcXV0j7nOVHaR5pJOhD24gsEw4rNCczSELlPrTS_cH9FqFoZNxbrtWlOJuhqHLMyRh1hhw8KVWEMm2hVUv04Vh4SxDlNhj070gBbnP29jMgguSlKez2Z3U_7ZztlG3VRxUWOGc49LqzxxBnksd1PMrqvbJQECkDoToqV4kjHCMynhB88Q6aubzVl__TjKPzUWt6MevXbhFbNZYSgCxwBDi2vCEHohbX4b5GXUp5Be4NFDcOTrjmk-LCu4-zCEZnPl5z2lP-sfpEl90RkbzPmB76tGe28Vsp7Kt_4gUfYBKZvDSwHu8fhCPzH2DFQsEjAozmSxq1DVYkz5yLs1s8lkrZDhhCJTP35iAG3GF7wqzuzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: آنچه در هر جامعه‌ای جشن می‌گیریم، بازتابی از ارزش‌های ماست و ما زمان زیادی را صرف کلیک‌بیت و خشم‌بیت در مورد فرهنگ سلبریتی‌ها و شایعات می‌کنیم و زمان کافی را به محتوای واقعی اختصاص نمی‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129180" target="_blank">📅 19:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129179">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
نعیم قاسم، دبیرکل حزب‌الله : تلاش برای حذف حزب‌الله شکست خورده و اسرائیل بالاخره مجبور میشه از هر وجب خاکمون عقب‌نشینی کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129179" target="_blank">📅 19:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129178">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18a311e35a.mp4?token=CyhuTtm6QAPOQ7gZDYfPq-Fov12IaD4QIPbk8OOTPzH3uKBoQhDLogOhOGkiO4w5g5hWcZPw5PqsPuhg9RJYv8wLNafbSTMTwT2_mLoO7W86oHIAEtsbUAixtsxJHAUhChi5l4y6WD3DuNzcgvSTBc3wr6Z9wj6xtbkuFdFyR1lyl_LyHCFluYoRsUdPfV_9b-ixHkvzwEH39I7uPNGe1ETtKdCmct1sBK-nE1u9EmsvwRbDN22zU8i20iwTpb9avsA3WAq6pt-shfgKr301VoXCHELgk2afxH0JQK474CfJphf5Mwdvi1qlUL0C848qzlYpSNj_ZmWbVpdQqTuUTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18a311e35a.mp4?token=CyhuTtm6QAPOQ7gZDYfPq-Fov12IaD4QIPbk8OOTPzH3uKBoQhDLogOhOGkiO4w5g5hWcZPw5PqsPuhg9RJYv8wLNafbSTMTwT2_mLoO7W86oHIAEtsbUAixtsxJHAUhChi5l4y6WD3DuNzcgvSTBc3wr6Z9wj6xtbkuFdFyR1lyl_LyHCFluYoRsUdPfV_9b-ixHkvzwEH39I7uPNGe1ETtKdCmct1sBK-nE1u9EmsvwRbDN22zU8i20iwTpb9avsA3WAq6pt-shfgKr301VoXCHELgk2afxH0JQK474CfJphf5Mwdvi1qlUL0C848qzlYpSNj_ZmWbVpdQqTuUTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: از نگاه بین الملل در ۴۰ سال گذشته یک روز نبوده که ایران بدنبال ساخت بمب اتم نبوده باشد
🔴
اگر ایران به سمت بمب اتم حرکت کند همین چین روبروی ایران خواهد ایستاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129178" target="_blank">📅 19:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129177">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy76vKiZ7rCdzArQwftsCVYZyKKq7BnXTGVQxZsO-uXw9lKQs7_Pzz8TouTb-QieSiKSihyz5z4PtoS1t3XDMK88SSf0loNbZwH5MFMhYr20Lsd2B9Ri4i_jRJufaQ0sqooyJVtV9kIL8fyjK5JV5ORWRsxfinyn8Bvf_dnZP3kDTYqQlsyoTRdvRcrHyFjglCZFKk1gxhUD0_zTec22Xs-T7r--cF3ZGpOd0fgYTcT00Na0_aGS8U14RoCLby-TvGfmWFWTIBS8AvY7pvxtLLO7SoDzWd6y5dsRbJXa8IiiIb48VR7-DzvueOnJEK6fyFVblFzkFNFAgvAMuhcBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور هیات قطری در سوییس بدون حضور ایران و آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129177" target="_blank">📅 19:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129176">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
واشنگتن پست: سازمان اطلاعات آمریکا اعلام کرده که اسرائیل به طور فعال در تلاش است تا یادداشت تفاهم ایران و آمریکا را بر هم بزند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129176" target="_blank">📅 19:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129175">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری / هلند: برای تضمین آزادی کشتیرانی ناو جنگی به تنگه هرمز اعزام خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129175" target="_blank">📅 19:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129174">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
امانوئل مکرون: برای مشارکت در اجرای توافق بین آمریکا و ایران آمادگی داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129174" target="_blank">📅 19:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129173">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نتانیاهو: حزب الله بهای سنگینی پرداخت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129173" target="_blank">📅 19:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129172">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سنتکام: بیش از ۲۰ کشتی روز گذشته با امنیت از مسیر تعیین‌شده در تنگه هرمز عبور کردند
🔴
از کشتی‌ها می‌خواهیم دستورالعمل‌های مرکز اطلاعات دریایی مشترک را رعایت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129172" target="_blank">📅 19:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129171">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سی‌بی‌اس: ۴ کشورمیانجی تفاهم ایران و آمریکا یکشنبه آینده در مصر نشست برگزار می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129171" target="_blank">📅 19:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129170">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
گفتگوی قطر و سوئیس درباره حمایت از مذاکرات واشنگتن و تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129170" target="_blank">📅 19:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129169">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت امور خارجه ایران: عراقچی به همتای پاکستانی خود در مورد پیامدهای هرگونه نقض تعهدات یادداشت تفاهم هشدار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129169" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129168">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
بلومبرگ گزارش داد که ۱۱ نفتکش حامل مجموعاً ۲۰ میلیون بشکه نفت ایران این هفته بندر چابهار را ترک کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129168" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129167">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فدراسیون فوتبال ایران بابت رد درخواست ورود به آمریکا ۲ روز قبل از بازی با بلژیک به فیفا شکایت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129167" target="_blank">📅 18:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129166">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
مالک شریعتی نماینده تهران: ظاهرا همراه با پیشنهاد جمع‌بندی شده‌ی شعام درباره متن ۱۴ بندی تفاهم‌نامه،
یک متن تفسیری ۶ بندی نیز درباره اقداماتِ طراحی شده‌ی ایران، متناسب و متناظر با بدعهدی‌های احتمالی آمریکا، از سوی رییس‌جمهور محترم برای رهبر حکیم انقلاب ارسال و اجرای آنها تعهد شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129166" target="_blank">📅 18:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129165">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی آمریکا:
جنگنده‌های اف-۱۶ به گشت‌زنی‌های خود در خاورمیانه ادامه می‌دهند و آماده مداخله هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129165" target="_blank">📅 18:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PEe4SfTK3Y0uI72835emKnoHXE3blDw1aMLtosm08shMnkwP-WVciD-Q-Tbuie3-s_ufPpE05y_CJfrH_bAZi0wcf_jZShewzGuIEErdp-fnUVcGhmtnO2PIHDLPjetac0NEKaGbwElnyz8fB0ikvAzz3Kcww4aur7OuFYX3bopHS5Naa7QqXuUVx4-_-FqqpW-33Yx_S8PmesTOA-8oEcLU52eat9E2at1Y84foNzGCflyEnOVtqpn8LH9RLdTI07b41iodlzdI6zFS6O8T6ohdvw4paqVpa4qZb32DAmhaGZ277lb6AkLRFmd1Di_GX7pUn2etoZ69EB1V1Q0fEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CoTauB6JAG_YIPr1zKi7lpiqq8ZSR9-vF53aKQ0PCmvFt-DmlErnMqJ7cd_p-9o2c-_2bfHx_1E-YmMGnLkheD4euJoYc4PGj55EvGgVtiaaV5NVLwq_dL4Ter92ilRNZn9_qJPxDvkmQvBWeeOkDSN9HNJlQpAqQAKAeZ4Fhu_A880qjlx-7_MzO6Bwo5bxAqwOLFkEG-LQljQF5InRLmkUQANkCZCiYHcsVRpWdrEqcrrE5SzCpaOrCZ31PWgh6_xyCuGfxs5iYBJAEjvADdpekSXuKBQY90uOiZGqXZ_y9TTO4EEtgcuojLHrDRXndxsYya2qtfiCtYcmpzE_zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5245763015.mp4?token=low_ufZIBVx_v2p0PHfoQU30XLPuTL3nLLJabywtSo6186XwAXm_n10KDhG49j9_hlFi0pa5-zsYUYz8_Gmhh-JHX7QLURlxEWQlk0HXjm8SLAf-jpYbdKFI7yjeNHV59ZH9v54b4sJRCUytRrOJcuuClFcYsMlwticaP4eU9JfpLaBJkOp7BGVa8fvaENRVSl2RbO78LKEQntZaSB5kXudEL63piouZzNnQZDfb6LN6yPlqhDkzqYmw_pv0XIC55kd4M-oBGSEThKWlWLuc13JqaIC2AAwr6omtoLOMGetizbK55fidskoe-o0fksO_iCDHXsVCA1dnxQelwfqYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5245763015.mp4?token=low_ufZIBVx_v2p0PHfoQU30XLPuTL3nLLJabywtSo6186XwAXm_n10KDhG49j9_hlFi0pa5-zsYUYz8_Gmhh-JHX7QLURlxEWQlk0HXjm8SLAf-jpYbdKFI7yjeNHV59ZH9v54b4sJRCUytRrOJcuuClFcYsMlwticaP4eU9JfpLaBJkOp7BGVa8fvaENRVSl2RbO78LKEQntZaSB5kXudEL63piouZzNnQZDfb6LN6yPlqhDkzqYmw_pv0XIC55kd4M-oBGSEThKWlWLuc13JqaIC2AAwr6omtoLOMGetizbK55fidskoe-o0fksO_iCDHXsVCA1dnxQelwfqYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129162" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129161">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXQoYSmZTg54iPvS2HD4SE6UDcUv0c_ww3arVGrECH3_Msab41w5MR6QnAzumgCaiMLcNAMES7w42kswXqGX6V5oDFfO9PZ9Nky_eSPUszqc_6rZpholacCnQ6JDFvttL_QyN2YA4_0wxj4i0YExwLFziAsY8lV3hi4HlpcqwntTpulS0XT2wzU8n4hgV0UA2g7s6ANZ0dxfs6fwnqU6-CHtToW56DL1IB21Wc9WZeASkLzAIW49qEJWIDC9SpLa7HCivjDS0u6GoYFBvY9qEqwBegwZ_N4TnXFc7V6BGnEB1JA4tO2dNPFxWAWCpWSGlI_eS-Zdx2SZAk-jswLyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدمنان رییسی، نماینده مجلس:
خوش‌انصاف‌ها(منظورش قالیباف) مجلس رو باز کنید، رهبرم تنها مونده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129161" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
