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
<img src="https://cdn4.telesco.pe/file/a3yVBkYbm5hjl6vmeaj3FFFFk0E1Ox-NW_yz64TWsIPeXGqarjwHJ9BOXb4oILhhqg2n0hAp44RVjcjB0-iB5eYEyInN1xe9za-rLg9oWCKbgyLb6dWtfFvXdAOW_YhtNH4yHf99dgjV3dphGn44z12mu1KuB76ZXZnAwggRLR93SuVV0bHTZD2b_111F3G1_FPSZ_aoG5CGW0Qsv_EK8C-FTwDNNEUhNkOLt6llo1OFC_qlG43q6dtsUyUXhdlpJgeMTuZHmPEY0yC_I2-hIg0eeQUdlIm6VuTFvZX9C7EHNMs-Zfef9OJdYcocmU-8wgAh1xEAksN_6FfksEsO9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.4K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 11:20:30</div>
<hr>

<div class="tg-post" id="msg-3129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهاستینگ افزونه نویس</strong></div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/iaghapour/3129" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌ تبلیغ‌شده زیر، قوانین را بخوانید
👇🏻</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/iaghapour/3128" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc27095fa8.mp4?token=kDjXF2DGsCck4RatFbf2iAnWWkV2-0hbTsNoCFnEnUp0uAaGQWxo0Q-VWN9tJAnpH0Hh14YycmZWURp1z6E3P9wLuQXAqC_21aD6QF11NUI2P3Uj9BPDJLE7eGlgGY4albereauWWQFieDAnEiC1NJOsC3k7wshfM0U5qNyvmmIqj_K3zP9za2wj3KnVBycn2nCmMvK6zVbKqLWmrYDoIDummnG2-OlIE8SkJbEr8_Ryr27sCxDZIglw2uws4A1ru-0_RI67fJcZUENkZaCHQmfe2qIIpBAtcDCvLLkjmuBM0jN8QDYp45yx8mOZGNldt4VlAvn0zCsFKCIOAOfVsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc27095fa8.mp4?token=kDjXF2DGsCck4RatFbf2iAnWWkV2-0hbTsNoCFnEnUp0uAaGQWxo0Q-VWN9tJAnpH0Hh14YycmZWURp1z6E3P9wLuQXAqC_21aD6QF11NUI2P3Uj9BPDJLE7eGlgGY4albereauWWQFieDAnEiC1NJOsC3k7wshfM0U5qNyvmmIqj_K3zP9za2wj3KnVBycn2nCmMvK6zVbKqLWmrYDoIDummnG2-OlIE8SkJbEr8_Ryr27sCxDZIglw2uws4A1ru-0_RI67fJcZUENkZaCHQmfe2qIIpBAtcDCvLLkjmuBM0jN8QDYp45yx8mOZGNldt4VlAvn0zCsFKCIOAOfVsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده‌های عزیز قرعه‌کشی اکانت هوش مصنوعی (دوره پانزدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده‌های  اکانت هوش مصنوعی مشخص شدن:
👤
برنده عزیز با آیدی یوتیوب mohammadparsa-g2t
👤
برنده عزیز با آیدی یوتیوب nadervafaeifar1935
مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/iaghapour/3127" target="_blank">📅 20:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb5uGS-Ku9P8KCHQF7oUB9MDsrAmpUS3QvwluS3XqHsJI9leLxDGP5rhCotzkaQlaE7PQHwZDrBt8F26aA_OgVpkTcO4tXqE86oLYAetMK8ueRmOtVu2y4MlolLsSAnfKRw72NrtbzrHuKE8QO3BwXId5PW-CSBDyBAzJKchJH7PBSUj0oRTd4vJP98iwRk4AuIDay0FvC2jTqZvI17Kj4B7o_GAEUGiIn1f2Euj1rUPTeclOdPHOkWLnhs-8_Wb5neqhGS4D0PqC1JolXNAOrlYp3qx07nci5pJ99F2yZO4O6BhlnWhQrJpwqPLmUw29cwMXsg_bv8GVHKd7KDfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی ابزار iMonitor؛ پنل جامع مانیتورینگ سرورها
پروژه متن‌باز iMonitor یک جعبه‌ابزار همه‌کاره تحت وب برای لینوکس است که علاوه بر مانیتورینگ دقیق سرویس‌ها، امکانات کاملی برای ساخت تانل و مدیریت شبکه در اختیارتان می‌گذارد.
🔹
مانیتورینگ جامع و وضعیت عمومی:
بررسی مداوم آپتایم سرویس‌ها (HTTP, TCP, DNS و V2Ray) همراه با ساخت صفحه وضعیت برای نمایش به کاربران و ارسال هشدار قطعی در تلگرام.
🔹
ساخت آسان تانل
: اتصال سریع دو سرور لینوکسی (مثل سرور ایران و خارج) با پروتکل‌های مختلف (WireGuard, GRE, IPIP, SSH) تنها از طریق یک ویزارد سه‌مرحله‌ای.
🔸
تست سرعت و عیب‌یابی داخلی:
امکان بنچمارک و تست دقیق سرعت آپلود و دانلود بین دو سرور تانل‌شده، بدون نیاز به نصب نرم‌افزارهای جانبی.
🔸
ابزارهای پیشرفته شبکه:
دارای امکانات کاربردی مثل انتقال پورت (Port Forwarding)، محدودسازی سرعت ترافیک، کنترل اتصالات TCP و بکاپ‌گیری خودکار.
🔗
لینک پروژه در گیت‌هاب
🔻
این برنامه اوپن‌سورس و کاملاً رایگان است، اما کدهای آن توسط ما بررسی امنیتی نشده؛ قبل از اجرا روی سرور اصلی، سورس و مستندات آن را بررسی کنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/iaghapour/3126" target="_blank">📅 18:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJOT49YOpTrtrUsdHpRUR8CxjdF2oflbjTMm7ihliqXxGIu-qXlrykriEegfJ2SEage7YPFlNghyGa8QQ16i7ZsVRzUKcxUH9-9p6bNp4DssRLMgtLDhpZTVdsC7upc9ZZ6r2KZkp5D5Pkvy-GWB_AKTf6S5RNU56n6cJBMswm7dijMSV1MwTYsQRcs3oYqMgheVQbQmg_xLeln5X_zuWd8rt4bQsdL55Y0nfUoldYoKcW8r28e-1NRXhCqgXCOJ6uOTHPMKo2DB1H57zeLmED-v3nl8WscIqTCXyf1AtEKkC9Lol0nWbaBjK0Upkp7vT1YrqYJSWxMfxKqPq2UW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
پایان کل‌کل با هوش مصنوعی برای خلاصه نوشتن!
اگر کلافه شدی از اینکه مدام به چت‌بات‌ها التماس کنی یا بگی «خیلی کوتاه بگو و پرحرفی نکن»، نیازی به نوشتن جملات طولانی نیست؛ فقط آخر پرامپت خودت عبارت
TLDR
را بنویس.
🔹
مفهوم اصطلاح:
واژه TLDR مخفف
Too Long; Didn't Read
است؛ کلیدواژه‌ای استاندارد در دیتای هوش مصنوعی که مستقیماً مدل را به ارائه کوتاه‌ترین و فشرده‌ترین چکیده ممکن سوئیچ می‌کند.
🔸
فرمت‌های حرفه‌ای‌تر برای خروجی تمیزتر:
• خلاصه نهایی دقیقاً در دو جمله:
TLDR: 2 sentences
• چکیده در ۳ بالت‌پوینت تفکیک‌شده:
TLDR in 3 bullet points
• تنظیم ساختار برای یک پست کوتاه تلگرامی:
TLDR for Telegram post
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/iaghapour/3125" target="_blank">📅 16:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from👇👇👇</strong></div>
<div class="tg-text">📱
تا داشتن
شماره مجازی تلگرام
کشور دلخواهت، کمتر از یک دقیقه فاصله داری!
⚡️
🌎
از هر کشوری، حتی
ایران
🇮🇷
💵
کمترین قیمت
💎
بالاترین کیفیت
✅
اکانت‌ها به‌صورت
آماده ساخته شده
هستن
❌
پس احتمال
دیلیت و فریز
تقریباً صفره!
🚀
سریع، مطمئن و باکیفیت
👆
برای سفارش وارد ربات بشید:
⏺
@yoozseenfabot</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/iaghapour/3124" target="_blank">📅 21:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌های تبلیغ‌شده، قوانین زیر را بخوانید
👇🏻</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/iaghapour/3123" target="_blank">📅 21:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63c53b317c.mp4?token=akofKqRwTwI3vBlEeuKwfVGV7bEteOFJRzfnm9GkM_VlqVkcIzcKHxuxKFEiDaPUYgAmhQHzcVDCaJUusW1imyCATAJUzE32STsJQ5YiyyTYzXUKbPWnkZoX6f00rtpR8uLWhixg1P6l-mO2MlcNElRgQ8n2SGWmhbUgwNvWrC4-epGMqjfejBnJ83bObIdaBmMN3JXSvboDMUGxXTGAqH1tmGqz0K3z0EhtWfHH_PD9dqt6q5BLmYQmaNj248VpwmaV2RS6PWSEuSuQM466hf9vJNAJd33tOvOlyZO8PII2AV3gtaEYhfeM6ktpwkPm0d6wR_49Y4ysjwk9OLJMDaJE13duO4tLtUGdK7wSTKf-pdkEQgFMf7uT0dSbdsFH8vKH0s9NMU0Zj5LZev5kuOfngYxAugeYjIaYq0lfE-l8qFijDIc18cOvlN31Qg8qjIb9k7ULnY1LagW_uKG2Pi32z0NNWEDQ_hImOnEig_QRzMf520uWkWVqUENYWSj4p8trpRtyEMCOF67cryXlC1QWywePOW0Sh0hC-uyQrDjkb_dJx5RuVRvNure-ElT-8Nr0XAt7jCRxRdAepepMh0A40cU_eLilN7OSn9NcYnHhNDzSEwmLC6oM_zes4Jip8pqsaYXGHsoB8OxuCRIOTSmAlu-_gq7sOpO0bZ-b9-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63c53b317c.mp4?token=akofKqRwTwI3vBlEeuKwfVGV7bEteOFJRzfnm9GkM_VlqVkcIzcKHxuxKFEiDaPUYgAmhQHzcVDCaJUusW1imyCATAJUzE32STsJQ5YiyyTYzXUKbPWnkZoX6f00rtpR8uLWhixg1P6l-mO2MlcNElRgQ8n2SGWmhbUgwNvWrC4-epGMqjfejBnJ83bObIdaBmMN3JXSvboDMUGxXTGAqH1tmGqz0K3z0EhtWfHH_PD9dqt6q5BLmYQmaNj248VpwmaV2RS6PWSEuSuQM466hf9vJNAJd33tOvOlyZO8PII2AV3gtaEYhfeM6ktpwkPm0d6wR_49Y4ysjwk9OLJMDaJE13duO4tLtUGdK7wSTKf-pdkEQgFMf7uT0dSbdsFH8vKH0s9NMU0Zj5LZev5kuOfngYxAugeYjIaYq0lfE-l8qFijDIc18cOvlN31Qg8qjIb9k7ULnY1LagW_uKG2Pi32z0NNWEDQ_hImOnEig_QRzMf520uWkWVqUENYWSj4p8trpRtyEMCOF67cryXlC1QWywePOW0Sh0hC-uyQrDjkb_dJx5RuVRvNure-ElT-8Nr0XAt7jCRxRdAepepMh0A40cU_eLilN7OSn9NcYnHhNDzSEwmLC6oM_zes4Jip8pqsaYXGHsoB8OxuCRIOTSmAlu-_gq7sOpO0bZ-b9-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📸
اسنپ‌شات (Snapshot) سرور در دوپراکس
🔸
اسنپ‌شات در دوپراکس چه فرقی با بکاپ‌های معمولی داره؟ اسنپ‌شات در واقع یک تصویر و کپی کامل و لحظه‌ای از کل سیستم‌عامل، فایل‌ها و کانفیگ‌های سرور شما می‌گیره تا بتونید از اون برای ساخت یک
سرور کاملاً جدید
استفاده کنید!
📝
کاربردهای اسنپ‌شات برای ما:
🔸
کلون کردن سرور (کپی‌برداری):
فرض کنید روی یک سرور، پنل و تمام تنظیمات تانل رو با دقت انجام دادید. با گرفتن اسنپ‌شات، می‌تونید در چند ثانیه چندین سرور جدید (VM) دقیقاً با همون تنظیمات و بدون نیاز به نصب مجدد بسازید.
🔹
نجات در شرایط بحرانی:
اگه سرور اصلی شما به هر دلیلی کلاً از کار افتاد یا آی‌پی اون مسدود شد، جای نگرانی نیست؛ با اسنپ‌شاتی که از قبل گرفتید، همون سرور رو روی یک ماشین مجازی جدید بالا میارید و فقط آی‌پی جدید رو جایگزین می‌کنید.
🔸
تست امن:
می‌تونید از سرور فعال خودتون اسنپ‌شات بگیرید، اون رو روی یک سرور جدید ریستور کنید و تغییرات یا آپدیت‌های جدید (مثل نصب نسخه‌های جدید پنل‌ها) رو اول اونجا تست کنید تا سرور اصلی مختل نشه.
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/iaghapour/3122" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3121">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVpElWll9A7zmTgp6Uye60EeRRICrk54VkWnCwrlNOPRLKvs6no4GolAC7WMihmfqj7AoSy20erYQNFyw7BWGY1zgJNtb6H7ROF1wmTxtAc96p1ZDH5phP32J6-md564bvTPt6k-B_NgGLSnrY4mYVoq4wicCmiBIhCnuSaSGVvFd8lC9dua20kNBf2o7fuPETghQcgmazjhuP-_XBn-aOWNjAFB-hRCCW66QklUjGKm4dYzKU8ql8GOI6rzyvly2WhAWdUT0Uscw4MmOATDWVYv0IU88_kNTmOeaXAgXkHvEpCPsOxK8Z-oV1b-PFHbftjSI9GXuZZyKEK5cJ9jqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⛔️
بانک مرکزی دسترسی ۵ صرافی رمزارزی به تسویه ریالی را محدود کرد
با دستور بانک مرکزی، دسترسی ۵ پلتفرم رمزارزی داخلی به خدمات برداشت غیرحضوری بانکی به مدت
۳ روز
محدود شد؛ تصمیمی که تسویه و واریز ریالی به حساب کاربران را با تأخیر روبه‌رو می‌کند.
🔹
صرافی‌های درگیر:
پلتفرم‌های بزرگی از جمله نوبیتکس و بیت‌پین این موضوع را تأیید کرده‌اند.
🔹
وضعیت دارایی‌های کریپتویی:
موجودی رمزارزها، معاملات داخلی بازار و امکان برداشت رمزارزی (انتقال به ولت شخصی)
هیچ مشکلی ندارد
و این محدودیت صرفاً مسیر تسویه بانکی ریال را هدف قرار داده است.
🔸
مدت و شرایط بازگشت:
محدودیت ۳ روزه است، اما با توجه به حجم درخواست‌های انباشته‌شده، تسویه کامل مبالغ ریالی پس از این دوره نیز ممکن است زمان‌بر باشد.
🔹
علت اختلافات:
طبق گزارش‌ها، بخشی از فشارها به اختلاف‌نظر پیرامون نحوه دسترسی نهادها به داده‌های کاربران، حریم خصوصی و ساعات فعالیت بازار بازمی‌گردد.
اگر قصد نقد کردن دارایی را دارید، در نظر داشته باشید که چرخه تسویه بانکی ریال فعلاً با کندی و تأخیر مواجه است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/iaghapour/3121" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3116">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌های تبلیغ‌شده حتماً بخوانید
!
از شما تقاضا داریم برای درک بهتر محدوده مسئولیت ما و حفظ امنیت مالی خودتان، پیش از هرگونه تصمیم‌گیری یا خرید، حتماً این 2 پست را مطالعه بفرمایید:
🔹
قوانین و محدوده مسئولیت ما در قبال تبلیغات
🔸
قوانین خرید از سرورهای تبلیغ‌شده
هدف ما همیشه حفظ شفافیت با شماست. همان‌طور که پیش‌تر هم بارها تاکید کردیم.
ممنون از همراهی شما
🌹</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/iaghapour/3116" target="_blank">📅 16:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3115">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJZMoUPE9J_NhZaYZeNi0Gu2jL-GXVdhu7ciOeNk6V5nPrwSQKIsZ_UMhbb2p95HNg4O2Cn-d7rC4qx6rvN7j2-iA9nx4oWL6aYTzu-Q6Fh-PzBHZh-ifsaZ-kuMY4ODOoePI30eZCB6Q2a1eMPsmm0WOLWSjhAsqOWUUrK5gxm2YHw1DmxmxZkUvD1g3rWPjJK8wf0c_ax51zOSC_zWUDI23cTbL_etjPxWLFDJ1gXcJOs3fyEs4LJA2AMbKTEj2JI-SVfe2CWVgV2JEI1qeFu3GcUzffXbLESVDNvCDq8m6g7M5WI3d8yopYBjsu3tFh5NinKG8xU1cW0llEy-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
معاون وزیر ارتباطات: احتمال قطع اینترنت در صورت بروز جنگ یا ناآرامی وجود دارد
وحید یزدانیان، معاون توسعه شبکه ملی اطلاعات، در گفت‌وگو با سیتنا درباره احتمال تکرار قطعی اینترنت در شرایط بحرانی توضیحاتی ارائه داد.
⚙️
محورهای مهم اظهارات:
🔹
احتمال بالای محدودیت در بحران‌ها:
به گفته وی، در صورت بروز هرگونه شرایط جنگی یا ناآرامی، اعمال محدودیت روی شبکه‌ها و احتمال قطعی اینترنت بسیار بالا خواهد بود؛ هرچند هنوز سطح و ابعاد این محدودیت‌ها مشخص نیست.
🔹
نقش مستقیم رئیس‌جمهور:
طبق تأکید شخص رئیس‌جمهور، هرگونه دستور قطعی اینترنت باید منحصراً از طرف او صادر شود و در صورت اتخاذ چنین تصمیماتی، نقش مستقیم دولت و رئیس‌جمهور در اجرای آن نسبت به گذشته پررنگ‌تر خواهد بود.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3115" target="_blank">📅 14:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKDg5Da8KNzw9oQdkNHF0j8P-TEe86QxUZE_j-6C3pQmo1DofZGc3d_RAk7gMofq9nDncJOexLa5CyVpQ3f6k5ZpbF4l5b7m69L40PelXNmtK94pPLCaOYkT1yik8JkkiaJHDaX1gEw0tcfJK3GnFhQsr79UDhANT3zNT0lBlqV2MVxWuDXja4On2_yzMEyxdS0LwP55Z-gDnVtZY2jcp9_C5V8U3d009fO47WzKuvAAm6dJtpNgHs0NASLG-ZD5HdBL_RqBlJY0jSZYpDVHWhsVz-MdYfPKM_I6rMV9aFTOTjhUKnVwVBKaf_ScMkjElBN2q8jYfPXtHYNQoqJj4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔐
مهاجرت به SSL داخلی؛ ۱۶ بانک گواهی امنیت بومی گرفتند، ۱۰ بانک در انتظار
در پی لغو گواهی‌های امنیتی بین‌المللی بانک‌های ایرانی توسط صادرکنندگان خارجی (CAها) و اختلال در دسترسی کاربران، پروژه اجباری دریافت گواهی SSL بومی در شبکه بانکی کلید خورد.
🔹
بانک‌های تکمیل‌شده:
۱۶ بانک از جمله بانک مرکزی، ملی، ملت، صادرات، پاسارگاد، تجارت، مسکن، پارسیان و رفاه هر پنج مرحله دریافت گواهی SSL بومی را تکمیل کردند.
🔹
جامانده‌ها:
۱۰ بانک در حال طی مراحل هستند؛ درحالی‌که بانک سپه، بانک مشترک ایران و ونزوئلا و مؤسسه ملل هنوز اقدامی نکرده‌اند.
🔸
چالش جدی کاربران iOS و وب‌اپلیکیشن‌ها (PWA):
اپلیکیشن‌های اندرویدی با تعبیه زنجیره گواهی (Certificate Pinning/Bundling) مشکلی نخواهند داشت؛ اما از آنجا که ریشه گواهی‌های بومی در مرورگرها و سیستم‌عامل‌های جهانی (مانند iOS) تایید نشده است، کاربران آیفون هنگام استفاده از وب‌اپلیکیشن‌های بانکی با خطای امنیتی SSL و عدم باز شدن صفحه مواجه می‌شوند مگر اینکه پروفایل ریشه گواهی را دستی نصب کنند./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3113" target="_blank">📅 20:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCbKmWl0vNH1pw1Pqyg04GGIOcENjI9-o_y0z_I-zdRJcVyVUG6UYShLdkJ_qgM_PPRVamlE-tuERhxRsnED_sH5OYHub3susIaZKUcoCgYtTFkxY49K0YBtVpkEhDYFQ0qu6-ySsr32Q0Ix_u_lLXkbOT-GFLQATY9Cott5LHsIV0qBjjxo4QFVR_wvdwvLUTMWv8fhohtvt7g2n-us-939Ao8k6bSUNfPx5y2dJ2e-vWT0fQmAgm6Sabob53ZS_TqNLXp_FFv_H92TLTwWD7lv2EvcWK9Is6Dsvltge_CI4NHP1sOYSd4Okq5KlBddvg5vT34IG5QmZL83m-nyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار امنیتی فوری: تلگرام دسکتاپ ویندوز را سریعاً آپدیت کنید!
پژوهشگران امنیت سایبری یک آسیب‌پذیری بحرانی با شناسه
CVE-2026-107181
(سطح خطر ۸.۱) روی نسخه ویندوز تلگرام دسکتاپ کشف کرده‌اند که امکان سرقت سشن و دسترسی کامل به حساب را تنها با کلیک روی یک لینک فراهم می‌کرد.
🔹
تزریق دستور در ارتباط بین پروسه‌ها (IPC):
عدم اعتبارسنجی کاراکتر سمیکولن (
;
) در ارسال لینک‌ها بین پروسه‌های تلگرام، به هکر اجازه تزریق دستورهای سیستمی را می‌داد.
🔸
سوءاستفاده از پروتکل متروکه
interpret:
:
این باگ در ترکیب با دانلود خودکار مدیا در گروه‌ها، فایل‌های حیاتی پوشه
tdata
(شامل سشن‌های فعال و کلیدهای ورود) را بدون تایید یا متوجه شدن کاربر به کانال مهاجم ارسال می‌کرد؛ به‌ویژه برای حساب‌هایی که Passcode لوکال نداشتند.
🔹
رفع کامل نقص در آپدیت جدید:
این روزنه امنیتی در نسخه
7.2.9
با حذف پروتکل آسیب‌پذیر و ایمن‌سازی دیتای سوکت محلی رفع شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3112" target="_blank">📅 16:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3110">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmAv6Lfv11Fx8uo0E4zspPGbalLeM4FKYoNCQPg4rHo6z0tCJ6truhOmp2Vol-8X9MlPxz2WCzRxO_UQz5z0it_xP3Fv5S0vEZhHai29hcz-kR9P0pQ3DE6RKkxVtUENT2PrwhHr1nGQGy-jXmF2Gk4AcSCrP37eDI7yuut0kyCoN9Wmx4tE8uBZIpa8gwk2f0asQoWsKl1gdqHP0gZPdFnlD4AKayOKXrV-LHlDNTK_p8i1bC8zWstBTTW27gk2U-xQjiBbrRYswlLsWrPaeaiR2yvSBBdHHfxHMhSK_Hjt0vlmw8f0smsI_VOOgeGP8X3S7zEdcSn7aqe8-xqhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تداوم جنگ بی‌پایان دنوو و هکرها؛ کرک‌های مبتنی بر هایپروایزر از کار افتادند!
قفل ضد دستکاری
دنوو (Denuvo)
در جدیدترین نسخه خود سازوکار امنیتی تازه‌ای را پیاده‌سازی کرده که روش‌های دور زدن پیشین، به‌ویژه کرک‌های متکی بر هایپروایزر (Hypervisor-based) را با اختلال اساسی مواجه کرده است.
🔹
مسدودسازی شیوه‌های بای‌پس سخت‌افزاری:
در بازی جدید Star Wars: Galactic Racer، دنوو وابستگی مستقیمی به برخی قابلیت‌های پردازنده تعریف کرده؛ به‌طوری‌که خاموش کردن یا دستکاری این تنظیمات بلافاصله اجرای بازی را متوقف می‌کند.
🔹
از کار افتادن راه‌حل‌های قبلی:
متدهای متداول پیشین برای خنثی‌سازی لایه‌های حفاظتی روی این نسخه به‌طور کامل بی‌اثر شده‌اند.
🔹
ردیابی هکرها:
توسعه‌دهندگان دنوو علاوه بر سفت‌وسخت کردن لایه‌های فنی، اقدامات جدیدی را برای شناسایی و ردیابی تیم‌های فعال در حوزه کرک (از جمله گروه‌هایی مانند voices38) کلید زده‌اند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3110" target="_blank">📅 20:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3109">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taWMRb-7gga2ViXf612UoPOI8hT6kNsOgJNs6hwujNidbHkkk127S7wQ3aZJAJtNinvYC0nAdz_iepTKf1thmZChbA_WZIIlTaBPlT5f6eP7Qac41wzBY01gmLPZdvd4fH5wa44bAQpyCyyUjGVkQifVMOlBOB-pCyshzPGmUFXgaoVqZFG3hzLl3EqXPUAPQ5PySsNeB7tXlw-WqEbfTpcrPKi4W2KmonnIpU1HXX3rc_u-M_92pgBK6B9ZiWYpwojAEozXgk53hCG0IH9KQZ0zrhfK0ZlQ5KeI_FPRUSiX10N_li9C8poYn479KlYlamESMHq2A3p5UDHOJ22ERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سامانه «حسام» فعال شد؛ مشاهده و بستن غیرحضوری حساب‌های بانکی مازاد!
بانک مرکزی سامانه
«حسام»
را برای مدیریت یکپارچه حساب‌های بانکی بدون نیاز به مراجعه به شعب فعال کرد:
🔹
مشاهده تمام حساب‌ها:
امکان دیدن فهرست کامل تمامی حساب‌های بانکی و مؤسسات اعتباری فعال به نام شخص در یک پنل واحد.
🔸
بستن آنلاین حساب‌های اضافی:
ثبت درخواست الکترونیکی برای بستن حساب‌های قدیمی، مازاد یا فراموش‌شده.
🔹
انتقال خودکار مانده‌حساب:
پس از طی مراحل قانونی، موجودی حساب بسته شده مستقیماً به «حساب پایه» انتخابی کاربر واریز می‌شود.
🌐
آدرس سامانه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/3109" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3107">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiKl_EKVpG81S5C8jc_A82dNuFOZQ1mASeVqY4e3qzR3QtX7X0w45QLB3lyeDGVzeIUnM90eSoeG065d-kqPJVLb7y8iGXhsiqF54xAEvFgt2EgnRao3KNfqaGvo76FxVOQzXdWWhKEBKzII7e1tRefgtSBO2GCmHa3sCWjXCCgtxvOUKzxqJUeIvi3Pqj_Y3UvPGPAsmpbwcipy3ITMRXWQoi9FDRvZLi-OPdX7WGHI5xxUjYhnQfCx8GGscQPsL5MQg3HUGeKoXiVnPhcAMOwMxw4i2ihdz7aUlesvMjKti6C3d6xF0m52rKA-zgcvdELvBOCmQS1RhE2wQx77og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت آسان کانفیگ‌های VPN میکروتیک در مرورگر
پروژه متن‌باز
MikroTik VPN Generator
یک ابزار تحت وب و بدون نیاز به نصب است که اسکریپت‌های آماده کانفیگ روترهای میکروتیک (RouterOS) را برای پروتکل‌های پرکاربرد تولید می‌کند.
🔹
پشتیبانی از ۴ پروتکل اصلی:
پروتکل
WireGuard:
تولید اسکریپت سرور (
.rsc
) به‌همراه فایل کلاینت (
.conf
) و بارکد QR با تولید کلید امن در مرورگر (Curve25519).
پروتکل
OpenVPN:
خروجی اسکریپت سرور به‌همراه پروفایل آماده کلاینت (
.ovpn
).
پروتکل
SSTP و L2TP/IPsec:
ساخت اسکریپت سرور برای اتصال آسان از طریق کلاینت‌های بومی ویندوز، مک و موبایل بدون نصب برنامه جانبی.
🔹
امنیت و ذخیره‌سازی محلی:
پردازش تمام مقادیر درون کلاینت و ذخیره فرم‌ها در
localStorage
مرورگر بدون ارسال اطلاعات به سرور ثالث.
🌐
اجرای مستقیم ابزار
💻
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3107" target="_blank">📅 19:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3106">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB9qpAhvflxvN96jZMCbvMFmYI5Kdmzc2AVha9A0M5UtS-WDEBaR_G0kn8JBWE4N16c_51RWOOpwODM-I6uAa7yigdC4HC60Ywp3heM2qpesMYCPeUAeg5DoNP4jNLmTvkRKYK3qYVlFYSrUpjE6yk_ha2leXbXV3vnMAEogc3yVTjUQZ-KSI4fopS6vRM6gk_6K0GT-QIScIPkibGVYziWGUUrhknnU4plw02i7IvHBAlDLzL7JIliQYIpnQUN-j-6Bn684AY8m6lN4Cmu5VUlEPYvcqOQa2_1K_TLwJyyvKxtz-ttAWaL_4f205iAyv4wBisKzgWO1OUcNx42C5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گوگل ابزار تشخیص محتوای هوش مصنوعی SynthID Detector را عمومی کرد
گوگل پلتفرم وب
SynthID Detector
را که پیش‌تر در انحصار رسانه‌ها بود، به‌صورت جهانی در دسترس عموم کاربران قرار داد تا امکان شناسایی رسانه‌های تولیدشده با هوش مصنوعی فراهم شود.
⚙️
جزئیات و نحوه عملکرد این ابزار:
🔹
نحوه کارکرد:
این سرویس با بررسی واترمارک‌های دیجیتالی نامرئی جاسازی‌شده در فایل‌های تصویری، ویدیویی و صوتی، اصالت و منشأ تولید آن‌ها را ارزیابی می‌کند.
🔹
پشتیبانی گسترده از توسعه‌دهندگان:
علاوه بر محصولات خود گوگل، توانایی شناسایی واترمارک ابزارهای هوش مصنوعی شرکت‌های OpenAI، انویدیا و Kakao را دارد و اپل نیز به‌زودی از آن پشتیبانی خواهد کرد.
🔹
محدودیت تشخیصی:
این وب‌سایت یک دیتکتور همه‌منظوره نیست و صرفاً فایل‌هایی را ردیابی می‌کند که حاوی استاندارد SynthID باشند؛ همچنین تفاوتی میان محتوای صددرصد تولیدی و محتوای ویرایش‌شده قائل نمی‌شود.
این قابلیت تشخیصی پیش‌تر درون موتور جستجوی گوگل، جمینای و مرورگر کروم نیز تعبیه شده است.
🔗
آدرس سایت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3106" target="_blank">📅 16:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3104">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe7423d72.mp4?token=qtp-e9g76-N451YCzsCVN7eE3OjjsjKq8D3jc9bRb5h8CXXAVLHiXPyvRTyqPZwIkN6XiWwYJbsAAj8ORfEEXVufK_fy6OYGHdf3h5xggPaIYKa1S2a76FO-MTsGbMOJ4SJk2OR0b5q-74glRSEaHiSV4FFSu9b9_fTa3pfDndhwkw1wNSFFsJGEdaCle153UKfnddqkTmR55pgTgaykr220b-uuIiZk0WhSg9miQXxaCNHM2UBUI7-hbiTCuW90i301c6NaIvF9O1zLzAyZ3BAXZ1ppvhVQpSAjxu4AbRBTfs7LMpWWN9b_-d1m_cxAL-TNL28A3Q3BPeexvrG5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe7423d72.mp4?token=qtp-e9g76-N451YCzsCVN7eE3OjjsjKq8D3jc9bRb5h8CXXAVLHiXPyvRTyqPZwIkN6XiWwYJbsAAj8ORfEEXVufK_fy6OYGHdf3h5xggPaIYKa1S2a76FO-MTsGbMOJ4SJk2OR0b5q-74glRSEaHiSV4FFSu9b9_fTa3pfDndhwkw1wNSFFsJGEdaCle153UKfnddqkTmR55pgTgaykr220b-uuIiZk0WhSg9miQXxaCNHM2UBUI7-hbiTCuW90i301c6NaIvF9O1zLzAyZ3BAXZ1ppvhVQpSAjxu4AbRBTfs7LMpWWN9b_-d1m_cxAL-TNL28A3Q3BPeexvrG5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی (دوره چهاردهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده  اکانت هوش مصنوعی مشخص شد:
👤
برنده عزیز با آیدی یوتیوب samansh2915، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3104" target="_blank">📅 20:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3103">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9681d3a3.mp4?token=miuhA3NrVeYMoDXH2OI4jiyMq5aUSfOPdNwRBcJtMCiaqn_I86B1fsP5IJpXjdQ1wsI_07XSrVW-5oxpYAUGwCz4S-NR6f8MFeQYyncLHddvYN3bpYvjFjILXReiSHyrjAx1tk9bAyLVR5764HoW_4vqLj2IlNgONyHbQie1DNSw0t_DIuKwX38SyuCETQk5k1OKUyGKAFgjstUqXAfkOHn-guU4gaGp87sDsHn3OMeLUzslJSYf_z3gPU-8oW_XPKSt9w603VRxWoJPeyaq0cDWjUd8elTLpHzVS5_vnsTN8L7a3YMJRhd_fPE0VCxDh3-K-Xf6uifEPq4NJJpLmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9681d3a3.mp4?token=miuhA3NrVeYMoDXH2OI4jiyMq5aUSfOPdNwRBcJtMCiaqn_I86B1fsP5IJpXjdQ1wsI_07XSrVW-5oxpYAUGwCz4S-NR6f8MFeQYyncLHddvYN3bpYvjFjILXReiSHyrjAx1tk9bAyLVR5764HoW_4vqLj2IlNgONyHbQie1DNSw0t_DIuKwX38SyuCETQk5k1OKUyGKAFgjstUqXAfkOHn-guU4gaGp87sDsHn3OMeLUzslJSYf_z3gPU-8oW_XPKSt9w603VRxWoJPeyaq0cDWjUd8elTLpHzVS5_vnsTN8L7a3YMJRhd_fPE0VCxDh3-K-Xf6uifEPq4NJJpLmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوگل از Playground رونمایی کرد؛ ساخت بازی‌ها فقط با متن و پرامپت!
گوگل پلتفرم جدیدی به نام
Playground
(زیرمجموعه Google Labs) را معرفی کرد که به کاربران اجازه می‌دهد بدون نیاز به دانش برنامه‌نویسی و صرفاً با نوشتن پرامپت‌های متنی، بازی بسازند.
🔹
طراحی با پرامپت متنی:
تعیین قوانین بازی، فیزیک، کاراکترها و محیط بازی (دوبعدی یا سه‌بعدی / تک‌نفره یا چندنفره) با چت مستقیم با هوش مصنوعی.
🔹
موتور هوش مصنوعی تلفیقی:
قدرت‌گرفته از ترکیب مدل‌های جمینای، نانو بنانا و لیریا (Lyria) در قالب یک فریم‌ورک اختصاصی بازی‌سازی.
🔹
اجرای آسان تحت مرورگر:
بدون نیاز به نصب نرم‌افزار؛ بازی‌های خلق‌شده مستقیماً در مرورگر لپ‌تاپ و گوشی اجرا می‌شوند.
🔻
این سرویس به‌صورت رایگان عرضه شده و مشترکان Google One سهمیه مصرف توکن بالاتری دریافت می‌کنند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3103" target="_blank">📅 19:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlaCt69SSrxCkkA4DaL0H00WKRX9OgM4w1P2EgC0uQVbA4-ala80xgsZ-GOHwh-R7LyfPUWnyV5d4Iru1XlB3kyC7O4bdrT7B0oqsXfO3w2Dv5ZFyW7f1kZtGT8c9TEvuvD0IbrAwQ45HOUovjOi5C1iy2rzVzQyDJvqcybI40VB_5ua1_NsGKA2CWwI-0bl-YDH2ZHUZJcvYS1doeCnTFvcR3poATkSmYLg7ti4_45u3HxKhj44PtvyFhXW6vF3Qs-Le1y-NoS3e6YRE5N9FbQeels7-vwNPmTISs7R9K3TvdLWaJ7k3yk_C9X7mn_AvTcwhE5EDKffuNBnK5Livg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
وب‌اپلیکیشن کاربردی ارتقای کانفیگ‌ها با ECH، فرگمنت و چینینگ
پروژه متن‌باز
Proxy Builder
یک ابزار تحت‌وب کلاینت‌ساید است که به شما اجازه می‌دهد کانفیگ‌های تکی یا سابسکریپشن‌های VLESS و Trojan را مستقیماً درون مرورگر به ECH و فرگمنت مجهز کنید یا آن‌ها را زنجیره‌ای (Chain) نمایید.
🔹
ارتقای کانفیگ با ECH:
افزودن خودکار پارامترهای
ech
و اثر انگشت TLS (
fp
) به کانفیگ‌های تکی یا کل لینک ساب با پریست‌های آماده (کلادفلر و AliDNS) جهت عبور از مسدودسازی SNI.
🔸
تزریق فرگمنت و سایفرسوئیت (Fragment + Fingerprint):
اعمال پارامترهای
cs
و
fm
با نسخه‌های بهینه‌سازی‌شده پریست V1 و V2 به‌صورت تکی یا دسته‌‌جمعی روی کل محتوای سابسکریپشن (متن ساده یا Base64).
🔹
سازنده کانفیگ زنجیره‌ای (Chain Builder):
ترکیب دو پراکسی (مثلاً وارپ/ورکر به سرور اصلی برای ثبات آی‌پی و رفع فیلتر) و تحویل خروجی آماده JSON برای هسته‌های Xray و sing-box.
🌐
اجرای آنلاین ابزار
💻
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3099" target="_blank">📅 20:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ob-ZBBubHNndg6TAPTr3t35hhlGGtBwFvpz4AKIcdGb1ppUGV4CgvCuWNJZiWztgah1IcMCPvr65JorrAMAs9WdqXmI_YJ_LfKl4iY-u7dZDyFbsUnasGlfIiMyki9eguAQ8jhDOhDkMPIFAeuDBM8Fg2p7P2BiRva5jIXPyP0o-_S2sEvsNMeIzn3Wl1TyhVqB4XmD7Qf5NZx286Sy9zbV6NHOf0dcpauCJfq7ryUWTXySUpz8FQSQk3sqIj9OCQZhRfNzUogQdHNq7fTV3UYaEQJBzzJt5R9dIozq0Qe856NvrQrgiR_sKdTnURX2kON4ztgXbIdnQ9rmmli2G-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی نرم‌افزار EtherDNS؛ ابزار مدرن تغییر DNS و مدیریت شبکه در ویندوز
پروژه متن‌باز
EtherDNS
یک جعبه‌ابزار همه‌کاره برای ویندوز است که علاوه‌بر تست و تغییر سریع DNS، امکانات کاربردی مختلفی برای عیب‌یابی شبکه در اختیارتان می‌گذارد.
🔹
تغییر سریع میان ۴۸ سرور DNS تاییدشده:
دسته‌بندی سرورها بر اساس ایرانی (تحریم‌شکن)، گیمینگ، جهانی، ضدتبلیغ، امنیت و حریم خصوصی، همراه با امکان تعریف DNS اختصاصی.
🔹
بنچمارک دقیق بر پایه UDP:
تست پینگ سرورها با ارسال کوئری‌های واقعی DNS به‌‌جای پینگ معمولی ICMP (برای دقت بالاتر) و انتخاب سریع‌ترین سرور.
🔹
نمایش زنده و نمودار وضعیت:
مانیتورینگ لحظه‌ای پاسخ‌دهی DNS، وضعیت آداپتورها و کلیدهای فوری Flush DNS، تجدید IP و ریست کامل تنظیمات شبکه.
🔹
اطلاعات کامل IP و لوکیشن:
نمایش لحظه‌ای Public IP، ریجن، ASN و رفرش خودکار پس از اتصال یا قطعی فیلترشکن.
🔗
لینک دانلود در گیت‌هاب
🔻
این برنامه اوپن‌سورس است، اما کدهای آن توسط ما بررسی امنیتی نشده؛ قبل از اجرا روی سیستم اصلی، سورس آن را بررسی کنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3098" target="_blank">📅 19:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3097">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📡
موج جدید اختلالات شدید روی شبکه اینترنت کشور
طی چند روز اخیر وضعیت اینترنت دوباره به‌شدت ناپایدار و فرسایشی شده است:
🔹
نوسان شدید، قطع و وصلی مداوم و افزایش بی‌سابقه پینگ.
🔹
مسدودسازی و فیلتر شدن بسیار سریع IP سرورها.
🔹
اختلال و دراپ گسترده پکت‌ها روی رنج آی‌پی‌های کلادفلر.
اگر در اتصال کانفیگ‌ها و تانل‌ها دچار افت سرعت و قطعی شدید هستید، این مشکل فقط برای شما نیست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/3097" target="_blank">📅 14:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g24z126968HXMxdZXoMGaqi_rmFC_fywG3Ugm9pcBvR7bVZJuXAMhh5o0LBp9q-1hBRjD2NWPZFj7bcJzWv2vltARSXzD9xIa4icEKUw22fdWt0NZlumq95plH61XmdGhuByjHXWkmDWrc8fGxDB_Zjo8G2uxEZvtpIKR0xhYkVIY9mmvst4b2NQY6NbHSVvP91_qyGcYLQgdFvOLEtaj6hrbFFdFqhTEZBVF4LvtAHPDqhX36XfZ_pzdw7gxkrzuH6bKz4W7Tgv2ElbOProiPtCE6ZxXg718baPPBDuyKcIe3qRee_iaL19A1dSOIn0K1f5QJQRfImwikoh4RhUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کلادفلر تأیید کرد: ناهنجاری بزرگ و افت غیرعادی در ترافیک اینترنت ایران
داده‌های رسمی رادار کلادفلر نشان می‌دهد ترافیک اینترنت کشور از صبح یکشنبه ۱۲ مهر با افتی ادامه‌دار و تغییرات ساختاری بی‌سابقه روبه‌رو شده است.
⚙️
شاخص‌های کلیدی گزارش کلادفلر:
🔹
افت ترافیک کلی:
کاهش محسوس در ریکوئست‌های HTTP و داده‌های جریان شبکه (NetFlows) از ساعت ۷:۱۵ صبح ۱۲ مهر که همچنان پابرجاست.
🔹
تغییر سهم پروتکل‌های وب:
سهم ترافیک انسانی HTTP/1.x از ۵.۳٪ به ۱۵.۲٪ جهش یافته و سهم HTTP/2 از ۹۴.۷٪ به ۸۴.۷٪ افت کرده است (ترافیک HTTP/3 و پروتکل QUIC پیش‌تر نیز بسیار ناچیز بوده و عامل اصلی این تغییر نیست).
🔹
افزایش سهم درصدی IPv6:
سهم IPv6 از ۴.۳٪ به حدود ۱۵٪ رسیده است؛ این افزایش به دلیل افت شدید حجم کل ترافیک IPv4 بوده، نه لزوماً رشد فیزیکی دیتای IPv6.
🔹
اثر ملموس روی کاربران:
افزایش شدید پینگ، اختلال گسترده در اتصال تانل‌ها و کانفیگ‌ها، و لگ سنگین در بازی‌های آنلاین.
هنوز منشأ این وضعیت میان محدودیت‌های هدفمند زیرساختی یا اختلالات فنی مسیرهای بین‌المللی رسماً تأیید نشده است.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/iaghapour/3095" target="_blank">📅 20:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0-vlvwA4ukmpg9DiI34MXX91ysmHTbDAofCn6Ro_1DChCgcT3ZEw5kPXSW7ARR1dDkqISok_gvPi-Wdba2Cf7lBYJMHYXby8Yh8DKjhodYSfThLzUyFbrjaYoufXa6696NCv-XCQ7cOz75RJvu5En7pqk1JPiw3takCD8QK6U2A4nwPhLnLQgqQB0_zSWzATjuRxRXE9V61YAssZUlu7eOfuEranFpy7wis55UkE8avo3VtzuS2Dt9m-Ph8kcPTJNhxYhIUXUTj5HT0XlQzCdHHKzySvFT0okjTC1yy2CUhnzA-Oo7rU4J-DxOJ0Ph3oMads-ppFWW9xhtxRLLL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پرونده جنجالی فیلترشکن جامپ‌جامپ (JumpJump)؛ شایعه هک فیک بود، اما بدافزار واقعی است!
اسکرین‌شات فروش اطلاعات کاربران جامپ‌جامپ در دارک‌وب ساختگی از آب درآمد، اما بررسی‌های فنی نشان می‌دهد خود این برنامه یک تهدید امنیتی بسیار خطرناک است.
🔹
نسخه‌های تلگرامی دستکاری‌شده:
نسخه‌های غیررسمی پخش‌شده در کانال‌های تلگرامی با سوءاستفاده از آسیب‌پذیری‌های اندروید تلاش می‌کنند دسترسی ریشه (Root) بگیرند؛ دسترسی که به مهاجم اجازه کنترل کامل دستگاه (دوربین، پیام‌ها و فایل‌ها) را می‌دهد.
🔹
رفتار مشابه گروه‌های سایبری APT:
تغییر سیستم آپدیت به کانال‌های تلگرامی و جعل امضای دیجیتال برای نصب بدافزار سیستمی.
🔹
مجوزهای خطرناک نسخه اصلی گوگل‌پلی:
حتی نسخه رسمی نیز ۳۷ دسترسی غیرضروری از جمله IMEI، فایل‌های شخصی، سیم‌کارت و دیتای رفتاری را ثبت می‌کند.
🛡
اقدام فوری:
اگر این برنامه را نصب دارید، فوراً آن را حذف کرده و دستگاه را اسکن امنیتی کنید.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/iaghapour/3094" target="_blank">📅 16:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg37yn6WPuEG9_QLXKhhu4FqIHED5bvr7plO8kTIyJgVWTjmi9oRKDyJ3tlzyebj0qXs3fqP71MmdivIUXmYEjT5_ypbHvYWMJVxpknXx2-mAE0xmWgGAqGwkLoLUrzyuJIYNDAMwjowcuwlVDwg6YavlTTpcl_CYNIAqDHoamaWymibCocZIwG-CI1tzPWI5snvZ1a_OUi5WNZsHd0osYM1xzRFKTb_zYQz8EO38R_WVIZfd8GeV1G3U9UlePx5KladjyBWrs0fqkRFoDNEEVzQao4NZASqyiXd-eeQk1wyASbBXZ10lUYNkdLyxOCkkaXf6TteZkGDG6dvnh7N8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مذاکره‌کننده گروه باج‌افزاری «کیل‌‌سک» بازداشت شد؛ مدیرعامل ۱۶ ساله یک استارتاپ هوش مصنوعی!
مذاکره‌کننده مظنون گروه باج‌افزاری بدنام
KillSec
شناسایی و دستگیر شد؛ فردی که در پوشش زندگی حرفه‌ای خود، مدیرعامل یک استارتاپ حوزه هوش مصنوعی و تحول دیجیتال بوده است!
⚙️
جزئیات ماجرا:
🔹
هویت دوگانه متهم ۱۶ ساله:
وی در معرفی رسمی خود مدعی شده بود که هدفش کمک به کسب‌وکارهای کشور عمان و منطقه خلیج فارس برای پیاده‌سازی راهکارهای هوش مصنوعی و ورود به دنیای دیجیتال است.
🔹
نقش در حملات سایبری:
شواهد نشان می‌دهد این نوجوان به‌عنوان مذاکره‌کننده و نماینده گروه KillSec با قربانیان حملات باج‌افزاری تماس تلفنی برقرار می‌کرده است.
🔹
سرنوشت قضایی:
متهم اکنون با احتمال استرداد به پورتوریکو روبه‌رو بوده و مجازاتی تا ۱۰ سال حبس در انتظار اوست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/iaghapour/3092" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxXxei3euPNO3k9drbltu3eVxWRqtYzuwCJ2CrxiO5kk6_H4CmdtodAdXt9bL9OypHbyDbyOkknCYfJstm2-TVQ2z0ZRb4FAdol5kws0rt3pOL8pBoI1ea1i2Pbhhp0WyCBCygmHwBVRqmY-HmY4o16jvQSh9fMqj6lq9amYhiuU0nVqErv1yemNDin-IMEOsZL_lXX2lWve2t7otn7O1IZ2Btnl74_R5G8hz8OJOdGQBePBZYwIrcd7_q39DawalcphjR1yeIe_2ki9kPrD_6gJ2btWp0gKvGtXTqsgOR8sGqR5_8DTNJrwmjOPg1NAURIMIeGittTrMYrN8nbFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
️
پایان دسترسی رایگان به جمینای پرو و فلش
گوگل با به‌روزرسانی اسناد پشتیبانی خود سیاست‌های جدید دسترسی به مدل‌های جمینای را اعلام کرد که بر اساس آن، دسترسی آزاد به مدل‌های پیشرفته محدودتر می‌شود.
⚙️
جزئیات تغییرات و سطح دسترسی پلن‌ها:
🔹
کاربران رایگان (از ۱۷ مهر / ۹ اکتبر):
قطع کامل دسترسی به مدل‌های Pro و Flash؛ تنها مدل فوق‌سبک
Flash-Lite
در دسترس خواهد بود.
🔹
پلن AI Plus (ماهانه ۴.۹۹ دلار):
حذف دسترسی به مدل Pro؛ دسترسی فقط به مدل‌های Flash-Lite و Flash محدود می‌شود.
🔹
پلن‌های AI Pro (ماهانه ۱۹.۹۹ دلار) و AI Ultra:
دسترسی کامل به هر سه مدل Flash-Lite ،Flash و Pro حفظ می‌شود. همچنین قابلیت پردازش عمیق
Deep Think
بدون هزینه اضافه برای مشترکان AI Pro فعال خواهد شد.
📊
قابلیت‌های جدید و سیستم محدودیت مصرف:
• امکان تنظیم سطح پردازش و تفکر مدل‌ها در سه حالت کم، متوسط و زیاد (تحلیل دقیق‌تر به قیمت مصرف بیشتر سهمیه).
• ریست شدن سهمیه مصرف مبتنی بر توان پردازشی هر ۵ ساعت یک‌بار تا سقف مجاز هفتگی.//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/iaghapour/3091" target="_blank">📅 17:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3089">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKjsdsO5wwRGnQ0dopxvPmYdo_dWnizpCvMAnzsGhFtBaHkwu8J_BKLrWlcdjiUjw8p9N1oi6IgnZNVtbv1pC_c6RZJ5DDng4Q5OQVR1TEYZPrP0jldiDtE9JnTBE6VBH1PD7fx-I0v7DeXYgsM4cgZa0zgb-8DKzGIbTisipedt1O2guUQqfeJA9Q05i0846zM9vRzVWo5Zd_3tNWHVlVhzl-pcvhNv4f-wWV4OGLySPYCkkKS3lig3hmhT1oOJ1yLUO8ENS-flhYZ4C6yDW2ccqdOB2oNIkPLxHaUDeMZzkYSzmDyECxkTBZ1PJcbr9SQprGSzO-lqzZfVIGWx9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
معرفی FleetPanel؛ کنترل‌پنل امن برای میزبانی هم‌زمان چند ربات تلگرام روی یک سرور
اگر چند ربات تلگرامی را مدیریت می‌کنید، اسکریپت و پنل
FleetPanel
به شما اجازه می‌دهد همه آن‌ها را به‌صورت کاملاً ایزوله روی یک سرور لینوکس بالا بیاورید.
🔹
ایزوله‌سازی کامل هر ربات:
هر ربات دارای یوزر مجزای لینوکس، استخر PHP-FPM اختصاصی، دیتابیس MySQL جداگانه، کانفیگ اختصاصی انجین‌ایکس و گواهی SSL مستقل است تا مشکل یکی به بقیه آسیب نزند.
🔹
پنل وب و CLI:
داشبورد مانیتورینگ مصرف CPU و رم، نصب خودکار ربات از طریق وب‌هوک و دریافت توکن، تهیه بکاپ و بازگردانی خودکار.
🔹
امنیت سخت‌گیرانه:
رمزنگاری توکن‌ها و پسورد دیتابیس با استاندارد AES-256-GCM، هش ایمن رمزها با Argon2id، فعال‌سازی CSP سخت‌گیرانه، محافظت در برابر حملات CSRF و مسدودسازی وب‌هوک‌های بدون Secret.
🔹
عدم تداخل با سرور:
اسکریپت به سایت‌ها، گواهی‌ها و دیتابیس‌های موجود سرور دست نمی‌زند و فقط فایل‌های اختصاصی خود را اضافه می‌کند.
🔗
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/3089" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سلام بچه‌ها، وقتتون بخیر.
به دلایلی حساب‌های توییتر (X)، اینستاگرام و چند تا از پلتفرم‌های دیگه‌مون رو خودم موقتاً غیرفعال کردم. از طرفی طی روزهای آینده رویکرد و مسیر کانال هم یه سری تغییرات داره و از مباحث فیلترشکن و... فاصله بیشتری میگیریم.
فعلاً نیازی به توضیح بیشتر نیست؛ سر وقتش کامل براتون توضیح میدم. ممنون از همراهی همیشگی‌تون.
💚</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/iaghapour/3082" target="_blank">📅 20:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3081">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULn8MwsIfM0NuIItAMr0cl8FUathPGd2H7CTrxRC-r-FzrNpW1Tv-DaOua_d3bsa2Fr9Qi8F4r1ccvhDkyMxUvSyUB_W8VtGYtgSmvXz0HDzQxrVN6SAOxCrgaE5idRzmRl7_a0opsITNPMoYNKl-JftIdgZdP2sa-HGiYZ0Awb7ncCP0ZOiNdR2l_j7Bkd8CHgICZXeQog6HQoPfaqYmnLEwVqQGi5DXWwMebml36Gt4XZ86eB_DE5NFtR6IO8dsNUy9JEJkVwppVLHtWg5LCtGjxCRvy-c13WTUIBTFEpkE8GpytFITXkymOko2-gyHIobEPEA8YLGA7gwCpC8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
درخواست اپراتورها از وزیر ارتباطات: فیلترینگ اینترنت ثابت و فیبر نوری را بردارید!
در جلسه کنترل پروژه فیبر نوری، مدیران اپراتورهای اینترنتی با اشاره به هزینه‌های سنگین توسعه و عدم استقبال مردم، پیشنهاد رفع فیلترینگ اختصاصی روی شبکه ثابت را مطرح کردند.
🔹
پیشنهاد رفع فیلتر برای جذب کاربر:
نماینده صبانت اعلام کرد برای ایجاد انگیزه در کاربران و افزایش فروش ترافیک جهت جبران هزینه‌ها، مسدودیت پلتفرم‌ها حداقل روی اینترنت ثابت برداشته شود؛ چرا که کنترل امنیت در شبکه ثابت ساده‌تر است.
🔸
اقتصاد در حال احتضار اپراتورها:
نمایندگان شاتل و پیشگامان از خسارت‌های چندصد میلیاردی ناشی از قطعی‌های اینترنت، هزینه‌های استهلاک باتری‌ها در خاموشی‌های برق تابستان و عدم اصلاح تعرفه‌ها گلایه کردند.
🔹
کیفیت پایین اینترنت ثابت فعلی:
به گفته مدیرعامل زیرساخت، کیفیت ADSL کشور به شدت افت کرده (سرعت آپلینک ۶۰٪ مشترکان زیر ۸ مگابیت است) و همین امر بار مصرف را به شکل نامتعادلی روی شبکه موبایل انداخته است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/iaghapour/3081" target="_blank">📅 19:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5jE-VVrSyjptD2SM4OZLWIpkrRjTouEdW9RZJPNrFP4wsk_XnE-cX96Xl2FvKpPHMQq5WT6jtSQsNQQSSdMerpBaHd5howUT5huKcmg9Hkd2i1HQYt3KsuvLWHFJYk6dSKfAvFvhviveipAFPz8G5axhi5SNiXS9IGCLfmVeA-4dlAM0aMo72Y1ZL1jX-aNvQdrFYvjrGc2uukkBQ0EMdrhFCxtWyuaiTg3UEAYuPEsEre3JrHic7mdK6mK1PvcrMr5KJcxpFOgumnVw9oTf1ytjmNofrufDCl0TqBnxUTGICkCea5Jjh9zhtVsQlktRaRtGSC-cavDG7_eXjMvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی‌ها واقعاً فکر می‌کنن ما همین الان از پشت کوه اومدیم!
🏔
😅
ماجرا از این قراره که وقتی ما بین کامنت‌های یوتیوب قرعه‌کشی می‌کنیم، تو ویدیوی اعلام نتایج، اسم، عکس و آیدی دقیق برنده مشخصه. حالا اتفاقی که میفته اینه که یه عده از دوستانِ فوق‌تخصصِ جعل هویت، تو سه‌سوت میرن تو یوتیوب اسم چنل و عکسشون رو دقیقاً شبیه برنده می‌کنن، یه آیدی مشابه هم میسازن و میان میگن: "سلام، من همون برنده‌ام، هدیه‌م رو رد کن بیاد!"
🥸
🎁
رفقای زرنگِ من! فارغ از اینکه این هدیه واقعاً ناقابله و فدای سرتون، ولی یوتیوب یه چیزی داره به اسم Handle (همون آیدی با @) که تو کل دنیا یکتاست! یعنی هیچ‌کس نمی‌تونه آیدی تکراری داشته باشه. ما هم موقع تحویل جایزه، فقط همون آیدیِ اورجینال رو چک می‌کنیم، نه یه اسم و عکسِ فیک!
🕵️‍♂️
خلاصه که سرعت عمل و خلاقیتتون قابل ستایشه، اما متأسفانه جواب نمیده!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/iaghapour/3078" target="_blank">📅 20:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt6tR_XwNUkTqnTnoiCnz4imfsK2Wennl_DFtkc7bTSa7_wIWTntPtz03ohfNfw7zel3vwnLsemqAQ5l8tbjqqcfiruqCVeOMgys5J19yKNmdJtGNYcq-C2x5kfmAjNJyRZSGO-hcueAvos6hTfalgMNdIQcZQkX2Yi7xVN_dBtXXlf7cyoFLDZYnyphknXuUL2rF30JOb3q1g5TKMnPTOeS-2tKvuGu_7kEi9cfKir-327QrwJd_aNu9-jaHXPSN05avpW-O1o4IV6eCQWByuwfVRKvaUavE1PlC-87KfIcK39YsAVcA_YVfTH-jL_TVhw_Tc6ogGK7Szm8FlKkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
مدیرعامل مخابرات: اختلال اینترنت برطرف شد / وضعیت IPv6 بررسی می‌شود
محمد جعفرپور، مدیرعامل شرکت مخابرات ایران، در گفت‌وگو با رسانه‌ها از برطرف شدن اختلال چند روز اخیر اینترنت و فیبر نوری خبر داد.
🔹
علت اختلال چندروزه:
قطعی اینترنت، سایت شرکت و سامانه ۲۰۲۰ به دلیل ارتقا و به‌روزرسانی زیرساخت‌های سامانه‌ای مخابرات رخ داده و اکنون اتصال کاربران بازیابی شده است.
🔹
وضعیت پروتکل IPv6:
جعفرپور تأکید کرد از سمت اپراتورها منعی برای ارائه IPv6 وجود ندارد، اما سیاست‌های بالادستی شبکه در اختیار آن‌ها نیست.
🔹
احتمال تأثیر تغییرات دوران جنگ:
وی اشاره کرد که تغییرات فنی اعمال‌شده روی شبکه در شرایط جنگی ممکن است همچنان بر وضعیت دسترسی به IPv6 اثر گذاشته باشد و این موضوع نیازمند بررسی فنی دقیق برای شناسایی منشأ اشکال است.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/iaghapour/3076" target="_blank">📅 14:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3074" target="_blank">📅 20:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3073">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW3NToJDW8wHOnatvlhWw_VtxL_t0UP2ctZ7k7RUMWZ_tnfk0ES10yC5MCQiCeqhntsmtLOoyn6VDlKOc3sDQRvCURkeWNq_GwUXqd-Kd82NoV57cu_cmKDOQ4o6qQGGQm6LAGXsgshVP64BHSuAfZmJWaACeyhLEpv3iB5pLGDUiLiE-R5U1FMbk8NP8PvnRNr4AIs5uHRS8Mj9gZGK-0G_lZ-yv0fAr8g_JWoulfT15GJwJKpwWToVpBN4tIBJUNg3d7mO2wCUHBEMZN3kHshl0jAFLM04Oz3QyrsAWUuCYGs1eI6j2whBjULGY9KuWQWRAoQXqYY5IcT2CODtEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
تولید ویدیوهای 1080p با هوش مصنوعی برای تمام کاربران گوگل فعال شد!
گوگل قابلیت تولید ویدیو با کیفیت
1080p
را در ابزار
Google Vids
برای تمام کاربران عادی و مشترکان Google Workspace در دسترس قرار داد. این ویژگی با بهره‌گیری از مدل پیشرفته
Gemini Omni 1.1 Flash
کار می‌کند و ورودی‌های متنی، تصویر، صدا یا کلیپ‌های موجود را به ویدیوی خروجی تبدیل می‌کند.
⚙️
قابلیت‌های کاربردی و کلیدی:
🔹
توسعه هوشمند صحنه‌ها:
امکان افزایش طول زمانی کلیپ‌ها با حفظ ثبات کامل در نورپردازی، چهره کاراکترها و زاویه دوربین.
🔹
هماهنگ‌سازی و افزایش رزولوشن:
تنظیم دقیق مدت‌زمان هر فریم برای تطبیق با صدای گوینده، به همراه ابزار ارتقای وضوح (Upscale) کلیپ‌های قدیمی به 1080p.
🔹
سرعت بالا در تولید:
رندر هر صحنه ویدیویی در این پلتفرم در کمتر از ۳۰ ثانیه انجام می‌شود.
سهمیه استاندارد به تمامی حساب‌های رایگان گوگل اختصاص یافته و کاربران طرح‌های تجاری و پولی سهمیه ساخت بیشتری دریافت می‌کنند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/iaghapour/3073" target="_blank">📅 18:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭕️
اجرای مستقیم و بی‌دردسر پروژه‌های داکر با Docker Compose در دوپراکس!
🔹
دوستان عزیز، یکی دیگه از قابلیت‌های فوق‌العاده دوپراکس بخش App Space و پشتیبانی مستقیم از کدهای داکر کامپوز هست!
🔸
اگر پروژه‌ای دارید (مثل ربات‌های تلگرامی، پنل‌های خاص یا وب‌اپلیکیشن‌ها) که با فایل
docker-compose.yml
اجرا میشه، دیگه نیازی به سرور لینوکسی خام، نصب دستی داکر و درگیری با کدهای ترمینال ندارید. دوپراکس یک محیط کانتینری کاملاً آماده در اختیارتون میذاره.
📝
مراحل اجرای پروژه‌های داکری:
1️⃣
ساخت فضا: از منو وارد بخش Container Platform بشید و یک App Space با منابع دلخواهتون بسازید.
2️⃣
تب Compose: وارد فضای ساخته شده بشید و در بخش Topology، روی تب Compose کلیک کنید.
3️⃣
وارد کردن کدها: کدهای فایل داکر کامپوز خودتون رو مستقیماً در ویرایشگر پیست کنید، یا اینکه خیلی راحت با دکمه Upload YAML فایلتون رو آپلود کنید.
4️⃣
اجرای نهایی: در نهایت دکمه Apply changes رو بزنید. (حتی گزینه‌ای برای جایگزین کردن امن منابع قبلی یا Override existing resources هم وجود داره).
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کانتینرها، شبکه‌ها و والیوم‌های (Volumes) تعریف شده در فایل شما رو در لحظه می‌سازه و پروژه رو ران می‌کنه. یک مدیریت کاملاً گرافیکی، سریع و حرفه‌ای!
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/3071" target="_blank">📅 20:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iX7ON_aVL4-cYNHYS_xf_emHcmfzONcGr2lD_L6JgroTJTW4Y0OUTBxvUm1b4XNfZp1EUyAh-HK5yTGFRyM66YqF7py7BSZ8G51V-lBL8RklDIU4_413V3ux1FmqB6Xg2WHWBV03QV0RnRLovSn2tRAQan7UvAGIVwDY_wCDVuAklmQhj-OXzRkL-YHtjyqwtfzWw9Ncrv5UCbtsv_1kQBhqBzEownu7OT-spsfY9Dit3K2CNNQbW2k6NI_WxuTCK33CSP2EcvzCkkJX7p07Ays3XtCIdw13ANYYIdKrPrC1VKqwB4b1oYh0u6xvyP6HNAVEHabpyaS_gyKswyBuzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXJ139X9j7NFN6VzdsJPM2YYY5R2I8pgvCZ_76lKOSLAC1CAv68hG4dmtsg3wUmZqQGO9pwq8fyc0F97YD2RConD9mGEELPkPrMgzvsORrhKT2iiHqBow0ghF5PTHOfFPm3eBImUcjnGE2-3apVDKai18LmjYuokqq_ouEhDKhY7KsJzlH1u3qG7OVBPkqHcKqgNONXbJRvUwYeoqrjWx_Mk7AgIbZlksx3nDOpa5UGXAaV0WljoOnf3o0gvIUdTw8b6SESS2SDJgBOgHuFE9Yrs7xn5JThqQ31o2nPEPaPi9cZX9uUlaObg3lLXHFADW0-478V0zbzkUlONacgAiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه همراهان عزیز کانال!
💚
به لطف و حمایت‌های گرم شما، تونستیم
8 عدد کیف
مدرسه و تعدادی دفتر و... رو برای چند تا دختر کوچولوی دبستانی تهیه کنیم. (همشون تو عکس جا نشدن)
این هدیه ناقابل، نتیجه
مهربونی
و
همراهی
تک‌تک
شماست
و از طرف همه‌مون به این بچه‌ها تقدیم می‌شه. سال قبل هم اگه یادتون باشه اینکار انجام شد.
اطلاعات بیشتر
ازتون ممنونم که باعث و بانی این اتفاق قشنگ شدید. دلتون همیشه شاد و لبتون خندون.
🌹
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/3069" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=ntp9LJFz6HR4w2C9-vXTeVIIgHJ1tkDFFbqgtU0DPHDudTHaBt8YaqDNhJ34oHWwOlbLdphODR8mhZ1ErIYq3s5EeeeERoC4yl-VIsFs9oA1d060uv3LSTtZRh3McrXbReLhPRLIcHAHaA1q26D8OBm0jtRvBjO9fClpncGUlBejhNjWc-cDA-Okq8TanrtuqxxPAoo6dZpUiytlrPahm5NQzSg403X0NUEKDtFUGR3mntq2G47TuJchY7ax4Ye6L0jv1UGGMbtwSi1HZQSfuRtENzSPLb5vRu4dmauS6H-enVrwtivBiktGJR6fcrju1iGkow_5wgRybc6b790rsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=ntp9LJFz6HR4w2C9-vXTeVIIgHJ1tkDFFbqgtU0DPHDudTHaBt8YaqDNhJ34oHWwOlbLdphODR8mhZ1ErIYq3s5EeeeERoC4yl-VIsFs9oA1d060uv3LSTtZRh3McrXbReLhPRLIcHAHaA1q26D8OBm0jtRvBjO9fClpncGUlBejhNjWc-cDA-Okq8TanrtuqxxPAoo6dZpUiytlrPahm5NQzSg403X0NUEKDtFUGR3mntq2G47TuJchY7ax4Ye6L0jv1UGGMbtwSi1HZQSfuRtENzSPLb5vRu4dmauS6H-enVrwtivBiktGJR6fcrju1iGkow_5wgRybc6b790rsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی (دوره سیزدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده  اکانت هوش مصنوعی مشخص شد:
👤
برنده عزیز با آیدی SattarBayat، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3066" target="_blank">📅 16:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC7QNijYHC0VHcJSLWY14PF0PXDuOKISZC_J58qKwYjvAw3NlJ9v0E7Nc6oHLUcimyQMtwSA5uS_DkshIx4RFhO1oetr8Qi3n7u6iEM8dlYC5BIdMdSbCbvm4Z-B2TrgAvlrgKQXYxZZ5aM3wnffkNxfa2KP6FUFBkbTerUjznJAqBZPncvzqMXOyELdWNczhJYmVdsJd1Hvu5OfCVJCx6AqXARvhiLUg80F5zr5P939HNn66moXE964l1Wo2nxhq9bMvy85BprRmTXS2O_t5JNZE5htErE1RkXfnXSCYwaUJ2MlBLMCkggYRUZt-2zZFYzSbDR1WCuoOxxukKOWIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نشت اطلاعاتی چیست و بعد از لو رفتن اطلاعات چه باید کرد؟
رخنه‌ی اطلاعاتی زمانی رخ می‌دهد که هکرها با نفوذ به سرورها و دیتابیس شرکت‌ها، داده‌های هویتی، تماس، رمزها و اطلاعات بانکی کاربران را سرقت یا در دارک‌وب منتشر می‌کنند.
⚙️
۵ اقدام فوری و حیاتی پس از افشای داده‌ها:
🔹
تغییر فوری پسوردها:
تغییر رمز حساب هدف و تمام سرویس‌هایی که رمز مشترک داشتند (با کمک Password Managerها).
🔸
فعال‌سازی تایید دومرحله‌ای (2FA):
فعال کردن کدسازهای معتبر مانند Google Authenticator روی ایمیل و تمام شبکه‌های اجتماعی.
🔹
امن‌سازی حساب‌های بانکی:
مسدود کردن آنی کارت مشکوک، تغییر پسورد اینترنت‌بانک و فعال نگه‌داشتن رمز پویا.
🔸
استعلام سیم‌کارت‌های به‌نام:
ارسال کد ملی به سرشماره
۳۰۰۰۱۵۰
یا سامانه
cra.ir
برای بررسی عدم ثبت سیم‌کارت مخفیانه با هویت شما.
🔹
هوشیاری در برابر فیشینگ ثانویه:
عدم کلیک روی پیامک‌ها یا ایمیل‌های مشکوک.
⚖️
در صورت بروز سوءاستفاده‌های قضایی یا مالی، فوراً از طریق مرکز فوریت‌های سایبری پلیس فتا (
cyberpolice.gov.ir
) موضوع را ثبت و پیگیری کنید.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3063" target="_blank">📅 20:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3057">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9aICUuFBrtnByjZS9Q8OJHpwwU2fugWycVOLnjTlV4IsVg3DtoEKM2UISNnrIw6s3mNhKhIBxAZTg63J5-XjaFkGY-3WnrCAANiS2PNTOr-Cx4RNQCGEyex1YAW52GaU1_l_2XKdVDYS33tNMMMzaCSMbMAGSKEJRpAikXzMZU9V9oew66azdABsc8TeciwVD9Ss5NBGLe73ywDHzOAyElqU2u-1MT646RKQXsEj_ZPnITuPi6g_p9Jp01PMft_1HDeF3lvT2K2tEPj0jA3fKTLuXlFQvLtbhj0ZCJAGmxJgjwPKFJ4u-hBXx2v8XfjWNZXuvvIFuWtfM_LA1qAng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎒
حرکت جالب WinRAR؛ فروش کیف به قیمت ۵ لایسنس نرم‌افزار!
شرکت
WinRAR
از یک کیف جذاب با طراحی آیکون نوستالژیک و معروف کتاب‌های خود به قیمت
۱۵۰ دلار
رونمایی کرد.
اکانت رسمی WinRAR در توییتر (X) با لحن طنز همیشگی‌اش نوشته:
«حالا که هیچ‌کدومتون پول لایسنس برنامه رو نمی‌دید، حداقل بیاید این کیف رو بخرید!»
😂
قیمت ۱۵۰ دلاری این کیف معادل خرید حدود ۵ لایسنس رسمی نرم‌افزار است و یک راه جالب برای حمایت از سازندگان این ابزار نوستالژیک به حساب می‌آید.
©️
Behrad Javed
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/3057" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw8cd6fTqM4a0NyODLYYYsQ1f-b_n8XoVb_imICGjM_inQoQuoM6KsxSh6sGCNZWH7hhJ3ZmDBOnFO-5zYI2kOp_hyXxon-9H6Xj1HKhzZGgFeVW_Qg0zSMzjdhNKTmuo0ZYz7Im6uJmiSONPcMPcNNLaZ43AI2vL7F90m2wozCL7kYlGx-hqa3HZpU8sKUd0Eh4R_X1B08HmuSpjKQcONYWpnjd_UigD4iMY_v6-EV4NWRAxiBH9ojZV8KXTjMd6i5IDs4lI0meUWZM4FhpNF7GKDk51QOQoHwkFpFsOwNDS6DMsv9VS7dDZSqZVYUMkpQ8iQkfBOVIYwYRPXRTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
رئیس جدید گوگل دیپ‌مایند: جمینای 4 تقریباً برای عرضه آماده است!
پس از مدتی فاصله گرفتن از رقابت پرچمداران، گوگل در آستانه رونمایی از مدل قدرتمند و مورد انتظار
Gemini 4
قرار دارد. «کورای کاووک‌چوغلو» رهبر جدید بخش دیپ‌مایند گوگل اعلام کرد این مدل در مراحل پایانی ارزیابی قرار دارد و بسیار زودتر از پایان سال جاری میلادی عرضه خواهد شد.
🔹
عرضه زودهنگام نسخه پس‌آموزش:
کاووک‌چوغلو اعلام کرد با توجه به نتایج فوق‌العاده و هیجان‌انگیز تست‌ها، گوگل قصد دارد در اولین فرصت نسخه‌ای از فاز Post-training را منتشر کند و سرعت ارتقای مدل‌ها را بالا نگه دارد.
🔸
بازگشت به رقابت با GPT-6 و Mythos:
در حالی که رقبایی مثل OpenAI با معرفی مدل‌های سری GPT-6 و آنتروپیک با خانواده Mythos پیشتازی می‌کردند و عرضه وعده‌داده‌شده‌ی Gemini 3.5 Pro لغو شده بود، دیپ‌مایند هدف خود را مستقیماً روی جهش به نسل ۴ گذاشته است.
🔹
تغییر استراتژی فنی:
کاووک‌چوغلو علت تأخیر در عرضه پرچمدار را تمرکز موقت روی بهینه‌سازی مدل‌های سبک و سریع Flash دانست و تأکید کرد گوگل همچنان جایگاه خود در خط مقدم هوش مصنوعی را حفظ خواهد کرد.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3055" target="_blank">📅 16:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX15tyBpLk4FewwKpzAShSoT6ur5tosVhhQ0AFYRCJT7UNewfEbqtFM39KICA7VAN4lBulqXuIwQF0_HFkigbh40Wa5CaonG41RBr-ucCgrQAFVgPQ1hYPA4-jCUfp39quV_h75DVPeNBWOzZ-XrB0VIswWrdlJ7kJHfFWEiWVb0H7dLRnfE2XdaHLBXPOlrDcVJ8AkRwpHaXtB2o-7-hiXMK0weIsvVMPUM6YnywspevPnDf8V2Cdn8e4NmWDeTExFICj_4GqerehZp7InPgo6xZ-Xj2rueVJrGNS67H5eULG0-t3HV1DRuILXvIKcv6lOPIrVgBYZ0wfti9jIgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گزارش رگولاتوری از ماجرای اتمام زودهنگام بسته‌ها
سازمان تنظیم مقررات پس از بررسی گلایه‌ها درباره پایان زودهنگام بسته‌های اینترنت، اعلام کرد اپراتورها تخلفی نداشته و ضرایب مصرف را رعایت می‌کنند.
⚙️
دلایل اعلام‌شده برای اتمام سریع بسته‌ها:
🔹
کیفیت ویدیوها و فرآیندهای پس‌زمینه:
افزایش حجم محتواهای ویدیویی، آپدیت خودکار نرم‌افزارها، بکاپ‌های ابری و فعالیت برنامه‌ها در پس‌زمینه از دلایل اصلی جهش مصرف عنوان شده است.
🔹
شفاف‌سازی ریزمصرف:
رگولاتوری اعلام کرد عدم شفافیت برخی اپراتورها در تفکیک ترافیک داخلی و بین‌الملل پیگیری و اصلاح شده تا مشترکان دقیق‌تر مصرف خود را ببینند.//شبکه‌چی
💬
خلاصه اینکه اگه قبلاً بسته ۱۰ گیگی یک ماه براتون کار می‌کرد و الان یک هفته‌ای تموم میشه، مشکل از سیستم نیست؛ مصرفتون یهویی رفته بالا و شما حواستون نیست!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4cs30AffsTnounBSHGBJcJIPIPoS0nloe7fbzmYV0_izw1FWKW1GnbAKXgc0UPFdyJjuSxpk2uFVqZzbcHd10pt-6Ei4DOLAe5ovG-vVIjGt2wrl-E4AwL6RV2ogMnivADUKd-9xME4S9nIOqm-Zzs0IClNRbqLMgU3i0Ad62QS2PUkRdvjcHUZBTTm9vGSBYxFlnI_w2JMPoQZmXGKSE8zdlLpHyuppELfaKbDmsWgk382dXVeCRd81zmsLjEbd7Xi9bq47WQ0bqcO1WbSUTFCNfUyeeQvkvyNHhJEiRNI8Prvz8oNiHgS7AY-2pV4pRcrrKOQyVWZARxF4zyBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی بدون تانل + پنل مدیریت (مشابه شکن)
🔹
خیلی وقت‌ها برای دور زدن تحریم‌های اینترنتی (سایت‌های برنامه‌نویسی، بازی‌ها، صرافی‌ها و...) نیازی به درگیری با تانل‌های پیچیده نیست. تو این ویدیو بهتون آموزش میدم چطوری یک تحریم‌شکن شخصی قدرتمند (مشابه سرویس شکن) بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awxTx2GWVskDMjMssgW5uhqPNEP85wt3VBL-oBGQGLIsHcaVw3Uk1YnfVZ-hAReAZ4eQN8Ws-LZcUSHSX6V7F6NMfu3EfnkDbfZi_GV83jz3j7DchZ_-boVgQbBaWEDAscImPGOgRI5zkxSHa31pPVPGCy7tB0-6B4wBAbhB4jsOFAtGVeUEDcxNxizspNFlpq7Q9-L2H1oMde8YLu7MgPFxQcEYWZ8TMu31fREuGOHYMyF4G3vV7_5JDEvgqP-60AitVxZbckUmzFM4cHGQPji9LBPFTcl6dFw6VlKvSJFNSEYx8j20vPILuRv-WWRJYZfG3_Xvr560-2iOm-YRWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GPT-6 Sol و GPT-6 Luna؛ مدل‌های جدید اوپن‌ای‌آی با نصف قیمت!
اوپن‌ای‌آی دو مدل جدید
GPT-6 Sol
و
GPT-6 Luna
را با تمرکز بر سرعت بالاتر، خطای کمتر و
۵۰٪ کاهش هزینه API
معرفی کرد.
🔹
هزینه بسیار پایین‌تر:
ورودی Sol به ۲ دلار و Luna به ۰.۱۰ دلار به ازای هر میلیون توکن رسیده است.
🔹
عملکرد قدرتمند:
در بنچمارک‌های برنامه‌نویسی و اتوماسیون (نظیر AutomationBench و DeepSWE)، مدل Sol رقبا مثل Claude Opus 5 را با کسری از هزینه شکست داده است.
🔹
کاهش ۵۰ درصدی خطاها:
دقت اطلاعاتی مدل به سطح GPT-6 Astra نزدیک شده و پاسخ‌ها در کارهای فنی شفاف‌تر و کوتاه‌تر شده‌اند.
🔹
دسترسی:
فعال در API با شناسه‌های
gpt-6-sol
و
gpt-6-luna
، ابزار Codex و به‌صورت تدریجی در ChatGPT Work و دسکتاپ.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/3048" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=ErBABVOUA1ODYSzlyBimrPoFKLH9jP8fPd40IG8YQVkg5cXE2W-6C5_3IOTUdLjysaKE2YCnAaUFoyLl6VBWUe7ZX3ri9_WkpnihRr2474CSbytovFSKDL7GQd1xhFOjhQxc8Gg6QQgujJBquhjDr9e-nSZQiUvzhUqX5Jdk2WQ4cviDj31w2hSZrzgU4IBNhZ60ZfDBD7WvII0P2qZveSzHFGRVDt7cLn2vXumsw_IeQcHLd3hsNRQ1ton9OVfvF851bZoKaJdydiT0JWDoXIE4DCSM7vYWKtWxvt9bvwkXjV0SDPOZXxiFSfVgn7MASrr6wAlz-gDy0Uon5P_86w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=ErBABVOUA1ODYSzlyBimrPoFKLH9jP8fPd40IG8YQVkg5cXE2W-6C5_3IOTUdLjysaKE2YCnAaUFoyLl6VBWUe7ZX3ri9_WkpnihRr2474CSbytovFSKDL7GQd1xhFOjhQxc8Gg6QQgujJBquhjDr9e-nSZQiUvzhUqX5Jdk2WQ4cviDj31w2hSZrzgU4IBNhZ60ZfDBD7WvII0P2qZveSzHFGRVDt7cLn2vXumsw_IeQcHLd3hsNRQ1ton9OVfvF851bZoKaJdydiT0JWDoXIE4DCSM7vYWKtWxvt9bvwkXjV0SDPOZXxiFSfVgn7MASrr6wAlz-gDy0Uon5P_86w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی 18 ماهه (دوره دوازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی 18 ماهه مشخص شد:
👤
برنده عزیز با آیدی matintarafdar4000، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3045" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9OKTGGUI7Em3cItujPQ_aXy63ySRYPx_DBzX1_SJeCAgTxWlM4vibZjYWn22jBSKCsYuFj2XB7-zE5j13-6NKun9Dtmbzw_XTTGltK2VEh2bpbH6Ooh2TYDX5vVb_4plygsNc2K5eXUF3ZRdazEiavU3jHw2zd1lk9jn-FeymkEI19B-YH50OaMp9VCOcOAwJPf9n8jeMiN7C6CPkyDB7OPVrcI9PBHktnfUWUdYCaDpyKSq74PUI1RJAspBKlSHIs8ZUSqkQn2k5Y38yMG6iLeGvJh-SWya-rurIw7o2ih6IaA5kJhROQ8UVyTEotgRb8w7UZg7KWhNTq2EQrE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل DeepSeek V4 Flash در OpenRouter رایگان شد!
نسخه
DeepSeek V4 Flash
بدون محدودیت سخت‌گیرانه (Rate-limit) روی پلتفرم OpenRouter به‌صورت رایگان در دسترس قرار گرفت.
🔹
سرعت فوق‌العاده بالا به لطف معماری بهینه MoE
🔹
کانتکست عظیم (بیش از ۱ میلیون توکن) مناسب تحلیل اسناد و کدهای حجیم
🔹
اتصال آسان از طریق API به افزونه‌های هوش مصنوعی در VS Code و ابزارهای مختلف
🔗
لینک دسترسی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/3044" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGkpzvnHnWMIs2P8OOoSMkHlw5RdpcMIg6c_kxHwH50QpN1EI2oaarkf-IC9q_NPO8lUIMPvpfSyRn6LVv0G13buxK1L4PAB7HEcNzJCsZRbH-GaN3nb_-1uqaJhiidD9K-SVATHUGZajiFICaZ997IjToEFKxtY7sq8LlVZQOax3nKoHhArpj7arL60KDTJuvK2AJ0t_0QXvu1Acs8Ic5vo82G11mDJQAcyeQyOpDHVBg8IDoh42kHBYLej35atMPX-_E0BKBaGIiNTdQumjSujawX_Qn_TNZTv6hWY4axEn48x0y7bK9kS59h5anSSUzR3vEoOtiJJmA-_V4rRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت اینترنت دیال‌آپ، صدای قیژوویژ مودم و استرس اینکه مبادا کسی تلفن خونه رو برداره قطع بشیم... و در نهایت رسیدن به این صفحه جادویی!
✨
نسل جدید هیچ‌وقت لذت و هیجان این لحظه‌ها رو تجربه نمی‌کنه:
• لرزوندن صفحه چت طرف با BUZZ وقتی جواب نمی‌داد
😂
• ساعت‌ها گشتن تو روم‌های ایرانی و چت با غریبه‌ها
💬
• تیک زدن گزینه
Sign in as invisible
برای اینکه مخفیانه بیای.
👀
• استاتوس‌های سنگین و خفنی که با کلی فسفر سوزوندن می‌نوشتیم!
تلگرام و دیسکورد هرچقدرم پیشرفته باشن، اون ضربان قلبی که موقع چرخیدن این آدمک طوسی و لاگین شدنش داشتیم، دیگه تو تاریخ اینترنت تکرار نمیشه.
😊
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3043" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnQStw92WaaA-J5WzUTolxM2fmVlxMjhOiTvAWglCRzdzHgqeeEKxM1eYxZQrUprAgGQEe--sQMmK7FOHnedgkuEWO-6HlRwcOYN2GUL3IMtJoHzdpp4kHqaIIjph-54hYgd6t1VL2TWrdSzSI_3vDSH6hsIKxjHze-xb_LtEH8CZl8XnThz6PCFZ91sJyRb00lM-c8Hi0ma7WMqxGpxK4KyftspHibEx02Ystkt4aRiujkZOehKOBdjEZKmFhm4tyqFzWxPPh9FLw38podKCdyrS-HP6EWpT6dMiXLoU6r0PXgEVZeofzP8Yagocjw_W2_QeF5S0S6m4X-Udjcm9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار مهم امنیتی: انتشار آپدیت حیاتی سپتامبر ۲۰۲۶ برای اندروید ۱۴ تا ۱۷ با رفع ۱۸۰ آسیب‌پذیری
گوگل به‌روزرسانی امنیتی ماه سپتامبر ۲۰۲۶ را برای نسخه‌های
اندروید ۱۴ تا ۱۷
منتشر کرد. این بسته به دلیل تغییر سیاست گوگل به بولتن‌های فصلی و عدم انتشار جزئیات در ماه‌های جولای و آگوست، حجم بسیار بالایی دارد و
۱۸۰ حفره امنیتی
را ترمیم می‌کند که بیش از
۳۰ مورد از آن‌ها دارای سطح خطر «حیاتی» (Critical)
هستند.
⚙️
تفکیک پچ‌های امنیتی:
🔹
پچ اول (سطح سیستم و فریم‌ورک):
رفع
۹۵ باگ نرم‌افزاری
که شامل ۲۶ رخنه حیاتی در هسته سیستم و فریم‌ورک اندروید است؛ خطرناک‌ترین آن‌ها امکان
اجرای کد از راه دور (RCE)
بدون نیاز به تعامل کاربر را به مهاجم می‌داد.
🔹
پچ دوم (سخت‌افزار و تراشه‌ها):
ترمیم
۸۵ آسیب‌پذیری
مرتبط با چیپست‌ها و درایورهای سخت‌افزاری شرکت‌هایی نظیر کوالکام، مدیاتک و آرم.
⚠️
خطر حملات هدفمند علیه گوشی‌های پیکسل:
گوگل تأیید کرده که شواهدی مبنی بر سوءاستفاده‌های محدود و هدفمند هکرها از برخی از این آسیب‌پذیری‌ها روی دستگاه‌های پیکسل مشاهده شده است.//پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/3042" target="_blank">📅 16:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3040">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcAQpIg631QAEMnx1-liLrB9I1EXn1k_L4FqKgokVQfX2KVX0-uJhiU5d7rQNUhgDsOorzVqapXLs6ZzGjtBTm37QAf4eov71skAJDDxIam8gUPZqka1pyWtDxLKv1JbAjdUr_W-QRNLm3eggbmuSTrCmMqCGqnFVkiGLldz2lgcluxGH7GZNkrAWFf0r0T4FDRArlXLlKVrAAPupOJQ6ZpS0wvr4y3N8CGzSaIdEcSGw4MXNHfNcaf0a_pu8RrqbJQgu7v-RtLdASylbNiP6Ho9B74mJmWelnOf-vHSYEunFAxKwPC6MkWUbQYrx8LhjEk3pI7m3YiFNxFyqcaTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
آماده‌سازی اینترنت برای AI Agentها توسط کلادفلر
کلادفلر در حال ساخت زیرساختی است تا عامل‌های هوش مصنوعی (AI Agents) بتوانند پروژه‌های توسعه‌یافته روی
localhost
را بدون دخالت انسان تست و اجرا کنند.
⚙️
نحوه کار:
🔹
ساخت فوری URL:
با ابزار
TryCloudflare
، ایجینت بدون نیاز به دامنه یا لاگین، سرویس لوکال را به یک آدرس اینترنتی عمومی و موقت تبدیل می‌کند.
🔹
تست و بررسی با مرورگر:
ایجینت آدرس ساخته‌شده را با مرورگرهای هدلس کلادفلر (مثل Browser Rendering) باز می‌کند، المان‌ها را بررسی و خطاهای کنسول را می‌خواند.
🔹
دیباگ خودکار:
در صورت وجود باگ، ایجینت خطاها را تحلیل کرده و کد را در لحظه اصلاح می‌کند.
🔗
تست سریع ابزار
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3040" target="_blank">📅 20:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la7HRjs7RrYKUPMozc1ycw8eMvJ136ThQxXBjvrGjTFb_WLKhWrCjUVuJTO46HzvMVwD3G9ArqvZ_P4JNP9zOBdtMmPox_UgpK_xa2_T2ikiuYmGQrhRQFgOE1djbAa5nZlO8_wf8J3yBNz3dAQbSxjEOJYN6Q6eJwWyuXui6JNjprJVbPLsqNGqcc8NrLxhqIjqNY6HdEAlGmBbopO3uZymFC3sVl2PTCfeJRfY_CC8DMWANkGClke-b0GpETAwp9D0uk-uVU_LgmLICUIGCjsrPC2r0ip6OqdnW4XVAP-5icWBnZgE1ljcDqkrMhptNBKnOmN6wItLJ-huBf0klQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش افزایش سرعت بوت و بالا آمدن ویندوز
اجرای خودکار نرم‌افزارهای سنگین و انیمیشن‌های سیستمی از دلایل اصلی کندی بالا آمدن ویندوز هستند. با دو اقدام زیر زمان بوت سیستم را به حداقل برسانید:
⚡️
۱. غیرفعال‌سازی برنامه‌های استارتاپ (Startup):
— کلیدهای ترکیبی
Ctrl + Shift + Esc
را بزنید تا
Task Manager
باز شود.
— به تب
Startup apps
بروید.
— در ستون
Startup impact
به برنامه‌هایی با برچسب
High
دقت کنید (بیشترین مصرف منابع را دارند).
— روی برنامه‌های غیرضروری راست‌کلیک کرده و گزینه
Disable
را انتخاب کنید.
⚡️
۲. تنظیم سیستم روی بالاترین کارایی (Best Performance):
— وارد
Settings
شوید و به مسیر
System
⬅️
About
بروید.
— روی
Advanced system settings
کلیک کنید.
— در تب
Advanced
و بخش
Performance
، گزینه
Settings
را انتخاب کنید.
— تیک گزینه
Adjust for best performance
را بزنید و روی
OK
کلیک کنید تا افکت‌های گرافیکی سنگین غیرفعال شوند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3039" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rswedwgT8YHPk4n9mtuVZfE-lNzQpZQ6ls-d7SRIOhr2Sco_zDWTrADc70PDDgu88CIiT9bKCX6lTk2PpQ8zkwnwIJMXC2np6639jy-Q05kzm5A2xT9r0XO49Gvzcj86ER70Rh6SExxVfVgV7i0M58oEenx5EqcTrIMPTvS-a_F5AHPmwZkpm3ZOlnpC3YWrlXcCP0E4aZMkj2uPBotxBNRF0f9JlBBSasKwlx896_ODdrLc6_4cy--jf7400vwd22SSP7Yv-jFg6xmGSbcNgi7axy1ZHO2Hz3kKplIbM9-Dc7-ngm-CG43o3aNFYHxuo1_mnnu69a2c1_avKCzbmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
هوش‌ مصنوعی Qwen و Kimi هم کاربران ایرانی را محدود کردند؟
دسترسی کاربران ایرانی به دو ابزار محبوب هوش مصنوعی چین، Qwen متعلق به علی‌بابا و Kimi ساخته‌ی Moonshot، با اختلال جدی مواجه شده است.
🔸
گزارش کاربران نشان می‌دهد دسترسی به نسخه وب و حتی API این سرویس‌ها در برخی موارد با خطاهایی مثل 403 Forbidden مواجه می‌شود؛ با این حال، هنوز هیچ‌کدام از این شرکت‌ها به‌طور رسمی درباره مسدودسازی کاربران ایرانی اطلاع‌رسانی نکرده‌اند.
🔹
هنوز مشخص نیست این محدودیت موقت و مرتبط با سیستم‌های امنیتی است یا آغاز یک محدودیت جغرافیایی دائمی.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3038" target="_blank">📅 14:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmoK5WOyJNaRFInSvs2xK5gqm6tgZjgf4JXNv97MvO6XId2sgpTsIsiVj1ZySe0SkdtfozyjIc2Fy5ZePeIv-hQA-Csiyb6_mKdIpW9iqlUN8uWAlkZM0cRTweN3YK1zK31hU-7cFgWDPfTnmyI0BFHbjlVNDJpISxk7SgsGuUxLm8raCyMNhVG21UCCSV4piDq5ajXYc9ExYA00EceXPDbk1W5SKeeoo3Eco09JQwcmIKTQ6RW9x01xci9G0DYxakCu3pxowXTzz_h9UiobVQtWiGX-SfK1D5wd1TqwdiocqoN1x57giaPjCoaURgnCXXUdDG0tXVZwcWbGSTLaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
یک پنل، ۹ پروتکل فیلترشکن! با پشتیبانی همزمان
😍
🔹
در این آموزش، نحوه ساخت یک پنل حرفه‌ای با پشتیبانی همزمان از ۹ پروتکل و سرویس مختلف شامل OpenVPN، WireGuard، AmneziaWG، IKEv2، SoftEther، SSTP، L2TP، Cisco و Telegram Proxy رو یاد می‌گیری.
🔹
این پنل علاوه بر پشتیبانی از چندین پروتکل، قابلیت‌های متنوعی مثل نمایندگی، مدیریت حرفه‌ای کاربران و امکانات کاربردی دیگه رو هم در اختیارتون قرار می‌ده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو قرعه‌کشی اکانت هوش مصنوعی 18 ماهه داره،
برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/3036" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT7zMgCfXIdfSxqP3xkJy_Y-pTLqjVjvLVi3yAXU0bPgAsfeB8WgMW4RU5WaptDn37skYdCHilKNGP5yRmaV5clQirruDg2p4Ilak4Ep6RZESoEdgPwPKyJju9Nyk9TyH93BMZg_q06R8e5AcicyDrcEK1k7suz6RPWe8sYVByG3HtfkH4qD9itteevbwNvd3ZL0GD8sf30y-sCGN94zooKv5uHlNal_Q2XkOD64QI6iqyLBkCvURuCo6sU8YPlkmCRQHvj4rfvGPmC2AqdTUGj9x-Uhi07pPT3mR20Vn1cTzWt7bGwTv8xQAEq_dw_3HHXci1Sd2qCj6-5Zcgsi3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
حجم ویدیو و عکس‌هات رو راحت کم کن!
اگه برای ارسال یا ذخیره‌سازی فایل‌های حجیم ویدئویی و تصویری مشکل داری،
CompressO
می‌تونه یک گزینه کاربردی باشه.
🔹
یک ابزار
رایگان و متن‌باز
برای فشرده‌سازی ویدیو و تصویره که روی هر سه سیستم‌عامل
Windows، Linux و macOS
اجرا می‌شه.
🔹
پردازش فایل‌ها به‌صورت
کاملاً آفلاین
انجام می‌شه؛ بنابراین برای فشرده‌سازی نیازی نیست فایل‌هات رو روی سرور یا سایت خاصی آپلود کنی.
⚙️
این پروژه از ابزارهای قدرتمندی مثل
FFmpeg، pngquant و jpegoptim
برای کاهش حجم فایل‌ها استفاده می‌کنه.
🔗
مشاهده و دریافت پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشب روشن</strong></div>
<div class="tg-text">چشمان یک انسان دیگر باش... فقط با نصب یک اپلیکیشن رایگان!
👁️
❤️
.
تصور کن گوشیت زنگ می‌خوره؛ یه تماس تصویری ۱۰ ثانیه‌ای!
پشت خط، یک فرد نابینا است که فقط می‌خواد بدونه تاریخ انقضای این خوراکی چیه یا تابلوی جلوش چه آدرسی نوشته. تو توی چند ثانیه جواب می‌دی و استقلال و لبخند رو بهش هدیه می‌کنی!
✨
برنامه Be My Eyes داوطلب‌ها رو به افراد نابینا وصل می‌کنه تا کارهای روزمره‌شون رو راحت‌تر انجام بدن.
📌
چرا نصبش کنیم؟
🔹
کاملاً رایگان برای اندروید و iOS.
🔹
بدون تعهد زمانی (وقت نداشتین تماس رو رد می‌کنین).
🔹
حس فوق‌العاده با یک کمک ساده.
📲
دانلود:
نصب از گوگل پلی برای اندروید.
نصب از کافه بازار برای اندروید.
نصب از مایکت برای اندروید.
نصب از اپ استور برای آیفون.
📢
لطفاً این پست رو توی گروه‌ها و کانال‌های دیگه هم بفرستید.
شاید فوروارد شما باعث شه افراد بیشتری نصب کنن و گره از کار ده‌ها نفر باز بشه. مهربونی رو تکثیر کنیم!
🕊️
✨
.
@shaberoshanIR</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3034" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsKI9c4EBsdnxh22bjjo8Oi6TFbmyeKZ20Q-7KZ1_aovLTePlNj8Uyhuse95_VfxaOQa_Iqh3BrXSuXBi2rZHSQ1S8Jc52JEMpcvEZMQgu4FoWfUECqJys9YvIA1kBdCGg3Zez0WlJnQDQ_-8St5AjHzHLdDUQ5JDAPKykVoEveC2FWpGF6cnuNyufEeTdLY-jNtK1K_nlMR7MgyLoTTFl4eKDZ22ikxD2fUwYAK4LsVgpp-dL6hiSRxR8FDCI6i_Sz1K5sbBjRNe7WTVeNUM383u6ZsP4DsqXFOclr8QYtl0RutHilxkDhiQq55HDbKR0BCeKXtP7d6ueCALujkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج جمنای از محیط آزمایشگاهی و نفوذ به ۳ شرکت واقعی!
گوگل اعلام کرد هوش مصنوعی Gemini در جریان تست‌های امنیت سایبری، به دلیل دسترسی ناخواسته به اینترنت، از محیط قرنطینه خارج شده و به زیرساخت ۳ شرکت واقعی نفوذ کرده است.
🔹
نقص در اتصال به وب:
دسترسی اینترنتی ناخواسته در محیط تست به مدل اجازه داد فراتر از آزمایشگاه عمل کند.
🔹
خطا در تفکیک هدف:
مدل قرار بود یک شرکت فرضی را تست کند، اما به دلیل تشابه نام، شرکت واقعی را هدف گرفت.
🔹
ورود با حدس پسورد:
جمنای با کشف و حدس گذرواژه‌ها وارد شبکه‌های این شرکت‌ها شد.
🔹
توقف خودکار:
مدل پس از تشخیص واقعی بودن محیط، عملیات را فوراً متوقف کرد و آسیبی به بار نیامد.
⚠️
باگ دسترسی اینترنتی در محیط‌های تست برطرف شده و به شرکت‌های هدف اطلاع داده شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMYHzhcT2XpMRcWAHd-r2h0KPsRLTs8kvowiaeA__S5mr5GDGFsQOLG6S7P5lAHu-EYjp9XEXHmsI-qLCHkFnR9V92gTcFizh0hC6LBteVuWsT-u6TdYZ5aH4g6FE30c-rcCN2CgpMYJj40jik85ZMnkIohvMSFwKhy5vqi0bu3vTy4Vg98BZyyURRcJDR0itFkpPX_bOiE_LBoK56E-jfimQQbdbsykQxIM9ox_SIC3uUFqaoZa5RJPn7EuEfoXfxMO9HifZ7xmfOvUzQ0mwKlcon8Nm_RgaxGPN-lzV0tOxSPnXDmWgWksKgkLRitzZaeUFb99cJJ6qA5lvpds-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
توقف ارائه خدمات میکروتیک به کاربران ایرانی؛ روترها از کار می‌افتند؟
شرکت میکروتیک (MikroTik) در پی اعمال مقررات تحریمی الزام‌آور اتحادیه اروپا، سازمان ملل و آمریکا، ارائه خدمات و پشتیبانی مستقیم به کاربران با IP ایران را متوقف کرد.
🔹
روترهای فعال از کار نمی‌افتند:
سیستم‌عامل RouterOS پس از فعال‌سازی، لایسنس را به‌صورت محلی روی دستگاه ذخیره می‌کند و عملکرد روزمره روتر وابسته به اتصال مداوم به سرورهای میکروتیک نیست.
🔸
چالش‌های حساب کاربری و لایسنس جدید:
در صورت تعلیق حساب‌های کاربران ایرانی، فرآیندهایی نظیر خرید لایسنس جدید، انتقال لایسنس به سخت‌افزار دیگر، بازیابی کلیدها و ثبت تیکت پشتیبانی رسمی مسدود خواهند شد.
🔹
ماشین‌های مجازی و سرویس‌های ابری CHR که نیازمند اعتبارسنجی مداوم لایسنس و تمدید هستند، بیش از روترهای سخت‌افزاری با ریسک و اختلال مواجه خواهند شد.
🔹
با پایان رسمی پشتیبانی از RouterOS نسخه ۶ در سپتامبر ۲۰۲۶ و عدم انتشار پچ‌های امنیتی جدید، مهاجرت به نسخه‌های جدیدتر برای سازمان‌ها با وجود محدودیت‌های جدید با چالش فنی و لایسنس همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=unskIsjjG0hbeqmeJsYN0qeYMiF4TcjBUqSnThppv4x0fButJAHeeUp9S8SqpqrRgsv6KmTBYNNPCuJkdZi3V2BpecRbwdHcDyne5ItSwdpjnIkb6xvjJooOtbHyCnmFAe1xq5bX3fRWUcH1EpPjavxMk8-ZHa70ouJJDTEEXKThSQ1X_oqrmTWjhVgmbo-j2ti6yASc5bhctTcuSM9c_SH7FeRXnUkLbUvqQ0JpawvKa8tL-hMu38-Ud1uAjbuNjIeRgJQrb8OaT41nybnm11_g20bFM_qLBx6e1sq99F22djYQ4PVmxkmuUCz7VaRwVbsFdqlZ5XFvbPKckZ4iUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=unskIsjjG0hbeqmeJsYN0qeYMiF4TcjBUqSnThppv4x0fButJAHeeUp9S8SqpqrRgsv6KmTBYNNPCuJkdZi3V2BpecRbwdHcDyne5ItSwdpjnIkb6xvjJooOtbHyCnmFAe1xq5bX3fRWUcH1EpPjavxMk8-ZHa70ouJJDTEEXKThSQ1X_oqrmTWjhVgmbo-j2ti6yASc5bhctTcuSM9c_SH7FeRXnUkLbUvqQ0JpawvKa8tL-hMu38-Ud1uAjbuNjIeRgJQrb8OaT41nybnm11_g20bFM_qLBx6e1sq99F22djYQ4PVmxkmuUCz7VaRwVbsFdqlZ5XFvbPKckZ4iUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
ورود مستقیم آنتروپیک به رقابت با آفیس و جمینای؛ معرفی قابلیت‌های Claude Docs و Claude Slides
شرکت آنتروپیک با رونمایی از دو قابلیت جدید متنی و ارائه‌محور، چت‌بات کلود را به ابزاری جامع برای محیط کار و رقابت مستقیم با پلتفرم‌هایی نظیر گوگل داکس و جمینای تبدیل کرد.
🔹
ابزارهای Docs و Slides (نسخه بتا):
کاربران اکنون می‌توانند مستقیماً درون محیط چت، اسناد متنی کامل و فایل‌های اسلاید ارائه ایجاد، ویرایش و دانلود کنند یا لینک اشتراکی آن‌ها را برای دیگران بفرستند.
🔸
همکاری تیمی هم‌زمان و ثبت کامنت:
همانند گوگل داکس، فایل‌ها قابلیت اشتراک‌گذاری، ویرایش گروهی به‌صورت زنده و ثبت بازخورد یا کامنت توسط همکاران و خود چت‌بات را دارند.
🔹
عرضه و دسترسی:
این قابلیت‌ها ابتدا برای مشترکان پلن‌های Pro و Max در وب، دسکتاپ و موبایل فعال شده و به‌مرور در اختیار کاربران رایگان و پلن‌های Team قرار خواهد گرفت.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4eCvQ9t_6UFlbCSUipSPrASSBEDnXMnKheUEbwNzmaByyqEcNFD27t0V-aJMXxxPmK76um8pZpNiJUTUkMNDhnIxWbKLvd1uj0Z687UkNEjA29btNEoc0jfwaH70H1bF9MoItClv_NDCkDqJQIZo1Ksdyev5Ekh7q0-GkgNfou_4mbJ9wpmshsXKX-7wIh5Xq-LViRzHAR6RYy_uOnSl3EDDa_GoXkc6lx62DFRDKBhJ4UupXw04Ysn9ZxccKlygHvWYdfkNF2I-lwqI8z-c7pGUgmpwT0Ny93cQBt1Xq5dereF0xOtumXrUt0Ay3yAJgcx9zj_Mm-r0kuhUstmxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دانلود فایل ایزو ویندوز اورجینال از سرور‌های مایکروسافت (با ۱ کلیک)
🔹
اگه از نصب ویندوزهای دستکاری شده و پر از باگ خسته شدید این ویدیو دقیقاً برای شماست. تو این آموزش، ۲ روش فوق‌العاده ساده و سریع رو بررسی می‌کنیم تا بتونید با ۱ کلیک، فایل ISO ویندوز اورجینال (ویندوز ۱۰ و ۱۱) رو از سرورهای خود مایکروسافت دانلود کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#ویندوز
#اورجینال
#windows
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js3XweyxtkfUdnKRR4U3AEKEPQJ7VQh03OlX_zJa4Ym9zQ5K8PQPTvOWVJetIdoXwY0urGSEVRKq6imH_hEGGs2p-9n9bmA7XybVkNLclGcu4-B8Sj2N8TA7POY5toJAywekbxMB3EPTnfVVzbbnCLURjrW7RYLE3G7SeGJrMcTI_ZSvGEpej5snLx9gc6Q37ejWid6a7H9zCzpgt1-Obh4tLdUTX-UtIf6lOZYyVjYnU4nmxyiJF9lFpEi36SdKN_YCHlto7LsuDRofIc6XqdtRXyUBdDx1UfnboyrqFs1jDNT8EnAxJzPLU_VpVAFF1rO4267RBfrG7e91Z9EmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
کرکر سرسخت دنوو با وجود شکایت قضایی دست از کار نمی‌کشد!
با وجود فشارهای حقوقی و تلاش شرکت توسعه‌دهنده نرم‌افزار ضد دستکاری
Denuvo
برای شناسایی و توقف فعالیت کرکر ناشناس، او اعلام کرده به دور زدن قفل بازی‌های ویدیویی ادامه می‌دهد.
🔹
شکستن قفل‌های پیچیده:
قفل دنوو سال‌هاست به‌عنوان سرسخت‌ترین لایه حفاظتی بازی‌های ویدیویی شناخته می‌شود و دور زدن آن مهارت بالایی می‌طلبد.
🔸
شروع درگیری قضایی:
کرکری با نام مستعار
voices38
توانست پس از حدود یک ماه و نیم قفل بازی
Resident Evil Requiem
را بشکند؛ اقدامی که خشم دنوو را برانگیخت و باعث آغاز پیگیری‌های قانونی برای فاش‌کردن هویت واقعی او شد.
🔹
پیام جسورانه در ردیت:
با وجود تشکیل پرونده قضایی و تلاش برای شناسایی او، این هکر با انتشار پیامی در ردیت به کاربران اطمینان داد: «همه‌چیز مرتب است و تمام کارها طبق روال عادی ادامه خواهد یافت.»
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgDyWaN0uIc7xDLaBYatpZU8rYxTUIY9LhCPRJnI3ZXW46aCEJbDRaX2M2TrRpAjL6hUqdKObImz6k9DkKEiMs8XAQxD0vd1vNmF6UKDnpTfqS1n-ROYAXQyFld3VqAdJyNQ_94LIMNxJBLHgK2kso1XTCLJlVR5dpYynrItfYo7sIe_08BpewYdPljv0UAwQ2mydvjSF2bVN3lyXmgqpaDc-ze0bQDFopLtZMzke6nuq_itVnm6khFAUE5psTeM7KFOF5Xbefy_rer2ZLEEfwNhrPS1zRuR6u8lAILuWjTbdghS91tuO12UYGfEklcOgJShsUrmA9fRCiowKXjwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Screenbox؛ پلیر مدرن، سبک و جایگزین شیک VLC برای ویندوز
اگر پلیر پیش‌فرض ویندوز نیازهایتان را برطرف نمی‌کند و از طرف دیگر ظاهر قدیمی، شلوغ و منوهای تو در توی VLC کلافتان کرده، برنامه متن‌باز
Screenbox
دقیقاً همان گزینه‌ای است که دنبالش هستید؛ پلیری با موتور پخش قدرتمند VLC اما با رابط کاربری کاملاً مدرن و هماهنگ با طراحی ویندوز ۱۱.
🔹
موتور پخش قدرتمند LibVLCSharp:
اجرای روان تمام فرمت‌های صوتی و تصویری رایج، پشتیبانی دقیق از انواع زیرنویس‌ها و هماهنگی کامل با موتور اصلی VLC.
🔸
طراحی بومی و مینیمال ویندوز ۱۱:
رابط کاربری مدرن، شفاف و چشم‌نواز بدون گزینه‌های اضافی و سردرگم‌کننده.
🔹
بهبود کیفیت تصویر (Upscaling):
قابلیت ارتقاء وضوح ویدیوها در محیطی با تنظیمات ساده، سرراست و قابل‌فهم.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYjzMa1jwoq4-icMQw0V_RVp5d7VVxrbdmZwxvkkKU6eg3W48h8KcGpitqMR4p9P6Dl0YcZqXk03FWEJKi2Ck7b1spbXZ5fCw5FCjcqLKVS3mIesYl_By5LypsRbdxnqifswiF7S7yJcic98qPo1VRIaP6dr5jwEVFHenKDBs-9BrKenDPv8HMGu8nofir7H53gsu86s7AWdOfcK7y0_cA59lghkcA8ZA6PsP-8yb4UuHw3-a8CPF1xqV8F5GB5DLfuqh4fQWlWBSdIS7XxVx2tvL0cP1QvPboMjOBwk_cGkYCdux6V9qbwl11JX7vwQTQhFo3PNmKM5jA0YjPLpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام تعطیلی رسمی صرافی کوینکس (CoinEx) پس از ۹ سال
صرافی شناخته‌شده
کوینکس (CoinEx)
که از سال ۲۰۱۷ فعال بود و به‌دلیل عدم اجبار احراز هویت (KYC) در سال‌های گذشته یکی از اصلی‌ترین مقاصد کاربران ایرانی به‌شمار می‌رفت، رسماً اعلام کرد که فعالیت خود را متوقف کرده و تا
۱ دی ۱۴۰۵ (۲۲ دسامبر ۲۰۲۶)
به‌طور کامل بسته خواهد شد.
⚙️
زمان‌بندی مراحل تعطیلی صرافی:
🔹
۲۴ شهریور (۱۵ سپتامبر):
توقف ثبت‌نام کاربران جدید و انتقال بخش معاملات فیوچرز به حالت Reduce-Only (فقط بستن پوزیشن‌ها).
🔸
۳۱ شهریور (۲۲ سپتامبر):
توقف کامل معاملات فیوچرز، استیکینگ، وام‌دهی (Lending) و بخش واریز اکثر ارزها به صرافی.
🔹
۷ مهر (۲۹ سپتامبر):
توقف معاملات اسپات (Spot) و بازخرید توکن CET با نرخ ثابت ۰.۰۰۵ تتر.
⚠️
نکته بسیار مهم:
صرافی اعلام کرده رمزارزهای غیر از تتر را ترجیحاً تا قبل از ۷ مهر خارج کنید؛ پس از این تاریخ ممکن است دارایی‌های غیرتتری به تتر تبدیل شده یا رمزارزهای کم‌حجم پشتیبانی نشوند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRmKvQ8nr2OVTuLTAkhEPlQncm3DfMiWcQgxqsJUJ9DwLEd6qbp4X3DCBonXObfs4BiW2RX2UJ_9mTVpPy9BLwgfGlmBcollMsGwBEkIzj8Wn7R7Ty4VqXkShoAKqq6NDKt2LOptHblGvLnh3WdfyFZNWW1EbU6IocSDI9QILsRkqLduxjj-rl5z6f-KQDBl-r7PebXn5omENugaFK3QkxmtDK7S9fDscU9zSrzcb1Otf1CRzSgIzWfKoTzKhN1_rJvGJIKFtmyQFjDhuzl4IGf8J_oPok2b4tkhhL4uWnLrcIB0kX8bBUq_JGyp-mt-sRmRftOlA4WdGCIGLtGh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Subify؛ افزونه هوشمند ترجمه و دوبله زنده ویدیوها به فارسی
سرویس
Subify
یک ابزار کاربردی و مدرن برای مشاهده ویدیوها با زیرنویس دقیق فارسی و حتی دوبله صوتی هم‌زمان است که بدون نیاز به دانلود فایل جداگانه و با استفاده از API شخصی هوش مصنوعی کار می‌کند.
🔹
ترجمه آنی و بدون تاخیر:
استخراج مستقیم کپشن‌های زمان‌بندی‌شده یوتیوب و ترجمه پیش‌دستانه (Pre-fetch) با سینک زمانی میلی‌ثانیه‌ای بدون معطلی.
🔸
دوبله زنده صوتی
: دوبله هم‌زمان صدا بر بستر مدل‌های جمنای، با امکان تنظیم بلندی صدا، کاهش صدای اصلی ویدیو (Audio Ducking)، انتخاب گوینده و تنظیم سرعت.
🔹
پشتیبانی از مدل‌های AI متنوع:
اتصال به کلیدهای API شخصی در Google Gemini ،OpenRouter و OpenAI به‌همراه سیستم فال‌بک (Chunked) هنگام قطعی مسیر لایو.
🔸
شخصی‌سازی و فونت‌های فارسی:
تنظیم کامل فونت، سایز و استایل زیرنویس با فونت‌های جذاب وزیرمتن، استعداد و لاله‌زار به‌همراه پیش‌نمایش لحظه‌ای.
🔹
استخراج لغات کاربردی از دل ویدیو و امکان مرور کلمات به‌صورت فلش‌کارت در حافظه محلی مرورگر.
🔗
دانلود
افزونه برای انواع مرورگر
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYv6VIs41KyWk8NfPG7G2vwUHXx9Z7G6lhVfxYLk_-sJIsman-WjyKqePoZGV-qtKRIjcTXWsrUZM6nN1hkE_greuKn2R44BbRihqEnFa9h5pEuRymq61c0lnQcQsiY0SVK8myH791Bb2AjJ2pTtc9RTDPUvq-gseVVBlGGzVXycqWqIIzKWK4bk04VGlTnRMPYwX_3_M0i3LiBAbyj-QKnn0kXPIF5KMWD2TIrABFk3ciy6_jWEpDvt5_SkTKljc6h28ZW4N3kpGwzYCnkjALNb6LDNUTdJ52Nvwj4ca8JdpdocxJo1VwYUFF4PhJPG0fD2JQ0h91GTgMxe1QGnyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل سبک Zefira؛ مدیریت هم‌زمان چندین پروتکل
پنل
Zefira
یک ابزار پایتونی سریع و کم‌حجم (مبتنی بر FastAPI و SQLite) برای راه‌اندازی و مدیریت اکانت‌های VPN است که بدون درگیر شدن با Docker، امکان ارائه چندین پروتکل را در قالب یک لینک اشتراک واحد فراهم می‌کند.
🔸
پشتیبانی از پروتکل‌های اصلی:
پشتیبانی از VLESS (همراه با REALITY و چرخش خودکار SNI)، هسیتریا ۲، تروجان، VMess، شادوساکس، WireGuard و OpenVPN
🔹
لینک سابسکریپشن یکپارچه:
ارائه همه کانفیگ‌ها در یک لینک با خروجی‌های Base64 و فرمت Clash YAML
🔀
مدیریت تانل:
تسهیل ارتباط سرورهای ایران و خارج به‌همراه بررسی وضعیت اتصال نود ایران.
👥
کنترل دقیق اکانت‌ها:
تعیین حجم، تاریخ انقضا، لیمیت دستگاه، فعال‌سازی با اولین اتصال و تایید دو مرحله‌ای (2FA).
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=XsGUsDon3Si_PwXd_IPtVvkvAzIBDmh7Do5U5V8CJTFZSy5tgdQG6DoWPEuqFL56JSloWxHreQwNdOd-_4nIfO7l6qu_2ik-pkYZ2bCsZ2zSBt7bjSdbXrztakw-Wsi2v_F34PPGAZe3IrguzMND_SlvYH6P28ben9sREcDOF_so3i6JJ6xKtVmo03kMnrVaW9eF52zLFDw6KoVm-fHC3hyDocJkg4DiNDLv_0EbwfZVM9dim4x-rmJKmyRy3oy80rZFYGgsiXw2x6GsussDEU8C68qwERAVNjQ08JYXZ7DWXxYBrosU1UfESvQcU2f9JzFQHTvHvb9iJU6eTe4j9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=XsGUsDon3Si_PwXd_IPtVvkvAzIBDmh7Do5U5V8CJTFZSy5tgdQG6DoWPEuqFL56JSloWxHreQwNdOd-_4nIfO7l6qu_2ik-pkYZ2bCsZ2zSBt7bjSdbXrztakw-Wsi2v_F34PPGAZe3IrguzMND_SlvYH6P28ben9sREcDOF_so3i6JJ6xKtVmo03kMnrVaW9eF52zLFDw6KoVm-fHC3hyDocJkg4DiNDLv_0EbwfZVM9dim4x-rmJKmyRy3oy80rZFYGgsiXw2x6GsussDEU8C68qwERAVNjQ08JYXZ7DWXxYBrosU1UfESvQcU2f9JzFQHTvHvb9iJU6eTe4j9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی (دوره یازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mahdi9226، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvoNnzgGE8uAAXKuMPNlrA98OG6Oy8EkG0a1oNoox8OPjoqV2LZVdo4P-dguOR9X64Ri1mQq64YFR1ukRPBymHgYLds3xPVMeWL3LvOgiSa_q3JqCiSZRmvf4_VDLt-iUW11jzI1L31vA81MelAih3mNIYTBWHBYpKaxDInQElaotCjocDhzX75IG6776vSGKbyBXHTxR1biY3xTXx76quKVSN-BxFQOx7bfCPxRmUhFq4qfP1NSYM7fpAy1mWWlZGNNMERBWsutGGPV-qPvRV_D8XkJ9Zo2CsvOCpZgze18_RhMfqN3qkzYRaO6s3bl9diTYxZr1Dijo4H06zL1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی DNS Changer؛ ابزار مدیریت و تغییر سریع DNS برای تمام پلتفرم‌ها
اگر برای گیمینگ، عبور از تحریم‌ها یا افزایش امنیت مدام در حال تغییر DNS هستید، برنامه
DNS Changer
یک ابزار رایگان و کراس‌پلتفرم است که این کار را با یک کلیک و بدون نیاز به دستکاری تنظیمات شبکه سیستم‌عامل انجام می‌دهد.
⚡️
پشتیبانی از بیش از ۳۰۰۰ سرور DNS:
دسترسی به دیتابیس عظیم ارائه‌دهندگان معتبر جهانی به‌همراه تست پینگ لحظه‌ای.
🛠
شخصی‌سازی کامل:
امکان افزودن، ذخیره و دسته‌بندی DNSهای اختصاصی برای استفاده مجدد.
🖥
پشتیبانی از همه سیستم‌عامل‌ها:
دارای نسخه اختصاصی برای اندروید، ویندوز، لینوکس، مک و محیط خط فرمان.
🔗
دانلود برای پلتفرم‌های مختلف
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
نصب خودکار و یک‌کلیکی اسکریپت‌ها در پنل دوپراکس!
🔹
دوستان عزیز، همونطور که در ویدیوی آموزشی مشاهده می‌کنید، پنل دوپراکس (Doprax) یک قابلیت فوق‌العاده جذاب در بخش
مارکت
داره که کار شما رو برای راه‌اندازی سرویس‌ها بی‌نهایت ساده کرده!
🔸
دیگه نیازی به درگیری با کدهای پیچیده، ترمینال و تنظیمات طولانی نیست؛ فقط با چند تا کلیک ساده می‌تونید هر اسکریپتی که نیاز دارید (مثل پنل معروف 3x-ui) رو در کمترین زمان روی سرورتون نصب کنید.
📝
مراحل نصب خودکار:
1️⃣
ورود به مارکت:
از منوی پنل، وارد بخش مارکت (App Market) بشید.
2️⃣
انتخاب اسکریپت:
از بین برنامه‌های موجود، اسکریپت دلخواهتون (مثلاً
3x-ui
) رو انتخاب کنید.
3️⃣
انتخاب سرور:
سروری که از قبل تو پنل ساختید و آماده کردید رو به عنوان مقصد مشخص کنید.
4️⃣
نصب با یک کلیک:
در نهایت فقط کافیه دکمه
Install
رو بزنید!
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کارهای لازم رو انجام میده و اسکریپت رو روی سرور شما نصب می‌کنه و اطلاعات ورود رو در اختیار شما قرار میده.
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPVVbY0db-OsAMTS9eOPEPNXs6NwyuIkzyce9R3owOutj0Z6s5aE1mBpeBLQ3EZM_F4jIKdb2A-n2Zv8KzYn_y8Ygz5I-pUJaqr2P5FTBA_unPBbdiYVWojfMoDjPG7DASKoCBAieCEQKGT8JrEW4KEQ8NtwCr8y4LdkAUmRKN6HVqr3LvnV9UL4J73WgGPrq_BquNu84JA3e2lE_ygout6OGKv2IX5CmmO_cIJ7-t7UITfudFVwI2ganCqxbFtieAPhxR3gyKkdCrFe0xt7gv3K80kbBVjIQYXbmIBNZ3jsltj6byRaCCvEDLT0ZCuL3hHVmrfYmgfxLfURq_ERCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل idontScanner | جعبه‌ابزار تست شبکه و TLS روی VPS
اگر مدیر سرور هستید یا می‌خواهید کیفیت اتصال، اختلالات شبکه و وضعیت پروتکل‌های امنیتی سرورتان را دقیق رصد کنید، پروژه متن‌باز
idontScanner
یک ابزار سبک، سلف‌هاستد و سریع برای همین کار است.
🔹
کالبدشکافی دقیق TLS & SNI:
تفکیک دقیق زمان‌های DNS ،TCP و TLS Handshake به‌همراه نمایش جزئیات گواهی SSL، نسخه پروتکل، Cipher و ALPN.
🔸
بررسی در دسترس بودن Endpoint برای لینک‌های VLESS ،VMess ،Trojan ،Shadowsocks ،Hysteria2 و WireGuard (بدون ذخیره افشای کلیدها و UUID).
🔹
سنجش لتنسی، جیتر و پاسخ‌دهی پلتفرم‌هایی مثل YouTube ،Instagram و Telegram مستقیماً از مبدا سرور.
🔸
دارای رابط کاربری روان به همراه منوی مدیریتی تحت ترمینال برای تغییر پورت، مشاهده لاگ‌ها، اتصال ربات تلگرام و آپدیت بدون از دست رفتن داده‌ها.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c25-yYd9EVy95w2Sf_RRH1Xo9A9032wrLad99-t_ib1hEJLl2TwfYT5eC7kjk_mt9w13NYx-JHb6kSTXeGs0DeN2QHu4e2nwVwh_dat-X9eSwgMM6BuK-M45e50JqgR6LwNoSQMV7z3D70entp23p73mxFvWlnJwd1aWHUeNAJnX5584HQCzeIhA0UGIQtGorcNtfChJHFKe9McGH5BWF95WknYs1J-k-VFOHZCnekwE0T6lT7QOgoHokeJpT7tvbQxxfntqJX6qXIClHESQtkrNYpU_NoJZMuIGyutnAJTqi1LYQP5nMzKOrsKn4DRHQkkNOpEU525OTKYRElMVUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اعتراف مدیرعامل زیرساخت: ۱۰ درصد ترافیک اینترنت کشور به استارلینک کوچ کرد؛ سهم 5G تقریباً صفر!
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، در نشست خبری خود از واقعیتی پرده برداشت که نشان‌دهنده شکست سیاست‌های محدودسازی اینترنت است: حدود ۱۰ درصد کل ترافیک کشور اکنون روی بستر اینترنت ماهواره‌ای استارلینک جابه‌جا می‌شود.
🔹
سهم ۱ ترابیت‌برثانیه‌ای استارلینک:
اکبری اعلام کرد با وجود بازگشت ۹۰ درصدی ترافیک، ۱۰ درصد باقی‌مانده دیگر به شبکه داخلی بازنگشته و جذب مسیرهای ماهواره‌ای غیررسمی شده است؛ حجمی که حتی از کل ترافیک برخی اپراتورهای داخلی فراتر است!
🔸
تداوم فعالیت ترمینال‌ها:
به گفته وی، استفاده از استارلینک به‌ویژه در دوران تنش‌ها و محدودیت‌ها جهش پیدا کرده و ترمینال‌های فعال‌شده همچنان آنلاین و در حال سرویس‌دهی باقی مانده‌اند.
🔹
سهم ۵G نزدیک به صفر:
در شرایطی که میانگین جهانی مصرف دیتا روی نسل پنجم به ۵۰ درصد رسیده، سهم ترافیک 5G در ایران تقریباً روی عدد صفر قفل شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLH2EMKq_5wxhbetN0dPeFaLUEq4N7BZJnTlxWAlKNH3nVLw3AV26kFQUupaE_FLT9PBE0QNEj6uyQM7pi2Z9xWLRzouQjF61iH8mUvTPUUtTgsKANEIpX_QsUqjnSBFMJZPYLFInczvmzYcAFl2xOqHKIsoWc-wR9YgBYTZ2Px3cHDMZxTT9yhmgEcadtTSAnCL1m33VnlqsZ1-xR2PKChNmGWu7OV__5fkd-EpkoRaPNSF4l6161sBeZZ3F-V1zQLEKcE0lRovcxc0xPvm2w5Qq2rg-SfKfEDniZ5-3hvCAE0q1BM1e7yvz8LPRNXjVIm6fKvjh3OYw4tIsTlLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های ترافیک IPv6 در کشور
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، پس از تذکر اخیر وزیر ارتباطات اعلام کرد که محدودیت‌های اعمال‌شده روی پروتکل
IPv6
برداشته شده و اپراتورها از امروز هیچ منعی برای استفاده از آن ندارند.
⚙️
جزئیات و نکات کلیدی خبر:
🔹
۹ ماه مسدودسازی بی‌دلیل:
ترافیک IPv6 که نقش مستقیمی در کاهش تاخیر (Latency)، پایداری شبکه و افزایش سرعت ارتباطات دارد، از دی‌ماه ۱۴۰۴ تا امروز دچار مسدودسازی و اختلال گسترده بود؛ محدودیتی که حتی خود وزارت ارتباطات هم مدعی است مصوبه قانونی مشخصی برای آن وجود نداشته است!
🔸
وضعیت ترافیک در کلودفلر رادار:
با وجود اعلام رسمی شرکت زیرساخت، داده‌های لحظه‌ای
Cloudflare Radar
هنوز تغییر محسوسی نشان نمی‌دهد و سهم ترافیک IPv6 ایران همچنان روی رقم ناچیز ۷ الی ۸ درصد ثابت مانده است. انتظار می‌رود در روزهای آینده با بازگشایی شبکه اپراتورها این سهم افزایش یابد.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An3iXYxuYWHW2GI0niaHZwA2OunwGGPP3tc45plb9gQwyufajn1FHhVzSlzsf04aNkMqhhjgjgYaQdt2CVqWVNbeBja6Efnq5mChcAPqAclF7AzWzXifbNeZEjaABW5fNdNSXiT2qLYzS06ZYGqzSjFbJyMbr26HTgBuLZ9FiQIrDkg4NrKARsq0lOlNqTVJeBKyrOtQrzmV2w4VwZskY7gSz0MJcap2wpE-IlQIXuqXzjVKvKSKVLfCPbz46e6UYaYZMZNehH5SMnrA2RRXJZnnilwjKfPsB40_VP2DdAIpEBb9PFewCCkaQMXFX0M5-dY5dn4O7GfpbQkVJBSyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی + پنل مدیریت و فروش «مشابه شکن»
🔹
تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم چطور یک سرویس رفع تحریم اختصاصی (شبیه به سایت معروف شکن) بسازید و با استفاده از یک پنل مدیریت حرفه‌ای، کاربران رو کنترل کنید، اکانت بسازید و به راحتی فروش داشته باشید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💬
راهنمای خرید سرور از هاستینگ هایی که معرفی میشه
رفقا سلام.
بعد از
هم‌فکری با شما
و بررسی نظرات خریدارها و فروشنده‌های عزیز، به یه جمع‌بندی نهایی رسیدیم. برای اینکه هیچ سوءتفاهمی پیش نیاد و همه چی کاملاً شفاف باشه، رعایت این موارد میتونه بسیار مفید باشه. این موارد قانون نیستن بلکه یک راهنما هستن برای اینکه شما با آگاهی کامل بتونید خرید کنید.
🔹
۱. ملاک قطعی سلامت آی‌پی:
تنها معیار سالم بودن سرور در زمان تحویل، موفق بودن تست پینگ و
باز بودن پورت SSH
از طریق سایت
Check Host
هستش، نه تست بین ده‌ها اپراتور کشور که هر کدوم فیلترینگ داخلی و محدودیت‌های خودشون رو دارن.
🔸
۲. داستان اپراتورها و فیلترینگ:
اگه سرور تو چک هاست اوکیه ولی روی نت شما (مثلاً ایرانسل) جواب نمیده یا بعد از چند روز آی‌پی مسدود میشه، این موضوع به خاطر فایروال‌ها هستش، نه خرابی سرورِ فروشنده.
🔹
۳. تعویض آی‌پی:
وقتی سرور با Check Host سالم تحویل داده شد، در صورت فیلتر شدن آی‌پی بعد از تحویلِ موفق (بعد از چند ساعت تا چند روز)، فروشنده تعهدی برای تعویض رایگان نداره و این ریسک در شرایط فعلی اینترنت پای خریداره.
🔸
۴. ارتباط سرور ایران به خارج:
سرورهای ایرانی که تهیه می‌کنید، باید ارتباط باز و بدون محدودیت با خارج (ترافیک بین‌الملل) داشته باشن.
🔹
۵. وضعیت پهنای باند و ترافیک:
فروشنده موظفه کاملاً شفاف بهتون اعلام کنه که پهنای باند سرور
«اختصاصی»
هستش یا
«اشتراکی»
. همچنین سقف دقیق مصرف منصفانه برای سرویس‌های اصطلاحاً "نامحدود" باید مشخص باشه.
🔸
۶. مرز پشتیبانی:
وظیفه هاستینگ تحویل سرور خامِ سالم با شبکه متصل هستش. نصب پنل، کانفیگ، ران کردن اسکریپت و رفع خطاهای نرم‌افزاری سمت سرور، به عهده خودتونه.
🟢
و اما یه نکته دوستانه و مهم:
— بچه‌ها، ما تو این کانال همیشه فیلترهای سخت‌گیرانه‌ای داشتیم و
فقط هاستینگ‌هایی رو معرفی می‌کنیم که دارای نماد اعتماد (اینماد) و سابقه مشخص هستن
. هدف ما ایجاد یه پل ارتباطی امن برای شماست. با این حال، وظیفه ما صرفاً «معرفی» هستش و صفر تا صد توافقات خرید و پشتیبانی، بین شما و فروشنده انجام میشه.
—
یادتون باشه هر هاستینگی ممکنه قوانین و شرایط فروش اختصاصی خودش رو داشته باشه که لزوماً صد در صد با موارد کلیِ بالا هم‌راستا نباشه.
پس حتماً قبل از نهایی کردن خرید، قوانین خود اون سایت رو مطالعه کنید و با آگاهی کامل خریدتون رو انجام بدید.
— چنانچه خدای نکرده مشکلی هم پیش اومد که نتونستید با فروشنده به توافق برسید، می‌تونید از طریق همون نماد اعتماد به صورت رسمی و قانونی شکایتتون رو ثبت و پیگیری کنید. این مسائل از دست و مسئولیت کانال ما خارجه.
🔻
امکان آپدیت در آینده وجود داره!
دمتون گرم که با آگاهی کامل خرید می‌کنید!
🌹</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB8LFv1aW5614flfdF44NWxd7cDYjZu3QOr4sc0ZaLtOSz3S7N8DJJblSA7giq1aDvijT7AhlMK0IGSKLCuGcIowVlpq0LnQr6wZr8JfYZsCCTrTc3-01cEgEwjbNeyCPs7uO_QpscI8h5gmKCdFYcBdGXTP6TBAlYbYmTQVhM_wMWzgSgq-aB8xSGFji-tQRGzaeOW39-5dC7ijQxXTLPX0t1ZQ3ty9CnQlyuLvT7jnQKt4FB2rz0g2bluJ2aoPnbzKxlbTYEc63hS_o0pOURC8ngyk0JwVUnc2Z8hYiluEGDa8s1vNMK6iT_iXyIX1ZUBicgR6XAEvz1RQMFoD5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی اوپن‌ای‌آی از ChatGPT Sites؛ طراحی و انتشار وب‌سایت تنها با پرامپت متنی
شرکت OpenAI قابلیت جدید
ChatGPT Sites
را به‌صورت بتای عمومی عرضه کرد؛ ابزاری که امکان تولید، ویرایش و میزبانی مستقیم وب‌سایت‌ها و وب‌اپلیکیشن‌های سبک را صرفاً بر اساس توضیحات متنی زبان طبیعی فراهم می‌کند.
💬
طراحی پرامپت‌محور (Sites@):
ساخت رابط‌های کاربری چندصفحه‌ای، داشبوردها، پورتال‌های درون‌سازمانی و ابزارهای تعاملی با ارسال متن، فایل‌ها و دیتاست‌ها
🚀
میزبانی و هاستینگ رایگان:
میزبانی خودکار وب‌سایت روی زیرساخت OpenAI، تولید لینک اختصاصی با قابلیت تعیین سطح دسترسی (خصوصی، سازمانی یا عمومی بدون نیاز به لاگین)
🧩
المان‌های تعاملی و شبه‌وب‌اپ:
پیاده‌سازی فرم‌ها، فیلترها، سیستم جست‌وجو، جداول داینامیک، نمودارها و سیستم احراز هویت اولیه
👥
همکاری تیمی (Collaboration):
امکان کار اشتراکی روی پروژه، اعمال تغییرات و به‌روزرسانی نسخه‌های منتشرشده با اعضای فضای کاری
📊
دسترسی:
دسترسی برای اکانت‌های Business، Enterprise، Pro، Pro Lite و Edu فعال شده و عرضه تدریجی آن برای کاربران پلن Plus نیز آغاز شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daIkYP9BO65w2bo83KVX3Il7NUQINNrPIl2PNIX-RfT_S47ZM-DM-Hkm1TAsvBQL7tdua96io09u9hOpZHrqL8TXUzmdux9sXl53K7Cw1V8t5aKnfLk_ZUSzRT2hPfjxpqhGc3kzxjgocIjQL56PktHVIWmBxfRYkkl-9SAvUVbmIcmccjw4iZjvfxk7GWmknYWh4msLjSrr99Tgbr2_-fMXxYcmaJg_EH19wtxYGrJsi1-rziRwjtdhXXTr9_bZLRtoHAny3n02DQSvekl9xzoKubvIlgdcmJYJpJosWMGKW-__Cx-xscWwrVN-hIrVZ8gLYC5RsarpffRA7lDBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
بکاپ خودکار از پنل‌های V2Ray و تحویل مستقیم در تلگرام با ابزار bkup
ابزار
bkup
یک سرویس سبک برای سرور است که در فواصل زمانی مشخص از دیتابیس پنل‌ها فول‌بکاپ می‌گیرد و فایل خروجی را مستقیماً به تلگرام می‌فرستد.
🔄
پشتیبانی از ۴ پنل:
اتصال به پنل‌های 3x-ui، HM Panel، PasarGuard و Rebecca با دکمه تست آنلاین اتصال.
📤
تحویل خودکار در تلگرام:
ارسال مستقیم فایل بکاپ به چت یا کانال بدون نیاز به دانلود دستی از سرور.
⏱️
زمان‌بندی دقیق:
تعیین فاصله بکاپ‌گیری بر حسب ثانیه، اجرا در قالب سرویس Systemd و فعال ماندن پس از ری‌بوت سرور.
🧩
ابزار Reassemble:
قابلیت چسباندن پارت‌های چندتکه بکاپ‌های حجیم ارسالی تلگرام در پنل وب و ساخت فایل کامل
💻
مدیریت وب و ترمینال:
دارای داشبورد گرافیکی با لاگ زنده، به‌همراه منوی ترمینالی برای آپدیت، حذف و تغییر پورت یا پسورد.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=mallpSE7qpmH2thEhKNhNCSUTTsaanTwYbL-nIgmtiflIQdzp_7eFToXY8V1zCruoABlj3hh1gPSdKR9o8eELM_f63om-U26aYRImlG0QeeLVY1WQyxxAvqw7CTppGhidItAHWVgNoudNo4nmTRl-MR4qqVeT8OwIOoakhDmd72DWrBu_oiAhPRwOBFSzNL0MqVEcjI0Oms7RtTsZoSgORu5xOBsy2U95y6xNqcaM2IQejZpDjNGB0F-5M_zkRAYJ88DjXenSswszRlVulRs2W59pjxdg8vD7NAn9A3iCilHPwhkJz4K1OJjyoDlIUBqnN3TdjvnHV-6pCRCVpGxLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=mallpSE7qpmH2thEhKNhNCSUTTsaanTwYbL-nIgmtiflIQdzp_7eFToXY8V1zCruoABlj3hh1gPSdKR9o8eELM_f63om-U26aYRImlG0QeeLVY1WQyxxAvqw7CTppGhidItAHWVgNoudNo4nmTRl-MR4qqVeT8OwIOoakhDmd72DWrBu_oiAhPRwOBFSzNL0MqVEcjI0Oms7RtTsZoSgORu5xOBsy2U95y6xNqcaM2IQejZpDjNGB0F-5M_zkRAYJ88DjXenSswszRlVulRs2W59pjxdg8vD7NAn9A3iCilHPwhkJz4K1OJjyoDlIUBqnN3TdjvnHV-6pCRCVpGxLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی اوپن‌ای‌آی از ChatGPT Images 2.5؛ تبدیل اسکچ ساده به تصاویر واقع‌گرایانه
اوپن‌ای‌آی نسخه جدید مدل تولید تصویر خود را با نام
Images 2.5
معرفی کرد؛ مدلی با نورپردازی طبیعی‌تر، بافت‌های غنی‌تر و بهبود چشمگیر در وفاداری به تصاویر مرجع و ویرایش‌های متوالی.
⚙️
امکانات و ویژگی‌های جدید:
✏️
قابلیت Sketch@:
امکان رسم طرح اولیه و نقاشی ساده داخل محیط چت برای تبدیل مستقیم آن به تصویر پرجزئیات نهایی
⚡️
کاهش ۵۰ درصدی تاخیر:
سرعت تولید و بازبینی تصاویر دو برابر سریع‌تر از نسخه Images 2.0
🎯
ویرایش موضعی پایدار:
تغییر دقیق بخش‌های مدنظر (مانند متن تبلیغاتی، پس‌زمینه یا سوژه) بدون دست‌خوردن هویت اصلی یا افت کیفیت در مراحل بعدی
📁
قالب‌های آماده (Templates):
تسهیل ساخت پوسترهای تبلیغاتی، تراکت‌ها و عکس‌های صنعتی محصول
این مدل برای تمام کاربران در وب، موبایل و دسکتاپ فعال شده است. برای توسعه‌دهندگان نیز در دو نسخه ارائه می‌شود:
Flare
(پیش‌فرض، سریع و کم‌تاخیر) و
Sunburst
(مخصوص خروجی‌های بسیار دقیق و سنگین).//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGz4XTRBGsmb_pY3ROW_mIvGPJHeF3d-w6Wp6TUzjO7QtFYPZRDWvwu5ugFjyMHmCNAzfDjE7mpHjLHEIJ_5WGCnKT6A0Q57LejNQ-RlqvqpI301nGAtHUi8LUyu_Jic3Q1hgyjjH5E3qXXHhdDbn6DAUCkdgyOcEw4kymNSKbfiMl4bzADPuSlCm4iyfOHlv5zjDnhwubQgy572BBUGkK6s5DHBHV8JQV9S2HTVqmVkc3NIq_nEEWpOTCYCtHqvVpXctrvP951-k4VVhmlz3w0BA1comXkb2SXRT8wYeMfRFNP2DJ8AjRokUD2x4s5gQEIeTbCCDrvl9j6vHx34EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای نقشه ذهنی کلیدهای میانبر کامپیوتر با کلید کنترل
🔸
این تصویر یک نقشه ذهنی از کلیدهای میانبر عمومی کامپیوتر است که هسته اصلی آن، کلید کنترل (Ctrl)، قرار گرفته.
🔹
هر شاخه شامل لیست‌های دقیق از کلیدهای ترکیبی و عملکردهای مربوطه است که به راحتی قابل درک و یادگیری است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=bbbm8iIYhCYVev7HVpVCPWo60SkO3nF83l01eyVljw_y5bRXMi7p3CwZYaFNTnAgNvEuQ3wFjpswKyfxkH1IW2MnNUb3MGN8BvYSUoz4JuRtrYwmjm21aQ8ffAiXZ0jPSm09dC4ExOEUNaxXNarOYj2JTIOLrWO1Ja8Zs1WAPjX0kJ_1UgHLNjzd6Fl1I1dYsVgpXFA-W7UExH3zYyV5qekIiZQKw0xl7zAfb_KMUs1CAo3MwWQJ2TojVJh7yuB7htlJ45kVKcIc52zjIliLfG-pk0Ac_oznwzqG3ZJEZbyR5--LQGZluMHr12yRoKIU81_WRi-sjGriPLYpVVMmaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=bbbm8iIYhCYVev7HVpVCPWo60SkO3nF83l01eyVljw_y5bRXMi7p3CwZYaFNTnAgNvEuQ3wFjpswKyfxkH1IW2MnNUb3MGN8BvYSUoz4JuRtrYwmjm21aQ8ffAiXZ0jPSm09dC4ExOEUNaxXNarOYj2JTIOLrWO1Ja8Zs1WAPjX0kJ_1UgHLNjzd6Fl1I1dYsVgpXFA-W7UExH3zYyV5qekIiZQKw0xl7zAfb_KMUs1CAo3MwWQJ2TojVJh7yuB7htlJ45kVKcIc52zjIliLfG-pk0Ac_oznwzqG3ZJEZbyR5--LQGZluMHr12yRoKIU81_WRi-sjGriPLYpVVMmaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره دهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mmdoo-yt، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFKJeImfBtzkfxMTHKiYFJ9tBR2gq8w3s7HBrEgkMa62_voCnjyxAK8Nk9bWeA_u6V3ipkeRpONKyORXYZsGQA6h5c6THBz7SZcFGpCnNBbtjoh8OxnYYp5gEvk4SVJHPhLJeQiR2UojHLnu8YSNnEunU6G_DQM3OiUF4NC-iymU5Ojtr_nPi-F8nXXdUeJHahj9HOYoRdCvx6kFkZIK6uEJiqGAh9ubZs2FNPf5BPE1XCKq4QhoZl2SE5nCq68cd5oGz9ilPzRzojeXXPd551bDG8l9qGeSuEkjn3uKHdeJa0ObXCmOadPSIYX08QkEx-jrKEta9oOdJ2y_NKn7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.12 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر بالا بیارید و با دوستان خودتون چت کنید.
👇🏻
تغییرات کلیدی سانگبرد (Songbird)
:
🐘
پشتیبانی از دیتابیس PostgreSQL
🪣
ذخیره‌سازی ابری روی آبجکت استوریج‌های سازگار با S3
📥
پشتیبانی کامل از استقرار به صورت PaaS یا CaaS (
دیپلوی آسان در Railway و Render
)
🎬
ورکر مستقل مدیا برای پردازش و تبدیل ویدیوها
📴
کارکرد چت در حالت آفلاین (صف‌بندی پیام‌ها و ارسال مجدد خودکار)
🛡
دسترسی اضطراری به پنل مدیریت
👥
عضویت خودکار کاربران جدید در چت‌های عمومی
📦
قابلیت Rollback (بازگشت به نسخه قبل) در اسکریپت نصب
👇🏻
بهبودها و رفع باگ‌ها:
🔸
استفاده از شناسه UUID برای کاربران، چت‌ها و پیام‌ها
🎨
بازطراحی رابط فهرست چت‌ها با تایپوگرافی بزرگ‌تر و ظاهر مدرن
🔧
ارتقای امنیت با رمزنگاری اختصاصی تامبنیل‌ها و فایل‌ها
🚪
رفع پرتاب کاربر به صفحه ورود در صورت قطعی موقت سرور یا اینترنت
🔗
داکیومنت پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lChMZZf83eU2Vu-rQy1yS1uxGJmBRRZ_PlePFGv-enQwds1gRgYTcRnO1JlXsolPh9tJqmE6qDawUyFR5vzbUH0PFNNRZlVdMjwfHJCmxknQBhxXBRmj-WjxfKda8b7DJkm2pRgnjuvUENvOXzN4lnRJ9--YOAokI5ZF6eVKoP59Hvo7WOB5Jw9UqPxA2LIT92BsreUkEXrdcOYpWkQ3biwjsqAO4q2Kg79Zisq1UepvQGI8jN43KlTwvhr1eosdB_lPk9zpobjymmO3ijJKptLp08ARBPfHeD9q7gGkRpEMS8ymoFbyqXzyZlTHFDQ6p4X5fNUokpBE-AQSXe3lIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازم داستان تکراری؛ اینترنت داغون، اما ادعاها برقرار!
🔹
از دیروز وضعیت اینترنت رسماً افتضاح شده؛ پکت‌لاس شدید، کندی اعصاب‌خردکن و قطعی‌های مداوم. بهزاد اکبری (مدیرعامل زیرساخت) هم طبق معمول اومده توییت زده که علت کندی «قطعی فیبر نوری در ارمنستان» بوده!
🔹
الانم ادعا می‌کنن مشکل حل شده، ولی در عمل کیفیت شبکه—مخصوصاً روی اینترنت موبایل—هنوزم افتضاحه و هیچ تغییری حس نمی‌شه.
✍🏻
جالبه که با یه قطعی سیم توی کشور همسایه کل اینترنت مملکت فلج می‌شه، ولی موقع افزایش قیمت بسته‌ها همه‌چیز سر جاشه و وزرا توی صف اول توجیه گرونی می‌ایستن! اول یه اینترنت پایدار و بدون قطعی تحویل بدید، بعد دم از گرون کردن تعرفه‌ها بزنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze86sTrV-GY320-aR_wbf_Ew00Te7FIGgojxj-L8khQcJnZtkIMV2-QMF3mC52Gqjxkg00ofRo9Ee9N-4LiQRpIqgZayKaexC9O2LoDMOuEfOfS59M7Vdnbwms0MyKAnewHgIeKh835Zc1pKiWYVtwn1nbnHPbykBdWcEfWlZyjHj_bfXXxbuGve9FF5-QycvLPoDt9d6HwcKJm9jJaEpljYgLOKuOiE85ZBfFAsD-jwSRg5V88SJGty2oB6Oa3hhqiOr81sSQg9-JITO0MLJMf7k-2lNwNqm2Cf4P5KdSxYlex5sxZCv9wzmPzXZHRSMlAWbg_jT-EnrQS2gGscbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
زنگ خطر امنیتی؛ لو رفتن دیتابیس حساس کاربران JumpJumpVPN
🔻
دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اگi از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns || ircfspace
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_2cCmGRObzTZmihs3ZsrUpiTbC4sk2SSSdM9GOKQGtjDBQOqPXyOtDPi1KJdBh6YeTKVTFzJuhjAGaXjrPyHKFID7_YJW_VJxLBN4bkZe8iSWho1ykHhOVq_DeXSaFBhEW7HSARO9FXv5kDOm1oUxkQ_TNHAolRM83gIFOA_zCOzKWCfE9utYb7biodaRPCbj0Ry5vVobAHgBSOe4-Cs0ttmQjhYF9W-HkSv6D8XVxRal7zo_nAo9rq9h9qJeFKAOHX8Ii4heX_zebUL3RoITCyBGnbj6Iah6gov4d9rCFj8cg3yqbLPKZq9QGj8U5HUyAHu0Va2NKlTvXamkMm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بروزرسانی جدید برای نسخه اندروید oblivion منتشر شد
🔹
فیلترشکن رایگان
oblivion
به صورت اوپن سورس و امن برای اندروید توسعه داده میشه و میتونید ازش استفاده کنید.
🔸
هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
🔗
دانلود از گیت هاب
#فیلترشکن
#oblivion
#رایگان
برای دور زدن فیلترینگ و آموزش کامپیوتر و تکنولوژی و... ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SoftEther Code -- @iAghapour.txt</div>
  <div class="tg-doc-extra">3 KB</div>
</div>
<a href="https://t.me/iaghapour/2983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci0NzLTb10Ly6UxuuoyFyTipIvknK8EnEFPB-FJpxppGw7akQsA4IumzIkErVUyoOVU1bJvuyYrz1qhOe0wMrMrIHLvWS7Z9YJiiFfIsDt_UpwGr1v6dhuTHKOTyZIm0vuV7TXLs4XhZ4IoevjwYtbIDfm5PGLRoPmKIv3m_1b2J_wo-vTN8stWv6ufy9NL84bMgx9BFJhelaef9duNZ7EN5UNzaDXA3HNnskcXodLTpAtrak2BljHdqEkG1fAagW88RF8J_VIvc-Keyk9eZ7OOy6Drmgdzg01AOqy5dZLRi3gTWjIjEzSnPKnJnhyaBHrY56WF7auRvALVGQzqw8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🚀
🔹
توی این ویدیو قدم‌به‌قدم بهتون یاد می‌دم چطور سرور SoftEther رو به همراه یک پنل تحت وب اختصاصی راه‌اندازی کنید. این پنل قابلیت‌های زیادی مثل مدیریت کاربران، اعمال محدودیت حجم و امکان استفاده از پروتکل‌های مختلف رو در اختیارتون قرار میده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#سافت_اتر
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCAL7GrS1Kt0MWr6mO6yoWFSXBlp8MhyUGlxp7ec2Q-mIj6A3yMg9v8NoHakiXsqNulG-mpxvju8X6Alp0kVr5GkM5N0wI5KiR9zSHvxOTs9VNjOA4aL7qIBk9zIOrI5RRodu5QSHJVt8XhaNGFTIbuldX1iZyncajlekfomuXg8eb_jQRFQR6QWe_iicWG9OpScopAbXInFeAVapzn75nbwr-F6tSYo1aqDLIfePpTOV0vGPhzQh_OSIJjk-DlH0Nt7Fd9L1U5sxo93kBa9cz8x3FV1Ib-FRCXhVaWlAaB4JkmxS94sWSiT5P7GgC_2DJDxqOjUugWehYYBn2PuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی EMS IPAM؛ سامانه مدیریت آدرس‌های IP و تجهیزات شبکه
اگر برای مدیریت ساب‌نت‌ها، رادیوهای وایرلس و تجهیزات شعب مختلف هنوز از اکسل استفاده می‌کنید، ابزار
EMS IPAM
یک پنل متمرکز و گرافیکی برای سامان‌دهی و مستندسازی شبکه است.
🔹
مدیریت ساختاریافته IP:
پشتیبانی از رنج‌های /16 تا /32، جلوگیری خودکار از تداخل ساب‌نت‌ها و نمایش ظرفیت آزاد/مصرف‌شده.
🔸
مستندسازی شعب و تجهیزات:
ثبت موقعیت شعب، پورت‌ها، توپولوژی و ذخیره راه‌های دسترسی سریع (WinBox، SSH، RDP و وب).
🔹
پایش مستقیم میکروتیک:
اتصال به RouterOS از طریق API و نمایش زنده وضعیت اتصال، سیگنال و پهنای‌باند رادیوهای وایرلس.
🔸
کلاینت ویندوز:
باز کردن مستقیم نرم‌افزارهای مدیریتی (مانند WinBox) با یک کلیک از داخل پنل بدون درج رمز در مرورگر.
🔹
تعیین سطوح دسترسی، ایمپورت/اکسپورت ساب‌نت‌ها و پشتیبان‌گیری خودکار.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbs2MtPObSl1GX2iPElDJxxCnS2GcYpkNEh2xeKF-dVk6U06lKyFBn5qQ7Xd1LfbXS8MSSc0_91m_PgZk727UxXQmyxPriDtd14ta2PLjPVPYvcUJ4Ayhw8o_k2YsBJumRBavoBMeMBUKXR46rCDY5HDHRXC8GYBkObcDI_5Gx5AhkjA5ti1R_OXwqBaBvI9HsSZ4dR_xIBXrOl1W1k_RsC_EPReGqhSasvRdtvidVNIywaCQiCIZQQO62oKGx9-XfMmHVLqOFNhxyEsFnb-0bD0rlqcDprifLDxIgfCOLCKdo4iXsNV3-6Qus6x5a62yCR2aaKrUftM8ofhJC6Q2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نرم‌افزارها در پس‌زمینه سیستم شما چه می‌کنند؟ کنترل کامل ترافیک با فایروال متن‌باز Portmaster
اگر زیاد اهل تست و نصب نرم‌افزارهای مختلف هستید یا نگرانید برنامه‌ها دور از چشم شما تله‌متری و اطلاعات به سرورهای ناشناس بفرستند، ابزار
Portmaster
دقیقاً همان لایه محافظتی مورد نیاز شماست.
⚙️
قابلیت‌های کاربردی و مهم:
🔹
دیده‌بانی زنده اتصالات:
نمایش شفاف و لحظه‌ای اینکه هر برنامه دقیقاً با چه IP، سرور، در چه ساعتی و از چه طریقی ارتباط برقرار کرده است.
🔹
مسدودسازی هوشمند ترافیک:
امکان بستن ترافیک‌های مشکوک، ردیاب‌ها (Trackers) یا تبلیغات به‌صورت موقت یا دائمی با یک کلیک.
🔹
ایزوله‌سازی آفلاین:
امکان قطع کامل دسترسی به اینترنت برای یک برنامه خاص تا صرفاً به‌شکل لوکال و آفلاین اجرا شود.
📥
دانلود از وب‌سایت رسمی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyotwUB9wwgTQ9fmyHww69AAbnDn8i9yq4Txc0oJzCktokXCiebcAkfT-HWU70n9LcPS-K55x3zzlxwedil9uEsNvmFyT2abWZZUc1X6LlfuTaqmBPuBqX7rtX17HzFPP8Vj_jOOwE1_MhT3yBWwToRhazAnH2-Qw_JG5a3zvAo9v0Q4WCWprbpiIdfy32JDw6Xdi2zZmUt_FeOfE4l2Xw_fvb7Yy6rZ3zVz6GCQ_MCCppSZlGxXvbPkK4rlRXRjXlpMmHd6XDtnu7-jWM_Xd8zhd5xgQZceUSfzYid3yfuuMeKEy2xCDsUP9XUGpHWOJ2Z-seSISzhcILCfDe3lfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی از «آیزا»؛ دومین آنتی‌ویروس بومی مبتنی بر شبکه ملی اطلاعات
دومین آنتی‌ویروس بومی کشور با نام
«آیزا» (Ayyza)
رونمایی شد؛ سامانه‌ای امنیتی که با تکیه بر هوش مصنوعی و ساختار شبکه ملی اطلاعات، امکان شناسایی تهدیدات و دریافت آپدیت‌ها را بدون وابستگی دائم به اینترنت بین‌الملل فراهم می‌کند.
🔹
موتور تشخیص هوش مصنوعی و سطح کرنل:
توسعه انجین اختصاصی مبتنی بر یادگیری ماشین و بهره‌گیری از فناوری‌های سطح هسته ویندوز (Kernel-level) جهت پایش دقیق‌تر، واکنش سریع‌تر و بهینه‌سازی مصرف رم و پردازنده.
🔹
عدم وابستگی به اینترنت جهانی:
قابلیت آپدیت به‌صورت آفلاین و انتقال داده‌ها و امضاهای امنیتی از طریق بستر شبکه ملی اطلاعات (اینترانت داخلی).
😁
🔹
اکوسیستم امنیتی یکپارچه:
ترکیب فناوری‌های EDR و XDR برای شناسایی حملات چندگامی و روز صفر، در کنار هماهنگی با سیستم‌های جلوگیری از نشت اطلاعات و مدیریت دسترسی‌های ویژه (PAM).
✍🏻
حواستون باشه قبل نصب با آنتی ویروس معتبر مثل کاسپر اسکن کنید آیزا رو :) تازه با اینترنت داخلی هم کار میکنه :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=piZFk03t_KszQVqaJGyVJNPnXVbsGzHKM7-u3b8xbp-6Eo8JCdzWxkfw9Ki07ojAMAAMt5Ute3QOuh0mN_Fm0n2MuWfwzWMRTQ4iklsPaR052-UItnxSPwwk_NvXEje1FrQv5ZKNMhw0mcjjvUNgwQSSTtiWwilfKaLxvGbbmjoi1YfncH37BGJK1SjZFWPC5VxS56tBvYZIUultlJvGrJH9U4_Q4gZCHUOND3idY2bN_wOwcVzFJvsIHupDzJokba7_TNpGjneITk0jx1QPLOMEHDHHt9V7UNQ0r7gbEj_xoXVxyVFukr_4-AQggGjXO-4GC-HIpHXbHTRO6NhZqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=piZFk03t_KszQVqaJGyVJNPnXVbsGzHKM7-u3b8xbp-6Eo8JCdzWxkfw9Ki07ojAMAAMt5Ute3QOuh0mN_Fm0n2MuWfwzWMRTQ4iklsPaR052-UItnxSPwwk_NvXEje1FrQv5ZKNMhw0mcjjvUNgwQSSTtiWwilfKaLxvGbbmjoi1YfncH37BGJK1SjZFWPC5VxS56tBvYZIUultlJvGrJH9U4_Q4gZCHUOND3idY2bN_wOwcVzFJvsIHupDzJokba7_TNpGjneITk0jx1QPLOMEHDHHt9V7UNQ0r7gbEj_xoXVxyVFukr_4-AQggGjXO-4GC-HIpHXbHTRO6NhZqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره هشتم و نهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
برنده عزیز با آیدی AhvanSalehi-f3r، مبارکتون باشه!
✨
👤
برنده عزیز با آیدی abolfazlghasemi1-q7t، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxuQQ4PuZItSvNlfD6hjWNBQF1dbc6anpg4gikpIBrumV9YqmvfWyOoR_uObyxAPfOvzzYDbn67Ay7Z_CrVvSyimWzJx5QhDrTbNyTwM7w3XOaRbywfuoZCoQawIN3a-VAKrj61LWQiAcC7-73gJJbsgVeE2hznOb4auGb7cRcLaHB6GdumBVzq-_lYSHaZmYzflQlWYOZVi8gZXyJ3jFAc6w5FtpwRC36GPa9asMshbOTulErHbVT0JRBhTfdM4kPgzCVQ2VIqvmrqZ0jVEt07hfuyIv0Q2Hbs3V0jabeosurOI7WArIfb8HgWoUUtqsj4YBvb3ETnZ_x4h5GUE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
وقتی خودتونم توی پلتفرم داخلی دووم نیاوردید!
🔹
سال‌ها اینترنت رو بستن و با فیلترینگ شدید خواستن مردمو به‌زور بفرستن سمت پلتفرم‌های داخلی، کلی هم بودجه خرج کردن و هر روز گفتن حمایت از پیام‌رسان بومی!
🔸
حالا بعد از این‌همه وقت، ستاد فضای مجازی خودشون جلسه گذاشته و گفته ممنوعیت حضور ارگان‌های دولتی توی پیام‌رسان‌های خارجی رو برداشتم، اسمش رو هم گذاشتن «پایان یک خودتحریمی عجیب»!
🔻
جالب اینجاست که می‌گن: «برمی‌گردیم همون‌جایی که مردم هستند». خب اگه مردم اونجان و خودتونم فهمیدید بستن این پلتفرم‌ها جواب نمی‌ده، چرا باید برای ارگان‌های دولتی آزاد باشه و پیج بزنن، ولی همون مردم برای باز کردن یه اپلیکیشن عادی هر ماه پول فیلترشکن بدن و با قطعی سر و کله بزنن؟!
این یعنی همون یک‌بام‌ودوهوای همیشگی؛ خودشون توی اپ‌های داخلی دووم نیاوردن و برگشتن، ولی زحمت و تاوان فیلترینگش هنوز رو دوش مردمه.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.
گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به هر دلیلی آی‌پی روی یه اپراتور مثل ایرانسل دچار اختلال یا مسدودی میشه، پیام میده که «سرورتون خرابه، بیاید رایگان آی‌پی رو عوض کنید.
واقعیت اینه که این روال، نه از نظر فنی درسته و نه منطقی
.
🔹
تست اولیه حق شماست:
وقتی سروری رو تحویل می‌گیرید، همون ساعات اول کامل تستش کنید. اگه دیدید همون بدو تحویل روی اپراتور مدنظرتون پینگ نمیده یا دسترسی نداره، کاملاً حق دارید به پشتیبانی پیام بدید، درخواست بررسی کنید یا حتی طبق قوانین هاستینگ سرویس رو عودت بدید. این حق کاملاً منطقی و محفوظه.
🔸
تفاوت خرابی سرور با محدودیت اپراتور:
وقتی سرور روشن و سالمه و روی بقیه شبکه‌ها یا اینترنت جهانی کار می‌کنه، یعنی سیستم مشکلی نداره. مسدود شدن آی‌پی بعد از چند روز کارکرد، ناشی از حساسیت فایروال اپراتور روی ترافیک عبوریه، نه نقص فنی سرور.
🔻
ارزش منابع:
آدرس IPv4 منبع محدودی در کل دنیاست و هزینه جداگونه داره. هیچ مجموعه‌ای نمی‌تونه آی‌پی‌های سالمش رو به خاطر مسدود شدن‌های بعد از استفاده، پشت سر هم و رایگان بسوزونه و جایگزین کنه.
👈🏻
ریسک اختلال روی شبکه‌های مختلف توی این بستر وجود داره و همه ازش باخبریم. بهتره با آگاهی از این شرایط خرید کنیم، تست‌های لازم رو همون ابتدای کار انجام بدیم، و اگر بعد از چند روز استفاده آی‌پی دچار محدودیت شد، مسئولیت این ریسک رو به پای خرابی سرور یا کم‌کاری ارائه‌دهنده نذاریم.
🟢
در همین راستا و برای حفظ حقوق شما، از امروز تمام ارائه‌دهندگان سرور که در کانال ما تبلیغ می‌شن، ملزم هستند تا ۱۲ ساعت بعد از خرید، امکان عودت سرویس یا تعویض آی‌پی رو در صورت وجود مشکل برای کاربر فراهم کنن.
بنابراین حتماً به محض تحویل سرور، تست‌هاتون رو انجام بدید تا در صورت وجود هر مشکلی، بتونید توی این بازه از این ضمانت استفاده کنید.
// قوانین در حال بروزرسانی و قابل تغییر هستش.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHNDeiCgSAxKI_ad7pQ5Wm3vHlZitDOsVru8Rum7rRx_a_QJcBeRn42trRDmjN402cIbDrLbmQZpjVmo6d_MwbYAXTAVxXyH1dj1n9Y1FSGbLwOdEib6I6mTcZwXf45JdR6YOAfeSG_CcGaHVrwyDVcVou6kOeSYGHmtAnE3hGp4-jBtpNiCvi0Nuj3wEZbRmKeojkVZBc_mRjfhBMFDTlSqb0Vwam8vV1KBLW4sm6khQt5PSakVJxJKxgxeSBpLM9SlwZvLZ_O6jAL6d3WqV1eGtihU9bHiom28it-WFSSoqcRMSwqaLNp37qYjcOPh56EJcZXLRCGHJJ1pAPg_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
شکست قفل Denuvo بازی Mortal Kombat 1 و قدرت‌نمایی هکر Voices38
قفل امنیتی جنجالی
Denuvo
روی بازی پرطرفدار
Mortal Kombat 1
بالاخره پس از گذشت حدود سه سال توسط کرکر سرشناس موسوم به
Voices38
شکسته شد.
⚙️
چرا جامعه گیمینگ می‌گوید دنوو به سخره گرفته شده؟
🔹
طوفان کرک در ۲۴ ساعت:
هکر Voices38 نه‌تنها Mortal Kombat 1، بلکه در یک روز ۵ بازی سنگین و مجهز به دنوو از جمله
Persona 3 Reload
،
Star Wars Outlaws
،
Metal Gear Solid V: Complete
و
Prince of Persia: The Lost Crown
را کرک و منتشر کرد!
🔹
جانشین بی‌حاشیه دوران پس از EMPRESS:
برخلاف رفتارهای پرحاشیه و بیانیه‌های طولانی کرکرهای سابق، Voices38 صرفاً روی بایپس و حذف اجراییِ قفل در زمان کوتاه تمرکز کرده و عملاً انحصار دنوو را در سال جاری به چالش کشیده است.
🔹
آزادسازی منابع سیستم:
بازی‌های مجهز به قفل دنوو همواره به‌دلیل ایجاد لکنت، افزایش استهلاک پردازنده و افت فریم مورد انتقاد گیمرها بوده‌اند و حذف کامل این لایه محافظتی معمولاً به بهبود روانی اجرای بازی کمک می‌کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmoPefrxYdTt9scmFPkNG2CO8xjCAPp5fumzkhd4z5VDfiL8nsCV1Cvf753AKvufV_hIhFgiRTCrQQH7ERiVtgRCOFO9YCnKogkWg30mx01F89a6NrahQ7nqmtIx24KhtnOL9E8CmARKlQxN0hU1DZuIbONms-wFSWX3AM4mxkkOGJrXkktbeQM3pl1BeqzQ5x9x-zU4ARpkecZ7LBAm7FZig521vabgx7U-ibRfppSukfJ34LQonfbkmfMlmX9oAtA5WtD72wW3l1pM54WKybgetDh3eRvuvUK0bKxeg0KFJE9ol1O9IkaaKlL1UnBFj6CVA7z2xYVDCSG92d8c2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بهترین پنل وایرگارد همراه با مدیریت حرفه‌ای کاربران + تانل
🚀
🔹
تو این آموزش بهتون یاد می‌دم چطور یک پنل جامع و سبک برای وایرگارد نصب کنید که هم امکان تعریف و مدیریت دقیق کاربران رو بهتون میده و هم قابلیت تانل زدن پایدار بین سرورها رو به ساده‌ترین شکل ممکن فراهم می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم قرعه‌کشی اکانت هوش مصنوعی داره و فقط تا فردا فرصت دارید! (شرایط: فقط قرار دادن کامنت زیر همین ویدیو).
👈🏻
قرعه‌کشی این ویدیو و ویدیوی قبلی با هم انجام می‌شه.
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djQSB27CmomCIbeis0pPSn-_-gYPuI_ISAYbq43dFLazrKCyl_XhEB6eYfJ5tvcTnzeHzEsAzW-R7bzpaxEnNz8u89eCCnfuhZk1VH_YMNZvPBaXcpcI0DcX6oTodxlBg9CS2UyvJMt3sON-JljV9XIO2jGlDI1a5t__Fc1i4Sg2-Nng0hjI3MiaN0LdcBMhJAyRSqwxqe9WD2HY-FKD5hPEpcFHfPckaMG7hhTKRT6dhbi99Gijri9NL3JEeAvHPaLcPN7qvRcTVJz0GMWMeNQeGqA9KdcAtbROfkgU4a5z4_f0Z1aQwPk3c8DGLLTPrj8GT2VUbpMKGqWeldcofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مایکروسافت از Project Zenith رونمایی کرد؛ نسخه‌ای اختصاصی برای توسعه‌دهندگان
مایکروسافت پروژه جدیدی با نام
Project Zenith
معرفی کرد؛ نسخه‌ای بهینه‌سازی‌شده، مینیمال و «آماده کدنویسی» از ویندوز ۱۱ که بخش‌های اضافی و نرم‌افزارهای غیرضروری را حذف کرده و تجربه‌ای نزدیک به لینوکس برای برنامه‌نویسان فراهم می‌سازد.
🔹
تمرکز ویژه بر هوش مصنوعی محلی
:
امکان اجرای مدل‌های زبانی محلی با بیش از ۳۰ میلیارد پارامتر (+30B) بدون محدودیت و افت کارایی.
🔹
پیش‌نیاز سخت‌افزاری سنگین:
طراحی‌شده برای سیستم‌های قدرتمند توسعه با حداقل
۶۴ گیگابایت حافظه رم
و پهنای‌باند بسیار بالای حافظه؛ نخستین بار روی مینی‌دسکتاپ Ryzen AI Halo شرکت AMD عرضه می‌شود.
🔹
بهینه‌سازی محیط برای کدنویسی:
نصب پیش‌فرض محیط‌های اجرایی (Runtimes)، ابزارهای ضروری برنامه‌نویسی و اعمال تنظیمات پیش‌فرض مناسب توسعه‌دهندگان.
⚠️
با وجود استقبال برنامه‌نویسان از یک ویندوز خلوت و بهینه، محدود شدن این نسخه به سخت‌افزارهای گران‌قیمت ۶۴ گیگابایت رم در بحران فعلی بازار حافظه، دسترسی بخش زیادی از توسعه‌دهندگان مستقل را با چالش مواجه کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=QOm33sezic35ZcRDxKOsl0UeTLdlou_ICZSXM7YNBftJnWHkY3ECSAOHtRNNOtudFV1JHN4WpcgrFVVBFXHPI29Iy67aOwNC5-CLXf8zPoi4Jkk6kvPu229yJbE-ibGsRnaZqmoGOgfqcoSaoL1j9fUQKp8GRF-cjByZVfNaU091GIJdXaLkck4whfNCQtbdD4CpfmQLgVI9HO0qi1M0CLP7lPUVDIZI_bAAn-BCxL-reAVCAHaeapA8UnSZmN6VtSU--whiXDqImswHPGcAq3_L2cQ-weGZke0yczdeEHqabTpJAHee80Qi53uELqwR9B3JzwQAq55OEG4WOwK7HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=QOm33sezic35ZcRDxKOsl0UeTLdlou_ICZSXM7YNBftJnWHkY3ECSAOHtRNNOtudFV1JHN4WpcgrFVVBFXHPI29Iy67aOwNC5-CLXf8zPoi4Jkk6kvPu229yJbE-ibGsRnaZqmoGOgfqcoSaoL1j9fUQKp8GRF-cjByZVfNaU091GIJdXaLkck4whfNCQtbdD4CpfmQLgVI9HO0qi1M0CLP7lPUVDIZI_bAAn-BCxL-reAVCAHaeapA8UnSZmN6VtSU--whiXDqImswHPGcAq3_L2cQ-weGZke0yczdeEHqabTpJAHee80Qi53uELqwR9B3JzwQAq55OEG4WOwK7HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی مایکروسافت از MAI-Image-2.6-Flash؛ تولید ارزان و سریع تصویر
مایکروسافت نسخه سبک و کم‌هزینه مدل تولید تصویر خود را با نام
MAI-Image-2.6-Flash
از طریق پلتفرم Microsoft Foundry در دسترس توسعه‌دهندگان قرار داد.
⚙️
ویژگی‌های کلیدی:
🔹
سرعت بالا و صرفه اقتصادی:
۲.۸ برابر سریع‌تر از GPT-Image-2-Medium و با ۷۲ درصد کارایی بالاتر؛ ایده‌آل برای اتوماسیون و ابزارهای تعاملی پرمصرف.
🔹
ویرایش نقطه‌ای:
اصلاح دقیق اشیا، نوشته‌ها و چیدمان بدون تغییر در سایر بخش‌های تصویر.
🔹
ثبات کاراکتر و محصول:
امکان بارگذاری حداکثر ۵ تصویر مرجع برای حفظ یکپارچگی چهره و کالا در خروجی‌های مختلف.
🔹
اتصال به وب:
ارتباط مستقیم با موتور جستجوی بینگ برای رندر دقیق سوژه‌های واقعی.
💰
هزینه خروجی تصویری:
۱۹ دلار به‌ازای هر میلیون توکن (در برابر ۳۸ دلار برای نسخه پایه 2.6).
هر دو مدل هم‌اکنون در مرحله پیش‌نمایش عمومی در دسترس هستند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTtTSUbHUr9CRuv2D5MgMz3fD91Ongoe5JLUgMtEvf2Hm5ao4YnwBjczvPm69U4wgt-ZsmHgombj9tiN26FWr5CzWsOWV0_sJTBBv3oO1fP2Hq5BvB7_6otJZVN5w6AbkGp6ofPiyEA8nRBIE2tDVOcz4EjWrd2FgPh_yJ-ZaammQgCV-iIELeuJ3Z7cucY4pNCI8jvWCSN68jqSkLfj_BN0K9Vogvr8XNmP0NqsTqNR3EMdYXNKvLN8LZFUxm6K3HRftX0VPqt5PUymg-4C0S7TTS7mSkpubcTV8LELOz-TJoCOGtOMNAugVsOGNL82-F16-Pb4NtbOEqFex3jBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل «زاگرس» (Zagros)؛ فورک چندهسته‌ای مرزبان
پروژه
Zagros
یک فورک از مرزبان است که محدودیت تک‌هسته‌ای را برطرف کرده و به شما امکان می‌دهد تمام هسته‌های معروف VPN را هم‌زمان روی یک سرور و نودهای مختلف مدیریت کنید.
⚙️
هسته‌های تحت پوشش:
🔹
هسته
Xray:
پروتکل‌های VLESS، VMess، Trojan و Shadowsocks
🔹
هسته
sing-box:
پروتکل‌های Hysteria2 و TUIC v5
🔹
سایر هسته‌ها:
WireGuard، OpenVPN، SoftEther، SSH Tunnel و PPTP
🚀
ویژگی‌های کلیدی:
🔹
اکانتینگ یکپارچه:
اعمال سهمیه حجم و محدودیت تعداد دستگاه متصل به‌صورت سراسری روی همه هسته‌ها و نودها
🔹
کلاستر نودها:
اتصال امن نودها با تایید Fingerprint و مدیریت هسته‌های مجزا برای هر نود
🔗
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🧠
رونمایی اوپن‌ای‌آی از پرچمدار GPT-6 Astra؛ ادعای ورود رسمی به «عصر AGI» و انقلاب در کار با کامپیوتر
اوپن‌ای‌آی با رونمایی رسمی از مدل پرچمدار
GPT-6 Astra
، آن را جهشی نسلی در حوزه‌های امنیت سایبری، برنامه‌نویسی و تعامل مستقل با سیستم‌ها نامید؛ تا جایی که گرگ براکمن صراحتاً اعلام کرد:
«به عصر AGI خوش آمدید»
.
⚙️
ویژگی‌ها و قابلیت‌های محوری GPT-6 Astra:
🔹
توانایی عامل‌محور و کار با کامپیوتر:
این مدل بدون نیاز به رابط‌ها و APIهای پیچیده، مانند یک کاربر انسانی با موس، کیبورد و صفحه تصویر کار می‌کند؛ فرم‌ها را پر می‌کند، رکوردهای CRM را تغییر می‌دهد، نرم‌افزارهای مهندسی (KiCad/FreeCAD) را اجرا کرده و کدبیس‌های پیچیده را مدیریت می‌کند.
🔹
سرعت و بنچمارک‌های خیره‌کننده:
🔸
در تست OSWorld 2.0 امتیاز
۷۲.۶٪
را با سرعت حدوداً
۴۷ درصد بیشتر
از GPT-5.6 به ثبت رسانده است.
🔸
ثبت امتیاز
۹۸.۶٪ در آزمون معتبر تعمیم‌پذیری ARC-AGI-3
و امتیاز ۱۰۰٪ در بنچمارک ExploitBench.
🔹
جهش آموزشی با زیرساخت Stargate:
نخستین مدلی که با بیش از ۱۰۰٬۰۰۰ واحد پردازشی آموزش دیده و برای اولین بار، مدل‌های نسل قبل به صورت خودکار بخش اعظم نظارت بر آموزش آن را بر عهده داشته‌اند (حرکت به سمت خودبهبودی بازگشتی).
⚠️
ابهامات و حواشی مهم پیرامون رونمایی:
🔹
غیبت بنچمارک اقتصادی GDPval:
در گزارش‌های منتشرشده، نتایج آزمون GDPval (سنجش کارهای واقعی بازار کار و اقتصاد) دیده نمی‌شود که این امر تحلیل دقیق بازدهی سازمانی آن را فعلاً با شکاف روبه‌رو کرده است.
🔹
سایه بحران‌های امنیتی پیشین:
این رونمایی پس از حادثه جنجالی نفوذ یک مدل داخلی و منتشرنشده اوپن‌ای‌آی به هاگینگ‌فیس انجام شده و مدیران شرکت بر حفظ لایه‌های نظارتی سخت‌گیرانه روی ایمنی Astra تاکید دارند.
🔹
عرضه:
دسترسی سازمانی برای بخش امنیت سایبری از امروز آغاز شده و طی روزهای آینده برای کاربران Plus، Pro و Enterprise فعال خواهد شد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4hXVfIynm7dCxML7vWjKNyoQqGKod0KzGTyMov5A1pgIMXeK5M61XSizgWK0fGfErgrL9JGQZoGiNH_Rg5dyMe_t1xQtD3qhC3I4HHW0EprnA4LVoOcCXCMCnDyyXkjT4JhhlV6E3S1o5iCHSgCy8V9uSXtPA4njMyT2FgZpiJUsm0QOow8jqCKrwJcqGD6ZWngsCm5rl2_puR0jDUdHHOy9NhA_QGCfohY6eqtXfg7aVv2C08aYoKPpk0HTPyO_0FKoNzLICFvBhpeSTljsPojXP456cRW8S93lTrvXMzFgy73ZYb9ToT8LyZC29DXRx1c50DeMl-Rn-MjpotppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏛
مخالفت زاکربرگ با طرح نظارت بر هوش مصنوعی در گفتگوی محرمانه با ترامپ
به گزارش نشریه
Politico
، مارک زاکربرگ، مدیرعامل متا، در یک تماس تلفنی خصوصی با دونالد ترامپ با پیشنهاد ایجاد یک نهاد نظارتی ملی و فدرال برای هوش مصنوعی به مخالفت پرداخته است.
⚙️
محورها و جزئیات کلیدی خبر:
🔹
پیشنهاد نظارتی به سبک FINRA:
این طرح که با حمایت دمیس هاسابیس (مدیرعامل گوگل دیپ‌مایند) و برخی مشاوران ارشد کاخ سفید مطرح شده، به دنبال ایجاد یک نهاد شبه‌مستقل ناظر (مشابه FINRA در بازار مالی) است تا مدل‌های پیشرفته هوش مصنوعی را پیش از عرضه عمومی، از نظر خطرات امنیتی و فنی ارزیابی و آزمایش کند.
🔹
موضع زاکربرگ:
مدیرعامل متا در گفتگوی ماه اوت خود با ترامپ تاکید کرده که هرگونه ساختار نظارتی باید با رویکرد «مداخله حداقلی (Light-touch)» دولت همسو باشد تا مانع رشد نوآوری و سرعت شرکت‌های فناوری آمریکایی نشود.
🔹
دو‌راهی دولت ترامپ:
کاخ سفید در حال حاضر بین دو گزینه مردد است: پذیرش مدل نظارتی مشابه FINRA یا انتخاب رویکرد صنعت‌محور و پیشنهادی دیوید ساکس (David Sacks) با حداقل سخت‌گیری دولتی.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVs6FZanhCslf345JHrnqddkQsMJ2WN0d-27UCfcF0ieVJpRK7zJZcN8GdFBTX-o7p7dYB0RlP-m_sZD_epkP2ge3q9S41WT0HmyAdGBu-kVWH2qMpK9DzGfN6wVzc7CAMGTGEyjiwQ4iMtGfI8VaFU61uaCiQm28--qsNauaG-CqxOfMgeLX_dOFNSSCe6sI_Be049lbvVWq3vf93sexLOWqNZ9cAnrZflPd28Sl5PZV7zd-eMV2tQE7mieJSTyg3tXapygD4r-WOXAtFUV5So4ixkf1gbaNqHJifSMwEtbZlWZ_fwUWg9RlWSqp0ibKpSHjotw1W0BtLsxX_bkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
خاموشی هم‌زمان چت‌جی‌پی‌تی، گراک و کلاد
سه چت‌بات بزرگ و محبوب دنیای هوش مصنوعی شامل
ChatGPT
(اوپن‌ای‌آی)،
Grok
(ایکس‌ای‌آی) و
Claude
(آنتروپیک) به‌طور هم‌زمان دچار قطعی گسترده و سراسری در جهان شدند.
⚙️
جزئیات اختلال و سرویس‌های آسیب‌دیده:
🔹
دامنه قطعی:
دسترسی به رابط‌های چت، APIها، قابلیت‌های صوتی، تولید تصویر و بارگذاری فایل‌ها در هر سه پلتفرم با خطاهای گسترده روبه‌رو شده است.
🔹
اختلال در ChatGPT:
نمایش خطاهای مداوم و از کار افتادن سرویس ورود و جست‌وجو؛ این اتفاق هم‌زمان با انتشار پیش‌نمایش‌های مدل جدید
Astra
رخ داده است.
🔹
قطعی کامل در Claude و Grok:
سرویس کلاینت و کدنویسی Claude Code و همچنین چت‌بات Grok در وب، اندروید و iOS به‌طور کامل از کار افتاده‌اند.
🔹
علت نامشخص:
تاکنون هیچ‌کدام از شرکت‌ها دلیل دقیق این خاموشی هم‌زمان یا ارتباط احتمالی میان این اختلالات زنجیره‌ای را رسماً تایید نکرده‌اند و تیم‌های فنی در حال رفع مشکل هستند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
