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
<img src="https://cdn4.telesco.pe/file/RB7jsSRsErKHaUH4E-YOuKK3iyxmnVoDJal7tEXsd31ndInj26JdZsN5DWeodzvKBtGxD6DhtlgS8hrJvD73NdOjjOLUKrbpTM_7XNfqmF5pTDPAjb4w_K1-hI9hVkJULmpqMaG-2IpysWUr_ayMm75Z9iXmgD5aGb8EYGGxzFCXqAlTDQoMP2jaY-iWdqYPqmQ85RhXJ-CwcpKVuk9pxOaWTVHApNaZuRqRlpGuS-QO0fYJOOTyuANU7zNNY0wOi4q3yznZSP2z-0UaOd5HOf2M0d_7jd-J0C2DbO3evPWQNHBazSG0QwoI9UVO3vqaB3S3IivPRDW2lFZJCLndWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 161K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 15:41:04</div>
<hr>

<div class="tg-post" id="msg-68536">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uykzaa_AqJ5BXAu2mC3fT4lp9DVQXDUz6Gv6mwqTPRvxsuK4XqEXRnAPVsjtyfbM_Ut3qRyTGYxYWiapa1IpIED6gMemuws4qKTqo8hzgO-KCpVcLXu5UChh2ykeO4atWH9Pv6OjepFs7-_B_Dj4_-5Z1G15QaTbNv6_9RcSBSFKnSqbeZJ8vEpSYCv2ChvvgBqr9uAKv1bvc9QJmV0kSs4zLgWPUIzyh4-t_VcNjz0HsuKPwIawg0Y7qxG_W69kx1eL4hasDpmDYif3c6Ug-v2IWf3BWRi_3Rey3ArWl_Q_du7QoHSVjjErwsrzcAg0JolEVHtRC16hLdvqRR6klw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛ این 12 نفر از متهمای پرونده میدان علیخانی هستن. +پرونده میدان علیخانی مربوط به  اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/news_hut/68536" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68535">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
عراقچی:
بمباران بیت از طریق حفره امنیتی صورت گرفته و این حفره امنیتی همچنان وجود دارد
.
@News_Hut</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/news_hut/68535" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3548648f57.mp4?token=EngxXc3kUSX1LTEMlUTksaOcYtwSgR2808WXiCIDYXwdZggdLPH5KFdKgpDDW8OCFR01I6ExCEPvUewQtRdzv296vbgKVJMeWDzm5nU7zIuefNVMq6kMNXV9mpPnui9MWX8u0tiUKe1lvYb5LLowGFvoZDauTxleldf8LOUkO6UWAeftS9a8qpWm-5EEyRp5lMPAaddkoeQqx-VZawR7BNHkL9GgL6v1JIfwgH93PXSJwq5IIoirC4HYsg3NOt-G6XVicKnsWtbfK6c16yOWQPCnaXQVc9f7qHbWqs0ss6btwmgzgCQlasGfwUzrE67P8qchS-VUmo2qxZSNSkvMfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3548648f57.mp4?token=EngxXc3kUSX1LTEMlUTksaOcYtwSgR2808WXiCIDYXwdZggdLPH5KFdKgpDDW8OCFR01I6ExCEPvUewQtRdzv296vbgKVJMeWDzm5nU7zIuefNVMq6kMNXV9mpPnui9MWX8u0tiUKe1lvYb5LLowGFvoZDauTxleldf8LOUkO6UWAeftS9a8qpWm-5EEyRp5lMPAaddkoeQqx-VZawR7BNHkL9GgL6v1JIfwgH93PXSJwq5IIoirC4HYsg3NOt-G6XVicKnsWtbfK6c16yOWQPCnaXQVc9f7qHbWqs0ss6btwmgzgCQlasGfwUzrE67P8qchS-VUmo2qxZSNSkvMfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وضعیت ایستگاه مترو در کیف بعد از حملات سنگین روسیه به پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/news_hut/68533" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/news_hut/68532" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exzxR_1SF-itmE77JipijOZ4Ri-8puENs3_sEyaxBXWcgIXH1AkyWWD9vPVo2Fl4NyUcRK3dkwXLQTsyAP0yzjXQn2frRXUT4TzrMqXtlMgq1Na8x6043RyDWa5tSWlQbFmXFFCaW2bQD-HNea1rvRJ4hckl4y_2FExwZ0pMWWjFobCdowvpQRkZD3pV3zLs1m4QmN9hhmOlfhlQ6hf3oyGarP8HVCJzO4Ucvb7aSVlj_Gp7P4RC6MRkC-MKG7NBbtbLfxq2kW9x1b1M9sdWxO_SWVpclNqS7ChMFQ0_5eKTmfNEtE6RqIPQaXZAm8kZOFamycaN1jMLeOde4WPR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/news_hut/68531" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68530">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326d421018.mp4?token=e4LO0EsXbEeT-tygIxNGYDojeLUCI6pSg5QQKYA0vy_6_MidAjlyuq94Lu6CfdJjjn-i7w4yE-UuEyjOd12VmJNN_OHcAEU_MDvlQDSuQaEQxsHHxFkSxOeoBxlegccS2S8DB-jtcs-CDh2YCCgJnXXy7KokLndO1kgwdJFke0xzJXIV6suL85WMbhjNYD-YEkSy80Siw9XQpLvSTG6SRWEAU636qxXKNZ-2n8mDwW8NQPP93RLawXKjOlhr9VnviwCfjWlHYqlZQyX2F_UJm84sRr-w3CgyCQEdHU0DMFrkyjsizRTv8bzjZpzeEaUQA_IfDYHjAkwP3KsoJW5dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326d421018.mp4?token=e4LO0EsXbEeT-tygIxNGYDojeLUCI6pSg5QQKYA0vy_6_MidAjlyuq94Lu6CfdJjjn-i7w4yE-UuEyjOd12VmJNN_OHcAEU_MDvlQDSuQaEQxsHHxFkSxOeoBxlegccS2S8DB-jtcs-CDh2YCCgJnXXy7KokLndO1kgwdJFke0xzJXIV6suL85WMbhjNYD-YEkSy80Siw9XQpLvSTG6SRWEAU636qxXKNZ-2n8mDwW8NQPP93RLawXKjOlhr9VnviwCfjWlHYqlZQyX2F_UJm84sRr-w3CgyCQEdHU0DMFrkyjsizRTv8bzjZpzeEaUQA_IfDYHjAkwP3KsoJW5dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای امنیتی سوریه یک محموله تسلیحاتی دیگر ج.ا به حزب‌الله را توقیف کردند، این یک کامیون خیار بود که زیر آن ده‌ها موشک کورنت ضد تانک قرار داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/68530" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68529">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
ملی‌گرایی از نگاه خمینی، بنیان‌گذار انقلاب اسلامی:</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/68529" target="_blank">📅 14:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68528">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=SVrIsRSDiLCtB94da0rwcjajTvR9uQzqfMKZ_HvQ-OnJX__sHiM5rt5oaaHIzLPdicA_POVhAXR5sl3YIOOnhaTjWZZzNaNkGJO1RUN6FZ3iM9G49CgdhWO7YD5EENqBWxkDSwDRVH2a4kEc2hughY_Wzu9f_xCW8dny9QEndENHVrOLUOP2o-Mqh3nImp2gDhfGRS85IVAFJt08VPTFqxN8KoMG8ubA56S2WofE-4ntfv3ku54gXxLGc_ZVVjBkwx2tmL21NaGP7Z281NNTI7Z1gsAFRuAso1rHSHzurqtaY4N__Oy4JZtDUVPUszeBnt46cEui3QVGyNwUKGe_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=SVrIsRSDiLCtB94da0rwcjajTvR9uQzqfMKZ_HvQ-OnJX__sHiM5rt5oaaHIzLPdicA_POVhAXR5sl3YIOOnhaTjWZZzNaNkGJO1RUN6FZ3iM9G49CgdhWO7YD5EENqBWxkDSwDRVH2a4kEc2hughY_Wzu9f_xCW8dny9QEndENHVrOLUOP2o-Mqh3nImp2gDhfGRS85IVAFJt08VPTFqxN8KoMG8ubA56S2WofE-4ntfv3ku54gXxLGc_ZVVjBkwx2tmL21NaGP7Z281NNTI7Z1gsAFRuAso1rHSHzurqtaY4N__Oy4JZtDUVPUszeBnt46cEui3QVGyNwUKGe_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آتش‌بس با نظر آقا مجتبی بود؟
🎙
پاسخ
عراقچی:
این چایی برا خوردنه یا دکور صحنس؟
☕
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/68528" target="_blank">📅 13:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68527">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران:
ساعاتی قبل، دو کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و دو کشتی دیگر از ادامه مسیر ناایمن منصرف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/68527" target="_blank">📅 13:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68526">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=NnZNY146_4UQIX5sC7hnbSmomDrnKNUZWCgVa7ulxWrl4o34WSy1weGLPLosmMLCZWrQbcRpQIp72AjPX6XqSVqDIs7KHZj4EiEFJExY7uLs-_zSC2JDQgUSJIHkoKIRf5EIcfXBLoLCFzrEtEghiUKJ60vDDV7LOlr7vkusnXVxuxC9DnQt7nOVzYMfRH1AfWLVTweDsrOPRDn5uUMsOuffTXdFPeAD-3DA1Eo9qT6luMu-v776ledK3SQU_eQ6yM7wwlXIny5nZuBY7Zs4bwSOLDuld5dXPoFGJlTijsAoRpinRoAHRsD7OFr1l3FTQdjC9iiZG7uvMpvJXM4OpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=NnZNY146_4UQIX5sC7hnbSmomDrnKNUZWCgVa7ulxWrl4o34WSy1weGLPLosmMLCZWrQbcRpQIp72AjPX6XqSVqDIs7KHZj4EiEFJExY7uLs-_zSC2JDQgUSJIHkoKIRf5EIcfXBLoLCFzrEtEghiUKJ60vDDV7LOlr7vkusnXVxuxC9DnQt7nOVzYMfRH1AfWLVTweDsrOPRDn5uUMsOuffTXdFPeAD-3DA1Eo9qT6luMu-v776ledK3SQU_eQ6yM7wwlXIny5nZuBY7Zs4bwSOLDuld5dXPoFGJlTijsAoRpinRoAHRsD7OFr1l3FTQdjC9iiZG7uvMpvJXM4OpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویری از انهدام یک پهپاد نظامی مدل MQ9 متعلق به ارتش آمریکا در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/68526" target="_blank">📅 13:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68525">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpmb9TlA_hwLq4ffdEU5z3BU9hyjvpfieh_fxk1mGiRXjL4XQCgXpu5le9xMS2oD40I4hT3ZXeEqJ4auEvmC7-z5fItpZ3L3Fm9wz8syeJBeOLUbkFKMqQgEVkXPwE9ShgudiU48Q34ChPH74weJhZd_EFBebsBLRBEhhAwTgfCkiBfWjni5Ggr_5fjrQWW9jQ5w3rYicaObLNxv7uREiE01vaNRqhAYMPvnosC3GiYIpSR0JBnB0u6W8jFW1avstuLHLI8d7tXD9V7TjcVmvLLo-gZbcuPcNDdCQ93QZlJjQZekY8sEgUWxTGgl9AeC6IFdTwzOmwCZQBLQo1mTLH_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpmb9TlA_hwLq4ffdEU5z3BU9hyjvpfieh_fxk1mGiRXjL4XQCgXpu5le9xMS2oD40I4hT3ZXeEqJ4auEvmC7-z5fItpZ3L3Fm9wz8syeJBeOLUbkFKMqQgEVkXPwE9ShgudiU48Q34ChPH74weJhZd_EFBebsBLRBEhhAwTgfCkiBfWjni5Ggr_5fjrQWW9jQ5w3rYicaObLNxv7uREiE01vaNRqhAYMPvnosC3GiYIpSR0JBnB0u6W8jFW1avstuLHLI8d7tXD9V7TjcVmvLLo-gZbcuPcNDdCQ93QZlJjQZekY8sEgUWxTGgl9AeC6IFdTwzOmwCZQBLQo1mTLH_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
مصاحبه عراقچی با جواد موگویی؛
جواد موگویی: دست فرمان شما دوباره باعث جنگ شد.
عراقچی: دست فرمان من نبود.
عراقچی:اگه ده روز زودتر آتش‌بس رو انجام میدادیم لاریجانی رو داشتیم خطیب رو داشتیم عسلویه رو داشتیم فولاد مبارکه رو داشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68525" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68524">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=Rb4CJ_GmckZMg9uFnTfFm7vZdokB4z5MNpcYPyX-cP2OUVMEE70rreqlSrNS0N6njHjLDApskkNWvCt9IVpd3G-gPYBP7JlwBfNPEmQOoDx7sZ1sYUyN7om-TyFdgvqJygHjwVzghirUOta2Sfs0JhW_QYzsm_exoPxEgRePiHk0ri-PcCZUMIPCEkHvTTHMDPMpzgl5_voxSA0POG7Ialfzu_yBSmgMFudL7zEVvIQisPkGEnkw9zzyvgSI6TGzPomvC7eehvFAvcSe9QS9Aap9y-t4zjUX6JNdPT97bQvHDdPiunj2xBMe9ESVdKECmydI0IbSLFzyU-Dt6rpD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=Rb4CJ_GmckZMg9uFnTfFm7vZdokB4z5MNpcYPyX-cP2OUVMEE70rreqlSrNS0N6njHjLDApskkNWvCt9IVpd3G-gPYBP7JlwBfNPEmQOoDx7sZ1sYUyN7om-TyFdgvqJygHjwVzghirUOta2Sfs0JhW_QYzsm_exoPxEgRePiHk0ri-PcCZUMIPCEkHvTTHMDPMpzgl5_voxSA0POG7Ialfzu_yBSmgMFudL7zEVvIQisPkGEnkw9zzyvgSI6TGzPomvC7eehvFAvcSe9QS9Aap9y-t4zjUX6JNdPT97bQvHDdPiunj2xBMe9ESVdKECmydI0IbSLFzyU-Dt6rpD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68524" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68523">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇮🇷
فعال شدن آژیر خطر در بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68523" target="_blank">📅 11:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68522">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3dTHwDJE1eHwsWaNvZuLeL9X32J2h1URQGoIf3vUMIl0bi_ITo_UmdIxReUMIIf5BY4sRab3aSzUkSrgs4JlNR6F5QtemOI3OOfaz9GmirNeouBMsF2_tpMBuVPijX_y6oYpf20FuKYD2al0nsimhbFx6Ys8FwqKTcMZfSddX8pH3DtnxAjK5IlzldvAFUHDA86hMkfTEQg6mLhZBnXXb0M4Gv3dLUgkK0ThpmU2DVwJoIIYhOi-w2iRn9Jc_eiC5sZ3PDgSxh00uUKgUhP1j0X8nNl0IUAh6YDi6EjMlLnyMHyvb-tBvcYJTac_xKcxqzOFbWG-e88bnHYIiFVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛
این 12 نفر از متهمای
پرونده میدان علیخانی
هستن.
+پرونده میدان علیخانی مربوط به
اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی شد؛ چهار نفر از نیروهای بسیج و فراجا تو اون درگیری‌ها کشته شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68522" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68521">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
در هشتمین شب متوالی حملات ایالات متحده، نیروهای CENTCOM با موفقیت به تأسیسات نظارت ساحلی و پدافند هوایی نظامی در ایران، قابلیت‌های دریایی و انبارهای موشک و پهپاد حمله کردند تا به تضعیف قابلیت‌های نظامی در ایران ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68521" target="_blank">📅 10:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68520">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
جدیدا تو جشن های تعیین جنسیت دیگه خبری از ترکوندن بادکنک نیست
الان پدر بچه رو میکنن تو منجنیق پرتش میکنن تو بادکنک و آب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68520" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68519">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=F4jKt383PcCm37SyCgjCwgjMIGAZMTSLJRNPOYBaDwlxTfIv-XxfMi9zRD0hT47aIGWdWcHX2T-6xHAsEYfCQ1mK96MtB85m-hw8DyfsxPiYEzGqhxMUKsFH60M0xmcXIup2TztC9ZUfs5UA_WkzkXARIb7MAX_BhTYsr0bLVRbFBbGDRK9xHq8jc_ggac-31JJFw1DBGkv3bwRabhEw9fJOk5cAs4Gw4xpopz1FjQoEK-zfI3_AnzsBBjlBnXQPlep38fK9h_QxkdEEprLYZe9AAuElRLSr2tir-P8mP1LmV_MSmaAEvw0L0uQ_o688NqgT3gXrOwIrIeD5KsYQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=F4jKt383PcCm37SyCgjCwgjMIGAZMTSLJRNPOYBaDwlxTfIv-XxfMi9zRD0hT47aIGWdWcHX2T-6xHAsEYfCQ1mK96MtB85m-hw8DyfsxPiYEzGqhxMUKsFH60M0xmcXIup2TztC9ZUfs5UA_WkzkXARIb7MAX_BhTYsr0bLVRbFBbGDRK9xHq8jc_ggac-31JJFw1DBGkv3bwRabhEw9fJOk5cAs4Gw4xpopz1FjQoEK-zfI3_AnzsBBjlBnXQPlep38fK9h_QxkdEEprLYZe9AAuElRLSr2tir-P8mP1LmV_MSmaAEvw0L0uQ_o688NqgT3gXrOwIrIeD5KsYQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇱🇧
پس از ترور خامنه‌ای، یک گروه از حزب‌الله تلاش کرد تا پسر نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به نام یایر نتانیاهو، را در خانه‌اش در میامی ترور کند.
⏺
سازمان امنیت اسرائیل، شین‌بت، این توطئه را در آخرین لحظه خنثی کرد، زمانی که این گروه از حزب‌الله به طبقه زیر آپارتمان او رسیده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68519" target="_blank">📅 09:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68518">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68518" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68517">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=iTvL29JICXu8WT3aJCTrxd_u1ss5OLCrU7tdYIHCMjYXIuWeqJtVKnaKVbOKWFWwcC0obRQ8dmVXX248NsGEMFPNQYuKBkwKotwvxl5vhSJY7a_GBOz7YaFB7Ix2SswCI_s8qXN40nah7DV5ORFTJBYPRzUirFabtEvtRX2gdVlyX_FYIrUCcxQfaZMaqSaa1WIcFpm9qzYl5jVLWGgxBpk31xPSOEleQhmwf_h5_nAefA5xnjJUPo7VZck3zCEE3srSk2CtMx9FdjDVcg-RuWdE1XJSxpr_n1MSM9h85MO9i5YOZfuokpNHgAIDF2EOANLjZLbjax--0RYF3lHuYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=iTvL29JICXu8WT3aJCTrxd_u1ss5OLCrU7tdYIHCMjYXIuWeqJtVKnaKVbOKWFWwcC0obRQ8dmVXX248NsGEMFPNQYuKBkwKotwvxl5vhSJY7a_GBOz7YaFB7Ix2SswCI_s8qXN40nah7DV5ORFTJBYPRzUirFabtEvtRX2gdVlyX_FYIrUCcxQfaZMaqSaa1WIcFpm9qzYl5jVLWGgxBpk31xPSOEleQhmwf_h5_nAefA5xnjJUPo7VZck3zCEE3srSk2CtMx9FdjDVcg-RuWdE1XJSxpr_n1MSM9h85MO9i5YOZfuokpNHgAIDF2EOANLjZLbjax--0RYF3lHuYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68517" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68515">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BA-6FGctFNYRpd6hMy0xGM_gk5VYoIghPIDR8TJVKeoBRIfwGobA704WJi_2f89GPeChy8HPsDDXeTmoAW8RkhSf9l5XtULmhKuLagBMIT8lkwu4VJKHPR86NlsCeDcT6XYh9DLg23vcQH3IqIstv_7rj-10MMZQrrouCCI-w5OoBVhQAEaOtcod60dXI5eDRkOk0cSFl-REqNvhLpt1gsoAdR0hawn-Vl4Yx_8Buz80RCQftfGbVFJvQJXMQH_9QArdLqQCaVAkwd47CjyfU1lvkhCkcMUHCFf625yP7iEbD0U-9GaY3AcIzRX-RcaJyRTjaOEANBJaYPnMYKqJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gr0fI8WKVu5xLfh6Y40N6WKTfz9tOwfieHTR5-WZEVWuRPLRrF07-g3zslo22gNxSQcllLCQPEhWdr5wJRHiViV6nrcYlciIpXGV2A-lAeybwnDNAkoNztjLE3avwJXaLHWYRP0DrkMw_-mHDFAeFMtPzWLg8mqggYDaINbN6xqLN4SsbAh6AeaIi-LDVVttATM-PTvgzB6woTG-FQwF6J15247lyx_RtRL_hhDzmExJbKsyITz_MS9N585BwS5jiLsVtwgpg21vfB3mz55rD41jdgWZZfhvYXCm0lx-weSoVejtH2qiNOPaypDvICc0xJ7X_XTizrjqbdQlhaZiuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
حملات موشکی روسیه به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68515" target="_blank">📅 03:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68514">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🏆
رده‌بندی جام‌جهانی فوتبال|انگلیس برنده جدال بازندگان در یک رالی تماشایی گلزنی؛ دشان و تیمش در روز رکوردشکنی امباپه و اولیسه با مقام چهارم با جام ۲۶‌ام وداع کردند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
😃
-
😀
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68514" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68513">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
تسنیم:
حملات نظامی دشمن آمریکایی به حوالی حاجی آباد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68513" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68512">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68512" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68511">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
دو انفجار در بندر‌لنگه
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68511" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68510">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
صدای جنگنده در آسمان کیش
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68510" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68509">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=G9bRB2iZNmh3r3zYM3P7AlkgldaRm0Ez0kEwTcThaSr5T1pd496mL599sY-Ju4klRKtMgwkTmEYNzfJArD6Qcuau8Gz04VQ8BQww8r9a3DZcBonX2UCD9KsvBX6_cLByvrgDzDrmnFCSKF0o-cr7-_vRT1iL_GGC-XDS_iTiJRTQzbw4N1JLGwyrcjMEtVB9pGb0cfi9DOhYI_1ag9jMM3YyZi2S_6XRGVYv2eat6s3i198NP70lz6FWk28zEMhnn5i16M7dSmpVlNdVnfU_ejV8WjZCiK2HLsZwu_PaGW4B8S8uTxw79VX4XeYieOfi0WClo3gt0tMjoLseMRbhzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=G9bRB2iZNmh3r3zYM3P7AlkgldaRm0Ez0kEwTcThaSr5T1pd496mL599sY-Ju4klRKtMgwkTmEYNzfJArD6Qcuau8Gz04VQ8BQww8r9a3DZcBonX2UCD9KsvBX6_cLByvrgDzDrmnFCSKF0o-cr7-_vRT1iL_GGC-XDS_iTiJRTQzbw4N1JLGwyrcjMEtVB9pGb0cfi9DOhYI_1ag9jMM3YyZi2S_6XRGVYv2eat6s3i198NP70lz6FWk28zEMhnn5i16M7dSmpVlNdVnfU_ejV8WjZCiK2HLsZwu_PaGW4B8S8uTxw79VX4XeYieOfi0WClo3gt0tMjoLseMRbhzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68509" target="_blank">📅 02:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68508">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68508" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68507">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph-wYO6kmrLWyjEc8ZM63zlPKSmi9rTGSG_YaXEb3D65vfio8WF6mciqTyhj88U_lZ_YH4MyZgw_V7yGZIlyzMdR2YwgPYqq9J7DBu5IbeswbouLMPhM75IKcQQxoZIZHw71x_WmZQqn3Ine7fVj_hODaygPk3ZhPRQMc_U0g6q_SX7bccSykLLBz2TL38zhbRUsDE5n4Llh-BRFCaRm7yD9_QY_LPsX2wBFxiz6wpYvEpn46oQzylomdM0fNVBNaIgwqZLdJj4DRYVwHD7_U4fuaFVMIe_6oahsiJQVFmawN2fIzsg79jwqd0GCDMuHgmvj66h1SJqRMNhDq2at-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ عصر به وقت شرقی، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و تنبیه فوری نیروهای سپاه پاسداران انقلاب اسلامی است که شب گذشته به نظامیان آمریکایی در اردن حمله کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68507" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68506">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام اعلام کرد دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68506" target="_blank">📅 01:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68505">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm9llfHlOia3Hzh2XeNhHNa8_JxSZUmcIU_sP5iPn1FcWTnyHNB5mByMQj8JNKL8my83wLFg5U1NdBCzzD9WU6-oCaI0gIYiSM3KjJUvOomXH3x9eLbBNxq8_4rnNp-qOSHDlmMCerLLQ0x7d1Dq3QnkgVR_acHCj4vvG7kls_P_Sx4No_44Ref_OmQhTt2s5Ny4e74YgSrQTch5H3L6-rs3pGZ0JYCjC6ZAqUxbsBUSsbJYrDVrZWb_qdKqSuiT8w4whyriu8QQvO0ivGEqkKX72EPayqUIK3HGyIne-ieLJ68hUQdIPfvh7W_682dNL5ONBj-hbqxIjhrtu_3fgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
حداقل پل صراطو نزن بتونیم رد شیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68505" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68503">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vdoanx6icZ7tyHyl6UphWr_Iim43skmrbVRj_SyzdBjv9A3SUazfFHUQ4z7iYY2ENXn_rljxiuhb1gGVtzL5XlK8kAoHKekgFf0-FJeQWR4YWJ7jmR2DArpNYC2C98G89J0l62Gxb1A-XrTjo2fenDVWEqYnxbdWIPwKz8B5iCIwc8w-R_Z8cgoprjHkxAVaoifjlW31jP8NgGfjykY6Z_aEerjDyMaCiVYrslgTyX7ZcYh9hmDB-PnrCUd8NeUMEi-5S2nbc65dZJc0K0u7WwObJHHHGCSm4Bz2Uh9M-Y_u5l_ARIj8_R8LfcEB1lvL-KMaFohBB5DrKWko-aEL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPZqwzuv-HwZMS2Gjp9nWH8VcUCKKpPj0b31u7feRxsUC79V6vkqcdRHPNWHED8YTHEtFUayJcT8Dkf_Xs6QSgOMshzb_m23x2B3pAArKlCLx_pwap9NSGMZetMvlQr2e9bpFMych9BviWxeZUobJ-H3NQwu5dePmhBUTPMozlA8m1zSFzSIl3_JdnAUcHm4tlbdnE4_Apqj4OAYTRvogiRRmNov6XW4h2ggPE_Jow16RagzXv8APnilugbaFYWTReC2okHA_b9fNh3F7dMWWP1MP5rCYdz0eriCpOBomjVvXMKx3Q30ukiCC2wSq_NNAFvut8ifATov9b8CrkiIPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
امارات خواستار توقف فوری تشدید تنش‌های منطقه‌ای، بازگشت به مذاکرات، حفاظت از کشتیرانی در تنگه هرمز و پایان دادن به حملات علیه زیرساخت‌های غیرنظامی است
🤟
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68503" target="_blank">📅 01:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68502">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرنگار: ایران اعلام کرده دیگه به تفاهم پایبند نیست نظرت چیه؟
ترامپ: خب بتخمم
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68502" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68501">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68501" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68499">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rH7wumbhHuQmyGMOCCy3ZiuSI0w1XJJ0orbq_GTtestDGVs-WJUdKrF8j_Fon6E_3bWr6zkd1YWIPg3R_oCK8pjhyZboWvxJX8gKFiZLnkex08Xo9ija6hoW_YGwkxq3VNK3Iofr5EWw9G0tcS6V7g8LkrR00fvYGMcCF9BP8EVjq94urfC52LwYWK4GXajlWgIjXpBlzPXV32Nw_j90ALX7MPtxsdG7nAfda36MXMcoR8DCqkPYIajjO1e40uqc17XhEcJr9A3qGR_Ha-JW_94ydFim5Rl6IGE0VCzkmfRtUyojir75WQGrZypiAXCaI6zwPKM6eSUlwCnc4A32qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6WT8yE2iehIlRT2q07PJzL7M9fP-Bha2WT2Xx9TaDF55Q_Gaxix1-Nvde4IKDi_85XlR5eYnxNRG1a3mqrM2h6n4f_x4__PF6ipE1D80uTRxmqgcU5-NOhMojQloNTcELBzyQfY8YL_TCpBGYtOi4fC0nE8-vvdcLvDpntrvgiIWvGAyRNPDQh4G4f_B8QKMIVirdoqMo6FHrNx3MPSBXZbg5f4tv7ldQaLYEGo6Zbi4CyzbvUPpSeOy-0iZfZG4kl83s2xEzHKNx5RDvnKjiWb_JbXO8pkMwwaOAu44iF7AvJYqXtpL8jwWmkdsI7t_1Y6gwupwpBvsAqAfGgA5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68499" target="_blank">📅 01:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68498">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDqjtEJdFHIS-eJVL0s0KyVCse8EQ3OLRDbXilZRcT_L3KU-8Uykp6q9-q1bJAK8ZtX3IsCaLHA0x0QG0GuenOWL5kv6H6GSLKnL1CpCU7bEkKXVO0uiwtR6LC9GJZC_yeda600jCUI2h9LVoLZ_J-IDf8aqYFTQOp_4vRBK6oLgqSdyZm0MRjCDmBwERLmwLPOEghXgrRz5XXB5GjdpzhWl8fLoS3Wy8Q2F8bjHPwaTjNqd0DFJz0UClZv92KM-z8HqzGTdF9lv_LHaRkp6nLFbWhKu2Gg7GvTrO2-xtxXCS4kwmt6r6EK6XP6qVig125jmR2p94HdDnsGc7p99aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
دونالد ترامپ، رئیس‌جمهور آمریکا به «نیوزنیشن»، در واکنش به کشته شدن دو نیروی نظامی این کشور در حملات ایران در اردن:
«بسیار غم‌انگیز است؛ اتفاقی بسیار تأسف‌بار است. ما از وقوع چنین چیزی بیزاریم. آن‌ها در راه خدمت به کشورمان جان باختند.»
او بار دیگر تأکید کرد: «ما هرگز به ایران اجازه نخواهیم داد که به سلاح هسته‌ای دست یابد.»
ترامپ همچنین اظهار داشت که برایش «اصلاً اهمیتی ندارد» که ایران اعلام کرده دیگر به تفاهم‌نامه (MoU) پایبند نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68498" target="_blank">📅 01:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68497">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JULJDxvLcuw8_Zl2MURHK-hac4MVnxiPxKgEKTDtI5UJXatpWTuIe8h45PZnKeMEUzSoRAPvcnlfh2A9XEXvaVmi_J_KKgwkUSIM84kYnegEKXHEvG1dfGnTL_j36uV02lBUcBmLvIBjvdVrmI-jaN8II0HnFmBV6pK_GPGs_sWjV4XOWmn1wAXvNYNwe9E3-6oSNuuJLdlJUUmTe4pEKgJbjITO0okNtS2eboqa6yUrvw2Qi3wMLQL3BDSak9SOnr7rArgpS2ftn-bYCJoYzOTX1rgWuWtmnoc8igOmuoVKFAr5DgtWoMTXZrL0MuxlvJuJYayqimGBzwe1kcBA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه المیادین گزارش داد که در پی حملات ایران در خاورمیانه طی هفته گذشته، ۳۰ سرباز آمریکایی مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68497" target="_blank">📅 00:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68496">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
بندرعباس زلزله!  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68496" target="_blank">📅 00:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68495">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
بندرعباس زلزله
!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68495" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68494">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwwiuoBtZLtjce1KRm1dVj6lbkuv-dR9T7FST0XWzGhh5qbvLvD_A9RC4Lqj7y1ad2d6m1BOSxRmMlTQIYzDtB1WifY0AaMyhWMUXDzyxdT-RZA2CkCMLYhrXF_pO7zd06oaWuVsBcbK2vV26wYOvVq1ppn2E_oapuvGpnuo9T0gSCtx2neFKhkKqzsvVUo_xY_MxjNYNdgk5mpEyEv8DJ8NpY5JIbGjo0bVMYVs0IbKbAKOaDYk3ylRDVj5P4l8bIBD54ymw0jfct6LVIzhQxEeltanvCTxLW_66bcQ1Wq5q2HDnTLnGlWuP29FMzDHqfY94TqnHTw6ssE8DWwUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز: ایران در طول پنج روز، چهار حمله علیه نیروهای آمریکایی در اردن انجام داده است.
اولین حمله، یک مرکز مسکونی در پایگاه هوایی شاه فیصل را هدف قرار داد و تا پنج سرباز آمریکایی را مجروح کرد.
دومین حمله، یک پایگاه شرقی در اردن که توسط بالگردهای بلک هاوک آمریکایی استفاده می‌شد، را هدف قرار داد و به چندین فروند هواپیما خسارت وارد کرد.
دو روز بعد، موشک‌های ایرانی به پایگاه هوایی موافق سالتی در ازرق اصابت کردند و حدود ۲۰ سرباز آمریکایی که در پناهگاه‌ها پناه گرفته بودند، مجروح شدند.
یک حمله دیگر در روز جمعه به پایگاه هوایی موافق سالتی انجام شد که در نتیجه دو سرباز آمریکایی کشته شدند، یک نفر مفقود شد و چهار نفر دیگر مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68494" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlhvRlPY63YQ41UNdlH3tNBpQPW5uUUjdRdHbjZzaGZr_xDtzw0KLX9qZF9Dg6b_NGeifX5EGA3eax-INIpNb7aLRA2yDuE6zCdLSc1BgufL0lXfP1DzNaVOOLfqlLqAUmcM0y-fU9cQ-gzymJyHj30zrvPuzCc4QoSn3ognXNOUJMwGb7mF1vPysrs4CvSvMgxI1VUTNDpHAg8onTjnAbFywVlIPPk3R7ukUUqD96UOX8ggA2CPukxWEfpP1WuizADlevByuEmifUklNgp7_3Yk2-Nxvyqr60Bb_7IJrWJq_xADMlynrzHhTApHvXx60u8ELTxzSGhz-64RCDDZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیومدن؟
#hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68492" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ciPDXrqd7sb9FgmWPlKC49aTXnXU_sS0aXN4Q6nTBBvlP2GRDvurw7VeUncctp43VcYIg2SXlnurhX9VtchO893zyDD1yhjFkEq_BNqWNzg_-nfTyeEtQVwfC3_qExDRIFd80ApRormo79VQl-0JPAU89MSNGdIIdo1eR1KG-_wm3HeD2KxYUrzQFKeVSIUyUVSr7l3ics4txe5Jdk5KVU_zc9fnMQhdBZQquig1KOwtJbgzrzeJXmcUQE8tL7ym2bnrlMgr1_g9md_MjU0WYYk4GjbGyW5VvG7jA68Vrvo8lsYOhcacpuzr0932ObvLL74JYTBO7p_SB_A4B7ePtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PgzxwtKj5fjAS_NcfGEwB4tZ5JXmzfJWeD5J2E0-jXw95cD7_tJ265OIfos6Pf7Kz3e95USbhwR0o6ndkNdv-OIIExTZz_KznwdN3THT8ZN4YggaNTF6KXeie0DkOV0RxVNdzGb2G71UBpj9ihs5IBXk-eKrmpGXPBtQ8ELvL_Et1gkW-bIc4qxrt5RnTozBIV2-xCw8nhXvvN2j0eNyLn4AIxLauIihHT0N-oYAZgQX7yqO5Dz1nD554W98g5WEYW_v41imP2pgihTr1eAhthDerXB4SG4XW-77OFpX4F_bBL7XxgeXvm6to48LNG8h2ww03e0v5m3DK7bCYrx8fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیلی افشار دوست‌دختر سابق تتلو و پویان مختاری هم این وسط تصمیم گرفته پورن استار شه و یک کانال زده تلگرام که ورودیش 2500 استارز یعنی معادل 8 میلیون تومن پول می‌خواد، البته محتویات کانالش لو رفتن و کافیه کلیک کنید رو لینک های مدنظر پایین :)))
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part2)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part2)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part1)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part1)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part2)
🔥
🔗
مشاهده ویدیو های لو رفته جدید
(Part3)
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68490" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اماراتی های کاکولدزاده خواستار پایان درگیری ها شدند
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68489" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68487">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=VdL8ahBdtOF4nKaxwxldFZ-GDubYT_W_Au5nMAJXQdKwaKCi97CF32ggpb3vkS-QLaoKIhk3eqNgDuK3GgH51GJDaU-e3bt5p-o02ZW2OnsBJ-dPKs2-JIhK14HVH47jmT2rnANGEzbWIBGhZ-BqzvrOhk8ggAAGVunTtReKDTBIDKKcU5h_bV9K_-_pIcRAo7mDIsxV8GN8fmSiSl5IzzD54azsHv1VE5tSc4_mmf6abLe3Z6G_2kU6yV-zydpZA0ithQNZ1SqW39xK1pbSi7te0N4SODWI1xhVF1cvmoLa7LBFtE6zLvH6ATDzbgICLUsuQJ4Q9Z4QI4p6r1MeFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=VdL8ahBdtOF4nKaxwxldFZ-GDubYT_W_Au5nMAJXQdKwaKCi97CF32ggpb3vkS-QLaoKIhk3eqNgDuK3GgH51GJDaU-e3bt5p-o02ZW2OnsBJ-dPKs2-JIhK14HVH47jmT2rnANGEzbWIBGhZ-BqzvrOhk8ggAAGVunTtReKDTBIDKKcU5h_bV9K_-_pIcRAo7mDIsxV8GN8fmSiSl5IzzD54azsHv1VE5tSc4_mmf6abLe3Z6G_2kU6yV-zydpZA0ithQNZ1SqW39xK1pbSi7te0N4SODWI1xhVF1cvmoLa7LBFtE6zLvH6ATDzbgICLUsuQJ4Q9Z4QI4p6r1MeFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایونت ورزشی، ۲۶ تیر؛
پارک پردیسان پونک
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68487" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68486">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام آمریکایی به شبکه NPR گفت:
«رئیس‌جمهور ترامپ دستور داده است که فرماندهی مرکزی نیروهای آمریکایی (سنتکام) در ساعات آینده، «دروازه‌های جهنم» را به روی ایران باز کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68486" target="_blank">📅 23:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68485">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=e1ixUgtEO6xlxt9foA1Bje11P2ALyMj0uFXIIwHO9h-jynf8q9drthQiaT2MRL4EvVdCLjGbfzy1WX1i_VOFPwf-4-VLIsbnPEe-q1a0purqr1VNvYfxApxIJLKRwcd4rcdGQ0nyvnqZOvSWHYMxa_Z_MU3e-2fKHBkg-Y2QLdCEtxUM1Szmpm37FGgk1XuWmcVxqdpH1FwAPDC3QzMS-XmDxujDMOzi4UaTwatO62FzIAbHm7V2I0eyKSKNYrfCALE-JdP1uijyuu0MXFcwyRXUpXIX0d4TNTWLqRERAgZgVuyGt5kyu-saM_C9qjoTBMrcSUprxNu5R3LQ60Bl3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=e1ixUgtEO6xlxt9foA1Bje11P2ALyMj0uFXIIwHO9h-jynf8q9drthQiaT2MRL4EvVdCLjGbfzy1WX1i_VOFPwf-4-VLIsbnPEe-q1a0purqr1VNvYfxApxIJLKRwcd4rcdGQ0nyvnqZOvSWHYMxa_Z_MU3e-2fKHBkg-Y2QLdCEtxUM1Szmpm37FGgk1XuWmcVxqdpH1FwAPDC3QzMS-XmDxujDMOzi4UaTwatO62FzIAbHm7V2I0eyKSKNYrfCALE-JdP1uijyuu0MXFcwyRXUpXIX0d4TNTWLqRERAgZgVuyGt5kyu-saM_C9qjoTBMrcSUprxNu5R3LQ60Bl3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که دن اسکاویینو، از مقامات ارشد تیم ترامپ در پلتفرم ایکس منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68485" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68484">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68484" target="_blank">📅 22:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68483">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇱
نتانیاهو شیرِ یهود برای آرژانتین در فینال جام جهانی در مقابل چپول های اسپانیایی آرزوی موفقیت کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68483" target="_blank">📅 22:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68482">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68482" target="_blank">📅 22:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68481">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ پیت هگست: خدا نگهدار قهرمانان؛ فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68481" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68480">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖄𝖚𝖘𝖊𝖋</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=Wkjo2HWdzKx_rW0Okps4qfnf1Mc7RLEnDFYgSMoKttRUsDIjEy9b0tiLF4qy9cp3JxYyyz4nbrpi1zCQWZdPGW1GiBC8zT0sdWMiQ9CXwC6DlzzV7CtZhXhUS19Hm4PfCJ6lDxswqFMyZSUiqU_AVlXKrB4TSlV5kT3o8PM2ppwKE51bsyRjZ_e2uMBXSncnNX-bB79bS8Gwy_V3Rj8jx6EgyTcYLKMLWp3pXBEPPoO80-_N6FgRI3rtyFz4u0QZ5V7AltN7_TR8oUbVQkdICDrbTAAD-pUe8RgE2co_tXC1WOfw9FfG4Da8c53FG8YUVcBs7RgeUFPtyjfUx1lGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=Wkjo2HWdzKx_rW0Okps4qfnf1Mc7RLEnDFYgSMoKttRUsDIjEy9b0tiLF4qy9cp3JxYyyz4nbrpi1zCQWZdPGW1GiBC8zT0sdWMiQ9CXwC6DlzzV7CtZhXhUS19Hm4PfCJ6lDxswqFMyZSUiqU_AVlXKrB4TSlV5kT3o8PM2ppwKE51bsyRjZ_e2uMBXSncnNX-bB79bS8Gwy_V3Rj8jx6EgyTcYLKMLWp3pXBEPPoO80-_N6FgRI3rtyFz4u0QZ5V7AltN7_TR8oUbVQkdICDrbTAAD-pUe8RgE2co_tXC1WOfw9FfG4Da8c53FG8YUVcBs7RgeUFPtyjfUx1lGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش پیت هگست به کشته شدن ۲ تن از سربازان امریکایی</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/68480" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68479">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=c25CwuF9Bb47pASNugiEVe5gvahgD0S_62qd9G6Y5s62gST0OmF_ekOJKJhYxQvlVoPHDJP39GO5QCiWMC8bK6Mz_9wok2-FO9VEl7pyZzE42JdvoUY2Z92eE4rs1SxhXGpJLOn_gEjuPZhQJXTHOQ78lFSvIpp5T-CLrknl5oQnL94PPQ2LL1sqK5vaRGuNxGBEYIJe8XpEGScmDIAKgZggrgd4yGw6XlRbXzfoemR3Je5yNDRu0yYqTG_F7MeO680Kn-jnxhyHALqrsL_YXyuI31qZEcT7Rs8KMKt_ss8kRGamSDKrw779VMSQj9FYcoOlUyDiH0TFLSG0g0p6_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=c25CwuF9Bb47pASNugiEVe5gvahgD0S_62qd9G6Y5s62gST0OmF_ekOJKJhYxQvlVoPHDJP39GO5QCiWMC8bK6Mz_9wok2-FO9VEl7pyZzE42JdvoUY2Z92eE4rs1SxhXGpJLOn_gEjuPZhQJXTHOQ78lFSvIpp5T-CLrknl5oQnL94PPQ2LL1sqK5vaRGuNxGBEYIJe8XpEGScmDIAKgZggrgd4yGw6XlRbXzfoemR3Je5yNDRu0yYqTG_F7MeO680Kn-jnxhyHALqrsL_YXyuI31qZEcT7Rs8KMKt_ss8kRGamSDKrw779VMSQj9FYcoOlUyDiH0TFLSG0g0p6_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه اصابت موشک‌های بالستیک به پایگاه موفق‌السلطی اردن که گویا منجر به کشته‌شدن دوسرباز آمریکایی و مفقود شدن چندتن دیگه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68479" target="_blank">📅 22:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68478">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیش‌بینی می‌کنم که حملات امشب، از دیشب هم شدیدتر خواهد بود... #hjAly‌</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68478" target="_blank">📅 21:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">همونطور که پیش‌بینی می‌شد، دامنه حملات امشب گسترده تر از شب های دیگه شده و حتی حملات به یزد هم کشیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68477" target="_blank">📅 21:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=JYo_TbJomA9G8FAP4bOkie2NjmrudHkdizfenpwhWO4PopiNBQRggMKfmBi3iSHQ2RPpn3CfRkwDP5ZoDEg0nz_W1a2OkokFzdcEruKnIdR11NorwwzEkrEhSRk7KmDvrc0mkB4ERHprIIWmTeEkKsGK86Do_h72jUyagrURVu_0pzgpbcmWPORkA73FutIphUM1VVnoATpSebEloy0wSAMFpvLrBIBP32BlZo44fbte1M38sVaCTuOXLK5zL9mAv3QX7u4I8s0KNRiTzvYBHydxFrvubc1CsGeJKHnTKmKo-FeRqR4MQg06Uvk24EMiQUYUw17etnVMbsueNi79nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=JYo_TbJomA9G8FAP4bOkie2NjmrudHkdizfenpwhWO4PopiNBQRggMKfmBi3iSHQ2RPpn3CfRkwDP5ZoDEg0nz_W1a2OkokFzdcEruKnIdR11NorwwzEkrEhSRk7KmDvrc0mkB4ERHprIIWmTeEkKsGK86Do_h72jUyagrURVu_0pzgpbcmWPORkA73FutIphUM1VVnoATpSebEloy0wSAMFpvLrBIBP32BlZo44fbte1M38sVaCTuOXLK5zL9mAv3QX7u4I8s0KNRiTzvYBHydxFrvubc1CsGeJKHnTKmKo-FeRqR4MQg06Uvk24EMiQUYUw17etnVMbsueNi79nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
یادی کنیم از این سکانس که ترامپ چند وقت پیش در تروث‌سوشال پست کرده بود: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68476" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68475">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:  در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68475" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68474">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojkkdEPmhPIkUsZrI4izNy2jJjm2nxR1Fun72VWSn7w196M8uGSaVSRQ6fL74H5UxVP8H-RjL4srbbLnG36N2b-ajZ2CX-sqqqHBd3RQLtIgcawYk8YQOLI5_nkXLujbFJDIbvmFJvbOVe7AxA88VI6zNEqEaNtiFoQcU0BUDui39gHQwhjcrjXwGKXPWCpzKNhSjndjyoD7wTQQMDeglQemFPvRn-1nscWgxfTtZvOhKdkHiz3S9zt3txJo0J5f5zNKF3N6pc5qly1Wm2uxHYOtm0e9IkG2bUihiiMsUTlSckKw1cl34Ofq8kO_0EFW20lpr0rF4ddGALV1FTBwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.
همچنین، یک نیروی نظامی دیگر در حال حاضر مفقود است.
چهار نیروی نظامی آمریکایی برای مداوا به بیمارستان‌های اردن منتقل شدند که همگی تاکنون مرخص شده‌اند.
سایر پرسنلی که به دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به محل خدمت خود بازگشته‌اند.
سنتکام به احترام خانواده‌ها، از انتشار اطلاعات تکمیلی — از جمله هویت نظامیان جان‌باخته — تا ۲۴ ساعت پس از اطلاع‌رسانی به بستگان درجه‌یک آن‌ها، خودداری خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68474" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68473">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=vYP3eMX_TgwbhmmvYcIY3iCmlOH3OZJ4a-OInWeLXdFQPnQ4znU6RGIED7aPUSACju6EUhL1mSbVx6zjbquoh-9q5P9vvcFieyrU2LnBjoiczBlIZZwJbBhUZ2ZSSK_obdLrXIq3AnUtthb1tizADtK6bkdYoPC0AV6eB8ExZPru9QVfSmtc4TY8cFNRsZhB-NuEzNd9-h7drM7ZWD14zQxf4ayMMKKo1IbVD5AtoDIvKOE9zS7Astrwdn_d8BnjPx9jEJFjik93PGxWaAGglJlrUY47MrEQrvGC_HFIrduIXhaCBeD4MfxWBRwrsdUPGVFS2I6_FlhHggEWfrnvgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=vYP3eMX_TgwbhmmvYcIY3iCmlOH3OZJ4a-OInWeLXdFQPnQ4znU6RGIED7aPUSACju6EUhL1mSbVx6zjbquoh-9q5P9vvcFieyrU2LnBjoiczBlIZZwJbBhUZ2ZSSK_obdLrXIq3AnUtthb1tizADtK6bkdYoPC0AV6eB8ExZPru9QVfSmtc4TY8cFNRsZhB-NuEzNd9-h7drM7ZWD14zQxf4ayMMKKo1IbVD5AtoDIvKOE9zS7Astrwdn_d8BnjPx9jEJFjik93PGxWaAGglJlrUY47MrEQrvGC_HFIrduIXhaCBeD4MfxWBRwrsdUPGVFS2I6_FlhHggEWfrnvgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
اگه حملات آمریکا تا چند روز دیگه ادامه پیدا کنه، وارد مرحله تهاجمی کامل میشیم
اون موقع دیگه فقط جواب حمله رو نمیدیم و حملاتمون گسترده‌تر میشه همه جارو میزنیم
آمریکاس که ریده به مفاد تفاهم‌ نامه و همرو یکی‌یکی زیر پا گذاشته و عملا از تفاهم نامه فقط اسمش باقی موند
آمریکا از جنوب لبنان عقب‌ نشینی نکرد، توی تنگه هرمز مسیر غیرقانونی ایجاد کرد، به حاکمیت ایران احترام نذاشت، به سواحل ایران حمله کرد و اموال ایران رو هم آزاد نکرد
دیگه نه روی کاغذ و نه توی عمل چیزی به اسم تفاهم‌نامه اسلام‌آباد وجود نداره
اگه دوباره مذاکره‌ای شروع بشه، از طرف آمریکاست و اونه که دنبال نوشتن یه تفاهم‌نامه جدید با تغییرات تازه‌ست
اجازه نمیدیم نیروهای دژمن از تنگه هرمز رد شن و وارد خلیج فارس بشن، چون امنیت کشورمون به خطر میوفته
🌅
قبول نداریم آمریکا توی تنگه هرمز، که گلوگاه انرژی جهانه، نقش یا حضور داشته باشه
آمریکایی‌ ها منتظر موج موشک‌ ها و پهپادهای ایران باشن چون ما جواب حرف‌ های ترامپ رو توی میدون میدیم
فعلا سیاست ایران اینه که هر حمله موشکی رو با همون شدت جواب بده
انتقام خون فرمانده شهید و شهدای جنگ رو میگیریم
آمریکا میخواد با محاصره دریایی، مقاومت ایران رو بشکنه
ممکنه دوباره به سایت‌های هسته‌ای حمله کنه یا بعد از اقدام نظامی، ایران رو به مذاکره با شرایط جدید مجبور کنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68473" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68472">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68472" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68471">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=pXHQmuXbBC6LfpbHtYGZfXu88kOW9_OHKfZKLgv8v_ryfhM0Fo5sBN4r8mEaN-2jy9QzsiR3HbBDgrQsrokRYnh_XnUuPnbiFMUUbqNZ1UkJQ2-DeU-JVkR1LFE22LyLPQ-ixNZ31nLJCpFC1o_Zl9eYVNNcAVg4B59GQWCoilTBMstS3mB1uzOyQWuNTuwbAK_YIheWVMFY7mbKaGqO0nlGnyB-BEWQs29CfI_pHmQkCioUiwsW-Cnc1lhUtYwocnKSHw32cddQ9usfvk1wWLliGDTM6ahDlI4dsQnLLoziOtyS5sTz2iJfkpaPMzQMmiLCHA5tzRsRWLXi-34r4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=pXHQmuXbBC6LfpbHtYGZfXu88kOW9_OHKfZKLgv8v_ryfhM0Fo5sBN4r8mEaN-2jy9QzsiR3HbBDgrQsrokRYnh_XnUuPnbiFMUUbqNZ1UkJQ2-DeU-JVkR1LFE22LyLPQ-ixNZ31nLJCpFC1o_Zl9eYVNNcAVg4B59GQWCoilTBMstS3mB1uzOyQWuNTuwbAK_YIheWVMFY7mbKaGqO0nlGnyB-BEWQs29CfI_pHmQkCioUiwsW-Cnc1lhUtYwocnKSHw32cddQ9usfvk1wWLliGDTM6ahDlI4dsQnLLoziOtyS5sTz2iJfkpaPMzQMmiLCHA5tzRsRWLXi-34r4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68471" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68470">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی مبنی بر وقوع حادثه‌ای بین یک کشتی تجاری و نیروهای نظامی، در فاصله حدود ۱۰۰ مایل دریایی به شرق شهر الدقم در کشور عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68470" target="_blank">📅 20:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68469">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
تفاهم‌نامه بار دیگر ثابت کرد که امضای رئیس‌جمهور ایالات متحده هیچ ارزشی ندارد و هیچ اعتبار ندارد، و مردم ایران درس‌هایی فراموش‌نشدنی برای دشمن آمریکایی دارند.
امروز، "شیطان بزرگ" بار دیگر بدون هیچ پوششی، چهره واقعی خود را آشکار کرد. این تجربه تلخ از جنایات و نقض عهد، مدرکی جدید و قاطع بر دروغگویی، بی‌منطق بودن، عدم شایستگی اعتماد و فریبکاری ایالات متحده است.
اکنون که دشمن آمریکایی در تلاش است تا جنگ را شعله‌ور کند و هزینه‌های گزاف بیشتری را متحمل شود و اعتبار خود را بیشتر از دست بدهد، باید بداند که مردم عزیز ایران و جبهه مقاومت، درس‌هایی فراموش‌نشدنی برای او دارند. در این روزها، شجاعت رزمندگان اسلام و جوانان مناطق جنوبی، نمونه‌هایی از این درس‌ها را نشان داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68469" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68468">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای ساعت ۲۰ پیامی را منتشر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68468" target="_blank">📅 19:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68466">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
هم‌اکنون زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68466" target="_blank">📅 19:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68465">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoZocu4UliizRVSmkcEWO_kh5T4zgu8ULs1ffQp1eigyHIMV7CoakJ4XpLIJH5BSWurU2RlIsV5Yn2hAuxLerrjHWyNDJkVjcVlqWvsOPxG4rsz1Ig-5dCn3CHoM-QhKmNPQJSKt-Mfobdcgo_EW4U-NWJlxr1CuLibrWPgzFNOT6YIaAgQB_qH1E8gvGDVJDkupajibw86lYs_B8EEQqzLkg0lCUCFk14_35h9icxWQ5Y9NHmiDjIKxkCOz5GUtsY6GQrbdeyYcLELDA_Aq5pPH20PYbAoL0COg96NPb2tHkm1FvcLIzMevnqef6yAEB54tSR7DTWKwgRxuV6q9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68465" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68464">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68464" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=cyH5RI4hszpnI8pEIfT1slj7-2qAmIEVTHqAX6cABcIPQOhuHlhdStwAb70T-BY1cvkpsIiq9Wcb_Bf1LKn4swQ9O0Th7smHDbfd4kEu4e3aVr6gVlgjVDI5Ad0-5lRih5AL-d7jRpMzV6AnYpWQ3naXrIeInqqolkJAkWmAAGsNLeD2DyShJEfm_-IzaYQ8Ywf3JPhh6TtKM665UhOPFPVwCAnlNM5IfpHoYwOjK5N61ostPcs67oawPwPMXotWQrPkMstV928cW-_qDEY-WiEdmhCpDxj9Y1tYGYQDSkcybYXc5E2XNbZx4moHZDGYI7JfKDe23jav8jyrY_taIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=cyH5RI4hszpnI8pEIfT1slj7-2qAmIEVTHqAX6cABcIPQOhuHlhdStwAb70T-BY1cvkpsIiq9Wcb_Bf1LKn4swQ9O0Th7smHDbfd4kEu4e3aVr6gVlgjVDI5Ad0-5lRih5AL-d7jRpMzV6AnYpWQ3naXrIeInqqolkJAkWmAAGsNLeD2DyShJEfm_-IzaYQ8Ywf3JPhh6TtKM665UhOPFPVwCAnlNM5IfpHoYwOjK5N61ostPcs67oawPwPMXotWQrPkMstV928cW-_qDEY-WiEdmhCpDxj9Y1tYGYQDSkcybYXc5E2XNbZx4moHZDGYI7JfKDe23jav8jyrY_taIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این ویدیو کامل نشون میده که تحرکات هواپیماها های ترابری امریکایی از سمت اروپا به خاورمیانه بشدت افزایش داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68463" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp20oR_BkzUmnXsRR6-0vCv1V-WloCiwk15tqPI0HYjxsNJ66N1VjAeX66OeBZWo2ktYLhn19CbCr4gwxhjiRaFVXLJgNYc03HOocEvhK-2x59IMQevnO8z9MfikePMMXR5sRvo2F1eqTtIPQiNQVkSPKTve1x2Fu_UHg_R-Y2G-5zbEGqt4AduzfPhHs2HNnRUK3fJ8HbNkj4_6vYR0ldLS8IBJ_z2zEf56e-HVXqmmBVlQ5kCU7DtMS4lYh5_OSTuebOnLLkYZIlgW6Z_DrWyu3h0Hn7TGxheh6L3VmR4isQfpixGofPLHBT2s-suzkj6oQNacRuHEfdR8RQ0Dsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68462" target="_blank">📅 18:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4px_nKd6LyBZpQGQ2QSEM9LJma0w8LTJra8cGZTcoWsu8CR1UsrpoPbBhMI4UtE1EbWu5J_nTAMvCccz8LmU_7uxjNcb-c881NlWrvD4UrnQFOuQ64k17eyisg8W9upz0sp8YHsu3eJHmW8SGsLGChmGvZioD5INCtD56bE3itP7jXwQjPDN5am-9VpCBRoBJqa0uQARdiWphUQJXuRrSaeCPdO-oIRm7CTSsQvqzkqDk8EPvMoLkO22WF7WbW88mDRpiIKYifIHQ1h4Cy_Zvm-SQWxW1CpqOJvtm1GVyCCMLfEPQNGnjXGpc7cszDaDknFPF0K5VhM6ULQ6I7Lfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نماینده مجلس:
بنزین گزان میشود؛لیتری 10 هزارتومان
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68461" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:  «اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68460" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:
«اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68459" target="_blank">📅 17:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=X0-VRPAx5my5R5Wis3Y07H8ljAjw_n9zWQIbYFSloCdfTim5Ii5oBUuqOJpe8BfRoPVIrk7H3p7LBMbydtGVeb2hh72JDx1uf_gMiGIJ1fSUQCO1N36MF2jpPVbs4frRMmZ7CTyi8s3c7qNrHB_egJxOvj5Rs_3PGRFmA3E4Z3P8N9UQXvNOXvxh8qijEgAiIwwln-vYzmGZz-09bvKNNA6Hun6yUwdp0dKOfPcK0njKmcO4UXqdPL55r5943AFoKg69ZiGGDvY35dJVc_J4t_HbflF1Jzq7IpzlQMIPe6zhFdLXJOHHyCzRfnfRj8HU924BQ_gZs7UcfPClIubNjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=X0-VRPAx5my5R5Wis3Y07H8ljAjw_n9zWQIbYFSloCdfTim5Ii5oBUuqOJpe8BfRoPVIrk7H3p7LBMbydtGVeb2hh72JDx1uf_gMiGIJ1fSUQCO1N36MF2jpPVbs4frRMmZ7CTyi8s3c7qNrHB_egJxOvj5Rs_3PGRFmA3E4Z3P8N9UQXvNOXvxh8qijEgAiIwwln-vYzmGZz-09bvKNNA6Hun6yUwdp0dKOfPcK0njKmcO4UXqdPL55r5943AFoKg69ZiGGDvY35dJVc_J4t_HbflF1Jzq7IpzlQMIPe6zhFdLXJOHHyCzRfnfRj8HU924BQ_gZs7UcfPClIubNjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی در کویت به دلیل حملات موشکی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68456" target="_blank">📅 17:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHKLKeqX9vL2EOn-DYU7H9t-XxAIGcU_FdQ2FiXe-0Se84zM1N6VPck5YGaQXAvDtt3ea4m16EGu2COSKtUIul53weh4yEJeok21mWxlXUidDaYXfmR81XYmjJl52cevdzRv639MaCpH9R2S6bOZv9U_8F4YFKRwkauz_6OGTPoS_r-2jybVPPlvcSeM_zOs6Nnz25ahwY6F16wWT0ZywqIKDGjRM0HtHFd4_4vVZt5J7gHQwYQkVcJE3OdyCnktLaEEhdtcM_qMrrqdQ4tsWfUrK5sgGKJPRYnvZQmEv-xQKMLo-DS6HhsB4PStiiAQhdE7n4MPsba-kptzBICy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛معاون وزیر امور خارجه جمهوری اسلامی، کاظم غریب‌آبادی:
«از این لحظه به بعد، ایران اجرای تمامی تعهدات خود را بر اساس یادداشت تفاهم، به حالت تعلیق در می‌آورد.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68455" target="_blank">📅 16:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68452">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00f574479.mp4?token=Iw0OUW021sGKlx3xNTkqM72B-J0XeCwGhSJxvWFR_L7_GFLR9tepSGFKlRG3PxAlT0_GcrqixejHWvwKtcRUdvDjXf5eCMyB2PyotTkHpU1YVm85AN_PYTHMlIccUxwur3ddEdJPm4zs1nnQfEwKACYLkw7iDHzJxV4fey97I8EHDwPM5xxl2KCacMcXButcNHUEicrTuiGuozGxdGeQi5BvLZQlmnYCvO_MnGs98V0LiM-uHHMJz_gfe_UK_FzntT-B34W3QEOB7De6Cb6I31CQhi417EIlYkopJUwdXdu0iQFey3Sft-Kv9qZ-vQun89YnsopP5tFxwalSUS_RMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00f574479.mp4?token=Iw0OUW021sGKlx3xNTkqM72B-J0XeCwGhSJxvWFR_L7_GFLR9tepSGFKlRG3PxAlT0_GcrqixejHWvwKtcRUdvDjXf5eCMyB2PyotTkHpU1YVm85AN_PYTHMlIccUxwur3ddEdJPm4zs1nnQfEwKACYLkw7iDHzJxV4fey97I8EHDwPM5xxl2KCacMcXButcNHUEicrTuiGuozGxdGeQi5BvLZQlmnYCvO_MnGs98V0LiM-uHHMJz_gfe_UK_FzntT-B34W3QEOB7De6Cb6I31CQhi417EIlYkopJUwdXdu0iQFey3Sft-Kv9qZ-vQun89YnsopP5tFxwalSUS_RMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
چند روز پیش یه ویدئو از یه پسر نوجوون وایرال شد که از سرکار اومده بود و داشت موتورهای یه نمایشگاه رو با بغض نگاه میکرد و حسرت می‌خورد؛
⏺
این ویدیو خیلی دست به دست شد و نهایتا مردمِ نازنین ایران، تو کمتر از یک هفته پول جمع کردن و واسه آقا یاسین موتور خریدن و اینجوری سورپرایزش کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68452" target="_blank">📅 16:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68451">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون جنوبی:
همه دارن از جنوب صحبت میکنن که دمشون گرم ولی منی که خودم جنوبم نمیدونم چی بگم.
درمورد پمپ بنزینی که یکساعته داخلشم صحبت کنیم یا مثلا درمورد برقی که الان رفته و نمیتونم برم خونه صحبت کنم
درمورد ماشینی که نمیتونم خرجش کنم صحبت کنم؟
درمورد وسیله ای که میخواستم بخرم و امروز صاحابش 40 میلیون گذاشت روش صحبت کنم؟
یعنی حتی نمیدونم از کجا شروع کنم
ببین قبلا به موجودی کار نگاه میکنم میگم خب بعدا این چنین میشه اما الان تخمم نیست
الان میگم بتخمم ک میزنن نهایتش اینه منو میزنه و میمیرم
چرا برق بقیه شهر های دنیا نمیره برق ما میره ؟ ما اضافه ایم ؟
بدترین اب و هوا و اکوسیستم و بی برقی و جنگ مال ماست نمیدونم از چی باید بگم
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68451" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68450">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFkIHiSafhUw1WgFnkYzETsrqhtP2MHx_LqIZ-AAepZLzuXvjjvHfFzCzCmFTYSKmROkndP_UbizsZR4_7RCemPRZdDWFkAt-MvZHFJjfwVLiNBcoZufEnRy1Q31BYadmnnYgB-DdSzZL4VtLcvb5tDY80ei_90S9sTcqVmJcLUVPTsFt-oNb2B7bvtmdyKpx-u8U5huAiFZi7KaniMRZY0FJezuXBqhnLhrvt-WqWdSTsf0KLS3SJnXNaHweXAFxpnOkLRHyfFhPV7ChLu5jC__W6LJ0LDZ1EFi9nuJnNK0LsZCus2cVpwo_TfFi72VRwzLxbp9a1pykshwM-kN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حکومت داره به جانفداها زنگ میزنه که بیان آموزش با اسلحه ببینن و برای جنگ آماده بشن
😂
😂
اگه کسیم بهونه بیاره که مثلاً مشکل دارم و نمیتونم بیام، میگن اشکال نداره، بیا آشپزی کن یا کارای دیگه انجام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68450" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68449">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=MIylg5r0QyfQ-fQurbnFgH174uwX0X0E3zTBo2Sz4lqj0wTETMZLf12ah0ubaWh3R6D3759a7QQ6AnPz0FBV7Hb5_Sr7tFo9gUgRmaC5u3QOLVY_a0k-RQOyGPJE2IptzT7Bjla5e_PrpeFyFj0oEQlNOz7NhO6PIgRSTYFrfwlp5wdpm4rjyuEQJWV72EFYC6a5LN-rhlKAWmGcapULPSfR3ghU2PnKI4b6vbx8HQt5MLc5255uTDcEXwFsLb_50z43PAHYIWuP3IBfSs_9wL1_IM_nQbaGhvfqpZI8C_MKUUlxXEGoFeRlLSsd_zIBor8FFf7DabgXYfHfTgEAFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=MIylg5r0QyfQ-fQurbnFgH174uwX0X0E3zTBo2Sz4lqj0wTETMZLf12ah0ubaWh3R6D3759a7QQ6AnPz0FBV7Hb5_Sr7tFo9gUgRmaC5u3QOLVY_a0k-RQOyGPJE2IptzT7Bjla5e_PrpeFyFj0oEQlNOz7NhO6PIgRSTYFrfwlp5wdpm4rjyuEQJWV72EFYC6a5LN-rhlKAWmGcapULPSfR3ghU2PnKI4b6vbx8HQt5MLc5255uTDcEXwFsLb_50z43PAHYIWuP3IBfSs_9wL1_IM_nQbaGhvfqpZI8C_MKUUlxXEGoFeRlLSsd_zIBor8FFf7DabgXYfHfTgEAFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واسه دومین بار طی دو روز گذشته، جمهوری اسلامی به نیروگاه برق و تأسیسات آب‌شیرین‌کن تو کویت حمله کرد و باعث آتش‌سوزی شد.
کویت حدود 90 درصد آب آشامیدنیش رو از طریق آب‌شیرین‌کن‌ها تأمین میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68449" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68448">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6BD4hs6Fi_itJPgw07KV5jWLPnzxqRfN0xcwS8DG0Eo040Qrj8MKfFAg7wrS3bcI5bmPOzF-7on_PGRuQduBgsBpp1tTY-rBtHU66sxerfEIvn-HGeEd0zNj74RAvPTKNiE63-Kla-JH6R_dt5JjYDzV3kwImt6B8JpFdLd_41ifNiCgG3RrtkoNIyZA-wrjAe23gXMWLB0DzmoQRGMhjPfNzfmJtAYZk4akslEG4neK-DkkYydiOSgucwK7699Tmj_CiMaD9IwFbq_nGEsYXqMlwhq-0AtxAd69MThk1DmNb4u_Lg60D0dMDTcrHZgS9fT_41FRD2aNRILTLgWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68448" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68447">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68447" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68446">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=OvVVv3hf1B6eCxHSg7ht8XfJAS5K2VKLA17zR20paG6PgKC8YvQ_a0B6w66NIazhljaxpV0ey6H26tmWaMPq9fBck3JjB-PsrqRwZ52835gD0qeWpAJVFrdtPwAxc6036RhQYht1imZ6sbgi2vF9fSx_jYxYx8qXbI9X_Z_NWo1Ekn5QLtrZlLA71j1qoA2b1c2igaMrBk-LSxw2ePioDTWV1eLp0i4KAeB9VL50fpU4hJfi1hQTUN25P4iXGVA5vo5V1FPTEunl9zNKmfwho8MUhc_uWQQ7uV0hBjeFkxhuZ4Kbpfd3D2jtlYVLJ4o7YSzFhXupp4uHeXURklPybg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=OvVVv3hf1B6eCxHSg7ht8XfJAS5K2VKLA17zR20paG6PgKC8YvQ_a0B6w66NIazhljaxpV0ey6H26tmWaMPq9fBck3JjB-PsrqRwZ52835gD0qeWpAJVFrdtPwAxc6036RhQYht1imZ6sbgi2vF9fSx_jYxYx8qXbI9X_Z_NWo1Ekn5QLtrZlLA71j1qoA2b1c2igaMrBk-LSxw2ePioDTWV1eLp0i4KAeB9VL50fpU4hJfi1hQTUN25P4iXGVA5vo5V1FPTEunl9zNKmfwho8MUhc_uWQQ7uV0hBjeFkxhuZ4Kbpfd3D2jtlYVLJ4o7YSzFhXupp4uHeXURklPybg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68446" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68445">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⏺
وزارت نفت کویت:
خسارات مالی سنگین در پی حمله‌ به یک تأسیسات نفتی‌مان رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68445" target="_blank">📅 13:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68443">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=FvQRRlRup3ixn3ZSLIKLyRjAUeJvsA6wpY-Ek1j3xioT_k324Iipg4zHjcIhJuog95RlVf-bupGeT71VxftaqYW88Y3UfSRI14sUvjj1G-43A4YLlF76EgZEFmlvyvNd6zkID-asP7XsGsb2fYeoeX3gOu3fgWV1at0KpIK7VK6crX2tfJd8ThsrjNNWiDFLLBnF89rCf-VnZQ9lpNxrgVYrdWHlBc0nYyqihxj58Nqnk_tny45fHwTHU3YxusRj7luuSZKm9p6FqBTcwQDUgphje19LBwIp8IGYSi1tF2jdXs7G3wqf8ulEE3vFm3SXWAkc7dpI8eCStlTkJpQYHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=FvQRRlRup3ixn3ZSLIKLyRjAUeJvsA6wpY-Ek1j3xioT_k324Iipg4zHjcIhJuog95RlVf-bupGeT71VxftaqYW88Y3UfSRI14sUvjj1G-43A4YLlF76EgZEFmlvyvNd6zkID-asP7XsGsb2fYeoeX3gOu3fgWV1at0KpIK7VK6crX2tfJd8ThsrjNNWiDFLLBnF89rCf-VnZQ9lpNxrgVYrdWHlBc0nYyqihxj58Nqnk_tny45fHwTHU3YxusRj7luuSZKm9p6FqBTcwQDUgphje19LBwIp8IGYSi1tF2jdXs7G3wqf8ulEE3vFm3SXWAkc7dpI8eCStlTkJpQYHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موج جدید حملات موشکی و پهبادی سپاه پاسداران به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68443" target="_blank">📅 13:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68442">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=od5U1muKa6firAeubS5ZNxb6bqJv_J7xuBd1PE8bjR8s4j1g1vC9SDrIV_QJ8Xd84osfgAijWg_YTp5RPaXxkAVN4k14rvgf99i4sGPIgh0k7wRfHrWjGT7eX1abzHTB3PUz_sG4tle4QZx6I3YRS5DuFW1uzoONARFDwR-N5ZcPXW19bzeE-vdhMiOcZbwpvvWanvjraG7lh083M-ErQomfk6z9_rPLUL-9TCqi08-7Le0_-bYabqJ31rOrgHJd57xJQo-WVA2fBB3TczNoa2FojkPZ35ivmZmxvZOQsbQFnwrXOYfpn7X3eRRNHBEqaXnW6UrrTbHmtpqbdS5vlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=od5U1muKa6firAeubS5ZNxb6bqJv_J7xuBd1PE8bjR8s4j1g1vC9SDrIV_QJ8Xd84osfgAijWg_YTp5RPaXxkAVN4k14rvgf99i4sGPIgh0k7wRfHrWjGT7eX1abzHTB3PUz_sG4tle4QZx6I3YRS5DuFW1uzoONARFDwR-N5ZcPXW19bzeE-vdhMiOcZbwpvvWanvjraG7lh083M-ErQomfk6z9_rPLUL-9TCqi08-7Le0_-bYabqJ31rOrgHJd57xJQo-WVA2fBB3TczNoa2FojkPZ35ivmZmxvZOQsbQFnwrXOYfpn7X3eRRNHBEqaXnW6UrrTbHmtpqbdS5vlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپهبد خلبان نادر جهانبانی؛ میخواهم شاهد پرواز گلوله ها باشم
🫡
نادر جهانبانی (۲۷ فروردین ۱۳۰۷ – ۲۲ اسفند ۱۳۵۷) سپهبد خلبان نیروی هوایی شاهنشاهی ایران و معاون فرماندهی معروف به ژنرال چشم‌آبی بود.
وی بنیان‌گذار و سرپرست تیم آکروجت تاج طلایی است. از او به عنوان یکی از بهترین و برجسته‌ترین خلبانان عصر خود نام می‌برند.
نادر جهانبانی دانش‌آموختهٔ دانشگاه خلبانی نیروی هوایی روسیه و آموزش‌دیدهٔ دوره‌های خلبانی جنگنده‌های جت از آلمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68442" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68438">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=SGtZMZtk41fCG2cKUXyK02t4wwcttYQWfHEdb9A8KngXbe-HUk5Y9abHjgw9Ni2ngg-MRNbVlCHeUMFx4C7ByOo789lRJX9TERbajvq4r9yDPTPGNQIsBXnJZOl_td-TTBZwFo3yT9I1GKAm2Hvrtx-4v9plKwcYvVJBBoMjsKDk1Zn7ki4TDc4lMVDFxzjq7WUnNgZm2JyWb9A3e7dWbq5cQqJB2hgZfFeFzBJO6ET8IMaguiOofWUIm_LC-BUIXBdA_5MpIMw1K0KTfWVwd_ljA8rjNo7dPUF69g6esUJ2X5A0uR1FHogKGydxGmrXMr96swrzrjPkCR1ZFOwYfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=SGtZMZtk41fCG2cKUXyK02t4wwcttYQWfHEdb9A8KngXbe-HUk5Y9abHjgw9Ni2ngg-MRNbVlCHeUMFx4C7ByOo789lRJX9TERbajvq4r9yDPTPGNQIsBXnJZOl_td-TTBZwFo3yT9I1GKAm2Hvrtx-4v9plKwcYvVJBBoMjsKDk1Zn7ki4TDc4lMVDFxzjq7WUnNgZm2JyWb9A3e7dWbq5cQqJB2hgZfFeFzBJO6ET8IMaguiOofWUIm_LC-BUIXBdA_5MpIMw1K0KTfWVwd_ljA8rjNo7dPUF69g6esUJ2X5A0uR1FHogKGydxGmrXMr96swrzrjPkCR1ZFOwYfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
🇷🇺
حجم آتش‌سوزی در مسکو پایتخت روسیه بعد از حملات پهبادی اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68438" target="_blank">📅 13:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68437">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=LngJbUIpNmosc3JrLZ185WGMOUMQUFzNr7zVfdKLgIBXLPFqhEuzCidfoS9a3f_wdzi9n-EeT3IZOxDSGAZkrp5WmvbYBbWPUfeGWj1wFRfXsyvbr4_z4lfzpBVu1CXq_5pRrfFCjtfOGdksVqlFNAQfbkm7KUOn2zevtAuKDpZgsJpptgAcDS_HY8owmRwlliPIyfQJd6BKM41V4a9Gv6cswQCsx0GkvIrTi6I71fUkO7xc_KwVH5nfuJE4kakobunneBNlxQBCREh1HlIazgL1n3kt7qE0o6PI9CAb6t7NR1LjZpyb6jgIOStjiB4FLi_cRbQyrGlWPMBDZYHsVV314iuLg3Psk-fdx8RVmbbznORSJwNNa6B04JnEAiIGAqOEU6gTB9e3xvYFxuA8IyPd1GN-Y1hu46d66MTjUc6QFU3YYSWnZGiymXGVHyXSZSETOhZqu0f304kUZF7LUHf2zIkkrTYsUbRuXDMQ7Sjd2qOpjXQl9ubxCuWTndeofkDx46hWblBGiRROfq1ieo0y07e3fgfX9bx_A6k8HQgZfr2hPRoABSrZa4YsTfWyB0sUvcvugemeLQmAOJR36mox9BDwTACUhzKqw8du7ooKs9-MhNefRt-8Mz17cwKAy_pQmEbe5nJEUR2wnGXxVstTnPHOpVkoThD45N4TyNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=LngJbUIpNmosc3JrLZ185WGMOUMQUFzNr7zVfdKLgIBXLPFqhEuzCidfoS9a3f_wdzi9n-EeT3IZOxDSGAZkrp5WmvbYBbWPUfeGWj1wFRfXsyvbr4_z4lfzpBVu1CXq_5pRrfFCjtfOGdksVqlFNAQfbkm7KUOn2zevtAuKDpZgsJpptgAcDS_HY8owmRwlliPIyfQJd6BKM41V4a9Gv6cswQCsx0GkvIrTi6I71fUkO7xc_KwVH5nfuJE4kakobunneBNlxQBCREh1HlIazgL1n3kt7qE0o6PI9CAb6t7NR1LjZpyb6jgIOStjiB4FLi_cRbQyrGlWPMBDZYHsVV314iuLg3Psk-fdx8RVmbbznORSJwNNa6B04JnEAiIGAqOEU6gTB9e3xvYFxuA8IyPd1GN-Y1hu46d66MTjUc6QFU3YYSWnZGiymXGVHyXSZSETOhZqu0f304kUZF7LUHf2zIkkrTYsUbRuXDMQ7Sjd2qOpjXQl9ubxCuWTndeofkDx46hWblBGiRROfq1ieo0y07e3fgfX9bx_A6k8HQgZfr2hPRoABSrZa4YsTfWyB0sUvcvugemeLQmAOJR36mox9BDwTACUhzKqw8du7ooKs9-MhNefRt-8Mz17cwKAy_pQmEbe5nJEUR2wnGXxVstTnPHOpVkoThD45N4TyNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حاضری به عنوان یه جان‌فدا، بخاطر مملکتت، بخاطرآب و خاکت بری بجنگی و از مملکتت دفاع کنی؟
🇮🇷
جان‌فدا : آره، من بخاطر مملکتم جان میدم.
🎙
خب الان بیاین امضا و اثر انگشت بزنیم که بریم خط مقدم جنگ.
🇮🇷
جان‌فدا : من بخاطر مملکتم جان میدم، ولی الان کار دارم، شما برید من بعداً میام.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68437" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68427">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sydi0fcYre-5sM8dg6Ihq0YGRwMhCP2phZCeOqkbZqBUFhI1uWf7LYjvQjUV-7aPWmrEz42mxZgUmYYdMP5rNM4aj-NmYbdMOjxmo1OtpOxBmALa_Qi-cY7GtD4v1mX4zORbLMfqXQqAJzcPdd9nyv-gAuJu8z-slqgngQWE297exs1Sex1JyVVbCaGsEy-bN6JGcdjbsdBJqcXY_guzo94c4Tcq3HzSqTn5g_KY95ybTX_fsigNqRXxfOorc-ZaFjGDr-qQop2bDONwOzfFJH-a5rLeYBUzeSLJBtT9DC2-aq3Mgib5Yclq9M-2_1L5H0XrUvVta9eKAme8LInZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bt73masxI8kqoyMfP9_2qHShnWblk4z213_7Qv5mZ6s9kdL9U0FjS7uNwfUgH9SIDMGLPq76Tx5V4MJ6iOjFQHiu1pCQ1IGo_qGEQCMJjch3vj4gz1_5lndkXaVTchZgHHtOcCrf8p5agDmevFkxgtnpnNaydlX7OqdRelBwNaE5yA2g9G_vtUbBbmV8y9x7M3F6GvA_OOW-JCtWTcyZKuj-i3HTU78y1kBIn-Keh1u77C6xgVknuBLKYi1z95wUoHcskB5M9Dcj2YPQMmglLrIk7syCAJuqUjviyGTwiuxSEz4Q0-c5uY8Bvfqq2loM-QXit7eSz18cm4W5_QTKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLGMKviCHRy_LBiDH8jVOtOGDZ3YZAEzzGdXsADUIp7r4gSpJBGTmIPTah_Esz3vWlOCDIjGFfSJE9Sw71M_P7I7xpEMx5FtdANFN_ihSg50INRD5zMvOfJct_MatF6BV0tt8cW0J_6f3SPpDKs0PzfEnASDvoRx4YUPCKrmTx2FLsHFUcqz2HMmU4N9CN6HGjRjpnKeYABGmmn_ZHuT1NRX3PQ16xWpbMhlAgv2YaremCckunGBrj-xq3v_nsWjr8I0oGSsb1awhaAT6QmASx4YCeJ1PPv1Zl1trmEbVSGvozAZuRMwt6JbnI5z3GPtmqHUuoPJt1S_kHaSl3foOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjYcBK9VyRHwQJgmmtqtBhaZtAEe7Tl_JE0yeTDJGo2CjaLi4jsnl151Yp6X8yW54dVdfMC33R16IC1TnPwMAr8GBmB1mHXZvlhAnbC6JJO9Ahv1o9jf_3PY_NUBlx0Mk279JJI-0kZpGQhw-WI5WZm-1_6BbWljnVConH5OLsjRDDblRH4lJu8f5ScPGuiQzBxlQBCNbjy1A5wFs44BEA9VRYhVJKJFZx1vpgQWjXK3Mu0aLRsab_zd7uvOQFNrrbUPXIv3yg2aqyVgduLHB8twye-5R98APwt1MOtv79aKiUzeKMbWYf-1T-MNZPs4nv0d8bvPhKMDnHBXP4DZ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDTxHEKfbvkHAgzSnu25AAfmi4QSuMk5MFlyCNoG4yzD4NaVf7FoLHpkp0NDR5zUfCPv_uiIDTrz4D8RO0WEgq7IZytpC5xkhbdDsGlLvGsu3U4op2gAB6bzuVlnNCZe9dvOvtBUYBJxHRzE5vVfw4L5HUIIXVt0ZQg4FzDpKSeQJs_lJ2Ee_1A9iAPBSZwkVVYn3vpkDOXWs0bPkZ6LOTZG2VUWYqeSnzpZIL2YUHVAgoEOlwWtu_Z7TocH1URigKsDtzOvzFcy9ef1zM4WbvT7WPOmWZK72OyVKHCfVaNQSyoNsEphE2DuLsK5FjnOzznJR7ZrZvbpKuMepMrybA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Av4pDp46dzWUgE0fVuJUENjEgf3aUDfMDCS0dxM0dDdaPglN-EPPM1aGvhkxenwMLQR-IfbbXQqV6PohkzBDTtt4Nl-bwU1_1frdy5w4Gcu7f5ig3lX2HVVhvCedt0AXX_UtzniORwVgLSl5jNbtDzWlt3kexlLsXy4tAXLXwyDRgNlT-F5zWfP3O5VRc9hbaFvzGHxkqS8rxMlavzN7DkAXbCF9qX6mYpqOOdLfiLJK8YEOF5U8SalfotZbUM3cWGKedFxqOs6ZUa-zOELhpaDNBpx_9jYoDE2QgbDnm01f9ePqrIckcRD-1nvi7sImrnw_4xfakd0k5mCuYUFYZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rs3h5gu8lVAX9-rPdTlOetYYsJN1EQYlwik4d-rkX7x8b7IMs_0oyMtt99e5pnbifGsTRl5rkes5mNICD-PBrm1K99IwiVaueLkR6ev1Eg3GtQbKpSDk2g4UUEuzQH_-BWR2I099_0PMLshv8C8CaFSsXkF5oP1kAlToBpJm7-ZOfmJp4V8tUOwc7t32lS9Q7whfmexTv8q5ZibLaXQOS4rLEq0SoAEVX-tEsRmv6U6kwtqCFLCBMw6uwXPuvNyRYHhA6Ouj-sx8hArLfbYk7lvGh4TZng8dd5-LwOV6TdWmKy8vTwIY_xRsGS7inxGGzSOL8tVjh_Ir7cayjmD3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-Sz_YMHKVxL8rDpwvQg9L5LCkpnAXn8qpIElScjfZrkyU7Vvelf5qHYHTEJkLfUhmNG7I0Dld2TKD0nNca0ga6BqFisjYGkD2oQrG8N5Vh19NHnSr-bo3YtbyxCSqFExfZvfVmr7evfhFuWbhFy7x0YktfA0GbDKmsWQCb-4KKFNKBecNS8UTB6EW4bkV2h5-fZ66oVDmW4PvDpzWRQTTLFtiH3DOZCg6a1SNkyBegXsBb5TPFgB4g3STLXHYqL98Z1aNSYQCYEiopAgTvRg_wjObtFHi5PKXrlnSJ2_ktWQAWyk0rmArPi7gtY3XVzLyUSF91Tx6H-oipIBQVFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EgOfsNOnQTgy_0fWzuoqjjoqGw_3AyGJZmICnTQGOR4c7mwrL-56Fqr8zuNJKPH9n5RVFVn7vyu85w12nsNJY2xIhLtVnir37mYf5o72u6o3tOq-dnz2POc7g0n08ybvAMHqcDYo7bJAaG5k82AHOx5uvS_1sQNgZNQV5XygAFDUueWdqpd0Yn3rljhOoqX3jACLT5zwaSpNhynhVTymGG3eGilycIf3jYF4TwEDFkC23PaTnPeXh8vuTOqPm_N42tLudsjqbHyEiFrGaXDyR0Y7G66QSEQJUpKbaBZzTapusfMDOI51GDAJKaOx6xBST7FfhtpldkDyzHYMR8KQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANaN7svm-eL5DIdictBDCoMAVUH7AiiVIw3pIFsjTuWZGTnQqmzJ7ZPYYtJUN8YSKzcLyu_zsMl8x0bkYQfKncCwu7JgWAlucHtdUqNm9lyzCY7Xmjzo4o2YcaaE8ouJ5KPxsLmXOKSXh7BRxxROnZRSAee9KFLwqquB_1q88N0bmNtHAwjE0m1aYffEqlJKp31nSPeihWLN3t40zGfAUB6fCxgckEXySSBnXbgXSLCZTwRtC8lB9uXdULaEK2XSVltF48AehTMIwSPQliTILOoGGLJ6ZbjMMhEGnuDMemz3LDkaeCIEZuTXoItsr9gObb8Rj-Aje0wmWX1DUpHtRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آب‌شیرین‌كن  بونجی جاسك تخریب شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68427" target="_blank">📅 12:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68426">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=OVSGevxgdD5JnxL8dj-oqzdDra3YVC1Ru5zoVyARTjOIVEMan3-O_YdjC5EW0RklXioweiOiOJpWatu02gJ7iThY0ldCQ1RPKCHlcLdLAnUW4BsmnMk5jypDCTF5gx74NJfKYSWJWLNkW6pUmz14hnPdtE6cM_12fwwikRunzhSWMS8qK--9Z0EqBwNrqAtK_HEM0bz0SwXjzGrqE11WPdTu412zs6M3p5EHf4UJHZ-GoJDoJZkicnA8Bn-M5_3m5A2kSzfJocPG-cB9UCZkA5UQZ44M_I-ysmViK_iu58YlcZsbWUcRjJfhEOoR7FXyc3qhmXnDawQ8Mh0KsHb3Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=OVSGevxgdD5JnxL8dj-oqzdDra3YVC1Ru5zoVyARTjOIVEMan3-O_YdjC5EW0RklXioweiOiOJpWatu02gJ7iThY0ldCQ1RPKCHlcLdLAnUW4BsmnMk5jypDCTF5gx74NJfKYSWJWLNkW6pUmz14hnPdtE6cM_12fwwikRunzhSWMS8qK--9Z0EqBwNrqAtK_HEM0bz0SwXjzGrqE11WPdTu412zs6M3p5EHf4UJHZ-GoJDoJZkicnA8Bn-M5_3m5A2kSzfJocPG-cB9UCZkA5UQZ44M_I-ysmViK_iu58YlcZsbWUcRjJfhEOoR7FXyc3qhmXnDawQ8Mh0KsHb3Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تونل گلوگاه، در حملات شب گذشته آمریکا آسیب جدی دید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68426" target="_blank">📅 11:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68425">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68425" target="_blank">📅 11:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68424">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IetbLJAv1nVwUBasVXpEcn2jfs_XNwpkKXb_JMpF3XE3uWQkpsefmpST0SQ10j5DE0EJK7Y1MyUQi0c3ualuFL0qPj8fRmhPkaZcWZHmECASpd8iUf4PNHb9eZ_PnuP478z2JR8H_Clhc8yIcJAvmHY-6H5yAj7OcoX_SYjR-yhUri6apkZDhBTdP86Aicw0pyycsldyUabd82KuIWA1XLpWU0ZGZk7Gzyn6wnwtERUooA86yKqKvQsqEzoN49vOQnxWon5nWSxzBcmDOEdgGAY9mqlqCsmmK0Fcylm7prERNwM0Y7dXJg7QM0iAiORFEcR9Vt1a8hZ8z6oc7uLeHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است که دو نفت‌کش در تنگه هرمز، پس از برخورد با مین در این آبراه بین‌المللی، منفجر شده‌اند.
✔️
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران، نادرست است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68424" target="_blank">📅 10:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68423">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=rAIkEcjuq86c4GyEVf9nTrAVXZFdBTUFzVAYRxE3SbSRe4GL5TXPnPjfq9DSJg47m0KLIw2GAVhfwobAudvAZT6jmEtU7zbep_IWvAW1d-jaGFtPD01GzmR9LI1Od52nTbBs1UE-uknHV3p6C--AXfNyNwPX6X3ypmDXMG283uhtfB5bALxy-K0TcZCZkvK29ChmUr1c_2EE4WuxiSx4d7xVvdwj0L1P3oyJEP7J71v5MaM69duHmyehskcZqxCH8iN8XIlqvY2D4739ZKHerFMBmQ8a7P9eNxR5LKHNnl5-FhoclOfW_gIEeqiB9e0oTrF_VFqUG6peOsfswJWBdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=rAIkEcjuq86c4GyEVf9nTrAVXZFdBTUFzVAYRxE3SbSRe4GL5TXPnPjfq9DSJg47m0KLIw2GAVhfwobAudvAZT6jmEtU7zbep_IWvAW1d-jaGFtPD01GzmR9LI1Od52nTbBs1UE-uknHV3p6C--AXfNyNwPX6X3ypmDXMG283uhtfB5bALxy-K0TcZCZkvK29ChmUr1c_2EE4WuxiSx4d7xVvdwj0L1P3oyJEP7J71v5MaM69duHmyehskcZqxCH8iN8XIlqvY2D4739ZKHerFMBmQ8a7P9eNxR5LKHNnl5-FhoclOfW_gIEeqiB9e0oTrF_VFqUG6peOsfswJWBdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68423" target="_blank">📅 10:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68422">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ34dW0gdkzRgRJ2JtnNZ1Cj62bp_tsrEJTDKjUN-C0FqvgNfouBMN5TuZ3ayDyK3zGcPb6P2cQVlqMXiFQ-L-MeBspQ9F5yhVv84jqN2k1vNR_fcRJmahj5wLmdvgII-ymTnup4WtddIjh0s6ow0jOH1cxQUySUn6s9lIxVWK4dumXIpZp6UekaKnQJC8aXdJtqDTTp8UbfsyPVCsmA37WQQpbstwHY6oymAWSA2oSb2IhPlYDNqKvL5ZOhiY8VyHC1goDhhEkVLl-6mIGPV9eoeqDa8pmpTaQNe8ZqVOMX-wCm3o63qunwrUwrfJw-IA2_k6SqqfPxv4pOQC4x1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اکسیوس:سه مقام آمریکایی و اسرائیلی اعلام کردند که دولت ترامپ به اسرائیل اطلاع داده است که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند هواپیمای سوخت‌رسان دیگر به این کشور اعزام می‌کند.
پس از آنکه روز سه‌شنبه چندین طرح نظامی جدید در جلسه «اتاق وضعیت» (Situation Room) به رئیس‌جمهور ترامپ ارائه شد، او در حال بررسی یک عملیات تهاجمی گسترده علیه ایران است؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
از جمله گزینه‌های در دست بررسی می‌توان به:
⏺
بمباران تأسیسات زیرساختی ایران مانند نیروگاه‌های برق،
⏺
انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف مدفون کردن عمیق‌تر اورانیوم غنی‌شده این کشور، و بمباران تأسیسات زیرزمینی «کوه پیک‌اکس» (Pickaxe Mountain) اشاره کرد که گمان می‌رود مرکزی در حال ساخت باشد.
ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد مایل است با تشدید درگیری و وارد کردن خساراتی سنگین، حکومت ایران را وادار به بازگشایی تنگه هرمز و پذیرش شرایط هسته‌ای ترامپ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68422" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68421">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68421" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68420">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSdWaiLxIDzCs_QRgQYxI7l7_GHQuKNJL4LFOQ-tQ_y-wpALE4ux6t1hKfgmjvBFFRnFgKR91yyHWru0RJA2TaCkgoZSqnPR4lsqHTr3f9760mSlqbOJFOWAes0qDgfSjG-Sp87W12CkQD0CC10HpB4KK8PYTnNnZ8URPVZD_JJvESyJGJRFJQXC3jGSic_bVvcqtJcGg_dHiSMYKYgnDH48lv8V_h8jMfAy5c7X6jhexukntcNB7-omkKav6NDVdwacGVJat3uBd6PKjQtNEMVf3cZ5Eicx_3i3uio3Kl8zLjFhS6VAQfEq16XyrH4LtgZpuxvEg__U1QFcZaviSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68420" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68419">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در جزیره لارک
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68419" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68418">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvzt2u4m1dx02IwT42iRq-IAoxsTsuLBEdSSMNsyywboj8C5hqX7yoIUwx4wnIrgc-2pnXyI4oLZ1YJwQWaympNDWMfOsbSXrtELlHOhs7emHe-e_S4VCD197PjKXvBN-UuhUGiSibseeBe_BjzQQ6VF9S4LPYvRal9sTfgOrEDgdOiEJ5AIOjwdemZTjmEmFLJRmByAyXm2tTKtp0y6TskQIsqt0RnvTtaosdFxiOOMmxJ0DKF5Qkdb-kFe5nEyPDyf9w8v31aF3WcM1gIuq19a2mMTK1Awfz-s99n4MpbPBBTRO4DLW3OKGCMz-roClEPcFAvkVBjWW-IpNaMcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۳ نفر در اثر حمله به پل بندرعباس_رودان کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68418" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68417">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:    ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.   اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68417" target="_blank">📅 02:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68416">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvplStLDzhI2U7HkA5trufOJqrzC-IxdWVAzpsM4WPk9em1PdAl_VS6eJPMvz4AOCNh60f7FzUNbT2IlE5w9l2YgzhXDnV7sokCPaSQ0YqXZXOIwyqt9t40NLLEYIQwlI8aBaCSkgNiD3Q94mQXSt9-hC-1GgWUrbKig2bEtnu65OIU01VhEfeEYd8-1CUgjGGGPR6OYYw8ousqzRGm-jXcS0ulqHvqbzyrw_iWq1YBF6DEBxapajL8D6FaUZaThe25glWT3WyD87CrGEv3eSFGtioJh8n23F1cJStEn2j90JXs2XyvGNcRZNrA940CesOmbvn2h4HJypQkL9T_vbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:
ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68416" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68415">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.  حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68415" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68414">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
فارس به نقل از منابع عربی:
حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68414" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68413">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=eQ-wEw3QcG4ne1W3IiH5Fm4vfYlKvcOc2tlsFTQ-dNWdN94JcRq-8Breoe4cfMt7ya9y5kWv1eB9RfIp6VO0VsIwo0zAAWZVUgG2rxkv2VJ1FLSdP-9ufDfKKf6BkxqtK7V9aseIw3xyK-o9yXZnARgJmkv9SoFtVmfuEZGIwrOg__2PwTcUxWexRZ7ZIKhin3PjaeRaMW2L_P3hjHqfYydL4Dk5iVAFiaM2ZFBGJvbhotheze1y5DuU7zHBVdjKVJNvet7safv32C1WaIRv-IoexkWcEmZxos1H6EHIIciJllyctRkNb9CyyzYFk07t4fhp5ylK52XjSj4Noh0_wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=eQ-wEw3QcG4ne1W3IiH5Fm4vfYlKvcOc2tlsFTQ-dNWdN94JcRq-8Breoe4cfMt7ya9y5kWv1eB9RfIp6VO0VsIwo0zAAWZVUgG2rxkv2VJ1FLSdP-9ufDfKKf6BkxqtK7V9aseIw3xyK-o9yXZnARgJmkv9SoFtVmfuEZGIwrOg__2PwTcUxWexRZ7ZIKhin3PjaeRaMW2L_P3hjHqfYydL4Dk5iVAFiaM2ZFBGJvbhotheze1y5DuU7zHBVdjKVJNvet7safv32C1WaIRv-IoexkWcEmZxos1H6EHIIciJllyctRkNb9CyyzYFk07t4fhp5ylK52XjSj4Noh0_wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پل مسیر بندرعباس رودان
بعد از ایست بازرسی چغازردی حوالی روستای سرزه پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68413" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68412">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMzKkbpm9nDYNm80TUwqLSLk5uGGnBHRcBQA2x-lkUA4huh4aXGKmlePKMkt0CQIfQ_6dBGLU5m4GXDV1ckhxa7sszidHmZnmkpUQuHOx0fahlTehVtY3aQahGMGvWHCDyLWjkjuLs7a5zp7-3Ngttd9-c4YXkygWrkixsks0Slb9ImVWLs_YJLQ8yiYVjzeu6jxTplwuqrbWkvMobzGq2Dh1BG3anvrUZ_yDKwqtMZ1pjLBUM16NmGy7RGPxgB6Iq61PNmJo5fYLEAY0LmrZ9OgzCNvNQ_PZMJ2YQBSFu8VbMMdU04auLNTtkJ27-G8DfIJM5Wg5QH3vmsykQvHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیرهای هشدار در شهر الخرج، واقع در عربستان سعودی، به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68412" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
