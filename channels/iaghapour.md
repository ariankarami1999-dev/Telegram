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
<img src="https://cdn4.telesco.pe/file/W-TJyFJTXie5Tcz0uOoMAw2_0cTPKMpDQ6mEMK5EnOpvwR_9jjzstwlffU2-Xuqr7fUceJyjDBKSaM_KP25P-JfE6b-jE-rR6JJnB9oLmaO7Vf7aKHYic9kqkDiUgTZ5at8wPKKZvvPzo70zyP_rTcL6RGAZUjRK-BE4tTPldBHh9BosZUMJ1oUYDxhb0uqC2z0nSazlRheyOkgR_uUceRq0AZJixxedFv-u-PVGj-QFud_cN6_2Iqkmu5g-GhxZc8TFtnZB49fl8B6P1oYuSeN2ayFwndwIs-Uw-aRxN5f31tsCMioXmyjXmDgLU_Nw_pH72GhhDwDA3gopappW3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.4K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-3129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهاستینگ افزونه نویس</strong></div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/iaghapour/3129" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌ تبلیغ‌شده زیر، قوانین را بخوانید
👇🏻</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/iaghapour/3128" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/iaghapour/3127" target="_blank">📅 20:10 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/iaghapour/3126" target="_blank">📅 18:34 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/iaghapour/3125" target="_blank">📅 16:01 · 21 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/iaghapour/3124" target="_blank">📅 21:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌های تبلیغ‌شده، قوانین زیر را بخوانید
👇🏻</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/iaghapour/3123" target="_blank">📅 21:00 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/iaghapour/3122" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/iaghapour/3121" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3115" target="_blank">📅 14:10 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/3113" target="_blank">📅 20:36 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3112" target="_blank">📅 16:10 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3110" target="_blank">📅 20:40 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3109" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/3107" target="_blank">📅 19:58 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3106" target="_blank">📅 16:44 · 16 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuwh-L6t4kE4q6YhMx2Ey5uo-Ezj0BeuajUu9M6Puh_S5iKTzTsScIwroAdyIqM9S2T_hBWWSxXn61JwWGUYZ9l8gNGg-UNGlvpCm4A_GWa5pXpecjAcmxEncl9tEez4shvZhhnEEO8vk_VDQqkinCBF2mhIOYh1d5kGK5JzBht78IobxdQ5JxTSAxiK33Q-UoXbhdGcweLFnHBB_5thQrKqXqJ9EUGHHTV4Gg9SSgnmk7TFGH7xM_NWMEHKzCmBBWltB6dUSO76TYq69qTZni-DJxi8OCgWEmG_-JGgLh94qomdvD3tsKfJ8luRKowC0gHm8xqNLwAy82VXLc9hpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3098" target="_blank">📅 19:57 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/3097" target="_blank">📅 14:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZBfrLWNAceBEy8ridjSSHCP0GJf-9bClpYKsJZCKqhLNrDKumsshcE8gNar_q_YJQyQQOJUdqoUqGa-vfQAVtiSWlnLitjOT-_klvotY_16c-H5mhXHKl8gTOu801mxmjqTLmPdydk4Qw_UkTjCreQ8LZXfC9v03GN2EmuwfJFTBrIVfCCizWvFAlM8B3mSVBH4_VTXf1Gyz9zzNhM1HwqXgYdHmLSHz7vvak05acklfcrPIffvMrvOghsUdq708A8txxpYaZ_AiCFBhMt9uOUTnm0-BXpKLq8TIsGD0mYr1dHXj_sTeC2zWhCwD-cttpUwiPDK96sEyRYt5-7zgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayHmuWy2y4DVH_r1T0vuEqGFfjIc0NIOX9nKTiKksb5ipZJbFVpdCa0OlOIEmn5zfAmVEHlRnNnrCA-uZZqmJ6fnMpZyJA5tcHqiAsARFgWdWAbJdfmrQtgKLrClh4fBrkia3q7NUl6x3W8qACZANgCzZc50UwWMyKPDwogx1i8kG-GlDQqFLTdQu4IThWSHMZCm23gSrA2IW_-JK1OydSCq0nCPcP4--GoG-UR7QheXXrxj3uARuVRKEGW-Yc0itFbzteGaEyMyZ9Yb4C5N5mhGjblC8ieRAopVDfwnLl_jPafotzWJB5Gck8mFW_6KkrrvKtCqWrf58AfPVEE_Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/iaghapour/3094" target="_blank">📅 16:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVTmNGvq7WClY2qnSgjLhFrMkIHA4RCVty7t7fC2wUSrNi2b-NZWWkNDwg3Wn74O9QSqHKVAdWbHRacDapaynD4VVupxQ9yZDej6c_53t-4BYVtBUAhTlvFIVTcNXwEx2W-rSd4oMyUcYB1cjJYoXRx_6oVHqzV6cDqAJ5ORHN9YA2K6r95zZIhy1MvsVej4qmHxfOHomMdmgPzoQVEaf8hU2rgATxy-DuwI8drYOiKTnw4an_U4-LrIJcbWQCAKnx3MkpQ9KikOmcZjLiOaDGzD0XSYcH6Y8FJusnTn_CVtrfgdWVGpFQ5F0GRanC_mBsSzuLIHEJgikKI4va0aaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/3092" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHzlkhXMP-_XvzGn9NxPeHbqUAKqXir3WFc70gIuCWrJqn0fbap1VXBM12oVSZ1uDfsNbBLfYOLic-OPAx94LUZG-PynvsjjPMld2w_vvJduu1aHq2GzINBD-C0fD24SsVPleyyrf1WSDmLtYUroeKut_6pd5c28E4GiCPNUlwiXlIcPt2h-g9aEUyfBUqk-02OccbTzghZSATW92MlrnFLgmA5k_wyVj61QSFsMhjPDidp3B16J3Ncoyg3rpjYx_QM0dgdruE_-kaJ1ozOly2pSN-pd_Swr0oY3ut3qPd8OAv5t9tNXLXsSbL3UCFEpEykMJAxIUSov-OikrSwonA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7verdE7vM7pXE_ALzl2sE0pwVPR6Nxs2unsPCQCWKxIO38jLP0Mca5eEMbSIy1MJyPcvUkjR_LZBG-hetm6jKnH56lNmWK_Z2jzTgqHdhsJ3sl5T2arXuFednVXuz8LVti-OkIsdUaOY7sSWzWxaVnhMzLhs11u2_Yy71eapLkG2TyQOC-nbNF3FMpD8J_Z3kG1woMzGvrwIPULigN253TTBmd6FNqcJxmYaHbc0DzyIn3Kg0ZEcSLtBt73_PvRXz6ZiMaXpaWtKgBs2-Okipy0szw8Hjzqlr8lX3obweT9Z4ZaG2Ml6yAsGcUlJi_Rho-u-2F-3Qg_9P0FMwTYSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljpUGcV_XXDVMzzDwIZAkWVBpIgur7djgA1BBgJ01DGhD31Zj4k_kps_K7QikXI25J4IGqcUZ8VPaTFlwYX5NY5AY3OOlSQMY4ZMc7Thm5QwCmaskMz9TbAcdyyJO8T6EzNjGodtCJwX6ooiHRBM6razF5msGzARBslOtvutkwfQvcmCHoRdLADlosRbdySGj8T4IeJPnPYItFZQfr0IWwifdUrJfWxEm8qkIGs-h99X_PF6PC9ibJ99a9bGVt3ioa9m3pe9dRLVqSdsJmo2NSJiJkYOya_KZwgPbOfLGmDomTVqiVsbiErXbeQkLzBCjP7_tIs5UMA6-v-3AtWy0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6apClsOnl6XC9nmJMwG1Y9zRxURwwboGcd3SXCDkS72nZUXaxHawXMxSr8ExGzqrcZedOtm8eJtbiiyQYgFLetks8s1L-MIDbWg-uXAGJ6fsHoqsNIqyfwSJNkqek6Zzn8dCfLiogWyFDH5rmWZIz9pRkWL2sMy4mG92DYbpWHW92xXX3KbKL9eZevRAsW8EeRMr8F-RshDaWeczh6hf3MakvgSg5sAFT569f5hMbuaetAURITZgz3QbSY5syGNuhKt94Zbryc1r67xKCkO2WcItmy9H51rUaFtbzUSOPyXanAa2r3rKyXsV5dQPn567albw-dF8FchEpblV95mlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4XiJUyjQ-ZI3-4XbrISRhOOjn4Q1hzttVd2U7DuNLKrkwylZbEy-4yl4Bf2KDy6INWokvjmNZvrnn1_sS0n0_C0r_aPQEf78YKafwSI3Q8wC12_HuTwv4CkjRgpI9mPJISMGz3rOz__7s3sV8BHhcX5NUrRW5PkUzl5_RZP3C-NPPziOD1S4W2WJnO9-ASNHNDkSLr0jjo0ltb-iIHMZ3ZwRpMnrbp8mnNN3qxrDJCGwrmQFWAP_qfVy7C-9SNEzR6Irqqpo0i0O0MbY38_8jidpmTWoGeHT_u9izixt5koA4ESnXRJm5zr3IfHkr1N_UgfUmfMmmF-Oe_BTDFd8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/iaghapour/3076" target="_blank">📅 14:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3074" target="_blank">📅 20:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3073">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdLGFaSbSOfmOBfYGe3LZM85BZzqXL035_LMiKBowJgvVkmzaiEEPoe0oEmTnVUD29jVakUVrH3e-Gvk7nvBhKtwobOvtNwecgcQ0zvla3fMhQeZoCQEP1ht1iw8CuBsM9F6YvFlEXK7EhQhMOks-CrIkFe10Cpp7MZsNeSPt_Wat5mJcdaG6JOQjnzCQ7zxcQTG7ExWycYI6HV4X0na-HLg9UacMah7Z69vtBYXvz8rkicampYMhGZwUvl4eupZrSf6O3pGRLKwdqyhflU-osAKtORUPONt33UFx_EITexAGExLN-B_WrWPYce6sSqLhuNcbQ8mxjG3Mr7EHARbDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/3071" target="_blank">📅 20:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSyyrLQxcAA_ezbX1KFMuCMeG6A614XOS7nuMwlzLKSUGVHaritQmqQKPw3PAHCGzXRu4XNp-peyVvTDiHRA7Zn4xZ1y5UBJ-pFWRJ0iDmchVdGw6Wz2FgphGY3IXRBQPKhh5snNkS-FD4pqvpyVcqSir1cc909z1eagUTSsamkUaUKUdrBE9kQJzGyuYJFLKU3HvUUBnEe3OD4IslTRmvAKvlOAQeNVR9i9xBVWu_DKHq80bOc4am-2MF6IUKWYQ7MUqY7Q4GBU-Csr0AG3qv5KwMRVJvDhiUEzTX-Dgg4Ka8PEy1r6I6fOSUYJrP8yrhVTpaRVlkZ0xYcZlYqGRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlR_ts1ds4I_0EerWfezxRJYR43t1klQb5b4Pj_dGrpoGbcyf23RQdbxqKt3ROKM0QOtB5B38jmAoKQ0L2TGok8I8VQQWvhkQfFjOdwpgbA_77JjoTxho1JBWmGJsKP424i2SWV1SsO9maSWrdFqT6vZC3dcOlYXfTQEe3NlFcdeiP-BcZNkBlHqgVLeBme5YYs5jyZO1lht4rI0srFjNEQjC8bdhmYFUZ3UdJqCFRMJkJiKjRbUKmipcH-gUcZMGov23p6WcJtW3tC78pfWXhh52HTNJGqWA7QX424uJP7JbklB6kF7Uxmcf36BLc9gxVm5xdBK_s3qpLD5mC-1Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/3069" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=Q7SXUGFoFJRosYJwCwSrzVRafcXPj-fEiBWtAYtxvlvfMrF6T0mGRiKdyjER_UoHRoVnhjovAJUE-cVnYLeNKweji2P6mh34IN_LTcYndFTSRizs8UqOyw3WSiYr6UzkJH3_9spxepB0lje03Y3mynvPA_wNMmP-B9bdflx0awOKPE_9vFIIE8S3sYQGMqnerPxnxNP5Xp4bf1-l1i1nkkL5mk3VTGgxpu-a-sm_R1OqF4x6pUFAM_ghq4NzdO3o7uqMXo4s1sLrCr9IAkRA69qTzQ9ON5L0NMCCYxE7fbqbBueIW4bQEdCYZ_mHPJ-pOmEnCMD2nHjbtb3mK_22QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=Q7SXUGFoFJRosYJwCwSrzVRafcXPj-fEiBWtAYtxvlvfMrF6T0mGRiKdyjER_UoHRoVnhjovAJUE-cVnYLeNKweji2P6mh34IN_LTcYndFTSRizs8UqOyw3WSiYr6UzkJH3_9spxepB0lje03Y3mynvPA_wNMmP-B9bdflx0awOKPE_9vFIIE8S3sYQGMqnerPxnxNP5Xp4bf1-l1i1nkkL5mk3VTGgxpu-a-sm_R1OqF4x6pUFAM_ghq4NzdO3o7uqMXo4s1sLrCr9IAkRA69qTzQ9ON5L0NMCCYxE7fbqbBueIW4bQEdCYZ_mHPJ-pOmEnCMD2nHjbtb3mK_22QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzuOui6MBk3sTOygU8T88qdlQXA2mbhFDv5ywgA-w6QKDM5d9Rpvic3uzE3MtqsQEeC8BS1_04FMhyD5qXhC5MAnH803AoXzvpv5xi99ZgoKNK8dOqgpWl5jUXYrBUber4Q45NQvpw0lUynxofNtGWH-r1UMediOSJMY6p3ibhdNUvCaa2Prj9AhtIcASaFFyegOz4KLzkHX_-cD7glMOAvD9LcvVRSfZkJbBJd1UaQTr7tfpcfHxLSjgERvDB-_vnfEaHtJZs-Z9FUc1Jt7Rp_GlEhm-cx4TjE7xBuzb17fwcV-tlTuYHPorzR9Rnmmk9RL0lwAcz2QeDxZDA4G-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csyuAYufH1zFwtljNKkXngxXWnbwCl0vSU5daFsnBozXONHr5LjirHvyAWIeUoaan_7s-QLifPtoKx1S_2P6a7wbGDB1G4pOn2maiBrCT2dL2RT9iC3saz9urkULF8hkk3a9E9ouFYraSbosotaQYfCTb3WjuVTCN8d9oCBZ0IpBLFk7J9FtLJKVrsBfi1g-BfvRDY5UBut2G2nF1galu7bsCdnTJMYr5ZTdYDb8B3sbU5123KcohY3MXRdFgK-DIG-GCa13zsuGuG9bpAUOtrthB6Mh014EYpwXnmENzB2payYNFLEpfPOA6FzV5tRyAQUa3v5aQSJ1kU6qrq0mhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3057" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c73BgkLCqxT5yN4YRRG0f-m1tgKl2in1hZpO8DjHHttercRXyA2yJmC05XtWKAMjxyMFRZukW_A66TE-4GPOp5ufqGmeWC0m1qU7ZzN68eb0J_e6QFmkrChCZkG75xNdsT1B7Xyy8tgRuq0FWmI2cu08pqQ91GCn2zDxOSgOo9YXoOihIc2fxAAT84uHSbmLZMPyEzZetieACRILo9sTh_oC8h2mAOIq2rl_T_HFv9_9QT2_r27Jx15Je0tw7o2NhMu8uC2QlrPNBBn1MpnuekSw2PBdEqxxcqARCgym-rMn4an0gIWPZUfa9mM_qqlnMgMGbiHnuwYMfhQ5Eh8YNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgJyWozlugbRDL9V9iClS7icduVxZ65D3lRipZWp9o4b57TakaNty1ZwJtGmEukh4OQKtWkAyPlp5flBQa97uciDK0cCUWsngwy1qGlZ_BgKT-9wHwMxii4n_znThfLB0dr2MzUMZoQ5XmUMaYf_ZgxJb5MlQPDnjx7SnsMVSYt2ErG5GspisnsSpXJ7oIMx9wjItcicLmWmQzc7gsTqzetJCkYjPZlvhf9rxcB9S4jiPqyEVxtRrusOcnjEHbeqnP_UwoPTBIl5X2JhPM3gWwcfNqMdbxArrR5fkspOMlqtMk74E3YIwcQU1RZZiM6TgZF3razr51JIsDx-BUv0EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7uZuQkQnA3FtWvpaauc_5y7pkaQct4lssU_yY1WLRmnD10pcDdLQo3YzqaIhrPMaGbigtCXRXilHbcjWYH79gvjbyzJv-_F1DkBIXGSFAQoBBPiUFU_WbiUdrQ76q0CZFxJEX8SrBAKDDkRtKqCM1wtmthYjTAjyjASCEkFLYgyvMIdkZ4iHniYp47Cw2RuiCoRHjpOxFjZtRvunREFw8wIeNmOhY931nk9UouBMz5tf0m-kAWR8nHpBDJHbraeBEeXIznVEiRSXR0R4Z0hpgroyZQXGeJUV4tLKSBkf7LzpNbqFIjjcup-iBSIvds4IsTVa7rm2qN5b8Ohv4ipRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ39IzaAaBY1Ai-MQkgw1zcJw_SgWju-9E5SdqZ9iG359xZKzVf8qEcJe47Fb2k9RMwuEj9I5bBeNDyWqqT6JjdXMYbye8W6UZ4a3VTndVycrg8fTvgdr3LxNpbPziBqgv_zqFimbNEmQ2Y8aSm_VtBgPACqUHsFrk3ubLY0GxsplCDotbLg3PooiY7YCdCpDA5JQ-pbrPPCEFic-tgXRl5aZDKGxGIPcQeAMdQVLJ9vWPWDu20j3K8e4irO1m8fl63mkjnTCI_X9iCJhXmCoFW0LuHdjAMBt24g7dm1pNUiQYx2S9NKK6TKWHr5qYsr-y5dyDpRxUeLy5z6cvyI3w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=F0h6u8X6ABO87af213QchEHWCOOQKtNjdtdrYWur9tNe-BSn82YXGRCPnRu_g9OMWSUPByA50sivNEq7FaFMEW_iuEO7xpCtGuEX6LaE1TXp1UsOcYYBFFnpwXZ2BR-lM1ZYM7d2hRjOg00stEtZr19Leen_beblOX4YDhxc0npnqc5uywabN517qODPPBQ-d1rQ7x3nlIu7OZOAW-U9FVRPbvyTD_X5TCh7jZdggtleSSAq8UidGK1ycNbB4IbQRObG0XjSbRxblPUlsiLRe5gMr5UBwdVBrdNGaHvI80hoHKto49uJGFxfgI6rZpYcy55l7UhmSUu_u2D3yV6gnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=F0h6u8X6ABO87af213QchEHWCOOQKtNjdtdrYWur9tNe-BSn82YXGRCPnRu_g9OMWSUPByA50sivNEq7FaFMEW_iuEO7xpCtGuEX6LaE1TXp1UsOcYYBFFnpwXZ2BR-lM1ZYM7d2hRjOg00stEtZr19Leen_beblOX4YDhxc0npnqc5uywabN517qODPPBQ-d1rQ7x3nlIu7OZOAW-U9FVRPbvyTD_X5TCh7jZdggtleSSAq8UidGK1ycNbB4IbQRObG0XjSbRxblPUlsiLRe5gMr5UBwdVBrdNGaHvI80hoHKto49uJGFxfgI6rZpYcy55l7UhmSUu_u2D3yV6gnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1WmEkHlJl_jGytV6LgOixsoLhpA1D2pvsz5naZL5ZiNEGI_tDTn3hZy6XKb248C5ICtqRHP0cGN9f2rsSj3evfuH8ALzp_n-4SRjm5NGHUg8wykPQUZDaB5VoR7S1vzbig_C5YeaCi11P261b7F4uYnsMkMpqAKhyfNryY3U9BxADMmwaLWryQgEfU7UeIlZSLMyu8tcz6BWSmIYXYymH37ySWT-SqsS1ap9zXJRhyFZb0KFXq1nuR61JC0ReRQRH0REyFH0jcwyHBIWxMI7mZL6inqS3wSv-vzF_MSxnzHiqEhgeVMyMR-p7bMBwlEQe0iw2jI5layE9uiER98LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYufklsDrWjynCoPZOzFamiQmAad3284E0PAXmKuZpnDB8udC3JoeAwGLebpcWGMmQBT3CH79xpgUxA2C9RTJdFhV3ZGUtkwwdrYruogHqgpqYizGzmE40lfOYXkAsIPqNR0usXHzqaPfg9dITIoK9m3dA-GPdZzVhFL6x0Jx-aA0nJV3Acs3qee7EH26MExFLsqa_hyfdTeppPZAOlFAb_ZvqSsWDbE4yC2IvBX_LnASYuiV5gIqGS2DQn2bARmUDhQzHFwYCsUqeOQqQxh_rl3hOibhcZ5Nqa0rAZjxoY0aWTZ7zX6k2hT0Jw71SA6ypOd3v3UIRT3tzhc2wDTYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6_zJebIo6BI8Xo6xssrFkXbNd_eCxHYhhk5gCtxwas2aQaBfd1k7uc1SQ_H1Bpwh52bHEzg77AkJE1UpS82kau0hL-T4sVBvKHlQ_-NYvRyTNiz8JWc-mOifBpAePs8Drb3xbZz7UzE_7mVCQwkhLtHNDkHpRSUpnytKNld5J3i3ZzYcVGpCmxzufYcZVl93M1L87C6FN9y0HoY7lM7B9SuH1f5r6EpzP_D7hy2fixK8L-jQ9Tfimu4cEVbHDoIEgJz_URVw2QUlckCEd76A0qu05hiXYDvZaPhEP0Wy9IyRbM34_2NcOarPSfqXK_MIsYLQ6q0lP1EBFol1RrgsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddkDIHcm3RU244rzrEUTqQDVTc3p3N6U1KRYN7X-EJ8gI3tQ6snuMqBuWUqRa1kv6phv2Giz64Z5GKwuMGfCRc1dP8YxCc4AGgZ5Fvg8pTsnAciVCdF0KYBpWX2WLr35LwOAaHsIxDgrP7MKfyqhbl5a2I3Pn9wVidi8M-SXMVtf0CGzsFOjwnncff9dZhKpUmto7XyzUgGUrBdj5_HSzT6b_r8bdFkw-3SBRHGTrAxpWFR6gGAUDzJULr58kwZBRga_vFZIM_El10sMRGreekzOE7VR-DYG4hMmylXWKv7cF0rx0UiZtnZad2PM-WqvVL02VHO7vpHwgWUxvd-xRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-Egy_4bTKig_LiTs0Sd08UIy5ef3pWm5AD0WSIxtDS5jfy_wluXO9Pq9cR56ei4YPcBqRMrTcE4TgKxurJuBrvydmiYMwDhmsdzHnaFDUlzeCjTdfM37yUoM2kj_ii140QqonigVOgU1esQedmMg38fz1x2c7mw-xqxgN883Nv7SiPtwI560YQ5Iy1PgeG-Bftwg92Tim3yJnYcRM0InLbMCK3048kNev759wpdbAx_EcHwZOCfG2TYLIovIozpDquqqu7FrhuZrrrSBXoxjCIx5OqlMWaBGGrA1zltNXrSftq_R33ktDqLb7ur3kNXL3ARHV6HFS3TseXy3aI2SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h56EimD1AELdNKX1HemngBgchxYUWXTKy0asEUgy3eGPLjMBg9DAaUXzhoS4kxtGFsOFA7hCt9Rzx9WCb_aS1jUcp8bQWEq2tkdwKgoxrA4QwJUh32eMJpAAWO66e9Qm4UO2aFeasiVD1GIMSAwf1esdbi_5bk1cTGGnd6dPXryybS4s9_L58pYkcvCQAcg3xYS-PwYpyG0NqdjBb8Dwpoc3u-xBT-7TkG96zZ6jS68xuFyACbUon2gY5Kt88Me83eOVitqmWlkeAP5uWTZI3F44ugFTr91FrLZknoUhhrWzvVwX9ILKx4Fw7TAqDQO6PnGsE9LOncx6Z8bFsSOzEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViWVfFOliEDWZD8q5V9osoGklFvlgRV905CGh4YK1YWWtCYpOS1xINy3EJk8NQP4KmJCd-kH1_LQ6bsB2ZYr5djeDTaa2cRPdj_uIk29NncgP290XeR5Yrm8wrKcqbJXT6viyl0uUnIMFQiTIKQRcJwYoxqb-DqSK7EEnCbq2PvYazebq1Q1IQONC5yOXDYK8_QNUL0O9CYI-EDhOhv9aYIskO-wCkxttKPTSQJLX-ZW5fDViCIC0kXDfivftXYZSwE3JEzHi4JVeQVIKHjZgz8RwMQDad4n809cq8c8nb7TfgY4bwYKNciR3LTTiw3LTxfwh1az_Hi3kN5QJRCeJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_0D_u3TSlkSU7ELR5IYDpkqpDyBlXazkDEApYfTBTN8KHQBSMftgWSprc8t3t9kaDYlMxzEVretxT61LijQjeXxKPVh6HbIeFlMG2DMghMqqSmbeMuvuaok5BtfwS6mBaMSKcAhiSPPDRCC0Nrjx9QgkVM4P3C_HJZVOcpuIkZzNa1p3_mRl4oK2IEldst41ohF2qVrRn7s9Fb0BdY35wvmbSEkO080CQwmK48s3NwUAtDqfHua5Yub6SzLUvjP47_eB7VNt-qNvcepXcj-nDXu_Ds7fMHPk0ZfhmmdDEr96rUG59zznRlEHMt78fNO5QA4PGZGAUnelE_2XrELJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvTvjrW9SUkk4z_F61TrH0mRmDpRjMpG4lPXNkyGhk-CBP1J8CwMbvbdaU9aP2sOAv5oYdJvtU6jXNhL6ICPALYWYWsKOWUSEw7OtmFfOwUE01SZhuKNzCy6e8CsSWPPANtpVZtNiWrJQcb-DvkJtyiq6PWSG3YYREJ5yVdS_OqIjP6YOfHteYLDFLbn0QErqm1N5mfj1yxZFCN_IJaxAN0b-xHqdNelpOhNq972VHVutag5nDIQ_BRVesTAxNim-smEOTC0EfY1HWMQBgoNk6e_G26xnu8tilrOoo3TJanw7ErCH59RvfztQcbZW20GKX6TjfbGKWpEK9lGmn9oEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFvgi33b6JvcrSy0aSAiSVb9bvR_xQtJC4M1euJ8Z1aZgUD15AoTpjzXBtAUnxNGKmxuzH5RWSfmY8e1XtKX3Xidk8Zjkc-_oDx8_6Bo9PNWf5bp3QthPaQZ9id94_nrOD8e9_FwOXX67_TZeluWZnlG-Bd7PaMnQv3x2W4cde1iFNw7deBLvIc3VCJ-8aHupLP7614BX74Z0iJNpXuV9N_KkHUsyBom2-IfUQLLXmbf68LzOrPdcJW21AjY9yQjxTmTeM8SqoOEG_JZ09l1VDuGTOVSqSKrWQA0ndnQBgNYBDfwUlBvyDMoIO1xr_YqNDnHRoCJCmpKbNiXItSVsA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=qFAkE1S_3NF-wud_6dubeFxr-v3FG4N0dGwEaK9hF7Zxism_KcJ3J2QG8rEHDJDJs634lCr1GxAeUvOB6SF2LWxanqqo6qd9eeE-eP0LF2MTjjME8qKBVVeCOyk0J7VHlyV_g-JpdaeVqJh8SeuNCdsoplAIBOruTiaOnBBPEBg2aNNpI2RlGJKsw9OEFQGW9oX0UrFwY8xzhx5Sch5yWUJEG39Me36_8-ni3l935VWwbRPNF-WcYDIU-LYrQLmKowx18PFnGD341QEV3cyZi32FHg9ZcmHC4xerXD4YvaOC3hi92Nkn7Edc20jGLUrzByHQA0ERUTpsVYkbz3Vgtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=qFAkE1S_3NF-wud_6dubeFxr-v3FG4N0dGwEaK9hF7Zxism_KcJ3J2QG8rEHDJDJs634lCr1GxAeUvOB6SF2LWxanqqo6qd9eeE-eP0LF2MTjjME8qKBVVeCOyk0J7VHlyV_g-JpdaeVqJh8SeuNCdsoplAIBOruTiaOnBBPEBg2aNNpI2RlGJKsw9OEFQGW9oX0UrFwY8xzhx5Sch5yWUJEG39Me36_8-ni3l935VWwbRPNF-WcYDIU-LYrQLmKowx18PFnGD341QEV3cyZi32FHg9ZcmHC4xerXD4YvaOC3hi92Nkn7Edc20jGLUrzByHQA0ERUTpsVYkbz3Vgtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLKrm0dhA_gyI4v6-kyEsbDXVq3mgoSHesKhr6dZvNubUVj_zdxkqGtL4kKlR-iSOX7ShmFU1nfzqTpKZOyfpvUPekuJypp-BKjAtBtfyIgP_HxxRPui2G1AW9m7s0gzRd-D8MwmJB7Z2FKkKFby0LptAn8Kva_H3OVVavbVhBSXM4gV2DtBcp4DzEccReP0BROYHqKi7F7gyEKFQzlQyk1s_lXNSqGLc3nIrXPLJrwCJ3mAKjYzi2DzbPOpYwg4X8mi_QiFtluOVJWnOcjdv_7dDeEmCTDLWzif4EDDYrpwN8KychvyJxFmVX1NqaPRKEQFdqpsksnpVtrQlmy23w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzmEuA0yFx4Zb0ZHH1Bh0ZwLY7ZRKx4G9dZFH0WdVIETMU6v8Ot6Ju01193EksBN1tvAmTJgTcUuXx6MeII6WwjbFFjfbW0Ouqsg8Q-U8QdDasj9mUGPsQOVsXWZugttzTJy9_8YFLQg_6jEfxaW9JmiShNyqsYKSLziGQcuBOC3wt0Csik-WmWo0fN8KrkVgvJ3Bj8uQtt8DxCpjnsqAb2Vhv_edN1FKoK78Kcdy9bWm86OjJgF4WnvtXLAPzSwx_MLqIPo3Cvv_Q41CzTTXknpGYCPcotcuQbKFpHuru5yJ42C6ZMZg5wXDliAWCXo2Ck4ckNY5WSD2KLQYDZoFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlHyhprqq3ZVLNHCQoU3NUenI3BbDM9i0GsMvzASci4tC_y5Vx9wJvJPbGTe55QiXb50jclBD6SrpmCpegbhkbOFc2GvzggONv4wp3rDbRR1lEO0vbVCTHIKYevuxLCJu2LfKqhxc8LXuzTSYVLrzvbfmQ3Xe-bcVqkxbNvaaCX9LRqvDietR8DwTvuTR-wBolawegqPPE5uX4YdoWvYpjZcu2evIrjQgyh3Wa3MqVfkUoVNo7dAq0BEJAxmGTo_3m9XZd6IPGXgtFPT8eEZuvgYUuRzePt954CtBhZmLWuP-0Cg3YNVS0UC0WpnEZHYt3tJC5aWXHIoRxcr_A4XBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKUzOOK9IqLFw0Ao6cvwFg7XCMQ45lf9nsmKo5N_x4R_fBuOK_-Nai0rsBAmvII_Gyj46oaIcU0jdg_BVn1R-FVZg3BdvYbYAXygrU8vCQCkvk3fUkgrZjcvjB1c88YfBOh6ZqgnPPnAdSfFOTdlQS-p2ir-LSgAHsFTV4sS2UMS0DI3EYGWpredNvfI1SXGv6gg73jKfSLta6pUVMLYyaWrbIK8LGpBEGfyCVEONiKu9K8XSl9LzKXu2w9Dr2CVCFRkY0NnAjBm-ql11ZcIguRQjkelRamm6Eu1moilKLjVp5eELPpo39D5ILqCpu_9I_oFBqgAtWgRZ2nFsfNo2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJSmh-tM2F16rzyFfJNmNrkbgtdX0kWXgCrKwUmtiXPL25S7zgivcXkgqw4GplUwTgIaBtKZ8XK7L99_jIUFGn9_kk7dl_bUsg2B7HiKmJ3oh4bNNrTS9_o2qaGyaLp_ZD5WGIqbo8JAHN3WNwEhTK4eYILUugx2Zo4zLJ7j1fZMc5poqD4rkEyjk9h6dNfTZwrKnfArAd7TRDzz35qVrTPvpeER48leyG0eRycfxHtbK62VkiMba6An1q0l_HzloBsa5SnT3LMU_FTmXyjg3RyLaOlIX2sAXXiOq8CrH5_uXY-dYPk8l3QmMQRPz-3yMwV1vD0-MZUcejoD6Pbvgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7QzTOv4iw_NieDR8J2qZMVsmKEWTy4Lq_dwb_fRLauFaCRi8S0IOVoaA2YHEYC0WNObadLYRuKlsqyEmRqMyuHwkLK6R4i2wEMhYFSpNToNSq550-UUmAp2neeii7eTFu_o7A0gpxOwuU_2DxyIFjMCs5CND2G-sCJ8enocSfZKuunUr6ibw8jh3Ml5rg3Yq0lKtmLjGhqdBUn7JE8S1wsXVfEW2A8zppB6bX_aUKJwBQUhWGzrzqF2MhPgggNopVmvTFVDCJ5u7YTd4Tfrt-juYHDlLFZ9VPYiJ6XVTjwZgy0fEhPKSTw5StlBv1Xd5fsfIJ4ifR68yfDxtzafRw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=GrDjmQqeSaNiOM-nnAoXNRUqHm830BCEDHPeRbD91xZzE3K8D2ws_e20b_n7R2RabsXG1ACaRc8VHI-KIi3_jm562pd1OdSvayKDjfjlTRkdnj6pQUZ-xzx3dn4ePBOSTCegnGD8JC8cGzBnQe0dyH072HabqI-OSwyXL9T1FEo3yxXSZg8395uMA9Jhy_ecw3Q7XBxeP8heprNd_H1DMTRpsymvo72Xa8_xZ6qRagn7TPr9FsidBDThb29tvbgWjgQ_BM9uX3BtI1juz1YK9sfBn3euEqgaXSDDCKuIpn2bHTmCLt-ktqoQ6q7MEjDAa2Cl1b5l8t2CpcebsU3xxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=GrDjmQqeSaNiOM-nnAoXNRUqHm830BCEDHPeRbD91xZzE3K8D2ws_e20b_n7R2RabsXG1ACaRc8VHI-KIi3_jm562pd1OdSvayKDjfjlTRkdnj6pQUZ-xzx3dn4ePBOSTCegnGD8JC8cGzBnQe0dyH072HabqI-OSwyXL9T1FEo3yxXSZg8395uMA9Jhy_ecw3Q7XBxeP8heprNd_H1DMTRpsymvo72Xa8_xZ6qRagn7TPr9FsidBDThb29tvbgWjgQ_BM9uX3BtI1juz1YK9sfBn3euEqgaXSDDCKuIpn2bHTmCLt-ktqoQ6q7MEjDAa2Cl1b5l8t2CpcebsU3xxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STr4TxympkE_C7vkZ_I1C80zdOwJ7OWyoPOYay61O2_bfdFSpGIwHEfq3enFyFi-gv9Z0lGau0yf_cbGG6HmbMq0ndLu2Vw58v8SMOsFzxNvyNVjoVO4dTxQL2gIZA0f9vlQhKum_HlzlHXkLI-ToD4OZN5piXXow_r6_dzEGmyzPvBiuliCJW1XKTvXwoSYGYqwayEMoGgZtRbZH2YjWIvzt1coTBXd1zKhBTr-7SVTreXnlddi7eWHMEnW9uq5oBZvGpBLpgHN5sIU7NhdHgoZot6fJCLN5MHa67zDOGt0YALKBb9xMjzeM3jACGT3mbtc9RnZrdPUEjqLZHMScw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4B41HeFlHykSPd5EKiQBQ8CJ75UQ6EC8suDtZmwVSMOKxAetovKeZW8-ogHV9AqfpuTizzJG_RSVpd5ViGABIHSD_ZSr3gwXGV1RNIiRmCvt8KUGtgagvrZjwS8WX5KES7yn3S2qhn44vkY6CcfjoFxqB2YbY2Q-SGmtVfMUa3F5gzVkNXlCuiAkjvbbIVqXIVT9oc5GHLAONaUkJ6dFCJat8Aubd5jPPVFUUZn1-z4V84U88lig1Lkb08gukQQC1eVyP0UE87AeBtj7fuXaZ6CV7Uj3q1aW5_5CJYIOi6PbS9_f19y3gX2rBCknHlpQznpnfOLCjAlR9uV_140Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfdTcBPdXHiu6zv8wmKF6RMlFGPMb_N4sd493PKKs2KdFKnR7_EWPW8hU8zo6hxiOODlWLa1qM5ljf1OUWy_oL3IH8mzxch5-vKOBb_iQ5S-T9Ea8jkQiU-tAh68LMJZ2iZviDT0BT8eJsETuC6XbTQ_fLlFXjqBYyF_ahdaKAlzEYfCgjmy_ZA-q4sk-q5QmpbV1HrZDM7sdOJof3jJfVCUV_28UABzNvIdKAwnn9Lkm44F0CxdbnhPfG172pXsRcRJ42L1Ij2aakygfZ314z8yy0gCh5p1ZMb-onr1OcSllsm8IbW8S0wyAY8n9TupBi_gxmJrJWZh0xcC-aeDNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdBFcQjHKhWlIi0NyAa-A5_2Hiu4y90Ozc659M4NlCbcaIj8XSoYmiYKzkCTCjgAPSvxAF6I4mom_63b5fdMQ_PaoN8HbZdQ_jNj8O3buhehl0HzkkBhu8Fh489Lw-lSV0EsezUF1-bWglVNdJcNmy6dNCDIR_jzd9Di1pc2rM5bs5onAaipwFZJ7pgixI6DpPz9JRzKVuhiQRdKEcUaQOV_8OIR51THMuzgyQlRFib2YhRys7pDOU4a8PacI_TGUAsAlQ_PNwwvqNjcrhvlwVeyrwZgcKh-ypOLHizOy9CQAJasiF_zXfLqrCmhIUWueQQUPOyXIgIr0YiwCcWXoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE9Duoz8Hbtgmb403X4BFwLHFf6CraoP0gehq8m8Ahomf-jasE5sSjoD86PZyTZ1bAMfvDUiIh77dz_ry4BZ314cmsJjtaaRrqhgOLozNVM6smg9eWTrTOQwdSe6npbNp7oetD4-GLWn04SGnQI1bcJkfDznz_IsM3PeYcRAcosD0ktEBsaihPOZsyDGWcwh4R8tSIfpB_koDFTuYh4HdvE_ciAF5dK9nPMRLeEYwHbO167O6Er_wAImwcTp5S5ghBtkfmybMVcdVrzGFMhmqjIorFj5mLwaE2wBMQo0j6DxxTUSo2thHmDhEzuvssyQwFnvOb8OWp4VnG77rrhWTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaXI2YHKDNyvq6OVSB5tvBYhTv19T6rpEBv5auIpXgUzhRYsFnRBbNwil5qlbituEu05vFLdazhmGkKG3ZxvlEZKryBYbQrF7Ko9HzyFNOeElTzIhGsbiY60hBRZ1aDzSdwfii2a0Elfw0RPpTZlhN1Em3Rn3ktcZJhh1Rlt7tOBOalBOZWq2guwVTFxJFurapNov_g8hhxhLObEv5I4WzE1SVuNRbNNVvK3lXB_fCq_oid5irN80G3SH_PjZ4V_zTm9ki7LpBSvAEaYByR_l9kTYTreiqmYzeUiz6fFj1GKe66JtuijnFDsgpEGtpqIwTV21iQXacxx9pIKDMKY-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRrdNdnHQVYqESvHfWq3S4kDh-8GUjn4_I-Jx0LQwYV2iAagcxFYsS391NICbwAySwAwpKrh2Pm-3nvSDbTo-Om3EgbMRnuzGQQOlNZXyohG1ukxN0f3NTwzolW13RDRamMXTty3dL9ea1PHbr18Cqia-h0Zv35WK1QhgCsuqHcaBi96arb2R3qeERvzDaEG7vPv4gu9NURgbTB-qdq74RT8ghthy1xPhXTvf4FY4vR3esq3AoLNv9kWeawXCSWW6T31k5ktM4sAqzW26PLngn1IjNrYfo7TLu9tOKk9TK66nXpXcjo8mMvaVO6_xQ2sW6Msm-H70a4Sf2pBRxgiKQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=V7w9rEWALrJXvue2X1pj-c_x_z58hNy6TiNgYWabqRPBbkZUcbKLYCDEDfdJBwye5nMFtVvgkitEYJLt6-eTwZYUReRi4z0tVrZUepm2HkZVKYRzd01RzUCIkenP8QBWzr7DCpFi5IIFjoiFycwSPFmKDEsNC7gBlkcGFC8NuAGCavVEIEae06CuvAgG7TWg6-xob5-DoFVtuqtMu78Hjw1LuVHNgV05AM8AJDl3k-2-FwHjGjzn6eMop6Ig5YSemg3fGS1rfNLl49ElNSAQV6IY4hqWLVezOPL1ByNKRBGSEA7x7d7913mFFNHoicIOwhtQjCM0rKdUPEtn-x6_Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=V7w9rEWALrJXvue2X1pj-c_x_z58hNy6TiNgYWabqRPBbkZUcbKLYCDEDfdJBwye5nMFtVvgkitEYJLt6-eTwZYUReRi4z0tVrZUepm2HkZVKYRzd01RzUCIkenP8QBWzr7DCpFi5IIFjoiFycwSPFmKDEsNC7gBlkcGFC8NuAGCavVEIEae06CuvAgG7TWg6-xob5-DoFVtuqtMu78Hjw1LuVHNgV05AM8AJDl3k-2-FwHjGjzn6eMop6Ig5YSemg3fGS1rfNLl49ElNSAQV6IY4hqWLVezOPL1ByNKRBGSEA7x7d7913mFFNHoicIOwhtQjCM0rKdUPEtn-x6_Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P24v3LIbZQohrj3td6S0x8MFqhEkQbf5vBm11lMgAqaLXwnrB6cdtCBc6Kjk6FGLiqtKbU0wNLJpYUYe1cpLWSuGxzdponz1ql3Yi0BWYc_pXEUS0MJxVnnURfkgN0wjW6s3dhEwQh8y5rKynJiXnKt17CQlR0WeKb_1fgpG9mc5CbE9t9lmOT4IOxvat9l6f-d29pZWDtJfHnerleZ9r08kJd2qBg3tAzqd3gaCc3L8_CJPtjE65B3u0D-qW-RACoinsAWl1etdWQoXjUwRIh7oMLm1t7GcMWeUmS6-fx_0raMy3z5O2JE3mjqSlI6O1lZwAkapuRIR1W9Ggo9sbg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=XToljKaNf0J3oeADQAi5WJe8yq3wpmoLqmWrO5UxSA1mwWwHTEG2ken9MRQ2DqNM4LnfB9vwECefzFf_KuulefAXfHQ26Wnvkz3q1afgsHoJoiUG25BimFBHp5cItJM4TH6HU1ib8t879ds0GHBns6AnhhV9vGd4s8MeNGEJSOVDfSDbmBuygsy_Ehh26cWbGD69_XkfS3lek83FYDq48Pvh9XWUOa2c01voLo2U8qsKbSMIybgjOiKPz-dAa5QlQb48zdmR71YO2Lp6UOUdZH-kvno9n5mrqpmKs2ns5kiGefjNvwTNkTWWZTNveKn94iClD4p10GLfYvqJyxZ8fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=XToljKaNf0J3oeADQAi5WJe8yq3wpmoLqmWrO5UxSA1mwWwHTEG2ken9MRQ2DqNM4LnfB9vwECefzFf_KuulefAXfHQ26Wnvkz3q1afgsHoJoiUG25BimFBHp5cItJM4TH6HU1ib8t879ds0GHBns6AnhhV9vGd4s8MeNGEJSOVDfSDbmBuygsy_Ehh26cWbGD69_XkfS3lek83FYDq48Pvh9XWUOa2c01voLo2U8qsKbSMIybgjOiKPz-dAa5QlQb48zdmR71YO2Lp6UOUdZH-kvno9n5mrqpmKs2ns5kiGefjNvwTNkTWWZTNveKn94iClD4p10GLfYvqJyxZ8fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2ns5J5mcfzXJRv4Xr8O0XZYFvSqkI5XSeOGa6SUoRGyeH2EFZUTbmTNxE8H4lVNdye69ezuYMXRw3QIZXkVin8xoh4LN7HRo2tboonrJCMEhmfu-efwU4Mk6mMhHLl7OYiN05vuHOximK0jSChtGyxSW63tUU1GuK8Kox3s3lCv23NLDMoAGLfMZXFL3MIZXTyrTrQWvLGkLwEoeuHDblDk7DYqwvttQvR3rYdxEu4sDbxFtHcLUW_NvOAEU7ZuJjV_7l7p20AzwLzJYtgq20vuErRbMOEVxgbkPzPk_iPddptPheK12ZicfERV79bifDmtLAG3CWDF0SV2OJMIAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1E5xcQSaqjm88f26Ot649R7qN0x9klPItLih6jp7HQG24CE3naVRu4QtbzKBMxU60LGTx71zi_ZcQP6DFMiw8Jbu4SbKkOe809YXSp48dvPqTN5ARiIg81deq4SEnaphz6eCMHh4B2JYD0uuDGxBlzHiKJkABcxA_uiie6-av8JPXqaW-hZTZmI36Bo3C8gLSFrP2LFl-x169wdRIuClEyzLn8smOmDdzdd_2GXKqO7O3y436A2KvpUp383PwvJzXT3joob6lQVsKJQzi6NLefNk48bSXa5qRiOpMpDEvTm8gaFAX8dzOE4ZXwY54wwe26BrifxM6Dp6zeLqC3shA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuxOyMU8nHogQOjXdakV3KrORYJq6_sfJoa535EftXsae2dnFRJrW-uN9hNFcJjEnaBjrwxqSTRSv4_yq9IH-pCAu_A85wrE-k-bw3iHivVyMwssht1e4Whi_ijlW6uRIRXnpMir3UNHgPjNcdsOAbr5rl-dLXrtlPjtfQJfAb7aC8VGguEvVYCWONZv2BTm5GEwQLfa4o-BYFLAE2gAuMbinkkNGDx4lFpm3dx_7qfsTLCYTpTYmaPoPkN1j6rQR_ZG3-assZl_BmiQ40oDkXsRfDKHyOSi5Dngy7YQsPzFFUXMDuATeqRt-OQ4W2jCFlV5yZ1WvlxZRfkLm6WBtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdrlt0wt6xiBGMie2eTuddhNvFyS4rZCL52S8vS8BR5OFuKj5w_WkpBlp2ai0F9lp9lehvUrt9dzIVeGrkp9QSLozl0BujTZPcbnrsFOHTbnpoZqxk2rTTo25oeNIT_FPWsm83iSuiVnR9-xnkSC9k9gAWq_Ttl1gFLf9fNubjv9KWSKt-glvOnx-OLpwDizlf2Id79ptaAA6yksYlKz8-v7GC8ej5r5jHZwhJEOcLtZH3gU8uBnK7281bkQCfB4_k3gwsx2geR5jXbdG-im48yQvTijM14-nhpQW2RJ_ePyxxp3J4pYFzxcM9NW0zVQ3fmKPBJHRjhIP2XGNnB71Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkAtQmgamnU9FwDmaZ2h80SwPbI5mchz2-u6vz5tp8x9mj6qOHPv9Bhgq0RxjowUt5fQdc4V2PPiBjOrhI6imSsC4EW0R2LbvhUsYi-7fE8p-uybVGBpnAQMOOb-MdgwEHAZc5sa_b_vMr6SO24WC7FrfEXAyDPhqVLkNFZG2q43vNCr5ngHV40i-OmNUv6iJLiI9tkCyWlJlTw3JPMw6RWQnjIT5bmZmTWQUoIcugZCcoiM1IDKUATZ9XFIi2GZtS64YId-eYTmS122_l7V9knYLU3qhpMy_EpQcLqaIcLrl45ORL-ptl_7CrPgvHaywp_at_8ypcOc4vw3B6Ff3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE08AY8UZVQC7C4YTptpIOwQp1Nrw9EtC14yu4NOVZvBhaik73XPMYDeDJZRhGaokaXuOiOC1qdGO--iuNr0Xqszd9qRGo1WFDFBWglDPL4n0as-WnRB6i5kCtqwfqcUwJlmKT_1oKRGufu6l7RiVFGyPFCFMbq57z0Gvm2x_Tj6W_gaJrYSJ1fsqD3lSoYIfdyXVRHnhQh2pM0hTPLEJEGdX81LE0hvTiiZG8BIIbclg6lz3FSE_qOqmzlZt3OY5X0dhMyIKq_3bMKTmoE1CqzIX5XtIUx2uemUS2_8CG-oPuXF8W-S-O0yn3nLiJSQ91m3x2L0a1c6esdb5j21pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azaQLtNmdNkPP9XB2iszvhi2GlB0OoOE4jDI9mif7Q2CuZ3f_tjbwZ64lO67GJY9PEjRQDgeBpYOOUVkXbZdydbvkqQhxv8gHrBVsNCj7RxJosG9C6Y9y39sk73OhjMjy7aMd-QulT6tIrVGFLeGHpDSrbuv52Cip4o7lJ9I9D3mCVNEMsIf5A38o9uT13T4SCpNnl5janlilAZMf8ktv42DXGkjeVWbHxRmVcSPapPS_OA-9ZH6DFayka__-IKoaVnKuIi69KvoGXeMt1d9KbFM4nwKmry9ptbW86Ci7l2VyMQNSIxduGCFW5y8fzEkbUs-KWbcrMc3HFakrsaWHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqiI0h1Azy8QpwYvs1kKAVLNqDyhmIi-dlEmpnaiaIFFrayaA5M9i60sHxz5K6rd5dr8rqcc1MVmLP-jRM_BZRVcH-z0CXYEfpIR_LMPVK40Fr3OoCln-fLycLTemlVIWMb2ZT1MBhPTzzWjub1-IgP64xgaVSoEiRdsIGWvu8h6Lcm49CQk4Ot7PELTNukklhi7Co9o9NzGcbVqrmOWbLFoyGuhpxhc2fnyRIBZXsdAKhiRCyLKyAuQjJL7BIvoW-_0wi_3N53LfeQIIEctr0YKf7kZfyGn2dJogI-uPDtTDUQheg_7pmR3E4l4NxWaRKDQV_ttgQjaCagFZsBrBg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=rQ39DRbVqtbrCBmQID-BXu30751-i6I4Ep5In_ACXDhfWY25Z9xEX0ECBGKKcezGRuedGnnXUGh8lW7KzFHmTolnm0HSzKWExpeYB_fh5uHcfEYzwBCmqOB9zpY-EmZmdpht1vVGqOeTt57YvUPzqGgPY_L9go_51VJBULS_5e6WJull7ByrT2BSOK1FF3bHC3pjyXdTFAo_C3g4pNuEMs3S2qMX4gisjgtSFKIQUCAoavrVlVkfEti-foJA87KZTd7_6aI7F3Yve1Xnrk2_bTAwZGeAtKr9TVGG4M_OL3_JYhNXSRC_uXesfKJry92DDPGYXwfkDg5_ZrOPmWelTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=rQ39DRbVqtbrCBmQID-BXu30751-i6I4Ep5In_ACXDhfWY25Z9xEX0ECBGKKcezGRuedGnnXUGh8lW7KzFHmTolnm0HSzKWExpeYB_fh5uHcfEYzwBCmqOB9zpY-EmZmdpht1vVGqOeTt57YvUPzqGgPY_L9go_51VJBULS_5e6WJull7ByrT2BSOK1FF3bHC3pjyXdTFAo_C3g4pNuEMs3S2qMX4gisjgtSFKIQUCAoavrVlVkfEti-foJA87KZTd7_6aI7F3Yve1Xnrk2_bTAwZGeAtKr9TVGG4M_OL3_JYhNXSRC_uXesfKJry92DDPGYXwfkDg5_ZrOPmWelTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbVdNjcLcPIrjMHbp0DFiQvpT_mask-Chsg2q3mm4ehVD3zshQctqU9WLDPwcBQRBfg4SYpjtlYr193jpZElI_y92fly5t87wn74CVUm4EUintVtdpxg_x1gO3FUxZtnPC6jEnQFT9EtkSMwTNR8jsEiyBJ-gpSbhMRj-MizVfTQIln1EBhM8zDqm4-3KayQpMLk4AXP1wXdOy3bprvpnTQEmkn2akcTN68qRHo4WfKgKm-hOeC7ukxYvjuBFJtz1_VggLNeIcplPaCQ_DXbef9YChWJOD3HnrzEIJfjWUXEvRCIzpaIU4wPyURHKowg-W2kPWB6B9r7xtcRggoXYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suZm1rZyVGBGCx1E0SzILl_CCZSzbR5QQ0X76MNqwN_crIhxTWlMnzDHQ5F08EFWlmaWfGBz0BK94R0Dh_V-zkEAiTsKsUg9UBewchvYd_LJ8VK2FnlTF8y3Hm5CYdt-_d3xE5eUiIX4pcxaJrbonScYRNrTGNQqfWEeXWP3ONwXaNmdk8yK71vYb8Q6iqRhO07-4uijVMup05x8fIXRnVPKCPVnLmr_R-NySpdD9LQbbSFw9IIbqDD-olYAbHJajs8wvSOFhgPPdvtjbO4zSImhKuDSKn57z4Y79Ut0qpPMC5flXaSuZHDFunsHd29iAXd_mFF_KT_PcqOi6gR80Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHw1n2X9TMcnpEfDeeldW3Xbxmv3MtfQBtJ3jBnPT-v92rMIQhxKv1tC51imYLqEgsO1ROwqMCwvG0T2cmvHB5wgGRJXfjTxjpD5q3Qg1829A3us5DHJ9pCdplhy9Gv_AlhJPmWeADExAE_DDQlNdEdTDQJ7anaMcQh6dGfdDgVlifwBlfZkHsvCke-2_UeRcs6y-6Ow4x_0T9KG6pavXzBeTA5Dsd6S_i-N6p4a_gzqv5XASek6xzoThO9ol1znVl-_hz8II_iGg6C-yYd1CP5DnoIneTrwzfKbqlKHo2Q0jMligZZMJRWblkPFXuvGP-JijrdxlVOW7_LwnDBPJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSwadNgK5ILK8HD_IqlbyNl6QFgxVQkrGvEan02r6oDuy7s0l7SjNnS5Y7kzaquzU1vrq-EJI_k7V3H-aAq0q51p2xvy3xL6gfZeMvO2z0wpUMBepRPYezLLXrCTMTGWb0PRejoFCgiOSLUjnM00mUgSpUIH62Zg3DyZQ5bDgx3jbF1BzbhuXorTbael5qWsomMFe1iPDKINYtG9hHUhEjgXBcS0s6eSa4ZHIP7Xd0StvAxy2BsTPDPK8aZWKgKE-J2z4cTUW0POEFschWTHETDvdYHFCDPEmnaThrrv9gZ7R5l-gdoL5hX7CoYMd-Zxz-QD0AG-rCBHPFI-MhufKQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=j0Q8jPcW9jRF83eXRMZhwC0h4KaSb88hZXeN9I-EKu0KfP_jVQbOqLpnRiWjQ49qDhG48xXZLxPDrMXz0LUWmobCu7WGUuirsN25NGFkdaY05BrHxIZY-bBx4Q16wI_hEoc3eXmJVuoWCJEVnfhIJoqtQVI3zjSyBB3JNYTOUQNQYmflQ-1_uUMxSDHXg5_LG1weI40ES7_dS1BX-Qhxh4XIzKWlDVowjb6OKnrLtlKOhMxe4cgk5mQc-OSdhTIXNDL9pMVplHuZw641tCHc0dF85cmwQH4elbpUY0cmgnxqPj4Odj0nPaVPwF-HFln_QjZKJXmxG8tHdWlsF_XokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=j0Q8jPcW9jRF83eXRMZhwC0h4KaSb88hZXeN9I-EKu0KfP_jVQbOqLpnRiWjQ49qDhG48xXZLxPDrMXz0LUWmobCu7WGUuirsN25NGFkdaY05BrHxIZY-bBx4Q16wI_hEoc3eXmJVuoWCJEVnfhIJoqtQVI3zjSyBB3JNYTOUQNQYmflQ-1_uUMxSDHXg5_LG1weI40ES7_dS1BX-Qhxh4XIzKWlDVowjb6OKnrLtlKOhMxe4cgk5mQc-OSdhTIXNDL9pMVplHuZw641tCHc0dF85cmwQH4elbpUY0cmgnxqPj4Odj0nPaVPwF-HFln_QjZKJXmxG8tHdWlsF_XokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJaDXUf7WKmwMJo9v6qVpY7edEf4R9d1oyYuoy8WFbjZ-LVgQYqZYKXSwji_SVPHpBKIpAJRQHhuZFUStzrGZvsvAwJ0vl88yOmBTr02XeB_UHIWyNgXgVPdKhcNieH-Hmm58ga_UIVdH4yAlHs107CQVE1GNtM9fbOStTRvhOe7XsGddKOIEuhSRJtfkdkNcHscwJWZaFLi17hX30DzudNT-BFBwU7UTgitwKbZ5kx1v0MOAnGBjDNZZgtzrGZFn4bpmGSmQQ5wZ97y1fnS1R4Gs7ungUxBIaQBP5YI89zp5RIMDVTNlawPS8AIoS5KvHLkn-v8m8WUzMbsTK9Fhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpYYuaJuVYjK304YeWgHTKqc3HCdpVOYeDGBbF5WQWZBUGFDDdvV_UuPYQl4bcphUZG6qZAhWvI7w-EgqnwXU7QANYSzm2YluoNje0LkoemYd6xNa8GIIlPgkcQPisd_mvdFxQxj6IskS1eRXW193toLwJCi_Pjzz0NmLF0b-nYsUBPOp5zHr_Xg8gqoKs0fT-2AtqO-jX9G_f10G4VfETeJXwhRpqCe-RObO4HnQNQVwMcImCzVu1pUCN8QMCzGWwvPejnaLVxpEWcTGIVrzvsBSemPrsMV0ALuToAt4DgFDEzS7Lshybpgl-zY6VrN1S9YvJJD4oFSJG4ZtkvOHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to2I1eKXSqmPA6Bxf71L0TQC3Vr--SOuRDm_mjsxmMtOG33EFzd32jdHMaFj3SZZeEhJiSAYX4tu10H1eYiJDby9WMIDS8NJbrWRhvDuAaR_ReE2LBRErYlt2l40nZay3cxxXCNpuo1CiV06eSA9f7ajayrfeB-PaQAAvATdfuBOw7dKZoqRgXz3Rk81q77jEMTCgw4Ujf6889fUvlQ95z-4Bm_wvTS0sB__bg0_C4f-BpuzDtsS_xNRSwAL3SN7Aq7lsqywuTP_Z8BQcYjS7gnzsvsdLu1Zsdio85ys-yLWUmyeMllhVlVFrTxOlFZkaxYdUMfKpltLT_wxnFhbLQ.jpg" alt="photo" loading="lazy"/></div>
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
