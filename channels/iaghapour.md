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
<img src="https://cdn4.telesco.pe/file/eSz27MsCkjNLn9OSs_VflAEWJGaKVZyeXFCkRAxgRcoMR-vbLPIXcSRzX8WfO5JaoISWQe-VrirDGle3LddDCSEqBIX92WRY9AAOCQxY0GM9DGmse3HxGwihRlqAXPGzgwChdZti4BX3zMB8syHKCc3cG8ZvZZsm5aXHJtOoGXP8pPj3C6NVin3BgwNThB52xHwymVjYBLBmbaOM6eRe5E8hqlxxw9OUYym1pDKqQflAZa8jAQOlXK4zU5EI6ij1gtZV62KSJGrvQL8KwZvW9h0ph4BMQXYZ_u2ngzXuNgmGL5V5r0oYGP-4IZiddps2ilIY7MmlzcejKymNSklIAA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.6K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 02:05:02</div>
<hr>

<div class="tg-post" id="msg-3033">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTixo Cloud</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4MRYHe8ta9-riNSHpBK7IV44pKEU1yqjDaMSU2amvi4qVEOiEHp1xr4NKwpZX_p0WBpbPbrXvdO8QnpK6yg7l6TJdIxG5B0y6gqNUPDwV2jwLr7s38A242d3LL6aQsGGTal4wP00WEV28zi31i8JtmvvbaKhWfMlcW4eWC8uPLG9rC8AeTnxuBUuKv79GwaZUUp1iKx4zNWwPTbK1DwbHT5waAQE1ps8ZCZS9Y_3_stcbHqOk2g1S1KJf-c3brYkXYO9LpNzTHihs_RZe1LSplncv8J9BDKEMer-RdFt-rfoR_zlIymhznfr0NAevwPQ7-DHyttKZQYAc-EcDsZ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
برای ترافیک بالا، زیرساخت معمولی کافی نیست.
🛜
سرور مجازی ایران با شبکه پرسرعت و
پورت اختصاصی 10Gbps
🌐
مشخصات شبکه
• پورت اختصاصی
10Gbps
• دیتاسنتر
مبین‌وان با Uplink آسیاتک
•
آی‌پی نیم‌بها
• مسیریابی بهینه و شبکه پایدار
• ترافیک با
آپلود رایگان
🪙
تعرفه‌ها
• پلن‌های سرور مجازی از
۶۰۰,۰۰۰ تومان / ماه
• هر ترابایت ترافیک:
۸۵۰,۰۰۰ تومان
— آپلود رایگان
• هر آی‌پی:
۲۵۰,۰۰۰ تومان
•
تخفیف اختصاصی برای مصارف بالا
💎
تمامی قیمت‌ها
نهایی
هستند و مالیات بر ارزش افزوده به مبلغ سرویس اضافه نمی‌شود.
📦
مشاهده پلن‌ها و قیمت‌ها
🛠
وب‌سایت تیکسوکلود در حال بروزرسانی و تکمیل است؛ در حال حاضر
ثبت سفارش، خرید، تمدید، شارژ ترافیک و پشتیبانی
از طریق تلگرام انجام می‌شود.
⚙️
راه‌اندازی و کانفیگ اولیه تانل، یک‌بار رایگان
💬
پشتیبانی ۲۴/۷
☁️
تیکسوکلود | شبکه‌ای قدرتمندتر، تجربه‌ای سریع‌تر
👤
@TixoCloudSupport
✅
@TixoCloud
🌐
TixoCloud.com</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/iaghapour/3033" target="_blank">📅 21:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_lbHKwBg7gkvgy_nyb_0NgidsxhjwuUFgbhkzWwBctJvr6t68ajs-dfTfOT8KRs1YgTa4CevZIVCia_VVkKpBM2co60L-BemnE5AEqWcj6xKnRO8cmQ3PUGKckSANA6VkFocehS23enYsdo4OOkiRfzt0BgZ1RDpC888_t2o1SsmlxovQRoNrihXvK9Y94FnEP0rllR9W79NhwQSGVR4785CgrCmT-D9DNGDJ0hxwFvtQ99_MdMaQZhWeOdo2pUDygBIvI0Ba51Y_yhFEXGy_Ypj0qM7W1_QRhEyA7MVlTmFeTWuti1_usC9IXevKLD2NIr2bV4qJ2JupWdCirRnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHZIYmdUGSlWrbCQVWNtBFAvkgVEKEaoYcW4adCyf7mQ8617DhYvsCIRV3xFjbcQicqHYQR0ur80xQ1bY-Pv4qLvfHmnAohNqdoh-EhtiQs6Lh4OZ0xukRU8A--tsTZ6n6S0sZE2kjKol8XaJJwJrieaIxL1szqg1GBQc7yEm0aq-AQjVMpxaO2UMil784mMNNP8llDbIoizhXpf5QzGlNNujQ6WcXke89AwSoa9XZ6Vh89iwo_wp7KjNCxxs1PX4KlwOxDlX7BEsuIJ8yIrT6V0iFQmWkLy-w4eqltsRsnnIcAPkcda4A1F7FJg9DrS1xgDo8iL_tYVPSrJSrEU1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3030">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ8YPytWiCU_1dJhn190A3exDwKvjIlOSwzKQ69is9DF8s4-GDkDp6YM7zHikBmz6V2KUs_PxAHQeFFk_Y_9TYpoVC6aSJa1oDwr2TlYJI5jjq73bRXPpzY3Y6HipyieMowAIFlcHZd6VaebBTSClnr5H9TOfV3DzobQBXRBCxoshzAt16v3W1p8I_8NtkIGKgLXckrpQwGLb6FOE35foBmdPjehBt6bZ5iDDDpPvlqboZ7QeCdauqwv2Z2plASclO8fDucrg6zlResQpxVEPSE1v3_yoBMxrBvAbgs9dkI--5EWd5agcKdY6qvZErqp5q6dXPRYF9L46hmc5dfNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎭
دم خروس پاول دورف از زیر لباس ایتا بیرون زد!
سال‌ها با بودجه‌های چند ده میلیاردی گفتن: «ما با اتکا به دانش بومی و نخبگان داخلی، پلتفرمی کاملاً ملی، مستقل و امن ساختیم!»
حالا توی جدیدترین آپدیت نسخه وب مسنجر ایتا، دولوپر خسته یادش رفته حتی کامنت‌ها و استرینگ‌های سورس تلگرام رو کامل Find and Replace کنه؛ کاربر زده سابقه جستجو رو پاک کنه، پاپ‌آپ اومده بالا با فونت درشت و انگلیسی:
«Telegram: Are you sure you want to clear your search history?»
قشنگ مشخصه برنامه‌نویسه کدهای Telegram Web رو کلون کرده، کنترل+F زده هرچی Telegram بوده رو کرده Eitaa، بعد سر این یدونه دیالوگ اینترنتش قطع شده یا چاییش سرد شده یادش رفته Replace All بزنه!
خلاصه که زحمت نکشید فیلترشکن بزنید برید تلگرام؛ خود تلگرام با سورس رایگان و دست‌نخورده در ایتا منتظر شماست، فقط سرورش توی ایرانه!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/iaghapour/3030" target="_blank">📅 16:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3029">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from✿⃟🍂 Sαм! / سام</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSfZhD6jln7tlBYaw8a_CTql_mOOKfZSJUSASesGm2TwekyDaPyje5PHCNcbNeVbLMDSeeeOXXzGdyJitFK_SjOvk28kK6KP-XlZjqfmp_oC92CcrvX_6c9EO3ol-hWyxc5q0aMDRS-pwV3tgs0DDuPNp5snh-WE4hCIWJSe-Y-4KBpj6HncfU1EdrtJmkMBpixKC64yRDbzu6RiasiYF5YiTZn5k4rf6qeWuRs7BekaObSuHfIT1M_f45uUWs-_eGC87L6Ch_bAke5goyv4i02QVYAjTJ9vsfGsW5dfOnlu6iMkq4R98zqmUd9avQCF-DTa5JoFzyAjSsKksxOXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
🔻
♻️
سرویس ویژه یوتیوب، ترید وگیمینگ (بازی) با WireGuard
🎮
🪩
آواژنت
با پروتکل
WireGuard
سرویس اختصاصی، با 2
لوکیشن
🇹🇷
🇵🇱
با یک خرید.
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
♾
اشتراک
♻️
نامحدود مولتی لوکیشن کامبو؛ بدون دغدغه حجم!
با 3 لوکیشن
آلمان
🇩🇪
و ترکیه
🇹🇷
و آمریکا
🇺🇸
؛ رفع انواع تحریم ها از جمله جمنای Gemini .
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🎉
20
تومان هدیه خرید اول با لینک زیر؛
شروع
قیمت ها از 100 هزار تومن
. روی لینک معرفی بزن و شروع ربات و بزن.
⬇️
https://t.me/avazhnet_bot?start=ref_531615606
🎁
تست رایگان |
اول تست کن، بعد خرید کن.
⬅️
تمامی سرویس ها تانل شده
و
سازگار با تمامی اپراتور ها
.
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/iaghapour/3029" target="_blank">📅 21:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=M-a0OOw5dhsLAQ92BWe0mYFur1QMNgxZl23gw34Axzm9Xy-U4iy0f9HwKAp6Y16JnSoPshXnf4jG8nqije2ZIcWzFVDrPmKGEd6aZpLCX9AOe1SSrW8hTgozAXnCvTsG9xhMPqTpqTaRCsBIcQYIDtA6a2oR2XIL_EvGp5-HzJKMVp5UVB5qot3-AJy2LBfaokPwGgSOFd5NKn7mhUvflUQ4-vUqX2azDqbkm3dNreS4JoMrJvlAq2aSuQxjNxL0ZNWKErNbTTnmUHhPGqZ_p6q9etsp1n78VS6GxJFL2ksaLd1mRbQw6Id7deCK5RaKFfJyZyVFKEOd1jQWZfbpog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=M-a0OOw5dhsLAQ92BWe0mYFur1QMNgxZl23gw34Axzm9Xy-U4iy0f9HwKAp6Y16JnSoPshXnf4jG8nqije2ZIcWzFVDrPmKGEd6aZpLCX9AOe1SSrW8hTgozAXnCvTsG9xhMPqTpqTaRCsBIcQYIDtA6a2oR2XIL_EvGp5-HzJKMVp5UVB5qot3-AJy2LBfaokPwGgSOFd5NKn7mhUvflUQ4-vUqX2azDqbkm3dNreS4JoMrJvlAq2aSuQxjNxL0ZNWKErNbTTnmUHhPGqZ_p6q9etsp1n78VS6GxJFL2ksaLd1mRbQw6Id7deCK5RaKFfJyZyVFKEOd1jQWZfbpog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3026">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBwHwpBGWXyjvWK8oSPE0xXmlvIKlXmmGY5jwEnf5GN7883OxM3NiPny7hmYE4bH_AjAnrIJmTZlyHHAWrM03Tuj_OaMgRQd4tJsh8bG5q8XX0zg0fwmsXNHqG0zcoss2FzLMbrvh0T2JqQAR-0fcu_M3_Ka6viP5STVRU5ikVPr5xA4SeTXSDLVMd9NxnX0ZMTEvY5Si2XsZ1R9z9XFUAHljVR12p9zWNuEMNDrE5A3DmYsa9XLfovIEqJ7Lrq9QOPxK6Ll0zaqv6C-AuqAM_3RhGt-7Xi_xSlpAC66SS6aUBDY69Hw3CNPKmNyixZp8l0qCvZUz2mVvXJmdOQW7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
هشدار پادشاه بریتانیا به غول‌های هوش مصنوعی: تضمین دهید سرنوشت بشر از کنترل خارج نمی‌شود
چارلز سوم در یک رویداد سلطنتی در اسکاتلند، با چهره‌های ارشد هوش مصنوعی پشت درهای بسته دیدار می‌کند تا از آن‌ها تضمین بگیرد که پیشرفت پرشتاب این فناوری آینده و بقای بشریت را تهدید نخواهد کرد.
⚙️
نکات کلیدی این نشست و حواشی آن:
🔹
حاضران کلیدی نشست:
دمیس هاسابیس (هم‌بنیان‌گذار گوگل دیپ‌مایند)، نمایندگان ارشد OpenAI، انویدیا و آنتروپیک، به‌همراه کاناتیشکا نارایان، وزیر هوش مصنوعی بریتانیا.
🔸
شکاف عمیق میان رهبران فناوری:
درحالی‌که داریو آمودی (آنتروپیک)، سم آلتمن (OpenAI) و دمیس هاسابیس خواستار ترمز در توسعه و مدیریت ریسک‌های مرگ‌بار این فناوری هستند، جنسن هوانگ (مدیرعامل انویدیا) با هرگونه توقف، کندسازی یا قانون‌گذاری مازاد مخالفت کرده است.
🔹
نگرانی از پژوهشگران فراری:
هم‌زمان با این نشست، استعفای دو تن از محققان برجسته دیپ‌مایند و آنتروپیک با ادعای «مرگ‌بار بودن پتانسیل‌های کنترل‌نشده AI»، موجی از هشدارها را در محافل علمی و رسانه‌ای ایجاد کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/iaghapour/3026" target="_blank">📅 16:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSh3Zh7GLwc5pFwhQlXw8hG2xGtIOSjtjLmQF_XSkx2Tgwy31htmUuaryQ_9TfaXOCAyWyDvK2fB4fnWgJK6IL-Kwc1h_SvbM2cQ_cp8UA_dUXGHphaDkujZtY0TAV4p1I8r4bMaEGdEl3O57QTj_FHAFoIV_zal9tGKkj45gDKvWILm2k75CFLK0hweH12vDpyM4huKfw6okk5VOpPHl9UWXs4H8Ab93Z6QgRggjVmTsSVauhJ0mR3LyJIxUEu1vRHfmTQXcXO5tXk586MT0gtcb-0TnGjKIMO9z1OQfGsOgUqjHAD01JJ7_0MOF7UK6pJ0CQQELLKrszdTMp-Z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دانلود فایل ایزو ویندوز اورجینال از سرور‌های مایکروسافت (با ۱ کلیک)
🔹
اگه از نصب ویندوزهای دستکاری شده و پر از باگ خسته شدید این ویدیو دقیقاً برای شماست. تو این آموزش، ۲ روش فوق‌العاده ساده و سریع رو بررسی می‌کنیم تا بتونید با ۱ کلیک، فایل ISO ویندوز اورجینال (ویندوز ۱۰ و ۱۱) رو از سرورهای خود مایکروسافت دانلود کنید.
🔗
تماشا ویدیو در یوتیوب
⚡️
دسترسی به تمام مدل‌های هوش مصنوعی فقط با یک API
👈
لینک سایت
||
آدرس کانال
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
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx9UtHueKuK9fN_GMB7IIVwmbBhaNsrktg63EXc44m3MY_UCVvo-2nHANDkcw75mTI9O7SWKlvOnvUNh1_7wQZRjdyKCT_nCJ2gN5GQTiyqwi5E0L3beBna03tVoeTu7O3EnPAEaf81ko2Z3oF-cvAtbOaUoVhSOD_ydxZEk2w40zPTf5w0_52K8Krf20iLnFSz_MTTefXj5J00qr4E58u67p2VgUE61ZzhaBNGnvLILTuHhksAgQY1MFMeEqOwKllrKVpgvrOfs18iPTaZltX1JSYXdVZ9PajsWyMhBfrZofaeG68OzEl0ICzoP44ESEBeIj-bXMS-OD-N1oiKfdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYuALdJqlF4AcFP5CZ7JLJe6KBvUnkMOEaCCtzsrsShmxnU0H5TJkR1Zxmxwkn50N6l7rDDMaH0mc_jPjvVixO5J_Z2nPtIzEpyk9niJWVjzKB_5DpcVAKlEf6uTmPNRSiSB039bLqPwrSw7E5an2g9J2z8gbgbpNqw5A-ugG3NUELXblrWUkqPYJN3wee3mDSv30jClAfJklQNaF3Ba-hNSJuxOOD_fj8W8trZS4aMA7MeMMZn8DajRvLrBbiXbkUFySm5kSEA4gCezDHozknXj1e3hQsMXcHU_5Qf8leGj6ZqfIqZvBFjMmS9LJ8V58z4UVSjFm-BMVEj7yBippA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbHzYoNNdKY_hzYSNICXw0OhTaZ71t1_mTFgmtphdOY779DG047kbFXw3CdQJ-0sPVdNxshrIeNHkgfHUC-i1S0y7C3q3vbUe-MW-rVAchFzN6IM9-MoStD4abDQH8lkp4dnZXmciQ-hDy_4lP-wlkbtjvn25LLBfJZA4-_sNZ8DufKvuAvA1O4zeOVdE2aszSEhP6AdB_vkoFEMRJcXkGa_qxjRE_ZuwgLWo1Aq5uwU9bInCE9T5mjgHZxK94gnoO-HqIAfiCwNo37uGLeQgHoFORzd5AaBbuAde9jpDrXGDb-earlPqo_9aqTpfJvSWPXfIagVYQP15sP4okT62A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyBb2URC6GXQ7d3glu6VJWqXVs3PRcTAfJwhHi4RTLEOpDoEBtWQv8xw7_XGTGSoBTA5kaXKwsoTzLG-pcXEUfxp5dm8lD6guLqZMCfgR7xXLWNCNzoLj1-JTEKCGu8fRAfO_drNsEVcjwzIOvc9LJnC34N4KK6Z00Zp4vIj6FnEpvC3Y2dkA3sEu2ALYr-1EhqnRi85QzcLjzoRTXH0fZuLyLqVkKBZR_i3Ndgdu3WSS1JBoHh-sXxE3jUbYPsTIKM5qXO2k6zAWD_jHT3qK8rYNNkNSpAXieLudgI6PdLxb3gY02lTERyDljMajwDLxE4gmwGhfeDtg7nizy71WQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLfYwRwAR59dbLLDitFm65bH6B0v2LyAwYjo1e2x2JPJsnAchtuwBcs6keZXa4ZKKE2anCfPWkp_0VuyRASjGYJEhzORo6FM6wC_z6UebV1-3tKzmPLvhqLYkzEI7xH6nSYUS-tjmQ5mDP26hgKW8mHsblpC9SkWoyO_I5YGVrWykT4io7qauz3Yn0H36h86lHb-lhl3ZeuFOVAmaCFMFPZPOeivb4TdLdNUd-MsPc4-FHt8aGJ1Kzor5ql9zGxPsflrtbgiprbPZkkhXSYe54kt2814iFNOdK6ZSxK9h40eOc629-HPZaeelxajQjPA46AclxeRmXLC5A6jY2_ZhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=qYrQVvLVg_GCQacrms3iWWcwRKrxAPuHrUgpxp9SECprlM8cz5dA3-XZAiyAL1OH4tGxCfc_CPXyN5gVbMufuUjc341qIyHkyXHh1BQnaC4Q_BxF_fHKAQ39yNMO8LbwroVxyeuR-AJNh9Re5x39tGptY8Hk1X5gmYlQs1jgPAAA7I2UXtLDJIgMOb0aMZCNGp9cOVo-sb4u7qHSntDx0mGBoFXaFXhlui3sl7eXAKIO3LWluRLJF7Ym1PqoQI2Bvw9RRkoVr647-UyPZYAxHM07_JRWD0i8Vm5XdzK-sFbkZhCmze3x5lIlMAlK8iYKsrrvuJ-bBQO3cGiJhQD5KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=qYrQVvLVg_GCQacrms3iWWcwRKrxAPuHrUgpxp9SECprlM8cz5dA3-XZAiyAL1OH4tGxCfc_CPXyN5gVbMufuUjc341qIyHkyXHh1BQnaC4Q_BxF_fHKAQ39yNMO8LbwroVxyeuR-AJNh9Re5x39tGptY8Hk1X5gmYlQs1jgPAAA7I2UXtLDJIgMOb0aMZCNGp9cOVo-sb4u7qHSntDx0mGBoFXaFXhlui3sl7eXAKIO3LWluRLJF7Ym1PqoQI2Bvw9RRkoVr647-UyPZYAxHM07_JRWD0i8Vm5XdzK-sFbkZhCmze3x5lIlMAlK8iYKsrrvuJ-bBQO3cGiJhQD5KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNxXB2TzE8JMh3OGrWd7g8BB-LJPR2n7gn7KcX4VuqM4RnPosiPSNS2xoR6NJvE-g4GHp1cHW-D-9pfYkXm-bEkjNwynA39sBZKTEWC5FDntNTyflhTaLr_QH8ZJSnFw_9INwybrta62KhgNHsGBKL_lQFrLpwYYkvFh8LKByfi_DSC9vsACOFBVMO-hSwiG-LbfHnI1LhKPYo1RiVjZ_kZ0h7akDJdMd1M3sqKhUI8BK_RlEyfoTGrZxFDmkddvCfE0XxTtuB2sG9uhbm5n5aiX0F3DKCTDMBuW1ihlQUnW0RFuwqVx0MXsKSBIXhQah1EUig1mZ_fDOxUyjOehTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC43kEo6nQ0X8DnNAW3-8ZjtpcMwPy0umBRbsAf8SaBBBWzUIXgEtNqkATz4nPbjrV8BTZ0m-9cOIxRxKaYCqGUHHfZvVF1QihIbwlcaZ1916FqUfngikQSar7gaU_Njpz2cnMTHD5uRhCBbIaJkGw8-FvpwJPqmFGIeRJpqn-Eu9K4_wvmky2deEIFyUuKkMRuXewfIMwUxETSLMdzHxUgfbW7DYQr2yGbZDSA04RF6VWLDOGsXP-w58RUtHpCAa7Og5HgPOgSo9IX6rYg7NX2rZOo2CkUhy3BFWfcLS0YGh2PYrW2DYfui_CWMY7JGiuzHPL-tAtjlVBGd6q400g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNKDFL7D3uIh5bFqlabg7YxaZjluuAaOIh7I_JJEk2W3eZF5OV0EsLOcZz-KV_duDk5NHke-80jjFT2qEo2myKtHUjEF9rtr_AKVM3XauXWgFe5xUDdvNOcJl8UCNRdB3FMdSc43h5V5IyEvR2zEh5CyjozBSdoOygdrPTrzAjwHMqqJfvbqfklZj7hUqYTRn7vMGETTEy1mfYtTCSiyO89jkYymEh94q2DHLkYgUCzUAq-9QbsoMNhrPzhnKz3O3CyBlE-1gIifMCy-KDKYLOUyjKzNbAKA26eYP_G_iO2-rGvaAA24rHAzkiCcH2SdZFmnVAkCDReAVxV2w6uN8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGWA9-wD4dwNvblkxkf8vmvLUunDDMgU3xIEh1pIqvPqDvCzOowjdvebQ3msZ2Da8Nk7dI7WXZl0yBZuKjoG60EQzUWM4_Ktiy9C9sC7ThLY_oO2E3srwgiAlfox_iSf2a-QOA9va_mWlDdpYurmYfYlLNLZHyceOV5lW8c2cJduK9rorp5aUpzQLYF8YhaOQdogvDdrmvASazGm4Pj9lt9iCtL3x_ERv-Uc-EuW3M3otES7uYduyzBCyj476_GYW4dq3Rz_IRgvrO9qd-XTVN7V3lfkmTm3JaMlGU1IyQbNgfA9viu-ZM2wY9diw2kZS_BJSlyr082XhfB3LR4zRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6a1cj_f8Gubsh2dySb1EiGFU92glKVBjsZzcZ___DtFJhUI77RS5NDke0ZCNXzaFy_tbdy4Z8hBtgSyjqpEdLfn6qu0QzPucr4cmgFMIJ77E5oM5BdbyDGKmN5o2Ao4_UwoTeluhmSn3xVss0Zjigwkkuxuz_Oov7Ph0GSwonTKTWtuJL404CeCoveeZ2BWuOP_pyQ55_eK64Bo1nvaqnZkQJ59Y7ZS98NDnokjL8poW_YBkIXeAqYPwTVHgL_Ss5_EIAYXWjsCiOK40gBs36mKLA6RyqYfJIRu1MYwcTqp-0KOHy9u-7hO2B41ICAtMEAewb3qu7YZ4bYgpI09ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3003">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kymRhydg-ef1-BjNQJYnH9dEqpGXrQ3HRZNfv-kh7f7bS-AI2eyk9wC4EWV3WV8nsKEjngyKbjiy3CMqkyBahAUqlFQvzP7ts07Kja87M59NqlrytXh3xKG31jf78VYXzC-ClY_Ppv9S_5KHu2q9Vy4ZcgSwcRbk9E_FYrvai7ODV8pdvuJG_4qWX6WMIvGJmB4VnCNGRgogKgF22q1XpgiIPJ8DYSjhrZP6z3lXi7Q4jpwjeR8eov6JnmO6jvln6EjFEYgdhwWdDwhjzBLo-6ppQSa780KQOa7jx-5BoS8qN-GS690132HlVdjl2Fcyl6ivALZQW0U_W3GHF7tULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دستور وزیر ارتباطات برای بررسی و رفع محدودیت‌های پروتکل IPv6
ستار هاشمی، وزیر ارتباطات، در جلسه شورای راهبری شبکه ملی اطلاعات خواستار تعیین تکلیف سریع و رفع محدودیت‌های اعمال‌شده روی پروتکل
IPv6
شد.
🔹
نبود توجیه قانونی برای محدودیت IPv6:
وزیر ارتباطات تأکید کرد اگر مصوبه قانونی برای محدودیت پروتکل IPv6 وجود ندارد، اعمال محدودیت فنی روی آن هیچ دلیلی ندارد و موضوع باید فوراً رفع شود.
🔸
همگام‌سازی شبکه با استانداردهای جهانی:
هاشمی اعلام کرد شبکه ملی نباید در تقابل با فناوری‌های روز دنیا باشد و مهاجرت به استانداردهای بین‌المللی مثل IPv6 از الزامات توسعه زیرساخت است.
🔹
پایان نگاه دستوری به فناوری:
وی با اشاره به شکست پروژه‌های دستوری مثل جستجوگرهای بومی، تأکید کرد فناوری با دستور پیش نمی‌رود و سامانه‌ها باید توجیه اقتصادی و رقابتی داشته باشند.
پ.ن: سال‌هاست به بهانه اختلال در سیستم‌های فیلترینگ و رصد ترافیک، پیاده‌سازی کامل IPv6 رو توی کشور معطل نگه داشتن و شبکه رو از استانداردهای جهانی عقب انداختن!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3003" target="_blank">📅 18:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG0qV1bmL9PeFGi27vCcw0zGNOT1VnXdrPqJx8RhuETagxDiFKDcz03lkjrzqHt7OnCT2hcu-MMJIOkZYua8vjw5jOBRFIwUvRyLRKeLoZjoDdbpSpORdJRmpSqjkcdLNzyzoKYyuGsD1lqyQM3AWgj4BFID52JhyR48zi2ZC8jh35wT590y-p8IMoXfX66F9b_wBfkBJ5GaL4YvCRp0JvAfrenf5ka5PgDxt-81zDf_kbPiMYoIYF_rWdou2cIZQc746c0jrA0tNOgF5IzSQP4H-Xg7nG4kb7Sk3HpgRMxRDfxR8Gpzx47RXDbbA1PxWMoPBwS92lmdXbT2ivfuFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5_U4rOr_CdPS3iN8--GiPJVQ6fc2WiH867vKHDlgbWeCQJejsdltX-DIKXUA7pC0bVNb8ZlSdhAJ_wPSzKw2BEBf26Jgyp4hNOCFiJd3gNhVc7vYaF3z_tVJIdUbGPD9VO8MxJaVwmYPbR22ZAx1EzOfSukp5CmxTTo-yOufhhOc9DFLPtVizNY5FNJ_nI7rfku4Wmo88UVeAQ5oSki8txf7RoG3-mJBD-LVj9mBJE2YswLtP4y0QhjK9eDB_cOJ07WRfDDO0XFl8jhT6xECjPyugBigugV6SxHrYOQakl-HHF-iiIRwnUEkCMSrS7B11EQ6vE-tleom_rPBbNgzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=GdplL8j-9OfuPnSKj4YEKVcfjy_mvRyv7ceZ-71qhfNBTx57G173d4sY07ZRh-OkTZa4vxT0JuU8tWpz9rvLbP0od_Zv5FORgB-XFkz1B_t7sWaVo0biqgtcIed1fZjG04novrExXt8iSeLcLnS4b2tqoDI6VkVhzNQx-OWWKdh3nau_Nkx7T5BYADJtyjfG_2KlhrwuXogmQkhpfi6HatXa3W81Uupqvd1wJNjuHoNrIiOZFu8skd6UUyyw56WageQKDPv5j-QCI1kj0OgsHAG36IPRpQrCKOzYBVT3OYKc2ku7wkLpB7YjL214ygIHJ-aHlxu-Bs5IBg3fCQqoBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=GdplL8j-9OfuPnSKj4YEKVcfjy_mvRyv7ceZ-71qhfNBTx57G173d4sY07ZRh-OkTZa4vxT0JuU8tWpz9rvLbP0od_Zv5FORgB-XFkz1B_t7sWaVo0biqgtcIed1fZjG04novrExXt8iSeLcLnS4b2tqoDI6VkVhzNQx-OWWKdh3nau_Nkx7T5BYADJtyjfG_2KlhrwuXogmQkhpfi6HatXa3W81Uupqvd1wJNjuHoNrIiOZFu8skd6UUyyw56WageQKDPv5j-QCI1kj0OgsHAG36IPRpQrCKOzYBVT3OYKc2ku7wkLpB7YjL214ygIHJ-aHlxu-Bs5IBg3fCQqoBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJgfZPVHeFowde-aGOUiYoDoORx8Djk_RHxgbIE0BD3tDOxOqKKWj6iP8AoHtK8C8j7Kh4RfBgYlAAZL8Kj6REXDD-curNfKWylJRyPKP0GypLy9o9xv0bldAvQSBYVEuBgtBz4gW60jZBZgdKvBusZdUmNPOUb7sFAJ0dxG8YyT7bjCcab4sDwJF8j_cJUKrjtHoqskmeNnOezv8JGRwf4JgVL7DpVOy2cO4uMRm9tvHm1F7jjUTmx4i31nOkd-rrTr3zlnIdFXl3bfrhdBlukEL6oLNHyR9ZZQdawCJkQMcnb227UkQxsMEEnX05ZefKhkb6Xa9oFoM-Ye10TjHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=eBI4vWy0yp-lGDLjsCDoUfJZJI3QycE6IFjIGZKQ-Q1OFHn3oW-W9NiYdGEwN8BqxaJ_g-8PEoHnrJOE5ME3ViMdinoszYt6pbSEMQy5VT15h_e1plHVYcwwbwvVLNbPiv7Oydi_NjGaheYVaXQGSGTMdCXxnPsGRy7RpZQ4npiQbhYTMRFnu56LiP3yAEgz7wthAm_H2hQT_6_EycgfM0W6X9eYeXNctxyIOVj1Khp38P_VHt_ZLTPa9mtUyj8-9649Q5lEDY6Z6Ku_XVOLJxxzyw48bnx7-J2T9pNa8dsfu6kPgnCBTcCrg01B2pmc79NmE9EDB4UtqT1JB5cgzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=eBI4vWy0yp-lGDLjsCDoUfJZJI3QycE6IFjIGZKQ-Q1OFHn3oW-W9NiYdGEwN8BqxaJ_g-8PEoHnrJOE5ME3ViMdinoszYt6pbSEMQy5VT15h_e1plHVYcwwbwvVLNbPiv7Oydi_NjGaheYVaXQGSGTMdCXxnPsGRy7RpZQ4npiQbhYTMRFnu56LiP3yAEgz7wthAm_H2hQT_6_EycgfM0W6X9eYeXNctxyIOVj1Khp38P_VHt_ZLTPa9mtUyj8-9649Q5lEDY6Z6Ku_XVOLJxxzyw48bnx7-J2T9pNa8dsfu6kPgnCBTcCrg01B2pmc79NmE9EDB4UtqT1JB5cgzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyLR6SOyLbZXCMVJWX6QJr34551zc9loob5Qc2MxWgAmg1yObJJyxaq2JUTy08l17uPJVjoy9ZK_zEyLyb6rYRWbexvEEZx33cctvFjcUZY0NLHDzNwoLE6kCE86UIRyS4a026kwTF6nqu7fHtXioQqZ2ONYkiIPQd8Y3y7eQlLdPK2jC4wqeCyAGOYOCDZKCRnQuUu7HHcF9osBSt1iP03nfgmDnbHOB_HXv6UDsts_IvEJZrXflIu4Y1aqHL_PfRIfzZtdsfPzI-azv_vHNwHcCTa6QFcbG489Jdtu2KukSwx2l8h2_aax1CzioZTAQYxXAEtDMcr4iFGlWO58cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2991">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNA_eJnDKi91B88dhVMzbUgt7tF3eftJIv1Y6HuLO3zj1eHQGb_rBdRNrFF-cr_rrW-hyQkZnZwoknr6thCswLFE2IyFMb54Y0GT_pg5-2OCMva9Zt-uPRuuF3yCydKbb24xzYkKUjNOqnuqq9xf3O3O5BhIH3Opusu4b3xoaaOJCPGfOje2ecvOWsR9kwPl-JlZAGm2v-83U-tzyx542TVLBQQ6ihMDmsxh0oxNn9q0w9jezr7IgafE7lQFYOJZRnDz8z0T7WVWbNHDaaPne97SoZafvyfDoRPxhQHLcFTh5n43h-TjxkJLsPfinI9606vT6lTF0agu-f-epeEyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnyyRRivb60fB6Og_ZVEVJXm1JebKt_4z-bneagYrAF0Dg5kuu2D8IN1V9JMSwmDsS2LGShvWcGltM83R-fXn1-4dMYbUVfnD6s_gKlT7UAFPHkznTXRM5Yxu-WuqHnX9uwSxNSgL-HYok2ShOr0JrH34UuTLZWz23WwIrPjUWe8lcosOqTjzZ_-4VcEEdntCDLgCNsLKjbPKU6tfyWahNdERVrCF1-Omf3iqQ9D1bBQPtABEomIOkec2X6sXrmUTAe-GahnaecTT_9WifGNVWcTOmfvtZKreXybhVSbkbHG3WziCBNqow42KaOGADUmZWN1IO-Js2FC4zfRLdO5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e83kJwyqQDOJo86vWvYQz51QN4x_m_IbAsNbrtIjCWcUSB6MI1sxifS9YSRQpedasawVLbQ3GhaFTHRXV4RQknvpcGa_1VS2f5EuSpbUPLWQlKr-SzDtvXVZYWEn5QyAeZ0RhpcF4Rk5KCXwuLrpOKNev1pEzaAKL6EsiGBGhO_cOnCJprAF1CaKG_zanT1X36k4FFHzGzhOTJyOaQ2gfxsU98EapetQRUSzZhZ0AzhGaibC9rUL-rbETz4YyPSk2OMMMYV5pRRie4nFPLScyQX7eL5qWze3Qep5z3bvQBLvXdbNeQcF4vdAuhExIDbAU_6m-FLBl-FRMZUTeiu2vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
رکوردشکنی تاریخی قیمت آیفون در ایران؟!
اپل رسماً قیمت گوشی تاشوی جدید خود یعنی
iPhone Duo
را در نسخه پایه (۲۵۶ گیگابایت)
۱٬۹۹۹ دلار
و در بالاترین کانفیگ تا
۲٬۹۹۹ دلار
اعلام کرد؛ رقمی که با ورود به بازار ایران احتمالاً به برچسب نجومی
یک میلیارد تومان
خواهد رسید!
⚙️
چرا پیش‌بینی قیمت ۱ میلیارد تومانی برای آیفون دوئو دور از ذهن نیست؟
🔹
مقایسه با قیمت آیفون ۱۷ پرو مکس:
نسخه پایه ۲۵۶ گیگابایتی آیفون ۱۷ پرو مکس با قیمت دلاری ۱٬۱۹۹ دلار، در بازار ایران به صورت رجیسترشده در محدوده
۴۴۰ تا ۴۵۰ میلیون تومان
معامله می‌شود. بنابراین پایه دلاری ۲ هزار دلاری Duo با احتساب هزینه‌های رجیستری، سود واردکننده و حباب هیجانی روزهای نخست، به سادگی مرز ۱ میلیارد تومان را رد می‌کند.
🔹
چالش بزرگ eSIM در ایران:
اپل در آیفون دوئو درگاه سیم‌کارت فیزیکی را به‌طور کامل حذف کرده و فقط از
eSIM
پشتیبانی می‌کند؛ با توجه به عدم فراگیری و محدودیت‌های گسترده فعال‌سازی eSIM در اپراتورهای داخلی، استفاده از این دستگاه در ایران با دردسرهای فنی جدی همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2991" target="_blank">📅 17:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnzQ7REwwcosOXJ0PzOi0cjzlbj1EglJMhIVZlA9kBE3aWIn_tNyC5LOzhNPjDTlRAFuQVF7H19Zyl7kyU2xqcAnPk_-5cEBP0634w7XIzaDzWQViwNjbs1X62VqrS8eYBxYQS-X_jKYA_NnX5HJ42OslZZNgJQqIMXKZdSamyeAMXRFwIsQ4WrI-X0YfFtoLUGfm7OdEirj11p0LN28tlAhahz4bG91vuyOieqYE2Ft-5_yuysMMkZsdWtocoa3uguXSGTGNEHh2OFqjF46yCR4iTF95mdDeJDWjD2V4E1qP_8-JjuGv3zVqQkvNF3raBDFe0Kk2pe6RjR67NJ0XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO0uMuYs5QQGdWUlpWIFf_dlQ1GLCGwa1dPkdBiv92uxI8s2cwvH29i4bZZX1nxI35f6d4O5EuiU_dfNbRQc6SXBAKK86e3udGji0zUfhamR-CI3mW0X-uMSltX_MHRjOKH9XS5dGtmsdeKyhJnVXIpSpMSb7g9VKM8WdHZE8s9Ggzi2gDBn4VaKTDPyvzPwgegZ2PqRbC3fbWUkse69PHzBcuWbBgavxjtnOEU7mUWEfjLMKVhBqgCXXTRbQ-OT1Biu9hqb_vS9E9O1PFi6Bj4VIuSxVEmQM0RHtnn0qjBc0zC262rL6GkIIm7ti6kBFXF45Yz-iIA61PVzF34XoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdbXeygsqAc-R5mK8-BAHtkFm8yfugdeTd6Rcv94fR-pXXb11Yd8G9mGPTee6GBOfPSP0VJIfqe96BsI-XR289dJsWduZ2iniiUrdhLglv8_3Wl5UqKfv-5O0jai5yZz9awgtS2JriQtSepCbiii8dm4x52MPXPgibDzqSF8BVEAYMEzqCHKcr4o4wJ1Nvm3BOzfcZkZf4Jn28Z0Crv4yr8HC340b4DcMdiuGwDwXsoHfG2CCWYWtp6WA-0dv77FntiAt4JcFwgSLfsul3npUTFSZnRH5PxQ0OU-Sx3gx5yqkSodavwD9rORLtrnr96CpU3Lh7FYGYYArJYL8dyFVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnMHc-T8cXaYrnfXQhHhMUre4HJ2ZiXWqKDjGvLljQy0p1vUCi4JXE4jKYmOVfU82HiSy0HOUXgshHGkEPCxYNZ0gqlphsmj4JF_Spxes2fdTlsea_jKdjUNSkV9ePpq7bjf6lH1nzbW1grw4LyowRhFuM3leVeM9aFzzbHJMz-akhD9c77maSFR_0VL3wFQBGtg6wafm2czN1N3wmzVEU2raSj_HK7uu4OVVGOubB-4TeaE1roE3Nvs7XuDN3WMeyKOdF3ocRzVKpOVjvlEDHj39hUjdD6ViIMBSTL9wqJ8cFpUI_OwqPLsbxiNEDf05450u1CCNbp_XEOutfqvng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2981">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⭕️
دفاع وزیر ارتباطات از گرانی اینترنت: کمتر از بقیه کالاها گرون کردیم!
ستار هاشمی، وزیر ارتباطات، در صحن علنی مجلس در پاسخ به سوال نمایندگان درباره گرانی شدید بسته‌های اینترنتی، از افزایش تعرفه‌ها دفاع کرد و آن را با سایر کالاها مقایسه کرد؛ پاسخی که در نهایت نمایندگان را قانع نکرد و منجر به کارت زرد مجلس شد.
⚙️
محورهای صحبت وزیر و استدلال‌های گرانی:
🔹
مقایسه با تورم سایر کالاها:
وزیر ارتباطات مدعی شد طی ۵ سال گذشته، با وجود جهش ۲۰۰ تا ۵۰۰ درصدی قیمت اکثر کالاها و خدمات، رشد تعرفه‌های ارتباطی کمتر از ۸۰ درصد بوده و در نتیجه گرانی روزافزون اینترنت مطابق واقعیت نیست!
🔹
عوامل توجیهی افزایش قیمت:
افزایش هزینه‌های ارزی، مصرف برق و انرژی، هزینه‌های نیروی انسانی و نگهداری زیرساخت‌ها به عنوان دلایل اصلی افزایش تعرفه‌ها عنوان شد.
🔹
کارت زرد مجلس:
پاسخ‌های وزیر درباره گرانی بسته‌ها و عدم توسعه فیبر نوری نتوانست نمایندگان را قانع کند و به او کارت زرد دادند.//شبکه‌چی
پ.ن: می‌گن «چون بقیه چیزا ۵۰۰ درصد گرون شده، اینترنت رو ۸۰ درصد گرون کردیم.
جالبه که هیچ‌وقت کیفیت خدمات رو مقایسه نمی‌کنن، ولی برای افزایش قیمت سریع دست به دامن مقایسه با تخم‌مرغ و گوشت می‌شن. کاربر الان نه‌تنها بابت همین اینترنت محدود و کند پول گرون‌تری می‌ده، بلکه مجبوره‌ ماهانه به اندازه همون بسته (شاید هم بیشتر) پول فیلترشکن و سرور بده تا فقط بتونه به اینترنت آزاد دسترسی داشته باشه؛ این هزینه‌های تحمیلی رو چرا توی آمارهای ۸۰ درصدی حساب نمی‌کنید؟!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2981" target="_blank">📅 17:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwY_8v3VeKBnoTwvm7XbivMZCd60uNHDU9JZBaSidpQlEwEZTUohJDtXJgnUBP93JKsIWPGURky0Fh2YUtTTtJGDP24GIZ4nmrhiX_8FMociB4SH-PziqhK_XnisJWPfPpGbAkWzD_bkrIYTxAai_T56C1u3wQpbjWax68ITQZ9DikJpuMyR7mypPKOSFk812WubEBXsuiDklOVJVj2V6LJqdtM53qRmKSz3y7vlIvZvNROQr5eGKWuXj05obiZae52IUiY0-ARrGkU5RpRzd-5biEGhFenuekbLWs6oUwBMNwOZr56krXqRdsDkAnnZH5Khn4rN5GKYdgPwuzt-tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7bAmLw5Tq_gcK3FKksa-7tqVNF5UlDS1vmFMz29ynhXFMbOvtpnbyLdW3bnhAeyzuhPzrDBs0QIAepAwdzwtrHD2pgshEHPjDUi7O_onAhlkgfGjH6yPQhDq_Ls-tSci4trRouoxs3o2SKw7dEIsJelaoi1_UeWFhrXjQEZjb0Y3vloAUmLNAEC1rjB48K3E30qD86JzaSe9_LOqNyVhnWvKEY7WGwP-ZD59lAJp0n8U_o-OCEx4OVbGzxpSPIthtvqRIj08VcgbOheTsqzfw-7YxTh34_axFYRkM-PI9MLEXf_k0x2te61lyC9xpeybPaHUpMHrres8lyRaAVZlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2977">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWbCegMNdUXGXfAdgL1K29hkYK0UnMv2A6DaV9FuYrS0Wch3ufIdb1l2zONbkZ8liHHUxZSzyj2zWHAYxwuo6AsgFvdy9-yeuBukA1BLxTSl2d-VkvhWqfRYDxid0hPdL91x-6CrzyeuSoyJtfgaFCr6nqWE0T6Ekt7tk-gmXg6G7zBi-_dDuPEtYonRH3Aa_d8jIJPeGcRRcu4SZvenHJ9vSFF1r7PYQiEsIrHAQ-XZ63yXFA-pZVc9Ch-NpSSzjlbHg6eG1d77nhaOUb35TS0qc7MSC-HEo2DNpen8gNUa5HCPUEvc7o5Mqlx0d26cDAg7IUdZi6zU5Axnqi1LuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بحران لغو گواهی‌های SSL در شبکه بانکی ایران
🔸
تحریم مراجع بین‌المللی صدور گواهی امنیتی مانند Let’s Encrypt و Certum علیه زیرساخت‌های ایرانی، سیستم بانکی کشور را وارد یک بحران امنیتی تازه کرده.
🔹
تغییر آدرس به جای حل ریشه‌ای:
برخی بانک‌ها (مانند بانک ملی و بانک ملت) برای دور زدن باطل شدن گواهی SSL، اقدام به تغییر دامنه‌های اصلی خود کرده‌اند؛ حتی در مواردی بدون ریدایرکت خودکار یا اطلاع‌رسانی دقیق، که مستقیماً کاربر را در معرض صفحات جعلی و لینک‌های فیشینگ در گوگل و شبکه‌های اجتماعی قرار می‌دهد.
🔹
عادی‌سازی خطای مرورگر:
مواجهه مداوم کاربران با خطای قرمز «اتصال امن نیست» در سامانه‌های رسمی بانکی، حساسیت عمومی نسبت به هشدارهای امنیتی را از بین می‌برد؛ کاربری که یاد بگیرد این خطا را نادیده بگیرد، طعمه ساده‌ای برای حملات فیشینگ و صفحات جعلی درگاه‌های پرداخت خواهد بود./دیجیاتو
پ.ن: اگه فردا روز دیدید یه «SSL ملی» راه انداختن اصلاً تعجب نکنید! چند وقت دیگه میان به بهانه تحریم و امنیت، همه کسب‌وکارها رو مجبور می‌کنن برای گرفتن درگاه پرداخت و ای‌نماد از همین سرتیفیکیت داخلی استفاده کنن.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2977" target="_blank">📅 17:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbU4Yi7nrQCofKiy4tzQSJuThhqzR08DiklK146GPPQ5OuLm-z8NcpzUizm_CX6BIoP2yej3nNCDDhQaZGQSGRdkDpxvrE32boFj_2DqLFVPgNTcWBVgzQxyAYAeNvqSLVVMM63qTj4cyFTNmvu8oLvv0NIGQBnRCc8uOe5M5zqQgMuVKcLrz5Wr2qn557z5Qqi7mGwKPMpsBu8wACoLPtSoI-AXDS3anGv-43V58ubzaxPmBKTXv9nBSBusmyyRgQuK8aDd5nMTV_yZUuYIsehTeMXtN_o_NPGT97QqmHPJPiEU7DL7PoIVxVGOa0Ex55zzkZAczcmGBUOin4d22g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=knf-HakwEwvTvlqQoMtYG6nbsYwZsb_CZJrO9Zhmy_iwaWKPnEa7bOv0LJZfqTDMUBCJnUUpbaz_44MHLLDyp4eqDDD3ifmoFUaU3yHXoxKQyMB43duBsAe6T2kmINQh_DUJIeHHcKksUk1IxLr5XxBVgENUn5vLO7TcsrocNXeG903DMUUddhbXnKF3nkLhqRP4fRxtGqUVosuRwVW0-g_sbYeOtwGZFWoDEGj20Cu4YXFUpclX-8WkKKiYxj0oqPO-G964JxncKQTPnGdCbAJWvAkHeJI-cN15m5uZ_j6KDAscNtbINCTwVgHq638deSA3S1gC9oXm2AyBERhRdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=knf-HakwEwvTvlqQoMtYG6nbsYwZsb_CZJrO9Zhmy_iwaWKPnEa7bOv0LJZfqTDMUBCJnUUpbaz_44MHLLDyp4eqDDD3ifmoFUaU3yHXoxKQyMB43duBsAe6T2kmINQh_DUJIeHHcKksUk1IxLr5XxBVgENUn5vLO7TcsrocNXeG903DMUUddhbXnKF3nkLhqRP4fRxtGqUVosuRwVW0-g_sbYeOtwGZFWoDEGj20Cu4YXFUpclX-8WkKKiYxj0oqPO-G964JxncKQTPnGdCbAJWvAkHeJI-cN15m5uZ_j6KDAscNtbINCTwVgHq638deSA3S1gC9oXm2AyBERhRdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEleV6MHteHNN7EuO66Bm3ZSHdVN643Qcyiye2PmOD099_3znRkm8huF9xQBNDswflrYumgSIZeDMPxRihkV-cCpF0FB9PCxJot1qwjhkC-OV1Y_8yPgWnNPoXhUddZCwa9MnX9n2f0hlYOfetN_bzfvxdaI8Q5OqrZtTSQ6oDMbMz3_MI1VYMSlaRFPP9gDvZKKUulZQcKfkANWaZYcXHrF3Uu5nRwMSOZLC-OkXTLeLfqz-0INF3l8WYVgFzM99dcxk8kiG3g7_vOsgOGpRfT3a5AaXcH3nWWlUx43RM-JWEc__6nq1VE2tpUHEtuy3IV3Mm2BZ0rQrjU7LufvMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6GPLYC1ox_T-dPRkfA8UFXrsA6Z0DNkAAqsRoY1_gJy7UTrd2-ID9nEttPBd3ijPu7ygoIt02b78Hk5BcBb5SjBQsvP51IFl22wYFCd7AD77S8EJWWKpUfNGP5WdAxRegRElARMASyDejaL1WnW91LCCKbJgxrgSarOohC9ASU1kGuAt7E6e63-zN_X72ZgEo6ZJKzJ4k2mX6E9tAvlw7EZqLAvChJ8qfueNtmlRnHoXvOAzQqlHoPaDlyEG6qY4BTIb9VA4ZFwM_JKw8j6bU6dUeKWEWzg4Vlh0VYuSU3Itzy76g2JeCx4ygZWfUFIgm8Pnvhy4w9GW4c5vJhQVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL_-LpizYKNeqlR6tt1yuoHXbFleve0zhaQLx3MF6D2pxmOflLBwVluxe-1PbgHO_I0gW5A34KXD1q6il_A_NcSZkx2ExWt94t_OxxTqIQddklgFNn1vFz0eti30285ZBAv5a-bJvPwk1dE8CEbie8h8lCYupCX9NYu2p_9wH2Yvcw-hnNYY0FGhwnSpq6t39jj40wTeH38uNJtOysH17sh6BsxJACyw9OmqByuqRiqV_H-Q2ES2JDjScRC_RVFFkvs2P0gzUcfenFMK7KAot7UcneUFLGAiM6Hc-su3N3Sorn8GZ3M-PYTqTMaq_Mot7y48quIiltLDUHAOHTrTkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j09LV_9XVH81cY1HCbrG_3Dw6Kd_sAkPsFoO-Ijo7WDYGC_4mn0liznkTGEKNysgr68U4-K7QVQYWKjsoCpVJ8o-QFvjkf-2XoRNE4K8xnyduwnQbh4iozE9uYwwzI3HePXrX97MOc5V8s3EBUbrmAusFNiwbfvmLod6ggkpYAu578Ih3MHsCgtb-pWV0CqxNGtMZlHdtbyVrQG9gGz9laX9xomdGtdrd5cwIlYTQ0xaa6jC3dKVeoNJP1ka22_FSbnrysl24cPKd4MaiWWkJqWf3JyKVrFzCFXqQgElqwBgBZmLi1fZ7K9ZzMADTI6Pk-hn_JqooNObXpvNLkZuQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=RFsUjmz1FoH14lsGst2ENApKoSUdGWGaxGdfjS170LxXzZ-N6Ug3zRoGf7j-LS0CQ0k38nDvZA2plSmrrfI0X57hIhy1yVw3SybdI103oZ4Wn_M2J_OkE2t-Fp8M4OvC1_SlSkr_n_xwNwseqEmfOXdXTXsRJVC5vxuNLkwjupcSQLZE-290VlAhVb0yCch6fdx8faC5FGwMsQrWY1-V3GcgRsXKLXb4uItxoYeKLS7smKqb9io9rND14sV9e-W9wAtl3ABwWsa8bQlhyCJk6AsPlQQ9WX8LSCy3aboEMYdrEzpfShB0TA2iCcFasK_Wil2OHvqpEGxNbSTH3IZhGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=RFsUjmz1FoH14lsGst2ENApKoSUdGWGaxGdfjS170LxXzZ-N6Ug3zRoGf7j-LS0CQ0k38nDvZA2plSmrrfI0X57hIhy1yVw3SybdI103oZ4Wn_M2J_OkE2t-Fp8M4OvC1_SlSkr_n_xwNwseqEmfOXdXTXsRJVC5vxuNLkwjupcSQLZE-290VlAhVb0yCch6fdx8faC5FGwMsQrWY1-V3GcgRsXKLXb4uItxoYeKLS7smKqb9io9rND14sV9e-W9wAtl3ABwWsa8bQlhyCJk6AsPlQQ9WX8LSCy3aboEMYdrEzpfShB0TA2iCcFasK_Wil2OHvqpEGxNbSTH3IZhGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYAMStjQWulckoSJehj75OTuLmDleTRjmV6xXoJlZ1gNTe1AU2rdHnzhA4thsEornAjzLrItFeZ7-M3TKa2UBwIYu6f3vSKiL2VJfXr6mDy7emnL8nKkLF4l78aEzZMhFxWkcVJT8FOzPLX9jyi_t0lJpKZvUcNUPEf_AngdCOZg0SIeQz4Q51azrlszWqh3PoVz5Nbsl0Yrgwv2UrKU6fec5otYHVDVPKPWNNJuQ5vitHvyyOiLKiyWAxnpoQgohx5MqSpwD1ipsgmZmbPuCD2Fcw84c5V0hlzFklQiwaUodWcnEgnY8nb3Y2h9jJX3AQG8QDdq4-G0D0DSuTRIaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niRAQa8cCTznEn28LmvR7bFJ96s8zcdwHIW2xe71jwcES5wvDCl-gC66a_MACdWLltDaN1q3mH7OgM_srikKFKg2BSOjBe5KRc0IQG2SVDFRk1kXMkogbBzGwTlMD3sCwdWxa4sfvBMD-oO1uHV5EVcvMXHfEMYXMlsukzpeMrWU6WxL9PjrlCzX1MhoLpNzLt6K7X7-LJPdQymS2xcAZGbcjhwiNl1VgdQZ6p32GCrPxD1Sxju0hzbHJryeJp1fbQcT4aGDS-U65ge7oaFGnAv4jzKrDoaOLyqLGv4qYmsPhGXsP6dCt-LbRXCUde9u4MxJkJqZb7CWjzGcizNjoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2960">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQWQXCHhlRk-2_Kesz6l7XaVQzY37P5mRNPsn0evQz4XHgt8VkGlsAxjqSbRFu_bseyQVe2dSa_fcC9SpYlCDJn637ZMhovf_BXOR9oAvAPEPwVm2bNAJc6GgsXpjBM5OSGTNoSvv-_j5DZH6G4UXNf7WfCXWfMUbj_0iJ4Z4N6Rw5tT_c1-bJXxSKBV0Ud7I-WG22s4uUd-520dj-0nBfAUnBSHX4BRmFA2ImVxGwZcbxcW2V5f7bFatEoJIXwRT1jW6WzcqZtaOdB6eejmxt9l5yaJ5NxpSIfG0TZTS6gTxHD6MtSaifY5kxkiAiwzeGW3ZsVMOhIMyfi0NnlyBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
توصیه بابک زنجانی در الکامپ: گیر کلاهبرداری نیفتید
— بابک ولمون کن!
— بابک خجالت بکش!
— بابک حیا کن!
— بابک شعور داشته باش!
بابک زنجانی در قالب هلدینگ «دات‌وان» (با ۲۷ شرکت زیرمجموعه) در نمایشگاه الکامپ حضور یافت و از چند پروژه رونمایی کرد:
🔹
توکن و بلاکچین «دوتو»:
وعده پرداخت کوین به رانندگان تاکسی اینترنتی (بدون تاییدیه بانک مرکزی و بدون لیست شدن در صرافی‌ها).
🔹
سیم‌کارت و شبکه اجتماعی:
معرفی اپراتور مجازی «دات‌وان سل» بر بستر eSIM، پیامک انبوه و پلتفرم «مای دات».
🔹
پلتفرم معاملات طلا:
ادعای عرضه طلای ۲۴ عیار بدون حباب با ۱۹ لایه امنیتی.
⚠️
ابهام در مجوزها:
بانک مرکزی پیش‌تر اعلام کرده بود فعالیت‌های وی در بازار طلا و ارز فاقد هرگونه مجوز قانونی و نظارتی است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2960" target="_blank">📅 20:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzOxTgW2bR3y6nuKxVy2WqxLurJmGT2dolFsUDcFbnigStq9Rs7l6UYUQgNE5OVCROCi3eWViRTiWH7Bn2sV5M3qYiyXn-P0agZ35Qt42-G3HJtOm1XoyHuEU2WcjNhrssYRSyuN25q2Nd8GjBDtuYWxXVNXB6X237y6MS1o74W1_77joQ8yFDwrZuZcu20_FOy0--EFdm8-dc3vaiok7YGy1ApMFnoyFGtaOEW1DZ5xaCZa1qbKAZzjsoYT6BRTDJICna_nHjGWguA7znJTYYaxwEepcv8KXUIVil7tkvM3IMAUlY_nvmgqukPF8uqCVErqdL130Nkw-n46TNKQ3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⭕️
قیمت آیفون ۱۸ پرو و ۱۸ پرو مکس لو رفت؛ افزایش ۱۰ تا ۲۰ درصدی به‌دلیل بحران حافظه
✍🏻
احتمالا با این وضعیت دلار و سودی که  دولت بابت ریجستری گوشی میگیره که در اصل یکی باید برای دولت بخری یکی برای خودت فکر کنم بالای نیم میلیارد پول این گوشی باشه تو کشور.
😐
بر اساس تازه‌ترین گزارش مؤسسه پژوهشی
ترندفورس (TrendForce)
در آستانه رویداد جدید اپل، پرچمداران سری پرو نسل جدید احتمالاً با افزایش قیمت ۱۰ تا ۲۰ درصدی نسبت به نسل قبل روانه بازار خواهند شد.
⚙️
پیش‌بینی قیمت‌ها و مدل‌ها:
🔹
آیفون ۱۸ پرو:
بازه قیمتی
۱٬۲۴۹ تا ۱٬۲۹۹ دلار
(در مقایسه با قیمت پایه ۱٬۰۹۹ دلاری آیفون ۱۷ پرو).
🔸
آیفون ۱۸ پرو مکس:
بازه قیمتی
۱٬۳۴۹ تا ۱٬۳۹۹ دلار
(در مقایسه با قیمت پایه ۱٬۱۹۹ دلاری آیفون ۱۷ پرو مکس).
🔹
آیفون تاشو (آیفون اولترا):
ورود به بازار با قیمت پایه
۲٬۰۹۹ تا ۲٬۲۹۹ دلار
و احتمال عبور قیمت قوی‌ترین کانفیگ از مرز
۳٬۰۰۰ دلار
.
🔍
علت اصلی گرانی؛ بحران و تقاضای هوش مصنوعی:
🔹
هزینه تامین تراشه‌های حافظه ۲۵۶ گیگابایتی به دلیل توسعه سنگین زیرساخت‌های AI در سطح جهان نسبت به سال قبل نزدیک به
۴۰۰ درصد جهش
داشته است.
🔹
هزینه تمام‌شده قطعات (BOM) برای یک نسخه پرو ۲۵۶ گیگابایتی حدود
۳۸ درصد افزایش
یافته که زنجیره تأمین اپل را تحت فشار گذاشته است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2958" target="_blank">📅 18:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsHIzfrEXTIGE8BUQZMgrEw-LFy31kkqF37k7QTGb34uiPPybuDSfZKIhH5PEfZBgCNJafFw5iCQODW5Jj76CIemIjXuKjqsv5klx_EbZhYNnq_yZATHjjY-1jVaJKkyRBlmV5vzwywX9wMMe6MaLCTk91PGGEHHnUWGdHXv66E13NWjrIJR3qTQL8onfy-wptTpH6Tz6597u9M4vdNSUKv0ATt7D5OjezIixZJqyBom3HrhOzawmNrsT2l6pNLE8O2OMRV6sS0mIKCbeSL-ydKDydCU2F5p1beu3GdSic8xXTbAXyTY4Lc8fkD48OibVaSN6GgpsHN9OS0NTPm19w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3Go_yn_bX-l-32XmZgTa_45wvnTrF7McylJUDJpyvoJS_vDuWLaxj_2IQQA7GSeN9cUQPYddrd0C8ys2kHDCJaZyPVx7JpHYRL2Y2ZcUCi6btbwQFjgBoioRpfrjVxkYtujlLtgjfVBlsibu3wc9q2ILGdKSYAAmKhnCDb2xWyruuXIHpRCmFRtW2PjfIcjpImeryPSuWJ5VGfQa4iO3JEOJyG8iTpD1cld27WP6HxS1wAjroA7b2ORc-4IRWgMdNGuhYBqLENJfyWIy3oDXpKQNkbT6ORCKxh2Pxip7XU1V6kY0W6oBfUyyoSzcWjwZLLXiWJXj7x0OSsZhf3R2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY6InIrbbKJZ0pWd0RsDf7g9bBJULd81gfyK69M55cDnlwt2m9H2pWyEnFuNNVLJXIYr-2KFjc71fwgGbA63oBls3rke0YvtoTzv2-4O_SnvMHLIprrVuCt_hvOFMzBuN-I7KyHQOv7J4YWkNxe_7URYduPWiHdIuTkqsf5ohW5pu3-6g4dbLfeUVCxXjbiWqyAHvaH9XcEgR02J6bQuuVOslanUowRzzmMGhFRLkRDOM5yGURY4yD2XwiZTjElqi31T2H2XdIGrNXL6mfSYigXJ1EyW6tOpSkdjXG6Xg7GvCY-Oce_bg4HBXT0VwuEp4oESEpEyD34NMb9-nhEKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنتر ها است.
در این طرح شماره موبایل + شماره ملی + آی پی به هم وصل می‌شوند و بدون ثبت آی پی در سامانه شاهکار دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©️
Saeed Souzangar</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/iaghapour/2951" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2949">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgpqTb_f0VZvXPJfALfyg28KQMI3525oa0ZpfBVbeQKblzrXXmU6XkcDz4NQ23BrrbklTHnmOvt7hf3l8V0DoqgByMwzOXEDnMXq9aUp1ol8_Z0pvtz74BLLZfMlF_SyAQd8pH1ezpdUTbXK4_2xbKRYITo1OnebHZwVRaJdrnNcMp4nVfB_uY-xkB4TkLXxaGrGNWm0JCM5RGHOWHQANU8UJbL62Yo-poDUKtAH0gZJgiYGDRtSjFGhZ6v-LyYe2BVU-KBpAy4HN4aVRRL18z2fnWuo6SOte9tcZDkX5p9JAMUn3WY9Kq_Zwm7BjzUNsvN8zLKLgVXD328Ie_j3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معاون وزیر ارتباطات: گران‌فروشی اینترنت احراز نشده است / فیلترشکن‌ها منشأ اصلی حملات سایبری هستند
محمد حاتمی‌زاده، معاون حقوقی و امور مجلس وزیر ارتباطات، در جمع خبرنگاران پیرامون ادعای تغییر حجم و قیمت بسته‌های اینترنتی توسط اپراتورها و چالش‌های امنیتی شبکه توضیحاتی ارائه داد.
🔹
عدم احراز گران‌فروشی اپراتورها:
علیرغم دریافت گزارش‌های مردمی و بررسی اسناد توسط سازمان تنظیم مقررات (رگولاتوری)، تا این لحظه وقوع تخلف یا گران‌فروشی بسته‌های اینترنت اثبات نشده است و نظارت‌ها همچنان ادامه دارد.
🔹
فیلترشکن‌ها؛ حفره امنیتی و اقتصادی:
استفاده گسترده از فیلترشکن‌ها به ساختار شبکه مخابراتی ضربه زده، باعث نارضایتی کاربران شده و ریسک‌های امنیتی بزرگی را به کشور تحمیل کرده است.
🔹
منشأ داخلی حملات سایبری:
به گفته وی، بیشتر حملات سایبری ثبت‌شده در کشور از طریق بستر همین فیلترشکن‌ها و از داخل خاک کشور هدایت و انجام می‌شوند.
🔹
محدوده اختیارات وزارت ارتباطات:
تمرکز این وزارتخانه صرفاً بر اقدامات و مدیریت فنی است و ساماندهی کامل این فضا نیازمند همکاری نهادهای امنیتی و نظارتی است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/2949" target="_blank">📅 21:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPD3IdgIdIGchtedKqC8Z5iNCaY9fO31NPl8m79bLXEdcdFyENiIJE2-hWRCIIzbueFFt8j_H0qAa7r6Zz8v2ZQ0aaMsawKlnv6iSvi4MFimEgw73gCib1Y1Y6154tYJPmybJZdAmqvCpxbWrM6hj2sexQvbrsKddbj5P1Ac2lAUwBsAL1WD1EuOP-4pRl-831fzw9B_OwFYSZmqPpiaLKjU9G5QHKAgYTHPSExJjfOQsa0FuqyeuufMAqEh7CeIXdi06Ih9eP-wg3Zqwr1ixArnnHVVNqnl0-gPxLwwW5Jrw1zYaxa7GsRx6cVfbiwCnVieF4QWMKbZPGQLFum4PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2947">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⭕️
موضع دفتر رئیس‌جمهور درباره فیلترینگ: دوره محدودیت و اینترنت طبقاتی گذشته است
سید عباس موسوی، سرپرست معاونت سیاسی دفتر رئیس‌جمهور، در گفت‌وگویی مواضع دولت پیرامون رفع فیلترینگ، اینترنت طبقاتی و فناوری‌های نوین ارتباطی را تشریح کرد.
🔹
پایان دوره فیلترینگ با پیشرفت فناوری:
با گسترش فناوری‌هایی نظیر اتصال مستقیم گوشی‌های همراه به اینترنت ماهواره‌ای، سیاست‌های اعمال محدودیت و فیلترینگ دیگر کارایی فنی ندارند و دوره آن گذشته است.
🔹
رد کامل اینترنت طبقاتی و تجارت فیلترشکن:
تداوم محدودیت‌ها در زمان صلح، ایجاد دسترسی‌های طبقاتی به اینترنت و شکل‌گیری بازار فروش فیلترشکن به‌هیچ‌وجه قابل قبول نیست.
🔹
تفکیک شرایط جنگی از زمان صلح:
اعمال محدودیت‌های مقطعی ارتباطی صرفاً در شرایط اضطراری، بحران‌های امنیتی و جنگی برای مقابله با تهدیدات سایبری توجیه‌پذیر است، نه در شرایط عادی.
🔹
رویکرد پیگیری رفع فیلترینگ:
پیگیری موضوع رفع محدودیت‌ها در جلسات تصمیم‌گیری بدون ایجاد تنش و بر پایه اقناع و وفاق انجام می‌شود./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2947" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=AJAI3rIwlWz8N1KCTICoEOwpRFdeKQ025srgMJvio88D_syPgi1onbZxGNMnOM_I1_GYmYjAD0CIJvogm5L_YqOtSOcMiacgmMPpjT_jTMa0NQZeZEhJqkzptDacV2V5oR8_zmRsv9vnW_qiGtOgNlGWoA7XVi0R02lwkYXxU7NXvOi7bAzuAsU9DclxXwXzz2x1CnfwtpXwGqr1A2CDpUgp12RMtc1QmkW8vHxa6AdDa36-6fT7jmzasi8YkfipfpUug2k6CC6-6HV9eQSemnn3fr9qytgdpqdYh6NAnAKVL3wuNz5cc0m3XhIkDv4NySchVvf235Q87ysZvFY94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=AJAI3rIwlWz8N1KCTICoEOwpRFdeKQ025srgMJvio88D_syPgi1onbZxGNMnOM_I1_GYmYjAD0CIJvogm5L_YqOtSOcMiacgmMPpjT_jTMa0NQZeZEhJqkzptDacV2V5oR8_zmRsv9vnW_qiGtOgNlGWoA7XVi0R02lwkYXxU7NXvOi7bAzuAsU9DclxXwXzz2x1CnfwtpXwGqr1A2CDpUgp12RMtc1QmkW8vHxa6AdDa36-6fT7jmzasi8YkfipfpUug2k6CC6-6HV9eQSemnn3fr9qytgdpqdYh6NAnAKVL3wuNz5cc0m3XhIkDv4NySchVvf235Q87ysZvFY94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2944" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M94PUjpLDpvFnOORUc6PEdQbs8KkIc_-dB2d4KtPRVf3bCzTRcJKMFp_UgrUvWXC1YTAQPTWTGAVHgS6n6S2kwyWC2Z1qIdOjCKQzeoYpOANS7jDJdkzNeG3UU_yeNQZXlUmFcK4UJvzdgJxnNArEnKYmLeX3VTkp6j3VbQJ-pvBgWGHqwswCSk0yefCmGdqAzJnWgjGMdAr8hYNmq4lP02N0MkKVNnlUWjCVA_NO_IykCuatHZz1_1wIIDvyZpYecfJZHkbUj9y_gkJkA8mF5jpT0HeeaCn5RuaLCmvnwRjaSrxyxfmlF1k9ptKxWjv8TPkd8-xXepXSvCPmGJnIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeK6GIrECKLJvyJcDSy-SOwNn6btRSE-0obRaEQD6kKufFgaDLhZm4MPcK_ax5y5j5VVCapiQZKFeuQgwuqxigpYtT2oUELTpSOHeZXBooirUvSbHuZinBy4dmN0vJ-ychRScsFwx0KpcAGO89_tL0ZKdbUYbP4bkmRXwb62GafwVu3NMo3S9INv6xFep9h87i7z5-TVUrSMFTvbL81hB3tjKm8Z83ppa76Yc-yzI75X7jtYCd4InFimVFa2RV8wzoaMGje_T_g0NbzyFPrR9VON8KPbTMAMTAorO4SoY7GXFvv7VZs2wzfOaZpapjzN7kEf1MIMc-yRnAqzHizQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مقایسه WiFi 6 در برابر WiFi 7؛ کدام نسل در سال ۲۰۲۶ ارزش خرید دارد؟
با گسترش روترهای
وای‌فای ۷
انتخاب میان خرید یک روتر جدید نسل ۷ یا یک مدل مقرون‌به‌صرفه نسل ۶ به یکی از دغدغه‌های اصلی کاربران شبکه تبدیل شده است.
⚙️
تفاوت‌ها و مزایای اصلی WiFi 7
:
🔹
پشتیبانی از فناوری (Multi-Link Operation):
ارسال و دریافت همزمان داده‌ها روی سه باند ۲.۴، ۵ و ۶ گیگاهرتز که پایداری ارتباط و سرعت را به‌ویژه در محیط‌های شلوغ به اوج می‌رساند.
🔹
افزایش پهنای باند کانال تا ۳۲۰ مگاهرتز:
دو برابر پهنای‌باند WiFi 6E که برای استریم محتوای 4K/8K و کاهش تاخیر ایده‌آل است (در مدل‌های پیشرفته سه‌بانده).
🔹
سرعت تئوری و برد بالاتر
و
سازگاری کامل با نسل‌های قبلی
دستگاه‌ها و تجهیزات قدیمی.
🤔
آیا خرید WiFi 6 هنوز منطقی است؟
🔹
بخش زیادی از لپ‌تاپ‌ها و گوشی‌های فعلی هنوز از پهنای‌باند ۳۲۰ مگاهرتزی یا سه باند همزمان پشتیبانی نمی‌کنند.
🔹
برای کاربردهای روزمره، استریم و سرعت‌های معمول اینترنت، یک روتر باکیفیت WiFi 6 کافیه./شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2942" target="_blank">📅 18:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmer0poRJqHQ3RO3N1VRykxN4a9ZgeHGO2AR3E5ObDouyOoX40xKuOpkWnGQ3WLlv1OzAzVg1fqs0xXAFZoIAsXek_x3lXdHqaB1vQyRhpMSMslJS0mvkxdZQj8GbC0eKRmhvNy1mDAUFiNYOsL2-v1AejnM0jYFVI5QeWKlOo9I61eQh3-9S6qLhhG3I86AGtF26-KEECTKXNpNzVUv_rlRaMmOGde8sOvwzAMTID3gp_osYoQ-V4cCpAlhsVxpSfv0ggQXEmmR0SEZYlElefBF7SHQlu0UT1d6YbP_Or_aTtJDyWcHdRIN1EqmR0P1hx1aTkdjrBiOz9olJ_C27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
گوگل در حال آزمایش هوش مصنوعی Gemini 3.8 Flash
بر اساس گزارش‌های فاش‌شده، شرکت گوگل فاز آزمایش داخلی نسخه پیش‌نمایش مدل جدید
Gemini 3.8 Flash Preview
را روی پلتفرم کدنویسی اختصاصی خود موسوم به
Jetski
کلید زده است؛ اقدامی که از احتمال انتشار عمومی آن در آینده بسیار نزدیک خبر می‌دهد.
🔹
پیشرفت چشمگیر نسبت به نسل قبل:
طبق ارزیابی‌های اولیه کارکنان، نسخه ۳.۸ فلش عملکردی به‌مراتب بهتر و ملموس‌تر نسبت به ۳.۷ فلش در سناریوهای مختلف ارائه می‌دهد.
🔹
تمرکز ویژه روی مدل‌های اقتصادی و پرسرعت (Flash):
در حالی که مدل‌های سنگین پرو در دست توسعه هستند، گوگل تمرکز اصلی خود را روی بهینه‌سازی مدل‌های ارزان، سبک و پرسرعت سری فلش برای کدنویسی و توسعه دستیارهای هوشمند (Agents) گذاشته است.
🔹
سرعت سرسام‌آور چرخه انتشار:
پس از عرضه نسخه ۳.۶ در اوایل تابستان و معرفی نسخه ۳.۷ تنها با فاصله ۳ هفته، اکنون نسخه ۳.۸ وارد فاز تست شده است.
🔹
رؤیت در بنچمارک‌های جهانی:
شواهد نشان می‌دهد که ردپای تست‌های آزمایشی این مدل به‌تازگی در وب‌سایت معتبر ارزیابی هوش مصنوعی
Arena AI
نیز مشاهده شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2941" target="_blank">📅 16:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAk5ErjZRRj8VE1IuoV3jUkz2jRYkkc7LcoHS03FBOocGSAjWYdhD2zkNFCJe2e8HJEUv9F4n_2fPwHbrWtIatM-aBX_fBWo7F-7YJ2sACZRkotqAvaLfQkjPc7lezY19XPhHcN_tQBqSRmisPRXc7Gwrc-EQ0qc0U6PL3E8VdXaQZ6LHGAEK4p9BX3q39RwAjY8WR2ILNJ4G0GvFLh7VgsYskZzo8y6iKO_tV4talgKqbkE0MUOB7qFHLx8W6prE0YYciA1arP9KeWxd-WOqtEDf1ux8efqxlXUMzBzdhnCr1SCfa8vO3NvZyM9tBXt7zl4o-JF3mUTRBDQ3Y5xJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTQdSbaPmG-imESw7kuJrSEIZ1EjOuXvYH0-XFlOXidT2dXO9i_ngWG7JGch7PXkp91Z7HhfP7cvX0P5vRPwmCN9HYZw7ZNIw_dz_J_NRrspZyc6uBiYZYEunjPVH1ue51KMHkkYZE_rBOUEpgIMwn4wLBbkD92_9XXEpPcJcdyDPLXKjdYH6nv0f380tiOvsJg17LhIaJZfGnbwsb2hjLomsTCxUpLDiHwhN7eYWiZi9EV15_Bhw67IRohRLgqwaK2UnLtIjY8YZfmo8hXiO9JqdthEsxBLw6FfkLAPfArSWdR8ZZ0jRBnsLiGwX6D2jV5L1CFb617MV2UKhoFXEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎮
فناوری DLSS 5 انویدیا پیش از عرضه رسمی لو رفت
تصاویر فاش‌شده از نسخه آزمایشی و اولیه
DLSS 5
انویدیا روی بازی‌های کامپیوتری نشان می‌دهد که این فناوری رندر عصبی هنوز تا رسیدن به استانداردهای مطلوب فاصله زیادی دارد.
🔹
تغییر رویکرد در آپ‌اسکیل:
برخلاف نسل‌های پیشین که تمرکز روی افزایش شفافیت تصویر بود، DLSS 5 با بازتولید هوش مصنوعی تلاش می‌کند متریال‌ها و نورپردازی را بازسازی و فوتورئالیستی کند.
🔹
نتایج عجیب و غیرطبیعی روی چهره‌ها:
در تست‌های اولیه روی کاراکترها چهره شخصیت‌ها دستخوش تغییرات سنی نامتعارف شده و ترکیب این چهره‌های تغییریافته با انیمیشن‌های حرکتی ثابت بازی، حس غیرطبیعی و ناهماهنگی ایجاد کرده است.
🔹
افت FPS:
فعال‌سازی قابلیت رندر عصبی در بازی Control روی کارت گرافیک
RTX 5070 Ti
در رزولوشن 4K، فریم‌ریت را از
۷۱ فریم‌برثانیه به ۳۵ فریم‌برثانیه
کاهش داده است.
🔹
نسخه رسمی DLSS 5 برای پاییز برنامه‌ریزی شده و باید دید انویدیا تا چه حد می‌تواند با بهینه‌سازی نسخه نهایی، مشکلات افت پرفورمنس و رندر غیرواقعی را برطرف کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2938" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2937">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6u1JgcrFSZbcXCi8l_T5iLyEhkAiDQeW5JhLCec-7qeJ7EznC_Tr88Um8boM4w8_HsHQuMgclUwLDRWQI7_8tPn0KdTXy93Nl6hFi9OuUqhnoJ636A85VjNI832KHUJVaXoR7nmJWL6V_BpmaiHXdJOKuKMXM2NfcqljbFguVE3gtrhxc4T-bDCrQvRNLST0XKABvqLX-OtfY0hv4fR0r5yI-d5bFEBS2B8Y1mkiP2ht871Tyz4BajcidI7IZaOfaxzavuz7S-ekt--WPTr7H4abqteOGDyhEBsBLXq4Uff2Sxf4qjA_WcWKuhA0ReZUVal-2wVgwsJsy1SySPC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
توقف کامل آزمون زبان دولینگو (DET) برای تمام دارندگان مدارک ایرانی از اول سپتامبر
بر اساس اعلام رسمی پلتفرم
Duolingo English Test
، از تاریخ
۱ سپتامبر ۲۰۲۶ (۱۰ شهریور)
، دسترسی به این آزمون برای تمام متقاضیان داخل ایران و همچنین افراد دارای مدارک هویتی ایرانی متوقف خواهد شد.
⚙️
نکات و جزئیات مهم این تصمیم:
🔹
محدودیت فراتر از موقعیت جغرافیایی:
این تصمیم صرفاً مسدودسازی IP یا موقعیت مکانی ایران نیست؛ بلکه تمام افراد دارای مدارک هویتی و پاسپورت ایرانی (حتی در صورت سکونت در خارج از کشور) امکان احراز هویت و شرکت در آزمون را نخواهند داشت.
🔹
تاثیر بر مهاجرت تحصیلی و اپلای:
با توجه به پذیرش مدرک دولینگو در بسیاری از دانشگاه‌های معتبر بین‌المللی، این تصمیم فرآیند اپلای متقاضیان ایرانی را دچار چالش جدی می‌کند.
🔹
پیشنهاد به متقاضیان:
متقاضیان ادامه تحصیل باید پیش از هرگونه اقدام، فهرست مدارک زبان مورد تایید دانشگاه مقصد را بازبینی کرده و آزمون‌های جایگزین (مانند آیلتس یا تافل) را در برنامه خود قرار دهند./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2937" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2936">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdRAIceQj2YNRyidx_f6E5r20zySUplMtlFcIsP3vgKK4-lcOlNKUNv4pT7yJ5SvBxM0xoaZmhMvA2h3rB1CyTHJdqRnJlWA_yWjwDyEQd3u3yOGFdYRcL_rPBCpJItFqPwelnt0aJVTUTEtTrcq7lTDMF19yI_T-BwyfhlyaIdYAf7NXJt36BcClWEKSVVeWPbk6exeh4Ji_TZq-OCkBcgs7kUarGFHl9sQ4dIIPSZM6DIFq2LKYScnb1xOgVnxTVY02tAkwIj0bhbfDjnNNPg0Z3hjz9drkg_zSnsgWR3xWuHXmzVpLhImCfR-qX-DxlXIxF1vOTyL4tg0E5Dx1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل مدیریت نمایندگی و ادمین برای 3X-UI
پروژه
x-ui-reseller-panel
یک واسط تحت وب مدرن است که به مالکان سرور اجازه می‌دهد بدون دادن دسترسی مستقیم به پنل اصلی، دسترسی‌های مدیریت‌شده و تفکیک‌شده به نمایندگان بدهند.
🔻
امکانات اختصاصی ادمین:
🔹
ایجاد، ویرایش و حذف اکانت‌های نماینده
🔹
تخصیص سقف ترافیک اختصاصی برای هر نماینده
🔹
محدودسازی دسترسی هر نماینده به اینباندهای مشخص
🔹
مانیتورینگ کاربران آنلاین و آمار مصرف ترافیک زنده
🔹
پشتیبان‌گیری از دیتابیس پنل و پشتیبانی از تم تاریک و روشن
🔻
امکانات پنل نماینده
:
🔹
صفحه ورود مستقل برای هر نماینده
🔹
ساخت، ویرایش، حذف کاربر و ریست حجم مصرفی
🔹
باطل کردن لینک اشتراک (Revoke Subscription)
🔹
مشاهده کاربران آنلاین و حجم باقی‌مانده
🔹
همگام‌سازی خودکار ترافیک با پنل اصلی X-UI
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2936" target="_blank">📅 14:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7Igf_AwiMzgfv3HQzZLX9gk83-Myb4yoZVYHjqoR2Tqk4Chb2FBSwgI3Sk-aySSLNnozT_jOQcX7uf3SSOc9Iu3psWAycUHcVNhlIbmcXkTWB6tT2YboJld-I5ldBsfMdFKHqRd-0XTIHPRznWiTgC_Yj3NrHcaKxFm4DbiAUqvbDbjNlvDu0NoPBZcWOwQXV9HxVuHXdF_lNEsJGfIvFXkTYvGuev0O6SQIiOpMbCRloMsql-Ki3ZIw_cIapgxN0Ws0NzIPvAuZgbnzOegAzxV-wmhvV0r9ciBXtl7g_1fSnT2GRMde1J1oHppOtBxyAKX9y1g3t5B4S-TrMsktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ربات فروش خودکار کانفیگ تلگرام (جایگزین ربات میرزا) + آموزش راه‌اندازی
🔹
اگه دنبال یک راه بی‌دردسر برای اتوماتیک کردن فروشتون هستید، این ویدیو دقیقاً همون چیزیه که بهش نیاز دارید. تو این آموزش یک ربات تلگرامی فوق‌العاده رو بررسی می‌کنیم که تمام مراحل تحویل و مدیریت رو براتون به صورت خودکار انجام میده و از تمام پنل ها پشتیبانی میکنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#ربات
#فروش
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2934" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2933">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERuOhXVp1B2YPZm4VE4VfBcw2yMbuzZlc5LseBUc8zP6y6O9uq1gPhKLgBseVAiAZO2CNVcmq1g9Mun-kUg8xkH0sAnGRDR6uuJRwArOSp7eEjSewb_ig66WYTYwZMCeuBl5DpO-RCIKE4-SeGfVebzqG4JDSK2jwNGk5MPkMjH-nsgfe6-D5YOlt07Om9Qa0OIzgsIfZQyWoaZ4Me87rD3eNqMYj2qkMTG1MlEKBqyFNQJdcvDRR03HzdSBs1pVQCf4R4-oYhNjwZ3DsB6_seTM6RvqLD9fhzf_u7Ttt4BzlvqhnM641VV6yZAl1rHq_UH_szVOEdU3REJz2SUWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شناسایی شبکه گسترده افزونه‌های جعلی فایرفاکس برای سرقت رمزارزها
محققان امنیتی شرکت
Socket
شبکه‌ای سازمان‌یافته شامل ده‌ها افزونه مخرب را در مرورگر فایرفاکس شناسایی کرده‌اند که با هدف سرقت کلیدهای خصوصی و عبارت‌های بازیابی (Seed Phrase) کاربران وب ۳ طراحی شده‌اند.
⚙️
روش کار و جزئیات این حمله:
🔹
جعل هویت کیف‌پول‌های معروف:
این افزونه‌ها نام و رابط کاربری ولت‌های معتبری مانند
OKX
،
Rabby Wallet
و
TronLink
را شبیه‌سازی کرده و بلافاصله پس از ورود اطلاعات توسط کاربر، کلید خصوصی را به سرورهای مهاجم ارسال می‌کنند.
🔹
تغییر ماهیت بعد از جلب اعتماد:
تعدادی از این افزونه‌ها ابتدا ماه‌ها در قالب ابزارهای نمایش نتایج زنده فوتبال و بسکتبال، تم تاریک، پسورد منیجر یا وی‌پی‌ان فعالیت می‌کردند و پس از جذب نصب بالا و امتیاز مثبت، با یک آپدیت مخرب به بدافزار سرقت دارایی تبدیل شدند.
🔹
ابعاد کمپین:
کارشناسان موفق به ردگیری ۷۷ شناسه مرتبط شده‌اند که مخرب بودن حداقل ۴۰ مورد آن‌ها به‌طور قطعی تأیید شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2933" target="_blank">📅 15:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2931">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwEJQTx9eb-vT9HLpBK7f_hbv-httoU8ZkhfO7c2CyGBPTXn_aKuZfR1TgrgYvHQ_ola0Ug4O8Et2uaes-zqIbmzHVpqB6NSBD-t7va0uTI1DDJKI0_a9PJBR1tLJF2idtdiVReXcMfvKYVql35u1i9egPSL5B1JK8VzFM8guCPf73MAe4vbho_qjuyKPllRzBoVONs38bsJaHkIlaUXJ_71LJKAH5jS_ubSAfkdy_iKVamfPYpFWAcG_rFNeFgk5nGWetVpKQ-5m69mVpTPySw9T0OAlR-PVjPLM-LNNGqO4oiWSKjAWtjJFKTSEYb04M79x3wunQJuh8PT0LBaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
لطفاً برای هر ایده ساده، اسکریپت جدید نزنید!
✍🏻
دم همه‌ی دوستانی که توی این یک سال اخیر با کمک AI اسکریپت‌های کاربردی نوشتن و به بقیه کمک کردن گرم. ولی یکی دو تا نکته هست که باید بهش دقت کنیم:
۱.
فورک‌های بی‌مورد:
لازم نیست هر فیچری که حس می‌کنید یه پروژه کم داره رو سریع فورک کنید، بهش اضافه کنید و با یه اسم جدید بدید بیرون! با این کار فقط کامیونیتی تیکه تیکه میشه و کلی ریپوی نیمه‌کاره و بدون پشتیبانی روی گیت‌هاب رها میشه. اگه واقعاً ایده‌تون کاربردی و درسته، بهتره همون رو به صورت Pull Request برای نویسنده‌ی اصلی بفرستید تا روی سورس اصلی مرج بشه.
۲.
تمرکز روی نیاز واقعی، نه هر ایده‌ای:
لازم نیست هر چیزی که به ذهن می‌رسه رو با عجله کد بزنیم و فکر کنیم حتماً به درد همه می‌خوره! مثلاً واقعاً نیازی نیست برای یه دستور ساده‌ی Iptables بیایم اسکریپت نصب آسان بنویسیم.
۳.
مسئولیت نگهداری و امنیت:
ساختن اسکریپت با هوش مصنوعی شاید با چندتا پرامپت ۵ دقیقه زمان ببره، ولی پشتیبانی، رفع باگ‌ها و حفظ امنیتش کار راحتی نیست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2931" target="_blank">📅 20:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2930">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭕️
طرح جدید «نظام‌بخشی فضای مجازی»؛ از جریمه ۱۰ درصدی درآمد تا لغو مجوز پلتفرم‌ها
پیش‌نویس سند «طرح نظام‌بخشی فضای مجازی» با هدف تفکیک وظایف تنظیم‌گری، تعیین مجازات برای پلتفرم‌ها و تعریف حقوق کاربران نهایی شده است.
🔹
تفکیک وظایف تنظیم‌گری میان نهادها:
مدیریت اینترنت، کلاود و دیتاسنترها به وزارت ارتباطات؛ پرداخت‌ها به بانک مرکزی؛ ضد انحصار به شورای رقابت؛ صوت و تصویر فراگیر به ساترا؛ و اخلاق و ایمنی الگوریتم‌ها به سازمان ملی هوش مصنوعی سپرده می‌شود.
🔹
ضمانت اجراها و مجازات‌های سنگین:
شامل اخطار، انتشار عمومی تخلف، محرومیت ۱ تا ۳ ساله از تسهیلات،
جریمه نقدی ۱ تا ۱۰ درصد از درآمد سالانه
، تعلیق و در نهایت لغو کامل مجوز فعالیت.
🔹
مهم‌ترین مصادیق تخلف پلتفرم‌ها:
نقض حقوق کاربران، رفتارهای ضد رقابتی، عدم احراز هویت معتبر کاربران پیش از ارائه خدمات، خودداری از ارائه اطلاعات به تنظیم‌گر و عدم رعایت مصوبات قانونی.
🔹
به‌رسمیت شناختن حقوق کاربران:
تاکید بر «حق دسترسی به شبکه»، ممنوعیت قطع یا دستکاری ترافیک بر اساس اصل «بی‌طرفی شبکه (Net Neutrality)» و رعایت رده‌بندی سنی و حقوق کودکان.
🔹
سامانه حکمرانی مشارکتی:
الزام به انتشار پیش‌نویس مصوبات ۲ هفته پیش از تصویب جهت نظرخواهی عمومی از مردم و کارشناسان در یک سامانه هوشمند./
مقاله کامل
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2930" target="_blank">📅 20:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2929">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIPMiqdzuoLciyjd2pKmu388Lddxs4ou3prGM5Q409Fjk7UcmrmMV4TtIPqMzNeAcJduBTP5BuB4zJhY0il7FR2GLG3s5_T6tvDqJVSGmhRVxbJCRGb0PQmN1Tgtjj9TjuxaTTqX3khK_CJ_l6DbAtuW8qI8apVJZSXJuF-5JrzgKpjxYjCHwaZH16HvovKVFc3aZIjs61_Cpx03E8zYFEg8eI3QrmmeOL4Y-Ve4ws0-AIgN8e3a_VTsv8EBNTTBs5dpXpWNOoJuBqV_bl_1_aBSIpOnSKeFgI_a0Ik-lgN11wf_TOMVNsoA758POvabiQ5rA6bDxpIEPSMF_HHrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی تانل سبک و بهینه Netlink Tunnel
پروژه
Netlink Tunnel
یک ابزار تانلینگ سبک، بهینه و کاربردی است که امکان مدیریت کامل و سریع تمام اتصالات را از طریق خط فرمان (CLI) فراهم می‌کند.
🔹
تشخیص قطعی و پایداری بالاتر:
واکنش سریع‌تر سیستم در شناسایی قطع ارتباط و اعمال Reconnect خودکار.
🔹
مانیتورینگ و آمار ترافیک Live:
نمایش لحظه‌ای حجم دانلود، آپلود و مجموع ترافیک مصرفی.
🔹
گزینه Optimize:
ابزار اختصاصی بهینه‌سازی پارامترها و تنظیمات شبکه.
🔹
پشتیبانی از پروتکل‌های متنوع شامل TCP، TCP Mux، حالت‌های مخفی‌ساز TCP Stealth و TCP PCK
🔹
پشتیبانی از اتصالات وب‌سوکت WS / WS Mux و WSS / WSS Mux
🔹
انتقال پایدار روی بستر UDP + FEC (تصحیح خطای رو به جلو)
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2929" target="_blank">📅 14:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu7YSSxAGqn6nlV6a2ZNYYnR2ygZWlY6PGlRcz8FGE6Ll8wC0VbqGvhWzufv-b8po8VO1F3SGOLBEFumwtwbYrS7GwEGBDs8uDPOcyzA-TZ_PtVD6JPN2l_kt_r0iUreL7aDFMnA1kkAWXHWf6ZTY-MK-uPlRJd3YTcMfYm4AaDnJpTB5SrcrATXWTybRYLa5G34cutD_H5uBE-paCu9wRMZyRssM4rVNecxht2_fVaCoSxnfKnP6RjBHSFghi6JtktjGZ5bWuv-AImoWJXm_X9Nl7JoD_TlgxOtvbqhM_pn24xJEPvjZ2qyDuAyfIhGtGDdmxSLjlgSl7lnWbaT_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔐
معرفی DayLock؛ گاوصندوق دیجیتال و ‌امن
پروژه متن‌باز DayLock یک سرویس اشتراک‌گذاری پیام و فایل بر پایه معماری «دانش صفر» (Zero-Knowledge) است؛ یعنی سرور هیچ دسترسی یا کلیدی برای خواندن اطلاعات شما ندارد!
🔹
رمزنگاری سمت کاربر:
تمام داده‌ها مستقیماً در مرورگر شما رمزنگاری می‌شوند و سرور فقط کدهای نامفهوم را ذخیره می‌کند.
🔹
پنهان‌نگاری پیشرفته:
مخفی کردن امن فایل‌ها و متن‌های حساس داخل تصاویر (PNG) یا فایل‌های صوتی.
🔹
رمز فریب‌دهنده (Decoy):
امکان ایجاد یک گاوصندوق جعلی برای مواقعی که تحت فشار مجبور به باز کردن فایل‌هایتان می‌شوید.
🔹
قفل‌های هوشمند:
محدود کردن دسترسی بر اساس کشور (Geo-Lock)، شبکه اینترنت (ASN) یا تنظیم زمان مشخص برای باز شدن پیام (Time-Lock).
🔹
تخریب خودکار:
قابلیت حذف برای همیشه پس از اولین بازدید (Burn-on-Read) یا پاک‌سازی خودکار در صورت عدم فعالیت (سوئیچ مرد مرده).
🔗
لینک بررسی و نصب در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2927" target="_blank">📅 20:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2926">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tETr1XjqTWtBBqmnLyBoYYzMOspsfidz4OCgPnfHOoqRrjzVN1TKOiPAypy4BjENXZj1UYjRrJ2LnNTY_B-RHgENHcEBFks5KN1XJgyirV_qfO84QFMLyRsAwxUlWVD2xAbd15Ra4WA43p_wlIMvz3VyqdbS46aclElvvLIXdNGnQlLkyWXYRGStlMPB4VqwCVOxakGFpnwhRUyIcABc2EZV763xEkk6vgpLDKzpq-twadW8RqudN47VEpEdyUKV8SoZ_1pOsl1atis1k0pol3LTc_eB5N231gW1GylAGH6v258pATDHiO7OR5Ism0n8XLgRIRq-Y6SajQx4kYSkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتار آدم های معمولی با هوش مصنوعی
در مقابل
رفتار برنامه نویس ها با هوش مصنوعی :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2926" target="_blank">📅 18:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2925">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5EagVDkbz5wH62bHj6cESMH13RnwaiumZawxveBoRSxHr29pUVqQ-RGF4OmPZs6MGJ-2-0rlYAj1q7f_7ywYrTFqsbhM39yVPmGBnorBKgQgizJT5-WDIbPbXm3_JBdiPVdQw-fOLAMB-dbTZSN3R6Kea4spjd62c5eCL_HtyB--et1Xmt0HZZQqbkqi19CF7xAZ2HZERaveAZKZVmtZI_TzAV0bTmkStJM2Ca24w082nP1Vrc3hpjIOyxXaGyOpn52ti9WufXTZ6bSIuuDa3B-4p9z8JQf6jfH_oT50-pbJuanePZbe3OnDqNazM7rhmkk6LeHDAlUsRVBknrFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
آپدیت بزرگ ۱۳ سالگی تلگرام منتشر شد؛ از فایل‌های درون‌متنی تا پیام‌های خوشامدگویی اختصاصی
تلگرام هم‌زمان با سیزدهمین سالگرد فعالیت خود، آپدیت جدیدی را همراه با قابلیت‌های کاربردی برای کاربران، مدیران کانال‌ها و توسعه‌دهندگان بات‌ها معرفی کرد.
🔹
پیام‌های خوشامدگویی:
مدیران گروه‌ها و کانال‌ها اکنون می‌توانند بسته‌های خوشامدگویی شامل متن، عکس، ویدیو و جداول بسازند که تنها برای کاربر تازه‌وارد نمایش داده می‌شود.
🔹
دکمه‌های تعاملی درون پیام‌ها:
با به‌روزرسانی
Bot API 10.3
، توسعه‌دهندگان می‌توانند دکمه‌های کنترلی تعاملی را مستقیماً داخل پیام‌ها قرار دهند و امکان اجرای بازی‌ها (مانند شطرنج)، آزمون‌ها، نظرسنجی‌ها و سفارش کالا را به‌صورت زنده فراهم کنند.
🔹
قراردادن فایل داخل متن:
ویرایشگر پیشرفته متن اکنون امکان گنجاندن فایل‌ها و آهنگ‌ها را درون بخش‌های مختلف نوشته فراهم کرده است (با نوشتن بیش از سه خط متن فعال می‌شود).
🔹
افزودن امضا و پیام به هدایا (Gifts):
هنگام خرید هدایای کمیاب (Collectible) با استفاده از Telegram Stars، می‌توان امضا و متن شخصی دلخواه را به هدیه پیوست کرد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2925" target="_blank">📅 16:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2923">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🛑
یه اشتباه خیلی رایج و خطرناک: «هر اسکریپتی که اوپن‌سورسه امنه!»
سلام دوستان عزیز
✋
همون‌طور که می‌دونید، هدف اصلی این کانال معرفی اسکریپت‌ها و ابزارهای اوپن‌سورس برای دور زدن فیلترینگه. اما یه سوءتفاهم خیلی بزرگ و خطرناک بین کاربرا وجود داره که وظیفه خودم دونستم حتماً در موردش باهاتون صحبت کنم.
خیلیا فکر می‌کنن چون یه برنامه «اوپن‌سورس» هست، پس قطعاً هیچ بدافزاری توش نیست و ۱۰۰٪ امنه. اما واقعیت اصلاً این نیست!
متن‌باز بودن فقط معنیش اینه که کدهای اون برنامه برای همه قابل دیدنه.
این ویژگی به خودیِ خود امنیت رو تضمین نمی‌کنه؛
بلکه امنیت زمانی وجود داره که متخصص‌ها، اون کدها رو خط‌به‌خط بررسی کنن. اگر کسی کدها رو نخونه، یه بدافزار خیلی راحت می‌تونه جلوی چشم همه تو همون کدهای اوپن‌سورس قایم بشه.
من خودم همیشه قبل از اینکه اسکریپتی رو معرفی کنم، تمام تلاشم رو می‌کنم تا در حد توانم و با کمک هوش مصنوعی، کدها رو بررسی کنم تا مورد مخربی توشون نباشه. اما یه مشکل بزرگ وجود داره:
👈🏻
اسکریپت‌ها مدام آپدیت میشن!
🔹
یه اسکریپت ممکنه بعد از اینکه تو کانال معرفی شد، تو همون چند هفته اول ده‌ها آپدیت جدید بده. بررسی تک‌تک این آپدیت‌ها برای منِ نوعی واقعاً غیرممکنه. این یعنی ممکنه اسکریپتی که ماه پیش کاملاً امن بوده، تو آپدیت امروزش حاوی کدهای مخرب باشه (حالا یا عمدی توسط خود سازنده یا به خاطر هک شدن اکانتش و...).
💡
خب راه‌حل چیه؟ چطور امن بمونیم؟
۱.
هیجانی آپدیت نکنید:
هیچ‌وقت به محض اینکه سازنده یه آپدیت جدید داد، سریع نرید اسکریپتتون رو آپدیت کنید! حداقل چند روزی صبر کنید. اگر تو آپدیت جدید بدافزاری باشه، معمولاً بقیه برنامه‌نویس‌ها زود متوجه میشن و گزارش میدن.
۲.
استفاده از نسخه‌های تست‌شده:
سعی کنید از همون نسخه‌ای (Release) استفاده کنید که روز اول تو کانال معرفی کردم و داره کار می‌کنه. تا وقتی اسکریپت فعلی‌تون بدون مشکل وصل میشه، لزومی به آپدیت کردن مداوم نیست.
۳.
به اعتبار پروژه دقت کنید:
پروژه‌هایی که تو گیت‌هاب ستاره (Star) بالایی دارن و افراد زیادی اون‌ها رو فورک (Fork) کردن، معمولاً بیشتر زیر ذره‌بین متخصص‌ها هستن و امنیتشون از اسکریپت‌های ناشناس بیشتره.
۴.
گزارش موارد مشکوک:
اگر خودتون برنامه‌نویسی بلدین و کدهای آپدیت‌های جدید رو نگاه می‌کنید، اگر مورد مشکوکی تو آپدیتی دیدید، ممنون میشم به ربات ما پیام بدید.
در نهایت فراموش نکنید همیشه حواستون جمع باشه و به هیچ ابزاری، حتی اوپن‌سورس، چشم‌بسته اعتماد نکنید.
🛡
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2923" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2922">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVhAFN4i8AEkF4s1dvsOyn6dPSZqSSo8lWdMww0chsmc5Ehi9v_GKMkyTREftAVtQWClu7bpYzoTnW-SBf_xvWyD8Wm3asoR587q98MUI1xPycmkFv57UY1Pk-2W6KZetwPhG8VXtUaSH3PMcTq4dt-zqFapJzB2YlgG_H11ysAVb7vcltNxLJ4aFKa1OztP7-PgsvRarMFgfPDIeTaxdSrQktJUP-Ncf_EgKEgev3vvBGkGFjON-KqT6Zwq50sKUISe_t9X5ewgcEtJR2C4S9VvWwJbYA36iZNR73YWuGMRzFT7qjtAySm9VPSeICpYtL448PONbXRGi4_BPjuDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگه سوال مالی داشتید میتونید از آرش بپرسید بچه ها :)</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2922" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2921">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuU20stzQqwrLs6k2AoQnjtANNMO4Umu0U6paC_vT7NdIqIunQ5z6HvzhumPZEnip1TDNFPjmEMSd-nnD5IlWqznY9NdYcdXBdKDdbnVDR5zainoS1Xg0-qvCCcJYQmLUD6byNXhK9wXCxCVqPzjFWEkj4LuH7UFSkCz4tCVXt-EoKHMiSkGtEZqnLB0iGSiGMSV3uDfSFHroIAt5u9CnBD_Zx62L7xQ8b5TYb4OYSDOq927m1AmKEtGh7-yzJB4dmvxakARabL4OGeJwGyLJWvPmJjS8siDlup6-drEO17SZl9hwzaQRqC62Vc0WSwOZij0Grj3rQkEmedumtm-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
وضعیت اینترنت این هفته
🔹
بر اساس داده‌های Cloudflare Radar، ترافیک بین‌الملل ایران همچنان حدود ۵۹٪ سطح عادی پیش از قطعی است. برخی مناطق مثل مازندران، کرمان و آذربایجان‌غربی افت محسوس‌تری داشته‌اند.
🔸
اگر این هفته با کندی یا قطعی مواجه بودید، تنها شما نیستید.
منبع: توییتر سایفون
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2921" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2920">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v88KJPn4KregZncL29P41oPE_m1M7cyizNZa3u6Fj0GuWfy-kQxI7UUlbCxPZUx06IadI8xyjLBQh3mPpgOi011-Be3ZEMvvMXOaP0qHHQZ_qvoin2HdEwNVSWfXrzYc7PjoI9kZUamA8sKka4nJnlI1ZMZ11i7aNuozSTlrInXhripIR02N_mp3YHTK4dRkJ-PJqGx1UPkD1-_akBJ5c7G1Q7CJJFq6izR8UbooxeuTL2NjnyyrpFgbIylfj4uLetAVs2nrTQuhhmAzSCZ7SJ13HiZjEHhhloWGaQS7xVpI_QYppyaqNvlmGeIzlKINEajwcnG2dEkDIC_Jils-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت پنل و شروع فروش در ۱۰ ثانیه! (معرفی ربات پنل‌ساز)
🔹
تو این ویدیو یک ربات پنل‌ساز رو بهتون معرفی می‌کنم که بدون نیاز به هیچ تخصصی، فقط با زدن ۲ تا دکمه می‌تونید پنل اختصاصی خودتون رو تحویل بگیرید و بلافاصله کارتون رو شروع کنید.
🔸
این ویدیو یه پیشنهاد عالیه برای دوستانی که پیام می‌دادن به خاطر شرایط خاص یا مشکلات جسمی دنبال یه راه درآمدزایی هستن.(می‌تونید ربات رو ۲ روز تست کنید و بعد از تحقیق و صحبت با پشتیبانی، کار خودتون رو استارت بزنید).
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#پنل
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/iaghapour/2920" target="_blank">📅 18:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2919">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ab5fc23.mp4?token=nv2rpjKoreFU4ePUyPXvjdtwIf5Rdos-dcOnmImQIbTj0GR0tKNGIWsdCtRgUoJj7POzPrW4ha5kLKfaUmjOINimJMlTHqJbyZgZptgh26RYzfJ9-xaUYHztDvuncRW8d-ZIDQdjtKONYwLGQbi1zz9mlI4rrGhcNxey4F1vhWZ3Hbb3GqWyk9bnisrbSXQbCB9r9jRdbdeTF7NRueD82sQFpP3MOO6BVg80M2oYjnYRDGS-7MJx08YqxQmsHgvXgd5SmLDeYtxlRuTrc1a9yclf0PpRaGZ-EHQ5ewp_wWcVg44mpImiYXfsOeIqe5550Otxdc5Yge18M_RA_Dhl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ab5fc23.mp4?token=nv2rpjKoreFU4ePUyPXvjdtwIf5Rdos-dcOnmImQIbTj0GR0tKNGIWsdCtRgUoJj7POzPrW4ha5kLKfaUmjOINimJMlTHqJbyZgZptgh26RYzfJ9-xaUYHztDvuncRW8d-ZIDQdjtKONYwLGQbi1zz9mlI4rrGhcNxey4F1vhWZ3Hbb3GqWyk9bnisrbSXQbCB9r9jRdbdeTF7NRueD82sQFpP3MOO6BVg80M2oYjnYRDGS-7MJx08YqxQmsHgvXgd5SmLDeYtxlRuTrc1a9yclf0PpRaGZ-EHQ5ewp_wWcVg44mpImiYXfsOeIqe5550Otxdc5Yge18M_RA_Dhl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
علی‌بابا از مدل قدرتمند تولید ویدیوی هوش مصنوعی Wan 3.0 رونمایی کرد
شرکت علی‌بابا (Alibaba Cloud) رسماً از مدل پیشرفته و ارتقایافته
Wan 3.0
برای تولید ویدیوهای باکیفیت ۳۰ ثانیه‌ای رونمایی کرد. این مدل با هدف رقابت جدی در بازار جهانی تولید محتوای ویدیویی هوش مصنوعی عرضه شده است.
🔹
پشتیبانی از ورودی‌های متنوع:
امکان ساخت ویدیو از روی متن، اسناد، صفحات اکسل (اسپردشیت)، اسلایدها و صفحات وب.
🔹
پذیرش چندگانه فایل‌های مرجع:
قابلیت دریافت همزمان تا
۱۰ تصویر مرجع
،
۵ ویدیوی مرجع
و
۵ فایل صوتی مرجع
برای هدایت دقیق خروجی.
🔹
حالت تفکر:
پردازش هوشمند و تحلیل دقیق‌تر برای دستورات و پرامپت‌های پیچیده و چندمنظوره.
🔹
حفظ یکپارچگی کاراکترها:
توانایی حفظ ویژگی‌های بصری شخصیت‌ها در طول صحنه‌ها و سناریوهای مختلف با خروجی‌های بسیار واقع‌گرایانه و پرجزئیات.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2919" target="_blank">📅 16:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2918">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIDJUpEgjCGJWgT7jjAA672ekcFGIShG2zMUMvZjbnOtMEgng7iBqZye8qs4z2BrQczMhs9GZCa6e8l5-ILjTD3Dnq3JJqFjOWf2N0D63mcp2vwpqQVxQAPZUI6clVJDPDPtT8P54qGbDaQLvGLCbW_WB37ucWKH3d1ecK4JTxBqUfH1-r3VycVuUCLidvB6UXqkuf2aZbqzG24vzJG3OU6Ebo3B5-xjEuO1X8_E-WSNqc3Pm_Ew4IJ5vxgc_GAU4KRutE3U4BpRtLbQ-1mBvvsEpvifpxPm2_4meWbIIknKwq2l2-goil0KsptXiFYT1XXhAHp53we8NfmP-r0H8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پروژه استقرار PasarGuard Node روی بستر ابری Railway
پروژه
railway-pg-node
یک Wrapper مستقل برای بیلد و دیپلوی مستقیم نود پاسارگاد (
PasarGuard Node
) روی کلود Railway بدون نیاز به خرید سرور اختصاصی است.
⚙️
معماری و نکات کلیدی راه‌اندازی:
🔹
مدیریت پورت و لیسنر:
کانتینر یک لیسنر از نوع TLS اجرا می‌کند؛ متغیر پورت (
PORT
که معمولاً ۸۰۸۰ است) از سمت Railway تزریق شده و اسکریپت
start.sh
آن را به عنوان
SERVICE_PORT
ست می‌کند.
🔻
اتصال به پنل اصلی با TCP Proxy:
از آنجا که پنل مدیریت خارج از شبکه Railway قرار دارد، باید از
TCP Proxy
استفاده کنید:
🔹
پورت داخلی:
همان پورت داخل متغیر
PORT
یا لاگ سرویس (مثلاً ۸۰۸۰).
🔹
پورت عمومی:
پورت تخصیص‌یافته توسط Railway به همراه دامنه/Hostname عمومی.
⚠️
نکته مهم آدرس داخلی:
دامنه
railway-pg-node.railway.internal
تنها در شبکه داخلی Railway معتبر بوده و برای اتصال خارجی باید از آدرس TCP Proxy استفاده شود.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/2918" target="_blank">📅 14:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHw6WdEu2eiY7eZBjB-bkBg3DAX71yuKgEFNdo930vP6DBK2ZIOgPB2pOTKNdp1GVnqEya1WAe-Wr19VQWyFEuROfcvvNP7xF_sdLoSZ0EkUtBvJIzFouG-uSBGLkNo0vBZR6GgioDHfiJ-NXJO4sX6cm7iMR4aGoGqQoN7WoNSGzQZcH7u7MMhYz_UuibNHLXQ5l-88S5N9yOS8w3QbFM-8xB1NuRorohN8h8BfcOZVmWQqc-EQwRbDYNMh0Znww9VkKQfR7Cez7yHEi-nhFeLmWKVJf5DUyBH465PiRfMpGksuFmyhvMkRRmuE_uw6jqqmyNFuWFrrI7ni2rmBcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی tproxy-server؛ نسل جدید پروکسی‌های وب برای تلگرام
این پروژه سمت سرور یک طرح اثبات مفهوم (PoC) از سوی تیم تلگرام دسکتاپ است که روشی کاملاً نوین برای عبور از فیلترینگ ترافیک MTProxy از طریق مرورگر داخلی (
WebView
) ارائه می‌دهد.
🔹
پنهان‌سازی در قالب ترافیک وب (HTTPS/WebSocket):
اپلیکیشن تلگرام فریم‌ها و رمزنگاری استاندارد MTProxy را حفظ می‌کند، اما تمام اتصالات TCP را از داخل یک لایه انتقال مبتنی بر WebView و در بستر امن HTTPS یا WebSocket عبور می‌دهد.
🔹
چندین اتصال در یک مسیر:
این سیستم چندین ارتباط لاجیکال را مالتی‌پلکس کرده و در سمت سرور، رله این جریان‌ها را مجدداً تفکیک نموده و به سرویس رسمی MTProxy متصل می‌کند.
🔹
استتار به عنوان یک سایت عادی:
دامنه سرور مانند یک وب‌سایت کاملاً معمولی و عادی HTTPS عمل می‌کند؛ تنها با داشتن Secret اختصاصی، صفحه پل ارتباطی پروکسی فعال شده و سایر درخواست‌های عمومی فقط وب‌سایت اصلی را می‌بینند.
🔸
سازگاری کراس‌پلتفرم:
این ساختار محدود به سیستم‌عامل خاصی نیست و هر کلاینت دارای WebView می‌تواند از آن استفاده کند.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/iaghapour/2916" target="_blank">📅 20:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpeXAgL-zpA0YBbL0MYPdS8EDi1oLZUX2Tm-HypdmtOM2mOc16ACGooKhgn-96p0nBZ4Nw2CyoUKxMgJD-poZoZ3s9S0O9yTrCNLpLg841MzXD8t3hLbJGHvOf6AtYQ_R05WTuf-M43rvuwEIGXiQaPTcj-YW69iWgl3zUwWxfxrBYkyQ48zkqpsTT0RkAycGrR4Ep9Go3I3vTF2uG2qWMN98P_nlEEDFA9dkp8OcratOBrUwSPQzJJzHCIZ7TKytjLHFxnlxmpQmKmg_wSxZEWlnhGsozooedT2zdC3l93A1EMKB42NOwOjizcffBl2qzVqEZQWa1skO4TxAUJJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
حدود ۴۰ درصد از آهنگ‌های جدید ماه ژوئیه با هوش مصنوعی ساخته شده‌اند
بر اساس گزارش تحلیلی پلتفرم
SubmitHub
و با بررسی بیش از ۱ میلیون قطعه موسیقی، نزدیک به
۳۸.۵ درصد
از کل آثار منتشرشده در ژوئیه ۲۰۲۶ با مداخله هوش مصنوعی تولید شده‌اند.
⚙️
آمار و نکات کلیدی این گزارش:
🔹
سهم آثار هوش مصنوعی:
۲۳.۲ درصد آثار کاملاً با AI ساخته شده‌اند و ۱۵.۳ درصد شامل قطعات تولیدشده با AI بوده که سپس توسط انسان‌ها ویرایش شده‌اند.
🔹
عدم توانایی تشخیص مخاطبان:
تحقیقات نشان می‌دهد ۹۷ درصد شنوندگان متوجه تفاوت میان موسیقی انسانی و تولیدشده توسط AI نمی‌شوند.
🔹
هجوم اسپم صوتی (AI Slop):
پلتفرم Deezer اعلام کرده بود بیش از نیمی از آپلودهای روزانه جدید آن به موسیقی‌های هوش مصنوعی اختصاص یافته است.
🔸
واکنش و مقابله پلتفرم‌های استریم:
🔹
پلتفرم
Bandcamp
انتشار هرگونه موسیقی هوش مصنوعی را کاملاً ممنوع و مشمول حذف اعلام کرده است.
🔹
پلتفرم
Spotify
از سپتامبر نشان اختصاصی «AI Persona» را به پروفایل‌ها اضافه می‌کند تا شنوندگان آثار ساخته‌شده با هوش مصنوعی را به‌راحتی تشخیص دهند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2915" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzvmZVD1mXqqfMlUXj9uWZTDTWc_gYT1FuZ5r4cfTAlshwqGDbK19hziXIRnVZLHBOBPAhZ6eGDiND9bnhm1z3B-n7BXVArt_YxTiNKufoCjDCUQfuRMLV1vNCkA4hWhJ2ix_Sa5eOMhXPVppashWcrwXTB1sSM3YKBwyhEjo3iaPcdgjiv-V1rY43LaO3BwBvKBnbRqxAIS6f9pKdYIT43Pi2nifDeXfg_o9v_nPXJP2c_3XHy0EBXffIfF8EQdPvpk8_Ydi1t8W1e3LmeJzRH1NO1mSTZKTw-mSUn6qIO20Z-7UphLukLhi9Q0nnYKI5Aen9v8uER_sTnzlJnVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دسترسی رایگان و آزمایشی به مدل‌های هوش مصنوعی Qwen در سرورهای Hetzner
هتزنر امکان استفاده رایگان و آزمایشی از دو مدل هوش مصنوعی
Qwen3.6-35B-A3B-FP8
و
Qwen3.8-27B
را برای کاربران خود فراهم کرده است که می‌توانید آن را به نرم‌افزارهایی مثل 9Router متصل کنید.
⚙️
مراحل فعال‌سازی و اتصال:
🔹
۱. دریافت توکن:
با اکانت خود وارد سایت شده و به آدرس زیر بروید تا یک توکن بسازید:
🔗
آدرس سایت هتزنر
🔹
۲. اضافه کردن به 9Router:
وارد برنامه شوید و یک پروایدر جدید از نوع
OpenAI Compatible
اضافه کنید.
🔹
۳. ثبت کلید:
روی گزینه
Add API Key
بزنید و توکن دریافتی از هتزنر را وارد کنید.
🔹
۴. ایمپورت مدل‌ها:
روی دکمه
Import from
کلیک کنید تا مدل‌ها به لیست شما اضافه شوند.
⚠️
وضعیت فعلی:
در حال حاضر مدل
Qwen3.6-35B-A3B-FP8
فعال و قابل استفاده است، اما مدل
Qwen3.8-27B
با خطا مواجه می‌شود.
©️
aleskxyz
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2912" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">💡
راهنمای ساخت اینباند در پنل 3X-UI روی سرویس ابری Railway
نکات تگمیلی درباره
ویدیو بالا
☝🏻
با این ساختار می‌توانید بدون نیاز به خرید سرور (VPS)، پنل
3X-UI
را روی کلود
Railway
اجرا کنید.
🌐
مکانیزم عملکرد پورت‌ها:
پورت‌های ۸۰۰۱ تا ۸۰۵۰ (وب):
ترافیک از طریق Nginx روی پورت ۴۴۳ مدیریت می‌شود (مناسب برای WebSocket و HTTP Upgrade).
پورت ۸۰۸۰ (مستقیم):
از طریق
Railway TCP Proxy
مستقیماً هدایت می‌شود (مناسب برای Reality و gRPC).
🛠
روش اول: ساخت اینباند WebSocket / HTTP Upgrade (پورت ۸۰۰۱ تا ۸۰۵۰)
۱. در پنل وارد بخش
Inbounds
شده و روی
Add Inbound
کلیک کنید:
Remark:
نام دلخواه (مثلاً
WS-Inbound-1
)
Protocol:
انتخاب پروتکل (
VLESS
یا
VMess
یا
Trojan
)
Port:
یک پورت بین
8001
تا
8050
(مثلاً
8001
)
Network (Transport):
انتخاب حالت
ws
(WebSocket) یا
HTTPUpgrade
Path:
متناسب با شماره پورت (مثلاً برای پورت ۸۰۰۱:
/in1
، برای ۸۰۰۲:
/in2
و...)
Security:
تنظیم روی حالت
none
روی
Save
کلیک کنید.
۲.
تنظیم بخش Host (ضروری):
روی گزینه
Add Host
کنار همان اینباند کلیک کنید.
Address / Host:
دامنه اختصاصی پنل در Railway (مانند
your-app.up.railway.app
)
Port:
عدد
443
Security / TLS:
فعال‌سازی گزینه
TLS (Enabled)
⚡️
روش دوم: ساخت اینباند Reality یا gRPC (پورت ۸۰۸۰)
۱.
ایجاد پروکسی در Railway:
در داشبورد Railway به مسیر
Settings
⬅️
Networking
بروید، روی
Add TCP Proxy
کلیک کنید و پورت کانتینر را روی
8080
بگذارید. دامنه و پورت اختصاص‌یافته را کپی کنید (مانند
domain.proxy.rlwy.net:12345
).
۲.
ساخت اینباند در پنل 3X-UI:
روی
Add Inbound
کلیک کرده و
Port
را حتماً روی
8080
تنظیم کنید:
حالت Trojan gRPC Reality:
Protocol: Trojan
|
Network: gRPC (حالت Multi)
|
Security: Reality
حالت VLESS TCP Reality:
Protocol: VLESS
|
Network: tcp
|
Security: Reality
|
SNI: یک دامنه معتبر (مانند yahoo.com)
روی
Save
کلیک کنید.
۳.
تنظیم بخش Host در پنل:
روی
Add Host
کلیک کنید.
Address:
دامنه TCP Proxy دریافتی از Railway (مانند
domain.proxy.rlwy.net
)
Port:
پورت دریافتی از Railway (مانند
12345
)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2911" target="_blank">📅 20:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCbzN1We9C3DdkHAVos0TxRBo9qAPNxseT1-TkS6-JF4o-Z0X_Bocgfgx6TjZLViOPr2T5js2W69R18ht2_36nscbDEVXO8PQ0IvqheZtRLsYwRz4WnBWRXnk__eJsaBiz4_j2lL2SkHbWnEfOawECqddE9WEfKCum_L7IZcDz8XTrbddjnxBAwRqRLdNx9ZbtC83xNaZnK_OYxOfZ4Ufyo2GJVBqXL5gxu7B6qJDHCWAwqswlImCOqel2rIiAg6bvsaU6BQfHPbaTGJmbrnYl659CUMGUWEYxCue229KRqzuSg5c-9qvJxoSE5STUKMLB7InSXRS-G7hJEpA222fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بزرگ‌ترین آپدیت تاریخ CPU-Z منتشر شد؛ نسخه V3 با ۱۰۰ تست سلامت و سیستم اعتبارسنجی جدید
نرم‌افزار نام‌آشنای
CPU-Z
بزرگ‌ترین به‌روزرسانی تاریخ خود را از سال ۲۰۰۱ تا امروز تجربه کرد. نسخه جدید (V3) با بازطراحی کامل بخش اعتبارسنجی (Validation) و افزودن ابزارهای مانیتورینگ سلامت منتشر شده است.
⚙️
امکانات و تغییرات کلیدی نسخه V3:
🔹
اعتبارسنجی استاندارد:
بررسی سلامت کامل سیستم در کمتر از ۱۰ ثانیه با ارزیابی بیش از ۱۰۰ شاخص مختلف (درایورها، دمای CPU، برنامه‌های اضافی و...).
🔹
اعتبارسنجی پیشرفته:
تست استرس و خطایابی سنگین و دقیق روی CPU، رم و کارت گرافیک به همراه بنچمارک جامع سیستم و سنسورهای مانیتورینگ پیشرفته برگرفته از HWMonitor برای بررسی دما، سرعت فن‌ها و فرکانس.
🔹
حالت اختصاصی اورکلاک (XOC):
محاسبه فرکانس مؤثر پردازنده‌های مدرن و مدیریت صحیح اورکلاک رم جهت جلوگیری از رد شدن تصادفی تاییدیه‌ها و ثبت دقیق‌ترین رکوردهای فرکانسی.
📥
دسترسی:
فایل نصب نسخه جدید از وب‌سایت رسمی
cpuid.com
قابل دریافت است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/2910" target="_blank">📅 18:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de89d4765.mp4?token=fDMP5m1ozpvxvkUNACdUmC6DCEMysXB3OAuVx5lYt3hLawBoiQSiT38S3JVpzzELK5zP1b8lVZflsfGxwux-lQNR5ORBXR4QKuI-pq_u_5RCK5X6DkuGFKb9ZCNaZeGonGivh5nBfyeabLw35WPUTcXAiMHf3lLhbTAXvfSW5atThjccoBEFkZd0Lw8S-u-WSErGMvDo6t-RZEthNj9rUUZeIXypNUnMvCN9ToqtOMA9tzeaHJiL9F7LG10JcPopSxWE9ktj_xEM1mpGg-T3FXCc13HWjp2vDqo4jrMPHIPvG2kc1GSnyHt8H8Lu5nJwHXENb1NDnTx02U1UuudVcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de89d4765.mp4?token=fDMP5m1ozpvxvkUNACdUmC6DCEMysXB3OAuVx5lYt3hLawBoiQSiT38S3JVpzzELK5zP1b8lVZflsfGxwux-lQNR5ORBXR4QKuI-pq_u_5RCK5X6DkuGFKb9ZCNaZeGonGivh5nBfyeabLw35WPUTcXAiMHf3lLhbTAXvfSW5atThjccoBEFkZd0Lw8S-u-WSErGMvDo6t-RZEthNj9rUUZeIXypNUnMvCN9ToqtOMA9tzeaHJiL9F7LG10JcPopSxWE9ktj_xEM1mpGg-T3FXCc13HWjp2vDqo4jrMPHIPvG2kc1GSnyHt8H8Lu5nJwHXENb1NDnTx02U1UuudVcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره پنجم و ششم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
نیما عزیز با آیدی nimashokri5515، مبارکتون باشه!
✨
👤
حامد عزیز با آیدی hamedsalamati2286، مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسرهای عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2908" target="_blank">📅 20:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2907">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmi19KqCZJvM7jXHzXL9vz_d3i7IKVDC2K4eQvkRdFuh7lY_l10zF_x141Z_MBptiJcq9JZxCWTvig0ED_bnGDyO8obbjp7QsEXknBAvJiey5CPQ9Va1A7CK5jXlnOWPbBvMM8r1xUGaB1Qxe2qfaueBY_1I3Ene897fBX7KhPgrA7aQqZSG5yVCRmrHAnFqBp4WM7Ghi8hp6m2ZvZsPI-8VVVyuOmhBoxiE2L4QFScHk9CBaJ_zOhkLAbowMJp0_oK_b_lGHkKwUr3EGszB-UZ51asXFawSnEhLaYjm7SrqZdb6mG_s3OcQbC43n9r6vRHPA5ZnWucVCBg_IGg1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
تداوم ناپایداری‌ها؛ دیتاسنترها گرفتار فیلترینگ سخت‌گیرانه و سامانه «شاهکار»
بررسی‌ها و تایید مدیرعامل شرکت ارتباطات زیرساخت نشان می‌دهد وضعیت اینترنت در دیتاسنترها هنوز به روال عادی قبل از دی‌ماه ۱۴۰۴ بازنگشته است.
⚙️
چالش‌های کلیدی مراکز داده:
🚫
فیلترینگ شدیدتر:
دیتاسنترها با محدودیت‌هایی به‌مراتب سخت‌گیرانه‌تر و اختلالات فنی مرموزتری نسبت به اینترنت خانگی دست‌وپنج نرم می‌کنند.
🔻
بحران سامانه «شاهکار»:
بزرگ‌ترین مشکل فعلی، الزام به احراز هویت دستی کاربران در سامانه «شاهکار» پیش از اتصال است که این فرآیند را از ۲۴ ساعت تا
یک هفته
طولانی کرده است.
🌀
سردرگمی کسب‌وکارها:
تیم‌های فنی هنوز درگیر ترمیم زیرساخت‌های آسیب‌دیده از قطعی‌های طولانی هستند. فقدان تضمین برای عدم قطعی مجدد، شرکت‌ها را میان بازگشت به معماری استاندارد یا حفظ آمادگی برای بحران بعدی معلق نگه داشته است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/2907" target="_blank">📅 19:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2906">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6DJ1RiFttDnULp42l3__3tLhuziDincLE0LctSITmA7_MYIcgcBDdd4G1v5EyiF9KZ19tEFO-z2bn_ioK4rthetYc1EBpZ6SPnkKU__6bMIxIaulmhAk5qvNUna1P2VSUw55K7OZbXRe1v1BWBG5c_lLLwkNP_7uNLvXDuasA8c2_neMbtVo-cm9fXd2sbBLULbh3UiURpCetAQ-DBD2Gn75RFvHISF8mhsI5Qq-GXhsfmYezQ9uu32BGx1uYP4-yRgscH-xpTtu6PkfhM346SjyZufK4ncnd1n9ewmL4f6ugpEhi0bfUTm4i_F7JmMHyk6F0mnIjwHc2p0OOmIXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی Tor Node Manager؛ اسکریپت ساخت و مدیریت خروجی‌های تور تفکیک‌شده بر اساس کشور
این پروژه یک ابزار تعاملی است که به شما امکان می‌دهد روی سرور خود نودهای مجزا و اختصاصی Tor را بر پایه کشورهای مختلف (مثل ترکیه، آلمان، هلند، فرانسه و...) به‌صورت پروکسی‌های لوکال SOCKS5 بسازید. این پورت‌های لوکال به‌راحتی می‌توانند به‌عنوان Outbound در پنل‌های
3X-UI
،
Xray
یا سایر برنامه‌ها استفاده شوند.
🌍
تفکیک نودها بر اساس کشور:
ساخت نمونه‌های مجزا از Tor با لوکیشن دلخواه و پورت SOCKS5 اختصاصی روی
127.0.0.1
.
🔄
سرویس‌های مستقل Systemd:
اجرای هر کشور به‌عنوان یک سرویس مجزا در سیستم‌عامل به همراه فایل کانفیگ، دایرکتوری داده و لاگ اختصاصی.
🔍
تأیید خودکار موقعیت جغرافیایی (Geo-Check):
بررسی زنده و چندمرحله‌ای اتصال و کشور خروجی Tor، همراه با سیستم تلاش و ری‌استارت مجدد خودکار تا زمان تایید قطعی لوکیشن انتخابی.
📋
کانفیگ آماده Xray Outbound:
تولید و نمایش خودکار قطعه‌کد آماده‌ی JSON برای اضافه کردن مستقیم به بخش Outbounds در Xray یا 3X-UI.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/iaghapour/2906" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2904">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBnCBFi9Iv4cDeeEoGvYFl6c0_0gkL9iv-NG69KHYbuBpnoMM4nSSmlhTQoq-giosTpSnQQhbNxX4xC1y9m6aTIfdSztxurkROm2jlSBiSD6xjWi-zxXezQK7gvzAb1CBFj7iMiCR1qLlZAM1KTF00yJ7k0zJqgC3KFYcjfERDhFcjCogIkeN2B4aT0s8YjuIExsb2NfL3HaDM1PSjXE4aCC8JedVXbiwIDRvJ7crM_Y524tA08_Q6v34-VOUpAFLn3E_XU8tT3-qgDN-xMoxqfDSSQTzONNIMaDYAL0zy4UBx9fL8dsAFH_eErSnA3Uktmc6-wPSAL2hXtmD1Oeyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن شخصی بدون سرور و دامنه (کاملاً رایگان!)
🔹
اگه می‌خواید یک کانفیگ کاملاً شخصی برای خودتون داشته باشید، ساخت فیلترشکن شخصی بدون سرور و دامنه همون راهکاریه که بهش نیاز دارید. تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم که چطور بدون سرور یا دامنه، پنل X-UI رو راه‌اندازی کنید و برای خودتون کانفیگ شخصی بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت فرصت دارید.(قرعه کشی این ویدیو با ویدیو قبلی باهم انجام میشه)
#آموزش
#فیلترشکن
#رایگان
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/iaghapour/2904" target="_blank">📅 17:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2903">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP1lm5bzylr14CIQJF8b6e0wuIOwttQOutgqlYASlSEH-nvxnX3SOWVoxJdWM0QZTpL-2oCztWYQ9vS_B70vfLqzvufyZe4QcytcKzWOcPF8cG--3qjkLU6c4-woLuX3hSfvXYGymKANZdNIToHqQbQZZysh0Xg_eCl7C3eJetJicd5LiOhDwiQUoHXTmeh6B3nDBo_JQrnRrPmIPKm17Wd0kOSA-dn232xAFAK-Bt-Qs776IOq6ugIih4mA_b74LpJdLoNhE9RutqZapmOcB2R_Ysa4u1sfsRyTbmFoMFADLWzlXl6ahcUNZ41oRgJFgmP_rSz5veHAEgZovacN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش استعلام سیم‌کارت‌های فعال به نام شما با کد ملی
بی‌خبری از سیم‌کارت‌هایی که به نام شما ثبت شده‌اند می‌تواند باعث سوءاستفاده‌های حقوقی، امنیتی و جعل هویت شود. طبق قانون، هر فرد حداکثر می‌تواند
۱۰ سیم‌کارت فعال
در مجموع تمامی اپراتورها داشته باشد.
⚙️
روش‌های استعلام:
📩
۱. استعلام سریع از طریق پیامک:
— کد ملی ۱۰ رقمی خود را به سرشماره
۳۰۰۰۱۵۰
ارسال کنید.
— پیامکی از
CRA.ir
حاوی تعداد سیم‌کارت‌های فعال شما در هر اپراتور ارسال می‌شود.
🌐
۲. استعلام کامل از سامانه «دولت من:
— وارد سامانه
my.gov.ir
(یا اپلیکیشن دولت من) شوید.
— پس از ورود، از بخش
دسته‌بندی سازمان
⬅️
سازمان تنظیم مقررات و ارتباطات رادیویی
را انتخاب کنید.
— با انتخاب گزینه
«تعداد خطوط مشترکین تلفن ثابت و سیار»
، تمام شماره‌های فعال همراه اول، ایرانسل، رایتل، اپراتورهای مجازی و سیم‌کارت‌های TD-LTE را مشاهده کنید.
⚠️
اقدام فوری در صورت مشاهده سیم‌کارت ناشناس:
اگر خط ناشناسی به نام شما ثبت شده است، بلافاصله از طریق اپلیکیشن یا نمایندگی‌های اپراتور مربوطه نسبت به
سلب مالکیت یا سوزاندن سیم‌کارت
اقدام کنید./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2903" target="_blank">📅 16:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2901">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umRWsjoySf854zdIwtHAY38Wf-9U0duvqcGMgYD_Pjmr68rHYx-HIq7gmxTGQfRplCyhWHImi4LCYgETb5lhXuraf9KDsg8nHL6elZNeDFshOhejoGChvBaDmckLxyWTfUI3-1oTtH41WMzWUh0ta2kR3mnarW7AxwMZosdgxImX1SMvRLFNLsqA5xN0TlFz1xuL16xiftVJxGndtXJNO5pIsEc309DGYY39ykSpV7jPy5IBOYcncFamAVsayKJ8BfB3XpggMRrWajd10bUFA3IHeYXX68nZB-9onZxPX4NiAWxyiUxu1kUfouzCIvVQFwLTiy0IBgd6CCoJgvYN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
فقط با یک سرور، 3 لوکیشن مختلف داشته باش! (با پنل 3X-UI)
🔹
اگه می‌خواید تو هزینه‌های خرید سرور صرفه‌جویی کنید ولی همزمان به آی‌پی‌ با لوکیشن‌های مختلف نیاز دارید، این آموزش دقیقاً همون چیزیه که دنبالشید. تو این ویدیو قدم‌به‌قدم بهتون یاد می‌دم که چطور فقط با یک سرور، 3 لوکیشن مختلف داشته باشید و این کار رو به سادگی روی پنل 3X-UI پیاده‌سازی کنید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت فرصت دارید.
#آموزش
#فیلترشکن
#ثنایی
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/2901" target="_blank">📅 18:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2900">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwwBFm3in05GHctEa_v0oPP7DbM8igcW54Jts1-d-uby3qKzH8dYhxkMWhVbc-xiJ6P-nhA3YlrXuMKRRNuhAR6eDJj1nZZtp-_kf38fQYnBYxGmMa03BrZhjUAN0DGCqRG6mGSwxNbaNax4mjdZdEZX_g5ujijx91ZIoJXRv6W8EiAZoWMEnCwBbLEgH_rKMD8BRZuuaU-TW0eqaeYJlX3ck7A8rT0pUAghD5pkIbdr4qqvhicGoXssMY-GTPycutry5ky6v8dx0Tbvr6QxmtKFwViRAr6_H3CcgdF4sTsHRvWch8vCYsWDy1gVI5UEgdDETCWY05SbwME-o5Jp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تلگرام به هر کاربر دامنه اختصاصی با پسوند gram. می‌دهد!
تلگرام رسماً درخواست ثبت دامنه سطح‌بالای اختصاصی (TLD) با عنوان
gram.
را به سازمان آیکان (ICANN) ارائه داده است تا کنترل کامل زیرساخت آدرس‌های خود را به دست بگیرد.
⚙️
جزئیات و امکانات این طرح:
🔹
دامنه اختصاصی برای هر کاربر:
در صورت موافقت آیکان، بیش از ۱ میلیارد کاربر تلگرام دامنه‌ای بر پایه نام کاربری خود دریافت می‌کنند (مثلاً
username.gram
).
🤖
ساخت وب‌سایت با هوش مصنوعی:
کاربران می‌توانند وب‌سایت‌های تعاملی خود را روی همین دامنه‌ها و با میزبانی مستقیم تلگرام، تنها با وارد کردن یک دستور متنی (پرامپت AI) بسازند.
🛡
استقلال از واسطه‌ها:
این اقدام پس از اختلال اخیر دامنه
t.me
توسط ثبت‌کننده پسوند
me.
انجام شد تا تلگرام از وابستگی به رجیسترارهای ثالث رها شود.
⏳
وضعیت تایید:
پذیرش این درخواست منوط به سپری شدن مراحل نظارتی، فنی و حقوقی در سازمان آیکان خواهد بود./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/2900" target="_blank">📅 17:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2899">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSgWGxhSkIGlu98ZB-feJZrHFflENyliU8xjZLFZGIucUDPtlNE3EoNJAqP5xfLUVXZm_IpY2dAqxBAw-axnfqJ52x47HvwMtSt-Qql0wlCFOpnnU1qvIfK3Tgkj2Lk-Met8KvwXQ_zByI4inCcVDf8a60oNVIYUxHMCqwt106oNDxzHBe-nrSkZ01v8GgPY_AHoBzeusg7e54smVOQ4CTHeVA4xy2oLz4HDyBY3Xu2-lxRuZ1RuX_ujhz1t1ggdD8G8iZpy4j-uLL0Ze1eMrujiQ_hunjOmGnAGrHr65L9YHCrF6q4EJLlgIx6E-MjlRkAnBSEJx6ucrQ9MPKWgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نظرسنجی ایسپا: بیش از ۲۰ میلیون ایرانی خواهان استفاده از اینترنت استارلینک هستند
بر اساس نظرسنجی جدید مرکز افکارسنجی دانشجویان ایران (ایسپا) به سفارش وزارت ارتباطات، در صورت فراهم بودن شرایط، بالغ بر
۲۰.۵ میلیون نفر
از کاربران ایرانی تمایل دارند از اینترنت ماهواره‌ای استارلینک استفاده کنند.
⚙️
یافته‌های آماری و نکات کلیدی نظرسنجی:
📊
میزان آشنایی و تمایل:
۵۶.۶ درصد
کاربران هنوز شناختی از استارلینک ندارند.
در میان افراد آگاه،
حدود ۶۱ درصد
تمایل دارند این سرویس را تجربه کنند یا به صورت دائمی به آن متصل شوند.
🚫
مانع اصلی، قیمت و دسترسی است نه قانون!
برخلاف تصور، منع قانونی دلیل اصلی عدم اتصال اکثر افراد نیست؛ تنها
۳۸.۲ درصد
به دلیل غیرقانونی بودن سراغ آن نرفته‌اند.
نزدیک به
۶۰ درصد متقاضیان (حدود ۱۲ میلیون نفر)
اعلام کرده‌اند دلیل وصل نشدنشان،
قیمت بالای تجهیزات
و
عدم دسترسی به فروشنده مطمئن
است.
⚠️
پیام هشدارآمیز داده‌ها:
آمارها نشان می‌دهد در صورت کاهش هزینه‌های تجهیزات یا تسهیل مسیرهای ورود به کشور، تعداد کاربران استارلینک در ایران می‌تواند با جهشی میلیونی روبه‌رو شود./شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2899" target="_blank">📅 16:01 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
