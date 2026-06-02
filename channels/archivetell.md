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
<img src="https://cdn4.telesco.pe/file/q7PUYAvXGMoLc70LeGdoNorZxhNCntRc4ixPGaipzyg5ixPCr9L0oPdaoUwnARaFh_8F0pWO-Ru6qZkpE16c-QMMj1wm4cqH-3Sk2yvObOal56Wt2OsKbZ0a3JZayjtuix4dJGuG8aSv_z2b-kDpPwiJgYyPIuKuBKRlR_rurbigFowtQg1SjdfVNR7xFo2xohhsxCDY1FltDd0HgtcVh-yvYsxu6RqEGjr3_9jYKrAvv0pVObzHhy2N4CJzR1K0zqQ55yXJVfFkKZZFVmr48ksrYbh0W4zoxYz0vgiTRr0Dfu_B5hPy8Wfv6U95zsJhh4Rp1G95G-DlhfRLh4e2Rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.81K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 03:37:39</div>
<hr>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اپن سورسه پروژه
البته باید کدش بررسی بشه
ولی شدیدا روونه
و کلا انگار ی اپ دیگه اس
😂
خیلی خوشگله
در کل جای کار داره و ابتدای کارشه پروژه ولی خیلی باحاله
اپشنای خوبیم داره بررسی کنین</div>
<div class="tg-footer">👁️ 110 · <a href="https://t.me/archivetell/5859" target="_blank">📅 03:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMonoGram</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">monogram-arm64-v8a-0.1.0-release.apk</div>
  <div class="tg-doc-extra">49.1 MB</div>
</div>
<a href="https://t.me/archivetell/5855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 156 · <a href="https://t.me/archivetell/5855" target="_blank">📅 03:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6jOcwIN4YR16Kye10ihGho2BDVMa1K08sQkZIOhCj6ujeoqU9eZSMMQm8CaOFRHTHGvKLR9POvoJ1KHfw_k2_L_Nc0Vk2b8nuf2qxnVbsRPcOfaFhMdYuFDwzsKHBlnyEuXn9xHqJ2SjsMeAfAj7uw6PIBiqnMk_fdDsLpXaTubmZ4pmHBCf24AxhazecUhA_xurZxP3nyUz4MDxsrAcXxHf_K0jS_tLsqAn9SyOD1nhRdYy-IrIRKTaPBwhS_gT0bdOKDo1RqNoly50PWnP4yQwMCllMv-ySuvFm6RzJDoRhy0_YlOmIfTST31SAbxqCo0Ithwqc3gLFVuQvl1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠️
MonoGram؛ یک کلاینت متن‌باز و مستقل برای تلگرام
MonoGram یک اپلیکیشن غیررسمی تلگرام برای اندروید است که برخلاف بسیاری از کلاینت‌ها، از صفر و بر پایه TDLib توسعه داده شده و فورک نسخه رسمی نیست.
✨
ویژگی‌ها:
• رابط کاربری مدرن با Material 3
• عملکرد سریع و روان
• قفل بیومتریک و ذخیره‌سازی امن
• پشتیبانی از جستجوی داخل چت
• مدیریت بهتر فایل‌ها، رسانه‌ها و استیکرها
• متن‌باز و قابل بررسی توسط همه
📌
توسعه‌دهندگان اعلام کرده‌اند که MonoGram روی تجربه پیام‌رسانی، طراحی مدرن و عملکرد بهینه تمرکز دارد و قابلیت‌های NFT و کریپتویی تلگرام را اضافه نخواهد کرد.
این پروژه هنوز در حال توسعه فعال است، اما با انتشار نسخه 0.1.0 امکانات و پایداری آن نسبت به قبل به‌طور محسوسی بهتر شده است.
🔗
GitHub:
https://github.com/monogram-android/monogram
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 168 · <a href="https://t.me/archivetell/5854" target="_blank">📅 03:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">100GB
⚡
vless://29f8120c-fa78-4b20-b5a5-5390d9cfbbc9@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=a28e08feb9324fb0#%F0%9F%87%B3%F0%9F%87%B1%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 292 · <a href="https://t.me/archivetell/5853" target="_blank">📅 03:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇫🇷
ss://YWVzLTI1Ni1nY206ZjRlN2NjM2ItMWZkZS00ODYxLTlhN2UtMjk0NzI4ZDhhMTZh@51.195.235.71:2083#%F0%9F%87%AB%F0%9F%87%B7%20%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 359 · <a href="https://t.me/archivetell/5852" target="_blank">📅 03:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚡️
چینی‌ها از Qwen3.7-Plus رونمایی کردند؛ یک مدل چندوجهی و Agent محور جدید!
🤖
شرکت Alibaba مدل جدید
Qwen3.7-Plus
را معرفی کرده؛ یک مدل چندوجهی (Multimodal) که بینایی و زبان را در یک معماری واحد ترکیب می‌کند و برای اجرای وظایف پیچیده طراحی شده است.
🔥
قابلیت‌های کلیدی:
🔹
فعالیت به‌عنوان یک Agent کامل در محیط‌های GUI و CLI
🔹
تحلیل همزمان تصاویر و متن
🔹
کمک به برنامه‌نویسی و انجام وظایف بهره‌وری
🔹
پشتیبانی از ورودی‌های چندفرمتی
🔹
درک تصاویر، استدلال روی آن‌ها و ارجاع پاسخ‌ها به اشیای مشخص
🔹
استفاده از جستجو برای افزایش دقت پاسخ‌ها
🔹
سازگاری با فریمورک‌های مختلف Agent
💡
به زبان ساده، Qwen3.7-Plus فقط یک چت‌بات نیست؛ بلکه یک Agent چندرسانه‌ای است که می‌تواند تصویر ببیند، متن تحلیل کند، کد بنویسد و در محیط‌های مختلف عملیاتی شود.
📌
این مدل از طریق API در Alibaba Cloud Model Studio در دسترس قرار گرفته است.
🔗
وبلاگ معرفی:
https://qwen.ai/blog?id=qwen3.7-plus
🔗
نسخه آزمایشی:
https://chat.qwen.ai/?models=qwen3.7-plus
🔗
مستندات API:
https://modelstudio.console.alibabacloud.com/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/archivetell/5851" target="_blank">📅 00:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5850">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ji_4eY6Lps-Fr7v0jWCeX4H9OMSQEB3Ymtvv2YAJHhZH0YXK2RF6EkDzANIkp1mJGuP-70gc3GMTCVqVQNx6cfks3pqeeFID3HVZACHgcpCfJXQrnVUPM5YT2i4qzHcb-KXcPP-MM8wa8Q5k4e0pjhzbZMv2gQgrQEdN2JVbMTClEfjbKmFFSkeuaSoaorwQLy8MY1Law3KSLfs5hl0C3LSwjQR4uoPEy8GvieLt3qCRLtbXGfTDAGI6oyCQcv1L1mY_XDbnxFf8JT1VbqIfnuIBtdQWQscccz8Xe2WXJ1zDCAaM8BFSjRWfgThY0-bEh8rcBLs2Bw4ukLMOYBYlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Golazo پخش زنده متنی فوتبال
⚽️
فوتبال را مستقیماً از طریق ترمینال تماشا کنید
https://github.com/0xjuanma/golazo
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/5850" target="_blank">📅 23:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترجمه پیام Void Verge: از زمانی که اینترنت ایران توسط دولت بازگشایی شد، تغییرات گسترده‌ای در سراسر شبکه داخلی کشور در حال رخ دادن است. پس از هفته‌ها قطعی، تقریباً تمام روش‌هایی که در آن دوره استفاده می‌شد، مستندسازی شده و به مقامات تحویل داده شده است. سیستم فیلترینگ در حال آماده‌سازی برای مرحله بعدی قطعی‌هاست. روش‌هایی مانند DNS tunneling، MITM و Domain Fronting قطعاً در قطعی‌های آینده دیگر کار نخواهند کرد.
علاوه بر این، مقامات فیلترینگ گام‌های مهمی برای ایجاد ارائه‌دهندگان واسط برداشته‌اند که خدمات خارجی را با محدودیت‌های شدید به ایرانیان ارائه می‌دهند، یا وب‌سایت‌های ضروری را که نمی‌توانند از روش‌های قبلی استفاده کنند، NAT می‌کنند.
در این شرایط، انتشار علنی و عمومی روش‌ها هیچ فایده‌ای ندارد جز اینکه کار مقامات فیلترینگ را آسان‌تر کند. این مکانیزم باید زیر رادار عمل کند — به صورت سورس‌بسته و بی‌صدا.
در عین حال، مافیای اینترنت ایران قدرت بیشتری پیدا کرده است — مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، ISPها و دیتاسنترهایی که فروش اینترنت نامحدود به فروشندگان VPN را با قیمت صدها میلیون تومان از طریق مکانیزم‌هایی مانند سرویس‌های پروکسی و سرورهای اختصاصی با قابلیت NAT آغاز کرده‌اند.
این مافیا چنان قدرتمند شده است که موفق شده شورای عالی فضای مجازی ایران را به سمت محدودتر نگه داشتن اینترنت سوق دهد تا سود خود را به حداکثر برساند، آن هم علیرغم شرایط بحرانی و جنگی هفته‌های گذشته.
ارائه‌دهندگان ساده میزبانی وب در ایران، تنها پس از دو ماه قطعی، به فروشندگان میلیونر VPN تبدیل شده‌اند.
ما در هفته‌های آینده به جمع‌آوری و انتشار داده‌های لازم ادامه خواهیم داد. اگر این وضعیت ادامه یابد، هدف بعدی ما باید مافیای اینترنت در ایران باشد.
امیدواریم این روزهای سخت برای همه ایرانیان بگذرد. دردی که دشمنان داخلی و دزدانی که به بهانه جنگ مردم را غارت می‌کنند ایجاد می‌کنند، به مراتب بدتر از خود جنگ است!
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5849" target="_blank">📅 23:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">SNI Spoofing
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.18.35.46
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
replit.com
"
}
{
"LISTEN_HOST": "
127.0.0.1
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
45.85.118.176
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
shad.ir
"
}
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/5848" target="_blank">📅 22:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
آموزش راه‌اندازی VLESS WS با دامنه اختصاصی ابر آروان (روش True CDN Proxy)
این روش آی‌پی سرور خارج شما را کاملاً مخفی می‌کند و با عبور دادن ترافیک از سرورهای داخلی، سیستم فیلترینگ (DPI) را به طور کامل فریب می‌دهد.
پیش‌نیازها
:
* یک سرور مجازی (VPS) خارج و پنل 3x-ui نصب شده.
* یک دامنه بین‌المللی برای سرور اصلی (استفاده از پسوندهایی مثل .shop به جای دامنه‌های ملی، امنیت شبکه شما را بالا می‌برد).
* یک دامنه ارزان .ir برای ثبت در شبکه ابر آروان (به‌عنوان ماسک).
🛠
مرحله ۱: تنظیمات DNS در ابر آروان
1. دامنه .ir خود را در پنل ابر آروان ثبت و تایید کنید.
2. به بخش
رکوردهای DNS
بروید و یک
رکورد A
جدید بسازید.
3. در بخش مقدار (Value)،
آی‌پی سرور خارج
خود را وارد کنید.
4. حتماً نماد
ابر را روشن کنید
(پروکسی شبکه فعال باشد).
⚙️
مرحله ۲: تنظیمات پنل 3x-ui
1. وارد پنل شوید و از بخش Inbounds یک کانفیگ جدید با پروتکل
VLESS
بسازید.
2. پورت را روی یکی از پورت‌های امن و مجاز آروان (مثل
443
یا
8443
) قرار دهید.
3. در تنظیمات Transport، بخش شبکه (Network) را روی
ws (وب‌سوکت)
بگذارید.
4. مسیر (Path) را روی یک عبارت دلخواه تنظیم کنید (مثلاً /secure-tunnel).
5. در فیلد
Host
، نام دامنه .ir خود را که در آروان ثبت کرده‌اید بنویسید و تنظیمات را ذخیره کنید.
📲
مرحله ۳: ویرایش نهایی برای کلاینت (v2rayNG/v2rayN)
1. لینک کانفیگ ساخته شده را از پنل کپی کرده و در کلاینت خود ایمپورت کنید.
2. به بخش ویرایش کانفیگ (Edit) بروید.
3. قسمت
Address (آدرس سرور)
را پاک کرده و
دامنه .ir آروان
خود را جایگزین آن کنید.
4. بررسی کنید که فیلدهای
SNI
و
Host
(یا Peer) نیز دقیقاً همان دامنه .ir باشند. ذخیره کنید و وصل شوید!
💡
چرا این روش عالی و بدون قطعی است؟
در این معماری، کلاینت شما مستقیماً به آی‌پی‌های تایید شده داخلی ابر آروان متصل می‌شود. فایروال محلی فقط یک اتصال امن و داخلی را می‌بیند و ترافیک را مسدود نمی‌کند. سپس خود زیرساخت آروان در نقش یک تونل معکوس، ترافیک شما را به‌صورت کاملاً مخفیانه به سرور خارج منتقل می‌کند! آی‌پی سرور اصلی شما هرگز لو نمی‌رود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/5847" target="_blank">📅 22:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترمینال برنامه‌نویسی هوش مصنوعی با عملکرد بالا
🔥
یک ترمینال کدنویسی بومی هوش مصنوعی مبتنی بر Rust که از همکاری چند عامل هوشمند، رابط کاربری TUI و محیط ایزوله امن پشتیبانی می‌کند و مخصوص توسعه سریع طراحی شده است.
https://github.com/Agions/synerix
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/5845" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgfmDuELfxJTt67iPlQuvGRkThmEgZmiKZcf_xDut-GWXPXE72fD6hg9VPX1eIv12Uy0cogUcwOJO2ynl3D1V-WZuUzI3YiOlPBxYfBQAmG9Fe5dJWzwzCh1iMbeLp4q8BwCnER_vC0D7XN-hzHrpdVh6FVQZ_HZCcj3K_ksVy8qLPvXIYp4ql4Tc-3E-EocHW_-tlJLv65JyAw4xq4Rm2F2SbdhZFjhPA_yMAXfaSxt_0oUIESGQIYtBZZ420C3d_nW-agW0QyRkGbpVq-GwYu84DF4D0WALtwI4wUR70AaoINiawhzbxGs2L1Lo1nAxwJRbnCkP2QQeewapcKtkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
TON رسماً به Gram تغییر نام می‌دهد!
🪙
پاول دوروف اعلام کرد که ارز داخلی اکوسیستم TON از این پس با نام Gram شناخته خواهد شد. این نام در واقع همان نامی است که در اولین وایت‌پیپر پروژه تلگرام استفاده شده بود.
🔹
فرآیند ری‌برندینگ حدود ۳ هفته زمان خواهد برد.
🔹
شبکه بلاکچینی همچنان با نام TON به فعالیت خود ادامه می‌دهد.
🔹
Gram به عنوان نام توکن و ارز اصلی اکوسیستم شناخته خواهد شد.
این اقدام چهارمین مرحله از برنامه ۷ مرحله‌ای «Make TON Great Again» است که دوروف برای بازگرداندن هویت اولیه پروژه TON معرفی کرده است.
📌
خلاصه:
✅
TON = نام شبکه
✅
Gram = نام جدید ارز اکوسیستم
✅
زمان تکمیل تغییرات: حدود ۳ هفته
🪙
به نظر می‌رسد نام تاریخی Gram پس از سال‌ها دوباره به اکوسیستم تلگرام بازگشته است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5844" target="_blank">📅 19:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1m7mzlcLeDNC5VJWgzbVREHzi37uu2MPDEb4ggS6qVSxJmcETN4NGJzShMUXofI2ECbnu31o7-qRauQyCZzU36IIiDw10dfCAeX8uoNOp8o1LMGbEIFO4wa6oMbfwIq59RxKzLH4b-1jAR2M4-aR2NyL1Ru1qICY5hV3Mp8oWQ7YkGD4L18rfPz7CopF0kRVCGrHk3WV_R5BYFDK0nc5ET536vxHZGnxUDEB0VyHtWrgkrklMnNWU8Vr5r1LyrvJ-RrelwHXGyrbIr_Sy1nsur9SnXADrvWAoNmL8QolWMOEnQkbbxSlQ93bfJOeuAfXs0UNWTtPkcwfRDCOWJy9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
پوسترهای فوق‌العاده حرفه‌ای از شهر خودتان با هوش مصنوعی!  اگر دوست دارید در چند ثانیه یک پوستر سه‌بعدی و لوکس از شهر خودتان بسازید، این پرامپت فوق‌العاده را امتحان کنید.
🛠
مراحل استفاده:
🔹
وارد GPT Image شوید.
🔹
عبارت [نام شهر شما] را در پرامپت زیر با…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/5843" target="_blank">📅 18:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚡️
پوسترهای فوق‌العاده حرفه‌ای از شهر خودتان با هوش مصنوعی!
اگر دوست دارید در چند ثانیه یک پوستر سه‌بعدی و لوکس از شهر خودتان بسازید، این پرامپت فوق‌العاده را امتحان کنید.
🛠
مراحل استفاده:
🔹
وارد GPT Image شوید.
🔹
عبارت
[نام شهر شما]
را در پرامپت زیر با نام شهر دلخواهتان جایگزین کنید.
🔹
پرامپت را ارسال کنید و منتظر نتیجه بمانید.
🎨
خروجی چه شکلی خواهد بود؟
• پوستر گردشگری سه‌بعدی و ایزومتریک
• نمایش معروف‌ترین جاذبه‌ها و نمادهای شهر
• معماری مینیاتوری بسیار واقع‌گرایانه
• افکت‌های سینمایی و نورپردازی حرفه‌ای
• دریا، ساحل، پل‌ها، جزایر و مناظر شاخص (در صورت وجود)
• تایپوگرافی اختصاصی با نام شهر
• مناسب برای پروفایل، چاپ، پوستر یا شبکه‌های اجتماعی
💡
نکته جذاب اینجاست که مدل به‌صورت خودکار مشهورترین بناها، خیابان‌ها، سواحل و نمادهای شهر را تشخیص می‌دهد و آن‌ها را در قالب یک دیورامای شناور و لوکس ترکیب می‌کند.
Create a premium stylized 3D isometric travel poster of [شهر] designed as a floating miniature world placed on top of a large ticket, postcard, or stamp platform with perforated edges. Automatically include the most iconic coastal landmarks, skyline, architecture, cliffs, islands, harbors, bridges, beaches, or sea views associated with the location. Arrange everything in a compact cinematic composition with realistic geography and recognizable visual identity. Style the scene as: - ultra detailed 3D diorama - photorealistic miniature architecture - cinematic travel advertisement - luxury tourism aesthetic - highly immersive but minimal - clean and elegant composition - realistic textures and reflections - soft atmospheric haze - subtle depth of field - premium Instagram-worthy artwork Environment details: - beautiful coastline and ocean integrated into composition - tiny boats, ferries, or sailboats in water - curved shorelines and waterfront promenades - lush greenery or terrain matching the destination - floating soft volumetric clouds around the city - warm cinematic sunlight - subtle shadows and reflections Add tiny realistic miniature people naturally placed near landmarks or waterfronts: - tourists taking photos - couples walking - tiny silhouettes for scale only - avoid crowds or clutter Typography: On the blank white ticket/poster area, automatically add: - the destination name in large bold elegant typography - a short poetic luxury-travel-style tagline matching the location Typography style: - modern sans-serif - premium travel poster design - minimal and elegant - subtle shadows and clean spacing Background: - smooth vibrant gradient background - color palette should naturally match the destination - minimal distractions - lots of negative space around the floating platform Composition: - floating centered platform - isometric perspective - balanced proportions between sea, architecture, and typography - destination should feel suspended in air - cinematic framing - visually clean and uncluttered Aspect ratio 1:1 Extremely detailed, cinematic, modern, premium, luxurious, artistic, visually striking, travel-poster aesthetic.
🔥
نتیجه نهایی معمولاً شبیه پوسترهای تبلیغاتی حرفه‌ای گردشگری و کارت‌پستال‌های لوکس خواهد بود.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/5842" target="_blank">📅 18:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پروکسی متصل سامانتل و مخابرات تست شده
https://t.me/proxy?server=87.248.129.52&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5841" target="_blank">📅 18:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">trojan://humanity@198.62.62.23:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/5840" target="_blank">📅 18:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک استارتاپ هوش مصنوعی چینی یک مدل ۱ تریلیون پارامتری ارائه کرد - کاملاً رایگان و متن‌باز.
👀
نام آن Kimi K2.6 است - ۱۲ روز پیش توسط Moonshot AI منتشر شد و در حال حاضر توجه‌ها را به خود جلب کرده است.
اعداد و ارقام باورنکردنی هستند. ۱ تریلیون پارامتر. فقط ۳۲ میلیارد پارامتر در هر درخواست فعال می‌شود - به این معنی که با وجود حجم عظیمش، به طور کارآمد اجرا می‌شود. پنجره زمینه ۲۵۶ هزارتایی. کل پایگاه‌های کد، اسناد حقوقی و مقالات تحقیقاتی را در یک مرحله مدیریت می‌کند.
اما چیزی که آن را واقعاً خاص می‌کند این است - Cursor، یکی از پرکاربردترین ابزارهای کدنویسی هوش مصنوعی در جهان، مدل Composer 2 خود را مستقیماً بر روی Kimi ساخته است. این اعتبارسنجی نهایی است.
این مدل کدنویسی، استدلال، ساخت وب‌سایت، ایجاد اسلاید، تجزیه و تحلیل داده‌ها و اجرای وظایف چند مرحله‌ای مستقل را انجام می‌دهد - همه در یک فضای کاری تمیز.
و برخلاف GPT یا Claude - کاملاً متن‌باز است. استفاده، اجرا و توسعه رایگان است.
🔗
https://kimi.com
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/5839" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ905OoFDxjfDCWAHhirD957alYO3wBFvUf-NEF6nl6VKCfom_4DvPE2U_Ruy9St1sG933L5TILdKXejDr876LN8jRJApaiFTsH8n4MRIyS5pkEVMfIIy6MGx-Iyh-btSG6E0I1sl6ptUhEjpE6rh888An-uqrS-OpWlH5eg5eH3KyFLi3ET_kgW9uAjCr0mAjGaRuvlEF0dIoDfnnn7n80ShgrEd9W_-0_ngbLa_l2AGIc9fYhE3WG6YApobnGfX0WDWmMLx46eT9s5jwsWk7mOdjj63iI6n4zz7iLP9YhPsjGAMlbKQifndST5ZUTvzEXY8Zn-oM1zgypMxDXwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
گوشی اندرویدی را به یک میکروفون حرفه‌ای تبدیل کنید!
📌
پروژه MicYou به شما اجازه می‌دهد از گوشی اندروید به‌عنوان میکروفون برای کامپیوتر استفاده کنید.
📶
اتصال از طریق Wi-Fi
🔌
پشتیبانی از USB
🔊
حذف نویز و کاهش اکو
🎚
کنترل خودکار حجم صدا (AGC)
💻
سازگار با ویندوز، لینوکس و macOS
⚡
راه‌اندازی سریع با پشتیبانی از Virtual Audio Device
💡
گزینه‌ای کاربردی برای جلسات آنلاین، استریم، ضبط پادکست یا زمانی که میکروفون مناسبی در اختیار ندارید.
📥
لینک پروژه:
github.com/LanRhyme/MicYou
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5838" target="_blank">📅 15:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎁
دسترسی آزمایشی به Claude، GPT و Gemini در یک پنل!
📌
سرویس Bind چندین مدل هوش مصنوعی را در یک داشبورد واحد ارائه می‌کند و برای کاربران جدید دوره آزمایشی دارد.
🤖
Claude Sonnet
🧠
GPT
✨
Gemini
🔄
جابه‌جایی سریع بین مدل‌ها
📋
مدیریت همه چت‌ها در یک محیط
🛠
شروع کار:
🔹
وارد سایت Bind شوید.
🔹
یک حساب کاربری ایجاد کنید.
🔹
گزینه Free Trial را فعال کنید.
🔹
در صورت نیاز، پلن‌های آزمایشی و امکانات تیمی را از داخل پنل بررسی کنید.
💡
اگر می‌خواهید چند مدل مطرح AI را در یک محیط تست کنید، Bind می‌تواند گزینه جالبی باشد.
🌐
app.getbind.co
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5837" target="_blank">📅 14:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel(𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣⚡️)</strong></div>
<div class="tg-text">رفقا سلام!
✋
در این پست آموزش جامع راه‌اندازی اسکریپت بی‌نظیر CFnew (نسخه 2.9.8) رو براتون آماده کردیم. در این آپدیت، تمام باگ‌های یک ماه گذشته برطرف شده. این ابزار روی کلادفلر (Workers و Pages) اجرا میشه و یکی از کامل‌ترین پروژه‌هاست.
🔥
ویژگی‌های اصلی CFnew:
* پشتیبانی همزمان از پروتکل‌های VLESS، Trojan و xhttp.
* پنل گرافیکی قدرتمند: مدیریت کانفیگ‌ها تحت وب با دیتابیس KV (اعمال تغییرات در لحظه بدون نیاز به دیپلوی مجدد).
* Sub-converter داخلی: تولید کانفیگ کلاینت‌ها (Clash, Sing-box, V2rayNG و...) بدون نیاز به سرویس خارجی.
* پشتیبانی از ECH: دور زدن محدودیت‌های پیشرفته.
* تست پینگ داخلی: تست و انتخاب خودکار بهترین آی‌پی‌ها.
* پشتیبانی از رابط کاربری فارسی.
🛠
پیش‌نیازها:
یک اکانت کلادفلر + ساخت یک UUID معتبر از سایت
https://www.uuidgenerator.net
(این UUID رمز ورود شما به پنل خواهد بود).
💻
نصب روی Cloudflare Workers:
1. ساخت KV: در کلادفلر، از Storage ➔ KV یک Namespace جدید بسازید.
2. ایجاد Worker: در Workers & Pages یک ورکر جدید بسازید، کدهای قبلی را پاک و سورس CFnew را از گیت‌هاب پیست کنید (Deploy بزنید).
3. تنظیم متغیرها: در Settings ➔ Variables، متغیری با نام U (حرف بزرگ) بسازید و مقدارش را UUID خود قرار دهید.
4. اتصال KV: در Settings ➔ KV Bindings، دیتابیسی که ساختید را با نام C (حرف بزرگ) متصل (Bind) کنید.
5. تاریخ سازگاری: در Settings ➔ Runtime، گزینه Compatibility Date را روی 2026-01-20 تنظیم و ذخیره کنید.
6. اتصال دامنه: در Triggers ➔ Custom Domains، دامنه خود را متصل کنید.
🌐
نصب روی Cloudflare Pages:
1. آپلود فایل‌ها: در Workers & Pages یک Pages ایجاد کنید. با گزینه Direct Upload، فایل Zip پروژه را آپلود کنید.
2. تنظیمات: مشابه روش قبل، در Settings متغیر U (برای UUID) را ساخته و KV Bindings را با نام C متصل کنید.
3. تاریخ سازگاری: در Settings ➔ Runtime، تاریخ را روی 2026-01-20 تنظیم کنید.
4. دیپلوی مجدد (حیاتی): چون متغیرها فوراً اعمال نمیشن، به تب Deployments رفته، Create deployment را بزنید و همان فایل Zip را دوباره آپلود کنید تا پروژه از نو ساخته شود.
🔓
نحوه دسترسی به پنل مدیریت:
مرورگر را باز کرده و آدرس دامنه خود را به همراه UUID وارد کنید (مثال:
yourdomain.com/UUID
). در این پنل گرافیکی و فارسی، می‌توانید لینک‌های اتصال (Subs) بگیرید، ECH را مدیریت کنید و آی‌پی‌های تمیز وارد کنید.
🔄
نحوه آپدیت برای نسخه‌های بعدی:
* اگر از Worker استفاده می‌کنید: کدهای جدید را کپی، جایگزین کدهای قبلی کرده و Deploy کنید.
* اگر از Pages استفاده می‌کنید: در تب Deployments فایل Zip جدید را آپلود کنید (بدون نیاز به تنظیم مجدد).
📥
سورس کد و دانلود زیپ:
https://github.com/byJoey/cfnew
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 562 · <a href="https://t.me/archivetell/5836" target="_blank">📅 14:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آیپی تمیز کلودفلر مخابرات و ایرانسل تست شده
45.130.125.96
27.50.48.49
208.103.161.170
45.130.125.0
45.130.125.160
45.130.125.69
66.81.247.155
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5835" target="_blank">📅 14:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">۵ گیگ کانفیگ از پشت cdn رد شده همراهم میاره
vless://6053415d-763c-4132-9445-e4a0329a594b@snapp.ir:80?encryption=none&host=netrox.cnxman.ir&path=%2F&security=none&type=ws#netrox%20--cdn%20-%20tunnel
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5834" target="_blank">📅 14:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">۱۰ گیگ کانفیگ تانل
🔥
vless://a5400c9e-2f0f-41c9-aa4d-5a77c0787af3@cnxman.ir:17544?security=none&encryption=none&headerType=none&type=tcp#tunnel
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5833" target="_blank">📅 14:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5832">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">1 ترابایت اهدایی از یکی از ممبر های عزیز
❤️
vless://ZoRoVpn@104.253.18.220:80?security=reality&encryption=none&pbk=D4tCeuAMOZViac1SOVD5ABdN86EkAn9ql3NEuQlneXQ&headerType=none&fp=chrome&spx=%2F1vwstnEi2HFdu63&type=tcp&sni=www.yahoo.com&sid=88ab02c0#1.00TB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5832" target="_blank">📅 13:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVUL2YiN1wFhp3QFixkyLumLCDd8MOEj3e0VkHFg4uZRaKFcRZhGFCJBJendB7cmO4AVeVw1M2ItxtTQGHoihx6a7T6dvocYCIqmTo5nfbq-O9NGyFyb8Nbwt2izLcyzAozhYSk9dEns3hie7MxiqFszFxY6P42oq3bMgqR_F3Sa5hrnLVos8yy8bE2NnRrXAYjweGacweEs9mNYiD9uGoBZjMHRJwiFWITPdiO8w3K-Iv3WUkvi9prgYzGm0QYQfCM7WG7wqvHdeE2iF-uyd3F4BhRTnw-p89ipQUgdFX3O0kBUorNrpQ4ysOYwHyNxKUZly4xW-q-eDxJJFdTw7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3e809b21-e29b-49ec-a7fb-5301ec7c1cee@food.artmisserver.site:8443?encryption=none&host=ap.isowli.ir&path=%2F&security=none&type=ws#Artmis
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5830" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJFdI8OGSELxPUoFp57iaUeO-OmWG9yWR2g7t68vuaGhBhai1yZ1ofmZF7HZaSBf-oAK6saSkyt9TdL6Ghl9vZIM8e7RWnp0TlCYTWubdIr9QcJQL8MjR1KgZ-L0V6lfR9RSebJ_O7UybwfJq1aBzeaqkvVsXoZEWqiy68KPTPE-9plVgAq8WeFOgpbr1audNt-_qTRZU8_IDHTJ0nNcjid86gI_HUoQpchZkQuNpJAROKW6sorkx0Q6VKYpvYHY9YJzRZYkJnqD1hORD7IF5C0N5511xecQdQrhIGwW6k2hUSRdETx7rkCBopUlMQN35z8iAKjYwkdO9G0kraHnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
تبدیل خودکار هر صدا به متن و خلاصه!
📌
ابزار DeLive صدای در حال پخش روی سیستم را به‌صورت لحظه‌ای دریافت می‌کند و از آن زیرنویس، متن و یادداشت تولید می‌کند.
🎙
تبدیل گفتار به متن در لحظه
💬
نمایش زیرنویس روی صفحه
🌍
پشتیبانی همزمان از دو زبان
👥
تشخیص گوینده‌های مختلف
📋
تولید خلاصه و گزارش از محتوا
❓
امکان پرسش از محتوای ضبط‌شده
💡
مناسب برای کلاس‌های آنلاین، ویدیوهای آموزشی، پادکست‌ها، استریم‌ها و جلسات کاری؛ بدون نیاز به یادداشت‌برداری دستی.
💻
پشتیبانی از ویندوز، لینوکس و macOS
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
https://github.com/XimilalaXiang/DeLive</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5828" target="_blank">📅 12:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">0BITO.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/5827" target="_blank">📅 12:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://9e48e5db-e5cb-462f-ab0b-6f573aa73728@31.56.229.237:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=rT-KdyGuCqbP8c-CilgD2sSWMkSSLe8xbEeRNxypsSk&security=reality&sid=941935f2d0e82539&sni=www.amazon.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/5826" target="_blank">📅 12:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🕵️‍♂️
مرورگر شما چه اطلاعاتی را روی سیستم ذخیره می‌کند؟
📌
یک راهنمای فورنزیک نشان می‌دهد که در مرورگرهای Chrome، Firefox و Edge تقریباً همه ردپاهای کاربر روی سیستم ذخیره می‌شوند.
🔖
بوکمارک‌ها و سایت‌های ذخیره‌شده
🌐
تاریخچه مرور و جستجوها
🔑
رمزهای عبور و لاگین‌ها
🍪
کوکی‌ها و اطلاعات نشست‌ها
📂
فایل‌های دانلودشده
🧩
افزونه‌ها و تنظیمات مرورگر
🖼
تصاویر کش و فاوآیکون سایت‌ها
🛠
همچنین ابزارهایی مثل Hindsight، DB Browser for SQLite و LaZagne برای بررسی و استخراج این داده‌ها وجود دارد.
💡
اگر کسی به سیستم شما دسترسی پیدا کند، بخش زیادی از فعالیت‌های اینترنتی شما قابل بازیابی خواهد بود؛ حتی مواردی که مدت‌ها قبل مشاهده کرده‌اید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5825" target="_blank">📅 11:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🤖
یک لیست طلایی از ابزارهای رایگان هوش مصنوعی!
📌
اگر از بین صدها ابزار AI نمی‌دانید کدام‌ها واقعاً ارزش استفاده دارند، این مجموعه می‌تواند نقطه شروع خوبی باشد.
🎨
تولید تصویر: Raphael AI ،Krea AI ،Magnific AI
🎬
تولید و ویرایش ویدیو: Runway ،Kling AI ،Hedra
🎙
صدا و موسیقی: ElevenLabs ،Suno
💻
برنامه‌نویسی: Cursor ،Replit
،Bolt.new
📊
تولید محتوا و ارائه: Gamma ،Napkin AI ،Notion AI
🔎
جستجو و تحقیق: Perplexity ،Phind
🤖
چت‌بات‌ها و مدل‌ها: Claude ،Poe ،Hugging Face
💡
مجموعه‌ای از ابزارهای کاربردی برای تولید محتوا، برنامه‌نویسی، طراحی، تحقیق و ساخت پروژه‌های شخصی؛ بدون نیاز به جستجوی طولانی بین صدها سرویس مختلف.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5824" target="_blank">📅 11:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">80 گیگ کانفیگ از لوکیشن های
🇳🇱
🇫🇷
🇮🇩
🇩🇪
vless://aa918a17-0c07-49b2-aec5-b72809d91a17@185.211.101.214:38200?mode=auto&path=%2Flightyagami&security=reality&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=JL7JvLV0E3dvB48lp5UpSyzx1ATHPS3Kgjv2Ox9HtjQ&fp=chrome&spx=%2F&type=xhttp&sni=www.yahoo.com&sid=4306#OBITO
vless://c649466f-e700-4d78-be2c-a9d915434f34@82.40.62.67:80?fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&type=xhttp&sni=www.yahoo.com&sid=49a5ec2ac3&mode=stream-one&path=%2Fm4rg&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=QWHdk8IaYGGm_CkKaBTLeLlOKhFGLx2pA3qBBRmiM3Y&host=light.96s.dpdns.org&spx=%2FMwzynVriGAhj8A1#OBITO-20.00GB%F0%9F%93%8A
vless://1b16b6f8-b8dd-43d7-84f9-8eb8a7e15504@sina.35o.ir:25645?security=reality&encryption=none&pbk=GnAQ0pqW4HGqMuOY7crTmcQ56FuABKPP9YaiJzOS3X8&headerType=&fp=chrome&spx=%2F&type=tcp&sni=www.yahoo.com&sid=d6372f1a0a#OBITO
vless://0c3f5b49-d0ec-451b-bf30-f50e229b645c@panel.96s.ir:8080?fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22initStreamReceiveWindow%22%3A8388608%2C%22maxStreamReceiveWindow%22%3A8388608%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIncomingStreams%22%3A1024%7D%7D&fp=chrome&type=xhttp&sni=www.yahoo.com&sid=775a6745d1&mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=0ySdtEa5hyO50lsKB3FdbcHaGCn0tw6BeYvabtJpb2s&host=panel.96s.ir&spx=%2F#%DA%A9%D9%84%D9%88%D8%AF-0BITO
@Sina_1090</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/5823" target="_blank">📅 10:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حذف واترمارک ویدئو، PDF، PPTX و اینفوگرافیک‌های NotebookLM به صورت محلی در مرورگر، بدون آپلود فایل.
لینک:
https://notebooklmremover.org/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5822" target="_blank">📅 09:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گل سر سبد ربات های سرچ تلگرام
@oksearch
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/5821" target="_blank">📅 09:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پروکسی متصل
https://t.me/proxy?server=fresh.t-proxy.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5820" target="_blank">📅 09:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">OBITO.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5819" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5819" target="_blank">📅 08:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZL2IY2ETBXsGN1Q160B3vL-9UXPUv36Y_IFD9F3s_yMWMVonqogSQMwDvBEeXbODGPZYOqZEJarYEV0oZeOSC7gp-mPos4Hp_E9HcurEKE0a3Y912YEkUEOmfrToyGBzBVlPUU77ZFgJr4Ml2l91Kt8vOn4JWYieWZVe9y3RsNuTx-HrKXKrEHWZsSKxfvN4vPAd3oqt4W9oFPA8WR6vp-1HA40O467_zc4U0xjlMBsQgs_s9jlyo31f5BqLRpXj6EfOSvZzgGmDw0Sb9v5UcnvUZkaP7x7iZMG1u4hJ5DLp4IGdjECqoxOjtceVmaU_x_U4rXQEltmcHk0zJU32Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی دلش وایرگارد میخواد....؟  @Sina_1090</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5818" target="_blank">📅 05:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کی دلش وایرگارد میخواد....؟
@Sina_1090</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5817" target="_blank">📅 05:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">vless://f6108273-3a0a-4f6c-bd82-62dc234d2945@yasin.mohraz.top:80?mode=auto&path=%2Fyasin&security=reality&encryption=none&pbk=UkHH1vDkeIQkCWeVeOAyEnYAC2yZSfq8caBjQ-H_ihQ&host=yasin.mohraz.top&fp=chrome&spx=%2FF4vpNKDpUgGorWY&type=xhttp&sni=www.yahoo.com&sid=b44e2473841b#VIP</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5816" target="_blank">📅 04:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
⚡️
❤️
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo4QW5Za3J3VDByMzlIZFJ6REtDNlNPeUE@45.39.241.51:25083#%D8%A7%D9%87%D8%AF%D8%A7%DB%8C%DB%8C%2050%20%DA%AF%DB%8C%DA%AF%20%DA%A9%D8%A7%D9%86%D8%A7%D9%84%20%0A%0A@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5814" target="_blank">📅 00:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://ead394bc-06b3-4cc0-a904-668a607aac0b@31.56.229.237:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=rT-KdyGuCqbP8c-CilgD2sSWMkSSLe8xbEeRNxypsSk&security=reality&sid=57e7bd&sni=www.amazon.com&spx=%2FSBDHPWNzLaqiYei&type=tcp#3alqhl5fyg-49.38GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/5813" target="_blank">📅 23:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ss://YWVzLTI1Ni1nY206ZjRlN2NjM2ItMWZkZS00ODYxLTlhN2UtMjk0NzI4ZDh
ss://YWVzLTI1Ni1nY206N2UxZGQ0YzU1YmY4NWRhNQ%3D%3D@212.192.15.225:20129#%F0%9F%87%AD%F0%9F%87%B0%20%40ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5812" target="_blank">📅 23:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:443?m
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:2082?mode=auto&path=%2FMohraz&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=D6IW407GuNM0FT8slImWUQL2ABfzYnf2pet0FdpGFwc&host=95.182.101.96&fp=chrome&spx=%2FzlropzOvVbv1I3R&type=xhttp&sni=www.yahoo.com&sid=cae7dd3426354120#MOHRAZ-yasin-20.00GB%F0%9F%93%8A
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:49612?security=reality&encryption=none&pbk=JRLAhrl2S4BFWT64IDgXHvJSozFfocZ3I0Z6yiozkWc&headerType=&fp=chrome&spx=%2FP262IStz3xi6uwS&type=tcp&sni=www.microsoft.com&sid=d0df63a4af11#MOHRAZ%20-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:2030?path=%2F&security=&encryption=none&type=httpupgrade#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:20828?security=&encryption=none&type=grpc#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:8000?path=%2F&security=&encryption=none&type=ws#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:18442?security=reality&encryption=none&pbk=Y8MrhrV6WraccHAPfCv8NNdyGsmAhmbD_9t7Blh49m4&headerType=&fp=chrome&spx=%2FeHjIIQnd5E35bJz&type=tcp&sni=www.samsung.com&sid=e478f43b0c25df12#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:38796?security=reality&encryption=none&pbk=LuelZgJCGhzxoQwgZRbxpFyza95n3jmoSt7eAgXr318&headerType=&fp=chrome&spx=%2FqdZ5PJq0TTISh4c&type=tcp&sni=www.bing.com&sid=412082ae#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:38956?security=reality&encryption=none&pbk=UMF9YjdC1voBk_82jBmWYR6ikJrruBwbtgReKatAQmo&headerType=&fp=chrome&spx=%2Fso8Gm7hC851Caio&type=tcp&sni=www.microsoft.com&sid=1f495c03ce#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:44535?security=reality&encryption=none&pbk=-0MP4KyHJ12AZ-z1YA5ITIjMOh8FUnGzSOSu2DFSgmI&headerType=&fp=chrome&spx=%2FYTBOOoz6loWLYfx&type=tcp&sni=www.yahoo.com&sid=de50a62ae9c03b#MOHRAZ-yasin
20GB</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5810" target="_blank">📅 23:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromaaa</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">New Text Document.txt</div>
  <div class="tg-doc-extra">55 KB</div>
</div>
<a href="https://t.me/archivetell/5809" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5809" target="_blank">📅 22:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr Killer</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SNI_SPOOFINGconfig.txt</div>
  <div class="tg-doc-extra">10.8 KB</div>
</div>
<a href="https://t.me/archivetell/5808" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5808" target="_blank">📅 22:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">rstaspoof.go</div>
  <div class="tg-doc-extra">47.7 KB</div>
</div>
<a href="https://t.me/archivetell/5806" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5806" target="_blank">📅 22:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❤️
تریاک ناب آماده شد
❤️
+sni spoof
و زنده کردن کانفیگ مرده و افزایش سرعت اینترنت رو گوشی حتی بدون روت!
توجه: این آموزش روی گوشی غیر روت  ضبط شده است!
قدم اول
برنامه ترموکس رو دانلود و نصب کنید
اینم لینک مستقیم ترموکس
حتما وی پی ان رو روشن کنید و دستور هات انجام بدین...
قدم بعدی زدن این دستورها در ترموکس....
اولین دستور:
apt update && apt upgrade -y && pkg install golang
دستور دوم:
termux-setup-storage
دستور سوم:
cd /sdcard && go run rstaspoof.go -listen :40443 -connect 104.17.121.71:443 -sni www.hcaptcha.com -method combined
و در آخر فیلتر رو خاموش و پینگ بگیرید..
دوستان اگه ای پی تمیز کلود فلر دارین می تونین با این ای پی جایگزین کنین.
گروه رفع مشکل...
@archivetell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5805" target="_blank">📅 22:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🤖
ساخت اپلیکیشن بدون حتی یک خط کدنویسی!
📌
پلتفرم Anything.com به شما اجازه می‌دهد فقط با توضیح دادن ایده‌تان، اپلیکیشن یا وب‌سایت بسازید؛ بدون نیاز به دانش برنامه‌نویسی.
⚡
ساخت اپلیکیشن اندروید، iOS و وب
🎨
طراحی رابط کاربری با کمک هوش مصنوعی
🔐
راه‌اندازی خودکار…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5804" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5802">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🤖
ساخت اپلیکیشن بدون حتی یک خط کدنویسی!
📌
پلتفرم
Anything.com
به شما اجازه می‌دهد فقط با توضیح دادن ایده‌تان، اپلیکیشن یا وب‌سایت بسازید؛ بدون نیاز به دانش برنامه‌نویسی.
⚡
ساخت اپلیکیشن اندروید، iOS و وب
🎨
طراحی رابط کاربری با کمک هوش مصنوعی
🔐
راه‌اندازی خودکار ورود کاربران
💳
اتصال سیستم پرداخت
🛠
رفع خودکار برخی خطاها و مشکلات
🖼
تولید تصاویر و المان‌های گرافیکی
💡
اگر ایده‌ای برای ساخت یک اپ دارید اما نمی‌خواهید درگیر کدنویسی شوید، این ابزار ارزش امتحان کردن را دارد.
🎁
در حال حاضر برای برخی کاربران اعتبار رایگان جهت شروع پروژه‌ها ارائه می‌شود.
🌐
anything.com
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5802" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خفن ترین ربات پینترست در تلگرام
@PinterestAllBot
🔥
دانلود فوری ویدیوها و تصاویر پینترست
🔍
جستجوی مستقیم پینترست در تلگرام
👤
بررسی هر پروفایل پینترست
⚡
استفاده از جستجوی درون خطی در هر چت
👥
همچنین در گروه‌ها کار می‌کند
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5801" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۵۰۰ گیگ کانفیگ اهدایی یکی از ممبرای گل کانال
😎
vless://d02f9d1f-7e41-4e0b-8d11-439e0f719e74@95.182.85.120:80?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&host=ata.photodrop.ir&mode=auto&path=%2FMySecurePath123456789&security=none&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5800" target="_blank">📅 21:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اقایون گویا یه روش اومده که میتونید
Sni spoofing
روی گوشی بدون روت اجرا کنید
+آموزش رو بزارم.....؟
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5799" target="_blank">📅 21:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اقایون کانفیگ sni کی داره
دارم یه چیو تست میکنم.....?
@Sina_1090</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5798" target="_blank">📅 20:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پروکسی ایرانسل ، سامانتل و مخابرات تست شده
https://t.me/proxy?server=87.248.129.51&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5797" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پروکسی مخابرات و ایرانسل
https://t.me/proxy?server=fresh.t-proxy.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5796" target="_blank">📅 18:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdbc4c5695.mp4?token=HGKxX-KO0F36tAvrImK-rpOd311tGLFdSLRmXlqaYr5cyvn5L1ABPdRT1vNmfKzMiUrRmwvf3d8HwwqTAg_u6wztjbm6jZtPWK1zreKNsFCYQJLxoHpuazTt6OyglAesmMLJ5Ho4XLVmxP7NFRGg3FQrkiBJNl353EBE9E-IdQNRK3VYr-aS4HW8w2Uu8rtJPVT3lDV8uxEoUpu376e1mQsy1u0JTWPk9cVIb249gze02k2CVobpkGo7nvtF3pYuu5hXz6xJrcMNrJ8o-uECDgXjUt72TM6t3pc4TzlxGbk7JNR6SyfwRJX95rhNRc0b-T-_Tus64QmIFCdXVpiU9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdbc4c5695.mp4?token=HGKxX-KO0F36tAvrImK-rpOd311tGLFdSLRmXlqaYr5cyvn5L1ABPdRT1vNmfKzMiUrRmwvf3d8HwwqTAg_u6wztjbm6jZtPWK1zreKNsFCYQJLxoHpuazTt6OyglAesmMLJ5Ho4XLVmxP7NFRGg3FQrkiBJNl353EBE9E-IdQNRK3VYr-aS4HW8w2Uu8rtJPVT3lDV8uxEoUpu376e1mQsy1u0JTWPk9cVIb249gze02k2CVobpkGo7nvtF3pYuu5hXz6xJrcMNrJ8o-uECDgXjUt72TM6t3pc4TzlxGbk7JNR6SyfwRJX95rhNRc0b-T-_Tus64QmIFCdXVpiU9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دوبله ویدیو با حفظ احساسات واقعی صدا!
📌
شرکت ElevenLabs نسخه جدید Dubbing Studio را معرفی کرده که می‌تواند ویدیوها را به بیش از ۹۰ زبان دوبله کند؛ آن هم بدون اینکه حس و لحن گوینده اصلی از بین برود.
⚡
پشتیبانی از بیش از ۹۰ زبان
🎭
حفظ احساسات، لحن و سبک صحبت
👥
تشخیص چندین گوینده در یک ویدیو
🎵
جداسازی خودکار موسیقی پس‌زمینه
🎬
هماهنگی دوبله با زمان‌بندی ویدیو
💡
اگر گوینده بخندد، هیجان‌زده شود یا آرام صحبت کند، هوش مصنوعی تلاش می‌کند همان حس را در زبان مقصد نیز بازسازی کند.
🎥
ابزار بسیار جذابی برای تولیدکنندگان محتوا، یوتیوبرها، مدرس‌ها و کسانی که مخاطب بین‌المللی دارند.
🌐
elevenlabs.io/dubbing-studio
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/5794" target="_blank">📅 18:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برنامه‌ریزی هوش مصنوعی برای هفته کاری ایده‌آل
reclaim.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5793" target="_blank">📅 18:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5792">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04ea6eda3.mp4?token=WrEM-8_3KYX7thiXKd8JlxxG8x8aAN5av74DIlZTlzXq3SdYBSKuQ8hbfBr2G-48zeFnUR-YuyoMew0YnsX7UDaCx_khR0_RnVU17x0lcRvW9XEafZ8r91FnfI3yer4YukRWkpkDff1OykknUlIxLaPCSmbCE2Des9cCn9XK1mRCUlXrPeheQ6sIOWiTBO084bEAnlkhVoDGTfDY0-N6B011twsOeMGrIr4hBUjEGrMKPvNX6QBzIv7XIV3FGco2FbR1_Y1PZ17710QFnai839iKfyVUrWSbFeO1Z_E9DqZPw-e2V7e1CsCl43t17Pp3iKKso5lUUvZEQpdqvSQS7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04ea6eda3.mp4?token=WrEM-8_3KYX7thiXKd8JlxxG8x8aAN5av74DIlZTlzXq3SdYBSKuQ8hbfBr2G-48zeFnUR-YuyoMew0YnsX7UDaCx_khR0_RnVU17x0lcRvW9XEafZ8r91FnfI3yer4YukRWkpkDff1OykknUlIxLaPCSmbCE2Des9cCn9XK1mRCUlXrPeheQ6sIOWiTBO084bEAnlkhVoDGTfDY0-N6B011twsOeMGrIr4hBUjEGrMKPvNX6QBzIv7XIV3FGco2FbR1_Y1PZ17710QFnai839iKfyVUrWSbFeO1Z_E9DqZPw-e2V7e1CsCl43t17Pp3iKKso5lUUvZEQpdqvSQS7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📄
یک ابزار رایگان و متن‌باز برای ویرایش PDF!
📌
پروژه Every PDF به شما اجازه می‌دهد فایل‌های PDF را بدون نیاز به اشتراک‌های گران‌قیمت و نرم‌افزارهای سنگین ویرایش کنید.
✏️
ویرایش مستقیم متن PDF
🖼
افزودن تصویر، لوگو و واترمارک
📑
ادغام چند فایل PDF
✂️
تقسیم فایل‌های حجیم به چند بخش
💻
پشتیبانی از ویندوز و macOS
💡
اگر فقط برای چند تغییر ساده مجبور به استفاده از ابزارهای پولی می‌شوید، این پروژه متن‌باز می‌تواند جایگزین خوبی باشد.
📥
لینک پروژه:
github.com/DDULDDUCK/every-pdf
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5792" target="_blank">📅 17:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5791">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd1Gb86wNQZaRUz4fb9q1vGMjj8OH1T1PsM0KlZf1EhYwKcGHhU3a7saIb8eXZVQq7Zzq8yfVSF-xStutRCK4J8hl7tijpL3SfEq4Fabjz-2AGO9ezcDICgSo6jcvdJkO-ZLqLZhT3Kns-oPGY57DrF93Zr4ovFb7wd0-enNB1KckuG-di0c8Rt2NvgVMfCle0EYBBpQjO1fDbE45f9_anGF1fAfV6OrVyBX-aO2affMxAwXEwrYlAhpplCWmHSAeGHgzwkSbi-tvr64VgAMc9YmkbijkHDb7FbVmUxnJS6Ww1CiXi658pBoq-G_u8X3xiSsJDA8GJv7pAF2mde_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💧
دستگاهی که آب دریا را شیرین می‌کند و همزمان لیتیوم استخراج می‌کند!
📌
پژوهشگران آمریکایی فناوری جدیدی برای نمک‌زدایی آب دریا توسعه داده‌اند که بدون نیاز به برق و تنها با استفاده از نور خورشید کار می‌کند.
⚡
بدون مصرف برق
☀️
متکی به انرژی خورشیدی
🧼
قابلیت خودتمیزشوندگی
🌊
تبدیل آب شور به آب شیرین
🔋
امکان استخراج لیتیوم از نمک‌های باقی‌مانده
💡
نکته جالب اینجاست که نسخه پیشرفته‌تر این فناوری می‌تواند لیتیوم را به‌صورت انتخابی از مواد باقی‌مانده پس از نمک‌زدایی جدا کند؛ عنصری که نقش مهمی در تولید باتری‌های مدرن دارد.
🔬
اگر این فناوری به تولید انبوه برسد، می‌تواند هم به بحران کم‌آبی و هم به تأمین مواد اولیه باتری‌ها کمک کند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5791" target="_blank">📅 17:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پروکسی
https://t.me/proxy?server=r33.proxytg.space&port=8443&secret=eec38451cb166b3ed3a1bbf1d4e7e382817233332e70726f787974672e7370616365&&
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/5790" target="_blank">📅 17:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">vmess://eyJhZGQiOiJzbmFwcC5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiZC5hbGlzZWN2aWNlLmlyIiwiaWQiOiI0MTA1MjgzZi1iMDM2LTQwNDMtYTE2NS0xM2MyYjA1MTY0MDgiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwicG9ydCI6IjIwODIiLCJwcyI6IjgwMl9zNDk3ODM2LTIwNC44ME1C8J+TiiIsInNjeSI6ImF1dG8iLCJzbmkiOiIiLCJ0bHMiOiJub25lIiwidHlwZSI6Im5vbmUiLCJ2IjoiMiJ9
vmess://eyJhZGQiOiJzbmFwcC5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiZC5hbGlzZWN2aWNlLmlyIiwiaWQiOiJkNWZhZjU3OS04YmMyLTRlZmUtOWFlYi05YTRhOWFiM2VlYWYiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwicG9ydCI6IjIwODIiLCJwcyI6IjgwM19hXzIyNjYtMjA0LjgwTULwn5OKIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiItLS0iLCJ2IjoiMiJ9
vmess://eyJhZGQiOiJzbmFwcC5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiZC5hbGlzZWN2aWNlLmlyIiwiaWQiOiI4NDJmYmM5NC1kNzMwLTQyNTAtODYyNi05MzQ1M2NjMWE1NmYiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwicG9ydCI6IjIwODIiLCJwcyI6IjgyODYtMjA0LjgwTULwn5OKIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiItLS0iLCJ2IjoiMiJ9
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/5789" target="_blank">📅 17:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">vmess://eyJhZGQiOiJhbnRlbi5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoidDIuYWxpc2VjdmljZS5pciIsImlkIjoiMmJiODVkNzQtNGE0NC00NWY2LTg3NzUtMDc3M2I0NjZjNjRlIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsInBvcnQiOiIyMDk1IiwicHMiOiJOZXctNzk1Xy0xMC4wMEdCIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiItLS0iLCJ2IjoiMiJ9
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5788" target="_blank">📅 17:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwQXgQJr90KVxvis2mL6V0D1fQHjWO1b9yfwLn5n0KmFdQi-djR7L99j44dXFokFAZe_BVnIHXeORlSvf3mLMfnV6FuOImznGvv-Q4moi54VwAijtBjAHIsmvZonaLueZ8cAywzEuuxLw2EmXXObLxgERW4aaKdch72a4h7bXLSZ48S7Q2d-bdVDQuov2-jHrvasYFtmNAqVM7F3dkwe7Ec3k_g87XpBfPpLnj7hJSEK9v-d0NcsItBJQMZFi5pRB3exIrvbe53E2MdC6PfRUULbINK34_7HegOnG7bhN9MqaqVATwQR6sqF7r3RF0LgicJ8-m8-X0dqEdrRllX3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxv2tqGUSTzjcxOJ8ecQ9HcHLS4T5Luacc7ZmNRmtw_uSM0FlfmhbjPcpHpN_47Bp4Nmw_zpkP-mTxNrxsfzndM047-5H51_ls33oFkjcZj8Sr4tARiqmxVYOWVJ25E7WraVcc_fRhzfBynIFHSjTPiAcHbSZIDW9O90jDY6Q3B6crKHvghkCOsY8IxlYKzb09HaIH6udQ8Rwx5YlAv6Y21DQYZMOjXEBYf7O-O49CW-8fR1i2hgtZvB2aCDdlbtzBVPBvM1negWSJZvU9mB2ev7g3itwqRSSVbAeLDPTV4XasPG2_y7Kr1_5VkJRsR_WH5zRrG8zC0swdM20dzPfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نسخه جدید MidONe Scanner منتشر شد!
اگر دنبال IP تمیز CDN، کلودفلر یا DNSهای سریع هستید، این اپ اندرویدی می‌تواند کارتان را راحت‌تر کند.
✅
اسکن حرفه‌ای CDN و Cloudflare
✅
پیدا کردن IPهای سالم از روی رنج
✅
تست و رتبه‌بندی DNSها
✅
تشخیص IPهای ناپایدار و محدودشده
✅
ذخیره و کپی نتایج با یک لمس
برخلاف خیلی از اسکنرها، فقط پینگ نمی‌گیرد؛ اتصال واقعی را تست می‌کند تا نتیجه به چیزی که در عمل تجربه می‌کنید نزدیک‌تر باشد.
⚡
📥
دانلود:
github.com/mwhammadrezss/midonescanner-android
توسعه دهنده
@mwhamadreza
یکی از ممبرای عزیز کانال
❤️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/archivetell/5786" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmOuSkr2Fy9zuNOde1uXlovxyzhKRnNHU_o-HB_gEzGfHVkYkmYSzaG2-JsD72EyALdzlUpnLFpxWkVhrLb-1V-jKU0XJ9c-WMlWzaEfxaj7c1OywZe5HXQK58v6GIEf3njZktlgykuXcArB4DA5gxvBqDPgVY67C85-B_A7DCGYH_GRm7oLANlPF8x5BfciHGyCy_c8lkeR4Ad91K2bTcXTd-hHw1b-ZYnD5SI6sx-cGLiV2VbWFIvfWgFx37ph1UPB1-ZAqVsQjAIhOApHZkxF8sUs7Cpvn4SMvG9KE4q4OZBTjRFRmtHpEPIxg5JADLYmiOEjtNG5h7zjgHnH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📂
انتقال فایل بین گوشی، ویندوز، مک و لینوکس بدون نصب هیچ برنامه‌ای!
توسعه‌دهندگان LocalSend نسخه تحت‌وب این سرویس را منتشر کردند و حالا فقط با مرورگر می‌توانید فایل جابه‌جا کنید.
🚀
✅
بدون ثبت‌نام
✅
بدون نصب برنامه
✅
بدون محدودیت حجم فایل
✅
سازگار با همه سیستم‌عامل‌ها
کافیست هر دو دستگاه به یک Wi-Fi وصل باشند، سایت را باز کنید و انتقال را شروع کنید.
🌐
web.localsend.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5782" target="_blank">📅 15:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keZuff11GyYo6GlA6m1_FyrH-KVCxllydtdnRSy-m3TSbGDwLRsKxf4mDCgr7MYV_b1dzgtOMzYYWxxkdjw-XApzm_pozyuQ82baJE3_QomCzWuF97KpDGvOESPMUO0--4eqSLBIXFJtTK49vClxFPAIFIL2VAv2--zT5F0hM94CHQbMKC6IKC4aHFMFORGlMLKX0WZJioCrcnRClmHZ2mTA7TRGQaW0jRjwzqJFgwRmeOLFM_BJJVMMksrYnMKl8UoEy0hafwnWhxUk9i_BiWbkqUbPk_L9Z6QnPlf10Cr6-VxstFkNf5GaO0Mhp6vFuX4ypoijuupLT0YyjihkEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
😁
❤️
vless://14037bcc-1d1d-41dd-9ff6-be16926c44e2@dood.rostamiarp.ir:8443?encryption=none&host=ap.isowli.ir&path=%2F&security=none&type=ws#@ArchiveTell @ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5781" target="_blank">📅 15:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5779">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
😁
❤️
vless://14037bcc-1d1d-41dd-9ff6-be16926c44e2@dood.rostamiarp.ir:8443?encryption=none&host=ap.isowli.ir&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5779" target="_blank">📅 15:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانفیگ نامحدود ۱ ساعته اهدایی یکی از ممبرای عزیز
😁
❤️
vless://614ad5da-e5cc-479d-bc90-3db549ca96e4@84.75.220.223:33434?encryption=none&fp=chrome&pbk=CBLftLCz0w2EX8H3sQ4ahU_lc9_aWJZO_8OHJEWGjDo&security=reality&sid=0af57b636837&sni=www.yahoo.com&type=tcp#ArchiveTell%201
vless://afce710f-2261-403e-ada6-459dbcb44b64@84.75.220.223:80?encryption=none&fp=chrome&pbk=XnjRQWaZ2QGrIJBGPuYOePg2wLl_ZM_gkCyJ2aKxylQ&security=reality&sid=7797159c&sni=www.yahoo.com&type=tcp#ArchiveTell%202
vless://3d1dbf5c-6f7d-47ee-9138-e217e0a77265@84.75.220.223:41034?encryption=none&mode=auto&path=%2F&security=none&type=xhttp#ArchiveTell%203
vless://5c5cb739-1112-4eea-bad1-282db5c24512@84.75.220.223:443?encryption=none&fp=chrome&pbk=g_oiiXO-P1L5MgEzE9qx7Vt0x-Z1-vI5QjXmscfh6Uw&security=reality&sid=27fd6d7ea3&sni=www.samsung.com&type=tcp#ArchiveTell%204
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5778" target="_blank">📅 13:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBMRG_13QJDfKSwlIpZyD83QNlS5yaDUI9HvrphZ1_GFbB6tqzQsH69-JUwD25la2LmLCsAx5cKCTEoh8iV-DcEQBTKB_jMzePUt9HlC1cnuhlTGaZ89bpuU_JrlRdIO4rkqne2o9MJn4UZPzriRkbRp89XAu7haxo3djNU0TTjS9UjYWAfnn7fmTgmpWJ8KwFQpGCqGKXP3x-5sV7WGgUaFz8q0ChvuoU12ab4CSgF7V8JlOK6J8odt7aeruJYoQWsHpRDDhG5CJQMe7Z4mJf3lbNfTehjgwQfWF93d3RGqiyqPYE6rlgc1dAID4pdmwsbeWh97K_CLH6FWdSiBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
افزونه Advanced Proxy Manager منتشر شد!
📌
اگر از v2rayN استفاده می‌کنید ولی نمی‌خواهید کل ترافیک ویندوز از پراکسی عبور کند، این افزونه می‌تواند فقط مرورگر کروم را به پراکسی متصل کند.
⚡
اتصال مرورگر بدون تغییر پراکسی کل سیستم
🔄
پشتیبانی از SOCKS5 ،SOCKS4…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5777" target="_blank">📅 13:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌐
افزونه Advanced Proxy Manager منتشر شد!
📌
اگر از v2rayN استفاده می‌کنید ولی نمی‌خواهید کل ترافیک ویندوز از پراکسی عبور کند، این افزونه می‌تواند فقط مرورگر کروم را به پراکسی متصل کند.
⚡
اتصال مرورگر بدون تغییر پراکسی کل سیستم
🔄
پشتیبانی از SOCKS5 ،SOCKS4 و HTTP
📋
پروفایل‌های آماده و قابل ذخیره
📶
نمایش پینگ اتصال
🔒
کاملاً لوکال و متن‌باز
💡
مناسب برای زمانی که می‌خواهید فقط مرورگر از فیلترشکن استفاده کند و برنامه‌های دیگر مثل بازی‌ها یا نرم‌افزارهای بانکی بدون پراکسی کار کنند.
📥
آموزش نصب سریع:
فایل
.zip
رو از بخش Releases گیت‌هاب دانلود و اکسترکت کنید. بعد توی کروم برید به آدرس
chrome://extensions/
، حالت Developer Mode (بالا سمت راست) رو روشن کنید و روی
Load unpacked
بزنید و همون پوشه‌ای که اکسترکت کردید رو انتخاب کنید. تمام!
🔗
لینک دانلود و سورس‌کد در گیت‌هاب:
🐙
https://github.com/johncarterjourney-rgb/advanced-proxy-manager
👨‍💻
Dev:
@Bachedev
#Proxy
#Extension
#Chrome
#V2rayN
#OpenSource
➖
➖
➖
➖
➖
📢
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5776" target="_blank">📅 13:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKDuQELWb2DjWeHrfMZHY_6yGAxRPWaAz4zIFLbU_VbVz8DSR1XA3gdvI5zh6N9o4p8cMDza91lw_eBY0XLEDqv1QMEWwlTYL0d-gSWDDiwVYVkb4Gzu228ILmAP0-bGMpZaIb3lMQ-jvdXCoi1yYGH5bfgkRwsPkvPw4VdFYQIfdp1w9DWd3gSK2eZUInPkTZvyahKOlfKY4spAi6QT0XxwW0xXF8h8fM81o2z6cY0ORH5aepIN0Xd54xOfHSo1GtGRIwc6O3YnL1eJrlgvVikitkh-XIqq1woP_Slft7Xgd0kIfinMChlvdiIBukm1_s7RrYHF7knS9hnEbiutdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی کردن سبک هر وب‌سایتی
👀
⚡
ابزاری که هر رابط کاربری را به یک فایل آماده برای استفاده در گردش‌های کاری هوش مصنوعی تبدیل می‌کند
🕤
کافیست لینک یک وب‌سایت را وارد کنید تا این سرویس به طور خودکار رنگ‌ها، فونت‌ها، فاصله‌ها و ساختار رابط کاربری آن را اسکن کند.
🕤
این سرویس از صفحه اسکرین‌شات می‌گیرد و همه چیز را در یک فایل مرتب به همراه جزئیات طراحی گردآوری می‌کند.
🕤
نتیجه؟ یک پایه آماده برای تولید تصاویر مشابه با استفاده از هوش مصنوعی.
🕤
تنها کاری که باقی مانده این است که فایل را به یک مدل هوش مصنوعی بدهید و آن سبک را در پروژه خود اعمال کنید.
🕤
این ابزار رایگان، متن‌باز و به صورت محلی اجرا می‌شود.
https://www.designmd.supply/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5775" target="_blank">📅 12:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ss://YWVzLTI1Ni1nY206RmpHM0lQYm55KzBaWVU0L3AxdlVMUDg0R2NLcEdvWnBXS0FheTE2VmhJdz0%3D@51.254.128.106:2083#%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5774" target="_blank">📅 12:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">trojan://humanity@188.114.97.6:443?path=%2Fassignment&security=tls&alpn=http%2F1.1&insecure=1&host=www.calmloud.com&type=ws&allowInsecure=1&sni=www.calmloud.com#%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5773" target="_blank">📅 12:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPViQUoYKr-PVQhD6OFAtSAtYnTBuracB4Wvb2qv5ZSOkH93Y0mIoRYGn4u_K6DmivDUHjYAZiINDRL5oIGJ7R37vRofj-Ubxag8jXnZoITLlMxN1nyDRVHdahIDnP1aHD3oOZNmGWcE4Ut1HUwZBsIuh1myA1x6S1QvdJM9QXgcuDbFZEYfyt9aqjit8Q4ozOG2oRdOUzn3qT0Exw6x3r7adDt0QuLj2FpgkFReVa78br0v80PiK-EjHPuzKxUQhTtBfcFkk1YW8Y90IXxcvK19lSWK1JiLgbh-cRjG4F7yvm0VR5WhDXwtmJT0RSurTqqzGEbERAKD_uuTH0KYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ابزار جدید برای پیدا کردن IPهای سالم کلودفلر!
📌
پروژه CrimsonCF یک وب‌اپ متن‌باز برای اسکن رنج‌های Cloudflare است که به‌جای تست HTTPS، مستقیماً اتصال TCP را بررسی می‌کند و IPهای سالم را با سرعت بالا پیدا می‌کند.
⚡
اسکن سریع و موازی
📋
خروجی آماده برای Xray،…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5772" target="_blank">📅 12:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔥
ابزار جدید برای پیدا کردن IPهای سالم کلودفلر!
📌
پروژه CrimsonCF یک وب‌اپ متن‌باز برای اسکن رنج‌های Cloudflare است که به‌جای تست HTTPS، مستقیماً اتصال TCP را بررسی می‌کند و IPهای سالم را با سرعت بالا پیدا می‌کند.
⚡
اسکن سریع و موازی
📋
خروجی آماده برای Xray، sing-box و Clash
🗂
ذخیره تاریخچه اسکن‌ها
🌐
ثبت سریع‌ترین IPها روی DNS کلودفلر
💡
اگر برای کانفیگ‌هایتان مدام دنبال IPهای سالم Cloudflare هستید، این پروژه می‌تواند حسابی به کارتان بیاید.
📥
لینک پروژه:
github.com/amir0zx/CrimsonCF
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/5771" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5770">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۱ ترا کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://2d0b825d-cbe0-46b7-98e9-e955b99e71c9@cz.helper-internet.com:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=W-zf_ncm9sYALF5EqvUsxqTkYGdAw-tQczT2SqwVMGE&security=reality&sid=ff776ff77be48b88&sni=cz.helper-internet.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5770" target="_blank">📅 11:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5769">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ربات های سرچ تلگرام
@MotherSearchBot
@en_SearchBot
@SearcheeBot
@argo
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5769" target="_blank">📅 09:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🤖
افزونه‌ای که کاربران Claude باید بشناسند!
📌
افزونه Tally میزان استفاده و محدودیت‌های Claude را به‌صورت لحظه‌ای نمایش می‌دهد و قبل از رسیدن به سقف پیام‌ها، وضعیت حسابتان را نشان می‌دهد.
⚡
نمایش تعداد پیام‌های باقی‌مانده
⏳
نمایش زمان بازنشانی محدودیت‌ها
📊
نمایش میزان مصرف جلسه و هفتگی
🔄
انتقال گفتگو به ChatGPT، Gemini و Grok با یک کلیک
💡
جالب‌ترین قابلیتش اینجاست که اگر وسط کار به محدودیت Claude بخورید، می‌توانید کل چت، فایل‌ها و کدهای تولیدشده را بدون کپی‌پیست دستی به یک هوش مصنوعی دیگر منتقل کنید.
🎁
نسخه رایگان روزانه ۲ انتقال را در اختیارتان قرار می‌دهد.
📥
لینک افزونه:
chromewebstore.google.com/detail/tally-claude-token-counter/baicaaiepddopbodaccgfffdimceidbp
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/5768" target="_blank">📅 09:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzkoEZrWHAgk5_2drYymBCEOmzuUy1bHM7A4_FjNd3s2JmRvY7y3Kcqj687wr3UUlCJCHyBPeqqFZTwcU9ODFqtulyNMvGKWvwJ6U1NaojsuKw5jEkxCbiuU6EyA78tZDiGx5Pf0p49NzZdovK3h-ITwQm-BpC1qxBuyfPrJQrcZlkPAOffPQPbodQGjyviFil_Vzqah6wotck89TH4jXa-Q6C4XRckhDQEdGvF2WsEoGd4esaqg3170md3wDLKCTljKwxIuaYnc6VNNWN4WPBbqr11uge3ea1777B80U-pNwCx3dBSFn2cQUDx3hL3kAKWh95GLgAAEh-u_AjFdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوق العاده</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5767" target="_blank">📅 08:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانفیگ نامحدود اهدایی یکی از ممبرای عزیز
❤️
vless://42adc67e-49cb-4c62-b6ec-1b26c33980e3@140.248.190.1:443?allowInsecure=1&alpn=h2&encryption=none&host=shahrvand.ir&mode=packet-up&path=%2F%3Fed%3D2560&security=tls&sni=speedtest.net&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF%20%D8%A2%D8%B1%D8%B4%DB%8C%D9%88%D8%AA%D9%84
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5766" target="_blank">📅 07:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">100 گیگ کانفیگ اهدایی یکی از ممبرای گل
🤍
vless://9146fb59-a4fe-4bb8-9a25-9eb5fc31f45a@a.harmonycodesign.shop:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=TAJxu6wnkIMcHn5KhnND8RiNJr6-q8zIQAwWzQdSqXo&security=reality&sid=8eb76dd83c&sni=www.yahoo.com&spx=%2FiQkeLHgmqtVGmzs&type=tcp#test%202-100.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5765" target="_blank">📅 07:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvKwmDv3sI_w4stkQZwoMxkLJXHIYal2oE_-WS8oMPzzG1LjyTTcCOrIV7bEsHsBH6J99VPGft--CTCzJmTdmBlYaB9VQU2zHVkYeYI4jUNAQW00VIKelj9clSz_GkWfvQW3XMia9NaCAnXrKVfQ-8PyjkaDWUiGvuPG3jAx2RMTvtmVCKhd3PZFVbSiIfKVl3wRz3TV8HNfAFyEjauLbmy8atvhyBLrAh4xo9U1R2P2s3HWOEI0gbJnilRlKnK57EAKtQzrcVENeCI7Z1KW87qzH0xVK25w1Vuz1En3DzlApzrP5-tVBhwy03OM1F1WGc7VtEKWQjP6HU3685NAiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت
گوگل
شما به صورت پیش فرض روی
3 ماه
قرار گرفته تا اگر بعد از
ماه سوم اکتیو نشدین
از
دسترس
خارج بشه
🤩
توسط لینک هایی که پایین این پست در دسترستون قرار میگیره میتونین اکانت های جیمیل خودتون رو روی
18 ماه
تنطیم کنید
👍
➡️
https://myaccount.google.com/inactive
➡️
https://myaccount.google.com/inactive/inactivityperiod
💻
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5764" target="_blank">📅 02:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@archivetelll.npvt</div>
  <div class="tg-doc-extra">6.9 KB</div>
</div>
<a href="https://t.me/archivetell/5763" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5763" target="_blank">📅 02:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ss://YWVzLTI1Ni1nY206RmpHM0lQYm55KzBaWVU0L3AxdlVMUDg0R2NLcEdvWnBXS0FheTE2VmhJdz0%3D@51.254.128.106:2083#%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5762" target="_blank">📅 02:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۲۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
ساب هیدیفای ، اد کنید
https://panel-01.sidin.com.de/NvBmpAnVK6fqJOC4hmd7eiSaJyLs/64d5ede0-8ffb-4636-9565-bf95515a479c/#اهدایی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/5761" target="_blank">📅 02:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5760" target="_blank">📅 02:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromOpenSourcePulse</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbRpOtppfVnd0dC1I7v1hgxDAYh36Wxkqqs9_UgKF50rBXLJcy3b31OQHK59TnBAMoRA3N34AbC7ndqPdk0TVNOH8mxa6XW2DqffUSccxFs3Qn-YOtru6tfk-JPUWcUZl-l2sA1SnxOkM61w-WZYm9BgF166Q05fFq874Y_IcAi3CCZmZzaOCvgspcgANhEGDzPFFc5k-L5q7h8eNhF_ZZyTWcFnHfRdZ_pSpHKH0qukNKxlJvtmIRKAtjp2gPr7UM9s-rrbEV-ZxJlgw_JIfl1oHsHSzjeJVrQ63yPX9c8wv2TxwyngwxkD0E9Gh25RXvdvujfaXh4ad0C2f5HIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
New Release Alert!
📦
MITM-DomainFronting
🏷
Category:
Community Suggested
🔖
Version:
MITM-DomainFronting v22
📅
Released: 2026-05-30 21:21 UTC
📊
Assets: 0 files
📝
What's New:
Add DOH; Add meta (facebook, instagram, whatsapp, ...); Unrestricted youtube
🔗
View on GitHub
📥
Download Release</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5759" target="_blank">📅 02:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">💣
بمب جدید اینترنت آزاد: دسترسی به یوتیوب و اینستاگرام «بدون نیاز به سرور و ورکر!»
رفقای آرشیوتل سلام!
🌹
امروز می‌خواهیم یک متد کاملاً انقلابی و تازه نفس (آپدیت شده در ۱۰ خرداد ۱۴۰۵) را به شما معرفی کنیم که معادلات فیلترینگ را به هم ریخته است. پروژه‌ای به نام
MITM-DomainFronting
(توسط توسعه‌دهنده ایرانی patterniha) که حالا مستقیماً به هسته Xray اضافه شده است.
این متد چه کار می‌کند؟
با این روش، شما برای باز کردن سرویس‌های مسدود شده (یوتیوب، اینستاگرام، واتس‌اپ، فیسبوک، ردیت و سایت‌های پشت دیتاسنتر Fastly)
هیچ نیازی به خرید سرور مجازی (VPS) یا ساخت ورکر کلودفلر ندارید!
این متد با جعل هویت سرور (MITM) و استفاده از یک SNI جعلی، اینترنت شما را مستقیماً و به صورت لوکال به این پلتفرم‌ها وصل می‌کند.
---
⚠️
یک هشدار امنیتی به شدت مهم (قبل از شروع):
این روش نیاز به ساخت یک گواهی امنیتی (Certificate) شخصی دارد.
تحت هیچ شرایطی
فایل‌های Certificate دیگران را روی گوشی یا سیستم خود نصب نکنید و فایل‌های خودتان را هم به کسی ندهید. این فایل‌ها کلید امنیت دستگاه شما هستند!
---
🛠
آموزش راه‌اندازی (خلاصه و مفید)
۱. ساخت گواهی امنیتی (Certificate):
*
در ویندوز:
فایل
certificate_generator.bat
را از گیت‌هاب پروژه دانلود کرده و در پوشه
bin
نرم‌افزار v2rayN اجرا کنید تا دو فایل
mycert.crt
و
mycert.key
ساخته شود.
*
در اندروید:
به سایت‌های سازنده SSL رایگان (مثل regery) بروید و یک گواهی خودامضا (Self-signed) بسازید و نام آن‌ها را به
mycert.crt
و
mycert.key
تغییر دهید.
۲. معرفی گواهی به دستگاه (Trusted Root):
* شما باید فایل
.crt
را در ویندوز (از طریق کلیک راست و Install Certificate) یا در اندروید (از طریق تنظیمات Security و بخش Install CA Certificate) به عنوان یک گواهی «مورد اعتماد» نصب کنید تا دستگاه اجازه تغییر مسیر ترافیک را بدهد.
۳. اجرای کانفیگ جادویی:
* فایل
MITM-DomainFronting.json
را از گیت‌هاب دانلود کنید.
*
در ویندوز:
در برنامه v2rayN یک Custom Configuration بسازید و این فایل را وارد کنید (Core Type را حتماً روی Xray بگذارید و Socks Port خالی باشد).
*
در اندروید:
فایل‌های گواهی را در بخش Asset Files برنامه v2rayNG وارد کنید و سپس فایل json کانفیگ را Import کنید. (گزینه Enable Hev TUN باید روشن باشد).
---
📌
چند نکته طلایی:
۱. این متد در گوشی‌های اندرویدی (که روت نیستند)
فقط روی مرورگرها
(مثل کروم) کار می‌کند. یعنی برای استفاده از یوتیوب یا اینستاگرام باید از طریق مرورگر گوشی وارد آن‌ها شوید، نه اپلیکیشن اصلی.
۲. در فایرفاکس باید تنظیمات
Use third party CA certificates
را به صورت دستی در بخش Secret Settings فعال کنید.
📥
لینک دانلود فایل‌های مورد نیاز از گیت‌هاب اصلی پروژه:
[لینک گیت‌هاب MITM-DomainFronting](
https://github.com/patterniha/MITM-DomainFronting
)
🔥
این پست را برای تمام کسانی که توان خرید سرور ندارند یا از قطعی‌ها خسته شده‌اند فوروارد کنید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5758" target="_blank">📅 02:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
اتفاقات عجیبی در Bitwarden در حال رخ دادن است!
📌
برخی کاربران متوجه تغییرات قابل‌توجهی در پیام‌های تبلیغاتی و مدیریتی Bitwarden شده‌اند؛ از حذف عبارت «Always Free» گرفته تا تغییر در ارزش‌های اعلام‌شده شرکت و جابه‌جایی در تیم مدیریت.
💡
این موضوع باعث شده بخشی از جامعه متن‌باز درباره آینده Bitwarden و حفظ رویکرد شفاف آن ابراز نگرانی کنند.
🔐
اگر به دنبال کنترل بیشتر روی اطلاعات خود هستید، بد نیست نگاهی به Vaultwarden بیندازید؛ یک پیاده‌سازی متن‌باز و سبک که روی سرور شخصی اجرا می‌شود و با اپلیکیشن‌ها و افزونه‌های Bitwarden سازگار است.
✅
میزبانی روی سرور شخصی
✅
سازگار با کلاینت‌های Bitwarden
✅
متن‌باز و قابل بررسی
✅
امکانات پیشرفته بدون نیاز به اشتراک رسمی Bitwarden
⚠️
فعلاً هیچ تغییری در امنیت Bitwarden گزارش نشده، اما برای بسیاری از کاربران حریم خصوصی، این تحولات ارزش دنبال کردن را دارد.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5757" target="_blank">📅 01:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">30 گیگ کانفیگ
🇺🇸
vless://02b0ce21-e1b0-456a-b26a-746948db90b2@104.167.199.250:21886?encryption=none&fp=chrome&pbk=lCJf5rHYWjlRoBt04knpHb3PJKX6lpmdnq1Uk8le6WY&security=reality&sid=6812cc8489&sni=www.yahoo.com&spx=%2FtVArRVlBAtoiJnE&type=tcp#30%20%DA%AF%DB%8C%DA%AF-30.00GB%F0%9F%93%8A
@archivetelll</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5756" target="_blank">📅 00:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">50 گیگ کانفیگ مولتی .....
👾
💀
vless://61ff07a8-9f1d-4bac-a9a2-37249ad3a5b4@104.167.199.250:21886?encryption=none&fp=chrome&pbk=lCJf5rHYWjlRoBt04knpHb3PJKX6lpmdnq1Uk8le6WY&security=reality&sid=0febf6&sni=www.yahoo.com&spx=%2FAbfBgvqwqJDzQOU&type=tcp#10%DA%AF%DB%8C%DA%AF-10.00GB%F0%9F%93%8A
vless://1b16b6f8-b8dd-43d7-84f9-8eb8a7e15504@sina.35o.ir:25645?type=tcp&encryption=none&security=reality&pbk=GnAQ0pqW4HGqMuOY7crTmcQ56FuABKPP9YaiJzOS3X8&fp=chrome&sni=www.yahoo.com&sid=d6372f1a0a&spx=%2F#..
vless://cb61a314-9e39-45b5-bf3b-264912e7553b@panel.96s.ir:8080?type=ws&encryption=none&path=%2F&host=&security=tls&fp=chrome&alpn=h2%2Chttp%2F1.1#%DA%A9%D9%84%D9%88%D8%AF-%F0%9F%91%BE
@archivetelll</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/5755" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
😁
❤️
مولتی هست ، همشو اد کنید
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:35503?encryption=none&fp=chrome&pbk=kg3m6BZFVDfMlVFmB_mGcdt8DSep31F80p5HFcftbhU&security=reality&sid=25d3055f&sni=www.yahoo.com&type=tcp#-50.00GB%F0%9F%93%8A
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:34409?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&mode=auto&path=%2F&security=none&type=xhttp#50%20GB
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:51796?encryption=none&fp=chrome&pbk=j8GasBT0TZtEb8wnWUqydRpfhJ8hYENOGSTMPOCkZgY&security=reality&sid=04f58eb4&sni=www.samsung.com&type=tcp#50%20GB
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:80?encryption=none&fp=chrome&pbk=MSuNU70q36Ubt3AsmqUNYq4xreSxZOzGkIHsUt8SVig&security=reality&sid=5c20c9b00ee2be&sni=www.yahoo.com&type=tcp#50%20GB
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:37424?encryption=none&path=%2F&security=none&type=ws#50%20GB
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:443?encryption=none&fp=chrome&pbk=jPF_6gmAt1CFrD4DSoe8vl3SeEYjYpEaU7nt8JYsWUM&security=reality&sid=2a5fc7667f&sni=www.samsung.com&type=tcp#50%20GB
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5754" target="_blank">📅 20:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">​
🚀
آفر ویژه و اقتصادی سرور مجازی (VPS) از شرکت آمریکایی RackNerd
​اگر برای تونل های DNS، بالا آوردن پروژه mhr، ساختن تانل یا کانفیگ‌های شخصی عبور از محدودیت اینترنت دنبال یک سرور خارجی باکیفیت و از همه مهم‌تر «ارزان» می‌گردید، این تخفیف‌های سالانه رکنرد رو از دست ندید.
​
🔹
پلن ۱ گیگابایت رم: فقط ۲۱.۹۹ دلار «برای یک سال کامل» (یعنی ماهی کمتر از ۲ دلار!)
🔹
پلن ۲ گیگابایت رم: فقط ۳۵.۹۹ دلار برای یک سال
⚡️
سرعت پورت 1Gbps و پهنای باند فوق‌العاده بالا (۳ تا ۵ ترابایت)
🇺🇸
آی‌پی آمریکا
🎛
دسترسی کامل روت (Full Root Access) و مجازی‌سازی KVM
​این آفرها توی بخش عادی سایت به سختی پیدا میشن و برای مدت محدودی فعالن. از طریق لینک زیر می‌تونید مستقیماً وارد صفحه آفر ویژه بشید و پلن مورد نظرتون رو با همین قیمت ثبت کنید:
​
👇
ورود به صفحه آفر ویژه و خرید:
🔗
https://my.racknerd.com/aff.php?aff=20075
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/5752" target="_blank">📅 20:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5750">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ss://YWVzLTI1Ni1nY206RmpHM0lQYm55KzBaWVU0L3AxdlVMUDg0R2NLcEdvWnBXS0FheTE2VmhJdz0%3D@51.254.128.106:2083#%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5750" target="_blank">📅 19:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5747">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۱۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://599fc8a8-a939-405f-a755-922381ffa3ba@172.234.105.250:56845?encryption=none&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5747" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5746">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAfBvt5mbHAUSBrqLYIH_jS4vspQbho-HIeqtpHY0i5VG7qhuHcziBxn_fUG3iGL8iMmVMoDH4ZoiqpS8NkNvZrb6QQEzYgELVHkXeygccSm9HdRlHLN35M_m78BEAOfrv6xxaDsAfw88GuZkIPCb_RK3ZFvMgl-DCecoiO3Y1v3r0VuMtsZyuMXICB9DO1WalPe6_ccTFFwuN1bTmG-EFu1AoUBto1Z_B-jFE_NjmMEiPhWC9CxbF4WOpRZIeD0bjPkkDtKzWjHG9AD7AstXvRELjo3CbhClrDBEAxzn7oKfprV9_pKNfp_sCsxUwCFJoQtLyy0ZO3r_zd-Aw-PDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس ProtonVPN اعلام کرده که با شروع اتصال اینترنت کاربران ایرانی، بسیاری از کاربران شروع به ساخت اکانت در این سرویس کردن و تعداد اکانتهای ساخت شده در ProtonVPN توسط کاربران ایرانی، 25 هزار درصد رشد نسبت به حالت عادی رو شاهد بوده
🤔
✈️
@Archivetell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5746" target="_blank">📅 19:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">10 گیگ کانفیگ سرور هلند....
🇳🇱
vless://60eab5f4-e085-49b6-9d1b-2e9122dcb6ee@panel.96s.ir:32373?type=xhttp&encryption=none&path=%2Fmarg&host=panel.96s.ir&mode=auto&x_padding_bytes=100-1000&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&security=tls&fp=chrome&alpn=h2%2Chttp%2F1.1&sni=panel.96s.ir#10%DA%AF%DB%8C%DA%AF
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5745" target="_blank">📅 18:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlFwNrAkHM5sru_54AOzgcZc2FWjoKn5IkXd16rnTnoCscLKsH1G2dDNoQHCq2kt5Wc0ngEy5R1Ro2VYP2zAyOsRiU0GJOw2nzB8jIGIu1_api1Wk0JvfDu6jcX2mQAUvxkAL7O__SYJtXa1e073M4evKLLBXmBr86iPO2PkwBuRpCa7iFdYwFiI9xjHPe4DryXiALPKD4J9nbT756pwAwEPj76FxSIJLtSFUPqT1h1tvg7SWaDwxLPO_90wN1Ss2apYwslCv0pHuIndwUewGhXiWMA-l3sMvITRELp4y2uwYfbRciXNZTQDqFg1c-w7Y0CI_6yQgzIEjbhGIhliDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMoQhJebc_OaK0BlalU9FEWNcRGEaetADbEJMjYYd8gPi0Kr63axYo7AntCAgUj9ZrxPffcB7FveNmT1gUmo8z-jIV5daaxHAkrmV6dC9TfPWLDU5E68HpZkWGhpaWwh4Gcxw4-_LPmqdHR2zBkyz0qCy0g6PmFLyM7QlwWPOQzUKqUpD1etUa71yWb0b-iBG6kxt95iKYI4r3eBUf8hbeifiMYI1MYMQue5_B-wp79HgiLKbeJFDXTjDYkpYI8Jo20F241vVLoDyMqKigild0psmhqs2r8PegakbSmTx1GlaJffJwUuvpEIOeIF4Ir47akBfv8KRlOL0GxRV2K2DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9846908dae.mp4?token=ghtT2fIZhWMUvLot9jlCzVJ9I9v2tuH9vMUI4dmb48tGji0j8hk60nPNupx9rErfm07OJEkiaRIULdYJ83rfBhyUWlLP-19kXqnXnpHzAOOrPbLBJXYYu6T8cZpKtXwaDXuBxruZnXnJ4A493dL9AkmW5LjJeGNlfhuZ1RNlhqNDm-6z9AnJwkfOHjGV3Pl_fd_-aCYH3SywEsPxcT70Xvj-P72e1u9WoT4WvChDDedocUgtJM1fU8e3DihGPl5FX1mBH3EkefCS3JBVmYrBAGZ32WDocOe50KwzUFfjUZgcorBVRHDnt1ZbuTogFaJjDsf9XXsIdcoBYTgrTz847TcuqZTL51MjCDWXHmnRD8vMALGRXvK1HP5EI63DGU04NoojRkRAS9OL1xaqQ4ZalDi0VvTV6v0Byf65tfATSZn7WePGNATAlabPiiyZzM516tSAwAl1jq4A4z05bQKXpNB_V2zHWEdRJ1tcDIsbbbOj2HVTOvilbG1bPN4N_2fIrGgJT2IjulUCGzDNV_bogsX7cLBF1ytWt44z2Ayd6AoBHC4hOi5yfWd3Ca0O4rNLsti1gZ74_6aR3UcI5HsR2OhLS6yOa_Lt98FKjHaAwOhTUpTrHf91CpJwJ3yW-Lr6HXa8HaRHhnaG36FzuiHiecfZDP0gV-YsWZFVDPIC2wY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9846908dae.mp4?token=ghtT2fIZhWMUvLot9jlCzVJ9I9v2tuH9vMUI4dmb48tGji0j8hk60nPNupx9rErfm07OJEkiaRIULdYJ83rfBhyUWlLP-19kXqnXnpHzAOOrPbLBJXYYu6T8cZpKtXwaDXuBxruZnXnJ4A493dL9AkmW5LjJeGNlfhuZ1RNlhqNDm-6z9AnJwkfOHjGV3Pl_fd_-aCYH3SywEsPxcT70Xvj-P72e1u9WoT4WvChDDedocUgtJM1fU8e3DihGPl5FX1mBH3EkefCS3JBVmYrBAGZ32WDocOe50KwzUFfjUZgcorBVRHDnt1ZbuTogFaJjDsf9XXsIdcoBYTgrTz847TcuqZTL51MjCDWXHmnRD8vMALGRXvK1HP5EI63DGU04NoojRkRAS9OL1xaqQ4ZalDi0VvTV6v0Byf65tfATSZn7WePGNATAlabPiiyZzM516tSAwAl1jq4A4z05bQKXpNB_V2zHWEdRJ1tcDIsbbbOj2HVTOvilbG1bPN4N_2fIrGgJT2IjulUCGzDNV_bogsX7cLBF1ytWt44z2Ayd6AoBHC4hOi5yfWd3Ca0O4rNLsti1gZ74_6aR3UcI5HsR2OhLS6yOa_Lt98FKjHaAwOhTUpTrHf91CpJwJ3yW-Lr6HXa8HaRHhnaG36FzuiHiecfZDP0gV-YsWZFVDPIC2wY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
اگر با Claude Code کار می‌کنید، این پروژه را از دست ندهید!
📌
Claude Flow یک مجموعه متن‌باز از ابزارها، عامل‌ها و افزونه‌هاست که برای توسعه نرم‌افزار با Claude Code طراحی شده است.
⚡
بیش از ۱۰۰ Agent و Skill آماده
🧠
فریمورک SuperClaude برای مدیریت پروژه‌ها
🔌
افزونه‌ها و دستورات کاربردی
📋
مدیریت پروژه به کمک Agentهای هوش مصنوعی
💻
ابزارهای CLI برای کنترل و هماهنگی Agentها
💡
اگر از Claude Code برای برنامه‌نویسی استفاده می‌کنید، این مجموعه می‌تواند بخش زیادی از کارهای تکراری و زمان‌بر را خودکار کند.
📥
لینک پروژه:
github.com/ruvnet/claude-flow
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/5742" target="_blank">📅 18:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوستان، تانل تست کردین؟
سرعتش میگن خوب نیس
خوبه؟</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5741" target="_blank">📅 18:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/recUxoiQ9zb8PBuPFoGVHI1AHV2ufHnTbjMpDMb3bDTX9TGaqY_RNwJGZ4ihc6oOzfOVD1zHS6j8a0P2DIKpKGoLrSyevyTIc95uk_J2vqh1hW7cHTLoPwan8yrgvtugB2Rn-V9n2QC-zJqSYVFMHQhOcV_LT84gaT73joZdprFaQtQwrC1C8Fa3oiimcsVmEvy1SmBr07E9PhQQjBg-wXrNZ4ObYqG5v3ptCAHMtS7EVMatFHOUJqKquQ3AmcxZL8R9T1baehzHYkzgD7H1MgdrTkwnoY3HWUEHRNL5trheMHmfdnml4KR_d8R-kkKz_JRNhS--pa7c7_i4CXA2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Burner Emails
پنهان کردن ایمیل واقعی خود —  آدرس‌های یکبار مصرف را در عرض چند ثانیه مستقیماً در کروم تولید می‌کند.
https://burnermail.io/
🕤
هنگام ثبت‌نام از ایمیل موقت به جای ایمیل شخصی استفاده می‌کنیم.
🕤
تمام ایمیل‌ها به‌طور خودکار به ایمیل اصلی شما ارسال می‌شوند.
🕤
آدرس واقعی مخفی می‌ماند — سایت‌ها و سرویس‌ها آن را نخواهند دید.
🕤
از اسپم خسته شده‌اید — آدرس موقت را با یک کلیک غیرفعال کنید.
🕤
به عنوان یک پراکسی ایمیل کامل برای حفظ حریم خصوصی و محافظت در برابر هرزنامه کار می‌کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5740" target="_blank">📅 18:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رفقا سلام!
✋
در این پست آموزش جامع راه‌اندازی اسکریپت بی‌نظیر CFnew (نسخه 2.9.8) رو براتون آماده کردیم. در این آپدیت، تمام باگ‌های یک ماه گذشته برطرف شده. این ابزار روی کلادفلر (Workers و Pages) اجرا میشه و یکی از کامل‌ترین پروژه‌هاست.
🔥
ویژگی‌های اصلی CFnew:…</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/5739" target="_blank">📅 17:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URuUc9eSa594mhON-exLSu6a16Q__mekLOjxNhCHLNvzcSEPMUAyf77ZQ1L2aPygZWNZ098CLZtiZN5R6t6xb6xLsAstQFn9i834lD4pxIX8pU-YPw-Af5-aMrTTSYZu23tgPAHzHO2hOM0O8EwnQpP-QjsEjKaUguNL2M4uHBVWegAKyLWXKEPJSmT_HsjBlPWTQn27o_54Qu2lS589YyZz-r07w5t44LsNRwTQ9YNzQdgZYw6F-b5dm6k8wDsfS-LqYic3-eCCayqvCOg-KMUCZ5jv8tpMbLI5OLXpqVX8VBSZeEyH8nmgvlBnBfAVKKtB1hDOqErFo43B6hNuCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر تو متود Sni spoofing درست براتون پینگ نمیگیره و براتون
➖
میزنه از قسمت :‌
Settings
➡️
Options Settings
➡️
V2rayn Settings
➡️
Speed Ping Test Url
رو روی Apple ست کنید
✅
❤
@Archivetell</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/archivetell/5738" target="_blank">📅 17:34 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
