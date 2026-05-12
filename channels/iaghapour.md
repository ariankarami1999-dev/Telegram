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
<img src="https://cdn4.telesco.pe/file/Idg7r2Xx2DfIbvSXSCBgDz6-3SuEZpLB6BJrB59NN660gmKL2_sPEFU1d6ZgbByDtWyBNHrHh3iPzB4hnvR48EmJk8i-mPkUOeqkgAbXOuHRYH5UEz2FEDuYWzNSK3AkWqS1uG3P75TkcVvEXU0bts6Nu0Y4kgxUISL07nPiQGbTi3aTnjGuN8ZzuEeI1jt2aSvQpg3hKbLHED6uyByXeYj3TUd4vkk8VCWcFKiwAeLxukY6h-27t2Wr--S-GghvYAe9N_QMT_GkqFpqXxnQrl_5qOhG_k03_bDyV6Ce2Q9HpIdbIBVtrGWm-G7zNPRPZMR1XYDPIx6v32gDPxEQJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 50.5K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 21:28:40</div>
<hr>

<div class="tg-post" id="msg-2602">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚀
آپدیت بزرگ و انقلابی پنل 3x-ui (نسخه‌های 3.0.0 و 3.0.1)
بالاخره یکی از مهم‌ترین آپدیت‌های پنل محبوب 3x-ui منتشر شد! در این نسخه‌ها شاهد بازنویسی کامل رابط کاربری، اضافه شدن قابلیت‌های مدیریتی کلان و بهبودهای چشمگیر امنیتی هستیم.
🌐
۱. بازنویسی کامل و سریع‌تر شدن پنل (مهاجرت به Vue 3)
رابط کاربری از پایه بازنویسی شده است! این یعنی سرعت لود بسیار بالاتر، طراحی مدرن‌تر، صفحه لاگین جدید و بهبود چشمگیر تم دارک.
⚡️
۲. آمار زنده و در لحظه
: با جایگزینی سیستم قدیمی با
WebSocket
، از این پس تمام آمارهای داشبورد، مصرف حجم کلاینت‌ها و وضعیت سرور به صورت «زنده» آپدیت می‌شوند و دیگر نیازی به رفرش کردن صفحه نیست!
🌍
۳. مدیریت چند سروره (Multi-Node Deployment) -
🌟
ویژگی طلایی
یکی از مورد انتظارترین قابلیت‌ها اضافه شد! حالا می‌توانید از طریق یک پنل مرکزی (Manager)، کانفیگ‌ها و اینباندها را روی چندین سرور دیگر (Remote Nodes) مستقر و مدیریت کنید.
📱
۴. رابط کاربری کاملاً سازگار با موبایل
: داشبورد، لیست کلاینت‌ها و بخش لاگ‌ها حالا به صورت "کارتی" و کاملاً بهینه برای نمایشگرهای موبایل طراحی شده‌اند تا مدیریت پنل با گوشی بسیار راحت‌تر شود.
⚙️
۵. خداحافظی با کدهای JSON و تنظیمات آسان‌تر
فرم‌های ساخت کانفیگ (Inbounds) کاملاً ساختاریافته و گرافیکی شده‌اند. دیگر برای تنظیمات پایه نیازی به دستکاری JSON خام نیست (البته تب Advanced برای حرفه‌ای‌ها همچنان وجود دارد). همچنین مدیریت DNSها بسیار پیشرفته‌تر شده است.
👥
۶. مدیریت گروهی کلاینت‌ها (Bulk Actions)
امکان انتخاب گروهی  کلاینت‌ها برای حذف یا اعمال تغییرات اضافه شده که کار ادمین‌ها را بسیار راحت می‌کند.
🛠
۷. امکانات جدید Xray و Outboundها
اضافه شدن پروتکل Loopback، دکمه
Test All
برای تست همزمان همه Outboundها و ارائه گزارش دقیق از تایم‌اوت‌ها، و همچنین خاموش شدن امن هسته Xray.
🔒
۸. ارتقاء امنیت و نصب راحت‌تر
➖
اضافه شدن سیستم امنیتی CSRF Protection برای جلوگیری از حملات.
➖
اضافه شدن گزینه
skip-SSL
در اسکریپت نصب (بسیار کاربردی برای کسانی که از ریورس‌پروکسی یا تانل استفاده می‌کنند و نیازی به سرتیفیکیت روی خود سرور ندارند).
➖
اضافه شدن صفحه مستندات API (API Docs) در داخل خود پنل برای برنامه‌نویسان.
و بسیاری از تغییرات دیگه که میتونید در
این لینک
مطالعه کنید.
💡
نکته:
برای تجربه این تغییرات فوق‌العاده، پیشنهاد می‌شود هرچه سریع‌تر پنل خود را آپدیت کنید. (توصیه همیشگی: قبل از آپدیت بکاپ فراموش نشود!)
✍🏻
با تشکر از ثنایی عزیز.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/iaghapour/2602" target="_blank">📅 18:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⭕️
عصبانیت سخنگوی دولت از انتقاد خبرنگاران از قطع اینترنت
فاطمه مهاجرانی در نشست خبری امروز خود به اعتراض خبرنگاران بابت ادامه قطعی اینترنت واکنش نشان داد.
سخنگوی دولت گفت: «در شرایطی که رئیس جمهور آمریکا اعلام می‌کند آتش بس به دستگاه تنفس مصنوعی وصل است، پاسخ شما چیست؟ کشور در جنگ است. بپذیریم که ویژگی جنگ، امنیت مردم است.»
✍🏻
پ.ن:  خانم مهاجرانی اگه دوباره عصبی نمیشید خواستم بگم کاش به فکر امنیت اقتصادی مردم هم بودید! کاش به فکر امنیت ذهنی و روانی مردم هم بودید! کاش یه فکری برای چند میلیون آدمی که با قطعی اینترنت بیکار و ناامید کردین هم بودید!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2601" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
نمیتونم خبر رو تایید کنم ولی میگن:
— افغانستان اینترنت 5G آورده.
— عراق تلگرام رو رفع فیلتر کرده.
— سوریه هم که ویزا و مستر کارت و...
این که ما درگیر فیلترینگ مسخره هستیم واقعا گریه داره...</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/iaghapour/2600" target="_blank">📅 09:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سلام خواستم یه نکته کوچولو بگم
فقط بحث کسب و کارهای کوچیک نبود
فقط بحث آنلاین شاپ ها نبود
ماهایی که ۴ سال تو دیجیتال مارکتینگ بودیم توی طراحی سایت و سئو و اتوماسیون کار میکردیم هم کاملا ورشکست شدیم
نه از ۹ اسفند
ما یه بار جنگ خرداد زمین خوردیم تا اومدیم بلند شیم از جامون و داشتیم اوکی میشدیم دلار دی ماه سر به فلک کشید و بعد یه قطعی دیگه داشتیم که خیلی ها بهانه کردن و پول ندادن آخر دی ما هیچی پروژه نداشتیم حتی بهترین کارفرماها اومدن گفتن کار شما خیلی خوبه ولی ما واقعا پول پرسنل رو هم به زور میدیم نمیرسه به سئو
بهمن اومدیم خودمون رو جمع کنیم تیر آخر رو اول اسفند بهمون زدن
دفترمون رو تحویل دادیم
نیروهامونو از بهمن تعدیل کرده بودیم
و الان چه جوون ها و چه پدرانی که بیکار شدن
منی که تمام تخصصم همیناست
یک متخصص بیکار محسوب میشم.
©️
پیام ارسالی از کاربر shafikhany</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/iaghapour/2599" target="_blank">📅 01:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✍
حدودا 500 پیام بررسی نشده از 2 روز پیش داریم که پشتیبانی تا فردا همه رو بررسی میکنه.
جدا از بحث بالا، از ته دل آرزو میکنم تو این روزهای عجیب و غریبی که داریم می‌گذرونیم، حال دلتون خوب باشه. می‌بینیم و حس میکنم که زندگی چقدر برای خیلی‌ها سخت شده و دغدغه‌ها چقدر زیادن.
امیدواریم هرچه زودتر این روزهای سخت جاشون رو به روزهای روشن‌تری بدن. هوای خودتون و دلتون رو داشته باشید.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/iaghapour/2598" target="_blank">📅 03:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvLtnDPc9e2iuFG9LXs7Ljti8sDguUsG2nv4PDOuhvAGTyEgSmZNzM6i6G-cYZn0ZXvL1SCTeEy2U6ndQzq5q3mbIz0WwacxJHHbE-Kx_IFNvHARNhNhzU-2DWZ8KRYPyo6lAtjL2Njzep-rJghDk6dKZe-wXw1Qn_Cb5jn4slhTXWaZ0QdpgnISoEp1u4LGeYPZDFD0cvB1ve-ebyaHJie5SpfiQYLy7-jP5n6TOwNl8f-KuFVuzI2cpRXDxFa_BPaNq4fJsiaCH75MFWTL_cudcBIwjCppLvoaA9QUpYDD-IFPTF5oL45Kyha0voNH1-isZtf8UCB2Hy_kn9Wj1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت ورژن 0.10.0 سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور ایران خودتون یک مسنجر شخصی بالا بیارید و با دوستان خودتون چت کنید.
توی آپدیت جدید سانگبرد با فعال کردن قابلیت Remote channel، میتونید پست هایی که تو یک چنل تلگرام ارسال میشه رو، به یک چنل توی سرور سانگبرد خودتون استریم کنید.
-
📡
قابلیت Remote channel
-
🔗
ساده سازی سیستم Invite link
-
🎨
بازطراحی بخش ساخت/تغییر کانال و گروه در UI
-
✨
انیمیشن build-up پیام ها در چت ها
-
🔔
بهبود عملکرد push notifications
- تغییرات گرافیکی اسکریپت نصب آسان
-
🐳
پشتیانی از TLS با سرتیفیکیت self-signed در Docker
-
🔧
رفع باگ های گزارش شده
-
📄
اضافه شدن نسخه فارسی فایل readme
🔘
اگه به هر مشکلی خوردین، حتما تو گیت هاب یک issue باز کنید و گزارش بدید.
⭐️
اگه از پروژه راضی بودین، با ستاره دادن تو گیت هاب از پروژه حمایت کنید.
🔹
چنل پروژه
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/iaghapour/2597" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⭕️
ساده‌ترین راه برای دور زدن فیلترینگ با تانل DNS
اگه خانواده‌ شما هم داخل ایران برای اتصال به اینترنت مشکل دارند، این پیام ممکن است به شما کمک کند.
این برنامه یک برنامه‌ی  گرافیکیست که کار با آن بسیار ساده است و برای اتصال به اینترنت هر دو روش MasterDNS و VayDNS را پشتیبانی می‌کند.
👈
لینک گیت‌هاب
👈
دانلود
اپ
📖
آموزش کامل MasterDNS و VayDNS
▶️
آموزش روی یوتیوب
📱
آموزش KevinNet DNS
▶️
آموزش روی یوتیوب
🔄
آپدیت‌های جدید برنامه
در صورت وجود هرگونه مشکل یا سوالات مرتبط با KevinNetDNS میتوانید با آدرس ایمیل زیر در تماس باشید:
©️
متن تهیه شده توسط نویسنده اسکریپت KevinDNS
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/iaghapour/2596" target="_blank">📅 23:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭕️
ادعای عجیب نماینده مجلس: با ۴ هزار میلیارد تومان ایتا را به سطح واتس‌اپ می‌رسانیم!
رئیس کمیته ICT مجلس در اظهارنظری جنجالی مدعی شده است که فاصله میان پیام‌رسان‌های داخلی مثل ایتا با نمونه‌های جهانی مانند واتس‌اپ، تنها در کمبود بودجه برای خرید سرور خلاصه می‌شود. به گفته او، ارتقای این پلتفرم‌ها هزینه چندانی برای کشور ندارد.
این نماینده مجلس معتقد است که پلتفرم‌های داخلی از نظر فنی کمبودی ندارند و تنها زیرساخت‌های سخت‌افزاری آن‌ها باید تقویت شود:
🔹
بودجه برای رقابت:
مصطفی طاهری مدعی است با صرف ۳ تا ۴ هزار میلیارد تومان برای خرید سرور، می‌توان کیفیت ایتا را به سطح واتس‌اپ رساند تا توانایی پذیرش بدون مشکل بیش از ۲۰ میلیون کاربر را داشته باشد.
🔸
هشدار درباره جاسوسی سخت‌افزاری:
این مقام مسئول همچنین به موضوع استفاده از بیگ‌دیتا (داده‌های بزرگ) اشاره کرده و مدعی شده که آمریکا قوانینی برای جاسوسی در لایه‌های سخت‌افزاری و تراشه‌ها (حتی پایین‌تر از سطح سیستم‌عامل) دارد.
این اظهارات در حالی مطرح می‌شود که کارشناسان حوزه تکنولوژی، موفقیت پلتفرم‌های جهانی را فراتر از صرفا تعداد سرور می‌دانند و مواردی چون امنیت، پروتکل‌های رمزنگاری، حریم خصوصی و نوآوری‌های مداوم نرم‌افزاری را از عوامل اصلی برتری آن‌ها به حساب می‌آورند.
یکی از کاربرا زیر همین پست در دیجیاتو کامنت جالبی گذاشته بود:
مامان‌بزرگ منم با چند میلیارد نیکی میناژ میشه!
پ.ن: حالا فارق از این حرفا داره میگه اینا دارن از کاربراشون جاسوسی میکنن برای همین ما باید اپ های خودمون رو داشته باشیم... من حرفی ندارم.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/iaghapour/2595" target="_blank">📅 18:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiNffo1NVcvK7FJ0lvwAX_QHOY0Qm0ocmapnvyk-7Mctt0SFVM3IEwfAtx3TIUCqbSYysocMe1e79amCrFsjUxt-Y7ZcO1DUQmpB6k543XbIo_KQbLIlHsuKXKdoPkSt_gG1N-KZCmaScOMwhBH61nmIi3Zu8SnGCcHEwwQH72vVybhRpUOntVtPXUjEcVZOylMo0ji39bJMM2rbl6Du8oyy4n-zVJAdh-3yLX3imrL5mAum2ea6rEouXJ-dnTlBWLIOqYtomMdmLvHzAsdGca8Z0JS1TVUr5aUOcGgq1Zk5u0MUfqecqMC5pdX-by5ZomD9pKzAE3CRljBUvR3M-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ایران 11 هفته در خاموشی دیجیتال!
هیچ‌وقت تو زندگیم فکر نمی‌کردم یه روزی برسه که این‌جوری تلخ، شاهد از بین رفتن زحمت‌ آدما باشم. ۱۱ هفته قطعی اینترنت واسه خیلی‌ها فقط یه اختلال ساده نبود؛ قصه پدر مادرا و جووناییه که با هزار امید یه کسب‌وکار کوچیک راه انداخته بودن تا خرج زندگیشونو دربیارن و الان دستشون به هیچ‌جا بند نیست.
تا همین چند وقت پیش با کلی استرس می‌گفتیم کسب‌وکارهای نوپا و خونگی تو «مرز نابودی» هستن و همه‌مون چشم‌انتظار بودیم زودتر اینترنت وصل بشه؛ ولی الان دیگه حرف از مرز نیست. خیلی‌ها کل سرمایه، جوونی و حاصل سال‌ها تلاششون جلوی چشماشون دود شد و رفت رو هوا. کاش دردی که افتاده رو دوش این مردم، میافتاد رو دوش مسئولین...
🆔
@NetProPlus</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/iaghapour/2594" target="_blank">📅 11:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#فیلترینگ
به ما تحمیل شد,
ولی
#اینترنت_طبقاتی
رو شما باید درخواست بدی تا بهت بدن...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/iaghapour/2592" target="_blank">📅 18:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8lZn2L5Ufq0xhipPeqbu7xQcAJ26AbE-56w-nx-9DK1pOrD7JzYw4w8Ko6CdLdN8ECRTqMe1H4Q4FQeowolHcRBDM-dlON3PgffjmRKbQi8cxdxGEevKkDj2YKnEFRwrQZU1yt6cvYfoy1nbXkBgCSkh8_4uSc68IRxVK1szTUvx0kTfDHUeqiugNhbGyCfQPgfPd6-KxPsj8voImUdg1o9gLps9lAjvjxlvyPtvZGvUUhoGor8u3CmEJSSg6WEc4LPKYa6CP0SKL0eT-jQ8Dd_Jy5GSXYX3uCRt8oPaaIowIF9RMzPSBCMmfDvdK4AWDWO4BZaJxigvcLTfLW2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ تلگرام: ورود دستیار هوشمند به پروفایل شخصی!
تلگرام در آپدیت جدید تمرکز ویژه‌ای روی هوش مصنوعی داشته است. در ادامه مهم‌ترین تغییرات این نسخه را مرور می‌کنیم:
🔹
ربات‌های مهمان:
فراخوانی ربات‌ها در هر چت یا گروهی، تنها با تگ کردن آیدی و بدون نیاز به افزودن آن‌ها.
🔸
منشی شخصی هوشمند:
قابلیت اتصال مستقیم یک ربات به پروفایل شخصی تا در غیاب شما به پیام‌ها پاسخ دهد!
🔹
تعاملات زنده هوش مصنوعی:
تایپ و نمایش لحظه‌ای پاسخ ربات‌ها، به همراه قابلیت جدید ارتباط ربات با ربات برای انجام وظایف پیچیده‌تر.
🔸
امکانات جدید برای کانال‌ها و تولید محتوا:
قابلیت محدود کردن نظرسنجی‌ها (بر اساس کشور یا عضویت در کانال)، مشاهده نمودار آرا، و همچنین ساخت استایل‌های متنی سفارشی.
🔹
اضافه شدن قابلیت انتخاب فونت از سیستم خودتون (میتونید فونت وزیر رو نصب کنید و استفاده کنید).
با این به‌روزرسانی که شامل جستجوی هوشمند ایموجی‌ها، ارسال بی‌صدای پیام زمان‌بندی‌شده و رفع ۲۰۰ باگ فنی است، تلگرام قدم بزرگی برای ادغام کامل پیام‌رسانی انسان و هوش مصنوعی برداشته است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/iaghapour/2591" target="_blank">📅 14:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
مومن‌نسب: فضای مجازی به هیچ وجه نباید به حالت قبل برگردد
حالا این آدم انقدر مهم نیست که دربارش صحبت کنیم ولی خواستم بگم این همون آدمیه که چندسال پیش تو صداوسیما میگفت من خطرات اینترنت رو میدونم و اطلاع دارم یک نفر با 2 گیگ اینترنت حامله شده و پدر دختره با گریه اینو برای من تعریف می‌کرد...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/iaghapour/2590" target="_blank">📅 11:35 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
اطلاعیه مهم: معرفی فروشندگان کانفیگ
طبق نتایج
نظرسنجی اخیر،
قصد داریم فروشندگان قدیمی و معتبری که از قبل می‌شناسیم را یکی‌یکی برای خرید به شما معرفی کنیم.
📌
قوانین و شرایط مربوط به فروشندگان:
—
عدم پذیرش فروشنده جدید:
در حال حاضر شخص جدیدی معرفی نمی‌شود؛ بنابراین لطفاً در قسمت
«تماس با ما»
برای معرفی خود پیام ندهید. افرادی که معرفی می‌شوند، همگی پیش‌تر در کانال ما سابقه تبلیغ داشته‌اند.
—
تضمین خرید شما:
مبلغی از پول این افراد نزد ما به عنوان امانت می‌ماند تا در صورت بروز هرگونه مشکل، بتوانیم مطالبات شما کاربران عزیز را پیگیری کنیم.
—
ضمانت بازگشت وجه:
این فروشندگان موظف‌اند در صورت لزوم (بسته به شرایطی که خودشان به شما اعلام می‌کنند)، بین ۴۸ تا ۷۲ ساعت امکان عودت وجه را فراهم کنند.
—
قیمت منصفانه:
تمامی این افراد تعهد داده‌اند که نسبت به شرایط بازار، قیمت‌های منصفانه‌تری برای کاربران کانال ما در نظر بگیرند.
— معرفی فروشندگان صرفاً در زمینه
فروش کانفیگ
انجام می‌شود. هیچ‌یک از فروشندگان معرفی‌شده مجاز نیستند پس از معرفی، در کانال شخصی خود تبلیغات مربوط به "
اوتباند
" قرار دهند و یا به کاربران پیشنهاد خرید آن را بدهند.
⚠️
نکات مهم برای کاربران عزیز:
—
انتظارات از کیفیت:
کانفیگ‌ها باید بتوانند تلگرام، اینستاگرام و یوتیوب را به راحتی باز کنند. با توجه به شرایط فعلی اینترنت، داشتن سرعت‌های بسیار بالایِ گذشته کمی دور از انتظار است (هرچند ممکن است کیفیت سرویس‌ها عالی باشد)، پس لطفاً واقع‌بین باشید.
—
اختلال و پشتیبانی:
ممکن است در طول هفته، گاهی با اختلال مواجه شوید. پشتیبان‌ها موظف‌اند در سریع‌ترین زمان ممکن مشکل را حل کنند؛ اما لطفاً صبور باشید، حداقل یک ساعت به آن‌ها فرصت دهید و از ایجاد فشار زودهنگام به پشتیبانی کانال‌ها خودداری کنید.
— در ضمن، توجه داشته باشید که
ما ذی‌نفع این کانال‌ها نیستیم
و فقط به دلیل درخواست‌های زیاد شما این دوستان را معرفی می‌کنیم.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/iaghapour/2589" target="_blank">📅 23:36 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyyJF9XBsp8gSP53g6YhTWbZU_YSQ9OcMQXmmDT7ohZqyj_xdTSFLV2ngAExhRIDLSxVHAWvYaeOxPkue4S75ad40r-O9eT6Sjve-HMOoaXVGZrUlNqmwlnD2poA0zc-5GOliR1e7yz0LGuATG2QeuhsoOg3cV4p9R4j9nExV83_3hqB93b6yPPPpjFc1A5XCzNLUsGGPrY3Fx4nEdf6Vg51qTvK4oI3OIwZIEGYrJp5M_fZJpHR0f_IRaKQ1Ti-Jiez1LxsaZcLQyGdJ3O2Q_qndmoh2nRoaIMVpBVhPN5GX8R_wEMkqKPMAdTnyeHOY9U_qJ9qgtpRD3t6aDL23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
سخنگو وزارت خارجه حذف تیک آبی خود در شبکه X را (سرکوب حقیقت) خواند.
68 روزه اینترنت مردم ایران رو قطع کردن، بعد یه تیک آبی‌شو گرفتن میگه حقیقت سرکوب شد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/iaghapour/2588" target="_blank">📅 20:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔻
تسنیم: درآمد طرح اینترنت «پرو» در سال به ۹۶ هزار میلیارد تومن می‌رسه!
🔹
خب با این رقم‌های نجومی و پول هنگفتی که درمیاد، معلومه که از این تبعیضی که راه انداختن حسابی راضی‌ان. وقتی محدودیت و فیلترینگ این‌قدر براشون سود داره، چرا نباید اینترنت داخلی و بسته رو بیشتر تحویل بگیرن؟
🔸
این وسط یه تشکر ویژه و خسته نباشید هم باید بگیم به اون دسته از دوستانی که رفتن تو صف اینترنت پرو و این سیستم طبقاتی رو خیلی راحت پذیرفتن. از رئیس فلان اتحادیه و مدیر فلان اداره بگیر تا نماینده صنف لاستیک‌فروش‌ها و یه سری کسب‌وکارهایی که واقعاً بدون اینترنت آزاد هم کارشون لنگ نمی‌موند. تو شرایطی که ۹۹ درصد مردم هیچ دسترسیِ عادی به اینترنت آزاد ندارن، مرسی از شماها که رفتین این اینترنت رو گرفتین و با این کارتون، قشنگ به این تبعیض و نابرابری رسمیت دادین!
پ.ن: البته به این نکته هم توجه کنید که خبرگذاری داخلی اینو گفته و ممکنه دقیقا مقصودشون از این حرف هم همین باشه که بگن چقدر این طرح خوب و سودآور هستش و...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/iaghapour/2587" target="_blank">📅 14:33 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⭕️
وعده بازگشت به وضعیت عادی؛ توجیه محدودیت‌ها یا امید به بهبود اینترنت؟
معاون ارتباطات دفتر رئیس‌جمهور به تازگی اعلام کرده که وضعیت فعلی اینترنت مورد تایید دولت نیست و رئیس‌جمهور، محمدرضا عارف را مامور ساماندهی این شرایط کرده است. به گفته او، این محدودیت‌های شدید و قطعی‌ها صرفا تصمیماتی از سوی شورای عالی امنیت ملی و به دلیل شرایط خاص امنیتی و جنگی بوده‌اند.
🔹
وعده روزهای بهتر:
این مقام مسئول قول داده که با عبور از این شرایط ویژه، اینترنت نه تنها به حالت قبل برمی‌گردد، بلکه وضعیتی بهتر از گذشته پیدا خواهد کرد و وعده‌های انتخاباتی رئیس‌جمهور در این زمینه همچنان پیگیری می‌شوند.
🔸
دفاع از اینترنت پرو:
در واکنش به انتقادات، دولت ادعا می‌کند طرح «اینترنت پرو» صرفا برای نجات کسب‌وکارها در روزهای محدودیت ایجاد شده و نباید به آن برچسب اینترنت طبقاتی زد؛ چرا که به گفته آن‌ها، در شرایط عادی اصلا نیازی به چنین طرحی نخواهد بود.
🔹
کاهش محدودیت‌های عمومی:
خبر دیگر این است که قرار شده تدابیر جدیدی برای دسترسی بهتر سایر شهروندان به اینترنت اتخاذ شود تا فشار محدودیت‌های فعلی روی مردم کاهش یابد.
در حالی که دولت تلاش می‌کند قطعی‌ها و طرح‌های بحث‌برانگیزی مثل اینترنت پرو را صرفا به شرایط اضطراری گره بزند، کاربران و کسب‌وکارها همچنان منتظرند تا ببینند آیا این وعده‌ها در عمل به یک اینترنت آزاد و بدون محدودیت ختم می‌شود یا صرفا وعده‌ای برای کنترل نارضایتی‌های فعلی است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/iaghapour/2585" target="_blank">📅 21:12 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭕️
ایده عجیب در مجلس: تاسیس «اینستاگرام دولتی» و مدیریت کامل اینترنت!
نمایندگان مجلس در تازه‌ترین نشست خود با وزیر ارتباطات، از طرح‌ها و نگاه‌های جدیدی برای کنترل بیشتر فضای مجازی پرده برداشتند. در این جلسه، پیشنهاد ایجاد یک پلتفرم کاملا دولتی مشابه اینستاگرام مطرح شد تا به زعم آن‌ها، نیاز کشور برطرف شود.
🔹
اینستاگرام دولتی:
یکی از نمایندگان با اشاره به بازار سیاه و چند میلیونی فیلترشکن‌ها، رسما پیشنهاد ساخت یک سکوی دولتی شبیه اینستاگرام را برای پر کردن جای خالی این پلتفرم ارائه داده است.
🔸
رویای مدیریت اینترنت:
نایب رئیس مجلس تاکید کرده که مشکل آن‌ها اصل اینترنت نیست، بلکه می‌خواهند در صحنه بین‌المللی، مدیریت اینترنت کاملا در دست خودشان باشد و این فضا را به یک جبهه تقابل تشبیه کرده است.
🔹
فرصت‌سازی از بحران:
بخش قابل توجهی از صحبت‌های نمایندگان، حسرت خوردن برای از دست رفتن فرصت در شرایط ملتهب و جنگی است؛ آن‌ها معتقدند باید از این شرایط استفاده می‌کردند تا مردم و کسب‌وکارها به اجبار به سمت سکوهای داخلی کوچ کنند.
این صحبت‌ها به وضوح نشان می‌دهد که دغدغه اصلی، کاهش نارضایتی مردم از قیمت و کیفیت اینترنت نیست؛ بلکه تلاش برای بومی‌سازی اجباری، قطع ارتباط با شبکه‌های اجتماعی بین‌المللی و کشاندن کاربران به پلتفرم‌های تحت کنترل و نظارت است. / زومیت
✍🏻
پ.ن: از سوپر اپلیکیشن های ایتا و سروش و گپ و بله که از تلگرام کپی کردین مشخصه توانایی اینکار رو دارید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/iaghapour/2584" target="_blank">📅 19:36 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
مرگ خاموش اقتصاد خرد: نابودی ۴۰ درصد از کسب‌وکارهای اینستاگرامی!
قطعی‌ها و محدودیت‌های اینترنتی فقط حق دسترسی آزاد ما به شبکه‌های اجتماعی را سلب نکرده، بلکه تیشه به ریشه‌ی اقتصاد خرد و معیشت مردم زده است. طبق اعلام پشوتن پورپزشک، عضو هیئت‌مدیره اتحادیه کسب‌وکارهای مجازی، فیلترینگ و اختلالات باعث نابودی بخش عظیمی از مشاغل آنلاین شده است.
🔹
فاجعه‌ی آماری: نزدیک به ۴۰ درصد از کسب‌وکارهای اینستاگرامی برای همیشه از بین رفته‌اند؛ این یعنی مرگ مستقیم بیش از ۴۰۰ هزار شغل!
🔸
دومینوی ویرانی: وقتی شوکی مثل محدودیت اینترنت وارد می‌شود، ابتدا کسب‌وکارهای کوچک و آسیب‌پذیر می‌میرند، اما این نابودی با کمی تاخیر گریبان شرکت‌های بزرگ اقتصادی را هم خواهد گرفت.
🔹
زنجیره‌ی به هم پیوسته: کسب‌وکارهای بزرگ در تولید، تامین و توزیع به شدت به همین کسب‌وکارهای خرد وابسته‌اند. توهم مصونیت برای شرکت‌های بزرگ، در نهایت منجر به فروپاشی خود آن‌ها می‌شود. منبع: زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/iaghapour/2583" target="_blank">📅 19:29 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسم این زندگــــــی نبود
یک مبارزه تمام عیار بود...
#جوانی
#زندگی
#جنگ
#اینترنت</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/iaghapour/2581" target="_blank">📅 19:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
حل مشکل دانلود از ریلیز گیت‌هاب با LatestReleaseMirror
اگر در دانلود فایل‌ها از بخش ریلیزهای (Releases) گیت‌هاب به دلیل محدودیت‌های اینترنت مشکل دارید، این اسکریپت کاربردی دقیقاً برای شما ساخته شده است!
ابزار
LatestReleaseMirror
به صورت خودکار فایل‌های آخرین آپدیتِ ریپازیتوری‌های دلخواه شما را دریافت کرده و آن‌ها را به عنوان فایل‌های عادی در ساختار پوشه‌های گیت‌هاب ذخیره می‌کند؛ در نتیجه می‌توانید آن‌ها را به راحتی و حتی با اینترنت داخلی دانلود کنید.
🔹
دریافت و آپدیت خودکار آخرین نسخه با استفاده از GitHub Actions.
🔸
امکان فیلتر کردن فایل‌های مورد نیاز (مثلاً فقط نسخه‌های ویندوز یا اندروید)
🔹
دسته‌بندی تمیز فایل‌های خروجی در مسیرهای مشخص.
🔗
لینک ریپازیتوری و راهنمای استفاده
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/iaghapour/2580" target="_blank">📅 16:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ركورد جديد سرعت اينترنت ژاپن:
با سرعت 1.02 پتابيت بر ثانيه، كل نتفليكس را در 1 ثانيه دانلود مى‌كند.
✍
ما هم اینجا باید با DNStt وصل بشیم تا بزور بتونیم فقط این خبر رو بخونیم...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/iaghapour/2579" target="_blank">📅 13:56 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⭕️
اسکریپت بهینه شده XHTTP Relay ECO برای Vercel Pro
🔹
نسخه ECO طوری تیون شده که علاوه بر امنیت سفت‌وسخت v1.3، کم‌هزینه‌ترین رفتار ممکن روی Vercel Pro رو داشته باشه؛ یعنی با کنترل هوشمند Timeout، Inflight، Throttle و Logها، مصرف منابع و هزینه نهایی تا جای ممکن پایین نگه داشته میشه.
🔸
فقط با GET، HEAD و POST کار می‌کنه تا امنیت بالاتر بره.
🔹
احراز هویت فقط از طریق هدر x-relay-key انجام میشه
🔸
هدرهای اضافی پلتفرم و hop-by-hop رو بی‌رحمانه فیلتر می‌کنیم.
🔹
روی آپلود و دانلود محدودیت سرعت (Throttling) واقعی گذاشتیم.
🔸
بردیمش روی Node runtime با لیمیت ۱۲۸ مگابایت رم و مدیریت کانکشن‌های همزمان.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/iaghapour/2578" target="_blank">📅 22:28 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭕️
ورژن جدید کلاینت اندروید GooseRelayVPN منتشر شد
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
هسته پروژه به ورژن 1.5.0 آپدیت شد.
🔸
قابلیت fake dns اضافه شد.
🔹
باگ ها در این نسخه برطرف شدن.
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/iaghapour/2577" target="_blank">📅 14:05 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiS5WD12DVa7mYptOZ-bjMtf6hNPBKkxSt7qEcMKDyUi4RrtPpoh2dC98OEFKVsG4gyLujgcvrC3Iecp4h8SU3Wdg4_1ODs7wFQyrZDawaiePcYIuLd97Devcf0epeh3dAJhmCFgxMahiwQpmYaeF_sPtwgwQyunnSljNYHeqyDw_o_k_I5Q-smSR7LmFQHvOTfMjWPr-xUfQ4oQTtEk3jS5hZikry0iJObt__ktlFAxbJOiK1eVaTZIeHLx9zIPRZuGb29I4-2M_16viXWlZkn9IstAi12-FR9B15b5XbfNfRiRtbNHeLfWfJ1SjTbyTwKhxMvqGSDP9s6GOizDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن رایگان و شخصی به 2 روش با نت ملی
🔹
با استفاده از دو ابزار قدرتمند MHRV و Nova-Proxy، دیگه نیازی به خرید کانفیگ‌ها و سرورهای گرون‌قیمت ندارید. تو این آموزش قدم‌به‌قدم به ۲ روش مختلف پیش میریم تا بتونید یه اتصال پایدار و بدون قطعی داشته باشید. حتماً تا آخر ویدیو همراه من باشید.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔹
دانلود کلاینت ویندوز
🔸
دانلود کلاینت اندروید
#آموزش
#فیلترشکن
#mhrv
#novaproxy
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
@iaghapour</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/iaghapour/2576" target="_blank">📅 19:53 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFoejPmVuBX59_f8emVMtCyW8becp2PmIRIW1fbd1dwqSH5QWSYMX4G7BOX8HIwSAhRguiEdcWnQtQ91bK_qGazLIwvyHGBqZ3IAD5e6WByBRC0e8-J9xU0_HX1B5VSv556-XRkTx8p-WDIMb-TrfIdRW_lOI7xzNoWq-klh-2eOcXKjHkuEcYR3xR38m_BamipZs1FeERA907EnsbDvfCHcmWOXU8TsAYfcwEH_xxAnG3idA_igyiScKpVVZhUtIoqli5T8f7seRgGRaGpkR6rG_9z7Rzhrit5OJ7dIeTy2OO-XtSHyLJ0eHkxLsfF3WrsdZ6RW2j14OQdqYjfNXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پشت‌پرده‌ی «اینترنت پرو»؛ امتیاز ویژه یا تله‌ی نظارتی؟
این روزها سیم‌کارت‌های بدون فیلتر با نام «اینترنت پرو» در ازای دریافت هزینه و ثبت کامل مشخصات هویتی به فروش می‌رسند. اما هدف اصلی این طرح، دلسوزی برای نیاز اینترنتی اقشار مختلف نیست.
هدف اصلی و پنهان این ماجرا، چیزی جز «تشخیص هویت دقیق و رصد لحظه‌ایِ کاربر» نیست.
👁‍🗨
وقتی اینترنت آزاد را مستقیماً با نام و کد ملی خودتان دریافت می‌کنید دقیقاً چه اتفاقی می‌افتد؟
🔹
پایان گمنامی:
تمام سایت‌هایی که سر می‌زنید و محتوایی که می‌بینید، مستقیماً و شفاف روی نام خودتان ثبت و مانیتور می‌شود.
🔸
تزریق خودسانسوری:
وقتی می‌دانید هر کلیک شما رصد می‌شود، ناخودآگاه وارد یک «زندان شیشه‌ای» می‌شوید که خودتان هزینه‌اش را داده‌اید!
🔹
تجارت با حقوق اولیه:
حق بدیهی دسترسی به اینترنت آزاد را مسدود کرده‌اند و حالا همان را به قیمت نقض حریم خصوصی، به عنوان یک «آپشن ویژه» به خودمان می‌فروشند.
«اینترنت پرو» یک امکان رفاهی نیست؛ ابزاری برای کنترل نقطه‌ای و عادی‌سازیِ اینترنت طبقاتی است. بهای اصلی این سیم‌کارت‌ها پول نیست؛ حریم خصوصی ماست.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/iaghapour/2575" target="_blank">📅 15:30 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnQ_9IF8Jj1S9h9v2KQomFw-JWG9cjMjCKskWdYgIM2Lvikt3ht1ebLmeNCQkiACtqYm-G4D0iboPNtY_737d8d3rpmlzT7EjArJsdYxrys8_xaUNy3vP7Sy8gAZyxEPItC4XNx04KLUGsCxnx4j__rqR3wWRkf_GQSSlYzT5BMYuainIrLiYgRk3KbUzZI8xwcYd2rPxpzZksfE2HACt9Beey-l3POfxM9h1YPp6wTB7xnAVJyr7AOSJMcEJXwXRexb2SxKv7hzrEttcgGFufqJ3zvmfGxBB_0Msm8l5gHAo1SebO4Wl9XWddO4r8zbt4j9OKj6byJmGJwbO0CHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کلاینت اندروید GooseRelayVPN
🔹
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
پیکربندی مبتنی بر پروفایل
🔸
وضعیت و تله‌متری در صفحه Home
🔹
تب Logs برای عیب‌یابی Android/Core
🔸
قابلیت Split Tunneling و Internet Sharing
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/iaghapour/2573" target="_blank">📅 20:06 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">💢
رئیس اتحادیه کسب‌وکارهای مجازی
:
به شرکت‌ها زنگ می‌زنند و پیشنهاد فروش اینترنت بدون فیلتر(پرو) برای کارمندانشان را می‌دهند.
⁉️
اگر موضوع واقعاً امنیت ملی است، چطور با پرداخت پول، امنیت تأمین می‌شود؟!
منبع: کانال خبری
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/iaghapour/2572" target="_blank">📅 13:23 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-poll">
<h4>📊 ⁉️نظرسنجی درباره سوال بالا (اگه واقعا نیاز دارید بله رو بزنید).</h4>
<ul>
<li>✓ بله معرفی بشه.</li>
<li>✓ خیر نیازی نیست.</li>
</ul>
</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/iaghapour/2571" target="_blank">📅 00:25 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✍🏻
دوستان، همان‌طور که خودتون در جریان هستید، من در این چند ماه حتی یک مورد
تبلیغ فیلترشکن، اوتباند
و موارد مشابه
قرار ندادم.
الان هم واقعاً تمایلی به این کار ندارم، چون شرایط اصلاً به‌گونه‌ای نیست که بشه کسی را معرفی کرد.
با این حال، در همین چند ماه پیام‌های بسیار زیادی داشتیم که درخواست می‌کردند حتماً یک شخص معتبر را معرفی کنیم؛ چرا که خیلی‌ها از کلاهبرداری‌های پیاپی خسته شدن و ارسال این دست پیام‌ها تا به همین امروز هم ادامه داره.
به همین دلیل، اگه خودتون موافق باشید،
افرادی رو که
از قبل با ما همکاری می‌کردند
و تا حدودی قابل‌اطمینان هستند، یکی‌یکی به شما معرفی کنیم. در این مورد ذکر چند نکته ضروری هستش:
🔸
عدم تضمین صددرصدی:
ناگفته نماند ما واقعاً نمیتونیم کسی را با اطمینان ۱۰۰ درصدی تأیید کنیم، اما افرادی که معرفی میشن همگی سابقه همکاری با ما را دارن.
🔹
عدم پذیرش تبلیغ جدید و اوتباند:
تا زمانی که شرایط استیبل و پایدار نشود، تبلیغ
هیچ فرد جدیدی را قبول نمی‌کنیم.
در ضمن،
تبلیغ فروش اوتباند هم به‌هیچ‌وجه پذیرفته نمی‌شود.
🔸
قیمت‌های منصفانه:
تمام سعی ما بر اینه افرادی را معرفی کنیم که در این زمینه منصف باشند و قیمت‌های بالایی ارائه ندهند. ولی خب، طبیعتاً نمیشه انتظار قیمت‌های قدیمی را داشت؛ چون همان‌طور که خودتون میدونید در حال حاضر هیچ‌کس با اون قیمت‌های قبلی فروشی نداره.
اگه تمایل دارید، لطفاً در نظرسنجی زیر شرکت کنید.
البته نظر شخصی خودم اینه که اگه در حال حاضر واقعاً مشکل خاصی ندارید، در نظرسنجی همان گزینه
(خیر) را انتخاب کنید
.</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/iaghapour/2570" target="_blank">📅 00:24 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚠️
هشدار مهم درباره اسکریپت VPN Over GitHub
▪️
لطفاً از این ابزار به عنوان
فیلترشکن
استفاده نکنید!
🚫
بن شدن اکانت:
تبدیل گیت‌هاب به تونل ترافیک، خلاف قوانین این سایت است و خیلی زود باعث مسدود شدن حساب شما می‌شود.
🐢
سرعت بسیار پایین:
برای هر ارتباط به یک بار
push
و
pull
نیاز دارد که آن را عملاً غیرقابل استفاده می‌کند.
🔻
خطر برای برنامه‌نویس‌ها:
گیت‌هاب یک سایت حیاتی برای توسعه‌دهندگان است؛ سوءاستفاده از آن ممکن است باعث حساسیت شده و دسترسی به این پلتفرم مهم را دوباره از کار بیندازد. (خارج شدن از لیست سفید و...)
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/iaghapour/2569" target="_blank">📅 19:21 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ای بابا روش Vercel چرا بسته شد؟ هنوز آموزش نداده بودم که.
😁
سازمان فیلترینگ زرنگ شده ها. فک کنم خودشون رو آپدیت کردن دیگه به کانال من نگاه نمیکنن :)</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/iaghapour/2567" target="_blank">📅 16:34 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
دلار 177 و طلا 19,400,000
شب میخوابی صبح بلند میشی یه پله بدبخت تر میشی!</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/iaghapour/2566" target="_blank">📅 11:10 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حالا نیاز نیست پول بدین ری اکشن فیک بزنید.
😁</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/iaghapour/2565" target="_blank">📅 20:52 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GooseRelayVPN Guid -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.2 KB</div>
</div>
<a href="https://t.me/iaghapour/2564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
دستورات
برای ویدیو
GooseRelayVPN
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/iaghapour/2564" target="_blank">📅 14:21 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjNv98mvNSlX8mghAxH7eUltDMSoUFyYeyOvqsoCJGW8sVy4l97-hWGyrFmPhfyuPztG9eUNpCI5zbXkLSIIKiEbMn16V_bLvVkvMHatYmb-l3n8mmgA7CsaAY935e__DjYHQ9A1WGWauCuAmM2L6i9g5D6YZ39nlLcHWOz8d0TcJz1mzfLpy2a4EcF6xZpVPHAMhTaKxf3BKJr4FgIG8AuRcdbOCc041I3YSg0JrHIcmam48i1INO_wlLt9Dg0jFnGhCyLM-3BgIwmb-LBF9Iwwpsj1bSsPFfgE1iPAHyuAv0dii7edQG4mHxNQd_mZF-IhoN66Z5gdDy-8PsyMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن شخصی و تانلینگ امن با سرویس‌های ابری! (GooseRelayVPN)
🔹
در این آموزش، یک روش عالی به نام GooseRelayVPN رو بهتون معرفی می‌کنم. با استفاده از اسکریپت‌های ابری (Apps Script) به عنوان واسطه و اتصال اون به سرور لینوکسی خودمون، یک تانل امن میسازیم.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔻
دانلود فایل کدها
#آموزش
#فیلترشکن
#گوگل
#تانل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/iaghapour/2563" target="_blank">📅 14:18 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✍🏻
از اونجایی که دیگه کسی حوصله خوندن خبر رو نداره براتون عناوین خبر رو قرار دادم :)
🔸
دو ماه قطعی اینترنت؛ تعدیل ۳۰ تا ۵۰ درصدی نیروی انسانی در شرکت‌های اینترنت اشیا
🔹
ثبت ۳۱۸ هزار درخواست کار در یک روز در جاب‌ویژن
🔸
کانون وکلای اصفهان هم اینترنت «پرو» را نپذیرفت
🔹
ارسال پیامک اینترنت «پرو» این بار برای مهندسان
🔸
خزنده‌های گوگل پس از ۶۰ روز قطعی، دوباره سایت‌های ایرانی را می‌بینند
🔹
ضربه سنگین قطعی اینترنت به اشتغال زنان
🔸
دبیر سابق شورای‌ عالی فضای مجازی: اینترنت بین‌الملل می‌تواند ظرف ۵ دقیقه وصل شود.
🔹
سخنگوی دولت: با پایان بحران وضعیت اینترنت تغییر خواهد کرد
منبع: زومیت - دیجیاتو
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/iaghapour/2562" target="_blank">📅 11:54 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اسکریپت KevinNet DNS با پشتیبانی از VayDNS آپدیت شد
حدودا 1 هفته پیش یک آموزش ضبط شده به اسم
(بهینه ترین روش اتصال با پروتکل DNS)
و توی این ویدیو ما اومدیم اسکریپت
KevinNet
رو معرفی کردیم. و الان در آپدیت جدید میتونه از VayDns هم ساپورت کنه.
🔹
اضافه شدن قابلیت تغییر مقادیر در برنامه
🔸
قابلیت تست ریزالور حتی در vaydns
🔹
قابلیت ایجاد پروفایل متعدد برای دامنه
. قابلیت های دیگه ...
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/iaghapour/2559" target="_blank">📅 19:22 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol06pBLTmln75fl2_96_S5x28cPN2ji_w4jAKmCqHwQO6Sv7pNLBXzjFelphMeBlaQa32a_wP5zVBUMZGxZYd-pnPB41WEhzrrd3ZBi_kIJQQiipkJGuiErlV7058t-YSDkQs-8IOgUW8sywkCtmBV2qND2XdM1HyVm5I7AUOZk9UA9iR7vrOp1mMrnMC1ys3-HkQOBNEjznbFb3nFveD-7Qrc3vZOTHmCWtRltJFMymTCmb-CwNiQ3iCSqHtrm1RFrCJjgiP22twC_MHY40OAlt37AKQHuRhXt29Ugc7fgl_vZG1etQSrFr6d5casjAlHBvjjxlQjWa4hKpkta9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت هارد ۱۰ ترابایت بنفش (Western Digital Purple) ناقابل 108 میلیون
🫠
همینطوری ادامه داشته باشه برای خرید یک گوشی دکمه ای هم باید همین مقدار پول بدیم....
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/iaghapour/2558" target="_blank">📅 09:34 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gglRtbmnOcGArKxlWPQ6uqLS84bU4Ijc_N064GDX_jyED-5fp0xxsBmbij7B9yjVAW_ir37Hvjsih4E2Rbbmpu-PqIL58XXrWiO-JaWlsE32zWHnEP_r1XglC0CjyPkL0EmLmsmiQKL8kyQZm-4d8VpeZFJ5y1AM8zNodcYrHR2xY-cfi69m3_lBySMcpGdqjpe7g4M3Y_eO_pF7n-lFyIZ-V7QWYNaHvq7GR2Vmr8vSCZpAEAVkHb1PiuslYsHec4YP7OA2cEBE9N_JZCZCi0nKopa9Ma1U6NLOZI5Ebl1Ho0t9-DKJ_rAV7elt05IeqhZOyWgiJzwzOHXjLaCBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نصب‌کننده خودکار Parley Chat
🔻
از اونجایی که راه‌اندازی و کانفیگ کامل یک پلتفرم چت روی سرور (با تمام دردسرهای تنظیم دیتابیس، وب‌سرور و گواهینامه امنیتی) کار سخت و زمان‌بریه، این ابزار جذاب اومده تا همه چیز رو براتون ساده کنه!
🔸
راه‌اندازی کامل بکند (Backend) و فرانت‌اند (Frontend)
🔹
کانفیگ خودکار Nginx به همراه دریافت گواهینامه SSL
🔸
ایجاد سرویس‌های Systemd برای مدیریت آسان‌تر و پایداری سرویس
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/iaghapour/2557" target="_blank">📅 21:48 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urmz1QhgRIZsixYHNth91ulGy-0NkF_1hx6eETN0bM2E4mTZalFjzwAMuOFfc4tsf5O2XJBlPNST9wjYADHFq4beyGy_daN6eS-YA0F0oW8mYbaubiztn7lyNjlxdhbbtF0kiy3dOsRBatot3psd-mVDaIscuecZEAP3gFMYg_CoZRY43FSiaOJsyxXFdbj4ox2oXfJm_614AJw8tXp3NkKmRhCEx4zzgEh3FUm7keHWWAWIX4uDHZQrY3bavN-KcMDOtVEvYWQwAn_9yCADieiLwMpZdp-_vMzv-uacf-p9K0FvDWNkCUG2OeEzvCwITz11vQJyQlogayuybgv0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
لینک همه سایت‌های کاربردی تو این سایته!
🔹
از اونجایی که پیدا کردن لینک سایت‌های کاربردی در دسته‌بندی‌های مختلف مثل آپلودسنترها، سایت‌های دانلود فیلم و سریال، ابزارهای آنلاین و... خیلی سخت و زمان‌بر شده، سایت WebDX اومده همه این‌ها رو به صورت منظم و دسته‌بندی شده یک جا جمع‌آوری کرده.
🔗
لینک ورود به سایت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/iaghapour/2556" target="_blank">📅 21:40 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">💢
سازمان نظام پرستاری:
با وجود اینکه امکان برقراری اینترنت پرو برای اعضای خود را داریم، تا زمانی که همه مردم ایران به اینترنت متصل نشوند از این امکان استفاده نخواهیم کرد.
🔴
در اطلاعیه کامل سازمان نظام پرستاری:
«بسمه تعالی
سازمان نظام پرستاری جمهوری اسلامی ایران به اطلاع کلیه پرستاران و مردم عزیز ایران می‌رساند؛ با توجه به محدودیت‌های ایجادشده در دسترسی به اینترنت بین‌الملل به‌دلیل شرایط خاص جنگی کشور و ارائه دسترسی محدود (اینترنت پرو) به برخی اقشار، امکان اعطای این امتیاز به اعضای سازمان نظام پرستاری نیز از سوی مقامات مسئول اعلام شد، لکن سازمان نظام پرستاری جمهوری اسلامی ایران براساس بررسی جوانب مختلف تا زمان رفع محدودیت‌های دسترسی عموم مردم به اینترنت بین‌الملل، درخواست هیچ امتیاز ویژه‌ای را برای اعضای خود نخواهد داشت.
ان‌شالله زمانی که این امکان برای همه مردم ایران فراهم باشد، پرستاران نیز در کنار آحاد مردم از این امکان استفاده خواهند نمود.»
﻿
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/iaghapour/2555" target="_blank">📅 13:20 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLDGYNemGCYYdueZLezx0DtQdijPtIV-Ec3arFZHydAR1eTu9Oymp1ho_Rgba_D1IJ1IxDh9D-AaO7qo8pG-YY9MH1bEMU0pIQvxQJOJbGzXYVCReixjaXn4PjtHSh60lpdSZGgGTN6eknjGg6KxAJ7TfoXhpvH-4nqEUUPbufTuCVuLhLm0zsBrrwgWAWixSeWUWtOaOUtAVzcDrLNm0CIC4WvA3zJIxkNgI_b1KXGjAcdkZSUZdNrNTkk-9Bf300zr-rYH1CGex9WvEjF4afIi9DPG5LZjw6H5y6xIzNr6CvP1mAbr0lL5P4ouwhMjLTPc66WhJud1Q3vp5r8Bkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ربات‌های کاربردی تلگرام برای شرایط اینترنت محدود
با توجه به محدودیت‌های فعلی، این ربات‌ها حکم یک اینترنت آزاد و همه‌کاره را در قلب تلگرام دارند:
🔹
@GPT4Telegrambot
دسترسی به ChatGPT، جمنای و تولید تصویر.
🔸
@WebSearchAiBot
جستجو در گوگل و خواندن محتوای سایت‌های فیلتر شده.
🔹
@apkdl_bot
دانلود مستقیم برنامه‌های گوگل‌پلی (جایگزین استور).
🔸
@SaveAsBot
دانلود ویدیو و عکس از یوتیوب، اینستاگرام و توییتر.
🔹
@reddit_download_bot
دانلود محتوای متنی و تصویری از سایت ردیت.
🔸
@UrlUploadBot
تبدیل لینک دانلود سایت‌ها به فایل مستقیم تلگرامی.
🔹
@ReadabBot
تبدیل مقالات وب به حالت مطالعه سریع در خود تلگرام.
🔸
@vtovbot
تبدیل فایل‌های صوتی پرحجم به ویس باکیفیت و کم‌حجم.
🔹
@voicybot
تبدیل ویس به متن با پشتیبانی از زبان فارسی.
🔸
@fakemailbot
ساخت ایمیل موقت برای زمان‌هایی که جیمیل در دسترس نیست.
🔹
@newfileconverterbot
تغییر فرمت انواع فایل‌ها مثل عکس، ویدیو و داکیومنت.
©️
با تشکر از ایوب عزیز.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/iaghapour/2553" target="_blank">📅 20:41 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2552">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💢
اردستانی؛ نماینده مجلس
:
حکومت تصمیم گرفته فعلا روایت خودشو بیان کنه. برای‌همین به خبرنگارها؛ دانشگاهی ها؛ نماینده های مجلس و هنرمندانی که با حکومت همراهن اینترنت داده تا برای خارجی ها تولید محتوا کنن.
پ.ن: عجب بابا عجب دیگه کار از مخفی کردن و شرمنده بودن و... گذشته. خیلی قشنگ این تبعیض رو فریاد میزنن.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/iaghapour/2552" target="_blank">📅 17:38 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✍🏻
یه تناقض عجیب بین حرفای مسئولین و واقعیت اینترنت کشور هست. از یه طرف رئیس‌جمهور میگه موافق وصل شدن اینترنته، از اون طرف سخنگوی دولت میگه اصلاً اینترنت طبقاتی نداریم و وزیر ارتباطات هم کلاً وجود لیست سفید رو گردن نمی‌گیره.
ولی خب تو عمل، داریم یه جور تبعیض و آپارتاید اینترنتی رو به چشم می‌بینیم:
افراد رانتی:
اینترنت کاملاً آزاد و بدون فیلتر (همون لیست سفید).
شهروندای درجه دو:
یه اینترنتی که بدون فیلترشکن دوزار نمی‌ارزه (همون اینترنت پرو).
مردم عادی:
محدودیت کامل و حبس شدن تو شبکه داخلی.
از همه جالب‌تر مسئولینی هستن که میان میگن این محدودیتا موقتیه. یعنی ۶۰ روز قطعیِ پشت سر هم، معنی «موقت» میده؟ اصلاً می‌دونید موقت یعنی چی؟
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/iaghapour/2551" target="_blank">📅 19:30 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OB-4yiAOhZk6mN3RtXoyHCbXFPKPud9rlx6AhGbOUwxmaf4ySp4z4UFYA0rw-268tZ69Jn_4R_C1XVbnAMKCMuT41lCCnPUUiWOVrLU1FIE8_Co_2nZ517k3usIY7Mx-okKsIuq-_2kk0c5P04iwnAIil0xzO-sP7Xn8z63IzQq-oPbHWk64e9PnC3faBYa6s4Tf3h1vnq-gh_U-YPla-WUelvOq9Sdw8uD8hn1OVyzNJ6gGienipkli9tx5XcpeVguqM_zVPcalqKIyjK39Cn-myaj_BiQJRDG96lVOChyFrlD-DFX4NpZNmjL9uunq6hCyA_Nqrg7IyFV3I7i8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
روز ۵۶ام از قطع اینترنت در
#ایران
هستش و اتصال بین‌المللی بیش از ۱۳۲۰ ساعته که قطع شده و کسی پاسخگو نیست!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/iaghapour/2550" target="_blank">📅 11:19 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚠️
یک یادآوری و هشدار خیلی مهم به دوستان عزیز
دیگه واقعاً حسابش از دستم در رفته که تا حالا چند بار این موضوع رو گفتم، اما باز هم باید تکرار کنم:
ما اصلاً هیچ گروهی نداریم!
متأسفانه بعضی‌ها با استفاده از اسم و عکس ما اقدام به ساخت گروه یا کانال می‌کنند. حتی بعضی‌ها خودشون رو به عنوان «پشتیبانی» ما معرفی می‌کنند. من قصد قضاوت در مورد هدف این افراد رو ندارم، اما این کار باعث سردرگمی شما میشه و اصلاً درست نیست.
لطفاً توجه کنید که فعالیت رسمی ما فقط و فقط در چند آدرس زیر انجام میشه و تمام:
🔸
یوتیوب:
youtube.com/@iAghapour
🔹
کانال تلگرام:
t.me/iaghapour
🤖
ربات تماس با ما:
@iaghapourbot
🐦
توییتر:
(که البته خیلی اونجا فعال نیستم)
نکته مهم: هر گروه، کانال یا شخصی که خارج از این لیستِ بالا خودش رو مرتبط با ما معرفی کرد، هیچ ارتباطی به ما نداره.
ممنون از درک و همراهی همیشگی‌تون!
🌹</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/iaghapour/2547" target="_blank">📅 15:42 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
معرفی پیام‌رسان دلتا چت و سرور Madmail
🔹
یک پیام‌رسان امن و غیرمتمرکز بر بستر ایمیل که حتی در زمان محدودیت‌های اینترنت هم به کارتان می‌آید! با پروژه Madmail می‌توانید به سادگی و سرعت، سرور اختصاصی خودتان را بالا بیاورید.
🔻
ویژگی‌های کلیدی:
- امنیت به شدت بالا: رمزنگاری پیشرفته و عدم نیاز به شماره موبایل.
- مقاوم در برابر قطعی‌ها: امکان راه‌اندازی آسان رله‌ها روی سرورهای داخلی.
- اجرای سرور چت‌میل تنها با یک فایل باینری (حتی روی سرورهای آپدیت‌نشده و بدون اینترنت بین‌الملل).
- پشتیبانی از تماس صوتی و تصویری.
🔗
لینک گیت‌هاب برای بررسی و نصب
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/iaghapour/2545" target="_blank">📅 13:15 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✍🏻
دوستان، اگر برای باز کردن تلگرام و سایت‌های مختلف از روش
MasterHttpRelayVPN
استفاده می‌کنید، حتماً حواستون به این 2 تا نکته مهم باشه:
۱. آی‌پی شما تغییر نمی‌کنه:
برخلاف فیلترشکن‌های عادی، آی‌پی شما تو این روش همون ایران می‌مونه. در نتیجه سایت‌های تحریمی براتون باز نمیشن و حتی ممکنه سایت‌های حساس اکانتتون رو به خاطر آی‌پی ایران بن کنن.
۲. جیمیل اصلی‌تون رو استفاده نکنید:
یه سری گزارش‌ها به دستمون رسیده که گوگل ممکنه اکانت‌ها رو مسدود کنه. با اینکه هنوز مدرک زیادی وجود نداره و قطعی نشده، اما بهتره اصلاً ریسک نکنید و از جیمیل شخصی‌تون استفاده نکنید.
۳. نسخه اندروید رسید:
خبر خوب اینه که از امروز می‌تونید نسخه اندروید این روش رو هم نصب و استفاده کنید.
🔻
ممکنه مواردی رو من پوشش ندم ولی کانال
IRCF
که یکی از قدیمی ترین و بهترین کانال ها هستش میتونه راهنمای شما باشه.</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/iaghapour/2544" target="_blank">📅 13:09 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⁉️
جواب به سوالات پرتکرار شما + بهینه ترین روش اتصال با پروتکل DNS
🔹
توی این ویدیو به پرتکرارترین سوالات شما درباره ساخت فیلترشکن جواب دادم. در نیمه دوم هم یک روش فوق‌العاده و بهینه برای اتصال با پروتکل DNS رو به صورت قدم‌به‌قدم آموزش دادم تا پایداری بیشتری…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/iaghapour/2542" target="_blank">📅 17:08 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU4zM5MLieS9rSQGwkZ9h2kZytPMLkigBoRcau_qrFHZxovY0h-PLWtoI1r8FhRI6MO8W1A0SwDWkeUmf7JJo8-0DROLsEZGZnw1wBoAPPuh3ru0mA_j3cBgNEKgmPbHb0iiSIbv0WCBsaVpQE9b3ntvf-KDYtlmqyTYxTVlrp3bX72vEbs5Yr3DhJslGjl7PUMapQZNiVOoBhwQ3rxF-qeuBjWrt7Y3A_4yPj6HyZiRJu52kXHXD_S81Y-V8y02TFn3yv4TFnYKOLlbtbU2aNyQ4E45kdfZb0sczqSHztGJsDkmlr4lR-l01ICcB0KVjgXGYTOtk6_rLnpl7SlW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
جواب به سوالات پرتکرار شما + بهینه ترین روش اتصال با پروتکل DNS
🔹
توی این ویدیو به پرتکرارترین سوالات شما درباره ساخت فیلترشکن جواب دادم. در نیمه دوم هم یک روش فوق‌العاده و بهینه برای اتصال با پروتکل DNS رو به صورت قدم‌به‌قدم آموزش دادم تا پایداری بیشتری داشته باشید.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔻
دانلود فایل exe اسکریپت
#آموزش
#فیلترشکن
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
@iaghapour</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/iaghapour/2540" target="_blank">📅 16:25 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXygB95YSgUJQcGDEAL2jC1ak3ZsIs3DYdZh76Cz76oyZ8tIJMl1zOueN8rNrNocoEoNCuz7-Uu_9UwlSwh3lgZ7MXzD_IByi8rh_PqkNARwuVGBNywexCV0CRK2nHlkxtj63SnnNmi-Gy-vxKexCrOG00eyHR2cVwDXGbhjczqo8w5RqajqoiZsIqc17AuM0sTgl2Bbnfj7afY7wf2EaYqPB60mvUCg6MXBmYwNhxIm3zTH9LBfcpbhfgUEY-nOamn_TRqYuROvNb_o-RJ6VACF--683HdfqOE5mMG6Yu3GIFb27VPbJGXmvvDPiMNb1PUSLR3dgsoH1hSA9egC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
درخواست ملی کردن کامل اینترنت فقط برای طرفداران نت ملی!
🔹
هرچی از طنز ماجرا بگم کمه :) یک
کارزار
ساختن و گفتن کد ملی طرفدارهای نت ملی رو بگیرید و اینترنت رو برای اونا برای همیشه ملی کنید :)
داداشایی که سنگ اینترنت ملی رو به سینه می‌زنن، بفرما این گوی و این میدان! لطفاً اینترنت این عزیزان رو روی کد ملی‌شون برای همیشه «ملی» کنید تا دیگه غصه ما رو نخورن. ما خودمون یه جوری با این اینترنتِ پر از فسادِ بین‌المللی کنار میایم!
🤣
🔥
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/iaghapour/2537" target="_blank">📅 01:02 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بچه‌ها حجم پیام‌ها اون‌قدر زیاده که اون عزیزی که به عنوان پشتیبان داره همکاری میکنه با ما واقعاً نمی‌رسه همه رو سریع بخونه یا جواب بده. شرمنده‌ی روی ماهتونیم و بابت این موضوع از همگی عذر می‌خوایم.
🙏🏻
🌹</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/iaghapour/2535" target="_blank">📅 00:37 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭕️
آپدیت مسنجر سانگبرد منتشر شد
(
v0.9.0
)
🔹
با اسکریپت زیر میتونید روی سرور ایران یک مسنجر شخصی برای خودتون و خانواده بسازید.
-
📥
قابلیت آپدیت آفلاین برنامه از اسکریپت
-
🔒
رمزنگاری Client-Server
-
📃
قابلیت Context Menu اختصاصی برنامه
-
↪️
قابلیت فوروارد کردن پیام
-
🗑
قابلیت پاک کردن پیام (یک طرفه و دو طرفه)
-
✏️
قابلیت ادیت پیام
-
💬
قابلیت پاک کردن خودکار پیام های متنی
-
📜
امکان دریافت سرتیفیکیت 6 روزه برای IP در اسکریپت
-
♻️
دستور بازیابی دیتابیس از بکاپ در اسکریپت
-
🚫
دستور بن کردن یوزرها در اسکریپت
-
✨
بهبود UI/UX
-
📜
قابلیت نصب سرتیفیکیت با فایل های کلید SSL
-
👤
دستور ادیت مشخصات یوزر در اسکریپت
-
⚙️
قابلیت تنظیم پورت دلخواه برای nginx در حالت نصب با دامنه
-
🔧
به همراه رفع باگ های متعدد
اطلاعات بیشتر در گیت‌هاب
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/iaghapour/2534" target="_blank">📅 00:31 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">2 تا آموزش عمومی و خوب در پیش داریم.
👈🏻
یکی آموزش نصب و اجرا هوش مصنوعی لوکال و بدون اینترنت.
👈🏻
و یک آموزش کاربردی و پاسخ به سوالات پر تکرار شما.
فردا یکی از اینها منتشر میشه.
💚</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/iaghapour/2533" target="_blank">📅 00:26 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✍🏻
همان‌طور که احتمالاً دیده‌اید، اخیراً آموزش‌ها و اسکریپت‌هایی (مشابه Spoof SNI) برای دور زدن فیلترینگ یوتیوب و برخی سایت‌ها منتشر شده است. البته قبلاً هم شاهد موارد مشابه بوده‌ایم.
دلیل اینکه ما این روش‌ها را در کانال قرار ندادیم، درخواست بعضی از دوستان بود! درخواستشان چه بود؟
اینکه روش‌های جدید را «پابلیک» نکنیم
تا مبادا هزاران نفر از مردم عادی از آن استفاده کنند و روش بسته شود؛ در عوض، فقط یک عده محدود بتوانند با خیال راحت از آن لذت ببرند. واقعاً عجب منطق جالب و «ازخودگذشته‌ای»!
😇
ولی خب به هر حال، کانال‌های دیگه این آموزش‌ها را منتشر کردن و میتونید از اون ها استفاده کنید.
این توضیحات هم بماند برای آن دسته از دوستانی که قدرت تفکر دارند و متوجه ماجرا میشن. :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/iaghapour/2532" target="_blank">📅 00:25 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
آتش بس تا اطلاع ثانوی تمدید شد.
🔹
ولی اینترنت باز نمیشه. چون امنیت به خطر میفته. این که 2 ماهه سیستم خودمون و حتی گوشی رو آپدیت نکردیم و آنتی ویروس خودمون رو آپدیت نکردیم و.. خیلی به امنیت آسیبی نمیزنه. حداقل به امنیت ما آسیبی نمیزنه :|</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/iaghapour/2531" target="_blank">📅 00:14 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">💢
رئیس شورای اطلاع رسانی دولت: قطعی اینترنت موقتیه و یکم دندون رو جیگر بزارید تا دشمن رو به یه شکست ذلیلانه بکشونیم بعدش حتما وصل میشه و به شرایط عادی برمیگرده.
پ.ن: کاملا از ثبت نام اینترنت پرو در رسته ها و شغل های مختلف مشخصه دارید راست میگید.
👌
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/iaghapour/2529" target="_blank">📅 17:53 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔻
گوگل و گیت‌هاب دوباره باز شد!
بازی موش و گربه شده قشنگ!
🧐
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/iaghapour/2528" target="_blank">📅 13:31 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚠️
گیت هاب هم بسته شد
احتمال موقت بودن یا اختلال هم وجود داره!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/iaghapour/2525" target="_blank">📅 11:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚠️
گوگل مجدد فیلتر شد
البته وقتی سرچ میکردی سایت های توش رو نمیتونستی باز کنی پس خیلی هم فایده نداشت! مثل این میمونه که بچه رو ببری ویترین اسباب بازی رو بهش نشون بدی ولی بگی حق دست زدن نداری...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/iaghapour/2524" target="_blank">📅 11:44 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtSsj0xHvya39065Nf7P2N7V4ZZc47w-ZS1MX_1WldTy9GkKbpYT8p7OS0dKGj2oz6P1r0fFe8363jXP627K-99jjq459bDYFZGD8kz8uyDDF6TvfDi77LDUyi1trxtWjPa6yPTrETrpckwCagq46tN7WGOAg7FmFexNBBep9t4UEE_MWjd8iyPCI0CmLBM0gbc45LFqcVo1aXoZUl-iBi6VAMwRSV31EqNxil0UtPVpVD_Aqr4E0W57w6YNG07z8tsNsxfcG9jLwQrvqM1qOMFX0WF2RubCX9lKwupoZdVw61qcj80jN18Pqx0plsSM4Od7EqZaDEgBXw3AnU7c7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استارت اینترنت طبقاتی توسط همراه اول!
🔹
همراه اول رسماً از طرح اینترنت طبقاتی خود رونمایی کرد. با افزوده شدن بخش «اشتراک پرو» به منوی این اپراتور، زین‌پس تنها افراد خاصی که فرآیند احراز هویت را طی کرده باشند، امکان دسترسی به این سرویس را خواهند داشت. گفتنی است هزینه بسته ۵۰ گیگابایتی در این اشتراک، ۲ میلیون تومان تعیین شده است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/iaghapour/2523" target="_blank">📅 00:27 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxHfhYI0PVwLVuolxKFShXJ5_YbCyQgILsGLgcBBpJtJzSTWG3zuGEMhjvYyxDUQVjh_8Y8LJIp2ZAO75HkUV1ejYZavk6nuwgdiNq8HorSlKTzaw08M2VnDsGO8msc8QxJgo8IqshCbqWAI7xfGkbYQx3jmVVyFhB-wGxBJYSYK32jmClhVKUDYi3eYNSuJrc_LgYTROzvuhiuv2Zen3frkwGZ5aZbD6l-unrB_WJAE0R78GFUvx4nHIzjydE6CQpbsnD4Vrc_BvUGhoAtnaEDn2CLFubf2NXhtaZKrgfHTee9wXzfVwpi8yBbuWRRZrS8PlOQh3rafUDPesZ_Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
چرا جهان، زندان دیجیتال ایران را نمی‌بیند؟
بیش از دو ماه است که اینترنت در ایران قطع شده و میلیون‌ها نفر در یک «اینترانتِ» محدود و ایزوله حبس شده‌اند. کسب‌وکارها نابود شده و ارتباطات فلج شده است، اما در کمال تعجب، سازمان‌های مدعی حقوق بشر خود را به خواب زده‌اند.
🔻
چرا نهادهای بین‌المللی خفه خون گرفته‌اند؟
سازمان ملل سال‌ها پیش قطع اینترنت را نقض صریح حقوق بشر اعلام کرد. اما ظاهراً وقتی نوبت به ایران می‌رسد، این قوانین چیزی جز کاغذپاره‌های نمایشی نیستند.
اگر اینترنت در یک کشور غربی دو ساعت قطع شود، دنیا جلسه اضطراری می‌گذارد! اما ماه‌ها حبس دیجیتال در ایران، ارزش یک واکنش قاطع را برای آن‌ها ندارد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/iaghapour/2522" target="_blank">📅 19:45 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naK4I7NHL31j1Lke1LHnUJEHv2xK0IMyb7-nFUjteC_PYXu1aVs5WlZCB4lLCeFYZSX3GP5eknAySaqP7lbboyAXE2-83y_iWKmqL160VBv7yY6CrrPR6Fu0PCVg7sReOriEF5Zq9iyVJi3O_TAfZk8TfdX8CZqtTwU6n90brFNB_NxIlPHwRCYcSd_KqG9lLQQiAmIlRQw52gdKNORIhWwFifipwAP44D-f4O_RPoSG9sI8N4pcBmceAjjR99NI1UcNHOc73N2DDYsTbXWSDYteZVbClF0SR5ylr2bIjc_urXiLqrk0-khxOoGoTdGguLa1UejAMVHsbLZJuNPtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین کانفیگ فروش دنیا
😊</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/iaghapour/2521" target="_blank">📅 15:30 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
موج حملات در کمین سایت‌های آپدیت‌نشده!
تو این دو ماه اخیر که اینترنت ملی شده و دسترسی‌ها به شدت محدود بوده، یه خطر امنیتی پنهان اما بسیار بزرگ، خیلی از کسب‌وکارهای آنلاین رو تهدید می‌کنه:
عقب موندن از آپدیت‌ها!
فکرش رو بکنید؛ تو این مدت چقدر سایت وردپرسی و پلتفرم‌های مختلف داریم که هسته اصلی، قالب‌ها و افزونه‌هاشون رنگ آپدیت رو ندیدن؟
⚠️
خطر اصلی کی خودش رو نشون میده؟
دقیقاً همون لحظه‌ای که اینترنت دوباره به حالت عادی برگرده و دسترسی‌های بین‌المللی باز بشه. ربات‌های مخرب و هکرها منتظر همین فرصت هستن تا از باگ‌ها و آسیب‌پذیری‌های امنیتی این چند وقت (که پچ و برطرف نشدن) سوءاستفاده کنن. با وصل شدن اینترنت، باید منتظر یه موج گسترده از حملات هکری و بدافزاری به این سایت‌های بی‌دفاع باشیم.
🛡
چاره چیه؟ (همین الان دست به کار بشید)
آپدیت دستی:
منتظر آپدیت خودکار از پیشخوان نمونید. فایل‌های آپدیت‌شده افزونه‌ها و قالب‌های ضروری رو (از طریق منابع در دسترس یا شبکه‌های داخلی) دانلود کنید و از طریق هاست یا FTP به‌صورت دستی جایگزین کنید.
بک‌آپ‌گیری فوری:
همین الان یه فول‌بک‌آپ از دیتابیس و فایل‌های سایتتون بگیرید و تو یه فضای امن خارج از هاست ذخیره کنید.
محدودسازی دسترسی‌ها:
موقتاً تنظیمات افزونه‌های امنیتی (مثل Wordfence یا iThemes) رو روی حالت سخت‌گیرانه‌تری قرار بدید.
🔄
حتماً این پست رو برای دوستان وب‌مستر، طراحان سایت و صاحبان کسب‌وکار بفرستید تا اونا هم آماده باشن.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/iaghapour/2520" target="_blank">📅 14:32 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یادتونه یه زمانی می‌گفتیم هوش مصنوعی قراره خیلی از ماها رو بیکار کنه؟
هیچکس فکرش رو نمی‌کرد یک روز سیاست فیلترینگ و نت ملی و... نزدیک به 10 میلیون آدم رو بیکار کنه!
بیش از چند ماهه که هزاران کسب و کار نابود شدن و هزاران آرزو مردن! پاسخگو اینها چه کسانی هستن؟ تا کی قراره قطعی اینترنت ادامه داشته باشه؟
#اینترنت_را_وصل_کنید
#اینترنت_ملی
#DigitalBlackOutIran‌
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/iaghapour/2519" target="_blank">📅 11:30 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btCFXHnIJrdubzYTqQPn_ERqFLWQaIPhuYy_1uUogroNfP7bDKMa0Ak3nYZZxsAx03nL7L160VSLmkffO2U3FzgmoyNJUh6yz_iS17EIdINoYf73P74qdpOO2RzrWHkzwjXBO_hv1UXfllLSpIEgUqv_BMKFa9V5iiz2YYVhTZgaOtAIGASokInRvcX53Kdj5D8wfglfHN8y5knpBzH0F80k12fV0mrPUNFiI0m3EjOSKHN8p8ZnIRCfTnr9FdHkb4mSW12kPoMDLMxO8Yx_VFDcZ7STYmUwz_2JKZiRvukg97Vmt_rqmk_7c-1PmiwoiAxy7KENCxfVKtIyXrqP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
تعطیلی پلتفرم «کاموا» در سایه جنگ و قطعی اینترنت
🔹
پلتفرم فروشگاه‌ساز باسابقه «کاموا» پس از ۸ سال فعالیت، به دلیل بحران‌های سنگین ناشی از دو جنگ و ماه‌ها قطعی کامل اینترنت، از فردا برای همیشه به کار خود پایان می‌دهد.
🔸
هادی فرنود، بنیان‌گذار این مجموعه، ضمن اعلام این خبر تلخ اشاره کرد که اگرچه در سالیان گذشته توانسته بودند از سد چالش‌های اقتصادی و قوانین دست‌وپاگیر عبور کنند، اما تحمل بحران‌های اخیر غیرممکن بوده است. او این تصمیم را فراتر از یک اتفاق تجاری دانست و کاموا را بخش مهمی از زندگی خود توصیف کرد.
🔹
فرنود به مشتریان اطمینان داده است که تمامی هزینه‌های آن‌ها به صورت کامل مسترد خواهد شد. وی در نهایت تاکید کرد که رسیدن به خط پایان به معنای بی‌ارزش بودن این راه نیست و کاموا یکی از مهم‌ترین تجربه‌های زندگی او باقی خواهد ماند.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/iaghapour/2518" target="_blank">📅 23:33 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnRJ8W1XHTDQn8Setx1cTRyv5vPEC8EeSMVTuU6dmCe74IFdAVUmucXdirPfeJleSz_7Z8EctFRIKE4PvdZNWU1W-Ru81cCnGKvIgZ_kcJutv9UgeW3E8xYpmfGM8P-5bGnAaWnG8AdfYOtKHA8-lRt3OY5DRZpiwIIUW3lurOnenF_2UQPNGFhhE-l7KaKFAQThxbj7SN2XUkm5mrjUvFmlmZB7LQ4gnWL3e1fX7Q5SbflAjviPWV3VBeSLQwTUdC3Cv1vE240EdJY3hsKYrPyBem6ZEtrLiKBmnI2rIV9jhC0sqZWSLL8sEjcvUPL5xMUMX_C9BSuLwitDnufePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت بحرانی اینترنت در ایران؛ رتبه ۹۸ در میان ۱۰۰ کشور جهان!
📉
تازه‌ترین گزارش انجمن تجارت الکترونیک تهران از وضعیت اینترنت ایران (زمستان ۱۴۰۴)، تصویر بسیار نگران‌کننده‌ای را نشان می‌دهد. بر اساس این گزارش، اینترنت کشور را می‌توان با سه کلمه «کُند (رتبه ۹۲)»، «پراختلال (رتبه ۹۶)» و «محدود (رتبه ۹۸)» توصیف کرد.
📊
آمارهای کلیدی و نگران‌کننده:
🔹
سرعت پایین: میانگین پهنای باند در ایران تنها ۵.۴ مگابیت‌برثانیه است، در حالی که میانگین آسیا به ۱۳ مگابیت‌برثانیه می‌رسد.
🔹
اختلالات شدید: شاخص تأخیر (Latency) بسیار بالاست و تنها ۳ درصد از وب‌سایت‌های پرکاربرد برای کاربران ایرانی در وضعیت مطلوب و پایدار قرار دارند.
🔹
فیلترینگ گسترده: با مسدود بودن ۳۹ درصد از دامنه‌ها، اینترنت ایران از نظر میزان سانسور پس از چین و میانمار در انتهای جدول قرار دارد.
پ.ن: به نظر میاد این آمار فقط مربوط به سال قبل باشه در صورتی که تو کل سال جدید که 1 ماه ازش میگذره هم اینترنت نداشتیم!
©️
زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/iaghapour/2517" target="_blank">📅 22:45 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPjtr0vDdBLHg51SFvrA87ESNG5SBF5XTcN4x97sKC448esgWpP--3NPdIjpFx1XzvoFavzojjW9BtIdSW69brCjdpawemKQ2z1UPylqWEnQmDrVs7njQ0uRGmbRCMxGk6OGDPw5YdLkBAo5ANYodM1ebBCUAMJGrz_YuceHHJyMbbm5pKKnerGqU1DTNBiWGNJseZPj8zhDYNBCO2wlRxuZ4yuNhg7hIgl6HFMfj9V1Ys0YTyHFOCR07pMJwmJk7eM9JBstmTgG65xogPn3fl9BTMA0XpBQd7JZy4vJ0panYdFdl5TGBZGvy1WcW0jqK8L4iHd8NoXZierZDYq6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
معرفی اپلیکیشن Range Scout؛ اسکنر قدرتمند DNS برای اندروید
🔹
اگر به دنبال یک ابزار حرفه‌ای و در دسترس برای اسکن و تحلیل DNS resolverها هستید، دیگر نیازی به سیستم‌های دسکتاپ ندارید! اپلیکیشن Range Scout یک ابزار کاملاً رایگان و متن‌باز برای اندروید است که این کار را مستقیماً روی گوشی موبایل شما انجام می‌دهد.
🔸
این برنامه با موتور اسکن قدرتمند خود، به شما کمک می‌کند تا بهترین و باکیفیت‌ترین Resolverها را پیدا کرده و آن‌ها را بر اساس عملکردشان بسنجید.
— اسکن منعطف:
پشتیبانی از اسکن دقیق روی IPهای تکی و همچنین رنج‌های کامل IPv4.
— پشتیبانی از پروتکل‌های اصلی:
موتور اسکن DNS با قابلیت پشتیبانی کامل از هر دو پروتکل UDP و TCP.
—
تشخیص پروکسی:
قابلیت بسیار کاربردی تشخیص DNS Proxy به‌صورت شفاف (Transparent) در اسکن‌های UDP.
📥
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/iaghapour/2516" target="_blank">📅 21:53 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6tP2hLbmYbRSMIfBtgMl4J6x11zsJFnR5EKxwtasTVmAWdya1qrvN2ui3DK3s5N_GgZ88F8PlIaEzub6AxdpRotwiPBFGRyBnDujW5DwfvAzX3qmCFA_WAjvMm-BiczHRq9bnrd5qmYWsSCuvt_UlUsa7a4z-3C7x4qMb4fTSuRz9t4v2q87nmc-eEZ_3mSP3f5wwnOxubxejDb2R941wfAXLKQuDLhCnk5q1j0HcLYKNipxRZNfEZPQpAXgo1KPnXkopwuqH1fF9x_y-FunEcku_6LBJ8Q0M5vXyvqOsq4PdabPUcGhBNAyGsOdHJbaY_pT5NTu9W_zqBUohczkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی ابزار MasterDnsWeb
🔸
این ابزار بدرد کسانی میخوره که، روی سرور ایران میخوان نسخه کلاینت MasterDnsVPN رو نصب کنن و از طریق وب مدیریتش کنن.
🔻
ویژگی‌های اصلی:
🔹
قابلیت ساخت چندین Instance به طور همزمان
🔸
قابلیت مدیریت و انجام تغییرات کانفیگ و ریزالور روی وب
🔹
نمایش لاگ های هر systemctl و قابلیت ریست کردن و استارت کردن.
🔗
گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/iaghapour/2515" target="_blank">📅 20:28 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-poll">
<h4>📊 به نظر میاد لیست سفید داره اجرا میشه و فقط به سایت‌هایی که خودشون باز میکنن قراره دسترسی داشته باشیم.هیچ نشونه ای از بازگشت اینترنت نیست!⁉️نظر شما در این‌باره چیه؟</h4>
<ul>
<li>✓ همینطوره و قرار نیست باز بشه.</li>
<li>✓ باز میشه بزودی.</li>
<li>✓ بعد جنگ باز میشه.</li>
<li>✓ نمیدونم :(</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/iaghapour/2513" target="_blank">📅 01:24 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✍🏻
چندتا از کانال‌ها لطف کردن و تو چند روز گذشته کانال ما رو معرفی کردن؛ به همین خاطر افتخار این رو داریم که میزبان چند هزار عضو جدید باشیم. :)
🔻
دوستان عزیز، به کانال خودتون خیلی خوش اومدید!
💚
فقط یک خواهش کوچیک دارم، ممنون می‌شم پستی که
بالاتر
براتون قرار دادم رو حتماً مطالعه کنید.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/iaghapour/2512" target="_blank">📅 00:36 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH_LXT5bQqzEKA7-u446b1noxIzya4CD-VP25Vc5OjvlDNHFEn4S-7WAWTZf1LZOj-5kxS5fMx_th41CwcJ3wy5YunorSbXCCk3_yyFZ_mGSzwCVAJVv-Bct3zCtnlsz11UVlKawPvIQ3yHXq0Uz4OMsuCpqUWcZ7ig7wZkxfe2ELusBUBgKWHmwmMGJVzfDTb-0q_-x_gTxpnm-VYw2o0XY6WtnGWo4BO-55nKNUe_Bh0Zh_Fj_pF4UHMtFjHmxASulWBTu2MhTiJA0-RSDcwDZAQd87QxzpoD1AK3pBiC59QFktwySq7ZkrUPKaPL2oik_M1PthM48afGB8Nr78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گیت‌هاب در بیشتر نت ها و دیتاسنتر ها باز شده
سایت گیت‌هاب (GitHub) به‌تازگی روی اینترنت‌های مختلف و دیتاسنترها باز شده و در دسترس قرار گرفته اما ظاهراً ماجرا به همین سادگی نیست!
🔹
طبق گزارش کانال IRCF:
ترافیک سایت‌های پرکاربرد برنامه‌نویسان مثل Github و Npmjs در حال حاضر به‌جای اینکه از مسیر عادی و بین‌المللی خارج شود، در داخل کشور به رنج‌های داخلی (شبکه زیرساخت) هدایت می‌شود.
⚠️
این یعنی چه؟
این اتفاق به این معنیه که دیتای شما در حال عبور از یک مسیر دستکاری‌شده هستش. این نوع مسیریابی غیرطبیعی (Hijacking/Routing Manipulation) میتونه خطراتی برای امنیت داده‌ها داشته باشه یا نشان‌دهنده‌ی پیاده‌سازی سیستم‌های مانیتورینگ جدید روی ترافیک باشه (یا شایدم من دارم اشتباه میکنم).
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/iaghapour/2511" target="_blank">📅 23:28 · 29 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
لیست لینک های مهم و کاربردی (سری دوم)
این لیست، یک راهنمای جامع و دسته‌بندی شده از تمام آموزش‌ها، ابزارها و مطالب مهم 3 ماه اخیر کانال است.
=================================================
🟢
بخش اول: شروع از اینجا (بسیار مهم برای اعضای جدید)
🔸
لیست لینک‌های مهم و کاربردی
(سری اول)
🔹
پاسخ به پرتکرارترین سوالات شما عزیزان
(حتما مطالعه شود)
🔸
چرا آموزش عمومی، تنها راه بقای اینترنت آزاد است؟ (حتما مطالعه شود)
|
لینک دوم
🔹
مراقب کلاهبرداران باشید!
=================================================
🔵
بخش دوم: مفاهیم پایه و آگاهی‌بخشی
🔸
وقتی اینترنت ملی می‌شود؛ چه راه‌هایی واقعاً باقی می‌ماند؟
🔹
اینترنت ملی چه تبعاتی دارد؟
🔸
چرا الان خودمون فیلترشکن نسازیم؟
🔹
دلیل حمله فیلترشکن فروش‌ها به کانال ما
=================================================
🟡
بخش سوم: ترفندها و آموزش‌های عمومی
🔹
آموزش ساخت کانفیگ محافظت شده با Npv Tunnel
🔸
حل مشکل گیر کردن و لود نشدن سایت‌های ایرانی در زمان اختلال اینترنت
🔹
اشتراک‌گذاری فیلترشکن از طریق هات‌اسپات گوشی
🔸
ابزار رایگان تبدیل فایل JSON به لینک Vless و...
🔹
توقف کامل آپدیت مرورگر فایرفاکس، کروم و ادج
=================================================
🟠
بخش چهارم: آموزش‌های تخصصی عبور از فیلترینگ
🔸
آموزش VayDNS و MasterDnsVPN حتی با ضعیف‌ترین ریزالورها
(پیشنهادی)
🔹
نکته بسیار مهم و اصلاحیه درباره تنظیمات VayDNS
🔻
آموزش ۴ روش اسکن بهترین DNS سالم در موبایل و کامپیوتر
(برای روش های مبتنی بر dns نیازه ببینید) | چندتا از پست های پایین تر همین پست رو مطالعه کنید.
🔸
دو کلاینت اندروید برای MasterDns منتشر شد
🔹
آموزش متنی SNI-Spoofing
|
لینک دوم
🔸
کمی توضیحات درباره روش Spoof Tunnel
🔹
پیاده‌سازی همزمان NoizDNS ،DNSTT و Slipstream در یک سرور
=================================================
🔴
بخش پنجم: آموزش‌های کاربردی و مفید
🔸
قبل از تانل زدن ببینید: آموزش تست ارتباط بین سرور ایران و خارج
🔹
آموزش نصب آفلاین هر اسکریپتی روی سرور ایران + نصب X-UI
🔸
آموزش گرفتن سرتیفیکت برای دامنه پوینت شده به سرور ایران
🔹
آموزش ساخت ربات تلگرامی برای SSH زدن به سرور
=================================================
🟣
بخش ششم: ابزارهای کاربردی | اطلاعات مفید
🔸
اسکریپت کبوتر برای دریافت خبر از تلگرام با DNS
🔹
پیام‌رسان شخصی و رایگان موروِب
(قابل اجرا روی هاست)
🔸
نصب آفلاین مسنجر songbird
🔹
راهنمایی درباره کامنت‌های یوتیوب و ربات تماس با ما
🔸
درباره تبلیغات تلگرام و کانال
🔻
ممنون از حمایت و دلگرمی شما
❤️
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/iaghapour/2510" target="_blank">📅 20:20 · 29 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">💢
هشدار اتاق اصناف درباره ابعاد فاجعه‌بار محدودیت‌های اینترنتی
سخنگوی اتاق اصناف ایران با اشاره به سهم ۵ درصدی اقتصاد دیجیتال در تولید ناخالص داخلی، ابعاد خسارات ناشی از قطع اینترنت را بسیار فراتر از پیش‌بینی‌ها دانست.
وی تأکید کرد که رویکرد «دسترسی گزینشی» یا اینترنت طبقاتی برای واحدهای صنفی کارآمد نخواهد بود؛ چرا که در صورت عدم دسترسی مشتریان به شبکه، عملاً بازاری برای فروش باقی نمی‌ماند.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/iaghapour/2509" target="_blank">📅 18:39 · 29 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💢
در حالی که دنیا با سرعت نور به سمت پیشرفت‌های نفس‌گیر مثل هوش مصنوعی پیشرفته، مأموریت آرتمیس ۲ برای بازگشت انسان به ماه، و هزاران نوآوری دیگه پیش می‌ره، ما اینجا اسیر یه چرخه‌ی تکراری و خفه‌کننده‌ایم: هر روز باید اخبار رو چک کنیم و ببینیم که بالاخره کی قراره این چکمه‌ی سنگین سانسور رو از گلوی اینترنت‌مون بردارن.
این وضعیت نه تنها فرصت‌های برابر رو ازمون می‌گیره، بلکه ما رو از جریان اصلی جهان عقب نگه می‌داره – انگار که به جای پیشرفت در یک مسیر، داریم تو باتلاق محدودیت‌ها دست و پا می‌زنیم.
امروز وارد پنجاهمین روز
#قطعی_اینترنت
شدیم.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/iaghapour/2508" target="_blank">📅 12:07 · 29 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✍🏻
یه سری از دوستان گله کردن که چرا من فقط به کشته شدن بچه‌های دی‌ماه اشاره کردم و حرفی از بچه‌های مدرسه میناب نزدم.
تو فضاهای دیگه چندین بار راجع به این اتفاق تلخ حرف زدم و ابراز همدردی کردم. ولی با این حال، مگه میشه آدم به این فاجعه فکر کنه و دلش خون نشه؟ از دست رفتن بچه‌های معصوم میناب واقعاً قلب هر آدمی رو به درد میاره.
این غم خیلی بزرگه... به خانواده‌های داغدارشون تسلیت میگم.
🖤</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/iaghapour/2506" target="_blank">📅 21:12 · 28 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💢
فضل‌الله رنجبر (عضو کمیسیون اجتماعی مجلس):
«دسترسی به اینترنت فعلاً به مصلحت نیست و این ما هستیم که زمان وصل شدن آن را تشخیص می‌دهیم.»
✍🏻
پ.ن: آدم می‌مونه چی بگه! بیشتر از چند ماهه که با این وضعیت، کلی کسب‌وکار رو به مرز نابودی کشوندن. حالا به جای اینکه بابت این خسارت‌ها شرمنده باشن، خیلی راحت میگن «فعلاً مصلحت نیست مردم اینترنت داشته باشن!»
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/iaghapour/2505" target="_blank">📅 21:01 · 28 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">می‌گویند وقتی سنگی در تاریکی پرتاب می‌کنی، صدای کسی درمی‌آید که سنگ به او خورده است. این روزها شاهد دست‌وپا زدن‌های حقیرانه عده‌ای هستیم؛ همان‌هایی که اینترنت آزاد را که حق مسلم هر انسانی است، به چشم یک تجارت پر سود می‌بینند و خون مردم را در شیشه کرده‌اند.
✍🏻
هدف من در این کانال از روز اول فقط یک چیز بوده و هست:
کمک به دسترسی آزاد شما به اینترنت.
درد شما این است که من و امثال من، با آموزش‌های کاملاً رایگان، دکان شما را تخته کرده‌ایم. درد شما این است که ما به مردم یاد می‌دهیم چطور بدون پرداخت هزینه‌های گزاف و «گیگی فلان قدر تومن» که به جیب شما می‌رود، به اینترنت آزاد دسترسی داشته باشند.
من هیچ‌گاه نیازی نمی‌بینم وارد حاشیه شوم یا پاسخ کینه‌توزی‌ها را بدهم. تمرکز من فقط روی ارائه بهترین روش‌ها برای شماست و بهترین پاسخ به بدخواهان، همین استقبال و حمایت شماست.
دلیل وقفه کوتاهی که در انتشار آموزش‌ها افتاد، دقیقاً مدیریت همین حواشی بود. وقتی منافع عده‌ای در خطر است، با تمام توان سنگ‌اندازی می‌کنند. در مقابل این هجمه‌ها، سکوتِ کسانی که از این مسیر استفاده می‌کنند، کمکی به ما نمی‌کند. این مسیر دوطرفه است و ادامه آن به حمایت و صدای شما بستگی دارد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/iaghapour/2504" target="_blank">📅 15:00 · 28 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGJEUZ3QEGZbTVX7syUy9dSbw7E1vd8n4U2zk1Mha7ZSBi_TzYP2Aj7kjRgwC19HwoOarOucb0ZIfQ0VYQwHXXCPJ1srmYfuDUs2P9A6sTdzvkMPCkR8GtXl7OWvnf8EBKttgN6a7ILMpcz3tQsZjoyQXDu2VJY9b2I8qKuQbgeImxIm4oeYv4uMmAy8c406F-KnY_mXcAJhPw4KndhsAOKL5MxSdA6hD1K8VGChHlwVbsrxrHnqayWWGexlh6aRHis23vaX-6hOuRCwvRrpJwz-sL9x53ladadZqeAsCq0ng7tf1cZgi-omvRjotlBAWpN8oEeZJbTPD7Ia9bAnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
فکر کن تیتر خبر تو یه کشوری باز شدن گوگل باشه...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/iaghapour/2503" target="_blank">📅 12:21 · 28 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3AQ4WSf1NzpjXVD5PGBLfs0C3iQWpHyGPenUeTeu1qb0f9o0AAz2P7IjD_49-e2TYuKYdZ6-r2YEJHyAfA4dPaUevgC5WjgkpVBg5_gsF2IGfONx3y_ZgmjFMY9EgrNSTds7aWAOQb3qfupiw6KUWmBhcr1f7ZRrR5Le8Ha11W64JGE6HGxWeMod_lbQN2MGIXyKQCUXZgdPSDF5SGu6iCQR8gcKjOxAH6_nzx3XgPScD2H3MOAO7lGreXVMG1E33fCJNj-HpMNlIKbqsHDOZJ9Mcde6TmQ3q-spofS2wU2Hka_EgOWB7fDOIcvBH0D94syy7T3r6nqo34VyD_RPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرفت کردیم و بعد 49 روز و 1152 ساعت سطح اتصال به 2 درصد رسیده.
😡</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/iaghapour/2502" target="_blank">📅 11:04 · 28 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">من کسانی رو که میشناختم به خاطر بی احترامی به کسانی که نمیشناختم از زندگیم حذف کردم.
#دی
🖤</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/iaghapour/2501" target="_blank">📅 23:03 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7uZ36TV_MzU6Y26NkGvjZrifAE0bKcc32fAKKYf9Jes9FLcvWFhf5402RX33eK8TiRJlemqS575ylNWEMF8IONFiphnXrMCNg7Uy0YZuzXcRbpfuUWCTbZPbpd-xyHk5pnTyogG_Llb_iaqww9dynWffXkeFuGc_BlM0cfmIlEsMMV1FFAb1J1HQG6zaco0-xzxqQxqqtV7DSMPjbUIz0TbLhB5i4aQV1JOoOGFnwek4gyYRFyALZOHMMmzBetjOA0FEFJ1SCkcNxyAiDjGP9Q9yxFNRaKMhA7Hdnb90_DiO2YeSwxwNg1e2D-6OVas1q-sSiYSqyqYZi9-q_Ubng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
موج فیلترینگ آی‌پی های ایرانی
🔸
یکی از بچه‌ها این عکس رو فرستاده و میگه تو یک دیتاسنتر معروف برای یه سرور ایران، تا الان ۳۷ بار آی‌پی عوض کرده ولی دریغ از حتی یه دونه آی‌پی سالم!
🔹
به طرز عجیبی آی‌پی سرورهای ایران هم دارن فیلتر میشن و بدتر اینکه این داستان فقط مال یه دیتاسنتر نیست و ظاهرا بقیه هم درگیرشن.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/iaghapour/2500" target="_blank">📅 19:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ببخشید این خبرهای ساده رو پوشش میدم ولی میگم شاید برای یکی مهم باشه.
💢
جیمیل در دسترس کاربران قرار گرفت.
‌
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/iaghapour/2499" target="_blank">📅 18:51 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭕️
به نظر میاد هوش مصنوعی
#Deepseek
هم باز شده. رو اینترنت های خانگی و همراه تست شده. البته روی دیتاسنتر ها هم به نظر باز شده.
✍🏻
توی تست خودم اختلال زیاد داشت.
🔹
به نظر میاد همون وایت لیست هستش و نشونه ای از باز شدن اینترنت وجود نداره!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/iaghapour/2498" target="_blank">📅 18:01 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💢
گوگل رفع محدودیت شد
🔹
در ساعت‌های اخیر دسترسی به موتور جستجوی گوگل مجدداً برقرار شد.
پ.ن: آدم روش نمیشه این اخبار رو منتشر کنه.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/iaghapour/2497" target="_blank">📅 16:24 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913ef6b1f4.mp4?token=En_xhfXoCz9BWlsM4yCLdZjPQlePToztkFhxbXmib7Lj9P9M_oqHZ0Yy4fjcHb6QbwxnGUSIKhnugCggxGX7V00HYKXxTi7fWd_jsfXfFTFkxPWw8kI6msVvKO0hvB_oKTZQrIIyCN2fSvADl6xf_wc8CTT65MBYrSJmF4qGv_hRCxDO03SfHGybJfBhT7G4ZWtrPtZpeJx8twSvMuE3Usj03tmELXqBVJ2BF1jf8Jpa-l-n1Aa36IxhsomxerUNeGUur51A9ApGKKqWsisyJkSIulD6U7sZIdiEtvQYvkj86NBBG3GUdLgUe3y1-eyJAjaQYrI2QOC6-APIm4TQjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913ef6b1f4.mp4?token=En_xhfXoCz9BWlsM4yCLdZjPQlePToztkFhxbXmib7Lj9P9M_oqHZ0Yy4fjcHb6QbwxnGUSIKhnugCggxGX7V00HYKXxTi7fWd_jsfXfFTFkxPWw8kI6msVvKO0hvB_oKTZQrIIyCN2fSvADl6xf_wc8CTT65MBYrSJmF4qGv_hRCxDO03SfHGybJfBhT7G4ZWtrPtZpeJx8twSvMuE3Usj03tmELXqBVJ2BF1jf8Jpa-l-n1Aa36IxhsomxerUNeGUur51A9ApGKKqWsisyJkSIulD6U7sZIdiEtvQYvkj86NBBG3GUdLgUe3y1-eyJAjaQYrI2QOC6-APIm4TQjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه متنی توی توییتر دیدم واقعا قشنگ بود و حال و روز خیلی ها رو نشون میده. میدونم شما هم با این افراد برخورد کردین تو این روزها. یعنی افرادی که در مقابل فهمیدن مقاومت میکنن چون سودشون تو نفهمیدن هستش.
👇🏻
ظاهراً حماقت مسری شده و جمعیت احمق ها هر روز در حال افزایشه. یه عده هم کارشون شده گوسفندوار سوار هر موج مبتذلی بشن و تهش هم بشن یه احمقِ کپی‌پیست شده مثل بقیه. گور بابای حرف این جماعت؛ کرکره‌ی گوشِت رو بکش پایین و فقط مسیر خودت رو برو.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/iaghapour/2496" target="_blank">📅 13:59 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭕️
خلاصه‌ی داستان SNI Spoofing (جعل SNI)
🔸
این روش چیست ؟
به این تکنیک SNI Spoofing (جعل SNI) یا Fake SNI می‌گویند که یکی از قدیمی‌ترین و کلاسیک‌ترین روش‌های دور زدن فیلترینگ است.
کار این روش این است که در اولین مرحله‌ی ارتباط (دست‌دهی اولیه یا همون Handshake)، یک نامِ دروغینِ مجاز (مثل
auth.vercel.com
) را به فایروال نشان می‌دهد تا فایروال گول بخورد و دروازه را باز کند.
🔹
چرا در ابتدا کار کرد؟
چون فایروال ملی در نگاه اول فقط به همین نامِ دامنه (پوسته) نگاه می‌کند. از آنجا که دامنه‌هایی مثل Vercel یا Ubuntu برای توسعه‌دهندگان حیاتی هستند و در لیست سفید  قرار دارند، فایروال به آن‌ها اعتماد کرده و اجازه عبور ترافیک را می‌دهد.
🔸
چرا بعد از مدت کوتاهی از کار افتاد؟
هوش مصنوعی و سیستم‌های فیلترینگ پیشرفته (DPI) امروزی، فقط به نامِ دامنه بسنده نمی‌کنند. آن‌ها در لایه‌های بعدی یقه این روش را می‌گیرند. دلایل اصلی بسته شدن سریع آن عبارتند از:
—
تحلیل رفتار غیرطبیعی:
فایروال متوجه می‌شود که حجم و الگوی مصرفِ کاربری که در حال استفاده از این روش است، شبیه مرور یک سایت عادی نیست، بلکه شبیه یک تونلِ دانلود/آپلود سنگین است. بنابراین آن را قطع می‌کند.
— لو رفتن آی‌پی:
این ابزار معمولاً ترافیک را به سمت آی‌پی‌های معروفی مثل
188.114.98.0
می‌فرستد که فایروال ملی مدت‌هاست روی آن‌ها حساس است. وقتی ببیند هزاران درخواستِ عجیب با نامِ ورسل به سمت این آی‌پی می‌رود، آن را مسدود می‌کند.
—
مسدودسازی توسط خود کلادفلر:
خود شبکه‌ی کلادفلر (مقصد) نیز استفاده از SNI جعلی برای دسترسی به دیتای غیرمرتبط را مسدود می‌کند.
🔻
نتیجه‌گیری نهایی:
استفاده از این ابزار (جعل SNI روی بستر TCP) مانند پنهان شدن پشت یک شیشه‌ی شفاف است؛ در لحظه‌ی اول شاید کار کند، اما با کمی دقت کاملاً لو می‌رود.
پ.ن: شاید هم مواردی وجود داشته باشه که از درک من خارج باشه.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/iaghapour/2494" target="_blank">📅 20:36 · 26 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
حل مشکل گیر کردن و لود نشدن سایت‌های ایرانی در زمان اختلال اینترنت
🔻
تو زمان نت ملی وقتی وارد یک سایت ایرانی میشید میبینید سایت خیلی طول میکشه لود بشه یا ناقص لود میشه. اگر به گوشه پایین مرورگر دقت کنید، معمولاً می‌بینید مرورگر روی عباراتی مثل Waiting for
www.googletagmanager.com
یا
fonts.googleapis.com
گیر کرده! دلیلش هم اینه که سایت های ایرانی یک سری فایل ها رو از منابع خارجی لود میکردن و الان دچار مشکل شدن!
💡
راه‌حل چیست؟
با مسدود کردن هوشمندِ این سرویس‌های اضافه‌، مرورگر دیگر منتظر آن‌ها نمی‌ماند و سایت را بلافاصله برایتان باز می‌کند.
۱. افزونه uBlock Origin را روی مرورگر خود (کروم، فایرفاکس یا اج) نصب کنید.
۲. روی آیکون افزونه (سپر قرمز رنگ) کلیک کرده و آیکون چرخ‌دنده
⚙️
را بزنید تا تنظیمات باز شود.
۳. از تب‌های بالا به بخش My filters بروید.
۴. کدهای زیر را کپی کرده و در آنجا Paste کنید:
||fonts.googleapis.com^
||fonts.gstatic.com^
||googletagmanager.com^
||www.googletagmanager.com^
||google-analytics.com^
||www.google-analytics.com^
||hotjar.com^
||clarity.ms^
||mc.yandex.ru^
||connect.facebook.net^
||googlesyndication.com^
||doubleclick.net^
۵. در نهایت روی دکمه Apply changes کلیک کنید. تمام!
✅
⚠️
نکته: لیست بالا کاملاً بی‌خطر است. فقط دقت کنید که هرگز دامنه اصلی گوگل (
google.com
) یا ریکپچا (recaptcha) را مسدود نکنید.
🔗
صفحه افزونه برای کروم / ادج
🔗
صفحه افزونه برای فایرفاکس
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/iaghapour/2492" target="_blank">📅 19:46 · 26 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📉
بر اساس اظهارات افشین کلاهی، رئیس کمیسیون کسب‌وکارهای دانش‌بنیان اتاق بازرگانی ایران، خسارت مستقیم ناشی از
#قطع_اینترنت
در
#ایران
روزانه بین ۳۰ تا ۴۰ میلیون دلار برآورد می‌شود. اگر تبعات غیرمستقیم هم در نظر گرفته شود، این عدد به حدود ۸۰ میلیون دلار در روز می‌رسد؛ رقمی معادل نابودی روزانه چندین پروژه زیرساختی بزرگ.
©
پس‌کوچه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/iaghapour/2491" target="_blank">📅 18:10 · 26 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✍🏻
شاید دلم نمی‌خواد قضاوت کنم، یا شایدم می‌خوام... واقعاً نمی‌دونم! :( اما بعضی حرف‌ها رو دیگه باید زد.
🔹
روی صحبتم اول از همه با کسانیه که «سیم‌کارت سفید» تو جیبشونه یا به هر شکلی، رانتِ داشتنِ اینترنتِ آزاد و بدون محدودیت رو دارن. شمایی که وقتی مردم عادی برای باز کردن یه عکس یا فرستادن یه پیام صوتی دارن با ده تا پروکسی و فیلترشکن می‌جنگن، خیلی راحت و بدون دغدغه وصل می‌شید.
🔹
بیایید با خودمون رو راست باشیم؛ شما هیچ فرقی با سیاست‌گذارهای فیلترینگ ندارید! وقتی شما دردِ قطع شدن و محدودیت رو حس نمی‌کنید، یعنی دقیقا دارید از همین ساختارِ فیلترینگ حمایت می‌کنید. سکوتِ شما و استفاده از این رانت، تاییدِ وضع موجوده.
🔸
اما روی دومِ صحبتم با اون کسب‌وکارها، برندها و مجله‌های ایرانیه (که نیازی نیست اسمشون رو بیارم، خودشون می‌دونن). شمایی که بدون اینکه واقعاً مجبور باشید و کارد به استخونتون رسیده باشه، خیلی راحت کانال‌ها و پیج‌هاتون رو از تلگرام و اینستاگرام جمع کردید و بردید تو پیام‌رسان‌های داخلی.
🔸
شما با این کارتون عملاً به فیلترینگ مشروعیت دادید. شما به اون کسی که دکمه فیلتر رو فشار داده این پیام رو دادید که: "دمتون گرم، ما که مشکلی نداریم، با شرایط جدید هم کنار اومدیم!" شما با عادی‌سازیِ این شرایط، دقیقاً از محدودیت‌های بیشتر حمایت کردید.
🔻
پس لطفاً... حداقل با ما صادق باشید. برای ما ژستِ آدم‌های نگران، دلسوز و دغدغه‌مند رو نگیرید. کسی که تو روزهای سخت، به جای ایستادن کنار مردم، فقط به فکر بیرون کشیدنِ گلیمِ خودش از آب بوده و با محدودیت‌ها همراهی کرده، حق نداره ادعای همراهی و پیگیریِ حقِ مردم رو داشته باشه.
#فیلترینگ
#اینترنت_آزاد
#عادی_سازی
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/iaghapour/2490" target="_blank">📅 16:11 · 26 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">💢
مشکل ارسال کد تلگرام با پیامک درست شد
بر اساس گزارش‌های دریافتی از کاربران، اختلالی در ورود به پیام‌رسان تلگرام از طریق پیامک وجود داشت که در حال حاضر رفع شده.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/iaghapour/2489" target="_blank">📅 22:28 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🟢
روش SNI Spoofing همچنان فعاله.
دلیل اینکه آموزش رو کمی دیرتر گذاشتیم این بود که می‌خواستیم اول خودمون دقیق تستش کنیم. البته قبل از ما، بقیه دوستان آموزش‌های متنی و ویدیویی کاملی ساخته بودن که واقعا جای تشکر داره. حجم پیام‌ها اونقدر بالا بود که پشتیبانی فرصت نکرد زودتر این اسکریپت رو بررسی کنه. جالب اینجاست که بیشتر از ۱۰۰ نفر این اسکریپت رو برای ما فرستاده بودن تا آموزشش رو بذاریم :)
🔻
پشتیبانی ربات گفت که چند تا سوال پرتکرار داشتید، که اینجا بهشون جواب می‌دم:
۱- آیا این روش خطرناکه؟
— همون‌طور که قبلا هم یه توضیح کوتاه دادیم، این روش با IP Spoofing فرق داره. پس مشکلی نداره و با خیال راحت می‌تونید ازش استفاده کنید. یک نگرانی درباره فایل EXE وجود داشت که دوستان گفتن بررسی شد و مشکلی نبود.
۲- امکان استفاده از کانفیگ‌های رایگان و یا کانفیگ‌های BPB وجود دارد؟
— من خودم کانفیگ‌های BPB رو برای این کار تست نکردم، اما بچه‌ها تو ربات پیام دادن و گفتن که بدون مشکل کار می‌کنه. (یه نگاه به عکس راهنمای کانفیگ که بالاتر فرستادم بندازید).
۳- دلیل از کار افتادن ناگهانی این روش برای برخی کاربران چیست؟
— با افزایش استفاده از هر روشی و فراگیر شدن الگوی مصرف آن، احتمال مسدود شدن وجود دارد. با این حال، روش فعلی همچنان فعال است. در صورت بروز قطعی، به فایل config.json مراجعه کرده و آی‌پی‌ها و دامنه‌های تمیز (سفید) دیگری را جایگزین و آزمایش کنید.
۴- آیا احتمال مسدود شدن کامل این روش وجود دارد؟
— صد درصد این امکان وجود داره. یادتونه یه مدت (دوران اعتراضات) دامنه ChatGPT باز شده بود و همه روش کانفیگ می‌زدن، اما بعدش مسدود شد؟ همون‌طور که گفتم، وقتی یهو همه برن سمت یه روش و الگوی مصرفش مشخص بشه، سیستم فیلترینگ متوجه می‌شه و جلوش رو می‌گیره. پس به حرف افراد با دانش کم و یا بیسواد توجه نکنید و هر روشی که الان کار می‌کنه رو با دوستان‌تون به اشتراک بذارید تا تو همین مدت محدود بتونن استفاده کنن و کارشون راه بیفته.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/iaghapour/2486" target="_blank">📅 12:26 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fddUpm9nOT_m9vtfnZDTCJf4p3uQu7Kvc_90-_RFTqpmG7YPvkTd8_5Qm3TimPXYKNXVGQto7IfuWHPS6C43-0einu8daUAXh1BuEskHrVra-THfkK1V_uxhkKcvyFmkhIbhyJlUvaRqm-CmMvBdz2I7DoMEBssK1bhx-i7eGTuRL3X9uvmXKEh2pDZ4Jq-knHX3OfQNdhxUClvd2knexmcYEV2TQeAlQfCiKnxQ66RH6ftft3ZS1XdpynleMST6R7JCbs2sdjKq-LP4mQ7059SdVb3Ve5HLGIKcKPw-TOavD9O0rxgv4ouufEcKAz7jdNhE8xlP0vY0xHstpbFyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای کانفیگ برای روش SNI Spoofing
🔹
بعضی از دوستان دچار مشکل شدن و میگن کانفیگ از کجا بگیریم. هم کانفیگ های رایگان در سطح وب که وجود دارن میتونین استفاده کنین هم خودتون یکی با دامنه بسازین و بندازین پشت کلودفلر.
— فقط کانفیگ باید پشت کلودفلر باشه.
⚠️
نمونه کانفیگ ویرایش شده رو به شکل عکس براتون ارسال کردم.
🔻
لیست یکسری سایت هایی که سفید هستن هم براتون میفرستم حالا نمیدونم همشون پشت کلودفلر هستن یا نه! میتونید این سایت ها رو در فایل config.json تست کنید.
vercel.com
sourceforge.net
ubuntu.com
letsencrypt.org
react.dev
nexjs.org
python.org
pipy.org
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/iaghapour/2484" target="_blank">📅 03:33 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭕️
آموزش متنی SNI-Spoofing برای استفاده از آیپی سفیدهای کلودفلر
میخاستم تا فردا صبر کنم که یهو 100 تا پیام اومد :)
🔸
یکی از دوستان زحمت کشیده و از دامنه هایی که آزاد شدن استفاده کرده برای اینکار. به فایل config.json توجه کنید که هم حاوی آیپی سفید هست هم دامنه.
نحوه کار این ابزار به این صورت است که با جعل آدرسِ سایت‌هایی که در حال حاضر در لیست سفید (Whitelist) قرار دارند، سیستم فیلترینگ را دور زده و اتصال شما را به اینترنت آزاد برقرار می‌کند.
با استفاده از این برنامه، می‌توانید تمام کانفیگ‌های مبتنی بر کلودفلر را که از کار افتاده‌اند رو دوباره زنده کنید!
🔻
مراحل اجرا و تنظیمات:
اجرای برنامه واسط:
پس از دانلود فایل، روی برنامه SNI-Spoofing کلیک راست کرده و حتماً گزینه Run as administrator را انتخاب کنید تا با دسترسی ادمین اجرا شود.
تنظیم کلاینت:
وارد برنامه کلاینت خود (مثل ،v2rayN یا هر برنامه مشابهی که استفاده می‌کنید) شوید و کانفیگ مورد نظرتان را برای ویرایش باز کنید.
تغییر آدرس و پورت:
در تنظیمات کانفیگ، بخش آدرس (Address) را به آی‌پی لوکال
127.0.0.1
تغییر دهید و پورت (Port) را روی 40443 تنظیم کنید. کانفیگ را ذخیره کنید.
کار تمامه و میتونید به کانفیگ خودتون متصل بشید.
🔗
آدرس گیت‌هاب پروژه برای دانلود فایل
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/iaghapour/2481" target="_blank">📅 01:44 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕️
همونطور که بالاتر هم اطلاع داده شد یک سری سایت ها از دیروز باز شدن که بیشتر به درد برنامه نویس ها میخوره.
🔹
البته برای من رو ایرانسل سایت sourceforge باز نشد :)
https://vercel.com
https://nextjs.org
https://sourceforge.net
https://letsencrypt.org
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/iaghapour/2475" target="_blank">📅 16:37 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭕️
دیجیاتو
روزشمار قطعی اینترنت گذاشته بود صفحه اول سایتش که فقط نشون میداد الان چند روزه مردم به اینترنت آزاد دسترسی ندارن!
⚠️
امروز به دستور نهاد امنیتی از روی سایت حذف شد!
روز شماری که فقط تعداد روزها و ساعت قطعی رو نشون میداد.
هیچی دیگه همین...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/iaghapour/2474" target="_blank">📅 16:31 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzZkNHyh_vDAfMPsa9Cnb-1uEVVRRjnQapFIjU2tmkvjl7jY1WxvUo51gpLXXkSMZboqtxT04kxviupN8e_2Lc23yYRY2YsrfNxQzgksHx8NO91QG15H8jwEUA6v5-uE42Q0Ni3gEnjof0vfd8KSOliVTtCjSt46tOi-RvOOnNFYM3N7ewtkkJE6MvNJo3Gz-SWxVW211YMsWiEpzWCsc0L4VX2mLUShfk8AWv4X_NJmN670GEu7MydOv7AMqW9Dm0LM5v9ST2ElH0BUDcf3XbOoz4lK8e9fhNmSXzlHKI4QFwKHRbi_H99I1NE5v8ep06ocQ0mNQpxwgqu7NEfvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این خیلی مسخره‌ست که منظورمون از وصل شدنِ اینترنت شرایطیه که توش فیلترشکن های ارزون بتونن وصل شن.
یه سطحی از بدبختی به عنوان شرایطِ خوب بهمون قالب شده و خودمون یادمون نمیاد کی اینو پذیرفتیم.
©
Kian
🔹
پ. ن:
البته نپذیرفتیم بلکه تحمیل شده به ما...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/iaghapour/2471" target="_blank">📅 13:25 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚠️
سخنگوی دولت اخبار این روزها مبنی بر باز شدن اینترنت را تکذیب کرد؛ به محض دریافت خبر رسمی اعلام خواهیم کرد
سخنگوی دولت:
💢
باز شدن اینترنت موضوعی نیست که دست ما باشد.
💢
به محض اینکه خبر رسمی از مبادی رسمی دریافت کنیم، حتما اعلام خواهیم کرد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/iaghapour/2470" target="_blank">📅 11:17 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPN8NHcinnhpnJuDHwU0bniT1jpnc1H4iGRwBmvnTlTySop93np3VPzb4E_y-d3tnWB-GCxHgOh9QXTUYKXEVx5k7KuEu35B0LFsUca5-jGf6HC2ddg5v0PSPAb3Q3d_-36tGSmaShlH2NhILAldxXPeLQQnsUBpnMwbUkdWALwY_kiYMRHVdv3kYOaNy1k9LFv35PlwnQTLiUNjpqP44OCBS63TCbrZAr-um5osB-WiImwnsiJ2zw0LlJ66hg1xAA8Yn_2LFXVV-dhmuvk0PtxbaPxcDNRzDQVF3Tg915c-V-xbTAbFZCmPQtbL7Dl2FQmEqEOw-mXdyaY5ll7xwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
صفحه
#نت‌بلاکس
در X یه نظرسنجی گذاشته و از مردم پرسیده؛ «آیا شبکه‌های اجتماعی مثل توییتر و تلگرام و اینستاگرام و ... باید حساب‌های دولت‌ها و مقاماتی را که اینترنت را برای مردم خود قطع یا سانسور می‌کنند، تعلیق کنند؟»
🔻
که بیش از ۹۶ درصد گفتن آره باید صفحاتشون مسدود بشن!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/iaghapour/2469" target="_blank">📅 20:42 · 23 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⭕️
خودم نمیتونم تایید کنم ولی عده ای میگن
#سایفون
رو همراه اول متصل هست.
سایفون در حالت فیلترینگ عادی جواب نمیده حالا آدم شده برای ما
😁
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/iaghapour/2468" target="_blank">📅 20:36 · 23 Farvardin 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
