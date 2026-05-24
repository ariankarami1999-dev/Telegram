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
<img src="https://cdn4.telesco.pe/file/ftPG1UWxIxWxqgwDDrkA27aBYI5hN0ZA3JjIhsd-8xe90mmcHE4xs4mYeDi7I0FNYh9JfqLyGhOKcSS8WsIsL2qBTcmZrvcNyzPXT-6RN1FhgRvUZ9WCA6n_oReAMgcOf3cMRMC4VWkww1uiWPmP7186AvUUhdZjLh5Qrx7cQtUPb81DjnDKs5F5mJUkCJTj4s-VhoU-S9AMuimr0ukVl3RzuRcHWzKbNSfUIDm21yHBk3Go9qOL5FN1BL6_J9OMtHRNnW-nWU2G_IF_TTsAjHrC5EWa-QpVMCoTPJmdFhFV3vnYcNx6uV4Dkp9bIl9aQRLEzz_f_eiNzmtPgYT1TQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.13K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 01:00:26</div>
<hr>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-text">🥮
آپدیت پروژه IR NETLIFY RELAY
📌
v 1.1.2
📦
ورود به سایت و دریافت فایل پروژه
🔸
روی دکمه Generate & Download ZIP کلیک کنید
🔹
فایلی که دانلود میشه استخراج کنید
🔸
داخل پوشه Template Sites چند تا سایت فیک هست
🔹
این 3 سایت فیک رو با فاصله 1 دقیقه در نتلیفای دپلوی کنید (روی یک پروژه)
🔸
هر سایت رو که دپلوی میکنید آدرس پروژه رو باز کنید تا طبیعی بشه
🔹
پس از دپلوی آخرین سایت فیک، روی همون پروژه کل فایل زیپ رو دپلوی کنید (استخراج نکنید)
⚠️
خیلی نرم شروع کنید ترافیک رد کردن
🔺
اکانت نتلیفای تمیز بسازید
🔺
جیمیل تمیز
🔺
آیپی تمیز
🌐
گیتهاب پروژه
⚙️
کانفیگ ساز
🌟
انرژی بگیریم
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 170 · <a href="https://t.me/archivetell/5382" target="_blank">📅 00:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Code obfuscator.html</div>
  <div class="tg-doc-extra">11.8 KB</div>
</div>
<a href="https://t.me/archivetell/5381" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
ابزار  Netlify obfuscator
یه ابزار سبک و به شدت کاربردی برای کسایی که روی
Netlify
پراکسی ران می‌کنن!
🌐
این ابزار بهتون کمک می‌کنه کدهاتون رو با کمک هوش مصنوعی کاملاً Obfuscate کنید (تغییر نام متغیرها و فایل‌ها) تا شناسایی نشن، و در نهایت
مستقیم یه فایل ZIP با پوشه‌بندی دقیق و آماده دیپلوی
تحویل بگیرید.
⚙️
چطور کار می‌کنه؟
1️⃣
پرامپت آماده‌ی داخل ابزار رو کپی می‌کنید و به همراه کدهای اصلیتون به هوش مصنوعی می‌دید.
2️⃣
متن خروجی هوش مصنوعی رو داخل ابزار پیست می‌کنید.
3️⃣
با یه کلیک، فایل .zip آماده شامل netlify.toml و توابع Edge رو دانلود می‌کنید!
✅
مزایا:
*
اجرای لوکال و آفلاین:
کاملاً روی مرورگر خودتون کار می‌کنه و هیچ دیتایی جایی ارسال نمیشه (امنیت ۱۰۰٪).
*
ساخت خودکار ساختار پوشه‌ها:
دیگه نیازی به ساخت دستی فایل‌ها و پوشه‌ها نیست.
*
ساده و سریع:
مناسب برای دیپلوی‌های پشت سر هم.
@ArchiveTell</div>
<div class="tg-footer">👁️ 623 · <a href="https://t.me/archivetell/5381" target="_blank">📅 00:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">trojan://humanity@127.0.0.1:40443?host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell%201
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%202
trojan://humanity@127.0.0.1:40443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%203
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%204
trojan://humanity@127.0.0.1:40443?alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#@ArchiveTell%205
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%206
trojan://humanity@127.0.0.1:40443?path=%2Fassignment&sni=www.multiplydose.com&type=ws#@ArchiveTell%207
این کانفیگا UDP ساپورتن
@ArchiveTell</div>
<div class="tg-footer">👁️ 332 · <a href="https://t.me/archivetell/5380" target="_blank">📅 23:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کانفیگ sni spoofing
vless://1b69417d-afc8-4f26-ab5d-fcf515e68492@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1&encryption=none&extra=%7B%22mode%22%3A%22auto%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&mode=auto&path=%2F&security=tls&sni=infinityservers.space&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/5379" target="_blank">📅 22:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
معرفی ابزار RM SNI Spoofer: دور زدن فیلترینگ با رابط گرافیکی (GUI)
---
رفقا اگر یادتون باشه قبلاً در مورد ایده جذاب SNI Spoofing (فریب دادن سیستم فیلترینگ با ارسال SNI تقلبی) از بچه‌های تیم Patterniha صحبت کردیم. حالا یک توسعه‌دهنده (rm-rfd) اومده و این پروژه رو کامل‌تر کرده و براش یک
رابط گرافیکی دسکتاپ (GUI)
ساخته!
💡
این ابزار دقیقاً چیکار می‌کنه؟
این برنامه قبل از اینکه ترافیک واقعیِ شما رو بفرسته، یک بستهِ تقلبیِ TLS (با یک SNI فیک و شماره توالیِ اشتباه) برای سیستم DPI (فیلترینگ) می‌فرسته. فیلترینگ با دیدن این بسته گول می‌خوره و مسیر رو باز می‌ذاره، اما سرور مقصد اون رو نادیده می‌گیره و دیتای اصلی شما بدون مشکل عبور می‌کنه!
✨
ویژگی‌های فوق‌العاده این نسخه جدید:
🔸
رابط کاربری گرافیکی (GUI):
دیگه نیازی به درگیری با محیط کنسول سیاه و کدهای پیچیده نیست؛ همه چیز با چند تا کلیک مدیریت میشه.
🔸
هسته داخلی Xray:
این برنامه خودش هسته Xray رو همراهش داره! یعنی خودش کانفیگ شما رو می‌خونه و بهتون پورت SOCKS5 و HTTP میده (عملاً بی‌نیاز از اجرای همزمان v2rayN).
🔸
مدیریت پروفایل‌ها:
می‌تونید چندین لینک مستقیم
vless://
یا
trojan://
رو داخلش ذخیره کنید و هر کدوم رو که خواستید Active کنید.
🔸
تست سلامت کانفیگ (Delay Test):
دقیقاً مثل کلاینت‌های استاندارد، می‌تونید از کانفیگ‌هاتون تست پینگ بگیرید تا ببینید کدوم سالم و سریع‌تره.
⚠️
نکات مهم برای استفاده:
- این برنامه فعلاً
فقط مخصوص ویندوز
هست.
- برای اجرای درست و دستکاری پکت‌ها (WinDivert)، حتماً باید برنامه رو با دسترسی ادمین (
Run as Administrator
) باز کنید.
- فقط از پورت ۴۴۳ برای ریموت پشتیبانی می‌کنه.
📥
لینک دانلود و دریافت نسخه اجرایی از گیت‌هاب:
🌐
https://github.com/rm-rfd/sni-spoofing-gui
📌
#معرفی_ابزار
#ویندوز
#SNI_Spoofing
#فیلترشکن
#تونل
#رابط_گرافیکی
#Xray
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/5377" target="_blank">📅 22:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
آموزش اختصاصی: حل قطعی مشکل لاگین نشدن در Windscribe
---
رفقا تو شرایط فعلی، خیلی وقتا سرورهای Windscribe سالمن و کار می‌کنن، اما API لاگینش فیلتر شده و اصلاً نمی‌تونید وارد اکانتتون بشید.
امروز یه ترفند اختصاصی و تضمینی داریم که با ترکیب
Proxifier
و
سایفون (یا WhiteDNS)
این محدودیت رو دور بزنیم و با موفقیت لاگین کنیم.
🛠
پیش‌نیازها:
۱. برنامه Proxifier (برای تونل کردن ترافیک)
۲. برنامه Psiphon یا WhiteDNS
###
💻
مراحل انجام کار (قدم‌به‌قدم):
مرحله اول: آماده‌سازی مسیر
۱. برنامه سایفون (یا WhiteDNS) رو باز کنید و متصل بشید.
💡
نکته مهم:
اگر از سایفون استفاده می‌کنید، ریجن (Region) رو روی
سوئد (Sweden)
یا کشوری بذارید که مطمئنید سایتِ اصلی Windscribe رو بدون مشکل باز می‌کنه.
مرحله دوم: تنظیمات Proxifier
۱. برنامه
Proxifier
رو باز کنید.
۲. از منوی بالا برید به
Profile ➔ Proxy Servers
.
۳. روی
Add
کلیک کنید و آی‌پی لوکال سیستم (معمولاً
127.0.0.1
) و
پورتِ
سایفون یا WhiteDNS رو وارد کنید (پروتکل رو روی SOCKS5 یا HTTPS بسته به خروجی برنامه‌تون تنظیم کنید) و OK رو بزنید.
مرحله سوم: ساخت رول (Rule) برای وینداسکرایب
۱. حالا تو همون Proxifier برید به مسیر
Profile ➔ Proxification Rules
.
۲. روی دکمه
Add
کلیک کنید تا یک Rule جدید بسازیم.
۳. در کادر
Applications
، روی Browse کلیک کنید و فایل اجرایی وینداسکرایب یعنی
windscribe.exe
رو انتخاب کنید.
۴. در پایین همون صفحه در بخش
Action
، منوی کشویی رو باز کنید و اون پروکسی سروری که تو مرحله قبل (مربوط به سایفون/WhiteDNS) ساختید رو انتخاب کنید.
۵. همه پنجره‌ها رو OK کنید تا تنظیمات ذخیره بشه.
✅
مرحله نهایی:
تمام! حالا برنامه Windscribe رو باز کنید. الان ترافیکِ لاگینِ وینداسکرایب داره از تونلِ سایفون عبور می‌کنه. یوزر و پسوردتون رو بزنید و به راحتی لاگین بشید.
⚠️
توجه:
بعد از اینکه با موفقیت لاگین کردید، می‌تونید Proxifier و سایفون رو کامل ببندید و از خودِ Windscribe (با پروتکل‌هایی مثل WStunnel یا Stealth) به صورت عادی استفاده کنید.
📌
#آموزش_اختصاصی
#وینداسکرایب
#Windscribe
#پروکسی_فایر
#سایفون
#Bypass
#آموزش_شبکه
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/5376" target="_blank">📅 22:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
hcaptcha.com
"
}
🔻
کانفیگ موردنیاز :
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?allowInsecure=1&ed=2560&eh=Sec-WebSocket-Protocol&encryption=none&host=sni.jpmj.dev&path=%2F&security=tls&sni=sni.jpmj.dev&type=ws#@ArchiveTell
آموزش sni spoofing
لینک داخلی V2rayn ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/5375" target="_blank">📅 22:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برای تونل شدن بازی‌ها و… با متود SNI SPOOF
یه روش که خودم تست کردم الان هم خیلی پایدار تره هم پینگش خوبه، هم میتونید به هر لوکیشنی که خواستید وصل بشید:
بعد از ران کردن اسپوف میتونید با
Se7en Pro
ترکیبش کنید (تو ستینگ برنامه قسمت Upstream Proxy
127.0.0.1:10808
) و باز تیک Allow lan بزنید تو ستینگ برنامش و تو گوشی به ادرس ایپی لپتاپ و پورتی که بهتون میده وصل بشید!
@NET_SPOOF
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/5374" target="_blank">📅 22:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ربات های سرچ تلگرام
@MotherSearchBot
@en_SearchBot
@SearcheeBot
@argo
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5373" target="_blank">📅 21:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آموزش بازی های انلاین با پینگ خوب برروی ویندوز با استفاده از روش SNI Spoofing
موارد مورد نیاز:
1-اتصال به Sni Spoofing
2-کلاینت V2ray
3-نرم افزار Windscribe که از قبل توش اکانت داشتید حتی اکانت فری و از قبل بهش لاگین کردید .(الان نمیشه بهش لاگین کرد اگه کسی روشی داره بگه بهمون )
شروع:
فرض بر این میگیریم شما با sni وصل هستید به اینترنت ازاد
روی v2ray پروکسی رو بذارید روی Clear system proxy و اصلا نباید حالت TUN روشن باشه .
حالا باید توی تنظمیات وایندسکرایب این تنظیمات رو اعمال کنید :
1-در بخش Connection روی split tunneling بزنید و بذارید روی Exclusive و در بخش app همون صفحه روی دکمه + بزنید و برنامه SNI SPOOFING رو پیدا کنید و اضافه ش کنید و مطمین بشید تیکش سبز باشه .
2-برگردید به بخش Connection و در قسمت Proxy setting و در بخش پروکسی تغییرش بدید به HTTP و ادرس و پورت زیر رو بذارید
127.0.0.1
10808
3-دوباره برگردید به بخش connection و Firewall رو بذارید روی حالت Manual
4- بخش conncetion Mode رو بذارید روی حالت manual و پروتوکل TCP و پورت 443
دقت کنید فقط پروتوکل TCP رو میتونید با این روش بهش وصل بشید و پینگ خوبی بهتون میده اگه اینترنت نرمالی داشته باشید .
سرور هم میتونید از المان فرانکفورت یا فرانسه جاردین استفاده کنید.
با این روش اینترنت شما مستقیم از وایندسکرایب گرفته میشه که هم اینترنت تمیزی بهتون میده که همه سایت ها و اپلیکیشن ها باز میشن هم پینگ خوبی بهتون میده .مطمینم میشه همین اینترنتو روی گوشی هم شیر کرد تا بتونید با اینترنت کامپیوترتون روی گوشی گیم بزنید ولی نمیدونم چجوری .
ویندسکرایب با هر ایمیل که بتونید وریفای کنید ماهانه 10 گیگ بهتون میده واسه گیم زدن کافیه فک کنم.</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5372" target="_blank">📅 21:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiFm-kaphU5KSeH-RyHCYvRqIGILxrk49-tshpqbO6orBc9t9Xx00GoqWBkuqzNLt9_4GGF69X_QRgFSyYMpIZM12wK9XWlD8GLpPeMRfXP6aNIhH67W7VLN-WzOXv3QHc0xhuxq9C3AzMJxdd9u88ADAMIld0jPSKYm18PN-x_yTLVsy9Elgq0iDYVBa0C6EUD1K0ZiSwo7_tFYSFMIX4Nd-PN5uw6pE3RsW4BS1mpPoHehlTJCOsMfqE-2LfQQ9w3rK5w_G-A46jaNroVMklYobf9MPcxxCYG4vhfMhxgIwQxHDTb_GatJXbj41VqE00lAQzAQPKZwqIcizM6ICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان واسه اینکه کلا ترافیک سیستم رو بتونید از داخل تانل فیلترشکن رد کنید و نیاز به غیر فعال کردن هم نداشته باشید برای شبکه داخلی یه راه حل خوب استفاده از
Throne
هست، همون نکوری هست ولی توسعه اش ادامه پیدا کرده و خیلی بهترش کردن
گزینه  Tun رو فعال کنید، بعدش پروفایل ایران رو دانلود کنید و بعدش هم فعال کنید، اینجوری شبکه ایران از داخل تانل فیلترشکن رد نمیشه
خیلی خیلی هم بهتر جواب میده از همه لحاظ این کلاینت</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5371" target="_blank">📅 20:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">معکوس کردن ویدیو و صدا برای ایجاد ویدیوهای جادویی
Reverse Video - Apps on Google Play
با برنامه Reverse Video، می‌توانید به‌راحتی ویدیو و صدا را معکوس یا به جلو پخش کنید تا افکت‌های سرگرم‌کننده، شگفت‌انگیز و جادویی ایجاد کنید. بخواهید کسی را طوری نشان دهید که به عقب می‌پرد، آب را دوباره به لیوان برگرداند یا به صورت معکوس صحبت کند — این برنامه انجام این کارها را آسان و خلاقانه می‌کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5370" target="_blank">📅 19:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📡
اشتراک‌گذاری اینترنت PC با گوشی (بدون نیاز به کانفیگ مجدد)
---
💡
رفقا، اگه کانفیگ (مثل SNI-SPOOF یا هر روش دیگه‌ای) روی سیستم (PC) براتون وصله، دیگه نیازی نیست روی گوشی هم جداگانه درگیرِ دور زدن فیلترینگ بشید! کافیه با یه تنظیم ساده، همون اینترنتِ آزاد رو مستقیم به اندروید و آیفون منتقل کنید.
⚠️
پیش‌نیاز خیلی مهم:
لپ‌تاپ/سیستم و گوشیِ شما باید دقیقاً به
یک مودم یا شبکه Wi-Fi
وصل باشن.
---
🖥
مرحله اول: آماده‌سازی v2rayN روی سیستم
۱. برنامه v2rayN رو باز کنید.
۲. از منوی بالا به مسیر
Settings ➔ Core Settings
برید.
۳. تیک گزینه
Allow LAN connections
رو فعال کنید و OK رو بزنید.
۴. از پایینِ صفحه اصلی v2rayN، پورتِ نوشته شده جلوی
Mixed Port
رو یادداشت کنید (معمولاً
10808
یا
10809
هست).
۵. حالا
CMD
ویندوز رو باز کنید و بنویسید:
ipconfig
۶. در اطلاعاتی که میاره، عددِ جلوی
IPv4 Address
رو یادداشت کنید (مثلاً
192.168.1.5
).
---
🤖
مرحله دوم: تنظیمات گوشی اندروید (Android)
۱. برید به تنظیمات وای‌فای (
Settings ➔ Wi-Fi
).
۲. روی اسم وای‌فای خودتون نگه دارید (یا آیکون چرخ‌دنده
⚙️
رو بزنید).
۳. گزینه
Edit
و بعد
Advanced options
رو انتخاب کنید.
۴. بخش Proxy رو روی حالت
Manual (دستی)
بذارید.
۵. حالا این اطلاعات رو وارد کنید:
•
Proxy hostname:
همون آدرس IPv4 سیستم (مثلاً
192.168.1.5
)
•
Proxy port:
همون پورت v2rayN (مثلاً
10808
یا
10809
)
۶. ذخیره (Save) کنید.
✅
تمام! الان مرورگر و اکثر اپ‌های اندرویدتون آزاد شدن.
---
🍎
مرحله سوم: تنظیمات گوشی آیفون (iOS)
۱. برید به تنظیمات وای‌فای (
Settings ➔ Wi-Fi
).
۲. روی آیکون (i) کنار اسم وای‌فای ضربه بزنید.
۳. بیاید پایین و
Configure Proxy
رو بزنید.
۴. روی حالت
Manual
قرار بدید.
۵. این اطلاعات رو وارد کنید:
•
Server:
آدرس IPv4 سیستم (مثلاً
192.168.1.5
)
•
Port:
پورت v2rayN (مثلاً
10808
یا
10809
)
۶. ذخیره (Save) کنید.
✅
تمام! آیفونتون هم از فیلترشکن لپ‌تاپ استفاده می‌کنه.
---
✈️
مرحله چهارم: وصل کردن تلگرام (بسیار مهم)
تلگرام پروکسیِ وای‌فایِ سیستم رو نادیده می‌گیره و باید جداگانه بهش پروکسی بدید:
۱. توی تلگرام برید به
Settings ➔ Data and Storage ➔ Proxy Settings
۲. روی Add Proxy بزنید و نوعش رو روی
SOCKS5
بذارید.
۳. اطلاعات رو وارد کنید:
•
Server:
آدرس IPv4 سیستم (مثلاً
192.168.1.5
)
•
Port:
همون پورت v2rayN (مثلاً
10808
)
۴. تیک ذخیره رو بزنید و فعالش کنید. تلگرام هم وصل شد!
---
⚠️
یک نکته مهم:
این روش فقط ترافیک رو پروکسی می‌کنه و تونل کامل (Full Tunnel) نیست:
•
✅
برای وب‌گردی، اینستاگرام، یوتیوب و دانلود کاملاً جواب میده.
•
❌
اما بعضی از گیم‌ها و اپلیکیشن‌های خاص ممکنه کار نکنن؛ برای اون‌ها باید کلاینت و کانفیگ رو مستقیماً روی خود گوشی نصب کنید.
📌
#آموزش
#شبکه
#ویندوز
#اندروید
#آیفون
#اشتراک_گذاری
#v2rayN
#پروکسی
#LAN
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5369" target="_blank">📅 19:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آموزش اشتراک گذاری sni spoofing رو گوشی
برای اشتراک گذاری همین کانفیگی که روی ویندوز متصل شدید به دیگر دستگاه ها مثل موبایل کافیه مراحل زیر را انجام بدید
ابتدا cmd ویندوز را باز کنید و دستور زیر را وارد کنید و اینتر بزنید :
ipconfig
در کادر ipv4 address ایپی مورد نظر را کپی کنید (این ایپی متغیر هست و هردفعه که ویندوز را ریستارت میکنید ممکنه تغییر کنه)
سپس در هر برنامه ای که روی اندروید یا ایفون دارید یک پروکسی socks5 یا http با مشخصات زیر بسازید :
Ip : YOUR WINDOWS IPV4 ADRRESS
این همون ipv4 address هست که مرحله قبل با دستور ipconfig گرفتید .
Port :10808
متصل بشید و لذت ببرید
نکته مهم:
سیستم و گوشی های مد نظر همه باید به یک اینترنت متصل باشند .
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5368" target="_blank">📅 17:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🛠
حل مشکل قطعی SNI Spoofing در حالت TUN (در v2rayN)
---
رفقا سلام!
✋
اگر موقع استفاده از روش SNI Spoofing، وقتی v2rayN رو روی حالت TUN (تونل کل سیستم) می‌ذارید اتصالتون قطع میشه، علاوه بر روشی که بچه‌های تیم Patterniha گفتن، یه راه حل خیلی ساده و تمیز هم از داخل خودِ تنظیمات v2rayN وجود داره!
فقط کافیه یک روتینگ (Routing) مستقیم (Direct) برای آی‌پیِ مربوطه اضافه کنیم تا ترافیکش به مشکل نخوره.
🖥
مراحل تنظیم روتینگ:
۱. برنامه v2rayN رو باز کنید و از منوی بالا به مسیر
Settings ➔ Routing setting
برید.
۲. روی دکمه
Add
کلیک کنید تا یک پروفایل جدید ساخته بشه.
۳. در کادر
Remarks
یک اسم دلخواه بنویسید (مثلاً
direct-4-snispoof
).
۴. حالا در همون صفحه، روی
Add rule
کلیک کنید.
۵. در پنجره‌ای که باز میشه،
Remarks
رو برای نظم بیشتر روی همون آی‌پی بذارید (مثلاً
104.19.229.21
).
۶. گزینه
Rule Type
رو روی
ALL
قرار بدید.
۷. گزینه
outboundTag
رو حتماً روی
direct
تنظیم کنید.
۸. در کادر
port
، پورتی که SNI Spoof استفاده می‌کنه رو بنویسید (اکثراً
443
هست).
۹. برای
protocol
و
inboundTag
تیکِ همه‌ی گزینه‌ها رو بزنید.
۱۰. برای گزینه
network
هر دو مورد
tcp
و
udp
رو انتخاب کنید.
۱۱. حالا تو کادر بزرگِ
IP or IP CIDR
، همون آی‌پی‌ای که با SNI Spoof بهش وصل میشید رو بنویسید (مثلاً برای الان
104.19.229.21
هست).
۱۲. تو کادر
Domain
هم آدرس
hcaptcha.com
رو وارد کنید.
۱۳. در نهایت تمام پنجره‌ها رو
Confirm
کنید تا ذخیره بشن.
✅
مرحله آخر (فعال‌سازی):
حالا برگردید به صفحه اصلی برنامه. از همون نوار پایین برنامه (کنار جایی که پروکسی سیستم رو تنظیم می‌کنید)، منوی کشویی Routing رو باز کنید و اون پروفایلی که الان ساختید (direct-4-snispoof) رو انتخاب کنید. تمام! اینترنت بدون مشکل تونل میشه.
📌
#آموزش
#ویندوز
#v2rayN
#روتینگ
#Routing
#SNI_Spoofing
#تونل
#حل_مشکل
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5367" target="_blank">📅 17:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چیه همش با روش های رایگان وصل میشین؟؟؟
کانفیگ فروشا زن و بچه ندارن؟ زندگی ندارن؟ نباید ۲ تومن بیاد سر سفرشون؟
#طنز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5366" target="_blank">📅 17:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شیر و خورشید همراه اول و آپتل وصل
- SNI:
yryirjrhqffsxwpg-a.akamaihd.net
- IP:
63.141.252.203
لینک داخلی شیر و خورشید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5365" target="_blank">📅 16:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">trojan://humanity@127.0.0.1:40443?host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell%201
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%202
trojan://humanity@127.0.0.1:40443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%203
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%204
trojan://humanity@127.0.0.1:40443?alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#@ArchiveTell%205
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%206
trojan://humanity@127.0.0.1:40443?path=%2Fassignment&sni=www.multiplydose.com&type=ws#@ArchiveTell%207
این کانفیگا UDP ساپورتن
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5364" target="_blank">📅 16:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آموزش sni spoofing
کانفیگ ها ۱
|
کانفیگ ها ۲
لینک داخلی V2rayn ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5363" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">برای مک از ازین ریپو هم میتونید استفاده کنید
https://github.com/selfishblackberry177/sni-spoof/releases/
1. فایل دانلودی رو با config.json داخل یه دایرکتوری بگذارید
2. داخل ترمینال cd بزنید و دایرکتوری رو بیارید
3. sudo ./sni-spoof-darwin-arm64 config.json</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/5362" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">🍷
ورژن Python برای SNI Spoofing:
https://github.com/patterniha/SNI-Spoofing
ورژن Rust برای SNI Spoofing:
https://github.com/therealaleph/sni-spoofing-rust
ورژن Go برای SNI Spoofing:
https://github.com/aleskxyz/SNI-Spoofing-Go
ورژن اپ مک برای Sni spoofing:
https://github.com/g3ntrix/Cloak
👑
@ArchiveTell
💎
@xsfilterrnet</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5361" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel(𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣⚡️)</strong></div>
<div class="tg-text">🚀
معرفی ابزار FakeSNI: دور زدن فیلترینگ با تزریق SNI فیک (مخصوص لینوکس)
---
رفقا سلام!
✋
در پیرو پست قبلی که درباره مستقیم شدن دامنه hCaptcha و روش SNI Spoofing صحبت کردیم، حالا وقتشه یه ابزار عالی برای پیاده‌سازی این متد روی سیستم‌عامل لینوکس معرفی کنیم.
پروژه
FakeSNI
یه نسخه بازنویسی‌شده، سریع و بسیار تمیز از پروژه معروف
patterniha
هست که با زبان Go نوشته شده.
🔥
این ابزار چطور فیلترینگ رو دور می‌زنه؟
این برنامه روی لینوکس یه پروکسی TCP می‌سازه. دقیقاً بعد از اینکه دست‌دادنِ اولیه (TCP Handshake) با سرور انجام شد، این ابزار یه بسته حاوی
ClientHello
با یک SNI فیک (همون دامنه‌ای که فیلتر نیست مثل
hcaptcha.com
) رو به بیرون تزریق می‌کنه.
چون شماره توالی (Sequence Number) این بسته عمداً دستکاری شده، سرورِ مقصد اون رو دور می‌ندازه؛ اما سیستم فیلترینگ (DPI) وسط راه گولِ همون بسته رو می‌خوره، فکر می‌کنه سایت مجازی رو باز کردید و مسیر رو برای دیتای اصلیِ شما باز می‌ذاره!
🤯
🛠
پیش‌نیازها برای اجرای ابزار:
🔸
سیستم‌عامل لینوکس (Ubuntu, Debian و غیره)
🔸
داشتن دسترسی روت (Root)
🔸
فعال بودن
iptables
روی سیستم (که معمولاً روی همه لینوکس‌ها هست).
💻
نحوه استفاده خیلی ساده:
۱. سورس برنامه رو از گیت‌هاب دانلود یا بیلد کنید.
۲. یه فایل به اسم
config.json
بسازید و دقیقاً مثل پست قبلی، تنظیمات آی‌پی و SNI فیک رو توش قرار بدید.
۳. ابزار رو با دسترسی روت و دستور زیر اجرا کنید:
sudo ./fakesni -config config.json
(نکته: این ابزار خودش به صورت خودکار رول‌های iptables رو تنظیم و بعد از بسته شدن پاک می‌کنه).
🔗
لینک سورس کد و توضیحات کامل در گیت‌هاب سازنده:
🌐
https://github.com/PechenyeRU/FakeSNI
📌
#معرفی_ابزار
#لینوکس
#فیلترینگ
#اسنیف
#FakeSNI
#SNI_Spoofing
#DPI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/5360" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">لینک داخلی V2rayn ویندوز
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/5359" target="_blank">📅 15:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش استفاده از tun موقع استفاده از sni spoofing:  خیلیها سوال داشتند که چطور کل سیستم رو موقع استفاده از sni-spoofing تونل کنیم تا بازی ها و ... هم بتونن تونل شن. دقت کنید در این روش دیگه نیازی به سایفون و وینداسکریب و ... برای tun کردن کل سیستم نیست و مستقیم…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/5358" target="_blank">📅 15:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش استفاده از tun موقع استفاده از sni spoofing:
خیلیها سوال داشتند که چطور کل سیستم رو موقع استفاده از sni-spoofing تونل کنیم تا بازی ها و ... هم بتونن تونل شن.
دقت کنید در این روش دیگه نیازی به سایفون و وینداسکریب و ... برای tun کردن کل سیستم نیست و مستقیم کانفیگتون به کل سیستم تونل میشه.
همچنین میتونید tun رو به راحتی شیر کنید تا دستگاههای دیگه (مثل ps و xbox  و ...) بدون نیاز به v2ray مستقیم از کانفیگ لپتاپ شما استفاده کنند.
۱. برای اینکار cmd را با run as admin  قبل از قرار دادن v2rayN در حالت tun اجرا کنید و سپس دستور زیر را اجرا کنید:
netsh interface ipv4 add route 104.19.229.21/32 "Wi-Fi" 192.168.1.1 metric=1
دقت کنید بعضی پارامترها را نیاز دارید تغییر دهید:
اول ۱۰۴.۱۹.۲۲۹.۲۱ باید همان connect_ip شما در sni_spoofing_by_patterniha باشد،
دوم "Wi-Fi" باید اسم اینترفیسی باشد که از آن اینترنت میگیرید و در صورتی که با وایفای متصلین معمولا همین "Wi-Fi" هست، به هر حال میتوانید با دستور ipconfig اسم اینترفیس رو هم ببینید.
سوم default-gateway هست که اگر به وای فای خانه وصلین معمولا همین
192.168.1.1
است و اگر با گوشی اینترنت رو برای لپتاپ شیر کردید default-gateway برابر ip گوشی میباشد، به هر حال مقدار default-gateway را میتوانید با استفاده از دستور ipconfig مشاهده کنید.
۲. در تنظیمات dns-settings در نرم افزار v2rayN مقدار remote-dns را برابر
https://dns.google/dns-query
قرار دهید (چون بسیاری از ورکر استفاده میکنند و ممکنه dns کلودفلر براشون در دسترس نباشه)  و حالت tun را فعال و استفاده کنید.
///
دقت کنید با ری استارت کردن کامپیوتر route اضافه شده پاک میشود و باید دوباره دستور را وارد کنید. (میتوانید با  اضافه کردن  store=persistent به دستور route رو به طور دائمی اضافه کنید ولی پیشنهاد نمیشود چون ip ممکن است عوض شود)
///
اگه شرایط پایدار بمونه تو ورژن ۲ این دستور رو به صورت خودکار اضافه میکنم و log رو هم درست میکنم.</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/5357" target="_blank">📅 15:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲ خرداد
👾
لینک دانلود
کلاینت :
3️⃣
WhiteDNS
1.5.1
3️⃣
Windows
|
Linux
|
Mac
1
.0.0 Beta3
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihWSVAtMSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidmlwMS5tYXNpci1zZWZpZC50ZWNoIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihDSVAtMSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiY2lwMS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihDSVAtMikiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiY2lwMi5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihDSVAtMykiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiY2lwMy5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihDSVAtNCkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiY2lwNC5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihDSVAtNSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiY2lwNS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
⚡️
پک ریزالور
⬅️
فیلم
اموزش
اندروید
|
دسکتاپ
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5356" target="_blank">📅 15:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">sub2.txt</div>
  <div class="tg-doc-extra">87.9 KB</div>
</div>
<a href="https://t.me/archivetell/5355" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حدود 400 کانفیگ spoof همش پینگ داد واسه من. با
104.19.229.21
تقدیم به همتون
💪</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5355" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SNI-Spoofing_by_patterniha_v1.rar</div>
  <div class="tg-doc-extra">9.8 MB</div>
</div>
<a href="https://t.me/archivetell/5354" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل برنامه رو ران از ادمین کنید(همین)
وصل شید این کانفیگ
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&fp=chrome&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#archivetell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/5354" target="_blank">📅 14:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تشکر از دوستانی که نبض بازار کانکت شدنو تو دایرکت بما میگن
اگه چیزی میدونین کار میده اینا دایرکت پیام بذارین، تو چنل بذاریم
https://t.me/archivetell?direct</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5353" target="_blank">📅 14:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فرانسه برگشت
😁</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5352" target="_blank">📅 14:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسپوف کامبک..</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5351" target="_blank">📅 14:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اینارو تست کنید
hcaptcha.com
https://www.hcaptcha.com/cdn-cgi/trace
اگر براتون هر کدوم اومد بدونید میتونید استفاده کنید
اینم آیپی ها برای تست
85.198.12.209
2.144.19.238
185.236.38.44
95.38.177.31
46.38.137.156
81.12.32.136
104.19.229.21
🔥
104.19.230.21
🔥</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5350" target="_blank">📅 14:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانفیگ اسپوف
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?allowInsecure=1&encryption=none&host=sni.111000.indevs.in&path=%2F%3FTelegram%D9%8B+%40ProxyVPN11&security=tls&sni=sni.111000.indevs.in&type=ws#%DB%B1
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?allowInsecure=1&encryption=none&host=sni.latonyamadeline.ndjp.net&path=%2F%3Fhttps%3A%2F%2Ft.me%2FProxyVPN11%F0%9F%87%A8%F0%9F%87%B3%3D&security=tls&sni=sni.latonyamadeline.ndjp.net&type=ws#%DB%B2
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B3
trojan://1710442808@127.0.0.1:40443?allowInsecure=1&host=subb.nrshop198.workers.dev&path=%2F&sni=subb.nrshop198.workers.dev&type=ws#%DB%B4
trojan://humanity@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B5
trojan://humanity@0.0.0.0:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B6
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.multiplydose.com&path=%2Fassignment&sni=www.multiplydose.com&type=ws#%DB%B7
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#%DB%B8
trojan://humanity@127.0.0.1:40443?allowInsecure=1&path=%2Fassignment&sni=www.multiplydose.com&type=ws#%DB%B9
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B1%DB%B0</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5349" target="_blank">📅 14:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
hcaptcha.com
"
}
رایتل تست شده ، بقیه نتا تست کنید</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5348" target="_blank">📅 14:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسپوف کامبک..</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5347" target="_blank">📅 14:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چنل سطح مقاومت 8 هزار رو رد کرده و احتمالا این سطح نقش حمایت رو در اینده ایفا خواهد کرد.
در روز گذشته یکی دوبار به سمت 8 هزار پولبک زد
انتظار میره در روز های آینده چنل سقف های قبلی رو بشکنه</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5346" target="_blank">📅 14:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این داستان گروه های ۲۰۱۶ قدیمی اینا چیه داستانش؟
😐
همش واسم سوال بوده</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5345" target="_blank">📅 13:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">92.123.106.90
Google.com
اینم رو مودم ایرانسل وصله</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5343" target="_blank">📅 12:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">142.54.178.211
jkiysqntxacscicm-a.akamaihd.net
همراه اول وصله</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/5342" target="_blank">📅 12:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آپدیت جدید شیر و خورشید
نصب کنید
قسمت آیپی و sni خالی بذارید ، بزنید اتصال ، خودش اسکن میکنه و وصل میشه</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5341" target="_blank">📅 11:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مخابرات  اوووف وصله  yryirjrhqffsxwpg-a.akamaihd.net  142.54.178.211  تشکر از یکی از ممبرا @ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5340" target="_blank">📅 11:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">😐
😂
😂
مخابرات ظاهرا خیلی بده اگه جواب گرفتین بگین رو چه اپراتوری بهتره</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5339" target="_blank">📅 11:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF9pP4kQ6DYLOTqAZ3IYgXrAtjgH1haQ-A5yY19qaS4sJLBf6sLR8y1Pnc2iZBn8mALe7lr0pvIW6gIv3smfiiJ89J5dnjw-Nu6SLXG5GEQ1GJ_WmASdnmpbJhhgonSO8aeh4UhzBgZJKbzqU3Bj1ehcgKEm2PFxdTfd2d_7aheDbuQzahO0tFwzDMNJYAmFR8ib6Wlc3kNN0l0h2rff5BRdmgC4vQ4prN5fIoqepDDVV08kOBnzfy4U9JPQlPrfjzHb4-2qNPhWDjwIOxzCvTy61jqbxkUswJPxq--2wc33OA_wwl-DhcODXR1yfNCUgnFx0Ujt_JdCSDFyJF-QdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😂
😂
مخابرات ظاهرا خیلی بده
اگه جواب گرفتین بگین رو چه اپراتوری بهتره</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5338" target="_blank">📅 10:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">لینک داخلی آپدیت شیر و خورشید
https://punkpaste.ir/f/ShirOKhorshid-2026-0-03iy5e
https://dl.toolschi.com/view.php?f=43accc69841b6088.zip
https://punkpaste.ir/f/ShirOKhorshid-2026-0-03iy5e</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5337" target="_blank">📅 10:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1nYw7pxO0D-4XrB31rkIq4WqsbEMos9p5mwULV6tdDFs9lkyyA9oHMBBRkGD5r7x82L7ukeGDMlq_lOc4acPH2v_nVSzT0-HCRevU5tRu9Wr4D1LC8lMhBiNYLINzhx3nYBaGYQaXdkNn49uXMcsQkRvGZlfNkrrGRMI9GM6l7jDquhvkVNijCqVGdmIg-gzOXaPyLYRWhey0WJP3xNu4cebfl2enuAMHGsUnPy8_oxInWDhWTJoNnmtYKtuX9KMFrWG0EykEw58TERgmsvU3FLwJ2Fc_YtUIy2VAHbQK6_i6zWP49oPjiapmMWMBmkRAh9dSxeB1CeU5nIGcmo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثه قبل start بزنین تا اسکن کنه
و قبلش تنظیمات قدیمیِ IP و SNI رو از قسمت Settings برنامه کاملاً پاک کنید (خالی بذارید)</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5336" target="_blank">📅 10:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.24.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/archivetell/5335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/archivetell/5335" target="_blank">📅 10:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
آپدیت جدید کلاینت "شیر و خورشید" برای اندروید (نسخه 2026.05.24)
---
رفقا سلام!
✋
نسخه جدید و جذاب کلاینتِ شیر و خورشید منتشر شد. توی این آپدیت، تمرکز اصلی روی پیدا کردنِ آی‌پی‌های سالم و بهبود اتصال روی CDN Fronting بوده.
✨
تغییرات و امکانات جدید این نسخه:
🔸
اسکنر قدرتمند آی‌پی (IP Scanner):
برنامه حالا یک لیستِ بسیار بزرگ از آی‌پی‌های ممکن رو در خودش جا داده.
💡
نکته مهم:
اگر در اتصال مشکل دارید، پیشنهاد میشه تنظیمات قدیمیِ IP و SNI رو از قسمت Settings برنامه کاملاً پاک کنید (خالی بذارید) و اجازه بدید خود برنامه اسکن رو انجام بده. *(دقت کنید اسکنِ بار اول ممکنه خیلی طول بکشه، حتی چند ساعت! پس صبور باشید).*
🔸
بهبود اتصالات (CDN Fronting):
پروتکل‌های بیشتری که با CDN Fronting کار می‌کنن به برنامه اضافه شده؛ در نتیجه احتمالِ وصل شدن و سرعت کلیِ شما باید بهتر از قبل باشه. قابلیت Beast Mode هم برای کارکرد درست روی این حالت آپدیت شده.
🔸
تنظیمات حرفه‌ای LAN Proxy:
حالا می‌تونید «پورت» دلخواه خودتون رو برای پروکسی کردنِ شبکه خانگی (LAN) تنظیم کنید. همچنین امکان تعیین Username و Password اضافه شده تا امنیت بالا بره و فقط کسانی که رمز رو دارن بتونن تو شبکه بهتون وصل بشن.
🔸
خاموش کردن تبلیغ سایفون:
بالاخره قابلیت غیرفعال کردنِ سایتی که بعد از اتصال سایفون به صورت خودکار باز میشه، اضافه شد!
🔸
آپدیت هسته:
هسته‌ی اصلی نرم‌افزار (سایفون) به آخرین نسخه ارتقا پیدا کرده.
---
📥
دریافت آپدیت:
می‌تونید فایل نصب (APK) رو مستقیماً از لینک گیت‌هابِ زیر دانلود کنید. اگر از این ابزار استفاده می‌کنید و براتون وصل میشه، پست رو برای بقیه هم بفرستید تا استفاده کنن.
👇
🔗
https://github.com/shirokhorshid/shirokhorshid-android/releases/tag/v2026.05.24-a3b91cf
📌
#آپدیت
#شیر_و_خورشید
#سایفون
#فیلترشکن
#اندروید
#تونل
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/5333" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b4dd5d5da.mp4?token=CqFS4A2Xv9fI2Nej9v2IXCpxH2TiUkFuVrD-rcJ6VOOjWQand8v2DFsqTYMd-U_bP0tSuhATW6Pbzi6MjsJJChP9e7RaAEq2orqxn3WsZfK-iDtWo3qHvLJiFGVMsp7Er8TZrExWlUsxkHbp6SGsSRoGtqYd4MNczdfC6s0vBnw7PNAntTQCzDRzEE06-MahqcVUpM-TVZsh71Jkz4X4hXqS5Yp6TCsidEKXaMG5QqnEmDodz-pHsmLEgfdWinm_MT5Xyu1X_BsMkZVyWy4Ym5Hlz8tS50PDh91FL_bAor88V2rRNuQq5zNOwZWYreC584Usb9aEVdjg1r4W0Fa7OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b4dd5d5da.mp4?token=CqFS4A2Xv9fI2Nej9v2IXCpxH2TiUkFuVrD-rcJ6VOOjWQand8v2DFsqTYMd-U_bP0tSuhATW6Pbzi6MjsJJChP9e7RaAEq2orqxn3WsZfK-iDtWo3qHvLJiFGVMsp7Er8TZrExWlUsxkHbp6SGsSRoGtqYd4MNczdfC6s0vBnw7PNAntTQCzDRzEE06-MahqcVUpM-TVZsh71Jkz4X4hXqS5Yp6TCsidEKXaMG5QqnEmDodz-pHsmLEgfdWinm_MT5Xyu1X_BsMkZVyWy4Ym5Hlz8tS50PDh91FL_bAor88V2rRNuQq5zNOwZWYreC584Usb9aEVdjg1r4W0Fa7OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چت‌جی‌پی‌تی به سمت شخصی‌سازی بیشتر پیش می‌رود.
نسخه چت‌جی‌پی‌تی پلاس اکنون قابلیت بهره‌گیری از خاطرات، گفتگوهای پیشین و فایل‌های متصل به کاربر را دارا می‌باشد تا پاسخ‌های هوشمندانه‌تری ارائه دهد، بدون آنکه نیاز باشد زمینه گفتگو در هر بار مجدداً تکرار شود.
شرکت OpenAI همچنین مکانیزم‌های کنترلی برای مدیریت، به‌روزرسانی یا حذف اطلاعاتی که چت‌جی‌پی‌تی ذخیره می‌کند، اضافه نموده است.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5332" target="_blank">📅 09:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aa3af6eac.mp4?token=NMUhtSyyajG0PlduYQvqUhUizmRmtn1d_y2mITmkElsAaQsh0zY5S7rVtVH3ZfVz1MfMm4JA5DWNIOor0kN08HB6s0p5_sYqZddEMes42ebaLU0nwnd_xAPKudrChdvadghVrgrhNVAGStvvI4hgQxhPQKqCbf1gtgJEZ8Ra3N9T99FYN5BYEPEAT_ujeQPaIbM8f3Zc_ZYWFUCgTJax59GWCDWjhVC0DlnTWr-72mta4hG6etcU2f_5ZZzP1gxLATabp8Ceo9_xq0iOkYUXebKwYjTBNAuYi_i6a93WIxoWjNPhL08qco7Tbw37wGC3AsNwOiF3Xo8ZibVHae0UUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aa3af6eac.mp4?token=NMUhtSyyajG0PlduYQvqUhUizmRmtn1d_y2mITmkElsAaQsh0zY5S7rVtVH3ZfVz1MfMm4JA5DWNIOor0kN08HB6s0p5_sYqZddEMes42ebaLU0nwnd_xAPKudrChdvadghVrgrhNVAGStvvI4hgQxhPQKqCbf1gtgJEZ8Ra3N9T99FYN5BYEPEAT_ujeQPaIbM8f3Zc_ZYWFUCgTJax59GWCDWjhVC0DlnTWr-72mta4hG6etcU2f_5ZZzP1gxLATabp8Ceo9_xq0iOkYUXebKwYjTBNAuYi_i6a93WIxoWjNPhL08qco7Tbw37wGC3AsNwOiF3Xo8ZibVHae0UUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
مایکروسافت AI Engineer Coach را به صورت اوپن‌سورس منتشر کرده است — افزونه‌ای برای VS Code، Cursor و Antigravity که کارایی عوامل هوش مصنوعی شما را به حداکثر می‌رساند.
https://github.com/microsoft/AI-Engineering-Coach
کارهایی که انجام می‌دهد:
• لاگ‌های محلی جلسات را از GitHub Copilot، Claude Code، Codex CLI، OpenCode و Xcode می‌خواند.
• جریان کاری شما را بر اساس ۵ پارامتر ارزیابی می‌کند، از جمله کیفیت پرامپت‌ها و مدیریت زمینه.
• بر اساس پایگاه داده‌ای شامل ۴۵ الگوی خطا بررسی می‌کند: مثلاً سوختن غیرضروری توکن‌ها یا جلسات خیلی طولانی.
• همه قوانین بررسی را در فایل‌های معمولی Markdown (.md) ذخیره می‌کند تا به راحتی قابل اصلاح باشند.
• الگوهای تکراری در پرامپت‌ها را پیدا کرده و آن‌ها را به مهارت‌هایی برای عوامل هوش مصنوعی تبدیل می‌کند.
در نهایت، سیستمی بهینه‌شده برای اتوماسیون هر پروژه‌ای از شما به دست می‌آید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5331" target="_blank">📅 09:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">trojan://humanity@45.89.221.111:443?path=%2Fassignment&sni=www.ignitelimit.com&type=ws#ArchiveTell%20
مخابرات و آسیاتک وصل</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5330" target="_blank">📅 02:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قیمت لحظه ای‌ کریپتو های معروف در تلگرام  https://t.me/addlist/X6c9tOtZoLhkZTAy</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5329" target="_blank">📅 01:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4726a7517b.mp4?token=cQ9DWTb8n3Q4hhGErDQoFoyxfdQTN2P812ZzaBIinWO2larEs-wjVI2Y5GeqHT5NWLy9x9exyA4VJr_-Ticxx0TRhKDxpPEunf2c4afcddXerMrQTRq1T5EXwRAF3Cc5CcOVsCiu3j0IvRnyYaCGlvdsAFoy1arckcxnBiVGpU4shYhWHCdMxVRL487UySAwM4t_e5MGxf8MSJhbCONgt08TQd-2m00pj2shxR4S2cjGTXmRJBQxAM-G3PHB7HcHNad9VpZgzyNTI5G6GQefNDEzgmoDrc-z1af-2RjChQ3Byqy5UhegcBk74yjv0fdK0W55sdazrGszyg3r7hV0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4726a7517b.mp4?token=cQ9DWTb8n3Q4hhGErDQoFoyxfdQTN2P812ZzaBIinWO2larEs-wjVI2Y5GeqHT5NWLy9x9exyA4VJr_-Ticxx0TRhKDxpPEunf2c4afcddXerMrQTRq1T5EXwRAF3Cc5CcOVsCiu3j0IvRnyYaCGlvdsAFoy1arckcxnBiVGpU4shYhWHCdMxVRL487UySAwM4t_e5MGxf8MSJhbCONgt08TQd-2m00pj2shxR4S2cjGTXmRJBQxAM-G3PHB7HcHNad9VpZgzyNTI5G6GQefNDEzgmoDrc-z1af-2RjChQ3Byqy5UhegcBk74yjv0fdK0W55sdazrGszyg3r7hV0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ تتر: 167,600 تومان ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ تاریخ: 1405/03/03 ساعت: 01:10</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/archivetell/5328" target="_blank">📅 01:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c57ee64b0.mp4?token=SkwJu2aqADg_YkxyItP-2BAftDepXmNfDg-tyBiVRADh0hTzxaIM2ftmMo7pxUvJulUdaLCXU6c6i0OzmnMnxE62nl3ZZ2qV3fpwJTkdLXXlUYt8bddGvE0YMZ9HTC02VT6CBPdjccdyR9GjdDgzSyLYUhWapWTLoo1Q_kMIZgxV_db77bToVV86xrCE8wokbhFOs0twhixTc3Guvo20voqSej9h2GakFUasPXakFzOUj9q4Qk00pWZ8oWQSptM4sdWBfeq6FTJpybaEt8aHwFR-ftj0qEjIaO6UQJRL74I-i1__AfrNFgyEOH9Enlfw-Iv-yOcFM2rI0g5CvgV-yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c57ee64b0.mp4?token=SkwJu2aqADg_YkxyItP-2BAftDepXmNfDg-tyBiVRADh0hTzxaIM2ftmMo7pxUvJulUdaLCXU6c6i0OzmnMnxE62nl3ZZ2qV3fpwJTkdLXXlUYt8bddGvE0YMZ9HTC02VT6CBPdjccdyR9GjdDgzSyLYUhWapWTLoo1Q_kMIZgxV_db77bToVV86xrCE8wokbhFOs0twhixTc3Guvo20voqSej9h2GakFUasPXakFzOUj9q4Qk00pWZ8oWQSptM4sdWBfeq6FTJpybaEt8aHwFR-ftj0qEjIaO6UQJRL74I-i1__AfrNFgyEOH9Enlfw-Iv-yOcFM2rI0g5CvgV-yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت الان :</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5327" target="_blank">📅 01:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نرخ تتر: 167,600 تومان
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
تاریخ: 1405/03/03
ساعت: 01:10</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5325" target="_blank">📅 01:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e97817b2.mp4?token=RQz4pvJPmgocsrOtoyCiSGlo8xfYmdU-iSFL5G2x97yWQ2K0oW36OUFe_3pU4sV9J8Y_-vI48gIOwRYCCSJpgbitZQjwGeQ0sik6eS0XTN3rrfmTtVEfJRR_XNmOBrED1y_F9EtKEpS_fsnSPGUPZcfsLJNaeXg4Gb16AJrwodzknwDTRzpb0Tc4SfL0hXuUk-XHZna6Q9TX2vE60OJoFcjsFpjny6A_thTdO_hB1GvKvifrAbPtZ_7pVQxyovU-6dP31iGmfTiNjXosDWv0NY8UqLgIC0PdAtZiPGpLpPPOZqiVxzO_6NOPj4cqjHp9cccZo7ia7n1GkcJlZKGsNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e97817b2.mp4?token=RQz4pvJPmgocsrOtoyCiSGlo8xfYmdU-iSFL5G2x97yWQ2K0oW36OUFe_3pU4sV9J8Y_-vI48gIOwRYCCSJpgbitZQjwGeQ0sik6eS0XTN3rrfmTtVEfJRR_XNmOBrED1y_F9EtKEpS_fsnSPGUPZcfsLJNaeXg4Gb16AJrwodzknwDTRzpb0Tc4SfL0hXuUk-XHZna6Q9TX2vE60OJoFcjsFpjny6A_thTdO_hB1GvKvifrAbPtZ_7pVQxyovU-6dP31iGmfTiNjXosDWv0NY8UqLgIC0PdAtZiPGpLpPPOZqiVxzO_6NOPj4cqjHp9cccZo7ia7n1GkcJlZKGsNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب دوستان قراره سنگین بزنن</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5324" target="_blank">📅 01:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4024c3c872.mp4?token=NhOxMmyVvjrsEarNZ7Ix0twcTMOUepzubdY5E0c3xikU2u8lkNXlNbareGzBqliOD7aZbaHa6gfcDVjXZSWzvXulHAUiy1bOB-R_QdYl6lK0hYqK8gAhu4d_cHNza7PXUaUIWOt4COxgenQ_stPpwY-1npjBRlHFGaUrm3c5M4tWU_biXfu3mvWewhXuum_6TIx4cXurf9McDwV3v6Onmv93BeDgdWbre9IcLV7xX0HcuhLwDmATqnZ_Bdxjgi-LJtG1kixqeR1p6rpNZkq8KtTuJGoqMZXJdxM4bcKU1nr_ED8i4AFriPwb0Lb_f3VMAHcQg_F81Csf6t5tMrnvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4024c3c872.mp4?token=NhOxMmyVvjrsEarNZ7Ix0twcTMOUepzubdY5E0c3xikU2u8lkNXlNbareGzBqliOD7aZbaHa6gfcDVjXZSWzvXulHAUiy1bOB-R_QdYl6lK0hYqK8gAhu4d_cHNza7PXUaUIWOt4COxgenQ_stPpwY-1npjBRlHFGaUrm3c5M4tWU_biXfu3mvWewhXuum_6TIx4cXurf9McDwV3v6Onmv93BeDgdWbre9IcLV7xX0HcuhLwDmATqnZ_Bdxjgi-LJtG1kixqeR1p6rpNZkq8KtTuJGoqMZXJdxM4bcKU1nr_ED8i4AFriPwb0Lb_f3VMAHcQg_F81Csf6t5tMrnvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/archivetell/5323" target="_blank">📅 00:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب دوستان قراره سنگین بزنن</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5322" target="_blank">📅 00:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار  قیمت عالی  @ArchiveTellbot  آموزش ساده خرید تو پست بعدی..</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/archivetell/5321" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پخت و پز باشه  https://github.com/MHSanaei/3x-ui/releases/tag/v3.1.0</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/archivetell/5320" target="_blank">📅 21:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قیمت لحظه ای‌ کریپتو های معروف در تلگرام
https://t.me/addlist/X6c9tOtZoLhkZTAy</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5319" target="_blank">📅 21:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پخت و پز باشه
https://github.com/MHSanaei/3x-ui/releases/tag/v3.1.0</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5318" target="_blank">📅 21:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستان تو ویندوز ترکیبی وصل میشه با سرعت قابل قبول
پیش نیاز  :
آ
خرین ورژن v2rayN
آخرین ورژن سایفون
sni spoofing
به ترتیب اول Sni  :
"CONNECT_IP": "
85.9.112.219
",
"FAKE_SNI": "
www.hcaptcha.com
"
بعد  :v2rayN
این کانفیگ رو اکتیو کنید ، set نکنید
trojan://humanity@127.0.0.1:40443?host=www.gossipglove.com&path=%2Fassignment&sni=www.gossipglove.com&type=ws#@ArchiveTell
پینگ نگیرید چون پینگ نمیده فقط این کانفیگ رو فعال کنید
بعد سایفون :
upstream proxy
host :
127.0.0.1
port: 10808
کانکت و تمام
(پینگ اصلا مهم نیست امتحان کنید وصل میشه)</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/archivetell/5317" target="_blank">📅 19:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5ef99e9cca.mp4?token=Uu1wkSidObX_JY5i0_RLNH1zH5J8-npeuXYUArVABiDCi8ovxeoyUQkA7JHAmMir7y76yT_EioWZPSq0i79_E4QterDyCD7sKkzMAJ5GeaDBBq0lQnZJ8KgXm1XKerycPpovnlaEHsupcVExmrKznOpYmwUYQU_DO0iNW9yrcHS4c7aXbGV_x5hE8rpEupFrS5ItLSUE9lpM2ICV7rJRVGJ2ru_o6QgwWVIGeF48DATj_Tp1R0HFwzsPMQBJ6LYVUXvY00v_IzP6Fym6CbLjrzP8FH16GmjrA1uK5XDQHivaK1yLxkpDAXdINH3gonN-ppcAtzHAOA_Rd-NwmZ13gg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5ef99e9cca.mp4?token=Uu1wkSidObX_JY5i0_RLNH1zH5J8-npeuXYUArVABiDCi8ovxeoyUQkA7JHAmMir7y76yT_EioWZPSq0i79_E4QterDyCD7sKkzMAJ5GeaDBBq0lQnZJ8KgXm1XKerycPpovnlaEHsupcVExmrKznOpYmwUYQU_DO0iNW9yrcHS4c7aXbGV_x5hE8rpEupFrS5ItLSUE9lpM2ICV7rJRVGJ2ru_o6QgwWVIGeF48DATj_Tp1R0HFwzsPMQBJ6LYVUXvY00v_IzP6Fym6CbLjrzP8FH16GmjrA1uK5XDQHivaK1yLxkpDAXdINH3gonN-ppcAtzHAOA_Rd-NwmZ13gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💣
گوگل مجموعه مهارت‌های خود را برای تولید رابط‌های وب مدرن منتشر کرد ، بهترین شیوه‌ها را مستقیماً در زمینه عامل هوش مصنوعی شما پیاده‌سازی می‌کند.
Modern Web Guidance
دیگر خبری از APIهای منسوخ و طراحی‌های قدیمی UI که شبکه‌های عصبی روی آن‌ها آموزش دیده‌اند نیست. درون این مجموعه بیش از ۱۰۰ مهارت به‌روز و تأیید شده توسط کارشناسان وجود دارد. با Claude Code، Cursor و Antigravity کار می‌کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5316" target="_blank">📅 18:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سری بعد روش
شکن + نتلیفای + ورکر کلادفلیر  + ورسل + vps خارج رو میزارم
بدون قطعی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5315" target="_blank">📅 17:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">cloudflare_netlify_bridge_V1.3.7.zip</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5314" target="_blank">📅 16:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA Channel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">cloudflare_netlify_bridge_V1.3.7.zip</div>
  <div class="tg-doc-extra">12.5 KB</div>
</div>
<a href="https://t.me/archivetell/5313" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل پروژه
👋
پروژه هنوز توی مرحله تست هست.
حتما قبل از انجام هر کاری دوتا فایل آموزشی رو به طور کامل بخونید.
توضیحات تکمیلی در پست های بعدی...
نکته: از اونجایی که پروژه در مرحله تست هست، ممکنه هر چند ساعت یک بار فایل پروژه آپدیت بشه، پس حتما از آخرین نسخه پروژه استفاده کنید.
وضعیت فعلی: آپدیت شده.
✅</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5313" target="_blank">📅 16:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">میتود جدید اومده
شکن + نتلیفای + ورکر + VPS خارج xhttp relay
خیلی خوبه یکم انجامش سخته ولی میگن سخت تر بن میشه
تست کردم اوگی بود میزارمش
👇
👇
👇
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5312" target="_blank">📅 16:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
یه خبر خوب برای کسایی که ویندسکرایب اشتراک پرو دارن🫪
دیشب با ادمین بخش تکنیکال ویندسکرایب در دیسکورد صحبت کردم که نسخه نهایی کی اماده میشه؟
گفتن نسخه جدید بتای ویندسکرایب تا کمتر از ۱۰ روز دیگه رونمایی میشه
هر زمان که فایل بتا رو برام بفرسته  همینجا داخل چنل براتون بصورت اختصاصی میزارم
❤️
با متد جدید تست گرفته شده کاملا موفقیت امیز بوده و گفته شده وصل میشه
😁
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5311" target="_blank">📅 16:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbsLAN-gEi3WA6JHuo5Yoyveu-yIQBJEClP2pdWVdSdJ7aRrXHcYEi5Ny2KMa6fi8QZrWb9MITkn9AE8LvtUbSPe8xvZfvGG5f9ohgObSuS1drYgDMJctZRpQfx8U_jExbAPBsOOOXeazRT2NPYEeI-b6BQb_eIDSuQrUm6uyYj_BP1dSdfx1sBqW_LE-mlzz5zG_N7uE4Qm4AJHEW6czFxW8WO8uF-It__mppcUb5xPE1ucm_WXX5GB2PE89HQ4YyKO8Tyzklvuw0G3L0H37k5c-K6ja72ZtkyWhwQxCss2rO1kpHSt_f04oXmDB6LRWYYgH0am51IZvA1BuOVf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://play2go.cloud https://aeza.net مقایسه پلن های پلی 2 گو و آئزا</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/archivetell/5310" target="_blank">📅 14:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L942M7qnQN-7TP1PmIs5pFdyXa-lscvpp0lpML498Tf-rVantQxAAlx65JwbVKRxgCt0DA7NcmmUoLI9PQ0NEsiZp9zPBCnkqEH3krH9V6--LXZ1dax1v_V8lEoonyv8PkFOQgy2SjanYExFSMryOPBetg1H_03XhNq6dQFv30Dli7oMsY7oU_Bg_NqpZZ4iGZeppJu2pGxCtRRdL9B6WANUPHq47uukMDn5WLamUHiyt0qX7qL5_it1h4hAyabb5pRVmdbV1UTIG847leSP1KaReq1UNy2kQwWmYLR4_LM1As62dSNHfvWj24q3lHKM4k7CMbSavvuSOdpXLt9Q3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
در مورد سرور (VPS) برای پروژه‌ها  ---  رفقا شب بخیر!
✋
خیلی‌ها توی دایرکت می‌پرسیدید برای راه‌اندازی پروژه‌هایی مثل GooseRelayVPN یا متودهای تونلینگِ جدید، الان چه سروری بگیریم که هم قیمت‌اش معقول باشه و هم موقع کار اذیت نکنه؟  راستش من خودم این مدت پلن‌های…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5309" target="_blank">📅 14:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOi_ub6GpOs2Sa8Wu0O74RUIDtIuYaxO3RbsF_GKSxMSfOnrFq9kuS0llXN7f-kVS9FRuGEfioi4E1bUOiiCwSVcSoPBxYsgwmab3m6XbTdxK5Zhx8sDDLurLyaQbEtU3nN3kJB1qMoffLi8-S65OSKH9hyy_CnZvhZd9OI-VE9Xw1BP8N7KTfLWDehDmxUhDiftpfO-lp5YFGvBGAZYTYwMcpnQPv8oBEBvGuiqE8CdRxiArRvFySgsuBjhy6fW1TY5lvXTpJoirMo1OjAmEn-cgxaQd2DNvKCy_3dpTnSk_9mTB3TBd4hldnW68YWdOrjqLmsHXD1MSd7_Ethejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
در مورد سرور (VPS) برای پروژه‌ها  ---  رفقا شب بخیر!
✋
خیلی‌ها توی دایرکت می‌پرسیدید برای راه‌اندازی پروژه‌هایی مثل GooseRelayVPN یا متودهای تونلینگِ جدید، الان چه سروری بگیریم که هم قیمت‌اش معقول باشه و هم موقع کار اذیت نکنه؟  راستش من خودم این مدت پلن‌های…</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5308" target="_blank">📅 14:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ربات هوش مصنوعی Claude رایگان
@bs_cluade_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5307" target="_blank">📅 14:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">2.17.35.217
2.17.35.40
2.17.35.24
2.17.100.234
2.17.97.137
2.17.106.118
2.17.35.163
2.17.106.137
2.16.53.57
2.16.53.65
شیر و خورشید ایرانسل ، همراه اول و سامانتل
کلاینت اندروید
کلاینت ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/5306" target="_blank">📅 13:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تا یه مدت پیش همینا نمیدونستن متد دی ان اس چیه
😁</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5305" target="_blank">📅 12:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBreak The Barriers</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQaONbyZCOhCZUUuEmBamJ_GN-EW14_FgDXkygFY_rz4oEDfakGxfqsPMoKAe6oSbcFKPLdKvjWYaW5k7XeHffthcP-quG2mibay5fodB8ZAY7PBG5Fn68_MVnAttSI6NbeaQTqhCPJ4gYfhQWTzGBYBAEIWOyDXyqg8k1UkSVdmrjONpIquIxB1AINNi-xsPrc9OneOeILgfuGkAsaFdZk2S_UxbrTJF_wtSY9WS8IlQU1MdPlaQdIrC3Y060kbKV9_WbTYiHawlp6-7R3eUWl2qsTHITJA5MK2feEqosY7gj7-Cu-pWIANaZyLT9SmwsN5A1OYySLuy1kGgwOpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسی که هیچ هزینه‌ای نداده و فقط متد بقیه رو منتشر می‌کنه، به کسی که صدها دلار برای اینترنت رایگان مردم هزینه کرده میگه «احمق»، «مزخرف» و «پولکی».
در این حدود ٣ ماه قطعی من حدود ٣٠٠ دلار هزینه بابت سرورهام دادم.
سرور و اتصال رایگان، با توییت و فحش تأمین مالی نمیشه.
بعضیا فقط بلدن حرف بزنن، نه اینکه بار واقعی چیزی رو به دوش بکشن.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5304" target="_blank">📅 12:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خیلیا این چند روز تو دایرکت کانال پیام دادن که اپراتورا خیلی بیشتر از حجم مصرفی از بسته اینترنت کم میکنن..  هیچ جوره جلوی دسترسی مردم رو نمیتونید بگیرید ، اینقدر زور نزنید
😁</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/5303" target="_blank">📅 12:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خیلیا این چند روز تو دایرکت کانال پیام دادن که اپراتورا خیلی بیشتر از حجم مصرفی از بسته اینترنت کم میکنن..
هیچ جوره جلوی دسترسی مردم رو نمیتونید بگیرید ، اینقدر زور نزنید
😁</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5302" target="_blank">📅 11:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDsk8-m9_6t4cMfeD9wmoS52zvGp2IaYkR0mZd156R686MuI7H_8Nmr23ig-di5As6N91Ts_skqS7V3XdhRxeyW5___3uKJcZQXveFiKgBURv2JUI8nAjVCg9GMbf7pfIwkLP743NZJ4mENdjxp9WnqSAETrdGr_r8ikU_k1F1Z3oxTcS-B7XNRnPv35MY0_QePL2rjW9u2T2ILZPOttu-iWpQ1NZeZ14kGYCuJDC5oWGVLuJGgaj0XTkcY8u4EREuyAFAa6B5EKJHrMQlpUx7O-NUKPSDVjW2Eu2oN5-5rhDx8AazQcPKy8u98nG0fvB3WDyberYCwAcJ8n6MGusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KL0vIFwM2iCQqhGfOex86eoq6VtDCP9QYQbWX2r2ZhwP5q4QqMFX4kERb-jkAwNV-0-mU0YOXpKU1Jdbu1_N0Q2Vq0GEKTjE51a2kOKM7rdztUPRGkGry9DCF4BwcClq5RffXjAEIZYspmUSOQ3HuS_QZspz3jw9n_6ah9T1hZ0aNCLGYfdrXBFrp2bSMzl4eO0_ZfVf0czLaSeCenfRmtSwlhsf6bi98_taQdLy89d0s38lmcCf1fnJaTsTJPZxtt5lpsdS3omi1jMTXNb0HZk2Z4l_uHlgI5E1i7i8KYvPHPd_mxIFc_2Xx8c21ztv5WpPYx3ZcS956yLpVik5iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه میخواین ترافیک از جایی کم رد و بدل بشه اینجا برین
تو اندروید های بالای ۱۳ هست این اپشن
مثلا نتلیفای که بن نشه
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5300" target="_blank">📅 11:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">46.38.137.156 81.12.32.136 تو sni spoof با hcaptcha.com بزنید جفتشون کار میدن</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5299" target="_blank">📅 11:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
46.38.137.156
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
chat.deepseek.com
"
}</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5298" target="_blank">📅 11:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانفیگ اسپوف
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?allowInsecure=1&encryption=none&host=sni.111000.indevs.in&path=%2F%3FTelegram%D9%8B+%40ProxyVPN11&security=tls&sni=sni.111000.indevs.in&type=ws#%DB%B1
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?allowInsecure=1&encryption=none&host=sni.latonyamadeline.ndjp.net&path=%2F%3Fhttps%3A%2F%2Ft.me%2FProxyVPN11%F0%9F%87%A8%F0%9F%87%B3%3D&security=tls&sni=sni.latonyamadeline.ndjp.net&type=ws#%DB%B2
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B3
trojan://1710442808@127.0.0.1:40443?allowInsecure=1&host=subb.nrshop198.workers.dev&path=%2F&sni=subb.nrshop198.workers.dev&type=ws#%DB%B4
trojan://humanity@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B5
trojan://humanity@0.0.0.0:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B6
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.multiplydose.com&path=%2Fassignment&sni=www.multiplydose.com&type=ws#%DB%B7
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#%DB%B8
trojan://humanity@127.0.0.1:40443?allowInsecure=1&path=%2Fassignment&sni=www.multiplydose.com&type=ws#%DB%B9
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B1%DB%B0</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5297" target="_blank">📅 10:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مخابرات | sni spoofing    hcaptcha.com  46.38.137.156</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5296" target="_blank">📅 10:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مخابرات | sni spoofing
hcaptcha.com
46.38.137.156</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5295" target="_blank">📅 10:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">46.38.137.156
81.12.32.136
تو sni spoof با
hcaptcha.com
بزنید جفتشون کار میدن</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5294" target="_blank">📅 10:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">2.19.126.205
23.216.77.172
2.16.6.219
23.213.161.104
23.48.23.162
23.222.250.244
184.25.52.67
95.101.111.141
2.22.89.33
2.16.55.15
95.101.137.74
2.20.168.195
23.218.225.17
23.48.23.171
96.16.122.153
23.3.89.123
2.16.220.194
95.101.171.159
2.21.2.65
23.11.206.114
2.22.151.183
95.101.29.12
2.21.240.145
2.16.245.170
95.101.29.23
95.101.137.201
23.44.203.191
23.48.23.194
2.22.31.99
96.16.53.156
2.19.126.92
23.216.77.70
2.16.245.177
2.16.55.45
23.3.89.97
2.20.168.16
23.218.225.41
2.16.154.104
2.19.198.75
23.44.203.205
88.221.169.185
185.200.232.8
2.22.89.195
96.16.86.206
185.200.232.65
23.48.224.82
23.219.36.112
2.16.6.206
23.55.244.243
2.18.20.57
23.42.205.29
104.111.202.22
شیر و خورشید شاتل ، پارس آنلاین ، سامانتل و ایرانسل
کلاینت اندروید
کلاینت ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5293" target="_blank">📅 09:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ربات ویرایش mp3 و پیام صوتی
@mp3_Service_Bot
🎤
تبدیل تِرَک ها به صدا
🏷
ویرایش برچسب‌ها (عنوان، هنرمند)
🖼
افزودن کاور
🔊
صدای 8D
🎚
مسترینگ (تمیز، بلند، صدای استودیو)
🪄
افکت‌های بیس و ریورب
🔄
تبدیل به MP3، WAV، FLAC، OGG، AAC
📦
پردازش دسته‌ای چندین فایل
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5292" target="_blank">📅 09:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آیدی عددی رو بفرسید این ربات و اطلاعاتش در بیارید
@fustating_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5291" target="_blank">📅 09:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیدا کردن افراد با آیدی عددی با این فرمت :
tg://openmessage?user_id=
بعد از = آیدی عددی بذارید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5290" target="_blank">📅 09:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سامانتل شیر و خورشید سرعت فضایی
CDN edge IPs :
184.24.77.42
184.25.28.31
184.28.165.4
184.51.252.4
184.86.251.12
184.86.251.27
184.25.52.200
184.28.230.87
184.30.150.142
184.51.252.36
184.51.252.38
185.200.232.40
185.200.232.41
185.200.232.42
185.200.232.43
185.200.232.49
185.200.232.50
184.51.252.152
184.51.252.157
184.86.103.210
184.51.252.135
CDN SNI hostname:
snapp.ir
Beast Mode : روشن
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5289" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رایتل شیر و خورشید
142.54.178.211
5.144.129.174
80.191.243.226
2.16.53.50
79.175.169.59
95.38.201.199
5.160.13.85
2.23.170.80
193.148.67.117
2.16.53.11
کلاینت اندروید
کلاینت ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5288" target="_blank">📅 08:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">همراه اول شیر و خورشید
184.86.251.27
184.51.252.36
185.200.232.50
کلاینت اندروید
کلاینت ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5287" target="_blank">📅 08:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0003b579.mp4?token=dbKnbyvZLfNmLIil7JRzavfpwTxUJTRs4Nlxfs19k_ZJ9AqE84Co7RicA0JsZQ5tjHoHygYghjK06fEl-3on7L7PCoymAG_iWD0Pw3WMPzkLRa5miBkTzZQgn62CgvEZMsgi8RMzi_xkFwtMNDvJcARx74-NWDjJFH0jQ9sgZEy8prgZ7HQzC_WbdMCmL355yZYfatADAEl6YcvAbeGqCklocJr-K6GLDmTMyWjITPK78_24sPr4ll1FhV_eMGX68Ntbt8WuXXuWp-PwqL-EzQro0PZGLH-vl8IVRSe4CvkQSZQuUphtEkAM0ApK3GS1-fTcMtkylDPGqfUggs4ssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0003b579.mp4?token=dbKnbyvZLfNmLIil7JRzavfpwTxUJTRs4Nlxfs19k_ZJ9AqE84Co7RicA0JsZQ5tjHoHygYghjK06fEl-3on7L7PCoymAG_iWD0Pw3WMPzkLRa5miBkTzZQgn62CgvEZMsgi8RMzi_xkFwtMNDvJcARx74-NWDjJFH0jQ9sgZEy8prgZ7HQzC_WbdMCmL355yZYfatADAEl6YcvAbeGqCklocJr-K6GLDmTMyWjITPK78_24sPr4ll1FhV_eMGX68Ntbt8WuXXuWp-PwqL-EzQro0PZGLH-vl8IVRSe4CvkQSZQuUphtEkAM0ApK3GS1-fTcMtkylDPGqfUggs4ssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5285" target="_blank">📅 02:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b443b9a9.mp4?token=XB6n-qfGM3s55-bEM-DOOAhyX8zF5aPDVwM4J_4kqdYdgXveMnKhnSfRmqxrGiORdgXH634N-3i-Fkkqt63q1EVejt9z3oVAuKwRwZpHEGISVt24v1ZzBI_fdOi5ApKKlTgGx3OQpD1kFxok7WrDj8KCxmPX-f-9TT0yoY1Da1L_tYET8Jk09FFXXjS7y7XisIJ8o9qBevIs1Ql3QeDaemD0BMS5k_bAfANyLQ6LjWdg0T5gN2uOV7Pp6I-zT8x8LhiAuCouAlAvlwt1Z38MchzNTrv7gcLU1KnAxdrGBOldcLpIDrsoVI6IWP61JFRYJI9vrCJ_yN7vsY5BXzfqlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b443b9a9.mp4?token=XB6n-qfGM3s55-bEM-DOOAhyX8zF5aPDVwM4J_4kqdYdgXveMnKhnSfRmqxrGiORdgXH634N-3i-Fkkqt63q1EVejt9z3oVAuKwRwZpHEGISVt24v1ZzBI_fdOi5ApKKlTgGx3OQpD1kFxok7WrDj8KCxmPX-f-9TT0yoY1Da1L_tYET8Jk09FFXXjS7y7XisIJ8o9qBevIs1Ql3QeDaemD0BMS5k_bAfANyLQ6LjWdg0T5gN2uOV7Pp6I-zT8x8LhiAuCouAlAvlwt1Z38MchzNTrv7gcLU1KnAxdrGBOldcLpIDrsoVI6IWP61JFRYJI9vrCJ_yN7vsY5BXzfqlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5284" target="_blank">📅 02:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoTnNUnxLIJA3LSKDcL3JhNyZjzSXcoF3igwppPaZp-28wbpYu4uSDpe9pFqohZ8PsXhKmyvvOHgBlxh-d7CCedG_9QTsP97KLDQgEBxKcYjvUDV5baOulxFk3DE6-yo4zj99ABhQmpSEaoiHXAI9YjXsZhYphMyrFoMNiNVwXz4cTtZIdv7LzqVsKoMRKOBYa7b8x86fJ-wQB04fd900BeKIRdwpJvIFFzbK73v8lrXBG_Y8aywLrJdLpNjayIypXCHhTccxSkEy2-_2VpetDhPEuh8PnUrHmtu8Uua2irRGiDrHoE7tmzrgV6i7PE5n4Pxn7w2jQ9Y__Go73lwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
در مورد سرور (VPS) برای پروژه‌ها  ---  رفقا شب بخیر!
✋
خیلی‌ها توی دایرکت می‌پرسیدید برای راه‌اندازی پروژه‌هایی مثل GooseRelayVPN یا متودهای تونلینگِ جدید، الان چه سروری بگیریم که هم قیمت‌اش معقول باشه و هم موقع کار اذیت نکنه؟  راستش من خودم این مدت پلن‌های…</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/archivetell/5283" target="_blank">📅 23:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
معرفی GooseRelayVPN: کلاینت اختصاصی و قدرتمند اندروید برای متد رله گوگل  ---  اگر از متدهای رله‌ی گوگل (مثل MasterHttpRelayVPN یا مشابه اون) استفاده می‌کنید و دنبال یک اپلیکیشن اندرویدی هستید که هم ظاهرِ تمیز و مدرنی داشته باشه و هم مدیریتِ کانکشن‌ها رو…</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5282" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
معرفی GooseRelayVPN: کلاینت اختصاصی و قدرتمند اندروید برای متد رله گوگل
---
اگر از متدهای رله‌ی گوگل (مثل MasterHttpRelayVPN یا مشابه اون) استفاده می‌کنید و دنبال یک اپلیکیشن اندرویدی هستید که هم ظاهرِ تمیز و مدرنی داشته باشه و هم مدیریتِ کانکشن‌ها رو براتون به صورت خودکار (VPN Service) انجام بده،
GooseRelayVPN
دقیقاً همون چیزیه که نیاز دارید.
💡
چرا باید از GooseRelayVPN استفاده کنیم؟
بزرگترین مشکلِ کار با این متدها روی اندروید، محدودیت‌های مرورگر و نیاز به تنظیماتِ دستیِ پروکسی بود. این اپلیکیشن با استفاده از قابلیت
VpnService
سیستم‌عامل اندروید، تمامِ ترافیکِ گوشی (یا اپلیکیشن‌های انتخابی شما) رو به صورت خودکار از تونلِ رمزنگاری‌شده‌ی گوگل عبور میده.
✨
ویژگی‌های کلیدی این کلاینت:
🔸
پشتیبانی از VPN Service:
نیازی به تنظیم پروکسی در مرورگر نیست؛ کلِ گوشی یا اپ‌های منتخب شما به صورت VPN متصل میشن.
🔸
داشبورد حرفه‌ای:
مانیتورینگِ زنده وضعیت اتصال، پینگ و لاگ‌های سیستمی برای عیب‌یابی سریع.
🔸
پشتیبانی از پروتکل‌های هسته‌ی GooseRelay:
این اپلیکیشن از هسته‌ی بهینه شده‌ی این پروژه استفاده می‌کنه که پایداری بسیار بالایی روی اینترنتِ محدود داره.
🔸
مدیریت پروفایل‌ها:
می‌تونید چندین کانفیگ مختلف رو وارد کنید و به راحتی بین اون‌ها سوییچ کنید.
🔸
وارد/خروجی گرفتن با فرمت JSON:
مدیریت کانفیگ‌ها بسیار راحته و می‌تونید اون‌ها رو بین گوشی‌های مختلف جابجا کنید.
---
🛠
چطور راه اندازی کنیم؟
۱.
پیش‌نیاز سرور:
ابتدا باید هسته‌ی اصلی (GooseRelay) روی سرور لینوکسی شما نصب باشه و Deployment ID و کلید امنیتی (Tunnel Key) رو داشته باشید.
۲.
تنظیم اپلیکیشن:
- فایل APK رو نصب کنید.
- یک پروفایل جدید بسازید.
- مقادیر
script_keys
(لینک‌های دیپلوی شده) و
tunnel_key
رو دقیقاً مشابه سرورتون وارد کنید.
۳.
اتصال:
بعد از ذخیره، روی پروفایل ضربه بزنید تا VPN فعال بشه. (در اولین اجرا، اندروید اجازه دسترسی به VPN رو می‌خواد که باید تأیید کنید).
📥
لینک گیت‌هاب و دانلود:
🔗
https://github.com/Hidden-Node/GooseRelayVPN-AndroidClient
📌
نکته فنی:
اگر موقع اتصال، وضعیت روی "Preparing" گیر کرد، حتماً بخش
Logs
توی خودِ اپلیکیشن رو چک کنید. اونجا دقیقاً بهتون میگه مشکل از کجاست (مثلاً اشتباه وارد کردنِ Tunnel Key).
📌
#معرفی_ابزار
#فیلترشکن
#اندروید
#گوگل_رله
#نت_ملی
#GooseRelayVPN
#VPN
#Android
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5281" target="_blank">📅 22:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHTmFoAYThzwxo-o9HD1KW5VpaewxsG9Hcj9P5UlZ82hb5zbG_B7ZD3XEEmWm-vb6IYVclHDh-1ZKx6mjR2zBvVuq2M3X4iYoQTPHsCSwY6N25b2YE1LKNSfQU6FqN_nNSbqzNzqBuC8jIWQs3lVDkxB5sxmOwItFsv2t9rY9GQ54n2e937CjKHTdW5EPU74Ih27RUfdNPZHpdu6QCEkTcHkVOAkxc9J4Y-fU-4ymrKtmsD_fGqnOKuzc2Gt9mwPf7G1Na1skO9oMfDc6_3tx3q30IW2LhEiChTbwvjgSNIV_QLDHEA3eznI9qGedC3BNRkdIbZTRZPQj_0Qxh3agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
FileShare یه ابزار ساده برای اشتراک‌گذاری فایل توی شبکه محلیه.
با این برنامه می‌تونی فایل‌ها رو روی سیستم خودت آپلود کنی و از یه دستگاه دیگه داخل همون شبکه، خیلی راحت دانلودشون کنی.
✅
کارش اینه:
- فایل را می‌فرستی داخل ابزار
- برنامه فایل را ذخیره می‌کند
- لینک دانلود و لیست فایل‌ها روی دستگاه‌های دیگر هم در دسترس است
✨
این ابزار کار را برای انتقال فایل بین دو دستگاه خیلی راحت‌تر می‌کند، چون نیازی به فلش، کابل یا نرم‌افزار جانبی نداری.
🔐
درباره فایروال:
اگر دو دستگاه داخل یک شبکه باشند، معمولاً کافی است پورت برنامه باز باشد. در بعضی سیستم‌ها ممکن است فایروال دسترسی را ببندد، پس اگر اتصال برقرار نشد فقط باید اجازه دسترسی به برنامه یا پورت 8887 را بدهی؛ معمولاً لازم نیست فایروال را کامل خاموش کنی.
لینک دانلود داخلی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5280" target="_blank">📅 21:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">exventa.io
پلتفرم مدرن برای ارزهای دیجیتال که از هوش مصنوعی برای ارائه استراتژی‌های معاملاتی استفاده میکنه
- قابلیت‌ها: مشاهده زنده عملکرد، مدیریت امن موجودی و ربات‌های خودکار برای کاربران بی تجربه.
- هدف: ساده‌سازی معامله برای کاربران عادی و ارائه ابزارهای پیشرفته بدون نیاز به دانش فنی.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/5279" target="_blank">📅 21:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لینک داخلی آموزش
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5278" target="_blank">📅 20:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">scannerv2.zip</div>
  <div class="tg-doc-extra">12.4 KB</div>
</div>
<a href="https://t.me/archivetell/5277" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
معرفی نسخه جدید CDN IP Scanner  نسخه جدید CDN IP Scanner منتشر شد؛ یک ابزار سبک، سریع و کاربردی برای اسکن IP، CIDR و لیست‌های CDN با امکانات حرفه‌ای‌تر و backend پایدارتر.
✅
قابلیت‌های ورودی:  * IP تکی * لیست چندخطی IP * CIDR * رنج IP * فایل txt شامل IP…</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5277" target="_blank">📅 20:37 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
