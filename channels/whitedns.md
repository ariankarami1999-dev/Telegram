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
<img src="https://cdn4.telesco.pe/file/e0oXxnGQZ1JtbKA7yeTx9UVsYnGGzRs7MXa1RuzfBmUNn8lqeXtebqFsJU26PwFJ4duPnWCkToL2Ip0_Ndfih5B53pmr_2wmH4cwl44nK4VwEe1ap0rd2sCuB9xxF-PSzF5MKu6VSK-2EQRoqnBhhJXTmIXKUQm2K1ZvqMoJ1EzVbpUlqB-8vc84HIPu7bu1IM61nJ8pxrhFACFm3A7c1BW7TKoDXW-AkU0hLkhWACTFER8T2J6IH6n3UZWHL4jVRskxB7tcN0JLv-fNdGhrflMx38ZLSEf-F3xcqVaowMwJo3l6JAZMQB8nvbiLO1bUKkn944LzGTqR5GRUhvE12g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhisperInHeaven</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-947">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">👥
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/947" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-946">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-poll">
<h4>📊 "موقت"الان با چی وصل هستید ؟</h4>
<ul>
<li>✓ با روش های مبتنی در dns , مثل masterdns</li>
<li>✓ روش های مستقیم مثل vless</li>
<li>✓ psiphon , tor , .....</li>
</ul>
</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/946" target="_blank">📅 10:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-945">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از کاربر های گروه لطف کرده یک ویدیو خیلی کامل و خودمونی از نحوه استفاده از اپ WhiteDNS  درست کرده.
پیشنهاد میکنم تا وضعیت مناسبه دانلودش کنید.
ممنون از همراهی شما
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/945" target="_blank">📅 07:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-940">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/940" target="_blank">📅 05:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاوید نامان ایران(Bamdad)</strong></div>
<div class="tg-text">#کانفیگ
#دی_ان_اس
#وایت_دی_ان_اس
#مستر_دی_ان_اس
انکریپشن کی:
aaf4b6-@JavidnamanIran-aaf4b6fff
c.namad.xyz
c.irdmc.com
c.bamak.xyz
c.javidnaman.com
c.jnir.my
c.igoii.org</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/939" target="_blank">📅 05:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ابزار WhiteDNS  برای ساده‌تر کردن راه‌اندازی و مدیریت سرورهای شخصی،  با نام  WhiteDNS Wizard آماده شده است.  هدف WhiteDNS این است که کاربران بتوانند بدون نیاز به دانش فنی درباره تنظیمات سرور، DNS، اینباندها، اوتباندها، گواهی‌ها و پنل‌های مدیریتی، سرور خود…</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/whitedns/938" target="_blank">📅 09:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سلام خدمت دوستان عزیز،  ما سرورها رو آپدیت کردیم و با همکاری جدیدی که شروع شده، از این به بعد ساب‌ها رو مرتب با کانکشن‌های جدید و تازه‌تر رفرش می‌کنیم تا کیفیت اتصال بهتر و پایدارتر بشه.  اگر این دامنه‌ها هم فیلتر بشن، لینک‌های جدید ساب رو براتون می‌سازیم…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/whitedns/937" target="_blank">📅 09:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سلام به همه دوستان عزیز
در حال حاضر گروه ما هدف یک‌سری حملات از سوی ربات‌ها و برخی افراد مخرب قرار گرفته است. این حساب‌ها در حال ارسال تصاویر و ویدئوهای نامناسب و پورنوگرافی هستند.
تیم WhiteDNS به‌صورت مستمر در حال مانیتور کردن گروه، شناسایی و مسدودسازی این حساب‌ها و ربات‌ها است تا محیط گروه برای همه اعضا امن و مناسب باقی بماند.
از صبر و همکاری شما سپاسگزاریم.
با احترام
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/whitedns/936" target="_blank">📅 17:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سلام خدمت دوستان عزیز،  ما سرورها رو آپدیت کردیم و با همکاری جدیدی که شروع شده، از این به بعد ساب‌ها رو مرتب با کانکشن‌های جدید و تازه‌تر رفرش می‌کنیم تا کیفیت اتصال بهتر و پایدارتر بشه.  اگر این دامنه‌ها هم فیلتر بشن، لینک‌های جدید ساب رو براتون می‌سازیم…</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/whitedns/935" target="_blank">📅 08:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRedvnALYNHo36YMJnQ4uaYWIjm2TXeAOlEJYOVuh_fwL2Ic_GlqPSgR9J3AU-CMemfsyZcYCnsb22uAOKeLugSTJ7htUm3kDJ6iNywaVk9ezbxOoVD81jGk8J1-r1x2YfZQS24gU8SmQvmaujKwdlhjUT8CO9f70w-FV3zBI96WS6SptCyGzZjVQCy309f8bDVwcyc_IzX6D80PMwqJuPcWt5QCNPxAoDBauwvdapnDrf7qCh1WJ51pRbmp3zA4SWVUgec2JqD3ts-TxKfrldHxvXF3m8uIqddwm9nEe51ZURncigd42Y_jyYhXEmDBocib7vy6Sv1_glwmTomYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار WhiteDNS  برای ساده‌تر کردن راه‌اندازی و مدیریت سرورهای شخصی،  با نام  WhiteDNS Wizard آماده شده است.
هدف WhiteDNS این است که کاربران بتوانند بدون نیاز به دانش فنی درباره تنظیمات سرور، DNS، اینباندها، اوتباندها، گواهی‌ها و پنل‌های مدیریتی، سرور خود را به صورت خودکار و یکپارچه آماده استفاده کنند.
با این ابزار کافی است اطلاعات اولیه مثل دامنه، سرور و دسترسی Cloudflare را وارد کنید. WhiteDNS به صورت خودکار رکوردهای DNS را تنظیم می‌کند، ساختار مورد نیاز روی سرور را آماده می‌کند، اینباندها و اوتباندهای لازم را می‌سازد، گواهی‌های مورد نیاز را مدیریت می‌کند و در پایان لینک‌های اتصال آماده را در اختیار شما قرار می‌دهد.
تمام مراحل به شکلی طراحی شده‌اند که کاربر نیازی به درگیر شدن با جزئیات پیچیده کانفیگ سرور نداشته باشد. هدف ما این است که راه‌اندازی یک سرور شخصی، از مرحله اتصال دامنه تا دریافت کانفیگ‌های نهایی، تا حد ممکن ساده، سریع و قابل فهم شود.
WhiteDNS برای کسانی ساخته شده که می‌خواهند کنترل سرور خودشان را داشته باشند، اما نمی‌خواهند زمان زیادی صرف یادگیری تنظیمات فنی، خطاهای رایج، مدیریت DNS یا ساخت دستی کانفیگ‌ها کنند.
این پروژه قدمی دیگر در مسیر ما برای آسان‌تر کردن دسترسی به ابزارهای کاربردی، مستقل و قابل مدیریت برای کاربران است.
https://github.com/iampedii/WhiteDNS-Wizard/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/whitedns/934" target="_blank">📅 19:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سلام خدمت دوستان عزیز،
ما سرورها رو آپدیت کردیم و با همکاری جدیدی که شروع شده، از این به بعد ساب‌ها رو مرتب با کانکشن‌های جدید و تازه‌تر رفرش می‌کنیم تا کیفیت اتصال بهتر و پایدارتر بشه.
اگر این دامنه‌ها هم فیلتر بشن، لینک‌های جدید ساب رو براتون می‌سازیم و منتشر می‌کنیم.
لطفاً این لینک‌ها رو تست کنید و نتیجه رو در کامنت‌ها بگید. اگر لینکی فیلتر بود یا مشکل داشت، اطلاع بدید تا جایگزین کنیم.
لینک ساب برای Clash Party / Mi Clash / FLClash:
https://sub.iampedi4.live/sub/mihomo.yaml
لینک ساب برای اپ‌های V2Ray:
https://sub.iampedi4.live/sub/base64.txt
آموزش استفاده از FlClash
آموزش استفاده از Clash Party
ممنون از همراهی شما
🤍
محتوای همه‌ی ساب‌ها یکی هست و فقط دامنه‌های جدید اضافه شده‌اند، چون دامنه‌ی قبلی فیلتر شده بود.
ساب گیتهاب فعلا آپدیت نخواهد شد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/whitedns/933" target="_blank">📅 18:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستان عزیز WhiteDNS
🔥
اگر از WhiteDNS Sub استفاده می‌کنید و اخیراً احساس کردید کیفیت بعضی از کانکشن‌ها افت کرده، لطفاً بدونید که موضوع در حال پیگیریه.
ما در حال بررسی و بهبود وضعیت کانکشن‌ها هستیم و به‌زودی یک کانفیگ های بروز رو منتشر می‌کنیم.
خوشبختانه همکار هایی پیدا کردیم که می‌توانند در این مسیر کنار ما باشند و کمک کنند تا کیفیت و پایداری سرویس بهتر باشه.
به‌زودی آپدیت جدید روی Subscription قرار می‌گیره و اطلاع‌رسانی می‌کنیم.
ممنون از صبر، همراهی و حمایت همیشگی‌تون
🤍
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/whitedns/932" target="_blank">📅 14:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در ادامه فیلتر شدن دامنه ما، دامنه جدید برای ساب آماده کردیم.
محتوی همه ساب ها یکی هستش، فقط دامنه جدید اضافه کردیم چون قبلی فیلتر شده.
تا فردا هم فیلتر کنن
(
🖕
)
ما لینک ساب جدید میسازیم  براتون
لطفا این رو تست کنید و نتیجه رو در کامنت ها بگید. اگر فیلتر بود یکی دیگه میسازیم.
🔥
لینک ساب جدید
https://sub.iampedi2.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/whitedns/931" target="_blank">📅 05:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان و همراهان عزیز، سلام
🌺
لطفاً چند لحظه وقت بگذارید و این پیام مهم را در خصوص
نحوه ارتباط با ادمین‌ها
مطالعه کنید.
آیدی ادمین که در توضیحات (بایو) کانال قرار داده شده،
فقط و فقط
برای موارد خاص زیر است:
🔸
گزارش تخلفات
🔸
پیشنهادات همکاری در زمینه‌های مختلف
⚠️
لطفاً به این نکات توجه ویژه داشته باشید:
۱.
سوالات خود را در گروه بپرسید:
تمامی سوالات و مشکلات فنی باید فقط در
گروه‌های ما
مطرح شوند. لطفاً از ارسال پیام خصوصی (پی‌وی) به ادمین‌ها خودداری کنید. ما تیم پشتیبانی مجزایی نداریم که بتواند روزانه به صدها پیام خصوصی به‌صورت تک‌به‌تک پاسخ دهد.
۲.
توقع پاسخگویی در موارد نامربوط:
متاسفانه روزانه پیام‌های بی‌ربط زیادی دریافت می‌کنیم و در کمال تعجب، برخی از دوستان در صورت عدم دریافت پاسخ شاکی شده و حتی تهدید می‌کنند!
برای روشن شدن موضوع، به طور مثال
موارد زیر در تخصص ما نیست
و از پاسخگویی به آن‌ها در پیام خصوصی معذوریم:
❌
رفع مشکلات کامپیوتر، موبایل و یا خرابی مودم خانگی شما (برای این موارد به متخصصین شهر خود مراجعه کنید).
❌
مشاوره برای خرید تجهیزات سخت‌افزاری (مثل قطعی کابل شبکه و اینکه چه کابلی بخرید).
❌
آموزش خرید رمزارز و معرفی صرافی‌های مناسب.
❌
و هزاران مورد نامربوط دیگر که خارج از حوزه فعالیت ماست.
🙏
خواهشمندیم با رعایت این موارد، از ارسال پیام‌های خارج از موضوع به ادمین‌ها جداً خودداری فرمایید تا بتوانیم در موارد ضروری پاسخگوی شما عزیزان باشیم.
از درک و همراهی شما سپاسگزاریم
🌹</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/whitedns/929" target="_blank">📅 16:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⚠️
⚠️
⚠️
#موقت
⚠️
هر پیام اضافه، سؤال، بحث یا محتوایی غیر از نام سرور زیر این پست، باعث بن شدن خواهد شد.   سلام به همه دوستان عزیز  برای بررسی وضعیت اتصال، نیاز داریم یک تست همگانی انجام بدیم تا مشخص بشه در حال حاضر کدام متدها و سرورها برای شما وصل هستند. …</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/whitedns/927" target="_blank">📅 08:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⚠️
⚠️
⚠️
#موقت
⚠️
هر پیام اضافه، سؤال، بحث یا محتوایی غیر از نام سرور زیر این پست، باعث بن شدن خواهد شد.
سلام به همه دوستان عزیز
برای بررسی وضعیت اتصال، نیاز داریم یک تست همگانی انجام بدیم تا مشخص بشه در حال حاضر کدام متدها و سرورها برای شما وصل هستند.
لطفاً قبل از تست، ساب خودتون رو یک‌بار Refresh / Update کنید.
برای شرکت در این تست:
به سابسکریپشن WhiteDNS وصل باشید.
داخل اپلیکیشن موبایل یا کامپیوتر وارد بخش Logs / لاگ‌ها شوید.
نام سروری که به آن وصل شده‌اید را زیر همین پست برای ما ارسال کنید.
لطفاً فقط نام سرور را ارسال کنید.
اگر نمی‌دانید دقیقاً باید چه کاری انجام دهید، مشکلی نیست؛ می‌توانید در این تست شرکت نکنید.
ممنون از همکاری شما
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/whitedns/926" target="_blank">📅 07:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لینک ساب ها درست شدند
😃
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/whitedns/925" target="_blank">📅 04:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">متأسفانه سروری که برای اسکن و بررسی کانفیگ‌ها استفاده می‌کردیم، به‌دلیل حجم بالای اسکن‌ها، از سمت ارائه‌دهنده به‌عنوان رفتار مشکوک یا سوءاستفاده شناسایی شده و دسترسی آن محدود شده است
😣
در حال بررسی و رفع مشکل هستیم و تلاش می‌کنیم سرویس اسکن را هرچه زودتر دوباره پایدار کنیم.
تا زمانی که این مشکل برطرف شود، می‌توانید از ساب‌های GitHub استفاده کنید؛ اما فعلاً امکان ارسال آپدیت‌های جدید از سمت ما وجود ندارد.
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/whitedns/923" target="_blank">📅 17:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تیم WhiteDNS از ابتدا با هدف کمک به کاربران فعالیت کرده و تمام خدماتی که ارائه داده‌ایم، رایگان بوده و رایگان باقی خواهد ماند.
در این مسیر سخت، تعدادی از شما عزیزان با کمک‌های مالی خود از ما حمایت کرده‌اید. چه کمک‌های کوچک و چه مبالغ بزرگ‌تر، برای ما بسیار ارزشمند بوده و واقعاً دلگرم‌کننده است. همین حمایت‌ها نشان می‌دهد که این مسیر برای خیلی‌ها مهم است و ما بابت این همراهی صمیمانه از شما سپاسگزاریم.
مبلغ کل حمایت از ما تاحالا حدود ۵۰دلار بوده است.
متأسفانه اخیراً کیف پولی که برای دریافت کمک‌ها استفاده می‌کردیم، شروع به مسدود کردن یا محدود کردن تراکنش‌های مربوط به ایران کرده است.
به همین دلیل، از شما خواهش می‌کنیم تا زمانی که راه‌حل امن و مناسبی پیدا کنیم، فعلاً برای ارسال کمک مالی اقدام نکنید.
قدردان محبت، اعتماد و حمایت ارزشمند شما هستیم.
با سپاس فراوان
تیم whiteDNS</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/whitedns/921" target="_blank">📅 16:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔥
اگر محتوای WhiteDNS برای شما مفید بوده، با Subscribe کردن کانال یوتیوب ما می‌توانید از ادامه فعالیت‌های ما حمایت کنید
.
https://youtube.com/@whitedns</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/920" target="_blank">📅 15:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-917">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/917" target="_blank">📅 11:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستان نگران نباشید، ما ۱۰۰۰ تا دامنه خریدیم این مدت برای سرویس های DNSTT & MasterDNS
تا فردا هم فیلتر کنن
(
🖕
)
ما لینک ساب جدید میسازیم  براتون
لطفا این رو تست کنید و نتیجه رو در کامنت ها بگید. اگر فیلتر بود یکی دیگه میسازیم.
لینک ساب جدید
http://sub.iampedi1.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
نکته، تمام آدرس های قبل کار خواهند کرد. ساب گیتهاب و تمام این ساب ها و ساب های آینده یک محتوی خواهند داشت.</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/whitedns/916" target="_blank">📅 11:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📌
چند نکته کاربردی برای بهتر وصل شدن با FlClash در اندروید
یکی از کاربران WhiteDNS تجربه‌ی شخصی خودش را از کار با FlClash فرستاده که برای اتصال بهتر مؤثر بوده.
اگر با FlClash مشکل اتصال، آپدیت نشدن ساب، پینگ‌های عجیب یا ناپایداری دارید، این موارد را امتحان کنید.
━━━━━━━━━━━━━━
1️⃣
بعد از نصب، قبل از اضافه کردن ساب، Resourceها را آپدیت کنید
بعد از نصب FlClash، قبل از اینکه لینک سابسکریپشن را اضافه کنید، وارد این بخش شوید:
Tools → Resource
و تمام Resourceها را آپدیت کنید.
⚠️
نکته مهم:
طبق تجربه‌ی بعضی کاربران، اگر اول لینک ساب را اضافه کنید، ممکن است بعداً Resourceها درست آپدیت نشوند یا اپ رفتار عجیب نشان بدهد.
━━━━━━━━━━━━━━
2️⃣
تنظیمات Network
از بخش Network این موارد را بررسی کنید:
✅
گزینه‌ی DNS Hijack را فعال کنید.
❌
گزینه‌ی
Allow applications to bypass VPN
را غیرفعال کنید.
این کار کمک می‌کند برنامه‌ها ترافیک یا DNS را از بیرون VPN رد نکنند.
━━━━━━━━━━━━━━
3️⃣
تنظیمات دسترسی و اجرای پس‌زمینه
بعد از نصب وارد این مسیر شوید:
Tools → Advanced Configuration → On Demand
در این بخش، گزینه‌های مربوط به دسترسی‌ها را روی Authorized قرار دهید.
همچنین در تنظیمات باتری گوشی، برای FlClash حالت Battery Optimization را غیرفعال کنید تا اندروید برنامه را در پس‌زمینه نبندد.
━━━━━━━━━━━━━━
4️⃣
گوشی روی Power Saving نباشد
اگر گوشی روی حالت
Power Saving / Battery
Saver باشد، ممکن است اتصال ناپایدار شود یا برنامه در پس‌زمینه قطع شود.
برای استفاده بهتر از FlClash، هنگام اتصال، حالت Power Saving را خاموش کنید.
━━━━━━━━━━━━━━
5️⃣
تنظیمات DNS
از بخش DNS:
✅
گزینه‌ی Override DNS را فعال کنید.
🌍
گزینه‌ی GeoIP Code را روی IR قرار دهید.
بعد از این تغییرات، لینک ساب را اضافه کنید و تست پینگ بگیرید.
━━━━━━━━━━━━━━
6️⃣
اگر ساب آپدیت نمی‌شود، حذف و دوباره اضافه کنید
طبق تجربه‌ی بعضی کاربران، FlClash گاهی نشان می‌دهد که ساب آپدیت شده، اما در عمل لیست کانفیگ‌ها تغییر نکرده است.
اگر حس کردید ساب درست آپدیت نشده:
1. لینک ساب را حذف کنید.
2. دوباره همان لینک را اضافه کنید.
3. مجدد پینگ بگیرید و تست اتصال انجام دهید.
━━━━━━━━━━━━━━
7️⃣
در تب Auto کمی صبر کنید
طبق تجربه‌ی کاربر، بعد از حذف و اضافه کردن دوباره‌ی ساب و گرفتن پینگ در تب Auto، ممکن است اول فقط چند سرور پینگ بدهند و بقیه Timeout شوند.
اما بعد از اولین اتصال، FlClash ممکن است خودش شروع کند سرورها را دوباره بررسی کند و از بالای لیست Auto دونه‌دونه سرورها را تست کند تا به گزینه‌ی بهتر برسد.
یعنی ممکن است اول یک سرور اصلاً پینگ ندهد یا در لیست بالا نباشد، اما بعد از اولین اتصال، همان سرور یا سرورهای دیگر دوباره تست شوند و وصل شوند.
⏳
گاهی این روند کمی زمان می‌برد، پس اگر همان لحظه همه‌چیز Timeout بود، چند دقیقه صبر کنید و دوباره وضعیت را بررسی کنید.
━━━━━━━━━━━━━━
8️⃣
مرتب‌سازی سرورها بر اساس پینگ
برای اینکه سرورهایی که پینگ گرفته‌اند بالای لیست بیایند، روی سه‌نقطه بزنید و وارد این مسیر شوید:
⋮ → Settings → Sort → Delay
با این کار، سرورهایی که پینگ بهتری دارند بالاتر نمایش داده می‌شوند و انتخاب سرور راحت‌تر می‌شود.
━━━━━━━━━━━━━━
✅
ترتیب پیشنهادی بعد از نصب FlClash
1. نصب FlClash
2. آپدیت Resourceها از بخش Tools → Resource
3. فعال کردن DNS Hijack
4. غیرفعال کردن Allow applications to bypass VPN
5. فعال کردن Override DNS
6. تنظیم GeoIP Code روی IR
7. غیرفعال کردن Battery Optimization برای FlClash
8. خاموش بودن Power Saving گوشی
9. اضافه کردن لینک ساب
10. رفتن به تب Auto و گرفتن پینگ
11. تنظیم Sort روی Delay
12. اتصال و چند دقیقه صبر برای تست خودکار سرورها
━━━━━━━━━━━━━━
⚠️
این تنظیمات تضمینی نیست، چون شرایط اینترنت، اپراتور و گوشی‌ها متفاوت است؛ اما برای بعضی کاربران باعث اتصال بهتر و پایدارتر شده است.
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/whitedns/915" target="_blank">📅 10:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69013b2789.mp4?token=RbsG753d5YybQ9AZ2HsQIerJCw0L4kx85wcR_sf4kOCVkwsPqZ2mpkfHg6j9xKGiMa_GFIn9VQfZl9ZgvF8isexOUIaZcTBAqT2XWRRMslH2l-HThjUEhY6A1mExOs_GYOED3dVIu4i5MyterXIP2XUAoA0zIPvBSgFIjYnNph8Q7ZX0z63PlQEw4iZ_UBF9QVDdLtF_T43e_yIqDXlXad-pxGtKinYMaBima9xXQA5s0IB6fTrNRa7oO-3LQl8QyRXjgUvChBjI2hPCeSH85rruPPRz43Gv7W_CVuNHQSUQLpaai55OMd-PiRbYIfKCtWzEhdlDBHHVmdHgmwrVAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69013b2789.mp4?token=RbsG753d5YybQ9AZ2HsQIerJCw0L4kx85wcR_sf4kOCVkwsPqZ2mpkfHg6j9xKGiMa_GFIn9VQfZl9ZgvF8isexOUIaZcTBAqT2XWRRMslH2l-HThjUEhY6A1mExOs_GYOED3dVIu4i5MyterXIP2XUAoA0zIPvBSgFIjYnNph8Q7ZX0z63PlQEw4iZ_UBF9QVDdLtF_T43e_yIqDXlXad-pxGtKinYMaBima9xXQA5s0IB6fTrNRa7oO-3LQl8QyRXjgUvChBjI2hPCeSH85rruPPRz43Gv7W_CVuNHQSUQLpaai55OMd-PiRbYIfKCtWzEhdlDBHHVmdHgmwrVAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آموزشی فعال سازی Fragment در اپلیکیشن V2Ray در موبایل و دستکتاپ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/whitedns/911" target="_blank">📅 02:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سلام خدمت همگی،
دوستانی که از همراه اول یا سایر اپراتورها استفاده می‌کنند و اخیراً با مشکل اتصال مواجه شده‌اند،
بر اساس تست‌های انجام‌شده، به نظر می‌رسد در روزهای اخیر روی برخی اپراتورها، از جمله همراه اول، DPI سنگین‌تری نسبت به قبل اعمال شده است.
به همین دلیل پیشنهاد می‌کنیم اگر با اتصال مشکل دارید، گزینه
Fragment
را در تنظیمات اپلیکیشن‌های زیر فعال کنید:
V2Ray
FlClash
Clash Party
Mi Clash
گزینه Fragment می‌تواند در بعضی شرایط به عبور از DPI و بهتر شدن اتصال کمک کند، مخصوصاً زمانی که اتصال روی برخی اپراتورها سخت‌تر شده یا کانفیگ‌ها دیر وصل می‌شوند.
اما توجه داشته باشید که فعال‌کردن Fragment همیشه به معنی افزایش سرعت نیست. در بعضی موارد ممکن است باعث کندتر شدن اتصال اولیه، افزایش جزئی پینگ، کاهش سرعت در بعضی کانفیگ‌ها، ناپایدار شدن برخی سرورها یا مصرف پردازشی و باتری کمی بیشتر در موبایل شود.
بنابراین پیشنهاد ما این است:
اگر اتصال شما مشکل دارد، کانفیگ‌ها وصل نمی‌شوند یا اتصال ناپایدار است، Fragment را فعال کنید و تست بگیرید.
اما اگر اتصال شما بدون مشکل و پایدار کار می‌کند، الزامی به فعال‌کردن Fragment نیست.
به‌زودی آموزش ویدیویی فعال‌سازی Fragment برای هرکدام از این اپلیکیشن ها ارسال میکنیم.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/whitedns/910" target="_blank">📅 02:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اپلیکیشن‌هایی مثل FlClash و Clash Mi چطور کار می‌کنند؟
اپلیکیشن‌هایی مثل
FlClash
در اندروید و
Clash Mi
در آیفون، برنامه‌هایی هستند که به شما کمک می‌کنند راحت‌تر به کانفیگ‌های مختلف وصل شوید.
فرق اصلی این برنامه‌ها با بعضی از اپلیکیشن‌های دیگر این است که لازم نیست تعداد زیادی کانفیگ را یکی‌یکی وارد کنید و هر بار دستی تست کنید کدام وصل می‌شود.
شما فقط یک لینک سابسکریپشن وارد می‌کنید. بعد از آن، برنامه خودش لیست کانفیگ‌ها را دریافت می‌کند، آن‌ها را بررسی می‌کند و بر اساس تنظیمات، بهترین گزینه را برای اتصال انتخاب می‌کند.
مثلاً وقتی شما لینک سابسکریپشن WhiteDNS را داخل برنامه وارد می‌کنید، برنامه یک لیست از کانفیگ‌های آماده را دریافت می‌کند. سپس می‌تواند از بین آن‌ها، کانفیگی را انتخاب کند که در آن لحظه بهتر کار می‌کند.
آیا این برنامه‌ها هم‌زمان به چند سرور وصل می‌شوند؟
معمولاً نه.
این برنامه‌ها معمولاً برای هر اتصال، یک کانفیگ یا یک سرور را انتخاب می‌کنند. یعنی سرعت اینترنت شما با وصل شدن هم‌زمان به چند سرور مختلف ترکیب نمی‌شود.
اما برنامه می‌تواند چند کار مهم انجام دهد:
کانفیگ‌های مختلف را تست کند
کانفیگ خراب را کنار بگذارد
بین کانفیگ‌های سالم، گزینه بهتر را انتخاب کند
اگر یک کانفیگ قطع شد، سراغ گزینه بعدی برود
مسیر بعضی سایت‌ها و برنامه‌ها را از پراکسی عبور دهد و بعضی‌ها را مستقیم باز کند
برای همین استفاده از این برنامه‌ها معمولاً راحت‌تر از وارد کردن دستی تعداد زیادی کانفیگ است.
فرق FlClash و Clash Mi با برنامه‌هایی مثل V2Ray چیست؟
در برنامه‌هایی مثل V2Ray، معمولاً شما یک کانفیگ را وارد می‌کنید، همان را انتخاب می‌کنید و به همان وصل می‌شوید.
اما در برنامه‌هایی مثل FlClash و Clash Mi، شما معمولاً یک لیست کامل از کانفیگ‌ها را وارد می‌کنید. بعد برنامه می‌تواند بین آن‌ها انتخاب کند و بر اساس قوانین مختلف، ترافیک اینترنت شما را مدیریت کند.
به زبان ساده:
V2Ray یعنی: این کانفیگ را بگیر و به آن وصل شو.
FlClash و Clash Mi یعنی: این لیست کانفیگ‌ها را بگیر، تست کن، بهترین گزینه را انتخاب کن و اینترنت را هوشمندتر مدیریت کن.
حالت‌های Direct، Global و Rule یعنی چه؟
در این برنامه‌ها معمولاً چند حالت اتصال وجود دارد:
Direct
یعنی اینترنت بدون پراکسی و مستقیم از اینترنت معمولی شما رد می‌شود.
Global
یعنی تقریباً همه ترافیک اینترنت از یک کانفیگ یا سرور عبور می‌کند.
Rule
یعنی برنامه خودش بر اساس قوانین تصمیم می‌گیرد کدام سایت یا برنامه از پراکسی رد شود و کدام مستقیم باز شود.
برای بیشتر کاربران، حالت
Rule
بهترین گزینه است، چون برنامه هوشمندتر رفتار می‌کند.
چرا استفاده از سابسکریپشن بهتر است؟
وقتی از سابسکریپشن استفاده می‌کنید، دیگر لازم نیست هر بار چندین کانفیگ را دستی کپی و وارد کنید.
کافی است یک لینک وارد کنید و بعد از آن، برنامه خودش لیست جدید را دریافت می‌کند.
اگر لیست به‌روزرسانی شود، برنامه هم می‌تواند کانفیگ‌های جدیدتر را دریافت کند.
این یعنی استفاده راحت‌تر، مدیریت بهتر و دردسر کمتر برای کاربر.
خلاصه خیلی ساده
اپلیکیشن‌هایی مثل FlClash و Clash Mi برای این ساخته شده‌اند که کاربر مجبور نباشد بین ده‌ها یا صدها کانفیگ سردرگم شود.
شما یک لینک سابسکریپشن وارد می‌کنید، برنامه لیست کانفیگ‌ها را می‌گیرد، آن‌ها را مدیریت می‌کند و کمک می‌کند راحت‌تر به گزینه مناسب وصل شوید.
این برنامه‌ها معمولاً چند سرور را با هم ترکیب نمی‌کنند تا سرعت چند برابر شود، اما می‌توانند اتوماتیک و یا در حین اتصال کانفیگ‌های خراب را کنار بگذارند و اتصال پایدارتری ایجاد کنند</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/whitedns/909" target="_blank">📅 17:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه  https://github.com/iampedii/whitedns-sub   لینک ساب برای Clash Party & FLClash https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/whitedns/908" target="_blank">📅 17:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔥
اگر محتوای WhiteDNS برای شما مفید بوده، با Subscribe کردن کانال یوتیوب ما می‌توانید از ادامه فعالیت‌های ما حمایت کنید
.
https://youtube.com/@whitedns</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/whitedns/907" target="_blank">📅 14:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ما هر ۴۰ دقیقه ساب رو آپدیت میکنیم. شما هم یک آپدیت توی اپ بزنید تا بهترین کانفیگ هارو بگیرید.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/whitedns/905" target="_blank">📅 13:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/whitedns/904" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/whitedns/903" target="_blank">📅 13:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-901">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">😊
آموزش استفاده از Clash Party نسخه ویندوز در کانال یوتیوب WhiteDNS
🔥
کانال مارو Subscribe داشته باشید.
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/whitedns/901" target="_blank">📅 12:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آموزش استفاده از FLClash
ممنون از رضا عزیز
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/whitedns/898" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚠️
برای وارد کردن ساب باید به یک وی‌پی‌ان  متصل باشید</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/whitedns/897" target="_blank">📅 10:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/whitedns/896" target="_blank">📅 10:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-893">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5u0jgF1Cr2ysYzecu5KyrK_BirKr0uH4tKdeeuyTY2-e6pnRuE9Cm6fjM657o5hxrSnLnA9KkWxJsWNLQRpAbDYLS0ICqX-kObJIUqQT8PhfB9Pvm0cG3cSFo81ZCHOVh_oiZ_6oZl8m7uz5CqFgdur-PBRY2nTfj6zOU-kkZgob0V18rCOWjZXlP5zrk9a3AefkryTrr--dmKeogBlgOk158osfjzWKBudVNx9qyMOWwOJh4f7xhAdSRZo_ZwdZZm2gREGvxy4Bftnz6j3Itmgub2dKamhVqc1-W7cM8T3i3P4fxs2H_0QSYvarPH1INxjFhIBHOZRKxP0ISTR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی
از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:
اندروید: FlClash
آیفون: Clash Mi
با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.
ما در سرورهای WhiteDNS بخشی از کانفیگ‌ها را بررسی و فیلتر می‌کنیم. سپس اپلیکیشن موبایل به‌صورت خودکار از بین کانفیگ‌های باقی‌مانده، بهترین گزینه‌ها را انتخاب کرده و به آن‌ها متصل می‌شود.
لینک WhiteDNS Sub برای استفاده در این اپلیکیشن‌ها:
http://sub.iampedi1.live/sub/mihomo.yaml
لیست سابسکریپشن ما هر ۱ ساعت یک‌بار به‌روزرسانی می‌شود.
دانلودFLClash برای اندروید، مک، لینوکس و ویندوز
https://flclash.cc/en/download
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/whitedns/893" target="_blank">📅 10:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89b2fd3cd.mp4?token=C5pgZ7DrNEjxPYbsbcLCY-X1ooRSidLKjxIeW079r7Q09SqyoNaKjb8_IUadR5R2I2-cfvx7TRtGAt76zFa0V8Aj7eRiaOalzzYSgmXU7PpThZSlxczB2K8w1Pp-z14SJy_RZTiSr2xdKAKPLkffT0XGvMouTecxHXJhfXlEDmqvqzI-vNvB_AXt3P17N4R_LmWgnRz3tHOmfg4KT9pi7fwDLOuy3YCQ8D6UlIpEhK8qG9cmGjlT89rdK7QnL-4ojYUtvmTZavySimiitiY09EdUADce-_jxfJ66tU-3vUy0FXjD6aoFFWsZxAskFW_SVtPetWIkwDpha1UQvcXxlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89b2fd3cd.mp4?token=C5pgZ7DrNEjxPYbsbcLCY-X1ooRSidLKjxIeW079r7Q09SqyoNaKjb8_IUadR5R2I2-cfvx7TRtGAt76zFa0V8Aj7eRiaOalzzYSgmXU7PpThZSlxczB2K8w1Pp-z14SJy_RZTiSr2xdKAKPLkffT0XGvMouTecxHXJhfXlEDmqvqzI-vNvB_AXt3P17N4R_LmWgnRz3tHOmfg4KT9pi7fwDLOuy3YCQ8D6UlIpEhK8qG9cmGjlT89rdK7QnL-4ojYUtvmTZavySimiitiY09EdUADce-_jxfJ66tU-3vUy0FXjD6aoFFWsZxAskFW_SVtPetWIkwDpha1UQvcXxlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنین کاربران نسخه دسکتاپ می‌توانند از قابلیت
تبدیل کانفیگ‌ها به IPهای سفید
به‌صورت مستقیم در داخل اپلیکیشن استفاده کنند.
🚀
Tools > V2Ray White IP Generator
@WhiteDNS
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
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
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/whitedns/885" target="_blank">📅 04:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXGSzPLJtd2qYRO1SwnnSq-NVahHbMbKF4b-ikzL8tgkWnNflcPPBIPkX2wOV9Cnug1hsjujgQNXlp0obH710QuGmdOM5E4GlKWqN3D_2Zr8UvaPdfCZPbBuW8oRUyOEJsxtN8_dt2zcrU3QgVg-zlu-NQByBlIYlKT4NwkVA2w3X2Dq2L7y_b-SVOldTkZaNE7aZLuus1xWHW6vP8csKlG1Y-Jv65KkMEtflQ0HpOCe5aj_J_yl791II4iMQYupMByLY2aU46xiTi1Exs0rReS_yXVbi9LTX-HhWWxXZWeovPHQxMihPPmbmMwoLgqoRi4HEPdUvCRdB-iH333jaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/whitedns/883" target="_blank">📅 03:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سلام خدمت همگی
❤️
الان تنها راه اتصال پایدار و بی‌دردسر اینه که شما یکبار اسکن کنید، آی‌پی مناسب پیدا کنید و بذارید جلوی کانفیگ‌هاتون.   متاسفانه فرمول یکسانی وجود نداره که برای همه کار کنه.   این روش رو میتونید برای کانفیگ‌های رایگانی که از ربات ما هم دریافت…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/whitedns/882" target="_blank">📅 02:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/881" target="_blank">📅 02:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر:
https://t.me/MatinSenPaii/3598
پنل BPB روی گیتهاب:
https://github.com/bia-pain-bache/BPB-Worker-Panel
پروژه اسکنر روی گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت پنل BPB ورژن جدید
2- رفع مشکل پینگ -1 کانفیگ‌های آپدیت جدید و درست کردن تنظیمات کلودفلر برای کار کردن پنل
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Worker
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- توضیح حجم مصرفی و استفاده از این روش روی کلاینت‌های متفاوت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/whitedns/880" target="_blank">📅 02:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW8FF-BJHgzDQ5vj6LyQ7_le_fZ1s3W_kYDt_yvNyPONpT-QKWG2rz-u3-MrxUTmD5nQJjTxMJ7G8B7IubEBjkbrwIBxx1nD-750b303Iuy3h0kW_q50Anc7TnnKb_m4nma6ZRjGKyAvz_jsu_tz3sk7XEVwQwlCqaN4nQs-s6AToFHtFJsZWXXYMbu4s2MZ1aY2ccdNDN8p1PJsIX4SilmwQInGx0xOkcjAN2hf009jMVnTiY1MttNktWzbNQuBGo1GvqH2gW733f_tpbQi10VcARLAmwo5kJ-wG7nvgZFzvM92GBW7PJ_Sjw31en8kA4YZNdTsHP9oY9hKmPJvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در شرایط سخت و روزهای «خاموشی دیجیتال»، تلاش کردیم با ساخت ابزارهای مختلف، آموزش‌های کاربردی و راهکارهای ساده‌، کنار مردم باشیم و کمک کنیم تا حداقل دسترسی آزاد به اینترنت حفظ شود.
اگر در تمام این مسیر فقط توانسته باشیم یک نفر را دوباره به اینترنت آزاد جهانی وصل کنیم، برای ما ارزشمند و افتخارآمیز است.
اولویت و هدف تیم WhiteDNS همیشه ساده‌تر کردن ابزارهای پیچیده و تسهیل در دسترسی به آموزش بوده تا به هموطنانمان کمک کند وابستگی به بازار سیاه، واسطه‌ها و مافیای VPN کمتر شود؛ با این نگاه که هر شخص قادر باشد ابزارها و اتصال‌های امن خود را بهتر شناخته، بسازد و مدیریت کند.
امیدواریم هرچه زودتر شرایط بهتر شود و حق اولیه و ساده‌ی دسترسی آزاد به اینترنت دوباره به همه‌ی مردم برگردد.
از تمام اعضای تیم WhiteDNS و تمام وطن‌دوستانی که در این روزهای سخت کنار مردمشان ایستادند، صمیمانه تشکر می‌کنیم.
دم همه‌تون گرم
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/whitedns/879" target="_blank">📅 15:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-878">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeTX9wcF1ra_URv_FkI6_rhwB_5bjQfG1D_ynCiwzPESRyDrGxrceOpz_c3bOKDAm2sn47Ccivk_hzufj4ouKDVu5hPzFzohaRA6UQWcW7FZgovoYbKwLqEHvy7-9yvMEgLp2XD7S9w7qOuF3_qrbPnYQW71KD2mYpLpE1OB0MxhGyBvh4b79gPIPX9__qL174zbue6xT934MDDBtWOZKkyfDAW4NOjEprw0vbFc9fyvXtjBOTHkw56cK3itljOBB76e0YJ2Umi54me940Kcez_ZJs52v6C2udwNkSUy-REbvcn7juIj_yw9q4dWTaUtX0BJGik6HbtRPxXR_4MNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
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
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/whitedns/878" target="_blank">📅 11:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-877">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🤩
آمورش کامل استفاده از اپ WhiteDNS در نسخه کامپیوتر  - آموزش استفاده از کانفیگ های MasterDNS  / StormDNS و اسکن کردن - آموزش استفاده از V2Ray  - آموزش استافده از Scanner, Validator, White IP Generator
⭐️
دانلود از لینک داخلی  https://guardts.ir/f/6f56591f7b7a…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/whitedns/877" target="_blank">📅 10:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-875">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">#موقت
ارسال شده در تاپیک سرور ها
سرور اهدایی از بامداد عزیز برای MasterDNS  قابل استفاده در  اپ WhiteDNS
🔑
Encryption Key
aaf4b6-@JavidnamanIran-aaf4b6fff
💻
Domains
: جداگانه امتحان کنید
b.bamak.xyz
b.igoii.org
b.namad.xyz
b.jnir.my
b.irdmc.com
b.javidnaman.com
Encryption Method
: XOR
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/whitedns/875" target="_blank">📅 04:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👥
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
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/whitedns/873" target="_blank">📅 02:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🤩
آمورش کامل استفاده از اپ WhiteDNS در نسخه کامپیوتر
- آموزش استفاده از کانفیگ های MasterDNS  / StormDNS و اسکن کردن
- آموزش استفاده از V2Ray
- آموزش استافده از Scanner, Validator, White IP Generator
⭐️
دانلود از لینک داخلی
https://guardts.ir/f/6f56591f7b7a
https://up.theazizi.ir/download.php?t=ecabdec17d6cbb16f37a13fe28c724cdb591
😊
مشاهده از یوتیوب
@WhiteDNS</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/whitedns/872" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔥</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/whitedns/870" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگر در اجرای نسخه مک مشکل خوردید دستور زیر رو اجرا کنید
xattr -cr "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/whitedns/869" target="_blank">📅 12:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/whitedns/865" target="_blank">📅 11:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/whitedns/861" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/whitedns/861" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrlFpwLSzI8RrS54PmrTLu6kBcquEIVtFyOVKGVMYpfOvbg6xW_lKaeLZLBlIKHfYNmbEXbSROEAZeq45J1FmyrwFPLBVdNRRbjFmbQ2UlpwBWi2yELWTrBn52susIHvOvCvFP1fmVGexW5Lavit0Uw4sDDvEQ10g32XDFi4SIUhbUDww54pztVHib7zFX4AIrocu9j4PpJ4kcKAuFygWy0q2mVE8KH8zyZvskYS8Zso4y8XKmX7-OpckIqOJdZgSmLqFoacL4bOC8orKu7sc_xOdxIogC5rEDRA3s2f2EUKfmzUzSbGM2LsTH05Olha9oE7DPqcc3g32LVAUq8Y-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/whitedns/860" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXGCtKY-QGNa-sZw32jE27wGwieLoOdhLMNr8Ry0jvsCEUFkB7ydY1t5iixNyUMFWOE3t0NeCXdqAxFiZxzPThZLq0kJ5zMqpXpeGwPDbUfSXKLHy4ilgG2TTaqYuJeVOPjs7I8D2MFp29Uar-wxHsnUIZnGXf2XBoD6N2xbdpEjMJf6Gkmpw0a6ZDOjqpfaYkF5V7IWIg_B-wHaFE9VYJCF2W5ptpfWYycaSF2U3oLmWSUGO9OHES3kI08lC-kfLDOjkAvWbIXLwHSXmlsCk8eVV2T2SLOAfLNWnVsLR2SLfa77RCbx09MZ6hKdn0ruF7oZxxvSaF0mEcOfI-uqTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/whitedns/859" target="_blank">📅 04:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/whitedns/852" target="_blank">📅 04:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">☠️
پروژه‌ی SenPai Scanner — اسکنر IPهای Cloudflare   چی کار می‌کنه؟   از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.  چطور اجرا می‌شه؟   فقط فایل مخصوص…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/whitedns/851" target="_blank">📅 03:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dtW_p85gWCx7E40z6trIb48sfbM2_n36eLanmcf1dVJ4LT3fE9BuEVwqhI2p5If6YIpOqCccBomElmBhy2TzyGWtCS_JHLIRWFowH9eQbNdUpv8UcR87d8OYTjbWprMysP5uA4ov50gO7cPiTV8qxni5MINfp5kZM5qdLIp1zTWbSX1iTFsk0ngPqTZJQxwrhquCoPwu_dtc1fv8T7WDnv2833ZzXq0hJQEn1VABBAw2wmUAzOHX5qPqFVM9582lD704f3pSrkPux6sx6erP7lc94x1Uf_3NKT5YV-RrreTIUIsi3IUha53GYt9lTgEO0zJ5QLXQwGCctrgAFkL7fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/850" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H15Yw_xmqTfF26Z9rgvwU99TZXpi4FLbSo4FGS1mhIbRb4zRGnWR5S7dVMQmZlGQ7eQp1INO-b1HjBnpb_DMc1ZRtd4Z_K_g6rFPc0akmfLumYU_Di7UwKZBSxcfluUa9SBEz_emNlj9nANI1-hbo8Zv95h6QKeHnek8FTEcAFP4lRniWuEMRydSrxKjnf2hWqFAMLSNeqFQNRmDh6CCmemj5O1A98iKGzI8W1Jwpv3TnBNriGm_DVFJF62tOm7hDKnoDj7bnParg2xVTAeDXHYitSFiwRQFddtGJ5jP4qpbfrQ1iBAR7lrzk4EfjtVW_lsCSoFvY9tQrwGqlpS0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/whitedns/848" target="_blank">📅 17:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/whitedns/847" target="_blank">📅 14:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-841">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 102K · <a href="https://t.me/whitedns/841" target="_blank">📅 13:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/840" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b0XjGRIcRh92q3K_s_oRYSofXa5Oo1TUfU7ZKPYKpaguuRCGB4x9A2ki-8PEqZhLkcD3oYsfQtIOBiWLh6iVwZFT0_G5RSaZ13Ll75UeSpTJfkoc5_UrxQ5on7TbdjHR-qr_j_-1uxGUcbWQXT3btYs_APzhW4BFPy6NxmmumOHNeEG5KnnSZuA_8_wR6-W5-VMSE_PxKHBF3LS2qNPRHBllR3onMwZgznACjjiEi0XYwAfRDmAnYlHIvbl63aZYAOCzRNyx8MorqXL_EibcV0pc8nmvhuWAvq55UAr_bt6ucf58OjBNb3mOrN1JHOyNw9_eqNjnH99quTJ0UDpHVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O30-BbiX-C58W2UMJKPHzuVi3y5nUyVfL5jHNVMv5GVp-n07fO1JzmaOQ3SPnn7C_FRFrh7kNLOcU5H6AFffKonuc0J0f1LF4McT-8jBxm4gkf-_MPV2KoKbvPZU6D_69jwYEStPQDqFjLrWuTtV2jQ8Tgc2e7c10MDqDj-1aTcBeY60ohhmAcxUQdwN3Bg_He2CJzwlCpnEW3-6YGNShEZPzUBUsoTne9qIgYEdb8IfqEQNMJYSuXd_olIl1MRfIrbykqwQf3rd5hnjJvdNjMSNJ9Ub9C41Aluid4lNawJ6o8r-RdDkuCEAIX9KT8JZh8s2St5ck4U8GdYTEbmB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l61C21ILm1_RD5reQZiWPWIk4L0-n88FEgM3v0X1qOi4MTI3QNo76teF21SjUP3A2xHUjd_i6zsZx9jWgeWwpERDFN2U5evF8MHsWEIaszlNcp2783xdXWO521L_ZXvLt43RIUEEsjKaPsHctgTxUdALSvlNqM5mC8rroAMRtOAvluR8yS7ou8eUAYdrmu5lrUDqRwmQ-xTUgeHHTqObb-cGZ6Nv9JOMndDygIwSob5_yVKiRJWtQdyRv8B5hAJrz7cy3Q8igDbftX5jFEGi8ESSkkjVj7eG8dnYDRjJzic8R9QW8-PbKt9EJl7gudFP_A0NuxnU1absV8whjJ5RaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R4pHHJMOVXxQV12c0urXKWqU6OPIgWjCrCA_-F7osisAL69DUkE1KKzMWaam7jri9pyW6OXXymLaWx8k6fKwdfIC3Q7v49jKm9yk1MYXG3ughnmwvhjvzlQlyjNkKKChd4uTLxG0J8KkGcyToP1PZ7CQSI1vPTeGZbT1XVRsqRn8nUG6iS7_x7Z4EBC2mlaA2ZUgg6tvocKPbv6QF85ilXIVFS4r_quF-sQAuUu8sVyIpNMGzNPtpNJMVD3gXaREt8RTTslilg1pYADLmRFFvK-kOX7CkX9QJJUPPF4d6EqXpRn5WdsquSCdNwPFiDyB2f90zTBEfIMnxTdZ-Woggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ob-nsd3DnYvLRgWL1l6PPpYRAlB8d-Ry4bJybS1le4htgKU3Q58PbrhUyOYhsJc6kana6-jYEr5neCmYeHxVgr_zKztZaz0T7Tfd0UDI9qW-7Bw6Q9oyzmKCF4MyrRfUZ-9POnJXP8Begqh4E_83vnB5qvrByYKOk7pF1Nhe3Q20SlB9eO8HGTaQu4qZuelWR9sFyRu1clQHZIggkHNEGPxy7GM96ldAlKrNjC42zCohwJzIRH5IhlY276J0vO9BJbaOeS2TyiW_39kaMHjDaqWzwy8x3EizM4cQPjcXPIa9K0B-HFIGlrAdSUDKNjUEaxiVxRQrJnecLesXf8fCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KC9croKd3YogbJoJriS5IOyUvs7bzspaJklbsYRpTB2kvu7ZuyGGKcb-ALnwFxmDwSpdaAp_Wt3pY24TNplYrE28ZK7wigd2Zn-GKAFWzmE5rJr8NgRq0afRTYwUKLuRtDlgF3lukA5POn5ck_NjQbV86G1b3B-GoQVKzXet9UGF6eO6mN4cKgURRH6m0NNY_jUBVmz5aAgYieVdeSrNFIcw6OphiNRMmh9H2AHtmWi6a6NibZYhCEFgXb_wuLZQI_3uEnpOTj3bRR3jmI_GAEoGhIiEw0Av4qhh6RWs6gcW_kaHnOEChLBq1MKYiA65zLmmt5_WsFR-fGHkeRUN5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OdnIqUFe3W38blRFgGgVwUbHUv428ic7MjursxXMhpSL-HbKGeM1QVymUudRlKgCFt5NqHx-Erb2JQH6C762KcEqAbrOPQGtJOS9mO4GMO4Yq7fSwIz_mgddCrzIBDxczQpH5z78DosvXYnI8_Mu3cj0nH0yH8hOyzSrGp7YU68yDhLfQIhilAVGug8ejATQDIoqr8q0yZgn8BoiYnvHOngZerNwga5lqj3I3yCjw8mCDpro-ybiXVUpy4v6T0pdMfq5S76UXbPY01c0mP7gXz9xA_mNYzXXjJHHwfSa_Jva9emi9JFQI82aDMBplcm9BOTAhDncGtjwkNSaPEwd7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fry1Zo6XZjCyMlEnW-hjwY6qW2Php4FQ-vVyNgf6j6DCKaCJAUjbVNSRDmgf2-45M7rJbER9IWFwukBCUJKpQjUBTIJH8wEv8K2O4rWjXspguFJv7ko-EfZgP15OrHKDP_U98uDupaKOvusIexShdZ6P1xbamd53J1-EQTsItPqWjgDfTUveuAf3qorobw--e-_3R3IoC5ekAcSs8WtWcyGhKV_P11KU2taKLR8eYrU4a7P94FwMYzVWLK8RnKyXwya44VL2pvV-yyW2XXl490AiZTOvIa1gjy93Vku9M3EowR8icHcFrtV_iLjynkNvLCNhxNsjV2SPr2M3fxnGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OVt57hLXLZl59wWtWCeftRky-LG_TL6kfa_B8rTyvGsRGu_IFMMQJpZr1R77ofaDRijNIE3l6ewLw1cDNxrM7xd1U2taQ4LFEoENF7Lx6HKGIhnPXYDAbUUK9m1OmhFXyiCokefURrXX53zaYRT-flUkjKMeELXUY7gNA7AH_EXFuiWLsY1s9Xwo6I12v2-TsE4pgGA49t5VGvGhwbN_-6kmUj3HrO72OoRwOhpsZUil6f62fX8brrbOfEUFzYFYUNOcoqSOCvHuFuvPB8fH6d7EFrqlnLD37wjccfUdAP8Hd5TFXqp8v-wJGB8uXRr69z5eX6OkJD9lQQjmGjy3sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/whitedns/831" target="_blank">📅 13:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmIKWzjxLIK0lQsA6fyjOiv8iF8bALl8rxwIKO6RSscQTiK9q26_Z7qUGhNfcFDV6LbbhPDWeQu4xQkMZpZ8uDjchJmsm6eG82GR_DpImOGHEPMc2gGesnCTaQqzEDcDaz8TeT3gCihe26qKDlZm3UAP7UyJ5t5aIgZgkzgocsMIO6dnCXy0kj09ELWLeJkqVyf7KseEYxFtEMu0Oav_S3jYJm2h9VkkeDtDsvNCi33qbSF4fpwjqwd0ZyXUnF0UgVGEOs939tLx8Umj72ZFokbACu_1Xp-i5yduQxadEfUnWg-2Al6vtp5UnllOOU86wOK4Jk9_qiatFZOE97LpxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 120K · <a href="https://t.me/whitedns/830" target="_blank">📅 12:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-824">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/whitedns/824" target="_blank">📅 12:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-820">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/whitedns/820" target="_blank">📅 12:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-818">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/818" target="_blank">📅 11:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-817">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/whitedns/817" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آموزش اتصال V2Ray در نسخه کامپیوتر
دریافت لیست کانفیگ ها برای ایمپورت کردن
https://t.me/whitedns/804
https://t.me/whitedns/805</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/whitedns/816" target="_blank">📅 11:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-release-windows-x64.zip</div>
  <div class="tg-doc-extra">23.8 MB</div>
</div>
<a href="https://t.me/whitedns/812" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/whitedns/812" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjonK7bWBDQhymjeyfJnxBWkz0FrOrG-bxRHjqlae-Zq2YWiQIFvghc0u--QxQmjn15u0WDH0uZgMvmqu8f4jfTyRrxfwjWV3JTpEmPhe0ONuDEwvkruoubgk7pKclH-8KLQHP--oBLBpcIbUYWMrLIjK9y8vGbCnziRoY8P2K2lKF9Nzu6OriIS54kHJ-YyaaeQd_IRW1e4UpP9x17cSS7iSjkcdZZZ-PQ2j2nScV--By4rYtsfIevFLMVVt96FOTa_saHzznUcu5GEo7R150SNdqZDucnpbTCy3Tw1Q09FILK60fbEFVBNS96iE5tUZvavNRImltiDd9oR-29mVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/whitedns/811" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/whitedns/810" target="_blank">📅 10:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-809">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/whitedns/809" target="_blank">📅 10:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوستان سلام :
این یک مدت به همه سخت گذشت ، شاید شما اسم دو نفر را بیشتر شنیدید ولی بدونید یک تیم ۳۰ نفره بی نام و نشان پشت این کار بودند  توی بدترین شرایط از همه چیز زدند تا شاید یک روزنه کوچکی باز بمونه ،
ببخشید کم بود ، کافی نبود ،ولی در حد وسع خودمون تلاشمون را کردیم
یک تعداد زیادی از  دوستان پیام دادن ، تشکر کردند و گفتن ادامه بدیم ، خواهش کردند بمونیم
ما هستیم کنارتون ، مگه میشه این همه عشق و محبت را رها کرد
یکم استراحت کنیم ،همه با قدرت بر میگردیم
توی این مدت مراقب خودتون باشید
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/whitedns/808" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIdFyCE8ND9Onn7pX7rGMvkYzuWu9gf5MDhaDsjtErPAnFG0UDGLvvZNC7Dckn8k-fdz354tXiMRdyQaZLV6aN7fKgcWwCih5l677_-4jCHfYAqPiWqXvbGFaVtjQ-U4P_p_V02kaJGiyrOdX9jyK0jPROG9IP7XOVkRHEBOjg7g4rIavUaAVKwBffpIrTljRjbgK7HU3-ciRLRK9vCUnE8jIAPlOfF9n7q8U0mTbDt38WrJj4yNEQjvcsvzzpvB-IJPKshzKvxmfJiG360JDHaqwnlTXnVsZEutpElubZ_0zB6Cx_HdGJxoYxRLI1FMg1r27nWehzY1AVXqpsDPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#موقت
یادمون نره کسانی که از ظلم پول در آوردند.</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/whitedns/807" target="_blank">📅 19:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-806">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/whitedns/806" target="_blank">📅 19:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-805">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/whitedns/805" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-804">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/whitedns/804" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5FPkbCtiLe2vTriWR3JpDrjGvsc0hOzbjqcAeHOFUKeaLrWAUfcdn_S3x_im7z8cWgT5a-z_Y55XqqiLcW5niEPqvBe9eYiwvUjmLDpAraUbsevo-1jvjXjC4YK5YMMfihg6E9AKND1r2Me1C_bxexJpQR1sxyCGgJTpWInqQU54QYMagS8U5UHKPLJTaziH2f0jOLqBOf_-jaEG6uXhl5tAGmY8kxkLH397LTSJxk9pgOBGquFxmnYHpPhQPhvdYF9Of-Ll9uWhiv0Z3LjlhbAC64eQq96FTxNWr56ZA992aekvYZ6Dlq7AD82d9wjGmwaenuqjeqUU5pgTPBi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGWMiv5PlH0p3xYmGcCKt8v8KwFjQWPh0jBncDBgNa_mGFFr9yhuq3eZ7rSpXDHYyrBnUtQSbd0LUm3thYoS7BD6EEk0UR_Las0QhAWei3ElKuQfi1mQXfXGUSxq8OQ69RM9eW2mdqnB1UeD74b6R6y3ErB-xS5QNcAchsnmvPrnUhmSTaSKW4GO3F0hbNnjS1Y6X5qLzsQmqeXG5eoAeNqK3sIWg324y8Xv-6dJtraKASHf9MVtctm8vAZrqzuEMRPFFVCZM2De5o2KmGu7PA9ah70lRTMAOitXtbAup8XMqe38bDc50yGvGzSkROiWQslGMBGANkDNWh-8aizVug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این هم یک تست سرعت با ریزالور های درست و با اختلال کمتر
🤌</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/whitedns/802" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/whitedns/801" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در طول ۳ روز گذشته، کاربر های ما ۱۰۰۰ سرور جدید اختصاصی با ربات WhiteDNS ساختن
🎉
@WhiteDNS_installer_bot</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/whitedns/800" target="_blank">📅 09:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دوستان گرامی :
ما هیچ گروه و کانال دیگری در هیچ پیام رسان خارجی و  داخلی نداریم
تنها گروه رسمی ما :
https://t.me/whitedns_group
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/whitedns/799" target="_blank">📅 03:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTBG7EySnqC-1vsrUjPfaHvJkq8txU-LyIWut4Rd_f8nFK07kGkw0j8QvBVjS6hp04TwkT315h1x15nRAgSwbSdgT7MHv13JDCvIdxzUA0wNeh1Jd77M58wnqUJ-3twDNHD722PWaJxH5fBqJz620i9mRafgzEcyjFPmOK7jpkM3YzuXkjVLOABJMYZmESntDMk2WasfrClW-ChVXmm_YCFsGxgQL4hGYfmOi6M90ZLTSDJ_hjSsHVfkY8cDjvw8rH9xqd20eiBM85hqiftFf4f3fOm4LlIWIbNGnFt13XSa7BDfBDp41k2ADYOjma1YMdSG6L8CeJ7AUDK30LSljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کیه این تک دلقکو همیشه میزنه
😂
؟
به افتخارش نفری یدونه بزنید ببینه دلقک کیه
🤡</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/whitedns/797" target="_blank">📅 16:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-796">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaCMqcx1KqlDm_mLI7sZAvKAL8rxIo6GLSXRgSz2cx_xpi3SAKIrKVhgiFxjybDS_dnoYDbu7kqOTjxBbIvwiSFZf2Y9dBlMxej7fXHNvnxd9rf3KJr6aLuj4GOuU2VOP3pAlk4ZEF55qj9LUWO6DGKrZ14HuBdz8wiul4xA6yTnHb73_7A7V9URN2inT1OlI7qwclQZmfdIAnHUjydOmy7eEdh3-ejuRSw_TYuH0neaVcloDkdxsDRQNPQWNFwH5TnTjeFK0IERNYGjtlh2W44zpwbSSumXCOEYs1lseKJm5i3EmlCBngjYFU88_3ipfrBOSBafUr3RagkjW6MuYz4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaCMqcx1KqlDm_mLI7sZAvKAL8rxIo6GLSXRgSz2cx_xpi3SAKIrKVhgiFxjybDS_dnoYDbu7kqOTjxBbIvwiSFZf2Y9dBlMxej7fXHNvnxd9rf3KJr6aLuj4GOuU2VOP3pAlk4ZEF55qj9LUWO6DGKrZ14HuBdz8wiul4xA6yTnHb73_7A7V9URN2inT1OlI7qwclQZmfdIAnHUjydOmy7eEdh3-ejuRSw_TYuH0neaVcloDkdxsDRQNPQWNFwH5TnTjeFK0IERNYGjtlh2W44zpwbSSumXCOEYs1lseKJm5i3EmlCBngjYFU88_3ipfrBOSBafUr3RagkjW6MuYz4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/whitedns/796" target="_blank">📅 11:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-795">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r46-FSLuq2bl3umpQDbk4aicpqomXsF0w4p_RsE7NZwyqclpRtwCdyePpADTnxU_Nm7ssTSc4GZeLs_Ukwb_hKo75gj5Drpxl9h9AvdQIRi9k7Q00VlIU2rZD_kC3Z35lUfUABO9NS9AcegmZGe677DrROp8jOPA8Jc6h9NEeWMyJfVeKlLT8NpBE91iAxnmWn61g3U7AcONRRb-tlV4s9W4GFST1jjCg3QguMhkbInxv8uZe53BJ4k9Ct0xZsFH2LC7-rYOyp0DcU1VHDXxiorxhRUa0CVVU4K8_wpqXcfU3-Iqn80IzriUANeNy291RbYaJhZh_3sT1le967B6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حال حاضر مشغول تست نسخه جدید اپلیکیشن دسکتاپ WhiteDNS هستیم.
در این نسخه، علاوه بر اضافه شدن حالت دارک مود، تغییرات مهمی در عملکرد داخلی برنامه اعمال شده است.
یکی از تغییرات اصلی این نسخه، تغییر کلاینت داخلی اپ از StormDNS به MasterDNS است.
این تغییر به این معنی نیست که سرورهای StormDNS دیگر قابل استفاده نیستند یا وصل نمی‌شوند. سرورهای StormDNS همچنان قابل استفاده هستند.
اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/whitedns/795" target="_blank">📅 09:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-793">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">White DNS
pinned «
دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و... ترجیحا نخرید. نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه. جای مطمئنی برای دامنه دیدم معرفی میکنم
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/793" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-792">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و...
ترجیحا نخرید.
نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه.
جای مطمئنی برای دامنه دیدم معرفی میکنم</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/whitedns/792" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-791">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز  ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.   تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.   من پیشنهاد میکنم برای راحتی کار شما، بعد…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/whitedns/791" target="_blank">📅 16:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-789">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 53K · <a href="https://t.me/whitedns/789" target="_blank">📅 12:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-787">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز
ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.
تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.
من پیشنهاد میکنم برای راحتی کار شما، بعد از خرید دامنه و اتصال DNS از ربات
@WhiteDNS_installer_bot
استفاده کنید.
اگر از این‌ ربات استفاده کنید، فقط با پروکسی کردن تلگرام‌ میتونید سرور خودتون رو مدیریت کنید و در شرایط بحرانی فقط از طریق تلگرام همه چیز رو مدیریت بکنید.
ممنون
@WhiteDNS</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/whitedns/787" target="_blank">📅 05:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-786">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/whitedns/786" target="_blank">📅 05:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-785">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnnxtGqYZY6fvtAyh9H4ClUOgUQ7kwskKrwztBCANU2yEaeV_Ng2zI-XE2oSelSjI0b0Jyx1e-E9AGxtmTuNVMlwZmo7VrFvImaihX5m2Y3N0dWbvRUlsp9cOuvvmo0SwVsdeyExYUJj133MjWIZ8O4Hue_JgS-EiA4bc0ZJiM-smCRPmI8CKswy1EhlKP1WFS0kuR7kAuaRyvtVt9AEufdxA42fhiw9c8KDuhkzURKZ2Wbn6JHBYU26n4Od0ouKDexYOA5QdUO_fxAbaoa73iZQ9eorYFvfXJ7i84xBaS54k0ewBNnuaZeUfX6HwC1etOqV0Yw4aOI2bXImnDCjGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/whitedns/785" target="_blank">📅 21:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-784">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUUL6KQz6EDuTWwZRUZqf5551KQ5yAd4RMv77jfU4VuMZcmve-RM-R8BdFc7bJ3UACjHuI0MXEgGsxprHGtf2fssrNO6raKoyV2k7LfY6pIAbh5mG4VEVKxY_-yROanV3LVjwpj7LP0l9obNvm5rJUK7p-9GKgWXQK1QAgfK8Lx1P83fKY7JWkKjrn67xD5bGGqwnyUgdKROl2P34VtlZgd-TZScIAlA2SleciNyXTQ7Lu7olNq1cvcjuIiPA071ipds2RNZtvmq1RGWKxoilM6DUhUynlCkjw4hJbuLJZ0oXHfn2891CAbY2979sHDu7B184nH5O7qze1ZIVK0_og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/whitedns/784" target="_blank">📅 09:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-783">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/783" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-782">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuFZoOv6COdZflZhi49-eJlWIhNzX7L1smNQyJux4VYN8TcNmMrCm-Ul1ZTJp-0xDxAuJA-93peur3UKYKqqoto4qL4JnUH6q9Npeikb2UQi8Ny7wXqIfbWnseIIxwqYAEq6bJZSEvVr5xIHpo3NHS35Qg7e4ehi1q-Gqu2ndPVfvAW4DH_dHDBkC7c6I3OTcAAQNKwilaFya2BGoy2Kiw8CAJbTPP9_qNQtNVlY5kzJcmG5RW9PYejaSlpP2-Xo_ixWhuLXna70VG20pEhXtuKSYh2AfApc4_M2JQguWx7DWcBHLGhBdcyxPmPTmZlP6K-smFDfeiI2LMTPr6VL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان
👋
چون سوالات خیلی تکراری و بی‌هدف شدن
🤔
ما یک گروه با تاپیک‌های مختلف درست کردیم
📂
لطفاً اونجا عضو بشید و توی تاپیک خودش سوال کنید
✅
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/whitedns/782" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-781">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soPJYC6Yk7UHLJy4YckrKgWsjAcY7qqvevGCcL0Xgygmb9zysLia-jOkeIfBYHlNIbeCaq46r9W3GeRRxiIsfYTj_DL3pBt0lFIi9kiYsXA7vyc5-AuM8ctu5JYW71ielStSAGt7HgCKTnF7Cikq-FI7Plewt1ULusv2vxtR_Tp89z4WYFyCzdM2v_xlZrUbAgk75HaWSxfxMlTczR2mglfvCsmayfSZnbkS--cnrYmoSZ9WYm0T8MVTjDClEYrXkpP8vEgbNE6hOa3pzxs5bHS8F2uCQQ7nG3_YyR6olBoVLluSeD2moNwGZ-8hEvytvRgq5n9WcDlAHvQgCJB1IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/whitedns/781" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-780">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">+۲۵۰ ریزالور جدید به ربات تلگرام WhiteDNS اضافه شده
برای دریافت وارد بات شوید
@dns_resolvers_bot
و بعد دستور زیر را اجرا کنید
/dns_master</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/whitedns/780" target="_blank">📅 16:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-779">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/779" target="_blank">📅 16:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-778">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">لینک داخلی آموزش ساخت سرور شخصی StormDNS & MasterDNS
https://guardts.ir/f/d68436b0fc33</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/whitedns/778" target="_blank">📅 10:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-774">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZGwdvavbbxUK4QXaHfnVq-reyraZ0djQujqasK70kQ9Gs60O2MLtYFosjmDC7s2EXQK3gJ2MmT4lcgY6wQPPd8at1bH8DWTb1TCFIpBL1chEaMTUdFLdK8Yfh8ro1WNRKcCC7y10_X8S56zQnGn0mv5knhncJCEfwctBvJmhwGwvjVVT9fIRkHCoAIBY-LWyP9wHgAnSp6gu3UkBjU9pyIjljU-wqhayunq8kAfqR7LqK47ljPdxXfXwt2hcZ_jJLUIl7N37v1C_5AQ3YWlN-0CepQ-6nN9f3ktWLG9BP0e9Jzk4tms5VgVZeQf2ZSaNmd2vnZFjYxwzHjB3T7fFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ga4_WXFx0VuGkgoY4SNA7YLGLonLjDRfywG6rV87NFnbQ0ECj8ShAnilTrEM57f2LYWphBhwrYL7J0LfsNyN-Ouo9lnAKj3vv57BolKiIhIuqYwE0oxfwLG1N-CnNLu9sT12y0RcRltYJjD16g-JRnpKCi4DqGqKz3BKLp8snK1S5M9rQxAqbss6h_PcX2W58QxEdnhKixF1o1vNca959te92_GbSTB1qzYoOfqJ4QUuFC7HPOm-I_6zwMNL7VZvS_kc9Lw61e3lUJHKKUxuvIz2YoEvTbFWRNdXoZxNqyVGjWM_NNyI4mTcPW8v18aUi0_ywZOTOBu0slV8XX7ITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baotgeV3MuFO83WDZVrzAA5quS0x-mHLI1HPc2ufaN0ATsslObDkC9kQ0tU3ako2FsIeDFZWlBN3EEv6Hkyf7nkXOVhTOR-vSBg_qzJIEkmQXKs2_8ZOiN4nyRv-gqJnVmD27n85uLUbmbtbkJ8arZvsCY6w9KoSKsOB5EWNqjnRRHaGyAFMtHFkV-FQS7ZVSEw0e44e83gRndsS7A1_LD6TA8j4BySrqbKcSByA-70PfrkdZKtkKMRftgAWa24k8ON8xNjqv-RIf6LkFoqjThpHYfBxrG2mVibm8YlDXCJ8-TDjo9ARsE9OH4LXTJ12XkuWlUPl4fdJOwyhGEkAsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">- برای پیدا کردن سرور برای وصل شدن به تاپیک سرور برید
- برای راه اندازی سرور شخصی به تاپیک سرور شخصی برید
- برای آموزش و یادگیری اولین شروع با این ابزار به تاپیک اولین شروع برید
🫡
لینک گروه اصلی
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/whitedns/774" target="_blank">📅 07:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-773">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جمع‌بندی نهایی
تیم WhiteDNS تمام نشده، رها نشده و قرار نیست فقط به چند سرور عمومی محدود بماند.
برعکس، هدف ما این است که استفاده از WhiteDNS از حالت وابسته به سرورهای عمومی خارج شود.
کاربران می‌توانند با آموزش، سرور شخصی یا گروهی خودشان را راه‌اندازی کنند و اتصال پایدارتر و اختصاصی‌تری داشته باشند.
این روش برای اتصال حیاتی، شرایط سخت و دسترسی ضروری طراحی شده است؛ نه برای مصرف سنگین، دانلود زیاد یا انتظار سرعت VPNهای تجاری.
تیم WhiteDNS همچنان کنار شماست.
فقط قرار است از این به بعد، به‌جای اینکه فقط ماهی بدهیم، بیشتر ماهی‌گیری یاد بدهیم.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/whitedns/773" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-772">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هدف اصلی WhiteDNS
هدف WhiteDNS کمک به دسترسی آزادتر به اینترنت در شرایط سخت و محدود است.
WhiteDNS یک پروژه غیرانتفاعی است و تمرکز ما روی ساخت ابزار، آموزش و کمک به کاربران برای داشتن راه‌های پایدارتر اتصال است.
ما همچنان مسیر توسعه اپلیکیشن، بهبود کیفیت، آموزش و نگهداری زیرساخت‌های فعلی را ادامه می‌دهیم.
اما می‌خواهیم کاربران کمتر به سرورهای عمومی وابسته باشند و بیشتر بتوانند اتصال اختصاصی خودشان را بسازند.</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/whitedns/772" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
