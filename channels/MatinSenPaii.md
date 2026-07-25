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
<img src="https://cdn1.telesco.pe/file/v5pDBFvRflqgTit95iaNRfFBmFIrboRMXOZ_e87S51bzoOUY9uii4nxMxUE4Pa420fNSuAgymWbCA36f3xS4HgYGhggZcY9_iaKwKE3oLIpuSoaWpJ5-bCb4eVIOQgZtAXdFf57sJopsh_I2eczbfWFYYTskH1Hils_ryU8lYT8pmQheO4h4hsdgoVDz7-jIfROGvphlhUnv55To_0LGPABhDbItpXJhkk_mh6GeefN5PkVRJI5kUmDfuopXILzFsfvwVnfFhSCLAbr41f6ZOiXgloUMX-yviJD7ZCggzWQP2hNSoYILgWww4daAYDIq5qd93WYt3nnLUq5aPqs6rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 157K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 19:27:26</div>
<hr>

<div class="tg-post" id="msg-4659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگه بک‌اند کار می‌کنید و Go می‌زنید، پروژه‌ی Gsxui احتمالا براتون جذاب باشه. این پروژه کامپوننت‌های فرانت‌اند استایل Shadcn رو مخصوص اکوسیستم Go زده که اگه با ابزارهایی مثل HTMX ترکیبش کنید، می‌تونید خیلی سریع وب‌اپلیکیشن‌های تمیز و مدرن بسازید بدون اینکه درگیر فریم‌ورک‌های سنگین جاوااسکریپتی بشید:
https://ui.gsxhq.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/MatinSenPaii/4659" target="_blank">📅 19:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⏺
عراقچی: کتاب نوشتم، «قدرت مذاکره» نتیجه‌اش هم داریم می‌بینیم.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/MatinSenPaii/4658" target="_blank">📅 16:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
برای اینکه مطمئن بشی VPN درست کار(نشتی ip نداره) می‌کنه، می‌تونی از سایت BrowserLeaks استفاده کنید. این سایت IP فعلی، موقعیت تقریبی، اطلاعات شبکه و همچنین تست DNS Leak و WebRTC Leak رو نشون میده تا مطمئن بشی
#اطلاعات
واقعی اینترنتت لو نمیره. اگر بعد از اتصال به VPN، آی‌پی و DNS نمایش‌داده‌شده مربوط به سرور VPN باشه و نه اینترنت خودت، یعنی اتصال به‌درستی برقرار شده و نشتی وجود نداره.
این سایت ها
#امنیت
سرور و نشت در اپ ها رو نشون میده:
https://browserleaks.com/ip
https://myip.theazizi.ir/
@xsfilterrnet
👑
@xszapass
🤩</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/MatinSenPaii/4657" target="_blank">📅 15:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تا اکانت گیتهاب سازنده‌ی Aethery اندروید درست میشه، به هیچ وجه از پروتکل MASQUE روی اپ اندروید استفاده نکنید.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4656" target="_blank">📅 05:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VNBFHYYZgk3ypdeIlD4BDHkH0FoflulwK_OpEm1pbge5gHRWWtwUs0g7dUasjUwSSG-Rx6SngFZNQaKwAx33xYATpNPRBRIe6Xv_hukyziZib7bSwi9O5k4extk85fc6ONeHGNAqumQevfFaydkuOvB9AjgjV6tY3GKf0rbJc1XyxnbKG63oAaUOtaCAcyO0cm0r8cRSzSr5otnsORCqRm4ltpY2JUBqioEAnsMSht2adcuFsQgyhBXH0gdq1H5VRcYNYc3qqyxYRdSOr-Trw9wjLyOkFLd1f9vc1Da86-aulsDlSHYuvr3XE-NqInUKm6hyboXR6w-ZwPRreDwBpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4655" target="_blank">📅 05:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TqOlrdicfvpnXuoIirXJyazY3j7QLIC1TFqFVvtORLWEeDs_4NNBgV4hteS4nKJEZNQL55UX3Pa23M8Z7z1Z6FEBG3tTRw0oG5pEn_Fv8yckX5NxC4NLyUiVB1brxtU5DpJN4UU3wBZZawC6qj09s6Z5p4uLiUGwlKseR6dg58u7HDc4OfiKMUp7WZNa6jqVsifbT7nWQRaFjyB4cDCDKW_OJ-G2XcDxbJEqVva8BPiZ9gI3KstDtmSsYAx7oeZut2BK4InggWO6P1K5-V_LlE-Oib-GDb-8HPq0v3PftutKJ421Gt2U8G3RoGF_gWsxU7TChfzkaStyuJApkzpTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با تشکر از علیرضای عزیز بابت تیزبینیش و زحمتای @CluvexStudio  این مشکل خطرناک که شانس MITM داشت حل شدش. حتما aether رو به نسخه‌ی 1.4.0 به روزرسانی کنید. آپدیت GUI هم به زودی منتشر میشه https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/4654" target="_blank">📅 05:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آپدیت جدید Aether v1.4.0  https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0  توی این ورژن بیشتر رو امنیت و پایداری واقعی اتصال کار کردم (توصیه میشه حتما آپدیت کنید) :  فیکس امنیتی مهم: توی ورژن های قبلی اتصال MASQUE اصلا سرتیفیکیت سرور رو چک نمی‌کرد…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/4653" target="_blank">📅 05:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether v1.4.0
https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0
توی این ورژن بیشتر رو امنیت و پایداری واقعی اتصال کار کردم (توصیه میشه حتما آپدیت کنید) :
فیکس امنیتی مهم: توی ورژن های قبلی اتصال MASQUE اصلا سرتیفیکیت سرور رو چک نمی‌کرد (verify کاملا خاموش بود)
یعنی از نظر تئوری یه نفر که بین شما و کلودفلر قرار بگیره میتونست یه سرتیفیکیت جعلی بده و ترافیک رو ببینه الان اضافه کردم که سرتیفیکیت edge کلودفلر با هش‌ های واقعی که pin شدن چک بشه هم روی HTTP/3 هم HTTP/2 این رو یکی از کاربرا (Matin Senpai) گزارش داد و خودش هم pull request فیکسش رو فرستاد بررسیش کردم درست بود، مرج کردم :))
فیکس مهم دیگه روی WireGuard و گول (WARP-in-WARP): گاهی اوقات "Connected" میزد ولی داده رد نمیشد. الان هر دو مدام چک میکنن که واقعا داده از طرف مقابل میاد یا نه.
اگه یه مدت هیچی نیومد خودش میفهمه تونل مرده و خودش دوباره وصل میشه. گول هم قبلا اگه تونل بیرونی قطع میشد کل برنامه میبست. الان اونم دیگه ریکانکت میزنه.
یه لیک هم فیکس شد: هر بار reconnect میشد (روی مسک یا وارپ) تسک‌ های پس‌زمینه‌ قبلی درست بسته نمیشدن. که روی نشست‌ های طولانی با قطعی زیاد رم رو الکی بالا میبرد. الان هر reconnect درست پاکسازی میشه. :))
--verbose
قبلا همه‌چی رو یهو میریخت بیرون که خوندنش سخت بود برای بعضیا که الان
--log-level
اضافه شده با ۵ سطح:
error warn info debug trace
دیگه راحتین :))
حالتِ info آرومه و عادیه
debug
جزئیات تونل رو نشون میده
trace
همه چی رو حتی تک‌تک پکت‌‌هارو
و...
Aether
الان موقع اجرا رم و تعداد هسته سیستم رو خودش میسنجه و اسکن و بافر ها رو خودش تنظیم میکنه که روی روتر یا برد ضعیف زیاد مصرف نکنه. با
--perf low/medium/high
هم میشه دستی مشخص کرد.
پشتیبانی از OpenWrt کامل‌ تر شد: علاوه بر armv7
الان بیلد استاتیک برای x86_64 و aarch64 هم هست
aether-linux-x86_64-musl.tar.gz
aether-linux-aarch64-musl.tar.gz
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/4652" target="_blank">📅 04:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مدل Opus 5 توی یه سری بنچمارک‌ها از Fable 5 هم قدرتمندتر بوده توی کدنویسی
با نصف هزینه
ای کاش زودتر بیاد توی کلاد کد تست کنیم. فعلا توی اپ اومده</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4651" target="_blank">📅 00:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26436ea3fa.mp4?token=W7-eWuNY7dJ6DzjypZdnke68yX-NGu77n4mTGm-fUHmf4Wod54J-nOl-FofETDZIB4oKbsBMJIQoshNwzqWiemyvIM_gPtiQZ48J4apN6L1I0j3sCSvEdkC8vt_X5O4ew7nz0LWH5Q95EqLf321GV1GhPejv-appIEKvT8JkF_ZXKT01w17M17Ah5LkRrTlUjSZ2fPbM11OLRGJA0xacFxe3Cik5Z7dJfD6VR9KojBjbQTusibwES4bQABXZL8BIqE7zVcmCch7LCz4mlzx_TCAI404F7iNDACDQh9ziLCgV8rGByDEnXepunN3xjR262dnyc2_U04smV3AcFiY-e2QSSn1JcB2SbOa7nBNPYir2qk5CJLTI13plK8XdeN6y7EIaIVI13427_X6YMZ3fVqJkQrjHtFD5pvSZgl4pdwG2HcMXu0tjDF47M5C6TJ2_cbwKCAgCgNvII7AZP2U04yF9l_Xwj7-XbbNAB8gVzcWt2XQtPddAqvzTu2-rBZuRNAMOF2g3m8jBrrUSWd4L1C7D7Dsa8_RyYLh49gnB6-F4YYQrNuoflJ9MDmn2EKSMrdJDVYH1pBDtPxrAZClOc111ZBU8io4j7GAhmhFuI2yiwZozjc-aoj6z5gNs_Nk7MoGfcDqnduRloLk__Yem8nRmz72HZHi_OvI36syjPO8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26436ea3fa.mp4?token=W7-eWuNY7dJ6DzjypZdnke68yX-NGu77n4mTGm-fUHmf4Wod54J-nOl-FofETDZIB4oKbsBMJIQoshNwzqWiemyvIM_gPtiQZ48J4apN6L1I0j3sCSvEdkC8vt_X5O4ew7nz0LWH5Q95EqLf321GV1GhPejv-appIEKvT8JkF_ZXKT01w17M17Ah5LkRrTlUjSZ2fPbM11OLRGJA0xacFxe3Cik5Z7dJfD6VR9KojBjbQTusibwES4bQABXZL8BIqE7zVcmCch7LCz4mlzx_TCAI404F7iNDACDQh9ziLCgV8rGByDEnXepunN3xjR262dnyc2_U04smV3AcFiY-e2QSSn1JcB2SbOa7nBNPYir2qk5CJLTI13plK8XdeN6y7EIaIVI13427_X6YMZ3fVqJkQrjHtFD5pvSZgl4pdwG2HcMXu0tjDF47M5C6TJ2_cbwKCAgCgNvII7AZP2U04yF9l_Xwj7-XbbNAB8gVzcWt2XQtPddAqvzTu2-rBZuRNAMOF2g3m8jBrrUSWd4L1C7D7Dsa8_RyYLh49gnB6-F4YYQrNuoflJ9MDmn2EKSMrdJDVYH1pBDtPxrAZClOc111ZBU8io4j7GAhmhFuI2yiwZozjc-aoj6z5gNs_Nk7MoGfcDqnduRloLk__Yem8nRmz72HZHi_OvI36syjPO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از کاربرا اومده توی توییتر یه مقایسه‌ی خفن بین مدل‌های Claude Opus 5.0 و Fable 5 Max برای ساخت کدهای فضای 3D (توی وب) انجام داده.
نتیجه این شده که تکسچرها، نورپردازی‌ها و جزئیاتی که Opus 5.0 تونسته خلق کنه، اونقدر باحاله که هیچکس باورش نمی‌شه همه‌ش فقط با کد زدن ( و بدون نرم‌افزار گرافیکی) درست شده باشه.
البته مدل Fable 5 هم این فضا رو با یه بار تلاش (One-shotted) در آورد، ولی خروجیش جای کار و بهبودی داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4650" target="_blank">📅 20:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اگر نمیدونید معماری پردازنده‌تون چیه، این نسخه رو نصب کنید
Universal</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4647" target="_blank">📅 14:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4642">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4642" target="_blank">📅 14:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4641">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saXCsiPoQKqVJClvV5XjBygED-H_Bm4_40ezQR_W4201NxvJqx9kWev2oPN3gwa5eGS1fMs1zsdkPm45PwGzlsutMDeAIOGNDuKb3_hFEm1TgYaVPVVv5AiufVZg-lvg871_LwMGjqXJzXxesUx0NR6_3OJ9wxYAmZW4g_O4h1G8Sq8gAC0SVc4IvL26lG9JD4rwRJMO-gq2iSMIvwC0nFehDWkUFXNRqsjXa1V_zSUXYSUbcsTUVUAdD7Vpubfwgu4PsXRRBjuY-2BOv3rbs16tZABGi4b8ICGx_LEtmsmcxSFOc37Gh7ZKsOdJC5AxUq55wVzng1TlRJR4rBg3dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/4641" target="_blank">📅 14:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4640">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4640" target="_blank">📅 02:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4639">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MAEfJF4ALokYxT94oU2TxtqXjPDlTZmDC9Dniph3w4AHNoGTAm4VoC5SPOzKB90xRLKsPRsjIdKbgPAiw1u7K6okZT2q-SBZKq9o1EJBNQQqXSci6Pfr9qdDFNAYSt1eMsi9y02o2Y0t7QlxWh8NT4mRo3YYzaoXoASCxUjzg6Qa3T7nnhtPlru5j8iCByBU0QGJof2gps0-m0zFaOAaGE-bAdqw5-LB_62TWG16rjmdNIUCwj-Y4hA_ol-8Fbo_mh62U3Rf4yA0mPBrImgRNbKJcsPi6e34D7HxhC9hrVNRuB3sLT8bf-vkVl6bQ9kr0DaGDHOLEHCMgAMn8Vd65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استارتاپ Screenpipe ابزاری ساخته که تمام تصویر و صدای سیستم رو به صورت لوکال ضبط می‌کنه. این ابزار به Agentهای هوش مصنوعی یه «حافظه قابل جستجو» میده تا بدونن چی دیدین و چی شنیدین، که برای اتوماتیک کردن کارای تکراری و ساخت SOP خیلی کاربردیه.
میشه گفت رقیب اوپن سورس کلاد توی این مورد
https://github.com/screenpipe/screenpipe
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4639" target="_blank">📅 01:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4638">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انگار دارن یه چیزی رو روی فایروال تست میکنن</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4638" target="_blank">📅 17:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4637">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یهو خیل عظیمی از آیپی تمیزهای range 104 کلودفلر واسم از کار افتاد
ایشالا که خیره</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4637" target="_blank">📅 17:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4636">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehFzzT_RISTKvFQlyCf093xLLUpX1DW7dW8IgO1SXnTipPWu6FH5720qvDc9YsyJtaEm6mHSpW_C4QZZrSJcjNmWqryTl_cFh5VZWsW3jwkcgEo1gcchfEWXWqMNvLDo98Y2xfcelPHfS8Rs0nUrAmRm2Uyazp1TYpWBIm4cEtNWA99sIThvqnsV9QpPC4MwYQf5dg1LiPtpdqzslV9YacCs4zAlUuhWNAIEeENu1RXKLIDh4KIB_rhYzHG5pvx7CTtBg7mg5fp9UcnIHyAAS8HOdAPs-zWWALkbfEqiw1nBKmgXr5JDCP_W1dBqnNRnrfb4beurewppxMgp5vJEPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4636" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4635">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hywgafi_13MXyQc8MD-SxxqiEy-Pn5vJzn7f_QIIuBIijfP2HNpyim3S0zzlYWVYisxSgOd8XzKed9tl3--Zbn6qWNUmoKLVjGRIgc_bfRbtcKHIs-_KXbgycKLzU1m4hKipy9J16hgH0J3yfI0oVGeAFE1bnPNcG16g01VoOpxNSj7A76S8ABeachz-fGLzXOW_Abpqq39JJC7Yy3gZwWUZZ15QhbVKGGGeHlZEYLw12I42QFQl4tj2BtaRvsQNqZtdTJZnGTsZppecZlLoZ-3KDxhFruG7Sqi_MrC4vTg-fXVnEoU-H23S-Uh3LKQ3fPOl_g00IJbNBm7t2JjV3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام
😭
اکانت Nous Research سازنده‌ی هرمس ریپلای زد روی توییتم
ولی واقعا قدرت این ترکیب hermes+9router+opencode+mimo هنوز باورم نمیشه که از پس این تسک پیچیده بر اومد</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4635" target="_blank">📅 04:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4634">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بچه‌ها من اگه کمتر هستم این روزا، چون دارم روی یه سری ویدئوی کاربردی کار میکنم که اگر اینترنت قطع شد به دردتون بخوره. و یه سری مهارت که تا اینترنت قطع نشده بهتره یاد بگیرید که بعدا اگر لازم شد آموزشی بدیم، بتونید سر راست برید سراغش</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4634" target="_blank">📅 02:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4633">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard  https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4633" target="_blank">📅 21:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4632">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4632" target="_blank">📅 19:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4631">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دقیقا. درخواست نوشتن راجب ریتالین هم داریم چون متاسفانه خیلیا به خطراتش آگاه نیستن</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4631" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4630">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">متاسفانه من مثال‌های واقعی زیادی از مصرف خودسرانه خیلی از دارو ها دارم میبینم و متوجهم که ما همیشه دنبال یه راهی هستیم که زودتر جواب بده، اما همین راه‌ها هم بدون آگاهی ممکنه شرایط رو بدتر کنه
❤️</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4630" target="_blank">📅 18:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4629">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.  ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4629" target="_blank">📅 18:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4628">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.  ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4628" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4627">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngvd2b927kt5RH5QKeQjxzsN4BZRKNv15f3Ct2zSH6GsgKjN-uLt0QLuzOu0QOWnWWpgFTiFp_TC6zMkvCt7e8FGwJ7apxUjtXjMMsswiXADi0p_V03llnRF4sp7NUb1uKAWnB8fd115_R7fOY4GBcm13pWpeB2L4kHGO7eZXkfQfAWJoPZxfL3JqpOxrOAFWRrCj8jCT-pOu-Or9maYNB4-NEI0iXcf48qJFdnh0WABCYF1ljsRwqlXPLt5uYy3e-CuRwL5XiglBsP3_7oounqnYFRyFVxRPujTmYP9lq13JyJ7PdGsfzUt7GLd1653h-l4jeH2nexCmadQvD9OLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.
ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد ایمن محسوب می‌شه، اما درباره استفاده طولانی‌مدت هنوز اطلاعات کافی نداریم. بعضی مطالعات، مصرف طولانی‌مدت اون رو با افزایش برخی مشکلات سلامتی مرتبط دونستن، هرچند هنوز رابطه علت و معلولی ثابت نشده.
از طرفی، عوارضی مثل خواب‌آلودگی روزانه، سردرد و سرگیجه هم ممکنه در بعضی افراد دیده بشه.
ملاتونین
دارویی هست که به‌صورت آزاد می‌تونید از داروخانه‌ها تهیه کنید؛ پس تحقیق درباره نحوه مصرف و حتی مشورت با یک متخصص قبل از استفاده از اون، اهمیت زیادی داره. معمولاً پزشک با توجه به شرایط فرد، پاسخ بدن به درمان و علت بی‌خوابی، دوز و مدت مصرف رو تعیین می‌کنه. اما اگر قصد مشورت با پزشک رو ندارید، بهتره از مصرف خودسرانه و طولانی‌مدت، به‌خصوص بیشتر از یک ماه، خودداری کنید.
جدای از همه این‌ها، بسیاری از متخصصان خواب معتقدند ملاتونین نباید اولین راه مقابله با بی‌خوابی باشه. تا زمانی که سبک زندگی، بهداشت خواب و عادت‌های روزمره اصلاح نشن، نباید انتظار داشت هیچ دارویی به‌تنهایی مشکل بی‌خوابی رو برطرف کنه.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4627" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4626">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHQWIDaubWxwmBSTJ-4LSIjMbVLphq57GKbA2f4tD0D939unLrJ1b2fftO90J01303Z-5PSWfnPedMvZCKiZ5SqAozGbAwKlKR38VSDQPng-IfL9EhZlUP4bNbBqZeG48Yl3jB2ExlkmbUD4Cd8Xq8ogmhCxdte1gZH3lN-RhmRbPtedPb9DBy-3Fc-tVILPxkOTbOPGxIzy7WMpPfiwtF6t-xe9QAHQTfQrqelM816qXZFZevFxp9QU3fcvW1XfLKT2wOlYSjVWP7hDGiqbDUqFhj3olqX2KHR_2LvReJZ6ZnjzQSOnHKi4X8sVqN0oxzAv2WHQT7bLWuuYKzD77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای فقط داره گند میزنه
الان نفهمیدم واقعا چرا نیازی به 3.6 flash بود
😑</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4626" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4625">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بچه‌های Fireworks AI یه بررسی تخصصی منتشر کردن که نشون می‌ده مدل Kimi K3 نه تنها با Fable در حال رقابته، بلکه ترکیبشون به سطح SoTA (بهترین عملکرد فعلی) تو خیلی از بنچمارک‌ها رسیده و می‌تونه انتخاب خیلی جذابی برای برنامه‌نویس ها باشه.
البته برنامه‌نویس‌های پولدار متاسفانه
😞
https://fireworks.ai/blog/kimik3-fable</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4625" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4624" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4623" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4622" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4621" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4616">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4616" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4616" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4615">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4615" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4607">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4607" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4606">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Anh8Gg-kSJNIp6iAntyb2jrv8wvrFXyJlEEifzx-B0jPfc5pnKHhNSmN6Lfh4J-FICG2N-5DcCNHL9teacsr0rnZyQY9t07yydGFoUiUosZkRFXFZMoJVEsW3PptjM-ukIv50HN63SVQAinwERRb__DlyiSjLUWKVJv4IB2eunw3QosuIM80bE5YflPUc0COAh3EpTgundzab4VwUBhPda-rlBl6GoupxMhPGVT1jp95-QHWQ5vnC-2xnu1mOfeiChVf8gS4qcQNnEEU803nB7u1QTlEhJQkF1EwaweHHD4344E9tj64lM05YOi9n8HGSe8qii4upn28sSGvHDJDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/4606" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4605">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه مقاله توی
exe.dev
خوندم، راجب این بود که اوایل سال ۲۰۲۵ خیلی‌ها می‌گفتن هوش مصنوعی مثل یه «کامپایلر» جدید عمل می‌کنه؛ یعنی همون‌طور که کامپایلر زبان سطح پایین (مثل C++) رو به زبان ماشین تبدیل می‌کنه، هوش مصنوعی هم «زبان طبیعی» (مثلا فارسی) رو به «کد» تبدیل می‌کنه.
اما الان جواب فرق کرده:
نه، کلاد کامپایلر نیست؛ خیلی از اون بهتره!
چرا؟ فرقش چیه؟
توی دنیای واقعی، نرم‌افزار لایه‌لایه ساخته می‌شه.
مدیرعامل استراتژی می‌ده
👈
مدیر محصول فیچر تعریف می‌کنه
👈
آرشیتکت معماری می‌چینه
👈
برنامه‌نویس کد می‌زنه
👈
و در نهایت کامپایلر کد رو باینری می‌کنه.
هرکدوم از این لایه‌ها دارن جزئیات رو مشخص‌تر می‌کنن و کلی
تصمیم‌گیری ا
نجام می‌دن. مشکل اینجاست که ارتباط بین این لایه‌ها پر از اصطکاک، و جلسات خسته‌کننده‌ست.
کار اصلی کلاد اینجاست: هوش مصنوعی می‌تونه
به‌صورت عمودی توی تمام این لایه‌ها حرکت کنه
. کلاد می‌تونه همزمان باهاتون درباره استراتژی محصول بحث کنه، معماری بچینه، کد بنویسه و بهینه‌سازی ماشین رو انجام بده؛ بدون اینکه نیاز باشه واسه هماهنگی اینا جلسه بذارید یا از کسی اجازه بگیرید.
یه مثال واقعی
:
نویسنده‌ی مقاله می‌گه برای سیستمشون نیاز به یه سرور DNS توزیع‌شده و سریع داشتن. به جای اینکه خودشون بشینن کد بزنن، اومدن چند تا ایجنت هوش مصنوعیِ موازی (کلاد و کدکس) بالا آوردن تا کل سیستم رو براشون بسازن.
نکته‌ی جالب ماجرا اینجا بود:
وقتی خروجیِ ایجنت‌های مختلف رو با هم مقایسه کردن، دیدن ایجنت‌ها کلی از مشکلات لبه (Edge cases - مثل وقتی که دیتابیس Rollback می‌شه) رو
خودشون متوجه شدن و بدون اینکه از برنامه‌نویس بپرسن، براش راه‌حل و منطقِ کدنویسی طراحی کردن
.
هرچند اگر نظر منِ متین رو بخواید، ai همچنان نیاز به یک متخصص خوب داره که بتونه دیتاش رو Validate کنه، پس به یادگیری ادامه بدید دوستان خوب من
🔥
🔗
منبع:
https://blog.exe.dev/claude-is-not-a-compiler
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4605" target="_blank">📅 00:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4600" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4600" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htn8j6gyOSbOn-gJjMxxhW0RF0OZhFZghGWP8jhxSof3meW0z4BITdtZO5Z1aTBZ3WoMEMew9BSkFRB_HIA7kwPlaYjPHgTpsXySZLIiLOffTNbuMvbbQJzmen0eKvS_KGrtUhud7ML7JMz-2BqPkl0z7b94NfmUIRUxGJ6RpuRT-UQvfMYWf3XFVd4tlLWbGO0mvTPldCtm43gdPfQbRDZHmExDBzjnKaCDp7m4bXLMEKF5BZiisM62UrfolObi0qmE06RBp_z8emhefkUEZakxbuPtn3JYpIkS4jaMNTGfSE4hqvwChbXd3MxaD1yxnkRfxbmZoahj-rPiHJNH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/4599" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگه شما هم با نمایش متن‌های فارسی در Claude مشکل دارید، ریک سانچز راه‌حلش رو براتون آماده کرده! فعلاً این ابزار برای macOS منتشر شده و کاربران ویندوز باید کمی منتظر نسخه‌ی مخصوص ویندوز بمونن. در طراحی این پروژه، به یاد زنده‌یاد صابر راستی‌کردار، خالق فونت…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4598" target="_blank">📅 16:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PuD3nrPo0330UJpf_87ckFACczp0HruhNA7WPiDQa6mHmqsPMC6N9_7YXwOsNTzNLUaTVv4JQsYEhInCLa_PrA17DXufAvHn0UG7qt3mhUfeToj2v20gHsALVXZ4SRCqB3Y_HDmmiXq08TGhmz04tQiQw0UIOj8mfdp0fEGaGfrDh41WmYu5z1eWcklrpcUBqW6ikBKPo4T9Ysknw-kjKgbD1RxNKascvpUh8qsDtnQiq37u36GIOVAi1oKmzJ2PCZ5vQar91iq_tgq8UNoQ-fJlD1bV3-rxhTgMS7qiX_r-gran4KMYkXW0QVZY3S-aDYfwVegVT7mM1D60nJ_lZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4597" target="_blank">📅 15:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4596">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAkYNkNNtu4oVnL7anGrFDhEVSyyao012nzWY7cGAjrlSp86PvMNi-y0URlU7lUGvwrD4FwPwDbn2CwLwxaOrjs-u3phcpGgvpOiaOx2oBnlSIawSnoXiY-khUemcFZTt4D4FaJUhRNufRfgTDzAXDo80fbaBTFPCznbDVCHhbG2kRtmYLzjmQp0PVBM6J9YFYpFz3pKwbhfsC8WCvjcth5wBP_Vm-f_OrkXAkCSQ8AmTtCylc39c8L87GMyaWKTrUXlp2_A2c4Gw-nQ_fc1iwj0Wwa2xehTAq8wf_oGUxz3D2WdAPDAFTKHl-Jhm38ymb1kEBOUYjz2R5N2M4m0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه شما هم با نمایش متن‌های فارسی در Claude مشکل دارید، ریک سانچز راه‌حلش رو براتون آماده کرده!
فعلاً این ابزار برای macOS منتشر شده و کاربران ویندوز باید کمی منتظر نسخه‌ی مخصوص ویندوز بمونن.
در طراحی این پروژه، به یاد زنده‌یاد صابر راستی‌کردار، خالق فونت وزیرمتن، از همین فونت استفاده شده است.
کافیه لینک زیر رو به Claude بدید و ازش بخواید نصبش کنه؛ بقیه‌ی کارها رو خودش انجام می‌ده:
https://github.com/m4tinbeigi-official/claude-rtl-patcher
به همین سادگی و خوشمزگی!
😄</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4596" target="_blank">📅 14:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tLp1Z8-QALLx6tM-bJl9yn2MZBptj580EwCNaa7ll9xFzVy2K_n_LMQSqF0BVqJI-1srWQaLR2QVW55ZYFlriWLl6v3Nt-m8vkEDP3BWW2WwZOLoShPFO5ZLg6DY-9HJLgFXgJ9uZXlID3Xar4HFuu_ZeQiryTHUYS46uKUBVlJ8p8SV7sqTAhIK1wgaHVO6WoEkgstfPLdyq3GR5Mu_m1khhbFD6uT9SY2YcicPZKX6gdXiinlTBTWZO-ZhExnhq_PQYu9u7MqC8fcafjuC_2KRa4_w40dp4kBAZVKtD_8TJlY4iM9XrdUu0CX0evWq1AjrJqdn9YWg6ms6_-SeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده است.
✨
مهم‌ترین ویژگی‌ها و تغییرات این نسخه:
🔹
نصب سریع با One-Click Wizard:
دیپلوی پنل حالا فقط از طریق ویزارد آنلاین و اختصاصی انجام می‌شود و پس از نصب، یک لینک کاملاً پرایوت به شما می‌دهد (روش‌های نصب دستی روی این نسخه کار نمی‌کنند).
🔹
داشبورد مدیریت داخلی (Admin Dashboard):
امکان آپدیت پنل به نسخه‌های جدید، حذف کامل پنل، و ریست پسورد مستقیماً از داخل خود پنل اضافه شده است.
🔹
راه‌اندازی ربات تلگرام:
مدیریت کانفیگ‌های تکی، دریافت لینک‌های سابسکریپشن و مانیتورینگ مصرف (همراه با هشدار مصرف بالای ۸۰٪) از طریق ربات تلگرام.
🔹
حذف کامل Environment Variableها:
تمام متغیرهای ثابت (مثل VLESS UUID، Trojan Pass، Proxy IPs و...) از داشبورد کلودفلر حذف شده و مستقیماً داخل پنل قابل آپدیت و مدیریت هستند.
🔹
ارتقای چشمگیر امنیت:
لاگین به پنل حالا نیازمند ایمیل کلودفلر شماست.
مسیر ورود به پنل به یک آدرس تصادفی و امن (Secure Path) تغییر یافته (دیگر با زدن
/panel
وارد نخواهید شد).
🔹
تنظیم سریع Custom Domain:
دامنه‌های سفارشی خود را می‌توانید مستقیماً از بخش Common settings وارد کنید تا کانفیگ‌های مربوطه با تگ
D
به سابسکریپشن شما اضافه شوند.
🔹
قابلیت‌های جدید شبکه و پروکسی:
پشتیبانی از Xhttp و VLESS Encryption برای Chain Proxy در هسته‌های Xray و Clash.
🔹
انتقال آسان تنظیمات:
اضافه شدن قابلیت جذاب به‌روزرسانی و همگام‌سازی تنظیمات از یک پنل ریموت BPB دیگر.
⚠️
نکات بسیار مهم برای اتصال کلاینت‌ها:
حتماً کلاینت‌های خود را به آخرین نسخه آپدیت کنید (حداقل Sing-box نسخه 1.12.0 و v2rayNG نسخه 2.2.3 به بالا).
برای اتصال پایدار در v2rayNG، حتماً گزینه
Hev TUN
را فعال کنید.
در صورت مشکل با فرگمنت در برخی ISPها، حالت
Packet
را روی
1-1
تنظیم کنید.
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
@whitedns</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4595" target="_blank">📅 13:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4591">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-poll">
<h4>📊 دوستان پروتکل WireGuard واستون وصل میشه؟</h4>
<ul>
<li>✓ 1- وصل میشه توی Aether، اما پینگ نمیده توی V2ray یا تلگرام🚫</li>
<li>✓ 2- کلا توی Aether هم وصل نمیشه🚫</li>
<li>✓ 3- وصل میشه، اوکی هم کار میکنه✅</li>
<li>✓ 4- دیدن نتایج(حال نداشتم تا الان aether رو ران کنم)🤡</li>
</ul>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.5.0 منتشر شد(با پشتیبانی از MacOS و Linux)  توی این ورژن، هسته (Core) برنامه رو به آخرین نسخه یعنی v1.3.0 ارتقا دادم. که توی این نسخه تمرکز روی پایدار کردن اتصال و اسکنر بوده. یه سری ویژگی کاربردی هم به رابط کاربری اضافه شده.  تغییرات…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4591" target="_blank">📅 01:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4590">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aMfgjxP0XpLJFed0iGRYpp1IC55y7isojiV7FRzVt9etRO0RMJTDfQRhpvOvg0lOSHjvtmOhA-G9aKv4Xl_1u7s6mqG77UZOETsh66O-BcTbCJD0U_YwcDQ_LCn8KBuMANDmGoxtg2ltIzOTIBotuHR05elAQlSJCZ7ige3irWzZCfypGlWb2acimlTdRj8gh3dzHNQbL37eFapDO_xHfvqKCcQrwRYhW2A1DB-NE8AhR8heAqKiWD-Ks3CnQLSkBGzjnxm0cKGCOfdOyOBnP-io44L1cQPnR6EUWdAKKf7IBs2lypac9Gj9fBALne1biGf37rxnU231PT4dpn_d1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.5.0 منتشر شد
(با پشتیبانی از MacOS و Linux)
توی این ورژن، هسته (Core) برنامه رو به آخرین نسخه یعنی v1.3.0 ارتقا دادم. که توی این نسخه تمرکز روی پایدار کردن اتصال و اسکنر بوده. یه سری ویژگی کاربردی هم به رابط کاربری اضافه شده.
تغییرات اصلی این نسخه:
1-
اسکنر قدرتمند Ironclad:
بقیه حالت‌های اسکن فقط چک می‌کردن که آیا Gateway پینگ می‌ده یا نه. اما Ironclad یه تونل کامل و واقعی می‌سازه و یه درخواست HTTP ازش رد می‌کنه تا صددرصد مطمئن بشه که کار می‌کنه. یکم کندتره، اما قطعی‌ترین حالت ممکنه
2-
اتصال مجدد (Reconnect) هوشمندتر:
قبلاً اگه اتصالتون قطع می‌شد، Aether می‌رفت از صفر کل آی‌پی‌ها رو اسکن می‌کرد (که تو حالت‌های سنگین ممکنه چند دقیقه طول بکشه). الان اول همون آی‌پی‌ای که تا دو ثانیه پیش کار می‌کرد رو دوباره چک می‌کنه؛ اگه واقعاً مرده بود تازه می‌ره سراغ اسکن کامل
3-
اضافه شدن بخش Obfuscation:
این قابلیت دستتون رو باز می‌ذاره تا شدت مخفی کردنِ هندشیک از سیستم‌های فیلترینگ (DPI) رو تنظیم کنید. پروفایل‌هاش با توجه به پروتکلی که انتخاب می‌کنید (MASQUE یا Wireguard) متفاوته. اگه دیدید رو حالت دیفالت وصل نمی‌شه، درجه‌ش رو ببرید بالا
4-
تغییر پورت و Bind Address:
الان می‌تونید پورت SOCKS5 رو به دلخواه تغییر بدید یا اینکه روی آی‌پی
0.0.0.0
ست کنید تا پروکسی رو به کل شبکه‌ی لوکال (مثلاً موبایل‌ها یا تلویزیون تو خونه) Share کنید. اون باگ کلافه‌کننده‌ی پروتکل UDP هم بالاخره تو هسته فیکس شده و الان بدون مشکل توی شبکه‌ی لوکال کار می‌کنه.
5-
پشتیبانی کامل از مک و لینوکس:
این اولین نسخه‌ایه که کاملاً مولتی‌پلتفرمه! فایل‌های نصب ویندوز (exe و msi)، فایل‌های مخصوص مک (برای چیپ‌های اینتل و اپل سیلیکون به صورت جداگانه)، و انواع پکیج‌های لینوکس (deb، rpm و AppImage) رو براتون گذاشتم
6-
رفتن به System Tray:
گزینه‌ای اضافه شده که وقتی برنامه رو می‌بندید، به جای خروج کامل، بره تو تسک‌بار پایین ویندوز و همونجا تو پس‌زمینه کارشو بکنه
ممنون از
@rqzbeh
عزیز بابت مشارکت‌هاش تو این آپدیت؛ و ممنون از
@CluvexStudio
عزیز بابت زحماتش روی هسته‌ی برنامه
لینک گیت‌هاب برای دانلود نسخه‌های مختلف:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.5.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4590" target="_blank">📅 00:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4589">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بعد میگن شبکه‌های اجتماعی چطوری پول در میارن
"Data"</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4589" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4588">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اون روز داشتم از claude راجب s3 storage سؤال می‌کردم و کمی داشتم دانشم رو بالاتر میبردم، صرفا سوال جواب بود فرداش فید گوگلم پر شده بود از خرید فضای ذخیره سازی s3 و کمترین قیمت s3 و...</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4588" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4587">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اون روز داشتم از claude راجب s3 storage سؤال می‌کردم و کمی داشتم دانشم رو بالاتر میبردم، صرفا سوال جواب بود
فرداش فید گوگلم پر شده بود از خرید فضای ذخیره سازی s3 و کمترین قیمت s3 و...</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4587" target="_blank">📅 00:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4586">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه مقدار برای همین طول کشید. اما خودم هم بیلد رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4586" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4585">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">در حال آپلود</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4585" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4584">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C54Dl2yiKT0ow2egJNKtlOZ59-ST_YcibhUDmEjJhQ6XRVvgyc0OuPIiCiIDbgmzAOXSOSaQsQzi9YiCoFxpi6w7dczh6sr8eAzzlTuEy9hU5U9JYmMjWX6Q4tZi6JJKKTZNZUEtKlZ8J8MvVgQmIRDILbBYIXV7BfdVmC8xE53PuzUUWH4x0BhHoKuxhfnQPHoszGpa1cPGSDaVLc_Yo4hX-rJFNz_m6AlUc-1_4IfP6FrNT7TMa_Luvve3dzloa1zLKp99gXKRRe1tKm7XEBVcuGEl_XxlDb9KaMyvGEtTxWFVIHbZy6QkGSFAou4OfhloTpCfe5NNnpDPs2TSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی تغییرات جدید به GUI اضافه میشه
🙏</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4584" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4583">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4583" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4582">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هکرها زدن کل دیتابیس ثبت اسناد و املاک رومانی رو پاک کردن:)))
یه هکر الجزایری به اسم ByteToBreach (که اسم واقعیش زکریا محجوب از شهر وهران الجزایره و قبلاً هم پورتال دولت سوئد رو هک کرده بود) با استفاده از اطلاعات ورودِ یه کارمند، وارد شبکه‌ی سازمان کاداستر (ثبت اسناد و املاک) کشور رومانی می‌شه.
هکر اول کل سیستم‌ها رو مپ می‌کنه و اسناد و اطلاعات کارمندا رو می‌دزده، بعد سعی می‌کنه ازشون باج بگیره. وقتی دولت رومانی باج رو نمی‌ده، هکر کل دیتابیس ثبت اسناد کشور رومانی به اضافه‌ی بکاپ‌های آنلاینشون رو پاک می‌کنه
😂
(یعنی عملاً کلاً نابودشون کرده).
این کار باعث شد کل بازار املاک و مستغلات رومانی فلج بشه و دفاتر اسناد رسمی نتونن هیچ سندی رو ثبت کنن. هکر هم دیتای دزدیده شده رو تو یه فروم دارک‌وب گذاشته برای فروش
👌
خب باج رو بهش میدادین دیگه ای بابا
مقامات رومانی گفتن که دارن کل شبکه رو از صفر می‌سازن. با اینکه هکر ادعا کرده تمام بکاپ‌ها رو پاک کرده، اما خبرنگار ریسکی‌بیزنس (Risky Biz) می‌گه به احتمال زیاد اونا یه نسخه‌ی بکاپ آفلاین (Cold Backup) داشتن، چون اگر اصلاً هیچ بکاپ آفلاینی نداشتن، فاجعه‌ای تو رومانی رخ خواهد داد که تا ماه‌ها نمی‌تونن ثابت کنن کی صاحب کدوم زمین و خونه‌ست! یا اینکه باید برن از دارک وب، اطلاعات خودشونو بخرن
😂
😂
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4582" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4581">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BvqPL83U-9DZADlCl8g2Woup7uWCFuBBwidyDNHBvFI-YLSn8ZTSq91fd6UD-NmsjoOPif9APFalX3QCp0N7nAZjss8ovNNO-M8a967i0003EYV1Ig2cH51B3xbk1m_pWN8t7FFVD3QqSHFZOckPWvDsv8LaVeRdWVJo2hNve-H7nz0dSNG8zIj4yEg8SqvPlN76WLR3ICnzowMkvSjjYetb62clc0ko57rKeJZ6srrM-rHQlTzNzEf53UlwuCVuAfUw5fHvd7zJewPgC8bLWNJvh-Ow-7AHSm6-KMd9sTXCnZ7mmIfCj4uBoJOsuxEO8Pswje2ianeEzATRs0CAug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4581" target="_blank">📅 14:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4580">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آپدیت جدید Aether v1.3.0:  https://github.com/CluvexStudio/Aether/releases/tag/v1.3.0  توی این ورژن بیشتر روی اسکنر و پایداری اتصال کار کردم:  یه حالت اسکن جدید اضافه کردم به اسم Ironclad توی این حالت برای هر IP کاندید Aether یه تونل واقعی و کامل میسازه و…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4580" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4579">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether v1.3.0:
https://github.com/CluvexStudio/Aether/releases/tag/v1.3.0
توی این ورژن بیشتر روی اسکنر و پایداری اتصال کار کردم:
یه حالت اسکن جدید اضافه کردم به اسم Ironclad توی این حالت برای هر IP کاندید Aether یه تونل واقعی و کامل میسازه و یه درخواست HTTP واقعی از توش رد میکنه نه فقط یه پینگ ساده. :))
یعنی اگه یه Gateway رو با این حالت انتخاب کنه مطمئنید که واقعا کار میکنه نه فقط جواب پینگ داده. کندتر از بقیه حالت‌هاست چون کار بیشتری میکنه... ولی از نظر قطعیت بهترین گزینه‌ست و همینو پیشنهاد میکنم.
- ریکانکت سریع‌ تر بعد قطعی قبلا اگه تونل قطع میشد (چه MASQUE چه WireGuard) Aether مستقیم میرفت سراغ یه اسکن کامل از صفر که توی حالت‌های سنگین‌ تر مثل Ironclad میتونست چند دقیقه طول بکشه. الان اول همون Gateway قبلی که کار میکرد رو یه تست سریع میگیره
و فقط اگه اون دیگه جواب نداد میره سراغ اسکن کامل.
فیکس UDP روی SOCKS5 وقتی پروکسی رو روی شبکه لوکال باز میکردید اگه AETHER_SOCKS رو روی یه آی‌پی غیر از
127.0.0.1
ست میکردید تا از دستگاه‌های دیگه توی شبکه هم بشه وصل شد
بخش TCP درست کار میکرد ولی UDP هیچ‌ وقت رد نمیشد
فیکس کردم. (گزارش یکی بود issue )
پشتیبانی از OpenWrt یه بیلد استاتیک جدید اضافه شد (aether-linux-armv7-musl.tar.gz) که مخصوص روتر های OpenWrt و سیستم‌های مبتنی بر musl هست.
(یکم مشکل بود این قسمت، کلی وقت گرفت، یکم دیر شد سر این بود)
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4579" target="_blank">📅 09:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گویا شرکت Moonshot ، توسعه‌دهنده‌ی مدل چینی Kimi 3 انقدر به خاطر تهاجم مردم فشار اومده به سرورهاش که کلا فروش اشتراک‌های جدید رو متوقف کرده:))
همینطور اونایی که قبلاً اشتراک ۲۰ دلاری رو خریدن هم شاکین. چون مدل سنگینه، توکن‌ها خیلی سریع‌تر از مدل‌های قبلی مصرف می‌شه و کاربرها می‌گن بودجه‌ی هفتگیشون تو دو روز اول تموم می‌شه. (این رو با مدل قبلی یعنی K2.5 که خیلی به‌صرفه‌تر بود مقایسه می‌کنن).
توی فروم‌های تخصصی (مثل Hacker News) بحثِ جالبی راه افتاده؛ خیلیا می‌گن دقیقاً به خاطر همین مشکلاته که ما باید به سمت مدل‌های اوپن‌سورس و اجرا روی سخت‌افزارهای خودمون بریم، وگرنه حتی بزرگ‌ترین استارتاپ‌ها هم یه جایی زیر بارِ ترافیکِ مدل‌های هوش مصنوعی زانو می‌زنن.
هرچند توی ایران متاسفانه نمیتونیم زیاد به همچین چیزای گل و بلبلی که خارجیا میگن واقع‌بینانه نگاه کنیم</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4578" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هرچقدر بگم هرمس برای تحقیق و پیدا کردن گسترده‌ی یه چیزی عالیه کم گفتم</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4577" target="_blank">📅 23:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4576">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبر فوری :  ‏اگر سایت وردپرسی دارید حتما هسته وردپرس رو آپدیت کنید دو تا باگ SQL Injection و RCE داره  نسخه های اصلاح شده: WordPress 6.8 → 6.8.6 یا جدیدتر WordPress 6.9 → 6.9.5 یا جدیدتر WordPress 7.0 → 7.0.2 یا جدیدتر    @Linuxor ~ seramo_ir</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4576" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4575">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">خبر فوری :
‏اگر سایت وردپرسی دارید حتما هسته وردپرس رو آپدیت کنید
دو تا باگ SQL Injection و RCE داره
نسخه های اصلاح شده:
WordPress 6.8 → 6.8.6 یا جدیدتر
WordPress 6.9 → 6.9.5 یا جدیدتر
WordPress 7.0 → 7.0.2 یا جدیدتر
@Linuxor
~ seramo_ir</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4575" target="_blank">📅 20:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4574">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qt3pkiQDYxpkP7AstfvcQ5R9bVb3dCuWl7cw7rLj1oGRvm_Zy5sZiHqIWHTfVQgsmuwfIlL0Oj9_DrGf462D4zG36pHcSEquk4cbfICbW6t3j884WKAEKk4QZghKZdol9dzQwHxZNnhBX9hI9Kf7FOnpTzho6YRSKd_-j59mAJLHlj4EorPMmL3YljixMrQKZ9DmTMLDml0sZABk0b_pvluUG6ag6-qx1l1puy0cxX2JwfGKSpTUx4h2dNzn1JojJrG1WDhMTY24A0fjoIPMIlGWKlam2iFceye8vaGup6lCI9DIp9UEKHueBoUmdM8tDqmUlfGj2oZCP2bzxZ73Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌های متخصص امنیت (که توی حوزه SOC و Red Team فعاله) یه سایت و کامیونیتی زده به اسم VulnCity (شهر آسیب‌پذیری‌ها). که یه مرجع جامع و دورهمی برای بچه‌های امنیته.
1- مقالات و آموزش‌های دست‌اول: مؤسس سایت هر چیزی که توی پروژه‌های واقعی (مثل Red Teaming) یاد می‌گیره رو به‌صورت مقاله می‌ذاره اونجا.
2- شبکه‌سازی: بچه‌های امنیت می‌تونن با هم چت کنن، پروفایل همدیگه رو ببینن و یه تیم بسازن.
3- بخش Vulndark: یه قسمت باحال داره که اخبار مارکت‌های فعال دارک‌وب، فعالیت گروه‌های هکری و خبر لو رفتن دیتابیس‌ها رو پوشش می‌ده.
آدرس سایت:
🔗
https://vulncity.com
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/4574" target="_blank">📅 20:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4573">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فرق H3 و H2 برای من روی یه اینترنت، 18 و 2 مگابیته
یعنی H2 سرعتش پایینتره
همینطور وایرگارد و gool هم برای من همون سرعت H3 رو دارن</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4573" target="_blank">📅 20:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4572">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">من حس میکنم به قدرت gool پی نبردید
یه تست بکنید جداً</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/4572" target="_blank">📅 14:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4571">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-poll">
<h4>📊 حالا دوستان MASQUEـی، بهم بگید کدومش بهتره توی آپلود/دانلود؟</h4>
<ul>
<li>✓ http/3</li>
<li>✓ http/2</li>
<li>✓ مسکی نیستم دیدن نتایج👺</li>
</ul>
</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/4571" target="_blank">📅 14:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-poll">
<h4>📊 توی Aether بیشتر روی کدوم پروتکل بودید و براتون بهتر بوده تا الان؟</h4>
<ul>
<li>✓ 1- MASQUE</li>
<li>✓ 2- Wireguard</li>
<li>✓ 3- Gool(warp-in-warp)</li>
<li>✓ استفاده نکردم</li>
</ul>
</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4569" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
اگر دنبال یه آرشیو کامل از یاد گرفتن ساخت کانفیگ با سرور شخصی و تمام روش های
#اینترنت
آزاد هستید از مبتدی تا حرفه ای میتونید از این آرشیو کامل که یکی از بچها زحمت کشیده و آرشیو بسیار کاملیه استفاده کنید.
لینک سایت:
👇
(باز نشد با فیلتر برید)
filtershekan.sbs
خلاصه:این سایت برای تمام آموزش
#امنیت
ساخت
#کانفیگ
و تمام روش هایی که شما رو میتونه با کمترین هزینه و رایگان وصل کنه رو گذاشته.
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4568" target="_blank">📅 13:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">اطلاعیه:
سطح پهنای باند و کیفیت اتصال اینترنت در تمامی اپراتورها و دیتاسنترها به‌طور قابل‌توجهی کاهش یافته است. بررسی‌ها نشان می‌دهد ظرفیت پهنای باند نسبت به روز گذشته کاهش محسوسی داشته است.
همچنین برخی رسانه‌ها از اختلال یا قطعی در خطوط انتقال پهنای باند و زیرساخت شبکه در برخی مناطق کشور، به دلیل حملات منتسب به آمریکا، خبر داده‌اند. :))</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/4567" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آپلود عملا مرده</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/4566" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvVcwPHWo3ZyEg5E43TnFajrCgnI5or2bQGzuVC1JAC-HeZUaL_beJlQgfs5osLtY2C27-kQSNgruaEwITogbbzqc7lasPXWv36Ho9wSpC7bGx7kjdbMShviRoQKdOGVQAdFMEbGnH6NtRYfFxkLvx7Fqm_3h6dYh1lwo_-OLeWy0lPCyYVlKfA2iPgRwpiLsJl8Znm1EewjpG8UiHcagSLPJa8YUHU4uGfoHRYi2_rHE21XeR5c5ikesv9GUSb4-frI9Y0CX1qu5y2e2yhm9bOw_VkWGwLYRpqO7bRly18578BpseEteGVOvrUBVX6fsSpzQhP4zZ6sn2M9h-n7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کپچایی بود خدایی حالم بد شد
کم کم ما ربات تشخیص داده میشیم،‌هوش مصنوعی انسان</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/4565" target="_blank">📅 22:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d80c0238b.webm?token=IwEKgM5DA_GHrMZgf4L7arvFjsgZP2WazpZUJdCwLSfsu2x28H-VHwaqjLCcZ6Us9OvNUl8mSChKZtgiip6Q7i7e_ELJs7YYBjs9u8WfG2G_gcKzkD50R7qk_5-g7MVmYO0AjyRTreioHBMuG9y4SluN7lxq1D_9EQFhs9g47IKyyEUgNaVPj-eZ4bpCoyPq4_h59OPORDh-pJPbo8hqfYatK5WiOxrbfpNC-0xRqQunrYjyyodZX_QkryY3ztAdthbCnK7_uoFIyboLjHpOpFJdBFvLBjyDs0PoDo9jBbGACVLyxJtnBiJCW1rf-uAeiE5U3xupYIACgSift8HCug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d80c0238b.webm?token=IwEKgM5DA_GHrMZgf4L7arvFjsgZP2WazpZUJdCwLSfsu2x28H-VHwaqjLCcZ6Us9OvNUl8mSChKZtgiip6Q7i7e_ELJs7YYBjs9u8WfG2G_gcKzkD50R7qk_5-g7MVmYO0AjyRTreioHBMuG9y4SluN7lxq1D_9EQFhs9g47IKyyEUgNaVPj-eZ4bpCoyPq4_h59OPORDh-pJPbo8hqfYatK5WiOxrbfpNC-0xRqQunrYjyyodZX_QkryY3ztAdthbCnK7_uoFIyboLjHpOpFJdBFvLBjyDs0PoDo9jBbGACVLyxJtnBiJCW1rf-uAeiE5U3xupYIACgSift8HCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز : ترامپ از کشته شدن سربازانش بسیار عصبانی و خمشگین شده است.</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/4564" target="_blank">📅 22:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سرعت نت من به شدت پایین اومده. از 30 مگابیت به 2 مگابیت عملا. با و بدون وی پی ان هم فرقی نمیکنه
نمیدونم چه گندی دارن می‌زنن باز</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/4563" target="_blank">📅 21:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رفقا یکی از دوستان من به اسم محمد، خارج از کشور هستش و برنامه‌نویس Back-end با بیش از ۵ سال سابقه کار هستش و روی پروژه‌های مختلفی از جمله سیستم‌های رزرو پرواز، پلتفرم VOD، مارکت‌پلیس، سیستم‌های پرداخت، احراز هویت، پنل‌های مدیریتی و معماری میکروسرویس کار کرده.
تکنولوژی‌هایی که بهشون مسلط هست:
Node.js • TypeScript • PostgreSQL • Redis • Docker • RabbitMQ • Microservices • Prisma • REST API
هم برای همکاری Remote میتونه اقدام کنه، و هم اگر فرصت مناسبی باشه، برای Relocation مشکلی نداره
حیفه که از چنین استعدادی استفاده نشه
😁
لینکدینش:
https://www.linkedin.com/in/mr-ln
آیدی تلگرامش:
@MRLN2001</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/4562" target="_blank">📅 20:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این وسط مدل Claude Fable 5 موندگار شد.
آنتروپیک اعلام کرده که از ۲۰ جولای، مدل Claude Fable 5 رو توی همه‌ی پلن‌های Max و Team Premium (با ۵۰ درصد محدودیت‌ها) نگه می‌داره. کاربرای Pro و Team Standard هم می‌تونن با استفاده از Credit بهش دسترسی داشته باشن و یک اعتبار ۱۰۰ دلاری هم دریافت می‌کنن. به نظر میاد فشار رقابت سنگین با GPT-5.6 Sol و Kimi 3 باعث شده آنتروپیک از برنامه‌ی قبلیش برای حذف کردن Fable 5 از پلن‌های اشتراکی عقب‌نشینی کنه که خب قابل پیش‌بینی بود
🤤</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/4561" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مدل Kimi 3 اومده با context یک میلیونی و به نظر خیلی خفن میاد
هرچند همیشه گفتم به بنچمارک‌ها اعتباری نیست، باید در عمل دید که چیکار میکنه</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/4560" target="_blank">📅 20:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یکی از بچه‌ها به اسم ارشیای عزیز این ایمیل رو بهم داد، برای خرید سرور:
من از hostvds خریدم. ۹۹ سنت هزینشه، یه ۴۹ سنت خرج می‌کنی ترافیکش‌ نامحدود میشه. هزینه رو یه دفعه کم نمیکنه ساعتی کسر میشه. اگه یه دفعه آیپی فیلتر بود میتونی سرور رو حذف کنی یدونه دیگه دیپلوی کنی.
پرداخت کریپتویی داره
با ایران مشکلی نداره
۲ ماهه باهاش مستر dns و پنل ثنایی فعال کردم.
پایداری و سرعتش خیلی خفن نیست ولی بدک هم نیست.</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/4559" target="_blank">📅 18:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PmcfXh-4deFjP-yvAUCd4oWQmExXzAYiGP3JhQHOPdhw0XyoDJNIBwdxy2CbuKuCo8gQ3EV6Yj2wgFx6Nsf20jfU7P2KiVlFIWbglcS-570Lrq7XA4Q0RA7pUzF3kF7MRgmVLRq6ecp4rjkzypuwK7S35P-va4-GvjLl4oZ07_ErEYoubTenKVAsFoukQaTGl3Hafz5OOhwteUfrC2VxoFmIA9YVbegJkYQf_ghy9D39faMAIeO0YtTu4BF-YMypzV1_cptYwOcvdTQUgRC7HIJQTVZcORHzTBCTE56xGgmNl4TtWOqFj0e2cXPYL01nkMkSJbf3DKm_ojG2IcvI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان گویا yotta src روی سرورهایی که برای masterdns استفاده میشن، ابیوز میزنه و سرور رو بدون اطلاع قبلی می‌بنده. لطفا دیگه به این قصد ازش خرید نکنید تا اطلاع ثانوی
و میگردم سایت اوکی پیدا میکنم واسه‌ی خرید سرور با کریپتو باز هم</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/4558" target="_blank">📅 12:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">پاول دورف و ایلان ماسک هردو گفته بودن اگه دانشجو هستید بهترین چیزی که میتونید یاد بگیرید ریاضی و فیزیک هستش
راستم میگن اما حرفشون یه اشکالی داره، یادگیری ریاضی فیزیک برای پولدارا و بی دغدغه هاست، برای مثال به خصوص توی ایران یادگیری ریاضی و فیزیک درامد خوبی نداره و شمارو اصلا وارد Positive Feedback Loop نمیکنه که توش پیشرفت کنید، ولی واقعا راست میگن من خودم اگر هیچ دغدغه مالی نداشتم تا آخر عمر ریاضی و فیزیک یاد می‌گرفتم چون جز بنیادی و مهم ترین ابزار های فکری بشر هستن!
@Linuxor</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4557" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4556">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستان عزیز لطفا مراقب خودتون باشید و توی جاده و نزدیک پل‌ها تردد نکنید اصلا
خیلی خطرناکه این روزا</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/4556" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4555">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N3xzhjprVJPJRvShK_ooqkAmNbFOIMYqfWatHVzxn0ztNTcxXHciWHQqqy7k_KR1Zd7QxlgDSAEtoJyeQnEhTtTBQWVGb3j8j0va0VMSp81JpCONmKegBS5HDdwe7RrrwEx43xhiF8_ASqSACSc2ahM4fQZ0_5qWm1lV1mdV7rUbxhPuRRWx9b2xmwV9SDOPxWCViE2dKxwrosoPAD4Slvfk3_jY5UG3renisDL4nveArMxlj2JmOCyGKiySHQNEaMXF4mpdGu858Q-_f9I9jUSjEPpxKGpIfTa__J_xvF1tZ7yfQba_OBrBDhCta5pFbq64UEJ6NX0C50DoQrTLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسایی که تا الان براشون کانکت نشده بود، یا کار نمیکرد، حدسم اینه به احتمال 90 درصد واستون کار کنه با تغییر پروتکل ارتباطی Masque به http2. من تا الان Masque روی نت مخابرات واسم کار نمیکرد، اما با این ورژن جدید دارم همین پیام رو میذارم با MASQUE+Turbo+Ipv4+Http2</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/4555" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4554">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید! نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن 1.2.0 ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک: قبل از این، بخش Validation ابزار با پینگ…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4554" target="_blank">📅 02:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4552">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/thczGdPFeWcE1UZG-jfbVlCehkdwinGxR8jMF5CxD4TnCi2K7CearCVs3Vz4licyt6kmLW86jdwxToNzdJmCnIgVKQnq4b_CPNVr_imIDq1z4_3F_x4rSbslGEoXNmpkCz-P4EGCrHLjUjlAWBPtdkTYnIuCvFAZyRHrQu_YB7rexshmARn8z-tVtumApez4Prby3hUbfQROai3FoXgkUtrzDWmRuw3VTqx4GOcYdVgsaxPbams88fo4SPtfKWBWIIM0w_kUF-rqtYmFrK48sezobMo01bbx1S0e6VQqehA2_HO5AQmjJAXtK0187QiC6mZERJo8ZwWJnRbbwD2LcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aAYbUsGiHYbnvWqxeC55653MEZBbMjelm_OnsA8--nPBccQ4sMkTOqSXX6ghyYM-lTPOKBo_QkdGSM4f673CJAmvYcPBNwBqlhYLnl9WJ3dL2xmXfeTpKjunkxIHYx_O4ZYKSKJsvK7OscWwmNa71mrf3S305J9Pt42Uw-ZriIzJiBZ32DDGwA6-vxIgWS_U8bJwu6KyHaHQT0hVVWG3GqbFP4iIcBpxIY0KY0K2S6l7oOVRzzAU5jZRpoO63vv-v076nnJmfcy9APm1a0eZePr4-gZsqbpVQt_w1AZKsQoH8SyEbIYHbPFU7jtzCSjQ30yH3nxz1useRSPFweYudw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید!
نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن
1.2.0
ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک:
قبل از این، بخش Validation ابزار با پینگ کردن
1.1.1.1
(که داخل شبکه‌ی خود کلودفلر هست) وضعیت رو متصل نشون می‌داد؛ در حالی که ممکن بود ترافیک واقعی اینترنت قطع باشه و لود نشه. حالا ابزار یک ریزالور خارجی رو هدف قرار میده و باید ۲ بار پشت هم موفق بشه. یعنی وقتی می‌نویسه Connected، واقعاً متصله.
🔵
اضافه شدن انتخاب ترنسپورت برای MASQUE:
توی بخش Advanced الان می‌تونید نوع پروتکل ارتباطی MASQUE رو تغییر بدید:
HTTP/3 (QUIC):
حالت پیش‌فرض؛ سریع‌ترین هاندشیک و بهترین کارایی (اگر شبکه شما با UDP مشکلی نداشته باشه).
HTTP/2 (TCP):
کاملاً شبیه به ترافیک عادی HTTPS؛ مناسب برای زمان‌هایی که شبکه شما UDP/QUIC رو اختلال می‌اندازه یا مسدود می‌کنه.
تنظیمات انتخابی شما به‌طور خودکار ذخیره و در استارت‌آپ بعدی اعمال میشه. (این سوییچ فقط روی پروتکل MASQUE تاثیر داره و برای WireGuard/gool غیرفعاله).
🔵
به درخواست دوستان فرانت کار لوگو هم از دیفالت عوض شد
🤠
دانلود نسخه 0.4.0:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/4552" target="_blank">📅 01:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4551">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به زودی به GUI هم اضافه‌ش میکنم</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4551" target="_blank">📅 22:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4550">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether منتشر شد.
v1.2.0
چند تا مشکلی که گزارش کرده بودید توی این نسخه برطرف شده:
- مشکل اینکه بعضی وقتا تونل ظاهرا وصل میشد ولی هیچ سایتی باز نمیشد فیکس شد.
یعنی SOCKS5 فقط وقتی باز میشه که مطمئن باشه
تونل واقعا کار میکنه... :))
مشکل دیر reconnect شدن روی MASQUE HTTP/2 هم برطرف شد.
الان براش HTTP/2 PING اضافه کردم و خیلی سریع ‌تر تشخیص میده.
اسکنر MASQUE هم بهتر شده
چند تا رنج IP رسمی Cloudflare که برای MASQUE استفاده میشن به اسکنر اضافه کردم، همراه با پورت‌ های بیشتر
در نتیجه شانس پیدا کردن Gateway سالم بیشتر شده.
موقع اجرای MASQUE هم دیگه راحت میتونید بین
HTTP/3
و
HTTP/2
انتخاب کنید.
کنار هر گزینه هم یه توضیح کوتاه گذاشتم که بدونید کدوم برای چه شرایطی بهتره.
به طور خلاصه:
HTTP/3
برای شبکه‌های عادی و سالم
HTTP/2
برای وقتی که UDP یا QUIC محدود شده
لینک پروژه هسته:
https://github.com/CluvexStudio/Aether
اگه خوشتون اومد از این پروژه، میتونید Star بدید بهم :))
Readme
هم بخونید حتما!</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4550" target="_blank">📅 22:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4549">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
فیلترنت به طرز همیشگی افتضاحه و عملا سرعت آپلود نداریم داخل هر پنلی چه کلودفلر چه سرور شخصی با ی راه وضعیت بهتر کنید.
دی ان اس گوگل اختلال زیاد داره داخل هر اپلیکیشن وارد کردید کانفیگ رو دنبال گزینه Dns بگردید و هر مقدار بود بزارید روی این مقدار مشکل حل میشه:
9.9.9.9
9.9.9.12
149.112.112.112
9.9.9.9
💡
داخل پنل هم دارید تغییر بدید این واسه همه اپرارتور ها جوابه بهتر از کلودفلر و گوگل هست تو این شرایط.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4549" target="_blank">📅 21:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4548">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مدل Fable 5 - بودجه 100$</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4548" target="_blank">📅 21:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4547">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مدل Fable 5 - بودجه 100$</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4547" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4546">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مدل GPT 5.6 Sol - بودجه 100 دلار</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4546" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4545">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مدل Fable 5 - بودجه 25$</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4545" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4544">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مدل GPT 5.6 Sol - بودجه 25 دلار</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4544" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4543">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یه آزمایش خیلی جالب توی وبلاگ TryAI انجام شده. اومدن یه محیط ایزوله ساختن و به دو تا از قوی‌ترین مدل‌های هوش مصنوعی یعنی Claude Fable 5 و GPT-5.6 Sol، یه آهنگ (Uptown Funk از برونو مارس)، یه متن از لیریکس آهنگ، یه سری ابزار (مثل سرچ وب، دسترسی به APIهای تولید ویدیو و ابزار تدوین ffmpeg) و یه بودجه مشخص دادن.
هدف این بود که مدل‌ها رو به حال خودشون رها کنن تا صفر تا صد یه موزیک ویدیو رو خودشون کارگردانی و تدوین کنن! هر مدل با دو تا بودجه‌ی ۲۵ دلاری و ۱۰۰ دلاری تست شد. نتایج و درس‌هایی که از این آزمایش گرفتن خیلی جالبه:
1- آزادی عمل تو انتخاب ابزار: هر مدل روش متفاوتی رو پیش گرفت. مثلاً کلاد تو هر دو حالت فقط رفت سراغ تبدیل «متن به ویدیو» (Text-to-Video). اما مدل Sol تو بودجه‌ی ۲۵ دلاری، اول عکس ساخت و بعد عکس‌ها رو متحرک کرد (Image-to-Video) و تو بودجه‌ی ۱۰۰ دلاری همزمان از ۳ تا مدل ویدیویی مختلف برای ساختن شات‌هاش استفاده کرد.
2- درک سطحی از شعر: هوش مصنوعی لیریکس رو خیلی لغوی و تحت‌الفظی می‌فهمه! مثلاً وقتی خواننده می‌خونه "Make a dragon wanna retire" (می‌خوام اژدها رو بازنشسته کنم)، هوش مصنوعی دقیقاً یه اژدهای واقعی میاره تو تصویر!
😂
3- مشکل در ریتم و تدوین: با اینکه مدل‌ها با ابزار ffmpeg بیت (Beat) آهنگ رو پیدا کردن و کات‌ها رو روی ضرب آهنگ زدن، اما حرکات داخل ویدیو (مثل رقصیدن یا حرکت دوربین) اصلاً با تمپوی آهنگ هم‌خونی نداشت و یه‌کم تو ذوق می‌زد.
4- کم‌کاری توی بازبینی: یکی از نقاط ضعف بزرگ مدل‌ها این بود که اصلاً خروجی کار خودشون رو نقد و اصلاح نمی‌کردن. یعنی وقتی یه شات رو تولید می‌کردن، همون رو می‌چسبوندن تو ویدیو و دیگه برنمی‌گشتن که افکت بهتری روش بندازن یا اگه بی‌کیفیت بود حذفش کنن. (به قول معروف چشم‌بسته تحویل می‌دادن).
5- بودجه‌ی اضافی کمکی نکرد: دادن ۱۰۰ دلار بودجه واقعاً زیاد بود! هیچ‌کدوم از مدل‌ها نتونستن از تمام این ظرفیت استفاده کنن (نهایتاً حول‌وحوش ۳۶ تا ۴۸ دلار خرج کردن). می‌تونستن با این پول کلی عکس ثابت از کاراکترها بسازن تا مشکل تغییر قیافه‌ها تو طول ویدیو حل بشه، ولی هیچ‌کدوم به این راهکار فکر نکردن.
6- هزینه‌های پنهان: با اینکه بودجه تولید ویدیو محدود بود، اما هزینه‌ی توکن‌های خود LLM برای کلاد به شدت گرون‌تر دراومد (حدود ۱۷ تا ۲۵ دلار فقط پول توکن)، در حالی که این هزینه برای مدل OpenAI زیر ۴ دلار بود. با این حال تیم سازنده به صورت سلیقه‌ای، خروجی ۱۰۰ دلاریِ کلاد رو بیشتر از بقیه پسندیدن.
حرف آخر:
هیچ‌کدوم از موزیک ویدیوهای نهایی شاهکار از آب درنیومدن و هنوز شکافِ بزرگی تو انسجام داستان، ثبات چهره‌ی کاراکترها و خلاقیت تدوین وجود داره. اما اینکه یه هوش مصنوعی خودش بره مدل ویدیویی انتخاب کنه، پرامپت بنویسه، ویدیو بسازه و با ابزارهای خط فرمان ادیتش کنه، یه کم ترسناک ولی باحاله!
لینک مقاله اصلی با ویدیوها:
https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6
سورس کد این پلتفرم (اگه می‌خواید خودتون تست کنید):
https://github.com/hershalb/music-video-arena
هر 4 تا ویدئوش رو آپلود می‌کنم ببینید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4543" target="_blank">📅 20:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4542">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب گویا تیم Turso دارن روی نسخه جدیدی از PostgreSQL با زبان Rust کار می‌کنن و هدفشون اینه که چیزی شبیه به LLVM برای دیتابیس‌ها بسازن. این یه قدم جذاب برای امن‌تر و ماژولارتر کردن اکوسیستمش محسوب میشه در کل. منتها این بازنویسی همه‌چیز به Rust هم خودش موج/تب جالبیه
🤔
لینک کامل خبر:
https://turso.tech/blog/a-new-modern-version-of-postgres-in-rust</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4542" target="_blank">📅 09:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4541">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مافیا بخوابه، شهروندا بیدار شین همه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4541" target="_blank">📅 09:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4540">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سرعت آپلود به شدت ضعیف شده اینجا</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4540" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4539">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4539" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4538">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4538" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4537">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4537" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4532">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4532" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4531">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4531" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4523">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4523" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4523" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
