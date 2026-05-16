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
<img src="https://cdn4.telesco.pe/file/IMNee_YTOptHYys8uFYSRd2ZnWnlNhgRCjVZNvSCpRyGNsRTUIn6sKj1l7dBNjVZMwsUyILNoM6LZVZhCRsrEiTOG6BHw6lTJuxVyiT7xvCJYARW3HCIN0_OSPTLvDjfWi6ShPs8tGiBKQrahcbWR69mgtJJJLdp1BcSIa6Dd-EEsjuvSiFVHLWP5TZdlwUVMhL0MLLpMm9YViReHw1DbXe4QbTc4egeqycSOMhRakOstWPRleRyxCk1WIRMKAJoF5XBARgTy5K8rNpi5g7ZNLrPe6E9bJVkypUjO_-iIge4R9c0Senovx5EN53u4DQhD1yjQ2RCx3fx6hwjPkJQZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 7.19K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 20:18:30</div>
<hr>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آپلودر های فعال بدون نیاز به ثبت نام
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
https://files.bokhary.fun/dump/
@ArchiveTell</div>
<div class="tg-footer">👁️ 911 · <a href="https://t.me/archivetell/5037" target="_blank">📅 19:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RI_wJ2VBklvD4OjNnfqlqha-V__ODI1Vw2beodTu4puAbwgucikgXOO8M3-GM56pBD-VoWkYi9njHc2CyW2gBFTzSmUG8vXNRDdGKo4Qteyx74E8P2hRnd-rIIaZdt-3kdCr0wbq_5gaoYNIRXsQ3nDUTTNAsTglmi6Psl4f9FwaBjRrZPCslkv_7g0aV6nS7d-RhIBNcVQc49Qc-i1J7-__wHsS6z_dHkXGWGY_Ihdu7X2D4hc-lLl6cf0bSlQMiwoFGNvDUudQo1WvJy2qpPkVlupcPFSfdU6wE-T458DF2dWOo879iEyVTHHtZn23FVIXuAb4zfUuzCGcfPvXZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnF478ZzJt8wyuB1wkmF4Gm4gWoJ2guZZCSzP5e-hGAAUn5p5BQrUW6Ai88JDseQGx4NCIejXfQ9ODsbw2ZOKNGjWcr7M3g6JePSGd9kpRTuC_abMjd8cwVyUfKEEwCGZyymx_DEEq7MwbfD5waJyGShWZ6GRWteYmiruyz_IDPyk-CHLiCvgUODzX9MEvIYr8ou8vxcVLG6CLwDWfvCDlmvmw3EdNGcylE_PQqKHRIgVYrMDfELHYWTmF5U9MvIkmk2WXibz88aIcBSOxLVwCn8qIvlGPE6q8hhLQxW_7FE_lTVH6rp11b0kpwL_t-Zr-WMImUlVhaG5_eWGKLAAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔆
آموزش تغییر دامنه نتلیفای برای وصل شدن
🔺
شکن دامنه نتلیفای رو بلاک کرده به سختی وصل میشن کانفیگا با این روش اوکی میشه
🔸
اینجا لاگین کنید
dash.cloudflare.com
🔹
در بخش
Workers and Pages
روی
Start building
کلیک کنید.
🔸
روی
Start with Hello World!
کلیک کنید و
Deploy
کنید
🔹
روی
Edit code
کلیک کنید و هر چی هست پاک کنید و کد زیر رو وارد کنید
export default {
async fetch(request, env, ctx) {
const url = new URL(request.url);
url.hostname = 'Your.Domain.netlify.app';
const modifiedRequest = new Request(url, request);
return fetch(modifiedRequest);
},
};
🔸
به جای
Your.Domain.netlify.app
باید دامنه نتلیفای خودتون رو وارد کنید و Deploy کنید
🔹
یه ادرس ورکر بهتون میده اونو کپی کنید برید تو سایت نتلیفای در پروژه خودتون بخش دامنه و افزودن دامنه بزنید
🔸
ادرس ورکر رو وارد کنید و
Verify
بزنید
Add subdomain
بزنید
🔹
در بخش
SSL/TLS certificate
حتما روی
Verify DNS configuration
کلیک کنید
🟢
و تمام حالا با ادرس ورکر خودتون کانفیگ بسازید (بازش کنید)
☕️
اموزش ساخت دامنه نتلیفای
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 894 · <a href="https://t.me/archivetell/5035" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">لینک داخلی شیر و خورشید
دانلود
Pass :
@ArchiveTell
انقضا :
۲
روز دیگه</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/archivetell/5034" target="_blank">📅 18:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ArchiveTel
pinned «
🚀
آموزش جامع و صفر تا صد راه‌اندازی XHTTP Relay روی Vercel (روش رایگان و ضد بن)  ---  رفقا سلام!
✋
پیرو معرفی ابزار خفن XHTTPRelayECO و ویدیویی که گذاشتیم، تصمیم گرفتیم کل مراحل رو به صورت یک آموزش متنی و قدم‌به‌قدم براتون ترکیب کنیم تا هیچ‌کس وسط کار گیج…
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5033" target="_blank">📅 18:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBehnam's Folder(BehNam)</strong></div>
<div class="tg-text">نسخه ی 1.3.8 پروژه ی XHTTPRelayECO ورسل منتشر شد
🔥
یه آپدیت ریز زدم. مود های Fast Pipe آپدیت و بهینه شده.
در حال حاظر با دیپلوی مجدد روی توکن Pro Trial تست گرفتم و جواب داده.
تست کنید و نتیجه رو اعلام کنید
❤️
روی اینترنت های مختلف تست کنید
https://github.com/B3hnamR/XHTTPRelayECO/releases/tag/1.3.8</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/5032" target="_blank">📅 18:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
آموزش جامع و صفر تا صد راه‌اندازی XHTTP Relay روی Vercel (روش رایگان و ضد بن)
---
رفقا سلام!
✋
پیرو معرفی ابزار خفن XHTTPRelayECO و ویدیویی که گذاشتیم، تصمیم گرفتیم کل مراحل رو به صورت یک آموزش متنی و قدم‌به‌قدم براتون ترکیب کنیم تا هیچ‌کس وسط کار گیج نشه.
این روش، امن‌ترین و کم‌هزینه‌ترین (رایگان) راه برای دیپلوی XHTTP روی سرورهای قدرتمند Vercel هست.
⚙️
مرحله اول: تنظیمات پنل (مثل 3x-ui)
1️⃣
وارد پنل سرورتون بشید و یه Inbound جدید بسازید.
2️⃣
پروتکل رو روی vless و بخش Network رو روی xhttp قرار بدید.
3️⃣
تو تنظیمات XHTTP، یه مسیر (Path) سخت و رندوم بنویسید (مثلاً
/api-b7f39xrelay
).
⚠️
این مسیر رو کپی کنید، بعداً لازمش داریم.
4️⃣
کانفیگ رو ذخیره کنید و لینک VLESS ساخته شده رو کپی کنید.
(نکته: سرور اصلی شما حتماً باید دامنه و SSL معتبر داشته باشه).
💻
مرحله دوم: اجرای اسکریپت در ویندوز
⚠️
هشدار مهم: برای اینکه اکانت ورسلتون بن نشه، به هیچ‌وجه پروژه گیت‌هاب رو فورک نکنید! فایل زیپ رو مستقیماً دانلود کنید.
1️⃣
پوشه پروژه رو اکسترکت کنید و فایل
Run-Deploy-Windows.bat
رو با دسترسی ادمین (Run as Administrator) اجرا کنید.
2️⃣
تو صفحه باز شده برای نوع لاگین (Auth Mode)، عدد
1
(یعنی Token) رو تایپ کنید و Enter بزنید.
3️⃣
توکن اکانت ورسل خودتون رو پیست کنید (از تنظیمات اکانت ورسل بخش Tokens می‌تونید بسازید).
🏗
مرحله سوم: ساخت و دیپلوی پروژه در ورسل
1️⃣
از منوی اسکریپت، عدد
5
(Deploy as NEW project) رو بزنید.
2️⃣
یه اسم انگلیسی دلخواه برای پروژه‌تون بنویسید (مثلاً
my-fast-relay
).
3️⃣
حالا برای انتخاب مود، عدد
1
یعنی
FAST PIPE LEGACY
رو انتخاب کنید. (این بهترین و ارزان‌ترین حالته که مصرف اکانت ورسل رو صفر نگه می‌داره).
4️⃣
در قسمت TARGET_DOMAIN، آدرس سرور اصلیتون رو با پورت بنویسید (مثلاً
https://panel.mydomain.com:2053
).
5️⃣
در قسمت RELAY_PATH، دقیقاً همون مسیری که تو مرحله اول تو پنل ساختید رو پیست کنید.
6️⃣
منتظر بمونید تا عملیات تمام بشه. در آخر یک آدرس دامنه (مثل
my-fast-relay.vercel.app
) بهتون میده. اون رو کپی کنید.
📱
مرحله چهارم: تنظیمات کلاینت (v2rayN یا V2rayNG)
1️⃣
لینک VLESS که از پنل کپی کرده بودید رو تو برنامه ایمپورت کنید.
2️⃣
برید تو ویرایش (Edit) کانفیگ:
🔸
بخش Address (یا Server) رو پاک کنید و آدرس دامنه ورسل (که تو مرحله قبل گرفتید) رو بذارید.
🔸
پورت رو روی 443 تنظیم کنید.
🔸
در بخش Host و SNI، مجدداً همون آدرس دامنه ورسل رو وارد کنید.
🔸
مطمئن بشید بخش Path دقیقاً همون مسیر اختصاصی شماست.
3️⃣
ذخیره کنید، متصل بشید و از اینترنت آزاد لذت ببرید!
❤️
تشکر ویژه از
@B3hnamR
عزیز بابت توسعه این ابزار فوق‌العاده.
https://github.com/B3hnamR/XHTTPRelayECO
📌
#آموزش
#جامع
#ورسل
#Vercel
#XHTTP
#تونل
#نت_ملی
#ضد_بن
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/5031" target="_blank">📅 18:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">scanner.zip</div>
  <div class="tg-doc-extra">8.5 KB</div>
</div>
<a href="https://t.me/archivetell/5030" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/5030" target="_blank">📅 17:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📡
🔥
آموزش اجرای Scanner در Termux (خیلی ساده)
━━━━━━━━━━━━━━━
📌
این آموزش برای اجرای پروژه Python + Flask هست
📂
فرض: فایل پروژه داخل پوشه Downloads/scanner قرار دارد
━━━━━━━━━━━━━━━
---
🟢
1) دادن دسترسی حافظه به Termux
termux-setup-storage
👆
اجرا کن و گزینه Allow رو بزن
---
📁
2) رفتن به پوشه دانلودها
cd /sdcard/Download
ls
اگر پوشه پروژه رو دیدی:
cd scanner
---
⚙️
3) نصب پیش‌نیازها (Python + Flask)
pkg update && pkg upgrade -y
pkg install python -y
pip install flask
---
🚀
4) اجرای پروژه
داخل پوشه scanner این دستور رو بزن:
python app.py
---
🌐
5) باز کردن در مرورگر
بعد از اجرا، این آدرس رو باز کن:
http://127.0.0.1:8000
---
📁
ساختار درست پروژه:
Download/
└── scanner/
├──
app.py
└── templates/
└── index.html
---
⚠️
نکات مهم:
✔
حتماً Flask نصب باشد
✔
فایل‌ها دقیق داخل پوشه درست باشند
✔
ترموکس اجازه Storage گرفته باشد
---
⚡
خلاصه سریع (One Click Flow):
termux-setup-storage
cd /sdcard/Download/scanner
pkg install python -y
pip install flask
python app.py
---
یکی از ممبرای گل زحمتش رو کشیده
❤️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/5029" target="_blank">📅 17:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
معرفی AniScanner: اسکنر شبکه پیشرفته با پنل گرافیکی تحت وب!
---
رفقا سلام!
✋
اگه از اسکنرهای متنی و محیط خشکِ ترمینال خسته شدید و دنبال یه ابزار شیک و گرافیکی برای پیدا کردن SNI و آی‌پی‌های تمیز می‌گردید، ابزار AniScanner دقیقاً همون چیزیه که می‌خواید.
این ابزار با پایتون نوشته شده و به جای اینکه نتایج رو فقط تو خط فرمان نشون بده، یه داشبورد وبِ زنده (Real-time) و تاریک (Dark Mode) براتون بالا میاره که می‌تونید نتایج اسکن رو خیلی تر و تمیز تو مرورگرتون ببینید!
✨
ویژگی‌های خفن AniScanner:
🔸
اسکن کامل اتصالات TCP و پشتیبانی از UDP
🔸
تشخیص نسخه TLS و اعتبارسنجی دقیق SNI
🔸
تشخیص خودکار CDN و استخراج اطلاعات ASN سرورها
🔸
دارای پنل مدیریت تحت وب با آپدیتِ در لحظه (SSE Streaming)
🔸
کاملاً بهینه شده و سازگار با ترموکس (Termux) گوشی و لینوکس
🛠
آموزش نصب و اجرا (در ترموکس):
خیلی ساده دستورات زیر رو به ترتیب توی ترموکس کپی و اجرا کنید:
1️⃣
آپدیت و نصب پیش‌نیازها:
pkg update -y
pkg install python git -y
2️⃣
دریافت اسکریپت:
git clone
https://github.com/ForExampleZERO/AniScanner.git
cd AniScanner
3️⃣
نصب کتابخانه‌ها و اجرای اسکنر:
pip install -r requirements.txt
python
app.py
🌐
بعد از اجرای دستور آخر، مرورگر گوشیتون رو باز کنید و برید به آدرس زیر تا پنل اسکنر براتون باز بشه:
http://127.0.0.1:5000
🔗
لینک صفحه اصلی پروژه در گیت‌هاب:
https://github.com/ForExampleZERO/AniScanner
📌
#اسکنر
#ترموکس
#لینوکس
#نت_ملی
#SNI
#CDN
#پایتون
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/5028" target="_blank">📅 16:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پروژه خیلی خفنیه
https://github.com/Code-Leafy/G2rayXCodeLeafy
فورک کنید رو گیتهابتون
Codespaces
ران کنید
صبر کنید اماده که شد 1 بزنید کانفیگ رو دریافت کنید</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5027" target="_blank">📅 16:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">و اینکه سامانتل بدون آیپی شیر و خورشید وصله..</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/5025" target="_blank">📅 16:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">و اینکه سامانتل بدون آیپی شیر و خورشید وصله..</div>
<div class="tg-footer">👁️ 442 · <a href="https://t.me/archivetell/5024" target="_blank">📅 16:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Akamai-IPs.txt</div>
  <div class="tg-doc-extra">99.3 KB</div>
</div>
<a href="https://t.me/archivetell/5023" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رنج آیپی های Akamai
حدود 20 میلیون آیپی</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5023" target="_blank">📅 15:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.html</div>
  <div class="tg-doc-extra">21.4 KB</div>
</div>
<a href="https://t.me/archivetell/5022" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر آیپی های شیر و خورشید</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5022" target="_blank">📅 15:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">لینک داخلی شیر و خورشید ، دو تا آپلودسنتر
دانلود
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 430 · <a href="https://t.me/archivetell/5021" target="_blank">📅 12:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شیر و خورشید ایرانسل
23.65.119.52
23.73.2.141
104.110.138.190
104.83.5.202
92.122.166.236
92.122.166.234
92.122.166.237
96.16.122.70
23.67.136.200
23.67.136.202</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5020" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
آموزش اشتراک‌گذاری اینترنت آزادِ «شیر و خورشید» از گوشی به ویندوز
---
رفقا سلام!
✋
اگر تو ویندوز برای اجرای متدهای جدید مشکل دارید، یه ترفند خیلی ساده هست که می‌تونید اینترنت آزاد و بدون فیلترِ کلاینت شیر و خورشید (سایفون) رو مستقیم از گوشیتون به کامپیوتر یا لپ‌تاپتون منتقل کنید!
📋
پیش‌نیاز مهم:
گوشی و کامپیوتر (یا لپ‌تاپ) شما حتماً باید به یک شبکه وای‌فای (مثلاً یک مودم مشترک) وصل باشن.
📱
مرحله اول: تنظیمات روی گوشی
1️⃣
برنامه شیر و خورشید رو روی گوشی باز کنید و وصل بشید.
2️⃣
برید به سربرگ Options و روی More Options کلیک کنید.
3️⃣
اسکرول کنید پایین تا برسید به بخش Network Sharing.
4️⃣
تیک گزینه Share Proxy on Network رو فعال کنید.
5️⃣
یه بار برنامه رو قطع و دوباره وصل کنید تا تنظیمات اعمال بشه.
6️⃣
حالا برگردید به صفحه اصلی (سربرگ Home). اونجا زیر لوگوی شیر و خورشید، دو تا پروکسی نوشته شده؛ ما با HTTP Proxy کار داریم. (شامل یک سری عدد نقطه دار و یک پورت هست).
🖥
مرحله دوم: تنظیمات روی ویندوز
1️⃣
تو ویندوز برید به تنظیمات (Settings).
2️⃣
وارد بخش Network & Internet بشید و از منوی سمت چپ روی Proxy کلیک کنید.
3️⃣
اسکرول کنید پایین تا برسید به بخش Manual Proxy Setup.
4️⃣
گزینه Use a proxy server رو فعال (روشن) کنید.
5️⃣
تو کادر Address، اون آی‌پی که تو گوشی دیدید رو خیلی دقیق (با نقطه‌ها و بدون هیچ فاصله اضافه‌ای) وارد کنید.
6️⃣
تو کادر Port، اون عددی که تو گوشی بعد از علامت دو نقطه (:) بود رو بنویسید.
7️⃣
در نهایت روی Save کلیک کنید.
⚠️
نکته مهم: حواستون باشه تیک گزینه Don't use the proxy for local (intranet) addresses خاموش (غیرفعال) باشه.
✅
تمام! حالا کل ویندوز شما از تونلِ شیر و خورشیدِ گوشیتون عبور می‌کنه و اینترنتش آزاده.
📌
#آموزش
#ویندوز
#شیر_و_خورشید
#سایفون
#اشتراک_نت
#تونل
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5019" target="_blank">📅 12:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شیر و خورشید همراه اول
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5018" target="_blank">📅 11:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شیر و خورشید ایرانسل
92.122.123.128,2.19.204.87,2.19.204.137,2.19.204.144,2.19.204.145,2.19.204.170,2.19.204.184,2.19.204.185,2.19.204.202,2.19.204.210</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5017" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRfvj7vRqcUIptpqmjWDCDJV8e9fFI-vXnlfznQu1F4EIHr1YmkbAWFE6055sOALyA2Rh76syvPthNxVu4iQMzleYkV8zcKTgp5-VX80ySBBe_hfh_aLTEUGLAdeTcBGRwaO_HmyPiQkFQNRJw8ewmP0ZCSMZcIJaoZpigZO0Qa8mATOF1vKXepjpaFEN3Q_VIr1l2oyxZM_KJc1VsoIz2gxczPHq_dfPRpcAcKLd24jvOaFm_9itWorAPXLGBQD9R-pmESqttClfGczemc4Hd9KChFqdyjDtSBnfMSG_B_Cwyuz002O24OMvmTuLjUWgiEJ7FdV_Y_tWxNzwoyuBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت:</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5016" target="_blank">📅 11:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شیر و خورشید
مخابرات
2.17.101.191
2.17.101.188
2.17.101.187
2.23.168.254
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5015" target="_blank">📅 11:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚀
ربات PlayDL: دانلود مستقیم و بدون دردسر از گوگل‌پلی به تلگرام!
---
رفقا سلام!
✋
دانلود برنامه از گوگل‌پلی برای ما ایرانیا همیشه با مکافات همراهه؛ یا تحریمیم، یا فیلتره، یا فایل‌ها به صورت چند تیکه (Split APK) دانلود می‌شن و رو گوشی نصب نمی‌شن!
امروز سورس یه ربات تلگرامی پایتونی به‌شدت کاربردی به اسم PlayDL رو بهتون معرفی می‌کنیم که این مشکل رو ریشه‌ای حل کرده (کاملاً مناسب برای استفاده روی نت ملی و دور زدن تحریم‌ها).
✨
کارهای خفنی که این ربات انجام می‌ده:
🔸
ادغام خودکار فایل‌ها: لینک گوگل پلی رو بهش می‌دید؛ اگه اپلیکیشن چند تکه (Split) باشه، خودش همه رو دانلود می‌کنه، به کمک ابزارهای داخلی به هم می‌چسبوندشون و یه فایل
.apk
تر و تمیز و آماده‌ی نصب بهتون تحویل می‌ده.
🔸
دور زدن فیلترینگ: چون فایل رو روی سرورهای خودش دانلود و بعد تو تلگرام آپلود می‌کنه، می‌تونید فایل نهایی رو با سرعت بالا و بدون نیاز به فیلترشکن دانلود کنید.
🔸
هوشمند و خودکار: قابلیت نصب اتوماتیک پیش‌نیازها و پشتیبانی از دانلودرهای قدرتمندی مثل gplaydl و apkeep رو داره.
🤖
نمونه ربات فعال و آماده (برای کاربرای عادی):
اگر سرور شخصی ندارید که خودتون سورس رو ران کنید، یه ربات آماده و رایگان از همین پروژه بالا اومده که همین الان می‌تونید ازش استفاده کنید و برنامه‌هاتون رو بگیرید:
👉
@APKNitoBot
🛠
برای برنامه‌نویس‌ها و ادمین‌ها:
سورس این پروژه با Python 3.13 و Aiogram نوشته شده. برای ران کردنش روی سرور شخصی به MongoDB، جاوا 17 و البته Telegram Bot API Local Server نیاز دارید. دستورات نصب کامل داخل گیت‌هابش هست.
🔗
لینک سورس اصلی پروژه در گیت‌هاب:
https://github.com/ZethRise/PlayDL
(با تشکر از متین عزیز بابت معرفی این پروژه)
📌
#ربات
#تلگرام
#گوگل_پلی
#نت_ملی
#دانلودر
#پایتون
#PlayDL
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/5014" target="_blank">📅 10:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVxeqVQFplnctCBtEZknp37Fod4Uq9rGq49Fii7vzo_R0KHI6ohi7xZ42Fv8p8XV35D48MOrZBAarv9IThnfwEeInDAxNWlC4j9mB9qz0yaOTtSnxgNu5FZphqvEZZm5RLo-TKW2bEocOufS-ODUI1OlmiBJ5_Le-bDoM6z62enGBBAgpctyfLINs7j8sCMPf-y_B_o2I14Po9puo3CdkfXvIdZFFQXYN04fFNJe839hOIV6OPIqukWYkKZ6uum43sXiGnjxR57TgDLlyRj3oFT_6Pht7Hf3Dfy-zZg7_Aei3Q_r-Z8EYIyF0odoj3ypaDmSkjZ5I_tHM1RX4aQryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0415430ff6.mp4?token=MA35QO-wzcxqhWLjN9j6SeFi9z9RAAGkutyfVTFqp-rU-12wElnrrMtBvf27DWy4Mey5x201qdrFnLc2R4FIG1aPesDs4ktvQ7u6GcQkYIRVwfOelqRjCEINtgDtd1fm60ekiTkIlfDrfwGMTUE6baWurIhNNXd-9HUZfmrBn9j3HImotDjrubbwkbhcGaXE98q22FAyR4JO7rKLenpdj3p6R5nfgYmTZonrKCFACFt5yB4WzC-VcvrZk1FKyX7-q1J8Ffvsm5NRrUIeS3iz4RzXPs6TIvOhIO8jJ6V1IeP1dR0sN8Z1yAxdrNoZ3w29Pl-jQ9zeot_jieTA8xT9Shyy4A8AMOwz2tjZ0jKvn1rFm1asaBcCr4p43pPcqtMpmOewiV8YRSy3tguzf-Zr45oCtK-c_w8BpgpZ8S7X2nmQK-gxUFl_-io737iKqF5CK5imjYE3RTyHAgXV8mSAttzkV2MZ-bnRpKQt4IRuBiu6PtZsqRw6MGTirxyoi0ccN_6ITDH5TBrlBcS_CjHLrMUw8rthYcvuN6KzxFiwZMb3LzDWX6fiM7ddcLdb_4VBNCEoAY1_nSE9uGxpO5bdc79ou7hZaw-Qb06GCG5EqdS5r4iYccvvSnWRxF1QP4tkA69vX-qlG0PzKkFJ9Aw0krafyhQIV5FG6H2X0V_Otzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0415430ff6.mp4?token=MA35QO-wzcxqhWLjN9j6SeFi9z9RAAGkutyfVTFqp-rU-12wElnrrMtBvf27DWy4Mey5x201qdrFnLc2R4FIG1aPesDs4ktvQ7u6GcQkYIRVwfOelqRjCEINtgDtd1fm60ekiTkIlfDrfwGMTUE6baWurIhNNXd-9HUZfmrBn9j3HImotDjrubbwkbhcGaXE98q22FAyR4JO7rKLenpdj3p6R5nfgYmTZonrKCFACFt5yB4WzC-VcvrZk1FKyX7-q1J8Ffvsm5NRrUIeS3iz4RzXPs6TIvOhIO8jJ6V1IeP1dR0sN8Z1yAxdrNoZ3w29Pl-jQ9zeot_jieTA8xT9Shyy4A8AMOwz2tjZ0jKvn1rFm1asaBcCr4p43pPcqtMpmOewiV8YRSy3tguzf-Zr45oCtK-c_w8BpgpZ8S7X2nmQK-gxUFl_-io737iKqF5CK5imjYE3RTyHAgXV8mSAttzkV2MZ-bnRpKQt4IRuBiu6PtZsqRw6MGTirxyoi0ccN_6ITDH5TBrlBcS_CjHLrMUw8rthYcvuN6KzxFiwZMb3LzDWX6fiM7ddcLdb_4VBNCEoAY1_nSE9uGxpO5bdc79ou7hZaw-Qb06GCG5EqdS5r4iYccvvSnWRxF1QP4tkA69vX-qlG0PzKkFJ9Aw0krafyhQIV5FG6H2X0V_Otzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Gemini Intelligence For Android
شرکت گوگل در کنفرانس I/O 2026، ابزارهای هوش مصنوعی جدیدی را برای خودکارسازی وظایف در دستگاه‌های تلفن همراه معرفی نمود. این قابلیت‌ها شامل موارد زیر می‌باشند:
• خودکارسازی فرآیندهای چندمرحله‌ای (از جمله رزرو سفر و انتقال لیست‌ها از برنامه یادداشت‌برداری به سبد خرید فروشگاه‌ها)
• ارائه خلاصه‌ای از صفحات وب و تکمیل خودکار فرم‌ها در مرورگر کروم
• تبدیل گفتار به متن ساختاریافته در کیبورد Gboard (با استفاده از ابزار Rambler و پشتیبانی از چندین زبان)
• ایجاد ویجت‌های سفارشی دسکتاپ بر اساس ورودی متنی (قابلیت Create My Widget)
اولین دستگاه‌های سازگار با این فناوری، گوشی‌های سامسونگ گلکسی S26 و گوگل پیکسل 10 می‌باشند که در فصل تابستان عرضه خواهند شد. تا پایان سال جاری، این قابلیت‌ها به ساعت‌های هوشمند، رایانه‌های شخصی، هدست‌ها و سیستم‌های رسانه‌ای خودرو نیز گسترش خواهند یافت.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/5007" target="_blank">📅 09:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZoEu4sdAqeLae1530Wegn-MsnhtUA10TI-IxNYhoNnCvOO9S3rnvmxRtaP-KtfpmrvglpSFxQO2GAfnOnuVJ5nNvZ7NpVyxdTInRQVrXjpPFlIRU0m20c5aWXOAo4hgtkgeArcEsSD-vEVmgDV8gOySClCdzoV4xwqfrK26FMoTaaE3d_t10AT_9htGRTkwl6f-l9s70wLNCMA4zpXlcGqCWdQcobdFS517cw4MnqCOKn699FU0_qUIvc5RWkWxwyOhFmzAO55d289QNKjxbwM3zxB3RLVbg3OfE-itEZd0-1ZHNhJnRXNp3mRk4iEH7LOu-eDNWuA74YVwui-C5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhatModels
ماشین حساب آنلاین برای انتخاب مدل‌های هوش مصنوعی متناسب با سخت‌افزار شما
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5006" target="_blank">📅 08:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">لینک داخلی شیر و خورشید ، دو تا آپلودسنتر
دانلود
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/archivetell/5005" target="_blank">📅 03:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سامانتل راحت وصله..</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/archivetell/5004" target="_blank">📅 03:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سامانتل  این کد رو داخل ترموکس بزنید هر چی پیدا کرد کپی کنید داخل شیر و خورشید 100% وصله: for i in $(seq 1 254); do     ping -c 1 -W 1 185.200.232.$i >/dev/null && echo "185.200.232.$i" done</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5003" target="_blank">📅 02:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ArchiveTel
pinned «
سامانتل  این کد رو داخل ترموکس بزنید هر چی پیدا کرد کپی کنید داخل شیر و خورشید 100% وصله: for i in $(seq 1 254); do     ping -c 1 -W 1 185.200.232.$i >/dev/null && echo "185.200.232.$i" done
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5000" target="_blank">📅 02:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">همراه اول شیر و خورشید
184.24.77.42 184.24.77.32 184.24.77.5 184.24.77.7 184.24.77.16 184.24.77.36 184.24.77.21 184.24.77.11 185.200.232.49 185.200.232.50 185.200.232.42 185.200.232.41 23.48.23.186 23.48.23.133 23.48.23.195 23.48.23.178 184.24.77.29 104.78.170.186 96.17.222.31 23.41.37.129 23.2.13.227 23.222.126.108 2.20.255.113 2.17.251.98 23.2.13.152 95.101.23.27 2.21.239.21 23.211.49.252 88.221.168.5 104.103.90.156 23.79.20.249 88.221.132.162 23.59.235.208 23.60.69.118 23.46.188.71 104.122.212.92 23.219.1.4 23.57.43.195 184.51.252.135 2.22.6.68 23.217.11.56 95.100.69.108 23.40.63.69 185.200.232.49 185.200.232.50 185.200.232.42 185.200.232.41 184.24.77.42 184.24.77.32 184.24.77.5 184.24.77.7 184.24.77.16 184.24.77.36 184.24.77.21 184.24.77.11 23.48.23.186 23.48.23.133 23.48.23.195 23.48.23.178 184.24.77.29 96.16.122.74 104.109.250.232 92.123.104.7 104.110.191.57 104.83.5.82 92.122.166.168 104.83.5.65 104.121.0.17 104.66.70.133 92.122.166.146 23.73.2.161 92.122.73.138 92.122.166.141 96.16.122.55 104.81.108.51 23.72.248.214 104.126.37.185 104.83.5.201 104.83.5.216 92.123.104.67 104.83.5.203 96.17.207.151 88.221.168.138 96.17.207.149 104.81.108.10 23.73.2.148 92.122.166.175 172.237.127.6 104.81.104.13 96.17.207.137 92.123.112.7 96.16.122.75 96.16.122.70 92.122.166.182 104.109.128.153 104.96.143.134 23.73.2.141 104.83.5.202 23.67.136.200 23.67.136.202 23.65.119.52 92.122.166.236 92.122.166.234 92.122.166.237 104.110.138.190 173.222.200.5 184.51.252.36 184.51.252.38 104.83.5.208 96.16.122.146 96.17.206.214 92.122.166.197 104.94.100.73 104.83.15.66 88.221.213.81 172.239.57.117 104.117.76.40 184.51.252.4 96.17.207.30 96.16.122.83 96.16.122.150 23.73.207.11 96.16.122.77 96.17.207.155 92.123.189.82 96.16.122.82 96.16.122.66 96.7.218.219 96.16.122.137 184.51.252.157 92.123.189.41 184.86.251.12 96.16.122.154 184.51.252.152 96.17.207.12 23.79.48.162 151.101.0.223 151.101.128.223 151.101.192.223 65.109.34.234 151.101.64.223 142.54.178.211 104.103.90.156 23.79.20.249 88.221.132.162 23.59.235.208 23.60.69.118 23.46.188.71 104.122.212.92 23.219.1.4 23.57.43.195 184.51.252.135 2.22.6.68 23.217.11.56 95.100.69.108 23.40.63.69 2.23.168.47 2.23.170.80 2.23.168.144 2.23.168.213 2.23.168.174 2.23.169.111 2.23.168.96 185.200.232.49 185.200.232.41 2.23.169.105 2.23.168.7 2.23.169.207 185.200.232.50 185.200.232.42
﻿</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/4999" target="_blank">📅 01:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سامانتل
این کد رو داخل ترموکس بزنید هر چی پیدا کرد کپی کنید داخل شیر و خورشید 100% وصله:
for i in $(seq 1 254); do
ping -c 1 -W 1 185.200.232.$i >/dev/null && echo "185.200.232.$i"
done</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/4998" target="_blank">📅 01:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">for i in $(seq 1 254); do
ping -c 1 -W 1 x.x.x.$i >/dev/null && echo "x.x.x.$i"
done
بزنید ترموکس رنج بدین ببینید چی میده ایرانسل (جای x ایپی بذارید)
رنج پست های قبل گذاشتم</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4997" target="_blank">📅 01:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آیپی های بالا با سامانتل راحت وصله</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4996" target="_blank">📅 23:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
ترفند: تست پینگ گروهی آی‌پی‌ها در ترموکس (سریع و ساده)
---
رفقا سلام!
✋
اگه یه لیست بلندبالا از آی‌پی (مثلاً آی‌پی‌های تمیز کلودفلر) دارید و می‌خواید تو گوشی و محیط ترموکس (Termux) خیلی سریع تستشون کنید که کدومشون زنده‌ست (UP) و کدوم مرده (DOWN)، این اسکریپت ساده خوراکِ خودتونه.
🛠
مراحل کار قدم‌به‌قدم:
۱. ساخت فایل آی‌پی‌ها:
اول دستور زیر رو تو ترموکس بزنید:
cat > ips.txt
حالا لیست آی‌پی‌هاتون رو پیست کنید، یه اینتر بزنید و در نهایت کلیدهای Ctrl + D رو فشار بدید تا فایل ذخیره بشه.
۲. ساخت فایل اسکریپت:
دستور زیر رو بزنید تا یه فایل جدید باز بشه:
nano ping_script.sh
حالا کدهای زیر رو کپی و همونجا پیست کنید:
#!/bin/bash
while read -r ip; do
if ping -c 1 -W 1 "$ip" > /dev/null; then
echo "$ip is UP
🟢
"
else
echo "$ip is DOWN
🔴
"
fi
done < ips.txt
(برای ذخیره کردن فایل تو نانو: کلیدهای Ctrl + O رو بزنید، بعد Enter، و در آخر Ctrl + X برای خروج).
۳. اجرای اسکریپت:
حالا با این دو دستور، به اسکریپت دسترسی اجرا بدید و استارتش کنید:
chmod +x ping_script.sh
./ping_script.sh
تمام! اسکریپت شروع می‌کنه دونه‌دونه آی‌پی‌ها رو تست می‌کنه و وضعیتشون رو خیلی تمیز بهتون نمایش می‌ده.
📌
#آموزش
#ترموکس
#پینگ
#آی_پی
#شبکه
#Termux
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/4995" target="_blank">📅 23:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رایتل و سامانتل شیر و خورشید
185.200.232.43
185.200.232.40
167.82.48.223
151.101.128.223
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/4994" target="_blank">📅 23:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رایتل و سامانتل شیر و خورشید
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
185.200.232.43
185.200.232.40
167.82.48.223
151.101.128.223
185.200.232.49
185.200.232.50
185.200.232.42</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/4993" target="_blank">📅 22:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">githubProject.html</div>
  <div class="tg-doc-extra">52.1 KB</div>
</div>
<a href="https://t.me/archivetell/4991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مدیریت پروژه GitHub
در ترمینال VSCode
در این آموزش با تمام دستورات ضروری Git برای بروزرسانی، حذف، ادغام، و مدیریت کامل پروژه‌هایتان در GitHub آشنا می‌شوید — مستقیم از ترمینال VSCode.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/archivetell/4991" target="_blank">📅 22:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آیپی تمیز شیر و خورشید همراه اول
23.54.210.170
23.44.201.206
23.220.163.205
23.209.46.33
23.10.34.11
23.39.185.35
23.32.152.106
23.218.232.181
23.206.188.212
2.21.2.89
23.208.222.120
23.48.203.248
23.44.201.136
23.44.201.151
23.44.201.149
2.21.2.58
23.3.90.48
23.44.201.41
2.19.204.184
23.218.232.188
23.44.201.12
23.212.253.227
23.201.31.155
23.220.163.203
23.44.201.185
23.52.116.66
23.44.201.17
23.62.54.24
23.218.239.132
23.39.149.69
23.52.40.147
23.58.95.144
2.16.244.58
23.212.253.137
2.17.106.176
23.62.54.137
2.17.106.5
23.203.134.233
23.212.253.232
23.206.188.197
23.44.201.170
23.54.127.39
23.214.170.83
23.52.40.89
23.55.176.73
23.202.229.140
23.215.56.61
2.17.106.166
23.222.126.108
184.25.85.224
23.1.241.123
23.3.90.43</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/archivetell/4989" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ip by dark.txt</div>
  <div class="tg-doc-extra">6.3 KB</div>
</div>
<a href="https://t.me/archivetell/4988" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">500 تا آیپی اسکن شده توسط یکی از ممبرای عزیز برای شیر خورشید
همه نتا</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/4988" target="_blank">📅 19:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خودتون آیپی اسکن کنید با این روش ها..</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/4987" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel(𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣⚡️)</strong></div>
<div class="tg-text">اسکنر برای آی پی تمیز https://github.com/seramo/sni-scanner</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/archivetell/4986" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">اسکنر برای آی پی تمیز
https://github.com/seramo/sni-scanner</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/archivetell/4985" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4984">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">hosts.txt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/archivetell/4984" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینا هم اسکن کنید..</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/archivetell/4984" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai-AS20940.json</div>
  <div class="tg-doc-extra">97.1 KB</div>
</div>
<a href="https://t.me/archivetell/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رنج آیپی akamai واسه اسکن</div>
<div class="tg-footer">👁️ 488 · <a href="https://t.me/archivetell/4982" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ping.py</div>
  <div class="tg-doc-extra">17.6 KB</div>
</div>
<a href="https://t.me/archivetell/4981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر TCP رنج ایپی های Akamai
فایل hosts.txt رو کنارش بذارید و روی هر سیستم عاملی با پایتون اجراش کنید (ورودی ایپی تکی و ایپی رنج ساپورت میکنه)
- قابلیت تشخیص NAT از اتصال واقعی بر اساس پینگ
- سرعت ورکر رو میشه تنظیم کرد
- قابلیت بهینه سازی تایم اسکن
- خروجی رو توی فایل vali.txt میده.
بدون پیش نیاز...</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/archivetell/4981" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sni-radar.zip</div>
  <div class="tg-doc-extra">303.4 KB</div>
</div>
<a href="https://t.me/archivetell/4980" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
سورس اسکنر اختصاصی تیم پرشیا
❤️
🟢
این
سورس اسکنر sni و Cdn هست و با بهترین قابلیت ها نوشته شده است
☑️
💡
اموزش نصب در کامپیوتر:
🔹
اول فایل را دانلود کرده سپس استخراج کنید
🔹
سپس رو محل فایل کلیک کرده ترمینال را باز کرده و در ان این دستور را بنویسید:
pip install -r requirements.txt
🔹
سپس این دستور را بنویسید:
python sni_web.py
🔹
بعدش صفحه باز میشه و میتونید اسکن را شروع کنید
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
⏺️
اموزش نصب در گوشی با برنامه termux
🔹
اول وارد برنامه ترموکس شده و پکیچ های پایتون نصب کنید
🔹
سپس دستور زیر را وارد کنید
git clone https://github.com/DevMoEiN/SNI-Radar.git
🔹
سپس این دستور:
cd SNI-Radar
🟢
بعد این:
pip install flask
🔹
و در اخر این:
python sni_web.py
⏺️
سپس این را در کروم تایپ کنید:
http://127.0.0.1:10808</div>
<div class="tg-footer">👁️ 764 · <a href="https://t.me/archivetell/4980" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">📌
نحوه اسکن آیپی‌‌های Akamai در ترموکس :
1⃣
به یک فیلترشکن متصل بشید و ​ترموکس را باز کنید و این ۳ خط را کپی کنید و اینتر بزنید تا ابزارهای لازم نصب بشن :
pkg update && pkg upgrade -y
pkg install nmap -y
termux-setup-storage
اگر پیغامی برای دسترسی به فایل‌ها اومد، Allow را بزنید.
2⃣
​
حالا فیلترشکن رو خاموش کنید و دستور زیر رو بزنید
:
nmap -p 443 --open -T4 2.16.0.0/1
8
‼️
من در دستور از رنج آیپی
2.16.0.0/18
استفاده کردم و 4 آیپی وایتی که اسکن کرد رو براتون گذاشتم، شما میتونید اون رنج‌ رو پاک کنید و از این مخزن گیت‌هاب، سایر رنج‌ها رو در دستور جایگذاری کنید :
https://github.com/platformbuilds/Akamai-ASN-and-IPs-List
بعد از پایان اسکن، ​هر جا نوشته بود Nmap scan report for و زیرش نوشته بود 443/tcp open یعنی اون آیپی‌ وایته و باید کپیش کنید
.
بهتره رنج‌های کوچک رو اسکن کنید، اسکن رنج‌آیپی‌های بزرگ، ساعت‌ها زمان میبره</div>
<div class="tg-footer">👁️ 661 · <a href="https://t.me/archivetell/4979" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">جهت اسکن آیپی های fastly یا akami یا هر آیپی / رنجی که میخواین میتونید از ریپوی زیر استفاده کنید
https://github.com/penhandev/IP-Scanner</div>
<div class="tg-footer">👁️ 643 · <a href="https://t.me/archivetell/4978" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ip_scanner_gui.exe</div>
  <div class="tg-doc-extra">9.6 MB</div>
</div>
<a href="https://t.me/archivetell/4977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر آیپی
قابلیت هاش:
1. چک کردن ایپی معمولی
2. چک کردن رنج ایپی Fastly و Akamai
3. بصورت دستی اضافه کردن ایپی یا رنج
4. بصورت فایل اضافه کردن .txt  و .json
5. ماکسیموم پینگ گذاشتن واسش مثلا زیر 180ms
6. ایپی های که داخل چنلا میزارن بندازید توش اسکن کنه
منبع : پای پکیج</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/archivetell/4977" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Akamai-IP-Scanner.zip</div>
  <div class="tg-doc-extra">1.8 KB</div>
</div>
<a href="https://t.me/archivetell/4976" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">برنامه Akamai IP Scanner
۱. لیست رنج‌های هدف (با پشتیبانی از تمام فرمت‌ها مثل 16/ یا 24/) را در فایل ips.txt قرار دهید. (پیشفرض قرار داده شده)
۲. روی فایل scan.ps1 راست‌کلیک کرده و گزینه Run with PowerShell را برای شروع اسکن انتخاب کنید.
۳. بهترین آی‌پی‌ها به‌صورت لحظه‌ای در clean_ips.txt ذخیره می‌شوند (هر زمان مایل بودید می‌توانید اسکن را متوقف کنید).</div>
<div class="tg-footer">👁️ 637 · <a href="https://t.me/archivetell/4976" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آپلودسنتر
https://files.bokhary.fun/dump/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/4974" target="_blank">📅 17:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">لینک داخلی شیر و خورشید ، دو تا آپلودسنتر
دانلود
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/archivetell/4973" target="_blank">📅 17:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Telegram.apk</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/4969" target="_blank">📅 16:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آیپی تمیز شیر و خورشید
2.21.134.89
2.19.204.217
96.16.122.149
172.237.127.6
96.16.53.158
23.55.163.135
2.19.205.64
23.73.2.148
2.17.147.11
2.19.204.240
184.51.252.36</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/4968" target="_blank">📅 16:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ایرانسل تست شده شیر و خورشید
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
2.22.21.152
95.101.23.82
23.215.0.164
23.197.161.35
184.28.230.87
23.220.128.221
96.17.207.142
23.50.131.18
23.36.162.209
23.219.3.212
23.223.245.150
96.16.122.59
23.2.13.138
23.2.13.144
96.17.207.135
23.220.113.51
96.17.72.41
23.203.185.105
95.101.35.83
2.21.239.23
23.54.210.170
23.215.60.73
95.101.181.125
23.192.237.222
23.200.143.71
23.58.222.98
125.56.219.8
104.80.49.118
96.16.122.158
2.21.239.10
96.16.122.65
95.101.23.170
104.111.202.158
23.2.13.201
92.123.102.104
23.58.222.139
2.17.147.89
96.17.178.132
23.49.248.6
23.222.30.64
23.55.110.70
23.2.13.153
173.222.105.65
23.200.143.73
23.201.217.14
23.55.110.200
95.101.23.25
23.37.206.186
173.222.105.42
95.101.29.12
88.221.92.177
23.50.131.132
184.86.251.27
2.16.244.11
2.16.27.71
2.19.10.30
104.121.12.86
23.73.207.16
2.18.190.26
96.16.122.149
23.201.217.150
95.101.23.168
96.17.207.162
96.16.122.48
95.101.35.73
23.192.237.208
80.67.82.179
96.17.207.154
2.21.89.66
2.18.190.27
95.100.156.147
23.192.46.51
104.76.220.137
23.36.162.198
23.37.197.128
96.17.207.143
23.36.162.208
23.36.162.202
23.200.143.88
23.55.110.46
23.55.110.143
173.222.105.18
2.23.176.166
23.44.10.10
104.126.37.171
23.55.155.169
23.210.123.174
104.117.76.26
23.46.188.168
23.58.222.147
95.101.200.63
125.56.219.32
23.192.237.209
95.101.29.54
23.46.230.118
96.17.207.153
184.25.52.200
23.202.156.203
23.36.162.196
96.16.122.145
23.33.126.163
95.101.29.30
23.36.162.215
23.39.249.249
2.21.239.29
23.210.73.136
104.126.37.161
23.2.13.186
23.50.131.160
23.219.138.200
96.16.122.153
104.117.76.146
23.38.49.97
2.19.196.105
96.16.122.141
104.78.170.186
96.17.222.31
23.41.37.129
23.2.13.227
23.222.126.108
2.20.255.113
2.17.251.98
23.2.13.152
95.101.23.27
2.21.239.21
23.211.49.252
88.221.168.5
104.103.90.156
23.79.20.249
88.221.132.162
23.59.235.208
23.60.69.118
23.46.188.71
104.122.212.92
23.219.1.4
23.57.43.195
184.51.252.135
2.22.6.68
23.217.11.56
95.100.69.108
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
23.40.63.69</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4967" target="_blank">📅 16:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTelegram APKs for Android</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">77.9 MB</div>
</div>
<a href="https://t.me/archivetell/4966" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">12.7.3 (6750)
Directly downloadable from
telegram.org/android</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/4966" target="_blank">📅 16:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRIT9uJpGDcGV4bYzhP-9W2eVyxO9hB_QwAaY_nf3QidjHPH8QFz6LNQFjdYMM3pbQ-IFSYF7do_py3yScjlME5nFmqSjcPESWavG3edlGnyyR7r2q9PnQ7x-s1t5eWjrCqRLgEnfplEOPSqVBAeb34FPOddA8fxWSIMb5funCrW0cEfnGyNrBgRB2VozXfJV3799HkYwXb_4Sr23hh104a5pUsBYgkiv7GIVxcDUaok8IDE8Gf8XjvF5wGXJu1c1xwGin4rzG-cFNHqKSPvcDRhvt2kPY-lb3G5L1feK8TrdtLAAlohFUEOMljoC1tIaO_8kVYR6ML5Of8AJBGxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساده ترین تلاش های یک ایرانی برای اتصال به نت بین المللی:</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/4965" target="_blank">📅 15:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شیرخورشید   CDN Edge IPs: 151.101.192.223 CDN SNI Hostname: python.org‎</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/4964" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شیرخورشید
CDN Edge IPs:
151.101.192.223
CDN SNI Hostname:
python.org
‎</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/4963" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسکنر برای آی پی تمیز https://github.com/seramo/sni-scanner</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/archivetell/4961" target="_blank">📅 15:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اسکنر برای آی پی تمیز
https://github.com/seramo/sni-scanner</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/4960" target="_blank">📅 14:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آپدیت ویندوز: من ادامه میدم تا وقتی نت هست اتشفشانو نمیشه با برف بست</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4959" target="_blank">📅 14:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دستیار هوش مصنوعی تولید محتوا:
@Scriblastbot
- مقالات و پست‌های وبلاگی اصیل می‌نویسد.
- محتوا را برای هر پلتفرمی بازاستفاده می‌کند.
- متن‌های جذاب برای شبکه‌های اجتماعی می‌سازد.
- سئو را بهینه می‌کند و لحن/سبک‌های متنوعی را تنظیم می‌نماید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4958" target="_blank">📅 14:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Windows.Update.Blocker.1.8.rar</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/4957" target="_blank">📅 14:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Windows.Update.Blocker.1.8.rar</div>
  <div class="tg-doc-extra">988.5 KB</div>
</div>
<a href="https://t.me/archivetell/4956" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">غیرفعال کردن اپدیت خودکار ویندوز 10 و 11
(تست کردم خودم)
با یه کلیک ساده اپدیت خودکار رو خاموش کنید و وقتی نیاز داشتی فعال کن .
منبع سافت 98
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4956" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آقا واسه شیر کردن فیلترشکن با PdaNet رو کابل USB که از همه پایدارتره اینجوری پیش برین: ۱. اول فیلترشکن گوشیو روشن کنین. ۲. گوشیو با کابل وصل کنین به کامپیوتر. ۳. تو برنامه PdaNet گوشی، تیک USB Tether رو بزنین. (اگه پیام USB Debugging داد، always allow رو تیک…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/4955" target="_blank">📅 14:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PdaNet+ v5.32 (Premium).apk</div>
  <div class="tg-doc-extra">1.7 MB</div>
</div>
<a href="https://t.me/archivetell/4954" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">PdaNet+ v5.32 (Premium).apk
@archivetell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/4954" target="_blank">📅 14:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شاید واستون سوال باشه که چرا پترنیها اینقدر تلاش میکنه واسه پیدا کردن این متد ها  چون حکومت نتونه وایت لیست  رو به راحتی اجرا کنه و فشار زیادی وارد بشه روی فیلترینگ</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/archivetell/4952" target="_blank">📅 13:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تازه اسکن شده سرعت فضایی
💥
:
شیر و خورشید؛
84.26.13.91
23.54.210.170
23.44.201.206
23.220.163.205
23.209.46.33
23.10.34.11
23.39.185.35
23.32.152.106
23.218.232.181
23.206.188.212
2.21.2.89
23.208.222.120
23.48.203.248
23.44.201.136
23.44.201.151
23.44.201.149
2.21.2.58
23.3.90.48
23.44.201.41
2.19.204.184
23.218.232.188
23.44.201.12
23.212.253.227
23.201.31.155
23.220.163.203
23.44.201.185
23.52.116.66
23.44.201.17
23.62.54.24
23.218.239.132
23.39.149.69
23.52.40.147
23.58.95.144
2.16.244.58
23.212.253.137
2.17.106.176
23.62.54.137
2.17.106.5
23.203.134.233
23.212.253.232
23.206.188.197
23.44.201.170
23.54.127.39
23.214.170.83
23.52.40.89
23.55.176.73
23.202.229.140
23.215.56.61
2.17.106.166
23.222.126.108
184.25.85.224
23.1.241.123
23.3.90.43
بزنید عشق کنید ری اکشن هم یادتون نره
❤️</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4951" target="_blank">📅 13:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شاید واستون سوال باشه که چرا پترنیها اینقدر تلاش میکنه واسه پیدا کردن این متد ها
چون حکومت نتونه وایت لیست  رو به راحتی اجرا کنه و فشار زیادی وارد بشه روی فیلترینگ</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/4950" target="_blank">📅 13:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POmbQd-V-QZD9fZVUwHX-vHkVszycHdk_Lqnj8G-l-zhimYBEXf1aaPAmHPIfVYZUvMwo--yuvZR5kTFRjuLH01gnolGiIAzT55vjaAB41nSnfvueXbMSmoveQimgwpde1KJkfRYb5Z7GmyNz6dCuAXB-PzeAajRLUJvvmEG32Iffdy70cb3P08S1BW7hFeSWqPXScqvRxwYyzk5opaT69lc1N7xy5LTIWMO3MQZxhm3hurOrzjv0xWQqu8DM2K9xwJ5mShdldiqXV3vvuhPhUmFi16H02O7yquexkO8STMFkGgrOlLOMVAni0TrkPn0zy2X3TJxfL9O-VHiLgnAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت.
حالا بیا جلو اینم بگیر
😎
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/archivetell/4949" target="_blank">📅 11:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتلیفای بای بای
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/4948" target="_blank">📅 11:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">hosts.txt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/archivetell/4947" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینا هم اسکن کنید..</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/archivetell/4947" target="_blank">📅 10:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai-AS20940.json</div>
  <div class="tg-doc-extra">97.1 KB</div>
</div>
<a href="https://t.me/archivetell/4945" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رنج آیپی akamai واسه اسکن</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/archivetell/4945" target="_blank">📅 10:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ping.py</div>
  <div class="tg-doc-extra">17.6 KB</div>
</div>
<a href="https://t.me/archivetell/4944" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر TCP رنج ایپی های Akamai
فایل hosts.txt رو کنارش بذارید و روی هر سیستم عاملی با پایتون اجراش کنید (ورودی ایپی تکی و ایپی رنج ساپورت میکنه)
- قابلیت تشخیص NAT از اتصال واقعی بر اساس پینگ
- سرعت ورکر رو میشه تنظیم کرد
- قابلیت بهینه سازی تایم اسکن
- خروجی رو توی فایل vali.txt میده.
بدون پیش نیاز...</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/archivetell/4944" target="_blank">📅 10:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ایرانسل ، همراه اول و رایتل   شیر و خورشید تست کنید   185.200.232.40 185.200.232.43</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/4943" target="_blank">📅 10:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شیر و خورشید
151.101.0.223
151.101.128.223
151.101.192.223
65.109.34.234
151.101.64.223
142.54.178.211
2.16.53.50
2.16.53.11
95.101.133.82
95.101.133.42
104.103.65.50
2.23.168.47
104.103.64.7
2.23.168.254
2.23.168.144
2.23.169.249
2.23.169.42
2.23.170.80
104.103.65.5
95.101.133.131
104.103.65.74
2.16.20.51
23.221.28.57
23.221.29.29
23.221.28.5
2.23.169.111
2.23.168.96
2.23.169.12
2.23.168.174
2.23.168.7
184.84.221.34
2.23.41.22
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/4942" target="_blank">📅 10:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sni-radar.zip</div>
  <div class="tg-doc-extra">303.4 KB</div>
</div>
<a href="https://t.me/archivetell/4941" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
سورس اسکنر اختصاصی تیم پرشیا
❤️
🟢
این
سورس اسکنر sni و Cdn هست و با بهترین قابلیت ها نوشته شده است
☑️
💡
اموزش نصب در کامپیوتر:
🔹
اول فایل را دانلود کرده سپس استخراج کنید
🔹
سپس رو محل فایل کلیک کرده ترمینال را باز کرده و در ان این دستور را بنویسید:
pip install -r requirements.txt
🔹
سپس این دستور را بنویسید:
python sni_web.py
🔹
بعدش صفحه باز میشه و میتونید اسکن را شروع کنید
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
⏺️
اموزش نصب در گوشی با برنامه termux
🔹
اول وارد برنامه ترموکس شده و پکیچ های پایتون نصب کنید
🔹
سپس دستور زیر را وارد کنید
git clone https://github.com/DevMoEiN/SNI-Radar.git
🔹
سپس این دستور:
cd SNI-Radar
🟢
بعد این:
pip install flask
🔹
و در اخر این:
python sni_web.py
⏺️
سپس این را در کروم تایپ کنید:
http://127.0.0.1:10808</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/archivetell/4941" target="_blank">📅 09:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ایرانسل ، همراه اول و رایتل   شیر و خورشید تست کنید   185.200.232.40 185.200.232.43</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/4940" target="_blank">📅 09:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شیر و خورشید همه نتا
185.200.232.8
185.200.232.9
185.200.232.11
185.200.232.16
185.200.232.17
185.200.232.19
185.200.232.24
185.200.232.25
185.200.232.26
185.200.232.34
185.200.232.40
185.200.232.42
185.200.232.43
185.200.232.49
185.200.232.56
185.200.232.57
185.200.232.58
185.200.232.64
185.200.232.65
185.200.232.66
185.200.232.67</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/4939" target="_blank">📅 09:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سامانتل شیر و خورشید
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/4938" target="_blank">📅 09:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سایت های وایت لیست شده رو بستن تا بتونن جلوی این متد رو بگیرن..</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/4937" target="_blank">📅 09:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ایرانسل ، همراه اول و رایتل
شیر و خورشید تست کنید
185.200.232.40
185.200.232.43</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/4936" target="_blank">📅 09:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-text">🔥
متصل
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR%20NETLIFY%20SUB</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/4935" target="_blank">📅 04:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=Wi7y_Q42Tr8wdUXx-uc6CeFZ9emYGarAJS1qdsA47ljcgw2UXVT6NvKox5Bc75z24KvrMEl5CI7F11byBBBpG1TCMNvIM69FwnpuLvuoDiRgI96272oy9fpqb1owajYYWaSc5D7PqTE90p6JX4YQW0GkXr6F3OP9W2x8wJzjGqRFBQHNIhTe-91uV718pVdTw_P4n3srQJQNIrYxf526BtB_HlyB5HPVuAMy5MhFHb7TxWc5DOlZrbIseYSIJpZTcP_Li2g7PHDKoVWv6BqNDxaPr0ZGPqJ4GD6Ek6K4OTfxFgPB5y8GD8Hik7bsfSoOk3PFSAgm2I4AQHptgGLEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=Wi7y_Q42Tr8wdUXx-uc6CeFZ9emYGarAJS1qdsA47ljcgw2UXVT6NvKox5Bc75z24KvrMEl5CI7F11byBBBpG1TCMNvIM69FwnpuLvuoDiRgI96272oy9fpqb1owajYYWaSc5D7PqTE90p6JX4YQW0GkXr6F3OP9W2x8wJzjGqRFBQHNIhTe-91uV718pVdTw_P4n3srQJQNIrYxf526BtB_HlyB5HPVuAMy5MhFHb7TxWc5DOlZrbIseYSIJpZTcP_Li2g7PHDKoVWv6BqNDxaPr0ZGPqJ4GD6Ek6K4OTfxFgPB5y8GD8Hik7bsfSoOk3PFSAgm2I4AQHptgGLEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/4933" target="_blank">📅 03:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">CDN Edge IPs:
151.101.0.223
151.101.128.223
151.101.192.223
65.109.34.234
151.101.64.223
142.54.178.211
2.16.53.50
2.16.53.11
95.101.133.82
95.101.133.42
104.103.65.50
2.23.168.47
104.103.64.7
2.23.168.254
2.23.168.144
2.23.169.249
2.23.169.42
2.23.170.80
104.103.65.5
95.101.133.131
104.103.65.74
2.16.20.51
23.221.28.57
23.221.29.29
23.221.28.5
2.23.169.111
2.23.168.96
2.23.169.12
2.23.168.174
2.23.168.7
184.84.221.34
2.23.41.22
CDN SNI Hostname:
python.org</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/archivetell/4931" target="_blank">📅 01:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭐
184.50.87.44
🫥
SNI Hostname:
python.org</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/4930" target="_blank">📅 01:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting-16.zip</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/archivetell/4929" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ مستقیم MitM-DomainFronting-v16: https://github.com/patterniha/MITM-DomainFronting/releases/tag/v16  تغییرات: باز کردن موقت سایت github</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/4929" target="_blank">📅 01:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">CDN SNI Hostname:
pypi.org
Ip :
151.101.64.223
CDN SNI Hostname:
a.optnmstr.com
Ip :
84.17.46.53
CDN SNI Hostname:
docs.mapbox.com
Ip :
13.227.192.92</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/4928" target="_blank">📅 01:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانفیگ مستقیم MitM-DomainFronting-v16:
https://github.com/patterniha/MITM-DomainFronting/releases/tag/v16
تغییرات:
باز کردن موقت سایت github</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/4927" target="_blank">📅 01:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📌
نحوه اسکن آیپی‌‌های Akamai در ترموکس :
1⃣
به یک فیلترشکن متصل بشید و ​ترموکس را باز کنید و این ۳ خط را کپی کنید و اینتر بزنید تا ابزارهای لازم نصب بشن :
pkg update && pkg upgrade -y
pkg install nmap -y
termux-setup-storage
اگر پیغامی برای دسترسی به فایل‌ها اومد، Allow را بزنید.
2⃣
​
حالا فیلترشکن رو خاموش کنید و دستور زیر رو بزنید
:
nmap -p 443 --open -T4 2.16.0.0/1
8
‼️
من در دستور از رنج آیپی
2.16.0.0/18
استفاده کردم و 4 آیپی وایتی که اسکن کرد رو براتون گذاشتم، شما میتونید اون رنج‌ رو پاک کنید و از این مخزن گیت‌هاب، سایر رنج‌ها رو در دستور جایگذاری کنید :
https://github.com/platformbuilds/Akamai-ASN-and-IPs-List
بعد از پایان اسکن، ​هر جا نوشته بود Nmap scan report for و زیرش نوشته بود 443/tcp open یعنی اون آیپی‌ وایته و باید کپیش کنید
.
بهتره رنج‌های کوچک رو اسکن کنید، اسکن رنج‌آیپی‌های بزرگ، ساعت‌ها زمان میبره</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/4926" target="_blank">📅 01:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌐
184.26.163.51
CDN SNI Hostname:
python.org</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/4925" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">CDN Edge IPs:
167.82.48.223
CDN SNI Hostname:
files.pythonhosted.org</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/4924" target="_blank">📅 00:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">CDN Edge IPs:
151.101.64.223
CDN SNI Hostname:
pypi.org</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4923" target="_blank">📅 00:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">CDN edge IPs :
151.101.128.223
CDN SNI Hostname :
python.org</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/4922" target="_blank">📅 00:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">CDN edge IPs :
151.101.0.223
CDN SNI Hostname :
www.python.org</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/4921" target="_blank">📅 00:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تست شده شیر و خورشید   CDN Edge IPs: 151.101.192.223  CDN SNI Hostname: python.org</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/4920" target="_blank">📅 00:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">از این کانفیگ هایی که وقتی کلودفلر بازه کار میکنه بدید کامنت</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/4919" target="_blank">📅 00:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">می‌دونستید جعبه سیاه هواپیما اصلاً سیاه نیست؟
✈️
🟧
آره، در واقع یه نارنجیِ جیغ و زننده‌ست. این‌طوری رنگش کردن که وقتی هواپیما سقوط کرد، همه‌چیز سوخت و به خاکستر تبدیل شد، بتونن از بین اون‌همه سیاهی و ویرانی پیداش کنن تا بفهمن دقیقاً کدوم فاجعه و کدوم نقص باعث این سقوط شده. جعبه سیاه، راویِ صادقِ فاجعه‌ست.
اما حالا یه فکت دارک‌تر: می‌دونستید «سیم‌کارت سفید» در اصل قرمزه؟
🩸
📱
همین الان که نت کل کشور قطع شده و ما رو تو یه سیاه‌چال دیجیتال حبس کردن، یه عده از «ما بهتران» دارن با همین سیم‌کارت‌های به‌اصطلاح «سفید» تو اینترنت جهانی می‌چرخن و احتمالاً الان دارن چک می‌کنن ببینن سهامشون تو بورس نیویورک چقدر بالا پایین شده.
ولی چرا می‌گم قرمزه؟
چون این سفیدی فقط یه روکشه. این سیم‌کارت تو بی‌عدالتی و خفقان خیس خورده. رنگش قرمزه، به رنگ حقِ بدیهیِ ۸۰ میلیون آدم که سر بریده شده تا تو جیب یه اقلیت خاص جا بشه. به رنگ خط قرمزی که روی صدای یه ملت کشیدن.
تفاوتشون اینجاست:
جعبه «سیاه» که نارنجیه، بعد از سقوط به داد آدم می‌رسه تا حقیقت رو بگه.
اما سیم‌کارت «سفید» که قرمزه، خودش همون موتوریه که داره مارو به سمت سقوط می‌بره و حقیقت رو خفه می‌کنه.
خلاصه که گول اسم‌ها رو نخورید... تو سیستمی که سیاهی‌هاش نارنجیه، سفیدی‌هاش قطعاً بوی خون، تبعیض و قطعیِ نت میده.
#سیم_کارت_پرو
#قطعی_اینترنت
#تبعیض
#اینترنت_طبقاتی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/4918" target="_blank">📅 00:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تست شده شیر و خورشید
CDN Edge IPs:
151.101.192.223
CDN SNI Hostname:
python.org</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4917" target="_blank">📅 23:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
معرفی ابزار Pantegnos: رمزگشایی و استخراج کانفیگ‌های قفل‌شده!
---
رفقا سلام!
✋
خیلی وقتا پیش میاد که تو یه اپلیکیشن VPN خاص (مثل Netmod یا Slipnet) یه کانفیگ فوق‌العاده و پرسرعت پیدا می‌کنید، اما کانفیگ قفل و رمزنگاری شده و فرمت‌های عجیبی (مثل //:slipnet-enc یا //:nm-vless) داره. در نتیجه نمی‌تونید اطلاعات اصلی سرور (آی‌پی، پورت، SNI و...) رو بکشید بیرون تا تو برنامه‌های استاندارد خودتون مثل V2rayNG یا NekoBox ازش استفاده کنید.
امروز یه ابزار تازه‌نفس و خفن به اسم
Pantegnos
(نوشته شده با زبان قدرتمند Go) رو بهتون معرفی می‌کنیم که حلال همین مشکله!
این ابزار برای محققین شبکه و دور زدن فیلترینگ طراحی شده و کارش اینه که کانفیگ‌های اختصاصی و قفل‌شده‌ی کلاینت‌های مختلف رو می‌شکافه و دیتای اصلی رو براتون دیکریپت (رمزگشایی) می‌کنه.
🛠
کانفیگ‌های پشتیبانی‌شده تا این لحظه:
🔹
فرمت‌های Netmod (مثل کانفیگ‌هایی که با -nm شروع می‌شن)
🔹
فرمت‌های Slipnet
(توسعه‌دهنده گفته به زودی برنامه‌های بیشتری رو هم اضافه می‌کنه).
💻
نحوه استفاده:
کار با این ابزار خیلی سادست. اصلاً نیازی به بیلد کردن هم ندارید؛ فایل اجرایی آماده تو بخش Releases گیت‌هابش هست. کافیه کانفیگ‌های قفل‌شدتون رو بذارید داخل یه پوشه (مثلاً به اسم configs) و تو ترمینال سیستم این دستور رو بزنید تا فایل‌های استخراج‌شده رو تو پوشه خروجی تحویلتون بده:
./Pantegnos -input configs -output outputs
🔗
لینک پروژه و دانلود در گیت‌هاب:
https://github.com/FrontierTM/Pantegnos
📌
#رمزگشایی
#دیکریپت
#کانفیگ
#نت_مد
#VLESS
#ابزار
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/4916" target="_blank">📅 23:48 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
