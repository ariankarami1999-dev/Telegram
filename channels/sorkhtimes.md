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
<img src="https://cdn4.telesco.pe/file/pXIRET1Ivb6DCLzsszBIujvTv6o9-D4vddbP2JDpiRggSqefwnpLncG6U5LH713NDS025lHdMxdzAKFvoGZrIVh6m892xYA1fb8sEKwMC3qo2QV-PAKrKDconEZKcQ1zpQs7UVkqHGnebJXojWQV-v5MlyG9Ka0nQUsUHK_8-TNuetFi35hq-oXYi2LTpl5WbJ8VLRzJPXIt_C9Fmdlh85BMrGqltzd5AwHyWnhRFjvjFX8v8ZRyO8oHey5EFdIRJ922FVbFQGh2Ol4N--6o-m7nvSQ6mCQqd4Qq5H4wq9KSglOBIoxWYJxX_pjXc8JOUQPz7OmKVNoVJHaNEFXIgw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 03:59:58</div>
<hr>

<div class="tg-post" id="msg-141005">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvI2jU3kOkJ67SkJyugtBcv4vceZBJxs1MwbnicIXkbY9taycp6nZe88wpYALV6UPbBNVeMY-R3EjInDaTi9h2Gm-jyhaJcFzdLXHmN95CrSAKHCVHWETRBX32aH3E_pEgEcobgKi4lenuHDOlxcBV0SOwy9LZRqK6l5V0-EUi38oC8EZq94fqiftO05pRTm4Azndu91LzbuydJHQzS8UEPl_-3N9CL1ELNSdIz8tPLzzJK1q8nRrfKzyz4UpSa4vP-bdpKa-14oAUbJTNVFFMdQK5YqDJ1EJN08OC8sPCyusLsU47pJca17vhrRJxuByoSYq9rUco-AJ0iHCZQ7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
سه‌شیرها در کمین؛ چک‌ها آماده‌ی شکستن نظم انگلیس!
🔥
⚡️
[
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇨🇿
جمهوری‌چک
]
⚽️
انگلیس با مالکیت و حجم حملات بالاتر، احتمالاً بازی را از همان دقایق ابتدایی در اختیار می‌گیرد. جمهوری‌چک روی دفاع فشرده و ضدحملات سریع حساب می‌کند؛ اما مقابل فشار مداوم انگلیس، حفظ کلین‌شیت دشوار است.
سناریوی محتمل: برتری انگلیس در موقعیت‌سازی و گلزنی، با احتمال بالاتر برد انگلیس و مجموع گل‌های ۲ تا ۳.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/141005" target="_blank">📅 01:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141004">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWyoAnnSRxvn8nydPw-pxvT2Bzi0ScXZtdnf-irxo4t7vM3SwiAHnHlFsdOVDKjX7_63MzZEdUE1mF4SN-K9mehNZzKjw307rJSaWAXWZJOntXYi0wqG3dK2D7WAxNiDOLIZrYwhfGbryzybeBLByVQfVSZm5_qVFfOrecd2ix6Q6shnN7bw4dUuE7EkLW-pet6PHmb56gJEAj2iGzxJWTlHCo6CGTjoJBeFzv1fRRiI-92GIsPTPB3ad9SYyCzcyQXhrAEFtXY3oUkd5RtN80I2SyJmFI7NiirC2g_zXWm5vP0LuEdAxj90BT6pFNm-L7FQJYZsTix-pwgU-AXHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سعید شیرینی، سرپرست سابق پرسپولیس، از مطالبات حدود ۷۳ میلیارد تومانی خود از این باشگاه گذشت.
🚨
بر اساس اعلام پرسپولیس، این موضوع مربوط به دو پرونده حقوقی بوده که یکی از آنها بیش از ۴۱ میلیارد تومان و دیگری ۸ میلیارد تومان مطالبه به‌همراه خسارت تأخیر تأدیه داشته است. با اعلام رضایت شیرینی، مجموعاً حدود ۷۳ میلیارد تومان از خروج منابع مالی باشگاه جلوگیری و پرونده‌ها برای مختومه شدن ارسال شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/141004" target="_blank">📅 01:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141003">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
مهدی ترابی در اندیشه‌ی بازگشت به پرسپولیس/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SorkhTimes/141003" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141002">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✖️
✖️
محمودی و صادقی کماکان از آماده ترین بازیکنان تمرینات پرسپولیس هستند
✅
✅
هر دو به همراه زارع در دفاع از بهترین های بازی دیروز مقابل گل گهر بودند.
✅
✅
باتوجه به مصدومیت ها به احتمال زیاد این دو بازیکن در بازی های آتی برای سرخپوشان به میدان خواهند رفت.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/141002" target="_blank">📅 23:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141001">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
عادل فردوسی پور: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبود بهش گفته خودتو بزن به مصدومیت تا تعویضت کنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/141001" target="_blank">📅 22:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141000">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
موبایل قاپ‌ها به حدادی هم رحم نکردند
💢
مدیرعامل پرسپولیس بعد خروج از ورزشگاه شهید کاظمی و دیدن بازی تیم بانوان در خودروی خود مشغول مکالمه بود، که یک سارق با موتور نزدیک شد و با قاپیدن گوشی همراه حدادی متواری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/141000" target="_blank">📅 22:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140999">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
✅
فووووووووری از فرهیختگان
❌
❌
پرونده آسانی از دست فدراسیون خارج شد حالا دیگه فقط ای اف سی درباره این پرونده تصمیم میگیره و کسی نمیتونه کاری کنه    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/140999" target="_blank">📅 22:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140998">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🔴
علوی: هیچ جامی قرار نیست به استقلال داده بشه و بحث قهرمانی این تیم در سال گذشته منتفی شده
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/140998" target="_blank">📅 21:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140997">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D84YggrhSgR9JhFpqWPrUujNtTo_TK23Pj9_z4qzIaQZvYOmycwmdSbyOrzPSdzJqULywLFTDi23OO_S6SeVWSUNTGwGfEZnp3pqcgS1Fw7As8HojDwLNOcPiLem7-F8naWh77Nv-XMFB-g5ZmVyC3wEttL3X2vjFDdeVk4f9HbqzgxET3b65ZS3zaxNQ2dxecp0nGOcp1WvbDCLnfJwxMgCu-4BLTSpZmx5pXS1Rp5492Q8yDIES1tBrHdUNgtfzryJZXu6iZsKfQ7__AJPdyI9Ho0Z_d_UVAWUvk-STLYWHJQZ_wd-ys5TuK4atycohYGnRdZSNUniAa38o6ODGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚩
گزارش تصویری از تمرین امروز پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/140997" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140996">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💚
عادل فردوسی‌پور: دیگه حوصله شوخی‌کردن با قیمت دلار روهم نداریم، روزگار سخت و تلخی که سپری می‌کنیم، شروع فصل لیگ برتر، با دلار 187 هزار تومانی، بازگشتش از فیفادی، با دلار 270 هزار تومانی!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/140996" target="_blank">📅 21:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140995">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
گفته میشه دولت قطر به تیم فوتبال استقلال قراره مثل آمریکا ویزا ساعتی بده تا این باشگاه برای بازی با الغرافه مشکلی نداشته باشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140995" target="_blank">📅 21:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140994">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✖️
✖️
✖️
فرصت طلایی
✖️
✖️
پرسپولیس در هفته‌های پیش‌رو برنامه بهتری نسبت به رقباش داره؛ استقلال و تراکتور درگیر آسیا هستن و سرخ‌ها هم بازی‌های عقب‌افتاده‌شون رو دارن.
✖️
✖️
با توجه به لغو جام حذفی، هفته‌های ۹ و ۱۰ می‌تونه فرصت خوبی برای تارتار و شاگرداش باشه تا…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/140994" target="_blank">📅 21:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140993">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
لحظه گل ثانیه پایانی جوانان پرسپولیس مقابل پارسیان توسط محمدامین قرنجیک
👍
👍
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140993" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140992">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1mKrZsW2JlxSp7JRkzFP43sc-FFPoNLTQxSmEgAH_XCvwV1vaxaKgO6RmjqnX3gBoBXLU_egign1Kyer4k05c4lcfk60u9iEgyWbOVjuT4Tgp60c3SuWer8X4n6177YdYL-04B2W16WHl4pDlVekGNqm5MoerXp-uLB2QtF8QgtCh6dNN5fTy2x8gVD6tQCc6Sw75nnssyxcPtxXR17iKN8uuWUK6LJhJZXAfElRzDUFZgLMn0Wbmddv1z80eUzKcsyJcMa0lK4O69NgtEWoZjBuljujL_WqavR3VX2BEcQocp5qt6fFlRYhyIg5xe9DtBy2z0vpbV_RfUmzDRZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
مهدی طارمی زمینه آزادی ۸ زندانی شد
👍
مهدی طارمی در طرح حمایت از حقوق اجتماعی و رفاه زندانیان نیازمند استان تهران، زمینه آزادی ۸ زندانی را فراهم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140992" target="_blank">📅 19:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140991">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
مزایده اموال پرسپولیس با یک خریدار خاص
🚨
در پی شکایت یکی از طلبکاران باشگاه پرسپولیس، دادگاه شعبه ۴۱ عمومی حقوقی تهران حکم به توقیف و سپس مزایده اموال این باشگاه داد که این مزایده در نهایت برگزار شد و بخشی از اموال پرسپولیس به فروش رسید
🚨
🚨
در این مزایده،…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/140991" target="_blank">📅 19:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140989">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmN_5mXObZryhu529bywKs6UcZR0y_cJg4nLdfhv5s6PZUQuc8YoxesZv2QnFWmN17kZeq8gnJvZtC1pEpojuGh_J4G2PHNaCOm7QYIpGHb9WFWlwWoZDzyxBGThNA-SaekT7ND8XyPHJ-E4Qq4LopMJXLHpFlHCtlWBm0J6kvdQYPjRpgx4hpwvanzPA_r8wb65UwUlY2eLrwlZxcNtmU7-wpdYQqDR7lWRxOK6saRnFHxbHvRHGKCqD-SirVDq58nMHpa2hMmdO08HBJhjungXxPvI9czXuzaVr91lFAnzglnwYvZ5Wb6lK0rUuoMwhbBE2kqXUvxil9vSmA6BGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد سلسائو با وایکینگ‌ها؛ پرتغال در برابر نروژ، یک شب پر از هیجان!
🔥
⚡️
[
فرانسه
🇫🇷
🆚
🇧🇪
بلژیک
]
⚽️
فرانسه از نظر کیفیت موقعیت‌سازی و عمق ترکیب دست بالاتر را دارد، درحالی‌که بلژیک بیشتر روی ضدحمله و انتقال سریع حساب می‌کند. با توجه به قدرت هجومی دو تیم، سناریوی گل‌زنی هر دو طرف محتمل است؛ اما فرانسه شانس بیشتری برای کنترل نتیجه در نیمه دوم دارد.
سناریوی محتمل: برد فرانسه با اختلاف یک گل.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/140989" target="_blank">📅 19:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140988" target="_blank">📅 17:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
🚨
فووووووووری
✔️
ای اف سی در نامه ای به فدراسیون گفته پرونده فسخ یاسر آسانی مشکوکه و جزییات دقیق خواسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140987" target="_blank">📅 17:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140986">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsR2LKaG_vslFZnbxA4t5GTIAONt3WVuSn0IkNoPm_AyGV2UMxWrPy5chFgcU2u7q5f8AaRcgDJBTESoL1l9uaoiKBPjs1GLg4oRGNxU1poZCb-nFMsLrIXe6afcUmbl3PyPtn5mubPH1pa9Iccrs7Di1YyK5UBBLzUJo--bj4dItMP2w-AMOkphE_n1xBrpkYvBrktmEb65bmMeuQ11pbCjK5aBdCjGRJb08lMpeCuYRGK6H5QvCSEi-0Xvp-N4-STLg-Nc6OO9ExY9Ve6M6Lm0Nv_OiWLnGVzMC-AWyolzyLoRtSz5mOs4CtVdDD9hEpYiW4EOw2GRtPzcqtxOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
ساختمان شهدای میناب باشگاه پرسپولیس مزین به تصاویر شهدای مدرسه میناب شد
🔴
به گزارش سایت رسمی باشگاه پرسپولیس، این اقدام، ادای احترام خانواده بزرگ پرسپولیس به مقام شامخ شهدا و خانواده‌های معزز آنان و گامی در جهت پاسداشت فرهنگ ایثار، فداکاری و شهادت به شمار می‌رود.
🔴
باشگاه پرسپولیس ضمن گرامیداشت یاد و خاطره تمامی شهدای مدرسه میناب، بر ضرورت صیانت از نام و یاد شهدا و ترویج فرهنگ ایثار و فداکاری در جامعه تأکید دارد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140986" target="_blank">📅 17:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBWPibePsE_21SOM_UqEYhFlTDL8K_gOLGuXPSq710oIWedLQOb604EAncIwPaV_BdXx-UExMnijGyCYSzFU37UR68xPqJ7xkkcciY-tIHWGonsCcsRM9sNTgnd1T9kUbzyuBtppeKfIJBxJ0JQ8aRXAF00VVS6yUKgZhl_kKD8emLryGUF6MzSaHDbTDY0G-WuWibitQ0EsMsaI0c9hIHJIcGxK5Fpn_WrRv2C0pHJ6877g8FwAqi4JJpKDG0Ow6gddqpq_VTQY3ymZdChdcOUOS02FkzZvL9cwVYupVn07CvCBfj0bm0AX04OtZcZ8S7zEWkzu6KsW1GEq9iHN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
سیدحسین شریفی به عنوان مدیر صدور مجوز باشگاه پرسپولیس منصوب شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/140985" target="_blank">📅 16:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140984">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
نامه دوم AFC برای بررسی پرونده یاسر آسانی؛ پاسخ نامه اول قانع‌کننده نبود
🔹
کنفدراسیون فوتبال آسیا (AFC) پس از دریافت گزارش‌هایی درباره وضعیت یاسر آسانی و احتمال غیرمجاز بودن حضور او در ترکیب استقلال، در دو نامه از فدراسیون فوتبال ایران و باشگاه استقلال…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140984" target="_blank">📅 15:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140983">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
کنفدراسیون آسیا جواب فدراسیون رو نپذیرفت
✅
کنفدراسیون فوتبال آسیا برای بررسی پرونده یاسر آسانی، این بار در نامه دوم مدارک و مستندات بیشتری از فدراسیون و استقلال خواسته و تأکید کرده فوراً ارسال بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140983" target="_blank">📅 15:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140982">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
کنفدراسیون آسیا جواب فدراسیون رو نپذیرفت
✅
کنفدراسیون فوتبال آسیا برای بررسی پرونده یاسر آسانی، این بار در نامه دوم مدارک و مستندات بیشتری از فدراسیون و استقلال خواسته و تأکید کرده فوراً ارسال بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140982" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140981" target="_blank">📅 14:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
🚨
فووووووووری
✔️
ای اف سی در نامه ای به فدراسیون گفته پرونده فسخ یاسر آسانی مشکوکه و جزییات دقیق خواسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140980" target="_blank">📅 14:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140979" target="_blank">📅 14:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140978" target="_blank">📅 14:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
والیبال به میرزایی رسید!
🔴
با حکم احد میرزایی؛ رضا صفایی سرمربی تیم والیبال پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140977" target="_blank">📅 14:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
سعید دقیقی در لیست نقل و انتقالاتی خود برای نیم فصل خواهان جذب سه‌ بازیکن از پرسپولیس شده است
🔴
حسین ابرقویی نژاد
🔴
یاسین سلمانی
🔴
محمد حسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140976" target="_blank">📅 14:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140975">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4NIz8aknghMPAxnP3F_PVixpZ4O0kaJpUwowUqPOqUs7FlUHgUaZZHDHl7I9MoFlO-IAy3BeNOEVJflc9uBCQXxo3mFEOFjmNUI4t7dFjZMteDXpA6lhS_DZUPEl0AzV-W1YkpqbCE-90y2wQZqAEsEhgz3DF9YhmELne4Pbw4QPOG85q9zpZ2xT6YPfgkMzLKXizSyst3A2UdpjoXzqmcYL-LdlNzyrdgOpoeUcXyJWeEdl8rHxin4a-6SFZ4J3znRUFtq6qxuf-iTXZiMVtb8Han1SsChW9bSqJ_hGC3Y0zhgWo9sFU9vN2wDg0V5O-C8plKb0eRWr5UtaJ5Dhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Italy -
❤️
Turkiye
⏰
Tonight 22:15
🏟
Stadio Renato Dall'Ara
⚽️
ایتالیا در ۳ بازی اخیر ۴ گل به ترکیه زده و در ۶ بازی خانگی اخیرش ۴ برد با کلین‌شیت داشته؛ ترکیه هم در ۳ بازی لیگ ملت‌ها فقط ۱ گل زده است. باتوجه به برتری ۴-۱ بازی رفت و برتری تاریخی ایتالیا (بدون شکست در ۱۵ تقابل)، کفه آماری همچنان کاملاً به سمت آتزوری است. احتمال می‌رود ایتالیا کنترل بازی و مالکیت بیشتر، ترکیه خطرناک در انتقال‌ها باشند و باتوجه به‌فرم دوتیم برد ایتالیا با اختلاف کم محتمل هست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140975" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
✅
#فووووووووری از تسنیم
🔻
جلسه کمیته استیناف برای شکایت پرسپولیس از آسانی امروز برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140974" target="_blank">📅 12:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140973">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac-_bipPdgXGibn3GICMt1Nzb3_I83LsWuZEKLBr9NUxWu1OufQTzXrpnlb70O42QXoJCtchZckmcPTWG7qMw6GBqAlZlTGyiLJzYU1YsXxB7B3IHFdbZ71fgw4ai4gJQNAbbtfRQvpy_ySjh4zngB5ZZg7esjL5zaysi96PeFryZvyI1aG90BtkOJeJshNSmPWzy0JmouOlqbf-7wJbvzzphU8ZLUcl2Lbpwp4VEFUGhTfRkrHVAmZJCTKUBfkzFHFpKxODEgZnpP4gfMheAoc-Utcm1xj29OiR6OethJzww-7t_OCIg8otUhKWQB57WP4yKcGo13FyWrwmnHL7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مهدی تارتار قصد داره از پویا اسمی مدافع ۱۷ ساله‌ی پرسپولیس در بازی‌های بعدی استفاده کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140973" target="_blank">📅 10:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9L54Qnzr4Wo2v0-Zuu8YoFsvClm4OKX2io9OUMCgPXqDHA36Zh1icivrC5l7_1ll9p1NzbmpksxLOR72-wyJUaK-maJdH002ExIXAfZ_MxwngwGpXTNjaq3sOLMLVKu-cB05ysGvu_Ka2XV0aASz6g5cLDXv0CRyjmP7V-fyKC-YTmBbst7N2pk9Dq8ZQDLcjj7utlaeGvLKxZLnAMVrv-ynFgomfxSzdkwH8d9Q32yVKT1LTgqWSZImSVs2cxVzQgpm6IYjygnDrlp0UmZMJB9RgoX30uLU3374XTyBfIoMoLxfHUoAj7_W1gfDgV-j2ABQAh7RNCGlyweHx9QTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووری
‼️
🤩
با اعلام خبرگزاری برنا
بازیکنی که مدنظر پرسپولیس بود
شرزود آسانوف ازبک بود که بین
دوراهی تراکتورسازی و استقلال قرار گرفته !!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140972" target="_blank">📅 10:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
عادل فردوسی‌پور: نیوزیلند جزو سه تیم ضعیف جام جهانی است. اما برای نتیجه نگرفتن احتمالی، برخی بهانه‌ تراشی می‌کنند. برو بجنگ بعد درباره ویزا حرف بزن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140971" target="_blank">📅 10:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140970">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
✅
✅
#فووووووووری از تسنیم
🔻
جلسه کمیته استیناف برای شکایت پرسپولیس از آسانی امروز برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140970" target="_blank">📅 10:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140969">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🤩
حدادی: برای آسانی مدارکی داریم که هیچ باشگاهی نداره؛ فدراسیون هم باید استعلام فیفا رو منتشر کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140969" target="_blank">📅 10:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140968">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
✅
تاجرنیا: بیرانوند دوست دارد حضور در استقلال را تجربه کند.
😀
به صورت جدی درباره بیرانوند صحبتی نداشتیم اما به ما هم پیامهایی رسیده است. اما الان فرعباسی و خلیفه را داریم بنابراین بحث بیرانوند یک مقدار این موضوع از ما دور است.‌ در هر صورت او هم شایسته است…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140968" target="_blank">📅 10:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZPbQx_cvJhBesP5Zp_kjRieMYX92r8bRGXLPzA-ApZZr0nrMvlUQ9Muck2SHrl7oSkUq-6RI_xKrPPt7Si6JMnuJl7Gy0j7aRiXq2g2r-dsKgzYlqn_Q9WOnL9JoZDoUcM6bVzmg0MTn56exd-WyCF1jd7p7M9NtPf3trOGsrkLXhHzij2ydJpP6tawwgfNOjMplldcLQMjHAtac_Od88_rIdRHwF9CYxnLH6VuxsTYBoryceIAz66tmCHzyNHGB7gJX55QlJHwdz9-ZuIsupW1m3Utef2wnszQcMfuwf61ZOjDEO7SbybbprY0LD0gxB3bhGyf1X5j7QI1jpXwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شایعاتی از نهایی شدن انتقال فرهان جعفری به پرسپولیس به گوش می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140967" target="_blank">📅 10:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140966">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭕️
⭕️
باشگاه پرسپولیس با خرید امتیاز باشگاه پادیاب خلخال صاحب تیم «ب» شد.
🆕
🆕
🆕
عصر امروز با حضور مدیرعامل و مالک باشگاه پادیاب خلخال در باشگاه پرسپولیس، امتیاز این تیم که امسال در لیگ دسته دوم حضور داشته به باشگاه پرسپولیس واگذار شد.
🔜
🔜
راه‌اندازی تیم «ب» یکی…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/140966" target="_blank">📅 10:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140965">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
مهدی ترابی در بیمارستان‌ آتیه تهران تحت عمل جراحی رباط صلیبی قرار گرفت و زانویش را به تیغ جراحان سپرد و شش ماه از میادین دور است.    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140965" target="_blank">📅 08:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140964">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140964" target="_blank">📅 08:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140963">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8Uy2oLcnIvIKVpKxQw8qdd35r-Irs0xqh9RU_fLIV1wAFmlfTBl2KkIErrPVDbV_AqdTF-pb6CVxdhDKR5xCKZX4NAydNBZlKZJN9b1wpGEi7no3tqFcaDsCToXWD9Z94Wo37XiTBRbIUcbZpJLsjbqUHRz4iHxvZwNftrJXe42xKzD4DEPNZ5FUFhYt20EsRD_kEw4xfhoRF5x56Y7yU8xtss49oKjTd5X1OObX8vZ6BXiKtTnhTb_QbNd0HYcCqvKLPtbmOycK3dOO7te_-_rcMcvt7-GBloZozD48b__RzQyq7-LD8pUG9kns3nULwVS8k3zvgAnV_DhpSwHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140963" target="_blank">📅 08:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140962">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ8_7hIJq6CCjG-a-svmcYoLLvaaka5Qij1bcklGtto8xjPG6htIsM4hjSbRuHJeYbNyNDUbrDeS_vrzpzejqo4TlZ23elbiNlXwNGobDe2vq7gVoYtjVeG6s2TXyaikXjcnC8Sq3fUAv-9BFHod8fOVoDcJCQlGMKGd0RRXelk7a8ncnFl5wEJ0n6CDXK1OoYjV-MakZOWxlMr7z-vxfTRBEGyv1_ZUhaJbOKyeLb9lNjnfpT60XzS8c4dxOzFJOq4fIy0JaeIeIoy5QxdKABdOb97Sav2DvPK7KsnlUm5yrYd9EYrr1VKYssXHfBOW8gABw5_pLzXumO41rVwJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
France
🆚
❤️
Belgium
⏰
Monday 22:15
🏟
Stade de France
🇪🇺
فرانسه از نظر کیفیت هجومی و میانگین موقعیت‌های خلق‌شده برتری محسوسی دارد و احتمالاً حجم بیشتری از حملات را در اختیار خواهد داشت. بلژیک در انتقال‌های سریع خطرناک است، اما مقابل فشار و مالکیت بالای فرانسه احتمالاً فرصت‌های کمتری برای تهدید دروازه پیدا می‌کند.
✅
برآورد آماری: برد فرانسه ۵۸٪ | مساوی ۲۴٪ | برد بلژیک ۱۸٪ | بالای ۲.۵ گل ۵۷٪
همچنین در غیاب دی‌بروینه و تیلمانس احتمال می‌رود خروس‌ها پیروز میدان باشند.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140962" target="_blank">📅 01:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140961">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">💢
💢
مدیران پرسپولیس به تاج اعلام کردن اگه استقلال قهرمان لیگ اعلام بشه از لیگ برتر انصراف میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140961" target="_blank">📅 00:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140960">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
حدادی : نمیتونم قرارداد محمودی رو اضافه کنم چون باید به سازمان بازرسی جواب بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140960" target="_blank">📅 00:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140959">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
فوووووری
🔄
🔄
حدادی: تا آخر همین ماه یه جلسه مهم برای بیرانوند تو فیفا به صورت ویدیو کنفرانس انجام میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140959" target="_blank">📅 23:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140958">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpZyBKAES8ai3l8Yr0VTn5hT68CTyoN8fsAKo-vuGoT77WgqNnvqtuVTBItJ7Zsif6rmzJ7Vj1KzL_YYKt6Vh_442hd97fn2PZcJC2MWrrHKTGnV71l8tyBhEscTkBvs9kV0-v_Dy9JMGuxUA90mZv55d9CJQVmASWytOKqLomGf9zD26HLXgbopbrfMY-a0_XQjfKrXWIwA_td48MPkb98Rl-FcfSXU4b7Fn6ra2Wvb0FrZSrtwqdH4pv2RsdKzx7SNHcY65mlyemR3DZp1_pY3e0oUGR3dBbrl5EPc3aUbOLk-T3dMHrbNwFurUTlKr4DVVrWLBQT7RRJGr_YkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚪️
برترین بازیکنان لیگ برتر تا این لحظه از نظر متریکا
1⃣
⚽️
🔻
علی علیپور 7.7
2⃣
⚽️
🔻
سعادت حردانی 7.49
3⃣
⚽️
🔻
اسماعیل قلی‌زاده 7.49
4⃣
⚽️
🔻
تیبور هلیوبویچ 7.48
5⃣
⚽️
🔻
یاسر آسانی 7.46
6⃣
⚽️
🔻
محمدمهدی محبی 7.45
7⃣
⚽️
🔻
عباس کبیریزی 7.44
8⃣
⚽️
🔻
امیرحسین حسین‌زاده 7.39
9⃣
⚽️
🔻
مجید عیدی 7.37
0⃣
1⃣
⚽️
🔻
امیرمحمد رزاق‌نیا 7.37
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140958" target="_blank">📅 23:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140957">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140957" target="_blank">📅 22:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140956">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
❌
خبرنگار الجزیره در تهران: به نظر می‌رسد که همه طرف‌ها در حالت آماده‌باش کامل هستند و منتظر هرگونه تحول نظامی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140956" target="_blank">📅 22:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140955">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
قرارگاه خاتم‌الانبیا: براساس اطلاعاتی که دریافت کردیم، آمریکا قصد دارد دوباره به ایران حمله کند. اگر حمله کند، پاسخ دردناکی می‌دهیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140955" target="_blank">📅 22:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140954">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
حدادی: قرارداد علی علیپور با پرسپولیس تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140954" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140953">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
غیبت عالیشاه برابر پرسپولیس/ ستاره سابق سرخ‌ها کجا بود؟
❌
امید عالیشاه در دیدار دوستانه گل‌گهر و پرسپولیس نه در ترکیب تیمش قرار گرفت و نه روی نیمکت نشست.
❌
❌
گویا عالیشاه در ورزشگاه حضور داشته و به دلیل مصدومیت جزئی در رختکن در حال گرفتن ماساژ بوده است. این…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140953" target="_blank">📅 22:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140952">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
حدادی : قرارداد همایی فر ۱/۶۰۰ دو سال دیگه هم قرارداد داره فردا قرارداد هرکسو زیاد کنیم باید بریم صدتا نهاد جواب بدیم ، اضافه هم نکنیم بازیکن انگیزه ش از بین میره و راحت می‌تونه فسخ کنه
☹️
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140952" target="_blank">📅 22:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140951">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎙
🤩
پیمان حدادی: به درستی قهرمان لیگ سال پیش اعلام نشد؛  امسال ۲ همت درآمد خواهیم داشت. خیلی از باشگاه‌ها پول نداشتند. پارسال ۵۶۰ میلیارد درآمد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140951" target="_blank">📅 21:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140950">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👀
❓
چرا خداداد عزیزی منتفی شد؟
🤩
پیمان حدادی: سیاست پرسپولیس و تراکتور فرق دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140950" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140949">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🤩
🎙
با اعلام حدادی ساخت ورزشگاه به خاطر نبود ثبات اقتصادی و امنیتی فعلا قابل ساخت نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140949" target="_blank">📅 21:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140948">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎙
🤩
حدادی: یا فوتبال یا یه کار دیگه! بازیکنای پرسپولیس باید حواسشون به فوتبال باشه. شکاری ۹۰ میلیارد از پولش گذشت و آقاسی با استقلال ۶۰٪ بیشتر گرفت. جام حذفی رو هم با تیم‌های حاضر برگزار کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140948" target="_blank">📅 21:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140947">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
قرار داد 27 بازیکنان ایرانی تیم 1همت هستش.
🔘
اسکوچیچ برای پرسپولیس بالای یک همت هزینه داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/140947" target="_blank">📅 21:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140946">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🤩
حدادی : حتی من لیست تابستونی فصل آینده رو هم دارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140946" target="_blank">📅 21:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🤩
حدادی: با همه مدیران باشگاها رفیقم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140944" target="_blank">📅 21:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140943">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🤩
حدادی: برای آسانی مدارکی داریم که هیچ باشگاهی نداره؛ فدراسیون هم باید استعلام فیفا رو منتشر کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140943" target="_blank">📅 21:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140942">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">▫️
🤩
حدادی: قرارداد علی علیپور با پرسپولیس تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140942" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140941">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🤩
حدادی : هرکس نمیتونه توی  جام حذفی شرکت کنه انصراف بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140941" target="_blank">📅 21:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140940">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🤩
حدادی : اون ۱۰۰ هزار دلار که بخاطر آقاسی دادیم بخاطر پیش پرداخت یک بازیکن بود که می‌خواستیم حسن نیت خودمون رو نشون بدیم و با اخذ رسید اون پولو دادیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140940" target="_blank">📅 21:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at1ptPcfx2K_qzaHKgm9ftFkGiaxP1PXEp9MT4kXhF4oGLRDxyCGk_PCqxGH7NcH3RSIWzXJ52vkXiOW6mVntDyz9zCCu_EWKZl6BJaCKn9tt58k5ulE_5pyADD47exws6AIbdS5ES5yrPwyDO8RIvthKHv3KZU5ys_l_ZVCzDYCMVx50iS44Zyarv92pTZKoUqUpAC4ubO1mYdni2ZFXt9sAq6qVzpuyIIAC2e5if-R2v-ITXWuUo4KkNZdcNO0CbkZssvM1wu2Wbo2uaEWZFGC78clhd1Z717KdlucvaIionusSyi0KGXYOGkrknwXKXg6N78saKzF22ErPSh2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
Portugal -
❤️
Norway
⏰
Tonight 22:15
🏟
Estádio Do Dragão
🇪🇺
پرتغال در ۳ بازی این گروه ۷ گل زده و با ۹ امتیاز صدرنشینه؛ نروژ ۵ گل زده و ۶ گل هم دریافت کرده، ضمن اینکه پرتغال بازی رفت را ۲-۱ برده است. از نظر xG، نروژ با وجود کیفیت هجومی هالند خطرناکه؛ اما مدل‌های آماری همچنان پرتغال را شانس اول می‌دانند: برد پرتغال ۵۵.۹٪، مساوی ۲۰.۷٪، برد نروژ ۲۳.۵٪. می‌باشد. احتمال بازی گل‌دار و نزدیک زیاد هست و همچنین احتمال ‌می‌رود هردوتیم به گل برسند.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/140939" target="_blank">📅 20:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
فووووووووری از حدادی : قرارداد امیر حسین محمودی 3 میلیارد و 200 میلیونه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140938" target="_blank">📅 20:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140937">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
حدادی : نمیتونم قرارداد محمودی رو اضافه کنم چون باید به سازمان بازرسی جواب بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140937" target="_blank">📅 20:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140936">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
فووووووووری از حدادی : تصمیم گرفته بودیم اورونوف و تمدید کنیم و بعد جام جهانی بفروشیم ولی نشد
🙁
🙁
🙁
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140936" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140935">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
فوووووری
🔄
🔄
حدادی: تا آخر همین ماه یه جلسه مهم برای بیرانوند تو فیفا به صورت ویدیو کنفرانس انجام میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140935" target="_blank">📅 20:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140934">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
فووووووووری از حدادی : تصمیم گرفته بودیم اورونوف و تمدید کنیم و بعد جام جهانی بفروشیم ولی نشد
🙁
🙁
🙁
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140934" target="_blank">📅 20:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140933">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140933" target="_blank">📅 20:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140932">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140932" target="_blank">📅 20:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140931">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
قرار داد 27 بازیکنان ایرانی تیم 1همت هستش.
🔘
اسکوچیچ برای پرسپولیس بالای یک همت هزینه داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140931" target="_blank">📅 20:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140930">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
حدادی : اجاره شهرقدس هر بازی ۱/۲۰۰
🫪
🫪
🫪
✅
بازی های میزبان ۴ میلیارد هزینه میکنیم مهمان ۵ میلیارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140930" target="_blank">📅 20:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140929">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔻
🎙
⚽
حدادی، مدیرعامل باشگاه پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
⚪️
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت، ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140929" target="_blank">📅 20:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140928">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=jdkj3kdfp1oTqcjGHHSPvhVxIiuoa1DF9yL_tezxtWjP0vuLesUB0QMz93Mp6h75yCDLQ7IqyOBro_7NQ6dwBXqYT7rSXWX_dXVcxJC35_Rf6dyRAIsveZhq0Jn-MNatxmXequZ0XjuU2XeWgFDuQjdu9jKyjI4--F2mChPq2Sw4MWmWQsLHgAPdZDG4swLFFgSaMJ-UJ56uBzLkAKZn42reMs94tP07c4Hyt1dzqM-MOuIrz9LI1r8nvh2IGMOZpktxzk6x8AkBYrvmst5MgUtKhF_8uTTg2a4zI6hVmrMCd_YA6tZN9aiEDxaig6xYikNIU67qGVtcUWUeBq2GJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=jdkj3kdfp1oTqcjGHHSPvhVxIiuoa1DF9yL_tezxtWjP0vuLesUB0QMz93Mp6h75yCDLQ7IqyOBro_7NQ6dwBXqYT7rSXWX_dXVcxJC35_Rf6dyRAIsveZhq0Jn-MNatxmXequZ0XjuU2XeWgFDuQjdu9jKyjI4--F2mChPq2Sw4MWmWQsLHgAPdZDG4swLFFgSaMJ-UJ56uBzLkAKZn42reMs94tP07c4Hyt1dzqM-MOuIrz9LI1r8nvh2IGMOZpktxzk6x8AkBYrvmst5MgUtKhF_8uTTg2a4zI6hVmrMCd_YA6tZN9aiEDxaig6xYikNIU67qGVtcUWUeBq2GJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🎙
⚽
حدادی، مدیرعامل باشگاه پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
⚪️
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت، ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140928" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140927">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: ما شفاف هستیم و هیچ مشکلی نداریم نگرانی بابت لو رفتن قرارداد های پرسپولیس هم ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140927" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140926">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭕️
⭕️
باشگاه پرسپولیس با خرید امتیاز باشگاه پادیاب خلخال صاحب تیم «ب» شد.
🆕
🆕
🆕
عصر امروز با حضور مدیرعامل و مالک باشگاه پادیاب خلخال در باشگاه پرسپولیس، امتیاز این تیم که امسال در لیگ دسته دوم حضور داشته به باشگاه پرسپولیس واگذار شد.
🔜
🔜
راه‌اندازی تیم «ب» یکی…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140926" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140925">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
❌
امشب پیمان حدادی مدیرعامل پرسپولیس ساعت ۲۰:۰۰ در لایو ورزش سه حاضر خواهد شد و به سوالات هواداران پاسخ خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/140925" target="_blank">📅 20:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140924">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✖️
✖️
شنیده میشود که رای کمیته استیناف نیز در پرونده آسانی تایید رای کمیته انضباطی بوده و پرسپولیس موفق به محکوم شدن این بازیکن نبوده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ﻿</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140924" target="_blank">📅 19:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140923">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
❌
امشب پیمان حدادی مدیرعامل پرسپولیس ساعت ۲۰:۰۰ در لایو ورزش سه حاضر خواهد شد و به سوالات هواداران پاسخ خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140923" target="_blank">📅 19:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140922">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
اوستون اورونوف در ادامه‌ی رقابت‌ها نقش موثرتری در ترکیب پرسپولیس خواهد داشت/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140922" target="_blank">📅 18:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140921">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
⭕️
۶ بازی آینده پرسپولیس در لیگ برتر فرصت مناسبیه برای اوج گرفتن و صدرنشینی در لیگ برتر
✅
✅
✅
ما ۳ بازی خانگی مقابل صنعت نفت ، فولاد و فجرسپاسی داریم و سه بازی خارج از خونه مقابل خیبر و مس شهربابک و نساجی و با توجه به آمادگی و اسکواد خوبی که داریم باید به…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140921" target="_blank">📅 18:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140920">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
پیمان حدادی: خدا را شاکریم که سومین برد متوالی تیم بانوان را شاهد بودیم. سه پیروزی ارزشمند که باعث شد در صدر جدول قرار بگیریم و در هر سه مسابقه نیز کلین‌شیت داشته باشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140920" target="_blank">📅 18:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✖️
تارتار به دنبال امتحان کردن امیرحسین محمودی در پست شماره ۱۰ است.
❌
با مصدومیت علیپور، احتمال داره محمودی از وینگر به پشت مهاجم منتقل بشه تا خلاقیت بیشتری به خط حمله پرسپولیس بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140919" target="_blank">📅 18:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
⁉️
‼️
یحیی گل محمدی به دلیل اینکه باشگاه دهوک یکماه در پرداخت دستمزد خودش و بازیکنانش تاخیر داشته اعتصاب کرده و تمرینات تیم شو تعطیل کرده:))))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140918" target="_blank">📅 18:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140917">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
مهدی تاج: سهمیه ما برای سال آینده 3+1 است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140917" target="_blank">📅 15:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140916" target="_blank">📅 15:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b62ce8f42.mp4?token=NQPrCC5It4CnvgO6WabqMuq0INZCh0_sPqRW-Keh2AW4z3GE8nsFtykbdwx7WD9xp7CmFETWgWyJUN1RULP0LniloSPB7Yl1zKCA8HY6Wkd05VZojx2Oi1cxszEG3yn_d6ETIYjm8prwvNEulkAfwXpFTYjY26x6BxwkUukmuI3L5Tf08YB4mnct09Qj9P9Wnsn1Y2jqlH8EjCZI0XfdNLBVkD0bH8EgLRdlIR21k1ER2pl5_5LuA5UoVKBrqGlspXsikM94-sNUc3I3S2fFfTptCf7GnYyugAHaj2xpNUHhRIxX1ppOMuAQJlxevZphEnK5L4SGUJJDNN9IeljnQUVHam41lLBC7L_77sPiimG_8JHYJQWvIRN39BGaJiXf_fHCEBhVc72prg2PCSbyG2MzB2sC5WOoKpExtYF2KM7SEiw0Gv9rBQtGfYdnwV6WYFi8G_73FhNqrTfncLHReYbo4R0xoz9B6xgS0P8YpNiv2dTi2e3hLqwvMZFsDPE6KWei9i1RoEUmi-XC70NsN3xBxA-6vPOSAuf3n3ASiC6R-yuktR8rHRlEfS4vIhKJiJB9-85VPlRSOBCcMjRcsFw_pg0GMzsOeDeLSXbQDvwRrsQVnlnEgtZurRwZKWvOCo9zwFq2Q8jqhTEHMgGEEkd8zSS4pezkOYon14J30KU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b62ce8f42.mp4?token=NQPrCC5It4CnvgO6WabqMuq0INZCh0_sPqRW-Keh2AW4z3GE8nsFtykbdwx7WD9xp7CmFETWgWyJUN1RULP0LniloSPB7Yl1zKCA8HY6Wkd05VZojx2Oi1cxszEG3yn_d6ETIYjm8prwvNEulkAfwXpFTYjY26x6BxwkUukmuI3L5Tf08YB4mnct09Qj9P9Wnsn1Y2jqlH8EjCZI0XfdNLBVkD0bH8EgLRdlIR21k1ER2pl5_5LuA5UoVKBrqGlspXsikM94-sNUc3I3S2fFfTptCf7GnYyugAHaj2xpNUHhRIxX1ppOMuAQJlxevZphEnK5L4SGUJJDNN9IeljnQUVHam41lLBC7L_77sPiimG_8JHYJQWvIRN39BGaJiXf_fHCEBhVc72prg2PCSbyG2MzB2sC5WOoKpExtYF2KM7SEiw0Gv9rBQtGfYdnwV6WYFi8G_73FhNqrTfncLHReYbo4R0xoz9B6xgS0P8YpNiv2dTi2e3hLqwvMZFsDPE6KWei9i1RoEUmi-XC70NsN3xBxA-6vPOSAuf3n3ASiC6R-yuktR8rHRlEfS4vIhKJiJB9-85VPlRSOBCcMjRcsFw_pg0GMzsOeDeLSXbQDvwRrsQVnlnEgtZurRwZKWvOCo9zwFq2Q8jqhTEHMgGEEkd8zSS4pezkOYon14J30KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تاج: سهمیه ما برای سال آینده 3+1 است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140915" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140914">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇵🇹
نشریه رکورد پرتغال : محمدجواد حسین نژاد در آستانه انتقال به ریو آوه قرار دارد
💵
مبلغ انتقال : 1/4 میلیون یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140914" target="_blank">📅 15:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140913">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
تاج: آزادی باید مسقف بشه؛ شرط AFC!
❌
❌
حالا سؤال اینه؛ سقف‌زدن آزادی چند سال زمان می‌بره؟ ۲، ۳ یا ۴ سال؟ وعده آذرماه هم که ظاهراً منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140913" target="_blank">📅 13:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140912">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
دهقانی ناظر AFC در امور استانداردسازی استادیوم‌ها
✅
باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140912" target="_blank">📅 13:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140911">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db93cfbe3.mp4?token=D9NCBfE4OhMF-RRHaXxq-nO4gJDFpkXSrc8cgJyuM41HeyDfBeHl7o_xxp7M_ZOvwQg5KQuTcTiIsJPpBTOMbQN7Rjvz2mRmkKSUajrF9zeXn40GvXruZEhEMr5vuUMGgowvRfmP6nDVzxa8orT0SjDy6YqG2oY0-INZDenweRIVck5Sz3zYNZ2-LmkZf6sbBXC3kxf6UC5WlT4A3v8mczSSA-w7-ItzY1Ocijm77GeSYZDhaXeffd9L_9w9XBlC28FK3xSF6lmCpTk2UyoEkHljGy4luaaA0AMbmspHAnEWDEqD9CUvq9zp16MrAR3sE-h5tPOn8tK6xt28tfThOJyIN4rBORteJMm3kfRiO6a0s8_fzbkr8PUcAlI7rO_McfHP4QrN08gu9-xKXDlMLYEJE9QubsyGobKHW5oY57cTUknZwgfVXHuWfQl9d5EAXaxFdty7fBtLAHRWgcxkNqiGyS_LJsQYBewFkjSfntT9Y8OJDirNXswvjv-vpP1btvAcf-DuRqjTYLEAhsNGRbWAHXLkQhLMBy3UZsMvzyD8fT9XFl2o18EXvD052oodeEWSAvZpBHpDlhz6hW_T335C6EwIDL0LIqzF1i_nbzSVuphMEXFiyHfTGE5lKb5chrcC13Kq5oOHbVigiiuh6eourk6Xt-CCNo4k5PhnYy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db93cfbe3.mp4?token=D9NCBfE4OhMF-RRHaXxq-nO4gJDFpkXSrc8cgJyuM41HeyDfBeHl7o_xxp7M_ZOvwQg5KQuTcTiIsJPpBTOMbQN7Rjvz2mRmkKSUajrF9zeXn40GvXruZEhEMr5vuUMGgowvRfmP6nDVzxa8orT0SjDy6YqG2oY0-INZDenweRIVck5Sz3zYNZ2-LmkZf6sbBXC3kxf6UC5WlT4A3v8mczSSA-w7-ItzY1Ocijm77GeSYZDhaXeffd9L_9w9XBlC28FK3xSF6lmCpTk2UyoEkHljGy4luaaA0AMbmspHAnEWDEqD9CUvq9zp16MrAR3sE-h5tPOn8tK6xt28tfThOJyIN4rBORteJMm3kfRiO6a0s8_fzbkr8PUcAlI7rO_McfHP4QrN08gu9-xKXDlMLYEJE9QubsyGobKHW5oY57cTUknZwgfVXHuWfQl9d5EAXaxFdty7fBtLAHRWgcxkNqiGyS_LJsQYBewFkjSfntT9Y8OJDirNXswvjv-vpP1btvAcf-DuRqjTYLEAhsNGRbWAHXLkQhLMBy3UZsMvzyD8fT9XFl2o18EXvD052oodeEWSAvZpBHpDlhz6hW_T335C6EwIDL0LIqzF1i_nbzSVuphMEXFiyHfTGE5lKb5chrcC13Kq5oOHbVigiiuh6eourk6Xt-CCNo4k5PhnYy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دهقانی ناظر AFC در امور استانداردسازی استادیوم‌ها
✅
باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140911" target="_blank">📅 13:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140910">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv-oY_ksk1_--6YBgfRD7FeyuxDbSlRk3fW0fASFhhl069PPar7WZ02-V0YdJQS81IDwGwaky-dlaG2qHZ3OOJsv56OtxfePOR0yLBaG6IL2ncVEY_A-H9fedBID7pt-XzbZI03Y6ZjsKi6wr9rlWMytmeptF_JJgip45ZnI0b4-mBwK5nOCYUNt7TTuBt-O8YWLI6NYrDtXjEzHnuH-KrYCpPSZig4q6zK0vtWDdODXdOo8GtO_LZLsAWNykhBHmZeQSZ-Z4AxMm3ll1zxGdqjAadNpU5l34a6lS0zvzi6wOYGffdepo4tNXXBlwFZKTGtGZiuGjR9_IgxynYIFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد سلسائو با وایکینگ‌ها؛ پرتغال در برابر نروژ، یک شب پر از هیجان!
🔥
⚡️
[
پرتغال
🇵🇹
🆚
🇳🇴
نروژ
]
⚽️
پرتغال با تکیه بر مالکیت توپ و کیفیت بالای خط حمله، معمولاً مقابل تیم‌های فیزیکی هم موقعیت‌های زیادی خلق می‌کند. نروژ اما با قدرت درگیری، انتقال سریع و تهدید دائمی در یک‌سوم هجومی می‌تواند بازی را برای سلسائو سخت کند. سناریوی محتمل، بازی نزدیک در نیمه اول و افزایش موقعیت‌ها در ادامه است؛ گل در هر دو نیمه سناریوی جذابی به نظر می‌رسد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140910" target="_blank">📅 13:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140909">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
تارتار هنوز به یاسین سلمانی امیدواره
🔻
مهدی تارتار این روزها تمرینات ویژه‌ای برای یاسین سلمانی در نظر گرفته و قصد دارد این بازیکن را دوباره به روزهای خوبش برگرداند
🔻
گفته می‌شود تارتار به اطرافیانش گفته اگر تا پایان نیم‌فصل اول نتواند سلمانی را به شرایط…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140909" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140908">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo6LKBURXBBctOf7glmvjOg38STgDZON0YrZsxK6-y87QQRDiNmL4WPMp77LlkzE3XvnOFDgugAueoPrwUybdMj-90exfXBcqojcmW1a9m25jnNypOegybpn2rk5yDRaBVlrj6-RG-GFs9bhk7lH1FlAVkXA8WNs23QbE2ZR-easutM23tYD3ADQQ-wyjumzVCWabjXRH8sf0zF5V9CuszeoH-oEEAAgVaICCHXvrqos56fxWmUZXH-MZvbj8J8tSGkZBGzepu-FKJ3YIKq2VZ7m2L-AtTKWbw9__PzrKhR1Y0e6M8a8asq3qB9oTJvjGxKL7Bqp6f0C9gsuisu0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
باشگاه پرسپولیس طی روزهای اخیر درگیر تمدید قرارداد سه بازیکن مهم خود یعنی نیازمند، اورونوف و کنعانی‌زادگان است که تاکنون موفق به توافق با دو نفر از آنها شده است که اون نفر باقی مانده اورونوفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140908" target="_blank">📅 13:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140907">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⭕️
❌
❌
❌
❌
ادعای برگ ریزون یه خبرنگار ورزشی: یه زن اعتراف کرده که باهمخوابی باچند داور برخی اتفاقات فوتبال ایران را باآنها هماهنگ کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140907" target="_blank">📅 10:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140906">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
حمید ابراهیمی خبرنگار ورزش سه: یه معاوضه دیگه بین پرسپولیس و گل گهر شکل گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140906" target="_blank">📅 10:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140905">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSNxExayEymbmvofxvGyF7oC5ceMDBm-Ks9l13cYb8cZllAUWWWssBDlhts0p6x_FoWTHWJRXEKHhUO8K_67FFLOuSK7Sn5Yj6MlZGU-5-g-aTKmN0D33XwhEUUE__NcQjO9fRK8LcaRwqLVQp25bUr4jT-M1cSIBCSru_jO2i0h4lxUfEJmzKdTbwgKqq4Ggw2zMW4P8TStCCrKGBsdIUWGmmYoLXAQT46LQzVf8dqJYIFwiQSQ_WgbIkjvjGjgulVIpUI_AAgJIKeARP88dyw5aIjQCwk9ZbvZdTdvTlvayAWmSmk4s9CQ8GacfDMr-UTLSVD-_XpbaceNaLVq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
بازی دوستانه تیم ملی که قرار بود در مقابل تیم‌های گینه استوایی یا گینه بیسائو برگزار شود به دلیل محدودیت پروازی و غیبت بازیکنان حریف لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140905" target="_blank">📅 10:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140904">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✖️
✖️
پرسپولیس امروز استراحت داره  و از دوشنبه تمریناتش شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140904" target="_blank">📅 10:33 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
