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
<img src="https://cdn4.telesco.pe/file/MruG6VfXXKXN0vG0PKWya-0nhOpeCxgj2sXwYKm1pBksL6wc2hZ1naB2eQEhqBNn5zZj-1u313WjFkmNn1ndW_QaNYXUbsYd5di-LNAF6IJy56BS-IfO0hlYCb_WMP9Lp1tvpdmxHtd9yz63BULUsRSYS3KxvD4QNQwy7rc3XH8xH0mmYJ3yod9KfVFzVYnqwlCDDSUYgX3fk_pCxnIvoXWD1TqsCY-v161r4UfcIF3PblaVp0NKbtXdCLOX1BYd2o5MqxwIsbKWlqrQa3ojjMPOqT5vTy7Datw9GG9KMF9pa7P20s-U20OfOjrvA9QUS--8MBrf2zb7BkriMVB2Iw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 430K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 18:55:34</div>
<hr>

<div class="tg-post" id="msg-20010">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea64fcfef1.mp4?token=RMPtDEpvRhpkVSaYQhHx2Usvzys18qD8E-Ik3ZgiscVT0-BPh0uAyPrD3HJ7Yb9RdsaxsOXwzcVscrnu7NPsouki1dkIM3r0P3VbhTwsja5JvcacNSLAVSdpj1GGZ_Xs5amIPdyZCX_6IZl3UVYGcNm9EQ1VISnXZ2PVne4gRVs-F-OF_WVaXgM3Lete25NPNBGnZPIqPWJrQh0Tf9QScOOHKqQyJo9cjPWeiBI3NVHrLJnthQviFOBFmn3Bhz7U4VrZR0V8hpJggXNh0k0cwyIcsw-HwzQr4P1X8Wm7G_CmUE4Y7_Zl6W1QUT1F7a72b4f-0i3bbB3pRCOn8rqeow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea64fcfef1.mp4?token=RMPtDEpvRhpkVSaYQhHx2Usvzys18qD8E-Ik3ZgiscVT0-BPh0uAyPrD3HJ7Yb9RdsaxsOXwzcVscrnu7NPsouki1dkIM3r0P3VbhTwsja5JvcacNSLAVSdpj1GGZ_Xs5amIPdyZCX_6IZl3UVYGcNm9EQ1VISnXZ2PVne4gRVs-F-OF_WVaXgM3Lete25NPNBGnZPIqPWJrQh0Tf9QScOOHKqQyJo9cjPWeiBI3NVHrLJnthQviFOBFmn3Bhz7U4VrZR0V8hpJggXNh0k0cwyIcsw-HwzQr4P1X8Wm7G_CmUE4Y7_Zl6W1QUT1F7a72b4f-0i3bbB3pRCOn8rqeow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیتر هگست، وزیر جنگ، در واشنگتن دیدار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/withyashar/20010" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20009">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نتانیاهو : جمهوری اسلامی، فرایند غنی‌سازی اورانیوم را در کوه کلنگ اصفهان آغاز کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/withyashar/20009" target="_blank">📅 18:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20008">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641e67f8eb.mp4?token=bkz5VZ8-Au-WVyFJrdbsR1RaQ4WaVedhDob_z3_xPHAFGcJ99BkS82IbmlWvXfXXsvy1oWUA_hRsSLI2PpaZ4tM1vYIFN3ge6YSBPCggK6C645L4hRiwt0zPuwatKNZMVnxA7yq_jPaXzsbcSM4tWLbajyHIPKppWZRiLf68_o_O7aZGkwKDcpTlVfwWfHrT-EGUDYws0-w9s4SOpUjPb9xW158lMYishw6JjiB2lVvx9zc2KalXxap2jGv1sUwQH8VETe6iUZS1b7qsjKHGRUkZlpnzsGnfddPNbIV_jEhHUhjKFn4QcSRioCjJ1JOaJAeewyPhVvUVpjNLMB4vng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641e67f8eb.mp4?token=bkz5VZ8-Au-WVyFJrdbsR1RaQ4WaVedhDob_z3_xPHAFGcJ99BkS82IbmlWvXfXXsvy1oWUA_hRsSLI2PpaZ4tM1vYIFN3ge6YSBPCggK6C645L4hRiwt0zPuwatKNZMVnxA7yq_jPaXzsbcSM4tWLbajyHIPKppWZRiLf68_o_O7aZGkwKDcpTlVfwWfHrT-EGUDYws0-w9s4SOpUjPb9xW158lMYishw6JjiB2lVvx9zc2KalXxap2jGv1sUwQH8VETe6iUZS1b7qsjKHGRUkZlpnzsGnfddPNbIV_jEhHUhjKFn4QcSRioCjJ1JOaJAeewyPhVvUVpjNLMB4vng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/20008" target="_blank">📅 18:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20007">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">زلنسکی:از ترامپ درخواست کردم که یک «بسته اضطراری زمستانی»، شامل ۳۰۰ موشک رهگیر پاتریوت را در اختیار اوکراین قرار دهد
اگر مشکل کمبود این موشک‌ها برطرف نشود، حملات روسیه نیروگاه‌های برق ما را نابود و یک بحران انسانی ایجاد می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/20007" target="_blank">📅 18:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20006">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه‌های حقوق بشری: اجرای حکم علیرضا سپاهی(فرد سوم در اصفهان)بعد از سکته قلبی متوقف شد.
@WarRoom</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/20006" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20005">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پس از تهدید ترامپ علیه ایران: قیمت نفت هم اکنون به 90 دلار به ازای هر بشکه افزایش یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/20005" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20004">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد نیروهای این کشور در جریان عملیات در روستای حداثا، واقع در منطقه حائل جنوب لبنان، تونلی به طول ۵۵ متر را کشف و نابود کردند که زیر یک کارخانه تولید مصالح ساختمانی و در نزدیکی یکی از مواضع نیروهای حافظ صلح سازمان ملل (یونیفل) در جنوب لبنان ساخته شده بود به گفته ارتش این تونل شامل سه اتاق بوده و حزب‌الله از آن به عنوان مرکز فرماندهی استفاده می‌کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/20004" target="_blank">📅 16:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20003">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانال ۱۴ : ترامپ درباره حمله ایران:  «قراره به باسن‌شان لگد بزنیم»
رئیس‌جمهور ترامپ پس از آنکه ایران موشک‌های بالستیک به سوی اردن شلیک کرد، وعده داد که پاسخی گسترده و سخت خواهد داد. این در حالی است که ایالات متحده و عربستان سعودی، در پی بیش از ۳۰ حمله پهپادی به نیروهای آمریکایی و تأسیسات نفتی عربستان، حملات مشترکی را علیه شبه‌نظامیان مورد حمایت ایران در عراق آغاز کردند
@WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/20003" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20002">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کانال ۱۴ : ترامپ درباره حمله ایران:  «قراره به باسن‌شان لگد بزنیم»
رئیس‌جمهور ترامپ پس از آنکه ایران موشک‌های بالستیک به سوی اردن شلیک کرد، وعده داد که پاسخی گسترده و سخت خواهد داد. این در حالی است که ایالات متحده و عربستان سعودی، در پی بیش از ۳۰ حمله پهپادی به نیروهای آمریکایی و تأسیسات نفتی عربستان، حملات مشترکی را علیه شبه‌نظامیان مورد حمایت ایران در عراق آغاز کردند
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/20002" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20001">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دونالد ترامپ اعلام کرد حملات علیه مواضع شبه‌نظامیان وابسته به ایران با هماهنگی دولت عراق صورت گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/20001" target="_blank">📅 16:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20000">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نتانیاهو شامگاه گذشته در اقامتگاه بلر هاوس با معاون رئیس‌جمهور آمریکا، ونس، دیدار کرد همچنین نخست‌وزیر نتانیاهو امروز با وزیر جنگ آمریکا، هگست، دیدار خواهد کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/20000" target="_blank">📅 16:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19999">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دونالد ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک سرطان جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نفوذی جمهوری اسلامی هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/19999" target="_blank">📅 16:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19998">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ درباره ایران :
ما به آنها اجازه می‌دهیم که به وراجی ادامه بدهند
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/19998" target="_blank">📅 16:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19997">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ درباره ملاقاتش با نتانیاهو:
این یک ملاقات عالی بود. او اکنون متوجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/19997" target="_blank">📅 16:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19996">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19996" target="_blank">📅 15:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19995">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/19995" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19994">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ:
حملاتی علیه ایران انجام خواهد شد و ما با قدرت به آنها ضربه خواهیم زد
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19994" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19993">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/19993" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19992">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسپانیا پخش اذان از بلندگو رو در بعضی از شهرها مجاز اعلام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19992" target="_blank">📅 15:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19991">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرگزاری رژیم فارس: تنگه هرمز بسته بسته است، دیگه از این بسته‌تر نمیشه.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19991" target="_blank">📅 14:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19990">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هم اکنون هشدار های حمله موشکی/پهپادی در تلفن های شهروندان اردن نمایش داده می شود
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19990" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19989">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رویترز: فرماندهان سنتکام در حال بررسی امکان توقیف تلفن همراه سربازان آمریکایی جهت عدم انتشار تصاویر خسارات ها هستند
ژنرال براد کوپر، فرمانده ستاد مرکزی فرماندهی ایالات متحده (CENTCOM)، به نیروهای آمریکایی مستقر در خاورمیانه هشدار داده است که ویدیوهای ضبط شده با تلفن همراه و منتشر شده در اینترنت، به ایران کمک می‌کند تا میزان اثربخشی حملات خود را ارزیابی کرده و موقعیت‌های نظامی آمریکا را شناسایی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19989" target="_blank">📅 14:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19987">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ed6y7I2P-gSsrdPShtHAQBmB3aZbfD4t1ET_3ubcVh_PUcceUHpiydK_KBLdJAJ26j4z90lqklcEEhmZktLw6HyMOWBMxyf73QPbPF7l23zZ-AqKMlhJtT0s46_0-D6cfiAQLkXEgiNZYOOFgU8svAE7qY_RVVrmyL5qdcEoHvbQIZ-2nXSzIFj1Cjdj9bdrqUqs-9WqK3xh97m8ZYr6C7-D6saW0PZ-3ZeA2RW7U-n6_QL_WdeVd-iQ4B5cGcvVxkamKa2RJCoYS3Ek5abtIk9cDg2hPSl7-q3caIJ5LFE4fxYtrYxgnIrf-J0-G_s6XTBytV--ZAyDvLx9o1yhhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzzbRyjCB3Bu75JNzzr_Kr-Rm6yf07El4vCB2utcjKGVTWCCCkwlVSTEADp45ZBQ4-DTK87eepexG15DsJnjPfux8CwmB6rydRWBOkBhLP40vWUM3f_TCocDjLy2v1aHBjWltPf1pSwd2I2y480FqShVjLHbY_CfGZcv-iXHe5RaqidCYf47DhlO_DF3kFOZx0A3Q3JEUXWIBVeuNps2v1tTA7x6qBBEIjBMW5kQQZLLU3BhriNv3tTyTq7xlh3nM6HdZEBho31fHQamiOtgAtEYSPVBJUNUJQQJiihJ7uOOdxL2QNYRHdYQIR9tU8cPBqVcULyEUgOruYZonw3Jdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمله به شمال ایران ساحل خزر شهر
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19987" target="_blank">📅 14:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19986">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش های تایید نشده رسانه های بومی و مردمی در خصوص حمله هوای به نوار مرزی پیرانشهر در ایران  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19986" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19985">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تصمیم‌گیری در مورد ایران
کاخ سفید اعلام کرد که ترامپ امروز ساعت 18:30 به وقت تهران یک جلسه اطلاعاتی مهم خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19985" target="_blank">📅 14:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19984">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">زلنسکی به اکسیوس :  رابطه‌ام با ترامپ خیلی بهتر و سازنده‌تره ، مثل قبل دیگه این‌قدر احساسی نیست
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19984" target="_blank">📅 13:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19983">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش های تایید نشده رسانه های بومی و مردمی در خصوص حمله هوای به نوار مرزی پیرانشهر در ایران
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19983" target="_blank">📅 13:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19982">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش انفجار در عراق و اردن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19982" target="_blank">📅 13:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19981">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش‌ تایید نشده شنیده شدن صدای پرتاب موشک از ‌کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19981" target="_blank">📅 13:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19980">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مشاور ارشد ترامپ: "ایران می‌خواهد حزب‌الله در لبنان فعال بماند، ما اجازه این کار را نخواهیم داد."
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19980" target="_blank">📅 13:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19979">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVMj_Wibe7bc1EdMsZODQOM_kP5jHhGIDIHd3uXq-DBNeFAw_N-1lNVDgasWvpDe3E_2-BfT8_ai-Iw3yMLADDXFKBYSY2XOnU3aYikz_YW66xPmey76060sw7mYnfC4YSqO3Gj2-qZHcU4jxDRu95zvpK9Z4JvBJA_6hMtnJX03qNXXwzucaKe-gyMFEgC99_WYVlNjoPydzCUyikld6OqDD6n-D_F3eVIYrL-HhdjqusK771EZA1tmqdS0oEzg9ykHEBiSJmn3xQnD5DEF8jWs65rNUcBY_oUXVlMExZB7ae_ZsBkmzm4MhVKW55bskqHLd1KRTRXXOwSD096nig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این عکس نوشت : شاهزاده رضا پهلوی، ولیعهد ایران، با شرکت در مراسم یادبود سناتور لیندسی گراهام، به نمایندگی از ده‌ها میلیون ایرانی که برای آینده‌ای آزاد و دموکراتیک مبارزه می‌کنند، ادای احترام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19979" target="_blank">📅 13:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19978">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fklR0OMjLt5FMKmFrI71HlSn4mStcXgs8XdLGg3Y-kUyoiIknXVtfe-ywOAqa8UaZ85ToGogEK5zCijtJqfNN7DNNJ8QvTyOw8MdMKvpXMhjWu0hkjjp3eXUNeBHhvLKf-5xG5-VOjRJ-eiIOm4Xh1FqulN1MT42h7JJU5jvviN50Ct8pj6gJrF3ycJWzA7jvTmEMCG0A87YluBcvdMOi7xfgX0QHGkJ9SHKF78Mti7WVhCV4ZuPCWTA864xidNjFI6xTOduwWn5rLI4rARIgPF7oGI2Kuzo-2ZcPrVWhl6q_Yr_ZE9ryqiuOHyt5FZOv6GZD9fQ5cR8HjNzzsjUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ حضور شاهنشاه آریامهر، ریچارد نیکسون، شارل دوگل و بودوئن، پادشاه بلژیک، در مراسم خاکسپاری رئیس‌جمهور ایالات متحده، دوایت آیزنهاور، که در تاریخ ۳۱ مارس ۱۹۶۹ در کلیسای جامع ملی واشنگتن برگزار شد…
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19978" target="_blank">📅 13:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19977">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏استیو استکلو، خبرنگار ارشد رویترز و برنده سه جایزه معتبر پولیتزر در گفتگو با شاهزاده رضا پهلوی و گفتگو دیگر تکمیلی او با بی بی سی فارسی @WarRoom وی در این مصاحبه به نکات بسیار ریزی اشاره و خودش همچنان اذعان میکند که شاهزاده را به چالش کشیده و وی خیلی مسلط…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19977" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19975">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏استیو استکلو، خبرنگار ارشد رویترز و برنده سه جایزه معتبر پولیتزر در گفتگو با شاهزاده رضا پهلوی و گفتگو دیگر تکمیلی او با بی بی سی فارسی
@WarRoom
وی در این مصاحبه به نکات بسیار ریزی اشاره و خودش همچنان اذعان میکند که شاهزاده را به چالش کشیده و وی خیلی مسلط و با تجربه به او پاسخ داده.</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19975" target="_blank">📅 12:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19974">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الحشد الشعبی: بر اساس آمار اولیه، دست کم ۲۰ مجاهد کشته و ۳۲ نفر دیگر زخمی شدند. این آمار مربوط به حملاتی است که توسط ائتلاف آمریکا و عربستان سعودی انجام شد و تعدادی از مقر‌های رسمی الحشد الشعبی را در چندین استان عراق هدف قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19974" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19973">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش‌ تایید نشده شنیده شدن صدای پرتاب موشک از ‌کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19973" target="_blank">📅 11:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19972">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromElahe</strong></div>
<div class="tg-text">سلام وقتتون بخیر
شما که انتقاد میزارین تو چنل
لطفا لطفا قدردانی ماهم بزارین از این همه تلاش ها و اخبار کامل درستتون خسته نباشید به امید دیدار در میدان آزادی عمو یاشار
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19972" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19971">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19971" target="_blank">📅 10:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19970">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19970" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19969">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رویترز: انتظار می‌رود ایران در چند هفته آینده، اولین محموله از تا ۴۰۰ سیستم دفاع هوایی قابل حمل چینی (MANPADS) را دریافت کند. ارزش این معامله حدود ۶۰ تا ۷۰ میلیون دلار تخمین زده می‌شود. طبق گزارش‌ها، این سیستم‌ها شامل مدل‌های QW-12 و FN-16 هستند و هدف از آن‌ها بهبود توانایی ایران در مقابله با هواپیماها، هلیکوپترها و پهپادها در ارتفاع پایین است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19969" target="_blank">📅 10:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19968">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نیویورک تایمز: ایران به این فکر کرده بود که یک حمله موشکی نمادین به یک بندر اوکراینی در دریای سیاه انجام دهد، پس از آنکه گزارش‌هایی منتشر شد مبنی بر اینکه اوکراین یک کشتی باری ایرانی را در دریای خزر مورد اصابت قرار داده است.‏
به گفته مقامات ایرانی و غربی، تلاش‌های دیپلماتیک تاکنون از تشدید تنش‌ها جلوگیری کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19968" target="_blank">📅 09:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19967">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حکومت ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19967" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19966">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc30Nf7Bau-MJoo3svDD_MozNb9dHTSVL-_otY2VFeJrTkSYW6_0SPqS7SvfJGuTQF65VSTnoSSBhrw_38JDK6V8psU6oSHXiasiW38vqrZzDvyhvMd0MqP3m0jyD8HNB47ZTQ_UAfESv-WswDkcubiOkXB9xHqP53hg1uUEgCvxZkxuivZwWkNrKHnDzFyj69SqFZMnhGBsWSBqMaYy3izFHa_LbRlz67wr3vOhvuUVwn2obq5kWqwPu7so82F628zQnCNUHWSp_GM7RSDkuhUBX0u8cRFgNcaC0-kY99RvZ9gm0oCAzmIfmEVrn72DO8nzkVEKHD228vZ1Pk_dFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی جمهوری اسلامی اعلام می‌کند که پیکر سرتیپ خلبان مجید کاظمی، خلبان یکی از بمب‌افکن‌های تاکتیکی Su-24MK که در تاریخ ۲ مارس توسط جنگنده‌های ابابیل F-15QA نیروی هوایی قطر در حین تلاش برای حمله به پایگاه هوایی العدید سرنگون شد، پیدا شده و ظرف چند ساعت آینده به ایران بازگردانده خواهد شد.
نیروی هوایی جمهوری اسلامی افزود که مقامات ایرانی همچنان در تلاش برای تعیین محل سه خلبان دیگر Su-24MK سرنگون شده هستند و جزئیات مراسم تشییع جنازه مجید کاظمی متعاقباً اعلام خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19966" target="_blank">📅 09:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19965">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b466899a00.mp4?token=c1cxGKndC37qkQCiRBuILiQz4pDKWZOkEKDliUiZ0dOvn1g0it_jXJcyAlDe9nuJn5ELZa4TiweaSSCjmhsVM4PLcQizT-CIrXK18FDm1jKzxT0pKkIgLgsG9CnhNChybF-tVEz7L1GeWex0iEcGbt0iaisLsekckWq1nisS4ANJK_gdZxDfHwG2MU5AJCSm-TreaormTzLq10WsC0za52bXsJ8WtPXuz9hCM6WWg5dkIid5df1WtEh70esIUefC310TWV9q9dcDRddbKpF3yYMpzveOKl64ItNbQohDW4C7MdxmBQGAP2xvV3Ez3xxwIWWRkEDAHNjhLMC_GnESCT21KhEYBcxUPfsmfVbqkHm7zG-YEFR2-xaDCNm6uCmimWRA8LG_8D-OGXR9245c75wJOMylK2ZaCfag1lmUSY6cKgImAxc8t3sVcP0ZgD-mwOzumklHXJLVPwRcogyXmBBNTHM-7msX6DIFqaigcu9zLnOZ3txQ6Wjk0AiHRTF_kDqupUngCMu-PhY3Jdrr7BTHkCqtyIy3cftwCOzSKYPxrhu-MkJRgOgHaqU2DpgCDTrgCYWdXWd_1uWp9Y_bvUSE8uke-k_AAngaQYsYnKfgEwOn87BHchaULUAGcOjtlnSIHqtCiHIuPWKwRo7BN8hoXeKbVV4n5qe8P8kGWZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b466899a00.mp4?token=c1cxGKndC37qkQCiRBuILiQz4pDKWZOkEKDliUiZ0dOvn1g0it_jXJcyAlDe9nuJn5ELZa4TiweaSSCjmhsVM4PLcQizT-CIrXK18FDm1jKzxT0pKkIgLgsG9CnhNChybF-tVEz7L1GeWex0iEcGbt0iaisLsekckWq1nisS4ANJK_gdZxDfHwG2MU5AJCSm-TreaormTzLq10WsC0za52bXsJ8WtPXuz9hCM6WWg5dkIid5df1WtEh70esIUefC310TWV9q9dcDRddbKpF3yYMpzveOKl64ItNbQohDW4C7MdxmBQGAP2xvV3Ez3xxwIWWRkEDAHNjhLMC_GnESCT21KhEYBcxUPfsmfVbqkHm7zG-YEFR2-xaDCNm6uCmimWRA8LG_8D-OGXR9245c75wJOMylK2ZaCfag1lmUSY6cKgImAxc8t3sVcP0ZgD-mwOzumklHXJLVPwRcogyXmBBNTHM-7msX6DIFqaigcu9zLnOZ3txQ6Wjk0AiHRTF_kDqupUngCMu-PhY3Jdrr7BTHkCqtyIy3cftwCOzSKYPxrhu-MkJRgOgHaqU2DpgCDTrgCYWdXWd_1uWp9Y_bvUSE8uke-k_AAngaQYsYnKfgEwOn87BHchaULUAGcOjtlnSIHqtCiHIuPWKwRo7BN8hoXeKbVV4n5qe8P8kGWZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید و پر معنی کاخ سفید
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19965" target="_blank">📅 09:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19964">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19964" target="_blank">📅 09:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19963">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏گروه تروریستی سپاه پاسداران مدعی شد که در ادامه تشدید درگیری‌ها، سه نفتکش را در تنگه هرمز با حملات موشکی و پهپادی هدف قرار داده است. بر اساس این ادعا، نفتکش‌ها پس از اصابت متوقف شده‌اند. این ادعا تاکنون از سوی منابع مستقل، شرکت‌های کشتیرانی یا مقامات بین‌المللی تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19963" target="_blank">📅 09:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19962">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سنتکام : ما و نیروهای مسلح عربستان سعودی در ۲۸ ژوئیه حملات دقیقی را در عراق علیه تروریست‌های همسو با ایران انجام دادند که سپاه پاسداران انقلاب اسلامی (IRGC) آنها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان سعودی هدایت کرده بود.
جنگنده‌های ایالات متحده و عربستان سعودی در پاسخی قوی به بیش از ۳۰ حمله پهپادی هوایی به رهبری سپاه پاسداران در ۷۲ ساعت گذشته، چندین سایت لجستیکی و تسلیحاتی تروریست‌ها را در سراسر شرق عراق هدف قرار دادند.
این حملات بی‌دلیل علیه نیروهای آمریکایی موفقیت‌آمیز نبود.
از فوریه تا آوریل ۲۰۲۶، بیش از ۶۰۰ حمله ناموفق به شهروندان و تأسیسات آمریکایی توسط شبه‌نظامیان تروریست همسو با ایران در عراق صورت گرفته است. سپاه پاسداران و گروه‌های تروریستی نیابتی آن باید این حملات را متوقف کنند تا از واکنش نظامی بیشتر ایالات متحده جلوگیری شود.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19962" target="_blank">📅 09:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19961">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عربستان : عملیات ریاض علیه عراق با هماهنگی سنتکام انجام شد
این حملات در پاسخ به حملات پهپادی گروه‌های وابسته به ایران در عراق علیه تأسیسات نفتی عربستان صورت گرفته
ریاض برای کاهش تنش‌ها در منطقه تلاش می‌کرد، اما این گروه‌ها ادامه اقدامات خود، مسیر تشدید تنش را برگزیدند
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19961" target="_blank">📅 09:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بصره عراق مورد حمله نظامی از سوی عربستان سعودی قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19960" target="_blank">📅 03:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجار انبار مهمات در مقر فرماندهی عملیات حشد شعبی، بصره
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19959" target="_blank">📅 02:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19958">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایرنا:
سنتکام دروغگوعه، تمام موشک‌های ما اصابت داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19958" target="_blank">📅 02:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19957">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">صدای جنگنده از کیش به سمت جنوب ایران
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19957" target="_blank">📅 02:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19956">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رسانه های داخلی : به اربیل عراق حمله پهپادی شده و جنگنده‌های آمریکایی بلند شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19956" target="_blank">📅 02:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19955">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اخبار حاکی از فعال‌سازی سیستم دفاعی "پتریوت" در آسمان جمهوری آذربایجان، کشور همسایه ایران، است.(تایید نشده هست)
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19955" target="_blank">📅 02:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19954">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yk7QdXrjclYjuIiFCD9RhBZ-Njx35yLsfostBSCFp_K95FLagHq0YBzC65vkqt2O1-XyAKEtUToMDt6UF1Nxt5dgiSWCvaeImT-6adQE93_2lwFh2zPNZu7Iv-vMqA2BPKaFcE3yxCTT9UEFAIauLbyruqgJ3C9g3z99qozCEDFfPVIw3aDbK6ItmXH0EBg3VqRuXe_In8SxH9cTGUVMVHb3Pb1xTgiTHgLXaHEFAnyMM0j-Tu7KEmVKg3_khan28FX9px5MBEa8G_0b2FpLdxksJjbukXL9wO8zxEifGzS5X4Q1f3UKt6cFXpW5VzCCDFgj1XtqjMKflfqoPNVvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاهی به برد موشک های سپاه به اکراین
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19954" target="_blank">📅 02:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19953">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سپاه به اربیل عراق حملات سنگین موشکی/پهپادی کرد و چندین انفجار تو اربیل شنیده شده
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19953" target="_blank">📅 02:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19952">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : دربون جهنم سابقه نداشت خبر از حمله سپاه بزنه! بدجور برد کوپر بد خواب شده ، مادر بگرید
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19952" target="_blank">📅 02:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19951">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمانده سنتکام بردلی کوپر رو از خواب بیدار کردند
👺</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19951" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19950">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">منبع آمریکایی به شبکه i24NEWS گفت که جمهوری اسلامی حداقل 4 موشک بالستیک به سمت یک پایگاه آمریکایی در اردن شلیک کرده است و این اقدام را یک "حمله بزرگ" توصیف کرد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19950" target="_blank">📅 01:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19949">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چنل و اینستاگرام رو فردا پرایویت میکنم یه مدت ، اگه فالو ندارید فالو کنید نمونین پشت در پیش عرزشی ها
t.me/WarRoom
instagram.com/yashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19949" target="_blank">📅 01:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19948">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من نمیدونم رسانه ها برای اینکه جو بدن چرا اطلاعات غلط میدن مردم اصلا آتش بسی نبود که بخواد نقض بشه. یه حمله شد، یه جوابی داده نشد. یه طرف کوتاه اومد، ادامه نداد! الان جواب اومده جواب داده
😁
چون نفت داشت میومد پایین فشاری شدن
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19948" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19947">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مقام ارشد آمریکایی: ایران موشک‌هایی را به سمت پایگاه آمریکایی در اردن شلیک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19947" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19946">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمانده سنتکام بردلی کوپر رو از خواب بیدار کردند
👺</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19946" target="_blank">📅 01:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19945">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پرتاب موشک جدید از غرب ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19945" target="_blank">📅 01:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19944">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش‌های تایید نشده از اصابت یک موشک به مرز اردن و اسرائیل و پایگاه آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19944" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19943">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87354e52d8.mp4?token=mgveV0wo5iQfZ1LVuTqloQrnrC6LRDuZFwBW9gQaeVzra-NHAhHAVSNDL0_ZIAvFY8KnE4ZEkZv1FDS9xsabDDGSlOaCQIIi1calzB4VEV4MCnWEEBmz6AnK-frOMT7AjpWXnS3VXlyb92PTttz8V9XYl0CaImmcQV3kgqdOTltCm60PBso25B22dAIXF5IAdRgzEur6X0On5cg9vJDZ_ao38wQ5Lq5pPnEHVtQL98XgpoYYpWdwHWdSaR_zBaKHNsmxTpxr7QP-3AQTlFdQEPybyv-vzWpevEjxbRncptQt4dPiowYVtoJcVFPsVM7LZO_PawKELggl4RN7rD7kRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87354e52d8.mp4?token=mgveV0wo5iQfZ1LVuTqloQrnrC6LRDuZFwBW9gQaeVzra-NHAhHAVSNDL0_ZIAvFY8KnE4ZEkZv1FDS9xsabDDGSlOaCQIIi1calzB4VEV4MCnWEEBmz6AnK-frOMT7AjpWXnS3VXlyb92PTttz8V9XYl0CaImmcQV3kgqdOTltCm60PBso25B22dAIXF5IAdRgzEur6X0On5cg9vJDZ_ao38wQ5Lq5pPnEHVtQL98XgpoYYpWdwHWdSaR_zBaKHNsmxTpxr7QP-3AQTlFdQEPybyv-vzWpevEjxbRncptQt4dPiowYVtoJcVFPsVM7LZO_PawKELggl4RN7rD7kRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان اردن ، پدافند درگیر شده
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19943" target="_blank">📅 01:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19942">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mydISaXZC58MBUEKO4u_U6JCn9fj0IUfrXaxPb7KDp6QUMGAY8ng06k_DmGETri9mQMLOBsumJHJyZZKxceU9o2icJu2VLD4HFmT5rlqDvEEIl6YOgFAfrFNBImEdovZIIuCgVaOA0DMXv4M4fWl6Fvtyr5I3s7-opOeg8CIPneVoXGTsCHJnJqxgQHOucyXDH9b1IMmKeRK8YXvF-9CQlLq7v9AwB_7x7A7oB_Y5pHT2FwFnQAKaIIkC9eZnrJpGdLcrl2wSv6NDxgtUzIn-sUNtwZchhLY3n7G6zBJkC_2mL1Y94JHiHyBnWQKrK7IfNYHYn0gLBn8fhIUnmLecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر موشک ها
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19942" target="_blank">📅 01:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19941">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فک کنم نتانیاهو با گوشی ترامپ به مم باقر فحش ناموسی داد</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19941" target="_blank">📅 01:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19940">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swLIX5zPIC1yXbfE-JSPVRrKFYgecUWJHtm3Y3tPLWZqCJxJr3ODA7y3NBYh-vEELM19Mj5RU1P9cgJroCo0Eml0PUT-MJbGJXr-bV1A8BQiltZqtI0C-UDVWxIOHaEl47M22ehUdZdKj0RvTtwLAygfOTz3ZIjdkcjTb-UPjTcL3O2vINcXkq_6RU1vp1g5wLy7hHZcqIwiVQUK-N2iHYug_nVjoS1vnMiHnqZ2nRFbz_w7N8I7zRP1tARbh5FMp332nrqRP368_J75b75UIevUkNVeJNL2_4qnRv1HiGE_v4UhzkDPLfWIE4oy1fBnOYH-tUEt1Grbm5tVE72nCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک ها در آسمان خرم آباد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19940" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19939">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آلارم اردن فعال شد
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19939" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19937">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6upDSGQtQMDxnaZDbsPzPqUE5y6QAFyebdbHJ4TGhqHbCztdGxtYpRmzQNMoAfi1OvIj5sTJ-ArWY7NWBx5KaemNllx2qxKx8UuHLqfYGWqG3begj3NudDh1puavZRC83ay-MFlT3AQeTH994v1cr2NQRHj1co6iFdXCvVs4fTjkx15sh2tyNolJrp9cxzeLmRojQSh20hrjj1oqkH86U68BulvnHrJxoC5dZPWyyKHGQGSG26sIr_Rc1oPknEZMnoPibgfk2Info1X1fML9bUTe41DAj_1pnZoVQtl9KQYMOghd9FHegCtAY52XGU3bphKYtJR1UVkiywsuq0tpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYdaNmpMMgutQgn_Q15Yac5-Gk1wkOCVTnMO3JVTz82RTA0-6yhKDqfmKxVrDSb_LUbaJcRUkUGdYVy2qZak0J6_aa__XQqH3YPtyO_J6LWYoDSQcI02f-Y0oqr7F0m0nXV0wreJaNVdTdbDjux-VD35BJvTgxxmN0TJLzYs1h-uTv2Tb7D4qvRSQCb4iVU4_qmUYwO7gHWGWAZ0KoUv3aFvH8_OmvGMegCFpVjBv4tryi-8nKQTxqRwkVsF9D53fY6ALn8vJtT6EWC8GOux5jojftCteR5B839ornIwd4oi_gzbC29F5EtY1WLzSQL5ULwnEU69kMlbyvvDjXvRbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شلیک ۳ موشک از خمین به اردن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19937" target="_blank">📅 01:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19936">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کانال i24 عبری : تنها چیزی که ترامپ را به سمت امضای توافق با ایران سوق داد، قیمت نفت بود.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19936" target="_blank">📅 01:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19935">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ddcbdc52.mp4?token=spPYBU_uCoM5NF561yVb4VkBgFaVXaSUXAchgIOKt68hgm9HIjQEdo_CTzjpMTb7Hgp22TW-CubLDxbWFsQjxQF_EWNNOcVtwGvwSomfuhLK6PoL0EFWxBhNcZKKQn4SpmWUANe9RAOxUEWanuJLFQy1kdO56FlOcTvCzkLr_UzjPddJ2u4kmdKK9ZKCevlXi8MV6Aw6XhT5HMZVUFt5hQ2tpgPXciZVN3ok8bjZf4XCb6GGP0h9L2wOwlDL0C4qLrUcon7tlzwXvoR1j1ekSe2SyidEbxe7YuWtwHTjpAJQLzIPWT6ap3CcU1iyYIekV2gt2Ax6vTIjR3bIu82dXZmLOiVQOMZw2WpMroEymh1iAdgLqdPJ2ePLH_cC7rCZD9AbqvAJ84dVQlaZlSUwh9-BTRQD-S6JaWqIHk_RCpctgiJN75cTULu_6Ygh6oCO9pHawOvcW1BTHMKVJQZmp3jNL3y5ApoyMfiJ9Zz8xLH40sfxmN4rmqREGTpeV3eGaDK7qKjdmuNGq3mct_5EDJVgqvAUVTSNOHH3q206ufqpU4U_oZoC84nf3773XLmwHZomYoV30Ggp53MtD020L2yzF2jOmQcjSwJ-i_hWTc1EvskcaIgBhUENbCNywPH8iHD8LrzQ43kAl4Jg54jfI8jwsRjNT9Fm1o0RuEO9JZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ddcbdc52.mp4?token=spPYBU_uCoM5NF561yVb4VkBgFaVXaSUXAchgIOKt68hgm9HIjQEdo_CTzjpMTb7Hgp22TW-CubLDxbWFsQjxQF_EWNNOcVtwGvwSomfuhLK6PoL0EFWxBhNcZKKQn4SpmWUANe9RAOxUEWanuJLFQy1kdO56FlOcTvCzkLr_UzjPddJ2u4kmdKK9ZKCevlXi8MV6Aw6XhT5HMZVUFt5hQ2tpgPXciZVN3ok8bjZf4XCb6GGP0h9L2wOwlDL0C4qLrUcon7tlzwXvoR1j1ekSe2SyidEbxe7YuWtwHTjpAJQLzIPWT6ap3CcU1iyYIekV2gt2Ax6vTIjR3bIu82dXZmLOiVQOMZw2WpMroEymh1iAdgLqdPJ2ePLH_cC7rCZD9AbqvAJ84dVQlaZlSUwh9-BTRQD-S6JaWqIHk_RCpctgiJN75cTULu_6Ygh6oCO9pHawOvcW1BTHMKVJQZmp3jNL3y5ApoyMfiJ9Zz8xLH40sfxmN4rmqREGTpeV3eGaDK7qKjdmuNGq3mct_5EDJVgqvAUVTSNOHH3q206ufqpU4U_oZoC84nf3773XLmwHZomYoV30Ggp53MtD020L2yzF2jOmQcjSwJ-i_hWTc1EvskcaIgBhUENbCNywPH8iHD8LrzQ43kAl4Jg54jfI8jwsRjNT9Fm1o0RuEO9JZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: به نظر شما چه صلاحیت‌هایی برای رهبری یک دولت انتقالی در ایران دارید؟
شاهزاده رضا پهلوی: اگر یک وکیل تصمیم بگیرد پرونده‌ای را به صورت رایگان بپذیرد، آیا این به معنای آن است که او شغلی ندارد؟ من چهار دهه است که این کار را داوطلبانه و رایگان انجام می‌دهم، درست است؟ به عنوان فداکاری من برای کشورم.
من می‌توانستم به راحتی در قاهره، زمانی که پدرم فوت کرد، تصمیم بگیرم: "می‌دانی چیست؟ به جهنم." من می‌توانم مانند بسیاری دیگر، زندگی، تجارت یا چیزهای دیگر را دنبال کنم... اما تصمیم گرفتم به خاطر کشورم در آن بمانم.
این یک فداکاری شخصی برای یک عمر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19935" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19934">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba487c3af7.mp4?token=bjki_cLql1dfcONGVPqlCuV0ijQZ_sfwERsYtxLWehqbB_mms4uST9I-HDQw2crupAgO2ag6VXUbNeKFejsUEjMbziSNRnpLhXJQbrZjkeEXbugjCe2_kC3rEGrVmqaYPl1ryoA2_QTZ5isVubwai7WVA38O0BCoPsxIYvPj-yfFmRWx8f47r9KXv7DHBFBgbzPHP4dE4w07Mwf8O3sx8LRaRJSeLt19uSdUhbMutBAOoi2w2wJg9_70Q4S7o5bOrnhUZYxXpDTaDxc4r-aETa0wp7SpMtje78sW6bpwQ3r-faDxTg9K3tqj4oO9NlcKG-5IoVtBfWo6WfhPvPuiig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba487c3af7.mp4?token=bjki_cLql1dfcONGVPqlCuV0ijQZ_sfwERsYtxLWehqbB_mms4uST9I-HDQw2crupAgO2ag6VXUbNeKFejsUEjMbziSNRnpLhXJQbrZjkeEXbugjCe2_kC3rEGrVmqaYPl1ryoA2_QTZ5isVubwai7WVA38O0BCoPsxIYvPj-yfFmRWx8f47r9KXv7DHBFBgbzPHP4dE4w07Mwf8O3sx8LRaRJSeLt19uSdUhbMutBAOoi2w2wJg9_70Q4S7o5bOrnhUZYxXpDTaDxc4r-aETa0wp7SpMtje78sW6bpwQ3r-faDxTg9K3tqj4oO9NlcKG-5IoVtBfWo6WfhPvPuiig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: گزارش‌هایی، تقریباً ناشناس، مبنی بر دریافت بودجه از اسرائیل و عربستان سعودی توسط شما وجود دارد. آیا این درست است؟
شاهزاده رضا پهلوی: کاملاً نادرست. من هیچ بودجه دولتی یا عمومی از خارج دریافت نکرده‌ام.
هر ریالی که به کمپین من می‌رسد از کمک‌های خصوصی حامیان است. امیدوارم خیرین بیشتری داشته باشیم که چک‌های بزرگتری به ما بدهند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19934" target="_blank">📅 00:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19932">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رویترز به نقل از یک مسئول آمریکایی: توافقی که در حال بررسی است و مربوط به تنگه هرمز، مربوط به هماهنگی است و شامل هیچ‌گونه عوارض عبوری یا هزینه‌های دیگری نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19932" target="_blank">📅 00:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19931">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4dee73717.mp4?token=K1UvrHinXGKrJ-wu7Tv_hpAdawS33uQfqINqky7SFIfOhG8ES3oxg4e09q55dIhswaVs-YypvKia3MOgwWRJ2l1-0V3Tj3nC-ROGekOCE_GU1X8dmdAErsw4S48iBhdI9Or_BUEHjgZBJ3smbRwesADa-BDp0YlQ0eTwjPQ0zN1AXX1rkNu2htbuyjfsfvSDS8_9PLhXaXL7d5Q53Dzj7ygoAP8x5GhacYV6x_7i0nfki9ZYuc5L5l_HJ8KaBlGqkewdkMAk_jH6VBdVDTRYla1BRwYOFKaYyAeAfDIgkZjp7PuV5-h8JluVbE0F5M-RLUNJ5TkML9R8GiZJLEKA94WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4dee73717.mp4?token=K1UvrHinXGKrJ-wu7Tv_hpAdawS33uQfqINqky7SFIfOhG8ES3oxg4e09q55dIhswaVs-YypvKia3MOgwWRJ2l1-0V3Tj3nC-ROGekOCE_GU1X8dmdAErsw4S48iBhdI9Or_BUEHjgZBJ3smbRwesADa-BDp0YlQ0eTwjPQ0zN1AXX1rkNu2htbuyjfsfvSDS8_9PLhXaXL7d5Q53Dzj7ygoAP8x5GhacYV6x_7i0nfki9ZYuc5L5l_HJ8KaBlGqkewdkMAk_jH6VBdVDTRYla1BRwYOFKaYyAeAfDIgkZjp7PuV5-h8JluVbE0F5M-RLUNJ5TkML9R8GiZJLEKA94WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی درباره ایران:
فکر می‌کنم ما به تغییر رژیم بسیار نزدیک هستیم.
رژیم در ضعیف‌ترین وضعیت خود در ۴۷ سال گذشته قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19931" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19930">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2dacc78c5.mp4?token=BCe2AVaayG8r-PB0FMvboV4bwBRHnLxGRqOgKwo70HNlM_YYIqmYNXnb_ntdKrOKc51GkzWj571sl9UajGREVfyFGr8FCd_83Gm6HKYW6F96NjevAhGbEJWF3rjzYTQMpWmIzDKLUwtqO083JdGPhCdTAY_6yCpQ5e1LrE5S5zM3JWVUjkXKIoiQKlm-TY7RIg2XiPIplKuaZtl8JH_fFqMERdQIGtum9yO19IZNMG8gKQgckcnY8yKDn7fFwfYkIjuMqiVQGKoeBleg19GX0ZmUMbPHUzm910i-BRvvdaIGO0cCSX_hrejbNti2qi5jTi3l1dRS4_iEd8bKsf1vkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2dacc78c5.mp4?token=BCe2AVaayG8r-PB0FMvboV4bwBRHnLxGRqOgKwo70HNlM_YYIqmYNXnb_ntdKrOKc51GkzWj571sl9UajGREVfyFGr8FCd_83Gm6HKYW6F96NjevAhGbEJWF3rjzYTQMpWmIzDKLUwtqO083JdGPhCdTAY_6yCpQ5e1LrE5S5zM3JWVUjkXKIoiQKlm-TY7RIg2XiPIplKuaZtl8JH_fFqMERdQIGtum9yO19IZNMG8gKQgckcnY8yKDn7fFwfYkIjuMqiVQGKoeBleg19GX0ZmUMbPHUzm910i-BRvvdaIGO0cCSX_hrejbNti2qi5jTi3l1dRS4_iEd8bKsf1vkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر واضح از حظور شاهزاده رضا پهلوی در مراسم
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19930" target="_blank">📅 00:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19929">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiQellOmtOxLeS6XBtub-NCb4kyFznguIyuscZ_6ChcjF4qBeDaVeoqH54bT7C-9gwzpYcQP_4FXMeAjhL-swb8HV3r-SDa2xB7VuJXa33ngBh_7eUZ6KJYWGa-8-i8R_XfhJM0YIiFB9fh4B8TT2xgPLxmc6nIJVXJVTG3JUeZCVYZRcRvZRmhRN5Ip6uDf8ua1PSe20VdtWChGUEgDE3ywiGXTvzOHLs-aW3XNALSGWF6kLDraqJhBFBILFPitzxw5nTsHV73h9mxvtwUYUuEnzn2m5CQhAHaVgO3eN0kblLhJA-8zqWeH5kxZBd2zJsC-CE9rFHGQnGnntBYCQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: در حالی که ترامپ مدام از مذاکره با ایران حرف میزنه، طی چند روز اخیر گسترده‌ترین تحرکات نظامی و لجستیکی آمریکا تو منطقه گزارش شده.
به گفته برخی منابع نظامی، آمریکا در حال آماده‌سازی خودش برای یک جنگ تمام‌عیاره!
@WarRoom
اتاق جنگ با یاشار: هم اکنون، در هنگامی که همه در مراسم سناتور فقید لیندسی گراهام هستند، یکی از سنگین‌ترین ترابری های نظامی آمریکا در منطقه انجام می‌شود.</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19929" target="_blank">📅 23:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19928">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تقدیم به نگاه زیباتون ، بشوره ببره
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19928" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19927">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19927" target="_blank">📅 23:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19926">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19926" target="_blank">📅 23:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19925">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فاکس‌نیوز:محور اصلی گفت‌وگوهای آمریکا و اسرائیل، تصمیم‌گیری درباره گام‌های بعدی پس از حملات اخیر به ایران بوده.
همچنین نتانیاهو احتمالا اسناد و اطلاعات تازه‌ای ارائه کرده که نشون میده جمهوری اسلامی با وجود صحبت از دیپلماسی، همچنان برنامه هسته‌ای خودش رو پیش می‌بره.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19925" target="_blank">📅 23:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19924">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19924" target="_blank">📅 23:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19921">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfrzB87cjIY2Rld8aYrCrHR3m4QAlk5ZiuKiIcf_QCyYxyP3qofR8hpqtrfvkR1hyxBLJIKXJkunpV7szsDyX5T2my-XLZ6chXT7m0cOzBS_pA3tQIob7Qx3pcBRu50XYefgNXG-0mmAi5jPL4xPoVqcupCevf2_mPST7Qx6ITxF33Qexp4suNbfGAjHTZBBLq11hQIdhSef5gdTCpcQYyHRRS5fPBq1J56WDoava3pijko3CGEezl-1Y6bG8YIg9h5vjdauW6_weSXo18FCjlsBrxVtOxjAUMZ4Hxyw6eXEP5U9mZKlCIPrYNV5F52exOVgnEvZvcWWg4DqXh4rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZ6btOhZVSNiab6xSyoNJ0GHpxaPg-hInIjVsqm25zu8-hwQ8uvulDcqv0WLm4d1eYQ7FJcdZPfv3cUpi4C3vwkrM-b11nQ5IsWfgMwP3b_kkzeJzsmgQ91eKBtnZJmvObmfvWqKfIBDDDud0USxB_1lmhdYTbxNA9qo33d9KStczDdIWU8Bo3EnTtZh2uBVEbem6S9CSzvpztrLHd1HDfzLU4UbAHySC7_CMIVhkZeLpEDMCDPMhgIHRISuB3UOZzYqKQcnSnlWIkzkzU5mQJKgoE98nomVV2HoimWs8A3gfbWOUOfg3YhGraiOryj-zSOVqpBbsiVLVRTTOxysRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehqn8ogTrCZvUQch4zOc1iXeUa0sOIp1qjH3DjCtlh3ssPFeWYOWBlJSxqZMPdsk-FuK3Rz1GHw3MlL9E5JjtM_QhfjeR87Y4lPBh_e6Hn63spR93lOO4zofYlqgpQhBwa3tCJ3xQfHLxeAAhYrE4U1LB4Ky7BxHfRLBM3ZccDU7_yYx83nkMbMpg1MoT0fGVoHNJ67kJIWn-3mRuy9-CaPiKmP1fkw1O9BlEs7kAhEPwLd8umFuI_D03WvLV1jRFlnN6z4XTQlSqDmk5iSfmb1rHHN20WLoS5FTGmi6BIU2M0Gy1t2GejyF8qeO1cJWIv0tVOGkH-34YX0eQ5aQmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین تصویر شاهزاده در مراسم درگذشت سناتور فقید لینزی گراهام که با اندکی فاصله سناتور تیم شیهی که صحبتهای جنجالیی درباره ایران در سنا کرده بود و ویدئویش را برای شما گذاشته بودم دیده میشوند.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/19921" target="_blank">📅 23:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERA_AFgWA6g1wGy3XgEe6W-BhsyNQb4tojuFcsHz-fsNFzN66N10MvPuu9uKk-zrMUD4_WCedPb3NBImO7sAIGckRKsTIq4BcCa6iQVBLoPCLqLzqmzzSGiG2-8S7PWvJatAQP3TjHa1YPWYOBa-XYdgcIiLu6Xa-5EBx1cRdrCqu7ZWn0mMyfyCUykZd888FA5PmJ1ex67fFlczPdsbtpbz9ebbOASTeMMLL-_dEvC_NxRP84cXbfPgzBRNPOVV6WFfVDvqeG3-bEb9mWaNLQ-kyfXNLTZW6e5hpTKOLeNxPRCTukOCwyNVOzzWeNJJ7Z2fU3Oyt9JFmn8THJjuYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rri5uNorsWnK77ze2rTjRcgu0iSBUdQj0ehk-HYE24ajcuzbBNWvbyoW26bZ4psqBLCSs1ebIjaGW9owM_0HafEmduE59g8nWUzQNuROWjPxWpCnB4SwHiNo_bO1yU1XW9L30KaNIbr0jhaiCajwpSmH0vKCVz7DcuCNWNYxrC-mXMmcnmkLRd1BYTjJ9FZbnuW7z7rvuxNg2wxSJRAExKEUXvyQ8-Iyq1xMlXRpezxrdqMktTJ3rl369QUjSZScj8P-q3XBe_ejKlWG7QF_5VkJB0mAqJyiUBnZgclWU0Rj5_aU0zh-3DJUz3KPZxiO30miNFmTe_UgyIfIh2A1ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهزاده در کنار کامران خوانساری‌نیا در مراسم
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19919" target="_blank">📅 23:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19918" target="_blank">📅 23:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19911">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اکسیوس:ترامپ و نتانیاهو جلسه‌ای به مدت ۹۰ دقیقه برگزار کردند که به عنوان یک جلسه سازنده توصیف شد و تمرکز آن بر روی ایران بود، بدون اینکه هیچ نشانه‌ای از اختلاف نظر بین آن‌ها دیده شود.
دفتر نتانیاهو تأکید کرد که اسرائیل، واشنگتن را در مورد ایران تحت فشار قرار نمی‌دهد و هر دو طرف در یک هدف مشترک برای جلوگیری از دستیابی تهران به سلاح هسته‌ای، سهیم هستند.
همچنین، دو طرف در مورد امکان عادی‌سازی روابط بین عربستان سعودی و اسرائیل گفتگو کردند. موضوع فروش جنگنده‌های F-35 به ترکیه مطرح نشد و ترامپ از اسرائیل درخواست انصراف از مناطق تحت کنترل خود را نکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/withyashar/19911" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19910">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9ed022ed.mp4?token=Q-RdvZUzd0O-DDfC1GcALdW-F0u7F2wRGO0mZmCBL6theKVnPmUwx-ZMGDaFYE0HkjZKXUG3U6pT6gczAXr6A5BgNBHqBPcVaTDHiKyye1MUdtRp8ekL_86FYIlR9nQKODZd_Bz_-LCR9Wz_2yohd_Wcn6BYsCDVyxROXnDITL_Sy5r9kr-tgnEGxiOfZ9gM7vEBDrzuW9X4-mTdLXWIRq42WqKLFMxZx6eLuW5EsJwvc-TlAuT_xV-cANkVqVvbIho11UfahSFn95LsSMSGtY0n4SJkehk9cavQb6vkI2PPXcCOJyX1RsCqj4UGoWeP82-cfEvUNZStn9P8_Go38w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9ed022ed.mp4?token=Q-RdvZUzd0O-DDfC1GcALdW-F0u7F2wRGO0mZmCBL6theKVnPmUwx-ZMGDaFYE0HkjZKXUG3U6pT6gczAXr6A5BgNBHqBPcVaTDHiKyye1MUdtRp8ekL_86FYIlR9nQKODZd_Bz_-LCR9Wz_2yohd_Wcn6BYsCDVyxROXnDITL_Sy5r9kr-tgnEGxiOfZ9gM7vEBDrzuW9X4-mTdLXWIRq42WqKLFMxZx6eLuW5EsJwvc-TlAuT_xV-cANkVqVvbIho11UfahSFn95LsSMSGtY0n4SJkehk9cavQb6vkI2PPXcCOJyX1RsCqj4UGoWeP82-cfEvUNZStn9P8_Go38w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره لیندزی گراهام گفت:
او به‌شدت جنگ‌طلب بود.
راستش را بگویم، هیچ جنگی نبود که از آن خوشش نیاید.
فقط دوستان نزدیکش منظورم را می‌فهمند؛
اما او همه این‌ها را برای کشورمان میکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19910" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19909">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک منبع آگاه گفت مهنام نواب صفوی، ۲۲ ساله، خواننده رپ فارسی و از بازداشت‌شدگان انقلاب ملی دی‌ماه، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد به اعدام محکوم شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19909" target="_blank">📅 22:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19908">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3QlfHd1M-3Sx2ILHze9MzGGVsk1ftbeT1fMs6xR7l6pCNMHj871B3gwYBh5vZSBRgdMo-hnn8vwuODuJZpR8SGSsWjEQLMvt-NdBIE-_Y6KeI7AExPMMmBN9Sd3wzdr-jEp55XG64mNLZvTJqKJFdAGfWSamTAnyeMi_M4h4EedJpJzusW-RC9r7XXrosSvhjUrPy7qjNBqWpIhIAF_G06-VxcwgfwnyQLqf5wfsa1DtJmXzS5eYOv6rLPhYkUkyHFjG19jbJiygz8YrIMagFf3BsNv0h_QQWCeYNRnWxvnj9p4BEYeYxz0LpOpMJbqwlY6K92OzDcHHgmtMkVXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز : علی واعظ، مدیر پروژه ایران در گروه بین‌المللی بحران، یک سازمان پیشگیری از درگیری، گفت که پس از ملاقات با رضا پهلوی در ۱۵ سال پیش، به این نتیجه رسیده است که او اشتیاقی برای کشمکش‌های سیاسی لازم برای رهبری تغییر در ایران ندارد و از آن زمان تاکنون هیچ چیز دیدگاه او را تغییر نداده است. اما پهلوی به رویترز گفت: «من از حمایت زیادی در سراسر کشور، در داخل و خارج از ایران، برخوردار هستم.»
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19908" target="_blank">📅 22:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19907">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال ۱۲ اسرائیل: نتانیاهو به ترامپ تأکید کرده که حملات بیشتر علیه تأسیسات هسته‌ای بازسازی‌شده ایران حتمی است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19907" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19906">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتانیاهو:من همین الان یک جلسه عالی با رئیس‌جمهور ترامپ داشتم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19906" target="_blank">📅 21:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19905">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">instagram.com/yashar
LIVE NOW !</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19905" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19904">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19904" target="_blank">📅 21:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19903">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19903" target="_blank">📅 21:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19902">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06b2086bda.mp4?token=MOh6eKB4HwYxcnIyqx2wjw9F2THrT6qm9d7dx0rHfO6gr4hjyqGWVuH-oCYKWq27dL9_FKTqKpUFcvMSHdxvVXJ_17481V1T1dZYviT-ptmAoMNdlOWwnvCA0DKKqcvbpqBilBy5ci4pDkTo8ay0AT6h32fgKoGc07pJHonYiSyJtFWfer7hHNGwnj9pY0UBn_RlJO_4A9OBBArHyIuK1lq2GeAxYp22aMCb5HSt1gdjtiK1F2PHgj0q3EzT-6SuboylZI4dO4a00B-PHgyyQ8mY4chDYTjP6URZRHxYVv57hBtnoUT645e8_qph9RurROf_ND_kbhI2pr_lnTLYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06b2086bda.mp4?token=MOh6eKB4HwYxcnIyqx2wjw9F2THrT6qm9d7dx0rHfO6gr4hjyqGWVuH-oCYKWq27dL9_FKTqKpUFcvMSHdxvVXJ_17481V1T1dZYviT-ptmAoMNdlOWwnvCA0DKKqcvbpqBilBy5ci4pDkTo8ay0AT6h32fgKoGc07pJHonYiSyJtFWfer7hHNGwnj9pY0UBn_RlJO_4A9OBBArHyIuK1lq2GeAxYp22aMCb5HSt1gdjtiK1F2PHgj0q3EzT-6SuboylZI4dO4a00B-PHgyyQ8mY4chDYTjP6URZRHxYVv57hBtnoUT645e8_qph9RurROf_ND_kbhI2pr_lnTLYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19902" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19901">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کاخ سفید : پایگاه مشترک چارلستون در کارولینای جنوبی به افتخار سناتور فقید لیندزی گراهام تغییر نام خواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19901" target="_blank">📅 21:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19900">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مقام اسرائیلی نزدیک به نتانیاهو:
ما در یک مقطع حساس هستیم. رئیس جمهور ترامپ به زودی تصمیم میگیره که کدوم سمتی باشه.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19900" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19899">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19899" target="_blank">📅 20:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19898">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال 14 اسرائیل به نقل یک مقام بلند پایه : ترامپ و نتانیاهو بر این موضوع تاکید کردند که هدف مشترک آنها، جلوگیری از دستیابی ایران به سلاح هسته‌ای است
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19898" target="_blank">📅 20:35 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
