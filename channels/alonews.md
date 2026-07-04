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
<img src="https://cdn4.telesco.pe/file/S3IdUroGKnTseHkP9ZLAZKAWQvGTbB9RI1irxMNz9_cnkg9iA97KLB-GBZGZwSj2vT6SUuQQV8T-tybNH2Cytf_LxZ0l8jqoJfJInd_Bf_ZWENIiYgntSi0jZEJBC9LPG-9hMIbpgMWnSzaRiUY5tZY0XuBH728vLdx4mvecXYNqgajYbt6YpXz08nW0y4IC071Hx1fXnMCwHOOD2O9peum64VA8s6UpMlNUlS8sFFouElzgLba0kpH7KnRFcAW25sPbGkMKS90dHZNDUtzb6h76FrwGAd8hjZ1EmSt_PsZNRtP7RaL2WC247Udx97RDiw_Bc7fYQpDfSw1999iRiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 20:24:41</div>
<hr>

<div class="tg-post" id="msg-131782">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c668b6cf80.mp4?token=lZ-YbrEUE_vD-zreCp5OLB6aiyyibcs0LVgZjhoLBHljeEkcGue7A9fA7fQPZQMxtmVl7Uk2qU9ygdYxapKh9ZoTUyyp4W1V6J2ATXDDhhVrFhAgCCd59unT3cp34vHIhSfxXPCNtOibIDHNfPdWmzrxuurSIGlDyMiLLOjXB6EeaSPaDHf8qcE-3EcLEgL74sgB-xtN4zagwm3IrZQHJhoQmV2bU5FNh1W8kMGJdjCgOzG2PN4i5JOoltZPQNsXfXWsNCv_RzLphQcoDz9d0SP4ZUts4L1CFWmDA5w0qOLvCRcn6EEPH2ajiMPCvaa_-rJEOAbCizEv7ZLkgUIzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c668b6cf80.mp4?token=lZ-YbrEUE_vD-zreCp5OLB6aiyyibcs0LVgZjhoLBHljeEkcGue7A9fA7fQPZQMxtmVl7Uk2qU9ygdYxapKh9ZoTUyyp4W1V6J2ATXDDhhVrFhAgCCd59unT3cp34vHIhSfxXPCNtOibIDHNfPdWmzrxuurSIGlDyMiLLOjXB6EeaSPaDHf8qcE-3EcLEgL74sgB-xtN4zagwm3IrZQHJhoQmV2bU5FNh1W8kMGJdjCgOzG2PN4i5JOoltZPQNsXfXWsNCv_RzLphQcoDz9d0SP4ZUts4L1CFWmDA5w0qOLvCRcn6EEPH2ajiMPCvaa_-rJEOAbCizEv7ZLkgUIzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت مترو بهشتی تهران: شعار مرگ بر اسراییل
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/131782" target="_blank">📅 20:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131781">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
به‌دلیل افزایش ازدحام جمعیت، از ساعاتی پیش قطارهای مترو در ایستگاه مصلی توقف نمی‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/131781" target="_blank">📅 20:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131780">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
پزشکیان:
اسرائیل به همه کشورهای منطقه حمله کرد و عامل بی‌ثباتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/131780" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131779">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سفیر جمهوری اسلامی در چین:  پکن از تسهیلات ویژه‌ ای در تنگه هرمز برخوردار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/131779" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131778">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcLdwhd1ZO2c0NO0q7QD7faXyaXwNZ1BLMyb75bCbiLSpib0KSI4GcimuVTYB5ZYU-EBZQoXuM_PguQ3ukbjB2iX2UDLSTUaZEMBkOjvz1WEvhHfzKw8Ex459KXUXXQtqt-QF4-s7ydBwRLAY169osFzLCl3M9obHtvSjqvW10Zk-3WVBqVkYOaMxrIeU5cWi7MafW6InMK0jz-ynw-b1UsaH-pZFWoU7Anx1Ju5hX3qa-NgD-0z0G2Uc8k_N6p4HbBmUuGx7fSFM0eR5IkKDOJrf4-LqAqP21XYO8Tnd83v8y-l4QKAUwZePdd1d4C-VfcBkye7-n1XLijiZjOIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا گوشی آیفون علی نعمتی در مراسم استقبال در فرودگاه توسط حامیان حکومت  دزدیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131778" target="_blank">📅 19:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131777">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNDZECTpRZWan7hPuzEM8ZiZJ-PAnI7bPgHq-2Jxh4OUDGBNH01CxdO9QC7pPGMDAEjiLutzm8vZSnJE5c648ML_HN6g4s_7uDgtTe-CfIZWTAH3RfsO93FaK7wxozkjQKOMJt_DcGQFvaDcDYPQw8t1rlWFh1iXEnDd9URVJVyf-qKgm2zyV1if3RtfEXo7Z3kBzvF22oHUGG8NZyUxs9moTssvSnRGl82c66ry-iu9N5j_yj7dorQHIEp7H4Nk5INUN-P-NXLzLLUWWXDmAMBfPVZP8vZNvy5Y9ubFw-sA7ldZmV7QELYOhiW-YTnoCE8ntxBVA4asmJ3tHeBeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
مردم برای یه لحظه هم موضوع انتقام خون رهبر شهید انقلاب رو رها نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131777" target="_blank">📅 18:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131776">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfMcuHkCA0LsvgURfrpZiIUveH34TzUZik0TQf9PTfle0z659kns7NSqOCT6PziNDr8FnFw5FQZoBzEASyjvhn9RzllW01RoydaGpavRyHsrPoQmXSFbVSkRTvmGzjfvHXSapJ25nxNvm8oErCcufR9Ccra02nenPprqB1laPPzCiSTlM541_K1OQgiDPfNYXgN-4JoqzOm9ndfbXDeQUZi8ji43qp4IwNzHshj5qZS0iZO2EbyB3j0Juql0kxY1M15vyyk9sSqZ_V6rOfid4TOTsHsWJ7B9_XiVvIKIjEe0E8uGKorHxIN_R9ZjzQLtiyruTE4Rr4w-Z4jkrNEGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌ها اعلام کردند که یک فروند بالگرد MH-60S Seahawk نیروی دریایی آمریکا که از ناو هواپیمابر USS George H.W. Bush به پرواز درآمده بود، در روز چهارشنبه در شمال اقیانوس هند سقوط کرده و یک خدمه از چهار خدمه‌ی آن مفقود شده و تا به امروز پیدا نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131776" target="_blank">📅 18:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131775">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb289f43ad.mp4?token=er2TBsep6_AsI1tZhcJNPEX5uNzRFy1Zwf2CA0I_wgIk0eviskjpYiItroZ9EcIVP69KLxrFKTzq1gqPlMGpvVQShAh1dhJ-SJezdxl5Qr-D6MXjvThm-rmcXji27xxjaQDaTQYe3yRjh6xJsord0jfBVeAqMK_kjbuVT6mkixf3obcwewH3EfayhXGKzYnjufUsuZqB8wc0URRAoG5wdX3FPcKj7GUkWFwR7rBPW4TwWal14ZXlEb9weY5T6JOEr13AANlnlwl0hvQ0igGkLsCEDAccFfpd6bQeyKNFJ8o8BsQsEwP0ojwXbdidq8BBTws70Nbo6xCEOkxcVPJVMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb289f43ad.mp4?token=er2TBsep6_AsI1tZhcJNPEX5uNzRFy1Zwf2CA0I_wgIk0eviskjpYiItroZ9EcIVP69KLxrFKTzq1gqPlMGpvVQShAh1dhJ-SJezdxl5Qr-D6MXjvThm-rmcXji27xxjaQDaTQYe3yRjh6xJsord0jfBVeAqMK_kjbuVT6mkixf3obcwewH3EfayhXGKzYnjufUsuZqB8wc0URRAoG5wdX3FPcKj7GUkWFwR7rBPW4TwWal14ZXlEb9weY5T6JOEr13AANlnlwl0hvQ0igGkLsCEDAccFfpd6bQeyKNFJ8o8BsQsEwP0ojwXbdidq8BBTws70Nbo6xCEOkxcVPJVMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهباز شریف: موفقیت ترکیه موفقیت پاکستان است.
🔴
پیشرفت پاکستان پیشرفت ترکیه است.
🔴
ما زبان‌های متفاوتی صحبت می‌کنیم و در سرزمین‌های متفاوتی زندگی می‌کنیم، اما نوری که مردم پاکستان و ترکیه را راهنمایی می‌کند، یکی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131775" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131774">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
هشت جت تهاجمی A-10C Thunderbolt II که در خدمت وینگ بیست و سوم ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131774" target="_blank">📅 18:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131773">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ارتش روسیه : ما 5 روستا رو تو شرق اوکراین تصرف کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131773" target="_blank">📅 18:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131772">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شریف :  با افتخار می‌گوییم پاکستان و ترکیه، دو قلب در یک روح هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131772" target="_blank">📅 18:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131771">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شریف :  با افتخار می‌گوییم پاکستان و ترکیه، دو قلب در یک روح هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131771" target="_blank">📅 18:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131770">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سردار رحیم صفوی:  بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131770" target="_blank">📅 18:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131769">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
اردوغان: ما از نزدیک تلاش‌ها برای برهم زدن توافق ایران و آمریکا را زیر نظر داریم/ نباید به اسرائیل اجازه داد دوباره بوی باروت و خون را در منطقه ما بپراکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131769" target="_blank">📅 17:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131768">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
اردوغان : وقتی آمریکا و ایران توی اسلام‌آباد به توافق رسیدن
🔴
دنیا نفس راحتی کشید و نگرانی‌ها کمتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131768" target="_blank">📅 17:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131767">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66ce12768.mp4?token=u1rGH4et9PkRumyEzVuKh4AHCboAZbiLqDo6K6u9BbaM2OvJqVGTh7iKjO8f8I_CjMsgsKXV5dHfAPlJ6szwHZxtN5c1gEFDGOoAko4d7aikehzIMa8o9AnOtQs8tSB9R7BUH3chooLipCGepmuLo-ZwFfhrrQzWSw1tnYfvX3Vibyl32mqsp05QuHVf5NC2Rv5bpkSYmJAO9b8lVXc3PVapZXeENseQSzkIL_GMa8vkVA02cTe-KwSEUds5qmSIECUADrbKbemMdCASA3hgvPS8J9RSxYrrS4M4RJQ2vUF2_UYP0_l-3damoAY9UrAY0OlgEpBhxAIyevtR-AwyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66ce12768.mp4?token=u1rGH4et9PkRumyEzVuKh4AHCboAZbiLqDo6K6u9BbaM2OvJqVGTh7iKjO8f8I_CjMsgsKXV5dHfAPlJ6szwHZxtN5c1gEFDGOoAko4d7aikehzIMa8o9AnOtQs8tSB9R7BUH3chooLipCGepmuLo-ZwFfhrrQzWSw1tnYfvX3Vibyl32mqsp05QuHVf5NC2Rv5bpkSYmJAO9b8lVXc3PVapZXeENseQSzkIL_GMa8vkVA02cTe-KwSEUds5qmSIECUADrbKbemMdCASA3hgvPS8J9RSxYrrS4M4RJQ2vUF2_UYP0_l-3damoAY9UrAY0OlgEpBhxAIyevtR-AwyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا کِیر استارمر می‌گوید که نمی‌تواند فاش کند از چه ژل موئی استفاده می‌کند زیرا این یک «راز دولتی بسیار سطح بالا» است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131767" target="_blank">📅 17:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131766">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123544aa58.mp4?token=mh1wdv6TbtzMBnc9IbSwDCpynSiYIZxYEes6-YbYhIXcs87EBADcCGChPxX-wYcmmk5Hh87ohVctvXsL13OO2tyf4eeuXisN6Sud4r9VZpiuWg6tQV2SAlYTLkH3NI7bia9pRHJ-MwOrjEke9_9eOncZQPWd6ZBEYuCV4A428NVCYjj13Vq6LdhRYr_XRgFv2pF1Il0gW0VrmEky8RVxTh6spEx8i1GYviGMBi-6Bks770lvqwE935J6X1adkuDxUB_bRBP7L4LeJXWXdByStvrDZSgeJwv1V7B6XnhBEzE7nC0JSMPJ5tvJLVUW89nFdK_np_3gw09-BoQ7hbMTyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123544aa58.mp4?token=mh1wdv6TbtzMBnc9IbSwDCpynSiYIZxYEes6-YbYhIXcs87EBADcCGChPxX-wYcmmk5Hh87ohVctvXsL13OO2tyf4eeuXisN6Sud4r9VZpiuWg6tQV2SAlYTLkH3NI7bia9pRHJ-MwOrjEke9_9eOncZQPWd6ZBEYuCV4A428NVCYjj13Vq6LdhRYr_XRgFv2pF1Il0gW0VrmEky8RVxTh6spEx8i1GYviGMBi-6Bks770lvqwE935J6X1adkuDxUB_bRBP7L4LeJXWXdByStvrDZSgeJwv1V7B6XnhBEzE7nC0JSMPJ5tvJLVUW89nFdK_np_3gw09-BoQ7hbMTyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جکسون هینکل فعال رسانه‌ای امریکایی در حال توزیع شربت نذری در مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131766" target="_blank">📅 17:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131765">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
به گزارش بلومبرگ، سفیر ایران در پکن اعلام کرد چین و دیگر کشورهای دوست هنگام تعیین سطح و نوع هزینه‌های خدمات دریافتی از کشتی‌های عبوری از تنگه هرمز، از «ملاحظات ویژه» برخوردار خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131765" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131764">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ادعای الحدث به نقل از منابع آگاه:
دور جدید مذاکرات آمریکا و ایران در تاریخ ۱۱ ژوئیه [۲۰ تیر] در پاکستان برگزار خواهد شد.
🔴
دور بعدی مذاکرات بر موضوع تحریم‌ها، دارایی‌های مسدودشده ایران و پرونده هسته‌ای متمرکز خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131764" target="_blank">📅 17:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131763">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAMxTg3ljJiV4Pimu9fNAovRlAzYeUV7dHS57gyZC27kHmIwQKV1AaAmB0Dp_buU6lnQX6hSdbPtnBqQnnF2RjSf_PQwjXdgrpbhXdHKdgeMUDIR79ycA9SNsIPDM4SfJkgOuCJPuKgMZitFIc8VaipX53tfC5qRhv1zQBoDVUkpVe3HLze6htUrwcnRr8IZJ2XkHbSRbteBtzdhKE6GihcS_LTaRVtwbAs5qBCEj9aGLXef3HmVVmUIWiqbPfYwXtX-4sZ4g6wocJw59AHmF0JxVbAHqUDrghXPkdPtRrBxZ8TEN0m3lvko73x8nRmBaNALmCYpnRxQS703T26IJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز مستقیم هواپیمای باری 17-C نیروی هوایی ایالات متحده از پایگاه هوایی نواتیم به پایگاه هوایی الظفره امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131763" target="_blank">📅 17:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131762">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ec205bc1.mp4?token=t7i-gIjMtw14b0qCUWMqQkXg__dgyNj3q09cR2HC6idbMmk96kmT0PoLxQ0ZZkuZMDDkMT4cZHslz1cfl72csxVoL3ceCPuRThHkrfY9Ma3hAwpOzP60Eor8Gyzt4cS2wCIeB6aMMTWB1gA1mC-VxY-xVMGrX35LMJx8IjJzIv4W-O_vVs3vCK4WIHaRadth8x8GPfE4OXiyT4XFEVMgrN2q9rOKYDnR8sK_dwzX9E8-IuQMic9iGd0OcLEqGy5eBIKufeKS2K6sAhHwmfxB-QWR2f0ZilM51OXvzhL8HbMPY4Yc5COvdEY-SNV2xDfkuNOkZLB3aKjv-ym_2cmNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ec205bc1.mp4?token=t7i-gIjMtw14b0qCUWMqQkXg__dgyNj3q09cR2HC6idbMmk96kmT0PoLxQ0ZZkuZMDDkMT4cZHslz1cfl72csxVoL3ceCPuRThHkrfY9Ma3hAwpOzP60Eor8Gyzt4cS2wCIeB6aMMTWB1gA1mC-VxY-xVMGrX35LMJx8IjJzIv4W-O_vVs3vCK4WIHaRadth8x8GPfE4OXiyT4XFEVMgrN2q9rOKYDnR8sK_dwzX9E8-IuQMic9iGd0OcLEqGy5eBIKufeKS2K6sAhHwmfxB-QWR2f0ZilM51OXvzhL8HbMPY4Yc5COvdEY-SNV2xDfkuNOkZLB3aKjv-ym_2cmNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز : هم‌زمان با مراسم تشییع رهبر جمهوری اسلامی در ایران ، آمریکا جشن دویست‌وپنجاهمین سالگرد استقلالش را برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131762" target="_blank">📅 17:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131761">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
به گزارش فارن‌پالیسی، هند و ایالات متحده ممکن است در برخی اولویت‌ها اختلاف‌نظر داشته باشند، اما رقابت جداگانه هر دو کشور با چین همچنان به اندازه‌ای جدی است که همکاری راهبردی بلندمدت میان دهلی‌نو و واشنگتن را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131761" target="_blank">📅 16:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131760">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کامران غضنفری نماینده مجلس: پول دادن به مداحان که دیگر در تجمعات شبانه حاضر نشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131760" target="_blank">📅 16:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131759">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
روزنامه تلگراف گزارش می‌دهد که یک ابرقایق ۱۳۳ میلیون دلاری که گمان می‌رود به ولادیمیر پوتین، رئیس جمهور روسیه، مرتبط باشد، به سمت بندر مورمانسک در قطب شمال در حرکت است تا خطر حملات پهپادی اوکراین را کاهش دهد.
🔴
این کشتی ۸۲ متری گریسفول توسط ناوشکن روسی سورومورسک و کشتی گشتی وووودا اسکورت می‌شود، در حالی که ناتو کاروان را زیر نظر دارد.
🔴
از این قایق تفریحی در حالی که تورهای ضد پهپاد عرشه آن را پوشانده‌اند، عکس گرفته شده و پس از ورود به دریای شمال، سیستم شناسایی خودکار آن خاموش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131759" target="_blank">📅 16:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131758">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نخست‌وزیر و وزیر امور خارجه قطر، محمد بن عبدالرحمن آل ثانی، با وزیر امور خارجه سوریه، اسعد الشیبانی، در دوحه دیدار کرد تا درباره همکاری‌های دوجانبه و آخرین تحولات در سوریه گفتگو کنند.
🔴
در این دیدار، آل ثانی مجدداً بر حمایت قطر از وحدت، حاکمیت و تلاش‌های بازسازی سوریه تأکید کرد و بر حمایت دوحه از آرمان‌های مردم سوریه برای ثبات، ایجاد دولت و بهبودی بلندمدت تاکید نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131758" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131757">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نشریه نظامی «میلیتاری واچ»: کارخانه هواپیماسازی روسیه تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط ایران را به پایان رسانده
🔴
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
🔴
احتمال دارد نخستین سوخو-۳۵ها از سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131757" target="_blank">📅 16:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131756">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01db34aaaf.mp4?token=X5o1RSSvnu80uYhliJ-0qt7qg6Ib1I399K2o2bNzdF8AXlH5-Z9HEjyNibk1-vl8weIUmDibfYfo90Mt79nAnEgXlGLWeuDGRnuP49FVu_oFJwhKswV4fBMrCEF43ZWR6H78ElxsAm_rH0b7x3LhEM1hdvtAFNlCLaYYGZihJ_absL4OehGHJl23YBHphMTTV2jwP83NdXSsyvhBD8ztPdlQjkjPQv6sqadH22RrKvjyb7AgmGj1_sRTKTkupfZiKj8ibanrQC8P0fVfuLiO2fmqWyXWo6aQAIZpS8NI-KfLa_78-S3CfNnnHGTz1cwlG9KLu24XBigIMBAQoWS7GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01db34aaaf.mp4?token=X5o1RSSvnu80uYhliJ-0qt7qg6Ib1I399K2o2bNzdF8AXlH5-Z9HEjyNibk1-vl8weIUmDibfYfo90Mt79nAnEgXlGLWeuDGRnuP49FVu_oFJwhKswV4fBMrCEF43ZWR6H78ElxsAm_rH0b7x3LhEM1hdvtAFNlCLaYYGZihJ_absL4OehGHJl23YBHphMTTV2jwP83NdXSsyvhBD8ztPdlQjkjPQv6sqadH22RrKvjyb7AgmGj1_sRTKTkupfZiKj8ibanrQC8P0fVfuLiO2fmqWyXWo6aQAIZpS8NI-KfLa_78-S3CfNnnHGTz1cwlG9KLu24XBigIMBAQoWS7GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای روسی مستقر در آفریقا، امروز صبح حملات هوایی را بر علیه مواضع گروه‌های FLA-JNIM در شهرهای آنفیس، گائو و سِوارِه انجام دادند.
🔴
همچنین، یک اردوگاه کوچ‌نشینان توارگ در منطقه زارحو، واقع در استان تیمبوکتو، مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131756" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131755">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpbd45n83Y6xXY5I9USlo6jqXfr5xNEp0HAPuoxk1HtIXfVy-pc3BiGTt4xL3W5icuw3bI-I9mi_MkbgiPZ2h-WcCGjiTjJfiWEGzq198oq_wHwb8Ti-ePdZDQNuPifxjBIVlkXPHXIsDy0AIMWw0-CPVUJUoSEWjH318WwS6OOUadBSFLlNkSCQ_pax28k-Jt5bggP8lDgYMN__bZQz88TeTNKFJmIXvqZ9eZ9w27EZ3hztS-PSMIkUwYBWlLnVajYZ1ew1WVlPKbZBA4X42uOpRASG9QVYrf87UpMKZRDHzA2Rx8MQnniLsouwHnDj26oyP6PqDeF3piw4yiOZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی در ایران به اعدام محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/131755" target="_blank">📅 16:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131754">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/فردا یکشنبه سراسر کشور تعطیل رسمی اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131754" target="_blank">📅 16:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131753">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdhyqBS7kkszvCITqSlegFY0DYlLMvONru0rvoKR79luviWeNibhGQID6dJA8uW5AIbaXxae6ENtv0Xj7WLazsmyroiO_Y6vlI8_qe2RnRQlppMN4L-AEvxfYSqkyrpAbVZPlIlp3Sli69rmcV3_XcIzZaVi68Zu3n1yt2ulEkS9lLVWuxJEa5zeCgDUB6aHqHcDm7lbC8tdgLejyquQ_NIi-ITpo6Se3Psci2-dm7WQbX1KuZRcEyhLfKhVjAev2uQvNOgtgS3UCK1y6glyi413d1Yf9Cuw9B3fvaSsQCqMbs6Kf1Wjes6OoRxV8JGexe2AFOUDRmsODpcPt8slHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار عظمایی به عنوان فرمانده نیروی دریایی سپاه معرفی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/131753" target="_blank">📅 16:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131752">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9286675b.mp4?token=gLDzVHhmCPZoQ2XfvVuwCyHbFqMG57SYD20juAOalZBT1okgMoSNiScUs97OO8orFTnp4UO1De3l-tdUBth8WSEyQY72x48kF0lL3eOUXEv_x26ZIJmskK6ucBpYbGanTIcYk_dpT4ynYLfsGYnyks0KLMxEyU_E5KeC5KuX2NxE5KaaPi_aYMvg6ypERLVVWZ9SdA5XQVSRZZB06oMThP2XhwnZGou_Zm2rlFYi5s6spAW8qu8bS4Q9U5eK7f8cFgF9FwfBwMyzlVlUzR43UkpaNCRtyXisg-5tSkrg0iz_9G_xzqcXSLWP5qr8Dt5iCkx-7Br3ge3xVI9HfEpbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9286675b.mp4?token=gLDzVHhmCPZoQ2XfvVuwCyHbFqMG57SYD20juAOalZBT1okgMoSNiScUs97OO8orFTnp4UO1De3l-tdUBth8WSEyQY72x48kF0lL3eOUXEv_x26ZIJmskK6ucBpYbGanTIcYk_dpT4ynYLfsGYnyks0KLMxEyU_E5KeC5KuX2NxE5KaaPi_aYMvg6ypERLVVWZ9SdA5XQVSRZZB06oMThP2XhwnZGou_Zm2rlFYi5s6spAW8qu8bS4Q9U5eK7f8cFgF9FwfBwMyzlVlUzR43UkpaNCRtyXisg-5tSkrg0iz_9G_xzqcXSLWP5qr8Dt5iCkx-7Br3ge3xVI9HfEpbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهرک‌نشینان اسرائیلی، دسترسی فلسطینی‌های محلی به زمین‌هایشان را در نزدیکی شهر سنجیل، در مرکز کرانه باختری اشغالی، با مسدود کردن یک جاده، مختل می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131752" target="_blank">📅 15:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131751">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
آگهی دبیرخانه شورای عالی مناطق آزاد تجاری: انجام هرگونه پیش‌فروش خودروهای وارداتی در مناطق آزاد ممنوع گردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131751" target="_blank">📅 15:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131750">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزیر خارجه مصر: از تسهیل مذاکرات ایران و آمریکا حمایت می‌کنیم
🔴
باید آتش‌بس در لبنان اجرا شود و اسرائیل به طور کامل عقب‌نشینی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131750" target="_blank">📅 15:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131747">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003c393383.mp4?token=vtPF5DwOuofdAtRxPZ6GmcuRF0MS60W6dFphdbReG6-uY-VNnHhm8Qx17aNj-PBC0pLpXYf3F1Wd3aDBRBGdxyzbr_Ll67q6MvYcq0WXlWCTloEIW2fFk3H4NboH7kdlObzYL7xZuQvu4kdUH10AeCyfl_0Fzbnd-h-rVYBJAZ1s3tnZxuNqAQI-fQxibDlZFOuDUD8SPGyx9jTV6MEwsPUtot2D8bWjaf1TPqozrQ5qo-MGAPWulzZZ6u8Nb58q8nE-Fhd_XknRchEYME3WOUD_t9s4WwIMwj8nPZ7Iy8RIj6n5CvovNBzTiNOZ5JoPRqmm2JJ0QjrUnvJy4oA2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003c393383.mp4?token=vtPF5DwOuofdAtRxPZ6GmcuRF0MS60W6dFphdbReG6-uY-VNnHhm8Qx17aNj-PBC0pLpXYf3F1Wd3aDBRBGdxyzbr_Ll67q6MvYcq0WXlWCTloEIW2fFk3H4NboH7kdlObzYL7xZuQvu4kdUH10AeCyfl_0Fzbnd-h-rVYBJAZ1s3tnZxuNqAQI-fQxibDlZFOuDUD8SPGyx9jTV6MEwsPUtot2D8bWjaf1TPqozrQ5qo-MGAPWulzZZ6u8Nb58q8nE-Fhd_XknRchEYME3WOUD_t9s4WwIMwj8nPZ7Iy8RIj6n5CvovNBzTiNOZ5JoPRqmm2JJ0QjrUnvJy4oA2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروه‌های بزرگ وابسته به سازمان FLA-JNIM وارد شهر آنفیس در شمال مالی شده‌اند.
🔴
تعداد زیادی از نیروهای ارتش مالی (FAMa) کشته یا اسیر شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131747" target="_blank">📅 15:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131746">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b402cee7.mp4?token=DVjPkj0_YBROg-1FiEEHAKmwL_GonsG9_h1TTffn3nhlCJrV0B8Jyrmrqbjl5yEoIuSXqL1qN3N3TYSudSmXerA0rlTG8JD8olAnantvyDSDZlntIG7mi6CkOCLcV7N8rA6NoABodyMN55iX_lYluVcDmwDCaX-XWyKeE4druwKZLQAVflMtkM_YPDAyJLwe0ea1SCl5MWwLD9eBMZJhqcgoysm2H7FPeZeix1jRUg_Bs8bMMFpA2SLTZqAgeTOEksKS3l3hiTTPLioR-S8QQFM1V_KagzaP76-MqK1xYXb4bbPYjA-rj_8x3YpSaGdqWydi8C1Rb6yJvCt9RxJJKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b402cee7.mp4?token=DVjPkj0_YBROg-1FiEEHAKmwL_GonsG9_h1TTffn3nhlCJrV0B8Jyrmrqbjl5yEoIuSXqL1qN3N3TYSudSmXerA0rlTG8JD8olAnantvyDSDZlntIG7mi6CkOCLcV7N8rA6NoABodyMN55iX_lYluVcDmwDCaX-XWyKeE4druwKZLQAVflMtkM_YPDAyJLwe0ea1SCl5MWwLD9eBMZJhqcgoysm2H7FPeZeix1jRUg_Bs8bMMFpA2SLTZqAgeTOEksKS3l3hiTTPLioR-S8QQFM1V_KagzaP76-MqK1xYXb4bbPYjA-rj_8x3YpSaGdqWydi8C1Rb6yJvCt9RxJJKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار نمایندگان جنبش امل لبنان  با سید عباس عراقچی وزیر امور خارجه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131746" target="_blank">📅 15:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131745">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی: پزشکیان به مجتبی خامنه‌ای اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
🔴
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی خامنه‌ای با یادداشت تفاهم موافقت کند.
🔴
دکتر پزشکیان، قبل از امضای توافق، به آیت‌الله سید مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/131745" target="_blank">📅 15:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131744">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
گزارش ها از پرواز گسترده و غیر عادی پهپاد های اسرائیلی بر فراز بیروت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131744" target="_blank">📅 15:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131743">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
تصویر بسیار منشوری و زننده دیگری را همسر سپهر حیدری در اونلی فنز منتشر کرده!!! که به شدت وایرال شده
◀️
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131743" target="_blank">📅 15:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131742">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSyowGP0DaIrGYxLi6IS4ZAIWI6r7Rrae-WV_T5u7rEyAY_LiwFddqqLiB46TIBdaXZApvUhbrHlOOttzEO83GpfLVo69TQzh55uQquY5O-HObLPRn5Ds7s_7Xb0TyKVKOTv8-0Jc5Hv-W0rZQjnOa5XxQ166J6YgtXJCIMaR2OG8uB4_JmSjVysQMOSUSP7FfNUFh8IpNc_aZ8Pc-2w8rO8jdA-APe6jG8id9LBx5lFaOgrkIx2zN5ptz_w4n5_7izd-VxAw6hruD08XyRzyN_Zq4i8smCS-0mvYlJnScrPHUIfrL3-MsSa0v9abZhq9Zm6NzwW3otwVLczkak8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خلاصه‌ای از کیفرخواست رضا پهلوی که توسط خبرگزاری تسنیم منتشر شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131742" target="_blank">📅 14:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131740">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رئیس‌جمهور عراق: عراق نه با ایران در برابر آمریکا متحد است، نه با آمریکا در برابر ایران
🔴
روابط خود را صرفاً بر اساس منافع ملی تعیین می‌کنیم
🔴
پرونده گروه‌های ضد انقلاب بر اساس توافق با تهران، حل‌ می‌شود
🔴
امنیت خلیج فارس، ما و منطقه به هم گره خورده
🔴
تلاش داریم تا بهترین روابط استراتژیک با عربستان برقرار شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131740" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131738">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d_Ct0ynsRcnZDeNPoz59KPFKOZLs_i-x786K7s1KCxXb-TufKScnnZRFog-oRjACgDCb8AEGvTZO1-HVTFd6JZiOQ5iic7n__uD8nWaFfPQaYbh-OvlYxDtKDXlNR3Y-jS9Sr00W2p6GvdZ_agzoibUI6g_glZj16Gzh6G-SoOjmN2dc5tzyq9StE8RKdSluAlkNkY9MV7M_vQuV_Wv0KqtRkt4Zm9lt2QiDLRd2YdhLR9GnKAldJmXqCzHMsZcPmNXC2qoCRbPOHsf9vP4B8aqDhSFXmqUoZrfPkQ3Ex0qCwcRIZfXeV0lw6qIrpnp-OiuXgPDEXX1O7o4gIFhc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UXbEXLCv2dxPusgLLL5up8sVmzB6yMoVIciakL8jIp_lJaFUqTtfwp8F3ZVYIm9Y96gTAk_8bSoqHVK7zJ61lzty6vakOVUc2jSv4Tz0zVz-g_7WUgpJk-53kJfqATxo9dSEU1PPFQqUeX7SRQsmiaCQHBeY1-MX5ARDGfcYAT6OzbC-UsVUJe2pEsLLdvIS0GyyHU8iKk8LxzCYXnYu_1I5ISG_vdaAaFzFzvRgAiAVkJ55nabWAZZU4OAPsi0DLz5FtVf8H08FVN7zNfqchfywLjQ26l4_nwD74mFHOnXCsAfve3KMQLWjIwu_CQ6A_bh76HfrU7wCaz5sYMCLuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا یک بالن نظارتی (الکترواپتیکی) یا مخابراتی در آسمان تهران مستقر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131738" target="_blank">📅 14:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131737">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
به گزارش اسکای‌نیوز، گروهی فراحزبی متشکل از ۷۱ نماینده و عضو مجلس اعیان بریتانیا از دولت این کشور خواسته‌اند بنیامین نتانیاهو و یاریو لوین را به اتهام نظارت بر سوءاستفاده و شکنجه سیستماتیک بازداشت‌شدگان فلسطینی تحریم کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131737" target="_blank">📅 14:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131736">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ : کمونیسم یعنی مرگ، استبداد و دنبال کردن شرارت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131736" target="_blank">📅 14:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131735">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
پیام پوتین به ترامپ: مطمئن هستم که روابط برابر بین مسکو و واشنگتن، به نفع کل جامعه جهانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131735" target="_blank">📅 14:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131734">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
به گزارش بلومبرگ، امانوئل مولین، عضو شورای حکام بانک مرکزی اروپا، اعلام کرد این بانک پس از افزایش نرخ بهره در ماه گذشته و انتشار داده‌هایی که از کاهش تورم همزمان با افت قیمت نفت حکایت دارد، در «وضعیت خوبی» قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131734" target="_blank">📅 14:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131733">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است؟
🔴
مقام‌های ترک و اسرائیلی سال‌هاست که علیه یکدیگر تهدید و توهین نثار می‌کنند. از زمان آغاز جنگ اسرائیل در غزه در سال ۲۰۲۳، این جنگ لفظی تلخ‌تر هم شده است. اما حالا به نظر می‌رسد اوضاع دارد از کنترل خارج می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131733" target="_blank">📅 14:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131732">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5_DeWNi1nYik9V297R8wJ9zWFyw85Km9gJyV276YpRk5IrWWFHy5rcQYTPPwAjgslgS_Ouxx-kf7Ct5_3hfoCgtM9umunnSZKtNo9NKs198MIq-AnTeIOxY1LebAXH5PrixSwEhGJyGBZZfEMLU-5MOFu6TBbtGGmaYuQSwkhUGOAdo7MqVFn-KxAkVuOcrJBMRNEf-q9U4ExR_5Ye9wNlqjZzmnOuneBukDz16gVf_PiOvLCFj-jHonpPis7as4s8ZA6ETgcNTKuEDEEYv19F1Qf8S-sJhUXZToix8186fptUKHBPpVNS0fHDfc1CzuZ5i4fDCfXEtA2-OxnhLkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار سی ان ان در مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/131732" target="_blank">📅 14:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131731">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m89zcPHBiw-UEmi0q3y5X3bZ4pZe06jTeOKnv_fJVTndwpQ0auRZlbaZg4E-ovgEVhyfMSZaF8EhyElsJVOn4hrUHExXqY6s6wUCl46aKX5Z_TjEJs5ue6fHdBaCd6gmF_k_AUyxnI4xWeZgrZrq_l2WIv70wPo7rxQTBJ1IABwKxEKCTXl3KfbAFc_e0ZQl8I98G8N_eocmUJsZcksVooExwEwOW-5-uZXZZVssJFJplgk7oNZIr_3wJ0KTkR2zAzYT62LI_GB0c1uK9jZS3Ah_IxBb7dqaCkNEZLqIyj4o5rLmmvhQPg3q4f2DNtW4azMCLgtd6my1gLK-AQthEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131731" target="_blank">📅 14:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131730">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر سقوط یک هواپیمای جنگی متعلق به ارتش روسیه به دلیل آتش زمین در شهر گائو در مالی منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131730" target="_blank">📅 14:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131729">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
به گزارش بلومبرگ، پاتریک پویان، مدیرعامل توتال‌انرژیز، اعلام کرد تولیدکنندگان نفت خاورمیانه به‌دنبال فروش نفت خام ذخیره‌شده در جریان درگیری‌های خلیج فارس هستند؛ با این حال نگرانی‌های حمل‌ونقل همچنان بر موجودی بنزین و گازوئیل فشار وارد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131729" target="_blank">📅 13:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131728">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
مهران رجبی : حسرتی که پس از دیدار با رهبر به دلم ماند این بود که نتوانستم پایش را ببوسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/131728" target="_blank">📅 13:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131727">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی : تاکنون هیچ حادثه‌ای در مراسم وداع گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131727" target="_blank">📅 13:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131726">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKxfyIFFweOqd4_2kOR4iB-DiRacTStObbx6_RJlJPkmeluyLOfo3D4wPVd2LyKDIVCvo1YVcSksQp1e28YYGGpI5F_K42DW9OogpmrLx3VbCsegTQejuBtDxN5mc1Eu6pKIt2WDEwqWjP0Xs7a-CFRWr8Nc5XMmbHaMeCWHCy-9Q4cElFhv_tuD9FFS79h1KN0HLA73Cx3_fNDrcQGe3OkHdydY_5NlMqEqlvLI4GCNTn9zXlTU9Yb4MhelFSQ533Wl8kl_08aUZDfKdQt-W3H-iq2pbYdHay2Oj7rVu_b0fHwT9Q4Lr18RMlihUlgLxLUXTzI55OZqTw8ELadJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز روز استقلال کشور ایالات متحده آمریکا هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131726" target="_blank">📅 13:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131725">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X53spOYrWcvT-hXyOHbqrrj0hYCg46jWg4kzSisaCwb9XSRITItUYISiuDRgnvmO5EVa91qhpvnixGQ45wLAP1HRevPPgWXuYect7vcgaIsp-B_gkNp2STUczZoQOZx9igGHUUEt3IPfBfyRicpI-GqXSiINIEkKW8EVv8btBRSBrXjXjEzU0nzLY4Rm9OeCnGqHMM9zl6QMWSGPJk4xa8JFqBSw0bwGFH9aMIzHeDbd3Pyob80ZEC6JByDEm2SpvAzSvLQlbFa2o8CfJDcg9QAtcQU4n2GUDw9aTJ_IYpmRgxwJPFpq3mnNGDU0AUcRf7I0VKWaY60YUxYb-D09LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب/برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131725" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131724">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
میشل عون در پیامی به ترامپ : از شما می‌خواهیم که همچنان در کنار آرمان‌های عادلانه لبنان و نهادهای آن بایستید تا بتوانیم فصل جدیدی از امید و صلح را آغاز کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/131724" target="_blank">📅 13:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131723">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ:هیچ کشوری به اندازه ایالات متحده آمریکا، خیر بیشتری برای این دنیا انجام نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131723" target="_blank">📅 12:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131722">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آلمان انتقاد ترامپ درباره صرف هزینه‌های نظامی کم در ناتو را رد کرد
🔴
فریدریش مرتس صدراعظم آلمان، انتقادات تند دونالد ترامپ رئیس‌جمهور آمریکا، در مورد کمک‌های ناچیز آلمان به ناتو را رد کرد.
🔴
وی پس از دیدار با سران کشورهای حوزه بالتیک در برلین گفت: آلمان در حال حاضر بودجه دفاعی خود را ظرف چهار سال دو برابر می‌کند. این بزرگترین تلاشی است که ما تاکنون برای تقویت قابلیت‌های دفاعی خود انجام داده‌ایم. بنابراین، چیزی برای پنهان کردن از کسی نداریم.
🔴
وی افزود که این موضوع را با کمال فروتنی در اجلاس آنکارا در روزهای ۷ و ۸ ژوئیه ابراز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131722" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131718">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwBkcSMna5liEHzgr9WEQEzDrshmo7gbX1jOPPsHMT1JU2hi-6xYj9ZhZ9GGQZK-9lZyPtACJC34H9ZqbcNny0FGEhsZ3VJYbRjJAzW3HuLXuS4oHfXF5Z9kF4enS63j9Cwfg0XvQecxrXW75FKEYXe9EHmRtUhOsMzzInfh6wFt92U1edkzvY3RCdOxxaRvlBCmDPcuRdaFyc31BddX2zldAWQmOln2R82d21KoYNH17d2gmAK2pagujB2W_V2Prru7eMlNgMF8L1052chd_bCTXnr63J0SNsKtDR0ftaK-YBoouB7YaYILXh2qtPmLV30q4St2go0ayG4SsSKBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atoXGr6uLVOpZhb8laFE-2q8HVdVhYlpduKNsUuFbBBTaouNHx_t-MUK8CUl9KR7MbJ80spXKhx6SN62HLUYt15Fp9EIKWIsv0M8W5qNo9DOYpqxRYz-faLjofysBm4nGk-VRFDsveEcZz1992-FC5y0cQqr_gT-M9tw0c49JLhb50Xiz8VH1V38EWLrmz3CB68UXcF23vKfpG-WwKn-zNR8G3CsDFZ5PfkbbhUOykFvdgbw2Rftwz1m9MEsZG-XMS5iOcf6UGloZ7estZHUW4jLg3DDom8DylGIVdnZYEMSleaxMsiFOwtc4Y5eOHHl0KNF472qSOYCHdAirEEkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKNRmP0t8OVvun3qCgjwCrvD-TjERSvm9e6YNhl2yUtNiaqcwiZ5jja-IGtUZEAp3Tw6I87AJzFSEAs1eoEMhwWs9Uqr8pLCjvzLmayl6udGPyWmuYGjaXR65uPoRcP_SToZJahfUE-EmqHJWgYEe7Od8WxyXodWFJilkuqJO8w4uIRJGT-_vt_ObGs_8iL2FVF_b4VqyizE81G6nGM8C70DGAJg5_tj3vIfSGca4Kt2QwCPJD1FTJxFNPU2vo1CuWRPpROW2DC54YD4PfMI9NSl-0J46v8EYpdOTvclTeFaFJ8Zokb3ClZBPV1a_ilKKjkLox91hxnCXcsb22FldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vx14sjFM1WKGp8WklFCPaO8o7hyLDhUucxzJfzEgEpN9wsXfDhkOcT5AlukvIY9gXWbqSKjpEBtnnSpDfdlrYIWmFmk5c0GYA4jUgAulKxfuaJcjcepBPTGpCNdmvJBcMAC441Okqk2DGQ_XpgNDZQPK0esCYqpRFXlbxxvB6AI36x178XzurcAI1AU2Bi1oCw7Z8LFLBzzmT6wFoSZUe4X17r7WH8gI5i6Hk8trR8xOgqku1G1G_Y4lW5QrvdsuZWQB-B0C8OTSSCkZp0DeD5TptrMG1fI1lx6F0sl3vodYR3jPCdN-YlCENJXIbVTHS1mqrR_hLInQ1q8wgzvjmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
به‌روزرسانی (تنگه هرمز): چندین کشتی به‌طور ناگهانی در حال تغییر مسیر از کریدور عمانیِ تحت کنترل آمریکا به کریدور تعیین‌شده از سوی ایران هستند، یا حتی دور زده و بازمی‌گردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131718" target="_blank">📅 12:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131717">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
منابع لبنانی از حملهٔ پهپادی اسرائیل به اطراف شهرک «صدیقین» در جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131717" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131716">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی: به سایت‌های هسته‌ای ایران باید دسترسی داشته باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131716" target="_blank">📅 12:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131715">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
زلنسکی: زیرساخت‌های نفتی روسیه در نزدیکی سن‌پترزبورگ را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131715" target="_blank">📅 12:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131714">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBTCkqxe4fNo3oh3E_ef9G_8bfEcb064zEhIiHVEqqEezSLRV2vk3_74um5YSV0xQsxgJMb9VsV6VJZzw3mPAsnmD_HZlAIejhoPIaKkZytXjkFV51qB0kHICShxx1FaVbbY5DIdEox9h46XS3XxKao2n6ULBZG9nBwg-O-PVcGkTSEsgQdGwJad2bDZ-fEyUILW_2Bbaux7ZNN_c6y5OtvRZI3eTma8DQ4ltLnS9MajBWAGbMTVyP_Arm0vIWZS4jChgtjsxjv5wxyk5EurLCOCSN7BxjiGi8k2i7KQIB8i-KjEJeOaf4cBAUZ1gEv7Jezc6MnuXvxl5K5KKsMC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌ پهپادی گسترده اوکراینی ها به یک پایانه نفتی در سن پترزبورگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131714" target="_blank">📅 12:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131713">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
تولید نفت اوپک با بازگشایی تنگه هرمز و ازسرگیری صادرات تولیدکنندگان خلیج فارس افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131713" target="_blank">📅 12:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131712">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNDbNNTizBbeib7TPwYfRmjeo3qzjLVYvM5MTYQj0j1BQI51Oqp4D_4EpXYkBtFVw6fMLy8Vl5X09Rr1Lo4f_jfrbTzaL25GmL0YJmLhOZH63BFSvnSJubfwHHYr5t36H52EHn8Xrm09xK--x0lvUpQscWkIJcLv4PLHgGYAheIFxaEcOloe2WwoCpxVI8051xaZ1Px3GnEFOAqoAx-BhgbC4MvJXh0_1YXfQjUFEvzj8Y8iclVqimyRZ0ILV5Mlfus_wDh9UZkC2u0o2bfRRskfrQxA89OVz0U2BIMGKo7DP77MYIcGzqw1-cQ8fnyXpAg-p0WUKDURMUpRq0lrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: به گفته سه نفر که از موضوع مطلع هستند، مجتبی خامنه‌ای در حمله‌ای که منجر به کشته شدن پدرش در آغاز جنگ شد، جراحات شدیدی متحمل شد، از جمله سوختگی در صورت و بدن و زخم‌هایی که نیاز به چندین عمل جراحی روی یکی از پاهایش داشته است.
🔴
انتظار نمی‌رود که او در مراسم تشییع جنازه پدرش شرکت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/131712" target="_blank">📅 11:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131711">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6duhHQEqyd3FoDIC8R63mc0aacteIK24LpKBE8qnKtyPYkkXtRfsTuITj0AB5Tc80F2NOpo9p07zj3cLkSsiawKeaRLj5FXgFYK69mqO88igQcdlMtOA9_8RbwgFhmnhRaNI_QWQkvX5Pg86SkIxQLjG2Vzdq0uweW1Enl41VsEg6B3gOZ091XB-R6sWKlnBBsIu8dY-2zWU-80rdoLhPdRuIjGcrDUBJ7JHLDgD11Ce5zLXo_7a1EYSvU2pvsUrBjh1XZiu96rUO_r6hVKs2Io-xecRgYOzAfKaqVLtXflgqOT5iF7BQ4FlKhzr-U1z9BQuqMTcMmwVKQuOIyYqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک
کاربر اسراییلی:همه کشورهایی که در طول جنگ توسط ایران مورد حمله قرار گرفتند، در مراسم شرکت کردند؟
🔴
چه آدم‌های بی‌اراده و بی عرضه ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131711" target="_blank">📅 11:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131710">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
محمدباقر قالیباف در دیدار با رئیس پارلمان عراق: درباره مدیریت تنگه هرمز موضوعات مهمی در تفاهم اخیر با آمریکا به امضا رسیده است و بر اساس قوانین بین‌المللی، اداره تنگه هرمز باید میان دو کشور ساحلی ایران و عمان انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131710" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131709">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
انفجارهای کنترل شده برای امحای مهمات عمل نکرده، امروز در جنوب اصفهان (ارتفاعات صفه و بهارستان) انجام میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131709" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131708">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOWQJxG9Tz91x42R-syV2-ubXLIOLaIfa33JZTroO6jhRRgzJGr5IlP8Jx1ywcsgu0FqaCbBUWKTyJ3IhJx9Z8ngB0396AOPDHMsHJRDDVVF8uBA97ed7swh8lX8PQLTQGqxPBAAdTRs0sTDQlCCFXXWS0NqxklLmnDCXtNucN3pYQAkk2-VJXyXmVFDR-PNmhKCpWvFUQ1cnmdtZPOvUNutWFzS_OI_fz9W6nA3hC--UOnPPKmiAodUSL3prnzARxMff1QOQP5gvcexjgeti4_TNJVVakmbzpX3qP3nwhTK5_4BpuPnB4cgOpsmtKsTQ-moXKxicjjhcOKq8ebEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده در رویترز از مراسم امروز در مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/131708" target="_blank">📅 11:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131707">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مدودف: تنگه هرمز اکنون برای ایران به سلاحی تبدیل شده است که از نظر اهمیت دست‌کمی از سلاح‌های هسته‌ای ندارد؛ اما یک «سلاح هسته‌ایِ» دیگر نیز وجود دارد و آن تنگه باب‌المندب است.
🔴
روسیه، ایران، چین و دیگر کشورها می‌توانند درباره ایجاد یک پلتفرم مشترک برای کشورهای تحت تحریم به‌منظور مقابله با محدودیت‌ها و تحریم‌ها گفت‌وگو و رایزنی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131707" target="_blank">📅 11:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131706">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ارتش اوکراین کنترل شهر کوستیانتینیفکا در شرق این کشور توسط روسیه را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/131706" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131705">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
تعطیلی سراسر استان تهران در روز سه‌شنبه اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/131705" target="_blank">📅 10:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131704">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
فرانس۲۴: عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند
🔴
از آنجا که‌ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد
🔴
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود
﻿﻿﻿﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/131704" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131703">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tdr08v6RAkTDNMxFVrsfSPSLwi4Xjxg3gmouJ_IBDZkz6Tl2-OCxTqfz0kTuL7ZV_xokaxiR5eSCgj1T3c2kJcwGoayOA0DCqJu7GpqkPSORFzPtblCA6WoXT963Q39GW1UCO4RcjhA_ImvBK0p7YYEFgI5Z5DSt-jJxrJBhchbnBSxRXWWGpxxP7SIEWAe7pUhnJtCoONMWlkhdzLdwD426d4fqgeHyuxZAnsndPKKWePDZ_FmmNZZiz5AbWvwEBzEFjk2zzKWwAeFxnRhLk8ETGv-yKd5G5LGpXvCUNsQHXqeNnhVPOxeZW7Zyr7AWyl_CmZjxOssYkVYuN-KiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت سنگین نیروی هوایی آمریکا در خلیج فارس
🔴
نیروی هوایی آمریکا در حال اسکورت کشتی‌ها در آب‌های عمان و جمع‌آوری اطلاعات درباره جنوب ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/131703" target="_blank">📅 10:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131702">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
🔴
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131702" target="_blank">📅 10:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131701">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1xtvxM2-jEhf0Z8rOtDoiOLpwIFAjpcbtc8TYbsiQ1_bS8KuyFsb6OljzmiIeUfnoB95yJIMWtPZVbfWu6nfNVRMqaQgwtNAu14jkl2MMlxvdx7_MkzsFP5pzU1lgYJtc1CCcjYVwoEQOQmZ0UUeDwrMYMlIIfg5Rr1ngRWZNhb3YAkc3WfcuXmwgrgLJifZS2oK5QetNwCK-KUv4jK55qe8mCm_Isp6xM6_m1FMRS9GWb9uPwDdR10tMRIL9YDf1uryc7MYWidCbQyGWvcL8lTpupmxvDQ8RRnUsqAdcLEbuoixYW6SFdgTCXcpv0JeyanFxFu8RfsV3C_4UDxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار غریب آبادی نسبت به هر حرکت نظامی در تنگه هرمز
🔴
معاون وزیر امور خارجه در واکنش به بیانیه مشترک فرانسه و انگلیس: تنگه هرمز میدان نمایش نظامی قدرت‌های فرامنطقه‌ای نیست. ایران به‌عنوان قدرت مسئول و ضامن امنیت تنگه، نسبت به هر حرکت نظامی در این آبراه حساس هشدار می‌دهد.
🔴
امنیت هرمز با دولت‌های ساحلی است؛ بحران‌سازان مسئول پیامدهای ماجراجویی خود خواهند بود؛ این هشدار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/131701" target="_blank">📅 09:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131700">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
گروسی: تاکنون نتوانسته‌ایم به تأسیسات هسته‌ای ایران دسترسی پیدا کنیم؛ این موضوع به مذاکرات جاری میان ایالات متحده و ایران بر سر تفاهم‌نامه گره خورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/131700" target="_blank">📅 09:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131699">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرنگار الجزیره تأکید کرد که تاکنون هیچ اظهارنظر رسمی از سوی واشنگتن منتشر نشده است، اما رسانه‌های آمریکایی به نقل از منابع آگاه از وجود «تفاهمی موقت» میان ایالات متحده و ایران برای کاهش تنش خبر می‌دهند؛ تفاهمی که امکان ازسرگیری روند مذاکرات را پس از پایان مراسم تشییع رهبر فقید ایران، فراهم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/131699" target="_blank">📅 09:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131698">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
مکرون، رئیس‌جمهور فرانسه: دو شناور مین‌روب را به خاورمیانه اعزام کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/131698" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131697">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiDPJOKcxgrMbGFyPsuBLTg3MV6XL40QlnyWi6lsKs4seW33WsegTQ13XD4YPhT2bwoEG_2ErkkUx4ougN3aL5cjaiI7fUe-sPG3GbYQmonKNzLZJgZc5ileAv2hVf98jMqdD3JWlm_32XvnyXg5-O9uDrbu9Bxy2ykk_fiEGDnYN2cdVG4sA7kc2VyXRMZDpNa-0UBlp8w8Hvk4xCQM3Og5OJ7DJ0ctKQFs_v36ojCH3JEBjikU6ISAziwqPfvqlinARhyFiuKKn17Y5IaDgxXwYq8JuD1Jyzt-Erw3_YoE60EriPSZDzRYqxlwnBMzvxw01_nziyTc1M_DZxQa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی از پهپاد انتحاری دوربرد «SKYWASP» رونمایی کرد
🔴
این پهپاد توسط شرکت SR2Vector توسعه یافته و برد عملیاتی آن حدود ۱,۵۰۰ کیلومتر (۹۳۲ مایل) اعلام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131697" target="_blank">📅 09:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131696">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فرانسه و بریتانیا آمادگی خود را برای استقرار یک نیروی چندملیتی به بهانه حمایت از آزادی دریانوردی در تنگه هرمز و تضمین عبور ایمن از تنگه هرمز که یک موضوع با اهمیت جهانی است، اعلام کردند.
🔴
فرانسه و بریتانیا هر دو همچنین بر تعهد خود به ثبات منطقه‌ای و احترام به حاکمیت همه ملت‌ها تأکید کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131696" target="_blank">📅 09:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131695">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OYM3bTQFvvHCDFbRtgu9qbahdHEme2mkHQzOKiQjJDq5w3ynmGZmm0ClmE5h_kqlTLRnHRzPS7vWQnUKVgfByOiq_s8t7_nu-P3fmCENODL3_SRFUQLy8_rd5tAnPe9DXtM65WRUkQc6AuX1KcMpBuI-5S3IZ2rgLFOiPYNdFZ_6gbF8Vu7qa3LbnYfSDMPJi9qSfdzmOBnsIhdw_wN9D1ZX1U9kDJrNbn3Zxtl9A3_QYWxAACpPu6DwwdY1Mnsgjma9y3c8TMiezDJaO8hMKTDR-nwZlsQko4NpVcHRyInqHx1tUUkinPVC10VjOiPeeabRvcU97DZUsoCouf4CzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی اسرائیل در نزدیکی تپه استراتژیک علی‌الطاهر، در جنوب شهر نابتيه، لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/131695" target="_blank">📅 08:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131694">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
متروی تهران از امروز ۲۴ ساعته شد
🔴
مدیرعامل متروی تهران: تا ساعت یک بامداد روز سه‌شنبه، ۱۶ تیر، خدمات مترو به‌صورت ۲۴ ساعته و رایگان ارائه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/131694" target="_blank">📅 08:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131693">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
منابع محلی از حملات توپخانه‌ای اسرائیل به منطقه «ارنون» در جنوب لبنان خبر دادند. گزارش‌ها حاکی است اسرائیل این منطقه را هدف حملات سنگین قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131693" target="_blank">📅 08:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131692">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeebf5f487.mp4?token=WxGWSNu59roqllzi2MayEaugRl-WItualp_1qB7JMM83hgyoGMfIRM7qn0RoP2JEBisa6o2X0NTKHEZK4luPhuGxA4grYQ1qHP99Vvsl2pph169eoQnOEGouTSv0wdddKOZT5k9sT0c3rSgoZGQQGVA1QoHpns_0ldO9vb6wu4E5PatadEunPxB06is_hQqZgdmYP-8wxQ9jPS7JfhvNz4Nbe9icBOGcUnHwqv3eEkQOt9paYPsDWKciw2istcTl0G0MiSyG0J45AmcrRhsYhnGfhLkkW9eBIvZ9YgXPa6YwZlBo-PD-jL-4gK-EFZ6xIyRF6YZkEqUXWg8mmfAL0bvhDjbbhDXsiVK37KwFLvOn1CxtFpFmjUsBCoEj-yEJhZ0Wzfa84ztqAOg_AeW9-gMWv0pJ8mbRGjPV9B0l4RetQ0OTmVk8tfTBgoDDlZ83Yc5tbf6arq-w4F2T0dp27KYzmQgIzKD56yBxwxHYHHdu81GFh6NLRcM1EpQ5TWvBUjLH-2yQX0sKO7wecHt7PqIQQtk_8kGU5GHxIABPYb9JejGwa7Tg7Nawe56ZHKJu34bMYVwdhz7oDY3nZHx7KwTJ7W-tUcmogFcW-GEfCw6Xgho-iOqBWUksttMX5R79zwc6CBIkKZUKhFv8UxGCLzlKv1ZQVTrmzVsp9pfSZBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeebf5f487.mp4?token=WxGWSNu59roqllzi2MayEaugRl-WItualp_1qB7JMM83hgyoGMfIRM7qn0RoP2JEBisa6o2X0NTKHEZK4luPhuGxA4grYQ1qHP99Vvsl2pph169eoQnOEGouTSv0wdddKOZT5k9sT0c3rSgoZGQQGVA1QoHpns_0ldO9vb6wu4E5PatadEunPxB06is_hQqZgdmYP-8wxQ9jPS7JfhvNz4Nbe9icBOGcUnHwqv3eEkQOt9paYPsDWKciw2istcTl0G0MiSyG0J45AmcrRhsYhnGfhLkkW9eBIvZ9YgXPa6YwZlBo-PD-jL-4gK-EFZ6xIyRF6YZkEqUXWg8mmfAL0bvhDjbbhDXsiVK37KwFLvOn1CxtFpFmjUsBCoEj-yEJhZ0Wzfa84ztqAOg_AeW9-gMWv0pJ8mbRGjPV9B0l4RetQ0OTmVk8tfTBgoDDlZ83Yc5tbf6arq-w4F2T0dp27KYzmQgIzKD56yBxwxHYHHdu81GFh6NLRcM1EpQ5TWvBUjLH-2yQX0sKO7wecHt7PqIQQtk_8kGU5GHxIABPYb9JejGwa7Tg7Nawe56ZHKJu34bMYVwdhz7oDY3nZHx7KwTJ7W-tUcmogFcW-GEfCw6Xgho-iOqBWUksttMX5R79zwc6CBIkKZUKhFv8UxGCLzlKv1ZQVTrmzVsp9pfSZBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: در آمریکا، ما به زبان انگلیسی صحبت می‌کنیم، زیرا این زبان، زبان بنیان‌گذاران ماست. و برای هزاران سال، این زبان، زبان آزادی بوده است
🔴
یک آمریکایی همیشه خواهان صلح و آرامش است، اما ما هرگز از خطر یا تهدید فرار نخواهیم کرد. ما همیشه خواهیم جنگید، جنگیدیم و خواهیم جنگید، و همیشه پیروز خواهیم شد، پیروز شدیم و خواهیم شد. ما باید این کار را انجام دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131692" target="_blank">📅 08:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131691">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ: شما می‌توانید به کارل مارکس وفادار باشید، یا به آمریکا.
🔴
شما می‌توانید یک کمونیست باشید، یا یک وطن‌پرست. اما نمی‌توانید هر دو باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131691" target="_blank">📅 08:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131690">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd5cf7670.mp4?token=ZLkoPK3Vtoc2VRxd5UaFoGz4KFpniJ3uHh94tbZBoXP5dGZTE7aPFQBhaNJKI_kNdMmB5E5WNltIhtcCX97uRZg2mIQbqYIPoIJ2kZLCVTn-Ly06r5AhEuiuIfX21w3R4heN4zK-nAFA8hPRGNNDqIvJiO1_zsFwRKaItepMDym0KzJSp2wydczXEfh8HlQks6inSZ1Ya3cUxcU13eFGGE3b-7gwrSWbmyTpoovrBEj3viuSZmroIkJowqHA9XoeXyxK_tMee-WSpkMfDAktla4X0BpEBBAS-HoTDBtBqh1NEcJsxXmX7PuV794JWXJ_kSokC4azM_EECIjPpFCyVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd5cf7670.mp4?token=ZLkoPK3Vtoc2VRxd5UaFoGz4KFpniJ3uHh94tbZBoXP5dGZTE7aPFQBhaNJKI_kNdMmB5E5WNltIhtcCX97uRZg2mIQbqYIPoIJ2kZLCVTn-Ly06r5AhEuiuIfX21w3R4heN4zK-nAFA8hPRGNNDqIvJiO1_zsFwRKaItepMDym0KzJSp2wydczXEfh8HlQks6inSZ1Ya3cUxcU13eFGGE3b-7gwrSWbmyTpoovrBEj3viuSZmroIkJowqHA9XoeXyxK_tMee-WSpkMfDAktla4X0BpEBBAS-HoTDBtBqh1NEcJsxXmX7PuV794JWXJ_kSokC4azM_EECIjPpFCyVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
🔴
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/131690" target="_blank">📅 08:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131689">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ifkprv9hcy-4eIm22s--u5ygtXZaa2C9aL_4RDSXtziO2gdotsku5qB00GpabH0A0NUxR3HrFOZPW6ABm_LRI9Qoyx5Z-oZETUDYXhGVFttvUTZqBz-YrgJ77FXMGoIO7qKSr3L7oil82rvRpLJkksAFU_Z0h5RIsSIQEyPZMBx-aEqfCx9Hj9u_Fhik6icJPitUTNmfpgj2hbVs9l49LCocdLfdfN-FpJckl-UyQL9KDf5v0FmLHRAXFZuCheWpDpi3fZe_nfLkL4bRwEj4sluZST-EeKLKz3R3q6SiEZbcJ7iKUp6ZVlAAJNpEWRiYPiAleQhaU3LMDbp0cU2Vjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بزرگترین سایت کاریابی روسیه، برای دفاع از آسمان مسکو از دست پهپادای اوکراینی به دنبال استخدام داوطلبان اپراتور پهپاده!
🔴
وظایف این شغل شامل آماده‌سازی قبل از پرواز، شناسایی و جمع‌آوری داده‌ها در روز و شب است؛ تنها مهارت‌های فنی اولیه رو هم داشته باشید کافیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/131689" target="_blank">📅 08:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M80RU6ZtwUN4bP_9om-uGfI_j4FQvicHwmsGsO1Ck15EHVUu_hHCNMNLimjrp32XXRujJ4dsPQRUi-inuE7AsCO1PWwtPfa3KGYzo5XLu95FJoC0OJiqe1SLFBZYxR0n52wbP-xdpW2mU-Jocp0thkjD3ISyOPyBDyBEZHVrEUkKhC0oonoaYHkNsl2-8g_Tg04Zi9_t-JkicQM0xPrM3Yku4sdQ_ypHkxOrf0nrvB3xeRLafz3XzNCLTg20TNDMUdSAYL9Y3LOyQV6Qj8CIS4Ouc2kpk23qGMGDmPqMaT-W9yQ2RcbPDgIya4U7hZDGj8Uj2kaxhK69SveVpaAOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqysU6XF7zXcQB6r67-K_O0UwoNm3HQsXoVtYDQudp7YTwyqtOm-OYtmxrioVMuzUVofi3oG_DC9sHEJVs1csiwwOmvDbgwfCSMEZbSNe4iOYFhHHD_O9-EttSvUc1PvmNh8znjufVY53S2Ly5d0jlA_wkX9oYdJSmMI7tuuCAwUy4OudUHQ8dKDdIEERAl1DM_LbUNknu7yYHj5E8YJ3z2evhkc7XDUz5QwKtXF-Alol6SWtKdvCO83OEnJVKM33Txi8JA-9NJm46HK-ise5VRzp36SsjCH4hfmmWrTwpPIxIwsx4mOLf08VRwsMxNfKE7G2qeCl0q6to14eitcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xg7EJaBtCsT7MNicl4tPZbi5E58Ov7s0NCcR-MksPEJDK2cAZxsYyScln5dZmSpCS0kSv8fG1voQwMVnu5QjHmsFr9PhdPLLyQwWCjbDTne0Inmt3w29mzkcKUaLLRQpzu9VaCxVAoSZwoQw91p8bwAShBGAIisWT5cz6zuufEkQeFH_GmIHg3Bhg_Umw3FVdQGUDAv-2j1kT9PybBr7jWfNmz3q8Xfh4ELmVRyoR5Wk4qEq2zoBHSiMGb9KQUemg4iDkR_kj_CSQ9onabttZ1vwY--DdWKt0qkpwLVbCmsExJWdyd8YeCx-tGufCMTSILxpEyWMM7iodr0Kpo7HIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/131686" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131685">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=tm_nJuJgmQX64RpplxJsA-BVba3kMQvs_5urJToGqX9ZOJAax1GgCzaQxkSpW9Lg7stMxST9bWGEzBaWbJrShuSbr7bWmiu568KJCeaYc3KmgBEFLJPq1EzhWUK374MrZPiun14kO2CjXBZYxxa713QOSWkG7NOesch7Zi_QrW9zILd8mD_8ic_Xg4t0oioYd_DwDlCSgKLkcHCBatyS47_3BOU-BKVBuIty0xSVfy8wQjfEgv5cvM94b4EluwgUCIRBDU8xajV0m_4Cwnwu9D_1Rcnj_A9XoyXkoFmmtRd3ZCm-dQtuPxeHrTigGkkQ0cgtszEDl22_9pEcX3_D0xh-bYpnN5lUHSw_wXDTdVsAMNSYd2iwi2XGG5tvQYXNtcYJDl598bNOKJCB9kMO11oyoAsZ2DPMF3Uho7rucoCk5M8p3eWZXNnAJVOAhOUi6UdSy7CB93rZmt0lFI8UkGj67GUKKvDoOIY22WrhEt9QOGnnjV1c5WJrYUY0Xm13KN-xLFTMLxC5M8hcv0cXgxeI-IdFlUIBas4qXN3O0gxoKJ9A2gNyphuInAWMdGc4pZuK17t917yco4tbLn6A293VTFLnEzcYmbnFK259mn93beGRCkEriImwuoLqrJJcP9sUnU2Rr5UZCCAjO8gk5bheOBAV8U5o11mJccJA4e8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=tm_nJuJgmQX64RpplxJsA-BVba3kMQvs_5urJToGqX9ZOJAax1GgCzaQxkSpW9Lg7stMxST9bWGEzBaWbJrShuSbr7bWmiu568KJCeaYc3KmgBEFLJPq1EzhWUK374MrZPiun14kO2CjXBZYxxa713QOSWkG7NOesch7Zi_QrW9zILd8mD_8ic_Xg4t0oioYd_DwDlCSgKLkcHCBatyS47_3BOU-BKVBuIty0xSVfy8wQjfEgv5cvM94b4EluwgUCIRBDU8xajV0m_4Cwnwu9D_1Rcnj_A9XoyXkoFmmtRd3ZCm-dQtuPxeHrTigGkkQ0cgtszEDl22_9pEcX3_D0xh-bYpnN5lUHSw_wXDTdVsAMNSYd2iwi2XGG5tvQYXNtcYJDl598bNOKJCB9kMO11oyoAsZ2DPMF3Uho7rucoCk5M8p3eWZXNnAJVOAhOUi6UdSy7CB93rZmt0lFI8UkGj67GUKKvDoOIY22WrhEt9QOGnnjV1c5WJrYUY0Xm13KN-xLFTMLxC5M8hcv0cXgxeI-IdFlUIBas4qXN3O0gxoKJ9A2gNyphuInAWMdGc4pZuK17t917yco4tbLn6A293VTFLnEzcYmbnFK259mn93beGRCkEriImwuoLqrJJcP9sUnU2Rr5UZCCAjO8gk5bheOBAV8U5o11mJccJA4e8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس :ساعت ۶ صبح بیاید مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/alonews/131685" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131684">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/667106b64a.mp4?token=a3QrgkqNfcRe6uhbDqUPzuk-PT2CPTekYIelZp6FQoc0dKHwlSB5HuoRYGhIBsnD1YEiZc1Bxf8ZYUXaudxr579Lez8f2SHQFmzSOGl9lINtcCaRvGunwAZC3C2MEk8X9deBlftuhMg2y8KRaY-exC4t4QAUn0DEwGsLDDOXMD-fFVGm6nSKRt_DGA9CafJGpA5jHn1AQC-HW13UoiKQAo50SIuhDSlEz3OIdVnAsp-c4Qzb5DorgW-51LOlVKQVWubmvWN-iGYKd2hkjtjRD5LSfCmJHddWDMffHTrGqd8XYC9wV42RpWC8uyk1GmCATnLto4s-Yh9M0CKKmOAw2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/667106b64a.mp4?token=a3QrgkqNfcRe6uhbDqUPzuk-PT2CPTekYIelZp6FQoc0dKHwlSB5HuoRYGhIBsnD1YEiZc1Bxf8ZYUXaudxr579Lez8f2SHQFmzSOGl9lINtcCaRvGunwAZC3C2MEk8X9deBlftuhMg2y8KRaY-exC4t4QAUn0DEwGsLDDOXMD-fFVGm6nSKRt_DGA9CafJGpA5jHn1AQC-HW13UoiKQAo50SIuhDSlEz3OIdVnAsp-c4Qzb5DorgW-51LOlVKQVWubmvWN-iGYKd2hkjtjRD5LSfCmJHddWDMffHTrGqd8XYC9wV42RpWC8uyk1GmCATnLto4s-Yh9M0CKKmOAw2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موزیک ویدیو کامل آهنگ جدید توماج صالحی به اسم «تو چی؟» که تا تونسته به رضا پهلوی دیس داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/alonews/131684" target="_blank">📅 01:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131683">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
توماج صالحی یه موزیک ویدیو به اسم  «تو چی» داده و رضا پهلوی رو دیس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/131683" target="_blank">📅 00:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131682">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aawiGpMPvU1Ez7kEJLUV6OfNzoGGOQWdsdJ7tm_snxFnv8jiNdUU7SGXpEO-cQ1bzogyVI0aTFu_Blj4IEkBfyb1ibuF1aCzCZC4B_6gepVYTFPxJ0CfNN4VQ2RvO8Z-y3JQ5F8x7iP9NKzo8DAU0bAqc8YbeoYsLfng87GfEuY_L9FOKrpha7Tpa4hZUZQuAz6C2dugiXXK4xcG5w7M89xVHhybBkPwScsXmEWBzQUSvKyaqrZ2_jE5hovqHAvlghS9vo_NYZwv3yTAR9DIJFMazJmW0D0p6xgh1o04tO8OJOHHCDPAHDhfTpYf4tIuT2nRfuKbAA62dUMuaefSLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/131682" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d68bfd54e.mp4?token=n77mndA6w56hTNzaBvV_UANdcLN-y3DQzXK8av-y2SsYIJUnvLl5B1Fs5xnN02bmB_Lk4mwC1qhj7UNYEJw9gpBpBdjjltpNLCqFYVFU2GdnefC1XeDuzwSrX1atLL2I1v6BsA2YJg_rvUan55IYHV695y0xqY27y_hBIUsx4R7se_l-_l8KVdzXQ-VN2Ok0XNMKTVvKSThBlmF1e0N6WU-CQUkxk0eIAWwUZ0mZ1c3VOC-oZFitO7sO-BNzcn3L2ZdDjzRSsbdu4qc5SKYFjo8CqOMHPsyuTcpg2IY9UXV6eyS5-Mi8at93B8EcJxm8xnmyuFsQixUkZbVdBREu-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d68bfd54e.mp4?token=n77mndA6w56hTNzaBvV_UANdcLN-y3DQzXK8av-y2SsYIJUnvLl5B1Fs5xnN02bmB_Lk4mwC1qhj7UNYEJw9gpBpBdjjltpNLCqFYVFU2GdnefC1XeDuzwSrX1atLL2I1v6BsA2YJg_rvUan55IYHV695y0xqY27y_hBIUsx4R7se_l-_l8KVdzXQ-VN2Ok0XNMKTVvKSThBlmF1e0N6WU-CQUkxk0eIAWwUZ0mZ1c3VOC-oZFitO7sO-BNzcn3L2ZdDjzRSsbdu4qc5SKYFjo8CqOMHPsyuTcpg2IY9UXV6eyS5-Mi8at93B8EcJxm8xnmyuFsQixUkZbVdBREu-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توماج صالحی یه موزیک ویدیو به اسم
«تو چی» داده و رضا پهلوی رو دیس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/131681" target="_blank">📅 00:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت
🔴
پ.ن : تاثیر گذار بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/131680" target="_blank">📅 23:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131679">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQl5vHgqCKMclEoSvm3y8cV6oiUR_6PXRIQPcMg2gXoG9gK4GsOQiVWLafHVg4yaYsZrmo6QIy17DUm_dFEM3Y5ZGk-HWroTWbHh_3uqgbGQze7MT9VwbMbhxedZzPGf5onA1d6x32ZPNed8sAAG_4aldcxipMRwoASR6sPH1MWd0MyCZRmlK_yP9lJ3vfioOGz-8ytj2Jpb_glK9CG-C6fd61r0hqULeFT8HduZ5bf5m5ERPNfu0-5BnY2zcRvrlWV2DGMK_QC0jZ8fCVFQtJk65OQsRxiS028rrwdlPXFJ-mq0uonTRsr1qq1QMFixiQYDJSGK92dhu43cL98rYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر پاکستان بعد از ایران به ترکیه رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/131679" target="_blank">📅 23:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131678">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/131678" target="_blank">📅 23:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131677">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/131677" target="_blank">📅 23:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131676">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F34OnpIFxC8uDP6NgxkGsmXNuu_sgKjBi8a6WnuJNLR9bh-BZ2zZjuXA1yt_JF2IIzY1dOCKg4HdREc9jDGldUinVXk4y3t4XtE4i7BLoWGrQDlnhcn5Sp2hmCChFQD6hoApwZ3JQYrtNoZpZP7iSo5HWaNXMZhcWgHFgx62IP6pmwtVOce9qLafEsdax9QBps0TaPF-8WHy_0frNS66uYN9fDkCZhZGiqjsmqUn0ov5tPmARVnHUNp1q2a5XCZTD0UUwpzng2n56cgpNf925xbF86kthsLMQutTQCgUwZ-rQVZIGvInSe3wH9h16E9v98Vb91gmmSiXDfz979N2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل به فارسی: ابراهیم ذوالفقاری چون تو مراسم تشییع رهبر شرکت نکرد،پس صد در صد مطمئن شدیم هوش مصنوعیه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/131676" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131675">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRQeEZSsU_a6ECUuB8PxVOuZ6-pN2prFK8STP92HI-BLjJTZX6gBBC0KAgY3mpqFQ4DLPL8hEcvb0iRPagj0zH6FyY54E4lBPb-tRseeIV6RtotNzuYIHyPBhtDXPbryMGZl9WDUDE4LHQQn9W4MclmrSDXpkZ-2bB9nmveyxtNrsPtOynZsTbcJw43ustm3qTKda6Db2mhUFw_yFUAWhzIXNLbGKw7snOoN-L_cs42TB5efUVXJLCKKjYQloNY1TxNHt-VIekHLIemCKgaiIh0GkmmrOcuxRSLj7F-8nv3uomuCEhCfdw5Alv34OJhmKSNpk0gaum4knGY6-rrWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصویر بسیار منشوری و زننده دیگری را همسر سپهر حیدری در اونلی فنز منتشر کرده!!! که به شدت وایرال شده
◀️
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/131675" target="_blank">📅 23:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131674">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff6ec588e.mov?token=Ju0TT-EjMeJ-7OQR9odTjRtQd1ZY8mWUXG3SA2jDhZMySGdmOty-oJTjEkB-DoLrqCRm8wrjGACK-oO_5LxOEQdYCforZpdmBtIdttlT-cPbQp-Rer0nPQMMRoAiyFX5grZEm8auyvhzRbmosRBhFMHz7Dbtwravji2o9S00x-ZglSyPipufeLbKGZ8ATVBNSPjsq7QVoD3m6_VoE_6Ttbp3L5zH41R-YS13kkyt5w-UP1M0_sVQHmckfsSrqQgxg_sb1THyb92_HHfCoaNbtHxVnUhDRRdTBBqWUMbxOcDmEWpDAhE7vuvN_6831goHNq7VjX_6s69Fv66aIWARRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff6ec588e.mov?token=Ju0TT-EjMeJ-7OQR9odTjRtQd1ZY8mWUXG3SA2jDhZMySGdmOty-oJTjEkB-DoLrqCRm8wrjGACK-oO_5LxOEQdYCforZpdmBtIdttlT-cPbQp-Rer0nPQMMRoAiyFX5grZEm8auyvhzRbmosRBhFMHz7Dbtwravji2o9S00x-ZglSyPipufeLbKGZ8ATVBNSPjsq7QVoD3m6_VoE_6Ttbp3L5zH41R-YS13kkyt5w-UP1M0_sVQHmckfsSrqQgxg_sb1THyb92_HHfCoaNbtHxVnUhDRRdTBBqWUMbxOcDmEWpDAhE7vuvN_6831goHNq7VjX_6s69Fv66aIWARRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین یبار دیگه با لباس نظامی ظاهر شد و گفت که نیروهای روسیه ابتکار عمل استراتژیک رو تو خطوط مقدم جنگ در دست دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/131674" target="_blank">📅 23:29 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
