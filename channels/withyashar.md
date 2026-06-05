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
<img src="https://cdn4.telesco.pe/file/p3vWM1xK7feOaqLbHVAzHegouR5ECJzbnjlpbFbuaYsOusk_oRrLiYUxXju_4Picg_KzHbUtLaLztJ3f4ecdwsxYzVHhVXdwj2w9RSYIGvZc0Gj_l-JJppKWHOvlWzTatzchZZ03Twi4uGikmqj8Go-zkRFr09F4FyljjX-D2h881hjlOgjOOZ6lExzoq04pghcGu6EaWifYXR1fAbU-iTJmsk15KKksncSYMUSFq2WYpsBVrI-2vq905xrN14ZziKZypvosKvC8f6MpETHZYO59JzDjeADgXAiWfCYzQ3uehdPXCE8mzzvYJG3rEYGyNJd2rzi01ofxZRXpTbkxRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 289K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 03:29:29</div>
<hr>

<div class="tg-post" id="msg-13534">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fcaccf1cd.mp4?token=Ode9Qj1oCrfcDMfwoePAk2sJClCrQw_Tg-TEXMWNiRAdTip_3IyN27I6K6XUJWD0_uYgZjcoKzfjzpw-bzlJN6e_KRUVtOdGqNVjl-AxAV-Bn8-IwGi0GeYURmFyYJ-IMDGnRATE9CiNN7KZkr8QOZ1zazQuHfr0ASMNHO38Ib4l8INb6rVrVW5OOOs4yHKNK-G_N8dRvUJWPl33pnEg-2_cyxDc9D8I1wUgbp5QCaD9ZQ0KniXAzq8JXGqlvk7KSgh5w6Za9mPvAs7KEbyQ7DIg9qzmObMao4BtbXSrZbP-tR9UbYGsglytY8A0-3MLaelFGHZoaM0a6lBr1bMNAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fcaccf1cd.mp4?token=Ode9Qj1oCrfcDMfwoePAk2sJClCrQw_Tg-TEXMWNiRAdTip_3IyN27I6K6XUJWD0_uYgZjcoKzfjzpw-bzlJN6e_KRUVtOdGqNVjl-AxAV-Bn8-IwGi0GeYURmFyYJ-IMDGnRATE9CiNN7KZkr8QOZ1zazQuHfr0ASMNHO38Ib4l8INb6rVrVW5OOOs4yHKNK-G_N8dRvUJWPl33pnEg-2_cyxDc9D8I1wUgbp5QCaD9ZQ0KniXAzq8JXGqlvk7KSgh5w6Za9mPvAs7KEbyQ7DIg9qzmObMao4BtbXSrZbP-tR9UbYGsglytY8A0-3MLaelFGHZoaM0a6lBr1bMNAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر اختصاصی جدید CNN خسارت ناشی از آتش‌سوزی در ناو هواپیمابر USS Gerald R. Ford (CVN-78) را نشان می‌دهد؛ آتش‌سوزی‌ای که در بخش لباسشویی کشتی رخ داده و در زمان استقرار آن در دریای سرخ و در چارچوب عملیات آمریکا علیه ایران گزارش شده است.
این حادثه در ماه مارس حین جنگ با ایران  رخ داد و نیروی دریایی آمریکا فوری اعلام کردن آتش «مهار شده»، دو ملوان با جراحات غیرمرگبار درمان شده‌اند و ناو همچنان «کاملاً عملیاتی» است.
اما ویدیوی جدید CNN نشان می‌دهد خسارت بسیار شدیدتر از گزارش اولیه بوده است و منابع به CNN گفته‌اند سامانه اطفای حریق ناو از کار افتاده بود.
یکی از ملوانان گفته است خدمه حدود ۳۰ ساعت به‌صورت دستی با آتش مقابله کرده‌اند و حتی نگرانی درباره احتمال از دست رفتن ناو وجود داشته است.
مقامات تأیید کرده‌اند این آتش‌سوزی به‌طور موقت عملیات را مختل کرده، پرواز جنگنده‌ها را دو روز به تأخیر انداخته و باعث شده ناو برای تعمیرات اضطراری در یونان پهلو بگیرد
@withyashar</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/13534" target="_blank">📅 01:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13533">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ می‌گوید دولتش بررسی کرده بود که نیروهایی را برای تصرف اورانیوم ایران بفرستد، اما در نهایت این ایده را رد کرد چون خیلی پرخطر بود و می‌توانست به تلفات آمریکایی‌ها منجر شود، و این موضوع را با مأموریت ناموفق نجات گروگان‌های کارتر مقایسه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/13533" target="_blank">📅 01:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13532">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ ۲۵ بهمن ۱۴۰۴: میخوام با آیت الله علی خامنه ای دیدار کنم.
۹ اسفند بخارش‌ کرد.
ترامپ ۱۴ خرداد ۱۴۰۵: میخوام با آیت الله مجتبی خامنه ای دیدار کنم.
چه تاریخی بخار میشه؟!
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/13532" target="_blank">📅 00:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13531">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ: ما به ایران رسیدگی خواهیم کرد، و به‌محض اینکه کارمان با آن تمام شد، در مسیر بازگشت، برای مدت کوتاهی توقف می‌کنیم و به کوبا رسیدگی خواهیم کرد… باید از شر این نظام خلاص شویم
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/13531" target="_blank">📅 00:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13530">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: برنده این جنگ ما هستیم حالا چه روی کاغذ چه با قدرت نظامی
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/13530" target="_blank">📅 00:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13529">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: جابجایی مواد هسته‌ای ایران مستلزم حضور یک یا دو هفته‌ای در منطقه درگیری بود، بنابراین ما این کار را انجام ندادیم
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/13529" target="_blank">📅 00:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13528">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ : من دنبال عملیات مخفی برای گرفتن اورانیوم ایران نیستم اون اورانیوم عملاً دفن شده و از بین رفته
اعزام نیروهای نظامی برای تصاحب ذخایر اورانیوم ایران؟ نه من نمی‌خوام جیمی کارتر باشم
@withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/13528" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ:
راستش نمی‌خوام با آیت‌الله دیدار کنم، ولی اگه ببینمش، برام افتخاره. با احترام هم باهاش رفتار می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/13527" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSiamak</strong></div>
<div class="tg-text">عمو یاشار اتاق جنگ نمیری امشب؟</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/13526" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ:
من در امور امنیت ملی خیلی تجربه زیادی نداشتم، اما فکر می‌کنم واقعاً کار خیلی خوبی در این زمینه انجام داده‌ام.
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/13525" target="_blank">📅 23:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منابع عربی:ظاهرا چراغ سبز برای بمباران حومه شهر بیروت گرفته شده است
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/13524" target="_blank">📅 23:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13523">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح هم اینا برن، طول می‌کشه. این زندگی واقعی هست و رؤیا و خیال‌بافی و وعده‌وعید نیست! حتی مانوک هم گفت بعد از مذاکرات تازه بازی شروع میشه، پس ما اولش هم نیستیم.
ولی با من این مسیر رو راحت‌تر از تمام حالات طی می‌کنید
❤️‍🩹
🙌🏾
ما بقی بازی سیاست و خبرگزاری‌ها و مارکت هست که ما هم به ناچار توشیم و انتشار می‌دیم! ولی این اخبار به هیچ وجه نه حرفه منه، نه کلاً تأیید می‌کنم؛ چاره‌ای هم نیست، این مسیر باید طی بشه!
از توجه شما به این مطلب ممنونم.
دوستدار شما یاشار</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/13523" target="_blank">📅 23:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13522">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فقط‌منننن خیلی‌رک میگم عمو ترامپ ۴۰ تا ملغ میزنه اخرم نمیگه
😁</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/13522" target="_blank">📅 23:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13521">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد @withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/13521" target="_blank">📅 23:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13520">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4113f62c.mp4?token=qYYK2z6XnP_FHBl0ok0_y4cn9U2OgIZb408zju6anDlUnwwy10C8cHJ-hpqjAxlkigxqhU24izp6yOwysVyhDVnOxTWzMY8XRrFaYAEDeV8Lk7QIZIGmiZfXzoTSuff7BGXOYVs4AMVbkfehoZIF8XvizDr3G8EBKkt6cqYfD5JD21mHqCJj_nltt1TExeKEAWNmFQx_Fg2_ZVGpGZuQ-BsbNJrJWS_XGSw-YzDZ-oP6ZWxYe1xPF5EDpht5QjScX1CSHutnUjYrRjTpLuiBvr-PFnyc_z6l7z1hxgQQIAmvsYuHqbqJ6zq-bEk7DiaaQKydMDHA2Wykxx8sGCUBMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4113f62c.mp4?token=qYYK2z6XnP_FHBl0ok0_y4cn9U2OgIZb408zju6anDlUnwwy10C8cHJ-hpqjAxlkigxqhU24izp6yOwysVyhDVnOxTWzMY8XRrFaYAEDeV8Lk7QIZIGmiZfXzoTSuff7BGXOYVs4AMVbkfehoZIF8XvizDr3G8EBKkt6cqYfD5JD21mHqCJj_nltt1TExeKEAWNmFQx_Fg2_ZVGpGZuQ-BsbNJrJWS_XGSw-YzDZ-oP6ZWxYe1xPF5EDpht5QjScX1CSHutnUjYrRjTpLuiBvr-PFnyc_z6l7z1hxgQQIAmvsYuHqbqJ6zq-bEk7DiaaQKydMDHA2Wykxx8sGCUBMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/13520" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13519">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ببخشید درود و ادب خسته نباشی</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/13519" target="_blank">📅 23:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13518">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM H</strong></div>
<div class="tg-text">ببخشید درود و ادب خسته نباشی</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/13518" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13517">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM H</strong></div>
<div class="tg-text">پدافند سمت وزارت کشور فعال شد الان</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/13517" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13516">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">منظورشان 3روز دیگست یا 10 روز</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/13516" target="_blank">📅 23:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13515">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAMIR</strong></div>
<div class="tg-text">منظورشان 3روز دیگست یا 10 روز</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/13515" target="_blank">📅 23:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13514">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال 12 اسرائیل:
مذاکرات به نتیجه نرسید، آمریکا تا آخر هفته پاسخ میخواهد و با ایران اعلام کرده یا توافق می‌کند و یا درگیری از سر گرفته می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/13514" target="_blank">📅 22:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13513">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaR0IWD6zPeqd4UpaPh2ssbMp-gGs1MDLhnLI6hKZNvDbgzPYn3NbAQjIUekS5Yh3evWbdVHESn2AjfhhuMLzsYUd5xctKtZYIVo1TS9fwllO6x7bwJQJEqYA7y0ra9iH-29Jv2D_LxT9Japa4yws7Okc2dzm6dj22SPQe_6EDg8FjZDM_HaJCsbeM0cVfryBrBCX2TRuX_wt5jOErycnisCd02kWUvoqt4aFTwSdrjj2B9DhX6nw8HyrvhDFyNqG6ZrD1ciFg1XzG86emGZ7wP5mA9xgP9kjhPSNazIs5WMAqBhg0TIDcNFD1Dhi7jozg90po7PC4aq9o91ssrItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده هشدار امنیتی برای تمام کشورهای خاورمیانه صادر کرد
دلیل این هشدار محتمل بودن درگیری اعلام شده و از همه شهروندان آمریکایی خواسته شده که نزدیک‌ترین پناهگاه را پیدا کنند
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/13513" target="_blank">📅 22:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13512">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBYCDYzUqszgmFF9qw0WiIZeq0QSwMgDCViq5m53ntyoiR2OXZBw81jg6Cl5392NZDYVzU8vt2Dg6_uENbr7UjB2ipyPyvbQ4m2QNSHq3dG8Lrdqx09Lpw9M7ZeRncFo84dYHrzCLD2tj6TfpVBPCg1Tnax3Qjir9MOka9AG7O3bl3SErnXHdyIp0iV67RVe7tAKL4YvBdWtugA-dsZ9LlWNYp38Hu6LS9udKUKBU-y6ehc_7-3SPfdMCxyhXULR9mjhHul6Shl5sdLYFgh4y658KnZaR-fzZYt1HU5s-yErcwfzlfGy96cA-iHcPdN8fZrdgpYB-bmnZWTCpucVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرشکیان و دخترش کشمش
🥴
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/13512" target="_blank">📅 22:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13511">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عراقچی: ایران و عمان مدیریت تنگهٔ هرمز را براساس معیارهای حقوق بین‌الملل تنظیم خواهند کرد
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/13511" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13510">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سفارت ایالات متحده در اورشلیم هشدار عدم سفر جدیدی برای اسرائیل منتشر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/13510" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13509">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سی‌ان‌ان: ایران می‌گوید در تنگه هرمز هزینه خدمات دریافت خواهد کرد، نه عوارض
ایران می‌گوید به دنبال دریافت هزینه خدمات برای کشتی‌هایی است که از تنگه هرمز عبور می‌کنند، در ازای تضمین امنیت کشتی‌ها، به جای عوارض ترانزیت.
این کشور به دنبال جبران خسارت برای خدماتی است که در کنار عمان انجام می‌دهد، از جمله کمک‌های ناوبری، جست‌وجو و نجات، خدمات امنیتی و ایمنی و خدمات پاکسازی محیط زیست در صورت آلودگی.
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/13509" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13508">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادعای رویترز بر اساس داده‌های حمل و نقل: صادرات نفت ایران به پایین‌ترین سطح خود در حداقل ۶ سال گذشته رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/13508" target="_blank">📅 21:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13507">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال ۱۲ اسرائیل: واشنگتن به تهران گفته مراسم امضای توافق با آنها در سوئیس برگزار خواهد شد!
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/13507" target="_blank">📅 21:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13506">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQzGecdJbhMC-BwdwqrUay42iamrM0YzRIV7O7anEKBR85s-_QyKt--Uhe5c-qm-KVNSx6_xmQqUEDfCIJrg_w5ukWsinnm9GabQuLDWkq06JOpZIqU0gXF4MR75DeaboIr5Qf_1MkgIFTFpazl_jNiBQ-dgEG8C9165UZ65B2fRvYuymSje4ISP1DrQw0AMk61Wos22ds8wJ7gPiVTnGpojkdo-9iHkZfPUDJgmE2D4EH8qgab_926TChLcCvh41od9tHLHkEjw3Gw7M7wGy_aOhDQzf91CmlCe3z7u9Fc4Pfe33OLZtbV74BoQT_IAcl3aKC9T-7RiOowFS2zoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل :
اعضای ارشد امنیت حماس را ب درک واصل کردیم
این اعضا وظیفه شون حفظ امنیت سران حماس بود ولی خودشون حتی نتونستن امنیت خودشونو تامین کنن
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/13506" target="_blank">📅 21:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13505">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خوانندگی قیصر برای کودکان میناب در میدان امام حسین
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/13505" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13504">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twUhrCpnoFrSjceIt2YVxmve4wWMIeuTIbFoVKbD5s5qSAnOXjLyULeRjH0Ri7fPGQJ2Dhq5PF9mZZFVn-XbOFu61VVmun4rGYxxVE_AltEiUlO3z3onelTo8TJRAkUlSj84AunDuFAY66njvAY0McPMTSPU8qJMdNyj8hH41GF0pJIVUH9cJ2n_v__HJlXY_ZvpoHYe_vMikt0x4eGvfhLlNZ7u5Ti8mbbsfCy0ugK-RWiqpjXmiPjjOQUBoPHA6HCK5GG4FNexUbhqD3fHSpGYe0rQlOmr4gYNucjPm-fAEx7ZpOilcwswAt-S1JjWstBSGdTBLy9_e6gqE2aPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها سردار سپاهی که امروز تو مراسم سالمرگ خمینی حضور داشته:
محسن رضایی
@withyashar
🥴</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/13504" target="_blank">📅 20:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13503">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">@withyashar
قیصر</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/13503" target="_blank">📅 20:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13502">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efc791eac1.mp4?token=eGnj7MLcZETWc5yUd3Uq_fER27dvbfnxI6BYRtA_IzAYhoo1rknfoWJefi1gQZsnbEnwgoPTWw5auBdDsPsU8TtX6Zg4qDsaG-xnhqd2jJ9HdNY1cACTfbiwSH2XRcDiqH7-cPsoBJiN9e_p_AeDf0BsxnF4y6FWE5ChEHwWCJk12t1vssHOq9Dcb-C4sg3osA9uja7WlGHG1bMgxosWWuowsk2wQLRPcxUDtol-zKCLbA5L9KmNCIQm9T8TRwnJMw69Vf3W51uS5Hkqj-11lG1lNeeOO_yLT_EUQjz61tSz2781uzXsF15I2VUx0ZLddU7_UebNyW5Nm-YZVNdkjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efc791eac1.mp4?token=eGnj7MLcZETWc5yUd3Uq_fER27dvbfnxI6BYRtA_IzAYhoo1rknfoWJefi1gQZsnbEnwgoPTWw5auBdDsPsU8TtX6Zg4qDsaG-xnhqd2jJ9HdNY1cACTfbiwSH2XRcDiqH7-cPsoBJiN9e_p_AeDf0BsxnF4y6FWE5ChEHwWCJk12t1vssHOq9Dcb-C4sg3osA9uja7WlGHG1bMgxosWWuowsk2wQLRPcxUDtol-zKCLbA5L9KmNCIQm9T8TRwnJMw69Vf3W51uS5Hkqj-11lG1lNeeOO_yLT_EUQjz61tSz2781uzXsF15I2VUx0ZLddU7_UebNyW5Nm-YZVNdkjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حظور قیصر خواننده
لس آنجلسی در جشن غدیر
🥴
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/13502" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13501">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/13501" target="_blank">📅 19:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13500">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">داداش این خاننده دوزاری لس انجلسی که اوردن ایران پشت پردشو تو باید بدونی دستت تو موزیکه
پتشو بریز بیرون این عرزشیا عر عر نکنن</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/13500" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13499">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرنگار بین المللی امور خاورمیانه:
من کاملاً مطمئنم که اسرائیل در مقطعی به بیروت حمله خواهد کرد،
زودتر از آنچه فکر می‌کنیم،
سپس ایران پاسخ خواهد داد و آتش‌بس پایان خواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/13499" target="_blank">📅 19:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13498">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس با اسرائیل را رد کرد
شبکه المنار حزب‌الله ،گزارش داد که دبیرکل حزب‌الله لبنان گفته است که این گروه از جنوب لبنان عقب‌نشینی نخواهد کرد.
نعیم قاسم در این بیانیه گفته است درخواست این توافق مبنی بر خروج نیروهای حزب‌الله از جنوب لبنان، در شرایطی که این منطقه زیر آتش قرار دارد، به معنای "تسلیم شدن، شکست و تحقق اهداف دشمن" خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/13498" target="_blank">📅 19:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13497">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وای‌نت: موساد در اقدامی با هدف سرنگونی جمهوری اسلامی، سلاح‌های ضبط شده از حماس و حزب‌الله رو به کردهای مخالف جمهوری اسلامی داده بود.
سازمان اطلاعات مرکزی آمریکا، سیا هم در طرح استفاده از نیروهای کرد به‌عنوان بخشی از تلاش گسترده‌تر علیه حکومت ایران مشارکت داشته. این طرح در نهایت پس از فشار رجب طیب اردوغان، رییس‌جمهوری ترکیه، و در پی هشدارها درباره خطر گسترش درگیری منطقه‌ای، از سوی دونالد ترامپ لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/13497" target="_blank">📅 18:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13496">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9fpnspHUKk96FFruDsl0-h62FbYkzAMgpFypdjac7IWqHFVh-4jt4G9fY48VoFIKSBbFIZCWqaDxOD8orVafLnKK9tUfholg5OnJIk3StoVFOFVsiu-i0-6EpOyUOfnEPWArIyTIukGClI3bm0IT9vRvZAYPQ2ygA1bAxiafBYF51iU95U1WUZrQ0DcqH7ndbPTh2eWZLYz26iLGn6szJ_ntoFp3puC3pr3TZMXeUhIyJbePcV-JB7Tx8-qPYrfNeR1k75zhsX9jGhWzFmliqgH6QGW2es7mqenddEnZTBwVlO3VUFYg7sDX5XtjKM2G1uAUaITlcUDyzodpZ30qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای کاتولیک یک جن‌گیر را پس از ارتباط دادن مشاهده‌های یوفو با فعالیت‌های شیطانی برکنار کرد،.
جن‌گیر مشهور و قدیمی کاتولیک، استیون روزتی، گفت به باور شخصی او بسیاری از مشاهده‌های یوفو ممکن است ماهیتی شیطانی داشته باشند ! وی علاوه بر آن روان‌شناس نیز هست. به همین دلیل وقتی او درباره یوفوها صحبت می‌کند، سخنانش بیشتر از یک فرد عادی مورد توجه قرار می‌گیرد
اسقف‌نشین کاتولیک واشینگتن این اظهارات را مغایر با رویکرد رسمی کلیسا دانست و روزتی از سمت جن‌گیر رسمی برکنار شد و همکاری کلیسا با مرکز معنوی او نیز قطع گردید.
روزتی بعداً عذرخواهی کرد و بر تبعیت از آموزه‌های رسمی کلیسا تأکید نمود.
این ماجرا بحث قدیمی درباره ارتباط احتمالی یوفوها، موجودات فرازمینی و پدیده‌های ماورایی را دوباره مطرح کرده است
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/13496" target="_blank">📅 18:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13495">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLMR7J7ZFncY-z2BVXT2qMsbRrSj-qpOZqzM2vXSkyqJ1sc5GawmLa5JNQZd0nZPiKFQp8zCXn8o1KET3H0gEaIYCNIjGiMWOPsVnn-VQ7fzyExdv5zH0g8dG_7Aa60xlJAoc6ampkS9aCZjqx6gz_Pn8bxPNVw4jiDZACRxeX_PNF3nCJbK6ofT7lJd66lJ_JoT3mf4_y_fR6C5bZZHwZ-eJAg6qaNjAW5Ii4Aoo3n_jNYEGK7ehF0wJD2u95CzYocW-RGSujsbndCHQQWX8o52GskOxLauQtafMs3oytg-TmdxGvFLydMB4VR1nN4dD8SOgA84BwpOePmeIKwjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم رو بردن تحویل بدن
🤣
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/13495" target="_blank">📅 17:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13494">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سپاه: اسرائیل فورا حملات خود را متوقف و از مرزهای اشغال‌شده لبنان عقب‌نشینی کند
هیچ آرامشی در منطقه بدون عقب‌نشینی از مناطق اشغالی لبنان برقرار نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/13494" target="_blank">📅 17:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13493">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اصلا جان بر کف و جان فدا برای ما بود اونا گرفتن
😃
🤣
اون عرزشی ها کپی‌کارن زبان فارسی‌هم میراث ما هست نه اونا ، شاهنشاهی هم میراث ما هست لغت شاه هم کل دنیابگین میگن شاه ایران !</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/13493" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13492">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مردم به ایلان ماسکم دیسلاک دادن موشک هوا کرد
😁
شما توجه نکنید پیشنهادم به بعضی ها اینه که یک جعبه شیرنی‌بگیرن و با خودشون آشتی کنند</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/13492" target="_blank">📅 17:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13491">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3A0ioUuqxgY12qZzgT5qU_fHHfvXI_4-QQFKEgLdWnGWRSpmzAmUKEVlRkwmB4s0Zz2ejtK6wSpmDA2QftHNARUJk35_EWncHT2H2fC9n5yaCaUZsDPnDF22wxP4AjgRdPEhYVh9uKvcf_30QV6LNePWbZa1-lwwjjydPm1HwP7aWPdi3ErNMiRVh5yp8nBuJy598JMA4Fibq88-sTZNDuQeL2S4RatnhwArMHEzg_ckeOgJAUYqv-RmycankJeY2lnqMs4plDsfrZuUD91lxx0nu5q3EBAvgbhc1AYLzja8ZjrGTqp_UEXEl3MRbhnSlrVbIirv4QW0ipTqUFlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا شاهزاده گفته جانفدا!!! جاویدنامان باید میگفت</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/13491" target="_blank">📅 17:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13490">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🌹</strong></div>
<div class="tg-text">چرا شاهزاده گفته جانفدا!!! جاویدنامان باید میگفت</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/13490" target="_blank">📅 17:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13489">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bf81edef.mp4?token=EpsraJuwgD76XbCCFbCALKKIyEukVo1QnjEjBOSrECOboWUGR-GCRuFDFLxSwzysKSzGeO9hY-7vgf1tfy5P-nemshfvpkH1ftLE1qiXPaYsjEAiis_nRWZrIUxC81jyvQnSdbYoFJz67P1bsHJpYi6YwKtpSRWfZdw3vhhCIQbFvAT6qwjvfRPzSu4sh4Cejzdl5nLDDXsuQ7Wa3MP43O36RxwBl4p_Gn3CsPPRiSZvwEApksjBJ71JYqqjNhxPST3lPuKh_dRVgPBWWmuSrrUBBozcJbp2PnZ2lD_lobLaTM0Yn7K_LiOfXPX_zkBWDyjJK_oUxZCia_9zahzkGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bf81edef.mp4?token=EpsraJuwgD76XbCCFbCALKKIyEukVo1QnjEjBOSrECOboWUGR-GCRuFDFLxSwzysKSzGeO9hY-7vgf1tfy5P-nemshfvpkH1ftLE1qiXPaYsjEAiis_nRWZrIUxC81jyvQnSdbYoFJz67P1bsHJpYi6YwKtpSRWfZdw3vhhCIQbFvAT6qwjvfRPzSu4sh4Cejzdl5nLDDXsuQ7Wa3MP43O36RxwBl4p_Gn3CsPPRiSZvwEApksjBJ71JYqqjNhxPST3lPuKh_dRVgPBWWmuSrrUBBozcJbp2PnZ2lD_lobLaTM0Yn7K_LiOfXPX_zkBWDyjJK_oUxZCia_9zahzkGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایت شهبازی از کار
😂
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/13489" target="_blank">📅 17:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13488">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohamad Jalilzadeh</strong></div>
<div class="tg-text">اقا ری اکشن کوچکترین تمرین هست برای پذیرش دموکراسی
وقتی یه عده همه ش دنبال کم و زیاد کردن ری اکشن هستن و دنبال اینن که کی چه ری اکشنی زده در آینده ی ایران چطور میخوایم همدیگه رو تحمل بکنیم و باهمدیگه حرف بزنیم؟
همه ری اکشنا باید باز باشه و کاملا مخفی</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/13488" target="_blank">📅 16:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13487">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شاهزاده رضا پهلوی : مسابقات جام جهانی فوتبال فرصتی کم‌نظیر برای رساندن صدای ملت ایران به جهانیان فراهم می‌کند. از این فرصت تاریخی بهره بگیریم؛ پرچم شیر و خورشید را در ورزشگاه‌ها، خیابان‌ها و میدان‌های شهرها به اهتزاز درآوریم و تصاویر جان‌فداییان راه آزادی…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/13487" target="_blank">📅 16:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13486">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چند گزارش ساعت ۱۵:۵۴ دقیقه محدوده شمال شرق تهران همچنین نیاوران صدا پدافند شنیده شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/13486" target="_blank">📅 16:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13485">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شاهزاده رضا پهلوی : مسابقات جام جهانی فوتبال فرصتی کم‌نظیر برای رساندن صدای ملت ایران به جهانیان فراهم می‌کند. از این فرصت تاریخی بهره بگیریم؛ پرچم شیر و خورشید را در ورزشگاه‌ها، خیابان‌ها و میدان‌های شهرها به اهتزاز درآوریم و تصاویر جان‌فداییان راه آزادی را در برابر چشم جهانیان قرار دهیم.
@withyashar
وی به این موضوع که ورود پرچم ما به ورزشگاه ممنوع است و چه راهکاری باید داشته باشیم اشاره نکرد.</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/13485" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13484">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjF2DDd-mLqRP8cb4LepUX8qDo6Fw9KALgZA8y22gzmWqy8_t-W78r1dvcJTjCYRNE9bImO7kEpJgTB0AlmqA8tqd5cozE6qgKIg1LAxDG6TYDc21HzjZpWgttLe80p_o4kbrqQrx_u-NXeU0-2E_emwjNW9aUb0rQnRV5tAAnS4DQDqnGdaW9m9bmpRuzMsgAgiCc9aYt0DzsOPZpfRj1hpc1rrD0GpeB_DgskFgRK5gn9b_VhhRiMd64ZBkHrVQwiHc_Z1jylBe9-miwNNn3_RXyD2IjHzxEHRaj7UhweCSCr-ZFYYUtRn6A8WbwCQlgb9hbQWaR6MMXu4tQ7eOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : سازمان تروریستی حزب‌الله گلوله‌های خمپاره‌ای شلیک کرده که به یک موقعیت نیروهای سازمان ملل اصابت کرده و در نتیجه یک نفر از کارکنان سازمان ملل در جنوب لبنان کشته شده است
شلیک‌های حزب‌الله نیروهای بین‌المللی را در معرض خطر قرار می‌دهد و به کارکنان سازمان ملل که در منطقه فعالیت می‌کنند آسیب می‌زند
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13484" target="_blank">📅 16:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13483">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نعیم قاسم، رهبر حزب الله: نتیجه مذاکرات دولت لبنان با اسرائیل شرم آور و پوچ است و اونو بطور کامل مردود اعلام میکنم.
تا زمانی که تجاوز ادامه داره به هر جایی که تصمیم بگیریم و بتونیم حمله می‌کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/13483" target="_blank">📅 16:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13482">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: در وسط مذاکرات پایانی برای پایان دادن به جنگ هستیم
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/13482" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13481">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCzNpLxL332Axl9nV37nCVzFWclkjVa4_NoH_I05gZqNyH3YZ0O8ohR3eJs7E_OOzRxEXXm_iiFPdAephcJb_q_Om1Wo1IOOlyiDpGaxe6tF7MgheoqklzzH1XyhYNl8FzECHvjesdWljPgGjPrHQdFRKvhnadBJkT8zwZrKZVdPh528b6GVAEdb1id9sgPoiCTrOEfBrk7I7Q5UoDz_OFZKa12UeQAgd-WH5Ksuf7jWODXiLpTdPXlWH61zHhIygyC1R3EhwM5BqZcuCN3DHO2Xsv6h932QqnRYvGGGGC9RnsvPV_L-RFtTVRdmFvcOFCdPSrQRopnRLRXhidCoNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عکسی از نشان‌هایی با نماد جمجمه به سبک ترامپ منتشر کرد
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13481" target="_blank">📅 15:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13480">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiQZ6oITSKi1rSukBHbPNKVaE6_v_Wf5z7XjeD4USnt5QEnUQq8XR-UeEyJMtOS-k3Hp8tuI6jUc3-a9g-ooFD84UCU0-EG0RY2H1l8Rimk-1Fp2lg1DGuauz7xfFoXHKcwGBrB-dGlzTKmaXm1K0VHKqKX3NB2ftYdpRU_JUss3mxMURvmqGAiv0lPWm5SvgRFFMZN-uGIcAI0ZxJg0KDeTGCs-doU_TeOuy4Sxbwtajj-HAeCYT9-7SR833CnFq-_jK-3g4eBMTYghomD-E8ixZF23sJdd_uBArRt1cb5mL4yhk2phKPkUilF-xF0i2fp-f3D4dZOiG8faqWJRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیروز، در یک رأی‌گیری بی‌اهمیت، مجلس نمایندگان با رأی ۴ جمهوری‌خواه بد و همه دموکرات‌ها، تلاش کرد اختیارات جنگی من را محدود کند؛ درست در میانه آخرین مذاکرات من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟ آن‌ها می‌دانند وضعیت مذاکرات در چه مرحله‌ای است. دموکرات‌ها با چیزی به نام «سندروم جنون ترامپ» هدایت می‌شوند. آن‌ها ترجیح می‌دهند کشور ما شکست بخورد تا اینکه من یک پیروزی دیگر از میان پیروزی‌های بسیارم به دست بیاورم. آن چهار جمهوری‌خواه، ماجرای دیگری دارند آن‌ها اهل خودنمایی هستند! باید از کار خود شرمنده باشند.
MAGA!!!
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13480" target="_blank">📅 14:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13479">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد. @withyashar
😟</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/13479" target="_blank">📅 14:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13478">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اکسیوس :  یک شکاف رو به رشد بین ترامپ و نتانیاهو در مورد آینده منطقه در حال شکل‌گیری است.
بر اساس گفته مقامات آمریکایی، ترامپ می‌خواهد تنش‌ها را کاهش دهد، درگیری‌های جاری را پایان دهد و به دنبال یک توافق دیپلماتیک با ایران باشد.
در مقابل، نتانیاهو به نظر می‌رسد تمایل بیشتری به حفظ فشار نظامی بر ایران و متحدانش، از جمله حزب‌الله، دارد.
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/13478" target="_blank">📅 14:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13477">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فیلم جدیدی که حمله هوایی آمریکا به پل B1 در کرج، ایران، را در طول جنگ نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13477" target="_blank">📅 13:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13476">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال ۱۳ اسرائیل: «کابینه امنیتی اسرائیل امشب ساعت ۱۷:۰۰ تشکیل جلسه خواهد داد»
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/13476" target="_blank">📅 13:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13475">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وال‌استریت ژورنال : آخرین پیشنهاد ارائه‌شده از سوی ایران نتوانسته رضایت کامل دولت ترامپ را جلب کند و هنوز اختلافات اساسی بر سر برنامه هسته‌ای، سرنوشت اورانیوم غنی‌شده، رفع تحریم‌ها و آزادسازی دارایی‌های ایران باقی مانده است.
وال‌استریت ژورنال تأکید می‌کند که تماس‌ها و تلاش‌های دیپلماتیک همچنان ادامه دارد ، ترامپ همچنان به دنبال توافقی است که از دید او برنامه هسته‌ای ایران را به‌طور مؤثر محدود یا برچیده کند. در مقابل، ایران خواهان امتیازهایی مانند آزاد شدن بخشی از دارایی‌های مسدودشده و کاهش فشارهای اقتصادی پیش از پذیرش محدودیت‌های گسترده‌تر است.
اما مذاکرات هنوز زنده است و کانال‌های ارتباطی بسته نشده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13475" target="_blank">📅 12:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13474">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وال استریت ژورنال:
«ترامپ به مشاورانش گفته است که جنگ تمام‌عیار با ایران را از سر نخواهد گرفت، مگر اینکه نیروهای نظامی آمریکا کشته شوند.»
مقام‌ها می‌گویند حملات مکرر ایران فشار بر رئیس‌جمهور را افزایش داده و تردیدهایی درباره دوام بلندمدت آتش‌بس ایجاد کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/13474" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13473">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انتقاد مارک لوین از تصمیمات جدید ترامپ:
جمهوری اسلامی شاید نیروی دریایی و نیروی هوایی قابل ‌اعتنایی نداشته باشد، اما همچنان سپاه پاسداران و یک رژیم ایدئولوژیک دارد که شکست نخورده است؛ ما ملت ایران را برای سرنگونی رژیم مسلح نکرده‌ایم. رژیم کماکان در حال شلیک موشک های بالستیک و پهپاد ها است و هنوز مشخص نیست این تبادل آتش بخشی از مذاکرات است یا نه؛ هرچند در نهایت، چنین مواردی قابل راستی‌آزمایی نخواهد بود.
به نظر میرسد ما از نابود شدن سازمان حزب‌الله لبنان ممانعت می‌کنیم؛ حزب‌الله، قدرتمندترین نیروی نیابتی رژیم ایران میباشد که در 40 سال گذشته آمریکایی‌ها را کشته است؛ همچنین حماس به جای خلع سلاح، در حال تجدید قوا است.
این وضعیت برای آینده و پس از پایان دولت ترامپ، نشانه خوبی نیست. من فکر نمی‌کنم چین کمونیست که بزرگترین تهدید برای ما است، تحت تأثیر قرار گرفته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/13473" target="_blank">📅 12:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13472">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9960590f00.mp4?token=F_WpJNqEZEtR72j_S_e-o940Tqh021-3pFdrmN8iZ1rCoXJTey1m9NOjaZ2CCT1TJD9__BTuYYFCi2Y4l4jVxaQN2r4YtFL2B5NyDhF-M5lZdfPWlZEQlbTI5kvHUZYUNTbSueh2ctfamEhhsEUgRzo-3egXaEs6t1uwEFplULduPo3LbqtuTjcnoq1zAa2UIPYonVZplPc9rnfoH6qPMSJYlfGsCrmzlp2eJkHiNVZX61dYkO8V4TMWLSXLpjpOAVdVVdYR-OrfHpGYyGJRw5SQcWJx4o_39ZPqrOEGJiH26MTw2504SxxJG_h0Nh-1p38SD-M9HaFKS9TZ_DaKvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9960590f00.mp4?token=F_WpJNqEZEtR72j_S_e-o940Tqh021-3pFdrmN8iZ1rCoXJTey1m9NOjaZ2CCT1TJD9__BTuYYFCi2Y4l4jVxaQN2r4YtFL2B5NyDhF-M5lZdfPWlZEQlbTI5kvHUZYUNTbSueh2ctfamEhhsEUgRzo-3egXaEs6t1uwEFplULduPo3LbqtuTjcnoq1zAa2UIPYonVZplPc9rnfoH6qPMSJYlfGsCrmzlp2eJkHiNVZX61dYkO8V4TMWLSXLpjpOAVdVVdYR-OrfHpGYyGJRw5SQcWJx4o_39ZPqrOEGJiH26MTw2504SxxJG_h0Nh-1p38SD-M9HaFKS9TZ_DaKvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری نیویورک پست
: آیا آیت‌الله (مجتبی خامنه‌ای) همجنسگرا است
ترامپ: بله.
مجری
: واقعا
دونالد ترامپ: بله، و فکر میکنم خیلی احترام براش قائل هستند.
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13472" target="_blank">📅 12:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13471">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">در مراسم سی‌وهفتمین سال به درک رفتن روح‌الله خمینی، پیام کتبی منتسب به مجتبی خامنه‌ای خوانده شد. در این پیام آمده است «نظام سلطه پادگانی به نام اسرائیل از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.»
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/13471" target="_blank">📅 11:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13470">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/13470" target="_blank">📅 11:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13469">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مجتبی خامنه‌ای: هدف دشمن اینه فشار اقتصادی بیاره تا مردم ناامید بشن، مردم باید مقاومت کنن تا به قله برسیم
@withyashar
🥴</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/13469" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13468">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ممد امین میمندیان، نویسنده پاورقی :  شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.  برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود @withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/13468" target="_blank">📅 11:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13467">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6sr7MM2GlfvRWUUSX2qHAjqXYOYCVrKKi9vuXHWLVtbstThVoZZ9-MLAWqFCa7RxRfFdNUxnjvaqly6ouvzuptf3YLMfznNSGgLAhOvSsu1EBk1lfhpFMa6xqvvZtZB2QQFcpZ3tmgA2cdp2QGy-w69Y3VlxcOXz0GExSG93H2vtEwaEBu-x3bSZ3VT4UKCwgR5r8ovSXm2KFRzhRC6OBvPWENBJORv9CIXrxO2HzjPUlJpi38076Vuntbk-aE7tFKQ_qyoOjH7LkWTcoYCuBefl2SbuuCp0OJ_qE24SlkMaJx23RA62vEpEC21WP1KTiC275u2GrIgx6OVLopX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور پهپاد شاهدی که به فرودگاه کویت برخورد کرد پیدا شد
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13467" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13466">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزیر دفاع اسرائیل: به هدف قرار دادن زیرساخت های حزب الله در لبنان ادامه خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/13466" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13465">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY4-xLjhKk4DYabcDz4zt7HCIgiz0Bw_64FjzBxwu9JqC1NGf91vstjY40L5Mn_Gf1h8YMWt9Qbny1_ybkxSk50WnbuNDEYfxykmcQeHLbaMGs4wJjRUnmXlWloNpajWoUU5yTFvSxe8B4hdwHPyo1x4iYZCLmcllvFZLktnP9hFrz4NFL9ZXpPzg9rPlIHRStsXcsItJ3GKm3OPW44Iu0k_a_iXcv_SrRir9Abhv95Dy6C10cj3i5bbc2m7bL5FlW_9HTrYPQHVbYo-vQNix1OCY491I7uArxDbx3Q810131LPeZfsQTjdsyTSFozYd_2U_nqxBsHv3rjDj02XuUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای Falcon 900EX متعلق به دولت ایران در حال پرواز بر فراز دریای خزر به سمت روسیه است. این هواپیمای خاص توسط مقامات ارشد ایرانی استفاده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/13465" target="_blank">📅 11:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13464">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مقام اسرائیلی: ایران تصمیم گرفته در صورت آزادسازی اموال بلوکه‌شده‌‌اش، بخشی از آن را به حزب‌الله اختصاص دهد.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/13464" target="_blank">📅 09:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13463">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جنگ ترامپ با ایران و اختلال در حمل و نقل نفت از طریق تنگه هرمز، ذخایر نفتی آمریکا را به پایین‌ترین سطح خود از سال ۲۰۰۴ رسانده است.
برای کمک به مهار افزایش قیمت سوخت، آمریکا میلیون‌ها بشکه از ذخیره استراتژیک خود را آزاد کرده و همچنین صادرات به اروپا و آسیا را افزایش داده است تا جایگزین عرضه از دست رفته خاورمیانه شود.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/13463" target="_blank">📅 09:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13462">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=FouQ2lMQ68C2PekeK_sniRlDmCThP7udtwWG6d9gfpMvRR0QyvHlbs64ATKN13QXNgaougIgypbvIHwpDVeSv_2tXqpQURUSlcHw36XYjYeLswXMMLbU-j-ylkLOjbMRiwYuExCNX_4p1dEo17CoUouKCn5-hJcAXkZn9HJgoZvJ1LItGx12vIUR9GiVczKXDgRbyvfRxQbXTJ1wEoCIsHXgSCgmT6a-5cjhWyol4eyaxzEgxSCzOdekoAG1eLJ8ioTSKMDRd2Q2l2Hn7hKCwpsEQ1rpWNMg0V7ExCUkA2j23XQe1vMKxMvWY6iYmhcI946Pp7ya7LQc713gAxs8wp7ZC3jryC1tyjBD5DyQi0BuaGUH7B7_zhVlZ_XedxZ15S0JHlnWefDU3Bofaquph99Yq8b7q83JUYTfDiCajTXdaetW3BsGagdG36xSGA9L-_TkaVJy52HDWTMtXPWar-hzkzzTWFgoEeqi17uiXFgF42gYNhYHciWRjwRecdu6zGUBntHg7OpZG5ZiZlRQM07uDpt3SM2td7ECB2dyLB0AcqicFHYVLwiZp03Efl0TPWr3vu3rLr7PoGxqs7skiGiFUwpyA8vQW39tyZ5dFQ_36j9ONlu5m-2dSVVsn9ZhfYNQRIaTG3CC5vpx8NMWaVCcQRDcXFZW46Y55NIX62o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=FouQ2lMQ68C2PekeK_sniRlDmCThP7udtwWG6d9gfpMvRR0QyvHlbs64ATKN13QXNgaougIgypbvIHwpDVeSv_2tXqpQURUSlcHw36XYjYeLswXMMLbU-j-ylkLOjbMRiwYuExCNX_4p1dEo17CoUouKCn5-hJcAXkZn9HJgoZvJ1LItGx12vIUR9GiVczKXDgRbyvfRxQbXTJ1wEoCIsHXgSCgmT6a-5cjhWyol4eyaxzEgxSCzOdekoAG1eLJ8ioTSKMDRd2Q2l2Hn7hKCwpsEQ1rpWNMg0V7ExCUkA2j23XQe1vMKxMvWY6iYmhcI946Pp7ya7LQc713gAxs8wp7ZC3jryC1tyjBD5DyQi0BuaGUH7B7_zhVlZ_XedxZ15S0JHlnWefDU3Bofaquph99Yq8b7q83JUYTfDiCajTXdaetW3BsGagdG36xSGA9L-_TkaVJy52HDWTMtXPWar-hzkzzTWFgoEeqi17uiXFgF42gYNhYHciWRjwRecdu6zGUBntHg7OpZG5ZiZlRQM07uDpt3SM2td7ECB2dyLB0AcqicFHYVLwiZp03Efl0TPWr3vu3rLr7PoGxqs7skiGiFUwpyA8vQW39tyZ5dFQ_36j9ONlu5m-2dSVVsn9ZhfYNQRIaTG3CC5vpx8NMWaVCcQRDcXFZW46Y55NIX62o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد.
@withyashar
😟</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/13462" target="_blank">📅 01:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13461">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=qrcZKYHZ1nXPiaH9tt3RDJ6Q9u-qLTLMpCgpFGJAWwrUXtU2yOtPW-SuXki2L_CpLvZXsywOX-3tevJq4iucAyWDCnz1opYrcjCEYu04jWDK7mXPr7KuaQ8wzOTyh36Iud_WLr481ROUHJTLdiCh9SxdKIFYecEkO0qtFBu43o5PDZmt5WHwgwmOspNBmjGz_is3PKXD2-3gASF3jZW-SWjRjhkX1J0_gnrUftkuRFH6ShoMWDlQ3dPyH4rrqRQTMnGEd-IywB-RJ-b_xkddgRbiatAOkcMvJQfJjAo2avYhjPvqLXSR757NYOV1rZ7vJxf24Fp_pxW93zobhHg6tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=qrcZKYHZ1nXPiaH9tt3RDJ6Q9u-qLTLMpCgpFGJAWwrUXtU2yOtPW-SuXki2L_CpLvZXsywOX-3tevJq4iucAyWDCnz1opYrcjCEYu04jWDK7mXPr7KuaQ8wzOTyh36Iud_WLr481ROUHJTLdiCh9SxdKIFYecEkO0qtFBu43o5PDZmt5WHwgwmOspNBmjGz_is3PKXD2-3gASF3jZW-SWjRjhkX1J0_gnrUftkuRFH6ShoMWDlQ3dPyH4rrqRQTMnGEd-IywB-RJ-b_xkddgRbiatAOkcMvJQfJjAo2avYhjPvqLXSR757NYOV1rZ7vJxf24Fp_pxW93zobhHg6tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
با این حال، این اولین رای موفق مجلس نمایندگان است که قدرت‌های جنگی کنگره را در مورد جنگ ایران تأیید می‌کند و اقدام نظامی آینده بدون تأیید کنگره را محدود می‌سازد.
چهار جمهوری‌خواه به نفع آن رای دادند.
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/13461" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13460">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">داداش اون بحث خیلی طولانیه اون میشه زمان ریست فکتوری طوفان بزرگ ( که با داستان خیالی نوح میشناسید ) تا اینجا بدون که قبلش تمدنهای بسیار پیشرفته بود روی زمین ، باشه برای بعد از آزادی
😂</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/13460" target="_blank">📅 01:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13459">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from00:30</strong></div>
<div class="tg-text">درود ولی من‌میرملاس لرستان رفتم اونجا دیوار نوشته هست‌مربوط به 12000 سال پیش</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/13459" target="_blank">📅 01:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13458">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یاشار : دمت  آقا دایی ، مردی ، خواستم تکمیل کنم که عدد
۲۵۰۰ سال
به طور مشخص به
سابقه پادشاهی شاهنشاهی ایران
اشاره دارد، نه به کل تمدن ایران ،
تمدن در فلات ایران ۵۰۰۰ الی ۷۰۰۰ سال حتی بیشتر سابقه دارد
@withyashar
😁
🙌🏾</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/13458" target="_blank">📅 01:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13457">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
‏ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/13457" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13456">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دو منبع مطلع در مذاکرات به i24NEWS عبری:
مذاکرات بین آمریکا و ایران به دلیل اصرار ایرانی‌ها بر آزادسازی پول‌ها، «پول نقد»، از میلیاردهایی که مسدود شده‌اند، حتی در مرحله اول، متوقف شده است .
در روزهای اخیر، میانجی‌ها تلاش کرده‌اند در این موضوع مصالحه کنند اما ایرانی‌ها بر دریافت پول در همان مرحله اول، در چارچوب توافق کلی، قبل از انجام هر اقدام واقعی در میدان، اصرار دارند.
مقامات ارشد آمریکایی تأکید می‌کنند: در ابتدا پولی آزاد نخواهیم کرد مگر اینکه ایران گام مهمی در مسئله هسته‌ای و هرمز بردارد و همچنین توافق کلی بسیار معنادارتر باشد.
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/13456" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13455">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naNxbzXoVcl2UYTXQCe5pj_GmnRdQZNUJSnpS-Fl37hIxQcns8csiateRUCsgjMNP7MqCp4M9eoeLTdpMzj8toetx6R02keBwEvaAyNunpFBPAlTb8sbHSurHFIVtGLSRkWwSmrwYjTgBJdkZDYCvJnWwzrDnuIB-8U1eDkgg2naGBJiNjTOloCZREoGiEntKzc9-CdWzrkPEHAzkO5ncYyCj38vBEYjd6vCi7scTZQRN-pLo2Tg2ITCNosr4FqRNz_9NupAUmArPnkp4h-I5v9Iizl0k6gA_Z_vWnf6PtBAIrLeZs_ZW6O0pEnj70Iqnfstr5yIAcPYwzzknolFjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات آمریکا
جمشید قومی
، شهروند دوتابعیتی ایران و آمریکا و مدیرعامل شرکت «فرار پرداز رایانه» در تهران را به نقض تحریم‌ها متهم کرده‌اند. طبق ادعای دادستانی، او طی بیش از یک دهه تجهیزات شبکه، امنیتی و رمزنگاری ساخت آمریکا را از طریق واسطه‌هایی در دبی به ایران، از جمله سازمان انرژی اتمی و وزارت دفاع، منتقل کرده است. همچنین متهم است حدود ۱۵ میلیون دلار درآمد حاصل از این فعالیت‌ها را به آمریکا منتقل کرده و با آن یک عمارت ۳۵ میلیون دلاری در کالیفرنیا ساخته است. در صورت محکومیت، با حداکثر ۲۰ سال زندان فدرال روبه‌رو خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/13455" target="_blank">📅 00:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13454">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">منابع العربیه: پیشرفت‌هایی در مذاکرات لبنان و اسرائیل حاصل شده است، اما هنوز توافق دائمی به دست نیامده است
اختلاف بر سر سلاح‌های حزب‌الله همچنان مانع اصلی هرگونه توافق بلندمدت است
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/13454" target="_blank">📅 00:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13453">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ:
ما در واقع برای اولین بار با حزب‌الله صحبت کردیم. نمی‌دانستیم آن‌ها صحبت می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/13453" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13452">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ : تنگه هرمز فوراً باز می‌شه وقتی من یادداشت تفاهم رو با ایران امضا کنم
تنگه هرمز باز خواهد شد، مین‌روب‌هامون اونجاست
زیر آب هستن، خیلی خوبن، تکنولوژی‌شون فوق‌العاده‌ست
ما مین‌ها رو جمع کردیم، بیشترش رو پاکسازی کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/13452" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13451">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستان خواهش میکنم دایرکت جای کامنت دادن به مطالب نیست
😟
خدایا به چه زبونی بگم ؟ بفرستید برای دوستون و باهاش‌چت کنید ، به بچه آدمیزاد چند بار میگن</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13451" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13450">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرنگار
: شما هفته قبل گفتید آمریکا می‌ره داخل و مواد هسته‌ای دفن‌شده رو در هماهنگی با ایران بیرون می‌کشه. آیا ایران واقعاً با این موافقت کرده؟
ترامپ
: خب، بستگی داره داری درباره کدوم روز حرف می‌زنی. این چیزها خیلی هم بزرگ‌نمایی شده. من خودم هم اون رو یه‌جورایی بزرگ‌تر از واقعیت نشون دادم.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/13450" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13449">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a531a29092.mp4?token=Gy40Slc7fPxTF_BTsbiQqOrynSs7-hnFE2yOcuT4a8kTNEWeqYg-sFlTAV7wV5brH0gZK041OmNBxDDVeC26LKAjGT66B87Mo1UKHlNFHB_BxR-DJ_PmrtQBXecM8tXJP_KQqoUwbCEQ4FSyxjz0ZRQcRFKVF0NryZ2J1np987PtlO21865RB-COQ1qmuRGfbqnPYjkEMVEZrV5EGALe0OhVi1gF79rcwvqBOLGWzud20lmH9yJzsE6dNW3a-fSSx3Kms3rm7KDylHYP_Pl7-JoImR5HGgak-VtgdS2C010eSab17S9-8FIniPcwxZyNZ0QwgKIRh1yJp9jTf7Zm_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a531a29092.mp4?token=Gy40Slc7fPxTF_BTsbiQqOrynSs7-hnFE2yOcuT4a8kTNEWeqYg-sFlTAV7wV5brH0gZK041OmNBxDDVeC26LKAjGT66B87Mo1UKHlNFHB_BxR-DJ_PmrtQBXecM8tXJP_KQqoUwbCEQ4FSyxjz0ZRQcRFKVF0NryZ2J1np987PtlO21865RB-COQ1qmuRGfbqnPYjkEMVEZrV5EGALe0OhVi1gF79rcwvqBOLGWzud20lmH9yJzsE6dNW3a-fSSx3Kms3rm7KDylHYP_Pl7-JoImR5HGgak-VtgdS2C010eSab17S9-8FIniPcwxZyNZ0QwgKIRh1yJp9jTf7Zm_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما می‌توانیم دو یا سه هفته دیگر ادامه بدهیم و همه را از بین ببریم. انجام این کار خیلی آسان است.
اما اگر بتوانیم چیزی را روی کاغذ بیاوریم و مکتوب کنیم که بدون کشتن همه، همان نتیجه را به دست بدهد، ترجیح می‌دهم آن راه را انتخاب کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/13449" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13448">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=KGGNQGoY3vpI5AxYcEWKBxycv6mGOnzdv_fhFH2Z8KthOCgSYhxPX59omf-Er-s75F_U2wm_xq7yDEvvUGBtcsxUcqPOsYPRK5cRBdsvDiB7mNrmX7VOXq1DvpXW6aGSzuJB631wsMpb3LgvMQW8EHgYisU8OeWxoYvplnLK02NfNYuVacfuTOOaYpXAWA5abv9csMFJqGuks-mu0b_5Vn4jrUMtsLbxumOonR_AB30KPbz3P_WxpLyU8R8tO0WBhYSRxAz18gEsMRqmriKx3Pe8ihW-DAKvzuIH36ule_9o8WSYpBh0qmxtyTJ1b2U9MwEFnLN-LIGdwCw7SjPekg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=KGGNQGoY3vpI5AxYcEWKBxycv6mGOnzdv_fhFH2Z8KthOCgSYhxPX59omf-Er-s75F_U2wm_xq7yDEvvUGBtcsxUcqPOsYPRK5cRBdsvDiB7mNrmX7VOXq1DvpXW6aGSzuJB631wsMpb3LgvMQW8EHgYisU8OeWxoYvplnLK02NfNYuVacfuTOOaYpXAWA5abv9csMFJqGuks-mu0b_5Vn4jrUMtsLbxumOonR_AB30KPbz3P_WxpLyU8R8tO0WBhYSRxAz18gEsMRqmriKx3Pe8ihW-DAKvzuIH36ule_9o8WSYpBh0qmxtyTJ1b2U9MwEFnLN-LIGdwCw7SjPekg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در آن بخش از جهان«خاورمیانه»، آتش‌بس زمانی است که شما به شیوه‌ای معتدل‌تر تیراندازی می‌کنید.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13448" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13447">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درباره حمله ایران به کویت:
برای هر چیزی دلیلی وجود دارد، و ما به آنها ضربه‌ای سخت زدیم... آنها کمی تحریک شده بودند؛ آنها در حال پاسخ دادن بودند.
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13447" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13446">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ : مذاکرات عالی پیش میره
می‌توانیم جنگ را دو یا سه هفته دیگر ادامه دهیم و همه را نابود کنیم اما ترجیح می‌دهم این کار را نکنم
هر اتفاقی ممکن است برای ایران بیفتد، و رهبری ایران سه بار تغییر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/13446" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13445">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش انفجار‌ قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13445" target="_blank">📅 23:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13444">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:دیشب و پریشب به ایران حمله کردیم و ضربه سختی به آنها زدیم
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13444" target="_blank">📅 23:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13443">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXQUfwKiWWhfBqSutM_nhJM2-Hd0OhsNMD4Kb8kNl4n6Ddfa7uS-K5SjeGBTmllrsJj9EKt-wLUkqN0pDgNRgVOjxoYMwdx3KLRFMV_x9PYgMd9NX8F0kHpc66FWIdnQlnHA-4Ka02RwTjWByeH4UDcZEvI6JV0vD1-maDaEku58jMSM3s0yKowtR9Ihxx_wWqBJWNzhc_JAXrAoxOTTMyClSqePMTH5Vw1BNf_6eRwES-_3hqoTm3LvqWUXhL7bQ3tQjrArxYH4IqiMSWVTZxZAdajUxyc92CNsvucZp2F22HGDN4I0jm8Ow4wf54_EAm9L0E0Zhg57oGBt73yjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات بین اسرائیل و لبنان به زودی به پایان خواهد رسید. به زودی اعلامیه‌ای از سوی ایالات متحده منتشر میشه.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13443" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13442">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دفتر بازرس کل وزارت دفاع آمریکا در حال آغاز یک بررسی (بازبینی و تحقیق رسمی) درباره «عملیات خشم حماسی» (Operation Epic Fury) است؛ کارزار نظامی آمریکا علیه ایران که با هدف برچیدن تهدید هسته‌ای تهران انجام شد.
@withyashar
این آغاز یک بررسی یا بازرسی رسمی است، نه لزوماً افشای تخلف یا شکست.
Office of Inspector General (OIG)
نهاد بازرسی داخلی وزارت دفاع آمریکاست و معمولاً پس از عملیات‌های بزرگ نظامی، نحوه برنامه‌ریزی، اجرای عملیات، هزینه‌ها، تلفات، رعایت قوانین و عملکرد فرماندهان را بررسی می‌کند</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13442" target="_blank">📅 23:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13441">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پدافند شهریار فعال شد
🚨
@withyashar
اینو دیگه دوستم اونجاست و وارده</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13441" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13440">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnqKvx1FK_KaiEwiYzt6oEcEVRWy-z2lpUWZnsr9T7SolExddCPbWf3eY4OhxtrYqWK8cz8gjNfmd0rH75CsdQc-dFq7WIK2BZmQigOLRk9_FEAUzpGfhB2zDPl2Dw_xZPosdodaujo6AM3ZbfgvAmyHYrcOyMWbSIUQNFEvdkFIJT80ja372srW63Ewbll8ylVc2BSQFjQ5k3DtaGMBglJArLXnWRJZ8cSfjIkpF-1kIJpNaf7e-kgsrLtoQUN3G1F8wkhi67lYNUjC9BuoUag44z8gA5yLzvcAP8rWEtM49c8pZKafwmXPPLpSUrdTIyVhmrWFSvd0aPD3MHUofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بلافاصله پس از یکی از سرگرم‌کننده‌ترین شب‌های تاریخ آمریکا، یعنی مسابقات قهرمانی جهان UFC در چمن جنوبی کاخ سفید، به اجلاس گروه ۷ در فرانسه خواهم رفت. سوابق نشان می‌دهد که اگرچه در طول تاریخ طولانی و پرماجرای کاخ سفید، مبارزاتی در سطح بسیار پایین‌تر در این کاخ برگزار شده است، اما هیچ رویدادی حتی نزدیک به این، یعنی بزرگترین مبارزان جهان، قهرمانان جهان، برای مجلس عوام در نظر گرفته نشده است! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/13440" target="_blank">📅 23:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13439">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزارت کشور بحرین به دلیل خطر احتمالی آژیر خطر را فعال کرد و از شهروندان خواست به نزدیک‌ترین مکان امن بروند.
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/13439" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13438">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیروی دریایی جمهوری اسلامی ساعتی پیش یک ناو جنگی آمریکا را در دریای عمان هدف قرار دادیم @withyashar
🚨</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/13438" target="_blank">📅 23:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13436">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رویترز: رسانه‌های ایران گزارش دادند که تهران به یک کشتی نظامی آمریکایی که ادعا می‌شود حامل «مرکز فرماندهی و کنترل» بوده، هنگام نزدیک شدن به آب‌های سرزمینی ایران در خلیج عمان حمله کرده است
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13436" target="_blank">📅 22:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13435">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c287d7f770.mp4?token=IhtNDMugs-hhVo9SgQvcX3noTpkSJPOw9ko407tWpCK0jdwuWVSG-D9indmdy1h4ikDAmnXmH-iQRNAV759XN0LTWZozr1bT8MXaBsr4j6_S-gm45VASTIufDflJFiil2DV7pkH9twGYoX4-iWoJmOgqXufg7b3eAtfjc6DPHfQloSDqZN4XxwZZJdC4gcbWB3mvVB4Jwm4dyLcZCchHw7D_92-dFSgqu34kSL3yMoiE4CRIQ6_pWgkNNvda2oXQwPujsFlnbIJExcI1aWKsZzkkB_6iI-iZmB_2nYO1QsXl65TIu0R9bZp_FoMsKOJbOJsvinntH71RzkK1wNNGIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c287d7f770.mp4?token=IhtNDMugs-hhVo9SgQvcX3noTpkSJPOw9ko407tWpCK0jdwuWVSG-D9indmdy1h4ikDAmnXmH-iQRNAV759XN0LTWZozr1bT8MXaBsr4j6_S-gm45VASTIufDflJFiil2DV7pkH9twGYoX4-iWoJmOgqXufg7b3eAtfjc6DPHfQloSDqZN4XxwZZJdC4gcbWB3mvVB4Jwm4dyLcZCchHw7D_92-dFSgqu34kSL3yMoiE4CRIQ6_pWgkNNvda2oXQwPujsFlnbIJExcI1aWKsZzkkB_6iI-iZmB_2nYO1QsXl65TIu0R9bZp_FoMsKOJbOJsvinntH71RzkK1wNNGIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی جمهوری اسلامی امروز ویدیویی منتشر کرد که نشان می‌دهد ساعاتی پیش موشک‌های ضد کشتی از کنار ساحل به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک کرده اند
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/13435" target="_blank">📅 22:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13434">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الجزیره: ستاد فرماندهی مرکزی ایالات متحده ادعاهای ایران مبنی بر اینکه خسارت به ترمینال مسافربری فرودگاه کویت ناشی از موشک رهگیر آمریکایی بوده، را تکذیب کرد
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13434" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
