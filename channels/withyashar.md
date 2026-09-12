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
<img src="https://cdn4.telesco.pe/file/mYhvndZIRou9U9_SrxHm39Ybrt-4F4qlMqkZcL7_qnn8Ze9tDslEbtAXGNgQuFc_FU8ciKzPPS2l68bm5j9CMyEeVbhahd-jxLwnWCHl6L_xyaARfHsjoI5QVO14C7ioigMjdR4SUQKe0N82gITNYxExegX_3kz26v7g2hkd_6EdPOHM34L3L4JwT3670OL54bVL3y_WYISbDLw3zSicc4xIA_LmExgtVxRFkpqFNWyPbJUW9LF-_CWZaeOYjSPLy7oWiR5E5zbJ_IZslQfl7RygbgwBVu3x33lfsZYtRU5edCVot6ZSBX3HurLTMDdA3ba7PWRV1M1qtbUyx7wlGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 09:32:03</div>
<hr>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">العربیه : نخست وزیر عراق پس از حمله شبه‌نظامیان هوادار ایران به عربستان سعودی، گذرگاه‌های مرزی شلمچه، شیب و مندلی را با ایران بستند. احتمال می‌رود تسلیحاتی که برای هدف قرار دادن عربستان به کار رفته‌اند، از طریق یکی از این گذرگاه‌ها از ایران به عراق منتقل شده باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/22912" target="_blank">📅 03:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فاکس نیوز از عرشه ناو هواپیمابر:  «یو‌اس‌اس جرج واشینگتن» روز جمعه ۱۱ سپتامبر در جریان استقرارش برای نبرد با جمهوری اسلامی آماده می‌شود.
این ناو هواپیمابر که حدود ۵۰۰۰ ملوان را در خود جای داده و توسط ناوشکن‌ها اسکورت می‌شود، آخر هفته گذشته هدف حمله موشک‌های بالستیک ایران قرار گرفت؛ این در حالی است که در طول هفته جاری نیز چندین مورد تبادل آتش میان طرفین رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/22911" target="_blank">📅 02:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رویترز: نفت در پایان هفته بالای ۱۰۰ دلار ماند.
برنت در پایان معاملات جمعه روی
۱۰۴٫۶۱ دلار
بسته شد و نفت آمریکا به
۱۰۰٫۰۵ دلار
رسید؛ نفت برای این هفته بیش از
۸ درصد
رشد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/22910" target="_blank">📅 01:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22909">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">به مناسبت بیست و پنجمین سالگرد حملات ۱۱ سپتامبر، سازمان اطلاعات مرکزی آمریکا (سیا) ۶۹ سند اطلاعاتی محرمانه را منتشر کرد؛ اسنادی که در سال‌های منتهی به این حمله تروریستی در اختیار بیل کلینتون و جورج دبلیو بوش، رؤسای جمهور وقت، قرار گرفته بود. در میان این اسناد، هشداری مورخ ۱۰ سپتامبر ۱۹۹۸ به چشم می‌خورد که بیان می‌داشت القاعده «ممکن است هواپیمایی مملو از مواد منفجره را به یکی از شهرهای آمریکا بکوبد.» این اسناد یافته‌های کمیسیون تحقیق سال ۲۰۰۴ را تأیید می‌کنند و نشان می‌دهند که نهادهای اطلاعاتی به‌طور مداوم درباره نیات القاعده هشدار داده بودند. با این حال، مقامات اطلاعاتی اذعان کردند که این هشدارها نتوانسته بود ابعاد کامل فاجعه برنامه‌ریزی‌شده را به‌درستی منعکس کند. جان رتکلیف، رئیس سیا، اظهار داشت: «بیست و پنج سال پیش، حملات ۱۱ سپتامبر ضربه‌ای به ملت ما وارد کرد، اما نتوانست ما را درهم بشکند.»
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22909" target="_blank">📅 01:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22908">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سخنگوی وزارت خارجه:
منشا حمله آمریکا به لامرد، خاک یکی از کشورهای جنوبی حاشیه خلیج فارس بوده است.
عربستان، ژاپن و اردن تبعات رای‌ مثبت خود به قطعنامهٔ ضدایرانی آژانس را خواهند دید و ما آن‌ها را پاسخگو خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22908" target="_blank">📅 00:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سنتکام : در اعمال محاصره ایالات متحده علیه ایران تا امروز ، نیروهای آمریکایی
مسیر ۹۹ کشتی تجاری را تغییر داده‌اند(۳ کشتی جدید فقط امروز)
تا از رعایت کامل مقررات اطمینان حاصل کنند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22907" target="_blank">📅 23:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مقام اسرائیلی در گفتگو با کانال ۱۲  : تسلط حوثی‌ها بر تنگه باب‌المندب به دلیل عرض بسیار کم مسیر کشتیرانی و امکان هدف قرار دادن مستقیم کشتی‌ها با موشک‌های ضدزره بدون نیاز به سامانه‌های پیچیده راداری، تهدیدی خطرناک‌تر از وضعیت کنونی در تنگه هرمز محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22906" target="_blank">📅 23:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ تلفنی ، درباره ایران: اگر نمی‌خواهید کاری را که من انجام می‌دهم انجام دهید،
آن‌ها به سلاح هسته‌ای دست پیدا خواهند کرد.
اگر من یک سال و نیم پیش با بمب‌افکن‌های بی-۲ آن‌ها را به‌شدت بمباران نکرده بودم،
آن‌ها همین حالا سلاح هسته‌ای داشتند و از آن استفاده می‌کردند.
اسرائیل از بین می‌رفت و خاورمیانه نابود می‌شد. شما این را از این واقعیت می‌بینید که ایران آن همه موشک شلیک کرد. مردم، از جمله عربستان سعودی، واقعاً شوکه شده بودند که ایران به‌جای آن موشک‌ها، ممکن بود از یک سلاح هسته‌ای استفاده کند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22905" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">لایو جنگ یمن در گوگل مپ
https://goo.gl/maps/LkwoDWLT38cUL1mVA?withYashar
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22904" target="_blank">📅 23:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-5fPapUsdy-g2lAc4uzQ9oXkoxZML_r8iapVQZPFoH9NXuV09KFkHqUra2HZXXGfa_Is8iCOzAyUPRoh4n9qT-8AoCUOUBQQvCaYrsii9ojF0b985Ptm7mjn29Ob_bCT2lgoSVP-lIdEHUWAAZ8V3quXZAroSEjUh54p3_Oyov48C1jac9aIwSep5Mt1OMZcOnEGMGb4FPerzGPzRVPiovSM6GaZPgsq7kuh1BJsVU7t4vylxVns5Oz23m2SYQgOmUOpUDUhdyaqZJ8qxe9HXxVZjLmsvVOzypuFan1QOlpNCFzYD5iSNbQEMLyaqhPsz30AnNCzY8m68gxDjE3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «سود سهام عدالت
۵۰۰۰ دلاری ترامپ
» که قرار است به همه بزرگسالان در آمریکا پرداخت شود، به‌دلیل اینکه کشور ما در حال جذب
تریلیون‌ها دلار توسعه اقتصادی، سرمایه‌گذاری و موفقیت واقعی
است، از سوی «دموکرات‌ها» مورد انتقاد قرار گرفته؛ آنها امیدوارند این طرح هیچ‌وقت اجرا نشود، اما
اجرا خواهد شد!
برای مثال، دموکرات‌ها می‌گفتند تصویب
«لایحه بزرگ و زیبای بزرگ»
که یکی از بزرگ‌ترین لوایح تاریخ کنگره بود و توسط رئیس‌جمهور امضا شد، غیرممکن است؛ اما تصویب شد. یا
پرداخت ۱۷۷۶ دلاری
که سال گذشته به نیروهای ارتش آمریکا اختصاص دادم؛ تقریباً همه می‌گفتند امکان انجام آن وجود ندارد، اما انجام شد، نیروهای نظامی میهن‌پرست ما پول را دریافت کردند و از آن استقبال کردند.
وقتی من چیزی می‌گویم، منظورم واقعاً همان چیزی است که می‌گویم! سود سهام ۵۰۰۰ دلاری اجرا خواهد شد، زیرا مردم کشور ما شایسته آن هستند.
به جمهوری‌خواهان رأی دهید، آمریکا را دوباره بزرگ کنیم!
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22903" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">روزنامه معاریو: نتانیاهو پیشنهاد حمله نظامی مشترک با کشورهای عربی به انصارالله یمن را داده است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22902" target="_blank">📅 22:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: ما انتخاب دیگری نداریم،
باید سخت با ایران برای پیروزی بجنگیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22901" target="_blank">📅 21:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏رضا نجفی، نماینده جمهوری اسلامی در آژانس بین‌المللی انرژی اتمی، به شبکه سی‌جی‌تی‌ان گفت: آمریکا ممکن است از قطعنامه اخیر شورای حکام به‌عنوان زمینه‌ای برای تشدید درگیری یا اقدام نظامی جدید علیه جمهوری اسلامی استفاده کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22900" target="_blank">📅 21:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏نیروهای مسلح دولت یمن اعلام کردند در جبهه شرقی و منطقه نظامی سوم، با استفاده از توپخانه و تک‌تیراندازان، نیروها، مواضع و انبارهای حوثی‌ها را هدف قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22899" target="_blank">📅 21:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏تانکرترکرز گزارش داد برای نخستین بار در دو ماه گذشته، مجموع صادرات نفت خام عراق، کویت، عربستان سعودی، قطر، امارات متحده عربی و عمان از خط محاصره آمریکا به‌طور میانگین از ۱۰ میلیون بشکه در روز عبور کرده است.
‏بر اساس این گزارش، صادرات نفت خام ایران همچنان صفر است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22898" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏ارسالی : ساواکیهای اخموی جذاب اگه توهماتتون  با ای آی تموم شد یه فکری بحال انداختن رژیم بفرمایید
‏مملکت به معلم و نانوا و تراشکار و مشاغل دیگه هم نیاز داره!!!!!
‏یادتون نره ساواک یه
**
مثل پدر مهران غفوریان هم داشت
‏یادتون نره هسته وزارت اطلاعات رژیم رو همون ساواکیهای خائن به شاه پی ریزی کردن
یاشار جان فروارد نشه
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22897" target="_blank">📅 21:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22896" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وال‌استریت ژورنال: یک گروه مرتبط با ایران از مدل هوش مصنوعی آمریکایی «کلود» برای ردیابی و هدف‌گیری ناوهای جنگی آمریکا استفاده کرد. بر اساس گزارش شرکت آنتروپیک، این گروه با کمک کلود اطلاعات مربوط به ترانسپوندر کشتی‌ها و هواپیماها، تصاویر نظامی و تصاویر ماهواره‌ای تجاری را جمع‌آوری و تحلیل کرده و برای شناسایی موقعیت و نقاط آسیب‌پذیر ناوهای آمریکایی در خاورمیانه به کار گرفته است. آنتروپیک اعلام کرد این عملیات را شناسایی و متوقف کرده و حساب‌های مرتبط را مسدود کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22895" target="_blank">📅 21:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سخنگوی نیروهای دولت یمن: نیروی هوایی، عملیات بمباران منطقه "صندوق مرگ" را که پیش از این اعلام شده بود، آغاز کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22894" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22893" target="_blank">📅 20:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سی‌ان‌ان گزارش داده که در پی مشاهده دود و آثار انفجار در نزدیکی خط لوله راهبردی شرق–غرب عربستان در جنوب‌شرقی مدینه، احتمال می‌رود این خط لوله هدف حمله قرار گرفته باشد. این خط لوله نفت خام را از مناطق نفت‌خیز شرق عربستان به بندر ینبع در ساحل دریای سرخ منتقل می‌کند و با توجه به اختلال در تردد نفتکش‌ها از تنگه هرمز، اهمیت آن برای صادرات نفت عربستان افزایش یافته است. منابعی در گزارش‌ها احتمال نقش
حوثی‌های یمن
در این حمله را مطرح کرده‌اند، اما عربستان تاکنون وقوع حمله به خط لوله را به‌طور رسمی تأیید نکرده است. تصاویر ماهواره‌ای نیز وجود دود در نزدیکی مسیر خط لوله را نشان می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22891" target="_blank">📅 20:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">احساس همدردی مردم ایران بعد از شنیدن خبر حمله تروریستی به برج های تجارت جهانی نیویورک در ۱۱ سپتامبر … که امروز سالروزش است ، خودم هیچوقت اون روز رو یادم نمیره @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22890" target="_blank">📅 20:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">روزنامه عبری معاریو: حزب‌الله تلاش دارد از نبرد علی‌الطاهر، روایتی از قهرمانی شبیه نبرد کربلا بسازد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22889" target="_blank">📅 20:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حتما تا آخر گوش کنید موتورم روشن شد</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22888" target="_blank">📅 19:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22887" target="_blank">📅 19:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSemoyami SMYM</strong></div>
<div class="tg-text">ولی یاشار اگه بهت بگن با یه بمب اتم تو یه شهر کار این نظام تمومه تو حاضری این اتفاق بیفته</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22886" target="_blank">📅 19:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22885">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ستاد کل نیروهای مسلح اوکراین⁠ گزارش داده نیروهای اوکراینی بندر تجاری مخاچ‌قلعه در داغستان را هدف قرار دادند؛ در این حمله در محدوده بندر آتش‌سوزی ثبت شد و میزان خسارت در حال بررسی اعلام شد. این بندر تنها بندر عمیق‌آب و بدون یخ روسیه در دریای خزر و
یکی از مراکز مهم کریدور لجستیکی روسیه و ایران است که بنا بر اعلام اوکراین، در آن مسیر قطعات و پهپادهای شاهد از ایران به روسیه و مهمات، مواد منفجره و قطعات پهپاد در مسیر معکوس جابه‌جا می‌شوند.
همزمان، اوکراین اعلام کرد در حمله به نووروسیسک، سه شناور روسی شامل ناوچه
آدمیرال اسن، کشتی آبی‌خاکی پیوتر مورگونوف و مین‌روب ژلزنیَکوف
آسیب دیده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22885" target="_blank">📅 19:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرانس‌پرس: حوثی‌ها با کمک هوش مصنوعی برای ساخت موشک‌های هدایت‌شونده تلاش کرده‌اند.
شرکت آنتروپیک اعلام کرده یک گروه مستقر در شمال یمن از هوش مصنوعی «کلود» برای طراحی سامانه هدایت، ناوبری و کنترل یک راکت هدایت‌شونده، یک موشک بالستیک چندمرحله‌ای با برد هدف بیش از
۲ هزار کیلومتر
و یک موشک با طرح سرجنگی گلاید هایپرسونیک استفاده کرده است. این شرکت می‌گوید شواهدی از عملیاتی‌شدن این تسلیحات ندارد، اما یک راکت هدایت‌شونده آزمایش شده است. با توجه به محل فعالیت و ارتباط این گروه با حوثی‌ها، احتمال می‌رود این افراد وابسته به حوثی‌ها بوده باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22884" target="_blank">📅 19:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f58f12cf8.mp4?token=WJX_hM64OtLz-YsUrhFqN8NzO9r9v5T2bZkOMCRpM3hFUkkrVYY45Zze661BCNg-l9FRhRFXBfSDHgIO-8cruwOqVdsCMRAOtzjRMzaw1emfvHyLaDh-22Prkaagcem9Ds3lueuDe1h1OqdCNeIx52VELjXx6VR9rYdSmqd6Lv1njkEF1i-V7O4ecYRwF9qnF_UCWo3Fn7pi-K6tvDHOPEY11gyBVxOhe7Hi6NHTrZLGGAn469QXGMAlIERQRwcrAFKchfSf4JJdwNbOsX9rdjaaLlvqT3mBOtxmBrCq0fTscTWxYpQ55l_7RpUlEyPifvI0Ih22HUzyeUhuMfOZwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f58f12cf8.mp4?token=WJX_hM64OtLz-YsUrhFqN8NzO9r9v5T2bZkOMCRpM3hFUkkrVYY45Zze661BCNg-l9FRhRFXBfSDHgIO-8cruwOqVdsCMRAOtzjRMzaw1emfvHyLaDh-22Prkaagcem9Ds3lueuDe1h1OqdCNeIx52VELjXx6VR9rYdSmqd6Lv1njkEF1i-V7O4ecYRwF9qnF_UCWo3Fn7pi-K6tvDHOPEY11gyBVxOhe7Hi6NHTrZLGGAn469QXGMAlIERQRwcrAFKchfSf4JJdwNbOsX9rdjaaLlvqT3mBOtxmBrCq0fTscTWxYpQ55l_7RpUlEyPifvI0Ih22HUzyeUhuMfOZwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما به نیروهای نظامی‌ای که همین الان مشغول خدمت هستن و تلاش می‌کنن مطمئن بشن بزرگ‌ترین حامی تروریسم در جهان، یعنی جمهوری اسلامی ایران، هرگز و تحت هیچ شرایطی به سلاح هسته‌ای دست پیدا نکنه، ادای احترام می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22883" target="_blank">📅 18:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e269d57611.mp4?token=J9PBKSSKu8mQ12uFQKbgR-uKC15IUTUt3r-bk7f0QMioSAtcwlLZvsZKkVYlawfjLm8hSaAzZc-JDZwoQk08O-R-ZbjcQGAWJf9GvL5v6KWIXgfCUDLtu6EKvIpNXELZC577vjoko0jsa2vZ4g9SqL2ucOpoZsAtSYqbwuGSn65-g-FcJm6nZEhHL60GJgV7YtYUAnWQKK4_8-QpcHLIzZ9z87cjL68o5lugt75oarm6qzBWVnVWxakx8T8VVqgUr4G3FUu9-bV4X0dLssBZyMOnauv7wVph8tGWAMaV3dYIW1BjHHvX5xcAV69OXZz272erz47mDrbYI2fOhSm2Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e269d57611.mp4?token=J9PBKSSKu8mQ12uFQKbgR-uKC15IUTUt3r-bk7f0QMioSAtcwlLZvsZKkVYlawfjLm8hSaAzZc-JDZwoQk08O-R-ZbjcQGAWJf9GvL5v6KWIXgfCUDLtu6EKvIpNXELZC577vjoko0jsa2vZ4g9SqL2ucOpoZsAtSYqbwuGSn65-g-FcJm6nZEhHL60GJgV7YtYUAnWQKK4_8-QpcHLIzZ9z87cjL68o5lugt75oarm6qzBWVnVWxakx8T8VVqgUr4G3FUu9-bV4X0dLssBZyMOnauv7wVph8tGWAMaV3dYIW1BjHHvX5xcAV69OXZz272erz47mDrbYI2fOhSm2Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر هگست وزیر جنگ:
تنگه را ما کنترل می‌کنیم و این نبرد را نیز تمام خواهیم کرد!
تاریخ به پایان نرسیده بود؛ هیچ‌وقت هم به پایان نمی‌رسه. مبارزه با شر ادامه داشت و الان هم ادامه داره.
و این مبارزه تا روز قیامت ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22882" target="_blank">📅 18:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cc98c2628.mp4?token=l05APLxxYksROIRy0lgxFcyVpTQn4uiCNcz5V4g6HvEQlagbqvt2CTvm8LTntgupDUzgJGnkZqulHpAnPcYFfh6I7muHrGXsFmpCKuSHCpo23teEZqMCRzzXQ1a1kmqsmZeufRckWY_EoWebCj0yrSCBLV-S1JMn-3bKKSXDYoYcEBazve4JcmQHsH2RYKWZr7Q7ajksxW5bYkxMgwPeakMdhQ2uYGerWyRMPPrMgsFDwRJwzLKWFxYmAHgB8laPp9dMh4it9e4Wh5lPOeC9uiYf7Rex1gzJSpoJP5R5_F4bHS-qGkj65UiDPMAEcqinxcrYy8lqeyYp_gttEPKkTDhR9SK8pgt4fcc0XjkSukHlT7R3xPPKZc3aDfGVxzw3dM9BaARQdYNnyzYguwLjIy4TH1kqzljyd_zKI1BIe0UfMf0FmYpHm4fB4xEfASihO4BTBMtCW2ey46uXaP64u-1Q7vtCkHx2TFjQ1xSFTBvOPlI5bypK2NX3ZGCZkZQxFpQLrT_9g_8C_xhKeSdyzg0PT-5uL4TECt_NczQPxz_LWzonHVcpkWA8Vd-f6m9SFj6CwJYkO0PPxLU5izeSgtr_-iwwbtX3AydYylIA5jjKtGoCRMbkDfbF92Fu7-ilI2p2aETUa1gX8b_QF4MwcJ1VFqXFcJkrT_DCgUQ5agw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cc98c2628.mp4?token=l05APLxxYksROIRy0lgxFcyVpTQn4uiCNcz5V4g6HvEQlagbqvt2CTvm8LTntgupDUzgJGnkZqulHpAnPcYFfh6I7muHrGXsFmpCKuSHCpo23teEZqMCRzzXQ1a1kmqsmZeufRckWY_EoWebCj0yrSCBLV-S1JMn-3bKKSXDYoYcEBazve4JcmQHsH2RYKWZr7Q7ajksxW5bYkxMgwPeakMdhQ2uYGerWyRMPPrMgsFDwRJwzLKWFxYmAHgB8laPp9dMh4it9e4Wh5lPOeC9uiYf7Rex1gzJSpoJP5R5_F4bHS-qGkj65UiDPMAEcqinxcrYy8lqeyYp_gttEPKkTDhR9SK8pgt4fcc0XjkSukHlT7R3xPPKZc3aDfGVxzw3dM9BaARQdYNnyzYguwLjIy4TH1kqzljyd_zKI1BIe0UfMf0FmYpHm4fB4xEfASihO4BTBMtCW2ey46uXaP64u-1Q7vtCkHx2TFjQ1xSFTBvOPlI5bypK2NX3ZGCZkZQxFpQLrT_9g_8C_xhKeSdyzg0PT-5uL4TECt_NczQPxz_LWzonHVcpkWA8Vd-f6m9SFj6CwJYkO0PPxLU5izeSgtr_-iwwbtX3AydYylIA5jjKtGoCRMbkDfbF92Fu7-ilI2p2aETUa1gX8b_QF4MwcJ1VFqXFcJkrT_DCgUQ5agw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احساس همدردی مردم ایران بعد از شنیدن خبر حمله تروریستی به برج های تجارت جهانی نیویورک در ۱۱ سپتامبر … که امروز سالروزش است ، خودم هیچوقت اون روز رو یادم نمیره
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22881" target="_blank">📅 18:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22880">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f47e9c912.mp4?token=fuWIsE92o_dOpVbRGKZWdwcSpJE5s2XJ1QC2LLplzIX5GXOWXPMLahs-WdYLMh7w68jXm9BM1mYp_y8MOMYv-sPH_u3YSPFRFuVs26b6zQcWWZ-t1wmVzNA6X0snsnjNleMeEbu88T0yobOn1X8bdozWvy1fqOKIDVzNsMeYxmQbF-5cnOmpfMTWXzIJkRNuYc8FJdtm7ePrOub3nKJQWv5o9NzUDa6Q31wP7kA0U-7B3vtNHv-0G5nhOq4s_RUYgNh0DvlxXTMkynK1eFrqlQA_unGpqrfLQW64rcrmSJ7LyaqA7XLjCETs2nwuEOCBn9HsDxPRMbSTLuWIsWE91w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f47e9c912.mp4?token=fuWIsE92o_dOpVbRGKZWdwcSpJE5s2XJ1QC2LLplzIX5GXOWXPMLahs-WdYLMh7w68jXm9BM1mYp_y8MOMYv-sPH_u3YSPFRFuVs26b6zQcWWZ-t1wmVzNA6X0snsnjNleMeEbu88T0yobOn1X8bdozWvy1fqOKIDVzNsMeYxmQbF-5cnOmpfMTWXzIJkRNuYc8FJdtm7ePrOub3nKJQWv5o9NzUDa6Q31wP7kA0U-7B3vtNHv-0G5nhOq4s_RUYgNh0DvlxXTMkynK1eFrqlQA_unGpqrfLQW64rcrmSJ7LyaqA7XLjCETs2nwuEOCBn9HsDxPRMbSTLuWIsWE91w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، حملات 11 سپتامبر را با جنگ خود علیه ایران مرتبط دانست: ما هرگز این واقعه را فراموش نخواهیم کرد. به همین دلیل است که امروز می‌جنگیم.
ما هیچ انتخابی نداریم. تنها نتیجه ممکن، پیروزی است
ایران بزرگترین حامی دولتی تروریسم در جهان است و هرگز به سلاح هسته‌ای نخواهد رسید
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22880" target="_blank">📅 18:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52171a753f.mp4?token=ulJUmYqAeZEzXd4yS_4QzFZHkXv-6tzQvXd_EiGZBuefAgb8HwuPDip_hPYgFYkHs6d1SLrfRYS90iPNR34_es02q_iofc5WdWFdlvSZdSiCEYr04SyYEI9UXZSJEHiO8vuddbNpbysJ-uavObF7jgYni2o3qk_vf4fkwOHOT1LXwl2p3I0Os1IafMK7mijPdS08o5h4x2QQ2O57qJ8eTmvqvJIU0YScXHs6kVhCFGezQhuWZL8-9op2DSDMYaxeD3HClug3V-yGhdAVYgwK6eJqUCce3CRqSFXQwa6sOIFvTKwNa_B_go5RC8jMSg964ueRuSC_O07OSE8HRd9D8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52171a753f.mp4?token=ulJUmYqAeZEzXd4yS_4QzFZHkXv-6tzQvXd_EiGZBuefAgb8HwuPDip_hPYgFYkHs6d1SLrfRYS90iPNR34_es02q_iofc5WdWFdlvSZdSiCEYr04SyYEI9UXZSJEHiO8vuddbNpbysJ-uavObF7jgYni2o3qk_vf4fkwOHOT1LXwl2p3I0Os1IafMK7mijPdS08o5h4x2QQ2O57qJ8eTmvqvJIU0YScXHs6kVhCFGezQhuWZL8-9op2DSDMYaxeD3HClug3V-yGhdAVYgwK6eJqUCce3CRqSFXQwa6sOIFvTKwNa_B_go5RC8jMSg964ueRuSC_O07OSE8HRd9D8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود ۳۰ ربات انسان‌نما و چهارپایه در اعتراض به عملکرد وزارت فناوری اطلاعات لهستان در ورشو، در مقابل این وزارتخانه تجمع کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22879" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX4q_l_yTLm79y_AwBgBiVsZjOP0GsEAelF7ttqV1UFMr95ovjNaI1vVF_waR-Mvk2E9VZ-JErbRRhga9FMOqRhuR4cHIchNaPyMfnP8Ta6lZLoyyKGRzGIq1_fUNcTSs0HyUfNJPyfPkCCCWjQzqY5jcX_EADRWE5sYlnhdem_jJqv50skADyj0mBRvns-f-zV1kUvLIHZTtq09rSdlHywz7qM5jHGhbjhFTYwIMomTos_Pwtq9Ga2kagaSwF-lfxUSFiMaa3fh2AE_Q0XGfjwKmrYXeSozBlWm-80HmzHh4PAQZsp4q_3U1jA_UNyb0efCQ1RfTJ6uSIBDx6IT3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراین در شمال‌شرق استان خارکیف طی دو هفته اخیر مجموعه‌ای از ضدحملات را برای جلوگیری از محاصره نیروهایش در شرق ووچانسک آغاز کرده است.
روسیه از اواخر ژوئیه با حمله‌ای دو‌محوره تلاش کرد حدود
۴۳۰ کیلومتر مربع
از مناطق تحت کنترل اوکراین را قطع کند و به سمت مرکز لجستیکی
پریکولوتنه
پیشروی کرد. اگرچه روسیه چند روستا را در این محور تصرف کرد، نیروهای اوکراینی با اعزام نیروهای کمکی توانستند پیشروی روسیه را متوقف و وضعیت را تثبیت کنند. سپس اوکراین با ضدحملات خود چند منطقه و روستا از جمله
آنی‌شچینه و ایواشچینه
را در اوایل سپتامبر بازپس گرفت و اکنون درگیری بر سر
اوستینیوکا
ادامه دارد. روسیه برای متوقف کردن این ضدحملات، از توپخانه، راکت‌اندازهای چندگانه و
ده‌ها بمب هدایت‌شونده KAB
استفاده کرده است. در جنوب نیز روسیه حملات خود را در نزدیکی
خاتنه
از سر گرفته و به سمت زاروبینکا پیشروی کرده است. طبق نقشه مورد استناد گزارش، تغییرات ارضی اخیر حدود
۴۴ کیلومتر مربع به نفع اوکراین
در برابر
۲٫۱۶ کیلومتر مربع به نفع روسیه
بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22878" target="_blank">📅 16:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22877">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پزشکیان: ایران به گروه بریکس پیشنهاد می‌کند که یک صندوق بیمه ۱۰ میلیارد دلاری برای پروژه‌های بزرگ زیرساختی و انرژی تأسیس کند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22877" target="_blank">📅 16:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا درباره ایران:
«ما داریم
آنها را به‌شدت تحت فشار و در تنگنا قرار می‌دهیم
. فقط به آمار نگاه کنید: هر روز به‌طور میانگین حدود
۱۰ میلیون بشکه نفت از بخش جنوبی تنگه هرمز خارج می‌شود
، اما ایرانی‌ها
هیچ نفتی خارج نمی‌کنند
. در یک دوره دو هفته‌ای، نتیجه
۱۴۰ میلیارد در برابر صفر
است. آنها فقط یک مشت
بازنده
هستند که نشسته‌اند و می‌گویند: «بله، این کار را می‌کنیم، آن کار را می‌کنیم.» واقعاً برای من
مسخره و خنده‌دار
هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22876" target="_blank">📅 16:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0273c7f90c.mp4?token=V3jEd-mkapQ2pAyRNsHcErbuOS6oHIKXxB6MsP5oQjGvZ-34MgJFxePc0EnToeBaxgcDRI_ID3aa8xGAFouN8AxZkFzqd8C3N-e6y1NJfbBrKzjM7x99urkp3ObrAYz0H1P0IB7NYfZpNACe7zBunjcH2Si-L_P6IQh_WgnUIoYjyI190r29KRhs7pw3LmVm0iX4WU-Kv_T53DoUa3PLk_HzAvvWYfCibxYakqIuY6DUnw4tOHy6ws-3SmqPMrfNH0wNkboUxJDS2abbHYeAqHOxOKmSI6zX91y7qQ8SxIr2ggnnMQ0-SCQkLJeVuUWjr8QXCIpvVoJ5q496WnYsloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0273c7f90c.mp4?token=V3jEd-mkapQ2pAyRNsHcErbuOS6oHIKXxB6MsP5oQjGvZ-34MgJFxePc0EnToeBaxgcDRI_ID3aa8xGAFouN8AxZkFzqd8C3N-e6y1NJfbBrKzjM7x99urkp3ObrAYz0H1P0IB7NYfZpNACe7zBunjcH2Si-L_P6IQh_WgnUIoYjyI190r29KRhs7pw3LmVm0iX4WU-Kv_T53DoUa3PLk_HzAvvWYfCibxYakqIuY6DUnw4tOHy6ws-3SmqPMrfNH0wNkboUxJDS2abbHYeAqHOxOKmSI6zX91y7qQ8SxIr2ggnnMQ0-SCQkLJeVuUWjr8QXCIpvVoJ5q496WnYsloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا درباره ایران:
«هر چیزی که ایرانی‌ها می‌گویند، بخش عمده آن بر پایه
خیال‌پردازی
است. بسیاری از این ادعاها صرفاً
آرزو و هدف‌گذاری
هستند. وال‌استریت ژورنال گفته ایرانی‌ها در حال بازسازی ذخایر موشکی خود هستند. شاید این‌طور باشد، اما
مقیاس آن چقدر است؟
اندازه و ابعاد این بازسازی کجاست؟ ما
۸۵ درصد کارخانه‌های آنها را منهدم کرده‌ایم
. حالا آیا آنها هر هفته یک کارخانه جدید می‌سازند؟ آیا دو کارخانه می‌سازند؟ می‌دانید، اینها فقط
تیترهای خبری
هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22875" target="_blank">📅 16:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا درباره ایران:
«اگر به حساب‌های ایرانی‌ها در شبکه اجتماعی ایکس نگاه کنید، آنها تلاش می‌کنند در آمریکا
مشکلات اقتصادی ایجاد کنند
؛ چه از طریق
بازده اوراق قرضه
و چه از طریق
قیمت نفت
. و می‌دانید، صرف‌نظر از اینکه استفانی،
بلومبرگ، فایننشال تایمز یا حتی وال‌استریت ژورنال
باشد، آنها آن‌قدر به دلیل
سندرم نفرت و جنون علیه ترامپ
از تعادل خارج شده‌اند که می‌خواهند به ایرانی‌ها
فضایی برای فعالیت و اثرگذاری
بدهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22874" target="_blank">📅 16:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwtH6-F_YLyssfECCQ_vkvPwBVYUECBljswLzN_kNLayFZkXIm-Lvv7r5Xdv9MQ7vu1Vf9wbA19YIoRo88mVFlqKzsioFvLVP8RcAivzV9h2M0Eji-bdVBxCWv_NiCzYjGVF08FgcnRK3o3cMMpi99OZgnFPed179WlcLW39n2mi3uXZREF5NkKYn68thXEEXZgs2qv1ocDwuCflidqUmizWSJpeurX7guYNeiv5kWYtSEeeZrNIwXOnpyDVnmVhl6U5RIKkX4vLoR6bIma78IuXaGwvPkPyJcwAhFgaKtrBO81TSm5MpMYDma1JZA8BTTdKbyI9aTimExZKd4lRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان‌ملل با ۱۶۴ رأی موافق در برابر ۱ رأی مخالف تصویب کرد که نقشه مرکاتور کنار گذاشته شود و از نقشه "Equal Earth" استفاده شود که سایز واقعی کشورها را نشان می دهد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22873" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل: حزب‌الله به دستور ایران، لبنان را ویران می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22872" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">امروز گزارش تورم مصرف‌کننده آمریکا (CPI) برای ماه اوت منتشر می‌شود؛ آماری که می‌تواند بر تصمیم بعدی فدرال رزرو درباره نرخ بهره و بازار کریپتو اثر بگذارد. زمان انتشار: ساعت ۱۶:۰۰ امروز به‌وقت تهران. تورم بالاتر از انتظار معمولاً برای بیت‌کوین و بازار رمزارزها منفی و تورم پایین‌تر از انتظار، مثبت تلقی می‌شود.</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22871" target="_blank">📅 15:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قیمت شورت بله شورت معمولی در ‌ایران به حدود ۱ میلیون تومان رسیده !
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22870" target="_blank">📅 14:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22869">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">داداش یاشار سلام خواستم از وضع مملکت بهت بگم والا مملکت جوری شده که یه شلوار خواستم برا بچم بگیرم پول ندارم ناهار و شام رو تو یه وعده میخوریم اونم نون و پنیر که پنیر هم به زور تونستم بخرم بخدا دیگه نمیتونم شرمنده زن و بچم باشم به خدا دیگه نمیکشم</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22869" target="_blank">📅 14:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22868" target="_blank">📅 14:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22867" target="_blank">📅 14:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2d53e8de.mp4?token=iSSFS8rz0uRvWmJJ3G--UIDZBV0SH33SAzut3O-zJ90y_q28SEpJj4LqjJ4oKPeJaG5EIJZiynEtLZ_az24FZ7P-W4c0c-rHakFx1dTENlmzGiWkoC0F3fATDerf6ynOjBAO7hl6Xc0ld8zWPb6OhMOg3gS1gNNA09PkWewcXsHyyaFxKKSfg5ireFWvvPt23ZoBWKWxM8VAQPxEg6SEKYP9qKGr4nbgeaUOYMVltz57g37BppjRPNd0oqEy7wQ0_B5k21eUweV1yddxOVFMJCMy5a7Mnwa8pokUrLPyGAxs8_qzIlOGLzR37opd2w4Fwpkwvd3Fc5BoX-YVHqLbU2QlCn4GtkSJWIkW769E-2atZCevMsy9818T8cU7C0k7zqBfiug6WkvSV8ROMI9eGUvShAPdYVIt01HvQgBFHSvv52v8_MigsJv6u9SNt6VN7fvBVfKHQ8qA3zVd3QoSvgZTrQSvhWUWftgBBVliTT7o3n3AdPih73Xul3Xw0uy-B-DgblU-vM2FuUpNZzQ15zJ3oxbnHVeK6SQnFFUR8jev4ImFMqmg2omoC4avWuDuymRfxgkb2YlrokWIXMrMODAjpCZg8_pVAUPcXbSYlH_8cBqHNjSZ9ch9lLU_NGlRv62sjZ8tP_bVK9b1dG8X4ddC2P724SzslGlR1MSvwqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2d53e8de.mp4?token=iSSFS8rz0uRvWmJJ3G--UIDZBV0SH33SAzut3O-zJ90y_q28SEpJj4LqjJ4oKPeJaG5EIJZiynEtLZ_az24FZ7P-W4c0c-rHakFx1dTENlmzGiWkoC0F3fATDerf6ynOjBAO7hl6Xc0ld8zWPb6OhMOg3gS1gNNA09PkWewcXsHyyaFxKKSfg5ireFWvvPt23ZoBWKWxM8VAQPxEg6SEKYP9qKGr4nbgeaUOYMVltz57g37BppjRPNd0oqEy7wQ0_B5k21eUweV1yddxOVFMJCMy5a7Mnwa8pokUrLPyGAxs8_qzIlOGLzR37opd2w4Fwpkwvd3Fc5BoX-YVHqLbU2QlCn4GtkSJWIkW769E-2atZCevMsy9818T8cU7C0k7zqBfiug6WkvSV8ROMI9eGUvShAPdYVIt01HvQgBFHSvv52v8_MigsJv6u9SNt6VN7fvBVfKHQ8qA3zVd3QoSvgZTrQSvhWUWftgBBVliTT7o3n3AdPih73Xul3Xw0uy-B-DgblU-vM2FuUpNZzQ15zJ3oxbnHVeK6SQnFFUR8jev4ImFMqmg2omoC4avWuDuymRfxgkb2YlrokWIXMrMODAjpCZg8_pVAUPcXbSYlH_8cBqHNjSZ9ch9lLU_NGlRv62sjZ8tP_bVK9b1dG8X4ddC2P724SzslGlR1MSvwqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی
پ
ِت‌پِتی :
من هانی رامبد رو بزرگ کردم ولی بهم خنجر زد. بهم گفت نباید پشت جمهوری اسلامی باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22866" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تلگراف : اسرائیل تیم بریتانیایی مستقر در کرانه باختری را که خشونت شهرک‌نشینان علیه فلسطینی‌ها را رصد می‌کرد و قرار بود مأموریتش را گسترش دهد، از این منطقه اخراج کرده است. این اقدام در پی تحریم‌های اخیر بریتانیا علیه شهرک‌های اسرائیلی انجام شده است. اسرائیل پیش‌تر نیز در واکنش به این تحریم‌ها، تعطیلی کنسولگری بریتانیا در قدس شرقی، توقف برخی برنامه‌های آموزشی بریتانیا برای نیروهای تشکیلات خودگردان و اخراج نمایندگان بریتانیا از یک مرکز هماهنگی مرتبط با غزه را اعلام کرده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22865" target="_blank">📅 14:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22864">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رویترز:
جهش نفت فقط ناشی از ایران نیست؛ همزمان
حوثی‌ها بندر مخا را تصرف کرده‌اند و به باب‌المندب نزدیک‌تر شده‌اند
. بنابراین دو مسیر حیاتی نفت و تجارت، هرمز و باب‌المندب، همزمان تحت فشار قرار گرفته‌اند. رویترز می‌گوید نفت این هفته بیش از
۷٪
رشد کرده و در مقطعی رشد هفتگی به حدود
۱۳٪
رسیده بود.
اما بعد از انتشار خبر تلاش کشورهای منطقه برای رسیدن به یک توافق موقت درباره عبور کشتی‌ها از تنگه هرمز، بازار برگشت و آخرین رقم
برنت ۱۰۳.۸۸ دلار و WTI حدود ۹۹.۱۵ دلار
بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22864" target="_blank">📅 14:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آکسیوس: دریاسالار برد کوپر، فرمانده فرماندهی مرکزی آمریکا، روز پنجشنبه به عربستان سعودی سفر کرد تا در بحبوحه پیشروی سریع حوثی‌ها در یمن، درباره تشدید وضعیت و گزینه‌های مقابله با این گروه با مقام‌های سعودی گفت‌وگو کند. این سفر همزمان با درخواست محمد بن سلمان از ترامپ برای انجام حملات مستقیم آمریکا علیه حوثی‌ها انجام شد؛ درخواستی که ترامپ فعلاً نپذیرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22863" target="_blank">📅 14:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">علم‌الهدی، امام جمعۀ مشهد به نقل از مجتبی ای آی : ۴ کشته شده در‌ تصادف راننده مست در مشهد با نظر رهبر عنقلاب، شهید شناخته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22862" target="_blank">📅 13:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22860">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رویترز: پاکستان تحت فشار قرار گرفته تا در جنگ عربستان و حوثی‌ها موضع بگیرد.
افزایش حملات حوثی‌ها به عربستان، پاکستان را که هم‌زمان متحد دفاعی ریاض و میانجی میان تهران و ریاض است، در موقعیت دشواری قرار داده است. توافق دفاعی جدید پاکستان، عربستان و ترکیه نیز می‌تواند در صورت گسترش حملات به خاک عربستان اهمیت پیدا کند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22860" target="_blank">📅 13:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آسوشیتدپرس: عربستان فرودگاه المخا را بمباران کرد.
یک روز پس از تصرف المخا توسط حوثی‌ها، جنگنده‌های سعودی فرودگاه تحت کنترل حوثی‌ها در این شهر را هدف قرار دادند. این نخستین اقدام نظامی مستقیم سعودی در منطقه پس از پیشروی گسترده حوثی‌ها در ساحل دریای سرخ است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22859" target="_blank">📅 13:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fae9ec34.mp4?token=KtLDnfXyXlOkd_kD5a36e3PYsPAR7qt7HckMIwqwmh6-6AGzNLjON1WHU7TQrOyxdXJoTXiiudZAc-H588itjrwp_f_tD6mVxxRdN49rCbt3_PnwAwU2AI2k8VqWEzZ0cfg5BHYc68pSfFrKcLBIb1ev4T-0-4MuyaTPAkw4bE4cJIlDAHNjhMhAeRUb9txWGKIheWyolOTnw15fd3DmP0PcJ_eMs3DmsO5UyzP1Xgea7LMxLuUMAQdiCV40Z-kwzYFkn9lRD0pWxhw2SfN52pooxHMkAXi6Gdq6sIVrBRtdHzChKKQqAfyd8HywwxH4nROeAw5jnyVy6p4-P9_GahByQC6LQGy-539stLV-L16toFyOKTkkW7Eef9daaXZNjRXxmadvmgzZKhn7dkvd9zNKs2GAJrxDzTmhHgPcPcFwXW3xwfTjDBQU2Z_3RkHrlU8DH1geiRegffZbggUSdSLs8u12Pzr42wdEuaCqXkLSlj6vFdfJFp2CRxhhVE15-oVPlZAwJye3gdXXQ6gH7fCmq3G7kz-XSNNUHURCfaARjnT9ZlFTlzob28FaP7UCXaDZUzdYsZ63yKTEXbZjW3-ZB31tGckjc5-vEUw73dMl8kyJnEX6Y4jQHsUR6d58xTsBiSEx3mNqH1-RqShjIumrZw0i9i4OUHYm-8v08JM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fae9ec34.mp4?token=KtLDnfXyXlOkd_kD5a36e3PYsPAR7qt7HckMIwqwmh6-6AGzNLjON1WHU7TQrOyxdXJoTXiiudZAc-H588itjrwp_f_tD6mVxxRdN49rCbt3_PnwAwU2AI2k8VqWEzZ0cfg5BHYc68pSfFrKcLBIb1ev4T-0-4MuyaTPAkw4bE4cJIlDAHNjhMhAeRUb9txWGKIheWyolOTnw15fd3DmP0PcJ_eMs3DmsO5UyzP1Xgea7LMxLuUMAQdiCV40Z-kwzYFkn9lRD0pWxhw2SfN52pooxHMkAXi6Gdq6sIVrBRtdHzChKKQqAfyd8HywwxH4nROeAw5jnyVy6p4-P9_GahByQC6LQGy-539stLV-L16toFyOKTkkW7Eef9daaXZNjRXxmadvmgzZKhn7dkvd9zNKs2GAJrxDzTmhHgPcPcFwXW3xwfTjDBQU2Z_3RkHrlU8DH1geiRegffZbggUSdSLs8u12Pzr42wdEuaCqXkLSlj6vFdfJFp2CRxhhVE15-oVPlZAwJye3gdXXQ6gH7fCmq3G7kz-XSNNUHURCfaARjnT9ZlFTlzob28FaP7UCXaDZUzdYsZ63yKTEXbZjW3-ZB31tGckjc5-vEUw73dMl8kyJnEX6Y4jQHsUR6d58xTsBiSEx3mNqH1-RqShjIumrZw0i9i4OUHYm-8v08JM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو چندین تُن سلاح حزب‌الله را که سربازان اسرائیل از رشته‌کوه علی طاهر بازیابی کرده و بیرون کشیدند را بررسی کرد.
پیروزی استراتژیک در مرز شمالی. دهه‌ها زیرساخت‌های تروریستی تحت حمایت ایران به طور کامل توسط ارتش اسرائیل نابود شد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22858" target="_blank">📅 13:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏شبکه ۱۳ اسرائیل به نقل از مقام ارشد آمریکایی : محاصره اقتصادی و دریایی آمریکا می‌تواند ایران را به سمت اجرای یک عملیات نظامی بزرگ پیش از انتخابات میان‌دوره‌ای آمریکا سوق بدهد. جمهوری اسلامی درحال بررسی یک جنگ بزرگ است که فقط به حمله به کشورهای حوزه خلیج فارس محدود نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22857" target="_blank">📅 13:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tp_5-4ar6Wjv-wTrMCUkhEdKQHvEoNmAkf505nJSvNq64qpxbQzD8nj4PUe1mG0dAO8VPPUfHdX0z67PeFRPjAsBZUfxrOi8dN4YYXFcm5ObEEWcFaceqR9ogYfLpgwvRuZQ7eZ5mBCwjt0pRHK4VTSEVTDJktK5mQarm_20ufV74VbHeurnqbRsLrOKhgmsYlWEd5VEw6g75f7iNgTmiWHIF9dqw2yckD_kEueY1m9dvSztzloi8Nf-bVwag3ykmWW2yzg5dKanyR7o8gFq8VtcscV2sAvbIY8__xg5BXET9Hq8OUHbCct3A9LlViJOfUX5i03bW9NNEBrJPxg-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8RX8QS8miQ6-fX-5tpipGjoVaxyeMilBBEuUYHVG9bz4jRot7J2JJayP81c4m5WxNHPbLnBOXIjzTOGYbf89lXZ_Ukb7WDFAizkRTfFcigkZk9erg_moB_Wy3sSgpqthh09sFU6IPYY84uEIle5dZ3B3iZzgTEHVKvSxQDOOZtmwzjPsXzquhNXcTRqTWKcedXLAYM2Kr-CkSggX5_wWkfv2rreG803T7UkM0dxMc8SwmiKKTdkkqt7WMBY-7g4PhUY4G9Jout0ZWU3OAeGpxn9v4KWCIfMpZR9pZRKsGglGv4glKV_tO3Rnn3JHfWYctplYMH_PSk_M3kuJuXeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gwu4XsMIxhQCMc7FKSR9-pjF0nl7bhlLMyCrVW9fisht3PKLIUXDUGuwhSzkBQ6GJHH2-PpVRUceQ86rDMUlAJw30csKTBbAk87m_Z9aoE9o9BChBIMzqpOfgtjQdt40UC323q4QfpkanCaV6KP8Ij8_G7UIRfDVu1kcJ6VcexMq7umF3IMtVJPKqQA61O9F7WjQ7xV7Bme3bv1DtVAS9TtFfIrk4HSKjBlxTn4TVTbB9_2lXrj40PbVk8ls3UvVLHqJ5tX5RM03NIggxP249syWFg4FJWXSZljgvj0DXl3FXU_SGw7yg_AS-yRUKD3vCZWpiP_f_JW1LntShu0o7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش های بسیار از ستون دود در شیراز , دیدبان های اتاق جنگ : دقیقا زاغه شیراز هست که همیشه مورد حمله قرار میگرفت
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22854" target="_blank">📅 12:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">منابع فلسطینی به شبکه الجزیره: محمد الیازوری، فرمانده گردان خان یونس در شاخه نظامی حماس، در یک عملیات ترور اسرائیل کشته شد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22853" target="_blank">📅 12:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22852">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سی‌اان‌ان: آمریکا طی هفته‌های اخیر
حضور اطلاعاتی و مستشاری خود در عربستان را افزایش داده
و بیش از ۱۰۰ مشاور نظامی آمریکایی، که ممکن است شمارشان به حدود
۲۰۰ نفر
برسد، به نیروهای سعودی در عملیات علیه حوثی‌ها کمک می‌کنند. مأموریت این نیروها ارائه
اطلاعات، پشتیبانی هدف‌گیری و ارزیابی لحظه‌ای میدان نبرد
است و نیروهای آمریکایی مستقیماً در حملات مشارکت ندارند. سی‌ان‌ان همچنین گزارش داده
صدها نیروی سپاه پاسداران در یمن حضور دارند
و در کنار حوثی‌ها فعالیت می‌کنند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22852" target="_blank">📅 12:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اقتصاد رو با کارتونهای انیمیشن ۳ دقیقه‌ای به رئیسی یاد میدادند !
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22851" target="_blank">📅 11:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رویترز: قیمت نفت برنت این هفته حدود
۱۳ درصد افزایش یافته
و در مسیر ثبت قوی‌ترین رشد هفتگی از ژوئیه قرار دارد. نگرانی از اختلال طولانی‌مدت در هرمز و پیشروی حوثی‌ها در دریای سرخ، برنت را همچنان بالای ۱۰۰ دلار نگه داشته است.
@WarRoom
فایننشال‌تایمز: نفت برنت به حدود
۱۰۶ دلار
رسیده و ادامه بحران هرمز فشار تورمی شدیدی ایجاد کرده است؛ افزایش قیمت انرژی باعث شده بانک‌های مرکزی از جمله فدرال رزرو آمریکا با فشار بیشتری برای افزایش نرخ بهره مواجه شوند</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22850" target="_blank">📅 11:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رویترز: منابع نظامی اعلام کردند
حوثی‌ها پس از تصرف بندر المخا در امتداد ساحل دریای سرخ پیشروی کرده و به جزایر راهبردی نزدیک باب‌المندب رسیده‌اند.
این تحولات تهدید علیه مسیر صادرات نفت عربستان و کشتیرانی جهانی را افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22849" target="_blank">📅 11:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آسوشیتدپرس: آمریکا توانسته تا حدی
کنترل ایران بر تنگه هرمز را کاهش دهد
و صادرات نفت ایران را تقریباً متوقف کند، اما جنگ همچنان ادامه دارد. جریان نفت از هرمز به حدود دو سوم سطح پیش از جنگ رسیده، در حالی که صادرات نفت ایران از حدود ۱.۸۵ میلیون بشکه در روز به حدود
۲۵۵ هزار بشکه
کاهش یافته است. هم‌زمان حوثی‌ها حملات خود به عربستان را افزایش داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22848" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce588839b.mp4?token=OYFFwXhDdtbRittia2hHmOvZBtQifIgQ-YB1EQkxof45MJ7Fzudu_KX-HOFTfdYf52P-quF43zT1EVIPpRW48QfTqFvBBZW8EiP8dSYqi8zwp5AtFCf3BPDBuhNxZ-Ustn5sKFIyT0-F3EadYBU8wjV_lSIMYg2vEyg-5vSL36GGEzn80_rBMEKrSPmjlniTzMdgmX3B98UpAMLXB-9zvSLrPcpgU5_FmTrSoZDEVsiadFw9YSRCnYQrhTcKVIVhMpQd7XWsuCX2yL6Y7eg6-exet8-OtvaGOFV3noTCK-IzkIacjvHv-wybmVvuIQYMmvWHwOGAS0Qy4QmVcpvdyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce588839b.mp4?token=OYFFwXhDdtbRittia2hHmOvZBtQifIgQ-YB1EQkxof45MJ7Fzudu_KX-HOFTfdYf52P-quF43zT1EVIPpRW48QfTqFvBBZW8EiP8dSYqi8zwp5AtFCf3BPDBuhNxZ-Ustn5sKFIyT0-F3EadYBU8wjV_lSIMYg2vEyg-5vSL36GGEzn80_rBMEKrSPmjlniTzMdgmX3B98UpAMLXB-9zvSLrPcpgU5_FmTrSoZDEVsiadFw9YSRCnYQrhTcKVIVhMpQd7XWsuCX2yL6Y7eg6-exet8-OtvaGOFV3noTCK-IzkIacjvHv-wybmVvuIQYMmvWHwOGAS0Qy4QmVcpvdyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار
:
آیا ممکن است جنگ با ایران تا پایان دوره ریاست‌جمهوری شما ادامه داشته باشد؟
ترامپ
:
نه. حتی یک احتمال هم وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22847" target="_blank">📅 11:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اکسیوس: محمد بن‌سلمان، ولیعهد عربستان، روز پنجشنبه در دو تماس تلفنی از ترامپ خواست
فوراً مواضع حوثی‌ها در یمن را هدف قرار دهد
. این درخواست پس از پیشروی حوثی‌ها و تصرف شهر بندری راهبردی
المخا
مطرح شد. مقام‌های آمریکایی می‌گویند واشنگتن ضمن افزایش حمایت از عربستان، فعلاً از
ورود مستقیم به جنگ یمن
خودداری می‌کند و تمرکز اصلی آمریکا بر باز نگه داشتن دریای سرخ است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22846" target="_blank">📅 10:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فایننشال تایمز:
ایران و کشورهای شورای همکاری خلیج فارس روز دوشنبه در شهر صلاله عمان درباره سازوکار مدیریت موقت تردد کشتی‌ها در تنگه هرمز مذاکره می‌کنند.
این نشست به ابتکار عمان و ایران برگزار می‌شود و نخستین دیدار سطح بالای دیپلماتیک میان ایران و وزیران خارجه شش کشور شورای همکاری خلیج فارس از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران در فوریه است. هدف مذاکرات، رسیدن به توافقی موقت برای تسهیل کشتیرانی در هرمز و کاهش تنش‌هاست.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22845" target="_blank">📅 10:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانال ۱۴ : سخنگوی IDF، جنرال بریگارد ایفی دافارین، به عمق شبکه تونل حزب‌الله در تپه علی طار در جنوب لبنان وارد شد، پس از اینکه نیروهای ما کنترل عملیاتی تپه و تخریب زیرزمینی زیرساخت‌ها در منطقه را به پایان رساندند.“این شبکه تونلی طی دو دهه ساخته شد، با بودجه و هدایت توسط رژیم تروریستی جمهوری اسلامی”، دافارین از تپه‌ها گفت. به گفته او، زیرساخت‌ها به عنوان یک مجموعه مدیریتی مرکزی و به عنوان “مرکز مغز” واحد بد حزب‌الله در منطقه فعالیت می‌کردند، از جایی که در عملیات شمالی کراس، عملیات عقاب، و همچنین در جریان نبردهای فعلی انجام شد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22844" target="_blank">📅 07:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935a8bd7c0.mp4?token=gR1BondUtSilfu7EiMzBxZFT7VTsnQkUUq05kO-YT-9mNyz2QZBCoo0QScu2KdSJJ7MEcR3BkqEgmZMqIBkXvw4SlzxTqfkBm75_1lC5Yj58EbfTQE2FLzLnrNbLoSRTR6ruu9_qr7lrs9OHnadN6_k0Bn53qMZ1niwXYpSgnGjuthv6gFSvNPHkGGjO_oeh-ptNthxXycLntzNAFrFi9CIiwaSRTR0hFUKHmliASihKyod0AdxU148VJb3F9lh4OpCx2zsEsEPairK2LBXqN3R1-LKF3x13xPmJ73CoA2rU7a8InhOBqDLv3Sl61TUrjR3lSiU7kSq3PoEHDIm-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935a8bd7c0.mp4?token=gR1BondUtSilfu7EiMzBxZFT7VTsnQkUUq05kO-YT-9mNyz2QZBCoo0QScu2KdSJJ7MEcR3BkqEgmZMqIBkXvw4SlzxTqfkBm75_1lC5Yj58EbfTQE2FLzLnrNbLoSRTR6ruu9_qr7lrs9OHnadN6_k0Bn53qMZ1niwXYpSgnGjuthv6gFSvNPHkGGjO_oeh-ptNthxXycLntzNAFrFi9CIiwaSRTR0hFUKHmliASihKyod0AdxU148VJb3F9lh4OpCx2zsEsEPairK2LBXqN3R1-LKF3x13xPmJ73CoA2rU7a8InhOBqDLv3Sl61TUrjR3lSiU7kSq3PoEHDIm-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ شامگاه (صبح جمعه به وقت ایران)، در سخنرانی خود در شب دوم و پایانی مجمع ملی جمهوری‌خواهان در شهر دالاس ایالت تگزاس، به اقدام نظامی برای جلوگیری از هسته‌ای شدن جمهوری اسلامی و تنگه هرمز اشاره کرد. (دوبله)
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22843" target="_blank">📅 06:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac2ec14c.mp4?token=eC6zr8SqiC7cC-1O0grvyGgrbxE0aCZNgO_gTR1-1-bacc7AUT4NFZUy4pKxTJWtW2YQYz55eG2IxP5SuZICIpta5pVNjccVuoDnkvaMTK__tSBOZ_DaxKyETd_PeNU4Ff9FAR06MUAgOmix1cydI18OT1O1xaQ6gTBOqfu3lTDNLHVbYEwqjEd8h03JO8WVw-Nkv8vYg2KZns-lHo1w2obHKBRxLomRv8_A8PZUG6CNA65PxKfR5oA860kFh1hWTO151OyDm983wOYFmg0g1gSfrbEnxfNM333mSbhhA6TxvC0mg7U24P0ZCfnIvCmWTELpUm6Lx3nAuMTOeh_Pxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac2ec14c.mp4?token=eC6zr8SqiC7cC-1O0grvyGgrbxE0aCZNgO_gTR1-1-bacc7AUT4NFZUy4pKxTJWtW2YQYz55eG2IxP5SuZICIpta5pVNjccVuoDnkvaMTK__tSBOZ_DaxKyETd_PeNU4Ff9FAR06MUAgOmix1cydI18OT1O1xaQ6gTBOqfu3lTDNLHVbYEwqjEd8h03JO8WVw-Nkv8vYg2KZns-lHo1w2obHKBRxLomRv8_A8PZUG6CNA65PxKfR5oA860kFh1hWTO151OyDm983wOYFmg0g1gSfrbEnxfNM333mSbhhA6TxvC0mg7U24P0ZCfnIvCmWTELpUm6Lx3nAuMTOeh_Pxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکی
.
خدایا کمکم کند.
جمعیت :
خدایا کمکم کند
اوه! حالا می‌دانم. حالا، می‌گویم که تقریباً همه… می‌دانید اگر رأی ندهید چه اتفاقی می‌افتد؟
به جهنم می‌روید.
این را می‌دانید، نه؟ باشه؟ به جهنم می‌روید. و من نمی‌خواهم چنین اتفاقی برای شما بیفتد، پس لطفاً بروید و رأی بدهید. چون باهمدیگر…
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22842" target="_blank">📅 06:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe1f11f1d.mp4?token=sQ7TlyXiNZeCN-Ao7zHKPTk818rPQxLF3svozQYLFzkFq7gLK3RZjnHwbIOQDACJtNVuJ2nDufWFK6pR3iHo3me9rNCTAtCq9OKhrK2CgmhefZvM8kHRYpXLH0cPhZkWqYWCrUiMyDEbf1r_JQSADxrQ-tJsIb8aGq5whX1mtIV5YwqjClEMjcIwXWEyxD7ZW6I7bCvUM-aIwESi7lKOk4XggGJJMJNFp1xZRSYz_YvAmFZ0i3GozD8od94qHWnU2PVvVkAgw4VV-X5LrzEJsqhb1Ty_pSQArITwTro1xTmOeHdoIMiR1DCdoat-mF5GH_XmBLFTIQlE8TwoQeuLJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe1f11f1d.mp4?token=sQ7TlyXiNZeCN-Ao7zHKPTk818rPQxLF3svozQYLFzkFq7gLK3RZjnHwbIOQDACJtNVuJ2nDufWFK6pR3iHo3me9rNCTAtCq9OKhrK2CgmhefZvM8kHRYpXLH0cPhZkWqYWCrUiMyDEbf1r_JQSADxrQ-tJsIb8aGq5whX1mtIV5YwqjClEMjcIwXWEyxD7ZW6I7bCvUM-aIwESi7lKOk4XggGJJMJNFp1xZRSYz_YvAmFZ0i3GozD8od94qHWnU2PVvVkAgw4VV-X5LrzEJsqhb1Ty_pSQArITwTro1xTmOeHdoIMiR1DCdoat-mF5GH_XmBLFTIQlE8TwoQeuLJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس:
اگر ما وارد ماجرای ایران نشده بودیم، شما الان می‌توانستید با خیال راحت به سمت پیروزی در انتخابات میان‌دوره‌ای حرکت کنید؛ با ۲۲۵ کرسی.
ترامپ:
بله، خب، شما این را نمی‌دانید.
مجری فاکس:
آیا پشیمانی‌ای دارید؟
ترامپ:
نه. من اصلاً به کلمه «پشیمانی» اعتقاد ندارم. البته آدم همیشه می‌تواند کمی خودش را مورد سؤال قرار بدهد و درباره تصمیماتش فکر کند، و مردم هم از من این سؤال را پرسیده‌اند. اگر قرار بود دوباره همان تصمیم را بگیرم،
دقیقاً همان کاری را می‌کردم که انجام دادم. توانایی هسته‌ای آنها را از بین بردم.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22841" target="_blank">📅 06:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb5e8b4ba.mp4?token=oHQoBfQ6PIfbhoYrPBKTtgLETATWet6FYMv4TMDzx4qaPFjwRZIYbgjWjC4ZxP8G0IeFNuwEiM1FV6_cNRmo4x-3D10NY6VdpioyXsMUDuNd8Xo767DjA8L5hAjrrnjWMB3WoBQ85kvxpyt0-lTNgx_dOzdlWqFYL5uFSNS8OyXv5bHGPRkKQxPkws8_cPQoEr3FupP6BunSRTSysHUIutNodncoJV328x-g0nZ3vpU4JyBeJEVNree6zcnVkqjHpp_x0uOFJqgvFV0LqSEYnS0GdhhCGFYjd_BnCaIX_0XujQxgv4EmZBvHr6AOje7bdMQykCgCNF6pdHw5xaQMQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb5e8b4ba.mp4?token=oHQoBfQ6PIfbhoYrPBKTtgLETATWet6FYMv4TMDzx4qaPFjwRZIYbgjWjC4ZxP8G0IeFNuwEiM1FV6_cNRmo4x-3D10NY6VdpioyXsMUDuNd8Xo767DjA8L5hAjrrnjWMB3WoBQ85kvxpyt0-lTNgx_dOzdlWqFYL5uFSNS8OyXv5bHGPRkKQxPkws8_cPQoEr3FupP6BunSRTSysHUIutNodncoJV328x-g0nZ3vpU4JyBeJEVNree6zcnVkqjHpp_x0uOFJqgvFV0LqSEYnS0GdhhCGFYjd_BnCaIX_0XujQxgv4EmZBvHr6AOje7bdMQykCgCNF6pdHw5xaQMQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر ایران سلاح هسته‌ای داشت، ما تماس می‌گرفتیم و می‌گفتیم: "قربان، آیا می‌توانیم با هم ملاقات کنیم؟"
ما با آنها بسیار متفاوت برخورد می‌کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22840" target="_blank">📅 06:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbf0f4f2b3.mp4?token=fcxlphG25HwB1TOmHK7OlVZbycTwcYE7w7JAN8XUD8of_0OPGqzNI7VKVYiFHTv-chYDRYX5DabPTduhQetR5TpkfxIr517j9knbjEaWp0MXsq2cqJBTSXmTkkixJyBpsG5FnpomjHfOtnMnej3Nh-tkqXiKinx9XaHnXeJDxtoOu0FBYnwts_RBRDOzbFk05PTW_vv8xfL5_iNU-4GfQBeOjtnWQgpvz5klwu16UkL8Z2Czwx1PKkqJOqjNBqvPV3eYoyKo0YLmQjxEaFYaJ1ob6ciQHWaz2PH49pIASkf7pthbCQ2ieAyjSAqAILCpDVthxZf8rmG1RF_3QljDwwjaKlf9YymInRibMIiOpQmYI37ghhlaeFqOcqacjBbrdFmqwWl9P2AIxZOnhKjTl1UbZWuDIyOUb4BBFABCNGNfRQ_E4yC7swjf-8Q5nYb0Mx3r6iYwkZ_EpfGBpWKgjVw61vriT2q8zmU8Y-XfTcVimtUA0hdEIr2GOtAOQkZLyo23o1jaPl-ruqCfpOpMC0w00QzjL1sIrhvDChuoNHrQu99-588Sg2In5j-b_PyrmY3MnQd6YyNFB0x57v2BhqBOLx3KzZ6aNgF7XAhfNS9HGznbTvyLcS6EwrwBDIrt0OaXOBLXyYrDoy71Y580xUJruUJvq4iC6-9cwow3ad0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbf0f4f2b3.mp4?token=fcxlphG25HwB1TOmHK7OlVZbycTwcYE7w7JAN8XUD8of_0OPGqzNI7VKVYiFHTv-chYDRYX5DabPTduhQetR5TpkfxIr517j9knbjEaWp0MXsq2cqJBTSXmTkkixJyBpsG5FnpomjHfOtnMnej3Nh-tkqXiKinx9XaHnXeJDxtoOu0FBYnwts_RBRDOzbFk05PTW_vv8xfL5_iNU-4GfQBeOjtnWQgpvz5klwu16UkL8Z2Czwx1PKkqJOqjNBqvPV3eYoyKo0YLmQjxEaFYaJ1ob6ciQHWaz2PH49pIASkf7pthbCQ2ieAyjSAqAILCpDVthxZf8rmG1RF_3QljDwwjaKlf9YymInRibMIiOpQmYI37ghhlaeFqOcqacjBbrdFmqwWl9P2AIxZOnhKjTl1UbZWuDIyOUb4BBFABCNGNfRQ_E4yC7swjf-8Q5nYb0Mx3r6iYwkZ_EpfGBpWKgjVw61vriT2q8zmU8Y-XfTcVimtUA0hdEIr2GOtAOQkZLyo23o1jaPl-ruqCfpOpMC0w00QzjL1sIrhvDChuoNHrQu99-588Sg2In5j-b_PyrmY3MnQd6YyNFB0x57v2BhqBOLx3KzZ6aNgF7XAhfNS9HGznbTvyLcS6EwrwBDIrt0OaXOBLXyYrDoy71Y580xUJruUJvq4iC6-9cwow3ad0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه دعوا شد ، صدای‌چند انفجار @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22839" target="_blank">📅 06:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c36615a19.mp4?token=T1-nx1cOjijnyRaD7SAf8tEjRgQi0De2wF3tGQu2TmTJA62sUm4Pbcg318_fcIHnxJj9qijstazGN63W49gsrL3h3gCD9ASLZq2wwLd9yOei2DKf6e5aEXnya_F0X1HQ9jPZOEsJlMXw_HfMULEVIBkbtzWcil2HZaYYRsJ_ZHjQGqw7FiRjg2xUyiA__MvWdFN5irbwbN1ptjmgQ5AYqxMd_4uffcANADGtr6VcVpftAypq0ZZSlMz-ESrRqQj6aCxyw1foh7WJhq9K6fjX1Y7UmGVvePBagyDsjBS-ErZmKTWealOl-36gDy-noHCabT2aDofl5k11L_cBZRO8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c36615a19.mp4?token=T1-nx1cOjijnyRaD7SAf8tEjRgQi0De2wF3tGQu2TmTJA62sUm4Pbcg318_fcIHnxJj9qijstazGN63W49gsrL3h3gCD9ASLZq2wwLd9yOei2DKf6e5aEXnya_F0X1HQ9jPZOEsJlMXw_HfMULEVIBkbtzWcil2HZaYYRsJ_ZHjQGqw7FiRjg2xUyiA__MvWdFN5irbwbN1ptjmgQ5AYqxMd_4uffcANADGtr6VcVpftAypq0ZZSlMz-ESrRqQj6aCxyw1foh7WJhq9K6fjX1Y7UmGVvePBagyDsjBS-ErZmKTWealOl-36gDy-noHCabT2aDofl5k11L_cBZRO8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس نیوز: چگونه ایران می‌تواند موشک‌ها را پرتاب کند، در حالی که ما آن‌ها را نابود کرده‌ایم؟
ترامپ: آن‌ها همیشه می‌توانند موشک‌ها را پرتاب کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم دارند. البته ما آن‌ها را سرنگون کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22838" target="_blank">📅 06:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22837">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cdw7Fc_D6y-1kwxo6cBkqR4VdvPNDdJtsnwp9qtNM03KaDZGRhbMoqWgbZnh9aaPAag5Kx49_0573EGRr8TmVJvgnIHTvLSVLzerMCOqcvMpupdJiwJgQXFYovkqeauMEwb95mKawBnvNhvMFkD0EGr8b8P5W-2ichFuHtaiR35Ba2LxZCpjlCRWggJvDdqq-8jP-V0VwDNkvg94EpbRdBJvLyfm3KrHOUmNs8pGiX0tVzj8goMjOwLCY5Wex_sTAucdoe7IjFzq_MSq8gSnX-On5kXKbz7zkLISB8kyaaj5JBn1qxrH1VDCO4cw_gy-V7_EM1Q4rlaAjYgwdHkAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا : دو شناور در تنگه هرمز، در حدود ۴ مایل دریایی غرب «خصب» عمان، مورد اصابت قرار گرفته‌اند.
یکی از شناورها هم‌اکنون در آتش می‌سوزد، در حالی که وضعیت شناور دوم همچنان نامشخص است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22837" target="_blank">📅 00:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رسانه های اسرائیلی : ده ها جسد تروریست های حزب الله در تونل ها پیدا شد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22836" target="_blank">📅 00:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو : امشب بزرگ‌ترین پایگاه برون‌مرزی ایران یعنی تونل‌های «علی طاهر» در لبنان را منهدم کردیم. مأموریت با موفقیت به پایان رسید. سال نو یهودی مبارک! @WarRoom یاشار : آتیش بازی سال نو به سبک بی بی
💥
😂</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22835" target="_blank">📅 00:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22834">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b3b329e59.mp4?token=sHoeB3A30dtCqvH8DsOFZ9bWn1xQaY0C1Amz80RsK5oTZ6atwQebzxNCS7xmZ_utEysav14f4RmjyNYOVEDDsuC9xokMc1gOfn6g3q5L4rp0lifCs22o7k0_TJl5y_WvippOFpe_SP7zwggYwPHpebeh6Y9XTbltXZtcIxJkHxwSjU0MZ8m-g_88CU65EkMTCzyvB9qTSeYQoDGyxHCBMXlCqRtsoEgGp59X4P-_7A5oXS3xISNRNlD9T8kuPOGR4v6BQ1yjYV5X4gMLpz-3fPHEHckDVep5SfTkBSuDzQeppbhRpD-mz8aoVOBgQfIU8g0T5GKVsbgdYBDbp_g_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b3b329e59.mp4?token=sHoeB3A30dtCqvH8DsOFZ9bWn1xQaY0C1Amz80RsK5oTZ6atwQebzxNCS7xmZ_utEysav14f4RmjyNYOVEDDsuC9xokMc1gOfn6g3q5L4rp0lifCs22o7k0_TJl5y_WvippOFpe_SP7zwggYwPHpebeh6Y9XTbltXZtcIxJkHxwSjU0MZ8m-g_88CU65EkMTCzyvB9qTSeYQoDGyxHCBMXlCqRtsoEgGp59X4P-_7A5oXS3xISNRNlD9T8kuPOGR4v6BQ1yjYV5X4gMLpz-3fPHEHckDVep5SfTkBSuDzQeppbhRpD-mz8aoVOBgQfIU8g0T5GKVsbgdYBDbp_g_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : امشب بزرگ‌ترین پایگاه برون‌مرزی ایران یعنی تونل‌های «علی طاهر» در لبنان را منهدم کردیم.
مأموریت با موفقیت به پایان رسید. سال نو یهودی مبارک!
@WarRoom
یاشار : آتیش بازی سال نو به سبک بی بی
💥
😂</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22834" target="_blank">📅 00:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیویورک تایمز: پشت پرده ونس ترامپ را دور زد؛ مستقیم از فرماندهان ارتش آمریکا ارزیابی های دقیق از جنگ گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22833" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا: آمریکا در چارچوب «عملیات طرد اقتصادی ایران»
۱۴ فرد و ۵ نهاد
مرتبط با شبکه‌های نیابتی پشتیبان
کتائب حزب‌الله، حزب‌الله لبنان، نیروی قدس سپاه و شبکه‌های دور زدن تحریم‌های ایران
را تحریم کرد. افراد تحریم‌شده شامل
علی حسن فرحان اللامی، حسین احمد حسین الضحیباوی، محمد امین فاضل علی الشیخلی، کرار محمد قاسم الحریشاوی، عباس جواد کاظم التمیمی، عبدالله ناظم لعیبی العامری، خلدون ناصر مریوش العباده، مجید علی‌اکبر نامدار المندلاوی، عبدالحسن علی ا. نامدار المندلاوی، حسین ابراهیم، عبدالله همیه، غیث حسین وهبه، مروت جمیل زهرالدین و امیر المکانسی
هستند. پنج نهاد نیز شامل
Al-Brouj For General Contracting، Ain Al-Iraq، Shams & Bahr Trading Company، YIM Exchange و Gold Pro SARL
است. آمریکا مدعی است
شرکت شمس و بحر مستقر در دبی
در انتقال میلیون‌ها دلار از عراق به ایران نقش داشته و برخی افراد این شبکه نیز در انتقال منابع نیروی قدس به حزب‌الله فعالیت داشته‌اند. همزمان، دفتر کنترل دارایی‌های خارجی آمریکا اعلام کرد روند
رد اکثریت درخواست‌های معوق برای مجوزهای اختصاصی مرتبط با ایران
را آغاز کرده است. همچنین OFAC از
تسویه یک پرونده به ارزش ۱ میلیون و ۴۲۷ هزار و ۲۳۰ دلار
بابت ۳۹ مورد نقض تحریم‌های ایران خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22832" target="_blank">📅 23:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed5786f00.mp4?token=nr4kuC25m7vMeKm-7DP9dP02A2y85dbRpo2GOERr46k_bf6B2mtRgsvBMR5c78xMC7FBlWLBfabidIUVeDUz2PNZGVHGQ24V8oZYWRifpFZf6cdYkSATrQ6CZkMyphv0thVDkzwrhu__V1TrH6EleYO_4aPsfwFbLcahmGTu5_g4g2wLU6Efjyye8lZj-y1-8T6lXg_SzmwA56ntJDCtBZpiQHgQacLZ6Ty-tEGqozX3UihxUQXlu4OnmGZNg95GlHdOgZqSdug_yovoH9bPJlaKLERLdoqX0n8xyl3AX_ZCjNjD3_oDDmjygoAC365O5UHSX6ygZFm17AuZ3AcAuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed5786f00.mp4?token=nr4kuC25m7vMeKm-7DP9dP02A2y85dbRpo2GOERr46k_bf6B2mtRgsvBMR5c78xMC7FBlWLBfabidIUVeDUz2PNZGVHGQ24V8oZYWRifpFZf6cdYkSATrQ6CZkMyphv0thVDkzwrhu__V1TrH6EleYO_4aPsfwFbLcahmGTu5_g4g2wLU6Efjyye8lZj-y1-8T6lXg_SzmwA56ntJDCtBZpiQHgQacLZ6Ty-tEGqozX3UihxUQXlu4OnmGZNg95GlHdOgZqSdug_yovoH9bPJlaKLERLdoqX0n8xyl3AX_ZCjNjD3_oDDmjygoAC365O5UHSX6ygZFm17AuZ3AcAuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه انفجار از دید سربازان اسرائیلی
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22831" target="_blank">📅 23:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک منبع آمریکایی به شبکه CNN گفت:
تخمین زده می‌شود که صدها نفر از نیروهای سپاه پاسداران انقلاب اسلامی در داخل یمن حضور دارند تا به حوثی‌ها در مسدود کردن تنگه باب‌المندب کمک کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22830" target="_blank">📅 23:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزارت دفاع : به زودی گوشه‌ای از کوه‌ یخ صنایع دفاعی ایران را می‌بینید.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22829" target="_blank">📅 23:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/045dcbc8ef.mp4?token=RZCdHI8Vzfjzgjm4Rp5legrzjKDZlbdpDfnsAvbzsqExKxC98-S5Z5iz27mtQ_dq9Yy96LT80g48CDc7VCW10L00XgGKqkb7wlQuK5ZxGW5eHI-xKaEozmwFSjADiUgUcXxGTfhZ4YgIhgd7vGmv5cySPEoER4_0x_5UDDWGWgd-ERr-glz11pW3MPvJKesU1Op7PqRfkshXKju6FYpGE3_Y7x836Zi-Io4yyFxPOUy3tYbDsQbWQZp_rrimkFRBMYMUbTbXurFYE9Ls_whiTnDOVeLOOiBmid2CQvjI4wtFQIgt5kA_zRJNKfhDmMCszywWaIxz4LcstRGQ_4ecJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/045dcbc8ef.mp4?token=RZCdHI8Vzfjzgjm4Rp5legrzjKDZlbdpDfnsAvbzsqExKxC98-S5Z5iz27mtQ_dq9Yy96LT80g48CDc7VCW10L00XgGKqkb7wlQuK5ZxGW5eHI-xKaEozmwFSjADiUgUcXxGTfhZ4YgIhgd7vGmv5cySPEoER4_0x_5UDDWGWgd-ERr-glz11pW3MPvJKesU1Op7PqRfkshXKju6FYpGE3_Y7x836Zi-Io4yyFxPOUy3tYbDsQbWQZp_rrimkFRBMYMUbTbXurFYE9Ls_whiTnDOVeLOOiBmid2CQvjI4wtFQIgt5kA_zRJNKfhDmMCszywWaIxz4LcstRGQ_4ecJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لرزش موج انفجار حاصل شده از انفجار تپه‌های علی طاهر از دوربین مداربسته یک خانه ،بنا بر گزارشها، این زلزله ۴.۱ ریشتر گزارش شده.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22828" target="_blank">📅 23:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیروی هوایی اسرائیل شهرک‌های «المنصوری» و «زبقین» در جنوب لبنان را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22827" target="_blank">📅 22:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به‌صدا درآمدن آژیرهای خطر در شهرهای ابها و خمیس مشیط عربستان
سازمان دفاع مدنی عربستان سعودی از فعال‌سازی سامانه هشدار زودهنگام در برخی مناطق جنوبی این کشور خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22826" target="_blank">📅 22:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وحیدی: خدای ما خدای زنده است، خدای غربی ها خدای مرده است
.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22825" target="_blank">📅 22:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تلگراف: ایران برای نخستین‌بار موشک‌های مجهز به جستجوگرهای الکترواپتیکی را علیه ناوهای آمریکایی به کار گرفت:
مقام‌های آمریکایی مدعی شده‌اند ایران در حملات اخیر به ناوهای آمریکا از موشک‌های مجهز به
حسگرهای اپتیکی
استفاده کرده است که با بهره‌گیری از دوربین و حسگرهای نوری می‌توانند اهداف متحرک را در مرحله پایانی پرواز شناسایی و ردیابی کنند. ایران پیش‌تر موشک بالستیک میان‌برد
قاسم بصیر
را معرفی کرده بود که طبق گزارش‌ها به چنین سامانه‌ای مجهز است؛ با این حال،
استفاده قطعی از قاسم بصیر در حملات اخیر هنوز تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22824" target="_blank">📅 22:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22823" target="_blank">📅 22:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این انفجار یک زلزله ۴.۱ ریشتری ایجاد کرد !
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22822" target="_blank">📅 22:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">توییت جدید سفارت ایران : سرآشپز رضائی در حال پخت و پز است. @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22821" target="_blank">📅 22:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ارتش اسرائیل: کل سامانه پدافند هوایی اسرائیل در حالت آماده‌باش کامل قرار دارد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22820" target="_blank">📅 22:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4ZkSwM5jZRIxIkxLny8g9rABrpjPiGT6-q2i_Ja8paRv9DnPaZHnR4zjp8hjd5PZjmHF7VpxNaBmZT5mqr1z0Dbtj5sguzjEei0LvOR25R3WBkOOLIeQLGPZ1X22JZ36O0eXg__EsaoX-curQiwOnn0ZyoiciAN7ZmeJ3yNbnEIJo2OiTpPZGzzyKUbewUfwYiTkbvwr2OqA-U2lJkYq7a7Ku_toQvUq7KGL8u2nrlyEU_bi0-dDj9vGJhs9VIvtf2pEV_Wv9nsOSByylnn4-_fCMGJI6H8NJ2I_EWHPlvm-pTqS6fmelkEeBGwH1nxEi9xcwKZ2ofe3C1xAUS5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان رفتیم مرحله بعدی‌کمر بند ها رو بیندید ، آیا رژیم اشغالگر جمهوری اسلامی جواب میده ؟</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22819" target="_blank">📅 22:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22818" target="_blank">📅 22:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بیانیه مشترک نخست‌وزیر و وزیر دفاع اسرائیل درباره ارتفاعات علی‌الطاهر:
بنیامین نتانیاهو و اسرائیل کاتز: «به دستور نخست‌وزیر و وزیر دفاع، نیروهای ارتش اسرائیل
زیرساخت‌های زیرزمینی حزب‌الله در منطقه علی‌الطاهر را منهدم کردند
و ایجاد منطقه امن در جنوب لبنان به پایان رسیده است. این زیرساخت‌ها که طی دو دهه با بودجه و برنامه‌ریزی ایران ساخته شده بودند، قرار بود به‌عنوان پایگاهی برای
تسخیر الجلیل و دیدبانی و شلیک به سمت متولا و کریات شمونا
استفاده شوند. با نابودی آنها، ارتش اسرائیل به
کنترل عملیاتی کامل منطقه علی‌الطاهر، در سطح زمین و زیر زمین،
دست یافته است. نیروهای ارتش در این منطقه باقی خواهند ماند، از بازگشت حزب‌الله جلوگیری و به نابودی زیرساخت‌های تروریستی آن ادامه خواهند داد. اسرائیل همچنین اعلام کرد هرگونه تلاش برای آسیب‌رساندن به غیرنظامیان یا نیروهای اسرائیلی را
با قاطعیت پاسخ خواهد داد.
»
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22817" target="_blank">📅 22:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22816">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22816" target="_blank">📅 22:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">استاد بزرگ شطرج، نتانیاهو : نیروهای ما عملیات خود را در تپه علی الطاهر در جنوب لبنان آغاز کرده‌اند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22815" target="_blank">📅 22:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595c3ab294.mp4?token=SySleSB1oleTE-9U2k81tf2-p_Vts8oUMHdDdrttLWlSeTj1cFgDA7LyIwH-uDUNMW3qk3eTuSyrruyuGRR0aeISqGQzoqPjskhXfL7Slm0lhaUM8VuwP60jE4D79cDDSTwWBtewDDcJy9YjclQM62wed2qM5UuwqPJtM920gT8n-8mzfhNinapIHb1MTyLoSnq4NC88kqxJYrAciIrX6U96m8Cgo_3GJtbaL_xYCJRmpflkDrKo4TQPwXb9l-n20smFsK5kdbx3CltLzvpsyevPwK3dBN6wxee9ZHlzlvI6BFSaCSXyMeDy1QmqYW54xNuIpdFQEFEmJjMIs131qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595c3ab294.mp4?token=SySleSB1oleTE-9U2k81tf2-p_Vts8oUMHdDdrttLWlSeTj1cFgDA7LyIwH-uDUNMW3qk3eTuSyrruyuGRR0aeISqGQzoqPjskhXfL7Slm0lhaUM8VuwP60jE4D79cDDSTwWBtewDDcJy9YjclQM62wed2qM5UuwqPJtM920gT8n-8mzfhNinapIHb1MTyLoSnq4NC88kqxJYrAciIrX6U96m8Cgo_3GJtbaL_xYCJRmpflkDrKo4TQPwXb9l-n20smFsK5kdbx3CltLzvpsyevPwK3dBN6wxee9ZHlzlvI6BFSaCSXyMeDy1QmqYW54xNuIpdFQEFEmJjMIs131qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل اعلام کرده است که بیش از ۱۱۰۰ تن مواد منفجره برای تخریب زیرساخت‌های تونل‌های واقع در زیر منطقه "علی طاهر" در جنوب لبنان استفاده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22814" target="_blank">📅 22:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/646f9ab553.mp4?token=AwNTZFjy1F4hl_4wlNn1mKQrESplM_Od62GZIKYb3jQy_w4Idfq0Kv1hMeYJlVHt_utKMvwXjniZLd_WNoyPT06hkQTcjA4ovot69M187D0cxVCpL2zVI5FuNuTa2ZlLfmUJYuxgWkqXtK2GyCuP0YeLBA-M9jRdBBZ5LMqorvZ6njSQ5Z7XFjvCWVxarVQtxYRmjH7vWX_0abN8fydoxLB55bDcjEgApBK79b3eAv8Dk9IgAXScqeniq4EMQYUMG5vcvwK8bDYh8_pMomCLvVsG6MsdiKMWFL4EU-kPLM9oEaY6fKUBGi1blR6lM46NJK9gbdpGndFEpQePHLhN2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/646f9ab553.mp4?token=AwNTZFjy1F4hl_4wlNn1mKQrESplM_Od62GZIKYb3jQy_w4Idfq0Kv1hMeYJlVHt_utKMvwXjniZLd_WNoyPT06hkQTcjA4ovot69M187D0cxVCpL2zVI5FuNuTa2ZlLfmUJYuxgWkqXtK2GyCuP0YeLBA-M9jRdBBZ5LMqorvZ6njSQ5Z7XFjvCWVxarVQtxYRmjH7vWX_0abN8fydoxLB55bDcjEgApBK79b3eAv8Dk9IgAXScqeniq4EMQYUMG5vcvwK8bDYh8_pMomCLvVsG6MsdiKMWFL4EU-kPLM9oEaY6fKUBGi1blR6lM46NJK9gbdpGndFEpQePHLhN2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل: آیا ایران واکنش نشان خواهد داد؟ پس از ماه‌ها عملیات، نیروهای اسرائیلی کنترل ارتفاعات علی طاهر را تکمیل و زیرساخت‌های تروریستی این منطقه را منهدم کردند و اکنون برای مرحله بعدی آماده می‌شوند. همزمان، با نزدیک شدن به سال نو یهودی، سطح آماده‌باش…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22813" target="_blank">📅 21:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رادیو ارتش اسرائیل: فرماندهی منطقه شمالی ارتش اسرائیل، دقایقی پیش شبکه تونل‌ها را در رشته کوه‌های علی طاهر در جنوب لبنان تخریب کرد.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22812" target="_blank">📅 21:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22811">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ada8c06b7.mp4?token=i1-fJU542R-MAFvXVUPOp3BtJhSVrxmIBMSEuqwd8px7T0S5C7b7n7kpWw_Akq9dxG5thEbE9J-bHyStiVfHjbvHNY28CfXdrbrm-z1_5t3X5CfjnAkTZKRPYv4YJn5SPKmwZfQaX8cZo6O3UArJZSOpdbHECKTWqc9X2MC1Hx2xKrMx5tpj9Txva210No0Pw2-p3u6WhpOiZ8Yo0Ab0MWEphglpS50zGbrKeHFmwAcism7mm50wXAsA_Rs-84Di1PIxCYpkDpcV9aiyghXzRAqRK3yPuok_PTj8GDOYwt9CAf1y7G98I6dRzvT6OiSVyNRPrUTRyWBoCa9l86A1PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ada8c06b7.mp4?token=i1-fJU542R-MAFvXVUPOp3BtJhSVrxmIBMSEuqwd8px7T0S5C7b7n7kpWw_Akq9dxG5thEbE9J-bHyStiVfHjbvHNY28CfXdrbrm-z1_5t3X5CfjnAkTZKRPYv4YJn5SPKmwZfQaX8cZo6O3UArJZSOpdbHECKTWqc9X2MC1Hx2xKrMx5tpj9Txva210No0Pw2-p3u6WhpOiZ8Yo0Ab0MWEphglpS50zGbrKeHFmwAcism7mm50wXAsA_Rs-84Di1PIxCYpkDpcV9aiyghXzRAqRK3yPuok_PTj8GDOYwt9CAf1y7G98I6dRzvT6OiSVyNRPrUTRyWBoCa9l86A1PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی تایر ترکید
🤣
با ترکیدن یک تایر به دنیا آمد و با ترکیدن یک تایر از دنیا رفت
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22811" target="_blank">📅 21:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22810" target="_blank">📅 21:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوست بیلیونرم ترجمه خبر زنده : ارتش اسرائیل عملیات انفجار تپه «علی طاهر» در جنوب لبنان را آغاز کرده است.
صدای انفجارهای بسیار شدیدی شنیده شده است.
برخی از ساکنان جنوب لبنان از وقوع زمین‌لرزه خبر می‌دهند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22809" target="_blank">📅 21:46 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
