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
<img src="https://cdn4.telesco.pe/file/lzhQ_4eMJZw__njfqTQG2rimpYsP1Bu78cX6dcZyk3VNgGLJ9AB_dihYAJrtsCOYSlXpszgr4xeSHXrHZ3axIjQVlXWKqaLwoDEl7EfJ80djd7kLtKZK9oASLIN8SUb7puKXc7JAly3c9TWMdhxHIyLtBWdL82MSeM77nbOH3X_f6gShBTXkzVwzEipZFLSs4HoVJzHlz6A6z9exjVofu5s774dUFwMCAr_HopMNTjRtOZXCc7lOsvgYKiD0WNY5l9_JtS1YP6gIYBh6EfmQiboyOebTczD5W06FM6IAVnNiCAyqOtzSQbcRLDI3Us2yxrctgs8h7etlD9JyOoNRkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 7.44K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 17:08:29</div>
<hr>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚀
معرفی اپلیکیشن TheFeed برای کاربران iOS (آیفون/آیپد)
---
رفقای آیفون‌دار
می‌دونیم که پیدا کردن ابزارهای دور زدن فیلترینگ برای iOS همیشه سخت‌تر از اندرویده. امروز یه کلاینت جدید و جذاب به اسم TheFeed رو بهتون معرفی می‌کنیم که فعلاً تو مرحله تست (بتا) قرار داره و می‌تونید از طریق TestFlight اپل روی گوشیتون نصبش کنید.
🛠
آموزش نصب و راه‌اندازی (فقط در ۳ قدم):
1️⃣
قدم اول (نصب پیش‌نیاز): ابتدا باید برنامه رسمی TestFlight رو از App Store سرچ و روی گوشیتون نصب کنید (این برنامه مال خود اپله و برای نصب نسخه‌های آزمایشیِ برنامه‌ها استفاده می‌شه).
2️⃣
قدم دوم (نصب اپلیکیشن): روی لینک دعوتِ زیر کلیک کنید تا صفحه TheFeed تو برنامه تست‌فلایت براتون باز بشه. بعد روی دکمه Accept و سپس Install بزنید تا برنامه نصب بشه.
3️⃣
قدم سوم (دریافت کانفیگ): بعد از نصب، برنامه خالیه و برای اتصال نیاز به کانفیگ دارید. سازنده‌های این پروژه یه کانال تلگرامی مجزا زدن که کانفیگ‌های مخصوص TheFeed رو اونجا قرار می‌دن. کافیه کانفیگ‌ها رو از اونجا کپی و تو برنامه وارد کنید.
📥
لینک‌های مورد نیاز:
🔗
لینک دعوت و نصب TheFeed (از طریق TestFlight):
🌐
https://testflight.apple.com/join/J6bfxDdZ
⚙️
کانال دریافت کانفیگ‌های مخصوص برنامه:
🆔
@thefeedconfig
📢
کانال اصلی پروژه (برای پیگیری اخبار و آپدیت‌ها):
🆔
@networkti
📌
#معرفی_ابزار
#آیفون
#آی_او_اس
#نت_ملی
#فیلترشکن
#TheFeed
#iOS
#TestFlight
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/5141" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آپلودر بدون نیاز به ثبت نام
https://guardts.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/5140" target="_blank">📅 13:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/5139" target="_blank">📅 12:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCheshm E Oghab - چشم عقاب</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CheshmehOghab-Android.apk</div>
  <div class="tg-doc-extra">26.1 MB</div>
</div>
<a href="https://t.me/archivetell/5138" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود مستقیم اپلیکیشن چشم عقاب
یا از طریق:
-
گوگل درایو
-
گیت‌هاب
-
گوگل پلی
میتونید این آدرس‌هارو با دوستان خود به اشتراک بگذارید از اونجایی که برخی از سرویس‌ها رو بعضی از آی‌اس‌پی ها باز هستند.
@CheshmehOghabApp</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/5138" target="_blank">📅 12:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
معرفی اپلیکیشن «چشم عقاب» (Eagle Eye): دریافت اخبار و کانفیگ VPN، کاملاً آفلاین و از طریق ماهواره!
📡
---  امروز با یه شاهکارِ تکنولوژی و انقلابی اومدیم که دقیقاً برای روزهای قطعیِ مطلق اینترنت (نت ملی) طراحی شده.   وقتی اینترنت کاملاً قطع می‌شه، اپلیکیشن…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/5137" target="_blank">📅 12:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
معرفی اپلیکیشن «چشم عقاب» (Eagle Eye): دریافت اخبار و کانفیگ VPN، کاملاً آفلاین و از طریق ماهواره!
📡
---
امروز با یه شاهکارِ تکنولوژی و انقلابی اومدیم که دقیقاً برای روزهای قطعیِ مطلق اینترنت (نت ملی) طراحی شده.
وقتی اینترنت کاملاً قطع می‌شه، اپلیکیشن «چشم عقاب» بهتون اجازه می‌ده اخبار، توییت‌ها، پیام‌های تلگرامی و مهم‌تر از همه،
کانفیگ‌های تازه و سالمِ VPN
رو مستقیماً از طریق دیش ماهواره و بدون نیاز به سیم‌کارت یا حتی یک بایت اینترنت، روی گوشیتون دریافت کنید!
🤯
🔥
مکانیزم کار چطوره؟
خیلی ساده‌ست! شبکه مورد نظر به جای پخش فیلم، یک‌سری QR Code رو تند و پشت‌سرهم روی صفحه تلویزیون پخش می‌کنه. شما دوربین گوشی رو می‌گیرید سمت تلویزیون و تو کمتر از ۲۵ ثانیه، تمام اطلاعات به صورت آفلاین وارد گوشی شما می‌شه!
✨
ویژگی‌های بی‌نظیر این اپلیکیشن:
🔸
۱۰۰٪ آفلاین و امن: این برنامه اصلاً مجوز (Permission) دسترسی به اینترنت نداره و فقط به دوربین دسترسی داره. محاله بتونه دیتایی ارسال یا دریافت کنه.
🔸
کانفیگ‌های داغِ VPN: دریافت سرورهای V2Ray، Shadowsocks و WireGuard از ماهواره؛ تا به محض اینکه نت وصل شد، سریعاً فیلترینگ رو دور بزنید.
🔸
رمزنگاری و امضای دیجیتال: تمام محتواها با الگوریتم (Ed25519) تایید می‌شن تا کسی نتونه دیتای فیک یا مخرب به خوردتون بده. اطلاعات هم روی گوشی با AES-256 رمزنگاری می‌شن.
🔸
ضد اسکرین‌شات: برای امنیت بیشتر شما، امکان اسکرین‌شات و ضبط صفحه بسته شده.
🔸
دریافت با وجود خطا: حتی اگه ۳۰ درصد از QR کدها رو به خاطر پرش تصویر از دست بدید، باز هم اطلاعات به صورت کامل بازسازی می‌شن!
📡
مشخصات شبکه در ماهواره:
ماهواره: ترکمن‌عالم / یاهست (TurkmenÄlem 52°E)
فرکانس: 10762
پلاریزاسیون: عمودی (V)
سیمبول ریت: 27500
📥
لینک‌های دانلود برنامه:
📱
دانلود مستقیم از گوگل‌پلی:
🔗
https://play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🌐
دانلود مستقیم فایل APK (بدون نیاز به گوگل‌پلی/فیلترشکن):
🔗
https://cheshmehoghab.app
(همچنین کانال رسمی خود برنامه برای دریافت آپدیت‌ها:
@CheshmehOghabApp
)
📌
#معرفی_اپلیکیشن
#چشم_عقاب
#آفلاین
#بدون_اینترنت
#ماهواره
#نت_ملی
#کانفیگ
#VPN
#Eagle_Eye
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/5136" target="_blank">📅 12:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یوتیوب داخلی
https://zintube.ir
همه ویدئو ها توش نیست ولی بهتر از هیچیه
ادمینایی که میخوان کلیپ آموزشی درست کنن ، به خاطر راحتی ممبرا از این استفاده کنن تو این شرایط
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/5135" target="_blank">📅 12:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">لینک داخلی شیر و خورشید
دانلود
Pass :
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/5134" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اگه نتونستید به تلگرام وصل بشید وارد سایت زیر بشید
https://market.qeshmyar.com/telegram/
بعد تو قسمت سرچ ، آیدی کانال مورد نظرتون رو بدون @ وارد کنید و بعد بارگذاری رو بزنید ، مطالب کانال رو میاره
مثلا کانال ما سرچ کنید
archivetell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/5133" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لینک گروه بچه های قشنگ آرشیو تل
😁
https://t.me/+xes6CqzcVcwwODFk</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5132" target="_blank">📅 11:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CDN_IP_Finder@ArchiveTell.html</div>
  <div class="tg-doc-extra">59.2 KB</div>
</div>
<a href="https://t.me/archivetell/5131" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5131" target="_blank">📅 10:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
معرفی کامل‌ترین اسکنر تحت وب برای پیدا کردن آی‌پی‌های تمیز (CDN IP Finder)
---
پیدا کردن آی‌پیِ تمیز برای متد «دامین فرانتینگ» (مثل برنامه شیر و خورشید) همیشه یکی از بزرگترین دغدغه‌ها بوده. امروز می‌خوایم یه ابزار به‌شدت خفن، ایرانی و اوپن‌سورس به اسم CDN IP Finder رو معرفی کنیم که این کار رو به ساده‌ترین شکل ممکن براتون انجام می‌ده.
🔥
چرا این اسکنر شاهکاره؟
چون کلاً روی یه فایل HTML سوار شده! یعنی بدون نیاز به سرور، ترموکس، پایتون یا هر پیش‌نیاز دیگه‌ای، مستقیم تو مرورگر گوشیتون اجرا می‌شه. ازونجایی که تست‌ها با اینترنت خودتون انجام می‌شه، نتایج ۱۰۰٪ برای اپراتور شما (ایرانسل، همراه اول، شاتل و...) دقیق و شخص‌سازی‌شده است.
✨
ویژگی‌های بی‌نظیر این ابزار:
🔸
پشتیبانی از ۴ غول بزرگ: قابلیت اسکن آی‌پی‌های Akamai، Google CDN، Amazon CloudFront و Azure.
🔸
تشخیص خودکار اینترنت: خودش می‌فهمه از چه اپراتوری استفاده می‌کنید و بر همون اساس تست می‌گیره.
🔸
داشبورد حرفه‌ای: بهتون نمودار پینگ، تاریخچه اسکن‌های قبلی و حتی QR کد (برای انتقال سریع آی‌پی‌ها به یه گوشی دیگه) می‌ده.
🔸
پیشنهاد SNI: دقیقاً بهتون می‌گه برای هر شبکه‌ای که اسکن کردید (مثلاً آکامای)، چه SNI ای رو باید تو برنامه وارد کنید.
🛠
آموزش استفاده سریع (تست با مرورگر):
1️⃣
اینترنت گوشی رو (بدون فیلترشکن) روشن کنید.
2️⃣
لینک نسخه تحت وب اسکنر رو (که پایین پست گذاشتیم) تو مرورگر باز کنید. (یا می‌تونید فایل index.html رو از گیت‌هاب دانلود و تو گوشی باز کنید).
3️⃣
شبکه‌ای که می‌خواید (مثلاً Akamai) رو انتخاب کنید و دکمه اسکن رو بزنید.
4️⃣
بعد از اتمام، آی‌پی‌های سبزرنگ رو با یک کلیک کپی کنید.
5️⃣
برید داخل برنامه «شیر و خورشید» ➔ تنظیمات ➔ بخش CDN Fronting. آی‌پی‌ها و SNI مربوطه‌اش رو وارد کنید و استارت بزنید!
🎉
(توجه: تو صفحه گیت‌هابِ پروژه، چندتا اسکریپت خفن هم برای اسکن از طریق سرور مجازی / لینوکس قرار داده شده که خوراکِ بچه‌های حرفه‌ای‌تریه که سرور دارن).
🔗
لینک مستقیم نسخه تحت وب (باز کردن بدون فیلترشکن):
🌐
https://htmlpreview.github.io/?https://github.com/hossein8360/cdn-ip-finder/blob/main/index.html
🔗
لینک صفحه گیت‌هاب پروژه (برای دانلود فایل‌ها و اسکریپت‌ها):
🌐
https://github.com/hossein8360/cdn-ip-finder
📌
#معرفی_ابزار
#اسکنر
#آی_پی
#آکامای
#شیر_و_خورشید
#نت_ملی
#CDN
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/5130" target="_blank">📅 10:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚀
لیست داغ آی‌پی‌های تمیز آکامای (تست‌شده روی ایرانسل)
---
رفقا سلام!
✋
یکی از ممبرهای گل و فعال کانال دست‌پر اومده و یه لیست تازه از آی‌پی‌های اسکن‌شده و تمیزِ آکامای (Akamai) رو برامون فرستاده که همین الان روی نت ایرانسل عالی جواب دادن.
💡
نکته طلایی (آموزش استفاده):
به گفته‌ی این رفیقمون، نیازی به هیچ کار عجیب و غریبی نیست! فقط کافیه تو برنامه‌تون (مثل کلاینت شیر و خورشید):
۱. گزینه Protocol رو روی حالت
cdn fronting
قرار بدید.
۲. آی‌پی‌های زیر رو کپی کنید و تو بخش
cdn ips
(یا کادر مربوط به آی‌پی) وارد کنید و استارت بزنید.
👇
لیست آی‌پی‌ها برای کپی سریع:
23.44.201.149
23.212.253.227
23.44.201.185
23.44.201.17
23.62.54.24
23.58.95.144
104.83.198.44
92.123.102.153
184.51.252.134
23.53.40.147
184.51.252.176
2.18.64.212
172.104.251.198
2.18.79.101
23.216.77.181
92.123.102.89
23.216.77.80
96.16.53.132
23.53.40.139
23.48.165.70
2.21.20.143
23.43.85.155
23.48.23.184
23.207.210.83
23.209.125.169
23.48.23.172
2.21.240.22
23.55.110.82
23.216.77.35
23.58.95.138
23.33.40.149
23.48.23.146
23.209.125.145
92.123.102.130
23.53.40.121
23.48.23.11
23.201.248.171
23.209.125.27
23.48.23.176
23.207.210.86
23.55.161.151
92.123.103.89
2.23.7.34
23.207.210.80
23.48.23.165
23.48.23.173
23.48.23.156
23.55.110.74
173.222.107.202
23.213.161.140
23.48.23.134
23.204.152.160
2.23.97.120
(دمِ ممبر خوبمون گرم بابت اسکن و اشتراک‌گذاری این لیست
🤍
)
📌
#آی_پی
#آکامای
#ایرانسل
#دامین_فرانتینگ
#شیر_و_خورشید
#بدون_فیلتر
#Akamai
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/5129" target="_blank">📅 10:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ربات های جست و جو در تلگرام
@en_SearchBot
@argo
@tgdb_search_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/5128" target="_blank">📅 10:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کانفیگ من کجاییی ،
کانفیگ پینگ پاییییین ،</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/5127" target="_blank">📅 09:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👾
لیست دانلود برنامه ها با نت ملی
1️⃣
WhiteDNS
1.4.0
(نسخه ی رسمی)
1️⃣
WhiteDNS
(Windows)
1.0.3
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
12.7.3
📱
Telegram
(رسمی)
12.7.3
📱
Telegram
(Windows)
12.7.2
💩
Whatsapp
2‌.26‌.17.‌72
💬
Instagram
v415.0.0.36.76
👑
ShiroKhorshid
2026.05.14
5️⃣
Mhrv Rs
v1.9.26
📱
MasterHttpRelayVPN
📱
TunnelX
v1.2.24
📶
Npv
123
📶
V2box
5.3.4
📶
V2rayTun
5.23.73
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
MasterDNS
HN 1.2.3
2️⃣
Masterdns
GG 1.1.0
📶
Windscribe
4.0
📶
Open vpn
3.71
📶
Open vpn
(Windows) 3.8.0.4528
8️⃣
Oghab
🤖
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/5126" target="_blank">📅 09:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">#اختصاصی
​یک ماه اشتراک رایگان Duolingo Super
​لینک :
https://www.duolingo.com/redeem
​
​کد:
UBERMDAYSABUP6M
​از دسترسی پرمیوم بدون تبلیغات لذت ببرید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/5125" target="_blank">📅 09:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">لینک لیست پخش اسپاتیفای را ارسال کنید تا فایل فشرده ZIP شامل تمامی قطعات، تگ‌های شناسایی (ID3) و تصویر جلد آلبوم دریافت کنید
@SpotifyDownloaderExdbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/5124" target="_blank">📅 09:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TxJ5zCDh9yFLXPbKNhenWzAKgm-SmCA8g0WRoG-3tCanzCNplBez9AViBZEnTQQJvcTE8P5N9fAxVUnn7pRfb0ltl56Ss3KV4IIn3gtxyZaqAHGjwnFc9CaqJkbbGO5oPrYEixYkFOCxRNOEkTbuYsdhtCqoU3UWGQSQRS7UtvdXHH26_IjKJX93kN1yUEugp203yogLJsvVV5aeAmzjOmDgl9S6KAUxqtW6bZvR87vP162ox01gztzTcY0Cf80BqyiTwdm8sQ_i5dPq2bdp04ERgAXUt1tsQxgDe_GtfTGHNqLQ2hTv8iBkdfXQrNz4UKk4obQdMqqR0QE_68T38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kM42SYIOdf7QulJ0KGHboOT_4rZNPFVuqZDwkJ9k4XXzldv69IXzetyWM7N0QmjrQXsWIiHsG7dyMcE6I0xY23xP8TgW0kwP6a_maTAKrQVu5_yJYCNBgtB_A6sP96vnw3WNM2aq4uejFSSrP45q-EcFBYIYTbcZVtJevTAKW-0ZEggr6w0bH5kE2JrX-BVV7LWd2FIkEEIiuIY-2H97d5nqj1EkZcYGFK2R8EbweKOMyfj99pPscovUacGC6oT1CDJaEUUKX1EImrIBDddg7Hii0pAm5W9HFuPz4nYQL-5wj7yG_DgCwM4Z494WiuQ5mdpNLm_zvPA5WZ64WnqsUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش اتصال بدون شکن با متود
🥒
🔹
مثل همیشه یه نتلیفای بسازید و پروژه رو دپلوی کنید
🔸
به جمینای این پرامپت رو بدید
Output exactly 25 raw domain names of old, obscure, and non-famous websites that are hosted on Amazon CDN (CloudFront), Cloudflare, or Netlify. Provide ONLY the list of domains, with each domain on a new line. Do not include any conversational filler, introductory text, numbers, or bullet points. Format the domains strictly without "http://", "https://", or "www." (e.g., example.com).
🔹
یه لیست میده بهتون یکیشو رندوم بردارید برید داخل دامنه پروژه نتلیفای ثبت کنید
🔸
نیاز به هیچ تاییدی نیست فقط باید ثبت بشه همین
🔺
اگه ارور
"
Another project is already using this domain
"
داد یعنی دامنه رو قبل شما یکی زده یه دامنه دیگه پیدا کنید
🔺
با این سایت
هم میتونید زیر دامنه های یه دامنه رو پیدا کنید اونا رو بزنید
🔹
وارد کانفیگ ساز بشید و با دامنه ای که ثبت کردید کانفیگ بسازید
🔸
اکثر سرور ها راه افتادن
🔹
در قسمت آیپی و sni هر دو این رو بزنید
104.198.14.52
🟢
کانفیگ بسازید و وصل
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/5120" target="_blank">📅 03:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚀
معرفی ابزار Skirk: دور زدن فیلترینگ با پوششِ گوگل درایو!
🤯
---
رفقا سلام!
✋
امروز می‌خوایم یه ابزار خفنِ اوپن‌سورس و ایرانی رو معرفی کنیم که ایده‌اش واقعاً شاهکاره.
ابزار Skirk، ترافیک اینترنت شما رو می‌گیره، رمزش می‌کنه و به عنوان یه فایل ناشناس، می‌فرستتش داخل صندوق پستیِ Google Drive شما. بعد یه سرور که اون‌ور آب دارید، این فایل‌ها رو از گوگل درایو می‌خونه، به سایت اصلی وصل می‌شه و جواب رو دوباره از طریق گوگل درایو برمی‌گردونه به گوشی یا سیستم شما!
🔥
چرا این روش خیلی خفنه؟
چون سیستم فیلترینگ (DPI) فقط می‌بینه که شما دارید تو اکانت گوگل درایوتون یه سری فایل رو آپلود و دانلود می‌کنید (که کاملاً هم رمزنگاری شده است). این یعنی یه ارتباط صددرصد وایت‌لیست و امن با یکی از معتبرترین دامنه‌های دنیا!
🛠
نیازمندی‌های این روش (برای حرفه‌ای‌ها):
این روش به درد کاربرای عادی که دنبال یه دکمه اتصال می‌گردن نمی‌خوره. شما نیاز دارید به:
1️⃣
یک سرور مجازی (VPS) که نت آزاد داشته باشه (برای نصب بخشِ Exit سیستم).
2️⃣
یک اکانت گوگل معمولی (جیمیل).
3️⃣
نصب کلاینت روی گوشی یا لپ‌تاپ خودتون.
⚡️
تغییرات نسخه جدید (v0.1.45):
تو این آپدیتِ داغ، سازنده یه فایل نصبی پرتابل (Portable) برای ویندوز با رابط کاربری گرافیکی اضافه کرده که کار رو خیلی راحت می‌کنه.
📥
لینک‌های دانلود مستقیمِ کلاینت (نسخه v0.1.45):
(توجه: برای نصب سرور، به صفحه گیت‌هاب پروژه که پایین‌تر گذاشتیم مراجعه کنید).
📱
اندروید (APK):
🔗
https://github.com/ShahabSL/Skirk/releases/download/v0.1.45/skirk-android-arm64.apk
💻
ویندوز (نسخه پرتابل و گرافیکی با رابط کاربری):
🔗
https://github.com/ShahabSL/Skirk/releases/download/v0.1.45/Skirk_windows_x64_portable.zip
💻
ویندوز (نسخه فقط خط فرمان/CLI):
🔗
https://github.com/ShahabSL/Skirk/releases/download/v0.1.45/skirk-windows-amd64.zip
🐧
لینوکس:
🔗
https://github.com/ShahabSL/Skirk/releases/download/v0.1.45/skirk-linux-amd64.tar.gz
📖
لینک گیت‌هاب برای آموزش کاملِ نصب سرور (بخش Exit):
https://github.com/ShahabSL/Skirk
📌
#معرفی_ابزار
#گوگل_درایو
#اسکیرک
#نت_ملی
#تونل
#Skirk
#VPS
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5119" target="_blank">📅 01:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آنقدر سخت که عقل از قبولش سر باز زند و آنقدر زهر که زبان از بیانش تلخ گردد...</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5118" target="_blank">📅 00:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚀
معرفی ابزار Whitelist Bypass: عبور از فیلترینگ با پوشش تماس تصویری «بله»!
🤯
---
رفقا سلام!
✋
امروز یه پروژه مهندسی‌معکوس‌شده‌ی به‌شدت فنی و خفن به اسم Whitelist Bypass رو معرفی می‌کنیم. این ابزار، ترافیک اینترنت شما رو مخفیانه داخل یک «تماس تصویری» در پلتفرم Bale Meet (بله) جا می‌ده و از سرورهای داخلی عبور می‌ده!
🔥
مکانیزم این ابزار چطوره؟
از دید سیستم فیلترینگ (DPI)، شما در حال یک تماس ویدیویی کاملاً عادی روی سرورهای وایت‌لیست‌شده‌ی «بله» هستید؛ اما در واقعیت، دیتای اینترنت آزاد داره از طریق تونل‌های ویدیویی (VP8) یا کانال‌های داده (DataChannel) بین دو دستگاه رد و بدل می‌شه!
این سیستم دو بخش داره:
1️⃣
Creator (سرور): دستگاهی که اینترنت آزاد داره و تماس رو «ایجاد» می‌کنه (معمولاً لپ‌تاپ یا سرور مجازی خارج از کشور).
2️⃣
Joiner (کلاینت): دستگاهی که نت ملی داره و به اون تماس «می‌پیونده» (مثل گوشی یا لپ‌تاپ داخل ایران).
💻
آموزش راه‌اندازی سریع:
🔸
تنظیم بخش Creator (روی دستگاهی که نت آزاد دارد):
۱. نسخه دسکتاپ Creator رو متناسب با سیستم‌عاملتون (از لینک‌های پایین) دانلود و نصب کنید.
۲. برنامه رو باز کنید، روی علامت + بزنید و تب Bale رو انتخاب کنید.
۳. با شماره بلهِ خودتون لاگین کنید. برنامه خودکار یه تماس می‌سازه.
۴. لینکِ اتصالی (Join Link) که بهتون می‌ده رو کپی کنید و برای گوشی/دستگاه کلاینت بفرستید.
📱
تنظیم بخش Joiner (روی دستگاهی که نت ملی دارد):
۱. نسخه Joiner رو (مثلاً فایل APK برای اندروید) دانلود و نصب کنید.
۲. لینک اتصالی که از مرحله قبل گرفتید رو تو برنامه پیست کنید.
۳. دکمه GO رو بزنید و دسترسی VPN رو بهش بدید. تمام! کل ترافیک گوشی از تماس ویدیویی بله عبور می‌کنه.
⚠️
نکات بسیار مهم:
🔹
امنیت: این تونل برای دسترسی به اینترنت آزاده، نه مخفی موندن هویت. بله می‌دونه شما کی هستید و به کجا وصل شدید. پس فقط برای کارهای روزمره و سایت‌های امن (HTTPS) استفاده کنید.
🔹
این ابزار یکم حرفه‌ای‌تر از نسخه‌های قبلیه و برای کسایی که سرور مجازی (VPS) دارن، بهترین گزینه برای ساخت تونل محسوب می‌شه.
📥
لینک‌های دانلود مستقیم (نسخه v0.1.0):
💻
فایل‌های بخش Creator (برای لپ‌تاپ/سرور دارای نت آزاد):
🔹
ویندوز:
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/Whitelist.Bypass.Creator-0.1.0-x64.exe
🔹
مک (پردازنده M1/M2):
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/Whitelist.Bypass.Creator-0.1.0-arm64.dmg
🔹
لینوکس:
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/Whitelist.Bypass.Creator-0.1.0.AppImage
📱
فایل‌های بخش Joiner (برای دستگاهِ دارای نت فیلترشده):
🔹
اندروید (APK):
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/whitelist-bypass.apk
🔹
آی‌او‌اس (IPA برای سایدلود):
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/whitelist-bypass-proxy.ipa
🔹
ویندوز (کلاینت):
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/WhitelistBypass.Joiner-0.1.0-x64.exe
📌
#معرفی_ابزار
#بله_میت
#نت_ملی
#تونل
#وایت_لیست
#Whitelist_Bypass
#P2P
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5117" target="_blank">📅 23:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
معرفی ابزار BaleVPN: تبدیل پیام‌رسان «بله» به تونل اینترنت آزاد!
🤯
---
رفقا سلام!
✋
امروز یه ابزار به‌شدت خلاقانه (P2P) رو معرفی می‌کنیم که ترافیک اینترنت رو از طریق زیرساخت «تماس صوتیِ پیام‌رسان بله» منتقل می‌کنه!
مکانیزم کار چطوره؟
🔸
یک گوشی نقش سرور رو داره: اینترنت سالم و آزاد خودش رو به اشتراک می‌ذاره.
🔸
گوشی دیگه نقش کلاینت رو داره: تمام اینترنتش رو از طریق سرور می‌گیره.
از دید سرورهای بله، این ارتباط فقط یک تماس صوتی طولانی بین دو مخاطبه! بدون نیاز به سرور خارجی، بدون ثبت‌نام جدید و پرداخت پول؛ فقط دو حساب بله که شماره همدیگه رو سیو داشته باشن.
📱
آموزش راه‌اندازی گام‌به‌گام (برای ۲ گوشی اندرویدی):
۱. پیش‌نیازها و نصب:
فایل APK رو از لینک‌های پایین دانلود و روی هر دو گوشی نصب کنید. (روی هر دو گوشی با شماره موبایلِ خودتون لاگین کنید؛ اگه شماره مجازی غیرایرانی بدید، کد تایید بله داخل تلگرامتون میاد!).
۲. تنظیم گوشی سرور (اونی که نت آزاد داره):
در صفحه اصلی برنامه، سوئیچ حالت رو روی Server (سرور) بذارید. سرویس خودکار شروع می‌شه و منتظر اتصال می‌مونه. (سرور همیشه باید روشن و برنامه در حال اجرا باشه. در اولین اتصال، روی گوشی سرور نوتیفیکیشن میاد که باید Allow/تایید رو بزنید).
۳. تنظیم گوشی کلاینت (اونی که نت فیلتر داره):
سوئیچ رو روی Client (کلاینت) بذارید. روی Peer Select (انتخاب مخاطب) بزنید و اکانتِ گوشیِ سرور رو انتخاب کنید. بعد روی VPN Start بزنید و دسترسی رو تایید کنید. تمام! اینترنت متصل شد.
⚠️
نکات به‌شدت مهم:
🔒
حریم خصوصی: ترافیک رمزنگاری می‌شه (DTLS)، اما این ابزار برای ناشناس موندن (Anonymity) نیست و سرورهای بله میانجی هستن. حتماً از سایت‌های امن (HTTPS) استفاده کنید و ترجیحاً اکانت بله رو با شماره مجازی بسازید.
⚖️
استفاده مسئولانه: فقط برای وب‌گردی، پیام دادن و کارهای روزمره خوبه. دانلود سنگین، استریم ویدیو یا تورنت اکیداً ممنوع! (چون ترافیک غیرعادیِ یک «تماس صوتی» سریعاً تو بله لو می‌ره و پروژه رو برای همه مسدود می‌کنن).
💡
دو فوت کوزه‌گری:
1️⃣
اتصال لپ‌تاپ: برای اینکه نتِ آزادِ گوشی کلاینت رو به لپ‌تاپ هم برسونید، اپلیکیشن EveryProxy رو روی کلاینت نصب کنید و هات‌اسپات بسازید.
2️⃣
نسخه فوق‌حرفه‌ای: اگر حرفه‌ای هستید، می‌تونید سرور Node.js رو روی لپ‌تاپ/سرورِ لینوکس یا macOS (با TUN واقعی و NAT هسته‌ای) ران کنید که سرعتش بی‌نظیره و گوشی اندرویدی رو به عنوان کلاینت بهش وصل کنید.
📥
لینک‌های دانلود مستقیم (نسخه 1.3.2):
(فایل اندروید رو به صورت فایل تو کانال هم براتون می‌ذاریم)
📱
نسخه اندروید:
🔗
https://github.com/kookoo1sabzy/BaleVPN/releases/download/v1.3.2/BaleVpn-1.3.2-release.apk
💻
نسخه ویندوز:
🔗
https://github.com/kookoo1sabzy/BaleVPN/releases/download/v1.3.2/balevpn-1.3.2-win-x64.exe
🐧
نسخه لینوکس:
🔗
https://github.com/kookoo1sabzy/BaleVPN/releases/download/v1.3.2/balevpn-1.3.2-linux-x64
🍏
نسخه مک (M1 و M2):
🔗
https://github.com/kookoo1sabzy/BaleVPN/releases/download/v1.3.2/balevpn-1.3.2-macos-arm64
🍏
نسخه مک (اینتل):
🔗
https://github.com/kookoo1sabzy/BaleVPN/releases/download/v1.3.2/balevpn-1.3.2-macos-x64
📌
#آموزش
#معرفی_ابزار
#بله_وی_پی_ان
#نت_ملی
#تونل
#BaleVPN
#P2P
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5116" target="_blank">📅 23:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آپلودر جدید
https://dardi.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5115" target="_blank">📅 23:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سامانتل شیر و خورشید وصل
2.16.105.221
2.16.152.18
2.16.103.34
2.16.118.127
2.16.128.254
2.16.156.128
2.16.159.249
185.200.232.49
2.16.176.93
2.16.172.173
2.16.102.167
2.16.169.209
2.16.11.208
2.16.149.128
2.16.151.107
2.16.216.153
2.16.141.148
2.16.144.59
2.16.176.33
2.16.160.71
2.16.135.126
2.16.178.15
2.16.164.125
2.16.128.79
2.16.0.17
2.16.108.172
2.16.138.218
2.16.167.199
2.16.163.128
2.16.191.68
2.16.138.157
2.16.177.249
2.16.139.247
2.16.22.170
2.16.110.202
2.16.118.49
2.16.184.169
2.16.125.64
2.16.153.190
2.16.136.127
2.16.173.37
2.16.148.33
2.16.100.71
2.16.221.231
2.16.163.36
2.16.146.17
2.16.220.94
2.16.218.50
2.16.41.114
2.16.116.43
2.16.226.113
2.16.72.117
2.16.1.139
2.16.159.36
2.16.143.115
2.16.37.71
2.16.205.79
2.16.173.204
185.200.232.27
2.16.206.86
2.16.162.23
2.16.86.75
2.16.135.4
2.16.166.156
2.16.149.55
2.16.200.249
2.16.197.101
2.16.169.168
2.16.222.189
2.16.85.120
2.16.112.85
2.16.40.69
2.16.174.10
2.16.56.69
2.16.224.52
2.16.134.254
2.16.112.112
2.16.152.41
2.16.206.193
2.16.100.81
2.16.79.19
2.16.146.106
2.16.224.70
2.16.189.236
2.16.201.36
2.16.179.232
2.16.73.74
2.16.143.225
2.16.166.181
2.16.14.118
2.16.119.211
2.16.125.18
2.16.142.41
2.16.49.105
2.16.187.49
2.16.223.248
2.16.115.68
2.16.206.248
2.16.67.30
2.16.206.239
2.16.130.121
2.16.140.209
2.16.128.2
2.16.215.35
2.16.120.193
2.16.193.235
2.16.208.65
2.16.154.163
2.16.205.216
2.16.225.51
2.16.4.200
2.16.128.166
2.16.27.68
2.16.200.6
2.16.227.247
2.16.137.57
2.16.121.19
2.16.22.133
2.16.202.64
2.16.206.151
2.16.104.244
2.16.34.72
2.16.105.166
2.16.95.168
2.16.218.155
2.16.107.245
2.16.222.174
2.16.128.68
2.16.116.137
2.16.60.143
2.16.127.104
2.16.42.3
2.16.109.19
2.16.206.185
2.16.163.126
2.16.177.236
2.16.120.71
2.16.65.21
2.16.44.129
2.16.38.180
2.16.151.226
2.16.141.84
2.16.146.220
2.16.179.72
2.16.87.189
2.16.110.20
2.16.216.122
2.16.177.225
2.16.172.248
2.16.75.171
2.16.141.162
2.16.131.51
2.16.99.240
2.16.169.138
2.16.126.65
2.16.26.159
2.16.30.95
2.16.220.73
2.16.130.194
2.16.49.167
2.16.31.190
2.16.2.217
2.16.80.10
2.16.189.232
2.16.138.98
2.16.87.55
2.16.70.198
2.16.205.167
2.16.150.195
2.16.155.228
2.16.33.227
2.16.163.141
2.16.70.152
2.16.84.136
2.16.187.51
2.16.45.79
2.16.49.48
2.16.211.90
2.16.40.164
2.16.191.84
2.16.212.94
2.16.37.38
2.16.42.13
2.16.104.209
2.16.213.68
2.16.20.59
2.16.93.180
2.16.64.44
2.16.60.235
2.16.113.55
2.16.224.25
2.16.126.14
2.16.143.42
2.16.189.148
2.16.167.212
2.16.44.162
2.16.59.231
2.16.212.21
2.16.115.83
2.16.145.167
2.16.125.199
2.16.114.64
2.16.204.70
2.16.45.42
2.16.203.1
2.16.193.73
2.16.203.80
2.16.210.173
2.16.166.126
2.16.43.247
2.16.206.141
2.16.209.11
2.16.73.104
2.16.194.74
2.16.47.71
2.16.146.42
2.16.19.227
2.16.210.225
2.16.220.1
2.16.203.34
2.16.212.71
2.16.166.193
2.16.203.77
2.16.197.180
2.16.179.251
2.16.150.85
2.16.131.48
2.16.188.192
2.16.30.209
2.16.60.153
2.16.190.172
2.16.132.226
2.16.105.159
2.16.135.245
2.16.114.221
2.16.141.77
2.16.137.243
2.16.204.162
2.16.179.77
2.16.137.11
2.16.186.23
2.16.166.51
2.16.206.207
2.16.17.116
2.16.186.10</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/5114" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتلیفای وصل
یکی از بچه های گل کانال زحمتشو کشیده
❤️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5113" target="_blank">📅 23:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdi Jenabi (Mr.44)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NETLify.txt</div>
  <div class="tg-doc-extra">144.1 KB</div>
</div>
<a href="https://t.me/archivetell/5110" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5110" target="_blank">📅 23:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ربات جمنای
@Gemini_PV_bot
@NewGeminiAi_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5106" target="_blank">📅 23:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5105" target="_blank">📅 23:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">لینک داخلی عقاب
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5104" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شیر و خورشید شاتل
یکی از ممبرای عزیز کانال اسکن کرده
2.23.170.80
2.23.168.144
2.23.168.47
2.23.168.174
2.23.168.213
2.23.168.96
2.23.168.7</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/5103" target="_blank">📅 22:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚡
آموزش ساخت Shortcut در Termux (اجرای سریع اسکریپت‌ها)
━━━━━━━━━━━━━━━
📌
با این روش می‌تونی برای اسکریپت‌ها و پروژه‌هات شورتکات بسازی
و مستقیم از ویجت گوشی اجراشون کنی
🚀
━━━━━━━━━━━━━━━
---
🟢
1) نصب اپ Termux:Widget
اول این برنامه رو نصب کن:
Termux:Widget
⚠
بدون این برنامه شورتکات‌ها نمایش داده نمیشن
---
📁
2) ساخت پوشه مخفی شورتکات‌ها
داخل Termux بزن:
mkdir -p ~/.shortcuts
---
📝
3) ساخت فایل شورتکات
مثلاً برای پروژه scanner:
nano ~/.shortcuts/scanner
---
⚙️
4) قرار دادن دستور اجرا داخل فایل
این کد رو Paste کن:
#!/data/data/com.termux/files/usr/bin/bash
cd ~/scanner
python
app.py
bash
---
💾
5) ذخیره فایل
داخل nano:
🔹
CTRL + O
🔹
Enter
🔹
CTRL + X
---
🔓
6) دادن دسترسی اجرا
chmod +x ~/.shortcuts/scanner
---
🚀
فعال کردن Shortcut روی صفحه گوشی
📱
حالا:
1️⃣
انگشت نگه دار روی Home Screen
2️⃣
برو بخش Widgets
3️⃣
ویجت Termux رو اضافه کن
4️⃣
شورتکات ساخته‌شده نمایش داده میشه
5️⃣
لمس کن → مستقیم اجرا میشه
⚡
---
✅
کاربردها
✔
اجرای سریع Python
✔
اجرای سرور Flask
✔
اجرای Bash Script
✔
اجرای ابزارهای ترموکس
✔
بدون تایپ دستورهای طولانی
تهیه توسط یکی از ممبرای عزیز کانال Samad.R
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5101" target="_blank">📅 18:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrfDN1H2A1Ou2EntxWCXjHRIKsjWBAb8lQ-NuavVLZ1d2gwmsinhh-DRw4-dTDmWhB9968iOMtPlpb-xFvZWMTQz0XCq0kzk0x0s6yUuEe0vh2kZTfav5VYJeT1YOh1fjjQa7tQKgnqGrh8_5-3VoLg1D345jui0DZ3iH2cZ-wv7f15rOSTC2EDa5cEk0y9J-eRGHO2_TCHbTXexFNytAbW5_3aC2wD2efHUDa3ZJ4x1vuliuMgXcZGl4FVo-rO_53XOypjn-e01RLa3FCZdSLlNPPn0g-2AiDv6C0p6D-Lcy3DU-IWfCgelkjHJcERIEAyXtxJs7RKEvvvPdf_aCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت تولید ایده‌ های محتوایی جذاب بر اساس حوزه فعالیتی که دارید
Based on my niche and audience below, generate content ideas that feel specific, relevant, and worth saving.
Avoid generic topics and focus on angles that would catch attention, start discussion, or make people think, “I need this.”
Explain briefly why each idea could work.
Niche and audience: [paste here]
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5100" target="_blank">📅 18:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">#اختصاصی
⚡
نکات برتر کدنویسی وب با هوش مصنوعی برای مبتدیان و توسعه‌دهندگان
🚀
1. بلافاصله شروع به کدنویسی نکنید
قبل از نوشتن کد:
• ایده را به‌وضوح تعریف کنید
• ویژگی‌ها را فهرست کنید
• صفحات/کامپوننت‌ها را مشخص کنید
• جریان کاربر را برنامه‌ریزی کنید
✅
جریان کاری بهتر
ایده → ویژگی‌ها → درخواست → تولید → بهبود → استقرار
🤖
2. یاد بگیرید چگونه به درستی با هوش مصنوعی صحبت کنید
هوش مصنوعی وقتی درخواست‌ها دقیق باشند خروجی بهتری می‌دهد.
❌
درخواست بد
یک وب‌سایت بساز
✅
درخواست خوب
یک وب‌سایت نمونه‌کار مدرن و واکنش‌گرا با استفاده از React و Tailwind CSS با حالت تاریک، انیمیشن‌ها، بخش قهرمان، بخش پروژه‌ها و فرم تماس بساز.
🧠
3. با هوش مصنوعی مانند یک توسعه‌دهنده ارشد رفتار کنید
به جای درخواست:
کد بده
بپرسید:
• معماری را توضیح بده
• عملکرد را بهینه کن
• رابط کاربری را بهبود بده
• کد را بازسازی کن
• اشکالات را رفع کن
• قابلیت توسعه را اضافه کن
🔥
4. پروژه‌های کوچک را سریع بسازید
صرف نکنید:
3 ماه یادگیری نظری
صرف کنید:
3 ساعت ساخت چیزی
🚀
بهترین پروژه‌های مبتدی
• اپلیکیشن کارهای روزانه
• ماشین حساب
• ردیاب هزینه‌ها
• رابط چت هوش مصنوعی
• اپلیکیشن یادداشت
• ردیاب عادت
• اپ هواشناسی
⚡
5. از ابزارهای مدرن کدنویسی هوش مصنوعی استفاده کنید
🔥
بهترین ابزارها
• Cursor AI
• GitHub Copilot
• Replit
• ChatGPT
• Claude AI
🎨
6. الهام طراحی را کپی کنید، نه محصولات کامل
از این منابع الهام بگیرید:
• Dribbble
• Behance
• Mobbin
یاد بگیرید:
• چیدمان‌ها
• رنگ‌ها
• تایپوگرافی
• انیمیشن‌ها
🐞
7. اشکال‌زدایی مهارت واقعی است
توسعه‌دهندگان حرفه‌ای زمان زیادی را صرف اشکال‌زدایی می‌کنند.
یاد بگیرید:
• خواندن دقیق خطاها
• استفاده از console.log
• ابزارهای توسعه مرورگر
• درخواست توضیح خطاها از هوش مصنوعی
⚡
8. همه چیز را حفظ نکنید
توسعه‌دهندگان مدرن:
• مرتب جستجو می‌کنند
• از مستندات استفاده می‌کنند
• از کمک هوش مصنوعی بهره می‌برند
تمرکز کنید بر:
• درک مفاهیم
• حل مسئله
• ساخت مداوم
🧩
9. مسائل بزرگ را به بخش‌های کوچک تقسیم کنید
به جای:
ساخت کلون نتفلیکس
تقسیم کنید به:
1. نوار ناوبری
2. بخش قهرمان
3. کارت‌های فیلم
4. واکشی API
5. قابلیت جستجو
6. احراز هویت
هوش مصنوعی با وظایف کوچک‌تر بهتر کار می‌کند.
🚀
10. یاد بگیرید کامپوننت‌ها را قابل استفاده مجدد بسازید
کامپوننت‌های قابل استفاده مجدد زمان زیادی صرفه‌جویی می‌کنند.
نمونه‌ها:
• دکمه‌ها
• کارت‌ها
• نوار ناوبری
• فرم‌ها
• مودال‌ها
این روش کار سازندگان سریع است.
🔥
11. میانبرهای صفحه‌کلید را یاد بگیرید
سرعت در کدنویسی وب اهمیت دارد.
میانبرهای ضروری
• کپی/پیست
• ویرایش چند مکان‌نما
• جستجو و جایگزینی
• میانبرهای ترمینال
• میانبرهای VS Code
🛠️
12. از کتابخانه‌های رابط کاربری آماده استفاده کنید
همه چیز را از صفر نسازید.
بهترین کتابخانه‌های UI
• shadcn/ui
• Material UI
• Tailwind UI
⚡
13. زود Git و GitHub را یاد بگیرید
هر توسعه‌دهنده جدی از Git استفاده می‌کند.
یاد بگیرید:
git init
git add
git commit
git push
مبانی شاخه‌بندی
🌐
14. پروژه‌ها را سریع مستقر کنید
پروژه‌ها را فقط روی لپ‌تاپ نگه ندارید.
استقرار با استفاده از
• Vercel
• Netlify
• Render
🧠
15. به صورت عمومی بسازید
سفر خود را در اینجا منتشر کنید:
• LinkedIn
• Medium
• Telegram
• YouTube
• کانال‌های WhatsApp
این باعث می‌شود:
• فرصت‌ها
• مخاطب
• مشتریان فریلنس
• شبکه‌سازی
💰
16. روی حل مشکلات واقعی تمرکز کنید
بهترین پروژه‌ها مشکلات:
• زمانی
• کسب‌وکار
• اتوماسیون
• بهره‌وری
🚀
17. زود APIها را یاد بگیرید
APIها برنامه‌ها را قدرتمند می‌کنند.
نمونه‌ها:
• API هواشناسی
• API OpenAI
• API Stripe
• API نقشه‌ها
⚡
18. دنبال تکنولوژی‌های زیاد ندوید
تسلط پیدا کنید بر:
• HTML
• CSS
• JavaScript
• React
• ابزارهای هوش مصنوعی
سپس به تدریج گسترش دهید.
🏆
19. استمرار بهتر از انگیزه است
حتی:
1 پروژه در هفته
30 دقیقه در روز
می‌تواند سطح مهارت شما را کاملاً تغییر دهد.
🔥
20 راز واقعی کدنویسی وب
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5099" target="_blank">📅 17:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ربات جستجوی معکوس تصویر با موتورهای جست و جوی مختلف مانند SauceNAO، گوگل، یاندکس و ..
@reverse_image_search_bot
@ImageEyeBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/5098" target="_blank">📅 17:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/5097" target="_blank">📅 17:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سایت زیرنویس فیلم و سریال
subkade.ir
subzone.ir
3fa.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5096" target="_blank">📅 17:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فیلم و سریال بدون سانسور و رایگان
https://www.my-f2mx.top/
ravinaz.top
F2mc.top
http://Paradoxmoviz.com
http://F2mede.top
https://www.simindad.top/
https://serialblog.top
https://www.sorkhcloud.top/
Movieyaab.ir
f2mux.top
www.myf2mi.top
F2my.top
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5095" target="_blank">📅 17:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این وصله واسه من
با شکن و بی شکن تست کنین
vless://56aaf8cd-d2fb-5211-bc9b-c242ee37d429@138.201.54.122:443?allowInsecure=1&alpn=h2%2Chttp%2F1.1&encryption=none&extra=%7B%22xPaddingBytes%22%3A%221-1%22%2C%22xPaddingObfsMode%22%3Atrue%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22xPaddingKey%22%3A%22iran%22%2C%22xPaddingHeader%22%3A%22iran%22%2C%22headers%22%3A%7B%22x-host%22%3A%2289.208.97.163%3A444%22%7D%7D&host=godxyz.dpdns.org&mode=auto&path=%2FIR_NETLIFY&security=tls&sni=vuejs.org&type=xhttp#%F0%9F%8C%90%20@IR_NETLIFY%20@ArchiveTell%20%7C%20vuejs.org%20%7C%20138.201.54.122%20%7C%20Test</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5094" target="_blank">📅 16:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شیر و خورشید سامانتل
185.109.61.27
31.214.169.244
185.208.174.167
178.252.128.66
185.88.178.196
185.142.158.162
185.53.142.174
164.138.17.122
37.191.95.70
185.208.175.228
85.133.167.108
185.50.37.52
109.230.206.175
5.160.128.142
78.39.234.140
185.141.105.139
185.37.55.30
94.232.173.28
78.157.41.60
2.186.121.65
158.58.184.147
93.115.127.9
185.255.91.60
2.188.21.138
185.137.25.146
185.141.106.238
109.72.197.1
89.32.197.226
78.38.174.2
2.188.21.58
217.219.162.200
46.32.31.30
شیر و خورشید</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5092" target="_blank">📅 15:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اسکنر اندروید و پیسی
توسعه دهنده
یکی از ممبرای عزیز کانال
❤️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5091" target="_blank">📅 13:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SNI Radar v2.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/archivetell/5089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5089" target="_blank">📅 13:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6cNpEGHjEnYUj9wMYRI3e5J7oreYTSF_Tf8dXg9NSGAcdL5ecGrRZjT5ZyEvNT5GbcxnzLrB5iqlphCrb6p9P6MCEJR0jlBjWIP0_l7PD1P5OtBAnXo7eJjSjDdfFyGwx5hWLhXcKaqIkWBPacZmL33ZOzfvnknitHtetylk4I_kqI5R1kdRsBwPQ9xNNNMTC5j15AZu5-TsebHzr3ytAw6x8By83NHqZTmuHMdB2QTVFvYvHYKteEWrzrv975sHJL1OYNvVEabUj_o7vPbrGzpIKIKfSa8eQ-QkQ4yJAGsPnZNNs8VJ53CzTDOg-eB_QUGFTlbQ6PaAraTDhL9xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5088" target="_blank">📅 13:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SNI Radar.apk</div>
  <div class="tg-doc-extra">4.7 MB</div>
</div>
<a href="https://t.me/archivetell/5087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5087" target="_blank">📅 13:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnEO5IbtNUbNdSKiQsH-0rk0LD2TPpi-ogs2wG_8_6SbL7__nLg-9pMvUMJq9Oo9rhOlqM0-l6q1JQiwhiRySlj8zDppyfApaRdjQIOgoq9UOTc_SqvWAL_jImNAzodFbZ620_9S0z2uQGbSUJXNPPCnDIaPz7ktU3aUEcFYWwIGhzAqDy_mF909Xg_BSOvuX28oovqbyMFts1vvtsMoS9p_OLJKPbjPv83a3YQ7QxgcoW1KT9Z2TnhxMjQBa3d-kiuSoUSM7CPzgSjVo9vj9SXr9VFjSiC0x3LytvRooRryIMS6_NlKfCHH7rNHySqTAN9FdlBGAje7PdJ7hDXcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fta8D8VL3X9tRNjTk4WcTO5SiOzA37LWn_GGq4c5lop853MGEMWnF6hsCqR4HFyH8xVpAKUmn8UX8LTUhU_RF26HEP8mBuHnvoo8AonjiAlWLlYagw2SYgO-XA0sho32ugTQjKUIuPvpWuYQiN0I9SRqNKtmaXkBd0mz3qs3URt1ta13Kl8mV2mt_p5AdX-rpUmBIJR1zdDYqZzCgERatYz5A7c1J3-Mwgpcw0Rfk88VUAA2fNR0T_ahKd1shSI9EJLH5yXMnzCYZMtWrJKRvwDahbrcZvqOz9chgrxO5SbDMVkO76SZxf_Z7kxQuSYAMt9QNZ1qDEL841tmi-YdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f45OegnjbufwdCbO08HltmYllZsY5v67sTxaIFTluG4dnhYBKtypzhRow79KjLOZkZyuIr8scnPKSdIfrk2YSDl8z7wrlmPq4fGD1d2IEL1Dly2J_1gmke2AAjE6eHtvMBgqxcR-qjn8sacie11LAryUbk0j403UaYpkdWcB9A2hrv_yugbqqaGQzK6tvRbhQHP-fZ8ETaZAxWKJM5LJkEGDO7Jm7nxPSwUcb4R1nxbbkdleJvoBtRmnFCEVeprah5mEJumrYSO8VVBlm3TyVbgPDQpjgNHTv8iz7NMfA7uCxlOXfSVdYUntf6Gu67BjYKUuzW5N24aICxzI3eAUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_xb1sb51hcR1VlmDBm95nZ-S_8dAfrdBSYhp8tTAgN0pNqqqWRpCp9NnW1lNuB2nikSjljH_w-BY4SnA0TMA7Eb1Xi3KZ5t7TZ3aoEyaSuCRB109tSnGT2RI1qV3jhtqAS224E2kN5k_6NcSLUw6N9_X4YHd09urjNoVxGfD_3jU7YAayLNKHBFm1FiuubWyZ96eOro6BJtW6yVaZzazz34vhYn7Z7RYYd4VLQccnziIXshW1o3BBHPcdmWlmi8WJXtbj90RQz9rTB3T7Xdjkze1pjfEv4fTGV5X5Da4BD8rluk5N9XzjjRTENxacsK3voqOp_KGwDuIUHUsnkbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ijd3rnPDBTMGgrjZTqqd_qnlhjuPkimuaXEMVjhGA65VlniL82A5EMFHzvPIJBaY9wUX2iXPocsO7n4-wD9j-52qIDGr-Otrnb7J3A3NuJd-LS0LZRDEL1SH73wGhU9UyoHd-p2DvNy8Eu8rELx1w0YX9pvZHVE5Qxw4Z0hzEWIuai4rw0bOmKNPNCfNO0EdJ9aIdVC_3NYbDa9HXQ4a9ca5TNJlK3ZmZpjIzVN10HcRzhPAUroi5bBVsYXdoE1XsNDrpXRpvosyF5NJrV3BLuDA8k7wOkVK3msRrBN1HLS5oICw6IhcUB9Ud5ebx9lXT72N1g43VupzxmJ_cKAiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guHD8vJKO_eCMAPLgHgujqZ_32G_NLtSzUHvqygBuH2DCm5bgzWG4l3QpYSSBrbkPvmqGTWDPw7ayBxK2zPqOsvf8JZbMdfE-M9kL0CJXOxonEV38tHnRVVA1JQK91e-rSFfJ_JaLQ-oXp_LDlJ-9ssuhSCr58Wl0X_lWEngCldGU-_WpZjxZCmPz6_eHkzl55eCr6W0uRnNVzHJt19caA85GpgITEFpg67PweAVXuPVX1zI8ITUqW1QNOWdCs-oKl4bNf5zPIoJsfuu2CU8VRMWP5-LNPTKOy8kPatnbX2P4TI_cIPhXZYqwOp4JP0hiOE5J3oPhOS5Khv25FYiqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیش از رویداد Google I/O 2026، انتظارات بسیار بالا است. گوگل ممکن است نگاهی اولیه به سیستم‌عامل دسکتاپ آینده خود، AluminiumOS (Android Desktop)، که قرار است جایگزین ChromeOS شود (احتمالاً در اواخر سال ۲۰۲۶)، بیندازد.
این اطلاعات بر روی یک MacBook Pro از طریق UTM اجرا می‌شود. سیستم‌عامل ALOS گوگل اساساً اندروید ساده با ویژگی‌های دسکتاپ است:
• پوشه‌های دسکتاپ و دسکتاپ‌های مجازی
• پنل تنظیمات و اعلان‌های بهینه‌شده
• ژست‌های لمسی و میانبرهای صفحه‌کلید
• برنامه‌های بهینه‌شده خاص (مانند مدیر وظیفه)
• اکوسیستم قوی بین لپ‌تاپ و موبایل (از جمله دستگاه‌های اپل از طریق «Link to iOS»)
واقعیت این است که ALOS بیشتر شبیه نسخه بهبودیافته Samsung DeX است تا یک سیستم‌عامل دسکتاپ واقعی. ضعف‌های بزرگ آن شامل عدم وجود برنامه‌های بهینه‌شده برای ماوس و صفحه‌کلید (حتی برنامه‌های گوگل نسخه‌های وب در پنجره بسته هستند) و سخت‌افزار محدود (چیپ‌های Snapdragon X به پای سری M اپل نمی‌رسند) می‌باشد.
آیا فکر می‌کنید ALOS آینده روشنی دارد یا زودتر از موعد به «قبرستان کشته شده توسط گوگل» می‌رسد؟
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5081" target="_blank">📅 13:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚀
آموزش تونل کردن ترافیک ترمینال لینوکس با Proxychains4
---
رفقا سلام!
✋
خیلی وقتا تو لینوکس می‌خوایم یه ابزار نصب کنیم، از گیت‌هاب کلون بگیریم یا پکیج‌ها رو آپدیت کنیم، ولی چون ترمینال تحریمه یا فیلتره، همش ارور تایم‌اوت می‌ده.
بهترین و تمیزترین راه برای عبور دادن ترافیکِ ترمینال از فیلترشکنِ روی سیستم (مثل V2ray ،Nekobox یا شیر و خورشید)، استفاده از ابزار بی‌نظیر Proxychains4 هست.
🛠
مرحله ۱: نصب
اول ترمینال رو باز کنید و پکیجش رو نصب کنید (دستور زیر برای اوبونتو، دبیان، کالی و مینت هست):
sudo apt update
sudo apt install proxychains4
⚙️
مرحله ۲: کانفیگ و اتصال به فیلترشکن
حالا باید بهش بگیم ترافیک رو بفرسته سمت پورتِ فیلترشکن ما. فایل تنظیماتش رو با ویرایشگر nano باز می‌کنیم:
sudo nano /etc/proxychains4.conf
با کلیدهای جهت‌نما بیاید به انتهایی‌ترین خطِ این فایل. اونجا بخشی به اسم [ProxyList] می‌بینید.
یه خط پیش‌فرض اونجا هست که نوشته
socks4  127.0.0.1 9050
. ابتدای این خط یه علامت # بذارید تا غیرفعال بشه.
حالا زیرش، آی‌پی و پورت فیلترشکن خودتون رو وارد کنید. (مثلاً برنامه‌های V2rayN/NG و Nekobox معمولاً ترافیک SOCKS5 رو روی پورت 10808 می‌دن. تو آموزش قبلیِ شیر و خورشید هم پورت 10808 بود). پس این خط رو اضافه کنید:
socks5
127.0.0.1
10808
فایل رو ذخیره کنید (با زدن Ctrl+O بعد Enter، و برای خروج Ctrl+X).
💻
مرحله ۳: نحوه استفاده
حالا دو تا روش برای استفاده دارید:
🔸
روش اول (فقط برای یک دستور خاص):
کافیه قبل از هر دستوری که می‌زنید، کلمه proxychains4 رو بنویسید. مثلاً:
proxychains4 sudo apt update
proxychains4 curl
ip.me
🔸
روش دوم (تونل کردن کل ترمینال به‌صورت یکپارچه - پیشنهاد ما):
اگر حوصله ندارید قبل از هر دستور این کلمه رو تکرار کنید، همون اول کار این دستور رو بزنید:
proxychains4 bash
(اگر از zsh استفاده می‌کنید بزنید proxychains4 zsh).
✅
نتیجه: با این کار، شما وارد یه محیط جدید تو همون ترمینال می‌شید که کِل ترافیکش به صورت خودکار از پروکسی رد می‌شه و دیگه نیازی به نوشتن proxychains قبل از دستورات ندارید!
📌
#آموزش
#لینوکس
#ترمینال
#تونل
#پروکسی
#تحریم_شکن
#Proxychains
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5080" target="_blank">📅 11:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سامانتل شیر و خورشید
142.54.178.211
185.137.25.214
81.12.72.218
5.160.13.85
37.255.133.30
81.91.145.2
2.23.169.105
2.23.170.80
2.23.168.254
185.200.232.40</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5079" target="_blank">📅 11:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">لینک داخلی جدید شیر و خورشید
دانلود
Pass :
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/5078" target="_blank">📅 11:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">همراه اول شیر و خورشید
files.pythonhosted.org
167.82.48.223</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/5077" target="_blank">📅 11:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تا ۱۰ روز دیگه جنگ میشه..</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/5076" target="_blank">📅 10:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbK6EQ94u9aE6SQNSwqz1PpER9Kr7aODNaCt7ESnHewSEvvh80pG8E6HjdsrghEyp6_fagXWyf1C8FeijudCZxCpWfZfOkmUmJ9O5CsugGqJXAU8UHSenCL54cdC8NQ_8Ps9k4UbE8CKmx9N6HTM60uz4OKdgarNvQ8pz6rc3JF2-5Imi8XIGbALRL9pjSE8G9ZtBkcszRWjoWQ-HryYHj9QCV5yK6bcJ9v2eId-OuT89ZJabxq_B0GP_bTqJ_ZbAcudT88NADc7-3n0jmhYjoVJ-7f6slNaFXneKbBqq92FDuDD3S3i3jHMBSSOi7oProb0vhtV_BhPt5Uun5CSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی TunnelForge: اتصال مجدد L2TP در اندروید!
---
رفقا سلام!
✋
گوگل تو اندروید ۱۲ به بعد، پشتیبانی از VPNهای قدیمی مثل L2TP رو حذف کرد. اگه سرورهاتون هنوز بر پایه این پروتکل‌هاست، اپلیکیشن ایرانی و اوپن‌سورس TunnelForge مشکلتون رو حل می‌کنه!
✨
ویژگی‌های کلیدی:
🔸
اتصال آسان به L2TP/IPsec (IKEv1) در اندرویدهای جدید.
🔸
دو حالت تونل کل گوشی (VPN) یا فقط پراکسی (Proxy-Only).
🔸
انتخاب برنامه‌های دلخواه برای عبور از تونل (Per-App Routing).
🔸
تنظیمات پیشرفته DNS و MTU.
⚡️
تو آپدیت جدید (v0.7.2) پایداری برنامه بیشتر شده و نام‌گذاری‌ها یکپارچه شده.
📥
دانلود مستقیم نسخه جدید (مخصوص گوشی‌های جدید / arm64-v8a):
🔗
https://github.com/evokelektrique/tunnel-forge/releases/download/v0.7.2/tunnel-forge-v0.7.2-android-arm64-v8a.apk
📌
#تونل_فورج
#اندروید
#نت_ملی
#TunnelForge
#L2TP
#VPN
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5074" target="_blank">📅 10:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromㅤ</strong></div>
<div class="tg-text">امشب شاخص ساندیس و فلافل از اینور بالا میره اونور پیتزا
😁</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5073" target="_blank">📅 10:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تا ۱۰ روز دیگه جنگ میشه..</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5071" target="_blank">📅 10:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به‌نظرتون  این "
⌛️
"چه معنی میده؟
🤔</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5070" target="_blank">📅 09:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/archivetell/5066" target="_blank">📅 02:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGithub Explorer</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">31.2 MB</div>
</div>
<a href="https://t.me/archivetell/5063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">app-arm64-v8a-release.apk
⚖️
Size: 31.2 MB</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/5063" target="_blank">📅 01:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Akamai-IPs.txt</div>
  <div class="tg-doc-extra">99.3 KB</div>
</div>
<a href="https://t.me/archivetell/5062" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رنج آیپی های Akamai
حدود 20 میلیون آیپی</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/archivetell/5062" target="_blank">📅 01:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚀
معرفی و آموزش جامع Network Checker: جعبه‌ابزار قطعیِ دور زدن نت ملی!
---
رفقا سلام!
✋
خیلی‌هاتون دنبال یه راه بی‌دردسر برای اسکن آی‌پی‌های تمیز روی گوشی بودید. امروز اپلیکیشن ایرانی و اوپن‌سورس Network Checker (توسعه‌یافته توسط mirarr-app) رو معرفی می‌کنیم که نه تنها اسکن رو براتون راحت کرده، بلکه یه «جعبه ابزار» همه‌کاره برای عبور از فیلترینگه.
✨
اول ببینیم این برنامه چه امکانات خارق‌العاده‌ای داره:
🔸
اسکنر CDN با هسته Xray (جدید در v0.5.0): قدرتمندترین اسکنر آی‌پی برای اندروید! هسته Xray مستقیم تو خود برنامه جاساز شده و نیازی به ترموکس ندارید.
🔸
بررسی Edge IP: اسکن آی‌پی‌های تمیز کلودفلر، آکامای و...
🔸
شکارچی DNS (DNS Hunter): پیدا کردن آی‌پی‌های فرانتینگ با بررسی دیتاسنترهای داخلی.
🔸
ابزار Vless Modifier: جایگذاری لیست آی‌پی روی کانفیگ‌های Vless.
🔥
رمزگذار پیامک (SMS Encoder): اپراتورها پیامکِ حاوی کانفیگ رو مسدود می‌کنن؛ این ابزار کانفیگ شما رو به یه متن فارسی نامفهوم تبدیل می‌کنه تا راحت پیامکش کنید! طرف مقابل هم با همین برنامه رمزش رو باز می‌کنه!
🤯
🛠
آموزش اسکن آی‌پی آکامای (مخصوص متد سایفون / شیر و خورشید):
حالا بریم سراغ کاربردی‌ترین بخش برنامه برای این روزها؛ پیدا کردن آی‌پی تمیز خیلی راحت‌تر از محیط ترموکس:
1️⃣
تنظیمات اولیه: برنامه رو باز کنید، روی منوی سه خط (بالا) بزنید و وارد بخش Edge بشید. قبل از دادن رنج آی‌پی، روی آیکون تنظیمات (بالا سمت راست) کلیک کنید.
2️⃣
انتخاب SNI و سرعت: تو کادر Test Domain (SNI)، دامنه‌ای که می‌خواید تست بشه رو وارد کنید (مثلاً
pypi.org
یا
www.python.org
یا
a.optnmstr.com
). پورت (443) رو دست نزنید. قسمت Concurrent workers رو بسته به قدرت پردازنده گوشیتون تنظیم کنید (مثلاً ۵۰۰۰) و Save رو بزنید.
3️⃣
شروع اسکن: حالا رنج آی‌پی‌های آکامای رو تو همون صفحه Edge پیست کنید و Scan IP رو بزنید.
4️⃣
استخراج: برنامه آی‌پی‌های متصل رو با پینگشون لیست می‌کنه (۳ تای برتر هم سنجاق می‌شن). وقتی ۲۰-۳۰ تا آی‌پی جمع شد، Copy all رو بزنید.
⚠️
دو فوت کوزه‌گری مهم:
🔹
مراقب پینگ فیک باشید: پینگ دادن تو اسکنر دلیل قطعی بر عبور از فیلترینگ نیست. آی‌پی‌های کپی شده رو همراه با همون SNI تو شیر و خورشید وارد کنید؛ اگر سایت‌ها باز شدن، یعنی آی‌پی تمیزه.
🔹
نکته برای کاربران ترموکس: اگر هنوز با ترموکس اسکن می‌کنید، نسخه گوگل‌پلی خرابه! حتماً نسخه سالم ترموکس رو از استور F-Droid دانلود کنید.
📥
دانلود مستقیم برنامه:
با توجه به سیستم‌عاملتون (ویندوز، لینوکس یا اندروید) آخرین نسخه (v0.5.0) رو از صفحه گیت‌هاب پروژه دانلود کنید:
🔗
https://github.com/mirarr-app/network-checker/releases/latest
📌
#معرفی_ابزار
#آموزش
#اسکنر
#آی_پی
#نتورک_چکر
#نت_ملی
#شیر_و_خورشید
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/archivetell/5061" target="_blank">📅 01:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رایتل فیلتر خاموش عازم اینستا بشید تا وقت هست
😁</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/archivetell/5060" target="_blank">📅 00:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ساب جدید ایران نتلیفای جون
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/sub/AbolUp.txt</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5059" target="_blank">📅 23:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">srckde_6a0367b09043e.html</div>
  <div class="tg-doc-extra">86.3 KB</div>
</div>
<a href="https://t.me/archivetell/5058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">با نت ملی بازش کنید ، خودتون میفهمید چیه
ترجیحا مرورگر کروم</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/archivetell/5058" target="_blank">📅 23:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
آموزش صفر تا صد + دانلود مستقیم mhrv-rs (تونل رایگان گوگل) - نسخه v1.9.28
---
رفقا سلام!
✋
برای اینکه گیج نشید، تو این پست کل معرفی، آموزش راه‌اندازی و لینک‌های دانلود آپدیت جدیدِ این ابزار شاهکار رو یک‌جا براتون جمع کردیم.
🔥
این ابزار چیه؟
یک برنامه به‌شدت سبک (بدون نیاز به سرور مجازی) که اینترنت آزاد رو کاملاً رایگان براتون فراهم می‌کنه. با این روش، سیستم فیلترینگ (DPI) فقط می‌بینه که شما در حال تبادل دیتا با سایت
www.google.com
هستید، در حالی که اسکریپت مخفیِ شما تو سرورهای گوگل داره سایت‌های فیلترشده رو براتون باز می‌کنه و از یه تونل امن به دستتون می‌رسونه!
⚡️
تغییرات آپدیت جدید (v1.9.28):
🔸
سرعت انفجاری با
Pipelining
: درخواست‌ها موازی ارسال می‌شن تا سرعت باز کردن صفحات به طرز چشمگیری بره بالا.
🔸
رفع مشکل تماس‌ها: با مسدود کردن پورت‌های UDP، مشکل وصل نشدن یا تاخیر تو تماس‌های واتس‌اپ، دیسکورد و گوگل‌میت حل شده.
🛠
آموزش راه‌اندازی سریع (فقط ۳ مرحله):
1️⃣
ساخت اسکریپت (فقط یک‌بار):
• با جیمیلتون برید به سایت
script.google.com
و روی New Project کلیک کنید. کدهای پیش‌فرض رو پاک کنید.
• کدهای فایل
Code.gs
(از گیت‌هاب پروژه) رو کپی و اونجا پیست کنید.
• خط
const AUTH_KEY = "CHANGE_ME..."
رو پیدا کنید و به جای
CHANGE_ME...
یه رمز سخت برای خودتون بذارید.
• دکمه Deploy (بالا راست) ➔ New deployment رو بزنید. از آیکون
⚙️
نوعش رو بذارید Web app. فیلد Who has access رو روی Anyone بذارید و Deploy کنید.
• کد طولانیِ Deployment ID که بهتون می‌ده رو کپی کنید.
2️⃣
اجرای برنامه:
• برنامه رو از لینک‌های پایین دانلود و نصب کنید.
• تو محیط برنامه، همون Deployment ID و رمزی (Auth key) که ساختید رو وارد کنید.
• روی Save config و بعد Start بزنید تا دایره وضعیت سبز بشه.
3️⃣
اتصال:
• حالا کافیه پروکسی گوشی یا سیستمتون رو روی آی‌پی
127.0.0.1
و پورت 8085 تنظیم کنید. تمام! اینترنت آزاده.
⚠️
نکات مهم: گوگل روزی ۲۰ هزار درخواست خروجی رایگان می‌ده که برای وب‌گردی یک نفر کاملاً کافیه. (سایت یوتیوب باز می‌شه اما ویدیوهاش پخش نمی‌شن چون گوگل دسترسی اسکریپت به سرورهای ویدیوش رو بسته).
📥
لینک‌های دانلود مستقیم برای اندروید (نسخه v1.9.28):
📱
نسخه arm64-v8a (مخصوص اکثر گوشی‌های جدید - پیشنهاد اول):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/download/v1.9.28/mhrv-rs-android-arm64-v8a-v1.9.28.apk
📱
نسخه armeabi-v7a (مخصوص گوشی‌های قدیمی‌تر):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/download/v1.9.28/mhrv-rs-android-armeabi-v7a-v1.9.28.apk
📱
نسخه Universal (اگر نمی‌دونید پردازنده گوشیتون چیه اینو دانلود کنید، روی همه نصب می‌شه):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/download/v1.9.28/mhrv-rs-android-universal-v1.9.28.apk
📌
#آموزش
#گوگل
#بدون_سرور
#نت_ملی
#تونل
#رایگان
#mhrv_rs
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/archivetell/5056" target="_blank">📅 23:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">لینک داخلی جدید یونیورسال مناسب همه گوشیا
🌟
❤️‍🔥
دانلود</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5055" target="_blank">📅 23:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">امروز دوباره از ساعت 6 اینا یه جمعیتی رفتن سروش و روبیکا مثل اینکه
🌟</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5054" target="_blank">📅 23:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">XuiFactor
ابزار لینوکسی برای اعمال ضریب مصرف روی کاربران 3x-ui
بدون نیاز به نصب:
sqlite3
python
یا ابزار اضافه
بدون تغییر در سورس پنل 3x-ui
فایل ریلیز مناسب سرور را با گوشی بگیرید و با Termius یا SFTP بفرستید روی سرور.
نصب روی سرورهای معمولی amd64
tar -xzf xui-factor_v0.1.0-beta_linux_amd64.tar.gz
cd xui-factor_v0.1.0-beta_linux_amd64
sudo ./scripts/install.sh
sudo systemctl enable --now xui-factor.service
چک سلامت برنامه
xui-factor doctor
بکاپ قبل از تغییرات
xui-factor backup
اعمال ضریب روی یک کاربر خاص
xui-factor enable --email USER_EMAIL --inbound-id 1 --factor 1.2
مثال:
xui-factor enable --email User --inbound-id 1 --factor 1.2
یعنی اگر کاربر ۱۰ گیگ مصرف واقعی داشته باشد، داخل پنل حدود ۱۲ گیگ ثبت می‌شود.
اعمال ضریب روی تمام کاربران یک inbound مشخص
xui-factor enable-all --inbound-id 1 --factor 1.2
اعمال ضریب فقط روی کاربران حجم‌دار همان inbound
xui-factor enable-all --inbound-id 1 --factor 1.2 --limited-only
دیدن وضعیت Rule ها
xui-factor status
دیدن گزارش یک کاربر
xui-factor audit --email User --inbound-id 1
حذف ضریب از یک کاربر
xui-factor disable --email User --inbound-id 1
حذف ضریب از همه کاربران
xui-factor disable-all
نکته مهم
وقتی ضریب حذف می‌شود، مصرفی که قبلاً با ضریب ثبت شده باقی می‌ماند.
از آن لحظه به بعد، مصرف جدید کاربر عادی حساب می‌شود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5053" target="_blank">📅 22:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dT1har4LYSDyUGfh7lxrw0tZZkyaZ9gvzfW4WFJyP7QZFeWMAaLlpovB7qP6sGuCPrODzjH3rLgzPV669TKkPgIRklfDuqgmJGq2Qou1-HTmWIxRPldGmuJUsKu1tCPyWxGxFChngqAtsY74toy8K_EtpGfjRy-OvxBHSd98HiSZq1QKNPJG1yskAIXTSO6VVUMWQr50VHMImVn6G8Rx2m_EgSYN2dTF4Q24xi0_jmNi26wQ1jc6v_VIfbXP8id8gjwYMouGtsq3zl5Cx1YdNobzyV9q0taxeNGLo3P9aw3RDXeRPbFeFQofCRIFq1iJvW_dqf2LrW7jOZgrwboT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">XuiFactor
این پروژه یک ابزار لینوکسی برای اعمال ضریب مصرف روی ترافیک کاربران 3x-ui است که می‌تواند مصرف ثبت‌شده را برای یک کاربر خاص یا همه کاربران، به‌صورت کنترل‌شده و موقت افزایش دهد.
پروژه XuiFactor به‌عنوان یک sidecar کنار پنل 3x-ui اجرا می‌شود و بدون تغییر در سورس پنل، مصرف کاربران را از طریق دیتابیس SQLite خود 3x-ui مدیریت می‌کند. این ابزار با تمرکز روی کنترل دقیق‌تر مصرف، ruleهای قابل فعال‌سازی، توقف، ادامه و حذف ارائه می‌دهد؛ به‌طوری‌که پس از حذف ضریب، نتیجه‌های قبلی باقی می‌مانند و مصرف‌های بعدی به حالت عادی محاسبه می‌شوند.
این افزار برای اپراتورهایی ساخته شده که می‌خواهند بدون وابستگی به تغییرات داخلی پنل، روی مصرف کاربران ضریب اعمال کنند، وضعیت ruleها را بررسی کنند، از دیتابیس بکاپ بگیرند، audit داشته باشند و سرویس را به‌صورت پایدار با systemd روی سرورهای لینوکسی اجرا کنند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/5052" target="_blank">📅 22:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">@File_linkerobot
اینم بات خوبیه برای دانلود فایل با نت داخلی
توسعه دهنده از ممبرای عزیز کانال
@parsimq
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5051" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5050" target="_blank">📅 22:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوستان و دولوپر های عزیز، پروژه ای چیزی اوکی کردین و میخواین تو چنل بذاریم، پیام یا دایرکت بدین درخدمت هستم
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/5049" target="_blank">📅 22:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ArchiveTel
pinned «
🚀
آپدیت طوفانی MahsaNG (نسخه v16) منتشر شد!  ---  رفقا سلام!
✋
اگر دنبال یه فیلترشکن رایگان، غیرمتمرکز و ضد‌فیلتر می‌گردید، قطعاً مهسا‌ ان‌جی (MahsaNG) یکی از بهترین انتخاب‌هاست.   برای کسانی که نمی‌دونن: مهسا ان‌جی یک کلاینت بر پایه v2rayNG هست که با جمع‌آوری…
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5048" target="_blank">📅 22:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MahsaNG_16_universal.apk</div>
  <div class="tg-doc-extra">172.3 MB</div>
</div>
<a href="https://t.me/archivetell/5045" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی یونیورسال مناسب همه گوشیا نیم بها
🌟
❤️‍🔥</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5045" target="_blank">📅 22:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
آپدیت طوفانی MahsaNG (نسخه v16) منتشر شد!
---
رفقا سلام!
✋
اگر دنبال یه فیلترشکن رایگان، غیرمتمرکز و ضد‌فیلتر می‌گردید، قطعاً مهسا‌ ان‌جی (MahsaNG) یکی از بهترین انتخاب‌هاست.
برای کسانی که نمی‌دونن: مهسا ان‌جی یک کلاینت بر پایه v2rayNG هست که با جمع‌آوری کانفیگ‌های اهدایی از سراسر دنیا و توزیع هوشمندشون بین کاربرا، یه شبکه آزاد و رایگان ساخته.
✨
تو آپدیت جدید (نسخه 16) چه خبره؟
🔸
اضافه شدن اتصال مستقل سایفون (Psiphon-alone): حالا می‌تونید سایفون رو بدون نیاز به هیچ کانفیگ V2ray اجرا کنید!
🔸
دامین فرانتینگ سایفون (Psiphon CDN-Fronting): همون متد خفنی که این روزها برای دور زدن نت ملی عالی جواب میده، الان مستقیم تو مهسا ان‌جی پیاده شده.
🔸
اشتراک‌گذاری شبکه (Psiphon LAN sharing): نت آزاد سایفون رو راحت به ویندوز یا بقیه دستگاه‌ها شیر کنید.
🔸
اضافه شدن موتورهای جدید MasterDNS، GooseRelay و FlowDriver برای بای‌پس بهترِ فیلترینگ.
🔸
شافل (تغییر تصادفی) آی‌پی‌ها در اسکنر DNS و رفع باگ‌های کرش برنامه.
📥
لینک‌های دانلود مستقیم:
با توجه به مدل گوشیتون روی یکی از لینک‌های زیر بزنید تا مستقیم دانلود بشه:
📱
نسخه arm64-v8a (مخصوص اکثر گوشی‌های جدید - پیشنهاد اول):
🔗
https://github.com/GFW-knocker/MahsaNG/releases/download/v16-(1405-2-25)/MahsaNG_16_arm64-v8a.apk
📱
نسخه armeabi-v7a (مخصوص گوشی‌های قدیمی‌تر):
🔗
https://github.com/GFW-knocker/MahsaNG/releases/download/v16-(1405-2-25)/MahsaNG_16_armeabi-v7a.apk
📱
نسخه Universal (حجم بالا - اگر نمی‌دونید پردازنده گوشیتون چیه اینو دانلود کنید، روی همه نصب می‌شه):
🔗
https://github.com/GFW-knocker/MahsaNG/releases/download/v16-(1405-2-25)/MahsaNG_16_universal.apk
لینک داخلی یونیورسال مناسب همه گوشیا نیم بها
🌟
❤️‍🔥
📌
#آپدیت
#مهسا_ان_جی
#سایفون
#دامین_فرانتینگ
#رایگان
#MahsaNG
#v2ray
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/archivetell/5042" target="_blank">📅 22:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شیر و خورشید همراه اول
185.200.232.43
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5041" target="_blank">📅 22:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ساب V2ray, Exclave
ایمپورت کنید و تست پینگ بگیرین
با شکن و بی شکن تست بگیرین
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/sub/new-sub.txt
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5040" target="_blank">📅 21:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شیر و خورشید ایرانسل
96.17.207.142
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5039" target="_blank">📅 20:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #25</div>
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
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/5037" target="_blank">📅 19:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvXHbT0bTfI1jiysPxOt0aZfTxlkMDjfcVQdvMdBJi2Us3G7WC1l7uRG54CrkpOob4zRdW5AIIwcm4M3n5kWsxDJu-qYbMYVJ-1g-Ww5IORCbRuECtQCPHbXTqWSJfcyklnuUDL9maWZOArtC0QbpWjAkAZxomozVkiYTLXyS2O4pBek0CYNkinns8JeUBlk_O5_aGHt6EFK-okgHo2b67P9fF8ZuZcp6jf79smyvT4ZCeGmda_nLHeFjhDJV4JkkhPfHAae2E4E_zhU7zFMGszI6-pcSkFzcL-zk5WBzMOCUw957OhDxWGhjG4SZqns6L3BNRkb6gDA1wcCwJs95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXqPnuKkYMb_m9TuiP3_NJTi2d342mOoBjcY6s4nIM8yx80O__8EaK-LGfI6U1DowMEb2PoKKoZ5oPaTFwkHopTDkCTbLXRpvjfQLqkwCOK98dbWZxpkwgmZ4sS534bHKGqWSJbwDKkhcrDjMUTFttOWW_OHJMq58Z14UXSXIgfwCHPRo-hlL6PVbYEmP4fmtxUIqnc9LWZd466NDqXvDzSTKLa4xqAMx8XJgE_hr0RC4wkfwzXcTYNcRKmCVmjDaYFFI2tY3w_iyKxxYhsnntr7qZPWfHC-WvfUbfclbFazCbrs0mlVAyJkeXttKfiBtB4mtwbcpIRqY7WLVF1yHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5035" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">لینک داخلی شیر و خورشید
دانلود
Pass :
@ArchiveTell
انقضا :
۲
روز دیگه</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5034" target="_blank">📅 18:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBehnam's Folder(BehNam)</strong></div>
<div class="tg-text">نسخه ی 1.3.8 پروژه ی XHTTPRelayECO ورسل منتشر شد
🔥
یه آپدیت ریز زدم. مود های Fast Pipe آپدیت و بهینه شده.
در حال حاظر با دیپلوی مجدد روی توکن Pro Trial تست گرفتم و جواب داده.
تست کنید و نتیجه رو اعلام کنید
❤️
روی اینترنت های مختلف تست کنید
https://github.com/B3hnamR/XHTTPRelayECO/releases/tag/1.3.8</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5032" target="_blank">📅 18:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5031" target="_blank">📅 18:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">scanner.zip</div>
  <div class="tg-doc-extra">8.5 KB</div>
</div>
<a href="https://t.me/archivetell/5030" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5030" target="_blank">📅 17:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5029" target="_blank">📅 17:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5028" target="_blank">📅 16:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پروژه خیلی خفنیه
https://github.com/Code-Leafy/G2rayXCodeLeafy
فورک کنید رو گیتهابتون
Codespaces
ران کنید
صبر کنید اماده که شد 1 بزنید کانفیگ رو دریافت کنید</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5027" target="_blank">📅 16:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">و اینکه سامانتل بدون آیپی شیر و خورشید وصله..</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5025" target="_blank">📅 16:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">و اینکه سامانتل بدون آیپی شیر و خورشید وصله..</div>
<div class="tg-footer">👁️ 708 · <a href="https://t.me/archivetell/5024" target="_blank">📅 16:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/archivetell/5023" target="_blank">📅 15:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.html</div>
  <div class="tg-doc-extra">21.4 KB</div>
</div>
<a href="https://t.me/archivetell/5022" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر آیپی های شیر و خورشید</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/5022" target="_blank">📅 15:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">لینک داخلی شیر و خورشید ، دو تا آپلودسنتر
دانلود
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/archivetell/5021" target="_blank">📅 12:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/archivetell/5020" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5019" target="_blank">📅 12:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5018" target="_blank">📅 11:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شیر و خورشید ایرانسل
92.122.123.128,2.19.204.87,2.19.204.137,2.19.204.144,2.19.204.145,2.19.204.170,2.19.204.184,2.19.204.185,2.19.204.202,2.19.204.210</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/5017" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3I5kUh0kcvoHeMiexiPdfJC4_by9jKmHjDtlRKtUT2MB8SJoN6lmfKeCZ73nIcUO1tNqLpRKkQSprO-DHzFJbig92nHRhX4YO8ujzhT3cB_gEpfBfNBuoqkj1x6ikyOY4mVNI3ByKhhvoWmV0s1kYZjkSvkGO8_VtpgIwFpP7ZAq5zYDHVaZuD1vuIKYmiKEenZkA4wu7jt4oR1rfUNAKMoAIQR-dkitNU56sym6iUxe94o4LToIgiORcKEn5FhFTtC8oxrMHeYdMJWFu8clMGtjXN3GtjKpLXfKnAFTPt5hA1GfkjMfFvd9TYh5oH_hIQm1vI2J7qiC-Kue9rY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت:</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5016" target="_blank">📅 11:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شیر و خورشید
مخابرات
2.17.101.191
2.17.101.188
2.17.101.187
2.23.168.254
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/5015" target="_blank">📅 11:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/5014" target="_blank">📅 10:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh0-FGGgDL4-79RXq4cBvQgCrnxqLHfJyJPQnDr2swNJnVln0s00ghBqfx1pAEg75LAfQdJS0k2Jezw6kBW9OnkgGCRNVLUiuzEqY63mndZ19VgfPd_DKGsvCmruy5ijW9aKP48ZwHsXFMdcBahlyVk_m0weffmHBvsa7dKZbpcz9ALXC3NXj2Jj_YRhWvqyC4b3yw5x1NlyJStCjWBbA56tFu5YXgfku7xX6Bdb8-DLw5u26SzrYLQ85L77Y4tRTYqVcwXtF9LM-yYcR65wsQ_0fQNhD2uxgp3ObkDkuyyDx5yw8O4sfuhc9e7IC9cmiZ7zTxkfsa2ypbh_x2vpQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0415430ff6.mp4?token=XwJknpUsC-N03nj14Hap0Jdc3VUSOB5k3ngx8LH4W0LYyX2-UdtOdAYm5ok6PZOgA2H2gFfeBByjAHWG_2CR1MGLwRQpaapFmvK2SJ0S0ZfKNJhHCxKv9j-HwEnYTOrR9RD7FeFpvjRY70HTkzhJj_OTScd_Pt5dOtGGu6zNw7Un43QfiBZJqUqqfkt52wKOIVA9p8uYcnTE8UsMhZeWOJNmfLKNI4PC5OrRJVE_GexEl2wmdfaQbv3rAnZQUl5IjZcJwBHFTfhqVlBkFlOzIvVo6lTBs-sSjXBnWc_peS8gEdG4U7ZcbUo_P-ExeNj8Y4Qb-aT_JMmE4Z1Tl4_ubaTFwhRPUCHOCu7bqOKDtUcjqwbKvnvPs3ocqMbs1iNz8xKpRBalXwrLRfxuUxzVHPjTtcxBEEsDBJB0tGzjCj2QIPDLoy5uHjQW63UgnAUE6vKdSu2LNHh-Y5Tf7nVKGqGH5wlbNFIuieCqnFFRN_8r1CGWgGZWQHvez3DECah0ZfkNNU105rbpMY3sAFdh8RTV7xK5xlFhrYQkT3zI1Zr08BgUq1nKlt_xe0ylQ4n2ZT5Z-2diJyGrPFBd8-Eml53oc9SnSfRsfW3xrxVu0DeZA8R5RLHr1I8lsde9TtO_bcokWgPTflllwZEm2E9qTh87FLiFtxCqiClTXv57UEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0415430ff6.mp4?token=XwJknpUsC-N03nj14Hap0Jdc3VUSOB5k3ngx8LH4W0LYyX2-UdtOdAYm5ok6PZOgA2H2gFfeBByjAHWG_2CR1MGLwRQpaapFmvK2SJ0S0ZfKNJhHCxKv9j-HwEnYTOrR9RD7FeFpvjRY70HTkzhJj_OTScd_Pt5dOtGGu6zNw7Un43QfiBZJqUqqfkt52wKOIVA9p8uYcnTE8UsMhZeWOJNmfLKNI4PC5OrRJVE_GexEl2wmdfaQbv3rAnZQUl5IjZcJwBHFTfhqVlBkFlOzIvVo6lTBs-sSjXBnWc_peS8gEdG4U7ZcbUo_P-ExeNj8Y4Qb-aT_JMmE4Z1Tl4_ubaTFwhRPUCHOCu7bqOKDtUcjqwbKvnvPs3ocqMbs1iNz8xKpRBalXwrLRfxuUxzVHPjTtcxBEEsDBJB0tGzjCj2QIPDLoy5uHjQW63UgnAUE6vKdSu2LNHh-Y5Tf7nVKGqGH5wlbNFIuieCqnFFRN_8r1CGWgGZWQHvez3DECah0ZfkNNU105rbpMY3sAFdh8RTV7xK5xlFhrYQkT3zI1Zr08BgUq1nKlt_xe0ylQ4n2ZT5Z-2diJyGrPFBd8-Eml53oc9SnSfRsfW3xrxVu0DeZA8R5RLHr1I8lsde9TtO_bcokWgPTflllwZEm2E9qTh87FLiFtxCqiClTXv57UEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Gemini Intelligence For Android
شرکت گوگل در کنفرانس I/O 2026، ابزارهای هوش مصنوعی جدیدی را برای خودکارسازی وظایف در دستگاه‌های تلفن همراه معرفی نمود. این قابلیت‌ها شامل موارد زیر می‌باشند:
• خودکارسازی فرآیندهای چندمرحله‌ای (از جمله رزرو سفر و انتقال لیست‌ها از برنامه یادداشت‌برداری به سبد خرید فروشگاه‌ها)
• ارائه خلاصه‌ای از صفحات وب و تکمیل خودکار فرم‌ها در مرورگر کروم
• تبدیل گفتار به متن ساختاریافته در کیبورد Gboard (با استفاده از ابزار Rambler و پشتیبانی از چندین زبان)
• ایجاد ویجت‌های سفارشی دسکتاپ بر اساس ورودی متنی (قابلیت Create My Widget)
اولین دستگاه‌های سازگار با این فناوری، گوشی‌های سامسونگ گلکسی S26 و گوگل پیکسل 10 می‌باشند که در فصل تابستان عرضه خواهند شد. تا پایان سال جاری، این قابلیت‌ها به ساعت‌های هوشمند، رایانه‌های شخصی، هدست‌ها و سیستم‌های رسانه‌ای خودرو نیز گسترش خواهند یافت.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5007" target="_blank">📅 09:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOgxeBzmAeEBg9m9G5aSf-A3acZI2woaS7Kb0MKAcqEWNno8pS-JUH1xMV7J28Laeu9g6EIPK1qYG5k_y8RwVZrdTjTrvS1I4zDSYUWzVDQAnBkcfTs6P32ThL23Ua6joQoYG4H6RLPDebTI7gNkF3L6x14wx1oznunP0JMCPdnJQbrAzh0m7Ovz6TXmQjJ7gp_F2E1BBfv3RjY0-5ZDLFqStLJKszZeqOAoDhmotd1oV0vXNTXluo6uBVubaFQZoxZekVxIZ0ebkCgB8vDq-ya9oAOI-0fFyMc2ND8lDUsU-lDpgojYIHkQfwGQcqNQoVnmEtZ9opk4B8_NbOXdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhatModels
ماشین حساب آنلاین برای انتخاب مدل‌های هوش مصنوعی متناسب با سخت‌افزار شما
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/5006" target="_blank">📅 08:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">لینک داخلی شیر و خورشید ، دو تا آپلودسنتر
دانلود
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/archivetell/5005" target="_blank">📅 03:07 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
