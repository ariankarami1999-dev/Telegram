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
<img src="https://cdn4.telesco.pe/file/s8k8TQdC7E1PGSvXDGszNjLKZulW6a2xpR0ZuMASembELxw1Wj6VXDNQXEguzdXDgGIQwZ1oG_AS-dkCnLsE4LSdP-Wvo3nz6s-LpYYlv2aIi7lljvK9S9vwsBFPe8ezsNxZlWNAHQTRa9DLhG-usJ6ukAtOxcIL5B0pTsvceC2VTgENuTFJUZ7ZaHhkZCJOAXw30UljmZ4A_iILcxLclvRa0_9-niUam54TF_an2Vpoj53UitWcR7CVU2HObrIQuAcpw3A2qmNDwmb-ApAp6S1xI5r4wNTHZZJ_DoGuezBwPDB5qarONtCb7P5PD_8JEUQcqJan6lkL_qpG1TOjIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-466247">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حملات موشکی یمن به تجمع نیروهای مزدور سعودی
🔹
سخنگوی نیروهای مسلح یمن: تجمع نیروهای سعودی در شرق استان الجوف پس‌از ناکامی آن‌ها در پیشروی به‌سمت مواضع نیروهای یمنی هدف قرار گرفتند؛ این تجمعات با چندین فروند موشک بالستیک و پهپاد هدف قرار گرفته‌ شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/466247" target="_blank">📅 15:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466246">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIT0C4MzG6_5odRUHKysdB64X3hbTxsxNqOCdqbhux3tzNLE9GwGyStMeuW1PGQj_l7soWubx8vHQA-gI4nXWJj2x_MmriUO3ZiEWLP7NmJumrE03Az2DJ_yYLOU_zN6NbPKSL1hvVXEF9Bcm6xoyA1vSxnByZhCq5C0DuMaBvSF8uPL6SiM29y3i_63CwA0lnWhtHmdj-MII5nsSRoDFDRl1N4T3dpo1qynegFqx1b9Fw7Dzp_namqdcdsmu6Tvm7egeaNpp53jX4eJ292NzW9p2WRlp7JpqE7SA-wp2wtq1uww9fKw0VGKkQldC1xOE5sS71ALE860ASMG-VzNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه جایگزینی تراستی‌ها آزمایش شد
🔹
بانک مرکزی تاکنون بیش‌از ۱.۵ میلیارد دلار از منابع ارزی خود را از طریق شبکهٔ بانکی روسیه منتقل کرده است؛ مسیری که طبق اطلاعات فارس ظرفیت جابه‌جایی میلیاردها دلار دیگر از منابع ایران را نیز دارد.
🔹
بیش‌از ۳ میلیارد دلار از منابع ارزی بانک مرکزی در بانک‌های روسی نگهداری می‌شود و این بانک‌ها بابت آن ۱۶ درصد سود پرداخت می‌کنند.
🔹
این ظرفیت درحالی وجود دارد که حدود ۸ میلیارد دلار ارز صادراتی در حساب‌های تراستی ۱۸ بانک باقی مانده و به‌گفتهٔ دیوان محاسبات، موجب تأخیر در ۸۵ درصد معاملات مرکز مبادله شده است.
🔹
شبکهٔ بانکی روسیه می‌تواند علاوه‌بر چین، برای تسویهٔ تجارت ایران با هند، برزیل و کشورهای آسه‌آن نیز مورد استفاده قرار گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/466246" target="_blank">📅 15:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466245">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHZ67gAjLoXXxayRAmki1yQs4rWDL08W9hMU-M9QD9tC6HTmEe9MkRBxuyPv1Ognu0I9YOGNywKB5G8oWC1fsfzU9G-4YpkfThdjQ3YT1kA1W2B53veAxSpI0-54vy7z5jf2c5ZSzQ-c2huzdxWLM_vTDnKf21lFl4OZ-omMuyp4xfQ7ydgk7M-fM9Jt89r7UOav-R-YqL_jwzAC7O2QH6e2sVSYGggNcDn5AFAOS-k05KhtSH9olBCIWhJBAqCCZos7O32Q6o9lSST2I64JgrOiwjp01d63b4oc4dRNSSoIw8BzninShBTbAD3xxGpozUzFAOPHUwhCV0DQhrfrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
در میانه سال دوم اجرای برنامه جامع راهبردی و فراتر از اهداف تعیین شده
🔰
منابع بانک مهر ایران از ۱۰۰۰ همت عبور کرد...
🔸
بانک مهر ایران به‌عنوان اصلی‌ترین متولی بانکداری قرض‌الحسنه در کشور، موفق شد با گذشت تقریباً نیمی از سال، رشد قابل توجه بیش از ۴۲ درصد را در شاخص مانده منابع تجربه کند و در باشگاه بانک‌هایی با بیش از ۱۰۰۰ همت قرار گیرد.
🔸
بانک مهر ایران به‌عنوان نخستین و بزرگ‌ترین بانک قرض‌الحسنه کشور، در دومین سال اجرای برنامه جامع راهبردی و به‌رغم ریسک‌های متعددی مانند بروز دو جنگ تحمیلی به کشور که شرایط کلان اقتصادی و فعالیت شبکه بانکی از آن متأثر شده، توانست منابع خود را به یک میلیون میلیارد تومان ارتقا دهد.
🔸
بر اساس برنامه جامع راهبردی، خطوط کسب‌وکار بانک تعیین شده و به تبع آن سبد محصولات متنوعی در اختیار مشتریان هر یک از گروه‌های خرد و اجتماعی، اصناف و کسب‌وکارها و همچنین سازمان‌ها و شرکت‌ها قرار گرفته است.
🔸
این موضوع در کنار تأمین مالی ارزان‌قیمت، سرعت بالا و فرآیند آسان پرداخت تسهیلات، ارائه خدمات متنوع بانکی و مالی به مشتریان و پایداری سامانه‌ها موجب افزایش تعداد مشتریان این بانک به بیش از ۲۴ میلیون نفر و به تبع آن رسیدن منابع به عدد ۱۰۰۰ همت شده است.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/466245" target="_blank">📅 15:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466244">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_2TtTq-3OmSJFmfrMixrR_OUsO9oGA53SmIfy7dP-QzZjv3Ho6yWBzOx3Vo-NlPvQ_G0iD4PBztaxZEJ9PGqC4yg_n4pKhfeePasAlvBaGz8ODhC1nnEcQ_FDk2jDWbVnBBjueF9A2SayaC6lozPq3mpbHtOPATtOLeGs9ASS7HFlEY_EXBu-kWoK2o0M6U8yorG_wqAOUdQXcVQdTK8RSla6-YD6YPoYhFGSktjP5EKePCMPyQ6ttjazxxC3lS2rYDtn6BzIDfTiLjnkvvFbEd0Y8YZOaXHGq4IAd83GLO1g1uVFB4B-T28KOZE7ZYqKUPvuHRFyxRvBOkP7F_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/farsna/466244" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466243">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/farsna/466243" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466242">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqiR1C8GcxOV3087YGv88Ek-bRPrTSS0bCbCGFU0mP11SG1D0pSpHWF7605ANBIovWDf6YUiPq-yeia6FqlseY7UdNB-QGFdy4B9Nr5RNJyMsX39vfrl-VU2zPNRFe0m0ta1QazD1p7Mj52tL4tmxjilmqQPod6K8wpICKlQrp6qApTDS25lKf11q-iX0KlJO-x3hz452R_6njtorF8CJnIuhKeNIrPxE8xgAU09RHIN-oXx7TtO1qE6F4F23M1nn6c4yv8hXfP2L2dFseIFkwxaEpeTJfzP-WnrBEDaML7uNKGL-fq5Hxm20vkcjMJJaU407bmHYqMrKla-px4mpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سرگیری پروازهای نجف از فرودگاه مشهد
🔹
مدیر روابط‌عمومی فرودگاه شهیدهاشمی‌نژاد: اولین پرواز در مسیر مشهد - نجف پس از اعمال محدودیت‌های دولت عراق، امروز ساعت ۱۸:۴۰ انجام می‌شود.
🔹
دومین پرواز نیز یک ساعت بعد از آن به انجام خواهد رسید و تعیین قیمت بلیت در اختیار سازمان هواپیمیی کشوری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/farsna/466242" target="_blank">📅 15:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466241">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzuXRlfCF_RPGOhcy1FyW_b44B-RKDWAWWcolO2IcrBT7sBQTlkOfjKt3HQy-mS69ogWMXRjlR_sIH-pdz2NyAiPnkL8UyRCj_8J2G5Z9oymb8IV1kbuR3tJUb4QfQ4zjAyvuvgWrIehTgtfzmv09nAIE45ItnQrrlq99rW-yGrSKD9jFZtcW8RUH6Y8_glL4ka4sxwD6qmrS2uhY8gd5Pmuei2gl_sqYfq8lanbal97QEu7ni2qgUC5kIaeXCks00RXn1_UUj-0tdeez88KTYH5ivo4aE6rL8n-1re-0suvxpn1khmIToc8s81uAclxZLMcomXcW0lEg3nZM7hQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال صهیونیست: شاید اسرائیل چند سال آینده دیگر وجود نداشته باشد
🔹
ژنرال بازنشسته ارتش اشغالگر با هشدار درباره آینده این رژیم گفت اگر مجموعه‌ای از بحران‌های داخلی، اقتصادی، امنیتی و بین‌المللی حل نشود، ممکن است اسرائیل چند سال آینده دیگر وجود نداشته باشد.
🔹
اسحاق بریک در مقاله‌ای در روزنامه «معاریو» تأکید کرد نخستین گام، خروج جامعه اسرائیل از وضعیت «انکار و سرکوب» و پذیرش واقعیت‌های موجود است. او جامعه اسرائیل را دچار شکاف‌های عمیق میان راست و چپ، مذهبی و سکولار و عرب و یهودی دانست و گفت غلبه منافع گروهی بر منافع داخلی، توان جامعه برای مقابله با چالش‌های مشترک در حوزه‌های امنیت، اقتصاد، آموزش و زیرساخت را تضعیف کرده است.
🔹
وی همچنین درباره انزوای بین‌المللی و تضعیف روابط خارجی رژیم صهیونیستی هشدار داد و گفت این رژیم طی سه سال جنگ بخش مهمی از روابط خود با جهان را از دست داده است. به گفته بریک، اسرائیل در حال از دست دادن حمایت آمریکا و کشورهای اروپایی است و ادامه این روند می‌تواند توانایی آن برای ادامه حیات را با مشکل مواجه کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/farsna/466241" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466240">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کشوری که ۱۵۰۰ برابر ایران هزینه کرد اما چهاردهم شد
🔹
قطر با صرف میلیاردها دلار برای ورزش و جذب ورزشکاران خارجی، ویترینی پرزرق‌وبرق از قدرت ورزشی ساخت، اما نگاهی به نتایج این کشور نشان می‌دهد پول، به‌تنهایی اصالت و قهرمان‌سازی نمی‌خرد.
🔹
این در شرایطی است که کمک مستقیم به تمام فدراسیون‌های ایران در سال ۱۴۰۴، فقط حدود ۱.۲ میلیون دلار برآورد شده بود.
🔹
ایران در بازی‌های آسیایی ناگویا ۲۰۲۶، ۵۲ مدال گرفت و رتبه ششم آسیا را به دست آورد؛ در مقابل، قطر با هزینهٔ ۱.۸ میلیارد دلاری برای ورزش در سال ۱۴۰۴، تنها ۱۶ مدال گرفت و چهاردهم آسیا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/466240" target="_blank">📅 15:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466239">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXuqCAKvD25F6kCIouvbi01-O3INloNGpF3xUERGhdzRErnEiGXOJdemW5v9SS1wWeTJfVwzRqvAZE9fjbBDff0eA3kXBsYEAigB_YLhaglpSV7rHsSslpgxOKtzQ6lcTlr1Y9EFEeunDS7d9MB1vs6e3CTRnJ-irVct384vPrnOzfWnJKNmGbyLWpGfGl35nPgaxc15LgAHal8-ZjsWEA46Ajn54nzsGK4eD-PKE5Gid6v6vK86RL4Ih7iypJeZFlx1IXVeVW6rJzZ_FdWxCWnTvWQTvxiAbm_7W1OJvwBqCnKsFDIIvMvf-c2CwNZFs3laBoiSgKtse6C7xIYWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل دسترسی کاربران رایگان جمنای را محدود کرد
🔹
از ۹ اکتبر (۱۷ مهر) کاربران رایگان جمنای فقط به مدل Flash-Lite دسترسی خواهند داشت و مدل‌های Flash و Pro برای آن‌‎ها حذف می‌شوند.
🔹
مدل فلش‌لایت برای پاسخ‌های سریع، کارهای روزمره و گفت‌وگوهای معمول طراحی شده، درحالی‌که مدل‌های فلش و پرو برای وظایف پیچیده‌تر و استدلال عمیق‌تر کاربرد دارند.
🔹
مشترکان AI Plus نیز دیگر به مدل Pro دسترسی نخواهند داشت اما کاربران AI Pro و Ultra همچنان به هر سه مدل دسترسی دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/466239" target="_blank">📅 15:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466238">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgyQd3I4PS_N5tKwON_V5gBakmn-9128A_fUyUVHdpgBipdamLYJgzReI7Te2nWg8Y8gQ1WTYgx2k05bM1RB0m4kh8VqTlAlEIUz1eH7h4MancF-dyfk0WEiALcgMsrsZ4nDpLM9QOo4yaGFdyKtBkr3BNhwLSaSd24_mUDiaAFP1ich3w9vOmYlf9G-t8MEL11hUEl-i1nqw6icwwTE43xDJF0xn7HvivorGniy8vhBWZZIc46BchyHodOtegDx3bCE0hxQZcjI5qLKnQYCLtUoLYiqKB3buft-9drN1Rgxr4cCjRuvyPVOele6x3rhNuhIe2Imz63d4BPjRxB9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رئیس سازمان حج و زیارت: اگر کسی از حج امسال انصراف دهد عین پولش برگشت داده می‌شود و سال آینده می‌تواند ثبت‌نام کند و اعزام شود.  @Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/466238" target="_blank">📅 15:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466237">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2f2cb823.mp4?token=Dx6AqoNgqTbEw3iOQ9IN1Ptz6ILVi1pU2qEAb1qtlB1T5aJvxR_OieEUFBpBw0eH7N1CbCzEUnG34R9wOWXPQDEE7A1ItiqHFu9skGKLlwhv-9vmQSZZHgP1bD6ZSHQ3jWD1OZewaK4f76BeFpxExBPMOfF7AriBUh3yfQxyz6050sd6rPNrCKvWUss8pLqTCrb29ylgv46YARccnpp-8b-5mYMZB_yafZiqU1tUtH5sjQ-PYnFaRGSdQR0CKHt5IDA4M_TQRFO4WRqMlTIQhRebb6Z2HcAuhACzef31BfieCGIePcPiDqAWBmUthxpuf3oQ-i-bxjnFGnnUlxBj0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2f2cb823.mp4?token=Dx6AqoNgqTbEw3iOQ9IN1Ptz6ILVi1pU2qEAb1qtlB1T5aJvxR_OieEUFBpBw0eH7N1CbCzEUnG34R9wOWXPQDEE7A1ItiqHFu9skGKLlwhv-9vmQSZZHgP1bD6ZSHQ3jWD1OZewaK4f76BeFpxExBPMOfF7AriBUh3yfQxyz6050sd6rPNrCKvWUss8pLqTCrb29ylgv46YARccnpp-8b-5mYMZB_yafZiqU1tUtH5sjQ-PYnFaRGSdQR0CKHt5IDA4M_TQRFO4WRqMlTIQhRebb6Z2HcAuhACzef31BfieCGIePcPiDqAWBmUthxpuf3oQ-i-bxjnFGnnUlxBj0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشف کارگاهی که بسته‌بندی برندهای معتبر را جعل می‌کرد
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/466237" target="_blank">📅 14:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466236">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f6940786.mp4?token=YbujUF9V6DNDbV_eggZhmYdKAd3FraaJO8q_DQRXx9mQHmnD8gkWN5VhJVOtM7d0k7VOLZAGuonx5_5rsy0Tw_D5OStJAVApOx9AOPYyBCEZ0SKgPy0GyaIoFJCkYGBgM-0_xvSiaOJLS1dr4L-fTKItNMHEX-CXLIUIcgtzitNpjgZs6ByEniM31Rzf6I0yDpTs6TpfHwUcMGnhBmLcgTGMcyVF8DJftGbOCQMiV2t1uvpHyQANN2IZsJcilxNztAZIIiyhsamJ5A1ar9zYUTL5zagC9VpqBKgD04YnWwG-S326by5laaNIRDSDILydSZgM2KR7FtnFR9FULby4Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f6940786.mp4?token=YbujUF9V6DNDbV_eggZhmYdKAd3FraaJO8q_DQRXx9mQHmnD8gkWN5VhJVOtM7d0k7VOLZAGuonx5_5rsy0Tw_D5OStJAVApOx9AOPYyBCEZ0SKgPy0GyaIoFJCkYGBgM-0_xvSiaOJLS1dr4L-fTKItNMHEX-CXLIUIcgtzitNpjgZs6ByEniM31Rzf6I0yDpTs6TpfHwUcMGnhBmLcgTGMcyVF8DJftGbOCQMiV2t1uvpHyQANN2IZsJcilxNztAZIIiyhsamJ5A1ar9zYUTL5zagC9VpqBKgD04YnWwG-S326by5laaNIRDSDILydSZgM2KR7FtnFR9FULby4Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: استان‌های شمالی و برخی استان‌های شمال‌غرب، غرب و جنوب امروز هم شاهد بارش خواهند بود.
🔹
همچنین فردا در بخش‌هایی از استان‌های گیلان، مازندران، کرمانشاه، ایلام، اصفهان، استان مرکزی و لرستان باران می‌بارد؛ موج جدیدی از بارش‌ها پس‌فردا وارد کشور می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/466236" target="_blank">📅 14:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466235">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3aa391a2.mp4?token=ETEkFy04liWeKFRbHFEssDPNvppwSi31TLFaWjBDqiseRo_S8ObREHKjTcNRyGizgy5T5uHzIE2M_CdHGat7Rk7FF1ThyRWxpGObY_fqZh-XcG9hZzb-9XabxSXzGiHegwSsrCunTI5oOiCrL9WCZPZtcLKcfLHwxhX1ATYI-5JPHkbicmEyJxvyIbe2eVmpn0oarCWBUMosN6fIKwI5WkCRRnj61MoTp8U7ldmTLUbI7-87Jeu67QB3HVYfHFUD9GsqoBKcmDCg6CQOOG9t9F6_I7DBloTTZQ0ce-WEiRI_0dy-4rsIbR_pGI5xjxPiTp010iqnKHdOeO1bXuOw11qjgEO6LjuAXo_ktn9IkiXRhAd5h47RQdtwmdrvxlCiwbw0xWTgvo6PjrioALILz1pV_QZThS_D2MslZFvxlXTmZBxAD_RE0mLdopCa5hMteFsQ4f7Qpr4lU3zrOMepp851swvtaNCAFMywWztGibtggBO-Fv3SiguvMP3eA9ho8uxMQa0iv_4WZL9CNqykD1w94f1OFRnvsz08JlTq-yEoy6DM5oLSfouObqEh2ySAROMtxTdyhxbe7HaXRMWxWmwmZkT9-u83nm9Ds-HLnU2svFiQ-STtjGoSGz_LBRYFNJ0ZPggCEyFzwdtZZi62bEuWZHvfPxltZHVGcnhyRpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3aa391a2.mp4?token=ETEkFy04liWeKFRbHFEssDPNvppwSi31TLFaWjBDqiseRo_S8ObREHKjTcNRyGizgy5T5uHzIE2M_CdHGat7Rk7FF1ThyRWxpGObY_fqZh-XcG9hZzb-9XabxSXzGiHegwSsrCunTI5oOiCrL9WCZPZtcLKcfLHwxhX1ATYI-5JPHkbicmEyJxvyIbe2eVmpn0oarCWBUMosN6fIKwI5WkCRRnj61MoTp8U7ldmTLUbI7-87Jeu67QB3HVYfHFUD9GsqoBKcmDCg6CQOOG9t9F6_I7DBloTTZQ0ce-WEiRI_0dy-4rsIbR_pGI5xjxPiTp010iqnKHdOeO1bXuOw11qjgEO6LjuAXo_ktn9IkiXRhAd5h47RQdtwmdrvxlCiwbw0xWTgvo6PjrioALILz1pV_QZThS_D2MslZFvxlXTmZBxAD_RE0mLdopCa5hMteFsQ4f7Qpr4lU3zrOMepp851swvtaNCAFMywWztGibtggBO-Fv3SiguvMP3eA9ho8uxMQa0iv_4WZL9CNqykD1w94f1OFRnvsz08JlTq-yEoy6DM5oLSfouObqEh2ySAROMtxTdyhxbe7HaXRMWxWmwmZkT9-u83nm9Ds-HLnU2svFiQ-STtjGoSGz_LBRYFNJ0ZPggCEyFzwdtZZi62bEuWZHvfPxltZHVGcnhyRpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخشش ایران در المپیاد جهانی نجوم
🔹
تیم ملی المپیاد نجوم و اخترفیزیک ایران در نوزدهمین المپیاد جهانی این رشته در ویتنام، با کسب ۵ مدال طلا در میان بیش از ۶۶ کشور و ۳۲۰ دانش‌آموز درخشید.
اسامی مدال‌آوران ایران
:
🔸
سارینا علم‌پور
🔸
محمدحسین حسینی
🔸
هیربد فودازی
🔸
حسین معصومی
🔸
ارشیا میرشمسی کاخکی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/466235" target="_blank">📅 14:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466234">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">صدای شنیده‌شده در بندرخمیر مربوط به فعالیت شرکت گچ بود
🔹
فرمانداری بندرخمیر هرمزگان: صدای انفجاری که در محدودۀ شهر بندرخمیر شنیده شد، مربوط به عملیات معمول و قانونی شرکت گچ خمیر بوده و حادثه یا شرایط غیرعادی گزارش نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/466234" target="_blank">📅 14:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466233">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5756415753.mp4?token=NsmDmx_UUY75MoVk6mhhx-bC-bFLgiW7fpPDGfReJ3wDv1lbdgC4BSvKI-O8JMh3PLKiTStXz_MEmLzNLEfdjkzmrrClNMmZNPKS1bMKkLso-Uc1x_MA7j4cl_xZ4CI35BDOgRnnwqHeOetGXrtMPBp1Wzd-tqCikpfiaLsJuPVzblUO5bZAJGQ-Z44xopYUu-gU5btYJ42PqFrKSTFlRB9wBKZhJC6pYMD6IjL1lt7NRAeSvo4cmxzvFsgcrOY3iTqGFQjgE8u0rqB7OMOcxFe8zs9pAUXMcoe66iq_YOAUv4_AiHKtBY_z454NTJ3i9xH1NgRlyrgcEu7IGJFVAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5756415753.mp4?token=NsmDmx_UUY75MoVk6mhhx-bC-bFLgiW7fpPDGfReJ3wDv1lbdgC4BSvKI-O8JMh3PLKiTStXz_MEmLzNLEfdjkzmrrClNMmZNPKS1bMKkLso-Uc1x_MA7j4cl_xZ4CI35BDOgRnnwqHeOetGXrtMPBp1Wzd-tqCikpfiaLsJuPVzblUO5bZAJGQ-Z44xopYUu-gU5btYJ42PqFrKSTFlRB9wBKZhJC6pYMD6IjL1lt7NRAeSvo4cmxzvFsgcrOY3iTqGFQjgE8u0rqB7OMOcxFe8zs9pAUXMcoe66iq_YOAUv4_AiHKtBY_z454NTJ3i9xH1NgRlyrgcEu7IGJFVAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ کابوس جمهوری‌خواهان شد
🔹
وزیر خزانه‌داری آمریکا: مردم آمریکا زیر چرخ‌های کامیون تورم له می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/466233" target="_blank">📅 14:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466232">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38fd43416c.mp4?token=Q3gTJomXlNBjmekyXf8bLnhpN7628tbwX0eaUb1CXGRiXLLmSIi-2Tx5imD3ZzUg1MVYidMvsbw5EpR-9BN6iy6hXU58DmVgnOXFtHng3BvMfdspDofhqb-jXG_r-tN0hvQKXCmyat9lg_i9anxP7jWK4O5CVgff6G0tvWSCK-W8_UiTm-cgG5R8AsqvoUz2M6lSNleyrgqSoDS0ZrrfUecAvbKUciqU7yxO4w_49dk9XjeH59GDrIOVNNaieZql7c9PiPVcS0hYW-VD_BWS0W6C_jIndIhKd3cfaHrtsDKop_MrgHM3Nh-oLGnqwl7ivb2kYCuL6goS__1yQ-wnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38fd43416c.mp4?token=Q3gTJomXlNBjmekyXf8bLnhpN7628tbwX0eaUb1CXGRiXLLmSIi-2Tx5imD3ZzUg1MVYidMvsbw5EpR-9BN6iy6hXU58DmVgnOXFtHng3BvMfdspDofhqb-jXG_r-tN0hvQKXCmyat9lg_i9anxP7jWK4O5CVgff6G0tvWSCK-W8_UiTm-cgG5R8AsqvoUz2M6lSNleyrgqSoDS0ZrrfUecAvbKUciqU7yxO4w_49dk9XjeH59GDrIOVNNaieZql7c9PiPVcS0hYW-VD_BWS0W6C_jIndIhKd3cfaHrtsDKop_MrgHM3Nh-oLGnqwl7ivb2kYCuL6goS__1yQ-wnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برجک زندان رجایی‌شهر فروریخت
🔹
در ادامۀ تخریب دیوارهای زندان رجایی‌شهر البرز، برجک این زندان نیز تخریب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/466232" target="_blank">📅 14:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466231">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88addec6bc.mp4?token=h7bpzjzEke6qT6kjrGMQJuHaYNGKkoIglnCvQ6oSve-uUQjwISHScWZPPHoYPtu6iS54sAYznS4zMYNXTRptUk0jT1s2-KFAj7haC4J86j-rXrL-Y3TXjBKHXrkO5u5kaliBQVys3nD4vbYBfIAAf-fSziUQmHe9tYSrsbode_KGmQAoU_W_QtW8qSB_nBdA64rc4RCT3bYR9RBK7YOSSnZs7c4ObfcVp6M6A8O5JdLsmJEwaBJKO7h0HMxeMCSduQdbtdjWcaopfFB7TPo9y_9VNE4g_iu5f7q74EcS1CSupcUWKsJ38rseAiMt9PBr9Fg-MYEa4deHdocc3wDb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88addec6bc.mp4?token=h7bpzjzEke6qT6kjrGMQJuHaYNGKkoIglnCvQ6oSve-uUQjwISHScWZPPHoYPtu6iS54sAYznS4zMYNXTRptUk0jT1s2-KFAj7haC4J86j-rXrL-Y3TXjBKHXrkO5u5kaliBQVys3nD4vbYBfIAAf-fSziUQmHe9tYSrsbode_KGmQAoU_W_QtW8qSB_nBdA64rc4RCT3bYR9RBK7YOSSnZs7c4ObfcVp6M6A8O5JdLsmJEwaBJKO7h0HMxeMCSduQdbtdjWcaopfFB7TPo9y_9VNE4g_iu5f7q74EcS1CSupcUWKsJ38rseAiMt9PBr9Fg-MYEa4deHdocc3wDb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
۱. آرش محمدی</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/466231" target="_blank">📅 14:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466230">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86022fba13.mp4?token=kF1BbXQ8_Pd6g_qwYKoS64LMlOvovt5SILAGo8FAviw-uLcIb36DbdSZO9uQ4EGUOYAiVfST9Zxg5djqO0gtVcJm3VvHaZrvAikGh1FWlFMEoutSkAogltKp4hKH91_YlES0_RS_6X1DjJo-rg3Dvvw2Ouncc7djsceCXzoPH85baPkq53yDnzX-By-qFYXbND7z4lGBKWG-pvoq6U__UWxZ9tpCuXttC8yN2WEZYQOdoKVE-fDr7VV6c5Oni8ZOUe1AD9-rdYZieR0Z1BH1NV1LAuIXcCNnFBajXW2y9rE5SxkIVb6soAeNVjZ-DDDKLf8vknLJgLGBSVwWslzOZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86022fba13.mp4?token=kF1BbXQ8_Pd6g_qwYKoS64LMlOvovt5SILAGo8FAviw-uLcIb36DbdSZO9uQ4EGUOYAiVfST9Zxg5djqO0gtVcJm3VvHaZrvAikGh1FWlFMEoutSkAogltKp4hKH91_YlES0_RS_6X1DjJo-rg3Dvvw2Ouncc7djsceCXzoPH85baPkq53yDnzX-By-qFYXbND7z4lGBKWG-pvoq6U__UWxZ9tpCuXttC8yN2WEZYQOdoKVE-fDr7VV6c5Oni8ZOUe1AD9-rdYZieR0Z1BH1NV1LAuIXcCNnFBajXW2y9rE5SxkIVb6soAeNVjZ-DDDKLf8vknLJgLGBSVwWslzOZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: ۳ ماهوارهٔ جدید از منظومهٔ شهید سلیمانی در دههٔ فجر رونمایی می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/466230" target="_blank">📅 14:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466229">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGlZpm1ZTH0HM-i8b4VTTLSljO4cKa3CDvqvenSVCJylX946vTO1ySkZVZWXa-5V4Nli97DpJdsEv5uKIBChZXu5Ys8kuwEm2Ju9SGoL4qZ8_wPB0RlLrCTrzfbe3NYoVqnr2f5YhEwOuAdKwgoOmNBeqkAuijdrdreQIDGcmRtsbfFzFtaTN2b-h7jlJ0nOn-tCqz--uKE3c0H294yrS3sW8GXd-ckgvQ3SJybzhQru6SuHWUuEgWzY2CGwAH-TiyoG3H_uAKwKP0-sgUIoLCTvo6h3tu1R81Tsu3BGWpiknCg3xk3FSv1ik0CpXKnFauSM14vU4rLimMf-2Sr_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش در تنگهٔ هرمز هدف قرار گرفت
🔹
به‌گزارش سازمات تجارت دریایی انگلیس، یک نفتکش در تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفته است.
🔹
ناخدای این کشتی می‌گوید که بر اثر این اصابت به موتورخانه این نفتکش آسیب وارد شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/466229" target="_blank">📅 14:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466228">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b68653419.mp4?token=OL3eib1OUheByO0p57fr6G0mHVCfEvQq_iVlk7uRsdC-374324i0j3Rmg911eb6zb-FPZKX7pkWxebEz2KKc8MbKgvDi0roc0IHsIa_vBK70MyZ5OI8RvyDONxabQ0zuHrWO6w8Yut_MUiMTwy7JglzabmAlHfBw_wGfOcxNNXwvt9vEQUQQZ8eSpA_JdisrJGVgMRHhEtv1FO_D6lkRBbpf-G9saXapqWHzSJVvzsbgyOJeQJFRuXyyQIp_E-nsaCzWHfKO9A5nMqL_bwlBp6xsQtpR7s1IIOYGfnos5lHMPh2avoZPpP-ynCO7ELUI8bmGPk9a_8SNqtXfkYUfz4OvE7hdt3WZY4OPrKm8-QiWYXs76K4x7et4biNKq8GiJa00LUUMjRWN9uJ7HitQ0NugYk_ynT2FQBuCbZzZfRZUH3cbPEhLr3hyEbpIYzXi9AGkoTwGQR7ay6Jlo0PnaKDVLJnvPhts1a-PWHKa2sgZTc9nWqXzQPWWVoGwk1Yr1mrtrJczG8INwg56JCeF10XqRae3NiOE_dUV-OxUcMv4zbwr-fy3zJfqeoMK985ArdzjsAUn4K2bkJaC3wTOr8pURJ2XSPg73KYiV7Ms79gEFkgQuHX-VW2Tw5jp7C04vMiwvVOMwWk0OcM5vgkHx1og6i_s5HIYKEJ3Sy-6Gto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b68653419.mp4?token=OL3eib1OUheByO0p57fr6G0mHVCfEvQq_iVlk7uRsdC-374324i0j3Rmg911eb6zb-FPZKX7pkWxebEz2KKc8MbKgvDi0roc0IHsIa_vBK70MyZ5OI8RvyDONxabQ0zuHrWO6w8Yut_MUiMTwy7JglzabmAlHfBw_wGfOcxNNXwvt9vEQUQQZ8eSpA_JdisrJGVgMRHhEtv1FO_D6lkRBbpf-G9saXapqWHzSJVvzsbgyOJeQJFRuXyyQIp_E-nsaCzWHfKO9A5nMqL_bwlBp6xsQtpR7s1IIOYGfnos5lHMPh2avoZPpP-ynCO7ELUI8bmGPk9a_8SNqtXfkYUfz4OvE7hdt3WZY4OPrKm8-QiWYXs76K4x7et4biNKq8GiJa00LUUMjRWN9uJ7HitQ0NugYk_ynT2FQBuCbZzZfRZUH3cbPEhLr3hyEbpIYzXi9AGkoTwGQR7ay6Jlo0PnaKDVLJnvPhts1a-PWHKa2sgZTc9nWqXzQPWWVoGwk1Yr1mrtrJczG8INwg56JCeF10XqRae3NiOE_dUV-OxUcMv4zbwr-fy3zJfqeoMK985ArdzjsAUn4K2bkJaC3wTOr8pURJ2XSPg73KYiV7Ms79gEFkgQuHX-VW2Tw5jp7C04vMiwvVOMwWk0OcM5vgkHx1og6i_s5HIYKEJ3Sy-6Gto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بلاتکلیفی ۲۳ سالهٔ زمین ۴۲ هکتاریِ قزوین که قرار بود گلخانه شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/466228" target="_blank">📅 14:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466227">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db14e940f.mp4?token=VuHEmxpjoMr7Pgd604xGDx58ZyF4i87DMmaMYVEYStFhkO7Y1ij2jgocGRhYv7SslZ6NlZd03eN2NhmNhiSYrgFXEnvk4Xx0TPZTXP4S8xFTnlHIWpZJL5lC_rRTk67QCGjhzW-EGGIeUAh8H--E1IEAzWshNttxvkLbPR8mmGVmn7Ao_S4h_PRyPLqvpLFv6NXeCOWzRJJ2l7li9l2ARP-8dxSLIZjKPIO0mwpNCHg6j1158HcItEgmeAFeLdWb7XRfxU7fyYaZoP92IxGmb9flODOAnTdXyAb_znswpfBuXijLGQsGPkIgZwL23AZSHcNeA-NngCbcnKmeYeaZYbrpCPXI-vPS5WjWATRdLma_ifzXVdyWHQNqJT7xKL-e0MeB17OhgtlJy2whDjKx7_fKUeDZsOfEBfh5Oa_G1pFDGnucWGjksaiw54yXHb1LKdr-vUUybSjhnZZpuqhKln84MawdbRhleSvQUbUmdx42BHzfS6nLc62Dcff99oTJrtRnLiGyxNIvW7Edj5Lj40CTBdqSDa4L--KHoSFoZhH3Rek2jsJ7dBYEccvSXKpzZuMXjbD3YQS4cunrIm2l2Tm0HqS4sUo_bF8618ZFKs-tifcQkdj6AdmuuqP7da5t_hnIVxC95LWD2kW_sRHhRYlm-vZInCn_xYMqx8jRCiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db14e940f.mp4?token=VuHEmxpjoMr7Pgd604xGDx58ZyF4i87DMmaMYVEYStFhkO7Y1ij2jgocGRhYv7SslZ6NlZd03eN2NhmNhiSYrgFXEnvk4Xx0TPZTXP4S8xFTnlHIWpZJL5lC_rRTk67QCGjhzW-EGGIeUAh8H--E1IEAzWshNttxvkLbPR8mmGVmn7Ao_S4h_PRyPLqvpLFv6NXeCOWzRJJ2l7li9l2ARP-8dxSLIZjKPIO0mwpNCHg6j1158HcItEgmeAFeLdWb7XRfxU7fyYaZoP92IxGmb9flODOAnTdXyAb_znswpfBuXijLGQsGPkIgZwL23AZSHcNeA-NngCbcnKmeYeaZYbrpCPXI-vPS5WjWATRdLma_ifzXVdyWHQNqJT7xKL-e0MeB17OhgtlJy2whDjKx7_fKUeDZsOfEBfh5Oa_G1pFDGnucWGjksaiw54yXHb1LKdr-vUUybSjhnZZpuqhKln84MawdbRhleSvQUbUmdx42BHzfS6nLc62Dcff99oTJrtRnLiGyxNIvW7Edj5Lj40CTBdqSDa4L--KHoSFoZhH3Rek2jsJ7dBYEccvSXKpzZuMXjbD3YQS4cunrIm2l2Tm0HqS4sUo_bF8618ZFKs-tifcQkdj6AdmuuqP7da5t_hnIVxC95LWD2kW_sRHhRYlm-vZInCn_xYMqx8jRCiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در این جنگ به این نتیجه رسیدیم که حتما باید برد موشک‌هایمان‌ را ارتقا دهیم و الان به این سمت رفته‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/466227" target="_blank">📅 13:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466226">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r50GDXim11TiI3OxnPOT3deHopxueCznwpnMDDNfh2ES_sKKIIh7sYBT7iSkDHB2btg4Erq1CmcU-Vck6SVZReEYH_i68dXqdzzXiy2Ejr80G1VT_BfEwco_LioCOktSFDrYCdIa0nAnsO0wjWTVGYujRNpDxF3BSGqXn-n4hTq0dHKMhxIWbWhgfqHfZX4pclgVmfAkXKkjl3PWi0T7EY429G3yZlliX-8nQa6Qm93SJWgF580dy2vlRoh7KBc3vDBFmiXVt0j_gqKhQatUZrpihRxlYWfepMdKIxa7pnspLyo6DRJWBqbE3-AaP1dmj7U-zYt4u-JkioTglWg_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس کمی ریزش کرد
🔹
شاخص کل بورس در پایان معاملات امروز با کاهش ۵ هزار واحدی به ۷ میلیون ۷۸۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/466226" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466225">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3g9tUHf8yNpqpvjNtf-tVQ1iWIfE899PVKekGDmPbi2uvPOtkiL2nJQUDFjLVz5P-jAR9n0EuZ4k6fKW44417TIFAd87tlu9yi8qCrQjHqIs1MJYOzxp-ih1IbI2npTlEHq-LMzt3Ue3UP7UAmbfn0A6-ZRZOrmA1ki_mnzNQPhrbfbe6NB51rEz2Oizvs0pzAM_0RjtK7ijE6gtKA87nz3erT8C6359WAt4Fm3VZ9FEZz_ekf9YREwU3zzynxjf1m5JnKAbW64jGC4afeQxWasOnxZNGzocDAGm5eNvTk4__uKCaCG_rtxzST92zGWs3dJ6i0MHMv7ZoD2dV30dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی هکرها به اطلاعات ۵۰۰ افسر اطلاعاتی عربستان
🔹
گروه «دفاع سایبری انصارالله» و گروه هکری «اویس قرنی»: به اطلاعات مرتبط با حدود ۵۰۰ نفر از کارکنان و افسران سرویس اطلاعاتی عربستان سعودی دسترسی پیدا کردیم.
🔹
برخی از این افسران طی ماه‌های گذشته با سرویس اطلاعاتی اسرائیل (موساد) و طرف‌های اماراتی همکاری داشته‌اند و رفت‌وآمدهای آنان با برخی فعالیت‌های محرمانه در منطقه مرتبط بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/466225" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466224">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ca67e9ee.mp4?token=M8DzgSHMyQFVlVa7YxKKfnsje8bGga-Svrvc3pxPTwa_2bPATOnCwC2hFWYbQfa1gGxebrhSxtr93pyTbtQ9aOlG5eq195F6taNXketClgir7--p-bcy5GDCY1bSicO7Tom0noUuPqOU17gHPd7HYPTrTaGQO2kS1UP0kj0Fyt4taK8El5BF9f3RhIEHTEpcIufaWW3-d1H1QiDToI1zPvhEUVxjbE_7YZIWHn_vnZGFoT76HH5y-z4bV2MT6TyCyU_Ua84ecsIXdXjlBxwy5PxzWnrRmpUU2k6w6b9HsJl93-pTFJpe3Cj9JKIQLVCNBgFBGTi0YDatvZ_Fl-C45w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ca67e9ee.mp4?token=M8DzgSHMyQFVlVa7YxKKfnsje8bGga-Svrvc3pxPTwa_2bPATOnCwC2hFWYbQfa1gGxebrhSxtr93pyTbtQ9aOlG5eq195F6taNXketClgir7--p-bcy5GDCY1bSicO7Tom0noUuPqOU17gHPd7HYPTrTaGQO2kS1UP0kj0Fyt4taK8El5BF9f3RhIEHTEpcIufaWW3-d1H1QiDToI1zPvhEUVxjbE_7YZIWHn_vnZGFoT76HH5y-z4bV2MT6TyCyU_Ua84ecsIXdXjlBxwy5PxzWnrRmpUU2k6w6b9HsJl93-pTFJpe3Cj9JKIQLVCNBgFBGTi0YDatvZ_Fl-C45w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بسیج اساتید: شرط التزام به ولایت فقیه را از آیین‌نامۀ جذب اساتید حذف کرده‌اند
🔹
پیشوایی: شرط التزام به ولایت فقیه، شرط مربوط به حضور در اغتشاشات و ملاحظات اخلاقی درباره اشتغال افراد دارای فساد، از آیین‌نامه جدید حذف شده است.
🔹
آیین‌نامۀ جدید هنوز به…</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/466224" target="_blank">📅 12:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466223">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
رئیس بسیج اساتید: شرط التزام به ولایت فقیه را از آیین‌نامۀ جذب اساتید حذف کرده‌اند
🔹
پیشوایی: شرط التزام به ولایت فقیه، شرط مربوط به حضور در اغتشاشات و ملاحظات اخلاقی درباره اشتغال افراد دارای فساد، از آیین‌نامه جدید حذف شده است.
🔹
آیین‌نامۀ جدید هنوز به تأیید شورای‌عالی انقلاب فرهنگی نرسیده؛ یک ویرایش در مجموعۀ وزارت علوم تهیه شده که اشکالات متعددی دارد و با بسیاری از قوانین بالادستی در تضاد است.
🔹
ما نسبت به این موضوع انتقاد داریم و معتقدیم این کار با بی‌تدبیری انجام شده و باید در اسرع وقت اصلاح شود.
@Farspolitics_
link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/466223" target="_blank">📅 12:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466222">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc678926d.mp4?token=B2ry7V37kW5YteZlGSHFK8-Fa86bVQGkgkuNG-XoGx3SdI2kY8zO7TmjB2dup5RA4D13_NTT6e2pYUq9FRVGwvpa6WX6QjITtsIOVssbw28QC1KAmHcA5pzzVo5bpdXiIwns5n70_nOfYTI3lST6Nij9KHn_b1rT7KKi--VT2tLtyIql4SPOGKsXDTk-gll4bKJcFJfJ4NKFcizmBirYaaL5sRXmcNtcZSXCMce_FHDFk468OGYiHnAy0Q35wbRwxhX3-5GMvmJWDu9bPnliQqJk3yBArKKTrqnDq633_0eMPaEXgnH44x42Md2gHRPJrmalZMn__CAk_5ySg3Yf2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc678926d.mp4?token=B2ry7V37kW5YteZlGSHFK8-Fa86bVQGkgkuNG-XoGx3SdI2kY8zO7TmjB2dup5RA4D13_NTT6e2pYUq9FRVGwvpa6WX6QjITtsIOVssbw28QC1KAmHcA5pzzVo5bpdXiIwns5n70_nOfYTI3lST6Nij9KHn_b1rT7KKi--VT2tLtyIql4SPOGKsXDTk-gll4bKJcFJfJ4NKFcizmBirYaaL5sRXmcNtcZSXCMce_FHDFk468OGYiHnAy0Q35wbRwxhX3-5GMvmJWDu9bPnliQqJk3yBArKKTrqnDq633_0eMPaEXgnH44x42Md2gHRPJrmalZMn__CAk_5ySg3Yf2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: امیدوارم خبر اعزام ۴۰ هزار نیرو از سوی پاکستان به عربستان برای جنگ با مردم یمن شایعه باشد.
🔹
زیرا هم ما و هم کشورهای منطقه می‌دانیم که هر مداخله جدیدی در تحولات مرتبط با یمن، صرفا باعث پیچیده‌تر شدن اوضاع می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/466222" target="_blank">📅 12:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466221">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc651cc526.mp4?token=gbrjVOzW_cUVIS5JtPTa-JKnd59pgXxSdfzuETOr_M8yQkDTtrO0LSLiZI7EIqq4BN1PY65hZya_nZIvBXilkIcxsZHb2z2SA32lNzeG3Q57grn05cnORZF088TFpsolxgvVgdZIJM8rZWM2CdDY9lyMye5Fhvj0kC4Y_yN2zC7RvsS6HmghKtG3kUaRPzeNyLxR_Piuh_8coDMsHx8hblVsj7oog8vz-snl2u0Xznj5hqB9-eP45fmEv0hDiwKc9p0hqtDwM6ACmjGosEmAIYx5Wl0SHV6vnTDoE7oQO5XSqRGfYyeEd3WevayXECWi9RAXN1zp6u_tqTq4v5RTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc651cc526.mp4?token=gbrjVOzW_cUVIS5JtPTa-JKnd59pgXxSdfzuETOr_M8yQkDTtrO0LSLiZI7EIqq4BN1PY65hZya_nZIvBXilkIcxsZHb2z2SA32lNzeG3Q57grn05cnORZF088TFpsolxgvVgdZIJM8rZWM2CdDY9lyMye5Fhvj0kC4Y_yN2zC7RvsS6HmghKtG3kUaRPzeNyLxR_Piuh_8coDMsHx8hblVsj7oog8vz-snl2u0Xznj5hqB9-eP45fmEv0hDiwKc9p0hqtDwM6ACmjGosEmAIYx5Wl0SHV6vnTDoE7oQO5XSqRGfYyeEd3WevayXECWi9RAXN1zp6u_tqTq4v5RTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: توقف بمباران و رفع محاصره تنها راهکار حل بحران یمن است.
🔹
موضع ایران دربارهٔ بحران یمن کاملاً شفاف و استوار است؛ تداوم بمباران‌ها و تشدید محاصره اقتصادی ظالمانه علیه ملت مظلوم یمن هرگز راه به جایی نخواهد برد.  @Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/466221" target="_blank">📅 12:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466220">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3503b34580.mp4?token=ep_ndicV65Oa28xskwiQCgY-HetrFqZfRLwm1VLDI2sZbXJd77zVdqzkLRGTUg1mpc78zgwuE2Ljs3AyslUtpBMWxctEcCgIy5XcNh2dIE5g7efXX7JmCwxjByVtMV1WWu6CwznI8tc9Le1LnCzOiyohUygsWFk0_aQS4g5HnVXOd_pjRiKBJaRaI2VoNHcGBN1ZdDP9rU6fZcapGjR07rNmVSUoPooofgE384gQkjJiIgPqBgKZGdgnwMpK4vI9jJdveUQYLStsRK53qy0JPEJo-ON_RMFfrYOxpGSIENiE_r300ZCGVaYYIHl66THqeR87II8yOGcRwkBxy0-PLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3503b34580.mp4?token=ep_ndicV65Oa28xskwiQCgY-HetrFqZfRLwm1VLDI2sZbXJd77zVdqzkLRGTUg1mpc78zgwuE2Ljs3AyslUtpBMWxctEcCgIy5XcNh2dIE5g7efXX7JmCwxjByVtMV1WWu6CwznI8tc9Le1LnCzOiyohUygsWFk0_aQS4g5HnVXOd_pjRiKBJaRaI2VoNHcGBN1ZdDP9rU6fZcapGjR07rNmVSUoPooofgE384gQkjJiIgPqBgKZGdgnwMpK4vI9jJdveUQYLStsRK53qy0JPEJo-ON_RMFfrYOxpGSIENiE_r300ZCGVaYYIHl66THqeR87II8yOGcRwkBxy0-PLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ازسرگیری پروازهای عراق ناکامی سیاست انزواسازی ایران را اثبات کرد.
🔹
اقدام غیرقانونی آمریکا در تسری بین‌المللی قوانین داخلی خود، نقض آشکار مقررات حقوق بین‌الملل و اخلال در اصل حسن همجواری و روابط دوستانه منطقه‌ای است.
🔹
دستگاه دیپلماسی…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/466220" target="_blank">📅 12:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466219">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743ca75329.mp4?token=YNhxHoZ79q2YDBfgLR-2BwOTtD-iu5vqa7jxJfO3JQIweLCSSji4Man9LYux5PkNTOvPbMFnzWkiRg59f85-ZIXgM-y6JzGhM0Lg9FZEQJfSU-sLJhSmVoL7UervMA2bduS9yF25vHQITweO9wkKwJq93zj6V-UeYDvTKyxLQtJDZxIgZBzWqO7mHRPCsyf-B5BeCP1FT1_b0tpO2sj_I4aOtJsSqqjmZChpIG0hnUXCG-WWcejoc6eLrQYBiFLKKUYgsmRd0ZPaYrwUPe_rFPTQ4AFipjf9I770HEn-yPjoc9hOEpiUMU_TK3J6FOQAfuvTF5PVZtoKJ8-RzXxG9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743ca75329.mp4?token=YNhxHoZ79q2YDBfgLR-2BwOTtD-iu5vqa7jxJfO3JQIweLCSSji4Man9LYux5PkNTOvPbMFnzWkiRg59f85-ZIXgM-y6JzGhM0Lg9FZEQJfSU-sLJhSmVoL7UervMA2bduS9yF25vHQITweO9wkKwJq93zj6V-UeYDvTKyxLQtJDZxIgZBzWqO7mHRPCsyf-B5BeCP1FT1_b0tpO2sj_I4aOtJsSqqjmZChpIG0hnUXCG-WWcejoc6eLrQYBiFLKKUYgsmRd0ZPaYrwUPe_rFPTQ4AFipjf9I770HEn-yPjoc9hOEpiUMU_TK3J6FOQAfuvTF5PVZtoKJ8-RzXxG9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: پاسخ آینده ایران به هرگونه تعرض از مبدأ منطقه کاملاً متفاوت خواهد بود.
🔹
ایران با صدور هشدار قاطع به برخی کشورهای منطقه، خواستار تجدیدنظر فوری در گذاردن امکانات و قلمرو خود در اختیار جبههٔ آمریکایی-صهیونیستی برای تعرض به خاک ایران شده…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/466219" target="_blank">📅 12:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466218">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91dd73c84d.mp4?token=gZiDL4mMttj5vhoOaAbGZk9ofmTTitk1FG8kHio0MRFEqqIPUFJXRfBOxMfhsKGZwXa2sGw6IixRxiqzNPSnpsCWUWcGCc47y69pcZkwexWHOdEzj2qcCea6mH0BCJEWl_os8J_x_LS0BDDcgVJCfmF3Vjlq-Nfi-qy428wQap30nc-LBFuGXYhzFs3bpHYavPKc65wbbLXTbMmBEK3a_GuWJzjkjDgEQLixSZeUpwPgg1HV6-ju285I82m-6IfdgsVCpZ3HmnDFCwrRVmzqTKaDsLxSSzH9aLKEH2lYwaoVUKnGIoiSopnGMWGgay_l-WqADFowwPqy7wOuuk06jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91dd73c84d.mp4?token=gZiDL4mMttj5vhoOaAbGZk9ofmTTitk1FG8kHio0MRFEqqIPUFJXRfBOxMfhsKGZwXa2sGw6IixRxiqzNPSnpsCWUWcGCc47y69pcZkwexWHOdEzj2qcCea6mH0BCJEWl_os8J_x_LS0BDDcgVJCfmF3Vjlq-Nfi-qy428wQap30nc-LBFuGXYhzFs3bpHYavPKc65wbbLXTbMmBEK3a_GuWJzjkjDgEQLixSZeUpwPgg1HV6-ju285I82m-6IfdgsVCpZ3HmnDFCwrRVmzqTKaDsLxSSzH9aLKEH2lYwaoVUKnGIoiSopnGMWGgay_l-WqADFowwPqy7wOuuk06jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ایران از حقوق هسته‌ای و اقتدار ملی عقب‌نشینی نمی‌کند.
🔹
تداوم عضویت ایران در NPT از سال ۱۹۷۰ و پایبندی کامل به تعهدات بین‌المللی، متأسفانه با بدعهدی، تعرضات نظامی جبهه استکبار، ترور دانشمندان و حمله به تأسیسات صلح‌آمیز هسته‌ای مواجه شده…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/466218" target="_blank">📅 12:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466217">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3178e27c.mp4?token=cCJ9awHZ_hwOVYuNuSt130R82oYvHcJSPqttwUyaljX0HPDQaRzkcn7RGkQY-ItkUKxGXLgOmFxO_mNTdxYgKxW15zGdmrwThfOnP-crDjCSJEGZEwQWng_LCtd6cNj5E-znkSOi4HXGq8ru-VP4mp4Uz-W87auM5oYkkvLWAJdjASh4KDWnjgLOTUbxFqP5Xic4beSY6MLnxVBmJ8TQEJ-u0kqCNCe_Tog5S9IJd7pUUsTRY7eCkxyPqQ2cgEVQe2oTBaPzi4gva9JpdxVPExS-zKEuBcph1NajuAZ_Ish0S1cmw_acKPIZnZXibXD128I295xdOTjVuzl3UpyHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3178e27c.mp4?token=cCJ9awHZ_hwOVYuNuSt130R82oYvHcJSPqttwUyaljX0HPDQaRzkcn7RGkQY-ItkUKxGXLgOmFxO_mNTdxYgKxW15zGdmrwThfOnP-crDjCSJEGZEwQWng_LCtd6cNj5E-znkSOi4HXGq8ru-VP4mp4Uz-W87auM5oYkkvLWAJdjASh4KDWnjgLOTUbxFqP5Xic4beSY6MLnxVBmJ8TQEJ-u0kqCNCe_Tog5S9IJd7pUUsTRY7eCkxyPqQ2cgEVQe2oTBaPzi4gva9JpdxVPExS-zKEuBcph1NajuAZ_Ish0S1cmw_acKPIZnZXibXD128I295xdOTjVuzl3UpyHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: خروج متجاوزان، شکست ۲۳ سالهٔ اشغالگری آمریکا در عراق را رقم می‌زند.
🔹
پایان اشغالگری آمریکا در عراق و گام‌های عملی در جهت خروج کامل متجاوزان، رویدادی مبارک در راستای تحکیم سیادت، حاکمیت ملی و استقلال این کشور و اثبات دیگری بر شکست تاریخی…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/466217" target="_blank">📅 12:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466216">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d534aef2.mp4?token=P4Ys4jgZZYLKubx3R8AwrZwGetvFhkvka6gT_5eYc5jY_Li0NDrY4RS09QitdYrdNQz0MauYXE_QH6syyBDrLmgHt2dz6yQhVGzOdYcT-Y0hcTrY4g3LbUhL_eNrUn9GOZFmtTWSteWj-ABDR-Rtx9yF3ekRKMygPWJQgCQf07hJ_Rog-LgVzAsVBfQb5Quv5Q6D4LyDEw5fTBHMVB6j7FSPEyCI9KLvGJrIa8XdVYTXNkZPZjYVw2iDxku4BXDrtYEJsGRstdlhZtnMBrfl3DDH2GwXBfsF_Zeva7BNMQZuW9agQhTHAibWdeRf3K2KqteN2yuUY-tApkT2ABAsJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d534aef2.mp4?token=P4Ys4jgZZYLKubx3R8AwrZwGetvFhkvka6gT_5eYc5jY_Li0NDrY4RS09QitdYrdNQz0MauYXE_QH6syyBDrLmgHt2dz6yQhVGzOdYcT-Y0hcTrY4g3LbUhL_eNrUn9GOZFmtTWSteWj-ABDR-Rtx9yF3ekRKMygPWJQgCQf07hJ_Rog-LgVzAsVBfQb5Quv5Q6D4LyDEw5fTBHMVB6j7FSPEyCI9KLvGJrIa8XdVYTXNkZPZjYVw2iDxku4BXDrtYEJsGRstdlhZtnMBrfl3DDH2GwXBfsF_Zeva7BNMQZuW9agQhTHAibWdeRf3K2KqteN2yuUY-tApkT2ABAsJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کتیبۀ جدید تصویر رهبر شهید در ایوان ساعت حرم امام رضا(ع) نصب شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/466216" target="_blank">📅 12:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466215">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08444f99d1.mp4?token=hl4RixdFqFh9fiUSoC2DIRkVNk54jsptPieraEueHwJIJpa7ENelwNjHVKcvtXMEA_m3gdqdx--X5m4C-1HgjXBR0r7xa9mdjINoxvsbiMA-zhqmmkzFsDZSWvE2yNDt0CzpLBByA_Awt6HmLOXe_zD2z5ouP_H7oBWEWNOfzKvs4t1hryw-S2O0VYZMaPSvp56D0W2FSn_1KAmBaCdb5Fo-xxFNZ3NTpmyeYi3Kh-ViXcPo7AyfPZXppgofoSCThH2xmK5EEQHYmniTFbQM7R2CkiCyRtLR5RA1KSevGWft00yxj8-JwovrIWDe-PA6Vr1I-1Lx3uSeRi2axJB65g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08444f99d1.mp4?token=hl4RixdFqFh9fiUSoC2DIRkVNk54jsptPieraEueHwJIJpa7ENelwNjHVKcvtXMEA_m3gdqdx--X5m4C-1HgjXBR0r7xa9mdjINoxvsbiMA-zhqmmkzFsDZSWvE2yNDt0CzpLBByA_Awt6HmLOXe_zD2z5ouP_H7oBWEWNOfzKvs4t1hryw-S2O0VYZMaPSvp56D0W2FSn_1KAmBaCdb5Fo-xxFNZ3NTpmyeYi3Kh-ViXcPo7AyfPZXppgofoSCThH2xmK5EEQHYmniTFbQM7R2CkiCyRtLR5RA1KSevGWft00yxj8-JwovrIWDe-PA6Vr1I-1Lx3uSeRi2axJB65g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: حضور رئیس‌جمهور در ترکمنستان دیپلماسی منطقه‌ای ایران را فعال‌تر می‌سازد.
🔹
حضور رئیس‌جمهور ایران در شهر «آوازه» ترکمنستان جهت شرکت در دو رویداد راهبردی، جلوه دیگری از پویایی مستمر دیپلماسی منطقه‌ای و تعامل مقتدرانه با همسایگان است.  …</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/466215" target="_blank">📅 12:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466214">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec971ed20.mp4?token=JmsdnmawGFPYVX9T7yutaFGVsdj9ZfxeiKNaqnWV68ihYvXPiiyD3OB_oo1r4MlnvqxFEwJd5lvfw21zPdbHE5popAzA_fmsled0Cz2CguUOGuB6bCOZYpmpIusc9j-xA6lHgD4GV3HI_EXUnjXbtaBMMgu0dC_8prF42pneAJU1mP41_KaXq6BRIl6rf5K3RzGxsn6Vw722g4pXqVdsrs_q1SKBcUwF6waQpKIlu6RpXNQ6DXBNRkFtAEs2NbPdhFLogcs-cj0O94aFNHJmR1pPLYtI_0mcv20x2V67i3rSme-XI1kV1V3xHhurSznC8EUUQxh02UQAYlP0L_sG1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec971ed20.mp4?token=JmsdnmawGFPYVX9T7yutaFGVsdj9ZfxeiKNaqnWV68ihYvXPiiyD3OB_oo1r4MlnvqxFEwJd5lvfw21zPdbHE5popAzA_fmsled0Cz2CguUOGuB6bCOZYpmpIusc9j-xA6lHgD4GV3HI_EXUnjXbtaBMMgu0dC_8prF42pneAJU1mP41_KaXq6BRIl6rf5K3RzGxsn6Vw722g4pXqVdsrs_q1SKBcUwF6waQpKIlu6RpXNQ6DXBNRkFtAEs2NbPdhFLogcs-cj0O94aFNHJmR1pPLYtI_0mcv20x2V67i3rSme-XI1kV1V3xHhurSznC8EUUQxh02UQAYlP0L_sG1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار بلالی: متناسب با نیاز عملیاتی در ساخت موشک نوآوری می‌کنیم
🔹
مشاور فرمانده نیروی هوافضای سپاه: خودمان سازنده و تولیدکنندة موشک هستیم و نیازهای عملیاتی را درک می‌کنیم؛ به همین دلیل به‌دنبال نوآوری می‌رویم و محصولات مورد نیاز عملیات را تولید می‌کنیم.…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/466214" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466213">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8523050e.mp4?token=ihaibbdJouXO9wqEfOjzpmK9sI0xuPt3K68oXeT1Y4ODkCd2ProXI0MKp8t0aZsXfQWEFy9zbBp1sK6BI3KhIrIVeB3tPStc1KOBdJbXf5EcpBorBnZ96B_wmYHI436mobYYFpd0zDLVQNrQER13R13UFmFGUHiYLeFJQIF0vC9m39VO6FLwa9LLrsCIfSXo3xnXRRP4LoGsGRxS6soJHs0IM8XNDqvFR2Hctg3rK2oGndhd-En-kb-qpI5Dqrxc4LWanvL0pACdGsuzY9z5YFaB9BXD-sFXaOBEpbtYFqG4Gb9v_ybciSnPpQ0Ty70l-NgFcRohZMvhhNIQozmKlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8523050e.mp4?token=ihaibbdJouXO9wqEfOjzpmK9sI0xuPt3K68oXeT1Y4ODkCd2ProXI0MKp8t0aZsXfQWEFy9zbBp1sK6BI3KhIrIVeB3tPStc1KOBdJbXf5EcpBorBnZ96B_wmYHI436mobYYFpd0zDLVQNrQER13R13UFmFGUHiYLeFJQIF0vC9m39VO6FLwa9LLrsCIfSXo3xnXRRP4LoGsGRxS6soJHs0IM8XNDqvFR2Hctg3rK2oGndhd-En-kb-qpI5Dqrxc4LWanvL0pACdGsuzY9z5YFaB9BXD-sFXaOBEpbtYFqG4Gb9v_ybciSnPpQ0Ty70l-NgFcRohZMvhhNIQozmKlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: همدستی انگلیس با در اختیار گذاشتن پایگاه نظامی جرم آشکار بین‌المللی است.
🔹
بقائی در پاسخ به خبرنگار فارس: احضار سفیر انگلیس و ابلاغ اعتراض رسمی ایران، پاسخ صریحی به فرار روبه جلوی لندن از مسئولیت بین‌المللی خویش در مشارکت با تجاوز نظامی…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/466213" target="_blank">📅 12:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466212">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZHJz9GVS4Rvai0i_bP0fz6v9Idyjy0N9-G0Of9gC0c4TdIrsHwQiYAtnbm3mrXA_ozbnKEAiT4QpPvpBfxT7Wpntzw3J40bZGIG0mnVgfmOtCx3jImF4f5u-tAnhOGPDlG_FF_eNHtAMZcZSZqiM64TAuwxVQ7u3oC0OBamS3cxcNS_Qm2HdUmrasDJzmLbCplXi14nx_NxLGdx5F3qkP_NJlDeL0FSoO8VRRVzgKDPqNGVlDcVA3iPf9l_-l0mUPsaPjG8mZyFiTnVjHKgdv16NfQwgcXlp7fCw-H734-l4irCDWQDggwuOh0phvjtnMXPkfv_pig5CuwtN9IZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس مهرماه سال ۱۴۰۵ تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا ۱۳ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/farsna/466212" target="_blank">📅 12:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466211">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0f900518.mp4?token=QsJMWC10vDVPlgy7Avn5BT8Xic39WhiD4URdbzIkvGExGQVIc087efTTxvCvMBAR5EedeR_cp-_eIby6teTNs6qUInIp4X99B5biItqueDC153H-90uFMjSPaZkDIZAUkmfHTfDRe4Gf3xiYCF2vl9DRCYTJDxdy-tRyZPDOJlo7eLYNXm2P-58cvQl7UVrTfzrUSwuyybfXty8WEnxrsJSQiQYkdv65RDMthpp2LmxxBKX1Lf68wPSui-PF8XkXzu1bPF8Iq1X-uJ2XpZy9SBSNC05kO2N6ncHIwG6srvpS8v98M87exHdTdrRM5faHby8h7eo6zH__q8m6QGnblA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0f900518.mp4?token=QsJMWC10vDVPlgy7Avn5BT8Xic39WhiD4URdbzIkvGExGQVIc087efTTxvCvMBAR5EedeR_cp-_eIby6teTNs6qUInIp4X99B5biItqueDC153H-90uFMjSPaZkDIZAUkmfHTfDRe4Gf3xiYCF2vl9DRCYTJDxdy-tRyZPDOJlo7eLYNXm2P-58cvQl7UVrTfzrUSwuyybfXty8WEnxrsJSQiQYkdv65RDMthpp2LmxxBKX1Lf68wPSui-PF8XkXzu1bPF8Iq1X-uJ2XpZy9SBSNC05kO2N6ncHIwG6srvpS8v98M87exHdTdrRM5faHby8h7eo6zH__q8m6QGnblA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ارتقای امنیت تنگه هرمز مستلزم لغو کامل تحریم‌های آمریکا است.
🔹
ارسال پاسخ‌های صریح و مقتدرانهٔ ایران به پیشنهادهای طرف آمریکایی از طریق میانجی قطری در دوحه، ناکامی واشنگتن در انحراف مسیر گفتگوها به سمت مباحث هسته‌ای را آشکار ساخت.
🔹
موضع…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/466211" target="_blank">📅 12:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466210">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5992e0e99c.mp4?token=M-w0D4bT2ehUyJMd6CrdrAvwGD5H4mU9yXrcH_-vOR9zVLj9jpf16Hv7dU2b-LoHpOQJDmdTj4PeKQDhh_0tcNoyIwWCfJDO52zs8q7iWUwIZCkJmRm_VhRwfofP_zDfGb1uPbnz2q2OVzxhRCc0vOhJucBG2VuJJshovMBirxsDG58utc5SXqKvXVQH87jCdgonYwwthurcl1Nno_-A8FCr79ApR-5NrUSxqoi0jVB2WVgg8HsNec8cwXotnUamjjVM_h0rocDhKdQNJkwIKeobCIc8JHl0dAKUCtBnMkRkbFm_JaDco_RRlrMJeJgP4gwzDAL7GbJgwKdpc4MZgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5992e0e99c.mp4?token=M-w0D4bT2ehUyJMd6CrdrAvwGD5H4mU9yXrcH_-vOR9zVLj9jpf16Hv7dU2b-LoHpOQJDmdTj4PeKQDhh_0tcNoyIwWCfJDO52zs8q7iWUwIZCkJmRm_VhRwfofP_zDfGb1uPbnz2q2OVzxhRCc0vOhJucBG2VuJJshovMBirxsDG58utc5SXqKvXVQH87jCdgonYwwthurcl1Nno_-A8FCr79ApR-5NrUSxqoi0jVB2WVgg8HsNec8cwXotnUamjjVM_h0rocDhKdQNJkwIKeobCIc8JHl0dAKUCtBnMkRkbFm_JaDco_RRlrMJeJgP4gwzDAL7GbJgwKdpc4MZgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ایران سوءتفاهم‌های دیپلماتیک با بیروت را از طریق گفت‌وگو رفع می‌کند.
🔹
علی‌رغم برخی فضاسازی‌های بیرونی، سفیر ایران پیش‌تر موافقت رسمی (آگرمان) خود را از دولت لبنان دریافت کرده و هیچ‌گونه اجماع‌‌نظری علیه روابط دیپلماتیک دو کشور در داخل…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/466210" target="_blank">📅 11:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466209">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb119fa8a.mp4?token=NGgfJG_rTEkwvMkzuG1DW02N99NmuzpYi0SVpY8GR5AHCtXXl3BQQPVwhESFHlEfBKVrdTKvZT_ND2JxbL02GA0EkKTvhbCA3eWJBXi8I_1ZmV6AELm2t3vW0hd5AUW6Lml_9-PvbAd_ynHTXZxM5Hx8qwsBFyArIIRPCW1-tF9aAQtJgWFlH9O4zfTPzJcniry19uzCQWjGzKcHoOsc7FZ6mbkEHxxm4aWMCcsfOFXm_4jqOfhoooVvY5offYKpQQhTf-eHBsxcttXWRg074Z2rewZqul-C-JkwtHBAsos72hi4oCjq46plNgeJrK_7dX_hlnUjNeCzvNhmcWexIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb119fa8a.mp4?token=NGgfJG_rTEkwvMkzuG1DW02N99NmuzpYi0SVpY8GR5AHCtXXl3BQQPVwhESFHlEfBKVrdTKvZT_ND2JxbL02GA0EkKTvhbCA3eWJBXi8I_1ZmV6AELm2t3vW0hd5AUW6Lml_9-PvbAd_ynHTXZxM5Hx8qwsBFyArIIRPCW1-tF9aAQtJgWFlH9O4zfTPzJcniry19uzCQWjGzKcHoOsc7FZ6mbkEHxxm4aWMCcsfOFXm_4jqOfhoooVvY5offYKpQQhTf-eHBsxcttXWRg074Z2rewZqul-C-JkwtHBAsos72hi4oCjq46plNgeJrK_7dX_hlnUjNeCzvNhmcWexIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: کمیتهٔ ۶ نفره شورای‌عالی امنیت ملی پرونده مذاکرات را هدایت می‌کند.
🔹
حضور وزیر خارجه در این کمیته عالی که مسئولیت بررسی دقیق و همه‌جانبهٔ موضوعات مرتبط را بر عهده دارد، گواهی بر هماهنگی کامل دستگاه دیپلماسی با تدابیر کلان امنیت ملی است.…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/466209" target="_blank">📅 11:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466208">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fe5ac6185.mp4?token=i4wOH4DF6rhxI41JR3IwnbfOZSKYRmpIZuPuJl1sXRVRZBJapiyqjy_TVYPLrFqR0wxQBRsS1xCFI080oJwlMqATvrVlLKhqtOwJ7q-Ju9XYen3HctIAFAYcUVFmRRYwUYh_yCzr6L0HZyUFWrh67ILr9iJAmddtMTz-myZNh8thWhBSh6MSgmQG8_kN6nHY2BVB7vxTAMwpWk1hxzEtAn1xj39hFoZI-_bf8thphxLeyJnYH7czSg1rOkC4CNAG5e3hKrkoLFM6aHiJTGx9aRs5-CzAIP7k1sbXSWfctYdzAIQuODwmRQceWc9l5PSs7Fz9rb_UpLdk49wlBN0NuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fe5ac6185.mp4?token=i4wOH4DF6rhxI41JR3IwnbfOZSKYRmpIZuPuJl1sXRVRZBJapiyqjy_TVYPLrFqR0wxQBRsS1xCFI080oJwlMqATvrVlLKhqtOwJ7q-Ju9XYen3HctIAFAYcUVFmRRYwUYh_yCzr6L0HZyUFWrh67ILr9iJAmddtMTz-myZNh8thWhBSh6MSgmQG8_kN6nHY2BVB7vxTAMwpWk1hxzEtAn1xj39hFoZI-_bf8thphxLeyJnYH7czSg1rOkC4CNAG5e3hKrkoLFM6aHiJTGx9aRs5-CzAIP7k1sbXSWfctYdzAIQuODwmRQceWc9l5PSs7Fz9rb_UpLdk49wlBN0NuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برجک زندان رجایی‌شهر فروریخت
🔹
در ادامۀ تخریب دیوارهای زندان رجایی‌شهر البرز، برجک این زندان نیز تخریب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/466208" target="_blank">📅 11:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466207">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wt8UiM8MrJ0oVXTZJsG94VDwVjJUWvMwAikgk99ec-89Ahmo8WC_QzOfTa1ttsAowt0f9-oGNTROpiLW_3d8kgNtAHDLqgQLNY0uKtLMKgF2T94cOcSTECeKRkaW_wiObKqwBoOAmjow3citAhS_KMN6lJISyYrb2sG3Mdjz56wwEr4DEWyDir-Uwi96mLGcYjLWYaswIKy7-PY50S3oyoCG7lHeemRJt1fbjD3eidIjZS3zOEI7lEKJk-Fjc0uUsunn7RYyTmVipano8IqG0ew4eZtAoY8AYnjdlEX9ksPhjwM6o9_kwYtG4jyqAMkOuaaHz6DVvcL4CpAlMGsttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: اخراج آمریکا از عراق، آغازی بر پایان حضور نظامی واشنگتن در منطقه است
🔹
حزب‌الله لبنان با انتشار بیانیه‌ای، اخراج نیروهای اشغالگر آمریکایی از خاک عراق را یک دستاورد تاریخی و پیروزی بزرگ خواند و آن را به دولت، ملت و مرجعیت این کشور تبریک گفت.
🔹
حزب‌الله…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/466207" target="_blank">📅 11:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466206">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28abbaba6b.mp4?token=AUJM_FSTdcoK6gJeg9Acs-0NVWIHffifTgSjxGcE-ogHwyRCzhbkk9yn3frwgb42xZTwFUAgKAWsWJUmC-jd22cuX2aC0UdVcCEOOk_Las3JpEhqJRwd1LLECsRc6IxuyXQ62ewuQMplOaSA6d5kQOtHhk2CWdlxJANeH_UI1_evK94hflQ7_8dotDmWCwN2WNPvrjzINRJExr4WAjGpbxGLaVJn3Ss64EkjajXZBYmLI4vvs3rZJB7eqsDqTXu2_VafNhNdp31C-HuHDyrsY_Md-eBa4yCXD7vqonT7z1GZBegz4Swak5VUOkbtdLsLdTCMsJhgOv2sW714SlQjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28abbaba6b.mp4?token=AUJM_FSTdcoK6gJeg9Acs-0NVWIHffifTgSjxGcE-ogHwyRCzhbkk9yn3frwgb42xZTwFUAgKAWsWJUmC-jd22cuX2aC0UdVcCEOOk_Las3JpEhqJRwd1LLECsRc6IxuyXQ62ewuQMplOaSA6d5kQOtHhk2CWdlxJANeH_UI1_evK94hflQ7_8dotDmWCwN2WNPvrjzINRJExr4WAjGpbxGLaVJn3Ss64EkjajXZBYmLI4vvs3rZJB7eqsDqTXu2_VafNhNdp31C-HuHDyrsY_Md-eBa4yCXD7vqonT7z1GZBegz4Swak5VUOkbtdLsLdTCMsJhgOv2sW714SlQjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه در واکنش به ادعای اخراجی هیئت ایران از آمریکا: دشمن با دروغ به‌دنبال دستاوردسازی است؛ این ادعا کاملا دروغ است.
🔹
ورود و خروج ما از ابتدا اطلاع رسانی‌شده و مشخص بود؛ یکی از دیپلمات‌های ما قرار بود چند روز دیگر برای انجام وظایف در نییورک…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/466206" target="_blank">📅 11:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466205">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e66396ea.mp4?token=JXscxRWFiq1UTPn7cs-WeMwkZJKj1QDqNRaYVT0SyMAapKF04pPABhA-145GIDMibx7CSYD3BPU4sV8VZ2DQXPxqAF9g1Pb49-XlmTmhJK5J_6QOMQgQhhRgkgMZfLalXTFHlK784NnZCH9sxw1IrGUSyWJ0YoTM_8ov4TnPUJOLfbfRxSPumhOU3yVLyk6evjVbciaBvV7bFYxQPdAe48O70wXTi2j0XZzsaEL8aOQrwKKCTEiWZZSW_UxiQ6O16Dqqy1Y8zJC2idP5g5JYR1zV9NESJ7gWXJMOkIGO6xaakz0YrExVlvVykbOOxz8pMvZGQ9on2uJUOpi477e1HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e66396ea.mp4?token=JXscxRWFiq1UTPn7cs-WeMwkZJKj1QDqNRaYVT0SyMAapKF04pPABhA-145GIDMibx7CSYD3BPU4sV8VZ2DQXPxqAF9g1Pb49-XlmTmhJK5J_6QOMQgQhhRgkgMZfLalXTFHlK784NnZCH9sxw1IrGUSyWJ0YoTM_8ov4TnPUJOLfbfRxSPumhOU3yVLyk6evjVbciaBvV7bFYxQPdAe48O70wXTi2j0XZzsaEL8aOQrwKKCTEiWZZSW_UxiQ6O16Dqqy1Y8zJC2idP5g5JYR1zV9NESJ7gWXJMOkIGO6xaakz0YrExVlvVykbOOxz8pMvZGQ9on2uJUOpi477e1HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: کشورهای منطقه باید مانع سوءاستفاده از قلمرو خود برای تعرض علیه ایران شوند.
🔹
در حاشیهٔ مجموع عمومی سازمان ملل با کشورهای جنوبی خلیج فارس صحبت کردیم؛ رایزنی‌های دیپلماتیک ایران در نیویورک، آزادی هم‌وطنان بازداشت‌شده در امارات را محقق…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/466205" target="_blank">📅 11:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466204">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29297c7fcf.mp4?token=CuXmDhoqf944a_T_9y-CnNwuBKpExYQWDhF8EIvjK4m4_xKGxt99P3UFPK17Fa89Ix2TaPJouw6J5W0M9NskDiD88KQQDNuQEuczt8NboQQRKW2L04E0hfvVYs3jzr0w7nZ5LKbPt8dXwdkziLixE4xVU-1wuzQqeN65k9oOkrwUJOOBku99vWIr52ulk47QR3d2qFnGkvo5az7KGmY9tEZe66igHYbMJBTEeoTMOwyaTYtxzN0aRGEooxHhRepC1MrfGfL7e5yxcQsKRxqEqle-nyb9XrWA6gUMM0rcxvNTiQv04NUhh_5NQOPmn3CPOPlV8RP7FkVrRYru0K25Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29297c7fcf.mp4?token=CuXmDhoqf944a_T_9y-CnNwuBKpExYQWDhF8EIvjK4m4_xKGxt99P3UFPK17Fa89Ix2TaPJouw6J5W0M9NskDiD88KQQDNuQEuczt8NboQQRKW2L04E0hfvVYs3jzr0w7nZ5LKbPt8dXwdkziLixE4xVU-1wuzQqeN65k9oOkrwUJOOBku99vWIr52ulk47QR3d2qFnGkvo5az7KGmY9tEZe66igHYbMJBTEeoTMOwyaTYtxzN0aRGEooxHhRepC1MrfGfL7e5yxcQsKRxqEqle-nyb9XrWA6gUMM0rcxvNTiQv04NUhh_5NQOPmn3CPOPlV8RP7FkVrRYru0K25Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مجمع عمومی سازمان ملل فرصت مهمی برای رساندن صدای منطق، اقتدار و مظلومیت ایران به دنیا بود.
🔹
یکی از موفق‌ترین حضورهای ایران در مجامع بین‌المللی را در هفتهٔ گذشته تجربه کردیم. @Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/466204" target="_blank">📅 11:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466203">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yonk55ma3BDIEaY1RXm3w3UOzMosvfrVFoEysFCfNnMu2I40tX7Y_daSwlcJSfYPH8hjEhptEFJPLk08dSdV1FM1AcK8tvUPyJMxi18cJT1IDIaowYZ3uYxN7Xf70m_uTtvn-ZUdJplG0SUZ0t41BPtWFRtVVGkhxiXv76-mGe1-Z4-nnY0DpHVrcQYGKSlNeEiH45FrjwqqiUj_th_MoAc3nlSipNWQTVWeovkCkJq50dAQTR1E3lc8x58lqzC7ihhtG92yMPX5wKavXaYByaX_cWQWt17UiG1LGukBLJMS_xJh6GW5ZmNOSczV7NquFICX22HYDUkvTgxAZw9w0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: درخصوص استیضاح وزیر کار تصمیم‌گیری می‌شود
🔹
بیگدلی، عضو کمیسیون اجتماعی مجلس خطاب به قالیباف: پس‌از اینکه استیضاح احمد میدری در کمیسیون بررسی شد، باید در نخستین جلسۀ علنی مطرح شود. از شما درخواست دارم دربارۀ ارجاع استیضاح وزیر کار تعیین‌تکلیف شود.…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/466203" target="_blank">📅 11:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466202">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16f66a5c2d.mp4?token=om4Qd2QP6m_IX2gxQIHIPLrvZLt3cttaF6Bbdeyr04SXv7uqwtJNFRJv0n6VSXPFvVvQKfvageJ7infZyJH8f8PIjGwHN20n60yykQBqg6YJ2Nli4ZdzKRtnHAostx02eKtNrHsW1OqWsu58EE_KpGf-dciGKO4NgMo9qKdfS8V1sWZ-B6upCJbyNlcQdD6HBrwkWx7nsuSSp6yn7N6-GQTOZugp5kCRJSxHSDPbpZD_s65UXi58F52cnFLU3-UNeO9IUlSRZSImOt8XKGAHV33RC58ojd8ignhm9Nw3XV6i2ozLIVXddmn5U_LqvI3nIzuGn0zbrclpKus5jS1PFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16f66a5c2d.mp4?token=om4Qd2QP6m_IX2gxQIHIPLrvZLt3cttaF6Bbdeyr04SXv7uqwtJNFRJv0n6VSXPFvVvQKfvageJ7infZyJH8f8PIjGwHN20n60yykQBqg6YJ2Nli4ZdzKRtnHAostx02eKtNrHsW1OqWsu58EE_KpGf-dciGKO4NgMo9qKdfS8V1sWZ-B6upCJbyNlcQdD6HBrwkWx7nsuSSp6yn7N6-GQTOZugp5kCRJSxHSDPbpZD_s65UXi58F52cnFLU3-UNeO9IUlSRZSImOt8XKGAHV33RC58ojd8ignhm9Nw3XV6i2ozLIVXddmn5U_LqvI3nIzuGn0zbrclpKus5jS1PFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مجمع عمومی سازمان ملل فرصت مهمی برای رساندن صدای منطق، اقتدار و مظلومیت ایران به دنیا بود.
🔹
یکی از موفق‌ترین حضورهای ایران در مجامع بین‌المللی را در هفتهٔ گذشته تجربه کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/466202" target="_blank">📅 11:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466201">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd1rdiGoyK75U0Ct4ka9lumUm3LXfCdMZ2DGNvd7w6Mf7lw_FYC6MFqD25pgZ7HV0gO4RAJO3ybdIMVzqJQrHRCjr8IFLsODnjMmWuTu3sxntTMILYZdSsZgs-iE0Qo_ixM-u0C6u4fKRNdjM08A04SmffQZXzzpyJd-EYz9KYN1KzaZiHgWrUaqPuW0Na2jRe4UJwgMLy3t9NcdzzWxvLZlJXRiQ9Bbquq4_Fl2pglM0Yq-GNMnXRkPx95iufBs_1lJS81ywxcjSE_JImtOKDXMvSXyIiIQCtEOY3gGC_c8NEtdrYw5FYQVRZX4WEaCTVgkx8XkzQ6Jmdanf59o2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسات مجلس از هفتۀ آینده در محل دائمی صحن برگزار می‌شود
🔹
سخنگوی هیئت‌رئیسه مجلس: طبق مصوبۀ شعام از هفتۀ آینده جلسات صحن علنی با سازوکار دیگری تشکیل خواهد شد.
🔹
براساس تصمیم جدید هیئت‌رئیسه، جلسات صحن هم در محل دائمی صحن و مکمل آن به‌صورت وبینار برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/466201" target="_blank">📅 11:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466200">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bdd591de.mp4?token=vkVXZjbrjJ-GKY6maQQRnoK50sFlWOBpmRHPYD5a3FS6iflZUqTZuqtL3PjP-Gg9wrkq3-s2v814nkPwMGp6G1O9nnpRUbZeJGrTv094ZL28dUZHYg6hzn3q2ZqpBnf7NMDHm2SF48Z_pF6-1Y2jeoZh8elV4VM_TPLm43vpJEe2Sfsk2el5mtyvKLupX8WMmSweSIlEH37FQ4jhDXTPuU-n7jpB_HJQiBSrftiffqix7EY6YrWmDMYgvPcbu3fxgnTutw7fhLu2uaegZmQqNl_xkqqJQDh4Z5S5tc-3Di8tnuOiS7fEmJIQLTDmdRvcagos_Loa2oDrwyvtiMC8JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bdd591de.mp4?token=vkVXZjbrjJ-GKY6maQQRnoK50sFlWOBpmRHPYD5a3FS6iflZUqTZuqtL3PjP-Gg9wrkq3-s2v814nkPwMGp6G1O9nnpRUbZeJGrTv094ZL28dUZHYg6hzn3q2ZqpBnf7NMDHm2SF48Z_pF6-1Y2jeoZh8elV4VM_TPLm43vpJEe2Sfsk2el5mtyvKLupX8WMmSweSIlEH37FQ4jhDXTPuU-n7jpB_HJQiBSrftiffqix7EY6YrWmDMYgvPcbu3fxgnTutw7fhLu2uaegZmQqNl_xkqqJQDh4Z5S5tc-3Di8tnuOiS7fEmJIQLTDmdRvcagos_Loa2oDrwyvtiMC8JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های پاریس علیه ماکرون به‌صدا درآمد
🔹
صدها نفر از معترضان فرانسوی در مرکز پاریس تجمع کردند و با سردادن شعارهایی علیه رئیس‌جمهور فرانسه، خواستار خروج کشورشان از اتحادیهٔ اروپا و ناتو و توقف حمایت نظامی از اوکراین شدند.
🔹
فیلیپو، رهبر حزب «میهن‌پرستان» فرانسه، در این تجمع گفت: «منابعی که دولت فرانسه برای اوکراین هزینه می‌کند، باید برای کاهش مالیات سوخت در داخل کشور اختصاص یابد و به مشکلات اقتصادی مردم رسیدگی شود.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/466200" target="_blank">📅 11:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466199">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۴ معبر تهران به‌نام شهیدان تنگسیری، شمخانی، موسوی و خرازی نام‌گذاری شدند
🔹
بزرگراه جدید‌الاحداث(دوگاز): به‌نام شهید عبدالرحیم موسوی
🔹
میدان نوبنیاد: به‌نام شهید شمخانی
🔹
بلوار دریا: به‌نام شهید تنگسیری
🔹
خیابان رام(پاسداران): به‌نام شهید کمال خرازی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/466199" target="_blank">📅 11:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466198">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4tXckXLwiNQHXZdiAKzY-i4sEts9UdUNNa9RrsVz1ycJxQOCxmpnUhwRGwu2uGLfQgCwkGBarBYmd2vfqcbZxmmTU-fLfQzikUJzdbLKjOYHE9xRfgOZRRjXeqHJ_GwPkXf6ueNQ1zXLSVqoS_psJoscOUUPhW_n_2vOVqSJaQ61OOR9Bs0X1tmqEk3HHcnQ1Xt-usGrVsywUgMVCROdZil6AZY6MlpcgoBICrCQWSat-BB3t5j2-xR80qdcqgUoRv9yqculgrHRYqOk8-F5cCZht6mxiMGQZAGNLvC-vKwTXfvhLktDEt84HJZUB5LZWEaPkJ-fOh-1HaFK7Z6dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: حملات به پالایشگاه‌های روسیه را افزایش می‌دهیم
🔹
رئیس‌جمهور اوکراین: کی‌یف در واکنش به تشدید حملات روسیه به زیرساخت‌های انرژی و شهری اوکراین، حملات خود به پالایشگاه‌های نفت روسیه را افزایش خواهد داد.
🔹
سرویس‌های اطلاعاتی اوکراین اسنادی به‌دست آورده‌اند که نشان می‌دهد رئیس‌جمهور روسیه «دکترین جدیدی» برای حملات نظامی تدوین کرده است.
🔹
این سیاست جدید طیف گسترده‌تری از اهداف غیرنظامی از جمله زیرساخت‌ها، مراکز لجستیکی، جاده‌ها، مدارس و بیمارستان‌ها را دربرمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/466198" target="_blank">📅 10:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466197">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گروهی از زندانیان ایرانی در امارات آزاد شدند
🔹
گزارش‌های رسیده حاکی است در پی رایزنی‌های مستمر هیئت‌های دیپلماتیک و امنیتی ایران، گروهی از زندانیان ایرانی که سال‌ها در زندان‌های امارات به‌سر می‌بردند، آزاد شدند.
🔹
این هموطنان که تا ساعاتی دیگر از طریق مرزهای هوایی به آغوش وطن بازخواهند گشت، شامل تعدادی از بانوان ایرانی نیز هستند. پیگیری‌های حقوقی و دیپلماتیک برای استیفای حقوق این هموطنان، به‌صورت جدی دنبال می‌شود.
🔹
بنابر اعلام این هیئت دیپلماتیک و امنیتی کشورمان، رایزنی‌ها برای آزادی سایر زندانیان باقی‌مانده در امارات و بازگشت کامل آنان به کشور، با جدیت در دستور کار دستگاه‌های مسئول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/466197" target="_blank">📅 10:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466196">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a02c8515.mp4?token=NuVAAEucPHh64mZY-Vw7Y5B5T71cSROgmoZ1beLhCHitJwUihiB3YLfT5eUTFZL4IfFn9UvxdU3nOIMJx6Zs1_kf0QjFeVKyrS8VcnfTEHXcTHFlpFu2afk_2Qx7TI5wrqwBR7Rzc-akfG0zSHxsD412kcBaQeiNzrGA_8TsBkgCO_O5DXFGW5gbajQGwKGNTpNMOREmYjLJeKXKbXEo1SvC-cfvOR4xwv28keWmNyJ7ZHHyQSSNG4uswi60oC3jpC4hoGXJ89OOKKr0P5gJsWBK43g2mpk0JXOjom4AZEW4Z7nNhLJKeSFYIBeb2hGSbKkfnZUgUSLzFz5EPcz_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a02c8515.mp4?token=NuVAAEucPHh64mZY-Vw7Y5B5T71cSROgmoZ1beLhCHitJwUihiB3YLfT5eUTFZL4IfFn9UvxdU3nOIMJx6Zs1_kf0QjFeVKyrS8VcnfTEHXcTHFlpFu2afk_2Qx7TI5wrqwBR7Rzc-akfG0zSHxsD412kcBaQeiNzrGA_8TsBkgCO_O5DXFGW5gbajQGwKGNTpNMOREmYjLJeKXKbXEo1SvC-cfvOR4xwv28keWmNyJ7ZHHyQSSNG4uswi60oC3jpC4hoGXJ89OOKKr0P5gJsWBK43g2mpk0JXOjom4AZEW4Z7nNhLJKeSFYIBeb2hGSbKkfnZUgUSLzFz5EPcz_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی در واکنش به ادعای مقامات آمریکایی مبنی‌بر اخراج هیئت ایرانی، با رد این موضوع گفت: هیئت ایرانی طبق برنامهٔ از پیش تعیین‌شدهٔ خود به آمریکا سفر کرده و بازگشته است.  @Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/466196" target="_blank">📅 10:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466195">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNli9aOtGKTAXTy5sxDU6V-s9AARTfO7Ar1BoAJovQ06889sHt3gcyRTR3pdaHO4AKBSogNtJu_HuiYyjilYZcJ1REQpoO1586Dd1LixZyNf5LlTzUYJz1cCFAE2a1z7At9dY4-F6I4ffOc7QiQKo2_ulhVS8rmbdijX-ZJbt0h3dM_yMdG7ZimAy9Y729PzU96W96N_TQ1wqtIQI7uXAMS6oPR05K_QHcWY1EI1UcQAIL7Wg-SXcceizPUG5hhrb4rP8FhdQxHZup6dgZxxqK7ht37OBLc7H7hWuK3mfZb7DkZNawMKDyvM4shUAdr1oY0B9gM_oVMRuHvGPcPBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس‌دفتر رئیس‌جمهور: شایعۀ موافقت دولت با استیضاح میدری تکذیب می‌شود
🔹
در فضای مجلس شایع شده که دولت با استیضاح وزیر کار موافق است و خود دولت این را گفته.
🔹
شأن دولت قطعا این نیست. رئیس‌جمهور از همۀ وزرا با تمام وجود حمایت می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/466195" target="_blank">📅 10:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466194">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6aNlvLBUTBE6eugqmO5wmIC0T_FYm3OVGSRgjJscw_5VQgcaHCBouVv6crBd8LaGQ55SJAS306uwwIYK6qI6uTCE1AVEFPmk_b77CjyUdlg9zc0pSYI3owUp6sCpmmRvCtgz9-OJ9m4Tk3KcfQlpL0jtLpo6xhhmUa4ytyMhjmXiA3A4Q6s6TV8qAlNuouR_JvIZbLCCInlFfdwERO1s952ZnroBZDaf1pkZq7Md3F0o5pa00c7uybRqLrjTKzvWz8WtzKG2gwOalQL2t6PsTSPJEzf6e17kM5bHb_OE0GgLnF9NZV2Z075iOPtWxo8mMxHQrzXNqO9rFHWy-RM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی عراق: پروازها به ایران از ماه اکتبر (۹ مهر) با مبدا نجف آغاز می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/466194" target="_blank">📅 10:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466193">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انهدام کنترل‌شدهٔ مهمات در پاکدشت
🔹
سپاه استان تهران: تا ساعت ۱۶ امروز عملیات انهدام مهمات عمل‌نکردهٔ دشمن در پاکدشت انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/466193" target="_blank">📅 10:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466192">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0194d01ade.mp4?token=dagGSQQ7DBflFzICGjEzoj0G11AKhy1t8-l3xLs65sEVXOiBtIICdDCRgGur8ZAY7qmYE1ez4UXQTqAOBUpVrDcPjq9EixTyt7_7rnBYnraP145MTVJcWwDg8U5Dn-u33H_Xgl-mdBT0m-7ISApSla8pftVrgAoDZJw_9CHKZOQVfP-LoXjVjys4SlsG_TCzm02KBFjdHM8V_mIOTLk9FBh2-XPSC40GK4hiy0BxMTQ2xOI0N6RLCjdshf5uaCpJ5M77z8iWQ1nEt585QIaF_nM96tzbLBccOIGpap34SBYRcOQlrmrTXeAWPivgTcoVGTRWLr1mwD_LjN03RfLQXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0194d01ade.mp4?token=dagGSQQ7DBflFzICGjEzoj0G11AKhy1t8-l3xLs65sEVXOiBtIICdDCRgGur8ZAY7qmYE1ez4UXQTqAOBUpVrDcPjq9EixTyt7_7rnBYnraP145MTVJcWwDg8U5Dn-u33H_Xgl-mdBT0m-7ISApSla8pftVrgAoDZJw_9CHKZOQVfP-LoXjVjys4SlsG_TCzm02KBFjdHM8V_mIOTLk9FBh2-XPSC40GK4hiy0BxMTQ2xOI0N6RLCjdshf5uaCpJ5M77z8iWQ1nEt585QIaF_nM96tzbLBccOIGpap34SBYRcOQlrmrTXeAWPivgTcoVGTRWLr1mwD_LjN03RfLQXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: دشمنان اگر برخورد نظامی را در پیش بگیرند پاسخی محکم می‌گیرند
🔹
وزیر خارجه در نشستی با سفرا و رؤسای نمایندگی‌های خارجی مقیم تهران: ایران در راستای دیپلماسی و پیدا کردن راه‌حل دیپلماتیک جدی است؛ همانطور که در دفاع از خود جدی است.
🔹
شرط‌های خود را برای…</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/466192" target="_blank">📅 10:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466191">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0wo30Ad4qltLQKDQUIR2y45yo5yFIb0aScCrhQ2Ewvw2eWb5wxgE6ldvYG8jr6eDnUvAlrZNUG-3ST3dBPsd9O4mbqccPTpHvRFIlXVo5a84D_OtdA2i9b8uwqKdxQtgDmF_Xs5XyJn8pYPjIIHYZKIsZapzNMglgN9lOCNdk1fZeC-ErDPPgEPyJeOHTg8CBwoh_FQh4NXHmMamenHm7I7C26ZA_dVZv1cUfy4jELOzCnuhEEGQTFYz2BdM0U36jTwpvsUNYm7WsI2lKj5gLDllQy5NgunPQTkqLSf_62UPfm9ArdujRGPfqbMHcb5TDmVgSQSPkhnUp2GMwpr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: دشمنان اگر برخورد نظامی را در پیش بگیرند پاسخی محکم می‌گیرند
🔹
وزیر خارجه در نشستی با سفرا و رؤسای نمایندگی‌های خارجی مقیم تهران: ایران در راستای دیپلماسی و پیدا کردن راه‌حل دیپلماتیک جدی است؛ همانطور که در دفاع از خود جدی است.
🔹
شرط‌های خود را برای بازگشایی تنگهٔ هرمز به وضوح برای همه توضیح دادیم؛ همهٔ این شروط منطبق با تعهداتی است که آمریکا باید بپذیرد.
🔹
اگر طرح ۷ روزه که به آمریکا ارائه شده است مورد پذیرش واقع شود، تنگهٔ هرمز مجددا بازگشایی خواهد شد.
🔹
اگر دشمنان ما مسیر برخورد نظامی را بخواهند مجددا در پیش بگیرند پاسخی محکم‌تر از گذشته خواهند گرفت و قوی‌تر از گذشته از خود دفاع خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/466191" target="_blank">📅 10:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466190">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHWga-2nMTdq10eFwis7_w2L9Xm0QfDwHosJ1UXtlMZ1BGZwT59NgXohLK2pVDXXgltFX1Qw3H9LAf6MzJYkQkFgkGnQ2p4DzfutSL1mxtk-CSL33-Jas3ANzwckiUOKfTFp2LOZAbztzZYeCUWF6YXdatKd07HcN6XQF4hPqpxknFMw0eq_tlafeIVX6hGIpTumdOcr5QqHFHM5j90ZH12zgmLTHMDNZftBJyjd6Qz54E98v6fQSqtHu0r7Sz9-quHgjFk6kmIrFxZDXw6oL_qJhTyo_SJTxK6pzHOQQqaIvZHK72SGkvJFZmsSHyzOQ74ppMKkPEufLDEHxFgejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی شهرداری تهران: اقلام دیگری مثل مرغ، رب و پنیر به طرح «تورم صفر» اضافه خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/466190" target="_blank">📅 10:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466189">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترک فعل بانک‌مرکزی به دادسرا ارجاع شد
🔹
دیوان محاسبات کشور: طبق آخرین ماندۀ اعلامی، معادل ۷.۹ میلیارد دلار از عواید ارزی حاصل از صادرات در حساب‌های کارگزاری، تراستی و پوششی مرتبط با ۱۸ بانک عامل در داخل کشور بوده است.
🔹
تأخیر در دسترسی به این وجوه باعث شده حدود ۸۵ درصد حجم معاملات مرکز مبادله، از ابتدای تأسیس تا مرداد امسال، با تأخیر زمانی بین بانک‌ها کارسازی مالی شود.
🔹
یافته‌های دیوان محاسبات حاکی از ضعف در سازوکارهای رهگیری و نظارت بانک مرکزی بر جریان منابع ارزی است. ترک فعل بانک مرکزی در این خصوص به دادسرا ارسال شده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/466189" target="_blank">📅 10:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466188">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کشف ۹۲ تن برنج احتکارشده در جنوب تهران
🔹
رئیس پلیس امنیت اقتصادی تهران: ۹۲ تن برنج احتکارشده در شهرری کشف شد. در ۴ ماه اخیر ۵۹۶۵ تن انواع کالای اساسی از جمله برنج و روغن و قندوشکر و حبوبات کشف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/466188" target="_blank">📅 10:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466187">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGRZ19uez7FQ_8oPJZA99AmCclrS_V165RA3gkC_uCWwMG9pSo91driTRAsDQSSWCMKfpfBmCIdq6px3D-0Ct5DK3cQ_R5m6GUMjic-IPP69CbFcImM1CT6m45n_upUu2IyeEAsXdMUFf_fJpZzOwPvzXl9BV7BSum5_eOwuDjUaCeOB536hOF5ld84hLh_UJ7T-n_y8A9IP0JXrZWTQH7LD5QaD40CP_EII1DngsaCBOHQmeG3ZdhvuipTJQRpX3OLwH8AiYtnsOoItiMvIaR6oGR86Tx2UC7cPY7r1vRR2xBhxTQQJpm1RlN4c7BUtvEZq_YN_ZqztJxJ7mMbtFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌های جدید ارز در مرکز مبادله اعلام شد
🔹
دلار: ۱۷۵٬۷۵۴ تومان
🔹
یورو: ۱۹۷٬۸۱۳ تومان
🔹
درهم: ۴۷٬۸۵۶ تومان
🔹
یوآن: ۲۶٬۲۱۰ تومان
🔹
روبل: ۲٬۱۰۵ تومان
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/466187" target="_blank">📅 10:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466186">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5fdf314.mp4?token=tryrZrKaOp28fCz5KQMXuU0pQUPsmpVeMufJ2mqwVR_jQid3bfStbEAI52BC93ni1jk1_xE6ymA-1vJZ71fk-5hg8WmMGfDP34D5mQ4YBEnxsrbuSxh1IG9Ki24BV7Xv69B1prU1jy54VjkdsJNM6mBkRGL-LP2T5yrT1PPDO6QNwsrQFzKIJi31MwnY5j3BoUYxEUV9J8gzAFGe4kjLeco-eyxVqfkDTUTGlgB8o2sy9z_RruUqtFlvSeGu8muwSGYpJsW_tTNncuG_Fy8BI48M3ZLqbdYu9UXt0meLWA0HsFs4pytbVNG2ifuFqs9Z4YhB5zY68ZPmCqoplCZxZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5fdf314.mp4?token=tryrZrKaOp28fCz5KQMXuU0pQUPsmpVeMufJ2mqwVR_jQid3bfStbEAI52BC93ni1jk1_xE6ymA-1vJZ71fk-5hg8WmMGfDP34D5mQ4YBEnxsrbuSxh1IG9Ki24BV7Xv69B1prU1jy54VjkdsJNM6mBkRGL-LP2T5yrT1PPDO6QNwsrQFzKIJi31MwnY5j3BoUYxEUV9J8gzAFGe4kjLeco-eyxVqfkDTUTGlgB8o2sy9z_RruUqtFlvSeGu8muwSGYpJsW_tTNncuG_Fy8BI48M3ZLqbdYu9UXt0meLWA0HsFs4pytbVNG2ifuFqs9Z4YhB5zY68ZPmCqoplCZxZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: اصلاح اساسی وضعیت معیشت پرسنل شریف فراجا یک اولویت قطعی است
🔹
مجلس تقویت همه‌جانبۀ‌ بنیه‌ انتظامی، از جمله تجهیز پلیس به فناوری‌های روز و اصلاح اساسی وضعیت معیشت پرسنل شریف فراجا و دیگر نیروهای مسلح را یک اولویت قطعی می‌داند.  @Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/466186" target="_blank">📅 09:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466185">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImZw_tZvM-k_dp9lzra59iuZYYiCvdLNPByYq266h36SW5D5J9nbaKh-DwvP1JrudOy5sWVUmK9RSjAd8iaNzwNkFMZcdjxjxzycUm7_yKiDbehYBuhybQzLyXf9wHC0su6z76lwd6nWO2EK85ODqrUflz2jCPX_v7otcqNS3rMykUzFDWNauuif0B42i_VCgUlt_FTIgwPa35FO_LCtOfjz2QGx21KZCUlYN0ufI2W_s6-4vzHmf1CfD_5IrqwIz1mZDFukUFkItqIjwx7rpn2pTRQQZE9u8UguyRHC1Zrm-SdfrqR9aB-98n0NbFdIg0ad1IrkTbqQpOv45pmkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجری آمریکایی: ادعای تروریستی‌بودن حادثه فلای‌دبی بی‌مدرک است
🔹
مجری شبکه آمریکایی «پی‌بی‌اس» با زیر سؤال بردن اظهارات دونالد ترامپ و بنیامین نتانیاهو درباره انگیزه حادثه فلای‌دبی، تأکید کرد که هیچ مدرکی برای اثبات انگیزه تروریستی ارائه نشده است.
🔹
«جف بنت»، مجری برنامه «PBS NewsHour»، پنجشنبه‌ شب در گفت‌وگو با «ژولیت کایم»، مقام پیشین دولت‌های کلینتون و اوباما، به اظهارات امارات متحده عربی درباره بررسی احتمال «فعالیت تروریستی یا برنامه‌ریزی قبلی» اشاره کرد و از کایم پرسید در شرایط فعلی درباره انگیزه این اقدام چه چیزی را می‌توان با مسئولیت‌پذیری بیان کرد.
🔹
کایم نیز در پاسخ گفت پس از هر بحران، حادثه تروریستی یا فاجعه، معمولاً خیلی زود روایتی شکل می‌گیرد که اغلب به دلایل سیاسی مطرح و تقویت می‌شود.
🔹
او گفت: «فکر می‌کنم فعلاً باید این مسائل را کنار بگذاریم، چون چنین اتفاقی معمولاً رخ می‌دهد. انتخابات در پیش است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/466185" target="_blank">📅 09:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466183">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f35df4ad.mp4?token=INbylFIpZnGFHiQRHKQ5Zh8n8wHBEqEYRgLs1d3Xagmbj626q_DAVLBumqNaq362SgbOocNVjH-KQggJn0GlNCGdjQBCL7YX6qsjJezCni2bwgcwICt7BliGBK0ylIXdmqaO93N1B1v7Ut96wngDAM2X7cr0zr8ddgEnOyp5ToZQGkOKocaVuvpg_bKRhknXlO5h2_Ehv_rd2tZwGOtL3ij0BmIkJ4VqPguyoGyFcBUfsW816mmq68kX3Bo5sRF9J0JVeyuo4fXaDNJnGeXiCXJbxLSf7Hn4PwabiuLv5IfOBIuMXbx-fhemB6KYvIpnd1iN9viLSHXFq0NbiYj5rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f35df4ad.mp4?token=INbylFIpZnGFHiQRHKQ5Zh8n8wHBEqEYRgLs1d3Xagmbj626q_DAVLBumqNaq362SgbOocNVjH-KQggJn0GlNCGdjQBCL7YX6qsjJezCni2bwgcwICt7BliGBK0ylIXdmqaO93N1B1v7Ut96wngDAM2X7cr0zr8ddgEnOyp5ToZQGkOKocaVuvpg_bKRhknXlO5h2_Ehv_rd2tZwGOtL3ij0BmIkJ4VqPguyoGyFcBUfsW816mmq68kX3Bo5sRF9J0JVeyuo4fXaDNJnGeXiCXJbxLSf7Hn4PwabiuLv5IfOBIuMXbx-fhemB6KYvIpnd1iN9viLSHXFq0NbiYj5rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: ۷ شرط ایران محقق نشود تنگۀ‌ هرمز باز نخواهد شد
🔹
این فقط صهیونیست ها نیستند که‌ در استیصال و درماندگی‌ گرفتار شده‌اند، آمریکایی ها نیز در مقابل ایستادگی و مقاومت ملت ایران مستاصل گشته‌اند.
🔹
آمریکایی ها که در رسانه‌ها حرف دیگری می زنند، اخیراً…</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/466183" target="_blank">📅 09:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466182">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76509c10a.mp4?token=UEEz0at0DlR6qR-rEsBgz8ek3uv75PfDFEOyaf0yQOElG7onpFw-WqO_D6HAB-3DekCiZfC3Dk0eW6Y-D-_PX9lCwBgLEhAsafecQLtfN9R7SnE7QxyPxWRlYH1VXYE9GpViBStN_AyxYPUhl5AxYzVE8MAQUwP5TpId_Ef1xzV5vSYhcwJO0aqDasM7eS-jh0xJVs0h_-EyAKq9qFbn5tYQeu63AraK1gv099t-zN5PGd0sCZLOblFwAb1FCFEBGQFAGUpvBe4hdUu1Mu6kPlYeKFglQlX6DlAKc4hTokqfeFwqKigpO51aB278uqj74m6Mpvy6NGBK5wjtIAO_Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76509c10a.mp4?token=UEEz0at0DlR6qR-rEsBgz8ek3uv75PfDFEOyaf0yQOElG7onpFw-WqO_D6HAB-3DekCiZfC3Dk0eW6Y-D-_PX9lCwBgLEhAsafecQLtfN9R7SnE7QxyPxWRlYH1VXYE9GpViBStN_AyxYPUhl5AxYzVE8MAQUwP5TpId_Ef1xzV5vSYhcwJO0aqDasM7eS-jh0xJVs0h_-EyAKq9qFbn5tYQeu63AraK1gv099t-zN5PGd0sCZLOblFwAb1FCFEBGQFAGUpvBe4hdUu1Mu6kPlYeKFglQlX6DlAKc4hTokqfeFwqKigpO51aB278uqj74m6Mpvy6NGBK5wjtIAO_Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ایران سیاست کلان و امنیت ملی‌خود را با توییت‌ها یا مصاحبه‌های روزانۀ مقامات آمریکایی تنظیم نمی‌کند
🔹
آنها این صراحت و قاطعیت ما را به خوبی می شناسند و با گوشت و پوست و استخوان درک کرده اند اما برای آن که افکار عمومی داخلی خود و مردم دنیا را فریب…</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/466182" target="_blank">📅 09:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466181">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fcde6921f.mp4?token=O_NB6ZR9sq9ZVlTNx1lDYE6EVGlhT67IeRoUOl4Wvxg8_-ilsKlWV5xbR93bglANnYr38nznMyz6PFU42AVEsc8gleZgoyAmrokQawOclbjlcrte2BXvHYIM4PUkmTUL0HN4ojCHn96orYUWgCvWZRaTDoGTawwexm2mr54uooo0WZ7B8nOyYjB7_Mgk1ecLSrMam_kMghsLjh4hBqScGsT_vDqXMKloLpwbukNi5PdfRg7wMaGHogr7f7zER3sc_y0JXDw4gt-yAuXemWapxox_mmQtVX73RTWliD8CglFzId61lRGVtbARxJJ6GYgU0Hzq7Q9UN0EAYbG1vLAj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fcde6921f.mp4?token=O_NB6ZR9sq9ZVlTNx1lDYE6EVGlhT67IeRoUOl4Wvxg8_-ilsKlWV5xbR93bglANnYr38nznMyz6PFU42AVEsc8gleZgoyAmrokQawOclbjlcrte2BXvHYIM4PUkmTUL0HN4ojCHn96orYUWgCvWZRaTDoGTawwexm2mr54uooo0WZ7B8nOyYjB7_Mgk1ecLSrMam_kMghsLjh4hBqScGsT_vDqXMKloLpwbukNi5PdfRg7wMaGHogr7f7zER3sc_y0JXDw4gt-yAuXemWapxox_mmQtVX73RTWliD8CglFzId61lRGVtbARxJJ6GYgU0Hzq7Q9UN0EAYbG1vLAj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: براساس راهبرد اقتدار و عقلانیت، نه هیجان‌زده می‌شویم، و نه مرعوب
🔹
آمریکایی‌ها که در رسانه‌ها حرف دیگری می‌زنند، اخیراً از طریق میانجی، پیشنهادهایی مطرح کرده‌اند. اما باید متوجه باشند که دوران فرسایش زمان و دیکته‌ کردن مطالبات یک‌طرفه گذشته است…</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/466181" target="_blank">📅 09:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466180">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11346e2d9b.mp4?token=BDgrlqpTtJzzcbkSRIJLhyaZLOVH6KWb5yRIIfJr1IqSD2OfNkgMxTJlklKxIWhP0_w5g3vadSfxx2nBo4b1NkJabb8nDpuUUF-_iGBq_LB4blL3_BaVjXDBW-UP842zb2CG8inA_jpMA-UR40bIbBt5s9hrIUa7PrR_cOMdTPEz6A2G8TE3f_Udt5NwXyZVitRpqZ36XciueSGXgXPIOaTid23nquXrZg2g9IC6NWEd3y-I3iwrHrJBm0usK40SB90abRFS3mOy1DPUS6EWKv2oByZe5bL6ODKp6gZVNj4M2x-jfMjj82MMD9-glxTBPhtazInpEqemE90CuNTnvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11346e2d9b.mp4?token=BDgrlqpTtJzzcbkSRIJLhyaZLOVH6KWb5yRIIfJr1IqSD2OfNkgMxTJlklKxIWhP0_w5g3vadSfxx2nBo4b1NkJabb8nDpuUUF-_iGBq_LB4blL3_BaVjXDBW-UP842zb2CG8inA_jpMA-UR40bIbBt5s9hrIUa7PrR_cOMdTPEz6A2G8TE3f_Udt5NwXyZVitRpqZ36XciueSGXgXPIOaTid23nquXrZg2g9IC6NWEd3y-I3iwrHrJBm0usK40SB90abRFS3mOy1DPUS6EWKv2oByZe5bL6ODKp6gZVNj4M2x-jfMjj82MMD9-glxTBPhtazInpEqemE90CuNTnvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: براساس راهبرد اقتدار و عقلانیت، نه هیجان‌زده می‌شویم، و نه مرعوب
🔹
آمریکایی‌ها که در رسانه‌ها حرف دیگری می‌زنند، اخیراً از طریق میانجی، پیشنهادهایی مطرح کرده‌اند. اما باید متوجه باشند که دوران فرسایش زمان و دیکته‌ کردن مطالبات یک‌طرفه گذشته است و موضع جمهوری اسلامی ایران کاملاً شفاف و قطعیست و تا زمانی که هفت شرط ما بر اساس تفاهم نامه اسلام آباد، محقق نشود تنگه‌ی هرمز باز نخواهد شد.
🔹
ما براساس راهبرد اقتدار و عقلانیت، نه هیجان‌زده می‌شویم، و نه مرعوب؛ هم می‌جنگیم و هم مذاکره می‌کنیم؛ هم با تمام توان در میدان نبرد نظامی حضور داریم و او را با شگفتی‌های جدید مواجه خواهیم کرد، و هم از ابزار دیپلماسی و برای تثبیت برتری خود در میدان نظامی و تحمیل حقوق ملت ایران، استفاده می‌کنیم، بارها گفته‌ام کسی در میدان مذاکره پیروز است که خود را برای جنگ آماده کرده باشد.
🔹
امروز به فضل الهی، جمهوری اسلامی ایران و جبهه‌ مقاومت در اوج صلابت، قرار دارد و کشور در نهایت اقتدار میدانی و انسجام ملیست و ذیل رهنمودهای رهبر معظم انقلاب اسلامی، هرگز اجازه نخواهیم داد توهمات دشمنان درباره‌ ایران عزیز ما محقق شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/466180" target="_blank">📅 09:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466179">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌ قالیباف: موفقیت کاروان «فرشتگان میناب» نشان از غیرت فرزندان ایران است
🔹
کسب ۱۹ مدال طلا، ۱۸ مدال نقره و ۱۵ مدال برنز توسط کاروان پرافتخار ایران که با عنوان «فرشتگان میناب» در بازی‌های آسیایی ناگویا حضور یافته بود، برگ زرین و سند زنده‌ای از اراده و غیرت فرزندان…</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/466179" target="_blank">📅 09:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466178">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در شوشترِ خوزستان
🔹
فرمانداری شوشتر: درپی امهای  مهمات‌ در شهرستان تا ساعت ۱۲ امروز، احتمال شنیده‌شدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/466178" target="_blank">📅 09:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466177">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🖼
پایان کار کاروان ایران در بازی‌های آسیایی با رتبۀ ۶
🔹
کاروان ورزشی کشورمان با کسب ۱۹ مدال طلا، ۱۸ نقره و ۱۵ برنز در جایگاه ششم جدول توزیع مدال‌های بازی ‌های آسیایی ایستاد و به کار خود پایان داد.
🔸
در دورۀ  قبلی بازی‌های آسیایی یعنی ۲۰۲۲ هانگژو، کاروان ایران…</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/466177" target="_blank">📅 09:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466176">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPb2zNd1LSk-O8E9QUmsKo29MhQ2nYVNElWPARe1rFe6AKPIIdhBdZXvsQAcMKz5petxksfE4QjzlxBaxhzvhhIPZ9XhTyxyPY-7HqDQ6qbGG1stNjUXM3QTvrzfEbEo8d95j5NllLeAoU3quaVLo3gjp0QD-hNyARcOTTWKcPrT7SQOxQKhgJsl9Ru7NZ1MTJu-X5DAlcqKL0EQPORacxbYxmhzTE5o4JCJYbCngj7OQPpssdevMXUdv7rprZlzxnBxckIpFE59dx_VZm4Ebv4jBLb7o0c9y1CVXILG_d_kWmci4Oee0jD9zK3mWxQYFPN_kh1TEqWVklXwlqpIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاصرهٔ داخلی، ترخیص کالاهای اساسی را متوقف کرد
🔹
تمدیدنشدن مصوبات ستاد مقابله با تحریم، ترخیص کالاهای اساسی بدون کد ساتا را از پایان شهریور متوقف کرده و محموله‌هایی مانند روغن، ذرت و جو در بنادر کشور دپو شده‌اند.
🔹
این درحالی‌ است که رهبر انقلاب صریحاً دستور داده‌اند کالاهای اساسی به‌هیچ‌عنوان نباید در گمرکات کشور بمانند.
🔹
همچنین تمدیدنشدن مصوبهٔ قرنطینهٔ محصولات گیاهی، امکان پذیرش مجوزهای صادرشده از کشورهای ثالث را از سازمان قرنطینه گرفته است.
🔹
در نتیجه، با وجود عبور کشتی‌ها از محاصرهٔ خارجی و ورود به کشور، امکان ترخیص محموله‌ها وجود ندارد و عملاً محاصره از داخل شکل گرفته است.
🔹
ادامهٔ این وضعیت می‌تواند به انباشت کالاهای اساسی در بنادر و کمبود آنها در بازار منجر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/466176" target="_blank">📅 08:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466175">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa91103df0.mp4?token=s025QiUbwRm8SHvF04P-65Ap9oY7Z9dlkwSYw6RxzOcohe0UzhdOOCk-G-d_4DP9qDX1V7fdVueyjqTeJIXczwo-X_9Y25jnp0_D57a1JvXbEuptU1fvZ8TQ8qX6sZnJtWfpz5lzEAHsUy_zzmvM4MLNozQOg9D_fnWNGrPtTv4rT40Qf8r49qisxPxrMjn0uhrnz_RaVvuvZe6Tq_NvvUjBCJsPwBcwOk_umcHQZNvmYNz-V8gqlgHPHc_-qiXtCBnCaHHafW2ONTHz1hWfLJff88wWpvCoLFSCLOK5J4yFccA39cJab7zeviy7XM7oe7MHVcn6nRwBAB8yi2e26A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa91103df0.mp4?token=s025QiUbwRm8SHvF04P-65Ap9oY7Z9dlkwSYw6RxzOcohe0UzhdOOCk-G-d_4DP9qDX1V7fdVueyjqTeJIXczwo-X_9Y25jnp0_D57a1JvXbEuptU1fvZ8TQ8qX6sZnJtWfpz5lzEAHsUy_zzmvM4MLNozQOg9D_fnWNGrPtTv4rT40Qf8r49qisxPxrMjn0uhrnz_RaVvuvZe6Tq_NvvUjBCJsPwBcwOk_umcHQZNvmYNz-V8gqlgHPHc_-qiXtCBnCaHHafW2ONTHz1hWfLJff88wWpvCoLFSCLOK5J4yFccA39cJab7zeviy7XM7oe7MHVcn6nRwBAB8yi2e26A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از امروز خنکیِ هوا در تهران کاملا حس خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/466175" target="_blank">📅 08:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466174">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8538ad4b03.mp4?token=A60ntukVy5z2LC1C26ka8QHUpn_NEDHfXlpPmLA_gOnKP0p8Ee22c2tXv_I4FXnq771PhRJ3j6bgNEAhVU9jLpgWN7mhLlGn7crJ3r2mn28bkUpb_ANEKJQLZjzEGtNqBFlfpTOwkl8ZZFPPuKStkecoDbj6e9-CRC_7EVQC469JmkNzj6hIizInB7lLfsDnkaEXQW5Lf0MAA7HxURxiW2WNrsapxB7HDUp6Ll0GciwMSvkIn0VvwhFXuzmMDTSQtfrm2QLtsKQmxk5y5aPZKH4QLCLCBog7jtV8pYP4d5ODnhMU35KgPBTngq9xVlINwq-DfsEjEvBNTVbA3nU7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8538ad4b03.mp4?token=A60ntukVy5z2LC1C26ka8QHUpn_NEDHfXlpPmLA_gOnKP0p8Ee22c2tXv_I4FXnq771PhRJ3j6bgNEAhVU9jLpgWN7mhLlGn7crJ3r2mn28bkUpb_ANEKJQLZjzEGtNqBFlfpTOwkl8ZZFPPuKStkecoDbj6e9-CRC_7EVQC469JmkNzj6hIizInB7lLfsDnkaEXQW5Lf0MAA7HxURxiW2WNrsapxB7HDUp6Ll0GciwMSvkIn0VvwhFXuzmMDTSQtfrm2QLtsKQmxk5y5aPZKH4QLCLCBog7jtV8pYP4d5ODnhMU35KgPBTngq9xVlINwq-DfsEjEvBNTVbA3nU7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استرس چطور معده را به‌هم می‌ریزد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/466174" target="_blank">📅 08:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466173">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فعالیت ادارات و مدارس کرمان با یک ساعت تأخیر آغاز می‌شود
🔹
مدیریت بحران استانداری کرمان: با توجه به افزایش آلایندگی هوا در شهر کرمان و بخش‌های چترود، ماهان و شهداد، فعالیت ادارات و مدارس این مناطق در روز یکشنبه ۱۲ مهرماه با یک ساعت تأخیر نسبت به زمان معمول…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/466173" target="_blank">📅 07:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466172">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هوای تهران «پاک» شد
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۴۷، و در وضعیت پاک قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/466172" target="_blank">📅 07:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466170">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">۲ کشته و یک مفقود در سیلاب‌ اخیر استان گلستان
🔹
هلال‌احمر گلستان: از چهارم تا یازدهم مهرماه، ۹ حادثهٔ سیل و آبگرفتگی در گلستان به وقوع پیوسته که متأسفانه ۲ نفر فوت و یک نفر مفقود شده است.
🔹
عملیات امدادرسانی و جست‌وجو برای یافتن فرد مفقود همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/466170" target="_blank">📅 07:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466169">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آخرین وضعیت فعالیت امروز مدارس و ادارات
🔸
مدارس نوبت صبح شهرستان ایذهٔ
استان خوزستان به‌دلیل بارش شدید باران، آب گرفتگی معابر و ورود آب به ساختمان‌ها غیرحضوری است؛ کلاس‌های نوبت عصر طبق روال عادی برگزار می‌شود.
🔹
فعالیت تمامی ادارات و مؤسسات، بانک‌ها، مدارس، دانشگاه‌ها و مراکز آموزش عالی در بخش مرکزی
کرمان، رفسنجان، انار، زرند، راور و بخش‌های چترود، ماهان و شهداد
، تعطیل است.
📺
درصورت هرگونه تغییر، این لیست به‌روزرسانی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/466169" target="_blank">📅 06:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466168">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX5z3ejEqEhXZEkcdjsX-OxtTC7d6oRJ453o03xvXIdNEQFWx0pl5vgYtqjEOAFxffR-1xyT3Iox3VtBBfzCdcOW73Y-H6Hak6Clu54mTnEUeMgg188ugBfaTOA5TCdruMC74KQSCYfLH-zRTQVlzp4-ZabA8zXd6pGPD-PvGNxsABfrGwcsVVQjpRIZEunfB4ODCI6P2Tbvccqim7rTqekF3z6iWvvXpYddYtX46mDBK0kpBVZLEMXWnekMMtiEZjT3MAE70fyJoxQCeasjDZoMfI2sgvtywap8lcadpRs8OE2X099lfxqKm2BZa4FBEt7Qpk17rznfcFthFCdXhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: رابطه‌ام با کیم‌جونگ‌اون خوب است چون ۱۱۲ بمب اتم دارد
🔹
رئیس‌جمهور تروریست آمریکا: من ارتباط بسیار خوبی با کیم‌جونگ‌اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای دارد، خوب است که روابط خوبی با آن داشته باشی. اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای نخواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/466168" target="_blank">📅 06:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466167">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فعالیت ادارات و مدارس کرمان با یک ساعت تأخیر آغاز می‌شود
🔹
مدیریت بحران استانداری کرمان: با توجه به افزایش آلایندگی هوا در
شهر کرمان و بخش‌های چترود، ماهان و شهداد
، فعالیت ادارات و مدارس این مناطق در روز یکشنبه ۱۲ مهرماه با یک ساعت تأخیر نسبت به زمان معمول آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/466167" target="_blank">📅 06:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466166">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSqDifTzsBgbglWxrWbEVXa1p2_68_sG5m_NAQSrpPRgLdlcPdf32rBphWgj8rSpW2dvGqrl3fE12r_CVLzA4XBzem8ValccFaLGUBk47OwTS7YbmpiXaxZ_IWds4Sum0Lreva9Vuf5LU07lVeeLa5_F3dlXhMdDI1z3pZfEUELhLkXf3eG3pR5wvZ8rS_-yxZAix_5WQUCFuipqiJgTBFN1osjAY8novSciRNmGopkNlZq_XvtwRjAdcafxMNE64LaqS4R9goRulADbORXMyX9bATr9GLRm9-EUtYwoIZAiPn1GCdT8Wav8RpashC7xn57A28sm9WzjM3tYG5z3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۸ درصد روستاهای دارای جمعیت به زیرساخت‌های اصلی مجهز شده‌اند
🔹
رئیس بنیاد مستضعفان: امروز بیش از ۹۸ درصد روستاهای دارای جمعیت از عناصر و زیرساخت‌های اصلی برخوردارند.
🔹
در بسیاری از این مناطق ظرفیت‌های فراوانی وجود دارد که اگر درست مورد استفاده قرار گیرد، می‌تواند به بهبود شرایط زندگی مردم کمک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/466166" target="_blank">📅 03:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466165">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کویت تابعیت ۴۱۵ نفر دیگر را لغو کرد
🔹
کویت با صدور ۶ فرمان جداگانه، تابعیت ۴۱۵ نفر و برخی افرادی را که تابعیت خود را از طریق آنان به دست آورده بودند، لغو کرد.
🔹
در متن این فرمان‌ها که در روزنامهٔ رسمی کویت منتشر شده، دلیل مشخصی برای سلب تابعیت افراد اعلام نشده است. بر اساس مفاد فرمان‌ها، معاون اول نخست‌وزیر و وزیر کشور کویت مسئول اجرای این تصمیم‌هاست و فرمان‌ها از تاریخ صدور لازم‌الاجرا هستند.
🔹
این تصمیم در شرایطی گرفته شد که کشورهای عربی حاشیهٔ خلیج فارس پس از جنگ علیه ایران، اقدامات امنیتی خود را علیه افرادی که ادعا می‌شد با ایران همکاری کرده‌اند را تشدید کردند.
🔹
کویت پیش از این روند سلب تابعیت‌ صدها نفر را آغاز کرده و در خردادماه تابعیت ۲۱۹۳ نفر را لغو کرده بود.
🔹
جنگ علیه ایران باعث شده است کویت که یک دموکراسی نصفه‌ونیمه را در بین کشورهای حاشیه خلیج فارس بنا کرده بود، تعارف را کنار گذاشته و عملا به سمت یک دیکتاتوری خفقان‌اور روی بیاورد.
🔹
یک مقام ناراضی امنیتی در خردادماه گذشته به مجله اکونومیست گفته بود انگار سرطان تمام کویت را فرا گرفته است. همهٔ ما مظنون به شمار می‌رویم.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/466165" target="_blank">📅 03:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466164">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab3c92a656.mp4?token=O-wDIngpgxe82MRchT3xgx6FuySRz06xzouRDwBdAq2DykX-HTPDl4MXeUJLxRkte01-IqDavCcwaHsYh357uAttOZppq-ZHotWtMtKyG6DK3j5WBC6TIwEZWujGKs4LmJSFrqYJrWAVhfLWySWD6nNLyc4IMnz4EDeUN3kDfJHCaMVUW6v6cPN-qUHImBChs234HcphGMh72rJeRMHE2qSCN14ZFgoV-L2o-jvSAYFaGo-b-Ufn35BF6STFOE4gAzq55UP0Nesu6XQ0m2y8E6uNMnuNYeP1Zbq4vxmNChVMCGa46V9gn4Va8wMh6u6jgDIJO_goej_KDaUQHf1OUDkbOmE8doWHT332B9WPFHPK3Keg1j-Iejvfq0ecUwkuMmt-SwvBDRnkvYRdpjX_fa_T7ujIMLYMX6pMpRVgTiFTvDd-6oJ7tXVv0_1w0QYqEtLzDUW8IiAB3BBYzU5rwfQacgey0C2D8_CYqUs6RXtOs3i5Qhoy3trWZ1Q1QgASvZbqmRQs5r71XMOb67MXg50uO5PW-HOl1ZbuR1d1GuWqwjXTz9c7UuO3lCEKtYcy7hNhLnpIyZL2GdjLTMsol7WTPziPOLlIA_rMh8--R1GNn6w77YM61nzliBZetyH5Md68SSppA5saStSc1FaTeKy9sxBTgqB9JsmYBjrcn6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab3c92a656.mp4?token=O-wDIngpgxe82MRchT3xgx6FuySRz06xzouRDwBdAq2DykX-HTPDl4MXeUJLxRkte01-IqDavCcwaHsYh357uAttOZppq-ZHotWtMtKyG6DK3j5WBC6TIwEZWujGKs4LmJSFrqYJrWAVhfLWySWD6nNLyc4IMnz4EDeUN3kDfJHCaMVUW6v6cPN-qUHImBChs234HcphGMh72rJeRMHE2qSCN14ZFgoV-L2o-jvSAYFaGo-b-Ufn35BF6STFOE4gAzq55UP0Nesu6XQ0m2y8E6uNMnuNYeP1Zbq4vxmNChVMCGa46V9gn4Va8wMh6u6jgDIJO_goej_KDaUQHf1OUDkbOmE8doWHT332B9WPFHPK3Keg1j-Iejvfq0ecUwkuMmt-SwvBDRnkvYRdpjX_fa_T7ujIMLYMX6pMpRVgTiFTvDd-6oJ7tXVv0_1w0QYqEtLzDUW8IiAB3BBYzU5rwfQacgey0C2D8_CYqUs6RXtOs3i5Qhoy3trWZ1Q1QgASvZbqmRQs5r71XMOb67MXg50uO5PW-HOl1ZbuR1d1GuWqwjXTz9c7UuO3lCEKtYcy7hNhLnpIyZL2GdjLTMsol7WTPziPOLlIA_rMh8--R1GNn6w77YM61nzliBZetyH5Md68SSppA5saStSc1FaTeKy9sxBTgqB9JsmYBjrcn6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ریشهٔ بدحالی ما کجاست؟
🎙
آیت‌الله فروغی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466164" target="_blank">📅 03:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466163">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">منابع خبری از توقف پروازها در فرودگاه شهر ریاض عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/466163" target="_blank">📅 02:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466162">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الجزایر نیز خواستار میانجی‌گری برای تنگهٔ هرمز شد
🔹
رئیس‌جمهور الجزایر ضمن انتقاد شدید به امارات متحدهٔ عربی و بیان اینکه ابوظبی از شورشیان الجزایر حمایت می‌کند، گفت که حاضر به میانجی‌گری برای موضوع تنگهٔ هرمز است.
🔹
او مدعی شد کشتی‌های الجزایری بدون هیچ مشکلی از تنگهٔ هرمز عبور می‌کنند و الجزایر با هیچ‌کس مشکلی ندارد.
🔹
وی با اعلام آمادگی الجزایر برای مشارکت در تلاش‌های میانجیگرانه در تنگه هرمز گفت که هر کس درخواست میانجی‌گری کند، ما حضور داریم؛ چه بزرگ باشد و چه کوچک.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466162" target="_blank">📅 02:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466161">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea12b8ce8.mp4?token=vw4DPP79f67GtO-Qx5VnWriZ3_9VHDPpALau8RbpO88caiUP7OrK8tk53jfBeAzyX1iq8ad3g4RlqhqAbXgDZYtsXqO4FbtMdCGrHZEmpYxrYT3U5mlfy9PJJsV6Jn8B23bP91nzYNcJP5z12oIiETa91wbWB0SwCIsHB988UZhClB5KlOmslYHL5J_-bxAVQERyhqFDqH91e69QAv4WffBocz-yDPHOAgM1qO0siXJGJAx5--MyK8khFH7W06DSdNkiVKIe_0grNoFXspp8McnSGumaASBTcBYLCUyBYsQ7bkv09zMuXd1WEqRnfSNL4wZrxm10uthDs6iB6L_Bpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea12b8ce8.mp4?token=vw4DPP79f67GtO-Qx5VnWriZ3_9VHDPpALau8RbpO88caiUP7OrK8tk53jfBeAzyX1iq8ad3g4RlqhqAbXgDZYtsXqO4FbtMdCGrHZEmpYxrYT3U5mlfy9PJJsV6Jn8B23bP91nzYNcJP5z12oIiETa91wbWB0SwCIsHB988UZhClB5KlOmslYHL5J_-bxAVQERyhqFDqH91e69QAv4WffBocz-yDPHOAgM1qO0siXJGJAx5--MyK8khFH7W06DSdNkiVKIe_0grNoFXspp8McnSGumaASBTcBYLCUyBYsQ7bkv09zMuXd1WEqRnfSNL4wZrxm10uthDs6iB6L_Bpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: با موشک بالستیک و پهپاد تاسیسات شرکت آرامکو در ریاض را هدف قرار دادیم
🔹
حملات ما دقیق و مستقیم بود و منجر به وقوع آتش‌سوزی در مکان‌های هدف‌گذاری‌شده شد. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/466161" target="_blank">📅 02:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466160">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba065d397.mp4?token=djJEOUBlyEIXyo2nUSNEyyLYLXqItpRNLU8z8o2XNdpWV5avL0WYVtB78938iBRbCjVvf3MzUACnVgQk_tY5Kj3gR8ng3s9o4LE97IacKp8wgBqyRB3mVgCu4Q5m5Se7sASzDvAxNY6tjm7GtRVrIM5M_EXZlklpSttvLO7gZ9m0F5RDenBsPJaQiIlnyz-W8EqQaPCoOj7k1gRkiI160fRolDKgPRCM9hT5O62Dqv4JHdwWP1LeggbU_HWSNgue5mndKxhhsyYO6vAvLHUwRQdCu1LcUuD7BwJiTi46p5P5_xmcy_KxySAASinIEY4WGvWpcPjBpSpO_Og-XBRjwg9eEBD3PEl0kPTu06xJop3A8oVxShYUsbr0sMlQ1wfC6FIabNCozl4xu33s2PpwJaFWjaV9FNl_5EaZPn0oj9f2Iorg_is6RS-4UjRgPcCuAdMZ9WPa1j6-sJ4b8ohsi1jWO2prX6SB4LFt144mck9XQF6eWVP1maTjqJ4JQgXBo7LECjiQcwmyIflSwK86i1nRvB22v6_EzqTxOjz5hGOvxy-7WUtFSKLLfuEPczdlqYjGp-KmQKj4zJAUSO0-1CXdy6BR9soAqnQ2bZ7Y81gXZuRSrZXAFfMaCZCwWrwfW0VwLh0VzHRqE5y40SQpscA-qpZ9Bc3vkrVhOAxo7to" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba065d397.mp4?token=djJEOUBlyEIXyo2nUSNEyyLYLXqItpRNLU8z8o2XNdpWV5avL0WYVtB78938iBRbCjVvf3MzUACnVgQk_tY5Kj3gR8ng3s9o4LE97IacKp8wgBqyRB3mVgCu4Q5m5Se7sASzDvAxNY6tjm7GtRVrIM5M_EXZlklpSttvLO7gZ9m0F5RDenBsPJaQiIlnyz-W8EqQaPCoOj7k1gRkiI160fRolDKgPRCM9hT5O62Dqv4JHdwWP1LeggbU_HWSNgue5mndKxhhsyYO6vAvLHUwRQdCu1LcUuD7BwJiTi46p5P5_xmcy_KxySAASinIEY4WGvWpcPjBpSpO_Og-XBRjwg9eEBD3PEl0kPTu06xJop3A8oVxShYUsbr0sMlQ1wfC6FIabNCozl4xu33s2PpwJaFWjaV9FNl_5EaZPn0oj9f2Iorg_is6RS-4UjRgPcCuAdMZ9WPa1j6-sJ4b8ohsi1jWO2prX6SB4LFt144mck9XQF6eWVP1maTjqJ4JQgXBo7LECjiQcwmyIflSwK86i1nRvB22v6_EzqTxOjz5hGOvxy-7WUtFSKLLfuEPczdlqYjGp-KmQKj4zJAUSO0-1CXdy6BR9soAqnQ2bZ7Y81gXZuRSrZXAFfMaCZCwWrwfW0VwLh0VzHRqE5y40SQpscA-qpZ9Bc3vkrVhOAxo7to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین سرسنگی؛ قهرمان میدان ورزش و میدان شهادت
🔹
این جوان دهه‌هشتادی و ورزشکار یزدی در راه مرزداری از وطن و دفاع از امنیت مردم ایران به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466160" target="_blank">📅 02:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466159">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">منابع خبری از توقف پروازها در فرودگاه شهر ریاض عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/466159" target="_blank">📅 01:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466156">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwcNuE_TA0vWJSfsD8Bqk-cI8YiqSazKBzec_eThuflZFIOlzDB74xa_7EYD5Q2kF2cvdtoBxO8H6x4oCRhGXNn1Hxw5RqLzqiH44wcr0a2DdKak8kYlbxwZIkaFJhBaNJ6mrdfjZ2WhaoTetLYHimIs2F3j4odSBGuTMwmMi9BZZzqWIh-9dcn_JTnkb0S88OfFAXrNPRuB2P3-kPhJz-EkUtM2p5id1FZbCV9S0GRG-3NfvkE0-kKsmcbfOYHJ3Qb1a1WNLG67ryglkORxEUUvJwAjE_IrZkHx5t27XLduv49jGPukwChwX40x1KIfeQqqh2FQqkVOHel_4AyTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clJ80LsuHHI8n1c0RCa1z1C3oTGmRvQq138ClV6kaeEA_5xiDxwHHfYsNeRHG_HzGF-pzUVkP324QFg7n1SpSZx9PDlHW0_dibY0H8IrATteFpsa_Q8bjMIpqyU_zvO3Y-e2P_vKinDDnqQ7Vjs0EvV4NqTsCENhrnCSwVUHVblMIPeXpxFWQw4ZJ4w93V_YxEgtSLkknwx4CLjja1rkbWCy5iNIPf-i-KSBo0w_D6mo73g6emC5y8f39fnpY1hTRSeEwmcbEswDqcNx7O8wyjMqmZtniDd2e41L2mseVhuuvn22fSXZGFHJxSioPlFyJAQnk8CVWENL2r0G1q5P-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQ30d-sj8NdtMlRhypjqiHVVscNoFcFqPpsvF-LX-_N8CJ3nE6gIXgFQC0Aj9QAFuTbdb2c4MQw7W-jegjq7KWJPAsiUkvcCufUjc3wAux2S8p6CIH-9vdVou9ZPzJkcUVEiF4wmDHwRBg1hnHq3yapczvLdGhhIXk3ktKgNlnGsXLEvbKAdolVFc87t1HP1M7YkBO9bR7P4c1ILSI3WLBsllvJrdMQPSjMr8Vm9qgywloV6Hj7dDZ7Sskm92tb_QVPRtKfW8e0lFrMVXGfA3FQez2bLP4RDlcbO1EZFMdGer2MeqU5fOz3Abs6pr2zb-a2fQVlyQRBTmUNvESNd6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تداوم اعتراضات دانش‌آموزی در فرانسه؛ ۵۰۰۰ نفر بازداشت شدند
🔹
دانش‌آموزان دبیرستانی در مناطق محرومِ حومهٔ پاریس، جرقهٔ یک جنبش اعتراضی را زده‌اند که به سراسر فرانسه گسترش یافته است.
🔹
به گزارش رویترز، این اعتراضات علیه فرسودگی مدارس، شلوغی کلاس‌ها، کمبود معلم و... در اقصی‌نقاط فرانسه برگزار می‌شود.
🔹
نیروهای امنیتی بیش از ۵هزار نفر را بازداشت کرده‌اند و برخی معترضان به‌شدت مجروح شدند. جراحت‌ها شامل آسیب چشمی، شکستگی دندان، ضربه به سر و... می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/466156" target="_blank">📅 01:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466155">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
سیلاب و آب‌گرفتگی شدید در ایذه
🔹
بارش‌ شدید باران در شهرستان ایذه استان خوزستان علاوه بر آب‌گرفتگی معابر، ورود آب به منازل و خسارت به شهروندان، موجب قطعی برق در برخی مناطق این شهر شد.
🔹
ادارهٔ برق ایذه اعلام کرد که تمامی اکیپ‌های عملیاتی علی‌رغم شرایط نامساعد…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/466155" target="_blank">📅 01:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466154">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">منابع عربی از حملهٔ نیروهای مسلح یمن به شهر دمام در عربستان سعودی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/466154" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466151">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmxWRlQKoe07kkOsDbQMSJt6pS3_6KnNXqvmg-bjXLC3X5XTyJE8YVMhrhgocwT2iucd3TDh8rv_cqXuQKUc1WMXcfUdWRKKs-1FOTwxIcIm899P4XYy2IQsWpr0AwJwge8wsmrFz7ov8Poqe6ns1pPvwaGYPTS95LMu0zAfnLIwe5h46yKjCvz6Vt44z_qixmhehAOQ1-qz36tiZ5ZRSlgBtlBWWne7EDWbR-PZhiwOX_duNX1CUskiVzfA_Lpd_xqlLc9tVqPapRDaaWy8e0vM4rYC-At_cdyZXtO53mzevKfOhvf-kgaCtzBgVIFER3rD97De1JtFKIDESAILmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l67fR0SWgASohK5dO2J7ev6xmc7bZu-UUB2tI5A9OYVzm7C-PLNFAJFEXhpUMaOtBPhzPyjjOpHAR2L_7v4OEQotUxPG-z92hndSOMKuolU1mEBDInitJlOkTy3rSMrqlzqD0VEpAjxnDtOyAxr7efcJ59eyRlJPjBQ5rfYW1VIxhsydyImuwxEs4PkXu6oiDd0E9DrcEzBrjpKThHwet9xM1OMKvByrhu4eg8mzBsqgEcqefeN52x50iCnkzwRXo7PMB7Mw6IixRkmg8GYBQn6yWcaJqRbHg1oKbIuEQ0fTRNuiDw5LTj7TSSNp48SITm9W3hFNwh7aAY4t3byVmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69445dd331.mp4?token=tMOQ3hUcxc6jT4P4b7VCUJggZAPDsUq5DZnGubLS_-l5QslXsH-_apSV49Depfglr_AIq9-U7mLSntzSHnRWmFaGZppltiYuR9I5nK_6jBDIkczjDRuObAAh0Sth6obMfKxz7ydE_fhtHcoM859GyrUUwMivJgmaBIuMtm9_d0QUZ_kAenwZ1dd-bpcxrDWek1BVKv_lZ4IIKUb7bJs-cAuAyubJvHZzYjEWge-AX5MpMjvq3tnrrbAC_QBBS9_THv5AH6syWkP_3jKINCK-YzV-y7zQMFlh5IRI7Q7XDeQhJ07f4ge7Lo6RSLoRk2ux8bm2jNvslLb1XAsdGdTjrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69445dd331.mp4?token=tMOQ3hUcxc6jT4P4b7VCUJggZAPDsUq5DZnGubLS_-l5QslXsH-_apSV49Depfglr_AIq9-U7mLSntzSHnRWmFaGZppltiYuR9I5nK_6jBDIkczjDRuObAAh0Sth6obMfKxz7ydE_fhtHcoM859GyrUUwMivJgmaBIuMtm9_d0QUZ_kAenwZ1dd-bpcxrDWek1BVKv_lZ4IIKUb7bJs-cAuAyubJvHZzYjEWge-AX5MpMjvq3tnrrbAC_QBBS9_THv5AH6syWkP_3jKINCK-YzV-y7zQMFlh5IRI7Q7XDeQhJ07f4ge7Lo6RSLoRk2ux8bm2jNvslLb1XAsdGdTjrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ بمباران صنعاء توسط جنگنده‌های سعودی
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/466151" target="_blank">📅 01:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466150">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
سیلاب و آب‌گرفتگی شدید در ایذه
🔹
بارش‌ شدید باران در شهرستان ایذه استان خوزستان علاوه بر آب‌گرفتگی معابر، ورود آب به منازل و خسارت به شهروندان، موجب قطعی برق در برخی مناطق این شهر شد.
🔹
ادارهٔ برق ایذه اعلام کرد که تمامی اکیپ‌های عملیاتی علی‌رغم شرایط نامساعد…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/466150" target="_blank">📅 00:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حملهٔ دوبارهٔ جنگنده‌های سعودی به پایتخت یمن
🔹
منابع یمنی از حداقل دو حملهٔ هوایی جنگنده‌های سعودی به شهر صنعاء خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466149" target="_blank">📅 00:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466146">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd3dfb4ffd.mp4?token=K049TxKY4dudeQm2g7HCyr6yICK5hgoFgQjVekBZkSQwy2yV7AQyTW4-2cIHbuZ5f70cNoChSRYL_4yZSSChyEiQQflCuLeaTD10JsGS5ox3L_bnJeVn_SVCwhWmXm5sp-EZBDXR-VmQKpltKSi-wzwaNsThwbTBJGpCSUDcT744USbfN-j52wv47oV79B-EWH_L34wr5L56BSxwSYJQvvFl3OQW6wb6rzy1wl2PxuPFI8Fx8qBf1lWFXg_mEN1P0ax0NBroQ0T80twPvT-8uuKCC6zMOvaMk6oJOKMaGD1mWRKPVl92r7eVGoMGJqsxTn6MG-UY9zYZFAjOQDfY1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd3dfb4ffd.mp4?token=K049TxKY4dudeQm2g7HCyr6yICK5hgoFgQjVekBZkSQwy2yV7AQyTW4-2cIHbuZ5f70cNoChSRYL_4yZSSChyEiQQflCuLeaTD10JsGS5ox3L_bnJeVn_SVCwhWmXm5sp-EZBDXR-VmQKpltKSi-wzwaNsThwbTBJGpCSUDcT744USbfN-j52wv47oV79B-EWH_L34wr5L56BSxwSYJQvvFl3OQW6wb6rzy1wl2PxuPFI8Fx8qBf1lWFXg_mEN1P0ax0NBroQ0T80twPvT-8uuKCC6zMOvaMk6oJOKMaGD1mWRKPVl92r7eVGoMGJqsxTn6MG-UY9zYZFAjOQDfY1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلاب و آب‌گرفتگی شدید در ایذه
🔹
بارش‌ شدید باران در شهرستان ایذه استان خوزستان علاوه بر آب‌گرفتگی معابر، ورود آب به منازل و خسارت به شهروندان، موجب قطعی برق در برخی مناطق این شهر شد.
🔹
ادارهٔ برق ایذه اعلام کرد که تمامی اکیپ‌های عملیاتی علی‌رغم شرایط نامساعد جوی در میدان حضور دارند و مشغول تعمیر تجهیزات آسیب‌دیده هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/466146" target="_blank">📅 00:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466142">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYMtuWGBqmwfOKLUSOxZcSbwP7yJVdc-RGGr3u0s18ICR3rT4W0eIxuEokiLXBzsUpo1gh7VQ4WH65s4beP9zI-fe6qDNGvUfwZ83pQdiYUlpVL7dML_dPdSo7QXNUKomb_ZKZgf4zOSw9sGCuwAz5jsfcoiPXDuftfP94-lzG3x0SpXdR7rfRr-lPiFkbhNC5-G5Wj-FYWSkJBCssv3vkHk2qt3QUqOfSTONyQoeeeRwaY4JMPBmaZqyMShn19Ioj74sPdcdoeUbWDq56lV2iS06x390zi5mktJv1TpVv1Ks9jdnfWKH8VB9jAjT1nstfbSIU_wA-IQkcRWml8HYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1_3_Y9eye0LNWeYeasYJFKcjLZnuoTDCqf8CoIyiXMwUEOqxb1Pl5i1riUkPcOO1PmKt26jz3xnUuVnX-G5kB4ewNp6aqjtPc6Q71RlObk4AQ48xztViF96D65ltbj0j47I8a2dDVtvfKhXO6rvVftOf2UqMiM4g6p2P2GwWKj5CojLwviPw3-MqgGmf-rrETXBAxJarGuIJJxKlft365Gr1Rfm5islGktVALugM9w-OrGh5KeFj0kxOuAHIW-ahDvVEGH78gz4T-IcU5BGXwE1_fXIS7y8Ss6Z0I0FXQ-BRESRtdp2yl6jXW-C42uZywK67GkPtm1q63-Aw4G22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN-abKFHLs8cckIPA_k16TNeLXSi1bWeHDh2J7p6PktARf7PEPlFiYtnWJ8O2YbsN5YgQXw6-3RrhGWkxDtr_uLbJLoUAbhbjPqISJoxl0g9zSYZbRbQc0f2eI9-D1qzs8mZSmIaaTib1p7NXX9rGQ9zowAUvnG9RFdiwWU0fY36DrbJRYIZw6xIu8TINcMnkO3kmmzYiB2-i97H2qoSE9JlFu0l9FjH0KD7Yte9AzPRp7BBW9pV_z6SeOaXE7SfeKpNCbkinBrjSMIfHB33M3y7AfbZeKNqJ_fyOZCvh3pIZk1SzLUVqd-ek7Lit2b3Rs7Ilkjovlq8A7crHtcfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERu3efl-cbWxmeYTBrSYzLFNe-POE0iAq4ZfhOJmauvKgOmDfwpgOjP5is6-JaPVzImjyRIy7PdNUBwBGSeVCS_xkrs0clwp0v_Pk7m5OEbWGZ1LFmQqGfQ53PXscTm_ccEFenrAW2k_7WqSt8BS3HecKevnTIm6dvujithUuoQlJKQPV5Cktx-xsixhvfTq_Ue9sv3UzOqV-qiWngUiGHkTFw5zw-RwMlaB2tBxzdPm6Hok-Fa26AbMyQFlCjCUflirpzXmn358pVANI5RGa-QoA9n3P_OnP5M5yqMw6EiWfqlA1qAUP2F-f60t6eZ2lPwms0DWOoIybG1IUMopNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر جدید از خسارات ایران به تجهیزات آمریکایی در عربستان
🔹
تصاویر ماهواره‌ای جدید منتشرشده از پایگاه هوایی «شاهزاده سلطان» در عربستان سعودی، ابعاد تازه‌ای از خسارت‌های واردشده به تأسیسات نظامی و هواگردهای آمریکایی مستقر در این پایگاه پس از جنگ با ایران را نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/466142" target="_blank">📅 00:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت ۶</div>
</div>
<a href="https://t.me/farsna/466141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۵ – سفرهای گالیور</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466141" target="_blank">📅 00:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1LPVgbucWoO6QuNXzOqJG3DWpDUyRXsBkFvLJC7Xmb6ZvFJN0vcLZE2jMXr3M-2W-MkAOqSD_9Ji1vHDqLTZOlcq7bDnzNtNIchRdD7hr5guMzE0_NXfJ65yOrApIX8H2yQVYet-977vouP_ZvXvsUcRu44uNwt2ChYgAHs7SbKXmI6k_fdiSS_d2u6ueSXow2-aY2cZmtPqCeonw6WAxTYmrn36bUyjc3U_ChqEyZcTPg7aCNZ8p9_3mBm6SSOP8YI7EYhkbNmGVQOHRPTXlRdiNT8J9e0X6JOKJTXoLOo5SDepSALBTe85ge8P5YD-SQjbGpJcfd5aC64ijmQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرنگی ناشیانه
🔹
مردی دندان‌درد شدیدی گرفت و پیش دندان‌پزشک رفت. پزشک گفت: «۲ سکه بده تا دندانت را بکشم.»
🔹
مرد چانه زد و گفت: «من بیشتر از یک سکه نمی‌دهم!» اما چون دندان‌پزشک کوتاه نیامد، مرد قبول کرد همان ۲ سکه را بدهد.
🔹
با این حال، برای اینکه به خیال خودش زرنگی کرده باشد، عمداً انگشتش را روی دندان سالمش گذاشت و گفت همین را بکش! پزشک هم دندان سالم را کشید.
🔹
مرد بلافاصله داد زد: «وای اشتباه شد! دندان اصلی آن یکی بود!» و این‌بار دندانی را که واقعاً درد می‌کرد نشان داد تا پزشک آن را هم بکشد.
🔹
کار که تمام شد، مرد با نیشخند گفت: «دیدی می‌خواستی پول زیادی از من بگیری؟ من از تو زرنگ‌تر بودم؛ کاری کردم که دندان‌هایم را دانه‌ای همان یک سکه حساب کنی!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/466140" target="_blank">📅 00:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466139">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5QLzNPl7oV5-fpkdqqXytFUY1oqrjfAjOfngT3gMEZB4snnOAN_4HKYLmvDUR4Ueh52eUIQUrzvhF31cN3rkFsKS_fyEUA22eHZ72gJts9gv-u2O-gmwmJWDTrY3v30FyFZte5EOpDhOdm52aF0ZJ0mzTEEw9BeQMk3TgsINm7eaeQ54oUs7Ogjh3X-4jdHUj6RIrSm52HZUDhwNxXgzqeal6E8sWpMhpVKtotDMw8N6MyayFD8sIMc9fKDdtJGwI-jZXu_Nl0Yj2j13ICzT10S3NlznclIiUaTcFyQSRIW2IXOJ7prGzpNEYk1df-0SuG9o0hW2_EXjMBP9vxbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466139" target="_blank">📅 00:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-text">🎥
فریاد خونخواهی‌ مردم شهرکرد در زیر باران
@Fars_Chb
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466138" target="_blank">📅 23:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP82H9Ike6eM4bLLvrpCGCumn7jR4E2tKlz4VpYkKAk_GANBxsmcwemCUncU-QM2Oq6ntlyoPXRFhHyN5raBjURNbFT9X59w4B6SgOLoPvSTJWn0DkXZJ8fLxr_qiktZecAUDBu0jsHCP-DIKH7H6oDd7tAXPHY7nrCDrmpxE4URBK_IFkESkzxk7HVUQ8A21Zvcoel-wSqI05Ek3ffEjqe7mjI7P9572CfQonQAXrwDcczjuo4qeoA2csXbxZg_1y-G99LDEm-5iB-on2aMPi3rgxZD4KmO0UmT3E6BpgmPWQVPzm3EVglUx92tB1IsF6tlPZLulTckHRS4VT8VXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: طرح «تورم صفر» با ۱۲ قلم کالا آغاز شده و قیمت این کالاها ۶ ماه ثابت خواهد ماند
🔹
برای هر قلم کالا متناسب با بُعد خانوارهای تهرانی سهم مشخصی تعیین شده؛ برای نمونه، هر فرد می‌تواند ماهانه ۲ کیلوگرم برنج با قیمت ثابت خریداری کند و خانوار می‌تواند از میان…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/466137" target="_blank">📅 23:52 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
