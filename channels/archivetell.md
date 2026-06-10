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
<img src="https://cdn4.telesco.pe/file/SAXMoVtsV5vR8Mog_ilzAdmm--ujVL-CFGa14rQ3HeKF_xndggELlVFR2poMfLXUaQwW-KXF4Pj5nozdcBGlPcmbHltWBzYyjZ0ntuwc0lO6gw9Ro2CyBUehzORSYrpgO-BAKYKoNKYFtZv59lHR-d5xjs51a15wGQs_GEixklfEikEyc4HkaWJ5_hqbL5oF4OZQO7N-aB8Y1GEot1NVP2ZRuyOgVAsCrSLPzayCxckdBELFjoh2C3E8Jji13afu1T-p3l-cGXapQueKwZldNz40cHDtfKwAdx0ZegYeDLDmOjMVs0n3xX3wyQx3oXos9utSefgOyfKezXRsR7b3QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.6K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 18:02:50</div>
<hr>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سیستم جدیدی به
ربات
افزوده شد.
✨
از این پس، در بخش
سرویس‌های هوشمند >> آخرین اخبار
، امکان دریافت اخبار روز ایران و جهان فراهم شده است
📰
🌍
هر دو ساعت اخبار بروزرسانی خواهد شد
✅</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🦀
Asterinas 0.18 منتشر شد
پروژه Asterinas یکی از جاه‌طلبانه‌ترین پروژه‌های متن‌باز دنیای سیستم‌عامل‌هاست؛ یک جایگزین مدرن برای لینوکس که تقریباً به‌طور کامل با Rust نوشته شده و روی امنیت حافظه، کارایی بالا و سازگاری با اکوسیستم لینوکس تمرکز دارد.
در نسخه 0.18 تمرکز ویژه‌ای روی اجرای Asterinas در محیط‌های کانتینری و مجازی‌سازی بوده و قابلیت‌هایی مانند Namespaces، cgroups و بهبودهای مختلف VirtIO به آن اضافه شده‌اند.
از دیگر تغییرات مهم:
🔹
درایور جدید NVMe
🔹
بازنویسی درایور فایل‌سیستم EXT2
🔹
پشتیبانی بهتر از نرم‌افزارهای لینوکسی
🔹
اجرای برنامه‌هایی مانند Firefox، QEMU و Codex
اگرچه Asterinas هنوز فاصله زیادی تا جایگزینی کامل لینوکس دارد، اما یکی از جدی‌ترین تلاش‌ها برای ساخت یک سیستم‌عامل مدرن، امن و سازگار با لینوکس بر پایه Rust محسوب می‌شود.
#Linux
#Rust
#OpenSource
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 435 · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانفیگ ناب اهدایی
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYA7WLdMe8FtcxNLqft5ndwGH6eatcxS27Df8fUY_M4KL03wXtzmJsX__Uo9OACIbNrgO29IwatuHdjyoB_Efr_Ol-F_MjvMDRGMiHRaFhk1IBZX38IgfGuxeS1Ro60BMteK0MblR8MbogYNI2jGlYNBbbnAw1VJo7QgsKNFak7PLbIXSA3GA3s8eQIIdaQkW8dlOFpL7GnEBPtitRDlFzFSXDo2qkm0eZbzxjtbjh78Joca56V3KcmGpjJRliv3Kem0O3Vj6-qRc91rhfirxskZECVNdwEK1fE6HMOZUQMLn8ajO7lciYjyZPGJpOXnLOFSmPX-l9g_JOrW4lQ-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
یک ویرایشگر ویدیوی رایگان که مستقیم داخل مرورگر اجرا می‌شود و فایل‌هایتان را روی کامپیوتر خودتان پردازش می‌کند؛ بدون آپلود در فضای ابری.
✨
قابلیت‌ها:
•
🔹
ویرایش چندمسیره ویدیو
•
📝
انیمیشن متن برای ساخت محتوای حرفه‌ای
•
🎧
افکت‌های صوتی کاربردی
•
🎨
تصحیح رنگ و بهبود تصویر
•
📦
خروجی با کیفیت 4K
•
🌐
اجرا در Chrome و Edge بدون نصب نرم‌افزار سنگین
🔗
لینک:
https://github.com/Augani/openreel-video
#VideoEditing
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=vhDR2xLiIAyQeZvmKRzPa7UDK2CKWj8Aib_NhXnN0o3qVE4EocXfGYGVvM4TXZ0mvGpP6Xgw4ojJQq74-RMKrtfEsAnX-qybzgBWINtKgIpPGvlHZiqPUY3Ijx7Sfh4L_1fgSSb3LHypXwVlFIrEhIMMjL2Z2OZzdSevDFwUlE75DySu84Aw83EsMlMBafgKO3JRHvcLaIKnDcnx3T2lhuDWJQVqotteIbkT8EqqCM6YdC9fntvkRJhY3hy_4HFfR9Q8Jc1M0dmy7OL01UyhuATftHx5q8nW7NjJD8seepm-Uy1r_5RocXB2s5hSWgdMrQ5uwrLRBH3fZV2QXRLOD6MJEipYUm-a3LmKponQtMz8sNVoyKMZ0rXa_mP00dT_tyXWrpnBgQUiWgg6u6ablNS1mmXRQ2miZqpcHRTmMiAU1FPpVocNovXcKx5W9Sk4wP_R_QbiA9oCuixf-l0bs-eEYjFETC66Z7wBCRy_4wT5HYlLYVWo_fc-r3Wd1c0GsRCqucNua_q3OgA_BSH_Y9Omcm3DZI2z7TZKh4NLtzfmjtjWvZHp05Bm93puix5UrT6vg9WoDWA6Jwsw8oTLKtG59WdeSdvyDv50n26rS_-J9UJG0drexGJ3EY3koJzSpzq_spKxAKQBG2_22CKxwgeC8pM5gzorwQytPlkJYAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=vhDR2xLiIAyQeZvmKRzPa7UDK2CKWj8Aib_NhXnN0o3qVE4EocXfGYGVvM4TXZ0mvGpP6Xgw4ojJQq74-RMKrtfEsAnX-qybzgBWINtKgIpPGvlHZiqPUY3Ijx7Sfh4L_1fgSSb3LHypXwVlFIrEhIMMjL2Z2OZzdSevDFwUlE75DySu84Aw83EsMlMBafgKO3JRHvcLaIKnDcnx3T2lhuDWJQVqotteIbkT8EqqCM6YdC9fntvkRJhY3hy_4HFfR9Q8Jc1M0dmy7OL01UyhuATftHx5q8nW7NjJD8seepm-Uy1r_5RocXB2s5hSWgdMrQ5uwrLRBH3fZV2QXRLOD6MJEipYUm-a3LmKponQtMz8sNVoyKMZ0rXa_mP00dT_tyXWrpnBgQUiWgg6u6ablNS1mmXRQ2miZqpcHRTmMiAU1FPpVocNovXcKx5W9Sk4wP_R_QbiA9oCuixf-l0bs-eEYjFETC66Z7wBCRy_4wT5HYlLYVWo_fc-r3Wd1c0GsRCqucNua_q3OgA_BSH_Y9Omcm3DZI2z7TZKh4NLtzfmjtjWvZHp05Bm93puix5UrT6vg9WoDWA6Jwsw8oTLKtG59WdeSdvyDv50n26rS_-J9UJG0drexGJ3EY3koJzSpzq_spKxAKQBG2_22CKxwgeC8pM5gzorwQytPlkJYAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
نسخه ۳.۲ مدل Ray از Luma منتشر شد؛ اما طبق تست‌های اولیه، هنوز با رقبایی مثل Seedance فاصله قابل‌توجهی دارد.
✨
نکات مهم:
•
🔹
پشتیبانی احتمالی از خروجی HDR با فرمت EXR 16-bit
•
⚡
تولید ویدیو تا ۱۰ ثانیه
•
🛠️
ساخت ویدیو بدون صدا
•
📦
ضعف در بافت‌ها، انسجام تصویر، دینامیک حرکت و درک پرامپت
🔗
لینک:
https://lumalabs.ai/ray3-2
#AI
#VideoGeneration
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXtKQhnxRD8XVMu8l_voWIe9zwAxDyqzTHNyzWwxCHhLVmFycZ6q5lmh5odFKSTih30pwaVMLbr62JEXxtkHGNzCid0X9YtTlz4w36rBUJ2CamEK86KMVZvzJhO4WcX6JFPfMwD-BAF4PmBL0ZUoH0ngTVDmTSjjuLWkxgOaurgpkttjBpXY-Y6YiUrtdICVKjoz-fAV3IJsQ2DHdbzsA0AIGR9h4CXgNfbzYKLULQGf9-jdiA7zuGkmQ_7capR8E0siKhXoIwRo99aqrX_l8KNtj2j5XqiUzokSz0dOo90_T7wpl-cM_XI1AIVUFT1Cuume8_OL79LfAsxd3-lPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fe_NSekPuvCnKRvPobmJHiVYCpgSpwKp066x4B5DYcVUSlz-FnnY80TqsHLUVN-Rc2OgzThTzsmIWHGqFPzxQx4ThX7TRuuWVBBxZslj9FVTGSZkwURDooxugspy5WWoPuieodw1lqpXimTeZ7R4z7mr4K0AAtN94rR6RWsNbuF7RbIQ6N49A5Q__vDbN77y1rX8y7r_bIcGjIUrVl8Qxc8XlSZfLMEsEdcdPKHwOpsUJPZHYjwxslxWLd9JEj1LpvRWLQJqktzknPekpUTXRCvF5Dx38sGLuE2C7P-oXezNd46LVBDlzlzx7NgauuT_cC94V7vDJ2nm2H5FGVnfZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
CodeWhale
یک عامل ترمینال رایگان و متن‌باز برای کدنویسی با DeepSeek و مدل‌های محلی است.
✨
قابلیت‌ها:
•
🔹
خواندن و ویرایش فایل‌ها داخل ترمینال
•
⚡
اجرای دستورها و کار مستقیم با Git
•
🧠
حفظ زمینه بین جلسات کاری
•
🛠️
پشتیبانی از MCP، مهارت‌ها و ابزارهای اضافه
•
📦
اجرا با DeepSeek، OpenRouter یا Ollama
نصب سریع:
npm install -g codewhale
🔗
لینک:
https://github.com/Hmbown/CodeWhale
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آپدیت جدید
ربات وگا
انجام شد
✨
- اضافه شدن GPT-5.4
🚀
- اضافه شدن Gemini 2.5
⚡️
- اضافه شدن Flux 2 Kelvin
🌡️
- جایگزینی Lucid Origin با Flux 2 در گروه ها
🔄
- حل مشکل هنگ کردن Gemini 3
✅
- رفع سایر مشکلات
🔧
>
آموزش گرفتن API رایگان GPT-5.5
<
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">💵
گوگل اشتراک AI Plus را ارزان‌تر کرد؛ حالا فقط ۴.۹۹ دلار در ماه با ۴۰۰ گیگابایت فضای ابری.
✨
قابلیت‌ها:
•
🔹
دسترسی پیشرفته به Gemini 3.1 Pro
•
🧠
Deep Research برای موضوعات حجیم
•
📒
NotebookLM برای تحلیل و ساخت پادکست
•
🎬
تولید ویدئو با Gemini و Flow
•
☁️
۴۰۰ گیگابایت برای Gmail، Drive و Photos
🔗
لینک:
https://gemini.google.com/app
#AI
#Google
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📱
اگه حافظه آیفونت زود پر میشه، iMole می‌تونه حسابی به کارت بیاد.
🔍
این ابزار فضای ذخیره‌سازی آیفون رو بررسی می‌کنه و دقیقاً نشون میده کدوم برنامه‌ها و فایل‌ها بیشترین فضا رو اشغال کرده‌اند.
☁️
از بکاپ‌گیری افزایشی هم پشتیبانی می‌کنه و می‌تونه داده‌ها رو با بیش از ۷۰ سرویس ابری مختلف همگام‌سازی کنه. بعد از اطمینان از سلامت بکاپ، فایل‌های اضافی رو هم پاک می‌کنه.
💻
روی ویندوز، لینوکس و مک اجرا میشه و خروجی JSON هم داره که برای ابزارهای هوش مصنوعی و اتوماسیون کاربردیه.
🛠️
پروژه کاملاً متن‌باز و مناسب کاربرهای حرفه‌ای و علاقه‌مندان به CLI است.
https://github.com/chenhg5/imole
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAJY8kNC40ZsOOMfUv2HdB8cRKhqFv7XQbftmoxdksLCsxb1XQHO6sTPngjF0G1Jfwy90fUrCdgFk1rh0bkJEfj9Oz0ScQdXGkkkj9UwS4pteinE7aSh1QBCuPc2Vfh_jbJAN-bkPnx3-p3yz_ZgAaCZSqhXZ5GSAsv65rop4xXDeIRQ-69b7dZikk_Zl5vTs1E-DAFs2_oH0U9u5dpRWwBSKuieER5mociQ6zyXJpCPwFInTW2elVG_adRUcZ431nS4ouk4tJZkO6JrJthoMUOqk89s1eI2HCoQrJzXOFAPkENyftQXUxY9AaA-9YIFtQUFZcRpABSQg-I2_V4DYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUg4bXY9_aSUDNCUovMlqSukOvq37v8yEpbEdpRTGzuJp9Gi0ypg9WplmhEJc9XcLXVlNYgSxQdZZq1n71QwSrI1UWjh4JZ4niG-p3LVjMSsE9HqZRV44rlrXJ1KSl0HYLnwwhLU9NB8i3dIyBTi352bWU80G6QSyyPAbqucixNBx9ridWFIUQJa8woEzIs2GaSco35OY_RlKjChYmVigTazmPwkHVxbbupXcm-kD0PER_FrC2zny-kK7HydmWamSV76oqXGShB3AETbzbeS3bHzV6kIfl5bexIdSt9JLIDrKfZ5r6JzW4IudXgipvXYDIR-FRkmFo5dOCyrRj76AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با «تحقیقات عمیق محلی» می‌توانید پژوهش‌های محرمانه را روی سیستم خودتان انجام دهید؛ رایگان و متن‌باز.
✨
قابلیت‌ها:
•
🔹
جستجوی خودکار در وب و منابع علمی
•
⚡
پشتیبانی از arXiv و PubMed
•
🛠️
کار با مدل‌های زبانی مثل Ollama و GPT
•
📄
بررسی اسناد شخصی و محلی شما
•
📚
تولید گزارش نهایی همراه با ارجاعات
🔗
لینک:
https://github.com/LearningCircuit/local-deep-research
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6250" target="_blank">📅 10:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T31Oer-inXkkWVNy42nXduwAYzAtgPBP_XZOkOnZNMpWtUdb9cGp3Q-L9pwUa0X6cPmzY8vqsAVs6PyMYXkNRxx7YTkEH9hH2d5N2qfAAXu0GKRn1AYGYiu5YoC3eCfgdIuWy31jigbDpq2VOrpIdKN_csx6IdImotuByQ9b8SALKKm7LVzceWDfh-CFw_bbxRfEEJQQPVyH5C8cEi29WOpBTUJmO6p5myvyiLhjfj3xTw7vslXHO8y1nuaBI8Jf-RG0i1XEH-Y9d2nSUDBweiGh-RkTrnMkpwh5sjG8wrjSwIjRFW7Xnz2zFDpis_7VvLx8IsPFX1hUgfWLqb4RFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید
اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت Split Tunnel برای انتخاب برنامه‌هایی که از VPN استفاده می‌کنن
🔹
پشتیبانی از پروفایل‌ها و سابسکریپشن‌ها
🔹
متن‌باز و رایگان
جذاب‌ترین بخشش اینه که از روش‌های پیشرفته عبور از فیلترینگ مثل Hysteria2، AmneziaWG و حتی olcRTC پشتیبانی می‌کنه؛ روشی که ترافیک رو شبیه تماس ویدیویی نشون می‌ده. همچنین توسعه‌دهنده‌ها اعلام کرده‌اند نسخه ویندوز و لینوکس هم در راهه.
⭐
برای کسایی که دنبال جایگزینی متفاوت برای v2rayNG، Exclave یا Hiddify هستن، ارزش یه تست رو داره.
🐱
GitHub:
https://github.com/yanisplugg/olcvpn-client
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6249" target="_blank">📅 10:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=DjWZhBBzDuUpE1MwqGmqJq5MbQK34xfcAvUpdZ8QvpSMeJi_Sfh6OkG_2hQTeuO1pSaCXlUwwtWx4_4WvuKg1ndn5c_rwAWeXr6PLXLoPn0WKh5ZngpnCzoeByExmsaDMhB3KC1AS89GUkW5zcAlRyEaDxXcPIf1ze01O6yr8PIe9nR7FTlIKSjpOQKXzAo8uw-EtuDyPrtQ_w6gI1Z4rcNQ-VsQIWLoWkqiXhvxWNRZn6cZR9WClrv9iXea5cYOq_CWTHaVJyeVdD-PxB2F15IbFeHL7PnVJ0j4KSmcelvVeM0FoPgEkt4q-7B4howubCbYbofKrq5iNXSqS_fOQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=DjWZhBBzDuUpE1MwqGmqJq5MbQK34xfcAvUpdZ8QvpSMeJi_Sfh6OkG_2hQTeuO1pSaCXlUwwtWx4_4WvuKg1ndn5c_rwAWeXr6PLXLoPn0WKh5ZngpnCzoeByExmsaDMhB3KC1AS89GUkW5zcAlRyEaDxXcPIf1ze01O6yr8PIe9nR7FTlIKSjpOQKXzAo8uw-EtuDyPrtQ_w6gI1Z4rcNQ-VsQIWLoWkqiXhvxWNRZn6cZR9WClrv9iXea5cYOq_CWTHaVJyeVdD-PxB2F15IbFeHL7PnVJ0j4KSmcelvVeM0FoPgEkt4q-7B4howubCbYbofKrq5iNXSqS_fOQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrNNp34CAse-tuSi1VNguUmPaeoksI3_7g0sDeA81dCWVuM-5Bo9ThVD4qJXp2z5YamrTzjqySEDdG7gJYe5tWIningqr9ubYPR5FaFnDrtjYZzA1oOA-ux2riuY1JWiII1rk_g0zZejbE0nyHD1N8I5xKGBiQEIGRaXxitB9vGoyFdYCKjPn-aJj9umh10EqYX8qw6FmzY2U96-jeeDmRAMfw_eXqbe4e3jPoB7mBlUMnD0rGeMV_3_q9jcus8kCBHCS7n7gRNZTiJWLV9zVOg1q8Trla5VtmGJZaDakrDbxQxaq4ibUaxAn9IAu6X6_0Oo5n0_7seaapMBB-KHuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک فهرست بزرگ از ابزارهای رایگان هوش مصنوعی برای تست، توسعه و اجرای مدل‌ها
🤖
✨
قابلیت‌ها:
•
🔹
مدل‌های متن‌باز؛ از مدل‌های سبک خانگی تا گزینه‌های قدرتمند
•
⚡
ارائه APIهای رایگان برای توسعه و آزمایش
•
🛠️
اجرای محلی مدل‌ها با تمرکز روی حریم خصوصی
•
💻
دستیارهای کدنویسی رایگان جایگزین Cursor و GitHub Copilot
•
📦
فریم‌ورک‌ها و دیتابیس‌های کاربردی برای ساخت سیستم‌های چندعامله
🔗
لینک:
https://github.com/12britz/awesome-free-models
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">💻
NekoBox 5.11.18 برای ویندوز، لینوکس و مک منتشر شد
🔹
یک کلاینت متن‌باز و قدرتمند مبتنی بر Sing-box برای اتصال به انواع پروتکل‌های ضد فیلترینگ.
🔹
پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria، TUIC، WireGuard، SSH، Tor و...
⚡️
🔹
دارای حالت TUN برای هدایت کل ترافیک سیستم.
🔹
سبک، سریع، رایگان و بدون تبلیغات.
🔹
گزینه‌ای مناسب برای کاربران Clash Verge، Hiddify Desktop و v2rayN.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV4Ehd4zJKrQzZgwRFN8PHwyv4GXQlXtdS5nfvaUcHATE9csaDvTF_E0BHWW4aGDC1DTRDnWYBuZdbiCANmZWyZ3FiuwYcB47A7voerMSCXlJgTs9cAipn94Jy0VPs2nR1Ijlxe_FoYOA8nUbHYQMxRyLV15-xKfmeOy_vykBA8bGg-X0zKGfWMI13WlOd-30a2dw5JE8poExK5tmVAvoABHTz6_MRDFD1uv1mNjT2gowymHl8lltWh-uilt3bYbkUZY3xc-eS_Knh0rma1533PyBUC08Hyn4A7C9ZvlHplqVtf5JSRdIlrpkVt157MbYDQmXIVE5eOi_uKXf7SS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
😱
💻
اگه با 3X-UI کار می‌کنید، یه پروژه جالب به اسم X-UI-PRO منتشر شده که کلی از تنظیمات REALITY و WebSocket رو خودش انجام میده و دردسر راه‌اندازی رو کمتر می‌کنه.
🚀
🔐
این نسخه Nginx رو هم کنار 3X-UI میاره، SSL رو خودکار تمدید می‌کنه، روی پورت 443 کار می‌کنه و حتی برای مخفی‌تر شدن ترافیک از بیش از ۱۵۰ قالب فیک استفاده می‌کنه.
👀
⚡
از Sing-box، Clash Meta و Cloudflare هم پشتیبانی می‌کنه و برای Ubuntu 24 و Debian 12 آماده شده.
🛠️
اگه دنبال یه پنل کم‌دردسرتر برای REALITY هستید، بد نیست یه نگاه بهش بندازید.
https://github.com/mozaroc/x-ui-pro
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hala Hey _ Live In Concert</div>
  <div class="tg-doc-extra">Armin Zareei _2AFM_</div>
</div>
<a href="https://t.me/archivetell/6243" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">امشب رو با این معما بخوابین
شرکت در کنسرت این شخص، از نظر اخلاقی، غیراخلاقی هست؟
#Moral_Dillema</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6243" target="_blank">📅 02:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLx4lwo6LFRAkqQHyIw9uL_-keWaAdkB69eb08fiichAMQURVJWP_TvmRx_KGEWFkqJTBZPpIDeiQLbbdPMabDpFVeDmZ99qY2Pzp0AY7qMY3C3k42vBayCk1fY01ILBOXgjo_xD1dAzXp4-MTDswutplhWmimU6yS9qM7mGAJwYrLMuIsEugp20O9V2H3G88aoUbb95qyJIYCTHddFEYpYlXO-VXntLuiwlhMrF6ye1VQUKv2Ug8z5TMq_-mYZZGGzqMeqC2vsE9T-YPBYE0DTWIzouEFR1g4aiLU0a4V1hHp3vNsCvPk4GgVi9Fbq3nfdqHC3PFIWBv3TCPKO94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Gemma 4 بدون سانسور منتشر شد!
🔹
یه نسخه دستکاری‌شده از Gemma 4 اومده که تقریباً هیچ درخواستی رو رد نمی‌کنه.
🔹
روی سیستم‌های معمولی و حتی آیفون هم اجرا میشه.
📱
💻
🔹
حجمش کمه و با Ollama و LM Studio هم سازگاره.
🔹
جالب اینجاست که با وجود حذف محدودیت‌ها، کیفیت مدل تقریباً مثل نسخه اصلی مونده.
⚠️
طبیعتاً دیگه خبری از فیلترها و محدودیت‌های امنیتی نسخه اصلی نیست.
👀
🫠
..
#Gemma
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6241" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
بی رفرال
🤐
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 140 / 140
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6240" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6238" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app
بخونید نظرتونو بگید
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6237" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">StormDNS
a.cyntarix.com
25ffbc77bcfb23b2d4ee225eedcd2466
داشته باشید اگه نت قطع شد</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6236" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این پروژه پایتونی جالب هم برای تشخیص اشیاء توی ناحیه مشخص شده کاربرد داره مثلا طبق مثال خودش که با QWEN ادغامش کرده یه نفر با هودی اومده توی ناحیه مشخص شده تشخیصش داده و به گوشیش نوتیف فرستاده و گفته چه چیزی با چه اطلاعاتی اومده توی ناحیه.
برای دوربین مداربسته خوبه یه ناحیه رو مشخص میکنی هر چیزی اومد توش بهتون خبر میده،کد اصلیش با پایتون نوشته شده و از ابزارهایی مث ffmpeg برای مدیریت استریم‌های ویدیویی استفاده می‌‌کنه.
github.com/roryclear/clearcam
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6233" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6232" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هر کی 99 تا رفرال داشته باشه ی کانفیگ نپستر میدیم بش
😌
🔥</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6231" target="_blank">📅 00:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6230" target="_blank">📅 00:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6229" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFWnfmcijyau-NOXzRIjIQZEmx_Pmbk0CipsjgdiRQRTeN6gP33sQ8rm5JX86iJIQsvULkxpYDfKWnOIvMGLwxur_2pXJbdj-r4339_1271T8ZVmNao0PHn-ZMC8sAvIEzSYQwhaTefbsc1zaikQAv6TnySBw8nn8SFgQ63FEbripXO7aMQNXJ222qf4eKI2dR-UIFIAlnZP0T5N_GplJRkG6Rj2H9YlgduGUhysMHR0l5005xOG91BaQQfjBMuFgX2h6aGeck44pacuZlxbqw4LeU-HqzLvR2JbJ9GIINutM4uEsTalJY4PnhzKam43J3nkLNenaTHZuOlwNTzwXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Gitdot؛ رقیب متن‌باز GitHub که با Rust ساخته شده
🔹
پروژه Gitdot توجه زیادی جلب کرده و به‌عنوان یک جایگزین مدرن برای GitHub معرفی شده است.
🔹
این پلتفرم از ساخت مخزن، Push/Pull، ریپوهای خصوصی و عمومی و مهاجرت از GitHub پشتیبانی می‌کند.
🔹
رابط کاربری آن با الهام از ابزارهای CLI مانند Vim و fzf طراحی شده و روی سرعت و ناوبری با کیبورد تمرکز دارد.
⚡️
🔹
قابلیت‌هایی مانند Pull Request، Issues و CI هنوز در دست توسعه هستند.
⚠️
با وجود استقبال کاربران، Gitdot هنوز در مراحل اولیه توسعه قرار دارد و فاصله زیادی تا رقابت کامل با GitHub دارد.
🔵
@ArchiveTell
| Bachelor
⚡️
https://gitdot.io/</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6227" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🛑
پایان uBlock Origin در Chrome نزدیک است
🔹
گوگل آخرین راه‌های دور زدن محدودیت‌های uBlock Origin را مسدود کرد.
🔹
پشتیبانی از افزونه‌های Manifest V2 به‌طور کامل در حال حذف شدن است.
🔹
فلگ kExtensionManifestV2Disabled نیز از Chromium حذف شده است.
🔹
مرورگر‌ های Edge، Opera و سایر مرورگرهای مبتنی بر Chromium هم این مسیر را دنبال خواهند کرد.
⚠️
نتیجه: نسخه اصلی uBlock Origin به‌تدریج از دسترس کاربران خارج می‌شود و کاربران باید به uBlock Origin Lite مهاجرت کنند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6226" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=QQzU4PUNBU5MAgbfIJ5cWpqNfRQl7czf6AgOaPAjSGU73kqUjRW0mmsNK5TsUyN_l6xpzSd9g9_4up2gNzafJpj6PLlzFQG09usrCrPx5DNeENoIEBlMyQNTzGo0-r_P1LVa34HOfk6hgvwXoUgqEFuNST0fphaXaidodPy94AMOT3cwORbC57yKEstbFyVEQ9spCBuM90_zo1Xvs6FrEOo7PC6TOzRMhzVhFhcs1volEAtRoalQwULx9SeZphL9z99JE1bAYrn3XHOv68GIfDxWuDL-MV6c3Ftr6ktFzk7JOlv2EG9WWZWvxM7vs1l-rCAi_yZ4xU_ZO7VDP4x8dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=QQzU4PUNBU5MAgbfIJ5cWpqNfRQl7czf6AgOaPAjSGU73kqUjRW0mmsNK5TsUyN_l6xpzSd9g9_4up2gNzafJpj6PLlzFQG09usrCrPx5DNeENoIEBlMyQNTzGo0-r_P1LVa34HOfk6hgvwXoUgqEFuNST0fphaXaidodPy94AMOT3cwORbC57yKEstbFyVEQ9spCBuM90_zo1Xvs6FrEOo7PC6TOzRMhzVhFhcs1volEAtRoalQwULx9SeZphL9z99JE1bAYrn3XHOv68GIfDxWuDL-MV6c3Ftr6ktFzk7JOlv2EG9WWZWvxM7vs1l-rCAi_yZ4xU_ZO7VDP4x8dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6225" target="_blank">📅 22:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRvPBIefOtFJ-DpbT5dRvligTb_K_rsMp7TUzs5rydonUnOe2r45chpG5ltChj_6-a8UyiysObXtOUaE70P7BSYDUdyDjVk0aT5En66oFT3Y6prMWVV9YPmwN_c_EpCg35PhNv0E56vI2w5-h_pkw-GKOm3acuFmPLf00vFxlEX0xW6v0Rh6I5STFpBPqqVbgQq5vm3VwdLRBqI5VuccKgQkaechRVr4hGAgiUcFPiRZzUzt-RiCrTpM4ylP9SrcoA2El1S-0EN_TpEsjg-epak799wgrWTgRYKce2X0gqGQSctu8B9Us4_tUXJqhKyAgDN5bRzc073smcMKlIQGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک ویرایشگر ویدیوی کامل که مستقیم داخل مرورگر اجرا می‌شود؛ بدون نیاز به Premiere Pro یا CapCut
🎥
✨
قابلیت‌ها:
•
🔹
پشتیبانی از چندین ترک ویدیو و صدا
•
⚡
رندر سریع با شتاب سخت‌افزاری GPU
•
🛠️
افکت‌ها، ترنزیشن‌ها و ابزارهای تدوین
•
📱
قابل استفاده روی کامپیوتر، تبلت و گوشی
•
🎬
عملکرد پایدار حتی در مرورگر معمولی
🔗
لینک:
https://tooscut.app/
#VideoEditing
#Tools
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6224" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">طبق درخواست شما عزیزان
تمامی سرویس هایی که API رایگان هوش مصنوعی در اختیارتون میزارن رو مجدد قرار میدیم
✨
Freemodel.dev
🥇
developers.cloudflare.com
🥈
console.groq.com
🥉
aistudio.google.com
build.nvidia.com
cloud.cerebras.ai
openrouter.ai
console.mistral.ai
llm7.io</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6223" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXzODVULcSPTZ641851q7hEbMeJIUoP9p7bM8PKqkUNMCR7lxVYGdcq9rb1A8zUJkmloLXRoDa9fPoAjlBTauBg5KRb8LwIeiVZleW7Jev2O5H63gOmm8TAtQH5fIYpKSj4lo4LtjNxa0sWGGY5rkJwFzEmcI4gfWcHGeFS3z4CgXXNVC9z7hBI7ZYs59lSoQtZnZRUxeHpfKj9eVT9HlqknfTUbu1OIHmVfpzliBV1uGb6A2hOoXn4A3XFH99KigV4d70bPhxImPOX_C95s0uF3kI1mESW_H6mR8d--ZIRozUhK7BwnEQMrW1NwN9AVWV76UUhq9JaWO2SPlFSx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
کاهش بار اضافی روی حافظه در ویندوز ۱۱ — غیرفعال کردن فعالیت پس‌زمینه Edge
😎
این کار از طریق ویرایشگر رجیستری انجام می‌شود:
1️⃣
کلیدهای Win + R را فشار دهید → regedit. را وارد کنید.
2️⃣
به مسیر زیر بروید:
HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Edge
3️⃣
روی فضای خالی کلیک راست کنید → «ایجاد» → پارامتر DWORD → نام آن را «StartupBoostEnabled» بگذارید و مقدار آن را 0 انتخاب کنید.
4️⃣
کامپیوتر را ریستارت کنید.
پس از این کار، Edge دیگر در پس‌زمینه اجرا نمی‌شود و منابع را مصرف نمی‌کند.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6222" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">walf.zip</div>
  <div class="tg-doc-extra">12.9 MB</div>
</div>
<a href="https://t.me/archivetell/6221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ℹ️
فایل سرچ پروتکل و سرور ویندسکرایب
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6221" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚀
برنامه WALF منتشر شد!
اسکنر خودکار سرورهای ویندسکرایب نسخه PC
اگر از عوض کردن دستی سرورها خسته شدی یا دنبال یه راه سریع برای دور زدن فیلترینگ میگردی، این برنامه دقیقا همون چیزیه که نیاز داری.
کار برنامه چیه؟
برنامه WALF کاملا خودکار و بدون اینکه نیاز باشه کاری کنی، تک تک سرورها، شهرها و لوکیشن های ویندسکرایب رو روی پروتکل ها و پورت های مختلف تست میکنه تا بهترین و سریع ترین اتصال رو برات پیدا کنه.
👇
چطور کار میکنه؟ خیلی ساده:
۱. فایل برنامه رو از لینک زیر دانلود کن و از حالت فشرده درش بیار.
۲. فایل walf.exe رو اجرا کن و دکمه Start رو بزن.
۳. تمام! خود برنامه اگر ویندسکرایب بسته باشه بازش میکنه و شروع میکنه به اسکن کردن کل شبکه تا بهترین اتصال رو برات ردیف کنه. (فقط مطمئن باش که قبلا توی ویندسکرایب اکانتت لاگین شده باشه).
لینک دانلود برنامه سرچ خودکار پروتکل پورت و سرور های ویندسکرایب در پست بعدی
⬇️
با تشکر از چنل
@CubicDreams
که زحمت کشیدن ساختن
🙌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6220" target="_blank">📅 19:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خب یه پست اختصاصی دیگه داریم این فایل رو خیلی جاها میلیونی میفروختن در حالی که رایگان بودش یکم دیگه پابلیک میکنم
🔥</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6219" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcOU3Rd5izW1vaq9cFwYeV-I4RJNNMwNxONM1hNkHDKoKelnkcttKLsbQQLuZYUI_uTNzw_cqvrtDKVjuZWiw_D2zOR6IShhkbzX90u2SWk5uZGwplH5w-7ZWOww1Ztig-rhQydApElTvTLTLzUZaPbmDQZh4Bm9xMEBU8fLeM-CFDMAeZ1s63VM-Roj6Hy4wRo_pQugUyRPkkBl_SCNn7fHVO6vHI-Ths9rvups0mMLxYqciHKg-iRXzLUuyVzq8nrFEYBLJhFTmOV0Fln409Tfn4KWEJ_cPM5MWZCSztHdyCszUhUDiZHPQ7Iwzllu6N0Rj5TkjCnUz6T0zzrssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel  اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت Freemodel شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6218" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚠️
اطلاع رسانی برای افرادی که اشتراک ویندسکرایب پرو خریداری کرده‌اند:
پروتکل
ikev2
روی تمام لوکیشن ها (تقریبا) متصل میشه
✅️
با تست هایی که گرفته شده با فیبرنوری مخابرات  سرعت همه سرور ها دانلود ۲۰۰ مگابیت و اپلود حدود ۵ مگ فعلا قفل هست
(پیش‌بینی میشه پهنای باند ikev2 کم کم محدودیتش برداشته بشه و به قبل شرایط ۱۸ و ۱۹ دی ماه محدودیت شبکه برگرده)
سرعت کانکت شدن به سرور ها و امنیت ، این پروتکل خیلی بهتر از tcp هست حتما استفاده کنید
👌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6216" target="_blank">📅 18:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6215" target="_blank">📅 17:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel
اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت
Freemodel
شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
بخش اول: احراز هویت با شماره تلفن
🔹
بخش دوم: احراز هویت با تلگرام
✅
گزینه احراز هویت با تلگرام را انتخاب کنید.  لینک ربات تلگرام برای شما نمایش داده می‌شود. وارد ربات شوید و استارت را بزنید
🎉
پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار  هر هفته: ۶۶ دلار اعتبار
💰
4️⃣
از منوی سایت وارد بخش API Keys
شوید و یک API Key جدید بسازید.
5️⃣
در بخش Docs می‌توانید مستندات کامل استفاده از API را مطالعه کنید.
🛠
تنظیمات نمونه:
model_provider = "freemodel" model = "gpt-5.5" model_reasoning_effort = "xhigh" disable_response_storage = true preferred_auth_method = "apikey" [model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses"
🤖
حالا API Key و مشخصات بالا را به هوش مصنوعی موردنظر خود بدهید و از آن بخواهید برایتان کد تولید کند:
✅
JavaScript
✅
HTML
✅
Python
✅
PHP
✅
Node.js
✅
و بسیاری زبان‌های دیگر...
💡
می‌توانید با آن:
🔹
ربات تلگرام بسازید
🔹
وب‌سایت طراحی کنید
🔹
ابزارهای اتوماسیون ایجاد کنید
🔹
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت خوبی برای تست GPT-5.5 بدون پرداخت هزینه است.
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6214" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6213" target="_blank">📅 17:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
hysteria2://5z15av99psrlhdqp@32.195.51.20:39150?alpn=h3%2Chttp%2F1.1%2Ch2&fm=%7B%22udp%22%3A%5B%7B%22settings%22%3A%7B%22password%22%3A%22dlxmzvxvcp3i6v0e%22%7D%2C%22type%22%3A%22salamander%22%7D%5D%7D&fp=chrome&obfs=salamander&obfs-password=dlxmzvxvcp3i6v0e&security=tls&sni=32.195.51.20#usa_hesteria-%40u2vpn-100.00GB%F0%9F%93%8A
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6212" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پروکسی‌های اختصاصی آرشیوتل
😎
⚡️
پروکسی ۱
🚀
پروکسی ۲
💥
پروکسی۳
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6211" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL5W_KAbaLPrgLR5UuME2pxbLjzViF5Y19906IwUzJm6KsikcIx1MvaINNchRkuenJEt-pc0k6iRM7qGov4cePQtn-iutaipgG6abgIXOrMduK3LJVy2wU3w2XxyK1nV56x-FfYhhDStHkKGTZ8E1EF7Lbl_0mAV3QtYZTlHOo-Tse_vsUWNzRgXgYpF1tmcZVDuCHJlrSt-bG3kWe7KL-sGUZzHNUoZ-8G2hRWUe7M0p4dDruCbfZIW0Ifa8v1mL9J-0S1lf4xjP8HzTeNpEhGjHO4YErVG98WjigTKhtfDwZpODSQuaH7abRdDCEcmcICtX5pE9akygIfJnwo7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب یه روش مخصوص ایرانی‌ها اضافه کرده، رو همه اپراتورها عالی کانکت میشه:
Settings → Connection → Anti-Censorship
گزینه Protocol Tweaks رو روی Enable بذارید، بعد وارد Configuration بشید و یکی از دو گزینه آخر که ایران هست رو انتخاب کنید. گزینه Large TLS رو هم روشن کنید.
پروتکل های udp و tcp رو تست کنید
ایرانسل tcp 587 france
مخابرات همراه اول udp 80
با فیک میل اکانت بسازید
https://windscribe.com/signup
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6210" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoJLMvVqEnRnRO4zlFWVo6WjPdz8ORHFBi6BbuxYZA_VOZLvfCZ6E64SP1HIBlyn5gtj1Ni6RVQn_L4DYjwsNEO7jKHdbBBGMDg0lPNP8yV4WQUdjKlm4VrBneLwS2DMHJjSKZ4xlxUdUg5D4cmjUOgQwipiH9hLQmSx26lHEOQe-4GG42vRO90D4LDl82j4XBAG-P2saC-PlWhqJwlMPGbM__13zus76OR88EQtsqqAIM1UxQXBX4-XBIeb4CWk-84YHBGClMDk9i8UhzcePKH4Zd_KVA8vumJRlRpLjJ17R7z_WF3L7KS2r6DGHMFaU1WS057iyDQls9Fdtanarw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
Impeccable
‏این ابزار به عامل های هوش مصنوعی کمک می‌کند تا وب‌سایت‌های منحصربفرد و بدون الگوهای استاندارد ایجاد کند
🔥
‏
✨
قابلیت‌ها:
‏•
🔹
آموزش عامل‌های هوش مصنوعی برای ایجاد طراحی‌های منحصربفرد
‏•
⚡
کار به عنوان منتقد، توسعه‌دهنده front-end و نویسنده UX
‏•
📊
آزمایش ماکت‌ها، برطرف کردن خطاها و بهبود طراحی
‏
‏
🔗
لینک:
https://github.com/pbakaus/impeccable
‏
#هوش_مصنوعی
#طراحی
#OpenSource
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6209" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrVAMvry2NWS8FEsiN48UviQ80aieRwDCYrfr-2Ie35__pZo79PSFImlFhEni7aV0TRE_mKHOiQu2v0fnuO33szKyAdZsGPZZCZY3Trgj8ZkCt7jbAjlmMwiXjD2KJwA_1dBkriceNxYpuXF52jqQg_0Tzbg5vVOJhktSD77_Lji8GPNosK3dQXxX_TbpJkn27ZAWP2CXpoPjlPYrd9wF8ulnhwaZl7u7fATpMa7htlRQJwf6Xwz_PrRfnqXHutu_5GyeBxitotKH9VOz2SK8TIBAxi2dQ7ed22GxNh9s_7IR_rxIf6kh8EUWjgi_CpfX9qUszF0TjhnGb8MkFJzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgMJnk1FdxeEKNQjdda2nbGS7Na6J3MXZ0yRQaw7MXWXIVuDpbFRk18NAUpWBjJKEtke_XlkyFCeyvTXuuzXkBSTOTolbKOxx6U9RR1D_udpLQFFEQUAxLoKumxFjSqDyyWTLfoek_Y2JBeXlGgnQhCS6ypRTTk9RvL5u4LpjHyaax_G71H0hYzHKDzalUVqfMYGMcao53VnsozMoi0FJr04digV8LzVhPIw9rKzoHwOWv_tdINclCvGXW-TKc3Lh5eibJ52THFrlZJBNPacszjS6mZjJzE8BwfEHJOxWF94oGhqK7FJvIdy4M0VKCxmt8hO0liUp4awziH7MVYOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OyQuqDN2TwltY1DTfGDOD36uHP8e3trb2mFuiqN9r06VBLayjgNhsNR20t1CpOecj4xUxTwYqkjtFihghAbLb_DyJXCUwZ_uDJ9IzSvwFr6CE0NsFTCzlWFS5sHwT1bPXOM__dEigzmSeNcZ0in7AIU3_k5H6zdRBf5nhbCrXBCuQ4yfvMJkt-Y7o96YihStgZF5ca8ZPJCQx9MO6UodHcHepP_FgwsRvpuvu5r92VrcNCDF6vMo7IBwoDOL3EYLenJh6rUUhADx52AJgPPp4s0NGfD_luQxNGnC7oCuHr-_hPbnC9J5Ttlfr0Lf04UPD60_YEYf8qKZgtgzmJ8RKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=r8lWDXIqVY61F2q86MnBIL8B0YN4qzScSaQKbZvybMzcQRuLOu6WOcfmzqr2hen5P9vD9k3qlj4OEqtxPKx5lY4AWzDQB3WSDwppcuYaIaPJV3MFurqj_7AsGHZbtEj5-wM1bfmpq6ryRyKu8kLGFktdOET_HYIgifLE5yZMb1yTP0hGJHOmvfDiXl2V7sCTr0d8qJdEX29iBWYaNDRpYSEkCzL7CXT6Mtvlptod2qvSVNAvFe7vDh46iHJeWjXMdd5QRTfsAkdieqf5N_S6jpnQ4_tF54NJO4mFxrmL7JHWa_L-6dFIw6_nTbAw9tVtCQMoU5FL_-FjmcxddWBEyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=r8lWDXIqVY61F2q86MnBIL8B0YN4qzScSaQKbZvybMzcQRuLOu6WOcfmzqr2hen5P9vD9k3qlj4OEqtxPKx5lY4AWzDQB3WSDwppcuYaIaPJV3MFurqj_7AsGHZbtEj5-wM1bfmpq6ryRyKu8kLGFktdOET_HYIgifLE5yZMb1yTP0hGJHOmvfDiXl2V7sCTr0d8qJdEX29iBWYaNDRpYSEkCzL7CXT6Mtvlptod2qvSVNAvFe7vDh46iHJeWjXMdd5QRTfsAkdieqf5N_S6jpnQ4_tF54NJO4mFxrmL7JHWa_L-6dFIw6_nTbAw9tVtCQMoU5FL_-FjmcxddWBEyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
هوش مصنوعی Siri یاد گرفته است که عکس‌ها را مانند Nano Banana Pro ویرایش کند.
✨
قابلیت‌ها:
‏•
🔹
«بازآفرینی فضایی» برای تغییر ترکیب، زاویه و پرسپکتیو عکس‌ها
‏•
📸
ویرایش پیشرفته برای ایجاد عکس‌های خلاقانه
#Apple
#Siri
#Ai
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6205" target="_blank">📅 12:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZrKct6yfCEnt7MSFmnVq3P5iD2BLRQxswCC6WRUWcnNauiRX-fBmgwYXcpUdcQBJ8_2jnyO-ZumTkkaZDo4HXF5EdHpXFOrOBOqAm2PXhIdI5FtQIXyfUO4TwxNnk5TQgd9JHQF-rZ40CA_WCbz9m-91AipB_rdbGuCRcx__YvHwDo1WQSiHoHOwm6LMh5nRbPFt7JSveULOrxkf46C52tlJUvVBgAuZObTWzq4NS3IbU64PGE2U5LRoNL0NP_p5-FVvAoRISxSW9nRo0AWncoF3j6Tx5yq2-pfRAP1ztcFwmuNLjvkpEt5UkpVny1UbY05M3IHwXlaMdYOtd7V9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
.FrameCoach معرفی شد!
‏این ابزار هوشمند تنظیمات گرافیکی ایده‌آل را برای هر سخت‌افزاری انتخاب می‌کند و حداکثر FPS را استخراج می‌کند
🎮
‏
‏
✨
قابلیت‌ها:
‏•
🔹
انتخاب کارت گرافیک و پردازنده
‏•
⚡
انتخاب بازی از کاتالوگ
‏•
🛠️
دریافت تنظیمات بهینه برای حداکثر FPS یا بهترین گرافیک
‏•
📊
مشاهده تأثیر هر پارامتر بر عملکرد
‏•
📈
تست تنظیمات و پیش‌بینی فریم بر ثانیه
‏
‏
🔗
لینک:
https://theframecoach.com/
‏
#گیمینگ
#بهینه‌سازی
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6204" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">با پلتفرم Cerebras به مدل‌های قدرتمند gpt-oss-120b و glm-4.7 با محدودیت بی‌نظیر ۱ میلیون توکن و ۲۴۰۰ درخواست در روز دسترسی پیدا کنید
🚀
شما می‌توانید کلید API خود را دریافت کرده و پروژه‌های هوش مصنوعی‌تان را با سرعت و دقتی فوق‌العاده پیاده‌سازی کنید
🛠️
. این یک موقعیت عالی برای استفاده از مدل‌های سنگین بدون پرداخت هزینه است
💸
، پس آن را از دست ندهید!
✨
cloud.cerebras.ai
🔗</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6203" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=kV-huSOwc15Q63D6Y8MhQaHUZ2IKygq0bzHvf4jbxy3NjvaHjYSmWHy_q6Jch8li-z4UVbpLOo8Hvq8T-OJ0CY1dDM3C5Ip73vK896TAuWPUz6uigoMCsxVM15WaTV0ymz7FqkXN-02Dzxs3Sqx3bE-AFcGY-xxeTlLxDZF7HDXWXFhJqpMSX9I4ljPlftmXIYonLwY4lf_ceIw6xJqmKG0yWFENwNLr6LFjcr3aVSW527SWCOrQZG-hQha43WRa3QTOufbORYOLX5D-w5LnR06d1cvm2cJuSgnBMJ7Lap5-b-G-RefErdzifcn8MR3TbgwmmeSGkmu3W9AmULT-tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=kV-huSOwc15Q63D6Y8MhQaHUZ2IKygq0bzHvf4jbxy3NjvaHjYSmWHy_q6Jch8li-z4UVbpLOo8Hvq8T-OJ0CY1dDM3C5Ip73vK896TAuWPUz6uigoMCsxVM15WaTV0ymz7FqkXN-02Dzxs3Sqx3bE-AFcGY-xxeTlLxDZF7HDXWXFhJqpMSX9I4ljPlftmXIYonLwY4lf_ceIw6xJqmKG0yWFENwNLr6LFjcr3aVSW527SWCOrQZG-hQha43WRa3QTOufbORYOLX5D-w5LnR06d1cvm2cJuSgnBMJ7Lap5-b-G-RefErdzifcn8MR3TbgwmmeSGkmu3W9AmULT-tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🤖
چینی‌ها یک هیولای هوش مصنوعی با ارتشی از عوامل عرضه کردند — Kimi Work می‌تواند تا صد دستیار را به طور همزمان روی یک دستگاه اجرا کند.
‏
‏
✨
قابلیت‌ها:
‏* تا ۳۰۰ عامل می‌توانند به طور موازی روی وظایف مختلف کار کنند
‏* مرورگر را تقریباً مانند یک انسان کنترل می‌کند
‏* دسترسی به داده‌های مالی را بدون پیچیدگی در تنظیم API فراهم می‌کند
‏* عادت‌ها، زمینه و اقدامات قبلی را به خاطر می‌سپارد
‏* با فایل‌ها و اسناد محلی کار می‌کند
‏* کد پایتون را اجرا می‌کند و فرآیندهای روتین را خودکار می‌کند
‏* کمک می‌کند برنامه‌ریزی کنید و وظایف بزرگ را تقسیم کنید
‏
🔗
https://www.kimi.com/products/kimi-work
#kimi
#ai
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6202" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">78.2 MB</div>
</div>
<a href="https://t.me/archivetell/6201" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">12.8.0 (6913)
Directly downloadable from
telegram.org/android
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6201" target="_blank">📅 11:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNgQe682CphVKq5ucMbKwpKPKjTSq_wUIHej6A9iDKO0_YWoGcZslX3yULeNTPsvJIm1696tdo5qN8CoLFbAOUY0UtW52jVCnxmJsNsp6OyjuHKeUiOnKKvr2E64LuE6NcN7tgCmnUXVO1YpNOVgQnImvWOY6HGrUQU1HbJ1vrM9bpfTjmpGap1VfQ4cGRXIyMbTe056c6T3ZX5ngl7OU2ZaZ_uFRy9xK0zqT1iupx1aw2SYbbzRt6n9c_Rii-G21DnabzMN34MF7uM3pLcOTN2C_FZpzzWNkRrhnlzBhM66G0QXN146YOnsyuAM7YgDGzEaDXCFPnqIvKqt9Xx1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
گوگل NotebookLM را با قابلیت‌های جدید هوش مصنوعی ارتقا داد.
حالا این ابزار از مدل جدید Gemini استفاده می‌کند و می‌تواند فراتر از یادداشت‌برداری عمل کند.
🚀
✨
قابلیت‌ها:
•
🤖
پردازش و تحلیل بهتر اطلاعات با Gemini
•
📊
ساخت نمودار و تحلیل داده‌ها
•
💻
اجرای کد مستقیماً داخل نوت‌بوک
•
📝
تولید اسناد و گزارش‌های مختلف
•
☁️
محیط پردازش ابری اختصاصی برای هر پروژه
🎯
ابزار NotebookLM کم‌کم از یک ابزار یادداشت‌برداری به یک دستیار تحقیق و تحلیل کامل تبدیل می‌شود.
🔗
لینک:
https://notebooklm.google.com
#Google
#Gemini
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6200" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee5737315.mp4?token=fEQU2RDH-FUAe_V2AWIHlGYqLBjY5WrmNdArCaqpwyBk8Z6-5nW8jga7tfvSuIjciW_yN9K2z0ITQqRDpOauBHc9g8HtCz1EXA4hsYjR2Q8BvkcQJowgvx9LfnOGX9k9-BGGFvRpjtKcWxl9ULXTLOENGerRn8ClYEdexv--RBj4KwvAbIGaq9cP492xlpil7mFqNmeB_2KF21GDr08Y6xtz4QfCPtnnyJw_Xi3i33C_bFzZ5iJ73cjObH4bqOfTtpy2F4DX-_-d4HOw-8UfQiRROvZjLnYWxG_mGlRKdBWQrYWHfO3scJCpkJK8CwJRyXekiSXgd4WOoi1QsJpUfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee5737315.mp4?token=fEQU2RDH-FUAe_V2AWIHlGYqLBjY5WrmNdArCaqpwyBk8Z6-5nW8jga7tfvSuIjciW_yN9K2z0ITQqRDpOauBHc9g8HtCz1EXA4hsYjR2Q8BvkcQJowgvx9LfnOGX9k9-BGGFvRpjtKcWxl9ULXTLOENGerRn8ClYEdexv--RBj4KwvAbIGaq9cP492xlpil7mFqNmeB_2KF21GDr08Y6xtz4QfCPtnnyJw_Xi3i33C_bFzZ5iJ73cjObH4bqOfTtpy2F4DX-_-d4HOw-8UfQiRROvZjLnYWxG_mGlRKdBWQrYWHfO3scJCpkJK8CwJRyXekiSXgd4WOoi1QsJpUfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔤
پیدا کردن فونت هر سایتی در چند ثانیه
ابزار
Font Stealer
یک ابزار رایگان برای طراحان است که فونت‌های استفاده‌شده در هر وب‌سایت را شناسایی می‌کند.
✨
قابلیت‌ها:
• نمایش فونت‌های به‌کاررفته در صفحه
• دانلود فونت‌ها در فرمت‌های مختلف
• پیشنهاد جایگزین‌های رایگان از Google Fonts برای فونت‌های پولی
🎨
ابزاری کاربردی برای طراحان UI/UX و توسعه‌دهندگان وب.
#Design
#Fonts
#WebDesign
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6198" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌐
اختلال VPNها در روسیه وارد مرحله جدیدی شده است.
گزارش‌ها حاکی از آن است که فیلترینگ در روسیه نیز دیگر فقط بر اساس IP نیست و اکنون الگوی ترافیک و TLS Fingerprint نیز بررسی می‌شود. همین موضوع باعث ناپایداری VPNها، MTProto و پروتکل‌هایی مانند WireGuard و VLESS شده است.
#VPN
#Telegram
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6197" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚀
پروکسی محلی برای تلگرام دسکتاپ
TG WS Proxy یک ابزار متن‌باز است که ترافیک Telegram Desktop را از طریق WebSocket عبور می‌دهد تا اتصال پایدارتر و سریع‌تری داشته باشید؛ بدون نیاز به سرور واسط اختصاصی.
✨
قابلیت‌ها:
• اجرای MTProto Proxy به‌صورت محلی روی سیستم
• انتقال ترافیک از طریق WebSocket و TLS
• پشتیبانی از Windows، Linux و macOS
• رابط گرافیکی ساده برای مدیریت تنظیمات
• متن‌باز و رایگان
📥
دانلود و مشاهده سورس:
https://github.com/Flowseal/tg-ws-proxy
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6196" target="_blank">📅 03:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قابلیت جستجو در وب در ربات هوش مصنوعی وگا اضافه شد.
🔍
همین حالا بیاید و اون رو در پیویتون و گروهاتون تجربه  کنید.
😉
@T_Vegabot</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6190" target="_blank">📅 01:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">موتور جستجوی ربات
Vega
چگونه کار می‌کند؟
🤔
بخش جستجو در وب در Vega از مدل gpt-oss-120b پشتیبانی می‌کند که API آن توسط Groq ارائه شده است.
🌐
همچنین در این سایت انواع مدل‌ها وجود دارند که سرویس‌های جستجوی وب مختلفی را ارائه می‌دهند.
🛠
سایت برای دریافت کلید و تست انواع مدل‌ها
✨
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6188" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=sbYFmouxkP9agCKUPNTxL1ZoDxV-lAcmE0lXmIQctkI9DX8XSBM364Veg11kxFETzNYDACuf0VtOJXVcD_rGrYda9ov7qgY9FXu0_qgj54RdCbpYV2-_ZRlPEhr5P6MpesXyzEFDcfXCq7WJJpGJp85EGdorUUJbYeyBuZUYsFPeS5fqIJgbef6uUP27whGRx2wC1WpNpqZc80vYeV7qM8zQVp0BEeyUDGHE0efSmOozwuq9SycyN_cgbEszYXkV6CWL1a0P6E0PJDJI-54rP9LfzVP4P801CSmy4lR2ssGAjAZP_p6nwkT6ivx9Ulaf9iQD4ngz5W8NFWg0WfMc5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=sbYFmouxkP9agCKUPNTxL1ZoDxV-lAcmE0lXmIQctkI9DX8XSBM364Veg11kxFETzNYDACuf0VtOJXVcD_rGrYda9ov7qgY9FXu0_qgj54RdCbpYV2-_ZRlPEhr5P6MpesXyzEFDcfXCq7WJJpGJp85EGdorUUJbYeyBuZUYsFPeS5fqIJgbef6uUP27whGRx2wC1WpNpqZc80vYeV7qM8zQVp0BEeyUDGHE0efSmOozwuq9SycyN_cgbEszYXkV6CWL1a0P6E0PJDJI-54rP9LfzVP4P801CSmy4lR2ssGAjAZP_p6nwkT6ivx9Ulaf9iQD4ngz5W8NFWg0WfMc5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍎
Siri AI: تحولی در WWDC 2026!
در آخرین حضور تیم کوک، سیری با قدرت گرفتن از Google Gemini به یک چت‌بات هوشمند با اپلیکیشن مستقل و دسترسی کامل به اکوسیستم اپل تبدیل شد.
🤖
این دستیار حالا با دسترسی عمیق به ایمیل‌ها، عکس‌ها و تقویم، می‌تواند کارهای پیچیده و چندمرحله‌ای را به‌صورت کاملاً بومی مدیریت کند.
✨
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6187" target="_blank">📅 21:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=QtUbAsbObfMgz6m7SWSDA1-WaLnDfuo8k4WKH7Ibbug-ip5MhMT4V2d3lvHgKJFrpouBi8Ldlj5Yw-zA_4zxcZDUbRxSmgvpBtB5jX716qCu7GLJldtjRHOxjJypg3-AWMnYbURTQB04XrBlSgETE6x4vEFywZYuUOK6fnQ4WDk9sTS7_bW_zKXK9B9Rv1oLRbOqPRNMgXM3PimxKzr-4G-kmcQSmcAGTdX-e5yN5pZKkyWbqY3j-cWLNu1NgOsSCzu-v6kREeoKDhgJcAhMhv2Z3R4FplBF1Xs-r2JYBSjnYp3Nm3kd3k6_J5B7mkYG9XpvaWqy25ObSdC6_WAj6w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=QtUbAsbObfMgz6m7SWSDA1-WaLnDfuo8k4WKH7Ibbug-ip5MhMT4V2d3lvHgKJFrpouBi8Ldlj5Yw-zA_4zxcZDUbRxSmgvpBtB5jX716qCu7GLJldtjRHOxjJypg3-AWMnYbURTQB04XrBlSgETE6x4vEFywZYuUOK6fnQ4WDk9sTS7_bW_zKXK9B9Rv1oLRbOqPRNMgXM3PimxKzr-4G-kmcQSmcAGTdX-e5yN5pZKkyWbqY3j-cWLNu1NgOsSCzu-v6kREeoKDhgJcAhMhv2Z3R4FplBF1Xs-r2JYBSjnYp3Nm3kd3k6_J5B7mkYG9XpvaWqy25ObSdC6_WAj6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Apple
#WWDC26
has started
Watch live:
https://www.youtube.com/watch?v=hF8swzNR1-o
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6186" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otnNHsAvhYxD4OHnjDZfqqYPMpdOGevw---2x6fFsKHfx_ZWSlEipVmNAyrvZeybdFTx5ylFcTuOoqqU5PkA1N_CdpiKxYSEZ1SB_ahnkWTNct_0NDjTU3znx8uRaHnVEjaWjxnAnA2hbsDO803s1vxEzHewLM-SRQRU6z4-K2FYVZx5BP5Q53clH6lffibPhLTRoXWZlyXWEjdX9PNekU62E8hEHQ4XZfGQzQ_oRuMho4Te7Q93_NEH6bDRSanDCC4JgJgdo1nymzI-B8HRIIFR7sJvkRpJZQL-fpHnE30OPWEtFug0zZhq3vzFiSZCX1cdNFsatWjK4QLJQBTGvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت ارائه APIهای هوش مصنوعی رایگان
🔥
از مدل‌های چندوجهی شامل متن، تصویر و ویدیو پشتیبانی می‌کند و یک راه‌حل توکن مقرون‌به‌صرفه برای توسعه‌دهندگان ارائه می‌دهد.
🔗
https://agnes-ai.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6185" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🤖
Kimi Work
دستیار هوش مصنوعی که کارها را خودش انجام می‌دهد
نسخه دسکتاپ Kimi Work منتشر شد؛ یک AI Agent محلی که می‌تواند بخشی از کارهای روزمره را به‌صورت خودکار انجام دهد.
✨
قابلیت‌ها:
• اجرای همزمان تا ۳۰۰ ایجنت هوش مصنوعی روی سیستم
• کنترل مرورگر برای جستجو، کلیک، تایپ و انجام وظایف مختلف
• دسترسی مستقیم به داده‌های مالی از Yahoo Finance و World Bank
• سیستم حافظه برای یادآوری ترجیحات و سابقه کارهای شما
💻
قابل استفاده روی Windows و macOS (Apple Silicon)
🔗
اطلاعات بیشتر
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6184" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKwDIi5dNhZmdQnj5tYTaghTtmmnvUC0PUw8VUHYPLn97QwrG1vbJCoZKf3Vc5SU8S2hR9rFm8Fueivjo5-cRq3wXE-MWHyc1hLBMPWplh3-vEZGiuOvDifueaEMZRaXK4hJDdGW-NUgrDqao1LXvuirPLdg3V8NZ0iEpScTaPJxrMb_UAuHUrxpYPIvOTRqeyrmSPaob00cuGF3ahqNWEodwjZG-bCrH8rZbC9C3rKio03cLXwGbGQXNUBDDc8pWmWMaxu9UcIjpZscvZvUhyE1BKTCRCJrqL9Nbey3ZDQln54YTS2EwZcpnXYVF3bvsFHexA6bP9uyIozY1UhzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
جعبه ابزار رایگان ویدئو
🔸
فشرده‌سازی ویدئو برای صرفه‌جویی در فضا.
🔸
برش سریع.
🔸
حذف کامل صدا.
🔸
ایجاد GIF از هر ویدئویی.
🔸
تبدیل بین فرمت‌های محبوب.
🔸
کنترل سرعت پخش.
🔸
افزودن واترمارک‌ها.
🔸
ادغام چندین ویدئو در یک فایل.
🔸
همه چیز به صورت محلی روی دستگاه شما انجام می‌شود.
https://www.zipvid.online/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6181" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
هکرها با سوءاستفاده از ابزار هوش مصنوعی متا، بیش از ۲۰ هزار حساب اینستاگرام را هک کردند
شرکت Meta اعلام کرد حدود
۲۰٬۲۲۵ حساب اینستاگرام
در جریان سوءاستفاده از ابزار هوش مصنوعی پشتیبانی این شرکت، در معرض تصاحب قرار گرفته‌اند. مهاجمان با فریب چت‌بات پشتیبانی مبتنی بر AI، موفق می‌شدند ایمیل حساب قربانی را تغییر داده و سپس رمز عبور را بازنشانی کنند.
🎯
در میان حساب‌های هدف قرارگرفته، نام حساب‌های مرتبط با
کاخ سفید دوران اوباما، برند Sephora و جان بنتیوگنا (Chief Master Sergeant نیروی فضایی آمریکا)
نیز دیده می‌شود.
🔒
متا می‌گوید این آسیب‌پذیری برطرف شده، لینک‌های بازنشانی رمز عبور نامعتبر شده‌اند و حساب‌های آسیب‌دیده تحت اقدامات امنیتی اضافی قرار گرفته‌اند. این حمله عمدتاً حساب‌هایی را هدف قرار می‌داد که
احراز هویت دومرحله‌ای (2FA)
نداشتند.
💡
این اتفاق بار دیگر نشان می‌دهد که واگذاری فرآیندهای حساس امنیتی به سیستم‌های هوش مصنوعی بدون کنترل‌های کافی می‌تواند پیامدهای جدی داشته باشد.
#Instagram
#Meta
#CyberSecurity
#AI
#Hacking
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6180" target="_blank">📅 18:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3BfOjgoIokQbVNxEsgG_TPxbc3K-BZQBv3jJ2bHDomCU9nVGtTPOKNm1dW2uqWn9pvH63Pq4L_Y8W86jE9oOE_vZ9cLfzsyESk9EL8u9IW_zfnR_DJ4DmgGLuRfXKAQ722rPOvnRgZ1y5PZ8Q23USxjXA6cHDsKvmFV3vHUCfKL4hPIazKq-vn7kIsVgBhhIKFyp00iI5BAC6v8r-6jR-6iSdsvSnE850oucdk5X-hBopV7gvM1DGsxDNYKK3eB_mGhAaJewQx7aTUFGoahQ-QdF-iEiBpHr9-aeGg6WxTUq1X0Qb5qi_yvycmyG4-4XCyFIw_M_rZiTJ28sLpLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦾
شبکه‌های عصبی اکنون شبکه‌های عصبی دیگری می‌سازند — با عامل هوش مصنوعی خودکار ML Intern آشنا شوید.
⚡️
دیگر نیازی به یادگیری کد ندارید — عامل هوش مصنوعی مقالات علمی را می‌خواند و مدل را برای نیازهای شما می‌سازد
💎
مستندات Hugging Face را مطالعه می‌کند، مجموعه داده ها را جستجو می‌کند، کد می‌نویسد و آموزش را اجرا می‌کند
💥
خطاها را پیدا می‌کند، کد را اشکال‌زدایی می‌کند و شبکه عصبی آماده را مستقر می‌کند
🔗
https://github.com/huggingface/ml-intern
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6179" target="_blank">📅 18:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
کمپانی
OpenAI حالت Lockdown Mode را برای ChatGPT معرفی کرد
🔒
شرکت
OpenAI
قابلیت جدیدی با نام
Lockdown Mode
را برای ChatGPT معرفی کرده که با غیرفعال کردن دسترسی به اینترنت، Deep Research و Agent Mode، خطر نشت اطلاعات محرمانه از طریق حملات Prompt Injection را کاهش می‌دهد.
⚡
این حالت به‌طور کامل جلوی این حملات را نمی‌گیرد، اما آخرین مرحله استخراج داده‌ها را مسدود می‌کند و امنیت بیشتری هنگام کار با اطلاعات حساس فراهم می‌سازد.
💡
با وجود این قابلیت، OpenAI تأکید می‌کند که Prompt Injection همچنان یک چالش حل‌نشده در مدل‌های زبانی است و کاربران باید در استفاده از داده‌های محرمانه احتیاط کنند.
#OpenAI
#ChatGPT
#AI
#CyberSecurity
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6178" target="_blank">📅 17:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
ss://2022-blake3-aes-256-gcm:dxzSnG5le2y16bNqdyL2Hj2b9Qjptq2Ust7li7mLR6Q=%3AGZs23OkRjsO4i11hMhke9I48yENOx6VVuL23GKRXTi0=@37.32.8.201:8080#%D8%A2%D8%B1%D8%B4%DB%8C%D9%88%20%D8%AA%D9%84%20%D8%A7%D9%88%D8%B4%D8%A7%D8%AE%D9%84%D8%A7%D8%B1%DB%8C
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6177" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb2k9FMt4_gPhtel-dRVEFN_KcNwzCKfUAAxcSzKux8n3_hQNU_KUs5wgqMbCRz6vhYzim5SMB9V0MrTvj4RKktGN_csdp0b5scGv0UEF5aPK3dxQn2vQJgORa_PDwqr1J54llmwJi1kpooNQmdT8yWHw8XYmj6-dJ4OgoqJMLsMJ08_NFNvDYpVhY9IjIjRVkJieGSTARTlf5M8GlEhuLnW2NFkdKUm5e3GNWH_jJA7KBO2tO8-dh192F7u7spPB8Ksk8SiolEUYU2xoa63JXY2X4tMd0x3VSHnkA8q5rVy6wjIDhmr5IyYKX4n2P2S_lXee3IKMW3e973dGDpv1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار تازه و ناب
🔥
@ArchiveTellNews</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6175" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6173" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=g50X7vgpaH3MycYV_kt7EFNcFvHpciVyKiXSeWgQLjskjCqgGb9eTI96AEOD-jKEutC5hAcCo9K7qausDV5dARKYuyKxLEXClppknRlBuTdnl3YzEbyyv7GoJMj3Vpu1dTf3a6h2wSSZ8EqNKa9fLfz0pJMYyqFME8LL5W-WXyTAI9XKpxCeprrS2XCglk9UavmMXjD7lCH_Ym_pwrer9TBZnn4PBEQc6lM0StRz4227dErSN-lrZx09yOlcCG2Rzh17z8XBuX_tf-m0nkwhGTXmeY2vetpMOWjzbAl8hB0qcDoe7ckqPPEknQb6byB9fMQV3kSpA7Z4U5rJK94U_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=g50X7vgpaH3MycYV_kt7EFNcFvHpciVyKiXSeWgQLjskjCqgGb9eTI96AEOD-jKEutC5hAcCo9K7qausDV5dARKYuyKxLEXClppknRlBuTdnl3YzEbyyv7GoJMj3Vpu1dTf3a6h2wSSZ8EqNKa9fLfz0pJMYyqFME8LL5W-WXyTAI9XKpxCeprrS2XCglk9UavmMXjD7lCH_Ym_pwrer9TBZnn4PBEQc6lM0StRz4227dErSN-lrZx09yOlcCG2Rzh17z8XBuX_tf-m0nkwhGTXmeY2vetpMOWjzbAl8hB0qcDoe7ckqPPEknQb6byB9fMQV3kSpA7Z4U5rJK94U_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
AlicentAI — هوش مصنوعی برای ایجاد محتوای متنی
💎
این سرویس پست‌ها، توضیحات محصولات و مقالات را بر اساس درخواست‌های متنی تولید می‌کند.
⚡️
از طریق وب کار می‌کند که در آن می‌توانید بلافاصله نتیجه را برای نیازهای خود ویرایش کنید.
🔗
https://alicent.ai/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6172" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">برای مدت کوتاهی اخبار مهم رو منتشر می کنیم
🙏
❤️
کنسل شد نمی کنیم
😂</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6170" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
تهران پارکینگ‌های زیرزمینی را به پناهگاه تبدیل می‌کند
بر اساس اعلام شهرداری تهران، در پی افزایش تنش‌ها و حملات اخیر، پارکینگ‌های زیرزمینی در سطح شهر به‌تدریج برای استفاده عمومی به‌عنوان پناهگاه آماده‌سازی و تجهیز خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6169" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم  بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6168" target="_blank">📅 12:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم
بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی یک عملیات جدید محسوب نمی‌شود، بلکه ادامه عملیات Operation Rising Lion (شیر خیزان) است.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6167" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نت رو قراره بزنن
ای‌ک</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6166" target="_blank">📅 12:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
منابع ارتش اسرائیل: آماده سناریوی حملات گسترده حزب‌الله هستیم
بر اساس گزارش رسانه‌های اسرائیلی، منابع نظامی این کشور اعلام کرده‌اند که هماهنگی کاملی با آمریکا برقرار است و هم‌زمان برای احتمال حملات موشکی یا پهپادی گسترده از سوی حزب‌الله به مناطق مختلف اسرائیل آماده می‌شوند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6165" target="_blank">📅 12:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی
💎
vless://1b5607ba-c295-43f8-923a-dc633a099276@82.47.63.98:8443?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=farsroid.com&mode=auto&path=%2Flokayb&pbk=US5uDp2cCip8cEuQUWEf4o7VbASXg45EeVia_Kz2QTI&security=reality&sid=fc0f43e6354ef57b&sni=www.qq.com&type=xhttp#%F0%9F%94%B5@ArchiveTell%20%7C%2050GB
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6164" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شرکت Wizz Air اعلام کرد تمامی پروازهای خود به اسرائیل را حداقل تا فردا لغو کرده است. برخی پروازها نیز در مسیر فرود به تل‌آویو به مقصدهای جایگزین مانند لارناکا هدایت شدند.
در همین حال، سازمان فرودگاه‌های اسرائیل اعلام کرد که فرودگاه بن‌گوریون همچنان به‌صورت عادی فعالیت می‌کند و پروازها طبق برنامه در حال انجام هستند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6163" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📰
گزارش‌ها از حملات به مواضع امنیتی در ایران
بر اساس گزارش‌های منتشرشده از منابع ایرانی، چندین موضع و تأسیسات امنیتی در نقاط مختلف کشور، از جمله استان استان همدان، هدف حملات قرار گرفته‌اند.
همچنین برخی منابع وابسته به اپوزیسیون ایران مدعی شده‌اند که تعدادی از نیروهای بسیج برخی مواضع خود را به دلیل نگرانی از حملات احتمالی ترک کرده‌اند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6162" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇩🇪سرعت فضایی.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/archivetell/6159" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حجم : ۲ ترا
💎
متصل رو همه اپراتور ها
✅
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6159" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4d671db5.mp4?token=EzbC4zZ4fbzoikC6K9Nxeouip5rzFNTsJYJgOtMyWn7W72C6kS0Kme_BKZFEFgDqTjRzHWjTK1cOhzkRkQjo3lYRU1-UYrfln9p6U_Hzst4Dvc4IllVPAHurqIrAog6zf39mnIrx8UhigTRSfLT8I6eiN1tiVtL1pnq2ZU3Hsdi-408qUnWny36RGDNxjuaN06-HQccYZ2iVNaUV4T_Af3vNZvQZq93YIVJBvwGOyPvOFNAb-MEqg4hlX5QZ16GmrgeGYXDBnIDGzHifQ73b9mifY5GXBwZHftvHhIcvjt-3HgDmfZgk1ctQSnDvSGGnCJ7UedPPTjJzo9rGK90NoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4d671db5.mp4?token=EzbC4zZ4fbzoikC6K9Nxeouip5rzFNTsJYJgOtMyWn7W72C6kS0Kme_BKZFEFgDqTjRzHWjTK1cOhzkRkQjo3lYRU1-UYrfln9p6U_Hzst4Dvc4IllVPAHurqIrAog6zf39mnIrx8UhigTRSfLT8I6eiN1tiVtL1pnq2ZU3Hsdi-408qUnWny36RGDNxjuaN06-HQccYZ2iVNaUV4T_Af3vNZvQZq93YIVJBvwGOyPvOFNAb-MEqg4hlX5QZ16GmrgeGYXDBnIDGzHifQ73b9mifY5GXBwZHftvHhIcvjt-3HgDmfZgk1ctQSnDvSGGnCJ7UedPPTjJzo9rGK90NoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📨
پیدا کردن اطلاعات از یک آدرس ایمیل - این سرویس ردپای دیجیتالی آدرس ایمیل شما را در منابع آزاد آشکار می‌کند.
🔥
حساب‌ها و پروفایل‌های عمومی مرتبط با آدرس ایمیل شما را جستجو می‌کند.
⚡️
منشن‌ها و سایر داده‌های عمومی که ممکن است به صورت آنلاین در دسترس باشند را نشان می‌دهد.
💥
به شما کمک می‌کند تا ارزیابی کنید که جمع‌آوری اطلاعات در مورد شما از یک آدرس ایمیل چقدر آسان است.
💎
فوق‌العاده ساده است: آدرس ایمیل خود را وارد کنید و نتایج را ببینید.
🔗
https://behindtheemail.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6157" target="_blank">📅 09:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSsVwOL4vKIkwxkqHl7CJhUdDH0Capi44PD87iaEqbzSxkYyuIk9j20NrTYagHDenZ4Mc-7SQHpQroQnHoERxBWzDqa0l2Vwco7L471uhWSebdSkQg9QhNxH5rvWLZMSF6CQ4QLWe0h4jPR7qrD-rUXFI5nh6h2wU1snGJ4ita63oFRbmxpZyxon2btqO8Nb1rUJ-maV9QLTNZH8omiV-phsN1PpATf_-jgenby1oyQQWcG35bDAuAWxdZspEZHY5XyRF5JnfeIVOWOtzeKk8_qHr3TZdUfesXBcdtBfcVggMmaeH7cPlC00iFraLp4_fafKdYf3mID1iPYVctcw7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جمع‌آوری داده‌ها از تلگرام به صورت خودکار - یک اسکریپت پایتون به طور خودکار پیام‌ها و رسانه‌ها را از کانال‌های مورد نیاز جمع‌آوری می‌کند.
⚡️
پست‌ها را از کانال‌های تلگرام در قالبی ساختاریافته ذخیره می‌کند.
💎
عکس‌ها، ویدیوها، اسناد و سایر پیوست‌ها را به طور خودکار دانلود می‌کند.
🛡
از نظارت مداوم و جمع‌آوری نشریات جدید پشتیبانی می‌کند.
📱
به شما امکان می‌دهد داده‌های جمع‌آوری‌شده را برای تجزیه و تحلیل و پردازش بیشتر صادر کنید.
💥
با پشتیبانی Telethon، یکی از محبوب‌ترین کتابخانه‌های تلگرام.
🔗
لینک پروژه:
https://github.com/DarkWebInformer/telegram-scraper
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6156" target="_blank">📅 08:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999b60eca7.mp4?token=Srs5-SmrdP_tYJ4RJ-WJT0hk2kTlfNXjTL6NKjJJHaPhmLcdyesh-GKSzdhkEL6n0HRqbuw0G6wcthNIQoShTxXuJGdKFE1TFFM4WvvY5yDYG1dPmoC4CXCLVsWZBt6BoaRP96pl1j4ePll6qIfywVoKuGKF3rCPDmka_Sbg3iOpw7RRex-6H7zhewJLb23yl6PSN5X_U3ec7Ub14ExcL2HRa1_x77GOzHzERoHsCa_Qpu4CQOzPKpoBNXYjy7RlqCn5gM4HESBpwsRpEFT-mdxYrhHfNJ2dzzTvF1EjvAbMAHuIfjOAnwK-oEscnZE3D2Hpbed7C7TCfgfF0mIlNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999b60eca7.mp4?token=Srs5-SmrdP_tYJ4RJ-WJT0hk2kTlfNXjTL6NKjJJHaPhmLcdyesh-GKSzdhkEL6n0HRqbuw0G6wcthNIQoShTxXuJGdKFE1TFFM4WvvY5yDYG1dPmoC4CXCLVsWZBt6BoaRP96pl1j4ePll6qIfywVoKuGKF3rCPDmka_Sbg3iOpw7RRex-6H7zhewJLb23yl6PSN5X_U3ec7Ub14ExcL2HRa1_x77GOzHzERoHsCa_Qpu4CQOzPKpoBNXYjy7RlqCn5gM4HESBpwsRpEFT-mdxYrhHfNJ2dzzTvF1EjvAbMAHuIfjOAnwK-oEscnZE3D2Hpbed7C7TCfgfF0mIlNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
🔥
جعبه‌ابزار حرفه‌ای برای ساخت AI Agentهای قدرتمند
برنده یکی از هکاتون‌های Anthropic مجموعه‌ای از ابزارها و تجربیات یک‌ساله خود را به‌صورت متن‌باز منتشر کرده است؛ یک پکیج کامل برای ارتقای Agentهای هوش مصنوعی.
🚀
✨
داخل این مجموعه:
•
🧠
بیش از 183 مهارت (Skills) آماده
•
🤖
بیش از 48 ساب‌ایجنت تخصصی
•
⚡
بیش از 69 دستور Slash برای خودکارسازی کارها
•
💻
قوانین و Best Practice برای 12 زبان برنامه‌نویسی
•
🛠
ده‌ها ابزار، Workflow و الگوی کاربردی
🎯
سازگار با:
Claude • Cursor • Codex CLI • OpenCode و سایر ابزارهای محبوب توسعه مبتنی بر AI
اگر روی Agentها، اتوماسیون، کدنویسی با هوش مصنوعی یا ساخت دستیارهای سفارشی کار می‌کنید، این پروژه ارزش بررسی دارد.
🔗
لینک پروژه:
https://github.com/affaan-m/ECC
#AI
#AIAgent
#Claude
#Cursor
#OpenSource
#GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6155" target="_blank">📅 08:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Always-OBITO.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/6154" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6154" target="_blank">📅 07:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6153">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWAw6Xkl7ocNGUTOLd2dzu37cJ6YBo-C-bIvRoOKQkV2htox3-xq-B8N8CP8s5NQ3l4pb4X0aRQsv83uOEEzPn0C-XZu49smg1zSp1FHnj7HT16130l0u4EBp_1GxYzhK8ghtP7oDF_mpD3VAmCxlLJCbunKdsOsqRyaxrTvmMV4YBgUN4wVoQOKZQVhCWcn9EXPh0nqkFazfmC5LlcWl5oFpTg0aABJt4lzv6WyF01dtSH0Jbs65PRodJjl0biSVXhiQ5s1oOaTOSRVGYoOD4AL1WeuBRI_mrTmiTR53I0lkIb9cvcVVcWKD2XWiOqqKO2IQ_OF08OfDBOVqED6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی وایرگارد میخواد....؟!
@Sina_1090</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6153" target="_blank">📅 04:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه اینترنت ملیمون نشه؟
طرف آدم بدام*
کانفیگ فروشارو می گم</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6152" target="_blank">📅 03:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
60GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: 1 GB
⏰
مدت اعتبار: 3 روز
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6151" target="_blank">📅 01:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">vless://f5ed097b-b078-45fa-bf8b-a534f94206db@85.198.20.217:443?path=%2F&security=&encryption=none&host=play.google.com&type=ws#hetzner - heybaat  نامحدود تانل  وصل شدید دعا کنید</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6150" target="_blank">📅 01:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXHddw4vqz3w5XZqNb8eH6IbCv3wOi0Rk9uKhGiRMIpwI968_nyhoZ8Z9Zgyl2jvA4n3_25HoerXePmlj2XIaDH3RqJRhnl60mwfkMU-GhQKH_sg2OCMMIDGb5ly9l9mCpABgym4VsAh5HtnJmSB9ekRXWleSAKOxq_GiiBuYNun66f4Uv2Ng0z3kptztJUPll6DdvaHRQk7FZTAYR_7N4NKqrhyq0B-2r0bM2BVRlhwnzvLEBaHmFrzndG8idex6XPLqoocwjXO_akNq9p5kT7b1UmWRGHIacGQWBmQxTo0g_OAW1MKCLtW5bzb4ukM7uovQ_XNdgm2Pi_ksBARuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم اطلاعات
قیمت هم 720
سرعت گاد
@Sina_1090</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6149" target="_blank">📅 01:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">vless://f5ed097b-b078-45fa-bf8b-a534f94206db@85.198.20.217:443?path=%2F&security=&encryption=none&host=play.google.com&type=ws#hetzner - heybaat
نامحدود تانل
وصل شدید دعا کنید</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6148" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نصب انواع تونل های DNS بر روی سرور شخصی:
curl -fsSL https://raw.githubusercontent.com/anonvector/slipgate/main/install.sh | sudo bash
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6146" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اگه نمیزنید ما بریم بخوابیم</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6145" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Fasten your seat-belts
Pack your Backpack
🗿
😂</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6144" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">185.226.117.8.txt</div>
  <div class="tg-doc-extra">38.3 KB</div>
</div>
<a href="https://t.me/archivetell/6142" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ریزالور</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/6142" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-universal.apk</div>
  <div class="tg-doc-extra">16.9 MB</div>
</div>
<a href="https://t.me/archivetell/6141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/6141" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ریزالور
95.80.164.6
84.241.3.33
185.179.170.127
188.136.174.86
46.143.244.4
46.100.46.8
46.32.4.164
62.60.167.216
185.128.138.250
185.128.138.249
188.121.129.238
93.115.151.185
10.233.249.52
217.170.242.11
185.57.135.72
2.180.21.144
213.176.4.6
93.118.162.116
5.160.162.44
77.238.123.238
216.147.121.66
176.59.222.24
216.147.121.152
95.217.210.65
176.59.31.187
178.252.180.62
176.59.31.198
176.59.222.28
176.59.31.195
176.59.31.197
81.168.119.130
216.147.121.105
176.59.222.30
176.59.222.31
176.59.31.191
176.59.31.192
176.59.222.27
176.59.31.194
176.59.222.25
176.59.31.189
176.59.222.29
176.59.31.186
176.59.31.188
176.59.31.184
176.59.31.196
176.59.222.26
176.59.31.193
176.59.62.14
176.59.31.190
176.59.31.199
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/6140" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ربات تست ۱۰۰ مگ فقط با ۴۰۰ تا رفرال بزن رو لینک</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6139" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279755f66a.mp4?token=f_DSNacsMvsgqutRqlcucGINMXBvuutOI-E3ohiF7svJ_GFHKLpxmMigQVolO4KFKkkIW5jnKbnH9_gmeS6bwtJq8f9QJJ485pow4MUqGDSfsTCZUxgPNI2-xra9AiJHuu1FYoBK21_yTrcTdU-vpU3eyshc1ySfSCTRRdE01kgmVHY2E3UHVwC8YwlePnpY7FnOecfaVRs6_MvvzuqqZsdvbgDc_Ml_-3r9BVtfMDudf7s1ETSmeqKVBXOXwZk4PxKBVfsg8bYS0gd77MGWvhAwOl9PKLa_qtrwKDqMDRLyKwex9Y2qppfArIjADxnYEpPucoJ7I9ZVEm3wFyxvRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279755f66a.mp4?token=f_DSNacsMvsgqutRqlcucGINMXBvuutOI-E3ohiF7svJ_GFHKLpxmMigQVolO4KFKkkIW5jnKbnH9_gmeS6bwtJq8f9QJJ485pow4MUqGDSfsTCZUxgPNI2-xra9AiJHuu1FYoBK21_yTrcTdU-vpU3eyshc1ySfSCTRRdE01kgmVHY2E3UHVwC8YwlePnpY7FnOecfaVRs6_MvvzuqqZsdvbgDc_Ml_-3r9BVtfMDudf7s1ETSmeqKVBXOXwZk4PxKBVfsg8bYS0gd77MGWvhAwOl9PKLa_qtrwKDqMDRLyKwex9Y2qppfArIjADxnYEpPucoJ7I9ZVEm3wFyxvRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6137" target="_blank">📅 22:49 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
