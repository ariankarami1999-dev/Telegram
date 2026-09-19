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
<img src="https://cdn4.telesco.pe/file/I_6TyvfvTYFRLjeO_IAeJD6kmXInTEaLYe3gWzxJNfjeypcHlgEuszMclycf9z6FXpW5aDsll8OUUXAcvqAGNpS6ushpfhkOeKBEHMiK-0Ma86eQXDmtF3W-Dw0ZI0ZnSw6S4JR9jJkrjcEQvA9mB0cZLif1TcFF5Z2lAXI-KzfVqz7UBrmLersLyhRrsT7AlYrtdgKRBeQklk5On_Q6plgtXDaoX9CjhBkgvIpXK4yjabyBkHLvgjcMQ54Vkx8xvwFLvDVelLJCF_pzYpV6sYFPvkyQwJGTS8_Z-0BTXkG0quF8qmfrnFE_AurGYbGAhpByc-gamQ_pSy1n5mZb-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 485K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 05:53:03</div>
<hr>

<div class="tg-post" id="msg-30037">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=FRaXTZF80vi6sUqFqsil-_uSLEM2iwPY0klFe23UF3UH5n9IpUX2LCBNpK0j1JvKjBaTUog1YZqCTj2jNms8yHXrJQx8u_Ak_MRkHFeYXktPtXrzfsh8OXL9UGnGpBAVRx4jYRLTsHfdPHANH3dqY3aUIT3C2q_PmJ94EYSGM5c4eSTFphtp_0uRVTj6Khk9DCpbarcIuv2RUUbQO6uTm1eFbI2ua1KHoyab7SQ9_syaQ252q5lds5A0niumVzOT8rrNXVCKdstrC_eGuMeuywDKvqPkIZaNffvAx3vBJFDeTsdGwdDRkDzZWh2LudN82tnFHcZthRo6nvCZG_v2fKR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=FRaXTZF80vi6sUqFqsil-_uSLEM2iwPY0klFe23UF3UH5n9IpUX2LCBNpK0j1JvKjBaTUog1YZqCTj2jNms8yHXrJQx8u_Ak_MRkHFeYXktPtXrzfsh8OXL9UGnGpBAVRx4jYRLTsHfdPHANH3dqY3aUIT3C2q_PmJ94EYSGM5c4eSTFphtp_0uRVTj6Khk9DCpbarcIuv2RUUbQO6uTm1eFbI2ua1KHoyab7SQ9_syaQ252q5lds5A0niumVzOT8rrNXVCKdstrC_eGuMeuywDKvqPkIZaNffvAx3vBJFDeTsdGwdDRkDzZWh2LudN82tnFHcZthRo6nvCZG_v2fKR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌مهدی‌مهدوی‌کیااسطوره فوتبال ایران و باشگاه‌پرسپولیس‌درباره‌پیشنهاد 2.5 میلیون دلاری باشگاه چینی داریان که به آن پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/30037" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30036">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIFBKtHTRDs7aU_1KvoqQSHF1cacWu8hNvj_Ez7UcKXU3Tr_3rZ7NprCr6hxGoFwnMw728UBI16-b8QDde_7d5b8Ktq-XUtLnsQ9fWHt0tynxnC2jz-yrF_Ift4-tTw5IDBirpNRYFzJTf8LTdie-7WmXKhd5yeSdPcWJs3ByTB2gU2XdYeYaOTnwP2eFE5wbqfGQRkerY4Hdh0RvCToF-CGoqmNTW65Y9zTZYd8orzvmsQGrr5AcB_OC6mUwCisAn4ZhBrylyn6khvvcgVLNjVYPpfxXR21VWVlrsgtFFOsGGXfJCeVTJA3l0NhowCF7x0KRuJV27GNJpErWsEGdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل‌تمام‌عیار یاران دیبالا vs لائوتارو مارتینز برای صدرنشینی در رقابت های سری‌آ و مصاف تماشایی شاگردان فلیک با سویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/30036" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30035">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJoSAL7CgUIDvFGkkEZpKgCyoB36xI9zqzvn07ESZbMXAFY437U8L_ZjZpzt8g1Wyod788l8H0vXBLb5L7ZA8izwSHiCeXAtuBJBxZA-7SnHuNaSLaxg07zFhfnIQT7kbdemhhGY9qNcua_YrMmA7b4gTTeYBfgV76BYESI9zMWA6yJj1ht8jyDYewczJx4VT3g1g13Og2i04_m9KRw22PKHmtH0jFNVXifzBiaQk-BHRiMjgGS3BH-vIAVfvU-jiqhC4kD9riOoJwhh_d9y17iFHCoq-5awVNJXEK9u69PtUGIe9Q9N3bZQEECLjpwXTkFUa7QuuNu9NfaIbSjMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از نمایش ناامیدکننده یاران ژابی تاجشنواره گل‌مونیخی‌ها درشب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/30035" target="_blank">📅 00:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30034">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMKf2O9mb3S5QjPlA7ww8Z76BGmfj6eXVW0FpDK2KgdcQ0eJsE0iI1dVkkl8M0HRjvvnrQEzZTefiGLADl2oHuJxR96bsCAsgZwmikXYik6aljdAYpC1NPi7V--uMi0C_eI6a2yuE_AQP19zc-ppA82gxbYsIz-u7VBjw_2EkB26vfoTDiRlj7sBvPHkMvWI9YUhILTNppwKnLlKdXgT0PfMqn0McxwFCKQ38WZS1IRQlvl47z1k2fPmwYhNI2a1caIZ4MoLIimeeP-Z8xr85-IdZpEvteF6AqdL78JIVuO1mDF631ywsfLaC4FtZLgcV85wM5oJ5gw_xz3TiIJK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💎
🤩
روزهیجان کازینوبا
🤩
🤩
🤩
بانس
شنبه،دوشنبه،چهارشنبه وجمعه
🔔
ویژه پروایدر Playson
🎮
بیش از هزاران بازی محبوب اسلات
🆕
متدهای پرداختی ریالی و دلاری اتوماتیک
💵
🤩
🤩
🤩
بانس‌جبران‌خسارت بازی‌های کازینو
🧬
ورود به دنیای کازینو با هدیه‌ای ویژه
همین حالا ثبت‌ نام کنید و برای واریز اول از بانس خوش‌آمدگویی‌کازینویی‌تاسقف
🤩
🤩
🤩
میلیون ریال بهره‌مندشوید
🔝
فرصت‌های جذاب درانتظار شماست
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
📱
کانال اخباروهدایا
🌟
p27
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/30034" target="_blank">📅 00:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30033">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
#تکمیلی؛بهداد اقبالی مالک‌جدیدتیم چلسی: از کادرفنی‌حمایت‌کامل‌میکنم و هرچقدر نیاز باشد برای این‌تیم هزینه‌خواهم کرد تا به قهرمانی لیگ جزیره و لیگ‌ قهرمانان‌ برسیم. به هواداران قول میدم چلسی رو درآینده‌نزدیک به جایگاه‌اصلی‌اش برمیگردونیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/30033" target="_blank">📅 00:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30032">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUTi5mX67TmHAhdSa8VRDnECWQniUkGU11hY8us44zKkBFjAqNQSMH4EfkbqKMWIIcfbOL38zqKzd3uNy5qOY10EWjHs0xM4DuvT_V3J0wjlrNSN3IT7gTJxXQiqzS77yL6OzK-S5MYm8a63PiuOi-qk5mfttrd7ru-aQEiu0lTJ2ksIdSZaqE1HyUTAuM5IM_GC16Fsi9-vIRoeS0Nj3hDIzW60N7FwdPHFkzqJyBO6sdOXuZErXxNxuxwaugN4YvKQsczN4RJM1DmfLfu-I-MxiRsUavCQ2QOQuGUPEJvaUczG0BRmrHBxWGKPXF1Zxcn8bC9lKNClBxmDsYQjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: دوس دارم در چمپیونز لیگ به رئال مادرید بخوریم. برای‌الکلاسیکو 3 آبان بی نهایت انگیزه داریم و میخوایم یه نتیجه تاریخی رقم بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/30032" target="_blank">📅 00:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30031">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/30031" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30030">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr3Vkaj6wMggIBRphdxrOXBGo0ygUHnRQCv60AlgJUcLteWWe6Eu18I-niG8lUeyJgnpB-1PsBMEcmFtw5UCDfyIy4Y8i9RM3PjO_bq3vlJr69P3_wbjBV3yh0I6sZH3Q0-6HAn_35stO1jZr75EKn-wxpnOylRHOR5R4lSLH8x9V87dkpCZwIViKYYgRqDiGtNrszoiUpCcUn3RZbrcbPuVRxYIAhNSMZt5l_b3zAzJgp98TAYduG86IQriDfXgugX0OFqIjkHBOn71aWopvD3HeT0veEaiimNk3mbDvfAs0SUJf2lVAZNuD9dq09q7z6bBDU9iizL5sfxSf7C8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهم‌یک‌امتیازی‌یحیی و علیمنصور از هفته هشتم لیگ‌برتر عراق: دهوک‌مقابل المینا به تساوی یک بر یک رسید. الطلبه هم با الجولان 2ـ2 مساوی کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/30030" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30029">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY3yhPGSOuYqPbSll4_o8XNtzbg9od_eROi5c1YKkPwmVABHyOk82pivbHXDrfoSO7z9xi0WFqoR5Mn_FEpKKEh7eSkGy4oUFuTactw1wWBAynHQTf9HNPDZVhfLIuz5N9IV_A4ENJ6gcJMVAN7PAa8vXdtUjyVNRxi1VzngnCgmgAJB00GH_EpJeuFneSmcqKHq-LoZo7t5eQCof4MHLHDr1Nv--zsAko4mcYvw1_SZPnC4OHbmVeBQs2jPEj_0Nv_W5e_YVvgaSF_5wPx1HgEHcx8HBMlLvZXGLkDNsrUJlMVEDrmVWzJL1slh68FsFoPeZm7c3FnF-6r2_AOfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدارهای هفته اول لیگ برتر بانوان؛ استارت پر قدرت استقلال، پرسپولیس و سپاهان با برتری قاطع مقابل حریفان در ایستگاه اول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/30029" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30028">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=BO8pDdt3oUbUPvNduNTpaJ18cOKKh2b8k6yfQn_dZcxz6GOQ8nOlNAhDkPCVIWRB5HJ_VVOgkrFDO21aKXokIKQD_f7xEvisTaztTdqkfukTcXRvFCXJfQNzyjh7jR7tYWeeVAlo_0pkdPXJqfJeKC5H-P08gPy_EXv-9i8ulLNtNMA4SfQLXTy4MQqmtaHKW1RrzJtFRjW6QCaSqtyXcEQIjxcro3ghEbj9tsOD7QRUAdlBMR89Khqvc1tXBDu9wXFIa4eQZY-PgPM7CWq1mZt-A-lz2WzNE1n_8KjjboCKL0e0KoR0D5h5luGQLk3AOD8qGi8XXAqcgvOUqfU2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=BO8pDdt3oUbUPvNduNTpaJ18cOKKh2b8k6yfQn_dZcxz6GOQ8nOlNAhDkPCVIWRB5HJ_VVOgkrFDO21aKXokIKQD_f7xEvisTaztTdqkfukTcXRvFCXJfQNzyjh7jR7tYWeeVAlo_0pkdPXJqfJeKC5H-P08gPy_EXv-9i8ulLNtNMA4SfQLXTy4MQqmtaHKW1RrzJtFRjW6QCaSqtyXcEQIjxcro3ghEbj9tsOD7QRUAdlBMR89Khqvc1tXBDu9wXFIa4eQZY-PgPM7CWq1mZt-A-lz2WzNE1n_8KjjboCKL0e0KoR0D5h5luGQLk3AOD8qGi8XXAqcgvOUqfU2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نحوه وام‌ گرفتن درایران به‌اینصورته که میبینید؛ تیکه‌سنگین مهران مدیری به وام های کلان بعضی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/30028" target="_blank">📅 23:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30027">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=q2JV-5K57btPTJ5NC_ItcAcx5fc5Yg_DKPboBa_1LrS6dhfRKmEZKhq9-t1hY6gxJPCfHJC2uMxgL3EjCv_uhV3Lb9KgRUx5Fa9nhLM_8W1fPSANSDAR15rc_qMayPZvhQIz5KNsHJoC_j_lNP3of4H-qYrLKaWKgw_lcISaZVFuJQBgI09hbTqCComTGY3txOJ9OjfxZnneNMU6xQkz-gq50aekFsOQbkxT94WPK6aWpWusJ-bX5g7tkVgNqZkAQIb9Iaqt7gfwp9qbvs8EWMn2ykuIfB4NlDX5a86t3hHq9O9mvrwHfhLb9GHIKoqmDMe6Q7kmMndYBtOO9HUlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=q2JV-5K57btPTJ5NC_ItcAcx5fc5Yg_DKPboBa_1LrS6dhfRKmEZKhq9-t1hY6gxJPCfHJC2uMxgL3EjCv_uhV3Lb9KgRUx5Fa9nhLM_8W1fPSANSDAR15rc_qMayPZvhQIz5KNsHJoC_j_lNP3of4H-qYrLKaWKgw_lcISaZVFuJQBgI09hbTqCComTGY3txOJ9OjfxZnneNMU6xQkz-gq50aekFsOQbkxT94WPK6aWpWusJ-bX5g7tkVgNqZkAQIb9Iaqt7gfwp9qbvs8EWMn2ykuIfB4NlDX5a86t3hHq9O9mvrwHfhLb9GHIKoqmDMe6Q7kmMndYBtOO9HUlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو باشگاه ماخاچ قلعه روسیه از شاهکار تماشایی محمدجواد حسین‌نژاد دربازی شب گذشته؛ تکنیک‌ و آگاهی محیطی حسین‌ نژاد خیلی بالاست سریعا هم تیمی‌اش رو در موقعیت گل قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/30027" target="_blank">📅 23:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30026">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eV7aAd2uP5jYYxmO3QM1wp1q5m5U-1ZwYJSS-kPwdpEOqdmnltUTRXTYJBbuxYulveV6BuBa7qHjabW1HPEL7pcTDtOISEnj_ozVo3UI-J5sm_DHAEgM9S0pHa_Ib6sCYi00pkjdXUklj32ttHpM-ALEUh9K_t67f3XnuwpuRFqkly5Q-qtJZfsu__hjhIa2DcedURb-VlMvSu-Xh6yBsPZfmL-Ul24fxZTNgpLAhTrZ7gruns2vbeSAxavG8oUKzBTay0-jAh_bwsHZARPQBrJwotUXlDqOSzhD8VoEndNDEFfPPwGMuJmOrF4GNm6Qvz9GM4dRlkxS5TVd7HGT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بااعلام مدیربرنامه‌های داکنز نازون؛ بازگشت‌این‌بازیکن 31 ساله به جمع آبی پوشان منتفی شده و این بازیکن به مدیریت باشگاه استقلال اعلام کرده علاقه‌ای به بازگشت به لیگ برتر ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/30026" target="_blank">📅 22:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30025">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU3BG6Uu8eu_d9gH5W5nL4MJSAErKUZVodlaZVIjXZpjPyxFIr0NVAEFI82QGhY2rzZp3R3mwx-bwzzJ1NplgSYLSsBHGMJqmoV2oBHrenWue-J-rS0UZRc2euQo4XBkdFzjm9FTpIJTgPRzXhU31wV2v0MeZo1Q5nMmipdo8Rf_eeHv4Q4O0Z1earP5omW0lz95DnL3NT3OYW7JwfRwn0zSh-iZ-ZFFwx3uZxgejgG37GqT81vyVaDf_p-QMflXaeDQFK705KiXSXvE8PibBjlz9gOo2l7Z7Wwtd6yrYBro02B2f6-MZHG4CQAioZNooPA5Ds07X8eNfLednt_9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/30025" target="_blank">📅 22:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30024">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmDF-LTdqdE50ZLjzzpxKVr9GsRN5KBNzDOCnHITbU2qygY-KhiMh_nPYUkYwQaN-cuaH07BeMNh2SS4G2OtUqaJN3sr9xk2oOAxMAS-2mQizAlepuxvvB0-m7xNP_dDW0xIjaYNOyWzD9hrgBFJjj-HX8Z_JHxdipjlVYnq--1GpIrUcJEqB-4kF1eKtwFOgT_aiIgaRGALttD4sL563qzCmEgKl8tjsW70zzGjE7Pu5FTyGh1fMlTe37nPH1v9Lha4Q37lXiE4cQDKpgjyrBBhlEfl_i4sqVjg0y8bt40bn73qoUAPRF6Wq8GBcpe6uWUlj-mUrHfOgf9V7QOPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/30024" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30023">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyVJP9Tnzv3M3ksfoA00wejTXgjI06wTuF86BKBwHJ-EpF67h8dABUbxYy9COXQeCAqXsaeccfhFa6jvy8pfOYq_6XpY54fdfwPdXx-qk9PiQwMDIVC_7_0LwIWdfdFsLMXeWvObW8q4IOTefFkQwioohZynkuQcmJ-W67-LILNwqsCxHQVe8--dljGkl_6J97ueRpiE7DHLIUadXXzOzDaNZEm1a8FgLiXWMitDr1ZCLUQJOs3JAOGrwhX05biUG9mBu06Ads3UUUE-5wiGzAlxdgOsnLIEoifKFww0rvOe25UU-ScODr5ljJOZRFTPVW5KcbyMcFpdgHdJK75BvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی تیم ملی پرتغال؛ کریس رونالدو اسطوره پرتغالی 41 ساله تاریخ رو برای فیفادی پیش رو به تیم ملی دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30023" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30022">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz5xYnvI85vfSbdlJcLfnJqXm9AWwkYK5N1ESRM9XxDb0ZyNot_rrsk6Aqt6rbfM3085GGDR90UPKQe87t_IrkgaiISR32k2UWAqNQk2aYcGmD_6NYXB0hyRJ3VbZ2BXH-B4oCiQ9M4A-uL7JD5oodpyk4GkBUwufKRPE_ikMAvzcti__zgRQpODO1diEzGADWprjJnyXY_6pyuXh9SODGWtVMR24hzduiuRATp3f0b_BFDH_PFRye_mIkL_5L0iaLRaksnNoc7Fc3MmryCD3mT9s5ZAf1sNIRz3EfMsMq5w2qA2TjqV9e7wzuiGhdYcBFe37aSQhOlnecdpQ9NVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
تجربه ای متفاوت از شرط بندی میکس
💎
دو برابرشارژبیشترویژه روزهای دوشنبه و جمعه
💎
🤩
🤩
🤩
🤩
بانس میکس شگفت انگیز پین‌ باهیس تا سقف 30.000.000 ریال
💎
🤩
🤩
🤩
کش بک باخت شبانه مخصوص شب زنده داران
💰
برداشت‌راحت‌وسریع باووچر و ارزهای دیجیتال با بالاترین نرخ دلار
💎
🤩
🤩
🤩
فری‌بت هدیه هر بار واریز با ارزهای دیجیتال
👀
این فرصت ویژه رو از دست ندید و شانس برد شدن شرط میکس را بیشتر کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
G27
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30022" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30021">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AITz_6TGvlAxlaf-YEJtBkFUrBEl601HUxxLKcjpIBJuRjhFp8JkspHFuMErX9xxbPXNBiLgdmlarctP88UIXRsGwsgi0HZn4qHzxOpNoWs7IW8viHUL1tDe4SLbPgS4sFwXT_Qt9zyC5Qq1zEl4l5EdJT3ALazgo9L7pBSYjj73-ae1OmFzRuJDbNaO7GbMB69A33GkYUlZ30Zr2NPjqbwEEVt-BdRAeIGEO5hhrk2uQr_0-1Ljq_gDKKUxwuNP8wyrDcvJntwVmNHIHgifFqRGjXx1tV1nkoz3u7D9teCZTW0DfNMqJjZ3dOirsd3awYtOm5Pqgd7oHmzDdE2JPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30021" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30020">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🟡
👤
سه‌سال‌پیش‌درچنین‌روزی؛
حین ورود رونالدو همراه با بازیکنان النصر به‌تهران این حماسه تاریخی و فراموش نشدنی توسط مردم خونگرد ما رقم خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30020" target="_blank">📅 20:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30019">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWi7m8AN0vDxUhS3o-2Mg3B-rjSo4xDYJpMCyKKNWU-ixsx_tEosoXDtT_HM8CWq64Qom3II5CA3IGJZ7uI3QY0OI9fokY7UBwHDa3JzaWlr7onfwy1vjcGIg16yKHNRHbKQsObm6RFdCiBvtkt5IuOCimTuLPZFhIUSMk2ig5toYBQt387RUUgXRViUgEBOl-_ZtbTU-lXuQo42Wm7YPcGwnHrkKUc29JEPOzMtbDLWBDx9ssA8L4bWq1F5DWF2UGe6KHm7IKDj8lIrTvxTh2emEOuSafjOG1LE2cxEF8bkj3DBf5UrUjKEgMHTn0OCY5NOpmCeC21iR1XaWXtZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30019" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30018">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIKnJZk6N2VWB63MRQyO2HMrDLigdtgXZkMFLDezM32fmbyC4sI1c2zUF2p6mPbQphFyNwoJzvjuzkDfmaj_cD5Eis7OPrd3JAT5t0JPbPOIWevSqoj35RlLokdA4mX07jYxCa2W6Q9O5Fv3KSX_NUHgLfef1oywUZkxSlpf167JTYb01TcIiaP3QORURu4yp-5wKjdNgAKZamxieEVd4FGCuHAEy0AxtAJk8Qn7XwWNYakt4eeUcugUTEIDz7TF7voXsl_PUbNe2C3KhNl6RcyAMIQTUwT_sojP9VvDEc48Td0F7lFEisGoD4RxWyR56Ulbfxq7Z3feTU0jN9rr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30018" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30016">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRRAKVbeTt6r2hL8aE0ocUW_HB0nd7GWASO3rJ_AMpJ1pUeSSUiNl4IGNAkicvj7_bYGZlAdHje29DVlS8uABfyxH2VM4hkTlxm99SGUhpJfmGUawLxgi8H16iEwUwKJspJyvrroaWMi06SUpw4PXj_ZXfLnyD3phhJql76aizxnqNi74qPSaWG7pwDf8GFHHRlauZ-Y2-JoqpDgfdOv0RxYklzdnB1Rzd9QZc7lwFOf5qgw9UlHBCyFf-PtUX8rp8C8NMzcNz_l1r9qaoutckyoPYpmuxIA3VLCMBSMg97e1mcTQ0lJJQKOTRzrfrfOmz5u-HdBLIdNfZqG6Qh89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rwTx5DBKkSTqsTTCDe-TNnreJPkUgTluGv0Q0kLy7yh04znAEm9KYthihWnBGhHsqh6sVmMZnfOksSPxOFVgvRG7EhXfGU7wOgO_jpYBcf30TjQYiHNeLDvvHlZadYqTAMd5l8X3nsoHBDxRoJ5JcBmRHIS2WwHhyQ5LMwmw_-p8Tykl0w6ib-YXG4iZSQI2PC_xqjDktMcQFl4CPKIwEZkRn65lNIFfamAJRRYxUnBqDrlfHGaT230r2qRBq5Vvrllw5NS_dV6uYLjxqaM6bodxv9iqv7UCozWSzBdRZQs1uPLkssXeGafNUFwUeW2zoC-dokGcdwR0zNoK2Tun7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30016" target="_blank">📅 19:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30015">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RT7ZOJO--TYNRbLiloOglFTfFo9L6vGe3FRUQ5ax50clgjQVSRwtxKj6iGAO47z9hlnBFCDNOCFSID2tUgdHUI9ruE0sNXzxAm_HtzKe71kchDKByNmlUiQg3EiOj9qYsnmV1CJJHbkamlvOIuBd3pr90Gg19F-K4aVL0Jvpno856yztfB4RnVbqBplo4k1vB4K0PZr6HRaWKDJSF7sn4NLX-5Og0dVMkn9nkdmhHSFEd2QQEUMbwDqIfVq3xLvxRBdcL9Ep_dIeXA-Kpivl2QfEJDSDteVlF7qgU2nreO1TyK8XUCdvpLaYDp3jcPt8nMMB9z7727IpLLQ3KZB3nF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RT7ZOJO--TYNRbLiloOglFTfFo9L6vGe3FRUQ5ax50clgjQVSRwtxKj6iGAO47z9hlnBFCDNOCFSID2tUgdHUI9ruE0sNXzxAm_HtzKe71kchDKByNmlUiQg3EiOj9qYsnmV1CJJHbkamlvOIuBd3pr90Gg19F-K4aVL0Jvpno856yztfB4RnVbqBplo4k1vB4K0PZr6HRaWKDJSF7sn4NLX-5Og0dVMkn9nkdmhHSFEd2QQEUMbwDqIfVq3xLvxRBdcL9Ep_dIeXA-Kpivl2QfEJDSDteVlF7qgU2nreO1TyK8XUCdvpLaYDp3jcPt8nMMB9z7727IpLLQ3KZB3nF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابک مرادی هافبک سابق استقلال: واقعا دوست دارم زودتر بمیرم. خسته شدم از این وضعیت!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30015" target="_blank">📅 19:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30014">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=sfygSFtmHque8PN44bwQhRpD4ufaJjZDOx3O_TmVl9hc7Rk0FjDTfG2h61h5zroh_7oG3DVaO8mLjNNw1yT2gXf7gnky43tbcPvhoQjEpdBfH2qixGCrcch7DL_h-9hp1_sA7MPkoJ5epNiuff0KvqT66I8Kow-46V3TRTZBLYbM6Tyk6qZUm6XvuVfZmc787rl_UBbrwaupmDOGVKf3advPP6ygFfZeSbGm6ZvVOw5Lx-SK8QdKclt9Ph_llVSfZtQkY9BnBTnGJbf7KSvwa8CkaObsD-M60HDb6yEwGfst2PTI6Fm_-EiAdMqTwY8UQE7IBgiNudPjK67WRlx76bWxd9iGYsrKDRvRmztYq1P6b8S6U_3A3LHvG3mY3DxGCLl00LlJhFW0iI37t2KCpJHtQA2sTmd3EyfGuqKhYYW-dk_aRYT20PZuQt0BzoHQDn5dhwH9yZ8boBSzb6AWSbub_erk4rQ0WNL--8kbwFZORaGPQpnCLrn_UjCQotzeEg3mbB3IcZxpYXJFzCbi9dl63GflpWpXetCxBX59yVz-RfePhPJ8YEAuQQxs9NB1BOhrF5MGnq2sE4aAPNcNMHlyvIt7TTirvoS07H93hgkeBWv1uv8PsUIZvhKCjSwD9HZ4yaLRKgoxD70HKdl3YVkbPZVAy88GSaK8-Gk1hAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=sfygSFtmHque8PN44bwQhRpD4ufaJjZDOx3O_TmVl9hc7Rk0FjDTfG2h61h5zroh_7oG3DVaO8mLjNNw1yT2gXf7gnky43tbcPvhoQjEpdBfH2qixGCrcch7DL_h-9hp1_sA7MPkoJ5epNiuff0KvqT66I8Kow-46V3TRTZBLYbM6Tyk6qZUm6XvuVfZmc787rl_UBbrwaupmDOGVKf3advPP6ygFfZeSbGm6ZvVOw5Lx-SK8QdKclt9Ph_llVSfZtQkY9BnBTnGJbf7KSvwa8CkaObsD-M60HDb6yEwGfst2PTI6Fm_-EiAdMqTwY8UQE7IBgiNudPjK67WRlx76bWxd9iGYsrKDRvRmztYq1P6b8S6U_3A3LHvG3mY3DxGCLl00LlJhFW0iI37t2KCpJHtQA2sTmd3EyfGuqKhYYW-dk_aRYT20PZuQt0BzoHQDn5dhwH9yZ8boBSzb6AWSbub_erk4rQ0WNL--8kbwFZORaGPQpnCLrn_UjCQotzeEg3mbB3IcZxpYXJFzCbi9dl63GflpWpXetCxBX59yVz-RfePhPJ8YEAuQQxs9NB1BOhrF5MGnq2sE4aAPNcNMHlyvIt7TTirvoS07H93hgkeBWv1uv8PsUIZvhKCjSwD9HZ4yaLRKgoxD70HKdl3YVkbPZVAy88GSaK8-Gk1hAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
#تقویم
؛ چهارده سال پیش در چنین روزی؛
کریس رونالدو فوق‌ستاره‌پرتغالی‌رئال مادرید این گل استثنایی رو در دقیقه 90 به تیم منچسترسیتی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30014" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30013">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUnPuzIftZFsLye0LEsI-4LuCHN1QmhRb0rkjr6T4ephGOO1oTlh7yvkFWzigHeUi9mp0fYn6FNutnkgpIcyHpe5FCWSvBJdsNK8fYlbqoJJ7bSxe6a7anvu_gIZzKpdJAkql-5dnpobGItnhZUX0iBAfAJUJfgxwdsSh-P0JhjyEsbxwVjGF5Whv1sD8ZbM2c9YLC03Rm9reje8Bfyk3Wks8t-CIcnA5HgnQ45j_2zsDDfQ-8qGNavoMx_OpKiVse8KfZwNFAiIJuGjmfjLhSF5alPEVInKoUowq3kWJabBQpNzeb8q-32SJTEeh-XQwXUvz62lO3ip-EvmExgoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تقویم؛ سال1999میلادی درچنین روزی؛ تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30013" target="_blank">📅 18:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30012">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdbXCl9GjqDhllNmAGLJGSqD-1SywTaMFqsw7_5zFZ8LXmA0Nhsq5FfQwvJyovpKoGWSr_YrjGp4KKGm7yuLhX7dYlIp-PLYyUORqL0yIB9Lw2QZPo4JPr0baF-g3dl4oRV83eEJ6wXIw4mJvQta4LuMItVhW38QWOfh10dbGYor_xMLpQ_3QLJgSw09NwgRgFm4TjQb96cJZb738EkBSdoUIjB_CVudR6OZ9L5kkTq1_TrPnZBnrJ0bBtvb2uEh5r4etzLxVVuGZvEIVP5w1f1aRpLZtJWwxZOfOMzTgC9YcdSh-wAmlzXl1XQ1HtElJ4ju6bKAG5fVI2GLs5KJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30012" target="_blank">📅 17:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30011">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2GeHS20Zsk2CATjWeynR6vOwlmuVJ5tzAydx8I3EZs7Cw-kFAitx8kECXUKR0j0QQzUCpZLWZXfNffvfh7-_A0GqT0gy26zV_VfWN-U1BPf-jIZjog2yCcQP7oo1k0zNxFZa-zGsQxTS3XFduYxpVht2Tg1xnlG_J4yzbOKW3GWLPzm1wH93WR8Sll59wNPm4BVt9Ytcz3t3SujxYAx1k20S5WgMGp8vBS-6PqThw7CRCXdB_qUTaMIgX0ZrxFWgXYpP0DB9iN4M_7g5EDgrdC3cd3eYwwuYkR4muP02uUGIYLRUGVdSTDGgtCxwAyPQK0lNM-uqiNOrEbbleMnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزنی آلیسا لمن برای تیم‌فوتبال بانوان یوونتوس در هفته گذشته رقابت‌های فصل سری‌آ ایتالیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30011" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30010">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=Msv8obm8o7SWN-f0KetvZWpqdhdSVS-Q66SQqFbRaX-PKiyWn2XKc_OCuqz9uSe7ty2IqMQ7rty1AMSIGMVkD_N56B6F1uNwYeXI1KQdkmcSVdtAKnWgOgKzGE0nHlvF-p7kJLKqadH7wTwikAXZiqxI41Y8RzMU-DvU1khuSLWKjqOTgdcW0Mi7eQQo2PJ58LtYFcSML_IDGHSBPVZcmsZzlaqItVsVxphsqHGcCYc201JExXZ-lAKHo68QLr1C1h89dp-wpesAD20pUbOQ8BhBGVv43azY5Mhg78cIsMXmCATE6OZlxqf-7SE6ggYJ13q6EkGTxcmY-cmkICFvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=Msv8obm8o7SWN-f0KetvZWpqdhdSVS-Q66SQqFbRaX-PKiyWn2XKc_OCuqz9uSe7ty2IqMQ7rty1AMSIGMVkD_N56B6F1uNwYeXI1KQdkmcSVdtAKnWgOgKzGE0nHlvF-p7kJLKqadH7wTwikAXZiqxI41Y8RzMU-DvU1khuSLWKjqOTgdcW0Mi7eQQo2PJ58LtYFcSML_IDGHSBPVZcmsZzlaqItVsVxphsqHGcCYc201JExXZ-lAKHo68QLr1C1h89dp-wpesAD20pUbOQ8BhBGVv43azY5Mhg78cIsMXmCATE6OZlxqf-7SE6ggYJ13q6EkGTxcmY-cmkICFvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ سال1999میلادی درچنین روزی؛
تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30010" target="_blank">📅 17:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30009">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgDW85xd6QNjiMDXY6nfWrwYB-rs7beYNWOHb51dkc9XlaAP7bJRYojTeV8KWovoGdFyHkSCCxRi6sUzFXQsFYydkssFfapjc84LSEZYDst7TSUxVzzgTM_LceKh_AvGQBZukPZqbX9ga5oO3pCbZaeTP8QRe2PR5Jdb17_4L1lVjd1ifIPGIPAt_n7Qv7mGRAHqv0xOoHV7_irO80sOeRtp8Kp3ru7j0oNUIUenbg83XzwlHwwuvAvUAMnswQOCKqx-NGmOS9WPDc-xF5R7kusMF_58pMEj3YgLbZeRtXbkM5VlLv1hpBu197kf1Y30Iqy-gMVfUrruC1qc3L-C8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30009" target="_blank">📅 17:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30008">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=IBxWb720vDv1GjU0HohMRYHrD9B3EQcwUF_efB3Gp1zSCY8lVFoCbOC8ObljK-392-BYYwtP6XFtixmu2kxZc3uINVr4Jqvs_hdl0xAr7PrubSTYdekDf3plKv1m0lPIShtcxqXBnGK1so9-6dBdg4qzDGrInFDXbHJubSvXf0IbwL46SWCa6JBkJEqX3JyNMBLlCzzRrsemx5CE9gKMp2UaavPw4Q3-MahSrXIqtQYAgTkLsM563hONTMAFm-4B0jEN0HNs-QbVP6xYnpV6KBhVC_2kbgM6IGohtLtSjSS4fooeXXFEgZ0av2sh7lIk2tY6bJKyscCd-L2R2OjQNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=IBxWb720vDv1GjU0HohMRYHrD9B3EQcwUF_efB3Gp1zSCY8lVFoCbOC8ObljK-392-BYYwtP6XFtixmu2kxZc3uINVr4Jqvs_hdl0xAr7PrubSTYdekDf3plKv1m0lPIShtcxqXBnGK1so9-6dBdg4qzDGrInFDXbHJubSvXf0IbwL46SWCa6JBkJEqX3JyNMBLlCzzRrsemx5CE9gKMp2UaavPw4Q3-MahSrXIqtQYAgTkLsM563hONTMAFm-4B0jEN0HNs-QbVP6xYnpV6KBhVC_2kbgM6IGohtLtSjSS4fooeXXFEgZ0av2sh7lIk2tY6bJKyscCd-L2R2OjQNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروزصبح‌یکی‌از بزرگترین دوهای ماراتن ۱۰ کیلو متری کشورمخصوص دخترا تو بوستان ولایت تهران برگزار شد که‌ چندین هزار دختر توش شرکت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30008" target="_blank">📅 16:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30006">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkA5YyDb1jvRSuo0FdSLSWPZpE_auhXa25cK5zlYfwUFj5Ns67CdtLYxZUOJPrgm1-Xq_GZPOxlXuEOZ4HQqNU4TrgNQz2v2cB09HUoe2p7gvGETBe1nxIrom20z6KGN6ynOfPtV6-9vBET1zSOxIIIo5x8lYNmXpQ7MiF7UF7KJWo0SW6EG7_aufhoMgCXmU2BAxDKsBMwpjZq_6mdxGrO5W00McroKki1o-Uds26rNEQBOAn3OKQa452X-LToAaDkBM8YbqfvOpOpeG_43Be0dWHVWkPnxz6h3eXsgSB1EATBireiwOcGMsQ9vGutrOOpFex83wMvYbZuf4JZSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7yW0yBsmyOsJMYIKu-0jqNEgZ1joy4KLDbq1Up4_drfxOyZNBW_jjCAhJpSCebHOgak5CEA7C0m8nLO9c3Jxh5YsaQQ3206o7fHiZArBW4jx6tVI01O4A8DE_-Vai_OgsDH9f4duQOcT034UK6JTWngr3ITmuGsySXIlMesaZylFi5vZEhhI3chWbfW_L8clGyTgwmHCs3C6TdaYhWaoIgC4yua4MLL6YR9KcTvqYyYpSJqc4H5jRU183qplroaMRKaqSOnFYYu80PFJ5s0IeH-J8eQMMV4jOU3KOYaLFzCPl0yguPRgd9UgNJSfayko9AJFu_BYZl9DyWbNKraQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30006" target="_blank">📅 16:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30005">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chlOuJ0qvtfty0qI16ixgzREQP4Qfws9XuOXM80d4TDU_93wZFcH1I1H8cyvzES59anMCdBLzrGfG2cGRyqwfC34E6xg2vUPROAKBFzP_YgFWLJ9Zt6SNi0EcMUoN7fFFXXEPxV0YaW0DRDkhJ4UcEWU5ZaZAM-ZyGHZ2dYj5lqFzPytUsSQSLTSfPi_yZaetR326u1uRc6VhjVBRNv-2thxyfyjwpg17avbvrfsSlcfavKwryy2NHeexkdkm2o443Ba-8PbJ6thxoDuENcYTGsJvRKIsUjAWtQto2H7VKUmkHx4kc7CLgCzQnEsrA4ObpTcR2ZRsVU84aaM6X75fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30005" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30004">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEq8TeofjxaLw294Yq-snDKMv8rI8vWJALxNsI86TdcnuFyhjHlmQRLkSGu1uxRVvd0UMVPYatN521Vvvir3FaeUrCu-NM3_zDdAR7JY46-4VRsG5JVkrekKmZwpKsA7wW8H3_oUF1SJq-m9L0M8_-310Oi-k0t8AXRLq0hcp1YphSFGH1ZqTreVVZmH_SVQ6qTyW2CHdhztDCql7V0gqjAQ1sHfI2HwwXdx_TQTVFmbK2wTAPX1S_X1Qf-7jcji5bBBqFMUtHjBcL96-q_2zJeiozFnaPDiZlBMgq4Za7XzKIxU_9Emtl9BFMNz8g7pPZJ60c_mlyCIICB6XmZmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30004" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30003">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3aujRsgqkh1-5Q6LTD6gpCmPLgzMTKXtlpdXGCpg2GwScvj69Vtzb5Y8neAWDw4It1khwfZz2q5tLRKYvv7l8T5Ek1d8G2myW9McTdd5cfz9Y-1Mh2WGP4yoLQaMcGQG6x7H4aeOfaXCpKotvzA7XW0w5vGaK1tUV2H28qBrxXb_MPD91TbIKJxLdET0LLg7aoKB-Jr0xAqq9clbZTxDTPmd4sffQrg9FPByNgacG2a6mowY04pi2OnF8bK3xQLv76Qn26gVVD4gqYI9ipM7u93cEwpmPx15VNN2uNgVC96MFVyI_qRWOuiueRvoqs4cpX1y0X0vazkCxEnHlLzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30003" target="_blank">📅 15:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30002">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULsq8TQz16i42KwR6RYOFSIIqr3huwHcuCVLG0f5yp15uyGY7hC66RHFmxBiYOaAJ2E3RLVJD6rmwIJpG2g__lNr2-7xzmMUdVRq9eMmgqnmgZtPFV3l9XOmxMPewfHKnIQ4CLCC9ZA0U6GTSSve3iuNBMDC_FaR1QeTNTtVEm6BdBLuSbWxC3OpYBOpEoH0WjcAby3SqzXIKb4z2HLImWC6LMeYvS_PbhxQGNDwfjKLxUrYhwWr4Dhu8gWHouJ13grDC5OPlJSxsswGP-zmfYRw-lG9vVIewXUcrRWbdvJDFilerelJiEntFXsre5o0ZFYoeBa58WcOZdj5oUAX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30002" target="_blank">📅 15:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30001">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=m_WlzsXLQ_MNlb4As00ZG2-t3151Dewy4Yl8-JJoXJUzJM5Lyv-CJQ9YaxhZEg-M1cyrweCtHdrfBiH4-rkeV-zcajJgw0kteUjrAVU1TuGOp3sgoAh9KwQfOKp9OobiTdY6AY3UAhEb-RNQQfMdfy0rYIfqYGzxgWDUw9KPOCtnAo9ergHD0rmoon9lFPSimIXuH_yzieNbOgcA1u2FYQ6WBvXvjY8ohS1_GPH9bdZz3qrxeeQX4MF-m3jj8x70QmmLk6Kq1DaR249R_kEug16iX1kYimEzDnhNRI1rFW-OzOThKwuIKuApujVostAZJwxbS6-ZAGBAdTY6oChaLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=m_WlzsXLQ_MNlb4As00ZG2-t3151Dewy4Yl8-JJoXJUzJM5Lyv-CJQ9YaxhZEg-M1cyrweCtHdrfBiH4-rkeV-zcajJgw0kteUjrAVU1TuGOp3sgoAh9KwQfOKp9OobiTdY6AY3UAhEb-RNQQfMdfy0rYIfqYGzxgWDUw9KPOCtnAo9ergHD0rmoon9lFPSimIXuH_yzieNbOgcA1u2FYQ6WBvXvjY8ohS1_GPH9bdZz3qrxeeQX4MF-m3jj8x70QmmLk6Kq1DaR249R_kEug16iX1kYimEzDnhNRI1rFW-OzOThKwuIKuApujVostAZJwxbS6-ZAGBAdTY6oChaLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو ستاره‌برزیلی‌سابق رئال مادرید: حاضرم تمام پنج قهرمانیم تو چمپیونزلیگ رو بدم تا فقط یک قهرمانی جام جهانی با تیم ملی برزیل داشته باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30001" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30000">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdLriqM2nkUmrTxhjSTdI5aJcEfh-sGV0BdpQgpxM4BMyLmHTATPNCihr1_j_8cJ5VqzepTt6RNNr-UPzp2-jXImT6PhpU7BrHz1PyPV2uKtiF1Z-4kV0Mw7si225i_uMKApTGyNfBAquFKwK8_fMTZRJDm9UtWo8-xtIj-uWMww7gFEQy6nz5qGXKIoAOhJ725hv-TxQ8m5vNa5MPzrYSsg7AnMUVSY1SadJbwnN9UQizq7Z9jKJ8Ul_gHfKQJNu45-2T7Imj5SRoFVb7Ce-yOJDLB0LK54tcOXCgBEqZ-6txidu1sPhDuy5jjqfueHDwXvkfZAVgjfuU5gYfXMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30000" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29999">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVSUY8I3hLeIw9BQJiysmqwt9ojNEs5e4jp8C25nqcBxS1LtFrNjhQer3x3JnJt5BPijlPfKThVUPRqFrJGcjsNJIhO47nLmG1j0EXiCI3f4kL-4cm3e1rMQfNXtGQ8V4KvBCLoPYlkGXrBHLZwGUoJpWeeQik_1yqDB9OA8KVxPQUBwidCN7GGzVX04j4QjX5K56yvWTfx3F4WT6lZLVk4IkSfuAPoA7TNLQotDDji46Xuw5_xphlUBUU3P8uu1Fvl0x3y8-YSxk9ONZxBpeb-LiljZ6J5cL2Ybgnj919Y-q3iAz3fX_cUOm_2znlAsgWgkJqpNhBvLBDYIq7GSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
👤
عملکردفوق‌العاده درخشان تیم منچستر سیتی انزو مارسکا در فصل جدید در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29999" target="_blank">📅 14:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29998">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfdssbuHzgS_pdB4TY1r18_vlSpLI8sQKGDapZfdO3ddNQV3euj4ZFypQ5LVU1z8_T5FNxxRfuv1xTFKH5lOqPe_js5ZQFP8GbH1XW3gKtCgWMhdvceRvdlXL6ySStYqkrF62yp1ulLV5peAbfulAjDjQqAok3t-GOKpwFtoIOArbjD7IrvF-M53lxEDbbGF33KbQosdgrwg9H_p6BgdBdX8XVuttMnMLlu5EOyu3eBFetmFR9WNckEyDV-Q7HEfj-HcYZyGbhO7Jmj-FyLRh14ba_N1y5-1B_d9j5Xh4Zb24ndR5p_kq2iCO67aNRekYnzDGcSipcUEG7uhTU306g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29998" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29997">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=SOn8G8TmMARtsQ9jsTIgZGZDj5oCvjUgQD9KItl2NTLZG_y-slxFjbgUsOV6hpDa_QBYqkHPadCvgRcna3IgaiGZtXQs5rLvR9oF6Z9q4NTQWCbl7zJwgbL9aLyOhDx5Pp-V66x7qJ7YZgfd-EZgCLF1gRRMZCXiPtAhkqTJ2XokDbm7lwms7I6Ouc7w58ge5ABGVZWEbyT51vtq_Jcvo0TbChreBH02tyc3bV2UWtyx2AnCfWjVau2KEG-ihEAWYenK9g-jY0UPKiLgJcJ5drRnWmsHfCa6s0kEWJn0E2Gsq15hAqzIUH3yTVOABi4Y4l0ZjN8EisOQfLCz1lHxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=SOn8G8TmMARtsQ9jsTIgZGZDj5oCvjUgQD9KItl2NTLZG_y-slxFjbgUsOV6hpDa_QBYqkHPadCvgRcna3IgaiGZtXQs5rLvR9oF6Z9q4NTQWCbl7zJwgbL9aLyOhDx5Pp-V66x7qJ7YZgfd-EZgCLF1gRRMZCXiPtAhkqTJ2XokDbm7lwms7I6Ouc7w58ge5ABGVZWEbyT51vtq_Jcvo0TbChreBH02tyc3bV2UWtyx2AnCfWjVau2KEG-ihEAWYenK9g-jY0UPKiLgJcJ5drRnWmsHfCa6s0kEWJn0E2Gsq15hAqzIUH3yTVOABi4Y4l0ZjN8EisOQfLCz1lHxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ 15 سال پیش در چنین روزی؛
نانی ستاره پرتغالی منچستریونایتد این سوپرگل دیدنی رو در رقابت‌های لیگ جزیره به چلسی و پیتر چک زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29997" target="_blank">📅 12:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29996">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf51IvkjXUEM2_62Zo9BDW3pRBmdWjXEPXK9iuvqS7qOatnRRCK50mY00D3dXkX0ZM03js1qy6_Z8mEek4nP8RwTc6-IHRWMZX19j0ix9VPmWihn0OQjVS2TNN3vFwqVGgiyEMXX6ZYd95iPbLZ1Ssbc6JYDRdFxRkyI2uERDs8_hlMC_4S3SNYTC_uUPrCmPT_plQujArhyZaCVMshc4g5GBWE4AVNkky0VPOlb3ezjboaCvBPw1P9YCxbAuU7ak8xMauF3FYNeiaoes92iNqn97RjoW9ETV0rtM8LYxULjb7rNzTn7Ns9mUh3OpmlO08hkuDU35DSHX0X8XJTXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب پشم ریزون و استثنایی فوق ستاره‌ هایی که همگی‌موافقت‌ خود را برای‌حضور در مسابقه خدا حافظی کارلوس توز از دنیای فوتبال اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29996" target="_blank">📅 12:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29995">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In_vWZCzBfLXZBJ33w3zrhqDy5ClgcGqG8Q71tBhSoV3Cs7kfAUG69KfsRUPZ09APFNJLwFFbzLNJ_1NCMSYl-8tGtq5sWbVo1-i4OmeZ-irKaRucSwAt-jtt-Np2isiJlK2dLgnGNaMz0s0fCJgwI4XTGOzTriig-jlVzfDX_-jMNFpZ_AEOlir2XfFAbWLBrxkkS_C9tUHegONdTuOAjCe982IcqWLnXnsTWwroxOitl2MdtU35IyxKEqpQicEM8dm-AUOSvGW-OTL2KT8pqs4MeuID2-FlLnmU3tg4TO2UQbibO9ok513RJJvx74Jd6hN48IG67CeojdlCpT0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29995" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29994">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCiu8q5L2A9ODEnPaEG8KLmOgaq8VOMR06h6gsP2dOFRr593SbfYpCAM6s-wWtvmjXA9xA_FMmYPGnNDtfkCsx8BubxBeQp0J-EcVWH5rsl6px-5F1DNQS8Jqqa4Kc-8TrJSrM33RlY0YRKG-7fjJFWCnGCD-VWfB6byA8ZCt_p-hQ4F1ork2WSyluQ6wqoKprLBbFEwL8cecC3JCIyD4lUfohHsI5vRDJwj1Dtvzj3H2T0lfGsCzJDZFQm5uRp0OwyU0ULLQKGr6INCnMmAdtrV7_2KzA6AKQpQJOFWsXCXRX2kjqsyTbycip_VVsHkb7kNqf1pcmDfg6nAX1Kp9IGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCiu8q5L2A9ODEnPaEG8KLmOgaq8VOMR06h6gsP2dOFRr593SbfYpCAM6s-wWtvmjXA9xA_FMmYPGnNDtfkCsx8BubxBeQp0J-EcVWH5rsl6px-5F1DNQS8Jqqa4Kc-8TrJSrM33RlY0YRKG-7fjJFWCnGCD-VWfB6byA8ZCt_p-hQ4F1ork2WSyluQ6wqoKprLBbFEwL8cecC3JCIyD4lUfohHsI5vRDJwj1Dtvzj3H2T0lfGsCzJDZFQm5uRp0OwyU0ULLQKGr6INCnMmAdtrV7_2KzA6AKQpQJOFWsXCXRX2kjqsyTbycip_VVsHkb7kNqf1pcmDfg6nAX1Kp9IGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از کاشته های دو ضرب در محوطه جریمه حریفان؛ همه خراب کردند تا اینکه بالاخره یه نفره یه بهترین شکل مملکن دروازه رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29994" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSJKqjDa4GXATE0dU7yEAksZ_O1Zo2Ky6PUt6u-IjpmvPCJRZkbEgjyvEYQwodXt_63tzcNpLqPMWCpw9mbk9glzjrCrCWnJfqaIYB1QLYrSQGx_pgL6j7-PcVLIF8yLzy9t2lOMrgzFA5UVrjf-0OgQ8AtQCHhEO1zNMo0cQ_n_VCdIMUAuzLll-SiNXzZ6UZ7B5Hxz1aBVUW74eN7KC59pjY_jIgPg2OhNhZSwlW_TS1mO6qmevoAJjbMhN8bDHLZzWShw5aKhErReIgiLN3vX9JnufwLmF_TrhD3OpGjvc79yGfzeJ5CQdjPlE3Hk0J-qLwPYpmP44J5_1zXeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29992" target="_blank">📅 11:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zYhOdt_AdUQWpukLO7EDtooosS0s9om2gKy8xjl-P_XtyOJPuT1IpwxFKS4BHpESWTHW4MrhCNJO3aXlR712dq_T7HwdV4-VRWLuGaUQgZnexU9RsjibgGDWB6btb_rJZF-PiMn-XcQ08xZEPQlsfiUuVCNMQONmsuetxihel1MOBl-mKbpRf1DqAzC9tiau7k1h5P4ZVrB-eOX2dmByLbThAZ7S0_XxGwyam0bK7xMzI8uaK86DtyLzK4KWb37yOaF7Om2hYpOx2tyDGY2p1KmFyrL7RWyYd-wbP1MV6Ek8A_-3-F4He2F6pGDXgQhWfSPhSZp3XvyDUTBOMsTtpNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zYhOdt_AdUQWpukLO7EDtooosS0s9om2gKy8xjl-P_XtyOJPuT1IpwxFKS4BHpESWTHW4MrhCNJO3aXlR712dq_T7HwdV4-VRWLuGaUQgZnexU9RsjibgGDWB6btb_rJZF-PiMn-XcQ08xZEPQlsfiUuVCNMQONmsuetxihel1MOBl-mKbpRf1DqAzC9tiau7k1h5P4ZVrB-eOX2dmByLbThAZ7S0_XxGwyam0bK7xMzI8uaK86DtyLzK4KWb37yOaF7Om2hYpOx2tyDGY2p1KmFyrL7RWyYd-wbP1MV6Ek8A_-3-F4He2F6pGDXgQhWfSPhSZp3XvyDUTBOMsTtpNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دقیق و برگ‌ریزون عادل از پاداش 20 هزار دلاری مهدی تاج و دار و دسته‌ اش سر پیروزی شاگردان کی‌روش مقابل ولز درجام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29991" target="_blank">📅 11:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiJiqAxcJ4s5jd3ksqDaprHbGljwlfYprp45Kybx-gnIdA-S6dd6tCzohGvBdCyZA7ZdAoT1vgtEtbzL_JrzLa55iVGIB-aSq4iIfW3AptZaoqg88E-IFFQPGtMn2LZyywhbVoHkgas92JLqfpDd5831EvH3dfcsFnEn0N1Qqkuq4xrownbNUU1pECOyPYU9GVTQW32TMbjK9db_9oFFOJQFWUBcGM1NQZs78ls6IHDL72fggG2AN7HwY1vmEURDm-JVBZpM5mXbmdvNfHc15nhpA1iG86XIj_j_FF2amxwvIlbHKMzJh5IHvaqefGEXtB_V9CLPAtbNsU4Bpu_7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور
🆚
رافینیا دیاز با پیراهن بارسلونا؛ رافینیا همین امسال به تعداد گل‌ های نیمار در کل دوران حضورش در بارسا میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29990" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RosLnKfcyKB1Kl3yckG_RZMGGWHZfQt_95v0NRw3N3JW9F2oVomcIASPgsIHkUv_hl6rpJm0tz4spc3uYeYZEsRv-w6ciprcsKDB8zyhvzgM_4KBPcyIjzNQczABSsaQ5NntiZnsz03-89K14DXLvFrXaK-QWHYz_OEFDt9k-8AQVFUlB-9_UHTzCP6mgqd3dkj3GnB5NpmjWy55b4dEQyZuM_atKXfec0o1Mt3JNeuZcQ2WF_F9If1F8J7h91GTYkS_5bNLie0Nul7HkG4VYe5kBrWWW2U_aMTucgeHSVcJpvyu7Idiu08eogiWHqvmliw_I2YCjGO6v0pV_AwiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برترین‌گلزنان‌ پنج‌ لیگ معتبر اروپایی تا پایان رقابت‌های این‌هفته؛ رافینیا دیاز با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29989" target="_blank">📅 10:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKbls051N-w8up2YsRU7NGg0PN48LLhQe6RDAorDaInMBDKMb0AHI-d9JuztPf8O1KCPdba2wTZS4MEwJ7sN9uwQ8VnH7tbvg6vi3cBCmNGmnO3ddr6VkrPU3VSOu5iyUEdn9avfJX6c-8mwOlUvvVX2fq5BEuvityeAKs5Dv0lOMKk9_2ioEmwVoF8maFxC2XlqNrVlmkU0mzvrz15DuvzJOw-S9JjQCuVwS0_0p9-wlZ97rjSNhWmyJtLstH7yWGTCdoLouG-16_Jf04Yrlo6WW56RaowOh8lE8Wdxm1FCl4YftEZHD1d_ngqc8mUwa9lRlhRiOCNwmg2EKq30Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29988" target="_blank">📅 10:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=rHVTBu55SiamxdJjhZzGSGqEwxr7mvPN10gJXFdItGyBX_5XrnmwieDvlbFxr9AvjDQj1owqYOXeHKEGd4ullyhzV1Yl3NaSNFw3mayCYLjOXsbW6Ed9PlBJC-pyT9mhQ3EXDx0STCo5aPTi_cxE-RgPbReiHnGDls1GpG_G2wxmNPrvdxt3iy7vVXeLjDkV4MA67GYGibtco5hl8qinYk-Z8QGHgAuBlKCXFlWNfKMiHbfJSSvz2sB_hAgw22VfGEPGPYQG2RnVphmzO0XzkziLwDmZIsSacmIcAqrXmKDdsy2OfPVHP_B1SxN8ZRGRTh_zQVhV_tZfQlKyY9GDCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=rHVTBu55SiamxdJjhZzGSGqEwxr7mvPN10gJXFdItGyBX_5XrnmwieDvlbFxr9AvjDQj1owqYOXeHKEGd4ullyhzV1Yl3NaSNFw3mayCYLjOXsbW6Ed9PlBJC-pyT9mhQ3EXDx0STCo5aPTi_cxE-RgPbReiHnGDls1GpG_G2wxmNPrvdxt3iy7vVXeLjDkV4MA67GYGibtco5hl8qinYk-Z8QGHgAuBlKCXFlWNfKMiHbfJSSvz2sB_hAgw22VfGEPGPYQG2RnVphmzO0XzkziLwDmZIsSacmIcAqrXmKDdsy2OfPVHP_B1SxN8ZRGRTh_zQVhV_tZfQlKyY9GDCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی مثبت 18 مجری‌صداسیما روی آنتن زنده؛ طبق آماربببنده‌های‌صداوسیما از سال گذشته تا کنون به یک دهم‌تبدیل‌شده. مثلا یه برنامه تلویزیونی زنده شاید روی هم50هزار ببننده‌داشته‌باشه تو ‌کل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29987" target="_blank">📅 10:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29985">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a52708609.mp4?token=NCjdTpQXMGE5nr24SL3mbisuaFBVkA49pOjeuEzifxOu2csALJgILIS38pJoMC4o37ho4zR1HUhhr69AaV6YsiNRF9Sy9b1rFWJEeRdVzIzTRI3H8tnDLupNfr5DVWm3i7819SgoAbeGpqH6I9sc-8l7GE5UNQTQLq2t9IACjck6VnBPmJDDJ-11DrbZdV4ijm7D5cWZQZ3KoDm8XDO_jjmDzdVa5PZUSbHarBsQyc7iPc9flRW0t0ljmAzmOgRbdzqwG3KkDh5_dIfuK2Ny9EtEIFU-J8GsWkqATkNSXyvcTvEKZoffxK0zBQbKvSWD4vfewZ5vF1fVQgttOUWP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a52708609.mp4?token=NCjdTpQXMGE5nr24SL3mbisuaFBVkA49pOjeuEzifxOu2csALJgILIS38pJoMC4o37ho4zR1HUhhr69AaV6YsiNRF9Sy9b1rFWJEeRdVzIzTRI3H8tnDLupNfr5DVWm3i7819SgoAbeGpqH6I9sc-8l7GE5UNQTQLq2t9IACjck6VnBPmJDDJ-11DrbZdV4ijm7D5cWZQZ3KoDm8XDO_jjmDzdVa5PZUSbHarBsQyc7iPc9flRW0t0ljmAzmOgRbdzqwG3KkDh5_dIfuK2Ny9EtEIFU-J8GsWkqATkNSXyvcTvEKZoffxK0zBQbKvSWD4vfewZ5vF1fVQgttOUWP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
محمدجوادحسین‌نژاد که جدایی‌اش از ماخاچ قلعه در نیم‌فصل قطعی شده امشب از نیمه دوم برای تیمش به میدان رفت و با اینکه بازی رو سه بر یک واگذار کردند نمره خوب 7.0 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29985" target="_blank">📅 09:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29984">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogqBmAS0Ittu0bLFLmmTmu3DtAx4QlXdVFFolbyPEgn5DRk8gYxAZi1Scb6Hc7BeHTgUiPbNbLVHPPgpy0rJxm_mF3rWZc4tpZ2U8gsj1uR8kGVsLp_P_w2_iptLCbpt8hLE5WqV--b_rS8JlQk9Z1P1IXR-L_Jg0NKXb-p8IAiljrb3iQA_RQPXenqKMLJdDwtfLzzsG0_6GrmukmQZRKz1JTECt8H7w6SO66uh-p_61nHTFhj-ri0yijVx91N_Z-ywOpyl8LMEunlR854ytfoceNKV8UExn_bcTzVtuI6uhrhAcNFO69rSiIfAK5ScZssX0NlMKUHGnrGbzW5bOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امباپه‌ستاره‌رئال:
اگه‌میتونستم یه بازیکن رو به رئال مادرید بیارم کریس رونالدو رو میاوردم. او در این سن هم میتونه موثر بازی کنه. اگه به رئال مادرید برگرده قطعا میتونیم یه زوج خطرناک تشکیل بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29984" target="_blank">📅 01:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29983">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6tAb8-xY5XVhX6gLWcj_ETzEhC2C79yGkuVOsw7IgGMXz4dMo0Phg1s2xMyBULwfASCRM4OerXMv94-t1ZVdBzYbxkK53aEF0muslaXPkTQyqR3vgczeR6FbdChFNM7d7_xaMEDy0q1PcYvJcpvuer0uAki0jiXbSoj05POX3ku_Y8LFI5CNW-X-GETgghvzCatOGoIuzaNjLhA30kVINTEwgEWx1EydBN96CVROORJIoay4zkAS6q8IaygFLeXpBinIjzbaIEy9uQv0bEzXF7cpvmYAqh0LKPrQmMptFmUFryAfHacTy3tEzdShQ8_ZFP0eS-99TWOrfL3m3DN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29983" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29981">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv4Q-6PBQHV3f0b_1IP3YhG4p7RnqjAjFJ8xrnJhJZgdJroXlKZ8GcRQqUNHeyCIX9fCHJWpjOFcXzD8dVg6B66lWKkXlwYvvbgllLl-i2N6aOJSN_LfwHoqWfbsxNeV4a_Q3roqLUz75ouxmHtYUBhCPK3YARE4zq96fW9xFzKC1Jyh7-VFbCmRgtDg6BBwyEzWJey4y1JZFyWV5-QDs70Jasz5D1N1q2dhYAVEEqroEfjCGL3PJgi-WF2eBCXdCrRlXlI3DwopIyi7m1B0KDpGpe20c4IMxhe5_hhLrvo-dbZwM2ndhQDt_qX4ZFS2TYv0aDZU5c7ClxroLVbMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛جدال آلونسو و شاگردانش با برنتفورد برای بازگشت به کورس صدرنشینی لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29981" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29980">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d835P8mfBhO99-ZkkVU2tu7u9x-57fLVlgB-z_bsK1wvtutrUpAY89n2v1Azqt1SEe3JYiPXOSyDSVpcw0ZbhqmpIQnIT1Idx09UG0_ylOON7BRGs_TduHzZa3HKq84Yk7TAoEbdanPY48u23KxpxtK2lRzj1WXzreCbsqFIhd-k5Xb328lv-0T0X0qlaZyw4Yhfkjb5nVW22J-IRsFOhPRYyhjFPX3gk-MLIMGoxiKL8d46h5rJ2opUwUm5YOkb_l9YhnvGnyaVYuJxpl9IMEOqJy-_qpKYu7HhbCFIlwQ5J1JpvHwetfxudbEzESjWNPhQOTQ-i7jwswpIDRMJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازچهل‌‌نهمین‌قهرمانی مسی افسانه‌ای تا برد پرگل یاران اسپالتی در آغاز لیگ‌اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29980" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29978">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📊
عملکرد بازیکنان رئال‌مادرید درفصل‌جدید؛ امباپه با 8 گل‌زده و 2 پاس گل برترین بازبکن کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29978" target="_blank">📅 00:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29977">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqvBV73dbL0zNViYwlthe8cal2QbBSCXJ15ByrWVHE3CBHKwP6hkF8eORmkDWrcwXcclFOh1q_zY9u_Tk0OjTQpfbLPlE-InVDcsP-1OLYwwukrxmOHdgr5NktirDivp6Phb_Cg0d4n9y690VEDQWyTmJLQyJNWlk7x41XaCoWtDoe-SD0Nl5n9NXGuPLNYJujRRzuGvmaGp6oyyS5NKN9DeC7mhr2Yhysv21JTa2CSBwtTKz95z3ucwrwWl8PCYikXeOa2Xc2qUapXborfJoc47QSaXQQnCwCYJ4T8n1cWAXcNUWNhat8u3V_yoJ_HaEX2G2W580bdMkwiVyklqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29977" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29976">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTfrmtrl4vM8Tug_TztIwFfSoioRT-4gJcboM6ApFgMoayfpJlP9T1nUhVO36g47_UcmCGlIrmcvlOJu3Qv5285qgeLXn6l_oVwTfy-g6H3UVTrGUpJGyvJqss49F6pxfOU_T7E7UKCl_PZSmvzn4_7dbbtHBVU2p-5CsQ0ToTDISykKoK99bZs-0Yu3jdoub8PfU3OWxMO6yPpxK08A_BeoCtW__Fm8_0T0nWvoB2wxzzuJKuw7sq7ZJKpgBGrtm2M-Yh8jmjJotWOh3a1Gv76FdIHN7Eiu2On3JMkqR_vppZlkdZpt7nkpTdo0tooia2_3Hu7_3Fik_I_SKIks-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29976" target="_blank">📅 00:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29975">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMknuGkTP2wbfAhm2C7g8JmkMv1byQ9X6zEei5CANws5PZ7ToZBfglYakuPSS1lv25I8J0XPkprfzCTYdHk43rYVWK3Pcv18Nh-yoe3WCykstXkdZPUSWH_7Q3D_fj-7EQzPUwHDp3Sqdrzs76mjkgZu9_rN2Zye8q3JO_zZ57SQbZ1eaqF0nlyPr-XZ6Y-HpdrFTaZBceSIF-lFi59C4UQ_5EzdDALyxHSlobIFRiDToyRxAeMKVnIItaYQmiFdICWhGLhu9e7RFKFyDCef-Wveyyo1Ajqrdz3nznqvweX1PtDeWDLpV51KhuTVlCbi0rzKBtImkQVNuiRKzizqyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این پست برای رفقایی که بدنسازی کار میکنند؛
ویتامین‌ها و مکمل‌های‌مهم برای وررزشکاران در کنار یک تمرین خوب برای ساختن یک بدن حرفه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29975" target="_blank">📅 00:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29974">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te-rJMyBKGvGI7HyjSDTifZG1cDd2UiSPq4oF3Ok-J4TtT_I8gd8afDxk7aF1-rGABhQxhuh5ieR1bcDnrQ2bK7eaWGwbIoao5OsC4Ckd2nSIp2Qkg2bk7uef7t-Cy9XLBewKJqFg2x0vSnnhv7-clbdrhlrROZ3OHgwYQbodPgHcH4I-Co8LIh9qG4shZ9z0SCRalSFExYUTrbf0vbbnxj6o9mhxTdXf5hkBUN2_BTqhuKwwC1KGW4ddWR-eZ4J4GP9wGcxY_yeqz3snr2_re2KDyvC_bAkfZCcenR_V3MRPRVqgdIC1cZOpKVRsT7jOpoyhc5sixwhKENOuRmgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29974" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29973">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzlFOiraGfiyxW8E08N1eZJBBLfIpblYdJ3O3Op6OCKd6ke9Zl_CoxlpwCjg7wP5hf1F5Na8pZgwB-s-GIjcWANGTjuupmTGgexi4H5DI9E0V-I6KVLOvavzTy-A_O4h1oYy7xryRjgQnYzBNx3Ggc3dPbVG75DzJxVm0ektS3274yydr2_XxX5RzrrNNX7jZhIvWgFHh0NSihfKKTj8dFl1li1oV27DnF2e2eh-FHtytwPtmmAwwOl4UYGMVgJF_dHsZExhmuEuOblnq_QYFQ9DB7vUzZ6gic_2Y3dKnye3wxM7zeSO4f8Ix7KQnGi6aNu_Jnkstq1ZTC1ROFQ6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN
: درصورتیکه‌هانسی‌فلیک امسال تیم بارسلونا رو به‌قهرمانی لیگ قهرمانان اروپا برسونه لاپورتا قراردادش رو سه ساله دیگر تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29973" target="_blank">📅 23:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29972">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7EeTuEtdslbzBZDX03Y7UQ9foWO9-9J5q83dWSrePS6Me8QOosReptheIMCe-XkRKqzxV_hwFQWB4ryzOXXJXW2g_PgXpW1JdLmhcdeHl8TJ-TqikNQAMCJG3uBWEDvz6gmycQ2s4ZPcuCytYHMHLuoN1w2DEfX4W4AEfEbv45luxqyJyMK5Rs3FehICTZiH6o1U8FPAxFOAZwsQBVr1tQgoxnGjvFEx70EQvZoEeU_-3Y_naH035LGNAXWTTNwyjMToCaLDBuQ3WUYEK-V5pqrvIdwnJtw8X_s9ZkYIpaEiunWvNrNA2Ocpt5HIOyrlBnH0RvX9W3y7FLS8CZ8Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29972" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29971">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDWQWnTC5AijG7leQZXMJADrD41r0i7WqCVAVPGDAbNWjj1rZDp31AYH7Cj8ssyXhqjdGKRYzsKnOr8kaQvKW-hYMLxUrNpb2Ewd91-v-AcfQlX1FeXVWDWWKD3ZpdsYUQqUjKdZKlR0FCMble2Yy-bFmmYgKuZQBBLIv32cTxa_gU63BB4EMpfjY-JubUMqIi6j4KZVDAlGVER5GRC4WirxeZR9G6RCRf6c6An2receta6oAqTxuTJoAployjGntW8NXY4z7GeqfYrYh6GK-edadzID8oADF8EDcsZD-3u_e5bWzsnVi3P7IF9yL-S4zN6k3G1jjfDmX-7WB00PbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29971" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29970">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1O_n7gsM6i73sLFilztJ_iJcCKQ8Pnk2WjX3szFwcEysl0WAub7xG18j7KACKCQ_KL0mGYZWPedEFmwNNClMOoA8n9ACCPOmhtsLT4UEOaGGNA2v0xwFcrEl1mEy32G29jdW7LPXexjOvEXU5Vdvct2W_4earSWniKTjLk8MeLixBHviEZi9lWqsTkvjnj8VtHHFBY3ILRx3x_YN3dfnPq3Dx3CNWjDVJUTJQ8Spjan6KnFbAMqHVKs-5xjq7vd_1K36LEVhMxRIPon2Namjskiit6MakS7ubN0Av2ZzEKTtvFDKGzcsOuVBe3vTjsCq55Z7SFBITMyDXHJqqsN9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29970" target="_blank">📅 22:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29969">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=XyCPlbc4h2ckhkbbJv9VGGGfTgGiEuJEVWWQZHil1id-INqn3tzQOn3Txjy0Nfzt5ZNze3oKEPOiI0palHtYy-MeYpaR0gcTiw28dsbqizXCcy2uwFTgcum39R3Iv8MDXW6VgoEHriBDOM1KOi9sQx_5R1d1VxhcMlIRCK-KGRRKHkikE3AXynH77dqgg98xQKP0wEXcU1mYTZfmqPeiKvQTTOCsahCVkLHPy5cnenTF5as8s-aS4Q4blNjGTAMwginFE9pnHvbdLtOcb-aE_EO5LktjcjlRbbQxfWRodrj3z9zROuy0iynoIA4UxnkpBGzfppawYUfCRkGveuOvww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=XyCPlbc4h2ckhkbbJv9VGGGfTgGiEuJEVWWQZHil1id-INqn3tzQOn3Txjy0Nfzt5ZNze3oKEPOiI0palHtYy-MeYpaR0gcTiw28dsbqizXCcy2uwFTgcum39R3Iv8MDXW6VgoEHriBDOM1KOi9sQx_5R1d1VxhcMlIRCK-KGRRKHkikE3AXynH77dqgg98xQKP0wEXcU1mYTZfmqPeiKvQTTOCsahCVkLHPy5cnenTF5as8s-aS4Q4blNjGTAMwginFE9pnHvbdLtOcb-aE_EO5LktjcjlRbbQxfWRodrj3z9zROuy0iynoIA4UxnkpBGzfppawYUfCRkGveuOvww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29969" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29968">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=mg39VpnKgk9TuT3hDg6hhabmvULbcSa35741fVrRnboG2wt39KXBQ2Lh1DXRspkKA4HeSfgSNJoyZlFdchXjtZYUsX9bmhrk7DJ_mPCxtYWk7kH6nVX6ayTN6f9u16NOWLU4DI8a__9NZRp7lfAP6V-O_tEp0hJKtH7k5NQyjnvR-aPJDssULD8GFo883y56jtiXPZq3X1Oqj5Zpq6pXBxOrMHF7AdXkKpnsA5a-NpZDUn9jvMpHGeZYBKqUWZShX0xW_sUyEvy4hknjjZpjbD_yJauVO8d84zp0cjk3F3LcQZA7-U-k2QKEpiS8uSRi_XVItV2hgMDkZalJDOXmUI1wWrhG_95cqg4t-FiHb2HNVxIe5SBTPonzz_ZOhh4ixqmyyi1B_T6NGd6IfFApKYN9_1m_5s5jd9BY3cBsjysedEhFq8SI1SJ7DqlHjYH6S9Rv9qqD9NoJhFh9SwOHxRdBwp4ZG6OeH2ueraWNytcrmD5NDLfhBpw8ScIdWJGWHPrw6E03ppqJxFqMbIzGe2iGwM_aTUFRi3vmDMbPyGs8-Jw6iiGkdB7OD_NrdJSJcRfVubLDnC8Xmm5g4q56seRj04VmTPqZKnU687AmV_LoINvKEuyDyt9NUAjkjhD4yEdj3wfZXd3jvWUbMUBHSGySPLhZUFhAv-xkRnDNtso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=mg39VpnKgk9TuT3hDg6hhabmvULbcSa35741fVrRnboG2wt39KXBQ2Lh1DXRspkKA4HeSfgSNJoyZlFdchXjtZYUsX9bmhrk7DJ_mPCxtYWk7kH6nVX6ayTN6f9u16NOWLU4DI8a__9NZRp7lfAP6V-O_tEp0hJKtH7k5NQyjnvR-aPJDssULD8GFo883y56jtiXPZq3X1Oqj5Zpq6pXBxOrMHF7AdXkKpnsA5a-NpZDUn9jvMpHGeZYBKqUWZShX0xW_sUyEvy4hknjjZpjbD_yJauVO8d84zp0cjk3F3LcQZA7-U-k2QKEpiS8uSRi_XVItV2hgMDkZalJDOXmUI1wWrhG_95cqg4t-FiHb2HNVxIe5SBTPonzz_ZOhh4ixqmyyi1B_T6NGd6IfFApKYN9_1m_5s5jd9BY3cBsjysedEhFq8SI1SJ7DqlHjYH6S9Rv9qqD9NoJhFh9SwOHxRdBwp4ZG6OeH2ueraWNytcrmD5NDLfhBpw8ScIdWJGWHPrw6E03ppqJxFqMbIzGe2iGwM_aTUFRi3vmDMbPyGs8-Jw6iiGkdB7OD_NrdJSJcRfVubLDnC8Xmm5g4q56seRj04VmTPqZKnU687AmV_LoINvKEuyDyt9NUAjkjhD4yEdj3wfZXd3jvWUbMUBHSGySPLhZUFhAv-xkRnDNtso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌انگیز و نوستالژی از تکنیک برگ ریزون نیمارجونیور در دوران حضورش در بارسلونا. اونقدر خفن بود این پسر ویدیوهاش تموم نمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29968" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29966">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shIciCMgTp2EkaDQNVFW8kPYNJdcN8bjJPSYRsuXdt8EZ039Pct6OvHvQkjgOqQjHLdyOcEHNd2_szM-bSK5MygGMNBpaNKDmJkrd6wp0bOj_iI5-Zy1rMaNnwSryq4fKacYESBvQx907qN_jQsT9lmF45LYbC__M-ouO0tPFiE1KhxiyZNspcESrcN4qZo_hsgA3kytoIwCuROGYSeau-1jguJgIvFatP1PrrBVHA8wIsR--4Zq1O9cyR2RaVntfAtbGO_pUCUMfg-Ff69VUdYqOpMBhp0J-MON5dbMcXnmLAh7JWZH7aqcWxRlLsSicAhECIolXhV9EvfWdixocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29966" target="_blank">📅 22:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29965">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeKkenzKnhUxHNxPkNB9Cqt0JI4-vkOtaJum2nNvjvzdUzu8FSZxwUpJrtsYBZRjoNIqj1xqw9F71Tn7ySR46wKczaUEK1SciqARhhq-K6EXcGidrxOMTjwOXSObYbnkCHg_n9AVRL6iuXjhJ2SBvwahAsqy-SxKwPh4IEWdrmCQa5CL4yTS1yvb3eVDtVj0wboYDo55TWN5MMok_JJCEAdT8Ans2qrijuwuifxxbW1Gcl7dTnL86inD14XjLalaoHZF5_STX2Ea4nUUzcss5QLaLN-zuupcvT22rLEYIVR5BeVH62oXXakwpgeNNWino8utpHNxds2wIytBTFmSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک‌تعدادقهرمانی‌ستاره‌هایی‌که‌بیشترین تعداد جام رو در کل دوران حرفه‌ایشون بدست آورده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29965" target="_blank">📅 21:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29964">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAqOkiAmQXBJOdzE70U5sFn4pu8NXPVRImcOXEr4fue6cALX-HNE63LRh_pcoEOK7w9SK68srY7Mwq6YDM-3AVceg3jSJ_CqasHZrxu1EyggUEpJru-l6UseQ1yk1IHCclLKb7oblMDzQkm2XvuUc24mzjWXCsr46cB1QefnM3I2JS2riWOg-g2SiD8nHhP2xHQ72Mw6Az29vIjKSCnIbwAFeDaN0UMqqTlcdMM3kRwiub6kMUlhDW8PA7a7YXNecvfLlwW4nNgq21_ymoHl7iU3SDzpoEiRW-q5Gos5Z5YOpLqxZ2137l8OMOrYhpBWfWLcxe5RWXGDnuvMd91jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29964" target="_blank">📅 21:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29963">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8G-bH2JCpVY89MPXc6lCPRFNdfRr1qZApVRo5flLl5Zhwy4IOkazoFBQY9zpQ9bfUfocf1bCxbvd6ycEP1UMu_VPNrwYllOvyupYG0z4dfSeKSQ8tO2B0fOPaNbOQ5VyP-fVeIZftngI0MZrvI-CHPvAoCJ1T34tYRV2TNMYByagC9G2tguYQIDSaftPh88575Wgpq6sZTtLN_SVStRfWb7Fwkf_d0Lecytn3NDwSZzekSekMnmRmiyHmgVzy-3c0ykvfLBMRdMZ_Z-woHMUn65PgZHNXAf8Rsn00Gi-5lM9q3fOHCnoMXsdUjYklOvWVxqnbWHaF0AUQd6jdRTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضا بیرانوند دروازه‌بان ملی‌پوش تراکتور قبل از اعزام به خدمت از تیم تراکتور آفر تمدید قرار داد سه ساله‌دریافتی‌کرده. درصورتیکه بیرو به‌این آفر پاسخ منفی بدهد بعداز خدمت بازیکن آزاد به حساب خواهد آمد و به هر تیمی که بخواهد میتواند برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29963" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29962">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlvvHLMvPoWI0f-a9w1mC9W0IQF74SMF0NWztYQ1izErTvzhlW5RO_In-cpVZKDPmj_Fr8Jli7nv8Z92mtpGjcxkuvfxA7Jue-oweGE_uEfeZ7JpVhhcO_PAVE5THqAgu4VCFtU0KOvDmdH2foqtwfiqP6Lv66P-sW2BI8PJWEYHqZzF24CmqcYdfJNCzatdfD89KTMvC6V19LWFhUfv0vvYW0xOWcNducac1D9BRPqXgx93qQwwBQ2aRL5o2yRxs1nW_oyBVvF1qj0K4OxdbEzd43t830lgwZQVvGIZ-axHtt2V7B1pcNX11kUP4wEV8VNEGlPNuYE3Mo-KJzsDIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛ ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29962" target="_blank">📅 20:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29961">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLVsW1bELIvxyiHq9rem2jnWaWzzf5UEwSHAxtMEU3kvYv5HufzbrPl9oxtDXAp1TpRVsrqYZ5UfllCM9gEDvVaiQBsMGlLbIu3fG-S1V3BWJ3xmQWxW0FX-th0I0VX4WKU0Ewp_DT5JHnBQtOWtbxoPHyoIDx_P5kNs7V7wu2fwbcilsvPz3MAUMk8Y--WFjpzqS4KZSTCyMdoICbdlpLmI8vbq9Ru9h5DeZkQ1z6XrsyuX3bMKObHSBYEkKI4SmJnNc0TkLe3aJ8i5UfZ_QnTSI6SP4zYIZyA-L2frzAvv11TZeFj0siwKmkgH_J9285vxVzw12x6wjfnGttw2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگهداری درست از کنسول بازی، عمرش رو بیشتر می‌کنه! اگه داری این‌نکات رو رعایت کن و قدرش رو بدون. الان‌شده‌حدود 300 تومن. دوهفته‌دیگه 400.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29961" target="_blank">📅 20:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29960">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9FdaJa_KQH67dlCiAJkoEYBt1X2DZTUc1sI3CIzaNaB5wjvAvejkpTbTVfLXq_3GBSaYwAW_F9mCRptSbo1_eSvQUVYb0ksTDc-TRkEFthZUibAfWDh3y2J-hOrFQ9Km2lHAQBn2pdMSnUOmo31x5GlKtMdGIoPgwNnrkH7pKILa2np-sCikPv2PPliWHBmeZO5AGXfhKun-g2jz1aJ-28_Xm6LLFe9tEO1iH9XHYNjaQ7IFZv8RE-ZFR0xAOH7OlVnw_lBb4ofhg6KHkeOQfkgHZJI08dDRQeVwcsrPLMMr4QYwqN_TBB2HzmPpigyJ_rrfwpMB6tQ82qLTa1pCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29960" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29959">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVWZX5vhcpmJ_n_53ipQUcotKYoOjE9JIBb7nRG6eJ2uDFso9kFw4WF-zS_gndIeBDmaNfw9lkMUkxYLGXL0F2-mxhzSbiD483wxxl5wLbEt0SroAfh2LJ21E2-n6jOvEpyx8WlZ54ynkFYtQZxs6YGQbDhQIDIwHIa9rgyLXftBEYk70e0Tqjv7c8zZWEmiIf6rimWV_MXv8YH1J6ZMD2GAEbURbddbRWC-f_amVWv4OErRXdWn7xqwpYMnDOcGNKwqt9e0kp57FMZ9Lhsa-tKCqe6Nyf_pGYcxJDvnFNg0TcDl_wahMMU7hXQJMaz1Dsv6rReK-Vqk6ibz0LEgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بازیکنان رکوردار بیشترین تعداد جام در کل دوران‌حرفه‌ایشون؛ لیونل مسی با 49 جام بااختلاف پر افتخار ترین بازیکنان تاریخ مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29959" target="_blank">📅 19:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29958">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIUZ7XFRUtmiH-1y0Zeu3gXzGe41cJIqd9mXfdCDcpW3pgswQLKeDDhpllGo8BJ5HFfKsdxwNiwvJXv20JTgc4qrryPH8NzQtBuZNPws2n_yqsTcnd5TbJMRzfnlpvonM_fJVnlN3AoopKhnqfhul5Emeap1vRnqxh_VOzkjbjw4GB48LbdMUr8PkAWaBxvbxR0nYc3HhVvE_wAm_tR0fjojZ-tjuXuN4pZ1sxfypLB_2HsJ_Bm-yBB43mtihwNrsST6_zZSC8MvxsgFRAbSc_l1Qw_c7_NQy6KmHAN-d9J6woPhFwoundrexiAc3-WwvpN64nCe8B-N8uMzhMI5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29958" target="_blank">📅 19:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29957">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_IPZwxYJjUVP81YD6RE8Oqss-5nd4FK0mjo3XW7Ky37WXpX_Xqz3m1KhwuCaMbzrUEKNTJNqtbif8sWQ0m4JPN8NFCvFMVu3dC5Fh9tzmwHKf6WafVFIKmK9AuRelZeC82C4pv8s3a_lMBH8j970DFLQZ0ZTCEobJk4DdTJxCu36ZWtbVze3i-1CvUYXN8pxQVW04ApFs_tKctoAyuM7fmcKvU4LEgRkM2sIKE_klSMJ5Ni2Qsw1hwDK2X5i3AS0A79aZlW6Bl7-u9uVUrUaxX5dT_3hjTPuHXE8xwarYORrM6Px9K23WCLm7bgb4uTCkNpSB9MmCH8keFN5csIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس میخواد درپایان جام ملت‌های آسیا برانکو ایوانکوویچ‌سرمربی‌سابق سرخپوشان روبعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29957" target="_blank">📅 19:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29956">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYFriLMCgdNGpm0gnzc5CbJFoB7H7ELUKLv-O7s-6DTTcKTG7VOtQCVC8FjAbgow4a7YTu9S_AX12iAl9ZJY1d4cBrjoAAs3GOnFsBvRPWLJ4UFneWvp7vu2-EWIp_ho-mgWUwTZm8Q8UGVxsGEqOBw5S7GNqOqW151Th-EV5Vu5RNq2wTuLRmzYHNB2HTG97gG0C3v73lQz4A4GQAWPP7_redd81K3tEZqrh-6Qns4NLX8P0TteYJZu_RQ-nFHPanexqgkEz5envG_g8jegDmlg1Z2UouAL_VH1ZVLfPcKFLfike1KLAd6e9Djx0ZP-9o5ThX254UaE2rRpKmYwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29956" target="_blank">📅 18:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGdOveoWcE6VyhJYsu0t2S64r_UVVCbJO5NamUvCWicHCreCIt-OjD9NKrvhOZbACflEIGI7sX_7qjzqpWVVWO7XIM8G202jW8ylIHuXexeUEpvM1a6LoLCsabvhncwF07EnN6NYCOjokvytErjo5pQwPGro-paaHDgwkQvi7nqUYBnqwczi62YC16chnW1Re3Gf4nqa2cNyLSt1GZTDGqYpvKfgaX_CZFReoFngJQPtS8QkfjHf6VYew4MYTJ2lkQaUyfyVRR2WHBUmdl2Z1UiGalVMz-XaYFxRNK7BJ1ebV4-XgCjNIiDEEbK8pfCVYMT3uQouGOvh1fDBZA-9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ارزش باشگاه‌های لیگ برتر ایران براساس آخرین اپدیت سایت ترانسفر مارکت؛ پرسپولیس ارزشمند ترین تیم این فصل لیگ برتر ایران لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29955" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29954">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=tMxMR1Pja7WQ3_bKY7umTnhVTSzNLcOQPtgFrbUPteXWbAUUInvSq_lyfpRWeYJbC9WoOLYhFqRB88pBk0x9XxAm1-_4AVOkVhuWGE8kZZxkqph5SAMBx-0K2aOj4TqCmx7en_TuE8KO2laKXij_eKA3OYL4UpY0MumpfoJC_Z6VsUQbh14G2Om9KGIKl7eMLqdFgfiH12-NkbR2wCsYdTU6E94pQEWcC7rhWy-9gp7DtS0pIHtlAi62GIANS_mZJnEOmGByDGZZBXY6sC6R1lUTiMZbGIR3bWI7I8_t6ByF8t0gTLQ_HS9BW_HZXou9DY-nu71piV5IEwLhLwm65zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=tMxMR1Pja7WQ3_bKY7umTnhVTSzNLcOQPtgFrbUPteXWbAUUInvSq_lyfpRWeYJbC9WoOLYhFqRB88pBk0x9XxAm1-_4AVOkVhuWGE8kZZxkqph5SAMBx-0K2aOj4TqCmx7en_TuE8KO2laKXij_eKA3OYL4UpY0MumpfoJC_Z6VsUQbh14G2Om9KGIKl7eMLqdFgfiH12-NkbR2wCsYdTU6E94pQEWcC7rhWy-9gp7DtS0pIHtlAi62GIANS_mZJnEOmGByDGZZBXY6sC6R1lUTiMZbGIR3bWI7I8_t6ByF8t0gTLQ_HS9BW_HZXou9DY-nu71piV5IEwLhLwm65zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29954" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29952">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhvrYxCpoBS0F5JZDmK079DlEhhLstg8i3-DOC3JBGbxqi1Sq3rb-iozWfQNw9l9UQMqeX-9lXAt7QTrh1v_5g44z2GFMNsa7zGJ_uqi7lJmu0eulwkOSUjnnSQgZvzLuQB07Ru8GU-IehDKz5DQPbloWkpxRo0vpwPJH-P0C3BBcBfj-y8VGlmiqUZrhKxsSBZZ6o6a5J6dXsceqmOTCB6DDHz2OaOQxytPtZr7rzHutI9OZirqB7WCKYkMUVkUC1Z9CFyq5n_RCSsPo5pAGsMLmoAeL7Br0pe3kU5x1m7u5lAuMAA9aq4dHEApidu2uiL1w3rsJv1UQ6kCwxW9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29952" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I52GI14jY7o9USALKHNUtF6mbZTbPNVp8WFNSstRGheWIEXOsguFzPT8afTehz6MCClyqIkiLB7k9fqlMWnO2G_HRlvwbNsBYw29h49l1T9hOih3QIU5BcKO3k5Tme5wwjEa80wsCPfLY6dlvZlJ0US-fQg0AyzbPpbq96znBYPkYLHvVSKqbK1OU-zxPKT42s0Qjg2ODgMJJA5ZdNseYocqk_9HfVrXFI9_Nvgxcr2sgjMXuteou8jhYLFVpjf9CFfPbhhB283mlv7JAHG8XmAqypZI-56jfBo8s6UhqK98KYKLnZPesTUugLPaCPM1G-wVNE_sgvOBMT6PNBfGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌سوپرجام اسپانیا
؛ بارسلونا و اتلتیکو روز 13 بهمن‌ساعت 23:30 به مصاف هم میرند. روز بعد همون ساعت رئال باسوسیداد بازی میکنه. برنده این دوبازی مسابقه فینال سوپرکاپ رو برگزار میکنن که روز 17 بهمن ماه ساعت 23:30 برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29951" target="_blank">📅 18:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsgnjD4kqKgS-5a5vkynTjhxZOo7hHNB7qUFPF1B5HaH9TLCuZUSLhc5VKpQda7gCvEx3yiG0NUrtMrcTAHgUuAM994nAmqcAJJ_9zNCZk1Jn03fFJqTzkZMA5wQjfSIZyOqCCICBNPIXJHjDmbf0awLxjkmklsQt00OQ3cSuOcX7Bi7Gf2toOczAlpVYyQh1NrrTHzKVrCdcn1hxxX0sbhX7cL9TDidxSVViJuKF6yjM3wOhpJ4iGg5ipS9MuA3aKj8SF-Kns11UZfyvDM3TFDh_AOpviyAi9STK28LDRr-FONFkGHoA0NswVIGjbEza_qYe9IMAlBZSiBuyP5N4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌پیگیری‌های‌خودراانجام داده و در تلاشه تا علیرضاجهانبخش رو نیم فصل به این تیم ببره. جهانبخش از اول دی ماه سرباز خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29950" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeL80zM8msVZ_u84Z-wnTYXJA1HSJ_-SA7emIR0uIeLeGn7me7f8D8jaeqAFLyaT_p9axRIJt395GvUGS_5LgCeisbchGkawRlKmrtlqhyRtg543vBt5Za_lRUA18lfoVmNFhDvaAJd5FTUU7xTdZkGk2rNaJKDw10bUJe9MQ0tqwbHQKJJQJSkoLxg7CSImPs1_I-kRXFJW6hrwnHfXjUNE2VskzhNs7UIscDJ537JCFhnPpsCZlOxhhtu6Ij29NfPOq-bXEtc5Rzxs57MzH_AgYdJ6tDu58TRr-Do24m0rSLjhxCUaksJBxLZcfImZ_R2kPzcAWdGTrTpbtR9G8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29949" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZa3nVAJk9CBYBtIxjVxSTC9_k8LCVWeI1U8jyyNnWL5cMVd2uwoTocFUJT-kcIpuPY7c0apicSjNAX3RP9SSF3jWFEZm-Ki3Aen0H6lTpmiqYafmnRJ8Mk2a15QMV9LRDgw5ar0ATtiGXLUVoU0GfQzgccWnlv3sqMuLmJbCAxPSjFxEpgmgy1LRsJKjsCAvZotJshuR4Mj3gW5EgGRaMrz2WtKR9--ez_kvAuwLMpgFbJVAj72nub2u9dTqewTfP53ZIjLoBwz5Ti85fsaW125wk4PoGUULKghBXG4OwmWIrn_-B8W8gmjEGFdszaibqLQjfyi7VLR07fxncjRPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29948" target="_blank">📅 16:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29947">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgrSkFqGgrHN5GQ3vFruOERysx_7AZGe5cCQBERUY5gu3HNrcpPRC1gkjDbeF8tTHIaQWLAZiXYrZ6Qv0F78dif-Vs3x6IylHdi3i6MuBNtwOpBKIfXvEmvFTBgBEZzzvGRmrLDPSscBfcDwun7p8lx-ohqQ_HNZdp0OiJqR8a_GgY_Qu26HUSCWSJD-4rTcyAjWEpPCiP4JiaV1naEQY7ClphqXe6m-l3Hm02CpctUf2hC1ukoHJy2ZaZKgFG-DrGg3f49eDbctun9dY06FbAAps_jEyBn8WJQMUwTDmZrWX-jKo6QeFaR322t0wM_a__ckfsCNQ8iY0mjh1VUEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یک‌ایرانی‌مالک‌چلسی‌شد؛ بااعلام‌باشگاه چلسی، شرکت‌های‌گروه سرمایه‌گذاری Clearlake Capital رسما 87درصدسهام چلسی‌راخریداری‌کردند و به‌این ترتیب بهداد اقبالی تاجر ایرانی مرد اول چلسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29947" target="_blank">📅 16:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29946">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e07abed.mp4?token=q0bS80MgOeRCT22Gg6wJ7FmSJFz0fXzz8CSX_ap88xNrFGZb70me1HOkXEoVhUErX0m4fAiH7o_pHeNXq3qvpzSP6jEsqFpcb30iCPippdNoM1N5RE0r9jOoZtOj5ClrupcVb0OjthkF4Kd2dt0X134qMsIVqVsJxvI7NCZTVtUygJ68Wvdy5IRk_aqSU67uFNzJq3gXWv4P52PPhlIu-_38GdhWpgjJvbV-ZRRe01sLtUlz_FYnSRuFmYW7BizQQWuNeO7yxre3r-_aNyaorhtA-iMyJXVB7nQgm16WLibbI3hEu5yUxvb_E0dstCQ9MfzNIfGpzTdrIUb4fVwB4LCRANfTkXZQ98d5PoX6tu00AjC4m3KbYQcGb8q-sdjn8ryag_pBPoCqWc6RelbUJ2qVzKPZYkJsEXfdUU9ZRtoJgDW_Z1gB7ElA9UuY4duJabHEe91IdKkMpjtRHjE2RHHZrkYspd7JgAONcZOTT1CKzo-jFpoY5esVq78Qk_i5MnVLmwZIXuEyA4KOpUMkJFh23J-a-nS7eJFQBkpkKxMt-9p-CFZNlwDVSSy7goSe_msVTN-SYU6AWN40NdgGs9JWFnfjKrLzhlAvc83QftuXyvhfPAvqClgxobNE8Ve9bGhsyWHezkS0lsvJlb6VxaqfFJTxRLFfDQIMqAuRXE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e07abed.mp4?token=q0bS80MgOeRCT22Gg6wJ7FmSJFz0fXzz8CSX_ap88xNrFGZb70me1HOkXEoVhUErX0m4fAiH7o_pHeNXq3qvpzSP6jEsqFpcb30iCPippdNoM1N5RE0r9jOoZtOj5ClrupcVb0OjthkF4Kd2dt0X134qMsIVqVsJxvI7NCZTVtUygJ68Wvdy5IRk_aqSU67uFNzJq3gXWv4P52PPhlIu-_38GdhWpgjJvbV-ZRRe01sLtUlz_FYnSRuFmYW7BizQQWuNeO7yxre3r-_aNyaorhtA-iMyJXVB7nQgm16WLibbI3hEu5yUxvb_E0dstCQ9MfzNIfGpzTdrIUb4fVwB4LCRANfTkXZQ98d5PoX6tu00AjC4m3KbYQcGb8q-sdjn8ryag_pBPoCqWc6RelbUJ2qVzKPZYkJsEXfdUU9ZRtoJgDW_Z1gB7ElA9UuY4duJabHEe91IdKkMpjtRHjE2RHHZrkYspd7JgAONcZOTT1CKzo-jFpoY5esVq78Qk_i5MnVLmwZIXuEyA4KOpUMkJFh23J-a-nS7eJFQBkpkKxMt-9p-CFZNlwDVSSy7goSe_msVTN-SYU6AWN40NdgGs9JWFnfjKrLzhlAvc83QftuXyvhfPAvqClgxobNE8Ve9bGhsyWHezkS0lsvJlb6VxaqfFJTxRLFfDQIMqAuRXE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🔴
#تقویم؛ 8 سال پیش در چنین روزی؛ شبی که پرسپولیس، الدحیل را در آزادی شکست داد. 26 شهریور 1397، پرسپولیس‌پس‌از باخت 1-0 در بازی رفت و شکست 1-0 در نیمه اول جدال برگشت، در نیمه دوم سه بار دروازه الدحیل را گشود. سرخ‌ها در مجموع 3-2 پیروزشدند و جشن‌صعود به نیمه‌نهایی…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29946" target="_blank">📅 16:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29945">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUQAQNTo-GKQhIaDC_AzXXxm86MUQl2yj9IB_v1Rba5Omee3P_CLsDkXJ9_hkl0r5dh7FoykIo9ahETtREe2bImCv80AhGXXk1Vn9WtotLZs2vlyh9HdR2k2wwYWh7FT8F2sCQ1JW5ri-Red-xxiS0W441cVMwh2pqnWxhB4oymIJabnr1mSGRr1Pd0ltMLpljQXjJkZe2JqO2crGxgxQ0-djyREDFZ88doHRCJRDAfcC5zrC6oBeCwpHXZprH3YgQAHCPbTPwWkurG2tOD7WBow4rXcYIh2sMvZEIGTI92xf_PqnQ7bVn7UB5jd5f0iiyeFLOKCYyLYxhmR-xonkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🔴
#تقویم
؛
8 سال پیش در چنین روزی؛
شبی که پرسپولیس، الدحیل را در آزادی شکست داد. 26 شهریور 1397، پرسپولیس‌پس‌از باخت 1-0 در بازی رفت و شکست 1-0 در نیمه اول جدال برگشت، در نیمه دوم سه بار دروازه الدحیل را گشود. سرخ‌ها در مجموع 3-2 پیروزشدند و جشن‌صعود به نیمه‌نهایی لیگ قهرمانان را در آزادی پر از تماشاگر برپا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29945" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29944">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27095c80f9.mp4?token=vRm0nHHW5CEiHJttCrY_yM8CY9klD6iqa4bLF7EtZLtcW5j_cw3izIUjPMIGEh9ofmlIti-CzBGRNNlhm-WF45VT8bAC7JPZavGdlQH45hrc7m1XdMcqqJkt-hytUKI79lDNO8fNzj0RuplwL-ViMC6tkz-zRnOvN5hJuoHdYyOGg79x9NPBnRoxGIAaH4XKNYSEDOllCHI-BLts_o05zUsJDUQNiQ_St9neC86glwKqwSIF2RGE6ZqzyDnWe_Ux8aQpM8s2kzuLBqcBDK7pkLwbtgslkpkmK2MB3HjKg0MHNFkCAM-fKbyDqOEWcoOz1HxNa74p8LvpLYDw8wbCZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27095c80f9.mp4?token=vRm0nHHW5CEiHJttCrY_yM8CY9klD6iqa4bLF7EtZLtcW5j_cw3izIUjPMIGEh9ofmlIti-CzBGRNNlhm-WF45VT8bAC7JPZavGdlQH45hrc7m1XdMcqqJkt-hytUKI79lDNO8fNzj0RuplwL-ViMC6tkz-zRnOvN5hJuoHdYyOGg79x9NPBnRoxGIAaH4XKNYSEDOllCHI-BLts_o05zUsJDUQNiQ_St9neC86glwKqwSIF2RGE6ZqzyDnWe_Ux8aQpM8s2kzuLBqcBDK7pkLwbtgslkpkmK2MB3HjKg0MHNFkCAM-fKbyDqOEWcoOz1HxNa74p8LvpLYDw8wbCZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ خاطره‌‌انگیز و نوستالژی از سوپرگل‌های تماشایی و برگ‌ریزون کریس رونالدو در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29944" target="_blank">📅 15:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29943">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU7fEwO6-gDBYVDpxZqhmEhEkGegm2M_lAGdtGUZfWphcKfh4T7BDV_EBVbsboHBWsvZAacxCSVeu_rE-ERQQgjnAW8OyAPFzZGlREJMMeVdcLZ1v_s7cJHPEmiffu3QrbSctHcM2CEjZ3o5fU6LA4Oyv3YxyfKehHQIvGrlKXEfYHTkbTfbio6QRFXTPXTjqCXSsGv6Vemw3nxY_xQ3R_qHbONqH4DMbrUmlXlFmCbqnlbWEev1ji71jW5ozQvxk8PDumxZhFKjgNYwGu6UNqAQwHP44UR63AkT6XEK80RXacEookRLZrSRHitPgGoBSjWmY9Z74E2KseZIpzV0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29943" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29942">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXNcL1K4s_NQDrhHG5DvpePYlAa55tva6XyXmrc1Lcbu0hTIpl83d-2zzEscf_rNX7b_BRXNCTzIbQGcxWxWGOfdb3MHqmGqrVBeXA29CUzkwgtCP1C_RcQm8rJMxmTQ3YqljB3ZrbRftuPNJcwzmvvaW-454UsMGNuOBOHQefg_JaVhMYoLWujWJ5cIsGpCMRSnrjwycqezL4s1yESleClRIFPSUkwuLvYVhScPrWkHCoNiiimIsTBRFzSCvW89e_A4me9wJ3Ry227rdNyCREQ2PEoqGm-zcYMrD3Xk_EPsJ577BWRoMSB2tBk3mDtmvWxdf4saei9VAXy3VNXgTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
از 368 بازیکنی که در یورو 2004 بازی کرده اند 367 نفر بازنشست‌شده‌اند و تنها بازیکنی که هنوز هم پرقدرت ادامه میدهد، کریستیانو رونالدو است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29942" target="_blank">📅 14:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29941">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8NAwwCk4oVODFi-sP8rc1Y0emh_jlhicd-eqJrSsS4BX_vXbuhwiO5s8hr03tQ5NKJ-9p62vhqBKIWZ0SpiwI3BCdsEHdj1s8pYpMj1MAqzF8i0FHpQOUqzGNQYyUr3PZcnMFbrjRVVfaPygOdPkHFqse8LKSOlAA4mrlYUPEnkCiOvYkETiPFKq-DjrAnkt5EfDyKmNOTe0aL_V8jJBn-YbDZSkOKJvqQQ2zup0asKEWWhoUL7K2bMBStfGHuUL3F_reody4OVf3ymOSnQB_RPgr_FB6sdiCBPYGFv6fauJLQsM6EpoDkfEE99PekayCCWi8WkfU34xozsDWx4_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
باشگاه‌پرسپولیس‌بزودی هزینه حق دادرسی که حدود 150 هزار دلاره به CAS پرداخت میکنه و پرونده یاسر آسانی رو به دادگاه عالی ورزش میبره!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29941" target="_blank">📅 13:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29940">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GE8UG3dvsa_iAmjih7XSCrk5xKqeuvpPC-gq-e57DfpqIyBODv6nV0kreXsAsR4CpoefYewPRHkwg-YaYmwHsHh5KgHvb7IU6V1jlLASnXEyamLoo69OmrY4cXf3rCFgwo3n7_Z8P0UKckxMNAzG72Qq8UaosAwo9NHsOy3javQEdutPR4HokFzCAQwWywuWmN6c2AiG96StHh_w6QX3X_Uu59h3I67arwGFaGy_B5a-p5fGNp49PegLzOqr8c5ncMo6r_bgIxAvx-AGZ_KN-KYWnokMEhFMyTEQT2onO97LmXWistDNvj2hcXl1osbcmudxCBjtverw27kVz2l5TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29940" target="_blank">📅 13:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29939">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUpbDO8jOUHZSvjxrCTWx5VrxJQgJEBbqHnpq_tbXqgJIQgHzRVNA03wmTlfClqv3NtvUrBckc6qivLSpiIvb0-bWJuqRNoZZhaTrtp53_c-JKsWYKgIhAXb_VbPMT4HqjumNWC_tEKdI_FYG3FdOVUu6l-CaGqM9aMe8XO49nWoIq3KgLWz_gvJk0j0V77pQAiGhGtZdSUWzxKhDjZWJCreMhzo_0gmUhuGHwp-ifSR8btqd0Jkp3dWTZd1i-uNSTjUekkX3c9oAvsYhywGhxlcorPymURZ9eqm70feTf4a4fui7RerbA11Yn8G7Ob0dvHGTG29NohjBYY_5VgbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29939" target="_blank">📅 13:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29938">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_hAPHv8OxEJ6fgZsy-7Snuc30DWdv9vzzms_ZrKPUXtvwX-vnUMW4kfs_iWUM1yNOD4tbGzpKiR5pIe1bRy71o8RFz51tZ5cwg7ly8etWv2oZRJe9t6hvylpf8Pqp5fqqlQqyrL1kQgxJ_kK3vFASihrdMSPcwrrF_56LoQ1twm4neQBS5GgXYeRklo98k2yleo_wUTVSKqydeCLXqztaybWnBORyAme89qI_PFy4RyjxZlXOG6y-mAtl7OyRFgmF_hynGU0OzhEibi7JeiW7dZdOHswbdpmvXBIWsll-OMfZnNCGdsYBd_g56IiRqsBwdyi18Q3dOMUbdF-kNtJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29938" target="_blank">📅 13:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29937">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf13ecGFR5iyjnKoau6Ah8bp3JKux-MqJKZuXK9Na9RUR1iZMh5rZO2UUfc3d-DU6Tx84a4Byf078NLrgHTT3yHYOJg31L9UPClTsQKwu0jk5G32Rk1AhRaK1oNT_K902qTCjpoyIOA05NQ5sovt746Wl9HRYQiYTcMCuaqAXU7dp1TQgT4Yk-XwUI3Yz35zsF4c_dwgt5H55mRam8QG1tSKqP0oxxMrtLEN-spyIsCFPIDQMHrd5TYKJ4Ek-FQ78aPgD6iHB-c5LPDNJYlB8jbFcG58z9dE7dPo0ngC5ZWIfJAjG_YVEKCyL-M04lFO29fDHrlOzAUy_eFYPTok2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29937" target="_blank">📅 12:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29936">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=aDOKREnJPnzoujbXtBDHsW9LJ4ziM9V06ngYKRgosacSDFy8dqZ1OuFxLQWIJuzydzo1NmqYpJ-YkPJ3dEPy24WNAWlkKgOnyVS5Q6Zj4Ia6SFAiuiU3FtTR6kT6zuHf75cM2ueaHV3-KFyONPzd3F_K4SkYEV4Ztg0_ttCoK6LQ1sAutIDPftTWH6G6fHgjWOgqEV_Pm-YkbUidyG1EPXrkZ1rCWMVFDMxz6LvZQL6Mes0Y0qAWyIkYY_mxZ1IqX_IjoPs0yoCFF2miaV00wlLBT6SEoII57HYyo94ursNk_2c9tBV-MPCrNIjI_J4FJHFU4R0AUlF6gLc13V1W9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=aDOKREnJPnzoujbXtBDHsW9LJ4ziM9V06ngYKRgosacSDFy8dqZ1OuFxLQWIJuzydzo1NmqYpJ-YkPJ3dEPy24WNAWlkKgOnyVS5Q6Zj4Ia6SFAiuiU3FtTR6kT6zuHf75cM2ueaHV3-KFyONPzd3F_K4SkYEV4Ztg0_ttCoK6LQ1sAutIDPftTWH6G6fHgjWOgqEV_Pm-YkbUidyG1EPXrkZ1rCWMVFDMxz6LvZQL6Mes0Y0qAWyIkYY_mxZ1IqX_IjoPs0yoCFF2miaV00wlLBT6SEoII57HYyo94ursNk_2c9tBV-MPCrNIjI_J4FJHFU4R0AUlF6gLc13V1W9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
صحبت‌های دیوید بکهام مالک باشگاه اینتر میامی درباره لیونل مسی بعد از قهرمانی دیشب: ما هنوز باورمون نمیشه که لیونل مسی رو داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29936" target="_blank">📅 12:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29935">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB8KOlv37o_meXNmZM-DUnKjv4wBDwxlC0C1-hCb_qJRWiL3_wfbnVOLjc2ynnmJov_haDvUNP3zSNejFsVI69Dby2wcdqxEh6Lv4S_t3aFVX3MsreBv-hzVJL0alOddX6kT7YIhlZCKKTimaLhUrqMQzDngfGlXTWkrdydfVfua4BHHH85LqPtXLp-eQlrWmXFWMTqfJLeOmHb8RNabp8_t743YVeT6i6_MvAPee0bM5lRufJDT6vODmIJqqnrVH6Q9yb8dFq6uIhGjySanVEI4Grv7Jegyr_H6dIOJdklVLrohaGuN1JDH_WNd6B5lwqVMgOeUC5Pp4tKYz_4riQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روبن نوس ستاره‌تیم‌الهلال: کار زشته هواداران التعاون رو هرگزفراموش نمیکنم. اونا ادعای مسلمان بودن میکنند درحالیکه‌به‌کسی که دستش از این دنیا کوتاس رحم نکردند. توصیه‌ من به اونا اینه که دیگر نماز نخونند چون اصلا مورد قبول الله نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29935" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29934">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzWS-j7XKyaCw7NMb24bxGCJL_WcJvJWk9wn42XHuDOIssQYfHr8HvLW6Xb86PpJ1HR1Vuo9JEOF64sJwq9TQiOHR_ZIH2d55tD1tINvvUGEgQ-VTP4hBj7An5xoKE0x0mjtuf9ylCat1KuX1jjLeOiubpv7DlvjE4cZ01HsRDWKLuNLaqoLA-7wNBoj2WkIjq_M_jM0PqrRUJh1eU8aOLm49GiHiyrYIucV4dHUujdNecT6gtFOlPFUEKBFEIi02aoKzw9pb3nDzvI2iweqePvk281ezjnefdQykhnMqqnrfPUT0B_6hnDLrAUVLCirSVD2hwwpJWJAkGD5COAsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29934" target="_blank">📅 11:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29933">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIOsHyfnFllSbGex4tZHN9pxOSar5owq25TFWQu61qOPn5dW6tWEug2GXAvVMokb9VRddOFsQ3jkKGpxg3zsRF8sGBLRipTyB0rxZWyGsE7rNU53n4HBSfdnxrLkAb9iO-jM0wNe2O7_K7T0Nawy9ALrc01R7xDgdw-a8TvC8p8xj5AhJKjt_5P0Onep2V5gP0Kk5_3xbpHH1ijRcOMdDUuiALOQa19uZc3zfEn4PZiA5P91yWJ6nJ1RmNkVKgVCzhtGVB5zjUEW3iF9uzq2vsXzZhxl409R_pz9XI6-urwGtO6YXL-wQZrd_uDih2iWUq8FQkmppwsDvCxgFVEogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29933" target="_blank">📅 11:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29932">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQZgxVH_P129mqhFow49RKbqmb7csSmUWdHtAyacdGU_m4JFdUHLWmPTqhilFFpcCFW2MO5j6pFYFZdmN-jbSZ6aMwggYOfcB7OWh3MR-NKjUALZfG-jInmu3EpYojnvxJ0G1Aq7FkpR_LfDeJdJm2_7hxTXuwGHtnMlqyOJzMS7ffYuSWl1Qrf4OXesbNFgOOnRwM98UItcYw28DGfRnIwJ5chhDelwSlBpG3idPq2K5FoFwOjAsJJ_q1WEWEKnQ4e-omIvMe3q4c27cKEv1lMLM--7QK-nobvZUUeveZ43NaMcech4SmN4w1u6vGiAUVOmJT0kPTaTOCvSuQeKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29932" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29931">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr1Y7ECMqC-zs-g9gxdGVfEJ5O_8fPvIxe_ukGV_IThOa-kc_1aHOGagO3sPQ7O5rEXixiXJop4lOVlkDq4I1PRW87wb2zYVGUh92cCaKT-t9tYcHDx3WRgRMJU1X-snj8BLCxL5BrNrI2N_xZkK8pQuzW1H7XJOiV5xv0uf664IxkreFzaKbBaeCn-pFrxhJQDilsODqEKM8vA421z_aLryLVaH8_dZJ2iWjkEBmziRyg83XQ6pE7GkFgzCcOMWIzPYtMHHUACjRW7_49QyzCAwwwl5YOMdBeBCqhCTwXfXsTk0nUodGOsO1CFQudWr0jbtBTE4eAWLi4gGp4rSYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جی جی گابریل پدیده 15 ساله منچستریونایتد که در دو راهی رئال مادرید و بارسا قرار گرفته تموم بازیکنان تیم‌رئال‌مادرید رو در اینستاگرام فالو کرد تا نشان بدهد علاقمند به پیوستن به باشگاه‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29931" target="_blank">📅 11:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29930">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCzObsetP13FaAx9kedHX4MDs4PJZGB1hMr0B2yhkea3UXJAbDXBZLyB3EHZYLX7NPR85NYE6CaJSilawmqhTpHipiXiNpSzH3M9GSAxEPEMnStY-DW-hG216foMgB0GATDesSrN4_kKB0maEYuYbnA3FWU6ZbVCOnYt4dZ28uXmVvEme-4CnsdICgCRLRydQropg-E_JPYJ2Amu1YReTUaVh4I7LxC9Q5zlbnhIjnQ2Xp2Nsw7peLgVrVyqRCXBRsCZcovJTf-LxEN21kolKyZO-MmF4662i2GfLgDY1DeWQvo7Z-OXzg3w4wqzrOUEWmfSfLRRU7PplqO18oo3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29930" target="_blank">📅 10:49 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
