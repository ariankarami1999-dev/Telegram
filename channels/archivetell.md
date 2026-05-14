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
<img src="https://cdn4.telesco.pe/file/UQ7VuJU0q3KyPSn2NK1IunUH7FOx-lVJBniobtsxCsUzIS7s-wp1P9nmEmfPxr4aLmHN0YC3gEBIYqfZj_pUQVxx7AgXHxLJMK476k8gc-GSNA6sGm_eRFRYgBzz9iBv3PUSBQx5fB9i9jBddzLQ4v31FB2zT4I7u28v3elxt5uOGQJNgRck_3RYrWx3aowE5qbCToOA0mbdgKGocYAYAB0D-zIxkD2neM1YkadUkzlkKF2ZQd9woIqC6OTHiKrrHzdRUBQle5Nlrh15sB7-vLZL5GikGBBdiJekynJ9mrYL2sZRapnVFuiR0mEpg6qmidd7PBohsgRbZMtChWPdEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 6.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 16:43:36</div>
<hr>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فعلا در این کانال صرفا مطالب مهم و پین‌های گروه  @ProjectXHTTP   گذاشته می شود.  ///  اگر کارهای بنده باعث شده گره ای از مشکلات شما باز شود ممنون میشم حمایتی هم از اینجانب بکنید:  USDT (BEP20): 0x76a768B53Ca77B43086946315f0BDF21156bF424  USDT (TRC20): TU5…</div>
<div class="tg-footer">👁️ 372 · <a href="https://t.me/archivetell/4880" target="_blank">📅 16:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">فعلا در این کانال صرفا مطالب مهم و پین‌های گروه
@ProjectXHTTP
گذاشته می شود.
///
اگر کارهای بنده باعث شده گره ای از مشکلات شما باز شود ممنون میشم حمایتی هم از اینجانب بکنید:
USDT (BEP20): 0x76a768B53Ca77B43086946315f0BDF21156bF424
USDT (TRC20): TU5gKvKqcXPn8itp1DouBCwcqGHMemBm8o</div>
<div class="tg-footer">👁️ 273 · <a href="https://t.me/archivetell/4879" target="_blank">📅 16:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شیر و خورشید
CDN SNI hostname خالی بذار
CDN edge IPs :
92.122.123.128
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
138.201.54.122</div>
<div class="tg-footer">👁️ 477 · <a href="https://t.me/archivetell/4878" target="_blank">📅 16:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">psiphon-helper-force-akamai.json</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/archivetell/4876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سایفون میتواند هم از طریق akamai و هم از طریق fastly متصل شود.
این دو کانفیگ سایفون را مجبور میکند که از طریق akamai یا fastly متصل شود.
در کانفیگ akamai شما نیاز به یک ip سفید و در کانفیگ fastly نیاز به یک sni سفید دارید که میتوانید در صورت نیاز آن را در کانفیگ ها تغییر دهید.
گرچه دومین‌فرانتینگ های استفاده شده به اپ شیر و خورشید اضافه شده اما با استفاده از هسته Xray-core شما از ویژگی های متعددی مثل "فینگرپرینت کروم" و "happyEyeballs" و ... برخوردار هستید.
پروژه های دیگری در راه است حمایت فراموش نشه
@patterniha</div>
<div class="tg-footer">👁️ 505 · <a href="https://t.me/archivetell/4876" target="_blank">📅 16:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">منتظر ایران نتلیفای باشین، از معجزاتش زنده کردن مرده هاست
ایشالا که خبری بشه</div>
<div class="tg-footer">👁️ 956 · <a href="https://t.me/archivetell/4874" target="_blank">📅 16:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎯
خلاصه و جمع‌بندی متدهای امروز (سایفون + دامین فرانتینگ)
---
رفقا سلام!
✋
امروز یه رگبار پیام تو کانال داشتیم درباره متد جدید و می‌دونم ممکنه با دیدن این همه فایل و ربات و کد، خیلیا گیج شده باشن که «بالاخره کدوم رو باید انجام بدیم؟!»
بیاین خیلی عامیانه و تروتمیز جمع‌بندی کنیم که دقیقاً بدونید باید چیکار کنید:
🔥
راحت‌ترین و سریع‌ترین راه (بدون هیچ دردسری!)
اگر حوصله درگیری با فایل و سرتیفیکیت و تنظیمات پیچیده رو ندارید، فقط نسخه آپدیت‌شده‌ی برنامه «شیر و خورشید» رو نصب کنید.
تو این آپدیت، فقط کافیه پروتکل اتصال رو بذارید روی "فرانتینگ cdn". تمام! برنامه خودش وصل می‌شه و نیازی به گرفتن سرتیفیکیت، برنامه V2ray و وارد کردن کانفیگ نیست.
📱
روش دستی برای اندروید (V2rayNG)
اگه دوست دارید خودتون متد رو دستی پیاده کنید:
۱. دریافت گواهینامه: باید دو تا کلید بگیرید (یا از سایت regery.com، یا ربات‌های تلگرامی مثل
@CrtGen7Bot
). در نهایت باید دو تا فایل به اسم‌های mycert.key و mycert.crt داشته باشید.
۲. نصب در گوشی: تو تنظیمات گوشی CA certificate رو سرچ کنید و فایل mycert.crt رو اونجا نصب کنید.
۳. تنظیمات V2rayNG: برید تو بخش assets files برنامه و اون دو تا فایل رو اضافه کنید. بعدش طبق آموزش قبلی، سایفون رو بهش متصل کنید.
💻
روش راحت برای ویندوز
برای ویندوز ابزار آماده PsiphonOverMITM کار رو راحت کرده:
۱. فایل زیپ پروژه رو از گیت‌هاب دانلود و اکسترکت کنید.
۲. روی فایل Run-PsiphonOverMITM.bat راست‌کلیک کرده و Run as Administrator رو بزنید.
۳. برنامه سایفون رو باز کنید، برید تو Settings و تو بخش Upstream Proxy این مشخصات رو وارد کنید:
Hostname:
127.0.0.1
Port: 20808
۴. تغییرات رو تایید کنید تا متصل بشه.
⚠️
اون آموزش طولانی SSL سرور ایران چی بود؟
پستی که درباره انتقال فایل‌های fullchain و privkey به سرور داخل بود، فقط و فقط مخصوص ادمین‌ها و کسانیه که سرور شخصی دارن. اگر شما یک کاربر عادی هستید، اون پست رو کاملاً نادیده بگیرید!
💡
نتیجه‌گیری: اولویت اول برای اینکه گیج نشید و سریع وصل بشید، همون دانلود نسخه جدید "شیر و خورشید" و گذاشتنش روی حالت "فرانتینگ cdn" هست. لذتش رو ببرید!
✌️
📌
#آموزش
#سایفون
#دامین_فرانتینگ
#نت_ملی
#تونل
#شیر_و_خورشید
ArchiveTell |</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/archivetell/4873" target="_blank">📅 15:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
آموزش اتصال رایگان به اینترنت آزاد (ترکیب Psiphon + دامین فرانتینگ پترنیها)
---
رفقا سلام!
✋
امروز یه متد به‌شدت خفن، بدون پیش‌نیاز و کاملاً رایگان براتون داریم که با ترکیب کلاینت سایفون (شیر و خورشید) و کانفیگ‌های دامین فرانتینگِ پترنیها کار می‌کنه و اینترنت آزاد رو براتون میاره.
این روش برای وب‌گردی، اینستاگرام و تلگرام عالیه (البته برای گیم آنلاین پیشنهاد نمی‌شه). تمام فایل‌های مورد نیاز هم از قبل آماده شده و لینک‌هاش پایین پست هست!
👇
🖥
آموزش برای ویندوز (V2rayN)
1️⃣
نصب V2rayN: برنامه V2rayN رو باز کنید (اگه ارور داد، Runtime و Framework نسخه ۶ به بالا رو نصب کنید).
2️⃣
ساخت سرتیفیکیت: فایل Certificate Generator (موجود در فایل‌های دانلود) رو داخل پوشه bin تو مسیر V2rayN کپی و اجرا کنید تا دو فایل جدید ساخته بشه.
3️⃣
نصب سرتیفیکیت: روی فایل mycert راست‌کلیک کنید، Install Certificate رو بزنید. مسیر Local Machine و بعد Trusted Root Certification Authorities رو انتخاب کنید تا نصب بشه.
4️⃣
تنظیمات V2rayN:
🔸
برنامه رو باز کنید، از Configuration گزینه Add Custom Configuration رو بزنید. یه اسم بذارید، فایل Json پترنیها رو Browse کنید و Core type رو روی Xray بذارید.
🔸
تو مسیر Settings ➔ Option Settings، پورت Mux رو حتماً روی 10808 تنظیم کنید.
🔸
کانفیگ رو انتخاب، Enter بزنید و وضعیت سیستم رو روی Clear System Proxy بذارید.
5️⃣
تنظیمات کلاینت شیر و خورشید: برنامه رو باز کنید، برید تو Settings. قسمت Upstream Proxy، هاست رو
127.0.0.1
و پورت رو 10808 قرار بدید و استارت کنید.
📱
آموزش برای اندروید (V2rayNG)
1️⃣
پیش‌نیازها: نصب آخرین نسخه V2rayNG و کلاینت سایفون (شیر و خورشید).
2️⃣
نصب سرتیفیکیت: تو تنظیمات گوشی CA Certificate رو سرچ کنید و فایل mycert.crt (موجود در فایل‌های دانلود) رو نصب کنید.
3️⃣
تنظیمات V2rayNG:
🔸
فایل‌های سرتیفیکیت رو تو نرم‌افزار Add کنید.
🔸
فایل کانفیگ JSON رو با زدن دکمه + و Import from local وارد برنامه کنید.
🔸
تو تنظیمات، پورت (Local Proxy Port) رو روی 10808 و Mode رو روی Proxy Only قرار بدید و کانفیگ رو استارت بزنید.
4️⃣
تنظیمات کلاینت (شیر و خورشید):
🔸
وارد Options ➔ VPN Settings بشید، تیک Don't tunnel selected apps رو بزنید و V2rayNG رو از تونل خارج کنید.
🔸
تو بخش Proxy Settings، گزینه Connect through an HTTP Proxy رو انتخاب کنید. هاست رو
127.0.0.1
و پورت رو 10808 بذارید و استارت رو بزنید.
📥
لینک‌های دانلود و منابع مورد نیاز:
تمام فایل‌ها (V2rayN، V2rayNG، کلاینت شیر و خورشید، Certificate Generator و فایل Json پترنیها) رو می‌تونید از لینک‌های زیر بردارید:
🔗
لینک دانلود مستقیم فایل‌ها در تلگرام:
https://t.me/MatinSenPaii/3035
🔗
لینک پروژه اصلی در گیت‌هاب:
https://github.com/therealaleph/Maste
...
📺
ویدیوی آموزشی کامل در یوتیوب:
https://youtu.be/M3kZxw1M3vE
(اگر این روش براتون مفید بود، می‌تونید از توسعه‌دهنده این متد از طریق لینک
matinsenpai.pages.dev
حمایت کنید
☕️
)
📌
#آموزش
#سایفون
#دامین_فرانتینگ
#نت_ملی
#تونل
#رایگان
#Psiphon
#V2rayN
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/4872" target="_blank">📅 15:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">##
🚀
آموزش اشتراک‌گذاری اینترنت آزاد روی هات‌سپات (بدون نیاز به نصب برنامه‌ روی گوشی دوم!)
اگر می‌خواهید اینترنت فیلترشده را از لپ‌تاپ به گوشی یا دستگاه‌های دیگر منتقل کنید، به‌طوری که بقیه فقط با وصل شدن به وای‌فای شما به اینترنت بین‌الملل دسترسی داشته باشند، این روش بهترین گزینه است.
###
🛠
پیش‌نیازها:
1. لپ‌تاپ دارای کارت شبکه وای‌فای.
2. برنامه
v2rayN
(نسخه جدید).
3. فعال بودن یک کانفیگ سالم.
###
🟢
مرحله اول: تنظیمات v2rayN
ابتدا باید قابلیت عبور ترافیک از هسته برنامه را فعال کنید:
1. برنامه v2rayN را باز کنید.
2. از منوی پایین، روی آیکون برنامه راست کلیک کرده و
System Proxy
را روی حالت
Set System Proxy
قرار دهید (آیکون برنامه قرمز/رنگ روشن می‌شود).
3. گزینه
TUN Mode
را در قسمت پایین برنامه فعال کنید. این کار باعث می‌شود تمام ترافیک سیستم وارد تونل شود.
###
📡
مرحله دوم: فعال‌سازی Hotspot ویندوز
1. در ویندوز به بخش
Settings
و سپس
Network & Internet
بروید.
2. وارد قسمت
Mobile Hotspot
شوید و آن را
On
کنید.
3. نام (SSID) و رمز عبور را تنظیم کنید.
###
🔗
مرحله سوم: اشتراک‌گذاری آداپتور (مرحله طلایی)
حالا باید جادوی اصلی را انجام دهید تا اینترنتِ "تونل شده" به هات‌سپات منتقل شود:
1. به مسیر زیر در کنترل پنل بروید:
Control Panel > Network and Internet > Network Connections
2. در اینجا لیست کارت‌های شبکه را می‌بینید. کارتی را پیدا کنید که مربوط به v2ray است (معمولاً نامی مثل
nekoray-tun
یا
v2ray-tun
یا
Sing-box
دارد).
3. روی آن راست‌کلیک کرده و
Properties
را بزنید.
4. به تب
Sharing
بروید.
5. تیک گزینه اول یعنی Allow other network users to connect through... را بزنید.
6. در کادر پایین آن، نام آداپتور مربوط به هات‌سپات خود را انتخاب کنید (معمولاً با نامی شبیه Local Area Connection* X یا Microsoft Wi-Fi Direct Virtual Adapter ظاهر می‌شود).
7. روی
OK
کلیک کنید.
###
✅
نتیجه نهایی
حالا هر دستگاهی (گوشی، تلویزیون، کنسول) که به هات‌سپات لپ‌تاپ شما وصل شود،
بدون نیاز به هیچ اپلیکیشن اضافی یا تنظیم پروکسی
، مستقیماً به اینترنت آزاد متصل خواهد بود.
🌐
💡
نکته مهم:
اگر بعد از این کار اینترنت قطع شد، یک‌بار هات‌سپات و v2ray را خاموش و روشن کنید تا آی‌پی‌ها به‌درستی ست شوند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/4871" target="_blank">📅 15:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ما بزرگ بودیم..
با من در نیفتید</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/4870" target="_blank">📅 15:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔐
دریافت SSL برای سرور داخل
وقتی سرور ایران کلاً روی نت ملی افتاده و دسترسی به خارج نداره، گرفتن گواهینامه SSL مستقیم غیرممکنه؛ چون سرور شما نمیتونه با Let's Encrypt ارتباط بگیره.
بهترین، سریع‌ترین و مطمئن‌ترین راه برای بالا آوردن پنل‌ها (مثل 3x-ui) یا وب‌سایت‌ها اینه که SSL رو روی سرور خارج بگیریم و دستی منتقل کنیم.
🚀
در ادامه قدم‌به‌قدم این ترفند رو بررسی می‌کنیم:
###
🌐
مرحله اول: خواندن فایل‌ها در سرور خارج
اول وارد سرور خارج (که اینترنت آزاد داره و SSL رو روش گرفتید) بشید. ما به محتوای دو تا فایل نیاز داریم.
۱. دستور زیر رو بزنید تا محتوای فایل fullchain نمایش داده بشه. تمام متن رو (از خط BEGIN تا END) با موس کپی کنید:
cat /etc/letsencrypt/live/yourdomain.com/fullchain.pem
۲. حالا همین کار رو برای privkey انجام بدید و متنش رو کپی کنید (می‌تونید موقتاً تو یه نوت‌پد نگهشون دارید):
cat /etc/letsencrypt/live/yourdomain.com/privkey.pem
###
🇮🇷
مرحله دوم: ساخت فایل‌ها در سرور ایران
حالا لاگین کنید به سرور ایران. اول یه پوشه امن برای گواهینامه‌ها می‌سازیم:
mkdir -p /etc/ssl/mycerts/
۱. ساخت فایل اول:
nano /etc/ssl/mycerts/fullchain.pem
متن فایل fullchain رو اینجا Paste کنید. (برای ذخیره: Ctrl+O بعد Enter و برای خروج Ctrl+X)
۲. ساخت فایل دوم:
nano /etc/ssl/mycerts/privkey.pem
متن فایل privkey رو هم Paste و ذخیره کنید.
###
🛡
مرحله سوم: تأمین امنیت (بسیار مهم)
برای اینکه خطای امنیتی نگیرید، باید دسترسی کلید خصوصی رو طوری ببندید که فقط روت (root) بتونه بخوندش:
chmod 600 /etc/ssl/mycerts/privkey.pem
###
🎯
مرحله آخر: اتصال به پنل
کار تمام است! حالا فایل‌های SSL شما روی سرور ملی آماده کار هستند.
تنظیم در پنل‌های پروکسی (مثل 3x-ui):
کافیه برید تو تنظیمات پنل و این مسیرها رو تو بخش Certificate و Private Key قرار بدید و پنل رو ری‌استارت کنید:
محل سرتیفیکیت:
/etc/ssl/mycerts/fullchain.pem
محل کلید خصوصی:
/etc/ssl/mycerts/privkey.pem
تنظیم در Nginx:
ssl_certificate /etc/ssl/mycerts/fullchain.pem;
ssl_certificate_key /etc/ssl/mycerts/privkey.pem;
💡
نکته:
هر زمان که SSL در سرور خارج منقضی و تمدید شد، کافیه همین پروسه کپی و پیست رو یک بار دیگه انجام بدید.
#آموزش
#سرور
#شبکه
#اینترنت_ملی
#تونل
#لینوکس
#SSL
#3xui
@Archivetell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/4869" target="_blank">📅 15:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وصل..</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/4868" target="_blank">📅 15:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">با فرانتینگ سایفون زنده شد
😁</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/4867" target="_blank">📅 14:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPBk5qYrtbydBMbNavNvr5dbIWs7vQxli0F8_09iUKd3SoogXP4alqcRfFC5Pf0teuBLhOJYXJHhYjiCHXkL37NiZHEM4sS2muXCadqLlpAR-9kZjfctslLYgDxiODbNoSKM8nOzT8O7X7c8wlNTT1PiJiTwcu0KeeBKkHZKFK2wZ-QxYMQK9RBbMIP5TYaNAcCfHFUZqMJPm8aS3_OiFVek52CRolFDswEJVe3s0LElwxt9z1Eu38QsXU2Bq-X6d964kkVkoqsKcEFJ_cz-WHdIAsfn_vcLy6cw3Qj2hZpeZag8kITKQWcqL7mtPgwyKzTkIfqEUR1AsbF1sRbliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وصل..</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/4865" target="_blank">📅 14:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">لینک آپدیت شد</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/4864" target="_blank">📅 14:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFshKrHlUdlfxknMd5UijgP3WeKNU0kIOVVhQfmBN992TfAfr7Jy9Pt1pgq4XdWbokLJqLM-A0ZuZBc1_VqkZ1_HZcz5vtEWzRRa5Rpr8trbjNCzs5qYRRJi_psSNT0PCbJTOrEUu1VcdjakI77XvB71zZIdkRFj2YrPx6cneNrvd8cEY4xxlfTjS0NroJknHe8tcHn9n3tCPDuc-pYecrT750CbtgC9L9lTaJLmyE8FMPGNCYdc5b_6XGKod7L-lyZLcH_V4AtyA5qdSLAmDr33e6c4BTx9uwOypw9WKdI2sWxOPCZXrkknRomn5cL0VUmMOfaikAMZyNx1WrApjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrCc1g219KKcfpQ7y-LdgdOw3mzA2q8Ea0kdHf6R2BUjFUk6FeTmJ-I5vVxvZVZ4KbkxsCtcIEyEtJrZvRTe9VGF467YrFW4b4snLPvft7zC_YTn5nYLU9QDYdHo5nI1d_2p6FMk3TWZDKuPej6A-PkBw8Gry9nny-prMWeMo3P4VdyClpgeIAj9jm6U1oZGwFx1hnXVCPrcu6k52Sl43MWDfwM378ar33XZNJFL6vPTeKacH2OMT5pH5YJOGFz34tbF_7HjUCzLkgxjHu18lN4jepywJsZ4qRPrISu6rt0TSE-PN9t94eJu0zeBhyW1digc5REBQvcsaFKVxAngjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گیت هاب نرم افزار شیر و خورشید آپدیت شد
پروتکل اتصال رو بزارید روی فرانتینگ cdn خودش وصل میشه ، نیازی به گرفتن سرتیفیکیت یا v2ray و کانفیگ هم نیست
لینک داخلی شیر و خورشید
گیت هاب شیر و خورشید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/4862" target="_blank">📅 14:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ProxyVPN11.Json</div>
  <div class="tg-doc-extra">6.6 KB</div>
</div>
<a href="https://t.me/archivetell/4861" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ جدید متود ترکیبی پترنیها + سایفون
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/4861" target="_blank">📅 13:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">این ربات ها سرتیفیکیت میده اگه سایتو نمیتونید باز کنید
@CrtGen7Bot
@SelfSignedCertGeneratorBOT
﻿
@ArchiveTell</div>
<div class="tg-footer">👁️ 711 · <a href="https://t.me/archivetell/4860" target="_blank">📅 12:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfMIk-4qpKneG4Id356aX0sWr6aP9OA4Tm9YUDm5L9uJYGoK3LYThRRfDAwy8_GgWCojH1UFYFuvdJ-wZol0fa7GGrWlL_bI35gc9KESLp-fdKhPHJhhwhf7oD0_EEIsnJKdLKAUZTRbMWOKqEOw6toVSCmNlx-LLKlzcItffPZEzsvVUiYwbn746ano7200fvCgRyKB8UTOWPJU8XcnGCuLJStuQVMG3m75XY8vXc-zNsoS0Uin7UyBUFiWgZtLPMAkbQOM41p1wNr8k2h0Te0G8KNuFQalhddTkd1TF3xEzUnmCRDPgyo90TbngKhXMtmwOwchn2IfNqOC6sVzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی راحت به اینترنت آزاد متصل بشید   PsiphonOverMITM  یک لانچر ساده و آماده برای اجرای Psiphon over MITM روی ویندوز  مراحل استفاده :   1) به صفحه ی ریپو مراجعه کنید و بر روی آیکون سبز رنگ Code بزنید و بعد Download ZIP را بزنید. 2) فولدر را اکسترکت کنید و…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/4859" target="_blank">📅 12:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">استفاده از سرتیفیکیت تو ویندوز
از این ربات
@CrtGen7Bot
سرتیفیکیت و رمز رو بگیر ، نصب کن ، بعد هر دو فایل رو انتقال بده به پوشه bin تو پوشه v2ray
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/4858" target="_blank">📅 12:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4857">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خیلی راحت به اینترنت آزاد متصل بشید
PsiphonOverMITM
یک لانچر ساده و آماده برای اجرای Psiphon over MITM روی ویندوز
مراحل استفاده :
1) به صفحه ی ریپو مراجعه کنید و بر روی آیکون سبز رنگ Code بزنید و بعد Download ZIP را بزنید.
2) فولدر را اکسترکت کنید و بعد فایل Run-PsiphonOverMITM.bat را Run as Administrator کنید.
3) تمام. حالا فایل p3.exe که برنامه ی سایفون هست رو باز کنید. به Settings برید و در Upstream Proxy آدرس لوکال و پورتی که فایل Bat بهتون داد رو وارد که به صورت پیشفرض 20808 هست
Hostname :
127.0.0.1
Port : 20808
4) بر روی Apply Changes بزنید و تمام
تشکر ویژه از پترنیها بابت این متود بمب
https://github.com/B3hnamR/PsiphonOverMITM
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/4857" target="_blank">📅 12:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ادمین های محترم کانال ها
واسه اون بی شرفایی که اینترنت پرو گرفتن راهکار ندین..
پ.ن: کلی برنامه نویس و آدم فعال این زمینه پیام دادن که ما تن به این خفت نمیدیم
پس واسه خودتون توجیه نکنید که ما به اینترنت پرو نیاز داریم..</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/4856" target="_blank">📅 12:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گرفتن سرتیفیکیت با ترموکس ( واسه متود جدید ترکیبی پترنیها + سایفون )
pkg install openssl
openssl req -x509 -newkey rsa:2048 -keyout mycert.key -out mycert.crt -days 3650 -nodes -subj "/CN=localhost"
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/4855" target="_blank">📅 11:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این ربات ها سرتیفیکیت میده اگه سایتو نمیتونید باز کنید
@CrtGen7Bot
@SelfSignedCertGeneratorBOT
﻿
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/4854" target="_blank">📅 11:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آموزش ویندوز هم مثل اندرویده..
لینک داخلی آخرین نسخه سایفون ویندوز
لینک داخلی آخرین نسخه V2rayn ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/4853" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">v2rayNG 2.1.7 لینک داخلی  دانلود  با این نسخه وصل شید..  اینم لینک داخلی سایفون  واسه اونایی که نصب ندارن  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/4852" target="_blank">📅 09:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">متوود جدید ترکیبی پترنیها + سایفون متود ترکیبی Psiphon + MitM  1. برنامه ویتوری رو نصب کنید https://urldl.ir/download/499338  2. برید به این سایت و یک نام دلخواه وارد کنید  و بزنید روی ذره بین. دوتا کلید میده بزنید روی دانلود. https://regery.com/en/security/ssl…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/4851" target="_blank">📅 09:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">v2rayNG 2.1.7 لینک داخلی
دانلود
با این نسخه وصل شید..
اینم لینک داخلی سایفون
واسه اونایی که نصب ندارن
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/4850" target="_blank">📅 09:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/archivetell/4849" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">psiphon-helper@patterniha.json</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/archivetell/4846" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1. این فایل رو به ویتوری اد کنید‌
2. ویتوری رو بزارید روی حالت پروکسی مود
3. داخل سایفون برنامه ویتوری رو don't tunnel کنید.
4. این پروکسی رو داخل سایفون تنظیم کنید
127.0.0.1
10808
5. وصل بشید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/4846" target="_blank">📅 07:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4-r0PEHmQzSWnB9Fk5FluSA8bbCstJCNfOHQCdxkmFkne7FRFomR4Vxt15NQfBFLUAnT0LEbB07eCVLcedHfsUN7650OD5uln1A0lKMdkf-IbrJKFsOSkwCZ_VUu-NF6ZNoBoVDS5ZuU7nYO8cw_1R12cFsag4bPF35G_8h9HoKcqVJZiHBwtncqaYOG73Opzs4WO6GcVXejGN8Ksqz_ZZpgWS70FQTc1z6CXhi21gfgZ4iUKIg99yY3Qk4VtVbkWY4qH8QqwuOtV_AGUw8tn9tOMyASA1e7WSBY01N8xSzX7_f-gkmZ-nlpi3769NOpslRnN8Q_Le3zLmvsOSZRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل ویتوری روی سه خط بزنید و گرینه assets files رو بزنید و دو تا کلیدی که گرفتید اضافه کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/4845" target="_blank">📅 07:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMe-a2TJdGFVTGXmsVZ-WFRL-lKoo6z3OOmd4fOagwJ_2y6GI5FDNGmviml3Rf-TOl-3Ee_jXI5RdweZbvJD3h8hYLdnlbR-i57BIuN3q0oZTlyYBkbvkOlF0-Qbr_t-jLl1fRUykfUFwGCkp-lzT7rw2LJSeU-fvm8F6O7RoUzbE8qJJfR7NjySRtX5ogPplENdn4_e4vpfXt1yN7E8jLXP6vleGruRJxPqYClee1QHwxtvQvwAj7ibdTshxWdTXE9bzYwpAXsE7JuvKLOAQRWQmGIbWcVcI9zPTR4To427pT5ARA3mVAIeDc0QnZb-3odlAnDF5IvJUy0endzShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متوود جدید ترکیبی پترنیها + سایفون
متود ترکیبی Psiphon + MitM
1. برنامه ویتوری رو نصب کنید
https://urldl.ir/download/499338
2. برید به این سایت و یک نام دلخواه وارد کنید  و بزنید روی ذره بین. دوتا کلید میده بزنید روی دانلود.
https://regery.com/en/security/ssl-tools/self-signed-certificate-generator
اسم هر دو فایل رو بزارید mycert.key و mycert.crt. اگه گفت همچین نامی هست اول یه نام دیگه بزارید بعد دوباره عوض کنید
3. برید تنظیمات گوشی و سرچ کنید:
CA certificate
بزنید روی install و فایل mycert.crt رو از پوشه دانلودها نصب کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/4844" target="_blank">📅 07:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEUDNg-JBmDlhoLP_Rqudxbzu6c5icfDQPSecvdFm6WsEkCIUU8FsqHY_xpaXTZdBH1QQnLY9_-4h15QjsSgsO7N9CcbnKPGVVBjmx7vz1FOcaV3p3plt1dK9cpYBZXuiHxChIRQ5KxDjv5Xrl7cI9N3eAob0rwkuZ_k0bKZQ0ZtpAVL_w1ZULnA7jiTTWNj3uEdfKlJVgaoo7CjHVi8tnp135SVQx_9dbjfKSCFaxeTXSxv8u6SinhkznRx0dr8wTIPTijtRiLpJhGZrLUMuj1yOP0p1qyVkdsRGNS-2G2orrhdO7kF5yXQAakPnNcuWPY3kyW4JPGA5dx7xgg5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
20 سرور با قدرت متصل
📌
فایل برنامه
📌
لینک سایت
☕️
اموزش ساخت دامنه نتلیفای
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/4842" target="_blank">📅 02:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqe5nHlgPy1V_eVeCODxk6NXLVJbJ9qT9OfoYBE3zGb_faw-TFtDCHYAHxdMLUooPNnWOqtp6ZDgR_fhKYkHZWCE2DNpZXxW6SWBGbUH_xvVtXd0SHuiuwaXOKU0opAPneezO5mkrCsylpB4Rc6QJq7BWnOI68mv3HWPUOWM92BHsvOm063EzSZXRHQkdK6y3ua45lD9UWHIDJhYHdqCxzZTwr-PCSd3CyDbsOEJlIdUXW6ATcGxPA3wwyW6YazKfFCCEsYOm5NMcgsMN-Y82_To8zyMBmlfL90GRZTnZPIC051Zjw8UAnL5W5wzJqaRaFrIgTIEFXf8MW09saM0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🌐
اضافه شدن سرور های تازه نفس
( اهدایی عزیزان
❤️
)
🔺
اضافه شدن کانفیگ ساز قدیمی
☕️
اموزش ساخت دامنه نتلیفای
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/4841" target="_blank">📅 01:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔥
بهترین ابزارهای تحقیق، جستجو و تحلیل اطلاعات با هوش مصنوعی
1) Perplexity – جستجو، تحقیق و تحلیل سریع با منابع معتبر
لینک:
https://perplexity.ai
____
2)
ChatGPT Search – پاسخ‌های عمیق، تحلیل داده و جستجوی هوشمند
لینک:
https://chat.openai.com
____
3)
Andi Search – موتور جستجوی مکالمه‌ای با نتایج دقیق و خلاصه‌شده
لینک:
https://andisearch.com
____
4)
You.com
– جستجو، خلاصه‌سازی، تولید محتوا و ابزارهای هوش مصنوعی
لینک:
https://you.com
____
5)
Scite AI – تحلیل مقالات علمی، ارجاعات و منابع معتبر
لینک:
https://scite.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4840" target="_blank">📅 21:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIAZotEVsof0KiWjyt6fSx-2_G1BoJWm7YRFE1hGA7XSAmadU9-su--_7cMlVL8zzLohgeMPzeKTzcB_q4KBarn_3ZFYl6SQlfKL3F8RLe6sDpajf3gQv0MLJ2LcuQ8TuW0Sui39Pn31Ogv1lVON64ZjfhWsuCMoQf2DTdLiJ3dxo5tEUXyIdaAT0Pi6zSJRY9_Vi3pXvCJLenWtwWNBoNuEuXSvtQSlEeWb0ddqllkiXjAgl7lQMz7FR1GTBjoebA_KBurdCPPZn-0-p4rh-Rdm9FzvQk6Vi1n8uScwbJsIdZy2GP4QOY0qldlsWE7YUIsnwc4kXiSuQxbr0-R93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساب های کانال آپدیت شدند
🔺
لینک ها تغییری نکرده فقط اپدیت کنید
🔥
ساب جدید https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
🚀
ساب قبلی https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB.txt…</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/4839" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رفع ارور No Internet در ویندوز  وقتی اینترنت قطع یا محدود میشه، ویندوز ممکنه اتصال وای‌فای رو ناپایدار نشون بده یا مدام پیام No Internet بده.  این روش فقط بررسی اینترنت توسط ویندوز رو غیرفعال می‌کنه و ممکنه مشکل نمایش اشتباه اتصال رو کمتر کنه.  مسیر: Win +…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/4838" target="_blank">📅 19:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4837">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رفع ارور No Internet در ویندوز
وقتی اینترنت قطع یا محدود میشه، ویندوز ممکنه اتصال وای‌فای رو ناپایدار نشون بده یا مدام پیام No Internet بده.
این روش فقط بررسی اینترنت توسط ویندوز رو غیرفعال می‌کنه و ممکنه مشکل نمایش اشتباه اتصال رو کمتر کنه.
مسیر:
Win + R  :فشردن کلید
regedit
:وارد کردن عبارت
بعد برید به:
HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet
مقدار زیر رو روی 0 بذارید:
EnableActiveProbing
بعد سیستم رو ری‌استارت کنید.
برای برگشت به حالت قبل، مقدار رو دوباره روی 1 قرار بدید.
@archivetell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4837" target="_blank">📅 19:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👀
کروم اندروید رسماً هوشمند شد!
"گوگل جمنای رو کامل وارد مرورگر Chrome روی اندروید کرده و حالا مرورگر میتونه خیلی از کارهارو خودش انجام بده"
مثلاً:
فرم پر کنه،
خرید انجام بده،
صفحه‌ها رو خلاصه کنه،
یا حتی از داخل عکس‌ها اطلاعات استخراج کنه
📌
یه دکمه مخصوص Gemini هم کنار نوار آدرس اضافه شده که باهاش میتونی مستقیم درباره محتوای همون صفحه سؤال بپرسی!
🗣️
ولی قسمت عجیب ماجرا اینجاست:
جمنای فقط داخل مرورگر نیست…
به سرویس‌های گوگل هم وصله!
یعنی میتونه:
» رویداد اضافه کنه به Calendar
» لیست خرید بفرسته به Keep
» داخل Gmail دنبال اطلاعات بگرده
عملاً کروم داره تبدیل میشه به یه دستیار واقعی که به‌جای کاربر وب‌گردی میکنه
@archivetell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/4836" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رادار وضعیت اینترنت
http://radar.chabokan.net/
@archivetell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/4835" target="_blank">📅 18:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/archivetell/4834" target="_blank">📅 17:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4833">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQaci9ccmplpfqE4b6cm1dEZs2Uo-HtlbueATakbBuREpfvT6ZCs5e5Yawy5xZmBpEOd-MgrsFRyKjg_shKVNAFQLF3L2PKSDjCfqmwVq5Ll8vjiyw4Yvyo9h5E7WLRdanRZzdBAtUJEcQg9xno7gWlSbOwEF0WhKcB8nfGewk4rhD2nRfpwIFHyXQ7cVejcAI3mblpYoQsotyje95ycREau0ftYBY9vz9OrmNxL796pvG1jrFEoJCzhpmmtKwsKyOTwX47yPQ4XdHUDC5gFRw54y5xmeKEMeppUYd5eB7lHgCLD_6aFq36kMksqN6_CO_MF2qZZ4amewc8DBoD-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
میگی g2ray ساختم وصل نمیشه؟؟
🚀
دوستان، اگر بعد از اجرای G2RAY در گیت‌هاب کداسپیس برای اتصال مشکل دارید، این آموزش کوتاه رو مرحله به مرحله انجام بدید تا کانفیگتون بدون مشکل وصل بشه:
1️⃣
اجرای سرویس:
ابتدا پروژه رو در GitHub Codespaces ران کنید تا اسکریپت اجرا بشه و پیام G2RAY - XRAY SERVICE INITIALIZED رو در ترمینال ببینید.
2️⃣
پابلیک کردن پورت (مهم‌ترین مرحله
⚠️
):
به‌صورت پیش‌فرض، گیت‌هاب پورت‌ها رو پرایوت (Private) نگه می‌داره. این یعنی کلاینت شما به‌جای اتصال به پروکسی، پشت صفحه لاگین گیت‌هاب گیر می‌کنه!
* پایین صفحه سمت راست، روی تب
Ports
(آیکون آنتن) کلیک کنید.
* پورت
443
رو پیدا کنید.
* روی اون کلیک راست کنید (یا نگه دارید) و گزینه
Port Visibility
رو از حالت Private به
Public
تغییر بدید.
4️⃣
آپدیت هسته Xray (Xray Core):
چون این کانفیگ از پروتکل جدید xhttp استفاده می‌کنه، حتما کلاینت آپدیت کنید. قدیمیا این پروتکل رو نمی‌شناسند.
✅
کانفیگ رو کپی کنید، توی برنامه ایمپورت کنید و متصل بشید. لذت ببرید!
✌️
@archivetell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/4833" target="_blank">📅 17:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">۱۰ دقیقس دارم پست مینویسم، ارسال رو زدم تلگرام کرش کرد. درباره g2ray میخاستم بگم که میگین وصل نمیشه‌.
ولی نمیگم دیگه</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/4832" target="_blank">📅 17:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4828">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9S23dOesYKBF735WkH1gr9kuq_kRdfAwhvsVwskguJZEE0kR4V3laLWHZ8G0LKxPen9jh03SYCh2IjrwAFg7zzD46IzjrKukj8ilL0wsq_gne5IoSGgq1FhEVL8icxLRXDo5czOsasBP6u01SiUkCJZDVoQuEd6TajtTNI4nvw9MoTjVvW7woQkN0C1kvVB3jBXjOSQ0zyLgqTl2210BBHsMBU5UfeUbeCnVh7vyz82INbdqH6GxNwKRFZmqlLsMrQplcpYX9rMOdJeJ9nkuj2kxUaZS8CYmZ4Ri9ShxxL9Omz_19PTtJmAfvW1dw5IGc37_qKrz6AluPcMuoEYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید UI جمینای  با الهام از open ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4828" target="_blank">📅 16:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">لینک داخلی آخرین نسخه Happ اندروید
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/4827" target="_blank">📅 14:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
ساب های کانال آپدیت شدند
🔺
لینک ها تغییری نکرده فقط اپدیت کنید
🔥
ساب جدید https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
🚀
ساب قبلی https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB.txt…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/4826" target="_blank">📅 14:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-text">🚀
ساب های کانال آپدیت شدند
🔺
لینک ها تغییری نکرده فقط اپدیت کنید
🔥
ساب جدید
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
🚀
ساب قبلی
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB.txt
🚀
ساب های متغیر رندوم ( با فیلترشکن باز کنید )
https://sub.ir-netlify.workers.dev/new
https://sub.ir-netlify.workers.dev/
⚠️
: ساب قدیمی نیاز به اهدای دامنه داره شدیدا لطفا
ورژن 1.0.2 پروژه
رو دپلوی کنید و دامنه نتلیفای اش رو بدید دایرکت
t.me/IR_NETLIFY?direct
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/4825" target="_blank">📅 14:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">VaultGram
یک ربات تلگرامی برای ذخیره‌سازی امن فایل‌هاست.
@VaultGramStorageBot
- فایل‌ها در «حساب خزانه» جداگانه نگهداری می‌شوند؛ حتی اگر حساب اصلی‌تان حذف یا مسدود شود، داده‌ها ناپدید نمی‌شوند.
- رسانه‌ها (عکس/ویدیو) و اسناد (ZIP, RAR, Docs) در پوشه‌های مخصوص خود سازماندهی می‌شوند.
- با نام کاربری و رمز عبور حساب خزانه می‌توانید از هر حساب تلگرامی به این فایل‌ها دسترسی داشته باشید.
- یک کلیک کافی است تا تمام محتوا را بازیابی کنید.
به‌صورت کلی، VaultGram داده‌های شما را به‌صورت مستقل، منظم و با حریم خصوصی بالا نگه می‌دارد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/4824" target="_blank">📅 14:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ClonethBot
رباتی برای ساخت هوش مصنوعی شخصی در تلگرام
@clonethbot
- مدل‌ها: شامل
Minimax M2.5
و
Nemotron 3
؛ هر دو بدون نیاز به کلید API کار می‌کنند.
- پاسخ‌ها: نامحدود و رایگان؛ می‌توانید به‌صورت مستقیم در چت با ربات گفت‌وگو کنید.
- راه‌اندازی: فقط کافی است ربات را به‌عنوان منبع مدل انتخاب کنید و از دستورات ساده برای تنظیم پارامترها استفاده کنید.
برای شروع، ربات را در تلگرام پیدا کنید و دستور
/start
را بفرستید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/4823" target="_blank">📅 14:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📌
ربات برای ssh زدن به سرور:
@EazySSH_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/4822" target="_blank">📅 14:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq-_da3faj31PhhWQUyUEWnaFWbUQKofH_annVS89jTvVXZV10EB71fJYxGFQ-mTp5UJgajvLCex4hBBjdW46HngpE2gXmY5ztfchZ-HtbvWO6FWFQQTDvG9F9ncqbtTDOaRCzbyAlkXX1igIwdIiKd-I5mW6oVLkt4nPaw0J_Sz1TL3gAnNJXUbulwCeYg5GMclHrOjxE5QmYQxi3JfrFI0v_Yjby2yW0CkTQsKJ4CAUzC3ahI5VX0ZJLaIJQyyLU7jWRVMHBeEeW1xeAOg8tzOIfA08jGn8DA-PsrcbBB9QCdx_v9wsL5VcZN-iYVvUiTGeILwHrVFevDxuQxAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🚀
وصل شدیم (بقیه سرور ها هم بزودی فیکس میشن)
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/4820" target="_blank">📅 12:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دوستان ، تغییر نتلیفای کسایی که قطع شدن
نمیدونم با این تغییر چقدر دووم داشته باشه من که فعلا وصلم.
یه تغییری باید سمت سرور و کلاینت بدید
اگه سرور ندارید صبر کنید صاحب سرور انجام بده خبر بده
سمت سرور
:
اگه پنل ثنایی دارید ، قسمت inbound
یه فیلد هست نوشته
padding bytes :
و خالیه شما بکنیدش 1-1
اینجوری میشه :
padding bytes : 1-1
اگرم xray دستی نصب کردید و پنل ندارید باید فایل config.json ادیت کنید زیر path همینو اضاف کنید که احتمالا بلد باشه هرکی دستی نصب کرده.
حالا
سمت کلاینت :
کانفیگتون رو ادیت کنید (علامت مداد)
زیر path
عنوانش نوشته Xhttp extra raw JSON...
داخلش اینو بنویسید یا اضاف کنید
{ "xPaddingBytes": "1-1" }
اگر خالی نیست هم همچین فرمتی میشه(البته من از فرمت بالا استفاده کردم این پایینی رو یکی از بچه ها فرستاده تست نکردم) :
{"headers":{"x-host":"netlify.parsashonam.sbs:444"},"xPaddingBytes":"1-1","scMaxEachPostBytes":"1000000"}</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/4819" target="_blank">📅 11:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتلیفای وصل
kubernetes.io
،
50.7.5.83
65.109.34.234
،
kustomize.sigs.k8s.io
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/4818" target="_blank">📅 11:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4817">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👾
لیست دانلود برنامه ها با نت ملی
1️⃣
WhiteDNS
1.1.0
(نسخه ی رسمی)
4️⃣
NekoBox v8a
●
NekoBox v7a
1.4.2
7️⃣
The Feed
0.17.5
📱
Telegram
(گوگل پلی)
12.7.2
📱
Telegram
(رسمی)
12.7.2
📱
Telegram
(Windows)
12.7.2
📱
Whatsapp
2‌.26‌.17.‌72
💬
Instagram
v415.0.0.36.76
👑
ShiroKhorshid
2026.03.17
5️⃣
Mhrv Rs
v1.9.14
📶
Npv
123
📶
V2box
5.3.4
📶
V2ray Ng
2.18
📶
V2ray Ng
(Windows)
3️⃣
Am tunnle
(pro)
37
3️⃣
Am tunnle
(lite)
🕊
Slipnet
2.5.3
2️⃣
Masterdns
1.0.9
📶
Open vpn
3.71
📱
Happ
3.20.4
💻
Happ
(Windows)
📶
Psiphon
462
📶
Psiphon
(Windows)
8️⃣
Bd net
104
6️⃣
Mahsang
15
📶
http injector
6.5.0
📶
Wireguard
1.0.20260315</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/4817" target="_blank">📅 11:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4816">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">لینک داخلی V2rayn ویندوز
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/4816" target="_blank">📅 11:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به زودی جنگ میشه..
دارن همه راه ها رو میبندن تا دوباره فقط آیپی های وایت وصل بمونن و قیمت رو ببرن بالا</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4815" target="_blank">📅 08:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4814">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جدیدترین سریال ها
https://www.nilfgaard.top
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/4814" target="_blank">📅 07:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه سری گفتن نتلیفای وصل شده دوباره ولی برای من نشده. برای دوستانی که از نتلیفای لعنتی رکب خوردن:
(شکن ظاهرا تو این قطعی نقشی نداشته ولی از کجا معلوم پشت پرده یه صحبت ریزی کرده باشن!)
یه راه حل
موقت
(امیدوارم آدما‌ی نتلیفای اینجا نباشن) که کانفیگ رو دوباره زنده میکنه ولی Pros and Cons خودش رو داره از این قراره: PaddingBytes رو توی کانفیگ غیر فعال کنید و کانفیگتون به کار می‌افته طبق مراحل زیر. قبل از هرچیز: من اینا رو با شکن تست کردم و جواب داد ولی شما باید خودتون اینو تست کنید. اساسا ایده‌ی xPaddingBytes برای مبارزه با DPI بوده و شاید این روش مناسب نباشه.
۱. برای سمت کلاینت v2Ray، این بخش رو به XHTTP Extra Raw Json کانفیگ اضافه کنید تا پدینگ بشه فقط یک بایت. (و بعد مطابق معمول کانفیگ رو به صورت لینک یا JSON بفرستید برای بقیه)
{ "xPaddingBytes": "1-1" }
همچنین ظاهرا ویژگی‌های ظاهری پدینگ هم قابل تغییر و رندوم کردن هست (پیش‌فرض فقط ۱۰۰ الی ۱۰۰۰ تا X). با این من راهی پیدا نکردم که پدینگ رو کامل خاموش کنه از سمت کلاینت.
۲. مهم: قاعدتا باید سمت سرور هم همین تغییر رو بدید، چون سرور Xray حداقل تا نسخه‌ی 26.3.27 حتما چک می‌کنه که کلاینت این پدینگ رو با سایز درست (که پیش فرض اندازه‌ی ۱۰۰ تا ۱۰۰۰ بایت هست) داشته باشه. دو راه پیش روی من بود، یا این تنظیم رو توی سرور عوض کنم (و از اون ور هم سایز پدینگ بشه ۱ بایت)، یا کلا سرور رو پچ کنم (و البته ظاهرا یه درخواست از طرف توسعه‌دهنده‌ها هم هست برای Xray Xhttp که الزام داشتن پدینگ از سمت سرور برای کلاینت رو حذف کنه).
من سرور رو پچ کردم چرا که می‌خواستم رفتار سرور عوض نشه (و نتلیفای حداقل
هنوز
رفتار سرور براش مهم نیست یعنی پدینگ‌های از سمت سرور رو کاری نداره)، شما می‌تونید تلاش کنید که xPaddingBytes رو توی تنظیمات سرور بذارید "1-1" مشابه کلاینت (من با پنل ثنایی و اینا کار نکردم، یحتمل از اونجا هم میشه این تنظیم رو داد).
اگر می‌خواید مثل من پچ کنید، مشابه تغییر branch پایین (نه main) بیلد کنید برای لینوکس یا غیره و باینری رو جایگزین کنید (فورک از ورژن 26.3.27). بیلد کار پنج دیقس، از AI بپرسید.
🔹
به هیچ وجه باینری از کسی نگیرید! خودتون بیلد کنید.
https://github.com/Sprimesson/Xray-core/tree/feature/no-xpadding-checks
اگر میخواید پچ نکنید و بجاش کانفیگ سرور رو با کلاینت یکی کنید (من تست نکردم) باید ذیل xhttpSettings توی config.json همین اضافه شه مثلا:
"xhttpSettings": {
"path": "/s1",
"xPaddingBytes": "1-1"
}
۳. یه موضوع دیگه که من به نظرم مهمه: من کانفیگ‌هام دو تا نسخه داره Normal و Slow. توی Slow، تاخیر توی ارسال POST اضافه کردم و این باعث میشه پینگ کانفیگ بره بالا ولی روی سرعت آپلود تاثیر ملموسی نداره (برای دانلود هم به نظر میاد فرقی نداره). استفاده از Slow باعث میشه تعداد ریکوئست به نتلیفای لعنتی (که سرگردنه وایساده و قیمت گیگی/ریکوئستی‌ش از رقباش که اونم حرومزادن و دامین فرانتینگ رو بستن بالاتره) کمتر بشه و به عبارتی اقتصادی‌تر باشه. مثال برای XHTTP Extra Raw JSON:
{
"xPaddingBytes": "1-1",
"scMaxEachPostBytes": "4000000",
"scMinPostsIntervalMs": "500-1000",
"scMaxBufferedPosts": 30,
"scStreamUpServerSecs": -1,
"xmux": {
"maxConnections": 3,
"hMaxRequestTimes": 0,
"hMaxReusableSecs": 0,
"hKeepAlivePeriod": -1
}
}
این JSON ها وارد لینک کانفیگ میشن و مشکلی نیست.
Source</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/4813" target="_blank">📅 07:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">aio‑downloader  اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده. این…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/4811" target="_blank">📅 00:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">aio‑downloader
اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
لینک پروژه:
https://github.com/ProAlit/aio-downloader</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/4810" target="_blank">📅 00:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I__83P7Oc-WN91j4YyWrwTEqiILqOnNgfemeOoBEaE1Yxtq_xnv3yDghmt8aP2umYEKD23Rkkn-jLcqI1DEu9imSkrnT4F9gCydkOYFVzRmC_Ir2KMZy0WS-MMO_zpw81gpX-oTasKZcnOx8cx_IBc2_xhmdeYVVxDY1jKbhhiUgA_oYrhDPo6WrFKVegc3pen9d3t2CZh47tpQ-3sn-_5yZR4gTs5oB1UvW_P9Su6n8yLcESW_sV-amHpLsUdIHiKz75JmAjUqNZ1IlzRFXK4wh41MD2iSa0TzreH6mP5Z5dyX1A0uJhCBmP4TbYiv9-GspKzQl2ezNv7hoDiRKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتلیفای بای بای       @ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/4802" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تا ۱۰ روز دیگه جنگ میشه..</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/4800" target="_blank">📅 00:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتلیفای بای بای
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/4798" target="_blank">📅 00:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سایت های موزیک بدون فیلتر
http://toogoosh.com
https://rozmusic.com/
https://upmusics.com/category/single-tracks/
https://musics-fa.com/download-songs/
https://bir-music.com/
https://biamusic.ir/
https://mahanmusic.net/top-songs/
https://radio.biato.in/
http://Sptfy.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/4797" target="_blank">📅 00:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فیلم و سریال بدون سانسور
Movieyaab.ir
f2mux.top
www.myf2mi.top
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/4794" target="_blank">📅 23:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سایت داخلی برای دانلود frimware ios
https://ipsw.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/4793" target="_blank">📅 23:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چطوری تشخیص دهیم سرور شما اسپوف خور هست
؟
روی سرور مقصدت بزن
tcpdump icmp
بعد روی سرور ایرانت بزن
iptables -t nat -A POSTROUTING -d TARGET-IP -j SNAT --to-source SPOOF-IP
ping -c 10 TARGET-IP
تارگت ایپی ایپی سرور مقصده،
اسپوف آیپی ایپی ای که سفیده میخوای اسپوفش کنی
اگه تو ترمینال سرور مقصدت پکت ها اومد و ایپی جعلی روشون بود ایرانت میتونه اسپوف بزنه اگه هیچی نیومد تو tcpdump اسپوف خور نیست.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/4792" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ربات جمنای
@Gemini_PV_bot
@NewGeminiAi_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/4791" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ربات های هوش مصنوعی همه مدل ها
@chat_llm_100_bot
@GPT4Telegrambot
@GratomicAiBOT
@GPT4_Unlimit_bot
@GPT4AgentsBot
@grok_gidbot
@ChatGPT_grok4bot
@ChatGPT_General_Bot
@Javidiran_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/4790" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4789">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آموزش_اپلود_و_استفاده_اسکریپت_در_کولب_گوگل.pdf</div>
  <div class="tg-doc-extra">2.5 MB</div>
</div>
<a href="https://t.me/archivetell/4789" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت) خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟ ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها،…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/4789" target="_blank">📅 23:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ربات تبدیل ویس به متن
@VoiceToTextMasterBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/4785" target="_blank">📅 19:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
امروز می‌خوایم درباره موضوعی حرف بزنیم که احتمالا از این به بعد بیشتر اسمش رو می‌شنوید؛ مخصوصا برای کسایی که خرید
کارت به کارت
کانفیگ از شخص یا ربات انجام میدن
❗️
یه سری گزارش بهمون دادن
از طرف No Caller ID براشون زنگ زدن و سوال‌هایی مثل:
● شما به شخص "برفرض قلی زاده" واریز کردید میشناسیدش؟
بدبینانه ترین حالتش اینکه:
● ما از تماس**** میگیریم شما از کجا کانفیگ خرید کردید؟ بیاید اداره تعهد بدید و بیاید اینجا توضیح بدید دارید چه کاری با vpn انجام میدید.
اول باید یه نکته مهم رو بدونید:
خیلی از فروشنده‌های کانفیگ، پرداخت رو به‌صورت کارت‌به‌کارت انجام میدن که بتونن مشتری بکشن این کارت‌ها معمولا دو حالت دارن:
۱️⃣ یه سری فروشنده‌ها مدت طولانی از یک کارت ثابت استفاده می‌کنن و ظاهرا مشکلی هم براشون پیش نمیاد (پارتی دارن)
۲️⃣ یه سری دیگه مدام کارت عوض می‌کنند بصورت روزانه و هفتگی ؛ بحث اصلی ما با این دسته‌ست.
مشکل از جایی شروع میشه که ۱۰۰٪ از این کارت‌ها اجاره‌ای هستن.
معمولا بعد از مدتی حساب مسدود میشه و صاحب کارت باید بابت تراکنش‌ها توضیح بده و درگیر دردسرهای پولشویی و قضایی بشه.
از اون طرف، تمام تراکنش‌ها داخل سیستم بانکی ثبت میشن:
شماره حساب، اسم و شماره طرفین، مبلغ، زمان تراکنش و...
حالا اگر مشخص بشه اون حساب برای فروش VPN یا کانفیگ استفاده میشده، طبیعیه که تراکنش‌ها و افراد مرتبط بیشتر بررسی بشن.
که ۱ ماه پیش خبر این تو کانالها پخش شده بود از پیش شماره Vaja برای کانفیگ فروش هایی که مستقیما از کارت خودشون استفاده می‌کردن پیام رفته براشون
🤔
حالا میپرسید راه‌حل چیه؟
تا جای ممکن کارت به کارت نکنید.
بهتره به جای این مدل پرداخت‌ها از روش‌هایی استفاده بشه که مستقیم به کارت‌به‌کارت نباشن؛
مثلا پرداخت از طریق تراست ولت یا صرافی‌های ارز دیجیتال مثل نوبیتکس یا بیت‌پین و خیلی صرافی های دیگه که ثبت‌نام تو این صرافی ها هیچ سختی نداره و عرض ۵ دقیقه ثبت‌نام میشه کرد
در نتیجه پیشنهاد میشه تا حد امکان از کارت‌به‌کارت به حساب‌های متفرقه خودداری کنید
میگید به خودتون چرا مشکلی نداره که؟ اینم فکرشو بکنید که بابت کانفیگ ۲۵۰ تومنی برید خودتون رو به دردسر انداختید و حالا باید جواب هم پس بدید
🥴
این موضوع احتمالا در هفته‌ها و ماه‌های آینده بیشتر درباره‌ش خواهید شنید که  از No Caller ID تماس گرفته شده. خیلی‌ها الان جدی نمی‌گیرنش، ولی بعدا درگیر این موضوعات میشن که دیگه خیلی دیر شده
ℹ️
هدف ما ترساندن نیست و صرفا جهت آگاهی و امنیت شما اطلاع رسانی شده
❤️‍🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/4784" target="_blank">📅 18:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
قابلیت جدید Codex
با یک کلیک انتقال پروژه‌ها/گفتگوها بین Claude و Codex
- استفاده از قدرتمندترین مدل برای کدنویسی هوش مصنوعی
- صرفه‌جویی در زمان و بهبود کار تیمی
https://chatgpt.com/codex/switch-to-codex/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/4782" target="_blank">📅 17:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Balancer_ArchiveTell.html</div>
  <div class="tg-doc-extra">28.3 KB</div>
</div>
<a href="https://t.me/archivetell/4781" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Balancer.html</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4781" target="_blank">📅 16:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎉
۸ ابزار هوش مصنوعی فقط برای سرگرمی
1️⃣
هنرمند تتو – طراحی خودکار تتوهای خلاق
🔗
https://tattoosai.com
2️⃣
صحبت با کتاب‌ها – گفتگو با متن‌های کتابی به‌صورت صوتی
🔗
https://books.google.com/talktobooks/
3️⃣
عکس‌های قدیمی – بازسازی و رنگ‌آمیزی تصاویر تاریخی
🔗
https://myheritage.com/ai-time-machine
4️⃣
سلام به گذشته – تعامل با شخصیت‌ها و رویدادهای تاریخی
🔗
https://hellohistory.ai
5️⃣
جعل خود – ساخت صداهای مصنوعی شبیه به خودتان
🔗
https://fakeyou.com
6️⃣
وعده غذایی غیرواقعی – منوهای خیالی و جذاب برای لذت بصری
🔗
https://unrealmeal.ai
7️⃣
تغییر چهره با هوش مصنوعی – سوئیچ و ترکیب چهره‌ها به‌صورت لحظه‌ای
🔗
https://hey.reface.ai
8️⃣
تغییر صدا – تبدیل صدا به انواع شخصیت‌ها و افکت‌ها
🔗
https://voicemod.net
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4780" target="_blank">📅 16:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Balancer.html</div>
  <div class="tg-doc-extra">13.2 KB</div>
</div>
<a href="https://t.me/archivetell/4779" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
ابزار اختصاصی ساخت کانفیگ بالانسر برای v2rayNG
🚀
> خسته شدی از بس دستی بین کانفیگ‌ها سوییچ کردی تا یه سبزشو پیدا کنی؟
با این ابزار ساده، تمام کانفیگ‌هاتون (حتی لینک‌های نامرتب با پروتکل‌های جدید مثل xhttp) رو یکجا وارد می‌کنید و در ازاش یک «کانفیگ کاستوم هوشمند» تحویل می‌گیرید.
>
⚡️
چیکار می‌کنه؟
> این کانفیگ به صورت خودکار پینگ تمام سرورهای شما رو (مثلاً هر ۶۰ ثانیه) چک می‌کنه و ترافیک شما رو بدون قطعی روی
سریع‌ترین سرور
میندازه (LeastPing).
>
🔒
۱۰۰٪ امن و آفلاین (توی مرورگر خودتون اجرا میشه)
>
📥
کافیه فایل HTML رو باز کنید، کانفیگ‌ها رو بدید و خروجی JSON رو توی v2rayNG کپی کنید. فق دستی کپی کنین
‌
🆔
@archivetell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/4779" target="_blank">📅 16:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستان برنامه نویس خیّر اندروید کسی هست؟
کار اونقدی سخت نیست
دایرکت یا پی وی پیامم بده
کار عام المنفعه هست برای اتصال به اینترنت</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/4778" target="_blank">📅 16:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWsNe_I4nOK3jy_cZK0DyinitGvt79GITLLMmV3PRnuzEw9Oo68L1jyLmfrw3PRGrs_36WMVHiZ_icSu3IG494zG1W211HLU0NPs3cLHnBGIpB85RwsadUgP5A1YzmKLuVEd0RBiiALE-5NymuXYaFZYQZqfs_Jm9QRZobQcr9rFkadSWAqriMsZIbHaTBN0dwCuvjqENBOiGyLHbAAmnGcl2FoWx9YcEcBcOfHazyu_TROO3Vm9ggZhm0OeqLMbcdFYW5pLfUYRg4PDv5hH8Z-NK9Dd8EBHDPs8V0R72H11rXoHMZQTjRgNwju74b3lNt6-O_Iouf7zscLkx_zJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🌐
اضافه شدن سرور های جدید ( اهدایی عزیزان
❤️
)
🔺
بهینه شدن لیست BEST
⚡️
اضافه شدن sni های جدید
●  کانفیگ ساز جدید فقط روی
نسخه 1.0.3 پروژه
کار میکنه
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/4777" target="_blank">📅 14:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ربات فشرده‌سازی فایل‌های PDF
📖
📚
@PDF_Compress_Robot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/4776" target="_blank">📅 13:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ez04vajQNFERWq7INDifwlrF2crKzbkZU0e_iXSOesx-Z7RyjwvoEfJgF_txOKwnGrZNW4oSG_yeZ6FAIQaJBq2rBEYPgikadYXcRfwAGIwDbMAItNQFhju9OFoGEyaiFGmL89EQ80S6z3YMe0Ws_ulo0qabuHwm3S1HsIKlTEaVVkD1q_Cjr1vzYa5-9MSExT_huQeoxT4lVflEGFKGg8nymqvcIvyZii6g_SMuwRJK5gAfKbLjg41G71NnZj7m_K_9gpXzhG-6XfhHYDSeeQQBku4Qjbuo5LkIhcCJDkNhBuC_xC-4kldxNczCVYSFREuwLcpfRdahU7IT62cPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
MattDownloader
نسخه اول منتشر شد
❤️
می‌خوای ویدیو از یوتیوب (یا هر لینک دانلودی دیگه رو) بدون VPN بگیری؟ با MattDownloader این امکان میسر میشه:
GitHub Actions روی فورک خودت فایل را از اینترنت دانلود میکنه و آماده‌اش میکنه؛ تو فقط با اپ از همون گیت‌هاب بدون اینکه روی گوشی VPN لازم داشته باشی، فایل نهایی رو می‌گیری و ذخیره می‌کنی. یعنی گوشی بیشتر با گیت‌هاب حرف میزنه، نه مستقیم با سایتی که برات مسدود یا ناپایدار است.
چطور کار میکنه؟ لینک را به اپ می‌دهی (مثلاً لینک ویدیوی یوتیوب که به لینک مستقیم تبدیلش کردی)، ورک‌فلو روی ریپوی تو اجرا میشه، بعد اپ فایل آماده را از مسیر jobs میخونه و روی دستگاه دانلود میکنه.
🎬
مناسب برای ویدیوهای یوتیوب و لینک‌های سنگین
⚡
ست‌آپ یک‌بار با توکن و آدرس فورک
📥
دانلود نهایی از گیت‌هاب
🖼️
امکان ذخیره در گالری برای ویدیو/عکس
راهنما و APK اینجاست:
https://github.com/matthewnet/MattDownloader
آخرین نسخه برای نصب:
https://github.com/matthewnet/MattDownloader/releases/latest
تجربه‌تون را بفرستید
💙
برای دریافت نسخه‌های بعدی:
@mattspoof</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/4774" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت) خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟ ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها،…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/4773" target="_blank">📅 12:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8KjCuCRl6XC5mQlBFEzJ6Qy1pKiYSEZHXnHbFbY90Cuug1bq-HlOHPWkAwDfSo5zwyFPqvw0bNMSSMKZTt9--3K7Xmaf2u3R9LpJwLlaIz31ksQekY_5gdnyme8ZOb7UKikZOiu5Q09IvSpcm6Cg3XGGtoqYnm42wjFWMEpxVNOhhmpBsOmLXzhxWGk51t3hfINexZ_O00p5rv6MQ_mEDmeSwcTDbfxWrdrXEDmk0udyCFj0CCokLAEh4R5CPcYfDl2oBZ2ioOWW4yYgEGW_UUf-RDPqvKRCyN8s_BSA1ttmLgGHMVwxtuSNtKqMJ0-4RbtxvlzeJeZmwGrUzXIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت درحال احراز کردن IP سرور های ایران هستش. اینطوری صاحب هر IP برای حکومت کاملا مشخص میشه.
قبل از این، دیتاسنتر ها احراز رو خودشون انجام میدادن اما برای اکانتی که میسازید نه IP سرور. اگه حکومت هر دستوری بابت پیگیری IP خاصی میداد، باید از فیلتر ISP عبور میکرد که میشد با روش هایی دورش زد یا گردن نگرفتش
اما الان خود حکومت دیگه میدونه کدوم IP برای چه شخصی هستش...
@ArchiveTell
Source</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/4772" target="_blank">📅 12:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ربات تبدیل صدا به متن رایگان
@sedatextbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/4771" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
آموزش صفر تا صد راه‌اندازی تونل ریورس (Reverse Tunnel) در 3x-ui
---
رفقا سلام!
✋
امروز یه آموزش پایه‌ای اما به‌شدت کاربردی داریم برای راه‌اندازی تونل Reverse بین دو پنل 3x-ui (سرور ایران و خارج).
ممکنه بسته به شرایط سرورتون نیاز به یه سری تغییرات ریز داشته باشید، اما ساختار اصلی و تضمینی همینه!
مرحله ۱: ساخت Inbound روی سرور ایران
🇮🇷
1️⃣
وارد پنل 3x-ui سرور ایران بشید و به بخش Inbounds برید.
2️⃣
دو تا کانفیگ باید بسازید:
🔸
کانفیگ اول (برای Tunnel):
• Protocol: VLESS (یا پروتکل دلخواه)
• Transport: WebSocket
• Path: /tunnel
• Remark: tunnel
• Port: حتماً یکی از پورت‌های پشتیبانی‌شده توسط CDN (مثلاً 8080 یا 2082)
🔸
کانفیگ دوم (برای User):
• Protocol: VLESS
• Transport: WebSocket
• Path: /user
• Remark: user
• Port: یکی از پورت‌های CDN (مثلاً 8080)
⚠️
نکته به‌شدت مهم: حتماً از پورت‌هایی استفاده کنید که CDN (مثل ابرآروان یا کلودفلر) اجازه می‌ده؛ مثل: 80, 443, 8080, 2052, 2082, 2086, 2095.
مرحله ۲: تنظیم Reverse روی سرور ایران
🇮🇷
1️⃣
برید به بخش Xray Config و بعد تب Reverse.
2️⃣
یه Reverse جدید بسازید (بخش Portal):
• Tag: portal
• Domain: یه اسم دلخواه (دقت کنید که روی سرور خارج هم باید دقیقاً همین باشه).
3️⃣
حالا Mapping رو انجام بدید: کانفیگ tunnel رو وصل کنید به user (یعنی Tunnel ➔ User) و ذخیره کنید.
مرحله ۳: انتقال کانفیگ به سرور خارج
🌍
1️⃣
از کانفیگ tunnel (که تو ایران ساختید) خروجی (Export) بگیرید.
2️⃣
وارد پنل سرور خارج بشید و برید به بخش Outbounds.
3️⃣
یه Outbound جدید بسازید و لینک ایران رو اونجا Paste کنید.
(دقت کنید که دامنه‌تون باید پشت CDN باشه و به آی‌پی سرور ایران اشاره کنه).
مرحله ۴: تنظیم Reverse روی سرور خارج
🌍
1️⃣
تو پنل خارج برید به بخش Reverse.
2️⃣
یه Bridge بسازید:
• Tag: bridge
• Domain: دقیقاً همون دامین/اسمی که تو سرور ایران گذاشتید.
• Interconnection: همون Outboundی که تو مرحله قبل ساختید.
• Internet: روی direct یا freedom تنظیم کنید.
3️⃣
سیو کنید و تمام!
✅
نتیجه چی می‌شه؟
سرور خارج به ایران متصل می‌شه ➔ تونل ریورس برقرار می‌شه ➔ کاربر به سرور ایران وصل می‌شه و اینترنت آزاد رو از سرور خارج دریافت می‌کنه!
💡
نکات طلایی و عیب‌یابی:
🔹
مسیرها (Path): پث‌ها (مثل tunnel/ و user/) باید مو به مو یکی باشن. یه اسلش (/) اضافه یا کم، کل کار رو خراب می‌کنه.
🔹
نقش CDN: بدون CDN این روش یا کار نمی‌کنه یا شدیداً ناپایداره. حتماً پشت CDN باشید و تیک WebSocket رو هم تو تنظیمات CDN روشن کنید.
🔹
نیاز به TLS یا Nginx: استفاده از Nginx الزامی نیست ولی برای تمیزیِ کار، روت کردن پث‌ها و استفاده از پورت 443 خیلی جوابه. TLS هم بستگی به شبکه داره، بعضی جاها فقط با 443 جواب می‌ده.
🔹
مشکل وصل شدن بدون اینترنت: اگه وصل شدید، چند کیلوبایت سند و ریسیو داشتید ولی اینترنت نبود، شک نکنید مشکل از ایناست: اشتباه بودن Path، مشکل تو هدرهای Upgrade/Connection، مپ نشدن درست Reverse یا گیر دادنِ CDN.
📌
#آموزش
#تونل
#ریورس
#Reverse_Tunnel
#سنایی
#3x_ui
#vless
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/4770" target="_blank">📅 11:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سایت ارسال کانفیگ
http://m.ulni.ir
https://sphost.theazizi.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/4769" target="_blank">📅 09:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آپلودر های فعال
https://up.zaringo.sbs/
https://rozup.ir/
https://uploadgirl.ir/
https://seup.shop/
http://uplod.ir
https://up.20script.ir
https://punkpaste.ir
https://my.files.ir
https://toolschi.com/tools/upload-center
http://nixfile.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/4768" target="_blank">📅 09:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ربات کاهش حجم ویدئو رایگان
@mediaEasyBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/4767" target="_blank">📅 09:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کاش زودتر آیفون ۱۸ بیاد که آیفون ۱۷ ارزون‌ تر بشه بتونیم تن ماهی بخریم.
@archivetell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/4765" target="_blank">📅 00:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">IR NETLIFY V10.2 • BACHELOR EDITION
⚡️
تغییرات اصلی نسبت به نسخه‌های قبلی: ۳ تب کامل و حرفه‌ای:
⚡️
Generator — با پشتیبانی از چندین دامنه نتلیفای (داینامیک)
🔄
Replacer — جایگزینی دامنه با قابلیت توزیع خودکار بین چند دامنه
🔧
Tools — ابزارهای پیشرفته (Rename…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/4764" target="_blank">📅 00:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👾
لیست دانلود برنامه ها با نت ملی
1️⃣
WhiteDNS
1.1.0
(نسخه ی رسمی)
4️⃣
NekoBox v8a
●
NekoBox v7a
1.4.2
7️⃣
The Feed
0.17.5
📱
Telegram
(گوگل پلی)
12.7.2
📱
Telegram
(رسمی)
12.7.2
📱
Telegram
(Windows)
12.7.2
📱
Whatsapp
2‌.26‌.17.‌72
💬
Instagram
v415.0.0.36.76
👑
ShiroKhorshid
2026.03.17
5️⃣
Mhrv Rs
v1.9.14
📶
Npv
123
📶
V2box
5.3.4
📶
V2ray Ng
2.18
📶
V2ray Ng
(Windows)
3️⃣
Am tunnle
(pro)
37
3️⃣
Am tunnle
(lite)
🕊
Slipnet
2.5.3
2️⃣
Masterdns
1.0.9
📶
Open vpn
3.71
📱
Happ
3.20.4
💻
Happ
(Windows)
📶
Psiphon
462
📶
Psiphon
(Windows)
8️⃣
Bd net
104
6️⃣
Mahsang
15
📶
http injector
6.5.0
📶
Wireguard
1.0.20260315</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/4763" target="_blank">📅 23:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtW_bVZnqqReSGjLNyP2pPJn-IgcI4FZij0vab3D_mX_PQHS6toJwvQWUvbbboIPRWESV4nAdhXop3NiXv54aGi8YhT810wt-xMGtIUAjpgfKXa3LMlWn7WSWpVYvybAIMoQ-VdxybDnTyTVEX0Qj02MzodWPuSraLv7QvYXAB0l16pwD0g4_vaKSoRWLfk97660KQL2yaoBFgfukZi6u4vmIC2mm-Wdj2axGquMYrTFf0-ZyOvKqRg1TyhRjkFUewkK8lUBVOLbg0uc96Glv--4DibtVGJ1IZIiNnO8FINWm_O8DYClxCHEJEbjYmysK4SxO83669h_yndsOEfc2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
بومی‌سازی هوش مصنوعی برای توسعه‌دهندگان.
ترجمه YAML، JSON، TXT و محتوای چندزبانه با حفظ ساختار، جایگزین‌ها، متغیرها و قالب‌بندی.
@LocalynBot
⭐
کد منبع گیت هاب
https://github.com/LocalynAI/LocalynAI
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/4761" target="_blank">📅 22:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">YT_dL.ipynb</div>
  <div class="tg-doc-extra">22.5 KB</div>
</div>
<a href="https://t.me/archivetell/4760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/4760" target="_blank">📅 21:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت)
خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟
ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها، فایل‌های صوتی و حتی پلی‌لیست‌های کامل یوتیوب رو با بالاترین کیفیت ممکن (تا 4K) دانلود کنید.
💡
هدف و مزیت اصلی این اسکریپت چیست؟
تمام فرآیند دانلود توسط سرورهای قدرتمند گوگل انجام میشه. این یعنی شما می‌تونید ویدیوهای چند گیگابایتی رو در چند ثانیه دانلود کنید، بدون اینکه حتی یک مگابایت از حجم اینترنت گوشی یا سیستم شما کم بشه!
🛠
چطور از این ابزار استفاده کنیم؟ (بدون نیاز به کدنویسی)
استفاده از این اسکریپت به شدت ساده است و دارای یک رابط کاربری (فرم گرافیکی) است:
1️⃣
اسکریپت را در گوگل کولب باز کنید (فقط به یک اکانت جیمیل نیاز دارید).
2️⃣
در فرمی که می‌بینید، لینک یوتیوب رو پیست کنید.
3️⃣
کیفیت ویدیو (مثلا 1080p) یا فرمت صوتی (مثلا MP3) رو از منوی کشویی انتخاب کنید.
4️⃣
دکمه اجرا (Play
▶️
) رو بزنید و تمام! اسکریپت به صورت خودکار ابزارهای لازم رو نصب کرده و دانلود رو شروع می‌کنه.
📁
فایل‌های دانلود شده کجا ذخیره میشن؟
در تنظیمات فرم، گزینه‌ای برای اتصال به گوگل درایو وجود داره. اسکریپت به صورت خودکار به درایو شما متصل میشه و فایل‌ها رو در پوشه‌ای به نام YouTube_Downloads (یا هر اسمی که خودتون در فرم بنویسید) ذخیره می‌کنه. بعد از اتمام کار، کافیه برنامه Google Drive رو باز کنید تا فایلتون رو اونجا ببینید!
🔗
لینک ورود به اسکریپت:
[لینک گوگل کولب خود را اینجا قرار دهید]
👇
اگر سوالی در مورد نحوه استفاده داشتید توی کامنت‌ها بپرسید.
Developer : Samad.R
@ArchiveTell
‌
#یوتیوب
#دانلودر
#گوگل_کولب
#ترفند_آموزشی
#ابزار_کاربردی
#دانلود_از_یوتیوب</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/4759" target="_blank">📅 21:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c7bc1a6d.mp4?token=V7nRmsA4PL3ynyebdTO2_KgWigLdG0Mn8uLiFNVRSr_YAResow6Jz1Wi4nwCjeJHhTisYIUaN3qQ7JT-sQUPEgvviMAd-j5mvfwLV_uOeoVLGLITdv2Cgl9LZaUGtcjEtFyZfGrIO310ORnVaBPv0MW4kYCYp4ZaqT6cSl1sFnOyYVq8Ua6JFpmyjJjHiR5rjGSs91bFMywVbLLozKThVnqVmp6Xl7TN-KRZGBK6P-x_MC8O_DkxBLG1AHlzKkh89NRZ7T9bdl_IotsdcBUm7he5Yt5-depr-EUHFLys4-mu_fc2VWqMt4UaFyjSdtoHWKog-nAjyCHudt33mh8CbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c7bc1a6d.mp4?token=V7nRmsA4PL3ynyebdTO2_KgWigLdG0Mn8uLiFNVRSr_YAResow6Jz1Wi4nwCjeJHhTisYIUaN3qQ7JT-sQUPEgvviMAd-j5mvfwLV_uOeoVLGLITdv2Cgl9LZaUGtcjEtFyZfGrIO310ORnVaBPv0MW4kYCYp4ZaqT6cSl1sFnOyYVq8Ua6JFpmyjJjHiR5rjGSs91bFMywVbLLozKThVnqVmp6Xl7TN-KRZGBK6P-x_MC8O_DkxBLG1AHlzKkh89NRZ7T9bdl_IotsdcBUm7he5Yt5-depr-EUHFLys4-mu_fc2VWqMt4UaFyjSdtoHWKog-nAjyCHudt33mh8CbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
گوگل در حال آزمایش Gemini Omni
✅
قابلیت تولید ویدئو – جایگزینی مدل‌های Veo با یک خط تولید یکپارچه.
✅
همزمان خروجی صدا و تصویر – ترکیب چندرسانه‌ای پیشرفته.
✅
معرفی رسمی – انتظار می‌رود در Google I/O هفته آینده به‌صورت کامل اعلام شود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/4756" target="_blank">📅 19:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram-X-0.28.3.1785-arm64-v8a.apk</div>
  <div class="tg-doc-extra">56.6 MB</div>
</div>
<a href="https://t.me/archivetell/4755" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی Telegram x
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4755" target="_blank">📅 18:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPYDDhsuPxDVr_hvLk1Qt7XyvHXlNanQalfPncYDGQ_hhXUMfYzx_rlMhN5ERvajbMfjaTNfNe2JCG2J_OkP3xnGonZFoWZcbtcGJJaUr6NtSLvBgs-spH1q_zSzAKlOnJBnwXR9dXvkZL2b0VMMvguLb6ypXaF2-jOhkKYO6V_ED7i27zRE2TpUXMKBUGClKTIFc7wrppw5F84T_jgHDgc9MjVJeyq5jTSf6YrTg4i69JxHzyBJEhFugLh6_H5-ea2KKV7luRrlmXi--XKM8rcdfVg_Ki8t0a4iahCYg3AkRk1GaQ89DZjR0C39hHFA-P9n9FHh0ByAFgjlQxl73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ویژگی‌های کلیدی در آپدیت جدید
🛰
امکان اسکن با DNS شکن
(نسخه آزمایشی، ممکنه کار نکنه)
⚙️
کنترل دستی پردازش‌ها (Thread Control):
قابلیت تنظیم تعداد تردها توسط کاربر برای جلوگیری از کرش کردن (خطای Signal 9) در ترموکس اندروید.
💻
نمایش زنده در ترمینال:
نمایش آنی کانفیگ‌های متصل در صفحه ترمینال، علاوه بر ذخیره در فایل.
🛡
عبور از فیلترینگ هوشمند (DPI):
تست واقعی لایه اپلیکیشن (HTTP Status) برای جلوگیری از دریافت پینگ‌های فیک و دراپ شدن پکت‌ها.
🌐
دیتابیس داخلی غنی:
شامل بیش از ۷۰ دامنه CNCF/Cloud-Native و بیش از ۱۰۰ آی‌پی‌ تمیز CDN (بدون نیاز به فایل‌های متنی جداگانه).
https://github.com/johncarterjourney-rgb/NETLIFY-SCANNER</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/4754" target="_blank">📅 18:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تا ۱۰ روز دیگه جنگ میشه..</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/4753" target="_blank">📅 17:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">77.9 MB</div>
</div>
<a href="https://t.me/archivetell/4752" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی Telegram 12.7.2
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/4752" target="_blank">📅 17:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یکم زمانبره. لیست ایپی ها و sni ها افزایش پیدا کرده و تستش هم دقیق هستش. برا همین طول میکشه. ببرین تو کلاینت Exclave یا V2ray همشون پینگ میده.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/4751" target="_blank">📅 16:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6_AwhaT281vg1oraidHfYGb0_u9mmokAnCom4dspqzp828xIvRLU7kd8GJgWsSv_2rzExXXRCT2jHr7lZt8uhKO9qBBqfoiWhr5yaHT69MJx2I-FuVfRyaPR2JKOP1pZEXPFRYZixJHv4vVKK9uHR9rOikhu48dHy4PuqCK7ltKAmiIf7GS_4AOvzbnnOmZhMStrEk5RXYuh9w8yYi0Nkni4vB_30U9WaAUiwKbB-gULFfPUg5RWXMYTWCX31ppUKeezJZlckPRyMbI2TJPwrE7xHjSeyuakpbJ98p35IG_11XbQ9DYr4RqO7FPLt5vEl8dELh7fXHwWigkKE6niA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ابزار NETLIFY-SCANNER (نسخه V1 Pro)
🔆
اسکنر IP و SNI های نتلیفای  ---  رفقا سلام.
✋
اگر با کانفیگ‌های نتلیفای کار کرده باشید، می‌دونید که خیلی وقت‌ها پینگ دارن ولی عملاً وصل نمی‌شن (پینگ فیک). این اسکنر پایتونی رو برای حل همین مشکل آماده کردیم.  تفاوت اصلی…</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/4750" target="_blank">📅 15:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1RHbHJlROjV1tuFjgt_EzX3R8GHuK9nnFUY72fKFOxpfY8eIsE3z_aiGnLUdBcz9-74_OPlsk5eR4fLclzkMBg7Iu1MoxCvHDje2Es6EBsZPUQQKCAwgds_yCXXEfwGHfczmQkLhRI6gXRJqrrxvZs52Zwjg49ZhfVzhiU6FGjnmkzIOsPmjZ56Nu7qXmy_0wlGxLUaA3He5CugXoLW7xPum95zZRMhRPqE64ca5W5njL5vARm_PwZsD_vbo0w4T0JvHkYII_Qeq4eRnjfp528-Xi3dOIJvmMABDessWLa8wFSjzdX-WPzGom-rrx_1-abLu-08BJJBfaDYH3HGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
اسکنر IP و SNI های نتلیفای
📌
github.com/IR-NETLIFY/NETLIFY-SCANNER
🔺
مواردی که ok میشن بدون نیاز به شکن وصل میشن براتون
🔸
دی ان اس شکن رو کامل حذف کنید از سیستم
🔹
یک بار مودم یا نت رو خاموش روشن کنید تا آیپیتون عوض شه
🔸
بدون هیچ DNS و فیلترشکنی اسکنر…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/archivetell/4749" target="_blank">📅 15:12 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
