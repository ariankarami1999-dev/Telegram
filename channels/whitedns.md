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
<img src="https://cdn4.telesco.pe/file/SsngmHEbUruuE5taW7GhUkjEXEo5MIzggFVah1afcNZXX_RhK6yLElbCMuiYwN2KhIudrcjh29pUVFjQQuIFmU1Lhc3oKbuqc0SkZcjmMQRDZ-e3oO_gD5Q6l6M-bHh0sbgMAiG7MkFCv2CXpe7_UPgnA98R8xQH5sNpEJXzWYGpEClebpp0t3tckf6ndwvY8npGpyrYiDFzGL0gnUdn8uoKAqiPNfWaXYo_oHkH9oyQ03JcnJ3HnYua7gN0SfaDceU0xUEc6vNye8YJKmb6cNjCHywxRGmApe-YyxL9NL6qlUnfz_I1cibBo0QoIEPKIi-ef517GpxQvo2a91q6nA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 99.5K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhisperInHeaven</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔥</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/whitedns/870" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اگر در اجرای نسخه مک مشکل خوردید دستور زیر رو اجرا کنید
xattr -cr "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/869" target="_blank">📅 12:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-linux-amd64.deb</div>
  <div class="tg-doc-extra">19 MB</div>
</div>
<a href="https://t.me/whitedns/865" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/865" target="_blank">📅 11:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/whitedns/861" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/861" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmat4-gwLG_lmdSGjUHxe5pdXkNxFAHpfv3gYbfZfR_zx2mhdyE1CDO5HDa3EMtjcgnOvhlU0b-mL8b8aFA6sEfDqbw-_b7iBCUWzL9Ho3kK9X5kRK_GGw-GxtCnoRKL7BNSK83_KzXdotUqgtUED10TulCfXqaIYZ2jcDbCGfAEKSqvtovOm5bAGweWFk2IbL2Rr92GC7ve7nnXgsjFPSFNfGi2IHJbJF5ycE9P8MuhEfDDPbDcIz3LctBRT1zUawgBryrUfMW395wNiDRHJ50sB4DUaaJw3k1s4yGzurk0uZIhcGMTXpkffmZFU18dB59Y7q9DR4gcHuMoZBlBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
انتشار نسخه v1.0.0-beta5 اپیلیکشن کامپیوتر WhiteDNS
⚪️
تغییر هسته از Sing-box به Xray
🔴
اضافه شدن امکان اسکن آی‌پی‌های شرکت‌های زیرساخت ایرانی. با این قابلیت، اگر رکوردهای A+، A یا B پیدا شوند، می‌توانید از آن آی‌پی‌ها به‌عنوان سرور برای کانفیگ‌های خودتان استفاده کنید. شما همچنین میتونید لیست خودتون رو برای اسکن وارد برنامه کنید.
⚪️
بازطراحی بخش کانکشن‌های V2Ray. این بخش حالا برای مدیریت تعداد زیادی کانفیگ مناسب‌تر شده است.
⚪️
اضافه شدن امکان Speed Test برای کانفیگ‌ها.
⚪️
اضافه شدن پشتیبانی از پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، Hysteria2، WireGuard، SOCKS و HTTP Proxy.
⚪️
اضافه شدن قابلیت سفیدسازی کانفیگ‌ها. ابزار جدیدی در بخش Tools اضافه شده که با وارد کردن کانفیگ V2Ray، آن را به کانفیگ‌هایی پشت آی‌پی‌های سفید سرویس‌های مختلف تبدیل می‌کند. همچنین می‌توانید لیست آی‌پی‌های سفید دلخواه خودتان را وارد کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/860" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqMvDxgnaRI2QOJ1MM3e46hfXulrTFWbc7Zi-uWapnWvq_R6l_6ZQf-bC-UuxThfjaKIptozRyXFykzJSu9DWi_e5c1a2WlofnUw2V8IljpGTJEj2KA7tddbtgWSMBXmt4PPHW1RzWkFrm-4jF_QSgax3G-e3go0SUWqVijvzVji3hlumD4xao7KzNXUewIE9qecar5ah2IZU9t23N6jqP7JJo092UyWYe8YEMLnEXwuNRzqYKSWNzUvwSywR0qSUNVFaJuFaeHCP-vSh0oyEojAwo8Fm-O6VzwXug0M2s50noBSpBd0sTS4hsyjcNfQjSJctn4fY3vCf6ZLAGfg4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/whitedns/859" target="_blank">📅 04:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/whitedns/852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/852" target="_blank">📅 04:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">☠️
پروژه‌ی SenPai Scanner — اسکنر IPهای Cloudflare   چی کار می‌کنه؟   از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.  چطور اجرا می‌شه؟   فقط فایل مخصوص…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/851" target="_blank">📅 03:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-850">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gUDkReCCci5KfUhhNZ4FDaN9qXhQbYawL8TJz4DKye1diGxi8utefCZ0tYQoJlPkgzlFPtSA-1RGRY4W_zUtsU1jTcay6BcsqzDJRhAQ2Hnp2Gi-lPgDu1UZ4_YKMUL436pJ9h7kNGbnPO2_Yl5nfdu5vcLobind0wGpNKKIvjprC7YE88gsujR3dSvZSMQJb4aVhSRVE2f5CjjEpqbRvCLkNwgLIixUO2xzxNXma75LmgN1BOBfkbHHDjZuPZ2E2md7KA7_gA9Ql6mv_c1HHzfJBQnIYu0X1dnfp3aWPCZNqXyiicsCEXfjg6wtslfFV0t9nM1LEq3zLISoalD2GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/whitedns/850" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCbeC2-N4pg8dAXJCS4rILS_yKT8x-CDs9DYhnTNTfBQYiCrO5bvLEW5K_LtrQMISeNRsM5HilbK4Y3Z5bfXXRSU3iFdCILwy9LwYcEDF2zI1-UbtBBd8UeSzAroSBtLBg-SDUneB7r3nHG6KPYg36g-pJe0fN8z-cIVpaHlxsMMTwY9puzO6NELSKekpaI0Yxo49kf3AWnYNVBqquGOSLLy07a3H6AsmOZNgJsiK7BW5wfk5SRLhKnRE5K2izTzPapMfd2A0btNH7r_w1U5dYagl-lBYCpNQgQm6-fvvWfkTACJhf81clt_Yq-WUkABNUiK_93-6Wa6hOEKJ4SfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/whitedns/848" target="_blank">📅 17:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/whitedns/847" target="_blank">📅 14:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-841">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/whitedns/841" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/whitedns/841" target="_blank">📅 13:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/840" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JvWu1EMKxi72S2T-Zmo82P7EQfeuIK0At_uW-5yFWogHJm7Cujqtyb43-PaRoV0aMZLkfgxUcpiVvyL4wl5Ud6JPRaXA3qC2E6-rTe79-QqHc0YLkqfnFfyVyK9rxkK20AmTwea9JVKYA_zul_DLXOcWvmj-b1mD4VLb48d3BxjWg8dcdnV-N_ekDcJzeHytgeSyxMm_MLClR-OLs39v-DXUCbd9J2r4NheBEYjnWOcmftcPazvYH2xicTDkDmjnezmljqBj2SNqlfZO1JeV0oNnJmcYNh6kdZSv1zHDuaiYJVJQ2lfl1AJ7wa7A4VAzr66YplzxmfR6ssLlKa7uBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/msdseKrNjc9rSeCbNiiNL-O7TtBP8k5S_OnAhKTS86Yi_bAAclmjFhEwBkgO-xkmu6V7YK2l7ELcVTsEFwY8mulcfTtziZumJjxRehZ3vxSR5G0rZKkBKsSDNKhWOJ7oTer1TB6wa0e_qc9HE00o18I_8gsabQA1cEPQUGlJHIplSbtSr95IOSIP8pHQGBfj54SQWGb91mXerbVZ203FDZJGL-iebnmyTg1YvcpCSLEYEA-nMn3A5mwnsJl39ViAzxtH1HmCmrQrISfKUxFW1hkUzGhoFjPiGKYLpLVvgawPeFfwK6FLsVJ7N8EXx18waZqo-IUxhm5qsA686vFZuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sSAQ53a91I0HoS5hTVZRBQ8D6T4WCPUOJFekqPAo1puyd6KwROFshKiZQjmyZ81Jd2itYXu8wDtIqGKjESFSVqFzNiV7_18WdwaJm3HtoYZhgCbKCiPjsgwJRNqZnEhaE8TGuXIuomS_K2B-RTpNnz5F7XIUg0U_XuWXkD-8AVQRkdrXTLS7kFH6Smu7nNqlZaGIO0qYaw-Qggy3efRvLl_VEc6HRhDlGfiTEtGwiXczbUSXePj1RP5FEjCbSLWJksES4G8BuWXcds8WNCfZe_-BFkPggloPiKBmWyEITJzSifeNltGS5l0tGsjHUMNFr97cZfgCh3CYzfgFL07w5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yb61Sb__qmxfnnUI3KemK7VOdK6PW1sp4ps0z1Ifr71jUVyNkau0st2zYy9xzbsQ1QMsRTi9seFAcUrtXXss58_3xWDKRT1Jnx-DKXCHyrk2vAoPmfr2zLDGVYfN6m1qAcldub9Y--_YiST-QNj0aZTA1YHDAdYOsvnIVIqpP_vy0ldVE3IA0FWbpJDeMnyW4KqUQ-asnB_V-v9mukC2nfOVz2s3oMx7xSDHhlxj1A0ay25B8VkR6mhQ7N8vBgkOrAQoXrKu30mdpos4wax2MGSl5MlI1_mECC3E9_VUUiEEsdDcCtgbOnjwUXlcrn4cHbR6jVf6K45zWSriBn2CdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GYKltEZ1z9DE7bNXL5hAew35edC6kFhXyYCYPptSaSdqTTudaYOGM3UnKsIRt_eSpziAb2hGLMpSYUjgROE_nfWSA2a4sSKPquJqOyPm_NkoN8CTUTxxd3t4WEZRB86r0vta9mnesr8vPYpNz3QiGB5DxZ8XLt6AkEhGDHYAPMk1IHmsTwx32B6iotsN2FZwUw3T6q0_Ki4G96s9_d156XJg_DJFlG_hsvKen51cHJ2ZwlXX3iVuqvu9OUO4McyqSiN2PVSDB9hExudr66dMfY3iqKDuFFZdRICa0GwjWSxVK1tWbY-YeSJ1e2Mnei8UHA9AM0RdtpBNEpK2SnQUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gMVeTvnFsQ6x946rbZrohLwlv-kstmvYrg9PqK99yjNix7KvgWN2Yd3bcTkHcOLaduPNmAYg_drkKrgIveYy5u5ULbD_vXWfoptBjb70UM3pGRyffvHdZN9Uoqa4L0Bes8jArjCF4VcygKqGzFeE8c9HmIMVB2MXnTwcd5C8dOhJka9CpdbkU07RBb9e4-gUWS51jwcJonTS1x0mbCc8qUKLHctj7s2yeZDEmXe5ywTiGI5jyXTQoM1xqAuwOo4mWT6kUb2OFvv3hih3k-_wORnlCfe7AACOXSxpb_dG_z1PfYxDv1k1nStpANv06muyre32A2ZCKlfdLApZY0VsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DDD-o9lSHMbQ3Y4C3y66qXk3fPotcqQ7dL7nLb4mBjevYoFtX7K6T9UodqOhOi0NBT5pIAosSrtcapVGHrowxh3AWpHRr284CGvt5XEmBHlUylsVw08WwZR0c4k0tokmq7wFIFNCRlFI1eQA-nahgcirjeu9PsOjyynMCB44tVYx61X3n_7WkJkdRPyZ8jWhpx8jVaPsPfLGuvgbxzu9_frEz5bNZgrKKfS3khmJpqF_gI_SYb4xwX8WtHJU81pIqE_TTofxuLwsTo-6y_3dwVdf33BmnWw_ItzQV-qXRN7VwnI3C5KFXnS7Ap0FDPfn2lnoSTR3Fu24hGP8MsX0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SUE0SR2MRxropeFkiX2RydGmwvjx11lhzbomySaNwY4lHFDfr0Quj07KcADpEt3nVJjzka7V_c-2bhIv9L_uD-xvyVxcgsxNufM2s8zHeghPP2UxOYK5Tk-o49r7qL24tnKdfCTeYSupyDB-SgMNeZXlY7BTmngoLTKhJCyx8lOJ_BHskh7vT-vjKiCier78GdeRkjTZgMnU_t2NuLvqGvZVN9bAdqKyhKHp7UT0DBQcjkFS3B3DQMVt2IV6vy8lsTBNnLY6vJIvMf6N-nXNKUF6Ti6tJdVfBeUqVWfhO5W0eAR38Nl0HwEfXlC-YVBy1f7VPJZhrWrZYa_69N9k0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ooL7isWObcRwg04f7hf1naOEFP5zyugH4SbyJ3cPD45Xl-z62EjJtmupMU8A4J7jdnhiydGC6CDBClIAScC1hi5b2a5OCI32lD388chim4D9BVBixf7CWGjaVrwB3HT4tY1qId6UV9M4cgWqo-ZiFx3n3cblVN5YwRRLUECIblXKAIEOrt1z7yzveWrhjOnL_HjJEeaRpf9BlFdOFvrs1JUE-zuBXiuTbTzzIot8VHXSMKELjrZ75MK1wWCF-vfmFt--C_Iuji1JkhQ8ADWATfTqC1Yu4ri_UJm7BCvJG4b4VqZvnhMD__nflpnbg4i8ibYWkCcZ7pWykyey3X9t7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/whitedns/831" target="_blank">📅 13:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BECStTa85MRw1aGoJP4mLu7Wur_pxSraXfRpNN8SQbT8RdKRhEsnr2w3EJVnui79RJwcQHAX-hTYCYZx3OVDHK7PITZI62p4dKoGBea-Xa7XbnT29uQ22yM_UrfBaAFV5OOFOk4EVldT6p1_zGQNUnokvxkVMwFe0nBjJPD4iuih8ztELXBLbf2VOBUmHcCEErSaXuUCruYmlgLordWfmnRpYOP5zgRHQ9VH8KkL2HtmatuNhI82nY2GMHeKGfd6D8L8biTArk7moInviCRHXFPduLoR5PYTCAJOSRYuFMd5f0BUOTtCgSMeAFnAsyNOnu82HmgyEl8STB1u9ep-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/whitedns/830" target="_blank">📅 12:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-824">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/whitedns/824" target="_blank">📅 12:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-820">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-linux-arm64.rpm</div>
  <div class="tg-doc-extra">24.8 MB</div>
</div>
<a href="https://t.me/whitedns/820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/whitedns/820" target="_blank">📅 12:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-818">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/818" target="_blank">📅 11:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-817">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستانی که از نسخه اندروید اپ WhiteDNS  استفاده میکنند.
برای بیشتر کردن سرعت و پایداری
، میتونید با وارد شدن به بخش ریزالور ها، یک پروفایل جدید با مقادیر زیر بسازید
1.1.1.1
1.0.0.1
8.8.8.8
8.8.4.4
9.9.9.9
149.112.112.112
208.67.222.222
208.67.220.220
94.140.14.14
94.140.15.15
برای کم کردن مصرف
، سپس وارد بخش تنظیمات و پیشرفته بشید و‌مقادیر زیر رو تغییر بدید.
Upload Dup = 1
Download Dup = 2
اگر سرعت شما قابل قبول نبود، دوباره مقادیر Dup رو بالا ببرید.
توجه کنید که این مقادیر فقط مناسب اینترنت پایدار هستش. در صورت بازگشت اینترنت به وضعیت قبلی، باید کانفیگ های متفاوتی اعمال کرد.
ممنون
تیم White DNS</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/whitedns/817" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آموزش اتصال V2Ray در نسخه کامپیوتر
دریافت لیست کانفیگ ها برای ایمپورت کردن
https://t.me/whitedns/804
https://t.me/whitedns/805</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/whitedns/816" target="_blank">📅 11:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-release-windows-x64.zip</div>
  <div class="tg-doc-extra">23.8 MB</div>
</div>
<a href="https://t.me/whitedns/812" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/whitedns/812" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWPRrc4pRZBdZeMyH-Hje4_eH-r9e3tZUJfSfzvV8j-f0rjQ5Eor8k8v_au6i7UlBqGcHFJ7eEHAknCzfNHoWGEz2h3_HIFZG4nCnYCliLMmsNgylV3vGZdzlWGWOVCBtw7qEeDNbSvdxB3_rAulAxbxOTGeZKZlCiKdMx4luFAX0yu47SxgttT7JAGRnGsALcAFwX4req8rVLWU216tLc_X6omCbd9NdPqLQtksUp60Bg0ylqfVWHsdllzgyr_5sUTS_N7I9g8U8sasM9x0dASKQCb6LK2aUduwPZIV87OLNDq9VwGPZbfowP7tb70J4wk_U0XmPIpf-0TLcr03WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4
با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.
در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription اضافه شده، و ابزارهای داخلی برای مسیر‌دهی هوشمند، مسدود کردن تبلیغات و عبور مستقیم ترافیک سایت‌های ایرانی از شبکه داخلی فراهم شده است.
اتصال MasterDNS هم پایدارتر و کم‌مصرف‌تر شده؛ درخواست‌های تکراری حذف شده‌اند و مصرف اینترنت حالا تقریباً شبیه یک VPN معمولی است.
✅
پشتیبانی از V2Ray اضافه شده است.
✅
پشتیبانی از VLESS، VMess و Trojan اضافه شده است.
✅
امکان وارد کردن کانفیگ و Subscription اضافه شده است.
✅
آدرس‌های خصوصی و داخلی مستقیم وصل می‌شوند و از مسیر V2Ray عبور نمی‌کنند.
✅
سایت‌ها و آی‌پی‌های ایرانی با geosite-ir و geoip-ir مستقیم از شبکه داخلی عبور می‌کنند.
✅
تبلیغات، بدافزارها، فیشینگ و ماینرها مسدود می‌شوند.
✅
همه ترافیک‌های دیگر از پروکسی V2Ray انتخاب‌شده عبور می‌کنند.
✅
کش داخلی sing-box برای لیست‌های قوانین آنلاین فعال شده است.
✅
MasterDNS پایدارتر و کم‌مصرف‌تر شده است.
✅
درخواست‌های تکراری حذف شده‌اند و مصرف اینترنت تقریباً شبیه یک VPN معمولی شده است.
✅
سرعت اتصال بهتر شده و Packet Loss کمتر شده است.
✅
ریزولورها به گزینه‌های بین‌المللی و قابل اعتماد مثل
1.1.1.1
و
8.8.8.8
تغییر کرده‌اند.
✅
حالت تاریک، Scanner جدید، بکاپ کامل و رفع باگ‌های زیاد هم اضافه شده‌اند.
@WhiteDNS</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/whitedns/811" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Defyx VPN
🚀
یک اپلیکیشن VPN مدرن، هوشمند و متن‌باز که با Flutter ساخته شده و با تمرکز بر امنیت، حفظ حریم خصوصی و تجربه کاربری جدید، دسترسی آزاد و رایگان به اینترنت را فراهم می‌کند.
🌐
🔓
🔹
متن‌باز و قابل بررسی
📜
🔹
رابط کاربری مدرن و روان
💻
🔹
تمرکز بر حریم خصوصی و امنیت
🔒
🔹
مناسب برای دور زدن محدودیت‌های اینترنت
🕸
بروزرسانی جدید
⬇️
GitHub:
https://github.com/UnboundTechCo/defyxVPN
📂
@whitedns</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/whitedns/810" target="_blank">📅 10:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-809">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Orbot for Android v17.9.4 BETA 2 (tor
0.9.4.8
)
بروزرسانی جدید
Orbot 17.9.4 (2.7.0) برای اندروید منتشر شد
📲
این بروزرسانی، موتور Tor را ارتقا داده، روش‌های اتصال جدید اضافه کرده و چند مشکل اتصال را برطرف می‌کند
🔒
🔧
.
✨
تغییرات مهم:
• ارتقا به Tor
0.4.9.8
برای پایداری و عملکرد بهتر
🚀
• اضافه شدن پشتیبانی از Shadowsocks داخل خود Orbot
🌐
• امکان استفاده همزمان با پل‌های obfs4 ،Meek و WebTunnel
🌉
• گزینه جدید «بدون پروکسی» برای خاموش کردن سریع پروکسی بدون حذف تنظیمات
⚙️
• بروزرسانی پل‌ها و ابزارهای دور زدن فیلترینگ
🛡
• بهبود DNSTT برای اتصال بهتر در اینترنت‌های محدودشده
📡
• رفع چند باگ و مشکل اتصال
🐛
📱
مناسب برای افرادی که از Tor برای دسترسی آزادتر و امن‌تر به اینترنت استفاده می‌کنند
🔐
🌍
.
دانلود
📥
https://github.com/guardianproject/orbot-android/releases/tag/17.9.4-BETA-2-tor-0.4.9.8
@whitedns</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/whitedns/809" target="_blank">📅 10:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان سلام :
این یک مدت به همه سخت گذشت ، شاید شما اسم دو نفر را بیشتر شنیدید ولی بدونید یک تیم ۳۰ نفره بی نام و نشان پشت این کار بودند  توی بدترین شرایط از همه چیز زدند تا شاید یک روزنه کوچکی باز بمونه ،
ببخشید کم بود ، کافی نبود ،ولی در حد وسع خودمون تلاشمون را کردیم
یک تعداد زیادی از  دوستان پیام دادن ، تشکر کردند و گفتن ادامه بدیم ، خواهش کردند بمونیم
ما هستیم کنارتون ، مگه میشه این همه عشق و محبت را رها کرد
یکم استراحت کنیم ،همه با قدرت بر میگردیم
توی این مدت مراقب خودتون باشید
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/whitedns/808" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItlPj7MBuA4GDTVTUXMcSrQJZso5MecyKQ66GZ0ilopP7wFmlu1Ivaj94JE5dKTbJT_RLL86dOpF65Igm1Jt_yikNIvl9cIwehOzbifq2YU0nkQWeR1fJ43MGTTEYf81UmU_9TsGGUUhmvUyxrrR44PJUUzO0YvGC5vWN0sTNP70bYTC-ZZNTaXj3pV7gAhI7pt8VtKZUYP6x3CocNyjnUs4MOR_mG9LsVxI4dCB1rGP0lOG8Z04B92DW9-7-9cooNi3cXeduuS2mM0tLSSxkhM_kLaU0AUbCOfmVtHA3Emt7F7HBA1gHOfldtAmx5lEqlleFRMtE2BJpL2lGp6M2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#موقت
یادمون نره کسانی که از ظلم پول در آوردند.</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/whitedns/807" target="_blank">📅 19:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-806">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">برای استفاده از کانفیگ های بالا میتونید از اپ v2ray یا دیگر اپ های مشابه استفاده کنید
👆
👆
👆
اپ های قابل استفاده:
npv tunnel
happ
nekobox
MahsaNG
v2raytun
v2box
V2rayN</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/whitedns/806" target="_blank">📅 19:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-805">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayconfigs_with_WhiteDNS_2.txt</div>
  <div class="tg-doc-extra">30.2 KB</div>
</div>
<a href="https://t.me/whitedns/805" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">115 کانفیگ تست شده دیگه پینگ 100-200
ممنون ازعلی عزیز برای تست و پاکسازی لیست
@WhiteDNS</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/whitedns/805" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-804">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2ray_configs_WhiteDNS.txt</div>
  <div class="tg-doc-extra">38.3 KB</div>
</div>
<a href="https://t.me/whitedns/804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">141 کانفیگ تست شده روی مخابرات پینگ 100-200
ممنون ازعلی عزیز برای تست و پاکسازی لیست
@WhiteDNS</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/whitedns/804" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ba3aKEPxBYVmE_tSEFVQlpXhxsa8MzZcHGb9Qd9kKLBKS7gwPBjX3gjPosRPrRwynYzcD0CDJq77n-i0xoGTdEzy7vqOndiyRX0iiEdU5JHqylP0omqTgfO4JXFwjTli5_ouNB2d9k_BGbC4HLVFjIWG-m99kLHmWY7hxciOgfBaAw4Avjbh8Q7y0kP_Mc9iAe7NaAIlfi_UwcKs-q7TeIUsrjFXXLJI-5LR5R2AKfLEb_2OH80oWi3TfsErtUF1t_U2injgeEPxf1juFGnb_VrlHYTeqZmbQ15VECLLjy_rUJALymp-HMuwYB1bWYKAUj5ewmVO3608hfCrFaiXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UF8WysTa2M24Bk3EwE1RdEIoVSaZMe5aCYHwjsMDruvvozSgD21VkzzngRoaLu9li0BPYGJNqHGMIn1JUMjG1Toku3TM8e8gLgyvFJLa3pU10ur4-RUuGzUTb2fMds28OCtn3pVA11AxVzgIAULnhqTYsK1Mtwz5dD49Yi8iyoyGgWvECEGTKrI7g7p-k_99bGcuStsNocjxEMhc9mhh1JZzF7ySZT2-QUA7IsXWwLCBvpqW3CjaVs4MDIPAU3-Q4xndl4IdIQn2CYAnucyqd-B2PmAIVL4QawF6WChS_kp4YAtk-fFVcrHN95bedZPeqFNbUTwR_p1JbPfZOnVrqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این هم یک تست سرعت با ریزالور های درست و با اختلال کمتر
🤌</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/whitedns/802" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">“}
سلام خدمت همه عزیزان
❤️
امیدواریم این روند ادامه‌دار باشه و اینترنت به‌زودی برای همه اپراتورها به حالت پایدار برگرده.
برای دوستانی که فعلاً به سرویس‌های دیگه دسترسی ندارن، می‌تونید از ریزالورهای زیر استفاده کنید:
1.1.1.1
8.8.8.8
همچنین بهتره مقدار
Duplicate
رو کمتر کنید تا مصرف اینترنت پایین‌تر بیاد و اتصال داخل اپ پایدارتر بمونه.
حتی در صورت برگشت کامل اینترنت، سرورهای WhiteDNS همچنان فعال می‌مونن و می‌تونید ازشون استفاده کنید.
یادمون نره، مارو از کمترین حقوق شهروندی محروم‌کرده بودند. فراموش نمیکنیم.
دم همگی گرم بابت همراهی و صبوری‌تون
🔥
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/whitedns/801" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">در طول ۳ روز گذشته، کاربر های ما ۱۰۰۰ سرور جدید اختصاصی با ربات WhiteDNS ساختن
🎉
@WhiteDNS_installer_bot</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/whitedns/800" target="_blank">📅 09:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان گرامی :
ما هیچ گروه و کانال دیگری در هیچ پیام رسان خارجی و  داخلی نداریم
تنها گروه رسمی ما :
https://t.me/whitedns_group
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/whitedns/799" target="_blank">📅 03:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgsNtIfO9IKuzFFjUhF0JSUFcEiYo3kTLo0TcQp-2puVqMs4X0mGaQNopJwKEdannlQEzitCMyEn15Vmeygnj2Xv9LiieoyktJvHJ5LkJKOSrwDQ6eLx1U1RnKSTcSQqFpxDUMwaY9b8sxFHQXdtQxNYPuqwmKqSoyF1SLey5AckXG62lT61pQ97vviomh4fAoBN4YVRSxecwe9fEFyErRuQ8b8jm_yD2RN_M8NymlE8gIGA1ka3qqU7GoQAO3mogUgX5iD1A9LuPKS-6loHcqJO9m3yRfotGoxaKyD2zKzjenaoPJkrEMuUmiaGoZVcFgNnQRPza6ZfWQ-5398x_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کیه این تک دلقکو همیشه میزنه
😂
؟
به افتخارش نفری یدونه بزنید ببینه دلقک کیه
🤡</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/whitedns/797" target="_blank">📅 16:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-796">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaHxpeAMMA80jylKwIHMS58t_podMfRjWoZm8DKOPwSE_iFW9aaJRC5t3Au7s2xqtCkrS0JJTiaOS1vvX6c6tNH1mptKxbjK7JP0Ueg3hzd6A0bzle3_jWiN_BhU73mASo0MNKC8F7b9jCxUkQG7DZEEiMRgbqN9W080wrW9K6-F35q2zl6ZnITF5xf9Y681ToLx0_epasekAvwsk3s88IicCZJA8J1DsTVJFwqo1mjUHRGDunHu93W0EQYrSe4mDIm7womX9uKg4sr0BV4rBoE97pJ0dwLyCiy3JAwuF2i_g3m_-W3yAzJio6NeSnhiIjVNkuJT-85CmwJBqJQES3nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaHxpeAMMA80jylKwIHMS58t_podMfRjWoZm8DKOPwSE_iFW9aaJRC5t3Au7s2xqtCkrS0JJTiaOS1vvX6c6tNH1mptKxbjK7JP0Ueg3hzd6A0bzle3_jWiN_BhU73mASo0MNKC8F7b9jCxUkQG7DZEEiMRgbqN9W080wrW9K6-F35q2zl6ZnITF5xf9Y681ToLx0_epasekAvwsk3s88IicCZJA8J1DsTVJFwqo1mjUHRGDunHu93W0EQYrSe4mDIm7womX9uKg4sr0BV4rBoE97pJ0dwLyCiy3JAwuF2i_g3m_-W3yAzJio6NeSnhiIjVNkuJT-85CmwJBqJQES3nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/whitedns/796" target="_blank">📅 11:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpvAtainPxJsRUVDwe4x3mmeDaHBGWxtuZI8ToGLfreZwAPMppCouY6h12r__2srTpYzPRCwCROq5wyuAWZvSA43RwHhmWDfPFoYbyOTiTtT3woERvvgD15Ph5A8YX2ZjkCfEAV7j4HBum-g-4JMgDSM2JhRARmN73gC9DBg47goM63Xba1KXFNm5KiM_y9dcHrggDXWyDJ0GeQ8Es03tVRY3IZrPSDFec4-mQHpN1pEPTAyc2OFoBivIMrZannfVbsulv7rkXmMSXCZcKj3lP5GcRrj4xVSHWkaVZ63Oj9a_BdZbbkW9pm6rqtPDJHeMzp-fHiI_KBErXEvKRzMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حال حاضر مشغول تست نسخه جدید اپلیکیشن دسکتاپ WhiteDNS هستیم.
در این نسخه، علاوه بر اضافه شدن حالت دارک مود، تغییرات مهمی در عملکرد داخلی برنامه اعمال شده است.
یکی از تغییرات اصلی این نسخه، تغییر کلاینت داخلی اپ از StormDNS به MasterDNS است.
این تغییر به این معنی نیست که سرورهای StormDNS دیگر قابل استفاده نیستند یا وصل نمی‌شوند. سرورهای StormDNS همچنان قابل استفاده هستند.
اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/whitedns/795" target="_blank">📅 09:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-793">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">White DNS
pinned «
دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و... ترجیحا نخرید. نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه. جای مطمئنی برای دامنه دیدم معرفی میکنم
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/793" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-792">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و...
ترجیحا نخرید.
نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه.
جای مطمئنی برای دامنه دیدم معرفی میکنم</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/whitedns/792" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-791">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز  ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.   تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.   من پیشنهاد میکنم برای راحتی کار شما، بعد…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/whitedns/791" target="_blank">📅 16:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-789">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">💥
موقت
🚫
دوستان :
اگر سروری دارید از جایی  میگیرید که پورت ۲۲ نمیده اصلا خرید نکنید
ظاهراً یک عده دوباره دارند سر مردم کلاه میگذارند
داستان داریم به خدا
لطفا اگر توی گروه های ما کسی داره کلاهبرداری میکنه با ذکر ID گزارش کنید
@WhisperInHeaven
🚫</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/whitedns/789" target="_blank">📅 12:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز
ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.
تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.
من پیشنهاد میکنم برای راحتی کار شما، بعد از خرید دامنه و اتصال DNS از ربات
@WhiteDNS_installer_bot
استفاده کنید.
اگر از این‌ ربات استفاده کنید، فقط با پروکسی کردن تلگرام‌ میتونید سرور خودتون رو مدیریت کنید و در شرایط بحرانی فقط از طریق تلگرام همه چیز رو مدیریت بکنید.
ممنون
@WhiteDNS</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/whitedns/787" target="_blank">📅 05:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو:
https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو:
https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- خرید دامنه و سرور ارزان با کریپتو(+آموزش)
2- تانل کردن ترمینال با Proxifier و ssh زدن با خود ترمینال
3- تنظیم دامنه در کلودفلر و راه‌اندازی ساده‌ی سرور MasterDNS
4- استفاده از سرور MasterDNS در کلاینت های ویندوز و اندروید WhiteDNS
5- توضیح استفاده از Parallel Testing در WhiteDNS
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به خریداری یک عدد سرور لینوکسی و دامنه داره(مجموعا 5 دلار نزدیک به 800 هزار تومان) کافی برای اتصال نزدیک به 5 نفر
کانال مستر دی ان اس:
1-
https://t.me/masterdnsvpn
گروهشون:
2-
https://t.me/MasterDnsVPNGroup
کانال وایت دی ان اس:
1-
https://t.me/whitedns
گروهشون:
2-
https://t.me/whitedns_group
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/whitedns/786" target="_blank">📅 05:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URKzr5dEkvie0AG5tEJy36Zlz_P2rKyaaAwXCajdMqWECQv7q-ucIfWciMNWc5YfacwtljgI0Pac58qUNwxWRtQ5yaF9Cfbe-ZgtENZ9-O4gtN9eiehURwVgZKkKhLCWHUCiz1IKqPIChgUtb99eBcCiPDvlXPHFKIHrQw1ihZQDjernoaYtCEvlUm9wxBXhBCVn7xUPiYn5DZnrrCn91sb5UrD-N1zfpV45JoDL9KN0Aam64suNuQ85UKKrJxwnnFOlIjWI1T1NcxvxFKE01l2O3enfEfZfJcQhVKs1i4_vIW07fjW7RDzpW2fXet_nzhzi6F4Brz7Dfty0g7Fzsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot
این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی و از طریق تلگرام مدیریت کنید.
✅
نصب خودکار MasterDNS روی VPS
✅
مدیریت سرور از داخل تلگرام
✅
دریافت اطلاعات اتصال و Encryption Key
✅
بررسی وضعیت سرور
✅
ری‌استارت و مدیریت سرویس
✅
مناسب برای استفاده شخصی، دوستان و خانواده
🔐
نکات امنیتی:
اطلاعات کاربر، اطلاعات ورود به سرور، رمز عبور، کلیدها و مشخصات VPS به هیچ عنوان ذخیره یا لاگ نمی‌شود.
اطلاعات فقط در همان لحظه برای اتصال به سرور و اجرای دستور مورد نیاز استفاده می‌شود و بعد از پایان نصب یا اجرای هر دستور، توسط ربات نگهداری نمی‌شود.
بعد از انجام عملیات، اطلاعات ورود و مشخصات سرور توسط هیچ‌کس قابل مشاهده یا دسترسی نیست.
به همین دلیل، کاربران همچنان مالک کامل سرور، دامنه و تنظیمات خودشان هستند.
این ربات فروشنده سرور یا دامنه نیست.
کاربران باید:
* دامنه خودشان را تهیه کنند
* سرور خودشان را تهیه کنند
* دی‌ان‌اس های لازم را روی دامنه تنظیم کنند
هدف ما این است که راه‌اندازی و مدیریت سرور شخصی برای کاربران ساده‌تر شود؛
نه این‌که همه وابسته به چند سرور عمومی و متمرکز بمانند. ما باور داریم کاربران سرعت و پایداری بیشتری با سرورهای شخصی و غیرمتمرکز خواهند داشت.
⚠️
این ربات در اولین نسخه عمومی منتشر می‌شود و ممکن است هنوز باگ یا مشکل داشته باشد.
لطفاً مشکلات و بازخوردها را برای ما ارسال کنید تا سریع‌تر بهترش کنیم.
ویدیو آموزشی خرید سرور و دامنه و تنظیم دی‌ان‌اس به زودی داخل چنل قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/whitedns/785" target="_blank">📅 21:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW4-mLKQx6yPjldQxBYUTRtKnYvv_yeAfeFFGODp6QLprwArMIqDW18e1l3yhPq0cSGVi6qo2ClMujAHRUaHtS2ATU3HmirCqf00BjTM6qzwvRX6ebyfYMdOR4a_dAuX3vmhva1vqgb1ewqXNt0PLhvcPfJMl9zo9pQ63cbvGbrlTgb3IsmrZYFE1nqtnqhI_g0lSkwprluBLqTiJ7HRK4p1Df3knWqE4DX3ydrUBFQgeLDReTuevOtuLbb1QJ9UhqqHtltRO65hXkFbGz0CdfJZmYzzQWZWhlBMOTRv9XPpGgv_Erfo0LzP2Kx6zd1C5CWunCBmGdewqfSna70ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
پروژه جدید WhiteDNS در حال آماده‌سازی است
♨️
تیم WhiteDNS بر روی سیستمی کار میکند که کاربران بتوانند فقط با داشتن یک VPS و یک دامنه، سرور شخصی MasterDNS خودشان را مستقیماً داخل تلگرام راه‌اندازی کنند.
هدف این پروژه این نیست که ما به کاربران سرور یا دامنه بفروشیم یا مدیریت کنیم.
هدف تنها ساده‌تر کردن فرآیندی است که امروز برای خیلی‌ها پیچیده، زمان‌بر و فنی محسوب می‌شود.
در این سیستم، کاربر فقط:
• VPS خودش را تهیه می‌کند
• دامنه خودش را تهیه می‌کند
• DNS Record ها را تنظیم می‌کند
و باقی مراحل توسط ربات و Mini App تلگرام به‌صورت خودکار انجام می‌شود.
سیستم به‌صورت اتوماتیک:
• وضعیت DNS Record ها را بررسی می‌کند
• اتصال دامنه به سرور را تست می‌کند
• MasterDNS را نصب و راه‌اندازی می‌کند
• اطلاعات نهایی مثل Domain و Encryption Key را به کاربر تحویل می‌دهد
در عمل، کاربران می‌توانند بدون درگیر شدن با دستورات پیچیده لینوکس و تنظیمات طولانی، سرور شخصی خودشان را راه‌اندازی و مدیریت کنند.
این پروژه متن‌باز خواهد بود تا همه بتوانند کد آن را بررسی کنند.
در حال حاضر پروژه در مراحل نهایی توسعه قرار دارد و طی روزهای آینده نسخه اولیه آن منتشر خواهد شد.
@WhiteDNS</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/whitedns/784" target="_blank">📅 09:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/783" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHEFLb1xrN_tSn6cBofRYcqSB8zCD5n27q3LnCnRonvxmem1ONygl1wg3j_e7LOFLi3uXjNAaF6DT-eBdU0DLXaqmeIbpCV8YQ8fQasxrEPdOqV957hixst8uxIPEhEcoVhG2HL1TwkLGXo45Q_1DjLqWv6mVYf6qLNDE4ZBGkXJrJJ9TzVGzkcBgcRrz7-_6b8CHsbzW9vnR9vlE9KTwYK_c5hi3grDlm7VLTgTo_T82M9aBblkXrqUznDpBjPuEOFRX1-QI8Ezv8lg5jYepzoMbWhqCM7Wtjd38NdX7oPTIrl5cmYTJzOFZueDP01QHGqCcT0jra-yNiWoMtQ1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان
👋
چون سوالات خیلی تکراری و بی‌هدف شدن
🤔
ما یک گروه با تاپیک‌های مختلف درست کردیم
📂
لطفاً اونجا عضو بشید و توی تاپیک خودش سوال کنید
✅
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/whitedns/782" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-781">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv30OvpRa_zKmVDbGKHU-ZM1sG-ovYddeDGzXk_pGVE-dNx0rNKqaUiS76733iiAU2pRDteN2IFCx-cP_RbFFd4LYqmvK9zNzRS-B9Bz-yeU-hhnmPZoIemUKf7JzHHtjtZdWdtpXeUXUa5gR5Mik9Rz-7WZHtFYXTVlfLNQ3k3Px-jZCEAVDI0be3rArI0RVGap0puHi0DxsXKwJSlkSDBVgNIdK21worHx_ioti2Y9u7C1XBfGavc06u6Z8PJmm9zgTOKSO-0zABs65rGsBMb5XKNch7iuc_JWSfe0X-B-c3N2YxqXaxYVCFTL-GfPYNOaCwy1YsV-wQXo9ZsdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش پروکسی و تانل کردن ویندوز
در این ویدیو نحوه پروکسی کردن فایرفاکس با نرم افزار WhiteDNS
پروکسی کردن کردن کروم ادج
و همینطور تانل کردن کل ویندوز با متود جدید آموزش داده شده است !
لینک دانلود ویدیو ( داخلی ) :
https://dl.toolschi.com/view.php?f=9f27edab8159500e.mp4
لینک دانلود نرم افزار  TunnelX ( داخلی ) :
https://uplod.ir/75m7wx9r6c17/TunnelX-v2.1.0__Whitedns.zip.htm
لینک گیت هاب TunnelX
:
https://github.com/MaxiFan/TunnelX/releases
امکان هست که آنتی ویروس  TunnelX رو حذف کند. در صورت نیاز اون رو به لیست نرم‌افزار های سفید آنتی ویروس خود اضافه کنید.
منبع تصویر کانال اینترنت آزاد
1️⃣
@WhiteDNS</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/whitedns/781" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-780">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">+۲۵۰ ریزالور جدید به ربات تلگرام WhiteDNS اضافه شده
برای دریافت وارد بات شوید
@dns_resolvers_bot
و بعد دستور زیر را اجرا کنید
/dns_master</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/whitedns/780" target="_blank">📅 16:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-779">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/779" target="_blank">📅 16:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-778">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">لینک داخلی آموزش ساخت سرور شخصی StormDNS & MasterDNS
https://guardts.ir/f/d68436b0fc33</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/whitedns/778" target="_blank">📅 10:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcoKb8gvPX36esTj0Lz151Q5B0fxiVy7oFgDBTw5uYQ-hDlgMsWkSwG4dcunzOrBDTKi_5tvZ2hlTf1S2sqbgm-dge5LfRPbu9JKveTdJzesyhzH-oAdCc1gUC9Otbuxwz-wQvHC9uR_TDIrTJSiMqoUyA1QGhxtiqRIjdLPnYJeF11JSTRFP24V8_YDIzBv2cQEGivbpZwfGuFFnfCBDCoB-wNvjBJ4UkCmsgk9TWbJs3DrEa-Mb1CXHiQCrkvPTKdOcjumdn3DT_0a2FnaGMzuL5imQwkGUerpRO3hFmm3-YNEX8hERI_Q1hAqsekELjG_fY8HwHChq0b_NdaIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-5vitYA1dSLqNvd5OHrpqskUg1DQDMQ_R6G7nfT6dUNSWo_kzV2q3CqWzsZ6hL4_ArwhBr1OhH2ij9j-FGnMkHE1HRfWcc71vCIYd8iYOied3ouBVXsF_RJcq9QYJrzatPxbS1E554MGKvgiBebBS3vtVFeBmYs_nnOBiXADMcn4uqGQPdejdzeIbu-UeR7ARZAoXwhpg72XT-HWxquBR72PSPCb81ygleqAhPO4ti4w6ME6RZoD9it7MGE94et6Ml0Coi9f3VUfdp5TH67LSkSvbFzInpA9ub-lGhlSnPSbAWCNd08VLorOo0gkZmlLQemkscqO7y-LpFkztJ4zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEeLG_iaaZmA0hrjnhSGIN7hhF2MqsMTrkAlLR_pmNGBaWXVV5vbSNUkaOEG_kDMc4JeLmDOnpMZ-DarvgFLmkCFflgz4N7GgwNGrjVg_txeuSUhYFGULLrWDn_mE-ImNZP7i8WvASwXQDIsLpOIFuIivZXMSHqA6qROa8sp_xyTPLxsU8_ydtA-Q8oX9l7yjD3JGGqF25p3klrm8sf18aMMu3pxmKFd2DBDp9V4AdufmxVHH_j2yRr3Vf0S0TmVgVUQ1CZqJV_gjtQO-z4bvYYTItXNYjOsWQitZU9cu-oai0rjF3R-qlpAfmskORz1mqZ5Bdfkl3NvlsL1bSxi9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">- برای پیدا کردن سرور برای وصل شدن به تاپیک سرور برید
- برای راه اندازی سرور شخصی به تاپیک سرور شخصی برید
- برای آموزش و یادگیری اولین شروع با این ابزار به تاپیک اولین شروع برید
🫡
لینک گروه اصلی
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/whitedns/774" target="_blank">📅 07:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">جمع‌بندی نهایی
تیم WhiteDNS تمام نشده، رها نشده و قرار نیست فقط به چند سرور عمومی محدود بماند.
برعکس، هدف ما این است که استفاده از WhiteDNS از حالت وابسته به سرورهای عمومی خارج شود.
کاربران می‌توانند با آموزش، سرور شخصی یا گروهی خودشان را راه‌اندازی کنند و اتصال پایدارتر و اختصاصی‌تری داشته باشند.
این روش برای اتصال حیاتی، شرایط سخت و دسترسی ضروری طراحی شده است؛ نه برای مصرف سنگین، دانلود زیاد یا انتظار سرعت VPNهای تجاری.
تیم WhiteDNS همچنان کنار شماست.
فقط قرار است از این به بعد، به‌جای اینکه فقط ماهی بدهیم، بیشتر ماهی‌گیری یاد بدهیم.</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/whitedns/773" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هدف اصلی WhiteDNS
هدف WhiteDNS کمک به دسترسی آزادتر به اینترنت در شرایط سخت و محدود است.
WhiteDNS یک پروژه غیرانتفاعی است و تمرکز ما روی ساخت ابزار، آموزش و کمک به کاربران برای داشتن راه‌های پایدارتر اتصال است.
ما همچنان مسیر توسعه اپلیکیشن، بهبود کیفیت، آموزش و نگهداری زیرساخت‌های فعلی را ادامه می‌دهیم.
اما می‌خواهیم کاربران کمتر به سرورهای عمومی وابسته باشند و بیشتر بتوانند اتصال اختصاصی خودشان را بسازند.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/whitedns/772" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آیا دانش فنی زیادی لازم است؟
برای راه‌اندازی اولیه کمی دقت لازم است، اما آموزش‌ها طوری آماده می‌شوند که کاربران معمولی هم بتوانند مرحله‌به‌مرحله انجام دهند.
اگر هیچ تجربه‌ای با سرور نداشته باشید، شروع کار ممکن است کمی سخت به نظر برسد.
اما بعد از یک بار راه‌اندازی، استفاده از آن بسیار ساده‌تر خواهد بود.
هدف ما این است که این مسیر را تا حد ممکن ساده‌تر، قابل فهم‌تر و قابل انجام‌تر کنیم.</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/whitedns/771" target="_blank">📅 07:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آموزش‌ها کجاست؟
ویدیوها و آموزش‌های مربوط به نسخه اندروید، نسخه دسکتاپ و راه‌اندازی سرور شخصی داخل کانال قرار داده شده‌اند.
لطفاً قبل از پرسیدن سوال، داخل کانال سرچ کنید.
برای پیدا کردن آموزش‌ها می‌توانید این عبارت‌ها را جستجو کنید:
آموزش
سرور شخصی
دسکتاپ
اندروید
StormDNS
MasterDNS
Resolver
آموزش‌ها مرحله‌به‌مرحله منتشر شده‌اند و با کمی جستجو قابل پیدا کردن هستند.
همچنین داخل گروه اصلی تاپیک اولین شروع همه چیز رو توضیح داده
https://t.me/whitedns_group/32380/38590</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/whitedns/770" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگر سرور کند بود، مشکل از اپلیکیشن است؟
نه لزوماً.
کندی یا قطعی می‌تواند دلایل مختلفی داشته باشد:
- شلوغ شدن سرور عمومی
- ضعیف بودن Resolverها
- اختلال یا محدودیت سمت اینترنت ایران
- کیفیت پایین مسیر شبکه
- تنظیمات نامناسب
- استفاده تعداد زیادی کاربر از یک سرور مشترک
کیفیت نهایی اتصال به سرور، Resolverها و شرایط شبکه هم بستگی دارد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/whitedns/769" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چه انتظاری نباید داشته باشید؟
از WhiteDNS نباید انتظار سرعت بالا برای مصرف سنگین داشته باشید.
ممکن است شبکه‌های اجتماعی باز شوند، اما همیشه سرعت عالی نخواهد بود.
برای مواردی مثل این‌ها مناسب نیست:
- دانلود زیاد
- ویدیو با کیفیت بالا
- وب‌گردی سنگین
- استفاده هم‌زمان چندین اپلیکیشن پرمصرف
- انتظار سرعت شبیه VPNهای تجاری
این روش بیشتر برای دسترسی ضروری طراحی شده، نه مصرف سنگین روزمره.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/whitedns/768" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این روش برای چه کاری مناسب است؟
WhiteDNS و روش‌های مبتنی بر MasterDNS/StormDNS بیشتر برای شرایط سخت، محدود، ناپایدار و اضطراری ساخته شده‌اند.
این روش برای مواردی مثل این‌ها مناسب‌تر است:
- اتصال حیاتی
- پیام‌رسان‌ها
- دسترسی ضروری
- شرایط محدودیت شدید اینترنت
- استفاده سبک و کنترل‌شده
این روش جایگزین کامل VPNهای پرسرعت تجاری برای مصرف سنگین نیست.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/whitedns/767" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">استفاده گروهی با دوستان و آشناها
یکی از بهترین روش‌ها این است که چند نفر با هم یک سرور تهیه کنند.
اگر دوست، خانواده یا آشنایی خارج از ایران دارید، می‌تواند برای تهیه یا راه‌اندازی سرور کمک کند.
بعد از راه‌اندازی، اطلاعات اتصال داخل WhiteDNS وارد می‌شود و همان سرور به‌صورت اختصاصی‌تر برای شما یا گروه کوچک‌تان قابل استفاده خواهد بود.
این روش معمولاً از استفاده از سرورهای عمومی شلوغ پایدارتر است.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/whitedns/766" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هزینه تقریبی سرور شخصی
هزینه راه‌اندازی سرور شخصی معمولاً خیلی بالا نیست.
به‌صورت تقریبی:
شروع کار: حدود 7 دلار
هزینه ماهانه بعدی: حدود 6 دلار
البته ممکن است سرورهای ارزان‌تر هم پیدا کنید.
یک سرور حدوداً 6 دلاری معمولاً می‌تواند برای حدود 5 تا 10 کاربر سبک و معمولی کافی باشد.
اگر چند نفر با هم هزینه را تقسیم کنند، هزینه ماهانه برای هر نفر بسیار کمتر از اکثر سرویس‌های VPN خواهد شد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/whitedns/765" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مزیت سرور شخصی
راه‌اندازی سرور شخصی یا گروهی چند مزیت مهم دارد:
- فشار کاربران عمومی روی سرور شما نیست
- پایداری معمولاً بهتر است
- در بعضی شرایط سرعت بهتری می‌گیرید
- احتمال پیدا کردن Resolverهای مناسب بیشتر می‌شود
- کنترل کامل‌تری روی تنظیمات دارید
- هزینه آن معمولاً از خرید VPN کمتر است
- می‌توانید با دوستان یا خانواده به‌صورت گروهی استفاده کنید
ابزار WhiteDNS برای همین ساخته شده که فقط محدود به چند سرور عمومی نباشد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/whitedns/764" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چرا سرور عمومی جدید منتشر نمی‌کنیم؟
وقتی یک سرور عمومی در کانالی با ده‌ها هزار کاربر منتشر می‌شود، خیلی سریع زیر فشار زیاد قرار می‌گیرد.
در نتیجه:
- سرعت کم می‌شود
- اتصال ناپایدار می‌شود
- سرور گاهی از دسترس خارج می‌شود
- کاربران فکر می‌کنند مشکل از اپلیکیشن است
در حالی که مشکل اصلی معمولاً فشار زیاد روی سرور، محدودیت‌های شبکه، یا وضعیت Resolverهاست.
طبیعتاً یک سرور عمومی نمی‌تواند هم‌زمان برای هزاران نفر مثل VPN اختصاصی کار کند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/whitedns/763" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وضعیت سرورهای فعلی
سرورهایی که تا امروز توسط تیم WhiteDNS ارائه شده‌اند، همچنان نگهداری می‌شوند و تا جایی که امکان داشته باشد فعال خواهند ماند.
اما از این به بعد برنامه‌ای برای انتشار مداوم سرورهای عمومی جدید از طرف تیم نداریم.
اگر سروری متعلق به خود تیم WhiteDNS باشد، فقط داخل تاپیک «سرورها» اطلاع‌رسانی خواهد شد.
تمرکز اصلی ما از این به بعد آموزش، مستندات و کمک به کاربران برای راه‌اندازی سرور شخصی یا گروهی است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/whitedns/762" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-761">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تمرکز جدید کانال
از این به بعد تمرکز اصلی ما بیشتر روی این موارد خواهد بود:
- آموزش استفاده بهتر از WhiteDNS
- آموزش راه‌اندازی سرور شخصی MasterDNS و StormDNS
- آموزش نسخه اندروید و دسکتاپ
- آموزش پیدا کردن و تست Resolverها
- معرفی تنظیمات بهتر
- رفع اشکال و راهنمایی کاربران
- بهبود اپلیکیشن و اطلاع‌رسانی نسخه‌های جدید
هدف ما این است که کاربران فقط مصرف‌کننده چند سرور عمومی نباشند.
نرم‌افزار های ما طوری طراحی شده که بتوانید از سرورهای خودتان، سرورهای دوستان‌تان، یا هر سرور سازگار با MasterDNS و StormDNS استفاده کنید و اتصال پایدارتر و اختصاصی‌تر بسازید.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/whitedns/761" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-760">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سلام به همه همراهان WhiteDNS
از امروز رویکرد ما در WhiteDNS کمی تغییر می‌کند.
WhiteDNS از ابتدا برای استفاده با سرورهای MasterDNS ساخته شده و همچنین از فورک StormDNS هم پشتیبانی می‌کند.
یعنی استفاده از WhiteDNS فقط محدود به سرورهایی نیست که از طرف کانال معرفی می‌شوند.
هر سرور MasterDNS و همچنین سرورهای سازگار با StormDNS می‌توانند داخل اپلیکیشن WhiteDNS استفاده شوند.
تا امروز، در کنار توسعه اپلیکیشن، تعدادی سرور آماده هم در اختیار کاربران قرار دادیم تا شروع استفاده برای همه راحت‌تر باشد.
👇
اما در ادامه یک سوءبرداشت ایجاد شد:
بعضی از کاربران فکر می‌کنند اگر سرورهای معرفی‌شده شلوغ شوند، کند شوند یا موقتاً در دسترس نباشند، یعنی خود اپلیکیشن WhiteDNS مشکل دارد یا قابل استفاده نیست.
در حالی که WhiteDNS فقط یک اپلیکیشن وابسته به چند سرور عمومی نیست.
قدرت اصلی WhiteDNS این است که هر کاربر یا هر گروه کوچک می‌تواند سرور MasterDNS یا StormDNS خودش را راه‌اندازی کند و از همین اپلیکیشن برای اتصال استفاده کند.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/whitedns/760" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-759">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">White DNS
pinned «
سرور جدید WhiteDNS   Domain: v.wdn.best Encryption Key: bad99364093861634030e96f11fe3132 Encryption: XOR @WhiteDNS
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/759" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-758">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.wdn.best
Encryption Key:
bad99364093861634030e96f11fe3132
Encryption: XOR
@WhiteDNS</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/whitedns/758" target="_blank">📅 06:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-754">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/754" target="_blank">📅 16:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-753">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHEmXfgVKyJy4eDM0bTx23AXYIxxAI1GZUMPJscCDW6_zWy-nC9DgIqRB_sVG7HFqj9zsViEA53yFwSVdCsgBBqS7ocvkPpwPU5Apr42MpTCwY2hgaTvokRwb-5fIbTBHmetD8L0C7LdTuHpoT7uiOE69vLm-LVDLozi6uZDHeVIJ6mW37gfMI_Zm9OrLbJZYJfuMooXErFkNUO3wKxR4pVVuWAqL_q9cNRNkJr4jDtrKtDsT9YADxEkGXIcmjsHnzTKLRZ0Pxv9wOhVIys7fpBLiQ4PWk1I-phPFPhMdHW-A75rBXj5O8tWdUMEPf6CafwyHStjHD22CfOszMTP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/whitedns/753" target="_blank">📅 15:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-752">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompythash</strong></div>
<div class="tg-text">سرور ها آپدیت شدن
دقت کنید هم رمز و هم دامنه تغییر کردن
سرور StormDNS اختصاصی چنل Pythash/پای هش
StormDNS Server Configs
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
@pythash
Domain:
v1.pythash.tr
Key:
Telegram-Channel------->@pythash
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
@pythash
Domain:
v2.pythash.tr
Key:
Telegram-Channel------->@pythash
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
نحوه اتصال:
windows , android:
https://t.me/pythash/74
linux:
https://t.me/pythash/81
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🌀
@pythash
🌀
@pythash</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/whitedns/752" target="_blank">📅 15:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-751">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/whitedns/751" target="_blank">📅 14:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/749" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YDIZcGe8rj9GUn2GDMQmNAMKzjTyvEc3MijmRlQyALu4o6ZWpq5sI6x_cJrnVov5l04O8_Ocjd2gur3kLT3pXZgtYfwj-Xd_Bhp5tPs-rqxwkv9GG0mGoUA9PpY4wYUpRz0pkUHT0ZgMLBv3yIEmT_5bX5M9lSNvY5KnvNM5D3MKjhL9TSzyPq74nPCSpsE3KpvtWqY-41_8UIa68yfLanSIK92HgvhZftfX8rVnZ7HowZ3QrRqx2PuU9g8O_JnMZ0XHhSlhCJq-xAAd4jS3XnYc0U9-uVVJcwkhtqZpbLU4H1k51d_NwrfHGcbWccu8M1dYx4BmHhAp0--q1TGiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/whitedns/748" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-747">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-poll">
<h4>📊 🌷نظرتون در مورد نسخه جدید Whitedns windows چی هست ؟👀⚠️</h4>
<ul>
<li>✓ عالی</li>
<li>✓ خوب</li>
<li>✓ متوسط</li>
<li>✓ بد</li>
</ul>
</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/whitedns/747" target="_blank">📅 13:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-745">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWXeITcFTr0qmfIKxVqOQItUQURPx2J4zeieIQk3PDVB3zkKrPFffWTfjzRWBqS7FmC5Z_5WIaV88w6qWL1BdRaSN6j9px0WmRLq4c_Kn1K4Kh8pkTIF_7CGqsW7na8_x23hi4uN8USj9TrxM1rUCmumAzRGU843jg4xaUxMdufHN42ebd46SBj8x7SWH2L7sR1-mszXDg4lDJFg5zPf-e0pD8oZg7PWVZ_6cri1BGAKV3qRClimnSfA7uLEyqBjBHmhXIobUuKCA-tJ_smsN7ze2oRJeqxbiLFa14iq4pKyGz547ecQVk13rSRrU6NC6UW0wc57m4INkVZpvQIRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mppLSQluTvHTFBuFnqx-LvHreiEtvoQv6MbCBjaCgqgmlU6kULzsuMpXWYRoO_PQdVUwRmElhUqgXN4YKBVtOS6_QqdlhPNia6YIC8u4MFUk7ANZiY7K8Po0Og9sw39J5KWjVKIgxLVfRhEPyKZA05b4iq4w-6CO5ROEYDdXT0v0V9m42H7yJrz9R0EA7aQLMoxFAQK8ariATjRDiorhDafnErZUR2E-iGSb1P5B9wQ0yyLQQ2ZM-B6gu5e55n5stc_Jpy5YmE5DQdt7wQoHPgsgOa5lMzB9mGWJo9ZEq3ZumArlAfs76hv7YsROcDEJ-p3GtFoqbg6PH6JJHjVsrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♨️
نسخه 1.0.0 Beta 3 ویندوز WhiteDNS منتشر شد
♨️
سلام به همراهان عزیز WhiteDNS   نسخه جدید ویندوز منتشر شده و در این آپدیت تمرکز اصلی روی بهتر شدن تجربه کاربری، تست سریع‌تر تنظیمات، مدیریت راحت‌تر سرورها و ریزالورها و رفع مشکلات گزارش‌شده بوده است.
🔅
قابلیت‌های…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/whitedns/745" target="_blank">📅 11:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-744">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👇
👇
👇
👇
👇
👇
این گروه توسط جمعی از فعالین این حوزه مدیریت می‌شود و هدف، دسترسی مردم به اینترنت آزاد است.
چت کردن، صحبتی به غیر از دسترسی به اینترنت، تبلیغ، سؤال راجب فروشنده‌های VPN = مستقیم بن
گروه اصلی:‌
https://t.me/Ir_Blackout
گروه کانفیگ:
https://t.me/Ir_Blackout_Config</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/744" target="_blank">📅 10:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-743">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">لینک های داخلی برای دانلود اپلیکیشن های دستکتاپ
⬇️
Windows
|
Linux
|
Mac
1
.0.0 Beta3
باتشکر از چنل
@masir_sefid</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/whitedns/743" target="_blank">📅 09:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-741">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-arm64.deb</div>
  <div class="tg-doc-extra">15.5 MB</div>
</div>
<a href="https://t.me/whitedns/741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/whitedns/741" target="_blank">📅 09:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-735">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.9 MB</div>
</div>
<a href="https://t.me/whitedns/735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/whitedns/735" target="_blank">📅 09:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-734">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE5ukUTXKKCk4QMtEU6MqjYAFt1H_tSOuw1E7L4OOMdAnFwu8maRxwJpamyyuJ0UrNm4NwkChkW34vHw-1j4M3VonwB35zw8TS1eA-RIf5o2s1x-O4WNsY8g5S1BUaC97K-yETubX0IP0Vg3c80qoL3Zzl72vv2xfi1U6xlwGQJgp_AJhHfTQybH_IPSzfLU4pD-RGcMgiLQ5u9H0h8FNwwqgM7fbyrL_CYOjIqjyRxi_Ze7cNXCWlhH1EjZe9lzXKZS_vD8gsTcadzNR9Fd3lchpGvsHsflSqsu0oeSYHFr4RMp0DtZEZXeU-alQ6xA2dq8_TNYKOdIJeE0PENbpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
نسخه
1.0.0 Beta 3
ویندوز WhiteDNS منتشر شد
♨️
سلام به همراهان عزیز WhiteDNS
نسخه جدید ویندوز منتشر شده و در این آپدیت تمرکز اصلی روی بهتر شدن تجربه کاربری، تست سریع‌تر تنظیمات، مدیریت راحت‌تر سرورها و ریزالورها و رفع مشکلات گزارش‌شده بوده است.
🔅
قابلیت‌های جدید
✅
اضافه شدن قابلیت
Parallel Test
برای پیدا کردن بهترین تنظیمات اتصال
✅
اضافه شدن دکمه‌های جدید برای حذف لاگ، کپی لاگ، خروجی گرفتن از سرورها، ایمپورت DNS، خروجی گرفتن و ایمپورت تنظیمات
✅
امکان انتخاب نتایج اسکنر و ساخت پروفایل جدید بعد از اسکن
✅
امکان کپی همه نتایج اسکن، انتخاب دستی نتایج و کپی موارد انتخاب‌شده
✅
اضافه شدن قابلیت مرتب‌سازی تنظیمات، سرورها و ریزالورها
✅
نمایش IP ویندوز برای اشتراک‌گذاری اینترنت با موبایل و سایر دستگاه‌ها
✅
اضافه شدن قابلیت ریست تنظیمات برنامه
🔅
بروزرسانی‌ها و بهبودها
✅
بازطراحی و رفع مشکلات تب داشبورد
✅
اضافه شدن اسکرول در بخش‌های سرورها، ریزالورها و تنظیمات
✅
بهبودهای مختلف بر اساس گزارش‌های کاربران
لطفاً نسخه جدید را تست کنید و اگر مشکلی دیدید، همراه با لاگ و توضیح دقیق در بخش مربوطه گزارش دهید تا سریع‌تر بررسی شود.
ممنون از همراهی و گزارش‌های ارزشمند شما
🙏
@WhiteDNS</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/whitedns/734" target="_blank">📅 08:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-732">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.8 MB</div>
</div>
<a href="https://t.me/whitedns/732" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
دوستان عزیز Linux, اپ دسکتاپ WhiteDNS Beta2 برای لینوکس هم آماده کردیم و میتونید دانلود کنید.
این نسخه بتا هستش  و ما در روز های آینده دایما با فیکس ها و فیچر های بیشتر آپدیت میدیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/whitedns/732" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-731">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twAS9n2U5DR-8QWvBHLCzISeBwNv3vCjeRwFkqyBKLf1LKBFfYUvQjWgKpHj0YX0LcZijh6xpEee4OxDgDKQ-tIAQTbhs3A1l5kedtyjHyLPQRShKOYmmTUVsjOu01PvPJW8ADNPPd9ypB0ZiMeuBccTb8cpru0W5mOwLn7cubG6fP4trqe1kQ2wF9xA8nvz67yEESVP661gm8SvEkaEjKABCFoEvd_nktoxpmndvKXokoqZKWdwkWu-TJuCMHnZOLh7BDlafIKcSnN1pN5hTGP5-EUAG-bY_phsAcoRjCdcDEVx6jSe1Xck87iidKm_R1ZwHQnWXE9boJM-SyIX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/731" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-730">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لیست ۱۰۰ ریزالور موقفی که در ۲۴ ساعت گذشته به سرور های WhiteDNS وصل شدن
80.75.7.2
31.214.169.244
185.208.183.29
62.60.144.87
93.115.127.9
5.160.128.142
109.230.89.90
185.142.158.162
134.255.206.205
185.53.142.174
94.232.173.28
185.88.178.196
2.188.21.58
46.245.80.82
62.60.144.85
185.255.91.60
185.109.61.27
2.188.21.70
74.63.24.210
185.208.174.167
185.141.105.139
185.51.201.58
217.66.203.211
2.188.21.46
85.185.157.181
5.202.252.30
172.64.32.0
173.245.58.0
93.118.127.118
108.162.192.0
78.39.234.140
178.252.128.66
158.58.184.147
37.191.95.70
164.138.17.122
185.50.37.52
46.32.31.30
185.53.141.230
92.246.87.191
93.118.109.213
5.160.140.16
2.188.21.146
2.188.21.138
2.188.21.62
5.160.227.78
5.160.2.55
5.160.137.130
109.72.197.1
74.80.77.246
80.210.40.53
74.80.77.247
80.210.40.50
207.211.215.145
185.191.79.210
74.80.77.244
81.16.121.151
78.157.41.60
217.218.59.18
45.135.241.33
194.61.120.143
74.80.77.245
217.219.76.102
85.185.1.10
185.129.170.75
46.209.44.74
43.226.5.169
87.107.9.233
79.175.172.101
2.188.21.78
172.253.228.147
185.213.11.85
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/whitedns/730" target="_blank">📅 16:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-729">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سلام عزیزان، امیدوارم در این اوضاعِ به شدت خراب و زندگی در کشوری که توسط یک رژیم فاسد اداره میشه همچنان قویی باشید و حال دلتون عالی باشه. همونطور که میدونید ما
به شدت
با پروسه‌ی فروش
مخالف
بوده ایم و تمام فعالیت های ما برای
تمام
مردم ایران به صورت
کاملا
رایگان
بوده؛ اما جا داره که از تمام کسانی که چه با کریپتو و چه با استارز زدن به پست ها از ما حمایت میکنند تا فعالیت چنل و سرورها مداوم باشه، تشکر کنم. در این مدت دقت کردم که تمامی پست های چنل حداقل یک استارز خورده و بدونید که تمام این حمایت ها حتی یک استارزی که میزنید برای ما خیلی با ارزشه و از شما قدردانی میکنیم که در این راه دشوار و مبارزه با این حکومت خون‌خوار در کنار ما ایستاده اید!
❤️
- کوچیک شما Patrick.
WhiteDNS-Team
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/729" target="_blank">📅 14:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-728">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">لینک داخلی تمام پلتفرم های برنامه‌ی WhiteDNS Desktop:
Macos-amd64:
https://guardts.ir/f/736498ddfb14
Macos-arm64:
https://guardts.ir/f/4594c5008167
Windows-x64(amd64):
https://guardts.ir/f/2549b69980b3
Windows-arm64:
https://guardts.ir/f/05e3847a8a43
@WhiteDNS</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/whitedns/728" target="_blank">📅 13:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-727">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فیلم آموزش استفاده از نسخه WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/whitedns/727" target="_blank">📅 13:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-726">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فیلم آموزش استفاده از نسخه WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/whitedns/726" target="_blank">📅 11:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-725">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQGId8CWU1dYBgWCS5BbHIbmiu1zVjMmjkIv8DLAPO3KIhAdBhz_LL94qJVZ5c6ZZEcxLTPAuB64eKjxBzxjNBMZJ50Yugg0pxP3U2rKHZfC1ZSkWZzQCM-btgF3dwgtdEL_n32JudkQckhhN-7UIfuFel9E_OjuCW62RcJaM3-XaGv_dGLtuj60Jp5i9RUHoRe6ILRmd5qt_FEk6bLLcH2Nskn8x3KaEGdFlusOYRdGKlUTnuqV5oBzlsscs0rfZbBqfGBpoWsNtimM3vaTvfFVSz0gZWIrcZZHIZ1dKgTwNTRnyIYqM6ZweDKHPAmH-LGsW5oJ24T9FmD7uiSIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی مک، دوستانی که مشکل باز کردن اپ رو دارید، دستور زیر رو اجرا کنید
chmod +x "/Applications/WhiteDNS Desktop.app/Contents/MacOS/WhiteDNS Desktop"
xattr -dr com.apple.quarantine "/Applications/WhiteDNS Desktop.app"
open "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/whitedns/725" target="_blank">📅 11:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-721">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/whitedns/721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه WhiteDNS Desktop V1.0.0-beta2
✅
حل مشکل باز کردن در ورژن های قدیمی مک
✅
حل مشکل وصل نشدن و خطا بعد از ۴۵ ثانیه
✅
حل مشکل وارد کردن کانفیگ به صورت گروهی
✅
حل اضافه شدن دگه ذخیره برای ریزالور های سالم و. فعال به صورت جداگانه
✅
حل مشکل مشکی شدن صفحه در ویندوز
✅
اضافه شدن نسخه های لینوکس</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/whitedns/721" target="_blank">📅 10:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-717">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/whitedns/717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎉
WhiteDNS Desktop منتشر شد</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/whitedns/717" target="_blank">📅 08:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-716">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwL24lIUpHHETQCgsRmsllmLQJMRs87HYqvj0vaGjUhL1hZtgIgGSnjO5f49ejXsBFjzlnY7MdQW3WgqnEV8236LZK2aMDylecojfoEvMjJ3L3DvbcTwnCpQlD7P0khsXJcBIYeP4KteFosgsq6ePaJR0oVh030fw8PwyCKJdUYVXHD8BKwh8AzHbaafzxUuzPX5VhlMtpPUK8DdiCZJANCcae81fVIDrIQ40tE3T0OgRXrHR5Ncgth-UZQ3fJktahBR0LGLsaSuz_GH1uxMnfDRgM78tNjDUv1Wg9Ig7XNI3hfpcBQLHrXgsYkht4wJWG2xRlB6o6o7T-mWaAeFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteDNS Desktop منتشر شد
نسخه دسکتاپ WhiteDNS حالا آماده استفاده است.
این برنامه برای کسانی ساخته شده که می‌خواهند اتصال‌های MasterDNS و StormDNS را روی کامپیوتر، ساده‌تر، سریع‌تر و بدون درگیر شدن با ترمینال و فایل‌های تنظیمات اجرا کنند.
با WhiteDNS Desktop می‌توانید پروفایل اتصال را وارد کنید، Resolverها را مدیریت کنید، اتصال را فقط با یک دکمه روشن یا خاموش کنید و وضعیت همه‌چیز را به‌صورت زنده ببینید.
✨
امکانات اصلی
✅
اتصال و قطع اتصال فقط با یک دکمه
✅
رابط گرافیکی ساده برای Windows و macOS
✅
پراکسی محلی آماده برای مرورگرها و برنامه‌های دیگر
✅
پشتیبانی از SOCKS و HTTP از طریق sing-box
✅
امکان فعال کردن System Proxy
✅
وارد کردن پروفایل‌های آماده با لینک‌های
stormdns://
✅
ساخت و مدیریت چند پروفایل اتصال
✅
ساخت و مدیریت چند لیست Resolver
✅
بررسی خودکار معتبر بودن Resolverها
✅
نمایش Resolverهای فعال، آماده‌باش و ردشده
✅
نمایش سرعت دانلود، سرعت آپلود و مصرف کل داده
✅
نمایش روند اتصال و درصد پیشرفت هنگام راه‌اندازی
✅
امکان توقف و ادامه دادن تست MTU هنگام اتصال
✅
خروجی گرفتن از تنظیمات به‌صورت
client_config.toml
✅
بخش لاگ و جست‌وجوی لاگ‌ها برای عیب‌یابی راحت‌تر
⚙️
تنظیمات پیشرفته برای شبکه‌های ضعیف و ناپایدار
برای کاربرانی که روی اینترنت‌های محدود، ضعیف یا ناپایدار هستند، تنظیمات پیشرفته هم داخل برنامه قرار داده شده است:
✅
انتخاب روش بالانس بین Resolverها
✅
تنظیم Packet Duplication برای پایداری بیشتر
✅
تنظیم فشرده‌سازی آپلود و دانلود
✅
تنظیم MTU، Timeout، Retry و تعداد تست هم‌زمان
✅
کنترل Workerها، Streamها و صف‌ها برای سیستم‌های مختلف
✅
وجود Watchdog برای بررسی زنده بودن اتصال
🔍
ابزار Scanner داخلی
در این نسخه، یک ابزار Scanner هم داخل برنامه اضافه شده است تا تست و بررسی Endpointها راحت‌تر شود:
✅
تست سریع یک Host با چند پورت
✅
اسکن گروهی از فایل‌های TXT، CSV یا JSON
✅
تست پروتکل‌های TCP، TLS، HTTP، WebSocket، UDP، QUIC/H3 و DNS
✅
نمایش Score، Grade، Latency، Jitter، Packet Loss و Stability
✅
بررسی اینکه Endpoint برای Tunnel آماده هست یا نه
✅
امکان دیدن و کپی کردن نتیجه کامل به‌صورت JSON
این نسخه برای کاربران عادی طراحی شده تا اتصال راحت‌تر و بدون دردسر انجام شود؛ اما برای کاربران حرفه‌ای هم تنظیمات دقیق‌تر در دسترس است تا بتوانند اتصال را با شرایط شبکه خودشان بهتر هماهنگ کنند.
⚠️
توجه: این نسخه هنوز بتا است.
اگر مشکلی مشاهده کردید، ارسال گزارش خطا، لاگ برنامه و توضیح شرایط شبکه شما کمک زیادی به بهتر شدن نسخه‌های بعدی می‌کند.
ممنون از همراهی شما با WhiteDNS
🤍</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/whitedns/716" target="_blank">📅 08:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-715">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nv1BOKr2AmO3VqazJoAUXCdQO_R0eqz_-3guCiyc2Zzvhz4QLTmuVplgTQR6Ju073K8jAydOfOXI8Gh6rfFdm_YewHSDffskp7n5p8acd4TAvceIqgeDdnPlBN3oMPGlSNF-CTc_flZiD753Qr1bT5v5Gw-d0otSOVPbVz4XS3DQq_GAKTxB3VqoUBLy4rvA-VG8OrjvSp_snF0FQEu-HawUp_k7rI0fQg5AqPpJjM_fR7Pi8pQb0OhnjiiQHOJkVJuFKebruifZ4TA4mA19mLNzbeZEbnS5fwI0UazpqiT7LyHPJ3633RGIN7fIv7v6Apv_DbOKhs-0TjFg7LzzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همراهان عزیز،
بعد از بازخود هایی که ما از ورژن قبلی اپ ویندوز گرفتیم، تصمیم به بازنویسی این نرم‌افزار برای سیتم عامل های
مک ، ویندوز و لینوکس
گرفتیم.
تقریبا تمام امکانات اپلیکیشن اندروید در این اپ خلاصه شده اما با قدرت و منابع بیشتر.
سعی میکنیم هرچه زودتر اپ رو آماده و در اختیارتون قرار بدیم.
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/whitedns/715" target="_blank">📅 07:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-714">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">خب این هم آموزش SNI Spoof برای مک.
فرآیندش برای ویندوز و لینوکس کاملاً مشابه هم هستش. فقط باید فایل اجرایی‌ای که برای sni spoof هستش رو مطابق سیستم‌عاملتون دانلود کنین.
فرقی هم نداره که از چه برنامه‌ای برای کانفیگ‌ها استفاده کنین.
لینک دانلود برنامه SNI Spoof برای مک و لینوکس
برنامه آپلود شده در تلگرام
لیست کانفیگای جمع آوری شده توسط متین عزیز.
کانفیگ JSON
لینک دانلود ویدئو بالا برای اینترنت ایران.
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/whitedns/714" target="_blank">📅 02:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-713">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp44HYg66I9IFP51AJAPeqjQY3BCyXVlI5ud01Dp40RsfDfN0Fj9kqF3JjLVlcslyd-VIu3haw8HurXo-SSCdKdIpYKBcQcxDdP0vft9jSJDhN105ONu9awILTW_1YIdeWQR5rRZKxTq7L4ydf3OZF2PO2AaNN61FBna6RC06QFI1qZF9O_5E41srcIsLcsSnGRSgJDVFm0tA94VTu7wp3nwR9c9IpxkVMdWtQjlio3ki9AQTxxJ_I68w5ql_sp6OVcr_NCvNCK-1LodPOE32R--mYql-j0N8_0faPyUjqsmyWdzHPIZKW43nxfJbB37UybBk32K3ceV1NtxxYAVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد میکنم تنظیمات موازی سازی MTU رو بین ۵۰ تا ۳۰۰ بسته به جدید قدرت گوشی همراهتون بذارید.</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/whitedns/713" target="_blank">📅 18:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-708">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/708" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/whitedns/708" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-707">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc7OTT2s3mavtkT1OBzYEOlHW6NjY52w0KBkU3ShseB6xAWbtRfpQ4ReTxiCl6rYMwzKekQ5uF8lg_2OWaQCezKAcRcJcxF_hr5B_djWRRv_AgR81fokpWglFTi5xdCDvoiKCnKaAJxX0hnG_oppG1lw0fB6lmkoSdFSZnStl7lcg0EZNkSg_16f5FHkAoEntvRgVioHacPsfH09Qp00U977LpRGVIgZtlwqaNAH8J1KlgsbXPluTUnzFbM5gMKGwRs3QISR8bcjpFC9VKH6KeGQspR0QeMadmCQg2KV_8TiswEVXvQrGvMxmPBnKG7Tqt_tNiU7YjsjGMtnNdEMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همراهان عزیز
تغییر بزرگی در این ورژن انجام نشده. تمرکز در این نسخه روی
بهبود  تست موازی تنظیمات بوده. در این نسخه تنطیمات بیشتری و بهینه تری به این قابلیت اضافه شده.
✅
نسخه اپلیکیشن به 1.5.1 ارتقا پیدا کرده
✅
جدا شدن تنظیمات پر مصرف و بهینه در تست موازی.
✅
بعد از یک همه پرسی در کانال، حالا تنظیمات در ۱۰ دسته متفاوت تقسیم شده تا بهینه ترین تنظیمات بر اساس ریزالور های انتخاب شده برای شما استافده شود.
@WhiteDNS</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/whitedns/707" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-705">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برای باز کردن اینستاگرام در مرورگر گوشی (بدون اینکه وارد اپلیکیشن شوید)، می‌توانید این مراحل را دنبال کنید:
📱
💻
۱.
مرورگر خود را باز کنید:
🌐
وارد مرورگر گوشی خود (مثل Chrome در اندروید، Safari در آیفون، یا Firefox) شوید.
۲.
به سایت اینستاگرام بروید:
📍
در نوار آدرس بالای صفحه،
[www.instagram.com](https://www.instagram.com)
را تایپ کرده و جستجو کنید.
۳.
وارد حساب کاربری خود شوید (Log In):
🔐
در صفحه باز شده، روی گزینه
Log In
ضربه بزنید و نام کاربری (یا ایمیل/شماره موبایل) و رمز عبور خود را وارد کنید.
نکته مهم (جلوگیری از باز شدن خودکار اپلیکیشن):
⚠️
بسیاری از اوقات، وقتی آدرس اینستاگرام را در مرورگر وارد می‌کنید، گوشی به طور خودکار شما را به اپلیکیشن اینستاگرام (اگر نصب باشد) هدایت می‌کند. برای جلوگیری از این اتفاق، می‌توانید از ترفندهای زیر استفاده کنید:
راه حل اول (سریع‌ترین راه):
🚀
مرورگر خود را در حالت
ناشناس (Incognito یا Private)
باز کنید و سپس سایت اینستاگرام را در آن وارد کنید. در این حالت، لینک‌ها به اپلیکیشن منتقل نمی‌شوند.
راه حل دوم (تغییر تنظیمات در اندروید):
🤖
به تنظیمات گوشی (Settings) بروید.
بخش برنامه‌ها (Apps) را باز کنید و Instagram را پیدا کنید.
به بخش
Open by default
(باز شدن به‌طور پیش‌فرض) یا
Set as default
بروید.
گزینه باز کردن لینک‌های پشتیبانی‌شده (Open supported links) را خاموش کنید یا روی حالت "همیشه بپرس" (Ask every time) قرار دهید.
راه حل سوم (در سافاری آیفون):
🍎
در گوگل کلمه Instagram را جستجو کنید. روی لینک سایت اینستاگرام در نتایج جستجو
انگشت خود را نگه دارید
(Long press) و از منوی باز شده گزینه
Open in New Tab
را انتخاب کنید.
@whitedns
📡</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/whitedns/705" target="_blank">📅 07:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-704">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">WhiteDns-Windows-Setup.exe</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/whitedns/704" target="_blank">📅 07:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-703">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/703" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteDns Windows 1.0.6
🖥
🔌
راهنمای اتصال هوشمند (Smart Connect)
🤖
قابلیت اتصال هوشمند به برنامه WhiteDns کمک می‌کند تا بهترین تنظیمات اتصال را به‌طور خودکار انتخاب کند. کاربران عادی نیازی به تغییر دستی تنظیماتی مانند MTU، Workers (تعداد پردازش‌گرها)، Packet Duplication (تکثیر بسته‌ها)، فشرده‌سازی (Compression) یا سایر تنظیمات در بخش پیشرفته (Advanced) ندارند.
✅
نحوه استفاده
📝
۱. برنامه
WhiteDns Windows
را باز کنید.
🪟
۲. به تب
Connect
(اتصال) بروید.
🔗
۳. مطمئن شوید که گزینه
Smart Connect
روی حالت روشن (
On
) قرار دارد.
🟢
۴. هدف اتصال خود را انتخاب کنید:
Stable (پایدار)
🛡
بهترین گزینه برای شبکه‌های ضعیف یا فیلترشده. این امن‌ترین و مطمئن‌ترین گزینه است.
Balanced (متعادل)
⚖️
برای اکثر کاربران توصیه می‌شود. این حالت تلاش می‌کند ضمن حفظ پایداری اتصال، سرعت خوبی نیز ارائه دهد.
Fast (سریع)
🚀
بهترین حالت برای زمانی که شبکه شما از قبل قوی است. ممکن است در این حالت از تنظیمات تهاجمی‌تری استفاده شود.
۵. موتور (Engine) را انتخاب کنید:
⚙️
MasterDNS
برای اکثر کاربران و اتصالات پایدار توصیه می‌شود.
StormDNS
در صورتی از این گزینه استفاده کنید که پروفایل/سرور شما برای StormDNS ساخته شده است یا می‌خواهید موتور سریع‌تر را آزمایش کنید.
⛈
۶. حالت پروکسی را انتخاب کنید:
🌐
System proxy (پروکسی سیستم)
برای وب‌گردی معمولی توصیه می‌شود. مرورگرها و بسیاری از برنامه‌های ویندوز به‌طور خودکار از WhiteDns استفاده خواهند کرد.
🖥
SOCKS5 only (فقط SOCKS5)
اگر می‌خواهید پروکسی را به‌صورت دستی در برنامه‌هایی مانند تلگرام تنظیم کنید، از این گزینه استفاده کنید.
📱
۷. روی
Connect
کلیک کنید.
👆
چه اتفاقاتی به‌طور خودکار رخ می‌دهد؟
🔄
وقتی اتصال هوشمند (Smart Connect) روشن است، WhiteDns کارهای زیر را انجام می‌دهد:
- استفاده از موتور انتخاب‌شده (MasterDNS یا StormDNS).
🛠
- بررسی تنظیمات موفق که در دفعات قبل جواب داده‌اند.
✔️
- انتخاب یک پیش‌تنظیم (Preset) مناسب بر اساس هدف شما.
🎯
- استفاده از بهترین تنظیمات شناخته‌شده برای تحلیلگر (Resolver).
📊
- امتحان کردن تنظیمات جایگزین امن‌تر (Fallback) در صورتی که تلاش اول ضعیف باشد.
🛡
- به خاطر سپردن تنظیمات موفق برای استفاده در دفعات بعدی.
💾
کدام هدف (Goal) را باید انتخاب کنم؟
🤔
ابتدا از
Balanced
استفاده کنید. این بهترین حالت پیش‌فرض برای اکثر کاربران است.
✅
در شرایط زیر از
Stable
استفاده کنید:
- اتصال مرتباً با شکست مواجه می‌شود.
❌
- اینترنت شما به شدت فیلتر است.
🚫
- تونل وصل می‌شود اما اتصال به سرعت قطع می‌گردد.
- سرعت برایتان نسبت به پایداری و اطمینان در درجه دوم اهمیت قرار دارد.
در شرایط زیر از
Fast
استفاده کنید:
- حالت Balanced در حال حاضر به خوبی کار می‌کند.
- سرعت بیشتری می‌خواهید.
⚡️
- شبکه یا سرور شما قوی است.
💪
تنظیمات پیشنهادی برای کاربران عادی
👥
اتصال هوشمند (Smart Connect):
On (روشن)
🟢
هدف (Goal):
Balanced
⚖️
موتور (Engine):
MasterDNS
🛠
پروکسی:
System proxy
🌐
سپس روی
Connect
کلیک کنید.
👆
اگر متصل نشد چه کار کنیم؟
🛠
این مراحل را به ترتیب امتحان کنید:
۱. هدف را به
Stable
تغییر دهید.
🛡
۲. گزینه Smart Connect را همچنان
On (روشن)
🟢
نگه دارید.
۳. دوباره روی
Connect
کلیک کنید.
۴. اگر باز هم متصل نشد، به بخش
Resolvers
بروید و یک اسکن اجرا کنید.
🔍
۵. بهترین نتایج Resolver را اعمال (Apply) کنید و سپس دوباره سعی کنید متصل شوید.
✅
برای کاربران تلگرام
💬
اگر از گزینه
SOCKS5 only
استفاده می‌کنید، پروکسی تلگرام دسکتاپ را به این شکل تنظیم کنید:
نوع (Type): SOCKS5
هاست (Host):
127.0.0.1
پورت (Port): 18000
نام کاربری/رمز عبور (Username/Password): خالی بگذارید
🔓
اگر از
System proxy
استفاده می‌کنید، مرورگرها معمولاً به‌طور خودکار متصل می‌شوند، اما تلگرام ممکن است همچنان به وارد کردن تنظیمات دستی SOCKS5 نیاز داشته باشد.
برای کاربران حرفه‌ای
🎓
اگر گزینه اتصال هوشمند را خاموش (
Off
) کنید، WhiteDns از پروفایل فعلی و تنظیمات پیشرفته‌ی (Advanced) شما دقیقاً همان‌طور که هستند استفاده خواهد کرد. این ویژگی برای زمانی که می‌خواهید کنترل کامل و دستی روی تنظیمات داشته باشید بسیار مفید است.
🔧
🚫
خیلی مهم :
به هیچ عنوان هیچ نرم افزار vpn دیگری مثل v2ray و یا ..... نباید روی سیستم شما باز باشد . مطمن شوید که حتی در پس زمینه هم بسته شوند
🚫
برای تست روی مرورگر ها حتما از گزینه New Private window یا New incognito window استفاده کنید
👍
@whitedns</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/whitedns/703" target="_blank">📅 07:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-702">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RiIj4MOn-NI_CbhY6B8gEDrC7rfZSPI60sZ-dHH4MiWMNcITq_HQAZlhLvprCVSdTGL5a2FZnZlXDB0zx1gHgjlK4xQDVJMF0JLcZ8M59TML5VgqTV4JIEmkDlRmRVsA_toR4Limq5A2as_2P_CrGB6MlB7uXlwU-zVUMkoQ-07lXpla0bumj0E8wA9MXMY8VYOgGa5DCXLtR8JEMKb-Dhm7mV-YcxXksMRrj4JnteT1fsK9Wx9LNYXHYqitPM1FT0zKij614C0F3FAgFSZoVzKgFQ8RRyGc8j_ZwDVv-GnlX4Dvky8Z_PiXccxAGTN2CKjjblvqqVtyz6osHfqB8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در نسخه ۱.۰.۶ -
WhiteDns Windows
🪟
قابلیت
«اتصال هوشمند» (Smart Connect)
اضافه شده است؛ یک حالت اتصال خودکار جدید که به کاربران کمک می‌کند بدون نیاز به تغییر دستی تنظیمات در تب پیشرفته (Advanced)، به تنظیماتی پایدار و مطمئن دست پیدا کنند.
🚀
اکنون قابلیت اتصال هوشمند می‌تواند اتصال را بر اساس موتور (Engine) انتخاب‌شده، سرور، کیفیت تحلیلگر (Resolver) و نتایج موفق قبلی تنظیم و بهینه‌سازی کند.
⚙️
کاربران می‌توانند یک هدف ساده را انتخاب کنند:
پایدار (Stable)
🛡
متعادل (Balanced)
⚖️
سریع (Fast)
⚡️
. سپس برنامه پیش از برقراری ارتباط، به‌طور خودکار تنظیمات انتقال و تحلیلگر امن‌تری را برای MasterDNS یا StormDNS انتخاب می‌کند.
همچنین این نسخه نتایج موفق اتصال هوشمند را به تفکیک هر سرور، موتور و شبکه به خاطر می‌سپارد؛ در نتیجه اتصالات بعدی می‌توانند با استفاده از تنظیماتی که پیش‌تر جواب داده‌اند، سریع‌تر برقرار شوند.
🧠
اگر مسیر اتصال ضعیف باشد، قابلیت اتصال هوشمند پیش از نمایش پیام خطا، تنظیمات جایگزین امن‌تری (Fallback) را امتحان می‌کند.
🔄
صفحه اتصال (Connect) با یک پنل کنترل جدیدِ اتصال هوشمند به‌روزرسانی شده است، در حالی که امکان اتصال دستی معمولی همچنان برای کاربران حرفه‌ای در دسترس قرار دارد.
🛠
@whitedns</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/whitedns/702" target="_blank">📅 07:12 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
