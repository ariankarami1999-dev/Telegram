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
<img src="https://cdn4.telesco.pe/file/J5wUx1ecuigg8FHemIEK4JBpFcDnOGFT1VXwFPSLUZ9_rPlcWhO_KfWxZPvS9GXGuyP6pmJQQHRiccnzfyCYKiAPIVfyNWV7p0I8tNO7UB7zQVgaOE8FpBKoCCEIC9wLdgAva5I_zco1z0-k1lz2_tYTr8r1dYGUtnS2nbyKxbYAz-7zgsVIYHx1cMInLbQLEYiMXc_vWypdJMm77pbyMfFMf1sGc0nJedyiRwCifykBPrJGAE5AzyqPBbigQSyjmyRjpBWefuznKuxVam194w-Ye9HOMGIsXFDmggUm4UmaRJKHtza6qTnP5MGwjh0XDI679OJK6EKsRamdv9xSjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 22:33:56</div>
<hr>

<div class="tg-post" id="msg-131665">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6d85daac.mp4?token=tbHLTnfNKthFQA90M0J5Wrf74fGos5pK1kb_B0JQ5L3bi72NNDfHs9NEnHr0xog70VZcwG6wuvDtDkqPewlhDGI8eVWisEQO9hNEeaJXRsFP2Z23HHD0v9kJEWj0xL-6-Ql1flrNDd-kkXkFHoPZY_1zsfxq5paV1Mw3AWG4QSDfcawrej4WEfhIl-ganDJ3iavAmREAO-NWOQO_RoVsgi2WtLMkbDkyFUveGuq60PpNvyl_TO3rGl0zQ1GCEr_hGKnd2_FPXvwcWy537Ar5PIJ5Me4JrFrxvpQ8H-K1xXYJv5ve2UAxq7Yof9cAZkqRKLucB0mR10c8ElkVOe4Reg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6d85daac.mp4?token=tbHLTnfNKthFQA90M0J5Wrf74fGos5pK1kb_B0JQ5L3bi72NNDfHs9NEnHr0xog70VZcwG6wuvDtDkqPewlhDGI8eVWisEQO9hNEeaJXRsFP2Z23HHD0v9kJEWj0xL-6-Ql1flrNDd-kkXkFHoPZY_1zsfxq5paV1Mw3AWG4QSDfcawrej4WEfhIl-ganDJ3iavAmREAO-NWOQO_RoVsgi2WtLMkbDkyFUveGuq60PpNvyl_TO3rGl0zQ1GCEr_hGKnd2_FPXvwcWy537Ar5PIJ5Me4JrFrxvpQ8H-K1xXYJv5ve2UAxq7Yof9cAZkqRKLucB0mR10c8ElkVOe4Reg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های آشپز برنامه "به خانه برمی‌گردیم" صداوسیما که تغییر جنسیت داده و دختر شده :
تو 5 سالگی، یکی از آشناهامون بهم تجاوز کرد!
من کلا تو خونه پوشش دخترونه داشتم و این عمل، تغییر جنسیت نبود، تطبیق جنسیت بود.
من حتی دفترچه خدمت هم پست کردم که شاید از این حس فرار کنم ولی نشد.
تا 25 سالگی به کسی چیزی نگفته بودم ، حتی اون زمانی که تلویزیون می‌رفتم هم از همه پنهون می‌کردم.
2 تا خودکشی ناموفق هم داشتم چون اون موقع حس خوبی با جسمم نداشتم...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/131665" target="_blank">📅 22:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131664">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید کاملا مورد
تایید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
➕
با کد تخفیف زیر میتونید با ۵۰ درصد تخفیف خریدتونو انجام بدید(فقط100 نفر اول)
✅
🎁
کد تخفیف :
Express50
.
🤖
خرید سریع
:
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/alonews/131664" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131663">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
سرویس VPN (V2Ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
پنل اختصاصی (مشاهده حجم و تاریخ انقضا)
✅
سازگار با تمام دستگاه‌ها و اینترنت‌ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
تمدید و خرید مجدد بدون تغییر کانفیگ
✅
بدون محدودیت تغییر دستگاه و IP
🛠
پشتیبانی تا پایان اشتراک
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 100,000 تومان
▫️
۴۰ گیگابایت — 190,000 تومان
▫️
۶۰ گیگابایت — 280,000 تومان
▫️
۸۰ گیگابایت — 370,000 تومان
▫️
۱۰۰ گیگابایت — 460,000 تومان
▫️
۱۵۰ گیگابایت — 680,000 تومان
▫️
۲۰۰ گیگابایت — 900,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 1,150,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 190,000 تومان
♦️
۵۰ گیگابایت — 280,000 تومان
♦️
۷۰ گیگابایت — 370,000 تومان
♦️
۱۰۰ گیگابایت — 505,000 تومان
♦️
۱۵۰ گیگابایت — 730,000 تومان
♦️
۲۰۰ گیگابایت — 950,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 1,350,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 480,000 تومان
▫️
۱۰۰ گیگابایت — 555,000 تومان
▫️
۱۵۰ گیگابایت — 785,000 تومان
▫️
۲۰۰ گیگابایت — 1,010,000 تومان
▫️
۳۰۰ گیگابایت — 1,445,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 1,650,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/alonews/131663" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131662">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj1dqY_GfdkUUP0gn6DDDWKCHOAbHKvF_1hhjwOpH3qA_8A915ZjMF-_BfjuM6vHKRNW7-kt-SOE4MdiTmnyTNL3o7iIsgehX30fwDtn-_cfw534IyNAGXHHbO119Y0aUFEB8z2DqLheOQoQkVq7CWMa64bnK0f9VSkO1OxJy8votd_cuNUEac1hVuOiEFe8Tcg4LNPZdFxVtszgkBpWJYNbg0L36B_t83IcElZ2W0veSkO4M51awab7-0_2kXGjuPvol3K1wmPoEN0plRs_JJM2Ilnqfmp1HH6QmlOiLyfXmW7Uj6dYVEc6Azfkg6Y4cacSbKYIh0oAVOV6aY1R1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف به ترامپ: به فکر سوء تغذیه ۴۰ میلیون نفر در آمریکا باش، مشکلات خود را به دیگران نسبت نده.
🔴
ایران خودش درباره دارایی‌هایش تصمیم می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/131662" target="_blank">📅 22:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131660">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
حسین یکتا: ترامپ که می‌خواست ‎۳ روزه کار ایران را تمام کند، هنوز خون‌خواهی ملت ایران را ندیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/131660" target="_blank">📅 21:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131659">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoThN3hchJWvN12i2xx-NdJv1k55QxX__Y8gZzkNdFvXoKoGz8fWk8NJnX_MKuMmd6AlF49Bq3bvg-r9Wa7iisIEyTNMcE0tiifmNVIxiYXVr5xdZWoBVxmRroE3vaBNNwaopKGKKHvFi06wtDw1B9Z7NoRjgUbptLaZyWNmFArgUxfKT_h2vZqLGGfYPdiPOmWGM5tgCmAup8GYiCqiHQhS4ShqbEhb7aJd9hNJUIuIMKgGGpIUXqSJ6-ViqvDLua2WtARjoay8KLrTnoPXjziHx1lXUELiJ6ZcZN5gTm1bZHVLxQoEalujUSJMc14-cmXHk_5siwYxyTTSdRxfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سال قبل در همین روز، مجله تایم عکس سیدعلی خامنه‌ای را صفحه اول گذاشت و دقیقا بعد از یک سال روز تشییع جنازه علی خامنه‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/131659" target="_blank">📅 21:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131658">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
فرمانده قرارگاه خاتم: اولویت‌های دفاعی تعیین‌شده از سوی قائد شهید امت، دست نیرو‌های مسلح را برای پاسخ به دشمن باز کرد و پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131658" target="_blank">📅 21:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131657">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
المانیتور: مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131657" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131656">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سی‌ان‌ان: رفت‌وآمد کشتی‌ها در تنگه هرمز در حال افزایش است
🔴
هفته گذشته ۳۳۵ شناور از تنگه هرمز عبور کردند و پیش‌بینی می‌شود این هفته نیز تعداد عبورها در همین حدود باشد؛ به‌طوری که تا پایان امروز، شمار عبور کشتی‌ها به حدود ۲۱۵ مورد برسد. این در حالی است که پیش از آغاز جنگ، به‌طور متوسط روزانه حدود ۱۰۰ کشتی تجاری از این تنگه عبور می‌کردند.
🔴
اگرچه روند کلی فعالیت‌ها در حال بهبود است، اما بازگشت کشتی‌های تجاری بین‌المللی احتمالاً با سرعتی کمتر از ترددهای محلی و منطقه‌ای انجام می‌شود؛ زیرا بسیاری از مالکان کشتی، اجاره‌کنندگان و شرکت‌های بیمه همچنان رویکردی محتاطانه در پیش گرفته‌اند.
🔴
ابهام درباره خطر گسترش درگیری‌ها همچنان پابرجاست، به‌ویژه پس از آنکه حمله ایران به یک کشتی در هفته گذشته، عملیات تخلیه دریانوردان گرفتار در منطقه را متوقف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131656" target="_blank">📅 21:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131655">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
باراک راوید: ترامپ امروز با نتانیاهو تلفنی صحبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131655" target="_blank">📅 21:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131654">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/En7BOMnzLTvP48ajB25RqWND0O7hmoE2PTAD9tcRM4AeqqxlEqGLNUyj5CcQ1EtTE7yabt4XofNii-TUAHafmcmfUN_dUF7DPlIHoO9HqK2igbPi4fn_yJeB3wMJSjcwXF67dSdsx2PTplHFAUv1pxA9f5FxTeWlbLZl0CNMC_dtlOORz8-LIJOtNy7MFNf9TrjMmeUJqcFkjwZxcYOKngp8Rb2sDRhfPcsKsZJ_enrTmVEUY2iUIs42Ww9Ed1Y0r-a3opTCjA2fMJCrhIceomymsiItJc_ATEcu6azlwpc8FaeA4hawogrbziXIVH4Bgt2wV5ypHHGPdM7pLdYVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
با اعلام رسمی فیفا، علیرضا فغانی به عنوان داور بازی انگلیس و مکزیک انتخاب شد.
@AloSport</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131654" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131652">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c6feb8e70.mp4?token=JZCUOqbs7Fgo6AhT0HPiqTEWY43u8CkkwV7uZZmczyOjk6XaPdMlcapqXyowBKMyyX2qQ0x7Qzk3LxT9rnee3zAZ4KUmnxqEPzJ-P_FB79-U9mnY0hU7B7HSCV7CDIkuJmE5bQoErzPhbcZvWEiJFzA0qU3QNZsS8ybWqKc1lJvkzQGCwz5GZ_xt1rwaEwT1QRWCQvUTcnUMPchyM_vhkrR7AOvmNsOexqpjz6POU3JtzS2JXdG7wnBndZ0aQHfTf1uuMeLXYFfJnbg4HppXrIUzSOItC-9Taw3qMjmlp-EZBbAUKweRrHnCo7jGb1m9LpTtScvdIo7NDsxwFW2A2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c6feb8e70.mp4?token=JZCUOqbs7Fgo6AhT0HPiqTEWY43u8CkkwV7uZZmczyOjk6XaPdMlcapqXyowBKMyyX2qQ0x7Qzk3LxT9rnee3zAZ4KUmnxqEPzJ-P_FB79-U9mnY0hU7B7HSCV7CDIkuJmE5bQoErzPhbcZvWEiJFzA0qU3QNZsS8ybWqKc1lJvkzQGCwz5GZ_xt1rwaEwT1QRWCQvUTcnUMPchyM_vhkrR7AOvmNsOexqpjz6POU3JtzS2JXdG7wnBndZ0aQHfTf1uuMeLXYFfJnbg4HppXrIUzSOItC-9Taw3qMjmlp-EZBbAUKweRrHnCo7jGb1m9LpTtScvdIo7NDsxwFW2A2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیم نمایش‌دهنده جت‌های جنگنده F-35C نیروی دریایی ایالات متحده در حال پرواز و معلق ماندن بر فراز نمایشگاه ایالتی بزرگ آمریکا به مناسبت روز ۴ جولای و ۲۵۰ سالگی آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131652" target="_blank">📅 20:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131651">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1445c04c7c.mp4?token=ga0sJUmFhy-uG6QOA957VC0NlFJTs6jsrrJ09iBCtaqAO9OfCf08FNEZ82OJIvtDk_5e9rHc6VZS_Sh01cDTlCvd6YsJ6-37nqX0eel2arB1JFySHYYDRGqr6ZaM28llj0PHjv0bULbW6YrQoag6fs0A65Ic_QEjbbAXxFqufhPeDl0J4Qz4IM03axs3Ovl-zOpaZAeH9BwjXqtxWDn-i5VGbr21r6vKhB3RdZLEljUpacsdFj04-i_pJJGN8D3AcOaUUbGO2ux6oNdb5KEeRIDkAOt20-8G-0p-NqWrnTpjxwJAkMUupVvsG_jXz34v5rBWrYWbydV9JO_x8JMKgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1445c04c7c.mp4?token=ga0sJUmFhy-uG6QOA957VC0NlFJTs6jsrrJ09iBCtaqAO9OfCf08FNEZ82OJIvtDk_5e9rHc6VZS_Sh01cDTlCvd6YsJ6-37nqX0eel2arB1JFySHYYDRGqr6ZaM28llj0PHjv0bULbW6YrQoag6fs0A65Ic_QEjbbAXxFqufhPeDl0J4Qz4IM03axs3Ovl-zOpaZAeH9BwjXqtxWDn-i5VGbr21r6vKhB3RdZLEljUpacsdFj04-i_pJJGN8D3AcOaUUbGO2ux6oNdb5KEeRIDkAOt20-8G-0p-NqWrnTpjxwJAkMUupVvsG_jXz34v5rBWrYWbydV9JO_x8JMKgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توکیو به مناسبت ۲۵۰ سالگی استقلال آمریکا آتیش‌بازی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131651" target="_blank">📅 20:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131650">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/آکسیوس: نتانیاهو به زودی در سفری ناگهانی و قریب الوقوع وارد آمریکا خواهد شد و با ترامپ درباره ایران دیدار خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131650" target="_blank">📅 20:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131649">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPKqrUt4MDxIR_IFuZhTFa8yH47EvsJW3mLQOtoaeBrE_7_gdYzgUE76nMmGRk6NeGjirPlycZUc_pZxK-ubVVEZXTYLwW36rWPx5YOPWmXZ2ihTEOi2MyzdnwCpQELWaDkHUqurPVxSE0kmnpjdFt9-Am6yBrBf_m65nvnhbp5ch0g3DL6cU3o0Ltg7xJPmFp1onzP7C9kbfof80bQlVTL8P9bgTxh7NDFAnOvmx31B5hOku1EL7smoOvtub7hwPINBwmxevrm0RmJvBb6JTCTuSM7hpQnqkWGRG0dhLTtH5Uv2VpCUJwwNm4j5Q8TSLzuty8IiJcCa6mQUUAjq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست: رئیس‌جمهور سوریه یک بازیگر زن محبوب تلویزیونی عرب را برای مجلس انتقالی جدید کشور برگزیده!
🔴
رزینا لازکانی، ۳۶ ساله، به‌عنوان یکی از ۷۰ نفر منصوب‌شده احمد الشرع در مجلسی با ۲۱۰ کرسی انتخاب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131649" target="_blank">📅 20:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131645">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3767bfbca0.mp4?token=FkAW3X1DQPeAqMFkFk2iIx6HeGCd8ZYXw9gWIU_yW1Fq_3yZHSAxDwEAh3TpgVDHaJXspyDfzL9IoaGSlPBMRycCCI8YH9th0p_BcHW731VJH9rEJAuEHOnFgTN5UeSFv3l2UmJwRwR334hjBfGRoW9bPBeBq04zRiS0UJok265ZPsR2pq6z8oMLMSjtBGY2sfYWtbCegPKWF82hAJUsNCM51I1I-PnDAKzJ62zQ4PmmKcLtIh_xLleM_XZlV5X6gRV4FVV1zVp6cuD8pXGzkotFgKvSnQ0CQDxDfJ6CFqgzAw_uKJKo2AIJDPHdBC47rWO6aHs5jZnd4WrqZ58VYx58Vfv3lKiX9gHh5faceaFb00WSjh364NvNonXV1aLob3NbYikIqZk0HTRkUxcbG4xqL0B3b5GOYbP3B3vbiVZIqOBXW3d-eUqirdukjbI-p4IH20sA1MAdEhU8hT-qDYNGIMnt0TPvx8MvsZPcoJ7HOvE-7hWncr5GOtFF-LEsoZ-fy0Lz7aK8EGmHfPKgrLkDdBOkbKf9kQFwxcVkf0Mr2lPvrZwtBuuxw2HP9c-0PVLG3t_acJwS-8HbynneoNG-_cEd8PKrcezpuz7ehW6Twiky0MkKIMHJYBZuIvlKL2Ap7tWmcEQKSje8yzhjB4k2_vvkeEDOymOWj4PQSg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3767bfbca0.mp4?token=FkAW3X1DQPeAqMFkFk2iIx6HeGCd8ZYXw9gWIU_yW1Fq_3yZHSAxDwEAh3TpgVDHaJXspyDfzL9IoaGSlPBMRycCCI8YH9th0p_BcHW731VJH9rEJAuEHOnFgTN5UeSFv3l2UmJwRwR334hjBfGRoW9bPBeBq04zRiS0UJok265ZPsR2pq6z8oMLMSjtBGY2sfYWtbCegPKWF82hAJUsNCM51I1I-PnDAKzJ62zQ4PmmKcLtIh_xLleM_XZlV5X6gRV4FVV1zVp6cuD8pXGzkotFgKvSnQ0CQDxDfJ6CFqgzAw_uKJKo2AIJDPHdBC47rWO6aHs5jZnd4WrqZ58VYx58Vfv3lKiX9gHh5faceaFb00WSjh364NvNonXV1aLob3NbYikIqZk0HTRkUxcbG4xqL0B3b5GOYbP3B3vbiVZIqOBXW3d-eUqirdukjbI-p4IH20sA1MAdEhU8hT-qDYNGIMnt0TPvx8MvsZPcoJ7HOvE-7hWncr5GOtFF-LEsoZ-fy0Lz7aK8EGmHfPKgrLkDdBOkbKf9kQFwxcVkf0Mr2lPvrZwtBuuxw2HP9c-0PVLG3t_acJwS-8HbynneoNG-_cEd8PKrcezpuz7ehW6Twiky0MkKIMHJYBZuIvlKL2Ap7tWmcEQKSje8yzhjB4k2_vvkeEDOymOWj4PQSg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چتربازان و هلیکوپترهای گروه "گلدن نایت" در حال پرواز بر فراز نمایشگاه بزرگ ایالتی آمریکا در واشنگتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131645" target="_blank">📅 19:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131644">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COifDbQuOexX8hJ4QSnR6-Kmp4EjxRMMRRPKjbCm10SY3Yi8ldFXF515AyP4wZSpcTbBiAIEd7bap2rlIOijQ94F9VvZ4ZfvN9F7-VQNJ6nbNtO6TgTOkGdfXPrZxx2nN5nf4bhOXHX-hIusLyWxTy0pTzvd7XiYbaZEV1hknt8_V3Bo7UawStdJeAI4Kaha3OBXYi8tUrsWusW_vtQ-IyyXXF_bB5P-87cv-cR5OWGDWcpe0pHE2wZGzweMEWTFeWvI_NpwnskOtnVwFNBOoD4W5WYUn1XAy1-eWBrPoPag23OgvRrPjBpiux2ddT9hBnn8R5LxwE55iTOvumcOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عاصم منیر با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131644" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131643">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
فردا از ساعت ۵:۳۰ صبح مترو تهران فعالیت خود را به صورت ۲۴ ساعته آغاز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131643" target="_blank">📅 19:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131642">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: اهمیت نداره که چه DNA تو بدنته یا چه چیزی مصرف میکنی یا عمل میکنی، وقتی به عنوان یک مرد به دنیا بیای هرگز نمیتونی تبدیل به یک‌ زن یا جنس دیگر بشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131642" target="_blank">📅 19:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131641">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
حوثی‌ها اعلام کردند که جنگنده‌های سعودی را از حریم هوایی یمن بیرون رانده‌اند، پس از اینکه این جنگنده‌ها تلاش کردند از فرود یک هواپیمای غیرنظامی ایرانی در صنعا جلوگیری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131641" target="_blank">📅 19:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131640">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eizXhXu9KW576QlhLPD5VVogKrNaARrr9ZQ6CrI2swJOJq-8jBMDs3EkwOT9E7bfvudMNXpvX5UZnKDosjTY4ZGEl4AlPTit_EuHRez8XLn4XxHV3Ile-NlnZa2DdhNnPDO7xAn21zIt8r08NfXixHTQsUOYCKtLi27N0WGBPWfQL8VMRkGEqe5sCnv52bWWGL4osR3xrGHE40xvXa1Se0sOoAwDudnUS6_lkP0XBPvlV5FFpiANefERx9jvVl9xajAIG8iyluz52srZUEF0skrP51m2MTQEmcb97gxjlL7LELxj5vaXV8Jsuz5FrYRN342-K2ucXwFx8hGTUUduvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل، گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131640" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131639">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، در گفتگویی تاکید کرد که افشای درآمدهای میلیارد دلاری اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا از حوزه رمزارزها هیچ‌گونه «شائبه یا تضاد منافعی» ایجاد نمی‌کند.
🔴
بر اساس گزارش‌های مالیاتی و افشای اطلاعات مالی که اوایل هفته جاری منتشر شد، دونالد ترامپ از زمان آغاز دور دوم ریاست‌جمهوری خود، حدود ۱.۴ میلیارد دلار از فعالیت‌های تجاری مرتبط با رمزارزها درآمد کسب کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131639" target="_blank">📅 18:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131638">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/alonews/131638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
ویس لو رفته از ابویسانی، مشاور وزیر آموزش و پرورش که دانش آموزا زنگ زدن میگن بخاطر مراسم تشییع خامنه‌ای باید امتحانات عقب بیفته و در
جواب میگه خامنه‌ای و مراسمش چه مسخره بازی ایه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131638" target="_blank">📅 18:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131637">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz0WLejqufBY81xzrdjA6e03QDdc8FKotRw25LIIVVwztGNocsBwxM8L5swTiGjR1XWPqsTgmI2FLFRFR97_LeTTbXlMjyeuwmwxwMJ8FN5Bi6dlFxAZHAcg0Y0BdRgkFgLISX7963kpSCUX6AuIP_QZ9-nM2f3a2DwYtv_HLFHsl48PLGEM61F06h5ylasChc-vyiuxz2irziYK45MIvRtj1Yq6Pji1q9HAV-IKwPZOadfN_Qa1IzFYw949RVjy2PrYIs3Hpn9fTC0K4qH1dEVyPYseO0Gd2Cu_SR0i8j3IzYZfRNUeqFKimdrjw9pwKyEfQcw3nSigeA5hrJjMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاه و تعجب عراقچی از گریه قالیباف که مورد توجه فعالان فضای مجازی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131637" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131636">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
دونالد ترامپ درباره باراک اوباما:
من نمی‌دانم که آیا او یک بازیکن بسکتبال خوب است یا نه. من شخصاً شک دارم.
🔴
در واقع، ورزش مورد علاقه او گلف است. اما او به زودی در مسابقات "ماسترز" شرکت نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131636" target="_blank">📅 18:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131635">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ: رئیس‌جمهور آبراهام لینکلن از سوارکاری با اسب لذت می‌برد. من هم دوست دارم سوار اسب شوم
🔴
اما وقتی از اسب می‌افتید، من شاهد اتفاقات ناخوشایندی زیادی بوده‌ام. افتادن از اسب اتفاق خوبی نیست.
🔴
بنابراین، ما یک اسب پیر و سالخورده خواهیم داشت که بسیار کند و تنبل است، و شاید من هم سوار آن شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131635" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131634">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a185ba29be.mp4?token=DUTR0sy1k6LSl9E57gijSdcswXzVk0gbrNqYsP9OYt7fLzlwF9trDGTkoFxAtADDKCLOWyrjb7ylfDAAQkW_Wn1F9iK-IdpKMUzvIyzgWQrA4kuy-aQ5eDn5gBUh6ZCJUbNpFHOwwa9CsIbvXGbJ86D2CDw-6HnaprKamQH-c-iyf_5ium_GdPsbl9L5Ol2v4kCdrhWfjWouwmd5488_hhfxHQ0MNyq8giVtJ9wTmbPjS-PWOmC4IQ0ftJ6UbJ3TaCUPnVFtuYnwXdexxmqx4U8hA53dKNiInmicLZA6_gpY91ArEKm2YZkmtBpkCTXW1G6NMtrsH_aT01XqUKXGaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a185ba29be.mp4?token=DUTR0sy1k6LSl9E57gijSdcswXzVk0gbrNqYsP9OYt7fLzlwF9trDGTkoFxAtADDKCLOWyrjb7ylfDAAQkW_Wn1F9iK-IdpKMUzvIyzgWQrA4kuy-aQ5eDn5gBUh6ZCJUbNpFHOwwa9CsIbvXGbJ86D2CDw-6HnaprKamQH-c-iyf_5ium_GdPsbl9L5Ol2v4kCdrhWfjWouwmd5488_hhfxHQ0MNyq8giVtJ9wTmbPjS-PWOmC4IQ0ftJ6UbJ3TaCUPnVFtuYnwXdexxmqx4U8hA53dKNiInmicLZA6_gpY91ArEKm2YZkmtBpkCTXW1G6NMtrsH_aT01XqUKXGaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بیل کلینتون: او در واقع آدم خوبی بود. من بیل کلینتون را خیلی دوست دارم. هنوز هم همینطور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131634" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131633">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn72V8-HM0Uabt3wLQTCvvmb3WDGEC5uiloJ4pe4WG2YV5rD9_-JzYD253_34PjuO-dbyXIWThQnnf9QyURTXwKUYZbeP8afEJ4pirGH8mpn3X5vSSOeEH93OrqChpHdRklqE3K-sbu4VZ1QEsD-mNPvbOZ0tyPyll4JSWMMdyr7cJcSsTdfb78P_aCQLBjrwbKVFGbqW5-8TzD3xQes4U5kn5KdyR1qJzaARSm3EB48JqcxdWmWR1AwntIGf9lB-2919lI61XZdJzsL6KXa-lk1aV4fmChn8eWjl94WbaiCXPtia9dOAw6cCpPnXtuZbaom40_VFBU-Om8Y7fMdIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: تو این چند روز اینترنت رو قطع کتید تا دشمن سواستفاده نکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131633" target="_blank">📅 18:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131632">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYGS8nPezzPwbpynfIo85KMEgQ_kTCVRpw1dasKq0__TNQcWqW1l8Yya6F5WZm_KmuNUZgvxHvyvI3fwnHcWUDo_B9FtVIzBoFtP_d0RGHzFA8vRaAnY92ayXHuqWQ9wFc6Hn7HLk3isvDneXGhwNjyO0pMlVlZRNQnJeqTefxbpGFwBxPy9YDDlBQcpu2GZw6cRWTnPXIiFH8RsrXRXWyAXMUaPSEZY0grVHkhhbHyUFyLgPD5VWbpd9rH__jPzrs9P7eypu1Copd3qhZSt176KzSyS0twBdjy3d04WrTP7kQynuXa7jzlwQ9MBgnLsCEYGEfF_sbgFEVq6gbu--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس برآوردهای کارشناسان، هزینه جنگ ایران برای آمریکا می‌تواند تا سه برابر رقم اولیه کاخ سفید باشد؛ هزینه‌هایی که شامل جابه‌جایی تجهیزات، خسارت‌های جنگی، استقرار ناوهای هواپیمابر و سامانه‌های پدافندی، استفاده از موشک‌ها و بمب‌ها و حملات بمب‌افکن‌های B-2 می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131632" target="_blank">📅 18:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131631">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
🔴
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131631" target="_blank">📅 18:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131630">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=Bqhcjk0fN86qxlgmgaXa_5TorfMiKDFD-55oe75XLZ0s-ZdqcAVk3-iPCWjs2QULD4LpdRIt6TutR6wDJTjZz2FLcnR_nxO7k6QY8OcNmBGyK8IUfBaf5Oa5RXr_Ke0WaR4l60k4DpJktWYruTO3SrTgK-IInuo7cQ-wYIMWzXnxdhZLfOAT_gHmC5tJUuetokUbXGGk4esuE5QgDSrvuLaqX9l1l4rfzEH808xXa05Zfq5uFCqDrx-T7gNuS9WvWaUMR54R6HLzwx4TSXEAhanP1rjoNvgMdC0WRraq-WAbK17llRDL_4k42dEbjn1GIrW_LBGmhxXwtlvjht11kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=Bqhcjk0fN86qxlgmgaXa_5TorfMiKDFD-55oe75XLZ0s-ZdqcAVk3-iPCWjs2QULD4LpdRIt6TutR6wDJTjZz2FLcnR_nxO7k6QY8OcNmBGyK8IUfBaf5Oa5RXr_Ke0WaR4l60k4DpJktWYruTO3SrTgK-IInuo7cQ-wYIMWzXnxdhZLfOAT_gHmC5tJUuetokUbXGGk4esuE5QgDSrvuLaqX9l1l4rfzEH808xXa05Zfq5uFCqDrx-T7gNuS9WvWaUMR54R6HLzwx4TSXEAhanP1rjoNvgMdC0WRraq-WAbK17llRDL_4k42dEbjn1GIrW_LBGmhxXwtlvjht11kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نایا: تصاویری از حمله امریکا از خاک کویت به ایران، با موشک‌های هیمارس در زمان جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131630" target="_blank">📅 18:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131629">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: ارتش باید در هر زمانی که لازم باشد، آماده انجام یک عملیات مستقل و اسرائیلی در ایران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131629" target="_blank">📅 18:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131628">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
الجزیره: ۵۰۰ میلیون دلار برای ترامپ، دسترسی برای پاکستان؛ چگونه شرط‌بندیِ کریپتویی - دیپلماتیک اسلام‌آباد جواب داد؟
🔴
وقتی این هفته جزئیات درآمدهای مالی دونالد ترامپ، رئیس‌جمهور آمریکا، در سال ۲۰۲۵ منتشر شد، یک رقم بیش از همه جلب توجه کرد: شرکت رمزارزی خانوادگی او، ورلد لیبرتی فایننشال (WLF)، فقط از محل فروش توکن‌ها در سال گذشته بیش از ۵۰۰ میلیون دلار برای او درآمد ایجاد کرده بود؛ بخشی از یک سود بادآوردۀ بسیار بزرگ‌تر از حوزهٔ رمزارز که در مجموع صدها میلیون دلار دیگر هم ارزش داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131628" target="_blank">📅 17:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131627">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f227c1ee.mp4?token=NcpzDLS8xRyx0xxPatfDpUIhaGFlne3G1aQUYMbnWlLGyKuUfHM40mkO4Ot_ifa85G0FEsWoPODtv5yo1lJ6GGXavpZaT2Me8JDVXsicysv5nJdn6QGngZhGJqUwonRudFcAatjQfpyhrv13zf57D4EFO1IAlka87eZ-hjUAYuQf4jYcfie8HlkjCTk-he2LVptHTnnZMR8IfHs-RtWL3FrZ555oHmXBRJas7CwJRroHkXTAH6pKKG_42-zQi43eFYHdZ8nmOKVAyKEe_kuG-8TLGTq2DzfY_X9_pMlLPsHu9m4_KMx4DSMSmCBr3uvXRqyCQTc5xZvYrBs7Bu6PgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f227c1ee.mp4?token=NcpzDLS8xRyx0xxPatfDpUIhaGFlne3G1aQUYMbnWlLGyKuUfHM40mkO4Ot_ifa85G0FEsWoPODtv5yo1lJ6GGXavpZaT2Me8JDVXsicysv5nJdn6QGngZhGJqUwonRudFcAatjQfpyhrv13zf57D4EFO1IAlka87eZ-hjUAYuQf4jYcfie8HlkjCTk-he2LVptHTnnZMR8IfHs-RtWL3FrZ555oHmXBRJas7CwJRroHkXTAH6pKKG_42-zQi43eFYHdZ8nmOKVAyKEe_kuG-8TLGTq2DzfY_X9_pMlLPsHu9m4_KMx4DSMSmCBr3uvXRqyCQTc5xZvYrBs7Bu6PgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر وداع عاصم منیر و شهباز شریف
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131627" target="_blank">📅 17:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131626">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iK7j2tFVP4B5-tjz_EJ6kx5SvQxxOO0PnyQiOx6neTmrULEip1Fbpw5j7yrJTVNRStQhhkr1ThPGaMDRYA9sQbOncEJyiImUUxklKnomysVSdWXh-V5rk6KAIhiSY-usQYCAFBtXbCuXUr_PizvkZG4vwz3OKI6vO6PhHTp7uUQqsAlrrVxS3VIK-IbzHvTI02NkWyO_axTI1XAFIYipajh2r5_Cfmx8elSWRv2gRN4Y55s8DWG8qII_5Tc86FHuhmE0sj_z-IEwbZUuvcp9RNhRtLCmD2dZAYmrr2qY0ZfK5VsMAZ9XzqUzHgfRFDuYYkXrkQqWHsc7rxYjs3Vhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز
:
به سه منبع ایرانی و غربی استناد می‌کند، ایران مذاکراتی را برای فروش نفت به شرکت‌های ژاپنی آغاز کرده است، اما خریداران احتمالی به دنبال دریافت معافیت طولانی‌تری از تحریم‌های ایالات متحده و اطمینان از ایمنی تردد کشتی‌ها در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131626" target="_blank">📅 17:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131625">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f37b08bded.mp4?token=gd2J9kp77UKN1zTkXTjMOExteskMA1digyy9jrvfd818twEjzEmh6wj5y4ltOdOY-Rgy7FzgYA7g7WFst3Z-7NqblyfR2MV9DLKCtYOoqTWTl9H9U5OUXKdcu1bhxqqDEBPQq3AqIOLVO_GbN4sxtjbM4eRbCFUVccQE18dXHuOobeTp9EzswSLTZDaksMwQlYucNixnPhg6FopRCWUzOJ-qmPDdR4MENAi5sIT5JWb7PPEnCnKDqm8rRDZ-uL7x0kNYKDuAcJ2WM52Vi5MMkKTffCbTJkIX_-lGtX0sW-0ktiZ6JjT2CNjcTQDZio-xmCGZ09KJORMxp42lRX4I0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f37b08bded.mp4?token=gd2J9kp77UKN1zTkXTjMOExteskMA1digyy9jrvfd818twEjzEmh6wj5y4ltOdOY-Rgy7FzgYA7g7WFst3Z-7NqblyfR2MV9DLKCtYOoqTWTl9H9U5OUXKdcu1bhxqqDEBPQq3AqIOLVO_GbN4sxtjbM4eRbCFUVccQE18dXHuOobeTp9EzswSLTZDaksMwQlYucNixnPhg6FopRCWUzOJ-qmPDdR4MENAi5sIT5JWb7PPEnCnKDqm8rRDZ-uL7x0kNYKDuAcJ2WM52Vi5MMkKTffCbTJkIX_-lGtX0sW-0ktiZ6JjT2CNjcTQDZio-xmCGZ09KJORMxp42lRX4I0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام دیمیتری مدودف، معاون رئیس شورای امنیت روسیه و فرستاده ویژه پوتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131625" target="_blank">📅 17:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131624">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/63e838adce.mp4?token=PH30KMGWD83z4asOzon0WMJWXCgI7Xgr-mhvgV1tbvv0PeqpxRic0x3C2KbgihMH4-Y7zsYR0G0sWlT371obu1qSji_vZQRNHvvCwreQAfb3xtXo4k1ve1-EZCDosIhh8k3WPHlFxb8EINyRBSqIPOZhPZG79d_QBnsVOH5u6hkCeBIkBS9dV6SQ7v1kTIRjjQ3BdTpwiKNyzS3aOLpKSv7dWZo8D3YtEWYcz7cC7Jsrxg2JuCaUymnnutKQmkLdHkSYxWX7SF4AGXuHgp8A-AlolS9crvmuQWhXl7mIBaPOW4Vq9BYNJvHew3TLA_l8rCThofqTHo2vx07A494R_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/63e838adce.mp4?token=PH30KMGWD83z4asOzon0WMJWXCgI7Xgr-mhvgV1tbvv0PeqpxRic0x3C2KbgihMH4-Y7zsYR0G0sWlT371obu1qSji_vZQRNHvvCwreQAfb3xtXo4k1ve1-EZCDosIhh8k3WPHlFxb8EINyRBSqIPOZhPZG79d_QBnsVOH5u6hkCeBIkBS9dV6SQ7v1kTIRjjQ3BdTpwiKNyzS3aOLpKSv7dWZo8D3YtEWYcz7cC7Jsrxg2JuCaUymnnutKQmkLdHkSYxWX7SF4AGXuHgp8A-AlolS9crvmuQWhXl7mIBaPOW4Vq9BYNJvHew3TLA_l8rCThofqTHo2vx07A494R_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام وزیر آموزش عالی گوام
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131624" target="_blank">📅 17:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131623">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
معاون اردوغان از سفر احتمالی رئیس جمهور ترکیه به ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131623" target="_blank">📅 17:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131622">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKr2OQm8eynDwlTO0VXHSqiYyUCVddljNAyaz6TnaTpNN7nKx19Zi0e-rQx6YuKc_p1H2ZeTyZJ3D76QaZS_OBKL1WZD2h46wLmlxHRTZn3aQLQWnTPDHld9swcEX5wm0SH14IxUXCFgO52SGkERCBAFpPUJW07XwKDpra8V77iqDIkt-3rIucUmq6kxefRD1YFMqOIJgw-5Pl_qIXOz_H6CyF4o0M0BArZdXqQu4Y552d8v0LZsZ1fTIrguW5jBI5R4sKlAk64OeP0U_jURMapo8ZJv5Mo8ohrqKrBuW_1uwb2PiEz5yl4ByFFlTAHom_LccP4n7FzgorOv3mPM8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز یک پرواز ماهان‌ایر جهت انتقال مقامات انصار الله به ایران وارد صنعا شده و پس از مدتی به سمت تهران بازگشت
🔴
این اولین پرواز مستقیم ایران-صنعا در حدود ۱۰ سال گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/131622" target="_blank">📅 16:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131621">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رایزنی احتمالی OpenAI برای واگذاری ۵ درصد سهام به دولت آمریکا
🔴
به گزارش تایم، شرکت OpenAI، سازنده ChatGPT، reportedly در حال بررسی واگذاری ۵ درصد از سهام خود به دولت ایالات متحده است؛ موضوعی که می‌تواند ابعاد تازه‌ای به رابطه دولت آمریکا و صنعت هوش مصنوعی بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131621" target="_blank">📅 16:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رویترز: ایران گفتگوهایی را برای فروش نفت به شرکت‌های ژاپنی آغاز کرده است!
🔴
خریداران احتمالی خواهان تمدید طولانی‌تر معافیت از تحریم‌های نفتی آمریکا و همچنین دریافت اطمینان درباره امن‌ بودن شرایط کشتیرانی در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131619" target="_blank">📅 16:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af94fcd247.mp4?token=GFBHwoDj-s8lzFrRgSNOvpx15idB7WvAAk4Chd7GGNBGEd_GSzwWizr5gnj9ob9g5LzoAE4KfKx8EyTQUUud1H36XKnHeJSmxqdx-Ek7M2ubypqx70XBif-R8tECtYqotHUm1R9_F8k_7WFux44U8vyxQIKvP1PEEOZn8Bq5stpwf9M9LlFHvvHXYFvNAcgYxHcbSKJHBAfHlAUKP0mkjmAJEu4yn9oga8IYXo30dnwsu1rCT6tGVJTiDQ1H-N5zNwzbUQYZd-ozEnmvEh-ndPUYl50uvOip2Ap-DmjVYNbjXk8deo-Ff2TGxo6r1IizNOxQXY-Axir8OKSpX-Vr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af94fcd247.mp4?token=GFBHwoDj-s8lzFrRgSNOvpx15idB7WvAAk4Chd7GGNBGEd_GSzwWizr5gnj9ob9g5LzoAE4KfKx8EyTQUUud1H36XKnHeJSmxqdx-Ek7M2ubypqx70XBif-R8tECtYqotHUm1R9_F8k_7WFux44U8vyxQIKvP1PEEOZn8Bq5stpwf9M9LlFHvvHXYFvNAcgYxHcbSKJHBAfHlAUKP0mkjmAJEu4yn9oga8IYXo30dnwsu1rCT6tGVJTiDQ1H-N5zNwzbUQYZd-ozEnmvEh-ndPUYl50uvOip2Ap-DmjVYNbjXk8deo-Ff2TGxo6r1IizNOxQXY-Axir8OKSpX-Vr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام وزیر کابینۀ نامبیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/131618" target="_blank">📅 16:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1def7056a.mp4?token=qTOo0MSqNops6vYpKQi7bTdjf7lAiwPS1C-Y3zMWI2MDGvmCXRUCJfowc2egACcpfGzhoFOlpqAXi_lnqqEU_PdeT7zKLgJ5oFaxg-T_JcPu3bsEDHheq5newG7kv2gCTMJ0cNR_EWf19NpCMAbEMdowDtD0_sQNlu3u_0nbPrz_YoaDmX4kNNlbKalQrayBmDmWIxt8DGjoIr1lVQdl8oXzxaWPBxEg9J5jiSa6wPOrP5pEuoo6reU9RCHnzgELbYftvt-goYZMwiBPHQ-Ce71WGYYCtWUvYD_9FmeaoLw0dZDau1hJXk1nSu2O0xdktAkHTmqj2_Poub6Fsd2Nmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1def7056a.mp4?token=qTOo0MSqNops6vYpKQi7bTdjf7lAiwPS1C-Y3zMWI2MDGvmCXRUCJfowc2egACcpfGzhoFOlpqAXi_lnqqEU_PdeT7zKLgJ5oFaxg-T_JcPu3bsEDHheq5newG7kv2gCTMJ0cNR_EWf19NpCMAbEMdowDtD0_sQNlu3u_0nbPrz_YoaDmX4kNNlbKalQrayBmDmWIxt8DGjoIr1lVQdl8oXzxaWPBxEg9J5jiSa6wPOrP5pEuoo6reU9RCHnzgELbYftvt-goYZMwiBPHQ-Ce71WGYYCtWUvYD_9FmeaoLw0dZDau1hJXk1nSu2O0xdktAkHTmqj2_Poub6Fsd2Nmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیمیتری مدودف، فرستاده ویژه ولادیمیر پوتین وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131617" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMhaWwyk7ITp_ZGlnBWnuQgNKH9fxa19RrENgq1lni69BJoHWSNypwZcmg8FkQMHf4ut184CEs5XyCac9AVmfgrisDi7lSEIRMv6o7t3iJ7C40Vt-d-kKO4h0UpH6smsxcJpjQIx3-vIiLeywbdhgCvdTANQBHQu9n9XOFLQc1f7PknwDQ6nYPhf-8Y8WeYkmZ5BvPG6OvMYr0vDMGT_l8zfXQ3bRqqLlNB6q0vA0nw4sDGfdWAFXxS1DSv_znW3_UMC_txbPIsJEyHtGt7zkFoVt8C58kTCI0nIiev1MPn97T0ETQo9nCftUPFfTZpTpMoel9-Qin1wWn3PmOU9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، درباره ناتو : برای آمریکا واقعاً مسخره‌ست که همین‌جوری توی یه رابطه یه‌طرفه بمونه
وقتی طرف مقابل هیچ متقابلی انجام نمی‌ده، اونا هیچ‌وقت موقع نیاز کنار ما نبودن!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/131616" target="_blank">📅 16:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/131615" target="_blank">📅 16:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ارتش اسرائیل:
روز گذشته به زیرساخت‌های حزب‌الله در جنوب لبنان حمله کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131614" target="_blank">📅 15:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131613">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdoPNmNZBXok1qSBFUuUtsYe9XwYWJZWEEHotv_RF-_8MXuz4dtt75jh5fTME1pCRKnkqXdKsWHPjpwGW0p7fc4eqQeXjcvgL2SjYnKCVSvCiurXMh6U_E4xpnppVPnutU24FhloXHv0XzpHPlDVZIkxejNvVgbCBGfgirUVKsNo_VW7PyBMkkmX-xBH6f1nb5n_aVGGR5JpCz9emr6ZxA27qv560u8PJesx2u6ilWwTeMn8cF3dugt9QsXEkJI7llSAbNa_lg63NDppPX4VkOW0SROu8fwGTBU_cAGcZj51QXmDPiIT0vUwVXiVeHGn1aVyc2w67qUpY2B1ZzQpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
میثاقی به اسنایدر:
ما بدون باخت و با سه مساوی از ادامه باز موندیم
🎙
اسنایدر: وقتی صعود نکنی سه تساوی با سه باخت فرقی نمیکنه
@AloSport</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131613" target="_blank">📅 15:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otCSifEwsjuqiMW-JRmuf9hT4mqw2yTaSC9jtvcXNrip2a8ExsmGSq7-zOSXwDfGtreranWNvAaiF6RqwGXi-NeVa3NfAcB1fOLnNDZrj0wxUf2KZyCXVTvDiCHE1yYSg_-M7ALkrZcCa2uaRAkNp4QxUsQBaMemPJ25KwaCCl534eaOUhk7FCR9EBO2WsZNt6PZvSmTHk70PERWDLEWJA7ha4zuh_UmLJ9c5y_vFJUCGQjsmD3eSoNol1CF2ETcxDORvLapTmreCn4dus3ql4h3UgnQ40xiUBr-z6UDNZd9IRhUnjPCz3ZrOyLSni9SWdZydq22IEYXluwPOpDckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلش ریپورت: پنج فروند هواپیمای بوئینگ 777 که قبلاً متعلق به شرکت هواپیمایی سعودی بودند، علی‌رغم تحریم‌ها، به شرکت ماهان ایر ایران تحویل داده شدند.
🔴
دو فروند از این هواپیماها در فرودگاه مهرآباد تهران دیده شده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131612" target="_blank">📅 15:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt01xbCZu8S-iBTAlHwydQPlU6GdvB5J6Jy19gjQSQpH1_gb8kXJMgfFhbCt5_y15FqGg8_YpLB5LrTxGMe0kzcxfNbOQyuO0naC-4efBobLV9l1hNx0NxyW_RLJMVGDt9VC6wZ4PQ3oYuzEDZVoAOazmGlHqat9_GOcB-Y0slUy6c0cpmTP7RFkY_J5g0-Uuk7ztj5Zw1Uzmfx5CcqY1hmr6_H3zRWC7l65hAJz5m0wgXd7VSbAgMTdGLO6E8DFR8XXg8oyDjB6y1vw0t7Sq1EWmhxbWQxHIORQqNEekbbfar44EuA5DfkXV-aX_6V2u8hEpRHdjU-JZZaMcixDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش آشنا به نبویان: راست می‌گویی در حدی نیستی که از بالا تذکر بگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131611" target="_blank">📅 15:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131610">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4987a0d8.mp4?token=fjitt_znSnDNve09W7Bsqq8hc5v7HEHyf1N6fhCPXqbw2nCZSBdBVX6hHymTOBjYg9aDv04kCinq9UErxY-x3TYeZpfzQorVeyBwmDA-70S9M9O1GtExb7ZqBr7fBBQFS6deIMExUfBABEINfUyCGISI1O8bAEcoTuXGkgbOUi8nMQk--pMwjlgLhumsQQB1M47GSDswm-ZgvA8UJXe7mEyF7hi6T_3miUperIHvZHQIkgABgCkTIcqYn3nrxe2dkFvXdLLt4WytxlBcWgoR-l0ISXQmCXevmtkK6D9qVLzCv5uf7jJIJIvumJYpOdriSFTnUh5OHrydBXMOtQnh0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4987a0d8.mp4?token=fjitt_znSnDNve09W7Bsqq8hc5v7HEHyf1N6fhCPXqbw2nCZSBdBVX6hHymTOBjYg9aDv04kCinq9UErxY-x3TYeZpfzQorVeyBwmDA-70S9M9O1GtExb7ZqBr7fBBQFS6deIMExUfBABEINfUyCGISI1O8bAEcoTuXGkgbOUi8nMQk--pMwjlgLhumsQQB1M47GSDswm-ZgvA8UJXe7mEyF7hi6T_3miUperIHvZHQIkgABgCkTIcqYn3nrxe2dkFvXdLLt4WytxlBcWgoR-l0ISXQmCXevmtkK6D9qVLzCv5uf7jJIJIvumJYpOdriSFTnUh5OHrydBXMOtQnh0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عده ای از مردم هند در راه ایران برای شرکت در مراسم خاکسپاری سید علی خامنه ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/131610" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131609">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac7N7Bd7LH-HjwT373e1--HxBs0JoYoQScj7NenRinjwfl417ZBQ3qwJfly0gBr1LkOW7Q7GUoh9egNux5f9LN2-jxJOzxKNT1kAQRirJjS61yuTPTo2Z6pTrXUCmeDk3iQgf9k8G7Ck-Nzl4JHyv99NOa5Ivc-H61tMG3U2cOHP1iAGEqlYTTqL995eyOlRY8OsrLdGCEqFNTy5SRXRIkkmmRDc33sTjMeEkS9VVCoLluCokzgcrU289rWo-RLywO37RvzHuQvHhVf98Fs_o2LfqOzEQxZDAVZCky5u5eQiLbmuCcWbw9_KGt5YH9DPgPhkq9I-1IE9OpRe_VtX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهره خوشحال پزشکیان در استقبال از مقامات کشورها با انتقاد حامیان حکومت روبرو شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131609" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131608">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
احتمال گسترش بیماری‌های عفونی و آلودگی آب‌های زیرسطحی با برپایی تعداد زیادی توالت در سراسر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/131608" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131607">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سرپرست وزارت دفاع: اگر حین مذاکره تخلفی و نقضی را از آمریکایی‌ها و افراد مذاکره کننده در طرف مقابل‌مان ببینیم، در میدان به آنها پاسخ خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131607" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131606">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
واشنگتن پست: اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
🔴
واشنگتن پست مدعی شد: مقام‌های آمریکایی اخیرا فاش کرده‌اند، واشنگتن طرح‌های از پیش‌تدوین‌شده اسرائیل برای ترور عباس عراقچی، وزیر خارجه ایران، و محمدباقر قالیباف، رئیس مجلس، را خنثی کرده است.
🔴
این اطلاعات همچنین اختلافات و شکاف آشکار واشنگتن و تل‌آویو درباره اهداف جنگ علیه ایران را برجسته ساخته و نشان داد که اسرائیل به دنبال سرنگونی نظام ایران و براندازی آن بوده است.
🔴
طبق گفته مقام‌های آمریکایی مطلع به روزنامه «واشنگتن پست» دولت آمریکا خیلی زود به این جمع‌بندی رسید که این هدف از طریق جنگ، قابل تحقق نیست و بنابراین تمرکز خود را بر هدف قرار دادن توانمندی‌های نظامی ایران و ناوگان دریایی این کشور گذاشت.
🔴
نقطه عطف، ترور لاریجانی بود؛ در حالی که واشنگتن به دنبال فردی در ایران بود که بتوان با او وارد تعامل شد و ناگهان چنین فردی دیگر وجود نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131606" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131605">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری / آغاز درگیری ها در یمن!
🔴
گزارش ها از پرواز جت های جنگی عربستان بر فراز آسمان صنعا، پایتخت حوثی ها و بمباران مواضع حوثی ها در نقاطی از یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131605" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131604">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
تحلیلگر عرب در حوزه ایران و پژوهشگر ارشد مرکز مطالعات الجزیره: آماده‌سازی‌ها برای آغاز نشست‌های سطح بالا میان ایران و تعدادی از کشور‌های شورای همکاری خلیج فارس و عراق
🔴
این نشست‌ها طی چند هفته آینده آغاز خواهد شد
🔴
هدف از این نشست‌ها ایجاد سازوکار‌های امنیتی و نظامی است که منافع مشترک را تضمین کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131604" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131603">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
خروج بیشتر نیروهای آمریکا از عملیات ضد داعش در نیجریه
🔴
به گزارش جروزالم‌پست، فرمانده فرماندهی آمریکا در آفریقا اعلام کرد که واشنگتن بیشتر نیروهای مستقرشده برای عملیات اخیر علیه داعش در نیجریه را خارج کرده و اکنون به درخواست ابوجا، پشتیبانی اطلاعاتی ارائه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131603" target="_blank">📅 14:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEfchmfzdsw7HsM_w0SJ_LnLvQWHs4IRae9mPIzsohfyiqgsYTzgnoFsSe0rhXFYRIaJVZT7nDR11zcTzIo8sbwGW4IRBabsEyAMXVHgBsJLOy4uwcT6fXZUxh7r2NDk0JP4SMVmdaBPgUoqe5SrU4e5h-bS-v2igPkRaVhOjDZWFz_LTsNeqeCtwk8OfxrzUyNVwYr56Z91cp-4piDlTvaAqyHZGmOUEQEwHbiYgwbuhQz_bOGaz2ezgkZwJNt0nwurKeMhtUseBTK5LKbfaYXw0rtjeGf6IzMRULaeadNKzrBvWbCxepr_U_qGa7zRKp_I_1l_-OMS3L39ho0bzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0pxGFr55rRlzjIs_RwBWphvZboXDJC4ovhBEBlgf9KYC8Ch8kSd3_j2vyj6mi28mdebunTTAgZn08p7tkdv6Hx0RyaAT4VfwZaaip_3vbiyO4JQ5zKLc8_mTHKHgqjmpj4CYjRSnU0pAs2VVApnKzS4r7hOoRhkfgJj4D_U2St7d57Ql3jF4MHcTDkOkIc5y5fo8OpZPv5dEC3lhyjQDq6zjA_41GU6n-kJrXqJOQkc5280xOdxfaAebj7QpDeAcRJku2UAfPV6OJSWvL4kBhGADgnqr-Z4UE3nHo-HwUAz7tDRRSsW3lIMwvLkUjO5OIvBVeut61dlfDtQ6tc_ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجله اکونومیست حدود یک سال قبل یک تصویر داد بیرون که اتفاقات آینده رو پیش بینی کرده و دونه دونه داره پیش میاد
نکته اینه مجسمه دست خامنه‌ای هم تو مجله اومده بود
😐
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/131601" target="_blank">📅 14:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
صدا و سیما: تا کنون نمایندگانی از بیش از 100 کشور وارد تهران شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131599" target="_blank">📅 14:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131598">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
صدا و سیما: تا کنون نمایندگانی از بیش از 100 کشور وارد تهران شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/131598" target="_blank">📅 14:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131597">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e23cf75c5.mp4?token=ln2lCW2GcP0wfTk2lUKVMZAH7AMecwRINezO6aG0pX9sdpVR2T8zhj7cN3qFjSvhBbkI-ZSNckl13lTkKIQGcVtoYipZM_Ubbc9nCdkaGwzVeY1lNc74UkQzKLk3a-44WGSokAbROs4KTMJIEOml6TAUlM074XGkwgUXOonjTUpLhCw00zJCM4i0B7T-4pCYpwRn9hv0XZhx2NZvAjlpTLSBebxkqslg5kKgicuMoBqOPSbpKsa45GBavXbbiG1j14FhzjQT_I-kqrz4iXCf2lbp3qXt9Zo950f3SVN-PyRvp_thrRAbSKZYfz9khAGA1i2HEhEeJdZSIo-EBpt9-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e23cf75c5.mp4?token=ln2lCW2GcP0wfTk2lUKVMZAH7AMecwRINezO6aG0pX9sdpVR2T8zhj7cN3qFjSvhBbkI-ZSNckl13lTkKIQGcVtoYipZM_Ubbc9nCdkaGwzVeY1lNc74UkQzKLk3a-44WGSokAbROs4KTMJIEOml6TAUlM074XGkwgUXOonjTUpLhCw00zJCM4i0B7T-4pCYpwRn9hv0XZhx2NZvAjlpTLSBebxkqslg5kKgicuMoBqOPSbpKsa45GBavXbbiG1j14FhzjQT_I-kqrz4iXCf2lbp3qXt9Zo950f3SVN-PyRvp_thrRAbSKZYfz9khAGA1i2HEhEeJdZSIo-EBpt9-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گریه پزشکیان، قالیباف و محسن رضایی در مراسم تشییع جنازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/131597" target="_blank">📅 14:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131596">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343711e162.mp4?token=BMyl19lS3ZfnmzfnPBFmZwIPy-f5y5vd102n9PpOUjfOOluynVl9TVfkY17YkNYvSk07korMimXMq2ZWkMYeAa5cs37CL2ngVc0MBEAvvIImnqP_p-Q3Ml_vcHqy_YTHStCmHiAuCOv66UikmSeY_327ttLkP4gd0Ico3A4yZ2UwgdtZw1SC69mi7Bx80-WPBt6_thqZ13123VujEOG5sOOtq-CzaHdkiL2EYheIFc7hAGIlMSCz_hbOJ3OIjQZACY8PF4pyh_PoYXDUmBVyXGwc0z5y1qRkOh2fokbkoLwnFU7IBzjl4RTyS4jjePp4jzDZSmkiii9iut7KoPOVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343711e162.mp4?token=BMyl19lS3ZfnmzfnPBFmZwIPy-f5y5vd102n9PpOUjfOOluynVl9TVfkY17YkNYvSk07korMimXMq2ZWkMYeAa5cs37CL2ngVc0MBEAvvIImnqP_p-Q3Ml_vcHqy_YTHStCmHiAuCOv66UikmSeY_327ttLkP4gd0Ico3A4yZ2UwgdtZw1SC69mi7Bx80-WPBt6_thqZ13123VujEOG5sOOtq-CzaHdkiL2EYheIFc7hAGIlMSCz_hbOJ3OIjQZACY8PF4pyh_PoYXDUmBVyXGwc0z5y1qRkOh2fokbkoLwnFU7IBzjl4RTyS4jjePp4jzDZSmkiii9iut7KoPOVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چندصد تن برنج
🔴
چندصد تن گوشت
🔴
چندصد تن مرغ
🔴
چندصد تن حبوبات
🔴
چندصد تن از همه چیز
👈
فقط برای یک مراسم خاکسپاری از پول بیت المال هزینه میشه
🔴
اونوقت به مردم میرسه میگن کمبود داریم و گرون شده و نخورید بابا
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/131596" target="_blank">📅 13:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131595">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
زلزله‌ای به بزرگی ۶.۲ ریشتر سواحل شرق اندونزی رو لرزوند - USGS
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131595" target="_blank">📅 13:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131594">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a42929a30.mp4?token=OdIzZa4XKJ01lslQkb-8ZJf0R8vpbEPoKC-MzJpaUPupvMdHeO6Zq7EM13-1ylrvI5ki-TMpXo2Bcd50CS_0VPDSp_aQQicn_Nr5suV41wst1eJWnMB8YHJ8rpOMvk9jPAFTu12eD59SLEcAZIfOf4-L_HUoAkO8jhCv0iWL2Oj1wKf26Q3rvv5n7XKo3FJafTDBwHG_w0Xc4T_0vIMxBuzydRx5oWcFcLo7Xoo6rF7VMjuHvwYvoJ5yfL0uGypCCBaSGUqIVT_lTgM7z8uQPqZ6zRg8pb20SL0SH0ScfNs_PRoOLMb-wkzEtfZ9cFV7p0tXZW3dMij-bBQFGcpA5Fq9_Z3TOIDRUIboT0NsCi-_frT-roKMMhoNEUV6qKfNL3pqFjPhHY5Cmd0rVjitrt6zBn8g5kWTVekHY8AvjSXBiUsY7MnWW8N1gjF1nevPhhwcCOnHyLr4HtL5kzTKL0BfnCRGagz98l2BPhWm1YUq4ekWXu_9BThe74cSLGZeJBknziHRgfL2KRoxLc4cQoho0Rqiq7K2L8_x8L_H4zMK_MBwhoQeBGB7qqIfzkfRksQ2FEh_BPScDxpIbgo6Sc_FBKzJ-qZigOtuTnQvmRRAArlxG2nO3m_S_A5zU8JAEMcAl3orXb-KAM-mkI2V0vQ7S8jxtfJ7If1SXFB597Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a42929a30.mp4?token=OdIzZa4XKJ01lslQkb-8ZJf0R8vpbEPoKC-MzJpaUPupvMdHeO6Zq7EM13-1ylrvI5ki-TMpXo2Bcd50CS_0VPDSp_aQQicn_Nr5suV41wst1eJWnMB8YHJ8rpOMvk9jPAFTu12eD59SLEcAZIfOf4-L_HUoAkO8jhCv0iWL2Oj1wKf26Q3rvv5n7XKo3FJafTDBwHG_w0Xc4T_0vIMxBuzydRx5oWcFcLo7Xoo6rF7VMjuHvwYvoJ5yfL0uGypCCBaSGUqIVT_lTgM7z8uQPqZ6zRg8pb20SL0SH0ScfNs_PRoOLMb-wkzEtfZ9cFV7p0tXZW3dMij-bBQFGcpA5Fq9_Z3TOIDRUIboT0NsCi-_frT-roKMMhoNEUV6qKfNL3pqFjPhHY5Cmd0rVjitrt6zBn8g5kWTVekHY8AvjSXBiUsY7MnWW8N1gjF1nevPhhwcCOnHyLr4HtL5kzTKL0BfnCRGagz98l2BPhWm1YUq4ekWXu_9BThe74cSLGZeJBknziHRgfL2KRoxLc4cQoho0Rqiq7K2L8_x8L_H4zMK_MBwhoQeBGB7qqIfzkfRksQ2FEh_BPScDxpIbgo6Sc_FBKzJ-qZigOtuTnQvmRRAArlxG2nO3m_S_A5zU8JAEMcAl3orXb-KAM-mkI2V0vQ7S8jxtfJ7If1SXFB597Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون اقتصادی مجلس: ۲۴ میلیارد دلار منابع بلوکه‌شده در قطر و چند کشور، به‌زودی به‌صورت نقد و تهاتر آزاد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/131594" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131593">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پزشکیان: ایران همواره خواهان روابطی مبتنی بر حسن همجواری، احترام متقابل و منافع مشترک با کشور‌های منطقه است
🔴
انتظار می‌رود هیچ کشوری اجازه ندهد قلمرو، امکانات یا ظرفیت‌هایش در اختیار متجاوزان برای اقدام علیه ملت و حاکمیت ایران قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131593" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131592">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
به گزارش جروزالم‌پست، محمدباقر قالیباف، رئیس مجلس ایران، در دیدار با مقامات چینی اعلام کرد که تهران و مسقط درباره تنظیم تردد در تنگه هرمز به توافق رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131592" target="_blank">📅 13:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131591">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131591" target="_blank">📅 13:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131590">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دلار هم اکنون 175,700 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131590" target="_blank">📅 13:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131589">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d447837fc5.mp4?token=BdF3-sTJnfgGf1pcV8Th0n3tfZiDdwnYDZ5sXpwEu-OwwlZy1ieNnpf-cXNnmeDtE-cnxuKAIUPOc--aVMqWMw5v5qfwPwnyfciyPB0VlRsfkBIHGckIaPnxDt-vBAn3BDcsDKWvl9kqQ_yyZSGEYZhbKJSOE1uS7bFCDCxC8IywMitQaeYBJ6P8qgDPLB0ltinrIsAhp5N9a8GWjuQnd-wyWNJrIpeLhb2ALccBhFott8mRbII1RI5PJi4dq3-bzr6Vhkyhs2mftis9Sk1vcfN5h-l3wLGFZr-lvj05MLxHDo4w_x22d0kHt0qizcjqt0WcnzLo8kWv0wD43i2EMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d447837fc5.mp4?token=BdF3-sTJnfgGf1pcV8Th0n3tfZiDdwnYDZ5sXpwEu-OwwlZy1ieNnpf-cXNnmeDtE-cnxuKAIUPOc--aVMqWMw5v5qfwPwnyfciyPB0VlRsfkBIHGckIaPnxDt-vBAn3BDcsDKWvl9kqQ_yyZSGEYZhbKJSOE1uS7bFCDCxC8IywMitQaeYBJ6P8qgDPLB0ltinrIsAhp5N9a8GWjuQnd-wyWNJrIpeLhb2ALccBhFott8mRbII1RI5PJi4dq3-bzr6Vhkyhs2mftis9Sk1vcfN5h-l3wLGFZr-lvj05MLxHDo4w_x22d0kHt0qizcjqt0WcnzLo8kWv0wD43i2EMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده ارتش پاکستان با استقبال وزیر کشور و سرپرست وزارت دفاع وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/131589" target="_blank">📅 13:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131588">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
امارات : یه حمله سایبری به نهاد مالی‌مون رو خنثی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131588" target="_blank">📅 13:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131587">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=ib3kuZF7u5odnh210UXIQelfnSAHoWPGMmVFHnrGLZWwENKpUlaFdflyju3HWByNu0Xhh3PgFkCRVYmGUmNhM-11RQcmGcg6EJeUoaYfQkPrkAnILDoMe0XNOLWTh6wMmrytSZJQcug6szB7nNYOVjWMBssDkAH2tNYs6OdDGU-Y8_iB8dZjkkMHaeH2WVp_znN_zEO9W10Xr8MS0f2x_i6IqzlQ09eS0SJDb-eUS8FC2rdn3ajd0CGYDVj61gL72QINUqnBHrAB_nAzgn_kbM5sepXvgGl6A8QpBzmMG1Kz056HYm7S9vKfEbhfFM5yoJqb3SBosLJKHtvKObMx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=ib3kuZF7u5odnh210UXIQelfnSAHoWPGMmVFHnrGLZWwENKpUlaFdflyju3HWByNu0Xhh3PgFkCRVYmGUmNhM-11RQcmGcg6EJeUoaYfQkPrkAnILDoMe0XNOLWTh6wMmrytSZJQcug6szB7nNYOVjWMBssDkAH2tNYs6OdDGU-Y8_iB8dZjkkMHaeH2WVp_znN_zEO9W10Xr8MS0f2x_i6IqzlQ09eS0SJDb-eUS8FC2rdn3ajd0CGYDVj61gL72QINUqnBHrAB_nAzgn_kbM5sepXvgGl6A8QpBzmMG1Kz056HYm7S9vKfEbhfFM5yoJqb3SBosLJKHtvKObMx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
دیدار رئیس‌جمهور گرجستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131587" target="_blank">📅 13:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131585">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحرونوت: انتظار می‌رود «اسرائیل» برای مدت طولانی در منطقهٔ امنیتی باقی بماند و این منطقه همچنان یک میدان نبرد فعال باشد؛ اما این بار با اجازه و موافقت دولت لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131585" target="_blank">📅 12:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131584">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شرکت آمازون سرانجام به تعداد ماهواره کافی برای راه‌اندازی سرویس اینترنت ماهواره‌ای خود موسوم به لئو(Leo) رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131584" target="_blank">📅 12:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131583">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
گروسی: درخواست دسترسی به تاسیاست هسته‌ای ایران را ارائه داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131583" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131582">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
🔴
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131582" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131581">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeFTnzq99Yf7iA6q_5IULgafziXOTVrsAJo_SrkMFN5RUPgMAIWwHRQqML5ZnlMieoKsmsl8DvvH2kSNt0nvb5kL8Bijs2DqJNj0bMSPWxSxH7lrkwjmcBNXFb2Dct7ld1NwYcDQDmuKIEumGpCo-LWBy6gII1f2H4cMypbj3okMYi0mFp-Pg7eJZHLhBrIcNrQGza4VBGdNydibhLTzUATQNIPukixAM2tS6gtzyEk27yG_RMTSzbE0-VWuxBQ4Hf2kIBN5-8o3Ia7tj1l8YoFTqjgaOQRwzlvgFbRExqF0HNFlt4gWC0E7Lmor0kwPpXIrOHp39c7dZ2snzP7lqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
15 سال پیش در چنین روزی؛ احمدی‌نژاد: به هر خانواده ۱۰۰۰ متر زمین می‌دهیم
🔴
مردم بروند ۱۰۰ مترش را خانه بسازند و در بقیه زمین فضای سبز درست کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131581" target="_blank">📅 12:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131580">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ab2ff613.mp4?token=Vy5t0p2S1M1ytstMbx0rR21zGbJPON6jQ7O1jwtXZeQEu1lX0bJUZli9RBCoNMKukVXvIlWa853_hSFz02BvciPfpzIxKV59X3ATbfDPeG-H9iHL0rzDy8Z0-RUFXde1_zW0hZj6aO1fwMZq3SN-KmRULGfgU_4qwgeVjYbyWA2wnkUQHELKrOy6eMwlwQJC_FbPz0x04tsZgQPzsCUg12GVTXHWWxN9TdGMw35SxQzjXfDkR1Bh75e9CwhLXP_WJZfPfPZ9ORDCEn9NjirXk0S_YSRf2C4ndSbo2_Tnow98bN7bmt0-OeWsSbHmZCk7hY1DhRHLEzC4KSCsxvto4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ab2ff613.mp4?token=Vy5t0p2S1M1ytstMbx0rR21zGbJPON6jQ7O1jwtXZeQEu1lX0bJUZli9RBCoNMKukVXvIlWa853_hSFz02BvciPfpzIxKV59X3ATbfDPeG-H9iHL0rzDy8Z0-RUFXde1_zW0hZj6aO1fwMZq3SN-KmRULGfgU_4qwgeVjYbyWA2wnkUQHELKrOy6eMwlwQJC_FbPz0x04tsZgQPzsCUg12GVTXHWWxN9TdGMw35SxQzjXfDkR1Bh75e9CwhLXP_WJZfPfPZ9ORDCEn9NjirXk0S_YSRf2C4ndSbo2_Tnow98bN7bmt0-OeWsSbHmZCk7hY1DhRHLEzC4KSCsxvto4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس‌جمهور عراق با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131580" target="_blank">📅 12:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131579">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قالیباف: آمریکا و اسرائیل به تعهدات خود عمل نکنند، اقدامات متناسب خود را از سر میگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/131579" target="_blank">📅 12:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131578">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f39132db.mp4?token=vVPl7dowVH6y_CuYf3e8hHTAqBuYdMZaGZENNHS4Y0J6k32vr7vlkwjnrqx_JsKXY5Y-6kYd48l6uC2WM3sGZtDVnjZfwddT6GpslIM4dPGoRFlWnuX6IKsFDr-YFINbwt9n6elIdt3fdHu3SlBELaN8KuPZqt9GmzwmUhsVcazYnSckxO_VdFIjonYW63U8kpcH7F9fFvYvJiV9Z8gRguVnijsP6dQHrOzDEWj62RIaxufV-mUx0nLa-g7bUJd2xqd-_SpatI9VZgYqkfjI95Xc1AgOhgx_Pc89s7Pal0yrqXhpOqx9e3s7V5iuiZ6wLQtWGElSF24T53JXwmUdmgvWI5-Bvuq9FrPGrtzZD6s3QxSOqm4d0hJ8LtaoRsjJdnUnsvtrmIBQ9faEzqvcVrk_PCCaLg8_Pn9uRtjwFLpLE8yMUgsv_UtSj-n3XO2O2yDsY_NoOeyJnJxUF4IrjXzx-NqD5VkTWccnbBYZeB3oItE_SdEXIGY5_Ly2963BKwxWLvI1JAbQKyXORqNodRYkn9-1bg0MlZGE4Am6VYFLQOewdQwQGNoRaEi4g9wslpR-a6Cj1ThL3rEBxSiXIxo4gFLS1xlYr3Rer2Qi6XJYNkb8B47J81vypC4OBk1bgcL-NT67griQU9ui9fMzHU-yUn8-GO-M82A17T5bqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f39132db.mp4?token=vVPl7dowVH6y_CuYf3e8hHTAqBuYdMZaGZENNHS4Y0J6k32vr7vlkwjnrqx_JsKXY5Y-6kYd48l6uC2WM3sGZtDVnjZfwddT6GpslIM4dPGoRFlWnuX6IKsFDr-YFINbwt9n6elIdt3fdHu3SlBELaN8KuPZqt9GmzwmUhsVcazYnSckxO_VdFIjonYW63U8kpcH7F9fFvYvJiV9Z8gRguVnijsP6dQHrOzDEWj62RIaxufV-mUx0nLa-g7bUJd2xqd-_SpatI9VZgYqkfjI95Xc1AgOhgx_Pc89s7Pal0yrqXhpOqx9e3s7V5iuiZ6wLQtWGElSF24T53JXwmUdmgvWI5-Bvuq9FrPGrtzZD6s3QxSOqm4d0hJ8LtaoRsjJdnUnsvtrmIBQ9faEzqvcVrk_PCCaLg8_Pn9uRtjwFLpLE8yMUgsv_UtSj-n3XO2O2yDsY_NoOeyJnJxUF4IrjXzx-NqD5VkTWccnbBYZeB3oItE_SdEXIGY5_Ly2963BKwxWLvI1JAbQKyXORqNodRYkn9-1bg0MlZGE4Am6VYFLQOewdQwQGNoRaEi4g9wslpR-a6Cj1ThL3rEBxSiXIxo4gFLS1xlYr3Rer2Qi6XJYNkb8B47J81vypC4OBk1bgcL-NT67griQU9ui9fMzHU-yUn8-GO-M82A17T5bqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس‌جمهور تاجیکستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131578" target="_blank">📅 12:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131577">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رئیس مجلس عراق با قالیباف دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131577" target="_blank">📅 11:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131576">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu2LmvJAup3kcgL5U6c04EEr4_hWoAOmcQ4OkqMmIe5OH0NQGnv5SliMsMAqf4UvOtiMUI8-alfHPDB5qzkOVQdKNViYgNioPXJmr7DvPBUVYRa03MSd0pWqNUNVqF6o7epKDDIZSdMbNTuTeFuyGFQYhCG1SB8_Pcx_nieEWeqxQJCaDPCQOkTmnXjfpxqlMNq9COQaHgNC4sJaBKx3F8Tur80if9hxwYaQ1HETWGhKjxPfg4sHwkMQKLh4hNHo8zQsIDCrEq0Mo3O_T9UcS3wkVV-V1SRMDXb76gqBzdw7A157gGqFSRNtWNgvEtLuXX9w7OJg7RF30o035pYZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس حوزه انرژی: با روند فعلی تنگه هرمز، آمریکا به زودی عوارض می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131576" target="_blank">📅 11:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131575">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رئیس سازمان هواپیمایی کشوری: فضای هوایی تهران دوشنبه به طور کامل بسته خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131575" target="_blank">📅 11:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131574">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیرجهاد کشاورزی: هیچ الزامی برای خرید کالاهای اساسی از آمریکا وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131574" target="_blank">📅 11:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131573">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سپاه : «خطای محاسباتی دشمن با پاسخی کوبنده‌تر از همیشه مواجه خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131573" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131572">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlmITyIF0GCdLhHMvHT1kK6jrp3B2RgIVuVmi4dLmY13RJJaE1lZIXjGog38LBT9x8JY68e_xmKfBIlh01FyfRAF2GoHpcrBzC9NuN16IpuLM9HaMkqjlFqVgmBBPq-rcvo-EP3H6r6EC9q80KCkO5IGMhxprwuKxkBskyd33BhKk7b2Jq8LLJscf7WGvg5IaSs8omWwyRkWvlDTWqyFs14MiI7NpWGdTP_tA5ZLalRQtCnzwZkCVhkY84HPwKLn5VPJk_J_O-U4kuo5ECyP6la-jfSiCAfV8EH7vJItrEAZmT-K-Z9W7ubJB6ZbHSU4D-gEm5W9G9r0iKPhtsfLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از پل ارتباطی دو استان کرمانشاه و کردستان معروف به پل بین دو بهشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131572" target="_blank">📅 11:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131571">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سخنگوی اتحادیه جایگاه‌داران سوخت: برای تسهیل سوخت‌گیری، تعداد کارت‌های سوخت جایگاه‌ها افزایش یافته است؛ هرچند اولویت همچنان استفاده از کارت سوخت شخصی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131571" target="_blank">📅 11:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131567">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OuGGaDLBCBpBEhRZaLuei-wpxypU9XHdizhW2Pg2ITCR08BLsaOC29IVi9PSX0iDiEbQnubxtTZk7gvn7Gy-bSIoxP7Zwhvygyi4AK28bbhCzpGNP8XbmkBHJx_qcYEdJxHBp4slJtblJAS5XuOAjMOnuMPUhBWTFnY76Iw1qYJZ5u_QFAzBR5mOKfaFjbbUFLvCdtneCYWcuur660l4mBcezxJFshgWmdsEwPlVvfx3k67wqdS-O4RqOECXguoWCJP6ftM-_a6mdiDcIN27Oud8F4nl2NXuRhroLO9DMjpn8P07PSlzZeRboRqgqd6RqRa6Lo1kp0gqpAsjGNemRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knIZ3mx7HD2rN2HFhNjbQHVy89XdHVkGCS4bygKl0kkqFOiSrnyNR06PDLobjkb7igwx4_4324MTVN79z4slErFxqZ1VHblVdDO80-J7xwepVqQSA8QsUJTOolSXnUf49jwqMMEkpbRTGuwpvjXA23t4alQHRcVsI9KDA-opk6ai3_yhW86R88cCEOTQ79o5Qq7GVZ3Oy89iZfr1CNpk5itG49dr9zEmlsNr4Wl4wwtUs7NwvEqz3r6vZLC0RQCIyo-qNZ0ndZF9kYJxWFqx9NFm13jdM_5LT4L3Eg0PmoZ6-oaWqzKx3ZIaJU8Z4YnVbr4yDacUpSCabiRzliFLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8fzRjl-2t_AxF5uiV3F16rghNrkxMzv0Q3fM2Dk4nKpZtB9C1ynw4a-6PwiJ9Gpk1BB5HMjSIawqvEGt0RmLlBOsbG6-0b2S7uaDA6dYOxH5FRu4Y8OcPAu2pD9TIwNeQnofzT25vdLKQ5Hi8ECey1pKgOpw_blxXl_QtBDi4KjLuWTo-pYuZuVX7hRZ4iz6FlA6WFOgEpBQCEH_Me4MMaCRLv_7-b3Wf13mHhHzCcKbv8to49IZ8JduktgRCQb-SwmWJ_SsmAG2wD2NOXAdQCcs9uCZfVNFbIkolJJhTnuYLy6GI3qYDO1cL5n5jZvf-DNWsogMZxf0HtE48jKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJWyYdUQCXULwuLWUPaX5Bdste99UvEqWdu3BSIzb4oX5xhzR3bDZagEa1i7LRv66jAMW70ep1rrE0me_X7nJEPUUS0ouQEhFn_Nmw2k3FM22vRMmil9IFQKS1JZLlhi6qsF7WEQ1ipU7e1ZEU4DyxqLMV_Bh2wCTLjAhEBUusz4HJ0D-opwIIRRNoqkAlrHMKNXFC3URccb5FG8-waIk2LiSTP-F_mUHA8_E8vU_CA6EIbS7Sz-iGXugieK7AvboaVqjo1DJ3Iwj0YoZ3EIskDr0yQAskUa9Cj6mIQoCZuXst_6Y4pf3HQxoJ2nkDWtJW3Ov0QxSGwJjkyCQq2amQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار نخست وزیر ارمنستان با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131567" target="_blank">📅 11:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm2R4YT4BeB5cavkZAPBjGjeow5oAozGVS7BNb__65DE6QbeXwwPnEyhdxXbyfV-RufNfakzT2dQNHBOpz70N0ODkYUDDfLlU-8iCYJJ4-F73iKGoJ44gErzp0EX54QqtBKzzbG8w6lpPwEpGF2g2pzYLxDdPbr0Oib_sA-d4NRkPKlHAF4yF3vaxLNYGu22VqI5PWBE7eTZDlOvCxIuLIh8b0Kn06ObbEw1TQz3BCh-kq5oocqpOW527z4t5-diQm8yLgervjzdbgoJijZLjo8DyY8YldoGWbOH7t8ef9NocinqcHFLHqIyU3fpucaq3RIUiiyxu1XDg15SMEHKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIQH9TwFYTRwHmrOhoZP1eHwFpF_vH-LQZB9t7_PO-NFn2sG1ChlxUTEmL7jWtXN3dx8QoroGVZsYZyteFL51yIJIM67EapyGa8OHP60ZDRBf_UNc4AQk3rfGsHebvvFJ6UhOx8llZMYbS65CoP9ra8TiDIQaKZIwhQPQ_q-jgLjA8u2IffZOzzTgThJtzjO0QRKeAP-Q2YwlQeQUV0KlVNRxf8dMIRv8fdL5SJwip9Zcdb4tzBFbZsgeysWrH3lic0_kwwk4ErVr6j72qDWXpzLHenF0F_Y-QsZPPTTklk3GAMBuJhp0h6VZJyfZlOBdBee0Zrs8CzdTbd4jyYo0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
براساس تصاویر ماهواره‌ای به تاریخ 7 تیر 1405، آواربرداری و پاکسازی اغلب سازه‌های آسیب‌دیده در جنگ اخیر در حال اجرا است و برخی از آن‌ها کاملاً پاکسازی شده‌اند
🔴
هم‌چنین جزئیات موجود در تصاویر نشان می‌دهند که فعالیت‌های تولیدی در بخش‌های سالم این مرکز با شدت بالایی دنبال می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131565" target="_blank">📅 11:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131559">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XbjM9wt9qhPYe_q0Bw-LbCwsK_nP7IK_KksBncm7ITNv-qUPcmqn7P0sxLsi-0eIM5F6pP428kr1Y410B7TiMZTEvzQ2V6MmKRk6uHuFknbOLhlwRe2SY99R6ei0XuwcqcQkjJCSIY6zF5KLjRHQzPCajuoHUPcmiIiIo1KMMDZFZplm0nVEQbpAvfONkd0aFQNS0KSlHsw22AZPYcT0zkUQgrP2A7R8KD8QTNGRTDIdVzVt8iBhNEE4v36RPNdRqxtX2zhOVlL7xdOjXXFM4FSysCEDNYZL8P9o2Ks0JpcVw-bdn0VLSNRZotVj5C3DvqFMEsFGuQ2a0u5TXgKDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S328FWSBbdt39PwaR6tiF0aRuLGYEOTEtJ_FrGyMoSnQbOZJem6EGHOwndYlDOO8T_U1Wj9HTg8lK0uNqs_FryMpWWiyrfR2pYVSO6B-OBG0CKW9zttt3aSLr4e6P9sPTQMHPj25_nbp8fZI_Y22DwY_UGNCn1sZ3d_yQGxyDSSCXdrCEU9q2D_XMI4JtvM6pEg6dSZmBlScLJRRXfF8bn7ksqFfWa9i00r1OtwwBuaIxfZ9U7EGiV5Q3hms4_jO1mS8NI08EjeUtJoY-HMaO0a7J_ZuEHIxn4zi_bnMRGwVgR0nDjZf2TMhE7lfahayAeLawrIsq79L6Ra8KqXR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7OrPmd3_Xt_UT3em4FH4niOTz1E6QIFLzDR-QsFZrc1Z9HQwEbsk8LOK5GTz-Wi8YaPNCbGJQWsOHYw65Jt8BIkDFW0k4AyGJrdF7Sbitxx4oGV5G3q6Q68sbEkW2uj67roUIednTJu0kbPJjl8AlD2_h_xCbKoGkKqp0Z7daARym-b7UXX4HrFA9IqEWf8jT4DKZaFZ7U89U7TgpsImjwfmo2UUJwvu188Mi54TVEkNyiD2YLaqcMoNHJDVVQQRe4r1bIc_CKNhRRV3q2clLvT0JFMl_ytwa6RKgH8O9bkS0TSyeZGZRmtKSrcPk_dEictBeVyRcU7BDRYlKpXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwswPVtGDjlt3b39NMt_TrME-0fOUDHHnykqHVpyCsbBu5yISLhrm8xIbye7lfjvbn05svE36g-1Eu_wSpjjOY0ovJ7oTzXRFNIRTnTRPBT8RF1SswW3sTBH9PYljDayxXM-FQs2kWt_fRrzSlKTv8gJ8u0mcMS1ULM33vQwm-x69ufhJnT2yr0TPK9_DO0alvrFY0guLlxzPJO_CPLolGPDuhUxOHrUE9i8MEQWqLMicb5Mlta1jAkoNZWAtxP7sdgOhaT6wWLDOIKePM5TNhbr-Nwg8-429cUdx_j-FoIyK_OmmBiaqDw07F1YvtTCQT_84umq2de6SoS7dSzQaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-H21vl6HizyfS0yljGKh-1KmGsn9ItcYS7tErwENkFvVaO-InO46E9X4lqn5pQS1SV2CtegyLgv9PubBbFOwLFcZ4EKbKkRZ2OBnK5EXavyqBQwzpF2gk8D1W7vdBiKcVQOqS6cW9Tc9tG13Ly6pYM3n-wrtSQP2htiaN3p0n-aFAUR0EPsatWZRF1qp-B032lnbORI61Y0WvIMK6YPhwixB6eAMs-5sHBHlCvq3xDQ-u00eHjXxPxh9G8K3EvolGyCi_oCXG3PJ0pFMLJxQNkAXVHU7fBtj4HzPCUSTkzYUzKRDWVrlHtq0HtvfN_iV6vEzF61A0IZUyvQCgsCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bE3DLR8Y95l3ts2A76dQmoST5NEaBCzwXNW1Hfe513s6wBSr1tEDove_BYcUvMdrMaXR4Gum_Xfogf7Xh3-Pe7l8hHqDjCu1TPAp25Hv6g24UxdkH-URc2kx5u12S6R_9dD4UaQX0-vMezxcRl5TENB0OlmpKzdZ5aWVRYc57Y6kzjI2imULoC9Bt_cwp81WX8tYdaGk9C8HunN-hGN2lzEaFCoN2xOggTQwquEwKkj-G3GemqPJZ6WoFRaMBtUySk_KjONl90GzlVoG9aIsR2Yy_Gl-EbJygV6WoYseplI-xexIHgOLySHSPDnnksxLYRvNXqdfOOdvfPx1YF4lhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار رهبر ملی ترکمنستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131559" target="_blank">📅 11:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131556">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ci-xzw2WI9P1zmf5y3d3PcekclopNtaqb3Uki2gE6h_v-5TZPx3NxnId2yBe-maC05fJ3t4vkVbHjY-iYzJHJwuL-wlzpwFRnK-Y9_Te6EZPHNKjFernMBTm0U5NJursxdrvGIthqOTdJrZLZMGrQj1daIh-gmUsOV42pXpkIexKoh8DiV22QMl9cm-nRBYUHvHKKcd79ojgMI9VP5g4dOm7_sTuBwh4qjBan_DYcOCnaYSgRDFRKHhU8wZOXqzdCD1J3Q-zkjgpXXabHNvosfZP7jsi7ILIWs7HNpFr9VL8vHgHu8T8OnS-SkWGbBpVIJpxvN4BtYgOq0tOJmbiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5t5zIeqtIVvw1Pu8-LaDor7wICYpFALlN8OzQBQOYG3Ov9218jvY7jpfyrrW5xe3qgK5LDyECHePOIG77FR-qi9oGssXbBLWhwaxgNBQa-NgzJv-Dw8Zxw5rDDzsvHg1B015pAW4c1CfX7-OcJ6OkMn5G626V-RfON8GOs6bVY0MjqK-FRWny9h8eBBD_uH_lcnZrOQVLz7UNkZwt7eMoynnRLGSLwnLzRDT3QadoUelhPt-k2aAzj0_ZOn7ljjP5Y9LmxGdEjSM1HjX5PYPYKCTcheGA0fdcWWqoVNC2E6Nii5tUFLkpZyFrwho5I4GUN7bnurhWSxQHQCXgTZog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjuy2xthdUnjXSjOrAOHBXEIsoijT14q8n57yiTYIkdu0JQee7RBj8A3Zs7jdtmqW7UY006ddY4Y7iKbOHWQy62PqlrmTmuY4_2-TjWo3i0ErKfQ345iCrXNfArrvUsK0wOVkESebq8cWgQfXhFnsLvV3BbDRLfTgr26CEzN8sBQib7_VugylDPs_aXgQyOvoH_OcWe6sZpo7aA2MOKuKvtMBYjgqQ77_Q6ki5gKsjPPrcWWxjrwKbDhxPkxfyWTxca1OUCHwqfz9d8IEvPWK7c3wb9MQzEjslJLRCTunQJn1QX92_eprzUCwbsX0K8vSE230QCU6A39cTCVkcQ-rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار چارلز موبیتا وزیر کابینه ریاست جمهوری نامیبیا با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131556" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131555">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBySMeYHRuiqidbtqFEHq534tNYERyV4-6F1mgjdWCLUwYSuV_YEa79-yW_r5HZXbNnm8yInmiKQXvWuezZhd04XIttuDwkB5cNd5OW-ICy-KCENxcZD08avuLCUiaQb6xXZadb5PFCplIz2vGq0RlK7WCdKfImjd_rQHIQ7qYv3W4T2Vj6T5oGi8RS8rM86wSH0SasqCGBMQHTO3mpuc-XCJkiWuIEDnmxqPdp2NXdgmGGQvjSEk8TGXo-3ONfba6xzISxSCdVU4QY9WrqRd0BzSyjn-xUCig1t7EMJd2lHF9gb9lTzYKNtBdzc-d5gSesH_8kPjWSEJFOedtmnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت جدید ظریف ، وزیر خارجه سابق
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131555" target="_blank">📅 10:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131554">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
قالیباف در دیدار با معاون کنگره چین: اجازه دخالت آمریکا در تنگه هرمز را نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131554" target="_blank">📅 10:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131553">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9742057ed5.mp4?token=VU0vYz95mTZyV--xJJ2VQESTMeECJtIAzqMZUu73Wgz6jnxARL13SLNS9kWeO3eRLdVQIZcnHI0ibtdq6I-Z6ealVviJeNMvy0UX-m7ALKju1sQhg2iVpw5B9fBk2ydXaxxlKj4aEQDbjgDd5KU6K15dHr-2xTq7e2obo4rEpjU022FOGO0gv1NZYXwk2wNHCUcc52KDFlCrsq_McBcBXQZgQ31EO3qSShZvg8kLmP2_ZTRviaiVUDI--I9_5pal7KnJx59ktKCZrPCakSWhrP8KGABMiK-IkEq7zQVjTlBdgza1X9Ukvk6q80Terb5Bmcwp_ZQrDdv2R63JpZMrPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9742057ed5.mp4?token=VU0vYz95mTZyV--xJJ2VQESTMeECJtIAzqMZUu73Wgz6jnxARL13SLNS9kWeO3eRLdVQIZcnHI0ibtdq6I-Z6ealVviJeNMvy0UX-m7ALKju1sQhg2iVpw5B9fBk2ydXaxxlKj4aEQDbjgDd5KU6K15dHr-2xTq7e2obo4rEpjU022FOGO0gv1NZYXwk2wNHCUcc52KDFlCrsq_McBcBXQZgQ31EO3qSShZvg8kLmP2_ZTRviaiVUDI--I9_5pal7KnJx59ktKCZrPCakSWhrP8KGABMiK-IkEq7zQVjTlBdgza1X9Ukvk6q80Terb5Bmcwp_ZQrDdv2R63JpZMrPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشت جوان پول خود را روی هم گذاشتند تا یک موتور بخرند و نوبتی استفاده کنند...
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/131553" target="_blank">📅 10:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131552">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فایننشال‌تایمز: ترددها از تنگه هرمز چهار برابر شده‌است
🔴
یک رسانه انگلیسی نوشت: اعتماد به آتش‌بس افزایش یافته و ترددها از طریق تنگه هرمز در هفته گذشته، بیش از چهار برابر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131552" target="_blank">📅 10:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131551">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزیر کشور پاکستان پس از ورود به ایران: اینجا خانه دوم ماست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131551" target="_blank">📅 10:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131550">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd05539a.mp4?token=nRa8zF_BIJwa26SQzRtKJ6fvZkrvjD_PzP1RY83hkxvtIswzJXyiPQSRAAf-mN8Qp-Zm_kQD1hsxk2ALiefJW5fhrJtFeAdIta86YT1Cb6zaBIMyLzhBYSzu-tV1VtxN0uJAtHXSZbgkaxdL0UMsThCvLOEQpZAnk4ih38xyfoprSjSGGqEKSq02acHV4IE65Mvnvh45xq93DT_UPz1VoFQmoodadLhAIj-B0rJFl3njzm9TuOJ4J3l0MgN7HUGWqH49nJNx_zIYuOOrBpfiTtU1luy3N-hsgm685gRpQlVam9G6kcR9TxJxweNuczKJRYM0Ic2tjXEBnjHS9837mTGxTdOHoqEl5kBRohxoMA9Bc6fA9KehlRGAreqmXfceC_HIStubYMbmpZm4TYyhsG0IUCBu1WXdmOj9oyGZYHlGUCYKrlQ-Na-UJBWD-3C-yCOIAMeiqCxzXePyLNrQgih5w1RIq45wqth3JmJ28GzIedL6JOAnDLtbkd4L1OcF-fGTumjvJCnojMUm5paENYiDa7PWEKVF3sFuTWR5iEoH4RinFbO80i7F4evL54w5p8y4y95IzVkCDvD_RUj1QY9l7fi2AXWLUtDlg14nYl2_twNZsukBQOBeAKDnPsASyGItiD4SBFDz55IPgPKcp61a7fIxxb8WBcnJ-mh-3e8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd05539a.mp4?token=nRa8zF_BIJwa26SQzRtKJ6fvZkrvjD_PzP1RY83hkxvtIswzJXyiPQSRAAf-mN8Qp-Zm_kQD1hsxk2ALiefJW5fhrJtFeAdIta86YT1Cb6zaBIMyLzhBYSzu-tV1VtxN0uJAtHXSZbgkaxdL0UMsThCvLOEQpZAnk4ih38xyfoprSjSGGqEKSq02acHV4IE65Mvnvh45xq93DT_UPz1VoFQmoodadLhAIj-B0rJFl3njzm9TuOJ4J3l0MgN7HUGWqH49nJNx_zIYuOOrBpfiTtU1luy3N-hsgm685gRpQlVam9G6kcR9TxJxweNuczKJRYM0Ic2tjXEBnjHS9837mTGxTdOHoqEl5kBRohxoMA9Bc6fA9KehlRGAreqmXfceC_HIStubYMbmpZm4TYyhsG0IUCBu1WXdmOj9oyGZYHlGUCYKrlQ-Na-UJBWD-3C-yCOIAMeiqCxzXePyLNrQgih5w1RIq45wqth3JmJ28GzIedL6JOAnDLtbkd4L1OcF-fGTumjvJCnojMUm5paENYiDa7PWEKVF3sFuTWR5iEoH4RinFbO80i7F4evL54w5p8y4y95IzVkCDvD_RUj1QY9l7fi2AXWLUtDlg14nYl2_twNZsukBQOBeAKDnPsASyGItiD4SBFDz55IPgPKcp61a7fIxxb8WBcnJ-mh-3e8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مأمور پلیس آمریکایی، یک زن را به ضرب گلوله کشتند
🔴
مقام‌های محلی در اورنج‌کانتی آمریکا اعلام کردند که سه افسر پلیس پس از مواجهه با زنی که چاقو در دست داشته، او را هدف گلوله قرار داده و به قتل رسانده‌اند.
🔴
گفته می‌شود تحقیقات درباره نحوه عملکرد نیروهای پلیس و جزئیات حادثه آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131550" target="_blank">📅 10:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131549">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پنتاگون: اروپا مسئولیت دفاع از خود را برعهده می‌گیرد
🔴
وزارت جنگ آمریکا مدعی است که تلاش آن برای وادار کردن کشورهای اروپایی به برعهده گرفتن مسئولیت امنیت خود، موفق بوده است.
🔴
«البریج کولبی» معاون وزیر جنگ آمریکا در امور سیاست‌گذاری، در صفحه شخصی خود در شبکه اجتماعی «ایکس» (توئیتر سابق) نوشت که ائتلاف «ناتو» اکنون به سمت تکرار وضعیتی پیش می‌رود که در آن «اروپا مسئولیت اصلی دفاع متعارف خود را بر عهده می‌گیرد».
🔴
این مقام آمریکایی اظهار داشت که هنوز کارهای بیشتری باید انجام شود، اما واشنگتن به حرکت به سمت نسخه جدید ناتو که مبتنی بر مشارکت، نه وابستگی باشد، ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131549" target="_blank">📅 10:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131548">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
به دلیل تهدید مداوم وزیر دفاع اسرائیل به جنگ و ترور، ممکن است در دکترین هسته ای خود تجدید نظر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/131548" target="_blank">📅 09:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131547">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سرپرست وزارت دفاع در گفتگو با وزیر دفاع ترکیه: ایران توافق آتش‌بس را با هدف کمک به بازگشت ثبات منطقه و به درخواست کشورهای دوست و همسایه امضا کرده
🔴
اظهارات اخیر مقامات آمریکایی درباره گشایش جبهه جدید علیه حزب‌الله لبنان می‌تواند کل منطقه را با مخاطرات امنیتی جدید مواجه کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/131547" target="_blank">📅 09:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131546">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
میخائیل گالوزین» معاون وزیر امور خارجه فدراسیون روسیه بامداد امروز گفت که مسکو آماده است تا مذاکرات با کی‌یف برای پایان جنگ را ازسر بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/131546" target="_blank">📅 09:42 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
