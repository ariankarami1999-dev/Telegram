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
<img src="https://cdn4.telesco.pe/file/JxUApXNeeRg8RmR05A0xdd413RzMzWIvjQUqjwUk6RHHxqMQ5vop5KmTCR4bKbJwkKeJfMoqE0k9w5J42OtVV9UiNe5FaHN0J3_Wlmkm3YhMffyyD0p-6mRyjnWBygf9S_Rfhx26QsbSQbhI7q8AjxA2JG_xTJOhvygzd08k5nMbxJ9gm3Vf8wTEXGlo8wtnl68_f07G0Ona7ND5x5DX8j2RWxCcj4ubY-FVRv7SIge40kEPd5I0sza8d1b9k6mb1Ze_wmmV5jm8sJG1KXWckGUsGzyiye91cY7z6mCtWgooZ-HR9DtzkDE5X-85aJQlqFwGDfkNc6-xl5uuMd8I4w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 466K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی: تهران ادعای پاسخ نظامی به محدودیت‌های هوایی اخیر را رد کرد و از مذاکرات جدی با کشورهای ذی‌نفع برای رفع محدودیت‌ها خبر داد؛ در عین حال، هشدار داد در صورت لزوم، گزینه‌های متقابل غیرنظامی علیه برخی فرودگاه‌ها را اجرا خواهد کرد، هرچند امیدوار است موضوع به این مرحله نرسد.
@WarRoom</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/withyashar/24246" target="_blank">📅 16:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV04QAXATGNU7pQqA4M2J3wNCYuLpxMZbkkL6ENQrGb_Kc7IERBlC8umA8sRUqhSH-LwirMhyMcalN6IsH5jHGtXzgrb964gCpOYFqgD2O_LuYNBhMbYhwnTNjbKO3DVrX5WLLp7wAHBUqJdr9FkSnnamIafQDmWZBUKYuWIo0rozhDq28P9KW2bM0Wr1zJnMMSKCcmzzOx5TtL9SjYDkPlg8XLhjgxue_OzrgLuLzddGYh3zNwVAKi6G6csaOS-BVy3mmtQCJ457tzdMSU3kvN5WBKjEFQsJIZW5vG1ulV3MyxuxQB7LofufWKmuBiFuWO4XKCpIXCU3WH-aiSCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گارد ملی آمریکا اعلام کرده که در ۲۲ و ۲۳ سپتامبر، هواپیماهای C-130H3 هرکولس از گردان ۱۶۶ ترابری هوایی دلاور برای پشتیبانی از عملیات سنتکام در خاورمیانه اعزام شده‌اند و حدود ۱۰۰ نفر از نیروها نیز همراه آنها مستقر شده‌اند. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/24245" target="_blank">📅 16:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراق: خروج ائتلاف بین‌المللی (مبارزه با داعش) به رهبری آمریکا از این کشور در آستانه تکمیل است.
رئیس سلول رسانه‌ای امنیتی عراق اعلام کرد ائتلاف تمام پایگاه‌ها و مقرهای خود در مناطق فدرال عراق
(از جمله پایگاه عین‌الاسد)
را تخلیه و به مقامات عراقی تحویل داده و خروج نیروهای باقی‌مانده از
اقلیم کردستان و پایگاه اربیل
نیز در حال انجام است. مهلت نهایی پایان مأموریت ائتلاف در عراق
برابر با ۸ مهر ۱۴۰۵
تعیین شده است. این به معنای قطع همکاری آمریکا و عراق نیست و پس از آن، روابط امنیتی دو کشور در قالب
همکاری دوجانبه
ادامه خواهد داشت.
@WarRolm</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/withyashar/24244" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تایمز آو اسرائیل:
ائتلاف سعودی اعلام کرد دو پهپاد حوثی‌ها را که به سمت ریاض شلیک شده بودند رهگیری کرده است؛ این حمله در پی افزایش حملات حوثی‌ها و همزمان با مذاکرات امنیتی عربستان، ترکیه و پاکستان رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/24243" target="_blank">📅 15:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUbwPBqlmvff5H1udGSyUb_LOXZs7hHPcbov3r0nKulOcAlMxw2qrmwczKmhr4l8yDBtxXLFwn98djwI001QxAiZWeu666KZlE89ifw5l0KQZlF94fXKfKsTAZEnldUDq3xs2ZadVd5jRbB5oGfCfTptkLXvAs2oxuECetUudTtaKW5jE1yg2LGwAHioirW8SxzCSBjStzmaXe9irQk9-SFLo93jiTwNjb0bKCBPPEuRdiR2UkG5q8_d5fNe-GNFrOQzDy5UeXUOgQ8wUHbzLJDOQGu8G0cBtaLL2H6304hPPRPndGloUUhnFWFjlmcMWE530vHFCiLLhOkFyYUJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس:
دونالد ترامپ در
واکنش
ی
تمسخرآمیز
به رژیم ایران تصویری از نقشه تنگه هرمز در شبکه اجتماعی خود منتشر کرده که روی آن نام
«تنگه ترامپ»
درج شده است؛ این اقدام پس از پیشنهاد ایران برای بازگشایی تنگه ظرف هفت روز انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/24242" target="_blank">📅 15:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نیروی هوایی عربستان سعودی در حملاتی در شهرستان حیفان، جنوب استان تعز، پروژه تصفیه آب منطقه الأکبوش و شبکه ارتباطات این منطقه را هدف قرار داد.
این حملات در منطقه
الأکبوش ـ الأحکوم
انجام شده؛ منطقه‌ای که طی روزهای اخیر شاهد درگیری‌های شدید میان نیروهای یمنی و حوثی‌ها بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/24241" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24240">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پزشکیان در مصاحبه با سی‌بی‌اس: ما چند زندانی آمریکایی را آزاد کردیم، اما آمریکا به تعهد خود عمل نکرد.
پزشکیان گفت: «ما کاری را که آمریکا از ما خواسته بود انجام دادیم و چند نفر از زندانیانی را که درخواست کرده بودند آزاد کردیم. قرار بود پول‌های ما آزاد شود؛ این پول از کره جنوبی آمده بود و قطر قرار بود آن را به ما منتقل کند. ما به تعهد خود عمل کردیم، اما آمریکا به تعهدش عمل نکرد.» پزشکیان افزود: «آمریکا چیزی را که می‌خواهد می‌گیرد و بعد به تعهداتش عمل نمی‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/24240" target="_blank">📅 14:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بلومبرگ: پایگاه نظامی دائمی آمریکا در لهستان، موسوم به «فورت ترامپ»، ممکن است تا ۴.۴ میلیارد دلار هزینه داشته باشد.
رئیس‌جمهور لهستان، کارول ناوروتسکی، گفته امیدوار است این پایگاه پیش از پایان دوره ریاست‌جمهوری ترامپ در سال ۲۰۲۹ تکمیل و افتتاح شود. مذاکرات درباره
مسائل مالی و اداری و انتخاب محل و زیرساخت پایگاه
همچنان ادامه دارد. بر اساس گزارش بلومبرگ، این پایگاه می‌تواند محل استقرار حدود
۵ هزار نیروی آمریکایی
باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/24239" target="_blank">📅 14:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه، اعلام کرد که در سال ۲۰۲۷ به دلیل محدودیت‌های قانونیِ دوره تصدی، از سمت خود کناره‌گیری خواهد کرد، اما احتمال بازگشت دوباره به ریاست‌جمهوری در آینده را رد نکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/24238" target="_blank">📅 14:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرمول کلاهبرداران
@WarRoom</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/24237" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یاشار جان درود اینترنشنال الان باید آنفالو بشه یا زوده؟</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/24236" target="_blank">📅 14:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMojtaba Bahrami</strong></div>
<div class="tg-text">یاشار جان درود
اینترنشنال الان باید آنفالو بشه یا زوده؟</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/24235" target="_blank">📅 14:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24234">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗦𝗔𝗝𝗔𝗗™</strong></div>
<div class="tg-text">حاجی پس ما برقمون قطو وصل میشه بخاطر این لاشیا بود
🤣</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/24234" target="_blank">📅 13:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef185bab33.mp4?token=LUw9NngkQw5bcRnFw8PMwEKmDDS45fjdjt1wBcXoTS07Jy3fRyWUYnRNvCVl8jRS0fb2epaTJTo9ySZemCer696xWB9XwmgtP2s6NPpozWEAIiAYU5k3kqdiTY2kWpktIGG16FMsJUb2wkLx9cLrhKS39V97m2km6FEh3f39SNVEF0Xq-o0aILhg8pQIXUVRyQQnegg9czeuAD7gmuFUSqZWehAK1QmbfuZkffTrEveEVeDANZ_dgMu1e5RHmw7tFjS95b4tnDLybv96FSoTd10shcPoQtM0f2RE5DW9HArVnUGntoC5YwBX3ok8xNb4-B87pHGNWXSW-DKBi2ktog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef185bab33.mp4?token=LUw9NngkQw5bcRnFw8PMwEKmDDS45fjdjt1wBcXoTS07Jy3fRyWUYnRNvCVl8jRS0fb2epaTJTo9ySZemCer696xWB9XwmgtP2s6NPpozWEAIiAYU5k3kqdiTY2kWpktIGG16FMsJUb2wkLx9cLrhKS39V97m2km6FEh3f39SNVEF0Xq-o0aILhg8pQIXUVRyQQnegg9czeuAD7gmuFUSqZWehAK1QmbfuZkffTrEveEVeDANZ_dgMu1e5RHmw7tFjS95b4tnDLybv96FSoTd10shcPoQtM0f2RE5DW9HArVnUGntoC5YwBX3ok8xNb4-B87pHGNWXSW-DKBi2ktog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">IRAN: NO PLACE FOR AMATEURS
ایران جای آماتورها نیست
@WarRoom</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/24233" target="_blank">📅 13:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اگر بیماری قلبی دارید زیرزبانی دم دستتان باشد.
@WarRoom
😂</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/24232" target="_blank">📅 13:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رؤسای جمهور آمریکا و چین توافق کردند که ایران باید به تعهد خود مبنی بر عدم توسعه سلاح‌های هسته‌ای پایبند باشد و نباید برای گذرگاه‌های آبی بین‌المللی عوارضی وضع کند.
همچنین واشینگتن و پکن بر سر کاهش تعرفه‌ها به ارزش 30 میلیارد دلار توافق کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/24231" target="_blank">📅 13:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش شنیده شدن صدای انفجار در خارگ @WarRoom
🚨</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/24230" target="_blank">📅 13:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پزشکیان: در حال حاضر قطر و پاکستان پیام‌های ما را به واشنگتن منتقل می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/24229" target="_blank">📅 13:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش شنیده شدن صدای انفجار در خارگ
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/24228" target="_blank">📅 13:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ee584150.mp4?token=l84J5eEZoI3IC-BkZHvPp3nzQ6pYy8H7gsS0u4ECNu7L7n_EgLUDusnekK03LLEynrK0dQRE3YpBYt_FcIS3GY2jheej3vWjtQsmCH4GwakjjwZKd-Tqc8Xz26d6hOWx1f17hwKTqfhnPtmPqfwFqIjkoRJqr3Csa1avBiH5PGHoWOk4BWWP3Tg2v1D477Zy-_3E1pxtV6so7EvBfH8BIZPDqNfBMSkZ81xtp63Y41XbQTDICZwOUZP6iiy1Hijz9vuws-FWg6DoGXwBzeSurZSh3ZHT6PA5EtOBR-M499FyyfehSrNreuhoW2yZwZ3KMqd_eCjArJ0x9ckwjI6j7i2huBVwsYo1yopdUszgWV0q8YfD4BmJP87pqL5-cuFx7m8BtmRsAK9RZTNFdc9jVxg6rteoF_lQ-fpfJR49eer__17YKfldvWparlCa64mEymkgnHREwSk-60q6VuMXDOgO-F9ZcWze8OyTbAiHNXXVhYSjUb8rjvdq5uLguzRqoqkHj-l5uvioaInG3LvQ6yTKgi4xWgwVBAb7cEZw3pEtVWolzDK45Y40iVBMNBAPUeWRZGHhdO7Ai7eJXrsaDjZ4OoZqB3wGePM28ft_kLKou-ITNoxpn3ceQkg3pB2jVU9dEAvzJVLXk1YhLld04SfNZC1CfVw4bLtztBpNMEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ee584150.mp4?token=l84J5eEZoI3IC-BkZHvPp3nzQ6pYy8H7gsS0u4ECNu7L7n_EgLUDusnekK03LLEynrK0dQRE3YpBYt_FcIS3GY2jheej3vWjtQsmCH4GwakjjwZKd-Tqc8Xz26d6hOWx1f17hwKTqfhnPtmPqfwFqIjkoRJqr3Csa1avBiH5PGHoWOk4BWWP3Tg2v1D477Zy-_3E1pxtV6so7EvBfH8BIZPDqNfBMSkZ81xtp63Y41XbQTDICZwOUZP6iiy1Hijz9vuws-FWg6DoGXwBzeSurZSh3ZHT6PA5EtOBR-M499FyyfehSrNreuhoW2yZwZ3KMqd_eCjArJ0x9ckwjI6j7i2huBVwsYo1yopdUszgWV0q8YfD4BmJP87pqL5-cuFx7m8BtmRsAK9RZTNFdc9jVxg6rteoF_lQ-fpfJR49eer__17YKfldvWparlCa64mEymkgnHREwSk-60q6VuMXDOgO-F9ZcWze8OyTbAiHNXXVhYSjUb8rjvdq5uLguzRqoqkHj-l5uvioaInG3LvQ6yTKgi4xWgwVBAb7cEZw3pEtVWolzDK45Y40iVBMNBAPUeWRZGHhdO7Ai7eJXrsaDjZ4OoZqB3wGePM28ft_kLKou-ITNoxpn3ceQkg3pB2jVU9dEAvzJVLXk1YhLld04SfNZC1CfVw4bLtztBpNMEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مخزن سوخت یک جنگنده آمریکایی در ارتفاعات ایران پیدا شد: تصاویر منتشرشده از یک مخزن سوخت خارجی پیدا‌شده در ارتفاعات ایران، با توجه به صدا و جنس فلزی برای یک F-15E Strike Eagle است. چون F/A-18/EA-18G از
فایبرگلاس
استفاده می‌کنند ولی ساختار اصلی این مخزن از آلیاژهای آلومینیوم هوافضایی ساخته می‌شود و در بخش‌هایی از آن نیز فولاد، تیتانیوم و مواد پلیمری به‌کار می‌رود. این مخازن از نوع Drop Tank هستند و خلبان می‌تواند در شرایط عملیاتی، پس از مصرف سوخت یا برای کاهش وزن و مقاومت آیرودینامیکی، آنها را عمداً از هواپیما رها کند (Jettison)
@WarRoom</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/24227" target="_blank">📅 13:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1482c7d1a.mp4?token=nxv2dLnzpwlIQU1L9bqGg-t9KVgiLHnKb--Z-26eh5_cr5BAHlKAnVQ002eTnhTil4oqvRz4IsJHwhoJGygT1LQIEnJuI2bOVaywCZydMVIprwS6QrFHk2bR5IeAQbUV56Bs1UtOOQS_MApFSxP8PttsbHWtSS67BiekaYuD9J8eFYhQG-cWofjlkPHfiw8fiE_bpdKjepggOFrOiHnVu3LV5IDjudIxgd9WTzx_5Pob7X1PfewEsMzAz4b3-pOkaLlu0uArys2hIjEagRnRT3H60KdX8mtufruMYeBx05JEeKsRv-FY0MTONilp2kqxGuBEMTT0FhY_OLalwR_S9Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1482c7d1a.mp4?token=nxv2dLnzpwlIQU1L9bqGg-t9KVgiLHnKb--Z-26eh5_cr5BAHlKAnVQ002eTnhTil4oqvRz4IsJHwhoJGygT1LQIEnJuI2bOVaywCZydMVIprwS6QrFHk2bR5IeAQbUV56Bs1UtOOQS_MApFSxP8PttsbHWtSS67BiekaYuD9J8eFYhQG-cWofjlkPHfiw8fiE_bpdKjepggOFrOiHnVu3LV5IDjudIxgd9WTzx_5Pob7X1PfewEsMzAz4b3-pOkaLlu0uArys2hIjEagRnRT3H60KdX8mtufruMYeBx05JEeKsRv-FY0MTONilp2kqxGuBEMTT0FhY_OLalwR_S9Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش یک معتاد خمار از لانچر
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/24226" target="_blank">📅 12:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24225">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozpa_OxNbHF7Jt86aezQ6OqnpuQEgW4qYIdZJQCwX2X2Xp8fY4-EslE8viqMvWMcqprys1Ce-NxiGaTwUMRZlQ_CTngb9PJVqrQ0APq0sq8FA1W0O-sHfV36-GPqx5MlMr-S7kXO9oUUcZdCybJWSxBp0Jmv6ieDDLTdlrI_eVFK8SztlbmxmLI1jgb-__amEfbkif-c48cGQ-G9Eyr_qHO_FP2Ju8he8qjRYgTXnqoeCUZojYvJ2IVXP3AgaW7bZhw_rxhB8pdAy9Hek3YcVdKcctzXrfN-cng81Uy3b-fRxz-A1FziTTZvNGw-97Okg2R1h4rN2AT36f6EL5-Pjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرشکیان دو ساعت و نیم پیش نیویورک را ترک کرد و هم اکنون حدودأ در مرکز اقیانوس آتلانتیک شمالی است. بسیار جای مناسبی است تا کوسه‌ها او را بخورند.
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/24225" target="_blank">📅 12:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a6f13b5b5.mp4?token=sgccC8TSBLu1gVJxUrOMvstN3vkM8v5-oauJJknGTxC6ahagDC2tiBmCmMi3KAFWkS37rARqsHjgzDHkqlzsJZ3qrZMP4_ZFtSWMQ8oNAp3uRAp7Oh_DKcaUCZcgsW7ENV4NZ75vrtNKivamDo7maWayoAfsVOB68850xsJOEwpVkDAfH7hD1JZViT-0sUzJIqHP71bJKEra8JzmToZZi_ZB-j-ajGcN3vK1Ugw5WPOIcc8hCnBQ_2WXDTrKIfFK5yUaEjRsjrq-PVcZoaVBDuY_-DpTaITMqMFHAXmN4r9hj1Rm8z8UCFMd63uWputbCK6qMJkmAMzJ7i8VMB_D5j4ewDiNWmZtMp2i7_Bmyr8261KfwLr217ZFtFeuZaJb_B3qkdBodQumGexBnzoO0-Qr9_iTMgKBz2XNln1nDbzmYHJ5hu5S6t4GqO6hqTxeqfJlVukCUlyrmClVgKGKAYgDcVcyL5PwPg_EVYVqjMahdXhfU48gL4tTOhQp_J6sGIyOrvNSCHxvV5wRCHRvxFk7fciE_tQiDwyn__BnqNGO5JwzbP_3JuF-8dllcmVd7eWpr59kG4z4OduspSG_JG7h1vDgCQHTQ28DcU_eCm6pnxQWm5bSeo8NTWxdclJTklyx-dAlvudsnmgqKuFRS6C6duteZSHETGBdPgACntM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a6f13b5b5.mp4?token=sgccC8TSBLu1gVJxUrOMvstN3vkM8v5-oauJJknGTxC6ahagDC2tiBmCmMi3KAFWkS37rARqsHjgzDHkqlzsJZ3qrZMP4_ZFtSWMQ8oNAp3uRAp7Oh_DKcaUCZcgsW7ENV4NZ75vrtNKivamDo7maWayoAfsVOB68850xsJOEwpVkDAfH7hD1JZViT-0sUzJIqHP71bJKEra8JzmToZZi_ZB-j-ajGcN3vK1Ugw5WPOIcc8hCnBQ_2WXDTrKIfFK5yUaEjRsjrq-PVcZoaVBDuY_-DpTaITMqMFHAXmN4r9hj1Rm8z8UCFMd63uWputbCK6qMJkmAMzJ7i8VMB_D5j4ewDiNWmZtMp2i7_Bmyr8261KfwLr217ZFtFeuZaJb_B3qkdBodQumGexBnzoO0-Qr9_iTMgKBz2XNln1nDbzmYHJ5hu5S6t4GqO6hqTxeqfJlVukCUlyrmClVgKGKAYgDcVcyL5PwPg_EVYVqjMahdXhfU48gL4tTOhQp_J6sGIyOrvNSCHxvV5wRCHRvxFk7fciE_tQiDwyn__BnqNGO5JwzbP_3JuF-8dllcmVd7eWpr59kG4z4OduspSG_JG7h1vDgCQHTQ28DcU_eCm6pnxQWm5bSeo8NTWxdclJTklyx-dAlvudsnmgqKuFRS6C6duteZSHETGBdPgACntM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در مصاحبه با شبکهCBS: هر بار که تفاهم هم کردیم باز حمله کردند و کشتنمان،  آمریکا به تفاهم عمل نمی‌کند، مذاکره کردن چه مشکلی را حل می‌کند؟
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/24224" target="_blank">📅 11:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24223">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتاق جنگ با یاشار : به زودی قیمت سوراخ موش در‌ ایران سر به فلک خواهد کشید …
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/24223" target="_blank">📅 11:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وال‌استریت‌ژورنال : ترامپ قصد ندارد محاصره دریایی بنادر ایران را لغو کند؛ واشنگتن امیدوار است فشار اقتصادی، تهران را به پذیرش شروط آمریکا(تسلیم) وادار کند. @WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/24222" target="_blank">📅 11:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وال‌استریت‌ژورنال : ترامپ قصد ندارد محاصره دریایی بنادر ایران را لغو کند؛ واشنگتن امیدوار است فشار اقتصادی، تهران را به پذیرش شروط آمریکا(تسلیم) وادار کند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/24221" target="_blank">📅 11:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کوین‌دسک ,
رشد برخی آلت‌کوین‌ها
: در گزارش بازار روز جمعه، کوانتوم (QNT) حدود
۳۸
درصد، اوندو (ONDO) حدود
۲۸
درصد و چین‌لینک (LINK) حدود
۱۱
درصد رشد روزانه ثبت کرده بودند. این ارقام قیمت لحظه‌ای امروز نیستند
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/24220" target="_blank">📅 11:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">روزنامه گاردین: عباس عراقچی، وزیر امور خارجه ایران که پیش از پزشکیان به نیویورک رفته بود، قصد دارد تا یکشنبه ۵ مهر در این شهر بماند
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/24219" target="_blank">📅 11:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏سیدمحمد مرندی، مشاور پیشین تیم مذاکرات هسته‌ای رژیم جمهوری اسلامی، مدعی شد مذاکرات غیرمستقیم با دولت ترامپ بدون پیشرفت بوده و منطقه به سوی تشدید تنش می‌رود. او همچنین کشورهای حاشیه خلیج فارس را به همراهی با آمریکا در جنگ علیه ایران متهم کرد و اقدامات ترامپ و اسکات بسنت را «توطئه علیه مردم ایران» خواند.
@WarRoom</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/24218" target="_blank">📅 11:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رویترز ، عربستان، ترکیه و پاکستان هماهنگی امنیتی را افزایش دادند: مقام‌های دفاعی سه کشور در ریاض درباره وضعیت امنیتی منطقه، تبادل اطلاعات، هماهنگی نظامی و یکپارچه‌سازی نیروها گفت‌وگو کردند. این نشست در چارچوب توافق دفاعی مشترک مکه برگزار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/24217" target="_blank">📅 11:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24216">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">«یک مقام ارشد اطلاعاتی اسرائیل، در توصیف میزان ویرانی رفح در سال ۲۰۲۶، گفته است: تقریباً هیچ ساختمانی در رفح باقی نمانده، مگر ساختمان‌هایی که تصمیم گرفته شده بود حفظ شوند.»
@WarRoom</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/24216" target="_blank">📅 11:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a2522c0a.mp4?token=TNX4lFiRVRYol0UXRgWMNY-dXCN9gnihGBo6MOaAhs3-Z14VEqMDI7JmipkMfvnTUPEKIDHHoyzDyTjZ_zmRFaD3oBaen17WLLeV_eNqJmAJy47WYYf2Mm8CH2fdnQ1mTaozstSeXjXMmixvcaaod-W1pstOfUAPjmZ8PnUitTcwR56Fx8skJW8KwO-0So91Uza6yCA_JqMq7tXDT_zN0OSinmVIalKWnpBXPUlsNCoV3LgRBPNm4bOe_jTXRTvzsIm3hOTfsgiu7SXL4RTXHpaD-Do_eMTvg6RmLPaG6SzXd92RE_atEGH58Xl6OUoQ-GRicDf4VjDIsEOkI_f-YKh-jBJ57SXyeggveXmL9BxziF8U-cTgDj95dHJgV73Zq9Q2KQThPWZEM-pmEan6pIqy-nNYP0tsiGyl1quaEeOs6LdwE83p81MejFJs8OJn4bhypV2e7cIUok89TdOJe5bdFXv3JC4_e7eAEItHcvF4K1B9h_4hxoxTmbCZNqHwMM71LUjYuYKR7yaHOcSDuz41_6XY4VOFVYb2hr87grIQjkttjtY8yO9L1ZApV8dxCi-DJVkqTNNCvMeySIC14bzj-yn2mVr_MhEArlaPr-SnYw7V0yiG4RuYnbN3zgmVv-d2iJZkHIj7hYieZA6kXHa1XekKxLhASaYlY-uneBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a2522c0a.mp4?token=TNX4lFiRVRYol0UXRgWMNY-dXCN9gnihGBo6MOaAhs3-Z14VEqMDI7JmipkMfvnTUPEKIDHHoyzDyTjZ_zmRFaD3oBaen17WLLeV_eNqJmAJy47WYYf2Mm8CH2fdnQ1mTaozstSeXjXMmixvcaaod-W1pstOfUAPjmZ8PnUitTcwR56Fx8skJW8KwO-0So91Uza6yCA_JqMq7tXDT_zN0OSinmVIalKWnpBXPUlsNCoV3LgRBPNm4bOe_jTXRTvzsIm3hOTfsgiu7SXL4RTXHpaD-Do_eMTvg6RmLPaG6SzXd92RE_atEGH58Xl6OUoQ-GRicDf4VjDIsEOkI_f-YKh-jBJ57SXyeggveXmL9BxziF8U-cTgDj95dHJgV73Zq9Q2KQThPWZEM-pmEan6pIqy-nNYP0tsiGyl1quaEeOs6LdwE83p81MejFJs8OJn4bhypV2e7cIUok89TdOJe5bdFXv3JC4_e7eAEItHcvF4K1B9h_4hxoxTmbCZNqHwMM71LUjYuYKR7yaHOcSDuz41_6XY4VOFVYb2hr87grIQjkttjtY8yO9L1ZApV8dxCi-DJVkqTNNCvMeySIC14bzj-yn2mVr_MhEArlaPr-SnYw7V0yiG4RuYnbN3zgmVv-d2iJZkHIj7hYieZA6kXHa1XekKxLhASaYlY-uneBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در شبکه CBS: اسرائیل هر کسی رو که دلش بخواد با تواناییی که داره ترور می‌کنه، با پشتیبانی آمریکا. رهبر ما مگه تروریست بود که کشتنش. خیلی راحت میان ترور می‌کنن و بعد به دنیا می‌گویند ما با تروریست‌ها می‌جنگیم.
@WarRoom</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/24215" target="_blank">📅 11:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c51e273e7.mp4?token=PGkvvdfmSuKd6TKAeV5ilY0XcVhjhDqdQiqpiYGtQYxT0oi-_0FfqvMd1f0tUKazjE6FM-lMqXqc5FFrUwiRCdU1XRS7Ik0tmpUlU6vh3YiI4XcXOWQLhbKcX4uz0Fibm-DECqKi23I7mHmFdN22w1FguTXxoFn9b-A6Cr1fGdEgL9zu7dPFAihLulcnKni4C8538LCBlSrwmJySIeiZahppIwaDBDOEOaR5OljrLwHnZCcF2a7GchG6mpUjqYOcJ1NK6zO9THKSAM7G9Vje5XIJZwmdUgQzLgI-HY6kkxnqdcIalCQ8rNXIfYxC9yEvkJAKW6RDIzVe0eqycbtBpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c51e273e7.mp4?token=PGkvvdfmSuKd6TKAeV5ilY0XcVhjhDqdQiqpiYGtQYxT0oi-_0FfqvMd1f0tUKazjE6FM-lMqXqc5FFrUwiRCdU1XRS7Ik0tmpUlU6vh3YiI4XcXOWQLhbKcX4uz0Fibm-DECqKi23I7mHmFdN22w1FguTXxoFn9b-A6Cr1fGdEgL9zu7dPFAihLulcnKni4C8538LCBlSrwmJySIeiZahppIwaDBDOEOaR5OljrLwHnZCcF2a7GchG6mpUjqYOcJ1NK6zO9THKSAM7G9Vje5XIJZwmdUgQzLgI-HY6kkxnqdcIalCQ8rNXIfYxC9yEvkJAKW6RDIzVe0eqycbtBpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضجه های حقیرانه پزشکیان در شبکه سی‌بی‌اس: آنها دنبال این هستند جامون رو پیدا کنند و هر وقت دلشون خواست بکشنمون ما گفتگو می‌کردیم که آنها ترورها را آغاز کرده‌اند. هیچ ضمانتی وجود ندارد که دوباره آمریکا و اسرائیل دست از ترورها بردارند.
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/24214" target="_blank">📅 11:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873be0f119.mp4?token=JX_Jn9knalLfO9VCdSv33pbWcknpKTtr7w7D4hxScEbHPn5f9vRSyhtunWqW9vD9woChA6l5E_14nYMIhnsNKtPNGqB8_rz1tGhcx2Kro7ZCMcms8K6QNWjDX1V4nEnN0EnqGrF3lk_aSlI_kAHt3-Ppq4nYt1WeNS0Hu7828X9KZqeOdKt2o9vtNrD2pVUFU2KwhMOG9xkGYPJVQlyZ--HeuceUR6ANh09FlvssdXALqx5qCv04mnuxM3gNCmiYZaKQDfEUNCS_02jduZgZC89pvdHgLBx4vAyvwxbonReSpZJePuM5xfa2YBaLpvX57QsHSq3iiEg6aiyHtWFTKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873be0f119.mp4?token=JX_Jn9knalLfO9VCdSv33pbWcknpKTtr7w7D4hxScEbHPn5f9vRSyhtunWqW9vD9woChA6l5E_14nYMIhnsNKtPNGqB8_rz1tGhcx2Kro7ZCMcms8K6QNWjDX1V4nEnN0EnqGrF3lk_aSlI_kAHt3-Ppq4nYt1WeNS0Hu7828X9KZqeOdKt2o9vtNrD2pVUFU2KwhMOG9xkGYPJVQlyZ--HeuceUR6ANh09FlvssdXALqx5qCv04mnuxM3gNCmiYZaKQDfEUNCS_02jduZgZC89pvdHgLBx4vAyvwxbonReSpZJePuM5xfa2YBaLpvX57QsHSq3iiEg6aiyHtWFTKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی‌بی‌اس: «اگر رئیس‌جمهور ترامپ این پیشنهاد را بپذیرد، آیا می‌توانید تضمین کنید که نیروهای نظامی ایران هم به آن پایبند خواهند بود؟»
مسعود پزشکیان: «طبیعتا هر تعهدی که بپذیریم، پایبند خواهیم بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/24213" target="_blank">📅 11:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0590db4d.mp4?token=JiLLUm-FNFBzWH5LWXktDCu7TP5KGCNVGco4xjRQy65aNu4Ppyo5eVlpF1L6EcRhqWhyXGfsJwmLoTbW4uTxE25k3WxFXmSCBm-Hi2W96azRsWg7hSJCm5jMHXCBZgnc8aU3AbEuQsyT9YJGcHqfy0K6lbBO8_fPO664nBB5M9g5dN8njccZzIAdBhZFF_lFXwCrwHXLXcG5ROnSiuo0f94PJcsmg7GwDi-Bv8Z9rBM37wzrbenhnBScixToYgxnvXVH9G6NKEfn72F8iDu0i71kMSZ4JjTDFV2wW5oWu05RdA4N5iPiUfidEC0po8ZOmz2zmAgsTQprcwPlT-JTxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0590db4d.mp4?token=JiLLUm-FNFBzWH5LWXktDCu7TP5KGCNVGco4xjRQy65aNu4Ppyo5eVlpF1L6EcRhqWhyXGfsJwmLoTbW4uTxE25k3WxFXmSCBm-Hi2W96azRsWg7hSJCm5jMHXCBZgnc8aU3AbEuQsyT9YJGcHqfy0K6lbBO8_fPO664nBB5M9g5dN8njccZzIAdBhZFF_lFXwCrwHXLXcG5ROnSiuo0f94PJcsmg7GwDi-Bv8Z9rBM37wzrbenhnBScixToYgxnvXVH9G6NKEfn72F8iDu0i71kMSZ4JjTDFV2wW5oWu05RdA4N5iPiUfidEC0po8ZOmz2zmAgsTQprcwPlT-JTxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/24212" target="_blank">📅 10:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a70d94d064.mp4?token=tFpHTfPX3WBJLC7jTE_fNGcJYIuT22i7PTRma6hyqvm08Wg5bFWbXcfuNb43HkPNA0oJFFzj9RzfP-_9pqJItBaxVgXagIGxELhAymx2rJWmNHfh3OHrycc3YQpTYV4wXkknT62HZVY9-Beo59LLViF1inA7OXEKsWgw9SJoU7LxdO3c4MGnbvbYxm3gv_JgL7X87DJZdCFZJdO4_AAH62vCkEcz08hXv9AtZQXMP8rwlgNgxZ_FdpdJBWjQ5QCs827w7GUhHm14POZeezTq9NOZuwReo8THm9mOXpy4Nz3WZMglvBGC_Yihjq-P4tTiQ4MmAASBo_T2VxHZSwwhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a70d94d064.mp4?token=tFpHTfPX3WBJLC7jTE_fNGcJYIuT22i7PTRma6hyqvm08Wg5bFWbXcfuNb43HkPNA0oJFFzj9RzfP-_9pqJItBaxVgXagIGxELhAymx2rJWmNHfh3OHrycc3YQpTYV4wXkknT62HZVY9-Beo59LLViF1inA7OXEKsWgw9SJoU7LxdO3c4MGnbvbYxm3gv_JgL7X87DJZdCFZJdO4_AAH62vCkEcz08hXv9AtZQXMP8rwlgNgxZ_FdpdJBWjQ5QCs827w7GUhHm14POZeezTq9NOZuwReo8THm9mOXpy4Nz3WZMglvBGC_Yihjq-P4tTiQ4MmAASBo_T2VxHZSwwhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید امیدبخش ترامپ در تروث شامل صحنه‌ای از منهدم کردن لانچر رژیم جمهوری اسلامی
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24211" target="_blank">📅 05:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری ABC : در شروع عملیات، اسرائیل اعلام کرد حدود ۲۰۰ جنگنده در بزرگ‌ترین مأموریت پروازی تاریخ نیروی هوایی اسرائیل شرکت کردند و حدود ۵۰۰ هدف را زدند.  آمریکا در نخستین ۲۴ ساعت بیش از ۱۰۰۰ هدف را در عملیات چندمحوره مورد حمله قرار داد. طبق آمار بعدی، تا…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24208" target="_blank">📅 05:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24207">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرگزاری ABC : در شروع عملیات، اسرائیل اعلام کرد حدود
۲۰۰ جنگنده
در بزرگ‌ترین مأموریت پروازی تاریخ نیروی هوایی اسرائیل شرکت کردند و حدود
۵۰۰ هدف
را زدند.  آمریکا در نخستین ۲۴ ساعت بیش از
۱۰۰۰ هدف
را در عملیات چندمحوره مورد حمله قرار داد. طبق آمار بعدی، تا ۲۳ مارس بیش از
۱۰ هزار پرواز رزمی
و بیش از
۱۰ هزار هدف
در عملیات ثبت شده بود. گزارش سپتامبر Air & Space Forces Magazine می‌گوید Epic Fury در مجموع به
بیش از ۱۳ هزار هدف
حمله کرد و حدود
۱۰ هزار سورتی رزمی
در ۳۸ روز اوج عملیات انجام شد. همان منبع آن را
بزرگ‌ترین کارزار هوایی آمریکا در یک نسل
توصیف می‌کند. خود CENTCOM در ابتدای عملیات آن را
بزرگ‌ترین تمرکز منطقه‌ای قدرت آتش آمریکا در یک نسل
نامید.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24207" target="_blank">📅 04:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">۱۵ روز قبل از شروع جنگ ۴۰ روزه ۰۲/۱۳/۲۰۲۶</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24206" target="_blank">📅 04:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9961f001.mp4?token=k1LsUyZQht_VcaZXlAYBDXt5o0M8mX9LuWbXzmxaom2mTTyKXs28VeRpPhvQeHYC0ifHFSgDWamKE39MMnylipmjd3kFbxO8h1RgCq56f1azHe3OAQKm2uQZLnI27wJowAodcjmn-JR58vRxSSF-t2iQPdD3_ILkFKKBZCMMacywq7uPWH2YmB-zA_Ja_OSkTOuxHzXU94Jk6qrYNciwktgVJrBFBzMvfte7bFYRPNXTSsN3byWPnmWhD_QOzq6IFuzNIgfAvbyBRzE3DlKFIDUvEdUncqpIUksBnXeRLKqAMgy1C2Qyes_hFhNonUrbPMicCzBAqrTE7g7NinGK_wQE8xRy42nUH0yW7MxHecbF-HeHnYqa_vHdotBXHSSSYZlo5uwKS2L_9_pf4q4ZpNoRE-EDKZD4rkeYsYAxeFEEy6AYrihVLO4O6CHEDgDWpVuvi7qd7cN3T0BTmI6ee5VB_qkHUN6sEzzL4T2e6cpV5Goyu2aVJ7M4K6VN5-A_4KRMVMfOTkflusos_ZcDj2OYbQ-75ggZpcffVFkepZnxbGy5ZW5oo1OOhWDx8kNdGszGET5yEqZbPZ3S3lyPQ7XQbI-Gw8-XtigWAmWKwvyBxZAj6oMlv6F1DAyC029QCPhhMC1M7qPN0otbHa6p2Di7-GCD0XyBo3YUteZgEgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9961f001.mp4?token=k1LsUyZQht_VcaZXlAYBDXt5o0M8mX9LuWbXzmxaom2mTTyKXs28VeRpPhvQeHYC0ifHFSgDWamKE39MMnylipmjd3kFbxO8h1RgCq56f1azHe3OAQKm2uQZLnI27wJowAodcjmn-JR58vRxSSF-t2iQPdD3_ILkFKKBZCMMacywq7uPWH2YmB-zA_Ja_OSkTOuxHzXU94Jk6qrYNciwktgVJrBFBzMvfte7bFYRPNXTSsN3byWPnmWhD_QOzq6IFuzNIgfAvbyBRzE3DlKFIDUvEdUncqpIUksBnXeRLKqAMgy1C2Qyes_hFhNonUrbPMicCzBAqrTE7g7NinGK_wQE8xRy42nUH0yW7MxHecbF-HeHnYqa_vHdotBXHSSSYZlo5uwKS2L_9_pf4q4ZpNoRE-EDKZD4rkeYsYAxeFEEy6AYrihVLO4O6CHEDgDWpVuvi7qd7cN3T0BTmI6ee5VB_qkHUN6sEzzL4T2e6cpV5Goyu2aVJ7M4K6VN5-A_4KRMVMfOTkflusos_ZcDj2OYbQ-75ggZpcffVFkepZnxbGy5ZW5oo1OOhWDx8kNdGszGET5yEqZbPZ3S3lyPQ7XQbI-Gw8-XtigWAmWKwvyBxZAj6oMlv6F1DAyC029QCPhhMC1M7qPN0otbHa6p2Di7-GCD0XyBo3YUteZgEgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24205" target="_blank">📅 04:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ پیشنهاد آتش‌بس ایران را رد کرده و از احتمال تشدید بمباران‌ها پس از انتخابات میان‌دوره‌ای آمریکا خبر داد @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24203" target="_blank">📅 04:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24202" target="_blank">📅 04:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24201">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383cae6fd9.mp4?token=pJedq7bFgNZ8plMdtFMi2_gn5jPuzZCymw0ZrC5LEJAVG3IIQtERudS9nuLqf5bDMbtpDEebNaBndGNJmXAna-ogBYs6OIUX0SnHzZ2lXHzzKNLy8Yp4ViTaenxLWN9BdIVAy5yhkCSMPY9T_sLKkKp0g14XD2ROjM1-JPHFN1jR_Deww2XPZM9_NbI3vwuvbeBk6zZBZmM0ik-2L3DJuddG4ub6mOfXEqdWVR8HNIfzvEmJLRlom8AxaIEHoiMHgosmh6oYsHpk0eFpNB38DzalnbVNeo-G5JJKVGsni9FkoYbXRv-2uiSH8CuV-M6kunLtKsKr41owuAkcaiPhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383cae6fd9.mp4?token=pJedq7bFgNZ8plMdtFMi2_gn5jPuzZCymw0ZrC5LEJAVG3IIQtERudS9nuLqf5bDMbtpDEebNaBndGNJmXAna-ogBYs6OIUX0SnHzZ2lXHzzKNLy8Yp4ViTaenxLWN9BdIVAy5yhkCSMPY9T_sLKkKp0g14XD2ROjM1-JPHFN1jR_Deww2XPZM9_NbI3vwuvbeBk6zZBZmM0ik-2L3DJuddG4ub6mOfXEqdWVR8HNIfzvEmJLRlom8AxaIEHoiMHgosmh6oYsHpk0eFpNB38DzalnbVNeo-G5JJKVGsni9FkoYbXRv-2uiSH8CuV-M6kunLtKsKr41owuAkcaiPhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏هم اکنون مایک والتز ⁦سفیر آمریکا در سازمان ملل : رژیم تروریست جمهوری اسلامی باید از بین برود
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24201" target="_blank">📅 04:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/24200" target="_blank">📅 04:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">واشنگتن‌پست: پنتاگون ۳۷ نظامی مجروح دیگر را به آمار جنگ ایران اضافه کرد؛ مجموع به ۸۶۱ نفر رسید.
پنتاگون این هفته بدون توضیح عمومی، ۲۹ ملوان نیروی دریایی و ۸ تفنگدار دریایی را به آمار مجروحان اضافه کرده است. زمان و نحوه مجروح‌شدن این افراد اعلام نشده و یک مقام نیروی دریایی گفته ملوانان به خدمت بازگشته‌اند. مقام‌های دفاعی پیش‌تر گفته بودند ثبت آمار تلفات ممکن است با تأخیر انجام شود، از جمله در موارد ضربه مغزی و آسیب‌های مغزی که علائم آن‌ها دیرتر بروز می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/24199" target="_blank">📅 04:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/24198" target="_blank">📅 04:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/24197" target="_blank">📅 04:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ پیشنهاد آتش‌بس ایران را رد کرده و از احتمال تشدید بمباران‌ها پس از انتخابات میان‌دوره‌ای آمریکا خبر داد @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/24196" target="_blank">📅 04:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdZL7kHrt2ZjIsD73vvNHwMbvQF5x1IzxezkY3olgMVqM_jqu6CkW9f2QaUIYaKTVZELYX1pVpuup8Zk7_9QR8wOyNTclcdSsYeyLw6QM_rhHXaJ8Xn7Wmvb4RwOFWNxSuNg-PfyYHpTRRACzi9W62ivg6eDMpbUEGCxs9IK8pcJ3EQ0qOtf-rQ6sjjlQDlTor-XQEZn-TbCUq2IIytPso-gNfBKEsxyvPtSJDLAjxumOvs8oC3LqhPOAC0rNHFurlzGNKb59kvmNrQijEK30X99wBQlQ5M-mLD_jh_wyjsQ6GdwPEQReWy-zZvLpPKaeqf9zLh9NGHy_l2xaOybVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ پیشنهاد آتش‌بس ایران را رد کرده و از احتمال تشدید بمباران‌ها پس از انتخابات میان‌دوره‌ای آمریکا خبر داد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/24195" target="_blank">📅 04:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/24194" target="_blank">📅 03:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/24193" target="_blank">📅 03:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/24192" target="_blank">📅 03:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/24191" target="_blank">📅 03:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d80d824a.mp4?token=c94lCXH2ik4Rrqfgj2wUdSq7kho7y4riLtGzhnSgK7lBhwdxnUK9nKx43q6uPglmRblGS8DBkbY4EnLxtR9SYabWL48suQkHMPw751CgKjM3l78TcsO4YydjGHLd2ly_chBMYpJpYZIClAjYyAssrtmGFzLQfsG8B_Y-wtOasFdxXwk3_L-mZYzx3a10eJtXBvHysQ5PEyBd1cXS02Q0ag3fExB3UGgf9uflrfWItdk-QxMqxYmvk_ZbBhVCIGLHlOvK9I7NewfZy2fj5rLk2Gu_B9WD_zNpYqy0je6h40BEsZqhuzEz-b5_7qIlZmXeqWBe1uptrN63RGwnLC95tjxVQ207oky_LygbrJdPf9l_3xooBFvdObPMRmvcYdFw3Z9YMgCSwK86qTzAi1aRxQBMNMyEemkf0medcFXwcGPExH66Fl0dTrnP91BBeZ_m1OvuLXeyrzIcm-UVAif3DQ3Fd4Z5fTf-GZ0xsjSMs7BT4oG2dnFKGx5B_EN_0qwdCFOSCfHBGwJbY_T3c3Bh8qwh9t9yLqgKabeO9E37ZEyL21tv-KqGpwHt2PJxCg8PUv1kgmLRzWY1N7RBguoZFq7msJcVmISvUFfSVMS7wpWKQNm8NuMwhRaiKG3nLNqTIUrR6Zm6CjaZKo9ycIdyoe755kHBIJUdpasFQEbX6Ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d80d824a.mp4?token=c94lCXH2ik4Rrqfgj2wUdSq7kho7y4riLtGzhnSgK7lBhwdxnUK9nKx43q6uPglmRblGS8DBkbY4EnLxtR9SYabWL48suQkHMPw751CgKjM3l78TcsO4YydjGHLd2ly_chBMYpJpYZIClAjYyAssrtmGFzLQfsG8B_Y-wtOasFdxXwk3_L-mZYzx3a10eJtXBvHysQ5PEyBd1cXS02Q0ag3fExB3UGgf9uflrfWItdk-QxMqxYmvk_ZbBhVCIGLHlOvK9I7NewfZy2fj5rLk2Gu_B9WD_zNpYqy0je6h40BEsZqhuzEz-b5_7qIlZmXeqWBe1uptrN63RGwnLC95tjxVQ207oky_LygbrJdPf9l_3xooBFvdObPMRmvcYdFw3Z9YMgCSwK86qTzAi1aRxQBMNMyEemkf0medcFXwcGPExH66Fl0dTrnP91BBeZ_m1OvuLXeyrzIcm-UVAif3DQ3Fd4Z5fTf-GZ0xsjSMs7BT4oG2dnFKGx5B_EN_0qwdCFOSCfHBGwJbY_T3c3Bh8qwh9t9yLqgKabeO9E37ZEyL21tv-KqGpwHt2PJxCg8PUv1kgmLRzWY1N7RBguoZFq7msJcVmISvUFfSVMS7wpWKQNm8NuMwhRaiKG3nLNqTIUrR6Zm6CjaZKo9ycIdyoe755kHBIJUdpasFQEbX6Ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از مهمانان ضیافت شام دفتر نمایندگی مفت خورهای جمهوری اسلامی در نیویورک تحت عنوان «دیدار با ایرانیان فرهیخته و مقیم ایالات متحده آمریکا»
@WarRoom</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/24190" target="_blank">📅 03:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX4cik0V7_m7hcPjBnd0zFdIVtcCOIp5b02ns4UhcAnk1l7AoBc2Af7cgZzzfxXBGa8aZHKxKKIsfWm7Qd2THDWt8T0EdPE2Ox15hE03VpL-VuR_1jSx4vRzvQVMipM2PFvbbXT6ExOa0tBAf5yUFvuCvwfd5Rbjv3ny-g3VKO-Wo9A0t22yzkeTX2EeR5GlyBPVWJwOj9FBaxvUEAdqWPKadsXQNVYSnLoi7O4UQR107JSjBkqhXiwsXx2l6wb4MJbFxnNxoYK_Nc46Vrcr7J070tUlBw9Rs8d80Q3beOVfzVfeWTCBqWW1ePNoh5RNvQhfRrQFbo4vUcD9cRjrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ریخت و وارد کانال ۹۷$ شد
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/24189" target="_blank">📅 03:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/24188" target="_blank">📅 03:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/24187" target="_blank">📅 03:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/24186" target="_blank">📅 03:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش صدای انفجار شدید از‌ تنگه ، پیغام های زیاد از بندر و قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/24185" target="_blank">📅 02:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش انفجار شدید / شاید شایذ پرتاب از مرکز شهر تبریز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24184" target="_blank">📅 02:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من قدم ۱۹۱ هست
😂
عکس‌ ها رو هم عزیزان دلم درست میکنند
😼</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24183" target="_blank">📅 02:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🩵</strong></div>
<div class="tg-text">با قد ۱۶۰سانت واسمون کماندو شدی</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24182" target="_blank">📅 02:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کمیسیون بورس و اوراق بهادار آمریکا (SEC) توضیحات جدیدی درباره قوانین کریپتو منتشر کرد!
طبق این توضیحات، بازخرید توکن توسط یک پروژه لزوماً باعث نمی‌شود آن توکن اوراق بهادار محسوب شود. همچنین توکن‌هایی که کاربران در ازای استیک کردن دارایی‌هایشان دریافت می‌کنند نیز در برخی شرایط اوراق بهادار محسوب نمی‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24181" target="_blank">📅 01:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عراقچی هم اکنون : سیا توبه توبه سیا نرمه نرمه
البته CIA
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24180" target="_blank">📅 01:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlGzbtiQjURRJ0QlLpjU8mxGKDU57y_43F2FZnrKbgA1loY_cY2QP7c_WsFb0posAr3XQUrjbGPX8BXxkIX8HiRcSynbwlnMVl3cYUlfmEQkW1VCee7g-CrGVDppwRKMK9vFQsE2m6Gs6iAIPK-gAIdIFm1B6lVYbXBUssZ4oo_hBw1gbGCS1-pPy9qRjOLcG-zpRo9U_i0ncLbWMrcHSHEdOJEJFU3t4J0hY6Y4szkFuWHljAPgV4o8szMyiKZWzR_Qu60ZX9NCzlDU961UWvDFp1B-rGhIbUakl6pNx2lfHKdUJv9K-l0qQjE1euB5bIDQR2NV8WBHnSJvi2OE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ سوخترسان جدید الان از قطر بلند شدن در‌ مجموع ۵ سوخترسان همگی ‌از قطر و ۱ پی ۸ از بحرین از که از ۸ ساعت پیش در حال انجام ماموریت بر فراز خلیج فارس و تنگه هرمز هستند
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24179" target="_blank">📅 01:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خانعلی‌زاده : دستاورد سفر نیویورک رئیس‌جمهور و وزیر‌امورخارجه، افزایش احتمال اقدام نظامی علیه ایران بود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24178" target="_blank">📅 01:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromادمین</strong></div>
<div class="tg-text">یاشار. داداش من الان رسیدم پیام هات رو دارم یکی یکی نگاه میکنم من و خانومم خیلی وقته اینتر آشغال رو نگاه نمی‌کنیم کلا پاک کردیم خیلی روحیه مون خوب شده من که فقط کانال تو رو دنبال میکنم ،دهنت سرویس چقدر تو کانالت خندیدم،بزار اعتراف کنم اولین کانالی هستی هم اطلاع رسانی هم تربیت هم فرهنگ سازی هم مبارزه طلبی و هم خنده و روحیه خوب داری به مردم یاد میدی در کل عشقی داداش</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24177" target="_blank">📅 01:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L50LwyyecxVZ8rMVp654LTLWH9jtsLjwM5w6iCetHVG3lxFzlc3kz9zRMKjyfGy4cfzhtLhcCK1dsczNHAFee79bxIPHrcYhK0uK9YQ0t3GO2OXD5ux3cft_zPsqqCxSQOIikXmdyqNe0VD-QxgNO8VpZa2Ybhl2U4pVFkpc2YMnGYPaXbR4n20iAHonebo2PIEuoluDomT-ukXpRJ8JZQXfEzrBjVV6JoKXrPzjrepO9WSiX2qvTGxaI0fEjaWPfs7C18gTMq61XUwXMvz8u6t9HCg3yz9uruFvE-5Q6oEiXEl4H6aZi7hhL3XajH9rQLBhJNPNssNN_DiilkQ-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : ایران آزاد میشه
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24176" target="_blank">📅 01:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عراقچی: ما از طریق قطر، این پیام را به آمریکا را منتقل کردیم
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24175" target="_blank">📅 00:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امشب دیرتر‌ میرم بالا منبر</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24174" target="_blank">📅 00:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24173">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدای ریکشنا نمیادااا اهااااا بیا وسطط</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24173" target="_blank">📅 00:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24172">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پرتاب ۴ موشک از سیریک با صدای کشته شده های حکومتی‌که راننده مست زد پرتشون کرد اونور بلوار
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24172" target="_blank">📅 00:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نماینده اسرائیل یه استارلینک میبره برای نمایندهی ایران در صحن سازمان ملل و می‌گه اینو بگیر به کارت میاد. و می‌گه ما عاشق مردم ایران هستیم و برای تغییر رژیم دعا می‌کنیم. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24171" target="_blank">📅 00:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل گفت اسرائیل هم خواهان تغییر حکومت در ایران است و هم به تحقق آن امید دارد. او افزود این موضوع هدف رسمی عملیات نظامی اسرائیل نیست، اما به گفته او، تحقق چنین تغییری به سود مردم ایران و کل منطقه خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24170" target="_blank">📅 00:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عراقچی در نشست خبری نیویورک:
اگر شرایط فراهم بشه و فضا از فشار و تهدید دور باشه، تنگه هرمز ظرف ۷ روز باز می‌شه و امنیت کشتیرانی هم تضمین خواهد شد.
این مهلت ۷ روزه از زمانی شروع می‌شه که آمریکا طرح پیشنهادی جمهوری اسلامی رو بپذیره؛ الان توپ در زمین آمریکاست.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24169" target="_blank">📅 00:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سنتکام: رزمایش «شیر آماده ۲۰۲۶» در آمریکا به پایان رسید.
این رزمایش دو هفته‌ای روز ۲۴ سپتامبر در پایگاه فورت کارسون ایالت کلرادو به پایان رسید و بیش از
۲۰۰ نیروی نظامی آمریکایی و اردنی
در آن شرکت داشتند. این نخستین‌بار بود که رزمایش «شیر آماده» در خاک آمریکا برگزار می‌شد و آموزش‌ها بر
عملیات ستاد فرماندهی مشترک، دفاع سایبری، واکنش به بلایای طبیعی و افزایش هماهنگی عملیاتی
میان نیروهای دو کشور متمرکز بود. این رزمایش دوازدهمین دوره «شیر آماده» و بخشی از همکاری دفاعی بیش از
۲۲ ساله آمریکا و اردن
محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24168" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سلامتی همگی
😂</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24167" target="_blank">📅 23:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24166">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مستند «پیجینگ حزب‌الله» درباره پشت‌پرده عملیات انفجار پیجرها و بی‌سیم‌های حزب‌الله در سپتامبر ۲۰۲۴ ساخته شده است. در این مستند
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیوید بارنیا، رئیس پیشین موساد، دیوید پترائوس، رئیس پیشین سازمان سیا
و چند مقام و چهره اطلاعاتی اسرائیلی و آمریکایی حضور دارند. این مستند به کارگردانی جاستین فولک ساخته شده و قرار است
۳۰ اکتبر ۲۰۲۶، برابر با ۸ آبان ۱۴۰۵
در آمریکا اکران شود.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24166" target="_blank">📅 22:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIuwAvl51S0Q-xvc5ZqikhX-aGkCeOYjsPZ2hK0_tQo3UeFvWZYIsGCYSr0AVOghASzTXwCMfnZz89-__EzshSQcslGafyDC-qROrIVn4dFcAEvxqKRW84SXmg2XyzxZMy0KLjiLUEjAsdyNN8nn_k_QzGcCh6g4gOKUJarQektJmiCu3vDzs7T31ZjmvvGLfza_jvO0Z-al1EJWt-Kl9-7iHMn0LGUKr7MFx58zm8bZKAEdGXh5FSwUo_fl4yOMmvnAMY7stDusLi64Z51H3iUZTF0N1gP8N08g6Z4wchtH3KQxzsyJalpmbSp_J33vdItaA41uPxMxR-Vzc3vy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارگارت برنان
(مجری و خبرنگار سیاسی شبکه CBS آمریکا)
: رئیس‌جمهور ایران، مسعود پزشکیان، در گفت‌وگویی با ما درباره وضعیت
دیپلماسی با آمریکا برای بازگشایی تنگه هرمز، برنامه هسته‌ای، رهبر جمهوری اسلامی و جنگ
صحبت کرد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24165" target="_blank">📅 22:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L43PnvsN3UzxzdJfNbiNFJVbWBTHiBad39QEF9upHjKlOa_BfylhgpdQmUCBgTutCyKDa437zFSYtrXrhid04DzxfuTpM34glBYjVBK8jRXWIp1djMfQqXFXiaqPrq0xMCt5FB58h9slWhtD85Kq8aEzPnehBqmpqY0iwogyYq9w8DH-OcTrEw7plE8oPqyHrN5_AHja3ynnYt-ZBc4rZrfVWPt5RD1YV2qCQYsYb8SSnVkcE88zCNhZJzjr_PPdSnYxeVLQ2TuvQzkAyn4DLjZ0ifZNIIC_XCkokt-WQom_igpb1RSytMMis6lM4aBuJQOu_mjpEyS2MFMpgL0OSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: هنگام آغاز سخنرانی بنیامین نتانیاهو در مجمع عمومی سازمان ملل، چند هیئت دیپلماتیک در اعتراض سالن را ترک کردند. بر اساس تصاویر و گزارش‌های منتشرشده، صندلی‌های هیئت‌های عربستان سعودی، ایران، سودان، تونس، ازبکستان، سریلانکا، بنگلادش، الجزایر، مالزی، مونته‌نگرو،…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24164" target="_blank">📅 21:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzSx5DrQrmW3Pe9dXWiJd7IntR5MT6-VKssj1_PLtZXxVh6R7yGFhHVfJPyZ17gV33Ee-8jM7ap90wli4d5ZhgBUdTqkGJpe7Hqrw1uPBeXdx-c9Qu9m5_jnlRbSBwH84T2yBfIrb_7JdHaAMtPgNXajpQYwxTSChyVPfrt-ghpinsQDK-JxuVURHj-vfOqCB-h6gfSY_q9Ey8V6IA5-TBr559a-_iLHC6hRajZWzf7xmKN0-x3X3WYKAhLZr1Lh30m-rUhWEDUHxjjXELAbkbS8K79ldZP1H8nbRPiVMPVf4Zs3GX-1owlAxqySgo_uco0Y-2tOwDTWu8d6LxxElg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای سوخت‌رسان بریتانیا وارد جنگ علیه یمن شده‌اند؛ به‌طوری‌که برای نخستین بار از زمان آغاز جنگ عربستان و یمن، یکی از این هواپیماها بر فراز خاک عربستان سعودی و در نزدیکی مرز یمن دیده شده است.
این هواپیمای سوخت‌رسان بریتانیا از نوع Voyager KC.2 با شماره ZZ333، صبح امروز از پایگاه آکروتیری در قبرس برخاسته
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24163" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مشاور ارشد محسن رضایی : تاکنون
هیچ پیشرفتی
در مذاکرات میان ایران و آمریکا حاصل نشده است،آمریکا با شرایط ایران برای بازگشایی تنگه هرمز
مخالفت
کرده است،در صورتی که دولت ترامپ محاصره دریایی علیه ایران را لغو نکند و تحریم های نفتی علیه ایران را کاهش ندهد،پنجره نیمه باز دیپلماسی به زودی بسته خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24162" target="_blank">📅 21:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ در تروث : رئیس‌جمهور شی و خانم پنگ به‌تازگی واشنگتن را به مقصد چین ترک کردند. این دیدار، نشستی سرشار از دوستی، اقتدار و موفقیت برای هر دو کشور چین و ایالات متحده بود. ما بار دیگر در ماه نوامبر در چین و سپس در ماه دسامبر در اجلاس گروه ۲۰ (G20) در میامیِ فلوریدا با یکدیگر دیدار خواهیم کرد. دستاوردهای بسیاری حاصل شده و خواهد شد. مشتاقانه منتظر دیدار بعدی‌مان هستم!
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24161" target="_blank">📅 20:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کنسولگری ایران در نجف : فرودگاه بین‌المللی نجف، حرم امام اول شیعیان و پایتخت آخرین امام آنها، به روی بزرگترین کشور شیعه جهان بسته است؟!
@WarRoom
😂</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24160" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مسئول آمریکایی به شبکه الجزیره: واشنگتن در موقعیت قوی قرار دارد و کنترل تنگه هرمز را در دست دارد، بنابراین عجله‌ای برای رسیدن به توافقی با ایران نداریم.
حدود 40 میلیون بشکه نفت در 48 ساعت گذشته از تنگه هرمز عبور کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24159" target="_blank">📅 20:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAlDaQ3fH4wGBp5R5MvCbSphKr-Xn84UeE0tIpAPnWk2wiXcPEAlBdG9yQusOQr7PTAcDzwXggUabBKKDLPFZLLLOZzeaAReVxKolFdAbYuZ-4OepYxDkv2tQ1YEglCGWQkz85jGL8Sh3XTA9V_fZ84JJmNJlZh1O96gFK8D14vN_8GfPr3WpDdsDmiwqWS8MqgOVACKycB-mDbwqkSktK6WcCd8EDX2GFhKAZAKhww_O2i_H-t0qWrhC4x_rRRiqfOVsuXTF3L6coJ0LoZz8MAa28Ur1ZX57FahtZw1Pj7oC1FiglZzcexozu96P52yczOGbXK1SNtyxr-Ys8A33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
تفنگداران دریایی آمریکا از یگان اعزامی تفنگداران دریایی یازدهم در حالی که روی ناو آبی‌خاکی
یواس‌اس باکسر (LHD-4)
در آب‌های منطقه‌ای در حال حرکت هستند، آموزش می‌بینند و به اجرای محاصره آمریکا علیه ایران ادامه می‌دهند.
تا ۲۵ سپتامبر، نیروهای سنتکام ۱۲۲ کشتی تجاری را برای اطمینان از رعایت کامل محاصره تغییر مسیر داده‌اند.
یعنی نسبت به رقم
۱۱۵ کشتی در ۲۳ سپتامبر، طی دو روز ۷ کشتی دیگر
تغییر مسیر داده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24158" target="_blank">📅 20:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24157">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیویورک‌پست: اشیای نورانی مشاهده‌شده در آسمان تهران ممکن است مربوط به سلاح‌های لیزری آمریکا باشند.
این رسانه با اشاره به سامانه
هلیوس (HELIOS)
، گزارش داده آمریکا از سلاح‌های لیزری برای مقابله با پهپادها و موشک‌های کروز استفاده کرده است. هلیوس یک سامانه لیزر پرانرژی نصب‌شده روی ناوهای جنگی آمریکاست که می‌تواند با متمرکز کردن پرتو، حسگرها یا خود پهپاد را از کار بیندازد. با این حال، ارتباط مستقیم اشیای نورانی دیده‌شده در تهران با هلیوس
به‌طور رسمی تأیید نشده است
.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24157" target="_blank">📅 20:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پرتاب سه موشک از کوهدشت لرستان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24156" target="_blank">📅 20:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز گفت: ایران در مورد برنامه هسته‌ای خود هیچ‌گونه امتیازی نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24155" target="_blank">📅 20:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک مقام آمریکایی به «اکسیوس»: ایران تصاویری از ماهواره‌های چینی را برای اهداف نظامی بکار برده است. واشینگتن به تهران ابلاغ کرد که ایران کنترلی بر تنگه هرمز ندارد و بنابراین حق ندارد درباره این آبراه شرط‌‌هایی بگذارد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24154" target="_blank">📅 20:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24153">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f03282bab.mp4?token=WciCKbNISSRBADB_HbXisHm3ux8CdJGMwY2ASjLs1ZvJf_QkO81im1gHhTHYzvBV5_ch8zbjCS7N6FDnomyXCnN8d95DmNLw-_otODtlxD7uhk4h1p0JuIUY1aOFY9kpeQQLHWBGvlV6Fx_iaujykwoEPt7ZC5AdlERQyPAo17d-ApPFPFJ1sC_0pqw6BhseyPMnpp2NPLAv8HgGP--u_JdBmkHO3UOUKXe8T4dfn12MCjNSDopUG-2r6i49T24Lt8kERgFNve7AeWOUHdl1BmgXY_tg-wrlDHtCT7iuXD4O9TLsoGQ-zAEXHVjfKGjCwbi6lKKVBBKvwEd07oziDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f03282bab.mp4?token=WciCKbNISSRBADB_HbXisHm3ux8CdJGMwY2ASjLs1ZvJf_QkO81im1gHhTHYzvBV5_ch8zbjCS7N6FDnomyXCnN8d95DmNLw-_otODtlxD7uhk4h1p0JuIUY1aOFY9kpeQQLHWBGvlV6Fx_iaujykwoEPt7ZC5AdlERQyPAo17d-ApPFPFJ1sC_0pqw6BhseyPMnpp2NPLAv8HgGP--u_JdBmkHO3UOUKXe8T4dfn12MCjNSDopUG-2r6i49T24Lt8kERgFNve7AeWOUHdl1BmgXY_tg-wrlDHtCT7iuXD4O9TLsoGQ-zAEXHVjfKGjCwbi6lKKVBBKvwEd07oziDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا
در مور
د جنگ با تهران با شی جین‌پینگ بحث کردید؟
ترامپ: بله.
فکر می
‌کنم قرار است درباره ایران عالی عمل کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24153" target="_blank">📅 20:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیوزمکس, ایران پیشنهاد معامله هرمز را ارائه داد: تهران می‌گوید اگر ایالات متحده تحریم‌های نفتی را لغو کند، دارایی‌های مسدود شده ایران را آزاد کند و با پایان دادن به جنگ در همه جبهه‌ها، از جمله لبنان، موافقت کند، می‌تواند ظرف چند روز تنگه هرمز را بازگشایی کرده و مذاکرات هسته‌ای را آغاز کند.
پزشکیان: آخرین پیشنهاد ما برای بازگشایی هرمز منتظر چراغ سبز ترامپ است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24152" target="_blank">📅 19:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1621b33d91.mp4?token=qCxs3X3oizDzRh3jb-w2KIj4SZl9-TuOk8tvZQ9Lct-d7m8B1LEAbsgJVcl3wK8wzMy92dcTzYL-S6-VyIsw9Edjg6In2LpFDHMocQiZAapYuqRxtWLnEnUFcT9BeWrVRlJeXvkBz-HIibNhlKN238fB3tqJmEKSoNfrGrfxCdnx2emR6iATXpDukvgSjTawAZpJoN5SqpY3vXAohzefR093je3pVTkQQLEILKDxIxgxPgO56KgVRCns7t5NvmnuYF5k9Bfkw_YnnX2SHtF0E6wgzSrZatgns1JlBnj87BhjJfdYkT8s-HSqVubobZLYTdx-8a9RAOp0jSF5H1FmvGzd1dfagZdFHkb49GutWgSmPltyns7xLkJQgyPK8Ibl9fm-KPieAojk2d4n3kqofxeeUSV_van-6NGIfk7RmhSSOTobjxey_mOxFN6jwkVaOb_VLjDqcF-b8isgubbD9BF8FeIOaLCdRPk1PwZJynZs_p2zDTS1U-FsxTzpfEar7i_Bf7nRMghGSB0LyyLHZNcFAnaIwfuPec619_ACffTprpeE1bYdfnGbp0DMJA8-MOdyelG29EDfRo9OmzIJ1Pp0KItp0XdMxMFkzE7eMQv7SQc9fezKKh4hlwhEp6vMgOiRebVOPHCxy5a746jC8u7lfB3Avlu7jRBN9043dMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1621b33d91.mp4?token=qCxs3X3oizDzRh3jb-w2KIj4SZl9-TuOk8tvZQ9Lct-d7m8B1LEAbsgJVcl3wK8wzMy92dcTzYL-S6-VyIsw9Edjg6In2LpFDHMocQiZAapYuqRxtWLnEnUFcT9BeWrVRlJeXvkBz-HIibNhlKN238fB3tqJmEKSoNfrGrfxCdnx2emR6iATXpDukvgSjTawAZpJoN5SqpY3vXAohzefR093je3pVTkQQLEILKDxIxgxPgO56KgVRCns7t5NvmnuYF5k9Bfkw_YnnX2SHtF0E6wgzSrZatgns1JlBnj87BhjJfdYkT8s-HSqVubobZLYTdx-8a9RAOp0jSF5H1FmvGzd1dfagZdFHkb49GutWgSmPltyns7xLkJQgyPK8Ibl9fm-KPieAojk2d4n3kqofxeeUSV_van-6NGIfk7RmhSSOTobjxey_mOxFN6jwkVaOb_VLjDqcF-b8isgubbD9BF8FeIOaLCdRPk1PwZJynZs_p2zDTS1U-FsxTzpfEar7i_Bf7nRMghGSB0LyyLHZNcFAnaIwfuPec619_ACffTprpeE1bYdfnGbp0DMJA8-MOdyelG29EDfRo9OmzIJ1Pp0KItp0XdMxMFkzE7eMQv7SQc9fezKKh4hlwhEp6vMgOiRebVOPHCxy5a746jC8u7lfB3Avlu7jRBN9043dMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکر کارلسون می‌گوید پس از آنکه تلاش کرد ترامپ را متقاعد کند وارد جنگ با ایران نشود، رئیس‌جمهور ترامپ به او گفت:
«بله، حق با توست؛ اما در نهایت همه ما می‌میریم، پس اهمیتی ندارد.»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24151" target="_blank">📅 19:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf75471ddf.mp4?token=PGNweNsU3fgCfSH6f8i-zSZ2OHnS7WoUYpi8HY1SE73dTp7LCQCiAAdtd-m4HzhCb45RJ6uK3CWGY1i4UOV_j4FGIQMWCKRYsKf3rbqOrUco3nun50XXDVGryXpUWWTlCHnNcDiObHykb0xMxORrG24envdH2meXwsQZuMthQLOL7dnWUjlpIJLoJZXSLK6_yTceWM1_eE0nAuWNZLnjaEHFSi_bQwi3GucFMlh_nNNJYudHYqaS4jw48eBPX5Hh4nkMk2eAmhcIlCuQbfz1aGRUZRNl5P49Fb8gd9a1AfZ1KLcM77fvOhMEOJQhYMnc1oijJFgbcZt4k9vkue4x3XUF0mvVikks7E7F2TNsUngmiKnLJoWGZ86UJDuptSdeELv-EwQj13qxHf9sr44TDHXQgwjzO5aq27VCU8K96PEv-CEFovFrPqWLeeiMUVrDi1aN-qDDcmnke9jfkF3BZ52UIzmiXELF3TPG-59GGaJ0yE5JA1cSwPmjaSV-kJq1O_l3FILjeufkdcMC2BJUUtcXjIOyAiIyPgU5CqkvRqITygaiFruU0XPFe8N3aHXXMnJl9JovjduGcslYryZ_7BNRUzFb8Mv5H8yaVEjw0ihhAQIsWF5lLBBqPUEwNbGgevGM93NYa2ZwdUajgAdEuXwy5hw_qdkSRzzGamsOleg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf75471ddf.mp4?token=PGNweNsU3fgCfSH6f8i-zSZ2OHnS7WoUYpi8HY1SE73dTp7LCQCiAAdtd-m4HzhCb45RJ6uK3CWGY1i4UOV_j4FGIQMWCKRYsKf3rbqOrUco3nun50XXDVGryXpUWWTlCHnNcDiObHykb0xMxORrG24envdH2meXwsQZuMthQLOL7dnWUjlpIJLoJZXSLK6_yTceWM1_eE0nAuWNZLnjaEHFSi_bQwi3GucFMlh_nNNJYudHYqaS4jw48eBPX5Hh4nkMk2eAmhcIlCuQbfz1aGRUZRNl5P49Fb8gd9a1AfZ1KLcM77fvOhMEOJQhYMnc1oijJFgbcZt4k9vkue4x3XUF0mvVikks7E7F2TNsUngmiKnLJoWGZ86UJDuptSdeELv-EwQj13qxHf9sr44TDHXQgwjzO5aq27VCU8K96PEv-CEFovFrPqWLeeiMUVrDi1aN-qDDcmnke9jfkF3BZ52UIzmiXELF3TPG-59GGaJ0yE5JA1cSwPmjaSV-kJq1O_l3FILjeufkdcMC2BJUUtcXjIOyAiIyPgU5CqkvRqITygaiFruU0XPFe8N3aHXXMnJl9JovjduGcslYryZ_7BNRUzFb8Mv5H8yaVEjw0ihhAQIsWF5lLBBqPUEwNbGgevGM93NYa2ZwdUajgAdEuXwy5hw_qdkSRzzGamsOleg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ پدر جاویدنام ⁧
#عرفان_عبدی_پور
⁩ به اراجیف دیروز پزشکیان در فاکس‌نیوز
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24150" target="_blank">📅 19:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24149">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیوید پردو سفیر آمریکا در چین:
ترامپ دیروز به شی جین‌پینگ صراحتاً گفت هرگونه کمک چین به ایران، چه اطلاعات باشد و چه قطعات یا تجهیزات نظامی، کاملاً غیرقابل‌قبول است,
ترامپ مواضع و منافع آمریکا درباره ایران را برای چین کاملاً روشن کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24149" target="_blank">📅 19:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627df24333.mp4?token=g1OmzbcVvefawMk2IXHGHbGFMTBnlQTV0U2psnEWZ8vVpv7YTYKqAr24suLe57_nTR8f3WSXDArerR6m8-wjhkrzCq46N4qvnet3s5Wsl8CnWcLNBm5U7S9O7kgGi7uN0zjDHriRqCCsAbNWxCbzVo9yO5QF1IXDlhvLT6z9TOir-euqaMM3VK6f-pNmYsKXxe0XHBxPUlp-H99t6NWmFX58SdLTCgsun7ynEQp46FkFP3yv4NRxHppUHA3a324zZWugF7fxcVBku_X7qCvDF2lXCe96nIn7OQpzhHGHYXDwrRi-ODdqTZ_zznXtTO8fPjA1pcAWznUDIONNF-kFDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627df24333.mp4?token=g1OmzbcVvefawMk2IXHGHbGFMTBnlQTV0U2psnEWZ8vVpv7YTYKqAr24suLe57_nTR8f3WSXDArerR6m8-wjhkrzCq46N4qvnet3s5Wsl8CnWcLNBm5U7S9O7kgGi7uN0zjDHriRqCCsAbNWxCbzVo9yO5QF1IXDlhvLT6z9TOir-euqaMM3VK6f-pNmYsKXxe0XHBxPUlp-H99t6NWmFX58SdLTCgsun7ynEQp46FkFP3yv4NRxHppUHA3a324zZWugF7fxcVBku_X7qCvDF2lXCe96nIn7OQpzhHGHYXDwrRi-ODdqTZ_zznXtTO8fPjA1pcAWznUDIONNF-kFDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش تحرکات ترابری آمریکا در ارتباط با خاورمیانه،د
ر۲۴و۲۵
سپتامبر(دیروز و امروز)
، فعالیت هواپیماهای ترابری و پشتیبانی آمریکا از جمله
C-17، C-5M، C-130 و KC-135
در ارتباط با منطقه خاورمیانه مورد توجه قرار گرفته است… یه خبرایی داره میشه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24148" target="_blank">📅 18:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گارد ملی آمریکا اعلام کرده که در
۲۲ و ۲۳ سپتامبر
، هواپیماهای
C-130H3 هرکولس
از گردان ۱۶۶ ترابری هوایی دلاور برای پشتیبانی از عملیات سنتکام در خاورمیانه اعزام شده‌اند و حدود ۱۰۰ نفر از نیروها نیز همراه آنها مستقر شده‌اند.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24147" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کارشناس نظامی صداوسیما:
در روز های اخیر پرواز هواپیماهای جاسوسی و شناسایی آمریکایی اطراف ایران بسیار افزایش پیدا کرده است که نشان دهنده یک حمله قریب‌الوقوع احتمالی به ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24146" target="_blank">📅 18:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2fc3da78.mp4?token=lY9LEOWNicC1LumM6D_YOCrpF_ErCCZoD96PH7fCNAHgaGDXAgN2jsQ5axkWzjKZnVaSCrt8PyYisal-gKHeQurOz01D3egwgw9Fvz2WgZTMxzYSXHw1Om5OLbm1FOE0wt66JfEg2_UH6otdTOlG36G2X2ipA2tGYIiVScXe6Dw0HBeyjdX4RKST3I3KuzLbLmRKDaOkZ4qVAiRdau3hPYO1rNbKJvsQ_b7C6RWaMpUV6mM2oIUQcfo2DT7uezVRiaCSm1u9FTBXlBAbl140w6LvN6Nd02oYn4BGqi-cZ4Hs3uJTY3HhQORZzt5QJ2W_PhZgpS49r5Iy1c_bLmAqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2fc3da78.mp4?token=lY9LEOWNicC1LumM6D_YOCrpF_ErCCZoD96PH7fCNAHgaGDXAgN2jsQ5axkWzjKZnVaSCrt8PyYisal-gKHeQurOz01D3egwgw9Fvz2WgZTMxzYSXHw1Om5OLbm1FOE0wt66JfEg2_UH6otdTOlG36G2X2ipA2tGYIiVScXe6Dw0HBeyjdX4RKST3I3KuzLbLmRKDaOkZ4qVAiRdau3hPYO1rNbKJvsQ_b7C6RWaMpUV6mM2oIUQcfo2DT7uezVRiaCSm1u9FTBXlBAbl140w6LvN6Nd02oYn4BGqi-cZ4Hs3uJTY3HhQORZzt5QJ2W_PhZgpS49r5Iy1c_bLmAqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای مهیب و ستون دود هم اکنون بهبهان
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24145" target="_blank">📅 18:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24144">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFfQ29VAC2DFDWNXz24vkpdhg4PkkQx6OZPSCnQiYXHlb4T9LVCbiyfqyxQloHV0DE7nN90bDMNZ3XRUu3TvE7pl5RB5ThLNECueN2tpbLx01AlB3WM7Q97zlSoMz71IMk_WcDPXFI2rp4JHg5WheEG4IUsk-bJPHvCPVVR7NkqGgXzhxFcEj7dIqE1ojpRuotJdRu99_NQfvHVQ1qrdWH8W81KBMJTCi0nVff29FoRGc-JUJONsDANTjdixIGm2uKxTH4L_3TFKaFzZ8EQvjY3ixJyiC2wYphAnRY0KGu-_UFEB6CyxI8PNwqg89Lv6pRtBQU1EyS7I17_N7XBkRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین نام رسمی جنگنده پنهانکار J-35A را اعلام کرد:
رسانه دولتی چین، CCTV، برای نخستین‌بار این جنگنده نسل پنجم را با نام
یون‌لونگ (Yunlong؛ اژدهای ابری)
معرفی کرد. در همین برنامه نام جنگنده‌های اصلی نیروی هوایی چین نیز اعلام شد:
J-10 — منگ‌لونگ (Menglong؛ اژدهای نیرومند)، J-11 — یینگ‌لونگ (Yinglong؛ اژدهای بالدار)، J-16 — چیان‌لونگ (Qianlong؛ اژدهای پنهان)، J-20 — وی‌لونگ (Weilong؛ اژدهای باابهت)، J-35A — یون‌لونگ (Yunlong؛ اژدهای ابری).
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24144" target="_blank">📅 18:07 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
