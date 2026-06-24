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
<img src="https://cdn4.telesco.pe/file/tdn0nNdQz1I-CRPn6gpL4ftYOHYtPunv4G84ObMTusyPIA4YKEfQs2t_CkkPj_bDR8O9lPJcotI3hyY219t-45s64ebtXNg2AbSICPhrp9E4lZfvz0hGPTDpcj-0mbriKuzbtvzlHoyA17VTchsYLFNA1kjh6kIgWk9SAP5y6-CC39pLAk6mUwEssv-ln6JqaTIcW7hw7mYEfYCSfm7of37GOErcym20yquEQHiRzkupaJUq8Z6InLkjz9vjjSHjDkQyXQn8_d61c31-GskcUv7n2Mm31dyhScHtppgiJRda2fQtiK4rm-UMzp7HPEA2PZe2FO0psAl7kELalLz-Eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 944K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 18:45:45</div>
<hr>

<div class="tg-post" id="msg-130046">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vu-1rbctnylFAmw1pextHFUjsD2jFp5gBqXXP0-XbMj6Rvul4S90EZ_CJ-eJnVx2CYcq2rWZuOlJDGRNr1mlcO9xUGbRC1RLerp3rGx0hLbI1NqfuarELLt0xvJLF82EyDaFyP4c8fywyuuq3-rA3HNPeyaeyrjqu6Skj_3YNkXEeb9N6ag8REgnh013uwpcoMZDt5bsW1D8bvt-KwHu2hLrQc0h7VSBmT7Tbhwk2ucYg_0kZPNCFIllCxdMcxrMGPtCsCxZ11ozoxHw5GXz28v6bAklnF9G4yU8qXF76IXLV168gPdTfF6pKavNY0R9iv5SWV0eITq0JmGfLyb6eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: داماد ترامپ به جمع میلیاردرها پیوست
🔴
منبع اصلی این ثروت افسانه‌ای، همانطور که در گزارش فوربس آمده، شرکت سرمایه‌گذاری "افینیتی پارتنرز" (Affinity Partners) است که کوشنر در ژانویه ۲۰۲۱، یعنی درست پس از پایان دوره اول ریاست جمهوری ترامپ، تأسیس کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/alonews/130046" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130045">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/alonews/130045" target="_blank">📅 18:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130044">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
تنگه هرمز رو با مذاکره فتح نکردیم که با مذاکره واگذار کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/alonews/130044" target="_blank">📅 18:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130043">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/alonews/130043" target="_blank">📅 18:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130042">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/130042" target="_blank">📅 18:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130041">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/130041" target="_blank">📅 18:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130040">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/130040" target="_blank">📅 18:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130039">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb4DJcmQUX7LLPzgTX6JoVIo-WAiSAi9D5a95BtUTvsXQF4aglYrkuSZs120NJHE_yGJOPUdV7Hk_8HK72BdmzzxGaOT_UoLmH5FWZ4X8Vy6ci-zRHqXYYuHmlA3he47lG0XK-L_ChF0TNw4D4ilZdqUGxaJTXmvP3nbaVXwaUe6tTd_LvCxeBhpinVUjMDhkBOPokum4XCFAHlgYzyiUmF9iJVRPGe-TB56aX5YN42JEf3Kcc6wIWaV1kB5ztprNOet5oMw4Lnx_KwfdMLR1GQ9ZW9diC7RD1Gm6H3-mU2I4FZpxBy0fWbFTRqVmIfaiC6ujZZ9gU44IEmQv1zimQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/130039" target="_blank">📅 18:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130038">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: اوکراین در میدان نبرد عملکرد خوبی دارد.
آن‌ها هر ماه حدود ۳۰ تا ۳۵ هزار نیروی روسی را کشته یا به‌شدت زخمی می‌کنند.
این اعداد واقعاً شگفت‌انگیز هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/130038" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130037">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3c9d8282.mp4?token=RrREUHoJF1yngg5DOgpYIZk6T3kBFihNuqNmtE7LHlctlBoBHIUM2tLERqXQRoxkoBwx9n6riG-EIYUBiddtflnngx8FJ009yrwRJ3pJFH5bSKPqu6NkEBeTBUsu05Y7JKskowVqiRlkw0jd5SCDdfCuFN_oEZR3j_HwqPyOQ5JBo6GUQOqbDE7RVA9d-fevlc1lYXoWtJ-LW2J5dUB35im1jlBNL3pEk2B2V8QKSmCOKCxrrr12uSEIsQ6s9v4PUOu5aqGV5ar2Uu9BR9tjRQjlhKMWVuiY3OrE6-xqCTviKKjSWHGgteGYyLQ2aK43izao7mwIMF9A7WNdUMWMk4IJPD5dv0PqT3A9HM8baES50x23rc5gwwzaBfExqn1DqVsgJSyvo4XQLN5MNDjlI3-KEZLQwtH-WSuwS6aSbDbdBFgKspUahX-zM7lWFqpOENIow3TvxkvnStG3-LqMS2XuAMzP_Ujwm4RocThDKexbd79uckaPmDtz52-m3XPpW-HGAYcKM8ULiegm9Ba_vpeSiAM68zmi0-Dr7cbE-ghz6LmjCBtl2en8RGCbNzIG7HOZPihd89dOJDBB5wOPjyTT6QY5PjnLkOvQH_jBXrdriZh9t9VZbG7PP5xl41OOSCLOYxa_c7D2J8zL2TIvhrKyWEUQ7bg_BnnSQJhv3VE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3c9d8282.mp4?token=RrREUHoJF1yngg5DOgpYIZk6T3kBFihNuqNmtE7LHlctlBoBHIUM2tLERqXQRoxkoBwx9n6riG-EIYUBiddtflnngx8FJ009yrwRJ3pJFH5bSKPqu6NkEBeTBUsu05Y7JKskowVqiRlkw0jd5SCDdfCuFN_oEZR3j_HwqPyOQ5JBo6GUQOqbDE7RVA9d-fevlc1lYXoWtJ-LW2J5dUB35im1jlBNL3pEk2B2V8QKSmCOKCxrrr12uSEIsQ6s9v4PUOu5aqGV5ar2Uu9BR9tjRQjlhKMWVuiY3OrE6-xqCTviKKjSWHGgteGYyLQ2aK43izao7mwIMF9A7WNdUMWMk4IJPD5dv0PqT3A9HM8baES50x23rc5gwwzaBfExqn1DqVsgJSyvo4XQLN5MNDjlI3-KEZLQwtH-WSuwS6aSbDbdBFgKspUahX-zM7lWFqpOENIow3TvxkvnStG3-LqMS2XuAMzP_Ujwm4RocThDKexbd79uckaPmDtz52-m3XPpW-HGAYcKM8ULiegm9Ba_vpeSiAM68zmi0-Dr7cbE-ghz6LmjCBtl2en8RGCbNzIG7HOZPihd89dOJDBB5wOPjyTT6QY5PjnLkOvQH_jBXrdriZh9t9VZbG7PP5xl41OOSCLOYxa_c7D2J8zL2TIvhrKyWEUQ7bg_BnnSQJhv3VE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز:
۵۰۰ هواپیمای آمریکایی از پایگاه‌های آمریکا در ایتالیا به پرواز درآمدند تا از عملیات Epic Fury حمایت کنند.
این یک عملیات بسیار بزرگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/130037" target="_blank">📅 18:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130036">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95dd83e81c.mp4?token=AsPraGxAGnlqJGE5qU-57zAiJTyI4bOUe7osjJBuktFgzTR3VaOb9K_hNAolXSs9VBYtlAL3c_326_qOaZOXxRxM2NUlzVFPyXKppmv8hmhDDIhof-NUBWPFBTz_rXTumb4qjIeMhdTlHWSMLq8z1IEp79HRGMjIvY6gUo4zLIs8se2xuVrRczf_vbIVWtbyN7nZbEshVtmUBjOEXbNWpqSzF4e-my4EdVUINIRfYaJwvzFzFc5EHTCE2NtSzIZGA_465CW-0-AqXuelb2DgIITBlZsEWRIfAVqDaXQYjelSknZpL4BMN_Y5qNsRb5xSr9I3CwQ893cZwnScKAOqXrA_g2d0eje_SPnbLG9TY_YC5xZOfh9oa6LqLgH_fuchXnJTC09qBjT0zXB2HeTBZ3wXVi_4la7A8OGQ_NvSW048lMFXfpdZDXmaLTx2-q4kqzUmhY-p9Vamn0wJmlgfRN78yoyrhBM-w-w375bbQwhzSKLgWfBOFZnKAjPtlUvR41CWJPIp7iad0DVIWS8NE-py60dNeMlTGeuC3BASUCIeqR8-yh_IEpSWrWvIEnpSrcVvTWxguQLNM0jhj2itc313OlgXaKmCEa_ZUFiMkXoq91Rw4Uzw4jfPUer_0LtoweuYSsyddkHkyMqVGwd3gwKTw8DOWK5YnodIOSgSWcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95dd83e81c.mp4?token=AsPraGxAGnlqJGE5qU-57zAiJTyI4bOUe7osjJBuktFgzTR3VaOb9K_hNAolXSs9VBYtlAL3c_326_qOaZOXxRxM2NUlzVFPyXKppmv8hmhDDIhof-NUBWPFBTz_rXTumb4qjIeMhdTlHWSMLq8z1IEp79HRGMjIvY6gUo4zLIs8se2xuVrRczf_vbIVWtbyN7nZbEshVtmUBjOEXbNWpqSzF4e-my4EdVUINIRfYaJwvzFzFc5EHTCE2NtSzIZGA_465CW-0-AqXuelb2DgIITBlZsEWRIfAVqDaXQYjelSknZpL4BMN_Y5qNsRb5xSr9I3CwQ893cZwnScKAOqXrA_g2d0eje_SPnbLG9TY_YC5xZOfh9oa6LqLgH_fuchXnJTC09qBjT0zXB2HeTBZ3wXVi_4la7A8OGQ_NvSW048lMFXfpdZDXmaLTx2-q4kqzUmhY-p9Vamn0wJmlgfRN78yoyrhBM-w-w375bbQwhzSKLgWfBOFZnKAjPtlUvR41CWJPIp7iad0DVIWS8NE-py60dNeMlTGeuC3BASUCIeqR8-yh_IEpSWrWvIEnpSrcVvTWxguQLNM0jhj2itc313OlgXaKmCEa_ZUFiMkXoq91Rw4Uzw4jfPUer_0LtoweuYSsyddkHkyMqVGwd3gwKTw8DOWK5YnodIOSgSWcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: می‌دانم که درباره ناتو انتقادها و نارضایتی‌هایی وجود دارد.
اما باید توجه کنیم که این موارد، استثنا هستند، چون واقعیت بزرگ‌تری هم وجود دارد.
کشور پشت کشور، متحد پشت متحد، پایگاه‌های خود را برای عملیات Epic Fury در اختیار آمریکا قرار داده‌اند.
هزاران پرواز عملیاتی از پایگاه‌های اروپایی انجام شده تا از این عملیات حمایت شود.
بنابراین اروپا عملاً به سکوی پرتاب قدرت آمریکا تبدیل شده و امکان اجرای این عملیات را برای ایالات متحده فراهم کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/130036" target="_blank">📅 18:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130035">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acce89e784.mp4?token=HeCbeFH72VPszwcsL_8lubPxIn10d5ch_U0ZaKV4rlcGIfQhmLKVw9Dsx8ibDCZ2OToR-n3y1vRAP-ACQW7fVuOnY6LtzqnT_NTkFl47TVyzmrW4OTTcNv0vB1i5eMXK_7ZVr1MyfVmNZdn7QoKN-lwExL_29z560_Zo5wGjoP_dFLyEdWWFZhzpxYGzofJ6rXvlfMgLkBU2nVbNQ0Uo5reCxIRer-0LUhKpWd85uzCYtdb29O3cqMzc_pc2GyElbb83QKkUmvCh4O0f5apDlKfiptlUNyp01R8kjoBwtgAXxuOzOv5rATE7umJVAz671OAtgUR8YpzC28y6qiNtRUPKV8lvT4HOZk0uHsOyVm3JMR4FU6IG-Z7chCojHr9vP00kKYu3Irdm2_cRAycC6AgH3Pv5YLoQtfcqF5ck1hZEU924JLj-m2FK4SL5wmt57c8KV6BpPtpwSKfC_iUTd6jkTugZ5wr5e7_Rl4P0PpWT0MGwasLzs5xTSMjF-cI6Q-gMbJQXwgrHMdMrArheI8WbWr2Tcm1g62W8jwX-ths69P6UD1aEzH8MNA1ia60Rvns-GGfMVg4MJEyt5eA4Z8Rm61PexI5dmBNCEUG_MFEXfhl1i0dfdS8-uhIbMbxksLLJghWCo_Dnd5e7Blw14JrZJY11mG2Mt0T2rO2xb2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acce89e784.mp4?token=HeCbeFH72VPszwcsL_8lubPxIn10d5ch_U0ZaKV4rlcGIfQhmLKVw9Dsx8ibDCZ2OToR-n3y1vRAP-ACQW7fVuOnY6LtzqnT_NTkFl47TVyzmrW4OTTcNv0vB1i5eMXK_7ZVr1MyfVmNZdn7QoKN-lwExL_29z560_Zo5wGjoP_dFLyEdWWFZhzpxYGzofJ6rXvlfMgLkBU2nVbNQ0Uo5reCxIRer-0LUhKpWd85uzCYtdb29O3cqMzc_pc2GyElbb83QKkUmvCh4O0f5apDlKfiptlUNyp01R8kjoBwtgAXxuOzOv5rATE7umJVAz671OAtgUR8YpzC28y6qiNtRUPKV8lvT4HOZk0uHsOyVm3JMR4FU6IG-Z7chCojHr9vP00kKYu3Irdm2_cRAycC6AgH3Pv5YLoQtfcqF5ck1hZEU924JLj-m2FK4SL5wmt57c8KV6BpPtpwSKfC_iUTd6jkTugZ5wr5e7_Rl4P0PpWT0MGwasLzs5xTSMjF-cI6Q-gMbJQXwgrHMdMrArheI8WbWr2Tcm1g62W8jwX-ths69P6UD1aEzH8MNA1ia60Rvns-GGfMVg4MJEyt5eA4Z8Rm61PexI5dmBNCEUG_MFEXfhl1i0dfdS8-uhIbMbxksLLJghWCo_Dnd5e7Blw14JrZJY11mG2Mt0T2rO2xb2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: فکر می‌کنم ترامپ دقیقاً همان کاری را انجام می‌دهد که لازم است؛ یعنی تضعیف توانایی هسته‌ای ایران.
می‌توانید تصور کنید اگر ایران به سلاح هسته‌ای دست پیدا کند؟
ایران صادرکننده آشوب است. صادرکننده تروریسم است.
این مسئله برای منطقه فاجعه‌بار خواهد بود و برای کل جهان هم فاجعه‌بار خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/130035" target="_blank">📅 18:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130034">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA1FtNRbgjcdhi4E2aanpn-YG_y0mVU4pSJBqpKsJCItcmp_r3fVXhL_ujMdbHE2OEvguywlDanVPM3edZJf7jVkUowYfKuCHyKYotOw5JxDOHSdYx3nRV_4IVgbz5rdIS-lhNBIJlTbYkzEjA9XjBQwqkfqGTYErDeuAIQpmCjderYaLCN-11l35R0iLgl_rvEEtB_6aKTKdq4UlkZ4foq7JfdAj8iXcpWq1qMIj_axwQcxABlEBOrq1YYpeJAIPQ7wxgQ0U3r4mZWuSQp-Gd0IDwGN-uuLFn2kic9JZT-vWLy54WDRcqdMbzUXUZLKUBcPWpCIpqqn-lA1wW6CUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ
: کنفرانس خبری و مراسم امضای مربوط به مسکن که قرار بود امروز برگزار شود، تا زمانی که قانون بسیار ضروری SAVE AMERICA ACT تصویب نشود، لغو می‌شود.
من این موضوع را یک وضعیت اضطراری ملی می‌دانم.
از توجه شما به این موضوع متشکرم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/130034" target="_blank">📅 18:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130033">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBZUj9zn7MW_x-MS_541mIHqc6A_jLvYvXGWUYW6bYPQNCwwq0LtvDXzrvXNfOdqdjeDn9VFb85KbOt4pD9SzGDmvZjrF1tljPtxVvAX77NkIMeb6IJIKuStDxep4oofqM6x3qis5rp4cvEBy1CD1dCnzbgC59fwv9tAli1EKShshlrdHw9lpfG8xaeS5ywTLp6YcWF8eZdznHBZEgpBB5XEpCeNCE3KRZinsMHoRyDZPXCPx4DHsTIBsEMen8lzyiHSMJxRaPjrYC9gHmu0CzKnM_t7qzijD7iDdPlUbqqORE5OnyxMqV1P0kVB_HaEwcOPFlQf9BXUgljMmKyIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت انواع سکه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/130033" target="_blank">📅 18:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130032">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXXcT_rvhCctcR3LDLbRZ2sDx_uxRx8At9VGkgDhTd9FpPDX00PyFA9H3uQxWR3z7vXgLbOeOgmDJoWMv6nF3AXRYdVWYul_r3Ri0vSutmnMk_7MBbto8gbs4aB5KLZ-nEIZ5l5Cok-J8SfrNYuLgoE8YDMZT84oPa947nG_p7-dcU16P3XMd5txrEuWc-yO0VjpIktWBiLgYvAtVSGe-r0LWM54pusmhDQ7lReTSjl0079UW0Fof327S2Gcqc8CGS0VQl_biBPC8oZELGsfLZQdVHFT76UwiIORvE-h4J3zTAD_tpxPDd9rBanaH-zO1j83sXBv600lrt7FKlEMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت طلا و نقره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/130032" target="_blank">📅 18:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130031">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuOxswJf4aR0socS-dmrkFtljQWEI89kOWOPRL8EWaxv4P0Bv9tBFFIcc2MoRcWqZeaxGLVbkbFfo4bDWnKX6M0xwMg7u8OWjvh66MCHcUo0qr0aJsRlz1fz7DSJzmuf5dSo-uvUdriaMQAmVC5rAvoQwLg8YGjp77-YMOqxa__XDPHDBdKIu96QeRhMtjh03LhYU5d76IZ2s0mnlpl9w3CLsl3_4M0T30R9dCTE5QnD8Sol-R_cexIVffM3NZ895OOzbUUPCqAx1dsbFfEI9zD73MTzxMnMcYMnr7NrRYaaM_pxPMZDtKlTbGKQgDxjkU3ZWmGZnLRKCc-IsgLHtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت انواع ارزها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/130031" target="_blank">📅 18:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130030">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
جاده عین عرب به الوزانی در جنوب لبنان توسط نیروهای ارتش اسرائیل مسدود شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/130030" target="_blank">📅 18:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130029">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYoCPob0M0eguOBZksn5-dMKtf9ouFyDSHQW6gnbcV2823pW4RFRjCg_DqKIRdLowPIZzpE6O_anmVj9aEmZate9dlQVoFS1zCgF8bqcmtJbmnB8dDeFG1gIFh-5RBqWPre6ol6tBf6Q_Zz5Rlbdoadv7FpJCTrq8DoPf58a3YM7bm_qHyn5C1lBmXE9nXRDsZoSmGeQUvpf1polQwvq6t2eRIhfbNUx6moStaEs3IAo2bDi-5cX_YSpCQG17hlpzQ-eyl44gRUwGmNImhcPvfK0vPehzVQ-GAer-nTM101ZVMdnyVJiH5pR3lMBAllqJKdz7Ni4CYyuGkW8BQSH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شماری از مناطق گردشگری در فرانسه در سال‌های اخیر به گردشگران هشدار می‌دهند که اگر با بالاتنه برهنه در خیابان‌، میدان‌ یا مناطق تاریخی شهر دیده شوند، ممکن است تا ۱۵۰ یورو جریمه شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130029" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130028">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKn1ylt5YPPbN7gFxH0SMeUhC0mfxl9kx0JR2RlKn9LhuRMHTttTqI-W_A_KfJbtLGjETWN2grpAPVM1NvihS-gSxu6XuuQ1ApzpKM0D_IgE0OfY9z_0-L3LvYSA6aOKO2uiRufSXqPTRUh-vw-dyOPsIQs71Vxt3Jk9hiCuYH13thYe_e2UXL1CmlDnjC4fZ9yZ9DV1Wuxp3Wa-3lRDys-6okIbVDGDb4QwZ-iNTgBFNzLy-UTQ-ztDZRHkg3ayNQu4_5M5oX6n9g3wRG8mcswcU_xbu9q_ngQofGR56dJ_2k0hCg-2SbZU9le7IwUPhAobbF0ho-_7pzYa2RmYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامران غضنفری، نماینده مجلس:
دیدار نخست‌وزیر پاکستان با رهبری، برنامه آمریکا و اسرائیل برای زمینه‌سازی شهادت ایشان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/130028" target="_blank">📅 17:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130027">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPJmyyn16plwmcwMv3Oo3L_eZH0OFKyw0w03tkV0Y0YXQLqhFl44zKTYVwxtUaNgzn9-EOXTK2dUylD6YzuR_iCnYeyraPmJiy2iysCWefs33NsAs6RjJB1dfAAnIqtFIQ5nUM8VESNFqcAxPvAwNP4QM0VP4ITxMUxwT8zhmQKBi69gbGiTEfFMwzsWNzs-jkC9pO4zNh4wvrJTvrvwCAep9NvT9ONoiqSLb35le_PqffljhzjcbQU-T6EB3C1bRUQG97vde4-3-P1JQybcxMq5j7-UkfvOhN8Lf0zU6ZfDWIpPk3Q6N4WyTSIoBaWmuH1jZc69Qz2o1IWfR-2otg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: برای دسترسی به مواد هسته‌ای عجله‌ای وجود ندارد، زیرا در پی عملیات «چکش نیمه‌شب» در زیر زمین دفن شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130027" target="_blank">📅 17:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130026">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNrVdIH8-cCGJaZVZZwt7AXUET85eQQ0tmC9fU6BneQf-aSmLsbJBff-PxfVs4GzcL80R-9HgI7o_kaamhQvo7UYbbNn6ifEAM4zHRk5XglkjQzlS2YvrXRXak0VmgrRpO6ma-GBDWVW_8U7VPf2sl_a8Ru7yHzS6s3QkcRlOYc6cFV6HaHwDuihWsTwehlpI1kqvs8SRB903VrFHwVoweD_aYkJlDIVswrxk36XNau8qBxdWpLvLiVGMTVOFiUbZZhheJWvk9pTUHnM3I_Uji7E-Gv6o1WUY-_FizzodPEeHL52zXT77-jrkjQ9p49G-EgHeIR3rhCJr10qErJxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ایران و پاکستان در آرمان‌ها و امیدهای خود اشتراکات عمیقی دارند؛ تلاش بی‌دریغ پاکستان برای گسترش صلح در منطقه ریشه در فرهنگ غنی این کشور دارد
🔴
در سفرم به پاکستان به منظور تقدیر از میانجیگری‌های پاکستان، درباره گسترش تعاملات با برادرانم آصف زرداری، شهباز شریف و عاصم منیر صحبت کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/130026" target="_blank">📅 17:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130025">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5SGSP53nth_yXMlGIZ3oUjeCLtkd-SK2OO7a7x4oHUEsl-TNs8IYeGO82xMrd7Sz9GKhzhqUryknygGjhH5toZLvxc-q8P8O4JR4SOXU53PPO6-50juYMrYfqgO20MTYyd1xX_X-BSroY2puvOmo2xbewRhjrVBR7wIkXTg4wYRKUHamgWVqQjb1jfbmmFUnkusrbjaweVtz3JBev-CMRA-_UslSgVlmoqUWXPipsnQzqzZ4yigkZNm4aSgbXYOFoqRpK2Hr72KIqzxF4u-2DL8KILH_4q_Ge7TZdvRlSkGgpqLo4AVWN2UO9B5uLSsY7Zn0ToahwxUj0D41_Rniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
رای های من اکنون به بالاترین حد خود رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130025" target="_blank">📅 17:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130024">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Srw_4WLlirUSB6IJawyHw_bJNXe1XwrKRzt9h6LPSbUsfVqcKGy3LvKCN4sig2agmsEO8PROSBXDtsEClipepAQFsaMtiY-P6ZO_8jILOSFYZj7-aNw-ithzzpNAXacIRth7Cb0caarKkfocqH3YONGzbUQn_vXx1SwoaZgpcPWGFDk7FJeOMdG1ze8mNH-eqYgiIT226N7xbSwH8sgvkI5f5RZZCj1GQXsXSc1pf0te9hOH5kVcwUjKzxpZPyVtOxvfA8aGLj494R9V1ErQiztvq0d_4M5DN9hvw4z3CBRIYdwHlumRxdM2FdwxFt2Qm4wdJ9pqg1MsOgUvl9PTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت ترامپ:
شهردار ممدانی با حمایت سه کمونیست تمام‌عیار به پیروزی رسید و رسانه‌های جعلی هم با سروصدای زیاد و به‌صورت یکپارچه برایش کف زدند. تبریک آقای شهردار!
من دیشب ۱۶ برد از ۱۶ داشتم و به انتخاب میهن‌پرستان فوق‌العاده آمریکایی کمک کردم، اما رسانه‌ها حتی یک کلمه هم درباره‌اش نمی‌گویند.
در دو سال گذشته، حمایت و تأیید من باعث ۲۵۹ پیروزی در انتخابات مقدماتی شده و تقریباً هیچ شکستی نداشته است، با این حال هیچ توجهی از سوی رسانه‌ها دریافت نکرده‌ام!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/130024" target="_blank">📅 17:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130023">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مدودف: اختیارات زلنسکی مدت‌ها پیش منقضی شده است و این واقعیت او را از هرگونه مصونیتی محروم می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130023" target="_blank">📅 17:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130022">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEtmbFJfQPd5GmarwfqFPnLWofdZANL7Wtu4Rh48wUyUTLjo2UeAUs0qCARukkYDDH9RTiIJ4OL833iXyQ5lBdoKlwevS9kEQNcQcGnXwbT7nxIfi0PSCPCMWPPTIpLvqEBIpzJbwm9h5_0LXSV9_zx2arcj-djNWWcNah79jigwD6RHWACyMr-P4hjgpDfjUa9svav467NTCjgQ4tRh0s6DqxoIx_LI_nl6m7AcY58ykCIHvtMF7djQ7FgQFocr8XkFOhHYgyqA5ZGkpR_qwK6A8DVjC80D-syQROMfAolpfMAHkg9ozc0dIUgZWTS66AD7eCKbKaY_3QtXVRS76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تو این مدت جوری پالایشگاه‌های روسیه رو زده که نصف روسیه درگیر کمبود بنزین و گازوئیل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/130022" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130021">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHxAEN_CZVlKMqqLGB-GNTbIDPRxWjXQO-LTkCMNzc2Su1rk4AXd4tB6Rg5xfICeohZExuV3PpLSuSTnWZA38nhSK5Rr4CiwwyK2P5YOR85ZcynzlXs-tqg4nsG3GN-rrX8nJXPD8XX-Gth3vFn7w44kS_zIghrldc6G0cuO7y49tgEYy68adrpvUa7w6sfxhKGA_E0LQ-Rym1VBW10ze_C6nYW7IfGz3Qyxc_a37OzsinBawoRTF8pAZM6a-iC7GhqwNJnUVM6vG7veUk7mNvJznhfkRCjD6fAvbdGr22IEcyAE4JfU9MVBvdV8NSNETD61KGAQJxtL2bYxCbjTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده روز چهارشنبه سوم تیرماه اعلام کرد که مارکو روبیو، وزیر امور خارجه این کشور، در دیدار با شیخ محمد بن زاید آل نهیان، رئیس دولت امارات متحده عربی، درباره یادداشت تفاهم با جمهوری اسلامی ایران گفتگو کرده است.
🔴
بر اساس بیانیه این وزارتخانه، دو طرف در این نشست علاوه بر بررسی مفاد این تفاهم‌نامه، در خصوص تضمین تردد ایمن و آزاد شناورها از تنگه هرمز و همچنین اهمیت حیاتی برقراری و حفظ صلح و ثبات در منطقه خاورمیانه به بحث و تبادل نظر پرداختند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/130021" target="_blank">📅 17:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130020">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffHQqDeuCDDJIVt0VlyyX2JRTUYcFYJI4y40egBfzh8PQaV90kzCTOQ3owB8I_cGBnEWxhlBBeDJN57ZSBGDqtDoUVRcCQCyNDfNy2oNowfB1Hlmo5yG3jGXG-7KqopeyJnT82tSLccKMmPpGZZsZRbs3BUcQ3Ttv0K8tKt4gdlVzPJFtwlUUKjTGkcO9YRsViRUper8z0Dz_NYZmjNOsHXXbmLs89knb2np_ydPyMcPluVNAQ8X3WIt8GokYE8xZIfUW6ZcNdugL8UELAfcN_FJomfdyAXfQQsWtSi2l7gJ-CADlCf0DYOEwNWla8MCCwUiUnX_L3U5dI2sTvKYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط عجیب طلای جهانی/طلا به زیر 4 هزار دلار رفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/130020" target="_blank">📅 17:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130019">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEK3PYIInLQtq7KaKk4V9cN0Bl45BfzN5wo6pZEMl75cms9jZUH1zUjGXpZXAKiqtrk7iFoSpV4WE8cwjxYjoSKzSpq6f4KpYz6lWzmafNY9LPYSuj78S-hqPbdDDjcPtC5cWLwaZv8E6iA8Sxa3yL_XT8bppsBDU6oHZKaHWdkCw27c6IdnnrtBZQOstonvegVG6vk2Jcv-33Tf0-D2HIsG_7CWE3dJtTAdKV_lsR_OXwjFVG50dkN6JC5Lh6IPSK2oxFi-OBwoQ88OzrMke7tVKkoQzwLxcg_vSd3AaZ0HznN8PKDkPt6pVLfIsVZ2YxjdGpsUnJVzB0GCzHrUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قضاوت جنگ صدرنشینی گروه K به فغانی و تیم داوریش سپرده شد
@AloSport</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/130019" target="_blank">📅 17:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130018">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db753fb80.mp4?token=XIRRRbCNVrk1mIS4U-DKriMGrssQHM4j0jqRrX18LxZdNR1G5-SVD0uP3-oosVrMGA5t8zcEMiq63Dfcedb_Di9W_bL_687qigZsdMPKbR1FoalJGEBhxpJttO_Ps2fEA-RVPjnhgA_T6L4TU9sue-sBhjZMqoHCCVbA_3rY0bjFQjTYXi9B0nWWssNqFKBLeZYa2ntMkRGFm6UYAFk22IubdA_pivkHEiuYF35NX9MVqggCzCc910_zAz-UCAN446kt98gOex7y5fYaaR9VKi6gk9HYwCNTVrkGGzpoTQXgg2MFi8578QNyhZmRD95rtmQefj0WltkRo2EX3897PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db753fb80.mp4?token=XIRRRbCNVrk1mIS4U-DKriMGrssQHM4j0jqRrX18LxZdNR1G5-SVD0uP3-oosVrMGA5t8zcEMiq63Dfcedb_Di9W_bL_687qigZsdMPKbR1FoalJGEBhxpJttO_Ps2fEA-RVPjnhgA_T6L4TU9sue-sBhjZMqoHCCVbA_3rY0bjFQjTYXi9B0nWWssNqFKBLeZYa2ntMkRGFm6UYAFk22IubdA_pivkHEiuYF35NX9MVqggCzCc910_zAz-UCAN446kt98gOex7y5fYaaR9VKi6gk9HYwCNTVrkGGzpoTQXgg2MFi8578QNyhZmRD95rtmQefj0WltkRo2EX3897PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از حجم بسیار زیاد آب رودخانه سیمره در شهرستان دره‌شهر ایلام
🔴
نیروهای امداد و نجات هم از پس سیمره برنمی‌آمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/130018" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130017">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6001bc8d37.mp4?token=fE9_9KeB7TnSemEMUl9lFclk88kautKPVCrVe544IxWs-UHdm8viJ3mBqckj4n96uwjYFWJ2S0zjJNAYXAdCygdfBkPEkeJws7ezHyTJ2ht-mxcgnxA2lfaccGdMCS7h437wsEpg_9N63MBBL48rUY2VzUW7AZJatZZBGnVwWQCDSnKquDvbOEVIPBo1nxzK7MAHnv89Fn92yJCO9NUE3byiStDYU_98qvuidoZC8p4KVPf3Fg3ORdJl3pIDCyNSWJm4yVCSjAx2W2uXyjV3QCer3deWsBhjHo2t7Jg5wV3_TYhaBlr6xnrXBn-xPmhdSpVbzSpps7AxjmLiVaBsXYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6001bc8d37.mp4?token=fE9_9KeB7TnSemEMUl9lFclk88kautKPVCrVe544IxWs-UHdm8viJ3mBqckj4n96uwjYFWJ2S0zjJNAYXAdCygdfBkPEkeJws7ezHyTJ2ht-mxcgnxA2lfaccGdMCS7h437wsEpg_9N63MBBL48rUY2VzUW7AZJatZZBGnVwWQCDSnKquDvbOEVIPBo1nxzK7MAHnv89Fn92yJCO9NUE3byiStDYU_98qvuidoZC8p4KVPf3Fg3ORdJl3pIDCyNSWJm4yVCSjAx2W2uXyjV3QCer3deWsBhjHo2t7Jg5wV3_TYhaBlr6xnrXBn-xPmhdSpVbzSpps7AxjmLiVaBsXYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا، بسنت : سلطه دلار خیلی مهمه
🔴
همه کارهایی که ترامپ داره انجام می‌ده، دلار رو دوباره محور تجارت جهانی می‌کنه
🔴
تو ونزوئلا و حتی مذاکرات با ایران هم می‌بینیم که معاملات قراره با دلار انجام بشه
🔴
در کل، همه این اقدامات جایگاه دلار رو دوباره تقویت می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/130017" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130016">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTFwF2XGGZhLZxG68pHmYyDaTYb2p3aDb0Mkctlg-wjST2oaBMKR4OvusoWZx7us6HpOFJRCJbykGhjo5UClVDqWs5AlcdAseka622FW4UCb0VTbs8JMS33mKgUC23tGfTIgYz6jk1msLNoLdL_eXQMT_1GLd-JcUUR2DqO8ZN9cagaRl0WS3nFpxiihKzt0Q6DQb1xw_MlLEdx8QlwtFQTG2pwLN7bE9j5QdWPnX3bpBCVItUc83bzmMNDx1N9N03K71y4ZBY-CZJpmWY_9gcNNdNex_R9hJ3Tsq7CTkAbWviwmou9OPGBGypXi-rCeMkEsgLKDLSFGu-6mg6IcMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا به زیر 70 دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/130016" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130015">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یک دیپلمات آگاه به خبرگزاری AFP می‌گوید که مذاکرات آشتی کشورهای حاشیهٔ خلیج‌فارس و ایران در عربستان سعودی برگزار شود.
🔴
این دیپلمات می‌گوید که پیش‌بینی می‌شود نشانی سطح بالا با هدف ترمیم روابط میان کشورهای خلیج‌فارس، ایران و احتمالاً سایر همسایگان منطقه‌ای در پی جنگ، در ریاض برگزار شود، اما تاریخ دقیقی مشخص نکرده است.
🔴
او می‌افزاید که این نشست‌ها مستقل از مذاکرات جاری بین ایالات متحده و ایران خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/130015" target="_blank">📅 17:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130014">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn6dduMMzIclFIxeyW-JUjIVXeKmzHd6VXgAQhSl_mxpZh-UnnR88NUt5s5nN5JJApesFqJXOeHOE4K9MujnbdfMbjrzvySDi8mn1Ae0B1fpDULV9ZrJ9GxzMaR9YJ38Zz0g1V4ciOl415vBWYJgwhkKjPGPhUw3zW-gtKcbzZlMNt54ahymPelHpBnwnVUWYMWywl20DSXMuakzDfu6hD4nJOcerpXY5LFPyE48xxi5bTaKBFOcVZjmaO9yibenzopr6vieY8XmN6jznH1XGVdCCGKYyX9qp0qBiW2-cFwEQZgS6gZsSUSqYL0yB2WQ0w7tJ1yvYY54z-n2sufaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکسی از اسکورت هواپیمای پزشکیان توسط جنگنده های پاکستانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/130014" target="_blank">📅 17:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130013">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm7PguaODrZ8499m6fE28zZ82pdJYM3wXZe298ttUX5uO7USrsT1m7r_YrYXEMe0zl75Otp_shFV5YI1kKIVusR2A23jTlpvF_d0zUiuPfoA9ZrUSyUJZ1fSrmu3K0RooqLDaAmYCtRDQ6wUXBOvF9WQVbt4s9xrTRClBxadYeEkLZsVPlZsCJI4RLZjp4WvFw7KJxtvQU5VIFUfNMMikBs0N6LUyAuBTo8qLKWsV3JP8kTDNHG7u7I-3jPa3mwNu9419RJTd3mIbSha0D-hE2oZ9InfSK8oDMNq3ZXHuxwpcFeR0YeYMCKqbXf0dx1E5ywNSYCiSsrymmLqvm95iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شواهد نشان میدهد مدیران دفتر انتشارات مجتبی خامنه‌ای دقیقاً امضای ابزار یکسان ، نسخه یکسان و سیستم عامل یکسان دفتر انتشارات قالیباف استفاده کرده اند.
🔴
در‌نتیجه هر دو نامه قالیباف و مجتبی خامنه ای با یک کامپیوتر نوشته شده در ابتدا و بعد از اوایل ماه ۶ میلادی، اوایل خرداد ماه، رایانه را از مک به رایانه ویندوزی تغییر داده‌اند.
🤔
قالیباف همون مجتبی خامنه‌ایه. خلاص
🔴
حالا طرفداران بیت رهبری محکم تر بزنن تو سرشون
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130013" target="_blank">📅 17:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc80afd3b.mp4?token=L94CZibIdWjVvMjrIOnDDNQtzAFfL5LgW6AfGAvRZUxj4xUq0gXujO8843YGTz4Lh5cJDnTIBMO1eEnCcTfNCZRqsGbrp-f0DiJcR86iGm9rDwWhJzYS8Giq1Ri2Ejex4WIn2peRHRsE2UCNzHztBvemq15TsNKN0w8lXS38GWxL8NEdlhXEwPBa0jMNkTnEOObKHV2y9GX1Dg8IeKMCIp5w54LO5oUdFsxn5iWxYqhmp5IuRMncodgYAuoU9Ydgh3bPG2illZ29iHr-fDFnHqJKOuGsKfgVSAVvcW0bYPHAj6fihBo_kAVaIUx4vi1O9V83oPeDKxCk4DH-xp9WKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc80afd3b.mp4?token=L94CZibIdWjVvMjrIOnDDNQtzAFfL5LgW6AfGAvRZUxj4xUq0gXujO8843YGTz4Lh5cJDnTIBMO1eEnCcTfNCZRqsGbrp-f0DiJcR86iGm9rDwWhJzYS8Giq1Ri2Ejex4WIn2peRHRsE2UCNzHztBvemq15TsNKN0w8lXS38GWxL8NEdlhXEwPBa0jMNkTnEOObKHV2y9GX1Dg8IeKMCIp5w54LO5oUdFsxn5iWxYqhmp5IuRMncodgYAuoU9Ydgh3bPG2illZ29iHr-fDFnHqJKOuGsKfgVSAVvcW0bYPHAj6fihBo_kAVaIUx4vi1O9V83oPeDKxCk4DH-xp9WKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، برای دومین مرحله از تور خاورمیانه خود به کویت رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/130012" target="_blank">📅 17:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itC5AsomZpqi1l16-1lJ7vuhXV6D4HRubCtuZW-9bUbldcgMTn-ed0daiG9QH4AcUe23Ii7PCHc2pzeapYxfnXD39iN0T5tiaGf2NPuhJX9_eS92w21y6_qemLiTG1mnZRgtcIJTCtDdwL-jfZD9OmILFVwrjiZL5CSn-Ftt_mkvRDbMSuxl0XETStM4s2k3J4z9CDgqkaKG0zUAxAXETXoLk6eB5rFR7Sb_F5OjT34h7ScX0IKzpq0zVB0EmGqpN1fRKkChP1_lFEmYm9H2FiIsMr63yq8N3XvxGiNxnl0H2fblewEu5F_0V90QQ9VUFu6CradZJl0yUBwUyRk5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی کتاب جدید وزیر امور خارجه عباس عراقچی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130011" target="_blank">📅 16:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130009">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41470bf010.mp4?token=WNBbEcz4hq7KXtWZZK8HfkBX6RAF2Ke17f4PJVUFW4tdRlYUaDWaP75UHYQtj03SPqn6VAILbxe-aoMFz3WV3BKvlFFttXMRJAcwefLoLtVV84ltQHcj_3OrmbQAW6KJzqZvcspe_LtiENK2tv0oLzGwu76NVWsP1i_5me07oatiPQhVemmmYNwnXTkMfkUyTJVqCVmjVYfPJYPVAmGq4qlmxXAeu6QkqCDZjjuChwVHMO_i_8knaMtzPvQ7dzQZV0EAfgSCALpaQqK9xoZLCvoHxSFgvBQqexEn_EZUPfA3ZgFML2o1HWLu-2dJeHBPqNdVFdPL-gCt2cfNwoTuCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41470bf010.mp4?token=WNBbEcz4hq7KXtWZZK8HfkBX6RAF2Ke17f4PJVUFW4tdRlYUaDWaP75UHYQtj03SPqn6VAILbxe-aoMFz3WV3BKvlFFttXMRJAcwefLoLtVV84ltQHcj_3OrmbQAW6KJzqZvcspe_LtiENK2tv0oLzGwu76NVWsP1i_5me07oatiPQhVemmmYNwnXTkMfkUyTJVqCVmjVYfPJYPVAmGq4qlmxXAeu6QkqCDZjjuChwVHMO_i_8knaMtzPvQ7dzQZV0EAfgSCALpaQqK9xoZLCvoHxSFgvBQqexEn_EZUPfA3ZgFML2o1HWLu-2dJeHBPqNdVFdPL-gCt2cfNwoTuCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عزاداری‌های زیبا در سراسر کشور
از خون جوانان وطن لاله دمیده
🥀
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130009" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130008">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a64587f2d.mp4?token=rNXFx4HKxGphF0mw7ahRyooR4nh3LE_fcDPyuCorGnwFRG9qjX1mKauTtS68C4unK8Xn71fpRgdF1EO6oA3tSZLGjZh-V9sp-cuxIEHenTQ4k_tRWAzdBYQuSOoYifM_JEESSKBZMuT616A3LfOzstgR3ksQIfvWRfOK-B4v5QEHBOkjP15WIRsQNwuVhbBIuJB9-LPpfD2Sts2P7gRqBirj7VOQxSiw3Htw5Tc-2IAHQxLctnNPFjQhfXVWgncuL1-ftDr0MJ6zzbNAcKuMg3EEQT0Cf8L-8YK0VEPLdF8tg3SmLwn5V6LvhizQGR_e9QuB68EgvPKcDrJuWemcEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a64587f2d.mp4?token=rNXFx4HKxGphF0mw7ahRyooR4nh3LE_fcDPyuCorGnwFRG9qjX1mKauTtS68C4unK8Xn71fpRgdF1EO6oA3tSZLGjZh-V9sp-cuxIEHenTQ4k_tRWAzdBYQuSOoYifM_JEESSKBZMuT616A3LfOzstgR3ksQIfvWRfOK-B4v5QEHBOkjP15WIRsQNwuVhbBIuJB9-LPpfD2Sts2P7gRqBirj7VOQxSiw3Htw5Tc-2IAHQxLctnNPFjQhfXVWgncuL1-ftDr0MJ6zzbNAcKuMg3EEQT0Cf8L-8YK0VEPLdF8tg3SmLwn5V6LvhizQGR_e9QuB68EgvPKcDrJuWemcEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه دو: به یه جاتون بربخوره دیگه...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/130008" target="_blank">📅 16:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130007">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در تاریخ ۱۹ ژوئن در شمال غرب سوریه حمله هوایی انجام دادند که منجر به کشته شدن یک رهبر ارشد داعش شد.
این حمله دقیق علی حسین العلوی را کشت و بخشی از تلاش‌های مداوم ایالات متحده برای مختل کردن و از بین بردن تروریست‌هایی است که به دنبال حمله به آمریکایی‌ها در خارج یا خاک ایالات متحده هستند. نیروهای CENTCOM به همکاری با شرکای منطقه‌ای ادامه می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130007" target="_blank">📅 16:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130006">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: بازرسان آمریکایی برای بازرسی سایت های هسته ای ایران به آژانس بین المللی انرژی اتمی می پیوندند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130006" target="_blank">📅 16:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130005">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فحاشی بسیار رکیک یک دوازده امامی به یک شش امامی در صحن حرم امام حسین
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130005" target="_blank">📅 16:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130004">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f20ebd3f0.mp4?token=BmVVGPPSl-coBXPbx-ObfVevD-lfBsVAyf0C_NAg7NOKumkrs77EqerakJzFFtfm0tivjwAsfVfcGfQOJvRz6o4NXVUNCu3SKyOttV0GVXfy1CxKSmPgj-TAAMoRP40r3J3ACwi08DHQxwkTqpo10sBSJyu5x1RB1a2v-uYSPZvtYI7xM4auOWxz4QoDE__0dTHLw295tH6Wbzz7-CF5_QehxfAk_fpLDs4vDkGlfux_80cv1SV4kdu5X4QjZtA-YlOr8CWHm3Wcr4XnOV93aFRcyOqaJWqX19Wv3H3VluGIvpXLo_OBW0y2kltmGTmi3NpQDK_gum9YYZPTHN87qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f20ebd3f0.mp4?token=BmVVGPPSl-coBXPbx-ObfVevD-lfBsVAyf0C_NAg7NOKumkrs77EqerakJzFFtfm0tivjwAsfVfcGfQOJvRz6o4NXVUNCu3SKyOttV0GVXfy1CxKSmPgj-TAAMoRP40r3J3ACwi08DHQxwkTqpo10sBSJyu5x1RB1a2v-uYSPZvtYI7xM4auOWxz4QoDE__0dTHLw295tH6Wbzz7-CF5_QehxfAk_fpLDs4vDkGlfux_80cv1SV4kdu5X4QjZtA-YlOr8CWHm3Wcr4XnOV93aFRcyOqaJWqX19Wv3H3VluGIvpXLo_OBW0y2kltmGTmi3NpQDK_gum9YYZPTHN87qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فحاشی بسیار رکیک یک دوازده امامی به یک شش امامی در صحن حرم امام حسین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/130004" target="_blank">📅 15:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130003">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VhGdxAas1MNnqIJiX4HBwtwfIQn0TCTNGB5YqntMRQY1FfsoNaX_M4N_0Bn4NzClfBNsiyiBTJ3SQ5jJPasniKXc6ZTeB02SJDvUEG7DhJGt8CSxAq4e7QqqKMw5u3UogZnmmh1tTHteJAJsuzHZfjNv0I7cQ3lKm4UAYaK9ntUh1m8G03eTdFVKVz7faKNDW_JFmsexVrDGVHfNw56DofQ_3aq2h6EySyKPao_jGd9v3bs1jiQVGEIh2kiUtnWBOOwQHHsK9QA89OgmsmrbzEUz3EK97jxdKezqobAaObwW7AlrY9EABtrCz4tipwg5PB68Gah9Y2L-uBc-FhdkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دادگستری هرمزگان:
حتی تار مویی از ماکان نصیری هم پیدا نشد، احتمالا موشکی که به مدرسه میناب شلیک شده بود مستقیماً به بدن «ماکان» اصابت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130003" target="_blank">📅 15:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130002">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtntOif9EOaXLJL6PKYCRbb7rGaU10-ks1v94mqqBKl3B5vXyTSpg3HnxcsH2OKlIdqPdLMpAKhLqYcezXyLwwtM7AhOtJYFjmGv9q0LO4iz7Q4dKMEIq9pbNlOdZFH68B6YCtE_Pj_JKc3IfhsPj7RdhBHfJMJFqKE_-gZyhh8GvhugmNJs0PLJjKPW77G-GNwOPfU7I-UdPXLrF9URFOVOSA6-I8xhMg22ecTc_pemWmy8OHbYAcTmTkgizVxp-mdnBFx-hXXFyEEUNg0jirOh0rmg6dth1k6AMD5s7l0vLkRszoDtgKZP4_6M8CV-JaGk8EkbkhNm4Ow07tBNaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ یه پست گذاشته و از خودش بابت اینکه اجازه نداده ایران به سلاح هسته ای دست پیدا کنه تشکر کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130002" target="_blank">📅 15:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130001">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5SQ61CNNRIhRMmnwgLxdl_oGaChJX8Na4To2ankEAbAEkT5puTzF9ObjAoikG3sYDs2w3PY2IXlrUICuI4Calx0CAqktk-hkFFKWcmXvkUV5JNIAynwpf1AdEkI7Cexg5a0wfnsSlkyY6hM1Oigy3rNWDlcYtDVsmH1UMyoDkKDHrGwm3KsE7hNOfZiIaPfmYd0JUUzEq3CQeh3RVlNx3kczP-r76Qg_nKmWo6yNKTMomJUkmph6E-TeJrDeKrTsiOKCBL13XYJ_DKSWvZjG8m_tfwOaEBnTN7zfNGmwjwjbjK4FntQgUmRqFWZOZiLEL26lHGBnSF37YZiP4YXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار قالیباف و الهام علی‌اف در باکو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130001" target="_blank">📅 15:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130000">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر خارجه اسرائیل: مذاکرات جاری در واشینگتن میان اسرائیل و لبنان تاریخی و بسیار حائز اهمیت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130000" target="_blank">📅 15:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129999">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB3s8XmuhTsj95JVFdFYdYY_MaBevLyJcevE-1v2L-CLNtBVMmiAKN23_wJlUV2FKQfHUzTGMN1nCmG8TbyXhc5ymvL-vW9G_D2ipwvo2b97p1oJEit38Qnv98dADR84E4GQGk3bfzd1-akmdTnCSzAxBupWpzJHy7kSW6OGFC-sUWJH2M5-o8f7-PrgehIEUpkMC8fPTWyB4lRPsTugKnc_gzfyut-aMOVv4toPUroS-6-5GHtZpJEkfvJ5XrPp_zXfmCi_bMLPomHrPmr6Ih7mtWQezbp4b-jDV-4G2hj7YSmOJKt-EXtgaJHRy1s-qBR4UatNKrjfKM9UlSbMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایران به آمریکا اطلاع داده است که برخلاف گزارش‌های دروغین اخبار جعلی، «هیچ عوارض گمرکی، هیچ حق بیمه و هیچ پرداخت دیگری از هر نوعی توسط ایران برای عبور کشتی‌ها از تنگه هرمز درخواست یا دریافت نمی‌شود»
🔴
اگر این اطلاعات نادرست باشد، مذاکرات فوراً متوقف…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129999" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129998">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCIq6cAJ3h6XLKsuiDf8SBWgW-9MPUBz0h6qWUkF-wGbFbMcOpAX-VTMIUasWWbtbULECa4xRTsFjM6IuD_QacMhEUrGZFYJaYSpm8eqVkCcfsFKnuqWtgTIpJX3UPsTv3jrc_JgzZGym5JxMOTY6PGooUsCPZcwntlIMAXobBvwyCrzDAcBcq-XwZtkx0sC237t_iSn_NwfIJfMxjc1_GbA0Np0ixuHdejV4AvJQOguYhcofqEiW5gNaVuBv3QBt_g52dYIaEXUkpBBCjAyRwXIwYk3hztQLzEYcWyaV9WHAh90XfpM5Obl4AQ_TqgikLzNRqg8-AKk7YwE3WRq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
: ایران به آمریکا اطلاع داده است که برخلاف گزارش‌های دروغین اخبار جعلی، «هیچ عوارض گمرکی، هیچ حق بیمه و هیچ پرداخت دیگری از هر نوعی توسط ایران برای عبور کشتی‌ها از تنگه هرمز درخواست یا دریافت نمی‌شود»
🔴
اگر این اطلاعات نادرست باشد، مذاکرات فوراً متوقف خواهد شد! علاوه بر این، هیچ پولی به ایران منتقل نشده و هیچ منابعی از صندوق‌های آنها توسط آمریکا آزاد نشده است
🔴
ما بخشی از پول آنها را که کاملاً تحت کنترل ماست، به کشاورزان و دامداران خود اختصاص خواهیم داد تا ذرت، گندم، سویا و سایر مواد غذایی را خریداری کنند
🔴
ایران به شدت به غذا نیاز دارد و ما آن را صرفاً از ایالات متحده برای آنها خریداری خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129998" target="_blank">📅 15:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129997">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XVVxMsd4TvWHnJjtfL3XJdzQIKlNRPtzdL-CnO-Ka01gHQe_oyts6gizuzdelgXtoPh47r4PxpFklXIuzzcwoiWdtJ-HNRWPUu3UAQ6fLbiliBZH6LjSi4CPJUltKjIX_4EPrIpdTEdG2q2tahNjXTowXhbAX24wwRZ26RVaePtFgjX2wqaX2Mqe9RPoQW1cZ7hf7VWb7fXgo6Q9FYF577HSOJTFcLlk54MYurSp8EMSQG9jRiaPBtXSGdqhMjrdGt-12Cec9s83yV-m0NlCoHTA9A6_c4ic9FdF6CNrU-6uTkULoH9SnO3ABg2FtTAy8IZXoiAaUa3nfLiE_e9Wyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مصاحبه وزیر میراث فرهنگی با خبرنگار اسپانیایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129997" target="_blank">📅 15:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129996">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=rXBcpbkAM_HpbCEdtgcDDGhv2JgDfFr5W2W7pCh3SAaytXjCPykqQYSOFnrpDeVbaYbMkH2s4kP99GwpESK7GKRYQI7Cm8kE2qyDooTs7008MaocYHJxUhhY4hWInFok5xjK1hkj3DaW-Yn0E9xJxtmEhUDfIeK_8N-ouywe_aevM7TrNUdmhWsL3l38QH1IcWIC73P-g3zjeB9hWopuqiMKPBqoegL6azldp2Gm79yvYfFn4QMARO6-pPHZFVlRu5Ju2mGRyT7qNmfdP4eXORpgtVzvXdIx3KU0ZNF9Q4ZPv6KzBF7wjCqtJoRRACesOTbAxbNbWxx5UIWefSCxAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=rXBcpbkAM_HpbCEdtgcDDGhv2JgDfFr5W2W7pCh3SAaytXjCPykqQYSOFnrpDeVbaYbMkH2s4kP99GwpESK7GKRYQI7Cm8kE2qyDooTs7008MaocYHJxUhhY4hWInFok5xjK1hkj3DaW-Yn0E9xJxtmEhUDfIeK_8N-ouywe_aevM7TrNUdmhWsL3l38QH1IcWIC73P-g3zjeB9hWopuqiMKPBqoegL6azldp2Gm79yvYfFn4QMARO6-pPHZFVlRu5Ju2mGRyT7qNmfdP4eXORpgtVzvXdIx3KU0ZNF9Q4ZPv6KzBF7wjCqtJoRRACesOTbAxbNbWxx5UIWefSCxAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب صداوسیما یه نماهنگِ سرطان پخش کرد؛
بعدش دیدن خیلی کسشر و آبرو بره، کلا گرفتن از آرشیو شبکه سه هم حذفش کردن
😂
😂
😂
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@AloSport</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129996" target="_blank">📅 14:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129995">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsV2wQv3jqIthSyRkIQ4WWGJvrX0AKNVu2orpY6hfGL3uTbpjWoD9r2zlJxybyH5jELXGGxQ0klWhuezb5urLZE6P7rGJlsY36rVFfdQ3sS9WD7jaNbDIsY8l38ZEVI-kyxyWJU8u8vKCyo5BcDl8op_n18TA-hEgdGqWJ3i6ScBY3j8kdXYhk53s7vHFs4EMa7I7RlxZz67J2IJlhGxxlNmYGyBlNTl8FvODmx5tkTAJJqpLGqQ9IdrwIA9146CSVfsRdGc3F8p7XndWRBLPkjl_XLBjWowMqoPe1tDX8yRjkIl8J2atqmcbEaz1JTm5B1hl03cLOIVHA0kaCmVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارن پالیسی:
توافق ایران زمینه درگیری‌های بیشتری را فراهم می‌کند
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129995" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129994">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/obbGf4LdyKfn-WCsT8tTbDJKi_iaOdGNaeK7OVhwG7JKgk29sC1R1wwTLEtZEs8EmLSGtACx1AUFB3M8K1wGPeBmKlfv_yKPLMJDOhD5uO_nItgWJgFznpRl14zTWBbojoTE3hfSykFCrUD9uuwwz3GxslugkYCrocqTg-pgYiOjwPgjJoao9ux3-zfn7hUm_4jKVnbmXnyEYhppc8xe9xNu-kX1b0eiX-MeSUrqUEuEMWQt912KDYRkZRo_Nxv72LF-DC2qhOsSbNfntQzAvBnMOamG6uMl4-cDQVBRIgtbyHJYry_6V4tJ3s6PZUD36dPYANwV2WsRHJxd7NVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا ایران ۱۰ فروند هواپیمای مسافربری بوئینگ ۷۷۷ به صورت دسته دوم از عربستان خریداری کرده
🔴
تصویر ماهواره‌ای ادعایی از اولین فروند تحویلی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129994" target="_blank">📅 14:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129993">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل:
حتی اگر واشنگتن از ما بخواهد، از جنوب لبنان عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129993" target="_blank">📅 14:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129992">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5cIIoMrZ_vRciF2zaWeG19nmvd4P0k5uGGprShWnix29u5lZ__F47-3sBiz7LKzU7fZ4C3opIPhVnAyr7FzW78NKzIiMXFxopslcG5KCvO_B3txYJoE27mv9mXqNEKFuQv9JD0URId8oTPAwjXD5GeJzdhWM_rKvA4VbU_Gz9AVyCI8NqgasxkTelGtSwwZQ_2VRnGp6WMnxBCsvFcz3axmeBSkECHB71IkHYNr7lPiaVakQqe9KC9sb1L35LUqU7V3ds24EVNWd7najZReL_Vbu3-W-vEw5TUxwQeUIkLsqXRi8QmZi46mRV-I2CB4Ids-1VLSzQq3qpOdOlA8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: برنامه‌ای برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد‏
معاون وزارت امور خارجه:
🔴
در سوییس هیچ نشستی با گروسی، علیرغم درخواست وی، برگزار نشد.
🔴
هیچ برنامه ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته ای وجود ندارد.
🔴
این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم ها و... بررسی و تعیین تکلیف خواهند شد.
🔴
نمی توانید با هیاهوی رسانه ای، سیاست "راه بینداز و جا بینداز" را پیش ببرید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129992" target="_blank">📅 14:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129991">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
دلار با افزایش قیمت به ۱۶۵۰۰۰ تومن رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129991" target="_blank">📅 13:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129990">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سخنگوی پوتین: سلاح‌های هسته‌ای تنها چیزی هستند که از جهان در برابر یک جنگ جهانی محافظت می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129990" target="_blank">📅 13:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129989">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وقوع تیراندازی در آنکارا
🔴
رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129989" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129988">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ایسنا: اختلال خدمات کارت محور بانک‌های کشور برطرف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129988" target="_blank">📅 13:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEzDjrbnZJWvCikv61RBIzRIgheBd39K8lEYCPr2GzZOcgK4Mx6MoVmhJn7a-M36SdLtN1GNXHKkotESf33by29s3p3G981JYNdeAxixWg3OzhW4QGnOtCLyki2VSU6pCYErqtJPnl_Z_npWfPL8VFX7KzebQwmaD2ncqWnfqSAtNEG2vbbJrPtr2i6s-P5nw9hFt7hi84J6VLSStso8_X2yAR0rksNdWSEXHhRX2yyCStL12T1-J5a28aJQiGXdHKecFoCCLnX59kQ0ubYRqKyAqpURqRkvy_ccx2JNJ3araRnhCFTx_rHojAuVq5RMe_wELsFhKhqLQKer0rDiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایید 4 سال زندان برای دو ورزشکار ایرانی در کره جنوبی به دلیل تجاوز
🔴
دادگاه عالی شهر دائگو در کره جنوبی با رد درخواست تجدیدنظر، حکم چهار سال حبس دو عضو کاروان دوومیدانی ایران را که پیش‌تر در پرونده تعرض جنسی محکوم شده بودند، تأیید کرد و به این ترتیب، رأی صادرشده جنبه قطعی پیدا کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129987" target="_blank">📅 13:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxyqjfw1WMcJj0UZ8KwVm4iucLz0Mw9H1k0j3ApAy9-PqUr7hjddgodvICHXD2oDFF8VbVYucKU4ij2rbGAT3MkbcT1jVBLRL6qUos098r2EXZo5Vd3IHsI2V3Pl2QAQpbGjP42pH98dmdgbHnyb0yAsYhlzDL_RhZc77h_vT83erSyn9fki6hA4l022g-Iz8mHnMH5kZ3DEwBspBbrFUFrd7E_o6ooSepCSShlmaqGVSmm4IhrNxfE3EXwp0rw8PfHbITKDPlvdYIAV_DI5fH7JSJeCd0jjnGRCUweL5mVYPVuyxrK2rf6JLbGm5Mr8_Y12omXmSEfC1KSRE6HlOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: تاسوعا رو تسلیت عرض میکنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129986" target="_blank">📅 12:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129985">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=ELXRowjNXGRmTeBp3sOnTzDTQP81jenA-3092MPXrsRua1EvlCjfxt-cpTuJGBW3DKYDM8rsWmxXJWgWfaefr1DyfbQt8TWulbqLtFjf9cqj4NNg9HjGLpOZyqtc6Qx_WnbiHEjkXv5ap6p33DK5LJEoxv_BKXsE97S6AkIFu_1lMcj2suzwEVdzQj91z-vRCJf1ARWaJLjda0VE9n9bH33PkYbCkAADZ6kVpBfwBspG-9eRyM0Iw9CN4QXAQYl6bCxKNe3vsensf0J-eVGt3ok51QX4bLNtDLsx9QiLLFNBoihBm4FJRe5kixkGznGbRCTnqiSh6vmqtWYStxfVPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=ELXRowjNXGRmTeBp3sOnTzDTQP81jenA-3092MPXrsRua1EvlCjfxt-cpTuJGBW3DKYDM8rsWmxXJWgWfaefr1DyfbQt8TWulbqLtFjf9cqj4NNg9HjGLpOZyqtc6Qx_WnbiHEjkXv5ap6p33DK5LJEoxv_BKXsE97S6AkIFu_1lMcj2suzwEVdzQj91z-vRCJf1ARWaJLjda0VE9n9bH33PkYbCkAADZ6kVpBfwBspG-9eRyM0Iw9CN4QXAQYl6bCxKNe3vsensf0J-eVGt3ok51QX4bLNtDLsx9QiLLFNBoihBm4FJRe5kixkGznGbRCTnqiSh6vmqtWYStxfVPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
🔴
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129985" target="_blank">📅 12:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بعضیا هیئت عزاداری سیدالشهدا رو به میتینگ سیاسی تبدیل کردن تا به امیال خودشون برسن
تف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129984" target="_blank">📅 12:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129983">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa3359d12.mp4?token=Ej0OCupmPJit31zpYqyB9qlY5XhqKWIAFiMyRv2wS7nXj2NLL_5hido3YWTp-Irk_Ew4--6lrzzXqrEFeWUzCAJijXuDe-iDjz1h-o-uI7geCL-dN10psQgmqT1HdSskalFLLB_52h5eCGf1J-bk_GLCX_FSuHaV_Tn8cOAd4i_BhA5oMjwsF2nhHfMnmRZ7r25-Atr76_wrwVXWH_viA9Rvvd8HLMPv3lrYfRz2Qkisz79faPtayRZqxJwblTWPZAnHhrAv4FeFF1Y-tjEBgJYNmrpQi2U1SFfeJ3fgV2KGWwvE8VmTepYXaEJPthN2pXqb_tyJOH2BjtolJxNsDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa3359d12.mp4?token=Ej0OCupmPJit31zpYqyB9qlY5XhqKWIAFiMyRv2wS7nXj2NLL_5hido3YWTp-Irk_Ew4--6lrzzXqrEFeWUzCAJijXuDe-iDjz1h-o-uI7geCL-dN10psQgmqT1HdSskalFLLB_52h5eCGf1J-bk_GLCX_FSuHaV_Tn8cOAd4i_BhA5oMjwsF2nhHfMnmRZ7r25-Atr76_wrwVXWH_viA9Rvvd8HLMPv3lrYfRz2Qkisz79faPtayRZqxJwblTWPZAnHhrAv4FeFF1Y-tjEBgJYNmrpQi2U1SFfeJ3fgV2KGWwvE8VmTepYXaEJPthN2pXqb_tyJOH2BjtolJxNsDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بند دوم تفاهم‌نامه نقض شد
🔴
شعار مرگ بر آمریکا در حسینه زنجان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129983" target="_blank">📅 12:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129982">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
اینم یه عزاداری زیبای دیگه
از خون جوانان وطن لاله دمیده
🥀
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129982" target="_blank">📅 12:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129981">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be27f0a22.mp4?token=Md3jPnRC4IxwVF48fI7fua_omfWQ8VNG5wJVQENEMJEYxwgY4jxrybW4dJpDmATudvVYkUxbhnAfmp7rNepGGdLKx-fm2DMCicNAleZ4Rskj-mgaf2zH6xKMqCB6Y7XDK_0eN0nphbZJHsSQs70qiJhPFhs5i0xFdWnNJM3fK5vPUyrMXvXZCqIafgi70Qxvyzimn102NWNXqerrVYXFIWZu0tssHVMED5PiGZBfJPbaNqDzIv24Sp4FFw-bIovPOI_s3ZROzX6VwoOhu_wfpGM8MHBUlTsdhykuOXy6Fe7ypi02QLwIcieSN-dZmpc-vQhWdUSteskz08SxEU5l0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be27f0a22.mp4?token=Md3jPnRC4IxwVF48fI7fua_omfWQ8VNG5wJVQENEMJEYxwgY4jxrybW4dJpDmATudvVYkUxbhnAfmp7rNepGGdLKx-fm2DMCicNAleZ4Rskj-mgaf2zH6xKMqCB6Y7XDK_0eN0nphbZJHsSQs70qiJhPFhs5i0xFdWnNJM3fK5vPUyrMXvXZCqIafgi70Qxvyzimn102NWNXqerrVYXFIWZu0tssHVMED5PiGZBfJPbaNqDzIv24Sp4FFw-bIovPOI_s3ZROzX6VwoOhu_wfpGM8MHBUlTsdhykuOXy6Fe7ypi02QLwIcieSN-dZmpc-vQhWdUSteskz08SxEU5l0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زیباترین عزاداری این روزها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129981" target="_blank">📅 12:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129980">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اروپا به شرکت‌های هواپیمایی توصیه کرد همچنان از پرواز در حریم هوایی ایران خودداری کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129980" target="_blank">📅 12:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129979">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رئیس جمهور لبنان: مذاکرات  اسرائیل و لبنان در واشنگتن در حال انجام است و جدا از آنچه در جلسات سوئیس بین ایالات متحده و ایران منتشر شد، می‌باشد.
🔴
تلاش برای تثبیت آتش‌بس در جنوب در حال انجام است و پس از آن نیروهای اسرائیلی عقب‌نشینی خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129979" target="_blank">📅 12:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129978">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز: قراردادهای آتی نفت خام برنت به ۷۵.۷۴ دلار کاهش یافت که پایین‌ترین سطح آن از ۲۷ فوریه گذشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129978" target="_blank">📅 12:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129977">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
الجزیره: برای شبی دیگر در لبنان، خبر چندانی از تبادل درگیری‌های نظامی وجود نداشته
🔴
به نظر می‌رسد که آتش‌بس همچنان برقرار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129977" target="_blank">📅 11:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129976">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4FPr96n0a0QyaVRLW1dsQ5K0QpGBDiCHtesYCbT2zMMx0UhD6EVOOLtgCdzCYM__d1Ad6ENKqkLkCdH863ZZl0KjG86qYhTAuX2sgNjOuSc-yL3rPiLNFIYCAnFAkuIRHEa4aH9SWdKEknRzHhKoXaVyvDAGuJP5pOoaPrFlzrlSoTay255FSslD3T1UswPIUYynkvNm2_Pq1w3-lycSKuY9YdE842DHdwEAqgq8mKQxEbTB-VNn2X4z4nVwkdtS-g4MnnFjJNcecRcp_vFHmIXPA4iNcrNqVC3o1cazU8U-KMeBNEcXbcyQYs_REeAFJY0IDQ-_mDftvcVjyTXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخابره کد اضطراری توسط سوخت‌رسان آمریکایی در آسمان امارات
🔴
یک فروند هواپیمای سوخت‌رسان KC-135R ارتش آمریکا که از فرودگاه بن‌گوریون در اراضی اشغالی برخاسته بود،، در حین پرواز بر فراز امارات و تنگه هرمز، کد اضطراری ۷۷۰۰ را مخابره کرد. این سوخت‌رسان سپس تغییر مسیر داده و  به تل‌آویو بازگشت.
🔴
ارسال این کد به معنای وجود یک وضعیت اضطراری و فوری است که نیاز به فرود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129976" target="_blank">📅 11:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129975">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad6aa88dd9.mp4?token=kHMST9j6RH40WlDEEiC-2yRj58AHEtGRDiVEUEHrybX7AW7U8y4ab1I6HXO-ytldfFdiKUfijf1txszZaUvgl5EvWdH2rIqiYlfTNLEdTYKKCGjJENJm3GbycuYxVetbvl8GSyt_KgqkRygA_MCO6hk3UAsO_OydMlONsAi45t7J-jRWZLoFqQ_WsxCtSwZcpOv8O-QzYwlTkfKM8p1tcO2nk_1C0pAmNEAbGU0wzxjlpG_Y_N1KIG5xSr0dMZfZJ9gv_S1K54AuwK0VO7WjsS0h3DOFO4lUmpCDO0zKvvkrkQZxcuFLIE_u9bRA4tVY-GJxFIxdnxW5eW-PGbzrMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad6aa88dd9.mp4?token=kHMST9j6RH40WlDEEiC-2yRj58AHEtGRDiVEUEHrybX7AW7U8y4ab1I6HXO-ytldfFdiKUfijf1txszZaUvgl5EvWdH2rIqiYlfTNLEdTYKKCGjJENJm3GbycuYxVetbvl8GSyt_KgqkRygA_MCO6hk3UAsO_OydMlONsAi45t7J-jRWZLoFqQ_WsxCtSwZcpOv8O-QzYwlTkfKM8p1tcO2nk_1C0pAmNEAbGU0wzxjlpG_Y_N1KIG5xSr0dMZfZJ9gv_S1K54AuwK0VO7WjsS0h3DOFO4lUmpCDO0zKvvkrkQZxcuFLIE_u9bRA4tVY-GJxFIxdnxW5eW-PGbzrMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: تفاهم اسلام آباد حاصل مقاومت و اقتدار ملت شجاع ایران بود
🔴
این یادداشت تبدیل به اعلامیه شکست آمریکا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129975" target="_blank">📅 11:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129974">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قالیباف: همسایگی صرفاً یک واقعیت جغرافیایی نیست؛ بلکه یک مسئولیت هم هست.
🔴
هیچ سیاستی که بر پایه حذف، تضعیف یا  بی‌ثبات‌سازی همسایگان طراحی شود، در نهایت به ثبات پایدار برای هیچ طرفی منجر نخواهد شد.
🔴
درمیانه جنگ اخیر نیز بر اساس نظر رهبر معظم انقلاب اعلام کرده بودم ایران با نهایت علاقمندی به همه کشورهای اسلامی خصوصا کشورهای‌منطقه، بویژه کشورهای ‌حاشیه ‌خلیج‌ فارس اعلام می‌کند که آماده توافق های امنیتی است که با همکاری های اقتصادی پایدار شود و سرزمین های اسلامی برای تمام سرمایه گذاران، امن شده و دربرابر دشمنان مشترک خود ایمن شود.
🔴
جمهوری اسلامی ایران دست برادری و همکاری خود را به سوی همه کشورهای اسلامی دراز می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129974" target="_blank">📅 11:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129973">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
قالیباف: امنیت منطقه باید توسط کشورهای منطقه تامین شود / هیچ کشوری امنیت خود را در ناامنی دیگران نخواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129973" target="_blank">📅 11:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129972">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
قالیباف: ایران از صلح استقبال می‌کند؛ صلحی که بر پایه حقوق ملت‌ها، احترام متقابل، تعهدات متوازن و منافع مشروع باشد.
🔴
بر همین مبنا معتقدیم دفاع مقتدرانه، انسجام ملی و دیپلماسی، سه رکن مکمل یکدیگرند و تلفیق هوشمندانه آن‌ها، تضمین‌کننده امنیت و ثبات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129972" target="_blank">📅 11:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129971">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
قالیباف:  ایران آمادگی دارد با همه کشورهای اسلامی، بر اساس اصول احترام متقابل، عدم مداخله در امور داخلی، حسن همجواری و منافع مشترک، همکاری‌های خود را گسترش دهد.
🔴
ایران از هر ابتکار عملی برای شکل‌گیری سازوکارهای مشترک اقتصادی، تجاری، مالی، علمی و امنیتی جمعی حمایت کامل می‌کند.
🔴
ما در سخت‌ترین وپیچیده‌ترین شرایط، دوستان و شرکای راهبردی خود را تنها نگذاشته‌ایم.
🔴
برای ما، آتش‌بس در لبنان به اندازه آتش‌بس در ایران و در ادامه، خاتمه جنگ در لبنان به اندازه خاتمه جنگ در ایران اهمیت داشته و دارد و باور داریم که ثبات واقتدار در هر نقطه ازجهان اسلام، به تقویت عاملیت، عزت و ثبات در کل امت اسلامی منجر خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/129971" target="_blank">📅 11:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129970">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: مذاکرات فنی در سطح کارشناسی هفته آینده با میانجیگری پاکستان و قطر از سر گرفته خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129970" target="_blank">📅 10:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129969">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان: در حال برقراری ارتباط با دو طرف آمریکایی و ایرانی برای اجرای مؤثر تفاهم‌نامه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/129969" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129968">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8-yHVQnWRmnklYeLlqmw5NRPjY8Af1YFPAyZDjwj9lkNsnJCs9UrrqoyuluLWYq3oZBc7cJjb0L-lHwxq8kvv6OjayTtNRFunEuyDrKQTaS-fmsr5GX1SCDVGSCUKEh6IEZCv3uEtpnVGZ78BTFHAbk--HJres9-keGH2ZNRa02CvPQAoNjl72AKX9JeEwYEtjG-z1Fq4kaoplNF3P3e6Wuen1bQ4E71SoyoF9D_VDAvn5nJ8Eet_wLgKx89QBrgYE_oCxOM0GSLBM7dz75i62Z97e7Z4786gARS8mAtsBY22XhkpMY19U2YMum73MeHLvK61fRkBrH8e8Zaqtv3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون وزیر ارتباطات: نسبت دادن اختلالات اخیر بانکی به بازگشایی اینترنت بین‌الملل ادعایی غیرکارشناسانه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/129968" target="_blank">📅 10:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129967">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: از تأسیسات هسته‌ای ایران بازرسی خواهیم کرد
🔴
ما معتقدیم که بازرسی از تأسیسات هسته‌ای ایران در اسرع وقت بهترین گزینه است
🔴
اولویت اصلی ما مشخص کردن محل ذخایر اورانیوم غنی‌شده با خلوص بالای ایران است.
🔴
ما از محل اورانیوم غنی‌شده با خلوص بالا اطلاع داریم، اما مهم است که ایران ما را از آن مطلع کند.
🔴
به زودی با ایران برای تعیین تاریخ بازرسی‌ها و جزئیات مربوطه مذاکره خواهیم کرد
🔴
آژانس ما بازرسی را انجام خواهد داد و این به تهران بستگی دارد که واشنگتن یا ناظران دیگر را دعوت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/129967" target="_blank">📅 10:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129966">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBwa4sI9Vj7OvsrdUplXZC0wmO184XSCEruTESI7Q_46T517H27ySVNd8GO65m4fPykMTL016Ei8IeETDA4qEB8HgY1AtKZHt0c18wxr_Gw4823Nw3UHKCR40mipOSZNcM9plzt3f8W7BEjhFGY8y1uG33S1zdhQOVa8eqjPvEs1tezaj3NHBkz9yjtE4wWsCCH9mLGu7KDLQHgPCri2n-DvgulFQJ1Ru-APg7z4dAycOmp2Vos7zqaPHj3KKTXkbxfxjwWRq6DuKZQpXsV_JThroHBKAJ8xlTzDxpudmOR7knybcYrPC0JkznAYsNOBsM96xIKRsljE9bumhiFcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: آمریکای زیبا هرگز یک کشور کمونیستی نخواهد شد!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129966" target="_blank">📅 10:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129965">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: همه از نتانیاهو خسته شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/129965" target="_blank">📅 10:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129964">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aacf80584.mp4?token=Dz2CLJzi5-5TIInAvFMD60Vo61XrpnqxGYPUCefNtSwlg6BLMHfIPt9yinIVYxgS7xn-dcA6DIC52L0gNmGyMw9v-NTmRWwFdzX7QsOTJM92emqj9oLxSErgKDbEprkdGVFihgw-0_t3p0Chyk2cHihitd9Bp-P77bCYUsAgDOyxupQdjQSbewZbAhmWm9c50DN3Zt5HPQKMN4i1tS2ECbGJDalNuR49WMcR-bp7Kz3xjjkv5tpJaag6L7Wc1F_bpX0C0MwaEForKXpVmimO1knXTFX3eFpRx4iO8ZVcL3_ZWotCn0_9kF50I4X4q9QQh2uETFh-bZqoYrgSAkmp8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aacf80584.mp4?token=Dz2CLJzi5-5TIInAvFMD60Vo61XrpnqxGYPUCefNtSwlg6BLMHfIPt9yinIVYxgS7xn-dcA6DIC52L0gNmGyMw9v-NTmRWwFdzX7QsOTJM92emqj9oLxSErgKDbEprkdGVFihgw-0_t3p0Chyk2cHihitd9Bp-P77bCYUsAgDOyxupQdjQSbewZbAhmWm9c50DN3Zt5HPQKMN4i1tS2ECbGJDalNuR49WMcR-bp7Kz3xjjkv5tpJaag6L7Wc1F_bpX0C0MwaEForKXpVmimO1knXTFX3eFpRx4iO8ZVcL3_ZWotCn0_9kF50I4X4q9QQh2uETFh-bZqoYrgSAkmp8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ که توی پیجش قرار داده و مضمونش بر اینه که هیچوقت نمیزارم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/129964" target="_blank">📅 10:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129963">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وال استریت ژورنال :  اسرائیل با فشارهای آمریکا برای خروج نیروهایش از جنوب لبنان روبه‌رو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/129963" target="_blank">📅 10:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129962">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
قالیباف: بعد از جنگ اخیر، شرایط منطقه متفاوت شده و باید با نگاه دیگری آن را دید
🔴
در گذشته برداشت برخی کشور‌ها این بود که نیرو‌ها و کشور‌هایی که از هزاران کیلومتر دورتر وارد شده‌اند، می‌توانند امنیت منطقه را برقرار کنند، اما بعد از جنگ اخیر مشخص شد که نمی‌توانند و خود از عوامل ضد امنیتی هستند
🔴
باید از این نگاه جدید در منطقه استفاده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129962" target="_blank">📅 09:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129961">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نخست‌وزیر قطر: ضرورت ایجاد یک خط ارتباطی میان تهران و واشنگتن در دوران پاک‌سازی مین‌ها در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/129961" target="_blank">📅 09:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129960">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نخست وزیر قطر به فایننشال تایمز:
مذاکرات سوئیس (ايران - آمریکا) زمینه را برای مذاکرات دائمی حل و فصل بحران فراهم کرد و کار تازه آغاز شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/129960" target="_blank">📅 09:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129959">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE1sQPtFg_5pmZRENTlup6RQ4-uIielyNcbIDhWH6P2zZAvkSSs2mAOz-3JCeckvgsPdquCKTifTQ7Z9GVhf_VYg1I4oAJkPmeniw4FoFVQ__wFUG94an-qKIT8M2J_afgB9a8c3x-Z-RzUhIbmapEbqtvqSLu9ydyz4FwBntSg7VtfWSsB-u345f6Vi_0IX1lfkNux-lMeJyXdjDdC3JnvRJdLa_XajB6g0kW0nnsshimu19V6ny9ycqbv98UnEdziLX_HjSHrRt6BnpEYbSV3-W58yx9lTY0W_q7caJzChgS7ofCNUxTOkFjjP-9hsKcni0mBtbj-y4nUeeeeURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد ترامپ از پمپ بنزین های آمریکا: قیمت را با کاهش بهای نفت پایین نمی آورند
🔴
ترامپ در شبکه اجتماعی اش نوشت:
شرکت‌های بزرگ نفتی قیمت‌های خود در پمپ بنزین ها را به اندازه کاهش شدید قیمت‌هایی که برای نفت می‌پردازند، پایین نمی‌آورند.
🔴
این قیمت‌ها مثل سنگ سقوط می‌کنند! به عبارت دیگر، مشتریان «سوءاستفاده» می‌شوند.
🔴
من به وزارت دادگستری دستور داده‌ام فوراً به این موضوع رسیدگی کند. قیمت بنزین باید خیلی سریع‌تر از چیزی که من می‌بینم کاهش یابد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129959" target="_blank">📅 09:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129958">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f466cb2cd.mp4?token=gXwu7weUH6a5RsqpHbzzostTgBKQFKkPBtbiXV_8fZmuKWJhlsM1VzKIp43mQa-AXjzoM7S5M3JI9VxqwWHSJJYckARoA0TQdEbEsRI4X6zbg8lJ22XkV2oxwyFueN1ouvK-O1jy-MRUnvsbynBkW7ZGBZGcREfEOlauT-yN_7tK_jxEi6ObhCRF_M4SRgrMwZGcGSDpn-UytNntTtACQIaMb5aZ4f5Tzm_TVTvl8nnxskt5szGS76MOKQbxC1u0lW9BXEaEJkzBTGKg7LqWA4H2q4VHJ-yeFLbqpQlgJBGjNPJX_aOWNGjfxWacbXiSqec-IRkOTYk96hR38XrU-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f466cb2cd.mp4?token=gXwu7weUH6a5RsqpHbzzostTgBKQFKkPBtbiXV_8fZmuKWJhlsM1VzKIp43mQa-AXjzoM7S5M3JI9VxqwWHSJJYckARoA0TQdEbEsRI4X6zbg8lJ22XkV2oxwyFueN1ouvK-O1jy-MRUnvsbynBkW7ZGBZGcREfEOlauT-yN_7tK_jxEi6ObhCRF_M4SRgrMwZGcGSDpn-UytNntTtACQIaMb5aZ4f5Tzm_TVTvl8nnxskt5szGS76MOKQbxC1u0lW9BXEaEJkzBTGKg7LqWA4H2q4VHJ-yeFLbqpQlgJBGjNPJX_aOWNGjfxWacbXiSqec-IRkOTYk96hR38XrU-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: همسرم به من می‌گوید لطفا نرقص، اما من عاشق رقصیدن هستم
🔴
رئیس‌جمهور آمریکا در ادامه گفت: همسر بسیار شیک‌پوش من به من می‌گوید؛ عزیزم، لطفا نرقص! این در شأن ریاست جمهوری نیست. اما من می‌گویم مردم عاشق رقصیدن من هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129958" target="_blank">📅 09:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129957">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
اکونومیست: نتانیاهو در نهایت مجبور است با توافق تهران- واشنگتن کنار بیاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/129957" target="_blank">📅 09:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129956">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix-6PZoiL56cNZHW3qx02_EwtUVionBR1bLa3ByvkJVpii2T69hpmYkTltcNHIwfBZEHFr_HoeLTa5775r3_d-UNbKyfFDSEIZ4z9rxaOPZAR_haA4yQjkRK4b3DdCd1wwtbhu00OiRk89Y2GPQHRwbfMpSa50d6P9CrJjB2qKyMaIiy57ewvNfesDBnTp16CrGWecddxvbEGHGuxzY8zg3bBHydd_ARx9BP7WxCgNeNzl_g59a2T_Ldznzl9MY-7toBacYveZx_MJmz3hzls42pnmmJEfAuvsZwnSg_tjmjOKOPSb0svSkRXBk2Ut4vgLrpSvoob-48VLQOoSpsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش سناتور برنی سندرز به تصویب قطعنامه غیر الزام‌آور اختیارات جنگی در مجلس سنا: کنگره بالاخره کاری را که باید ماه‌ها پیش انجام می‌داد، انجام داد: به درخواست از ترامپ برای پایان دادن به جنگ با ایران رأی داد.
🔴
قانون اساسی واضح است: روسای جمهور نمی‌توانند به طور یکجانبه ما را به جنگ بکشانند. این مسئولیت کنگره است.
🔴
زمان آن فرا رسیده است که کنگره سرانجام مسئولیت خود را بپذیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/129956" target="_blank">📅 09:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129955">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نخست‌وزیر قطر: امکان سرمایه گذاری کشورهای خلیج فارس در ایران طبق بند ۶ تفاهم نامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/129955" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129954">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
مهر : اختلال خدمات کارت‌محور بانک‌ها رفع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129954" target="_blank">📅 09:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129953">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
لبنان و اسرائیل امروز هم مذاکره می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129953" target="_blank">📅 09:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129952">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
لوفت‌هانزا: تمایل شرکت‌های هواپیمایی زیر مجموعه‌ ما به ازسرگیری پروازها به ایران
🔴
بررسی و برنامه‌ریزی برای گنجاندن این پروازها در برنامه زمستانه این شرکت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/129952" target="_blank">📅 08:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129951">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dae873392.mp4?token=Fd0ol51LdSFNTHBuwbqBcgULWEpoBnBDXp8pE5yhyVvW_3woQ8CyiNSY2468eIowaNDO1ooK_yZPBNF7mBCJb3C8E9N-2X8AR7vh-BiMZToMTToSDozFkHvlRBUHZ_dkDj2zMXsI6Yvu2HgElpsV2JhbBxkEOuaZlVTipf82RbDvZgKwcWkAOAPqn4h_5iqowFxYnVNCxck4Zn30QVJrfLcEYIT9HEPWpcSZBDVQl9Ijk0rBVLQP2bXWAHkPGtBpYauqzbGY8C4uqpAKkAlzkjreaGlC7nUR1aIHTCQXvuabVfYIftZ-mXY9mV5kHsDmvOCmb81X749zVo2xM3bh5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dae873392.mp4?token=Fd0ol51LdSFNTHBuwbqBcgULWEpoBnBDXp8pE5yhyVvW_3woQ8CyiNSY2468eIowaNDO1ooK_yZPBNF7mBCJb3C8E9N-2X8AR7vh-BiMZToMTToSDozFkHvlRBUHZ_dkDj2zMXsI6Yvu2HgElpsV2JhbBxkEOuaZlVTipf82RbDvZgKwcWkAOAPqn4h_5iqowFxYnVNCxck4Zn30QVJrfLcEYIT9HEPWpcSZBDVQl9Ijk0rBVLQP2bXWAHkPGtBpYauqzbGY8C4uqpAKkAlzkjreaGlC7nUR1aIHTCQXvuabVfYIftZ-mXY9mV5kHsDmvOCmb81X749zVo2xM3bh5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از کیروفسکه، کریمه، در میان حملات پهپادی اوکراین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/129951" target="_blank">📅 08:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129950">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OWjQgyqQoHC4XBnJis6NlM1SDyFwVgKPW4OOR7UH_skeY0jASCCDxAfq5F6Wqh-_9WDOWtTlsyKBvGqIw7rmE_lRxdTLxHIJgvrxYWr4nBH2xonhTwSYBz5SWhw7akkJ4JOQNwG8H3Oc2qNyjIAwj-Qq6D4_8F2KF3nlCaK1mH36HEb97-_MKtyBHnE-qag-96jLBLjzSsqC2C4P60cdy9kY188IUojTNfKMHUWFhP2hgeJzI1Y7ZJkgzGHdcV3CLLnwz8ldOvV5Dz8bSVWPImXxvkSij2-8ikZq1Ni3_9LvXLIE1yL8x6wbxPthExW9mQbTsIrbMtefkPAkexpLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه ایالات متحده، تحریم‌های اضافی علیه «گروه مدیریت کسب‌وکار اس.آ.»، یک کنسرسیوم تجاری متعلق به نیروهای مسلح انقلابی که اکثریت تجارت کوبا را کنترل می‌کند، اعلام کرد؛ به‌طور خاص بخش‌های این کنسرسیوم که در بهره‌برداری از ذخایر معدنی و فلزی کوبا و بخش‌های مسئول انتقال دارایی‌های مالی و فیزیکی نقش دارند، تحریم شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129950" target="_blank">📅 08:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129949">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnnGgLC777H7Vm-iGfOaQC8I4xeMbVfgIPapyhZTYF6m6LcGBaZgslVSkcjG-ekmwQ977y57Hcc9v-0NBw8VSq3o7B2yub8DQMvKfKcfr_Pq0tlxwTxrDADA-bW4ha6CVi0Wx3_2lDfsVMTJT5Sacm6bT9_xbhaPMEUznIW8dYzNJ_hKMzzvHX6YuKMtZcGIQi4RaWWwOZjshBrP2NJXlqvOUNpjjSxYMdIkUBHK7Z3rkLPc8Hp6gANzLqnh890Fb7i2PZUe5uAN57_R_paFCPSkoCPbTS4vaIF-6hTUUWD9CXU3uVz7gQjcNtGL9Xh2eDELuZMwXnGHAyjhCOvAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش ترامپ به تصمیم سنای آمریکا/سناتورها کار مرا دشوارتر کرده‌اند، اما من به هر شکلی که باشد آن را به سرانجام می‌رسانم
🔴
ترامپ: من ایران را کاملاً در تنگنا قرار داده بودم؛ در آستانه تسلیم بود، حاضر بود تقریباً هر چیزی به ما بدهد و برای نخستین بار در دهه‌های اخیر، احترام زیادی برای ایالات متحده و رئیس‌جمهورش، یعنی من، قائل شده بود.
🔴
اما سنای آمریکا تصمیم گرفت در زمانی نامناسب و بی‌معنا درباره قانون اختیارات جنگی رأی‌گیری کند؛ اقدامی که به بزرگ‌ترین حامی تروریسم در جهان این پیام را داد که ایالات متحده از کاری که من با آن‌ها انجام می‌دهم راضی نیست و باید متوقف شوم، و به این ترتیب به دشمن کمک و دلگرمی داد.
🔴
چهار جمهوری‌خواه بازنده همراه با دموکرات‌ها رأی دادند و ایران از افراد من پرسید: «همه این‌ها چه معنایی دارد؟»
🔴
این سناتورها کار مرا دشوارتر کرده‌اند، اما من به هر شکلی که باشد آن را به سرانجام می‌رسانم، چون همیشه کار را به نتیجه می‌رسانم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129949" target="_blank">📅 08:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129948">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJzTonVTeyqu4VUMYFKF-nXoBqdxyd9cXDc1AkX3g8w6Ts31Tw-g80B9-puQbo5W61hA5s8La9WD4o4W5Ld9P_S87r9KSFKuCm8xAsMY3f0_-A8OQMrBVZOLbGUX23B6KX8uqIHZacNBc8evUWqZJxBI-JB7ao4C_ekZECFmDFFE5_yY5tc2A5cM0fDbShtA75kMSUZW9fxV7SzUNpQEvBhHkwU-cplE0rP0KavVn4UbTKJJ-Gbb5RMEwzmwZa6sKn-pWbzSYjZ_6UGccKM2-8WFaHKibd7hPXEafD59hbPzQI4KppwSOlAsbXMlL6p5sxkHlEvorltuNjiiMLOThw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم جونگ اون، رئیس کره شمالی، اعلام کرد که برنامه تجهیز ناوگان دریایی این کشور به تسلیحات هسته‌ای مطابق برنامه‌ریزی‌های انجام‌شده در حال پیشرفت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129948" target="_blank">📅 08:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129947">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5wUVAjq71eJK71yw2KBwYowdtV6FB-9Ae31PvY8WwWGhFMIs9N3UM_fBPqZ7aMnC_m7DvCT2Tb0WEY9Di0tq5CHhxeQB14OpTkEhj3BpiAIxO6LcB1Fd-PvwQIKgiU0wWKAzIbTLm7spyzKt-UcP0kna3t1reevpsFvg15tPdEb0w52zZ3J7HScw6M2JyADj2afq8Fy-5bWCqOrIB8gVhWA8yJ58GbQJhzosGATs_JpO8GFKLGkKxzIFoydMWWmhPDrtVqY9zeXYbKTUYycwhoE3_xgMu_eHDLdwGfw0wOasjL4DxVziM5gJaectUI1CYcRi2nrrjOf2Fso0hpB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آای هیمتی:
اگه ذرت و سویا آمریکایی کیفیت خوبی داشته باشه، چرا که نه! میخریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/129947" target="_blank">📅 08:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129946">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miwle2PtcjU3gPt1baeQYW2YEYOt38eskwsG4hvGkeQqOOLt7_7oggCNpKl-9zxv9JuzSz8IqEIGV780RwXQ71xFSuR7Dq4R9dnB4E0zBxCL8b9tu_W0d2h7AEMnckxAZn0k_JE-hBktK3pybRKoDBEAEXNNZGzq39OwsplgVqpVvb1o918lAilEGhVHIlCGPI0T9G3Qj9JN8par93AsLjWs067wxYDLQRbwNK6VNFUekfHyxy8TlsrLFkdLiAIE8PTVCJ6zloeJ2QaCrJSWb33FB5mN-m4_JI_K5UbXYQy1mVo6UHiPqhgK5tcB6paFYG6fj7-zmaFTxtS34REMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری دنیا جهانبخت از حضور در مراسم عزاداری.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/129946" target="_blank">📅 08:17 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
