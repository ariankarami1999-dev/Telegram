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
<img src="https://cdn4.telesco.pe/file/uY-NJy5aX6_IqawzALUZWRvW8UT_wjYfLj7vF5MtjvImJiXn9QHV1oBolL-j9sGN9TMfeQabH6eUjCUHpfCKA72Avr7eY-V_etHhNwCtn2787CMAzlOo7ltq8Wss_26SnJFXjJJkV_Jk-L1_mD5KOE9jDvWSYxBhtahc15vcW5zwjlIoIQpMdxvog04vRRgQLPuzsk0SKc1tHB-Q-zdjYndrhQR8kBnTwQ_eYlEFF2nE1nywKPpf7wRaWim3sQEYx9cP0Lp0lYYtCHCA__KNi9C2BCV9WzLVJqy70X3RNPKRIw3jk2l8pmQ7XZ8nQkdcNiAlUXDa8ptNF171hM8BDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 11:32:26</div>
<hr>

<div class="tg-post" id="msg-138379">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دستور نخست وزیر عراق برای تشکیل جلسه اضطراری در پی حملات مشترک عربستان و آمریکا علیه الحشد الشعبی
🔴
در پی حملات مشترک عربستان و آمریکا علیه الحشد الشعبی، نخست وزیر عراق دستور نشست اضطراری برای بررسی تحولات امنیتی این کشور را داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/138379" target="_blank">📅 11:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138378">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDgXaChJJWkiBiXbBknbvfNWzPTiZt39OZUQiqD7YFUQMSJM2-7M-YvI5zhjEL4kB6ljDw9OIhOQc2Y3JsuwxwFrSa3uU3LqUfaInjrK6KEJTu75m6V4hNXZT_2sbwac5iuMO-0S9rUoUfVySKAtGgFDfurD_13zr4fZ8djxYzdLujbtjLwAAQ5DBWN50-v5O8L1m6DQTbEcpj4Bf6dAA7i9kKhwIYTUIMy_gaKcrVIgIe3Ml5DqmmgM3bNhNVCRJn4CYXWhFqYOGD81Qva6m347cGiI3TLcwf7NJfQmQVoS3gHmnBvbGQ6-2RaCHY87dyIvCNfDcf8Mv-j2zWpJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان امنیت فدرال روسیه؛ دوروف، بنیانگذار (تلگرام)، تو فهرست افراد تحت تعقیب بین‌المللی قرار داد
🔴
روسیه مدعی شده دلیلش این هست :  تلگرام کانال‌ها، گروه‌ها و ربات‌هایی رو که به ادعای مسکو سرویس‌های اطلاعاتی اوکراین و گروه‌های تروریستی ازشون استفاده می‌کردن،…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/138378" target="_blank">📅 11:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
دبیر کمیسیون امنیت ملی: عمان باید بداند مذاکره با آن‌ها در صورت مداخله آمریکا، هرگز اتفاق نخواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/138376" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزارت دفاع روسیه : دو کشتی باری حامل تجهیزات نظامی اوکراین هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/138375" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be8d96d36.mp4?token=YJ5QR4bORxZuLQFK4jXWL-mZe3CVBXW7YpPNUgokHA4IlzPkfnszM0wDFlPYxTNa6BkftORRHMaE4vraWp7lH-EJHzLg5xfDLwptpT3ahUQ_ciLolgizMF5jqzjZKjGQPBAqCxFIHmqWUmkZkaonvIpC-mVD4nmYhLGRX8OVoJEbnikJtUOY59d1MPnC3FOksDL7Fxa9Ce7yh5SpeCdWqY5S7WP7jfU8A2vO-NnHBFlXbRXYHRIrFehWxEctnhP1GmbKNgTsioOAUGOYABLokILaGozIhFgL3-b7gshQ_tk6OTuaI8MOpeeonJGtLwRVOCz-1T0qh82zNVSt6Vxhuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be8d96d36.mp4?token=YJ5QR4bORxZuLQFK4jXWL-mZe3CVBXW7YpPNUgokHA4IlzPkfnszM0wDFlPYxTNa6BkftORRHMaE4vraWp7lH-EJHzLg5xfDLwptpT3ahUQ_ciLolgizMF5jqzjZKjGQPBAqCxFIHmqWUmkZkaonvIpC-mVD4nmYhLGRX8OVoJEbnikJtUOY59d1MPnC3FOksDL7Fxa9Ce7yh5SpeCdWqY5S7WP7jfU8A2vO-NnHBFlXbRXYHRIrFehWxEctnhP1GmbKNgTsioOAUGOYABLokILaGozIhFgL3-b7gshQ_tk6OTuaI8MOpeeonJGtLwRVOCz-1T0qh82zNVSt6Vxhuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی دیگر از حمله آمریکا و عربستان علیه حشد الشعبی در نینوا
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/138374" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نتانیاهو : به نظر من، اختلاف این گروه‌ها بیشتر سر اینه که ما چقدر قاطع هستیم
نه اینکه از نظر فکری با هم فرق داشته باشند
🔴
کسانی که فکر می‌کنن ترامپ خیلی قاطعه، می‌گن بهتره باهاش درگیر نشند
🔴
ولی اون‌هایی که فکر می‌کنن می‌تونن با آمریکا کنار بیان، معمولاً خواسته‌های بیشتری مطرح می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/138373" target="_blank">📅 11:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نتانیاهو : وقتی نیروها و سربازان شجاع ما متحد باشن، هیچ چیزی نمی‌تونه جلوی ما رو بگیره
🔴
هانیتی (فاکس نیوز ): امروز با ترامپ دیدار داشتید، جلسه چطور پیش رفت؟
🔴
نتانیاهو : خیلی عالی بود، یکی از بهترین دیدارهایی بود که داشتیم
🔴
من همیشه از ناامید کردن کسانی که دنبال پیدا کردن اختلاف و ضعف در اتحاد ما هستن، ناراحت می‌شم
🔴
چون چیزی که امروز دیدن، یه اتحاد محکم و بدون شکاف بود
🔴
رئیس‌جمهور خیلی صریحه. ما یه هدف مشترک داریم
🔴
نمی‌خوایم تهران به سلاح هسته‌ای دست پیدا کنه و آمریکا، صلح جهانی و اسرائیل رو تهدید کنه
🔴
این هدف یا از راه دیپلماسی یا از راه‌های دیگه محقق می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/138372" target="_blank">📅 11:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
معاون وزیر علوم: آموزش در ترم آینده حضوری است.
🔴
دانشگاه‌ها مجاز به برگزاری ۲۵ درصد کلاس‌ها به‌صورت مجازی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/138371" target="_blank">📅 11:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRmV20kyVRx0fe9NanXiJaFMcmmf2zC4HYLLTsykokYHzk4Htt7-CARRXKfCtT4eAgosUAKek10dYJiX0jq9PrhXKf7XMCQS3ZdVxVmuw5JCgY2aix5aAbKzQ7sje_Kud36lM1TV0TuKBBbnxvt6BFX4KFXIJ5zxkeiLCFNBGddGjI3AYpMv4thhHViEIRTHee_c86fwv2cnn5kQM2fC_TagA6s-FB9X_20yF-g_1UdSARnAWgQAOfCDm62bKtyFBhSNsexD3axCrxvCBaQEyoz49QY7qRPsKKmSPSOOfsuPpePyjSsgHRi4e9yrwVJPGtUxNMbB1zxVneAmrWb4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز آمار: تورم نقطه به نقطه خوراکی‌ها در تیرماه ۱۳۴ درصد شد
‏
🔴
این شاخص در مناطق روستایی به ۱۴۰ درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/138370" target="_blank">📅 10:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b1c8f5ff.mp4?token=lNihtIEIp9JSmmc4Apk3KmGpx1mW7FqudHtBYGsDbIxevpGsQddlU7UCeUmPL3nnqiqQdOCkQfZEfrsWqchrgKuHx3b4z12QQk7uqHDmpi4k0j1jDV2f2lPqBa069xj1FxFtnJ4gOWLsUz61OihIci1_a34AeoW6UvqNu70hYUr260vVFMl76IX3Mtq3oNjgZ_qdbxxgPbtXeiZNWI1nOI6_Nyw1xgmmrE7b7l-jinMrlD2moPwPtf4CNpFY9homPxwjMukfXMvjxwkWuhUPLBmtMxUNfEzZvWAUb3bxQxBpmHjR2tFTkBdwY7L11lmc30_OyrA0PdEON0e2FGGP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b1c8f5ff.mp4?token=lNihtIEIp9JSmmc4Apk3KmGpx1mW7FqudHtBYGsDbIxevpGsQddlU7UCeUmPL3nnqiqQdOCkQfZEfrsWqchrgKuHx3b4z12QQk7uqHDmpi4k0j1jDV2f2lPqBa069xj1FxFtnJ4gOWLsUz61OihIci1_a34AeoW6UvqNu70hYUr260vVFMl76IX3Mtq3oNjgZ_qdbxxgPbtXeiZNWI1nOI6_Nyw1xgmmrE7b7l-jinMrlD2moPwPtf4CNpFY9homPxwjMukfXMvjxwkWuhUPLBmtMxUNfEzZvWAUb3bxQxBpmHjR2tFTkBdwY7L11lmc30_OyrA0PdEON0e2FGGP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیر کمیسیون امنیت ملی: عمان باید بداند مذاکره با آن‌ها در صورت مداخله آمریکا، هرگز اتفاق نخواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/138369" target="_blank">📅 10:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
حشد الشعبی در بیانیه ای اعلام کرد که در پی حملات آمریکا و عربستان تاکنون ۲۰ نفر کشته و ۳۰ نفر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/138368" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138365">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjDyWT3Y2PslsbkrVqy__GYOSaOg93CKLSUje0R-S_NLYVmfowyPlWeXFMBjh8jefJSma2I_niTGhQ13Eg4u06y_i5popn8nsyu89wmsgt03_98nHB93J5tx2UerbNhlvXgh2J4eRPc9sA2aanDfLHq57557Iv4CAC0kvJjTZLjS3jTVrOrkqzm_tP1cNzffAfJCdS619x96_GjS4Qk9BA11M4l1xUUVgV0rl-p8kJZiswsD3iPfXx38_DF8uRS89z83ENYzVsli2iTOVVWV96dYP8RLB-hwVVf-Dgzs6Cv6MbftoBmJXzaJ1Beqwn0Ydcq7ptahds3J1lFlm1IIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCR6XzvOBUB56Tj9rjm_lqXanDnLormeqV-dwpKS2Rnhz4QmMcD5i8kFhz1m1zjJ4FZGI-34YuGoa1IQiLZSxg1_NQbbdURIotmm20_doihI6qy05Mu8H-YzqPLjUjdffqa0UF_Q8jSHAsv08Heo_i7h0McEweKVA3u-e2gYqjA-cRqmhximozhX4njOInm-IZ_daD4kXIoNjpLL_grd24ve7NaZRT_kg-_X6KBkl2Ajok1kQbA_sFo1VNbhYQVBBxTirD2osAo-2TEVTu5eDFpR-UuOhf8blTTkCnchVqgJIuBqcLfOMR8oiy4SbNbB7-X4jvU4PiqHY3oZjaIJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EICIgMzvcH0_-kL6AAvXvGRegNoQBdfy3TVESDqOrwLSGO7zyuTjuZFLzwQRn6uDIEpLA7aGuxG-zuIq233_I5hv9oahv6vKR4GjU_090KlB29AweBgO0KhcC9_iOZUVxTRv6QafMfQCBxm6Hzn0U0QUzURYb-XQl-mGQoNtpG9igqgtsN5Rfvm29G-v7JcHzp7CZs7niI85hYwojfrRHtt8R-4hx3ctOUyS-b4dLyVCZyuLHVUn3Qxd8tTjHmrJTIP35BWG1WjWIakB1kp2x3YNvVPH5Vlv58ytTGPtHFhJbKkq0irMWOAGWxDkKxDFQBQg9b8EOYM5SZEBJT2prw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگری از تخریب مقرهای حشد الشعبی در عراق پس از حملات سعودی آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/138365" target="_blank">📅 10:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138364">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نتانیاهو به فاکس نیوز: من در مورد توافق با ایران شک دارم و این را آشکارا می‌گویم
‏
🔴
هر بار که توافق نزدیک است، تندروها می‌آیند و به کشتی‌ها در تنگه هرمز حمله می‌کنند.
‏
🔴
موضع ترامپ بسیار واضح است و ما تعهد مشترکی داریم. ما نمی‌خواهیم ایران سلاح هسته‌ای داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138364" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138363">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سفارت آمریکا در بغداد به شهروندان آمریکایی هشدار می‌دهد که از سفر به عراق خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138363" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138362">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سازمان امنیت فدرال روسیه؛
دوروف، بنیانگذار (تلگرام)، تو فهرست افراد تحت تعقیب بین‌المللی قرار داد
🔴
روسیه مدعی شده دلیلش این هست :
تلگرام کانال‌ها، گروه‌ها و ربات‌هایی رو که به ادعای مسکو سرویس‌های اطلاعاتی اوکراین و گروه‌های تروریستی ازشون استفاده می‌کردن، نبسته
🔴
از این کانال‌ها برای هماهنگ کردن حملات خرابکارانه؛
🔴
عملیات تروریستی و حملات سایبری داخل روسیه استفاده شده و به همین خاطر برای پاول دوروف حکم تعقیب بین‌المللی صادر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/138362" target="_blank">📅 10:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138361">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
روزنامه کیهان: دفاع از آزادی اینترنت به سود دشمن است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/138361" target="_blank">📅 10:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138360">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت انرژی آمریکا، ایالت‌های یوتا، تنسی، اکلاهما، لوئیزیانا و آیداهو را به عنوان گزینه‌های میزبانی برای «پردیس‌های نوآوری چرخه هسته‌ای» انتخاب کرده است؛ تأسیساتی که از تولید سوخت، غنی‌سازی، فرآوری مجدد سوخت مصرف‌شده و دفع زباله پشتیبانی می‌کنند.
🔴
این مراکز همچنین برای استقرار راکتورهای پیشرفته و مراکز داده در نظر گرفته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/138360" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138359">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
خبرگزاری فرانسه: وزارت امور خارجه ونزوئلا در بیانیه‌ای اعلام کرد که این کشور سفیر ایران، را احضار کرد تا به اظهاراتی که «تحقیرآمیز و نامناسب» تلقی شده بود، اعتراض کند.
🔴
مقامات ونزوئلا، مشخص نکردند که به چه اظهاراتی اشاره دارند، اما ویدئویی که به صورت آنلاین در حال پخش است نشان می‌دهد که عباس عراقچی، اخیراً گفته است که ایران در مورد مذاکره با آمریکا «ونزوئلا نیست»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138359" target="_blank">📅 10:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138358">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نیویورک تایمز: ایران به این فکر کرده بود که یک حمله موشکی نمادین به یک بندر اوکراینی در دریای سیاه انجام دهد، پس از آنکه گزارش‌هایی منتشر شد مبنی بر اینکه اوکراین یک کشتی باری ایرانی را در دریای خزر مورد اصابت قرار داده است.
‏
🔴
به گفته مقامات ایرانی و غربی، تلاش‌های دیپلماتیک تاکنون از تشدید تنش‌ها جلوگیری کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138358" target="_blank">📅 10:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138357">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJPa-VfmZfaToIqYjsEO9oExJuVYj1I_mq8vCrc7cuXF5_n3OwBNVXD32rYRzAiSKG6UK4Atn1ZD9j1xDnjPgu1pd4jgix1d7fKl97PomqGiBNxUbx6HB7mGJx0Rpj-X1ngBKLyT1wzpj9IEJ-r0mvSqJQJEfo2YGwc88TP2h0hR17ZdBtXcBgm3bnwQe-V_gwG5jRpvE4JQHxrzVu1F8ao0u7osfyqfxfTY64Ud308Ch97r0AfN1jWHf7zn_VQ80qRlghRBNpTlciN2rKMur1Swo1C-Uam5siQRz3sdgHneU70l9iMM8d5OyM33iNEsfZFm6dquFmTrwCFFdSy_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشته شده های حشدالشعبی توی حملات دیشب آمریکا و عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/138357" target="_blank">📅 10:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138356">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6c48fc229.mp4?token=Vm_BkKMaM-KtMbmSBbtYMiFqBMgs_Esf_81pG9nZrsBL2-Ge_Zsmz-FjZ9P2aQ7COBYPr0m70Cf_vOwH1OAXqdIU5Hc04J-NIXM4tg7ocOgcTpiI8rb39usDvKgR3inbPbpXhC9bZn-Cy3wQ6VjvgPUvL0soz0mzV8X74AkD-F4dbVpQlDXAyHqFojzZ5A7Yv1PLLpquSZ_aMoX8noRUztnpMY5pTOifrZ2Ug9gb8gxXOpUi0-xvSKJcfdfKzdko2LbQYlUFPra0FC3xKVMZLbeLgiyCiEgb9msQZ6UONTE_b_AlCymyHSfZGvP7Uj6U38x4YL8YnFSt6GjfHALXGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6c48fc229.mp4?token=Vm_BkKMaM-KtMbmSBbtYMiFqBMgs_Esf_81pG9nZrsBL2-Ge_Zsmz-FjZ9P2aQ7COBYPr0m70Cf_vOwH1OAXqdIU5Hc04J-NIXM4tg7ocOgcTpiI8rb39usDvKgR3inbPbpXhC9bZn-Cy3wQ6VjvgPUvL0soz0mzV8X74AkD-F4dbVpQlDXAyHqFojzZ5A7Yv1PLLpquSZ_aMoX8noRUztnpMY5pTOifrZ2Ug9gb8gxXOpUi0-xvSKJcfdfKzdko2LbQYlUFPra0FC3xKVMZLbeLgiyCiEgb9msQZ6UONTE_b_AlCymyHSfZGvP7Uj6U38x4YL8YnFSt6GjfHALXGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حضور نتانیاهو پیت هگست، مارکو روبیو و اسکات بسنت در مراسم تشییع لیندسی
گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/138356" target="_blank">📅 09:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138355">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رویترز: تهران پیشنهاد عمان برای مدیریت مشترک تنگه هرمز را رد کرده و این طرح را فاقد هرگونه شانس موفقیت دانسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138355" target="_blank">📅 09:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138354">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99a620e7eb.mp4?token=vQ-MhDTNfKARXLYVWt7FpBXfrQesngr0QPCTs2qOmHRPz1YhUVlsT13c9TSitt9ccfM7FcGR7NMUc5UBCuizB1-47Y7ePZSBdjmWPiGqCwZ4SdJuiuOne-K5AMbHxBnPvXvtrpE0t8yxuTqBjjwUN40zuAxCvR5PjPiq56zA85GPQ2N0P8W5RQsLOPj8ozbP_h5i20BKRhuBEtukYYSMGQDoGVguNZX_czPINWdU10T21oujPj5bW9-ol7JvyMbdnW78lJlQDiPA1BA46qRXquTeTP5RiZsXz5lvBcGOk0d59cfJ6ZAhL7yT66ZsliIpyYqtQ1zgBKNnk7MIpwCzXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99a620e7eb.mp4?token=vQ-MhDTNfKARXLYVWt7FpBXfrQesngr0QPCTs2qOmHRPz1YhUVlsT13c9TSitt9ccfM7FcGR7NMUc5UBCuizB1-47Y7ePZSBdjmWPiGqCwZ4SdJuiuOne-K5AMbHxBnPvXvtrpE0t8yxuTqBjjwUN40zuAxCvR5PjPiq56zA85GPQ2N0P8W5RQsLOPj8ozbP_h5i20BKRhuBEtukYYSMGQDoGVguNZX_czPINWdU10T21oujPj5bW9-ol7JvyMbdnW78lJlQDiPA1BA46qRXquTeTP5RiZsXz5lvBcGOk0d59cfJ6ZAhL7yT66ZsliIpyYqtQ1zgBKNnk7MIpwCzXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام
:
جنگنده‌های آمریکایی و سعودی در پاسخی قاطع به بیش از ۳۰ حمله پهپادی هوایی که طی ۷۲ ساعت گذشته به دستور سپاه پاسداران انجام شده بود، چندین مرکز لجستیکی و انبار تسلیحاتی حشدالشعبی را در سراسر شرق عراق هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138354" target="_blank">📅 09:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138352">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYYn9tuGjkvhgh986PLwdcBNJ2ATBBlBrtu8zzDLtChRJjsd935MutSfC-wMBahdWaYHvF0vjutEdKWcZMsX61VpiCQrwfE7gth6l8Vq45NMIXc93Csu-tdjNzD7eOOay-fCSuRwO-fYti4CpXnakwoLUWjaNtcEH-ejcHy1R7gkhudKlh6CCOpA6Smm8KHmluJyWqf0319GkmJEtV-XSqnfAGb7Hy0SSEJBvPTY01x91V-f8n9lvQF0NG2uS0biu-OwSzfVv7BctAAk5vSSCSsteGzjeUBPY2r5MspJoId4kFppFUV9wsBcHD267LcnUfdbVnAtGpNQL5czDcouRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-3zXBGgwZR4ck05wTG-zLv1ILs7NgpQjq1YbbDT1Tf_BML7QjvrwqG0-_fhkywEqgAfK5NMSZTkyS4ibEznA2EZkMGKSn8NCdDe5HX5Hy4SGobKM40_OTLKma7xvzcCaqQUTGOMkZNpy6YpVdGFEUnP9eR_2nhR5AzAVWeYcy4Iwv-qU8SbsPfEIm8pOsxXqjLYkhFdxY1ICbApV7SLn1YY_Ibkp3-vh7PCgHSCc8hyBS6ya3Oa65zMEfBoonevQ4j-0bXTAQafppO5FeR4C2QPUG7uXj0aHpdtzWex9wmQhnXYcSEnZ8Jcwqzbrdl9snGh1nHmZCT5rmaNj_IPmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری جدید از بمباران سعودی در مقر تیپ 24 در منطقه المقدادیه در استان دیالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138352" target="_blank">📅 09:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138351">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589d2ad2c4.mp4?token=bSqvwdUvD3ZVqDKavUrx08njPK5uueXr1_yo_PnLvliZIzWfRHXUwiZuYEVxOVgYRdCFfRK7fnbFOvb_-qVTG1iCbjYj3AQIync1piGElIPnD3R-UGGvwz-rBstdknW8B7rlBW6S3pNRmF6IfvzUgm31fdg3RmFOumH-Shrrk_UKodqhH2q9EuI13h_TP2Vk8AJyTEO6WT2r9lOfbADd-ukdg3xk2Pv94Zj_h6a-ikG_ol-tvz6JmlNTaV69HBbgwYlh1uKMN_wVFMG5CMmpJgRAfpG-_QLwfHb1X8LHV9PnEnDwvT0q3-Os5L6cKq05tSUwGlVxutuaFwEy5xzZM7WFd1cOAbFY_LaI6C5YWuZbu_eMKnxdHz73eBTl_OtKdp10TG5DrDXIKlPbMs_pjJZUp72UmeptZ0zDQFufWZHBgP0_KNxj5mbwwHaAYaRY36m88WZZ_ghqZ4ip26M9b72jLxGnOaWYjTB1y5piNU_NcTVtRyD5VyUPT0300uKDIecg5-MAw-gij39qTLNlPHuuYPsGIBYrKpi8TnOXFBbshv4M88mngot8ZPJilDmnE_BYiBoK2iFaFYukV4hYvEhDThu6kQ_7KaPUQkE8c2lKYA_1TuIT8_3ja7f4J5aC2Cut8ySbD5QrXS2SNuKfAjEubDp-ntgev3R_BrlTmYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589d2ad2c4.mp4?token=bSqvwdUvD3ZVqDKavUrx08njPK5uueXr1_yo_PnLvliZIzWfRHXUwiZuYEVxOVgYRdCFfRK7fnbFOvb_-qVTG1iCbjYj3AQIync1piGElIPnD3R-UGGvwz-rBstdknW8B7rlBW6S3pNRmF6IfvzUgm31fdg3RmFOumH-Shrrk_UKodqhH2q9EuI13h_TP2Vk8AJyTEO6WT2r9lOfbADd-ukdg3xk2Pv94Zj_h6a-ikG_ol-tvz6JmlNTaV69HBbgwYlh1uKMN_wVFMG5CMmpJgRAfpG-_QLwfHb1X8LHV9PnEnDwvT0q3-Os5L6cKq05tSUwGlVxutuaFwEy5xzZM7WFd1cOAbFY_LaI6C5YWuZbu_eMKnxdHz73eBTl_OtKdp10TG5DrDXIKlPbMs_pjJZUp72UmeptZ0zDQFufWZHBgP0_KNxj5mbwwHaAYaRY36m88WZZ_ghqZ4ip26M9b72jLxGnOaWYjTB1y5piNU_NcTVtRyD5VyUPT0300uKDIecg5-MAw-gij39qTLNlPHuuYPsGIBYrKpi8TnOXFBbshv4M88mngot8ZPJilDmnE_BYiBoK2iFaFYukV4hYvEhDThu6kQ_7KaPUQkE8c2lKYA_1TuIT8_3ja7f4J5aC2Cut8ySbD5QrXS2SNuKfAjEubDp-ntgev3R_BrlTmYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری فاکس نیوز: به نظر من اروپا یه قاره رو به افوله، اشتباه میکنم؟
🔴
زلنسکی: منظورم اینه که این اروپای متفاوته، درک نمیکنم چرا از اوکراین دعوت نمیشه برا پیوستن به ناتو
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138351" target="_blank">📅 09:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138350">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
آخرین آمار حمله عربستان به عراق به نقل از نایا
🔴
۱۰ کشته از تیپ ۳۰ شَبک
🔴
۲ کشته از تیپ ۲۴ حشد الشعبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138350" target="_blank">📅 09:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138349">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا:
تعویق درگیری در خلیج فارس می‌تواند برای میانجیگران وقت بخرد تا راهی برای بازگشت به دیپلماسی پیدا کرده و از بازگشت به جنگ تمام عیار جلوگیری کنند
🔴
مایه دلگرمی است که وزیر خارجه اوکراین با عراقچی برای کاهش تنش‌ها گفت‌و‌گو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138349" target="_blank">📅 09:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138348">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
حوثی‌های یمن با صدور بیانیه‌ای، حمله مشترک آمریکا و عربستان به حشد شعبی عراق را به‌شدت محکوم کرد و آن را اقدامی «جنایتکارانه، بزدلانه و غیرقانونی» خواند که ناقض حاکمیت عراق و مغایر با قوانین و موازین بین‌المللی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138348" target="_blank">📅 08:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138347">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
تعداد کشته های حشد الشعبی در موصل و دیالی به ۱۲ نفر افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138347" target="_blank">📅 08:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138346">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
خبرگزاری ملی لبنان از حملات توپخانه‌ای ارتش اسرائیل به منطقه تل النحاس، در مجاورت روستای کفرکلا در جنوب لبنان خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138346" target="_blank">📅 08:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138344">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kuvr6BA_HC3i9wi-hE1JgyQEBp66mV9EA0WpodUUr3p_tM5x2E_TbB6Q89a5deOokTMaLt0gXYAZIZIU0fzEoqe5CKJhoVyapu6YA0eoTe7_HMlz8rqhCX7HM8N-AFpUVqaZDec_bcgxrrzjwYkKmKQ5wcnjR_yFr76RN0K2lD9PbH0rRDQ2Ydzq4LFo9dhHFmL_Cu3kWTsQykPytA63L8JdCmjENbSw_eBW3C9lDn8sdMVP67bpNujAXrqlKUrMiRO8FRbaaW5KWxd6Ju8N4LmCtTnLIajDF3bLKR75w3NOTaQWdLQdMOiZe8YEOOlu36rNfwAS1Z0Wcqrb0o9v8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9Fl0fQ6GDc_J_A-8_V2IeuWT2ve-Jhtw2JaDbCXjxikSVYuRvqALt1nWSsSTUt67YrVeUEHWqWep7Jm66t0yLw7GpNY40ePti4oh7d4y4XxokH4cd2FCZ_XqAzVRmlBFGuU0At3PO1XjsY7AOIjurltoISVMDL5KHxr6PErh9lhnulwJ4t6ZIU9o5oXYXXc0y-UA8DnrC8cV955W8zuqh3-d_fpfSz95VRHcUM1y57Lq8-sCMa40wz0gNKeAs1ToDgwr71SgoxaeyPZVbKRXLEej81Y7VORTwfOBotdlq1B0H4ayr7uxPYX6yfcAnLCOoLP7g89z-HqUVb2ZVIwUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گزارش روزنامه انگلیسی از نسخه جدید پهپاد حدید 110: پرسرعت و غیر قابل شناسایی
🔴
روزنامه انگلیسی تلگراف در گزارشی به بررسی نسخه جدید پهپاد انتحاری «حدید 110» ایران پرداخته و نوشته است که این پهپاد پس از یک فرآیند به‌روزرسانی، اکنون با ارتفاع پروازی کمتر، سرعت بیشتر و قابلیت پنهانکاری بالاتر پرواز می‌کند و شناسایی آن نیز دشوارتر از گذشته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138344" target="_blank">📅 08:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138343">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رویترز: پیش‌بینی می‌شود که ایران در چند هفته آینده، بین 300 تا 400 سیستم دفاع هوایی قابل حمل ساخت چین به ارزش 60 تا 70 میلیون دلار دریافت کند
🔴
رویترز: سه منبع آگاه گفتند که انتظار می‌رود ایران ظرف چند هفته آینده اولین محموله از ۴۰۰ لانچر موشک دوش‌پرتاب دفاع هوایی ساخت چین را دریافت کند، این کشور در بحبوحه جنگ با ایالات متحده، در حال بازسازی دفاع خود است.
🔴
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگترین تلاش‌های شناخته‌شده تهران برای تقویت پدافند هوایی کوتاه‌برد خود از زمان آغاز جنگ با آمریکا و اسرائیل است.
🔴
وزارت امور خارجه چین اعلام کرد: «گزارش‌های مربوطه کاملاً بی‌اساس هستند. چین پیوسته در ترویج صلح و پایان دادن به درگیری نقش داشته است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/138343" target="_blank">📅 08:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138342">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42cf14717f.mp4?token=at5Iuu673X1owiNRtW1C7ht-or0MNuRqyBXaDMUOqJ390VfVCYt9pF24srAGs5ie-spjSN2IFDndoa8L3SbXhscaERASek3PA0j4FLjmje5EUzmKeSRf_2VWIRU1EB2ZEQLQOT4Cn6t8ljHApVSDmI88yDt8jj1_p2HWgqL8qyW0-56yXBg8AzdecTug3Kjc2p5lYV4cK8naiPhW8fKnyzb-nZiFoI7JTS9bxCKik9si_MO4wbOmSc3UM0qRQCVz-ureCiNav07ylIBWEPyfgg5x-16IsgCqgVrctzo-wbbvyzJEEvWiUEajgazE2NxKN2M7U0SvAc1ATNLy9K0wDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42cf14717f.mp4?token=at5Iuu673X1owiNRtW1C7ht-or0MNuRqyBXaDMUOqJ390VfVCYt9pF24srAGs5ie-spjSN2IFDndoa8L3SbXhscaERASek3PA0j4FLjmje5EUzmKeSRf_2VWIRU1EB2ZEQLQOT4Cn6t8ljHApVSDmI88yDt8jj1_p2HWgqL8qyW0-56yXBg8AzdecTug3Kjc2p5lYV4cK8naiPhW8fKnyzb-nZiFoI7JTS9bxCKik9si_MO4wbOmSc3UM0qRQCVz-ureCiNav07ylIBWEPyfgg5x-16IsgCqgVrctzo-wbbvyzJEEvWiUEajgazE2NxKN2M7U0SvAc1ATNLy9K0wDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صلاح الدین
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138342" target="_blank">📅 08:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138341">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
تتر با افزایش ۲ درصدی به ۱۹۴ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138341" target="_blank">📅 08:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138340">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
پس از حمله بامدادی ایران به اردن ،کاخ سفید پست جدیدی از ترامپ با متن
« کار این جنگ رو یکسره کن »
منتشر کرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138340" target="_blank">📅 08:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138339">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نیروی دریایی سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138339" target="_blank">📅 08:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138338">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
انفجار انبار مهمات در مقر فرماندهی عملیات حشد شعبی، بصره
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138338" target="_blank">📅 08:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138337">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-BbcZx49WzZH002IEdY40BZSUJuk_E9DkvmOev62KYnJkerMsONeAJyyaoYUlh3WqV9_avLmiYcze0vtcOgcDv8Py2pb1BIm3ErCnGjEHq6rEOIxfQMCMnxBMwPwi2beCz6LbACwfBfuqf2tjcTxpPC3MZej-hexjJK2UBtdeF5r50Zu89rBjmYbehYc2nGFHN5ge5xm8NgT0r3Qh4LalB6Y_oZj41hqLdbx0fGwl49EwxTwPbGWj7o4TdydU9t3HYG0wZ4cUbEc3BbjfEFXY3pO2fyUkMTrbcAIXi6NcYWavt8g2atRAoQ4D7yyJnbpgInnjX2pRt_VgynAa8DAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
آخرین قیمت نفت خام، ۸۷.۶۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138337" target="_blank">📅 08:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138336">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
انفجار انبار مهمات در مقر فرماندهی عملیات حشد شعبی، بصره
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/138336" target="_blank">📅 03:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138335">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اداره هوانوردی فدرال آمریکا:
شرکت هواپیمایی امریکن ایرلاینز در حال حاضر به دلیل اختلال در سامانه‌های فناوری اطلاعات، فعالیت خود را در سراسر ایالات متحده متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/138335" target="_blank">📅 02:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138334">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs2u003JlPLUZpgQuzGkFNVMmhhQNWQoA6_LsxwVgQkV6TsYK3ZIDhTnmZlhGwD9AWb_IiUy7A_7FIvK3CPk-IFuzfAGnbFalEXDhHg3AHt9J1EJ0HIq7vl-gEGMsTTTSQ2wrC8-jpjg5TZbletT-wRWmJw1TyI7UVUXSLOkhEEg-Smbek-jwITTSXnZNCJv6i4tb7dvDs9dO0Y7EJI81oB-ZOi0CqP0sEUIPWlD-fXajTyKpUwGtQLE831EjQ76gREc01Z2JyXeXGYDNedwPtYlRn35LbsG6-b8MNyhMKl4R3HgCnIV0lFQr9jGw2d87B0zfZMZ3ReiYMY7hL9ckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان آمریکایی پس از حمله موشکی ایران به پایگاه هوایی «موفق السلطي» در اردن، بر فراز خاورمیانه در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/138334" target="_blank">📅 02:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138333">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
اربیل رو هم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/138333" target="_blank">📅 02:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138332">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV2QgWy2CZS6DWFZ2KpkylvxTsJ3Hfh6upqlbfs3fs7kZbqWxkLXh-dFs_18b58las5x4bTbP7n9DubvNNbNosL_ijhBc3ZCENsk8L4_Wt0wsoGrpy3fomq2BbZLK-to1jwESw6S6kG3rZfv8PL-D76t2c4enNNtsVqSryot9l8WolZxJRIvfw0KxNKlFClmRjXwmnbXcuo4vCXA8hluxXLO6BZjzKXTXOZGpisXUExLQmMVaBiI00vqCIr8re7ReVt4TDN4QerQdfVNPX7YpnPO-5m-1N-uP1PZLNhUuAL4FE7W-bf4WgVpbRCqo3x4emcdlCl_dyGDbFukhfLZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ساعت ۵:۴۵ بعد از ظهر امروز به وقت شرق آمریکا، نیروهای سپاه پاسداران انقلاب اسلامی در یک حمله غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از ایران شلیک کردند. همه موشک‌های ایرانی با موفقیت رهگیری شدند. نیروهای آمریکایی هوشیار و در آمادگی بالا هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/138332" target="_blank">📅 02:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138330">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
منبعی آمریکایی به خبرگزاری i24NEWS گفت که ایران حداقل ۴ موشک بالستیک را به سمت پایگاهی متعلق به ایالات متحده در اردن پرتاب کرد و آن را یک «حمله بزرگ» توصیف نمود.
🔴
پ.ن: اینکه میگن حمله‌ای بزرگ بوده یعنی یه پاسخ قوی میخوان بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/138330" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138329">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCNWjU9XCS0INN6WrAh_7AosNqK_BuF2zQzTaueK9hWZGZGELr9CdtQ5mB8Pbp0JyS3VDShD5B3XjRkgKhabJB5x7WD1yx3hE2Ftj_-Behb7cGfkDLbORVRIZDeM1Uf-Vne5Y8QMN16oTi1wD4ZBLGqxASfz7TEW7CcYcjnN0u1FRu1XJCeUDGPjgiC6JbHTkioefJrxx2Eq4OjIUmIZwcFIbhw6tkgOYa1y7UcZo7vwa70DTD3K-MX_-OpFLWiPQBLnstosgMjGeF-gz5wcnVXjwTbzkqJxIfcAAdT-Cm1F7pM50bt9s0a24UvHZ0wPFlGkaFJu8Ur1PMyNJUqzQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا هیچی اصابت نکرده، فقط الکی الکی آتش بس نقض کردن و آمریکا بزودی بازهم جنوب رو میزنه با تفاوت اینکه اون هرچی میزنه میشینه و اساسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/138329" target="_blank">📅 01:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138328">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
مقامات آمریکایی: موشک ها رهگیری و منهدم شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/138328" target="_blank">📅 01:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138327">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMYnVMyRl8f7xrqionILSxViIgky5BO9RGD5kAWi26hCMu85G1o1vU5A7zn6ce00mky9eWiOyUC8ErYoBwuVYJVhxJ1GvnZSgR_MKm_SG0WS7pL6w6ASMtLlHUxtgxI4IlqMq8lWObs-ZxjkxnSauUcxF28T_O6o42sxRj9BPCWuK9qztG9sHis4CyQPQrFqFEJ2wln7C0gnSKGhehP_wjUtVg_QZU8sD_w0W0ABIs2jdRaN8DU4AMqVMI5fdztH1eADRc0RrN-S6FGzs97ArQLTq3JUXZ-thWhAp-ZHGcT1FHS6LTQaLAA9VCQAeuuSYLgkcjj_O4fkoAI2eCFlaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس: ایران موشک به سمت پایگاهی تو اردن شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/138327" target="_blank">📅 01:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138326">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOm_2l7Bo8pmwNUhc2k5MUU5RLmT2D_tiVh-6OMIPCaWp1ekc6SF1A_Ma_MNdixM92QijiBlAJxZGHQK5GoE2BMpxCLumyerAPZD56UkuyUb8Q9LIcmpSt4M_gNf13iJceVC1qXYLFefoJ0pZy2GhrREvfxw9QKf-KhM-OFhEgmQ0hQvZw2-dfXcG2J0SNuO5RX7kwSP6MJrrmlR-HHDByCfoNWvdrmvmHBSfgB63eV93w-4rcxHh2PrMaH-E542Pqbinv_YkwjkpvXfldp7lu9sSuaLF3brW0EAbMhuiA7WV9vyS39TsGRanUTidejL0fbF80zGuo9Ljuj3oxlrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی :
ایران برای جنگ تمام عیار کامل آمادستِ
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/138326" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138325">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxuRbw41ciRTtRH7D_lvDFzjIZge5jeimWIx-tMKjfF09sJflePmZoj0AWqdoduZPtf46GeXyjJz37Lq0mOrj-KM6LWpj7OPrY5-88niF3yxKtuRSqQa6YaERx0ESen5XI2xHgwkC70OMCEEF0rfNcyKEFLaEsPXxN4Nj5qUCcZP-6smSP6wAF_wtNwN6pmjg4LHMoOpqZTBD31EIs_yFY8cIGlNa21shggRPEQTLGjM59r07SnAPB2R4CZm-Pk_jM_z1llyLmTczFHyiuBkU8S-OAECxpV-RCUN7pG6ZcmLKlRlsGDYhN66Q1vGabhjTq9fm-gKscmDWqELdhYzQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آسمان منطقه هم‌اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/138325" target="_blank">📅 01:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138324">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
تصویری از ماهرخ عشق ابدی تو خونه تتلو که....... خیلیا نمیدونستن اونه اما خودشه
😂
◀️
مشاهده فوری</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/138324" target="_blank">📅 01:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138323">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوووووری/شلیک مجدد موشک از غرب
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/138323" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138322">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ الان میاد میگه ایرانی‌ها زنگ زدن و گفتن لطفا آقای رئیس جمهور بیایید مذاکره کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/138322" target="_blank">📅 01:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138320">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فووووری/انفجار مهیب در آسمان پایگاه موفق السلطی در پایتخت اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/138320" target="_blank">📅 01:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138319">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏
✅
‏ ️فوری/ پرواز جنگنده‌های آمریکایی به سوی ایران
✅
@khat_akhbar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/138319" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138318">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7b89adab.mp4?token=cvsd5wgE6toWvcWoy1jC4pHqzjsUqOD1XFi_Nas7OxLcHsArU5g1A5A285ngNa2z3Qfpg1an7M7VbmUaByxmHmxiS7_jIi2v5TdHm6sUwE2d0b-ypJ9DFXYOrL817XCnAIfX6ApuVtuNAR9kVpvPOJ8B6dWWLpx0W54HXMeDcLrzI6XlW2159jXl65BDU_w_9i_6rNljL7K6PM9WSRI6J1AK9AKtu1cIVo_4tuuKcZeW75N0MZc1MzY-H-aktDHHyRTuJqR--82x4pMwJOXrymy1BZ5qJQbRSQ9uawRqYwNFtifJYI2K5xFrjh1-PmaeJaL1ej2PiAVhZp0BrAs1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7b89adab.mp4?token=cvsd5wgE6toWvcWoy1jC4pHqzjsUqOD1XFi_Nas7OxLcHsArU5g1A5A285ngNa2z3Qfpg1an7M7VbmUaByxmHmxiS7_jIi2v5TdHm6sUwE2d0b-ypJ9DFXYOrL817XCnAIfX6ApuVtuNAR9kVpvPOJ8B6dWWLpx0W54HXMeDcLrzI6XlW2159jXl65BDU_w_9i_6rNljL7K6PM9WSRI6J1AK9AKtu1cIVo_4tuuKcZeW75N0MZc1MzY-H-aktDHHyRTuJqR--82x4pMwJOXrymy1BZ5qJQbRSQ9uawRqYwNFtifJYI2K5xFrjh1-PmaeJaL1ej2PiAVhZp0BrAs1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین تصاویر از آسمان اردن هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/138318" target="_blank">📅 01:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138317">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سپاه بازهم آتش بس را نقض کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/138317" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138316">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=hytiGO-Orn5eVMsxhdVBvT6BS2cFKVN6bcJtF1teWF972ZInpIavg_SvCqlBgAOi9Ko_GpqG1ci-Uq7YojdLqKUq1odFg_C5g-xMZFBT0iNQRDvBQEz3Ku7Yo_2-quR0clJio8ExvB0cvFTaQ6gw9mwcQh9PmKxuH2VI5NHpZoBU_-qcONh_OrGo0szJbVncj2cj4sByd0o_LipMZ1akTcek6WjXwKTMBR4PDAg24I7-dfje-eI-HG2GXsBfhMWM_ahDAmNxctWHQBpVl66gz0bo0rMRNCSjMQXsMSlZhux8mw5ijAWiBuJ0m52cULCdbILI666qLJPimdVueo59Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=hytiGO-Orn5eVMsxhdVBvT6BS2cFKVN6bcJtF1teWF972ZInpIavg_SvCqlBgAOi9Ko_GpqG1ci-Uq7YojdLqKUq1odFg_C5g-xMZFBT0iNQRDvBQEz3Ku7Yo_2-quR0clJio8ExvB0cvFTaQ6gw9mwcQh9PmKxuH2VI5NHpZoBU_-qcONh_OrGo0szJbVncj2cj4sByd0o_LipMZ1akTcek6WjXwKTMBR4PDAg24I7-dfje-eI-HG2GXsBfhMWM_ahDAmNxctWHQBpVl66gz0bo0rMRNCSjMQXsMSlZhux8mw5ijAWiBuJ0m52cULCdbILI666qLJPimdVueo59Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک‌ها به اردن رسیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/138316" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138314">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLfrZccynpS33fDwWTgS0Ua5t_2DGFSaOPKPVqnmMfUIxx4nYZJEoEBD3I79FQBsr0lClJdbxiJ-Me4icVQjBQWUEIqFd37BettR2ICeNOGs3uqk23j6QRBT9B3qdYsQg9EN-V07tJT2cMdLeM0Dalx-IHgDXB3TBBz3rdU24gWHMVYl2N5P0zNr2tP3HpTyqpnj-Za9CsZiSnnDoeo8cy0MwHK_xnYoedXrbcYvWLEIHQg5JEqnNiRSZYv6cX83Z5F-b8qcvYKC-OAbTLjfqNAPN5AkWLq1BKRPXyr4KjnZnlkaShR8VvIIa_fsZHCYQDnetiLAAic2I6YpnIhydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/شلیک موشک‌ها از خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/138314" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138313">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
گزارش شلیک موشک از زنجان
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/138313" target="_blank">📅 01:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138312">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/6 موشک تا کنون شلیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/138312" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138311">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/سپاه اردن رو زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/138311" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138310">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8StNUXgF7js0eXANr5xnALUp-tFwTRclEcp2EF-qeZWIC-Q3ocyWBlb1l_GHI-SsYPRCBDi9-xM59ynStHVIDRvv1yjHyIdVVO0oZaIwOC2QavWqREd6DB_nuyDjHKIkMQHVg_d9tuIjw3U8PIbymM_MJ7ro0_1I8KnZee_Bjo_fIhX0vNmfqTZga8aFN_JytUx27ocXZtRORz5jizVTsZeq84QWhBTpUvXj8ZbIbaqGjwo8XvZirwUaOGBwGYKRE1q1LpffqGzAXLQQv57XZCJVhWnKaFQIxBdjdaaQK2v3uJtJ4IdORFJ9nUYQvy5S6l-dvYR2XRPUF9XU1jxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/دقایقی قبل از خمین ۳ موشک شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/138310" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138309">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری/شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138309" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138308">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf75b734fc.mp4?token=BwFI3kSErsJsA9B_oA1DJ5TSRMB3PI1iNk6gwW47zCgrmRrTh8KmoYrG2UsWt9ekoF8-5Tp2Z1YaDrKvMSa6uenha5UXjOBlJaCkPsDIrskWOsCMU-qA4nLALheONyY_hPIytl1Gyb1q26XYfB1rafPL-NrDPvfJPqWtLj_W3RvVlq11T1u3wMMNOt_9Q1TzWmLQAy0YRl1JULt9zYcm5Jdueou5AE3zU1LHAA3sj3dL-4pFzWiPyS4Eqjk7vRz0v9Bc3wORh64IC-5pOIRz7Nm7S1-TAHsrV9K577eBGLfZXGgigyuYc4CvsH_stTxyfi-UXpPbADQGdVsr1j-FmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf75b734fc.mp4?token=BwFI3kSErsJsA9B_oA1DJ5TSRMB3PI1iNk6gwW47zCgrmRrTh8KmoYrG2UsWt9ekoF8-5Tp2Z1YaDrKvMSa6uenha5UXjOBlJaCkPsDIrskWOsCMU-qA4nLALheONyY_hPIytl1Gyb1q26XYfB1rafPL-NrDPvfJPqWtLj_W3RvVlq11T1u3wMMNOt_9Q1TzWmLQAy0YRl1JULt9zYcm5Jdueou5AE3zU1LHAA3sj3dL-4pFzWiPyS4Eqjk7vRz0v9Bc3wORh64IC-5pOIRz7Nm7S1-TAHsrV9K577eBGLfZXGgigyuYc4CvsH_stTxyfi-UXpPbADQGdVsr1j-FmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مجری: عموی عزیزم‌ محسنی اژه‌ای بابت اعدام‌ها دمت گرم
🔴
پ.ن: جواب با شما
#عموی_سوباسا
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/138308" target="_blank">📅 01:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138307">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082980e3dc.mp4?token=TBDHw9KgN6pBxPQwAubuzimNtY86NbmHN9GKyjl74QnduaEPcqlLPdBbteVTgvB8dJO3TWjt6mEV0VFX5cA3UVLizWWGDkO7eMvKpcNmdya-WZJzim6jdUdNWcCdy_HVZ48ulL_AyRnOXkM-Xv59lJsIIgswIcwyl9cV8qc7lWZoPgWoOMcgl3gSuHnJK0VCVM6lY46n6qP4RwhES20TgZknKOlozI4hkqmrN8vF5RIql3V9yRAVWie6LTZIqPEHvbBa3RSRANM5vOxs7b0Big9LVONVyao1Oq6JEC595t51spI11YFrSZ6-bFF_oGPhIn-7lwiAe1KraRDT-gdETTolSqic6DanqseNOZLvM1Wy6ZI0m6vnGejMOFoHKaRKQCH8QfmCOuSglMkIDIIgYNedB5kLypQpgLSIn3xHESFqE5xBzsJDFMng2PDIs1b5dl0u29zsxqzAQjX01naQEPTtfPF1m3uXZmpO21Qo1W9jo9IHvKWMSSIba8bq6jfC_b-dhdi4rOQkrqCT98LSmBHc1ef-_rJ4pdwYCLVo7OXIDA_zmQK7cEIxCxnnoQH_PVw42S3nhk-1ElXjieLIwbRENEah63SRBMsyMv-XNWXfwu_vpI7cNE7OKRg6hxvI5pFT41QUg7ZSxb5nje680BTCdPOgtOEpf40Fp36hyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082980e3dc.mp4?token=TBDHw9KgN6pBxPQwAubuzimNtY86NbmHN9GKyjl74QnduaEPcqlLPdBbteVTgvB8dJO3TWjt6mEV0VFX5cA3UVLizWWGDkO7eMvKpcNmdya-WZJzim6jdUdNWcCdy_HVZ48ulL_AyRnOXkM-Xv59lJsIIgswIcwyl9cV8qc7lWZoPgWoOMcgl3gSuHnJK0VCVM6lY46n6qP4RwhES20TgZknKOlozI4hkqmrN8vF5RIql3V9yRAVWie6LTZIqPEHvbBa3RSRANM5vOxs7b0Big9LVONVyao1Oq6JEC595t51spI11YFrSZ6-bFF_oGPhIn-7lwiAe1KraRDT-gdETTolSqic6DanqseNOZLvM1Wy6ZI0m6vnGejMOFoHKaRKQCH8QfmCOuSglMkIDIIgYNedB5kLypQpgLSIn3xHESFqE5xBzsJDFMng2PDIs1b5dl0u29zsxqzAQjX01naQEPTtfPF1m3uXZmpO21Qo1W9jo9IHvKWMSSIba8bq6jfC_b-dhdi4rOQkrqCT98LSmBHc1ef-_rJ4pdwYCLVo7OXIDA_zmQK7cEIxCxnnoQH_PVw42S3nhk-1ElXjieLIwbRENEah63SRBMsyMv-XNWXfwu_vpI7cNE7OKRg6hxvI5pFT41QUg7ZSxb5nje680BTCdPOgtOEpf40Fp36hyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعال رسانه‌ای نزدیک به اپوزیسیون: طبق اطلاعات محرمانه‌ای که به ما رسیده در دی ماه 378 هزار جاویدنام داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/138307" target="_blank">📅 01:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138305">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk989u_w5Uz6WOnRBC40nMUv4Wz3OumBBmevjjkGN03ZC2mGjqn6gMwP-wXxTNT5NPbdgKfm8brSpdyv-SbYQTf6GvMlShZyoComsgpVGN7W4B6eTuQ1FKgXvNEEt9tbta6ip58c1anccMLmzXmM8mNZsmXJw_oMiyYjxQY729pzBF2HKETB1vkeiiuI7vB-xcsE07iM5z-tM52y9oLPiQ-yZyOOHSSTcnwp6iHfqeKTAmcpcV2PA4CSKOGIHOnReXGvPQscxckhvBWbOoyvNRCPGjya-iWOiVf_RtT6hpzEF7FyCcJ9dOGOFs327hv2nlHRGdyS5SD4t08rH4eYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ما میخواهیم زیرساخت‌های انرژی ایران را هدف قرار دهیم اما آمریکا ممانعت میکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/138305" target="_blank">📅 00:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138304">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خب بریم یه افشاگری خفن از ماهرخ عشق ابدی</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/138304" target="_blank">📅 00:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138303">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
واکنش ماهرخ عشق ابدی به اعدام‌ با خنده:  «اگه میتونی برو جلوشونو بگیر، تورم بکنن جزو اونا، بشی چهارمی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/138303" target="_blank">📅 00:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138302">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vflMcb9ylxZ36mMpwr9fjUgBZ6zYSbynOrdzTBdLcSXr2vGoxaqtnAxHYBdUsaBqZMVO2NdjDs30xqAUxpdZe8Tyfj5BGIy7ZZesvYmw7o-TdEXDWPbvA3GZPkaeA14ilionVcMZCoPnwA1NxvoC3h8kIPDFBpI9PakIvuIiT-eyzj3GGwepJB6ECPRNBntgFLTRFzmYqFny72zFWUjLqJfUUKferLJn8q-4J_I0mjksq_-mR0ANgDytoS9iCsjZW-gJJ020yM-WRVVqmG30jdIvyPbnuigARVvQmIgWhEvXu90s6NHoyZ_Q237NR6peZIIdRReU0bHqghJZ_HGQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخوندا هم به درآمد دلاری رسیدن.
🔴
دولت اومده یه اپلیکیشنی طراحی کرده تا ایرانی هایی که خارج از کشورن و نمیتونن برن سر مزار عزیزانشون یک نماینده بفرستن تا قبر رو بشوره؛ شمع روشن کنه؛ قرآن براش بخونه و ....
قیمتشم از ۱۴ دلار شروع میشه تا ۱۲۴ دلار و هرچقدر کارای بیشتری کنه پول بیشتری میگیره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/138302" target="_blank">📅 00:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138301">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کانال i24 عبری:تنها چیزی که ترامپ را به سمت امضای توافق با ایران سوق داد، قیمت نفت بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/138301" target="_blank">📅 00:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138300">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با برادر خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
🔴
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/138300" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138299">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvHR4Sk0NpiOKp9Ouz2S-vWLzWEH70Jota4gF-p3TqA2w5OdWO4PshlqiGWTP_z3O_t9_WBRPoPQz4_65ycrsO3-eXvaZ6PttZxpjJ6TDAeBui93RxTLxMTqPmOA_SgUWFGi-QFjgc4zTRWft_CddPmhEsb-R6ABmUv07tCya6Dp3Wykn9y6R5_LWs1Db1BzWQdpYuk0ZqI18X5zWcPK8GfWxgkx6B6RHp3SfgCqFknT7A9Yw1tAQogCwGMCjhj1xssZKroXvAKhv9n82L3XXEH5ujkO2TPEvhbnYmIcLbJUbRM0z1EBt_LBUvRdVNy4EBXYLCF4urS6pgIP4Tmxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گفته‌ی محمدی، رئیس اتحادیه رستورانداران مشهد؛ از ابتدای سال تا الان ۳۰۰ رستوران تو مشهد تعطیل شدن.
حالا دلیلش چی بود؟
بخاطر تورم؛ گرونی؛ کاهش مشتری؛ مالیات سنگین و... که باعث شده بیش از ۲ هزار نفر هم بیکار بشن.
الان هم رستوران هایی که دارن کار میکنن اکثر دچار رکود هستن و مشتری ندارن و اگه وضعیت با همین فرمون پیش بره اونام تعطیل میشن.
تازه این مشهده؛ با وجود کلی زائر در سال که باید اوضاعشون بهتر باشه اینجوریه، وای به حال شهرهای دیگه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/138299" target="_blank">📅 00:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138298">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBa8kSM7eJlezcpv8hbdkYteY09vi0WLSWuxOK_GgHi0M1ZZwvmADBsWZmC56uh3_NKkwo4IU2LL3hH6ARe-zp8ziGAlvxbdw5jbtjNQnGWW3riu-13KQlvOJKIrUkV61ORiO6P3I4G2UqHrxeYsKCRuyXj-FN-b9nT-Ej8WpSg-JwozX9BWIQnZJD-BkKkaMuRIhSk4vHY-jx90rQV629lrrqXcjLV7GojVVd8JEc0d8c40BVVTmcBkzzxaY-mYKLlGW6eZDKyFOGWUE93OVTvJ8m_-r4uJ6s5cmYpGpSUA3YqbDOMNdlVu3Erw7f9DMFA9LIN8pGTkqkdN3pnR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نقل از رویترز، یک مقام آمریکایی گفت:ایالات متحده معتقد است که ایران در مطالبات خود در مورد تنگه هرمز اغراق می‌کند، به ویژه در اشاره به درخواست آن برای کنترل بیشتر بر تردد در این تنگه در جریان مذاکرات با عمان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/138298" target="_blank">📅 00:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138297">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
عرزشی های حرام زاده میگن رضا پهلوی با فراخوان 18،19 دی باعث کشته شدن هم وطن هامون توسط حکومت جمهوری اسلامی شدن.
🤔
خوب پس طبق روایات خودتون میشه گفت حسین هم باعث کشته شدن مردم تو کربلا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138297" target="_blank">📅 00:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138296">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
مقام آمریکایی به رویترز: توافقی در مورد تنگه هرمز که بحث درباره آن جریان دارد به هماهنگی مربوط می‌شود و هیچ‌گونه اخذ تعرفه را شامل نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138296" target="_blank">📅 00:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138295">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
کانال 13 اسرائیلی:مسئولان ارشد اسرائیلی اعلام کردند که "اسرائیل" شاهد یک عملیات بازسازی گسترده‌ای است که توسط ایران انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/138295" target="_blank">📅 00:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138294">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
در حال حاضر هواپیماهای ترابری نظامی فوق سنگین آمریکایی به صورت پی در پی از اروپا به سمت عربستان سعودی و اردن در حال حرکت می‌باشند،
یک پل هوایی نظامی تمام عیار از اروپا به سمت خاورمیانه در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/138294" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138293">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رویترز: در حالی که ترامپ مدام از مذاکره با ایران حرف میزنه، طی چند روز اخیر گسترده‌ترین تحرکات نظامی و لجستیکی آمریکا تو منطقه گزارش شده.
به گفته برخی منابع نظامی، آمریکا در حال آماده‌سازی خودش برای یک جنگ تمام‌عیاره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/138293" target="_blank">📅 00:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138292">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
اولین تصاویر از بمباران آسایشگاه سربازان بمپور
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/138292" target="_blank">📅 00:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138291">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس: وزیر خارجه(عراقچی) به جای اخراج کاردار سفارت اوکراین، به تلفن وزیر امور خارجه اوکراین پاسخ داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/138291" target="_blank">📅 00:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138290">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5MmvRgQcnncyW1rL2FZ9T7hKw_jAaX1vwI9-ZttrPsUFglVeok_o2dWamtfbMAwJmoqHK4lz6Ww3bFF0BQbQtrUlqw1H7Bq6Gk32JFWpLwzaq92rVrtsrM4uBgmlJY_TYPZ-E9lY8d5o07SCj7Wx91MhuKuvnTTM8_JYsvUusopWYK5msfSdXryJBulbWpTGi_q2JJ4LV9r-iSt9Q1Pl_bWCrUA2Sq_9-tAEkfL7uvek2g55UU0nACLdVGurBzML9SkBZMbLmvanpDCpuT3WdsQM6FBcgTENd06lIdWMApz7IuJ9YCMnWw0R84lheT06WSD287Wxu9jNRQji0grmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: اعدام هم جزئی از قانونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138290" target="_blank">📅 00:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138289">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVd_uzNTodClr6BkG7laXX8XBGgmZWmtdiqAaUL8GSgowZGd8YfK_bFFsnNN5qqvw2E3_Wb_AUc1PcdsrMBb-eaUl1NSozlC4d39Ve9EAuY2UdAmZN0dJ62M9kHg5zQCmymxsS4oBaCReDMXw10jtAH-HDJC7YGVBlji4b8o_u0dmYML0iJJkMWDs7knRbUQw3MRi8TWd6_C9C-kAbTvZYSrmWOxI2Czc7F7J2EGtkt2Xizsw-klJySmgtmu9S2yfJYy4fbGKXAlF2LsWW6iWI96f8xFzHkXGvRAOXRBqZOUQ9c8XCzGzbdXNzXiK2R5f332lQIptX8JIkuDlVq74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس:
نصف مردم آمریکا می‌خوان نتانیاهو رو حالا که تو کشورشونه، بازداشتش کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/138289" target="_blank">📅 00:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138288">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJE1sVRxgNmab_qXI_Fkx5F4OyXhoMtqhKjMyO_QWJu9n6M6AJl_538cQ5ZhI_SEhRlAqy4IMF4B-I9upw7CdHlg3nYC4HGh_CXi8vzVe8xSFSYFZPSZthkFTvZSGz8IKOTbLNLlp7Ifu7Dn76gliOfDBq4jK2w3fOLrE6hVBvqbkivjmgsEwjjjkiJZgvaLOUfjuo3B1xjySCl5KANvETrIoLUas0SJPb4GP9PqwVC93Ipcdftc992lGRjNsOOD2IlsaJIrIUwNaMSPkQKwz78bjv80i1qt3lXh21RGo0kCxB2AHUtFOC8r9I9dxa8RvXlW0uNBzwGx8SkWiojcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏شریفی زارچی، استاد سابق دانشگاه شریف:
🔴
‏به محض آن‌که آتش جنگ اندکی فروکش می‌کند، چوبه‌های اعدام علم می‌شود.
‏جمهوری اسلامی باید سرنگون شود تا ملت ایران رنگ آرامش ببیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/138288" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138287">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
عرزشی های حرام زاده میگن رضا پهلوی با فراخوان 18،19 دی باعث کشته شدن هم وطن هامون توسط حکومت جمهوری اسلامی شدن.
🤔
خوب پس طبق روایات خودتون میشه گفت حسین هم باعث کشته شدن مردم تو کربلا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138287" target="_blank">📅 00:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138286">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
واکنش ماهرخ عشق ابدی به اعدام‌ با خنده:  «اگه میتونی برو جلوشونو بگیر، تورم بکنن جزو اونا، بشی چهارمی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/138286" target="_blank">📅 00:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138285">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2c14506f.mp4?token=nRSeD69ukQWjPzXeP1p8tioY3soe7w4Z2RQWbVLi8ItWaenE-VeZLSBLI8MLFnJs8TzO1Pq1w0Ru-idrF8MSA2pV-6ZjST7zjCkcrmE6fbIiCgtCUxx0goZwhpkMrjyBrMGlCX6oaqkIrN8Ub1Je7s5UiJIaflTGPA_vT1MKVQzL5UP1ocsM6212MBankOmgfVRFqCn608ADP09_50DlqqfM6IY2jDptJrSv_9LeiYb1FpFmAYOwum80B3huRmuOQ9vLH9CCJtpmSN_uB5hgKgh_pZ-gg4xHtLekXaF4iDszpqXPu_Mt1ccZ6Z06s_WpzKZO3oNdj-PG26ZX55rW8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2c14506f.mp4?token=nRSeD69ukQWjPzXeP1p8tioY3soe7w4Z2RQWbVLi8ItWaenE-VeZLSBLI8MLFnJs8TzO1Pq1w0Ru-idrF8MSA2pV-6ZjST7zjCkcrmE6fbIiCgtCUxx0goZwhpkMrjyBrMGlCX6oaqkIrN8Ub1Je7s5UiJIaflTGPA_vT1MKVQzL5UP1ocsM6212MBankOmgfVRFqCn608ADP09_50DlqqfM6IY2jDptJrSv_9LeiYb1FpFmAYOwum80B3huRmuOQ9vLH9CCJtpmSN_uB5hgKgh_pZ-gg4xHtLekXaF4iDszpqXPu_Mt1ccZ6Z06s_WpzKZO3oNdj-PG26ZX55rW8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش ماهرخ عشق ابدی به اعدام‌ با خنده:
«اگه میتونی برو جلوشونو بگیر، تورم بکنن جزو اونا، بشی چهارمی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/138285" target="_blank">📅 00:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138284">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXNDKzDTYm47FALR0ut4Qd_-FeBEH48NG-9yRRl4n0dhx0-50OUYJnu97ex78e41o6L_22B4iHVW0136-dnR3xYyK1BawsD5ax6EZ22spZ0bZJ1ubUO3mJlVbzQL706yZpewHch0yEuDvNEKMVX_XTe3eb0CyaJFY6NA9OOB_sQlPVuJLnRKfJJPKoP8vj8J0bN8tuABlrkyY15zjPpLkINtskOH3iaYf22jAqp8vtSrAEDGXbYC7WfDOYSGMzKtO52bLvB7jPUZTo-RVGjDO7gSpxWpDCId_Z5eUFkXlWocRg7RPkXiy36VQIF4Qq320LMd90G2_E2EsSXilqEtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
حضور رضا پهلوی در مراسم لیندسی گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/138284" target="_blank">📅 23:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138283">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bee079a9da.mp4?token=QK4RpoPNXVOhaIH5WOEdkOz-0t8v4X_OdKGkPDFvDXnV0dar6pgIhUc-VmR8wnVvBAVPR8CFQyT5gZN2vJsIYFTnVCCphZ57igo9SHGC1DFIy_wToRO73sMDTevBXra169phca7YOE1-XGlYDtdgE6wVgHyyJubdf7U6so8tRIUar6UeC9lQ5PotezZfdAlojhbasTZeKEzGqnbi2NdvFWWuRsK3qBK7opKqbVdqlVAUobiCtUe00ZdZ3cWQgNb-AaFitb9msgmMiZixDOBQe6lc60J3PJSesvoEr0XLRe-nPBnWjsLzu15I0qzgX9D-HkJp-qO7GV53VkcdPkVnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bee079a9da.mp4?token=QK4RpoPNXVOhaIH5WOEdkOz-0t8v4X_OdKGkPDFvDXnV0dar6pgIhUc-VmR8wnVvBAVPR8CFQyT5gZN2vJsIYFTnVCCphZ57igo9SHGC1DFIy_wToRO73sMDTevBXra169phca7YOE1-XGlYDtdgE6wVgHyyJubdf7U6so8tRIUar6UeC9lQ5PotezZfdAlojhbasTZeKEzGqnbi2NdvFWWuRsK3qBK7opKqbVdqlVAUobiCtUe00ZdZ3cWQgNb-AaFitb9msgmMiZixDOBQe6lc60J3PJSesvoEr0XLRe-nPBnWjsLzu15I0qzgX9D-HkJp-qO7GV53VkcdPkVnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران مداوم مناطق نابتيه الفوقا در جنوب لبنان توسط توپخانه اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/138283" target="_blank">📅 23:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138282">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/919fe2f821.mp4?token=kFVgpqGxOziFmmNtPK46edRAQ-npOqxx6ZZztWQfbwhX8lQqbKuMThr4HtlQjr4hLuY8pggXyff1qZ01QbsFBgOmc5H9TRc5fDe5n4peyNZ3JpnDUCDpFkpmFbwLWVk44A3Sp1mD-ckeuqp0NZhL64Ffy9elvwDhhtZc3Yk09pE1JYaCSEO37lu_N7IEy4Y7gE_6JsaEnhLXYadSk9fg86U1xqSitVuYD146KyWFHOrm9P3Ml13MNNXT8iHqBy_JRPsYKzZDHfZ6c9v6a93BFbHcGFJPFwBLZ0tuOCD0p7bN-nEhh8HuvBnIkQVqwle8Vu5vX_4Qpt8PbbQQFCv60A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/919fe2f821.mp4?token=kFVgpqGxOziFmmNtPK46edRAQ-npOqxx6ZZztWQfbwhX8lQqbKuMThr4HtlQjr4hLuY8pggXyff1qZ01QbsFBgOmc5H9TRc5fDe5n4peyNZ3JpnDUCDpFkpmFbwLWVk44A3Sp1mD-ckeuqp0NZhL64Ffy9elvwDhhtZc3Yk09pE1JYaCSEO37lu_N7IEy4Y7gE_6JsaEnhLXYadSk9fg86U1xqSitVuYD146KyWFHOrm9P3Ml13MNNXT8iHqBy_JRPsYKzZDHfZ6c9v6a93BFbHcGFJPFwBLZ0tuOCD0p7bN-nEhh8HuvBnIkQVqwle8Vu5vX_4Qpt8PbbQQFCv60A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ تعدادی قرص "تیک تاک" (Tic Tacs) از جیب خود بیرون آورد و تعدادی از آن‌ها را به معاون رئیس جمهور، جِی. دی. ونس، در مراسم خاکسپاری سناتور لیندسی گراهام پیشنهاد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/138282" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیران امور خارجه اردن و پاکستان بر لزوم موفقیت آمیز بودن تلاش‌ها برای تضمین پایبندی به توافق آتش بس میان ایران و آمریکا تاکید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/138281" target="_blank">📅 23:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgjVuPWpOToppH7NqUl9aq2UAFOSRQZbaB5bsGc5jqrEnFaq-pEeqezLo6c8thStw0_elgRL5k3cRJjhFySJxiISIlcYapH1c7A7T2Jlo8JEC7F4MD0hnHpkefk3B9m1T0ouD45cT9fyb36vjleQK25AirMJpycQpHJHp8La0zECcnl8K_VV-7k9GbUfHQfP7m5OHbL4QoO0oGlgwKw80spB42WjqWLfnmxUMvv4WGT3Kxa86JYkomX1N3hGqV0kDBVLmXURuytWC_6d5kiOlI6TOQbQbi46wV_xn5UcBtm4J5GIycgGEV5hhKPf1xue3cPINQvqo0SnAfVSNdvTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت 83 دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/138280" target="_blank">📅 23:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/692d5412da.mp4?token=m7Hl7G_te0EAelvqFnFiKkasApPtSSXvQLC1K6fCj16Whx2JIBgBEblMmH7LVHtyQGEXtsIR6ol-8cwIt0w3YoZUCTOrtWBRoTnFPSh4wHwMVL5HCJ0UnHDAgA2wMRh2H_HiTmQgELKVu9mYTBLjhyD4sH6RthUbqRWjJ3MuF9yWAnJQbybHrU1V6HG-PXujBmsYBc5a1wRvqRYKFet3YhBtKtWbjN1-HSTJF_SJUVWxA9tS0ljK-_rR3l7OrO19THZuULgD3uuOlfVvAGNAD6l97ujG02D0nqKgZVc1RqmA131NXCeY9HNN959_TCBGv-GAWdbyTnwUHjyuc_Yvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/692d5412da.mp4?token=m7Hl7G_te0EAelvqFnFiKkasApPtSSXvQLC1K6fCj16Whx2JIBgBEblMmH7LVHtyQGEXtsIR6ol-8cwIt0w3YoZUCTOrtWBRoTnFPSh4wHwMVL5HCJ0UnHDAgA2wMRh2H_HiTmQgELKVu9mYTBLjhyD4sH6RthUbqRWjJ3MuF9yWAnJQbybHrU1V6HG-PXujBmsYBc5a1wRvqRYKFet3YhBtKtWbjN1-HSTJF_SJUVWxA9tS0ljK-_rR3l7OrO19THZuULgD3uuOlfVvAGNAD6l97ujG02D0nqKgZVc1RqmA131NXCeY9HNN959_TCBGv-GAWdbyTnwUHjyuc_Yvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نرخ جدید دیه : (دعوا هم دیگه نمیصرفه)
🔴
دیه‌ شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
🔴
شکستن فک بالا : 160 میلیون تومن
🔴
شکستن فک پایین : 640 میلیون تومن
🔴
شکستن هر دندون : 105 میلیون تومن
🔴
شکستن دست : 160 تا 210 میلیون تومن
🔴
شکستن سر : 120 میلیون تومن
🔴
شکستن پا : 210 میلیون تومن
🔴
شکستن گوش : 350 میلیون تومن
🔴
کبودی صورت : 6 میلیون تومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/138279" target="_blank">📅 23:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138278">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdvMlKMl7BTKhIJsbhQCAgcu--6awgCnES7gHrMdTSZEHjfLauZlpTjjB5FHbmdGxTVaWAKqkA1OeF_DCNCxVo8sCo6fCaSfcuy8yK2E3Pt1J4GrG16HQSIL26_5L7qmBnAM4tbJRdCTw2MlVqhpGIMpwxFKJOwZ2Zh3dcnoZvlj9woKat2nq8ZzmPJ9_ywbyOBf5Rvf532ju8Qn_TfmsyHy4ziF9Nw4rfnRH9xfX66WzdMp16jF8UINz8Q54iIyFRjDwNX4T8psekdUrReI9Qul262Y8c-lQV3ed4WmU0CLh-KgMfE2D507aYT0VS-T0JKnBo01Q7vaQveffHjfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار کوتاه زلنسکی و نتانیاهو در حاشیه مراسم لیندزی گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/138278" target="_blank">📅 23:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRoTs8r2eY_Zo6npCPCLoauL1MVazFk-P8A8hZrEfQ1gAq5MVIehw3u7oy_QK2veXQ6cAae1KBviDWAUOe1Fu2mZCvb4AtaT-k1ixrLLpz7qvFT0Oei-O6hQDEX7TxFaqaVe3SeYnL0fDGDOiK-ka28g1WdLl_zFwHQLEMst_vXLDVPTli6jyAUE4p8pqx1yC05_L7djCuvSEfn7Jch3jiXspWq4VeCNTLLgwH7Uv-iI5sFfY3FcgtbixPVUwS1bK2K_G3E7Cs2zBMm9GWtSc3RCXzm9q4M3k8qrxZnXj7WjLqq8h74CxYAtAPSWEZwTXkHRL6T-Izi4z6lRkY_JeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان UKMTO (سازمان دریایی تجاری بریتانیا) اخطاری را صادر کرده است، در سواحل شهرجازان، عربستان سعودی. این حادثه در تاریخ ۲۷ جولای (تقریباً ۷ مرداد) رخ داد. این اخطار پس از بیانیه‌ای از سوی گروه حوثی منتشر شد که امروز ادعا کرد به تانکر سعودی به نام "NCC Ghazal" حمله کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/138277" target="_blank">📅 23:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
جروزالم پست: نتانیاهو به‌صورت محرمانه به ایالات متحده سفر کرد؛ پس از آنکه نهادهای اطلاعاتی درباره تهدیدی از سوی ایران هشدار دادند.
🔴
بر اساس گزارش N12، نهادهای امنیتی اسرائیل توصیه کرده بودند که پرواز نتانیاهو در شرایطی کاملاً محرمانه انجام شود؛ زیرا گزارش‌هایی وجود دارد که نشان می‌دهد ایران تلاش‌های خود برای هدف قرار دادن مقام‌های اسرائیلی را تشدید کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/138276" target="_blank">📅 23:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
تسنیم: طبق آماری که به دست آوردیم ۷۵ درصد مردم خواهان کشتن ترامپ و نتانیاهو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/138275" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138274">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
عربستان : چند پهپاد رهگیری و منهدم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/138274" target="_blank">📅 23:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138273">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbvGZA2z9UuTBPYzUdk2XzvLsEwWqIIayAhOGObVtgNmkU-QLWqvPz-tcCdrh59QejlMPPqZWf0IbupnRJxo-TgEscDbMX-HLxpAXVzPrRsLhp8c7x1guln95yMunbads6lquL1HIFhmMLkoNcevM4kqWMfjrc5wyNqtegw94MHKJ3284xwCrHREHqRXzCI7ragSfMEOwuAr6Qeatak2aWBWmHvF7BmbyFoQshAhqShNCXZ-8IjdSRjgGCgxsyqOc_xsHcHXVmLuwouMnItqvcDvwUWmgzOlMYBAeKclIQu7OvnVmDh6ChWsFw6kzkZVDeyWYzXwYjV9fnZ-5c0fPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">POUYAM SMART CITY
آینده از اینجا شروع می‌شود.
یک شهر هوشمند دیجیتال که در آن شبکه اجتماعی، هوش مصنوعی، سرگرمی و فرصت‌های جدید در کنار هم قرار گرفته‌اند.
به آینده متصل شوید.
🌐
https://t.me/POUYAM_APPBOT?startapp</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/138273" target="_blank">📅 23:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
خبرنگار المیادین: صدای یک انفجار در حومه اربیل در کردستان عراق شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/138272" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138271">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
خبرنگار المیادین: صدای یک انفجار در حومه اربیل در کردستان عراق شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/138271" target="_blank">📅 23:04 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
