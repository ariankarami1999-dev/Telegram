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
<img src="https://cdn4.telesco.pe/file/lCSqOMvsVsCvAu3c-wLIdCZheCyat_hGoEcELgAL5PNUn0iOjSnkLfmoNSPFS3it0kVSjIJTWBx9EBwFLk9VTSG9wZmrFyw9VkOQgv_XKMjS5f48X2Lu_P0Br9HT9JEFulWHBed2xD4_UmrVPRKKgzI65APtOKMMbw3CbynbH1Wg6P-y8wPuUqVRhOIs4AElA0BcO1MZ1ydRgQnHjuTnJ-7i85o4xq0jVy7ayh9iOVZy9BQlHmRbJYyod_fhM7Q2_o9x5zhsNz0_E7j_UQKt13UNRmUz6IDScG9B3VO1fO9U-W9ZkkuXsGraVNdmnUfkmyIO5y9MiyZ4V9WgoCNCew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.5K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-3072">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپشتیبانی جمینو</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5_acnC36RxYeP70kzt4FydnsZF5i1IFdMqsDX1nHQhK5nUid5aOUdFcJH-eG3XtZahLO0ujD3Hcwt4YRqztH1KTH1kt_2pzLziaT76mapPnn3gqFKExPIma2hQt6Y_GppXNRCRF-paEZutKYhcJT6njQlDx-0Ildj5KYD4qw150d52pRv_Ndw_flKTRtaFjMqWZzX6j_jPF6cnjtSZ2TO_sW2m3vmdPTOKhB1v6cWFlHCmFLlp6g7YiQSGsls96u9KTj5bulG33izpOcGbMg26irWCGC_GAnV-IbFbvv7k1U5nCuMEtTYkFaik0WkNXC2G6HR2rGH_jS0WC9_jkeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اکانت های پریمیوم با بهترین قیمت و پشتیبانی در
فروشگاه جمینو
🪐
🤖
اشتراک شخصی
18 ماهه
جمینای
Google AI Pro
،
به مدت محدود فقط
980
هزار تومان با کد تخفیف
Gemini18
💎
Gemini Pro
دسترسی به آخرین مدل زبانی گوگل
🍌
NanoBanana
تولید و ادیت عکس با کیفیت
❤️
NoteBookLM
آموزش و یادگیری و ابزار تولید پادکست
📹
Veo
تولید ویدیوهای با کیفیت
⚽️
Flow
ابزار تولید تصویر و ادیت
🖥
AntiGravity
کد نویسی با مدل های کلاد و گوگل
‎
⚡️
تحویل آنی، فعال‌سازی مطمئن
کد تخفیف ویژه
400,000
تومانی قابل استفاده برای Gemini و ChatGPT پلاس پیش ساخته، برای ده نفر اول: Aghapour400Pro
👀
محصولات دیگر با بهترین قیمت از جمله :
انواع پلن های
ChatGPT Plus
🤖
اختصاصی و اشتراکی از
890
هزار تومان
💥
Claude
🎧
Spotify
📱
Capcut
👨‍🎨
Figma
❤️
Canva
🦜
Doulingo
📒
Notion
📱
Mimo
💻
Windows
‏
🛍
خرید از بات جمینو
🔙
@mygeminobot
‌‏
🌐
سایت + درگاه و اینماد
🔙
mygemino.ir
‌‏
💬
پشتیبانی جمینو
🔙
@mygemino
‎</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/iaghapour/3072" target="_blank">📅 21:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/iaghapour/3071" target="_blank">📅 20:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7nVAiXOV9HLRIhFlQYFhtYcM1vCNaFtwfclEBcVbkm6ZwoylSb-vFy729hsEEAZIv72a8_tzXdcvtXBA4KpNHrmiDyfZfox7MZ3zbhh8KSKKdYNzXa3KEnhA4dnu3bLBnMDRwV35W8OpDWoWewW7EZQQazWi_oufTlDVDSxOCSzZAdZphpsqDJaP85vzuKsiW4YvB1eqjEsf0W9uZu6_RHxxbsE1SBYruzASbT9qgCYBrCWvYAeqYPWMytxcjyVJ9CdKl2DNyV9mtcylGiAt0CnGCTPpq6uXOegVdly_h5_NqpYH0QwkMp5OAlUNmaPpgsRxzUwz4UOeK_LfQ_KTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKxHV07TKrCXBjVLDHhCmMylU_6JNeW3KjXqkpmH-dtiBOtWNIGnujHPjkgqPef8xFgXeLGt5aqOu30xOIAAT0JqL6_l8WUTMYbpULVZfzuCmOEQ6bg1xKLaL0cGotqvQCa48Xpkmana1jXmS6Ybd5t_uq296EvgYQZQsKUnJO-8bHBLu298Q-Fy8Ylu9-xBUmQEgwcEr2FEMKf9HFvfa5VUpwm-3rZ0Luqy-by4hhUu1uywJjuKsZS-PW56kvGe3mN3eT0xe4WcAWsZIvxHOOYgPMearhDoOEzfCIIH2nToHwvuV0qCFtqsy1s1L6qrIAAOkNZdZp21hiTMtBB8VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/iaghapour/3069" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3068">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنوین سلف | Novin Self(📝Řęžā🔊)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX3nhQRxjpr5rgtrsBVgBLA8Gz97WudmN70sC7P9S0qtOARYis5uXG9nMFJLdkbDOs9qamXyZrsf2CTDxehd7v5b7xQlb4GZiDu1NRfbaUhSELGAETqJm-TOKiwTPcfefIxsugbEp7n6BLYw8AOd0YLnWqPo_GoiiSxxQEnYSUVwoEKt00Onkm4Js2jvYXixNJfoRs_rWnBV6vLR9vZNETvgsMu56R7Ucz7N-xsdxzkFGU1yk3E_1mRq_KMKJGKWEzJNGLZbjWmkoBmXTPXTCF1zBLExMqD3rdiffoRCqc8oYRtP5dzHy_IIkjduuXltyKRceRe72-9t3dJfSe5P6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
● همه چیز برای تلگرام، یک‌جا
🙂
🤖
سلف  وتبچی امن (مدیریت هوشمند اکانت)
⭐️
خرید Telegram Stars
💲
خرید Telegram Premium
🙂
گیفت و خدمات تلگرامی
📱
شماره مجازی کشورهای مختلف
💬
ممبر، فالوور، ویو و خدمات مجازی
..
📱
🙂
ثبت و انجام آنی سفارشات با پایین ترین قیمت
‼️
شروع سفارش از ربات
👇
🙂
@Novinselfbot</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/iaghapour/3068" target="_blank">📅 22:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3067">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVq0w7Fi1yrKewGVs5jjtMymwHmFUSMv5jKJuFYGm1wwLFC_ajPqq77VOUtuoEUk32fl4-tJqJqldnOwMbhcUk3eIwjPNBQw49yw03hFGwFuKLQkPOYxQsVst4Xy-tZSg53ewoZVZG_5GNtfKx4_YC7q7lKN7oTHIfN9KvsJ3NyI8rYeasBAsDVEJZLrGfbU3Tl1sGI3L2lHIIRtm5PER_Ytw8jmMUsOhdKM6mYJ1GqtHMKH4HM_cYXqp4QcGhjoCAoFoqQv1w3a8v5CpfRnecvRYrKij9TMk7-XHyigZ7eEiVoKtySOhNsCGx39BROuCgFc90r60UK0p0HhtZhjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون کامپیوتر فیلترشکن بساز! (مدیریت سرور با گوشی - اندروید و آیفون)
🔹
خیلی از شما درخواست کرده بودید که آموزش کار با سرور مجازی رو برای کسانی که کامپیوتر یا لپ‌تاپ ندارن بسازم. تو این ویدیو قراره یاد بگیریم چطوری فقط با استفاده از گوشی موبایل (چه اندروید و چه آیفون) به سرورمون متصل بشیم و صفر تا صد کارها رو انجام بدیم.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#گوشی
#سرور
#اندروید
#آیفون
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
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/iaghapour/3067" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3066">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=L7Oi1h03PfpYasw-cpOjYT7oWqRFm65Ss3iursPzpcKm6xeNotnHOxLoWz4UKLhMjuNF9Tt5_uGOdJDS-jZD7TXDb2eDTPszNRxZ7WZpaX5bdga21_guh91d2Pa2JHtzOWcprBe6NwtSgOpeJGJBNJEZDf2HqxId-EEhfjVrWxfD1p-J4rMxEMb7bm_vMlGlkt0hwbyvD28x0CK7NTs9szH8HWM400upfMlpFPm1nK73pFQ4EGN6P0OfiyZIMi97ZbZuHZ7OX7C2qzGcO9OUHSuzBb_OJ6YhXt4vjE_8Qr01E383qHDdWUo0s12_d9A5mradI6J4I_7Nz47HYsfM3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=L7Oi1h03PfpYasw-cpOjYT7oWqRFm65Ss3iursPzpcKm6xeNotnHOxLoWz4UKLhMjuNF9Tt5_uGOdJDS-jZD7TXDb2eDTPszNRxZ7WZpaX5bdga21_guh91d2Pa2JHtzOWcprBe6NwtSgOpeJGJBNJEZDf2HqxId-EEhfjVrWxfD1p-J4rMxEMb7bm_vMlGlkt0hwbyvD28x0CK7NTs9szH8HWM400upfMlpFPm1nK73pFQ4EGN6P0OfiyZIMi97ZbZuHZ7OX7C2qzGcO9OUHSuzBb_OJ6YhXt4vjE_8Qr01E383qHDdWUo0s12_d9A5mradI6J4I_7Nz47HYsfM3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/iaghapour/3066" target="_blank">📅 16:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3065">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObGajQMAuEmyr-diNDsfYGPmUmL2NJQPaIc-TaSqcqVpwFnEFTX4I4iEgtmBjt6F52G8D85bsp2VqvI_DESVzlPgkS2hVC7AT9ONrIjWplL19W5mrIHXJsXlGyiZ7kkiMzmWc92A3xiw4oOSL9LkQmsxhR3m4uChGVpaFHxq8F-Lig8r0Yf_KNE5o-QDSX7m8nGcnbXvw2RVek3d3TPraHBUNELpO5Gc3ffoNuwo7Aw78jgcrSaiEUzG2Lpg2tYooA3vwG8LbQ3vF1Y8dVW6z919GagIldhrAeuW2St8FNDJ5ZOEnL6E-uxVqivIVeY7SZFI3S73mUolTPdsmO8E9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی VMTun؛ تانل کامل ترافیک ویندوز از طریق v2rayN و Xray
یک ابزار کم‌حجم برای ویندوز که پروکسی لوکال v2rayN/Xray را درست مانند WireGuard یا OpenVPN به تانل واقعی در سطح کل سیستم تبدیل می‌کند تا تمام نرم‌افزارها (حتی اپ‌های استور مایکروسافت و UWP) بدون نشت از آن رد شوند.
🔹
تانلینگ سراسری با Wintun و sing-box:
هدایت خودکار تمام ترافیک ویندوز از طریق مسیر پیش‌فرض و فیلترهای WFP به پورت ۱۰۸۰۸ v2rayN بدون نیاز به تنظیم پروکسی در برنامه‌ها.
🔸
جلوگیری از نشت اطلاعات:
بررسی و رفع نشت DNS، بستن نشت روت‌های IPv6، و مقایسه تایم‌زون و ریجن سیستم با سرور خروجی.
🔹
قابلیت Pro Connect:
فعال‌سازی هم‌زمان کیل‌سوئیچ فایروال ویندوز، بستن موقت IPv6 کارت‌های شبکه و بلاک کردن QUIC جهت رفع اختلال.
🔹
پایداری و بازگردانی خودکار:
برگشت امن تمامی تنظیمات شبکه پس از دیسکانکت یا کراش احتمالی (همراه با اسکریپت
Repair-Network.cmd
).
🔗
گیت‌هاب پروژه
🔻
این پروژه متن‌باز است، اما کدهای آن توسط ما بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده سورس‌کدها را بررسی کنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/iaghapour/3065" target="_blank">📅 15:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnOxE0KLZ1DQr9co-pbAB5mh07iqSga1zswIhD7-r80pn4njz8fJFJnuBqnwyMVsAAJpEZo98BgcaPDQwo4EtbxvR-2Ag8ymbpuVt68cUE88MV_8hzDUHOQ-HKbLlWYOGJ37RXdVoE0uuZSilcdh7EQrpYIszixmBm3_Zdb6vn3ZI0ZhFLv5hHi84-MkIzX4OMY779l1hM5yDGYY23vtVuJsVXpfeK2TS-p4rdyjqpG_wEyn7MuSs4puvXM5ogmL-OHzIOCaif0CcS_8Z4H6xGS8MW-lZxssVRauw3Kg2g_I0AWL4w69_8xbBMxIh3VEUONAP1boHskPV97JQ-6pmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/iaghapour/3063" target="_blank">📅 20:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltd68asjZDjT0kF4YKH2pJMm-nD9-xgSbth2dcyWlEwRFmgenpE3N60KBagoU-Vkazjqoc2pcMkETT4MWGUxDEK-vlfjobpKAsQl-GgeyL1_Dgm_DdK2yIf4CLpbidXweAL5EiAbSU15j7sSuGpgKKa9Ruj3t_-lOJt0xNlxkwF_tbbkfuBTskuuVdcJKGgvZPNX0Jmw4lJo8VdlnObnkCNrBZGagbomHHldSBPAzAu-yNqurwHclmeHOHMxd-JqnDG_n7o-ojMfSFjq6f5aAOPLOkpnRF51hug7BPtxMyTTGeVm_Ns2xGJnm0b2Qczvg_uT3nPaom5Xl_o2vjEYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت نقشه راه جامع دسترسی به اینترنت آزاد
🔹
خیلی از دوستان جدیدی که به جمع ما اضافه میشن، همیشه می‌پرسن:
"از کجا باید شروع کنم؟"
و پیدا کردن آموزش مناسب بین ده‌ها ویدیوی یوتیوب کار سختیه.
ما حدود ۲ سال پیش یک صفحه اختصاصی برای حل این مشکل ساختیم، اما امروز این صفحه
یک آپدیت اساسی
دریافت کرد! هم ظاهر سایت کاملاً مدرن و مخصوص موبایل طراحی شده و هم تمام لینک‌ها و آموزش‌های جدید بهش اضافه شدن.
🎯
ویژگی‌های این صفحه:
🔸
دسته‌بندی ۶ گانه:
(از نقطه شروع تا ترفندها و تانل‌ها)
🔹
سطح‌بندی شده:
(مبتدی، متوسط، پیشرفته)
🔸
توضیحات کوتاه:
(توضیح اینکه هر آموزش به چه دردی می‌خوره)
💡
کاربران جدید:
این صفحه بهترین نقطه شروع شماست؛ از بخش اول شروع کنید و قدم به قدم پیش برید.
💡
کاربران قدیمی:
حتماً یه سر به صفحه بزنید، آموزش‌های تخصصی و ابزارهای جدیدی اضافه شده که احتمالاً ندیدید!
🔗
لینک صفحه راهنمای قدم به قدم
🔗
سورس کدهای صفحه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/iaghapour/3062" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3060">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtcfnswMDrKlFUDJ-21EMdFm3upPcr-qMKeoIxzLxCkxU_26pETWc289YylPxK-7r35RitMQwYzg4LEphmS7IZF_KgDVqYQpa0s7sMCM5uVjwv1VMfpf1g08qkvDotv50dUAreE4NIhpTzk4nhC-vgOlp1DMbBWbHiTLe1Opve-jm_DFtHFvSMrl5CQcCxAqAzwYuq02_bFRggED8J8Scq13_qs0d9kNUUmmc2m1L0xjz0U4kqyoSJy4CWorqiJpDPFmspm38n1sxqRIVoqbTc_XLzlvAEX3wCfs6LPBjOAx68XhexC85zxjCaHJtIOTHVlzdHgfLnjec5AlxWHSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
بروزرسانی مهم: لیست جامع آموزش‌ها و ابزارها آپدیت شد!
اگر اخیراً به کانال اضافه شدید یا احساس می‌کنید حجم مطالب بالاست و سردرگم شدید، این پیام مخصوص شماست.
لیست راهنمای کانال با اضافه شدن آموزش‌های جدید و متدهای کاربردی به‌روز شد. این فهرست یک مسیر دسته‌بندی‌شده از تمام ابزارها، ترفندها و آموزش‌های تخصصی است.
🧭
پیشنهاد ویژه به افراد مبتدی و اعضای تازه‌وارد:
حتماً با
«بخش اول»
آغاز کنید تا قبل از هر اقدام فنی، مفاهیم پایه و نقشه راه را یاد بگیرید.
📌
لیست کامل در بالای کانال پین شده است؛
پیشنهاد می‌کنیم آن را ذخیره کنید تا در مواقع اختلال اینترنت همیشه در دسترستان باشد.
🔗
برای مشاهده لیست اینجا کلیک کنید
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/iaghapour/3060" target="_blank">📅 14:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3058">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKO6S3qnt4b4GfSx4HDhMcLcYDsJpy2ex-xg-VG4lkGhVvZJnIdEju5k875ObCkG_Jo9DzcMcVuj52JENPmCbhPNpuOCbJfJsJPtBgd5G8JRK3hkEVpQrcgiBuY1Ad-EVoNbGQ4bkH-fRCH7PiNoMJXiifvFqHs5YfnMCUR3FSM3mvqiPZreDgD_WEXklld2Q8YUhSCeDjtlTzFXqZUE1_TEd59rX7Bs7XPcG8go2q9pjWrKWhwTok1XJYVMY8HU7CrB3Rj8QZkBnJIbzUxe-y70c4m1XAHJXtFZeeRqxNoU-JbllRDKfrJfasATaVEs78QdFfCpsglsvAAj8pFmLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
رفقا یه نکته خیلی مهم درباره کامنت‌های یوتیوب، مخصوصاً وقتایی که قرعه‌کشی یا چالشی داریم:
🔹
خیلی وقتا پیش میاد که شما کامنت می‌ذارید، ولی یوتیوب اصلاً اون رو توی بخش عمومی نشون نمیده و مستقیم می‌فرستدش تو قسمت «بررسی دستی» (Held for review). حالا علتش چیه؟
۱.
کامنت گذاشتن در ثانیه‌های اول:
تا ویدیو پلی میشه سریع کامنت نذارید. یوتیوب به این حرکت شک می‌کنه و فکر می‌کنه ربات هستید. بذارید حداقل دو سه دقیقه از ویدیو بگذره و بعد نظرتون رو بنویسید.
۲.
کامنت‌های بی‌محتوا و تک‌کلمه‌ای:
متن‌هایی که شبیه اسپم هستن سریع فیلتر میشن. مثلاً طرف فقط نوشته «کامنت» یا یه ایموجی خالی و چند تا حرف بی‌معنی فرستاده. سعی کنید یه جمله معنادار یا نظرتون درباره ویدیو رو بنویسید.
راستش منم سیستمم طوری نیست که مدام بخش تایید دستی رو چک کنم و خیلی وقتا یادم میره؛ همین باعث میشه پیام‌هاتون یا خیلی دیر تایید بشه یا اصلاً به قرعه‌کشی نرسه. پس حتماً این دو تا مورد رو رعایت کنید. دم همه‌تون گرم!
👌🏻</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/iaghapour/3058" target="_blank">📅 20:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3057">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC4AdRa4ApomXtOpzMa9EttZCUA__FMoyjnf8vMJrsvmN7Zv9QF2xr_FrKcb3szTqsGTOKxpHfNFIcrW4DDrEgYVNCZI32oPzeO4UIdb16EqqI_HdPUcd6SgqwIpqSigTBTl_8yel41bDLw99pU_2k_dzSoDD7-_uNzkPIF3TJiQb4g3IB6Qxvxy7NS4PwjFI0E1iXNeflsqZfPA3iHU5hyjjLGykYYaH1cWTie8cdmoXiUlS3BQ7GmZD3zF04hVobi6vEL6iPjEJSQSGfC1NpFFQkR7g4Dc2oiceNGok8XUQvSyrx_TuCwNKolKnIxpAjlyI0ilW6Pf-vRHWagScQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/iaghapour/3057" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls-McviCDTmPmNPF4bagp5R1EVuRYS1YBDLq2PHR4xJC4zrQ8Be2QGCoAk5ybeq5FQXa2ve2pgTNAf7PwOl8iZ8P0Q59c3Pg6btpY3SMW5YNFKCWFIFpTtIDn0AIh420LWg6NbmWFfQuXYxyV9AVRQb838NV7yAGXPJdhaDyqsih40y2dQJajqBKMGd1X8MU9yUlgmD_vZt-v6PADkJjIJLshoMUQZ_D1FAoRykG16YrTAFkjF54q0l4-6GcbnkhcS-anEPSeJ4rw2U3pCDwZjiDs_NCbMSPv0NTrYA9Df_DUoBXBYcJ67PY9Yyi7vhktRamtLy3wdDm4_A9LGOjhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/iaghapour/3055" target="_blank">📅 16:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3052">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msmAIORKCZMCnQGepO6AHsYGy_QXZd7D--EH6xT250p6zQooVgBrfi1g20zeIMUk7WC3kw1oH34p5VsLkEbE2EAyV7J585QpStoRnDmxlmS5xOIdKAKKkkguN61xQD-V146Bo3PpVEjrgG7A1RDja-QvQXwz-7br6j0dp7FQH8ClcmmSBLPfGWoP2IGK_C0xHiGb2IfST6rQX8UpYzhUI59mzYgU0ao4glmSNXBnk9XaDLQR_cxoZFM6CYmzOQEpB3oZzlte6s6fGr6Cj1aud4pPxrsFP5eWp23c4AaHzw60XaFs0s6DPZZfC_nbE_7SAomynOaGT34frWlj-ICAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی جعبه‌ابزار کاربردی مدیران سرور و دواپس
یک ابزار تحت وب و رایگان که تمام کانفیگ‌های کاربردی لینوکس را به‌صورت بهینه و استاندارد تولید می‌کند:
🔹
ستاپ اولیه سرور:
تولید اسکریپت شل برای امن‌سازی SSH، فعال‌سازی BBRv1/v3، فایروال، Fail2ban و نصب داکر.
🔸
تیونینگ TCP/IP و کرنل:
تنظیم بهینه
sysctl.conf
متناسب با رم و پهنای باند سرور، کاهش پکت‌لاس و بافربلوت.
🔹
کانفیگ Nginx:
ساخت پروکسی معکوس با TLS 1.3، پروتکل HTTP/3، سوکت و هدرهای امنیتی.
🔹
فایروال و روتینگ:
ساب‌نت ماشین، پورت فورواردینگ (NAT)، رفع تداخل داکر و خروجی مستقیم برای iptables و nftables.
🌐
آدرس وب‌سایت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/iaghapour/3052" target="_blank">📅 19:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjpG7SqBo2Lohhd6hwOnePmk5pBazY_GDqPdJED_NGYoch7AO7XxG13iEEUWl-t3mrO3XAySYYatLcX9eviVwgOr96rttxxTiFkB5XxFr8nKPgFhLQG82nqcOgfdBLhQ81We0TZs3SlwdwaBsfYRIr5njpOPpOeNd93VaUk-TUxm0_Yc_-hyShvR6nLVZhsFPOWz2BjJHoQ__qHl8nJuyo7WKREVrJrh1sS-vd7qbxTD82DE3USfSDZBMVZFdw600X3U5sm3j5c-RgalZFbeIKznALy_0LD12zSKpDxWf88EPBCwI-Mj1ilbgftRPTRTjePmWN2NB0JHN_kXCB7UBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWbb_NpkL560RXngUkCexyxUHyMJbcDMnS7EO4UDi3sc7Pn-3ohlqlzryorRn3ch-2DvredQC-65QCnGUyhReORsrh-bvGS_1eXMCe0ClVpuAEdP4v9ErJZ3H76FA5Yr2IXEFiPoCVKyYhX69HQ-e5mJUfi9ygknijQwmyU3A2xQrEdh3O8PfckDkiCsYi1fnjUpcm3OCJ6mQ6_rDDjVHjrLtOz2cc6Lcg364pXZ52_aVQU05mp1jjDl1GtnVSftnoFOZVybVHdT7_Mw2FyKJuIo6OtJ8CCEwhq-J_LcrwXJc_WHgV3HOr6IXmDMykdfTqA8C1m77JIRvvDrgkbFtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL8n2e_yBEWleNRKbNvpTpxrm2hEA0ynsMp-JXTD5z3mS2DSkyZ8IaqJXqbqQFU0pziziakclVqUknNwaFIteoslefTB_gaggFSMLadFYVkURdusEoSHveVeEkXDKCiflvx6kc_B5myYnWAHl3CUz9LjnSQgnuciPcSPnSXV8qrwmO6K-CfKKHrswknVQhCBzt3XmkaP_UHNVYIpKIlmYwQXx5j-NOwsnqEDZCLEF049ufavFsCoot77WEev7gFtXu9AuDbbx7EOa-aMiNroFdHCvbAOudJG-Acfj519yGB62RZZDOH3t70SMXQs4sR8Wgkx6jgH-M1glQEaUUEwhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/iaghapour/3048" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=Q4CqKsSe3k0R-Bm_eSt3B5XxuzAJsUsbjpP1nc_KdVqJXBSUJQuMjdN9Bc9AYy3T992clUAOuY1jGtM8eVtJ4hjkpRDJU3Inww7W9fRA2CS0WvlEbAN6mzy9YRqV_3mhEiu616W4BXwlsJxl489ivZrZB3xoq1owYDqHUfGaKacfBF3rXkDnAZ8BlpuD9A7j8AzzgNrCQy34xzkU4e8DqOerUzIVVR8qhbOUqj5pWSy8rKRcTpU3_3IUjLPdChLVMT924tnEThMt0mEyDdia8P-fzsYHRS2bgsL_Dul72euWpYlC5TLDPfozDlIhUBMhg3xM0lMzOM9mBbbbAF-S-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=Q4CqKsSe3k0R-Bm_eSt3B5XxuzAJsUsbjpP1nc_KdVqJXBSUJQuMjdN9Bc9AYy3T992clUAOuY1jGtM8eVtJ4hjkpRDJU3Inww7W9fRA2CS0WvlEbAN6mzy9YRqV_3mhEiu616W4BXwlsJxl489ivZrZB3xoq1owYDqHUfGaKacfBF3rXkDnAZ8BlpuD9A7j8AzzgNrCQy34xzkU4e8DqOerUzIVVR8qhbOUqj5pWSy8rKRcTpU3_3IUjLPdChLVMT924tnEThMt0mEyDdia8P-fzsYHRS2bgsL_Dul72euWpYlC5TLDPfozDlIhUBMhg3xM0lMzOM9mBbbbAF-S-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/3045" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5br0uOQ4pZsLOM_R0ieXJwylcP3zY_gYxN0Od4Lw8AQ2_VHvnDtiyEDz5zHFPBYOzYdabqFvwNh2siRZ56MAOsRNzSdYBxPNiZhrlbs_FY-z8ofQWgUpvt_DuXLtRrNGga4bmd6nC6vWMGcGwYToMsLHlAi5XFtR8P8ReaDgqar9cHtYyveKIE-zv_VKGIRyBZmVHJ8Q-GQ6-YXALWuZiG3vMs19cDhh61l2PC-T-US-c6UJ7lURzSo3MZ5uafOSluU63SnlqVAiRLNe1RIYxKvXB-h3S-7twDRraryI6zemMSZp2GifTQGp4PmXSKBtzHtDohYz_qRRY_opYQJ0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/3044" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4PDzKhUmoqDR9YodJDGLWXZjFwL1CZkGSc6-gkaKEwAm4PCqY9ktG27gacjB0jM1nI7Z28eZpXqqU4U9xoLYEqm2Ffb-12VQFttUSfrDZHjpWemmx46jto7gjKTIFH6UdKKnHYPtBW4oP4-1nJ_VMg67KH5mQ0HeWrcrTXVZPlx29yV58u8-NUJ9yvCwCBoznqM1S6-imaj4nkwuZvzqeJmdBQ-O-18mC46A4IFN2hxYu9J84va2Qh5WhTeW2BWmhRLFzTwWjLjHn01zIMrLarVzQSD_PamFfRTnIzyNo60Ftd_uAat8yIGTHGrUKywVanzo23vkIEW-irnmNiMBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/3043" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPn8kMczX97vDiMpt847DxeMxSs7mIiGFe1K4j_8lNvmdmSwoLgyzLeFcaw_ZuKbyjnwBjzCPzeS_ld8gCNXuiBuCBHiBrEU_XRYeKrxeGOYcCHFLMB7fLRO5TH1uyt2WDG249-tgr5tqnd4ojtL1B0LpfGhmDzxC9pWfGassaXv4GWco1yLdtX9SY4n_KVeWWSn5wMtOp9WyYTGi-WbRmF0pDky-hpNp53OpDWcWbV19_HD0pUm1a5yQD7poyhl8Ldggbtptf5F_fAVpPB9rFP9oI4s8008YGD5IKM6SYmnrZxm3nM3IjlvrhsFOdGyM7lSbdhVls_TvR2D44tePQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/iaghapour/3042" target="_blank">📅 16:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3040">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9zNDoY2j-JNW6UBhid4kFTP6eLYBEBLuGyg02zdX_RqJRNhT3Te3O9UrV7Ap1eJSuPwkbriqgTctC5bp_lckU2akGiLIuG6AAtLCx9g2HWpKj5NkCrDq4VnH5Q4TquxQSr2lqERc8VAzxXMylTNoUVzNUDAGj0lk97G9NrJEkKLksQ9ODvgMo4BECP2QF13CKCoMMBiBK5hgJt1UHK2NSWI_OuQqY2pWck6wNP8D95KK7VXH46Fx3Engjl-hVxZPk3e8fqUPNWy0Y51ZpTfZ_wo8QqhFzfm_hRg48StkatRy9MgdtAyFb4o_SJnT2afBbxfxFw5sCrtC2i-u2zIFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/iaghapour/3040" target="_blank">📅 20:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dneveWnj4_NxfrkSOgagE3XuKDwd93mpDQ9wbvbLsGV79mrDWhpUXUP8HFaiysIGdtzvr4WgqBdAMGDHhPOJllSj2F6zsj_YRWzEnXhSVMKm07XYgvoreY96vGSAdNiVwp1YjzLjBPrnAYewSTYMJ7f6Ul9HlE_VHVZT8Xv_2-fAE-6Y5ibLumUF4hs_SZOZRZ28Mny82SDcIWJmUAUUnAoh02NlkXY-zL6m3LIrNSgrFUAk0IRNCnGdQYjH_8uAXH8LTojACMR-VhGw9cPSP5kmhMKc7-qNDFKeLoyoBNugG69pQkM2kb6zgF3Uc62FlxZIrp1l0aXrI-YUi4W2gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/iaghapour/3039" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWSRqJoMF59Nb7JfAh3X3x6WGE7xu_oAKCl5iF1Qt5BseywlPZJx38HPSBygMpM8LnAWkKVDHk68YQ7W-jeTVxYlzbxJe-BzeNFn4rs2DEN0XtPuKDKDImxnpfrKa0MXjc-aTPQ0AH0_CyBr0Tn_cI_vrmtT26Xhhr74VfB-4eoQjXJAktONVagXw_eUZizcn5HCuCoJtGg_ZZCWNpvDGBFE8rkvbCxsME8t_CG1Y5iDaQ4BluTdk5dEKyQO83DDR4k6OQWAzOxQLvkYuJVYV-WdJUuFDebM91xxw97svQv9YROzsFsK9RZCcV1OyHMfttOX7LiELCX-IoZWxUw3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
هوش‌ مصنوعی Qwen و Kimi هم کاربران ایرانی را محدود کردند؟
دسترسی کاربران ایرانی به دو ابزار محبوب هوش مصنوعی چین، Qwen متعلق به علی‌بابا و Kimi ساخته‌ی Moonshot، با اختلال جدی مواجه شده است.
🔸
گزارش کاربران نشان می‌دهد دسترسی به نسخه وب و حتی API این سرویس‌ها در برخی موارد با خطاهایی مثل 403 Forbidden مواجه می‌شود؛ با این حال، هنوز هیچ‌کدام از این شرکت‌ها به‌طور رسمی درباره مسدودسازی کاربران ایرانی اطلاع‌رسانی نکرده‌اند.
🔹
هنوز مشخص نیست این محدودیت موقت و مرتبط با سیستم‌های امنیتی است یا آغاز یک محدودیت جغرافیایی دائمی.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/3038" target="_blank">📅 14:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFqAzL16rWGLx9KUlWyAswH6dATFODUqZkWpSEJQ3TpEzS5wjQewoK5QJTPJU53oxCR1n0Y8dfSNrIsWYerLjig_TJkXlEt2Aw0J-WYT9cMWupbogPJMViiXpYg-FWprBlzrJUo40oZsWeOBg-E-A5CUa24dRogcXDIkGyj9m5zla7neLgaG8mkTxU0jwuJLsGTBKOAERTB3mXJFv7LXoV0kn0U3JbSGp-5LUwPFa-7wv4tNIyu1vqiYrpjFxlfMruYjnWvw7RVRCsOk5yr8pgDNNEkn0UtUTqz1d6db1XwKEQMv7rXfEDbXcXZuatrL7Wu_5R2cJnhthaJbs7O9gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3036" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFWk7JQwFzOaZSJL6263kIZgVhyRtoZ-jdV74x2F4g53Y6ofzlg1wHCXMBrnFxt_YgOLLPQ8zklrCdr1nbvYNK4iCLqhCmC4Ge8J1up-eIH9gp_M0avTdKoCAD6kDMDUPST0w0CB28yPQ1eLM85tuMBvGCFBJL3bPvMl_72fGE58MGkPUmKt38AtTAMoA8wRDZ0QS-zsld4077i4Nk8Q5z5-XA-4u1RX8kdSO01FMQLqHo3_f_131LD69ekCehH7yORiKNtYNqjIh1rAHmFe6WQffmDkt5Rq4vwlIralml2u3IE-wv4x64AfVsNzZYeLUYNprXjb8h6zNFYlU9os2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/iaghapour/3034" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDZbiK6wanVOkgaIfOXf0ummhcDwrDUXX7ewY9X7NGLyI01pmmXp4YH_XypytTRwRmuKJ_M2Kgrrzodd9vD2yKQOPnTPC6E-4YeEkDWpjJEiPIjcVoQZFjzShAVHLb7e6DOg79Wolz9mUYi3um7b-ltrcz3s74r_2_OXhdCY6q-rjDcUKRi4ERGF3IcWGCnuj6PQ3hbcxTVpPmgpHXNvdHPCKz2nxG7fAhfep80E3pYAS1s2-63lPFLjAzFRVHj2SIRSD1b4a9lO-V9vt6LwDXfvY1803Jlg24jdKfj8NhsvzeVaxnEPO96zAMi6_6-m0dZJd2d_304Y6pFqeawH4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCNDz99d4eqUkB_L74m4V4MLSbNCx3ZKVWWPlhk1kEUmpmFskU6y6lLlzsqFLLPfl4Q1yfbMcf8qZwyBx5POOqU9wcIA5dtqfHFWjTNgL_y87slasxJdIbOfhWIthFMn6rpcbQJMN59e5RndCfuQpwrFOSqWj3NBqGlhPRlLZqI7GQkzAip8NO1noL_OjDwr9OtH3lLvB8APg_2uH2l_BOfPWNKbNKII3DkvA1FeAv8bqqUQyb_plXVl7RbvrVjV83m7wziFgNnI6gAIa3tqtYZjvyhqWp86ksz1RxjAvuSb2BDKeOXbbXDAU2OSYchSUbEyroP0FLD3eyJPBuCQ8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=O01CtHAWeR4GuMvPsQz9cKW-so8Rp5UVNmJ_bDtxndPDjTk7WsShi7-E641rBDbZoHdvab-coYNy3FIymDOgm_UJS88dHCw03tYiGP-ll33lBDNVg2OJQFRRFe07JW9XbYx8qyq5dwvgEls5HalpsG-ys3aLj63znCunoq0QS0wUs1g-NIqq9bombDajMXnd-T2poou1GTL9JJGjFq59yvlEw_iwKd5XMJ9m3I3ImMZz3-X-2aM-Hj_fVTIiSEtMjB0fHIWcBhNXzs-6_puK2-a3OWyaMN4wI2HumxEWcm_NIzm9kVug7mQz55FFwYesCdGJgTz_vug64eon8Nnwvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=O01CtHAWeR4GuMvPsQz9cKW-so8Rp5UVNmJ_bDtxndPDjTk7WsShi7-E641rBDbZoHdvab-coYNy3FIymDOgm_UJS88dHCw03tYiGP-ll33lBDNVg2OJQFRRFe07JW9XbYx8qyq5dwvgEls5HalpsG-ys3aLj63znCunoq0QS0wUs1g-NIqq9bombDajMXnd-T2poou1GTL9JJGjFq59yvlEw_iwKd5XMJ9m3I3ImMZz3-X-2aM-Hj_fVTIiSEtMjB0fHIWcBhNXzs-6_puK2-a3OWyaMN4wI2HumxEWcm_NIzm9kVug7mQz55FFwYesCdGJgTz_vug64eon8Nnwvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS8REdrnk-kiU6qmyIpd5LsUX58J26JiJoFAXbvMVyzr4atgWjp549vD3ABrR_XDEZzL21ucmLnvWYuQzlRBoMKtVmWgQB_O2vpG6VZnnNWi0W9QuimO2WYr0kxWwbtYIW3Vwwv6TwTw6CgZGECZM2kX_2hHk0gz0XgMtfJiOEn4BJfNmmSlhiXEuLfWsNVt7weF2Dz_eRIdG6qb170E49iCz9lP8fYcpqkl9MMjZcdtDX2t2F4SQp2OmgmzISx8DwAiknLa01_Tzd-2jMuqTQC2dWMAPvSmuYFT_0JpMu9PM8jhC0GtHQTkH6-_0LysggJi11HAnALjIGhQjC3Byg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXJesSocBg-_PLrV7enSKjhNlEy9a_0JkjAgoJwpHzVfv3VoTJ2pKtIQ1_sm8l1fMsU03e61aQlvk5FGhQKS1niwQbW3oGUUNP-VDIl2gnAwISAiE_UZuzqRm2Rzsi1lVJGt2jFvHzMstdG-4bEWyH-Q2nmQ7mnUlqkprDC7_sy_-vUAvOmeOGWdqbOo9Eadx7YaXAc0aRATITtZfo6k5NARAgwqteJ7dPNqCH6k0SB1zumQchX7hPl4jkxVXL8APz7wPOmIpanF3wE7pJDRXqTAabecTsjs8tfO1eVoHltdM6HjHyI9sTP2qz7xArbJOmosdEIPgcozCzKKJZgLew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWMKin1yfdUxHWaKuRMz1EUhI9T4FOYcfAImtbtK1PYnXLPxzLr3983a9SM4iSZ2dGYPhd-mn_FuTwnFU0f80C8QKGj2z-GPFWkOx2Fid7WTyf5EkCKpg6qXIAVmG5cZvE_WhbtXReLf31lZT_a6WI6F7ce_H4X0rm1446-x4SHh8DDolZdTVb7ktkpc8LqL-mh0O_UZm1Lkg42t5AXYVMpxFX5LcoCR2lMM-9HGxuNb80u967REdC3C5Klu_M55mFOXG940VyALGPbxyr5AIn9RFYVN0JXTW4Vtrdv2-2GXnL-tsB0R7sNlpAMjQP75tUP9bqb9gEOsAqePGuJmoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5CvtiNKmQ2TmI3_DOv9Z1uAsYCoaAAMK03D1zQCSY9m5xm3fD23Um7mIkv-BTtSlZMzKTk4_mZCUG7YIqV1mVMkLGDNsfP_-wV57bp7tiMTPirwqU9RmRk9K5YPpvNsZFLjuDV-Nmg0vRdaAAq_GZb2MwiSO6LfzLPDv16kAMr0JcyfG4-h7cMTG3qtZ2_yX4cejq8aEtqNWBO5asuQd_5ktUIR2ts_5wbu5z3yUERLfRO86rAKo5ZRLuuFzdCuUIvdxX2RUtpHEnYODL3AzGtxXKdtIcmks4ZPWVVCzi9agdKnUew0neMuvrle_By5dovKroFKcFBTwounteKfSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGCMAGdEZYURTpgRN8uueGKo0y8vshEpFH_pcotW8bwUVKL1uXoVs-giG5l5vuVHVptJJWJ62hT4RZ38vrFH6HpG-rKSWmk4vihDLz0nBgjpIM2t2yKfzZ4X6GVjfEL43dAzoSByixyOOyRAwQGqo16pbqyx1QVaN35bd8_SgHvmBWok7sQ9lJBkIUPh7srmZNpaBi5TFInIYp2hE1Ag1wST7RDl_h8ZfnDTzsUev95Vpf1ntBm_7sf2XawG270PNJNZAuxx3wmvasJpue9-X8qI2d9Z1BZDdI-0zUuSKRj1HkMeaTtNPyMYVcMlyWvj8YhJR9OqONgH5akbPevFrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqIYtAnm34Vm3MdBpWg7ZMAj3w9S2-Y8arDAqaLrksOMQmLXNaVCulMHbfZQ5uyxCGWZwFPKq7MQAiaN58pNyQF6SY2lyO2s3avAx-5jbIXblSaz3pd-SBIqDLitfwvDOFVNbiKRdImIIiRWiG0jAXYaS6D0pMfyjjkAMMbDsfBQZEhTmPelpZ5syUGWpeqy1YvXbIjXDBb0qVDzUPzO9ZMPJ9muU5ka_LvLm_xZYzz5n1jOycixKGU9BYXsXp79rVWqCp3HM6PB8G1VLkbkRbp0MJpz9HoLCJMAua8TXTTQVLo1jhKLoNHmcRRvLGjm1iAXTahMwuOWwXtPuXibOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=SPHnFTLckbVvvmuwnjd6KKlvZfM-Qv1Fq3tioNuEVDO_Z9x2LnjQ6HrWvakg3WFPoPa-_k0pSj3oOPTeed2xZfe0FvkD8R-K4w1Rx57xpYC3EIi-ezKn5T3IHoIo3nQaVRZ6Q0qxRG0_j7v3ubfgPDWb-ftUC1IbdphAPZEaIBMzKSEDkxwnEfCreNyzW_9sDM44mkv6397RSzqpLcctC3zMV9mNnDXnr5QyQuNq5G6V5njFuL5K_BGID7j1N5Z7NZ56O20XNXIstHu_2bl7RCzJzjV2_emjuW0edzPSOH3MGs9Z5VaTOCt2aZ0YDmHmLl8Smmn1_XrkZ8x9rHZ9Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=SPHnFTLckbVvvmuwnjd6KKlvZfM-Qv1Fq3tioNuEVDO_Z9x2LnjQ6HrWvakg3WFPoPa-_k0pSj3oOPTeed2xZfe0FvkD8R-K4w1Rx57xpYC3EIi-ezKn5T3IHoIo3nQaVRZ6Q0qxRG0_j7v3ubfgPDWb-ftUC1IbdphAPZEaIBMzKSEDkxwnEfCreNyzW_9sDM44mkv6397RSzqpLcctC3zMV9mNnDXnr5QyQuNq5G6V5njFuL5K_BGID7j1N5Z7NZ56O20XNXIstHu_2bl7RCzJzjV2_emjuW0edzPSOH3MGs9Z5VaTOCt2aZ0YDmHmLl8Smmn1_XrkZ8x9rHZ9Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vT7Wn5JA02n_CZiWKVAFqpjoVp0Jyfp7NpcHqAlqpABunWJM30Gu0LYtQ3gjYQAlOC3W9AfCxNRT6pd7BEbvWxogh5agOgSuitwdtomFZz0OoexUg2ykIhaNZTSbP45BO93uMwhPwGTzuUlSShZb3puNclsRmPVQKbcC25T1jxFwnk-XB5guivHQvKUIuW3JU8JNr6WGaHON50D0FUE6aNfex-NMIayINMJ5iOPx-T37p9mLjh6Sv8zUQ-z4Jt_nksv48wXqCNEhsNaFBRIaeqLZ1HTGog-VesDYNVFJqIDna8_BgxuchcW5s9QYpfHlaFCELMdTAdzhe2lJLu0tHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUS-ZqeozNMbbpf29jpguNUcKvtDwLw7H_SytoOU4dmSiLOE5wQImrqrKoqtYtzJ9BAS2YlpjrAV0f6ldJ19Bx22R7mcThk23pgtK-fJW_VL605YwmSHS6DzpgnUEz03ivEXZGKJpWSPG0OOz--XHlui3WjldYrFKZkjaZE9djj3vVqHHjI2s2SDjFs1a_GveVDZAO3PUPK9P6Py-QU1vzQfIC8a5Mor5Fm2NwS8RYsOucCxBZ3x8YnygC91-J2rYza--0KMWAUja3zBrHUF8OnF9B2ocWGvqGUhjKSJYf0NFmmduiAXYRD2eRR0NqS6pJqBGonvyEdikHwzZfTbnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUSpTRJqGmcvunAy1CPduL9Mewdkc414glzI1ygBQIVpLn6enSTuTPlQLAP1mlbmui72HR2rtnLfeowI8NJI2GV0ALz0kAr_PL8u-nSlf4Y7sNVnDkl62tSx3KVebMnhgDrP0eKKaVclHtjFOgCjeHZR61UYTetRjmvtqJHdEZtbr2z-5jxHs-I8Wp9F87CHRKc7I7gCnHlUw7WHU5vRPIyrCQH5m-OzJW6-McNKH26KHYE_pjcHI7ZIgomQZFOmMHxtb6BEyPtmvDXSVI8ANH_pfsu22ZbAWdtEIRalrbctBGXgkWIjDd3ThfAxPRFRFNnnUCxFwS1v3XbIHmjVOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8WTdVdarH1DZZRGmxnhI0gcir3yaGS0TqOM8oV6s6YJZHpuTkEeNMHq7GmZdAASX3fgSjNhUSvelPLOx736rIuXzKs1N_NDtxT7vHBmoNzCVw0AMitIlGKqGh9WMvB58y40kRqakOdvmrxAX4luQsVSolSu3bBkzDcEV1YtVosT7kMUcG0FYhz4DjKWgoWfphVArO1jqj7z1b_TWHUq-6NEtTNxWfpR_75KDaiNHsSCj61aLl8i_z3E0L5vVJKTjD74X1FxtPTYWM47IyUIlN10qR-T6qJ_GptlhlObrxo4oOEk6hz8mr6u0zAjYBn57ln-HzBtySRuF6zzzxf4Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBMCHzOIFQjVjmGcV17rXjyiGT2cxTfOtawR-_9hDc3Uoy0NbJEwhlBNtDOX2sVG5ogILsquzJs2AXPtVuDqdr4Cd3FsT61RL3J4kTuL4ZOmaBuX2fjIAZgsuYXHQkgwaQQYOj7pQhdjQiTvywLZ_pY_cLogbRsyHkoRiONudtSKTEMrP5cJzKNHlh23Vzk8PNPnWDayL8RONBgaM_yFESZINaHgAeAaW9D22vgBZCr0hu3FeE0aiiO2czs0AqdExCa9BzRn6Cj4JA1UjUfrhkpZJ7Ir1p2cFVPK6HOzIZd46_sZ2ocvihieIO6jB0gPjB72ThhMI1IZvjRFxDLM4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RotF1kvW8fETUQJ9ma_cHkx11qUufXPJHcS0avitCM9BzTlcNAIWgOl9lYMbrk9Jjs-ajL-9mB0XoJcu-wZKXSvxfVfxHTyL-Ish3xsC_FnTwLMSFCCL90TUXQTbONpZn5gtoAi6-CT9V-5M3zRfPCSosJpdJLSS0Q7jl4P53nDuFv4fzSpCQRqjvwUoRyCKP-7ocQFTmJbb4l5QwRKP2cM-4vJWRalf7tr_FxsAjiuURmLOi9Hn2m3fimU_EBCMiua9gDlCsnIYImTjrB6Twyr7OMSU6mg4dRbeeigZZOtV4vufa5OykeuNYAXrwr7K4qC-ITlg4x15BAEBfn8MAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq-o3TBNWB1SvtU2PwiFDF8pYC4C6VhPEIfFRQ1WJbZut1jsEXAz71tSc29cSbWlxly6DblUqdQDtXNEeaSML1wPRK_x9BUS6jnuLTEkHny_fshtfsFn3mXAQb_XRWHl1eGqZCg-KjvbU04bMVU3dDPMORrMyaJccLCdgs96aAC0u0Sh5l4l43fbvIIeUtAT7Fja4OrPfkQIwhlDlP8RHZzbAVm0e1Kzc6V1zcScyl2GqxsxshJcJAANCNCblPcMhidfBFcLIxq_AwFdLUu66CHlqoWUW-vEQzMYab-UMTdDOCtESXWbDdXfIxBaYTcX5t9y90pY7o6jtMwVDfm_QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=rxNeav7pvj6KT7sCRxk4PowPhbgaCNy8zR29hmx7tuwqMpPclR6NOYrGZTL8Nd61hlzE4s9VyhMF7O_kRhqrxmGB-9pGJ1D4VvqeHfh7MksSfdl6DoBqsfmsiyUqq1Vj2-TyKKYG8dEIqgs8uX1f5BCvMQoBFrwINXvt_PKsuiaGxNES9y0XwQbjM1I_19dwQUztvLHCXdJn-kdBAJUG4CuGbMmAta9WU_HK5begqMR8edYOa8gKjBfASsn_RwsrKFIIv-LdiMKuO7bvqUbwSDdWqae1xvT_ZxUXf8yQxNmFxaTAQzpum3Z17py2X36nxUidXSnpxLayj4_Oj3LP5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=rxNeav7pvj6KT7sCRxk4PowPhbgaCNy8zR29hmx7tuwqMpPclR6NOYrGZTL8Nd61hlzE4s9VyhMF7O_kRhqrxmGB-9pGJ1D4VvqeHfh7MksSfdl6DoBqsfmsiyUqq1Vj2-TyKKYG8dEIqgs8uX1f5BCvMQoBFrwINXvt_PKsuiaGxNES9y0XwQbjM1I_19dwQUztvLHCXdJn-kdBAJUG4CuGbMmAta9WU_HK5begqMR8edYOa8gKjBfASsn_RwsrKFIIv-LdiMKuO7bvqUbwSDdWqae1xvT_ZxUXf8yQxNmFxaTAQzpum3Z17py2X36nxUidXSnpxLayj4_Oj3LP5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtwLQ7nbHjo7U86UBa2ux7CjtG-fFlyXFo2FQeHgmc6wUhFz154Z0g9n25lPzJmpmNnBBmBGlH0oi-cCVNenfm2k87l7rg6on1AKMIhRGxN4iUSzfebdxmf7cHEJqHzXwJYtKskgQfP5fx00K1I3_xrYy4VMFewTSpQeu4NhUMQkyEZ7K_63U0ySb9K7KyCaRBin_EN3TouTFJPMyY-QJ9NH523IHVlJkGUA59AM9_f4ZLnnTOkBfyMqt6S_Ro9kVFEjiomzc_RSIncVRXFlz3VCebQ7PjZ7USicXUPTllLmRdf0YPO6TrI6kG7BAjuZGzxEPoRWhZFBv2QNh4ItFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=JiBP1Q6ZlhzJi-UGNI7SwVyrQW4COfJ-C7lGYr2pFRXyUDAKBswP7-aIayO2fzGvLgdI1tF9FfX4qdBEmb9UjIWVjiG_cT3gY7mf4242EgPIeXLg4uRpdGrS3ctQfX2Dr2ZnDpHRG9PowtFvTgud13hXTxpKHmvIIk-JHB_zdkJdcAfr1vADw7OjLinMCagZhiv0Z7CbnqcMKW5Iq0d5VJTJHPcDwGtVX7hWXX0m0yljNSGt9QQnk34VTqtFdvNW92dcp59-W1bvdsjgHHnoKrrYygMAZwhyXMLzp29mHVRtzsTZp5FfM-bThOuBOsYglCsGgEwZIcbfASe-SZrbIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=JiBP1Q6ZlhzJi-UGNI7SwVyrQW4COfJ-C7lGYr2pFRXyUDAKBswP7-aIayO2fzGvLgdI1tF9FfX4qdBEmb9UjIWVjiG_cT3gY7mf4242EgPIeXLg4uRpdGrS3ctQfX2Dr2ZnDpHRG9PowtFvTgud13hXTxpKHmvIIk-JHB_zdkJdcAfr1vADw7OjLinMCagZhiv0Z7CbnqcMKW5Iq0d5VJTJHPcDwGtVX7hWXX0m0yljNSGt9QQnk34VTqtFdvNW92dcp59-W1bvdsjgHHnoKrrYygMAZwhyXMLzp29mHVRtzsTZp5FfM-bThOuBOsYglCsGgEwZIcbfASe-SZrbIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdN6wcSZmIosgolEA0gB3tzk9GOuOS7UUQWow3mykArcecOAEKxGKn1zmK5FVBHgb5spdfmy5pyzvBGkUgAJtMNvJiYyl9cO5a8txEqmPVTlIc0Lzkw_5Xwij0G2YgEW876Tkdt9i6Uj-nzW3Mcb5Pf0cf9dpr0sdgNBO5SVk21MDP_80QsjVd4jwM2yY0akXomXn34ncVNaFBzXI18_oVH21FAiVWsr4wh1wEG0LS14pta58zpV-U1uT99dva0UzxTlvUddY15eBcH8VKZeFUXdKrzvY3bNDhLSVV-N7J8OadRYmIHOQTc42uWm2CvdcKOuusbjqkdCd05MxGD0lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFCzlNEjAvAU6Ix9P4Vsc86e3A1BEy_XsxbdQVctFBy_1iclWGsMQm-AJhC5ZSWE93tzhcW331-3nNWupMPLF4RaP7u9Aw1l7Tj8k9KzghUm3sXNYVqHwCmHhsjmpmShKt-VN7blqZm1jjkZAjmpQLxq_u5C-r1jkTh0u_aXs-wnawBxsTUUo5OM9-X_jcTskaf3aVDo9w1pj95mUYSdVU_tvn93PZRV-Y6zGj47j7ThS_9ThR1IWJaRmTPQ3XQsE655aWWhvfqVJEnW17xvpDTidtT0Btm5qrBcMWgdyQrb5v8c2zlgkqv_3kAiC3A-5lvovtBgb5DXPJLr-7WCTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjVKK8BsfWtfiUaJY-Tn-B4GtdmqrrJXrYxMwm-5g8DMpdeDRiSyJWwWR-dwjNT2QOEGgfGMZFdJwvmo2NvH7bKg-p-4iXNEj6Q4M47RmDB6TPt7RWH2KA4vHmD64kLX3dJvxcbcvESuC2zoCVKiDHveN3abnhblb2HlHzUHoiGLbZm-E-LCn-64DzR9Dh4UqVSbz-jyx0xfeJAQCI9e8DMh32s-ypmOIA16v6KVYhAAPIf9WQ2RRYFSRkQOS1oq5UfrmtpZqYBcoLRsI_PRPzrFiWeWkfE4G39m1TbzGxaQcBzgDNEiG35YATuvyvIxwKJ17QkSoOcjSlkDF7Xy9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTHMDq4ovG04oTh2W159MhzP1LDSaRI3dnWlP6CIHS6RUU8WF3KNtQXY6GiquTCGdmpbyQBR8bhvDHmGiIFcMkXIXqEbERhUF6zuABt042tXaboX9RYuj3lDaV_QukbFK4tt21QJ0oWE7pPxRq8dWqXzfXvEDS3_dLIzBXlpK5HsrjieLFANHpj-FGMFdcDzZH1Ea_Heq97-oX-pBKLBFAUSYTdhkTPYKesqIZcbsVWqMAPUpmT0ae1kVUm9E-bB30-jcykud7GDByEriehFP2DAAfdG2Dt6PM-ZlejVRCb88pU_iUJv4Sa4ymDcUKRfhtDZ8XXQZV0n9kW56CTo3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5m9cnG0fC1ZHrl8mQ6x7sF3owU6OZuiY_O-hL10RQYGBhh7rpStmLslMSgRqcUWaGD6STZKQGBm40hoNDpLVRUZUJ4WYBWJq8Kup5-cBJyK9q_772LmE1jzOcD5iWtNuJi4DVNIhSvY47vcpIH0DaWfS9VmI9aHNEmJAqALdUaIu_BrgJD8jSCTsg3M3yEJXA6-ylOV9ctOifQWmuPMQyM0aaneJVCIs1gJ9D8Vi96M8cP4oA-TAVyU2w7wjL1AVRPpds-wV6125uIVGM3LQwt-Pf-CKRZPofcuaytl6Aqc0l3WOQT83z7ofIReTwDB14_fFa-I27Kjsi1t0aoKAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA7-qTefst44Gt2ZuAjTYKVmnnRq_Tq4CErpiVRyLLz0fECp6z-BGebhH2y0I0qNu90Vfqc-jnMNehcMGaBEL-ZfPkDZ50uNDG4jXiA1nrPVta6o500-Qxbvv1NWKvalshWEzsAJV7uYQo9dHeYQGoSyFpvC_qMHsBHmnDWQzGP1T_O2cXhw5VJ1DToRIXODfTifcCQHLi6tKW9klVOGz06zn278oAj0hUxiY5bBqejrTGEgS3i8WocktZOjSg4J6k79IaDWN3nd6Z0DetZgPPdLDdA44E3hNJQj678LP9Yj1rLy87qjl1a-hnvCsur5Jd3iiXqiBeskGTlEyUWtSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWNOp6mqyW-LssOenPn0ydtljppe0y9VjKTGD3XvVW9wrzYJOGITSK0Yqo0zfYTYEYENzVK0TOeL9XzNLrZV2ykZh_A1FMGSNARo1YyoGuqbQHCMDWH7TwddYlB5D1BDaTdi70-Ip8AxiiRLJ-V0x1hngGg_nG2vlNJkXaZQpJCWgaAt1j_pJdg4msvUSKaToyzY4vK9-fhhluv5M7BCajWFTklDd9PKyXZV6jDI2E46wd6VRnWu0OrQYsCZbqdfDtrMf8NUJLCY8RF7dSdlICXYMcTVlVMIPoJoO3xz82NnUGEPGrvrBGC0Whg_XDUZgjI4qXNgP8IsatvqXkjJAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLNw7pj3eZiCo9I_1KyfINgKQ2kNInP2ih4j0nIzMCBdP5Gf1eCl963nXDJdnJvX5lJdoCzeSdIT1WIFGCCXPuBr8-mAnOj77UnI5TTfaJKj3qGIcmmzOI8sZ2jZASV8JrK72V11Jyt4plE8hnf6SSUz7vLgV_MFeNO8zdajoLPqpNVTqu5VkL3_btC5Obfuomk5S210Oqo5nhjyRKMrXdbSsUaDF6RTT2DuwgNvj7YzoE_DSEymvEE6wYZc6qjy6u4UnTuyCy7ValvQ5hMJPLw6jknFPCIi2B-ncmNwDNxpodjo8SPaPFfoKEWAnpWbdWYhH8ndJtEF1Di8FWHpHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=jq2tIg_Hqhc_9oBrYiGTiENUzHbf_KFIxKii9-v6LQAlp4cuKs7QXjCkd1WU-d1elk8YmHlN6QvMLadvZaKGo_gOlhfL6y371PNuyPDlvfmcJI7zR5Vk8QXsLGxvty9kOt7yY1lBPMIIN0GuGQvArviKYpKkRiaII1Z3McfmOJhJjEqUt4k_S8x2z6_KI5ViCcZ6M-DmG5oNWG4w2754j9sMpz9fXvRblXrlcNRATXyVd4RwIVNHESjBvURjmO3PqB4-GEzMb8LRU2YcXcOhrbAp4pM901UNLj1EGvsYXtqctuI_mNU-aPNFrJvWHuobgvuloZFRLZWYm7K9E_ZNsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=jq2tIg_Hqhc_9oBrYiGTiENUzHbf_KFIxKii9-v6LQAlp4cuKs7QXjCkd1WU-d1elk8YmHlN6QvMLadvZaKGo_gOlhfL6y371PNuyPDlvfmcJI7zR5Vk8QXsLGxvty9kOt7yY1lBPMIIN0GuGQvArviKYpKkRiaII1Z3McfmOJhJjEqUt4k_S8x2z6_KI5ViCcZ6M-DmG5oNWG4w2754j9sMpz9fXvRblXrlcNRATXyVd4RwIVNHESjBvURjmO3PqB4-GEzMb8LRU2YcXcOhrbAp4pM901UNLj1EGvsYXtqctuI_mNU-aPNFrJvWHuobgvuloZFRLZWYm7K9E_ZNsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1ZjsuWud6IoP-u3oC_d6-m6PezxbSCcY5EYcxgYcS-aZnfIzLl8HB7Q46bGzCOg7_uS-KA2hBQ5EdVgEgLaAa-W04XwfDlACia7HN3o6C9fPCf240r7ylsoUVCtt0QPKs5aIB4Yfym5yHOPIWAPGXLNrTSZ2mjoTVyOJELDjlZIDTGPh1AZsn02mlo_CPz5jX5pTdiuH_0x2-ibgNoHctBGrS59I4_4_M0wh4zrfFHTL9cu7ixW0_HU_DOsZBvII-TD0u33fKFJ6CZN0cQPeCF1dB3WnXAbPdcP9YNhuf6V_NPsDvrhF4HTKe4tJcU0-tmH9t6yPOLSLrBdm37n-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqbv-GuRGgGhpFvpGfaomHVWJE5T18KWCIzpR1e-BCojEwng8dCtn31sKwkkYQS6kIIbnHk_Afk6kAO2C2qrs9iPbvJf9ysiZj9ukuDl9-xlcS9j8ZKgDvtaM8zJenPKqQKZxJy8zIWXPKdN9R4bo9a0W2GymiCDn_53Ky_m6Ta6ysbgStL-0YJlREpo6DmJauiKnpbmPqAJPA5hrzj0NONie_bOj7vixNOCm7FKLDATUEdXxGpQFI7ia8cqZN5fU2v6MEaku0JL7Z2WISVDqDJSkq8afTWYi6uzevshWAqhDW6ONJmknuLG2EtQd8NVCmNp332MGIjZ-WIQf1cr6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiNwdfmqmt-INZcCbYq5j_eGezFTVKGyXaNP2hZUNrraehcYCkO7FU_ClGvKeYojpBDZU1aYo85z-6QQXsT-lbEOzsYNdzXzrEBXlREeBWv_yymGyNjdcu7ZkHu3kP7mK0EswQPF3gg4ax1naBaz0-2fBD9w_-khJKfauD92HgilxUCh-H0eYvGv_opjvIxp11LBcxS3SwLswbwuO0Mf8BlcO_vf_wWiiCF0b_hJX7UiluC1lCBh7U_lx9zOkWhOKIRHlW1QnI1x-oGLx6SmNlHYbybNRlp2Mf8TCILLdoA5PCczM7SzaS0aA0v-IorCAb-_OMlhYAVrE5lFGT6CYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSSZj6RnkiCK4wsG0UMUgKVFIAnZZr5wT8x07qgcbi8uLgHMeu0JCM8DMtChFiRgsbcfm22BPJmPXmZ9a_yEs-0JytV3tj1eRzLiToXsm8kYbDVAJt1tktmiZ89I0hAiFXn3KjQnWJacer60VcD4Bs3GNtAnsKAZKOlRNXU-LmsVK3Q_hwfz9cgTRlm9_f2iossmg3PsLHP2Mkwl7wV6Y18yjGGOcyV0_jbud-SwDcN7sUylCvbpMSKAz77TOCDDitMEgwMNOx35O5fG19cMNnbbnI4-HbQoBgp39EH1VyNw21B5RiqgopYZVEpast8_csa6dZvgtObTCAtGl3gIEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=bJ_EiQ0YqoVVWR7MTYWN5s0cpnyFLBef0U726iJ6DlKEj1NNAVDhO_xM6GCBFFL6tmZKnpV2rcwAGy_W2AatF236AUIeoR5QTgePYM-oSfy1gYt2Meck1cLi2uJquzwo7U1ZhfLjGs-Iv15dLsN93U8x2MIUXabu3DAr6k3fso0YbOHgGWSwHaHCkTc22pPPJIIU9JZ9ODyNv9rlCwxSBbQvl6rYGdSEo8QSOpnNzFmuP4568ihc0-NQW8t5UtKXRdZvNy9LkRCbAl5no7-CEkts5A4a56cayYbCSJOxISp2zWiEVAGP6eQ3cBoBKlqgwD_Oqfy00W-H-aeT4eR6fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=bJ_EiQ0YqoVVWR7MTYWN5s0cpnyFLBef0U726iJ6DlKEj1NNAVDhO_xM6GCBFFL6tmZKnpV2rcwAGy_W2AatF236AUIeoR5QTgePYM-oSfy1gYt2Meck1cLi2uJquzwo7U1ZhfLjGs-Iv15dLsN93U8x2MIUXabu3DAr6k3fso0YbOHgGWSwHaHCkTc22pPPJIIU9JZ9ODyNv9rlCwxSBbQvl6rYGdSEo8QSOpnNzFmuP4568ihc0-NQW8t5UtKXRdZvNy9LkRCbAl5no7-CEkts5A4a56cayYbCSJOxISp2zWiEVAGP6eQ3cBoBKlqgwD_Oqfy00W-H-aeT4eR6fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMhdiCpQjfd8IUWir3r73e9p0WT1o1inBmQagBiS8wScnEMtYqC5v7dk-1SuAG61WGQW9zjhozGzzn7VOh2uqiW_lhafX9q6yoMDxurpeoE9kUF2T6fatHfEpoGL_XwXeMQNTkveRcYpvua74bCnthIrUOnFOM_8Fk82Ck68MPAV1dOje2jYBd7DcMJY8vPKbGUEQoBCuSfDEkGKPBxEFnnhZCqf-SOHlXW1w11YNGNgXc0W9YlRgBeUE5DjgXX7QfwPEjG0kIZef2oX35Cnac9Pbn30srPXFeHw5OyEGrXqGGv_3aX1BjnPHpakWQutayXKmq7reD_mNlasn9wC_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaR5kb-uV-aIwy63jWYOhmw9oX7lWj7MvayO812dp5l7hZLqbkByFmaa_DVjgJfkzvHEwWsOFbkZYavX-jhjbEX7MFZ3i5yCkhKRKQt3m_TnowYVYbjb9cS3wWxIRykfFGO2gmTbhz_Cujap5pkIv8AOANqoqWI6U3YllR7JzFDJlvE715Ir_beb8A4LUtR8Zv-DxW8yuX-EVwP4T43WFrQBwuCbMODPv8XUUy5uPiNW02roASYRneuUs0Sjj14O9d2i6fMYIDvlAvfWY5nW6cMu7CvD5sUX3kMCNQU8IwX6Nz50hw0p98QWrm9h9c785ubClFzVAozB18zpk-t92A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBlbGMOXHMmERABve5KA04awxkYet50i2MqfMFKee6Wk7TxcQZsdWqi6nJhKGHN1Uehmjq-8JMXqc9FxmOi66Thx8dieNAwOaAyf50h2N_cq46QjWgXLTifrgrJNb1YcbnUWoTDRqnUYvllr64qQ6BsDfEqJAY_jzFuUq2QRZCHeuu305WgRUDJXG4Sj4riSljdUCW0rZweWbqlng0sSZCBqbZoXMV1ZDdIHTXoztfuF5nByjJXDMKRZNpyo4wpdumVXGdfod_LejbYB0JMR3A-ee_cliCD-f_CBE3BYnQhQOmaLKe6G6y7XAEvbsMnAI0HolYcCZffKNHBJNf2etQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usiTARX0eUkDE9dWyF4JVI8RAktLtFL3pbXLvmKS6Pui9--shWW4NyxEuj5ATLH1bL2IWsJDFo-sbIfNTVMjo81FQPbcCiBVHV2ajg-DfFek96Pf8xVnzDwHj288f9YSRX9IxFtljCzJ2Cvp12rTzbc1cd8a0Q2IDumnTJi5zq8bIgniqcoi6-X4VOZLLui-qxvk6LKPaSG6Emesr8c8wdi8aSwHCN_IMFoE5lEGmOJ-ZhsM5yDuqlG4kEbHni1G0QAcnP02uwpRQPh2qyQrJud1Zo6BkQHMaVQmojxRvWdhzF2Z75u5kvx3kAiP-I0HQz0tBpZPuoDukKT7mWtbig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgKG0hafz_serZYBaSPcxaBelFrYSXlG7dDNoAg5xj08pNThkLblWtzNBIC0uHI3iGpZcH2VmcBi7UtvShDxaWSfz3Cx-n98dQzXnNHWbZFCY9rHHaG9Sz0FW-HTSIxmXzNk_L7X8p7s5Jh_f4PhWgviTKx5hqlqmwY4JvgcZf9ibK73ru7ab8UJC4Dckaw8_84Ae12nDSc6WEKGC0HAteX3Ns9rpA7Bg7kF3Jg-bX-5AjreybCH90ueaHPUiPP3jkcl5pTEgMfBFFD-0b6OxbbXVemw3I2vnr-T_Qc9Ra4-IkULxZYBszkgfVdRwYb4P0DlpxkHn4CSBpgsIQauKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-j69cnuhgoes9IWBZ58dVchkORCKQ1LZ3sboYcYgh--bnIZHGWjdsf8zdwFZNjPpUfmunKxIygRp0LaM0b134djLUvS3JQjazx-IYZRwkDXOqlriTFGsRueMitvMpqz04IvRp4nj7NZxInJ8NNLBtGUHuMgYyetd0vcAgr0UnIDynUoKmhEVTwv8Wg7rMIvzO8QteoDCkehrBa3H0pARly-AfE7nwvVCprIJlDCawJgcsU-dd-km6DiqQ2In8QUVEUfiBNr0sWxZm-K6BPCkdQksPQ6Vi1SdWoQq2zjAszvJB2Lsd2yOVSstPBitYWZe0lo7ObtovLN1-wjuSPORw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=dmcpKWjsNin27v4H-oznWMeBgf-NvK7fM7SpzacP8HXkGeUSfufDt5RALhDKusHdiMJzJKXN246me5dcj0ttV-4kiCozIRJZI5ogRf34ZHEvHmK00qe4nq8cmodSdPA9H1QDjXemeaPY7w4HpgjFF0FF-PUIgiF4274e1lpeh-ZFTAFiOn9SnxuiXJoYyoUx4_3_G7iCAOjs53dV6fc2fOnydTuw9VkkMb6ztnOd8b_8cg1C8vn3SLhc2NMP1tjYEHN_QGBYs_G3RjvX0DNrt_mBxO2PIPoqmiK58Rq8AZhsv5pF-UCz6stcEgVOepPczMOD1oA_qYjXifhRDnk3tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=dmcpKWjsNin27v4H-oznWMeBgf-NvK7fM7SpzacP8HXkGeUSfufDt5RALhDKusHdiMJzJKXN246me5dcj0ttV-4kiCozIRJZI5ogRf34ZHEvHmK00qe4nq8cmodSdPA9H1QDjXemeaPY7w4HpgjFF0FF-PUIgiF4274e1lpeh-ZFTAFiOn9SnxuiXJoYyoUx4_3_G7iCAOjs53dV6fc2fOnydTuw9VkkMb6ztnOd8b_8cg1C8vn3SLhc2NMP1tjYEHN_QGBYs_G3RjvX0DNrt_mBxO2PIPoqmiK58Rq8AZhsv5pF-UCz6stcEgVOepPczMOD1oA_qYjXifhRDnk3tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2944" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QREkDh7AOZ1Vg5FtTwVd-TItCLMJjnILsSdgH3EfhBur9pPhYX6PG9RA7bgNYaNWbLlQb2EhgC6k2x5WJ3VTZJSyXYiuIpgrxEhmKABi_AWvdn_ghzr5KVmGaU0f3BzWPYuOuwE20GLkMn-UDmPKHqieai11Z9TSTZfYVKJhDx0BuA2rZ35kgq5h6NaUTCMhYG5DJ6g-vUkCAdE-JiV4TVugi0zk9zUQElnbdmTb-3qkYTI0sHN5Ug50kv5uF4xV-qF4ErFjgr82Nrqau5L_yelvAQr_zXDSAKonRsNoJM6CwjTrUr7cidUTObVZdrpwDDFWoSvvglkXakBHytasCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAgad0lY-PCfEgqr1FDN_JihXM1IALl6JC8T5IuwX83iIRYYwtyqn2YOrHTER2-5xiYz3XMWSDNmeAY7spcw27wsOVm2s8BjG4O7IYarag-ndH2Fs0t31mjkCSWXzLDxBPjScY086Iq2xByUbdPQ5N-qLS_xk57RdCwt2O8SmOHvOSsP8FgM_gqtRSroWfTJTMoRUtuxePSTljTa_wmVm7h2tbz-rWSy9AD5Gd-aWwZ92IhaudVgB-F0fdoAs41Z4b4aenMyeROg5mmX3NfWLHVA6eyttQFdvrNoP2Na1JobGTIpMWQu4xK_h_RrpYEZSijMgdii1vWdzQoUaWaPHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/2942" target="_blank">📅 18:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KylGK9Xy7MS96Vr3q0o-9m-iOto17JHQ6ZJsGmaXV2aJA261aFmXlFu5CJS6NgFCDk7wrb3BRkbi6FH1Ji1scB4ULi95WLjugaexW7UqSP6hfeRlv3G0-3b7cpHOdzNedj8lBcuJFy4rqAZJPeCtqVORJV1A36Bk-qfaS0MH6s-73Ay1_2_S-s4wqtD20TR8TpJzEudosnXr08ZFTJ18pP0UAnzHYYq8yVOjdwluIZGDgIy-TUUtvdx7Xo3ssy2LnqzwMM2GCTql900usCVmlo4krc3DdgDE6fZyXYSTELwxD86iGGCVbaAsXiSsWJR1EE5z6QOltyOzfZmQRXAQ4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2941" target="_blank">📅 16:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viHXdqbLCEuVTGLeROMbcznc7bOZ0Gy-qxGah5EZkNkxrwIYb_sNQQyxZbsqL7cDp8MbSrPDSYO2d2_AZosjMSgBf9BT_IT6DX9fElUWElQDXzgYkOTItydq6lgOPzEjKesNeNqJ6Ar0RY9-gGP9Tyf-9jUqMFSShNSBT2vBJjGMw6hxyT4JYH4eKOBag5XQidRuf-Mcv4qBp8-LNd7esF543_zz7SCk_ZTLQwhqv_48ToWyolLh6EGnIAp3KpcLWfTOrnjIXOM3MDjqd0oH68wfYGNv1L2pk4eCrdNu3ZQ37zkc7E2RQp87mS0v6KfF3r5gBhIX7bOrv9ZEb6-ATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZl3xDaoTIj6LBPRvC544kWEGFBej4BUMGBI3ElCGCFw5JVfpqL4d3YtSAQX2ZPTxXApzQ6oYdBBZDP87lNAZTuT7tv31JoskSmPZgPHZcCk_gVOp66AxLIDWvzVhhjDz5yqjAVSiJdBk4r3fFMQcSR6038Qq07uWxVhlGI6H4363T2Vsu1miI1r1xqYyE3iovYavBtxt2cQbmtiratnUZb5LONr2cxBSPxTcOXnlRullJ5s4WwSNU7jCOuEINAWX_1NjXhQiPONA6UeHBhdRoIVZks5803zlxIxZB1SWsHJAxg2IAhw4nMVgJJ24MRolqOr2DmsEDL604vuOmaaxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2938" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2937">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3Mr5f8OJ-5xf79Spyidcp580LeK9ywt9eHU3cL9HeOi4URPuO2rgxFag3p6P3AkZThOcThSrJuM_nD62HF2tMnqVgkDn0Xdf9BrmvODrOZr2qx2nbILo2aCm-u0fqUANRLqQaEse38Htu3rhJxZbgUOa-Ofv4Ip5FADFtB1yFiGLeEPAQAYNAOvbg3Fexfmt_DWPYAjY2WSntbwaxkzHL8hliLuB4xdnBL0wMAkqDs7WDu55AK_AbD8N5BtcPE7ZBN8NfQ91Q4iJGVpIUb5uQJVI0wQo2O6xxi7H41rbpW0i1grJWPXlxNn_a07ae7iMP5ImI-sTg8TC2hafdBtQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2937" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBSise55IACyUmMhTxAj5oh1A_wI-icWyhqd4Mw19rOZagzMDCgeMjupg6M7U4_IShQejP6Gu2pSkC-dEZMj6bhZigZF0z-MRc_cUKhDQPxOKUAD8hFuGLTorTbIySPa-tYLr55w92Qt2nr8gXO2QUSGNcp8CYTF1R9EW5ezIqMfjKKogg7Kcz3ihL56QIpbGdanjYesy_-8aqn_-C2olqB5sWWsZ1fclE8u2zzMvrb0p8uWTSmZrOcuz3f5We9JwDnC1jJqk2ti21NL_9djupj8ERQxyyyS-vpSjXbF1mHxxj9uHfMY8Uw6Wqcc7jn4uyoNbHrv_gNe85WdYAlbJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2936" target="_blank">📅 14:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6E5AZX7TVs7IORE40nwGwAt7ALczz8tfhc1h1g4DrhFXqLz2bQIPoNxaM7OG1l5Eb095TR70M3_nz-CL2MkRHgdMoSWQu4i6Yr-8vZqg6mrcFJiB8aFgI-leb-2kwfzwC9D7-AYSAviJhryNhGVir9vXNg8pS1P02ynhhD0x6DsXEMq-BImdPMRjFzAJ3Edd8syEcX8HPkJS_2GWKR72fADtM60A4z60oJo-rvakecKazw4yMKQsyZahYhxJ-91ZGDy6mpawe00Xdxp6yaMg2Nyvj3_DnDRyiTK6jlAj1MSMvESDBBfYwoDdXpX6KtqVpxjAomyUC3kcjRi7yWJcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/2934" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2933">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFsRUAbC-LteteQrysL73XbX39ZeRJ2q6Vl_cqnChnMLA_Mgmx7xX9WjNCb-KpBUzYDmcjt_y606D9ZApnj5w-CUwGDNxwzoA85OkPzhpc8NgfGqL8ZZkQlNSmYZi_MWoulWCvbqB6YvzHazKE2_0t4fq-wNQHsR1tuwcYzEKj4RyGOWulUBxVFgXAS33ajYF27RMc4WNzUJk1rKtGVlTzI9njnRqw0-zS5JktH7lfmQocyEHjs60iO-htwRzjH8ebEmk_j0Mps9QDPv0CQQbGmsCzGMrthr_MeNiKuSz_I5Go6wyhcQ0HiQLid1DeEmt5ByDQtzTOvJwgkmyyMApw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2933" target="_blank">📅 15:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2931">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViLUnVwkqDXlCeZYA3agI7iLZK4-ZTibOmC-YSIM9QzBr_-AWvSmNKAHovEZqP0VHklpogdFHrDudN8XdKHlf58jTU_FUXzsXp8YD5gaKZvZOiNeNr4fNDWdbMMsa4gt5F2PZtB6KF3SYFYjL6xG3oFnTTgYiUoCbWlynijuo0S20MFBokqOLqFW6vM8PpQ52oesKthwMwoVTfJBRLWLMrncTCEqX-z6H6nXOJSQkXg1fPgXemcEFEg6ilIYOB3pKjEyPPR8J9QtBVD7_uc_WS-xGaSr-qTbiAr7bM9bhZRv_BS08rOTV-PlmtDyw92xp_mske7ZkpzYtMwASzp53g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2931" target="_blank">📅 20:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2930">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2930" target="_blank">📅 20:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2929">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqJkAmGeuy6zEOmrsU_dHusKUMXS2txJ8XFBjHmqlMBOu6xijU-PHOcv1NEGxh2lwRjGlyt5EcrIHAZBErsjdym_48gyd94UAfsPHtWVXFoN5QSBdALYugsD8D16LL7lyVuXoz5Rx_j2A39qihJXWyGU38qtU0xIffNpP3iOPVgumS21zdWCIP7Zx48o0TUZ0AWEvTn22q5rzT4HwG_LYrvDORxWR_px9fLdz4AmZi2rZYPx0L928Bj-PyflIxUNpJk4gcvNo7rXPN8WLYLd7KmUcWhqZ4hiTfFrdZI28PE3J-n7v4uYv5YX7r4XHo1Qzk97jNkFbKuM1dqQnrlmJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2929" target="_blank">📅 14:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2927">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4iHfPO__D3K8DgppyXeC-5FxFYmIGuRGbDojxTzvWw-hJKY8CWPSPQ7X0QL3dUv5RANpaEYkliCFmkE4v9wAWid_N8LLDbnVvCDKkPdNKutm0wkgNQeFKge_yabShIy5zbQ3nsYcmeWG0hM09NgROtrBT1VV_X7XCJTo5h2aBx2-08ENa8c9nRMDU6N5v0G5ajcMtj7KSziY83lIaETHnMjxyhlnxP9pHUusoJBqqPSm53KrCPCRoBZVZqBHcKDevEhyub7MFQ-doxebnH59HPaSkIoCOnBR3AKvgaLol2og09bOeIdV7HTtY3rAyinwEXpJLDF-1by_qrRK3HOeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2927" target="_blank">📅 20:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2926">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyTFgbknZE7CuwAV9KFvQ4WLHAn3uV3mHPdTDrfOOJODl4BivboW4TNnlxu2MOIxDCElhgNHEKgxnJAw1H_ydhgqho_qves0N5yRTBxXDDNg9uoqzBJoIxm7mmJ2s41eWxeBX3y9KK7aATUSCTeDs8jTNTXA7pyuUoo7T6gvL-N6iYZr3kc03o-rFEJ4aLDvIcNfcttI9Z6T74Mv_hcTtI5iQytyieHzSSEBXK7VQlYDNospvg40Ymq7pK0yY_Xa7WE61_THrroPyyqGBxvMZHZ9PpjGaUBwUu5elQVaqZ4kkuCCyHyhOu19QWbJHJf8736OQbSUlbHjtueZSHz0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتار آدم های معمولی با هوش مصنوعی
در مقابل
رفتار برنامه نویس ها با هوش مصنوعی :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2926" target="_blank">📅 18:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2925">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxjZIoxnUwSjL5KFMLZ6wF_8S98b32GrJd0vB6miVWQCWhQw3_QrRbll7SU5VmcwOg1aT4gmHn6JJ1O-rey1jVaDRm7W8R3P33hVz6-Wd1o44SX-l92whZkzZ1xZ1vJa1KOXN7NmDAPfxVeUfR_iGsQOuU0tfMGz2aGLJAu-8uak74EqhjEat8aNO5I1h8KfVxF9RLqlE_57-l8ZMZf4IGZkdujGM0yAslR-Ap7myAyJaRsv61MAlrOrNfgiYPy4LCoZ4HRlwbESFnU1oCL4HLy7hqX9oESoRUnfMD-c5bbSMhDr59DXZ83s0kTrPeI9mCkHER6b9D5M3h13W1j1eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2925" target="_blank">📅 16:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2923">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/2923" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhcYGWpP2YD2sYC2s_YlDhxoV-lF6tT31XsUKp65ahZIbcqBhAQIDD50c4NrRBi0QMIdUQFg9R3fYw8mPa9IQKckEj1oIxuu6Nqw568RxtSGdN9NAamUhfE4kWykSCNjpta2v1qO4CcVEZaN0JevWQjuhyLJ2sA5Z0IPHpggzHgiUez2mFMLET4OdRFoqqFrBLCuMo_5HnPnU7H0pUhO6a7cy92Q72y6RKHiKfUuWktn3oTVvsdCy0hYCnF-OFGruo9Q9hu3ea1KjZoXQmYb_V_TXqWQltQEqjdk0kbFp8mlun6_qwAqOxaZ0O5fXq_HMpRc4Rls5g_LVmgydnQSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگه سوال مالی داشتید میتونید از آرش بپرسید بچه ها :)</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/2922" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GISECBouhtZg51jgAt1_AG-dMni1kpqRRac1iBuAeLj8fTclNl6MVA-yKxwbIGZZdjo0pQVaPMnD45Z5NjzA39tgEpCDp0ZlMx14gMkX6pw75bQyTyea94BIgRtIxH7JV5ixpInEYkBVqPEkFqY2W5h9wSlEAS5kJTkZSt86ev2W3cgbeT_2YoTtKkN31ZLDXLFHzutTmb1pu9WmhYz7VUAWAuZngNZCB_kMUGgl-bNpumrWMHcLrx0r7Tw_ieceBtQdDSfewO0H-i_eRxlv0YoTsrAZELSFu5TSQRZ6CTP3_kzAELSe1YTTxDmQLVYBUc2VdxB25WWb5mS-hcBTlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/2921" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2920">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q57B40PJqkE2KTXOGLwqdjxTpEMYqPn0-wgDuOxDsWHf12v6PAoqJnzSwxQfvLxFkVziSVFz_UBpHb8dbedPqn3_UBAFjPxoK2_37CG-uPU_jq9eIG0WWEFb21Xnc5katTAlXs0P0TbhLFZhSGAE9ihXXPzKcQyZc97HB62ymAGxk7REnoYDzIEEa_840_tqJbLQMyMJW-V3nrKvrXhQ5gN8j2lxuKXYb_S6iHdb-a2bABAqWaIpj8OZbtj8AY9opCx6RWOaEzyuwZ3SrbyqrGVEklVt-z_jzX76zktbBsjyqLpyzwHmHs6loVrYxUOdfBRWIbJPUxlS1w5APLCZhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/iaghapour/2920" target="_blank">📅 18:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ab5fc23.mp4?token=u7jCxdpSWm3nLERT8Qu82jDKav1e6a5HVTfNhsBlxQb1mKL3ZQiYjJ0ps-eaPXnH_AShDBclaqdyHigcpJVxw8Js6FzSauRuPhF_xOAnpFFvGu-qNl6KkwLeFhJQR4TPxqRnuoYqe_aK4Ll3WW-ITUKbM9jdIKijOK5PqtdYtcSOgzyEK7Vuxt6ujDKKkAxJsgvD35rbaGgkQ27IWuJgKFYs3Osru1mw0nkr-JXZC6vZRSjwmpHSl62dqNemRvV76DLAeb6WHYJZR_A7kOB97GgJCIDHGO5fFRbt5kkzYHON5s_uOQTjr5_7U1g6i0oWj3IpNh8JXaJnKQIppPsGYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ab5fc23.mp4?token=u7jCxdpSWm3nLERT8Qu82jDKav1e6a5HVTfNhsBlxQb1mKL3ZQiYjJ0ps-eaPXnH_AShDBclaqdyHigcpJVxw8Js6FzSauRuPhF_xOAnpFFvGu-qNl6KkwLeFhJQR4TPxqRnuoYqe_aK4Ll3WW-ITUKbM9jdIKijOK5PqtdYtcSOgzyEK7Vuxt6ujDKKkAxJsgvD35rbaGgkQ27IWuJgKFYs3Osru1mw0nkr-JXZC6vZRSjwmpHSl62dqNemRvV76DLAeb6WHYJZR_A7kOB97GgJCIDHGO5fFRbt5kkzYHON5s_uOQTjr5_7U1g6i0oWj3IpNh8JXaJnKQIppPsGYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/2919" target="_blank">📅 16:59 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
