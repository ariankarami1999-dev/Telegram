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
<img src="https://cdn4.telesco.pe/file/YlMl7NJGgf81KO7Gxkmu4srEhG4ZMdC1WAp5xHRpCXtWh-7klBbPicUVU1hqYbAIP9HJ5Cflb8XhqpwPbN_qvV4w0f8ASHQJsVa63zQHlz7M6RIdgsL3ouqmDH2IfWWAtodDXMvj3dRE6FUDUHNhF1tcjkdeyKsLTDV7HluYjCqpXgc8vk72NBO0W5jmH7m8Px_PAlAL9Cilq1URIrvXjM7i20J5xEhlKDEp8qeluSZZjI7PzBDRZN7l3iyT0O8AhttGoPihj88y-Z2QAwa9_BcEe5fahgoca3tqPpAFRgHA7xfIOkWf9NoeNiKy-loV49xPJALfIP5lqEqeV8KNdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-135241">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/135241" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135240">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4XX9HWAMfNdvdcIGqqt63PCen4X2UCD_OJQOF75vJ8w8EExP7htKe5I-XhKq5hUj86TKiZymKi_QImt6FSR1RRwm4Maz3kcnJY6tkd_EB_M58_Hhs64oHrSndBAdVeTJrO_8ZyfNuRfpaBTfm3e8gziRtbMMKWJ6OE1t6onPsQWgS2TO06WUbWrg447cX3AlAx8qcWDDg50NwT5gx561t2Z7ZxSeYJleG0KtceO7hnTnZljsqHuzbVfNiqTyi76mOHZdcD5l7nhgZeQllsL8ygIZLxf80Km_YAJfYKa9C5db0JBhKzCh2aLbUefPi9PnHWrtaL_m_PDjOI-MEIipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/135240" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135239">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
فوووووووری/سنتکام: در پاسخ هم حملات ایران به کشتی‌های تجاری و نقض آتش بس، مناطقی در جنوب ایران را بمباران کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/135239" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135238">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
فوووووری؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/135238" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135237">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/135237" target="_blank">📅 00:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135236">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
حسام حسن، سرمربی تیم ملی مصر پس از حذف در بازی با آرژانتین با ادبیاتی تند گفت:
🎙
هر عواقبی را می‌پذیرم اما می‌گویم که این مسابقه کاملاً مهندسی و تبانی‌شده بود و همه دنیا این را دیدند. اگر تا این حد اصرار دارند که آرژانتین قهرمان شود، چرا از بقیه تیم‌ها…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/135236" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135235">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🔴
به امید عالیشاه، میلاد سرلک و مرتضی پورعلی‌گنجی اعلام شده در تمرینات حاضر نشوند و در لیست مازاد قرار گرفتند.
🔴
🔴
باشگاه همچنین به سروش رفیعی اطلاع داده قصد تمدید قراردادش را ندارد.
🔴
🔴
تارتار هم گفته هفته آینده درباره ادامه همکاری با بیفوما تصمیم نهایی…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/135235" target="_blank">📅 00:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135233">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
❗️
وای چیه این فوتبال ..از دقیقه 80 تا 90 آرژانتین سه گل زد و بازی سه بر دو جلو افتاد ..برگام ...جونم به این فوتبال جذاب ..مسی موند تو جام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/135233" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135232">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
با جدایی اوسمار ویه را و حضور تارتار فرزین معامله گری در پرسپولیس ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/135232" target="_blank">📅 22:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135231">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
دراگان اسکوچیچ:
❌
چون اجازه دخالت در نقل‌ و انتقالات را به مدیریت ندادم حضورم در پرسپولیس منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135231" target="_blank">📅 22:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135230">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
❗️
فرهیختگان: علی علیپور برای تمدید قرارداد با پرسپولیس کمی فرصت خواسته تا پیشنهادات حوزه خلیج فارس‌ اش را بررسی کند سپس پاسخ نهایی را به باشگاه بدهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/135230" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135229">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
✅
محمد گندمی ؛ سهیل صحرایی، فرزین معامله گری ، علیرضا همایی فرد و کسری طاهری از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/135229" target="_blank">📅 22:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135228">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
قدوسی: مذاکرات با احمد نوراللهی در حال انجام است و مدیران باشگاه در تلاش هستند این بازیکن رو به پرسپولیس برگردونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/135228" target="_blank">📅 22:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135227">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YI11M32-KDh_ftYoxyqMO7jkB15E4f2dWiiVq05zGVGerV_tntADbTyi7_caM2Vc07idRIL6eNIi1OtM8h5pJNaawY5Fer6iD8yjL8zX57T_yqzl1AAaxZFCxlOSvqkwShHa0q_oj6vSmzgYceAC-3FeUQzVnZjf9fiHGoabZLdcbTI736LIVzAxATpXS2n1B9RsetH2cghrmfx3Xe55LVjqircGfXXcdFHN3omaiQjOjwdkyG5rPIYK1Ne_1HQ9d2sA_Utf6a-XfQNKYVzQXvdAXHOLJfXoVv5ZHC9fcJcHuB13UBdyCYtIFQtPjWCg8Ln2IUwrPqGmfaU3JoIRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
استوری یکی از بچه های گرافیک کار باشگاه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/135227" target="_blank">📅 22:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135226">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🔹
قدوسی: باشگاه با احمد نوراللهی تماس گرفته و ازش خواسته برگرده!!!
🔹
پ.ن احمد نوراللهی در تمرینات پیش فصل اتحاد الکبا شرکت نکرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/135226" target="_blank">📅 22:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135225">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
محسن خلیلی: هر مربی ای باید افتخار کنه که سرمربی پرسپولیس بشه، اسکوچیچ نشون داد که چنین لیاقتی نداره.
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/135225" target="_blank">📅 22:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135224">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd8GjvJ049KXSJkZLcMLaSnjii9a8JRzGgClKxrYFWDnEZdwMAFGqP9fXKQY6UmuvGqln3pTfVxQy6r9GbhW9cyr7vqH3wYJzU85gmTuhnW9WclQwSnEEI2qHBiSKhpC_YAwAAPZkFZLcZE7PPr2MNcDbT7LcMsQohQw0uFoaJsKXEkT8TgddbMnDB6O7iDk5TUJ1ozlVBle6mgztCb15YfKuK6ObFS6L5XzIWSJ_7KsI1McpQwTDkGXJ4Z8NrJXxtp1BxttNwwhewDW5f4wOWlHa7Qde3AQYm9vTCa9gYj9nPJc1x6pOc66A_MsOLaF9vm_Hr9Dn8hTgQC1o_uSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
واکنش مدیر رسانه ای پرسپولیس به یک شایعه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135224" target="_blank">📅 21:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135223">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4b1NMpvTaAjyGSISkPu7Rm1WaVaZwyIDDV13bXsfOGLXvBx6SxiUiSZDl_CyScC10GLW9HdmZQko-5hpfi9ccWwq5mGEz2neQRdQnG58x2fc-gRqhVq9whnKgvkeA5LckZAdDOC2Xeb7-rHG7lLyWBu9fEwEe-sfRe43dTEq3cXTkf2uhYMDJel_3-M85G-LyBNp55yh_vpiIXQ5BtWsoaQHlFBH2apUFJ015lpEzcFyaA_rgv-Qb4GX3dOpOx4ldude57S2v_gWSCdfWBmMQOgFhPQpNwjgtfJfsfdi8jLu6q5U7Dk_mlYCXsThRQZ7nbEiRLurExh67Rz0Rz3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اشک‌های زیبای سلطان که در جام موند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135223" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135222">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
🔴
وااای آرژانتین تو ده دقیقه جبران کرد و بازی کرد دو بر دو و فعلا مسی موندگار شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/135222" target="_blank">📅 21:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135221">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
چه فوتبالی شده ی گل و جبران کرد آرژانتین و بازی شده دو بر یک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/135221" target="_blank">📅 21:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135220">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
برگام ...مصر گل دوم و زد و مسی هم مثل رونالدو بدون جام خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135220" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135219">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
خداحافظ مسی .خداحافظ رونالدو ...دو تیم گروه ایران رفتن جزو هشت تیم نهایی   پ.ن با این نتایج انگلیس تا فینال راحت میاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/135219" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
برگام ...مصر گل دوم و زد و مسی هم مثل رونالدو بدون جام خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/135218" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
خدا کنه مصر نیاد بالا .وگرنه قلعه نوعی بیچارمون می‌کنه ‌..میگه دیدین با دو تیمی مساوی کردیم که هر دو تیم اومدن تو 8 تا تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/135217" target="_blank">📅 21:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135216">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
اوه اوه مصر گل اول و زد ...آیا بعد از رونالدو مسی هم امشب هم خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/135216" target="_blank">📅 20:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135215">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
و همچنان مصر نمیخوره و داره آرژانتین و حذف می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/135215" target="_blank">📅 20:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135214">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
اوه اوه مصر گل اول و زد ...آیا بعد از رونالدو مسی هم امشب هم خداحافظی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/135214" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135213">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/135213" target="_blank">📅 20:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135212">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
✅
ورزش سه: باشگاه نساجی مازندران تا کنون برای جذب سه بازیکن جوان 115 میلیارد تومن هزینه کرده است!!!!!!   پ.ن امروز دانیال ایری با 70 میلیارد به نساجی پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/135212" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135211">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
فووووووووووووری
🔴
🔴
ایجنت میلاد محمدی دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد این بازیکن را به مدت دو فصل دیگر تمدید کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/135211" target="_blank">📅 20:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135210">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/135210" target="_blank">📅 20:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135209">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfbvJJhMTgPlYeMc3ii07oAWmimdhsKvHQlxTfuLwajn0uEjcTvqVnQ9yEUaX3S2GWK-3cgxR3Q7TKiODa715emX4dTccrvE0QKxtkQKDqU-7t4e9SEj9cNS41PY6PqaV_xa2YMwurKCTi1KmQpSMPwejcMB1W09FJuqM6608yL_i3a20FpOU-HbyciXuFq-bOfFC0nw9jkdmzAHfXCbZC46kODpbTcA_rUCcHIJYTtDQYRBQGBoQi4y6XijMws5Durb7enovwcQsp9LtrvsGOEz1D8lMB56O0s7po7Bd3DHi2FMGZ1JfOQVqE_XwYuixMduH27tXAqUVqqf5TB4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/135209" target="_blank">📅 20:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135208">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
تسنیم : میلاد محمدی و پرسپولیس برای تمدید قرارداد به مدت ۲ سال به توافق رسیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/135208" target="_blank">📅 20:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135207">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مجید عیدی با عقد قراردادی دو ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/135207" target="_blank">📅 20:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135206">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lOHaaQwhX140A3Gkybff0S17VrCVRU0KPVaQXF5r_6wugiTZA6pPHAnWofNHe86nBJYr_qNlEb2J0UZJu4Q0ag7Zbfi6AQ5hG5wburXnX2aXmZQ5cS8Oz79cLT5WRNf6nZR8rCNAguwnxT6mQeOvMtzwarKaM4xNB3vb603DD48yIi35KHMnr1N9Qd0lCn97g0NMoBTFd2b7bE91mrhdB3ZgLvBGOt4gqcIYc4gFN64svg-JMi29CDaC700dJjrmtj5i2pTiTnE2PNME_8isADfNia-ZD7i17vBewsgVXBFcf4ASmgx9b_ZBYY1urhQDFOlRjPcXkx6koy9FNvLGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌛️
پوریا شهرآبادی در آستانه پیوستن به پرسپولیس قرار دارد و در صورت نهایی شدن مذاکرات، به جمع شاگردان مهدی تارتار اضافه خواهد شد.
💬
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/135206" target="_blank">📅 20:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135205">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
بازی آرژانتین و مصر ساعت 19/30 شروع میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/135205" target="_blank">📅 19:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135204">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
نمودار درختی دور یک چهارم؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/135204" target="_blank">📅 19:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135203">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
🔴
خبرگزاری فارس مدعی شده محسن خلیلی میخواد احسان محروقی مهاجم فولاد رو بجای علیپور بیاره پرسپولیس‌
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/135203" target="_blank">📅 19:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135202">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
فووووووووووووری
🚨
قدوسی: حضور علی نعمتی در پرسپولیس احتمالا منتفی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135202" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135201">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
فووووووووووووری
🚨
قدوسی: حضور علی نعمتی در پرسپولیس احتمالا منتفی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135201" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135200">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
امید عالیشاه برای رفتن از پرسپولیس تمام قرارداد 80 میلیاردی فصل آینده خود را طلب کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/135200" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135199">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
فووووووووری از فوتبالی: ابوالفضل جلالی فردا ظهر جهت امضای قرارداد به باشگاه پرسپولیس خواهد رفت و قرارداد دوساله با پرسپولیس امضا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135199" target="_blank">📅 18:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135198">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
پیشنهاد مالی بالایی به پرسپولیس داده، اینکه میگن پیشنهاد خارجی داره دروغه و فعلا باشگاهی خارج از ایران نمیخوادش//تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135198" target="_blank">📅 18:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135197">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
شنیده ها :سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135197" target="_blank">📅 17:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135196">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
بخش‌رسانه‌ای‌باشگاه پرسپولیس طی ساعات آینده پوستر رونمایی‌از کسری‌طاهری خرید جدید این باشگاه را منتشر میکنه. قرارداد طاهری با پرسپولیس قرصی با بند خرید 1.2 میلیون دلاری خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135196" target="_blank">📅 17:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135195">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">#تلنگر
⛔️
اوسمار زنا زا… رو رد کردید ایجنت کصکشش رو گذاشتید تیم ببنده ؟! دوتا رونمایی داشتید جفتش بازیکن های این جا
…
بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135195" target="_blank">📅 17:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135194">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
❗️
پیگیری کردم؛ میلاد محمدی هم به توافق قطعی با پرسپولیس رسید و طی ۲۴ ساعت آینده امضا می‌کنه.///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135194" target="_blank">📅 17:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135193">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
تسنیم : میلاد محمدی و پرسپولیس برای تمدید قرارداد به مدت ۲ سال به توافق رسیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135193" target="_blank">📅 17:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135192">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
❗️
ابوالفضل جلالی با پرسپولیس به توافق نهایی رسیده و فقط یک امضا تا پرسپولیسی شدن ابوافضل جلالی باقی مونده.
🔴
سپهر خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135192" target="_blank">📅 16:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135191">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
❗️
ابوالفضل جلالی با پرسپولیس به توافق نهایی رسیده و فقط یک امضا تا پرسپولیسی شدن ابوافضل جلالی باقی مونده.
🔴
سپهر خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135191" target="_blank">📅 16:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135190">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
❗️
واکنش مدیرعامل نساجی به خبر پرسپولیسی شدن دانیال ایری: «ما چهارشنبه جلسه‌ای را مدیران پرسپولیس برگزار می‌کنیم اما با توجه به اینکه سیاست اصلی نساجی موفقیت در لیگ برتر است، ترجیح بر این داده می‌شود که رضایتنامه ایری صادر نشود و او در تیم باقی بماند.»
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135190" target="_blank">📅 16:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135189">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
✅
ابوالفضل جلالی و میلاد محمدی سمت چپ
❗️
مهدی تیکدری و مجید عیدی سمت راست
✔️
پ.ن دو چپ و راست خوب داریم
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135189" target="_blank">📅 16:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135188">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
فوری؛ باشگاه پرسپولیس پس از کنسل شدن جذب ابوالفضل رزاق پور، با ابوالفضل جلالی، مدافع چپ استقلال به توافق رسید و او سرخپوش خواهد شد. /تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135188" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135187">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
نظر شخصی :به نظر میاد تیم خوبی داره بسته میشه ..و بازیکنان توانمندی دارن جذب میشم ..اعم از جووون و با تجربه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135187" target="_blank">📅 16:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135186">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
فووووووووووری از فوتبال 360
🔴
لیست خرید تارتار برای پرسپولیس
🔴
مجید عیدی
🔴
مسعود محبی
🔴
علی نعمتی
🔴
دانیال ایری / محمد مهدی زارع
🔴
پویا پورعلی
🔴
کسری طاهری
🔴
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135186" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135185">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
تسنیم: ابوالفضل جلالی با پرسپولیس به توافق نهایی رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135185" target="_blank">📅 15:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135184">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
تسنیم : میلاد محمدی و پرسپولیس برای تمدید قرارداد به مدت ۲ سال به توافق رسیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135184" target="_blank">📅 15:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135183">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
✅
تسنیم: ابوالفضل جلالی با پرسپولیس به توافق نهایی رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135183" target="_blank">📅 15:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135182">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔸
شنیده ها :
🔸
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135182" target="_blank">📅 15:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135181">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
👀
ابوالفضل جلالی نام استقلال و از بیوش حذف کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/135181" target="_blank">📅 15:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135180">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6Qs0xn_SQo-vKNp6oj7ScayrtnPDtpQ0qkYolP-ZWj9mOHsHjVQ7ktW7h1JUCG80hA2j-TwbT5I9yc8JiIvumonHntRW_Wx8OM9zP4K5mBELSX_ttGwcIf6XK9Tcr0MnpQSmvYD0v5S3q4LTrjSF6vBjgRKD1dsvEErEL9C3l1tLPlLdHQxQWBTyNLeVCo6vR1ux-N4RObSvkgfv-ralgHA6BiLLYPiuDrnM5TnLk1PbPmFhFl87RBAuANc5W3WmfqF-F72whgUqlhxcvAmTDh_xSJ6XYEda0NoqQbgYS1e8lpJCo3bqP0bQ3IK11wgK8e2WnqYkgmKEZxbvlBmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فورییییی به نقل از CBS :
🔴
علیرضا فغانی قضاوت فینال جام جهانی 2026 برعهده خواهد داشت !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135180" target="_blank">📅 15:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135179">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7L2jxZmVdBoX-EVXakDKfM7amsF9u3Vz1nryLIeXr-WX5_q6YAB_BXcPCMgDm_MuV73a6NsimUfCN8oPluGA1HU1S-X9beMzyjwptH4uuJ6a2W6VxgO9ubtZUUA2wu_f94RRQruIwQn5fSSmKHdmPBjioaukcurTPrORxxHGKwEiHiUZmJXjoMUjjBE8BRhJpUfdEvD87MG2bQPe246ZeaSLvEJTx9MNOf8encQHB6_KMolIC8oC1poIQ3WIu6hXinSLfg6TJujV7sESlj4xyjJlGEwDRoGy1bzOQxm9CUOrbqviZixZwRNlEHcACthchSJEJXSbqpCqDdEFGHapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بخش‌رسانه‌ای‌باشگاه پرسپولیس طی ساعات آینده پوستر رونمایی‌از کسری‌طاهری خرید جدید این باشگاه را منتشر میکنه. قرارداد طاهری با پرسپولیس قرصی با بند خرید 1.2 میلیون دلاری خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/135179" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135178">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUyvwOxeEn0hgQ6TYfqi4-HhKH6HDi5gl1gjytuOx1i94wZSkYgeSWPbcYRr6YGnnxFt2siycsbl5vRZg9Ysmceq57dkcmLSHTh1Wu-mjbmjdTfh0YtkmjEF7mFgebkjexTw-SRzfwTF1sW4D7AxnDysVVallpgkBrz3C9E906tm86vsPe8Q8QbjScyHoJS6CY3nwbOvcq7j3OCAWofxnjUGFnlghQVFJRacV08Mcfoon6iBlNkWd-5hxf7BkAcOPhu6VQRglFJJkN_1xLINccnQjnNSQ9J9a41Y6G6DnU35CwT0wOq-v_EpW3ORuDHu__Laa2Jbnchy_cmd8pD52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135178" target="_blank">📅 15:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135177">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
مجید عیدی سی ساله، که در نفت‌مسجد سلیمان و پیکان و گل‌گهر با تارتار کار کرده، رسما با پوشیدن شلوار مشکی و نشستن روی صندلی فلزی، با قراردادی ۲ ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/135177" target="_blank">📅 15:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135171">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135171" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135171" target="_blank">📅 15:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135170">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GmI7qmfwgTL6Xkz9WOJO4mzxUuj5bACX5P-ADSrKVpijzog5go9dkHBdFw1GNuhf4BP963Ks2QZkQdaMFPzpC7bkHJp_e9tyL9egMrbkqOreyEwDTWL-owvD9ftucFPK6SACOZr3UMqEKj5RieZuOXG7YA8l6LOr9hM-lLoWWEq3D92kiaN71eXkft9mPtN5PXBAbkyAeWOxyw6Keddg0CF7TSZJuyEaW7vAu144ynk7J4YCnEVqW7wUYVC9SFpWKfGUCnnrPo-mL14G-Vm9UQogM0a5n5OLIZjY1llVc-l4rEalVbY6qRXQz06aHoTjhEs6d3ExwOaNSrbvhz13wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135170" target="_blank">📅 15:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135169">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
مجیدعیدی
🤝
پرسپولیس=۲ساله
🔴
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/135169" target="_blank">📅 13:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135168">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
✅
اختصاصی
🔴
رضایت نامه صادر شد؛ کسری طاهری تا ساعتی دیگر جهت عقد قرارداد راهی باشگاه خواهد‌ شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135168" target="_blank">📅 13:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135167">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
مبین دهقان: بازی در پرسپولیس برای هر بازیکنی جذاب است
❌
هافبک الوحده امارات در مورد اینکه گفته می‌شود باشگاه پرسپولیس با او مذاکره کرده است گفت: بله، باشگاه پرسپولیس با من مذاکره کرده است.
✅
بازی در این تیم برای هر بازیکنی جذاب است، چون پرسپولیس تیم بزرگی…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135167" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135166">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
❗️
تسنیم؛ گرگعلی نعمتی مبلغ سنگینی رو خواسته و قراره امروز ایجنتش جلسه ای با باشگاه پرسپولیس داشته باشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135166" target="_blank">📅 13:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135165">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با علی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
❗️
پ.ن تارتار به شدت بازی نعمتی و میپسنده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135165" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135164">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
✅
اختصاصی
🔴
رضایت نامه صادر شد؛ کسری طاهری تا ساعتی دیگر جهت عقد قرارداد راهی باشگاه خواهد‌ شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135164" target="_blank">📅 13:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135163">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
✅
خبرگزاری #تسنیم: دانیال ایری، پوریا شهرآبادی، پوریا پورعلی، کسری طاهری و مجید عیدی پنج بازیکنی هستند که پرسپولیس با آنها به توافق نهایی رسیده و به زودی قرارداد آنها را رسمی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135163" target="_blank">📅 12:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135162">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
فووووووری از حمید ابراهیمی: محمد قربانی در آستانه پرسپولیسی شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135162" target="_blank">📅 12:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135161">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🔹
قدوسی: باشگاه با احمد نوراللهی تماس گرفته و ازش خواسته برگرده!!!
🔹
پ.ن احمد نوراللهی در تمرینات پیش فصل اتحاد الکبا شرکت نکرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135161" target="_blank">📅 12:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135160">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
پورعلی با استفاده از بند فسخ قراردادش از گل‌گهر جدا می‌شود و به پرسپولیس می‌پیوندد. چون گل‌گهر سهمیه آسیایی نگرفته، این بازیکن حق فسخ داشته و قرار است فردا با حضور در سازمان لیگ قراردادش را فسخ کند تا قراردادش با پرسپولیس را رسمی کند.
🔴
تسنیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135160" target="_blank">📅 12:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135159">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEqX3s0iuJu4SggEov6gvLIa8iCSYivAReoEcFwa6AClpZH5soPeALAn3GIuZG7Z3t1JpTF0kGho0AEUSj1MLiB28T8qexGSevvBJpY8sSmukD01L8uP9H4VEcbQhoPvR95vRsmNJhjpV3NIYpYf4blh-TsEXUDD4aNpI-Xd6eMDuSE6K-vXIG_oNs53MndFgjhELuXeFkN0P26fspwHivJk3hMYFeXnbJKMWu8uQagmtXSr_zsfBHPHfxY2CMPor2XbXfS_4KcHn7lWAuZECKb9O6pIiA1xPVcdtvS2jjXO31-bIpPG1WINU1tJ4rkilA9I23_Y0CQKwa_JMm0Tsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
در جام جهانی که تیم های بزرگی مانند برزیل و پرتغال با شکست از آن کنار رفتند؛ تیم تحت هدایت این مرد بدون باخت به کار خود پایان داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135159" target="_blank">📅 12:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135158">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
شنیده ها: آخرین اخبار در مورد جذب پویا پورعلی:
🔴
بر اساس پی‌گیری های ما، پویا پورعلی هافبک 30 ساله گل گهر سیرجان سال گذشته قراردادی دو ساله با گل گهر امضا کرده ولی این قرارداد مشروط بوده و پورعلی مدعی است قرارداد سال دوم نیازمند توافق طرفین بوده و مانند…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135158" target="_blank">📅 11:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135157">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
🇧🇪
تیم ملی بلژیک توانست با نتیجه 4 بر 1 آمریکا میزبان را شکست دهد و به دور بعد صعود کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135157" target="_blank">📅 10:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135156">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا، داخل بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه!!
❗️
پ.ن سیاست آوردن تو فوتبال و ترس از آمریکا و ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135156" target="_blank">📅 10:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135155">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135155" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135154">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
محمد قربانی و مدیربرنامه‌اش طی ساعات آتی، احتمالا پای میز مذاکره با پرسپولیس خواهند نشست تا در صورت توافق ابتدایی، این مذاکره را دنبال کرده و شرایط نقل و انتقالاتی تابستانی را داغ‌ و جذاب‌تر کنند./ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135154" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135153">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس از دنیل گرا و بیفوما هم دعوت کرده برای مذاکره جهت فسخ به باشگاه مراجعه کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135153" target="_blank">📅 10:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135152">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1rqe3B_ys6PLxYsBLqNpQGOuxbQ91WYegCy7JpUwvLCsJFJGt_51VBDu8IQYR9hw5DNi-Wbv3UmjbrIZd32wuGX6e2YUf9wZxDchdmNfr9m0Ge-5ARw1pL9tNczbTXvw5vHz-fvEzyL4vgcCubdxC8HFvGyCEfHEYo4vdPsXa3kiCEBA5g9N0jpeDdQB5sc44onf9Z7zTcRwVwbiDNl296xfevzooPdt1Djsh9W16lNqTO3KAlNlWEhSMZIhweVbUpn6nq_Js--0hlUpDkNDmbS-xJRj162EEKLfiHdYwmnW7AyzLvPiaLFppGyj4KpjWgqrCeBCBbovds3z094hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نمودار درختی دور یک چهارم؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135152" target="_blank">📅 09:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135151">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
گزارش تلخ و ویرال شده عادل فردوسی پور بعد حذف کریس از جام جهانی
❗️
فردوسی‌پور: خداحافظ اسطوره برای همیشه
😭
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135151" target="_blank">📅 09:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135150">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
گزارش تلخ و ویرال شده عادل فردوسی پور بعد حذف کریس از جام جهانی
❗️
فردوسی‌پور:
خداحافظ اسطوره برای همیشه
😭
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135150" target="_blank">📅 09:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135149">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇪
باشگاه الوحده امارات بند تمدید قرارداد خودکار محمد قربانی را فعال کرده اما مشکلی با جدایی این بازیکن ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135149" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135148">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
فووووووووووری از فوتبال 360
🔴
لیست خرید تارتار برای پرسپولیس
🔴
مجید عیدی
🔴
مسعود محبی
🔴
علی نعمتی
🔴
دانیال ایری / محمد مهدی زارع
🔴
پویا پورعلی
🔴
کسری طاهری
🔴
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135148" target="_blank">📅 09:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135147">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHbbBvfacdRA_nqWDAIOcoUGfV6YqLhdNmc4Le3dw42gUcwekg8q8igJbqUwHTFwhZRsRX7wBIcpzgKWieE69WLZZi3zfSJgmit4YU2ZRkeSm5q648f3OfpUxOLSEAqOn3iS4ueohCdMP5cvnkKRvQV1xGJewjuJB3LCPubbVh4NildyM1Lw8Z2fo8OtshvOPr2rGTG8dzAEzj880RUUaTw3Ki6j5_XMuEH_WkHvVli0oxTSA8yyDtWiaM9_KIsKtiSsTmDl0pskHxpN8CFjPoKqeQTZTQvDbsnOccw06ez_Hj5dyclQXAgx6Q0yTgo1v6tj-BMB3MSoSeYzcZFfoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کریستیانو: من ناراحتم اما تمام تلاشمو کردم، آخرین جام جهانیم بود و الان با خانوادم باید به آینده‌م نگاه
کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135147" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135146">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135146" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135145">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORtWgTZzE-ONGRyvytrRknwu-DmRVTB2Y_j7oo8NrRSaX25W6NobsMZEVuoApv0YhQF2Fj-OijyGgRibZzEqv7tpvyRCbsuQA3E3F9nsDAylRRzoqUL9Ha2q5yPuneHDfqagEQ5D3-UcHUt1DWElim4Mp1sdWk2cfWzaa-umMIWCoImk9FbxGTP9ne1rVr-VctxZQf0MC1pLDjoHVuOo8wrZaAxsLkwoXNE0uZMDtaK9Pl1h3ljEcmg5FHHfLIYt4HloEjzo1QqdqKgnMw-oQ-64tG59VuieLsEl2GeLBskTct8Q_jg53JswM1R6xlyZ1sQ6KSPwxbXG2oXRjy7dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135145" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135144">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135144" target="_blank">📅 01:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135143">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
مطابق اعلام سایت ترانسفر مارکت؛ تا به این لحظه مهدی ترابی و مهدی هاشم نژاد قراردادی برای فصل آینده با باشگاه تراکتور ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135143" target="_blank">📅 01:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135141">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRm46eUEUn0yvXBXkK-5imUoYlhlm89RhBGuIDm2vqCEw9rD1RYChQIyK6wZM6pu7BaqprTvEu1Z3dKO_1BmbD8IKHXJzOkE0CmAjS1JW7SICO_Gijl58E-22HuAuPrOeYucp0RFASzoeDlDR2yhqPLwDbkwooYbEdpBDopXA3-gCXQhjYtdWPuz2yvwWhr0dyRy3QPbxg6oDLZ7gxN5-m62mUzMe7lI2VPCqg0keuHGoGkbfXeIrUIpErTTlHkkwC8O_lGX7LjBnH-9or3AHKmS5DeigD44IIVYQkhwoYRE_YPyXQ4n_r860Cz5MIMvSjITij3c_qKvObxepC8mSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
لعنت بهت فوتبال نامرد
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135141" target="_blank">📅 00:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135140">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFbHgVxgLAwt_m8yMs7IlOfrryXQj-Fx9LYWea9HqdMUD3CL_GluPnm08xHWmHUxHAkgbwMcOu9akhpgUZ9nbLJR9asOy9gDJ-wIcCBmtIhLCHYmOT-rErtfa_mXFoK7RhQ0sa7qRLmEwrS2NMd8pOkTGIBizpz7TdOJ5a0C488KikazrELWcXf32q9izdmOmSYUbi82DTy-dpflYfRwbbFsXNHCDRUvuzN4WF4H8xRMJbEYNAAYPtCdclrcYhSEWpTN0wZZsE5S2BGX3yQNihZF39gW7kVJZHAaGJ_xsBu0T-M7V4EvpEPZR5qfrcpKx8KBvj5HK4n3z_5g7j6zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قاب ماندگار بازی پرتغال - اسپانیا؛ دلجویی یامال از رونالدو پس از سوت پایان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135140" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135139">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrN1zDpYXLw7UlzE0ixp3J7lB-xJLSWGoqOrhW7pnALDEr7Q9aEuvx-kKTiYm3L02xxh7hKo3cpBisro1r3FT6fbUbk4tCFiksv7iEkoK-vnpCzk2am5XyKERwmJtTtjfiFWhGAsODssvQtOghp4JLA3GZ6cu9RgyNL4ZDoa4m7TK_7XU8UWfyZg-wtSPxJgFFDekZqiPGKrmy3xb29AbsAuBHuU42JX53hLQBYaB_3l6xe54KSXo1fjp0T_4FDwjxQwBhbtIGiD-rXpLKWLDe3WazEiEQlbXgCBjBCq0gWoArn-Brya7K1rq3ljjPqmnlIe3qrC5Y7LI4fBx26V8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خودتو کنترل کن اسطوره ما طاقت نداریم بخدا
پ.ن... پس از نیمار؛ امشب هم رونالدو گریه کرد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135139" target="_blank">📅 00:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135138">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
✅
اوه اوه اوج بازی ..اوج حساسیت ...بازی پرتغال و اسپانیا شروع شد ...تو 360 هم عادل گزارش می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135138" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135137">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
بعد انتشار خبر ایرنا، از یکی از مدیران در مورد صحتش پرس و جو کردم که تایید کرد.
🔴
🔴
اما دقایقی بعد گفت من منظورم خبر جذب عیدی بود نه ایری//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/135137" target="_blank">📅 23:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135136">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
کریم باقری:
❗️
من با باشگاه قرارداد دارم. سرمربی محترم هم با من حرف زده و خواسته که با او همکاری کنم. مشکل خاصی برای ادامه دادن ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135136" target="_blank">📅 23:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135135">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
شایعات؛ باشگاه پرسپولیس با هادی حبیبی‌نژاد قرارداد داخلی امضا کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135135" target="_blank">📅 23:03 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
