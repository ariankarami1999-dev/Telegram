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
<img src="https://cdn4.telesco.pe/file/ODlY8868Vc1bENeazxxYpXjdBdUGsMLwuS0XrzyVImHYtcj4yEkilP5ymy3ES7TdD9EHKzXC5N90Nx558M445Iu5uylHm4eI6QEFbyQWGnbtZhenF36IvwGZSKy08as9_sBKxlfCQjbdKY0zpb-EOQRnHFGPUAlJywFMwRZifCmewZ1IZYcmvWV6NYBiGTNoGCl07zgIZkY8UV72bEQY_0Za1STc8PX8n9Y4uL-_YuqfM-gk_q7yp-w8HGzWLyQrOkNXQ_ZVBSkwWFeFNij3xk6uC8xornvXh3zBlmNDL0Ite2CEfIqAlvj54hCtSveClKznu7LCOgb8drJVereXkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 23:41:19</div>
<hr>

<div class="tg-post" id="msg-124318">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ae224db9.mp4?token=td5l8wCntAsYS1EPgeswOPUNA5sV3vmWt25QGFnogTONoFWO2ADBhpQkg00TxXoWAClZy_XSe3UNxOUhz6klCsiPJupD1WnF0cGtBvobV0pL4T1xLkPBngWvzUBK73RgapLZTSgO-8gicxuDu_0u9CwngdMgm_hZotcPgle_OliXV-XzpahpDCJS_CcUhD3UTYTU2lar2PLawDXZ5Nkz6up2r791dtoxJPAhPrhuolss4iHbt16KDQjYXqJgCIofEht98_-6X0s4BlbULUl15rggpN0QprE_ynqGE07fndf4qCPVpPj26J3MeP58-BLFl20LKQbgpm8a0Lk29Xmocg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ae224db9.mp4?token=td5l8wCntAsYS1EPgeswOPUNA5sV3vmWt25QGFnogTONoFWO2ADBhpQkg00TxXoWAClZy_XSe3UNxOUhz6klCsiPJupD1WnF0cGtBvobV0pL4T1xLkPBngWvzUBK73RgapLZTSgO-8gicxuDu_0u9CwngdMgm_hZotcPgle_OliXV-XzpahpDCJS_CcUhD3UTYTU2lar2PLawDXZ5Nkz6up2r791dtoxJPAhPrhuolss4iHbt16KDQjYXqJgCIofEht98_-6X0s4BlbULUl15rggpN0QprE_ynqGE07fndf4qCPVpPj26J3MeP58-BLFl20LKQbgpm8a0Lk29Xmocg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روابط عمومی سپاه: در پی حمله ارتش امریکا به کشتی ایرانی  " لیان استار"  در محدوده دریای عمان،  نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی  "msc. sariska" با مالکیت دشمن امریکایی / اسرائیلی را  با موشک کروز مورد هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/124318" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124317">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxDjjUuhavWZaRKHpsCeRk_eAWSmgiB6-CdCS-h3unceQ-tY59VZz9VeIyHiWypcy6WuxCeJouNoswKrgYqiV0aBU70QIZ4nIBDJZ-mTTZ4WWX3QE0btz5UUdAIAuHCcPxF3sAI7eTAwF4A253V5qWuLs45hCocz6lYiVUFx2VDghbiy3kNXu18uCGPdofR2E1LFGDpHrSZVYHJ_YmmiAckE63med4maARpvm3shIa77FN1HjyUn2JCcZHMuAf9lCGpDBpdt8iY1_RVHPidOrGXdR_R1kWDwMSgq6OPUNy__3PpyKct9SeN_1F9SoP7a5S6jrO6oLt-JtYnvFifaAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴ سوخت رسان آمریکایی در نزدیکی مرزهای ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/alonews/124317" target="_blank">📅 23:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124316">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvUnQSJOIPZfQDeZ53P4tI_0SyzZKsJkqAaynhMh9x3BtOFG0VCRcV_ApaEs6KjbULAAMH6b9tAlDRwWspvxCCuZf7pS9_6TWNsv2y9_U0Zj8Y9CUXimQ373Wc-AziYS36Ce__XrRzkSNfl-qdDUbmHiLAr1m2TfRnJZiilvJ80wengqY7nnniaVQmouzJ4nxKgTFqgmCoon0hMogt4x4NKNYB9I8Bf6WIzJ5m0PTno7iBy7Vn5EWZ0pm6rqX9kmAV5SVNCyAI6IP7Dm8k0Tc8oXWQKZfPrtX6gO8X40Hyy7K9Si1PwL52grxv0YlTEKgZEi27z83cKw_aqWF27ZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تا ۱۲ ظهر فردا تخفیف جشنواره هم گذاشتن
❤️
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/124316" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124315">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
هم اکنون موج جدید حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/124315" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124313">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یک منبع مسئول در فرودگاه بین‌المللی رفیق حریری بیروت اعلام کرد که پروازها در این فرودگاه جریان دارد و این فرودگاه تعطیل نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/124313" target="_blank">📅 23:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124312">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نخستین پرواز شرکت روسی آئروفلوت از مسکو به مقصد دوبی در امارات متحده عربی امروز دوشنبه پس از سه ماه وقفه انجام شد.
🔴
‌ این شرکت هواپیمایی اعلام کرده است که روزانه یک پرواز از مبدأ مسکو به مقصد دوبی از امروز یکم ژوئن ۲۰۲۶ میلادی (۱۱ خرداد ۱۴۰۵) انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/124312" target="_blank">📅 23:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124311">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
آکسیوس: تصمیم ترامپ برای مهار نتانیاهو سیگنال واضحی بود مبنی بر اینکه او نمی‌خواهد متحد کلیدی‌اش مانع توافق با ایران شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124311" target="_blank">📅 23:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124310">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / بنیامین نتانیاهو : من امروز عصر با رئیس جمهور ترامپ صحبت کردم و به او گفتم که اگر حزب الله حملات خود را به شهرها و شهروندان ما متوقف نکند، اسرائیل به اهدافی در بیروت حمله خواهد کرد.
🔴
موضع ما در این مورد بدون تغییر باقی می ماند.
🔴
در عین حال، ارتش اسرائیل طبق برنامه در جنوب لبنان به عملیات خود ادامه خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124310" target="_blank">📅 23:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124309">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سردار قاآنی: شرارت جدید صهیونیست‌ها باب‌المندب را مثل تنگهٔ هرمز خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/124309" target="_blank">📅 23:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124308">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIBw1jd2g0WKEJLbdNB9_N8oHZlI6hIMOpq7NDWvTJ3u5pVgKWbYwEIoIJAxLtRmmozgwIB-FE84Vpua2B8vv-Hp0SFSTPf7P7pNEWMsKl7y21QLeq3EzC9KGzNZUixqyXWPjuYOYxfHCsMvcluJtl7ixI1smVuUT5Lx6R91xRurPkfyG6-DwZFSJae0AdfwWf6dAkpRSwwnuGKElNy_elJq7EaJegovpLOWgXQyzsSZDlfmvHGve4_R3RePgzEZE9lpdV-yxwiDA2RVyzU520egCH6MXVcbvt6D2S4YfbF1Xo4GZjdPq1qmtFQEJXoeiI5TqhLsCSqWApaz3uqysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز آمار: تورم نقطه به نقطه اردیبهشت ماه در مناطق روستایی به ۱۰۱.۸ درصد رسید
🔴
تورم خوراکی‌ها در مناطق شهری ۱۲۹ و در مناطق روستایی به ۱۳۵ درصد رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124308" target="_blank">📅 22:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124307">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: ترامپ تهدیدهای نتانیاهو مبنی بر بمباران بیروت را عبور از خط قرمزهای قابل قبول دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124307" target="_blank">📅 22:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124306">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام اسرائیلی: حملات برنامه‌ریزی‌شده به بیروت انجام نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124306" target="_blank">📅 22:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124305">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سفارت لبنان در واشنگتن: دولت لبنان در دور کردن لبنان از تشدید تنش‌های بیشتر موفق عمل کرد
🔴
ترامپ به سفیر ما اعلام کرد که نتانیاهو با آتش‌بس موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124305" target="_blank">📅 22:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124304">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
دونالد ترامپ رئیس جمهوری آمریکا برغم عدم مشارکت ناتو در حمله به ایران، بار دیگر از اعضای این پیمان خواست درباره تهران به او کمک کنند.
🔴
ترامپ روز دوشنبه به وقت محلی در گفت و گو با شبکه سی ان بی سی نیوز افزود: متحدان ایالات متحده در ناتو «باید وارد عمل شوند و به ما کمک کنند» زیرا آنها بیش از ایالات متحده به نفتی که از تنگه هرمز عبور می‌کند، متکی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/124304" target="_blank">📅 22:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124303">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
کاتز وزیر دفاع: ترامپ معادله‌ای را که ما تعیین کرده‌ایم پذیرفته است - اینکه شلیک به جوامع ما به معنای بمب‌گذاری در بیروت است. معنای سخنان او همین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/124303" target="_blank">📅 22:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124302">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ارتش اسرائیل: یک افسر با درجه سروانی از تیپ گیواتی در جریان درگیری‌ها در جنوب لبنان کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124302" target="_blank">📅 22:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124301">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
شبکه الشرق‌ سعودی: حزب‌الله پیشنهاد ایالات متحده را پذیرفته و آماده است که از هدف قرار دادن اسرائیل خودداری کند، البته در ازای دریافت تعهد متقابل مبنی بر هدف قرار نگرفتن حومه جنوبی بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124301" target="_blank">📅 22:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124300">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری /  وزیر جنگ اسرائیل: در لبنان آتش‌بس نداریم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124300" target="_blank">📅 22:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124299">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر با عراقچی درباره تلاش‌های میانجیگرانه پاکستان بین واشنگتن و تهران رایزنی کرد
🔴
وزیر خارجه قطر بر حمایت قطر از تلاش‌ها برای دستیابی به توافقی جامع به منظور پایان دادن به بحران در منطقه تأکید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/124299" target="_blank">📅 22:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124298">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری
/
وزیر جنگ اسرائیل: در لبنان آتش‌بس نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124298" target="_blank">📅 22:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124297">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بریتیش ایرویز تمام پروازهای خود به اسراییل را تا اواسط پاییز (۲۴ اکتبر) به دلیل تنش‌های امنیتی لغو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124297" target="_blank">📅 22:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124296">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
لیبرمن وزیر دفاع و خارجه اسبق اسرائیل خطاب به نتانیاهو: این نخست‌وزیر نیست، این یک عروسک است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/124296" target="_blank">📅 22:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124295">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
یائیر لاپید رهبر اپوزیسیون نتانیاهو:
یک کشور تحت الحمایه تمام عیار شده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124295" target="_blank">📅 22:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124294">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نفتالی بنت نخست‌وزیر سابق اسرائیل:
دولت کنترل حاکمیت اسرائیل را از دست داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124294" target="_blank">📅 22:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124293">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بازگشت نفت برنت به ۹۴.۵ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124293" target="_blank">📅 22:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124292">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
حملات اسرائیل به منطقه صور ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124292" target="_blank">📅 22:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124291">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بن‌گویر وزیر اسرائیلی: وقت آن رسیده که به رئیس‌جمهور آمریکا بگوییم نه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124291" target="_blank">📅 22:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124290">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHwfXREb3pLZkelkUoIbpcLy8vmbUQ8oDReo1FTcszT7V43DGHYIZfJY9px6sW-36x8dvEZsAEDW2UBYpVA0YB5QB-pufBBjcthwVISa2j2FOr_PDkIh0zZWXgGlu54bZtTmKSa_KvfCBg5oZmbF-iFjvU6zyEqZgipOqlefcwA1maMp8UVlUMnakbvEcnJszdE8W4KKGQwwFdJXA7b_cp22sLAFPQIhhvrgwUjMZSKGWCcJnWupm7KzTggJyUiqy4Q5F3pdzolA0XINyqPKY-AB8rjdtFioAelpJ-ny_Nb59WiVWPbUYKLlRKRD8qU15JQedn2kjiKDvxTnVlCa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/124290" target="_blank">📅 21:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124289">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
عراقچی در گفت‌وگو با وزیر خارجه پاکستان نگرانی ایران از نقض آتش‌بس توسط اسرائیل در لبنان و حمله احتمالی به بیروت را ابراز کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124289" target="_blank">📅 21:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124288">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رئیس مجلس لبنان: حزب‌الله به آتش‌بس جامع پایبند خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/124288" target="_blank">📅 21:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124287">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری / گزارش ها از حملات جدید اسرائیل به منطقه نبطیه الفوقا در لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/124287" target="_blank">📅 21:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رئیس دفتر پزشکیان وارد قم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/124286" target="_blank">📅 21:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ: هیچ نیرویی به بیروت فرستاده نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/124285" target="_blank">📅 21:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سنتکام می‌گوید نیروهای آمریکایی از آغاز محاصره بنادر ایران در ۱۳ آوریل، ۱۲۱ کشتی تجاری را منحرف کرده و ۵ کشتی را از کار انداخته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/124284" target="_blank">📅 21:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
العالم: حمله بزرگ اسرائیل به بیروت با مداخله امریکا به تعویق افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/124283" target="_blank">📅 21:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
موریا اسراف خبرنگار کانال ۱۳ اسرائیل:
در دفتر نخست‌وزیری اسرائیل سکوت حاکم است.
🔴
این واقعیت که یک رئیس‌جمهور آمریکا، هرچقدر هم که طرفدار اسرائیل باشد، اداره کشور را به دست دارد، باید برای همه ما مایه نگرانی باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/124282" target="_blank">📅 21:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c3f227d6.mp4?token=isBkl4_5CArYpiq2V4njPtxrcWvotvSzClzPJC1GZnzabzvmLkQSsREYhMt_cmJChn1lfi-MGpPRDCMzC9dslvhna6tkJ10qmcfUcCciE67_62ZocWpMnrtflYoEkaMz2xe4etepzv7S-ZGEQIXZaKV6YkXFoO8Scye2oD77dMEnt-ti90hfvqIQrpKdvLFY-BvsPRrDnw7sfw29taihk3WBdlA4XJXRXdvr24PQYNcxE-TrdItmUF39hiVKQow35j4Grn7c01FQ3ru3SafO9XtxjZZ_zzMx10bRG2CQqYu6XD0zqBpGpaTYv5Z6-2fhysWE8f4oTQAt5vR8qIfVgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c3f227d6.mp4?token=isBkl4_5CArYpiq2V4njPtxrcWvotvSzClzPJC1GZnzabzvmLkQSsREYhMt_cmJChn1lfi-MGpPRDCMzC9dslvhna6tkJ10qmcfUcCciE67_62ZocWpMnrtflYoEkaMz2xe4etepzv7S-ZGEQIXZaKV6YkXFoO8Scye2oD77dMEnt-ti90hfvqIQrpKdvLFY-BvsPRrDnw7sfw29taihk3WBdlA4XJXRXdvr24PQYNcxE-TrdItmUF39hiVKQow35j4Grn7c01FQ3ru3SafO9XtxjZZ_zzMx10bRG2CQqYu6XD0zqBpGpaTYv5Z6-2fhysWE8f4oTQAt5vR8qIfVgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام معین بصیری ۲۱ ساله
🔴
18 دی در تهران غرب شهرک اندیشه توسط حرام زاده های عرزشی کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/124281" target="_blank">📅 21:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124280">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رسانه‌ اسرائیلی : اسرائیل بعد از حرف‌های ترامپ گیج شده و از هیچ آتش‌بسی خبر نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124280" target="_blank">📅 21:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124279">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aoj7Uy_d7jRCj22dR3_E0ZE26CfmA7kpdxBIMGkTvCfxDExr2N6VZKtsaWlVeXcKswPt07PjgH0fsTMuNA6vezEBYPY0rLjwWS1EdX2BDJD28kJNc2HM93LhU6Z4K_ELnK4fs1RmVPZ0AhHl3XRkU5UukWhctKt9Ts0Nhvnj9XK4OIUtm3lIGLyjNBlf8617C2sD1OEff1qoTPHsgAR019pzzJAjRWxYCA5LAK1TtcIvw8FS_565Sj2iFr_CWu03qLITYiCm6Q3DEfDm9f5yQU9hizgjzy_jq28Uf90Qa0KYB4lysRFCWVgzRfSZRu7mcfnAbejbJpCrW377W5t4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: مذاکرات با سرعت بالایی با جمهوری اسلامی ایران ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/124279" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124278">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI5-BZvH0v6DUarVVt-XtQ27aYdgQAXDswlObO8vilREKckWA-cz34TrXIYzCSuArmWBTEa_0b2qSip05J488nH4oZFQ8PUxNOojaByEJj8iMLQVtv6xgBRCkaszRmO2qtTZsdXO3axo8XR7-DhZ186LGCyo41h9bC8929bq_PhkUYS9odnKmBWdybI0ZzCRVuOR9URIoKdH74Fc5Qjt8JDOHPKZhEcLHiofHcabhB63Sxr3vmEvZlxhE3rDKYnAScWoeoM4_x4xm_22hZVgCGl7RC9HCXgKwGpuaW1STUpr9Bncr3qg0veVGmWopciCVryySgHVwGlizFPr3RofQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ آتش‌بس ترامپ حدودا ۵ دقیقه دوام داشت زیرا به دلیل شلیک راکت از حزب‌الله، هشدارها در منطقه جلیل به صدا درآمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/124278" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124277">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رویترز: اسرائیل منتظر تایید نهایی ترامپ برای هرگونه عملیات در حومه جنوبی بیروت بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/124277" target="_blank">📅 21:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124276">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رسمی/ترامپ رید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/124276" target="_blank">📅 21:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124275">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QsduDTKqgKzrNmH9_L3WZtO_pWas0eR6zfs3B6-bTG-aIbqkIn2-pJ8RXQy-yO--w6bh_BPyRirAnsQ7upqsU_Ct1DVfTNJNUS5McHJ2fe2dnEduj9TMyelhsO7Xh6DZL1Do_wF34tgtbdnrRlZKfHVNgv4yc8OVOve5f81cn8jr5utE-i9rw5XvRsBUG5fdIJy7wXARRyaDSewX3g65sHleSjbQuA_MH_-vkAFKAezXipppI3kvAeseM7O60E3UmjtCoU8DbXVg9mKV_5oSnN-gfZTGqxo6LbBJ3LSw7Zas2uS7mNmJoNxga_F5NDa69Z3KRNJ6uu_ng5xhJuYqLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من یک تماس بسیار سازنده با نخست‌وزیر بی‌بی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردن که تمام تیراندازی‌ها متوقف بشه؛ اسرائیل به آنها حمله نخواهد کرد و آنها هم به اسرائیل حمله نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/124275" target="_blank">📅 21:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124274">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری/ ترامپ آتش‌بس لبنان را رسما اعلام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/124274" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124273">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp3HcSRKko7QGHfuA8y_JBy31ZrdZLdc8UlGBpLRAMRDoQlwXlvkui2-SWaJN2G5ZbdAIMvwNM7EXG76CSK7xB8SB6357zKPmH0_mYTk3SrWF5-f1gk_DYUj-HR7JKnGwe6VO5FDWycao1sBioVGY8pCivQ3nTaiMSzt-pkdk0_pZzDsJRa9puT1Mb5_3VuIl86hRgQr0qfiygiyZ37-SVUCjfHAcNngGhRKQR8m611KzlsAS-rWh74oJngC4flcbTFRIZ_ffOpoCFMMdwMTtdYNJ979deGhnm5oRycB6Ss-q_yNy6HmDwvMDGcLtTYk2coB3GzaMqw6pkBP7V1Qgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/124273" target="_blank">📅 21:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124272">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کانال ۱۲ عبری: تماس سرنوشت‌ساز بین نتانیاهو و ترامپ در میانه‌ی ابهام درباره اجرای حمله اسرائیل به بیروت.
🔴
نگرانی در اسرائیل از عقب‌نشینی از تهدید حمله به حومه جنوبی بیروت پس از فشارها و تحولات منطقه‌ای.
🔴
واشنگتن تهدیدات ایران را تهدیدی مستقیم علیه منافع آمریکا می‌داند.
🔴
ایران در صورت گسترش حملات علیه لبنان، تهدید به ازسرگیری تشدید نظامی می‌کند.
🔴
نتایج تماس نتانیاهو–ترامپ ممکن است در ساعات آینده مشخص کند که آیا اسرائیل حمله را اجرا خواهد کرد، آن را به تعویق می‌اندازد یا لغو می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124272" target="_blank">📅 21:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124271">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
به نقل از دو منبع اسرائیل: در انتظار تأیید نهایی ترامپ برای هر عملیاتی در حومه‌های جنوبی بیروت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124271" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124270">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رویترز به نقل از منابع اسرائیلی: اسرائیل برای هرگونه عملیات در حومه جنوبی بیروت منتظر تأیید نهایی ترامپ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/124270" target="_blank">📅 20:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124269">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت خارجه آمریکا به تلویزیون العربی:
واشنگتن پیشنهاد داده است که حزب‌الله حملات خود را در مقابل خودداری اسرائیل از تشدید تنش نظامی در بیروت متوقف کند
🔴
پیشنهاد ما با هدف فراهم کردن شرایط برای کاهش تدریجی تنش و توقف خصومت‌ها است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/124269" target="_blank">📅 20:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124268">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: همه منتظر نتایج گفتگوی دراماتیک بین ترامپ و نتانیاهو هستند تا بفهمند اوضاع به کدام سمت خواهد رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/124268" target="_blank">📅 20:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124267">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ به CNBC : قیمت نفت به‌زودی مثل سنگ سقوط می‌کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/124267" target="_blank">📅 20:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124266">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی: برایم مهم نیست که مذاکرات با ایران تمام شده باشد و نگران قیمت نفت هم نیستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/124266" target="_blank">📅 20:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124265">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی: از نتانیاهو خواهم پرسید که در لبنان چه می‌گذرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124265" target="_blank">📅 20:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124264">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پاکستان: ایران خواستار ادامه میانجی‌گری اسلام‌آباد است
🔴
وزارت خارجه پاکستان خبر داد که ایران خواستار ادامه میانجی‌گری پاکستان برای تنش‌زدایی در وضعیت کنونی و حمایت از آتش‌بس شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124264" target="_blank">📅 20:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124263">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری / رسانه اسرائیلی i24news: اسرائیل حمله در ضاحیه را متوقف کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/124263" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124262">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4aJw1tTlw11XbfKkDpm_nbENqe06nrQtEMxu6OxQJ9Qi68BHoE_hBZDjMLG3ql9ubHguty0rEKPnx32ZXW0RFmPypD7pePvgmcOB1DhQWrn0Ba2gAGKhDM_aEuiVk8sqLLRDD0IQ1P-GMZ7kk14UAjSbEmy4eBI1cgAyC9M0r9k_fwPTanneZ0xY3DEVsISu6OqW_rgkFJpKtHZbHiqjHxJQaiOKQWEnjcXcGPojwl4F8zhoV6c2ze2Dam0ef7_nQ5fnznIUfA22KFJuTIJKwcL_IwZyxUw9FqMi-pMA7IP2EvBYdwwh0OSIuFPVmIVRqD2IRC1cFHRF1Cwb5P7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پخش تلویزیونی اسرائیل: نتانیاهو در تلاش است آمریکایی‌ها را متقاعد کند که به حومه جنوبی بیروت حمله کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/124262" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124260">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / رسانه اسرائیلی i24news: اسرائیل حمله در ضاحیه را متوقف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124260" target="_blank">📅 20:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124259">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سازمان ملل : جدی خیلی نگرانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124259" target="_blank">📅 20:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124258">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjEn68fSM1Rl9B-918hEO54LnX_lh0hAQUmgvInt8mxIdo3DvcKRuJdQ1esXmYjRucSw9tPUZVqksaSrj8xU89aK-o3CnKSB6zHfffe7KRGdFaUuswkj-s3j0f-Ol94m0E4WYADNFwLFbJjInJtKnwTjgbaeSupUeyPG2CHjgVA4sZUFANC4SPwGjsM78WpxAK_2JLM83myzs-jV3iSdWyfVNkLAgEUhMFwZhUcp_W6JZeUtFAfWGgEll9LQFF-hFFgZTSMcpXA-waBOf8B1kYPNAlvXmkdGAdxS4GQMcXj90VS0Q0IITy1FrlKNY54szP4dAoUZWcEoGIeXe7WV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه روسیه :  بیشتر نقض آتش‌بس‌ها از سمت
اسرائیله
و هشدار میدیم حملاتش به
حزب‌الله
تنش‌ها رو به مرحله خطرناکی میبره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/124258" target="_blank">📅 20:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124257">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری / گفتگوی تلفنی ترامپ و نتانیاهو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/124257" target="_blank">📅 20:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124256">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
مشاور احمدی نژاد:  نگران نباشید ، حال احمدی‌نژاد خوبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/124256" target="_blank">📅 20:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124255">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: وزیر خارجه پاکستان در تماسی با همتای ایرانی خود، وضعیت جاری منطقه را مورد بحث و تبادل نظر قرار داد.
🔴
عراقچی نگرانی خود را درباره تحولات اخیر، نقض آتش‌بس در لبنان از سوی رژیم اسرائیل و حمله احتمالی به بیروت ابراز کرد.
🔴
وزیر امور خارجه پاکستان به عراقچی تأکید کرد که تضمین تداوم آتش‌بس برای جلوگیری از فروپاشی تفاهم‌های موجود ضروری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/124255" target="_blank">📅 20:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124254">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ارتش اسرائیل :  فرمانده یه واحد تو سامانه موشکی حزب‌الله رو از بین بردیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/124254" target="_blank">📅 19:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124253">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szVJ5X4_eL4rG3o8vKpUk67qlE8BgZ7jSOglBB6REciUkYWfXfyUI3jK4w3CTJdzWl6wG-_A4YjlD9ca4zSZGxqkKp1kh-i31kohhNNUwuhL9TlUd0pCHu4qSpAakFdFwJX25ocwqPsfEQeNy7dKEktFLyJgP6AIKR2DC15-Y3dCBd0KyaFhqKvhurVVtkfvx_BTVLEXre-xe3PoK24kRBX7mp5VSSRyKHFh0gkCCvikqYcNGbcjVmKfqbIrMl_O2bn1MuiZTwWhltUGv9pIPamy1SQssLZVhvBv7SBZCVeFuufFw3QLigYIoBkSnfw0d5mYjzf3tNfwiEc7C8kBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: تحریم‌های ما علیه ایران به محکمی فولاد است و به همین شکل باقی خواهد ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/124253" target="_blank">📅 19:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124252">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ : اگر گزارش‌ها مبنی بر تعلیق مذاکرات ایران با آمریکا درست باشد، «اشکالی ندارد»
🔴
ترامپ گفت: «این به آن معنا نیست که ما برویم و شروع به انداختن بمب کنیم. ما فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/124252" target="_blank">📅 19:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124251">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
دونالد ترامپ به ان‌بی‌سی نیوز درباره مذاکرات با ایران گفت: ما بیش از حد صحبت کرده‌ایم، سکوت کردن خوب خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/124251" target="_blank">📅 19:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124250">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/دونالد ترامپ: من هیچ خبری مبنی بر تعلیق مذاکرات با ایران دریافت نکرده‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/124250" target="_blank">📅 19:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124249">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سازمان هواپیمایی عراق: پروازهای ما به بیروت در حال حاضر به دلیل وضعیت امنیتی و شرایط حاکم بر منطقه متوقف شده است.
🔴
این هشدار در آستانه احتمال حملات اسرائیل به ضاحیه جنوبی صادر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/124249" target="_blank">📅 19:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124248">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مکرون: در گفتگوی دیشب خود با ترامپ درباره وضعیت خاورمیانه، از تلاشهای قاطعانه ایشان برای دستیابی سریع به توافقی بین ایالات متحده و ایران استقبال کردم؛ توافقی که فرصتی منحصربه‌فرد برای ایجاد چارچوب امنیتی جدید با مشارکت تمام بازیگران مرتبط به منظور تثبیت پایدار منطقه به شمار می‌رود.
🔴
بیان داشتم که
ما آماده‌ایم کاملاً از این تلاش‌ها حمایت کرده و سهم خود را در اجرای آنها ایفا کنیم.
این همان هدف مأموریت بین‌المللی است که با همکاری بریتانیا و شرکای خود ساخته‌ایم و به محض حصول توافق، برای کمک به تأمین امنیت ترافیک دریایی در تنگه هرمز قابل استقرار خواهد بود. همچنین
آمادگی داریم تخصص و قابلیت‌های خود را به گفتگوهای گسترده‌تری که باید آغاز شود، به ویژه در بخش هسته‌ای یک توافق، ارائه دهیم.
🔴
در پایان، از تعهد پرزیدنت ترامپ به حاکمیت و تمامیت ارضی لبنان استقبال کرده و
بر اهمیت آتش‌بس قوی و حمایت جمعی ما از مقامات لبنانی تأکید کردم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/124248" target="_blank">📅 19:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124247">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
عراقچی یه تماس تلفنی فوری با میانجی پاکستانی برقرار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/124247" target="_blank">📅 19:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124246">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqL3YQyu07Xht6b2cmM3436akrdJE-9A0Lppj55iyvkRElPqItGUaoOnH3PkTRhExV9Mr3yGOJytHu_fB-zbpp_oNoDff3Q3dC6wHww3Cn6bIB293L7djKl7Y27FqMuAh_ZNEiIsCjVv4lw-TYnVmADVte2qg5TwVFYXQEotW9LFx2TJ0GrSRfO5WBSO3PvVF3O9mieKc3Bl2cSK3Nc9KUJAjoWIiUXoNzIS2U3sBEAyVvVmLc1ivj1pNwhY63ikeLy2aDI22hCO55SPJjIequLVugiDHQXi7ynEh26qps1oJ_fvoCcZw1v00KRuHyB-iJDNbLO7TDcLr4zVTgeBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل :  فرمانده یه واحد تو سامانه موشکی حزب‌الله رو از بین بردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/124246" target="_blank">📅 19:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124245">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری /صدا و سیما: بسیار محتمل است که آتش‌بس بین ایران و آمریکا در صورت ادامه حملات در لبنان به پایان برسد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/124245" target="_blank">📅 19:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124244">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اکسیوس : حزب‌الله به دولت ترامپ گفته که آماده‌ست همین الان با اسرائیل یه آتش‌بس کامل و فوری داشته باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/124244" target="_blank">📅 19:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124243">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nM3JrYW0nfKNFIN6qVWUh6F2qxvXZ_2Mx_BSC8OTuX9y1mxSTb-FlarQIZ_zS2fz5zvzK2Wu1ZPPe4r6XkEj0DQOcdkd0wEd9Tigpu2NZrXpJqd19sxKYJhkg2Q7DJe8AJHEJUbk08IHjeIOIEP3QWQwsn65BKeirZerZ4SKtf2fs_VVIJo05wydNB4A3ZJHkXQ7xdiXelMDRObiyJ2sVL5ZDTwasSjVg4pWFPHNHFLVFmXo0sYty3kGVsAq3tVirN1vB845lD1gn_5zgL6nBwvhr0PTADHhUGaGAcGMDuhxcQHOfK1ja88SX55BlqizyTtgmX9uFzIocxrMLkpiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی
:
تنگه هرمز تحت مدیریت ایران است. اجازه تداوم محاصره دریایی را نخواهیم داد و تشدید تنش در لبنان هم تحمل نخواهد شد. صبر نیروهای مسلح جمهوری اسلامی ایران حدی دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/124243" target="_blank">📅 19:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124242">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان اسرائیل
🔴
سرلشکر خلبان علی عبداللهی: نتانیاهو در ادامه شرارت های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔴
با توجه به نقض مکرر آتش بس توسط رژیم، در…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/124242" target="_blank">📅 19:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124241">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogfwvVLnvILj6lBI-8I__uFYrIY1LyUn7YXP5pqcly0a46LwtO5yIAO48MeD2lU8cc2yPaOO9b7BVaUVEntGK8huCsjBdkWLHmfW8Sa2wJj3nl6-uCFhXHpvKY_fBHUYaqLAIzXlJjizUAMaMOuJlfZDm1qPlYsN_FTeNzwdE0eNqZ0jV2M80nPQAEeLKC8LuOqFWLrlvgiFnA788e_PRCJQGg3bm1Ttwp1c39aUCmuxZ4YYLnhIEK7qGVOvnsr2NxnN23zPBfBfhIeEKvq1gT2O5dXU70N5rvRPb4pl906OVa5ldGc62LP6f_vMkWugiJ3M4-WP13OUCJi8OrpH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حساب سازمان اطلاعات سپاه: هرکه باد بکارد،طوفان درو می‌کند
🔴
ایران عبور از خط قرمزها در لبنان و غزه را به معنای جنگ مستقیم و تحمیل هزینه بر امنیت ملی خود ومقاومت اسلامی فرض کرده و متقابلا عزم خود را برای عملیات دفاعی با انجام اقدامات معناشکن و گشودن جبهه های جدید به علاوه حفظ معادله تنگه هرمز قرار می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/124241" target="_blank">📅 19:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2FsS0PC_am1gDcCuHevgal6L8H0qNh36dmBhXhqHj_MUFZAyG4PJQdnQlBnVO7nH5kxQ5di6UYtoBL7uPdwS6TdAvbe1Ty4UiUjukncdzuN2_nMYngBLnKPkjAQMvr_KEFLxb_Z0ruH2wTbLR5UAyBcE-bWCmzsleWuU2gg-lCfoviK8slp5Z7jO7rIULXzoEgERAHyl1aqiHFnZqU1s0DEclIZyQQ_B-vN5JfZb-0Hb1JQGuTiDzK1Lc9p25opLI5wJ5AdBS7KZ-mhIQ-VfvjgRAoKz0-sF0dmQBQ8hMxGWXt9XcJfsJufNRAPdP2dqiDzQFg7bWwga7Lhoe63LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZJpddt_RARqZ961NBwte8m9gyNORoskN_HglGuS-ydSolP87KVzu0IvOxE58EqbmxiHnngAFNfAYY7vwFBlj0lFHeMNZ70mAqKKpEA1-g6_uVG7Sly8Sym8TuNIEqY4XqmtmVmnngrcPUwhtAeqPC6BJN0jLpewAt3yQZrlAsGNRsXoTuBEJyIO4ILICtqZmi0sSLz0FlTV480B1g6O4bPmhmR6koFMLUJcwlo4FPG97do6mvZwxxbgrhgH8HPaDoiXeEklrja3DgEdpnBzpyzpd3RAwoqGxIs0joHEgKPO8agJdiunRspPdiwUwBiQvQgApvdUZlQGxurRvGrqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrMhmouiV2_C4DN4yCkijT32l7t1R_9uTPJ73lIjJqT4o-1qMStwTkBoCJKxPymp_bRei3E-mpgOmoYCQlykiCJLtUYwOPQgcJMkbzO1A_ZfHBuZ1iJjOgPPSOl9W17rD4ehKxErtWSj7dZPNATtu3OYlP1ZQBvWVnq210ot2rinqIU5q09HWhgZLeUMMN1YOp9FhpnxGzHZ2vVF94elMlTjppSxo_P0Cmo67I_xYgiRkG4d9224x8n35hRyRTjm-L7pBWjMlOItjQaeBhxZCu5UFiEbPzmKy7dezAM_iw0-WJh0xnDHvEhmkBkvMpc82muyhkue_rExMHC8RrHUjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صحنه‌های ای دیگر از حمله‌ی سهمگین اسرائیل به صور، جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124238" target="_blank">📅 19:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان اسرائیل
🔴
سرلشکر خلبان علی عبداللهی: نتانیاهو در ادامه شرارت های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔴
با توجه به نقض مکرر آتش بس توسط رژیم، در صورت عملی شدن این تهدید به ساکنان بخش های شمالی و شهرک های نظامی در سرزمین های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124237" target="_blank">📅 19:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhNzcww8VbScBjySyq9zFPGwciHJntRiA3uEAK2U6yuhTf7l1BgNaYYnzk9NyRQvzY2h1Tzf0vaqdxSNai-1SC5tTXSstiEohDStRdudZbVS66gw9oyWQd1vs4BZ9M5IMk9PniaeXy_KSkD7HsfQ4QHmZ7MXHMIAw3P3qvb8tIdQPevFaCoX-w9JJLvPr_TACbieEOPqkzg_qyr3bNnGiLOJkDSYexseqnOmEpGmuBLvyq2dU1NwgFX-FpwNAK_OsiCW349gKHMbuMgKZJZnqC_IY4AXfBEGklgRLoX0pk76GIZQ5AZ_80yg4idSIBPQp_2dXnzSZnFYRdRJYfagfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/124236" target="_blank">📅 19:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6269863c82.mp4?token=iYp5XBWzKk-AagXB4N6zLOEULhjmFwLGsrknTg-mudsn3kFyVn8QljkevksUhn0hej3JAtA0Vf3ttWsyjr1KBMHSimav04zfbXF40S11uBemQh2bxMuA9JuwprSlQjla0zrTuNsQVHnD4qyOjYNHHsfe3eEDEa5gzsC7JLX05Oj1I-NLIenRdO1sJ43YJiWPql7nYFmXDfQYxVkJ53QPMFOlw2KucNEaowniHsxaKlCZwzb45PL3CHsndgQk0aCjgyDTy0il5M8k8-t_xIkrAXMQunmbR-NnJfFA0w1O-MFpxTSiVCGacMhog1Vok0gA4YIMjT8lH5pnNg47ibL3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6269863c82.mp4?token=iYp5XBWzKk-AagXB4N6zLOEULhjmFwLGsrknTg-mudsn3kFyVn8QljkevksUhn0hej3JAtA0Vf3ttWsyjr1KBMHSimav04zfbXF40S11uBemQh2bxMuA9JuwprSlQjla0zrTuNsQVHnD4qyOjYNHHsfe3eEDEa5gzsC7JLX05Oj1I-NLIenRdO1sJ43YJiWPql7nYFmXDfQYxVkJ53QPMFOlw2KucNEaowniHsxaKlCZwzb45PL3CHsndgQk0aCjgyDTy0il5M8k8-t_xIkrAXMQunmbR-NnJfFA0w1O-MFpxTSiVCGacMhog1Vok0gA4YIMjT8lH5pnNg47ibL3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله هوایی سهمگین اسرائیلی چند لحظه پیش در صور، جنوب لبنان، انجام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124235" target="_blank">📅 18:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZdiaHEbzoaHqT5Whr_BdjYRpHFccHEBQkVq9eM1s_PmZYF8w05Czxpx0I0bOqREaYU-koX4JcULEry9XiT2hGTaWihZ2NH4682NK-OOsttFv-4prsjjx46GFhyxFvb5JxlJK5P-DIIv1jj7Zg9jvSQ67cHujv6mxX6kDh6K4KKa0MwAiRfxlSdS3JJwldDclczWeT_OUyy2Zr8FzUUtkGeTA5lXyXt-TvS1-NvFmn9oexicKXI6uiTb8mfkncKc9csQrHGNcz9LximpU_kCjhXIT75w4J23FAxlADtB2hJaDrSBFzC7UAkOaNmuvhKEb-uzWWVR_5wEOkVKqoLsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حملات در روز های میانی جنگ به پایگاه چهارم شکاری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124234" target="_blank">📅 18:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای امور خارجه ایران و فرانسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124233" target="_blank">📅 18:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی در بیانیه‌ای اعلام کرد که شورای حکام این آژانس به درخواست مصر، اردن، مراکش و عربستان سعودی در پی حمله به نیروگاه هسته‌ای براکه در امارات متحده عربی، در تاریخ ۵ ژوئن جلسه فوری و اضطراری برگزار خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124232" target="_blank">📅 18:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWxByMJbzStwxcfzbL7VNDV2xDwq33ZZq3QnPPvbo0UbYFpor3qtbG95eknSaChOc4h5bUQ67a-LQ6J0dqGwnssCaitR-rhyb0UlXWGBhijnPiFFo5jGZD4JgjIOsV5e8Dbl4F8Ykm8qWC_-rGE-efGmA5-CPgrVA8mi-dKK725NSEUJkh3t13aSzOykNYTeejXE8BCl7hwhad8CnOvgmdSoPCgqQ-AXreDd1znamf6o--dMi05CUs8kVRxZKsRt2me40VN_l9ekejT6r-fNkxU5EWeAONOvu26Yaoffq2-En_hDv9b0ANfx7rxHwccLGkS8CoUKfu-b7RlSYF34LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایزدخواه، نماینده مجلس: راه قدس از ابوظبی می‌گذرد به امارات حمله زمینی کنیم
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124231" target="_blank">📅 18:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzmk1v2QP_O9rRa596kiR2P8QvWQelPCkHUDT1XbgBPmqn7JHa8RTSg9xBKxatiK2dYTLI7sNVXIN7ZbA4W2weC3cuyMlRZPXm3nS4wKOj_MMV5g_6xE7wFoAntCfFEjHdOCG2G5A8HGijH3E_Fb4jDKGMGTDoKonR855vjBP7N2NY8PWOQsuU8pyc-w9JOwAdj5Sx8nvthJRpj3ZjnKDsq0h1bNSyZHI2HNH_FraxMl_b05XodtjMiUIiUCOlJPhHhtVrxvaXNaBVDZJLX3IXYol9sKg7h9XUznt_YRafcRFhVlqmjbIGcraj1UZbproWNDqbR_lo3SEE-4_DRcvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در بنگاه شرط‌بندی مشهور آمریکا (Kalshi)، شانس بازگشت ترافیک دریایی تنگه هرمز به وضعیت نرمال تا 1 آگوست (11 مرداد)، به کمتر از 40% رسیده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124230" target="_blank">📅 18:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEROR0_RoTkcwRzD4rz5dUljanzLlAvJQgt1IVM-REH2o2Anl0gU5ZMVKutV3at8doXd_QcVPQfL7lAf668ul0nSSb5RfE_YixaajKjwv38ui0Jt8Y3pKUBeOEp2zEbbf1j3zkTpddotN0w6irKR1yepkOoEOtiacOVPoJlBuLrT0wE4CEoiI6ZW-Kiht4FsBMoCSoDFAJV8ypuPGt9Gp-J--LMQ-gWne6nQXsY1rNn96a7jhuGXLw3-rzwcfvt5OROnzYMl_NEykGDn42TXUSqNXb8-hMg8CcvPfN84Z0GuYYgBDiY5ElpSnG5FROMmcZ4NvXGPvXtuQCK4xNVYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت 97 دلار ، نفت آمریکا 94 دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124229" target="_blank">📅 18:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63c6a5299.mp4?token=oNTwIfnT3XNcSFD8ixkW4FMcLRcfz7ZouJy3alHGrwdaPHzULiEkv85Td3Xb99ON4XpwYy-ATEbcv8Y1zzF9nxG60vKanFISA2g2_mkkWHuLhb17BK9-o6tx6X-qe6a1HTytJNuWNm3MSJe-TGJlI-vsUEKIxtSgpjnnhpBUk74gEgdCDhOOCIyTrZmvNLXZNlxtU7bxV6ZahDyqAwZjNuiyP9i_WtQ8CrLWVr11Eil4imJRinuFxwwUxMSzIV_5V_X_jk1uaMRGOtNPnrRHJXVtOooMisXzfGzXqekBY6Vq1krK4IXcXiMCz_oFMYB3AkDviAonlPBZclA1qGptbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63c6a5299.mp4?token=oNTwIfnT3XNcSFD8ixkW4FMcLRcfz7ZouJy3alHGrwdaPHzULiEkv85Td3Xb99ON4XpwYy-ATEbcv8Y1zzF9nxG60vKanFISA2g2_mkkWHuLhb17BK9-o6tx6X-qe6a1HTytJNuWNm3MSJe-TGJlI-vsUEKIxtSgpjnnhpBUk74gEgdCDhOOCIyTrZmvNLXZNlxtU7bxV6ZahDyqAwZjNuiyP9i_WtQ8CrLWVr11Eil4imJRinuFxwwUxMSzIV_5V_X_jk1uaMRGOtNPnrRHJXVtOooMisXzfGzXqekBY6Vq1krK4IXcXiMCz_oFMYB3AkDviAonlPBZclA1qGptbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل، بزالل سموتریچ در نیویورک: دولت اسرائیل خانه تمام مردم یهود است.
🔴
امنیت یهودیان در اینجا نیز به قدرت و امنیت دولت اسرائیل بستگی دارد. اما بدون شک، هیچ جای بهتری برای زندگی وجود ندارد.
🔴
یادآوری می‌کنم که ما اکنون به مهاجران جدیدی که امسال به اسرائیل می‌آیند، پنج سال معافیت کامل مالیاتی می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124228" target="_blank">📅 18:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204ea63704.mp4?token=iVG8I4_oNlX5_eaSBA0ZQsVfBcF1OeB7GtLIgRrYNzf87sNr1aDfDhbN5UMGijtCQJK5L5MjwFZ9Mjb5gYDTFFsc1ZfTfs69BKYZn-6aCE3YswTCA5QpFzOOGpkby6eGZKfYBW9J7ck9T7SnP6xbX8U21y1zLLlZ6qEsZFGaW7gmqY_RFcOcDgOXzN2tvuPyB7NvszQA1f6gc-QcYVwupqN2Ndddr3PzdyrPKc2bZRIB8HWok4BGlKMOnBv6FxK0Vjsmn66bDIQXR6PnQx33romluELTQOEW2MKyZoTSKYxLg43c6JLy59dCFXOtFCC2FKXR8NbuywYUupSJZ8zWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204ea63704.mp4?token=iVG8I4_oNlX5_eaSBA0ZQsVfBcF1OeB7GtLIgRrYNzf87sNr1aDfDhbN5UMGijtCQJK5L5MjwFZ9Mjb5gYDTFFsc1ZfTfs69BKYZn-6aCE3YswTCA5QpFzOOGpkby6eGZKfYBW9J7ck9T7SnP6xbX8U21y1zLLlZ6qEsZFGaW7gmqY_RFcOcDgOXzN2tvuPyB7NvszQA1f6gc-QcYVwupqN2Ndddr3PzdyrPKc2bZRIB8HWok4BGlKMOnBv6FxK0Vjsmn66bDIQXR6PnQx33romluELTQOEW2MKyZoTSKYxLg43c6JLy59dCFXOtFCC2FKXR8NbuywYUupSJZ8zWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل بزالل سموتریچ در نیویورک: مردم ما پیش از این بسیاری از مامدانی‌ها را پشت سر گذاشته‌اند و اکنون نیز از پس آن‌ها برخواهند آمد.
🔴
در نهایت، انتخاب مامدانی، مانند هر کس دیگری، این است که در کدام سوی تاریخ می‌خواهد باشد.
🔴
اما تاریخ یک سوی درست و یک سوی نادرست دارد و این موضوع در طول سال‌ها آشکار بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124227" target="_blank">📅 18:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b099e3a6a7.mp4?token=hGTiMrYVYhFx--pBPEytVn1V74wMNyIdEMcUJMLRA2IBNdnCo9kYdMufM5rLDp-ca9OKQXaIXAgP0iX8jNz5Gmon0W0JMTf5h30WKoVSaPMEs54Vj1Q4tLh57fcdQ_FrgXEuobArCST367Bw-tbykFfDSDrzqvCsGDxl_9YkeZS2G1GuHWjPyvKZuUhU4JCdqfUAeKfNi-h6cSzA44f6vwOU6LBgCgR2so1ARaBuXHfQZz99KUBYugZNXRuv_2r72riqnV_5dcD9zTXsPJqS3KS8v3C-UZPrSMyS_pTf20uCSxJMvgJceLLu55HULbf-BJ-uLIb4Q4bQ4fhIw9NXmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b099e3a6a7.mp4?token=hGTiMrYVYhFx--pBPEytVn1V74wMNyIdEMcUJMLRA2IBNdnCo9kYdMufM5rLDp-ca9OKQXaIXAgP0iX8jNz5Gmon0W0JMTf5h30WKoVSaPMEs54Vj1Q4tLh57fcdQ_FrgXEuobArCST367Bw-tbykFfDSDrzqvCsGDxl_9YkeZS2G1GuHWjPyvKZuUhU4JCdqfUAeKfNi-h6cSzA44f6vwOU6LBgCgR2so1ARaBuXHfQZz99KUBYugZNXRuv_2r72riqnV_5dcD9zTXsPJqS3KS8v3C-UZPrSMyS_pTf20uCSxJMvgJceLLu55HULbf-BJ-uLIb4Q4bQ4fhIw9NXmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ملخ‌ها به مشهد حمله کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124226" target="_blank">📅 18:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRS6CxW3nEpBK4KxBejW-i-lj9kjlE17HwFRsWkn5ZZqErMLuxbiDSja_gkHGmhijjYP945oLvmLgXWuuSVvVIjTPv8fVIVzfEpDNSUurJVAObVThLI7SvpQjnUExQCItEt0uAFGkOBk2yemkFH-nZkWjXXvn_0Td3eM3v8UM-mk43c3KUcbtYl_fe3wI_CwmMk9n1TPwAZDIHzpIJzmtERKJ04pRuOPjzuPwVLROtjl3DpqEtvyLKAXO724o2GiQlKqxkgJxwPe3kTarIXYhy5mx0zgRGLJQBnK25Ykw7L-eFgJCAj8Xe2DhE-7kqqzWEjg8u-CsUgnFDLyrZelsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دفاع بریتانیا می‌گوید یک پرسنل ارتش بریتانیا دیروز در یک حادثه آموزشی در شمال عراق کشته شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124225" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزارت کشور کویت: به ساکنان خود هشدار می‌دهیم که در انتظار حمله قریب‌الوقوع ایران در مکان‌های امن بمانند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124224" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKFO4-xeWI5KKOS7AkCkRd69FEaofB115xu3Bun6Q08aWNlipRT69bY1M3oJHffDwkX6rnHNY6rZQ_VtZaJnZIhTtjhF64Tu2wkDnpAS2-qEm9fS5sCznf2kxy49mgx2cO5REEH6iYO-TKbO5NYcfEh0la2-1uqh3moNe-Slhs0HTGWul1okHBkQMrNyQzf7UCXkVnbaWTq0ERq-7SPVItDZITyhO5DRfYbqXff-8pNwVXwBcVWsNtqqU-_Sn_wcljNw77yRDdbWJ0Lzl1TM8lEbcWCyG6r1VfUL2wryb-5lfXOWqImYWKlz2f1yYtZPDjoCdD_xwzwDhU4GAc79Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش می‌دهد که یک کشتی باری که در خلیج فارس در حال عبور بوده، در ۴۰ مایل دریایی جنوب شرقی ام قصر عراق مورد حمله قرار گرفته است.
🔴
«یک انفجار بزرگ» پس از اصابت یک پرتابه ناشناخته به سمت راست کشتی رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/124223" target="_blank">📅 18:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بقایی: آتش بس در لبنان بخش لاینفک هرگونه توافق و خاتمه جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124222" target="_blank">📅 17:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اتحادیه اروپا از اسرائیل می‌خواهد «تشدید نظامی در لبنان را متوقف کند»
🔴
اتحادیه اروپا به کشورهایی پیوسته است که از اسرائیل خواسته‌اند حملات گسترده‌اش در لبنان را متوقف کند، پس از آنکه نتانیاهو گفت دستور حملات بیشتری را در حومه جنوبی بیروت صادر کرده است.
🔴
سخنگوی اتحادیه اروپا، انور العانونی، گفت: «ما از اسرائیل می‌خواهیم تشدید نظامی در لبنان را متوقف کند و به حاکمیت و تمامیت ارضی لبنان احترام بگذارد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/124221" target="_blank">📅 17:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
قطر و سوئیس در مورد حمایت از میانجیگری پاکستان رایزنی کردند
🔴
وزارت امور خارجه قطر اعلام کرد که شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر امور خارجه، تماسی تلفنی از ایگناسیو کاسیس، وزیر خارجه سوئیس دریافت کرد و در مورد میانجیگری پاکستان بین ایالات متحده و ایران رایزنی کردند.
🔴
به گفته وزارت خارجه قطر، این تماس به هماهنگی تلاش‌ها در حمایت از میانجیگری اختصاص داشت که به تقویت امنیت و ثبات در منطقه کمک می‌کند.
🔴
وزیر خارجه قطر در این تماس بر ضرورت همکاری همه طرف‌ها با تلاش‌های میانجیگری جاری تأکید کرد که زمینه را برای رسیدگی به ریشه‌های بحران از طریق گفتگو و روش‌های مسالمت‌آمیز باز کرده و منجر به توافقی پایدار می‌شود که از تجدید تنش جلوگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124220" target="_blank">📅 17:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ارتش اسرائیل(IDF): گزارش اولیه - صدای آژیر در مناطق مارجالیوت و کريات شمونا شنیده شد. جزئیات در حال بررسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124219" target="_blank">📅 17:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ارتش اسرائیل(IDF) هشدارهای تخلیه برای حومه‌های جنوبی بیروت (دیهیه) صادر کرده‌اند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124218" target="_blank">📅 17:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سرگئی ریابکوف، معاون وزیر خارجه روسیه: روسیه در حال مذاکره با ایالات متحده در مورد مسائل مربوط به کوبا است.
🔴
امیدواریم که توافق احتمالی بین ایالات متحده و ایران قابل اجرا و کارآمد باشد.
🔴
روسیه آمادگی کامل خود را برای ارائه کمک‌های عملی به توافق‌های احتمالی بین آمریکا و ایران حفظ کرده است.
🔴
آمریکا و ایران باید از تشدید اوضاع و ورود مجدد به چرخه رویارویی نظامی جلوگیری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/124217" target="_blank">📅 17:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
افزایش شدید نفت برنت ادامه دارد: عبور از ۹۷ دلار!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124216" target="_blank">📅 17:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
تجمع فعلی هواپیماهای آمریکایی در فرودگاه بن گوریون در تل‌آویو، اسرائیل.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124215" target="_blank">📅 17:40 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
