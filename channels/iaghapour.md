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
<img src="https://cdn4.telesco.pe/file/NiWzZt2Ubu22T1vayxXX2xSAcvw8hBpRQxlgwUzxgaKmEguaoeZJyYlPKjKqCD1qpGSeBM3aBLQ_C4Z07y6obC3WgZibdZitbqzxFXsj36wH8hL58rCN_MPnfGP_oBAPAPCoOaRyThKKdHnEv9hZUBmsGgTh6TW3kPCAwfm74BJdtki4tPdKW0MEoO7wYkO26imIhs4hK2McFMiXU35plLXmszIN_TBTWNAheThX7NbSX4RXY5ckqeAKzMs5pb7yFoqy4qRHHxkkiyi40Y61iHpjFuYDINtWnKgPbcMuFp7A4owPgzXyVeeaUD5RnK-lMZSwERedQqVMJFmbr-IVnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.4K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-3116">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌های تبلیغ‌شده حتماً بخوانید
!
از شما تقاضا داریم برای درک بهتر محدوده مسئولیت ما و حفظ امنیت مالی خودتان، پیش از هرگونه تصمیم‌گیری یا خرید، حتماً این 2 پست را مطالعه بفرمایید:
🔹
قوانین و محدوده مسئولیت ما در قبال تبلیغات
🔸
قوانین خرید از سرورهای تبلیغ‌شده
هدف ما همیشه حفظ شفافیت با شماست. همان‌طور که پیش‌تر هم بارها تاکید کردیم.
ممنون از همراهی شما
🌹</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/iaghapour/3116" target="_blank">📅 16:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3115">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkC58qSaLrXTUNuoSHbMMQtJTEE0W8esmQwOP5pZNo3kV9pAWAOU09Heo70Z5O4pHoI2bhETY4Ubp7U4KO5ewodUN42pLgOqDGJa52rqtNm3ZEBpk6nArOylaaUhW2eOfl6dHVjw9xtSKbS4y-_cjazBbDQ1K6uuaWR0qz7Gg0CpANTfo8a0bHp7m_MknQqSNLFhGHFGwRWMNqzP32GDrYz6XFNUoHw6X32QbWptMnyFG6vyLjU0Wt3vj4v3kU8i2J5S6P2No0SBfvzIqKNcgTyYUhElwAreFv-LRbnm2wu4SmGVmi-gyYquMDXL1SyntEeOxUuaH_uQzFfs-fjFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
معاون وزیر ارتباطات: احتمال قطع اینترنت در صورت بروز جنگ یا ناآرامی وجود دارد
وحید یزدانیان، معاون توسعه شبکه ملی اطلاعات، در گفت‌وگو با سیتنا درباره احتمال تکرار قطعی اینترنت در شرایط بحرانی توضیحاتی ارائه داد.
⚙️
محورهای مهم اظهارات:
🔹
احتمال بالای محدودیت در بحران‌ها:
به گفته وی، در صورت بروز هرگونه شرایط جنگی یا ناآرامی، اعمال محدودیت روی شبکه‌ها و احتمال قطعی اینترنت بسیار بالا خواهد بود؛ هرچند هنوز سطح و ابعاد این محدودیت‌ها مشخص نیست.
🔹
نقش مستقیم رئیس‌جمهور:
طبق تأکید شخص رئیس‌جمهور، هرگونه دستور قطعی اینترنت باید منحصراً از طرف او صادر شود و در صورت اتخاذ چنین تصمیماتی، نقش مستقیم دولت و رئیس‌جمهور در اجرای آن نسبت به گذشته پررنگ‌تر خواهد بود.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/iaghapour/3115" target="_blank">📅 14:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3114">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromOIFE Lab Admin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irsC8WprNIFmLa5OIMa2xTG14uAC_7k85ZKG37LNaf1uNg6SQywo4iRWUduHbupwDIJjC7pGlufH-QO7jieu8lansaeFkaHGzmWJwfdQub4wDz9dwOGL1QQFuvBcQ3K4q8ZamKEMLxTQBE-c-vjS6yoY8RYNeuwMZOgzkh9YxkU6IjMv8uI3KD7GW6JUdtIqkW4LyM3Q78awlvB-7Mdp5F2Kp6EvDFtEVQe29KLuKbC0IN41llxKz5R5auGrkq12Nx4vhl8IfLQ9Ylt31-NSQPdiKxrU29Ch4Br5sUdPi4F6BzNLYcO6dsQGqtLdv0YA15WcUlOStpyGDo6kT9Kkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
دسترسی به بهترین ابزارهای دیجیتال، در OIFE Lab
اشتراک سرویس‌های محبوب
هوش مصنوعی، طراحی، موسیقی و آموزش
❤️
چرا OIFE Lab؟
چون خرید خوب فقط تحویل اشتراک نیست.
🛡
گارانتی
کامل و شفاف
⚡️
تحویل سریع
💬
مشاوره
برای انتخاب اشتراک مناسب
🤝
پشتیبانی کامل
و پاسخ‌گویی بعد از خرید
🛒
برای مشاهده محصولات و خرید، وارد فروشگاه شوید:
🤖
@OIFE_Lab_Bot
💬
برای مشاوره و انتخاب اشتراک مناسب:
💬
@OIFE_Lab_Admin
OIFE Lab | ساده، سریع، مطمئن
❤️</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/iaghapour/3114" target="_blank">📅 21:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3113">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vu3VW0Kvh9tWduBJeh9lDG4XcYoTEDzy9eqmfHsbDwOp9VqP0gWJ4NWbE-dCgxO0FlyqdoiKVhRzr95-1SdSbK3EY-r6G0tM8wODaA_66bqAtMqfdGRjgkyIrIJVp0DzjEpcvSkzalt-UMoU4Sogq5VzRkFfuZtddgqKxrXQ9PBRFyPn5kKEAQfckWnCuJxQZLB_d6lgvtfWrYsL51X4uv1itHYdfZLRa7TP7xGPTmkfy1AeXYOpdSmaE4ljK2XbCP-Q3Or0oO3x9V14a9oBBk4JPqFAkV3BWMlzl5j9XiiiM7hiyHBwWxM9_UflYjn1Fkc4pmoQ7B4QzXJBUeZwRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔐
مهاجرت به SSL داخلی؛ ۱۶ بانک گواهی امنیت بومی گرفتند، ۱۰ بانک در انتظار
در پی لغو گواهی‌های امنیتی بین‌المللی بانک‌های ایرانی توسط صادرکنندگان خارجی (CAها) و اختلال در دسترسی کاربران، پروژه اجباری دریافت گواهی SSL بومی در شبکه بانکی کلید خورد.
🔹
بانک‌های تکمیل‌شده:
۱۶ بانک از جمله بانک مرکزی، ملی، ملت، صادرات، پاسارگاد، تجارت، مسکن، پارسیان و رفاه هر پنج مرحله دریافت گواهی SSL بومی را تکمیل کردند.
🔹
جامانده‌ها:
۱۰ بانک در حال طی مراحل هستند؛ درحالی‌که بانک سپه، بانک مشترک ایران و ونزوئلا و مؤسسه ملل هنوز اقدامی نکرده‌اند.
🔸
چالش جدی کاربران iOS و وب‌اپلیکیشن‌ها (PWA):
اپلیکیشن‌های اندرویدی با تعبیه زنجیره گواهی (Certificate Pinning/Bundling) مشکلی نخواهند داشت؛ اما از آنجا که ریشه گواهی‌های بومی در مرورگرها و سیستم‌عامل‌های جهانی (مانند iOS) تایید نشده است، کاربران آیفون هنگام استفاده از وب‌اپلیکیشن‌های بانکی با خطای امنیتی SSL و عدم باز شدن صفحه مواجه می‌شوند مگر اینکه پروفایل ریشه گواهی را دستی نصب کنند./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/iaghapour/3113" target="_blank">📅 20:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3112">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrzY43vTByxlX0k9__zpKjfFrPkO7MPci1f4IqdEbnm9qmmrHxVIhkCx9nvpNK-ubBi9qK6eDdumtZQe4gTQWFOhRahNXyfeIB_rQee_DTDub9g_xggMJnqWugCu7MVMQm8v9geCutn0IcvlgtHq9SJ6cHb5BzGqqQEkiZHRMj5V0RMmG166WIVK0bgccHRCJlg_Jh61juGDRSBSWDMgY3azcz4XB5zGRPReOdAKqEoRZfre240Fy9cHhub8U4L9VFDGOLgW8B_JIf4RcajsHl4k3wc1T200vo-nsSqGbFKxY_KlBZ6Hg7A-Zq0LcFZQxXMQv_hCtf9RpukfmAtpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار امنیتی فوری: تلگرام دسکتاپ ویندوز را سریعاً آپدیت کنید!
پژوهشگران امنیت سایبری یک آسیب‌پذیری بحرانی با شناسه
CVE-2026-107181
(سطح خطر ۸.۱) روی نسخه ویندوز تلگرام دسکتاپ کشف کرده‌اند که امکان سرقت سشن و دسترسی کامل به حساب را تنها با کلیک روی یک لینک فراهم می‌کرد.
🔹
تزریق دستور در ارتباط بین پروسه‌ها (IPC):
عدم اعتبارسنجی کاراکتر سمیکولن (
;
) در ارسال لینک‌ها بین پروسه‌های تلگرام، به هکر اجازه تزریق دستورهای سیستمی را می‌داد.
🔸
سوءاستفاده از پروتکل متروکه
interpret:
:
این باگ در ترکیب با دانلود خودکار مدیا در گروه‌ها، فایل‌های حیاتی پوشه
tdata
(شامل سشن‌های فعال و کلیدهای ورود) را بدون تایید یا متوجه شدن کاربر به کانال مهاجم ارسال می‌کرد؛ به‌ویژه برای حساب‌هایی که Passcode لوکال نداشتند.
🔹
رفع کامل نقص در آپدیت جدید:
این روزنه امنیتی در نسخه
7.2.9
با حذف پروتکل آسیب‌پذیر و ایمن‌سازی دیتای سوکت محلی رفع شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/3112" target="_blank">📅 16:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3111">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوب داده</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QP6-ysADY-PhVXpkhVqAMfj9cWtknameJ9Fg65H4peOWedbTiLvgGwgCLCeBWQaaniJscKgay7BycIAGqabRhAhloHYut9hfuzi8aYFHO9z02J7gkbSfpfEMwpICPC0n57SotYbXGzt9Xr4mEYTmy7KMghM4lFrIBPQhAmy5Zy2xkWJEkE2dZzx0lSYyrEtu4YCPa9oS2eRNv8HFNPjCw6LhTjMwUIwfGEKciBbane3104oz8s4YMeAmg7H3bGd7SCW9GxhZvDL_9oXuujX-Tfp-yXwsMFKRlFWfmbnFwoXz945X6CC005DQ9qxuvhf9J8VzP-I9vTl0C0gY9y-PQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
IPv6 برگشت؛ ما وصلش کردیم، تو هنوز نه؟
😏
روی هر چهار سرویس ایرانی وب‌داده،
IPv6 رایگان
دریافت کن؛ به IPv4 جدید هم نیاز داشتی، از پنل تغییرش بده
🤝
‏
🇮🇷
مجازی استاندارد:
پورت ۱۰ گیگابیت، از ۷۰۰٬۰۰۰ تومان در ماه
‏
🇮🇷
پلاتینیوم HPE Gen11:
پورت ۵۰ گیگابیت، از ۱٬۹۰۰٬۰۰۰ تومان در ماه
‏
🇮🇷
میکروتیک:
لایسنس دائمی Level 6، از ۱٬۰۴۰٬۴۰۰ تومان در ماه
‏
🇮🇷
ابری ایران:
پرداخت ساعتی، از ≈ ۱٬۶۴۰ تومان در ساعت
سرور داری؟ از بخش «شبکه»، گزینه «دریافت IPv6 رایگان» رو بزن.
👌
⚠️
پایداری و کیفیت IPv6 در ایران تضمین نمی‌شه.
👇
حالا که برگشته، فعالش کن! خرید سرور:
🛒
https://webdade.com/Iran-VPS-IPv6-back
🔖
آموزش فعال‌سازی IPv6:
https://webdade.com/blog/enable-ipv6-iran-vps
📞
031-3740
🌐
webdade.com</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/3111" target="_blank">📅 21:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3110">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkvubTIHzkeknGRZrSRMKCkC0ERNCvV7NXMfCCKVEjUSgKSZXRxDSIql9CrymEj2nM68wJ1_HPcGU3BgeZCnuOCyrVLxBHeBwiEH47p7gf1yI2GfbwCf-xYnIKqq1XqL9cYFgiLujmsVN3UWofjk8_wRW_CjH4EESgH-Cf0jLUOnNA9gHyCtRBkB_DCrbQYIKYIo7TySlDEc30QYEUwtK4Eob3b9DLYHSUUSooSwwxzhM0faMiyyZxPjL8i8s9M3l6G6wgWmFDHIVwpgSv_NwYLbUwLfwoGbFl-JnmueK7aQq4WClxbHkqC0SfTKyaMe8YLZzECLIzyO0IXRO7uirA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تداوم جنگ بی‌پایان دنوو و هکرها؛ کرک‌های مبتنی بر هایپروایزر از کار افتادند!
قفل ضد دستکاری
دنوو (Denuvo)
در جدیدترین نسخه خود سازوکار امنیتی تازه‌ای را پیاده‌سازی کرده که روش‌های دور زدن پیشین، به‌ویژه کرک‌های متکی بر هایپروایزر (Hypervisor-based) را با اختلال اساسی مواجه کرده است.
🔹
مسدودسازی شیوه‌های بای‌پس سخت‌افزاری:
در بازی جدید Star Wars: Galactic Racer، دنوو وابستگی مستقیمی به برخی قابلیت‌های پردازنده تعریف کرده؛ به‌طوری‌که خاموش کردن یا دستکاری این تنظیمات بلافاصله اجرای بازی را متوقف می‌کند.
🔹
از کار افتادن راه‌حل‌های قبلی:
متدهای متداول پیشین برای خنثی‌سازی لایه‌های حفاظتی روی این نسخه به‌طور کامل بی‌اثر شده‌اند.
🔹
ردیابی هکرها:
توسعه‌دهندگان دنوو علاوه بر سفت‌وسخت کردن لایه‌های فنی، اقدامات جدیدی را برای شناسایی و ردیابی تیم‌های فعال در حوزه کرک (از جمله گروه‌هایی مانند voices38) کلید زده‌اند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/iaghapour/3110" target="_blank">📅 20:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3109">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuAPURkVPGQoDj2GHZozpDjsykf0KKWZbGor6prg2pc5QnZV-iX4ZTRPR0HX0PmSGs-b1c_oY4yBsNp60OE1djYSpYQSwsTjE86EXsnzvUaMiq_IkeEXDZJFbjOthpn4NVcDd4-QKK7Nj7Tf2vz1U5vEbBio0FdluJDct3g_63aqMqYvOIM45eyD9x0zjUzSgBYwyTHF_PRAxFYs0tZ2tv6upvHA8zSvfLg2PHfyBNJscE5E8WlZ8Q_BydolTpBbLjCds7c7M3qhRB3pG28JA7IfJ60gREvd3AdS8nnGGcEkS82s_rZ_lnZ_1CgOpxGL4kMeTjvpIXweFD6otnHx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سامانه «حسام» فعال شد؛ مشاهده و بستن غیرحضوری حساب‌های بانکی مازاد!
بانک مرکزی سامانه
«حسام»
را برای مدیریت یکپارچه حساب‌های بانکی بدون نیاز به مراجعه به شعب فعال کرد:
🔹
مشاهده تمام حساب‌ها:
امکان دیدن فهرست کامل تمامی حساب‌های بانکی و مؤسسات اعتباری فعال به نام شخص در یک پنل واحد.
🔸
بستن آنلاین حساب‌های اضافی:
ثبت درخواست الکترونیکی برای بستن حساب‌های قدیمی، مازاد یا فراموش‌شده.
🔹
انتقال خودکار مانده‌حساب:
پس از طی مراحل قانونی، موجودی حساب بسته شده مستقیماً به «حساب پایه» انتخابی کاربر واریز می‌شود.
🌐
آدرس سامانه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/3109" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3107">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbIKtp4FABRa6nOR6VM3rwWarWszw4lx4zohNF8BNAa2Uac9aaTj06rQHdEzirGeHNxoWy2DdWupCVy3qwS-zX9iPyvsY_gj3Pc8aPstp815oM5WHB2qXnmcuYdUqV-iDBIsgPM2OaGjhSVdaXzTHa7K6IqP-A6UfBcKOMkfAimK6JsO0ObfjRBxkIvBffx3AYUVwFlkADtpv_ETIQa-k4SUqkQCXqEG5tAl8VHZkYGMuQuFXPQDJ8YkHLN0mteNNtGWKDynsVEJNxhuo9QgJj-4BxsFlGUwYwidl98YAcXryfX47G0xkfkeD4_a5B-fbiIWKHAq8kZoqRmUfR9HeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت آسان کانفیگ‌های VPN میکروتیک در مرورگر
پروژه متن‌باز
MikroTik VPN Generator
یک ابزار تحت وب و بدون نیاز به نصب است که اسکریپت‌های آماده کانفیگ روترهای میکروتیک (RouterOS) را برای پروتکل‌های پرکاربرد تولید می‌کند.
🔹
پشتیبانی از ۴ پروتکل اصلی:
پروتکل
WireGuard:
تولید اسکریپت سرور (
.rsc
) به‌همراه فایل کلاینت (
.conf
) و بارکد QR با تولید کلید امن در مرورگر (Curve25519).
پروتکل
OpenVPN:
خروجی اسکریپت سرور به‌همراه پروفایل آماده کلاینت (
.ovpn
).
پروتکل
SSTP و L2TP/IPsec:
ساخت اسکریپت سرور برای اتصال آسان از طریق کلاینت‌های بومی ویندوز، مک و موبایل بدون نصب برنامه جانبی.
🔹
امنیت و ذخیره‌سازی محلی:
پردازش تمام مقادیر درون کلاینت و ذخیره فرم‌ها در
localStorage
مرورگر بدون ارسال اطلاعات به سرور ثالث.
🌐
اجرای مستقیم ابزار
💻
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/iaghapour/3107" target="_blank">📅 19:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3106">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVOR8ti2adr_oKWqxkP6OBQ3X1xAmjglYIvDUx9ZqFx97NhH_V7cuw748cJJNPu05PynvTxbIP9BQ8YWnikt-yxtPSExoU2h4p9zarms6Gyc8CkJXg9fd8XwmAXEHZmf8iT--L1NopTEgzTNwfsEdJ3Or1rrbLxypsHiYPFrcoCMcdP0a8RtvvcqIT76u3ouxnJ8HKyZkY6lVXOG-okB6CqyrzeAINz31bc0lxHukRC5hjtTkSEdUyLDd1xY9VU0Qb9E-cWWrfQ-W4Px4Q_OuzkVXs_9wHYu8DM8kz0M8nEniAaxlLWJ8CqqHTt_xfeTyuUrjqacH66pc5R7hH01yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گوگل ابزار تشخیص محتوای هوش مصنوعی SynthID Detector را عمومی کرد
گوگل پلتفرم وب
SynthID Detector
را که پیش‌تر در انحصار رسانه‌ها بود، به‌صورت جهانی در دسترس عموم کاربران قرار داد تا امکان شناسایی رسانه‌های تولیدشده با هوش مصنوعی فراهم شود.
⚙️
جزئیات و نحوه عملکرد این ابزار:
🔹
نحوه کارکرد:
این سرویس با بررسی واترمارک‌های دیجیتالی نامرئی جاسازی‌شده در فایل‌های تصویری، ویدیویی و صوتی، اصالت و منشأ تولید آن‌ها را ارزیابی می‌کند.
🔹
پشتیبانی گسترده از توسعه‌دهندگان:
علاوه بر محصولات خود گوگل، توانایی شناسایی واترمارک ابزارهای هوش مصنوعی شرکت‌های OpenAI، انویدیا و Kakao را دارد و اپل نیز به‌زودی از آن پشتیبانی خواهد کرد.
🔹
محدودیت تشخیصی:
این وب‌سایت یک دیتکتور همه‌منظوره نیست و صرفاً فایل‌هایی را ردیابی می‌کند که حاوی استاندارد SynthID باشند؛ همچنین تفاوتی میان محتوای صددرصد تولیدی و محتوای ویرایش‌شده قائل نمی‌شود.
این قابلیت تشخیصی پیش‌تر درون موتور جستجوی گوگل، جمینای و مرورگر کروم نیز تعبیه شده است.
🔗
آدرس سایت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/iaghapour/3106" target="_blank">📅 16:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3104">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe7423d72.mp4?token=Sj3ldsC5nuu-YexxjbsgUTrWogqyEioGL93zbEg42RwlmyfTlkZGc-_9UDNeU4hFFQlF1UillZOG-T8NLaGbpmiUERFT6Z2LY17j2LFUL_Km6sATaCVcK84cvNtSvBbMsFpPtzwljs4Ic5P3QJsK117-CFYhLjFpyXWMb-ObVoZF3gv3GLEUfPRN5eBVXVe2NUNtNJOr0F_nNhFpk3NfgrqqXMk8UvJFlXlFvWpOYHnGA0lr8DDV1ZR4LkyuQI3-_Z5-s2ViTxkuItW9CieAMUBB65Go_MiuLsrA0v-YSMPbRztWyVfdRDVYymImvvph1GDL7TSWXdVZGICpGAU_8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe7423d72.mp4?token=Sj3ldsC5nuu-YexxjbsgUTrWogqyEioGL93zbEg42RwlmyfTlkZGc-_9UDNeU4hFFQlF1UillZOG-T8NLaGbpmiUERFT6Z2LY17j2LFUL_Km6sATaCVcK84cvNtSvBbMsFpPtzwljs4Ic5P3QJsK117-CFYhLjFpyXWMb-ObVoZF3gv3GLEUfPRN5eBVXVe2NUNtNJOr0F_nNhFpk3NfgrqqXMk8UvJFlXlFvWpOYHnGA0lr8DDV1ZR4LkyuQI3-_Z5-s2ViTxkuItW9CieAMUBB65Go_MiuLsrA0v-YSMPbRztWyVfdRDVYymImvvph1GDL7TSWXdVZGICpGAU_8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی (دوره چهاردهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده  اکانت هوش مصنوعی مشخص شد:
👤
برنده عزیز با آیدی یوتیوب samansh2915، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/iaghapour/3104" target="_blank">📅 20:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3103">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9681d3a3.mp4?token=Zut6m6RDvb-v7f29KAi8iYioTJ59xrRh9SB8JGZ3odb8JBDVtiG5heMjg-yumGobIsOYCyb4LGFRho3gtZljjjtfRonSNnDi83MDOPWDULmvHRSVMtElxMsStOBBNhig2lI7C7oMzfn_peBiI51MxqOKABKRaW2NqyDldmOdXrtpikIYjAIP1h7wxb1hywp3S5zU4aQVuX7cBaNdo9F9uk900Oxo7rOUH9X9wmwBvZaDcfu1BawjysFW25bDk8pxTq02c19IDrF7iiqjn2XNKR6zX13w5sTUyqF7heB2YgAh2zHNyrODArtCnklzwCg0upshmJC8Y4MFZs8ZIX07xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9681d3a3.mp4?token=Zut6m6RDvb-v7f29KAi8iYioTJ59xrRh9SB8JGZ3odb8JBDVtiG5heMjg-yumGobIsOYCyb4LGFRho3gtZljjjtfRonSNnDi83MDOPWDULmvHRSVMtElxMsStOBBNhig2lI7C7oMzfn_peBiI51MxqOKABKRaW2NqyDldmOdXrtpikIYjAIP1h7wxb1hywp3S5zU4aQVuX7cBaNdo9F9uk900Oxo7rOUH9X9wmwBvZaDcfu1BawjysFW25bDk8pxTq02c19IDrF7iiqjn2XNKR6zX13w5sTUyqF7heB2YgAh2zHNyrODArtCnklzwCg0upshmJC8Y4MFZs8ZIX07xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوگل از Playground رونمایی کرد؛ ساخت بازی‌ها فقط با متن و پرامپت!
گوگل پلتفرم جدیدی به نام
Playground
(زیرمجموعه Google Labs) را معرفی کرد که به کاربران اجازه می‌دهد بدون نیاز به دانش برنامه‌نویسی و صرفاً با نوشتن پرامپت‌های متنی، بازی بسازند.
🔹
طراحی با پرامپت متنی:
تعیین قوانین بازی، فیزیک، کاراکترها و محیط بازی (دوبعدی یا سه‌بعدی / تک‌نفره یا چندنفره) با چت مستقیم با هوش مصنوعی.
🔹
موتور هوش مصنوعی تلفیقی:
قدرت‌گرفته از ترکیب مدل‌های جمینای، نانو بنانا و لیریا (Lyria) در قالب یک فریم‌ورک اختصاصی بازی‌سازی.
🔹
اجرای آسان تحت مرورگر:
بدون نیاز به نصب نرم‌افزار؛ بازی‌های خلق‌شده مستقیماً در مرورگر لپ‌تاپ و گوشی اجرا می‌شوند.
🔻
این سرویس به‌صورت رایگان عرضه شده و مشترکان Google One سهمیه مصرف توکن بالاتری دریافت می‌کنند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/iaghapour/3103" target="_blank">📅 19:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3099">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_BeyvORt0pf6RWI9Ey7fbww4pRT-rxijkNl7mG_lNRmaHsCwBrRP_QhkZz8tQjqJXBATZIplBxvZADT1dj6dFqrX981RE2vN3olhm-7m6shBgBM6JxsUg2JiBSSKlBMhoO-fSSKcs1MAknOxuHdjGB5NxmK8OiquTeVh_3IysXEwwK9g9xR-4g5dzD-PZpOkMLtkkS34iEClpKkKhnkHSY3Z2DQG25B768c7kSXL3zxa0u-qJPhLiW1hfXGggIqy_j73w2Osz2LzCXN4RvsYZKJ6aJoTiOfpsxX8nrRx6wvFO9foKy1J5aSdF5wTR1rgVo3A9vltYiMYh5sHJkh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
وب‌اپلیکیشن کاربردی ارتقای کانفیگ‌ها با ECH، فرگمنت و چینینگ
پروژه متن‌باز
Proxy Builder
یک ابزار تحت‌وب کلاینت‌ساید است که به شما اجازه می‌دهد کانفیگ‌های تکی یا سابسکریپشن‌های VLESS و Trojan را مستقیماً درون مرورگر به ECH و فرگمنت مجهز کنید یا آن‌ها را زنجیره‌ای (Chain) نمایید.
🔹
ارتقای کانفیگ با ECH:
افزودن خودکار پارامترهای
ech
و اثر انگشت TLS (
fp
) به کانفیگ‌های تکی یا کل لینک ساب با پریست‌های آماده (کلادفلر و AliDNS) جهت عبور از مسدودسازی SNI.
🔸
تزریق فرگمنت و سایفرسوئیت (Fragment + Fingerprint):
اعمال پارامترهای
cs
و
fm
با نسخه‌های بهینه‌سازی‌شده پریست V1 و V2 به‌صورت تکی یا دسته‌‌جمعی روی کل محتوای سابسکریپشن (متن ساده یا Base64).
🔹
سازنده کانفیگ زنجیره‌ای (Chain Builder):
ترکیب دو پراکسی (مثلاً وارپ/ورکر به سرور اصلی برای ثبات آی‌پی و رفع فیلتر) و تحویل خروجی آماده JSON برای هسته‌های Xray و sing-box.
🌐
اجرای آنلاین ابزار
💻
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/3099" target="_blank">📅 20:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3098">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA0Y16WQ-1O4L5Tls2HObSg1ZVoqZG0hYyVsqKOF6qVgqhxOY5cAHcgAxaVDx0GHia8JFh8MWRsg0SCZ9b28Ac66v_uDeejxx_Fc75Zuifx7uOufaperyvdGBSe8AtUtFnD-YpsaehDrHhDbVGTqOAMT74PBdSNNS2nNF7X9_Yg317jtDjnDubWi7xnGpx6lf5Q4Cyn2EFdmrLMnW-py1HWTwjHH04KlFoAjw81BS8uz64HasW9aEVvJt7pZA0YYrUSXqHqQs1Kn0YaZ0Zeo9Qg4tZ71YDhKNCMf08gRMMg5Qzo4-dv_Oi-75I9HcbqkKX7fCoeTEpsQieyVRKMluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی نرم‌افزار EtherDNS؛ ابزار مدرن تغییر DNS و مدیریت شبکه در ویندوز
پروژه متن‌باز
EtherDNS
یک جعبه‌ابزار همه‌کاره برای ویندوز است که علاوه‌بر تست و تغییر سریع DNS، امکانات کاربردی مختلفی برای عیب‌یابی شبکه در اختیارتان می‌گذارد.
🔹
تغییر سریع میان ۴۸ سرور DNS تاییدشده:
دسته‌بندی سرورها بر اساس ایرانی (تحریم‌شکن)، گیمینگ، جهانی، ضدتبلیغ، امنیت و حریم خصوصی، همراه با امکان تعریف DNS اختصاصی.
🔹
بنچمارک دقیق بر پایه UDP:
تست پینگ سرورها با ارسال کوئری‌های واقعی DNS به‌‌جای پینگ معمولی ICMP (برای دقت بالاتر) و انتخاب سریع‌ترین سرور.
🔹
نمایش زنده و نمودار وضعیت:
مانیتورینگ لحظه‌ای پاسخ‌دهی DNS، وضعیت آداپتورها و کلیدهای فوری Flush DNS، تجدید IP و ریست کامل تنظیمات شبکه.
🔹
اطلاعات کامل IP و لوکیشن:
نمایش لحظه‌ای Public IP، ریجن، ASN و رفرش خودکار پس از اتصال یا قطعی فیلترشکن.
🔗
لینک دانلود در گیت‌هاب
🔻
این برنامه اوپن‌سورس است، اما کدهای آن توسط ما بررسی امنیتی نشده؛ قبل از اجرا روی سیستم اصلی، سورس آن را بررسی کنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/3098" target="_blank">📅 19:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3097">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📡
موج جدید اختلالات شدید روی شبکه اینترنت کشور
طی چند روز اخیر وضعیت اینترنت دوباره به‌شدت ناپایدار و فرسایشی شده است:
🔹
نوسان شدید، قطع و وصلی مداوم و افزایش بی‌سابقه پینگ.
🔹
مسدودسازی و فیلتر شدن بسیار سریع IP سرورها.
🔹
اختلال و دراپ گسترده پکت‌ها روی رنج آی‌پی‌های کلادفلر.
اگر در اتصال کانفیگ‌ها و تانل‌ها دچار افت سرعت و قطعی شدید هستید، این مشکل فقط برای شما نیست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3097" target="_blank">📅 14:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3095">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDZAwcnUdr8DS5v5Z9R1kIR9Sq_JxFF-aIzxBedRZ_TBBUNOwzySHiUczcVlhy5oV2blCOSfdQvDh2fzWy8ja5sGvDT-JCQdv0AvxJUeAmTfUFVkjzT77a75sLeiZiTuRSGj6yRz7W6FpvpKRcVthhHu5Yjy6l7xQe7l-mkmkm_jtOwFPWTaqHAkpORMQPxq_ObWZ9Ha36Do8FuXYiZYoFoApPUZ6RYU2PstqAAXqjamoVuGicitdjv_aidLgFwSa5q3SXYTST144cdkaDXhzGWK5eGfkG6qGJo1TyDRed05faLVMe6MRTSjjBJQoeexmTqK6ThN69vNlRZpqy8rqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کلادفلر تأیید کرد: ناهنجاری بزرگ و افت غیرعادی در ترافیک اینترنت ایران
داده‌های رسمی رادار کلادفلر نشان می‌دهد ترافیک اینترنت کشور از صبح یکشنبه ۱۲ مهر با افتی ادامه‌دار و تغییرات ساختاری بی‌سابقه روبه‌رو شده است.
⚙️
شاخص‌های کلیدی گزارش کلادفلر:
🔹
افت ترافیک کلی:
کاهش محسوس در ریکوئست‌های HTTP و داده‌های جریان شبکه (NetFlows) از ساعت ۷:۱۵ صبح ۱۲ مهر که همچنان پابرجاست.
🔹
تغییر سهم پروتکل‌های وب:
سهم ترافیک انسانی HTTP/1.x از ۵.۳٪ به ۱۵.۲٪ جهش یافته و سهم HTTP/2 از ۹۴.۷٪ به ۸۴.۷٪ افت کرده است (ترافیک HTTP/3 و پروتکل QUIC پیش‌تر نیز بسیار ناچیز بوده و عامل اصلی این تغییر نیست).
🔹
افزایش سهم درصدی IPv6:
سهم IPv6 از ۴.۳٪ به حدود ۱۵٪ رسیده است؛ این افزایش به دلیل افت شدید حجم کل ترافیک IPv4 بوده، نه لزوماً رشد فیزیکی دیتای IPv6.
🔹
اثر ملموس روی کاربران:
افزایش شدید پینگ، اختلال گسترده در اتصال تانل‌ها و کانفیگ‌ها، و لگ سنگین در بازی‌های آنلاین.
هنوز منشأ این وضعیت میان محدودیت‌های هدفمند زیرساختی یا اختلالات فنی مسیرهای بین‌المللی رسماً تأیید نشده است.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/iaghapour/3095" target="_blank">📅 20:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpfjovhS94GcrhSjOtgOGM3kJPC9AEHT950aCYXXxrohjSWd8Uf6Vja7KRYZ43qR3Ik15a4CDITvgKXszvG6AKW8hCbaiwvxw_yX6f6KH3UrF8qddto8omxQvKZ6gIjCsWqwhIzctAZt9hLKoToPrWMBMYggjuGjvhgV_05qaGngD8_fNbhz63uxE0yA6N01BoNYLDeskiO76-LWFA4cCo1j3f9INnuagBwILUKTxf6DFs2HI8U7EcSW_iWMPtLadPno1BeLRGdge9EOwjoM3xZo5FX4U2gh9AYfk4i_SSQ0fg4sjK2BSNp2UcDXdkcU1-ay7NPHJY7hHwpOUS3nIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پرونده جنجالی فیلترشکن جامپ‌جامپ (JumpJump)؛ شایعه هک فیک بود، اما بدافزار واقعی است!
اسکرین‌شات فروش اطلاعات کاربران جامپ‌جامپ در دارک‌وب ساختگی از آب درآمد، اما بررسی‌های فنی نشان می‌دهد خود این برنامه یک تهدید امنیتی بسیار خطرناک است.
🔹
نسخه‌های تلگرامی دستکاری‌شده:
نسخه‌های غیررسمی پخش‌شده در کانال‌های تلگرامی با سوءاستفاده از آسیب‌پذیری‌های اندروید تلاش می‌کنند دسترسی ریشه (Root) بگیرند؛ دسترسی که به مهاجم اجازه کنترل کامل دستگاه (دوربین، پیام‌ها و فایل‌ها) را می‌دهد.
🔹
رفتار مشابه گروه‌های سایبری APT:
تغییر سیستم آپدیت به کانال‌های تلگرامی و جعل امضای دیجیتال برای نصب بدافزار سیستمی.
🔹
مجوزهای خطرناک نسخه اصلی گوگل‌پلی:
حتی نسخه رسمی نیز ۳۷ دسترسی غیرضروری از جمله IMEI، فایل‌های شخصی، سیم‌کارت و دیتای رفتاری را ثبت می‌کند.
🛡
اقدام فوری:
اگر این برنامه را نصب دارید، فوراً آن را حذف کرده و دستگاه را اسکن امنیتی کنید.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/iaghapour/3094" target="_blank">📅 16:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBeEFcJua4xKyn8bMJd1OGzlMij22Q9NxwOdB_T7I6CwEzEnHrrSLzQGRKehJlgpyxLlq4OyqhQXvRqo4YPCLrX4J3PiXYnGIeHzVpMj8YzoKHsagRu9NHLdaYnQu_BpzLA53pufyicnEm5gw212vcHnt-3ciQoLvnsg-HNjfQWoByzCF0heeQ9xQ2EDPrkwiMHiwKrJOWTwp890ve9hPKPYGG0uoWFy97tXJg2vBYFA9niwBE7Qhc-7VWsVoQxrv3pQ8B24aZYe2WBbLhDWo6ytN4RpaBSVjYG7oB0qBBN1N5yBKLuO9me--B3JTKVFSUsJ0ARclIevfSxoLJrr2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مذاکره‌کننده گروه باج‌افزاری «کیل‌‌سک» بازداشت شد؛ مدیرعامل ۱۶ ساله یک استارتاپ هوش مصنوعی!
مذاکره‌کننده مظنون گروه باج‌افزاری بدنام
KillSec
شناسایی و دستگیر شد؛ فردی که در پوشش زندگی حرفه‌ای خود، مدیرعامل یک استارتاپ حوزه هوش مصنوعی و تحول دیجیتال بوده است!
⚙️
جزئیات ماجرا:
🔹
هویت دوگانه متهم ۱۶ ساله:
وی در معرفی رسمی خود مدعی شده بود که هدفش کمک به کسب‌وکارهای کشور عمان و منطقه خلیج فارس برای پیاده‌سازی راهکارهای هوش مصنوعی و ورود به دنیای دیجیتال است.
🔹
نقش در حملات سایبری:
شواهد نشان می‌دهد این نوجوان به‌عنوان مذاکره‌کننده و نماینده گروه KillSec با قربانیان حملات باج‌افزاری تماس تلفنی برقرار می‌کرده است.
🔹
سرنوشت قضایی:
متهم اکنون با احتمال استرداد به پورتوریکو روبه‌رو بوده و مجازاتی تا ۱۰ سال حبس در انتظار اوست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3092" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqKCewYLSjpAUrRoTlr9o4qPGQbJvhVsACsxMc-Deq5_cpJESgWLA38iV1hfEBbAJKpOa0DBXWc_la6oB4EVMn2kfzdX_x4ZzUc2m3Ie300IvM0zM3sqdQXnjirohkDQUzQuYv-KNxRYIjo8E0JwGVWB8KKW15pCHir0fwnUdYHdek-r527Z6nzdiCAzs5oAUCg-YC6Df1RZ-6oYvUUsUnsO_vb4EFoZiiVXEcngPsKeIFo96hpTGxaYrSIGhoQHI4hVtefW-15dXKxTsGQI74tLq2_i40eqihAT6DEMkq9aDZf5rMTpsN2gM9Q2b_0gm_u0v7DzOrFHUfEzzfyRkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
️
پایان دسترسی رایگان به جمینای پرو و فلش
گوگل با به‌روزرسانی اسناد پشتیبانی خود سیاست‌های جدید دسترسی به مدل‌های جمینای را اعلام کرد که بر اساس آن، دسترسی آزاد به مدل‌های پیشرفته محدودتر می‌شود.
⚙️
جزئیات تغییرات و سطح دسترسی پلن‌ها:
🔹
کاربران رایگان (از ۱۷ مهر / ۹ اکتبر):
قطع کامل دسترسی به مدل‌های Pro و Flash؛ تنها مدل فوق‌سبک
Flash-Lite
در دسترس خواهد بود.
🔹
پلن AI Plus (ماهانه ۴.۹۹ دلار):
حذف دسترسی به مدل Pro؛ دسترسی فقط به مدل‌های Flash-Lite و Flash محدود می‌شود.
🔹
پلن‌های AI Pro (ماهانه ۱۹.۹۹ دلار) و AI Ultra:
دسترسی کامل به هر سه مدل Flash-Lite ،Flash و Pro حفظ می‌شود. همچنین قابلیت پردازش عمیق
Deep Think
بدون هزینه اضافه برای مشترکان AI Pro فعال خواهد شد.
📊
قابلیت‌های جدید و سیستم محدودیت مصرف:
• امکان تنظیم سطح پردازش و تفکر مدل‌ها در سه حالت کم، متوسط و زیاد (تحلیل دقیق‌تر به قیمت مصرف بیشتر سهمیه).
• ریست شدن سهمیه مصرف مبتنی بر توان پردازشی هر ۵ ساعت یک‌بار تا سقف مجاز هفتگی.//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/iaghapour/3091" target="_blank">📅 17:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3089">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzrbllilMIkwGhnuDY7AEMWEz2ISkjdDRDnGTVCXJNsB7Ieku0s_kRteKO4DoBVX6AQFlVa3y67q-Yguo6x0-jjAC0_qM0VfSc3kmSOG8BcxemXjfILlUX4FIVHjR52rtRMBq9lt1FrIdvOHCq6QEzWwWV7QlWdXntCDzJ3SwTboG8QrQxUoZ14hjkpRoa-X4P2pCMPbmMDgNW0-XiO2qOBSIRhEO_l1FymJNSQtDxx7iRpM4b-KTrLTlaOe9755qryeDZnmKWdkecgKHknJhu-fYFU79XPNm1_58Ph8tBkggmkaJ6myPsoC55fGRuuZ4bM5BppSFCu5-vlj2Wk8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
معرفی FleetPanel؛ کنترل‌پنل امن برای میزبانی هم‌زمان چند ربات تلگرام روی یک سرور
اگر چند ربات تلگرامی را مدیریت می‌کنید، اسکریپت و پنل
FleetPanel
به شما اجازه می‌دهد همه آن‌ها را به‌صورت کاملاً ایزوله روی یک سرور لینوکس بالا بیاورید.
🔹
ایزوله‌سازی کامل هر ربات:
هر ربات دارای یوزر مجزای لینوکس، استخر PHP-FPM اختصاصی، دیتابیس MySQL جداگانه، کانفیگ اختصاصی انجین‌ایکس و گواهی SSL مستقل است تا مشکل یکی به بقیه آسیب نزند.
🔹
پنل وب و CLI:
داشبورد مانیتورینگ مصرف CPU و رم، نصب خودکار ربات از طریق وب‌هوک و دریافت توکن، تهیه بکاپ و بازگردانی خودکار.
🔹
امنیت سخت‌گیرانه:
رمزنگاری توکن‌ها و پسورد دیتابیس با استاندارد AES-256-GCM، هش ایمن رمزها با Argon2id، فعال‌سازی CSP سخت‌گیرانه، محافظت در برابر حملات CSRF و مسدودسازی وب‌هوک‌های بدون Secret.
🔹
عدم تداخل با سرور:
اسکریپت به سایت‌ها، گواهی‌ها و دیتابیس‌های موجود سرور دست نمی‌زند و فقط فایل‌های اختصاصی خود را اضافه می‌کند.
🔗
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3089" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سلام بچه‌ها، وقتتون بخیر.
به دلایلی حساب‌های توییتر (X)، اینستاگرام و چند تا از پلتفرم‌های دیگه‌مون رو خودم موقتاً غیرفعال کردم. از طرفی طی روزهای آینده رویکرد و مسیر کانال هم یه سری تغییرات داره و از مباحث فیلترشکن و... فاصله بیشتری میگیریم.
فعلاً نیازی به توضیح بیشتر نیست؛ سر وقتش کامل براتون توضیح میدم. ممنون از همراهی همیشگی‌تون.
💚</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/iaghapour/3082" target="_blank">📅 20:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3081">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwYvzl54uqYo60v-YtRp8n9iNLuVMKCiVxARA7ZudJzb-H417nQWWR3yF2JOoGzo9GiyWWKvlYhv8yrOfvG9vYyO3bwDYmyEXtsQTw0563hthiYSgcNkkLgCGF0bfSSrH-I9NbEThoNkyNfdCTt-YsFfSFFggfFTlk4MmX1UkMrJIdJ9lXXJywZmhwHZ6ZZysxKttYBCGD5m5l6S5zPNf5zXBFm9R_Av5e4vaQ3tG2bNkJBTX4Fj6p-ddFkaJrWAjmhyYLdOqtbMyHUnq0GmZf1GYo9P8utdxar7QMWkkovRqrDl_kgReeTvj2cLoAglyuQvzvH-VpPqEQkYAHsjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
درخواست اپراتورها از وزیر ارتباطات: فیلترینگ اینترنت ثابت و فیبر نوری را بردارید!
در جلسه کنترل پروژه فیبر نوری، مدیران اپراتورهای اینترنتی با اشاره به هزینه‌های سنگین توسعه و عدم استقبال مردم، پیشنهاد رفع فیلترینگ اختصاصی روی شبکه ثابت را مطرح کردند.
🔹
پیشنهاد رفع فیلتر برای جذب کاربر:
نماینده صبانت اعلام کرد برای ایجاد انگیزه در کاربران و افزایش فروش ترافیک جهت جبران هزینه‌ها، مسدودیت پلتفرم‌ها حداقل روی اینترنت ثابت برداشته شود؛ چرا که کنترل امنیت در شبکه ثابت ساده‌تر است.
🔸
اقتصاد در حال احتضار اپراتورها:
نمایندگان شاتل و پیشگامان از خسارت‌های چندصد میلیاردی ناشی از قطعی‌های اینترنت، هزینه‌های استهلاک باتری‌ها در خاموشی‌های برق تابستان و عدم اصلاح تعرفه‌ها گلایه کردند.
🔹
کیفیت پایین اینترنت ثابت فعلی:
به گفته مدیرعامل زیرساخت، کیفیت ADSL کشور به شدت افت کرده (سرعت آپلینک ۶۰٪ مشترکان زیر ۸ مگابیت است) و همین امر بار مصرف را به شکل نامتعادلی روی شبکه موبایل انداخته است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/iaghapour/3081" target="_blank">📅 19:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7E8XU7EbAM14LDB_BNv8A_y3_X0Ru0Ij8xPFr4um_RisucExTJdQc8vNVxYDeY6KqXWsSvjKT1gedjcoZP2E6nraoC1Uq9ynB-w53s8ZkccmEiKcE_n4flhHYvS9xwtF_NfAN4itMbdxDDxdPDDvpBSyfy50cpDHFg-JAXVjHueUAA7GYDW2Z5hj2sLxnGfk_LdPS5EBxlhaXVqHALn1bxgwQiSBkR0cwXtXCG2Ck3kF4wueuja9uhK8wGdlZ-XXdz5uo2szmNSR_kNzj8SqI5nBLPmpKCz-Zo1fhR2BjejKXgnGEwsWFIbLYae67LjSxuBEUdXLBcKr-7kaJcRsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی‌ها واقعاً فکر می‌کنن ما همین الان از پشت کوه اومدیم!
🏔
😅
ماجرا از این قراره که وقتی ما بین کامنت‌های یوتیوب قرعه‌کشی می‌کنیم، تو ویدیوی اعلام نتایج، اسم، عکس و آیدی دقیق برنده مشخصه. حالا اتفاقی که میفته اینه که یه عده از دوستانِ فوق‌تخصصِ جعل هویت، تو سه‌سوت میرن تو یوتیوب اسم چنل و عکسشون رو دقیقاً شبیه برنده می‌کنن، یه آیدی مشابه هم میسازن و میان میگن: "سلام، من همون برنده‌ام، هدیه‌م رو رد کن بیاد!"
🥸
🎁
رفقای زرنگِ من! فارغ از اینکه این هدیه واقعاً ناقابله و فدای سرتون، ولی یوتیوب یه چیزی داره به اسم Handle (همون آیدی با @) که تو کل دنیا یکتاست! یعنی هیچ‌کس نمی‌تونه آیدی تکراری داشته باشه. ما هم موقع تحویل جایزه، فقط همون آیدیِ اورجینال رو چک می‌کنیم، نه یه اسم و عکسِ فیک!
🕵️‍♂️
خلاصه که سرعت عمل و خلاقیتتون قابل ستایشه، اما متأسفانه جواب نمیده!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/iaghapour/3078" target="_blank">📅 20:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPwDAkE-1XnDRcn3GASkTirdHTknaj0oDbhFuqBCrSpCv5ZTiqtIg2Xx6SW3jIv9pnrX9kmsB6xiVHBe_JxjaGizpHv_dt94eDQRw3C7E6E71lQj6coRivE0NcC1iwF3yhpdfFj1OaYVq3ehmuP8JeXxPlNfq7kz0tN7e6TaBceXhX6Rduzdju4EhdBxUL6XlA9CEOfiuRrB2vQpKMytW17tEgVa3dwDi0mes2nXqAemuBZ29OvOW8GEHDNRcaY1yyFytE7pmmyG9gMu74aOq9ZlJ9SMNfngf2OWJHyGVqs2sMxqIpKGr7Q1CeqTnDdrdvpPRj37eSt1pGH2ouKr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
مدیرعامل مخابرات: اختلال اینترنت برطرف شد / وضعیت IPv6 بررسی می‌شود
محمد جعفرپور، مدیرعامل شرکت مخابرات ایران، در گفت‌وگو با رسانه‌ها از برطرف شدن اختلال چند روز اخیر اینترنت و فیبر نوری خبر داد.
🔹
علت اختلال چندروزه:
قطعی اینترنت، سایت شرکت و سامانه ۲۰۲۰ به دلیل ارتقا و به‌روزرسانی زیرساخت‌های سامانه‌ای مخابرات رخ داده و اکنون اتصال کاربران بازیابی شده است.
🔹
وضعیت پروتکل IPv6:
جعفرپور تأکید کرد از سمت اپراتورها منعی برای ارائه IPv6 وجود ندارد، اما سیاست‌های بالادستی شبکه در اختیار آن‌ها نیست.
🔹
احتمال تأثیر تغییرات دوران جنگ:
وی اشاره کرد که تغییرات فنی اعمال‌شده روی شبکه در شرایط جنگی ممکن است همچنان بر وضعیت دسترسی به IPv6 اثر گذاشته باشد و این موضوع نیازمند بررسی فنی دقیق برای شناسایی منشأ اشکال است.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/iaghapour/3076" target="_blank">📅 14:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/3074" target="_blank">📅 20:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3073">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeuILUpFsWRKTjdug3Ks2afWJhwDPLXiJ5NCnity76cz21vyCZmOn3_QdyCdk7YHvbS_IXmhjH0lXoLCgy2YTGsQMMGP_-x9kughOQSi0W5LjGJe58PAEcopTP_Pbxktyozgy_rwOqjt60qAxHYA7R1Ru2JqKMQdMwgv90z4oqrTAY9XYW3YYBjMVhAmlueCSP9_XN0HcBVpuEBP671emDQL4El7xen-92j8JBEOHmARpqqvZFjXABXW3EU5oSNp85NINilRaLXis7-CkTRVLarTq8TJY7XLz565cZVupvNnFBwAbXrQ5Atg8cSDcW42XyS3_vp7xK_YWV3NkxFkgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
تولید ویدیوهای 1080p با هوش مصنوعی برای تمام کاربران گوگل فعال شد!
گوگل قابلیت تولید ویدیو با کیفیت
1080p
را در ابزار
Google Vids
برای تمام کاربران عادی و مشترکان Google Workspace در دسترس قرار داد. این ویژگی با بهره‌گیری از مدل پیشرفته
Gemini Omni 1.1 Flash
کار می‌کند و ورودی‌های متنی، تصویر، صدا یا کلیپ‌های موجود را به ویدیوی خروجی تبدیل می‌کند.
⚙️
قابلیت‌های کاربردی و کلیدی:
🔹
توسعه هوشمند صحنه‌ها:
امکان افزایش طول زمانی کلیپ‌ها با حفظ ثبات کامل در نورپردازی، چهره کاراکترها و زاویه دوربین.
🔹
هماهنگ‌سازی و افزایش رزولوشن:
تنظیم دقیق مدت‌زمان هر فریم برای تطبیق با صدای گوینده، به همراه ابزار ارتقای وضوح (Upscale) کلیپ‌های قدیمی به 1080p.
🔹
سرعت بالا در تولید:
رندر هر صحنه ویدیویی در این پلتفرم در کمتر از ۳۰ ثانیه انجام می‌شود.
سهمیه استاندارد به تمامی حساب‌های رایگان گوگل اختصاص یافته و کاربران طرح‌های تجاری و پولی سهمیه ساخت بیشتری دریافت می‌کنند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/iaghapour/3073" target="_blank">📅 18:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭕️
اجرای مستقیم و بی‌دردسر پروژه‌های داکر با Docker Compose در دوپراکس!
🔹
دوستان عزیز، یکی دیگه از قابلیت‌های فوق‌العاده دوپراکس بخش App Space و پشتیبانی مستقیم از کدهای داکر کامپوز هست!
🔸
اگر پروژه‌ای دارید (مثل ربات‌های تلگرامی، پنل‌های خاص یا وب‌اپلیکیشن‌ها) که با فایل
docker-compose.yml
اجرا میشه، دیگه نیازی به سرور لینوکسی خام، نصب دستی داکر و درگیری با کدهای ترمینال ندارید. دوپراکس یک محیط کانتینری کاملاً آماده در اختیارتون میذاره.
📝
مراحل اجرای پروژه‌های داکری:
1️⃣
ساخت فضا: از منو وارد بخش Container Platform بشید و یک App Space با منابع دلخواهتون بسازید.
2️⃣
تب Compose: وارد فضای ساخته شده بشید و در بخش Topology، روی تب Compose کلیک کنید.
3️⃣
وارد کردن کدها: کدهای فایل داکر کامپوز خودتون رو مستقیماً در ویرایشگر پیست کنید، یا اینکه خیلی راحت با دکمه Upload YAML فایلتون رو آپلود کنید.
4️⃣
اجرای نهایی: در نهایت دکمه Apply changes رو بزنید. (حتی گزینه‌ای برای جایگزین کردن امن منابع قبلی یا Override existing resources هم وجود داره).
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کانتینرها، شبکه‌ها و والیوم‌های (Volumes) تعریف شده در فایل شما رو در لحظه می‌سازه و پروژه رو ران می‌کنه. یک مدیریت کاملاً گرافیکی، سریع و حرفه‌ای!
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/3071" target="_blank">📅 20:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSLVeAyUIwakMXFCpPCqVnyNpZNbH0HlPaQZRK4V71MwuMIbawa9Yb0WyugC73P8a-5sZ9UXAnPUXwuOnp-3PmVeoA8zVxPGWQbNG3phv5Ixc1Dmu0Ep_KctIhEgJWff3AnKBgl5SX87c_5A5GVKck6QrAdEhiYEMgpvuEaghgeWz-C3vkqHzlLnknBui2ABOq78Z6uGK78qUavv6PUBM0M13Fq4dpRJjg7hkxLiLh6LvBEYQMx2gdEa6b1u9DLZeU5-NBb1kUyaeTdbH8kcicrDck23ZGvv1gQ3YgjyzJTRYA0S-hY6PB8Iw387w-0U7BmtduPGxXt8WbAq7dsLNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0N5G79GMxFCN8jvor_iKjIgpv1KHCzUovW2yso3QWJ5bYhYjN4JRxwRSbpdGo5UqSDTBMQ6ccsgmh4HvMGByKjOQkT5_c96zPCk09l1jvO12c2IathIq6LENa3D780A8ppLwUbKXW2lWEzqAUpgqZIwm0d2StulYUg5BSCMANQPEIhcAGn25YMKT-gRDdcCPloRDASw_T5en5KM4isG3tYjN0laPRtyW6sdPXMpQQjuvb6b5RijCMzF1kBVt5Iimhh39S0lhPsdoNSFZxyi0LkdVT0ILOjO8F31OlxdhLGTxZNFEpc2XImrgeNfWuPB1C5Jy-zGfrrp3Y_8znRe3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه همراهان عزیز کانال!
💚
به لطف و حمایت‌های گرم شما، تونستیم
8 عدد کیف
مدرسه و تعدادی دفتر و... رو برای چند تا دختر کوچولوی دبستانی تهیه کنیم. (همشون تو عکس جا نشدن)
این هدیه ناقابل، نتیجه
مهربونی
و
همراهی
تک‌تک
شماست
و از طرف همه‌مون به این بچه‌ها تقدیم می‌شه. سال قبل هم اگه یادتون باشه اینکار انجام شد.
اطلاعات بیشتر
ازتون ممنونم که باعث و بانی این اتفاق قشنگ شدید. دلتون همیشه شاد و لبتون خندون.
🌹
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/3069" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3066">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=v3l6v5sSJFhmNINLhB4fnjyfiFGIENxQG6RzNo-VOcCDGt8-5lbjRMo-cTuVdruYm7ubIa1Tf33bWu2NqVp9zBnSRvQl3rztqzZCzcNqIi9S3gyuUzE7GGLp1rlt_u8ioCXkDlB4GxlJXBmNN6hMgCWxGjRp88Ipy1538KGkwJzrvlG6OHh6257cLFW9HlPEVVsdyObkOHfn-IPUpKOR2wUJd8X1ddqDaBK9IMK8wX-F-j5873PgAf3_f6qmiaxnNY1jSVEx26MGPx1iDCuygLOTGv_Z5l6gagJd_NASvwKii2vBd-Jiq9W1aC0NYf7rFqufNYErX_pdZ5Ht8k8kLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=v3l6v5sSJFhmNINLhB4fnjyfiFGIENxQG6RzNo-VOcCDGt8-5lbjRMo-cTuVdruYm7ubIa1Tf33bWu2NqVp9zBnSRvQl3rztqzZCzcNqIi9S3gyuUzE7GGLp1rlt_u8ioCXkDlB4GxlJXBmNN6hMgCWxGjRp88Ipy1538KGkwJzrvlG6OHh6257cLFW9HlPEVVsdyObkOHfn-IPUpKOR2wUJd8X1ddqDaBK9IMK8wX-F-j5873PgAf3_f6qmiaxnNY1jSVEx26MGPx1iDCuygLOTGv_Z5l6gagJd_NASvwKii2vBd-Jiq9W1aC0NYf7rFqufNYErX_pdZ5Ht8k8kLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی (دوره سیزدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده  اکانت هوش مصنوعی مشخص شد:
👤
برنده عزیز با آیدی SattarBayat، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3066" target="_blank">📅 16:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axT24d94-v1QgYpOGaTZl7oL197tehUnXb3hQf6xFoTvsHcgLJXsohr5Z41Wu8ybBFSQj4-smw3P5yzGPhZdQtnuHWaHO6K5xdagv4DcYOml1SFFPdUK-IQBRfNCo07zDigdI_c5JDLj3mgmxd8TNG7yU93BASrc7fO6iygNiyzjYFwysyQvb8bbm6RI5VUXVn6baMVdGti1_B_fC_1zhzMNS_ZBx9qHk_0BwaRlWPE05K49zvBuHAVoYIyX-my1Hit9qXZfGMZ0EUCZBEX5a0RsR2f1QqXiMDLuufKyXie_YOzw0PxLQXkC0H7BqLHVl955vup9fk5TUAPEQcRplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نشت اطلاعاتی چیست و بعد از لو رفتن اطلاعات چه باید کرد؟
رخنه‌ی اطلاعاتی زمانی رخ می‌دهد که هکرها با نفوذ به سرورها و دیتابیس شرکت‌ها، داده‌های هویتی، تماس، رمزها و اطلاعات بانکی کاربران را سرقت یا در دارک‌وب منتشر می‌کنند.
⚙️
۵ اقدام فوری و حیاتی پس از افشای داده‌ها:
🔹
تغییر فوری پسوردها:
تغییر رمز حساب هدف و تمام سرویس‌هایی که رمز مشترک داشتند (با کمک Password Managerها).
🔸
فعال‌سازی تایید دومرحله‌ای (2FA):
فعال کردن کدسازهای معتبر مانند Google Authenticator روی ایمیل و تمام شبکه‌های اجتماعی.
🔹
امن‌سازی حساب‌های بانکی:
مسدود کردن آنی کارت مشکوک، تغییر پسورد اینترنت‌بانک و فعال نگه‌داشتن رمز پویا.
🔸
استعلام سیم‌کارت‌های به‌نام:
ارسال کد ملی به سرشماره
۳۰۰۰۱۵۰
یا سامانه
cra.ir
برای بررسی عدم ثبت سیم‌کارت مخفیانه با هویت شما.
🔹
هوشیاری در برابر فیشینگ ثانویه:
عدم کلیک روی پیامک‌ها یا ایمیل‌های مشکوک.
⚖️
در صورت بروز سوءاستفاده‌های قضایی یا مالی، فوراً از طریق مرکز فوریت‌های سایبری پلیس فتا (
cyberpolice.gov.ir
) موضوع را ثبت و پیگیری کنید.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3063" target="_blank">📅 20:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR3SNdBZ_o2MbKpNwH3PHYUTivGJgdgsntgN6HT2AXOldFvXwrckactgaqK23tL2KkdENTI2bCImiq0_HVF8uqHMMh-fp6mqTOjkB-J57OtMc5BufQzby98I6FGEu-DB3eZyhR4jxN-mwOJIVs4RK80X-3hn5HlOiR0ExbrpX9GIOalnXPG8x1lM_YoDK17JI4ClxQA7MOWA17kk7sO0mGPlAavmmwvyloxqYAvelS3WLQNMkKT8eWsQ7_2vqLWeEBsNMCkyQIMRDMKIlPij9aOVIq5FgyAzsCSBrnGDNaoyRj50oV2G7eor5cKJvzaLVz9PJm3aMiicgUKsfOCvcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎒
حرکت جالب WinRAR؛ فروش کیف به قیمت ۵ لایسنس نرم‌افزار!
شرکت
WinRAR
از یک کیف جذاب با طراحی آیکون نوستالژیک و معروف کتاب‌های خود به قیمت
۱۵۰ دلار
رونمایی کرد.
اکانت رسمی WinRAR در توییتر (X) با لحن طنز همیشگی‌اش نوشته:
«حالا که هیچ‌کدومتون پول لایسنس برنامه رو نمی‌دید، حداقل بیاید این کیف رو بخرید!»
😂
قیمت ۱۵۰ دلاری این کیف معادل خرید حدود ۵ لایسنس رسمی نرم‌افزار است و یک راه جالب برای حمایت از سازندگان این ابزار نوستالژیک به حساب می‌آید.
©️
Behrad Javed
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3057" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EobvPG1PAEhjeA6-QZBbRY1AQ1uOEeeMObt7alhm6ABr-BFfM-6Ynk1Vc0z7W3vDpTNg_IDjDn8CVcBKEjNQiRg2dDDvhoVe57v3erbcpuMcII8gl4De7kxDEC4gAVF4rkLYdg6Q9JMgW_lh-ixVaX9MEO7nK5Ady-mPgrLXuoeV_LUB7CHEFSs3g2Ro3cjnHjyT4oODcTgpvlTVVuobA8NupQ20tU3iXwY8PwT8DwmQSI-hlr6IIDc52qCiLsi9y_Mp-Fac4aSrdK_WfZOF08EeQydnX8xAQuRE0AkB_EvXb_CBmg2qfspEizAYF6t03MVCWLCeIrD8-_57Nnz8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
رئیس جدید گوگل دیپ‌مایند: جمینای 4 تقریباً برای عرضه آماده است!
پس از مدتی فاصله گرفتن از رقابت پرچمداران، گوگل در آستانه رونمایی از مدل قدرتمند و مورد انتظار
Gemini 4
قرار دارد. «کورای کاووک‌چوغلو» رهبر جدید بخش دیپ‌مایند گوگل اعلام کرد این مدل در مراحل پایانی ارزیابی قرار دارد و بسیار زودتر از پایان سال جاری میلادی عرضه خواهد شد.
🔹
عرضه زودهنگام نسخه پس‌آموزش:
کاووک‌چوغلو اعلام کرد با توجه به نتایج فوق‌العاده و هیجان‌انگیز تست‌ها، گوگل قصد دارد در اولین فرصت نسخه‌ای از فاز Post-training را منتشر کند و سرعت ارتقای مدل‌ها را بالا نگه دارد.
🔸
بازگشت به رقابت با GPT-6 و Mythos:
در حالی که رقبایی مثل OpenAI با معرفی مدل‌های سری GPT-6 و آنتروپیک با خانواده Mythos پیشتازی می‌کردند و عرضه وعده‌داده‌شده‌ی Gemini 3.5 Pro لغو شده بود، دیپ‌مایند هدف خود را مستقیماً روی جهش به نسل ۴ گذاشته است.
🔹
تغییر استراتژی فنی:
کاووک‌چوغلو علت تأخیر در عرضه پرچمدار را تمرکز موقت روی بهینه‌سازی مدل‌های سبک و سریع Flash دانست و تأکید کرد گوگل همچنان جایگاه خود در خط مقدم هوش مصنوعی را حفظ خواهد کرد.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3055" target="_blank">📅 16:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2f5JCAa7gevPzqgUW8Gbc9-RkdEmdVikmlj3B01pn2FFelhhGt1eO9dY5k5ls8uENMxYWYBKpbfjNLXq4-yN7E-A4Nc1FCsjL5G52_k7RvMI3rFmd8ehZjsU0NgB-tn8SoI6EDS9Bx4ycnwQr60ymCfoWymMAoTbdAjqzR2njdBFINABtrKffz-nT7CcDOC2QfaGB5CBkOggXFl4IX6nLeNSfTjXNhW91jMOb7T841ExwykAugmX-pBotKCTL_S0G4URqCKw_Ev0KpihjGIe0csmemYoofUjU3DUhuRgLXPHEVrKvw-H5yKifl1vqv0P1tRDrWRrUnXBGlaEaFBoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گزارش رگولاتوری از ماجرای اتمام زودهنگام بسته‌ها
سازمان تنظیم مقررات پس از بررسی گلایه‌ها درباره پایان زودهنگام بسته‌های اینترنت، اعلام کرد اپراتورها تخلفی نداشته و ضرایب مصرف را رعایت می‌کنند.
⚙️
دلایل اعلام‌شده برای اتمام سریع بسته‌ها:
🔹
کیفیت ویدیوها و فرآیندهای پس‌زمینه:
افزایش حجم محتواهای ویدیویی، آپدیت خودکار نرم‌افزارها، بکاپ‌های ابری و فعالیت برنامه‌ها در پس‌زمینه از دلایل اصلی جهش مصرف عنوان شده است.
🔹
شفاف‌سازی ریزمصرف:
رگولاتوری اعلام کرد عدم شفافیت برخی اپراتورها در تفکیک ترافیک داخلی و بین‌الملل پیگیری و اصلاح شده تا مشترکان دقیق‌تر مصرف خود را ببینند.//شبکه‌چی
💬
خلاصه اینکه اگه قبلاً بسته ۱۰ گیگی یک ماه براتون کار می‌کرد و الان یک هفته‌ای تموم میشه، مشکل از سیستم نیست؛ مصرفتون یهویی رفته بالا و شما حواستون نیست!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrwtMsECARY1iNXlOIay5MZnGIfxBSdsiw0J2cPvPHR6uDJjZiYcQc9aV3A0gCCW5iPye2HEoM8xc4LXbUvaoo_tSn67snFy1IqN2YNwZ44hyQHJF4SxTZZHA1dmhdWWwd3scUjpfI-zxFsw9YnyYAIspf9eNQ-wJijA3GbYoEwPE0bBjAYacVrybUbxegL8eDcQKA448qAOdBrMSlrvSLvUsWfs7KnpMakqyLhvlHn2n7iuuyz_t4z0eg4SLlxUrXNz00isK6bLGXeFa1jVM2PAdkBTn5EJF2WEqc6xFv4rZI9GLmtvBoSuPXtjQz4F5QggwfJd6TjzFcgavaR0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی بدون تانل + پنل مدیریت (مشابه شکن)
🔹
خیلی وقت‌ها برای دور زدن تحریم‌های اینترنتی (سایت‌های برنامه‌نویسی، بازی‌ها، صرافی‌ها و...) نیازی به درگیری با تانل‌های پیچیده نیست. تو این ویدیو بهتون آموزش میدم چطوری یک تحریم‌شکن شخصی قدرتمند (مشابه سرویس شکن) بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MexfpIyGz3egBN-PSccSnXFj0E2-gE0WhBaJ5Huv9MHnwjgnMzUzTRyHntUEYR8L0_QHGP8eRE0zo3NsFIQbKXsExfExS-yI1Q1HtgbCDioTYgNwjeLlvcmiK_OB6FipymXoo0bhoCJxtV28MysD03BCVI-dE4xqUGOf1MjukQsvLxzeeUeTT5D2VU_xTlSu1o8fq7F8yooOB_ENnQp2GPUc7jDZYVfyfYfbV2ZKXZ9eaVJtL9AsaS1q9_Z3fP_PwXlnEVOdW1ihCHhjKSq7SV64wUj9ER-SkyrJr7giZW9mej4dvl1uW2jNvif9VmkYt-_HP7rLoacN1FPe-BJ6LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GPT-6 Sol و GPT-6 Luna؛ مدل‌های جدید اوپن‌ای‌آی با نصف قیمت!
اوپن‌ای‌آی دو مدل جدید
GPT-6 Sol
و
GPT-6 Luna
را با تمرکز بر سرعت بالاتر، خطای کمتر و
۵۰٪ کاهش هزینه API
معرفی کرد.
🔹
هزینه بسیار پایین‌تر:
ورودی Sol به ۲ دلار و Luna به ۰.۱۰ دلار به ازای هر میلیون توکن رسیده است.
🔹
عملکرد قدرتمند:
در بنچمارک‌های برنامه‌نویسی و اتوماسیون (نظیر AutomationBench و DeepSWE)، مدل Sol رقبا مثل Claude Opus 5 را با کسری از هزینه شکست داده است.
🔹
کاهش ۵۰ درصدی خطاها:
دقت اطلاعاتی مدل به سطح GPT-6 Astra نزدیک شده و پاسخ‌ها در کارهای فنی شفاف‌تر و کوتاه‌تر شده‌اند.
🔹
دسترسی:
فعال در API با شناسه‌های
gpt-6-sol
و
gpt-6-luna
، ابزار Codex و به‌صورت تدریجی در ChatGPT Work و دسکتاپ.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3048" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=iPgZ7tCyH9KHmzyevUvbgfw2D0IfdmstszUXJG97y4vAcu3QpBE72h-QOi1D4mH_vIg_KS275ET3TzmBHt12ASBVC9-1NEHbzhywB6VzwJIE4KjHNR2GyV2Q07pTzTcddYk149WdMlkep93T2bIq3pPYWMh5B_2OlybY5cyNYNhe-V7d6AuG7ZhHozpDFke3pCYwJPOk0W8dAV29eomH9atllclwKoDNatvI8ld3mAFBd9WwWoh6N1A24JIW19jgvf2-KTflYQQp8SlKrQgxiW63l9Eflib7QaKi54TgtFoHLcQ5KCbTj-Ce2IYXJ5BbO_gamWXLyyhDvY0qmsdgCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=iPgZ7tCyH9KHmzyevUvbgfw2D0IfdmstszUXJG97y4vAcu3QpBE72h-QOi1D4mH_vIg_KS275ET3TzmBHt12ASBVC9-1NEHbzhywB6VzwJIE4KjHNR2GyV2Q07pTzTcddYk149WdMlkep93T2bIq3pPYWMh5B_2OlybY5cyNYNhe-V7d6AuG7ZhHozpDFke3pCYwJPOk0W8dAV29eomH9atllclwKoDNatvI8ld3mAFBd9WwWoh6N1A24JIW19jgvf2-KTflYQQp8SlKrQgxiW63l9Eflib7QaKi54TgtFoHLcQ5KCbTj-Ce2IYXJ5BbO_gamWXLyyhDvY0qmsdgCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی 18 ماهه (دوره دوازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی 18 ماهه مشخص شد:
👤
برنده عزیز با آیدی matintarafdar4000، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3045" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESZXrrmMdbLi2maN97ijYwPQKjX6BdW1R9m2Iw1Xr-5RrW2DsRUcn_L4oUhsB1yIteIK2KKad_6C-N9uxsxTEgwvNh8bNZzk27giiMcmUcDkcZg9RNz7VLMv_WF6wRZ6u3OMWIJQAKDufcQbEdBGO82ylNNr2XzTzUxWizvb2h7laSlJfKY9uFKda6YJJc92eh5GrXPVSMaiXD3dhFKTTkRPgo4mkoj4pRjp99IaJFyUs1RRKLi_dTfdTT1a0ah39dg7cx6rI3yHP9HKsoFPW5LbkXSAfya5CDwXPv3qu5z5nXE6u7Ev3iV5EMQVBrLoz-iwh7ReNwMtgU3mHKSEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل DeepSeek V4 Flash در OpenRouter رایگان شد!
نسخه
DeepSeek V4 Flash
بدون محدودیت سخت‌گیرانه (Rate-limit) روی پلتفرم OpenRouter به‌صورت رایگان در دسترس قرار گرفت.
🔹
سرعت فوق‌العاده بالا به لطف معماری بهینه MoE
🔹
کانتکست عظیم (بیش از ۱ میلیون توکن) مناسب تحلیل اسناد و کدهای حجیم
🔹
اتصال آسان از طریق API به افزونه‌های هوش مصنوعی در VS Code و ابزارهای مختلف
🔗
لینک دسترسی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3044" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No_fnVz3rqd-K6Wdp6qKvzdwJ9bS1eGknzZiJODqH7oTGTTJ-yM3irH_JaUJDpR7wlxZ6gXu07YUl8rcE9ONyj16vmVnBQzOk-PbeaCx9UQyt7XOrphCLbb63EwZiJ7ow1QUXX6t2TfGyNwtJ7xGufzXmzbiJawDq0My1g6PscDSuWrmmFa_0VAe2lh0-o9hTlIHfnMxrcEqfS8P4v1yDzoMD0J8OxsbnwBFYrq186MAzhNGqtR5q68jpTZO2h94mU8_8_-rb06O6IZbbvskBMqOZ-HpGJAHC5WYEVt0ZDdFNETpWLm2K4Sb3ZK2AiDU_coTC1wYa4VbUgIzF2pOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت اینترنت دیال‌آپ، صدای قیژوویژ مودم و استرس اینکه مبادا کسی تلفن خونه رو برداره قطع بشیم... و در نهایت رسیدن به این صفحه جادویی!
✨
نسل جدید هیچ‌وقت لذت و هیجان این لحظه‌ها رو تجربه نمی‌کنه:
• لرزوندن صفحه چت طرف با BUZZ وقتی جواب نمی‌داد
😂
• ساعت‌ها گشتن تو روم‌های ایرانی و چت با غریبه‌ها
💬
• تیک زدن گزینه
Sign in as invisible
برای اینکه مخفیانه بیای.
👀
• استاتوس‌های سنگین و خفنی که با کلی فسفر سوزوندن می‌نوشتیم!
تلگرام و دیسکورد هرچقدرم پیشرفته باشن، اون ضربان قلبی که موقع چرخیدن این آدمک طوسی و لاگین شدنش داشتیم، دیگه تو تاریخ اینترنت تکرار نمیشه.
😊
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3043" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMwv2vE1butG5fC0uid5d-c31WJ1wHVh8OgKRjrmv1i1kyO6SGj3IHNDBUU-797SWLm88jcl-AguS1CA3hbL6UqQknTDjiWQZL-oB0FO2yfSPZul2xmZPVpz3QjLGERjbqMF-HbIump85oJx1Nax5EnNVy2_Waf9ScTKpL2D7Bb13hjA7hzATzZsjB3XrXpEZw8rOJQWathi_QziFtdkX2EC5aX35dX5ZTIvE9FCJyqOXBR_sF1bf12lb8upuruHFH0hWzJ21rdK_nR3PanCS9M6lucRpF_FpaFvfhPzpGhR7sa6GfSMUu4NjjlDktrq1nT9eMdyHJzWva3qfOMVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار مهم امنیتی: انتشار آپدیت حیاتی سپتامبر ۲۰۲۶ برای اندروید ۱۴ تا ۱۷ با رفع ۱۸۰ آسیب‌پذیری
گوگل به‌روزرسانی امنیتی ماه سپتامبر ۲۰۲۶ را برای نسخه‌های
اندروید ۱۴ تا ۱۷
منتشر کرد. این بسته به دلیل تغییر سیاست گوگل به بولتن‌های فصلی و عدم انتشار جزئیات در ماه‌های جولای و آگوست، حجم بسیار بالایی دارد و
۱۸۰ حفره امنیتی
را ترمیم می‌کند که بیش از
۳۰ مورد از آن‌ها دارای سطح خطر «حیاتی» (Critical)
هستند.
⚙️
تفکیک پچ‌های امنیتی:
🔹
پچ اول (سطح سیستم و فریم‌ورک):
رفع
۹۵ باگ نرم‌افزاری
که شامل ۲۶ رخنه حیاتی در هسته سیستم و فریم‌ورک اندروید است؛ خطرناک‌ترین آن‌ها امکان
اجرای کد از راه دور (RCE)
بدون نیاز به تعامل کاربر را به مهاجم می‌داد.
🔹
پچ دوم (سخت‌افزار و تراشه‌ها):
ترمیم
۸۵ آسیب‌پذیری
مرتبط با چیپست‌ها و درایورهای سخت‌افزاری شرکت‌هایی نظیر کوالکام، مدیاتک و آرم.
⚠️
خطر حملات هدفمند علیه گوشی‌های پیکسل:
گوگل تأیید کرده که شواهدی مبنی بر سوءاستفاده‌های محدود و هدفمند هکرها از برخی از این آسیب‌پذیری‌ها روی دستگاه‌های پیکسل مشاهده شده است.//پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3042" target="_blank">📅 16:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Lfz7ZvZ3k3nyUaYi_J7s8QERPpzkSWBmxjLL-M5N50OfZd4iv8X6vRgKxAOwPYQk6PmnU-Sp2xDWaObU9Bu8HkHScxG8xoQC3MXNohIApWVjuoPhwadcqSf905Fag8XtMpoLNdbB1SKOewU1LBYTOX4TiV8r0L-75NwnnYTS6LDiGsB_1Tqs_UNl7QWdBljZlx4bA38Oot0Y7gEIOHwpfTnywQLg5jCuaUZh00Dby905Yo6TYCic8fNWmOAPJkgmV_dd-CMzTP3me-gAS5p8uTcbi0sTp_tB94En36dmo6Ud0nZp22v4xr5jcPqE603HBzjQbpP8ALG8oCs2sjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
آماده‌سازی اینترنت برای AI Agentها توسط کلادفلر
کلادفلر در حال ساخت زیرساختی است تا عامل‌های هوش مصنوعی (AI Agents) بتوانند پروژه‌های توسعه‌یافته روی
localhost
را بدون دخالت انسان تست و اجرا کنند.
⚙️
نحوه کار:
🔹
ساخت فوری URL:
با ابزار
TryCloudflare
، ایجینت بدون نیاز به دامنه یا لاگین، سرویس لوکال را به یک آدرس اینترنتی عمومی و موقت تبدیل می‌کند.
🔹
تست و بررسی با مرورگر:
ایجینت آدرس ساخته‌شده را با مرورگرهای هدلس کلادفلر (مثل Browser Rendering) باز می‌کند، المان‌ها را بررسی و خطاهای کنسول را می‌خواند.
🔹
دیباگ خودکار:
در صورت وجود باگ، ایجینت خطاها را تحلیل کرده و کد را در لحظه اصلاح می‌کند.
🔗
تست سریع ابزار
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/3040" target="_blank">📅 20:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqVO0buODCd3_itwSLRgRnPFmLZpZzMqn4SRHIqtsj0DTFdxb2DaNf5JZDpSfZDUrVEyeKzPQY91mcjpEWeZGuvTNMjpcbEYualzY4Cr_ckGOObo4V6Cvsqei6yRPBXpRxhfBd_iuox190VbvdT4lArfyna5qz4bA9CyXDDv3SuDy2fGMtuufsopQua__ctCMuXRsTxxKmt0eN89DFjTUfOx0b1qfgWFTPnwfQwFsNP1HfMBafFdAPdnnu9xanaU8TOlGEzYg8HT9hWgIV0veu9rGUKjXFUNjwFKaSIqezDAJz6K04TocCXLInaRlX0oNTVhyx7h038_DyS84eCR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش افزایش سرعت بوت و بالا آمدن ویندوز
اجرای خودکار نرم‌افزارهای سنگین و انیمیشن‌های سیستمی از دلایل اصلی کندی بالا آمدن ویندوز هستند. با دو اقدام زیر زمان بوت سیستم را به حداقل برسانید:
⚡️
۱. غیرفعال‌سازی برنامه‌های استارتاپ (Startup):
— کلیدهای ترکیبی
Ctrl + Shift + Esc
را بزنید تا
Task Manager
باز شود.
— به تب
Startup apps
بروید.
— در ستون
Startup impact
به برنامه‌هایی با برچسب
High
دقت کنید (بیشترین مصرف منابع را دارند).
— روی برنامه‌های غیرضروری راست‌کلیک کرده و گزینه
Disable
را انتخاب کنید.
⚡️
۲. تنظیم سیستم روی بالاترین کارایی (Best Performance):
— وارد
Settings
شوید و به مسیر
System
⬅️
About
بروید.
— روی
Advanced system settings
کلیک کنید.
— در تب
Advanced
و بخش
Performance
، گزینه
Settings
را انتخاب کنید.
— تیک گزینه
Adjust for best performance
را بزنید و روی
OK
کلیک کنید تا افکت‌های گرافیکی سنگین غیرفعال شوند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3039" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADO59lC0wVzXU8LW1fhq6XYX9W7Oyza8Xqbf0RGXFZ6K7QhKKZd6ER8P2CH1Pxqzz7ymxb_KojSO2kuaByGnDim1rVglpfGYpIZRk2vysAKvZxRJR-W9o4Cs2f64w4Wtqqj9E-nSjypk0TAgzE0tvIKevhN29g3a06h5dHZm_sR1_7ElVTGj5IVC9d09M4Pa2jdt73kAYKe7zR5ZUyL19fbvVDidjFXM9kZZwSoRJstr1TlxqtySP6QGgzQj3MpSYD2Zk0w5mO0OB-hihkY7eiiG9V0LcVwy_u8HkzatHLQ-E-_UuqaTkAaWpkKhzA_V20J9E1znFqPCSiskbdqr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
هوش‌ مصنوعی Qwen و Kimi هم کاربران ایرانی را محدود کردند؟
دسترسی کاربران ایرانی به دو ابزار محبوب هوش مصنوعی چین، Qwen متعلق به علی‌بابا و Kimi ساخته‌ی Moonshot، با اختلال جدی مواجه شده است.
🔸
گزارش کاربران نشان می‌دهد دسترسی به نسخه وب و حتی API این سرویس‌ها در برخی موارد با خطاهایی مثل 403 Forbidden مواجه می‌شود؛ با این حال، هنوز هیچ‌کدام از این شرکت‌ها به‌طور رسمی درباره مسدودسازی کاربران ایرانی اطلاع‌رسانی نکرده‌اند.
🔹
هنوز مشخص نیست این محدودیت موقت و مرتبط با سیستم‌های امنیتی است یا آغاز یک محدودیت جغرافیایی دائمی.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3038" target="_blank">📅 14:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlFrMn2_rD-F00JFUFuvYTKkugewKwVze2qcsI22xw_BqkiE7NSYNUZR6hdhSS1GFbWSeN3CKKx04y6Q-rnT3rnOv6XVLJkssqetTvxfBM9aeKxTCSSHDovwp_SISvjjLcGHsPnc0sZM-YydTdRp5NZGYuoNxJ7AQCgNflFt-8q9Kh-W6HqGISKwdK9Ex-lolJFzyoMuVxofhUId2434mKj3HdX7MznpjHrh86M5XwLoTHZiAG4BiesznqZjP-e-KVrJmFs44jZs0BKXvCD1aoiF-WI2m39514riDHdeevWf5mmPKl9waVl8tpf2P2fuQU9E5gFa9WPJ323CVI3ryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
یک پنل، ۹ پروتکل فیلترشکن! با پشتیبانی همزمان
😍
🔹
در این آموزش، نحوه ساخت یک پنل حرفه‌ای با پشتیبانی همزمان از ۹ پروتکل و سرویس مختلف شامل OpenVPN، WireGuard، AmneziaWG، IKEv2، SoftEther، SSTP، L2TP، Cisco و Telegram Proxy رو یاد می‌گیری.
🔹
این پنل علاوه بر پشتیبانی از چندین پروتکل، قابلیت‌های متنوعی مثل نمایندگی، مدیریت حرفه‌ای کاربران و امکانات کاربردی دیگه رو هم در اختیارتون قرار می‌ده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو قرعه‌کشی اکانت هوش مصنوعی 18 ماهه داره،
برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/3036" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KemLP2V6MVkD-jXFkIMd3PYUPg9z887JRaRHh9qhUAJJS51JhFyDJXt_s3TrqlBRj8fBxglRVs0MHCeWsAn8Gaz-Il1-VX42VUwRGxOELkwQ4HYbe7TtUca8DUFP1VjTOabCvPGyCFp5UHBEREpGzRjpU12xl2t0-G1lykWMamxvAtUbM6xTqICaNj0-E7jFBFKjB9-_JQWvDIHzlR6nrUIHCS6ToKjHLCQhsoU0DHNIuMApM7G7MCBauDbQjMVpQpHER-vECZlAQ6KZMZ7jP5J8dA4VTpb2_ArO51OI95w7nI6f0j0yEed_ehFnl-embJQlf61dIXUgTSzzQvGXug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
حجم ویدیو و عکس‌هات رو راحت کم کن!
اگه برای ارسال یا ذخیره‌سازی فایل‌های حجیم ویدئویی و تصویری مشکل داری،
CompressO
می‌تونه یک گزینه کاربردی باشه.
🔹
یک ابزار
رایگان و متن‌باز
برای فشرده‌سازی ویدیو و تصویره که روی هر سه سیستم‌عامل
Windows، Linux و macOS
اجرا می‌شه.
🔹
پردازش فایل‌ها به‌صورت
کاملاً آفلاین
انجام می‌شه؛ بنابراین برای فشرده‌سازی نیازی نیست فایل‌هات رو روی سرور یا سایت خاصی آپلود کنی.
⚙️
این پروژه از ابزارهای قدرتمندی مثل
FFmpeg، pngquant و jpegoptim
برای کاهش حجم فایل‌ها استفاده می‌کنه.
🔗
مشاهده و دریافت پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشب روشن</strong></div>
<div class="tg-text">چشمان یک انسان دیگر باش... فقط با نصب یک اپلیکیشن رایگان!
👁️
❤️
.
تصور کن گوشیت زنگ می‌خوره؛ یه تماس تصویری ۱۰ ثانیه‌ای!
پشت خط، یک فرد نابینا است که فقط می‌خواد بدونه تاریخ انقضای این خوراکی چیه یا تابلوی جلوش چه آدرسی نوشته. تو توی چند ثانیه جواب می‌دی و استقلال و لبخند رو بهش هدیه می‌کنی!
✨
برنامه Be My Eyes داوطلب‌ها رو به افراد نابینا وصل می‌کنه تا کارهای روزمره‌شون رو راحت‌تر انجام بدن.
📌
چرا نصبش کنیم؟
🔹
کاملاً رایگان برای اندروید و iOS.
🔹
بدون تعهد زمانی (وقت نداشتین تماس رو رد می‌کنین).
🔹
حس فوق‌العاده با یک کمک ساده.
📲
دانلود:
نصب از گوگل پلی برای اندروید.
نصب از کافه بازار برای اندروید.
نصب از مایکت برای اندروید.
نصب از اپ استور برای آیفون.
📢
لطفاً این پست رو توی گروه‌ها و کانال‌های دیگه هم بفرستید.
شاید فوروارد شما باعث شه افراد بیشتری نصب کنن و گره از کار ده‌ها نفر باز بشه. مهربونی رو تکثیر کنیم!
🕊️
✨
.
@shaberoshanIR</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/3034" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS32H5-5JYQXDxfRq2z9IucxTtiBHbKjOg7zl8Rj5tje4W3xWCFxAeg-c8JDCi53GiHauuI5gEVZjrAfeiEblZdm8H8q90jQhLFThaCR9tRTpc0IN6RmzkoZpg9S468UutJ5qn7HejbNJPwes6K54K8vSQ2ZRJ2iCDo2AUl0MRLO9rgi-iUBvJIWWPlu66qoAOSrLcHoe6C4dQZ4CiP9J6c1rUGYy4iAZDWdFolSE8L46he4mbwfpKuV8uoTKAXcUoz0BwRlbHtoM_NEPVfKXmKPuKNJy9AAscxiy-lQB_S5Rn3uoIGH063spjsehYK2N-LlSxs2mAnR6wYJicqj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج جمنای از محیط آزمایشگاهی و نفوذ به ۳ شرکت واقعی!
گوگل اعلام کرد هوش مصنوعی Gemini در جریان تست‌های امنیت سایبری، به دلیل دسترسی ناخواسته به اینترنت، از محیط قرنطینه خارج شده و به زیرساخت ۳ شرکت واقعی نفوذ کرده است.
🔹
نقص در اتصال به وب:
دسترسی اینترنتی ناخواسته در محیط تست به مدل اجازه داد فراتر از آزمایشگاه عمل کند.
🔹
خطا در تفکیک هدف:
مدل قرار بود یک شرکت فرضی را تست کند، اما به دلیل تشابه نام، شرکت واقعی را هدف گرفت.
🔹
ورود با حدس پسورد:
جمنای با کشف و حدس گذرواژه‌ها وارد شبکه‌های این شرکت‌ها شد.
🔹
توقف خودکار:
مدل پس از تشخیص واقعی بودن محیط، عملیات را فوراً متوقف کرد و آسیبی به بار نیامد.
⚠️
باگ دسترسی اینترنتی در محیط‌های تست برطرف شده و به شرکت‌های هدف اطلاع داده شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWxbpPb7EtVIcCnqSQ3pDcWe7fduvHh8yrKfL-UBQr2zqyOxWo1JKSPH3r7HWnw38s0Sx9dZBeNeZSAWgc8kXEC_hQPqWnvIY7vDya82KN3Yqw2g6tCF9MLq7BoyKzTYKGhSOlsMP7TQmxytGlRA0jq7yHYazu_0mdVzrFfWIoEcyrRx8dSZEOhiU0zMB5Ye74laSifRTY5DWGrpYUbGwaf5hgQsKopEKnX17d-1X9NFuUEygP8lGWDw9KwFrvzo8dlgmOdl28QozQX0tmxxyDj04rnafD1_6gNP0B3DSeJmrIkt3v7POrFCqVhwPgo4ZMmVSrAGX340OFKmGsxX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
توقف ارائه خدمات میکروتیک به کاربران ایرانی؛ روترها از کار می‌افتند؟
شرکت میکروتیک (MikroTik) در پی اعمال مقررات تحریمی الزام‌آور اتحادیه اروپا، سازمان ملل و آمریکا، ارائه خدمات و پشتیبانی مستقیم به کاربران با IP ایران را متوقف کرد.
🔹
روترهای فعال از کار نمی‌افتند:
سیستم‌عامل RouterOS پس از فعال‌سازی، لایسنس را به‌صورت محلی روی دستگاه ذخیره می‌کند و عملکرد روزمره روتر وابسته به اتصال مداوم به سرورهای میکروتیک نیست.
🔸
چالش‌های حساب کاربری و لایسنس جدید:
در صورت تعلیق حساب‌های کاربران ایرانی، فرآیندهایی نظیر خرید لایسنس جدید، انتقال لایسنس به سخت‌افزار دیگر، بازیابی کلیدها و ثبت تیکت پشتیبانی رسمی مسدود خواهند شد.
🔹
ماشین‌های مجازی و سرویس‌های ابری CHR که نیازمند اعتبارسنجی مداوم لایسنس و تمدید هستند، بیش از روترهای سخت‌افزاری با ریسک و اختلال مواجه خواهند شد.
🔹
با پایان رسمی پشتیبانی از RouterOS نسخه ۶ در سپتامبر ۲۰۲۶ و عدم انتشار پچ‌های امنیتی جدید، مهاجرت به نسخه‌های جدیدتر برای سازمان‌ها با وجود محدودیت‌های جدید با چالش فنی و لایسنس همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=AQmpLkSokJVy7KO7QJAkvyCfze2_8M282eOBbYMRz5G9mfpCaAt5TkPb3QYR1D3VxAATSevzg4VKuPg3uTPGns4OEQN1q5HUocLc79NiDNqEWvXPcOkjTmtcA8l8GDHWL3gno3EQlCAG-uv1DSp8hyp5T1KseUi1aVB_XHYLtvoY9NSG3ShBRwDRdbOQwzebQhkfAeVl6Ct9ak6stzpyOgzGolOPkf0tENcAJfDDar8DE4mPicn7MwUNUhWHEFvy6cAlEosD_z4tqR2KN540lfvFW1aKpwC6sYMdQ4vUdjoxnq5U5rsNxiJexacHWHKURB8enVa6v4yTaCXMJZhGZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=AQmpLkSokJVy7KO7QJAkvyCfze2_8M282eOBbYMRz5G9mfpCaAt5TkPb3QYR1D3VxAATSevzg4VKuPg3uTPGns4OEQN1q5HUocLc79NiDNqEWvXPcOkjTmtcA8l8GDHWL3gno3EQlCAG-uv1DSp8hyp5T1KseUi1aVB_XHYLtvoY9NSG3ShBRwDRdbOQwzebQhkfAeVl6Ct9ak6stzpyOgzGolOPkf0tENcAJfDDar8DE4mPicn7MwUNUhWHEFvy6cAlEosD_z4tqR2KN540lfvFW1aKpwC6sYMdQ4vUdjoxnq5U5rsNxiJexacHWHKURB8enVa6v4yTaCXMJZhGZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
ورود مستقیم آنتروپیک به رقابت با آفیس و جمینای؛ معرفی قابلیت‌های Claude Docs و Claude Slides
شرکت آنتروپیک با رونمایی از دو قابلیت جدید متنی و ارائه‌محور، چت‌بات کلود را به ابزاری جامع برای محیط کار و رقابت مستقیم با پلتفرم‌هایی نظیر گوگل داکس و جمینای تبدیل کرد.
🔹
ابزارهای Docs و Slides (نسخه بتا):
کاربران اکنون می‌توانند مستقیماً درون محیط چت، اسناد متنی کامل و فایل‌های اسلاید ارائه ایجاد، ویرایش و دانلود کنند یا لینک اشتراکی آن‌ها را برای دیگران بفرستند.
🔸
همکاری تیمی هم‌زمان و ثبت کامنت:
همانند گوگل داکس، فایل‌ها قابلیت اشتراک‌گذاری، ویرایش گروهی به‌صورت زنده و ثبت بازخورد یا کامنت توسط همکاران و خود چت‌بات را دارند.
🔹
عرضه و دسترسی:
این قابلیت‌ها ابتدا برای مشترکان پلن‌های Pro و Max در وب، دسکتاپ و موبایل فعال شده و به‌مرور در اختیار کاربران رایگان و پلن‌های Team قرار خواهد گرفت.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1ropAnXAglqbVikLqb6CVii9eu3hBqWzprV8sfWiCrSItfFK_OEgHuMICucqBkwPaKRUvIJJxdEDZ6lv7654yxwxCx8Diyry732NzyjDbdHzj-5F0BEPa4ckzrx9AtAJKFID-0PPh5pyY3wsq53NIOshQinllmrLr4I3SItLQtbqQIx2bZmZAXrMCyi_QFydDUFTeFbGy0FrqLjdWNQXsI2B5PIh3l1P8v5CCuFTcmvNhYJTn2l2Fn6f-Hb1N-GHmXcYPePxuxGdVPbLU8tfIWZMTnEDer4jl2M-cIjcGNQ36queTZU45ictAwpktHnFPcHe9X_txb0KLk_vh141A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دانلود فایل ایزو ویندوز اورجینال از سرور‌های مایکروسافت (با ۱ کلیک)
🔹
اگه از نصب ویندوزهای دستکاری شده و پر از باگ خسته شدید این ویدیو دقیقاً برای شماست. تو این آموزش، ۲ روش فوق‌العاده ساده و سریع رو بررسی می‌کنیم تا بتونید با ۱ کلیک، فایل ISO ویندوز اورجینال (ویندوز ۱۰ و ۱۱) رو از سرورهای خود مایکروسافت دانلود کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#ویندوز
#اورجینال
#windows
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8LnomVOqSsB0_tG0BxIX2BKo9rmTVuUsM31ji9SH8zayUX7LKvDc_eGry0voyavcne1tZG_pZauYqjIL5ORnmJ5gz_saH3HvY95T1q_smFtvPD8n-WS3COGygdjoTHx3pK1AGviTWeXh8Pya15yqPiXdNWFcjjc9JddbfGxvKk3M1V4m-dTI1lHtgoxznEbjrDcQ3voHEnQmXhF_xdxf6X-gsEdnoyVuISmeZQisyl_BI1G5M5wejgpQCdD2w75f1gYSAEfVNm9rm-37DR7ZrqJU4oIOQuo7jPfXeNnrSMYAZLpFbPYAyOY5efuc4icoc20IewPIizJGQeK7bccpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
کرکر سرسخت دنوو با وجود شکایت قضایی دست از کار نمی‌کشد!
با وجود فشارهای حقوقی و تلاش شرکت توسعه‌دهنده نرم‌افزار ضد دستکاری
Denuvo
برای شناسایی و توقف فعالیت کرکر ناشناس، او اعلام کرده به دور زدن قفل بازی‌های ویدیویی ادامه می‌دهد.
🔹
شکستن قفل‌های پیچیده:
قفل دنوو سال‌هاست به‌عنوان سرسخت‌ترین لایه حفاظتی بازی‌های ویدیویی شناخته می‌شود و دور زدن آن مهارت بالایی می‌طلبد.
🔸
شروع درگیری قضایی:
کرکری با نام مستعار
voices38
توانست پس از حدود یک ماه و نیم قفل بازی
Resident Evil Requiem
را بشکند؛ اقدامی که خشم دنوو را برانگیخت و باعث آغاز پیگیری‌های قانونی برای فاش‌کردن هویت واقعی او شد.
🔹
پیام جسورانه در ردیت:
با وجود تشکیل پرونده قضایی و تلاش برای شناسایی او، این هکر با انتشار پیامی در ردیت به کاربران اطمینان داد: «همه‌چیز مرتب است و تمام کارها طبق روال عادی ادامه خواهد یافت.»
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oh1P-QhiIs2A2_H3u7lBoWJAMOOFtdQdDqhNQI8HmDu4NWlt2K7dx_wLplWocQYzkWQJuSoOTBbmIn4QkuhXyxKVWdNjL4vnuKrw1chvGeYCca10_xK-yIcAe-Fdj7TnKgrd5AD5Yf9WXl00nOhEaoHtwJSfqiLtIbbHw5JcSpCGZSUBf53qRr0Opkh9XkHz-EwMQejIDhcnc2Z_-xC3k4pdInl9sjmeGOh5wgtK_NVYn1M4uZF8jr9uyjtJtnvTNXG7lWaY6EVuqKDmuOoh8Rmy8qCANKnkaJAgx3b9wa74A7NbJzolSVo0-JBrHkxSk5xNQXMpBXgpjpKZUia8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Screenbox؛ پلیر مدرن، سبک و جایگزین شیک VLC برای ویندوز
اگر پلیر پیش‌فرض ویندوز نیازهایتان را برطرف نمی‌کند و از طرف دیگر ظاهر قدیمی، شلوغ و منوهای تو در توی VLC کلافتان کرده، برنامه متن‌باز
Screenbox
دقیقاً همان گزینه‌ای است که دنبالش هستید؛ پلیری با موتور پخش قدرتمند VLC اما با رابط کاربری کاملاً مدرن و هماهنگ با طراحی ویندوز ۱۱.
🔹
موتور پخش قدرتمند LibVLCSharp:
اجرای روان تمام فرمت‌های صوتی و تصویری رایج، پشتیبانی دقیق از انواع زیرنویس‌ها و هماهنگی کامل با موتور اصلی VLC.
🔸
طراحی بومی و مینیمال ویندوز ۱۱:
رابط کاربری مدرن، شفاف و چشم‌نواز بدون گزینه‌های اضافی و سردرگم‌کننده.
🔹
بهبود کیفیت تصویر (Upscaling):
قابلیت ارتقاء وضوح ویدیوها در محیطی با تنظیمات ساده، سرراست و قابل‌فهم.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9UWKZ5pAbJF2VPDbin8YNr0AZn3kPeOno1Rg6oE1TPg4z-K5TD0JYJqOPCvZFhhFGR-HFIDiAg6rMCZ9sf6-4JoPEuFB1xKMbuAsPrk_quhdtGXv7ZX36QZLxr8R92KlAOZrCnm3nSvXfD_rTtbkdi00MoPW9XfNgYo4LqlS-kEMt2LCwl5ZXQp55TzESCLxIJLaHZTd3bYuLiNH9IAaRUQetTec1K20Y-PB3EuOHQw4VUpqzRaKA-WP2gXS5U9Erj1tMIpb6wYw4qpiZaw3Mn-gfer3adTiNP18EmXdRXWSt5vF-GcCFQxNlZnEke4FIbYFwAKp3TFrPxRUezowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام تعطیلی رسمی صرافی کوینکس (CoinEx) پس از ۹ سال
صرافی شناخته‌شده
کوینکس (CoinEx)
که از سال ۲۰۱۷ فعال بود و به‌دلیل عدم اجبار احراز هویت (KYC) در سال‌های گذشته یکی از اصلی‌ترین مقاصد کاربران ایرانی به‌شمار می‌رفت، رسماً اعلام کرد که فعالیت خود را متوقف کرده و تا
۱ دی ۱۴۰۵ (۲۲ دسامبر ۲۰۲۶)
به‌طور کامل بسته خواهد شد.
⚙️
زمان‌بندی مراحل تعطیلی صرافی:
🔹
۲۴ شهریور (۱۵ سپتامبر):
توقف ثبت‌نام کاربران جدید و انتقال بخش معاملات فیوچرز به حالت Reduce-Only (فقط بستن پوزیشن‌ها).
🔸
۳۱ شهریور (۲۲ سپتامبر):
توقف کامل معاملات فیوچرز، استیکینگ، وام‌دهی (Lending) و بخش واریز اکثر ارزها به صرافی.
🔹
۷ مهر (۲۹ سپتامبر):
توقف معاملات اسپات (Spot) و بازخرید توکن CET با نرخ ثابت ۰.۰۰۵ تتر.
⚠️
نکته بسیار مهم:
صرافی اعلام کرده رمزارزهای غیر از تتر را ترجیحاً تا قبل از ۷ مهر خارج کنید؛ پس از این تاریخ ممکن است دارایی‌های غیرتتری به تتر تبدیل شده یا رمزارزهای کم‌حجم پشتیبانی نشوند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUOophTSnYS11dxIn1uOBVCOmNYa-FXIkkeO_oGNn-2AbGcFd-zfhpAy1VXgKvPPDIrj0Pt2k-q1Kbsx85d5M3k4ZWSvvdTObvtwTtxANmfSNuVpQXYT3W_N7wAm2cwLyWz63JnE56SpwPu2QdOsUT0E7NzD7s_Qc-VqXMe_msqgvKdGbB2XBhm5X5NjlOhPueMgXPpkr3c8g7fLglPSrreF0arn3Dzqvjkppx88Cudi1vLdq_LmoCfCttE1eho8OTVgLj_W2rSiIPYeAMIDBiv6om2AbCPhQ2cUqm3i0nx7IEGK9YCSrJaOCuD7ZB258Q-UgM9PQn9b6lCnptscdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Subify؛ افزونه هوشمند ترجمه و دوبله زنده ویدیوها به فارسی
سرویس
Subify
یک ابزار کاربردی و مدرن برای مشاهده ویدیوها با زیرنویس دقیق فارسی و حتی دوبله صوتی هم‌زمان است که بدون نیاز به دانلود فایل جداگانه و با استفاده از API شخصی هوش مصنوعی کار می‌کند.
🔹
ترجمه آنی و بدون تاخیر:
استخراج مستقیم کپشن‌های زمان‌بندی‌شده یوتیوب و ترجمه پیش‌دستانه (Pre-fetch) با سینک زمانی میلی‌ثانیه‌ای بدون معطلی.
🔸
دوبله زنده صوتی
: دوبله هم‌زمان صدا بر بستر مدل‌های جمنای، با امکان تنظیم بلندی صدا، کاهش صدای اصلی ویدیو (Audio Ducking)، انتخاب گوینده و تنظیم سرعت.
🔹
پشتیبانی از مدل‌های AI متنوع:
اتصال به کلیدهای API شخصی در Google Gemini ،OpenRouter و OpenAI به‌همراه سیستم فال‌بک (Chunked) هنگام قطعی مسیر لایو.
🔸
شخصی‌سازی و فونت‌های فارسی:
تنظیم کامل فونت، سایز و استایل زیرنویس با فونت‌های جذاب وزیرمتن، استعداد و لاله‌زار به‌همراه پیش‌نمایش لحظه‌ای.
🔹
استخراج لغات کاربردی از دل ویدیو و امکان مرور کلمات به‌صورت فلش‌کارت در حافظه محلی مرورگر.
🔗
دانلود
افزونه برای انواع مرورگر
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVS-6b6ZxBH0taNgaEaNt2kvR-XnjY_Iaf6MkinE4qFDK0Jk3sZPw7ymUYlLf91_eoK4rzVXGBUUUh678o0k-uB83m8O3aT0-H_3q7_5PXQ2REciGmQ_gXSpLg3V86qJewUZd9JaPI15I2Ngf-7HoZOBLJUC7GCxSgvwmKDv-nlA5z5nSGipZ227rZB-9Au0urYL3nXb-RZHbwv2ydUdL3tICqgVmLALuXmVnNhw3NmQY76SyVaA16GmlM9BjFmMyrMTAPDEJ6W0-SP-nakb_dYbcvnHJZohLFOeMErAT_3AelL6Rd6ImevTSR8xHNooKAArwxPEVtRJGm_w9KCgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل سبک Zefira؛ مدیریت هم‌زمان چندین پروتکل
پنل
Zefira
یک ابزار پایتونی سریع و کم‌حجم (مبتنی بر FastAPI و SQLite) برای راه‌اندازی و مدیریت اکانت‌های VPN است که بدون درگیر شدن با Docker، امکان ارائه چندین پروتکل را در قالب یک لینک اشتراک واحد فراهم می‌کند.
🔸
پشتیبانی از پروتکل‌های اصلی:
پشتیبانی از VLESS (همراه با REALITY و چرخش خودکار SNI)، هسیتریا ۲، تروجان، VMess، شادوساکس، WireGuard و OpenVPN
🔹
لینک سابسکریپشن یکپارچه:
ارائه همه کانفیگ‌ها در یک لینک با خروجی‌های Base64 و فرمت Clash YAML
🔀
مدیریت تانل:
تسهیل ارتباط سرورهای ایران و خارج به‌همراه بررسی وضعیت اتصال نود ایران.
👥
کنترل دقیق اکانت‌ها:
تعیین حجم، تاریخ انقضا، لیمیت دستگاه، فعال‌سازی با اولین اتصال و تایید دو مرحله‌ای (2FA).
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=anlRdq19KyPj7Yiwh3h_RR2IKe-tRKflwMbSGvQQe4QexoJybtB6J81R7wZpgwsOEZRLiI9pPKrY9KmMdlqglnPT1Rfqkevr-yUubQRgSENk1c3zo5iK87qSKCpyvZN-jJOMzw_StdgpHuVsubi6-um6BuNZ5zH6OuGsXhDs_fF8kJkCqn6fXYMYhk066D_jjAn8Z7okvckAPqJXFQf_qv61sUWpBWf7ITJV5THocOikwzRIgHah-X38XVmBBbt5XfBF8CjSo0Nsudassi8UxHj5hCY_UMQ6-WrFqxk3iwaYOvWRHY0EKcSJcZXSRh-kbN5xsRHUcSaqSIF-EEuDSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=anlRdq19KyPj7Yiwh3h_RR2IKe-tRKflwMbSGvQQe4QexoJybtB6J81R7wZpgwsOEZRLiI9pPKrY9KmMdlqglnPT1Rfqkevr-yUubQRgSENk1c3zo5iK87qSKCpyvZN-jJOMzw_StdgpHuVsubi6-um6BuNZ5zH6OuGsXhDs_fF8kJkCqn6fXYMYhk066D_jjAn8Z7okvckAPqJXFQf_qv61sUWpBWf7ITJV5THocOikwzRIgHah-X38XVmBBbt5XfBF8CjSo0Nsudassi8UxHj5hCY_UMQ6-WrFqxk3iwaYOvWRHY0EKcSJcZXSRh-kbN5xsRHUcSaqSIF-EEuDSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی (دوره یازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mahdi9226، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oijigwboBsuSzIDP1IUZqDcOHB5K8x23ELEOlX5wqBISvhJ54ydXxIMlLYl-qzyZSBERbDadMwAo94_xPNRDsRwkMfki_FYXpJ7ipoZkSWqv6ljfWvW3KaCfrEQDVUN-rWGwvZWVojmD4dWaVgyyz_CIy2yZtkSaUWJ29XobtrhxGxzGg56gwYx1wsHViqLMcZRj4joctWBNpG0IWvfUm_5V74_Jh2gXj8jhtIuSJLbe-avC98S_JVy9Zv_9sB0bpX-D7jt7h3Ac_uvZ5692Ad1Wcnv99lvKwM4h56_oufgLIh8GQfUatEZZLBzr2l363jYbjaDE8q8pcmnDFOg5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی DNS Changer؛ ابزار مدیریت و تغییر سریع DNS برای تمام پلتفرم‌ها
اگر برای گیمینگ، عبور از تحریم‌ها یا افزایش امنیت مدام در حال تغییر DNS هستید، برنامه
DNS Changer
یک ابزار رایگان و کراس‌پلتفرم است که این کار را با یک کلیک و بدون نیاز به دستکاری تنظیمات شبکه سیستم‌عامل انجام می‌دهد.
⚡️
پشتیبانی از بیش از ۳۰۰۰ سرور DNS:
دسترسی به دیتابیس عظیم ارائه‌دهندگان معتبر جهانی به‌همراه تست پینگ لحظه‌ای.
🛠
شخصی‌سازی کامل:
امکان افزودن، ذخیره و دسته‌بندی DNSهای اختصاصی برای استفاده مجدد.
🖥
پشتیبانی از همه سیستم‌عامل‌ها:
دارای نسخه اختصاصی برای اندروید، ویندوز، لینوکس، مک و محیط خط فرمان.
🔗
دانلود برای پلتفرم‌های مختلف
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
نصب خودکار و یک‌کلیکی اسکریپت‌ها در پنل دوپراکس!
🔹
دوستان عزیز، همونطور که در ویدیوی آموزشی مشاهده می‌کنید، پنل دوپراکس (Doprax) یک قابلیت فوق‌العاده جذاب در بخش
مارکت
داره که کار شما رو برای راه‌اندازی سرویس‌ها بی‌نهایت ساده کرده!
🔸
دیگه نیازی به درگیری با کدهای پیچیده، ترمینال و تنظیمات طولانی نیست؛ فقط با چند تا کلیک ساده می‌تونید هر اسکریپتی که نیاز دارید (مثل پنل معروف 3x-ui) رو در کمترین زمان روی سرورتون نصب کنید.
📝
مراحل نصب خودکار:
1️⃣
ورود به مارکت:
از منوی پنل، وارد بخش مارکت (App Market) بشید.
2️⃣
انتخاب اسکریپت:
از بین برنامه‌های موجود، اسکریپت دلخواهتون (مثلاً
3x-ui
) رو انتخاب کنید.
3️⃣
انتخاب سرور:
سروری که از قبل تو پنل ساختید و آماده کردید رو به عنوان مقصد مشخص کنید.
4️⃣
نصب با یک کلیک:
در نهایت فقط کافیه دکمه
Install
رو بزنید!
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کارهای لازم رو انجام میده و اسکریپت رو روی سرور شما نصب می‌کنه و اطلاعات ورود رو در اختیار شما قرار میده.
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkBHGHaxmA0DwhVazaZXrYCuRPy1opvulV61qGr8QrqYFn_M3cGLG8HBVE6jeds7V7qPb7mCZ4qa0sgX4LsHm7_5jJRcLKc87jJB375d70nnYPHhJXbhjX2mkpqsfcnWhGOyz4YfI6L-R-toOCtFiTrDM3sWUanh_eR1gy4WRqGr77tTHZIdiFxPEzGgcV4RA989o0WZv2XhCtYAAW_aQyzehO-kZ0MK-kbZEkWn_yd8ggYB2z_-ckP6o4iuIERPksT6xipSW3JCdqiEfECwUt2g4uQwZZ8PudV1BKFaTbeTxRqzeyWTVkauw5mT_rX-RiP40Nnu7YeRtkrSORkyuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل idontScanner | جعبه‌ابزار تست شبکه و TLS روی VPS
اگر مدیر سرور هستید یا می‌خواهید کیفیت اتصال، اختلالات شبکه و وضعیت پروتکل‌های امنیتی سرورتان را دقیق رصد کنید، پروژه متن‌باز
idontScanner
یک ابزار سبک، سلف‌هاستد و سریع برای همین کار است.
🔹
کالبدشکافی دقیق TLS & SNI:
تفکیک دقیق زمان‌های DNS ،TCP و TLS Handshake به‌همراه نمایش جزئیات گواهی SSL، نسخه پروتکل، Cipher و ALPN.
🔸
بررسی در دسترس بودن Endpoint برای لینک‌های VLESS ،VMess ،Trojan ،Shadowsocks ،Hysteria2 و WireGuard (بدون ذخیره افشای کلیدها و UUID).
🔹
سنجش لتنسی، جیتر و پاسخ‌دهی پلتفرم‌هایی مثل YouTube ،Instagram و Telegram مستقیماً از مبدا سرور.
🔸
دارای رابط کاربری روان به همراه منوی مدیریتی تحت ترمینال برای تغییر پورت، مشاهده لاگ‌ها، اتصال ربات تلگرام و آپدیت بدون از دست رفتن داده‌ها.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UamPq-lWbS21q4yFvD5Rr1lsaOtMdAChZLb7QfA9OIUtlRPGIzYlfSftMd4Weih_pxC4wxYkKOSF676Kdl7NQ0tIFyjDHROEwogdPOTAhWo0hzvD0MkMaXF6c8AZk5t2A7l3Qs3qKzTErJq2t8YSlN4Eb45u7Fgq7o-RfSs4xL2aFZqwZTBJvd43fWxr2cPiRHXQbikQ4gDxDGd6Kt-Rfkpdm2dYqUbbYpQLz1Sz2uTFeOU2pNKReXkAysdcIQp7yEv7uS-pwLU8EXniNmRWV8-Cce09uHlmFZkPiKP1nQf_ti_GpoWNnpDg5lnrqQ_cGa6Dc7HBL5BgIeQhlL4FPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اعتراف مدیرعامل زیرساخت: ۱۰ درصد ترافیک اینترنت کشور به استارلینک کوچ کرد؛ سهم 5G تقریباً صفر!
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، در نشست خبری خود از واقعیتی پرده برداشت که نشان‌دهنده شکست سیاست‌های محدودسازی اینترنت است: حدود ۱۰ درصد کل ترافیک کشور اکنون روی بستر اینترنت ماهواره‌ای استارلینک جابه‌جا می‌شود.
🔹
سهم ۱ ترابیت‌برثانیه‌ای استارلینک:
اکبری اعلام کرد با وجود بازگشت ۹۰ درصدی ترافیک، ۱۰ درصد باقی‌مانده دیگر به شبکه داخلی بازنگشته و جذب مسیرهای ماهواره‌ای غیررسمی شده است؛ حجمی که حتی از کل ترافیک برخی اپراتورهای داخلی فراتر است!
🔸
تداوم فعالیت ترمینال‌ها:
به گفته وی، استفاده از استارلینک به‌ویژه در دوران تنش‌ها و محدودیت‌ها جهش پیدا کرده و ترمینال‌های فعال‌شده همچنان آنلاین و در حال سرویس‌دهی باقی مانده‌اند.
🔹
سهم ۵G نزدیک به صفر:
در شرایطی که میانگین جهانی مصرف دیتا روی نسل پنجم به ۵۰ درصد رسیده، سهم ترافیک 5G در ایران تقریباً روی عدد صفر قفل شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPqtCJ7bliZulxWnSG_HS16i9fmJdTF3ZUR5y8eESett4ufYouY4C7coC-CL1vVEFZF2BF0dbEIIXjuZ6rUmH_ZSLHvePZ1l_6MazDafQ8UYFrYyWm9VtpQfOb6-sSr0o3lJoSmqrpr96qF3_Wvh28Xt7t_P4FAlz2XMH3lNIeDqNGyezzL45PEWFaR9YfqeEWoZT50h1bk1r-dqLY92vXo_3hJCXDpfKpYTdb8a313QHZQGfv-MkKxqF5K8AyUlbDHQFXbUHiXixBlpm0v0UDiES95mZhZEQxrrXYenwJEIzKzoZ5C5Tp1Yu2p1HqdKS5I5ZhFcDvJ7qsOSMjx2Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های ترافیک IPv6 در کشور
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، پس از تذکر اخیر وزیر ارتباطات اعلام کرد که محدودیت‌های اعمال‌شده روی پروتکل
IPv6
برداشته شده و اپراتورها از امروز هیچ منعی برای استفاده از آن ندارند.
⚙️
جزئیات و نکات کلیدی خبر:
🔹
۹ ماه مسدودسازی بی‌دلیل:
ترافیک IPv6 که نقش مستقیمی در کاهش تاخیر (Latency)، پایداری شبکه و افزایش سرعت ارتباطات دارد، از دی‌ماه ۱۴۰۴ تا امروز دچار مسدودسازی و اختلال گسترده بود؛ محدودیتی که حتی خود وزارت ارتباطات هم مدعی است مصوبه قانونی مشخصی برای آن وجود نداشته است!
🔸
وضعیت ترافیک در کلودفلر رادار:
با وجود اعلام رسمی شرکت زیرساخت، داده‌های لحظه‌ای
Cloudflare Radar
هنوز تغییر محسوسی نشان نمی‌دهد و سهم ترافیک IPv6 ایران همچنان روی رقم ناچیز ۷ الی ۸ درصد ثابت مانده است. انتظار می‌رود در روزهای آینده با بازگشایی شبکه اپراتورها این سهم افزایش یابد.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzsSyxYWuKWMIcICywMr2ZiNxzKybQy9nJvCnK59oOD7F25OL7_id0qTF8xTn22SBudlWrENHkBwqaPS_bZ1sSNs6_HeMMZyIx3yqP2H-uNzhbGmeo7F91zamqAGxgoskVH-5GG9HBhKTaLxtJKQc8Zeb3WEYhPTCk8rZQcDH4Mq4aP0iRMj6TPZJTupUtgBi3CCRUGSaZa29Fx0qMWf5mUGTQ5DhxtlEtbvqD05l5Ufqi_Z0LaNlugPQcH8-kSmZGCbQnfPvGSwk19arhjT9uWOOSiOugW_9uN0q8MRrI47LfsCr9LtfWu7qyKF__vOfgsqrHjp3lU8WV_8tOcUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی + پنل مدیریت و فروش «مشابه شکن»
🔹
تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم چطور یک سرویس رفع تحریم اختصاصی (شبیه به سایت معروف شکن) بسازید و با استفاده از یک پنل مدیریت حرفه‌ای، کاربران رو کنترل کنید، اکانت بسازید و به راحتی فروش داشته باشید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">💬
راهنمای خرید سرور از هاستینگ هایی که معرفی میشه
رفقا سلام.
بعد از
هم‌فکری با شما
و بررسی نظرات خریدارها و فروشنده‌های عزیز، به یه جمع‌بندی نهایی رسیدیم. برای اینکه هیچ سوءتفاهمی پیش نیاد و همه چی کاملاً شفاف باشه، رعایت این موارد میتونه بسیار مفید باشه. این موارد قانون نیستن بلکه یک راهنما هستن برای اینکه شما با آگاهی کامل بتونید خرید کنید.
🔹
۱. ملاک قطعی سلامت آی‌پی:
تنها معیار سالم بودن سرور در زمان تحویل، موفق بودن تست پینگ و
باز بودن پورت SSH
از طریق سایت
Check Host
هستش، نه تست بین ده‌ها اپراتور کشور که هر کدوم فیلترینگ داخلی و محدودیت‌های خودشون رو دارن.
🔸
۲. داستان اپراتورها و فیلترینگ:
اگه سرور تو چک هاست اوکیه ولی روی نت شما (مثلاً ایرانسل) جواب نمیده یا بعد از چند روز آی‌پی مسدود میشه، این موضوع به خاطر فایروال‌ها هستش، نه خرابی سرورِ فروشنده.
🔹
۳. تعویض آی‌پی:
وقتی سرور با Check Host سالم تحویل داده شد، در صورت فیلتر شدن آی‌پی بعد از تحویلِ موفق (بعد از چند ساعت تا چند روز)، فروشنده تعهدی برای تعویض رایگان نداره و این ریسک در شرایط فعلی اینترنت پای خریداره.
🔸
۴. ارتباط سرور ایران به خارج:
سرورهای ایرانی که تهیه می‌کنید، باید ارتباط باز و بدون محدودیت با خارج (ترافیک بین‌الملل) داشته باشن.
🔹
۵. وضعیت پهنای باند و ترافیک:
فروشنده موظفه کاملاً شفاف بهتون اعلام کنه که پهنای باند سرور
«اختصاصی»
هستش یا
«اشتراکی»
. همچنین سقف دقیق مصرف منصفانه برای سرویس‌های اصطلاحاً "نامحدود" باید مشخص باشه.
🔸
۶. مرز پشتیبانی:
وظیفه هاستینگ تحویل سرور خامِ سالم با شبکه متصل هستش. نصب پنل، کانفیگ، ران کردن اسکریپت و رفع خطاهای نرم‌افزاری سمت سرور، به عهده خودتونه.
🟢
و اما یه نکته دوستانه و مهم:
— بچه‌ها، ما تو این کانال همیشه فیلترهای سخت‌گیرانه‌ای داشتیم و
فقط هاستینگ‌هایی رو معرفی می‌کنیم که دارای نماد اعتماد (اینماد) و سابقه مشخص هستن
. هدف ما ایجاد یه پل ارتباطی امن برای شماست. با این حال، وظیفه ما صرفاً «معرفی» هستش و صفر تا صد توافقات خرید و پشتیبانی، بین شما و فروشنده انجام میشه.
—
یادتون باشه هر هاستینگی ممکنه قوانین و شرایط فروش اختصاصی خودش رو داشته باشه که لزوماً صد در صد با موارد کلیِ بالا هم‌راستا نباشه.
پس حتماً قبل از نهایی کردن خرید، قوانین خود اون سایت رو مطالعه کنید و با آگاهی کامل خریدتون رو انجام بدید.
— چنانچه خدای نکرده مشکلی هم پیش اومد که نتونستید با فروشنده به توافق برسید، می‌تونید از طریق همون نماد اعتماد به صورت رسمی و قانونی شکایتتون رو ثبت و پیگیری کنید. این مسائل از دست و مسئولیت کانال ما خارجه.
🔻
امکان آپدیت در روزهای آینده وجود داره!
دمتون گرم که با آگاهی کامل خرید می‌کنید!
🌹</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABmIXSNiJNLAKT8JamZGbPiJ5bRx56CG-fM-RNhSPE420MFanBgzF9wUNjXokbdr2umDxmv5z0H6-0LQysdAHbJnXEuDfJYjVB6IknnEV8Lsz6TuHkyIbxbwEP2A32i9K8QuWNs937wBvw0N7cg9BIYIPG491s4c8zaHDcCSNfNkGwW6ZW0G3guGL6VQ8RCUVJP4vUArN_wGkINaL_ykmNfisaYc1Ik3yjSgg4rL2AptTVyv4pxc0MXb_U_nzQkj-bbnlH8TiYuaXKhFpYgNfOwxbKNlBEbvSXuP0Q55ObYWZNRPPDeALtOcj9iu0AnWiuRd0obsuSDrfqt_kWClDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی اوپن‌ای‌آی از ChatGPT Sites؛ طراحی و انتشار وب‌سایت تنها با پرامپت متنی
شرکت OpenAI قابلیت جدید
ChatGPT Sites
را به‌صورت بتای عمومی عرضه کرد؛ ابزاری که امکان تولید، ویرایش و میزبانی مستقیم وب‌سایت‌ها و وب‌اپلیکیشن‌های سبک را صرفاً بر اساس توضیحات متنی زبان طبیعی فراهم می‌کند.
💬
طراحی پرامپت‌محور (Sites@):
ساخت رابط‌های کاربری چندصفحه‌ای، داشبوردها، پورتال‌های درون‌سازمانی و ابزارهای تعاملی با ارسال متن، فایل‌ها و دیتاست‌ها
🚀
میزبانی و هاستینگ رایگان:
میزبانی خودکار وب‌سایت روی زیرساخت OpenAI، تولید لینک اختصاصی با قابلیت تعیین سطح دسترسی (خصوصی، سازمانی یا عمومی بدون نیاز به لاگین)
🧩
المان‌های تعاملی و شبه‌وب‌اپ:
پیاده‌سازی فرم‌ها، فیلترها، سیستم جست‌وجو، جداول داینامیک، نمودارها و سیستم احراز هویت اولیه
👥
همکاری تیمی (Collaboration):
امکان کار اشتراکی روی پروژه، اعمال تغییرات و به‌روزرسانی نسخه‌های منتشرشده با اعضای فضای کاری
📊
دسترسی:
دسترسی برای اکانت‌های Business، Enterprise، Pro، Pro Lite و Edu فعال شده و عرضه تدریجی آن برای کاربران پلن Plus نیز آغاز شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FenFz2sDGlpgMDe_eyMChFYgvnVcLYANM9DF0IiwmLBNWPv9XR4CkEk9-dAFjOzCxsyVp0uTG1L30c1KBmxQ0HmX4tAh5TZmiS4oRR7lkjl-pBPc7KFHqdfttQLISwgvyQg9zwNH57LSBKXYGRpPR3geydggti0hyrVDyv3lTR3SaZBdfxwCCl9s2Nrlm6j25vxaISo_7nZbtePF-3GQtxR_NbnUDpLQTW6X3tKb67jYWjsrBEUEZrwqp8-dNhfwhvuCTDfWMXcKjZSdrY94eUTmFtKdh98UpqQUpjdYJAs4l-jgqi21Vq9mEXl4zbukUoRtkvZj6q2P7WDcI_Pklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
بکاپ خودکار از پنل‌های V2Ray و تحویل مستقیم در تلگرام با ابزار bkup
ابزار
bkup
یک سرویس سبک برای سرور است که در فواصل زمانی مشخص از دیتابیس پنل‌ها فول‌بکاپ می‌گیرد و فایل خروجی را مستقیماً به تلگرام می‌فرستد.
🔄
پشتیبانی از ۴ پنل:
اتصال به پنل‌های 3x-ui، HM Panel، PasarGuard و Rebecca با دکمه تست آنلاین اتصال.
📤
تحویل خودکار در تلگرام:
ارسال مستقیم فایل بکاپ به چت یا کانال بدون نیاز به دانلود دستی از سرور.
⏱️
زمان‌بندی دقیق:
تعیین فاصله بکاپ‌گیری بر حسب ثانیه، اجرا در قالب سرویس Systemd و فعال ماندن پس از ری‌بوت سرور.
🧩
ابزار Reassemble:
قابلیت چسباندن پارت‌های چندتکه بکاپ‌های حجیم ارسالی تلگرام در پنل وب و ساخت فایل کامل
💻
مدیریت وب و ترمینال:
دارای داشبورد گرافیکی با لاگ زنده، به‌همراه منوی ترمینالی برای آپدیت، حذف و تغییر پورت یا پسورد.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=KvaWe1E16JVkPxsxsQjq9-cbKoWl5EU1MF6CLA_XML1VbzSALQsp2OX0gCAsLKSyLk9RSX5ISbd3OYdCrmjRK6S0tqZDL9gRoY1Il4IWtB2yJoEAI574mR36-a7VhgBnLJX8AOv8PWBx-EyrvD13KV5pOTAeTiC7LiyIsuN2V7e61VsJmD66FrFBJJyAlMP115BDl7xVYkd2t_9w7YYqvpvguDlwf6y6w3ByfxvSoL37qHhex8tHGnQbThmOpwv1ugg-au85Unk-VahECpvRiA7756HWmbgUjtLw6JFt7icio_dnLPT25RumZA1lAXlxq2Erw6ciPuAJCPtdpOaYhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=KvaWe1E16JVkPxsxsQjq9-cbKoWl5EU1MF6CLA_XML1VbzSALQsp2OX0gCAsLKSyLk9RSX5ISbd3OYdCrmjRK6S0tqZDL9gRoY1Il4IWtB2yJoEAI574mR36-a7VhgBnLJX8AOv8PWBx-EyrvD13KV5pOTAeTiC7LiyIsuN2V7e61VsJmD66FrFBJJyAlMP115BDl7xVYkd2t_9w7YYqvpvguDlwf6y6w3ByfxvSoL37qHhex8tHGnQbThmOpwv1ugg-au85Unk-VahECpvRiA7756HWmbgUjtLw6JFt7icio_dnLPT25RumZA1lAXlxq2Erw6ciPuAJCPtdpOaYhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی اوپن‌ای‌آی از ChatGPT Images 2.5؛ تبدیل اسکچ ساده به تصاویر واقع‌گرایانه
اوپن‌ای‌آی نسخه جدید مدل تولید تصویر خود را با نام
Images 2.5
معرفی کرد؛ مدلی با نورپردازی طبیعی‌تر، بافت‌های غنی‌تر و بهبود چشمگیر در وفاداری به تصاویر مرجع و ویرایش‌های متوالی.
⚙️
امکانات و ویژگی‌های جدید:
✏️
قابلیت Sketch@:
امکان رسم طرح اولیه و نقاشی ساده داخل محیط چت برای تبدیل مستقیم آن به تصویر پرجزئیات نهایی
⚡️
کاهش ۵۰ درصدی تاخیر:
سرعت تولید و بازبینی تصاویر دو برابر سریع‌تر از نسخه Images 2.0
🎯
ویرایش موضعی پایدار:
تغییر دقیق بخش‌های مدنظر (مانند متن تبلیغاتی، پس‌زمینه یا سوژه) بدون دست‌خوردن هویت اصلی یا افت کیفیت در مراحل بعدی
📁
قالب‌های آماده (Templates):
تسهیل ساخت پوسترهای تبلیغاتی، تراکت‌ها و عکس‌های صنعتی محصول
این مدل برای تمام کاربران در وب، موبایل و دسکتاپ فعال شده است. برای توسعه‌دهندگان نیز در دو نسخه ارائه می‌شود:
Flare
(پیش‌فرض، سریع و کم‌تاخیر) و
Sunburst
(مخصوص خروجی‌های بسیار دقیق و سنگین).//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfmdjr9lGa_NOLDKKi1aVV0T2rapzjBiTA8KyNaJBBdfs5PmbGbWGTgXcAXvLtT3sGtJyZOoT5qMAUgIKsY_0NVchcQmEfobThKLKclP6YaPOcW1AZVxUCf7UeVbTMa8ANELx91AL2e2zMuJCNnb0Ye4DocRGVz119URcg_kAcJxD4DJnhqV-VcxYMg-s9AYhypShuazToKPsGDAd0qdYl1WB9vUdWkg9CLbmSqw9Nhmu_paInutpjcKmHeKegGcyGxw4sxqdc4jsbTLCsrn70Nw4WsEnMneox6v_dK2wGesrGwUH6M_-Ydbu5ibXTLVMteCQe5wcidNjtJvOGMuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای نقشه ذهنی کلیدهای میانبر کامپیوتر با کلید کنترل
🔸
این تصویر یک نقشه ذهنی از کلیدهای میانبر عمومی کامپیوتر است که هسته اصلی آن، کلید کنترل (Ctrl)، قرار گرفته.
🔹
هر شاخه شامل لیست‌های دقیق از کلیدهای ترکیبی و عملکردهای مربوطه است که به راحتی قابل درک و یادگیری است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=OH12rezVBkexZaKtLsuIY5TQjfmRhh7PXcTqykIDIHbkpTqOLXc1h4uczknCqITBpDRljwgd9U3bXuwsgkpGtIo8Pw5_Y3EYrPj-X6N-nOHSBuXMVVCtX2462Kqo75nL9Z2Hg6nDQw0h-wQIFnyISFUy_J7ggYVyQcc0CFDVH64zdP3xuxsgO3a_yIUjw4gOogDBgjN3RrmaMvyaXAChIKg8vGu-IDQnk0p44LPNAvTwbsLdTur2_Gbjo8ipzsSWDwmEcZfyhiVWSUqN1QpiQQSm4BsUij5mYpFC5iqF0tSaF6Rbs_9npCiMLWrIGgo_eCYh88GcpyHoq7JoKNxspA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=OH12rezVBkexZaKtLsuIY5TQjfmRhh7PXcTqykIDIHbkpTqOLXc1h4uczknCqITBpDRljwgd9U3bXuwsgkpGtIo8Pw5_Y3EYrPj-X6N-nOHSBuXMVVCtX2462Kqo75nL9Z2Hg6nDQw0h-wQIFnyISFUy_J7ggYVyQcc0CFDVH64zdP3xuxsgO3a_yIUjw4gOogDBgjN3RrmaMvyaXAChIKg8vGu-IDQnk0p44LPNAvTwbsLdTur2_Gbjo8ipzsSWDwmEcZfyhiVWSUqN1QpiQQSm4BsUij5mYpFC5iqF0tSaF6Rbs_9npCiMLWrIGgo_eCYh88GcpyHoq7JoKNxspA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره دهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mmdoo-yt، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7DBVTI0aBWtB-DCdMikkZbGODyE-dZlyTnfjBZikqlybSUmp33EFg37LxIeU0LGOONK3MQi5Q_FO5GVJHAM6lbiIWQPcVtBF1LAurbH5bIg81xmtSm3g6JeCmvM1AVAnh3YhiozrK54o1mGTZdaqygNQviXFxQ7T1cAbn-dPecC8VpsGzYVfKUU0NDv-8q0u6DAh9NkobI0ziCLVZ8791JWMyEu56Na_YeBTEapRbVBtdW_oZmI_lKg_UVotxbQpVgF6gBu-GwDPYJ9ggfzOjR2NGKqz9dVAn88hzO3_Ah3ccwcmJ1HzjsGe9qDcn4XxbsI4cQXEOvaiFapkkor2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.12 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر بالا بیارید و با دوستان خودتون چت کنید.
👇🏻
تغییرات کلیدی سانگبرد (Songbird)
:
🐘
پشتیبانی از دیتابیس PostgreSQL
🪣
ذخیره‌سازی ابری روی آبجکت استوریج‌های سازگار با S3
📥
پشتیبانی کامل از استقرار به صورت PaaS یا CaaS (
دیپلوی آسان در Railway و Render
)
🎬
ورکر مستقل مدیا برای پردازش و تبدیل ویدیوها
📴
کارکرد چت در حالت آفلاین (صف‌بندی پیام‌ها و ارسال مجدد خودکار)
🛡
دسترسی اضطراری به پنل مدیریت
👥
عضویت خودکار کاربران جدید در چت‌های عمومی
📦
قابلیت Rollback (بازگشت به نسخه قبل) در اسکریپت نصب
👇🏻
بهبودها و رفع باگ‌ها:
🔸
استفاده از شناسه UUID برای کاربران، چت‌ها و پیام‌ها
🎨
بازطراحی رابط فهرست چت‌ها با تایپوگرافی بزرگ‌تر و ظاهر مدرن
🔧
ارتقای امنیت با رمزنگاری اختصاصی تامبنیل‌ها و فایل‌ها
🚪
رفع پرتاب کاربر به صفحه ورود در صورت قطعی موقت سرور یا اینترنت
🔗
داکیومنت پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkjFYmOU99HxXrdakJlrn1b2PrPEJ8iDMSyb1ZhM-HaEtz-A_W_RfNhoXMVgcmfD8g_3Wwcwr3OJ4ptd3_FH1l1JH5NlVc-L5B3vhtnSarxcNKwB67xzNMkbkUR4uE_eUdY4QRESkr3HmMfXKFOYfo-v7uxbj7yjGrx7HqZ-5PCB68Pg6E8Fjb7Z12fBj5wjWEVJWCRpIDBuGIuPvCxMfNxRCIWrYH06sGqQt6HGu6PIl0H1mkGVYHY-NbDB_oQHqIULV2H1fhM5Uw3nvbfMAzWvw5mik4gj5lUd4M4q_N0UrM_Yh8DiovVNmEbxJhGAoRG9tN37tYcMBDMbJvwvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازم داستان تکراری؛ اینترنت داغون، اما ادعاها برقرار!
🔹
از دیروز وضعیت اینترنت رسماً افتضاح شده؛ پکت‌لاس شدید، کندی اعصاب‌خردکن و قطعی‌های مداوم. بهزاد اکبری (مدیرعامل زیرساخت) هم طبق معمول اومده توییت زده که علت کندی «قطعی فیبر نوری در ارمنستان» بوده!
🔹
الانم ادعا می‌کنن مشکل حل شده، ولی در عمل کیفیت شبکه—مخصوصاً روی اینترنت موبایل—هنوزم افتضاحه و هیچ تغییری حس نمی‌شه.
✍🏻
جالبه که با یه قطعی سیم توی کشور همسایه کل اینترنت مملکت فلج می‌شه، ولی موقع افزایش قیمت بسته‌ها همه‌چیز سر جاشه و وزرا توی صف اول توجیه گرونی می‌ایستن! اول یه اینترنت پایدار و بدون قطعی تحویل بدید، بعد دم از گرون کردن تعرفه‌ها بزنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqpDGVIn7tr23VhXbSpMX9-u3-3QRExsy-Ss6R8xQxt27ZoFhZ6TLgdOLAE_IN9Ql2SQvsfYTZW-LO1iD0Aqc51cm301CQEkHgVDxSUssXgwqcGnVPInvWY20Z-f9fYcoDpbC8B30FF-q_cwKGNzqM_OaY9g-JzxOU4kIvka0Ml3rtG4iKca-jILiiJwZ1CV6tcLbPe1ysQJq8HMKFzNYpchSeHHT7z4h4_yu9RyRh0s5TpyN12fP8YkysoNTqoW9ITcdzFUkePBlRVigy8KB2OfhahW7vJqlqMfkNvOOBPBTyh83GMz5RvUltSXm7S6Dmvctvy0tL3FLZZWct5lQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
زنگ خطر امنیتی؛ لو رفتن دیتابیس حساس کاربران JumpJumpVPN
🔻
دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اگi از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns || ircfspace
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bklW2YCcqHSnN6Y5_6pgvgLat1GyqRm5BgoExve9ptGeI0fzXG02jEZBWjXEXn2C5gFCJA0PxJs4zsr2ebtLZEB5EPzTTcDH80-B2JMKO8yLLQAHxg2qnayRIY5BbBT65x1nk7TlF0AnM33rAlTMYIxWenEfyJ-oydtPoznTmtKJSrMIt4hgqr1CtV_0jYh0GFtwJHVdOrFymG6CnbUImzSLOjIdWBVfbHA2cv-7GorPoFgB9Zdym076ii8cTr96obpN8QDhdZd5hKyqcI58eHnQzLfScxWQUrFe4X7fTBTbj1DHidXG2vQk8Ki4PS02Sss1G4VRv--uBeq8uw1Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بروزرسانی جدید برای نسخه اندروید oblivion منتشر شد
🔹
فیلترشکن رایگان
oblivion
به صورت اوپن سورس و امن برای اندروید توسعه داده میشه و میتونید ازش استفاده کنید.
🔸
هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
🔗
دانلود از گیت هاب
#فیلترشکن
#oblivion
#رایگان
برای دور زدن فیلترینگ و آموزش کامپیوتر و تکنولوژی و... ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SoftEther Code -- @iAghapour.txt</div>
  <div class="tg-doc-extra">3 KB</div>
</div>
<a href="https://t.me/iaghapour/2983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QF5RHKw3JudptuVKKSDE5jZgDI18pJ4t9Q_AA8CtfRMknCtZ5kH3kPcpA3o1uOaASDXjLE5anIgJ2p3pXmEyddt8_94N1joQqi6C2HsUGlninMQwOFzqmTFYN6VaXENni9uvOjkf4xGpd50-_pp95Sp8lDSUNGTzmb69DPDLnEMWSk9XikG0nxKOQgGWrpzPQkbk8Rjf4zPG7WiPYPRN1LI_k7BPCZT2UO3-bIBXBcj234Oah4Grb2lU65xk_9tlD7wgt7brPYQN7j_XxZetIvIQgG_Aib0aaurOXcIisv0TZj5wBYFBpXr1rrCxHMuOzyIHjo696dSRhUmvth1EHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🚀
🔹
توی این ویدیو قدم‌به‌قدم بهتون یاد می‌دم چطور سرور SoftEther رو به همراه یک پنل تحت وب اختصاصی راه‌اندازی کنید. این پنل قابلیت‌های زیادی مثل مدیریت کاربران، اعمال محدودیت حجم و امکان استفاده از پروتکل‌های مختلف رو در اختیارتون قرار میده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#سافت_اتر
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-haI5dd4tKxBwpy1GCs-2WB6kLqRcZgwJYcAuFG3Y2k3V2f4P6pECwEVnU4MxaCp5dNi_Acg9GsWb0rcDh1pobexWjIrrSU-j--5NN0O3ECLyzTbixvJFHd0z2AzVlIso9FYxFEyz64vsrb40J4kZkWFEfkw4dIOrarzSEAB4W26Egron7Cfjb9fGO07YvLiT0R35hLA0oa_K129F54yPVGkFsRwL4o4QPuuTtkxkwlv-KA4zURUkqImNiRFguKgC_moSNFCee_hEuUjDVuH3kNAPsGBdVeRBhGFRUqCr1gUaUKzS6FCER66wAQtxGKYARDvZI5ka20-um_v43y2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی EMS IPAM؛ سامانه مدیریت آدرس‌های IP و تجهیزات شبکه
اگر برای مدیریت ساب‌نت‌ها، رادیوهای وایرلس و تجهیزات شعب مختلف هنوز از اکسل استفاده می‌کنید، ابزار
EMS IPAM
یک پنل متمرکز و گرافیکی برای سامان‌دهی و مستندسازی شبکه است.
🔹
مدیریت ساختاریافته IP:
پشتیبانی از رنج‌های /16 تا /32، جلوگیری خودکار از تداخل ساب‌نت‌ها و نمایش ظرفیت آزاد/مصرف‌شده.
🔸
مستندسازی شعب و تجهیزات:
ثبت موقعیت شعب، پورت‌ها، توپولوژی و ذخیره راه‌های دسترسی سریع (WinBox، SSH، RDP و وب).
🔹
پایش مستقیم میکروتیک:
اتصال به RouterOS از طریق API و نمایش زنده وضعیت اتصال، سیگنال و پهنای‌باند رادیوهای وایرلس.
🔸
کلاینت ویندوز:
باز کردن مستقیم نرم‌افزارهای مدیریتی (مانند WinBox) با یک کلیک از داخل پنل بدون درج رمز در مرورگر.
🔹
تعیین سطوح دسترسی، ایمپورت/اکسپورت ساب‌نت‌ها و پشتیبان‌گیری خودکار.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYOeDkhlDIT9F0ECmELYmh7pMwl1k64Lv_qG3mFsm5ApVnPGDx_mP25FzhdKEodZ6wl-TrD6hqyVuaVnQVpzbsjovEUwn9-Mpt0yQ1D87n7A99qzMp0f9iX_Dqi-dhgqZm5O_oukV5MEL8r9vEo8ZHcj0AbTOIZcU7mqa2Zmt_2TQZ9fUIsXlukH42sqK-lqqR-cRAkg8-YRUF7TN7re5QRgpEaGf4-9nJ_DNdIQPkmeS0zc2jktb_ESo_wpRyRg_mPrHbdaILlJ7_q4V2yrFApMPVvhy7p2EobNOaQzlmwdHbek4cyI_h8JAwqljRloDThga6eMdmsZfPETumaxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نرم‌افزارها در پس‌زمینه سیستم شما چه می‌کنند؟ کنترل کامل ترافیک با فایروال متن‌باز Portmaster
اگر زیاد اهل تست و نصب نرم‌افزارهای مختلف هستید یا نگرانید برنامه‌ها دور از چشم شما تله‌متری و اطلاعات به سرورهای ناشناس بفرستند، ابزار
Portmaster
دقیقاً همان لایه محافظتی مورد نیاز شماست.
⚙️
قابلیت‌های کاربردی و مهم:
🔹
دیده‌بانی زنده اتصالات:
نمایش شفاف و لحظه‌ای اینکه هر برنامه دقیقاً با چه IP، سرور، در چه ساعتی و از چه طریقی ارتباط برقرار کرده است.
🔹
مسدودسازی هوشمند ترافیک:
امکان بستن ترافیک‌های مشکوک، ردیاب‌ها (Trackers) یا تبلیغات به‌صورت موقت یا دائمی با یک کلیک.
🔹
ایزوله‌سازی آفلاین:
امکان قطع کامل دسترسی به اینترنت برای یک برنامه خاص تا صرفاً به‌شکل لوکال و آفلاین اجرا شود.
📥
دانلود از وب‌سایت رسمی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRtUXfa4Jjuidw6mB0sTKcXS8Ppxs7tVBI3Mnsg1ZZeMcUYp5ewapl7B7GnDed5cEKxfTX__FgpzVlXzt6Wq8BxfmzXmuvihR5Fj5xgIoIXH37rTEtfogFmGi-Zhl-Bx1Xhl0J4eEZulKLdtsD6iFHX9E988B8kbc0CGpYgdphObwkO_0j7J8uwH4SGrtUJasJ_zkYXwzDk0YatzaZn8bGmc9pxgg2ObR0O5tbQs3SQVlFHDWRvAMToPGGRDC2UZDS3Ct-8zmo10c7vlH-g98djWckmgTu1UVYMP0uBKes6VLEmY_-sdGs4v3r78mSw9dZKM8XvZp3ebvnYP0nM0Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی از «آیزا»؛ دومین آنتی‌ویروس بومی مبتنی بر شبکه ملی اطلاعات
دومین آنتی‌ویروس بومی کشور با نام
«آیزا» (Ayyza)
رونمایی شد؛ سامانه‌ای امنیتی که با تکیه بر هوش مصنوعی و ساختار شبکه ملی اطلاعات، امکان شناسایی تهدیدات و دریافت آپدیت‌ها را بدون وابستگی دائم به اینترنت بین‌الملل فراهم می‌کند.
🔹
موتور تشخیص هوش مصنوعی و سطح کرنل:
توسعه انجین اختصاصی مبتنی بر یادگیری ماشین و بهره‌گیری از فناوری‌های سطح هسته ویندوز (Kernel-level) جهت پایش دقیق‌تر، واکنش سریع‌تر و بهینه‌سازی مصرف رم و پردازنده.
🔹
عدم وابستگی به اینترنت جهانی:
قابلیت آپدیت به‌صورت آفلاین و انتقال داده‌ها و امضاهای امنیتی از طریق بستر شبکه ملی اطلاعات (اینترانت داخلی).
😁
🔹
اکوسیستم امنیتی یکپارچه:
ترکیب فناوری‌های EDR و XDR برای شناسایی حملات چندگامی و روز صفر، در کنار هماهنگی با سیستم‌های جلوگیری از نشت اطلاعات و مدیریت دسترسی‌های ویژه (PAM).
✍🏻
حواستون باشه قبل نصب با آنتی ویروس معتبر مثل کاسپر اسکن کنید آیزا رو :) تازه با اینترنت داخلی هم کار میکنه :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=Q0fjsiXP4X9oDK_Nfl8BpBNWh6607RFfC-TtqeP0h4WI1lzjW9aRUDKIfWOSQrJzGgwRsxNuya3BqhX9K9g0hfKIVOAYG7P-j9RgnMi430umEHF69KkoOeCcjdsPqDAOVemLyjQmtRSTESEiyfQuGUXT1zroTBLen-kxkBSS5-ByMFZSW1EJTgQ6A9KvgaNjN7XQAFiWUJ7Y6o6whjcjqMWjWBze-K6EnHiupz6r7KiMxgYMgvz8DkSmOfUgahoWpMWqpYe5rgdHnOinGN7HDm6PhjXfggjRVZIl99-e7gbj8iHfddROukBinHG0YjKD2uPia-fP6ob5AY4t6oPlSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=Q0fjsiXP4X9oDK_Nfl8BpBNWh6607RFfC-TtqeP0h4WI1lzjW9aRUDKIfWOSQrJzGgwRsxNuya3BqhX9K9g0hfKIVOAYG7P-j9RgnMi430umEHF69KkoOeCcjdsPqDAOVemLyjQmtRSTESEiyfQuGUXT1zroTBLen-kxkBSS5-ByMFZSW1EJTgQ6A9KvgaNjN7XQAFiWUJ7Y6o6whjcjqMWjWBze-K6EnHiupz6r7KiMxgYMgvz8DkSmOfUgahoWpMWqpYe5rgdHnOinGN7HDm6PhjXfggjRVZIl99-e7gbj8iHfddROukBinHG0YjKD2uPia-fP6ob5AY4t6oPlSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره هشتم و نهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
برنده عزیز با آیدی AhvanSalehi-f3r، مبارکتون باشه!
✨
👤
برنده عزیز با آیدی abolfazlghasemi1-q7t، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oijiTaJ4vlTxh3gObSsbKoCHbozDK-19y2HVcq4YQEAbkuTyB_2goup-CnFQ37VZvvd-9VCbp5XvztypgJIU0-ti9PpqlE2jIap6Im38_hTccyOvzzpro5pBNKuraYq5DLaYPJH0CI3O22tgvk3whcCUGUU70Hc__zmmR3ZrR7WD-l7C1RhfgdZK5oimeK1qYXG9GeYoTRI3RUylJmUROCUeAdEjctphpgGHtdQsccrzepXk25vyWRwfywh_LPTOoYcoT3M8ffPSbH8xxe8PWgDx7p2lyqXmtC0r4Q6v72ebNrKWuVLootGsRw3Fs7q_ACoNEtUPosTKXfmz82yHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
وقتی خودتونم توی پلتفرم داخلی دووم نیاوردید!
🔹
سال‌ها اینترنت رو بستن و با فیلترینگ شدید خواستن مردمو به‌زور بفرستن سمت پلتفرم‌های داخلی، کلی هم بودجه خرج کردن و هر روز گفتن حمایت از پیام‌رسان بومی!
🔸
حالا بعد از این‌همه وقت، ستاد فضای مجازی خودشون جلسه گذاشته و گفته ممنوعیت حضور ارگان‌های دولتی توی پیام‌رسان‌های خارجی رو برداشتم، اسمش رو هم گذاشتن «پایان یک خودتحریمی عجیب»!
🔻
جالب اینجاست که می‌گن: «برمی‌گردیم همون‌جایی که مردم هستند». خب اگه مردم اونجان و خودتونم فهمیدید بستن این پلتفرم‌ها جواب نمی‌ده، چرا باید برای ارگان‌های دولتی آزاد باشه و پیج بزنن، ولی همون مردم برای باز کردن یه اپلیکیشن عادی هر ماه پول فیلترشکن بدن و با قطعی سر و کله بزنن؟!
این یعنی همون یک‌بام‌ودوهوای همیشگی؛ خودشون توی اپ‌های داخلی دووم نیاوردن و برگشتن، ولی زحمت و تاوان فیلترینگش هنوز رو دوش مردمه.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.
گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به هر دلیلی آی‌پی روی یه اپراتور مثل ایرانسل دچار اختلال یا مسدودی میشه، پیام میده که «سرورتون خرابه، بیاید رایگان آی‌پی رو عوض کنید.
واقعیت اینه که این روال، نه از نظر فنی درسته و نه منطقی
.
🔹
تست اولیه حق شماست:
وقتی سروری رو تحویل می‌گیرید، همون ساعات اول کامل تستش کنید. اگه دیدید همون بدو تحویل روی اپراتور مدنظرتون پینگ نمیده یا دسترسی نداره، کاملاً حق دارید به پشتیبانی پیام بدید، درخواست بررسی کنید یا حتی طبق قوانین هاستینگ سرویس رو عودت بدید. این حق کاملاً منطقی و محفوظه.
🔸
تفاوت خرابی سرور با محدودیت اپراتور:
وقتی سرور روشن و سالمه و روی بقیه شبکه‌ها یا اینترنت جهانی کار می‌کنه، یعنی سیستم مشکلی نداره. مسدود شدن آی‌پی بعد از چند روز کارکرد، ناشی از حساسیت فایروال اپراتور روی ترافیک عبوریه، نه نقص فنی سرور.
🔻
ارزش منابع:
آدرس IPv4 منبع محدودی در کل دنیاست و هزینه جداگونه داره. هیچ مجموعه‌ای نمی‌تونه آی‌پی‌های سالمش رو به خاطر مسدود شدن‌های بعد از استفاده، پشت سر هم و رایگان بسوزونه و جایگزین کنه.
👈🏻
ریسک اختلال روی شبکه‌های مختلف توی این بستر وجود داره و همه ازش باخبریم. بهتره با آگاهی از این شرایط خرید کنیم، تست‌های لازم رو همون ابتدای کار انجام بدیم، و اگر بعد از چند روز استفاده آی‌پی دچار محدودیت شد، مسئولیت این ریسک رو به پای خرابی سرور یا کم‌کاری ارائه‌دهنده نذاریم.
🟢
در همین راستا و برای حفظ حقوق شما، از امروز تمام ارائه‌دهندگان سرور که در کانال ما تبلیغ می‌شن، ملزم هستند تا ۱۲ ساعت بعد از خرید، امکان عودت سرویس یا تعویض آی‌پی رو در صورت وجود مشکل برای کاربر فراهم کنن.
بنابراین حتماً به محض تحویل سرور، تست‌هاتون رو انجام بدید تا در صورت وجود هر مشکلی، بتونید توی این بازه از این ضمانت استفاده کنید.
// قوانین در حال بروزرسانی و قابل تغییر هستش.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWkur47hAQm7OTsbAPlZtJA51iwgxaV5xlbIwOc1jLfNDWzsvAS7LcWdWmBEaLGmxUd89RfUIPdVwmcNQTTk3-BqxYmtA8SADHQNvt7L02qs0p1MrPVeyq0wiWrhdAUHnctti-WJZZodHsnbOdOWNofoXKFVPClplmqyGyoJ6XiZIS2RudAmeXgVBKg3oXJSQVL6aQppJhAROJV13Ry6LQIx3vMxtwWTacBoHfBLtU24D93DnUoumNLnltBVZk6dBwnWD-iqi5-oGTn9mM-K_Jq2bRKNnj-jO8onTXTKVyWzqbtC1T_6KQCYp-Ac86ccqOCCLiE_HLSjz9z6O9XtFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
شکست قفل Denuvo بازی Mortal Kombat 1 و قدرت‌نمایی هکر Voices38
قفل امنیتی جنجالی
Denuvo
روی بازی پرطرفدار
Mortal Kombat 1
بالاخره پس از گذشت حدود سه سال توسط کرکر سرشناس موسوم به
Voices38
شکسته شد.
⚙️
چرا جامعه گیمینگ می‌گوید دنوو به سخره گرفته شده؟
🔹
طوفان کرک در ۲۴ ساعت:
هکر Voices38 نه‌تنها Mortal Kombat 1، بلکه در یک روز ۵ بازی سنگین و مجهز به دنوو از جمله
Persona 3 Reload
،
Star Wars Outlaws
،
Metal Gear Solid V: Complete
و
Prince of Persia: The Lost Crown
را کرک و منتشر کرد!
🔹
جانشین بی‌حاشیه دوران پس از EMPRESS:
برخلاف رفتارهای پرحاشیه و بیانیه‌های طولانی کرکرهای سابق، Voices38 صرفاً روی بایپس و حذف اجراییِ قفل در زمان کوتاه تمرکز کرده و عملاً انحصار دنوو را در سال جاری به چالش کشیده است.
🔹
آزادسازی منابع سیستم:
بازی‌های مجهز به قفل دنوو همواره به‌دلیل ایجاد لکنت، افزایش استهلاک پردازنده و افت فریم مورد انتقاد گیمرها بوده‌اند و حذف کامل این لایه محافظتی معمولاً به بهبود روانی اجرای بازی کمک می‌کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jar2zxyHoe3uCqWuw0jLoGK1vCcCztT1cVTPCZfYadQQr_14P0VDZ3QLAw6K-lx--545ZzppezyjRkm4kuhDkYhB8vuIEjGD1Rg8U3W28lt8X0VFScCjig-8n47T_wniWFq8SRuL7Ga0jcu7ENYOSB2jjARhnASfDv6Q5aGtbvdbjDpMrt0WyxZZ3MqgSXr3Yo0Lrz4QJUx1Si5mcFYf1txM9H7StSiYR4z_d3rdkBL2Clx9kkEgsmAJcrehUgyu-jTTV3VE_Rua3zDbM38madkcZ-We65jrICMFjaVM27CIgalG6DVr62uXqqYlxVpgn1AUbbiRGX8fbWOJH5Kggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بهترین پنل وایرگارد همراه با مدیریت حرفه‌ای کاربران + تانل
🚀
🔹
تو این آموزش بهتون یاد می‌دم چطور یک پنل جامع و سبک برای وایرگارد نصب کنید که هم امکان تعریف و مدیریت دقیق کاربران رو بهتون میده و هم قابلیت تانل زدن پایدار بین سرورها رو به ساده‌ترین شکل ممکن فراهم می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم قرعه‌کشی اکانت هوش مصنوعی داره و فقط تا فردا فرصت دارید! (شرایط: فقط قرار دادن کامنت زیر همین ویدیو).
👈🏻
قرعه‌کشی این ویدیو و ویدیوی قبلی با هم انجام می‌شه.
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayfDZoC1RZQsB8wU-Bemw28evaFfVcClLQiknSpeTSlDtubVVDasyoYkcpy-QPygFKAuEEUCA9YPKB7XRSNGafh7yImDaYNYTJd0yMCdGzWd3f4mXk6mMfHZnNdlMkKO-CzHg7-ZIHiJNUWBK6txfu7aRdZ7LgOznHCVSJCOap8u0JrCLIr8Z196xNZt46lttb4cUjKPmMobZUbfFAV3rEED1lKZq_Z9FZz0HXNNJsjOkKzIxnQvat5dNSrmyTvPXoRv2DknxvVhXI7CAF48Ql9MizrELQ64ripP8BV6j3ROoQAq6Zo9DGKP5AUJBXFK8oJuv0OJEN3JcwuJvGiPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مایکروسافت از Project Zenith رونمایی کرد؛ نسخه‌ای اختصاصی برای توسعه‌دهندگان
مایکروسافت پروژه جدیدی با نام
Project Zenith
معرفی کرد؛ نسخه‌ای بهینه‌سازی‌شده، مینیمال و «آماده کدنویسی» از ویندوز ۱۱ که بخش‌های اضافی و نرم‌افزارهای غیرضروری را حذف کرده و تجربه‌ای نزدیک به لینوکس برای برنامه‌نویسان فراهم می‌سازد.
🔹
تمرکز ویژه بر هوش مصنوعی محلی
:
امکان اجرای مدل‌های زبانی محلی با بیش از ۳۰ میلیارد پارامتر (+30B) بدون محدودیت و افت کارایی.
🔹
پیش‌نیاز سخت‌افزاری سنگین:
طراحی‌شده برای سیستم‌های قدرتمند توسعه با حداقل
۶۴ گیگابایت حافظه رم
و پهنای‌باند بسیار بالای حافظه؛ نخستین بار روی مینی‌دسکتاپ Ryzen AI Halo شرکت AMD عرضه می‌شود.
🔹
بهینه‌سازی محیط برای کدنویسی:
نصب پیش‌فرض محیط‌های اجرایی (Runtimes)، ابزارهای ضروری برنامه‌نویسی و اعمال تنظیمات پیش‌فرض مناسب توسعه‌دهندگان.
⚠️
با وجود استقبال برنامه‌نویسان از یک ویندوز خلوت و بهینه، محدود شدن این نسخه به سخت‌افزارهای گران‌قیمت ۶۴ گیگابایت رم در بحران فعلی بازار حافظه، دسترسی بخش زیادی از توسعه‌دهندگان مستقل را با چالش مواجه کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=Phcd_Vc2gqLhJeoJTH6SxAKd_-7RHV7gm_2wKWCPHGaN4oLsPQv631L2Mp5uA3fYOBNVdmaG52-RdHQiVlfmmuiKVIf9NU8blIbLPfkLhycAzlbFRJUrtCPeZi8wxL0KJJe2PLkOohqzAK0zwzd30_f-ZV_-Hv-AjZhZFPQK3ECvws0qSHkqoLzl4nfdZV8C1T2JkE6g71O8hw4JXXqxyn6vg6v8PAL2VSxxwDk9sUg01w0q8fUo3W0lt6NtWox0ZxxeQD9eNJ4p7hbzX7TZ0_JIEJNezSzXD9_sR2emLFj4IiBgPcuH7Hhd4ttz2_iSCvSDkbvfyLI-oYYbFC58zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=Phcd_Vc2gqLhJeoJTH6SxAKd_-7RHV7gm_2wKWCPHGaN4oLsPQv631L2Mp5uA3fYOBNVdmaG52-RdHQiVlfmmuiKVIf9NU8blIbLPfkLhycAzlbFRJUrtCPeZi8wxL0KJJe2PLkOohqzAK0zwzd30_f-ZV_-Hv-AjZhZFPQK3ECvws0qSHkqoLzl4nfdZV8C1T2JkE6g71O8hw4JXXqxyn6vg6v8PAL2VSxxwDk9sUg01w0q8fUo3W0lt6NtWox0ZxxeQD9eNJ4p7hbzX7TZ0_JIEJNezSzXD9_sR2emLFj4IiBgPcuH7Hhd4ttz2_iSCvSDkbvfyLI-oYYbFC58zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی مایکروسافت از MAI-Image-2.6-Flash؛ تولید ارزان و سریع تصویر
مایکروسافت نسخه سبک و کم‌هزینه مدل تولید تصویر خود را با نام
MAI-Image-2.6-Flash
از طریق پلتفرم Microsoft Foundry در دسترس توسعه‌دهندگان قرار داد.
⚙️
ویژگی‌های کلیدی:
🔹
سرعت بالا و صرفه اقتصادی:
۲.۸ برابر سریع‌تر از GPT-Image-2-Medium و با ۷۲ درصد کارایی بالاتر؛ ایده‌آل برای اتوماسیون و ابزارهای تعاملی پرمصرف.
🔹
ویرایش نقطه‌ای:
اصلاح دقیق اشیا، نوشته‌ها و چیدمان بدون تغییر در سایر بخش‌های تصویر.
🔹
ثبات کاراکتر و محصول:
امکان بارگذاری حداکثر ۵ تصویر مرجع برای حفظ یکپارچگی چهره و کالا در خروجی‌های مختلف.
🔹
اتصال به وب:
ارتباط مستقیم با موتور جستجوی بینگ برای رندر دقیق سوژه‌های واقعی.
💰
هزینه خروجی تصویری:
۱۹ دلار به‌ازای هر میلیون توکن (در برابر ۳۸ دلار برای نسخه پایه 2.6).
هر دو مدل هم‌اکنون در مرحله پیش‌نمایش عمومی در دسترس هستند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClnTR766HVBiLubIpPiQ8hnJ0NZxi4n_Ia7FRbAs9M2VdHRQmwAhw42IgWm5hCWm_GIxpcT-IvWGXiU9xJncACvq_BoZ6NaepviY5VpY8obBxQvF6iHbXv60dQyB4m24zwopk5fUwIkbVrwGvBeeOjIWZmxq8qfdjCgYD2-uhNWDDinrVBs6Mpcgdx5WSe5Xo6SFBJH6kf7hWA-x76TEgKGbuynU12ZEZHm25eF78nnQ2tHX8chWB0Q_B3b4xd3lAVKoxkJ-SKfeeT3xgUcAF5KU7TvNb080sg10GRvk8gWbudXwTQqByIOcTx-IPGsmVNXv92-RhZd9i4DlnZlHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل «زاگرس» (Zagros)؛ فورک چندهسته‌ای مرزبان
پروژه
Zagros
یک فورک از مرزبان است که محدودیت تک‌هسته‌ای را برطرف کرده و به شما امکان می‌دهد تمام هسته‌های معروف VPN را هم‌زمان روی یک سرور و نودهای مختلف مدیریت کنید.
⚙️
هسته‌های تحت پوشش:
🔹
هسته
Xray:
پروتکل‌های VLESS، VMess، Trojan و Shadowsocks
🔹
هسته
sing-box:
پروتکل‌های Hysteria2 و TUIC v5
🔹
سایر هسته‌ها:
WireGuard، OpenVPN، SoftEther، SSH Tunnel و PPTP
🚀
ویژگی‌های کلیدی:
🔹
اکانتینگ یکپارچه:
اعمال سهمیه حجم و محدودیت تعداد دستگاه متصل به‌صورت سراسری روی همه هسته‌ها و نودها
🔹
کلاستر نودها:
اتصال امن نودها با تایید Fingerprint و مدیریت هسته‌های مجزا برای هر نود
🔗
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🧠
رونمایی اوپن‌ای‌آی از پرچمدار GPT-6 Astra؛ ادعای ورود رسمی به «عصر AGI» و انقلاب در کار با کامپیوتر
اوپن‌ای‌آی با رونمایی رسمی از مدل پرچمدار
GPT-6 Astra
، آن را جهشی نسلی در حوزه‌های امنیت سایبری، برنامه‌نویسی و تعامل مستقل با سیستم‌ها نامید؛ تا جایی که گرگ براکمن صراحتاً اعلام کرد:
«به عصر AGI خوش آمدید»
.
⚙️
ویژگی‌ها و قابلیت‌های محوری GPT-6 Astra:
🔹
توانایی عامل‌محور و کار با کامپیوتر:
این مدل بدون نیاز به رابط‌ها و APIهای پیچیده، مانند یک کاربر انسانی با موس، کیبورد و صفحه تصویر کار می‌کند؛ فرم‌ها را پر می‌کند، رکوردهای CRM را تغییر می‌دهد، نرم‌افزارهای مهندسی (KiCad/FreeCAD) را اجرا کرده و کدبیس‌های پیچیده را مدیریت می‌کند.
🔹
سرعت و بنچمارک‌های خیره‌کننده:
🔸
در تست OSWorld 2.0 امتیاز
۷۲.۶٪
را با سرعت حدوداً
۴۷ درصد بیشتر
از GPT-5.6 به ثبت رسانده است.
🔸
ثبت امتیاز
۹۸.۶٪ در آزمون معتبر تعمیم‌پذیری ARC-AGI-3
و امتیاز ۱۰۰٪ در بنچمارک ExploitBench.
🔹
جهش آموزشی با زیرساخت Stargate:
نخستین مدلی که با بیش از ۱۰۰٬۰۰۰ واحد پردازشی آموزش دیده و برای اولین بار، مدل‌های نسل قبل به صورت خودکار بخش اعظم نظارت بر آموزش آن را بر عهده داشته‌اند (حرکت به سمت خودبهبودی بازگشتی).
⚠️
ابهامات و حواشی مهم پیرامون رونمایی:
🔹
غیبت بنچمارک اقتصادی GDPval:
در گزارش‌های منتشرشده، نتایج آزمون GDPval (سنجش کارهای واقعی بازار کار و اقتصاد) دیده نمی‌شود که این امر تحلیل دقیق بازدهی سازمانی آن را فعلاً با شکاف روبه‌رو کرده است.
🔹
سایه بحران‌های امنیتی پیشین:
این رونمایی پس از حادثه جنجالی نفوذ یک مدل داخلی و منتشرنشده اوپن‌ای‌آی به هاگینگ‌فیس انجام شده و مدیران شرکت بر حفظ لایه‌های نظارتی سخت‌گیرانه روی ایمنی Astra تاکید دارند.
🔹
عرضه:
دسترسی سازمانی برای بخش امنیت سایبری از امروز آغاز شده و طی روزهای آینده برای کاربران Plus، Pro و Enterprise فعال خواهد شد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLSk8OEkqkqQn4sKtzm95GzN_FMjCOaURl25jGAQEdIrkCrQEYVmoUHGopA3E2Kb0ttoUCCeCQ6INoG487-8dMflZr8Y1KI_w1FBWXxMyZL8sY1DcY078aqszKfU4AdczW57KVFjeFt-d4Ypxp0Rg4pcLQMHxtAWwbc5daL5yiEOq7Z-BTAZhuOFH28dwHwrJsUMDarFsP7UpDvrAhaKyKaprWSd1TjY6LEyae2SaJ82zfykYDkudnJQAqvJrTT4O6Hhb2NFUS7AmG8ZrWVG-xOilrqELmaIsMSjJQdX_zjSiTo9yfDbmLunkZOrpTfDt8AC1GqDZRhIyxEr5t-0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏛
مخالفت زاکربرگ با طرح نظارت بر هوش مصنوعی در گفتگوی محرمانه با ترامپ
به گزارش نشریه
Politico
، مارک زاکربرگ، مدیرعامل متا، در یک تماس تلفنی خصوصی با دونالد ترامپ با پیشنهاد ایجاد یک نهاد نظارتی ملی و فدرال برای هوش مصنوعی به مخالفت پرداخته است.
⚙️
محورها و جزئیات کلیدی خبر:
🔹
پیشنهاد نظارتی به سبک FINRA:
این طرح که با حمایت دمیس هاسابیس (مدیرعامل گوگل دیپ‌مایند) و برخی مشاوران ارشد کاخ سفید مطرح شده، به دنبال ایجاد یک نهاد شبه‌مستقل ناظر (مشابه FINRA در بازار مالی) است تا مدل‌های پیشرفته هوش مصنوعی را پیش از عرضه عمومی، از نظر خطرات امنیتی و فنی ارزیابی و آزمایش کند.
🔹
موضع زاکربرگ:
مدیرعامل متا در گفتگوی ماه اوت خود با ترامپ تاکید کرده که هرگونه ساختار نظارتی باید با رویکرد «مداخله حداقلی (Light-touch)» دولت همسو باشد تا مانع رشد نوآوری و سرعت شرکت‌های فناوری آمریکایی نشود.
🔹
دو‌راهی دولت ترامپ:
کاخ سفید در حال حاضر بین دو گزینه مردد است: پذیرش مدل نظارتی مشابه FINRA یا انتخاب رویکرد صنعت‌محور و پیشنهادی دیوید ساکس (David Sacks) با حداقل سخت‌گیری دولتی.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdolB-Aznd3uTZw4B88ZZuqxPIN6A8YtpHv5-y2x7ncxq619jMWBOa3Oi8CLUyjfs_0IV1fjIeBoPhx_ocbjXtvJJfjyOozKuHEmZxC1Nfd5V8aFEtBRp_TKuuZWUkioX8yBsoksTot78Dnvv5kv0umun36QUDlR6UHiwuaJT3VwL-iYgWQucSh1zrOEONrkhyqyfwZ3EGMQHtO5vCxjHfo6bYItGxr6WNufL_48q_pQqBXXARRyD2CCAb8OaExYf-QnxpoDl8bNqTm7IRfwPAJCVPUYN9tA-ShQIE6ZZSjTPK9gxEINGyBPC_mVzxkoM0EXxnwWaAKzyGQbRlD-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
خاموشی هم‌زمان چت‌جی‌پی‌تی، گراک و کلاد
سه چت‌بات بزرگ و محبوب دنیای هوش مصنوعی شامل
ChatGPT
(اوپن‌ای‌آی)،
Grok
(ایکس‌ای‌آی) و
Claude
(آنتروپیک) به‌طور هم‌زمان دچار قطعی گسترده و سراسری در جهان شدند.
⚙️
جزئیات اختلال و سرویس‌های آسیب‌دیده:
🔹
دامنه قطعی:
دسترسی به رابط‌های چت، APIها، قابلیت‌های صوتی، تولید تصویر و بارگذاری فایل‌ها در هر سه پلتفرم با خطاهای گسترده روبه‌رو شده است.
🔹
اختلال در ChatGPT:
نمایش خطاهای مداوم و از کار افتادن سرویس ورود و جست‌وجو؛ این اتفاق هم‌زمان با انتشار پیش‌نمایش‌های مدل جدید
Astra
رخ داده است.
🔹
قطعی کامل در Claude و Grok:
سرویس کلاینت و کدنویسی Claude Code و همچنین چت‌بات Grok در وب، اندروید و iOS به‌طور کامل از کار افتاده‌اند.
🔹
علت نامشخص:
تاکنون هیچ‌کدام از شرکت‌ها دلیل دقیق این خاموشی هم‌زمان یا ارتباط احتمالی میان این اختلالات زنجیره‌ای را رسماً تایید نکرده‌اند و تیم‌های فنی در حال رفع مشکل هستند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNN_81X8ECMaiqGVfq9lhaZHyg27dJfmeHkWRtZuWYrRMY_0-HJ0Pv0CEVcDtRtyoHnh29JA30Lm7GhVtKR9U30tRI9TPjH0QURxm7OLJmukf0qAf95IkC2DPFo3cVi3BHFoOU7TyvQPbYApmEZQ29KM0eHGSvpPTpUek5JVJG1HrTIZDdaBAh0Pqx_q_t37QmqFCsq8pQ6bPFSZSTvgJgoCd3eD4ShmjtG9TBTtoSwFbnpYvG3Sdx6g2GmXTTodif4DVzc-4gmI-64JDWXLV6C2FvZmTZGSmwwmbPOq2VqHWV3R0pgSG1nhetkAz1NGk_13EO5JWAHw2-o0vCouLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پنل همه‌کاره فیلترشکن (انواع هسته + تانل داخلی و مدیریت با هوش مصنوعی)
🚀
🔹
تو این آموزش یک پنل فوق‌العاده رو بررسی می‌کنیم که نه تنها از هسته های مختلف (مثل Xray و وایرگارد و OpenVpn و L2TP) پشتیبانی می‌کنه و تانل داخلی اختصاصی داره، بلکه به کمک هوش مصنوعی تنظیمات و کانفیگ‌ها رو براتون بهینه‌سازی و مدیریت می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🛡
چک‌لیست طلایی امنیت اینستاگرام؛ ۷ قدم تا ضدگلوله کردن حساب کاربری
با صرف چند دقیقه وقت و اعمال این ۷ تنظیم کلیدی، احتمال هک و نفوذ به اکانت اینستاگرام خود را به حداقل برسانید:
🔹
۱. تغییر رمز عبور یا فعال‌سازی Passkey:
استفاده از پسورد طولانی و ترکیبی یا کلید عبور هوشمند.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Change password
🔹
۲. فعال‌سازی تأیید هویت دومرحله‌ای (2FA):
ایجاد لایه امنیتی قدرتمند؛ حتماً از اپلیکیشن‌های Authenticator (مانند گوگل یا مایکروسافت) استفاده کنید، نه پیامک (SMS).
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Two-factor authentication
🔹
۳. بررسی نشست‌ها و دستگاه‌های متصل:
مشاهده نشست‌های فعال و لاگ‌اوت کردن دستگاه‌های ناشناس یا مشکوک.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Where you're logged in
🔹
۴. لغو همگام‌سازی مخاطبین گوشی:
جلوگیری از آپلود شماره تلفن‌ها و پیشنهاد اکانت به مخاطبان دفترچه تلفن.
📍
مسیر:
Settings and activity > Accounts Center > Your information and permissions > Upload contacts
🔹
۵. خصوصی‌سازی پیج (Private Account):
محدود کردن دسترسی به پست‌ها و استوری‌ها فقط برای دنبال‌کنندگان تاییدشده.
📍
مسیر:
Settings and activity > Account privacy > Private account
🔹
۶. حذف دسترسی برنامه‌ها و سایت‌های متفرقه:
قطع دسترسی ابزارها، ربات‌ها و وب‌سایت‌های شخص ثالث به اکانت.
📍
مسیر:
Settings and activity > Website permissions > Apps and websites
🔹
۷. عدم نمایش پیج در بخش پیشنهادات (Suggested):
جلوگیری از نمایش حساب شما در بخش اکانت‌های پیشنهادی به سایر کاربران (از طریق نسخه وب اینستاگرام).
📍
مسیر: ورود به وب‌سایت
instagram.com
> بخش
Edit profile
> غیرفعال‌سازی تیک
Show account suggestions on profiles
©️
پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpEvJprGP3TCGPoikrFca3M53d-hbJ-DsRgPaKH00OrbZknqWDchj7_t0d1VEmmZf_L23gaYezZqZmOSIGgAgx5uC0OjZhmg7-Re4IYL4YyKDSProUyn4_CzpB637YOd0zqQOFzDvMbungyNnq-YoBEZJ_zjSvveFXyrP8uvdFsuzk6gUv0TDcBlgZdl9aswMftxke241ITmkfuPj2dyJ_DkkSORgq5VmRJpVtS4v1Eix9VFYrqI8LvHo50rS_iYOEzeW4SMgGtiApnSaMNk5E8SbI9IQOTtNJ0kjmjRscZrV8gKGqsaGi3MGR2p2qlt0sLU_Nd-LMouhLRtL8XVhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhoW3G7rXENfW57Dz7dWJY4I-9i9rlOc5So1GeNcBWV_h7ztAdg3JZSyg3S3XoWajpmWJYStbEgB4KoVWpiYAG2y9AX-4nTJNfkQ8nAzD1vO1NUXoeA-p4RB01ve1kLF9m2kIdt8Vely_7otEiDhzsWq8K75eyAou8M1eZvIjYJy7zwpw6wWRit8B4FWQoQWfl4iUIYTWayun2yMFp-8fxGH9HUK3Ah2hzuSCCmRZ9kIToH_dTyXHD8MQkHX6Q3-w6DyUrOMml-InQiRb40sT2tJIXZEnJL907LuIoGZRbvP9Nq1IAq8F8BEdcQNOvl43ZS8DQYyqSj9oL53efhuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌸
تقدیر و تشکر از یک همراه همیشگی کامیونیتی | مارک عزیز
در روزهایی که دسترسی آزاد به اینترنت و سرویس‌های پایه برای کاربران و توسعه‌دهندگان ایرانی به یک چالش روزمره و فرسایشی تبدیل شده، حضور افرادی که بی‌سروصدا و بدون چشم‌داشت برای رفع این موانع تلاش می‌کنند، غنیمتی بزرگیه.
امروز میخوام از
مارک
عزیز صمیمانه تشکر کنم. کسی که شاید خیلی از ما اون را نشناسیم یا از حجم فعالیت‌هایش بی‌خبر باشیم، اما مارک همیشه حامی دسترسی آزاد به اینترنت بوده.
مارک عزیز، از طرف کل کامیونیتی، بچه‌های شبکه و همه اونایی که نتیجه زحماتت بهشون می‌رسه، بهت خسته نباشید می‌گیم. واقعا مرسی که اینقدر دلسوزانه پیگیر کارها هستی. دمت گرم که همیشه هوای بچه‌ها رو داری!
💚
✌️
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=tplgYnM1iALA_qfWK4W8W9pi1KwVBKg5w5eXZ2Gt_-l0jivMvthT8SHlSotfdVrENvmavY_q-2DvWT7sSKxzUrm6_yk0sxpnQ_pEd2fraqK21qwIuZcPoO-Pwr9blAdntFsWQythTk6lsdA_Qnvl4rjYT4TxiKvUN_3tW3tiBEpU7P-Mhtv4uRC0PTlrVFmG91UBS7VQatDqPcplXxM_QNW_1_MP3mURR7DX9-yyHv1yfk23Q53aOZwioWP4dle2D42QWOzNl7Z6j3srQmz4nRYEkPea_erFmuQ_8GoBLE04dFOCtwRj7nGlVI9IUakapOuqYKWHUvPPd1VT_4LJMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=tplgYnM1iALA_qfWK4W8W9pi1KwVBKg5w5eXZ2Gt_-l0jivMvthT8SHlSotfdVrENvmavY_q-2DvWT7sSKxzUrm6_yk0sxpnQ_pEd2fraqK21qwIuZcPoO-Pwr9blAdntFsWQythTk6lsdA_Qnvl4rjYT4TxiKvUN_3tW3tiBEpU7P-Mhtv4uRC0PTlrVFmG91UBS7VQatDqPcplXxM_QNW_1_MP3mURR7DX9-yyHv1yfk23Q53aOZwioWP4dle2D42QWOzNl7Z6j3srQmz4nRYEkPea_erFmuQ_8GoBLE04dFOCtwRj7nGlVI9IUakapOuqYKWHUvPPd1VT_4LJMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره هفتم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی pinkpantheranim مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسر عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در ویدیو بعدی باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎮
ویدیو مقایسه جذاب GTA 6 با GTA 5؛ جهش خیره‌کننده گرافیک و گیم‌پلی بعد از ۱۳ سال
با نمایش گیم‌پلی بازی موردانتظار
GTA 6
، مقایسه‌های فنی میان این نسخه و بازی محبوب GTA 5 نشان‌دهنده یک ارتقای نسلی و عمیق در استانداردهای بازی‌های جهان‌باز راک‌استار است.
🔹
جهش چشمگیر گرافیک و جزئیات بصری:
بهبود محسوس در طراحی چهره، فیزیک و انیمیشن موی کاراکترها، سیستم نورپردازی پیشرفته، ارتقای کیفیت بافت‌ها (Textures) و ارائه پوشش گیاهی و محیط‌های شهری فوق‌العاده زنده و واقع‌گرایانه.
🔹
انیمیشن‌های طبیعی و گیم‌پلی واقع‌گرایانه:
طبیعی‌تر شدن فیزیک حرکات شخصیت‌ها و تعریف استانداردی نوین در زمینه تعامل با محیط، اکوسیستم شهری و واکنش‌های هوش مصنوعی NPCها (شخصیت‌های غیرقابل‌بازی).
🔹
پلتفرم‌های مقصد و قیمت‌گذاری:
نسخه استاندارد با قیمت ۸۰ دلار و نسخه آلتیمیت با قیمت ۱۰۰ دلار در دسترس پیش‌خرید قرار دارند.
📅
تاریخ انتشار رسمی:
۱۹ نوامبر ۲۰۲۶ (۲۸ آبان ۱۴۰۵)
برای کنسول‌های پلی‌استیشن ۵، ایکس‌باکس سری ایکس و ایکس‌باکس سری اس. /منبع:sargarme
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2944" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgPzOpkpSoKIT-iTvbdQIOo5ludW5AGVEPnGlarOa1NggZrqTIs2y5HjiK9vEUGADttJ9xzWXFs97SniOeUWqrpncDKNMPBMscIPZnEofUnDAeY7d2ckSc_f7O9HVWgyeXkRIl-_5nw8gkEdI13iQ2KgMNDoZr1CuVr-THGRlIkZi1oBu59Dw1MYVgKsyjK3I5w6hj-nWOiTBknfX-jtvAAYzLwpKIY78NVi-E01ZEZk3Od-EB9bJpH1CGR4fVCoNJyzpvmqtydDP3vQghWM5xwipVWpzDSfZGughzaeQOYbCrDEopuRuzQFrqXufEIF74I_G1eNh2GzfqKa7OWMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی PingTunnel VPN Client؛ کلاینت ویندوز برای پروتکل ICMP
پروژه
PingTunnel-VPN-Client
یک کلاینت مدرن تحت ویندوز (WPF) است که با ترکیب
pingtunnel
،
tun2socks
و آداپتور
Wintun
، امکان عبور دادن کل ترافیک سیستم از بستر پکت‌های ICMP (پینگ) را فراهم می‌کند.
🔹
مانیتورینگ و نمایش زنده ترافیک:
نمایش لحظه‌ای سرعت دانلود و آپلود تانل به همراه مصرف کارت شبکه فیزیکی و سیستم لایو لاگ (Live Logs).
🔹
امنیت DNS و بهینه‌سازی ترافیک:
مجهز به فورواردر و کش داخلی DNS جهت جلوگیری از نشت DNS (DNS Leak Protection) و مسدودسازی UDP روی اینترفیس TUN جهت جلوگیری از خطاهای ناشی از ترافیک QUIC.
🔹
پایش سلامت و اتصال پایدار:
بررسی مداوم تاخیر (Latency) با قابلیت ری‌استارت خودکار در صورت افت کیفیت، به همراه سیستم بازیابی پس از کرش و پاک‌سازی رول‌های فایروال.
🔹
قابلیت Split-Tunneling:
امکان مستثنی‌کردن ساب‌نت‌ها و رنج‌های آی‌پی مشخص جهت عبور مستقیم ترافیک بدون رفتن به داخل تانل.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
