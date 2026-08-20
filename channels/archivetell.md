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
<img src="https://cdn4.telesco.pe/file/qWs6pjhsVJdijZsrv_rWX29v_ecs7GJixGnPvnN3YOcWG6tC5cc62XMRjGeYFDxldU8xt3J_8td49RQn_aJf0y60gwlkcO22vPRGDumOfq7Gtj54EuL9dnYPA9CKwOrewW_jM-XAPDL6ILZipM32LjshESbAk-jVWaqqsqVfqwP7i_rW3rmBs6DIoBCWiQUyUz6BqEUyy6d3nhzbRWOzrBS_VCvZeMFdH5fqAmGo_UEnCMocpXjo7ycfgKFLWbNWxBtXkc5exSj4smh9ypw_D_B_rUuaiy8FYcTV8ljh3jaYj3nyIx5nke1sDVT4QvgzXZouLa_le3lZZHnBd06akA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 18:32:12</div>
<hr>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 508 · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beS8Jho-zGrwN9u2mM0Pt0AcwA644XSQgac7FGlrV2VCwW5vFtWcxL5WV6fxRtGsFqY-fZk080iBAcJcuOvIlMCcnBE684piUhTU-lO2ypq3AZOg_5C0T1-dG2PWFOysmg70gFOJGWSiCyXQ4w1-fERhD3kfInbSDOQinEpcutcjZwvyDwIL9oo860ajGL5wKg334clXbocHDkdBIdi1QbGvMNSxYBkYip3fLbL6ghPhKazrGlWduzJE2zKs0ClZxM9tcEEeQ1HxDIBrenVM22XQYWvqUM5cCT5Jj3bjAbaWHYYW4YdMGpWYFiY03x6ECSLAHsHazcrcmEuGmP0Vxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8DKDpVkYm7rExBRnCM21RETRCuXK1v20eMucwMYQMDbs_3whHXYh7Bres-R4BzgXSMvGIB_M2gbIpv5faEw3XuRff5GA4n5Sa9EIeCtUek-IX_05ZaBvmYa5BZzwMRvf3sNttpYFYVTToRHruTfuJk_xmFBhj3BzGmQlS0yv_dj90blzBgsI4JbuvNWsIvkHjbeMs-FRHmauvHDFeZx6-j620Wr8NwlZhZFLugDksACNoZ6gT5kyRgOkmsVy9QxN4tMqO0byTR9XXyh1G1S_j9eokdUrDHTK6WpYoCCwf6svqqmqu5UrLnS8zb7CvhmYUCRv9xmR_jzvH2T-y5M-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTB1skdJN51Xl8ltZ9rtYXDbM03AeolaJNPgdAiWFWbP5bM2WS63aAc0WpiRZAEq6xmJi9k8wi3IiolPdiQLqsjXDFJ2OluYbnqDbQI8omX2i9CysvXz5D2kxh3FpAmj6Y-Te2L8riYVQtBF_6t9DYVHiuxiy5_h3_JkkoKgyeloT5juSjR3l06iTeMTSMgVw9gp_IXc4UtxL_4x-ZwjxjKgg4oFNUWdao9d8vPs8CxoU_u1dtwFqsWFZke0B2fmfs9a8qtX7-_8ArXyBRaGniYlb4dKO_9Fey_8pa1NWObYCgJ-K2F-cw4pDNTEOMbUAByH4GMgnRpoAe1GgOp0yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی
💥
🆓
Kimi K3 | Qwen 3.8 max |  Gemini 3.7 flash | Sonnet 5 | GPT 5.6 Terra | Deepseek V4 Pro 0813 | Deepseek V4 Flash 0713 | Gemini 3 pro image
✅
با این سایت میتونید به کلی مدل قدیمی و جدید دسترسی پیدا کنید این سایت هر روز به شما 100k کریدیت میده
✅
📌
Base URL:
https://api.anyapi.ai/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مدل قدرتمند
Qwen 3.8
با ۲۷ میلیارد پارامتر الان رایگان روی پلتفرم آزمایشی هتزنر در دسترسه
☑️
اگه اکانت
هتزنر
دارید، فقط
API
رو بردارید و به هر ابزاری که با
OpenAI
سازگاره وصل کنید دیگه لازم نیست پول بدید
🆓
مستندات کامل اینجاست
➡️
experiments.hetzner.com/docs/inference
اگه کسی بلده چطور راحت‌تر اکانت بسازه یا ترفندی داره، لطفاً اینجا بگه تا همه بتونن استفاده کنن
🤝
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X97W4BGbaaRLA4jYudP0Gc72JHBDeaVr5LOuysY3xaCgJzZ9FEA3PKxhG9Hg3Le4DzN_CkRVrU-E-u9NyzT6T-nMfkEieW4QAEsu2_Mw8D8PolqM4R1G6MteSk2I9xz5kYtFrsgMsrC01NW-xEQBELCUoBA-hjHzFOHIDRXfft0oxLWTz9pmQHUn27y1-zVNyyRJhvV_9O_XoahmnlDsW19lq0qAso4OAzVk3H0xHN-229Z1j7fg3IVtSgJ0t7NuCCOW_FN_wlp-8iRCLk0FP_O0kj4PIvs6bSAjw72Oy_Oi42bTwM-MJpvxFsytsywkhP-6axN5zTrU7sdpZHht7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVU8MnEV6cCn98d8NNJdP7qvCS4H4GXfZ6mTaME_MT71EXC_vyVggs_oeHjIFdh_cZkdExQmTNxlmkSajcsHUYQtc4A4XrbE6aPzXVDKUOlMBjzrbfQfvwPPjz2o-_lVzKifl9OiL6jKli32kRCi-bjK3QSQBw20CrMZAiVQ4d4mvgBrLvzH8Dny5K5X24Rr4MNxxynCmQKYOsaHK7Wb-5wl-tBK_BnSHaIkPDNxQCo6cVKPb9sEPi7PXhXRV50H4AkTrUQknwXq3yom7F3agVeXLq-BVgbMlUslWTRscvfrPSop5UcUHXWJRL-u1ymylcmMtwWlT9Ggoa_nab_zPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان مادام‌العمر
💥
🆓
با این سایت یک ساب دامنه روی دامنه‌ی
kdns.fr
رو به صورت دائمی و رایگان دریافت میکنید همچنين میتونید اون رو به کلودفلر اضافه کنید
✅
✨
مراحل دریافت:
1️⃣
وارد
این سایت
بشید و ثبت نام کنید
2️⃣
به بخش
My Domains
برید
3️⃣
روی Order a domain بزنید و دامنه خودتون رو بگیرید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=kGSwYUCQ-as97s0wHAjsUQgNGp6Sw25w7sVC96aWfUOMmLSJKQ3pvJ-sdn3ttsG3VeS_lVJrM9Xr5RJvqlHmDl-idifh68Fl2pKCz_YM3cM0MApbXOY8dY1GffBJKgyQFvGoZEpEAyMMGI2__zeAMq0-TGmfMCA36HAoVWZSlFnrRs7DzFL7DX0tAX5H1iAjVqgPYVUVOjJpZX6k4N4KEfurIY9E6ucbCspFFhJ69HDbIVo8OYNwp8W1wE1wvwZ27ai36UWwvIEl2rutksZqDLNvEOT01Zs-2jiMtzvp3eKHRg9xeRgJKxWG4wzdxucBjAm3I7t_dkNgq1dvBlRqnYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=kGSwYUCQ-as97s0wHAjsUQgNGp6Sw25w7sVC96aWfUOMmLSJKQ3pvJ-sdn3ttsG3VeS_lVJrM9Xr5RJvqlHmDl-idifh68Fl2pKCz_YM3cM0MApbXOY8dY1GffBJKgyQFvGoZEpEAyMMGI2__zeAMq0-TGmfMCA36HAoVWZSlFnrRs7DzFL7DX0tAX5H1iAjVqgPYVUVOjJpZX6k4N4KEfurIY9E6ucbCspFFhJ69HDbIVo8OYNwp8W1wE1wvwZ27ai36UWwvIEl2rutksZqDLNvEOT01Zs-2jiMtzvp3eKHRg9xeRgJKxWG4wzdxucBjAm3I7t_dkNgq1dvBlRqnYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
📱
وایب‌کدینگ حالا رو گوشیته!
ابزار HAPI اومده که به‌جای جایگزین کردن ایجنت‌های کدنویسی، همون‌هایی که روی سیستمت داری رو مستقیم از موبایل کنترل می‌کنی
🔥
سازگار با Claude Code، Codex، Cursor Agent، Grok Build، OpenCode و چندتای دیگه
✅
🎙
کنترل با دستور صوتی، بدون نیاز به تایپ
📂
دسترسی به ترمینال، چک فایل‌ها و اعمال تغییرات — همه از گوشی
💻
سشنی که روی کامپیوتر شروع کردی رو بدون قطعی و از صفر شروع کردن، رو موبایل ادامه بده
🔔
تایید هر درخواست هوش مصنوعی فقط با یه تپ، حتی وقتی پشت سیستم نیستی
🤖
حتی از تلگرام هم قابل کنترله
نکته‌ی جالب: HAPI کاملاً local-first و متن‌بازه (AGPL-3.0) — یعنی داده‌هات روی سیستم خودت می‌مونه و به سرور خارجی آپلود نمیشه.
✨
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الان سه تا مدل قوی رو می‌تونید کاملاً رایگان تست کنید
🆓
برید سایت زیر ثبت نام کنید و به راحتی از مدل های زیر استفاده کنید
✅
✔️
مدل‌ها:
•
z-ai/glm-5.3-free
• dots-studio/dots3-note-prev
• deepseek/deepseek-v4-flash-free
🧾
Link
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تلگرام برای دریافت پسوند دامنه .gram درخواست داده است
🉐
اگر این درخواست از سوی ICANN تأیید شود، بیش از یک میلیارد کاربر تلگرام می‌توانند دامنه سطح دوم اختصاصی خود را داشته باشند
💎
مثلاً
@durov
می‌تواند durov.gram و
@monk
می‌تواند monk.gram را ثبت کند
☑️
علاوه بر این، کاربران فقط با نوشتن یک
پرامپت ساده،
وب‌سایت‌های تعاملی خود را مستقیماً روی زیرساخت تلگرام راه‌اندازی خواهند کرد
🤯
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiEomFhTbIkR_-CQ6Uj2SWp4rJoPe0wCbW9HMh1KjvvfaTqMfA7EAVKpd6sWH6To8VMw6S0WdV1Pzhkes9j-JnfxIXuhkpWaW-rrQy2UkBKxH_6BKYtCPzoammQxVnJ77uDA9q5OV4xYOXVQQzk4E3PZP22BlpoNLElzTT_HHOjTygYwMjnaeAvFJdlGmU9VvKc_mIEJsUDEw1Cuk_E3wDCFkeZkJxGQNfsX_buVk4FKcHd7dyEkI8yPUrqFA-V5PaJnNlT6QmvoDg_ODAzWDgqxwNjA_ESCK9YAvK5YA6dODmF70Y9tfMOSWbdwl8N3alRbDYLnwwFvlcLBrR2unA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود کد ابزار قدرتمند طراحی گرفت
🎨
تیم Anthropic به عامل هوشمند خود قابلیت جدیدی برای طراحی رابط کاربری وب‌سایت‌ها و اپلیکیشن‌های موبایل داده است. کافی‌ست دستور /design را وارد کنید و تغییرات موردنظرتان را توضیح دهید.
🔥
سیستم به‌صورت خودکار کدبیس موجود را می‌خواند، خودش را با سبک طراحی فعلی تطبیق می‌دهد و پیش‌نویس‌های متعددی را در قالب طرح (artboard) تولید می‌کند که می‌توانید به‌صورت آرتیفکت به‌اشتراک بگذارید  (The Decoder) . کافی‌ست طرح موردعلاقه‌تان را انتخاب و ویرایش کنید، سپس آن را وارد فاز کدنویسی کنید.
✨
این ویژگی هم‌اکنون به‌صورت پیش‌نمایش اولیه در دسترس است  (The Decoder) ؛ برای امتحان کردنش کافی‌ست دستور claude update را اجرا کنید.
✅
🔗
لینک دیدن جزئیات
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تست کردن مدل‌های هوش مصنوعی
🚀
حتماً براتون این سوال پیش اومده که مدل هوش مصنوعی‌ای که از یک سایت دریافت می‌کنید، چقدر به مدل واقعی نزدیکه؟
🧐
آیا واقعاً همون مدلی رو که ادعا می‌شه دریافت می‌کنید، یا یک نسخه‌ی ضعیف‌تر و متفاوت؟
👀
✨
توی این پست، ۲ سایت معتبر رو بهتون معرفی می‌کنیم که باهاشون می‌تونید مدل رو تست کنید و خودتون نتیجه رو بسنجید
🔗
لینک سایت اول
🔗
لینک سایت دوم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ii1gS4qh9k4vNsizLM8b0hJuXh0sybXKldZi-zpdkSNmVuVc1OiRg3Zp7_ctL7bjfWTorF8Ov3hhxM6zr5woWmdAGLHYqyZRrnNbTYD14JxNVKfVCSFJfzA2Vf1J68tiKIbnIvSUwGYfDk7Trigg6ptk6KaUj8VZou4ipoH1MbZF_B2RsZ4XtIXC2EADOjAuwRJ8eyRz7-iz18Ruv3cps5-sRuO98PBMvLPumdOG0Hk-1oXN8HMIf9RC8284vEPSXt0md_2pOZ4Whmh_tnGeDYmtDkwQdEtTVmqiz2gS8iBOyTDFN6AQC6xCry0U2B8pctcA11uvtN0r_ypTwYRKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL :
https://api.b.ai/v1
📌
Model ID :
deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDtpsCrnWKUHdv7c36bVbzC1001HMYiRLLWgRiFSiukklrme7ppEdt249N7PMGpTHu2jRVkCP7jSq0yyH4ZqzcKY53aydcQTxXkZIEFWdBZRouYUrW-ai3HbaJp0pwwEXFxny8dTEHosXWk0TUpJtJixMgAuBQxwvYgEuY5lF1kjMI5e9DZM0go5kwDmcq8Nbl_5mUWzAo1W3AN4eBeWiQ_b92GeSO24QUnGbgthBYwLI-PdZtUosCCMswu7JEkgFWxdotJJUbprFAqaTbnDvS9GbY4wDjXupbGxiwt3a-mtMGoaEQfIKmHMCi5DZAdkEuJjjJK4wMUI7Jfmf_jK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.2 الان روی OpenRouter رایگانه
💥
🆓
هوش مصنوعی GLM 5.2 یک مدل Reasoning قدرتمند برای برنامه‌نویسی، AI Agent ها و اتوماسیون پیچیده‌ست. نسخه رایگانش در اینجا با 128k Context عرضه شده و از طریق مرورگر یا API سازگار با OpenAI در دسترسه.
✅
❗️
از مدل z-ai/glm-5.2:free استفاده کنید — بدون پسوند :free نسخه پولی اجرا می‌شه.
⚠️
محدودیت اکانت رایگان حدود ۵۰ درخواست در روزه
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-IXNxrDiaLV2vNxU73TC0Y4zSW1uPrXj0a24SxG8LbD4TYkfp
🔺
Base URL:
https://tabitoken.com/v1
🔺
Model ID: claude-opus-5
ری اکشن فراموش نشه
❤️
توی کامنتای پست چندتا کلید دیگه هم گذاشتم واستون
✅
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdd7J0Sq0LU9VYtU94bQGdgBnB_gQEbplr_kSFAQbXwWvHjwP7FZ4J44JUYUSiyVSBJnmp2KmIPdyOHuU3OFhwTG1372hT9l_ix0YX_gWyS-s6VJ0DwZhwY_Nt8m79wryBBsoYk1JeJhvTe2jbkAsrkCJq7WpBN5fnlQvC5FEhMbKXg3uWoncv1R3bvD5YRIJ-j_DmsnXhdWsQGR0rrkLTFKzH3LcSABjWx0DrCF8b_qjU5msO8yGPQuKiKc3CWmhUpQbHqm-IeVMtcR-8qQtTB5YdNWY1NMZoi1UJAmDFqdyPnLvg2mUZkq2_mfN9zB23CbZWCeBTA-OI9rJNLHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 و Qwen 3.8 max به صورت رایگان
💥
🆓
این دو مدل در این سایت به مدت محدود به صورت کاملا رایگان و فقط از طریق API در دسترس هستن
✅
📌
Base URL :
https://api.tokenrouter.com/v1
📌
Model ID :
deepseek/deepseek-v4-pro-0813-free
|
qwen/qwen3.8-max-free
⭕️
محدودیت ایی در میزان استفاده وجود نداره اما به دلیل شلوغی بسیار زیاد سایت مدل ها کند هستن،  پس باید در تایم خلوت استفاده کرد
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=qWwkvfxexk-XoHR1wVFM4kZUR4PU_v93G84ZY7Sjtaj3bVf0TB6Y4Iznficq2BNCZyjDezv9BDV4R9-fVXEKTkPxPOMoa0yXXEy-v4mXGzd0EaV_BvTBVsdyFzAL3qVKw-qJpskooLEhf7mZ7nusRz7_GeOPgw_xvS9_6yNoCni_mtcwMeM5g0x2Utxlq1-K2DrTbJUv45ijTZRq7gVD7CrEfThCDf3v7VnmyfBjUK9jH9P6VKDcPmWY0LK3tkbU_CiyA9ro-usJ9O1MypzBBVUkfWR0vCWJmpDWj5D11vRIDcTfTOBETEdNUF7R-eAx-uZ3X11Q1gMzXA4ItdYbuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=qWwkvfxexk-XoHR1wVFM4kZUR4PU_v93G84ZY7Sjtaj3bVf0TB6Y4Iznficq2BNCZyjDezv9BDV4R9-fVXEKTkPxPOMoa0yXXEy-v4mXGzd0EaV_BvTBVsdyFzAL3qVKw-qJpskooLEhf7mZ7nusRz7_GeOPgw_xvS9_6yNoCni_mtcwMeM5g0x2Utxlq1-K2DrTbJUv45ijTZRq7gVD7CrEfThCDf3v7VnmyfBjUK9jH9P6VKDcPmWY0LK3tkbU_CiyA9ro-usJ9O1MypzBBVUkfWR0vCWJmpDWj5D11vRIDcTfTOBETEdNUF7R-eAx-uZ3X11Q1gMzXA4ItdYbuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎧
این اپ کنترل موزیک رو مستقیم به تسک‌بار ویندوز میاره
ما FluentFlyout رو پیدا کردیم — اپلیکیشن رایگان و متن‌بازی که پنل کنترل موزیک رو دقیقاً روی Taskbar ویندوز ۱۱ نصب می‌کنه. کاور آلبوم، Play/Pause، Seek، تعویض ترک، Repeat و Shuffle، همه یک کلیک اونورترن.
🎶
با Spotify کامل کار می‌کنه
💻
با Windows Media Player کامل کار می‌کنه
🖥
با مرورگرهای Chromium و Firefox هم کار می‌کنه (بدون Shuffle/Repeat)
🎬
با VLC هم کار می‌کنه (ممکنه Plugin لازم داشته باشه)
⌨️
با هر پلیری که از SMTC ویندوز پشتیبانی کنه سازگاره
سبک، حدود ۵۰ تا ۲۰۰ مگابایت RAM مصرف می‌کنه و عملاً مصرف CPU نداره.
✅
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYnNEsRK-sJia-PnA9ciitftqUKjsNm8oUIM7Ek_AYMJSaQjSwaGria3PKl24yRyTwImscVXOtQ4lzNEsApfVo-eYnLZh0KIYvMVi7-y-Up1NMtJgVS6eNiXpmTTrnpzluIfo44mMkgUlRDd0O7-39civI2xiIEwj9Gb1LvnnpX2rXyhq9J4rqHjVVic52LYuE0YaqYHveNF_CFOvOG29Qv3nu39bSgbwX3OYydxNevbzUp3O13YEpD3pC48C7KVlFVwm1cIG1fPCol0OAeLuBcJMx8vH917pbKLo3IPCr1yO2BHgotVBWWmzkhmxcvh_SlDpX3xCCZbe21sPZjXMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
این ابزار خط‌فرمان، یوتیوب رو مستقیم توی ترمینال میاره
ما ytsurf رو پیدا کردیم — یک CLI رایگان و متن‌باز که ویدیوهای یوتیوب رو تمیز و بدون حواس‌پرتی مستقیم توی Terminal پخش می‌کنه.
✅
👥
قابلیت تماشای مشترک با Syncplay
🎶
پخش و دانلود فقط صدا (Audio-only)
📥
دانلود ویدیو یا صوت با یک دستور
📌
انتخاب تعاملی Format و Quality هنگام پخش یا دانلود
📃
تاریخچه پخش با امکان تماشای سریع مجدد
📂
تنظیم مسیر دلخواه برای دانلودها
🔄
بررسی خودکار آپدیت برای نصب‌های Manual
📺
پشتیبانی از Subscription کانال و Feed شخصی‌سازی‌شده
⚙️
نیاز به چند Dependency داره: yt-dlp، mpv، fzf، jq، curl، ffmpeg، chafa. روی Arch (AUR)، Homebrew و NixOS هم قابل نصبه.
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=t96UFFEt22CNdPRfj2asvEtR4TnYo_RHEoJjzsAwARyMWoCQLTw3aMHOzaOdqqu5AHF_aZiYiBpHZQI6YbNzHMfQIFwqP3szId89ZPAEk3yKMF8v42HaIE4O-tMWSVbEpVhCfsu_WDdPYcAVOhJBGO6jx1yKg_0WlLb23PERau3KJ4MeXxilRieHSSrSyGCj_8mflY8FvTh082W7ABcgyeQOLlzRC-CU6PG_A6T6QJ98yrZNGIvTeiLBVGD0ypDCpa0KdmHuiQB0Rw-tIggUwNZEZdE1jf5o_GGlFkgvGojDglrAGtQpyk5bn3ZkxsNmTyMnxgLy-O6krYDXGqlzTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=t96UFFEt22CNdPRfj2asvEtR4TnYo_RHEoJjzsAwARyMWoCQLTw3aMHOzaOdqqu5AHF_aZiYiBpHZQI6YbNzHMfQIFwqP3szId89ZPAEk3yKMF8v42HaIE4O-tMWSVbEpVhCfsu_WDdPYcAVOhJBGO6jx1yKg_0WlLb23PERau3KJ4MeXxilRieHSSrSyGCj_8mflY8FvTh082W7ABcgyeQOLlzRC-CU6PG_A6T6QJ98yrZNGIvTeiLBVGD0ypDCpa0KdmHuiQB0Rw-tIggUwNZEZdE1jf5o_GGlFkgvGojDglrAGtQpyk5bn3ZkxsNmTyMnxgLy-O6krYDXGqlzTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پرامپت هر ریپازیتوری رو به یک نقشه سه‌بعدی تعاملی تبدیل می‌کنه
🚀
بده به Claude تا یک شمای ایزومتریک از پروژ با Dependency ها، مسیر داده‌ها، و توضیحات کامل بگیری
💥
📐
معماری رو مثل یک شهر سه‌بعدی روی Grid می‌سازه
🏢
هر بخش از Infrastructure = یک ساختمان با شکل متفاوت
↔
مسیر Control و Data رو دقیق دنبال می‌کنه
📄
به فایل‌های واقعی Reference می‌ده
✍️
پرامپت:
Analyze [لینک ریپو] at latest main. Create an isometric system map with legend and explainer panel. Show infrastructure as varied 3D buildings on a grid, with dependencies and payloads tracing real control/data paths. Cite files.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyCaBHoQfUPrGvPTtmf25Yyef5ilf128XDW-YcJxLNC9fW50VTYjkY22v09a-dzV_lX-jD_MnxFgws_k8gBv0gnANDCJHnu1qwZIvsH6-wiG3fk4Yq8jQjV0xeXApgDHNHm--OjcvBSlGh0uzajvctFwOXsM_gddKPsQc_MyKooN2yyeIlwE2BeFwJRr9ewmYW-LXvooQEBZkYN6fx4BhWxqgwy57csm4QaKjTzGGp7PjtyGeGs4eOAQ20BgbGOB2DNrIv0ryZ6p5AXN3sjWdt6G1ko6nKPmuNF734zeS6QjwTDetoBBFWyVyPLOtoykgunupIhsvY6yYXV2z63mSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧹
این ابزار متن‌باز، ردپای AI رو از فایل‌های شما پاک می‌کنه
ما watermarks-remover رو پیدا کردیم — یک Agent Skill به‌همراه یک سرویس رایگان که Watermark و اطلاعات پنهان تولیدشده توسط مدل‌های AI رو از فایل‌های مختلف حذف می‌کنه.
✅
📄
ده‌ها فرمت رو پوشش می‌ده:
PNG، JPEG، SVG، PDF، DOCX، ODT، HTML، Markdown
🔡
کاراکترهای مخفی Unicode و ردپای متنی AI رو پاک می‌کنه
🖼
متادیتای C2PA/EXIF/XMP رو از فایل‌ها می‌زداید
⚙️
کاملاً متن‌باز و رایگان، با پشتیبانی از Claude، Gemini/SynthID، OpenAI و مدل‌های Open-Source
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0yRSrNXQykdwMWIZ2IL_QCg2wa2UPhguet8uFcBRGFwu0p1IgUq-iLEeYNvlyy_hqAOGoaTOd3PumZiAtPbM7N0JB9rN0-emcJpsTSJtVZ1v1dB9_dfzBcDfR9TBrn3ueWjYyRNjR-5hqU3y12YC7PHRZQRWfSmTWwNnX82lEuBhQ8CKnmsWCsYwYgiUsM95j3uKZGXO2jEw7JwcOhyY2IoPS5ak0Hq0HVL9Z2c2NN1shZIzJkeygpP_Y0e6amyHhQTruZ7AGaGIWg-9C0aH6CBVZnm_CZd8ZPToyfI0jk514E_HZtCRKSXBy1gCRgvtjl68Nm1lXhiLWKHZnYuiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Grok 4.6 | Kimi k3 | Qwen 3.8 Max | Deepseek V4 Flash | GPT image 2 | Seedance 2.5
✅
این سایت بهتون 5 دلار به مدت 7 روز میده تا بتونید از این مدل ها استفاده کنید
💵
یکی از بزرگترین فرق های این سایت اینه که مصرف مدل ها به شدت پایینه و کریدیت خیلی کمی رو کم میکنه
✅
📌
Base URL :
https://heyroute.ai/v1
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=lksM_Uiv52wFDEROjp2D8DR8BzQD79yAXOJTplCXQm1cJYVJHinRziqTyOsYWS2eBC-iWe2nQyo2lMIQMi3mz-RzyV4ikgHHZYsI9syFdLOcdKfT_-kabGUxl8EhgCm5HXZLvlXZsM-4u6uRHHw52WATsYEJtB28F2EaHjRqFu5fb5ELKwHXHyPZSMjLFr4gnlKZ776uDkN6rQwr34EBbPpIV4FoN32og7GP1pspTNgDXvM_5O5mrTr5age06NpY6RoTYfjMkoIHfNf_U3MBsY2_X-NzwGa3Pv66HR68FPrVcXBWNUSHJSYh5k6Pmco2y9Ecch2sy2OVgGEU2hLxwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=lksM_Uiv52wFDEROjp2D8DR8BzQD79yAXOJTplCXQm1cJYVJHinRziqTyOsYWS2eBC-iWe2nQyo2lMIQMi3mz-RzyV4ikgHHZYsI9syFdLOcdKfT_-kabGUxl8EhgCm5HXZLvlXZsM-4u6uRHHw52WATsYEJtB28F2EaHjRqFu5fb5ELKwHXHyPZSMjLFr4gnlKZ776uDkN6rQwr34EBbPpIV4FoN32og7GP1pspTNgDXvM_5O5mrTr5age06NpY6RoTYfjMkoIHfNf_U3MBsY2_X-NzwGa3Pv66HR68FPrVcXBWNUSHJSYh5k6Pmco2y9Ecch2sy2OVgGEU2hLxwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرامپت، کل معماری پروژه‌ت رو نقشه‌برداری می‌کنه
🚀
پرامپت رو بده به Claude، بذار کل Repository رو بخونه، دو تا خروجی حرفه‌ای تحویل بگیر:
⚡
کل کدبیس رو تحلیل می‌کنه
🔗
ارتباط بین فایل‌ها و کامپوننت‌ها رو کشف می‌کنه
🗺
معماری رو به‌صورت دیاگرام تعاملی می‌سازه
🧭
مسیر کامل هر Flow رو ترسیم می‌کنه
💬
برای هر Component یک Tooltip توضیحی می‌سازه
📤
خروجی:
🖥
فایل HTML مستقل
دیاگرام تعاملی با Node و Connection، پنل Flow کنار صفحه، کلیک روی هر Flow → Highlight مسیر کامل، طراحی تمیز و Responsive
🧬
فایل JSON برای AI Agent ها
ساختار: { nodes, edges, flows: [{ steps }] }
مخصوص Agent هایی که باید معماری پروژه رو بفهمن
✍️
پرامپت:
Analyze my entire code repository thoroughly.
Generate TWO ready-to-use deliverables:
1. A single self-contained HTML file containing:
• An interactive architecture diagram (nodes + connections)
• A flow panel on the right
• When a flow is clicked, highlight the complete path
• Tooltips for each component
• A clean, professional, and responsive design
2. A JSON with the structure:
"{nodes, edges, flows: [{steps}]}"
The JSON should be specifically designed for AI agents to understand and navigate the project architecture.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLkw4qQf9yR1eACjGXvzt0PlvlNGAS6Uc6wLbitIYWORpbnTKkKBGmNLnM-_VPOgc8AR3OvxwOLR0k_swu2KXpbML9-K1_OuHV7apPFo1VO7jvoN9G-xygwokAhlPwkeRB3gIhdQaiSOh1Dl3CtZFjHSXgqxRbWWkKFSOBPE-6Nq1LL92XskkkDgZql22fyhBoZietsDOih_G5UUAuja_xGPhbjJxUfgVUyl7Xj2RjPRUunRbqZiYQryE_X9A3veSGKSbe4K3i4TvpaPON5C8NvOmD_6aR1MrJp9eog7LvYV6pTx7pkC9Q0Glq4NcUy6Zl7D2ZICZpzzo6vuUn9Y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی رو به یک ایجنت هوش مصنوعی تبدیل کنید!
🚀
دیپ‌سیک با معرفی DeepSeek Harness یک محیط جدید برای ساخت و اجرای AI Agent ها راه‌اندازی کرده؛ پروژه‌ای که خیلی سریع مورد توجه جامعه اوپن‌سورس قرار گرفته.
🔥
💡
ایده اصلی Harness چیه؟
تقریباً هر چیزی می‌تونه به‌عنوان یک Plugin وارد سیستم بشه؛ از مدل‌های هوش مصنوعی و Sessionها گرفته تا Skillها، Sandboxها، چرخه‌های اجرای Agent و حتی رابط کاربری.
⚙️
معماری Harness بر پایه‌ی Cordis طراحی شده و این امکان رو می‌ده که کامپوننت‌های مختلف حتی در زمان اجرای Agent هم تغییر کنن.
💥
چیزی که Harness رو جذاب کرده اینه که محدود به یک مدل یا ساختار خاص نیست؛ می‌تونید اجزای مختلف رو با هم ترکیب کنید و Agent موردنیازتون رو بسازید.
🧩
حتی جامعه‌ی توسعه‌دهندگان هم دست به کار شده و هزاران Skill آماده برای Harness ساخته شده که می‌تونید ازشون استفاده کنید.
📌
خلاصه اینکه DeepSeek داره یک رویکرد متفاوت برای ساخت AI Agentهای ماژولار و قابل توسعه ارائه می‌ده؛ چیزی که می‌تونه برای دنیای کدنویسی و Agentها خیلی مهم باشه.
🔗
لینک گیتهاب پروژه
🔗
لینک سایت پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJw77du7TAbJoYFjQc7fhUO3sXFEdPaquU1lnNh8CFlgOys3SgqAhZR3fc4JSB5Kp7uQd6H1OBORF8S6wttS0LkO4tap05BgQKiYzaN3bgBvEnlQJ9NaksedAe75i5yekjb4I-z5XmlblFWmymv3eVOHi2RdzxegjRMkB4qcfOInBsJY2D3LYdPMohDZToEMAnTPh2xPcQNDprJbRrlWYVTHdQP9SDyWEfEqRw5Km_M3Vv8Kq7CkptDr4LHYq-Z2Zn2Jq8aCJ-Or_8Zsgu_x35RTFIHi3xs66O_uxGaaXgL68RPbFtypXrw6NkN5TKjxqslDi_QUOJFP_Fd7Rxk8Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست طلایی سرویس‌های رایگان برای برنامه‌نویس‌ها
🖥
سایت
free-for.dev
یه لیست
کامل و مرتب
از سرویس‌های
ابری
و
ابزارهایی‌ست
که پلن
رایگان
واقعی دارن (
نه فقط تریال چندروزه
)
🆓
از
دامنه
و
هاست رایگان
گرفته تا
دیتابیس
،
CI/CD
،
مانیتورینگ
،
ایمیل
،
ذخیره‌سازی
و
خیلی چیزای
دیگه
🔸
اگه دنبال
ابزار رایگان
برای
پروژه شخصی
یا
استارتاپت
می‌گردی، حتماً یه سر بهش بزن
💻
⭐️
Link
⭐️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=RJ-q079x5ySQviLDZePUFdnPHtHxsanp6HB9HkBsb4SXvs6sJXlJZ059twgCbi3OmUTY8oOzGq0wxxjKFYTS4VlhgmX5NgpphchVt70PxI9Mmv9cvZwqw__TYeYcDPdPxtvPNY5hoRJ6R7kPsaHIPiIOdqUeyCmjeV0BT3tFnfyV9HnbEb-ZK6We5ywc4lpGQKBYr1KiPezoLXOgT9AKOqwXJ1h6DZAlaQqdlgv9ACSCXSp82Cf3aM23QQyqOjlB5ikF6ouCmLPcUuhde3oEHmqZjcr8eIuT0GWZKbe8YhOzqJbiCL2kt6OhVnzG8uXovfM4lWMpv6fDvqS90Wdcow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=RJ-q079x5ySQviLDZePUFdnPHtHxsanp6HB9HkBsb4SXvs6sJXlJZ059twgCbi3OmUTY8oOzGq0wxxjKFYTS4VlhgmX5NgpphchVt70PxI9Mmv9cvZwqw__TYeYcDPdPxtvPNY5hoRJ6R7kPsaHIPiIOdqUeyCmjeV0BT3tFnfyV9HnbEb-ZK6We5ywc4lpGQKBYr1KiPezoLXOgT9AKOqwXJ1h6DZAlaQqdlgv9ACSCXSp82Cf3aM23QQyqOjlB5ikF6ouCmLPcUuhde3oEHmqZjcr8eIuT0GWZKbe8YhOzqJbiCL2kt6OhVnzG8uXovfM4lWMpv6fDvqS90Wdcow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📝
♊️
گوگل هر ریپازیتوری رو به مستندات تعاملی تبدیل می‌کنه
گوگل ابزار جدیدی به نام CodeWiki معرفی کرده که با بررسی خودکار کدبیس، در چند دقیقه یک مستندات کامل و قابل‌فهم از پروژه می‌سازه.
🚀
🔺
ساخت خودکار دیاگرام و نقشه پروژه
🔺
توضیح بخش‌های مختلف کد و نحوه عملکردشون
🔺
تولید راهنما و آموزش مرحله‌به‌مرحله
🔺
تحلیل معماری و ارتباط بین وابستگی‌ها
🔺
ساخت یک چت‌بات آشنا با کل ریپازیتوری برای پاسخ به سوالات مربوط به کد
یعنی به‌جای ساعت‌ها گشتن بین فایل‌ها و کدها، می‌تونی پروژه رو خیلی سریع‌تر درک کنی.
👀
📌
این ابزار رو از دست نده!
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjzoQDyWQ3hkCUDVCUkqXjQ4VW3WU_OuHAkpnR57RM5nI93uTJzGJ5Os7qe9KlnOTFdhEWOsVnGQHyHHwIxm1RH8407TOfOZTj4PKmp4C20dJi5tGetw2wu-Wls3qjrA6EtwhBRBsxY83s3Dzm6ws6H9GfspC4W5Mj5rO7zxqYSvefa2sDObU81yGi6KU43sqZIRTRXyGgi0wC-f_FdtCcuIdVXOaU4f-9bvCJOL71-ywXdZIJHdjqoSDgY0MRyus9cyeRPqS1xRYMYLLWsJMqDljtYhvwYe4VsUnERvnG19kF1jfwONzrrWaJM3GAne3FPP0RdWOjSlv7sCahzb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TorrentSearch
♻️
اپلیکیشن متن‌باز اندروید برای جستجوی همزمان تورنت از چندین منبع
📱
با
TorrentSearch
می‌تونی
خیلی سریع
از کلی
سایت
و
پرووایدر
مختلف جستجو کنی، نتایج رو فیلتر و مرتب کنی و مستقیم مگنت لینک یا فایل تورنت رو بگیری
⏬
امکانات اصلی
💭
جستجوی همزمان از چندین
پرووایدر
(قابل روشن/خاموش کردن جداگانه)
🎁
فیلتر بر اساس
دسته‌بندی
(فیلم، سریال، انیمه، بازی، کتاب و ...)
📁
نمایش تدریجی
نتایج
+
مرتب‌سازی
بر اساس سیدر، سایز، تاریخ و ...
🪣
جزئیات کامل هر
تورنت
+ صفحه جزئیات داخل خود
اپ
ℹ️
ذخیره
بوک‌مارک
+ خروجی/ورودی گرفتن
🔖
حالت
Safe Mode
برای مخفی کردن محتوای
NSFW
🔞
پشتیبانی از
Jackett
/
Prowlarr
(
Torznab
)
🦾
طراحی مدرن
Material 3
و
دارک مود
🎨
⬇️
دانلود از گیت‌هاب یا F-Droid / IzzyOnDroid
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚡
پرامپت‌نویسی تغییر کرده؛ این ترفندهای قدیمی رو دور بریزید
بزرگ‌ترین دلیل جواب‌های پرت و توهمات هوش مصنوعی فقط یک چیزه:
وقتی جزئیات بهش ندید، جاهای خالی رو با حدس و گمان پر می‌کنه.
❌
ترفندهایی که دیگه منسوخ شدن:
•
نقش‌دادن‌های کلیشه‌ای:
نوشتن جملاتی مثل «تو یک متخصص ارشد با ۲۰ سال سابقه‌ای...» تاثیری در دقت نداره. مدل به فکت و داده نیاز داره، نه عنوان شغلی تخیلی.
•
تکیه به
Temperature = 0
:
صفر کردن دما جلوی اشتباه رو نمی‌گیره؛ فقط باعث می‌شه مدل خطایش رو با لحنی کاملاً جدی و بدون تغییر تکرار کنه.
•
پرامپت‌های ۳ صفحه‌ای برای تسک‌های عادی:
طومار نوشتن برای کارهای ساده، تمرکز مدل رو به‌هم می‌ریزه و احتمال نادیده گرفتن دستور اصلی رو بالا می‌بره.
✅
فرمول ۴ مرحله‌ای برای گرفتن بهترین خروجی:
۱. هدف دقیق (نه کلی‌گویی)
❌
نگو:
«این قرارداد رو بررسی کن.»
✅
بگو:
«این پیش‌نویس رو بخون و فقط بندهایی که بار مالی اضافه برای خریدار ایجاد می‌کنن رو پیدا کن.»
۲. بافتار و مخاطب (Context)
«مخاطب فردی بدون دانش حقوقیه؛ توضیحات رو کاملاً روان، ساده و بدون اصطلاحات پیچیده بنویس.»
۳. بستن راه حدس و توهم (خیلی مهم)
«اگر پاسخ یا عددی توی متن نیست، به هیچ وجه حدس نزن و صراحتاً بنویس: "اطلاعات در متن موجود نیست".»
۴. قالب مشخص برای خروجی
«پاسخ نهایی رو فقط در قالب یک جدول ۳ ستونه بده: [شماره بند | ریسک موجود | متن پیشنهادی جایگزین].»
💡
اصل ماجرا:
هوش مصنوعی ذهن‌خوان نیست. هرچقدر دامنه حدس‌زدن مدل رو محدودتر کنید، خروجی دقیق‌تر و کاربردی‌تری تحویل می‌گیرید.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA7st2WQe7DCOAtZ9tEtmoIuDAzpD0DPaStEp7Zj6JP62Cv35bK7EPuRRXOyAv8RFYMfYpk_0CSJTly_ML8QRMtE1uon4w9LuZaVs5eN_dnx--sDnmMc6ZeRnpXbli1LFPQzwYjX-dUHaJXGo9a2lnlw-hB6ycLi3OoDeVKMD3ZFywhOE1sfkcH3_oUCzoDzwPHTRCDg49EdXTCgFP0NOsYRIv76ZT1n-FMjMPRgB7xQPR4lJX8Bi4U-njgzzgUlh9CIdZkmBxLQlaLTmPhMpyf-9uR2PJE1iNnxxoBu5fQC-Y7iEaI4vGLDFnPzB6tLJ8bL0x2S2E3ouMh7PmlhLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی به صورت کاملا رایگان
💥
🆓
Sonnet 5 | GPT 5.6 Terra | Agnes 2.5 | Mimo 2.5 | Gpt image 2 | Nano banana 2
✅
📌
Base URL :
https://ai.furry.vg/v1
حتما در بخش انتخاب گروه ، گروه Free رو انتخاب کنید
‼️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCJHD8gkbZbrVjhJ6BbKnl6vmX2nMqiaek4PBsiY-cwvXWDr_9xqtschL-IGBrxIgslih7U3on8ETIWX2Tj3Ur8FTJk4NMOFN7aqZBgwA0WiL0wsCvmY1wH1Fj1UY2RqTp_60p98xW-QSGJcqMIFHNF1yNXYlKFL8Y4N_DmDMs1NvhP0XXeER5fLWm2x1Fjuf3bNpdT_YWCX-ZukQYONAOsB4wDkTMqPzu97ueINrJrt5xfeIzBpHprH6KUtWnT9lZSIS08agNj3l1CtPqCZMtweFU4kKrQIBr56ktVy7MDRfPEIBiCnKU4JnHh1bJEsHu3vzeUsjc21DlQBhfAcAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل Qwen 3.8
💥
🆓
با سایت Runinfra تا 48 ساعت آینده میتونید به API مدل Qwen 3.8 دسترسی رایگان داشته باشید
✅
📌
Base URL :
https://api.runinfra.ai/v1
📌
Model ID :
qwen3-8-27b
به دلیل شلوغی سایت ممکن است پاسخ مدل کند باشد
‼️
🔗
لینک دریافت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIZ4EtiA8A5PlJsuBGuRVwMdDZqjQOiUp05LC3w6huMo6dyHMWsBA9t_wxGPwbFw74Ihj9q4PcIvhtlTO6F8jQENW5vypRD8UtP27UVqMBQqEvdC9Nn3IA_8y6sCzk6k5GmbP2GgWgsCwKWCuU7D_t_GZF7R6Y6pGImmhjno1qb5nji0y8UYjt4ei54q5SYtkFiTqWJfuxfvNSZTwAHVErCMahiJFx0wNyy50ReOiqUywMvLt4KJYO98LWnYE0heN3ho904H9iNyNA0RylZowTB5RPiL3uylC8cBdhTQiGj1lVsCowb82RRQ4CwWFsXmrrv1gt5sR0H8peAuRNGZiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی محبوب
💥
🆓
Qwen 3.8 max | Deepseek V4 Flash | Deepseek V4 Pro
✅
📌
Base URL :
https://api.orcarouter.ai/v1
🔗
لینک ثبت نام
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2257GYj_IwJOS51p94dNhBRmDFdIArLQ_UvLN0g2U_nrv48TNwXQAXUOh31DwGpCq-jqzhDoQbHsbm4PW9nNELpCpVBMQGHC7lfKoV8EKYH-y4wYsQiRVYfIsxIeKc69aJ7M9pa3CdG5sAuuuDD_Qz9ja7YnGAYctITSUtHaxi4_f1VV4gpDpj0FNfDpuVtWVyzaG9L62TDLiyl9sZ_C3Jr_7kesiVmEuc63eSLmABsS4xp42mKbqw9kdjSMcr5CgiV0pFAF_shxlLVtdS7DO1AJ67RzOOEF56rJT7h3N5CxceSTuKQRuWm-lcPQ-GPPyo0xbzjLnMCzJkO1IZ14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت
z.ai
بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
100 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-bY9B0parF18s5v1wasRyzRZsVLzICaSVfZNVEMrqG2Rlt7dH
🔺
Base URL:
https://ai.venlacy.com/v1
🔺
Model ID:
glm-5.2
به دلیل شلوغی ممکن است پاسخ ها کمی کند باشه
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmrXIn6ti_4qYLdLJizK0XJMVFf4Hf3otbvJqzivjbxD8f2ZgAwcIzRmFV456RXVqk1T41LhmS3i-Y4Hq7OOwRK4OtSMyoXnLNXtKCgxgqm2iUKCVUp3QNDgOkMxQmvcx8jENg1zJ1cVZCS_mAroCaO_srug4XXi00ziprUlCnboUeqMdhwAPyQyug0m6wrqYSKj0fXQ4bnpAHXK6HpBzID7lAbVzOAld3oYJsGUGzARxZeZLrBlUlysGIcgSS2auE_n93MplnE1ctOUkD-yayOGYpo3pJgZ0j0cN5WGde1ToRJ70mOLLjx4n3vIuIB9mT5ajqsAa3WU-tHt7DWruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 رونمایی شد
🚀
نسخه جدید GLM با نتایج بسیار قدرتمند در بنچمارک‌ها عرضه شده و در چندین بخش از رقبا جلو زده است.
🔥
در مقایسه با مدل‌هایی مثل Kimi K3، DeepSeek V4 Pro، Qwen 3.8 Max، Opus 4.8 و GPT-5.6 Sol، GLM-5.3 در بخش‌های زیادی عملکرد بسیار رقابتی و حتی برتری دارد.
⚡️
🔗
دیدن اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BG6bPxBFsRTiCeakwJZtza5D3QtloyoLEdz-KdIHZE-SI-XNMJ5DAcJDlsHTIVmRKCIkpMe5lDoyBJLsMIYx7WYjCKhaZSw8bSaLwmEgPUoylrPMgcXzPfDSYRu_eNPZ5SjyaAq8jCD5Cgau-4xRImWmG7F6c7qrD2PC9nQ38IVxXPPo2fXEOkSEYvGvawvzp7ciu_7fVDHUadx1NQSQKsEp_uj-G3IAipAH3OChCxVgnGF372Xk7fLzC1LKNr0nN1kJEbAtwoVDiF_AcrIJ5ZdK0VAvyMngnXNUG55bpcFzok46DtVuHpNqrxZn7Xqno9p80QW6IhCG0T4lnH66JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmx7iHhkCik-ZiLO0lvwRQ6nfYAJfPMIfD_lP2wnDLnvwWixjuXZLhDnViMsCb81Hh5bZHFTxmUZA9ZjD7yXqyWXbTWT939IdMOROnHN5J_NCaS4j0lk4KkHa6fYnALaotLqjBwWhVsISaOd8qoR2yTA83n8TAWMZjPtf1NhkM2hTVrTdOYZyiA3_Y2rC8AFeHcdpmfkSGLnkKwKoX6oXIAXeQaLaqRiSGayUr2sM72nYQhgCkWPclioMGbvri3YKyXj3lVTL3k41iRfNKSszsp-RCgNPLbqLUWINisvVxoPAWmyNVkst_ALcjXxnf9WTOnRboQbAZjVDUk1x21-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ تست رایگان مدل ‌Seedance 2.5
⁩
💥
🆓
‏اگر دوست داری ویدیوهای سینماییِ ۱۰ ثانیه‌ای با کیفیت ‌480p⁩ بسازی، پلتفرم ‌JXP⁩ این امکان رو به صورت یک‌بار مصرف برای هر حساب کاربری گذاشته.
🎬
✨
‏مراحل ساخت:
‏‌
1️⃣
وارد سایت
jxp.com
شو و ثبت‌نام کن.
‏‌
2️⃣
به این
بخش
برو
.
‏‌
3️⃣
متن یا تصویر دلخواهت رو وارد کن.
‏‌
4️⃣
دکمهٔ Generate Video رو بزن.
‏برای این تست اصلاً نیازی به کارت بانکی نداری و کاملاً رایگانه.
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پرامپت تولید شعر بی نقص پارسی!
از پرامپت زیر استفاده کنین تا ai براتون شعر هایی در حد شعر های حافظ و سعدی بسرایه:
تو یک استاد مسلّم عروض و ادبیات فارسی هستی. در سرودن شعر، اولویت مطلق با صحتِ
دقیق وزن عروضی است. پیش از نوشتن هر بیت، آن را در ذهن تقطیع کن تا مطمئن شوی
واژه‌ها (حتی کلمات غیرفارسی) دقیقاً و ریاضی‌وار در جایگاه درستِ وزنی
نشسته‌اند. خروجی نهایی نباید حتی یک مورد سکته، لکنت یا ایراد وزنی داشته باشد و
باید کاملاً روان و موسیقایی باشد. حالا یک شعر شاهکار کوتاه و روان درباره مناظره یک قناری و دایناسور بنویس
.
﻿
تست کنین، به همراه مدل ai استفاده شده شعرهاتونو کامنت کنین، بهترین شعرو که لایک بیشتری بگیره بش جایزه میدیم
🎉
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEPN8m-Bbh6ScuSE7xEZD2snFBSv2o_rvxmw3pfCSpu5J4Kil-HMoleRd3DTEFbsLO90o8cyQFX4BMdqVbBb952bpETiQsRepIz6SI_xuYutiTt1mEmDrc2pAeTv6ovNlvlcbc9-nUx1RpOSSGE6bchVrjwW-NQNS0xJIpw1nHWJjT7eAEJ1OzJovPk2JJRLT_LHHD6EttCohoDatEqncvrAkAlEAaz83RDOiiJJCrROyO8HbfpJ3emnRVH1qGlKkIaoYYa5t27oaf6ujQ28LapORv7lx1y2_PM4Zc8ifZWT_ZBeG33I8HQaDJxJ29GgLlte6QkMu-OvLSZVM1iQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
CiteSeerX گنج رایگان مقاله‌ها
یک موتور جست‌وجوی تخصصی برای مقالات کامپیوتر و علوم اطلاعات که فقط به جست‌وجو محدود نمی‌شه.
👀
🔺
میلیون‌ها مقاله + جست‌وجوی متن کامل
🔺
پیدا کردن منابع و مقالات مرتبط از طریق شبکه استنادها
🔺
اطلاعات نویسندگان و تحلیل تأثیرگذاری
🔺
کاملاً رایگان، بدون ثبت‌نام و با دانلود مستقیم PDF
🎯
برای پیدا کردن سریع منابع علمی خیلی کاربردیه.
🔗
ورود به CiteSeerX
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">20 دلار برای دسترسی به مدل‌های هوش مصنوعی GPT مانند
:
💥
🆓
GPT 5.6 Sol | GPT 5.6 Luna | GPT image 2
✅
وارد سایت شده و ثبت نام کنید سپس یک کادر میاد برای جوین شدن در چنل و غیره ، کافیه فقط روی دکمه ها کلیک کنید و پس از ورود به صفحه بک بزنید صفحه قبل ، سپس روی Claim کلیک کن
✅
Base url:
https://apimaster.ai/v1
قابل استفاده در
Vega Agent
✅
🔗
لینک ثبت‌نام در سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlSaKsyg54Z2MquhvkWOTBrHzbukqcmEOqW8p6lx_XTf4w-o5MWjfKqnZlHl5jWpE2pK9SqLKb3DhClcvnmbrAqcaC5dfiGniJk_ofDlvnPZqlzscSFbgIllBUXdxqjGWEl_cJQA3E9enDm4ae6NZKgK5BOKaZmua_JmOgkWiAmuSzgs1UlxmB6MHSL8hinHrbLYr-vep3W1FEVo6GEACKLDKt9Dxtxbk3wTf4C5-hBPz-oYAMsbKpFLCuszIupAEtkB2BHPG_j8oMOiyy_I9jWgulIYPc1r3_WPIme3KycxinsSL5d6FVpi4k5MhBTWxUj0RwGf1UToQgANnSjSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 وارد رقابت شد
💥
مدل جدید DeepSeek با قدرتی در سطح Kimi K3، GLM 5.2، GPT 5.6 Sol و Fable 5 معرفی شد.
🚀
🔺
سه سطح Thinking: کم، زیاد و حداکثری
🔺
عملکرد بهتر در تحلیل و برنامه‌نویسی
🔺
اجرای خودکار وظایف و ساخت گزارش
🔺
پشتیبانی Native از OpenAI Responses API
🔺
اتصال یک‌کلیکی به Codex
🔗
تستش کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRWHU8zXlWQcOtGZVVk15jxfdFm90WzXkP5pEBkRfrmrFq35x511O_xUkwn8Bnx280NmS87VoYa0Q1ypTJQjB-EHVjivSa9kNzqa4VippSvOJaklkbpE5tljq7huqYdrxr3Pxu2tnVWVMjaFHSRop9c3I5O9E9j_UTTzFXeQY9sSwMeUzU8xLq9_fcTOlvodcqQ0cqkBRKPX04EIsdj33v04eUmNay47egOsvyy6kG9I1tPXY60OecdZOTYbVspWxlhcrDKQnb9gafeDcobYRIIdzNpVXr07gYAQhuMZTqizWhwCql1aryOd496AWIJtmXWtAVvN7S94ZkRHUlQQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش مصنوعی محبوب
💥
🆓
با این سایت
روزانه
300 کریدیت رایگان دریافت کنید و از مدل های هوش منصوعی زیر برای کدنویسی بهرمند بشید
✅
Sonnet 5 | GPT 5.6 Terra | GPT 5.6 Luna |Gemini 3.6 flash | Gemini 3.1 pro | Haiku 4.5
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPGlRXorzPaagKXWxCmDIwm3UxrkvMWtbxE9Z7EtcUwxvMdCWCS2Nrntd89CyysgFmalT1r6Hypf-SevjZhYNyj3BLQUJPXPZzzQ-Fa6i8KxKzIeOlb3iHuC5L-VzJhCweeabLu8GsAja7hAiswUE-XGeLxuNNtG0P4ovZI9nlttTHStZ2FPiLkX3GCrlun1xbil95dbksMmznWY07_TOnIYMAw5g6D-hrrqPJNvAzi-ffj1LA5y6p8l4pkJn6rO1oGzJ6ZW6nW83uT7oDeoplHVuEQvmh0I1OzoGTi3tPMTtzHhIeIvHrCkqUx5nqteryVxKk3gKhPxIduhD9zWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کریپتو‌مارک مخفی Claude حذف شد!
🥸
هوش مصنوعی Claude روی متن‌های تولیدی خودش یک نشان نامرئی می‌ذاره؛ چیزی که با چشم دیده نمی‌شه، اما در الگوی انتخاب کلمات پنهانه و می‌تونه برای تشخیص متن Claude استفاده بشه.
🧑‍💻
حالا چند کدنویس ابزاری ساختن که این الگوهای مخفی رو در متن تغییر می‌ده.
📥
فقط متن رو وارد می‌کنی و نسخه‌ی جدیدش رو تحویل می‌گیری.
🔗
استفاده از ابزار
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpfDnJhJURhOhHqji7FdonUfzqgkygcfr_hP9IDMNT1m4XcVehqDLZLnmkiGI1HLYYvWHeP7y74xZcU9Bp8JXRWIs9Uzfy8LTbDHAaFMjuLIFfSTsDZlIBgCKh-nxmyRUpEcc-LPG50OtNCg0p3G2cojCuXjptQ0Wwfdw1zWL_QT2fSsGiBTKaV8GuwWz684AII7hYjrJTIPfTX_uXBvUgTfjkZSCmqFEVJXOECQT3LnpyAFBqaZ5MoeTNJpYqxXZ_iCx6MD0uetz17GhuSFar8QHneAMMEoNVopN2Ke9OWq2671a4oy9djCyE7LdG3XlolQeLSn37lH_H17J1EPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/girZFZCrx1kopK3Xs7OYY-VwlcK4m_jCItMRugMLtzgUFbUo6dKrsn5RZ6_ZIFRfzJdGpIo8AW1MV3O-LBsRkiMF58SoUwGq5XLKrGErZz0AM55uO7dB7uMQ0v_39pECWuM8HI5XtfLMaI4Pa0JKDEm5dmdF4N4vqFe2-bIKUWZPIQRSKBvhToRTiL6GTUP0tmQ89B4_y24P_USS4mB0rWb8LVn3KZOux-ZB2z92dgGORNUpD1TZ-5XCy2QcYcVS87nIhHIVaQurqQlr3aPEIAJJ1VM_qjTAxdNMVwxdDpaJD-46khZ9rJU4byxzc1P61AfZcfnJgKcVCgWUGGpetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد
قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود
۱.۵ تریلیون پارامتر
داره و قراره در آموزش
SFT و RL
پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:
چند هفته بعد،
Grok 4.7
با حدود
۲.۱ تریلیون پارامتر
میاد؛ قوی‌تر و بهینه‌تر، ولی کمی کندتر.
✨
👀
باید دید xAI این بار چه چیزی رو رو می‌کنه!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎙
LivDub | ترجمه و دوبله زنده با هوش مصنوعی
با
LivDub
می‌تونی ویدیوهای خارجی رو
هم‌زمان ترجمه و دوبله
کنی؛ بدون اینکه مدام به زیرنویس نگاه کنی
🤯
✨
قابلیت‌ها:
🔺
ترجمه و دوبله لحظه‌ای ویدیوها
🔺
استفاده از
Gemini Live
برای ترجمه صوتی
🔺
پشتیبانی از
۷۸+ زبان
🔺
مناسب یوتیوب، دوره‌ها، مصاحبه و لایو
🔺
پشتیبانی از مرورگرهای Chromium روی اندروید
⚙️
روش استفاده:
مرورگر سازگار رو نصب کن → افزونه LivDub رو نصب کن → Gemini API Key رو وارد کن → ویدیوی خارجی رو پخش کن
🎧
🖥
مرورگرهای پیشنهادی اندروید:
Cromite • Helium • Ultimatum • Quetta • Yandex
🔗
افزونه کروم
🔗
سایت LivDub
🔗
گرفتن کلید جمنای
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpcq_lVlfLAxg-uL9mhrANA4G5vv-ovH4VaYOvbeO_2jOe1LUBiqIsL_rpHWiNdLzDDNe-amX2HnoGRqFgxXwTXk9Bt9g8STBVkgKVXoj-u6gUcUc3ZvDGeWNExP5QwCBd9227zzRxl2WfOwehGjPMzfDRGAeWHnOl88eowBNKq1qxbEjoEbSJ8wS9T937CwB4VYOh8z0O1Gde2SUcFUqYqBUNdSREn4dL92jeIfCxoZP8kFuon9bDW5vlRYSYY_y8H_OyI-1NY1IOWD5eT9UqP_s7oFCR96wG9lx8rInHTef4xHMxqkGwx91Dq53qJsyvjgLW4CrTuh33keb2R5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
FLUX 3 Video رایگان شد
؛Black Forest Labs برای مدت محدود، FLUX 3 Video رو توی Playground خودش رایگان کرده
🔥
⏰
فرصت استفاده رایگان تا دوشنبه ۱۷ آگوست، ساعت 10:30 به وقت تهران
قراره در ادامه قابلیت‌هایی مثل 4K، ادیت ویدیو و استفاده از تصویر/ویدیو به‌عنوان رفرنس هم اضافه بشه.
⚡️
✨
🔗
لینک استفاده
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آیپی تمیز
✨
188.212.97.3
94.182.177.92
185.50.39.15
103.25.85.84
176.120.17.44
45.146.240.17
45.146.240.70
77.237.246.20
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEhQs9Z_NJPAvKpRzwVgEWd9ScfqMpCFN_jjAr5fZOGljw_glpvyqWjJngbRLRw91J3-XJT8bboEOtSsrjrorv_ZaiNIQ5JhiEDh9B6KMo2RsezOUAZT7vqlH7JRKLcT3Ri_jN0U9scfQdg5hc3J-e8mJ_61cFD-yeCIIEoM99-phkCwn43GyuVQRVeQVr5pUzNckScnJMWSbXfak68ZAr55D_oHer7ZEnkRBd8Vk51nJ4CtImvgAmw3cV3ESJGnHJC-KB9_rw8ZYgn85UI9fafYAKOIOC_U0ks6H-Tl4iPY86vsYOmpQK97zZqn-BZW5ceepqg1qhSql2kbsOVu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از 1000 پرامپت کاربردی برای هوش مصنوعی!
🚀
یه سایت که مجموعه‌ای از بهترین پرامپت‌ها رو یکجا جمع کرده؛ از درس و برنامه‌نویسی گرفته تا طراحی و Excel
⚡️
✨
یه جور جعبه‌ابزار کامل برای کار با هوش مصنوعی
🧰
🔥
🔗
لینک سایت
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJCSXhySsR5MI1QW8y3kdWXRBKmO2N8kA-MGTx3xhuDDciE_ZsrIWkaHp68_kisLBCDUohBNi5bDSPfPcdBxHZE-aiwAes3iuLmg0PGuH0D7qI5_GYlA09ESZgaV1cN5h3_2v4MiwmCUcCbF33g76-fol9-s3wBQ8SK4AKEl7MCmI764Ul5etRgI5FhS6ZpbeGqbtODxf5A2kEcfqP2UDg6VKKyqu1YaowqUnG85GCzK2rkxjd_iR-N3ESqOvHFAAOYUH6cHREugr8ZYj8p-W0LeJH6p3pDmf9S1z-DPnd-rxHrFK9gxZjtpBJzLRDM9axytJUawNkW_mgI5P6tloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤔
گوگل قید Gemini 3.5 Pro رو زد؟
گزارش‌ها می‌گن گوگل عرضه‌ی
Gemini 3.5 Pro
رو متوقف کرده تا مستقیماً روی
Gemini 4.0
تمرکز کنه.
🚀
گفته می‌شه مشکلات عملکردی و سخت‌گیری‌های امنیتی در مرحله‌ی تست، دلیل این تصمیم بوده.
🛡
حالا رقابت جدی‌تر می‌شه؛
Gemini 4.0
می‌تونه از ChatGPT و Claude جلو بزنه؟
🤔
🔥
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ4kxfVT2xpofe3DBCGye6EX_wGPYfWWqlq17cpdE9EnFd46DTygLkHfPwOWfjqKrj8-wPopKJS3pj36T-Bj2_OEqV-aQFQ0xk-kDtoP7yf9nFqofNOnCt0U8yFqc1fI9dNHXSr5K6XVSMV6E9P0Ys0YfpeEiTVV77THxe23odGAg25EEPPBHkyCz_uCWvDrcNXk49tYcduXy-pKRnjKP3GqZqYwcrb-YYEt-Wip-x81qPjaDSdEg_rPZEoJY_zyW28MSkE5CEnzkXLjIP-wzWwgLj11HsFV56f6rT4e7XJ_TSB3hkQo3ys6ef020WcqfFdZ4h_hcRJbIItXU7vKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
✨
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✔
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
40 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oag8Di6Eg3o3bn34RIw4GjUTyL2wlyhKRkQ_Xp_RW6GKPNLLTOMwgetW5EMJhinL4s8JXJBLuwmCmW2d-mrUENS00acwtOzZoHKBg4GSgO419Nfxzsbht2R1bspa4pq3qi5n9Cd3sAESBsuvQT8O3NYNelSrJAKIDaDXoRuMlbSW55nfJ1midaNfyhuewLhneYylfOtRkt1Z6lfuaX9yi2nyUPdY7cKN5jC4ZNtU34q9mCRF94mQ_RoI6WRR5caZuMPmzS6uVe8RjTZbpXyNDB8wRTXK_N_XN06cN0gAMHP_L-kKjkYpmQQfrfmInf_0IWm-rXw2BmdmPONbXhDx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع بزرگ یافتن سایت های API رایگان
💥
🆓
💵
با پوینت های این سایت میتونید کلید های API خریداری کنید و یا کلید API خودتون رو به فروش بزارید ، همچنین میتونید Redeem Code برای انواع سایت ها خریداری کنید و کریدیت دریافت کنید
🔍
همچنین این سایت منبع بزرگی برای یافتن سایت های API رایگان هست
🎁
موقع ورود مقداری پوینت دریافت میکنید همچنين هر روز میتونید از بخش Daily check-in ده تا پوینت دریافت کنید
⚠️
🚨
نکته:
حتما با فیلترشکن وارد شید
🔗
لینک ثبت نام
🔗
بخش خرید و فروش کلید
🔗
بخش خرید Redeem Code
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITwoAoaQAct8_LCzZWOoKHPB_zsGXAWfRzSCtCIjZ7Ta0OvV8ArGOQEoQhmTZz5yS8QKdkdjlVz_MIiaN-lQ2bpN7c9r8idB8GtsHCWqMnlm8XlQmob1mh-tO9CaRpeoTE31ASeHDYysVObMIQkFauLXcGmawlw3ICfSW8QrCTgtXryoa4ryDIbZkbXT5aulX_b7hgUfEsbxJVu5wPGEJp6vIpd3J1mx1NNCh5hRPiigLs21GsUnexSwlYkSHjlPMWsq1I0JsfZPaCSf1uBAHJxtcJofrBRtcot_oc6BhPT1DxSFDSbxm87rMdW3DqpdW9PwdOnzbW6-iRkr875JVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش منصوعی قدرتمند
🚀
🆓
Opus 4.8 | GPT 5.6 sol
✅
وارد
این سایت
بشید و ثبت نام کنید
سپس به
این بخش
برید روی Upgrade کلیک کنید و پلن Enterprise رو انتخاب کنید و روی Start Trial بزنید تمام حالا به
این بخش
برید و در صفحه چت یه چیزی بنویسید و Let's Go رو بزنید
✅
پیشنهاد میشه که اپیکیشن Postman IDE رو دانلود کنید
‼️
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXOviUCz_1x19YWjvUIdks7yaGn0XI1m9LWqSTThXgMv1S6mrVx7EJ6RlT3tsx_NXNkHtAUX7Ks-yCkFqaLMqWUBgpEhpYjeVD9IKYtLRy7wWNAmEUPzG-wVB3GzvbuiyrEEbQg5qr9DnM_7Jqo8a0G-AwNZhgcaVjjodQEZ303k7-uxTDQngbMkh3A1c4eozdxCgEKM0wNNUV2MYEgjDaqlC9-ezFMu7HgxzxV7XwDqMRAk3sIcA2slWrNiF9F0MItGubbuJkRQpSH_hLONUvi3LnSa3BdVJoM4L-q8Ad-nCRfHnSiTOwCqukIF3RPpEzrSDRM47o7JxdTFQP4UuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 میلیون کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
dxai-sk-5feecf996d141afae9e16f8bc072d49a692312d7452a4043fd055c37aba2c8a9
🔺
Base URL:
https://airdropdxns.my.id/v1
🔺
Model ID:
grok-4.5
|
qwen3.8-max
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جزوه ساز پرومکس
❤️‍🔥
از این بعد لازم نیس سر کلاس چیزی بنویسی، فق کافیه فایل صوتی کلاسو بدی اینجا و  با کیفیت ترین جزوه ممکن رو تحویل بگیری!
📝
https://github.com/faithsaly5-stack/Study-Note-Maker
تست کنین نظرتونو بگین
❤️
⚡️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پایان دورانِ عذاب‌آور جزوه‌نویسی دستی!
✍️
یه متد خفن طراحی کردم که می‌تونه ساعت‌ها ویس و فایل صوتی رو به یه جزوه‌ی تمیز، مرتب و آماده‌ی خوندن (Study Note) تبدیل کنه.
✍️
فرض کن ۲۰ تا فایل صوتی داری (مثلاً ۱۲ ساعت ویسِ کلاس یا ویدیوی یوتیوب) که نه وقت می‌کنی همه‌شو گوش بدی، نه می‌تونی کلمه‌به‌کلمه بنویسی. با این روش،
بدون اینکه حتی یک نکته از قلم بیفته
، کل اون ۱۲ ساعت تبدیل میشه به یه جزوه‌ی شسته‌رفته!
🤩
فرقی نمی‌کنه دانشجو باشی و درگیر حجم سنگین درس‌های ارشد، یا دانش‌آموزی که وقت سرخاروندن نداره؛ این ترفند کلاً سیستم درس خوندنت رو عوض می‌کنه. کافیه صدای استاد رو سر کلاس ضبط کنی، بقیه‌ش با این متد!
🎙
دارم یکم دیگه روش کار می‌کنم که حسابی کامل بشه. اگه پایه‌اید و می‌خواید امشب تو کانال بذارمش، پست رو لایک کنید تا انرژی بگیرم.
☺️
✈️
ArchiveTell | S</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFsx_SHX5TTP9oC1ezXf7zb0Slqgt3Px7D8XIMUVyEfAwCk76Z2QbJexdaSIbUHMGcnuzsomLMY8BpovQpa0jbH5ogZQxxd4oTR4e0XhWpWMR6Kt4wAXHGs5rqElRV7_ClAahRHNw1jUTx1-P5iPnT2VgdE5hXwBxI8ii2RsPbtS-5uls1Y-lc1IVYoPoywEcNStFDyHFt-KqPU-JIxyOdYCOEj55WYwX00RuR1-iJThKki60JZrolQttFasSeohJW_8EMakQv8N6Wzug8lBcL0gFFP5H2XXFs_WHm0WD3Slzar2AzqMbkSosPHoCM5HGiPkn7jj3MTrbNTpQfwrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://tabitoken.com/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
120 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-wpJGnjAU50NQr_w85RBuzCfwfO_BY7iilNuqR5qTTsUvjGCFX4EYgeyYzxe90JoweKr9BgEMLkzymgiLk_W4rlktFOOsiBvbPUh773PiKEf8Rntrp_M4HCEm9Z3HJCzeK2BftcNDOUghoAfDfCxgOxJGx5URkDGsJpZgPcynyYlE-I40p7FOzuQktpI5d9YfbCwvLtrEfgyk11ukMwZokHcsdg58V7Dre7WBbyAL0mtBlXScTJWyHCrbkyJi_TD_-pmNlIiqTY2dvYMkTDfgcOeEJEEJx5eo3zT-HbEeVJYYIz7ViqmoX0hUYwa9sw2MJB_idigS6BYogluaxtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20
دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
GPT 5.6 sol | Mimo 2.5 pro | GLM 5.2 | Gemini 3.5 flash | Deepseek V4 Falsh | MiniMax M3
✅
برای فعال‌سازی فقط کافیه یک Gmail یا outlook داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://fapi.leileihog.top/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
20 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5jxn8goG5sxaMTNR4Y27-AK_ZnGdNVvDNhDbsQnw2eL2UqpnNeeazwnuxRdWyJSeunG7EZ44fax4r8d-k8QF_EdsBPV7Dt1WOPzGk1CgRh8PPoz4tY5Q49ctNNjF7iTPKytFi4nu3rTdhE2hKOGc0jRn3-AHXYf5SnBp6n13MfCOSofV3Y0jxgtkGBk8IXYhMEBirhKk-a7ob4AXHWaO9A9JYSSKHfl5O16hsjKZL5bperhns6Z7n2xSdyqCUp8gzuI5A5oXmrlUi79DUUNv1niNaqaMBtXqDt3jqckBvQbXbAQFi3-_WHazcFmCGB6yDL7bp9CWZ79DllnMvbcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10 هزار کریدیت برای دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
GPT 5.6 sol | Opus 4.8 | Deepseek V4 Flash | Kimi k3 | GLM 5.2 | Sonnet 5 | Grok 4.3 | MiniMax M3 | Gpt image 2 | Seedance 2.0 fast
✅
قابل استفاده در
Vega Agent
✅
Base URL:
https://www.getunikey.ai/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcpFC4ph8AB5A9VwaCQneK9gVRpKH69ydMYv-Zxoj7o_NiYwZCoFxHrQg55f28__WgOZsJeG3hlyreEpBGXmb2vzHaO1ceqWUPYrD9TWJp926Yl2OltZnfZwGWeOQ-iRWVnHVvLt2SCIEfEkRADvTptcnG3SVa1wnSPQn9_1lyGjaFD76GVd16MIoFfmgN6VP8IL1OdbQqhTiONmWGXgsl5w931Roah__RxqUrAJxwda0qBlVW3045VJSkqeukpyQqQmsQmHXYTJhcLkNpSViWi16AnuKfHyfMvZ1g8HW6dnKimjON7Mpn8CxPqF-1yUhLBUrUEHRj8t0rKASD5C8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان نامحدود به برترین مدل ها برای چت کردن
⚡️
🆓
با این سایت میتونید به 35 مدل هوش مصنوعی به صورت رایگان دسترسی پیدا کنید از جمله :
🚀
GPT 5.6 Terra pro | Grok 4.5 | Deepseek 4 pro | MiniMax M3 | Gemini 3.6
✅
🚨
توجه برخی مدل ها مانند GPT 5.6 از کریدیت شما کم میکنند ، این سایت هر ماه 3057 کریدیت به شما میدهد
💵
😎
🔗
لینک ثبت نام
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💥
🍌
نانو بنانا پرو نابود شد!
کمپانی xAI مدل Imagine Image 2.0 را معرفی کرد که با قابلیت‌های خیره‌کننده، اینترنت را منفجر کرده است:
🚀
🎯
پیروی دقیق از پرامپت بدون افت کیفیت
✂️
ویرایش دقیق و حذف پس‌زمینه پیچیده با حفظ شفافیت
🔗
پشتیبانی از ۵ رفرنس به صورت همزمان
✍️
رندر بی‌نقص متن روی تصاویر
📈
آپدیت و اسکیل عالی تصاویر
این مدل قدرتمند هم‌اکنون در Grok در دسترس است!
🔥
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=X6HGjCzlBHuiPVW2JgTyTpXZg1i7L809kQFd9g69AU2xj2dpKkETaYZg2rbnHBp-cpSn40OdE0rutpdCE4R2z6QVPX8g-JeRasPYoRd_ii1UDXBs_Rw08ZUg9G-PprWOrdwnV3f2pCk7JAivqMtqvEMwoDdhTpSmOOnFHabwfdkV2VWqJepX17jy0AYxuLjMKI86fzA4qKpQJwbAVJ3FZS9EYV9IIGJWksqdJyZL7vaLFKqY1SZB01lWDeVH9nN_4zQtmlc-hlFPlLcSCS3-BZb1Fr9i1wLsEUb99R7v7FlQCFc-yceWXMXyubX5qTjqb2-wOiZglnprV-s5wwvBiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=X6HGjCzlBHuiPVW2JgTyTpXZg1i7L809kQFd9g69AU2xj2dpKkETaYZg2rbnHBp-cpSn40OdE0rutpdCE4R2z6QVPX8g-JeRasPYoRd_ii1UDXBs_Rw08ZUg9G-PprWOrdwnV3f2pCk7JAivqMtqvEMwoDdhTpSmOOnFHabwfdkV2VWqJepX17jy0AYxuLjMKI86fzA4qKpQJwbAVJ3FZS9EYV9IIGJWksqdJyZL7vaLFKqY1SZB01lWDeVH9nN_4zQtmlc-hlFPlLcSCS3-BZb1Fr9i1wLsEUb99R7v7FlQCFc-yceWXMXyubX5qTjqb2-wOiZglnprV-s5wwvBiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهندسی معکوس پروژه‌های گیت‌هاب با GitReverse
◀
☁️
بچه‌ها اگه یه پروژه خفن تو گیت‌هاب دیدید و خواستید دقیقاً همون رو با هوش مصنوعی (مثل Cursor یا Claude) از صفر کدنویسی کنید،
gitreverse
خوراکتونه!
🔺
چیکار می‌کنه؟
لینک پروژه رو بهش می‌دید، اونم کل فایل‌ها و ساختارش رو آنالیز می‌کنه و یه «پرامپت» جامع بهتون می‌ده. حالا کافیه این پرامپت رو به AI بدید تا کل پروژه رو براتون دوباره خلق کنه!
🔺
ویژگی‌ها:
پشتیبانی از مدل‌های مثل Grok-3، Gemini-2.5-Pro و GPT-5.4.
🐱
دانلود سورس‌کد از گیت‌هاب
🌐
سایت رسمی (نسخه آماده استفاده)
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرار از زندان برای مدل های Sonnet 4.6 و Haiku 4.5
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8sjSTpacHloCnOXSODygEZ7JxooyeNuCw1M6z29mscOn8D8g5o73MrP3YiGRCFTDE-Sa9H2VyOVTsPWAExC9DPSzSgkMlPeEC7A27NMtIvwL8mGf6LMOZFTvHeZgEPznTgXW8pBxzpU-tBXvV-WbPtCDGU2-TfYyuW3QfCpLTFUP3acaEA7wGBL431CL9-1gW7LuQAzwIvXJxzvlpqXolR1vC07s0hCYp2taWhi2SJ58_Q-yypXvaI6df8lYsXT8wjPg9CtJJwmG2mlNDsz1NnsiRaxDjxZvW03bP8Gl2k3T_UGKzu8ynmETOf7PL0_jMddeNAw291W5Za18mwmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
Base URL:
https://tokenharbor.ai/v1
قابل استفاده در
Vega Agent
✅
با جیمیل وارد شید سپس لینک ارسال شده به جیمیل رو باز کنید و 5 دلار رو دریافت کنید همچنین تیک Free models enabled رو بزنید
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فرار از زندان برای مدل های Gemini 3.5 و GLM 5.2
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=ZG4lk8LnDqM8Vw9ZP8UXaTK2GDwNwP7H3wFYXYqTUMYcuWjovztjCcEUmOHHn8lH1FKlKfwULXOpWRA6xLYesmrQI_LKxOGgAlmfo0Ad79artzMIfJeFz8x4KjP0GBCHj4pJneBzqNhRk1CJxNTTDPGXvYxZnscTXbGuwKbttvn7ucx19KideBMmITr_wLAoORI-vQ50oawoZNPr45pGqKBZP17KWVzJnBSKOFOhmDWRPKsIrUD9sRppBhhnp_L7R3QZN0wt-wxd1C0fJayU5VZT7QClJG3wypYgqnc6rzivozj6D7gK8NtaUNxY3uvP_G3-50881oouo8qQQ5LCkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=ZG4lk8LnDqM8Vw9ZP8UXaTK2GDwNwP7H3wFYXYqTUMYcuWjovztjCcEUmOHHn8lH1FKlKfwULXOpWRA6xLYesmrQI_LKxOGgAlmfo0Ad79artzMIfJeFz8x4KjP0GBCHj4pJneBzqNhRk1CJxNTTDPGXvYxZnscTXbGuwKbttvn7ucx19KideBMmITr_wLAoORI-vQ50oawoZNPr45pGqKBZP17KWVzJnBSKOFOhmDWRPKsIrUD9sRppBhhnp_L7R3QZN0wt-wxd1C0fJayU5VZT7QClJG3wypYgqnc6rzivozj6D7gK8NtaUNxY3uvP_G3-50881oouo8qQQ5LCkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمدید فرصت ساخت ویدیوی رایگان با Gemini
♊️
🆓
بچه‌ها گوگل مهلت استفاده از ابزار خفن ویدیوساز Gemini Omni رو تمدید کرد!
جزئیات:
حالا تا
۱۱ آگوست ۲۰۲۶
فرصت دارید که
۱۰ تا ویدیو
رو کاملاً رایگان بسازید (قبلاً تا ۴ آگوست بود).
❓
چطوری؟
تو اپلیکیشن یا نسخه وب جمینای، برید تو منوی ابزارها (Tools) و گزینه «Create video» رو انتخاب کنید.
جا نمونید، برید تستش کنید ببینید چطوره!
😳
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUGdkLU46HwhuLpxMWvaSZYVX9a8svtQPuD485lzHC09iksNnAz03W0-hH0R66j6hWGPt2CiLMPBgh7Jd0LXGBR7J5krPazsy3lNNESeEp6AgYpsmMQHZ3k_sFt5V02VTefQtlL8xf5A8DwrqX3Tod0T8JVwMQEkVPphGX72cwmS6boc-dN71BDZe7OgIcieAZhiOmXlGSd0zQS5ntPkpBoIEOEcgw3-ivOq54-w3nKkk_2ovZDVpfwcJHtoTTeGehwlgo8tGZ9Rp3Utn4qKI89WzxGFe9Owhspgf3hxAsLxgafFtWk5AZdzU5mWtCW1BtE0AMptNQNuYhtet_YqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن خفن و متن‌باز بدنسازی با openGym
💪
💪
اگه از اشتراک‌های پولی و تبلیغات اپ‌های ورزشی خسته شدید،
openGym
یه جایگزین رایگان و کاملاً شخصیه که دیتای شما رو تو سرورهای غریبه ذخیره نمی‌کنه!
📌
چرا باید نصبش کنید؟
💠
دیتابیس کامل:
بیش از ۱۳۰۰ حرکت ورزشی با انیمیشن آموزشی.
🗺️
نقشه عضلانی:
روی تصویر بدن نشون می‌ده این هفته کدوم عضلات رو بیشتر درگیر کردید.
✴️
پیشرفت هوشمند:
خودش حساب می‌کنه جلسه بعد باید چه وزنه‌ای بزنید.
👾
بدون نیاز به پسورد:
ورود امن با اثر انگشت یا چهره (Passkey).
📜
انتقال دیتا:
می‌تونید تاریخچه تمریناتتون رو از برنامه‌های Strong ،Hevy یا FitNotes بیارید اینجا.
✅
صفحه همیشه روشن:
موقع تمرین صفحه گوشی خاموش نمی‌شه تا راحت رکوردها رو ثبت کنید.
💡
نصب:
می‌تونید فایل APK رو دانلود و کاملاً
آفلاین
روی اندروید نصب کنید، یا با Docker روی سرور خودتون بالا بیارید تا بین همه دستگاه‌هاتون سینک بشه.
☁️
دانلود APK و آموزش نصب از گیت‌هاب
🌐
نسخه دموی آنلاین (برای تست محیط برنامه)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH2a7TKQhcbvAxo8xACFYCCaKjc4SoO2aSddiSzqVHYRJeM3F1VOuwlAVJ-Yq9i3_EzgJro7d8Gs3urcXnXdgJ7dVe-gTosAL0HICbWedrpk6cwzLOzChkINoyPMgOkJInUCOEQAiMmj1M5hi9DU0ObuYD_GlPfwb_Jwj-ccLdWKfHK-MNjbJTQRnceuKP85qcihv6FzPWiEarGnBNtfYjfoOZql0i-PxkZnMyvFTke0Pxl564DZABzz-6CNA6RnhJeaVdZEwhTq2pPm0gb4vWmp1lG05tXl1R2GjpJtY_DvKWe9L7RvOzIVoXxCyFjjeZJTDUyGqId0eWyd0JKQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pT0ONWZzlbr4NOSCGJ0mKnpvbZF2hLk5KOM-fOxgUrlRkRnhFaX0_bweUcqh-18rKGor0cPb3NvyGfnCZz4CTcrK7uppUycdwzgBVvaTkMQDwQoyafVFrD7MXhUiG19jlpnNycb2TJqhgHTwCmt7X9slHVQoNbrkztSY9HJXP00bKP91hQZoib-8W2JVL3XnlH_4LcooQ9jNXZFdxtktCibAgzqA3ViquggOsFt6tGkIFQZZDOHg0qKlP35L0yL8h6MQ9N8Q62PBheZWDCd1-j6EVjLe4Ck8bNNO0uktdZ_0qQZW2wVIfvehAslluU_AaMy0IJskFasjjrFedYcITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🆓
دسترسی رایگان 14 روزه به GPT 5.6 sol و Claude Sonnet 5
​سایت و ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده که به ۱۶ مدل برتر هوش مصنوعی مخصوص کدنویسی دسترسی دارین.
💵
😎
​
📌
مراحل دریافت:
1️⃣
وارد این
سایت
بشید و پلن پرو رو پیدا کنید و تیک Free trial رو بزنید
2️⃣
استارت رو بزنید و با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
3️⃣
از داشبورد برنامه Zed رو دانلود کنید ( برای اندروید در دسترس نیست ) و تمام!
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=iCzzeJxAdcMml9facZLywgILQEk-2Xr569nIkJLb4e2mEvyd5z3ZrlWJsgOjvR6AHVd2Iw8xnb_QuISrxWIIV6DJpS27Ari_8oYa8wYvaqCCzikYY1l_XiuTsNlKfs4ZHyWFASJml6i-lqAAwu-A827TwiQVs0QfFWs3eD7sbmQbSiQxvy7igTGbjJWh13R_vK7pPQn323DtUsYPgKOBgNnRFEoSMTIuiG7gfB8ThuF9oHM8Zf7iJDlqVssm8xGFFxk_vKQswbpH1rGFdxVzDG25aH5cnhTb_1JAK5f5fDT8jna7S3GshXDEhddh9mUEx-k-k0rv-f5A34KwvYDqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=iCzzeJxAdcMml9facZLywgILQEk-2Xr569nIkJLb4e2mEvyd5z3ZrlWJsgOjvR6AHVd2Iw8xnb_QuISrxWIIV6DJpS27Ari_8oYa8wYvaqCCzikYY1l_XiuTsNlKfs4ZHyWFASJml6i-lqAAwu-A827TwiQVs0QfFWs3eD7sbmQbSiQxvy7igTGbjJWh13R_vK7pPQn323DtUsYPgKOBgNnRFEoSMTIuiG7gfB8ThuF9oHM8Zf7iJDlqVssm8xGFFxk_vKQswbpH1rGFdxVzDG25aH5cnhTb_1JAK5f5fDT8jna7S3GshXDEhddh9mUEx-k-k0rv-f5A34KwvYDqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چت‌جی‌پی‌تی رسماً تبدیل به فتوشاپ شد!
🖌️
⚡
ادوبی یه پلاگین جدید منتشر کرده که ۷۵ تا از ابزارهای حرفه‌ای خودش مثل Photoshop، Premiere، Lightroom، Illustrator، Acrobat و InDesign رو مستقیم میاره داخل ChatGPT.
😺
🔥
کافیه توی تنظیمات چت‌جی‌پی‌تی پلاگین Adobe رو فعال کنید و با نوشتن Adobe@ توی چت، از تمام این ابزارها استفاده کنید.
✅
این قابلیت از امروز برای تمام کاربران در سراسر جهان فعال شده!
🌐
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX-afkBHvS0clHESDPbMwlmyOQwDdeJEnQwX-rlaVgZGucGzbAVgL8uBVuIm1Sf9UEiPVOdsHf-graJZq46FlRnOHK-Wefr5sxhvXkUpR9BD-7OfCjFb5cVxoCkAECCDJngDIUfjMf6Xa1D3onItuy4LVOTUH63mgZtL3r6QgmLd15O1JE8P5ezK_ehk1DWxzoZQn0AVp_7F5-FFd79u4ND-vIq6_P7YK0sEyhMMXOcrJUy3s5dhxrmwrDiIuwnEZ93IQovOA5pK8r5QgclQSpXXJjXtBdbBsnD2ShznODgjNGQeIQv4LQbbFDGgxHo6HIeSlUXk9-lw1YEaVOAEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک ساز خفن گوگل
🆓
🎵
🩵
با این سایت میتونین با یه پرامپت موزیک و موزیک ویدئو های خفن بسازین و منتشر کنین.
با لینک زیر ثبت نام کنید و ۵۰۰ کردیت رایگان دریافت کنین:
🔗
FlowMusic
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inrZDifQbsWlNwYlF6YhhG9CJYDV-s6j2oiGECijaXfHalxeghMmPMn_y5ndA_vljJ04Fa_KNR2uPPwoZLiQ6sHCxynF0U9UYWLIShVHYJGH2yn4zeFoyWizOzmwKztejyqIi3_bWARf1KriZglYiRsaj2c7oeH-5K7Vx54ZH_fy8DJ6uk4HmeiQdFzO6XbPRY6R-g80r6tDaZclzBoMq9IXGHbVxMFDbvxxyDBa8sT1Utbd8KUMismALDxhIQHR8ianXDDJqaGb4088wt1Irpl0CmfkK91QDONPZlrBfDFpu0x0q9IB386iBOAe9nLsYetIkeXKzIhszUINcw9sdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1500 کریدیت برای دسترسی رایگان به برترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.5 | Sonnet 5 | Gemini 3.5 | Haiku 4.5 | Gemini 3.1 flash lite | Nano banana pro | Nano banana 2 | Nano banana 2 lite | Gemini Omni flash
✅
1500 کریدیت برابر با 15 دلار برای 7 روز
💵
🗓
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kilB5_SfynSgXXmLO-cBi9qvcVIATRW9EnsCPJRGaUWNuOjKqiOkRjrZJGUjrM6KLPgLM31S4Ryd7Lc72ecW1qMYWXbMbXJiiVbj9mlIj5l5AWahTZsuHwwVIOK8CX1HkMPj-PDlgdkhjXyqqasTzZoIOpPoLwGoQtRfdxGJJhzBNfq7z40XPW95OcdIFU0FBD3voL7chX0c8_o8c3odouRkJ43hZBoIOCB2anWJVHYS3lXp1luUy_MMjBYyeeZM8ztan0di6Krli7uij_0KlqIE25cAkdj0VmdMu-KoBj-1S-W8IPKWlrHGbhikj_h8UJmAFgy0am4aHtMUz4A3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به Kimi K3 و Qwen 3.8 Max
❤️‍🔥
🆓
بدون نیاز به کارت اعتباری کافیه وارد
app.clusy.io
بشید، با ایمیل ثبت‌نام کنید و توی پروژه جدید مدل مورد نظرتون رو انتخاب و استفاده کنید.
😎
⭕️
فقط ۲ روز از این فرصت باقی مونده! به دلیل ترافیک بالا ممکن هست سرعت سایت کمی کند باشه
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZgY915S_pbFKA7EfxzeflIf7GXod4JCr0Xd5iq-zwMdFhjxv9FR6fEaUXO70WM9OxggEPm28EXp-SFlyWoo8FxjRKQ4Us9g-5FJn-wfVve_lPuiCaXS2eIrSVX7xDO86Zzybnwu_49uTtkSGuuX5xZb5b1a2mgJh5JzFkEP6CzMBI-9jHbQi_MrYXn_9Drf62pxcuSWB3vmkC-03VBNxTOxf1yff0Y6PZG_ntCBaEey9nWCq4LdWcxr7mB9ttW6XAJDT1B5DQ4VZ0LwUv_4CZ-5q1xNhQihVASegNehA82H0VinubwGwi91dfttaw0zOZf861txrlVsRtuGpXTROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان:
امروز از ساعت 12:30 تا 20:30 به وقت ایران
⭕️
🛠️
مراحل راه‌اندازی سریع:
1️⃣
وارد
سایت
شده و با اکانت Google ورود کنید.
2️⃣
به بخش Account رفته و اکانت خودتون رو از طریق تلگرام فعال (Verify) کنید.
3️⃣
به بخش API Keys برید، یک کلید جدید بسازید و اون رو کپی کنید.
4️⃣
برنامه OpenCode (یا محیط دلخواهتون) رو باز کرده و اطلاعات زیر رو تنظیم کنید:
🔺
Base URL:
https://api.aigate.shop/v1
🔺
Model:
muse-spark-1.2
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYy31SJeZinnyuLM7eEAwCiQv8syey4isNTweXUT6g0f3XBRACozjWPr_GAzKpVCGNWuKHRy1j76V39A4_DHeYKCrWgPyxvq9jqfLPyEKDNIhaF1StT--lTIWzHLBXOgtjKPz5vP1UvqagPez6HVJr1yaYjaKPLDULGnSXUI6NJb6vvqF4t66CGF1lMKiW-S9wfvWgfOtkTuk9xK0XSZK-PfN0Es1c2X94NaV1A6-TcMAz4BAdZw7zEQ1Au8BzYQpMJnLc449TyOmrU4Q_z1nK_k6BAaMXGxdo54naN6UTPbZqjZDu3e1aJ17jqtMP0mI6cHHOUmoOqErnv33whLMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ‌سیک V4 Flash
به‌صورت
نامحدود
و
رایگان
تا
پایان
سال
6️⃣
2️⃣
0️⃣
2️⃣
به آدرس
cnb.cool
مراجعه کنید
➡️
هر
ریپازیتوری
که خواستین را باز کنید
➡️
عبارت
@codebuddy
را تایپ کنید
➡️
حالت
Work for me
را فعال کنید
➡️
تسک
مورد نظر را وارد کرده و اجرا کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVQkDX7CuubPClwQErySLr8WGkk7t1EMDxZkxN2XVbj_Puv6CpXdzhZ0-jz37Ed0Z_HcB70zQkxwPg6MAOJSMNYKbjTkzARfz0cSXySKTW4DEc-ZcLPxbTOAZaQJ1w9dkotPYu_3W3iRdwaJQZ3ZRQ_k7en0WsyTGRpauTilSpKKghf16GrOJWSaevDy2v4Ey-ia1XvPNt9c60SxDaqQzTKxEKs0EvJJHQLITPES4I9sUzVCkXFSgWgJIz-CmwuKkDUwM2zCO38_d0uYmaC4s6FSMgolDw-elHJ0wSgcbrp9ra-s4493xOCZ5VVWu9Re564SkWxyxS0xrnydKXptYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کامنت یه کاربر زیر پست تلگرام در ایکس:
من آدرس مخفیگاه پاول دروف رو می‌خوام
😕
💯
اکانت رسمی تلگرام:
مخفیگاه رو که نمی‌دونم ولی من رو می‌تونی تو خونه پیش مامانت پیدا کنی!
🙈
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpxbdeOja4LAA13kHthvzfYeuLg5HzQ3XE5dGqT6hENXc4HHIaJkNQrawxH9_OgU9S8uB1QK8s56IbMdYPO0ojFfl004zRTmqLe16mWYPhK83YBFwxR_qvJzYg3D3I3m9-9NCJLb51tRxDOgsmj5tn1N4uVQ_xnUye5c5CKAlUDMYrJPYUSqXbDmp19SD7NfMBT-9G0P9Yf09CkuiOPKSX8RKh7bhYnYCenZXqOZ9EeCQFOTkaTXsEgF5ZCq52l7x--rf388COnxUZAhz0N9ODk1Ld5JpZRcfXmpWaPth0JCleEEi8cKAOc_2_Uc7G84Jw6j11ij9-zHBwHSllob7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف فوری واترمارک تصاویر و ویدیوهای Gemini
🚀
🔥
دیگه نگران علامت روی عکس و ویدیوهای جمینای نباش؛ با این ابزار رایگان خیلی راحت حذفش کن
❌
😎
✨
ویژگی‌های کلیدی :
1️⃣
100% لوکال و حفظ کامل حریم خصوصی (بدون ارسال به سرور)
📶
💯
2️⃣
پشتیبانی از عکس و ویدیو با کیفیت های 720p و 1080p
🎞
3️⃣
کاملاً رایگان، سریع و بدون نیاز به نصب
🆓
⛓
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCm1cZx_S86uiIeDJzEG7k0Zq86VRvpBtD32uZ5Vueabpnu-1kum3HxO6YFvo2aZ_sTOO4TXXksaobdgCwResgxC8KTOLgbGMA98hjRG3rLYI6GbE7bC-5jUBFVgD6gig-DafERYKD10VR39tQYZfo279-1hih-3MzwbN0Uj1GpxxeSt3rVruV-X6bMF3NO55zyvuOsx5hz1f02kfCDMITztRGKNEcyg8r9fRJDrjhzVsMMNxahaz7bItqSb0y_SLAJcsujvLFlaSpoyRXcRIZ7hUKKA9QgGw95qzMGY0nRdNz42UuckcR-9WXrm7eKlZHN8fmyzOc9kG9blnLEv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت
Dola
مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت روزانه و رایگان
🔺
کیفیت و قدرت بالا در خلق ویدیو
🔺
استفاده آسان و آنلاین
🔗
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIjtCeXCQuH79P-Iqf_tULY65dVwq4vDT5T9WYu3s1YoWSPhrygCf3GnV4fZlJmxJNYa0dUXGx9hK7mSnuzeucmJ2dfLXq-OOJZEK9mV6DOoMqdQRtRqLoZo9XzZhpHF59c6Eo0Wua9NNQdjXRrpf0iudFXtFSiK72IHmN96sqvc2Px2je6r6kDg_cUeKnlsw9IFBPXJ5yiQmwxD4EiHE0-Zdm6BgRQ6CdZWXLABrV9Y294Ad8LWjM2_7IFcyNTlyZlCFrc5YHP8aijBzO_gPwksMDg_j_k3eHpaH_H-3qQvzZrbnv9ytgi3L-Zku0KO1b20j9rscDWk0bbgLDzLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
گنجینه API‌ های رایگان هوش مصنوعی
🆓
یک مرجع کامل برای پیدا کردن API‌ های رایگان مدل‌های زبانی (LLM) بدون جستجوی طولانی
🔍
✨
🗂️
1️⃣
freellm.net
بیش از 424 مدل رایگان از +30 ارائه‌دهنده با اطلاعات کامل شامل محدودیت‌ها
📉
📊
2️⃣
freellm.sh
لیستی ساده و سریع از سرویس‌های رایگان با نمایش وضعیت و محدودیت هر API
⚡️
🚀
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMlFJvz-KmTpHuJl3outopuKb4s9MUEaRCawKSZk4-C4Jqlfg2zdBBjgEp2kQaWLHrvNmkQGMb1BV-5Z1udZsED5RflwbF8TaLmoealXTVxWnfTwJOUet2mn9ydZ_cZ0m7THb6CBWRHU1ZSlKqW_2XwhN6Tb_AaQiNdqrWGf3DSB8TWYZODsusOSBHjGmCsbZhKcnpZkEpSHbKWQdQxxlMydQ-Zx-V5Eh4ztcDHnzq2SD_qP0YqaMeVi-roVOKmzYyexGc2cK1M3b9XmRbHC0cKJl69anSEwY2QwFPwx357M-E-c64dIhDmCx49ZWovAupEI442v9MnjgWRG7NSoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای اسپارک (Gemini Spark)؛ دستیار هوشمند و همیشه‌فعال گوگل
♊️
🔍
بچه‌ها گوگل با «جمینای اسپارک» رسماً داره هوش مصنوعی رو از یه چت‌بات ساده به یه «ایجنت عمل‌گرا» تبدیل می‌کنه! این دستیار کارهای روزمره و گردش‌های کاری شما رو به صورت خودکار پیش می‌بره.
✨
قابلیت‌های خفن اسپارک:
📄
اجرای ساختاریافته:
اهداف شما رو در قالب وظیفه (Task)، زمان‌بندی (Schedule) و مهارت (Skill) دسته‌بندی و اجرا می‌کنه (پشتیبانی از اجرای همزمان ۱۵ وظیفه).
🌐
وب‌گردی خودکار:
می‌تونه کنترل کروم رو به دست بگیره و پروسه‌هایی مثل جستجو تو سایت‌ها یا رزرو رو کاملاً خودش انجام بده!
😨
مدیریت ورک‌اسپیس:
خوندن و ویرایش فایل‌های Docs و Sheets، زمان‌بندی تقویم و مدیریت کامل ایمیل‌ها.
💻
کنترل مک از گوشی:
اگه اپلیکیشن جمینای روی مک نصب باشه، می‌تونید از راه دور (با گوشی) فایل‌های سیستمتون رو بررسی کنید.
🤒
شرایط و محدودیت‌های نسخه بتا:
❤️
فقط برای مشترکین پولی (Google AI Pro و Ultra) با اکانت شخصی (بالای ۱۸ سال) فعاله.
🔛
ویژگی Keep Activity اکانت باید روشن باشه.
❗️
فعلاً از زبان فارسی پشتیبانی نمی‌کنه و تو بعضی مناطق (مثل اروپا و بریتانیا) در دسترس نیست.
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjeB9KntkgTl2wTrY-joVxq6dzY2m4klxcFRwECdKX0ooEGgfVyEC1pu6hDy3AHgsdmDWfSkUF51pNySF-gbNbR_VasZiW2M5vbVLSkkczNpqqipsLSyAc3m3lEWnKHJq5tQGIGWrkkLyxBb00CnVjBQuIguTiOH2AV4ae9-PywaiSQQFoc7xhfLFZ8aOwy3rsD3FgzsfCL8-pIi07dp7MzLE4YqLEp3E8lFtIUfgFynwxdKAsN_nJtKrkzv9DtnloJBbcFJ_l6uMTYumysZPOtQer0x6UmjHcsv8_Isoi6b1RVmf1CdyTWTCn3w941M8q_4sJBy1Agt8OQyFU75ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی سرور اسپیدتست شخصی با OpenSpeedTest
🚀
🌐
〰️
بچه‌ها اگه سرور/VPS دارید، ادمین شبکه هستید، یا کلاً می‌خواد سرعت واقعی کانفیگ‌ها و سرورهای خودتون رو بدون وابستگی به سایت‌های عمومی تست کنید، ابزار
OpenSpeedTest
دقیقاً همون چیزیه که دنبالشید!
🚀
این پروژه یه ابزار متن‌باز و بی‌نهایت سبکه (حجم اسکریپتش کمتر از ۸ کیلوبایته!) که با جاوا اسکریپت خالص و HTML5 نوشته شده و بدون نیاز به هیچ دیتابیس یا فریم‌ورک سنگینی، سرعت آپلود، دانلود و پینگ رو اندازه می‌گیره.
📶
👩‍💻
👩‍💻
✨
چرا این ابزار خیلی خفنه؟
🔺
اجرا روی همه دستگاه‌ها
✅
🔺
نصب بی‌دردسر
✅
🔺
تست فشار (Stress Test)
🔤
🔺
بدون ردگیری
🔞
💡
کاربردش کجاست؟
برای تست سرعت واقعی ارتباط بین دو تا سرور، عیب‌یابی کندی شبکه وای‌فای خونه (LAN)، یا تست کردن افت سرعت موقع استفاده از تانل‌ها و پروکسی‌ها.
📌
👩‍💻
لینک مخزن گیت‌هاب و آموزش نصب
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔥
یه
پلاگین
به اسم
oh-my-hermes
برای
Hermes Agent
معرفی شده
🏥
این
پلاگین
سعی کرده چند
قابلیت
مختلف رو توی یک جا جمع کنه تا نیاز به نصب چندین
پلاگین
جداگانه
کمتر
بشه
✅
😍
از جمله امکاناتش می‌شه به اینا اشاره کرد:
✔️
هماهنگی کدنویسی و مهارت‌های codemode
✔️
سیستم مصاحبه هدف و پرامپتینگ برای برنامه‌ریزی و مهندسی حلقه (ulw-plan، ulw-goal و Loop Engineering)
✔️
معماری حافظه پیشرفته (شامل Dreaming، Pruning و مدیریت کانتکست)
✔️
سیستم حافظه لایه‌ای (بلندمدت و لایه‌های L0 تا L3)
✔️
متخصص‌های دامنه‌ای و قابلیت‌های تحقیقاتی
⚡️
تنظیمات آماده‌ای هم برای استفاده
سبک و سنگین
داره که می‌شه فیچرها رو
روشن
و
خاموش
کرد
GitHub
🐙
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdWzww2c-QXTRGNpfVa3YtgpBB7f0F2hH08UE185riRhNBtwuk4kNf3lZL0NyKA93ZVgiSgdRG50BcDZ5uJTHRuyXQ89sOFsAoBsNGW8n_g9_IxKCyQHVqQRN7lzCxRY-bN0GBg4XJyxnmbYHsz5gYxYaSola04hIPR4WV_6uEVW_BG-kqI3plnvC89VI9AO2iM4-PnahyMYZEd-yxqJUtmFrC5xZ9HaXwJZ6tdvec16P1c49_NB_2ruzdsfxEfftIruAx5jks3im3e2kUVV12vVJCG-FoP9dpnnDijqnlPq5k2xEMFI6eR5_827GzIkpdxvgOic34LYS4VJcEy4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱ میلیارد توکن رایگان  تا ۱۲ آگوست
🚀
🆓
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcCGcLCn-3A3HH9h6z0Ge0HqgcBaYR3EM_zPIpVrnZq2MZudH0W1J21QSCLWw7MMFmK9o6uXay9ukmx2Jeq7nVIRyppB56wiKPbk3TtVAP0bi6ssBq1b0zcZWlVzyWkryxhPGjWVWyOtdXiKwq6V1GSLMmbx6BAxLS1-D05cOnAa0EUOJSlv0yjKnCLF2GjwxLlThZikKHsuMEGo6kC50i6XkWKKHT_WxfzDAVIvGtwnrfTyHENmytGmI4AxjhxztVARRTY5Omy144cVD7XPhTV9Ywmf534NyfNmukcgLuqX1BAjkztEO05UqNXLxx6XEFarVi33eVpgUbCfB6HU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwlsiQpv9BsT5yTd_SGun-bu2Kz7weJWx-Ha9y91KJvyAc7SEQoM0F0w2N_Jf-T789oEeM_9RHoxOqDaJxKF_Y73gjFh6Va6SbWcc9P4kyMIyro1kKcxuzSdkGafnmxAygDeogN6_0C--oI-m2dyYPjYl_7tSwzossH5Mwlxf49gLAmi_wBOtbYCRBJMth1m-i9LT3aIALsNC28s3U-aWAZ9Nh9ejUy71JGfzLYxUbhGFHlyFG9e69biFDOPHvu6mxkjqvB6S_3QchNbL_TXkD6FRqUIDs-yIjR_H8gF5ly84ulUS-kPGWGbxm6wDvSBCmbafbJeJ3Z_GIHVINXE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=vHVzsvZAjct5M0pOiiYAnOZ4XwNzCQqDqubzO34-roZ0TZwMwVeddPLDwKfw9tqYFfjB3Yw1XKw7LvTLMcQpflYOfEbDQe0iC1-zhupFbMU6UaSS2WhnQ8XhHYhDXh7QqgTMfyZW4p1sYof2YvT8vINtPO9YHTH2mOwELfIk6Y7uV4ji1s9ZDNrfnHTr7mWRI6o8iCbgP8cT5xPnqjVEDasCQLmbsgjp6dHjo0gImv0tKlRv5MpNKL5rKUQYs0c7ScJQUJuQa91JclVn3dMKxWUSb_ZCzpG-zu4rBS5G7JmdrqX_WLhds6qcAaX9znLIN8MQ0KgqIYXcQGmgi2aNljC3JuiGGwfSNuaeNGczLhyv_9IE0uL86RnI9-9gTmjerKsQbl292o86F6-gaFuAfWgtsyt4ZDOYABqqccb-okA_pUK-cZAB1J3aykchOs0NmsEkcXeAT7VoeEArOGvbiaz64l-e1AUEdtC8dHIXxoBaPwGzR5qljCjihAxRYHFl2Ieq7CKlnDsWoz3D6q6gu-6JXm2jXeSBpqcNadeabfewZ8-aER5NCk4braFbpPhktm94-jN_mty9Do-rVXRQId83csVvq1UuwCqb31qlWXH5P_PPy7HHrnzxCY9Dwm7fHQqNHey2tzYAZx4DOj4eYAdIkF7Q43sFeIExnUqaS14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=vHVzsvZAjct5M0pOiiYAnOZ4XwNzCQqDqubzO34-roZ0TZwMwVeddPLDwKfw9tqYFfjB3Yw1XKw7LvTLMcQpflYOfEbDQe0iC1-zhupFbMU6UaSS2WhnQ8XhHYhDXh7QqgTMfyZW4p1sYof2YvT8vINtPO9YHTH2mOwELfIk6Y7uV4ji1s9ZDNrfnHTr7mWRI6o8iCbgP8cT5xPnqjVEDasCQLmbsgjp6dHjo0gImv0tKlRv5MpNKL5rKUQYs0c7ScJQUJuQa91JclVn3dMKxWUSb_ZCzpG-zu4rBS5G7JmdrqX_WLhds6qcAaX9znLIN8MQ0KgqIYXcQGmgi2aNljC3JuiGGwfSNuaeNGczLhyv_9IE0uL86RnI9-9gTmjerKsQbl292o86F6-gaFuAfWgtsyt4ZDOYABqqccb-okA_pUK-cZAB1J3aykchOs0NmsEkcXeAT7VoeEArOGvbiaz64l-e1AUEdtC8dHIXxoBaPwGzR5qljCjihAxRYHFl2Ieq7CKlnDsWoz3D6q6gu-6JXm2jXeSBpqcNadeabfewZ8-aER5NCk4braFbpPhktm94-jN_mty9Do-rVXRQId83csVvq1UuwCqb31qlWXH5P_PPy7HHrnzxCY9Dwm7fHQqNHey2tzYAZx4DOj4eYAdIkF7Q43sFeIExnUqaS14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBesJxYYmnnWJMZ0HCv3yd3IQhRAid0itAd94ISvN-MDdt1Z73imn39uneAUXWjJev_jaxpcDHtN33_fJnDDmrpg7hzq7wK_eyxoP1sNafykrh8xz11vRE9-GD022zcnh9UHt8D0De5xNUjFzWVynLQ_bXCMeKhySrstgXHodWLoX5h_Yin3ODj_Z2Rsb0ul51tAxKbImZKfPLIP1v-pBQyDn1ChNXzP9Jb-0vbxFERuoAaVpg2E6JgralV8RQB4_zboKOcz1y_Q54fzJju0K0c31jcCAMdoZbAOHcytHTzrXyfyMRb01QU1gm4TFeXNN8sVsizl4j7_y8il-Qq76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
500 دلار اعتبار رایگان API برای شما!
‏همین حالا کلید اختصاصی را دریافت کنید و از مدل‌های Opus 5 و Opus 4.8 لذت ببرید:
🚀
Api keys:
sk-2UddB27hnFA1z2LKWKnq6BQaffBLe86FU0htxAHm0Q9n5vjW
Base url:
https://agentrouter.org
Model:
claude-opus-5
|
claude-opus-4-8
✨
کلاینت های مجاز :
🔺
‌Claude Code⁩ | ‌VS Code⁩ | ‌OpenCode⁩ | ‌Hermes⁩ Agent | Qwen Code | Kilo Code | Cline | Roo Code | Open Claw
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3p0BZri3mEpyOndc1ETCftIqOm8inisU9EWuBTYneP9ghumtyAjzNxpnyQYVDRpGIwD-BC3010CgDeMhFLP6-E1TuBvSVNbjXCjDGZ-ZX4_VxAnv4GkP5zf11FXCM4Ak2rK4lkNC_BBEKDeYRszr0GWoUVcc-BEq8uJZQGzFbVrgSGxRxy6tfE6v9SVr5BqQvP_9YtoSt_ysDG7mDbQus-hWLmWLzF5Qih_ouX9i3sVzuFqrgFHN_Kc4pO2cwV0De5HFiptUcvgaLWNhK4XADDNoy3-965RaVoyWsBpypiVNsv7s_eVKzBVwuvJHWLECqphXr8MsuwrgR8kwV2TRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آموزش تبدیل کردن صفحه چت سایت Qwen به API
🚀
اگر در موبایل هستید از
Kiwi Browser
استفاده کنید
‼️
✨
آموزش اجرا :
وارد سایت
chat.qwen.ai
بشید و یک حساب بسازید
در سیستم کلید F12 رو بزنید تا Developer mode واستون باز بشه
در اندروید از سه نقطه بالا سمت راست از منو گزینه Developer tools رو بزنید
وارد تب Application بشید و گزینه Local Storage رو پیدا کنید حالا کنار این گزینه یه مثلث هست بزنید روش و سایت qwen رو انتخاب کنید
یک جدول باز میشه و آخراش یه متغیر هست به نام Token اون فیلد روبروش کپی کنید یا توی کنسول این دستور رو بزنید خودکار کپی میشه
copy(localStorage.getItem('token'))
اینی که کپی کردید در اصل api keys هست ، ممکنه بعد چند روز منقضی بشه و دوباره باید بگیرید ، تمام حالا میتونید توی هر جایی که دوست دارید استفاده کنید
Base url:
https://qwen.aikit.club/v1
Model
:
qwen3.8-max
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
