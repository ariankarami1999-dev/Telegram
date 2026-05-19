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
<img src="https://cdn4.telesco.pe/file/kj6FYt6MiYv7UqQB4ePZW9H_3yEoLRJgCBIdHqn3kTJs5IFDgp2OHNgxxg5RsFzbx7xy0bA-bU-GMWs90JvYR6OwotU_ikfSgWts4mpDlxjyR_8B_HbcFOpo74MAnpvd90n9iNCKP5HfMmgl281Jlz1_RjZCkqJzdYywyI0roVA4fiA7Vp7Ztf9kP9diPl_jwjk6BtB4QJfN4N5uwtoC81e2WVBnJITraTs02ybrJ662ek-InhaSAo2jPJW_FaWVeuk0uPrX1o6Omb5mVC8Eaw1cjoA7xhqPUhiNFC9Ewy8eDXDAQtLlFQjIKP4Jg--gkjcO40YBQMzgwH9wgi7MEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 948K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 06:57:32</div>
<hr>

<div class="tg-post" id="msg-120990">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPR7LAb2Ochc32sdd4ZIhwBB-QGqmeENumgYpJfux3QRMTX5oKuUl-uqyt40Jo3S2MZq0Jk1lPZV3aFOisimnLGMvICDvPgbYe2So16Ds49NVfQC8ICCGsInebZ09JJUFt8xORRb54uVz6ydxg4IH5v4FTMGvK7sqmxLF5y5bRo4JQ5n5eQpDzsJ1HlVN0SoMhHcgwjFHOU5dcMQOImL2xxb5vy6IJGUpumOQMvp9w1odjktoFKOkyeCjZStXSuT5E77d2YNEvIkOFIgAussLJ9cOlW0KoSTn2txBbxNxDpXnmTphyb1Qbn9PseS4S9DZXa0hj2YNxxg6J4SQLZTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ ظهر فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/120990" target="_blank">📅 01:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120989">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ: اسرائیل را از تصمیم برای به تأخیر انداختن حمله به ایران مطلع کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120989" target="_blank">📅 01:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120988">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ سه روز بعد : بخاطر روی گل افغانستان یه ماه مهلت میدم  [@AloTweet]</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120988" target="_blank">📅 01:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120987">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ: ایران نهایتا ۳روز زمان داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120987" target="_blank">📅 01:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120986">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152da11d16.mp4?token=AB-Mta8RLdl1dfFOHpRcYB_NDiWDMenf38OAqpS6l-AWDcG_RM-n9IDmElZlx8nFfA0Q_yjtWVvLDu75Lb9-VqKbYKDyMwYPVf4U5o5yjWzp1P03c1T5ixz5vfv8HezjLxJNRKQx58DD_dsxaVxW6uNGQ59KFZShkvZQjy_DnvykijBB0efXr8LNMSCwsbw5aih1iPYiL_CTJ6DUqF8UvYda_rGO4ZnTH76fm_8sfHAzykkW9d71vlQKLihmDETefSktI5XAg04eaoLnRNjxXSUlHOy4Ly1fVhLyLM0pzm8qYvy5BnsA7PGqK7RGTrhJTADtDnF3vw68WxhEc-gsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152da11d16.mp4?token=AB-Mta8RLdl1dfFOHpRcYB_NDiWDMenf38OAqpS6l-AWDcG_RM-n9IDmElZlx8nFfA0Q_yjtWVvLDu75Lb9-VqKbYKDyMwYPVf4U5o5yjWzp1P03c1T5ixz5vfv8HezjLxJNRKQx58DD_dsxaVxW6uNGQ59KFZShkvZQjy_DnvykijBB0efXr8LNMSCwsbw5aih1iPYiL_CTJ6DUqF8UvYda_rGO4ZnTH76fm_8sfHAzykkW9d71vlQKLihmDETefSktI5XAg04eaoLnRNjxXSUlHOy4Ly1fVhLyLM0pzm8qYvy5BnsA7PGqK7RGTrhJTADtDnF3vw68WxhEc-gsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ در مورد ایران:
ما به کشوری که قرار بود سلاح هسته ای داشته باشد رفتیم و عملا ارتش آن را نابود کردیم.
🔴
ما میتونیم همین الان بریم و 25 سال طول میکشه تا دوباره بسازن فکر کنم آخرین چیزی که اونا بهش فکر میکنن هسته ایه حالا بايد اينو به صورت کتبي بنويسن
🔴
ما ارتش اونا رو کاملا نابود کرديم ما رهبری اونا رو نابود کردیم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/120986" target="_blank">📅 01:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120985">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ:
ما با محاصره دریایی، دیوار فولادی دور ایران ساخته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120985" target="_blank">📅 01:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120984">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d41fab57.mp4?token=ug7NTT2xzWpCnMQjeaMx0Lj29clt9RlFhTyPesbOcoCf4cfnz9mcGaOBkoR37CCvmwSxJ4T5LGIQftkTj-e1PS9FXjV32_yTu-OIUU-Zuqb548J3H_1_IKZJEbjWVnp2bODKusF1F8uIPZkUS1YhmG5F7MqgIPUgIqz2unh0ds4FGkdi6V4pC0vK3OYFhqf3XlMFm0eS9SpdGyYGJ6tcb9cO5jnsA7p2LWa3LoU3erZlnfofw7Ip-VYDqQv0KoMEBz-EVR7GYkzn9R9Hg92bHEn71sSS5u1enBvDV4UnOh7oigOmzEegZ6uu3Ve9gnSQFHvqiCzJQAZ7dErg9v4JrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d41fab57.mp4?token=ug7NTT2xzWpCnMQjeaMx0Lj29clt9RlFhTyPesbOcoCf4cfnz9mcGaOBkoR37CCvmwSxJ4T5LGIQftkTj-e1PS9FXjV32_yTu-OIUU-Zuqb548J3H_1_IKZJEbjWVnp2bODKusF1F8uIPZkUS1YhmG5F7MqgIPUgIqz2unh0ds4FGkdi6V4pC0vK3OYFhqf3XlMFm0eS9SpdGyYGJ6tcb9cO5jnsA7p2LWa3LoU3erZlnfofw7Ip-VYDqQv0KoMEBz-EVR7GYkzn9R9Hg92bHEn71sSS5u1enBvDV4UnOh7oigOmzEegZ6uu3Ve9gnSQFHvqiCzJQAZ7dErg9v4JrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به زن‌های داخل جمعیت :
- شما خیلی خوشگل و خوب به نظر میاید، شما دوتا، بیاید اینجا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120984" target="_blank">📅 01:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120983">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7b1ceb70f.mp4?token=vSwiPlpIayledo9Qx-qF28YDK0urvjfU_oKBdSfvMG9NMRWZkAtlQEd8d07cRsML_q-MxXRX-c06EUniYIpFOh9r9MOQeoT3HSp60nzNhtCCOF4Q8Zcbbhd24uCZa4--t2QpFx7xC53rrkcHUqlmSw-YgIXR00sEsLd03X9zzaxfOilTROSlqcRfBzt4Jy9d97hDUgw3ttNymdYCyFUFQnLszjnB-9cK8-Rnv-mfh4g-l-UH6o1JoNGd86OXzSDaFKei3X9XZyxXqn7iSus7vTfHhQkqObnxHTX2-awQKiAIPFrSI9FrHQlWSQ1CxSmt1SZMla0jlDoCcXrv449N7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7b1ceb70f.mp4?token=vSwiPlpIayledo9Qx-qF28YDK0urvjfU_oKBdSfvMG9NMRWZkAtlQEd8d07cRsML_q-MxXRX-c06EUniYIpFOh9r9MOQeoT3HSp60nzNhtCCOF4Q8Zcbbhd24uCZa4--t2QpFx7xC53rrkcHUqlmSw-YgIXR00sEsLd03X9zzaxfOilTROSlqcRfBzt4Jy9d97hDUgw3ttNymdYCyFUFQnLszjnB-9cK8-Rnv-mfh4g-l-UH6o1JoNGd86OXzSDaFKei3X9XZyxXqn7iSus7vTfHhQkqObnxHTX2-awQKiAIPFrSI9FrHQlWSQ1CxSmt1SZMla0jlDoCcXrv449N7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ:
ارتش ما بزرگترین ارتش در هر نقطه از جهان است.
🔴
من تازه چین رو ترک کردم و باید بگم که رئیس جمهور شی خیلی خیلی از ارتش ما تعریف کرد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/120983" target="_blank">📅 01:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120982">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/پرزیدنت ترامپ :
ما به جمهوری اسلامی هیچ امتیازی نخواهیم داد. فقط تسلیم کامل!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/120982" target="_blank">📅 01:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120981">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6258c2ef8.mp4?token=U0PXBU8Fa4EE46UYpZ5bCtF9TYuNW1l5Wpj3iesRwAuX_UphbqYqY1y4vsdRMzNaE512jUtIy2LPWWWfEk8T1fKCE8aTogJyZVnNUVY_YGBRy8UM3_3x3iYdSSizTUJHJMPYVhEFyAUBV_ljZsczNLvCkbwYVql1Ta7RlOyYCYqAaDve69-NY8G45t9npSQGv74b7yjaLdoPL3aEeXDAVqtjt3BiOZjFIwCZcDHVaIcESwJ85v11fmDJ2sicaunsnhF5y8-2oQjWuKQqdKoAPpMEyFEUCheH4KelS3GmdeW9VJkv1l14un2BYz2lSthjDpQUTfHmH-6T1nmjn96foQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6258c2ef8.mp4?token=U0PXBU8Fa4EE46UYpZ5bCtF9TYuNW1l5Wpj3iesRwAuX_UphbqYqY1y4vsdRMzNaE512jUtIy2LPWWWfEk8T1fKCE8aTogJyZVnNUVY_YGBRy8UM3_3x3iYdSSizTUJHJMPYVhEFyAUBV_ljZsczNLvCkbwYVql1Ta7RlOyYCYqAaDve69-NY8G45t9npSQGv74b7yjaLdoPL3aEeXDAVqtjt3BiOZjFIwCZcDHVaIcESwJ85v11fmDJ2sicaunsnhF5y8-2oQjWuKQqdKoAPpMEyFEUCheH4KelS3GmdeW9VJkv1l14un2BYz2lSthjDpQUTfHmH-6T1nmjn96foQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
آیا آمریکایی‌ها باید نگران ابولا باشند؟
🔴
پرزيدنت
ترامپ:
من نگران همه چیز هستم. فکر می‌کنم که در حال حاضر به آفریقا محدود شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120981" target="_blank">📅 01:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120980">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: به نظر میرسد شانس خوبی برای رسیدن به توافق با ایران وجود دارد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/120980" target="_blank">📅 01:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120979">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ درباره «گفت‌وگوهای مهم» با ایران:
«این یک تحول بسیار مثبت است، اما خواهیم دید که آیا واقعاً به نتیجه‌ای می‌رسد یا نه.
🔴
دوره‌هایی را داشته‌ایم که فکر می‌کردیم تقریباً به توافق نزدیک شده‌ایم، اما در نهایت موفق نشدیم؛ با این حال، این بار شرایط کمی متفاوت است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120979" target="_blank">📅 01:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120978">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ: اگر بتوانیم توافقی را منعقد کنیم که مانع دستیابی ایران به سلاح هست‌های شود ، از آن راضی خواهیم بود‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120978" target="_blank">📅 01:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120977">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f3ba75465.mp4?token=tflAYOo78SpUrkUMFpYm11wUZhtMQ6qfXcPIRExsnp2iqMTAZ9gSm15DIonz474v-2gl59psDoJGIbCeppv_ZpBd1CSOCQ4N7JOkP0CzLHqhPFS9lpF_qnzu4Jba7plpN0jE6TcoL_KNbhLW0GGLb35aphVJ-64whIh4O4ZQHkZNN16Qp4nqtkwx2cluansiSPxciBKGcB2KeISoR_wGhhbjvNtHNw08SDod4BeRnH4DxgjFlpJRkzBEo3-WR2laAepmCEJvqg4TbeW46aV4dSNEDmBkmhdUTf0-h4oFTT1wQVcc_f2Fvy-S7LZIKCc_jLQCkPkzfF-Ji6lyMx_clg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f3ba75465.mp4?token=tflAYOo78SpUrkUMFpYm11wUZhtMQ6qfXcPIRExsnp2iqMTAZ9gSm15DIonz474v-2gl59psDoJGIbCeppv_ZpBd1CSOCQ4N7JOkP0CzLHqhPFS9lpF_qnzu4Jba7plpN0jE6TcoL_KNbhLW0GGLb35aphVJ-64whIh4O4ZQHkZNN16Qp4nqtkwx2cluansiSPxciBKGcB2KeISoR_wGhhbjvNtHNw08SDod4BeRnH4DxgjFlpJRkzBEo3-WR2laAepmCEJvqg4TbeW46aV4dSNEDmBkmhdUTf0-h4oFTT1wQVcc_f2Fvy-S7LZIKCc_jLQCkPkzfF-Ji6lyMx_clg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
- چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد
-  از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز عقب بندازیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/120977" target="_blank">📅 01:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120976">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26879febf9.mp4?token=rtTPxozp0pBd_ktzfr8rH7ampu_wVXaGBDr06vHZIkWUsRSxrvhPbSPShr_6uu1ZJFHwVz2_XbLfzPK9z--e89neangLDMTelJEKwtzRUJDW9B99e_JnJw-gdoBQYGpfs4blJPRB8MUchFOcqdAI-QX10yg7Fi7OMn-KI-82LcxLOV5SmZB_0tq4QzlM4nBHfyZReJt0a_tk2IDO2xWPL0AqzLeUUVR2X6YpOlpiWizop9D5ur5vlRP47cGL-tl42LQcCuG0BqULyzN_rJuyeTJ_pry5bH9pSv-gtdRXzeWNEYn3saSY7YGm3Dz-thM7xez72m-7qoB7-OeqHzfdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26879febf9.mp4?token=rtTPxozp0pBd_ktzfr8rH7ampu_wVXaGBDr06vHZIkWUsRSxrvhPbSPShr_6uu1ZJFHwVz2_XbLfzPK9z--e89neangLDMTelJEKwtzRUJDW9B99e_JnJw-gdoBQYGpfs4blJPRB8MUchFOcqdAI-QX10yg7Fi7OMn-KI-82LcxLOV5SmZB_0tq4QzlM4nBHfyZReJt0a_tk2IDO2xWPL0AqzLeUUVR2X6YpOlpiWizop9D5ur5vlRP47cGL-tl42LQcCuG0BqULyzN_rJuyeTJ_pry5bH9pSv-gtdRXzeWNEYn3saSY7YGm3Dz-thM7xez72m-7qoB7-OeqHzfdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/120976" target="_blank">📅 01:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120975">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678a888387.mp4?token=HSfJZsdGxMIrcLscdsEvnnilnMsoyuQ6fXx2HBvjOszUji8N-uZ6OPhhGcZj5v7gsd1TDGJgS5pFdl8gXss3lllO7KTQUpaeIvfvYsP3DVeMKwZ2MuXTJNF3i130y5Xk22z-U3Rw6L-ZoiQaLBk5KjV0vI5ypyCFdjqo29tU3ItsfOrwrPQ8JsuP8y65pGX6tiDg9Qc807IKnleV8LNktgGOHkQU1Vymw8tk4hJwLJExIxKoVGy7vWJZX4UiNYx7xuEfT9_E8cafFD196frhHGYVveuzpnk51YIkWmH-H9sHC0tBB4bhFFnrlrsgVz2EC_v7AjTwwj5n_4wLx8iang" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678a888387.mp4?token=HSfJZsdGxMIrcLscdsEvnnilnMsoyuQ6fXx2HBvjOszUji8N-uZ6OPhhGcZj5v7gsd1TDGJgS5pFdl8gXss3lllO7KTQUpaeIvfvYsP3DVeMKwZ2MuXTJNF3i130y5Xk22z-U3Rw6L-ZoiQaLBk5KjV0vI5ypyCFdjqo29tU3ItsfOrwrPQ8JsuP8y65pGX6tiDg9Qc807IKnleV8LNktgGOHkQU1Vymw8tk4hJwLJExIxKoVGy7vWJZX4UiNYx7xuEfT9_E8cafFD196frhHGYVveuzpnk51YIkWmH-H9sHC0tBB4bhFFnrlrsgVz2EC_v7AjTwwj5n_4wLx8iang" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ می گوید که قیمت داروها را 400 ٪ ، 500 ٪ ، 600 ٪ و حتی 700 ٪ کاهش داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/120975" target="_blank">📅 01:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120974">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تیراندازی فعال در مرکز اسلامی سن دیگو به نظر می‌رسد حمله‌ای وحشتناک باشد.
🔴
تصاویر هلی‌کوپتر نشان می‌دهد جسدی در برکه‌ای از خون بیرون ساختمان افتاده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120974" target="_blank">📅 01:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120973">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5J6AwYF822YrRmMA-F-ESYM9BtWZ_i1QyaAa-SJgpKY57ui5DhHFVg1DMGYoNJQMcpSomJTmRDWmmdhCShoj8V05rbJ49qFHDFhaO1Jip5WnwVEha1zCtwx2_se2kFWxFl87XgqYdQyktobpj8G8kf6BF1ppCUf6brlfxWaVOH6gQ6qwEWUXhlVjJ2pInp0uEGhN8YYNdjvWmq96G0b2ZZz6I4bZmvF3RSHFseCsp9FW1KDAufJvJegU_KwOajnQFb0CpsWO99HxLKyF915tpkQJyPfO9dpziVUUixVS7AtemIu_XA7ZN8iMpZSWPtCix1F8cGQHargxIZwvrxQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلهکی
، ‏
فعال رسانه ای حکومتی:
ترامپ «شنبه‌شب» قصد حمله داشت که صبح آن قطر به ایران هشدار داد. علت عدم حمله پیدا نکردن لوکیشن سران نظام بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120973" target="_blank">📅 00:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120972">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fb57441e.mp4?token=nhlucf9H6kKjdcEINMr5qtsGv3Rsstw3ebhq1lEz3JU_0dEUYgyLalZAIVt4DGE4oZUZ-hRtx8LVukzKXw4PG_VDNOp7gx6noKgSStN6OYOXvlWUuh-KkLhj8wOO0DGUEafjjNXhqb7qFm9iNZ-KYzoDc4Og7uYjTOtlDH74QSNM9xGlUnTZJXna2mEaXKl67Scvd-1TT2HqTGrto7MisjKV5V1GcYmygwYfDp0MTL0arEjL2KPuZ8Tz-jYQBwekB0WqN3SV6Y45SkmP5J9TfVTCjv2-V_5qJCSPSnw5K1FNDb0VnydK6ZZGbsdG9-nvtx0h2gLZMpIl8ixjuXuQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fb57441e.mp4?token=nhlucf9H6kKjdcEINMr5qtsGv3Rsstw3ebhq1lEz3JU_0dEUYgyLalZAIVt4DGE4oZUZ-hRtx8LVukzKXw4PG_VDNOp7gx6noKgSStN6OYOXvlWUuh-KkLhj8wOO0DGUEafjjNXhqb7qFm9iNZ-KYzoDc4Og7uYjTOtlDH74QSNM9xGlUnTZJXna2mEaXKl67Scvd-1TT2HqTGrto7MisjKV5V1GcYmygwYfDp0MTL0arEjL2KPuZ8Tz-jYQBwekB0WqN3SV6Y45SkmP5J9TfVTCjv2-V_5qJCSPSnw5K1FNDb0VnydK6ZZGbsdG9-nvtx0h2gLZMpIl8ixjuXuQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار جدید رونمایی شد
‼️
🔴
تندروهای خیابون امشب شعار مرگ بر "امارات" میدادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120972" target="_blank">📅 00:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120971">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
هاآرتص: مقامات اسرائیلی از دست ترامپ کلافه شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/120971" target="_blank">📅 00:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120970">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=gAzVcvLvgokwYZ4zvcMXI4lfILPBb0hQsTpwX256z21850oaMn40TBDy-nXl537ucgflJfhqbJeW8XdUlWdzBw2-dyXEr_aFqBbK3oeqjaRn05qBCcpSjMVs0swCDbwR5N-WUeakFOZZJHrF1QD4xMd2Fw4vilTh7-RDs4nKEMGGpg0p-6NEtD1EHrdwsFbJYRd30Dr7EFVntGQnKi00nTR-K_me8TeMMpjfwSe4ju7ScSAR8kKpM6gROYkxu1qzcBzUPqkjYF1oIIvLFjgqRkYY3DoSxa52v8HRpd-F4xcnq8XJeERXTI6u8NkuM95St9XOwyeLIPDhvOpAIUsr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=gAzVcvLvgokwYZ4zvcMXI4lfILPBb0hQsTpwX256z21850oaMn40TBDy-nXl537ucgflJfhqbJeW8XdUlWdzBw2-dyXEr_aFqBbK3oeqjaRn05qBCcpSjMVs0swCDbwR5N-WUeakFOZZJHrF1QD4xMd2Fw4vilTh7-RDs4nKEMGGpg0p-6NEtD1EHrdwsFbJYRd30Dr7EFVntGQnKi00nTR-K_me8TeMMpjfwSe4ju7ScSAR8kKpM6gROYkxu1qzcBzUPqkjYF1oIIvLFjgqRkYY3DoSxa52v8HRpd-F4xcnq8XJeERXTI6u8NkuM95St9XOwyeLIPDhvOpAIUsr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واسه اولین بار تو تاریخ؛ صداوسیما امشب یکی رو
کون لخت
نشون داد...
@AloSport</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120970" target="_blank">📅 00:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120969">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0gcX3aBSihf0fCs6aujmGCTgbjbEDrzRO5XmJudZwE8J1C9DFcST0VCDmduQu__Tua9HL7X6XZkzp_7QWIeV2oBaRuPYBBRqWsl6wx-TjmTTHD3xXADcDuY3HeKeHzpspGPvW3Z4S7ToBcR9Dr3UizWnSR8K-Rmr7OKX1O6Kqic5gQK7kJtKC_Six_WQsjOzmdiJ-M_PY2IQ77p0z9QnaZlcvKox1U1GeTZUSlPYUwLNff5tgAvofdGpeezSucB99dwNXj4X22pfviUgRFyftGLHC-36mIERqP9w1XpMv8Xm01NY27v2gsfctx1p58osJx-pOZJlS3yZvxH5FSMwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم هفته قبل: آمریکا تا ۳۰ اردیبهشت حمله میکنه
🔴
ترامپ امروز: فعلا حمله نمیکنیم تا مذاکرات ادامه پیدا کنه
🔴
پ.ن: عوستاد همیشه برعکس پیش بینی میکنه، سری قبلم گفت جنگ نمیشه اما فرداش شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/120969" target="_blank">📅 00:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120968">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه آمریکا در گفتگو با الجزیره: ترامپ برای رسیدن به توافقی غیرقابل قبول عجله نخواهد کرد
🔴
خطوط قرمز رئیس‌جمهور روشن است و آن اینکه ایران نباید به سلاح هسته‌ای دست یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/120968" target="_blank">📅 00:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120967">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bixUgO_0dAPLGHUKDNNxZ-572oI-j70t1gCqSjn1XMJNvZBJSiFtEHhwTBhcH_UDs2FrmmomYNUpcMC6tnCsNraAiNX_nx5aN85yVVFqFcxQqNlXUwFC4c6Fqy1tbjIIIe56mMKMY4UkupsxcBCGUyRBUVUKIzDBtEdHwKFEr-xA3swL3kkIfzn7yZByyczL5xzNLc9-oYbp4RDk7Ob8NlNiOOBfkjE4hcAWA4OEHrL-mAs68ffeKdMsLyL94lYk5ygz6P7pzb2bKSYSqjGNjg6BQBS5IAEfSTQ8PAtyNYkdqonMoitDUemMMkQu3tS4cJzv_OW0gbOC625Jwe2_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط تو صدا و سیما تانک آوردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/120967" target="_blank">📅 00:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120966">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
صدا و سیما: دیدید ترامپ ترسید؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/120966" target="_blank">📅 00:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120965">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پدافند اصفهان فعال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/120965" target="_blank">📅 00:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120964">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری/ترامپ: مذاکرات جدی برای رسیدن به توافق با ایران در حال انجام است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/120964" target="_blank">📅 23:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120963">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
اکسیوس: دو منبع آگاه گفتند که پیش از اعلامیه ترامپ، او با رهبران عربستان سعودی، قطر و امارات متحده عربی تلفنی صحبت کرده است. اما مشخص نیست که آیا هر سه رهبر او را به تعویق انداختن حملات ترغیب کرده‌اند یا خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/120963" target="_blank">📅 23:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120962">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McvaY6UMfFHoyR4DLcHpBUpLatW-__PbFck5_Qc7y-75SawCkWE-4745hWNPYYIM6a66BVzgo6o2BWBJdNQPjSwLe6xLwW8fvXEuJm5EhyvhCv1DoQ_EKbdtIBUKM2XD_HF0nBU08VD9soBruqM9T7uVjdeNZTe9zBDA3IT2ERKJMYwPnBAXvx73bBz33vJusre3hyoijkGekv1_q1AC4pKr7nd834JWhq8Kg-PsiOvDSU-uaZsJxMYZ20a4DMXf250jse-uKs8KCPak49UtnK2fxt9Lpsd59Keo4-tKA0NyZA-LG-W84VGUa3vpow6eRfT29hLAKYiKkNQWtg4fZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس:
ترامپ از زمان شروع جنگ حداقل 6 بار ضرب الاجل ها را تمدید کرده و حملات برنامه ریزی شده به ایران را به تعویق انداخته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/120962" target="_blank">📅 23:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120961">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZb5unuJ-nBRR1wcJgGcaBh1kbSKNUi6u0y2tj5Kscp1uVpcuvYzzJShgpbCCSSVe504lOjD_mW0KxP2FHDdIuFeC4fzRKB4IK4dF7GAj6nKiz9yi94rTMfB-u4xsd0WKoKlWOPqD9HUL5pn41owuVRrUtTtzkZqUKyeBlX712Enj3lt_k61oSVNfFvUh6kTcvY6_V3k1qwCbApH613RO-_QO36zMe9Vbf-WE5GscXOTm-vvUq5gP72PMti-XR2NcplYla30U7WSrjXDGzo7g-AfE0Q7bLwUqV81jFeA7gtyJLJzmuRdwZVd9yIEYAbT_Tk8ajXHwCNogaWC75dPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدم صاحب اینجا، یک ساندویچ ساده به این دوست بازیافتیمان که کمی دورتر مشغول سطل زباله بود، داد. چند دقیقه بعد که ساندویچش را خورد، در حالی که حواس کسی نبود، به کناری آمد و شروع کرد به جمع کردن میز و صندلی‌ها و رفت.
ایشان رایگان نخورد.
در شگفتم از مفت‌خورها، مال مردم‌خورهای تسبیح به دست
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/120961" target="_blank">📅 23:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120960">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/120960" target="_blank">📅 23:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120959">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBuRznpmRoXHkq6sdY8ANyUruEIp_VrSsTdVUR9uoi2M_e-IZUtL8jDDXkl8HHRdoDoU2qBWTaijoWg6yIIeZJo7cnJfyf5X0llSvQB4G5tWqtTLFVMo97o1RjTw0eKn-UCQb2Cv4aQACWQsv3jrg9xwYIJuMkqIR8dCFaMPi7ZyM1WxKfOfTF7d8Pp08qWp6nxJu-iMW8XKYdDMTrLpQapo91wjlPiroRa1YbA9TMvZpwdmV6fGiGgMdTxKRo5hiBRKfPgMtmK7m1gZm2oBHc3bKMel-SuSE1sptrZlEmrTRYULxLbXVp8amPVELLOpFi31VBg5E6P4H3JbRwjNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: وزیر کشور پاکستان که به ایران سفر کرده‌ بود، علاوه بر تبادل متونی، به نظر می‌رسد، ضرب‌الاجل دو روزه‌ ترامپ را هم منتقل کرده بود؛ مبنی بر اینکه یا توافق موردنظر امریکا را امضا می‌کنید یا حملات را به صورت گسترده از سر می‌گیریم!
🔴
اکنون ترامپ اعلام کرده در پاسخ به درخواست رهبران قطر، سعودی و امارات، حمله را به تعویق می‌اندازد تا مذاکرات پیش برود!
🔴
علی‌رغم تلاش‌های گسترده برخی کشورهای منطقه در روزهای اخیر، همچنان فاصله انتظارات، شروط و حتی نیات طرفین بسیار زیاد است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/120959" target="_blank">📅 23:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120958">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در سلیمانیه عراق
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/120958" target="_blank">📅 23:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120957">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bw-PpVy0ElWEOqo4qcNLOPkF2Ig1mLtN-zNLTrr3r6ameKvBO-dkKs2VoGyKNe4fw1OFZ5-jHZZGpe4arI_os-UYJqKY7bW7QLdi9P9UANWzevDbiIykAvXy7jxgc_LZcvCEW91oRgucdhlD_r0f781kAAdXRULWa27VKye8DMLyal339UWqSQL0rHuS91dYRrwOfXv42KfFgz3PBZ7fQLZE5-BiC3DDjbVqc41jWL9QcAPq455p7QdNd_Twn1pWe9Ta8sJdPn1yMGsujWCiDTAcEaHo_5QrcLIVw5EmelbCTBmE3m_cYoPPHs1eEPyBXxwfAxl3HgMlpOrhSTjBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمب‌های نور افکن تو غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/120957" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120956">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4686aac92f.mp4?token=AqP8Xxb6hYPW7GfANhJH8_uOGcqOSYAm3ek2C6Jk8YFmlwbftYrfagoP5J4-Hmy35h4b8EgY5ZGk4KYdVgxPjFTaf-7EL6hQSQ9eLkmpv3EirPb03lV7hYT3OcgbiUT92s88Jq29vrpiBMr68mMTa-bzR9mm_hrz_ZDiMKCF4ZkHNuV6g7dNQ7bN-HoPeMJBxpkB-ykwdiX1womUbKGcxGNMJFM_1IZVGHDhCTu7RC3Cj8twBxFI8xEOmwvgkOreZLAnYVUYFUKSIOBRBC9NsQPVBLEtKzKi0_5J3SPEFX8EwNXOflTv3wIYE-assWORPa_iulaNka168tqHXxKARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4686aac92f.mp4?token=AqP8Xxb6hYPW7GfANhJH8_uOGcqOSYAm3ek2C6Jk8YFmlwbftYrfagoP5J4-Hmy35h4b8EgY5ZGk4KYdVgxPjFTaf-7EL6hQSQ9eLkmpv3EirPb03lV7hYT3OcgbiUT92s88Jq29vrpiBMr68mMTa-bzR9mm_hrz_ZDiMKCF4ZkHNuV6g7dNQ7bN-HoPeMJBxpkB-ykwdiX1womUbKGcxGNMJFM_1IZVGHDhCTu7RC3Cj8twBxFI8xEOmwvgkOreZLAnYVUYFUKSIOBRBC9NsQPVBLEtKzKi0_5J3SPEFX8EwNXOflTv3wIYE-assWORPa_iulaNka168tqHXxKARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیراندازی فعال در مرکز اسلامی سن دیگو به نظر می‌رسد حمله‌ای وحشتناک باشد.
🔴
تصاویر هلی‌کوپتر نشان می‌دهد جسدی در برکه‌ای از خون بیرون ساختمان افتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/120956" target="_blank">📅 23:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120955">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thZhBljnjz66Ot6MDBD3tgocQO4SyIzHhIteWmdTxzUPux2IZJx7-Nw4Zw1yvgg-Acd_mSrEoZXE4kn4zRWQx4yVP0RA8hkih9yynmO_xEGF2sj2kn8_-Rz5Hx-nK7Gb-T9RmBWnlda23C_BGdnRZNG9wymfA28jUToeD1VdjJvnu1b0_k1H5kOwHYanSe6nW-4PR29LG5QaxGLLInl-gHqvsREj_BIHKdQk3eR850LpKVhxLdhFDU9ekf7skk9ibm2IrcQ3HXLPXbCoOoviXVOdPp8aNTV7BIpFvybosIIZ5JuLkb100cvjFjXd3t0d1uXmrxmCfr7vtAE8SdawKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
در مریلند، ۵۰۰,۰۰۰ رای پستی غیرقانونی ارسال کردند و گرفتار شدند! حالا قرار است ۵۰۰,۰۰۰ رای پستی دیگر ارسال کنند، اما هیچ‌کس نمی‌داند با ۵۰۰,۰۰۰ رای اول چه شده است.
🔴
علاوه بر این، بسیاری از این آرا به دموکرات‌ها رفت، بنابراین هیچ جمهوری‌خواهی که در مریلند نامزد شده باشد شانسی ندارد! این کار توسط فرماندار فاسد ایالت، وس مور انجام شده است. او اجازه داد این اتفاق بیفتد تا مطمئن شود دموکرات‌ها پیروز می‌شوند.
🔴
برای من هرگز منطقی نبود که مریلند به عنوان ایالتی خودکار دموکرات در نظر گرفته شود، اما حالا می‌فهمم چرا. مطمئنم این موضوع سال‌هاست که ادامه دارد. من از دادستان کل ایالات متحده و وزارت دادگستری می‌خواهم که فوراً تحقیقاتی در این باره انجام دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/120955" target="_blank">📅 23:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120954">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
گفتگوی وزرای خارجه کویت و عربستان درباره آخرین تحولات در غرب آسیا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/120954" target="_blank">📅 23:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120953">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در سلیمانیه عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120953" target="_blank">📅 23:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120952">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhY7lTjD0q0416oQeECZa0e0Ebm9i4ZmabBRbH5ym-WQd6IlNmHuNW-BwhGh1gSzupnoUYvezcDVFKiAGAMAS6ehTSA5C7-vfsmB2JoaXqr0w9KuIGDwkYYB5r9BsjwiJT3tO46rLB9NAKLXPdOK3WS0pKmXkZnr8trBCKXmB66ujWxuagctTrUzCGiqJqdVlKrkJlxfa2ig91MxizdHxx9vKlruYG_Mk1nAvdKyiIopLJNDkx1d3ge3yTox4-lT3Ngw0wCK6XYdjTci25-N3MHLJ7KDC3y4NMTJcxLULgOXVfTPr0839B2RYrGzgBoIHGicF0ls8LhkGDUyAOq_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تخفیف ویژه فقط به مدت 2 روز
🔥
🚀
با بالاترین سرعت و کمترین قطعی
💰
هر گیگ فقط و فقط 170 هزار تومان
⚡️
پینگ عالی
⚡️
دارای لینک ساب
⚡️
پشتیبانی 24 ساعته
⚡️
بدون محدودیت کاربر و زمان و ضریب
⚡️
مخصوص استفاده روزمره، هوش مصنوعی، گیم و ...
✅
جهت خرید با تحویل آنی فقط به بات مراجعه کنید
✅
@Lex_Server
👾
@LexVipBot</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/120952" target="_blank">📅 23:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120951">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: من به وزیر جنگ، رئیس ستاد مشترک و ارتش امریکا دستور داده‌ام که آماده باشند تا در صورت عدم دستیابی به توافق قابل قبول، حمله‌ای کامل و گسترده و همه‌جانبه به ایران را با کمترین هشدار ممکن انجام دهند این آخرین فرصت ایران برای توافق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/120951" target="_blank">📅 23:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120950">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
صداوسیما: ترامپ برای پنجمین بار از جنگ مقابل ایران فرار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/120950" target="_blank">📅 22:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120949">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
پلیس سن دیگو گزارش تیراندازی فعال در مرکز اسلامی سن دیگو را اعلام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/120949" target="_blank">📅 22:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120948">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
پدافند هوایی جزیره قشم فعال شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/120948" target="_blank">📅 22:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120947">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
المانیتور: شش کریدور پاکستان برای ایران شریان حیاتی تجاری ایجاد کرده که از طریق آنها می‌تواند بحران تنگه هرمز را پشت سر بگذارد
🔴
اقدام پاکستان در افتتاح شش کریدور تجاری زمینی با ایران می‌تواند به همسویی منطقه‌ای وسیع‌تر تهران سرعت ببخشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/120947" target="_blank">📅 22:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120946">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734d3602da.mp4?token=Dfi9k1qWuF3KrEvPJNEvf2Z9iWnVqGpfpct1QPypzsuCErgLB9u7QkY11rHVOvfWN0hxzGnHqd8QcJ4otGf5gARHn0lxB82ES0djPRmZ-vnIRi2B405WoA3eg7BEJZw_yVoi8a9hlReSoUWqqK4pvrQL9qeibaKiTyg1t8NOSARAZFJeSg8aaxtBpZbuhde5i8sDdfzNWWXbzIw2w3TVvZg4nh6C7EbHeUBUrBjqjAPyPtxCxn9iZJUEAC8bhhL-HViCCxacHv6OB6-cqcNscFX-s0PzyLXFsu6KJQs7UTJENpsSLfcSqSEuFgE_GLGLwmmjXafYI4HH_uqtIhwWjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734d3602da.mp4?token=Dfi9k1qWuF3KrEvPJNEvf2Z9iWnVqGpfpct1QPypzsuCErgLB9u7QkY11rHVOvfWN0hxzGnHqd8QcJ4otGf5gARHn0lxB82ES0djPRmZ-vnIRi2B405WoA3eg7BEJZw_yVoi8a9hlReSoUWqqK4pvrQL9qeibaKiTyg1t8NOSARAZFJeSg8aaxtBpZbuhde5i8sDdfzNWWXbzIw2w3TVvZg4nh6C7EbHeUBUrBjqjAPyPtxCxn9iZJUEAC8bhhL-HViCCxacHv6OB6-cqcNscFX-s0PzyLXFsu6KJQs7UTJENpsSLfcSqSEuFgE_GLGLwmmjXafYI4HH_uqtIhwWjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما دوباره فریب تصویر ساخته هوش مصنوعی را خورد!
🔴
کارشناس صدا و سیما مجدداً روی یک تصویر جعلی تفسیر خود را از سفر ترامپ به چین ارائه کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/120946" target="_blank">📅 22:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120945">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری/ترامپ: حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/120945" target="_blank">📅 22:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120944">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/ترامپ: حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/alonews/120944" target="_blank">📅 22:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120943">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7953d92b1.mp4?token=GayGVCSJs9U0UBnFqpDvgHUgjjyfl_bmcpZ98T1Z0D3f7WevChw8Np2OM1gAGZi0cTjDa5KYnncJ4gl55UbQzePOiL5N_3mXf171fo5EYPNPWT648cZaC7KyFWbk87B-TV3sBTLgVRwulac8wpRoXm0F8PL_S7ArZ20Ql2AmN3Ry3mlWqZYQcH_5aQB3pNQic_2agOdYPou3w9kHENUGIl4BZkMB4uH16e7TTZgNFC1pXga2WB3b8C9J6RehSmpjaKQBJ-y9niztJe2EbwnxpkQdhg7tzeU63slVwwg36fnAVEBndkiAYpX1geCOowcQPUVMPD7g48syKa5ZrqAo1zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7953d92b1.mp4?token=GayGVCSJs9U0UBnFqpDvgHUgjjyfl_bmcpZ98T1Z0D3f7WevChw8Np2OM1gAGZi0cTjDa5KYnncJ4gl55UbQzePOiL5N_3mXf171fo5EYPNPWT648cZaC7KyFWbk87B-TV3sBTLgVRwulac8wpRoXm0F8PL_S7ArZ20Ql2AmN3Ry3mlWqZYQcH_5aQB3pNQic_2agOdYPou3w9kHENUGIl4BZkMB4uH16e7TTZgNFC1pXga2WB3b8C9J6RehSmpjaKQBJ-y9niztJe2EbwnxpkQdhg7tzeU63slVwwg36fnAVEBndkiAYpX1geCOowcQPUVMPD7g48syKa5ZrqAo1zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: خیلی از مسئولان ارشد نظام معتقد دارند که باید در مقابل اقدام محاصره نظامی آمریکا، پاسخ نظامی به اسرائیل و آمریکا بدهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/120943" target="_blank">📅 22:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120942">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
پدافند هوایی جزیره قشم فعال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/120942" target="_blank">📅 22:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120941">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
یک مقام اسرائیلی می‌گوید ایرانیان در حالتی از سرخوشی به سر می‌برند، خود را پیروز نهایی می‌پندارند و معتقدند تهدیدهای ترامپ جدی نیست و او تمایل واقعی برای درگیری در جنگی جدید ندارد، طبق گزارش ی یدحوت احرونت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/120941" target="_blank">📅 22:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120940">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be8d77ef7.mp4?token=Qa7FL2jM7V-nqAJneb4HnF0Z-P6gP70WBYPpJCa5kiabOI6G6CPAEdvY6kuun9y9AF2rs4Y2pfvdlCBHxMkd4sFlF-xr7cHlLNNfWAxYIHcK1SWoN_DuxWV-b1G5iN-MLYcyUzn_XUHkXy-TLmI9d3_pxOuMSwvC4DGIYgmDqlmr87oxFP6CM4nB_onnZI_M9vIja6bwYK5NySuXgBEEIhQ0HLVkYFK3NralGyvUSpu8ABLrvujZHnHBIpWe2PNVU2Uy1MRtLsQeZuwWtfU8a6I1OX-8Y2BXNy2eXsoYjfJTgnVi8P7Cy56MBkEhYhwSVK4g_HK6fCop1_ru3MGjdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be8d77ef7.mp4?token=Qa7FL2jM7V-nqAJneb4HnF0Z-P6gP70WBYPpJCa5kiabOI6G6CPAEdvY6kuun9y9AF2rs4Y2pfvdlCBHxMkd4sFlF-xr7cHlLNNfWAxYIHcK1SWoN_DuxWV-b1G5iN-MLYcyUzn_XUHkXy-TLmI9d3_pxOuMSwvC4DGIYgmDqlmr87oxFP6CM4nB_onnZI_M9vIja6bwYK5NySuXgBEEIhQ0HLVkYFK3NralGyvUSpu8ABLrvujZHnHBIpWe2PNVU2Uy1MRtLsQeZuwWtfU8a6I1OX-8Y2BXNy2eXsoYjfJTgnVi8P7Cy56MBkEhYhwSVK4g_HK6fCop1_ru3MGjdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان، رئیس جمهور ترکیه : امروز دوباره دیدیم اسرائیل با یه طرز فکر فاشیستی اداره میشه
- نیروهای اسرائیلی به «ناوگان جهانی صمود» که کمک‌های انسانی برای غزه می‌برد، تو آب‌های بین‌المللی حمله کردن
- این کار دزدی دریایی و راهزنیه و من شدیداً محکومش می‌کنم،مخصوصاً چون سرنشین‌هاش از ۴۰ کشور مختلف بودن
- ما اعلام میکنیم که، کنار مردم غزه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/alonews/120940" target="_blank">📅 22:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120939">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcR89CIP_LBCdtfIldi30QXGYttOxLMX9uvgr0AjI96vkUa-v9OPdkfdSGW6HuR55qMHTzO4MsmN6woXoC4fGQwXSn-8zcz-ATX0V6ois7PtcvwN6WHJWkejVkb9zdzsxPYN7M9chDK8YCOy6Mh5PvDp34QtSc8HzIreKuXjgIxsHNaW90-k4EP2uQ4sVM8LuN0CjaZNip5Ax7So9trQ1fQb2blKMrPlxPGbKFEykjgF0T9vgpRaTIh0Ty13BIQQHfTob87ULOMCJJZoV27hxGGiKU_ZYF7LayXwUbyeXZGa2X3K81hOMOL7L6uAu7sMFJjVMUIyLbdu_zVb0qMxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: گفت‌وگو به معنای تسلیم نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/120939" target="_blank">📅 22:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120938">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فارس: قلب اینترنت جهان در دست ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/120938" target="_blank">📅 22:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120937">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHUip2oazPZhlrpkw-YGT788u3fkGJOJqMCXSmIV_3SMWpzTinOSPDutY2v3-uc850zzQ1xyaP0pkEZE_zP1gf54nmn3WdIb51t8LLDZQAkgU3LnCYcytNkzUZbmuSUv_z-TW3kgmjk9_lACTQjVf4Gi2bLJt7SWWSkgClA_Cj57dPZt3S3TmgG8FPWTu-7a1xX1Vgho4bzsjX7kKmwS2_bbLXMwCu7SZI4jNz7sV1_GynhDYsxtKofrppkJ2000iBQuGkU9nMV2AskwMwc3HO8aeECfloWLv9Rwh1NkcfURgTlgBIBgwk1-W_9Vsk_iN4-xRXa75q3jEmbN0d3RKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز آمار کشور:در اردیبهشت امسال، گوجه فرنگی و خیار بیشترین میزان تورم را تجربه کرده‌اند
و تخم مرغ رتبه سوم را در اختیار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/120937" target="_blank">📅 22:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL0BdMLg71eDdyHaBy9uNc6Ekn9h3du_gSrqhkf7cgN6uvUN-glqJXliAEp61Cmblw-ps44sBjNb8Tj5DPjEgeIusjbTBK8WPva88ImBkivOYTrT8YEjwor_5NSM_EVWdbklcEq4j_TgR_uo68BttlrP76AU_40iqZaayc3huDnlZbgujJQ3N5VFL5SJ5i2szhdWZaNr5_auy-VN9gxgqCZmr2-_K_Wyv_ZFnNZxPiJCbQ1zUMzmbTnPw7tKf4vjPVf9YNOt35mIS3Md9Nlayr0veZXrbNpRoxF6SYzsEVfVTVM6QHAGXT5QZBJXLV7xUlqF3lWtkHwuwRc5rvVn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اگر فرد اشتباهی جانشین من شود، برای آمریکا فاجعه خواهد بود
🔴
رئیس‌جمهور آمریکا در مصاحبه‌ای که روز دوشنبه منتشر شد، گفت اگر پس از پایان دوره ریاست‌جمهوری‌اش «فرد اشتباهی» قدرت را به دست بگیرد، این موضوع برای ایالات متحده فاجعه‌بار خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/120936" target="_blank">📅 21:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120935">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
معاون اجرایی رئیس‌جمهور: بر اساس نظرسنجی مرکز ریاست‌جمهوری، ۷۰ درصد مردم نسبت به محدودیت اینترنت ناراضی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/120935" target="_blank">📅 21:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120934">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEldIHRBxunDOGWAC2c-TcHe3EJo8d_LohJdcGsPiaFJEri0AIUS8iSWJXRteVqAeJDyPbvwyTMmz-m_xW8qbn0YOEfCIWWPm7deepXRneVcGj7e3NQ5snoiyS8HHD8zlANCeoqZJhvvdh0MnGbfX1iWR88TU0fz7QO9US-e4m9TW22VuuvFIeP_cVzbuCx2BIdI4VSX4rPSdrHbhi1Y_VXs0cm5tl1zd58rQZBABrLhpLOS4-LHjbNXdJ60qO1ZvyEt-KjfJmKQtoReGWf5QWSNckKcQiD9PXMHgXnSEZNOw989U7syc7yq0lKrMloqNClrgnU-BVDHDTrFGDYC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سالار آبنوش(ولایتمدار): آمریکا اگه تسلیم نشه باید منتظر موشک‌ها باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/120934" target="_blank">📅 21:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120933">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a95ed2f7d8.mp4?token=ur_paTiw2oQKVYmQHFO2B1gVg4f9QBEP1xyi6G7tC7KFBxoIrs0mSNTRW35ChkMmL2zLHAG8sUhVdpJMdD19wtpO4otpCLVu54AAR7Fc6jqZ8kgiBIk47JnKYbXkH2M2yPdRYGdbZdnXvBIq-LS-HcEqI3HntKjt1KrOsN1aQXI5YuKfD5Lx4JCfAI0pg73IvUx_7Aqeaak4OCUTSF7-eQjQfX5IT1m_0CT8VIRA-12gCPAdoMlRU_t_CEQ0k_tr3iQVYQU0lePrU4MhjC5vfFLEELyHiq5k8VdSfIZ5p2klxgJEp1alCc8k_0Vfr1Lb4M8cFFgu56hPh6GorkG4PhsFQV9vh6fwCZsDU5DKhpbCldAOi1n0tP39Hphf0kyuLpaCWm7zIu74bznqPRiC27Q33yu7VYnh_a5V97XbDc6OsDtCMhvlMzjy1Mwf5Hm_q-AILayjGIJ30xrIhjdUWp4dNBnQ70l2YanoZMoRwMy0vkgrFISC8TjioEbxN6ncypvDAtocZ_Dm66peCDE_A3LZUlG15rU9kHYseXBmXufQ1TFZ5OTz3FMoukdjrncvboB7pmOOIa_8u0LCDPp-XasIX_4D6L4Wf8HbT7drof6MGJJ9oY11mvnA7TfuFx7abhc8khZPG1WVsTdpGyG9zveKCLlvmgccpl3hSHRc5i8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a95ed2f7d8.mp4?token=ur_paTiw2oQKVYmQHFO2B1gVg4f9QBEP1xyi6G7tC7KFBxoIrs0mSNTRW35ChkMmL2zLHAG8sUhVdpJMdD19wtpO4otpCLVu54AAR7Fc6jqZ8kgiBIk47JnKYbXkH2M2yPdRYGdbZdnXvBIq-LS-HcEqI3HntKjt1KrOsN1aQXI5YuKfD5Lx4JCfAI0pg73IvUx_7Aqeaak4OCUTSF7-eQjQfX5IT1m_0CT8VIRA-12gCPAdoMlRU_t_CEQ0k_tr3iQVYQU0lePrU4MhjC5vfFLEELyHiq5k8VdSfIZ5p2klxgJEp1alCc8k_0Vfr1Lb4M8cFFgu56hPh6GorkG4PhsFQV9vh6fwCZsDU5DKhpbCldAOi1n0tP39Hphf0kyuLpaCWm7zIu74bznqPRiC27Q33yu7VYnh_a5V97XbDc6OsDtCMhvlMzjy1Mwf5Hm_q-AILayjGIJ30xrIhjdUWp4dNBnQ70l2YanoZMoRwMy0vkgrFISC8TjioEbxN6ncypvDAtocZ_Dm66peCDE_A3LZUlG15rU9kHYseXBmXufQ1TFZ5OTz3FMoukdjrncvboB7pmOOIa_8u0LCDPp-XasIX_4D6L4Wf8HbT7drof6MGJJ9oY11mvnA7TfuFx7abhc8khZPG1WVsTdpGyG9zveKCLlvmgccpl3hSHRc5i8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس:
ترامپ لباس‌های محافظه‌کارانه‌تر را دوست دارد. من این موضوع را به سختی سال گذشته یاد گرفتم، زیرا سنت این است که معاون رئیس‌جمهور نخست‌وزیر ایرلند را در روز سنت پاتریک خوش‌آمد بگوید.
من تصمیم گرفتم جوراب‌های چهاربرگ شام‌روک بپوشم تا نخست‌وزیر ایرلند را خوش‌آمد بگویم. ما در برابر خدا و همه مردم — احتمالاً صد دوربین تلویزیونی در جریان یک کنفرانس خبری زنده — نشسته بودیم و رئیس‌جمهور شروع به بیان سخنان خود کرد، سپس نگاه کرد و گفت: «با آن جوراب‌ها چه خبر است؟»
پس به سختی یاد گرفتم: در اطراف رئیس‌جمهور ایالات متحده به صورت محافظه‌کارانه لباس بپوشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120933" target="_blank">📅 21:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120932">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni2B1TSNCg2owruJdTFjyKpddt_3trFZUgyCQe3uKxL1lZoUZ5hGtXuZPKBNZ-Q5wx9ftNMKf6L68tL2ipL1XS84SH7enb-4rMZV1j3HC8NhzKi-BFTmIJdqmTs4P_jrOHutlFak5mUKzKMamyQsZeocFlRNbUOXNGBqVoUn9bw_Jo0Iw9uE2AhoXdAFw1SwfDh-f98Prd1zcMu_lA6md9Ix88e0GgkdlQoZOghr7VGFB2HGXasM-oqAOrKFcVMh3xoB1LaS6mw7VaAcJH5_pJwY3xL5mvd1jMpG9zKFFmjYSY8uG2p-MDDAVZ-TQB0Qy36ahbULjJvAmaqkar2Oag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عبدالمالکی، وزیر رفاه رئیسی: ایران هیچوقت دچار ابرتورم نمیشه چون وقتی یه چیزی گرون بشه مردم پولشون نمیرسه بخرن و فروشنده گرون نمیکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120932" target="_blank">📅 21:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120931">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKBvnUfE01vyr8hSke2fNApiP3WibvAgc2QmPePlXTMy-IB8qqSF-Zn0nkZ10qz--eilNjY3Uz4PHUP_S7dFSzr6lvt5l3uqK-9rW93atxc76UnEjzW64by3YBh8kRlNjgJx7eRJZcZD1n17fNT15FiDlmtEVT6NN7ptVPDCBcg-KMQQZ8KXxJ_kv2-jG4uMFHpp_NQfkGGdikzZ7weirRck_V-otd8bJF_Y_blUL_tnh-Ny_wCag-KqoOi9XuUgSpkc3jdvwyzCdo3-A4yeA3_awgHJCFOm7Ca5qjjhEDzJH_ac4IuGE0qCvZrRbfaqdJfdMAPzIwIuVUOAERwq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۷ اسرائیل: امریکن ایرلاینز توقف پروازهای مسیر نیویورک به تل‌آویو را تا سال ۲۰۲۷ تمدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120931" target="_blank">📅 21:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120930">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a835e4e8.mp4?token=t2AGqjqHW9EzoX3yDtKdzoQ1L3lk9-UfMP6LKsJXFfKYuzMlB1Hrke7PFdP9WTjF-LRg7G4YBQE0xLyw_tOYLUZBWcVsKKuklzhhtc7TOCImXKS8UnfTHAiM7HLxzAfmX01POYkXvhpr6vEnTuCwpZDa_fv-JjGJwIpoykGJDo5fhlLOQeXxaO4q5IN552-OT2QMWxUfIWxQ_aPT8Ne2WyZAxG545Ao6haNoOvTeiJ_-pSPvePIvY4BxKUNptUJUwL_yFp0czCyaKFAKMs1RBycWJnNrv4k_xfnpf7EgJDI8MZq7_FfpH_xUfhtYSy2zUpKMT7CMjZ9nZVKFyC4KhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a835e4e8.mp4?token=t2AGqjqHW9EzoX3yDtKdzoQ1L3lk9-UfMP6LKsJXFfKYuzMlB1Hrke7PFdP9WTjF-LRg7G4YBQE0xLyw_tOYLUZBWcVsKKuklzhhtc7TOCImXKS8UnfTHAiM7HLxzAfmX01POYkXvhpr6vEnTuCwpZDa_fv-JjGJwIpoykGJDo5fhlLOQeXxaO4q5IN552-OT2QMWxUfIWxQ_aPT8Ne2WyZAxG545Ao6haNoOvTeiJ_-pSPvePIvY4BxKUNptUJUwL_yFp0czCyaKFAKMs1RBycWJnNrv4k_xfnpf7EgJDI8MZq7_FfpH_xUfhtYSy2zUpKMT7CMjZ9nZVKFyC4KhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اینا بهتر از من و شما میدونن آخرش چه شکلیه برای همین دارن مزدوراشون رو آموزش میدن برای جنگ شهری.
🔴
این صورت ها را به‌خاطر بسپارید. همسایتونه؟ کاسب محل؟ فامیل؟
🤔
اینها قاتلین فرزندان ایران هستند. نه‌می بخشیم نه فراموش می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/120930" target="_blank">📅 21:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120929">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
خبرآنلاین: برخی شواهد نشان می‌دهد کشورهای عربی در کنار ترامپ در حال لابی گسترده علیه جمهوری اسلامی در چین هستند.
🔴
این کشورها به چین قول داده‌اند نفت آن کشور را تامین کرده و کالاهای صادراتی آن را به قیمت‌های بالاتر و نامتعارف خریداری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120929" target="_blank">📅 21:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120928">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c8ed7ff10e.mp4?token=ooAfoBoHjPicvfPgvyIE6sqzqMaQKx6AH8RxXkP_EW5T2Ueou0KMt79YkZFUgQbzXMHCI1eYxczlNAnTADcbgeZj_eL4mFpHqjnYPuYBKKEdq8PjY1wYW7GGTjEVl0l6ak9eeSUGJ9PYqzIIszM4WRkdxVfIWEXWQb8aFHfUWqXaRg2JvQq-tlq77VgZsYdnkY3MlMu-HiZMr1uWewng11Vx9rh16ZReKTjb2p_Jah5IHVQTymqf4AdVPH000aG-u-SyZ2iOcPvl7GwYhcp8yjoMHpWNS_oPWbbloooeaLA7x8zmd7YZOafufJElrc2gxfBxZlBWKdOJ4MXHLmWmwnEKMepD9IYlWzjHIa006IoAp7bXyezZxGvzaZZP2OeMTZhNIgMMr-B8Cmv4pGnSmrnFGCbGeSVnQFjUGfDfOm7rYrOMySjy2Hh2w_ENlKcgaHcVzdDHMUsSHK4gnkWMoYjxwE7pCIBlYEJOJdHDo3CwVH-ve9rDjdrED_Za-LO8MKtigReerDYBoEQJqbGvkPzL2tu6ca8rUkKiZ9S8Rn98ulN0OBICHkBvBkRyDvVS6WPNhdBSdgHq3hwZ04zipzWiK3koIDNIJ-52zv7YBVjj70J25gcsbD7eQ62jSQsFP5_Hsj8ceBEk8bLZKjfUxhxU0HMJySkdNb0LZdQ_8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c8ed7ff10e.mp4?token=ooAfoBoHjPicvfPgvyIE6sqzqMaQKx6AH8RxXkP_EW5T2Ueou0KMt79YkZFUgQbzXMHCI1eYxczlNAnTADcbgeZj_eL4mFpHqjnYPuYBKKEdq8PjY1wYW7GGTjEVl0l6ak9eeSUGJ9PYqzIIszM4WRkdxVfIWEXWQb8aFHfUWqXaRg2JvQq-tlq77VgZsYdnkY3MlMu-HiZMr1uWewng11Vx9rh16ZReKTjb2p_Jah5IHVQTymqf4AdVPH000aG-u-SyZ2iOcPvl7GwYhcp8yjoMHpWNS_oPWbbloooeaLA7x8zmd7YZOafufJElrc2gxfBxZlBWKdOJ4MXHLmWmwnEKMepD9IYlWzjHIa006IoAp7bXyezZxGvzaZZP2OeMTZhNIgMMr-B8Cmv4pGnSmrnFGCbGeSVnQFjUGfDfOm7rYrOMySjy2Hh2w_ENlKcgaHcVzdDHMUsSHK4gnkWMoYjxwE7pCIBlYEJOJdHDo3CwVH-ve9rDjdrED_Za-LO8MKtigReerDYBoEQJqbGvkPzL2tu6ca8rUkKiZ9S8Rn98ulN0OBICHkBvBkRyDvVS6WPNhdBSdgHq3hwZ04zipzWiK3koIDNIJ-52zv7YBVjj70J25gcsbD7eQ62jSQsFP5_Hsj8ceBEk8bLZKjfUxhxU0HMJySkdNb0LZdQ_8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک زوج حامی حکومت در برنامه صداوسیما اعلام کردند مهریه عروس یک «پهپاد شاهد» تعیین شده است.
🔴
در این برنامه تلویزیونی، داماد گفت امیدوار است این پهپاد «به قلب اسرائیل اصابت کند.»
این اظهارات در حالی مطرح شد که در هفته‌های اخیر، استفاده نمادین از پهپادها و تجهیزات نظامی در تجمع‌ها و برنامه‌های رسانه‌ای جمهوری اسلامی افزایش یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/120928" target="_blank">📅 21:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120925">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IocPaynZuibVIhnNk17dSAD4JBBfX21SIpAnbwGXct1sn75VyqUWzymyIJIwKDBmBPVbrGNgrwda2oodh2NeJZpRcHraToWp8EHPd2itntFTq2IdHYZnsMOeFM1DDLfZM-Iu-iUdNUI6fGFU5hzr70qujOhmJp9kfmzuxO88z1iNPVYJL9XEs3LrvSXkf-_8emrhHEctXOVWPJ_qQtK0qmUu4zW7PPM388AK3qluPqo8CRzgK6x5MvWA86LMj_1NGFbrY5sWIbdz9iHhY0IFFBY9FQRzHs5HupOWBXmsFouTTju2HubEq6m6g3zb5T7ZITbdzKWjuaXsmmXGYzycKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UoITXOvj-KyZio2Tt3yDzxXAoNOjnRsaymIqIjyYHBwP8bn69Fi_LEWblpsa3AXn2weigoi0iuF3dCfuHr129lo13YV-17LzRUF4pSL3Oe4x4ugPj0l0T6GPI6uFEHazX5oQXWrlQ7_wX0jY1zQ7Cdi-8la_VLiQLyHT0tT3OUPFWPzGQv3lPv3py_yxsRDAbT-OvDLxMvHqHbdUIIMuq19AlRNozqSzBp9ow4DA73S4nWZ38UiWgdJo_Pa5P2OBZ48UhqVelsYkf5oEBRRwxh-DTTe_dKpGAO3j5vqbDL1ajNmxsNkdcL-ZqGQI3Grs6Ep0cHnnD9VtOm3v4RukNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SbddxTOLIrVNSz0tdXQJkAGhBe8CcKlz3eOIeLb-s22cDiulVK2alt3U9n_upYbdo2MAqUz2Eqei4xfqO8elOkGATq4FM69gEiVZgV3WP3pm6D9f7Vyam1LxWEKbEWYsaD7PzekID_OlLVMT9dk__Q125X1LJzVg3ZxZbfIWuqKmVXLWVxnbfsyMqpyCzGJH-GebeDp8VcHxovqH3lb4ICGMNRHpMgkYOlbZIuxIs6uSS_I6KrhdQKcKGi-_mQEVacIZz7GS9nViUzPv6DKLv0Dxhkmdv5vLD2wYqGwjBPMSgpAU9j4aObHVeedrAt3rOussI0xCbwTvh8inbuNCkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
روز گذشته در غرب جزیره هرمز یک نفتکش در حال نشت مشاهده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120925" target="_blank">📅 21:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120924">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
حزب‌الله: یک جنگندهٔ اسرائیلی را با موشک زمین به هوا هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/120924" target="_blank">📅 21:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120923">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2pm4em6ATnmvMzO7dSWMZ87hR999AgLOugHeOJNlImCpjm9VO0I8Uy1wEeyEGkV7ruGOZHoa5Q9Bl-6lBvRZxA0a-Y2n5UtUZLuktdGwchceG6VQQxTLWvHGh8Qi9P5kmDfhkRSrJdyHMb-lcgE8Mur1s9pBDYyQTCxAqLZOjI6W2cFxr32-hCCRWiX-sH9JWM1l2YNpZbKUVAVhZ2LXoRJVCvKYrdRqjAjco2Sf7Tc6h0f2_0wvdXrFHnvuK1hrdppfPbRoj5aHvvi3W6_rkRLr12kSZ5ivIE57kornYtisGfEL3W8B2pkSHKkpv9DLbvapKO__FPTqwo3r1zaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر نیویورک پست:
ایالات متحده در آستانه از سرگیری نبرد با ایران با تمام توان است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/120923" target="_blank">📅 21:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120922">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: از دست تهران «کلافه» نیستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/120922" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120921">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وقتی از ترامپ در مورد ادعای منابع منطقه‌ای مبنی بر اینکه ایران سعی دارد در هر دو موضوع هسته‌ای و بازگشایی تنگه هرمز، واشنگتن را «خسته کند»، سوال شد، ترامپ گفت: «این را نشنیده‌ام».
🔴
او گفت: «نمی‌توانم در این مورد با شما صحبت کنم.»
🔴
ترامپ افزود «این یک مذاکره است. من نمی‌خواهم احمق باشم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/120921" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120920">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وقتی از ترامپ در مورد اظهار نظر جمعه‌اش مبنی بر اینکه حاضر است مهلت ۲۰ ساله برای غنی‌سازی اورانیوم ایران را بپذیرد، سوال شد، ترامپ در میان صحبت ادعا کرد: «من الان اماده پذیرش هیچ چیزی نیستم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/120920" target="_blank">📅 20:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120919">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwrQx3VcNOqZhFgm6HV61R8QFx-ak8PdzKOEa4_kh9c7BeIS6dYFqtVJz3lR1HUrEBmGyRhgnufgqn7Cg7Q-J5R8_szJuwpKzF7a2PwZIDmrKwiOb7u_HlVplPaIq0VWhsqFAWYYsSNs4sRn2vt_aRP3OnxW4F21zvVJFffKhR0JCWD8sDYmRaBytFEr-lonKD8wAxqgdVi16i4XV4T7acrd4GpoS3Exds6x1UkOPhq4kbtmsnaNmgMw6d7zavrOHKgtITAWuZdTB7vr4ouh9Mv6A6p6Lr6lXmy63RhHodkHVPhj2in2xY0SvV8NbpTCrzNu6KHRWFRIQqFGgpe10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به نیویورک پست : ایران می‌دونه که به زودی چه اتفاقی براش میوفته، هیچ امتیازی داده نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/120919" target="_blank">📅 20:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120918">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سنتکام: تا الان 85کشتی تجاری رو برگردوندیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/120918" target="_blank">📅 20:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120917">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
شاخص صف پمپ بنزین تو ایران رفت بالا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/120917" target="_blank">📅 20:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120916">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJjNZlFGI-d3oSYkQGFBfmw-liAX0bFrbLmjrrIUnK7Kt5RjVBEYnB-y7py4v1xx3iInKTAW2hU6IpcyGMQ2FNP6Q8O7Qbo7wF1s4CsJwn2KZqBh02WZUEzZfjtfYccX8wu33-uBZlAZ6s1fNlRtGkCyBeHEtk5QgJpEYnl3Dkov5CU3F2N6uj0iq1LfD-P8T4zhWuknEjlBdVGwkTT6OlMs9oizxK0QaOb_avy0Hc_-FQlSHLtBT7EGit7kLxO9877s6jMgLAUtsckC3MbM3KurEjbW7gEr-OBhz1Uq-LjqZ0NpR1x-Owc4yHcy91ecAp8eCBP3C1vKmUhD52Xb3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۱۱.۱۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/120916" target="_blank">📅 20:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120915">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: مجوز موقت 30 روزه برای خرید نفت روسیه صادر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/120915" target="_blank">📅 20:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120914">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
آکسیوس: بمب‌ها مذاکره خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/120914" target="_blank">📅 20:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120913">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
جلسه کابینه امنیتی اسرائیل، با نتانیاهو دقایقی پیش شروع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/120913" target="_blank">📅 20:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120912">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePjMt7QiUH0IMqkG_-6lDaq3TEqJpUuAy7MXvJ9gPS4H0B374UuAOL1hHnGSVIhc4kRUyCrPMGEmZjMWGBU-cJlRWITpU5RNEEOBNEt4gORoMIdLbqh09Qa7VX80d45HHuy5M8FfalNmiOUDBf1dYgXduPDdErxcY63dc8ZkCiZCIEW_PNMkoQe30CzouuTmpXQ2_83lNzToqw-FOnhldpd88SXiM7Rb62PRlel1qpK24qswxk7obEVnINT1IvQ6rfyRuDTZPPFSTtNiSXlIgzM72DQdoRh7s7fXmSRf34AuB1vLZ4E-JjHyQGreCBxZuYi9clPtrxOyaCh-f-9ILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تری یینگست، خبرنگار فاکس‌ :
- ما تو آستانه بازگشت به عملیات‌های رزمی تمام‌عیار هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/120912" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120911">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزیر کشور پاکستان که در سفری دو روزه برای آخرین میانجیگری میان ایران و آمریکا به تهران سفر کرده بود، پس از رد آخرین پیشنهاد ایران توسط آمریکا، دقایقی پیش تهران را ترک کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/120911" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120910">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری / کاخ سفید: آخرین پیشنهاد ایران که امروز ارائه شد نیز به دلیل ناکافی‌ بودن به صورت کامل رد شد، دیگر بمب ها مذاکره خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/120910" target="_blank">📅 19:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120909">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
طبق گزارش‌ها، جزیره خارک ایران حداقل ۱۰ روز است که هیچ نفتکشی بارگیری نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/120909" target="_blank">📅 19:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120908">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQhTytRL7rv09_bANBVJWHPbjpfdhG3EGjyVwbJYg4Rs34C72PhoWDnRYmHwk46_aztokvbZwAtaNUWJBqXNaxZmo3Ak8rfzAkGigs_mHObDpEUO5GjaTl96cUmRq03QbqLTQIB8ibDYbr89_RUGafTDxB22DMik6-Wgx-LrxcJGiq9hk8lKc_i3o7U_s7-z2oQYOXLf7DaEUnvP7bISIwwSca9EdCwW7TPcyXUhjIjJYQPqULDLoz1Tmvxtfe0WoL27kiAojBgvvaeAbvEpTU1EYUW2JpEo3fp9bsrBBB9uhdve8hhcOMdS6kOK_d4j6k9QNKzZAu56-Ob-0ip8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به العربیه : داریم کارو خوب پیش می‌بریم، پیروزی هم تو راهه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/120908" target="_blank">📅 19:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120907">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0Iyuh_i3kMI17L-9IPyi6gsH9EKfBKMSf1udw17xd-Nt1HL2cIYR9P2VR4ux19Trvt3s_EOSsBOozP3dUeN72kOmqtaCgrmlR7Hl5yAruJMSjnsZAL_vrbnw-kTkydFHJxMboKvNOc-OWb93jJ1hdbwo6mBg7K2_lh_d_FVPOOXF2v1ANxrqFlo72LyJqCISBD_fqwy619FAx_T4Dcdn5b1bmhHzmL39Y5pXsfwr3kzUhTTpeSQCfGZ1R8IHYZ_UgA9wYuA88p7dgmIRJMjaTwiG5suFO0R4WMvs1zKn6RMRZaDxDvVEoS8KjvHlsAtTJwjR2Q-S5m65CrDprqXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیر
:به هیچ عنوان استعفا نمیدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/120907" target="_blank">📅 19:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120906">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزارت بهداشت لبنان اعلام کرد که از آغاز حمله اسرائیل در ۲ مارس تاکنون، ۳٬۰۲۰ نفر شهید و ۹٬۲۷۳ نفر دیگر زخمی شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120906" target="_blank">📅 19:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120905">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❤️
امروز فقط با گیگی 159 تومن کانفیگ اختصاصی خودت رو بخر
❤️
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
ساب
✅
ضریب
❌
ضمانت بازگشت وجه
✅
پشتیبانی مادام
✅
پس دیگه معطل هیچی نباش و بدون واسطه خرید کن
😁
خرید مستقیم از ربات: @manageuser_robot
پرداخت ریالی فعال هست
‼️
پشتیبانی درصورت بروز هرگونه…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/120905" target="_blank">📅 19:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120904">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kskYLLxyBJ4NviOObWYuZFrtisug7E7H9G9Jz2CEeeTYoYNzMv-bIAfvKPXI7i77yAW3JLBArB-9NYfDOrlgs2b0yhtWZ2Che9M7BpXq1_iJx_yUEfws-KZvcjqzQJCXuHMU0vagQpLWu1rugVB14jVPWmiEunZXUdXQZvBoXMoyDZju6j5jx0_89ILAuy-JyY2g4_ZkZUyKlGN3jDJv4ht6LbZ86RT9uy6ziQKDc8h7SDPl9c5swPdldX5M5GEeqJnMiKd_lDJvUCIoLT3xjeGlO5jtw20tBnp012qN95TI9utkqlNZns2x91hQHDbGVs7gWrRHVo_odknrqwjVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
امروز فقط با گیگی
159
تومن کانفیگ اختصاصی خودت رو بخر
❤️
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
ساب
✅
ضریب
❌
ضمانت بازگشت وجه
✅
پشتیبانی مادام
✅
پس دیگه معطل هیچی نباش و بدون واسطه خرید کن
😁
خرید مستقیم از ربات:
@manageuser_robot
پرداخت ریالی فعال هست
‼️
پشتیبانی درصورت بروز هرگونه مشکل:
@Niiiiiimaaaaa</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/120904" target="_blank">📅 19:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120903">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
عکس‌ها و ویدیوهای دریافتی از فرودگاه بین‌المللی تل‌آویو نشان می‌دهد که حدود ۴۰ تا ۵۰ فروند تانکر هوایی (هواپیمای سوخت‌رسان) نیروی هوایی آمریکا در محوطه پارکینگ فرودگاه حضور دارند.
🔴
در چند هفته گذشته، حدود ۲۰ هواپیمای نظامی در فرودگاه اسرائیل مشاهده شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120903" target="_blank">📅 19:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120902">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رادیو ملی آمریکا (ان‌پی‌آر): عکس‌ها و ویدیوهای دریافتی از فرودگاه بین‌المللی تل‌آویو نشان می‌دهد که حدود ۴۰ تا ۵۰ فروند تانکر هوایی (هواپیمای سوخت‌رسان) نیروی هوایی آمریکا در محوطه پارکینگ فرودگاه حضور دارند.
🔴
در چند هفته گذشته، حدود ۲۰ هواپیمای نظامی در فرودگاه اسرائیل مشاهده شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/120902" target="_blank">📅 19:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120901">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سردار طلایی‌نیک: بخش قابل توجهی از توانمندی‌های ما هنوز مورد استفاده قرار نگرفته.
🔴
آمریکایی‌ها یا باید در برابر دیپلماسی و شروط ما تسلیم شوند یا در برابر قدرت موشکی ما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120901" target="_blank">📅 19:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120900">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبرنگاران مستقر در اسلام‌آباد و واشینگتن گزارش داده‌اند که پیش از ارسال متن تازه از سوی ایران، درخواست و پیشنهادی از تیم ترامپ ارائه نشده بود و هنوز به متن تازه ایران نیز پاسخ داده نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120900" target="_blank">📅 19:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120899">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72fa02f889.mp4?token=gZ1fxPB8cx1jxLlLHzaO4CN-FAlSwdJRieligOTb5F6uH-Mg5CtrO20su_4KV_lVT7ONXLZY6zoVC6wypVlAGPIBw_RXaKYRg1_GzROAJsfJxwTu9YMv-sSoWBrSIqTQeAT_obGZNFYNuH8PyPn6GZ-aEOt2OtUpQivCWeSL6ohc5BT4gim1H5bzA_GxynGbVIcVlKcvI8FmfgM9FuiWpBQVnonwfEIWRUBmo-EUmNX-6OOyvsznw095LCQXAd0BsS94tsM28OW4fwzOjEq4HqevV7LyrurQy2KDy6N-8GxBzGw2Z0LQIbt1EYaGuU-IiDc16OyiJm98-pi0_AoyBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72fa02f889.mp4?token=gZ1fxPB8cx1jxLlLHzaO4CN-FAlSwdJRieligOTb5F6uH-Mg5CtrO20su_4KV_lVT7ONXLZY6zoVC6wypVlAGPIBw_RXaKYRg1_GzROAJsfJxwTu9YMv-sSoWBrSIqTQeAT_obGZNFYNuH8PyPn6GZ-aEOt2OtUpQivCWeSL6ohc5BT4gim1H5bzA_GxynGbVIcVlKcvI8FmfgM9FuiWpBQVnonwfEIWRUBmo-EUmNX-6OOyvsznw095LCQXAd0BsS94tsM28OW4fwzOjEq4HqevV7LyrurQy2KDy6N-8GxBzGw2Z0LQIbt1EYaGuU-IiDc16OyiJm98-pi0_AoyBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار وزیر کشور پاکستان با عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120899" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120898">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
اسرائیل هیوم: وزارت دفاع از نتانیاهو خواسته بودجه ارتش را 14میلیارد دلار افزایش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/120898" target="_blank">📅 19:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120897">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری / رویترز: آمریکا پیشنهاد جدید ایران را رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120897" target="_blank">📅 18:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120896">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری /  آکسیوس: ترامپ در حال بررسی از سرگیری جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/120896" target="_blank">📅 18:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120895">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
کمیسر اقتصادی اتحادیه اروپا: در نتیجه جنگ با ایران با شوک رکود تورمی مواجه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/120895" target="_blank">📅 18:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120894">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ادعای اکسیوس به نقل از یک مقام ارشد آمریکایی: ایران یک پیشنهاد به‌روز شده برای توافق جهت پایان دادن به جنگ ارائه کرده است، اما کاخ سفید معتقد است که این پیشنهاد، بهبود قابل توجهی نیست و برای حصول توافق کافی نیست
🔴
پیشنهاد ایران که شامگاه یکشنبه از طریق میانجی‌های پاکستانی با آمریکا به اشتراک گذاشته شده، تنها بهبودهای نمادین نسبت به نسخه قبلی دارد.
🔴
پیشنهاد جدید شامل کلمات بیشتری درباره تعهد ایران به عدم پیگیری سلاح هسته‌ای است، اما هیچ تعهد دقیقی درباره تعلیق غنی‌سازی اورانیوم یا تحویل ذخایر موجود اورانیوم با غنای بالا ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/120894" target="_blank">📅 18:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120893">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: اولویت، حفظ آتش‌بس در جنگ ایران است
🔴
هیچ دلیلی وجود ندارد که ایران و آمریکا نتوانند در مذاکرات بر روی یک زمینه مشترک به توافق برسند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120893" target="_blank">📅 18:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120892">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfLka8qAVwuD9LsFWyN5KR1oibwOHFdO3GYg0HaEr88vRr8oQU47Kp_B5ZO2hMFqucqyc0WTfej8nc6ek7ZZKr3u-IrFkM6_5IquSroJJss7o1iIiCW7j-mAPrZqPDYML-vH1XRsyvyVIZwK_AaTov6Mr9VPwUq8HhZuphQkIxC8gYAKKaQnaYKw_8nBPAXopiDZrY6x4RDG6TdlF7T8YbokwzPsPUcsxhwP7cMyntIRC21UM7NlnUem4hzL78VkXfVjZzr07IWNBQXBGQ3wyK6_JycNftzbnjZA-JPncebp8W1J8E_CHx3Lcl5cykacVOQTIRLu-kn-_OU9HRyRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاول دوروف، مالک تلگرام: دلمان برای موشک‌های ایرانی در دبی تنگ شده. دبی پر از ترافیک شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120892" target="_blank">📅 18:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120891">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azRaYrt-fRyNZIa-ITvSWFbm324AdIY4gN3MQfEX5pn0Cd-oeWpdrSJJe48-4fAyHgJqotWNCdmyzqA4OVr5LFupcfmKRNIzN0gKiXHk7UEQ8wmnf5E5884QnTEcAMRm0gaevc5dj0eTDo2W7fskXMzF-DdWoCfKC0zM24n-cRrWt9yN2pLIVFFO0azwc2_eneo1SX-C1UZU37ZptFGfoJfqhpmC2qjTb7Qd4jU637lNGTxZcd0gRfVfMlx61simfxh-2oqhjb2EngcVeUnoh5gfs9P4YKhppJp0x6dE--j9to65lJHpkAGENBTomoAWVT9GC1qqizzgkb0BXoMtWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اگر ایران تسلیم شود، اعتراف کند که ناوگانشان نابود شده و در کف دریا آرام گرفته است، و نیروی هوایی‌شان دیگر وجود ندارد، و اگر تمام ارتششان تهران را ترک کند، اسلحه‌ها را رها کرده و دست‌هایشان را بالا ببرند و فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» و پرچم سفید نمادین را به شدت تکان دهند،
🔴
و اگر تمام رهبران باقی‌مانده همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت بزرگ و عظمت ایالات متحده آمریکا بپذیرند، آنگاه روزنامه‌های The Failing New York Times، The China Street Journal (WSJ!)، شبکه فاسد و اکنون بی‌اهمیت CNN و همه نمایندگان دیگر رسانه‌های خبری جعلی اعلام خواهند کرد که ایران پیروزی درخشان و استادانه‌ای بر ایالات متحده آمریکا به دست آورده است، حتی قابل مقایسه هم نیست.
🔴
دموکرات‌ها و رسانه‌ها کاملاً از مسیر خارج شده‌اند. آنها کاملاً دیوانه شده‌اند!!! رئیس‌جمهور دونالد ج. ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120891" target="_blank">📅 18:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120890">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کابینه ارتش اسرائیل امشب تشکیل جلسه میده - طبق گزارش رسانه‌‌های اسرائیلی
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120890" target="_blank">📅 18:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120889">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
کابینه ارتش اسرائیل امشب تشکیل جلسه میده - طبق گزارش رسانه‌‌های اسرائیلی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120889" target="_blank">📅 18:02 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
