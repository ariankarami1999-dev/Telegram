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
<img src="https://cdn4.telesco.pe/file/Ndhhce3dJbQNgk54-8hnYP35qtbxE0BO76V8B7GE58wipUrYlnWLc1ixetFslxzA-_VdYGMzz8QDF8d5ksNtPm4UlKqB66ZRUVYH3Ny1DlK-gEP6E1RCRxbP_4HVg_ADmsgfIH7gyiOf8FDS7fiHFrsz3t5LVA1IK9lD7yutUHUWHJzxGs-lI8k_47omJBTSVabrIdZM0_isru86vgalRoWJgny8MaqFO9UGRM8v6ivF5bHNCJGDxYyOvYibs36bMgRg_HcvckY7iSF-oOb5D9MtBbeaMw6A5dnyPNZlYTnPuzZwhKrD3CpBaCcZAYUxB0RotS68XRjKD4GKtlh-_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-151995">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل به نقل از یک مقام امنیتی: مذاکراتی اخیراً میان نتانیاهو و ترامپ درباره حمله به ایران انجام شده اما تصمیم نهایی اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/151995" target="_blank">📅 20:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151994">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
نیوزویک: ایالات متحده حمله به ایران را بزودی انجام خواهد داد
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/151994" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151993">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سپاه: یک سوپرنفتکش متخلف حامل نفت خام در یک آتش عظیم در حال سوختن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/151993" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151992">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل به نقل از یک مقام امنیتی: مذاکراتی اخیراً میان نتانیاهو و ترامپ درباره حمله به ایران انجام شده اما تصمیم نهایی اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/151992" target="_blank">📅 20:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151991">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f635d314c6.mp4?token=AkOpw7DdJD7lBR_d5f7ikwDD6ODrBTXxK8_DZQHJcSIQpXRoDzw4DU48_FiePtjV9p3tiRNglQTCw_9feFpaSpPnDAb0Y5BK4uuuf8SeRjwHft6eUkmsEI-5vMrsc9TrHQqtyyYmG_KbKcF8AUL0ljokpyseZVLfqqKF2ZPRwa7HVHyiSRbMfEw0MLPddq8CxSFf1hs1ZIrVYtXe64vWjX1V9LB3SrzUQIhbBq9Xgc5adwU0AdJ1KDUZs_gpGr3S1yyqU0b39zV4kSfa3rX6eNzl1wdNofmfdEZMEDBXwZHw1dFtcFr5vvxhLCq9YFMeZGkXriJK5Y1rGIRAXDTnIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f635d314c6.mp4?token=AkOpw7DdJD7lBR_d5f7ikwDD6ODrBTXxK8_DZQHJcSIQpXRoDzw4DU48_FiePtjV9p3tiRNglQTCw_9feFpaSpPnDAb0Y5BK4uuuf8SeRjwHft6eUkmsEI-5vMrsc9TrHQqtyyYmG_KbKcF8AUL0ljokpyseZVLfqqKF2ZPRwa7HVHyiSRbMfEw0MLPddq8CxSFf1hs1ZIrVYtXe64vWjX1V9LB3SrzUQIhbBq9Xgc5adwU0AdJ1KDUZs_gpGr3S1yyqU0b39zV4kSfa3rX6eNzl1wdNofmfdEZMEDBXwZHw1dFtcFr5vvxhLCq9YFMeZGkXriJK5Y1rGIRAXDTnIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من جلوی چین را گرفتم، و جلوی تایوان را هم گرفتم. این روند به همین منوال ادامه دارد. کی می‌داند چه اتفاقی می‌افتد؟ اما من جلوی آن را گرفتم.
🔴
من از وقوع هشت جنگ خطرناک جلوگیری کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/151991" target="_blank">📅 20:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151990">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=H6BZuK3QxZn3T8CwPu5dtDkFU6OQnKbgV-bQvG6N_CZvyzK18kuRULMVq5lXZcfZMEt2ANJCRGqpMEfO6tsoRvzwPvP8ZTFT4KXYyQrrUY8eQmA60WrmsWQ_W3XLpDQhHA93eg911jGHWx5tGEJ7WIfnGNVGPMMH6AYzfNqF9135f4HyfYwHKKXv9r2ZkEyn0cSnveBdb8AGAdmnl0W4V9lJJx4BpL7XctSeALGn3Qf5I8ZpinESSZv5ooUXsy_wtKaoIasc5WQa1VIETAiXM7F54A3Ft_wZfyNZAL2aK4mQnBK4FT9wtDzncELGahI2xBOGTF0zfLS7pN7-YjfuEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=H6BZuK3QxZn3T8CwPu5dtDkFU6OQnKbgV-bQvG6N_CZvyzK18kuRULMVq5lXZcfZMEt2ANJCRGqpMEfO6tsoRvzwPvP8ZTFT4KXYyQrrUY8eQmA60WrmsWQ_W3XLpDQhHA93eg911jGHWx5tGEJ7WIfnGNVGPMMH6AYzfNqF9135f4HyfYwHKKXv9r2ZkEyn0cSnveBdb8AGAdmnl0W4V9lJJx4BpL7XctSeALGn3Qf5I8ZpinESSZv5ooUXsy_wtKaoIasc5WQa1VIETAiXM7F54A3Ft_wZfyNZAL2aK4mQnBK4FT9wtDzncELGahI2xBOGTF0zfLS7pN7-YjfuEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: شما گفته بودید که قبل از انتخابات میان‌دوره‌ای به ایران حمله نخواهید کرد. آیا این حمله اخیر در عربستان سعودی این موضوع را تغییر داد؟
🔴
ترامپ: ما این موضوع را بررسی خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/151990" target="_blank">📅 20:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151989">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a642012a0a.mp4?token=kf4aNeqrCxJvMQnAfjW7nt53QmAUEJ8uDv4IoG8bMO4hyfTUrB6dBjECx5gMDKsBFNNYdx2uEnaPSoAPdpgtmmzGpHLF9QoY-20WT_gnUFgzYFeCjaw58EKq1vTExgg8jz50Qcw3kZWe1cGYvC_3K2hv43y4niiXsHzs2RYOnRCQ-187Y55nBMzBPPaT5kz-fxoSZCx2LqaZvmo7Q-prqoG7Y17jl01ynr0xVDNj72ebs4hjLqGCGHXESilqXFEH6aagGJVZoDH8-7oKgtRabVYAXy3kiTnas34oOvgeiVDq2TDafdiprJQH2PPDcRn2F113RsNM31XoktfxmNwmaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a642012a0a.mp4?token=kf4aNeqrCxJvMQnAfjW7nt53QmAUEJ8uDv4IoG8bMO4hyfTUrB6dBjECx5gMDKsBFNNYdx2uEnaPSoAPdpgtmmzGpHLF9QoY-20WT_gnUFgzYFeCjaw58EKq1vTExgg8jz50Qcw3kZWe1cGYvC_3K2hv43y4niiXsHzs2RYOnRCQ-187Y55nBMzBPPaT5kz-fxoSZCx2LqaZvmo7Q-prqoG7Y17jl01ynr0xVDNj72ebs4hjLqGCGHXESilqXFEH6aagGJVZoDH8-7oKgtRabVYAXy3kiTnas34oOvgeiVDq2TDafdiprJQH2PPDcRn2F113RsNM31XoktfxmNwmaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جنگ اوکراین: اگر من رئیس‌جمهور بودم، این جنگ هرگز آغاز نمی‌شد.
🔴
هیچ دلیلی وجود نداشت که این جنگ بین اوکراین و روسیه آغاز شود
🔴
این جنگ به دلیل نالایق بودن برخی افراد شروع شد.
🔴
نباید هرگز آغاز می‌شد. شما نباید ۳۰ درصد از خاک کشور خود را از دست می‌دادید
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/151989" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151988">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d6ccae64.mp4?token=rZjrvsZ1ggEQPP_5Vu6RjE_FlBaJ9CEvGq6zXkef51NSyVhwVIorOVX3L5OQ0iQXO0K9gIFDzCSM6fsKH1XyRR1clQLSUvQcHLkwpv5pDJUFCOkagaMGvaEFkluSJXN6j8Xvg1CeYpMfGbWz7Xc4X5-5tcS6lReQtz1_apvDmMfTYs_C0_lU38yP3aLvB-xal4tm6B8eAsnQm1FMbdors86_1V3OWEFURV8uiHq-_5A5lpGL4PtxZmnG8__ASDiLO0yHd_GLoDeu0-SSd0gRdIGGl-Z9ZHFZTsnu4Ll0sDdrE1PF6I2ejH1oE4T0z3nWlFj7y_tKZTzuwpeW3lCgZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d6ccae64.mp4?token=rZjrvsZ1ggEQPP_5Vu6RjE_FlBaJ9CEvGq6zXkef51NSyVhwVIorOVX3L5OQ0iQXO0K9gIFDzCSM6fsKH1XyRR1clQLSUvQcHLkwpv5pDJUFCOkagaMGvaEFkluSJXN6j8Xvg1CeYpMfGbWz7Xc4X5-5tcS6lReQtz1_apvDmMfTYs_C0_lU38yP3aLvB-xal4tm6B8eAsnQm1FMbdors86_1V3OWEFURV8uiHq-_5A5lpGL4PtxZmnG8__ASDiLO0yHd_GLoDeu0-SSd0gRdIGGl-Z9ZHFZTsnu4Ll0sDdrE1PF6I2ejH1oE4T0z3nWlFj7y_tKZTzuwpeW3lCgZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آنها جایزه صلح نوبل را به شخصی دادند که هیچ‌کس از او چیزی نشنیده بود. تنها چیزی که ما می‌دانیم این است که به نظر من، او بسیار ضد اسرائیل است.
🔴
مشکلی در نروژ وجود دارد، اجازه بدهید به شما بگویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/151988" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151987">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb64bf3ad.mp4?token=heug5B2w8T06lsuESd8kM258zEEn3A9cTKf9ZoC8eyPjFmXVfBHtQQNSSZyxnl2PyfYd66TaYK12BUt1uPnjszxx-i0GekrzbMIXcrckPk3wRynu-CjhM6IH1Pj8mKctZrv39robfQbBnzTv9iXHyoSIqqvAXzeYzgPsSUcC5OkJjwJoIHMoPBDwghJaVqw9vhNRXReVOYlwciCjGDuPit6wz2uNgW-KWhY2jiV6EaXFBwoqfLQ59cCm138yh5HPTG9nBg1XeLh4icsicWPZL9ZL0waLBKSECR4fKhLcpI9Jn6B3sl_bPf1XLdkqrIkHaqL0CKxJPoKBh01GhzciJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb64bf3ad.mp4?token=heug5B2w8T06lsuESd8kM258zEEn3A9cTKf9ZoC8eyPjFmXVfBHtQQNSSZyxnl2PyfYd66TaYK12BUt1uPnjszxx-i0GekrzbMIXcrckPk3wRynu-CjhM6IH1Pj8mKctZrv39robfQbBnzTv9iXHyoSIqqvAXzeYzgPsSUcC5OkJjwJoIHMoPBDwghJaVqw9vhNRXReVOYlwciCjGDuPit6wz2uNgW-KWhY2jiV6EaXFBwoqfLQ59cCm138yh5HPTG9nBg1XeLh4icsicWPZL9ZL0waLBKSECR4fKhLcpI9Jn6B3sl_bPf1XLdkqrIkHaqL0CKxJPoKBh01GhzciJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره پخش زنده اعدام نیدال حسن، عامل تیراندازی در فورت هود:
شاید با نشان دادن این اعدام، افراد دیگری از تکرار رفتاری که او انجام داد، منصرف شوند.
🔴
من در این مورد تصمیم خواهم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/151987" target="_blank">📅 20:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151986">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / ترامپ: در جریان حمله به فرودگاه ریاض قرار گرفتم و تصمیم خواهم گرفت؛ شاید به حملات عربستان به یمن بپیوندیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/151986" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151985">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: زمان آن رسیده که اوکراین رئیس‌جمهور جدیدی داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/151985" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151984">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: زلنسکی بارها می‌توانست جنگ اوکراین را پایان دهد، اما نخواست
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/151984" target="_blank">📅 20:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151983">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ: ایران در وضعیت بدی قرار دارد
🔴
خبرنگار: چرا اقدام نظامی علیه ایران را به بعد از انتخابات میان‌دوره‌ای موکول می‌کنید؟ چرا همین حالا اقدام نمی‌کنید؟
🔴
ترامپ: ممکن است اقدام کنیم. خواهیم دید. ایران به‌شدت در حال شکست خوردن است. ارتشش شکست خورده، نه نیروی دریایی دارد و نه نیروی هوایی. تورم این کشور ۳۰۰ درصد است و ایران در وضعیت بسیار بدی قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/151983" target="_blank">📅 20:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151982">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQyPtPIK7k4tvfOZcBuOJ6qNxkoL4qCG7oOPxLnD1J0mmZLnsnzQl2nA176Gqld89734wlWnz_s-hFlYXbGYqDioBoSfdhN1cFK_fNRDf06vgRKSYTHxcpnPzOl_fQ9TtugEwSY6_RNRP5hCns_CkHmzg4Fj9a4itK89CBz54wAX34Bj6aWXA6txgBy-PzdY9yna_P0ArHkJytklaqogE26TN6jl7mSJZYqdHgUxlmbWSOaInLLpdA8MOIT8tjM8hylieeOdquGdXaAu6srSpkKxJwTp36otPwteECK2VM-Ksszio46MdX1rnNObR6aLFjxe5zvSMNbJK9U9SkJ07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۱ هواپیما از فرود آمدن در فرودگاه جده خودداری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/151982" target="_blank">📅 20:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151981">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGLP2tfXVeDM_0PLs0vWgLwk3P-yfnb02YPlcGSom3oK5yHKaTDbK7FK9Lw_UujKOVkYqFo-0l9pJxayDmvs-9vOZT9OELvC4yik_mCubIUw7gZqpPXhL_yluGdmin6rfa4fwVzl1jbIq5WdeNmOabCQE6MHJiXvcqbQ-_N0OWxG0vJCM9aHLkHV-lc43-pmfUCsfAD5aqhiseCTXZYjMiNxvZZvDyYWty48kzaguUCRQ6yiq4JMPBPlWsRyISJoIKz67nTDOObOLn8SqhsB_M7xiAkMmaE1mIxC_nTeN9P2anG9Gx-oLCzk41xvBZvkDy5KvD92Lp1Noh7pfcTU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون هواپیماهای هشدار زودهنگام سعودی بر فراز ریاض پرواز می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151981" target="_blank">📅 20:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151980">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
روغن با افزایش ۴برابری، رکورد گرانی سفره خانوار های ایرانی را شکست
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/151980" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151979">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت ارتباطات: در صورت تکرار جنگ، احتمال قطع اینترنت وجود دارد / مشخص نیست که این موضوع در چه سطحی انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/151979" target="_blank">📅 20:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151978">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ایالات متحده از شهروندان خود درخواست می‌کند از سفر از طریق فرودگاه ریاض خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151978" target="_blank">📅 19:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151977">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرگزاری تاس به نقل از منابع روسی:
ویتکوف و کوشنر طی دو هفته آینده برای دریافت پیشنهاد پوتین درباره ایران و اوکراین به مسکو سفر می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151977" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151976">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فرماندار ایالت پنسیلوانیای آمریکا:  در حادثه تیراندازی در شهر اِری در این ایالت، ۹ نفر کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/151976" target="_blank">📅 19:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151975">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
تیراندازی پشتِ تیراندازی ۵ نفر در جورجیای آمریکا کشته شدند
🔴
رسانه‌های محلی خبر دادند که در پی تیراندازی در یک اقامتگاه در شهر داگلاس آمریکا، ۵ نفر به ضرب گلوله کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/151975" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151974">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6726b774fe.mp4?token=qBTkVyO7AiQH847eUvC3W1O67mBFoN02euFsLM7fWvAv2t57SSpc0nCIw4BXYltXLaWD4WEqguJqlkjvjiW3finXyLH8637ZrAAC3wrMYYKPdXV5TVfvWclz5vPKUyFspE_tY2fnYU-HkjSwtCoYWOO283Iyx81x2G6tdsO7JIqf-I7u8ninHj8g9Xsi8_YEqGYFydMMh6n4uBPexfi5UgmKrdz8hXtlNlnpMuIqtczmKSlVZvREFjvuYq3q7ynv6wMiusn936YBJvDdPaB4znbvpIsfap1sZndj5f4nfpIJbiYWUeS-3k2k1wphhMJ0WDkqRbw_KbegucZurGTRyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6726b774fe.mp4?token=qBTkVyO7AiQH847eUvC3W1O67mBFoN02euFsLM7fWvAv2t57SSpc0nCIw4BXYltXLaWD4WEqguJqlkjvjiW3finXyLH8637ZrAAC3wrMYYKPdXV5TVfvWclz5vPKUyFspE_tY2fnYU-HkjSwtCoYWOO283Iyx81x2G6tdsO7JIqf-I7u8ninHj8g9Xsi8_YEqGYFydMMh6n4uBPexfi5UgmKrdz8hXtlNlnpMuIqtczmKSlVZvREFjvuYq3q7ynv6wMiusn936YBJvDdPaB4znbvpIsfap1sZndj5f4nfpIJbiYWUeS-3k2k1wphhMJ0WDkqRbw_KbegucZurGTRyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی وایرال شده از یک مدرسه پسرونه که معلم داره درس میده و دانش آموزا ته کلاس دور هم جمع شدن و کله‌پاچه می‌خورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151974" target="_blank">📅 19:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151973">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBsTX4KwUkSjTtf2SqWso2rg7MjONbWEpeHl1lAziO0ZWgPa0b3fqTbSGEvJ5z9ki2UWmnBg9V9Vfp8cZSMrFP9iUydncllTxw_b6kVDsaBbprsbOk_cIr7f5H1San2rQgQB29kHG8_UxwcKa0tPOszgV5OkuEyY5NEEPkRQzGY3xXiL5dLcNvTSh4XghMsRlnqt2oats9e-q3LNcvNTOhxuKGlVi3_pc4y58fUpe4Dn89kuOnmFabczEUrsW-_M5r4J1kJy45xn1E9d-5ccMy7eCWm2eDkFCjWnF97nat5Iy1gNtbZA0OCpACy-zYQQEncO1xnUViVDfXy-rVefcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدمت چوگان ایران در برابر گلف آمریکا
🔴
واکنش سفارت ایران در ایروان به اظهارات روبیو
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151973" target="_blank">📅 19:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151972">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8e7gFTqQiiPUiwLtBTjmo80msijiFXGbm3UeW5WmVHWjXrY2Unnz2-RtJtFRnasQGDoyG_-o11_9T4ZXtygxTEu0gUalbX3SZu7xUBrBPFIT0rp29XZ0mQq13LUlNnYJ2LSApTPfdCjQcPXEdtBsezFum9TH_dzligkloUOwNZQx-Uxs9zFxXhm5Ziz7pFCj0CVfipXjXOH-DZAxBBDp7HMiFiFD-HFSVcG32Be4UFdBx9eIoRNOffzyFEeRMF0LqbBuQDLKMaqeS-iXt2buL5lcRkURJkzei-4l-dxJxgTzkRUOM1w1x-4H0OBVC0flTxQKnXJiKMla7hPBF-5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلمان، کانادا و اسپانیا به شهروندان خود توصیه کردند از سفر از طریق فرودگاه ریاض خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151972" target="_blank">📅 19:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151971">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
اتاق جنگ اسرائیل گفته به نیروگاه حیفا حمله کنید ترور می‌کنیم.  ایران مدعی شده موشک های خوشه ای مونو هم هنوز استفاده نکردیم.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/151971" target="_blank">📅 18:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151970">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تصاویری از ترمینال شماره ۳ فرودگاه بین‌المللی ملک خالد در ریاض، پس از حمله موشکی توسط گروه انصارالله.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151970" target="_blank">📅 18:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151969">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b28f6687ce.mp4?token=H3tw9e_AJx7-mHc-b_d7zY4THDiJUfSqG1UZ9KJ-c3qcQRRXm2EazjZyMr1WJAMnEBQArg6NsS-cjvdZgy5txKDXX8so41zFhGD35HclKzz9ez19JsU3zAuRmSlxSTkrr9XGuab2A3tj3WuAIYJOwlrUfNK1Y_bgrm4DdSEHpKeXAkXbbmx2Uce_XrbdkTYN-3jg_Xg7fYAHWF1Sjch0eARQura7V6unPzvzY_ef5KEKfNNqeVGmU6cp6myh51mgDJuG0rRQz4OzMnCjTn6ZbN0FpuKnF1o8CXQ2mWjD5uBbtCVUtMmxvFOhqx4cA1ITxZG2Dkq9J80amdMal8xBqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b28f6687ce.mp4?token=H3tw9e_AJx7-mHc-b_d7zY4THDiJUfSqG1UZ9KJ-c3qcQRRXm2EazjZyMr1WJAMnEBQArg6NsS-cjvdZgy5txKDXX8so41zFhGD35HclKzz9ez19JsU3zAuRmSlxSTkrr9XGuab2A3tj3WuAIYJOwlrUfNK1Y_bgrm4DdSEHpKeXAkXbbmx2Uce_XrbdkTYN-3jg_Xg7fYAHWF1Sjch0eARQura7V6unPzvzY_ef5KEKfNNqeVGmU6cp6myh51mgDJuG0rRQz4OzMnCjTn6ZbN0FpuKnF1o8CXQ2mWjD5uBbtCVUtMmxvFOhqx4cA1ITxZG2Dkq9J80amdMal8xBqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ترمینال شماره ۳ فرودگاه بین‌المللی ملک خالد در ریاض، پس از حمله موشکی توسط گروه انصارالله.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151969" target="_blank">📅 18:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151968">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
خبرگزاری تاس به نقل از منابع روسی:
ویتکوف و کوشنر طی دو هفته آینده برای دریافت پیشنهاد پوتین درباره ایران و اوکراین به مسکو سفر می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/151968" target="_blank">📅 18:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151967">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek0YtkxEe5muZKg22fPSFD8P9yH5Y7lX3G2GHvCR9ZCUyaOFOjffisi_1y-xXLQJd8UWODrwRLcG0Ge3WyVgpIzLvB2c0Y4iLNHBycLSqgmyvENdpZqXyTM3vCyPSKXPSQ4a-dfHKB7CuhwS-E6-h36uqskIy1vQ0Adl-6sWy-DIYjBs_utMJ9OFGm4ZG6Fmy-708P9Fz42yY7ApFtPJVcW58i4-4cd8jGvMwkxnTmD4jlFOKJNAPp9RPBQu6KklqwQ-o-ZDczA4zdz8G-V7TTpx9N9IsNSp-I1j03sLZb_r2uh0LYLqIfRgI515gfj-93J--iZ98AuIlAaAZ25vZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست: پخش زنده اعدام؟/ ترامپ: موافقم
🔴
کارشناسان مجازات اعدام که با رویترز گفت‌وگو کرده‌اند، پخش زنده اعدام حسن را نخستین نمونه شناخته‌شده از پخش عمومی یک اعدام قانونی توصیف کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151967" target="_blank">📅 18:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151965">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=augQKQNgXqf848Ge-V1CNmSjskeeIqDB7QtN-XMKNhQOI_qY_FAnzDzyagdL7hq3KSRtAjVRJuI7T4aEG1--S8F0z3Xh5SM5wcimLa3N2dIvsWYrhYxdJNWaKcMM646WGQDGAqitLuHca6E_70L6_0vGa9kYudaXi015BgjOBaUXVQGHDu-R7LSkN6r4xujMbSkf0eTghMzN5eOu1wre1Xm7zEWy9JBEJsr0uePY7UOua4ORGvHajYHAWUbuaaSytOtFtHIkWQZk-KLOkq3Bmj9anQidhSyJNYuZ944pbbZ0AkLSwcPhGpT_uMEpmxQftJC08hxA57ZvMPEimQJrtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=augQKQNgXqf848Ge-V1CNmSjskeeIqDB7QtN-XMKNhQOI_qY_FAnzDzyagdL7hq3KSRtAjVRJuI7T4aEG1--S8F0z3Xh5SM5wcimLa3N2dIvsWYrhYxdJNWaKcMM646WGQDGAqitLuHca6E_70L6_0vGa9kYudaXi015BgjOBaUXVQGHDu-R7LSkN6r4xujMbSkf0eTghMzN5eOu1wre1Xm7zEWy9JBEJsr0uePY7UOua4ORGvHajYHAWUbuaaSytOtFtHIkWQZk-KLOkq3Bmj9anQidhSyJNYuZ944pbbZ0AkLSwcPhGpT_uMEpmxQftJC08hxA57ZvMPEimQJrtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از فرودگاه بین‌المللی ملک خالد در ریاض، پس از حمله حوثی‌ها (انصارالله).
در این تصاویر، خون روی زمین دیده می‌شود و نیروهای امدادی در محل حضور دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151965" target="_blank">📅 18:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151964">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQnYUMnh1ysXu3CXtaZQPTph4QA9_QSppw5sUAM6uBn3xAQbPBw4jy3eH57d6YlUDumBXUKpJgpkE-zn5lRxMAnsH-ngQbipJubPDzkTpRtDOyKE0q6CTkIZNVxtaNwsaar5syZOUXxfol6GSbXtXO00DzgL_HrBgEO0woNr6r2rc-n1EouOQnbrVfX6OlZodYMGIlPPSfdU2W0YKjC-pt9cvMmPrkhaRA-2tukekk_hMwqUWZfXXaC7I4x2A8plzt7Gj8GadlF5RhIdZtAC8MDOe8qLDiPcrR-TZtYCiqIFw4bUvpzrRDHNlZQbjeUjz722ketc_hd5PEfgicuMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یادی کنیم از این پیشگویی تاریخی
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151964" target="_blank">📅 18:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151963">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
بانک مرکزی: بانک‌ها دیگر اجازۀ فروش طلا ندارند
🔴
بانک مرکزی با صدور بخشنامه‌ای ورود شبکه بانکی به خرید و فروش آنلاین طلا و نقره را ممنوع کرد.
🔴
مسئول گروه فین‌تک بانک مرکزی گفته این تصمیم باتوجه به بروز ریسک‌های عملیاتی جدی در یکی از پلتفرم‌های فروش آنلاین طلا و احتمال سرایت آثار آن به شبکه بانکی اتخاذ شده است.
🔴
بانک مرکزی این تصمیم را از ۱۳ مهر گرفته و کاربران بلوبانک سامان نیز از هفته گذشته اعلام کرده بودند که امکان خرید طلا در این اپلیکیشن غیرفعال شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151963" target="_blank">📅 18:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151962">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciJ6_xbwjP1IEQL_xa1m2ryKVp_cGoGMriHgNEHoDz-UfV9EYjfSnfmFzkLZ6Uc8cdBddwcb37sxlg6dez_G1t31NaQCiB6n1TXy-kcsJL4-v0sq5cdw974AUQ4UzRSuYkIKxSTsBmh-MDN6rUZHNGsU1rz6G9Ul6oSEeoTArnH6daDWcuVqdlsY8Shf6EE1-okg9UKPTwmAPpt3ggMKwrSX451M2kwHvcXToUWtLstKl5HLb9tN0ZNRGD7bTyEmovgTNJcyqdQmyERxlMqtHPoLqUHG92tNbgWopIlCMBAreC0C2Q0W6mkDVmtUNJdPoLwcEoIWmFPLEAIvdzULeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظاهراً یک هواپیمای مسافربری در فرودگاه ریاض مستقیماً هدف قرار گرفت
از تعداد تلفات اطلاعات دقیقی در دسترس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151962" target="_blank">📅 18:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151961">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCBC_ATpWav1h6vv9iejbmZefJJtGh2fl_4_KXs9GabqwFtjnxA3Kjz3XPIKnyXH22epJjfneNhK66LJq-k5n_J7wv7Rd-tXt39xMXOMAIBPtvtGU5yfGYY4mjdi94uHcI0-7exepAORhgQ95axNem7AAhYw5_9Mv8Jg3_3gL07qRULCKrn0-pUlGji4TGlf4jgfZqSRD_qRSP7kNcdNdXJCJZXtoI-HzzAQjdRLSWHi_4-DYvTu3wLWAimLnr7DUcDu4hbrx3CrFZNY-2S4VulbfuG1JxlyLvACxnEWWn_GET9Oi2YIPiv8cAPUDTLlWm-Yv-lkO6yfCICFahri4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏
تصویری از تخلیه کامل فرودگاه ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151961" target="_blank">📅 17:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151960">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
خبرگزاری فرانسه:  تخلیه مسافران از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، در حال انجام است
🔴
گویا حوثی‌ها حمله کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151960" target="_blank">📅 17:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151959">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUTsrIT_AGa-ZVHxXEMQbQPwc2vOB4dMNS3R-Z-PcPbPrC6VG1SpGLrb39vCDkCXMYwfj8eme6K63xYwsZtXiARw35OKgibXv8HTgLo8PrzAZueqXhjidz6LQdzIAlPjaql04gnf4EpyOPdDY1LQGn-N9S6NziMvjZsevzJ1jzlZBD9MNy7CI2l0eDbSmZh_P8ibtM_xUSZpOvV9Z_L51uvRzBpCSRcGyoJe7haCmTQ_LPbT3qV8RYZGladCbLASqDwnGtHb1UWRtO4kJ5YX_16n3xsR0RUOkhv4SblVe8Kq2KrheonVtV8cjRAjBZgIy2TFoO95kz4X5Ogs5NFb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز لیست ترور مقامات ایران را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151959" target="_blank">📅 17:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151958">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرگزاری فرانسه:
تخلیه مسافران از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، در حال انجام است
🔴
گویا حوثی‌ها حمله کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151958" target="_blank">📅 17:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151957">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
آمریکا اوکراین را به قطع دسترسی اطلاعاتی تهدید کرد
🔴
فرستادگان ترامپ به مقام‌های اوکراینی هشدار دادند که ادامه حملات کی‌یف به پالایشگاه‌های نفت روسیه ممکن است به قطع همکاری اطلاعاتی واشنگتن با اوکراین منجر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151957" target="_blank">📅 17:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151956">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d1f9cc921.mp4?token=CqPKDnvrbKITRohi5mNeSIPKCdHdFpzzcdzxxhrSeiRyB3Pcx7Jwq29hCGXVcbABxfuQuCyKePedvJ5JuaGQgWChYKXRHP5wgjXH6FxXY7YeSDuSoQEBRVxD1RSfakMGUbZ-4MDJNz8MLusoE9KAlRr3AMeq81vamnnj1qX-NXxyEJjkwT2d42RlE9dMX2SzBVZcoy4DLWzXZGBLYcXXgwSOOpDPEZuEJrn_g7Q5vO-1pf_awoUK2Ju-jkwIbRbSEHLrE7qrs-HV3zk5gWCrRdEZTmq3NzcdMc7ImYpyxmYmjGAWRzoqts3TLdS5C6Qsl21OnyEnYFghqEA6UOOmcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d1f9cc921.mp4?token=CqPKDnvrbKITRohi5mNeSIPKCdHdFpzzcdzxxhrSeiRyB3Pcx7Jwq29hCGXVcbABxfuQuCyKePedvJ5JuaGQgWChYKXRHP5wgjXH6FxXY7YeSDuSoQEBRVxD1RSfakMGUbZ-4MDJNz8MLusoE9KAlRr3AMeq81vamnnj1qX-NXxyEJjkwT2d42RlE9dMX2SzBVZcoy4DLWzXZGBLYcXXgwSOOpDPEZuEJrn_g7Q5vO-1pf_awoUK2Ju-jkwIbRbSEHLrE7qrs-HV3zk5gWCrRdEZTmq3NzcdMc7ImYpyxmYmjGAWRzoqts3TLdS5C6Qsl21OnyEnYFghqEA6UOOmcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی که به گزارش‌ها توسط ماهیگیران محلی در نزدیکی میناب در جنوب ایران فیلمبرداری شده است، هلیکوپترهای آمریکایی را در حال پرواز در نزدیکی یک کشتی در حال آتش نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151956" target="_blank">📅 17:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151955">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkR6AGy6ihxPc6xY95gRwaEAXlkTuNKZwihfZC5vhRSABuyl0hukzHf0S0ESqeag6k3Wf8vAiMoqa9X9N2SEeICUwVkQA63TmaJZmYKTw2bvqW9956UjzMisDK_mNcJW_PLe-4wUxNxeywk80DftfijtgeLusfAiovDWkq0wr-QxvTMGnbeymj3PwwJnOTxQD8ojCycz7JuyVZ9oiugjyKsnhfnoUTsqF2wKR8_ksCXIr9L9fHFdZVqe1Na-SPH6bJx1buScYeSoNK2eAsCpnHDsv1VPVgqhBZFemUR2DN1zlMZXOtF3TZ-pBjyJkr4ozDrspzpb3YdnDBtTEFfJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا امیرحسین قیاسی بخاطر پوشش همسرش قراره ممنوع الکار بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151955" target="_blank">📅 17:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151954">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
برخی منابع خبری از شنیده شدن صدای انفجار در شهر ریاض پایتخت عربستان خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151954" target="_blank">📅 16:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151953">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
میرسلیم: مردم باید بنزین را لیتری ۲۵ هزار تومان بخرن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151953" target="_blank">📅 16:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151952">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خبرنگار المانیتور: در گفت‌وگوهای دو هفته گذشته میان اسرائیل و ایالات متحده، آمریکایی‌ها، اسرائیل را برای انجام حمله‌ای علیه ایران تحت فشار قرار دادند، نه یک حمله مشترک بلکه خواستار حمله اسرائیل به تنهایی بودند
🔴
واشنگتن می‌خواست نتانیاهو، نه ترامپ، مسئولیت سیاسی آغاز حمله پیش از انتخابات میان‌دوره‌ای آمریکا را بر عهده بگیرد زیرا برای ترامپ هزینه سیاسی داشت
🔴
فعلاً این ابتکار به حالت تعلیق درآمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151952" target="_blank">📅 16:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151951">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327194aa76.mp4?token=sW2hx2p7m15BBPtMt9mzq3p2Z9C8jqlRRaTfETLDt7JORxJ4qjUiay4KPR_tBelTk_aQcednc6NCbx2AJzgiUSMRIpMgAI0Qcc6-dTvQcRUsZ4DPVEaYQrPJ8fDdFeab1L-KnNSlxvJnjka8lBffSglQ5fW9lLPIywahl7kPSKU_AbgWTZoy1DdlMTHhL6KwHsDVvniQf4jAqC-NfeQR-7kOvhf17dNsqyW7GYWfzetFAmeOcIOBTb1OejrZWsN9e3fOB-WwdvnYKwdPLBwdo8itRpl4T8HGewTI5Fo8YqoiHUQ3EtPHX5dNhfv1aGejy0xq592W1Dc3pzuz3Dvp9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327194aa76.mp4?token=sW2hx2p7m15BBPtMt9mzq3p2Z9C8jqlRRaTfETLDt7JORxJ4qjUiay4KPR_tBelTk_aQcednc6NCbx2AJzgiUSMRIpMgAI0Qcc6-dTvQcRUsZ4DPVEaYQrPJ8fDdFeab1L-KnNSlxvJnjka8lBffSglQ5fW9lLPIywahl7kPSKU_AbgWTZoy1DdlMTHhL6KwHsDVvniQf4jAqC-NfeQR-7kOvhf17dNsqyW7GYWfzetFAmeOcIOBTb1OejrZWsN9e3fOB-WwdvnYKwdPLBwdo8itRpl4T8HGewTI5Fo8YqoiHUQ3EtPHX5dNhfv1aGejy0xq592W1Dc3pzuz3Dvp9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جدال استاد دانشگاه تهران و مجری عرزشی برنامه تاریخی سر خدمات رضا شاه/ نیروی دریایی ایران در دوره پهلوی برای اولین بار به شکل مدرن در خلیج فارس حضور پیدا کرد!
🔴
هنوز از جنگنده‌های آن زمان استفاده می‌شود و حتی از F-5های ما در این جنگ اخیر هم استفاده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/151951" target="_blank">📅 16:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151950">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwN9EQtEKj6ZOHSVgfI1aF_-j8tonitRcb1_kjsWUWElSPkV11Y2lianQCCeB3m8wAu_f4Gl19zTlgAVoBZI77Zb2HvyUBxQPQQH2hc8QLjF4pTFtCmNzYwHS5hmNQ2CGt033CxdfhImQNj4JGFUoeSEM8o9b9guJgxSNBvBzgaXiBlwMcVEIxRiB_auvHVtBVnQnJA-boPLwq1LkPvIICUrEFb9IANpRTJoX7luOva_epS_7nOKXH7ORhFNROyzrnhZ18sAHsdF5qMWH0kb4oPbwdS1srnVOxdz4c6vpGV8Ag0YBUKd_o640iK9P738w_B_oOV-TuygaG6nLENQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱۰ اکتبر روز جهانی سلامتِ روانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151950" target="_blank">📅 16:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151949">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
عراقچی: سناتورهای آمریکایی خواهان خروج از مهلکه‌ شکست‌های فاجعه بار هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151949" target="_blank">📅 16:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151948">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوووووری / معاریو: ترامپ از اسرائیل خواست پیش از انتخابات میان‌دوره‌ای بدون مشارکت آمریکا به ایران حمله کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/151948" target="_blank">📅 16:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151947">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWD-MO4l1k_qOgkeejhCaDI-t5ctSoqf3_Yfz4Y4or4mMrgC3T0anNuZYtiImJnqhApmOA9yFtoH0-KCDFKZoeJRnuPvXYPe8W2lqqCVICw0Dw0jlvZ9SPLGTKm8kMquwWVs0RFYaCkPsXxZDTViuYcsWgWKP2GLpz2MTSFLvEDeAudRMQWMkJDUMhszzZ3XE8asCqGH3pOqnK26Rcm_mDYugya4_NHAayyh9zBgOhe-CBuaE9hkxX6OBQ7P3I7zAltBlJ6ZfO7N5xcw2aZ4275NzpPjtybcAGR3q0ArzkziT-FC50Fv1rph_LXpT_3sIHC6RthOWT5o303ChxLvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ویرال شده از یکی از فروشگاه‌های قم که به جای کلمه «کاندوم» از کلمه «تنظیم خانواده» استفاده کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151947" target="_blank">📅 16:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151946">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جان سینا از دومین ایرانی هم لب گرفت؛  تو فیلم جدید Matchbox (2026)  | مچ‌باکس با بازی جان سینا، یهو گلشیفته وارد میشه و اينجوری لب‌های سینا جان رو می‌خوره  این فیلم اکشن و ماجراجوییه، داستان هم درباره «شان واکر»، مأمور مخفی سازمان سیا با بازی جان سیناست که…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/151946" target="_blank">📅 16:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151945">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65fe6ddfb6.mp4?token=sn8fvZ_RT8BykfZ1aXyUX93Tyhu7Kmj2atauTNLJxWzvKUouh-YlymguZgzp8vjzkbt_6gom--r4VQrqEjIlzaIL6QIl30sp3i7M-VMtORmZhonHe-0NGFOAfNW8-tus6F3Q6mNV7jfu3MApT9dj--SexTxuaaUGF5JOhn96dFgiTLNaRgo286BB0QkWEXRVbywEptX0IQZt4Zg2agFoG9YjYqfKOK5lB5WiXkx61AqcLOs6anfRD0K1o3FhAsVaKzEQ5rgDXAi6M3Dt9gaURuv_rvBv1FKvEBfgcdvtDrGt5M-THSld181pu53bFBIdpGGMEf8JSbTY_8oj1R0n3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65fe6ddfb6.mp4?token=sn8fvZ_RT8BykfZ1aXyUX93Tyhu7Kmj2atauTNLJxWzvKUouh-YlymguZgzp8vjzkbt_6gom--r4VQrqEjIlzaIL6QIl30sp3i7M-VMtORmZhonHe-0NGFOAfNW8-tus6F3Q6mNV7jfu3MApT9dj--SexTxuaaUGF5JOhn96dFgiTLNaRgo286BB0QkWEXRVbywEptX0IQZt4Zg2agFoG9YjYqfKOK5lB5WiXkx61AqcLOs6anfRD0K1o3FhAsVaKzEQ5rgDXAi6M3Dt9gaURuv_rvBv1FKvEBfgcdvtDrGt5M-THSld181pu53bFBIdpGGMEf8JSbTY_8oj1R0n3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد علی اکبر رائفی پور تو این ویدیو یه جورایی از
خاک فروشی
حمایت میکنه و میگه چون ایران خیلی بزرگه آسیب پذیره
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151945" target="_blank">📅 16:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151943">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس جمهور موقت ونزوئلا، دلسی رودریگز، مجوز فعالیت شرکت اینترنتی ماهواره‌ای استارلینک، که توسط شرکت اسپیس‌ایکس متعلق به ایلان ماسک اداره می‌شود، را در این کشور صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/151943" target="_blank">📅 16:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151942">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6EFMr6z_RLAFewe88csJd_sVOialw2mVEHNM7MSCi4FmHWQJwYIwJ8YdgW_myjgX62a7PyKT3LA5oyqnogtwLaEtDO_Ig_bQwXonzHcYkW3u11cV5mmqpM09dHkCm9GLNHrMbY_H1nwNhmULldfINksGvQ6eFUgqSvBICcE3vajL50sz5CBWjk8qu2NdUSA6-L2dYr9aHuh-9IYvJGtj_1nnE6b7-YGpCqjfzjmVm1gJzHe0W1Lt6A5xfP4mdYtBmkXxqEhayuCa18BwBZK6rwTGa3dXzxk4eHRcvkb1AozEPmjERiVEYlpwvfMl5GYxxYkEHEfLt1II6W7zpPQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حشمت الله فلاحت پیشه: آقای پزشکیان! رایزنی با قاتل احیای برجام۱۴۰۱ و تفاهم اسلام آباد ۱۴۰۵، رفتن پی نخود سیاه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151942" target="_blank">📅 15:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151941">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رهبر حوثی ها: از آغاز تاریخ عربستان سعودی تا امروز، شمشیر نقش‌بسته بر پرچم این کشور هیچ‌گاه جز علیه مسلمانان به کار گرفته نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151941" target="_blank">📅 15:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151940">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP3Vf7oXUOc8zMN0CHqX-z3T4AItUqug3qOjssFEZjyGbTRfcXWBxW_YiSHSqsWeWVEn6UO0qShQg1tZHhcehgJSZXuoolxTylf2RguWss5gwPBOAGmR82odyLL6RgQDOr-oUN3ZaSVrjvqj2MisTOY7DapeK18y6H_KMfBwA9ShRl29stlXyUICM3BrqFpTK8-FQMZ0y00gMS_qZ1Uj-R3thlbyI-2dvVNsiJLxaie0GlhTJRkyY4jxpPWyBDQCClYhBUuUxm7qDZvOs3Zgwnf8yUU8oeWCqKhcW7y_LLtNZFuB4pAAAhMVI71pBk4TooWspNn1pitoplfrGb9uHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : من 8 جنگ را خاتمه دادم، و به پایان رساندن یا حل کردن 2 جنگ دیگر نیز در شرف تحقق است. تمام گروگان‌های اسرائیلی را آزاد کردم، از جمله 28 نفر آخر، هم کسانی که زنده بودند و هم کسانی که فوت کرده بودند. صدها گروگان را از کشورهای مختلف جهان آزاد کرده و به خانه بازگرداندم.
🔴
در ونزوئلا پیروزمندانه جنگیدم و دیکتاتور خشن آن کشور را دستگیر کردم. همچنین، مانع از دستیابی جمهوری اسلامی ایران، بزرگترین حامی تروریسم، به سلاح هسته‌ای شدم — و موارد بسیار دیگری وجود دارد!
🔴
با وجود تمام این دستاوردها، من یا ایالات متحده آمریکا، جایزه صلح نوبل را دریافت نکردیم. چه شگفت‌انگیز!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151940" target="_blank">📅 15:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151938">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGYlaGJhNYstRU6l9ibnDI5bOrkuIMguv1H1Ku8pKzV65981-2RkmGyNtwiFDDgT5r6gJz-3ULjWGdL-VbTHsyLJKLwX_FOIKqmYNMCc-dpJyrvo3vxQLFVwxWBdZyD9K0XCgwg8vKqCE8bHAPsb82vmTJ_bAmkgwG2NquQRTk8HDMrtscwfFjIrXQ4yZSVd94uz0JD0eJgsGCnasq0ZnTvZS8Q1TezYT_uZ--FPdNZsCN_0S1l1D6c9I_swwAl6oLGkQAl5eWuxYncZ-qLSe1UiVej092XqiPhSMI86j6ZPEDAXp3Lhn-NGJOwM7RAtGHlOq-4B7Q_UQqAzSCN3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، چندین کشور آفریقایی در حال حاضر در مذاکره با اوکراین هستند تا شهروندان خود را که پیش از این در کنار روسیه می‌جنگیدند، به کشورشان بازگردانند
🔴
کنیا در حال حاضر تلاش می‌کند تا آزادی پنج تن از شهروندان خود را به دست آورد، در حالی که دولت بوتسوانا در تلاش است تا یکی از شهروندان خود را آزاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151938" target="_blank">📅 15:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151937">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ram VPN_v3.1.apk</div>
  <div class="tg-doc-extra">55.1 MB</div>
</div>
<a href="https://t.me/alonews/151937" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی فیلتر شکن پرسرعت
Ram  VPN v-3.1
بدون تبلیغ و پرسرعت
🔥
رایگان و برای رفع فیلتر شبکه اجتمایی
⚠️
مناسب زمانی که اینترنت ملیه
❤️
🎮
دانلود امن از گوگل پلی
👇
https://play.google.com/store/apps/details?id=com.ramvpn</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/151937" target="_blank">📅 15:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151936">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nieyBgNG5SSA3w9b5wUkuibBu0QW6A1Re2mh-LHFTkmmjaIOFxQoR4bPoqCE6titSVVOAInWQxZCkrIwQ7fgbK0OlEe5ZOKnMaFnLDO-oAV3up1CZQ7lCjDowFIOIdM5bDlqttwPQKMfSdND-pdaSjfSbd8O3kONwm7zOTObaFIGVIZlRH2OqpkItXHgNEr6k2aqmmSdMeJprUrS0keBhEY3-IkoLqK7aFUsj2_nTFCSRA85Du4whUW86GCzkWMbhv5xmXtWiOSIg7G4C3_uNVREHHM7yv7nw-SqXKATHEdOtvcWUGYkQ17EDDrBC03yH_ua5nyieR4xNxyYxqqVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادوسلاو سیکورسکی"، وزیر امور خارجه لهستان: سفارت ما از کمبود سوخت حتی در مسکو خبر می‌دهد؛ شهری که همواره در اولویت تامین سوخت قرار دارد.
🔴
علاوه بر این، منابع موثق گزارش می‌دهند که اوکراین تاکنون به حدود ۵۰ درصد از ظرفیت پالایشی روسیه آسیب رسانده است. بنابراین، مازاد سوخت( روسیه) برای صادرات( به آمریکا) قرار است از کجا تامین شود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151936" target="_blank">📅 15:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151935">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341194d3c9.mp4?token=oKBv1g7GhMxuoaVCL82aEXxqX14XBdQh7b22B3Yn52SSl_f5ym3IUqhDd9e3tFv24X6aDS-KyFX0k_L6hQhBRd4-magpBQlT6VvCVnAW5jfZjAN8r6jPu-W7jit461oum2NEKIkyEnF-PamC-pLFL8SkZXAkZMpA3nttvrdpKtqQw2LuPz17ErSGVhZ_aEbwDENDPmJ-Qcr4jiD5ZKdIptvwmHU14jRKRHzYwJAJjdb4epuYYRYJKen1u0rS3K8BXOhCTV1jGsSGHyMUxXLPA7FBD_1J8s1lDa-YlSnd6iipGxlSJNkPz8SUOzG_yoGoBibmj53CQ4M9ojtsEPnyEwJZr_lnh20_8KaI_WIZwsMi4imP0f0P-BMx9XyLvVgUBaV4ADZQyDGLD4sL2KEDK06Sfx8nw-X_Uly_h1ZvS6eqHHJldbm7PCqOOxYMVmWk7EpyCnySuPSorD-n6D7EzXfNnIG00RW-qkwuLXKjyUaS-1u4Y2baK4XzoUOAV1EHcOeNf2yPxy0iSi1WEgbfspKXD_VDgWPib5yYS0t9_8SHRZiCjUrp3q3f0ROxoilgo1XPWGan3tLdtmRSpsqeBOivecLcO-VeTGQQR5LFpSLGjPzk5-RgN6r6Y4R97llwaiRrlMi5_vZeRT68u1yn_ojsqbJGxdtJ3annRuV9z8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341194d3c9.mp4?token=oKBv1g7GhMxuoaVCL82aEXxqX14XBdQh7b22B3Yn52SSl_f5ym3IUqhDd9e3tFv24X6aDS-KyFX0k_L6hQhBRd4-magpBQlT6VvCVnAW5jfZjAN8r6jPu-W7jit461oum2NEKIkyEnF-PamC-pLFL8SkZXAkZMpA3nttvrdpKtqQw2LuPz17ErSGVhZ_aEbwDENDPmJ-Qcr4jiD5ZKdIptvwmHU14jRKRHzYwJAJjdb4epuYYRYJKen1u0rS3K8BXOhCTV1jGsSGHyMUxXLPA7FBD_1J8s1lDa-YlSnd6iipGxlSJNkPz8SUOzG_yoGoBibmj53CQ4M9ojtsEPnyEwJZr_lnh20_8KaI_WIZwsMi4imP0f0P-BMx9XyLvVgUBaV4ADZQyDGLD4sL2KEDK06Sfx8nw-X_Uly_h1ZvS6eqHHJldbm7PCqOOxYMVmWk7EpyCnySuPSorD-n6D7EzXfNnIG00RW-qkwuLXKjyUaS-1u4Y2baK4XzoUOAV1EHcOeNf2yPxy0iSi1WEgbfspKXD_VDgWPib5yYS0t9_8SHRZiCjUrp3q3f0ROxoilgo1XPWGan3tLdtmRSpsqeBOivecLcO-VeTGQQR5LFpSLGjPzk5-RgN6r6Y4R97llwaiRrlMi5_vZeRT68u1yn_ojsqbJGxdtJ3annRuV9z8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویر، وزیر امنیت ملی اسرائیل:
ما هنوز کارمان را در غزه به پایان نرساندیم.
🔴
و همچنین، کارمان را در لبنان نیز به پایان نرساندیم
🔴
این وضعیت چگونه باید به پایان برسد؟ به نظر من، تشویق به مهاجرت و اسکان در سراسر نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151935" target="_blank">📅 15:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151934">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پزشکیان: جایگاه فعلی زیبندۀ ما نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151934" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151933">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فرمانده نیروی زمینی ارتش: بیش از 50 یگان رزمی و پشتیبانی ارتش در مرز های غربی و جنوبی کشور مستقر شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/151933" target="_blank">📅 15:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151932">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وقوع انفجار و قطعی گسترده برق در کی‌یف پس از حملات جدید روسیه
🔴
رسانه‌های اوکراینی از وقوع انفجارهای شدید در کی‌یف، پایتخت اوکراین، در پی حملات موشکی و هوایی جدید روسیه خبر دادند
🔴
وزارت انرژی اوکراین اعلام کرد، این حملات زیرساخت‌های انرژی را هدف قرار داده و منجر به قطعی گسترده برق در بخش‌های وسیعی از کی‌یف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151932" target="_blank">📅 14:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151931">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89eb24a75c.mp4?token=if34TNsm75u681pHVflX-pz7QAXaEBgEKkv9u4E1yMq_-1vtBETbSx60BlwbtgdjtZ1QAUdJiWlNQbpyQPUrZWf7pT0wgOAKyKRvLsFAEwBzUoRQ-SrMMIGpJyNkBOAGeW5mf34sGajtflQkUOyOVbY-RL-5O5zolC5ha0mn4Bm880OiCVjsg6DT2qV6LLbXja-OMASG8Bm9xGhjxstBDgSmzsbL8ctJ-8L9FzCsTl_IC94rmlbZpYw8tdXOcACytIcp6xJM5bIUkupje8xwKdj7jI346NNaFezPK1eZ8HX9JdpCOJMYDWPAsyVFdXXi5tee5M0uDnWxB-cPoeWcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89eb24a75c.mp4?token=if34TNsm75u681pHVflX-pz7QAXaEBgEKkv9u4E1yMq_-1vtBETbSx60BlwbtgdjtZ1QAUdJiWlNQbpyQPUrZWf7pT0wgOAKyKRvLsFAEwBzUoRQ-SrMMIGpJyNkBOAGeW5mf34sGajtflQkUOyOVbY-RL-5O5zolC5ha0mn4Bm880OiCVjsg6DT2qV6LLbXja-OMASG8Bm9xGhjxstBDgSmzsbL8ctJ-8L9FzCsTl_IC94rmlbZpYw8tdXOcACytIcp6xJM5bIUkupje8xwKdj7jI346NNaFezPK1eZ8HX9JdpCOJMYDWPAsyVFdXXi5tee5M0uDnWxB-cPoeWcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه هولناک فرو ریختن یک آپارتمان و زمین خوردن مردم در پی زلزله ۷.۶ ریشتری پاناما
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151931" target="_blank">📅 14:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151930">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlQcxnGiw5cebR_u529KTMKNGo2pLBHa5h0rjQVQuKxgVrQU-tJ_nh8yUoQxd_GalZ2WPKI6FJYIcB-d0YIovgfKA7QN_rFex9VulRBge5zAlu5iux44TWopN8mVBXV5otA2HfMNfNpukB4ibZoOxgqRvMENuQWjJTNuk4c8NHPDgV1VzoFYF5npplNaCP6tg6ZnJ0DBStfLGGrqFSznoKNzgop4vDAITH-UnStEpiqYAs2YtHhMdlKIxV-lwQ-yViq_4Fg0SDR80DMElzmhFdwrorpXDvBRMyN_h8yXOEiBLjDGu3F6P8TGa_uVqug6AEnfVwEGPYzyPHRizuINlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی، خبرنگار: بورس ایران قبل از تاسیس کشور امارات شروع به کار کرد، اما امروز ارزش کل بازار سرمایه ایران حتی به ارزش یک شرکت نفتی عربستان، یعنی آرامکو، نزدیک نیست
🔴
چرا کشوری با این حجم از نفت، گاز، معادن و سرمایه انسانی، نتونسته جایگاهی متناسب با ظرفیت‌هایش تو بازار سرمایه جهان پیدا کنه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/151930" target="_blank">📅 14:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151929">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔝
💯
دنبال کانفیگ ارزون و مورد اعتمادی؟
🖥
کلیک کن</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151929" target="_blank">📅 14:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151928">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شمارش معکوس دو انتخابات مهم؛ اسرائیل ۱۸ روز، آمریکا ۲۵ روز
🔴
با احتساب امروز، ۱۸ روز تا انتخابات پارلمانی اسرائیل باقی مانده؛ انتخابات کنست بیست‌وششم قرار است ۲۷ اکتبر برگزار شود.
🔴
در آمریکا نیز ۲۵ روز تا انتخابات میان‌دوره‌ای ۳ نوامبر باقی مانده؛ انتخاباتی که تمامی ۴۳۵ کرسی مجلس نمایندگان و حدود یک‌سوم کرسی‌های سنا را دربر می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151928" target="_blank">📅 14:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151927">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs6b69IsJXO_gqmqdq0-nReJggbfo0hAeTs90Q__WT6kxHfaVMI4l6P5Jcktm8EhU1EW6uHJnVphz_7IpXRtMze98498pcgbephbIGij-t7hux9HM8d-62j79i-1KzmjxZvCYItBYCbshvQjdIL-xdR_XUqboYQ5IShmoEBfxOQt7kFTbhhQxiAt2yYeztLKVJvWVndQL8IZXkI3V_oDhDY2z7aXvXjNk-2bQZPl2g8tBHw3iavLsJ3kqkrOJjNVt-H43HMqxc9MzUPZz9gWe27d7OHHG2GPuKKiS2sDB86wnyKmmtlt9KV5OLAZ7SyL8VjvVEA0MWyZGv5ZDkRlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم:
چرا باید بنزین ارزون بدیم‌ تا مردم تفریح کنن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151927" target="_blank">📅 14:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151926">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWcPqH5zAWtAHkQ7_czciRUIwMLhHBFlR-DX6gj3OK54PAJ-wENFegCj7_12llJp9LB-uvTX099bBqI02ISxYqy1HOu2QBUDN1SMexRMB2szsYRyPE91SAlGEI6hwzWJXEeTWMpLhjyugoTMYz211muVA4peaXLgmhcAXH_TtjrlSSDE_Tci0pCpJPnTX0my9KtZg18IN07NXRWtdMZaON8JFYTF49DVC0o6qzDwyz935sb427Bi1Gp7zeEEkJ7JTaJ0mDOF5GtisEl1CH3NjMb-9K6uY5vbJ8Akb4_unBtwpbs-4RWr99v5lVhWSteC_PI63jKV4lIZi3pvf4GH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی دولت: بمب اتم در اسرائیل است، اما بازرس‌ها در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151926" target="_blank">📅 14:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151925">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
مقام ارشد روسی: پوتین به ترامپ گفت که پیشنهاد روسیه درباره اورانیوم ایران همچنان روی میز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151925" target="_blank">📅 14:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151924">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8aa407e2.mp4?token=mxd68eEBvCb1rerKdAjVIVF0Eh_MZhOQUIHXDc3fhQglnEEfHGLBPRmTTQki6s9PxZIMmQUx-jTsar8hWw3OKeCa6UDEDGB8Jr0gaQis4b6YCDN42og1qoIi8Byx027lBH_MMunQNVBYi8NcJv7SAKJ1_LwG7RzS7WwTHooNw-SsagWJnIpRYjWa5iTS01x6MVBb5Jpcxl7frboBBpb7PEFlcS-XMeX5HywCHtOsbZBDaEj0dh9DosS3iHTGC9u7qu1KQGx62CGcArAP5w6FR8m4RippXZCEi72EGuj68ST-j6jWmrsq-DWKgFXZKDMXxtbWK-yHPY7MpWdBn6bkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8aa407e2.mp4?token=mxd68eEBvCb1rerKdAjVIVF0Eh_MZhOQUIHXDc3fhQglnEEfHGLBPRmTTQki6s9PxZIMmQUx-jTsar8hWw3OKeCa6UDEDGB8Jr0gaQis4b6YCDN42og1qoIi8Byx027lBH_MMunQNVBYi8NcJv7SAKJ1_LwG7RzS7WwTHooNw-SsagWJnIpRYjWa5iTS01x6MVBb5Jpcxl7frboBBpb7PEFlcS-XMeX5HywCHtOsbZBDaEj0dh9DosS3iHTGC9u7qu1KQGx62CGcArAP5w6FR8m4RippXZCEi72EGuj68ST-j6jWmrsq-DWKgFXZKDMXxtbWK-yHPY7MpWdBn6bkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان این چالش لعنتی رو اعلام میکنم
😂
@AloSport</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151924" target="_blank">📅 14:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151923">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: شهروندان ایالات متحده در منطقه غرب آسیا، با توجه به وضعیت امنیتی پیچیده، نهایت احتیاط را در پیش بگیرند
🔴
درگیری‌ها در منطقه ممکن است به سرعت تشدید شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151923" target="_blank">📅 14:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151921">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
قدیری ابیانه: زندگی مردم ایران از اروپا بهتر است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151921" target="_blank">📅 13:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151920">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ae8c9e28.mp4?token=tv8ewrIhlVVu-nZeRJ5OM-zjGTx0-rvpkehVKkyUVLjSFmHpt3ivNSCCegLebXsuF5cnR9TC3mDda0Io4HmmPLeA7YYhUzDi387b_pvW47yaBh7i9ZGC_sduvkog9-f8zqYgBFjDkR_AR994Lm_mW3tcPLQn7xFmzl-d-TnOiATiuzJMmR6SUafVI21FLVDiUmmtAjHnxmn38u4bj0yVOLcDOhuxPZ7b10AK13ma8fjp1jKFSd_S0zucPo01Kcd1Y4-1Cgz9h_wL-_cQkp1QeMFdCO6k4eT_PVVgQ07MQxq-omOxtpxH5fJvxlYr83ZQghq0_hYfhAUA_sVbkaNmlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ae8c9e28.mp4?token=tv8ewrIhlVVu-nZeRJ5OM-zjGTx0-rvpkehVKkyUVLjSFmHpt3ivNSCCegLebXsuF5cnR9TC3mDda0Io4HmmPLeA7YYhUzDi387b_pvW47yaBh7i9ZGC_sduvkog9-f8zqYgBFjDkR_AR994Lm_mW3tcPLQn7xFmzl-d-TnOiATiuzJMmR6SUafVI21FLVDiUmmtAjHnxmn38u4bj0yVOLcDOhuxPZ7b10AK13ma8fjp1jKFSd_S0zucPo01Kcd1Y4-1Cgz9h_wL-_cQkp1QeMFdCO6k4eT_PVVgQ07MQxq-omOxtpxH5fJvxlYr83ZQghq0_hYfhAUA_sVbkaNmlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۵۰ میلیون تومان طلا در سال ۱۳۹۵ در مقابل ۵۰ میلیون تومان طلا در سال ۱۴۰۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151920" target="_blank">📅 13:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151919">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUWQ96FtyL-gO1FdxQBIZT__Q-8LlesbRIcixw9W3qx4oPAKZPxDgUu0MW0eA575eLUgebW5VvF9S-fLHeqbb1aZVVyb3Y13QokDybSj2CYwLv4NT5w5nitBlpSVzDkf97IPOrXxmtjayvRUT-0c8gCiKaMmsTRuIkil3PYkJ_FQkaxmxI-eSUzv9Ys5kqW2G9XepCtNiD77t3grw_OtsQbgHZ4HoQ6KhiZuQVHcOPr8GF8kCF0800plc4125JdjxXdZzTn2OXYaAHDLTBkjadvaMsDY-Eny1Oy7JQAaNPDCRK_OiNsVfJ3JDpL0grg8_9JzYGxY2VizMJmUny1KnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجداد آمریکایی‌ها ۶۰میلیون گاومیش رو کشتن که غذای سرخپوست‌ها تموم بشه بعد وزیرشون به هخامنشیان گفته غارتگر متجاوز
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151919" target="_blank">📅 13:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151918">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سفیر کره جنوبی در اوکراین در اعتراض به افشای اطلاعات انتقال اسرای کره شمالی به سئول از سوی رئیس‌جمهور اوکراین، به کشورش بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151918" target="_blank">📅 13:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151917">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d6fcd9a1.mp4?token=Gz361hlIDqqfP6I4SSbQg0qD6FzXvEWjCj1mSZyQa9gqRegoMAqU6UweaMPAYQhL3ialR-aWB-9FDLgCE93WETj3VBcEpHKve0dj74mhiojFTQeK-Ec1c7nMRm8Gms8xZZB2pO98d_cuP64eIIofzHzbsBFHxsfmTxnS_oHVEZKwDXhlevVodRom9bYBNV50BPkFHNfRDJzwAmPSQ3kBbD2u-kaCoMhWZupML4i9JwcY5PjGYyr4hQNqXFgg_ybD_wuivV5uCD6m4vNWm7RGKQCEriUow1VAYJUo9lzIFuLGBFiXtB68yLEt-i3qYQNBpfktyYrUiVG57mIS-kVe3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d6fcd9a1.mp4?token=Gz361hlIDqqfP6I4SSbQg0qD6FzXvEWjCj1mSZyQa9gqRegoMAqU6UweaMPAYQhL3ialR-aWB-9FDLgCE93WETj3VBcEpHKve0dj74mhiojFTQeK-Ec1c7nMRm8Gms8xZZB2pO98d_cuP64eIIofzHzbsBFHxsfmTxnS_oHVEZKwDXhlevVodRom9bYBNV50BPkFHNfRDJzwAmPSQ3kBbD2u-kaCoMhWZupML4i9JwcY5PjGYyr4hQNqXFgg_ybD_wuivV5uCD6m4vNWm7RGKQCEriUow1VAYJUo9lzIFuLGBFiXtB68yLEt-i3qYQNBpfktyYrUiVG57mIS-kVe3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ستون‌های دود که از میدان نفتی الغور برخاسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151917" target="_blank">📅 13:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151916">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0ac4560f.mp4?token=jsUXgd28d2AAweSlOzEJpicGhdKn7hbLdxdoI1JDsrflq1hM_cqLQl8qlYnkU6Jv68l69aMBrB5y2-LFwvJtrZObs8zIYKiXsN8StK8EWMAAxOUmWBQ2u3Y28xwp-2gtbUxrVpx3MzDCEed52s-Tom0TGQFGQQXM-Ow3x5tID1yOAeSjntH3--tAX-Qw21ErhVx7lRztQcf905tkfqqXa2dA2aTmxsHl-qhTXTrfrGWNuv7GG7RGGAunropoPJU_zt-Dg0CRpY-Dv0NCgjRe3PxaBAEThiknfIaqL6EKH5sUf7sD3WV_2t1saXrqvvIbqt3hWwmD5xzYizTKjk7v_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0ac4560f.mp4?token=jsUXgd28d2AAweSlOzEJpicGhdKn7hbLdxdoI1JDsrflq1hM_cqLQl8qlYnkU6Jv68l69aMBrB5y2-LFwvJtrZObs8zIYKiXsN8StK8EWMAAxOUmWBQ2u3Y28xwp-2gtbUxrVpx3MzDCEed52s-Tom0TGQFGQQXM-Ow3x5tID1yOAeSjntH3--tAX-Qw21ErhVx7lRztQcf905tkfqqXa2dA2aTmxsHl-qhTXTrfrGWNuv7GG7RGGAunropoPJU_zt-Dg0CRpY-Dv0NCgjRe3PxaBAEThiknfIaqL6EKH5sUf7sD3WV_2t1saXrqvvIbqt3hWwmD5xzYizTKjk7v_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل خطرناک در شهر انگوت گرمی
‏
🔴
اردبیل/صبح امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151916" target="_blank">📅 13:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151915">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
عوستاد رائفی‌پور: روسیه باید پالایشگاه‌های آمریکا را هدف بگیرد تا حملات اوکراین متوقف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151915" target="_blank">📅 13:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151914">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
هزینه رجیستری خانواده آیفون۱۸ مشخص شد: آیفون ۱۸ پرو مکس ۱۹۷ میلیون تومان، آیفون ۱۸ پرو ۱۵۸ میلیون تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/151914" target="_blank">📅 12:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151913">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
العربیه به نقل از کرملین: پوتین با ایران هماهنگی کرد و دیدگاه تهران درباره راه‌حل احتمالی را به ترامپ منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/151913" target="_blank">📅 12:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151912">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: شروط هفت‌گانه ایران در مذاکرات با آمریکا، از سوی مراجع عالی نظام ابلاغ شده و قاطع است
🔴
پاسخ طرف مقابل به پیشنهاد هفت روزه این است که ایران ابتدا تنگه هرمز را باز کند و پس از آن، شروط هفت‌گانه به تدریج محقق شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/151912" target="_blank">📅 12:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151911">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رئیس سازمان امور دانشجویان: دانشگاه‌ها در هیچ شرایطی تعطیل نمی‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/151911" target="_blank">📅 12:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151910">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d2a16f11.mp4?token=uLGpLByNhPz6rDWY5Q3fHnoclrIaKNRoEYReItVxcyZ1tMsrInUXTOnabickXOhANVmgQ3yTvHSV5FknlJC3082sV5jJG6TTw9MJ3jEhGzOQgzZkwixr-w2p0kHm_JVEUBmFhN18M0XPbrWrTLlde3KMkltmCV7HCC0KeWpo7a3-uFwIaeSmQ_lC1YbsATwLCIt9YZOx_FTLRDfWy81PFWl4wuNORrUTEQt89-FJ2JcM_backnBS2c1OpisUD3jUugIHhbIpehyaiVyB3dQrG6SN0WoJ3aZ45VEU5UcvsZ3CjkDRy43Nl_jCvZ2E2og52kDAFRSW2w9NpgYiiTnRJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d2a16f11.mp4?token=uLGpLByNhPz6rDWY5Q3fHnoclrIaKNRoEYReItVxcyZ1tMsrInUXTOnabickXOhANVmgQ3yTvHSV5FknlJC3082sV5jJG6TTw9MJ3jEhGzOQgzZkwixr-w2p0kHm_JVEUBmFhN18M0XPbrWrTLlde3KMkltmCV7HCC0KeWpo7a3-uFwIaeSmQ_lC1YbsATwLCIt9YZOx_FTLRDfWy81PFWl4wuNORrUTEQt89-FJ2JcM_backnBS2c1OpisUD3jUugIHhbIpehyaiVyB3dQrG6SN0WoJ3aZ45VEU5UcvsZ3CjkDRy43Nl_jCvZ2E2og52kDAFRSW2w9NpgYiiTnRJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از دود برخاسته از میدان نفتی الغوار، پس از حمله موشکی یمن به کارخانه گاز شداقم در عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/151910" target="_blank">📅 12:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151909">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترکیه دسترسی کودکان به شبکه‌های اجتماعی را ممنوع کرد
‏
🔴
ارائه خدمات شبکه‌های اجتماعی به افراد زیر ۱۵ سال در ترکیه به‌طور کامل ممنوع شد.
‏
🔴
پلتفرم‌ها موظف شدند نسخه‌های اختصاصی با پروتکل‌های امنیتی و حریم خصوصی تقویت‌شده برای کاربران ۱۵ تا ۱۸ سال ایجاد کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/151909" target="_blank">📅 12:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151908">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پزشکیان: قابل قبول نیست که ما به عنوان انسان، ایرانی و مسلمان از بقیه عقب‌تر و ناکارآمدتر باشیم؛ باید ببینیم دیگران چه کرده‌اند که در برخی حوزه‌ها از ما جلوتر هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/151908" target="_blank">📅 12:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151907">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پایگاه آکسیوس به نقل از یک مقام آمریکایی : استیو ویتکاف و جرد کوشنر در حال بررسی امکان سفر به مسکو و کی‌یف در هفته آینده برای گفت‌وگو درباره پیشنهادات صلح هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/151907" target="_blank">📅 11:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151906">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آمریکا: شهروندان ما «همین حالا» ایران را ترک کنند
‏
🔴
وزارت خارجه آمریکا با اشاره به شرایط پیچیده امنیتی در خاورمیانه، نسبت به احتمال لغو پروازها و بسته شدن حریم هوایی هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/151906" target="_blank">📅 11:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151905">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sochKFYwO-dFQMjtZ1Cd3u8lzmPX4na-pbqTVfMFp-IA5WCDtFgtUyJkZezSJX5taodeWhDIV2IpAZTxWjU9noKuUyRPMCz0CzLo9y8d6YS-VZfK4yAGV7BM7OU1nvg8bFIlQBeiI5a1lhTnJqrUDczck9R5JYY7N0Ys-mrGE-cD_H7SLQQz494nsvBy3koHi6lSh0H1D6WzejQUa4P4M1bZ2_4ZybcZWdFpS3jVaeRt-n6XnFunI0Ysy-FO1FOA8fL18AnaTkCDbT4Q22Q2a1PeIxFa9TtodUFlQnKFRCSQcRxDwVqhjafgi8_8aI1P-Wb5K6sAYyWXFBqEy51jvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع لبنانی اعلام کردند توپخانه اسرائیل، شهرک المنصوری، وادی زبقین و حومه شهرک زوطر شرقی در مسیر میفدون را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151905" target="_blank">📅 11:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151904">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM0WxbDwQYNWihXXsAo-MNaO3az1qSe867FQo0UdAY9eg7lsTA2UGuPz2vHhKeI7Djz4r78wTGLw0CfrX7Sv4CzBNwCqcysMUNQMPF8q0zsdPLi7ftUAYyzJLQNXmSxzXNKTNnXXDDbC_S7APW0Qyho3LPTu30q17kw0SC0vyibYMy6FsfuxHVeXK2g8ERLFb1h0IMjoX5nTbDe-cSzxeJoH7C9DSmV6QOj_6h6E7SOxMgvGRLuSi6I_Dha0H5sGV_73dUIzp_Vz_MRutvWURG6j7ImI8wxWLJwwMTb5LMRrKVSh8TwtN78DnLyFCdNOZN1qY9KDb7F5zEeC21W7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم: بازنشستگی در اسلام‌ مفهومی نداره و منم کنار نمیکشم و به کسی ربطی نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151904" target="_blank">📅 11:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151903">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
آدام اسمیت، نماینده کنگره آمریکا: توافقی مشابه برجام، تنها راه منطقی پایان جنگ ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151903" target="_blank">📅 11:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151902">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
حداد عادل : هی میگن رضا شاه روحت شاد رضا شاه روحت شاد بخاطر اینکه راه آهن و راه ساخته شد و این مدرن سازی های عامدانه انجام شد، اما در ازاش نمیدونن که آزادی از مردم گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/151902" target="_blank">📅 11:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151901">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
امروز مردی حدود ۲۵ تا ۳۰ ساله با ورود اجباری به یکی از واحدهای تجاری در طبقه چهارم پاساژ سعدی تهران، با سلاح کمری به منشی شرکت شلیک کرده و پس از آن اقدام به خودکشی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/151901" target="_blank">📅 11:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151900">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
مشاور سنتکام گفته وقتی میتونیم محاصره اقتصادی و هوایی کنیم چرا نیروی زمینی پیاده کنیم که نیروها بمیرن و ترامپ انتخابات رو ببازه! محاله پیاده کنیم.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151900" target="_blank">📅 11:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151899">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پنتاگون تعداد تلفات نظامی آمریکا در جنگ علیه ایران را به روز کرد: ۲ کشته و ۴ مصدوم به آمار قبلی اضافه شدند
🔴
شمار نظامیان آمریکایی کشته‌ شده به ۲۱ نفر افزایش یافت و تعداد مجروحان نیز به ۸۶۵ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151899" target="_blank">📅 11:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151898">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
👈
پزشکیان: قابل‌قبول نیست از دیگران عقب بمانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151898" target="_blank">📅 11:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151897">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت دفاع ایتالیا اعلام کرد که عربستان سعودی به منظور تقویت امنیت و دفاع از قلمرو خود، رسماً از این کشور درخواست کمک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151897" target="_blank">📅 11:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151896">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c52c1a8d.mp4?token=v1yiuj7lXwFmSuayMl_9OTm4hbN0Or9rzRJoAmjwKuwSOTPjU2L0904ZrCKbUkb9WrxUEjlNEwDp1hPh0xtBiC3Cgssdt-1ixbk_sR2XgY6Sugin5G6zv0jilErX3g5PRqhFNaD1qYbjZKu_9Zqe7Bs5npluYtvQCxcIrNoZNEOdm6nKIP034GbuhEWfz_iDE8IeVO8j5jfrpKMzpDNluOAfI9CC6q3KHL63659kYnNARDc072dWQx9CgHlGUEhycYUpqE5lKi_nns7qFibZKxhDVZDn3YSVvtCzUR5BcHVa28c7mTZruXAIO7dmqcQvZX9zCjZEwjQDHysFNwI-pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c52c1a8d.mp4?token=v1yiuj7lXwFmSuayMl_9OTm4hbN0Or9rzRJoAmjwKuwSOTPjU2L0904ZrCKbUkb9WrxUEjlNEwDp1hPh0xtBiC3Cgssdt-1ixbk_sR2XgY6Sugin5G6zv0jilErX3g5PRqhFNaD1qYbjZKu_9Zqe7Bs5npluYtvQCxcIrNoZNEOdm6nKIP034GbuhEWfz_iDE8IeVO8j5jfrpKMzpDNluOAfI9CC6q3KHL63659kYnNARDc072dWQx9CgHlGUEhycYUpqE5lKi_nns7qFibZKxhDVZDn3YSVvtCzUR5BcHVa28c7mTZruXAIO7dmqcQvZX9zCjZEwjQDHysFNwI-pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که ستون‌های دود از چندین نقطه نزدیک به کارخانه گاز "شدقم" در عربستان سعودی به آسمان برخاسته است، که این موضوع به شدت به حمله انجام شده توسط نیروهای یمنی در دیروز اشاره دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151896" target="_blank">📅 10:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151895">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6VigUa4LRuDyNhB4Qn-RUgztLRj8EYJV5lh_JHfaHJRyWjm3OQa0kGd-xt0hKN3iIK4Ouu9lyWwgwMVaEl4wv3aTn-STPJA7-AHrmty7jTgsWOc2bVcy_p0odV-Ox3aEGpI5T5DmfB8oTpK0Z7wzn-WMLPRcPxFR3KUaJBeCD3JZfnne6p6ZEbBE6nDot__awZLYntYlM0GljjiI3mHvcB8jyNWtmTP7-gJdHKSmjGY4nDb-dTZoWE-VUVam8yvBCwtZGZFPbpDvjt8qPGl4UxWuPbBKJI5WBVgAs_UaPvtQzmUDrAw-gs4J8iFvXPHDahtomrHW0qTgn05gcx1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزان‌ترین خودرو داخلی یک میلیارد و ۶۶۰ میلیون تومان
!!
🔴
فروشندگان برای کوییک دنده‌ای ساده رقمی نزدیک به یک میلیارد و ۶۶۰ میلیون تومان پیشنهاد می‌دهند.
🔴
ساینا دنده‌ای نیز در بازار به حدود یک میلیارد و ۷۰۰ میلیون تومان رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151895" target="_blank">📅 10:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151894">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات الونیوز</strong></div>
<div class="tg-text">👈
پلن ویژه افزایش ممبر برای کانالهای تحلیلی و اقتصادی داریم جهت اطلاع از شرایط به دایرکت پیام دهید
دایرکت</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151894" target="_blank">📅 10:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151893">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avrI9paWh9GPe1UcK-vmosnQFQfsweMl_UDs7AxkdmD7z-OIMhRN0H95Y3dt61bGUKdokmTG3k33luIZaQMAv6gb6r2DxHUTm7PnE3Xyo7B_M3chtXbVd1jjjhukjoTMfxi2bcJgz9Y4e3uEqwahtGron-PFItxgKc53w4fzWdQ4t7jPm82GJeQa5g67EqJGjk2nw5DjuAHjo68vbN9N3Rk2vA_l5ADNoKqyikAqjuwpLSRenfrfIFan1ZTlKUt4cZ_vBKD0mnM5SBcFWgygVaAZr-EYS56DGySs6Nmpa94QhOyGGFRyv3oiO1KvYUmOoVf1IWW0-y_8b4hRxJE2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور عارف معاون پزشکیان: ترامپ قبل انتخابات کنگره حمله نمی‌کند، اما باید مراقب آذرماه بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151893" target="_blank">📅 10:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151891">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سازمان مدیریت بحران: ۲۵ الی ۲۷ استان ما درگیر پدیده ال‌نینو خواهند شد ما بدترین وضعیت را در نظر گرفته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/151891" target="_blank">📅 10:45 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
