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
<img src="https://cdn4.telesco.pe/file/sp59gkS8GmXTpqldZREMAlg2VMthzNaj0TLcoaId7OXbYBbbOdb6Z2KV-KEUzZx-GxBTqIAJ7qF5TmrPpRFP8IMgajoEpS3FSTaoEIiSuE7xFASzrf9puvA6ueu8TB6plQrUOMoXZKzspt8Y3px5rVbLESeSVtJqQWfIdVZ-ClDk2iTrfi6wxlyZAnlyh7Qc-jFARnR6IDWF7LGC7SNt404RzPqF1TxbC5DJoOOUGcDnq-ED0Iw4ntXAh9SKtbAa45gUje3zsc6gjSE0lJbtzPLASAaKiq_o_drqvT_mhT9ZghDUulcGkmQ1Xpn-gwE4bwucgMglSv6dKIRfOE3AEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.67K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📌
فهرست جامع و راهنمای جستجوی مطالب کانال (آرشیو ابزارها و آموزش‌ها)
📱
۱. کلاینت‌ها، اپلیکیشن‌ها و ابزارهای اتصال
جدیدترین نسخه‌های برنامه‌های اتصال به همراه ابزارهای اختصاصی دور زدن نت ملی:
*
شیر و خورشید (ShiroKhorshid) / Se7enPro:
کلاینت‌های اختصاصی سایفون (اندروید و ویندوز) با قابلیت CDN Fronting. ➔
#شیر_و_خورشید
#Se7enPro
#سایفون
*
خانواده V2ray:
کلاینت‌های محبوب v2rayNG (نسخه‌های 2.1.7 و 2.1.8) برای اندروید و V2rayN برای ویندوز. ➔
#v2rayNG
#v2rayN
#v2ray
*
مهسا ان‌جی (MahsaNG):
نسخه v16 با قابلیت اتصال مستقل سایفون و دامین فرانتینگ. ➔
#MahsaNG
#مهسا_ان_جی
*
متد رله گوگل (mhrv-rs / MasterHttpRelayVPN):
کلاینت اتصال از طریق رله گوگل با زبان Rust و پایتون. ➔
#mhrv_rs
#MHRV
#رله_گوگل
*
اسکیرک (Skirk):
ابزار فوق‌العاده تونل کردن ترافیک از طریق Google Drive. ➔
#Skirk
#اسکیرک
#گوگل_درایو
*
زیرلن (Zyrln):
عبور از فیلترینگ با ترافیک ابری گوگل و کلادفلر ورکر. ➔
#Zyrln
#زیرلن
*
نوا پروکسی (NovaProxy):
پروکسی دسکتاپ با ترکیب Google Apps Script و Cloudflare. ➔
#نوا_پروکسی
#NovaProxy
*
بله وی‌پی‌ان (BaleVPN) و Whitelist Bypass:
تونل کردن اینترنت از طریق تماس صوتی/تصویری پیام‌رسان بله. ➔
#BaleVPN
#Whitelist_Bypass
#بله_میت
*
چشم عقاب (Eagle Eye):
دریافت آفلاین کانفیگ از طریق فرکانس شبکه‌های ماهواره‌ای. ➔
#چشم_عقاب
#Eagle_Eye
#آفلاین
*
کلاینت‌های iOS (آیفون):
برنامه‌های NexaTunnel و TheFeed (نسخه TestFlight). ➔
#NexaTunnel
#TheFeed
#آیفون
#iOS
*
سایر کلاینت‌ها و ابزارها:
NekoBox، V2box، Slipnet، MasterDns، OpenVPN، Happ، TunnelForge، HashemVasel و ابزار کلاینت لینوکسی XuiFactor. ➔ (اسم برنامه را سرچ کنید) یا
#کلاینت
#ابزار
🛠
۲. آموزش‌های طلایی و متدهای عبور از فیلترینگ
آموزش‌های قدم‌به‌قدم برای راه‌اندازی متدهای جدید:
*
متد SNI Spoofing:
آموزش دور زدن فیلترینگ با تزریق دامنه فیک (مثل hCaptcha) برای ویندوز (RM SNI Spoofer / Cloak)، لینوکس (FakeSNI)، و اندروید به همراه آموزش راه‌اندازی روی سرور ایران با پنل 3x-ui. ➔
#SNI_Spoofing
#FakeSNI
#اسپوف
#Cloak
*
آموزش‌های نتلیفای (Netlify) و ورسل (Vercel):
دیپلوی کانفیگ XHTTP، تغییر دامنه نتلیفای با کلادفلر ورکر برای رفع مسدودی، و اسکریپت XHTTP-Installer. ➔
#نتلیفای
#Netlify
#ورسل
#Vercel
#XHTTP
*
ترکیب سایفون و MitM:
آموزش متد Patterniha با گرفتن سرتیفیکیت (SSL) برای دور زدن DPI. ➔
#سایفون
#MitM
#سرتیفیکیت
*
اشتراک‌گذاری اینترنت آزاد (Hotspot/LAN):
آموزش انتقال اینترنت بدون فیلتر سیستم (V2ray یا SNI Spoof) به گوشی موبایل یا برعکس با برنامه‌های PdaNet+ و تنظیمات LAN/Proxy. ➔
#هات_اسپات
#LAN
#اشتراک_نت
#PdaNet
*
گیمینگ و پینگ پایین:
آموزش اتصال ویندسکرایب (Windscribe) روی SNI Spoofing برای کاهش پینگ در بازی‌ها. ➔
#گیمینگ
#پینگ
#Windscribe
#وینداسکرایب
*
لینوکس و ترمینال:
آموزش تونل کردن ترافیک ترمینال لینوکس با ابزار Proxychains4. ➔
#لینوکس
#Proxychains4
🔍
۳. اسکنرها و ابزارهای پیدا کردن آی‌پی (IP/SNI Scanners)
ابزارهای اختصاصی برای پیدا کردن آی‌پی‌های تمیز آکامای (Akamai) و فستلی (Fastly):
*
نتورک چکر (Network Checker):
اپلیکیشن همه‌کاره اندروید (v0.6.0) مجهز به اسکنر آکامای و کانفیگ‌ساز نتلیفای. ➔
#نتورک_چکر
#Network_Checker
*
اسکنرهای تحت وب و ویندوز:
CDN IP Finder (نسخه مرورگر)، AniScanner (داشبورد گرافیکی وب)، SNI-Radar و ابزارهای اسکن Akamai با PowerShell و Python. ➔
#اسکنر
#CDN_IP_Finder
#AniScanner
#اسکنر_آی_پی
*
لیست آی‌پی‌های آماده:
برای دسترسی به لیست‌های پینگ‌گرفته شده اپراتورها (ایرانسل، همراه اول، مخابرات، رایتل و سامانتل). ➔
#آی_پی_تمیز
#آکامای
#لیست_آی_پی
🤖
۴. ابزارها، اسکریپت‌ها و پروژه‌های خاص
ترفندها و ابزارهای کاربردی برای کارهای روزمره:
*
دانلودرها و ربات‌ها:
PlayDL (دانلود مستقیم از گوگل‌پلی)، MattDownloader (دانلودر با GitHub Actions) و ربات‌های هوش مصنوعی (Gemini, Claude, ChatGPT). ➔
#دانلودر
#PlayDL
#هوش_مصنوعی
#ربات
*
ایزی‌تل (EzyTel / Telemirror):
خواندن محتوای تلگرام به صورت آفلاین از طریق زیرساخت Google Translate. ➔
#ایزی_تل
#EzyTel
#تلگرام_آفلاین
*
سایر ترفندها:
ساخت شورت‌کات در Termux، مسدودساز آپدیت ویندوز (Windows Update Blocker)، ابزار Netlify obfuscator و مدیریت پروژه در VSCode. ➔
#ترموکس
#ترفند
#ویندوز</div>
<div class="tg-footer">👁️ 643 · <a href="https://t.me/archivetell/5688" target="_blank">📅 16:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
معرفی olcNG: فیلترشکن سریع، ساده و بهینه‌شده برای اندروید
---
رفقا سلام!
✋
امروز می‌خوایم یک اپلیکیشن بسیار جذاب و کاربردی به اسم
olcNG
رو بهتون معرفی کنیم. این برنامه در واقع یک نسخه (Fork) اوپن‌سورس و بهینه‌شده از اپلیکیشن محبوب
v2rayNG
هست که توسط تیم OpenLibreCommunity توسعه داده شده.
اگر از شلوغی و پیچیدگی‌های v2rayNG خسته شدید و دنبال یک جایگزین سریع‌تر، ساده‌تر و البته امن می‌گردید، olcNG دقیقاً همون چیزیه که بهش نیاز دارید!
###
✨
چرا olcNG رو پیشنهاد می‌کنیم؟
🔸
هسته (Core) فوق‌العاده قوی:
این اپلیکیشن برای مدیریت ترافیک و پردازش کانفیگ‌ها، از Xray-core و ماژول‌های قدرتمند
AndroidLibXrayLite
و
hev-socks5-tunnel
استفاده می‌کنه که باعث کاهش پینگ و افزایش چشمگیر سرعت اتصال میشه.
🔸
پشتیبانی کامل از تمامی پروتکل‌ها:
هر کانفیگی که در v2rayNG استفاده می‌کنید (مثل VLESS ،VMess ،Trojan و ShadowSocks)، بدون هیچ مشکلی در این برنامه قابل اجراست.
🔸
رابط کاربری (UI) بهینه‌شده:
برخلاف نسخه‌های اصلی که ممکنه برای کاربران عادی گیج‌کننده باشن، olcNG با یک طراحی بسیار ساده، سبک و کاربرپسند ارائه شده.
🔸
منبع باز و کاملاً رایگان (Open-Source):
این اپلیکیشن تحت لیسانس GPL-3.0 در گیت‌هاب منتشر شده که یعنی هیچ کد مخرب یا جاسوسی‌ای در اون وجود نداره و امنیتش تضمین شده است.
---
###
💻
دانلود و نصب:
نسخه جدید این اپلیکیشن (v4.2.1) به تازگی منتشر شده و با اندرویدهای جدید کاملاً سازگاری داره. برای دانلود مستقیم نسخه رسمی، می‌تونید از لینک گیت‌هاب پروژه استفاده کنید:
🔗
لینک دانلود مستقیم از گیت‌هاب:
🌐
https://github.com/openlibrecommunity/olcng/releases/tag/v4.2.1
*(در صفحه باز شده، روی فایلِ با پسوند
.apk
کلیک کنید تا دانلود شروع شود).*
🔗
سایت رسمی پروژه:
zarazaex.xyz
📌
#معرفی_اپلیکیشن
#اندروید
#فیلترشکن
#olcNG
#v2rayNG
#Xray
#VLESS
#Bypass
#Vpn
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/archivetell/5687" target="_blank">📅 16:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
این سایت یه معدن طلایِ هوش مصنوعیه: از ساخت حرفه‌ای‌ترین پرامپت‌ها تا ویرایش عکس و ساخت موزیک رایگان!
---
اگر از ChatGPT یا Claude استفاده می‌کنید اما خروجی‌های دقیقی نمی‌گیرید، یا دنبال ابزارهای رایگان برای تولید محتوا هستید، سایت
The Prompt Index
همون چیزیه که بهش نیاز دارید. این سایت فقط یک پرامپت‌ساز نیست، بلکه یک "جعبه‌ابزارِ دیوانه‌کننده" است که امکانات پولی ده‌ها سایت مختلف رو یکجا و رایگان جمع کرده!
کافیه یک
اکانت کاملاً
رایگان
(0$)
بسازید تا به این گنجینه دسترسی پیدا کنید:
📝
۱. ماشین جادویی پرامپت‌سازی (Prompt Generator)
با این ابزار، کیفیت جواب‌هایی که از هوش مصنوعی می‌گیرید ۱۰ برابر بهتر میشه!
🔸
دارای ۲۲۸ فریم‌ورک استاندارد در ۲۵ دسته‌بندی مختلف (از برنامه‌نویسی تا حل مسئله).
🔸
حالت مبتدی (Wizard):
فقط با جواب دادن به ۴ سوال ساده، حرفه‌ای‌ترین دستور رو براتون می‌نویسه.
🔸
حالت حرفه‌ای (Expert):
امکان ترکیب قالب‌ها برای کارهای فوق‌تخصصی.
🎁
۲. سوئیت ابزارهای رایگان (AI Toolbox)
🎵
موزیک و صدا:
ساخت ۲ ترک موسیقی در روز، ۵۰ دقیقه تغییر صدای هوش مصنوعی در ماه و ساخت ۱۰ افکت صوتی روزانه!
🖼
ویرایش تصویر حرفه‌ای:
افزایش کیفیت عکس (Upscaler)، حذف پس‌زمینه و واترمارک، ترمیم و گسترش ابعاد عکس (هر کدوم ۱ تا ۲ بار رایگان در روز).
📚
کتاب‌ساز و نویسندگی:
ابزار PromptBook برای ساخت یک کتاب کامل به همراه عکس جلد در ماه، ابزار Humanizer (انسانی‌سازی متن برای دور زدن ربات‌ها) و استخراج متن از PDF.
💡
نتیجه‌گیری:
پیدا کردن سایتی که مجموعه‌ای از بهترین ابزارهای موسیقی، تصویر، متن و پرامپت‌نویسی رو یکجا و رایگان در اختیارتون بذاره واقعاً غنیمته. حتماً سیوش کنید که به کارتون میاد!
🔗
لینک ورود و استفاده از ابزارها:
🌐
https://www.thepromptindex.com/
📌
#هوش_مصنوعی
#پرامپت
#ابزار_کاربردی
#تولید_محتوا
#ویرایش_عکس
#ساخت_موزیک
#کتاب_ساز
#AI
#رایگان
#پرامپت_نویسی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5686" target="_blank">📅 14:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
آموزش ساخت امن‌ترین کانفیگ‌های VLESS REALITY (پروتکل غیرقابل فیلتر!)
---
رفقا سلام!
✋
خیلی‌هاتون پرسیدید این کانفیگ‌های قدرتمندی که براتون می‌ذاریم دقیقاً چطوری ساخته میشن؟
امروز می‌خوایم قدم‌به‌قدم بهتون یاد بدیم چطور روی پنل
سنایی (3x-ui)
دقیقاً همین کانفیگ‌های فوق‌امنیتی رو برای خودتون بسازید!
🛠
مراحل ساخت کانفیگ:
۱. تنظیمات پایه (Basic Settings):
بعد از ورود به پنل، یه Inbound جدید بسازید:
🔸
پروتکل (Protocol):
روی
vless
قرار بدید.
🔸
پورت (Port):
ترجیحاً
443
(یا پورت‌های آزاد سرورتون) باشه.
۲. تنظیمات شبکه (Network):
🔹
بخش
Network:
روی
tcp
باشه.
🔹
تیک
Reality
رو حتماً روشن کنید تا تنظیماتش باز بشه.
۳. تنظیمات استتار (Reality Settings) - مهم‌ترین بخش:
حالا باید ترافیکمون رو پشت یک سایت معروف مخفی کنیم:
🔸
در کادر
dest:
آدرس یک سایتِ بدون فیلتر رو با پورت ۴۴۳ بنویسید (مثلاً
www.microsoft.com:443
).
🔸
در کادر
serverNames:
همون سایت رو بدون پورت وارد کنید (مثلاً
www.microsoft.com
).
🔸
روی دکمه
Generate
کلیک کنید تا کلیدهای رمزنگاری (Private Key) و کدهای کوتاه (ShortIds) به صورت خودکار براتون ساخته بشن.
۴. ساخت کاربر و فعال‌سازی Vision:
حالا برید پایینِ صفحه تو بخش Clients و روی
+ Add
کلیک کنید:
🔹
ایمیل (ID):
یه اسم دلخواه برای کانفیگ بذارید.
🔹
⚠️
نکته طلایی:
در قسمت
Flow
، حتماً گزینه
xtls-rprx-vision
رو انتخاب کنید (این همون جادوییه که باعث دور زدن سیستم فیلترینگ و کاهش چشمگیر پینگ میشه).
✅
ذخیره و استفاده:
دکمه Save رو بزنید! تمام شد!
حالا روی آیکون QR Code کلیک کنید و لینک کانفیگتون رو کپی کنید. اگر به لینک دقت کنید، می‌بینید که دقیقاً همون ساختار حرفه‌ایِ Vless Reality رو داره. کانفیگ رو تو v2rayNG یا NekoBox کپی کنید و از اینترنت آزاد لذت ببرید!
✌️
📌
#آموزش
#فیلترشکن
#سرور
#پنل_سنایی
#VLESS
#Reality
#Vision
#کانفیگ
#تونل
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/5685" target="_blank">📅 10:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
معرفی پنل PasarGuard: نسل جدید و قدرتمند مدیریت پروکسی و ضدسانسور
---
امروز قصد دارم یک پنل مدیریت سرورِ بسیار مدرن، جامع و قدرتمند به اسم
PasarGuard
رو بهتون معرفی کنم. این پنل با زبان‌های Python و React.js نوشته شده و با ترکیب Xray-core و WireGuard، یک رابط کاربری بی‌نظیر برای مدیریت صدها اکانت به صورت همزمان به شما میده.
اگر دنبال یک پنل حرفه‌ای با امکانات توزیع‌شده (Multi-Node) هستید، پاسارگارد یکی از بهترین انتخاب‌هاست!
✨
مهم‌ترین ویژگی‌های پنل PasarGuard:
🔸
پشتیبانی کامل از مدرن‌ترین پروتکل‌ها:
پشتیبانی از Vmess ،VLESS ،Trojan ،Shadowsocks ،WireGuard و Hysteria2 به همراه قابلیت‌های TLS و REALITY.
🔸
مدیریت پیشرفته کاربران:
امکان استفاده از یک کاربر برای چندین پروتکل، پشتیبانی از چند کاربر روی یک اینباند، و تعریف فال‌بک (Fallbacks).
🔸
محدودیت‌های هوشمند:
قابلیت تنظیم محدودیت حجم و زمان، و همچنین
محدودیت‌های دوره‌ای
(ریست شدن حجم به صورت روزانه، هفتگی و...).
🔸
سابسکریپشن استاندارد:
تولید لینک سابِ کاملاً سازگار با کلاینت‌های V2ray ،Clash و ClashMeta به همراه تولید خودکار QR Code.
🔸
امکانات جانبی قدرتمند:
دارای ربات تلگرامی اختصاصی، محیط خط فرمان (CLI)، دیتابیس‌های متنوع، API کامل و مانیتورینگ دقیق ترافیک.
---
💻
آموزش نصب سریع (روی لینوکس):
توسعه‌دهندگان، استفاده از دیتابیس
TimescaleDB
رو برای این پنل پیشنهاد دادن. کافیه به سرور متصل بشید و دستور زیر رو کپی و اجرا کنید:
curl -fsSL [https://github.com/PasarGuard/scripts/raw/main/pasarguard.sh](https://github.com/PasarGuard/scripts/raw/main/pasarguard.sh) -o /tmp/pg.sh \\
&& sudo bash /tmp/pg.sh install --database timescaledb
پس از پایان نصب، برای ساخت نام کاربری و رمز عبورِ مدیر (Admin)، دستور زیر رو وارد کنید (به جای
<username>
نام دلخواهتون رو بنویسید):
pasarguard cli admins --create <username>
🌐
نحوه ورود به پنل:
پنل روی پورت
8000
اجرا میشه و برای ورود به آدرس
https://YOUR_DOMAIN:8000/dashboard
نیاز دارید. *(نکته مهم: برای امنیت بیشتر، پنل پاسارگارد الزاماً به سرتیفیکیت SSL و اتصال HTTPS نیاز دارد).*
🔗
لینک گیت‌هاب پروژه برای اطلاعات بیشتر:
🌐
https://github.com/PasarGuard/panel
📌
#معرفی_ابزار
#پنل
#PasarGuard
#پاسارگارد
#فیلترشکن
#سرور
#Xray
#VLESS
#Hysteria2
#Wireguard
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5684" target="_blank">📅 03:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
انتشار آپدیت بزرگ و جذاب پنل 3x-ui (نسخه v3.2.0)
---
آپدیت جدید و پر از امکاناتِ پنل مدیریت سرور محبوب
3x-ui
(نسخه سنایی) منتشر شد. این نسخه (v3.2.0) یکی از بزرگترین آپدیت‌های این پروژه است که تمرکز ویژه‌ای روی مدیریت گروهی کاربران، بهبود رابط کاربری و ارتقای پروتکل‌های دور زدن فیلترینگ داشته.
###
✨
مهم‌ترین تغییرات و قابلیت‌های جدید:
🔸
مدیریت حرفه‌ای گروه‌ها:
اضافه شدن صفحه اختصاصی برای گروه‌بندی کلاینت‌ها (Client Groups) و امکان خروجی گرفتن لینک سابسکریپشن مجزا برای هر گروه.
🔸
پشتیبانی از XHTTP پیشرفته:
اضافه شدن تنظیمات حرفه‌ای XHTTP و پروکسی‌های خارجی TLS (قابلیت بسیار مهم برای شرایط فعلی فیلترینگ).
🔸
عملیات گروهی کلاینت‌ها (Bulk Actions):
امکان اضافه، حذف، انتقال و تخصیص گروه به کلاینت‌ها به صورت دسته‌جمعی.
🔸
فیلترهای پیشرفته:
اضافه شدن دراور (Drawer) فیلتر جدید برای پیدا کردن سریع کلاینت‌ها بر اساس حجم مصرفی، تاریخ انقضا، پروتکل و وضعیت اتصال.
🔸
امنیت و بهینه‌سازی دیتابیس:
اختصاص Role رندوم برای دیتابیس PostgreSQL جهت امنیت بیشتر و بهینه‌سازی استخر اتصالات (Pool Tuning) برای جلوگیری از افت منابع سرور.
🔸
ارتقای پروتکل‌ها:
اضافه شدن قابلیت Salamander auto-seed برای پروتکل Hysteria و قرار گرفتن فیلد Testseed برای VLESS Vision.
🔸
بهبود رابط کاربری:
بازنویسی و مدرن‌سازی کامل فرانت‌اند پنل با TypeScript و اضافه شدن داکیومنت‌های API به داخل خود پنل.
###
🛠
مهم‌ترین باگ‌های برطرف‌شده:
🔹
حل مشکل قرار نگرفتن SNI در لینک‌های اشتراک‌گذاری REALITY.
🔹
حفظ انکودینگ صحیحِ اطلاعات کاربران در لینک‌های Trojan، ShadowSocks و Hysteria.
🔹
رفع مشکل تداخل External-proxy با SNI در اتصال‌های TLS.
---
💻
نحوه آپدیت:
برای آپدیت به این نسخه، کافیه به سرورتون SSH بزنید، دستور
x-ui
رو در ترمینال وارد کنید و از منوی باز شده، گزینه آپدیت به آخرین نسخه رو انتخاب کنید.
🔗
مشاهده لیست کامل تغییرات در گیت‌هاب:
🌐
https://github.com/MHSanaei/3x-ui/releases/tag/v3.2.0
📌
#آپدیت
#پنل
#سنایی
#فیلترشکن
#سرور
#Xray
#VLESS
#XHTTP
#Hysteria
#مدیریت_سرور
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5683" target="_blank">📅 03:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
آموزش نصب سریع Hysteria 2 روی سرور اوبونتو (بدون قطعی)  ---  رفقا سلام!
✋
پروتکل Hysteria 2 به دلیل شبیه‌سازی ترافیک به HTTP/3، در حال حاضر یکی از مقاوم‌ترین روش‌ها برای عبور از سیستم‌های فیلترینگ (DPI) است. در این پست، نحوه نصب سریع و بهینه این پروتکل رو…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/5682" target="_blank">📅 02:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5681">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
آموزش نصب سریع Hysteria 2 روی سرور اوبونتو (بدون قطعی)
---
رفقا سلام!
✋
پروتکل Hysteria 2 به دلیل شبیه‌سازی ترافیک به HTTP/3، در حال حاضر یکی از مقاوم‌ترین روش‌ها برای عبور از سیستم‌های فیلترینگ (DPI) است. در این پست، نحوه نصب سریع و بهینه این پروتکل رو روی یک سرور مجازی (اوبونتو 22.04 یا 24.04) آموزش می‌دیم:
۱. آپدیت سرور و نصب پیش‌نیازها
ابتدا به سرور خود متصل شده و دستورات زیر را کپی و اجرا کنید:
sudo apt update && sudo apt upgrade -y
sudo apt install curl wget ufw fail2ban -y
۲. نصب Hysteria 2
با اجرای دستور زیر، پروتکل به صورت خودکار نصب می‌شود:
Bash
bash <(curl -fsSL [https://get.hy2.sh/](https://get.hy2.sh/))
۳. تنظیم کانفیگ سرور
دستور زیر را بزنید تا فایل تنظیمات باز شود:
Bash
nano /etc/hysteria/config.yaml
سپس کدهای زیر را کپی کرده و داخل آن قرار دهید:
(نکته: در بخش password، حتماً یک رمز قوی برای خودتان بنویسید)
YAML
listen: :443
auth:
type: password
password: "Your_Strong_Password_Here"
masquerade:
type: proxy
proxy:
mode: remote
addr: [https://www.apple.com](https://www.apple.com)
quic:
initStreamReceiveWindow: 8388608
maxStreamReceiveWindow: 16777216
initConnReceiveWindow: 8388608
maxConnReceiveWindow: 16777216
maxIdleTimeout: 30s
activeConnIdleTimeout: 30s
disablePathMTUDiscovery: false
bandwidth:
up: 100 Mbps
down: 100 Mbps
udpForwarding: true
برای ذخیره فایل، کلیدهای
Ctrl+X
سپس
Y
و در نهایت
Enter
را بزنید.
۴. باز کردن پورت‌ها در فایروال
برای عملکرد صحیح، باید پورت ۴۴۳ از نوع UDP را باز کنید:
Bash
sudo ufw allow 443/udp
sudo ufw enable
۵. راه‌اندازی و اجرای نهایی
Bash
sudo systemctl daemon-reload
sudo systemctl enable hysteria
sudo systemctl restart hysteria
📱
تنظیمات برای اتصال در گوشی یا ویندوز:
در برنامه‌هایی مثل NekoBox ،v2rayNG یا Exclave یک پروفایل جدید از نوع
Hysteria 2
بسازید و اطلاعات زیر را وارد کنید:
🔸
Server:
آی‌پی سرور شما
🔸
Port:
443
🔸
Password:
رمزی که در فایل کانفیگ تعیین کردید
🔸
SNI / Masquerade:
www.apple.com
🔸
Skip Cert Verify (Insecure):
True
(حتماً فعال شود)
✅
تمام! حالا یک کانکشن به شدت پایدار و پرسرعت دارید. اگر در مراحل نصب سوالی داشتید، توی کامنت‌ها بپرسید.
👇
📌
#آموزش
#سرور
#فیلترشکن
#Hysteria2
#Hy2
#اوبونتو
#V2ray
#تونل
#VPS
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5681" target="_blank">📅 02:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">https://t.me/boost/archivetell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5680" target="_blank">📅 22:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⚠️
خدمت دوستان باید چند نکته مهم رو بگم:
هیچ تاثیری روی پروتکل های tcp , udp ,ikev2, wstunnel رو هر حالتی از سانسورشیب بزارید از کانفیگ A تا حتی H و I باشه هیچ تاثیری در وصل شدن سریعتر شما اصلا نداره! فقط این حالت برای وایرگارد قابل استفاده هست دقت کنید
نکته بعدی این هستش که شما حالت server routing رو هم حالت اتوماتیک بزارید چه حالت regular و حتی alternative هیچ تاثیری باز هم تو اتصال شما نداره فقط و فقط حالت اتوماتیک بزارید
مورد اخر گزینه large tls هم روشن بزارید چون به اتصال بهتر شما کمک میکنه وقتی خاموش باشه سخت تر وصل میشید در کل این ۳ مورد رو دوستمون دقت نکردن و نیاز بود این مورد حتما رو بگم که سرگردان تغییر کانفیگ های A,b,c نشید
❤️
#windscribe
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5679" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://80fbb3e8-d705-4eca-a519-fd82fd6d319a@46.38.137.141:38554?type=tcp&encryption=none&security=none#%40IR_SI%20%2F%20100GB%20UAE%F0%9F%87%A6%F0%9F%87%AA-nubknlau-tpbvyzw1
http://46.38.137.141:2096/sub/eyovzx7b813yvs6g
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5678" target="_blank">📅 21:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کانفیگ های اهدایی یکی از ممبرای عزیز
❤️
حجم ۲۰۰ گیگ
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@sv2.vaslimgroup.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-asli-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@snapp.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%92%9Asnapp%F0%9F%92%9A-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@tapsi.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%A9%B7tapsi%F0%9F%A9%B7-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@anten.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%94%B1anten%F0%9F%94%B1-200.00GB%F0%9F%93%8A
هر ۷ تا رو اد کنید ، بعضی مناطق بعضی هاشون کار میده
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5677" target="_blank">📅 21:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پروکسی اهدایی یکی از ممبرای عزیز
❤️
https://t.me/proxy?server=hh87.salarjavidan.online&port=8991&secret=f41d30c2e0ca3895ca053b26d98af5b3
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5676" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚀
معرفی فیلترشکن جدید و هوشمند Defyx VPN (نسخه v5.3.9)
---
امشب قصد دارم یک فیلترشکن متن‌باز (Open-Source) و بسیار قدرتمند به اسم
Defyx VPN
رو بهتون معرفی کنم که آپدیت جدیدش به تازگی در گیت‌هاب منتشر شده.
این اپلیکیشن رابط کاربری فوق‌العاده تمیز و ساده‌ای داره و بزرگترین مزیتش اینه که
نیازی به هیچ‌گونه تنظیمات دستی یا وارد کردن کانفیگ نداره!
✨
ویژگی‌های کلیدی Defyx:
🔸
هسته قدرتمند DXcore:
این برنامه در پس‌زمینه، ترکیبی از بهترین پروتکل‌های ضدسانسور دنیا یعنی
Xray, Warp, Psiphon, Outline
و
Warp-in-Warp
رو در خودش جا داده و به صورت هوشمند از اون‌ها استفاده می‌کنه.
🔸
اتصال تک‌کلیکی (One-Tap):
فقط کافیه دکمه اتصال رو بزنید تا خودش بگرده و بهترین مسیر رو برای دور زدن فیلترینگ پیدا کنه.
🔸
ابزار تست سرعت:
دارای اسپیدتست داخلی برای بررسی کیفیت و پینگ اینترنت شماست.
🔸
پشتیبانی کامل:
برای اندروید، آیفون، مک و ویندوز در دسترسه.
---
📥
لینک‌های دانلود رسمی:
🤖
برای اندروید:
🔗
[دانلود مستقیم از گوگل پلی](
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
)
🔗
[دانلود فایل APK از گیت‌هاب](
https://github.com/UnboundTechCo/defyxVPN/releases/download/v5.3.9/app-release.apk
)
🍎
برای آیفون، آیپد و مک (iOS/macOS):
🔗
[دانلود مستقیم از اپ استور](
https://apps.apple.com/us/app/defyx/id6746811872
)
💻
برای ویندوز:
🔗
[دانلود مستقیم نسخه پرتابل (بدون نیاز به نصب)](
https://github.com/UnboundTechCo/defyxVPN/releases/download/v5.3.9/windows-release.zip
)
📌
#فیلترشکن
#معرفی_اپلیکیشن
#اندروید
#آیفون
#ویندوز
#Xray
#Warp
#Psiphon
#DefyxVPN
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5675" target="_blank">📅 20:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آب را گل آلود کن و ماهی بگیر از این آب گل آلود...</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5674" target="_blank">📅 20:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqBuNx7TK-QT4T48oBEwLOiptmNU5RV8pcg0p7WjhflbhaWlLxDOPOHVgudwfTciOBByTgAnXVRU7d3sq2ECkKalfOy5NcZpBXEErFkdyhPx59BSrjue2a2La2h3bx7QDHG1yz1TVVRzScknB-HVLg_nax3WOc6QNZi9ABNB4XdMUEVzyjbveiapKRu8ArPttAXQ5wthiriV_MtGJrCN1oyGsp93bz99ioOF-jsybcsJJluzdgCANZReWmnatZBSZxFKhCy2a8AXDMYUoeyEeOPD_qcMy0XzVXl7V00LzGVMcUDon9gFyqEGOkTm1ETxp6itvYBGmyraSQ0uktYosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به عامل کدنویسی هوش مصنوعی خود، یک سیستم طراحی در یک فایل markdown بدهید.
Awesome DESIGN .md
مجموعه‌ای از فایل‌های طراحی است که از وب‌سایت‌های واقعی متمرکز بر توسعه‌دهندگان الهام گرفته شده‌اند. شما یکی از آن‌ها را در پروژه خود قرار می‌دهید، به عامل هوش مصنوعی خود می‌گویید چه چیزی بسازد و از آن فایل به عنوان یک راهنمای سبک بصری استفاده می‌کند.
بدون خروجی Figma. بدون تنظیمات پیچیده. فقط markdown که به عامل می‌گوید رابط کاربری چگونه باید به نظر برسد و چه احساسی داشته باشد.
https://github.com/VoltAgent/awesome-design-md
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/5673" target="_blank">📅 19:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نانوبنانا پرو رایگان می‌خوای؟
بفرمایید اینم یه ابزار خفن از گوگل:
https://labs.google/fx/tools/flow
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5669" target="_blank">📅 17:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مخابرات و همراه اول وصل
Windscribe
TCP, 443, Paris Seine
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/5667" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5666">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">اکسپرس برلین آلمان سوپر وصله</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5666" target="_blank">📅 17:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ykr2Z7iEB6tWL7E7YdiEkVqmeKkJ7bTLxxoq721ouvY2oKVPVftAB2H6xzem4BdkgC9AtwKecTrNrEAkyxFiD3qc26iQBArgQB2t_L4vKJjjd4Pc2YvqUjqJ9HY2jPT9XUA_r4YaKBRgb68oumUTvLjEmcCU09JRRkJt5oN_fjqVPHPxw6hJ-bT8PhCXtxuo_3tq8D2w97TS6UrTECjkq-pgyBIS4DtatFt6seipMAEMINEgrduou_6E3NXpwlYNtWzvfzBxCCIyKIts8eDMBi0UoFzvQOmhVt7dJcc5r13mtNVYlHwz9mgGzlLuOt4dBAQyEua2eYcnZc2h9xJyXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5XsYFJ71_ZQDr9pn5WEvQMGmN7Tbx58GHLdA3g8H2ZdDAhSkpD_dn0tnrFsMKJ-_YYpEhj1FFWLS1O3PmWo4jhENzWyyfKjWKNLZ2UMncSWrTHB4AHC9yxaLlgLrtC9Av1LGQwXg3aCkpA3BJnXYrpFPXu829cQFEyGqiK--ZrbskACZaWWZUC_U8OUdkY3faGlNIx35Tyv2eBwxUAWDYE9GdUL5j7EiBqiFmgOT_bBDvuimqb0YRwgnuKsnYjIsZje1-SOeQYrsyCKhx-aazhJY5KNLLiNlZx21XZRaVxE0E3psJdcuD-PKJviZ7IPcsWpOdeRVXqnKsYcUoMujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3GjyooJQkG3E5mHTLSJ3KkF3Ff-9tt0w5p562sllTpymh4kLDfeQemka7q78SPnDWYPvJsGBgu3a0XWftKv1W1nsW5KPh29_u6CN8MJGjRM7H23ut5V4QWhBOR3fF7O5otXrGMm7yDiKRMy2cDX1JeCw_Gxnk4q6a0LuPpBtmQrSS3EsRso2BF-XgrKSrJZQdxoUpn4fGiFNfVHwDYZMVXRh0rPMKdAdMeaQjYYKH3PVlmPrOvgW6SgSgSItsOLkCRzrdPVSeINB59zDJqay_C9GOiRICioYRGA4VQx5nR_M7K_Pt78TPSihd91Fe4K8bmEpECLp7xxbLtn-wuqlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر هنوز دسترسی به اینترنت جهانی براتون باز نشده و مجبورید از DNS Tunelling استفاده کنید:
با قابلیت جدید DNS Pool دیگه نیازی نیست دستی دنبال DNS بگردید یا اسکن کنید. می‌تونید تا ۱۰۰۰ تا DNS به برنامه بدید تا خودش قبل اتصال تستشون کنه و ۱۰ تا از بهترین‌ها رو خودکار براتون انتخاب کنه.
🕊
@slipnet_app</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5663" target="_blank">📅 17:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5662">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مسئله فقط اینترنت نبود
ما را از جهان در حال حرکت جا گذاشتند
صدا ها خاموش شد ، آدم ها فراموش شدند
و گل هایمان یکی یکی پر پر شدند
زخم این دوران هیچ وقت از دل ما پاک نمی شود..
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/5662" target="_blank">📅 16:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">برای گرفتن 15 گیگ برای اکانت ویندتون باید اول ایمیلتون رو تایید کنین با اینکار 10 گیگ بهتون میده
🆓
برای 5 گیگ اضافه باید توی سایتش لاگین کنید Tweet 4 Data این گزینه رو پیدا کنین یه توییت بزنین براش منشن کنین و تمام 5 گیگ دیگه هم براتون فعال میشه
👑
👥
موقع ثبت نام، اینو بزنین ی گیگ اضافی هم به شما اضافه میشه
Declinedrice
⛈
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/archivetell/5661" target="_blank">📅 15:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjYw8LfXibegk9z1jEhvQ2zcKVks7NfV1FsQoAmlApCLzbUgWMOCkh-BF1WX3H-DpVGM0jggy8me9t9kgmc37YxqQ_TNSACvvxJrH19usOH0MeC46u3hOJPHZ-VrETFF0inj7h3jsCqq5E2ZMSORtdkS0ioctknXXDkuwkW8NO2WAsawwwTFSiNeJ1aHiBy4OBQJkd_FKOdOoolUj6XathGgEHKepSPT3nSZfRM_t1Ccww9_uotKOqiAmOCHItod0Ot1KWF3vjoe6J8Naxkjo4J7XyjstHgy6pFkbWXgPY6VqTD0Z5IXBxmZvGpRabh2OXciI_HUMEJpPDMeh7UWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugDq3VZXzKM6ezP5Ss_BYBVGNzrrU0K1a1YfTbwSSIa23qtigpsVsnEoBqAUxGcac7fNnrsfhAp0KTUxmuA6mXOuZeztUEUv-sR6HIlQh02yjjKahUjHya0jW9wG9YQ6vSdYoCgt290oHJW-Xr144iOe3mxeyKBvUsLDIM5rAzNFlNpwJdSQ4miIRyJgDsZqwC3jwYwfJdzZP7dpIUdWhyMJXwWcjdF5atNTwvwSzug-2aOdqJjDrIvcmECjCmAvFpc3gmFqJ_QJyW_5A-XqARgyDoKKOcOLJy-VULmWgr8aDAOPxaNs6eG_Ju0tncV04E2tQWJyP0LgRSmx91u6dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینداسکرایب روی همراه آخر روی Tcp پورت 443 وصله
🛜
از تنظیمات قسمت
connection
بخش
Anti censorship
باید
Protocol tweaks
رو
Enabled
کنین و یکی از گزینه های
iran experimental
رو انتخاب کنین
✅
تیک
Large Tls
رو هم بزنین
حالا کافیه روی tcp 443 رو هر کشوری که میخواید کانکت شید
🧬
✈️
@Archivetell</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/archivetell/5659" target="_blank">📅 14:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🛠
معرفی جعبه‌ابزار قدرتمند cfray: همه‌چیز برای VLESS و Cloudflare در یک فایل!  ---  رفقا سلام!
✋
امروز یک ابزار پایتونیِ به شدت کاربردی و جذاب به اسم cfray (ساخته‌شده توسط تیم SamNet) رو بهتون معرفی می‌کنیم.  این ابزار که قبلاً فقط یک اسکنر کانفیگ بود، حالا…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5658" target="_blank">📅 14:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🛠
معرفی جعبه‌ابزار قدرتمند cfray: همه‌چیز برای VLESS و Cloudflare در یک فایل!
---
رفقا سلام!
✋
امروز یک ابزار پایتونیِ به شدت کاربردی و جذاب به اسم
cfray
(ساخته‌شده توسط تیم SamNet) رو بهتون معرفی می‌کنیم.
این ابزار که قبلاً فقط یک اسکنر کانفیگ بود، حالا در نسخه ۱.۱ تبدیل به یک "چاقوی سوئیسی" همه‌کاره برای دور زدن فیلترینگ و مدیریت سرورهای Xray شده.
💡
بهترین ویژگیش چیه؟
این برنامه هیچ پیش‌نیازی (Dependency) نداره! فقط پایتون 3.8 به بالا روی ویندوز یا لینوکس نیازه و تمام کارها رو با یک فایل
scanner.py
انجام میده.
✨
قابلیت‌های اصلی و جذاب cfray:
🔸
اسکنر کانفیگ و IP تمیز (Clean IP Finder):
دیگه نیازی نیست دنبال آی‌پی‌های تمیز بگردید. این ابزار می‌تونه کل رنج آی‌پی‌های کلادفلر (حدود ۱.۵ تا ۳ میلیون پروب) رو اسکن کنه، آی‌پی‌های سالم و با پینگ خوب رو پیدا کنه و مستقیماً روی کانفیگ‌های شما جایگزین (Swap) و تست سرعت کنه.
🔸
تست پایپلاین Xray (Xray Pipeline Test):
کانفیگتون وصل نمیشه یا توسط DPI مسدود شده؟ این قابلیت یه کانفیگ از شما می‌گیره و بهترین ترکیب از "آی‌پی تمیز + تنظیمات فرگمنت (Fragment) + دامنه‌های استتاری (SNI)" رو برای دور زدن فیلترینگ پیدا می‌کنه!
🔸
نصب و دیپلوی سرور Xray در ۲ دقیقه:
اگه یه سرور مجازی (VPS) خام دارید، کافیه این اسکریپت رو اجرا کنید. خودش Xray-core رو نصب می‌کنه، تنظیمات (TCP/WS/REALITY/TLS) رو انجام میده و کانفیگ آماده استفاده بهتون تحویل میده.
🔸
ساخت پروکسی ورکر (Worker Proxy):
اگه دامنه (SNI) کانفیگتون مسدود شده، این ابزار براتون یه اسکریپت Cloudflare Worker می‌سازه تا ترافیک رو از طریق دامنه‌های تمیزِ
workers.dev
به سرورتون منتقل کنید.
🔸
پنل مدیریت اتصالات (Connection Manager):
بدون نیاز به پنل‌های سنگین تحت وب، می‌تونید از طریق همین ابزار داخل محیط ترمینال، کاربر جدید بسازید، اینباند اضافه کنید یا کانفیگ‌ها رو مدیریت کنید.
---
💻
نحوه نصب و راه‌اندازی (بسیار ساده):
کافیه سورس برنامه رو از گیت‌هاب دانلود کرده و فایل پایتون رو اجرا کنید تا یک محیط گرافیکی و تعاملی (TUI) براتون باز بشه:
۱. دریافت از گیت‌هاب:
git clone https://github.com/SamNet-dev/cfray.git
cd cfray
۲. اجرای ابزار:
python3 scanner.py
✅
حالا منو براتون باز میشه و می‌تونید با فشردن کلیدهای میانبر، کارهایی مثل پیدا کردن آی‌پی تمیز (کلید F)، نصب سرور (کلید D) یا مدیریت کانفیگ‌ها (کلید C) رو انجام بدید.
🔗
لینک پروژه و آموزش کامل در گیت‌هاب:
🌐
https://github.com/SamNet-dev/cfray
📌
#آموزش
#معرفی_ابزار
#سرور
#کلادفلر
#Cloudflare
#Xray
#VLESS
#تونل
#اسکنر
#Bypass
#پایتون
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5657" target="_blank">📅 14:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac73908c6d.mp4?token=rHyJmytMPWEdLCBptJ5lV8mTVek0Dvb3dv9ViHuokOfDHfCjEuGgUD8s-LCpLZucN1wlS5Fbv4RRJ215xV_W-Omk3fNL5NjpsFe9xwqWpDuwXALVw2W8L0ul2OHmKM0z_N_vH2xE_T60PHyxJ6YPNZhYy576tlKdKwO8ZoHFtzYIrN1RdSwYVRlswJ7rk5kgwTPyu5m7oE-Sg5RqpU8I0rJSX6hIDhkN3SK4YoIJM605vurY8bLao6FkoEGFe7bzJwr1hmdK-9xtHBl9rbcYmr10jc9sTUCuRpvMkCO3iBWa5-tuz-QzHOT5QKyTDAaZ7dq56gPqtIL7f8W8UMzEUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac73908c6d.mp4?token=rHyJmytMPWEdLCBptJ5lV8mTVek0Dvb3dv9ViHuokOfDHfCjEuGgUD8s-LCpLZucN1wlS5Fbv4RRJ215xV_W-Omk3fNL5NjpsFe9xwqWpDuwXALVw2W8L0ul2OHmKM0z_N_vH2xE_T60PHyxJ6YPNZhYy576tlKdKwO8ZoHFtzYIrN1RdSwYVRlswJ7rk5kgwTPyu5m7oE-Sg5RqpU8I0rJSX6hIDhkN3SK4YoIJM605vurY8bLao6FkoEGFe7bzJwr1hmdK-9xtHBl9rbcYmr10jc9sTUCuRpvMkCO3iBWa5-tuz-QzHOT5QKyTDAaZ7dq56gPqtIL7f8W8UMzEUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧠
در GitHub پلاگینی به نام agentmemory محبوب شده است که به عوامل هوش مصنوعی حافظه «بی‌نهایت» اضافه می‌کند — این پلاگین تمام زمینه‌های جلسات، اقدامات و پروژه‌های شما را در یک پایگاه ذخیره می‌کند.
• به ۱۶ عامل هوش مصنوعی از جمله Claude Code، Codex و Cursor متصل می‌شود.
• تمام اقدامات آن‌ها را ذخیره می‌کند، به خاطرات فشرده تبدیل می‌کند و به‌طور خودکار در آینده آن‌ها را پیدا می‌کند.
• دیگر نیازی نیست هر بار زمینه را توضیح دهید — عامل همه جزئیات را به خاطر می‌سپارد.
در نتیجه، می‌توان تا ۹۵٪ از توکن‌هایی که معمولاً برای توضیح زمینه صرف می‌شوند را در هر جلسه صرفه‌جویی کرد.
https://github.com/rohitg00/agentmemory
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/archivetell/5651" target="_blank">📅 09:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانفیگ اهدایی
تشکر از
@thee_LaShi
بابت این کانفیگای ناب
❤️
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@tr-in.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=tr-in.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5650" target="_blank">📅 08:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانفیگ اهدایی
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@ninka.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=ninka.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5649" target="_blank">📅 08:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فیلترچی ری اکشن فیک بزن تا بسوزی
😁</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/5648" target="_blank">📅 08:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5647">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پخش کنید بقیه هم وصل بشن
😁</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5647" target="_blank">📅 08:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کانفیگ اهدایی
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@tr-in.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=tr-in.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5646" target="_blank">📅 08:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5645">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کانفیگ اهدایی
vless://0468a043-e12c-466e-881c-7d685c1b3950@roz1r.skystreamgame.com:8443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QHkXBS2ENHV0khgY9VBYi8_9bpfqnUYDcfQN4cW5Qg0&security=reality&sid=4326&sni=roz1r.skystreamgame.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/archivetell/5645" target="_blank">📅 08:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانفیگ اهدایی یکی از ممبرای عزیز
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@fishsea.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=0a6ba2716a409da6&sni=fishsea.api.dznn.net&type=tcp#@archivetell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/archivetell/5644" target="_blank">📅 08:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانفیگ اهدایی یکی از ممبرای عزیز
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@fishsea.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=0a6ba2716a409da6&sni=fishsea.api.dznn.net&type=tcp#@archivetell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5643" target="_blank">📅 08:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">windscribe_auto_hand .zip</div>
  <div class="tg-doc-extra">12.4 MB</div>
</div>
<a href="https://t.me/archivetell/5642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل اتوماتیک سازی فرایند جست‌وجو لوکیشن برنامه ویندسکرایب فقط نسخه ویندوز  با تشکر از چنل
@windscribe_auto_hand
که زحمت کشیدن کد نویسی این برنامه رو انجام دادن
❤️‍🔥
#windscribe
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/archivetell/5642" target="_blank">📅 02:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5641">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅️
خب از اونجایی که بعضی از پروتکل های ویندسکرایب باز شدن براتون یه اموزش و فایل رو میزارم که فقط مخصوص نسخه ویندوز هست
طبق این این اموزش جلو برید  و تک تک مراحل رو انجامش بدید :
کد exe اتوماتیک سازی فرایند جست‌وجو لوکیشن ویندسکرایب
مخصوص ویندوز
این کد به گونه ای نوشته شده که حتی موقعی که API وینداسکرایب کانکشن نمیده هم وصل بشه
⭕️
نحوه استفاده
اول وینداسکرایب رو باز میکنید
پروتکل و پورت مد نظرتون رو انتخاب کنید
بعد برنامه exe رو اجرا میکنید
وقتی اجرا کردید بلافاصله یه جایی رو windscribe کلیک کنید
حالا کد خودش شروع میکنه همه لوکشین هارو تست میکنه
اگر وصل شد توی پوشه logs تو فایل text مینویسه
تو این فرایند قهوه بنوشید و صبر کنید تا تموم بشه
امیدوارم به کارتون بیاد
❤️
با تشکر از چنل دوستمون
@windscribe_auto_hand
❤️‍🔥
که این اسکریپت رو واقعا زحمت کشیدن نوشتن و تو چنل قرار دادن اون زمان چون ایران اینترنتش اکسس بود قابل استفاده نبود ولی الان میتونید استفاده کنید
⚠️
نکته مهم : وینداسکرایب همچنان روی متد کار میکنن و باهاشون حرف زدم با اینکه اینترنت کمی محدودیت هاش رفته و باز کامل نیست
از پروژه دست نکشیدن و قراره نسخه نهایی رو یکدفعه release کنند که اگه یه زمان دوباره مشکلی پیش اومد همیشه این متد برای ایرانی ها قابل استفاده باشه
با تشکر از تیم ویندسکرایب که خیلی تلاش دارن میکنن نسخه نهایی رو بدون مشکل بسازن
🔥
🤌
#windscribe
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/archivetell/5641" target="_blank">📅 02:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">FileShare.exe</div>
  <div class="tg-doc-extra">48.6 MB</div>
</div>
<a href="https://t.me/archivetell/5638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
انتشار نسخه جدید File Share v1.2
توی این آپدیت کلی تغییر و بهبود اضافه شده:
✅
امکان انتخاب پوشه اختصاصی برای اشتراک‌گذاری فایل
کاربر حالا می‌تونه هر پوشه‌ای رو برای اشتراک در شبکه محلی انتخاب کنه.
✅
اضافه شدن آیکون اختصاصی برنامه
از نسخه 1.2 برنامه ظاهر حرفه‌ای‌تری گرفته.
✅
جایگزینی پنل ویندوزی به جای محیط ترمینال
رابط کاربری ساده‌تر و کاربرپسندتر شده.
✅
رفع باگ‌ها و بهبود عملکرد
پایداری و سرعت برنامه بهتر شده.
📡
File Share یه ابزار انتقال فایل تحت شبکه محلیه که بدون اینترنت کار می‌کنه.
کافیه کاربر دوم IP سیستم رو داخل مرورگر وارد کنه تا از طریق محیط وب:
⬇️
دانلود فایل
⬆️
آپلود فایل
💬
تبادل پیام بین دستگاه‌ها
به‌صورت کاملاً آفلاین و داخل شبکه محلی انجام بشه.
🛠
همچنین پروژه روی GitHub قرار گرفته تا به‌صورت Open Source در دسترس همه باشه و سورس کدها برای توسعه، بررسی و مشارکت در اختیار همگان قرار بگیره.
لینک گیت هاب پروژه</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/archivetell/5638" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b370928a6c.mp4?token=HL1qiLwb74U3WtteKFks9NCd-63mvs_2uxXp-AUqQZPUflMy-PvxUqdjf7_0W71vM4TJYR4zTc4LFIHNFapv7ZpqOHIogrQlQSliNP8YxXWDfeSAcoNdOrRNmXlZ7D8rErhpGQZNuhqkWaFzfQ2K-t4nQCvV3ExOMSZBPec_EPGNH3SO7k4CyzXKtRZgkNPK24PJ1hCAazGfV1vy9VNKJKSC0z62z18qzNH36DlR0xHhhQH2RCpBjfM4wkk0iiHkWdWiHsqVLJO4WS1cCxm4TcKZYt0vqMrJ1_0YiImtxRbvSFKe4I0JAAXRUzXi4jobGVV6rY-D01mytWQqrug4Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b370928a6c.mp4?token=HL1qiLwb74U3WtteKFks9NCd-63mvs_2uxXp-AUqQZPUflMy-PvxUqdjf7_0W71vM4TJYR4zTc4LFIHNFapv7ZpqOHIogrQlQSliNP8YxXWDfeSAcoNdOrRNmXlZ7D8rErhpGQZNuhqkWaFzfQ2K-t4nQCvV3ExOMSZBPec_EPGNH3SO7k4CyzXKtRZgkNPK24PJ1hCAazGfV1vy9VNKJKSC0z62z18qzNH36DlR0xHhhQH2RCpBjfM4wkk0iiHkWdWiHsqVLJO4WS1cCxm4TcKZYt0vqMrJ1_0YiImtxRbvSFKe4I0JAAXRUzXi4jobGVV6rY-D01mytWQqrug4Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاربران ChatGPT اکنون می‌توانند مستقیماً از طریق چت برنامه‌های واقعی بسازند
فروشگاه برنامه ChatGPT
به تازگی
AppDeploy
را اضافه کرده است و این قابلیت برای حساب‌های رایگان نیز فعال است.
توضیح دهید که چه چیزی می‌خواهید بسازید، ChatGPT کد را می‌نویسد، AppDeploy به طور خودکار در همان چت استقرار را انجام می‌دهد و بلافاصله یک لینک کارآمد به شما بازمی‌گرداند.
رایگان برای استفاده. نیاز به اشتراک یا کارت اعتباری نیست.
👉
نصب AppDeploy در ChatGPT
و راه‌اندازی اولین برنامه خود در چند دقیقه
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/archivetell/5637" target="_blank">📅 00:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گوگل پلی رفع فیلتر شده..</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/archivetell/5636" target="_blank">📅 23:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گوگل پلی رفع فیلتر شده..</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5635" target="_blank">📅 23:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ربات جدید تبدیل لینک به فایل
@url_uploder_nrbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/archivetell/5634" target="_blank">📅 23:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fb4063f0.mp4?token=IASTqfWyKbYJL16hZbGcukbWsB0pLc96-4tvTC2cRJb7ygpWPHXQOcBdhFxMbyPwTv9RtnBc1Swp1uavC4egyAR2GHMs3pYc_3Olnp_CPZc2NitsCPw1rk0KpTPN73OGCVL-vlzbqEBA2YT0aKsdu4ntJ2Xf7To3bW6_tjJ4FrfBycCUHW-x5sK3rHC5RND3_gb3-NKOn00Zcw51SFzEtUAelUt8T8bZN7EaiiVCoTjQr0jhvXNkjk-clj1iYxBMVgFbeeemL_ecn5ql2lmnsp8qWZTSQtGcTHzvudD6jMFm_-9Pk17_qfDVfGNbpPx5vsHuLGFdvyezle9z_QJp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fb4063f0.mp4?token=IASTqfWyKbYJL16hZbGcukbWsB0pLc96-4tvTC2cRJb7ygpWPHXQOcBdhFxMbyPwTv9RtnBc1Swp1uavC4egyAR2GHMs3pYc_3Olnp_CPZc2NitsCPw1rk0KpTPN73OGCVL-vlzbqEBA2YT0aKsdu4ntJ2Xf7To3bW6_tjJ4FrfBycCUHW-x5sK3rHC5RND3_gb3-NKOn00Zcw51SFzEtUAelUt8T8bZN7EaiiVCoTjQr0jhvXNkjk-clj1iYxBMVgFbeeemL_ecn5ql2lmnsp8qWZTSQtGcTHzvudD6jMFm_-9Pk17_qfDVfGNbpPx5vsHuLGFdvyezle9z_QJp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک مجموعه برتر از انیمیشن‌های رابط کاربری وب برای طراحان رابط کاربری که تمایلی به صرف زمان در ایجاد انیمیشن‌ها از پایه ندارند
https://transitions.dev/
این مجموعه شامل انیمیشن‌های آماده‌ای برای کارت‌ها، منوها، فهرست‌ها و کلیدهای تغییر وضعیت می‌باشد.
امکان بررسی مستقیم انیمیشن‌ها در وب‌سایت پیش از بهره‌برداری فراهم است.
ادغام در پروژه‌های فرانت‌اند واقعی به سادگی امکان‌پذیر است.
پشتیبانی از ادغام به عنوان یک قابلیت برای عوامل هوش مصنوعی ارائه می‌گردد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/archivetell/5633" target="_blank">📅 22:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121da40c06.mp4?token=NEe-VstTyVV2L1JVGlXWwR2lStbv1JYfzTESZaoGr29rodpbcMPcOqxnTPv2JUBs9oaSG-HhhIGbbulpXJflj7zXbkj00tZJ9HV5a1seJdnnbC9d-4rEHag-ZqP3mCbSe59pi-83BDOJmhnUUdcwNYXz6odhiZo1VqbX_MGp-uYfLOWrKrAur5-7wCeO0BfDEPpOiZbNLqZemE-x1VvFmKjJMOQQEun8rB8q4lQ10wC2XEzJRJPMK0ze8sdY4otEUppkpxCQ2m0wRut-4dkqAAh3M9oEmUCCUkfsOZO7ROS24qX-hJWK0LdtNSTfaAlrEBIGHyE4JECrjLJU7orOEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121da40c06.mp4?token=NEe-VstTyVV2L1JVGlXWwR2lStbv1JYfzTESZaoGr29rodpbcMPcOqxnTPv2JUBs9oaSG-HhhIGbbulpXJflj7zXbkj00tZJ9HV5a1seJdnnbC9d-4rEHag-ZqP3mCbSe59pi-83BDOJmhnUUdcwNYXz6odhiZo1VqbX_MGp-uYfLOWrKrAur5-7wCeO0BfDEPpOiZbNLqZemE-x1VvFmKjJMOQQEun8rB8q4lQ10wC2XEzJRJPMK0ze8sdY4otEUppkpxCQ2m0wRut-4dkqAAh3M9oEmUCCUkfsOZO7ROS24qX-hJWK0LdtNSTfaAlrEBIGHyE4JECrjLJU7orOEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎹
سونو را دور می‌اندازیم — ElevenLabs نسخه Music V2 را عرضه کرده است. توسعه‌دهندگان این را بزرگ‌ترین به‌روزرسانی شبکه عصبی موسیقی تا به امروز می‌نامند.
https://elevenlabs.io/music
🕤
تولید ووکال، ابزارها و آرنجمنت‌ها در همه ژانرها به طور قابل توجهی قدرتمندتر شده است.
🕤
سبک آهنگ را می‌توان در حین پخش تغییر داد.
🕤
هر بخش از آهنگ به طور جداگانه ویرایش می‌شود — ثانیه مورد نظر را انتخاب کرده و فقط آن را بازتولید می‌کنید.
🕤
پشتیبانی از رفرنس‌ها: می‌توانید صدا، متن، ژانر یا پرامپت معمولی بارگذاری کنید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/archivetell/5632" target="_blank">📅 22:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانفیگ پرسرعت
ایپی استاتیک کره شمالی
جهت سفارش پی‌وی
🐱</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/archivetell/5631" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شما می‌توانید Llama 4، Qwen3، Gemma 4 را اجرا کنید — همه رایگان، همه خصوصی، روی لپ‌تاپ خودتان.
🖥️
⚡
این همان Ollama است.
🔗
ollama.com
این یک ابزار رایگان است که به شما اجازه می‌دهد مدل‌های قدرتمند هوش مصنوعی متن‌باز را به صورت محلی اجرا کنید — بدون نیاز به اینترنت، بدون هزینه API، بدون خروج داده‌ها از دستگاه شما.
فقط دانلود کنید، یک مدل بکشید و شروع به گفتگو کنید.
چرا مردم واقعاً از آن استفاده می‌کنند:
→ بدون هزینه‌های ابری
→ کاملاً خصوصی — داده‌های شما هرگز از دستگاهتان خارج نمی‌شود
→ به صورت آفلاین کار می‌کند
→ مدل‌هایی مانند DeepSeek-R1، Llama 4، Qwen3، Gemma 4 را اجرا می‌کند
نسخه ۲۰۲۶ اکنون شامل یک رابط کاربری دسکتاپ داخلی، شتاب‌دهی Apple Silicon از طریق MLX، و پشتیبانی ابری برای مدل‌های بزرگ‌تر است — همه در یک رابط کاربری تمیز.
اگر برای اشتراک‌های هوش مصنوعی هزینه می‌پردازید و هیچ کار حساسی با داده‌هایتان انجام نمی‌دهید... Ollama ارزش ۱۰ دقیقه وقت شما را دارد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/archivetell/5630" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎁
دریافت یک سال اشتراک پرمیوم RoboForm (رایگان)
---
رفقا سلام!
✋
یه آفر فوق‌العاده و محدود داریم. پسورد منیجرِ معروف، امن و پرطرفدار
RoboForm
، به کاربراش
۱۲ ماه اشتراک پرمیوم کاملاً رایگان
(به ارزش حدود ۳۰ دلار) میده.
اگر هنوز از یه ابزار مدیریت پسورد خوب برای ذخیره امنِ رمزها، قابلیت اتوفیل (Autofill) و همگام‌سازی بین گوشی و لپ‌تاپ استفاده نمی‌کنید، الان بهترین فرصته.
💻
مراحل دریافت اشتراک:
۱. وارد لینکِ آفر در پایین پست بشید.
۲. ایمیل خودتون رو وارد کنید و روی دکمه
Redeem Offer
کلیک کنید.
۳. مراحل ثبت‌نام و فعال‌سازی اکانت رو انجام بدید.
✅
تمام! اشتراک یک‌ساله پرمیوم به صورت خودکار روی اکانتتون فعال میشه.
⚠️
نکات مهم این آفر:
-
💳
بدون نیاز به کردیت کارت:
برای فعال‌سازی اصلاً نیازی به وارد کردن اطلاعات پرداخت یا کارت بانکی نیست.
-
🆕
کاربران جدید:
این آفر فقط برای اکانت‌ها و کاربرانی هست که تا حالا پرمیوم نبودن.
-
⏳
مهلت استفاده:
فقط تا
۳۱ می ۲۰۲۶
(۱۱ خرداد ۱۴۰۵) فرصت دارید این آفر رو دریافت کنید.
🔗
لینک دریافت آفر ویژه روبوفروم:
🌐
https://www.roboform.com/lp?frm=offer-ga
📌
#آفر
#رایگان
#RoboForm
#پسورد_منیجر
#امنیت
#پرمیوم
#کاربردی
#تخفیف
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5629" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">600 گیگ کانفیگ مستقیم متصل همه نتا
اهدایی یکی از ممبرای عزیز
❤️
vless://22768339-9096-48aa-9109-ff28141145b9@roz2r.skystreamgame.com:8443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QHkXBS2ENHV0khgY9VBYi8_9bpfqnUYDcfQN4cW5Qg0&security=reality&sid=4326&sni=roz2r.skystreamgame.com&type=tcp#Aqa.rza
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/archivetell/5628" target="_blank">📅 19:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">kiro.dev
یک ابزار کدنویسی هوش مصنوعی از AWS که فقط کد نمی‌نویسد.
این ابزار کل پروژه شما را از صفر برنامه‌ریزی، طراحی و می‌سازد.
⚡
Free trial with 500 credits
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5627" target="_blank">📅 19:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آیپی تمیز کلودفلر، تست شده روی ایرانسل 104.16.81.122 104.16.81.43 104.16.81.86 104.16.81.12 104.16.81.24 104.16.81.125 104.16.81.40 104.16.81.133 104.16.81.68 104.16.81.101 104.16.81.23 104.16.81.155 104.16.81.112 104.16.81.106 104.16.81.67 104.16.81.82 104.16.81.157…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/archivetell/5625" target="_blank">📅 18:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Defyx VPN  رایتل سرعت بالا  https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn  @ArchiveTell</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/archivetell/5624" target="_blank">📅 18:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آیپی تمیز کلودفلر، تست شده روی ایرانسل
104.16.81.122
104.16.81.43
104.16.81.86
104.16.81.12
104.16.81.24
104.16.81.125
104.16.81.40
104.16.81.133
104.16.81.68
104.16.81.101
104.16.81.23
104.16.81.155
104.16.81.112
104.16.81.106
104.16.81.67
104.16.81.82
104.16.81.157
104.16.81.6
104.16.81.1
104.16.81.110
104.16.81.72
104.16.81.10
104.16.81.16
104.16.81.126
104.16.81.75
104.16.81.53
104.16.81.134
104.16.81.119
104.16.81.156
104.16.81.2
104.16.81.91
104.16.81.45
104.16.81.21
104.16.81.77
104.16.81.73
104.16.81.66
104.16.81.19
104.16.81.32
104.16.81.88
104.16.81.132
104.16.81.74
104.16.81.8
104.16.81.18
104.16.81.121
104.16.81.48
104.16.81.145
104.16.81.51
104.16.81.13
104.16.81.104
104.16.81.80
104.16.81.42
104.16.81.144
104.16.81.111
104.16.81.105
104.16.81.118
104.16.81.117
104.16.81.26
104.16.81.78
104.16.81.159
104.16.81.57
104.16.81.25
104.16.81.60
104.16.81.54
104.16.81.149
104.16.81.136
104.16.81.97
104.16.81.38
104.16.81.90
104.16.81.137
104.16.81.140
104.16.81.59
104.16.81.22
104.16.81.41
104.16.81.150
104.16.81.64
104.16.81.31
104.16.81.33
104.16.81.61
104.16.81.76
104.16.81.69
104.16.81.46
104.16.81.49
104.16.81.35
104.16.81.50
104.16.81.79
104.16.81.34
104.16.81.93
104.16.81.102
104.16.81.129
104.16.81.71
104.16.81.115
104.16.81.92
104.16.81.5
104.16.81.99
104.16.81.84
104.16.81.130
104.16.81.128
104.16.81.47
104.16.81.36
104.16.81.96
104.16.81.9
104.16.81.37
104.16.81.4
104.16.81.124
104.16.81.58
104.16.81.52
104.16.81.55
104.16.81.113
104.16.81.44
104.16.81.65
104.16.81.138
104.16.81.95
104.16.81.29
104.16.81.135
104.16.81.56
104.16.81.108
104.16.81.103</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5623" target="_blank">📅 18:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
مدل بعدی Grok از xAI ممکن است ظرف ۲ تا ۳ هفته آینده عرضه شود
👀
⚡
گزارش‌ها حاکی از آن است که مدل جدید ممکن است از مدل پایه بسیار بزرگ‌تر ۱.۵ تریلیون پارامتری V9-Medium استفاده کند که جهش عظیمی نسبت به معماری ۰.۵ تریلیون پارامتری V8-Small در Grok 4.3 است.
جزئیات جالب دیگر:
گفته می‌شود داده‌های کدنویسی Cursor برای آموزش اضافی استفاده می‌شود.
Grok5؟
👀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5622" target="_blank">📅 18:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#اختصاصی
🌐
دامنه‌های رایگان برای هر پروژه‌ای
https://github.com/DigitalPlatDev/FreeDomain
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5621" target="_blank">📅 18:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgYgI7swu00yOoiUdoCOkWlmXnXIjJ-0EAiEOl3jKRhVo2pufbhbsskuypaInOMKlAHIA4n-u_fdjhjbF1EcJPCvVSg2SLjHOeVOolx61ePJGnzcDqB7mAyBZAOo8hEN4XqmOD90XOmcCGJ36mh2Rxvz1g9jC6d4wWh3abbrhNATqjK2ZZ-iQNMlVM4f1zMosJxTVRFx_7PxY7dr8pvGlIaoJIGlbaX4kh5iTaQHKQw9GlRyH9T1Rp4-1Q7S98Ke1mUQEsYAQNfRIXS1f8N7MamVfRMFCUg32ZA2llqQVJQk0a1WJ2rGiPF8sP-bFyLYZwXRx9M-jmcSW1b8iwR3LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Defyx VPN  رایتل سرعت بالا  https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn  @ArchiveTell</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/archivetell/5620" target="_blank">📅 17:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">Defyx VPN
رایتل سرعت بالا
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5619" target="_blank">📅 17:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5618">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">configs.txt</div>
  <div class="tg-doc-extra">195.4 KB</div>
</div>
<a href="https://t.me/archivetell/5618" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دوستان میتونین با Hiddify روی سرور های رایگانش وصل بشید یا از گیت هاب بگردین دنبال ساب بندازین داخلش
👋
**میتونین داخل Github هم بگردین ساب های مختلف و وارد اپ کنین و تست بگیرید
👍
لینک دانلود داخلی Hiddify
👋
💀
@archivetell</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/archivetell/5618" target="_blank">📅 16:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5617">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAQRnMpGTeRCFBaHKtWW8wOv7tSVQnVS3Ft7VqeJodSFfCOS4RwtYVJJ4nTcFvoyLfxG7Ntgx8QjcyZ2kRI0J3TfSrn1fdneDWvd8a6QYmS-NZSuXgMlyM_-0QKH7FdB5pL9n7I7PPDbVUFh6-vjI0lYXAr6VMY2yV7XlXZ41SVCUgRaV3qsixPe0oq0FnzpD3e1oMfRUxuRzmvPs8PUpFTu4b2JflyW2DhfUXQKLnybFANliSpfQwXMtomWZmuZsW6I-_KhhhBgSNO4-gmPEEXfwusoBpIM4gN8NtLxI4NW3XYiZSpi99CULqJ-LiYJvEv_aZjJ881Y4myZJPg2cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان میتونین با Hiddify روی سرور های رایگانش وصل بشید یا از گیت هاب بگردین دنبال ساب بندازین داخلش
👋
**میتونین داخل Github هم بگردین ساب های مختلف و وارد اپ کنین و تست بگیرید
👍
لینک دانلود داخلی Hiddify
👋
💀
@archivetell</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/archivetell/5617" target="_blank">📅 16:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/archivetell/5616" target="_blank">📅 15:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAmzFk_5WNqt9WFQcXavErS9SkFB6RaWjDiYHn_Mkxa0DGTd1IZnHsmeoRPYOCQ4m6o-QH_2ZobGNxZLpFru4YCzIkfCI12rzHZ8oAkVZY5AI15IJOCMuLAOZtNSauRLKb9n_MIRrkHpKx-ENj_C1gu2eNXxJ9A-z7b7JND4Y_P2uNs94M5XQVLPF05N0QFNuC2gzozue4kmCcaFZlyAme1sc6-B2ooEnhHDhIWQcLSnHX9Z59P8tm_qchanJjZppedSKzlvkBW75SRDMqf9VasE659cadpopSyYfJYa2Qf1KM5lnjK9kk6vq5u0lmkwBFACI78_tznLabDfl55Kdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">162.159.192.1
162.159.193.3
162.159.195.1
برای وارپ وایرگارد با این آیپی وصل شدم.
پینگ می ده، لوکیش ایران می زنه
😂
ولی تلگرامم الا بالاس دارم باهاش پیام می دم.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/archivetell/5615" target="_blank">📅 13:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">در کل این اپلیکیشن D-Tools خیلی خوبه ولی حیف توسعه داده نمی شه، وگرنه یه اسکنر Google CDN و Cloudflare CDN و Fastly CDN می‌آورد خیلی خوب می شد.</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/archivetell/5613" target="_blank">📅 13:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">در کل این اپلیکیشن D-Tools خیلی خوبه ولی حیف توسعه داده نمی شه، وگرنه یه اسکنر Google CDN و Cloudflare CDN و Fastly CDN می‌آورد خیلی خوب می شد.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/archivetell/5612" target="_blank">📅 13:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKnNH-eorDrQblKlcnAAKQISfitDkHwAgmTt6ADpv3q5PrUZg96NalEBxrIeh10CQ_N1H6iDHOAE9T0BW9ptGvTCUFidXIHFU-8zGP4Vd9l05Z5pM0su3EhaeRm7TBIN0zJ8MitVaP-MJTQy2EWtGBr2jfUpRhcfXSALxQlNUTP6Mdp1fN4r7JUyVjJyaw3aMapwNgw9d0pdie9zvo0V0mJj21i5-iPSxYTvwKZ9YKWv2YVWuLpU6MtG3TcTaUcQA2JlN0fzYL7YxBSlVZ43Eys-_-Qx7HLhmYzoyc5L5mSK1MA2JhoBtYioG7V5ivQxCMLmTeYDi233KwXX5PRYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ساختن وارپ به این نیاز نیستا.  کانتریبیوتر v2ray، یک ریپو داره به اسم D-Tools. اپلیکیشن از پلی استور حذف شده ولی توی اینترنت پیدا می شه به شکل xapk. بدون سرور مجازی براتون کانفیگ warp می سازه.  {   "local_address": [     "172.16.0.2/32",     "2606:47…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5611" target="_blank">📅 13:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">D-Tools_0.0.6_apkcombo.com.xapk</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/archivetell/5610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینم فایل اپلیکیشنش.
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/5610" target="_blank">📅 13:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_JOd5LnMzqiN4zkFUObujEgdtSKtVXr8GJPhIA9saokDqBhSFmySW5cysG6WoI8PRl95rMuyNr_yNUglNjdQ-JXpGvEm7boywgGfSzGEdhJZnUiLdcNlaJ-n4FRZYjt3OMgZSd8xaBq4tj_1enIHGfRnMb_QIDSgYl9lIv8hIHMEX5KGwHzGecIR7MiVsBPB0QQrhkGSkzQnx2UryYmGJbD1OIl6-JfLbYueN-aGwzL08HXd9wr0P8swH3HQX7N8XI3z9rs3NJJ023mOhPRP5ayQ6soiLJANPam-1OMkdj3yfHf7lLDk4cx-hcqBFbh8NabW60pNC8BOl3mvaiDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش ساخت کانفیگ وارپ (نیاز به سرور مجازی )  با استفاده از الگوهای زیر، کانفیگ اختصاصی خودتون رو بسازید :  کانفیگ‌های خام:  warp://licence@ip:port/?ifp=40-80&ifps=50-100&ifpd=2-4&ifpm=m4  warp://licences@ip:port/?ifp=30-60&ifps=50-100&ifpd=3-6&ifpm=m6 برای…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/archivetell/5608" target="_blank">📅 13:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌐
بات تست رایگان بدون رفرال (خرید نزنید)
@Cheap_v2ray_bot</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5607" target="_blank">📅 13:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آموزش ساخت کانفیگ وارپ (نیاز به سرور مجازی )
با استفاده از الگوهای زیر، کانفیگ اختصاصی خودتون رو بسازید :
کانفیگ‌های خام:
warp://licence@ip:port/?ifp=40-80&ifps=50-100&ifpd=2-4&ifpm=m4
warp://licences@ip:port/?ifp=30-60&ifps=50-100&ifpd=3-6&ifpm=m6
برای استخراج لایسنس، آی‌پی و پورت مورد نیاز، اسکریپت زیر رو اجرا و مقادیر رو در الگو جایگذاری کنید:
اسکریپت استخراج:
bash <(curl -fsSL https://raw.githubusercontent.com/Ptechgithub/warp/main/endip/install.sh)
☑️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5606" target="_blank">📅 12:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همراه اول
Windscribe UDP 443 Censorship On Dallas BBQ
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/archivetell/5605" target="_blank">📅 12:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کسایی که سرور دارن.
اینباند:
Vless+xhttp+tls+Cloudflare clean ip
بزنین با آی‌پی تمیز کلادفلیر
عالی وصله‌
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/archivetell/5604" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">همراه اول
Windscribe UDP 443 Censorship On Atlanta Peachtree
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/5603" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">و اینکه، نرم افزار Karing گزینه وارپش کار می کنه و پینگ داره و کار می‌کنه.
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/archivetell/5602" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واقعا باورم نمی شه مردم چقدر می تونن عقده ای بشن.
📘
مگه ما فروشنده ها چیکارتون کردیم؟
😭
طرف با کانفیگ رایگان بعد ۹۰ روز وصل شده زنگ می زنه مسخره کنه. چه رویی دارین خدایی.
حالا من به وصل شدنشون می گم وصل، طرف فقط می تونه با کانفیگش پینگ بگیره
🤡
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/archivetell/5601" target="_blank">📅 12:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لینک داخلی
Am tunnle
(pro)
Am tunnle
(lite)
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/archivetell/5600" target="_blank">📅 11:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">AM TUNNEL
سرور ۱۶ fast dns روی ایرانسل و همراه اول سرعتش خیلی بالاست
https://play.google.com/store/apps/details?id=app.vpn.amtunnelpro
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5598" target="_blank">📅 11:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga5R_lVhs_JX9KSUnC75ysPZzFsN7shdbzGdcMH1mehZZEt8L7ICCtcytm_xOjZKww8wbAcHhNxk7khitZed15tzfGV1Y08FJsMxrjYaCN39GaJBW-1XBlvK5e6fZzRyg15vQAMEM0K0AwciWI703ZRV43IyvSu2b-UBtvS9jgUNRC0b6C2SmWY5t8tz33B8WvsmcyvTGRuIYb7GXCs13nYPwbxWOxv18voDzELGSSmttJjmsnvHOjPgOKeZutSzVgu7Utv9zNrEWaTWAkf2b-jVio-bzwtq75l-AVxhq3BunVVnmdWx8zjYSco-NjGZ0xAhIlsWsxidKI2VKSahig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Optimize-Windows
اسکریپت‌های بهینه‌سازی و ساده‌سازی نصب ویندوز
https://github.com/ShivamXD6/Optimize-Windows
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5597" target="_blank">📅 10:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kv7keKxt3JyktL5fb1pQpPz5qcxRas1QOJ68CRuibfUI_VHN9987J3jFahv9CrOd63XhUY1kqqFF3vLI2eTGIUUaEifRrqQvydvn-QWDyWCVdGJg9ukcT963ovt7V1ZP8RPWHOC7wGdJnJGLjGaXPe8_cLOrvJwBLPSAGPyBfTw3GKZgg2s0W6u6Jz8l3GDnhhPsTfxI_PXs4CVf2kGlNZX0r8Upt6cC7oAgs-MYXUAgiWVXbKrrMbdG9inYOtJ1xOp9OYVqWZ_Qy3QcScvhBbuRLo7LeBcyEY9Dv-YRSFvKKrtMiP8OiL4d9pKXXbtc0byoyP-y1CcCILPOAXU5Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ha6eYICvf4rFVPIHLpNls_wVNOKqH1dh9DRMlsNHLU4pIacmMaHknVLjofqQweXKaX5g2vVbDulbzTsRpSr14UBAHCE2f9devHPL5m7Sd4rHPQ0guQBSVLP0GCchWTav3jgBB5oYiZymAXWEJX431pAvost-Pz2P70Er8iwro7yUGuOUhtzO03bC5vxIgf0_P733U7VGg7uQu6ztpuZQCZNnnMHxEz07Q0UYD6j5Qtcz3WGaEwSnpVtY49pZ-N4U9BZ5APfclziro2gCXkE_g3om70oMClT9yMTL2jrSIvuS3xDcJUkoY_FVaJC0XRVYXOS9VWaz5-CfYPxFCmEZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3J0uxVnc5m3bdCwaNSD0rEB7PPvrq68A4ARHkq_ZOivUEKYQKEX0eAOzlcwrIl6-TabOhkN299pXknbDFAEpRJQSlYaoPSoGNgF4kZ7TrBvSrNnyFiQTJNGoyNncL2jkNhEDHkjcH7q8DTu8P4BONr4yHUXKFcxHXX62v8hVc-pIjqk4iGzllRnw_0o7KCowY7Tm5YF6vJup0ScAfUIz8fko9_cRRBQZqMFlUbAfA5wEWOyB4huKYEnMFL1lgnQukbABrrNd5C1lom3lUakAtoBHyVBuKbgVvHxGFB1Aa-DuicOLRbRh-PXGL_OdR-85j6EJ-KZhG6alZTlut9vNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBe0v5FdkcEnuFrXT3sBkYXM4upXVrXqaLpYispp81qFGxHQk7gbPLPCBXf3lorTTGtjwwS-AlF-0zcdY43iwW45doT2tBt3D_yAi8kEX54VAxSsmSnCybQP1VNLRCS1I40XbmKwmjjPDzgp2ULXZC1QkG7oBv64SwyH9kjFHMnFnl7ta18gzD1Kc0vmryzmS9M4V_sH-EHsxw9j5JvISdIn8Zap0zAMlBbdZzpggHmaPMuSlYMXNkJwr6UiSyrLCIV-tP0ZKmjvgZ3EPLM2OAk6WBcN0leOElZRWpVn1hWn0PePcVt5uCZw77X2Pza6Ub10kvw1tzOjGzD2nGh_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7wVFp13byJaHpjx7aVsDAhUEv12eg9tQKx5fCuXtll-3EukcocYmjs-CmvImutEKe35-V3n021fTwpzX-BDEwHbE_i0lsBNfqI_UmL5i9J50O_sbehm0Sydafw-3G_smErrRLqcvyzfzuhXGvTv-byNcYJp1-Y6kTe2BxVi5ZZo-qOrxJo8KQjhG_wBbeqfoFDvwbRLzbdpWmVDf2yzkHux6v5vml24icTgrfE7WJtpoff3nnO_csq24jhBYm-D_0XvsO1UYq0IEQJts9mLJdlF9cd40xUpwqBWVSczQJ3oGc7_LeZc6EKpa9QqrzGiAPb3peQNo0iA6AKwRiTgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNQFGjscbuxnWNg-392_fHOp6BXglJlMI-NnmwpdeOubEZgr_Kjqe0tZQVsHomdmbCqhxNHQXZwd2_VSvJE6fPp-XApPycLM8iXGcUTErvDO-hk88EEiygKipZ6g6Q69cFWDiSz8Kx-A5ODqYaJK6lpPQKTgwX5q6b14ajr36MaDdEHM1tzB0LdblFCIdPA0toql-ZfAAg0HoLT0kyu013Eul3pFPuQkqsTJ7PWcDxikAVwy6m-Acw7y949lsVseOrFY-pQPtL77kGPjcEr1olOTCUqnyc1YH_V0UkNW8BIoFnRFpLudXo7RxjJhZMrpPzzedgD9Uo16m5K-9k26bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bf1rKN4b5HHHcGmkERwNPFTBqMhqM2FlPn0Vscrf6EBAX8BU1EbeZG0zxR7W2ALD4S5g177n-pbSKFAUx7PjbVJI63ac45FlPFiOfUNzN-C684BEdk9XIrlTo4d36f7KRgK9KxnDEbH0a592owTdHq2agRLcgr501FLiGoIdkX2apvDAqWzs1EdXG0YlbQvd2GacQH_oTb-qBhbSu1pk9kJwDRGALC_b_mloz_UmkP9XDiMyY1PyziDTNx0Gf8vmntZ2FXHR5jQY8xoiZxp0Ai9zofMi3zQEA2W4FK7Bitqz2HyMQYwd6zIeWavMeQp5tIh1_U1m1NAk6Z0TYf944w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ربات دریافت پل تور
@GetBridgesBot
پل webtunnel سامانتل و ایرانسل وصله
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/archivetell/5590" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Invizible_Pro__beta_ver.2.6.9.apk</div>
  <div class="tg-doc-extra">38.1 MB</div>
</div>
<a href="https://t.me/archivetell/5588" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">InviZible Pro beta 2.6.9
* Updated Tor to version 4.9.8.</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/5588" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQbUc3ypxCrCR0mW_rQwilw-GcfwFbReppv1mW531jO_t5UBJCJxUTglIsU1PIrEdQz-q6MDU7GuWdCzbPou7j6ZWshMFzlJUOJlwKYcpDQMXLU_UXLnez2fxOYGDVDVFou9Ky_B5eeQ2yHQYYE07bx76mNmd5e3N7L7z2c3Iec5csBQQlg7nLCdDXvf4yixFTztZpZuPYYdLiAN8R1_u0AyAb1b5mn78xk4FzKIvY0QOaSRYmpfUJzBPNCLLl5mwvD0efiYwSycmPaNDyArVLhhTmH_Xtj9kLrbYVVZrz3pwvrrbBVR6V4Vz8yoI7MQwphAVxuMqsJdZNtH0C-xkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش invizible pro به زودی..</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5587" target="_blank">📅 09:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">MetaMask یا Trust Wallet?
🤔
👇</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5586" target="_blank">📅 09:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">BD NET VPN
مخابرات، متصل
سرور BCCF 01
@ArchiveTell
https://play.google.com/store/apps/details?id=dastan.prince.bdfreevpn&hl=en-US</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/archivetell/5585" target="_blank">📅 09:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شیر و خورشید بدون آیپی
مخابرات ، همراه اول و ایرانسل وصله
تنظیمات رو به حالت اولیه برگردون ( کلیر دیتا ) و پروتکل رو بذار رو CDN ، متصل میشی ( کمی صبر نیازه )
﻿
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/5584" target="_blank">📅 09:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آیپی تمیز کلودفلر سامانتل
208.103.161.170
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5583" target="_blank">📅 08:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📱
صد گیگ کانفیگ اوتلاین به همراه شادوساکس بهتون میده
✅
( پروکسی ام میتونین انتخاب کنین )
@OutlineKeysRobot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/archivetell/5582" target="_blank">📅 05:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/archivetell/5578" target="_blank">📅 02:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDFqNtx4Jasm_YJf5BC4_Q-iSwDTiG-EFSH59iMEJYLYxBz69fG2p899LVauIoh1nDUE1GHrmYEXJq0I2OMmbrg0HocRQKYRVPydW1da3511CmmrrJRtL9e4Fkd4SgZ_TguqXNN1wOU3IhT5BVx6uflg8gbbK44FKHMw3NTF_wVBCTXQouxthHF5oC_MGs9jWL3OvAv1bxt_w9k13eB0ELqygd-NLGwyynroy2uUlL6wnP-xQrnCWewBlfa6C1DILuNyyTiWzs7oQUkvNj-z2kOyTcwYiqrQ3lT_1nIoxayadRUmcQD_mPqPbwzxOSB_XyivMsy617yXycGRy7bAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب Obfs4/WebTunnel Meek Azure Snowflake اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/archivetell/5577" target="_blank">📅 02:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5576">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">octohide VPN
ایرانسل سرعت عالی
لینک گوگل پلی
از ربات
@octohide_bot
کد ۳ ماهشو بگیرین فعال کنین
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/archivetell/5576" target="_blank">📅 02:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🟢
نسخه جدید Argo VPN (اندروید)
🔺
بخش Network type رو روی Public Network قرار بدید و متصل بشید
اگه ارور داد یکبار برنامه رو ببندید و دوباره وارد بشید
https://dl.toolschi.com/view.php?f=ac33499153243a31.zip
(لینک دانلودداخلی)</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5575" target="_blank">📅 02:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5574" target="_blank">📅 02:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV5nosy567f4CtYjxr26LTrFriFdpZ_BWeqngevIukr-dYkCg91qLjdR1Gjd8q_5gXzECzMamV2PtIve6km0EkBcgdaZFTQSsbEHwxNedRx87ZBAp4E_rTHNMMTLA8463yI7Htyn2VlD8_Ul3gqTpdfEkW88OitHeXuP6Y-bY0MaE4wpKfRsNlfykNQaXPPAjaUImLzFQWHg2CfCq2-8UcnbCxOm2YjOAlCF3GDVzp6t6hhJVtfUSz8lDY8JVMi6gdtjA59AkjrCenvAnS_JXDlhtcAgd4N6HGsnjirH6mWKM4U-6Q6_YP2eHwK5sFYz_q9lxacNByU6VqIzJYN56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/archivetell/5573" target="_blank">📅 02:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5572">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب Obfs4/WebTunnel Meek Azure Snowflake اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/archivetell/5572" target="_blank">📅 02:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب
Obfs4/WebTunnel
Meek Azure
Snowflake
اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/archivetell/5571" target="_blank">📅 00:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5570">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کلاینت های Exclave, SlipNet از ssh پشتیبانی میکنن
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/archivetell/5570" target="_blank">📅 00:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NzjnHDPQttfB0bue3wSTxIDwr3OpXBZD8VkwYJ1ad7g0NWHVDGtyg-7abp7ZYl_if89kk28BCp_6pHCeiYEmb9NtuhxyK4TCHeFDGB1ZDIOGlYg_XvvypljIamGpkPUQvtsJIwuQYjRMnQlAxb6qTRjUTz-IJA04s3ddxLVXxNfMQtqUwYIWCAOHPCv87G_R20P82K9YR_i2CSDoXFO14LASdb23LeYgGT0Wib_18w6a2VhRJjuGSbfDHHzDEWsvf5r4dPc9DcRd-99t-vPih2Z3igPcBAgcDU1rtm7ceDayPHaCScHqd1MeS7pakmUpcO7_h_f7w1NJX6d-gWzTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxrS6CMktmFYby_BYeJOsmZT5ZWYMXnf8sIVOlC-85F4-5p-YO2LBemzl9T9G6yEtMAWIzaGDkveGP4jWSPE7o9djfwOvhkoIikfgOm2UG9teOTJ9hRb91BG4Uv7ibZwfpdtQyXohoAFtc9ZtnyoYb1d_hL_u1vJ9PS5tacGxo_H1tI5sg2X2q8JZodoxTdvvTqLmN_nB0Xlr36UztZIH-xDRlojRRV1HdalmIw50rfmjxHo9TtSm-nVc9-WVUz3AIKMq0pIi8f_LXlnOSAi57UqLdvYdaqFbm39mEAiDgukq6sQBloC76JBf3r82y-nYnM76ZM_Qp2o7tg1euEpNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmTjiApJYiRaObJakQdNFWGXWstg6wgjPdEbrOhquACGIoSh0C2UFWV22hT37GEQu8eDZJnzk8rEW6rZJeHNLWp6VJQLI0_vT479hZj954NuLKWHbHftzhamB4FlBzNRluJO3ifm6M1ZFPifQYgdvCsLVD3DSdkEfh-jqxFp8SzKjdLshDKHmTyHSepl4nPJeuNqwy4xN7Rpe6dz_jUg8R18Hi2ML8McKXNjDkpoFCZmPCWSDnr4-20HZMlPiGeKM2FbhnUSq_rR8jbaqLzm519KM1p1_ieIXuYwtrS7F7qNqvB0FAGTZktr73uKJUaxJSKX1bxjEvA9ww6LHbEtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bsYCgugeSovEwkHMjP_c_zEcuqxsNKf61vuekcguQbyksesY8BH74w9zU61RnYJcr-_xUNtNe82mEJCULlYf5L6SvdlVmjVIc4hrBMgQJ0jMrZbm4ySpoV2p-OrKDIsjoelKeVlcoGRFKVoPBQirnkuMHPJnZg1AiBVbHrLw8EdnqyuSnXOAqfLPSIUF2y4Cqt9mIX4Lss7aQDUMpizSb9i12PiIzlgR-3QgDZOiGA2B4RPOtS1GzB2WRrmuWZGEMA1fk1gjj1voxoIJS4_w1DnF-nWRoAbAY_u7bvg6UDsJ0fqBGaZFZ5TA852z3r_CbApGNvgPER0J-miv_m9t1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LizGCK1crToPasZAlaWhZ-SWOj_xr8DyHy-OJ8AMTrYg6J8vd0QszNXPQR3_SlPyqM1Vwqjfi7jnfezHekhxJTpH7bog8Yj-bBsP_dDFi5E5YxNfYScj2dvY3zLYU38uhC5OKVAZTYtnWLc9EHYJic7M4pyZ1L5zM7HOWMPtqNmgkQvsRJoFNMlGiIyTBzgBp5070HqoRSB4-e1d5CKwiKOlMabMklziq-E_d4FGyWU828buvEvDQc9dpnQd3lRaAcW6VcLhVpU4YsNq3keXrAfNdzXOpXGL0Ejvh8hnFUsnSAPoBc5GLIkew0wXBQFrR1ln-ymzuMXD7dNr-HVt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlLS69ORuZ-D_fM_ISwRW1WujyJHnEXRKB9MFl9dSxpM6ZhWyv1j2k6blbiv04t4t4PgdOV2oAduyJDEDqSU4edz4Gmsmftb6ufNx7XBxO-jJqPyT3m9F5gA76_PH802Ud4QrSfJAtLUltXWkPcRsB-IUkk-HwYlpBHllWf6s2HQx3TVUXIHKCAwlIPcitHEJWLY4df6YxFXdDXKnyBWrCWj-VLFY80CMDZ335vNTSCPZE_aBe0E2F92LZW4jyVu7WvMM3OKIml-N8agENjxCWxVzoUltkQpX889E0oHs96_f8cCNaIheVM0LIbMshPt9h_wPxqAuXyrkb4b_kppXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از بالا چپ به راست
اتصال Tor با برنامه اسلیپ نت
پل Obfs4
بقیه هم میتونید تست کنید
Snowflake, Meek Azure
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/archivetell/5564" target="_blank">📅 00:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پاکت هدیه
🎁</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/archivetell/5563" target="_blank">📅 00:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سوپرایز anonvector
❤️
🚀
آپدیت جدید و هوشمند کلاینت SlipNet (نسخه v2.5.5)
---
نسخه جدید اپلیکیشن
SlipNet
منتشر شد. توی این آپدیت، سازنده تمرکز اصلیش رو روی هوشمندسازیِ فرآیند اتصال و تنظیمات DNS گذاشته تا کانکشن‌ها خیلی سریع‌تر و پایدارتر بشن.
✨
مهم‌ترین قابلیت‌های این نسخه:
🔸
تنظیم خودکار شبکه (DNS Auto-Tune):
برنامه حالا می‌تونه به صورت کاملاً هوشمند، پارامترهای حساس مثل
Query Length
و
Rate Limit
رو بر اساس وضعیتِ فعلیِ اینترنت شما (برای کانفیگ‌های DNSTT، NoizDNS و VayDNS) تشخیص بده و موقع اتصال تنظیم کنه.
🔸
انتخاب خودکارِ بهترین دی‌ان‌اس (DNS Pool):
اگه این قابلیت رو از تنظیمات فعال کنید، برنامه قبل از هر اتصال لیست DNSها رو اسکن می‌کنه و ۱۰ تا از سریع‌ترین‌ها (با کمترین پینگ) رو برای کانفیگ شما ست می‌کنه. *(دو حالت اسکن سریع ۱۰ ثانیه‌ای و اسکن دقیق ۱۸ ثانیه‌ای هم داره).*
🔸
اسکنر و مدیریت پیشرفته DNS:
حالا می‌تونید آی‌پی‌های سالمی که اسکن کردید رو در قالب یک گروه یا استخر (Pool) ذخیره کنید و هر زمان که خواستید با یک دکمه فوراً لودشون کنید.
🔸
بهبودهای ظاهری و امنیتی (UI):
- منوی اضافه کردن کانفیگ جمع‌وجورتر شده.
- می‌تونید برای باز کردنِ باندل‌ها و قفل کردنِ پروفایل‌ها، پسوردهای کاملاً مجزا و مستقل تعیین کنید.
---
📥
دریافت آپدیت:
می‌تونید فایل نصبی این نسخه رو مستقیماً از لینک گیت‌هاب زیر (بخش Releases) دانلود و نصب کنید:
🔗
https://github.com/anonvector/SlipNet/releases/tag/v2.5.5
📌
#آپدیت
#SlipNet
#فیلترشکن
#اندروید
#DNS
#تونل
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/archivetell/5562" target="_blank">📅 23:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/archivetell/5554" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5554" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-text">v2.5.5 Changelog
🌐
DNS Pool (New)
•
Auto-Scan:
Automatically picks the top 10 lowest-latency resolvers at connect.
•
Verification Toggle:
Faster scans by default (10s timeout); optional full HTTP/SSH verification (18s timeout).
⚡️
DNS Auto-Tune (New)
• Auto-tunes query length and rate limits for DNSTT, NoizDNS, and VayDNS profiles at connect.
🔍
DNS Scanner
• Save working IPs as named pools and load them instantly via a new button.
🎨
UI Improvements
• Replaced the "add-profile" bottom sheet with a compact 3-column grid.
• Moved DNS section above Network in Settings.
• Independently set bundle-decrypt and per-profile lock passwords.
———————
✨
قابلیت‌های اصلی جدید این نسخه:
قابلیت Auto Tune: تشخیص و تنظیم خودکار و هوشمند پارامترهای Query Length و Rate Limit بر اساس وضعیت شبکه.
قابلیت DNS Pool (قابل فعال‌سازی در تنظیمات): اسکن خودکار و سریع لیست DNSها قبل از هر اتصال، و ست کردن بهترین و سریع‌ترین Resolver روی کانفیگ.
بهود رابط کاربری و رفع باگ
دانلود از گیت هاب:
https://github.com/anonvector/SlipNet/releases/tag/v2.5.5
🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5553" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkTuSL2QL3bqhUl6aizMskuQx6P70OfyNMm_ao4ib_DqRGLkqvmIgmLHJLleiGSJQ-z_NQu-sPdAqRT1RGxlPY3ThZF8MGvNyC2vCbCXx0APgVW3o-MoTgk4F1GenLs33ZMIFa5kNIb9Ekq4IINWwujz9UE8yIctAji2NlHxn67frXyBW9gY9FtezXDCHHzzyYqw_YhorqD954vxAXc1VU9PyMdFI22s2YkYF7KwhNIOGfDyzHdt5vJVOUowQ0_Of02OjmpGsmBuXBwu34XiiZH5gYlHXl4-YV6NuaSyF6cIUGA-ENF9Fzqnen_WwI5MigCMF_UG_J0dOW3updP3lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله  یکم لایک و انرژی بدین اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/archivetell/5552" target="_blank">📅 23:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5551">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سبحان الله  یکم لایک و انرژی بدین اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/5551" target="_blank">📅 23:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سبحان الله
یکم لایک و انرژی بدین
اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/archivetell/5550" target="_blank">📅 23:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نت شخمی نشده؟
کانفیگا پولی هم بد وصله
😐
😂</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/archivetell/5549" target="_blank">📅 23:26 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
