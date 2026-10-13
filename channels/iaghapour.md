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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 02:50:38</div>
<hr>

<div class="tg-post" id="msg-3129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهاستینگ افزونه نویس</strong></div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/iaghapour/3129" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌ تبلیغ‌شده زیر، قوانین را بخوانید
👇🏻</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/iaghapour/3128" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/iaghapour/3127" target="_blank">📅 20:10 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/iaghapour/3126" target="_blank">📅 18:34 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/iaghapour/3125" target="_blank">📅 16:01 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/iaghapour/3124" target="_blank">📅 21:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌های تبلیغ‌شده، قوانین زیر را بخوانید
👇🏻</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/iaghapour/3123" target="_blank">📅 21:00 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/iaghapour/3122" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/iaghapour/3121" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/iaghapour/3116" target="_blank">📅 16:32 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/3115" target="_blank">📅 14:10 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3113" target="_blank">📅 20:36 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/3112" target="_blank">📅 16:10 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3110" target="_blank">📅 20:40 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3109" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3107" target="_blank">📅 19:58 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/3106" target="_blank">📅 16:44 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3104" target="_blank">📅 20:20 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3103" target="_blank">📅 19:17 · 15 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFJyq6DHXknakUjkaBsMWi3LbfwZ_77jKnknOZZn0KE3FuDT8l7bueGtNPy4Qv5UcD2qBnYudbw-NN6ESnXECQcbJw-SMRNC88XNFFLeWsU7qxF9NYiWEbgVUBDxCZhk-metWFmKM45IOGHZXHCYCRIx7bbBVCATEUjXnxJMfQmrJH04RGNkGeu1xBTcxhcZeopV1WClRjN_IfZ11va7Y-vw_iNENBcEyvrjFJt2r4fIjDOJEIeC2BZJ-5Ef0Uc2yG3QMQxNyguOSXCu9aNBphxrZFiBk5Rg7pfUTp-KaFeQl0QbZ7t1P4uDQqC6jVCzDx_0v5oXfPniKevfcYrQDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTvNTQGUERJFRExzajmVM01NOx9ycM0aK4i2gpFTKbaig6cojB2Ed0jW4TDNPT8lxR1lGE4qyG-9lg87TbLJo-ZurPw0hmw-GIVNablxF_8ZO_h1ohZsQ6OfKRT2ySQoeT8L833lN2Adhn4Z8tgPqYu1Bj9BmXU8CEBzlhPfdX0HlkHfLS6tRP1Qqudgh3UzYoBKQHxmWbXGrAPuxrGEEjKhf93VHwlW5lpM_HiLNNVjYYWyCjIpxn0MthYiDLCPVI4Nj2RKvMXX40eUKp6IiuH3OnyI6_pKy5GWWF8DQH_xVScPWhKR6CJBSyYIro-n4PvJb7DRQPWYP3eL2SkUkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/iaghapour/3095" target="_blank">📅 20:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiZdVsRHrPVB0OVpVe-3k6DHR6mmAkBZGoOIVjZkY8v8om_nmy5OgGa8Mph_AtO_LHV533NdNOzavd-g3rfauWXI-wQLxjud86HRvUH59PqWdLg9kApaGsZEz-ZsUPepO5czujOAYCX8WPTvxZKUWKf5c7Vw0FSxLXkZdA5qG_fkVnACjoMg6M9FEpfZj9q-JRlY6zoXriqGwonBaLyrbLQl_3DjAOaFDqwgrkAp5FGjRyJfhkIO2gZnSMotJAT8RfrAmSzqzL-ahQcN6M_56DzwAO3OB9TORkYqc_GP22f5VzMFAtSbUA9cIxzlJ4iuPECKP8Adw3gSC_Pzo536Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK4v8RaSxvL4TLpDzliICfRg6H5PnYBWPsf-NjTu59p13dx-9vLxlojytJwlaHQftD2BfqDMSaQa-DOndGr9W6xvjeVG236nzrnlOtHlEEFMPGoTU3-2Hteco7zntJg3jXuHe6FjgCb1lz27K8Wj2yRDdR8ix3ReXKaZXLM7iqWOJe6O-01WNIzuBdMpPotM5a_RgAr22A8P5hYbkTFVnQbzAKkG4PgKePqgs9_9EeiT4lk0zAP_fZ4JYiQgoiOtf4_DljnD2y8_QnbH5aVFQdUMJBgsk8mCU2D_LfUmXbI4roTiji4wxdDE_PMaFjkaYDgljBR_crjatab-tJHAjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_e3X9wif25XHhLRZR-wFUTcx6OYfiLnEamFIoFlg4cHBAJ2Ljhff0910d9Hqju3qFhbah3qiALLLFFTrhBfcxaPsyMhFO-P6jgXUXGlYDysU-MexPzm8WZKO6HMAX0PjoSi3wuXwMYgkzc_e3xXQ25H4vH-x_ceVq5GscqjwoPhzZ3OHuJpLhWrgRTY0lrsFupy8m2zR3JQZAVglvykTfCyaplpWgyqJgRVAj_AY17wYZlvIj2Ail0znZ549Nii_90q4GPaGFh_txxk_am2gtdzVU0lxapTi8Y_ZGq7nuziE5Uq-dVUg7FyPzz0I4x53ZE_KZSXevATCYkgNGek4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPxKzE0-76E4zFMtp_60KdvVXiwalqmu81_iv3Lw-EGSuSigTmjiN_AT9L2SSvTVdd3_CaPItVDvILLbUmRCabFb1xRxaeIR7uEcfBLdHWMdoCSdwAPXF27iVKqtDmU3dvi9pzXxKuRKveBHoHmZoyIJzqEHPctqAH2AsG5l3CJ04OhMzmfDsH6n6XZVvwmjeYlhlGvaHybt_n7OPnbsOBYpatdo6Y0CD3_wKWvFEa3qGs2li0NkZfIeLDOPqYFy-YPUGZxHzqlRDdxTGt4KfviCzPSSM1GqQBhsr2-njat-8AyoVxgY5YH_fmMt037k1QtDv2N8d70PglFQysLphA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUwbRf8DHXntKPoD95_FToaZmA7tXJv66LSIgIrUoC_KWBVrnULVkaKJk-toaagWMWtMVO-4PzIIrDfoplg8cYTR68JH3SDCrPqmKmmt_QLHvH8716FGDJSrFKvva2KmnINE577qJ0al3DnhqT_c8OIe6_J0bIZLG1rpXQZTFk1gUBGV41bKxJZ3u_LBJJtYC6IdL450xUSmM5Hc7WLw_njxjp17bK2zFm_rBEUJzxSR2TizA0qQC6_JnrWTaJX0rK76brS39rdLyQp-WiefnXwR5rWnXilODAFP8-V2CO2eK1oE44uQxZ1EwIHNHfnkzsloh3psJFjsYEF9EckiCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL69hnpsD9WaFs59JonPRxWN0USlvK20bXtkb8ERtIK8vRLqoRGPVkhauXMCuPxjK9SPNfPWTzIuu79nNna8WxFrTzLO_6gnO2LZlxdrq_AgLwCdn3G1lPkbKlf5byoX_BPEyjpMUMD1RLddYY-qN5RVsl46An2ir3X4DWuU3q4bTQfjAEz-HMh1GtFjds9zZSpXxmSKICly4O7nIp1zhlGvQRdvcGZPkHhxq6WReAySnCNNkn7aEuv52-9_h_mPLvZttSvj7PCfwitsdV4x98-yvUHVQTZDTK0d0_VLF5juCVeuMkcmqBxWbItBrINqIeB-P9p13ahIrywQYNAB3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmIpX5ieKm8xOk5kkpR0kSDgyQw6y64zN6qOzzXwECqZw7KeEFCv1FEcOE22AucldacmioMOr9xYADWDUvfDpJ6m92cv8qc_RQU-CeNIiQgZWsg-YUvjQDX-fWzyFIr2lI3sa9kAZZ2GG7nOC_WA_NKbD3u9KizUwcZk1s_qerX-Ljo4HbYWEJdUoQ_dfbwVGKsexECa9pq7zt-jz1JGCMYURagv_Nbq1q-JF_Idgik-gWyA0xpLIInQrHTk_zhifHqMlegSRDJEUywfshbbCdNMFsZ1UxihEJIOnyMf44KgsA_4_xTuiPsYxJlGvq2UYq-7yETbgyN2i5lpvWY4sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3074" target="_blank">📅 20:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3073">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTr6OX9ATQy-dcYv46BqvzxrXkZXhixPrhxeV_zlwMwbAeyGMn5ECLFHQyYyshWZ3yhPojSarTPKnll8NKpGPyN9o4cM9W9OOnH3OgWr6PMg3j5suEqrMzBwuiBK3vxv7Lvjv0qQ-UVKlq3Z-ayTvqdqMPUuWkpCxNpDVWCzuVKkzrEAlua_rsWSLKbBFV7wgPNEtBtvRs5_9EoE7uQ58ce8ieswmTEMJu40l_ZdBIrG2yAjBCIap4-9TuSnxGQXZORFfUarheztOLiOGOBBXh1zIotaSuflNyL2XZbrLzliCkX-UHLo7ZVVHPl--9yuJQLp3vFR6Ap2nlHevA24ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/iaghapour/3073" target="_blank">📅 18:47 · 07 Mehr 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GYV4_ZHtO5ZjQwoN-1pTavgyunVa5nIH2E9MguG-IOBozFv3OTqAgoV4n3D3GJaG_qKpXmhrXTTAOLueuaVpnpie4hoAXuBX-JymGqJh78o1gQl4fJXp4AQlsOkQPO6A0WcXO7nKTVzFoZY8R42ARZbuh_yixyYXzonmiDl1ygfxfH5s6lYFrkQhz0f86v7PUp6xT_DFFeTTVa917VeIii7le5MlHCNjuzlBkmze-t1cGlOXF972GZaTDjzzLg7kmA9SedzNjdkfD4JHvOqXwMkZMHxTFrUI6v3o7w49pAcnT4TUCbiUbItB3uKxgQhdqXKrxcdDvB5niHP-3Sg9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdLGvi3m4SSuIKk3errfuP6GNYkQuxZPd6GavEB1U_ZsAZ7zUsl-k2FxUA2PYFnl491L00Rh6SFL8dX8hAfEKXk_rYBlkQij1zUHolZ-HXIjLnuTbUR3M43AKHTzY3GN45SRYA7LfdvbSTw7oVYl7RPAJvcSaGzDWS5TbVFeOrnLZZ1iku96M6HoI8z-I7D6WwVeXNrjNA00IBVQz-SX2TsoyGiTT1Sgs1GYXpKu5kTzhE83AZ0qli-aDmEwYd1beDwQNMkZy9Z9mcX6ZNFM8g0U-za1lt2kwEdDaszWKaOye0HfmV_9dyIg4tG8Vhs3S0maNi-Jur6MT8oB-Igi7Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=drDX_nh6muD7_JgKnGD7G7CtbSg0sEaMaKXy2l1XJYdiiR_1bCMPseUBa5UHx29wimolTGlqDnqo7rMNxaHOf9k_C8i2plfsauC9wXITDcujwFV3dp8K8YDdXr6HI8KSJuLncYDJV-Atyu9HcFWnVU-u2jky0QYUbDaeKikW9FyTsENeGRPkRbWAry-hQZRrXdkkg2QDhjmwYig673Ahv7h95CBS6zZyUWgfbHOWMNKbuCn9ESnAv0FnV6qBZOAduwaoDN-opcjYv26heuLDo0Vu_3aSVFgfASYnnUa5_aj-qLDlTTKfA_uE0FnP568w2V_usvFL9fCKEVF3yQTfdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=drDX_nh6muD7_JgKnGD7G7CtbSg0sEaMaKXy2l1XJYdiiR_1bCMPseUBa5UHx29wimolTGlqDnqo7rMNxaHOf9k_C8i2plfsauC9wXITDcujwFV3dp8K8YDdXr6HI8KSJuLncYDJV-Atyu9HcFWnVU-u2jky0QYUbDaeKikW9FyTsENeGRPkRbWAry-hQZRrXdkkg2QDhjmwYig673Ahv7h95CBS6zZyUWgfbHOWMNKbuCn9ESnAv0FnV6qBZOAduwaoDN-opcjYv26heuLDo0Vu_3aSVFgfASYnnUa5_aj-qLDlTTKfA_uE0FnP568w2V_usvFL9fCKEVF3yQTfdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4rU5x13bk1gfkSSlzF5DXpE0nUdLhTc2DGnMuEOUPiScKQRXiXge0eJaWXIVuNmaqMMC-s6oI-cic0MLT6adH6VUiFVy6_ZORsq7iPXd5rWrP34aOFaYdzevLqPJIebxyCVXfB4tTbAqCGXi0zN7SEspWlowOfgpihg7Q892S_Pj6iL7LPa-_ddnWjhMTZscaZDvW-3IUqCHsCeLV3zzdSAREqUIcnCpMytRpax7JbDvc8AZvv8CRKAtgkNXB3LX7_tM_FHdEtS2YwvlaKO4EEohV2Kf7MHL5FdhCzjoZ0OO_XGhYD2VjUa9FMT23TC0yES6Anjovvf43C78d_Rdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4_xz4XVjDvVSKj3CVWlTrQ8B6_Coph2vsP7f0RfYUnE4BsQWBGvEM3-EQvFmbQmbKDT1HpLhdWn5rNUrhmNWDVdZJ6a1KOSFCMvcai-c2Yv8WaslVMEoZ7bKJMN5mBJx1oJTkIzgU46weJ3PXEMYIieyuqxsahmytwzv9sau_kRwUHBFS75m7MZjESZxGUDQyW2-GLfQLtYyHkN9ZNmfmmXYNJW8YqXO4RMbafREUsFCA6GwgZBJBnLBSrxP4m_otLetU292NDPp3olvwNaAobiBWGw8UFGrTd1aKnuFJ9xV5wZxt7ro809m6UUQxUf_v5JTZSwKcHtA0oGaJrwzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IInQsdwuejhq67pxiX1vih9c5Hl6Hs-0EgYT9kprSugfeXuqqBFlMILk7-Nhq5KUykeuIJQz54MOJnkx67BCRNCGQ5Q2dV3cRYDEEKZnI4zN_6bd1WhbId_0NLLgnOQpEwImVGUTi7jfBY1fVKYfCQ4XxgcuC5MCBjzTDzWbX_Y80CEhn5yFe7MeIUGkBR6UXkGA-KpL5qk6ZzzNsHA2zR9_Joan24vbzCgfb37D6WPai-5AKw4FoN1o1pO7B6iFWfmoihKY_yQYHo8ACDY9SP_v1gFwbSyj3-lcz7CckB1ardINH85gtZnLxahRX5IwoYEdIba6P7LSL7mg7uFkrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg-Ra6XyJC-b1LZiJo2gi0YIHljtkuyDy8n6Ms3bv-4diio5DlMNXxemhY9AkNXLu-jE2Egs4jHL4dLbTk1cqoPoGpdcT2aNQij6jbyKx7hHzT4InnPnaegM0nuRDjUkRsNccKMFQkDESavMAC_PuAF5qAPGxnPGLAMz3hL_SgcZYwdsM5IQw87WJoo4-zF6Qd_WceGXqYd365QvM7ZZ4Z6Eu7tXCxfqbYqi8nIAD-lyqgv6WClL5abR3ya8lXxPRvWmldtfp_cL8bLeH2thTSQYEh7Y_hzDGj6LiP2zijzyWcFdd2Tn16scrUW_q5n29sdB_rPJ40xaFDRZTisgRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMzlGiOLIxH-k7d0ztCEur3bAAn-vH9EoM4T6BJR2btkGEZsKtsT925I8dPelT-lKIfX1-xjiy53y6tEC7uhLhMMxFORwUvor-2LJa4bbK6neVKBWo7_oz8w4ZccKceebzt01LUPSqNyZohXXUZauyiYKnjA4R4wUDZdu1fvV8Z5Z2-ym_h_-GLiWvlM1Mw68XdyGbVRWxTdT-bhVUUas826ZxRN9wMpYe1_FYMJjyV5X7ptb8n6zsj15wly6yviexNc7M5cioWXckx11p-JGne-n_y4iyqeI1sUS9vgujA7kDD88njFkuEzq9fjlR9pMIjZ9cfRn1Rg_tPOdwVKNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFX09Ox9uBRGCG4ZJ1uM-i5YoLMK4E79y3lh6rVLZYxSuOKLy9ch0Mf9zh7THlLwh7id9WcYEGpSNu0vhdJkjB8jE4TFDV37B0G39dP2iooZbqZQnR0WIr4yJO9_DGIfWzpSszCsnGcXqadUUJZxCFZYiVR_WTBG6d5HTULI0hZmYkcyF15j1MPzDLJX5dNjjMQNmuLCShA9qNmiy3j4lslxHhftHfp-P5Sl1gweQ4QqzQoZzfxtqp_ponZGIg32Qg1QtqNg3hwDVcMEF6k_sohLTCF-nk2cK4E2QhX77Ok_RuQHwYGke9WcUMfT_NyqzyUxSa20SNCPzyvY9BH9WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/3048" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=gshbDekjw7WlSDDjxV5UoQK7VjumTnFgW1Ib_U6ZS1Zv09cP5j38zaQZ_Xd4Yj5DB5ihO5HRh5MwD1txBhNq5-ebpn2dhC6uipNAD7Fyi2bW690n6VpyxWuBrVuBi-jq3XrHzT3eFYJbLAfCG7DZWsldtyOxwi_f0tiTfFZ_rsPRhxPykoV6Hnff6r4WNlGg__KaCzIFnKFm7aMoXZn74qwyX_4aMV0kA_2bti781AMrNXZqXcbrzK0-LydF3XvZd0WJ4RyyfeFTZw0MPUNXhjKzqTd38U0gGexGlItsnj9QDajhVNPDZTC_33Mk1JPCN2pIrl0ZFFgY4sDK6wmCgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=gshbDekjw7WlSDDjxV5UoQK7VjumTnFgW1Ib_U6ZS1Zv09cP5j38zaQZ_Xd4Yj5DB5ihO5HRh5MwD1txBhNq5-ebpn2dhC6uipNAD7Fyi2bW690n6VpyxWuBrVuBi-jq3XrHzT3eFYJbLAfCG7DZWsldtyOxwi_f0tiTfFZ_rsPRhxPykoV6Hnff6r4WNlGg__KaCzIFnKFm7aMoXZn74qwyX_4aMV0kA_2bti781AMrNXZqXcbrzK0-LydF3XvZd0WJ4RyyfeFTZw0MPUNXhjKzqTd38U0gGexGlItsnj9QDajhVNPDZTC_33Mk1JPCN2pIrl0ZFFgY4sDK6wmCgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-EsfzhaXKeCwLuFOWwk_nHX8y_m8A8L5ct_uBbaSBWVhlYYg9mNNeIJqm6Dc2iJZZfKsY_aMzWhLHnHsWzL6siTHdLQR1BoGFzdV1Xc7yyY2iVWp67Pmq5HsNEbkK_tp7PmIit8pi4XzWyf1AgEgUO-cX87UPnZEKSTF6uGyKEhR0BS71LDR5ZNkLTQPATORECZDJbZXPdwfne3En8kbIDrKRIj7QYbaW_b4GzzUaz0R6kt1yv1hzBXe-ydtyByzW9uFrqS0R_wA9krAqmb1d5xgV9Yl8EFNSN9saXL7H-YXVlF7RZ7IVoZ4CwdowI72Ezq85mbx5swGdv2HYDg0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kThFlxzmar0c13J0A-52W2wkKUChPXGpP3aQ1goxksbOxgE06642nIXeXhnbBE0gQ_Vn88IVVmRy-GYb0Wmajaxwxxp_1BIx3ko-LVuNJUJ6VgQ9OFKp08WWxMk7quqVTPzIn4kAiTDQTqWyCXKstqCAY4nGDSK2qaWKy2JnmBiBr9_a8WO8BoYSHrAzziXzb5c0FHkxeQFcS-QC5osSin3r2AYLNTk3BAdMuL3qawLP2mZfC_EUF-X7FxmKoPYnzIAJNyo4IUdBaUOrmi9xhIONwxUWP4bDKhl6N53COSzwPgMvyFpxLwOgkIo0t0FzI28vQyPRX9hhmqdXUSr3lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v87xRsKT-bGufLeVxpDtXsJOxEyDtVR1pHYE8_-3DRgsZvzWmS7YbwumYyF_vsEYbC8Ppq6ki6qqrEh3U-9eTN2e6nDB7CerzhkVGxE4nG9uMB0crV736q9eq7Zgc9tR1qRnHCOS0GFoWxjN2eUI_jfjrHPyyK0EpR1HEPgJDQcJ3RM7ALyow3VfabgXdRxqwevhXQ_zk8-HCMiwBqIzwF6g3hCDvYvVZQzPQNx6bPhjTMfyKEN0bpvZ9gR8PWdZKaDOYzLJRXWWx3K1QegScTVfeQMGf3kOoILBFIx4JuqcayUgMU0brxZSjAya2GF58wbaIYGIRoQnlsO_3aeggg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3_W87wJRxukzwn9IeYCRZH5xUAYhQ4dX6EQnbMDDDzT8RTSM1TycCOzoRq4vD3SCSZwPshwC27MPzScCufu-wt9QztukV7wz05u8d82Kga1Bybcru9wccajeahV5dkVqaAh5j3VfJumMtutH8WxqQ7gS20JAfSk-Kco-V3wJ7vXJfaqz_dd4-LK4iTAK0vFNVwzLJ3-4T6-yGs9dNSjnZTOdUnvtFSouneVQCGlWEtACj_10T4zFEOe7nAXOuf_avAjR8CwWmQNOAilxTR2dRyRGB6kuxi6lkl7MQBXA-Bz4FAUGT0xIkE8n-5CunmVv9h3JI34TMZDBVHJ8XUN1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnU9MWdKA14oirB22Ke6spYeeG5NxLeRZ2P-Wb_lfg3dAoAe_wqHiJp0rT3zQNZX1SS5R9EtkKs615ZmBCwfOJD_Iwi0_XL8lN_BSvHB5TuywikL9Wik_rWS5AsE57bMX58Mkne9NZcAgxk5g6jjshouOrhQUdEHGkBB233DvEa7PCW7g4kGkbBnDO2TEqNQZJInHMv3D7-q9O-9PVgduy-3jxRwu3nfexx2aGEgdLr2EI1ecsdpRnnXH9GdbQY6mVnJh0Inm2QfMCgDb8TkP8deZS8H4JEfVKTod7H26mQdY3RmLA1CweMUYrBnV7bLlQfqnAayQFU45x6dxpjV8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1AuVV3mTOX5l_TcrOdoyeUFHBJYFCLdbe8uQSkx0Db2SVqp9Fl-VlTlST4D_BkMldKUjeOgZI_Q-lj9uTv3IqgweQ3Ts5C6yxmisUFV6jAf_QJ2kJc0CldZzr8LyZPZZ95ISRIX1U4Ph77GTQmw9DiDPiL1E8NN2OLV6bZXi3lfbMeRLXBRnihJ0zTMKapjEZ6uFqfMvQ-2xbuIfb_VWeIpcNpDJuAeLqP36HBMQp8V2MZTpbKM4qLTikUY5aMEca0PaAqfptm-vK4rm71hzsFmsaCoDbOWujHs1vuv3c3Bv4qJT9mFxK2nQ08AA4CsOMC9Tgxg6y4zoeHCNN6Y8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAZO-a8pBul20GpiaQP8-0cr6GTKIL3vIb3T_8bkP8hnOFgy0nJlDUbSH6ZPpVxvGWVMuElXPW2o6GLEms5Lc350beVNKv3QsWLdIQXPClM2e6A9s70CLBk19sJmjvwt0ZDAOKILtol70nq-MKM2g4si-LHfjhGqOzBYC3m9PArJ5ddry9R63Mgubrf3GKTzndmWLWqGLi7pFE7GeBxpNzFp0ilovrfFZHDqhFstQTfLc3GnmDbs9XiY2N_ei2UCJiGzN-dpJ-0nwCf3z0vrY9kdBoaDnwh9-ba9_njPpyOHJ_Wci0zpW6m9k7AXtEu8Mlw8DpDnUk4uIh04i6VGXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTY2rS9d0HC_FXP82D-kt45xDqU9AtV-fUEyQ4pby_S4KCqLL3n1rXNplM9vtAFR6v7q0IOeFE9H6s3tWXlWLdc3KgwjWikxJPbly7YOnA5UEu1BHmV1MC6uvCOtytnB0NvHqBqSncD_vYz6TkDuxjb7IWg4ak6z_PluTvBiWNlUhWrm8YnjSYDZRhnLtrYo84qvsAu3pOGpTjpMvfQY-_Fiqyj3n74QCn_iYJQ9uxHwgGONDLqrFBRv4AwlJxphX1bdpNeHBaFUDqL8tSx9SoHaXgNiAa1woXtHgc6d5ImKUZCFnfAFtRMm8e4sBpHFKataBQKuQK5eQl0dTv1vHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7FRjbJjM6CQW5dCiDGJCcHlsmFWeoazQacSaS8Z15OEvwdkJw1l4H50aHr5GuM-9xFMzE3aO4IMz5lu2ZD_Z5350d-kWtf_KI6vtq4KR-gGVQLU31sFSpellm78Dxurpm-MVFC-mPLJN8r9jIc6bbdV0m7SPohlvb6sNFwBt7OSaapTUiFtU4xknar_SEtsUbxQSK5QJWSIwr8bcPxNvw46EAOGiGnR_lZiMVgWKuZUfldOkCS9MSDw0JX2v05qdaDAUolhYTA-xOBB7YewB2IAr2s7xFPI2dRkjRbLxHitzvZfvNfY8ietHXAMUhuGzFUFWj2c5g_wqD1BnLJ4Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4YyhpZZjj4c7DDa9Pvk1Q-cbb3glCNK8wazPsVZ45HNgTJ1VkTJhLRnJZAjh9FoThAl9_5m3G9MD3_XUnJt9VViccpa36kj_05mHSh0gpuqAWndMv6kmvE85DKJhSZZ_AJ-GmKEaVU6ZsTy0KaqJvlcDqfY7jOT5GvxCg425duL5rI4G9u2ZmOgEv2atfxSxaZ-XmiEZYTlh8-N-lUiTbL4-96OtWp0cBuP1B83X7BLUGq9IAnn5-s00gsnIGwlbv6yG6vFjJiV4zXX1FO255XfCRttvqF63fw60XiXjNQexmzQV6P-17YDzXfEXO4UOESzAsiAvZJA_XujCdl46w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=XLFEJhdPtqLT_i2z9QVX3BLqnzD4lDAjf1jn80Ewo512CygcKsbX5tACCj98sVOb26Hs_HOT1ZezRUbLzXTT4Iw6NTTK5qCgbC4J3Rm3PnNIvFisALCWP1O6a4hcnyYPlppxJK1Zx_SgZnn0I_A53kalA6kyVAt_CH6ybjPB1ykCqsPMAralfV1fau8FyFhTlV1ItePSgh3p-levaWpJJWrHJCgNFba4DXAXQNGXs_WrS4690lg58pCBuI0dpqmHLWDAiEMei50FLKNFB3P36yjEvdpGJykiUmufRsj1ghK09W1B4KppeRawgDazMNkrXeobmt3gg0wl20_az2N4dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=XLFEJhdPtqLT_i2z9QVX3BLqnzD4lDAjf1jn80Ewo512CygcKsbX5tACCj98sVOb26Hs_HOT1ZezRUbLzXTT4Iw6NTTK5qCgbC4J3Rm3PnNIvFisALCWP1O6a4hcnyYPlppxJK1Zx_SgZnn0I_A53kalA6kyVAt_CH6ybjPB1ykCqsPMAralfV1fau8FyFhTlV1ItePSgh3p-levaWpJJWrHJCgNFba4DXAXQNGXs_WrS4690lg58pCBuI0dpqmHLWDAiEMei50FLKNFB3P36yjEvdpGJykiUmufRsj1ghK09W1B4KppeRawgDazMNkrXeobmt3gg0wl20_az2N4dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYGOm0Q-J-UnLCR8eglJA260WbiaD9AbEwTU1Vy9RUwGNeFqzQKQROkVlQTZjTxYCb2VJQptXLS2LvUo7VRsViPcHfVVFvCz113CS0SyjsW43hSyAcB_v6k_5yOjCW7P9zgQNplw7oPvqMtglFs9yt9sNqxT-s_hyGGBjcDxcfkt9VneXfoHY0ZRsTKzAJfjk-rfAc8XCYcN10h0BhZbPYibF_6jctWOhyYYC8WnXkmKW6fsYRYM1vwTho40hRC8_wXASLPbDbXMo5B3sdYWXJv5rT3x2T76t5mkebAcKn55uHr7m6Vo3o6BwbSymYOyjMbjmuZ1ajddlFd8vpTVfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzGjNqBEUg-iOkcx9wpZ1b9L5Iktoq_H3CRs6BILefjySLLTODyeKxCYoHPBYxCpM4oPW3dTA77uIBqZ2KoJGeh5X-vqQxz4eMKxXxtxD5bUDqUrdoRp07_NnzJ91lrvqZPyUIQb8gZMTDOJJo-YtNBM5LpXwI6YfVexbev2dmg9-qNQGuadnF0HOuTiIK51rUmWk9iOqdL67eyHkpzO1XIUMAJdZO_QhrwK9DY-agk11BNhROma6x-SsJxZryJ0nF2XbzgGfdngRFNK2dPchDUO3yOU_u91cwvV_opDezThIGKpKGhirCQeQDjmtDGE6K6E_Se8iALIfOqXyNu3LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqJCbncPA9T3OKop8fJmIljv4Nyz3Bl3O5C5Duzvj76JhLJwRU0Fx5lvjx8KaEBdpG4UebiHjrMUZoT9byEWEtrnkdJhjqJ6zqLvqcbUag_455UofxxxutgxNdt_Qcw9IdTjV8a8tI1Fe623zoD0gHiz1O5wXU9vbLPKZ_FBIj4oPEdEqbY4nwoTYGB9Mfjd9EeggW8Zd75biwk4_mVOJMor2K9SpaCMwkAUKiVzd5WIj8_nHEbQSbbnP0hYFOdYVFY4BDS6LyOfz_Jp6ixmFleQs75WpOIs_X4pTXLEAuErwMLsev5K0jsTHPt39r8I68dBc-sNXniFez-wr5sufg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlkE4gXyOtrnrx_h2aAhwhrwsVdT9m-lcZakEezjqx5DSi_9xYDlU8r8w3unnkm8n5SXTPE8RtkkZ19kifL0EmwBJVBhNzt-S39uOm0SyxKfUIMhpeQsvETM6p4CS_EHvnNXtNrcx37mX8N67kPLsOr47lnQuTChogfmyZex8mV2vHmCJYcry3HVxLxL4D1f4x8ZEyTeln80rZ2c_Cr5ulNAW6HyMS67EMR9sfHWEi7ZZ45tN2JO_c-tQLkv99E0EMSzqddRKS4cnDIKiEiTaSW5hLFUwUXk7Rq8GVRb7eFRTy_ChGW8gqHA6ruZ3KXjxjB22auSv-w4EribgmYbeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvHSlUHmPFAwR2MGfgn6DEe6uTbEw8ifV79mTU7TxT_yffYHHVIO9TL4RE0WdF8GMvXcxpATb8AR0uJx-0Q7yTmfFKMZODNvHtItz6rJ96mTOg5o37XtLixckbWSu-D_aAxN3zmjB2okTkFqgroCH_C5bQUUxiSYQ1lNy9XS_fM3hqrU5DwCOERG27enUS3q8C_eJBJMrJ8_UjpMjnkJkn78cyhe2s3X9bSF2M9xVYFVjbi8ao9U20S92qnfnCfPkrBSU-QqrddXxm45-EkOS9l7KjN2q-2XBRe8kz_1ABPO4qSdKxYWdebpNZDsQ2w71lo1fdqRGYTTjCUs4lRtkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKOuby7i5F0nRXynm-zkAlhfzItrOQlCMFV_PLB4dPoPFdEkCSMnOLKx85mAmMIWC6nhla3MHhObhtcDQKwdebxiPzS8Dg4OaYsoKKQz1zT3J1C3uTtp8ax__tqXZqUXNjqGf-LRQl2jY_xxZv9SeAIp6aQSzD9FwRo_7c8g4U46Cj9fnBiW-mmg1Vye743OqcXB9CFBMGI12Fzhgi91HdY2S8JYyMx-bFodmGNpQ827D29B8NZqIf6rNne8s-R8oVNmqd8d5pC68i-siZ4LRqOXriPbqoOuqgGu9Rched0YhVNwZmXF-iID4XMDaR1D_52zKf8mp1ujqtCHLYR0Zw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=Lk55Tcztd4B8Eo3uRlg9wAYhTYkSz1B9bP5q6IhStErpLMcTTuiZZG9sZfyjqu9v1PldYxypVkqVIePEUxoYIiWmX0TAoq36xy3jkw66Z9Jst8o0ysesO24BE5OF05J5MqrQLOOLd36Rx1RKOcQCoegYy6hxttBO48lQD4Q8_zRyEK8DjkgZg5DTOV7QNO1IwLpadqk6KAhJtA90TaHmZj28KuKc0wR8AKPDGzdjHLPTuHpqkluMvL7f6ZgF2rRFyWObaPfyMPG0rvocyfkeCX02B7z89JKi8S8mLDm7dme-6eBFZVHAOABdFtAm0I9FopA73jZ1-YASWHhM2K9KFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=Lk55Tcztd4B8Eo3uRlg9wAYhTYkSz1B9bP5q6IhStErpLMcTTuiZZG9sZfyjqu9v1PldYxypVkqVIePEUxoYIiWmX0TAoq36xy3jkw66Z9Jst8o0ysesO24BE5OF05J5MqrQLOOLd36Rx1RKOcQCoegYy6hxttBO48lQD4Q8_zRyEK8DjkgZg5DTOV7QNO1IwLpadqk6KAhJtA90TaHmZj28KuKc0wR8AKPDGzdjHLPTuHpqkluMvL7f6ZgF2rRFyWObaPfyMPG0rvocyfkeCX02B7z89JKi8S8mLDm7dme-6eBFZVHAOABdFtAm0I9FopA73jZ1-YASWHhM2K9KFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EipPoCTYSrM9J4IHFfVwtPWBM4boECBh4J_qlOKbfPBEIIHbovTabqqyDo4d_YAQcCwZiBgjgSBWIcI0XK9HA2zCaYrX01e_hHNJjAV-T20uSCynMvyvLQ5Q5Lj4kO7zydlqO6xu3hsZeNupDMFNqVH13pZ38nefgQdpODgwJioPZDSq27JLJV25CWv2M1dHY-RmD013w5SwUm8UmFwY1j9pPcvVXjdz4p28g73gXycZOL7k7q1dJlHDoEiSUsjXiJRwy9j0FOLtJ3MPfI9VcYEk0eD-Kgo_u0mpvQAhvC2wLQ8RpbzUYIjKYpN2ExzB8gvfic3ULFm22LRKHnVT0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9VUAwWmZ-kkGIbkSvNKC0mi-8xAUTzDNjRwY00B8dskjtT90AbkSYfSP5ejWJ4aLRdTAl7ktWJS2xfmhVvkfJ3OqVzrzBHUvvky2LAvnaAggq2GWOW7KtKWP-7pBTq-uLRkC9W70x2QMcPoV3ascc7fJHDoPrv5ql01L1JpeaZd1UuKmHSSh6lMyW67piWu7iPilE8Fdi9zOsiUIUOTDcQvGxXPMOX96aEXt4k7bGBgd3i9-rYkGv3Rr_1TJMRSoyJEzvVY8UrSGArwScdwNi9dTc7euq_AXd8UzOiTmQVgI_nNizNmnZgPShLRNAOQG04YaSidM6XEv_9NzDeI-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BClSBIRMtkGqU4xOnpfClSpqN6bFO4NMxQ-ITlvUOygmZLVMly06y4IWjpicsXl6yk0DL0VGLhClJQZnTBK1CDN5o5QMa2QWV-0oDdLHmHLU1lXg2vn6L37fa2bBzXPpLwtFXUMSoU-GTquIysp53ILdysXUknoLd6S5V7P7zGyPZ4ggCA3nLorEtvpe4RwpRR4PVZ1jHShVs9DH5lmZigY0ZNUX3wqYqTxiCgFGLqksg9GrF_dL14cLlQ0zCN4HsvPv9EzWZKy_EF2Dve7IjQvIIHq4O-q0FHHbYMkeysUiO6vzlWMtm3QLhdceww16x-7GU-yL1-z_pbA5khkVbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYLPnIEBJgoWleWf4KjKyUVSjle1UG0xuSZoYg7sFq1a1NS2stX-MO72Lv3-GBZx1wwnKBhqlHKGiwral9TWts43n541yTfJgJbXDCIlvHnFsk2t30Bot3sZpZDnGRuz-bdBbTiLfg3fisl9lNdG4FhZpDeLVEfy3_byc9GxCe5tWNsfyQOrfUHVWXNVSmgVDk7x_pksI1wC5iDZ-UaRAHhktEeOrda5x6DriONrcEF6LDkmwtf6f5jbKsgjT5iuVGwoyFSM9C5pg5tebm_ZibUVOLP99ySCqvjXtYgUJxaRxpngCBcA5xDlDikAm6V0UXtLynwx-9pGODY5iheIZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_fgp7XPu11G6d_UhjGtxogelGV49I3skSqdEqw2V8JplmF1_GvXBLz9xn3a5eYGDlzptgG2ejx2Zlmcicy-kIctFL-B1GBs5PIveGxT0eayujLDKA9-QDRzm2it9KgNCXqWWBTOWe1jU_ncPAz73K7n87l2gkf4Psh-ggGX265cIPjLs4DklBk9FVSb36aIdsRdNwLah33_zJEAEAwhdM6oA2IHph_0Fcd24aDK9chSzGC8wgHThcuQi3dXxSLGRrWjbVcs35_C15wsVa2VaoCyauksks6TTU85nko0rmbloDhpoRmekK4M-QyiDcoY15GAfSyyl3nWlbSmoe_LHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iza5nUC7GDHPBSwDP-0_Sz7Ucio4PO4jVv3_wLh_rfdcF00rRYdeJuA2LvZZQ6okbmJf68KqOsI9gTaZe8r3TwrcXqbiop0e9hJzwSLFFTcaHTWGKT5saAlRrVGPEw2G7ZYj7515Sl2VV7kAhFt1-mo7jk5_4rABVlkeUx77M_KOtTO0f5omfcxHQ-coxcoVAAstkqTbss1IMJhkjrLHSPvHyLs-dUNPxCYxbOa6BBvxrbZWLckaLp4CeWf2-G6eSTRxa3IWfSL6PTpt-Xu3jF54Ggz5qqnQePq9Pg1B0g6zl9k8JtA61kxQHhdKK3YktDwcPPklwVB9UNkkb2aZZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oocm2JMX_FVTDXu6cy1lKRzXfYlw5S3nMdxYcHpSpjsX6XrHi6XK09mJUBBueRF7HLaUKpqna9hsFmcp2fk7WXA67qwqfFsnSkwEVYTdNh8KM2jLkicWO3A20rVJOlJgIr6NLy7d7lRUcvTn7pvJhW6sXZRy5HDKjvaaLkGI4on1cku4sUA8yFv4ADZ2c3Tj9xG6_got0Aj3ocBrX_D08ENcNIjXBAiQ8lf05hIL2om-Sb6Sp3RDwZi6tJeQlzXatibvBGfkCQYNgkYPbdBIVmu0bUFUcduDi0FQ1dNg4wBPflg5MnNLMMk2DIOD-nQhkfiVNwAwN-I7Jam-kDXXVQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=ovT0Gg4uPxKcgONeOxnOP18mO5LxctSeTvcdqYJ0IXEyINcf8uEWZi2nwMsoliNhGJh1YuJWjXG0K5RuO0i-3I3Lf9b9o72ryCHZcNmvkjsKXHRUaJ1ucD1AvyfdRQ-cY0jLibyS2ahM-rgVYG04m0iOuPIkvns8EYbmL1yPjBkXUlNQ982_DcPCP6HTYkR4rsvJS83HJtv9UG9FUaM8A6XFE_BZCQHU2rOS0zblieImi2GcayOPjxbZjTV0k8YVMIqhdwbVqwLurOUSUMBPnYXAv4eW6vdVNvDhLp7HDt4wtuaaO9wecuKekyJ974jdzzY8cAcYdUb9ndbLclSUvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=ovT0Gg4uPxKcgONeOxnOP18mO5LxctSeTvcdqYJ0IXEyINcf8uEWZi2nwMsoliNhGJh1YuJWjXG0K5RuO0i-3I3Lf9b9o72ryCHZcNmvkjsKXHRUaJ1ucD1AvyfdRQ-cY0jLibyS2ahM-rgVYG04m0iOuPIkvns8EYbmL1yPjBkXUlNQ982_DcPCP6HTYkR4rsvJS83HJtv9UG9FUaM8A6XFE_BZCQHU2rOS0zblieImi2GcayOPjxbZjTV0k8YVMIqhdwbVqwLurOUSUMBPnYXAv4eW6vdVNvDhLp7HDt4wtuaaO9wecuKekyJ974jdzzY8cAcYdUb9ndbLclSUvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVtStgfXtYS89_ej33GSCUBRMMtATxfocAlfxY-bdwafNvkuN4SR6WVIf30Of8O44_zUftMeuR9vdYMFO1kJaFtjluJjsozBTUtkgxUpbsh90NaOAxXM6HcHXaDjcjFPIkhfo4eDxFT6G4nuqt3-X6mIq_2mmjMmtHO5bjQD8F_8L3BSLlcqK3A5jPnK97N9ayNVCJuTmGN04lEXJrihXlRPOHoLTHw7padYiYCCAWxm2UqVyBSHR4BT2zyhqj3F9vipxqY_E6QcQHqlKczDIlgnfa1oklobHoViDQBUCqtlqeXYHaWIqGfXnO8G3IdLjooTxDc9RyLPpB1WCVCgcg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=Axvu4EyWb2XYxUqUBijKIqe72V5ByJXlrZPPTdZzk0a23hRmMC-2ge-pJbYuUApBvk42itqfZcbscpFpEPif34SR4nfk9xcSY8ANeLpOJCOAN-fg8KW_yH8lNNjpXqKyO6i13wyxcFu9TwZHn1WL6Xs6EN28kyjC3SrznbEB4UrZlXn7qFmM20RnkPeZ1xOnXEIIY6WAmgeFUSTn5ffdRJKuoFUOqcvsb-rKvB3_Iq-C5H8oFEpt5S8ndSmVMHeE3dntw2G9YgP4I4WInzaTqxjfeEMzavVHKpLsCG9quVpj1bd-GWE0HbRZRLYvRBDNURymrK-Eg_jL3ZjT38QRBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=Axvu4EyWb2XYxUqUBijKIqe72V5ByJXlrZPPTdZzk0a23hRmMC-2ge-pJbYuUApBvk42itqfZcbscpFpEPif34SR4nfk9xcSY8ANeLpOJCOAN-fg8KW_yH8lNNjpXqKyO6i13wyxcFu9TwZHn1WL6Xs6EN28kyjC3SrznbEB4UrZlXn7qFmM20RnkPeZ1xOnXEIIY6WAmgeFUSTn5ffdRJKuoFUOqcvsb-rKvB3_Iq-C5H8oFEpt5S8ndSmVMHeE3dntw2G9YgP4I4WInzaTqxjfeEMzavVHKpLsCG9quVpj1bd-GWE0HbRZRLYvRBDNURymrK-Eg_jL3ZjT38QRBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDR9vqX8JKtbiyeNCupeNOzxJQSUIWO0mKBPzql3stGJ5A1MpySyd82afaypxHCLqPxK-qTqTB4sT3eVU2XAz_Kwta92ygw0ZVupCUeUpm2bV5ZlR0g6HlJinwSym2sL0vR-EgIhHWwazM3i2XQXXX6yhMhZn8PTOGoYMdLIXEqG4wQkIu3lJd0PYOABSf7CprdcSSGEr9TiQ4CBkLS4JJRlnAr8OX_MAo_KrV3jq4gnDjxCC6XGWLexnlFAbntgsheihu3xIPLmP1U5RP2k5DIxlI0_XAsO1Fvj21rVSB0qWDb9e343aCx7QQnaXHS9cTVQPuoQhFsnAzLAmTk2kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUgvgy5mv0OTK-tGNIgzfvbHWO-V7Wq0GTIuVEHELDeVq-4u4M9E9zHM7FW7tq1aihl5B3BKia0U4cHSBouirLgWYQORHizbSq5EtEwi699seCznKbKn4L-ZqY0r2AtDpGl3casILWrb3yqUte2g4zi5q3HBSYIc2O66yVGMYmlKkmgg5_XUqXbQFrIRMfBzxEjAMDw4kQx_CSnO5bWUwSPYHfoGyqhFQea04K3TbC54yaSJoJSFGHb09BOyMahsNkaZ7tdSmMZopErKnpycnn-TAaEFLun1XeTSB79Ff02DlBFldVNvx7mOIVsbBpRMd-RHkCDcS-0EgXwT_orkPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOPUFpPmosseVU2AAxnRAD_huSabhdRs4ULbpNTNZWZpPbyYBzv7wgymXc9zP-tHnJPUt3onbXZJe_cgRfHFSpNh6jnDZmHEhXmPM3Vmg_btgYyEdtLK08t1v8cEk9vdnOx3gwOrjQeh3yopHYzghBdV3WCK0FGrwUFU_FFkADgHq-W8plx4EFkfowlg-VVaNck8o9VB5HwjnV-XbMS56mbhF-hMqruSKNuKLQfrPD9FSIjBE8e0Wz7sx0DRsCLaahQdG26zRBhrFZwjLvMK10o-LuhYISHtuzgmkCFuPteMMaGdSJyttDqWAbe43DqyG-4K79cnDiiHF5sF_o5Xow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR7kJKOm4BrYl8Wc3SrHxMBW-iTSRdcC6Ynz9NMZ8z0trUBlhBgV5-w2i3xqdw4WFKmhggKTKYAjKg9nD4MiNOQ1-1S3ZQMJXQ8A0_JrqOjjhjqFmNPW8eo8PG7oiyhbKCW9YSRQGB8JeTlYcb5LrYaEj0n9kErC_BbBpcPLX3eba50ENx-yaQOiMvEAUjYTt4zqwKVxZ7SPd0K4M57dVtJqoOMYFn5k-wZmCLGqAnikvzphXQow_1QYrHLNRQc4EhRp6FsOt8O7vMMpDrUCUgouA56s5Q73Zc8Ba72nu8dxxWsfMFCIbvJhSR9TNmeAjBab2AeobpadfPTkTjtQzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5sgaOmPj37CBxwHRA2DCgcpkvrfyCBG0enXLvWixB-lI6Mx9ter1StdgcfMriPG-kqKZVnbvxXT7jiF27NM1n3oKKCYz9PdnUIUjpcel1_5E8yb7PL0pGAPrr8I30YvrQPm-Ga6Wa9XaT6GJA_lavGqIMfUAVivnGP94nrshWj3y66bW5ezMgpe7D1m_A42laJsH_JGWzyrWrnb7wxIYMEflDqevXC2M2VMJs4LIM3-F6TDK8hePexBwY8wkfAuVFDBxOetn6sYu4JYuMPaALwvaDs2YJSzvpkSq8DdKli4nsnsWkPVKyeoQpi3U0jt1j9XrrqiadDKSJHKbKivZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQFMK5KYbxvqvQGJJzLMD9WD6Ixg125SLaLlNiOqOIhFm2GvFnZtT4xnBGu5JQPiVUaDUogG_JhXb85E4IjNcNmkFY9lguA4aId9lMmiPJi3QA1ZzzOLj8vLpl09pDlIr05hRZUJHzp6hD0_P3Sr2jAvnl8qe4HMN5jPz5YX-jkCSl7aPUu98PSNk7S3fFJi2IiRlgPgM_akLEjTgupcxo5Cf-fQsYN_lD8Xx1BQfqx9degm-lUAfdLrlsAuzjympo6gYbguSqUKSApZOKfIoQ8RIGZvadFEOFOuMV9pO4kifN_NLg1v5pKFytCYbuL107d5YXtlO4yw1bMw45g1lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMI4qpyzuO7fHcvIBWgX8XahURKRzSNFLVnxUpUImLKdkwfuJQS2erSUgbE3wGGWrwflgCwCQBWgrRBrzwQq1R6quJZk6ltIpztHJqGo4-x2bu5ZbMfRltGOVLUq_4FuWAXb3hW_0PLFIdc0rqtGDG9yyoXujPLIY5oTSzfHC9Dggn_1-R8lSWP5fV7UlPkyCba-5sgSrMGjyqowsOuDSMfkSdAAxXrW8JTMgbHdDuw_7WonYFyFBVy1jl-O2kyZOp720ObQFXvDat-WdNjUe4rCwR1Ze-6iFaKsB99kSFGNxxYGb9BloBpl34gZkbw84SAgcoVzT8lXewk3oEp_QQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFUkGN1sgrsitZMzywMeRQf49Pjgc_g-W4Ll-h4xSJx5CRfLNR9DAl-3K3ElZAYHzbp2-pX9kYZTprrUGZIz43CrsTXgVh095Z4ancj6yU2dvZhfD6ApitWiQya4eTXu-Zd8AHDJsZlbNPC01lrW2YT_2HvvY87Fntc8rVarDHEhV_dN1aBXQnbuQfa30EfXlrgyO7m4WPbdEbgDH-bHmbzrEOD96JMftCaN-tsjIHbYPPLTTf9bSm-sMO6aU2kaWVk5b1ShdUiRas1ZZfpkPJQS3VJpyBAiUU8Vvj9NlOg16jbTOprC1yq6zcnjd4_mYyvqzgBqhbX-QfPCuP3w_Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=QrDJDs1Rs8hb_f2YdvNzuPma6EMF0RzXLNV9HvDBZ9QY5X-_TvmDldaBOzVn8MLMkOVwcISBcWPcuWCQzu33FALwue2f_sVKRlOvIeJzvvt5XF1W-Bnykxa8Y3QWI8UHHwczC5xaPvzmZqGVAREdxjBsGQxXriJU9tt2FDj34iemwj7sTDLVxSjnVCbOHaQTajU7e8fm3maLWg0E86z0aKuGnWawr4a7L_qiWhbx-9RN5T9WEVYkslqYzlHseG3nday_tjIoN_AX_ypKfcqrqmFA3PLfkKB-IqhSvbDdmC4NfqD6nxzLrx9MwmFcHFe420XPwUDrQ_uXFVBgL_CEwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=QrDJDs1Rs8hb_f2YdvNzuPma6EMF0RzXLNV9HvDBZ9QY5X-_TvmDldaBOzVn8MLMkOVwcISBcWPcuWCQzu33FALwue2f_sVKRlOvIeJzvvt5XF1W-Bnykxa8Y3QWI8UHHwczC5xaPvzmZqGVAREdxjBsGQxXriJU9tt2FDj34iemwj7sTDLVxSjnVCbOHaQTajU7e8fm3maLWg0E86z0aKuGnWawr4a7L_qiWhbx-9RN5T9WEVYkslqYzlHseG3nday_tjIoN_AX_ypKfcqrqmFA3PLfkKB-IqhSvbDdmC4NfqD6nxzLrx9MwmFcHFe420XPwUDrQ_uXFVBgL_CEwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-jxzpguaIFxffx0ooivC-cdVyEec__izBySYsaLSutPZKtkvtq2v1qx61L0bTEI3yoJP3BEqJWqagMpyJEeuNQJJKpO7dE3owykEVDoi1MQpsbAlQD-r83gNJsT4UJFs8ZTjRT2e174L7rR2CTy2T4lDoiq4pNGX8FaUEzfvuVKMFahlXj8QAOvHPUdhLozaNB9ZziWo_P9ixUZIUxu7RFzGPwX2smeIPaQBSRBZDJCzjfKFkoiIZ0p_skYFIGQitIq6NTQqCnXo9JlxNgKxM0xQzi1x4iJdw9XMsc-xPazKChj40HrQUSNcqycjjc9ct3p8x7cX6RZIeed_B9B0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Unq_Q9PdfV1-V9JwawWRUI_Lltpb1uy1xmlbfZzSE7xHM6nZ74bNwbEjk-1S42J7hryX_CEiHFzvIvtbSRPl-nNMTPIjho1ZMvcrobpnK3xDbl53bqYvza7JbXftiZe_Jn_vUgLCjPSY642333yn0fybuTLqWCsZgr0bmOu9vaN5_qYH2dRckvMqlkMLvA4jp-FGHXxrnYS5y1j8nWU9HUz2rowaG-pWYGhFH8O3Ci93b6Q82A7HxHJlYS4msb2bKrU3kE_P1FQNzYlhj8ZQmMMQM2tXXDvdRkYCpj5VBHm7IS8mKNk9I-ySTtRl1kb__WSZpjxRll4MHKSSof1Ozw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNV_i7ftSNuHYQ6wf5-3a-WLiJfDDXHwQKNqNckKpgNj0jS-QXYdp2KnG0SbXfY9c11kMwIpKDsqlNsALTWQvYCpAb8XTYJAYwaikRxuoh-MpUl3B88FS0PEBdgyBWpUlytFSdjr6O0oQxABJ3cQb6lOxfANDXuB6gBR1AGiWffy-o4nMGKnUeVpGItbnW5-oNvpbOXWtl1pCd4RnXe6aDE1a_dWGkliY1JK97Eay4bEjhP-VocWCWc4PIrUhaA1rz0awbrW5_kSl4QbSFVRZIdobPxxkUWVKS_0kkhmDWN_GmrJGcTFif92aJrJ-Yuz9PvIxxrMrktcOu1HFLD5UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwDF0H1KtbaI2iD79Y0X_Ie98cYwX0lpapo4ErNCuDF2DIIcBqZQ6_bKdsE3Ok4muq-gbWiP5cS4ArlHde3PV6Meuhq9k9ilpslOwoWefSCw0teJu6ZPcVi-0uNZ-qBtvyKFt-GPeNB-t04qLWEhkHcR863pToQFZbpX9LKTorw46QgU4Hg0U0pmFhgHHYY2YNRtCwO3Jt3irHByOw0s_tO9WwXmatlJwRzCgRKTX678KybYLw_s_ZZOL94g1qCufOcP-1364dPYIzg9YJmc4vXIA_qfSGXpGMNzok7U7s2JpCc4lpAAGy1DPJKDUo0bkrZZKyKcnMouRZ3695_tZw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=UGl2KBJD38yVtHimcDx8PMbSRgHiZsPaBxebMajqk2vqhbsewyKzQAKFweLRhWO87yzKYAD1j64dgXr2CyQpL8RQZaMW4vHbSsEw3zI65snrooRKK34n6TSyW8eI85WkT7VRyHkgTUjlIxFM-pvPQUvJiQKRtr62fpQn5J5wZN7Zv4h4eaEhOkJcuqDfLButjqC9p86mUozpkQJfMMHZnh9oGLmRkwMsqDfRMOKLKPJCilgDQNP75D_MmFqm83VAEdncI6VGmQkqp661haaDSRUGgdQ7YgXJuXNW0AmpL-xoNNPl_Ur39kyyA6AFas9addWSZ8kS7vgKnQb45ea5yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=UGl2KBJD38yVtHimcDx8PMbSRgHiZsPaBxebMajqk2vqhbsewyKzQAKFweLRhWO87yzKYAD1j64dgXr2CyQpL8RQZaMW4vHbSsEw3zI65snrooRKK34n6TSyW8eI85WkT7VRyHkgTUjlIxFM-pvPQUvJiQKRtr62fpQn5J5wZN7Zv4h4eaEhOkJcuqDfLButjqC9p86mUozpkQJfMMHZnh9oGLmRkwMsqDfRMOKLKPJCilgDQNP75D_MmFqm83VAEdncI6VGmQkqp661haaDSRUGgdQ7YgXJuXNW0AmpL-xoNNPl_Ur39kyyA6AFas9addWSZ8kS7vgKnQb45ea5yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQWySeY3nA-7YVApNdIPbxnu2HiCr5-w56Rk8EoArpCX25WxcUa07uuWA5HxXYwua_S7k__0JxfYXEcPE8jW92I1RPTtGNjiaMSBVfHz6kOlX_HNMMD-ynTzh-aCOuZckSuEfX3dXDAZsSO-u7GewZXxR1OWDV0uDZNsnOHfTpyP2ernvqqekFD2sHzCCnDgEezw6SxBfSouPjkvvgMJ2P7kSHjpl7r3yKl66i9kQ8YrgJ1P1gIT9j9EzKBRjPiZz8SuDHb2HLsC5EAGqQn1pXAYfvd3xXL0ublCc396u0mMiMWBTmaH5s2_pyOT-5fiyJp30_X4qaFvQJasO_oGlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cj2XmezDh8ZEKcQZdLybuPPH8hAB5vJpHr4b_mkT7-ww9jHBXzTRCDVUoFzPc4A07zXDqBfW416RG1WHadSblVObG28bgoINlyJvXovaLNJPvg8381PxfpieHBfAKcNo9ujO_Q7DTvIJy2aVQVfqIB6uaHUUlaK5_UyRsdNwSBT6yUDMiGX8LBs_QIGSbvtqHjQhTs2IEJRBzLxkouLTzk5wJy2UrVJljE4yp_j2iDjF3IIsJ2OUC-THqY-Zjs4SA3SigNgc8LnCP0d0mllRcJbtaHNtgM1ddzhlf0B0sqANLHG7qKqvG8OgE68aI-zrI8plVqMpXDcUScAdp0JMSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjVYPlHikWyzaoCZKXZmxCZs9uA1NcvBn-weROIyWpM5mSDpfP2NyWCKhxR0W7Zt0jeQb3lZIqnS0q6hnTe8-hQJTi1E1XSeBcIbjgz6dVitWXNtMDiXZtJd5w-mI5B3ARvSnb16--bmG0-JxcFn9ldZHP99P0er7-XGiyd_pNJzlU304gK5oKCtLtuyE1LTqtZ0KnJ80bXYKwzr9Kt_9WHeFCDKK3Yb2RJty14xuX8uU-DVj7TA_GDEnjmwqtoPKUcO-e_p-QN2aAQRJdDqJyhtoKjFpDcD0OiM0CnDlqbVaSo1NxkA-W4oNnYiVNz-Jk5bIsu3RYcPhOD21N7arg.jpg" alt="photo" loading="lazy"/></div>
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
