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
<p>@archivetell • 👥 9.83K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 01:29:01</div>
<hr>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 439 · <a href="https://t.me/ArchiveTell/6798" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6797">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اقا سرعتی slipnet رو اپدیت کنید
😁
😁</div>
<div class="tg-footer">👁️ 593 · <a href="https://t.me/ArchiveTell/6797" target="_blank">📅 00:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎬
FreeCut | تدوین ویدیو با هوش مصنوعی
یک ابزار متن‌باز که با کمک مدل‌های هوش مصنوعی، ویدیوهای خام را به‌صورت خودکار تدوین می‌کند؛ بدون نیاز به API پولی.
🚀
⚡
ویژگی‌ها:
✂️
حذف مکث‌ها، تپق‌ها و بخش‌های اضافی
🎨
اصلاح رنگ خودکار و افزودن زیرنویس
🎥
ساخت انیمیشن و افکت‌های تصویری
🧠
پشتیبانی از Whisper محلی (بدون API Key)
💻
سازگار با Claude Code، Codex و سایر AI Agentها
🔗
https://github.com/Moh4696/freecut
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/ArchiveTell/6796" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/ArchiveTell/6795" target="_blank">📅 23:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromlocalhost(Yousef Taheri)</strong></div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 738 · <a href="https://t.me/ArchiveTell/6794" target="_blank">📅 23:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0akKCHanYEZALNexavN2i3-0NWK6slooHmIYVBIQG7_CCPjXWb3U4AxulUJU4mJMKFhs_RAxCCF5HyKm4aZMwU7mhY6nbWaIwZ4iP0swaOQOjt8lfhGxNcVHc8dD1y9bdiq4zM1sEu8j11CY4m0x-gUn4T-Fi_Inq2Azffs5Z5-UVp9u8A8vd9N0A7IX3H9XoGWgv1P_JN4EXrxKg6VhTsN7FkFJb134js1c-ljZ8j20wZNRDeqN_eLKSLiQ0IKcw67nyxPfC2NVxhm4dMRkq01j85Kb1WWD0ifNHRbeWaLPouivG3pqcz3etAmtZzjUrv0FDolnlDFVneoZ9m8rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Grok 4.5 منتشر شد
⚡️
این نسخه محصولی ویژه از ایلان ماسک است که به‌طور خاص برای برنامه‌نویسی و توسعه‌ی ربات‌ها طراحی شده است.
نکات مهم:
• این مدل به طور مشترک با شرکت Cursor توسعه داده شده و با استفاده از داده‌های واقعی میلیون‌ها برنامه‌نویس آموزش داده شده است.
• سرعت بسیار بالا: 80 توکن در ثانیه.
• قیمت بسیار مناسب: 4 برابر ارزان‌تر از Opus 4.8.
در حال حاضر، به صورت
رایگان
در Cursor و Grok Build در دسترس است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/6793" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/6791" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://878fa338-f275-4bf6-93ea-ef47d8865f59@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/6790" target="_blank">📅 19:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/6788" target="_blank">📅 19:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/6787" target="_blank">📅 18:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/6786" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6785">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/6785" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbOitG-3BJK4dIzK-6QyeeUG45oazu9WkW7Ed-ozqLuM9SUIlSpsbmbSm_pybpCNOYwOvkLlAa6Pf1BdcYrvhVrxzCrgXoUTzEi-zBNuYLw1vkJmArw0k-Mnfb7K-NkxfmXHgOjPu8ePETXXdfJwbD7GTLAajYOm61UXVhKR4g3tYnRLx1HvhZlaHXsXtTIDuPMpnQ1LQ4abhPepjAelkOBZ0LJLYvc0gBduBg97LaVr3rG2rLyFNDqckkIrvvM9B0LMt_OwcYVwWBqbGSU_9HPjOkQpctuJUtUq4F_SSyzOEML0A6ZtFLu6axLr4tpZ9z4rthFWC3zKnwGddWTiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SubFarsiPro v5.0
📹
این ابزار، یک دستیار حرفه‌ای، پرسرعت و متن‌باز برای استخراج زیرنویس از ویدیوها و ترجمه دقیق اون‌ها به زبان فارسی (با لحن طبیعی و محاوره‌ای) هست
GitHub
🐱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6783" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6782" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/6780" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ارسالی یکی از یوزرای گل
👇</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6779" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6778" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/6777" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6776" target="_blank">📅 12:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/6775" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9RI6PQ0N-9Ji9hGYiT6PbLm-ytTUG34EswHLEKPQWOvHJEeWuymvPbwHe-75NLwpKuP5xeC7r8VUHEKCO-rSFmhFBbPk2KTHpDMrZbxTp_Pphpz5gFY8D51AuTo4n6IRw8HPoLEXS7Gz95ScsfqiQMm6g35-eYfQvgceO2e5I0e0rYFJoqag-icxcvmQ80BFWH4oGZMtYJkxbpi3R2J5Me83sUyueZOmnDIo2SG8NYm0KIz_D2Z5d-yBxzC8Mfgt_Bg5V6EtHHuIUhoLPnxpRI0bSuvGAaRHjyU0He-TGl4WEgAHuS-4ktaRj0-bC6Y9x0kT5XAgAvfZN82pE5AZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/6774" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6773">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia462dyADEcp-tQr0qKTLrsLoSTy9YzVkFwW3_Iccexga5cB4lJr4lP81DYc-ZFF00Nm73w2386CItOGTvbGmrCgipjFEGk9e7cNfCKcUpiAQBzMG3qqKy0wN4PJmN3DItQwNKv2X8ZxF53691ymGPWjfsx70pPqWBu1d46vn-FZb8pTIYPxoom_b6PmPL12NzD24zqciUaUIu98sNX4kVsDZ6UJBv3yFtwDFVpvHaDkOifqHmyYHt6UGNeLNAuZBJ_eveSgBp3c5-SlrdT15BjuZpLUYTADy0bxODCElOryiqkxB2fitGxevPZlQJ3ytqt_PgGyY_3fUbkWuz8eMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/6773" target="_blank">📅 10:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6772">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8tNejRDzacInj4nH99THUdoTyc0ezOIERB8ws6qWe-xANmgekvCD5NOX4_FmNYtuSb8S0qJOg81iTxohD1u1X0CXtGADJTF4ijB_tIUMIbW7_nBUntCcmlAqvbybgbh6s85mWlSPyR8hScgv9ermm-y8jnnjez51qqS2Gc0guTZ1qdLpqA3GeWbPurRayHKfm6ZIwd78PPDmQsk3tqoQbjMwBF_VGDSslCeDTiVQt35nMuzIbF69vAwJQZjHiygwHpAFlmnd9mk5Le-DqkeAPJOIsavNi9r7J3ADjzphei8BQkAytglXRWgD8z28ZsF4c7mk8vbJBZ4dQ2kMsUahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت OpenAI
نسخه‌ی GPT-5.6 را برای Sol، Terra و Luna از فردا راه‌اندازی می‌کند!
🚀
دسترسی زودهنگام از همین حالا برای کاربران در سراسر جهان فراهم شده، می‌توانید با خیال راحت وارد شوید و آن را بررسی کنید.
🌍
🔍
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/6772" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlgN-ctkEKWW2kFZRwJldQ4I7h-BK4VSxiElMd_kZpySgKRBxUd6IoFLyqVJC_2e321j0s8t4iRJ6BrcnwFkK7md9K1uTymt9L8A6CmtEBdBo0d4mzovm6q3liZoPobKH7meaVlbC0EDApw38lI4TXl4_THXNHgjNgo1IFsNeTkIv56vNaIKvA5vPPmTKnH2YHR07oKU3Zi0bmip9JW6Bivbem5I5BVcn7nMCzxQaanqGwoIuYHxMh7XzhME2R6HbU2Otu1USbMycgleiZ29zEDzlhvFbhNkKjOSp3QqE0hKC8KV-jb0kG7YQ7wfa7gpoWUVXSijcSyz9NtdhgT4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Constrict ناجی شما در فشرده‌سازی ویدیو!
📹
- ویدیو را آپلود کنید و اندازه مورد نظر را انتخاب کنید.
- بدون نیاز به سرویس‌های آنلاین و دستکاری‌های پیچیده در کدگذاری.
ساده، سریع و کاربردی!
https://github.com/Wartybix/Constrict
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/6771" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLCe6Qj8cA4jmgyG-rgt_3K4yMLUe19Tp6Shl6dq7PUSfPnrafEwbBjcLQ_dSV-hk4y9HXOFLHQ4oxOpdB9zor4Fdt9RwGc4uQJyHe7LFxErDxfrWizijEd7_PJ5YfmdOvFXuAATB2VDWWMr2wqMO6mQQEM0xPN1PUg6FJcJ6So1lC4OrIp75MbJOz0RHqN9FybRXDDoPks1S74o5p4PrGPDTKGDzJJVuffTz0fJUXzvfOZClXzabwoQzudXH05aoqgcpzUlRPwLfvISKM489KfaRfRwaQRgCStUlaLBWQMEULVxRHTzIpHXzU01PEEa8KncQWjJrWKFYfzr3wp3Vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6770" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/6769" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqwSu2BS-9viQXnIBwJm6AuUWweB_8S9bqwerotpN1sRgWMaCJjo63FCBuvYlEpHjYGphz_BjmiJdjEn3L2twqBQuOSlk-KqsvdGlTDc5lO9-eHEVAayBYGA3DHg08l2mipCWSSxfPl-wlL_3IvJ-cvics0Jx5akiPEAVDROTrQt7mkPGcZLDDsj9Tbb6w41AA1G1enxXCLfsIpdqmTn24koGS9ym-aJoR1IXRzQ3w-1fI8NC8YL1QTKZxrQGmVNLw0N0HtyHez7Ln4cJ2ght0WvL0CpgPNvX77m2n3V12j2ujWclQ4ArFTubK5Wqd0sfQWgnTudUkYjP3-TcLaVVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6768" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6767" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snANLnDvPzAN9cyt9TaKnFHXbofa9mLqQ1lmV1jKliVUwxviEaX_bkokqCdne1KFOgQYtfN7NdKV-tbGTyPvAAgFY0e8R7nxPoccR8B8efYcuF3ZAsZ7v9fQc6p8J_54kRJfroGSWU7flYMLQGyAnPsyGIA5cOxQixSjUzSA79_JEC2gThaTDLUc0BrBpG6oDV6dv6dapTRigq8Lrq-nFJRC7fmK70a6pskfk_VRUIug2KFB8y6_Sa9zJzkJCeQaQ0C0XzOCaSvwoaoqc1_mRqyuOaZeG6aQZ4dkBTi6vm-b9hZ0b_qY4756vi-5U-OVCUgudt_oSq0BCSEeN5Y9DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6765" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6764" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6763" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6762">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnfGW87X-epa-F7phdJhtcetKa-cAczkDvLJeAwK_vFcIu1Nyjt5psgdVYebyqTPvt_zZv3VrwiEwhSHDER43SEolag1jtTD2TRtmP6F1Di04ASiSZ26q2efJo_L1GemA-JyZ-rl1iU-AjFI4c_8YvlEOFyBApXYjiZ6f_0hhIjVzM4dPLFhYDs3ajzZJW6fvrHZBiWqbG2lfePvYmNcrsWPlPUdav1iWaS8pLGJZg-elVYVEEIHH9ahViNvB6UlBClUzzIoe9vf-EMdvuEeaKPLlzHZjlYsPF_xJzMtsHQHOqTEofyBHKPYVAPuOdBNs_1C4_B2FkMdjRyf_VWobw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6762" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6HkdilOIc9nHOVA9LTuKuZj68ZBUfH2FrHsZ2BQ56A3NHO4j6mg8--JrH0h1hz6sbn-RKFZd7o5wEx31vD1oNlRMzoWbEMTN2L9iDndzxJNBhv1sjZoaUFTAJvBBEbJOSz6k0lxyvpheNVIcdpJylot5ryqI5XQtrJrv1jwv7ofaErcRTVZ8OiTwMf3zKvISKTj3zvK1rlik4ELXLtnsbTPWk524SM9BaQg4sJMyzGg18ahgLqtPKll5_g_xq1OIxHKNDqlCz24qLgdGa7e9JmBFABQyy9tYhgUoNDSQOH5ljYZyeGCqQN9a2qFRmgmiIy1DGB8LHafhq2UQj-6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به دنیای تکنولوژی، لینوکس، شبکه، سرور و ابزارای خفن علاقه‌مندین، یه سر به کانال لوکال هاست بزنین
توی localhost کلی آموزش، نکته کاربردی و تجربه واقعی از کار با سیستم‌ها هست. خلاصه هر چی از دل پروژه‌ها درمیاد، باهاتون به اشتراک می‌ذاره!
🅰
t.me/localhost_ir</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6761" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HySJOA905d9HziSkD9GUaK16THsQoS-prT-vtNRlR19EMoXgT3gdWDCG4pW2KWTiCAtH7aHd6vBPBBuou7HOy3dLscaUg43vBxOGIXoYuGBQDvYMWCjOzgf5zz7EO4J7Ck9-A4bqnKdyq_DBykM5xACaQh2KYZqP66ec7lxn5JpKbAPs6NicNh8FePQI5WUC_TGTRhakyElvzqmM3_XIbXVXxi5_FK3blwwJSZAYvoXcdUnEmUl2-ZxHvROw0JwdW2qiGZe6srh90c1-BFzrMtS18kRbu6iBFDXDREjc1opTfgi0frovm0RbJLiWzVdoLDRfINBklfTPaey4moBneQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6760" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7xuzzQmlupbE338DsC8005apdrv-1VfABwKO-PdBjWn8KzRNnR_wM7sioSrIt-6zXPPpZEDLIB5PL0olJ9p19jAZ_ucPfinwAa1K39Ohhwi51Xx0b-xrCUuyChz_EasNIaH3rjE7hzQS13h2SgvPppR6nRMyCLqLgvGeVdTyt1xk_nDfNabj1ipEdqyOgLSySg2pL5q-izQwC9zY2nEk7sQwfgAwKuOuHRoLvb01h3r9d_a7H26dm_-I-ZbXomCX4VrERLAzf2PhQ1D0vFgQvZgSp0VK-J0cmymWtRzUEc8tFIlqQjDelhJRrJiIYtiuHQLwbqcmDylbXiZ4Nk9gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهبود کیفیت عکس‌ها تا رزولوشن 4K با استفاده از ChatGPT
عکس شما را بهبود می بخشد و جزئیات را تا حد امکان حفظ میکند.
😮
پرامپت :
Restore and enhance an old damaged photo. Remove scratches, stains, and noise. Reconstruct faded or torn areas while preserving original details. Slightly sharpen the image for better clarity, but keep it realistic. Apply natural and era-appropriate colors to skin, hair, and clothing. Use a soft, balanced background color without being too striking. The final result should look like an old photo that has been realistically restored and colorized, while respecting its original appearance.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6759" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pn1VQZI5dlydwL04c6VyrxdS2f06oyxDyOp_AG_o_jmwln1H_i-jYA6k51Z93P3Ii6yjTdYu2z_ygrq2c0pOpX0Z9HJsNxF5k-A8ZodGy3wBqy82Vde0TAuw_r_2shzOiGNsNZSXto3n8_BucQv7RXdnql6gcYmK1SIZjEd3EespI10FIGFCDNJj5_AbaJN4s8TF8SpzncSsLNZTvAqRljtcYebUHywedzkxzoI04dHrGHtx2HUFhP4IMj4IzxHWehmsRxrGZ4PwhyfrtBsYcrdttToNQ4uWT28rxlsqWKuRcGdead_UpT5u8x46LKMHDI6xdAiBteUfQvycBmnskA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6757" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675041278d.mp4?token=mM1laOtCR1qD2gOHzZqQHnjtfVBW8Bv3hPAs0OBh7JuF5ygIz7K0yyikWx1UmAftX5JmgUlUdMErbsuau8MgEmBMWhQgOZB54IEXfLN7x7kwjgwB7BxOATk-izJWjeDktLyFICSCIXOItGNIW1VytDO-u_labwp3VFzwYq_JZxvewMOt7zUPdNcEqYCUii0O3EDNDvMZHNCLipAMbT79hQUnR38WvDg8yToThiwvMTxXIUhEtnRNPnWcRjYGt0Q0o1rc4fPX9aSSex6Ke-qtqNubfzDIlEaCjVIhn-lsEZ51uRUTndLm28mFKJJdGs1Wmv2ZXeyarM1C5i3WUDFjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675041278d.mp4?token=mM1laOtCR1qD2gOHzZqQHnjtfVBW8Bv3hPAs0OBh7JuF5ygIz7K0yyikWx1UmAftX5JmgUlUdMErbsuau8MgEmBMWhQgOZB54IEXfLN7x7kwjgwB7BxOATk-izJWjeDktLyFICSCIXOItGNIW1VytDO-u_labwp3VFzwYq_JZxvewMOt7zUPdNcEqYCUii0O3EDNDvMZHNCLipAMbT79hQUnR38WvDg8yToThiwvMTxXIUhEtnRNPnWcRjYGt0Q0o1rc4fPX9aSSex6Ke-qtqNubfzDIlEaCjVIhn-lsEZ51uRUTndLm28mFKJJdGs1Wmv2ZXeyarM1C5i3WUDFjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6756" target="_blank">📅 10:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6755" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6754" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E28i9S0L3syniGxR6y9c0kiIphpHpn1LejqZijODYA1tvh5i2546ImXm5QoSaws7-mC48YRKIvXtFgDWKoJ2TXU4W1TumZ6F1cjiatnyM8knzuHJiSM2KItTHf3Dv_GqyqrJT7A7smem1iY8Nr5LuZfa3uEl5RBllvLVxS3gE6eOnvKnCJp8k778ADfJQ94mwnBWsVsHKMTOUpidOEH-upfUERKnaZDHmRa3J5synr1ZxH9XjUYD_7p_ZeSN5UXe4QDB2tTpcVZ6_HKjDu7VRI7VtuQV-o_W4iD3iOovCgNCUjbru_951Ulh6IufnDW0NiH6XhSikSAL0qqLJGw0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بقول نیچه
در چنین گفت زرتشت
«من از خردِ خویش به جان آمده‌ام، چون زنبوری که انگبین [عسل] بسیار گرد آورده باشد. نیازمندِ دست‌هایی هستم که به سویم دراز شوند. می‌خواهم ارزانی دارم و بخش کنم...»
بیاین مثه نیچه باشین و این عسل و انگبین چنل رو به سوی دستان دراز بسپارید
نیاز داریم به حمایت شما
❤️‍🔥
https://t.me/ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6752" target="_blank">📅 01:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6751" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor
لینک ویدیو آموزش:
https://youtu.be/pN3LxWzDtKI
خود پروژه:
https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6750" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6749" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej42HYLF8v4uO3cHiQ3yQK2q4VfrdmIbcQQCuUzoseCdPm5NV9MawGFjcyst7Xqv1Y-6QiMpynFqZ00MfiKPde_KjnuOxCGJL33nR41-qFvpArsAMor6W3fW2p8Tz3aK1rRmgSmngx5vVhLWBrZxpivGvvHMc6eKimsrzHydZ7c2SBZP3U05WRKkyQtkF4O1yOHXkyng41SPuQZdtU3ekly1pqdLdBbFr_iDvJPPyXJCdSzskxD03307_NmeyheDg2O0Z5ez2Adar0oTaTRd-l2romfXnLK3Puw25AQEcmGrFpckdcoD4Y2VZPxfD1ua8XPggv5QF0iAyj0X1VY9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074191361432035554</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6748" target="_blank">📅 21:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsITqtJQDW1pWBEsT_3_aYJ0x63miOVt9rwQJhhlv5VUHeSPdZlozLB8tOrpgnYO3GIEHtMJlTfZK8Wt3H48JH7BXTSgsydBmDpNznGJhihsU9pKuyDeYhlQJqpInF53JnMn9bheMphimGhfJiVEj8p4ucwEwRsBZwVYQfyM1VehtvE4isqxEYuKEUFfhk8-vrVIsU9XFWGJd-jYGzbSYh1tI24j5Ho8jMdodx1DObVtf87bLXfNDZl09IDEQKzIVheii5FgsImULsRYeW22W-UiW9mCrFySmIeT_lFgtq-0qfpohLhB7Teaz0_TmTjdt61ajf_SC7vse0ArD_b7Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6747" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nr-Awyb2OF2zup_QWurCyNtTB9bkpKRoBrQ33VMf5jJv3y96ZrzBbU-arBwHh-JdI6a5FJPtQ4UFtM4_vPNfIeXaxRNcXbuue1z-eSk0_VEWwkpHoGcEEJdnFvCx8YEcHkRMl0hDM6O1TQXLO3oI5BKJPfLuC4lI7NIE0rCxLSRUN7te4i8N0IvlVJomRgDpAJ9T4C6bFuQ9nsxX-k24ksE6ei7iArlNdP7QzM9QLka8Fuolkquz8Zitm7uhy90tHdsoJvplfQ7IiNuwjpN07Geeugf1LxMjw0np8YSXNyJAAM2d960SN3TGKto0MIbGEGxA5vO8VXqKBWP71AdRkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6746" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxZN6ZN2RBQg82IeJwrYS4fiVIEoMFdSOMSslVIGX623SUAFz4c_U_VSGVR3pVN5O_RRmNSszdjFGQpvMtjPCjq6fXVKh8djakwg2LKNvbJkd8SeIikK6aKz0KII7xlp1tJTOiHaxtBKwIVTOm4BjJhM9dQJ2rzMIglMbQHDPCjxJWGd2bJBthG5EdkCW1oTpWXm371vbns4smbFRZwxfMOLJqFY7DT2ZkUOA2zRKkTXQWHZ3cu2z53cEbIb4LL0t1nXNIJv_A6BYCowRrRQJOq87qMx5U06Vxi2PI3m5GEXC9QxJA8AiBYgtMzJtQAGtQvu4jSt-HmuGxdwNfgSnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=XciEsuXWo9iLCiYcr3loI1myIci52F_kaj8IoRrpUc0HFbI6i7kaXqhaAN4-bxmN_YoDBPiJE_bKMKKzWYveHH6Nkg6OgWOb1SKppcT63aEew2NY0gO7xH8TQyqh00Py4uRajSBIypctugzqabWXMsnbH7KvDEz5_UMW_-5PPf6SsMvat2IsBmHzhMDVB7t4O-zwwshQcd7Uv_U0V2pcz__fhxs3EIWyMFJZc4nzmwoB0M0mJBRI5rSb3rdZn9gnGnpkBKNZ7k7r3QQmR862u-CRQJFhzKACkQW6VNmYYYNgkwuniNXZtligXfc6uMq8Lyi46mY6faUy8LNb1jTHkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=XciEsuXWo9iLCiYcr3loI1myIci52F_kaj8IoRrpUc0HFbI6i7kaXqhaAN4-bxmN_YoDBPiJE_bKMKKzWYveHH6Nkg6OgWOb1SKppcT63aEew2NY0gO7xH8TQyqh00Py4uRajSBIypctugzqabWXMsnbH7KvDEz5_UMW_-5PPf6SsMvat2IsBmHzhMDVB7t4O-zwwshQcd7Uv_U0V2pcz__fhxs3EIWyMFJZc4nzmwoB0M0mJBRI5rSb3rdZn9gnGnpkBKNZ7k7r3QQmR862u-CRQJFhzKACkQW6VNmYYYNgkwuniNXZtligXfc6uMq8Lyi46mY6faUy8LNb1jTHkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtTpbn08CCy4GIWVXMF9AvecA0zCxyvXO0ys7IUACiorINEqsLA0I2MBJH7m0rtlTKJcV6AtdxAL0DtaY2UFvUiGyFjBusUU4MEdvvsQ5OiQGgClz06MVoGT-bUVMJEgdpcj_vJ82B21f-Y4uU0PyG1-x2q5jo077SAFCj-FNfkRFIcEwYqfN8IWz3lmZh0O5kpfOa_IlxKtOBIhB-zOl0JlF5-pXZ_K_TRAz70HqBPab3aoBMaSEUJLXcGGrUE8IS7r42djQ_ATQxqbs323Pp0Ok5_KnGoIr1gNdNe9NcPKSfQ1N4zZe458dNGrI6HxiFsJyBNHByQ5cqfdujdmWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6740" target="_blank">📅 12:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون فضولی میکنه. یکی میفروشه به دلال های داده (مثه گوگل و مایکروسافت و...) یسریا هم که حریم خصوصی محورن.
الان هرمس اینا رو واقعا نمیدونم. هر چی بیشتر این مدلا رو بیشتر وارد چیزاتون میکنین، ریسکش بالاتر میره در کل. باز این شرکتا اروپایی نظارت بالاتر هست ولی نمیدونم طرف خوشش میاد از ی مدل میگه به به چ مدلی چقد قابلیت بذارم چنل، ملت کلی ویو میزنن استفاده میکنن. طرف به تلگرامش و... هم وصل میکنه بعد اخر بعد چند روز میگه ببخشید هرمس رو شخصی ران نزنید
اینو میخواستم چند روز پیش بذارم ولی گفتم ولش. ولی حس کردم بهتره بگم تا پیشگیری بشه بهرحال</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6739" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1lfVG7QJMrmuwf-FKkZEX5PFY0Oa4qoO_bziVPJNWkA7AQlw1Mvtm62jxOsBLhBHyowv6c0Va_43oUE7NYlDhjY8Gz6i11ZOa-YY0VuD2ivGjYYT_lIwtl0YCgjSWsO3-1Mxse9PX3ya5oIeGwRUDoe6zZXmpLZWAfMpQaZf2okFqF1tAkoUEco_4cgMLm571Qt3DaAV7Qr28WeR-HMogUypI9Ny9InuxqdjrB2wCmJpeakcYX65oh9KCJrd3QCiECWHq8Te0OAEMblMXsEmwvUPze3B4KA1yH9bZ2iVhKCXUMWZf1y1aDko9fpOxHLdWMbBMAaWJXgF1oQjdvNXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074039784629014892?s=20</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6738" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-vZDz6S9iJdHqx95_G6iZWAc8z91LWEj1uHO-GWQ-DgWf1rDRv1unPKvSqSOM_odtVd8Uz-N_KgeYbKRWKjTAEMutLOcgwKzwAO8V_1Ev9q26kTWgxFOQ9htmwwElG_asFeI8rYdqqR9Z2iLqxeInLgcL-MR6yMlceuTTVcX2aFvmRtSzxRudEyMW4m-6e03TTwrQEJ1nqegDldSys42bA7xgiBLI1-9Xxeu_WkF_5ZJQp_1TtTQVtJ8RpNawACNdRD3PVMemizdj2aVs9Bfrt3iE8Q-h-bg0vCFlYXNJdOEzdRlHGFLjEc8COnBU9pzZOMXvo_DFf26dn6QWKmkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6737" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBow9fvZxGKkhMVpyzKjBhVOZZL97_qTtiyukFxxFVfE2CRDaSxMqQ_R5NDJhvMbpy10K3JJQrgfIOnCqTILGvhzE9JDIuElb41uzXdWkrvTnB4B6w7a3QfX0TJGJkIve6BOEiB1PwehRyfUGmyknmSBnXOCHEvgvEoCJVIvkzFJP8DoVK-K6QfjbAe8Alwpp2HYRKxVkiN5wzonCsQtL0bHcjav1_T5i91fQGr8AF5DymIQrqsP8B1QM1n0tOgAS7UBJbFE0a18dXTCuxK3qfODhN7PCFbO2ELU-TSoXyQ9_iotTRiryouz75Rv2hJaMtObTRf7h1jUYSAG64fbkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6736" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6735">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMSj-5H9yUgi1F9xDYArZk89MppECnGATWSmPpCaOzlsejDcAaH5bbzITMMMF0lV65jJsqrs-WK2ionJeYh23mpfOn-60-bJHtF3EQzfhglrcmKwyyWjJR-BuxCejmbvgmGteBCK0XocPZjiJ4zeqnXTWeH--cUua2IN1gMtgWL2o-VbeyYE8gvPGfHUR8_Y69s95hvufAvBrPeNe2xyo3EUEAll6YAVuBQYtBMhY6noiQnsBO2hy8cxYG8NE-TeJ1iuwTsWsq8XNXDF5-goc2NW4hs7OFzI7J2hp-ob084ZQVpb8ozzLEnt3braESNuq8Na_CM_Szqx9ChyFcmVFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6735" target="_blank">📅 10:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6734">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl2WYA2r2JXYyAXLaQGRIJdBL7ViB4lpEDuQdGGZ3acXMYtjdGKO7S24wFC-M7Nju1OL0fQS2OAUcN3cbztlXyKOfSHWG8bTCA7jCJ77pfVl0ds-2H3FLUQ2rKokacGHuxOoptNAVqu7DRDOK2z8aNZn0PM6CnbvwtfR28_2EmszK377AHvYYTncrM13xfiowJ9f_0s5k9C9-VXyt2DgkBzGNMQxV-9eRSTMQKNsjBBvoY7wCkU8t1h2Wf040XezW4deixgtz7dJyZvu3xfw4ARKvkH4GavhhqKaLbdDzuaT8MKUg1K2mHsaRIzG1itUOFKmxEN9oXoUUkprfCbPrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6734" target="_blank">📅 09:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.  اینطوریه که ازت آی‌پی و پس رو میگیره  بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ... خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌  دیگه نیاز نیست دستور های ترمینال رو بدونی…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6732" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6730" target="_blank">📅 01:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6729" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6728" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6727" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.
اینطوریه که ازت آی‌پی و پس رو میگیره
بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ...
خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌
دیگه نیاز نیست دستور های ترمینال رو بدونی یا حفظ کنی. تو فق به زبان فارسی بش میگی انجام میده</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6726" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">https://x.com/ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6723" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دیده‌بان لیکفا منتشر شد
🆕
افزونه‌ای برای مرورگر کروم که هنگام بازدید از وب‌سایت‌ها، اگر آن سایت سابقه نشت اطلاعات داشته باشد، به‌صورت خودکار به شما هشدار می‌دهد. متن‌باز، رایگان، کاملا محلی و بدون ارسال اطلاعات به سرور
👍
Download
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6722" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5VYJLJXzXRw_Cc2J4U4-PS2dOZ9Q6aUBQLMBN0n3KvL-Okq8C-c11i8tDAeYeE5AAKd_0zfFx9SW2NVPcUVYfObpySbNIpy_xpAWGYutdVgsLirUqXoA3Sc1FmXVfoK7_a0NFuYEq8tuVbHKBh1asru1h3DZ8_GAd1phiPTpGKaD9gQybS81QTugDEdMHjQ8zq-BjCOwZgYHAwJoaMIQ0_AO0Lnsygw1mCQsxqRUIt8OJ4MRugsgsOPad_8VsmR6QvVi55Td1m0ccnaRDjHjoRrSKOqSm8Pv7402J7mcPqwD3oMIPvQaSqnrDSCQMTW2EmL3bvt8jwVM0uRohOsOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6721" target="_blank">📅 12:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6720" target="_blank">📅 11:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=PoObJKbQ3mj-5ysbFa_2JZyhkxPvVduRdvCvPGr-EuX0n6EINstBmup_vUl1ooZ5DS0jzmrSwk1x821afytMFBQUI0pWOlqEIDoRR7rC5w0brXFm9_EJh84qCLxYYnszPOBIudpIvUv37FM5IwilS6Zexa3GKDbyEnv5Ioph1qFTXFDN-mSj0K3mQ118MWEtpReJCrr5Z1upKPbOQgGSD4WbacFuGjMvn2gNUgmUabI-25Muu6V9mJuRJPJ_br_xw8_5T2TrwrmMH19gj0PujUN5J7Y-sywExGu-zOJ1GJzvDs4f60ARly4w7QU5zhfO_6gpoe8asv4cb1rnRzQW7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=PoObJKbQ3mj-5ysbFa_2JZyhkxPvVduRdvCvPGr-EuX0n6EINstBmup_vUl1ooZ5DS0jzmrSwk1x821afytMFBQUI0pWOlqEIDoRR7rC5w0brXFm9_EJh84qCLxYYnszPOBIudpIvUv37FM5IwilS6Zexa3GKDbyEnv5Ioph1qFTXFDN-mSj0K3mQ118MWEtpReJCrr5Z1upKPbOQgGSD4WbacFuGjMvn2gNUgmUabI-25Muu6V9mJuRJPJ_br_xw8_5T2TrwrmMH19gj0PujUN5J7Y-sywExGu-zOJ1GJzvDs4f60ARly4w7QU5zhfO_6gpoe8asv4cb1rnRzQW7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6719" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni3seOmD0KRSlobzDBS9G35DWzZo2luz2Kq2FetmCqsJqz297salY5PAZezgxo9NKAYJTaUrVpzyO1uPAEgiNl5L1eZ2J3uxY1pGkFk3Zi2IYpruhLV53UGiSqYiX5vDojDDpbU3D6SwewMkH41qNeSfHfrNaChC5ka7xmT7Djc4uGby85fVMXfq4SfWeEL-vTGwkLtuTmrR1jRGlwpzy9swBgHOispSeYKfsB1Tfh8F325cbBofCkxIG7-ICUX5QOVwE9D6hTWMPe1o0oof2EvyT_YtXK7Y9N2ToGnyzyU9ZE5nWJtZwfVA-afiZyZBz036kc2o0NrOfe_N_RTDfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6717" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6716" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6715" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=nj2kR5UkU7FMNYM4ylPRmSw-DPGB4SDhV_WhwZB-N8HVjcroIU_GNosUajfYN6ihQSn6dAmz7--ZgXtknAdU7mKbnF3WcdHqCALrfVgXqLyddZAU4khwK0txWBIA_MoMBeaUeDYzhPZfZYje7BXM57fVNwb_xifBZYLXq60pJ8l-Vl0vMapRwJ_aTmqCAzAdwvNtX4iWuW4UQG8urfdqM4vRkjXMNOUWPnhCU48QQwY2NaG_NC_d7KAqCNZ7ZxZ4UvEmu98ZL-50rYLBh1kwtvE0HJJGy3Nok67RvcpXkmx1AaurAZTEkM8tyO3jDdiuhOCd3jct6mi6AvmX19_9AXUtKeDAgcGbsjLzRhK0TlFzbeOM-NV18rVF_4P5A0pcq-gvBFoUJFW0uOuQUlLue6VPiFW5jMURJAKaeg4xk9wXBaLG6MLVzI-nUVg5AnbggpDFM2BIPLCSdpMRY5RqtlPcxvAU4aSNpm2wek0lfC4B9XEh9Ba-nYs6eGuPDqHvEJu5hdPEy3PfHIId3kq_7T1SwoDkQW0K6SwZMCowx7_BifQMs0Q78z1N5n-vOcpvamcJp_saYpsh8zUhA-1z5CXa3QBla6XyRBmmlMtGw3I8Y1HmRBMByRfgNi3KnRGq8UhVKCQQr4gottOtddVvZRMnW6RYMkjlPGCjQW1MS4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=nj2kR5UkU7FMNYM4ylPRmSw-DPGB4SDhV_WhwZB-N8HVjcroIU_GNosUajfYN6ihQSn6dAmz7--ZgXtknAdU7mKbnF3WcdHqCALrfVgXqLyddZAU4khwK0txWBIA_MoMBeaUeDYzhPZfZYje7BXM57fVNwb_xifBZYLXq60pJ8l-Vl0vMapRwJ_aTmqCAzAdwvNtX4iWuW4UQG8urfdqM4vRkjXMNOUWPnhCU48QQwY2NaG_NC_d7KAqCNZ7ZxZ4UvEmu98ZL-50rYLBh1kwtvE0HJJGy3Nok67RvcpXkmx1AaurAZTEkM8tyO3jDdiuhOCd3jct6mi6AvmX19_9AXUtKeDAgcGbsjLzRhK0TlFzbeOM-NV18rVF_4P5A0pcq-gvBFoUJFW0uOuQUlLue6VPiFW5jMURJAKaeg4xk9wXBaLG6MLVzI-nUVg5AnbggpDFM2BIPLCSdpMRY5RqtlPcxvAU4aSNpm2wek0lfC4B9XEh9Ba-nYs6eGuPDqHvEJu5hdPEy3PfHIId3kq_7T1SwoDkQW0K6SwZMCowx7_BifQMs0Q78z1N5n-vOcpvamcJp_saYpsh8zUhA-1z5CXa3QBla6XyRBmmlMtGw3I8Y1HmRBMByRfgNi3KnRGq8UhVKCQQr4gottOtddVvZRMnW6RYMkjlPGCjQW1MS4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تبدیل ویس به متن تلگرام کاملاً رایگان! (بدون نیاز به پریمیوم) با هوش مصنوعی Cloudflare
https://youtu.be/Xq7e2k3qlqA</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6714" target="_blank">📅 02:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوستان وقت بخیر و خسته نباشید
این چنل زاپاس آرشیوتل هستش
داشته باشین بهتره
❤️‍🔥
ی موقع اگ چیزی شد...
https://t.me/FOSSArchive</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6713" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=ThIqy5WUYtP1DE22PVm5yDiaD7wgloyWcZXLGZ80xJ44QStKfzDOwbq-LBcunYmzMAv0lPCyBfNy_R2zegQgHrU9J2dWNqRx8AandWwk-2ghmOxbQXGyHCHPaaHYCF9WX6Yr-FkMIbONDwv7L59wQ93Ey4OV-QzaGpiJrQdjg6RJp_VFMIIc3uolk_YcNf3To_Ucdg7CtTpngsLVrvDkZEb3Baw95juBlJbCziCEn0MtsgJd75dN2xn6SHtwcks6Ty70iQAiCQagXfH-h7dpri5LPZFD9LKc3TlIhuWqFPtQ0TgtFrxb1J7eBNngdMKyx3kCtqZn9VYwAqx-4u7ZXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=ThIqy5WUYtP1DE22PVm5yDiaD7wgloyWcZXLGZ80xJ44QStKfzDOwbq-LBcunYmzMAv0lPCyBfNy_R2zegQgHrU9J2dWNqRx8AandWwk-2ghmOxbQXGyHCHPaaHYCF9WX6Yr-FkMIbONDwv7L59wQ93Ey4OV-QzaGpiJrQdjg6RJp_VFMIIc3uolk_YcNf3To_Ucdg7CtTpngsLVrvDkZEb3Baw95juBlJbCziCEn0MtsgJd75dN2xn6SHtwcks6Ty70iQAiCQagXfH-h7dpri5LPZFD9LKc3TlIhuWqFPtQ0TgtFrxb1J7eBNngdMKyx3kCtqZn9VYwAqx-4u7ZXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6712" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423195fff7.mp4?token=FjSmzNgXFzXT4u0J7BCn83eSvRtNCtY4fjgLvBC3da5ynio02MOfPmxvn7_DVzBlXTaL9LXGBAwShoIxEHFObTbf0hw1ywHZTHfuN4Jk5BBr7PpgU00h0zQ8ygtcNPefoRFkKcI_oNv6gPO4xA4Tvt6H3cXc11jw6mQsf5__k7AkceQOHYoRxF0LfeN8M0FWkMC-9e6vo0l5_2aLXBB0gOO6Gsh-hAXdBBqPu9cXeQGlk5_Fj0xY14ydsVMpKexULK3bMCE1sb33SBKsJyJCqq94ZGZ0zEgb3STTiyVAzbb_nZF39k3b4J_vyovNvskYGsg7_ceaaFIDWQgfXT0gYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423195fff7.mp4?token=FjSmzNgXFzXT4u0J7BCn83eSvRtNCtY4fjgLvBC3da5ynio02MOfPmxvn7_DVzBlXTaL9LXGBAwShoIxEHFObTbf0hw1ywHZTHfuN4Jk5BBr7PpgU00h0zQ8ygtcNPefoRFkKcI_oNv6gPO4xA4Tvt6H3cXc11jw6mQsf5__k7AkceQOHYoRxF0LfeN8M0FWkMC-9e6vo0l5_2aLXBB0gOO6Gsh-hAXdBBqPu9cXeQGlk5_Fj0xY14ydsVMpKexULK3bMCE1sb33SBKsJyJCqq94ZGZ0zEgb3STTiyVAzbb_nZF39k3b4J_vyovNvskYGsg7_ceaaFIDWQgfXT0gYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کتابخانه‌ی معروف ‌Pad Shaders⁩ (منبع غنی گرادیان‌ها، پس‌زمینه‌ها و شیدرهای خفن) رایگان و متن‌باز شد!
🎨
✨
‏دیگه نگران لایسنس نباش؛ می‌تونی تمام پلاگین‌ها و ابزارهاش رو تو پروژه‌های شخصی و تجاری استفاده کنی.
https://shaders.paper.design/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6711" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6710">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6710" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjo9y7a57C2HWg8AEN8COOGa686TdZ3xNulQVeu62MxhlK6xnSw7tqlZc9r96ATaQc_GUmFdkPt5sPk6gRD_3qhRKeWN1hkdhGLyFEUBP-uhUTGRRzqKFmExrXwgblMf9e-oxVVVsVvZDw7kFMb6CAfDo0HtiF4ameckc3SHDmWJ1AcuY8gYzhLwcF5Qlvc0Z7NNG8hbprdwZ1t03B049LfY1LXrz1ik1d5SUdUgtTL3q3YiKNlxdt7UDEmQpDW90o1mHymP4d7TVpOjyGCmRk3kI489mLO6ioDXmXNTIgCf7HXhfgHeOXVpfl5nbYzS0hPBgnIhGLFX09dNyiszvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5
هوش مصنوعی رایگان و قدرتمند شرکت انتروپیک
10 دلار کردیت
با لینک زیر 20 دلار
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6709" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سایفون رو اپدیت کنین خوشگل شده
🔥
(نسخه بتا)</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/6708" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=pDvMif5xW_-UsueCrIrH3E16WKFgIr5j1wl5YBScpr0O7kcI37ZRkZ5OTFq7wfXJYNJqAC7US6Z3h8yHhXMbKSLTgMe5Xn4Urj3lZGuVXGTN11ZeX287pOItb3yLYPRsLHHB0Ewfug427QSY7LvBa76F9q4YvCIKB27hd-Ey-c4F5yG7gCFWP2hsX8HKOTnDk5yLHWiqwEFhNvxwz0qIyONrBSTZzehEeV6_eAwecbMyol9tcvSOh8py_Np71ezX0W0I0hjs-ZG6axTRnA0V6zEBmXO0-EJY8hUlsdY79Q3BrcUGReEv5AZHyJt3iFaFz-phYunITo0sWqtNto84YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=pDvMif5xW_-UsueCrIrH3E16WKFgIr5j1wl5YBScpr0O7kcI37ZRkZ5OTFq7wfXJYNJqAC7US6Z3h8yHhXMbKSLTgMe5Xn4Urj3lZGuVXGTN11ZeX287pOItb3yLYPRsLHHB0Ewfug427QSY7LvBa76F9q4YvCIKB27hd-Ey-c4F5yG7gCFWP2hsX8HKOTnDk5yLHWiqwEFhNvxwz0qIyONrBSTZzehEeV6_eAwecbMyol9tcvSOh8py_Np71ezX0W0I0hjs-ZG6axTRnA0V6zEBmXO0-EJY8hUlsdY79Q3BrcUGReEv5AZHyJt3iFaFz-phYunITo0sWqtNto84YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت 10 تا ایمیل رایگان با ساختن یک ایمیل اتومیک (مولتی اکانت)
https://www.youtube.com/watch?v=XHJ3TwrwG-g</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/6707" target="_blank">📅 03:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDyZpgXDUWEjN7r8nWg_beAdrKJSVkHYF1BDqjeVXzSOzKdTDITCIXE2cBDo0a1QLeoEzNZhCruk73YIBIiweXzvkKlQEkuz0vBEJEeBDQaanE2UF2Mw9QekfyjQPoHAM7UzjRDl8OiV42v4fV0FNjRFyL9y78-zKHtka8OiViG_2ww7Xi-oBFe3htYet7FgWBl9G-s8cTKue0U89pqBSnuXvCfx-smqs_z8QzZGnM6tZDrwkedTkMdY6bVhXerXlF_0Of9Lr__pNpV6XQ2IGBvkGXxIsTLOFfuRMEdDdLiIYylOzQ_fkwnBdchkH9ogv6RMryPmvZurmrW2cetIAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adlXcNVJnmBKOSTSJicIcdipGPX5vIu6y_r5vIDfhHtV1aPA0Mt3ka9Pxy0Pz66NtBulD3vgg8h1-zLuTLQ9zcsk8ft-Ku2e2lcdnVeU9lQeTJ0wjehddIiAqkQ8ef4r5qILe3PFSnnQvB-QEntVp-9NLNeB2W3H19ydVehfytbdSm69uWdqtsKGS3pYOA_jRaDWDN3orc7sR9ep46vbRjxIOdqFGn2a5XpOb0Ar6fMuB1Mnc7yFTRaLr_tw5daEMcS0m1EvQOUHYKTKnDal_-VqFaKQAo64LW9o_Kz9JEKFP6oRRLwFQXuO2CC4G8NjX19S4HMt4McTTTON7Hk8IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/6704" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkczaJC6_MHeKfCPwazyDgGtFelsKjV1BaquGPmvJado7uGiFaEOTJHf-sfwrLo9xIUhnTE05obKFH0scQAUMUqj2lGLOTCh4FekNTK1msrccNEeBKtDyeiqYcvM6-0xQzpmODbws08Drc3UGCoP1HLP-UsvrTrcnANms2WcyYOeeMBGqnzg0WrbqC97LkRiJ_vM3KjVvUxLDO0c9Hkp5En4c9dAjg4B2O3dNVSTLR4vFpasfNMgd_J3fBjGs-VvCE9EHS84aabTsDKH-q56moUfkAGCDUp24QohJPfpSRXca6rrN1AQMC89mThONUSNSKZUO75zZJ2b5C-yvCmDjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/6703" target="_blank">📅 22:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzNEKsrOVaSlbv7FgCuxqj72yLMwRIrwFNLjPnYUQzV4HYQqi2Ze0yJ4dhnOfK7yWoiht4TPxHuTuqreFaHYglXKSZtVWpZv35uNM5dvNI1OJlzqWwrYYHdRxmmw5Uc3klxxhN6uWVWNU8LWh-BTx4mkgm87oHDZB3MYxTEJOhrxhf47BHchvcmc8pfM3Km63KamJI8kF4vWn-riHMgi2h_XQYwjBDz4mH8Q3_EXnAwSsP26n-ApA3sJDJ1d5I-fQBx3-GatVS13faBbD9FjMIKUT1clMeF0O9I7BPB8tuSEC2nWjJWH-Sev0BAU1oBI5jogwIFWCs1qn60T6rj3LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا پولاتو چیکار می کنی؟
پولام:
به زودی ۱ میلیارد*
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6702" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRZXVPxl1jss3Jp1tA9GyQ153ebc_uR_LIoSiunq0bLAmnETHTbVth98kyE_jtQ_4K3DY4X0QXoqze6eH-2BGXsyh0uNhTrIm3OiP48XCseaaPjDZew_GQPVX00FyNJjmX_buBrZf6paQw1hoL_yKrwlHfm6E1RBDY-9uyg76vIp-R1q7zdzgv-833rqdbIquE82YubWbLm-RXqcSHHfpLIv1fcPiiTAHD2MPY3ll3oew72U8ujLamt_d2HcWkxMFWZEvd4VmOYktmLwING1zc7AVVA-2bb_D09U8uKCRsppFxW8rjV6xjnQOyznUJmX98NSOjhKXN3nXdoCt1cAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0m5Zv9AYJ29yi3WZ219TqdFNUyqxXssxROq770HG3nrD144j_X7OFgV2eSfd8hJEJ6ePiUVqJlQq22BN2ApZE1Z48ahgNP5Pxzb2HcmWmgQpo-QxdjwngFgkzhNtnMlvyV1bFB18VmN7N5YPTG6-Rh__lGhn9pSxJTPfjAerCLF_L6I0_l8mgbAJF_Swb4jxHUWwym3ToTmrKOzqtLRDhpKYHp37EFVPgwZhNpPb-Q_J0NRde-qev4oOlqKZuqFL_4Gt1dLkzaNYL21IZGyjQxJKmUWMoQFIyDjfxu4g1Lsf0rI1AjK47Np1eUvC7JAjCytBaU8AMaDmF2_nRJozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMxzSEHAAqsZwYOcea7XpK8E6UptRKTlU6E7Cncn86N6Btzny9xsYd3AbKRa4UA7tYjoVeT7vVfuycIiAfHXbKedQhCubnaXzk9EoB3Mk5hvmTCNStk5kL_-GNzhgqH2DQ4pT0y6vj7YpsTnNGJQin9BSVaECvmsw90j0WyQBqaxy2HY_3AH0pE4gsoZmfTsLz9yP3q5mYZob40kpu58QtK7UBV5peWo1c7MUcLz63OaKjPFmoDZcfsfqYOo80ArlChwxjKxm5VB19H4P5V6yrmWRN-0onyxkVbyQAwPBhrjmKord3WM63c4YLgD12CGjwf56z7pr0fK3hcigtKZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcacP_g4X7x56INP6kblZkhfdn3AkJvvuucb57qIDsq0oXNV61_HKriKC583_PzKHpojYaXWPWEJcr_KNNRH_xMoFjGwW3TYVADFG5ckk86eGab2xYtf3wHOF81stclJwEQYrngTzVwWRdslC7W40_wSwIV67UoLBXWhDb5z0TuMgSi5M7vZPUc1xZkAmRfHr1V30MtZi6RJmWqyw-xPKPzNT2lWud2q5eAwSA11NkAyqjO-0lCh1ifAvMhwAMD63u633przeucquPf-2r17WKKX6JoRrWknNqHAf-XI59KePTxFLtnjNf4MixeWyrJ5NXbPA34nnNvKv7qz6rZSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNcGXxf8HXYayZ5OlAxq6F1JccP1HWr8fCxqCZiu_DuLfNMiURcUCoPOoWIqq6ggDb5pcq_Dslam-8ppUEbbW7bkP2CCXmQ9IeS_37GYZN9DmR6OIJ4sEUnrmbo8Nmp2g4hlmV_OIEfznmXB8Yz_3nJZ4YZwL3IhW5wg1FWIBJiw4RB6urqZeOeCj13N8S4YEy7FsFaSwB2yoYtA-ovQ9pDHvecZdhZFyoN35kA911VtBXkSavBNQG7vT2-vgEO9RBi_FHQ_2XLCCVvMCjvdSimuMfWMaG49k8oWFv4CoBByw3AWe1eWDJ5pzycwH1A70YepgzUeaZwbhbe0DrcKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZQRpYqRW4kt4xLdTSvNrMI9S-NxJ7W3P6KWa6f8LTBUg-nQkt0m3OO49wcpV1JhKgMhbrgqo9YmYSwXV8qJZ0FMN0bZ29bodnUBy9ezcZCJn5JHZlBitgtfoGcx_Xno_NzOg4rMlxnNlmXQ9tEkSuUIonKs9MKUTryVIguh8k7lxZwcBIigQ5nlw3Khy6gNur_N39X_eenJ5wvW6yrf14WmzTeT9xdcjvhb3IsZue2kmV2WYc9ghxLfV3BRkvyUQ4gWjhve6nYGp-SzUY1BUn1r_ZJPuPMCL6Kg7DNrIPlaWlkL9GVhks3gzLL932Ag9gudR8BHwsxdFBd8iqSViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhMdto64GiPGQG3dGqtYSBk1UZLmmGbzBdS4KGCLR5zm8pC5YPlTrdTAOcBCJuILeMAvB4rVwKu6ElF3nzlnfsAiwhmRy5J0aSADIuSSODRdjGCRwidh5GZyHDfiMUTrAkJ4XrjY5Brl-KxhuWQrqjzVA8VYSxzyWOcwoB0Jc_5mK_yQ5F9jkaHQWovJtMNLECE1WKCXPylWVonFszoLeJkG1-hW23rTM5NmImxCkTH5WvPYvpUs9rbmcl2HIGFRGs8du9_15vInC3p-YeyuuF2S_CiTBesTWaEOgjix8FiT-8eBkwET7MGrgiALpFsB_gIlsOSXwfgruTaCyoIz8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج
جایزه عکاسی با آیفون اعلام شد.
در این مسابقه سالانه عکاسان از سراسر جهان بهترین عکس‌های خود را که با آیفون گرفته اند، ارسال می‌کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6695" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJCXgf4CPn3PRz_F9vJvkQ56pBcr57HgJQspgHeknwdGAJKbP-RyX-zh-ZBVcSSyg67LjAgA0C0l9ndC6K5-1XSo-PzhqXqROOGHBDlaiBVHvzc4eze_rzceRnDPD-fvBRuV86Q3_YfdekOs5X6hzPI-jzMUim0JvXTCfpv9HX3wCZVPMIUmmj11BqDfsez6Uhtn8LeTxSDaMZfVtHgGyp09GbURw1gpHulNk2gzHqWnaPqRynhdP0knS_H18FX1LagWmTsJQcHYtBb4dBsNz098HgNKuPM83bZoX3lD3rBhWa__Evh1MEaylbDD_gSDD-5PSz6gbMuaR1p5nOycmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AITwitter Generator
یک افزونه برای تولید توییت است.
این افزونه که بر اساس فناوری پیشرفته هوش مصنوعی ساخته شده، خلاقیت و سرگرمی بی‌حد و حصر را به حساب کاربری توییتر شما اضافه میکند.
https://tweethunter.io/generate-tweets
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6694" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW0CGH7EjUawcgCVpzZoNLGiJ8rIE2BSDyLJm-qO-qEGUSJ8WTS6Aq4YE_xKA4CiWYvmTGaPC_HvdfO9Ix921EgxOhMF0QonbgtJUbvcWm0ubYp247WhW-J7YXUn4hJeCphWFNlaY-wgb3VX5vWO3yBdqkLqACtfblgrumUgXsTX2zHMEa9IDMeawRdavR3hZndGJPKxDxqFI19pUI5Inm8-1uYZM-eo6Iqjbcc_-aB01evLJVbgv_0JgIhzffQP0LfkSYCzCLtAISiLVFmZUFqF9Jlw_GXufXuUTsEnZ2etLNvZAeat--Dk4C714EJIh9kXY6CJ29pg0RzJgL4Wrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک مجموعه‌ای رایگان از پرامپت ها برای Claude ارائه می‌دهد
🤩
این مجموعه شامل ده‌ها راهکار آماده برای بررسی امنیت، رفع اشکال و بازبینی کد، خودکارسازی وظایف و موارد دیگر است. برای هر پرامپت، توضیحات مربوط به نحوه عملکرد آن ارائه شده است.
https://code.claude.com/docs/en/prompt-library
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6693" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjF-p2Drnk8bAZIcm9d5SbSSm2OzvB4MdUS-DkXNcD9pdvTtQ4dDUYXRoHSSGevGYuWlsgG2M6TcuSqzs8u3srU6emQ9y3oYHp9irjZprNiT0pb9X12Oq9a64Bu_x-JySesLOY7yF88V_ogmkCt6bVoqKXoZYw_5VvPXO6g_rTUfdTWEr0HPHky38VmUIV9c7kdJ3IS6Ers3efVs7yZNmgvnkZOqW4eP4fCOWcjzqxbf0Fbg7TVA7QLsm27wf7ThGnejhNyuQepLTg_pbO5EX8JSG7BwrR3P62BRkiJ-hvNMFtod8Tp0g2WMMZYeMieQS46PCgYBfnW2OJuUPK0NEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6692" target="_blank">📅 14:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/6691" target="_blank">📅 23:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=QApMHbn58w8AnigEpD-qiNBrYV7tHXvjOPZ0jD1lYi8OO-bJGcD6dKFOmsdUOTYgFNIEALBQ5q8cxs77eIkJt9mKDjhyjY3v8CFKe774OxaEgwhh_k6K7EfDmLNOX_FwrEStS3lECNG6Jm3dx-T1leEr4mdru_S7ntsEtVWweVKzuskv-qkuh7GNCUe3e2OaHAcyVeVyEvE5yzp0chRIUnIEQs5PLGZkHh7tzstiys3ZfrT_zLtfBNRjrlLBlmyO-TgHn0lcLOCYz9_854Q3I-2t9hHcb2LF22cdbljXQVIDDJKBkt7yFbbjAf9N5aUkgOIEy6DxalUcuzRDdgY7uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=QApMHbn58w8AnigEpD-qiNBrYV7tHXvjOPZ0jD1lYi8OO-bJGcD6dKFOmsdUOTYgFNIEALBQ5q8cxs77eIkJt9mKDjhyjY3v8CFKe774OxaEgwhh_k6K7EfDmLNOX_FwrEStS3lECNG6Jm3dx-T1leEr4mdru_S7ntsEtVWweVKzuskv-qkuh7GNCUe3e2OaHAcyVeVyEvE5yzp0chRIUnIEQs5PLGZkHh7tzstiys3ZfrT_zLtfBNRjrlLBlmyO-TgHn0lcLOCYz9_854Q3I-2t9hHcb2LF22cdbljXQVIDDJKBkt7yFbbjAf9N5aUkgOIEy6DxalUcuzRDdgY7uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😂
سووو رونالدو با رینگتون های مختلف
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6689" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6688" target="_blank">📅 22:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6687" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaZGLYLuynfYbUGUN25k5adZPVccOYxpJMVxCg63_PgxG2HB1dKAjbXWj8CEC6XR1kXXLlf_U9Dy6KpXvbdKW8wQwsGQx_v55I3MVc4oy42ypLu3QlKHb14KLdB2Bmgjvxuk4UO7m109RMJHV3khiO0qdx6hisrXigI1XLIl8X-m2ffUkRKlIjiJk_dk0xm40IIPqEyrBWMWw89EXbvQbDgch-xj-23TuEX92-6HOYpQjo5woFTsmrBN7uo1J0_7hejPA9lfpCVmmNjAiFHVWStnGm5FZ9ER54EzAuenDbNu8vi8bMNNcj471Qf8ZsN_VpcthzUDYDkUVzfBVyAz51AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaZGLYLuynfYbUGUN25k5adZPVccOYxpJMVxCg63_PgxG2HB1dKAjbXWj8CEC6XR1kXXLlf_U9Dy6KpXvbdKW8wQwsGQx_v55I3MVc4oy42ypLu3QlKHb14KLdB2Bmgjvxuk4UO7m109RMJHV3khiO0qdx6hisrXigI1XLIl8X-m2ffUkRKlIjiJk_dk0xm40IIPqEyrBWMWw89EXbvQbDgch-xj-23TuEX92-6HOYpQjo5woFTsmrBN7uo1J0_7hejPA9lfpCVmmNjAiFHVWStnGm5FZ9ER54EzAuenDbNu8vi8bMNNcj471Qf8ZsN_VpcthzUDYDkUVzfBVyAz51AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیه‌ساز هاگوارتز ( مدرسه جادوگری سری داستان‌های هری پاتر ) از ‌Fable 5⁩
در این قلعه افسانه‌ای می‌توانید درس بخوانید و با جارو پرواز کنید.
🧙‍♂️
‏این شبیه‌ساز مستقیماً در مرورگر اجرا می‌شود.
https://hogwarts-production.up.railway.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6685" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ظاهرا کلودفلر اعصابش از ایرانیا **ری شده و از این به بعد دیگه ایمیل فیک قبول نمیکنه اگرم بکنه تایید نمیتونین کنین اگرم بتونین تایید کنین بنتون میکنه
😍
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/6684" target="_blank">📅 18:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ArchiveTel
pinned «
دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...  https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6683" target="_blank">📅 18:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trGb7MxU3BKSgD1HsVxaHNhotJ7ycbosp4rmp12E6f3gfI1Ybs8_dWhduzpq7Xu3kPRsfwkpW-uSxyO6b6M6R5Ni8sCMGhSRiOI96gsutCSn4BGUZ4Jyd129dkzb0K_dn-BtvsvB7iOEaOZQdZtpZpBSXjN487yASFYRp-BBp4DarRs6npwsivPwtJn1x3KMR7eF0ZBWTW4iGSoxQgT_xt-RFcMcMMDzTAKycWnW3tyJ4mo7pimz2GQ7WgIFTqz7Vuop2dHkRcD1fXtCD8wU3zY2Vj88FWSdc6KlYEOonMnvlrmZ29_d1jluo1a-nU1qLf2UmrSImEjF5V5wNYL9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
