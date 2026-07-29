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
<img src="https://cdn4.telesco.pe/file/J6KcmeRY7xxAcRrqbvEsL8tGxE1IYZPA_x7ZyZDhgqsa-FxI5TxDmqt_cieWiMNeVXu4m4io4lpVGk2b7EmYF596Pj5VGC-_b7OkBthCMkohVBlc9PdJs5vmNOLqMoSWbd3-J30R6bmXWE9EzBEROrIz2a6-B8scRSd2EazueSSLvNU9h8PG2KVcH46PdScI1rg66BWqmLJ5gBq6X3uh7Epw7XWhtowDn4-PZk0COt7SbcO-Ir_Y3Nuw03pXqwWP4ianlB65AhpRnPYiisetuI9jMffvtXTZq1_BXTAM3gERFWOgcxCq4hOuD5U4z9wBI0_GBiy7wYK1v4i0-0xxRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 430K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-20000">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتانیاهو شامگاه گذشته در اقامتگاه بلر هاوس با معاون رئیس‌جمهور آمریکا، ونس، دیدار کرد همچنین نخست‌وزیر نتانیاهو امروز با وزیر جنگ آمریکا، هگست، دیدار خواهد کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/20000" target="_blank">📅 16:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19999">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دونالد ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک سرطان جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نفوذی جمهوری اسلامی هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/19999" target="_blank">📅 16:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19998">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ درباره ایران :
ما به آنها اجازه می‌دهیم که به وراجی ادامه بدهند
@WarRoom</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/19998" target="_blank">📅 16:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19997">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ درباره ملاقاتش با نتانیاهو:
این یک ملاقات عالی بود. او اکنون متوجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/19997" target="_blank">📅 16:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19996">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e251708c59.mp4?token=csGPLvq3POHFJ9ImkCBGAOGreBIQRPA9dG6vSfaLwhPHU9bPI-grEqVnyvwwzq5H7rYFkjfYuro9nxd2tsk932Vq8X1NL0RdDhokr3CAQqNlX6sGV3XRxKdZ1u9j1tT8-mhSDKAG3Ooio7ru3lRAxQBU-ipoaw2koL8YLFEEgQtlnsPYw95RPcGhnFRfl1RcwDriM8N_AEUx0iJ6WZiJoV3L2yIc5ZRgXX9G210WU82AaqZnacVonJ7hp02HQjKu9e_3XT955q60B1pRv3sB6vy0DaBaKk88HJ8Jib-XDEqJ9HSIaEiq4hpbKscisqg-algK39xIUgaUnuQICwaatx7FH_kI-HxuvU3dmgA3HD34XjKb42-zPPJ8vy4L-9Imoh5uywwvH_Wf4YtAutVY_uWB76UezE9HyHxNlS-i_3bwdOgKx9fl6MQ5BoXesuFpq-YJti0mdfBwJfzklq_58EsH4TJTSQX8ZJIL6e8pPRUSDiuZ8qPqonSevS4D7hFF7575NFboy8JySmlXPx0Zghf55yLPpQOCHfxfGLdzq1SaKFAeYrPd-byrmm3fskEmWy3CU2zFcv7vZPsCIfM2BZ7KrwY_CPSSeXXRLuG8qYSqPOaWeKgNE_NH0UkAHaT6NVAIWBI3EmhR-6tT-IAztg0uvaojdtp31fyy45Bg2yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e251708c59.mp4?token=csGPLvq3POHFJ9ImkCBGAOGreBIQRPA9dG6vSfaLwhPHU9bPI-grEqVnyvwwzq5H7rYFkjfYuro9nxd2tsk932Vq8X1NL0RdDhokr3CAQqNlX6sGV3XRxKdZ1u9j1tT8-mhSDKAG3Ooio7ru3lRAxQBU-ipoaw2koL8YLFEEgQtlnsPYw95RPcGhnFRfl1RcwDriM8N_AEUx0iJ6WZiJoV3L2yIc5ZRgXX9G210WU82AaqZnacVonJ7hp02HQjKu9e_3XT955q60B1pRv3sB6vy0DaBaKk88HJ8Jib-XDEqJ9HSIaEiq4hpbKscisqg-algK39xIUgaUnuQICwaatx7FH_kI-HxuvU3dmgA3HD34XjKb42-zPPJ8vy4L-9Imoh5uywwvH_Wf4YtAutVY_uWB76UezE9HyHxNlS-i_3bwdOgKx9fl6MQ5BoXesuFpq-YJti0mdfBwJfzklq_58EsH4TJTSQX8ZJIL6e8pPRUSDiuZ8qPqonSevS4D7hFF7575NFboy8JySmlXPx0Zghf55yLPpQOCHfxfGLdzq1SaKFAeYrPd-byrmm3fskEmWy3CU2zFcv7vZPsCIfM2BZ7KrwY_CPSSeXXRLuG8qYSqPOaWeKgNE_NH0UkAHaT6NVAIWBI3EmhR-6tT-IAztg0uvaojdtp31fyy45Bg2yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : بعد از حملات غافلگیرانه به نیروهای آمریکا در اردن، حسابی جوابشون رو می‌دیم
محکم بهشون ضربه می‌زنیم، حسابی تنبیه می‌شن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/19996" target="_blank">📅 15:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19995">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">amme kojai(IG @yashar)</div>
  <div class="tg-doc-extra">TaTaloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/19995" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/19995" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19994">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:
حملاتی علیه ایران انجام خواهد شد و ما با قدرت به آنها ضربه خواهیم زد
@WarRoom</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/19994" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19993">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/19993" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19992">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اسپانیا پخش اذان از بلندگو رو در بعضی از شهرها مجاز اعلام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/19992" target="_blank">📅 15:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19991">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری رژیم فارس: تنگه هرمز بسته بسته است، دیگه از این بسته‌تر نمیشه.
@WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/19991" target="_blank">📅 14:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19990">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هم اکنون هشدار های حمله موشکی/پهپادی در تلفن های شهروندان اردن نمایش داده می شود
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/19990" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19989">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز: فرماندهان سنتکام در حال بررسی امکان توقیف تلفن همراه سربازان آمریکایی جهت عدم انتشار تصاویر خسارات ها هستند
ژنرال براد کوپر، فرمانده ستاد مرکزی فرماندهی ایالات متحده (CENTCOM)، به نیروهای آمریکایی مستقر در خاورمیانه هشدار داده است که ویدیوهای ضبط شده با تلفن همراه و منتشر شده در اینترنت، به ایران کمک می‌کند تا میزان اثربخشی حملات خود را ارزیابی کرده و موقعیت‌های نظامی آمریکا را شناسایی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/19989" target="_blank">📅 14:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19987">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ed6y7I2P-gSsrdPShtHAQBmB3aZbfD4t1ET_3ubcVh_PUcceUHpiydK_KBLdJAJ26j4z90lqklcEEhmZktLw6HyMOWBMxyf73QPbPF7l23zZ-AqKMlhJtT0s46_0-D6cfiAQLkXEgiNZYOOFgU8svAE7qY_RVVrmyL5qdcEoHvbQIZ-2nXSzIFj1Cjdj9bdrqUqs-9WqK3xh97m8ZYr6C7-D6saW0PZ-3ZeA2RW7U-n6_QL_WdeVd-iQ4B5cGcvVxkamKa2RJCoYS3Ek5abtIk9cDg2hPSl7-q3caIJ5LFE4fxYtrYxgnIrf-J0-G_s6XTBytV--ZAyDvLx9o1yhhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzzbRyjCB3Bu75JNzzr_Kr-Rm6yf07El4vCB2utcjKGVTWCCCkwlVSTEADp45ZBQ4-DTK87eepexG15DsJnjPfux8CwmB6rydRWBOkBhLP40vWUM3f_TCocDjLy2v1aHBjWltPf1pSwd2I2y480FqShVjLHbY_CfGZcv-iXHe5RaqidCYf47DhlO_DF3kFOZx0A3Q3JEUXWIBVeuNps2v1tTA7x6qBBEIjBMW5kQQZLLU3BhriNv3tTyTq7xlh3nM6HdZEBho31fHQamiOtgAtEYSPVBJUNUJQQJiihJ7uOOdxL2QNYRHdYQIR9tU8cPBqVcULyEUgOruYZonw3Jdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمله به شمال ایران ساحل خزر شهر
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/19987" target="_blank">📅 14:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19986">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش های تایید نشده رسانه های بومی و مردمی در خصوص حمله هوای به نوار مرزی پیرانشهر در ایران  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/19986" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19985">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تصمیم‌گیری در مورد ایران
کاخ سفید اعلام کرد که ترامپ امروز ساعت 18:30 به وقت تهران یک جلسه اطلاعاتی مهم خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/19985" target="_blank">📅 14:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19984">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">زلنسکی به اکسیوس :  رابطه‌ام با ترامپ خیلی بهتر و سازنده‌تره ، مثل قبل دیگه این‌قدر احساسی نیست
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/19984" target="_blank">📅 13:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19983">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش های تایید نشده رسانه های بومی و مردمی در خصوص حمله هوای به نوار مرزی پیرانشهر در ایران
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19983" target="_blank">📅 13:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19982">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش انفجار در عراق و اردن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19982" target="_blank">📅 13:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19981">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش‌ تایید نشده شنیده شدن صدای پرتاب موشک از ‌کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19981" target="_blank">📅 13:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19980">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مشاور ارشد ترامپ: "ایران می‌خواهد حزب‌الله در لبنان فعال بماند، ما اجازه این کار را نخواهیم داد."
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19980" target="_blank">📅 13:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19979">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVMj_Wibe7bc1EdMsZODQOM_kP5jHhGIDIHd3uXq-DBNeFAw_N-1lNVDgasWvpDe3E_2-BfT8_ai-Iw3yMLADDXFKBYSY2XOnU3aYikz_YW66xPmey76060sw7mYnfC4YSqO3Gj2-qZHcU4jxDRu95zvpK9Z4JvBJA_6hMtnJX03qNXXwzucaKe-gyMFEgC99_WYVlNjoPydzCUyikld6OqDD6n-D_F3eVIYrL-HhdjqusK771EZA1tmqdS0oEzg9ykHEBiSJmn3xQnD5DEF8jWs65rNUcBY_oUXVlMExZB7ae_ZsBkmzm4MhVKW55bskqHLd1KRTRXXOwSD096nig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این عکس نوشت : شاهزاده رضا پهلوی، ولیعهد ایران، با شرکت در مراسم یادبود سناتور لیندسی گراهام، به نمایندگی از ده‌ها میلیون ایرانی که برای آینده‌ای آزاد و دموکراتیک مبارزه می‌کنند، ادای احترام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19979" target="_blank">📅 13:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19978">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fklR0OMjLt5FMKmFrI71HlSn4mStcXgs8XdLGg3Y-kUyoiIknXVtfe-ywOAqa8UaZ85ToGogEK5zCijtJqfNN7DNNJ8QvTyOw8MdMKvpXMhjWu0hkjjp3eXUNeBHhvLKf-5xG5-VOjRJ-eiIOm4Xh1FqulN1MT42h7JJU5jvviN50Ct8pj6gJrF3ycJWzA7jvTmEMCG0A87YluBcvdMOi7xfgX0QHGkJ9SHKF78Mti7WVhCV4ZuPCWTA864xidNjFI6xTOduwWn5rLI4rARIgPF7oGI2Kuzo-2ZcPrVWhl6q_Yr_ZE9ryqiuOHyt5FZOv6GZD9fQ5cR8HjNzzsjUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ حضور شاهنشاه آریامهر، ریچارد نیکسون، شارل دوگل و بودوئن، پادشاه بلژیک، در مراسم خاکسپاری رئیس‌جمهور ایالات متحده، دوایت آیزنهاور، که در تاریخ ۳۱ مارس ۱۹۶۹ در کلیسای جامع ملی واشنگتن برگزار شد…
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19978" target="_blank">📅 13:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19977">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏استیو استکلو، خبرنگار ارشد رویترز و برنده سه جایزه معتبر پولیتزر در گفتگو با شاهزاده رضا پهلوی و گفتگو دیگر تکمیلی او با بی بی سی فارسی @WarRoom وی در این مصاحبه به نکات بسیار ریزی اشاره و خودش همچنان اذعان میکند که شاهزاده را به چالش کشیده و وی خیلی مسلط…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19977" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19975">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏استیو استکلو، خبرنگار ارشد رویترز و برنده سه جایزه معتبر پولیتزر در گفتگو با شاهزاده رضا پهلوی و گفتگو دیگر تکمیلی او با بی بی سی فارسی
@WarRoom
وی در این مصاحبه به نکات بسیار ریزی اشاره و خودش همچنان اذعان میکند که شاهزاده را به چالش کشیده و وی خیلی مسلط و با تجربه به او پاسخ داده.</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19975" target="_blank">📅 12:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19974">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الحشد الشعبی: بر اساس آمار اولیه، دست کم ۲۰ مجاهد کشته و ۳۲ نفر دیگر زخمی شدند. این آمار مربوط به حملاتی است که توسط ائتلاف آمریکا و عربستان سعودی انجام شد و تعدادی از مقر‌های رسمی الحشد الشعبی را در چندین استان عراق هدف قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19974" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19973">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش‌ تایید نشده شنیده شدن صدای پرتاب موشک از ‌کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19973" target="_blank">📅 11:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19972">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromElahe</strong></div>
<div class="tg-text">سلام وقتتون بخیر
شما که انتقاد میزارین تو چنل
لطفا لطفا قدردانی ماهم بزارین از این همه تلاش ها و اخبار کامل درستتون خسته نباشید به امید دیدار در میدان آزادی عمو یاشار
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19972" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19971">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff38dea688.mp4?token=f9k1gsPs2xyaSkzio0EhjouYF0kQEAXEvksNNUlWgqBFvfW8ysb3CQjIECULAf9nliA4tDPk4TOovOn5PsGU4BSBpbNJoNA86K7PVeTQmwLuUR8UDbsy7Rq0kECHwvNlI-KeRzRqGyE-R4FZdTEu3AbCtIU4kv_JeVqcgJgibb5ky-2Q2EWjW8UPv1xQmK-scVNUcFRypKF1DWswYPUloFOmUWgZy6mSBO2TNjcrNU4TogTCgeLMuJcwdohpKXIiXWuq_wF4ElDoSS9Upu1NWDmloLs5znpkYIgtM1bs6XG-sa7Bqod4_QTgHacyeTOSnLzgxQ8gLOrPQKq6zQY4q6dQg_Hddz6ocvwGOhKw6OukErSSRNK5q42X7i85VfsopHM_Do2SriWJng7mBpLnlN8qEs62uwNBQTbQl69qDgREVnsIhoqNroIpYde2pjqRGewfM0od_fW7LV3WqY7ukKs8aUPY6clfcGeBvQajbnTrMFpg17P2mMvB486X3aY2QISL8lSfD4UKwNNFdla7YBzdkTWY6IDPdDQpRSKbp9lUz80OFTIhH-5pPTIhef-X2eL1lHL95dyoOWmVQ-O1zjK_vL8Sylz0XdMUuJ2c6HN2a1X8vXMqTNalmkilStnKXxwerFKSY2cgl6BppIxwk3yDr6aM8tKIbsUVoRGF658" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff38dea688.mp4?token=f9k1gsPs2xyaSkzio0EhjouYF0kQEAXEvksNNUlWgqBFvfW8ysb3CQjIECULAf9nliA4tDPk4TOovOn5PsGU4BSBpbNJoNA86K7PVeTQmwLuUR8UDbsy7Rq0kECHwvNlI-KeRzRqGyE-R4FZdTEu3AbCtIU4kv_JeVqcgJgibb5ky-2Q2EWjW8UPv1xQmK-scVNUcFRypKF1DWswYPUloFOmUWgZy6mSBO2TNjcrNU4TogTCgeLMuJcwdohpKXIiXWuq_wF4ElDoSS9Upu1NWDmloLs5znpkYIgtM1bs6XG-sa7Bqod4_QTgHacyeTOSnLzgxQ8gLOrPQKq6zQY4q6dQg_Hddz6ocvwGOhKw6OukErSSRNK5q42X7i85VfsopHM_Do2SriWJng7mBpLnlN8qEs62uwNBQTbQl69qDgREVnsIhoqNroIpYde2pjqRGewfM0od_fW7LV3WqY7ukKs8aUPY6clfcGeBvQajbnTrMFpg17P2mMvB486X3aY2QISL8lSfD4UKwNNFdla7YBzdkTWY6IDPdDQpRSKbp9lUz80OFTIhH-5pPTIhef-X2eL1lHL95dyoOWmVQ-O1zjK_vL8Sylz0XdMUuJ2c6HN2a1X8vXMqTNalmkilStnKXxwerFKSY2cgl6BppIxwk3yDr6aM8tKIbsUVoRGF658" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به فاکس نیوز:
"به این رژیم نگاه کنید. به عربستان سعودی، کویت، بحرین و امارات متحده عربی حمله می‌کند.
ده‌ها هزار نفر از شهروندان خود را به قتل رسانده و معلول کرده است.
این کاری است که وقتی سلاح هسته‌ای ندارد انجام می‌دهد.
حالا تصور کنید که اگر سلاح هسته‌ای داشتند، با جهان چه می‌کردند."
مشکل عمیق‌تر این است که همین منطق هرگز پایانی را مجاز نمی‌داند.
رفتار بد ایران ثابت می‌کند که نمی‌تواند بمب داشته باشد؛ امضای توافق توسط ایران ثابت می‌کند که در حال خرید زمان است.هر نتیجه‌ای فقط به فشار بیشتر منجر می‌شود. من در مورد توافق با ایران شک دارم و این را آشکارا می‌گویم
‏هر بار که توافق نزدیک است، تندروها می‌آیند و به کشتی‌ها در تنگه هرمز حمله می‌کنند.موضع ترامپ بسیار واضح است و ما تعهد مشترکی داریم. ما نمی‌خواهیم ایران سلاح هسته‌ای داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19971" target="_blank">📅 10:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19970">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe5166c98.mp4?token=OjkEeSy-IO3uvr4MzMTNevUPC_ZGkjTW1OEVcHflvDr3Wo4U736Yh6mLBRCrvc1AX91WGKFipKgrXh4-annNRYjEnVlR2K6PY0NHFoJd_MI3PP_nNT727416lFnJcQvwhE3TOVaRdRXBVK9eonZdi8WT7AZRNz0DDh2BU1ZnfuXt2MJ5VwGBeSfwIqLAXp9hvgqyqYHmh-MwLpf1I4Mk-j-f2nxQTqpj9EbtJV3hdTHyCmPlrIFJTutJVT1bVAk4WRsv6HJ5fmScLxhUA_Qkt6pgPz0oqmipRJwaApO5qz3OJILuir1e2tiRKy20muN9S464Sz7fzvL7gyw0yCGgMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe5166c98.mp4?token=OjkEeSy-IO3uvr4MzMTNevUPC_ZGkjTW1OEVcHflvDr3Wo4U736Yh6mLBRCrvc1AX91WGKFipKgrXh4-annNRYjEnVlR2K6PY0NHFoJd_MI3PP_nNT727416lFnJcQvwhE3TOVaRdRXBVK9eonZdi8WT7AZRNz0DDh2BU1ZnfuXt2MJ5VwGBeSfwIqLAXp9hvgqyqYHmh-MwLpf1I4Mk-j-f2nxQTqpj9EbtJV3hdTHyCmPlrIFJTutJVT1bVAk4WRsv6HJ5fmScLxhUA_Qkt6pgPz0oqmipRJwaApO5qz3OJILuir1e2tiRKy20muN9S464Sz7fzvL7gyw0yCGgMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنا با ۸۶ رأی موافق در مقابل ۱۲ رأی مخالف، لایحه تحریم‌های دو حزبی روسیه و ایران را که توسط سناتور فقید لیندسی گراهام مطرح شده بود، تصویب کرد.
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19970" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19969">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رویترز: انتظار می‌رود ایران در چند هفته آینده، اولین محموله از تا ۴۰۰ سیستم دفاع هوایی قابل حمل چینی (MANPADS) را دریافت کند. ارزش این معامله حدود ۶۰ تا ۷۰ میلیون دلار تخمین زده می‌شود. طبق گزارش‌ها، این سیستم‌ها شامل مدل‌های QW-12 و FN-16 هستند و هدف از آن‌ها بهبود توانایی ایران در مقابله با هواپیماها، هلیکوپترها و پهپادها در ارتفاع پایین است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19969" target="_blank">📅 10:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19968">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نیویورک تایمز: ایران به این فکر کرده بود که یک حمله موشکی نمادین به یک بندر اوکراینی در دریای سیاه انجام دهد، پس از آنکه گزارش‌هایی منتشر شد مبنی بر اینکه اوکراین یک کشتی باری ایرانی را در دریای خزر مورد اصابت قرار داده است.‏
به گفته مقامات ایرانی و غربی، تلاش‌های دیپلماتیک تاکنون از تشدید تنش‌ها جلوگیری کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19968" target="_blank">📅 09:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19967">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حکومت ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19967" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19966">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc30Nf7Bau-MJoo3svDD_MozNb9dHTSVL-_otY2VFeJrTkSYW6_0SPqS7SvfJGuTQF65VSTnoSSBhrw_38JDK6V8psU6oSHXiasiW38vqrZzDvyhvMd0MqP3m0jyD8HNB47ZTQ_UAfESv-WswDkcubiOkXB9xHqP53hg1uUEgCvxZkxuivZwWkNrKHnDzFyj69SqFZMnhGBsWSBqMaYy3izFHa_LbRlz67wr3vOhvuUVwn2obq5kWqwPu7so82F628zQnCNUHWSp_GM7RSDkuhUBX0u8cRFgNcaC0-kY99RvZ9gm0oCAzmIfmEVrn72DO8nzkVEKHD228vZ1Pk_dFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی جمهوری اسلامی اعلام می‌کند که پیکر سرتیپ خلبان مجید کاظمی، خلبان یکی از بمب‌افکن‌های تاکتیکی Su-24MK که در تاریخ ۲ مارس توسط جنگنده‌های ابابیل F-15QA نیروی هوایی قطر در حین تلاش برای حمله به پایگاه هوایی العدید سرنگون شد، پیدا شده و ظرف چند ساعت آینده به ایران بازگردانده خواهد شد.
نیروی هوایی جمهوری اسلامی افزود که مقامات ایرانی همچنان در تلاش برای تعیین محل سه خلبان دیگر Su-24MK سرنگون شده هستند و جزئیات مراسم تشییع جنازه مجید کاظمی متعاقباً اعلام خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19966" target="_blank">📅 09:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19965">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b466899a00.mp4?token=c1cxGKndC37qkQCiRBuILiQz4pDKWZOkEKDliUiZ0dOvn1g0it_jXJcyAlDe9nuJn5ELZa4TiweaSSCjmhsVM4PLcQizT-CIrXK18FDm1jKzxT0pKkIgLgsG9CnhNChybF-tVEz7L1GeWex0iEcGbt0iaisLsekckWq1nisS4ANJK_gdZxDfHwG2MU5AJCSm-TreaormTzLq10WsC0za52bXsJ8WtPXuz9hCM6WWg5dkIid5df1WtEh70esIUefC310TWV9q9dcDRddbKpF3yYMpzveOKl64ItNbQohDW4C7MdxmBQGAP2xvV3Ez3xxwIWWRkEDAHNjhLMC_GnESCT21KhEYBcxUPfsmfVbqkHm7zG-YEFR2-xaDCNm6uCmimWRA8LG_8D-OGXR9245c75wJOMylK2ZaCfag1lmUSY6cKgImAxc8t3sVcP0ZgD-mwOzumklHXJLVPwRcogyXmBBNTHM-7msX6DIFqaigcu9zLnOZ3txQ6Wjk0AiHRTF_kDqupUngCMu-PhY3Jdrr7BTHkCqtyIy3cftwCOzSKYPxrhu-MkJRgOgHaqU2DpgCDTrgCYWdXWd_1uWp9Y_bvUSE8uke-k_AAngaQYsYnKfgEwOn87BHchaULUAGcOjtlnSIHqtCiHIuPWKwRo7BN8hoXeKbVV4n5qe8P8kGWZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b466899a00.mp4?token=c1cxGKndC37qkQCiRBuILiQz4pDKWZOkEKDliUiZ0dOvn1g0it_jXJcyAlDe9nuJn5ELZa4TiweaSSCjmhsVM4PLcQizT-CIrXK18FDm1jKzxT0pKkIgLgsG9CnhNChybF-tVEz7L1GeWex0iEcGbt0iaisLsekckWq1nisS4ANJK_gdZxDfHwG2MU5AJCSm-TreaormTzLq10WsC0za52bXsJ8WtPXuz9hCM6WWg5dkIid5df1WtEh70esIUefC310TWV9q9dcDRddbKpF3yYMpzveOKl64ItNbQohDW4C7MdxmBQGAP2xvV3Ez3xxwIWWRkEDAHNjhLMC_GnESCT21KhEYBcxUPfsmfVbqkHm7zG-YEFR2-xaDCNm6uCmimWRA8LG_8D-OGXR9245c75wJOMylK2ZaCfag1lmUSY6cKgImAxc8t3sVcP0ZgD-mwOzumklHXJLVPwRcogyXmBBNTHM-7msX6DIFqaigcu9zLnOZ3txQ6Wjk0AiHRTF_kDqupUngCMu-PhY3Jdrr7BTHkCqtyIy3cftwCOzSKYPxrhu-MkJRgOgHaqU2DpgCDTrgCYWdXWd_1uWp9Y_bvUSE8uke-k_AAngaQYsYnKfgEwOn87BHchaULUAGcOjtlnSIHqtCiHIuPWKwRo7BN8hoXeKbVV4n5qe8P8kGWZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید و پر معنی کاخ سفید
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19965" target="_blank">📅 09:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19964">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bf785ac3.mp4?token=rSuVLjAJUcNeGwXzvSxXSqtX6H9vk3KJe6RHHVQYsIg4hUjoKEVonf5s3K00M7XuktREa3l4-8fkn6Mb1mVeoL0i2FMv4V91hRekO5zwSp9cFDNpn6pZhOJXaZj3RrVdSLzYd6flvlZoQWZgULX3gcK0wK_Vp48GNdTzYN84Wl076fbl0KR5usNCfYvhk-YZdEgXhF2Zjyoc3pdoPbh1HsoDNAAUQsqP4dSiIBnKEETvOafJ-01gtzENp5dc9CqVK0uibqNTsQrVG3uJFQ0m0osXqgHnrlHKrcskvw0GVwWAwEbhMGBOIIkvm-mys8lngZqfKfc9X-xxluaDDaHQqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bf785ac3.mp4?token=rSuVLjAJUcNeGwXzvSxXSqtX6H9vk3KJe6RHHVQYsIg4hUjoKEVonf5s3K00M7XuktREa3l4-8fkn6Mb1mVeoL0i2FMv4V91hRekO5zwSp9cFDNpn6pZhOJXaZj3RrVdSLzYd6flvlZoQWZgULX3gcK0wK_Vp48GNdTzYN84Wl076fbl0KR5usNCfYvhk-YZdEgXhF2Zjyoc3pdoPbh1HsoDNAAUQsqP4dSiIBnKEETvOafJ-01gtzENp5dc9CqVK0uibqNTsQrVG3uJFQ0m0osXqgHnrlHKrcskvw0GVwWAwEbhMGBOIIkvm-mys8lngZqfKfc9X-xxluaDDaHQqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به فاکس درباره ایران گفت:
آن‌ها باید بدانند که اگر به ما حمله کنند، ما با قدرتی بسیار شدید پاسخ خواهیم داد. آن‌ها در درگیری‌های اخیر به ما حمله نکردند، به خاطر همان چیزی که همین الان گفتم.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19964" target="_blank">📅 09:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19963">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏گروه تروریستی سپاه پاسداران مدعی شد که در ادامه تشدید درگیری‌ها، سه نفتکش را در تنگه هرمز با حملات موشکی و پهپادی هدف قرار داده است. بر اساس این ادعا، نفتکش‌ها پس از اصابت متوقف شده‌اند. این ادعا تاکنون از سوی منابع مستقل، شرکت‌های کشتیرانی یا مقامات بین‌المللی تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19963" target="_blank">📅 09:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19962">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سنتکام : ما و نیروهای مسلح عربستان سعودی در ۲۸ ژوئیه حملات دقیقی را در عراق علیه تروریست‌های همسو با ایران انجام دادند که سپاه پاسداران انقلاب اسلامی (IRGC) آنها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان سعودی هدایت کرده بود.
جنگنده‌های ایالات متحده و عربستان سعودی در پاسخی قوی به بیش از ۳۰ حمله پهپادی هوایی به رهبری سپاه پاسداران در ۷۲ ساعت گذشته، چندین سایت لجستیکی و تسلیحاتی تروریست‌ها را در سراسر شرق عراق هدف قرار دادند.
این حملات بی‌دلیل علیه نیروهای آمریکایی موفقیت‌آمیز نبود.
از فوریه تا آوریل ۲۰۲۶، بیش از ۶۰۰ حمله ناموفق به شهروندان و تأسیسات آمریکایی توسط شبه‌نظامیان تروریست همسو با ایران در عراق صورت گرفته است. سپاه پاسداران و گروه‌های تروریستی نیابتی آن باید این حملات را متوقف کنند تا از واکنش نظامی بیشتر ایالات متحده جلوگیری شود.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19962" target="_blank">📅 09:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19961">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عربستان : عملیات ریاض علیه عراق با هماهنگی سنتکام انجام شد
این حملات در پاسخ به حملات پهپادی گروه‌های وابسته به ایران در عراق علیه تأسیسات نفتی عربستان صورت گرفته
ریاض برای کاهش تنش‌ها در منطقه تلاش می‌کرد، اما این گروه‌ها ادامه اقدامات خود، مسیر تشدید تنش را برگزیدند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19961" target="_blank">📅 09:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19960">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بصره عراق مورد حمله نظامی از سوی عربستان سعودی قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19960" target="_blank">📅 03:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19959">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجار انبار مهمات در مقر فرماندهی عملیات حشد شعبی، بصره
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19959" target="_blank">📅 02:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19958">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ایرنا:
سنتکام دروغگوعه، تمام موشک‌های ما اصابت داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19958" target="_blank">📅 02:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19957">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">صدای جنگنده از کیش به سمت جنوب ایران
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19957" target="_blank">📅 02:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19956">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسانه های داخلی : به اربیل عراق حمله پهپادی شده و جنگنده‌های آمریکایی بلند شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19956" target="_blank">📅 02:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19955">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اخبار حاکی از فعال‌سازی سیستم دفاعی "پتریوت" در آسمان جمهوری آذربایجان، کشور همسایه ایران، است.(تایید نشده هست)
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19955" target="_blank">📅 02:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19954">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yk7QdXrjclYjuIiFCD9RhBZ-Njx35yLsfostBSCFp_K95FLagHq0YBzC65vkqt2O1-XyAKEtUToMDt6UF1Nxt5dgiSWCvaeImT-6adQE93_2lwFh2zPNZu7Iv-vMqA2BPKaFcE3yxCTT9UEFAIauLbyruqgJ3C9g3z99qozCEDFfPVIw3aDbK6ItmXH0EBg3VqRuXe_In8SxH9cTGUVMVHb3Pb1xTgiTHgLXaHEFAnyMM0j-Tu7KEmVKg3_khan28FX9px5MBEa8G_0b2FpLdxksJjbukXL9wO8zxEifGzS5X4Q1f3UKt6cFXpW5VzCCDFgj1XtqjMKflfqoPNVvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاهی به برد موشک های سپاه به اکراین
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19954" target="_blank">📅 02:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19953">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سپاه به اربیل عراق حملات سنگین موشکی/پهپادی کرد و چندین انفجار تو اربیل شنیده شده
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19953" target="_blank">📅 02:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19952">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اتاق جنگ با یاشار : دربون جهنم سابقه نداشت خبر از حمله سپاه بزنه! بدجور برد کوپر بد خواب شده ، مادر بگرید
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19952" target="_blank">📅 02:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19951">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمانده سنتکام بردلی کوپر رو از خواب بیدار کردند
👺</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19951" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19950">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">منبع آمریکایی به شبکه i24NEWS گفت که جمهوری اسلامی حداقل 4 موشک بالستیک به سمت یک پایگاه آمریکایی در اردن شلیک کرده است و این اقدام را یک "حمله بزرگ" توصیف کرد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19950" target="_blank">📅 01:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19949">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چنل و اینستاگرام رو فردا پرایویت میکنم یه مدت ، اگه فالو ندارید فالو کنید نمونین پشت در پیش عرزشی ها
t.me/WarRoom
instagram.com/yashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19949" target="_blank">📅 01:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19948">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">من نمیدونم رسانه ها برای اینکه جو بدن چرا اطلاعات غلط میدن مردم اصلا آتش بسی نبود که بخواد نقض بشه. یه حمله شد، یه جوابی داده نشد. یه طرف کوتاه اومد، ادامه نداد! الان جواب اومده جواب داده
😁
چون نفت داشت میومد پایین فشاری شدن
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19948" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19947">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مقام ارشد آمریکایی: ایران موشک‌هایی را به سمت پایگاه آمریکایی در اردن شلیک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19947" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19946">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمانده سنتکام بردلی کوپر رو از خواب بیدار کردند
👺</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19946" target="_blank">📅 01:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19945">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پرتاب موشک جدید از غرب ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19945" target="_blank">📅 01:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19944">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش‌های تایید نشده از اصابت یک موشک به مرز اردن و اسرائیل و پایگاه آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19944" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19943">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87354e52d8.mp4?token=HZo_adqH3slYdcrmkpJZAfY18mrkjuaIxyBWGfUWWnFwAJhXBbLMXXwpLaoDbpVacjjnBHOeAU5wdEra2kdMQDeidFyGHDqx808eQ8zBoje9ZvucGHQO1K-UPrWl6nHgUuRiW45ppFuLfoAjZaMliDQWkZO666-lk5FPgX9-uBdxzjZHdZ8dRb2bV-UGcZ0E1kpJW5UHtk9_wIpV0uj5LpbrmhosAVjRnMS5U6JYqXcoHJo_LkzPZMedz0IvDGR0Z7gCO6Y6L4DconvAczdLDhvAqZpOjxCCRRmZNC54ldeX5Vw2qZvQt-r6IX95PuEhad9jzaDOCpI-fNBVtX26Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87354e52d8.mp4?token=HZo_adqH3slYdcrmkpJZAfY18mrkjuaIxyBWGfUWWnFwAJhXBbLMXXwpLaoDbpVacjjnBHOeAU5wdEra2kdMQDeidFyGHDqx808eQ8zBoje9ZvucGHQO1K-UPrWl6nHgUuRiW45ppFuLfoAjZaMliDQWkZO666-lk5FPgX9-uBdxzjZHdZ8dRb2bV-UGcZ0E1kpJW5UHtk9_wIpV0uj5LpbrmhosAVjRnMS5U6JYqXcoHJo_LkzPZMedz0IvDGR0Z7gCO6Y6L4DconvAczdLDhvAqZpOjxCCRRmZNC54ldeX5Vw2qZvQt-r6IX95PuEhad9jzaDOCpI-fNBVtX26Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان اردن ، پدافند درگیر شده
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19943" target="_blank">📅 01:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19942">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snTvqnvU7zEaP8Dye5jD5ROHL44ziJ_oOYF1q_ol9fYo3M3bDV3fsopUaZh3_yUFGEGn9keGOLF3B55GJirPb6xYMCZ7CazXB945TXcQFBGoS-oOAB1WX3WBor2yZ1wYCz4410dbr1yi_RBtAb8Xt6TJnLfcqbekxXNil04dFTokI8seu07I6lHFIa5R8G3jDlf2xfZCEqbpTx9H2wmFDF1mbh93clmue5DjLKVaKyAhLHTaykin9zm_5jYYZPKo79DQ_y52CDD1q7KxIzvcgTj9yuStRdnCXbyCY5hurcir4nRZN4T2VU_LDs4y83cepAOPAlTZOU1Vz-mENFEXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر موشک ها
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19942" target="_blank">📅 01:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19941">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فک کنم نتانیاهو با گوشی ترامپ به مم باقر فحش ناموسی داد</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19941" target="_blank">📅 01:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19940">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z53v6QWpVluAAgdrplmH1eZ8cKZNzhCBcBegz0t5I9YQam1axeZHAksACbmC8opcyb7kV-MvVNJFO_i9ai7z4pknhMI6X6ghrgQgTYR0xCZxtXqLjoetmFyUiDw7iUHy7OzOq9BPaOlHYdIRjsjKW8_wV4GEVz0GPGsuQtXF79Jw1VJ0VeOdFniwMX1vRRKDua69WRn_X5do7Utf_MJnmwK62ph_y0UQxk6OygXARoxrKiQGiPE3af_c8MZhlqgnvgi4Ab1RiSuLnrJZR4OyKicuG2u68GzhbpoGK97ghgnLemh5Y0js8iy6iQWKWH3Sny29eHG-fxyf6VGkF2aQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک ها در آسمان خرم آباد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19940" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19939">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آلارم اردن فعال شد
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19939" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19937">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4jJQ5O4jRZBHDaBSo7GzpkcGY9D-Q2duV4tmSPqst1LRPpzfbln9kEMEB6z_-LL7A7wuuCyWSnxQMLhhGVD2hxb7J9cAwksUNbCtbPHf2lF1GKIObRVO77ZciFlP3q1KO56y9Qa3ZSl5lORP-z_yxv1O2fcWgLrmrljlOA3yeRqvVkXQX7gGgP-84h9Al4UpsHf7xhO17f52af7QgOyUvSTeAiQ3ODMN8S4KIxM-b_huxoUFj0DoXbw3MCqe03LMNBij_qWxcyXN-DE9245tquAoVSQihOnodAjSXHzSW1vJyRD2MLT6PsCudrDwmc9VBVTo7zE-fzVO1kbd6N7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-IkhPqbHqwCtQjEl22bS1c8zEtiBhUv-UNRAL8_OpKOHGnxpfQhlHrKr_AAJqukRbocYnibuKZB1TAOdEg8uU4C86xkIXOuCrNwdrquoZj_W5AkiZ7726PUXuG0HDa2isalEmqKA-pBjgmxgvYkV8yvZzI64dh-ju3ikJXVJISBz5LxIiX1Nf_rfSQxLy8vltkLeOiBEPTHYXB6y8b_zWXP6YAyOvJSbv6ysQH0tAJQ_Ddcf_Fc6owinEvYoc6duRfPex5CsYrPzdfZgGxCDmY7RoiX7MWHi5mcITa9ixHHm75UzvqypDw1TlNtwBifHk_-G4ATh5eWXFWLqXiyAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شلیک ۳ موشک از خمین به اردن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19937" target="_blank">📅 01:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19936">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کانال i24 عبری : تنها چیزی که ترامپ را به سمت امضای توافق با ایران سوق داد، قیمت نفت بود.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19936" target="_blank">📅 01:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19935">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ddcbdc52.mp4?token=JJ-XkEQciUHsXk9qEN-ArIeXDKAFHDD_9jqX32CznBvpRQjpbSOxyEr6dP3uD-xdoxPIL6SqbZqtR3S9_u6QmTBfs-mpSLRyQq_Ue51bpMq6pLK2g7mwmnPgzhO1Ffv9BdjB38v4aoJM8QGU2MjOKZEsKKRuPyM2DgBMcQ7ZFr0LxYJ4Nsb7IIq8OCmJg72kyN_ylH7XKCrn8G8NK-w49A92EnKA9S_9HOaFemdEYUgqbuFVn8-m4RwPY2iHq2oAOtE8iR36bZKCa_SH35rWIS3WXh0XcztLCCdRcttZJ6TvsyCzjZUXfgocvUvZH-KuhFfxCKARO5pgWLEDoc5ixllRJo9BlxiLzRrUTzWGzSBTnoWtp2HSjNl_YtMoB2NaSHWeOGKjHAXbriHWQhXT9PwTbbnBQkdau4FS-krfIgCNkFI0epuum4AmTuHgstRgua-kkADR_y97FQAfBa--lFGiuShqwsdXZKiVHSrXUppwtl1MT_PsQRZlMMUsD503MR3hdmhXaa4tO9w8PhgYQYAEmmAn3uSI2alTdbpNrj298KliaLeuvh40jIunvEYSiI6cwX1P9mBT-yXpzHbALqhAAwBOaJgTv2EpJRtfZmLycnvgQWWcrxdTDBoCZE4o_HxMbNf7EYk89PO0fW_qvKkPs_GIlkeqY8ifXAaeQGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ddcbdc52.mp4?token=JJ-XkEQciUHsXk9qEN-ArIeXDKAFHDD_9jqX32CznBvpRQjpbSOxyEr6dP3uD-xdoxPIL6SqbZqtR3S9_u6QmTBfs-mpSLRyQq_Ue51bpMq6pLK2g7mwmnPgzhO1Ffv9BdjB38v4aoJM8QGU2MjOKZEsKKRuPyM2DgBMcQ7ZFr0LxYJ4Nsb7IIq8OCmJg72kyN_ylH7XKCrn8G8NK-w49A92EnKA9S_9HOaFemdEYUgqbuFVn8-m4RwPY2iHq2oAOtE8iR36bZKCa_SH35rWIS3WXh0XcztLCCdRcttZJ6TvsyCzjZUXfgocvUvZH-KuhFfxCKARO5pgWLEDoc5ixllRJo9BlxiLzRrUTzWGzSBTnoWtp2HSjNl_YtMoB2NaSHWeOGKjHAXbriHWQhXT9PwTbbnBQkdau4FS-krfIgCNkFI0epuum4AmTuHgstRgua-kkADR_y97FQAfBa--lFGiuShqwsdXZKiVHSrXUppwtl1MT_PsQRZlMMUsD503MR3hdmhXaa4tO9w8PhgYQYAEmmAn3uSI2alTdbpNrj298KliaLeuvh40jIunvEYSiI6cwX1P9mBT-yXpzHbALqhAAwBOaJgTv2EpJRtfZmLycnvgQWWcrxdTDBoCZE4o_HxMbNf7EYk89PO0fW_qvKkPs_GIlkeqY8ifXAaeQGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: به نظر شما چه صلاحیت‌هایی برای رهبری یک دولت انتقالی در ایران دارید؟
شاهزاده رضا پهلوی: اگر یک وکیل تصمیم بگیرد پرونده‌ای را به صورت رایگان بپذیرد، آیا این به معنای آن است که او شغلی ندارد؟ من چهار دهه است که این کار را داوطلبانه و رایگان انجام می‌دهم، درست است؟ به عنوان فداکاری من برای کشورم.
من می‌توانستم به راحتی در قاهره، زمانی که پدرم فوت کرد، تصمیم بگیرم: "می‌دانی چیست؟ به جهنم." من می‌توانم مانند بسیاری دیگر، زندگی، تجارت یا چیزهای دیگر را دنبال کنم... اما تصمیم گرفتم به خاطر کشورم در آن بمانم.
این یک فداکاری شخصی برای یک عمر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19935" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19934">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba487c3af7.mp4?token=MfcMWm8DLiFNeldtuZQ6yetNEMT_4i4PlSGobtg7lfP8dL1CfEE2oxhC7M-CWdSIOS450xgGfEXU-s1LKzt39X5dBzekTWKG158vnYxRgvHzf0B_oeHmhrmDy06WYO1gqK-SMWi1ydoIqnUBflSD48kFhZCnL-A6pD3dPDjQ0S8bilfPjucnfO_VSBh936k-hB5dMKEyDA-m7B5MnEF7CCD_EQWII1XaO1T-FhNe7T5PpmMjgKRuznCnrJeHyN5jkJYn4YQWTuI2RGceS_we0HJ0STxllThgEX1shWjwgzpQSVdbFzx1vf813YWSNMRPBEb_DTL355dhY4nQhzF8mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba487c3af7.mp4?token=MfcMWm8DLiFNeldtuZQ6yetNEMT_4i4PlSGobtg7lfP8dL1CfEE2oxhC7M-CWdSIOS450xgGfEXU-s1LKzt39X5dBzekTWKG158vnYxRgvHzf0B_oeHmhrmDy06WYO1gqK-SMWi1ydoIqnUBflSD48kFhZCnL-A6pD3dPDjQ0S8bilfPjucnfO_VSBh936k-hB5dMKEyDA-m7B5MnEF7CCD_EQWII1XaO1T-FhNe7T5PpmMjgKRuznCnrJeHyN5jkJYn4YQWTuI2RGceS_we0HJ0STxllThgEX1shWjwgzpQSVdbFzx1vf813YWSNMRPBEb_DTL355dhY4nQhzF8mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: گزارش‌هایی، تقریباً ناشناس، مبنی بر دریافت بودجه از اسرائیل و عربستان سعودی توسط شما وجود دارد. آیا این درست است؟
شاهزاده رضا پهلوی: کاملاً نادرست. من هیچ بودجه دولتی یا عمومی از خارج دریافت نکرده‌ام.
هر ریالی که به کمپین من می‌رسد از کمک‌های خصوصی حامیان است. امیدوارم خیرین بیشتری داشته باشیم که چک‌های بزرگتری به ما بدهند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19934" target="_blank">📅 00:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19932">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رویترز به نقل از یک مسئول آمریکایی: توافقی که در حال بررسی است و مربوط به تنگه هرمز، مربوط به هماهنگی است و شامل هیچ‌گونه عوارض عبوری یا هزینه‌های دیگری نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19932" target="_blank">📅 00:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19931">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4dee73717.mp4?token=nwZKzDtKYsrtx_3YsRytJU0A7miR7dYHlmhA3wmdncJ7mxrNsUd6H-ucKplCzom_e7r8jMy-xmSA0f_2iipd0sm5ur5gBHSYO5HdT_8wVe81fzQRawgtc_CcS0nXTNifF4kKuxeSXnc8kImNsuURblKxTTl4A19p18mc-18Bis77Z7K6GE3nquyNJEkwSozMlC8I8a3lJKbZQLcX2R_3Nmx2t0Dym-s-ZRVwF2rZapl4k6I271_4Cvgprl8wTAYwiYjZkHd0fwrnI9kxXOUFiEI5TQ407IYPGOBUxC-v2_aYxaBnFNWrtPQ43B2vP4DvLZgerhdHC_21g-MdV_PNS4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4dee73717.mp4?token=nwZKzDtKYsrtx_3YsRytJU0A7miR7dYHlmhA3wmdncJ7mxrNsUd6H-ucKplCzom_e7r8jMy-xmSA0f_2iipd0sm5ur5gBHSYO5HdT_8wVe81fzQRawgtc_CcS0nXTNifF4kKuxeSXnc8kImNsuURblKxTTl4A19p18mc-18Bis77Z7K6GE3nquyNJEkwSozMlC8I8a3lJKbZQLcX2R_3Nmx2t0Dym-s-ZRVwF2rZapl4k6I271_4Cvgprl8wTAYwiYjZkHd0fwrnI9kxXOUFiEI5TQ407IYPGOBUxC-v2_aYxaBnFNWrtPQ43B2vP4DvLZgerhdHC_21g-MdV_PNS4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی درباره ایران:
فکر می‌کنم ما به تغییر رژیم بسیار نزدیک هستیم.
رژیم در ضعیف‌ترین وضعیت خود در ۴۷ سال گذشته قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19931" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19930">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2dacc78c5.mp4?token=YnQYaDd2OTmb-tBKoNc2sxUFV8qjRkRST9L0CW5daQUQv_VC72QHSvToQIXwxQ91hLX4dip2131XENxKO9U5VTweBefc846f6yBdUESL9WNi_SXBuyWsMc_nirQEPbqNFLMooJZKpjCG5uWaBeMYneVBBwTYPq4Thvdml8u_qassEggIchNfK-s0DgqXbefRZVX1HQO6h2ByrLeC6_ioR6QIqrsvUtGevyFCsLgT-AvElFtdiyx2qGCz5UJaijOW4lrX-ODth_LjxASvUwj7b31y7tC16xf3kbAti1Vqo63tSPCb2z2wfZ7owbVNo_d-0umsMdf_2g3WjbJ8zoW0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2dacc78c5.mp4?token=YnQYaDd2OTmb-tBKoNc2sxUFV8qjRkRST9L0CW5daQUQv_VC72QHSvToQIXwxQ91hLX4dip2131XENxKO9U5VTweBefc846f6yBdUESL9WNi_SXBuyWsMc_nirQEPbqNFLMooJZKpjCG5uWaBeMYneVBBwTYPq4Thvdml8u_qassEggIchNfK-s0DgqXbefRZVX1HQO6h2ByrLeC6_ioR6QIqrsvUtGevyFCsLgT-AvElFtdiyx2qGCz5UJaijOW4lrX-ODth_LjxASvUwj7b31y7tC16xf3kbAti1Vqo63tSPCb2z2wfZ7owbVNo_d-0umsMdf_2g3WjbJ8zoW0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر واضح از حظور شاهزاده رضا پهلوی در مراسم
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19930" target="_blank">📅 00:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19929">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUhaF8RzNPwGY4vEPDNEl6Ad_4EFrL1CNHFGRwC344f-KX5c-kGEnruV4biYYWNA2hQErdyoojXjbe078oXy_Pw_paoCWmJyHwCJdVJFodNqpU33JPJ8TtGBaCjzgh8qWDQ0SM_wsr7gyAJalJWsYlMR7PglZOs4x77EUb2Xi-qXaiiehA5RdUnE5vGW9olfVxcK9Orys-owM1XC0dPY48MpeJiwpc34DnXaFMP__ZyO6ei4eeDjN2l8S-NsGZCu8hE3nOgqKF7VsxojHJIWdNMEamGI_B6HcZU_R59n6JXUkXyKGu1N1Q1jUOIuyWShIs9_1ILqOidPexeWHnaBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: در حالی که ترامپ مدام از مذاکره با ایران حرف میزنه، طی چند روز اخیر گسترده‌ترین تحرکات نظامی و لجستیکی آمریکا تو منطقه گزارش شده.
به گفته برخی منابع نظامی، آمریکا در حال آماده‌سازی خودش برای یک جنگ تمام‌عیاره!
@WarRoom
اتاق جنگ با یاشار: هم اکنون، در هنگامی که همه در مراسم سناتور فقید لیندسی گراهام هستند، یکی از سنگین‌ترین ترابری های نظامی آمریکا در منطقه انجام می‌شود.</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19929" target="_blank">📅 23:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19928">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تقدیم به نگاه زیباتون ، بشوره ببره
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19928" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19927">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19927" target="_blank">📅 23:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19926">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19926" target="_blank">📅 23:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فاکس‌نیوز:محور اصلی گفت‌وگوهای آمریکا و اسرائیل، تصمیم‌گیری درباره گام‌های بعدی پس از حملات اخیر به ایران بوده.
همچنین نتانیاهو احتمالا اسناد و اطلاعات تازه‌ای ارائه کرده که نشون میده جمهوری اسلامی با وجود صحبت از دیپلماسی، همچنان برنامه هسته‌ای خودش رو پیش می‌بره.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19925" target="_blank">📅 23:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19924" target="_blank">📅 23:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19921">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMliamFeuwm2lCAo5wZtJWdmkY6VdMC-_B8rJRDYu24OikjyRfg21edhZtLwIz_sUpcLXYqeX5nHF_WXh3bgy6qJh59IwGFxhoxNIjcgB4aKxVUSypWnNvGWpYPj8XodjuPEzhOjnjebgTcyelYDk26br0RvLL6EKYVMaKTLOWYArqURymnlR2ZeziUqqCxCivxQCTZw3FBsH9KmvLgFBe6R-D4D12eS8UyuNgl9fJA60nLuRUldmPDaCE90lkmNbiyaEMosuSuAm3IQciurN523NsRtS4Ec0YjMnNyGRHuIVTGkiyK_ha9ZYwfm-vNHIPzKJsBik76konJNNb0Ohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axZTl4o9Ni8RPnBd1hLPh1ef8sKC-SCRQempbE1B0wubEnBr9oEM0v8ZbkwC7VPgu0djaUYTrP5bT_qgxNKsVodOYF0_YsbMpjfHMyZ0VVWxfSw3mqJWfeWeep_B4GiZEMVAzGoCFsTEtYq9RmVzHOsY7OlRk9Qa4eDVCi2zPbjJ8lrOMNsgh-4pzIIOCfrnRKa6EY2aVqw906s35uUlD2M3_Bx5VrHFbsTD6D8zBGTskVfymLVfiEeKK67ASRiras9_uwFtSSje_0fra5eneAOQUXrKqkAgWKghv8IAZSj-eT3rIj1XM8NTV0_gN03gQkKNLr_UAyeLaAa8Icnl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4xHhdFXm3uVoDoteeFQuoEhhjV09x1vP7WrOQq5cj04S8Msk0FXdT4G3MsmzjyFydv_RjGiVD147eysYlR-WM5POFdGTw9ZDsVL_Ay6eDD9fYDiD5rBQJeOE3nHNMNn8N7Wuh1x6I2i6aaQ-jyIKy_5j6p6S_FKTDTkWfqa-BaPnZ9ovKcAtg7NR5GW5Mp8dnnLXVmnsZP6jbvXZsruBQalMi9nw_rqAgQ-oc3WZ_2bj_-w7gcXjxkiT8--fFYPEZiSiy5O9AhT0_0P_s7NpDw7_yO76mrnYlE7luDuU9qvfXoaqwXJM5Ct59XJR_g9fsQ0831PMitqmvEbSjjWfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین تصویر شاهزاده در مراسم درگذشت سناتور فقید لینزی گراهام که با اندکی فاصله سناتور تیم شیهی که صحبتهای جنجالیی درباره ایران در سنا کرده بود و ویدئویش را برای شما گذاشته بودم دیده میشوند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/19921" target="_blank">📅 23:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19919">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEHQP5gyAF-j7C1cTk7sNbObMyPndMfB8GrqKmnmTlF7Lj3j32wdz1pcNxb7pXdGslVYAb-M6ScCjw1t8Vd4LQEoSgH2sP1U1yM7nEly0OhYLA4Mjtw6UulmYv_oYlH7mzoN8YC7EmfE6sPcn6u_T1_mLlmZNgck_GQmBygYgI8HWHKf-Iq_BAUIYlRfieA9naC_ODmnMROenc6JmRS1lV8n2UvXy6TH_lH8_63f98SVnzVnXFyxyCJZYguudRhV6Oddr4opa-NIy6KqLVul-672dW2e9DMXHga0spldd6xackRqWsuJCxLMqgShguBDav3_8UmEuUUbYCJIftJ4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dddx-tlekG14bn4AojEye15dykaJ3_wCpfho0hxDOeKr_aaQbOfpHbA9nLklZ8Ky2CXVeD23YXmmxOimJ4sqmIHeq4e6R_hmTO1c6C0JihUz_CSDJyNXBwdG73ku05bah0F5f_sLvSIyVCKfL7OrXVC7ETOV2keFt6qnqxyfIyfghEWBsyeKXqXZoYJ4N06ftPhUWCdVU1gHa9ZLCSOAO9UdhxToBGikQKsNJ05SH6Vc97XQG9Md-Ioet5Qa3qnxWq2Oi4t9YnIVhXn6ZSNpyQcH9QvmZR-M3bIKxqh6821nYe8225EcPsHhgU8WC-0YDUpwHyFaGhSw55EkmhLEIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهزاده در کنار کامران خوانساری‌نیا در مراسم
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19919" target="_blank">📅 23:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19918">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19918" target="_blank">📅 23:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19911">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اکسیوس:ترامپ و نتانیاهو جلسه‌ای به مدت ۹۰ دقیقه برگزار کردند که به عنوان یک جلسه سازنده توصیف شد و تمرکز آن بر روی ایران بود، بدون اینکه هیچ نشانه‌ای از اختلاف نظر بین آن‌ها دیده شود.
دفتر نتانیاهو تأکید کرد که اسرائیل، واشنگتن را در مورد ایران تحت فشار قرار نمی‌دهد و هر دو طرف در یک هدف مشترک برای جلوگیری از دستیابی تهران به سلاح هسته‌ای، سهیم هستند.
همچنین، دو طرف در مورد امکان عادی‌سازی روابط بین عربستان سعودی و اسرائیل گفتگو کردند. موضوع فروش جنگنده‌های F-35 به ترکیه مطرح نشد و ترامپ از اسرائیل درخواست انصراف از مناطق تحت کنترل خود را نکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/withyashar/19911" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19910">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9ed022ed.mp4?token=lg8X7umzhPRlqXZWg28cwjNfbnMWoe6-wV96L8QlMqAmeY3tkm2IllW7IX6RU3p9HUVIwoVoHby1GfBDnMN71X3-M8_Yj5MlxDQU_MrskbND1TGzPNrzG_4sle65-9vLctxXGnnPjiuI_iypR-PoqFHQfiuyYb-klNvoSzA28izgncdya6ndYugyVFoGWJ_I2g8MfedtF80hKv1Jwn3zQBonL9F_-74ZOZr2NKVVlksT94pXHmfnLZJSekcLNLwGnyxbpFJoipLTpCBxJ1824XCc08cknrTRxq8hrOXVqqF68IAQk-BdDzzaX6g9hygpj1p8FyLcYbFIRbu061JvSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9ed022ed.mp4?token=lg8X7umzhPRlqXZWg28cwjNfbnMWoe6-wV96L8QlMqAmeY3tkm2IllW7IX6RU3p9HUVIwoVoHby1GfBDnMN71X3-M8_Yj5MlxDQU_MrskbND1TGzPNrzG_4sle65-9vLctxXGnnPjiuI_iypR-PoqFHQfiuyYb-klNvoSzA28izgncdya6ndYugyVFoGWJ_I2g8MfedtF80hKv1Jwn3zQBonL9F_-74ZOZr2NKVVlksT94pXHmfnLZJSekcLNLwGnyxbpFJoipLTpCBxJ1824XCc08cknrTRxq8hrOXVqqF68IAQk-BdDzzaX6g9hygpj1p8FyLcYbFIRbu061JvSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره لیندزی گراهام گفت:
او به‌شدت جنگ‌طلب بود.
راستش را بگویم، هیچ جنگی نبود که از آن خوشش نیاید.
فقط دوستان نزدیکش منظورم را می‌فهمند؛
اما او همه این‌ها را برای کشورمان میکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19910" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19909">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک منبع آگاه گفت مهنام نواب صفوی، ۲۲ ساله، خواننده رپ فارسی و از بازداشت‌شدگان انقلاب ملی دی‌ماه، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد به اعدام محکوم شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19909" target="_blank">📅 22:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19908">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwBPyMEfFi-Uf-hhbO72Ti0bUCBLRfUSGT0G0d5vP2pK-3juoXiei1OBu79naTaK2gFDMUT4ahxhMEVQo5jpI8sq7cAOYe7qI3loUr5WrTTNe97EWaWgO4zd05w36g6QGM7COuTh-t0m-uAyCObFOCCKKNJybIGQ2tJ8qoOd4jpsL1MPmGzJvNwNo1ePonVthIPYepk6N5zbLCOSikGj5rbe-LmMBH1eg0s4mPYznKM6dnhtzAn3_nKF4aJDbNa99qvi_911C4hCapebu5T1dT2_fVb1DVzsd3W50FAJwfk8dsbv8Rz0tajNRDZ_HoZGJ3gi5Q95CnEoKdcc7TcnCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز : علی واعظ، مدیر پروژه ایران در گروه بین‌المللی بحران، یک سازمان پیشگیری از درگیری، گفت که پس از ملاقات با رضا پهلوی در ۱۵ سال پیش، به این نتیجه رسیده است که او اشتیاقی برای کشمکش‌های سیاسی لازم برای رهبری تغییر در ایران ندارد و از آن زمان تاکنون هیچ چیز دیدگاه او را تغییر نداده است. اما پهلوی به رویترز گفت: «من از حمایت زیادی در سراسر کشور، در داخل و خارج از ایران، برخوردار هستم.»
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19908" target="_blank">📅 22:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال ۱۲ اسرائیل: نتانیاهو به ترامپ تأکید کرده که حملات بیشتر علیه تأسیسات هسته‌ای بازسازی‌شده ایران حتمی است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19907" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو:من همین الان یک جلسه عالی با رئیس‌جمهور ترامپ داشتم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19906" target="_blank">📅 21:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19905">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">instagram.com/yashar
LIVE NOW !</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19905" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19904">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19904" target="_blank">📅 21:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19903">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19903" target="_blank">📅 21:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19902">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06b2086bda.mp4?token=hPP7-5MnU8hnbtU7uPghJvYTi3F0p4_qPKLi0punGr78WoSrv4aoNL7q9Z2iLMEOE2BFvWskWwCzXD4e-PvU-nUBZl094g6mBEPwo75eAjKeS_obUiO8jXAB9jPK0g264qVz9bAmu6FzY8ZTVMPIcDJ5TfgOX3fp2sYPAny4zpVLb8k650sW7LTddIIAYlUQMY-_qN7WZhpenyzBKs8d6ONMxhbqgRjFBtYY3k5kJJ8d1oJOnDpBwspTuKb5XiESBJi--cyyfmEjKOevnZLA8Gr9RoX1pigC3pl9YWTc7UtC8JYlkRL9UhMg2DLH90Vtt1Kz7KZDqFlC4z1GSVuNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06b2086bda.mp4?token=hPP7-5MnU8hnbtU7uPghJvYTi3F0p4_qPKLi0punGr78WoSrv4aoNL7q9Z2iLMEOE2BFvWskWwCzXD4e-PvU-nUBZl094g6mBEPwo75eAjKeS_obUiO8jXAB9jPK0g264qVz9bAmu6FzY8ZTVMPIcDJ5TfgOX3fp2sYPAny4zpVLb8k650sW7LTddIIAYlUQMY-_qN7WZhpenyzBKs8d6ONMxhbqgRjFBtYY3k5kJJ8d1oJOnDpBwspTuKb5XiESBJi--cyyfmEjKOevnZLA8Gr9RoX1pigC3pl9YWTc7UtC8JYlkRL9UhMg2DLH90Vtt1Kz7KZDqFlC4z1GSVuNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19902" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19901">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کاخ سفید : پایگاه مشترک چارلستون در کارولینای جنوبی به افتخار سناتور فقید لیندزی گراهام تغییر نام خواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19901" target="_blank">📅 21:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19900">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مقام اسرائیلی نزدیک به نتانیاهو:
ما در یک مقطع حساس هستیم. رئیس جمهور ترامپ به زودی تصمیم میگیره که کدوم سمتی باشه.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19900" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19899">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19899" target="_blank">📅 20:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19898">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانال 14 اسرائیل به نقل یک مقام بلند پایه : ترامپ و نتانیاهو بر این موضوع تاکید کردند که هدف مشترک آنها، جلوگیری از دستیابی ایران به سلاح هسته‌ای است
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19898" target="_blank">📅 20:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19897">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19897" target="_blank">📅 20:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19896">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کاخ سفید:
جلسات ترامپ با زلنسکی و نتانیاهو، سازنده و مثبت بودند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19896" target="_blank">📅 19:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19895">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پایان جلسه دیدار بین نتانیاهو و ترامپ.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19895" target="_blank">📅 19:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19894">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRAtDdxtqLmGWdjwWUEQnD6AkeN2aDjQO4GWeM_YOhejxpSzMBfYyWHqEVOY-qXQAYihXOGr6ZpRBlbzBI_uuOO56awaqTHdmYUYDUX_lberdg2JJBtmrb0Q1g6AM6kUr9J2SHmLgMlTJE_fdrK-hhnhlS9_qPmN0vaRsKiY0VqxBll9A4gnFEbI-OXSzsbiPQEl3pZ3hK1fOYhda5Uzdq2cuYNV_QwRlBS9qHyxUV2fuwnRJdJzkBG2NYc0DY7a9Af_Znr4LdHfhYmvKgjJ6iQDkWBiYm9YevP22hjontJSb9euM56kpQCfd62bXWDKue-NOsNe-qAF6inR97CMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون نتانیاهو و ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19894" target="_blank">📅 19:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19893">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شاهزاده رضا پهلوی نیز ساعتی دیگر در مراسم سناتور فقید لیندسی گراهم در کلیسای واشنگتن شرکت خواهد کرد.
@WarRoom
🇮🇷</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19893" target="_blank">📅 19:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19892">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در دیدار نتانیاهو و ترامپ، یک تیم گسترده از مقامات ریاست جمهوری حضور دارند: معاون رئیس جمهور ونس، وزیر امور خارجه روبیو، وزیر جنگ گست، رئیس سازمان سیا راتکلیف و نماینده ویژه رئیس جمهور، ویتکوف.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19892" target="_blank">📅 19:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19891">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBt8mecxLB2VEBARgdOd3RluJiuyyNleF1suZp5G5YJqCZCdYyQam-IPCWs7VVdYjMtD1z7I_IqhSUqHfm4lUPV0Tfep1ag7I6sgiJZKc5pTdhlKR0w_dmGsJpv16e4QWKE3dEKivpGELORzQOxRKh6a4IDAlxHLlAf_cejTTp8K_4X8rGP10I5PljHv_i24jdIh-vpI7htRReV-Xvf7Wj02tEsQl0ojES1z2lh8ob-DFKqCV8NpViW3RLoeknBE5X8iQhu7kkpsetD9KMvfcDpDA1qqo8e7L-4p7GezOSSilEiRGYJAS0zLaIR0GkhnnXnNUxk0La-lXYToz1H4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملاقات ترامپ و زلنسکی در کاخ سفید: رئیس‌جمهور اوکراین گفت که آن‌ها در مورد مجوزهای تولید موشک‌های پدافندی پاتریوت در خاک اوکراین گفتگو کردند.
@WarRoom
پیشتر رسانه های فیک نیوز گفته بودند زلنسکی بدون ملاقات کاخ سفید را ترک کرده.</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19891" target="_blank">📅 19:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19890">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATIz3R9YsXmeTWWA8Zn8s0_0It8WgRHAFbeb8lnQh-tr2Gm8cjPpUD66hnW74yFL0T2S89CWo3fv76jjRha8fEL633lSwm616yB6t13PQeqcSsYkwAZJRSvMubG5UycOgtCnPEKq3PQtk9EVoOX1481hnyxvMAPn8Y1ZVeqVHU12Dnw5INYZT7n9kfPbaRrA-NOgqNXt-7LSAK3NFWknPhEt33uai0iiDBbyEn19_smOKqS42Jch51WRWw-qDtxVdrr6-4a-NRrRsB-W_wY0wpASkr_9AfaKrl7wMcDQm0vS3BgUg8dsmoK_xxlFb3l3e16DYUR__-RBWj4vsidqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19890" target="_blank">📅 19:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19889">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرنگار اکسیوس: یک مقام ارشد کاخ سفید گفت «ترامپ در مصاحبه با شبکه فاکس‌نیوز قصد داشت پیش از دیدار با بنیامین نتانیاهو، پیامی قاطع و سخت‌گیرانه به او منتقل کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19889" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19888">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سلاح دیوانه وار «میله های خدایان» گزینه دیگر غیر اتمی برای «کوه کلنگ گزلا» در ایران !
این ایده نخستین بار در دهه ۱۹۵۰ و سپس در دهه ۱۹۹۰ در مطالعات نظامی آمریکا مطرح شد و بعدها به دلیل جذابیتش در رسانه‌ها، مستندها و بازی‌های ویدئویی بسیار مشهور شد، عملیاتی بودن این سلاح مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19888" target="_blank">📅 18:49 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
