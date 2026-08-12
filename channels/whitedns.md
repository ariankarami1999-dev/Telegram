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
<img src="https://cdn5.telesco.pe/file/LTD7D70UwSKnOrM95U9YxDzrMZSzNzah_tWbH9XSvLk_d1GstpxoaqjOXV-Xsh7Zg_3GqeEW6IovZxPHhoORbte45msOUuE9TUiE47QaFTH_2rMoYFkmVBLRtUba3r3V7Lr6s-FlqSx2AKbBUL-31HfMbtCArzgQmgNJR44itBUrVnhYC5ulZiRXcO5J1EtmwV1YNsoFd8H-Lr--95XFAd_Rv0baI2kfB_FH1fQOpbJlAHQFtsg5HTD3UYkYgN2yHQSyvmEDX1kA8jBOw_S5i5UTCYgGj0hYGzj7HaMullP1K6iZYQWvRHtNRtwDREczzUk9FwQwsWbD8jo0-EINaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 02:01:18</div>
<hr>

<div class="tg-post" id="msg-1443">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Whitevpn dekstop v1.0.16
🍎
🐧
راهنمای استفاده روی مک و لینوکس
حالت TUN فعلاً فقط روی ویندوز کار می‌کند. روی مک و لینوکس دو حالت دیگر هست که برای اکثر کارها کافی‌اند.
━━━━━━━━━━━━━━━
🖥
روی مک — ساده‌ترین حالت
تنظیمات ← اتصال ← «پراکسی سیستم» را انتخاب کنید و وصل شوید. تمام.
مک تنظیم پراکسی را در سطح سیستم اعمال می‌کند، پس تقریباً همهٔ برنامه‌ها (سافاری، کروم، فایرفاکس و بیشتر اپ‌ها) خودکار از تونل رد می‌شوند.
━━━━━━━━━━━━━━━
🐧
روی لینوکس — یک نکتهٔ مهم
«پراکسی سیستم» روی لینوکس تنظیمات گنوم و KDE را عوض می‌کند. ولی این یک ترجیح است، نه اجبار: برنامه‌هایی که این تنظیم را می‌خوانند رد می‌شوند، و برنامه‌هایی که نمی‌خوانند نه.
معمولاً کار می‌کند: کروم، کرومیوم، فایرفاکس
معمولاً کار نمی‌کند: تلگرام دسکتاپ، ابزارهای ترمینال
برای آن‌هایی که کار نمی‌کنند، سراغ بخش بعدی بروید.
━━━━━━━━━━━━━━━
🎯
وصل کردن یک برنامهٔ خاص (روی هر دو سیستم)
اگر می‌خواهید فقط یک برنامه از تونل رد شود — یا برنامه‌ای پراکسی سیستم را نادیده می‌گیرد — این راه مطمئن‌ترین است.
آدرس پراکسی، بعد از وصل شدن، در صفحهٔ اصلی نشان داده می‌شود. روی آن کلیک کنید تا کپی شود. معمولاً:
127.0.0.1:2080
این آدرس هم SOCKS5 و هم HTTP را می‌پذیرد.
📱
تلگرام دسکتاپ
Settings ← Advanced ← Connection type ← Use custom proxy
نوع: SOCKS5 — آدرس:
127.0.0.1
— پورت: 2080
🦊
فایرفاکس
Settings ← Network Settings ← Manual proxy configuration
SOCKS Host:
127.0.0.1
— Port: 2080 — گزینهٔ SOCKS v5
⌨️
ترمینال (curl، git، npm و…)
این‌ها هیچ‌وقت از تنظیمات گرافیکی پیروی نمی‌کنند و باید دستی بهشان گفت:
export http_proxy=
http://127.0.0.1:2080
export https_proxy=
http://127.0.0.1:2080
(فقط برای همان پنجرهٔ ترمینال اعمال می‌شود)
━━━━━━━━━━━━━━━
💡
اگر نمی‌خواهید کل سیستم پراکسی شود
تنظیمات ← اتصال ← «فقط پراکسی» را انتخاب کنید. در این حالت هیچ چیزی روی سیستم شما تغییر نمی‌کند و فقط همان برنامه‌هایی که خودتان تنظیم کرده‌اید از تونل رد می‌شوند.
━━━━━━━━━━━━━━━
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.16</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/whitedns/1443" target="_blank">📅 16:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1440">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">Whitevpn desktop V1.0.15 ( linux 24+)
🐧
راهنمای نصب روی اوبونتو ۲۴ و بالاتر
بعضی از دوستان روی اوبونتو ۲۴ به بالا موقع نصب با خطای dependency روبه‌رو شده‌اند. مشکل از برنامه نیست — فقط باید فایل درست را دانلود کنید.
━━━━━━━━━━━━━━━
📌
اول ببینید نسخه‌تان چند است
در ترمینال بزنید:
lsb_release -a
یا از مسیر Settings ← About نگاه کنید.
━━━━━━━━━━━━━━━
✅
اوبونتو ۲۴.۰۴ و بالاتر (شامل ۲۵ و ۲۶)
فایلی را دانلود کنید که در اسمش webkit41 دارد:
WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.deb
و نصبش کنید:
sudo apt install ./WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.deb
⚠️
حتماً ./ را قبل از اسم فایل بگذارید، وگرنه apt دنبال آن در اینترنت می‌گردد.
━━━━━━━━━━━━━━━
✅
اوبونتو ۲۲.۰۴ و دبیان ۱۲
فایل بدون webkit41:
WhiteVPN-Desktop-1.0.15-linux-amd64.deb
sudo apt install ./WhiteVPN-Desktop-1.0.15-linux-amd64.deb
━━━━━━━━━━━━━━━
🎯
ساده‌ترین راه: AppImage
اگر نمی‌خواهید درگیر نصب و وابستگی شوید، فایل AppImage را بگیرید. اصلاً نصب نمی‌خواهد و به هیچ کتابخانه‌ای روی سیستم شما وابسته نیست:
WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
بعد از دانلود، اجازهٔ اجرا بدهید و اجرا کنید:
chmod +x WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
./WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
(این فایل برای اوبونتو ۲۴ به بالا است)
━━━━━━━━━━━━━━━
💡
چرا دو تا فایل هست؟
اوبونتو در نسخهٔ ۲۴ کتابخانه‌ای که برنامه‌های گرافیکی از آن استفاده می‌کنند را عوض کرد. یک فایل واحد نمی‌تواند هر دو را پوشش دهد، برای همین دو نسخه می‌سازیم. فایل webkit41 مال نسخه‌های جدید است.
📥
دانلود همهٔ فایل‌ها:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/whitedns/1440" target="_blank">📅 13:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1438">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۵
🐧
رفع یک اشکال مهم روی لینوکس
روی لینوکس، بستن پنجره باعث می‌شد برنامه ناپدید شود اما در پس‌زمینه اجرا بماند — بدون هیچ آیکونی برای برگرداندنش. تنها راه بستنش، kill کردن از ترمینال بود.
دلیلش این بود: برنامه فرض می‌کرد آیکون نوار وظیفه ساخته شده، در حالی که خیلی از محیط‌های دسکتاپ (از جمله گنوم بدون افزونهٔ AppIndicator) اصلاً چنین آیکونی نشان نمی‌دهند.
حالا برنامه واقعاً بررسی می‌کند که آیا آیکونی نمایش داده می‌شود یا نه. اگر نه، بستن پنجره یعنی بستن برنامه.
📡
اشتراک اتصال روی شبکهٔ محلی
حالا می‌توانید اتصال این دستگاه را با دستگاه‌های دیگر روی همان شبکه به اشتراک بگذارید — گوشی، تلویزیون، یا هر چیزی که روی همان وای‌فای یا هات‌اسپات است.
تنظیمات ← اتصال ← «اشتراک روی شبکهٔ محلی» را روشن کنید. بعد از اتصال، آدرسی که در صفحهٔ اصلی نشان داده می‌شود را در دستگاه دیگر وارد کنید.
⚠️
توجه کنید: هر کسی که روی آن شبکه باشد می‌تواند از این اتصال استفاده کند و از کسی رمز پرسیده نمی‌شود. این را برای هات‌اسپات خودتان یا شبکهٔ خانگی روشن کنید، نه روی وای‌فای عمومی.
📤
خروجی گرفتن دسته‌جمعی از کانفیگ‌ها
اگر کانفیگ‌های خودتان را وارد اپ می‌کنید و تستشان می‌گیرید، حالا می‌توانید آن‌هایی که تست را پاس کرده‌اند یکجا خروجی بگیرید — به‌جای اینکه یکی‌یکی share بزنید.
تست بگیرید ← موارد سالم را انتخاب کنید ← «خروجی انتخاب‌شده‌ها»
خروجی را می‌توانید کپی کنید یا در یک فایل ذخیره کنید تا به گوشی یا تلویزیون منتقل کنید. حالت Base64 هم موجود است، چون بعضی کلاینت‌ها همان را می‌پذیرند.
━━━━━━━━━━━━━━━
⚠️
اگر نسخهٔ ۱.۰.۱۴ نسخهٔ مک (Intel) را دانلود کرده‌اید
فایل آن نسخه ناقص ساخته شده بود و احتمالاً درست کار نمی‌کند. لطفاً نسخهٔ جدید را دانلود کنید.
📥
دانلود:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/whitedns/1438" target="_blank">📅 12:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1437">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-poll">
<h4>📊 با whitevpn desktop وصل هستید ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/whitedns/1437" target="_blank">📅 11:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1436">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/whitedns/1436" target="_blank">📅 03:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1433">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی  این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1433" target="_blank">📅 20:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1432">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=o_zJTBGXEKAqjTo_UalagxTD9VM7-k9pEp9nfqv5-eXy9BPHMV9ZuDD01tm3ETpDuyMEe8SVGo4PJQ9Dd2oqU50EkXoqsz9HiG34mONyHgGDnWvmHjD52eKsYuWOHkFDEKk-LZUQD9pzp0s7vMCbDuXIcmBAwRALv2bPCaq5f69t9F36xV4WcuBMvSxfK3c9cSKgJj8o6AFJJJ7URnSEQYxUUevqwTDZbz8eaMK7TY98zoeR0_PUCQSASQXZfP0OGu6E1YlDEQWoZ8SuO0P_zm9VUceggiJlDYt9tlNgXgh_kf5bPrkGrCYsc6s0vhlvvMcwfVUwUBxMBTUi0NbsFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=o_zJTBGXEKAqjTo_UalagxTD9VM7-k9pEp9nfqv5-eXy9BPHMV9ZuDD01tm3ETpDuyMEe8SVGo4PJQ9Dd2oqU50EkXoqsz9HiG34mONyHgGDnWvmHjD52eKsYuWOHkFDEKk-LZUQD9pzp0s7vMCbDuXIcmBAwRALv2bPCaq5f69t9F36xV4WcuBMvSxfK3c9cSKgJj8o6AFJJJ7URnSEQYxUUevqwTDZbz8eaMK7TY98zoeR0_PUCQSASQXZfP0OGu6E1YlDEQWoZ8SuO0P_zm9VUceggiJlDYt9tlNgXgh_kf5bPrkGrCYsc6s0vhlvvMcwfVUwUBxMBTUi0NbsFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/whitedns/1432" target="_blank">📅 19:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1431">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/whitedns/1431" target="_blank">📅 16:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1430">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">White DNS
pinned «
موقت
⚠️
دوستانی که از Whitevpn موبایل و دسکتاپ استفاده میکنید لطفا در قسمت subscription رفرش کنید یک تعداد کانفیگ اضافه شده است   ممنون  @whitedns
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1430" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1429">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">موقت
⚠️
دوستانی که از Whitevpn موبایل و دسکتاپ استفاده میکنید لطفا در قسمت subscription رفرش کنید یک تعداد کانفیگ اضافه شده است
ممنون
@whitedns</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1429" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1428">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">White DNS
pinned «
دوستان عزیز،  در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1428" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1427">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1427" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1426" target="_blank">📅 08:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1425">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">موفت
⚠️
تا چند روز اینده ما دیگه اپدیت برای Whitevpn dekstop نداریم
اگر موردی بود لطفا توی تاپیک زیر مطرح کنید
حتما با هشتگ :
#whitevpn
- لطفا توضیح کامل باشد
✍️
- و سیستم عامل را قید کنید
💻
🔧
به موارد ناقص و نامشخص ترتیب اثر داده نمیشه
🚫
تاپیک :
https://t.me/whitedns_group/17904
🔗
@whitedns
📢</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1425" target="_blank">📅 13:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1424">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/whitedns/1424" target="_blank">📅 10:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1423">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ApsSWIjc-GqTxIy3ReaZx2FP6gzaW7EfZ5ZZnoeYUk5M_8tP3GrUd2mPC4aM3l0n-8JxmMoGQRp0hD170Se4olIVGCO-StOLYFtwg6tY0yUbC_0FbgpMV5rvFoxsjmzC_42qX8Ic5HYi9y3NK8P_FBFJsEiWlLrmFnEPoot4qwxJAkZI1KgbUiSsMBDyjDx0SoMwuq57pOD_KaJsSfTIrt3_4k5qR6wL9o1Sx8g33i4ZU6qmB1AzuR0JgvzJV0T8b3l2vr_HkTctt2QODF4RCOEyH5JsNw9aI1D7ZqXUmB7pnI55eANbVxc9eigbHaBcRhlaYS_fvnm1dvQ0fgzUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۳
Stable
🎯
حالت «فقط پراکسی» اضافه شد
تا حالا دو حالت بیشتر نبود و هر دو کل سیستم را از تونل رد می‌کردند. حالا سه حالت دارید:
• پراکسی سیستم — کل دستگاه (مثل قبل)
• فقط پراکسی — هیچ‌چیز روی سیستم شما تغییر نمی‌کند
• تونل TUN — کل دستگاه، حتی برنامه‌هایی که پراکسی را نادیده می‌گیرند
در حالت «فقط پراکسی» برنامه فقط گوش می‌دهد و شما خودتان تصمیم می‌گیرید چه چیزی از تونل رد شود. مثلاً فقط تلگرام، یا فقط یک افزونهٔ مرورگر — بقیهٔ سیستم دست‌نخورده و با سرعت عادی.
📌
چطور استفاده کنید
۱. تنظیمات ← اتصال ← «فقط پراکسی» را انتخاب کنید
۲. وصل شوید
۳. روی آدرس پراکسی در صفحهٔ اصلی کلیک کنید تا کپی شود
۴. همان را در تنظیمات پراکسی تلگرام وارد کنید
هم SOCKS5 و هم HTTP روی همان یک پورت کار می‌کند.
🔒
پورت دیگر عوض نمی‌شود
در این حالت پورت ثابت می‌ماند و خودتان می‌توانید تغییرش دهید. اگر برنامهٔ دیگری آن را گرفته باشد، همان موقع به شما می‌گوید — نه اینکه بی‌سروصدا پورت دیگری بگیرد و تنظیمات تلگرام شما یک روز بی‌دلیل از کار بیفتد.
━━━━━━━━━━━━━━━
⚠️
نکته برای کاربران فعلی
سوییچ TUN در تنظیمات جای خود را به یک منوی انتخابی داده. اگر قبلاً TUN را خاموش داشتید، روی «پراکسی سیستم» قرار می‌گیرید — یعنی دقیقاً همان رفتار قبلی. تا وقتی خودتان چیزی را عوض نکنید، هیچ فرقی نمی‌کند.
📥
دانلود:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/whitedns/1423" target="_blank">📅 19:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1422">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔵
WhiteVPN Desktop —نسخه 1.0.12
*stable *
🔋
از نسخه ۱.۰.۴ تا حالا تغییرات زیادی انجام  شده.
━━━━━━━━━━━━━━━
🔓
اشتراک‌هایی که باز نمی‌شدند، حالا باز می‌شوند
مهم‌ترین تغییر همین است. روی بعضی شبکه‌ها، اشتراک اصلاً دریافت نمی‌شد و خطای مبهمی دربارهٔ TLS می‌داد.
دلیلش این بود: نام سایت در اولین بستهٔ ارتباط بدون رمز فرستاده می‌شود. فیلترینگ همان یک بسته را می‌خواند و ارتباط را قطع می‌کند — قبل از اینکه اصلاً چیزی رد و بدل شود.
حالا آن اولین بسته به قطعه‌های کوچک شکسته می‌شود، طوری که هیچ قطعه‌ای نام کامل را در خود ندارد. سرور همان چیزی را دریافت می‌کند که همیشه، ولی دیگر چیزی برای تطبیق باقی نمی‌ماند.
این کار فقط وقتی انجام می‌شود که مسیر عادی شکست بخورد، پس روی شبکهٔ سالم هیچ کندی‌ای ندارید.
🔄
اشتراک‌ها خودشان به‌روز می‌شوند
اگر اشتراکی روی شبکهٔ شما باز نشود، فقط وصل شوید — اپ خودش آن را از داخل تونل دوباره می‌گیرد.
🔐
گزینه برای اشتراک‌هایی که گواهی‌شان تأیید نمی‌شود
روی بعضی شبکه‌ها چیزی وسط راه گواهی خودش را جای گواهی سرور می‌دهد. برای این حالت گزینهٔ «دریافت بدون بررسی گواهی» اضافه شده — فقط برای همان یک اشتراک، و فقط وقتی نشان داده می‌شود که واقعاً به کار بیاید.
⚠️
توضیحش را حتماً بخوانید: نشانی اشتراک کلید حساب شماست.
━━━━━━━━━━━━━━━
🔔
اطلاع از نسخه‌های جدید
اپ خودش بررسی می‌کند که نسخهٔ تازه‌تری منتشر شده یا نه و به شما اطلاع می‌دهد. دیگر لازم نیست دستی سر بزنید.
━━━━━━━━━━━━━━━
⚙️
تنظیماتی که حالا واقعاً کار می‌کنند
چند تنظیم بودند که ذخیره می‌شدند ولی هیچ اثری نداشتند. همه درست شدند:
• Split Tunneling —
اپلیکیشنی که کنار می‌گذاشتید واقعاً از تونل خارج می‌شود
• بررسی سلامت TLS — اتصالی که در آن دخالت شده باشد رد می‌شود
• نویز اتصال (Amnezia) — روی اتصال‌های WireGuard اعمال می‌شود
• پراکسی سیستم روی لینوکس — روی GNOME و KDE تنظیم می‌شود
━━━━━━━━━━━━━━━
🛡
حریم خصوصی و امنیت
• نشانی اشتراک دیگر در پیام خطا نمایش داده نمی‌شود. قبلاً اگر از صفحهٔ خطا اسکرین‌شات می‌گرفتید، کلید حسابتان هم در آن بود.
• روی ویندوز دیگر دسترسی Administrator نمی‌خواهد، مگر برای حالت تونل.
━━━━━━━━━━━━━━━
🐞
رفع اشکال
• پنجرهٔ مشکی PowerShell که هنگام اتصال در حالت TUN باز و بسته می‌شد
• نشتی DNS در حالت TUN
• در نصب تازه، لیست سرورها خالی نمایش داده می‌شد
• گزینهٔ پاک کردن اطلاعات برنامه و بازگشت به حالت اولیه در تنظیمات
• پیام‌های خطا حالا می‌گویند دقیقاً چه کاری باید بکنید
━━━━━━━━━━━━━━━
📥
دانلود برای ویندوز، مک و لینوکس:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.12
@whitedns</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/whitedns/1422" target="_blank">📅 14:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=IA-wMUgXsds2Bb74zifnCvY0EFoKkfFUG3Xxmw2MNlRxVi80iP9Oiispob1L3MCeo0afuLjILpH66_FGwgWC-gj4tNJPRcOsaumtyjWRKRuh3Q1RCL-NQGSdDAUxgI_jVzOy2NyIrchxYlGjo-wOZyDxzLotzjwt5by5nxrHXvfqKMFFJf_0DTI-MgwgQnuDUKJJVjLN4dmasMoDPzpO2eyVzMUuLeQnGYpUhx2rVwYj_7yfjaB6K07xmbXA1ff5QL2g6PnU27dpi4lv8oCpNk8POZhOH3kIbPMkSflxH-xov9QTHcOTpOSFXeY4g875oycYFKdaoXJim3QnnDF9MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=IA-wMUgXsds2Bb74zifnCvY0EFoKkfFUG3Xxmw2MNlRxVi80iP9Oiispob1L3MCeo0afuLjILpH66_FGwgWC-gj4tNJPRcOsaumtyjWRKRuh3Q1RCL-NQGSdDAUxgI_jVzOy2NyIrchxYlGjo-wOZyDxzLotzjwt5by5nxrHXvfqKMFFJf_0DTI-MgwgQnuDUKJJVjLN4dmasMoDPzpO2eyVzMUuLeQnGYpUhx2rVwYj_7yfjaB6K07xmbXA1ff5QL2g6PnU27dpi4lv8oCpNk8POZhOH3kIbPMkSflxH-xov9QTHcOTpOSFXeY4g875oycYFKdaoXJim3QnnDF9MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/whitedns/1420" target="_blank">📅 11:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔒
WhiteVPN Desktop نسخهٔ ۱.۰.۴ منتشر شد
🚀
۱. رفع نشتی DNS در حالت تونل — مهم‌ترین تغییر این نسخه
🔒
در نسخه‌های قبلی، وقتی روی حالت
TUN
وصل می‌شدید، خودِ ترافیک از تونل عبور می‌کرد — ولی درخواست‌های
DNS
از تونل بیرون می‌رفتند و مستقیم به مودم یا سرویس‌دهندهٔ اینترنت شما می‌رسیدند.
🌐
یعنی محتوای ارتباط شما محافظت می‌شد، اما
فهرست سایت‌هایی که باز می‌کردید برای ISP قابل دیدن بود
.
👀
علت پیدا و برطرف شد. حالت پراکسی هیچ‌وقت این مشکل را نداشت.
✅
⚠️
اگر از حالت TUN استفاده می‌کنید، حتماً بروزرسانی کنید.
🔄
۲. صفحهٔ Servers
🖥
•
انتخاب همه
اضافه شد
✅
•
کپی به کانفیگ‌های من
— یک سرور از ساب را به لیست خودتان کپی کنید و بعد آزادانه ویرایشش کنید
✏️
•
مخفی کردن
— سرورهایی را که نمی‌خواهید از لیست و از مسیر اتصال کنار بگذارید. بعد از بروزرسانی ساب هم مخفی می‌مانند، و هر وقت خواستید برمی‌گردانید
👻
• رفع به‌هم‌ریختگی ستون عملیات
🛠
⬇️
دانلود برای ویندوز، مک و لینوکس:
💻
🍎
🐧
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.4
@whitevpn
📲</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1419" target="_blank">📅 05:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=FxiGSaJr1f2NQO4XbB-kgJAoH_SnuXok7IV5moITMj2sAfHSW4pICxKnMwj22W1O3WA-wBMikaFL1vQO_pV2vVngv6flYCRIwbJQxq2nwOzEKFdbTHkAq3_eXDUKnI_M-RThrxFFyFKXn4_hxGt4WHQfd-Db_gSUIuqFOen1bZ1jj8u8crW-h9_BoObpoUlVcPyIk35bYRtKAm_kGpUA6iuMNlrip0MXMffz3yVESHyNhvG2dRME_M98f9gblZHxStp3WRBr2msVlb0-qWh9bSPZL1Z2yoDbEROwAh1Hqm8W5Pm_duRAe-Z-NO201s5j0j4tU2ILFoXa3XXsDu89IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=FxiGSaJr1f2NQO4XbB-kgJAoH_SnuXok7IV5moITMj2sAfHSW4pICxKnMwj22W1O3WA-wBMikaFL1vQO_pV2vVngv6flYCRIwbJQxq2nwOzEKFdbTHkAq3_eXDUKnI_M-RThrxFFyFKXn4_hxGt4WHQfd-Db_gSUIuqFOen1bZ1jj8u8crW-h9_BoObpoUlVcPyIk35bYRtKAm_kGpUA6iuMNlrip0MXMffz3yVESHyNhvG2dRME_M98f9gblZHxStp3WRBr2msVlb0-qWh9bSPZL1Z2yoDbEROwAh1Hqm8W5Pm_duRAe-Z-NO201s5j0j4tU2ILFoXa3XXsDu89IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/whitedns/1418" target="_blank">📅 01:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1416">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚀
WhiteVPN Desktop نسخهٔ ۱.۰.۳ منتشر شد
۱. اتصال خودکار از پایه بازنویسی شد
✅
حالا دقیقاً مثل نسخهٔ اندروید کار می‌کند: اپ دیگر خودش نودها را یکی‌یکی امتحان نمی‌کند، بلکه انتخاب را به موتور می‌سپارد تا از بین صدها نود، بهترینِ در دسترس را بردارد — و اگر نودی از کار افتاد، خودش روی نود دیگر می‌رود.
نتیجه: اتصال در چند ثانیه
⚡️
، و خطای «could not connect» که خیلی‌ها می‌گرفتند برطرف شد.
۲. رفع مشکل حالت تونل (TUN)
🛠
مشکلی که باعث می‌شد روی بعضی سیستم‌ها کانفیگ در حالت پراکسی وصل شود ولی در حالت تونل نه، پیدا و برطرف شد. کسانی هم که IPv6 سیستمشان را غیرفعال کرده‌اند دیگر با خطا مواجه نمی‌شوند.
۳. حذف و ویرایش کانفیگ در صفحهٔ Servers
✏️
کانفیگ‌هایی که خودتان اضافه کرده‌اید حالا قابل ویرایش و حذف هستند. برای اصلاح یک کانفیگ دیگر لازم نیست همه را پاک کنید و از اول وارد کنید.
۴. پیام‌های خطای واضح‌تر
📢
اگر اتصالی برقرار نشد، اپ دلیل واقعی را نشان می‌دهد نه فقط «ناموفق» — هم برای شما روشن‌تر است، هم گزارش مشکل را خیلی راحت‌تر می‌کند.
⬇️
دانلود برای ویندوز، مک و لینوکس:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1416" target="_blank">📅 19:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1415">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cjxpF6ZRW_5lDUnmSclaU8O4DfqsU_zaCEM-nN5m4dwCs98DGnWl8LJ8X8X5S198QH-zmLHVTv-ily-BDF1Dj4TMKGoxyBxSjx6I-suKMReVgNWQpTQH1pllmd6cmWYK48O2kNrOEcw-BAAnN6t_WvzTkW4VXSjoMprwNj8KHicpn9DEguDNBUgmUvRQZojzbh4H6fOrWqH08HyIfQ4YOyKWa37pbtp1JnlTmyJjow_WxN1rnyK8roNaITjkFL9_TO_nR5cY5MtFtYiT336Kqb4TJmRxGE6nCoAAXzkSJyeWx6gXyHOcdDypIMMadmAwQECXIt4_ZpLbnfVb9vw9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN
Desktop
نسخه 1.0.2 منتشر شد
🎉
مهم‌ترین تغییر: حالا هر نوع لینک اشتراکی را می‌شناسد
🔓
تا نسخهٔ قبل فقط لینک‌های اشتراک معمولی (vless، vmess، trojan و…) اضافه می‌شدند. اگر پنل شما خروجی Clash یا sing-box یا Xray می‌داد، برنامه خطا می‌داد
❌
از این نسخه این‌ها همه کار می‌کنند
✅
:
- لینک‌های اشتراک معمولی و base64
- کانفیگ Clash / mihomo (چه YAML چه JSON)
- کانفیگ sing-box
- کانفیگ Xray و v2rayN
- و حالت base64 هر کدام از این‌ها
فرقی نمی‌کند پنل شما کدام قالب را بدهد
📝
. سرورها مثل همیشه در صفحهٔ Servers می‌آیند و می‌توانید پینگ و سرعتشان را بگیرید
📶
، مرتب کنید و یکی را انتخاب کنید
🚀
.
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.2
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1415" target="_blank">📅 15:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1414">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌎
نسخه‌ی دسکتاپ WhiteDns منتشر شد!
📤</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/whitedns/1414" target="_blank">📅 11:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1413">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚀
معرفی اپلیکیشن WhiteDNS Desktop
کلاینت قدرتمند تونلینگ DNS برای کامپیوتر
اگر به‌دنبال ابزاری حرفه‌ای برای تونلینگ DNS، مدیریت پروکسی و عبور از محدودیت‌های شبکه هستید،
WhiteDNS Desktop
یکی از کامل‌ترین گزینه‌های در دسترس است.
این اپلیکیشن یک کلاینت محلی DNS Tunneling را روی سیستم شما اجرا می‌کند و در کنار آن، امکانات پیشرفته‌ای برای مدیریت پروکسی سیستم در اختیارتان قرار می‌دهد.
✨
ویژگی‌ها و امکانات کلیدی
🔹
پشتیبانی کراس‌پلتفرم
قابل اجرا روی Windows، macOS و Linux
🔹
پشتیبانی از موتورهای مختلف
امکان انتخاب بین موتورهای:
• CottenDNS
• MasterDNS
• StormDNS
🔹
پروکسی محلی کامل
دارای پروکسی‌های محلی SOCKS5 و HTTP، همراه با قابلیت تنظیم خودکار پروکسی سیستم
پس از قطع اتصال نیز تنظیمات پروکسی سیستم به‌صورت خودکار به حالت قبلی بازگردانده می‌شوند.
🔹
مدیریت پیشرفته پروفایل‌ها
امکان ساخت و مدیریت:
• پروفایل‌های اتصال چنددامنه‌ای
• پروفایل‌های Resolver
• Import و Export تنظیمات
• تهیه بکاپ از پروفایل‌ها
🔹
پری‌ست‌های آماده
تنظیمات از پیش آماده‌شده برای شرایط مختلف شبکه:
⚡️
Speed
— برای دستیابی به بیشترین سرعت
🛡
Survival
— برای پایداری بیشتر در شبکه‌های محدود
🔒
TCP Survival
— برای اتصال پایدارتر با استفاده از TCP
🔹
مانیتورینگ زنده
نمایش لحظه‌ای:
• وضعیت اتصال
• آمار ترافیک مصرفی
• اطلاعات نشست
• لاگ‌ها و رویدادهای برنامه
⚠️
هشدار امنیتی بسیار مهم
نسخه‌های رسمی WhiteDNS Desktop فقط از طریق ریپازیتوری رسمی پروژه در GitHub منتشر می‌شوند.
برای حفظ امنیت سیستم خود، برنامه را از سایت‌ها، مارکت‌ها، کانال‌ها یا منابع متفرقه دانلود نکنید.
📥
دانلود آخرین نسخه از GitHub رسمی:
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases/tag/desktop-v1.2.0
📢
عضویت در کانال رسمی تلگرام پروژه:
https://t.me/whitedns
🤍
WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/whitedns/1413" target="_blank">📅 11:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1412">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌎
نسخه‌ی دسکتاپ WhiteVPN منتشر شد!
📤</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1412" target="_blank">📅 09:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1410">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5z8eu86fgDlkIcwPE7Pp42bALmKlXBOp_ZH_Apnja2OYVvtDIQdee8stukMYdqZXKdC4YJ_grHii6tzI_xTxn1kwiO0F47N2Imy_9i5adYd_z5XIH1nkfcnxlx6ZSilS5-h7leMoftxiOzUBDwiZW8Fza4tJer9cSDP8UpcbVAiaHL68ZjEosEI8dIjIYMIihDaHN317ffazhKGi5LUhoswtN0cWeplZBt26kjqVIrSuUFbh-NZxOz_3crjmgnPEmlI6t-4YMkSZdCNTVgfY-g34lpmfu7ljWRKiQhyl_tNKgU6yBaUjcKIWAjFzT1amKT7DDaPYTheUFyvU57RRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
نسخه‌ی دسکتاپ WhiteVPN منتشر شد!
اگر می‌خواهید روی کامپیوتر بدون درگیری با تنظیمات پیچیده به VPN وصل شوید، WhiteVPN Desktop برای شما ساخته شده است.
💻
قابل استفاده روی:
• ویندوز
• مک، هم Apple Silicon و هم Intel
• لینوکس با بسته‌های AppImage، DEB و RPM
⚡️
اتصال ساده و سریع
• اتصال با اشتراک آماده WhiteVPN
• اضافه‌کردن اشتراک شخصی
• انتخاب خودکار بهترین سرور
• انتخاب دستی کشور، نوع اتصال یا سرور دلخواه
• نمایش IP و کشور واقعی اتصال
• بررسی خودکار سلامت اتصال و جایگزینی سرور خراب
📥
واردکردن کانفیگ شخصی
• پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard
• امکان واردکردن یک یا چند کانفیگ به‌صورت هم‌زمان
• فقط کانفیگ را کپی کنید و Ctrl+V یا در مک Cmd+V بزنید
• کانفیگ‌های شخصی در بخش Manual و بالای لیست قرار می‌گیرند
🚀
تست کامل سرورها
• بررسی سالم بودن سرور
• تست پینگ واقعی
• تست سرعت دانلود
• مرتب‌سازی بر اساس کشور، پینگ، سرعت و نوع کانفیگ
• تست‌ها بدون قطع‌کردن اتصال فعلی انجام می‌شوند
🛡
تنظیمات حرفه‌ای، با ظاهر ساده
• حالت Proxy برای ویندوز، مک و لینوکس
• حالت TUN برای اتصال کامل ویندوز
• تنظیم DNS و حریم خصوصی DNS
• Split Tunneling برای مدیریت مسیر برنامه‌ها
• تنظیم IP Fronting به‌صورت خودکار یا دستی
• مشاهده گزارش‌ها برای پیدا کردن سریع مشکلات اتصال
🧰
ابزارهای کاربردی
• White IP Generator: ساخت کانفیگ با White IP و اضافه‌کردن مستقیم به برنامه
• Validator: بررسی تعداد زیادی IP یا آدرس و ذخیره نتیجه‌ها
• Full Backup: پشتیبان‌گیری کامل از تنظیمات، اشتراک‌ها و کانفیگ‌ها و بازیابی آن‌ها
🌍
رابط کاربری کامل فارسی و انگلیسی
• نمایش صحیح راست‌به‌چپ
• فونت فارسی Vazir
• محیط ساده و مدرن
• ادامه اتصال در System Tray حتی بعد از بستن پنجره
📌
چند نکته درباره نسخه اول
• حالت TUN فعلاً فقط روی ویندوز فعال است
• در لینوکس ممکن است لازم باشد Proxy سیستم را دستی تنظیم کنید
• برنامه هنوز امضای دیجیتال ندارد؛ بنابراین ویندوز یا مک ممکن است هنگام اجرای اول هشدار نمایش دهد
🔓
WhiteVPN Desktop متن‌باز است و تحت مجوز GPL-3.0 منتشر می‌شود.
⬇️
دانلود آخرین نسخه:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
اگر برنامه برایتان مفید بود، لینک آن را برای دوستانتان هم بفرستید
❤️</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1410" target="_blank">📅 09:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1409">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سرور های فعال WhiteDNS داشته باشید برای تست و زمان قطعی (کلیک کنید روش کپی میشه)
کلاینت اندروید و IOS از CottenDNS پشتیبانی میکنن و به زودی کلاینت ویندوز هم آماده میشه
Server #1 thx to LordofCinder
♥️
Location: Turkey
🇹🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HufCfh7cgdGh4IHRvIExvcmRvZkNpbmRlciIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFzaGVudGFqaXIuc2JzLCBjLmFzaGVudGFqaXIuc2l0ZSIsImVuY3J5cHRpb25fa2V5IjoiZTU1NGI4ZmI4ZGU4Mjc4ZDJmMTFlODcwNDA0NDI2OWEiLCJlbmNyeXB0aW9uX21ldGhvZCI6M319fQ
Server #2 thx to Bamdad
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEJhbWRhZCIsInNlcnZlciI6eyJkb21haW4iOiJjLmJhbWFrLnh5eiIsImVuY3J5cHRpb25fa2V5IjoiMmRkZWI5ZGYyYzJiYTRkMyIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #3 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InBhcmlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI1MjViNjkwYjU4ZmU0MTI0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
Server #4 thx to Araskhatare
♥️
Location: France
🇫🇷
2
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgMiB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiYS5hcmFzLmRwZG5zLm9yZyIsImVuY3J5cHRpb25fa2V5IjoiNzFkM2MwOWYyYmY1NmVkYSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #5 thx to Coreforge
♥️
Location: Turkey
🇹🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7nwn4e3ICAgdGh4IHRvIENvcmVmb3JnZSIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFub255bW91cy5vYnNlcnZlciIsImVuY3J5cHRpb25fa2V5IjoiYjI3NTAzOTE5OWIxYzhjOSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #6 thx to Araskhatare
♥️
Location: USA
🇺🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7rwn4e4IDIgICB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidXNhLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI5MzY5NjVjZWYzOWQzMmE5N2JlMWEzZDA4YzhiZmM5MyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1409" target="_blank">📅 04:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1407">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/3ae84e81b7.mp4?token=fS1fpQcgk5IwXV9QkLBHLss3Ps6v4IFZdthUmT8THTFFPiFVb9IHNbAG4C0-879L-gdj7z5lX_J0haY8E8CEJ7W2FNqJemA9y53U39mxO7XVvidP0QBl58a6Rpu5_9pjhZrJL4SmgaNYG3yIskBle_KklcSM6J9ibuMK3eUCVIYFlBRPPce4z-OdgPJlmeO_rt8_D2QJICfGx2sOH_naEOja1vpSk9uvWbCCMSLuhymcCLlfcY2NbDHW20rCsbay5zSH7_Z8eR3Ex3TSnUOSmy4KnmrG47OKwQPQrdgrI6GfnQnFnPpIHzgkJq-iREbN3SEXc8EcyQA57uzxGQxDuA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/3ae84e81b7.mp4?token=fS1fpQcgk5IwXV9QkLBHLss3Ps6v4IFZdthUmT8THTFFPiFVb9IHNbAG4C0-879L-gdj7z5lX_J0haY8E8CEJ7W2FNqJemA9y53U39mxO7XVvidP0QBl58a6Rpu5_9pjhZrJL4SmgaNYG3yIskBle_KklcSM6J9ibuMK3eUCVIYFlBRPPce4z-OdgPJlmeO_rt8_D2QJICfGx2sOH_naEOja1vpSk9uvWbCCMSLuhymcCLlfcY2NbDHW20rCsbay5zSH7_Z8eR3Ex3TSnUOSmy4KnmrG47OKwQPQrdgrI6GfnQnFnPpIHzgkJq-iREbN3SEXc8EcyQA57uzxGQxDuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
نسخه دسکتاپ
whitevpn
اماده شده است و به زودی بعد از طی مراحل آزمایش منتشر خواهد شد
@whitedns</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1407" target="_blank">📅 19:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1403" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1402">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال  سریع‌تر و پایدارتر بوده است.  امکانات و بهبودهای جدید: •  شروع اتصال سریع‌تر •  انتخاب هوشمند بهترین سرور •  جابه‌جایی خودکار در صورت اختلال سرور •  کاهش خطا و نیاز به چندبار زدن دکمه اتصال •  بهبود Real…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1402" target="_blank">📅 15:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1401">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS_Setup_Servers.md</div>
  <div class="tg-doc-extra">3.8 KB</div>
</div>
<a href="https://t.me/whitedns/1401" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش نصب DNS اختصاصی برای WhiteDNS
آموزش کامل و
قدم‌به‌قدم
نصب و راه‌اندازی:
🟢
CottenDNS
🔵
StormDNS
🟣
MasterDNS
از تنظیم دامنه در Cloudflare تا نصب DNS و دریافت
Encryption Key
🔐
📚
آموزش به‌صورت متنی آماده شده و
لینک آموزش ویدیویی
هم داخل پست قرار گرفته.
🎥
📥
فایل آموزش رو دانلود کن و برای روز مبادا نگهش دار!
🚀
@WhiteDNS
·:¨༺
@BlueKnight_Net
༻:</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/whitedns/1401" target="_blank">📅 16:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1398">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/1398" target="_blank">📅 12:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1397">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc0b81933.mp4?token=Vn1twfwlILZjFqjp_ZeVRJAjhv9aTnS88S7iplWuW4zVScqjt53oKP4AK6jlS5h-k1Kk8AAhoFezWayGbBHdKKB_lqT-ery_tBZYXmCh61n53iWvKzDvPqz9Qpc6ZkBl5zG11C1wjQkqcfxyr8ue-4w-KVru0jdUvCauduZftSuZobeQICwuAyiSWkeuPBzymLtrJlR9UrHaUx0e8tT7n8A4DD17R_qG5watSovdlwi3jBh_1oHoHDpaXEKOWzk6-4NveKBPM4Qg-jqs6XrRpXz3XerPblkeyfLlI2l5ZalH41U4PjHTVQ2zmsipgE93LTEdErDksmVMatBKdLB4taOuZZ2GnQtbnte_1hpCpNy1gQOhxLB2D3tcoABrqTz0l9-Lfly2p3k6k3Ie0p3JVjN0R3kl8MPpM8Z9m34jyPUg3seSof8vmcPjsQuTYPcfCkH5bQuqkQ5RiB48IbcBVCXcBnCS3xFJ5ZtZo-DaYWAMaCW3BPDF7HRC663271RdrEVlNjfyejn0JnbOlF3pcvaQOHKh5TL1JbbyqreyaLkzgmjhgUCfTtV0zC-pHb1Su6TsOScv8NcBz-GnkitQxAdC9taj77ElDIHb88QIXMgnqi2KTCC1I9F6gJHbOM9wWsdtBPdXtQ6uOk1noSOadCnFfeuMW-MsSH599iw02TY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc0b81933.mp4?token=Vn1twfwlILZjFqjp_ZeVRJAjhv9aTnS88S7iplWuW4zVScqjt53oKP4AK6jlS5h-k1Kk8AAhoFezWayGbBHdKKB_lqT-ery_tBZYXmCh61n53iWvKzDvPqz9Qpc6ZkBl5zG11C1wjQkqcfxyr8ue-4w-KVru0jdUvCauduZftSuZobeQICwuAyiSWkeuPBzymLtrJlR9UrHaUx0e8tT7n8A4DD17R_qG5watSovdlwi3jBh_1oHoHDpaXEKOWzk6-4NveKBPM4Qg-jqs6XrRpXz3XerPblkeyfLlI2l5ZalH41U4PjHTVQ2zmsipgE93LTEdErDksmVMatBKdLB4taOuZZ2GnQtbnte_1hpCpNy1gQOhxLB2D3tcoABrqTz0l9-Lfly2p3k6k3Ie0p3JVjN0R3kl8MPpM8Z9m34jyPUg3seSof8vmcPjsQuTYPcfCkH5bQuqkQ5RiB48IbcBVCXcBnCS3xFJ5ZtZo-DaYWAMaCW3BPDF7HRC663271RdrEVlNjfyejn0JnbOlF3pcvaQOHKh5TL1JbbyqreyaLkzgmjhgUCfTtV0zC-pHb1Su6TsOScv8NcBz-GnkitQxAdC9taj77ElDIHb88QIXMgnqi2KTCC1I9F6gJHbOM9wWsdtBPdXtQ6uOk1noSOadCnFfeuMW-MsSH599iw02TY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش دریافت دامنه رایگان و نامحدود
دیگه لازم نیست برای کانفیگ های شخصیتون دامنه بخرید.
https://youtu.be/Tiods_aCJX8
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/whitedns/1397" target="_blank">📅 11:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1395">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/whitedns/1395" target="_blank">📅 10:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1394">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/whitedns/1394" target="_blank">📅 08:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1393">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
لطفا تست کنید و نتیجه رو با ما به اشتراک بگذارید.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/whitedns/1393" target="_blank">📅 07:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1388">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/whitedns/1388" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/whitedns/1388" target="_blank">📅 07:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1387">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdPWY6xNxkNS7iXm1Io5A6D6TEndVkCSBKG_1zjZO_ouSwYvT0of68_5yfZ_WlZ3g-AtdH3pC4c4swdL6jhnh5CiF-WFVJcEoVMOCilESmyNd6tnkBgWK-caof-4ukD9QC-jCFsxL_MHthNEXW7UdVW6YDvTOlBPYrmKao4xv4UhlbL1yOr3--eUh4uXmWoV3NDrdxGh9z0jGNDMsDvKTX6318PX3MtOCo7NR0dnD2PDJXZqOzBgsmKlK3azYhTR4uPPT-OCDkSnQVCRSNjOrsHua2T6FuV36tcn6bbzsrJJXDDHxl8COBDH8rbVAC8kJChBxtyzWE4ghWh2QlKxjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/whitedns/1387" target="_blank">📅 07:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1386">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⛏
اگر در اتصال به WhiteVPN مشکل خوردید مراحل زیر را اجرا کنید
۱. به صفحه تنظیات برید
۲. از گرینه حریم خصوصی DNS گرینه DOH را انتخاب کنید
۳. مقدار زیر را جاگزین کنید
https://doh.whitedns.workers.dev/dns-query</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/1386" target="_blank">📅 17:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1378">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4JybDzYy96hqdTOvf3ojyOnJfSLlP7bZ6JORorgYizIJJvPgi-wf_QFGE6sX3LBh9tlgoF6JOpQdFaMhA9MhjE_ZkpwLjsrPIjr76b3x0Q4E2lX-lD3EJUca7rlO3lEIXY-0gWoC9yqwlZVVxqJuMmeoJD93_valh-W3zMqAoFaW2vz8rejncryP9xefcELphQFsSWoadjQBZi2C6wIjnP8APtbHsuB9RvA1D_q7syw5DFvQUP06pyKeoxz6GZBKdzXgiLmTTvt6pXQTAxg1dbXp68VMN6rP9OaKU7ELRv5txM8u5S6QufGzqhn9o7H3FfLGjUnZiUH_UiB-_sIsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای  ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/whitedns/1378" target="_blank">📅 11:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1377">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIIlQjdT2gvWXFuPEaT5UgYxQ1hZ7WtOl_1mCDBVxtKGkrzK6lid2Z0NyOVtQUlqSiez8nYlgwVB9HJC0ixEqQZdQlxgzp6P4_FXOJ4uy3Ch6VJMk2b0ob6qnbnTsNS0aQQ0Le8pbpCbCGix0vKH4a7j8FCLA3KDsebryCWtFHmmV98oOKpijmktM4DpF5VazORmoRERl9pDMDC3b6UHbzjqst-nueXPtR006Pok3SlXdrtNCBKUJwFLNezl39fGIYuJKnRdJFXsNSrHtQj3KAQyrJXX5xgQxfqC5sJAjeYlD6ZZqaW93vhtAAdtzhtUWQVzhJkNOtFpXUw0ofIyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/whitedns/1377" target="_blank">📅 04:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1375">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-text">پروژه دفید روی گوگل پلی قرار گرفت
میتونید از قسمت تنظیمات از چت ها و .. فایل پشتیبان بگیرید و بعد حذف کنید و بعدش از طریق گوگل پلی برنامه رو نصب کنید و دوباره فایل پشتیبان رو بازیابی کنید
https://play.google.com/store/apps/details?id=com.thefeed.android
میتونید با امتیاز ۵ ستاره دادن به پروژه از من حمایت کنید
🙏
❤️
❤️
❤️
ویدیو آموزشی پروژه:
https://t.me/networkti/516</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1375" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1374">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور   https://youtu.be/epG70Xl1xGI   @WhiteDNS</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/1374" target="_blank">📅 11:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1373">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=k2HaN9gbdubSJEv5EmjAht3confwYvZW89AGBWZbSVuhPcNq3Wjbp13URLHrWpBafZQ-59JL4qAL2XiGQLEnTCfSeBArojqz8Q4Hb36V7Uilxh3Mf82KpPGBaUIpI8Vw2H0DCWV6Qa_se_IzQEwNF_wHTj3p4Ow35uDkHx-U8WXfEJMqWGY1P6EulDVxFvNsnfmgc0JZFwMFivenV5UW1L-WaTQYNG_VKIwJJmo7B9LE0zR8w8sxqYK6xkbapNiS5seaXsyeEtIIdFkxgYM_rm4wpHX5_s7jMQDuvTvewNMmwsuEH911r2rLPBkBHGuyb_sa1kRKmhlTi-UFzwHyb4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=k2HaN9gbdubSJEv5EmjAht3confwYvZW89AGBWZbSVuhPcNq3Wjbp13URLHrWpBafZQ-59JL4qAL2XiGQLEnTCfSeBArojqz8Q4Hb36V7Uilxh3Mf82KpPGBaUIpI8Vw2H0DCWV6Qa_se_IzQEwNF_wHTj3p4Ow35uDkHx-U8WXfEJMqWGY1P6EulDVxFvNsnfmgc0JZFwMFivenV5UW1L-WaTQYNG_VKIwJJmo7B9LE0zR8w8sxqYK6xkbapNiS5seaXsyeEtIIdFkxgYM_rm4wpHX5_s7jMQDuvTvewNMmwsuEH911r2rLPBkBHGuyb_sa1kRKmhlTi-UFzwHyb4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/whitedns/1373" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">3 سرور اهدای CottenDNS
لطفا تست کنید و نتیجه رو بهمون بگید ( کلیک کنید روش کپی میشه )
Server #1 thx to Araskhatare
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imdlcm1hbnkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI5ODQ0NDhjZDRkZTYxZjgiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
Server #2 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InBhcmlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI1MjViNjkwYjU4ZmU0MTI0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #3 thx to Araskhatare
♥️
Location: Israel
🇮🇱
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HrvCfh7EgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyMjRiOWU4MjVlMzFkNWY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
@whitedns</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/whitedns/1371" target="_blank">📅 23:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oTgok-hCsi6n7L7I-KWZGA7vARJLPMiOy4EbXuIBdWS33eWCwOJDyJRCC6LmGx-4Xd5f_GprYLGPUtqJ98YpERKsycf2QaoCTzWwMI8qG2QwJxauFfN6IO-a6I-KUyMyytIaMQ2_WHvaFpXE7mbLAjwtis4rGzX3PAppE-xLzU3d9D6mZMRWU45Q6sE1Em7oFgfgmayU3ZaNCuJ-hnb2kWyDyG6Xy4AkKyluTTWouE_vh8n9CTns0zrmmlecLVFXtxqWYXE0ZurNDpG78--qF8NodD5PvQgFOArCvOM0pJGCkX1LjHyNS5OlXeHnyzx4lQPQMoUdKVKJWjAtAZ9_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه مهم درباره وضعیت ممیزی امنیتی پروژه‌ها
از این پس، هر پروژه‌ای که از برنامه ممیزی امنیتی
WhiteDNS Security
خارج شود، دیگر تحت نظارت امنیتی ما نخواهد بود.
این موضوع به این معناست که:
آخرین نتیجه ممیزی تنها مربوط به نسخه‌ای است که در زمان ارزیابی بررسی شده است.
هرگونه تغییر در کد، تنظیمات، زیرساخت، وابستگی‌ها یا به‌روزرسانی‌های بعدی می‌تواند وضعیت امنیتی پروژه را تغییر دهد.
پس از خروج پروژه از فرآیند ممیزی، WhiteDNS هیچ تضمین، تأیید یا مسئولیتی نسبت به امنیت نسخه‌های جدید یا وضعیت فعلی آن پروژه نخواهد داشت.
ادامه استفاده از پروژه، صرفاً بر عهده توسعه‌دهندگان و کاربران آن است.
در صورت بازگشت پروژه به برنامه ممیزی و انجام ارزیابی مجدد، نتیجه جدید به‌صورت رسمی اعلام خواهد شد.
آخرین وضعیت معتبر هر پروژه، تنها از طریق اطلاعیه‌های رسمی WhiteDNS قابل استناد است.
@whitedns</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/whitedns/1370" target="_blank">📅 11:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1368">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این روزها شاید همه استرس داشته باشیم
🤯
، بی‌حوصله باشیم
😑
و حالمون خوب نباشه
🥀
برای همین درست نخوانیم
📖
، درست نبینیم
👀
، ...
ولی برای اینکه نه به خودتون
🙅‍♂️
و نه به ما بد بگذره، لطفاً متن‌هایی که توی کانال می‌گذاریم را با دقت بخونید
✨
👀
ممنون
🙏
😊</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/whitedns/1368" target="_blank">📅 05:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hptkuDRqk7AoSPr2BddSxzMBvrCxMnLUHU54wHdpDW3WsRMevnwaIoVh6DFD6H8szICIJCtHXv6ENnzGfLCt2gr3Xtu9gFob5-qRFm7UINRzSYME5jbl8YMPYAg9C362URESzgmP9Zu7zluw_w_b1ld6EjDiDJbUiFd6bxnMrFDEtsQ_wr6ZFWfRPyntymQCDuNhGJ3OxSd145cfmroUFsHkraqXjy8VXoc6aHbg3n97Ru-gIFbSa8fV8tq9OYJtXlibzYp3saXlDD2xDGthcEib4u2UZVRZ5MNCqng6XoMxsVdiaUhql90COZ4wZ8byRC_eDzovXQjXHVz42g8OqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/whitedns/1367" target="_blank">📅 05:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1362">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1362" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1362" target="_blank">📅 05:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1361">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR0kPo_KNu-HclbDXS15bAS7D2vUiQh5EET46sSgsWo0pqwDdSARlNtPHJqZEeicx8iXDR-aLUw6d6wqVvDRhr1fMZd11O0CO--4SiG0g14q7WYJUMK0m7idfqoGlvkOEcGxk4W-6zojL51gBTfx2vV24AHz8U03ozDAhNlQjN1oVSXhzfQxS-tYj9uuHag_PeyHE5HDAQSHvHTQPHAZkSZz1o6OXM8WUfLqc7CvVy0GAuPkebm5dzCOZzkzHMF-EqxI4k2vnQn7cKnh4BU6CgIPkqhkevO1ojp44Q9sgTp_Vc40lUGOFQD7L3FYZ8JSFakXpOH_OvPUMvpyFviZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1361" target="_blank">📅 05:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1360">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/q_O9DQ-1-ajvF1-lFpHs3Po4dYd5iOjsyLHcXZSkyGS5jVgHNcmK11_GOkIAopDaGIkLDkzU0CmA4MjEfxTuduMGOAmJGjuGDLSPOJFgn15XPRXMM4-1FRunvR3ST3dIKeeNrXZUwrSsL2QvduPbFoM-xuJ07hbPdHiZqo1q4REG-G_9DWx0sqGzZoV2afmCiT4L0auulYG5FSCi6yyRFIeZO3S7a61CTqRBBmrX_Zxk7IUCS1xMOmb4xvdmk2-ZhCq39xnQJ1rrVjGwfrJtRd7-Uxpf13ODFZn3FacXNcliYHQD49PYIWDDtQAJx0Qy7FUrr4g-iKQgXa02pJFWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان
👋
کلاینت Aether  در دو نسخه اندروید و ویندوز که به تازگی توسط کانال ما منتشر شد -دیگر توسط تیم whitedns بررسی امنیتی (audit) نخواهد شد و ما از این لحظه امنیت این کلاینت را تایید نمیکنیم
⚠️
لطفاً با مسئولیت خودتان از این کلاینت استفاده کنید و یا کلاً این کلاینت را حذف کنید
🗑
لینک نسخه اندروید و ویندوز در زیر این پیام برای شما قرار داده شده که بدانید در مورد کدام کلاینت حرف میزنیم
https://t.me/whitedns/1315
https://t.me/whitedns/1335
نکته:
کلاینت مشابهی که توسط Matin senpai انجام شده مشکلی ندارد و میتوانید با خیال راحت از آن استفاده کنید
✅
@whitedns</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1360" target="_blank">📅 04:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1359">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1359" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1357">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UF9XUvnw_Rbb2J5ZPyF6RI4jAu8FcgQAitoLiL-MuvI-aZeyPX8FQKMrk-weHEnuf6ANszRkO8V-UTF_VcUNsffK8ISVVSNYBs482UE1860It8FcnTkv3w63xIoq62qVef3cQOfRGE2-tiQkJbhBFA0U8_icdtHGkF4Du7J7xVKMn6If6A3tVpYzE6ibRNdxySxZw_KHlrXsstuaJIZYGK_DB0YowqC74SAzIUJ1u4rKcx_sB3rDFSl_4Y0vnVE4tHnDjawULvjJYTYckPgXD1kQ5SG0PPlQbQUL3WrMA0Q17nCFr6iryI2AgCW91dRwrFgnKLCNOzXyLS6Ge2stsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/1357" target="_blank">📅 04:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1356">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">خب با کمک دوست عزیزم Mr Arrow مشکل سرورلس (فرگمنت) هم تو نسخه
48
برطرف شد.
https://github.com/patterniha/Serverless-for-Iran
* نیازمند:
Xray-core >= 26.6.27
(v2rayNG >= 2.2.6)
* برای آپدیت کانفیگها کافیست سابسکریپشن را آپدیت کنید.
* نکات استفاده را حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/whitedns/1356" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1355">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">3 سرور اهدای CottenDNS
لطفا تست کنید و نتیجه رو بهمون بگید ( کلیک کنید روش کپی میشه )
Server #1 thx to Araskhatare
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imdlcm1hbnkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI5ODQ0NDhjZDRkZTYxZjgiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
Server #2 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InBhcmlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI1MjViNjkwYjU4ZmU0MTI0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #3 thx to Araskhatare
♥️
Location: Israel
🇮🇱
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HrvCfh7EgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyMjRiOWU4MjVlMzFkNWY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
@whitedns</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/whitedns/1355" target="_blank">📅 18:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1354">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/whitedns/1354" target="_blank">📅 13:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1353">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/whitedns/1353" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1348">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/whitedns/1348" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/whitedns/1348" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1347">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQZlQu2CeNOQjNmn8B2Lq-NPf3yBjc3hEJddq-fPCQdeUsoYFWAWAQMzqsCDqgig4r5qTI0qOzBUxve-uWW39tjNnFxvoarGyLJnur2vTrgDdFaRVYzHy9CRwzaPFoRaVqAEnMHV_QxzYd59XnJ29RDoGE8klSE8d5nT15aI2AKSVDc_iB8hOMS3sMltavMCAICl8cdCymr72bMsavJASTvpNdL5DjZnw5_OPPT3e9UlslHV2dOb5b8KXCzZp1CuAqrbZBCzXPTmYjg2h9jYdX90EIV9I5lx0omlhm94DvnwhbqzHmTU3SWF-XydG-U6psU2AMXH7VKkG_MGFxntyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/whitedns/1347" target="_blank">📅 10:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1346">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🌎
دوستانی که با جزئیات فنی پروژه آشنا نیستند، به زبان ساده
CottenDNS نسخه‌ای کامل‌تر و پیشرفته‌تر از پروژه‌های MasterDNS و StormDNS
است.
تیم ما طی چند ماه گذشته، با استفاده از تجربه‌هایی که از قطعی و اختلال گسترده اینترنت به دست آوردیم، روی توسعه و بهبود این پروژه کار کرده است تا اتصال پایدارتر و سازگاری بیشتری با شرایط مختلف شبکه داشته باشد.
نسخه جدید اپلیکیشن
WhiteDNS
که تا ساعاتی دیگر منتشر می‌شود، از سرورهای CottenDNS پشتیبانی خواهد کرد.
هم‌زمان با انتشار نسخه جدید، یک سرور عمومی CottenDNS نیز در اختیار شما قرار می‌دهیم تا بتوانید بدون نیاز به راه‌اندازی سرور شخصی از آن استفاده کنید.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1346" target="_blank">📅 10:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1345">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
معرفی پروژه CottenDNS
https://github.com/WhiteDNS/CottenDNS
نسخه پایدار CottenDNS با تمرکز بر اتصال بهتر و پایدارتر در شبکه‌های دارای فیلترینگ، اختلال DNS، پکت‌لاس و تأخیر بالا منتشر شد.
در معماری جدید، سرور به‌صورت پویا با تنظیمات هر کاربر هماهنگ می‌شود. یعنی کاربران می‌توانند بدون تغییر کانفیگ سرور، روش انتقال داده، نوع رمزنگاری، MTU، فشرده‌سازی و قابلیت‌های بازیابی بسته‌های ازدست‌رفته را متناسب با کیفیت اینترنت خود انتخاب کنند.
مهم‌ترین قابلیت‌ها
🔹
سازگاری با شرایط مختلف شبکه
اتصال می‌تواند از طریق UDP و TCP روی پورت 53 و همچنین DoT و DoH انجام شود. اگر یک مسیر مسدود یا دچار اختلال شود، کلاینت می‌تواند از مسیر جایگزین استفاده کند.
🔹
مقاومت بیشتر در برابر پکت‌لاس
CottenDNS با استفاده از ارسال مجدد هوشمند بسته‌ها، Duplication و فناوری FEC تلاش می‌کند اطلاعات ازدست‌رفته را بازیابی کند. این قابلیت‌ها بر اساس وضعیت شبکه به‌صورت خودکار فعال یا غیرفعال می‌شوند تا سربار اضافی ایجاد نشود.
🔹
مدیریت هوشمند Resolverها
Resolverها از نظر سرعت، تأخیر، پکت‌لاس و سلامت بررسی می‌شوند. Resolverهای خراب به‌صورت خودکار کنار گذاشته شده و پس از بهبود دوباره وارد چرخه می‌شوند.
🔹
تنظیم خودکار MTU
کلاینت اندازه مناسب بسته‌ها را برای آپلود و دانلود پیدا می‌کند تا احتمال شکسته‌شدن یا ازدست‌رفتن بسته‌ها کاهش پیدا کند.
🔹
مقابله با DNS Poisoning
با استفاده از روش‌هایی مانند Transaction ID تصادفی، EDNS Cookie، تغییر شکل درخواست‌های DNS و ارسال از چند دامنه مختلف، مقاومت اتصال در برابر پاسخ‌های جعلی و دست‌کاری‌شده افزایش یافته است.
🔹
انتقال داده با فرمت‌های مختلف DNS
داده‌ها می‌توانند با رکوردهای TXT، CNAME، A، NULL و HTTPS/SVCB منتقل شوند. کلاینت می‌تواند بسته به محدودیت شبکه بین این روش‌ها جابه‌جا شود.
🔹
امنیت و رمزنگاری
روش‌های AES-GCM، ChaCha20، XOR و الگوریتم‌های قابل تنظیم پشتیبانی می‌شوند. نوع رمزنگاری هر کلاینت به‌صورت امن و مستقل شناسایی می‌شود.
🔹
سازگاری با نسخه‌های قبلی
کلاینت‌های جدید CottenDNS و کلاینت‌های قدیمی MasterDNS و StormDNS می‌توانند هم‌زمان به یک سرور متصل شوند. بنابراین کاربران قدیمی برای ادامه استفاده نیازی به تغییر فوری ندارند.
در مجموع، سرور CottenDNS امکانات مختلف را فراهم می‌کند و هر کلاینت بر اساس شرایط اینترنت خود، بهترین ترکیب اتصال را انتخاب می‌کند.
❤️
Thanks to
@masterdnsvpn
@WhiteDNS</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1345" target="_blank">📅 10:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1344">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MbjrYtJ7r1Aw-9HlOWGqhHZ_aNpONhzZIMC0i47PsIH6LZgmqwcMeZNdXokz2Ozxe2JQBtzbqg_pDNCX4X45n0fFnjAU0t33pgUmZvRM7RfUsnJzD57ItVQDuEIAK5Rh27gPgYP79udJjVc-t0_hACczxOyESj-9DHGgaukoAcSDGOw5HFG1VStZpApW0C7hEjpqdYD8ctZYJ16_Xt8b4DzQ1Vdfz0rq0M1P9-CGih2FHnFZa3AqVDlDVUXUC55xL0k8wwIjrtcf2d2kW6-8fCObWmi4daxK7BpHyMdZhOiW5gyhDfeOJepGMUFIuwLkTQuqKS0OGhv9E66rSLsSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضویت
در گروه whitedns
در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/whitedns/1344" target="_blank">📅 09:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1339" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/whitedns/1339" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpnt4v2dMd0-u4p9s3Wx0GZlMZFhZrZ7NGBELm9Bmx6Np3FBaSZ5MmCWcMt4-7n08CyQfpu2pI7vEChEtYK6or_iWobW-ZqLCGCeYYEEt9HhLRxWqSBDrssibfWBhce1eazWw58EW8egIdQZUazJL_2iDe-zk5O5XpnLx43zGb4Apna9XR1nkmKKjnXJWe2dQzP2L7gJuIm5QMd-kM9hM78gJkkRd9dFWnSlf8rpmP2MAlJ15kXrt9RSat6PGggyt-hONEMKU5ikt5sOWrpvkGJo7IgkK14nKSHCph7LMHKBQxhzzM72usTJrxB6xzLPmBCPWCmj4YlNZLMfle4XMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/whitedns/1338" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1337">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OpgXUjTyaP1cmEHG1Wn42tPYUR9tzreAuXXccwMp5vnob2PBRbfkkvWBADe93cc8Z4BA6-j9FcQ82CxyhA_zM9loeXWK8o2I2OottdcV91FltlvS1dLiEZm9idzVt0hCTujERIuXVeSdJnxpNcwqkN-gUFTisWyXRcFHqoZDf3laNpaLUJnHak9IrsQyLUCA-KPsHCLnBA5ooqXSwohCYDwWc5LmdOGyBj4GpC7wTdwzyjuu8_CQ0rJzVPCBnC8i3jycjWdsy7jg9JiMs77O71poHJeRMzBP0ErVYNWRkbH6sBv3nyHsyyDUb-NxUoGVetAVtDOyHdjpgPeyY2Kj1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
👋
:
حالا همیشه هم پست برنامه و توضیح نگذاریم، بعضی وقتها یکم حرف بزنیم با هم، اینجا همه با هم داریم کار را جلو می‌بریم
🤝
✨
برای اینکه یک پروژه درست بشه ساعت‌ها وقت و هزینه صرف میشه تا به دست تو برسه
💸
⏳
، وقت و هزینه‌ای که میشد گذاشته نشه، زمانی که میشد در کنار دوست و خانواده بود و یا اصلاً رفت عشق و حال کرد
😔
💔
. اغلب دولوپرهای این تیم کلاً نیازی به بودن اینجا ندارند، فقط احساس دین می‌کنند
🙏
.
شما میتونی با لایک
👍
و دیس‌لایک
👎
، پروژه را تایید کنید یا ردش کنی و یا با قلب
❤️
حمایت کنی و ....
خطاب به اون چند نفر :
اینکه تو اینقدر بی‌شخصیت هستی که آیکن
🤮
می‌گذاری این فقط یک چیز را می‌رسونه، تو لیاقت این را نداری که کوچکترین خدماتی حتی با دریافت هزینه بهت داده بشه
🚫
🛠️
. تو همون کسی که اصلاً برات مهم نیست چی به مردمت می‌گذره، برات هیچی مهم نیست
🤷‍♂️
.
متاسفانه تو جرات نداری بیای توی گروه‌ها خودت را نشون بدی و بحث فنی کنی
💻
🛑
، والا تکلیف مشخص میشه.
یک تعداد زیادی از شماها که همراه ما هستند یکی از یکی خوب‌تر و مایه انرژی ما و بقیه هستید
🔥
⭐
، دلیل اینکه ادامه می‌دیم شماها هستید، والا کار ما خیلی وقت هست که تمام شد
🏁
.
ارادتمند
👋
ویسپر
🎤
تیم whitedns
🛡️</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1337" target="_blank">📅 08:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hbz2ZO6vBechavStBmAxFOATC3MSrHIXfRD0Z6aExgeytIo16IC2_XbpnjJ2MGgLB4xx4A8TVGBjWPo2qoYP5DiXOM1FjtAo_EohtPWy8ZxE13-Djb5t-UTU42PsVGpaHgTxDJURHnfG3U-6NehAkeXo6t8XvN3aaRIiAn8Xzbt8kuIR9nJyQKb75pJWeCiT8ki7kptfGObg7fL8KdFZI3qTl_N5LsZBb5U1xQjAoSTHpgRVis7qSKccTwYZWIXnu0KbA9fhaUEV3oyNqikqKuZl2AktXmFmiUgIFRts--GoK24I5UoK9iohBkSG_ciXNCqwT4CRmjU78U5pn2yh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Aether Desktop اومد! — آزادی، با یک لمس
🔥
بالاخره نسخهٔ ویندوزی Aether رسید!
🎉
همون اپ محبوب اندرویدی، حالا روی ویندوز — با همون ظاهر، همون آیکون و همون هستهٔ قدرتمند. نسخهٔ 1.0.0 اولین انتشار دسکتاپه و هیچی از نسخهٔ اندروید کم نداره!
✨
چی داره؟
🔌
اتصال قدرتمند:
▫️
۴ پروتکل: Smart (انتخاب خودکار) · MASQUE · WireGuard · WARP×2
▫️
۵ حالت اسکن: از Turbo تا Ironclad
▫️
اتصال مجدد خودکار تا ۵ بار + انتخاب هوشمند پروتکل اگه یکی جواب نداد
▫️
پشتیبانی IPv4، IPv6 یا هر دو باهم
▫️
نمایش زندهٔ سرعت، پینگ، سرور و IP با پرچم کشور
🏳️
🎨
رابط کاربری خیره کننده و زیبا :
▫️
کاملاً دوزبانه (فارسی و انگلیسی) با پشتیبانی کامل راست‌به‌چپ
▫️
تم تیره با طراحی دقیقاً مثل موبایل، بهینه برای مانیتورهای بزرگ
▫️
نوار عنوان به سبک ویندوز ۱۱
⚙️
تنظیمات پیشرفته:
▫️
نویز (از سبک تا تهاجمی و GFW) · MTU دلخواه · Fragment · ECH
▫️
تونل تفکیکی (Split Tunneling) — انتخاب کن کدوم برنامه‌ها از تونل رد بشن
📡
اشتراک با بقیه دستگاه‌ها:
▫️
SOCKS5 روی پورت 10810 و HTTP روی 10811
▫️
هر دو پورت خودکار پروتکل رو تشخیص می‌دن — هر کدومو هرجا بزنی کار می‌کنه!
🛠
عیب‌یابی حرفه‌ای:
▫️
تست زندهٔ اتصال + بررسی ۶ موردی محیط سیستم
▫️
کنسول لاگ زنده و رنگی با دکمهٔ کپی
🪟
مخصوص ویندوز:
▫️
تونل واقعی سطح سیستم با درایور رسمی و امضاشدهٔ مایکروسافت (Wintun)
▫️
پروکسی سیستمی خودکار تنظیم می‌شه و موقع قطع، برمی‌گرده سر جاش
▫️
نیازی به Visual C++ نداره؛ WebView2 هم نبود، خودش نصبش می‌کنه
📦
دانلود:
▫️
نصب‌کنندهٔ گرافیکی برای ویندوز ۶۴ و ۳۲ بیتی
▫️
نسخهٔ پرتابل بدون نصب — هیچ ردی روی سیستم نمی‌ذاره!
👌
▫️
فایل SHA256 برای راستی‌آزمایی سلامت فایل‌ها
⚡️
ساخته‌شده با Rust + Tauri 2 — یعنی حجم نصب فقط چند مگابایته، نه ۱۰۰ مگ مثل اپ‌های Electron! کل بیلد و انتشار هم صددرصد خودکار با GitHub Actions انجام می‌شه، بدون هیچ دخالت دستی.
📋
پیش‌نیاز: ویندوز ۱۰ (نسخهٔ ۱۸۰۹ به بالا) + دسترسی Administrator برای ساخت آداپتور شبکه
📄
لایسنس: MIT — کاملاً متن‌باز و رایگان
💙
⬇️
همین الان از بخش Releases گیت‌هاب دانلود کن و آزادی رو با یک کلیک تجربه کن!
📥
دانلود مستقیم از گیت هاب
https://github.com/QW-AI-Code/Aether_Desktop/releases/
سلام دوستان عزیز
✋
یه یادآوری مهم که حتماً بخونیدش
👇
برای اینکه اپ (چه نسخه اندروید چه ویندوز) براتون وصل شه، این چند تا نکته رو رعایت کنید تا بهترین نتیجه رو بگیرید:
⏳
رو هر پروتکل ۱ تا ۳ دقیقه صبر کنید تا وصل شه. بسته به اپراتور و منطقه‌تون این زمان فرق می‌کنه، عجله نکنید.
🔄
پروتکل‌ها و تنظیمات مختلف رو تست کنید. چرا؟ چون DPI هر سیم‌کارت با سیم‌کارت دیگه، هر منطقه با منطقه دیگه و هر شهر با شهر دیگه فرق داره.
📱
اگه با موبایل وصل نشدید: چند بار گوشی رو ببرید رو حالت هواپیما و برگردونید تا رنج آی‌پی‌تون عوض شه، بعد دوباره پروتکل‌های مختلف رو تست کنید. خلاصه باید قلق DPI اپراتور و منطقه خودتون دستتون بیاد
😉
📶
اگه با وای‌فای هستید: مودم رو ۱ تا ۲ دقیقه خاموش کنید تا رنج آی‌پی عوض شه، بعد دوباره با پروتکل‌ها و تنظیمات مختلف امتحان کنید.
❌
اگه بازم وصل نشد، یعنی این وی‌پی‌ان با نت شما جواب نمی‌ده و باید برید سراغ وی‌پی‌انی که با نت شما سازگاره.
⚠️
و نکته آخر: بعضی از کاربرا میگن این اپ مشکل داره و واسشون کار نمیکنه.
اگه مشکل از خود اپ بود، نباید برای هیچ‌کس کار می‌کرد! همونطور که می‌دونید برای خیلی‌ها داره کار می‌کنه و هر کسی تجربه متفاوتی داره.
پس اگه برای شما وصل نمی‌شه، مشکل از Aether نیست؛ مشکل از DPIایه که رو اپراتور شماست و جلوی کار کردن اپ رو می‌گیره.
#VPN
#فیلترشکن
#Aether
#ویندوز
#متن_باز</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1335" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8d366d7.mp4?token=XGfAD9cJ2FZzpk5jKUTuxZ_wYqDfYYz3Kiy8Zhwm09ehw5Bc1jicsmg5eU11r_YHjFFMtU16HSKgh0lxVyL3bdF625hHvjP_3cvmJTVVVW7ef36dVUE95KqoQKku8clF5m3EQduY1r7aJG-SM9kLoh12cO1sjQKfmac3SC0yh_8m8HQCyJdKGU8igHZG9NB92qU4cIJodBSezFqP4k_9Hp-4YH-kclNoUf4fCwFEaHXnTG2n-ts6jRJpf_iGnFJOA72-H1jSc2l2ZyNitlbwKV36NWpm6XVH_A57pzUOgVknkohY78TSFuqm-pkSEdcdL3TcrN07qsDBJzK7gvOAYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8d366d7.mp4?token=XGfAD9cJ2FZzpk5jKUTuxZ_wYqDfYYz3Kiy8Zhwm09ehw5Bc1jicsmg5eU11r_YHjFFMtU16HSKgh0lxVyL3bdF625hHvjP_3cvmJTVVVW7ef36dVUE95KqoQKku8clF5m3EQduY1r7aJG-SM9kLoh12cO1sjQKfmac3SC0yh_8m8HQCyJdKGU8igHZG9NB92qU4cIJodBSezFqP4k_9Hp-4YH-kclNoUf4fCwFEaHXnTG2n-ts6jRJpf_iGnFJOA72-H1jSc2l2ZyNitlbwKV36NWpm6XVH_A57pzUOgVknkohY78TSFuqm-pkSEdcdL3TcrN07qsDBJzK7gvOAYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">UAC SNI Spoofer Desktop
نسخه 1.0.6
━━━━━━━━━━━━━━━━━━
تغییرات جدید نسخه 1.0.6
• قابلیت Mobile Gateway اضافه شد. دستگاه‌های متصل به شبکه وای‌فای مشترک می‌توانند بدون تغییر تنظیمات Proxy، IP یا DHCP از VPN کامپیوتر استفاده کنند.
• امکان پینگ‌گرفتن از کانفیگ‌های موجود در تب Configs و مرتب‌سازی آن‌ها براساس کمترین پینگ یا کشور اضافه شد.
• باگ‌های جزئی بخش SNI Config Maker برطرف شدند. اکنون کانفیگ‌های بیشتری از مخازن شناسایی، دریافت و پردازش می‌شوند.
• مشکل فعال‌نشدن دستی کانفیگ‌ها، به‌خصوص هنگام استفاده از Auto Mode، برطرف شد.
━━━━━━━━━━━━━━━━━━
لینک دریافت نسخه 1.0.6:
https://github.com/Floxu1/UAC-SNI-Spoofer-Windows/releases/tag/1.0.6
لینک گیت‌هاب پروژه:
https://github.com/Floxu1/UAC-SNI-Spoofer-Windows
t.me/UacSniSpoofer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1334" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌎
نسخه جدید WhiteVPN 1.1.0 منتشر شد!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1333" target="_blank">📅 17:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1328">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/whitedns/1328" target="_blank">📅 17:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1327">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJA3a2-_eIITdyPhVvX3jlHIWM_wLfjbIOkajad7eXdaMGgYTw7a-1CyQ3MpwulndKwia3yNoWYkA2Cq7xUWP84b4V9dXNOqK8V_m_UOdhyKXGsecF5hCOas5nIjN_ynAHWm0oPTKk-tixWeIZCf1AUcyoTJHGAqjJMiAnCnbBGqpFeT6UT0yH1fSuezTEUuS9M9-wp5GYJIterMMhRgx6tsqIY4sSJ2kSwl-ojRzk29by32p9Du4X2gwYjud6IunphrksEpl73OP7ZBeQXhXeAWYp_xyymu2_fqY7mjUKhC8ZBGEnzXJcAWG_R4Z5QFs3JlM2BgxkIXj7L-l5_KFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/whitedns/1327" target="_blank">📅 17:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1326">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AYjQnkEgWNT6E7VnP831uErgLJQyJfS-3nld53goK5XrgQ49QA4ZTdZ6orb2dgb7lEiup6-Dtubc1jKESZuIAHvyyFNOf6kPAHgL_JQLcn4u8Nx_p68jHBGRMN6oFg4peTZAV9tPaLLvbc0lJRCm5Zkn76I8l-yj2XpMqW2zvUFFolUd4cL2zMhJEgYvPyZSKbZh7BTuKqVUfo--mcI0cBkkwUZG7b7UGwa8YHWjJPoPoDQweU6MEZW6h5Bxudjgu1WlUuUgWQjUIo7zuZMQIZsqebyUGodudHz4cIJ7-DaAm9T1KWIw1EwiEME5XR_ubMtuyovnIRF1oE0L7Nxqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1326" target="_blank">📅 10:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1325">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-poll">
<h4>📊 از چه دستگاهی استفاده میکنید ؟</h4>
<ul>
<li>✓ اندروید</li>
<li>✓ اپل</li>
<li>✓ مک</li>
<li>✓ ویندوز</li>
<li>✓ لینوکس</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1325" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1324">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WDCOVFOtQgnCwwK1uTt4bPK0spdyZwdkNgEnpLcJf3qzuo_HgKQdNAKgE2km2h7EKrcoPBvgRY2HadEAcxuV7ro6iCSCfvj3ewRulCxwOU7UXdmTwQ78_q4_gCKfwM1T0qmm3QN0BUqh1X2kxennBPDNb7x_u3VIVQ0bmKt-h30JmAQ4S6YIoW6utQgo1zUuxe2iHTnQwZS0Y0v2U4d5z8y9lvrLAjvRM7rdfEprqBoAOgxpssXPI4zvjG0jHUCYySvmLeIJGdnv8dOWZ2rNNXeemTzwN6k2uRI10OTdQVuf9fN7t2VfVGRypHdbkBseHEL6gcFV4DUeLZ01DJYtVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1324" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1323">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستان عزیز، اونایی که Aether واسشون وصل نمیشه، یه زحمت کوچیک بکشید:
📱
✈️
چند بار گوشی رو بگذارید روی حالت هواپیما و بردارید تا رنج IP‌تون عوض بشه.
🔄
اونایی هم که با وای‌فای و مودم متصلن، مودم رو ۱ تا ۲ دقیقه خاموش‌روشن کنن تا آی‌پیشون تغییر کنه.
🔌
⏳
اینم یادتون نره که ما تو ایرانیم؛ سیستم DPI و محدودیت‌ها روی هر سیم‌کارت با اون یکی فرق داره، چه برسه به منطقه به منطقه و شهر به شهر!
🇮🇷
🚫
اینجا خبری از اینترنت استیبلِ خارج نیست.
📉
اگه این کارا رو کردید و پروتکل‌های مختلف رو هم تست زدید و باز هم وصل نشد، یعنی اون کانفیگ کلاً روی خط و منطقه شما جواب نمیده.
🛑
یکی دو ساعت بعد دوباره امتحان کنید یا برید سراغ VPN‌های دیگه که با اپراتور و منطقه‌تون سازگارترن.
🚀
🌐</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1323" target="_blank">📅 12:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1322">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-poll">
<h4>📊 با این لینک موفق شدید عضو بشید ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-text">عضویت در گروه whitedns  در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1322" target="_blank">📅 12:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1321">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1321" target="_blank">📅 11:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1320">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hNu5XRS5DGjHXpoxGkgprUagpKOnLAu4NFAv87F1DGnThWOASouGIJCkaQZtLQR0HifN0NStPaM3noohAaeVK-8a3CufYdYq-VXBdA3zmTqRwIXrJ21V8vk02B76U9LgsBKKThRE-m6pL1wCwgiXvRVbYDwqzmLR_X-GAegEDXAnCw_yKXepgz_PkrLFNKWY-9fjrFJbojuFEqQ9kw5gc-Pby1CT0Vo7wJ8WsxDXoZm8GHS1bzUJUk-ohPTgPqDrN0FChcb1apYdbKgox22Hzhwdo4vLBRp9tk6cdYQ4hXGxtssWxlJaQfSbuKPJj7rlhokUfBomlIIxVlncxf0SUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضویت
در گروه whitedns
در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/whitedns/1320" target="_blank">📅 11:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1317">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Aether 1.2.2</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/whitedns/1317" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1316">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سلام دوستان عزیز.
راستش ما قبل از اینکه بخواهیم نسخهٔ جدید ۱.۲.۲ پروژه اِتر (Aether) را منتشر کنیم، ۱ روز گذشته را کاملاً درگیر تست، آزمون و خطا و چالش‌های فنی بودیم. خیلی از کاربران از ما خواسته بودند که قابلیت انتخاب کشور را اضافه کنیم و خودمان هم خیلی دوست داشتیم این کار را بکنیم؛ اما بعد از کلی کلنجار رفتن و تست‌های مختلف روی اپراتورهای مختلف، متوجه شدیم که با توجه به ماهیت فنی این کار، عملاً چنین چیزی نشدنی است.
برای همین تصمیم گرفتیم خیلی روراست و خودمانی با شما صحبت کنیم و بگوییم توی این مسیر آزمون و خطا به چه چیزهایی رسیدیم:
### ۱. چرا در پروژه اِتر (Aether) نمی‌شود کشور خاصی را انتخاب کرد؟
پروژه اِتر (Aether) سرور شخصی و اختصاصی ندارد و کارش این است که شما را به شبکهٔ عظیم WARP کلاودفلر (همان شبکهٔ معروف
1.1.1.1
) وصل کند.
بزرگ‌ترین مانع ما در تست‌ها یک مسئلهٔ فنی بود: آدرس‌های کلاودفلر از نوع Anycast هستند. انی‌کست یعنی چه؟ یعنی یک آدرس مشخص، هم‌زمان در صدها دیتاسنتر در سراسر دنیا فعال است.
یک مثال ساده بزنم؛ شمارهٔ ۱۲۵ آتش‌نشانی را در نظر بگیرید. شما هر جای ایران که باشید این شماره را بگیرید، به آتش‌نشانی شهر خودتان وصل می‌شوید، نه تهران یا یک شهر دیگر! حتی اگر عمداً بخواهید به آتش‌نشانی شیراز زنگ بزنید، باز هم شمارهٔ ۱۲۵ شما را به نزدیک‌ترین ایستگاهِ خودتان وصل می‌کند.
آدرس‌های WARP هم دقیقاً همین‌طور کار می‌کنند. پروژه اِتر (Aether) به هر آدرسی که وصل شود، در نهایت این سیستمِ مسیریابیِ اینترنتِ اپراتور شماست که تصمیم می‌گیرد ترافیک به کدام دیتاسنتر برود.
*   وقتی اوضاع اینترنت خوب باشد، معمولاً نزدیک‌ترین نقطه جواب می‌دهد.
*   وقتی مسیرهای بین‌المللی شلوغ یا خراب باشد، سیستم شما را می‌فرستد سمت آلمان (فرانکفورت)، آذربایجان (باکو)، ایتالیا (میلان) یا هر جای دیگر.
توی بررسی‌هایی که قبل از انتشار نسخهٔ جدید داشتیم، دیدیم وقتی مثلاً لوکیشن روی «اتریش» تنظیم می‌شد، پرچم اتریش نشان داده می‌شد، اما خروجی واقعی اینترنت کاربر یک کشور دیگر بود! در واقع آن منوی کشورها فقط یک برچسب تزیینی و قشنگ بود، نه یک انتخاب واقعی. ما هم چون دوست نداشتیم توی پروژه اِتر (Aether) ظاهرنمایی کنیم یا آمار دروغین به کاربر نشان بدهیم، کلاً حذفش کردیم تا همه‌چیز واقعی و شفاف باشد.
---
### ۲. چرا ویژگی «اتصال فقط به لوکیشن‌های غیر از ایران» را اضافه نکردیم؟
شاید باورتان نشود ولی ما این قابلیت را واقعاً کدنویسی کردیم و قبل از نهایی کردن نسخهٔ جدید، آن را زیر تست بردیم. اما خروجی کار روی اینترنت ایران اصلاً خوب نبود!
منطق کار این بود: پروژه اِتر (Aether) وصل شود، آی‌پی خروجی را چک کند، اگر ایران بود قطع کند و برود سراغ آدرس بعدی. اما مشکل بزرگ کجا بود؟
وقتی اپراتور شما مسیرهای خارجی را محدود یا فیلتر می‌کند، تقریباً تمام آدرس‌های کلاودفلر به دیتاسنترهای داخل ایران هدایت می‌شوند. در این حالت، پروژه اِتر (Aether) یکی‌یکی آدرس‌ها را تست می‌کرد، چون خروجی‌شان ایران بود قطع می‌کرد، سراغ بعدی می‌رفت و در نهایت بعد از کلی معطلی می‌گفت: «اتصال ناموفق». یعنی عملاً به‌جای یک اینترنتِ وصل‌شده (ولو با آی‌پی ایران)، شما کلاً قطع می‌شدید! درست مثل کسی که چون فقط سوار تاکسی سفید می‌شود، تا صبح گوشهٔ خیابان در سرما می‌ماند!
تازه یک مشکل دیگر هم هست؛ سرویس‌های تشخیص لوکیشنِ آی‌پی همیشه دقیق نیستند. خیلی وقت‌ها یک اتصال کاملاً سالم و خارجی را به اشتباه «ایران» تشخیص می‌دادند و پروژه بی‌دلیل آن را قطع می‌کرد. به همین خاطر در آزمون و خطاهای قبل از انتشار متوجه شدیم وجود این گزینه فقط باعث خرابی اتصال و اعصاب‌خردکنی کاربران می‌شود.
---
### ۳. پس الان پروژه اِتر (Aether) دقیقاً چه‌کار می‌کند؟
ما در این نسخه همه‌چیز را هوشمند کردیم. حالا هستهٔ پروژه اِتر (Aether) در چند ثانیه کل رنج‌های WARP را اسکن و پینگ می‌کند و به بهترین، سریع‌ترین و پایدارترین نقطه‌ای که در آن لحظه روی خط شما جواب بدهد وصل می‌شود؛ بدون قطع و وصلی‌های الکی.
البته اگر کاربر حرفه‌ای هستید و دوست دارید خودتان دستی همه‌چیز را تنظیم کنید، هنوز هم می‌توانید از بخش تنظیمات، اندپوینت دستی یا رنج آی‌پی دلخواه خودتان را وارد کنید.
یک نکتهٔ بسیار مهم برای آرامش خیال شما:
خیلی از کاربرها نگران هستند که اگر آی‌پی خروجی ایران باشد، امنیتشان به خطر می‌افتد. اصلاً این‌طور نیست! حتی وقتی نقطهٔ اتصال شما داخل ایران باشد، تمام ترافیک و داده‌های شما کاملاً رمزنگاری‌شده است. مقصد نهایی این ترافیک، شبکهٔ جهانی کلاودفلر است و هیچ‌کس در این مسیر نمی‌تواند اطلاعات شما را بخواند یا ببیند چه کار می‌کنید.
آن نقطهٔ ایران، فقط و فقط مثل یک «درِ ورودیِ» امن به اتوبانِ کلاودفلر است، نه جایی که اطلاعات شما در آن تخلیه شود. پس اصلاً نگران امنیت خود نباشید.
---
###
💡
حالا چطور آی‌پی خود را به خارج از ایران تغییر دهیم؟ (دو راهکار عملی)
اگر به هر دلیلی نیاز دارید که آی‌پی خروجی شما حتماً روی کشوری غیر از ایران قرار بگیرد، در حال حاضر دو تا راهکار کاملاً واقعی و تست‌شده برایتان داریم که می‌توانید از آن‌ها استفاده کنید:
*   راهکار اول (سوئیچ بین پروتکل‌ها): تنها راه طبیعی برای تغییر آی‌پی این است که داخل تنظیمات پروژه اِتر (Aether)، بین پروتکل‌های مختلف سوئیچ کنید. در این میان، پروتکل وارپ (WARP) بیشترین احتمال را دارد که شما را به یک سرور غیر از ایران متصل کند. این تغییر پروتکل باعث می‌شود روتینگ اینترنت شما عوض شده و در نهایت به یک دیتاسنتر خارجی هدایت شوید.
*   راهکار دوم (ترکیب با سایفون): شما می‌توانید از قابلیت «حالت پروکسی» (Proxy Mode) در پروژه اِتر (Aether) استفاده کنید و آن را با برنامه سایفون (Psiphon) زنجیره یا ترکیب کنید. با این روش، ترافیک شما از تونل پروژه اِتر (Aether) رد شده و در نهایت با آی‌پی خارجی سایفون خارج می‌شود که تضمین می‌کند آی‌پی شما به غیر از ایران تغییر خواهد کرد.
@whitedns</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1316" target="_blank">📅 10:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1315">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dWkCMg43z7tRsfmkcMZcMw-Lrfn0as6OIcMJioyuOVr-oFt0GXDh8Pisk8hqqsa3D71oeqkxR6JHQ7L5x8u7FKaDxygZsCEOsUSbyWOLwzTpQVOrCDsCeP_oB8a70iCFcYrGyWssZnmHpCtuJXEHMRLWfFsaPNv6AuWMAxiqRDS-5g9t8Z9mY1rUVoPVZDe_zw94eFhc0S6GJ-g2rb8MPT9cCgQBqi0WHoAoCWOwtHSI7DUidE0ZVId__s8xcgghIqkXTCdS3ZlE64sEelJB_xNSG23OstQkivjRmKRQA-slFmW5FVRY6-g7GNN5xOpl2iIEyl3heL_5VVjBhngKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
تازه‌های نسخهٔ ۱.۲.۲ کلاینت موبایل Aether
🚀
یک به‌روزرسانی بزرگ و بنیادین با تمرکز بر امنیت حداکثری، کاهش شدید مصرف منابع سخت‌افزاری و ثبات اتصال منتشر شد! در ادامه خلاصه تغییرات این نسخه را برای شما آماده کرده‌ایم:
🔄
۱. مدیریت خودکار و ارتقای هسته (Core)
ارتقا به نسخه پایدار ۱.۴: هسته تانل داخلی برنامه به آخرین نسخه پایدار ارتقا یافت.
خودکارسازی در CI/CD: فرآیند همگام‌سازی و اعمال پچ‌های اختصاصی اسکن رنج به صورت کاملاً خودکار و هوشمند در خط‌لوله بیلد گیت‌هاب پیاده‌سازی شد تا از بروز کوچک‌ترین ناسازگاری یا خرابی در فایل‌های نهایی جلوگیری شود.
🗑
۲. حذف کامل سیستم به‌روزرسانی درون‌برنامه‌ای (ارتقای امنیت)
افزایش شفافیت و امنیت: بخش دانلود خودکار درون‌برنامه‌ای به همراه دسترسی‌های پرخطری مانند REQUEST_INSTALL_PACKAGES کاملاً حذف شد.
دلیل فنی: برای اطمینان از اصالت کدها و عدم نصب ناخواسته فایل از منابع ناشناس، از این پس تمامی آپدیت‌ها صرفاً به صورت رسمی و امضاشده فقط از صفحه ریلیس گیت‌هاب پروژه قابل دریافت خواهند بود.
🌐
۳. حذف لوکیشن‌های فیک و واگذاری اتصال به هسته هوشمند
حذف منوی انتخاب کشور: از آنجا که شبکه WARP کلاودفلر از آدرس‌های Anycast استفاده می‌کند، انتخاب لوکیشن در کلاینت عملاً تزئینی بود.
اتصال هوشمند واقعی: در این نسخه منوی لوکیشن حذف شده و وظیفه اسکن رنج‌ها و انتخاب بهترین و نزدیک‌ترین لبه ارتباطی (با کمترین پینگ و پایدارترین حالت) به صورت پویا به خود هسته برنامه واگذار شده است.
⚡️
۴. کاهش مصرف رم، پردازنده و بهینه‌سازی رابط کاربری (UI)
کاهش مصرف CPU در حالت آماده‌باش (Idle): تغییر ساختار مانیتورینگ اتصال از حالت Polling به حالت Blocking روی پروسه هسته که باعث می‌شود پردازنده گوشی در زمان اتصال بدون ترافیک، به خواب عمیق برود.
حل نشت حافظه (Memory Leak): محدود شدن حجم لاگ‌های ارتباطی به یک بافر حلقوی ۸۰۰ خطی (حداکثر ۵۱۲ کیلوبایت) جهت جلوگیری از مصرف بی‌رویه رم در اتصال‌های طولانی.
رابط کاربری روان‌تر و سریع‌تر: حذف انیمیشن سنگین شفق قطبی (Aurora) در پس‌زمینه و جایگزینی با رنگ ساده ساکن که بار پردازش گرافیکی گوشی را به صفر می‌رساند. همچنین منوی تنظیمات پیشرفته اکنون بدون کوچک‌ترین لگی فوراً باز می‌شود.
🔌
۵. رفع تداخل با v2rayNG و حل مشکل نصب (Over-Install)
تغییر پورت‌های پیش‌فرض: پورت‌های اشتراک‌گذاری شبکه محلی Aether به 10810/10811 تغییر یافت تا با پورت‌های پیش‌فرض v2rayNG تداخل نداشته باشند. همچنین سیستم شناسایی هوشمند ابزارهای موازی اضافه شده است.
حل دائمی مشکل امضای دیجیتال: گواهی امضای اندروید در بخش بیلد تثبیت شد؛ کاربران نسخه ۱.۲.۱ می‌توانند بدون نیاز به حذف برنامه قبلی، نسخه جدید ۱.۲.۲ را مستقیماً روی گوشی خود نصب کنند و تمام تنظیماتشان حفظ خواهد شد.
🔒
۶. ممیزی امنیتی ۱۰۰ درصدی خط‌به‌خط
کد منبع برنامه تحت ممیزی سخت‌گیرانه قرار گرفت و از نظر مواردی همچون اطلاعات هاردکدشده، نشت DNS/IPv6، ذخیره‌سازی محلی ناامن و ترافیک رمزنگاری‌نشده کاملاً پاک‌سازی شد.
📥
هم‌اکنون نسخه ۱.۲.۲ را به صورت رسمی و امضاشده دانلود کنید:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/whitedns/1315" target="_blank">📅 10:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1314">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-railway.txt</div>
  <div class="tg-doc-extra">168 B</div>
</div>
<a href="https://t.me/whitedns/1314" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک‌های استفاده شده در ویدئوی بالا</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1314" target="_blank">📅 04:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1313">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KZ3u8pcXTRS8E_t8jDPoJqxCYLjK5qlZ6GgCEVhMUcmVbtlxLMeGt0YDbGnBVQv-0_G2olqg9NS2gyisJ2c9x6fPYPtI0yn9Dj_UQO2nB-PU8K3AUZ6wEqP09P5E0fvCTII7k1fhm79M_A25eLr21qECWIZ5Yj33mK0a9cZXVpG4o-5Sk5vsrFfSeXsVJgxOePf7FSdyPymAPgABTDMoU2QFoCRagfakf2RzcyormiqC-tAxNPQvY46kgUx5NxSgp52NvS34vIOaJAkKYtqGfpuEw7w7ErHlGDHNJ6wbfCNkwUG1ZsjjvWW_DK-n99gbreioKU9FdEVJf4cgWJpsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
هرمس رو با گوشی موبایل روی VPS رایگان و تلگرام اجرا کن! + آموزش بکاپ کامل از Hermes
⚡️
دستورات نصب استفاده شده در این ویدئو:
https://t.me/MatinSenPaii/4683
⭐️
توی این ویدئو:
1- بهتون یاد میدم چه شکلی با گوشی آیفون/اندروید/لپ‌تاپ، هم Hermes و هم 9Router رو به رایگان روی سرورهای Railway بالا بیارید.
2- وصلش می‌کنیم به تلگرام و از مدل Mimo رایگان روی OpenCode استفاده می‌کنیم و API 9Router رو ست می‌کنیم.
3- به طور کامل بهتون یاد میدم که چه شکلی می‌تونید از اکانت گیتهابتون استفاده کنید تا Hermes رو بهش وصل کنید و به راحتی، هر چند ساعت یک بار از تمام داده‌هاش برای شما بکاپ بگیره.
4- به علاوه روش ایرانیزه شده‌ی استفاده نامحدود از کردیت رایگان 5 دلاری Railway
😂
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api و سرور رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1313" target="_blank">📅 04:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1312">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سرور های اهدایی و فعال WhiteDNS پارت ۲ داشته باشید برای زمان قطعی (کلیک کنید روش کپی میشه)
Server #11 thx to Araskhatare
♥️
Location: Germany
🇩🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6nwn4eqIDIgICB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiZGUuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI0OWUzNDlhNDc2NjQyYTg4ZTQ2NDVmYTJiZjgwZjhjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #12 thx to Araskhatare
♥️
Location: Israel
🇮🇱
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4exICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI2MmIyNjQ0NzU5MjU4OWE0NmQ1MzdlY2M5NDc3MzY2NiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1312" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">10 سرور اهدایی و فعال WhiteDNS داشته باشید برای زمان قطعی (کلیک کنید روش کپی میشه)
Server #1 thx to Coreforge
♥️
Location: Turkey
🇹🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7nwn4e3ICAgdGh4IHRvIENvcmVmb3JnZSIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFub255bW91cy5vYnNlcnZlciIsImVuY3J5cHRpb25fa2V5IjoiYjI3NTAzOTE5OWIxYzhjOSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #2 thx to Araskhatare
♥️
Location: Germany
🇩🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6nwn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI5ZGIxNjYwMmM4Yzc3NjcxOWJhZDE3ZWZjOWQxM2E0NCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #3 thx to Araskhatare
♥️
Location: USA
🇺🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7rwn4e4ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6ImVkMGNlZjE2YjcxNTNiOGQ4MzVhMzI3ODYxNTk3YzY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #4 thx to Araskhatare
♥️
Location: France
🇫🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6vwn4e3ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImIuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyZjAyZTNiN2NiNTg3ZjM4M2U0MWM0MmU4ZWYzYWY2MSIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #5 thx to Araskhatare
♥️
Location: UK
🇬🇧
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6zwn4enICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJkYmYwMmYyYWVmZmQzM2QyNDY0M2ViODM4OGY2N2Y0ZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #6 thx to Araskhatare
♥️
Location: Ireland
🇮🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjY0MTVlYjhmOTBmMWQ0NjY1N2JjZTljYjc5MTg2NDY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #7 thx to Araskhatare
♥️
Location: Sweden
🇸🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7jwn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InEuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjFkYjFiMWIyNGM2N2IxNzYwOTAzMmNjNDdhZmRhMzZlIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #8 thx to Araskhatare
♥️
Location: Spain
🇪🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6rwn4e4ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Im4uYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjU4MTcyOTA4ZGFhNTAxZTk0MjUzNWU2NTY3NzkwM2ZkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #9 thx to Araskhatare
♥️
Location: Italy
🇮🇹
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4e5ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imx5LmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJkMzM4NmM1MzkxZmRmOTJjMmNkODM3YmFkZTBhNGVjYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #10 thx to Araskhatare
♥️
Location: Brazil
🇧🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6fwn4e3ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlsLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJmNzk4MDAyYzlkMTkxMTg4M2MzOTE2YTQ4ZTkzNTVkMiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1311" target="_blank">📅 22:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1307">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162866f874.mp4?token=ktEswwd8MF0uw3ocrWSqvW77eQMBTR85HGVr9eC6KY3uvon2CQ4eQrMgHsN8JJ3AEgNTKtjjrkS3IAoj1euhPHH4UAfWRMUdqvvdhc_HJECQ3eCLwwx_7ZPTdU7kdZi8V6DHoz-u8JYOcgzGoXpicdnji9L0owYB4cdJxZdB9fPM9MHV22oUSCW6NEkB1uFuSszVSMkk0J1GVNgzKLo1mBAA2es5r8dZOwHo1-Qt1m3ir1qgZKaRNiEGkihQLWtlKKdhdth3JDdgc_fFpH7AOveYEqt-yMhuunmglejulCcgCsfFXSlG2NUBlvFkOm91fkLvlQFFFBI85R7EPX3b6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162866f874.mp4?token=ktEswwd8MF0uw3ocrWSqvW77eQMBTR85HGVr9eC6KY3uvon2CQ4eQrMgHsN8JJ3AEgNTKtjjrkS3IAoj1euhPHH4UAfWRMUdqvvdhc_HJECQ3eCLwwx_7ZPTdU7kdZi8V6DHoz-u8JYOcgzGoXpicdnji9L0owYB4cdJxZdB9fPM9MHV22oUSCW6NEkB1uFuSszVSMkk0J1GVNgzKLo1mBAA2es5r8dZOwHo1-Qt1m3ir1qgZKaRNiEGkihQLWtlKKdhdth3JDdgc_fFpH7AOveYEqt-yMhuunmglejulCcgCsfFXSlG2NUBlvFkOm91fkLvlQFFFBI85R7EPX3b6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش وصل شدن به این روش شیر و خورشید در Mahsang دوستانی که بلد نیستند.
1-اول به داخل mahsang برید
2-سه خط سمت چپ رو بزنید
3-قسمت تنظیمات سایفون رو پیدا کنید
4-پروتوکل روی cdn fronting قرار بدید(دکمه ذخیره یا سیو رو بزنید حتما)
5-برگرید صفحه اصلی گزینه F رو بزنید
6-حالت فقط سایفون/only pisphon رو بزنید و دکمه کانکت و تمام
حالا شما رایگان و با سرعت بدون نیاز به پیدا کردن ip به اینترنت آزاد متصل میشید
🔛
لینک دانلود نسخه جدید
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1307" target="_blank">📅 07:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MXEvCgP77gSvGLPE0YbGFZHYuZGL1TqYzyfSo0Zissywm-_7a-_HazuIyldA5v43hJ6KKYoiz6MVpiKChFMkf7cKVHJC0RiQjIKxnjrf4IC1Zt5zN4vgii4p1w_x9qzQCSyOl-DWSQoDQ7YRus2b_Yr4F79pHXvDu-Oi0dtU1hPkXB5SKe5IM-PMct3fbcdWypEKw3itwqbEQ04Kjqu3X85pY6L7n__rbkGwidrI9mBnHRUD8-ingxsFPBGNlQqU3fPAAHnkIXiIES1H1IdynMmjLoTS7DAX6M7KlpRKBAvMSh0EkKoyfml9b4cHP2uIxikTuhcko243RZPjlQQCBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1304" target="_blank">📅 05:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1299">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📱
آموزش کامل اپلیکیشن WhiteDNS منتشر شد
سلام به همه دوستان عزیز
یک ویدیوی آموزشی کامل برای استفاده از اپلیکیشن WhiteDNS آماده کرده‌ایم. در این ویدیو، تمام مراحل از نصب و راه‌اندازی اولیه تا اتصال و استفاده صحیح از برنامه، قدم‌به‌قدم توضیح داده شده است.
در این آموزش با موارد زیر آشنا می‌شوید:
• نصب و راه‌اندازی اولیه WhiteDNS
• اضافه‌کردن و مدیریت Resolverها
• اسکن و پیدا کردن Resolverهای معتبر
• تفاوت حالت پروکسی با VPN کامل
• نحوه اتصال از طریق DNS Tunnel
• مشاهده وضعیت اتصال و میزان مصرف ترافیک
• مدیریت پروفایل‌ها و تنظیمات برنامه
• نکات مهم برای داشتن اتصال پایدارتر
https://www.youtube.com/watch?v=tz8cj7HzHVI</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/whitedns/1299" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1298">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LzoTvyBl7T2FxyPviU5T6bKbL4ShHvdRprnsruaMl6t-GDTcUUenAJnLVu6rtTOgz4Ihk5DmWPvXhhYkC_c-c3eNjKUJaj1Y_b01483sgM_xVvSFinFglIsr-1JHIakelUXliq-Kr8mpNKN2SDbJMwH094Fvi0tGwoaIakAoWLPgNDLjTL7XoGsIePlCXrJ5YN0aQQt9kRvn02RVC8HBZFv8zsxDNAw-M8ZwuAcXFf_2DJLuFYapyZssYhyseLFcojqJTbck7Zg3Ka3ofAGAoaPK907ol3F2TmFIeUT5QvcC2OdkW39h8yZHGCi3-Es6ydnqgZnd8GEEcdGcu1dbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1298" target="_blank">📅 18:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1297">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FBvebABCQkonOWffmFxQPZQ-yM2baXEksruxe8kdJ6yJTCQfzXXoZpTF0ifSMBUo_h433NKKvteXnoJZt39r8-bWZmY-3LGRP9AkTxKwlFXNyERaZgPZGb2h7PnnLiA_oSJ0U8MqTr_E5txa6nrhLSltdaVBIS6Idx8gdDvHw2AxbVYqaaM2dbB4HZEEmWpVYngUHVfLBZvxRjAW1F-KMMACJENnC_hcAgAAmWC5np8uTD8PnGjTTETyjVHqRdH025exlb7aHA5U-ogMv2kC9iEYeJY8pxIJqxQw1vHGdd6RjZW0J8T5t0ho2G8k8UKKesDouJ813gSVhXRbHnlgSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1297" target="_blank">📅 18:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1294">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1294" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخهٔ جدید Aether منتشر شد! (v1.2.1)
نسخه قبلی رو حذف کنید بعد نسخه جدید نصب کنید
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1294" target="_blank">📅 16:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1293">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/H0nB1wDGc5QQvU1MK1YkZsxlaAfX5Zi34JM832AnklRdooFRj6r6T2oL0108uWyk6qvGrj26kwLyOw9V5I-BAQhbBAHaE3IHEMcSU94AdbvacB-IAfvAiCZtVJePbjp0S9gDZuh5w5YUiev_gHnKMaU4Qhf7AWhx6gYPxiL-LqIkMpbXLPsmDysDnRcCcePYO9rgJsCYQ0KR7Jsy3VlMp9X5GpFs08GOgoDV8OgUWrUAYPico743bloFvvPSRFX6iCjzxkpegDFV0RM3QWBkTCBR9Vb1gyZL6j01xopTEJ34Qe0yzytEeJwZ-Jdwad3Pejpz-y80FWn_B4plKHebOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخهٔ جدید Aether منتشر شد! (v1.2.1)
🎉
اگر به دنبال یک اتصال واقعاً پایدار، فوق‌العاده سریع و بدون نیاز به برنامه‌های جانبی (مثل v2rayNG) هستید، نسخهٔ جدید اِتِر موبایل با قابلیت‌های شگفت‌انگیز برای عبور از سخت‌ترین فیلترینگ‌ها آماده شده است!
🔥
تازه‌های بی‌نظیر در نسخهٔ ۱.۲.۱:
⚡️
موتور هوشمند واقعی (Smart Auto):
برنامه مانند یک مهندس شبکهٔ حرفه‌ای، ابتدا DPI شبکه و وضعیت اختلال‌ها (مانند فیلترینگ SNI یا خفه‌کردن UDP) را تحلیل می‌کند و سپس بهترین چیدمانِ اولویت‌بندی شده از پروتکل‌ها، سطح مبهم‌سازی (Noize)، فرگمنت و رنج‌های آی‌پی را برای اتصال گام‌به‌گام و کاملاً پایدار اعمال می‌کند.
🟢
«متصل» یعنی اتصال واقعی!
دیگر خبری از کلمهٔ «متصل» فیک که هیچ سایتی را باز نمی‌کند نیست! برنامه تا زمان دریافت هر ۴ تیک سبز سلامت (پورت، هندشیک، اینترنت و آی‌پی) در وضعیت بررسی می‌ماند تا از اینترنت واقعی مطمئن شود.
🛰
نمایش آنی آی‌پی و پرچم:
با موازی‌سازی سرویس‌های تست سلامت و تشخیص IP، این فرآیند با سرعت بسیار بیشتری انجام شده و بلافاصله وضعیت موقعیت جدید شما نمایش داده می‌شود.
🔄
آپدیت آسان و مستقیم (مشابه تلگرام - آزمایشی):
از این پس برای دریافت آپدیت‌ها نیازی به سر زدن به گیت‌هاب ندارید؛ نسخهٔ جدید مستقیماً درون برنامه به شما اطلاع داده شده و با یک کلیک دانلود و نصب می‌شود.
🛠
رفع ریشه‌ای تداخل‌های متنی زبان فارسی:
به‌هم‌ریختگی ظاهری و راست‌به‌چپ اعداد در فیلدهای حساسی مانند ip:port و اندپوینت‌های دستی کاملاً برطرف شده است.
🔒
امنیت بسیار سخت‌گیرانه‌تر:
تأیید نام هاست در اتصال‌های TLS (بستن راه حملات MitM)، حذف لاگ‌های موتور در نسخهٔ نهایی و مسدودسازی ترافیک ناامن HTTP برای محافظت حداکثری از اطلاعات شما.
🧹
دکمهٔ بازنشانی سریع تنظیمات:
با تنها یک لمس، تمام تنظیمات پیشرفته را به مقادیر پیش‌فرض بازگردانید.
لینک ریپو :
🔥
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1293" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1291">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhbu0aaLcErw_mD15KCw8EzJ87P-MuGeHKpXxU5aovpD3xexL51HioNM9MbndnoUx3Kx1ACWT01WMOJ8EGuP7hhaCc8SGL1wI6v8CrEUP_XFqjj1Wc3ejbizrv9_qKRdLqlrUaS7ZSO_wf-zgvxMCrWVPe5jkUgunm0HKGcVQVqAiXQXLFjW4HTy60xkLGI3G6u6VtAmaJ1yBTgdZfQa1ak_6MWqnsqjfEAAEU8LfWa56VuU1RiFUpqOUnW8HSJOprdSsz9hQCi_AJFyXrdPLZSLcCqRehDHbOeKi6JPPygV0_JIFrOLbqWlsblBLPRxrqf4GUyBXSAaCURiO5mY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/whitedns/1291" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنوا | Nova</strong></div>
<div class="tg-text">🤖
ساخت پنل نوا پروکسی فقط با ربات تلگرام!
دیگه لازم نیست مراحل نصب رو دستی انجام بدین.
😎
فقط وارد ربات نوا پروکسی بشین، اکانت Cloudflare بسازین، توکن رو دریافت کنین و چند ثانیه بعد پنل اختصاصی خودتون آماده‌ست.
🚀
بعد از ورود به پنل هم فقط کافیه رمز ادمین رو تنظیم کنین، کانفیگ رو داخل کلاینت Import کنین و از اینترنت آزاد استفاده کنین.
📺
آموزش کامل مراحل داخل ویدیو گفته شده.
💬
اگر سوالی داشتین، داخل کامنت‌ها بپرسین.
🔹
ربات تلگرام:
@IRNovaProxy_Bot
🔹
وب‌سایت:
https://novaproxy.online</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1289" target="_blank">📅 09:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard  https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1288" target="_blank">📅 04:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1287" target="_blank">📅 04:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1285">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9c-iLNv5e5wLVEk0bdPYvBUpy6xE42V0D5PoWzdhB3K7rwTxmzVci29XkSijg2i4ELPrT-mYP5eEyeluknYM6X_ghHM9DR8OE0XLAaou7oHYf5e3IobGHgRlsYFjJAnUAjmX99WDBPB6Nn6-rGBS14zutc3syDGijJ-4tbDtm9j6xbr_YtSSWc3Ne1L15IDWtjbEt7GlVvjis-BgmDY-7azHqa399Tsh-dh5zAtbYIoWSSEj5jE8RMGGs767twtUgAt1b24DhKbAXOrfQI8TuqGfg-wXlV5RYNG6k8jHpHNU0Cu0GVuXoGFBGZmFCu27R9AUJA2xBd7otTj7OgiqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/whitedns/1285" target="_blank">📅 15:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1283">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک ظرفیت جدید برای تست فلایت داریم که میتونید از لینک زیر استفاده کنید
🚀
📱
اپ  CoreForge  یک فیلترشکن ساده و قدرتمند برای iOS / آیفون که مخصوص استفاده در شرایط سخت، اختلال شدید اینترنت، اینترنت ملی و حتی دوران قطعی کامل طراحی شده.
https://testflight.apple.com/join/3htm1Whc
آموزش
🎥
📹
:
https://www.youtube.com/watch?v=filwdiPKN90
@whitedns
📢
🔗</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/whitedns/1283" target="_blank">📅 12:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1282">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uNxj4w5ziwZvcFJ8mTlbUUb3I4kFualXaWjUpSbVxXNcbsngvfA257JSIXjjZDZGr4Nh95k9zaGZOlMCZZpfYiUJD2n58XQbehD3v8KM9FBMdsxvvuzgseStwn9bn2QvSQT5j834K8hsSAFPx0RraZS9hmv1_RPuu8OXZm3V6ffC6xGbs8CjFLdpaiBghOI0lgTvjTYXapP4bHtQ7cEkVDIHr7G5phwHkxntSvS88TpHWq-3X9o_v7ZaJYVKT6yc_Ujma8I8fb2UFpxTqA41JByQCWM7f7sQZYgYgMvOoe6IQ47dp-hHuXN9BvlncJJls28L0SgWphIl-tYIZ9jCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1282" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1281">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MG-NPBPEaR3zgWzNZ2HEICihDhbFb5giQBLsT6vQFY0BXMUDbW2wlDCOwtfhsAFmot0b6_V9T64qHlFTD5nfh-BFxCrFMUmnoomZcs0Pw6aYk5RqKYHk6qwcrYdjMPaA_7y_bAzHMXQQebKzNmXo6G8Um_tqpvJUVVUsXzgkWnFOmO2_Pd2e3Jph6Wv245vnBDI0QJusHb8wsiCRiNoqZhmqN5Ih84Kboi6L2gUwLR-dDB7uRCCYBeyZxBC_gc7qXIDQ_9mxmvaPbLPU9yvpOREov7iCFlfGxxBrdqhLbCNHuzd3LrfqktqnkjKcCU9uRLp_UCsC8S7KQUF7znJSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1281" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1280">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Bja89UPgsd8sa4-Js1FdzqXQt1Neg3HRnVTnqizJoaBQ0xGcGsZQAn9vBX4vLfQRpL19YJtOcLokqFoBwEqWqPwhvwKiukIQrCp8-5uVfefRClb__qeTLaksO2az7_ZqmiXA43t4uDPAQWCSTHeHMoLVxvFZB8WGTlEluzaxu7D4FvoGlq9m743PsBWzRuYTHVZfP3u5YUB1XimNNaACkhjNjp9XwZ6OOttqfm2-tw-SGQHUC3sJ4Gdlcy6I_JoIzOKyubATlysFdsSdsCq2XTARAGcNJ0U2ebmgbEEZFomOAkevSEgOsPKe-oxbNlZYVOQXuDFQdHnpGpaGbAPrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/whitedns/1280" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
