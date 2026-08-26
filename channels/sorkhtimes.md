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
<img src="https://cdn4.telesco.pe/file/jRkPfbcXsVn1kKLK0ntU9OWXcBrumO-l33yy1J8_bCpTZIN5tcvSqGF5YJvVT3t1HKBg7Rf2cdu2UplGARy-gjd-RQdHbpOO27VcQcnbBdd1ol6ZdW_t1N5O1MdPmZySth7h2z0fM2vIhAzTOOUEy6K9L1Z5e6Q0zx932NAJZqPj_a7BCQV9taEwJBvBVeumE9Flb2E6woy6HCwaACTzebmeVZHII0ALqyRbJnpiNv4bnXohDvLOQKHe9TqrGOvfPrCPB3v5_1RZJJc__4x-FdCIOBoNapSEcdJ7lu8T_xh1ZoRJ1N4DoKY5jYswPsiferRUrIhJ60047RYsK3H9_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 14:28:49</div>
<hr>

<div class="tg-post" id="msg-138978">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kGu3AaLmixEkLuFvMmIn_0kXSBKxJ3ChR9tyHj8jCheJ-BqE11oCB05ICxJkxgB2BV9tjeuLerbO3Cwn36ri4JuSRSVJtaIaW-mxo28Ui46SctxXs_P_VUkZ-MH3RoACRaixEfTIbHIcy8HS1C80WkQ2mCGInhT4p8FaX9azv4kVjJpf0KXNl92DLU2KPGEK2-cGA_DiyXXycFSTET9S3ezjNZRk5xYKoVd-Th3sYd4bbzv9VN2D-J_9lObufTvp-G99Lwp1q92qYXOYFIdcMcDDdhzt2KTCUOoZPQMbTsZ8ARpxBzwbwuOtAsl8K1EoAA5CJiqBXnvsI51TVFbqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
وقتی میگیم پشت بازیکن جوان تیم باشید کفتارها در کمین هستند واسه این چیزا
✔️
✔️
سایت فوتبالی و چیا فوادی توی ۲۴ ساعت اخیر پنج تا پست پشت هم علیه دانیال ایری با کلید واژه مدافع ۱۰۰۰ میلیاردی کار کردن تا کمر بازیکن جوان پرسپولیس بشکنند
✔️
✔️
دشمنی این بیشرفا برای امروز دیروز نیست برمیگرده به محرومیت عیسی ال کثیر در آسیا
✔️
✔️
پشت جوانان تیم باشید نذارید رسانه های وابسته به کیسه نابودشون کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/138978" target="_blank">📅 13:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138977">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚪️
هادی چوپان: مجتبی خامنه‌ای پرچمدار دفاع از ایرانه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SorkhTimes/138977" target="_blank">📅 13:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138976">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abzXT5XXBfd1YcOYImonSiEuUgqPk5pGYg2C1-N3FZ8OxU6KcxEwnSxko4M0MRhJjTKSijmhn4HP4IzJUhdhdd_BGDXO0ker-NdCNCuwBF0fdoiI1dXA9pW-UuKavIOcZ527VPtSLHsw2NGX9EBD_Z4h-cBDfpMXagrrEdY5h1vbdpn9NYnPez_NEDC3LN1cf-rJYe6x7qmjF5vmIuy-2KGdhbmYy_6swSHOIZMRJY5iOss7xd1Tt1aJSu5mWIr4ifE2vDSEwN_ousp3-H3peGf76RGps2Y1LxrEQUEqKmGw8QhKmSbMO6SkRbAq6jzlv8q-_3ZwU_Bsd0Fyb20kTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئال در خانه؛ سه امتیاز برای کهکشانی‌ها یا یک غافلگیری بزرگ؟
امشب؛ بازی‌ای برای شکار بهترین انتخاب‌های پیش‌‌بینی!
[
رئال‌مادرید
⚽️
🆚
⚽️
رئال‌سوسیداد
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SorkhTimes/138976" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138975">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
امیر عرب‌باقری داور دیدار تراکتور و پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/138975" target="_blank">📅 10:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138974">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
سپاهان از استقلال شکایت می‌کند
❌
❌
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت خواهد کرد.
❌
❌
این در حالی است که چند روز قبل سخنگوی سازمان لیگ استفاده استقلال از یاسر آسانی را قانونی دانسته بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/138974" target="_blank">📅 10:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138973">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
✔️
مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/138973" target="_blank">📅 09:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138972">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/138972" target="_blank">📅 09:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138971">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
منابع مطلع میگن پرسپولیس علاوه بر رزاق‌پور، جعفری و صفرزاده، با چند گزینه دیگه هم وارد مذاکره شده.
✔️
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/138971" target="_blank">📅 09:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138970">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🗣
🗣
🗣
باشگاه پرسپولیس در آستانه توافق نهایی و جذب امیر جعفری است اما بخاطر باخت روز گذشته و ترس از واکنش هواداران، برای رونمایی تردید دارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/138970" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138969">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
دلیل نیمکت‌نشینی اورونوف مقابل تراکتور؛ پرس نکردن!
✔️
تارتار از مشارکت کم اورونوف در پرس و کارهای دفاعی ناراضیه و معتقده مهاجما باید بعد از لو دادن توپ، برای پس گرفتنش بیشتر تلاش کنن.
⌛️
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/138969" target="_blank">📅 09:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138968">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZFS0f4DjGNEf-Es2WcM0s2w5eol-YYjcCUdd6t-ONMBKKW7Iv-4hCPwXCmcnAQtJOz0t6NxnOW2gkxgVnV1W6EjGxlXdUt87K3GpRY9JOOKIZ1eoAsfP89q0-LRbCAw07wBzKn0tM9YWY3W1-BVuvAjOVe8JPb1MoAhQjepYA1q1GH2YgZDsPMyFggiEEPQLVuN9Tst2lFABYW6li28Q5drOhKeT3jVQHeXs-F_DsFgI12djqYwbwVH6Fia0RloW8O56egpP38I--pR_wak_3-xLRvfXBX9jIQPWFrCP6R5gQmEwvRn9woE_r7aVkOqMCHveczzvkql2NoyblcYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/138968" target="_blank">📅 09:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138967">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
📌
ورود سریع | مسیر ساده | دسترسی مستقیم
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/138967" target="_blank">📅 01:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138966">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
دلیل غیبت محمودی در لیست تیم ملی امید این بود که او در اردوی قبلی تیم در کایسری ترکیه شرکت نکرد و حالا عبدی برای حفظ نظم تیم این تصمیم رو گرفت/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138966" target="_blank">📅 00:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138965">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
باشگاه پیشنهاد معاوضه همایی فر+پول  رو با رزاق پور به  فولاد داده اما مطهری قبول نکرد بااین حال باشگاه هنوز پیگیر جذب رزاق پوره و میخواد تا 48ساعت اینده این انتقالو رسمی کنه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/138965" target="_blank">📅 00:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138964">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
وحید فاضلی، مربی تیم پرسپولیس: اگر از بازی مقابل تراکتور درس نگیریم به معنی ضعف کادرفنی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138964" target="_blank">📅 00:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138963">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/138963" target="_blank">📅 00:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138962">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
با اعلام باشگاه اوستون ارونوف در بازی دوستانه امروز مصدوم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/138962" target="_blank">📅 23:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138961">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b9a82ba6.mp4?token=srOpk3prjoo9fCsKYEe9ARjS7yNNl-_dl-ia3ZS7SuR2VPYWZETBBgpUGh_Nks2tWl0vOc12-m2GYkp5uWBCJ3G8iuTn6XMW0o2qRhZU1I37NhuPIVEkwKeKm_Llleb0K-X2YBaKw_UNTn5nh9XwrKGrzlGO89lbbQ-rmIp4GIB8_EjBxfh_P84GyWPC2OJiS0dffQdhEbtbYkWr8YABE7TayMWygzEYmqalR2Mt3kLOJDC1vIJHmJGuQqc2B6y1HJ8t9V7AI2MBKHqsyw79tFW9BVQ2gVV9WWYA3maDDT6bj1fXCKLC_eci1xN53xP5KW06OvVSb7waFzVZpycTqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b9a82ba6.mp4?token=srOpk3prjoo9fCsKYEe9ARjS7yNNl-_dl-ia3ZS7SuR2VPYWZETBBgpUGh_Nks2tWl0vOc12-m2GYkp5uWBCJ3G8iuTn6XMW0o2qRhZU1I37NhuPIVEkwKeKm_Llleb0K-X2YBaKw_UNTn5nh9XwrKGrzlGO89lbbQ-rmIp4GIB8_EjBxfh_P84GyWPC2OJiS0dffQdhEbtbYkWr8YABE7TayMWygzEYmqalR2Mt3kLOJDC1vIJHmJGuQqc2B6y1HJ8t9V7AI2MBKHqsyw79tFW9BVQ2gVV9WWYA3maDDT6bj1fXCKLC_eci1xN53xP5KW06OvVSb7waFzVZpycTqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ممبینی : به عنوان دبیر کل فدراسیون فوتبال تا الان نمی دانم چه کسی گفته است که تورنمنت سه جانبه برگزار شود/  هیچ کسی هم نمی گوید که من گفتم و اصلا نامه ای هم در این زمینه وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138961" target="_blank">📅 22:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138960">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
وحید فاضلی، مربی پرسپولیس: اینجا هستیم که فاصله‌مان با هواداران و ابهامات کمتر شود و بیشتر همدل شویم. از داوران انتظار عدالت داریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138960" target="_blank">📅 22:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138959">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138959" target="_blank">📅 22:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138958">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فاضلی: مربیگری بی‌رحم است؛ آقای تارتار با هدف بردن، تعویض‌هایش را انجام داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138958" target="_blank">📅 22:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138957">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
🔄
🔄
مانند یک هوادار دوآتشه دوست داشتیم بازی را ببریم و تمام تصمیمات را با قلب و ذهنمان گرفتیم، اما روزهایی هم هست که آن استراتژی‌ها درست از آب درنمی‌آید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/138957" target="_blank">📅 22:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138956">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
فاضلی دستیار تارتار :
🔴
اسکواد پرسپولیس بالانس نیست و ناقصه ، حداقل به دو تا سه خرید لازم داریم
🗣
🗣
ببین وضعیت چقدر بده که دستیار و مربی تیم اومده مصاحبه کرده داد میزنه بازیکن میخوایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/138956" target="_blank">📅 22:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138955">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✖️
✖️
برتری پرسپولیس در دیدار تدارکاتی برابر تیم امید
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف امیدهایش رفت که این دیدار در نهایت با برتری دو بر صفر شاگردان تارتار به پایان رسید.
✔️
✔️
پوریا شهرآبادی در دقیقه ۷۱ و ایگور سرگیف در دقیقه ۸۶ گل‌های پرسپولیس…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/138955" target="_blank">📅 20:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138954">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
❌
#فووووووووری از قدوسی
🔄
🔄
یکی از بین امیر جعفری و ابوذر صفرزاده طی دو روز آتی به پرسپولیس می‌پیونده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138954" target="_blank">📅 20:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138953">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
🚨
الوحده در پست قربانی بازیکن خرید
⚪️
باشگاه الوحده امارات با پرداخت 3 میلیون دلار رضایت نامه آدام چرین، هافبک اسلوونیایی پاناتینایکوس رو گرفت و این بازیکن برای عقد قرارداد با الوحده وارد ابوظبی شد /سدد امارات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/138953" target="_blank">📅 20:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138952">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3VsphK1NMsdv82zJ2LHMxV-ykFGfwyQRs_uxWEd7boZ7Cri_E-nXiU8CkPEyCyvQKj0-VBKnWQlr6-fqYOLHwbLsBKKDqrXHGTdm4kpnXQXsMcyvcvATFWVlqaIc-fo1gRrwMocbH3uWkibRoHK8eeVClk5zVSwVhwDMXJfVbF3RQfebJmvtyBF-b7LOr6lX3Xye6yojZpx_TqQ2xFHIrWIpC3lK7ebmHDk9fXztRf-8EOyVZccsKmDsWrS1Y-ksNhGyHXNl_BFZa25JJ3_t5fwBaIKyjGgj4puSyRrj-l0ERwF11duyX2B_cepy4w_CkG7hShRcMnHTiKE0Rhwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
✔️
۷۲ ساعت سرنوشت‌ساز برای پرسپولیس؛ تلاش برای جذب گزینه‌های نقل‌وانتقالاتی
✔️
✔️
در حالی که تنها ۷۲ ساعت تا پایان پنجره نقل‌وانتقالات تابستانی باقی مانده، باشگاه پرسپولیس تلاش می‌کند پرونده جذب گزینه‌های مدنظر خود را نهایی و ترکیب تیم خود را تکمیل کند.…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138952" target="_blank">📅 20:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138951">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
با اعلام باشگاه اوستون ارونوف در بازی دوستانه امروز مصدوم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/138951" target="_blank">📅 20:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138950">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
اورونوف و سرگیف هیچ مشکلی با تارتار ندارن/برنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138950" target="_blank">📅 20:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138949">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iY9k7AwtI2a0sF3uSyz1lJI9ThUNZPmIywqZ9iatlj6G2FqHDEfQx0QpFY1TdtuVARzu4y9ScwLGFdeF0weYK-RGU3tJWPqSWLknOtqBbvx7CAu_xCm2AuwBd8SaBx-H8GzbW_-zLoIwBH7b9xWXnSlh-cX4iR3sfhAlQO79ItUuEX1npN6qqgfz0faQNrcyGbXbrN0KEP58RNMPeZcoee9ssmagNSEG8gD6nzxTLkK9rDnuT37SC9PbYwjyo7K5H_HX17aeKsrQuxbhYYz7lmZs8ptlVLS0oMNLTfGyhsNnPJdiekZRdV1qw8J1bKxXpvWugfceAq5hMr2b2tVSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یک دوئل نزدیک در مستایا؛ جایی که کوچک‌ترین اشتباه می‌تونه سرنوشت بازی رو عوض کنه بتیس دست بالا رو داره یا والنسیا غافلگیر می‌کنه؟
[
والنسیا
⚽️
🆚
⚽️
رئال‌بتیس
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138949" target="_blank">📅 20:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138948">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🗣
🗣
تارتار:اورونوف و سرگیف به دلایل فنی نیمکت نشین بودن و من این تصمیم و گرفتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138948" target="_blank">📅 19:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138947">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIaPESQCMvgRhvakllOAaQEJBa-5lNDY5a9DHWwxxRIU_3sdnHxXvGT7fg2rdY0eE5iH3x0eT0NPW_tAsV1KefltFdJu8ri64fLmWjvT8OP_cNIhIMB5_s-M_Ni9e2DS66sRslV_asPMbY_L4qQGXohlSAulP-Cj7SgigG1AYZHHXIskiRSHL0q-j2faTHshz6N4oCDbwYQqU3dUMMpn5GFWMbfhB1WjOCd1iNnjKu2T7C-uHaJLlIzDprvZ3Zvh_kROPW_WQWeXL7EKPlOGv0mJJ041-GghiREK_xu_xRRGI5S8G1v0-BX2VJ6XNp7MD6UL6zjR-oNyZ7x-8bgU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
برتری پرسپولیس در دیدار تدارکاتی برابر تیم امید
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف امیدهایش رفت که این دیدار در نهایت با برتری دو بر صفر شاگردان تارتار به پایان رسید.
✔️
✔️
پوریا شهرآبادی در دقیقه ۷۱ و ایگور سرگیف در دقیقه ۸۶ گل‌های پرسپولیس را در این دیدار به ثمر رساندند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/138947" target="_blank">📅 19:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
امیر عرب‌باقری داور دیدار تراکتور و پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/138946" target="_blank">📅 17:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
پرسپولیس در آخرین پیشنهاد خودش به باشگاه فولاد برای جذب رزاق‌پور ، دو بازیکن+ پول پیشنهاد داده است!
💣
🔻
همایی فرد + انتقال قرضی صادقی + 100 میلیارد پول پیشنهاد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/138945" target="_blank">📅 17:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZLMP6BCTyKrg5_rPaqK332ttiy33vNjy80VH7tF0EhtXJXaqiWtRhCBrhjYSRLg2ce96IiQI_FpJli2gvCIbeofxINRrNqvvXO6bE_yiLGth07x1Rri6VVib0BmW6dVK8_Xr8Dj5igZmZhhvbAHKwkTkPObpHx57NY9sn96Y42JKEp_WCThlegpvJDvvrEMTY-CDWK-lf1MwZ2WblPh0KWVXiJTU4Eb2XTkDgX5PO-EDMC-QDn4ffp-Rw9aK0nlJQeYtGuE8tN2aMrTSMfrL46VPFzm_HWvzYUYBs034r8br4I44qLrm2fbH3WOjOqaOOwVCoE-CsW8mdT5FpgqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
مرتضی پورعلی گنجی از دانیال ایری حمایت کرد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/138944" target="_blank">📅 17:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
با اعلام امیرحسین روشنک مسئول برگزاری کننده لیگ برتر؛ دربی پایتخت ۱۲ شهریور ماه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138943" target="_blank">📅 17:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
🔴
🔴
ظاهراً درگیری تارتار با اورونوف سر اینه که این بازیکن در تمرینات دوندگی لازم رو نداره و برای دفاع به عقب برنمیگرده
❌
❌
بازیکن ها درباره اورونوف گفتند که این بازیکن به خاطر اینکه مصدوم نشه تو تمرینات صد خودشو نمیزاره و با بی‌خیالی تمرین می‌کنه و بیشتر ریکاوری…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/138942" target="_blank">📅 17:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
عارف معاون اول رئیس جمهور: گران شدن بنزین در محدوده 80 هزار تومان قطعی است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/138941" target="_blank">📅 17:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GouFz2gqVtD7Pj8mp4BDOJah9WDDajk3XA8Ihj-GrthIDkFoQhyc8RXAGzSOFOocrDxFqGFVpphvno40C7ERuCTTxuaDYLDGncWTzyBMzHMo-s3bUmTEzQeUvl7DFHT7g3zYS_bu2zD-9UcLUeUOvwTFJh6LuOUsTJf-OhufjXNjQ4-tUf1m2OEftFnVRuXRrAxgVib2WjQ7Gcoa4bjhruXeOnvDJT-VVkcgOdK6DDC1iT0FoXp0kwEoKsxqF5wyG-EGqyxg6egp251RsamhLk4rKLVGQHfqODydIXx5757u5S7TREeuo_lAU6pis2VfI5PYrpQYZ8ENDAeo7zItTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
💙
❤️
بااعلام‌رسمی سازمان‌لیگ؛ ظرفیت هواداران استقلال و پرسپولیس در شهرآورد یازده شهریور 50 50 خواهد بود و قانون 90 10 اجرا نخواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/138940" target="_blank">📅 17:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138939">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYLWpTFnV4A-TLtlNmKgzlR4Mh53O_cz9P85yso1rIuxU3itNzXteRK5FNt2FEaedDeMzdT0NgLdFQTTSbTGf9N2IK3RSXAo8Lp2x8syFdTUtKig5Fh9fZ3M2nmG7dOGcBARadrcr2x06FadUyEav4sOfkKU9ixMAdLbXt6Of8uIhkT6TOflQzcM4WVpuD0v8w-66K8qG8Tf41A87buCfzGM1EPoq-eBxw_YW0693guxn-Efn0LLAv_H7UdnutMNaBaW9Rb7JTiJZuYzVkABu3ltjFtr3A32slT6S-2CU9E4_mXn4T5_h3O-pm3XEoV3wiYTFaDWKrxG_omzWqYroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
استوری مشترک بازیکنان پرسپولیس بعد از شکست برابر تراکتور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/138939" target="_blank">📅 17:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138938">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1236791415.mp4?token=XmCQiJJrQfptL_v58NL0YgfiyGMhFVqLOXBvNEEH8Fqg2BR6QfFo6Thf3hqlqQCOU1WvuQBiCZQEYHS6BR_SwZfOfOiGhIW6-x0YaO7MLQM8Ckew6BQ31OzwydfKOy1H7iwHOE8dnBLMpRhx_RLMrezeN6cnQebU5DgSykuxfztY3KyKNQLj6dyGGp4OCnUeHXIfyiyZUYK8Vz9LqOSABwFarmZEOtGqjd4mSA6nGzfDLigQY9fIwl2PmJq15HsD2UqWK05fEmjBfexrvySU7z8YOljN3RI2We6cUsGjky6YXZhJcGRaFaKmqJSI_uHHGwpNczwfYHakjmrv4X2vdSMkYKYvKY0dqlaOGHyP4tFdkHHAw1Rwq3cmBGi1u7xhUKJ5ZSxXrAvaGnVeciIKerEZtvcTfK9yWtQqJj_zH7-mGLkwq5xCZByzLIf3CnwbSKBW0JvGkvDkEVw8fzOJAuGQ5UdXFfqmegFlQeDTQvHqn_cqgWVuz_UZaj_BdvU1vZ10WvngfHbzo04SxvaHCPB1bQ5RUKf5MWICuaH0dPD7USKUqSJHUL0VFrbL0TtwPgJ-j3NqOUSh6n_yrU1PCwOqDFcCOhkFGzVGyt5d2hDwFFi_7pMcbjoJwJAFoFi2HD-4LBC3iNeRgPvXk_iiM2aRZKEFT0js74sEZyM6a4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1236791415.mp4?token=XmCQiJJrQfptL_v58NL0YgfiyGMhFVqLOXBvNEEH8Fqg2BR6QfFo6Thf3hqlqQCOU1WvuQBiCZQEYHS6BR_SwZfOfOiGhIW6-x0YaO7MLQM8Ckew6BQ31OzwydfKOy1H7iwHOE8dnBLMpRhx_RLMrezeN6cnQebU5DgSykuxfztY3KyKNQLj6dyGGp4OCnUeHXIfyiyZUYK8Vz9LqOSABwFarmZEOtGqjd4mSA6nGzfDLigQY9fIwl2PmJq15HsD2UqWK05fEmjBfexrvySU7z8YOljN3RI2We6cUsGjky6YXZhJcGRaFaKmqJSI_uHHGwpNczwfYHakjmrv4X2vdSMkYKYvKY0dqlaOGHyP4tFdkHHAw1Rwq3cmBGi1u7xhUKJ5ZSxXrAvaGnVeciIKerEZtvcTfK9yWtQqJj_zH7-mGLkwq5xCZByzLIf3CnwbSKBW0JvGkvDkEVw8fzOJAuGQ5UdXFfqmegFlQeDTQvHqn_cqgWVuz_UZaj_BdvU1vZ10WvngfHbzo04SxvaHCPB1bQ5RUKf5MWICuaH0dPD7USKUqSJHUL0VFrbL0TtwPgJ-j3NqOUSh6n_yrU1PCwOqDFcCOhkFGzVGyt5d2hDwFFi_7pMcbjoJwJAFoFi2HD-4LBC3iNeRgPvXk_iiM2aRZKEFT0js74sEZyM6a4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
کشوری فرد دبیر سازمان لیگ فوتبال ایران:
🔴
سهمیه هواداران در دربی استقلال و پرسپولیس ۵۰-۵۰ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/138938" target="_blank">📅 17:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138937">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGQyztNrBRohB9PCq00E5VIxW5OvJqQlTltq2JocufxhVht1WLA4vgFxiVZN-2pKYgQCfHxAIflTiWcmVZpW9JtQ_PotZhyVJQEsugzwpCjAz26hL9daR7fhRXUZb15puOV_TGC6DEe1dO2XR1_vz_LRPLU00kkxQIZ0Px5o9hwpHqeuKkMdaReiIy_tCNrOyeHCzcBeFOcO0ii5oV6KOcZTk534SJdykLDtOn1VPnLVgDmBJGSvo31F0UihB5NNWz-fgRTD05qfQ7166LhogVd9BAvfObL6xgfYs5lam-zwcpAd1FcsgON1UTVXKtL5DIo3keByITGz2UQnNd5FOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
آقای تارتار به بهانه جوانگرایی فشار در رو ننداز روی جوون‌های تیم، عامل صدرصد باخت «دلایل فنی» شما بود نه هیچ‌کدوم از بازیکنان جوان تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/138937" target="_blank">📅 17:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138936">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BREXSwUbHJEk7iLGeeowYuAlVlGdNI7QJxKOyB96XKVjHmgGUy9olP5WqTQAb1Fbzjljs400VyLTUvZRznRoVHN7dULmrxjwiqICnWoDdLGdQeMp6B94yj0gr4HVA5tVMONqikJ5ozIkoOEBDzdIH9Vm131l8-RzFiHFwmcAKoxow9WO9lZe4Ngfj63hHBrkXporpJIlPm3FcmDeL6yYk_CFXcMmph1HK26602heY8e3g8A4ZZuBWZpgUYvlbgCrQjZ4er_J6qwLdRIMQL6a4HPlUdqUdwrrFfHs4VkGP2j6jG2cBCI1zBI9Wh2mkIUUVqPbY9HlYY-p79mDIsZ30Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب؛ چند بازی با چند مسیر متفاوت برای پیش‌بینی
🔥
⚽️
از تقابل حساس الاتفاق و النصر تا بازی‌های جذاب چمپیونشیپ و لالیگا؛ کنداکتور امروز ترکیبی از بازی‌های پرموقعیت، دوئل‌های نزدیک و دیدارهایی با برتری نسبی مدعیان است.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138936" target="_blank">📅 17:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138935">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
💢
💢
💢
💢
شنیده میشه که اورونوف و تارتار به مشکل خوردن و به واسطه کنعانی اورونوف کوتاه اومده و فعلا خودشو نگه داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138935" target="_blank">📅 13:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✖️
✖️
✖️
ابوالفضل جلالی در گفتگو با مجری فوتبال برتر گفته مصدومیتش جدی نیست ده روزه برمیگرده و احتمال خیلی زیاد دربی در ترکیب پرسپولیس قرار خواهد گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138934" target="_blank">📅 13:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
بازی بعدی
✔️
هفته چهارم
⚪️
شنبه ۷ شهریور
🔴
پرسپولیس - ملوان
🔴
ساعت ۱۹:۱۵
🔴
ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138933" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
علوی سخنگوی فدراسیون فوتبال: سرباز شدن بیرانوند؟ تاریخ بازی کردن او تا 31 شهریور در کارتش که در اختیار سازمان لیگ است درج شده و بعد از آن سرباز خواهد شد اما اگر نامه دیگری بیاید این تاریخ می تواند آپدیت شود و بیرانوند تا جام ملتها می تواند در تراکتور بازی…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138932" target="_blank">📅 11:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
✔️
۲۴ساعت تا پایان  پنجره نقل و انتقالات تابستانی…پرسپولیس هر بازیکن و میخواد بگیره باید امروز سه شنبه بگیره وگرنه بعدش فقط بازیکن آزاد می‌تونه بگیره بازیکن آزادی که مثل همیشه ی مدت بازی نکرده و مثل هندوانه سربسته اس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138931" target="_blank">📅 10:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138930">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
✔️
گویا دیشب تو رختکن حال دانیال ایری خوب نبود و ازبس گریه میکرد شرایطش اوکی نبود. بزرگ ترای تیم هرچی سعی میکردن ارومش کنن فایده نداشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138930" target="_blank">📅 10:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138929">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
فوتبالی: ایری تو رختکن گریه میکرده و بزرگترای تیم بهش روحیه دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138929" target="_blank">📅 10:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138928">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
باشگاه پیشنهاد معاوضه همایی فر+پول  رو با رزاق پور به  فولاد داده اما مطهری قبول نکرد بااین حال باشگاه هنوز پیگیر جذب رزاق پوره و میخواد تا 48ساعت اینده این انتقالو رسمی کنه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138928" target="_blank">📅 10:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138927">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚠️
آقای جاکش بخای ترسو بازی بکنی تیم میبازه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/138927" target="_blank">📅 10:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138926">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138926" target="_blank">📅 10:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138925">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❤️
❤️
صبحی که بازی و باختیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138925" target="_blank">📅 09:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138924">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔵
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔗
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
📌
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/138924" target="_blank">📅 02:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138923">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
آقای تارتار! بازی هفته قبل تراکتور با سپاهان را ندیدی؟ چطور دقایق پایانی حواس تیم تا این حد پرت شد؟ مشکل اورونوف چیست؟‌ شفاف به هواداران بگویید. پرسپولیس نباید بازنده میشد دو برد اول چندان مهم نبود اما این شکست خیلی غیرقابل هضم بود. به امید بازگشت هرچه…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/138923" target="_blank">📅 00:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138922">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✔️
✔️
۷۲ ساعت سرنوشت‌ساز برای پرسپولیس؛ تلاش برای جذب گزینه‌های نقل‌وانتقالاتی
✔️
✔️
در حالی که تنها ۷۲ ساعت تا پایان پنجره نقل‌وانتقالات تابستانی باقی مانده، باشگاه پرسپولیس تلاش می‌کند پرونده جذب گزینه‌های مدنظر خود را نهایی و ترکیب تیم خود را تکمیل کند.…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/138922" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138921">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
فوتبالی: ایری تو رختکن گریه میکرده و بزرگترای تیم بهش روحیه دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/138921" target="_blank">📅 00:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138920">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
آقای ایری؛ شما هم جوان هستی و هم تجربت کمه و فراموش نکن ماهم اونقدر بی معرفت نیستیم سر یه اشتباه بخوایم تخریبت کنیم
❌
❌
اینجا پرسپولیسه، قطعا یکی از تلنت‌های فوتبال ایران هستی و جام جهانی هم رفتی و ما انتظارات بیشتری از شما داریم. در آخر فراموش نکن هوادار…</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138920" target="_blank">📅 00:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138919">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d62852b4d.mp4?token=HOD5CeEqKNANmxFNw5wfvULIRaUg6PMFjJ8BQTIo_iqgJ4EQFexyeFY7Rt9cz-pDJ20x8rmiEQvvUB-aDLEXUEabvEZJv2Hd2lh37s-SjXU24FMICTAqJO3zWGC3egY3jatmlJPCiXBDddChxTM3_f7iYKjFwQ_zYBR_sQuQhDn3ZIKykWYl9KvZZ24lHTHEiIN_vCTLzbZ4F4Hf2I12MO0QPSsMyhIvfi4RcESGd5DxdHvOv8vY4BMKilr0WAFMhSo2OofDoymXZ2doObZpajYgIOWwP81HM4zTBCza2RwDNsmAAKJB8bGvgXn7SkUr-yIb4zdlSLonN_-JoF031g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d62852b4d.mp4?token=HOD5CeEqKNANmxFNw5wfvULIRaUg6PMFjJ8BQTIo_iqgJ4EQFexyeFY7Rt9cz-pDJ20x8rmiEQvvUB-aDLEXUEabvEZJv2Hd2lh37s-SjXU24FMICTAqJO3zWGC3egY3jatmlJPCiXBDddChxTM3_f7iYKjFwQ_zYBR_sQuQhDn3ZIKykWYl9KvZZ24lHTHEiIN_vCTLzbZ4F4Hf2I12MO0QPSsMyhIvfi4RcESGd5DxdHvOv8vY4BMKilr0WAFMhSo2OofDoymXZ2doObZpajYgIOWwP81HM4zTBCza2RwDNsmAAKJB8bGvgXn7SkUr-yIb4zdlSLonN_-JoF031g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون فوتبال: سرباز شدن علیرضا بیرانوند؟ تاریخ بازی کردن بیرانوند تا 31 شهریور در کارتش که در اختیار سازمان لیگ است درج شده است و بعد از آن سرباز خواهد شد اما اگر نامه دیگری بیاید این تاریخ می تواند آپدیت شود و بیرانوند تا جام ملتها می تواند در تراکتور بازی کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/138919" target="_blank">📅 00:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138917">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
حدادی مدیرعامل باشگاه:
🔄
🔄
ضمن عذرخواهی از هواداران محترم همه ارکان باشگاه در باخت مقصر هستند؛ از مدیرعامل تا سرمربی و بازیکن.
🔄
🔄
اما برای موفقیت، یک راه داریم؛ حمایت از سرمربی و حمایت از بازیکن، بخصوص بازیکنان جوان، اگر جوان‌ها اشتباه می‌کنند. مقصر من…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138917" target="_blank">📅 23:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138916">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
جوان بازی دادن تاوان داره
🗣
لطفا با یه اشتباه اینده های باشگاهو خراب نکنید
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138916" target="_blank">📅 23:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138915">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbe1-zZeviD4aW8veymuy18HJMbuj711NL9Qg6jkqE8XTiyc7l9R4Ly_ZMxzJPln2NdYxkJeP-ds4LyIHjSq_nYH1cQ4F8IkMLGOvArEkTMjtBxG_l3MQIAAXysf2HwqEXfqW7CwwxlGsgFF_8wrlI9zH3Dq5ILPz4GAelwEC06ck-jms8Uk2Kj35Tp75gq7okH5CPLjatex6rfl0gozaWuHbQ1nQGWNZCNZm6iLTk_N8DIVc2pPmeQlFDvixyWPKxjuNEGx6HFeX62PHaLat7hdUaC5X-BeFWe6BN9fZ17IRtYZyNSJHVSIhRHZWOtvzQf5yjtuUPNHkb27M9ZkJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
جدول لیگ برتر پس از پایان هفته سوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/138915" target="_blank">📅 22:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138914">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
باید بچه ها به خودشون بیان ...فاصله بازی ها کوتاه کوتاهه ...امیدوارم این باخت و جبران کنن ...با فاصله خیلی کم شنبه با ملوان بازی داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138914" target="_blank">📅 22:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138913">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚽️
⚽️
⚽️
⚽️
از بین ابرقویی، تیکدری یا عیدی یکی دفاع چپ پرسپولیس مقابل تراکتور خواهد بود/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/138913" target="_blank">📅 22:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138912">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
⚽️
✍️
دانیال ایری، مدافع ملی‌پوش و جوان فوتبال ایران با امضای قراردادی ۴+۱ ساله رسماً به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/138912" target="_blank">📅 22:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138911">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
⚽️
✍️
دانیال ایری، مدافع ملی‌پوش و جوان فوتبال ایران با امضای قراردادی ۴+۱ ساله رسماً به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138911" target="_blank">📅 22:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138910">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtkpvhavU63LDk7Fa9A-szx8qdBv2Mmo9PwB72ugRZW5T3eM9-JdGGoYglEeA0ta_zfz_FVj5GVm09CADIaV8tcQa2t8vFlkhB1L5tZiqFbyYRVzbIkKipmifeUcujuaV2lqB17SHLtFZ6LOLEOhCkFSVmbklAoUHfbyltWCm4zKooC411b1uvOVHqqwkiByhZV8UYBr0GYCrahJzSD01an1x2TcvIU6P9y1g4ue0PlCcmJ_0ThZtYM-sECRTRJU-0WORC7UnLTpJ6ZBdc5iPsH1UK4mrlueZeO23exiFiTk4xmRk0fjXy_5M_zKJiKkU4U3wSRmGszhQKLRMStNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تنها فقط تا آخر امشب فرصت برای بونوس ویژه بازی Scarab Temple باقی مانده!
🔵
کاربران اسپورت‌نود می‌توانند با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
🔵
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
📌
نسخه جدید سایت:
Sportn5b2.com
📌
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138910" target="_blank">📅 22:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138909">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/138909" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138908">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
✔️
تارتار: مسئولیت باخت امشب با کادر فنی است؛ فوتبال همین است اگر اشتباه کنی بازنده می شوی
🗣
جوان بازی دادن تاوان دارد/ اکثر بازیکنان تعویضی ما سنشان 20 تا 22 سال بود. نیمه اول موقعیت های خوبی داشتیم/  امروز کم شانس بودیم و کم تجربه، تاوانش را هم دادیم…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138908" target="_blank">📅 22:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138907">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
کمال کامیابی نیا: هواداران پشت دانیال ایری و دیگر بازیکنان باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/138907" target="_blank">📅 21:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138906">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
با تمام وجود امیدوارم این آخرین عذرخواهی شما باشه از هواداران ///اعظمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138906" target="_blank">📅 21:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138905">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
خلیلی: امروز فقط بهای جوانگرایی را دادیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138905" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138904">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
✔️
تارتار: مسئولیت باخت امشب با کادر فنی است؛ فوتبال همین است اگر اشتباه کنی بازنده می شوی
🗣
جوان بازی دادن تاوان دارد/ اکثر بازیکنان تعویضی ما سنشان 20 تا 22 سال بود. نیمه اول موقعیت های خوبی داشتیم/  امروز کم شانس بودیم و کم تجربه، تاوانش را هم دادیم…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138904" target="_blank">📅 21:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138902">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
امیر رفیعی، ابرقویی، عمری، سرگیف، شهرآبادی، محمودی، اورونوف، همایی فرد، سلمانی، باکیچ و ایری، بازیکنان ذخیره پرسپولیس بودن.
‼️
اصلا شما نیازمند به همین ترکیب اضافه بکنی به قرآن شانس برد مون ۷۰-۸۰ درصد بود/ حالا شما کنار این نفرات چنتا از نفرات اصلیت مثل کنعانی،بیفوما،زارع و حتی محبی رو اضافه کن اصلا تو مخیلات منم نمیگنجه ارونوف،سرگیف،باکیچ،محمودی حتی یاسین بزاری نیمکت استفاده نکنی، بازی هجومی و چشم نوازی ارائه نکنی حتی نتیجه حداقلی هم نگیری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/138902" target="_blank">📅 21:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138901">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
با تمام وجود امیدوارم این آخرین عذرخواهی شما باشه از هواداران ///اعظمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138901" target="_blank">📅 21:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138900">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2280d396d6.mp4?token=cq74xqDJlFflATqlvhvLQgH1cEOyKUvH3vuZ3cpxW3SXOPToBszqkkv4B36g6VeHIe-qoxhi0e17hqxLmxMyNilU6Ot5EwTpKjFMmQuUReGbjdabLs3J_0zB45kJflhLFoPgEh7NqZWSTjshwkwG2fE_hI3Da6rrJxGqhuvK59-t6HYUAEo4uAkOGHSF96lELuEQCii5MrNOOMqEWM6p5vYF2YBZqIs-vGsGK3YGF295RSdjNfwU46Y0RGu68ffSQ7O_0i4kQRjHHqWcRbySBPuaecoYPKuoGXP1-GVMZa5Hu9so5u8Yy3QbB5-GUCxKqWnlhNfW_uGbbWfJhyRnpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2280d396d6.mp4?token=cq74xqDJlFflATqlvhvLQgH1cEOyKUvH3vuZ3cpxW3SXOPToBszqkkv4B36g6VeHIe-qoxhi0e17hqxLmxMyNilU6Ot5EwTpKjFMmQuUReGbjdabLs3J_0zB45kJflhLFoPgEh7NqZWSTjshwkwG2fE_hI3Da6rrJxGqhuvK59-t6HYUAEo4uAkOGHSF96lELuEQCii5MrNOOMqEWM6p5vYF2YBZqIs-vGsGK3YGF295RSdjNfwU46Y0RGu68ffSQ7O_0i4kQRjHHqWcRbySBPuaecoYPKuoGXP1-GVMZa5Hu9so5u8Yy3QbB5-GUCxKqWnlhNfW_uGbbWfJhyRnpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔄
🔄
گل اول مس شهربابک
گل به خودی عجیب !!!!
که می‌تونه نامزد پوشکاش بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138900" target="_blank">📅 21:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138899">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
تارتار: عذرخواهی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138899" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138898">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔄
🔄
تارتار سرمربی پرسپولیس: بازی کم رمق امروز؟ به دلیل نبودن هواداران بود/ امیدارارم از این به بعد تمام بازی‌ها با هواداران برگزار شود
❌
❌
دلیل بازی نکردن ارونوف و سرگیف؟ این به کادر فنی مربوط است و دلایل فنی نداشت
⚪️
ما تیم پرمهره ای هستیم همه با هم رقابت می…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138898" target="_blank">📅 21:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138897">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🗣
🗣
تارتار:اورونوف و سرگیف به دلایل فنی نیمکت نشین بودن و من این تصمیم و گرفتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138897" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138896">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
تارتار: عذرخواهی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138896" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138895">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
پرسپولیس پس از ۷ سال در تبریز برابر تراکتور شکست خورد‌‌‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138895" target="_blank">📅 21:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138894">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
پرسپولیس پس از ۷ سال در تبریز برابر تراکتور شکست خورد‌‌‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/138894" target="_blank">📅 21:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138893">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
❌
تو روزی که تراکتور هم هیچی نداشت حتی یک موقعیت بازی و باختیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138893" target="_blank">📅 20:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138892">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⛔️
کوصکش خر لج کرده با خارجی ها، کدوم کوصکشی سرگیف که بازی قبلی گل زده میزاره رو نیمکت ؟! اورونوف نیمه دوم نیاوردی تو عمری آوردی گذاشتی مهاجم سایه ؟! شرف تیمو بردید به جای مهاجم و وینگر آوردن دفاع وسط اضافه میکنی؟! پرسپولیس با ۵ دفاع قهرمان نمیشه اقای تارتار…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138892" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138891">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚠️
آقای جاکش بخای ترسو بازی بکنی تیم میبازه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/138891" target="_blank">📅 20:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138890">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚠️
آقای جاکش بخای ترسو بازی بکنی تیم میبازه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138890" target="_blank">📅 20:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138889">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
تارتاری که ترسو بود ..سرگیف و ارونوف و نیاورد و دفاع آورد ..با ی اشتباه دفاع بازی و باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138889" target="_blank">📅 20:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138888">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
توی ی بازی سرد و یخ و بی روح و کلا دو موقعیت با ی اشتباه بازی و باختیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138888" target="_blank">📅 20:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❤️
❤️
نیمه دوم هم شروع شده امیدوارم با تعویض ها هجومی تر بشیم و بریم برای برد ....امیدوارم تارتار از باخت نترسه و بره برای ی بازی هجومی و برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138887" target="_blank">📅 20:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❤️
❤️
نیمه اول حرفی نداشت برای گفتن و گزارشگر ..تو نیمه سرد بازی صفر صفر نیمه اولش تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138886" target="_blank">📅 19:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❤️
❤️
❤️
الهی به امید تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138885" target="_blank">📅 19:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138884">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
✔️
✔️
کم کم بریم سراغ بازی حساس و استرسی ..امیدوارم تارتار از این بازی بزرگ هم سربلند بیاد بیرون ...امیدوارم .بیرانوند و شجاع اخر بازی از باخت فشاری شده باشن.امیدوارم ببریم بازی و انشالله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138884" target="_blank">📅 18:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138883">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🟥
💢
گرم کردن بازیکنان پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138883" target="_blank">📅 18:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138882">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f3c54f76.mp4?token=m3iFCt0OE7uP-uHmQtqIRFyG368WQf1S56ISe3I9LQTy4Zpjlh2cjSyj8jQ4KS-SNZBSi0S-ht0grdW3jPcEdQxbrf6nPJt7PvO9rmm5L3pwus1A5YCIKLrdCMcnOIS0HX-Va5iUCZHnm0m61b0kCTcNhBdOmABqHUMW2vA_3_W-GkoYxf73oA-3IZRlustqN3POy-aJ7c5wO-1JD2xfycGpo8ES5dwiq5SGXHzgrhf7ukLETU8smQESOd05WZZutM7ZcM0mEqvws4VWP-lCx1X_huVRsv_pWFCNWWO9kTt6YjITIOgR8bA3EMgm2bb2FtX1XFq0ov_u_NMRft6NDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f3c54f76.mp4?token=m3iFCt0OE7uP-uHmQtqIRFyG368WQf1S56ISe3I9LQTy4Zpjlh2cjSyj8jQ4KS-SNZBSi0S-ht0grdW3jPcEdQxbrf6nPJt7PvO9rmm5L3pwus1A5YCIKLrdCMcnOIS0HX-Va5iUCZHnm0m61b0kCTcNhBdOmABqHUMW2vA_3_W-GkoYxf73oA-3IZRlustqN3POy-aJ7c5wO-1JD2xfycGpo8ES5dwiq5SGXHzgrhf7ukLETU8smQESOd05WZZutM7ZcM0mEqvws4VWP-lCx1X_huVRsv_pWFCNWWO9kTt6YjITIOgR8bA3EMgm2bb2FtX1XFq0ov_u_NMRft6NDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
خوش‌وبش گرم و صمیمی کریم باقری و خداداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138882" target="_blank">📅 18:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138881">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25482bf71.mp4?token=RIqZHnRuve2xqKJQgeS_Nztp6th6USvx48hV1EiN_6v6TL9C-yrdicF-slAvHcjr540ZG_0kdqFJRNgDMJ0wsaeS4VAgRh-F2zvYW6XV-XHWBNuMCMNRPi-6B0swnWDf0Yq_gZ7LypQmxFkC3dK6OC-fHGIjr46zC72FG5h_7oT23PezDsexzgm44IwXpIFRSvikRAxSHBFayjnhWsydXhi2sinID5cy5qdjAkijXrhVhLYYHv1DU2on6gvjDn6rgfn1O7D9PnsOgx-cOPZHF3F_1foT3OhNzLgEdycAK4COasNhniw5xgkOpUjeJckG8cYRsW2czA8orDgtf50F0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25482bf71.mp4?token=RIqZHnRuve2xqKJQgeS_Nztp6th6USvx48hV1EiN_6v6TL9C-yrdicF-slAvHcjr540ZG_0kdqFJRNgDMJ0wsaeS4VAgRh-F2zvYW6XV-XHWBNuMCMNRPi-6B0swnWDf0Yq_gZ7LypQmxFkC3dK6OC-fHGIjr46zC72FG5h_7oT23PezDsexzgm44IwXpIFRSvikRAxSHBFayjnhWsydXhi2sinID5cy5qdjAkijXrhVhLYYHv1DU2on6gvjDn6rgfn1O7D9PnsOgx-cOPZHF3F_1foT3OhNzLgEdycAK4COasNhniw5xgkOpUjeJckG8cYRsW2czA8orDgtf50F0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
💢
گرم کردن بازیکنان پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138881" target="_blank">📅 18:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138880">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHq52Xv1zekx1kKgzU2nkMWfF7yIS1TIjw9HiKLSgkROEBsqvp1UzM3Gt-8uYndGtb-qEgCdZYsjL8DKRZxWTaszu9cC_OIMMYwAzy-bLWn_T6J6ltihoGF1EKPdQjUhcyU04edkybKAX0duAyOP3wt-8Qdnxw9dwBB8tlss6Mu0EomnmER_Vo5bjHUlgf0h88JsX3wJ-zTveISuzBwd2jLiykhJ_xech9YONAsHKD8noiLlDlAqlf9z7gvYH_B9BWM6TXfHxd3A8SfTyqJOEqs4VHndB-lf1WvNHnP1ui-crxb3AlsmLQh7b__IgJbUFUQ9miU4uJm_cTpmZGK10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
انفجار در تبریز؛ سرخ‌ترین نبرد فصل!
تراکتور و پرسپولیس؛ امشب فقط یک تیم می‌تواند با دست پُر از این جنگ بزرگ بیرون بیاید!
[
تراکتور
⚽
🆚
⚽
پرسپولیس
]
🔵
تنها فقط تا پایان امشب فرصت برای بونوس ویژه بازی Scarab Temple در اسپورت‌نود باقی مانده! کاربران می‌توانند با هربار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود اسپین رایگان کازینو دریافت کنند.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/138880" target="_blank">📅 17:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138879">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/138879" target="_blank">📅 17:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138878">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/138878" target="_blank">📅 17:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138877">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30428072b5.mp4?token=suIT_VmZQPoXkfkKhJfyvamHmqjL0zhMjQbC1AmbGB7ThkSLT2JAeDHIEbWCTcs8qsRn4SgLCTvgpFnyvl-2cNQN2JDhZRbC3zQadjlu_mHj_ZwbT-riuqCDjqwFDogLXTEq1Ss3uDgGYG3q3FUtjlqqG2PosuXPMrU-u4HurdgVmH44T6Uwf9fkgRPJHyq7_IabLUTihp89G56VCeK6fHcSA632K0KqMKqN-ZmjxPtgar8UD_QL2xJ9rbl1Xc_vq4vBbj9BQt7g3RjCMZUu3pI8x6OttjH3TnmuKx-2L_t42gNB1Kslzj1pfWjvhNNQYHrSr_mfGUDwEhrBnQgk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30428072b5.mp4?token=suIT_VmZQPoXkfkKhJfyvamHmqjL0zhMjQbC1AmbGB7ThkSLT2JAeDHIEbWCTcs8qsRn4SgLCTvgpFnyvl-2cNQN2JDhZRbC3zQadjlu_mHj_ZwbT-riuqCDjqwFDogLXTEq1Ss3uDgGYG3q3FUtjlqqG2PosuXPMrU-u4HurdgVmH44T6Uwf9fkgRPJHyq7_IabLUTihp89G56VCeK6fHcSA632K0KqMKqN-ZmjxPtgar8UD_QL2xJ9rbl1Xc_vq4vBbj9BQt7g3RjCMZUu3pI8x6OttjH3TnmuKx-2L_t42gNB1Kslzj1pfWjvhNNQYHrSr_mfGUDwEhrBnQgk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از ورزشگاه یادگارامام در فاصله یک ساعت مانده به بازی تراکتور و پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTime
s</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/138877" target="_blank">📅 17:43 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
