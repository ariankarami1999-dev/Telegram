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
<img src="https://cdn4.telesco.pe/file/C7TUBpbNoQzG6br1alPl75fnlC_72aY7yAhs5yHym17-XbDZHY-hzJag-kUnY5rYUELwUnAqvpQ4AOvWT1pju9xhCf1T9SJAzIKq7YiGzPQPd2nPMuKn_6a7micDFe0NMGhjscsI7UT4IvY7qT6Zh904FGej8IwuH_7xFHSfrUtusIg1QA1uraSdShUBab8kmStgwIHvVfEovftsaiyIXqdznb6ONOkM-X2wmvh5nxS7cTgFTT1-Iut_WcS7bOJrgAwAJuZ7S_L2aB-bk6gbuVJ7HliO0ZqsQuNz4oYN9mHaiNxymqFAujyf3VpUJFUthv0FRGy0-ywp3hWmoEGM4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.82K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 21:26:16</div>
<hr>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">#اختصاصی
شبیه‌سازهای پلی‌استیشن
🎮
PS1:
duckstation.org
PS2:
pcsx2.net
PS3:
rpcs3.net
PS4:
shadps4.net
PSP:
ppsspp.org
PSV:
vita3k.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 472 · <a href="https://t.me/ArchiveTell/6791" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://878fa338-f275-4bf6-93ea-ef47d8865f59@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/ArchiveTell/6790" target="_blank">📅 19:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=m3_irec0w3CTaLdCAmoTBxRPnDUgjFMhZ0jg9Msp-wZLb5z3g5bdtlNjw1iiKbbICcD2UUsKCeTlawMxPMiOA2WVnOA61eFBMqk2ZGnQZUuAW2GMlGxRjhY0E4zylW_bEQiywYkqm4Sx5ZHqsHxHE0bxDpGs5U1JyE14my9toDIwayWO5-yLEhXZaYOJ0xiVA4ScmRzqKkeqgNqDeL56qGHHSXBGvgytpS622_g4IFajvH6c8m3FSHWpIxdVX4Owg4Zzojpj1qZismLrwA6wjUtAG3Tc-1DM0iD5zXUDs35I3qnIfJQ5U2pw9lmVko-LTa3CcdXelTEjVntY5aijtxkNIz-4B0nCyrmjKReC4R_9n4aCGjwZAgodAjzyEicssY_zeAT-9Yad75tuoZCiuk0umZjBZjIGeDH8YNcZseP_nhirEcGQPx0OFgUgi9J7BTAahSyDpct4xSj40KUdulDsbTtLDPaLqOC6T-X6vMK1EO4HHKb8pi5TSaoTNRdA4db-jYKdT5aptlcbJY1vI-EYTOVvOrXcaRxbbtG1iSCiXNyueT1YVZvI0Aky3iyJzNIdoYoSkUgIBC4fkdLHDdIUHVBHm2E9SiPyAAVWRjzSl6vAzGEsJ-WYghQJ9tg4vo83DtnvdVygbXGKAiBNuvsggpm6NnE2R0wgMm0zQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=m3_irec0w3CTaLdCAmoTBxRPnDUgjFMhZ0jg9Msp-wZLb5z3g5bdtlNjw1iiKbbICcD2UUsKCeTlawMxPMiOA2WVnOA61eFBMqk2ZGnQZUuAW2GMlGxRjhY0E4zylW_bEQiywYkqm4Sx5ZHqsHxHE0bxDpGs5U1JyE14my9toDIwayWO5-yLEhXZaYOJ0xiVA4ScmRzqKkeqgNqDeL56qGHHSXBGvgytpS622_g4IFajvH6c8m3FSHWpIxdVX4Owg4Zzojpj1qZismLrwA6wjUtAG3Tc-1DM0iD5zXUDs35I3qnIfJQ5U2pw9lmVko-LTa3CcdXelTEjVntY5aijtxkNIz-4B0nCyrmjKReC4R_9n4aCGjwZAgodAjzyEicssY_zeAT-9Yad75tuoZCiuk0umZjBZjIGeDH8YNcZseP_nhirEcGQPx0OFgUgi9J7BTAahSyDpct4xSj40KUdulDsbTtLDPaLqOC6T-X6vMK1EO4HHKb8pi5TSaoTNRdA4db-jYKdT5aptlcbJY1vI-EYTOVvOrXcaRxbbtG1iSCiXNyueT1YVZvI0Aky3iyJzNIdoYoSkUgIBC4fkdLHDdIUHVBHm2E9SiPyAAVWRjzSl6vAzGEsJ-WYghQJ9tg4vo83DtnvdVygbXGKAiBNuvsggpm6NnE2R0wgMm0zQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چینی‌ها یک "غول" جدید برای تولید تصاویر معرفی کردند: Seedream 5.0 Pro.
ویژگی‌های این ابزار:
🔹
ویرایش لایه‌ای تصاویر
📦
‏
🔹
ترکیب چندین تصویر در یک طرح کلی
📚
‏
🔹
تنظیمات جداگانه برای سبک هر شیء
🎨
‏
🔹
ویرایش محلی مناطق انتخابی
🔍
‏
🔹
تغییر تصاویر بر اساس دستورات متنی
📝
‏
🔹
تطابق دقیق‌تر خروجی با درخواست
📊
‏
🔹
بهبود عملکرد در کار با متن داخل تصاویر
📚
‏
🔹
تولید اینفوگرافیک، نمودارها و سایر مواد بصری
📊
‏
نسخه ‌Lite⁩ رایگان در ‌
Higgsfield⁩
و ‌
Dreamina⁩
قابل آزمایشه
📦
👀
‏نسخه ‌Pro⁩ از طریق ‌API⁩ در دسترسه
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/ArchiveTell/6788" target="_blank">📅 19:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGcECkFpXtwBQsZplaNhebzIl9cY-XzUqr_t18eRkDjRtoIx5nKXfmncGnPoq5zkn6-uYaC7lg3hsYa4TOKQUrvgS7Ac3MQAWJgIXH5GxtlNwdX6xD5WDgEoUPO4_Zfzn-wka6ePVFFLllE8KmBvHImS-Hl9uImBFEb7B_W3GWk7rhO2ODcn5VseobJEg-tDxjMlhKrtH5tRqb6wrUKnCmrFSE8x7d1v60AhNVmTyRFZ5tftP4Exi6H5bN_pTWpvDFCS0PBA2o93ShlnzzOhBOHa2rZAVXzDwFN7fKiuAg_ZkTcJ8TXVtTzGEaXOo9JcWg2nFgY6afi1uYPNMyutcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرورگر
DuckDuckGo
در جدیدترین به‌روزرسانی خود قابلیتی اضافه کرده که امکان
حذف تبلیغات ویدیوهای یوتیوب
را فراهم می‌کند
🌐
این ویژگی با استفاده از فیلترهای
uBlock Origin
کار می‌کند. هرچند ممکن است در برخی مواقع
زمان بارگذاری
یا
بافر شدن
ویدیوها کمی بیشتر شود، اما در عوض می‌تواند تجربه‌ای بدون
تبلیغات
و روان‌تر هنگام تماشای ویدیوهای یوتیوب ارائه د
هد
😎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 838 · <a href="https://t.me/ArchiveTell/6787" target="_blank">📅 18:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
Recordly | ضبط و ویرایش حرفه‌ای صفحه‌نمایش
✨
یک نرم‌افزار متن‌باز برای ضبط صفحه نمایش که ابزارهای ویرایش را هم در خودش دارد؛ مناسب ساخت ویدیوهای آموزشی، دمو و معرفی محصول.
🚀
⚡
ویژگی‌ها:
🎬
ضبط صفحه، پنجره و صدا
🖱️
زوم خودکار، افکت‌های موس و حباب وب‌کم
✂️
تایم‌لاین ویرایش، برش و افزودن متن
📤
خروجی MP4 و GIF
💻
پشتیبانی از ویندوز، لینوکس و macOS
🔗
https://github.com/webadderallorg/Recordly
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 911 · <a href="https://t.me/ArchiveTell/6786" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6785">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🛡
Dangerzone | تبدیل فایل‌های خطرناک به PDF امن
یک ابزار متن‌باز برای باز کردن امن فایل‌های مشکوک مثل PDF، فایل‌های آفیس و تصاویر؛ بدون نیاز به اعتماد به فایل اصلی.
🛡
⚡️
نحوه کار:
🗂
فایل داخل یک محیط ایزوله (Sandbox) پردازش می‌شود
🖼
محتوا به پیکسل تبدیل شده و دوباره به PDF جدید ساخته می‌شود
🚫
کدهای مخفی و عناصر فعال فایل اصلی حذف می‌شوند
✨
پشتیبانی از:
📄
PDF
📝
Word / Excel / PowerPoint
🖼
فرمت‌های تصویری مختلف
💻
قابل استفاده در:
Windows | macOS | Linux
📎
https://github.com/freedomofpress/dangerzone
🐍
زبان: Python
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 967 · <a href="https://t.me/ArchiveTell/6785" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3M5kD1_C8IlsZ2sd56qW_EezOhDpoyeCxV1bMTnKA0Kc3hbvBc_6I0gexM6uEYQuCd7M2to9qKlFUcPez7tVvmF_Q4axChSF6IWvzjK1KzpFSKB0Tg3HzX3w5ttmOOuk1CS48PDx0m39Y2GeBlPmPDj3gTFMTbD7GhaIyOmAc-5yardAbpekno5jvKE1o2NZ2BIY7qb8Bz5yQi53E0PY4Pjf8MXQpDndSOJVvg5HYmbv2OlfarmpvIbVYQPdZPNmvITQqTuU5sh3gSVFJ8tf7zFkIzv_Yb9XDpCWDhn5IW8GlQajUL3IsB_JrsImxOSrVuWMUWJFGmotJREOsu1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SubFarsiPro v5.0
📹
این ابزار، یک دستیار حرفه‌ای، پرسرعت و متن‌باز برای استخراج زیرنویس از ویدیوها و ترجمه دقیق اون‌ها به زبان فارسی (با لحن طبیعی و محاوره‌ای) هست
GitHub
🐱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/6783" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📊
دنبال معتبرترین رتبه‌بندی مدل‌های هوش مصنوعی هستی؟
اگر می‌خواهی عملکرد واقعی مدل‌های هوش مصنوعی را مقایسه کنی، این دو سایت را از دست نده:
🌐
Artificial Analysis
📈
یکی از کامل‌ترین لیدربوردها برای مقایسه مدل‌ها از نظر کیفیت، سرعت، هزینه، کدنویسی و ده‌ها بنچمارک معتبر.
🔗
https://artificialanalysis.ai
💻
DeepSWE
🧑‍💻
یکی از بهترین بنچمارک‌ها برای سنجش توانایی برنامه‌نویسی مدل‌ها با استفاده از پروژه‌های واقعی و جدید، نه سؤالات قدیمی و حفظ‌شده.
🔗
https://deepswe.datacurve.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/6782" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/6780" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ارسالی یکی از یوزرای گل
👇</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/6779" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/6778" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔥
دسترسی رایگان به هوش مصنوعی قدرتمند Fable 5
اگر دنبال تست مدل‌های پیشرفته هوش مصنوعی برای
برنامه‌نویسی، تحلیل و کارهای پیچیده
هستید، این روش می‌تواند جالب باشد.
🌐
پلتفرم
Tasklet.ai
امکان استفاده محدود رایگان از این مدل را فراهم کرده:
✅
۵۶۰۰ کردیت ماهانه
✅
۳۰۰ کردیت روزانه
✅
مناسب برای تست و استفاده‌های روزمره
📌
روش استفاده:
1️⃣
با ایمیل ثبت‌نام کنید
2️⃣
وارد پنل شوید
3️⃣
از بخش انتخاب مدل،
Fable 5
را انتخاب کنید
هر بار کردیتتون تموم شد میتونید اکانت جدید بزنید
🤝🏻
لینک
🔗
:
Tasklet.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/6777" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🗂
نام‌گذاری هوشمند فایل‌ها با هوش مصنوعی (
Renamer.ai
)
پایانی برای کابوس فایل‌های بی‌نام‌و‌نشان مثل
Scan_001.pdf
. این ابزار به جای تغییر ساده متنِ اسم فایل، محتوای متنی و تصویری داخل آن را آنالیز کرده و نام‌های دقیق و جستجوپذیر پیشنهاد می‌دهد.
🔥
ویژگی‌های مهم:
*
🧠
درک محتوای فایل:
استخراج فاکتورها، تاریخ‌ها، نام شرکت‌ها و موضوعات داخل اسناد، تصاویر، اکسل و PDF به کمک فناوری OCR.
*
📸
سیستم پیش‌نمایش:
امکان بررسی و تایید اسامی پیشنهادی قبل از اعمال نهایی روی سیستم برای جلوگیری از خطا.
*
📂
پوشه جادویی (Magic Folders):
مانیتور خودکار پوشه‌های انتخابی (مثل Downloads) و نام‌گذاری آنی و اتوماتیک فایل‌های جدید.
*
⚠️
نکته:
نسخه رایگان محدود به ۲۵ فایل در ماه است. همچنین به دلیل پردازش ابری، بهتر است برای اسناد فوق‌محرمانه و اطلاعات حساس مالی استفاده نشود.
🔗
لینک وب‌سایت ابزار
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/6776" target="_blank">📅 12:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌐
وب‌گردی و انجام خودکار کارها با هوش مصنوعی (Browser Use)
یک فریم‌ورک اوپن‌سورس (پایتون) که مرورگر شما رو در اختیار مدل‌های هوش مصنوعی (مثل GPT و Claude) قرار میده تا کارهای اینترنتی رو دقیقاً مثل یک انسان براتون انجام بدن.
🔥
ویژگی‌های مهم:
🤖
اجرای خودکار وظایف:
کافیه با زبان طبیعی بهش دستور بدید (مثلاً "این فرم استخدام رو با اطلاعات رزومه من پر کن" یا "این لیست رو به سبد خریدم اضافه کن").
🧠
پشتیبانی از انواع LLMها:
کاملاً سازگار با مدل‌های معروف و حتی مدل‌های آفلاین/لوکال.
💻
ابزار CLI حرفه‌ای:
قابلیت اتصال مستقیم و راحت به ایجنت‌های کدنویسی.
⚡️
جایگزین مدرن:
بدون نیاز به درگیری با ابزارهای قدیمی مثل سلنیوم، خودش با المان‌های سایت تعامل می‌کنه.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/6775" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JapSbfCnpFeXTnz58PQ3EFxQ2f3RpZq52DoMp_osJ3tF3vl84jaZpJtWktRvl5nBT0owQTbE7UgpwOkBm1ccXlMRkMJJwdQAMNx9QZ7kZU8tGv95rIbyL0yvEZcsczK1HGvX_NjB7mUwAKTfn22R0d8uomQSQHm0Vxfn4hlA21hy2bAdKkniF3d1LqhZdaI5a21Lb4AFOwCH3Cmn1KqHgExaSfIRJUQq6XsUsgfpzRart9UWEPk3ZyqHKytNrNN87S3QzsaiyxT_xLZYCVMNZ7myhlqPFUP0T2MXW0E8g2alEJ7RWONVoi9GpR6shW_Dv50BL1rYJFm1OxHGW3HobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
معرفی Google Flow
این سایت جدیدی نیست ولی خب بعضی دوستان دیدم نمیشناسنش گفتم معرفیش کنم
😁
اگه دنبال یه ابزار رایگان و قدرتمند برای ساخت تصویر با هوش مصنوعی هستی،
Google Flow
یکی از بهترین گزینه‌هاست.
ویژگی‌ها:
✨
تولید تصاویر با مدل‌های
NanoBanana 2
و
NanoBanana Pro
🖼️
ویرایش تصاویر (چه ساخته‌شده و چه آپلودی) با پرامپت
🪙
ساخت تصویر با
۰ سکه
(رایگان)
📚
امکان ساخت همزمان چند تصویر و ادامه ویرایش روی بهترین نتیجه
🎥
قابلیت تولید ویدیو (با محدودیت بیشتر)
📌
لینک:
https://labs.google/fx/tools/flow
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/6774" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6773">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7jqo6V8yBNVqL30IDF2dA-1i5NkF7OzbXuqtsa7_qoZWxbTLsq-gnEkv3yBWwrcaMlryr5qHiAiSYYxwE-Xl5gMOqJC-Vb_najiZp90Yqhp8sw8hLO1SXGmHlWk71IDc1Dw-CSMG-Uzlj1paPDz4Z3RVxe0X1vpXWtZWmD9Cj83_Zn8ckOpM-dkpFnPg1ZUuZr6MdgNqVsgk0nydq34l6tSIH3HjlT6noHr1y-yM2VJpuTp4jRGYWRi6_NlarDYvUkZM6E0mikuswdJip-PGwUUkIh75YHbXrjyw-jOcVGSsMSm_zY_PEWO06BM-wfRFPMkVq-DAbR4sf2cRcnkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
WLLPR | ژنراتور والپیپرهای مینیمال
اگه از والپیپرهای تکراری خسته شدی، با
WLLPR
می‌تونی توی چند ثانیه والپیپرهای مینیمال و جذاب بسازی؛ اونم دقیقاً با رنگ و استایلی که دوست داری.
🎨
⚡
ویژگی‌ها:
• ساخت والپیپر برای
📱
موبایل و
🖥
دسکتاپ (4K)
• انتخاب رنگ، طرح و استایل دلخواه
• تولید نامحدود والپیپر با یک کلیک
• هماهنگ شدن رنگ رابط کاربری گوشی با والپیپر در بسیاری از گوشی‌های اندرویدی
🌐
لینک سایت:
https://bypedroneres.github.io/ai/
➖
➖
➖
➖
➖
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/6773" target="_blank">📅 10:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6772">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXyGHbLml5DzjjmT4sQFQmfX1W71Nd8bzrhGwPZd3dbAehSfNazUd3P5YWwqNDUf8b295E6IQC58iAq4dfXydPGd4TBOTGOCN3QpMNyXViqndePlvuBdbrZuElo7P5EZ_5DBdtwbmz5fOgmoCsny63Lhx9LkUyjTD9uRsgzB8feBKrfiCOQ6ZasT6UeC1YPmqUijhRVcZ9_GsK2VNZIuXL6btGSt-DV5rPTCO3ps0ahe7jnefKBFFm1kE049ypIYEbfaBLwqs511Glb7fMjgSM12YhR9fyAmo6EAlwoi_1_eIt_T1WLfybOVrszvThsh0gQtJk9kJDnFvQhHh_4tRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت OpenAI
نسخه‌ی GPT-5.6 را برای Sol، Terra و Luna از فردا راه‌اندازی می‌کند!
🚀
دسترسی زودهنگام از همین حالا برای کاربران در سراسر جهان فراهم شده، می‌توانید با خیال راحت وارد شوید و آن را بررسی کنید.
🌍
🔍
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/6772" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy5nwCj6cALialeXngS0wO_VVbwdJgF1-xM0laUUaQto-A38emKG2qD8vehFHT_-nlZKHvnxOCJSWV-ZWCrMMhsFsM7UB2BK_Dij4qAOZJhtuFxODENNNMTJ1TwLB_QkTZEf4W1g_L5ZEtPoZN-z0lkS7-KXbZXRdYUT0lNRQaK9gDoUOvqJOe6a73XbJiGMNlkjNbnl47GVWNr7ZUx-kShx9lDuvb79KtV0K1MmmiFdKo5s_wlwPFY_EvsUP7c_uz9W2PO2sKi7_1hUxCbYeKMls99n_OjkQ2Ty9s9gQEUGCZlQSBTXW7MbxwhPZiIp36LATnQRz1s8lwueeWBKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Constrict ناجی شما در فشرده‌سازی ویدیو!
📹
- ویدیو را آپلود کنید و اندازه مورد نظر را انتخاب کنید.
- بدون نیاز به سرویس‌های آنلاین و دستکاری‌های پیچیده در کدگذاری.
ساده، سریع و کاربردی!
https://github.com/Wartybix/Constrict
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/6771" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shWxaqEPTXQmvcWpI2lmoVGs3gJHvi8LR4xqppWQxnH89L6lyFzv2SEztVBHvJUYBDXZi8RNoCQUzvKZnEq1qiq8IvIVAIAOYzjP3NbGtwWqtdE_CU8IMu7x884-BnAVc9JwGqY3LDb6xOlvgyEOS918uSQQRUvFPdxaSKHtUfah9Zu6DtvV2b5UaAqfiWHiNX8uhbt1W2h9lrzXTfTQ4Rz9oCEMiM50SDCzSVOc6CWHqvtr2rqPBaELa4p2LNXp4UYfCyU3c7Trrl9qNg6Mle43A811oIAaam4UoXqTDabrLq3vX7hdtClvPIsWmYmhpbtOGZp4d9ouNmmAhosLLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تحلیل ویدیوهای یوتیوب، تیک‌تاک و فایل‌های محلی با هوش مصنوعی
؛
Claude Video
یک ابزار متن‌باز است که امکان تحلیل ویدیوها را برای دستیارهای هوش مصنوعی فراهم می‌کند. کافی است لینک یک ویدیو یا فایل محلی را به آن بدهید تا فریم‌های تصویر و متن گفتار را استخراج کرده و در اختیار مدل قرار دهد؛ سپس می‌توانید درباره محتوای ویدیو سؤال بپرسید یا خلاصه آن را دریافت کنید.
⚡️
ویژگی‌های کلیدی:
-
🎬
پشتیبانی از ویدیوهای
YouTube، TikTok، X، Instagram، Loom
و صدها وب‌سایت دیگر
-
📂
تحلیل فایل‌های محلی مانند
MP4، MOV، MKV
و
WebM
-
🖼
استخراج خودکار فریم‌های مهم و متن گفتار (Transcript)
-
🧠
امکان پرسش درباره بخش‌های خاص ویدیو، خلاصه‌سازی و تحلیل محتوای تصویری
-
🤖
سازگار با
Claude Code، Claude Web، Codex
و ابزارهای مشابه
-
🔓
متن‌باز با
لایسنس MIT
🔗
گیت‌هاب پروژه:
https://github.com/bradautomates/claude-video
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/6770" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#Android
#Gaming
🎮
MuMuPlayer 6.0 منتشر شد
نسخه جدید شبیه‌ساز اندروید MuMuPlayer با تمرکز بر عملکرد بهتر و سازگاری بیشتر برای اجرای بازی‌های اندرویدی عرضه شد.
ویژگی‌های جدید:
•
🤖
پشتیبانی هم‌زمان از Android 12 و Android 15
•
🚀
عملکرد روان‌تر و FPS بالاتر
•
🖥
بهبود اجرای چندین Instance
•
🎯
سازگاری بیشتر با بازی‌های جدید
•
⚡
ارتقا بدون از دست رفتن تنظیمات و Macroها
مناسب برای اجرای بازی‌هایی مانند Roblox، استفاده از چند حساب کاربری و تست برنامه‌ها روی نسخه‌های مختلف اندروید.
🔗
https://www.mumuplayer.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/6769" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHTKsOKLxm88u_2Gsgg8StGLV7S9ImLThZOmtTXm8jZN6r-DeQHcACBn1GzWZBhyDBe3QvGTA4pg7VA67ltQv4dLo-BbLz3XpeFINJdqUz23WmwvafjDrFuDSSc6BoHxNemdu9hsGcYQ66quAjsdgtWBMw18UPNfGF1QGkGVlb7uE_MlhkpdI56_UfN0JI2Owt_EdBlpqZQD6DvD9m3Rc0SZibo2zOsSvo1hRss4Vf_HuP5yrXR-CatZ0enW7nghLLpQifHAgD1auN_UQU5yrfYwSevoD89fk-w0z1pRmpe-o3Yo1yoiBy84DT72KN-h3uq9p3maGsm4QfFCt1sC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
یادگیری شخصی با هوش مصنوعی
موضوع رو بهش بده؛ بر اساس سطح و درک شما آموزش می‌سازه.
✅
آموزش مرحله‌به‌مرحله
✅
امکان پرسیدن سؤال حین آموزش
✅
مناسب هر سطحی
🔗
https://peras.app/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6768" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏
🎁
100 هزار توکن رایگان ( 3 روزه )
‏دسترسی به مدل‌های زیر و صدها مدل دیگر برای کدنویسی :
🔹
‌GLM-5.2⁩
🔹
‌Qwythos⁩
🔹
‌Deepseek 4 pro⁩
🔹
‌Kimi k2.7⁩
🔹
‌Minimax M3⁩
🔹
‌Mimo 2.5⁩
‏
💡
ویژگی خاص:
امکان استفاده از مدل‌های ترکیبی ساخته‌شده توسط کاربران (مثل ترکیب ‌Qwen + Fable)⁩
🔗
‌featherless.ai
⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6767" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEJhivST6lUTD7xuWQWAx3v65PiepMjTANXNS_JN7dVOpvB3OMkZ60ddbWpHDSxPDyc0n9inXGhe0Lcsyoslx3uC0UN-DvI-OdhiVNqw8s-xE9z7mJ0SJoz7h3jJOqo24XbXsgnme_2jW8_GM6Ga0teu6hTTN7rDcgtyRKygEtq96FPbLhAPCmazPcqcr38OIXoXJa31fsF817FaUgoBMRl6PY-3m0mfhJkUmIluGN1G7zfbYoOxPBbnAsVhSwRn-OotCFCSX5xzVBycNg0zPh2f2sgfCw5d954U3psoBDHOnyTO0INCuN9cTZXvb3PdckGhepMPu9mu940JV4w4lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
PixelRAG
یک پروژه متن‌باز برای Visual RAG که به‌جای متن، اسناد، صفحات وب و PDFها را به اسکرین‌شات تبدیل می‌کند و جستجو را بر اساس محتوای بصری انجام می‌دهد؛ بنابراین جدول‌ها، نمودارها و چیدمان صفحه حفظ می‌شوند.
ویژگی‌ها:
•
🖼
جستجوی مبتنی بر تصویر صفحات
•
📄
پشتیبانی از وب، PDF و تصاویر
•
🤖
سازگار با مدل‌های چندوجهی (Vision)
•
⚡
ابزار CLI برای ساخت و جستجوی ایندکس
•
🌍
API و نسخه دمو آماده استفاده
🔗
https://github.com/StarTrail-org/PixelRAG
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6765" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔐
VoidAuth
یک سرویس متن‌باز برای
SSO
و مدیریت کاربران در محیط‌های Self-Hosted.
ویژگی‌ها:
•
🌐
OIDC Provider
•
📖
LDAP Server
•
👥
مدیریت کاربران و گروه‌ها
•
🔑
MFA
و
Passkeys
•
📨
دعوت و ثبت‌نام کاربران
•
🎨
شخصی‌سازی رابط کاربری
•
🔒
رمزنگاری داده‌ها (
PostgreSQL
/
SQLite
)
⚠️
هنوز Audit امنیتی نشده؛ برای Production با بررسی کافی استفاده کنید.
🔗
https://github.com/voidauth/voidauth
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6764" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🖼
جستجوی معکوس تصویر با TinEye
اگر می‌خواهید منبع اصلی یک تصویر را پیدا کنید، نسخه‌های باکیفیت‌تر آن را ببینید یا وب‌سایت‌هایی که از آن استفاده کرده‌اند را پیدا کنید،
TinEye
یکی از بهترین موتورهای جستجوی معکوس تصویر است.
⚡️
قابلیت‌ها:
-
🔍
جستجو با آپلود تصویر یا وارد کردن لینک آن
-
🌐
پیدا کردن صفحات وبی که تصویر در آن‌ها منتشر شده است
-
🖼
شناسایی نسخه‌های ویرایش‌شده، برش‌خورده یا تغییر اندازه‌یافته
-
📈
مرتب‌سازی نتایج بر اساس اولین انتشار، جدیدترین، بزرگ‌ترین یا بیشترین تغییر
-
🔒
حفظ حریم خصوصی؛ تصاویر آپلودشده ذخیره یا ایندکس نمی‌شوند. TTinEye+1
🔗
وب‌سایت:
https://tineye.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6763" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6762">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDNU0-PGtXej6hiX_-cPeIWYsHPAbjhJX9p2AEebaXR-CraXUoGeQ5MZEWGRv6a7TQBG3uaacDCsxOSkFgPtXwT4I3A8Nuj5cZbYR_e99jjZT1LaXOJb4sSV-fMPmjNDmlNLeZD0G5NbG4Bmr3pqnNc2DTkl7OLD58bwS0WYtg7Cf61smz44pgEEjjVznzOcHpm7QmLoF3ZpZf7zwxZU3GtrXb3ZhA4XuKzHZYN5bTlca9S7YyhV-C6uG79rtkvmIRFTzyRMFhHTXtG0V5Neg-iAV4c3JdX-DZdLNycA1TBZWaibcR8tU8Z_QaBa8m239493fT5NraUzm9PH9DinJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تولید صدا با Pocket TTS روی پردازنده معمولی (CPU)
این ابزار یک مدل
تبدیل متن به گفتار (TTS)
بسیار سبک با
۱۰۰ میلیون پارامتر
است که بدون نیاز به
GPU
، پرداخت هزینه
API
یا وابستگی به سرویس‌های ابری اجرا می‌شود.
⚡️
ویژگی‌های کلیدی:
-
🚀
تولید اولین بخش صدا در حدود
۲۰۰ میلی‌ثانیه
و تا
۶ برابر سریع‌تر از زمان واقعی
روی پردازنده‌های مک.
-
🎙
امکان
شبیه‌سازی صدا (Voice Cloning)
تنها با یک نمونه صدای
۵ ثانیه‌ای
.
-
🌍
پشتیبانی پیش‌فرض از
۶ زبان
: انگلیسی، فرانسوی، آلمانی، پرتغالی، ایتالیایی و اسپانیایی.
-
🔓
کاملاً
متن‌باز (Open Source)
با
لایسنس MIT
و آموزش‌دیده فقط با داده‌های عمومی.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6762" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvVLXk8jUdlHgTZ7Xi6Z5lMIxcwMACmAAvy7MiExsBvZbLT3bJPW41AhYNGyWX5yhg2Jb75eLfcrCYHTJecF1GH4enHCe_oJa_3CJT5Xqn6wqYsUZUFoPTzcpl3-pi9ycLsn0GaI7sr-K8e76zkJqKtO_z6lfKuxj2ekN_rpunylpVIjIXfjvGYZ21Etx5oNzlptS_EBnJjJZgYvBoNMoo1rgnfV32IKXEPIlx0ljDmZ89XvtY177KTx4C0QMAZrgNeWIbiBce3adfMBNaS6982tUJmXDRi6d5tDCSiqCnhAdaMhKtgIYpCuzemip6b1iooKENn_qmngY0tSS917qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به دنیای تکنولوژی، لینوکس، شبکه، سرور و ابزارای خفن علاقه‌مندین، یه سر به کانال لوکال هاست بزنین
توی localhost کلی آموزش، نکته کاربردی و تجربه واقعی از کار با سیستم‌ها هست. خلاصه هر چی از دل پروژه‌ها درمیاد، باهاتون به اشتراک می‌ذاره!
🅰
t.me/localhost_ir</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6761" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ7wP_G8oFGHRzKj0lcvnT1bgqsmGvFlVnrWe505cn3YrH1dNQ6k6yQTbXkmDPElAb5VSHkOhLlqrBFOQicgk670x7iN3cLbeUJ17W9tAys85t5yAy_NTtBEO_H5YR52pW6cnkcNfAfuGHSygFR7svn1feW7n2sC1vJo_aTmmfWHTpqnweflzdfVNz8mkBM4ZFv_VWtGiV76re8aKLiw1mTB4WI3iuWGxeeUmr8ARI6wMXNzyI9zvurVp4hytQJqLAI6_OrC1GZkGsdbrgPcjzqSGsalDc6kmo_Pw3tipYZ3Vgk-gWA4S1SzxggX6TCw73tu7fB_6SXzCYy32T47Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود و مدیریت فایل‌های تلگرام با TDL
یک ابزار متن‌باز و قدرتمند برای دانلود و مدیریت محتوای تلگرام است که امکاناتی فراتر از یک دانلودر ساده ارائه می‌دهد. این برنامه با مصرف کم منابع، سرعت بالا و قابلیت اجرای مستقل، گزینه‌ای مناسب برای کاربران حرفه‌ای تلگرام محسوب می‌شود.
⚡️
ویژگی‌های کلیدی:
📦
اجرای برنامه به‌صورت تک‌فایل (بدون نیاز به نصب)
-
🚀
مصرف بسیار کم منابع سیستم و استفاده حداکثری از پهنای باند
-
⚡️
سرعت دانلود بالاتر از کلاینت رسمی تلگرام
-
🔒
دانلود فایل‌ها از چت‌های محافظت‌شده (Protected Chats)
-
🔄
فوروارد پیام‌ها با مسیریابی هوشمند و جایگزینی خودکار در صورت خطا
-
⬆️
امکان آپلود فایل به تلگرام
-
📄
خروجی گرفتن از پیام‌ها، اعضا و مشترکین در قالب JSON
-
🌐
متن‌باز با لایسنس AGPL-3.0
🔗
گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6760" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRUmnFaUijHvQmDG1fa9lD0lx7QELIPMhEgTCjySi5Z4UdaelxaNG-PuTfi2oXU6QU76LauW5JRhJ1AF_28dsr-u-u2Y7CwYxXab1P578nOeBlWdPKOQYruoZR8DV6Nnnae3F_DfL7AZQIz9yd_2njjsJB_W6uWzcvUNwb-mlatA8Q6QtDnwTWyl-TyNk7V-Kyxcnu3vAFVWuiKYCMl2-onbEazPll1lzIGVorXp5lVEAuGJNfqITHw0d7YuU3m8ThkQxys1WoeLs_aHFaobFxYyBjO3BKCq3TDc2R51U8hDhwJR54Zg3JwI8X_ftWzKiNoXJtht-d1uQK-vR1BVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهبود کیفیت عکس‌ها تا رزولوشن 4K با استفاده از ChatGPT
عکس شما را بهبود می بخشد و جزئیات را تا حد امکان حفظ میکند.
😮
پرامپت :
Restore and enhance an old damaged photo. Remove scratches, stains, and noise. Reconstruct faded or torn areas while preserving original details. Slightly sharpen the image for better clarity, but keep it realistic. Apply natural and era-appropriate colors to skin, hair, and clothing. Use a soft, balanced background color without being too striking. The final result should look like an old photo that has been realistically restored and colorized, while respecting its original appearance.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6759" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tY2zWK-RNkKn_YuleG8_qaJmsF9l8je_sv2WCykOtr28GXzkOu9-J5blGSdLE12-Rhwm8XDrnj8CagtMMd4TvSwgk16mrapTsooWfUPVpa_ksx-RmR4byznP_ZBRPXOqELNE1s9JR0PPIUMl1MLtatT9d8HOVe2kJ5t4FX98iVYo_vLj-i5rzSa-3apJvNDI_JM_cHuPB-MaYKH5wVs-IbW9ppvdLfotk_Us8wvsh8YlpfSCgGg8s-ssRS1NM04WUgKQ6iHtT2XxDotFY67UKbCZSfMo_qC4NxIqDIVvhOjSqMfLHEOm-zNIGeXoFTQkT2UBnXijJyJ80G2t4RPkLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اپ‌استور متن‌باز و جایگزین Appteka برای اندروید
یک مارکت رایگان برای دانلود، مدیریت و به اشتراک‌گذاری برنامه‌های اندرویدی که بر پایه مشارکت کاربران (Community-driven) فعالیت می‌کند.
🔥
ویژگی‌های مهم:
*
📦
استخراج APK:
خروجی گرفتن از برنامه‌های نصب‌شده (حتی برنامه‌های سیستمی) بدون نیاز به روت (Root).
*
💾
مدیریت فایل‌ها:
قابلیت بکاپ‌گیری، بازیابی و نصب مستقیم اپلیکیشن‌ها از داخل خود استور.
*
💬
تعامل کاربری:
دارای چت گروهی، سیستم نقد و بررسی، لیست علاقه‌مندی‌ها و دریافت نوتیفیکیشن آپدیت‌ها.
*
🔒
امنیت:
اسکن خودکار برنامه‌های آپلود شده (از آنجا که محتوا توسط کاربران قرار می‌گیرد، بررسی منبع قبل از نصب پیشنهاد می‌شود).
*مناسب برای توسعه‌دهندگانی که می‌خواهند برنامه‌هایشان را راحت منتشر کنند یا کاربرانی که به دنبال یک استور بدون محدودیت و ابزاری برای استخراج APK هستند.*
🔗
[لینک دانلود یا گیت‌هاب پروژه
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6757" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675041278d.mp4?token=VJR32iDjesjAp5vFIzHokrG-Bhzy8BIQ-uYZT_JHby32A4TVq63wsZ2ihyvZ9X0w81hJNMouwDsc0rGTZAcvlNOQrUtufemnv1r3c8RCVAIzDoeVls9i9dgGI7rbhcBVJSc-KNBG-7Jjv_1nQbbEKKudLPp_HmZuSk00SmlhwYkJOOCgQsR80fvhW-Pe_BCd5JH_Vjm7zEKP-hl5h_d-X84farvGPNlWoXoA5e15VPI5haMuVdhqfjSQkPLjRKMbYXsZEum0Rle0fMpgHpls-C_N5wFhFkqdH83Q8LuirxoQPZtwaCILJt3OFTnVTCPRQ_yW-oqEz93KLSy9lk1qag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675041278d.mp4?token=VJR32iDjesjAp5vFIzHokrG-Bhzy8BIQ-uYZT_JHby32A4TVq63wsZ2ihyvZ9X0w81hJNMouwDsc0rGTZAcvlNOQrUtufemnv1r3c8RCVAIzDoeVls9i9dgGI7rbhcBVJSc-KNBG-7Jjv_1nQbbEKKudLPp_HmZuSk00SmlhwYkJOOCgQsR80fvhW-Pe_BCd5JH_Vjm7zEKP-hl5h_d-X84farvGPNlWoXoA5e15VPI5haMuVdhqfjSQkPLjRKMbYXsZEum0Rle0fMpgHpls-C_N5wFhFkqdH83Q8LuirxoQPZtwaCILJt3OFTnVTCPRQ_yW-oqEz93KLSy9lk1qag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6756" target="_blank">📅 10:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📱
تست خودکار رابط کاربری و اپلیکیشن‌ها با Maestro
یک فریم‌ورک متن‌باز فوق‌العاده برای تست End-to-End (E2E) در اندروید، iOS و وب. با این ابزار نیازی به کدهای پیچیده تست (مثل Appium یا Selenium) ندارید و سناریوها رو خیلی راحت با فرمت ساده و خوانای YAML می‌نویسید.
🔥
ویژگی‌های مهم:
*
📱
کراس‌پلتفرم:
پشتیبانی از برنامه‌های Native، فلاتر و React Native.
*
⚡️
اجرای هوشمند:
بدون نیاز به کامپایل فایل‌ها، همراه با سیستم کنترل تاخیر (Smart Waiting) برای جلوگیری از خطای لود نشدن المان‌ها.
*
🖥
ابزار بصری:
دارای یک محیط رایگان (Maestro Studio) برای ساخت و رکورد تست‌ها به صورت ویژوال و بدون نیاز به ترمینال.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6755" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
۳۰ سایت رایگان ساخت ویدیو با هوش مصنوعی
#اختصاصی
اگر دنبال
Veo 3، Sora 2، Kling
و سایر مدل‌های ساخت ویدیو هستید، این لیست را از دست ندهید.
⭐️
بهترین‌ها
VeoAIFree
→
https://veoaifree.com
(بدون ثبت‌نام و واترمارک)
Vixdo
→
https://vixdo.art
(۱۷۰ اعتبار رایگان + بدون ثبت‌نام)
Pollo AI
→
https://pollo.ai/m/google-veo-3
(چندین مدل در یک پلتفرم)
GlobalGPT
→
https://www.glbgpt.com
(Veo، Sora، Kling و Wan)
Leonardo AI
→
https://leonardo.ai
(اعتبار رایگان هفتگی)
🎁
بدون ثبت‌نام
VeoAIFree • TryVeo3 • AIVideoGenerator • Veo3Free • Videomaker
💰
اعتبار رایگان روزانه
VeoE • EaseMate •
Veo3.us
• AIEase • Aitubo • Pixnova • SeaArt
🧩
پلتفرم‌های چندمدلی
Veo3AI • Pollo AI • GlobalGPT •
Media.io
• Novi AI
🎬
ابزارهای تخصصی
Digen
→ Lip Sync
MindVideo
→ انتخاب نسبت تصویر
DomoAI
→ تبدیل تصویر به ویدیو
Klap
→ تبدیل ویدیوهای بلند به Shorts و Reels
Fal.ai
و
Eachlabs
→ مناسب توسعه‌دهندگان
💾
این پست را ذخیره کنید؛ احتمالاً بخشی از این سرویس‌ها در آینده پولی یا محدود خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6754" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGCaYTjdb09dlwdAdmRNlC06EJqVoIdxGKxCMXvWUcIqAyxlLy3DB58_wXBC-C02qvjyC8wnBYmXyuVEonjw0xQaDc4xt4obK8GOGfyF9U5K3QeeVnNPefpEI_HpOnk3cUJtNLmGfRIW1uXERaAiVnOpDHq3sNGTZsz7i3ZgPqtP23h_STRu6cfw9R3Bjv7N5HtiRsc7kTGKzJDAPKD1HN17e6e47De9yzkvXoX_pQ2mPlVuUM2GHQ99rXrRbt3ui_nwgVuMVpWIOnhJbCTTaSc9U6cnoo59LYLGp38bcGvimqYDyA5M2SYEg3j7p7qqZzjo-grst3wwzyaSE43gNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بقول نیچه
در چنین گفت زرتشت
«من از خردِ خویش به جان آمده‌ام، چون زنبوری که انگبین [عسل] بسیار گرد آورده باشد. نیازمندِ دست‌هایی هستم که به سویم دراز شوند. می‌خواهم ارزانی دارم و بخش کنم...»
بیاین مثه نیچه باشین و این عسل و انگبین چنل رو به سوی دستان دراز بسپارید
نیاز داریم به حمایت شما
❤️‍🔥
https://t.me/ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6752" target="_blank">📅 01:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6751" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor
لینک ویدیو آموزش:
https://youtu.be/pN3LxWzDtKI
خود پروژه:
https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6750" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نیاز داری سورس کد کامل یه سایت (به همراه تمام فایل‌ها، تصاویر و CSS) رو یکجا برای استفاده آفلاین دانلود کنی؟
💾
🕸
ابزار اوپن‌سورس Website-Downloader با استفاده از قدرت wget کل سایت رو میرور (Mirror) می‌کنه و یک فایل فشرده بهت تحویل میده.
🧵
👇
#توسعه_وب
#اوپن_سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6749" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mspOViQFo5LhAE0HxGLCowbfvtUYNj4hmAad6SHNqMc91K9eBkJNtQnPfVzTsZMQjO9Y5747Wg9-_HSFgEHQiEKXMhJhVQgQEiKP-RS0lvfr6DR9Vf4qI_CJ3GVd5bbsi-0yss8_GoHRaLRN3sm1SrcAHDBV0D1w6em9_gWlI1Hg6CSjRgUXO6Nqav9njhxz5uRzMuJl_RjER2O07wexEdqnANjdz39aSmSSWXNX36b2HJzLC6X241NfLlGZJflW9KL24gxufefI-gJ60g3xCNRXgcsW5gdPgMBGSvCvgc6DLnG4qLTUAcoD5WuAlqla6WQnAJc5Nav8hS8GIoYsLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074191361432035554</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6748" target="_blank">📅 21:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPdNhQAtrqMi-pmSFlKZibTA1LV-V2sF9iquPRqA7hDvovaCS4dSQ_fl-A-HzUWAnUeKSKgjf-nKJq-Fnd4tjekCq8YCCjrQXshFJB1frZBvO4gOV8wvrU73RbfJwR9C3iBjeWhJvcdTPnDIgXEiZAdjWVX1mSDkpx85yETMPPIw0aH5plLtEbrFtd2M_LTPanoyJMQFTa09XPRF_BVYXyNL9CsLKBSZW9lGj6DJ9UW3JOnWne6Wzq6kd_3pZtm7Bv57iVOKQy_GMvNNgBdGGVFI8sTYw59hj5Vw9m73txaolWeX6a0ZwxnGnlOh8wkAH4PJqQ9MBBNEn_Yyr4Cd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🗣️
هوش مصنوعی‌ها دارن با هم «زبان راز» می‌سازن!
🤫
🤖
‏تا حالا فکر کردی اگه ‌AI⁩ها یه زبانی داشته باشن که ما متوجهش نشیم، چی میشه؟
🤔
‏پروژه جدید
‌GLOSSOPETRAE⁩
دقیقاً همین کار رو انجام میده:
🔹
تولید خودکار زبان‌های مصنوعی (از آواشناسی تا دستور زبان)
‏
🔹
ارتباطات غیرقابل‌فهم برای انسان
‏
🔹
کدنویسی خالص با جاوااسکریپت (بدون وابستگی خارجی)
🚫
📦
‏این فقط یه ابزار نیست؛ یه پنجره به دنیای ارتباطات پنهان ماشین‌هاست.
🔍
🧠
‏
🔗
لینک پروژه:
github.com/elder-plinius/GLOSSOPETRAE
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6747" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juKFnaGbQ2wwokQM7u2CKVTbWrbOAhagTq7dXXxH1bToMk3lrKXxTvVIDXC4BGgxPfmIIiSoUUbY1idNSUoAA6k-W_ictuYk7G2nTnOj2e2YXSV_b5ctF_mgtW_HUOfTHEe_KCiKnIgnTXleTNQUdfgEoDJ8Xz6g39ZlNTWIIvN7mXyVkmmZIY9e7h15PUHydLwmCPFpeMtLrzNu6BP9h0eB2KdpWC0uwq0XB600hDrdnnTOV_GzX79X31tTxE__W0cKOt35EcnF8dgIW9QPpSGIxsRL2egpCs8N5zCXKY9vH61GD_jE4poneAmnjGFn677kM3SQJ9IwCuL-0PitpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆓
دسترسی رایگان به غول‌های هوش مصنوعی!
🤖
‏‌یه گنجینه از ‌API⁩های رایگان روی ‌GitHub⁩
💎
🔹
مدل‌های قدرتمند: ‌Gemini Flash⁩، ‌Qwen3⁩، ‌DeepSeek⁩ و ‌gpt-oss⁩
‏
🔹
سرویس‌های متنوع: ‌Google AI Studio⁩، ‌OpenRouter⁩، ‌Cloudflare⁩ و ‌GitHub Models⁩
‏
🔹
یکپارچه‌سازی آسان: اتصال راحت به ‌Cursor⁩ برای کدنویسی سریع‌تر
🚀
‏فقط یادت باشه محدودیت تعداد درخواست (‌Rate Limit)⁩ رو رعایت کنی تا سرویس‌ها قطع نشن.
⚠️
⏳
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6746" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4AaLp8cXKizcQz7KvHtn9zxbbrT9Oo7QsO7H9Q8Z0j0Y9gUpMsoMIAMSs_BtsCrc2tpP0LK3Hz1_BFkOH2siYdQy_IIHuuN2sEibHEonA4eNp2US3tNnjnAzT5Fq8RzduWD-m01yfdqbbvn6T2_JhT6RT6jq2cU0KGPB-Q-XzJfUkCFMAUSEfYuDyVrFSQ7REo947B-xekedyGutpJuGJrlOhbY2hZ3xzG09Fhy6I0wJkGPMHBiWGRB6zWNpDkG1BBS_B_Hyq_Smnr5Cr6jUEh1OTt4fQ9zHWmgs14tRbjG9QsvPZqEGBtbkzgrVq6SJ9uybiUQG_HwIUPvcD_z5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
حذف پس‌زمینه با یک کلیک!
🖱️
‏این ابزار وب پس‌زمینه عکس‌ها رو با دقت بالا جدا می‌کنه و کیفیت اصلی رو حفظ می‌کنه.
✅
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=irV56t_1kik6SS-BshMH5uQsNb3UqgquUlQUtNswtDa4eAO6mxJtgQ5kF4iI4EfOA3utul1ajLGouFvzrb8oz54HHdXMViKgkJcEIehiNHiesfDd9EhZBUj022QiX7FUz6CtSwQuOqW7Tfu-Z95mU1RRS3gYpEUs5JpBuN051EYShezKYRZCkcsfN3-UN5nzk6RGZsmoKKES4_fY_ztgJxheezKZrD0gM0Z-JKieEAN4sryd2bhoUPZQCRf5aP57ekqGSsH0nEJsvdR6G9armRs3xDvNQrjCHB1JtivKIAzzsuoa4hAtNVbVvrGpKbVnfjYFMSqkIgoa_3QxPXNbDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=irV56t_1kik6SS-BshMH5uQsNb3UqgquUlQUtNswtDa4eAO6mxJtgQ5kF4iI4EfOA3utul1ajLGouFvzrb8oz54HHdXMViKgkJcEIehiNHiesfDd9EhZBUj022QiX7FUz6CtSwQuOqW7Tfu-Z95mU1RRS3gYpEUs5JpBuN051EYShezKYRZCkcsfN3-UN5nzk6RGZsmoKKES4_fY_ztgJxheezKZrD0gM0Z-JKieEAN4sryd2bhoUPZQCRf5aP57ekqGSsH0nEJsvdR6G9armRs3xDvNQrjCHB1JtivKIAzzsuoa4hAtNVbVvrGpKbVnfjYFMSqkIgoa_3QxPXNbDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
کالکشن ۱۷۰ ابزار کاربردی و متن‌باز
تمام این ابزارها تحت وب هستند و نیازی به دانلود فایل یا ساخت اکانت ندارند:
🎬
مدیا: ویرایش حرفه‌ای ویدیو و صدا
🖼
تصویر: فشرده‌سازی، تغییر سایز و افکت
🔄
مبدل‌ها: تغییر سریع فرمت فایل‌ها
📄
اسناد: ادغام، جداسازی و ویرایش PDF
📰
داده: پارسرها و پنل‌های مانیتورینگ
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPqQ5d-QIHcCjETulmmjB6-6pq26_ddvEviV_Bih2LBbRH8PdPp7WLwJQdYeKzeRpuJDoU0VRWduZt729vDCacwtk416KqAG1sCutpjbbxkEdcvdOz7NYO4a332Am_7Cvm-X-fzvTwivB4QtiAu98jFEIZZMrdOBxFi4GA-zPr9P7uyoNAVHD_L4YchhGiSftNkgxYX0C27D4EH_FRcIynqESexTvJrR0nx2emQSeEwPFyIaZxeNH2TCAaMQAQ8DvGk3h-JzrmunPWrGG7_2_ETtzP7UURIaDFAvqLu8p0ud4RROAlTNWfSSWHU8GvU3jqcUaqeHDn9n5mRZqysfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهکارهای اتصال پایدار و پرسرعت برای اینترنت آزاد
🔹
پشتیبانی از V2RayNG، WireGuard، SlipNet و ArgoVPN
🔹
ارائه اشتراک‌های عادی و گیمینگ متناسب با نیاز کاربران
🔹
انتشار کانفیگ‌های رایگان، آموزش و پشتیبانی
🔹
تست کیفیت اتصال قبل از استفاده
📢
TirexNet؛ همراه شما برای دسترسی بهتر به اینترنت
🤖
Bot:
@TirexNetBot
💬
Support:
@HRMP1386</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
🚀
دسترسی رایگان به غول‌های هوش مصنوعی!
‏اگر دنبال جایگزینی برای ‌Agent Router⁩ هستید،
سایت ‌
Bluesminds⁩
فوق‌العاده است. با ثبت‌نام، 100 دلار اعتبار اولیه هدیه بگیرید و با مدل‌های قدرتمندی مثل:
🔹
‌GLM 5.2
🔹
‌Qwen 3.6
🔹
‌Minimax M2.7⁩
🔹
‌Mimo 2.5
‏کار کنید. همین حالا امتحانش کنید و پروژه‌هاتون رو به سطح جدیدی ببرید!
✨
🔗
Docs
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6740" target="_blank">📅 12:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون فضولی میکنه. یکی میفروشه به دلال های داده (مثه گوگل و مایکروسافت و...) یسریا هم که حریم خصوصی محورن.
الان هرمس اینا رو واقعا نمیدونم. هر چی بیشتر این مدلا رو بیشتر وارد چیزاتون میکنین، ریسکش بالاتر میره در کل. باز این شرکتا اروپایی نظارت بالاتر هست ولی نمیدونم طرف خوشش میاد از ی مدل میگه به به چ مدلی چقد قابلیت بذارم چنل، ملت کلی ویو میزنن استفاده میکنن. طرف به تلگرامش و... هم وصل میکنه بعد اخر بعد چند روز میگه ببخشید هرمس رو شخصی ران نزنید
اینو میخواستم چند روز پیش بذارم ولی گفتم ولش. ولی حس کردم بهتره بگم تا پیشگیری بشه بهرحال</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6739" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkTvA_1KTc9YhwKq0yL7gAFTtl1s5YLGVO3uJ031LwS9_KLh9ey-5nQNTJ_tefFqIaBRIHQmuDH0w9MITphn_ZQCvhOHkKtCipSPcHH4Bhx4G7xin_zF-q_oWVjIAXEq5AObEAGGPOGSHKenNTwI15AiTWSyCpM9X6NghtB7Mw9tmga7vvDWY-uGKKRn7IRZUbkVbW3XDMimNWQ7AqKjmOZgxH49JMNCiWPY0N0VNxa_JKBP5qEYffnpQ4ClcenqRSB86PODbOY-zjQHgyjmf9NxwK_2kSsqHyjKfm9drLW4n_pJe10CwdkDtfxjeTqIcP6ou5WXLKlkjA5JwV4C4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074039784629014892?s=20</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6738" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VloXVdV5iguQXXXitpN5hIiBXm2FWciW_yYywMCHc3uBo8JIBBewzHCkI9e4aXsXSV_Nxl2PQzJiS8QX4n786EgKv0eIxE8KEbfBekAriFIjNV8yj4CYiEO1Y10vVSgMPyUd9SPj-Z-htlHosUBxTctjzyR8ZzGCLtTIcJpPRJo6ehB7P5PfYu30M4MTaGACWWPxZ9w2eOWBzwIuFxwaKf3eVw6UZEh68xG_ZEj9pkd86aYX_SwOgCU5VkUv3LOEn7PwW0n48aulRVI-vO7KvHlrug7eN8zrPp7pGZ0ZnU4Nuc2RDv_0kg1nzgQ4K-z8a2HlaKAJ7ayR0VBD1I105Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
اجرای هر بازی اندرویدی مستقیماً روی کامپیوتر
یک شبیه‌ساز رسمی از گوگل که واقعاً سریع است و به راحتی از رقبا پیشی می‌گیرد.
🔹
پشتیبانی کامل از اندروید 14، از همان ابتدا.
🔹
عملکرد از طریق Hyper-V — همه چیز پایدار و سریع است.
🔹
هر فایل APK را بدون هیچ مشکلی اجرا می‌کند.
🔹
بدون هیچ بنری یا تبلیغ مزاحم.
🔹
بازی‌ها بدون هیچ‌گونه کندی یا تأخیر اجرا می‌شوند.
دستورالعمل به زبان فارسی
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6737" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8hYRckCbQCQ5FZc8lR0FF06oP06EiTmZq-3NjIsgbD85NpisB-29-pjqylO6ExIi0x-MNaggl2ClYrl6o8vOkVdc7Xc7wkgiKWqcg2o1WUS03U2IlO256jiFbIetyc6HiopSqXSRv5wGxNIFAL0OzqgAeu4Ju40fTHl5T6w_FcQdtT9Eu3UwXEeS6Np4hNFqMivYEump4hSHfWXIP0ILa6vjy2rRKXzOmNoYW5Wi2KCYa_gJSx6M3jAnobf0RVJMhRjpibU-NAxjcImu_74eikfMIPjZTt6fdt7fUSVB5Ochif6rRurDXUDGozsUZ8l_1okdAcimb-vb-W40ek-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
کپ‌کات رو فراموش کنید؛ این ابزار رایگان و بدون نیاز به نصب جادو می‌کند!
‏اگر برای ادیت ویدیوهای خود به دنبال یک ابزار سبک، همه‌فن‌حریف و کاملاً رایگان هستید، پروژه متن‌باز ‌OpenReel⁩ دقیقاً همان چیزی است که نیاز دارید. این ادیتور قدرتمند مستقیماً درون مرورگر شما اجرا می‌شود و نیازی به نصب هیچ برنامه‌ای ندارد.
‏
💡
چرا ‌OpenReel⁩ یک جایگزین بی‌نظیر است؟
‏
🔹
ادیت چند لایه حرفه‌ای: قابلیت ویرایش همزمان چندین لایه ویدیو و صدا همراه با پیش‌نمایش زنده و بدون افت سرعت.
‏
🔹
امکانات کامل کپ‌کات: دسترسی به افکت‌های متنوع، ترنزیشن‌ها، پرده سبز (‌Chroma Key)⁩، کنترل سرعت و فریم‌های کلیدی (‌Keyframes)⁩.
‏
🔹
ابزارهای جانبی کاربردی: قابلیت ضبط صفحه نمایش، کار با متن و زیرنویس، و خروجی گرفتن سریع با فرمت‌های ‌MP4⁩ و ‌WebM⁩.
‏
🔹
کاملاً رایگان و امن: بدون نیاز به ثبت‌نام‌های پیچیده، پرداخت درون‌برنامه‌ای یا واترمارک روی ویدیوها.
‏بدون درگیر کردن حافظه سیستم یا گوشی، همین حالا ادیت ویدیوهای خود را در سطح حرفه‌ای شروع کنید!
🔗
Site
|
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6736" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6735">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhunjeUfCH952HWlK6Bfop64eUJvsqe-GM85R6ipJWuHpQEVtiHa1nB9mGeA1YGnUh894wfAZSfBHNvETJT9G7P_URGRLyKflyCM8vuPPNPB1FBuXJ_E_AppDPzbOGuEUaemvQimlXn-JUxPNMw6_tXdK2igff3NxOvUwVt5jW_7cmzntVfhHg79PFNyw7ZHKqI7rGCDDqh8EjWHdt5oNuNO00idKvTuYINk9RGHMnYepIne2Ubw_Ce--W7VjLwGdGmIgZY2E4kbkDZyi7MdYqm0it4-cWE0oNttRg8qbZmMxV6dVV_XyilKEQxaHTM0wNU8vXi6nkaVvUrA8PvfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تمام غول‌های هوش مصنوعی دنیا، زیر یک سقف!
‏دیگه نیازی نیست برای تولید متن، کد، ویدیو یا عکس، بین ده تا سایت مختلف چرخ بزنی و کلی اکانت پولی بخری. این پلتفرم همه‌چیز رو برات یک‌جا جمع کرده!
‏
✨
چرا این ابزار بازی رو عوض می‌کنه؟
🔹
تیم رویایی در یک پنجره:
به راحتی و با یک کلیک بین قوی‌ترین مدل‌های دنیا یعنی ‌ChatGPT⁩، ‌Claude⁩، ‌Gemini⁩، ‌Grok⁩ و ‌Kimi⁩ جابجا شو.
‏
🔹
تولید همه‌جانبه:
از نوشتن کدهای پیچیده و متن‌های خلاقانه تا خلق تصاویر و ویدیوهای جذاب، همه در یک محیط واحد.
‏
🔹
سهمیه رایگان روزانه:
هر روز کلی توکن رایگان بگیر و پروژه‌هات رو جلو ببر.
https://www.easemate.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6735" target="_blank">📅 10:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6734">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVLbXAKpwwtAJvLcU9rUuTZ9Pn6TjtpqQ5-F_w5xsK_edE4HcX6WCpW2wZIksLIYZhgB9JjX3aWtge0TZ4CqBq3FUhWVUpeyqsusai3-bdrfL27Uu5FxiLKC9qVtH_RLhNM-32xhiRHGbHN3-EC56iibCTTm7PTqvPiA-6AjvXiBII84tPPKX7e4OZxodQNAGCgEAYuPutltfi9bY1sn1DgkmUCmcn7LI64TbAAGa3lIYM82zxH1rYT4yXIK3bBb0W3HTFq8JwqQ4MjTemD1dW6Z_AR2dVPul7xxs9GCsOirOBVKRriCNmW_47Ry92nmA7ikXhxW_fbauK7KH2d7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
غول هوش مصنوعی، بالاخره رایگان و بی‌دردسر!
‏دیگه نیازی به خرید اکانت پرمیوم یا دردسرهای ست کردن ‌API⁩ نیست؛ از امروز می‌تونید به صورت کاملاً رایگان توی پلتفرم ‌Tabbit⁩ با شاهکار جدید ‌Anthropic⁩ یعنی Claude Sonnet 5 گفتگو کنید!
💻
✨
‏
💡
چرا این خبر بمبه؟
سونت ۵ در حال حاضر یکی از باهوش‌ترین و دقیق‌ترین مدل‌های دنیاست که حالا بدون هیچ محدودیتی در دسترستون قرار گرفته. فقط کافیه وارد سایت بشید و چت رو شروع کنید
https://tabbit.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6734" target="_blank">📅 09:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🗂
هیچ‌چیز رو دور ننداز! معرفی Karakeep؛ بهشتِ آرشیوکارها و خوره‌های اطلاعات
🧠
اگر شما هم از اون دسته‌اید که روزانه ده‌ها لینک، مقاله و ویدیو رو برای «بعداً خوندن» ذخیره می‌کنید و در نهایت بینشون گم می‌شید،
Karakeep
(با نام قبلی Hoarder) دقیقاً برای شما ساخته شده. این ابزار یک جایگزین فوق‌العاده، سلف‌هاست و متن‌باز برای برنامه‌هایی مثل Pocket هست که با جادوی هوش مصنوعی ترکیب شده!
🔥
چرا Karakeep بی‌نظیره؟
🤖
تگ‌گذاری خودکار با AI:
با استفاده از LLMها (حتی مدل‌های لوکال مثل Ollama)، محتوای شما رو بررسی کرده و به صورت خودکار تگ‌گذاری و خلاصه‌نویسی می‌کنه.
🗄
آرشیو ابدی صفحات و ویدیوها:
برای جلوگیری از حذف شدن لینک‌ها (Link rot)، کل صفحه وب رو به صورت آفلاین ذخیره می‌کنه و حتی ویدیوها رو به کمک yt-dlp دانلود و آرشیو می‌کنه!
🔎
جستجوی قدرتمند و OCR:
متن داخل عکس‌ها رو استخراج می‌کنه و می‌تونید در کل محتوای ذخیره‌شده (فول‌تکست) جستجو کنید.
📱
همه‌جا در دسترس:
دارای افزونه برای کروم، فایرفاکس و سافاری، به همراه اپلیکیشن اختصاصی برای iOS و اندروید.
🔌
تعامل با ایجنت‌ها:
کاملاً سازگار با ایجنت‌های هوش مصنوعی (مثل OpenClaw) برای مدیریت خودکار اطلاعات از طریق CLI.
اسم این برنامه از کلمه عربی «کراکيب» (Karakeeb) الهام گرفته شده؛ به معنی خرت‌و‌پرت‌هایی که شلوغ به نظر می‌رسن اما پر از ارزش و خاطره‌ان و نمیشه دور ریختشون!
🔗
لینک مخزن گیت‌هاب پروژه:
https://github.com/karakeep-app/karakeep
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝑒𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6733" target="_blank">📅 08:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.  اینطوریه که ازت آی‌پی و پس رو میگیره  بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ... خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌  دیگه نیاز نیست دستور های ترمینال رو بدونی…</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6732" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚀
آموزش نصب OpenCode و استفاده رایگان از مدل های هوش مصنوعی زیر :
🔸
Mimo 2.5
🔸
Deepseek 4 flash
🔸
Nemotron 3 Ultra
🔸
Big Pickle
🔸
North Mini Code
🔘
آموزش نصب در موبایل
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب OpenCode
npm i -g opencode-ai
4) اجرای OpenCode
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس‌ :
opencode
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر OpenCode را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
opencode
🔘
داکیومنت رسمی برای نصب در جاهای دیگر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6731" target="_blank">📅 02:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎬
تدوینگر اختصاصی شما داخل ترمینال! معرفی ابزار فوق‌العاده Video-Use
🚀
دوست دارید فقط با چت کردن با عامل‌های هوش مصنوعی (مثل Claude Code یا Codex) ویدیوهاتون رو ادیت کنید؟ پروژه اوپن‌سورس
video-use
دقیقاً همین کار رو می‌کنه. فقط کافیه ویدیوهای خام رو بریزید داخل یک پوشه و با زبان طبیعی بهش بگید چی می‌خواید تا یک فایل نهایی (
final.mp4
) ترتمیز بهتون تحویل بده
.
🔥
چرا این ابزار انقلابی و متفاوته؟
🧠
پردازش هوشمند و ارزان:
به جای اینکه کل ویدیو رو به خورد LLM بده (که به شدت گرون و پرخطاست)، فقط یک فایل متنی سبک از ترانسکریپت با تایم‌استمپ دقیق کلمات و در صورت نیاز اسکرین‌شات‌هایی از تایم‌لاین (شامل فرم تصویر و موج صدا) رو بررسی می‌کنه.
✂️
حذف اتوماتیک اضافات:
تپق‌ها، مکث‌های طولانی و کلمات اضافه رو به صورت خودکار تشخیص میده و هوشمندانه کات می‌زنه.
🎵
تدوین بی‌نقص:
روی تمام کات‌ها ۳۰ میلی‌ثانیه فید (Fade) صوتی میندازه تا هیچ‌وقت صدای پرش کات رو نشنوید.
🎨
زیرنویس و انیمیشن:
می‌تونه زیرنویس‌های کاستوم (مثلاً کلمات دوتایی بزرگ) روی ویدیو بندازه و با ابزارهایی مثل Manim ،Remotion و HyperFrames انیمیشن تولید کنه.
🤖
حلقه خودارزیابی (Self-Eval):
قبل از اینکه خروجی رو به شما نشون بده، خودش ویدیو رو بازبینی می‌کنه تا پرش‌های تصویری یا مشکلات صوتی رو پیدا و برطرف کنه.
این ابزار مثل این می‌مونه که یک کارگردان و یک تدوینگر رو همزمان داخل محیط کدنویسی خودتون داشته باشید که حتی پروژه‌ها رو ذخیره می‌کنه تا روزهای بعد بتونید ادیت رو ادامه بدید!
🔗
لینک گیت‌هاب پروژه برای نصب و راه‌اندازی
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6730" target="_blank">📅 01:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.30.8-universal.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخه جدید
#TheFeed
(v.0.30.8)
🔹
بهبود مدیریت لینک ها در برنامه، اگر توی یک پست ای دی یک کانال دیگه و یا لینک یک پست از یک کانال دیگه باشه، وقتی روش بزنید میتونید به اون کانال و پست منتقل بشید، توی قسمت فید باید اون کانال حتما توی اون کانفیگ وجود داشته باشه، توی قسمت میرور خودکار اون کانال به لیستتون اضافه میشه.
📯
من نسخه اندروید
universal
که مناسب همه‌ی گوشی های اندروید هست رو توی این کانال میزارم. ولی اگر نسخه‌های دیگه رو میخواید باید از گیتهاب و یا کانال زیر دانلود کنید (
ویندوز
،
مک
،
لینوکس
،
بی‌اس‌دی
، اندروید‌های
قدیم
و
جدید
،
ترموکس
، و حتی
نسخه ipa
آیفون) و لینک دانلود نسخه آیفون از تست‌فلایت توی کانال پین شده، البته هنوز آپدیت نشده.
📢
کانال اصلی دفید:
@networkti
📦
کانال فایل‌های باینری/نصبی دفید:
@thefeedfile
⚙
کانال کانفیگ‌های دفید:
@thefeedconfig
🔗
گیتهاب پروژه:
https://github.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6729" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
معرفی CdnScanner؛ جامع‌ترین و قدرتمندترین اسکنر IP و CDN
🚀
✨
ویژگی‌های برجسته:
* پشتیبانی کامل از ۱۷ سرویس‌دهنده (CDN): شامل Cloudflare (و WARP/Workers)، AWS CloudFront، Google Cloud، Azure، ArvanCloud، Fastly، Vercel، Akamai، Gcore و...
💪
تست فوق‌دقیق بر اساس کانفیگ شما: در این ابزار IPها فقط زمانی تأیید می‌شوند که با کانفیگ V2Ray واقعی شما (شامل SNI، Host و Path) پاسخگو باشند (پشتیبانی از TCP connect + TLS Handshake + HTTP HEAD).
🫆 اسکنر اختصاصی HTTP: امکان وارد کردن مستقیم IP، دامنه یا رنج CIDR (مانند
1.1.1.0/24
) با قابلیت بازگشایی و اسکن خودکار کل رنج.
* تولید خودکار خروجی V2Ray: ساخت بی‌درنگ لینک‌های VLESS ،VMess و Trojan از IPهای سالم با قابلیت کپی و دانلود یک‌کلیکه!
* پینگ واقعی (ICMP): عملکرد دقیق روی Windows ،Linux و macOS (همراه با سیستم جایگزین TCP در صورت مسدود بودن پینگ).
* اسکن کامل و بدون نقص: بررسی جزء‌به‌جزء تمامی IPهای یک رنج مشخص، به جای اکتفا به نمونه‌های تصادفی.
* رابط کاربری مدرن و فارسی (RTL): داشبورد حرفه‌ای و چشم‌نواز همراه با نوار پیشرفت (Progress bar)، کارت‌های آماری، پیام‌های Toast و طراحی کاملاً راست‌چین.
📥
دریافت و نصب:
همین الان می‌توانید این ابزار قدرتمند و متن‌باز را از گیت‌هاب دریافت کنید. (اگر ابزار برایتان کاربردی بود، دادن ستاره
⭐️
به پروژه در گیت‌هاب فراموش نشود!)
🔗
لینک پروژه در گیت‌هاب:
https://github.com/ScannerVpn/CdnScanner
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6728" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6727" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.
اینطوریه که ازت آی‌پی و پس رو میگیره
بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ...
خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌
دیگه نیاز نیست دستور های ترمینال رو بدونی یا حفظ کنی. تو فق به زبان فارسی بش میگی انجام میده</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6726" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">https://x.com/ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6723" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دیده‌بان لیکفا منتشر شد
🆕
افزونه‌ای برای مرورگر کروم که هنگام بازدید از وب‌سایت‌ها، اگر آن سایت سابقه نشت اطلاعات داشته باشد، به‌صورت خودکار به شما هشدار می‌دهد. متن‌باز، رایگان، کاملا محلی و بدون ارسال اطلاعات به سرور
👍
Download
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6722" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj784L_tFmoci7FqmwV8R13RUD5w6Qslnl99Tw57pvicfvKNIYFMGbcs_4igO2LJk6FN0dR8F3oZY-biTFlWJ_njNw7nok26FHRf_7DcH475_L8uWei5DKywbpRGM09fcFXwGHEiV_cOaR_K3kOMpncHV8qs2aZEO5T4n-iTtu5chDp178sdJ4mPKw551plk3BJliEe7tz06Dmj8LI5N_U6vV8jeJQiGTF7tt9HC-B6rMVRUlNGVhYu7XCS2mrrpcgcd4T-L3ll99MZfwwOmOmfpYCzBiTL2SVnlAHCITNssNXl8L_rP4wOdQNIjYAj_rb_5870hIQ7c5iq8T1AWwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
سیستم‌عامل شخصی، مستقیم توی مرورگر!
‏یک پلتفرم متن‌باز و سبک که می‌تونی روی سیستم خودت بالا بیاریش (‌Self-host)⁩ و همه‌چیز رو کاملاً آفلاین و امن مدیریت کنی.
‏
✨
چرا جذابه؟
🔒
امنیت مطلق:
داده‌ها فقط روی هارد خودت ذخیره میشن.
‏
🛠
ابزارهای کاربردی:
ویرایشگر متن، ضبط صدا و پلیر داخلی در یک تب.
‏
🚀
فوق‌العاده سبک:
بدون نیاز به سخت‌افزار قوی، فقط با یک کلیک.
‏
⚡️
راه‌اندازی:
دریافت سورس از گیت‌هاب و اجرا با داکر.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6721" target="_blank">📅 12:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🐦‍🔥
اسکنر قدرتمند سیمرغ (SIMORGH Scanner v0.3.0) منتشر شد!
🚀
اگر برای کانفیگ‌های VLESS خودتون دنبال پیدا کردن IP تمیز کلودفلر هستید، اسکنر سیمرغ یکی از بهترین ابزارهاست. به تازگی نسخه 0.3.0 اون با یه رابط کاربری وب بسیار جذاب (نئونی-رترو) منتشر شده.
🔥
ویژگی‌های خفن این نسخه:
💻
پشتیبانی از ویندوز و اندروید:
نسخه ویندوز به صورت Standalone هست و بدون نیاز به اینترنت اولیه یا نصب پایتون، به راحتی با یک کلیک اجرا میشه. نسخه اندروید (APK) هم با بک‌اند بومی Go نوشته شده و کاملاً برای صفحه نمایش موبایل بهینه‌سازی شده.
🎯
تست همه‌جانبه:
می‌تونید تک IP، رنج‌های CIDR و لیست‌های ISP رو اسکن کنید. این ابزار دارای دسته‌بندی لیست‌های آماده ISP ایران و بین‌الملل هست و حتی می‌تونید لیست اختصاصی خودتون رو به صورت فایل txt وارد کنید.
⚡️
امکانات دقیق اسکن:
دارای قابلیت‌های نمایش پینگ (Latency)، بررسی مجدد (Re-check) و تست سرعت (Speed test) به صورت مجزا هست.
📁
خروجی حرفه‌ای:
در نهایت آی‌پی‌ها و کانفیگ‌های تمیز رو رتبه‌بندی می‌کنه و خروجی‌های مرتبی مثل best_configs.txt و clean_ips.txt بهتون تحویل میده.
🔗
لینک گیت‌هاب پروژه برای دانلود نسخه‌ها
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6720" target="_blank">📅 11:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=f3JCp9KC3z_ggbKiFbDSRuOXvecW4o5SKp9Uu1bpr8U_4AhN2uOidAkzJNhK4rlLoJDhM0niRwOCJP7cYe1kVNh-3jQU6NBWAjdx4it0jdVGShktkfxqM5pfkTJ_wrqU-Sv3ydBii6fbKP_YQCsoN6O4A7zJKLOLPtwpO-fdBPb2Hiobrt5hovxtch84caqeGnHw9oOHgxKbxTO7MjLj3cc1JWd5LSSR6lONTkHRlpahZavt6oa6lnfJj503YOovrYSm-WkQ_MWPk8gpDRgDx9SZOIlb9HD9HC8nwVG1SRvp3ypUC9qR0pG0smWGbOy2T3RbiM_J5o_XxbQMsQLULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=f3JCp9KC3z_ggbKiFbDSRuOXvecW4o5SKp9Uu1bpr8U_4AhN2uOidAkzJNhK4rlLoJDhM0niRwOCJP7cYe1kVNh-3jQU6NBWAjdx4it0jdVGShktkfxqM5pfkTJ_wrqU-Sv3ydBii6fbKP_YQCsoN6O4A7zJKLOLPtwpO-fdBPb2Hiobrt5hovxtch84caqeGnHw9oOHgxKbxTO7MjLj3cc1JWd5LSSR6lONTkHRlpahZavt6oa6lnfJj503YOovrYSm-WkQ_MWPk8gpDRgDx9SZOIlb9HD9HC8nwVG1SRvp3ypUC9qR0pG0smWGbOy2T3RbiM_J5o_XxbQMsQLULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
‌GitFut⁩:
رتبه‌بندی پروفایل ‌GitHub⁩ مثل بازیکنان فیفا!
⚡
‏هر توسعه‌دهنده‌ای تو دنیای کد یه ستاره‌ست!
🌟
‏این ابزار
رتبه ۰ تا ۹۹
رو بر اساس:
‏
🔹
تعداد
‌commit⁩ها
‏
🔹
ستاره‌های ریپو
‏
🔹
دنبال‌کنندگان
‏
🔹
زبان‌های برنامه‌نویسی
‏بهت میده!
‏
ببین به کدوم بازیکن فوتبال شباهت داری!
⚽
💻
‏
👉
امتحان کن
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6719" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbJWjSTSfz5RdI96aS2pZJV3u4VKQXikGlS3nH0a8ONVyUkgrGd2Yk8ixUXum5RYGKxH0_IXSoC25Ue6lWazUNt1m6cu56WBTZf5P0Ui1cxUpzsu5O-Iy_zTGclGOphY_SQKb2lmBD6G33qJgU8VRxHXExWzfXBciD_LCsoxJK4JACPIdJmkupB-6JKbsGXkEpOFG3L-W2CG1vNptlA2NPcBX8z2xViZJPbaeWJC097oHbUgbkK-rRfJRT-AYduJIB6o4b7lYcUS3WtJX5qNMmQzdVKUotPgVvxzUlEWHxyu1iVwAXaZyTXc8SRwTjbP-N_XdlrbSBN1lJs3SjYDrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
‌scrcpy⁩
— کنترل کامل گوشی اندرویدی روی کامپیوتر!
📱
➡️
💻
‏
✅
بدون دردسر
: نیازی به روت یا نصب اپ روی گوشی نیست! فقط با ‌USB⁩ یا وایفای وصلش کن.
‏
⚡
سرعت بالا
: ۱۰۸۰‌p⁩+ با ۳۰ تا ۱۲۰ فریم بر ثانیه.
‏
🔊
صدا
: انتقال مستقیم صدا (اندروید ۱۱+).
‏
⌨️
کنترل کامل
: موس و کیبورد فیزیکی شبیه‌سازی میشه.
‏
🎥
ضبط صفحه
+ نمایشگر مجازی.
‏
🐧
سازگار
: ویندوز، مک، لینوکس (بدون نیاز به ‌snap)⁩.
‏
🔗
مخزن
:
‌GitHub⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6717" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏
🚀
‌Arvix AI⁩ = جعبه‌ابزار کامل هوش مصنوعی تو
‏
🧠
متن:
‌GPT⁩, ‌Claude⁩, ‌Gemini⁩, ‌Grok⁩
‏
🎨
تصویر:
‌Midjourney⁩, ‌FLUX⁩, ‌Nano Banana⁩
‏
🎬
ویدیو:
‌Kling⁩, ‌Veo⁩, ‌Seedance 2⁩
‏
🎧
صدا:
‌Suno⁩, ‌ElevenLabs⁩
‏
🎁
توکن رایگان + دسترسی به همه مدل‌ها
https://arvixai.net/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6716" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
🚀
آموزش دریافت ‌API⁩ رایگان ‌Nvidia⁩
🚀
‏‌
1⃣
ثبت‌نام اولیه:
‏وارد سایت
‌build.nvidia.com⁩
شو و یک حساب کاربری بساز
📧
2⃣
‏‌
شروع تایید هویت:
‏پس از ثبت‌نام، روی کادر زرد رنگ بالای صفحه کلیک کن تا پروسه وریفای آغاز شود.
⚠️
3⃣
‏‌
دریافت شماره مجازی:
‏به سایت
‌2nd-no.com⁩
برو و یک شماره مجازی موقت و رایگان دریافت کن.
📱
4⃣
‏‌
فعال‌سازی حساب:
‏شماره دریافتی را در سایت انویدیا وارد کرده و کد تایید را ثبت کن.
✅
5⃣
‏‌
ساخت کلید دسترسی:
‏به بخش ‌
API keys
⁩
برو و کلید اختصاصی خودت را بساز.
🔑
6⃣
‏‌
انتخاب مدل‌های رایگان:
‏به بخش
‌
Model⁩
برو و از گزینه‌های
‌Free Endpoint⁩
استفاده کن.
🤖
‏
🌟
برخی از بهترین مدل‌های در دسترس:
🔹
‌GLM 5.2⁩
🔹
‌Minimax M3⁩
🔹
‌Deepseek v4 pro⁩
🔹
‌Kimi k2.6⁩
🔹
‌Qwen 3.5⁩
‏
بدون محدودیت توکن
🔓
بدون لیمیت روزانه
‏
♾
40
درخواست در دقیقه
‏
⏱
🔵
@ArhiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6715" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=jXXbfL27bVy1VaCDIe3-AmucPf2s0YRmziqVEFK2XPiYUS-j_HEGvO_tE6NvJxtNWLuIDQH-UM9AFhqlBhpHS8GeIvunux3PmezPWSO9sOLP34wdqybkUVKfxKoVbZlX9qLWKCeWU2ZP4-gg5gZ4fjCqFMDVMamnW1OCXYcz-3ZoJwNW60VOLiHH7_2_RIe4WeHy7tsdt7nlb5kBLdSXlIa_1RYEIbfZOAOlwz2pAeGt9om4ntL7mQ6yYr83iPTRdD3Afh6n7UHe3d_DHnraOdrGwzr9r8AZUJ27jwHQ_CUEnZHnSWNSXJhdHVQYpsAUKpnEm0oaw3leQUD8Tsh0FrOgk7d12PR2_FSRUjYP2Z0bIuM94CYPZtQztR7hsRsT-8SnagdH28TnhU-3qNWV2Jotq-pPZUik-RwoUd5IILjkmtk9hR-bobqVgF572j2w5-QgimiN1a4Rr8b2q-r_vQZFxjtJyzwnVUMGl7JRlnW6ERq18g7aaIkA3m16p7YJpFjgG1tPl98X0ywzMMX_AgNCbvCefEx0YS6QO0uH-82TebMDMrhygTtQp6u1esnGF16UwAv9ykaQiXqbuQXMuaeueEDo9vla8jQXESOWr1KpplAapnDtUpXxOdftQljXlvBW4Jp8UlLQ0aZ6ie_mPJC_M5AWM_s7mUBKmUME-Xk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=jXXbfL27bVy1VaCDIe3-AmucPf2s0YRmziqVEFK2XPiYUS-j_HEGvO_tE6NvJxtNWLuIDQH-UM9AFhqlBhpHS8GeIvunux3PmezPWSO9sOLP34wdqybkUVKfxKoVbZlX9qLWKCeWU2ZP4-gg5gZ4fjCqFMDVMamnW1OCXYcz-3ZoJwNW60VOLiHH7_2_RIe4WeHy7tsdt7nlb5kBLdSXlIa_1RYEIbfZOAOlwz2pAeGt9om4ntL7mQ6yYr83iPTRdD3Afh6n7UHe3d_DHnraOdrGwzr9r8AZUJ27jwHQ_CUEnZHnSWNSXJhdHVQYpsAUKpnEm0oaw3leQUD8Tsh0FrOgk7d12PR2_FSRUjYP2Z0bIuM94CYPZtQztR7hsRsT-8SnagdH28TnhU-3qNWV2Jotq-pPZUik-RwoUd5IILjkmtk9hR-bobqVgF572j2w5-QgimiN1a4Rr8b2q-r_vQZFxjtJyzwnVUMGl7JRlnW6ERq18g7aaIkA3m16p7YJpFjgG1tPl98X0ywzMMX_AgNCbvCefEx0YS6QO0uH-82TebMDMrhygTtQp6u1esnGF16UwAv9ykaQiXqbuQXMuaeueEDo9vla8jQXESOWr1KpplAapnDtUpXxOdftQljXlvBW4Jp8UlLQ0aZ6ie_mPJC_M5AWM_s7mUBKmUME-Xk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تبدیل ویس به متن تلگرام کاملاً رایگان! (بدون نیاز به پریمیوم) با هوش مصنوعی Cloudflare
https://youtu.be/Xq7e2k3qlqA</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6714" target="_blank">📅 02:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوستان وقت بخیر و خسته نباشید
این چنل زاپاس آرشیوتل هستش
داشته باشین بهتره
❤️‍🔥
ی موقع اگ چیزی شد...
https://t.me/FOSSArchive</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6713" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=mg20upTRhxouVzruSqo83QwcfEIDHUOe1HhMZuQeKi9JvJfJBYBaaFJ8JqSciG1ImMVKJNsNLUvXu8btpsH2MBSckWtQoxTn5RqzxiRJRJCiesaiRqf2EU4Li7fC_gZmXPV3ANgk6E5w5FxTENVcKeW1Vmi18QOM2aLnY9dC_10izYkBASEAJsmiAi9J6mvDyH_5enisI0uPPKT5-YzecznQ9QEfPVSNQsVaTlWdodJjVoj5_q5Ljv3GTskRCaZk3A9ma2IijZKBX6BjHxz3co0mXHR-dZ8OQzA1D2VpWD2qpQRtqAJMPNXG9ob0Y11uyl6IB3NSGxojA9UXYCey7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=mg20upTRhxouVzruSqo83QwcfEIDHUOe1HhMZuQeKi9JvJfJBYBaaFJ8JqSciG1ImMVKJNsNLUvXu8btpsH2MBSckWtQoxTn5RqzxiRJRJCiesaiRqf2EU4Li7fC_gZmXPV3ANgk6E5w5FxTENVcKeW1Vmi18QOM2aLnY9dC_10izYkBASEAJsmiAi9J6mvDyH_5enisI0uPPKT5-YzecznQ9QEfPVSNQsVaTlWdodJjVoj5_q5Ljv3GTskRCaZk3A9ma2IijZKBX6BjHxz3co0mXHR-dZ8OQzA1D2VpWD2qpQRtqAJMPNXG9ob0Y11uyl6IB3NSGxojA9UXYCey7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
ImageGlass
ابزار سبک و سریع برای مشاهده عکس ها در ویندوز با پشتیبانی از طیف گسترده ای از فرمت های فایل.
• پشتیبانی از بیش از 90 فرمت: WEBP, GIF, SVG, AVIF, JXL, HEIC
• رابط کاربری بصری با سرعت پردازش بالا
• مناسب برای کاربران عادی و طراحان
https://github.com/d2phap/ImageGlass
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6712" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423195fff7.mp4?token=UqSej7W9kKSvIMFIPDoxJlfdn6Vj9I4EtvZD2tD6wxBBY6huy5km_vZoC28k3jTSuJuGz2B8qLmCfzwSQaIP_pHNraXunTYDQVpNZjCdPUZqRlElN5K3Up6s9LZVI0WfWEI2auPQxR8LN4-shR-yxSGpaIYHZXxH8_tl9Tj4Euo6aHhuKz0qbIXj7k00_Gyl4KE05yBcxOckHeRXKtTAMkn6lA4k7M8GMXGxtUUtCCDuEZf-9CGunanF_0n3URv4DDY7Ac5oBVqoMRCQwFWRYSDyogPZu3e2sKpJ3URtVDSQPQrYkoLBWmHs6vfoL7a3lbu-1NI6OrsQF3wyeS3AvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423195fff7.mp4?token=UqSej7W9kKSvIMFIPDoxJlfdn6Vj9I4EtvZD2tD6wxBBY6huy5km_vZoC28k3jTSuJuGz2B8qLmCfzwSQaIP_pHNraXunTYDQVpNZjCdPUZqRlElN5K3Up6s9LZVI0WfWEI2auPQxR8LN4-shR-yxSGpaIYHZXxH8_tl9Tj4Euo6aHhuKz0qbIXj7k00_Gyl4KE05yBcxOckHeRXKtTAMkn6lA4k7M8GMXGxtUUtCCDuEZf-9CGunanF_0n3URv4DDY7Ac5oBVqoMRCQwFWRYSDyogPZu3e2sKpJ3URtVDSQPQrYkoLBWmHs6vfoL7a3lbu-1NI6OrsQF3wyeS3AvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کتابخانه‌ی معروف ‌Pad Shaders⁩ (منبع غنی گرادیان‌ها، پس‌زمینه‌ها و شیدرهای خفن) رایگان و متن‌باز شد!
🎨
✨
‏دیگه نگران لایسنس نباش؛ می‌تونی تمام پلاگین‌ها و ابزارهاش رو تو پروژه‌های شخصی و تجاری استفاده کنی.
https://shaders.paper.design/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6711" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6710">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
دسترسی به قدرت هوش مصنوعی در سرور شخصی؛ آموزش API کلودفلر (Workers AI)
☁️
🤖
اگر برای پروژه‌هایتان به یک هوش مصنوعی قدرتمند (مثل Llama 3 یا Mistral) نیاز دارید، سرویس
Workers AI
کلودفلر یکی از بهترین و بهینه‌ترین گزینه‌هاست. برای استفاده از این سرویس، باید یک API Token اختصاصی بسازید.
🔥
مراحل دریافت API Token در کلودفلر:
1️⃣
ورود به بخش API:
وارد پنل شوید، روی آیکون پروفایل کلیک کرده و به مسیر
My Profile > API Tokens
بروید.
2️⃣
ساخت توکن:
روی
Create Token
کلیک کنید و سپس
Create Custom Token
را انتخاب کنید.
3️⃣
تنظیم مجوزها (بسیار مهم):
در بخش
Permissions
، گزینه
Account
را انتخاب کنید و دسترسی
Workers AI
را روی حالت
Edit
قرار دهید.
در بخش
Resources
، اکانت خود را انتخاب کنید تا دسترسی‌ها محدود به همان اکانت باشد.
4️⃣
نهایی‌سازی:
روی
Continue to summary
و سپس
Create Token
کلیک کنید.
⚠️
توجه:
کد نمایش داده شده را بلافاصله کپی و در جای امن ذخیره کنید؛ این کد دیگر نمایش داده نخواهد شد!
💡
نحوه استفاده:
شما علاوه بر توکن، به
Account ID
نیاز دارید که در صفحه اصلی
Workers & Pages
پنل کلودفلر قابل مشاهده است.
آدرس فراخوانی (Endpoint) شما به این صورت خواهد بود:
[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){ACCOUNT_ID}/ai/run/{MODEL_NAME}
✅
حالا می‌توانید با استفاده از این توکن، مدل‌های هوش مصنوعی کلودفلر را در کدهای خود (پایتون، Node.js و...) فراخوانی کنید.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6710" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RULSUtryxUITU_u-TZgyLxrPvVje-LqfhFNRQE3Kik3twoBwRWtUOIYBxd_w6vpjH99nohxHX-9WyhJcCMxF70sBRC0tghYz2-GJ0SgakzOHUkSgx7pzXL07Nmz8aDev4IGkea0wZHW1p0DSPVGa_WAnWL-gATGD2uKnSUe0oH8ymax96H3h6bst30hvDSQTfAdUToi7Sq65vhbTntCT6Eawd8Z_nNPEFnqYWPKAB0ImxCG_NpQJZ7LVYyRnjuC8cH2XaG5OQrQu3JpcfOzx3DDXYLox1BQr_iUpQWZhM1bFdoz9P4YKlKO1mGtp5RcOolIjnU2ZfJk2gbJXTqMXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5
هوش مصنوعی رایگان و قدرتمند شرکت انتروپیک
10 دلار کردیت
با لینک زیر 20 دلار
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6709" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سایفون رو اپدیت کنین خوشگل شده
🔥
(نسخه بتا)</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/6708" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=buTWUxQ4CcsT0ahKpj9YPfcXYhnQfhYao6_MOP73neuhCBRbWFU0gsjao9nb8XWtd0WzsS3GGsUbai-6mYVGtuxkBtYXbScRXMscC5JNPt135SLLNUaxJZ3EtA74udZ2wYyqH6j_Poj-rfHqAjvnnmqHhggpcgLcePJlkrlllMcHu12E8wQa5WHbfIWd-EicUNGO2vXru_z1LaCU1p9AYP6zYojiumFb8PhJiBw63Z0V191kGeLPRncF5xiUy5jcRKIJWnOTCPLJ0BsUpm7NDU2_vo0hHN7Q0lIyancGCvJWpBRHLPHYD1_MobiO2XwMXeOMF4tjYixDkftjTw7ehg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=buTWUxQ4CcsT0ahKpj9YPfcXYhnQfhYao6_MOP73neuhCBRbWFU0gsjao9nb8XWtd0WzsS3GGsUbai-6mYVGtuxkBtYXbScRXMscC5JNPt135SLLNUaxJZ3EtA74udZ2wYyqH6j_Poj-rfHqAjvnnmqHhggpcgLcePJlkrlllMcHu12E8wQa5WHbfIWd-EicUNGO2vXru_z1LaCU1p9AYP6zYojiumFb8PhJiBw63Z0V191kGeLPRncF5xiUy5jcRKIJWnOTCPLJ0BsUpm7NDU2_vo0hHN7Q0lIyancGCvJWpBRHLPHYD1_MobiO2XwMXeOMF4tjYixDkftjTw7ehg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت 10 تا ایمیل رایگان با ساختن یک ایمیل اتومیک (مولتی اکانت)
https://www.youtube.com/watch?v=XHJ3TwrwG-g</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/6707" target="_blank">📅 03:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrmibMGUmVfoSRWNNe_TcOLJ0GecR3TJlyGKBx8N-ip7DY06ILu1pwBj9Mw_Gs2qmN3aWp_LaTVS-N0Evhr-Mi9j1g9-C0BFsHo9MIav8dCUXICGZClU3EQgIHDBLwnZWH0YrWuvLz5qOQ1gqXF6_vSUprZ54PCYMbxstmtZ7AaaGHux_emS2N2aNpXD6PjPTcD_jM5slYF9mOfZJ1i6VTI03WPA2t73HtbpkuU9zku6xoo_LpM_2RISGGbAP0_fuCsd_CCGtAk4KRybAaIhEbPvSg66vKxtXvNwfdPszNyK3LfNoA_0y0oTQgI0CbKgGkQpjRKkgkTHIh1kJrqNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
قابلیت جدید «وگا کد» فعال شد!
💻
‏همین حالا وارد
‌Mini App⁩
ربات وگا شوید و از قدرت کدنویسی هوشمند لذت ببرید.
✨
‏
🛠
مشخصات فنی:
‏
🔹
پشتیبانی توسط مدل قدرتمند
‌GLM 5.2⁩
‏
🔹
سقف
۵ درخواست
در هر ساعت
⏳
‏
🔹
ورودی تا
۱۵ هزار توکن
📥
‏
🔹
خروجی تا
۱۶ هزار توکن
📤
‏همین الان تستش کنید!
🚀</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6706" target="_blank">📅 02:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yx2R4tjyVJom4ymT5H3xyyiiVY5YEEymo8yUkGCXv4INgQbko5hWals5Jo4nmxa1gP6VeQ5PhoeXcc1V6ARVRNp4Tbic3nmefohJTOwSYn6B7FKhswA_XZdgyRQ9-DxgyGK72ZUFlxuLZdNxCWiRT3PsNyEcN0sojbPbP71yF9GYnEX_1hcX2fFlk_KDauw8LNwnoDqqM465LH6UBF5348WpXn98K5Qvr7etFQGdlbdJLqZhBuIJ057DavufS6qQWupgHBgc7XA6ywg-fr4lGgLGiNpBTwAdfdfdQxFSS1I9JEROa73q0BuJFNVDiX87-psbJ83l2RHT3beqfzNygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک میلیون توکن رایگان Gemini از طرف
گوگل؛ بدون نیاز به کارت بانکی!
🎁
✨
گوگل به تازگی یک فرصت بی‌نظیر فراهم کرده است: دریافت یک میلیون توکن کاملاً رایگان برای استفاده از جدیدترین و قدرتمندترین مدل‌های هوش مصنوعی این شرکت. برای دریافت این توکن‌ها به هیچ‌گونه کارت اعتباری یا خرید اشتراک نیازی ندارید و همه‌چیز با یک کلیک انجام می‌شود!
🔥
چگونه کلید API خود را دریافت کنیم؟
1️⃣
ابتدا وارد پلتفرم Google AI Studio شوید.
2️⃣
روی دکمه Create API key کلیک کنید.
3️⃣
تنظیمات و محدودیت‌های تولید را به دلخواه مشخص کنید؛ کلید شما آماده استفاده است!
🤖
مدل‌هایی که می‌توانید با این کلید استفاده کنید:
Gemini 2.5 Pro (قدرتمندترین و هوشمندترین نسخه)
Gemini 2.5 Flash (سریع، بهینه و همه‌کاره)
Gemini 2.5 Flash-Lite (فوق‌سبک و اقتصادی)
💡
کاربرد: این حجم عظیم از توکن‌ها برای ماه‌ها کار فشرده، از جمله کدنویسی، پردازش و تولید متن، تحلیل داده‌ها و حل مسائل پیچیده کاملاً کافی است.
🔗
لینک دریافت کلید API
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/6704" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olQBS1eZByix_8HBQtT4w4uG6XaSPJaOjP7RyHq9qJuXZEKOj9_v_AEghGUvkdLhEeeeoUscj3E8fs7lcg__t1WepgdGlfYOZe1-O93ZaPIzKdsQdh02QBAZKi-coblBrGrg3zD5BkHwniZyne6U9lkriD1k4N2NbIlFTWBrAGvUBgVSm0x7ka4S5lxUU051_XBDULVObFJiY_N1dGvj5gL5jZktQ-XnZfnB0h-MqPPlvAGQciUxp-al5x8xh_Tf_FzeV2PXS1D2eSurAZlTf-kiYPHnSpNavWaJkKFxPgnXtbY5tbdQKxxNi0cabBLT6tchhS_zzTbQgfKIpDPfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفسیر خطاهای ویندوز با ابزار داخلی
راهنما:
— کد مورد نظر را کپی کنید، مثلاً 0x80070422.
— ترمینال را باز کنید (با فشردن Win+R و وارد کردن CMD).
— دستور
certutil -error 0x80070422
را وارد کنید.
— توضیحات دقیقی از مشکل را دریافت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/6703" target="_blank">📅 22:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfkuAENWkgbnS5TecJyU2QufYOZSDd23mj467Lt4wdbPhjm6sXxzj9tC6vfwbyU3SLjTHK7F-VU5KXqpqOEccfvINCmHguQlgYTCG9jM3QleZIB_zT7_kzlLYS_VxpQu6-8vK-ZZJT7c_b9B8wABPdsawo9bvSQNoOXxz925nsw9pi2i7ai9bN5coKGUG_PttYcCqHfGN-CL4SDuPadwVrbA8GiHBIVZEAndJwUGWrsnD88RxmJlBgX71tJ8OOrdLbpg-2vPB6kVVxow5OZYhfDIHplx3oJhg-RhRDDxbNsu9xww5zLgSjGxcHyly6i6Ggs6dbBHljI6nCo7DuKU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا پولاتو چیکار می کنی؟
پولام:
به زودی ۱ میلیارد*
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6702" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5cLokGSZPo--ngpeXMk8kr8x8yUB57aZhCQ64Vj5dDWJgbQOLFzNUAqA4OwNrywxlXWW9HWM_DFVDdCqrIz9H4mDaaQK6HSUFqMLzEn2vO_HJNjQqhSDcIbZrC3Itb5mruKIAYj3GsqNgoPGl-VJUF7ZcojF_R2f-bpbkFmi-wlH817d3TeN9ZSpvlk15ICXFXt5MnkM7c70-Z2f-nsLOGQORwXK_JmlQJV7FuPseUEIdQt1OqDjhyMF6RPzjRzU54EIqE-8N4Hh2sWBmvgYLApqLNX4TkDAXDHmpnMI0aoequozjtASA2up-C9O-jVOFZyUy0_e4CgrhZK7UcLwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuLKc2Casv85VK1V8aYiTUvyZ9QgWQ6J2Cihh4dka4tUQThHnSM2IV50enbrD_GvASCQqENmBc8wgNnmnw2y2OEHaotwSIvjSD6mc0eMWSwVSkLYsgn5RC2sJ3Ar7Qkl2Ax4LIAGanBJUI8EWbIVtp1kpHuw9ZngzZTEyDizm9xtTxccqTEBQA0OUHgNnGC5FJimalWDhWSCJH6yOwiiw5ZQpmBqauJThibP5JA0ohlaCkKl4b-gK7k6L5-cCtKr3Ja98tHGEzoeq1X0LqSHZYIN7Az1hJ6QVK_kJ6WlEZAYDh7eysJumQG755bJ0JTCm9rUMI__xEZKGaUEgPmFQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVlTUOEDfZaqVBu4B2aLN5Je_XDLnJOi-KZwNRvb20PaZ6Jx2CnlBza_GMm4F9W1mWHLyroGBvqArLDpsuI2366I0LPSPEpy8eycQqGQ2bXvujm23f0VFsGQO5GPNVMYpX9Fj-eWZmq9W1BcxIUBnasOXOXU_v6P6SwLr6ibMyOfXNeSOwRpM4Z3Go3mJxUFpqOulpynCSp16TIxWrYuc7cmA8-OIvC5LCEtGX6O9qFhPCwpQyuX0pJ0FwYi7J5TaGrJJJEiBP9azV8b8gqrArFb9bjt5hMx0p-cw2Gf-TGrE6OXg9_UhH9N6pEjQoWAMskctSejtpDNYuAaXp559A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rR7iffPlI89vlJdi5-ytiLtEWRi8OeqoxUBbM0Vgos-PCaAlNrerzww_UAHbmXMdrWfIMl38ZOJ7egGcJsegesh2kOz4vcRd_ws6N56EKufL7AVneon-SoXooUPI2pwidQlenCNCmeV_5gtMlszFkg0zMAdvIdu3VTAkeSMzcqk9T6mb65SUErWpeSp5Vk_QlOAeWJJ5m81V-jAdbBC2lW1HmOOU8fPDkOIOTZ2eJp7utz5RfmiMhqcxAz4oS_d_dAvonGEHeoTUSlYRaPPXxBSGOQD_1YfzE3Wd4WkEFGu40jQk2qDMR_ItNoBqIsPomxdRnkQXtCNLn3z9GoSm2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4HbYibQBm9Vo2whyTYvoHOg3z1BYOvZDUWOYSjhomcSKwqvVxJMPJYgmd43BCbKXIxLwOEsYNZlyUvw5vIGlkTZb-GDbbbiV4Bg-LhMNVm0Ao7bNkX_c2MlZq_p9P_BGIq9udcGK8WbIgKVop7Jtbh2_d31yZmE_VGxLjICZ40IxV5ZhM207LNwIMH7YCNkC2eRtG8gjcIjDFsNFc-o4D6y9jDIJiPFS62LM1xbVVRaCOSELpbrCgXers8hKsaVW5xpVfJFnKPImuKz80Xc6GlT9FOpKvlmjmgIXYDPTfjJ1iZsWkQA1eHc47PLBSLcOGdExuafkAnKRwFIIPOrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqNGharAPkGD7Jpnsewg7t3J9MJk7aohafVAKhBlVoXSMfR3qS2tj1iYABRAH4vX9neMroFuzZF9c4el5Lcd8yqFQFfGzXsB0SaSll5SIfO9sV_g36JtwuUlddrQVUg4D9mHRkJ8iKmn477VJIVVq5Cs4rsuqPvuuhe9DK2L9cLImNm5XUaGt75E1Hx9e1eMoSSB_5tg5NUJyYP3I05e7u4v5sJ4EaAD_ytdY-Rcp1d45SuvvV4_Gev7BF7u5D2bpdWZPTSKGUZGxDd7OtdyOku3N4IlPtB4Q6DgJVILNfjjGnv-K15IxMmUsdqwywi8qG0Dz-YIJgGZbQGRMmbCkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KH1xT8-70hxtWqtns1Ro3Jw_MqTbjj0j-giGZUKfucOn43SphCjqurG6ECLNLTBOStpw2Vw7Sb-4jgR2lHj82D3JWwd8ClKemxMqy6ipBLiI_Dnp0ms5MkynO59K3k40-FFY-4VfqvRQiAXNDgVHicTB0FGHVADWGJw34Gv8z9XoQ07PSzgKuNhkDRDH8xlKw26HwX3YjsHj21IujeV93HyfNG-3BRBaA2_v1dGleAkgFeXRY6lk_X6YUxHehyENJPBiB7B9xJSqXvThXrDUsuqEXPOI6WCI3ansTzn5qNXTtTc6EpZcWXmDzh6QEv-Xs58csdEG22Hx82zwDddb_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج
جایزه عکاسی با آیفون اعلام شد.
در این مسابقه سالانه عکاسان از سراسر جهان بهترین عکس‌های خود را که با آیفون گرفته اند، ارسال می‌کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6695" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYCq_B_E0bAiR_WLE2VlbCRPeszsFI6yTEc04FT3R803QlZQ5g8QQGTvdwWadjjnHWh7f04U26eMBER-CpDrNyYKf5OHMwd66yFzk0nLASOrpOd4TXJk7Vr9SGdv_0W5gxmlQgSxTAsFBSIeqBWeXyoWUGLuenFWWBEzo1LCFhb5AODvfMYjiP7EUTOTPz9mUPnOsKKzx-lL-1pk6abiezRjY9WheciaqGlzDgkJBkG80P6y7n1YuZHZk8VTCg4X5K3LgoFe7yntzG6qfAUJSyvd-rAwCL0mSFWN6bTpD94tJkmvpbFS6FBZrY8f_bnm9DoFls1qImPGy2KXtZgfsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AITwitter Generator
یک افزونه برای تولید توییت است.
این افزونه که بر اساس فناوری پیشرفته هوش مصنوعی ساخته شده، خلاقیت و سرگرمی بی‌حد و حصر را به حساب کاربری توییتر شما اضافه میکند.
https://tweethunter.io/generate-tweets
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6694" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHBYgI-NXuneFBS0XZC3i6IK33fQinBiVqn3zAhcaNkXXrU1MgynOB0kwXpMGfk1uwm1e3foDf_0vHHKbZnfoJt-FQhC8hGSt7EqKYCDW-QKqSdIKXAjqXnb0gJlkUylTcAzHZnkwC3234Amcnkd5haE-WBGz_mqaLNmffYLilYeOy0ejlEfcg_obvYDUA2d6qwnxdyrUXcsBU4fH7m317J2lNaKoDwbAQ5KP7VliA7Uxh-qiA7u0BnqX-5Gc6qY7lU6LAFGkFF8icvHwifwhiUSfHpt79MwtbrM8ftmt2AQ7fGugZ1qQwwaVb-AKHNeinOGXLUkJzyNNLYxyGuewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک مجموعه‌ای رایگان از پرامپت ها برای Claude ارائه می‌دهد
🤩
این مجموعه شامل ده‌ها راهکار آماده برای بررسی امنیت، رفع اشکال و بازبینی کد، خودکارسازی وظایف و موارد دیگر است. برای هر پرامپت، توضیحات مربوط به نحوه عملکرد آن ارائه شده است.
https://code.claude.com/docs/en/prompt-library
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6693" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InejEggDOqYxl48km9G_-E3msJCZCO5zBBtXfGx6XZeqllzp_i2Qt9lFffjf9Otk_t3vhGlPUwd-LihBUVgtj2QAiqeAf5RREJJgefOGNe5s0mXBjijuz42sSfGE0G2i54n8TjiKPZsZ25F-unlV8L7KTOcOr1T6VoEpHKu1vSeoITHR840twdzYzZX3r__lG7okbH8I19eruIQSy9HX-LJ3Abm0EcCuwHodFMicQadvkzrKJHooNLinFGopfSJTYSmIT6pvZiqmcAwrMEAOixYypCZCKOJDlNooeRN_tRGZBJykkUdvvgz1Ft2KHlnfgoS3Ssbr6fbVgT7F8wJoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فتوشاپ را فراموش کنید
🤯
یک ابزار مبتنی بر هوش مصنوعی می‌تواند تمام وظایف را با دستورات متنی انجام دهد و برای این کار نیازی به مهارت‌های طراحی یا دانش فنی نیست.
🎨
✨
🔹
همه چیز بسیار ساده است: یک عکس یا تصویر را آپلود می‌کنید، پس‌زمینه را تغییر می‌دهید، اشیاء اضافی را حذف می‌کنید، رتوش انجام می‌دهید، کیفیت را بهبود می‌بخشید و از ده ها امکان دیگر استفاده می‌کنید.
🖼️
🛠️
🔹
بدون ثبت‌نام و مستقیماً در مرورگر
🌐
🔹
کاملاً رایگان
🆓
https://ezmaker.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6692" target="_blank">📅 14:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
🎁
500 کریدیت رایگان ‌Opus 4.8⁩ و Fable 5 هدیه بگیرید!
‏دنبال دسترسی رایگان به قدرتمندترین مدل‌های هوش مصنوعی می‌گردید؟ با این روش ساده، ماهانه ۵۰۰ کریدیت رایگان دریافت کنید.
🚀
‏
1⃣
وارد سایت زیر شوید:
🔗
‌www.relay.app
⁩
2⃣
‏ ثبت‌نام کنید:
‏با اکانت
گوگل
یا
مایکروسافت
خود وارد شوید.
3⃣
انتخاب مدل:
اگر روی آیکون پروفایل خود کلیک کنید و وارد تنظیمات شوید
در بخش اکانت ، اولین گزینه را بزنید و select model را انتخاب کنید و مدل مورد نظر خود را انتخاب کنید
4⃣
لذت ببرید:
‏از امکانات پیشرفته و کریدیت‌های رایگان ماهانه استفاده کنید.
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/6691" target="_blank">📅 23:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🧠
یک سرویس جدید که قادر است مدل‌های سه بعدی را به کتاب‌های آموزشی تعاملی تبدیل کند!
📚
✨
هر مدل سه بعدی را بارگذاری کنید، سیستم به طور دقیق ساختار آن را تجزیه و تحلیل می‌کند: عملکرد هر قطعه را توضیح می‌دهد و نحوه کارکرد آن را نشان می‌دهد. در پایان، یک آزمون کوتاه برای ارزیابی دانش شما ارائه می‌شود.
🧪
🔧
برای آشنایی اولیه با قابلیت‌های این سرویس، مدل‌های آماده‌ای در زمینه‌های پزشکی، مهندسی و علوم طبیعی در دسترس هستند.
🏥
🏗
🌿
https://atlas3d.space/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6690" target="_blank">📅 23:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=B10qh04DRFRtONyCpWStuRRzX4jgQye7njD1EdCK75BJxZO0ji3-Qlg0LwnZvyQlm3eaGmDS0Wdr64LsHYTPdnZwzveejOTO1sSzbrusQARSpmooNgGmEyXHj1XNDIaze3W_x3TNDoK5ORNvurLSsgrdaQBvafHlZ03WRH750v6uODbnsSPmEjyHITiPu8rO0xLpFwCIV1CKlO2R2kG5tC8ep3rhq-RseuhYv3mwQ_A8XXimSOIaxM5lgVNZFVLAJw61Ah-s1oSrT3Q-DSba-7Z7EXYuZqY4WBJH3GPjFkv4h-XRAFH8vlRscEDJrHSLD7IC82XiGHw6njkWkQerng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=B10qh04DRFRtONyCpWStuRRzX4jgQye7njD1EdCK75BJxZO0ji3-Qlg0LwnZvyQlm3eaGmDS0Wdr64LsHYTPdnZwzveejOTO1sSzbrusQARSpmooNgGmEyXHj1XNDIaze3W_x3TNDoK5ORNvurLSsgrdaQBvafHlZ03WRH750v6uODbnsSPmEjyHITiPu8rO0xLpFwCIV1CKlO2R2kG5tC8ep3rhq-RseuhYv3mwQ_A8XXimSOIaxM5lgVNZFVLAJw61Ah-s1oSrT3Q-DSba-7Z7EXYuZqY4WBJH3GPjFkv4h-XRAFH8vlRscEDJrHSLD7IC82XiGHw6njkWkQerng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😂
سووو رونالدو با رینگتون های مختلف
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6689" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آموزش‌ گرفتن Fable 5 به صورت رایگان تا 1 ماه هر هفته 70 دلار
💰
برید توی
Aerolink
و ثبت نام کنید
📝
لینک ثبت نام
🔗
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
📄
نحوه اجراش روی
claude code
هم همونه فقط این تنظیمات رو بزنید جای اون
⚙️
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
هر ورژنی از claude code هم بزنید قبوله
✅
لیمیتش هم دقیقا مثل
freemodel
هست
🔒
موقع اجرای claude code بجای دستور claude این دستور رو بزنید
👇
claude --model claude-fable-5[1m]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6688" target="_blank">📅 22:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
معرفی Qwen Gate؛ دسترسی رایگان به API مدل قدرتمند Qwen 3.7-Max!
🤖
✨
مدل Qwen 3.7-Max در حال حاضر یکی از بهترین مدل‌های هوش مصنوعی است، اما استفاده از API رسمی آن هزینه دارد. ابزار متن‌باز Qwen Gate نسخه وب (
chat.qwen.ai
) را به یک API کاملاً سازگار با استاندارد OpenAI تبدیل می‌کند تا بتوانید به صورت کاملاً رایگان و لوکال از آن در پروژه‌هایتان استفاده کنید!
🔥
ویژگی‌ها و قابلیت‌های این ابزار:
1️⃣
سازگاری گسترده:
قابلیت اتصال بی‌دردسر به دستیارهای برنامه‌نویسی مثل Cursor, Claude Code, Continue و سایر کلاینت‌های مبتنی بر OpenAI.
2️⃣
چرخش اکانت (Multi-account rotation):
پشتیبانی از مدیریت و چرخش بیش از ۳ حساب کاربری برای جلوگیری از محدودیت‌ها.
3️⃣
امکانات کامل:
پشتیبانی از فراخوانی ابزارها (Tool calling)، استریمینگ سریع و دارای یک داشبورد حرفه‌ای برای گزارش‌گیری.
4️⃣
پشتیبانی از مدل‌های مختلف:
دسترسی به Qwen 3.7-Max, 3-Max, 3-Plus و سایر نسخه‌ها.
💻
نصب و راه‌اندازی سریع:
برای نصب کافیست دستور زیر را در ترمینال اجرا کنید:
Bash
curl -sSL https://raw.githubusercontent.com/youssefvdel/opengate/main/install.sh | bash cd opengate && qg
پس از اجرا، آدرس
http://localhost:26405/dashboard
را در مرورگر باز کرده و اکانت Qwen خود را اضافه کنید. حالا می‌توانید از آدرس http://localhost:26405/v1 به عنوان Endpoint (درگاه API) در نرم‌افزارهای خود استفاده کنید.
⚠️
توجه بسیار مهم:
از آنجا که این ابزار بر پایه اتوماسیونِ رابط کاربری وب کار می‌کند، احتمال مسدود شدن اکانت توسط سیستم‌های امنیتی وجود دارد.
حتماً از اکانت‌های فرعی و تستی استفاده کنید
و به هیچ وجه حساب اصلی خود را متصل نکنید.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6687" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚀
ساخت بی‌نهایت اکانت معتبر با یک Gmail!
📧
✨
سایت‌های حساس (مثل صرافی‌ها، ChatGPT یا AWS) ایمیل‌های فیک را مسدود می‌کنند. اما با ترفند پنهان «پلاس» (+) می‌توانید بدون نیاز به شماره موبایل، بی‌نهایت ایمیل معتبر (برای دریافت اکانت‌های تریال) بسازید!
🔥
این ترفند چطور کار می‌کند؟
قانون جیمیل این است: هر عبارتی که بعد از علامت + (و قبل از @) بیاید، نادیده گرفته می‌شود.
مثلاً اگر ایمیل اصلی شما ArchiveTell@gmail.com باشد، می‌توانید با این آدرس‌ها در سایت‌های مختلف ثبت‌نام کنید:
ArchiveTell+twitter@gmail.com
ArchiveTell+vpn123@gmail.com
از نظر سایت‌ها، این‌ها ایمیل‌هایی کاملاً متفاوت هستند، اما تمام کدهای تایید مستقیماً به
اینباکس همان ایمیل اصلی شما
ارسال می‌شوند!
🛠
ابزار کمکی:
برای ساخت خودکار هزاران آدرس مشابه، می‌توانید از ابزارهای آنلاین
Gmail Generator
استفاده کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#آموزش
#ترفند_جیمیل</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6686" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaXXY3o26cyOL18JBk6VAbERAKWeGSec5MqpPdniwxM-VQ-H1vCCPjDXEZGwTFR7bVEhBgG_qbcQZpCZtnO1Q0gTGBhKVdqewj-nO9vXHvVj9_Kce6-JQ5E05I8ymJqDHIxwFvElzJwM6ujImJqmtOZDC0CH7ATitRQ_HtJbuNtNuPvYgSrho81W4NRENrYlvAGEUUS87tyDACfoekfGqRyQHLROnJDsiDfDP2wzyBbC4BS3BlSFpSHcVU55IpBRWi-SF_NjnFy3k88Iell8dgIG1wHMGvlv9haKr8J_g54EWpHwZVg1lIjnEylhvxuA1uB3OM__TQmMnAFzJYaVBl70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaXXY3o26cyOL18JBk6VAbERAKWeGSec5MqpPdniwxM-VQ-H1vCCPjDXEZGwTFR7bVEhBgG_qbcQZpCZtnO1Q0gTGBhKVdqewj-nO9vXHvVj9_Kce6-JQ5E05I8ymJqDHIxwFvElzJwM6ujImJqmtOZDC0CH7ATitRQ_HtJbuNtNuPvYgSrho81W4NRENrYlvAGEUUS87tyDACfoekfGqRyQHLROnJDsiDfDP2wzyBbC4BS3BlSFpSHcVU55IpBRWi-SF_NjnFy3k88Iell8dgIG1wHMGvlv9haKr8J_g54EWpHwZVg1lIjnEylhvxuA1uB3OM__TQmMnAFzJYaVBl70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیه‌ساز هاگوارتز ( مدرسه جادوگری سری داستان‌های هری پاتر ) از ‌Fable 5⁩
در این قلعه افسانه‌ای می‌توانید درس بخوانید و با جارو پرواز کنید.
🧙‍♂️
‏این شبیه‌ساز مستقیماً در مرورگر اجرا می‌شود.
https://hogwarts-production.up.railway.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6685" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ظاهرا کلودفلر اعصابش از ایرانیا **ری شده و از این به بعد دیگه ایمیل فیک قبول نمیکنه اگرم بکنه تایید نمیتونین کنین اگرم بتونین تایید کنین بنتون میکنه
😍
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/6684" target="_blank">📅 18:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ArchiveTel
pinned «
دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...  https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6683" target="_blank">📅 18:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🛡
آیا وای‌فایِ شما واقعاً امن است؟ (یک تستِ ساده و حیاتی)
خیلیا فکر می‌کنن چون روی وای‌فای‌شون پسورد گذاشتن، امنیتشون کامله. اما حقیقت اینه که اگر پسورد شما ضعیف باشه، نفوذ به شبکه و شنودِ ترافیکِ شما برای یک فردِ آشنا به تکنیک‌های ساده، کمتر از ۱۰ دقیقه زمان می‌بره.
⚠️
چطور تست کنیم؟
در دنیای امنیت، ما از روشی به اسم «Capture Handshake» استفاده می‌کنیم. وقتی یک دستگاه به مودم وصل می‌شه، یک تبادلِ اطلاعات (Handshake) بین اون دستگاه و مودم انجام می‌شه. اگر کسی این تبادل رو ضبط کنه، می‌تونه آفلاین و بدونِ اتصال به مودمِ شما، اونقدر رمز عبور رو حدس بزنه تا بالاخره یکی درست دربیاد!
💡
چطور نفوذناپذیر شویم؟ (اقدامات فوری)
۱.
پسوردِ قوی انتخاب کنید:
رمز عبور باید حداقل ۱۶ کاراکتر شاملِ (ترکیبِ حروفِ بزرگ/کوچک، اعداد و کاراکترهای خاص) باشه. رمزهای ساده مثل شماره تلفن یا کلماتِ دیکشنری، در لیست‌هایِ هکِ «آفلاین» در عرض چند ثانیه شکسته می‌شن.
۲.
غیرفعال‌سازی WPS:
این قابلیت که اجازه می‌ده با فشار دادنِ یک دکمه روی مودم وصل بشید، یک درِ پشتی (Backdoor) خطرناکه. حتماً وارد تنظیماتِ مودم بشید و
WPS رو کاملاً Disable کنید.
۳.
ارتقا به پروتکل WPA3:
اگر مودمِ شما از WPA3 پشتیبانی می‌کنه، حتماً تنظیماتِ امنیتِ وای‌فای رو روی این گزینه بذارید. WPA3 به شکلی طراحی شده که اصلاً Handshake به روشِ قدیمی تولید نمی‌کنه و عملاً در برابر این حملات ایمنه.
۴.
تغییرِ دوره‌ایِ رمز عبور:
حتی اگر رمزِ پیچیده‌ای دارید، هر چند وقت یک‌بار اون رو تغییر بدید تا اگر کسی قبلاً در حالِ شنودِ ترافیکِ شما بوده، دسترسی‌اش قطع بشه.
این پست رو برای کسانی که هنوز رمزِ وای‌فای‌شون ضعیفه، فوروارد کنید!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/6682" target="_blank">📅 13:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQcDETQNn3b_LB3AXASDaz8pfhZFRrFweICRLjmdY8OuZ24cpZl3Dm7Lr3ZCT0hWkSzYO1sA64pKx2P6UfCYp8kRjHb0VBc6xtgeUM0UaVFQQ1anBotwA2zRDbnZ2UbIlJqaXUfRtfbLmD23YjkKF1_WYf0He4dsKCIT6SJ0VA0fRqEgYa_5bzl_IfgzMKSva0Kt7_lwMYWtP75oEauQfXAKaCGqeAPPA-IEPFfdY0V7fJCxBEO00op5PFCnNUINEd_lzixPz1_ZdSIN1uVZrta6xH1VX-Ru7BwcGlZe9pWoVYud8tGC8E6kgwgb2u0iInTh59fNkdmFqTpJ6wtXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است. با اجرای این ترفند، می‌توانید نسخه گران‌قیمت Ultimate را به راحتی فعال کنید!
🔥
آموزش قدم‌به‌قدم فعال‌سازی:
1️⃣
ثبت‌نام:
به سایت
gitlab.com
مراجعه کنید و با یک حساب گوگل جدید یا یک ایمیل معمولی اکانت بسازید.
2️⃣
تعیین نقش (مرحله حیاتی):
در بخش تنظیمات و شخصی‌سازی پروفایل، نقش خود را حتماً به عنوان
مدیر سیستم (System Administrator)
انتخاب کنید.
3️⃣
انتخاب نوع کاربری:
زمانی که پرسیده شد چه کسی از این فضا استفاده خواهد کرد، به جای گزینه «فقط من»، حتماً
«تیم من» (My team)
را انتخاب کنید.
4️⃣
تکمیل مشخصات:
کادرهای مربوط به نام شرکت، پروژه و گروه را پر کنید. (اگر با خطای «مسیر گرفته شده است / Path taken» مواجه شدید، کافیست چند عدد تصادفی به انتهای نام گروه خود اضافه کنید).
5️⃣
فعال‌سازی نهایی:
روی گزینه «ادامه به GitLab» کلیک کنید تا لایسنس آزمایشی ۳۰ روزه Ultimate شما فوراً فعال شود.
⚠️
نکته بسیار مهم برای جلوگیری از خطای دسترسی (Permissions):
وقتی وارد داشبورد شدید، به هیچ وجه چت هوش مصنوعی را مستقیماً از صفحه اصلی (عمومی) باز
نکنید
. ابتدا وارد داشبورد خود شوید، روی صفحه گروه یا پروژه‌ای که ایجاد کرده‌اید کلیک کنید و سپس از آنجا روی آیکون چت
GitLab Duo
ضربه بزنید.
در نهایت، از منوی کشویی انتخاب مدل،
Claude Fable 5
را انتخاب کنید و از دستیار برنامه‌نویسی حرفه‌ای خود لذت ببرید!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/ArchiveTell/6679" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...
https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/6678" target="_blank">📅 02:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Awz2UQkLdGqpPNYX-RzLvrX5YX_6hDmgijqXoJE9lajwJ0vwz7Bnf8HAEkBZmj-j_Sm3uXWK4hHpHKpis1JUyTRC3w1W8s61uApXBLFOIlysFLXlQ_PfXoWH3aexchbEwJRzFaEihLwwWvhOcZtjbu-pTMUAoFtcItbQt1T9eGv-421DISGcqTcVJsdVwl-1a_l8y8QBcS_86Z8cfKtb9KWzkcOq1v2kw47tcyb21JX4iHFe0-MhZIy3qhomr1GUZS-Nf1k5UV-1lQG-_f5-jkIQfxzkK4j-8TSOKNuXDUzC_LUZlL2m_c7AcVjbCwLG1YmdBqQXpIGg35o-JbhC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعه‌دهندگان چینی GLM ابزار قدرتمند ZCode 3.0 را معرفی کردند
😮
این یک ابزار همه‌کاره برای نوشتن کد و تعامل با عوامل هوش مصنوعی است: همه چیز در یک پنجره جمع شده با امکان کنترل از راه دور از طریق تلگرام.
این سرویس به صورت رایگان در دسترس است.
http://zcode.z.ai/en
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/6677" target="_blank">📅 01:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8mp_gRVU8QK1bVy3t6H4d6AFOUC-EoCFXvWHGkm9bx2c5Qvj001OZ7VhC88jgbE_heIt4B0r6CuuOLIw39sBD48eDLY7K46CeBWm491-Mp-OFyTPssXKs5nKK0PSRW8U72pFQTcYtmw9C78Ox2KK7WYGSngSIxuqwm34KVdVFrzUsElXcpn9oQaQwK2udBcK4181JZQyqcZ9HKtg-d8WKvVqO5YJ1c6vV333XWGb2isS3VCH-qeolBTC9vDxHdsur6-q-xxc-0iQfhFGst_y8KXzkcqrLXBjTJj71Ud1BkMHAEwiZOvA2x3PMHbHFwTDNDJXRCjqWWOh7sZo10yig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=oJadZAmjRwpAKXAUvhX6trCTFu4-Zlm4_uc6NK9VUGSes00cq_mCCiZc2ZS4tNzAskRRw_LHAaKKxKIVuCgJRXZ7QVd0rk2DY2vqquiWpZvTCNVbN9hHBU3wsOg1ejdjtBfyeEoat2Ol_zpF_T-m53Pxl1D3Z728KP9W3f0HRcVvyeLGwsZgwHjezXbXiAqnIfabqSCJ_v2ap8-7ME7ZJPvxEQkJGci8pK_-QZg1V_iOUD8-_65Zskr82hb1HvaM7Oy5Uw6KfMrvf7i-WCT0u4eO8gqy4sYppo0jr5loatZ39bYNg3kBNG7uQM-OQpEFRY_BaU0mBhbkeYbYJ7zayCJHe_wRhMM2fkUsp_5Ww9QY8OHkkVlSxYkH8DfWfod-pWIgDArpxb8YQYFnTa7WIHTwdJKsKEl82XuyoFhUhuihBPQH0jBh89GBzqoqO-3oJPo9j_C4dc0Umry4Wr9GLGLshCeALZj8aSuOXkvFKI7zfpOgRiIWfdh0ToAgXt_vHkOhkG7hvCFrucOeyPuDIJNcAq8ulnZ0t8V77p_YVu6dpF4z5C2Qg79K93pBF-uG_xRlrwAcWbI3GvRdkeycY2oUvJnKmRGafG44xqAtPrJaRlEGj9FiW0mzZfkCdyR7zRvgTnFq7FKIaLi2fIStxT0zOLZjx0f9G8rxFXAZNXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=oJadZAmjRwpAKXAUvhX6trCTFu4-Zlm4_uc6NK9VUGSes00cq_mCCiZc2ZS4tNzAskRRw_LHAaKKxKIVuCgJRXZ7QVd0rk2DY2vqquiWpZvTCNVbN9hHBU3wsOg1ejdjtBfyeEoat2Ol_zpF_T-m53Pxl1D3Z728KP9W3f0HRcVvyeLGwsZgwHjezXbXiAqnIfabqSCJ_v2ap8-7ME7ZJPvxEQkJGci8pK_-QZg1V_iOUD8-_65Zskr82hb1HvaM7Oy5Uw6KfMrvf7i-WCT0u4eO8gqy4sYppo0jr5loatZ39bYNg3kBNG7uQM-OQpEFRY_BaU0mBhbkeYbYJ7zayCJHe_wRhMM2fkUsp_5Ww9QY8OHkkVlSxYkH8DfWfod-pWIgDArpxb8YQYFnTa7WIHTwdJKsKEl82XuyoFhUhuihBPQH0jBh89GBzqoqO-3oJPo9j_C4dc0Umry4Wr9GLGLshCeALZj8aSuOXkvFKI7zfpOgRiIWfdh0ToAgXt_vHkOhkG7hvCFrucOeyPuDIJNcAq8ulnZ0t8V77p_YVu6dpF4z5C2Qg79K93pBF-uG_xRlrwAcWbI3GvRdkeycY2oUvJnKmRGafG44xqAtPrJaRlEGj9FiW0mzZfkCdyR7zRvgTnFq7FKIaLi2fIStxT0zOLZjx0f9G8rxFXAZNXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOyE9nUSQIeE6no7cGpvx0PVaR0EX7Y1mIeay0A_DOiJSauodNp4JM0br3kZEpy7CLVPsiuTlrz82Iqnuwu1EzGMgp8w-S1tfXId-LCveHFZf28b8Rgp4-5JPZZjEhRUYZquTeXN-9vBN3SgMxaCbH-JR4iOaAJrLg7ckZRJ3vWoV0rsjo_QtnQmAQJ2-kSfDzU3ChycoITL2kWseVgswlKuPhdkjH6x-GmqWnUV56gmXOK8OqUeDqyYAtb8ZZlSi6s6boFAmqYX-yTVR8VDg1wxBPzEZjj5iQbUdd6phvDCxrW1R8jALVJTkpS3Q5wirVKa1KcIiog1MdXTEGw8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
