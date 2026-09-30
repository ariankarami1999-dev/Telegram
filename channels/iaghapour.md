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
<img src="https://cdn4.telesco.pe/file/bvGtniESU0p0EKoHV10e7xhUlboob7VErSftqKqhc8pOxFLQJHqoHfvoGgMFgCHaFebLOSV-qPx_vv4YskgKA-089SGCAZHYiMu-5STlOF-ma5Moi4u5DRBUX7bxCTSIhUN8c2osTeRoK-jKS_TTkqt9Q_8lWQQXyS4My6aGPcUHffk4ca33wzsZKPwtBqRMGe0qug1vZ14jneR754YpmbvwqLNMkgjb_YcGeMuYCPsPHjw0UJRwcp7nTExBzReH3BqHL5z0yBrCtDyhxXkZkFAYdCT9O2X9Xy_jTJUS54s16TGnvNO4d79GqUjRqqwq5NKOOXchdWGb_HetkGQd6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.5K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 00:24:30</div>
<hr>

<div class="tg-post" id="msg-3079">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromdownload now</strong></div>
<div class="tg-text">📥
فیلم یا فایل رو از تلگرام برای ربات بفرستید؛ براتون لینک دانلود مستقیم می‌سازه تا بتونید بدون فیلترشکن دانلودش کنید
🔗
@dlnow_bot
📤
یه قابلیت کاربردی دیگه: اگه سرعت اینترنتتون کمه و می‌خواید فایلی رو توی تلگرام آپلود کنید، فقط لینک فایل رو به ربات بدید؛ ربات خودش فایل رو دانلود و داخل تلگرام براتون آپلود می‌کنه
✨
تبلیغات و جوین اجباری هم نداره</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/iaghapour/3079" target="_blank">📅 21:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdiVLRkrJvN9kDHyPNCK5GxA4uCBo97wITTwF6h_4I5zkip15f74RXMNtIm7MoNOLjDidgwIVWMzOMh4njOZnj1gMYe0MQhrbtgfKxR2QexRtx1UayLu3tqu84k9G2iQGvrxyfptgu6BbQNVNIDyP2fuXyh6lbdfqgZmnRyBPBzxw-UnmE4wod1lBh6k6M7qP9ga1Q5RwQ8fBHsZaa9ExIjpHzAisdgY0crRYPILc7XK70JUPtXDOwPanz_vncMU7hwrIrCMcN_nzYvz-KpZ6kPW4EwQ6ekPetOgzw6Vshfv9p6F-obUrynKUNAEYn0oQ9pXxwliSVsLoyFUZOieOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی‌ها واقعاً فکر می‌کنن ما همین الان از پشت کوه اومدیم!
🏔
😅
ماجرا از این قراره که وقتی ما بین کامنت‌های یوتیوب قرعه‌کشی می‌کنیم، تو ویدیوی اعلام نتایج، اسم، عکس و آیدی دقیق برنده مشخصه. حالا اتفاقی که میفته اینه که یه عده از دوستانِ فوق‌تخصصِ جعل هویت، تو سه‌سوت میرن تو یوتیوب اسم چنل و عکسشون رو دقیقاً شبیه برنده می‌کنن، یه آیدی مشابه هم میسازن و میان میگن: "سلام، من همون برنده‌ام، هدیه‌م رو رد کن بیاد!"
🥸
🎁
رفقای زرنگِ من! فارغ از اینکه این هدیه واقعاً ناقابله و فدای سرتون، ولی یوتیوب یه چیزی داره به اسم Handle (همون آیدی با @) که تو کل دنیا یکتاست! یعنی هیچ‌کس نمی‌تونه آیدی تکراری داشته باشه. ما هم موقع تحویل جایزه، فقط همون آیدیِ اورجینال رو چک می‌کنیم، نه یه اسم و عکسِ فیک!
🕵️‍♂️
خلاصه که سرعت عمل و خلاقیتتون قابل ستایشه، اما متأسفانه جواب نمیده!</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/iaghapour/3078" target="_blank">📅 20:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3077">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edJpe0M7lBb84BuyGbXx4N4FeSbLDsIGxbw6MNBenc-RnKY-n2-AM9-BUSCBUofKJiNNkxWGKLDgHoV8dHBeVDE02dvMe2-vlPQhS5ZRE50bh_osJNgnCXn_3PWIZa64P8Y5rxEHOAe2zrVETPFFKLsNtzNut4atjGcd8iWWVuSUZk5twIPgRIzwinlPtoeqPdy7dzhFLjfSBv6r2Us3bKnBJ3tStxpyDgUQ2l0V3l2EICeFjr4jnyR9sTaSfCRadXmbKPlmWaLAZxi03fEAa4o2Q0F0l54wR2ybiNnbMMSd2wRrDTmvXUcZ5ftQfU00oLO_gx7Hj6N3z4S65g7BjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه ۱۳ هیدیفای منیجر (Hiddify Manager v13) منتشر شد!
بزرگ‌ترین آپدیت هیدیفای با پنل مدیریت متمرکز و کنترل کامل روی جزئیات کانفیگ‌ها در دسترس قرار گرفت:
🔹
مدیریت Multi-Node پایدار:
فعالیت خودکار و مستقل نودها حتی در زمان قطع ارتباط با پنل اصلی و سینک پس از اتصال مجدد.
🔸
تفکیک آپلود و دانلود (Split XHTTP):
امکان تنظیم مسیرهای مجزا (مثلاً آپلود از تانل ایران و دانلود از Reality یا Cloudflare).
🔹
موتور جدید با هسته Xray و sing-box:
پشتیبانی از ۲۱۸ حالت پیش‌فرض و پروتکل‌های جدید مثل AnyTLS، Snell و SOCKS.
🔸
تونل‌های DNS یکپارچه:
ادغام پروتکل‌های MasterDnsVPN، Slipstream و VayDNS.
🔹
بهینه‌سازی عمیق:
۵۰٪ کاهش مصرف رم، شتاب‌دهی TLS، روتینگ بر اساس دامنه و تجمیع کل داده‌ها در مسیر
/opt/hiddify-manager/data
.
🔗
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/iaghapour/3077" target="_blank">📅 18:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7-YCopfdNabaQyccwTBNgOUwBpMwLfpa8einoNMAvGlu8FYNeSNoXHnq8PxYnxCEgigu0a-tM3HpPPxM-ON1g1xbRGvqrbRus5deFIeWpZjiI_UvR6lXRu7NTQ0moc-4V-v_1NXLXzH6YFT8i_K6Zil_AbRZ_7bOz7xx9Frwy5ick7lubuNWOARYXbkcKamcohZKZn8XdFVYw2jUkZErPPvSr_wwrpxcFR28HLEuHYTl_w8_-d1JIRpadi03s0Cc4CSSmT6fxSQMBaHAM2LVBMp0BnnmCMtAVlNIhYitX9lFcU3lkdxuzls9WTIMCoi6vnSStQMJWY9nD6_dTn3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
مدیرعامل مخابرات: اختلال اینترنت برطرف شد / وضعیت IPv6 بررسی می‌شود
محمد جعفرپور، مدیرعامل شرکت مخابرات ایران، در گفت‌وگو با رسانه‌ها از برطرف شدن اختلال چند روز اخیر اینترنت و فیبر نوری خبر داد.
🔹
علت اختلال چندروزه:
قطعی اینترنت، سایت شرکت و سامانه ۲۰۲۰ به دلیل ارتقا و به‌روزرسانی زیرساخت‌های سامانه‌ای مخابرات رخ داده و اکنون اتصال کاربران بازیابی شده است.
🔹
وضعیت پروتکل IPv6:
جعفرپور تأکید کرد از سمت اپراتورها منعی برای ارائه IPv6 وجود ندارد، اما سیاست‌های بالادستی شبکه در اختیار آن‌ها نیست.
🔹
احتمال تأثیر تغییرات دوران جنگ:
وی اشاره کرد که تغییرات فنی اعمال‌شده روی شبکه در شرایط جنگی ممکن است همچنان بر وضعیت دسترسی به IPv6 اثر گذاشته باشد و این موضوع نیازمند بررسی فنی دقیق برای شناسایی منشأ اشکال است.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/iaghapour/3076" target="_blank">📅 14:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/iaghapour/3074" target="_blank">📅 20:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3073">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm98eE8EAnEHORgR8PPPo01Kuj9T4LNkpfj6_f_oLpL_cWGjj9wZbptRx3_VTkh1JNBpIPfJIySwGrU9q_FkRKA8siZLTt-1PU57zKicUObSCPQMD9SFDT74sbxikIqcApGKxN_vtOISETUe3f3nL2Ble_PGrJtdNLSivxEnmfy13aRUcuaV5oRyFqe1-x-7Qvl1A1r5LRNO1xo7OV8NftbG0w8olwqim-4MCYC3O0_VgOjCI7tvQrGnEDd3CZv2bm83uu6E4HIbB1o0vET0m2_iKWcWsTMrhXwGQwqbI0rOi6XAusNAUppn7lw0aW-P0Wjj2tpdWc-KlNZgoXASDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
تولید ویدیوهای 1080p با هوش مصنوعی برای تمام کاربران گوگل فعال شد!
گوگل قابلیت تولید ویدیو با کیفیت
1080p
را در ابزار
Google Vids
برای تمام کاربران عادی و مشترکان Google Workspace در دسترس قرار داد. این ویژگی با بهره‌گیری از مدل پیشرفته
Gemini Omni 1.1 Flash
کار می‌کند و ورودی‌های متنی، تصویر، صدا یا کلیپ‌های موجود را به ویدیوی خروجی تبدیل می‌کند.
⚙️
قابلیت‌های کاربردی و کلیدی:
🔹
توسعه هوشمند صحنه‌ها:
امکان افزایش طول زمانی کلیپ‌ها با حفظ ثبات کامل در نورپردازی، چهره کاراکترها و زاویه دوربین.
🔹
هماهنگ‌سازی و افزایش رزولوشن:
تنظیم دقیق مدت‌زمان هر فریم برای تطبیق با صدای گوینده، به همراه ابزار ارتقای وضوح (Upscale) کلیپ‌های قدیمی به 1080p.
🔹
سرعت بالا در تولید:
رندر هر صحنه ویدیویی در این پلتفرم در کمتر از ۳۰ ثانیه انجام می‌شود.
سهمیه استاندارد به تمامی حساب‌های رایگان گوگل اختصاص یافته و کاربران طرح‌های تجاری و پولی سهمیه ساخت بیشتری دریافت می‌کنند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/iaghapour/3073" target="_blank">📅 18:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/iaghapour/3071" target="_blank">📅 20:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwkGJbgQDlMA4HL9hiUqbBGbkEVufScZYuhgSfcQszMTf1tzwc_iJdi0ZA58FPW5kuAbzyd1KfbyFd44bxOZqdfw7EHHb4dZuOpAYXYOvfeQjlJEDYEW1jrdc_1ysouPEhK_8xJt8SgM00NFbPglKgEBIZi7HRVitNCP7RxyiN1NeAUjctrfKpCiiWSSUlLznOs9W5EmqxCWraUJRdGLf1o119QZjLGf_bTwdt0_0YysovnH7OkZhlAbAtF9iU9-AOWNMIN9APM5YSQ5Xxy9FUVh3s_LRWe-cHVtwim3MS-2hkc_cU7kqGv523vbmgu4hcBUa4cv7TsbcxECSuWH6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axvoswnBZ9Jh-XZoeq01nNlP6F5rmKvNFAg_SVYLSz79omx5CyWF3EYxLE65LzLW8QmTUvz0Ins1ygzLZHVr5RL1GdyHrshIHOdnKy8lwgOOLv9h1ftwAhx0ulwebQLqBt6uomvQX9yktulYGxS0QWSIgmPDzyDea4DKdCybMOdjdIJZcreBObnNnvPzarcR18OQT1x9VN7b5QEDw6L_s6KCT8BvQ8UmeEk_XDs-mBQ4bv9t2juAOtMwN9SlZJduAsQZbe8zbIaLmc9YW8JzZ-SP_uydCKrPgOfKQ4nnTwuCjH-8mWgiNACl8lYuAs9Hf95C3Np2sfltnURhKejhmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/iaghapour/3069" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3067">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEVvIaUmAl45jSMb6fYoxsgQ1skOyG_ocI0B2qVtnfoKxEZnbhzM7_fIZjkE2VPAdpjBL5t1mglosZuYcG8RhaBm0LaOmzThpRFf1z62IPGCiOeYoam48etRrUbV9skQQI4puD-LO0aWy-OefqA-ZaaMbrJ22CN-c0ZQYBbdBsIxiU1v6_TIarnXYybqjgGu0Ndw6VgiLX6fcZsfvMOEOCnFxh3wQ3Gr5hqqkwrhtWFr14zzwkMutqz6wEEUqvdkwxIirec_elHx9U9rIuSJlePYtXIKSt4BL2UQVssd3PrbahWtqbuG5u0FoYJcKooItYfRerVqsv71em_O19Hbtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/iaghapour/3067" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3066">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=GWh99k-DidFJ0Oo2JSEG6rHJwmQjbZIh0fD_VtSKf0HwBryO-hxlhyRoi9hCrMK1CqJWwVGCIqMUXN6ow0L2iReG-xWmcgn2OaqxtxvSZm1EqkjSNJhdI7q5K1Fj0ymac-ofl5n9elFS1XGyjE7VE_WY-4_RCpfMovZFsdT-uus4m-ama3i5lVh-o0E923tQWEnagJGTWQK2S_w7xUAwlUgbytafqtTUOuypr8YtqYWg58lZMheBcPFiZ3Xb-ToDCjLOnTfHqynCThrwOSsjxZRBvMcK0gP_yukYQz_Beq-jghepSHuNyRkiKUR82bxwFgMDA1uDShWl_q_g0ULcKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=GWh99k-DidFJ0Oo2JSEG6rHJwmQjbZIh0fD_VtSKf0HwBryO-hxlhyRoi9hCrMK1CqJWwVGCIqMUXN6ow0L2iReG-xWmcgn2OaqxtxvSZm1EqkjSNJhdI7q5K1Fj0ymac-ofl5n9elFS1XGyjE7VE_WY-4_RCpfMovZFsdT-uus4m-ama3i5lVh-o0E923tQWEnagJGTWQK2S_w7xUAwlUgbytafqtTUOuypr8YtqYWg58lZMheBcPFiZ3Xb-ToDCjLOnTfHqynCThrwOSsjxZRBvMcK0gP_yukYQz_Beq-jghepSHuNyRkiKUR82bxwFgMDA1uDShWl_q_g0ULcKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/iaghapour/3066" target="_blank">📅 16:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3065">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx6Xcl8NCSI-YCtJZt1eneX9csKVxhz3km6p7P8xIlaf3LSOjIJzEux57GoyBTlfTbByEp83C0Vz9QKtIJpXIvyFxbHtqDrrAriyim9LLoxzvS8982bxyxf52eRqU7gsOEZgEN6VT26c-fiZ7J3morTgVC4H3B99LjwtoHQKCD9mjUu8MwTp2ymmJWg5mq1eU0ZQm0Xp3WLyKg-cYRkPBpWzk-GV5ncEF8_mp9Ia_sQ3lJgrKzCaRYzu73OBhkk2QIXMfTxRSoVkeV7LWGKvEQnCfD1LsMYtFaiZ4NqnG-FFmRDN6tBjO8iF6nKpoqXPwJUWo7PquHproz7qNMosTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/iaghapour/3065" target="_blank">📅 15:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8p2IhDAAMM1uWcPgI4ZG_Pq6Bkl6pdHyL7Bfxf3z1j_Dl-s6zGaDQ8gJgGcCPaJaKAmgthoPhTPxYBnCCivdr_28o8RyPakCiV9Jm2Ov7-8T-BsTiQ9BjgJmA8Lz814hfNj0nnnSGGIYtCNci3dW83BPU0yUafTcycGxbj8ScGF0eqqN3fLYs0scR33G2Omo5No6ept2qojylugFSUAefSDUW6uoAoaGB5AVaHn7goPwAbvik3mzfKHRzjT3lSfhi2_GYLZo2fwxE42w1ztH8T3gb5qFdPwO3x_GERGCfCpm5c6O9sUybj5RVUsT6Wrra1L9YSd7oLUcwJ-fH6ylw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/iaghapour/3063" target="_blank">📅 20:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3062">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7xU33do9EcOwoDIF2hPMx-6mZmDZcEDdKmRGeNmSXO18R8icqABAliQePtXnfY-7wxsY3DpXUXOJLO6VjT3uTUEnS0evOx1O6w6iwLzIc5wzXpY278Wdntw9R-xOBonxzON6Y7Gqa2c6R5g8CtmM5MVWoGN4fBs12R9qxwEW09IoSCSI_nd_UA3wHkVvCqynN7iFx4cl292rsGLjLUMOOe5K24_UrSrQmj83rZ7D4sQt31_N7MqVf2LZsYIEWXm5TWGooWmYS9GJDri6QQf0qdWTtfrHJ8xqE_oJdfQ4Z7epTxXgn9n4Jz9qjv70ZP9pvwtvGcDmFKIYmGi63Yuaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/iaghapour/3062" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3060">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kg-7xATthnfA5E8ef0yeKgBPOn13nC_mtSBgxXf4S-bGKj2Y8LR2rPe2H41U2kee81FZvoZFtqfdZAWuJy-zQwpGblg03pb3PUZuFrG3htGmlwfnf0xQYxAaprM7P6GpY1QcZN0v5Gd3urJR3SWgTMRel6B97AM73EdnlNxH6WOMZUHKTraUj8qAAcbllpdd1MgNHcHOY38f9yxgKNozUYmw6qP2QCEYXxOmAaYzjJXEOox0_9cX0kvjd-GVdsfmNk5hEDgher2cV1f8FIxYFBBw9xPZe1q9yVkKpWHiU1-EwUoaE4hNqlgMxKk2twtfIrIX3zK0KZ8xQDWrwkUgww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/iaghapour/3060" target="_blank">📅 14:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3058">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvca04lrycISfsmp9bjzZxCm5BYpli1Ku7xIUlTj-nu0pFkyOVCo-zPQxMwtXz7KFvFWaxuB7H7RU_ixd17B-ohmDeMICoe8xMsevneAhBrCd9ua9ubA7cCXdcmTH42Z0wOA2Lt7y6sN-MDrdjUjTEMRhoBIf88wq9bXXYnWRs8Uc_vg_yyuY3s5wvKSinAzjRURxmfOCxj8ZYj46cd-ND8r-fOAK1R5wfHsrmMdRR8lFI--9t3uzz7RX5TuGaEHYAk_F3Z3Wg6Jx2PmasBjNSwm6owQBeAVJ7VBB1o9TOJWT_3ZnMquATv8akgQI-dnGjbODUIf4pCnqDYcya828w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/iaghapour/3058" target="_blank">📅 20:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3057">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dusgS0DiPsw2gInoLdL5xil6BqSiRI66_XtVAPJMZAtXfJKh_O2abZ4NHrgXsQR5QXR2KUkOsiko0ux12-Edn4rk92btuQC1HWzlX9IGLDB0tadTwCQ1lMyGi86bokiB-OVxM3CRfFCEmzw1wXH3SZyz_iU3FoHOPj3iXS4t39551GwL91lPmEVVaJh-nxFS_mfvf2EbzUb6-dwsUixiSkMzkwA9a3hLHu9S2UpjMaRMTUN5BGtpOJ6Ctg4YYT6cmDXnbRzDECTdiBjnzBxPVz7WMEWBM4b6k4e6QLDW6-xCC6FoX26d9Jn4pMPoNGOjHWADfcqcU8ytYJlJQ-pryA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/iaghapour/3057" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ndzx9DLfGOfFIcDtQyxvQDXv3GkdC9gBJEbbHABTpJrSChu_qL6LWTyUku_HCNlGmF1KPidvZpihjZLzNSc1bE8d2peRPklV8TYlJjlGZ9zcXUe5y7R7VScPeEimC8hL7CzFgDCbAUXIVxR6nChtqam-Jq43PMlF4C11m6QzlGkqRJhvyEghwpbDkpKuCKxGYBlcJwsLZu35pLc2u-qB2MlydWJYnCWwcMA9hg-SfjiYoM-aKiUOBuZiPhSRCsHvlangS_w2n5KlXYYUPhIedqIcFtNAeRjEBKDGDvmtlsC9Ss517bzjtByR0yudjpXaTmBku9jLcF4jnCRJti3Zvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/iaghapour/3055" target="_blank">📅 16:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3052">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSnX3ww-pFHXoRhjbOulpclr09rsy1Len9DMqW6v2QjfTR78uCIgGIQBt0hPjoeHLgumee5NgChEbs927WR8aSZ8fl-c6kDU1WBI553-Q1Aqpnsedi2d8mhgh6OCjaVfw45UEHfwIRUZLeQVViy-jKipbPJFKWspzMO5ai8AQN-LYBBT0Ktp3jI7ZicXtYZdD-C3amOcLJeypLY84F7_hoyvRc7zj4q2TSCwZF6-uKjEStLgDJa3BvUdGq4pcgxwXr1jUFjEh9SnoGtOVcE48Wnf5bEU6_6XTiD4gePW2QY8zY0OBcbCcd4Muu5F5fl1HS0dUl0nPOuM9in7ED_I2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/iaghapour/3052" target="_blank">📅 19:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaoQQoXJ72m_OX6LNtJ0CBeCbe7YKOOzQWoa5teFTloDpo7gPJub6poRKhEfruO_kMUSqzeSBlbYLWmQ1BbyVMeAqpqTg6v8kU1IIaqwBlbEAqLlBDsPaFsuV6h89HE6ORs32ecPnnlxMYJ_tKjX2lFd8MaH6kU090uK66gqpTsITjOMDP50zASrpr3UYaB83u-rc9GxDOjoYCnwNpStB66jf_MO8GAT1mGrTdD0ABGAduKfy3qFOSg1J-LiFyOHDKHcuiLWpSxk6OWMSQCgGUVsyzzLLhpbvAstaz7UiJFaokkpYO3ynrFKTYgVHPyoqma0YVZkA9eUCBZ3NZM1hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuyZz5auujoUSXouoQ7u1JdVo8svirrRLtTp3KJVMxEhmQHsVyucBcAWnBy3DtARE0Qa9oYDNhM28nCrTyW8XRjIvLc4fkCE7oLv7WB_eO7ImwnhnaUkhI8wlG6aVWMP5hemVFdXtTjd9poBSn12Jh0zk4LINNbC7ilnj-psqjUbeyPvqbzFa60Sk7UKhUv0x88sG98LKn1J4rNzD_yOMdDvicY0B1upKQcCY1cJT2waVtDbU2lMfwNxM0GWXRW4bwBSuO1kp3v2sfAdpJYB41mvGp_mrvPf9gWtgfafC4y_sHS8iJ9S0K5hcwct9pRFqkUI2wWJKlrZtppRAs3MyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzA_FIQ92jPakPQSuMm9AdzkXrEzotvrWCvU5tgQ6ESCs-I-s2lz6jMpcHEu1dtZSqiyw1E-VDJwKlAbuaedkC3_b64-EMrgs5GrpnuETTi9DhCNlz5lXWmLj5uB8Gav5JYyjzjeybhNCh7rCJpbgxPZj6dbS5uKTfAtC-36DRvzVcyoQOxpe-8QUl02F_Rz9IX-TOPXjrPf6fScOLi6xsRXUO2bk28PG-J2yGL2qtnNy6InkPiUGapW3ovkYlYrzoqXdVu1VcaJdUo9lDmmCxZxudGSkl4NFRTAfWVab8nGhp94U3DH9le3_oj41PuNBuO1q2-daaYO7AJjuVp1LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/3048" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=PSDtgUkgdjRQNaMd25jAbHApb8bWZhDRm3tyI-l-KNnlMSUih3V8pO-sh5tL4c05UmqGZCzpLy_-qVe7o3qeaROyIfO-xmy-hrhk06A4cKW75HOBKISfCt9zYFgOKUIfjwWtSlf8ZCUb_6YI1qs9N0JAFUVIO-GmbBIFFwe1KSiB3jez95gLXujC74UhwrR_N2Ngb1qAVP5XI1zgaG_G3fBt5vbCplt1M2lh4DgDivC48dG7XPX1xEJEPwc6tUeWXGXl1i-CP7De5DMDvme5q5Feba8ST_0zEqqUouTIR5IlKq5KVBxIYWsPfkDkHdhMnJmMWnAWX-G0NlpVukQcsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=PSDtgUkgdjRQNaMd25jAbHApb8bWZhDRm3tyI-l-KNnlMSUih3V8pO-sh5tL4c05UmqGZCzpLy_-qVe7o3qeaROyIfO-xmy-hrhk06A4cKW75HOBKISfCt9zYFgOKUIfjwWtSlf8ZCUb_6YI1qs9N0JAFUVIO-GmbBIFFwe1KSiB3jez95gLXujC74UhwrR_N2Ngb1qAVP5XI1zgaG_G3fBt5vbCplt1M2lh4DgDivC48dG7XPX1xEJEPwc6tUeWXGXl1i-CP7De5DMDvme5q5Feba8ST_0zEqqUouTIR5IlKq5KVBxIYWsPfkDkHdhMnJmMWnAWX-G0NlpVukQcsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/3045" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix3JQF505_oC7WInW2ZOn0OJ6j9niYQxjoyDQixoMJvb9v98kpmzMFhv-fxpS9a88dbXzV0XI07HbvH8SWdb5VS_Ne3YJ5PpTJEEQ2jmbMCEfNaLrWolqen_QENDyllBznYRh6c5j1CU0ADBojPdA7G12yCSCGNClrLyUWrNfsSl1cvJPg6Lv1mUlBi-C91WTASF2xrrZMQs8D8b_4jLksUcGf6434n_td5trmfIcmGBw2RWzcxnzOBDZQOg4XeBRZmdLJKLjPSmWHZLLg1K_X-UGHCmMXF_KluXVEMJ-NKejRFI8HljIjr9jcWycf9xSzAex7En3BBtL38akI1Ztw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3044" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_jOTMCt6Vz5A6KlX4sPSUDRSFj8AODmIQ4EUYnLC627X-Ony97RuUgUXhbBqvLtv-vFVshhtSeBXh5EO-doa0DQEnFPsJBv1sZAFdoLkRBNWew07DGUNOIkfYiWh6x_A6hxXb5IDeNN28sFdvftRiNIbp5o0YlsdM4sxetJVSxkcQdsWuK92GWQ5q0N-zM7rG-HcVeUB1YsGK_VoZKrYAz5C6gCsB24eiVBWmtjJxALQTydhndaAgdG3bc4-9qLAIM5P8RWUVnV8YKrfQGMNuNi8mjdcZ4nnj9OEceVuwIiiJX9jKOr1Yy18cXASZNWBNo8GA2chxtmHmMnB2ifTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/3043" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOwTxELtvTfXZ952QUxlwx8V0zsaSAXB36Qg1LtXt5e0Ri-vLkPTtEXCC7Fuey_-pV2Zexq_4JpYPyZEXuY8vGuLsEytHCZMS6SC4c8fVFgQNMFWzDOhxAsJvnvIXnMLPphWhUIrFMZvD2GIhd6Y43789WSv3qghmNvTaRDGme2nknLsdXX5Utw3PWKWHhn_xUqqbStuxwbzbP1WU3GcX_pwCMuuoxy5sJdzzMw0UfA3zKzaoaVsJXiaggQFjplJDL6TflOeSJMnOqJuOYVY9SCMxkTYAV9AN3CHiD_rXsPqoM1_Zf4emDavLSJV2Xq0z64Dd-5zSL_aK9yKTyglzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/3042" target="_blank">📅 16:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3040">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHcACpTWXh23b6SRqf5lEAC2652RElSMOGE6CK5Szr2RG13Jp9jTMa1dillc5Z02FDmvq45BLI-hlYCljkhVp9cb7eiSPsGiKr_7bYb6_1rIp2KOAyyhWfWobLiMwex1t1Qk9sxxUMnDNbvy-eS1ss1pTZokDA3E5f4KUU0poCcMfUB0xZ_Cj30U0t-llcY1hJWo8lQ3TIw7oZJLxkuVmRdW05wXzmHZFET4CHUeIZaLgSfj6NYC08f_qjipRdVinN3Zhhn6L2lYsYHzPEB1C-laQifinUb74t1g1b6-kIl7-XbJKFUnDS1UyFLqw9_ZBuR_uoEm5LsMaXbLJQ72ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/iaghapour/3040" target="_blank">📅 20:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3o3ggB9MsY_m5lohx2sNbRp1y-Lfv0v0D5T-EQZxeYQ_ahgN26aR4m8Lmz83pQLn_eT_XynCrXTe4LofZl2XnvNFiaPoRpkeJC2ezy68gVG3cxZHh7quRNVz7jDCFk4a4vAlulIunLjJXxvtWgRDelPph3hEyO7blw8Vz86uwZCDjLE4bpsdJSZAwCcx2ZCQd04GggR1ECXKJ15J6J2NWipr0zA0Tu3Usq9SY7FfWy5l2XM4WVFNfHSeLUvgAlAuE0EddzajPb6ITcb-tp0VIPMslE-7bi5eWJC4_H_loIXSYWF1LohAtJGw-FL4yKFGNXIZ1ZbkbBGOHJq1XvwbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/3039" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMl1J-O-cAH6JNjnEGtMFtQSBKAYJYzWtySN_t21JTcaJdHeY8nuCzx1VeL-K2nkM_iJT-5bHxfLJ5nqWqmsn33G09f5JxSKiuVumpWXQ3DLN6fFb_i4b-EwECTI1Rn6vOBGnYReifu6r2Tf53w7mkpDypRoycaLn2Qf7xP4jr8SRGXGhCD1XZ2WqeW-qZ8Lhh8yaiVM82syx9JozflxM7zfDfPQX8RUcbPmwOn4leINaLuziJPgt_88qi74pPruDXevd-vzbUyw7LKVPlXzvgLe-7QOkAgvIWiGNcX4WRMX_dYgdUBk2dm_-mq9hA5l-gFxjP9T_X_d0nMqWPSurA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
هوش‌ مصنوعی Qwen و Kimi هم کاربران ایرانی را محدود کردند؟
دسترسی کاربران ایرانی به دو ابزار محبوب هوش مصنوعی چین، Qwen متعلق به علی‌بابا و Kimi ساخته‌ی Moonshot، با اختلال جدی مواجه شده است.
🔸
گزارش کاربران نشان می‌دهد دسترسی به نسخه وب و حتی API این سرویس‌ها در برخی موارد با خطاهایی مثل 403 Forbidden مواجه می‌شود؛ با این حال، هنوز هیچ‌کدام از این شرکت‌ها به‌طور رسمی درباره مسدودسازی کاربران ایرانی اطلاع‌رسانی نکرده‌اند.
🔹
هنوز مشخص نیست این محدودیت موقت و مرتبط با سیستم‌های امنیتی است یا آغاز یک محدودیت جغرافیایی دائمی.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/3038" target="_blank">📅 14:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIVsc-oYyfIOOrMAvCcH4_Gu8Us3bs5nM7S3CG_wn7o8LU_kxkP81G2J3SjX_hgmV-URg9reo3yQcPTw_Dy50N2U3s7vA-7jC0z44DhX_ko3JlbQGQu1bhQmaC47GBjUwZuTiub6eV7osYQdRcMdlqQxcprWf-VU4Ot6f6MET1chSCDOXqlGhOP82suNsaGVJSWFxvXpCiqCMLXrvm2AxgBk6Ja5QGK5y3Bqnvk84PW93_CP8xuqmEutnDqutLCGhXsgQprKJ2awliPyUr67Ai_nqOJdoPIS8loLtOw1zC8Lh5wIBuLr0eVdJA9-HpjwwYSu9xiFTQ-CIf35vECUbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3036" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvHQlhbYnhsu40WveBiCGFtRaJbLJvL8jXhSTcSDfC_MWMoxxbNxb7Mh1od0_Z8lEoMHGquU1ucEwzSErE3SeFBKlaRHcF1Bd2rpAbGypPolAT9Kw-Yewz_4bd1GE4gBIqUh6BqKcUHU0rGh9jd3Il36rJNrFTP53keJljnGE-gM1ioui7AYcDgAIx5KVLGFuhBqP904gGDw5-FEHMVzYUMX0UBu9S_htF2K6uEXMhuQj17qmRFVR-B69ZPc43ipzX6s2-gilsvypOt-1FWf99Uay1-P3dv77uTXOGksRA2JYdd_iKyRh5D9I2ynkLU84dOcxlbDZ1-fMdMqZfHnWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/3034" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyjSJXvoyY3M9LS_9xVxS0kNv6opURiRB2l0RtjrcqH2cO9BdlmjS8iSLYlRaRIyXt9sZiy5xJpEVpZuRpY_FTzLoJMBwPAdFI6EL5YDe_jlSrJz9hr6yIsAWmgHNgWilyus2Bn_1hCovCbf2U9zicHMWjdSCj6_Q6_Aqr3GiLQD-Trx1pfxE3CbukfpChK3gi8EDAaTtFJM07TsWEUlpJw3DNPZoUOvQzgBPr1BfQbFVSirjXm3-wEJ_nhnWCzSiG8UoyVCLTPan90x5b9R3a0KjoE99T2yndlhraiF5n9EJL-O1ETEE-vGfZNQJqMxRINw6w6iswy48k6s3xOpUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYfbCI8MgmKsQJ2JJp7Jz2ZxY-se0IcnP4hYSmrF5WsTXI2M4x3PZo9vJc8-1b-rsmZt_X2zeqjWHASbQSDFezyE3Fss-9ZOqz2h1awjL8YEO5WMC8_jQu2nvnuBXQBGrR4i6X6uPsFXJ89aPadIXuQbnlkIHz1HBnPO2_r18Ih3AjCs3km5yXZjmp1OQb2No3LnLplvpGo2kW2Q5wnje8UA8FsHI2NOw7Blr_8OgO-950ZoMQgZwa671ZI8PPknuK8TmTDK5mAaZOED1mNq6m7alEB7Qj56tsYPYPieNfplY3VbeL09SJ36kabVeM640JWU8psNV9aF5QfwmY721g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=pOAJaJru4cT97IoeBBH5Tg74mjyhv8xW5L43faQj9YWbRQQNFQNdJmOBtJ5cOlHSU4F2pVBklFT6bnEXukhhSmd2Wqfn5rfK0Sr71RZLHEZ6xM43ipChNLCLLTfiDTpDGEL5BgHRa5-QxeHUUBlDYnx7bcJZDt6BVY0LnF4LTvOe2yNZWFWnfeUSpJjdo0O5Lxme3EtsxTc25oQsy3eQI4PzTAz1VbICO8VpAM_9JkFTvoD8254tFCwKyZGaZLqOTrklX1iTW-z8lp8tLwLZwJsu-NhLos1YrLYkdMYhPXWR7fLCpp7w3qfi8AHUvdVU_pXFYTkUNIDMcm3VXmsY0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=pOAJaJru4cT97IoeBBH5Tg74mjyhv8xW5L43faQj9YWbRQQNFQNdJmOBtJ5cOlHSU4F2pVBklFT6bnEXukhhSmd2Wqfn5rfK0Sr71RZLHEZ6xM43ipChNLCLLTfiDTpDGEL5BgHRa5-QxeHUUBlDYnx7bcJZDt6BVY0LnF4LTvOe2yNZWFWnfeUSpJjdo0O5Lxme3EtsxTc25oQsy3eQI4PzTAz1VbICO8VpAM_9JkFTvoD8254tFCwKyZGaZLqOTrklX1iTW-z8lp8tLwLZwJsu-NhLos1YrLYkdMYhPXWR7fLCpp7w3qfi8AHUvdVU_pXFYTkUNIDMcm3VXmsY0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6mwlQbGDu7-Xe_enlwiiRk_glVbAg4-nT-IEqmqxIl3fcjOfRSla0TrIeySdYVGCIap_ln39RfLRHzlRiJaUwbMF4ZgCnDsDZtnQIM5dcs_Ha6_OHMsCJr5cDubPHq4vkjeaPSg3S29GJantSJtSy6rz0Wo-NkJ9VeXMjkWqQdIfi2GUiuuqmkH-N2g7GdgJl5BfjrwccEF3UcODbWev-pMxzrfqdpbYpXqklaw4kpLGZwQyuNd-tKakZonGgqdIDJuUuz8O367Mb-uR6csTgrmmJou0nNno4FO05AVtlI3wGQhle5IxIH4ESERDwBOKUZW2G574kXwNjRbHIFOog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvDt9NaJgJMcPVUWj0xrkwj0ontVJY_OMYYxzsbyPZrHiGTMpkP_Na_1Jl4r8I5HUDujND0HXExiFTlMM7ziiIMm1Awfe8sThimMtH6tKcdjlvpZe0qNnXLbfccekMRQda3uhi0kwPpFF5Uut4nNU8zmdAv3sCE4GclZxSJ4scKmA2CQpRSi1I-yFWP7ixhbpQ4R4S4C4qX2V-AAtOrjFyCZCTUO6tvnOUZXYfRcRaLJLrBzYgxhS6sjHlhqLyOAmx9thiiD92g1_4g5QBjGoMjYBraGXi5KSTpMbI3CYRFiG-cvDXPtB_IoIQbKW8mFZ-7hyZEaVHIPqIjuXgabBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1Z6rco4ZXF-IqazpYdvb2OfARtjc41SDvk6RBSme6EG58MtjSFWQuiL_dKIVVqs3-X9gVQXrML6uOdN1yk6a2jCzZx_Hi5iY94DZpSdX5y2_fHHs9DxcYwHMyTEeGYii1ecQthZ8-g9o8DL7zyG-C0XsIUv3lAD40xfkgg0PPG6QeXqbjgAEaPb12fudPjgSsbtpxMv2YCH0v0XAPaxvM8uH5JfX-gv7ZwTd5cOkMtM-LC8yehy3yJuJ-hdxxx8VXH8dQlLTqEKhf16hRf4y-tBLwEc2R2tkk-_bwS3ODUHrPTGNKzka4y-23GX3l8jOrxw1Rwxx-TcFYwciqAghw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Lg70G7nFopSfKQtu89A8xI8ENJA5n8Auz9-lOjowFk4UrvmGSFbav2EW7ya50k2_8Yjuihz01KH1R33BTELw5hqs9SW-VmiMoHYxWD_ztlQrzgQ9r5P9TKsumU_6cIKM2gz4PNRcLtwpSJI9Cvi6nEPd2yKKGNKm1Ggtq-Jtj_pSDWRcOjlsP2jxrJdKmJrUgNLJwpewjwZP4xLgGyiG6Ovk1_MIw1ya4kHXqGe5TbUIcyAKa6o6XmpWlyqSBYbB7eiSODPFq03RjFdfVrREfBgpuaQdIs2FMxQEsQrhP5oULkLI7ZT5C8hxhH8MmlrCI-ncqm8sd6p0tJLaAWow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUnS1_D1uaa2MoIRjtwZWODNfhhzgMXh9Pmnlqf8oAB9SFVjRFTmsMngxDfckQLzC2HfJBP1MKluOIOAGjqwLb3NGqHRgD1mL8iW7e2LHmp3qZwqtsAwxHhojbqYgPDBBL6sHWZ2OPVLE3PxUyuHGDJGf_6590eqnc_I5T4yLLwpHlGJzjwBn7MlM4hHIRD4lrGQG2NBMqTlXkBvwd2GGTWRMymEQ_VKoc1EVtq7Hepq2sRDpuye5vCTIKfZ7ggv9c03jg7MoF0xl9lmakpsRg4TWTGcllT9xBjL5TlMSgsoiaEweyn9gTU8Uytxdtd5ZYvlRATCRhgZWkfSa6CT7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTuv3U_UW4sVjVbCzgkj3Vp32F3xkXpjGn132j2_ETHFMxwHOM6FXux7AOsy9fbTdNp5YBpPzg_rPIcFAItQmcjjvNCHSo_2udigicaWnLsbe2g0EA1jeeh9EXaue5n3i7NxyvI36xhq3t2RtlHoLnOColsJBrlllox1lIoTupgkOLSzLrxfqsworDRxAYuIgrd__ybowGJMAtKWxwt9AXoAQl-lClqdzzHCybCafT7-HHj5av5L6uVGJLM3C3uCr-sJH-rFbDMcNOlg8WD4wRBNjdFt872HdCmJTZsUHN7SKNox1GWwIp1aeVMkBlxb21IQq9AwWw8esG-xIIu3FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=NuKjVzLWamJHEeBXBKzj8luQ5Kj1nE6K188WE4BhBsSgVwjYOUnChHqJlWGU5xlMfVdteoMQGWISNR5lan0eYqpfhblGuxZ4DCSJ5A3ybpIdKXobmmdeDrg0atJGkNleiHXWMGPSitK2McbaolCgudNKWyCxDviPEAuXNYlvTxl7atfP7_6xUgK75Y-DQoeTFw0Av5bzJK8RcK3ATcMHJJS26OS7YKdybQWxzlxAV5J17hXwact-5Z8UzDJeUEyRD3T_fihJAC3eKntfuLEnxQhDX-j0rEWKXDeYU-PZV5Z_W5pxW3HyOuftfiO6R_qlu-uVOT6g460yDQEj3s64dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=NuKjVzLWamJHEeBXBKzj8luQ5Kj1nE6K188WE4BhBsSgVwjYOUnChHqJlWGU5xlMfVdteoMQGWISNR5lan0eYqpfhblGuxZ4DCSJ5A3ybpIdKXobmmdeDrg0atJGkNleiHXWMGPSitK2McbaolCgudNKWyCxDviPEAuXNYlvTxl7atfP7_6xUgK75Y-DQoeTFw0Av5bzJK8RcK3ATcMHJJS26OS7YKdybQWxzlxAV5J17hXwact-5Z8UzDJeUEyRD3T_fihJAC3eKntfuLEnxQhDX-j0rEWKXDeYU-PZV5Z_W5pxW3HyOuftfiO6R_qlu-uVOT6g460yDQEj3s64dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dfk1F-BsGIj-7YcCE-Kw4_0ugeodxIP4BMO2f1_bnnS7LQQHZoL_3rxdrwP7TrBAdQ3wCMAow0UaeS2RdzDwMHhq3Tv3FNRR4V1CR2YFQimA0U69rDQvlQxdYBF6p3sQcaCvS_nMg9Wa49tA3q7dvqHwx70spvC4gXHr_lOEQtGDyNMiajnqQHWASwTj5gHLsqfu_17dTZ6kZEa1fQvAxxqbTwGrOA63tjyZaKBNRUVD_640XAo9tFemiZ_M5hrMr5Cv0xJdJcBBP5q6eXqSXtGdrboNdbLVP7kPuEuuYpaZqTASwaBgQDSuarez_hAbpGMQN44Y4gJF8VQtufsjAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVFotR6bxFbNIfjb2f9M32ugoCXZHo-QAXMEuMQuCgmec2Q23akcAKKrP8PSC1opqoPYoW56XU056ElSkhm_IApOh1AxUzLfgSNqTBAdH4NTcXYqiXJHkFSAybmvZ2tv6LyxTx0wDzluwf3cLOqxW_-y8jLa9brrWAFxfFuGEZEIINZEtOYyqbZRNr8gD92s1lbf0DeVBcRLmvW4YrjZkfc4RMpzRlGEQ-I1Qg7Ev8JfkiZhE5AwJV0_G2qYdoip-XEcbEWLaTEAeih0cYm9peQXELSVsDcpiMkEVVLNZE7l0mcHbdKvTmOSr768wcsV4mHOmAuLATgi1glKDl-zuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WstRV7HuFXnrMa6t-k2ewNIP2IEi9H_m0fpBjFrPg1Gu22pXafuS9J_Pt8CJskmmDgd6LXIC1OoLJWlQCun1Srdufe5Apfsss155XG1YrGQ01f-He31HntZc_2veOLQivgEnODbfPy3YO9W7hL_jYfgSKvLulLrnH3zJCqC_aoABz8uei5Nt7wjrmZqIO5Q9x2UxdUuv9tBB6BqG3E1FFw3ALhp33dGAZc-dQT5KWnRQLyZE4Xsxp6uaboKG70jWjExs7SvdavvcKwtK-jpqYEK2FNkHuTT_OtgCDwaNyxP9jqKDiVFHdiApoXUxPu7SJ3CgOj4fvRPiDaDbCW5_7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnC-ScW2pk0uxSelwyrox_patWdebLi5v_qQw3osW5LyMhkEm5xgLGh8Mr4nac9m_9hVOcwDhKrCKjziPXzFXThUtIBS63HJSyQDioi5G0meIQ38goH-A3X40JEu_yIG2uD7dayjoGpA4PowpXfywJltPiiAhZmmNyG2YKAhbyaBvaMqRcw5nx1G39UOg9GZXvT5gZKeiLiqfw4xCbsXQgxRGHJZV3JHD9ugnUVtKlawC-_443aBDhG2yhosEST35MMlAN1sk_gAiCHfQ0VFDvJhfWVMwT1sA3yguHh6hQzZt0tnIfy8hsbHQp7hacyHN2kY_X8Km5wvuV-9oZT_fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwENYqsX8yKrI0f1p-0dV_cZmKlsSkiqZ1A5FLF8mzsD14RXL3ViEgyyde6vyedYvGnrjCfT4xCJv7DsVP1rkr8fK2y9afmJdOf9TLszII9yEsC0Kx4IlgIRVZo6W0N0fSOb0cYe4iIi6tzleJMhNFZYtGVIvMZx7RsCWiPgHp-HLKAF_auLqFnS0bl9Zg6KoXUDIOSwhkedlRwhClGiYvl1sYVjlbQVICutZkyC6sNgFgB0mROVWIp8pQ_hogTpuXXTHd2XbLlEJPbvR4RNdeI4kDDEGLvBPuLnRgfe3_OVJTkGY6aYkja57My4Anau9vBg5zgMUlnPlIWGBf6jIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG8jtJZzJRgvFUwDyd72w6YxW0ghvYOWBnUoQujUI4h6-FVULdErLT84Mhu5Mcp32YmpstzSUMxdXvGa_Mu0WIi25EQbAsH8Ps7Z6FKfwLFVmb_2Qj8Evnpa-GKGQVwkNdscTyWJag6jl-LzrtazyA1CBIB7BRNht32VJydHf0Ll2ZKBqgOqfUkvlDsdSLpgPHWaJPp3ZfJK1bD0xkL86LwtCFi93-wzWGqCTw493XMqmjpcIHGPqzi33JfCx3cqvwwlyte6DOY_BSBpiDMKzEV_CokZlmPJFX3NNJH4Abkk3gt2uSNzD9lOb4TOljDJRVyGkq8gRiNSMscesyuyAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jORKg-Sx5Gc8pN8BnTkUMe152I8Tdj-fiQDtX-39X1FgsZ-srldnETXE9Dz99FxsDrObb4SBGzyo-4SLGHOAIuAayotAJ2n9v8TXaCUwe1qiIebMrmHqdoDSxiBFdVvtqprqrKOJrtVTBrQqQfrAD0q3Kq6lFa9vwrOj5suO-faS_QTiuWO36q3ylGMyeI-rS_rL2gXhLq-3wRo5zDkJsLaSxcZ1PK-qg2q8uRWYjOhMXrGgoiB1mWGVQZ3xqmcFF4_pQeBZqzlZQUOP7YCJ737U-Gj-0-sgNK8eUIL8LceQ5CJQH2LGy2-y6DBa71RvdvVAJMYAqLNXeS8pBOcIpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=FK5plSHRaZtE7jttS_s6A7voJQrZxIogfbDGcsDQV9LB86tdYQng1mj-Db0JjZoNTJRGCvBioW8E0VTPxK_ddsT0N6C3mJPF-h3h8_DvmuBbPRqkkTZ_GQQ63UKJ-MLY7L_JhZwgLJDAGDRkHariDqFRtqjUmXSoDm6E0NqLQCFzSAgm8HF7YWA0LrEKMYHnWwB5JNh_cBlPbSb_scZVLBZ2egF_rwK6XJ0HqIUGVlEP3gkvZRu8_0ZjapUOYyNGUgoqr_AjuTnQfa73x9hFtrH6_azWiTIyBSsrdTn7yZ3zOviY3Jp7DET0BkhYer_7XL-EFzs8zY2tRNsWYLXwoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=FK5plSHRaZtE7jttS_s6A7voJQrZxIogfbDGcsDQV9LB86tdYQng1mj-Db0JjZoNTJRGCvBioW8E0VTPxK_ddsT0N6C3mJPF-h3h8_DvmuBbPRqkkTZ_GQQ63UKJ-MLY7L_JhZwgLJDAGDRkHariDqFRtqjUmXSoDm6E0NqLQCFzSAgm8HF7YWA0LrEKMYHnWwB5JNh_cBlPbSb_scZVLBZ2egF_rwK6XJ0HqIUGVlEP3gkvZRu8_0ZjapUOYyNGUgoqr_AjuTnQfa73x9hFtrH6_azWiTIyBSsrdTn7yZ3zOviY3Jp7DET0BkhYer_7XL-EFzs8zY2tRNsWYLXwoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbtqGxqEMYFpf2WJs0DVO6K5CssqvkgvIzS4JZHgnR0FoUjBtYg2ApqKoh1L7PnQIWRRfi_yn9xm7yZa4gxz-OAr7MaSIQ3NQ8qKYk5vzlnYG4qgqiTMRHQ1ACauq_bTqOfSkS-n8zDE3eIWartoQiqyFk7Zao0pxlUN_Ck6Rjo1lwUot0N0D_RgUZ8YIlqnwXqFhCtZcQ1HJQXDe0llCX38bMPvDq454p-erkt5Gholme1Dx3iJKImCOfu8JdPFFBkvXxuRJkOh-eKrvF7sEyA46-PIcYzA-QIv1JHbfrRiUp0nw6aNPpb0TDCQ_rLIt2Crdotc1yWKvqo2jUViNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=trxsEqSROj6sYzeUmWtDoAsW1Ne8P4fSXaIGVcKDVRV6Lr9rPI3ZBJdm9-LJ396msvFGcJuWfNRZqXzaEEPNhutxAiL1kXD8R8g5TEXMtX6dH_YAyNFHmFDxILrGICXeVupDFjsQw1xtqFk2GBLC3YcBioHYdSf0ItMFw_ltC5rBTevMVUcB8pfHXvIYj5gkBudhy1D7-pNo6fsM4EU76pSKurS_PXCwPdK6zzUIfhxQmfSo2HpjtdGhAHYL9f6RRya9QP5VDuSFElWFxbGjsvq5WIPx9JJ8yUaFPxp1q3rjcYsQPVF5wiplCnRTgUu81kzUpVWuFEzPzyDGa1GlNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=trxsEqSROj6sYzeUmWtDoAsW1Ne8P4fSXaIGVcKDVRV6Lr9rPI3ZBJdm9-LJ396msvFGcJuWfNRZqXzaEEPNhutxAiL1kXD8R8g5TEXMtX6dH_YAyNFHmFDxILrGICXeVupDFjsQw1xtqFk2GBLC3YcBioHYdSf0ItMFw_ltC5rBTevMVUcB8pfHXvIYj5gkBudhy1D7-pNo6fsM4EU76pSKurS_PXCwPdK6zzUIfhxQmfSo2HpjtdGhAHYL9f6RRya9QP5VDuSFElWFxbGjsvq5WIPx9JJ8yUaFPxp1q3rjcYsQPVF5wiplCnRTgUu81kzUpVWuFEzPzyDGa1GlNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4LgydbhBdePrAtCnPkUHJTdTTmOH7IdMSBlQ4qC4DH5UeQuQu5znqrgXxBIWa7Ux-_rVT_Zy--wzVwhef3hj2PxwUSc0td0S8QG28RXR3nIrm6PWTzI9-22jjfFFSnPDK73z5hX8DajxLbTeG9BHdOCi4ZyygLFjqlmrroxOuBYV9HdfYHm2msbGeYRp7bD8lMjEPSX-0K_u3GK5nX5Cp8X3vI5eeICUEd7yp8m4FHwAn1H6SBffLCBEFg99q2irl1gZndxXXx2JED3WOZhTxB84R30MWgHjC7OiCfRzxLtOKm8nLj-Ayg0qvjrYs0mNdBeTfqHbnozBoqw-emG0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7PhDZ1Ug9DhKY7NzuyUs2xlB0f646Em60o77JUV8mF8PizHBjBmQl90EwixSeyYYk5nD67EZCmsK4MJjybxap1Ck_TT2UOhCd2w9vTpMUa6lN44vzSoLOkW1uV_CEolLWiN0Swl8mX8uwmYJTDFIVdzU7qOjEPucz60kyo1dY_xujOgXzDQlHAyaFAn2gIiGlE4kjRyJM4ZvENDMfNbC5J6koP9Vc3vus9-Ts18J4gaEVt1eVezaba0Po4dekMzXrYinlVblYJj8smmH2MEOiY62hBFNvIDELKx64d0Ugpml-E0JwcyXNHNjeUGAPZvReUzuW3Ko-c3y7xg5KZoDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjWSgfSQniUOIdKy7sOrArKUq-cUzydNYAcuwYv41xrkpNhGMr2QkU7jrvqEm9DLS62vGaJkNmaltdDz24fG0mAFX2LzTuukiyPJbBCZM_LyMWPkvBLc_zilKUt1y4Gwg3bS2rCOvob8wgSFDPBS7cg-EbG4zgRc7RTp_RrO900iMZQO5HEBAOODhwkL0g2OOuMR4IXScTB5Esc5hFrDpKiaMwZdZJSXfGWImuUXE-lZD98MP_aFLBF4orYTkNBaV5sywBb_o4mSH6K3y-I72KEE0RDGcw99FX7c1Es-jsDWOUxxpSJvfrINjVmMd2n6f19H7TQouXx8OF4H6U1GEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPUGgt7WaIVSouoe4NYee3YlPK4LD-FdewBl7XOrnwSDBOMAk0gZy2Xjt1EV-MMQLvSCu8Lg4kIVzetr4jOsBdTGRST0ZYj0cLIiWWVH-hLBUZ5hebqxIaPgCTmJayOplVnPkAujRLIRx1WufKzlMwHsx85V85wZBa-MTkK8On_ZIRY5cq9dkcKD20LFALQMdpJGgbKNz0JW97A5uq2Y4TFs3mZcm1mKGLqzqJwKsf0Do9fAHwtBiEw33NYReu25Tt2LuIZtADXHkPuP2K21jVeSYQ7ee67qDcQ3lJhg5fqHqM2B591R4Liw9291tg0SnRhdX0ZCtObuvjg9SW017A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kr6x8hvEm7Fmv2ca6TRJl2Hv1bjOi3BYsW9Oykxwg0de33t8q3Kl77NPdUaqhGfuHqNPPeIvZmmAchUn-AhQhza_HKZtPBj4anV0SSJ3MGOMk2qEtE-leXc7atEmuBrKFkkmjoCQBVh8biFmhG70k2xTLTLMHV3ylYGEmgcad0xsZl6zw_V0kyOrj2mmyYISeKxUpub9Cz3HCClvKdp_UbDTDJeiUQudaJGQBW83CxoGfc3f74bR3qOhE2rQNf6QKYzc6-AD1t-vKAJP5fjs9D2AZ77ZkwwhRbWfUdSr_lYvAFj37wquwY8CQMUgqLIOQhSK77QsRU8KfffldAhsag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c78tXfM1JBRicyhsUEA8SWfIZCSVeavHCeRMX91EWo56caOxopn1_JvCmhdEpjdHj0QxrdmuJKF8XEUP-e4rhlAJCpndandxFP-bZTs-8iOYjZJOVXU6YZG8SEJpxgP3REp1RdbRDN1VqKlycaVr1b4GJWUeXqSHNn5kmWT80Jctm_Ow5dbyLfEFKHboBBbVqZI6Z-isLRAFgRt_nkerHiSYvkCwZs0ZrQU5lhZIU9BHyomt5TpjFS4t7Ps5_SGiFmJ2gMI8LWAqPljiaYn0ls50r4njAyYKy9ILDL3BiZzzoZJWwbgKS5J07iomtZ-VtcqTEVk6LAekOHm4FjSWIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGvI6a3AseSoPwccAP5wMqKFnkLWveRvnxg2tipdYkUOWl1Z3hJ-KIPpFFs7TNqiVD3pUk-1wYov2LwMGdnwoZ-Y4ERfjaDjH-JEARCaau4XDGIUbrbfblww_Qi7f1dB35EV_-pqaBsd8g-kG82HzbqlYRRU__x9IPEVOZRI7lUpDIyMUNWzPGErA0WjhgvhO-7Zo55G71rFqsMVODLZf6V53cZP2BACTHPWkak-Zc1eZX8U4uyO137hItwKdFlqRlfsdjoNsSqTmpnOlk0IvPJNvI6PxqUJtqYo_EoDEHwwYsAMCVRFADgrxZbTXph1FNS5sNzvys4CBOZe6kNltA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0HFZnmjX9LYBeoBcdImdglu62Kc17A-Fdwf9W0Up1XN5QRPYdYEq34jjPpE5rE2F9Icnind_R4tklwKo7ldrHfY-MUF0ZS4Ygah4QFHeZYzTm8RA3C_KvGfxrpcnmj9tsBJDMY7oOoZuYUvD1JbssRBYTgTcHkfjfMm6gMpsDwPK1CApV-b8MdLGvozHSapiHfagrhZhLKbIZXqtSrTBfd6aep9yG-dgvGUMAHyHeUyJ-RZllmFLQNS2chvIXi5K3Tbk3qjV6KZ28Tv_Mt_d77HIOe3ZCbrPnkmBBKkd46HvTQjqNxJE6YjwthPbmwBwnOcTPTCG6h0DyREy3pnLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=VXLYJW_70evXsI2-QL9WbDMPAG0teshG8dGDobwP2klpA7FLKZICY_uJvPB2NIDCw4U1H-59jdWxXYdgepts5nNqYNsfq8YaWUyD_jaqMU6LClUkKU63J5q6D_tBEZspIx71i6UVwyuG1phCmvecEC-iBpNcw3cft5u7K0GDkvE1rEOsweHtw7pAgp6HHLWCjPT8-SKMDkgbPm1swjGMJ8yt5z59M1q4w7h5c0-LDNKvnMS-BlaW4EaIoiwNBqkjTl6xR0xEEvZ4zNsGiCZdz7yaypYTyoI-kEP9WkS39ixOzSok6nAuO2ejY77U43gGNq5gt_T7TbjpKy5-EVhudQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=VXLYJW_70evXsI2-QL9WbDMPAG0teshG8dGDobwP2klpA7FLKZICY_uJvPB2NIDCw4U1H-59jdWxXYdgepts5nNqYNsfq8YaWUyD_jaqMU6LClUkKU63J5q6D_tBEZspIx71i6UVwyuG1phCmvecEC-iBpNcw3cft5u7K0GDkvE1rEOsweHtw7pAgp6HHLWCjPT8-SKMDkgbPm1swjGMJ8yt5z59M1q4w7h5c0-LDNKvnMS-BlaW4EaIoiwNBqkjTl6xR0xEEvZ4zNsGiCZdz7yaypYTyoI-kEP9WkS39ixOzSok6nAuO2ejY77U43gGNq5gt_T7TbjpKy5-EVhudQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsXGY_1OfCnRM3UFDmfGIu1EXFLZD11TDvHRDXXkQ44t93e5XllrNWo4NNodpKJAspHgywsmLyIBT7TtEL4dII66B4daEEcoGTWZVz9c9qkYHFERC4qJuhiNNTvjVAWqu2gUwXUKCtBrIE-Ykruh6BXtMye0VtgIxv9nG-hwSX1tgr9jVmRfPHEuVqv3PrX5AKNbMdCXCd0OmlwpGAx7KqKJS2HDo2mzYnOUEPzyk3ujmGEJqGtvuoJCpuFNvtZJNVGZLtce4zjr8AFDx89Kjc403RV6WNKgswfoLQaRltzCP8bYu4CVC_nFgTiFia2T1szA6cIEfoKw0FUngZdkeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUZolXTNzxQmj-iutGosApXD_JN1xQmOhLbxi3uibnuM_keFsMCxNqNEbUvZBk-8DfFesQNsckeGenW2vQt6nygOUypUksGHIZx7V6zewKW-V889f_gdJNgTqyxjMMehTFuQQA4WdbUvuHRN9119ZJ_YIOlXUq8BV0zI0U4STIkSUtUJPTJHw-VyksYPnqp_zQry07ui1azqNEJXYiZ2S2o_hT6RYuLMmPXBy7fSpQ-SosNGG5JiHMWxpH32Q6vdQNyqp34hTcStkd4uDDMTIJvGrJSURD5Ue2go4sElopfi89HRw7IhqiScPuP8s6PocBLLly8fYwFASR3htU0usw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4lrYCuP0AZtAI0P0lrbVfDRHFRvDjCXXkruyVao0yr1I0loQogPhifX6XZwz_-k0MEUQH6z4IDLPtWEEilHZJ0_w-_oTA9vZmEDKBqiBcEdd3Be2RHLxgUj5hxaS-LkBUsHQskG1IpyAKKinxJQuftwvdSpqT-XDI-a6Fhiip5768lzx2A5ItW0nWJpcaP4QXKaYJMAptGp7_R54LzoDz8EErSberXRZBW5V4pWgAnj0oltkTS2LPqYOBwQKWbHJLZbEgaTftaghi46gsHNKHF1D_UIUJStHgh8gNBCGRKJEk9M_xF2DdFs2YKl6MgoG0lFgW3yVNE_mTxv-FG7gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9PUdR72aaEDXfjOGYC0ZJHvHB_rCq4oQO3U_Z2cHH7X0rsAa723OdBDjb49UCGWV4u1mvLgwadC5llTBGJkm-9Rh20ZpwVWs_rot4KsSOqqIflQRMoAZqhbblH1Hr_ycWRAz-VaL5161v9caa-uBUBf6-LMLwWxmA74_e6nqXm7zmzhqbT-dlsT9biR_B5aQhie18EAvxTMbp2Fu3rZKgHadH9yM9TtDFS2G_G8-_JRifsjwrJohIZUaxbFvEmp79_E1PHeg0wbieeiAc-TKueqA1WmwFi6n3xET-EIaD3Y8oNyHzg7PPi3Dy7eEr9WvaXkFq19rvegLjludrcPqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=vddf-VNdxbIzWuQeRNQP6_uVmYKk_YkwHvUxXvgrnIlnWx227c1496_qaa-Rai8RFNemHl4gOTQ7_qM1cskUy6uQVMIMmVyqnhcm4tI2_JnoB1S1o8SZQ_jYjXgcPcSSNzn8a0vfCSkj2oyGSlIw45xtJ9RmgYhDThy60y0C3LQ0l3n0woaowo79nMn2A-JnmR1BIXvpn7pavxY7YDS7763Z1vW9OecCFBTlE5lDJoFccX13cK9QrwTGyd2U4Q-vv_sTXOnEXriYuQRzkmKUULk5zCHJAmHU8joT2AlUA1uk2jwKfkfrVg5REKMdP0VymrVd8x6i3NLwuSSECzSGPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=vddf-VNdxbIzWuQeRNQP6_uVmYKk_YkwHvUxXvgrnIlnWx227c1496_qaa-Rai8RFNemHl4gOTQ7_qM1cskUy6uQVMIMmVyqnhcm4tI2_JnoB1S1o8SZQ_jYjXgcPcSSNzn8a0vfCSkj2oyGSlIw45xtJ9RmgYhDThy60y0C3LQ0l3n0woaowo79nMn2A-JnmR1BIXvpn7pavxY7YDS7763Z1vW9OecCFBTlE5lDJoFccX13cK9QrwTGyd2U4Q-vv_sTXOnEXriYuQRzkmKUULk5zCHJAmHU8joT2AlUA1uk2jwKfkfrVg5REKMdP0VymrVd8x6i3NLwuSSECzSGPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY7WVf9nNt49wk_W5kEx8zVgdgHrFFbps5q_BgcQZCEKk-VRpWk8OVPaPhOhoZRbv22XAEFvAHHD4NKpyhMlh1uMeHpdFEIX2YVaCpBsrKVFQ1CAfxNxJuO-eGj_p7zzTXIqGvJr59F1NkkA-rMKpcjqbyPaeO0kLYbr1Zb3Exuaz1spzX6H_HKQr2Hi0mJNk08I89Lnru2ovQoNGknBQwoe88iFgErofOSvcY8quVolHexdFi88kqyotjucFWJbG277Xu-gOAtqPEkUQU6_yNhnmpobXokc4z9Cv5yeqSgNs49fqEH1xtbUU1rzWM9uNzJt7s4mrApZ5qCyNqBx6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy5M6VIx_G7YW1R7WiUCItAIqHE8B5OQCSy4NhxpuFX1s0LkP4aLjR31wGJQiKjMPJ8iiQyw4jiMme3x70U-5aiAhodCSZEqy44vaTqlZO92pBSiWcAWpaKFKO0ZUmD1ih7ehoPMdvjViw21yxtiTOJoWdWGbRlC8uAvStFnk5zp-Vheae7EBhSJKP9VugZHnbrS9KTN5I1okShL6baLU0OmPonvsn7g07FXgMJ4NI1ut77puIc6yhQX5ResYxujY5LQwg11NZvEshKs6G2xr41SahkwmZ7xdd4Tvgb3TFCBfy2gPmNeyrOIuhO1No93Wq6ly6ti3gJY5SVGRnBojA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1sjF2hivyWceHbAAORFRKS5nIcuTr2s-svcMw-G_mL9aMhYc-DOgT8lpQO3xEaYeikC6fzSCdEIrt_xw-qgokNcAco22VKMInB5mLaOm9Gmlo7WXM0yv7Dihq0OMZMsjjU8FFLMlDagsTeJKCXHayuYm5-wq8PY2okyj0wUM7dI3aRhSO06V6oGF8Cb6jbsxj8rv8wTJurbm3eeKa_ihwg1o--ioOnGP42vfCsTFFdNLTseLhP2FJjfT-JdiiwqsCovYH14FDzSwN87jH3yr7RWqet5oeo1bvue6JocetD0QYCN6zrRvHweQN0bBgHz-hgGwly0RUBPImb8Hl4s9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDCLHENI5rbBzOYpsw0KHDtQTxjOUm-3Y7Y0cDFTQc6NoflerjhwJH3UTSUg63gazKOJG96Z4Nkqk820PYgmEjM2xvPAznm_yhbj8Ky9K2oJbPp_4DHJ3kijbpUUpEB1pGIxyZVJy7CGjIibIOiiRcIl59gPCJDSXsDUIyK_sRCLRdW0tWWlUacHGDnoLGAssw6fEWFKPUqGlq5O6LGfCIv8nlU1tveGtdbv4pGd70hwd_HlxVvaFA1w-0LXQjE6e_1AIxTtavg023xLkUmBiQVxmFHh17G1x4qOzH3a-ct13WEqdvRQw2qVQt5Enra35WUL0EPBv-iUjnjH9x68uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lujWj1gcRf0h4oMZPpwTtNYPutpfGnw-9F2b3MBn95UNPfmJRaM3-Uh6CNzTgYlXm4ASFeLGs6d-xFFF9XXb5bhhv39VH5AzLsw55DDdv7-USBGelxNcviMbTC804lQs3kPQ44TjKORGbUHHbQIaVjxCj6n7s1TPme9GO06IIAwGAu4wMOJcsnKdi_-07fxtSfLrJ9gVJD0cLlftOsExYoqSDAUATRwWgyqzC8YbBA-EewEOgDoxqZmi5WOlXdA2G2RN6ByuyXWrrYfh1awys_VL3TpXyhGH8s-GnGSlBzWVFCrDj-7eGezGvbcJikX0BY-HcycWrAPT9yRwMpudkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRxiJNzarW1jxCyJ2lG56-NdeYvxtMQhEQIH0VLbJ35rp2kuEJGl3T1lNp7zjRy9MDwKtVJ8s9MrxS0DPvJLpHlvis_3Q3kjg2yc-7OVAaV9opQ6x0yT2_U-JUemx8ZtgasurF70uxNIsEmUkyfe3b0o2c7wu0vrADdr97RQVki47HzVwsJQYoDNToVVf-OcBTRHRUSfx7x0e6XjHg_nzTQBIAQh2F8mEVG8w0TNkv-1ZmXGS0w8RDutd9MFNmXMvHNOatGI4aGKIgHjzcUJ5CdgHLeV4HivjpGEj_LlLc3Qh6wSHmY29ipHZFVn5VNSXts2cxodaDoG-2HOwuBEbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=JAC9rJN56jOf052CgBw3Q3xjwJb_t9MlekNDI_Hq0I4I8u99XUW2p-iAjunpcnH81s98Grg_jQ7x69H7tFeQeSxWX9KECZ2VnPXngAPQBT235v3XPTyZtvOyYi_Syw64Caoz_i6lNpyRIC_zhjsUWzWA8EYCigEFRphcMmVYvoSliyM0Z9EE6sIRdQghmdN-CwSJJGWbX0LKAoBZb7LHvnzoCFEx9Dgtt_lpf5Yc7zpVCuer7AWHpVWLqOdw3YF-SnjPY2MruClrIRkcVYT0J3fMXghxRK6WqXPWtJelD0YD5-5z8j6tBPy2G57XnZlztWQrr8qAI7N3gfavOghkcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=JAC9rJN56jOf052CgBw3Q3xjwJb_t9MlekNDI_Hq0I4I8u99XUW2p-iAjunpcnH81s98Grg_jQ7x69H7tFeQeSxWX9KECZ2VnPXngAPQBT235v3XPTyZtvOyYi_Syw64Caoz_i6lNpyRIC_zhjsUWzWA8EYCigEFRphcMmVYvoSliyM0Z9EE6sIRdQghmdN-CwSJJGWbX0LKAoBZb7LHvnzoCFEx9Dgtt_lpf5Yc7zpVCuer7AWHpVWLqOdw3YF-SnjPY2MruClrIRkcVYT0J3fMXghxRK6WqXPWtJelD0YD5-5z8j6tBPy2G57XnZlztWQrr8qAI7N3gfavOghkcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzfsK4FQRUBdwwCv4FaonUhGXcmR05KtuFwetTRTDSfBnp6hLliUuRubVEj3xxghVQKiZBfWr3bVKOcbQOdBn1TjBTjGu3S8OuZIElqFNy7qsWS87rbLULEsdoRbqI2l7JgJ7k50zBgTE4CnOOJ1JfBFSeZByxYgjD-mUiMH_sTvxFftJxYvjc-saV-ubzRWasUrsv27dNGxOdEGz9F66bWIIAtcvfH_J_oGDlIKMOvuJD_TnPWEgdsmhoYdkgah8_ONjhf4RN8dKp6EqPZ181eZ9XVhXNchffaJgJbsycEYe1uZq-V0WvVaDAcAijfDjtSEA8C3a8exMfwY74Pgkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf2BkIKnsuBUA820s8A8Z2SV4v3ZSuppQ7zvTT4vikdbR_B-S1FyO2TnudMl5-R03ZRcAFLfSwdZ6uhK_wPIP-HNc0Mp7leqfmWssoEfWPlBqN4aHl10X3skpTK58bJtAWdB15k-AjTGeTqqyTTI1m3v9Dxv7hG7lV6AQ4sJP772s4Q2ac45SW9YYUfX8SEUODfAAiHQ6R1ZqCxk8L-CWW77_KtyQAWEwAIE-o4TsH1LnPk8DRU7FQ9s8IKps4hlZCLBKg_zfbUYDN_wkW6Gs0D6QVsIRuBTZn1PNT15jzmfv0J-OFmT9RIRH9ZLrkSbMZeNXJHTvNJK-cv0waduGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVg5YtYj6D8JB45UXFGOsgMirNy3XaZ2cK6be9ZIKOYf-e0d0O19gKKE8fsmOyzMwtyiSfpOvY60xHZHiTtixxYTqw8VBNw5yiT1bWzWFdE8DWQ0d8c41kyznNqAirh3erv943VY4aevjGoge1JNUCJBMYJYE_3cStZqmy1bdtWUyN7mFqyEfA6saNhTbg578RNauhCE7pqzoMvHRGsGe6K0ermQMVWZBBY8bpd8MfwVrGAJJTQ44tjYXhuwSb2-3Hd8qNopi6FF8zOHR2H-bNV_edXee8riHdpJYmprCUHx9QML-7AwUGjaxQw4pT2SBRYJQqa5dEXrqSYR9i4zbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2941" target="_blank">📅 16:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHwdghUrExFo5IFxgAgkgv-LiMve9DNbBs3pfcHJRUHdnEHJbDR7kRpub5yGZXljcq6Tl5iUBZREFLi1wyoudbEXfAmzeCoUIzKm5OuEgtqMfVV3t3dZKRmQygKShtDZvdofmGP1QMbOOeR58B9_QAnhUxFv1cNdGxflwCLtWPdSYgZQAatIntdK5KGAsX5rdCv44prs61kf25S3btqMOQzwxzD_5yCc7Jf6i54KH0af_jcwRDt2G3MeU9w-6J_jw5s7G_7q2TIZwckwZJSJEwnRztA0ucVq8kzQiybVLqeWa7R3f_XagA2CdtteJRXSdxJdwfVwqKoeh6OtQAzkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY-Doja6HSLb9dZGWwRK7HhtC_wYfk4Z-lGcD2olCW-50-YU-BmGWGssCRPQU0F-o5ofJNSGR301ZqVGQlS9wwmJdV6vu2rGr0Kzptdb5U8QU98gLRf8Y1ZeUbv8W4Nk5vd4inDKT2ZVNT-Aid5ssY-LN0JmRvQiqO8OYeaO-l1FSLtq3l1GjBf4fJCMkVvFQbcf7zwhncxvYK9_m4qmgu_t61R4XWiFLoCvd3JD4OdHfv9Kb0rzEhKtPIl3BZjCt9itumhIHDQdgx0kYPY2AUbhROw6x7gc9ePo1Siy_JwnT2SkNZrEQpXttOPjx4hRhC6zxQA1WpSlkk5WTbpXgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUx7cJla_8uRNkeKlWbU_BjeCTtP-dAFGENnzD5FcFPuQVZ4kGm1PzQFYwNRmTeT783zoo0CkfiDZYSMJpOf5AWAQqzDXsWbNFdW8yP56YX88dMrefLRUHEBkuo0eORQOB7EmpjqlYwm9Vhlk20Vjq492muTz3DBgnSdsIst3D6F_ufzK4FS5HQu5DtJt8pfa1MZZXZf0mMCHQBOT8QjK2atwyywmdbknOkdxKnVDT7290vQ4HX-zoXj8K8bVUrP_0lPN_2GYTp9rju3luUZMgjriNNgierRA21CGgUtOM55kJoVTmw1IgpjdvaC_7zeTfylP-PfWrCOA7uUEHuneg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZEvGikZaz5QHLfS_7LNF5LPvUFS59PaHlgDZXnzT4_pv36_Np6Xgh2WxzIv9uN2vOOuAhBCiGWpysehg5RjuOxu7xozwty_3PXcyOKtoCyMgV8EVDgYLRIy_31cTI-UsdFNxj9I-WicVMRimYaDANN5KZndP2TNnFKdUa_0SDt9Smr1jxR9ULn6TuhBYiDMGr_CpPrWhqcS96ouAyaIrJ2eYOqQXNU52g2PLXxUoFCHhN3uFUq4ATA4UEzsEb0Ko2ya6Wu32V848iOlxK9Ux2gh9uw8rv8H-AMY9l-ZLvhfVeqMJxPLSjRrJXuq1l5Y_3NAn-WKiBugReMy43HZ-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2936" target="_blank">📅 14:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUwaJG_JGo2VE0ZUcGL_zCoIPUUuvDVbvej5PpaX0cy7LNqco9ut0RNd3_0lAUnjGiJHAmdlWdZ-q0wtq12iSHzJdyLIBOCsCxCcm0-xm1RJH_ABM3-woIx9BtItDidst0UbC9emg93Ob68sPLQclUy184OYsUCy2Jsf61pd7y_GeV8GhtOLTPTP2Od4lVXu76Lkhjljjs88xonQoj-eaHjT8yXylazjJ0mCR2fFpOOiTWzK5aJVMEtcf1anfd0xOtW2Vf9Pm5mA5ZG2Jrjc2Flck-lxlwKd75mRuUrY62aYXbRLdCWV1Ef-vNEiBvqvuCiuSN0o57AUYeiq_XT7BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/2934" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knoUwERBkMrCbTaSKLEWn8xQBQL7ceSDlSUn9bu-5DRtMsXi-7_DemIiDCKQoMlit94GCv_PFbhlxK2dFRxc3EgQu25-y_f5OcHThOxjO4u5sdB99d6W6KWqIzOl3RHCGT7XYsptFMpJTvZBhCsEYp6giLJrT4Ww8Hw8GKjn9Quz75hUG8X1XzY84zpsUxVA5Wxmdthv7YhHuCsMoyvlTdn_BsVlX9fPjv6jhpMCzMwHSNWLXNBQNBz1_SdklBkwZ6qxOGZbctk7SEIWdaNb7o6afSXjTpXtI1OVPnwe2AtBHK0R8Qh6pg14Ye_XZrWXBlaltB0CyZ35f8aFv6acCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKeHUjpuof4cqIb_zn3WG5swzWqVOzRsiFiWqCup57m-0qcdP6CrL3w05shAYousEYVsMRvyPHjoqieQ6qfcGsF8hNPKOXb8NPSrIwNYSWwMlGUWhrSpvBvGA6Bze8reJRtZcH6z47ZQY2ULFX3acdPGH7X4l_-ba-TWDCHOF8RHbzugJz3LvmWzEU6pTWGHJTv0WTv-IKzmfmyACYWVgBj9S7lCWekg6DrJF79sEWoCTHzNbJTHLgQSwi-tqFEd17mWtEoixd68SuMXbH5ku4NWwsi8UaxSeBHbnyxDAur7-a7Zwei-NCIHnJhlYpeGblSgcsBLOb75G9RF399XIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2931" target="_blank">📅 20:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2930">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkuWjOFWvSqliKY-2b-mYz5gLrsGTNN0m0TCkDdGbSp_ZMFrxVZNWfs78u4-1QzBNWjgIuJ9H01wYnrMFzdGMETd3iIfLWwxAZ1AJSkqbYw0Nksnbyhgz1_wOLV3o2icWfOZVSnFxUdCBySicWIeaERwiiGJDb-1VjeSmL6cnWcNi9Dynf0LHqXxvLafEIcQS6MoSZiGIfcppHXPGS875U6l_nmuI06v4n8PBZNxCUW8K1hme-oeVDXPbCcSo8vJ5B-sjEygkqd2X9Gpg8tR61rE39lJA3hM2ztefcyo8cY2E1Uzir80lRF0TQOddh-kIWVEe5WpXnMikf7yQuIAMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sY1311QC14NsXpgx5N5cFlcefOE5k9CkMrTaFMW75Fbb1DLxE8zVb9hxqSjUXI01r1i5ANwXw8qnHLWhzmnP7M-m0J1onL3UosmPZGyONOhLwqATooftSxb5sB0B8BqIZx9ffZvQFLTd7xeFPjJnmU7xm7R9Q1BSFz4xEaBGIfldpC5zsLZQfOTd2za76w2AHJKVWm1FA8s2mcXq5qXknONOxGYSmwBri18CYZ-DO9wwZzbuLnD_fLkZpJGxtBBx1FkeJhQ-3CUNdUoLV7iIiTXl-t_CUkqTuGRtirHejGs8ad1SXr0sgIpe9RI7blyPxn0u8-KiKSBsFEa1qEgKwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7ElCzTVd0Yb189a9NRXWzz4FWLiJK8x2KKtWAbrrqzjNb-mtN7fW8zNfIrwGXTdyWsg_ltEk2TXEYu8zVbvJT3ZaND49kx06vu_7Hto7ONLXy5xsWAmh_OAX5q8kmrs1oV9kB0yJCbETUO2g4NW5WAaNiYTCXwXQv-6V0R3MlZ2RSydFiiSpo6zQSpJQSSockAr5GhAQ5bBilreh5PsvRZzNNM8zbJCLEPTpcKsEsLUVYe9mA8nfQdwOHW9hAePMcwrwK1Pza2-tslBAufQGHgEI_cELkqs4bawHz6EjbSOwfk6ObBsgmJNZ6kYmta-L3yu_QdUAsBewt-oO_HjSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتار آدم های معمولی با هوش مصنوعی
در مقابل
رفتار برنامه نویس ها با هوش مصنوعی :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2926" target="_blank">📅 18:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2925">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTQZJFArbBv6K3bY8K0Z_tTG_hzoeorgSzfstakUnvXC0CSb79j1vfkyLY7KNrSXOliiO-Ss_j6NiDxLjrCr_eUYkx9FZizsnTR3M3myrohP_JuA6btiRb2uSSov8ZNvrTmDfNkoP6akn-ITkPyHFwBHangQTlFkNgRuA7abZ5Zww0Fdcyo2Q3MjRY2H-Ejg_FE_UL6yOTdRUxPITDQrMVB-z2l3bV50OzQg2xY55Fi6WvfySrIVEIitGszmyhVOzmN-o1LnIuQPa30QU00B1iDzJcT6ugD5bYxm8A6QJFaDlBzkS7JYxBAz3YTylNHelPngY80-yXbmK4odC3VLJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2925" target="_blank">📅 16:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2923">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2923" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
