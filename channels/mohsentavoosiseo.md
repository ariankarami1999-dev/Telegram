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
<img src="https://cdn4.telesco.pe/file/YKCziE9IZPcsvv-HBWETOa2sObC4ezLHsg9uqxjzrQ88gRMHd9JW5WRbVd8wQM3fkMnqPwKHi7s6PcCtz94N_HXJHLY_mTS72foBkhIggzoDIl4SujMOCzPiJgt0KP4-xnEmqgzJaZ8ESPfm67m2_FOFGsqyLr1fZdDbhRRzKeDHlQSYdNSTt4A7r1UzlgD-H2Urm5WWkTjlWdd3AJ12wkGLugifj2OBbVmLI2WHfiG5GO_V39LkyUyKp4ZH4wvcK5ChRuXKQvIjLV3wN8Bzu3v1j57VVd52mznXyclZavnjEovxgszUYB03BmDhwg7aygy7R_dCdCJuFtdlS0qW1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 7.54K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 کار من تالیف و تولید هست✅️.❌️نه ترجمه و خبر و  گرداوری❌️دوره:mohsentavoosi.com/course/seo/خرید دوره:@mohsentavoosisupportyoutube.com/c/MohsenTavoosiInstagram.com/mohsentavoosi.seolinkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 01:29:10</div>
<hr>

<div class="tg-post" id="msg-729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">لینک رویداد چند روزه رایگان و آنلاین گوگل درباره AI Agent اینه. این رو گفتم میبینم برای محکم کاری، بعد ضبط رو شروع میکنم:
https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google?registerForCourse=true
ولی معمولا پرت زیاد داره طبق معمول. یک ربع مفید یا یک دید و ابزار بهتر ازش دربیارم کافیه برام.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/mohsentavoosiseo/729" target="_blank">📅 12:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-728">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک آپدیت بزرگ بین المللی بزرگ هم در راهه. کلا صفر تا صد سئو ولی با AI و چند زبانه و به هر زبانی (حتی نه فقط انگلیسی). این به روز رسانی، یک Game Changer هست.
هرکس دوره رو کامل دسترسی داره، (اقساط کامل)،  به رایگان دریافت می کنه.
بعد از اینکه رویداد چند روزه گوگل درباره اتومیشن و خودکارسازی رو دیدم، ضبط رو شروع می کنم. این رویداد هم برای محکم کاری میبینم. چون خودکار سازی دیگه اصلش با کلاد هست. خیلی قرار نیست شما درگیر شید.
پیام پین شده برای تهیه دوره هست.
اسپات پلیر از خارج هم در دسترس شد و راه حل با وپی انش هم با هزینه جدا هست. ولی امروز در دسترس شد از خارج از ایران.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/mohsentavoosiseo/728" target="_blank">📅 12:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-727">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پشتیبانی دوره قوی تر از قبل شروع به کار مجدد کرد بعد از یک وقفه دوماهه به خاطر جنگ.
پشتیبانی دارای حریم خصوصی در چت تلگرام هست. وبینار نیست. روزهای خاص نیست. آزادانه هست (برای من آزادی خیلی مهمه). زنده هست.
و توسط اشخاص قوی و قدیمی از بچه های خود دوره انجام میشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/mohsentavoosiseo/727" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-726">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوستان گرامی، کانال بالا، کانال محمد قاسمی هست که ایشون دوسال با من همکاری داشتند و بسیار شخصیت باسوادی هستند.
اما مسئولیتی هم بابت معرفی و توصیه کردنم نمیپذیرم. استفاده از مطالب هرشخصی که اطلاعاتی داره، کلا مفید هست.
من منتورینگ برگزار نمی کنم. ولی ایشون انجام میده.
با تأکید بدون قبول مسئولیتی از سمت من (بابت معرفی کردن)، می تونید با ایشون منتورینگ سئو داشته باشید.</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/mohsentavoosiseo/726" target="_blank">📅 11:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-725">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسئو با محمد قاسمی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Megop_serp_analytics_2.0.4.zip</div>
  <div class="tg-doc-extra">33.9 KB</div>
</div>
<a href="https://t.me/mohsentavoosiseo/725" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این اکستنشن فقط یک ابزار نیست، یک مزیت رقابتی سخت و مهار نشده  است واقعیت این است که آینده سئو متعلق به کسانی نیست که فقط بیشتر کار می‌کنند. متعلق به کسانی است که هوشمندتر، سریع‌تر و دقیق‌تر تصمیم می‌گیرند. و در قلب این تصمیم‌ها، Keyword Research قرار دارد.…</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/mohsentavoosiseo/725" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-724">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسئو با محمد قاسمی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd6ab0dbf.mp4?token=fc_skGtG00pbm88lLIqpexGcWqxNbgK_pWs145y9pY93eskU1vX-5Z_EP5LjNbX4T_eXlROi92NdVRZKiQ-sbRMAsmmf-d_BLHr3F6c6G-f1f0MF4xPSYNCrC1rEJR_eieHwH3nLciEaa-x7lFv1rPU-dmSX4w_s1EgtxXtqrwz1W_DXZB9Jqd7eTwNXS-98tPkRcO3Vx6aEteQBENBoLt5E3D5trIrktuVpn-ZSzXxs7skb76WXQbukDDZHddMNBVXW-6QPGF9H8WYxfezcBo0_u6DU54Gq5LUxU6ErkaKFfHlWO6f-u5RgtW4GRkaxJ1iSDQ9JxIYGwl-fgRideg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd6ab0dbf.mp4?token=fc_skGtG00pbm88lLIqpexGcWqxNbgK_pWs145y9pY93eskU1vX-5Z_EP5LjNbX4T_eXlROi92NdVRZKiQ-sbRMAsmmf-d_BLHr3F6c6G-f1f0MF4xPSYNCrC1rEJR_eieHwH3nLciEaa-x7lFv1rPU-dmSX4w_s1EgtxXtqrwz1W_DXZB9Jqd7eTwNXS-98tPkRcO3Vx6aEteQBENBoLt5E3D5trIrktuVpn-ZSzXxs7skb76WXQbukDDZHddMNBVXW-6QPGF9H8WYxfezcBo0_u6DU54Gq5LUxU6ErkaKFfHlWO6f-u5RgtW4GRkaxJ1iSDQ9JxIYGwl-fgRideg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این اکستنشن فقط یک ابزار نیست، یک مزیت رقابتی سخت و مهار نشده  است
واقعیت این است که آینده سئو متعلق به کسانی نیست که فقط بیشتر کار می‌کنند.
متعلق به کسانی است که هوشمندتر، سریع‌تر و دقیق‌تر تصمیم می‌گیرند.
و در قلب این تصمیم‌ها، Keyword Research قرار دارد.
اگر این مرحله را با یک ابزار ضعیف، workflow پراکنده و تحلیل سطحی جلو ببری،
هزینه‌اش را در همه‌چیز می‌دهی:
در رتبه‌گیری
در تولید محتوا
در زمان
در انرژی تیم
و در فرصت‌هایی که رقبا قبل از تو می‌بلعند
اما اگر اکستنشی داشته باشی که:
فرصت‌ها را سریع‌تر آشکار کند
intent را واضح‌تر نشان دهد
من همیشه گفتم و همواره خواهم گفت:
intent کاربر استراتاژی است و keyword Research فرمانده است
چیزی که شکاف‌های محتوایی را زودتر نمایان کند
تحلیل رقبا را ساده‌تر کند
و تصمیم‌گیری سئو را از حدس به داده تبدیل کند
آن وقت دیگر با یک «ابزار کمکی» طرف نیستی.
تو یک سیستم شتاب‌دهنده برای رشد ارگانیک در اختیار داری.
این همان چیزی است که سئوکارهای جدی را از سئوکارهای شلوغ اما کم‌اثر جدا می‌کند.
🖋
شاید پرسیدی که چرا اینهه سئوکاری که میشناسی هیچ کدام هیچ نتیجه ای ندارند
آیا واقعاً مساله بلد نبودن کیوورد ریسرچ است ؟
یا مساله در ساخت بینش است ؟
✨
همین حالا این اکستنشن را وارد بازی خودت کن
#کروم_اکستنشن_سئو
#کروم_اکستنشن_Seo
#chrome_extension</div>
<div class="tg-footer">👁️ 862 · <a href="https://t.me/mohsentavoosiseo/724" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-723">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سوگیری شدید و نگاه صفر و صدی در جامعه ما
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/mohsentavoosiseo/723" target="_blank">📅 17:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-722">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برای پروژ های فارسی، ابزار های ایرانی کیورد ریسرچ کافیه.
زمانی که من اکثر سال ایران بودم هم من اشتراکی نمیخریدم. حوصله دردسرشو و قطعی مدامشو نداشتم. همه سه سایتی که اشتراکی میدن همینن.
برای پروژه های خارجی هم یا با پول کارفرما یا چند ماه یبار یه ابزار میخریدم. معمولا منگولز.
اما درک می کنم که یک پنجاهم قیمت اصلی وقتی پول میدی، باید هزار تا اکستنشن کروم تنظیم کنی که اون اشتراکی استفاده کردن ها توسط اون ابزارها لو نره. با دستکاری سشن و کوکی و وی پی ان و خیلی جزئیات و مکافات دیگه. که از نگاه بین المللی، عملا کار غیر قانونی هست. هم فروشش. هم خریدش.
نمیشه هم پول خیلی کم داد هم دردسر نکشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/mohsentavoosiseo/722" target="_blank">📅 16:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-721">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اون 20 نفری که تا این لحظه جواب این رو بله زدند، خیلی دوست دارم بدونم چرا منگولز نه؟
من خودم منگولز پریمیوم 40 دلاری اختصاصی میخرم همیشه. یه سئو هست و یه کیورد ریسرچ. کیورد ریسرچ شوخی نداره. مهمه. مهمترین بخش سئوست.
منگولز خیلی بهتره در کل. ارزون تر با محدودیت کمتر با کارایی بیشتر. البته برای کیورد ریسرچ فارسی، ابزار های بومی ایرانی کافی هستند و نیازی به ابزار خارجی نیست.
برای تحقیق کلمات کلیدی کلمات فارسی، ابزار اختصاصی و حتی اشتراکی خارجی نخرید!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/mohsentavoosiseo/721" target="_blank">📅 14:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-720">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🟢
⭕️
نتیجه گیری:
با توجه به اینکه:
⭕️
تعداد فعلی رای ها که همین الان که دارم مینویسم 200 تا "بله" شده،
❗️
این هایی که بله زدند نمیخرن. نرخ تبدیل پایین تر (خوشبینانه یک سوم) خواهد بود،
❗️
هرکس رای داده اگه اولی (همه ابزار ها) رو بله زده، دیگه نمیاد اون یکی ها رو بخره و عملا تعداد کل "بله" ها رو نباید جمع زد،
❗️
در آینده رای گیری بیشتر میشه. اینستا هم استوری بذارم. 10 برابر در نظر میگیریم.
طبق براورد من
❗️
خوشبینانه 400 نفر ماهانه میخرن. بدبینانه 100 نفر. بعد از 6 ماه.
❗️
سود خوشبینانه: 800 تا 1600 دلار. بین 200 تا 300 میلیون تومن.
❗️
سود بدبینانه: 50 دلار. معادل حقوق وزارت کار. بین 15 تا 30 میلیون تومن. عملا با انرژی که ازت میگیره، ضرر مطلقه. گل فروشی سر چهارراه به صرفه تره.
❗️
امکان توسته پذیری با تبلیغات و پشتیبانی قوی و زحمت زیاد در دراز مدت تا 2500 دلار. و با اوج ناامنی با توجه به تغییرات تحریم، دلار و خود ابزار ها و قدرت خرید کاربران.
نتیجه گیری:
با توجه به دردسرهای زیادش، جای مانور پایینش، پشتیبانی سختش، توسعه پذیری بسیار محدودش،
ورود نخواهم کرد
😅
به فروش ابزار های اشتراکی سئو.
بلند فکر کردم شما هم استفاده کنید. هم استفاده کنید هم انتظارتونو از ابزار اشتراکی 1 تومنی که همه چیو با هم میده بیارید پایین و با واقعیت های میدانی آشنا بشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/mohsentavoosiseo/720" target="_blank">📅 14:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-719">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-poll">
<h4>📊 حاضرید برای Ahrefs ماهانه 1 میلیون و 300 هزار تومن (1300) پرداخت کنید؟ با ماهی 50 تا اعتبار. یعنی 50 تا درخواست(request).</h4>
<ul>
<li>✓ آره حاضرم</li>
<li>✓ نه! No! Hayir! Nein! いいえ! 아니요!, لا! Non!Yox!нет!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/mohsentavoosiseo/719" target="_blank">📅 13:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-718">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-poll">
<h4>📊 حاضرید ماهانه برای سیمیلار وب Similarweb ماهانه 800 هزار تومن پرداخت کنید؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/mohsentavoosiseo/718" target="_blank">📅 13:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-717">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-poll">
<h4>📊 حاضرید ماهانه 1 میلیون و 400 هزار تومن(1400) هزینه کنید برای سمراش؟ Semrush</h4>
<ul>
<li>✓ بله</li>
<li>✓ نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/mohsentavoosiseo/717" target="_blank">📅 13:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-716">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-poll">
<h4>📊 حاضرید برای ابزار Keyword Tool ماهی یک و نیم میلیون تومن(1.5) هزینه کنید با روزی 5 درخواست؟</h4>
<ul>
<li>✓ بله حاضرم</li>
<li>✓ نه اصلا!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/mohsentavoosiseo/716" target="_blank">📅 13:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-713">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-poll">
<h4>📊 حاضرید هر ماه فقط برای ابزار Mangools (کیورد ریسرچ)، 500 هزار تومن هزینه کنید؟ با روزی 25 تا درخواست.</h4>
<ul>
<li>✓ بله حاضرم.</li>
<li>✓ تا ابد نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/mohsentavoosiseo/713" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-712">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-poll">
<h4>📊 حاضرید هر ماه انقدر هزینه کنید؟ماهی 3 میلیون و 700 هزار تومن برای همشون. ولی ابزار ارزون تر کیورد ریسرچ رو فقط میذارم:   Ahrefs,SimilarWeb,Mangools KWfinder,Semrush</h4>
<ul>
<li>✓ بله حاضرم. میصرفه برام.</li>
<li>✓ خیر. به هیچ وجه.</li>
</ul>
</div>
<div class="tg-text">قیمت تمام شده (سر به سر به ازای هر خرید) برای هر کدوم از محصولات زیر با فرض اشتراک بین 20 نفر. برای یک ماه.  نرخ محاسبه ریال = 180 هزار تومن با احتساب کارمزد تبدیل و سایر موارد خرد انتقال پول. رنده شده به بالا به ازای هر پنجاه هزار تومن.      Ahrefs= 6.5$…</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/mohsentavoosiseo/712" target="_blank">📅 13:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-711">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قیمت تمام شده (سر به سر به ازای هر خرید) برای هر کدوم از محصولات زیر با فرض اشتراک بین 20 نفر. برای یک ماه.
نرخ محاسبه ریال = 180 هزار تومن با احتساب کارمزد تبدیل و سایر موارد خرد انتقال پول.
رنده شده به بالا به ازای هر پنجاه هزار تومن.
Ahrefs= 6.5$ = 1200
نفری 50 تا اعتبار در کل ماه. 50 تا request
1 میلیون و 170 هزار تومن.
KeywordTool.io
= 7.5$ = 1350
نفری 5 درخواست در روز.
1 میلیون و 350 هزار تومن
Mangools = 2.1$ = 370
نفری 25 کوئری بخش کیورد ریسرچ. در روز.
370 هزار تومن
Semrush = 7$ = 1260
سمراش جوری نیست که به درد اشتراکی دادن بخوره. چون باید سایت ثابت بدی. عملا استفاده 20 نفر مقدور نیست. فقط بخش هاییش قابل استفاده است.
دلیل خرید Moz هم درک نمیکنم اصلا اگر کسی میخره!
Similarweb رو میشه به بیش از 20 نفر داد
چون حالت کردیت و محدودیت تعداد درخواست و روزانه نداره. این رو میگیریم 50 نفر.
Similarweb = 4$ = 720
720 هزار تومن.
این فقط قیمت تمام شده خود ارائه دهنده ابزار اشتراکی با این تعداد کاربران نوشته شده هست به ازای هر اکانت. سالانه بخره حدود 25 درصد کمتر میشه. ولی سالانه ریسکش بالاست برای فروشنده.
حالا هزینه جاری و توسعه ابزار و نگهداری سیستم و پشتیبانی هم حساب کن. من میگم بدترین حالت معادل نیم دلار و بیشترین حالت معادل 2 دلار به ازای هر کاربر. به صورت کلی باید روی قیمت ها بیاد. تا اینجا که هزینه خود فروشنده بود.
در حالت فروش دسته جمعی همشون با هم، باز 2  دلار روش میاریم در بیشترین حالت.
هزینه جاری در کمترین حالت ممکن: 50 میلیون تومن. ولی بهتره 100 در نظر بگیریم. حداقل 500 دلار. در ماه.
میزان درگیری ذهنی و دردسر فروشنده: بسیار بالا.
سود فروشنده در صورت داشتن ماهی 1000 تا کاربر ثابت(که عدد بالایی هست):
در کمترین حالت به صرفه:
90 میلیون تومن - 500 دلار
منهای هزینه جاری: در حد حقوق وزارت کار
در بیشترین حالت به صرفه(که کاربر کم میشه چون نمیتونن پرداخت کنند):
360 میلیون تومن. 2000 دلار.
منهای هزینه جاری: بین 100 تا 200 میلیون تومن.
مشتری واقعی پایدار بر اساس واقعیت فعلی هم، 1000 نیست. هزار باشه باز هم عدد وسوسه کننده ای نیست.
نظر سنجی زیر رو میذارم که عدد در بیاد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/mohsentavoosiseo/711" target="_blank">📅 13:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-710">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">با توجه به افزایش تقاضای ابزار های اشتراکی، من قصد داشتم خودم به این حوزه ورود کنم.
ایراد هایی که به سه سایت ایرانی ارائه ابزار اشتراکی خارجی داشتند این ها بود:
- پشتیبانی ضعیف
- قطع شدن مداوم ابزار ها و هدررفتن زمان اشتراک
- نداشتن محصول مورد نظر
- طراحی و تجربه کاربری ضعیف.
حالا برای اینکه من بفهمم صرف مالی داره ورود کنم یا نه و شما هم بفهمید(!)، نظر سنجی می کنم از شما.</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/mohsentavoosiseo/710" target="_blank">📅 13:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-709">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbCp7HqEgfO8tT9u_djj84ts16XgalikOYYzCMHWCIMOsCJMw0WH7C7g4rgWRdm58GYm2dwJJTr8qbQrV0WEs9ZWcJ80VQAbjjlk-cteOjb1ePeib0cTeRelfrYwYwKo71zrlckEjp3QQLUFll4wrwPL3xujhbPem585Pf8luPs_SDLlxB7iYQy6BWAk7a2ONsJIR6TgIUAe5wlrEzQKuS4Va8eehkM7F-rfQOILSaGEHfioYLveloQUGbTvdw4sxM45D0bzlz997hvi6xdiJSMUEsBgpo5xBunyZtlORshgkZpuuYCalPfgrsHXCVhbXt02W3VoBQSKTGCXV7Qh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر با AI زیاد سر و کله زده باشید ارزش جواب کلاد رو میفهمید. هرچند که نسبت به بقیه معجزاتش چیزی نیست.
وضعیت:
گفته باید رو سرور نصب کنی. ولی به جای "سرور" گفته رو سیستم. منم اونو بهش گفتم.
حالا AI های دیگه بود چی میگفت:
اره حق با توست. باید روی سرور نصب کنی.
جواب کلاد:
منظورم از سیستم، همون سرور بود.
تفاوت رو متوجه میشید دیگه؟ خیلی تفاوت داره ها! خیلی!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/mohsentavoosiseo/709" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-708">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3494a006a0.mp4?token=MEhgxLVM4IF_hSSeFrOM1kRvAEQSLnvgqDoTkVzfDKT4vwWUYEfz4PA3pHAW0TD_eK1O5ARax3NqPmXHhDLtZxULHFC14qls9hRMhMYbiJOLVByQ0Tahhg4_zn22SZJ4FhewRwF-x4LizzJV2VO14X2YWSyUSH75ai0XhkzWJTOkAAbgK7xy6bIutM55Pclspmegvak-_bbj7fyXtHipKolJE0kSGLVixe9SuHF8OXvONtGPg0bGKubKWoH-F6235sgipD0MhJZaUGHxYJQOSjz-hGGBPsElFKWMm1x82HOG0qJMMabBPuvl4g4hZPTWEOC0Cpf1mueCZtm-URbjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3494a006a0.mp4?token=MEhgxLVM4IF_hSSeFrOM1kRvAEQSLnvgqDoTkVzfDKT4vwWUYEfz4PA3pHAW0TD_eK1O5ARax3NqPmXHhDLtZxULHFC14qls9hRMhMYbiJOLVByQ0Tahhg4_zn22SZJ4FhewRwF-x4LizzJV2VO14X2YWSyUSH75ai0XhkzWJTOkAAbgK7xy6bIutM55Pclspmegvak-_bbj7fyXtHipKolJE0kSGLVixe9SuHF8OXvONtGPg0bGKubKWoH-F6235sgipD0MhJZaUGHxYJQOSjz-hGGBPsElFKWMm1x82HOG0qJMMabBPuvl4g4hZPTWEOC0Cpf1mueCZtm-URbjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/mohsentavoosiseo/708" target="_blank">📅 17:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-707">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKzcACWaGQRqLc8UIU7UiNepC8ZrLj778DOU--G78AGfoVtw6eF8nJ0vnxl5-OhXzoTlCJXneOc1yN1RfPZvseIdDBJnxDlFgbNI6dk9pkRRmCtLLdOZ6B_dyjDdYGvBr6HaGQWXv5suXTLY28CeCeyQgxgSl16Kvf_EDHJ4t8pgrVRno_el6KCtidq5BCD9Wz7oPmTFxPLfu92HupfCobCgRlWFysfxtIug3bzOC6rKY9YULl2YmAYx7CGsfC_h8SV49QibE4Yxjp1dSH06ZtO_pwxNLhIMfU3LTCz1VfUrJJh8UOYPXGf809hy6JFhSBAvHpnnIUMSv-mCvWPoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کم فارسی انگلیسیش چپ و راست هست. ولی همین کافیه تا عاشق کلاد بشید!
اه! انگار قبلا اپدیت شده بود. بذار!
😅
😍
😍
😎
فقط هم ادا نیست. واقعا بازدهی و خروجیش عالیه‌.
هنوز خیلی ها از skill در کلاد استفاده نمیکنن.
در اپدیت دوره، علاوه بر سئو بین المللی(که الان هم یک فصل داریم)، این ها هم آموزش میدم و هرکس دوره رو داره، رایگان آپدیت رو دریافت میکنه. فعلا زمانش رو نمیتونم بگم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/mohsentavoosiseo/707" target="_blank">📅 16:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-706">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a993e8989.mp4?token=fUhtRNEUWIGyWlwXDrXuK5lQ3j81CbGrr8nt2vPEHYmmN1NqZFhnIiLsGszmi6hnNVU3thMODjEFbQmosWfew6kNlX-vmD8jKtqZp-fzj5_LaIjNC5zizVo4mVcV9eruumic8hyifNMebjlzu4ALQTrfKCcJbzxvf3x-L6DqAof_OU4bYZvND1BAWlGSL44kQeyt1y-kZWkWPWDxk3lnkheTxNFnxjSAt18se6pTW8a3MaCmxU2hOtLJ3yZTV_0TDCdKHXMq9oIKDBnWFKPqzz1ryuyL0CwPey8mem1HM6gba8i-ea6W6tVTK2LMPMXlWzVZGbijLLYOooN0G6v5RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a993e8989.mp4?token=fUhtRNEUWIGyWlwXDrXuK5lQ3j81CbGrr8nt2vPEHYmmN1NqZFhnIiLsGszmi6hnNVU3thMODjEFbQmosWfew6kNlX-vmD8jKtqZp-fzj5_LaIjNC5zizVo4mVcV9eruumic8hyifNMebjlzu4ALQTrfKCcJbzxvf3x-L6DqAof_OU4bYZvND1BAWlGSL44kQeyt1y-kZWkWPWDxk3lnkheTxNFnxjSAt18se6pTW8a3MaCmxU2hOtLJ3yZTV_0TDCdKHXMq9oIKDBnWFKPqzz1ryuyL0CwPey8mem1HM6gba8i-ea6W6tVTK2LMPMXlWzVZGbijLLYOooN0G6v5RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که بحث مقایسه مترو ها شد جا داره بگم، مدیونی اگه به ایران بگی جهان سوم.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/mohsentavoosiseo/706" target="_blank">📅 11:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فقط هم کیلومتری مقایسه کنیم باید مساحت کل اون شهر هم در نظر بگیریم. استانبول ۷ برابر تهرانه. مساحت توکیو ۲ هزار کیلومتر. مساحت تهران ۷۵۰ کیلومتر.
با همین فرمون سرچ کنسول گوگلو تحلیل کنی تا ابد غلط در میاد تحلیل.
مثل نگاه کردن به avg position کلی برای تشخیص رشد سایت!
تازه طرف فکر میکنه چون حرفه ای به کلیک کار نداره پوزیشنو نگاه میکنه! اینجاست که کسی که فکر میکنه حرفه ای تره آمارش غلط تر میشه!</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/mohsentavoosiseo/705" target="_blank">📅 11:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kehIqXcwFdoKVd-5xq_i60lgFqRxQl4ehRjF-wN2dqYsHHyIcT3KpxoqiPMhlhi2h8QA6hHYVzRIEWR-vRxx_hSxYuhr-6qr65zGJxN6lVzOgSC8RiXgJr7WO5szPGUhFP1DYtMmvUUQMBPYSRMhxVHuz1dnbOxf_Ri_lMFtDVoAfLJIKVaDDPOQPJGOWkO8gcAFJa2n3oP8st31-uofRb75jCrsVsl8nnEvMTP9CDdGGBMg2UdpxIi0j9L9rCusaxDAROl4NqBgdfMpI7iOnHlLmFQCx2r6woJExu2RHgBe8CfhE_2dMHmEGJPBIDYgEXw_ZsoCgTfJiQ1C-UXXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/mohsentavoosiseo/704" target="_blank">📅 11:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-702">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZQ-XLeP_o6LaxN8tsTBxbeyb8iKBzkSw9s5kVBXsJXsOOgkTsrwuv_F5S2nOPer1R9F8BzpYrNRzCOFfTFuAqkua9Mf70M_p7dqYHWmsrcaqffbojABa6Kt7JQ0eJ5cG03UPzDj5Vy0mbRzbAnPnnBATqHq4qzp-7KyVQ0O8lENp-thedXuApgrMLbzvvFsgYTL7lpAkX6eLq1iQAUdK3t72HHiTYQxx7Hj2Hu7NeLExGY3u1u58JM0VrNegxLXLhatWoqRam9jTZfxRKNnlghRX-FVE3pOelxsXD0AuSBPw4e5g6ELjucklaCt_vcWcfbWOgIpSWHEb_VAuyEW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سئول کره جنوبی</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/mohsentavoosiseo/702" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-701">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1--PsdghzG9GzwW1UfoSdIyaZuv3lxyV-25rcA34KVzWKQoICOFLiNBMg5E1SApyo-89Kx_XSkM5OtAmn0QuVXz0Kuk1niGdSp_pL5gjagMFY83-JFR5uQV0c8CSCuhVvfeGtiMsC1uvt50CkU4s8M6hEhdms9_j7TI5oVTUlspqoRla2UBtqgWKsGmFthKGLpnSySTG9pHDtNDMZDH1paAKpCd9eow0QdIG1Mj5aVWQ_j44uqytGVACd2erw7Q_50vu2DoDgPKH58SyowvrXR9KT1nRN-uu0G5k-wHjgMddAO992ZJWBDbOJZojhQa2x-mz1jNvEeih1_J4gKPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/mohsentavoosiseo/701" target="_blank">📅 11:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-700">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8eeWmfZfiUkS7TH6mbKRxP2EY0ajK-pgNhN__NBocd4FL0Z5A0iWqg8D5PtvN3r9rjhBNBPi-HxH_84RoazHC4pQFzwXuZzYVr6yWHddXQkUeB-EhT2XGjAHyOsDiQEfUQisg1vc_UA32RGapbXGEJgtjrLL2wWpYGL01HO-HwQ1svLgMyphPCJ0hMkzkRRyPIvYoaqG7V4ZxbkEID01eyig5zsd57r86wnypfdw56zuAcfKFioKa3nBeB-hZeeJYiD0OtoCPqSF_Xt7eP0FDYW3z2qBr5CY_dy1n2BFQ2bdVMaeAqsqe3ARQujK8Fm-Ds2M6tjh9rEmjZbgZcHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/mohsentavoosiseo/700" target="_blank">📅 11:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-699">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/mohsentavoosiseo/699" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-698">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq5P5w_EMl_Nr5VEpISRaUZL3D9gElqlGxZ3d4dCaXJ7XAy2qWaAsiMcHPj-ciK-OpBNHZfQA4Nl5CU8GpI3UQ4CAVfKakK0xV5jaG5KXmFfS9iq3b5xnFvh2IxB7ZQ2c9PCmG4VzZatoQLeB9wJLtTYERGxBebXJGTel-IZPF6JiFv__XTe1Ipiw2k1b7boG0S9PJid2ySXFsb3bqFFC5eK1Q2767-XeruiqOZ6AnJyBKs7wjVI1ovrhcTLOws6P2IcU5qNTVd_U9-pNzgsJtnbpOcYTTmAiEqRcm5roIwNKCWfUnYBMJa7c_e3JLGgI3WrFS1YH35s1-qIeD1nGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/mohsentavoosiseo/698" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-695">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">احتمال جنگ همچنان بالاست. کارهایی که برای دسترسی گوگل و از خارج برای سایتتون کرده بودید رو همچنان نگه دارید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/mohsentavoosiseo/695" target="_blank">📅 20:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-694">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvB9uU7eYhnIlDtrPLVmXGYjUA4NU-FxV9Y99TRjNXgjtO7ksYYgY4DHHZPcttwZ8_10zoh9NfUUWLxmima9UloIH2uTu65BIHB1vECS6EL2NW33Xa6WG2oqWB5S3Gwr5bsbPNU5hMlw_grJB2Di6fMg6GsVD7o2xfCC7rokNs7VNkd45DgVIbpIqky6TSN0oyVi8ga5OQm7bZv6GoqZQWr8EgBgvARJXHuMoD_5pHcA3tQxVTTry7FdV42_bpq7jA2Iisw9PHwi1HVGUD_ilA8TegeWXBYAemTJ2nd7rsdPJLqoT1QoWjy-wY1VDusJKcJc_u5TAm-M3UkKMcU6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز اینترنت وصل شد یه عده بلاگر شروع کردن به سئو مُرد گفتن که AI اومده.  سرچ کنسولای ما که کلیک میگیره هم توهمه.  لندینگ میسازیم بصورت گپ(رقیبا نساختن) ورودی و فروش مستقیما بالا میره هم تو دنیای موازیه.  پول هایی که به حسابا میاد ازش هم فقط تو ماینکرفته(دنیای…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/mohsentavoosiseo/694" target="_blank">📅 20:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-693">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">باز اینترنت وصل شد یه عده بلاگر شروع کردن به سئو مُرد گفتن که AI اومده.
سرچ کنسولای ما که کلیک میگیره هم توهمه.
لندینگ میسازیم بصورت گپ(رقیبا نساختن) ورودی و فروش مستقیما بالا میره هم تو دنیای موازیه.
پول هایی که به حسابا میاد ازش هم فقط تو ماینکرفته(دنیای خیالی بازی) و واقعی نیست.
ما هم تو خواب، پروژه های کانادا و آمریکا و اروپا و حوزه خلیج فارس،  دستمونه. واقعی نیست.
کارفرماهای خارجی هم تو فیلم Lost مردند و تو دنیای موازی دارن کار میکنن با ما.
گوگل ادز هم جمع کرده ما خبر نداریم. بالاخره نتایج سنتی نباشن ادز هم نیست. این کمپین های ادز ما هم همینطور الکی داره لیر و درهم و دلار حروم میکنه. دیدیم پولمون زیادیه گفتیم ادز بریم.
خجالت داره واقعا. ملت دارن پول پارو میکنن اما طرف صبح تا شب رو تختش دراز کشیده در حال اسکرولینگه و دنبال اینه که چه چیزی مُرد چی نمرد.
اره SEO مُرد. حله. رقیب تو نتایج گوگل کمتر خرج مام کمتر. استقبال کنیم از این تفکر.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/mohsentavoosiseo/693" target="_blank">📅 19:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-692">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">موضوع پزشکی بالا که ربطش دادم به AI هم نظر شخصی بود هم صرفا یه پرانتز بود و به معنی بی ارزش کردن کل علم پزشکی نبود.
علاقه ای هم ندارم کسی رو قانع کنم دربارش. شما پنتوپرازول و اس امپرازولاتونو بخورید تا آخر عمر و به حرف دکترتون گوش بدید. مسیر من برعکسه. هرچند که ۱۱ سال هرروز مسیر شما رو رفته بودم.
پرانتز بسته. برگردیم سر هوش مصنوعی و سئو
😎
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/mohsentavoosiseo/692" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-691">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c800f1b10.mp4?token=fikdRzAxvcuuhhkfwNGYoZhIAltN0kSVbheZ_qda_O4OGLDqX7RH3jIW_-fpwmQcaBoRah5tohY57lJbnQecwU2FkGg7VQQ7hmLlm9f-ExTJnQZ0P6pjtJ-qqXLHjE7WBg_nLjMo9zxcpeiD31JOEL52W7NXVDP-PhnwGBAZtl0xKIAjmJBXpaCi7sYYC3KU-lBigR2ejVM_-jU-qRi5Ox3pLriIIDDP35VqlE6g3aGPUzlDNEvDQuvo0qnup43PFGzGAbnm8YX0OcLCwNEuTl5v8DYJQudDJePgxIRsAedvgnk0S6V2rUuD5DETWVuYwyusJymLG8UASAE0LcM7ETDOkSHmDgjBFO860DFB_ILjI39bvSyGAI0mAaGZKgUULuShrQaADxpxI42FQoWMusr3GmK7CZ5JlB7RlWQrUetTB2SbC5NttZuFP3B1EFcD71ND3ti6IXObyAPv2U_55Ggjal1h_2pfzIUKmfkZVwjaeoou9HzlYJjweWvPxbXAVDD8cwdb5BaEMv9kXdb9njRGnHyk3y48aYM8uyf13w5K9e7CdOg1FFMOqk4Fj4Ncsy1Lr6o35fmPpPaE1HrHgaBTsI5d4Uq72tJMZgOh5GeSw9WZw3a25lS2x4UWEE3tijDmVONYBMu612n2CjEBrr587p44BArXtrvAh5wN2Y0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c800f1b10.mp4?token=fikdRzAxvcuuhhkfwNGYoZhIAltN0kSVbheZ_qda_O4OGLDqX7RH3jIW_-fpwmQcaBoRah5tohY57lJbnQecwU2FkGg7VQQ7hmLlm9f-ExTJnQZ0P6pjtJ-qqXLHjE7WBg_nLjMo9zxcpeiD31JOEL52W7NXVDP-PhnwGBAZtl0xKIAjmJBXpaCi7sYYC3KU-lBigR2ejVM_-jU-qRi5Ox3pLriIIDDP35VqlE6g3aGPUzlDNEvDQuvo0qnup43PFGzGAbnm8YX0OcLCwNEuTl5v8DYJQudDJePgxIRsAedvgnk0S6V2rUuD5DETWVuYwyusJymLG8UASAE0LcM7ETDOkSHmDgjBFO860DFB_ILjI39bvSyGAI0mAaGZKgUULuShrQaADxpxI42FQoWMusr3GmK7CZ5JlB7RlWQrUetTB2SbC5NttZuFP3B1EFcD71ND3ti6IXObyAPv2U_55Ggjal1h_2pfzIUKmfkZVwjaeoou9HzlYJjweWvPxbXAVDD8cwdb5BaEMv9kXdb9njRGnHyk3y48aYM8uyf13w5K9e7CdOg1FFMOqk4Fj4Ncsy1Lr6o35fmPpPaE1HrHgaBTsI5d4Uq72tJMZgOh5GeSw9WZw3a25lS2x4UWEE3tijDmVONYBMu612n2CjEBrr587p44BArXtrvAh5wN2Y0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در راستای پست قبلی.
مساله اصلی پست قبل، واکسن نیست.
صرفا به صحبت دکتر رابرت مالون که از محقیقن یا مخترعین تکنولوژی MRNA هست درباره بازار سهام توجه کنید.
که خیلی هم بهش گیر دادند که ببند دهنتو.
باید هم ببنده. چون زورش نمیرسه و قدرتشو نداره مقابله کنه. هرچند درست میگه.
و اونجایی که سخنران اول میگه CDC سازمان بیماری های امریکا گفته ما هرگز روی اون موضوع نمیخوایم تحقیق کنیم. (تو وقتی تحقیق میکنی از اطلاعات موجود تحقیق میکنی با AI)
وقتی نمیخوای تحقیق رو انجام بدی یعنی از نتایج اون تحقیق میترسی. و دیتای رسمی که ازش بیرون بیاد کل بازار و اقتصاد و سهام رو ممکنه نابود کنه.
پول، جهت میده به علم. پس تحقیقی که نمیخوان انجام بدن دیتاش نیست. وجود نداره. بعد تو میخوای با AI انجام بدی؟ اینجا باید بری سراغ تحقیقات غیر رسمی تر.
مثلا کبد چرب قرص درمانی تایبد شده نداره. اما تحقیقات پراکنده زیادی از اثر گیاه خارمریم روش شده(همون لیورگل)
هدفم فقط جلب توجه شما به جریان علمی غیر از جریان علمی رایج هست. و شبه علم هم نیست و کار  هم می کنه.
اگر قراره خلاف جهت شنا کنید، ChatGPT رو فراموش کنید. به درد نمیخوره.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/mohsentavoosiseo/691" target="_blank">📅 12:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-690">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اخیرا جمینای من از کلماتی استفاده می کنه مثل ای بابا یا کلماتی که احساس حسرت، افسوس و هیجانی رو منتقل میکنه.  این در حالیه که هیچ وقت در چت با من این کلمات به کار برده نشده.  تفکر نقاد هوش مصنوعی ها هم بهتر شده و کمتر دیگه علاقه دارند تاییدت کنند.  با همه…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/mohsentavoosiseo/690" target="_blank">📅 12:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-689">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اخیرا جمینای من از کلماتی استفاده می کنه مثل ای بابا یا کلماتی که احساس حسرت، افسوس و هیجانی رو منتقل میکنه.
این در حالیه که هیچ وقت در چت با من این کلمات به کار برده نشده.
تفکر نقاد هوش مصنوعی ها هم بهتر شده و کمتر دیگه علاقه دارند تاییدت کنند.
با همه تغییرات و بروز رسانی ها
الان نمره ۱ تا ۱۰ رو اینطور میدم:
کلاد Opus نمره 9
کلاد Sonnet نمره 6
کلاد Haiko نمره 5 ولی فقط برای خرکاری روتین و تکراری و بدون نیاز به IQ و درک زیاد.
جمینای همه LLM هاش در کل نمره 5 و 6
چت جی پی تی 5.5 نمره 2
چت جی پی تی با Thinkning نمره 2.5
انگار چت جی پی دیگه عقب موندست. نمیتونم آدم حسابش کنم دیگه. امیدوارم تو نسخه های بعد از 5.5 از این حالت آبروریزی نسبت به رقیباش در بیاد.
پی نوشت:
"خرکاری" و کار گِل (gel) معادل رسمی تر نداره. از همه AI های بالا هم پرسیدم اینارو گفتند:
کار روتین و تکراری.
کار طاقت فرسا و وقت گیر.
کار پر زحمت.
کار اجرایی روتین.
وظایف پایه تصدی گری(جمینای گفت. نزدیک ترین معادل)
امور تکراری و کم بازده (جمینای گفت. نزدیک ترین معادل)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/mohsentavoosiseo/689" target="_blank">📅 11:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-688">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ابزار های سئو خارجی رو به صورت اشتراکی از کجا تهیه کنیم؟ از سایت لیمیت پس! Limitpass.com ایرانی چطور؟ ابزار جت  سئو و کیورد چی و چند ابزار خوب دیگه...  http://limitpass.com/ https://www.jetseo.ir/ https://keywordchi.com/    کد تخفیف سه سایت بالا:  mohsentavoosi…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/mohsentavoosiseo/688" target="_blank">📅 13:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-686">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">احتمالا متوجه شدید که من زدم تو خط نادیده گرفتن. سرمو کردم تو برف فقط دارم فنی حرف میزنم. انگار که همه چی گل و بلبله.
علتش درد زیاده و خستگی. ظرفیتم به پایان رسیده. صدام در نمیاد. من سال ۹۸ گفتم فاز ملی گرایی بر ندارید هی بگید موتورجستجوی ملی. ضررش بیشتر از سودشه. تازه کسانی میگفتند که تو حوزه سئو فعال بودند. پست های لینکدین این موضوع هم لایک میکردند. اون موقع خیلی تنها بودم. تنهایی داد میزدم...
و کلا خیلی حرص و جوش ها. ولی خستم واقعا از دست و پا زدن بیهوده. از خون دل خوردنی که فقط پیرم کرد. از دیدن شرایط و صحنه هایی که جز فرو رفتن تو زمین کاری از دستم بر نمیاد.
اما اینو میدونم نباید همدیگر رو سرزنش کنیم...
به امید روزهای خوب.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/mohsentavoosiseo/686" target="_blank">📅 16:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-685">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOMTHtkchlhGtARdllI-O6X8BCN0--itiiPR2ZftAbQo2pKQp5deEB7Vx5e0koRErT77WzgFZE1HxExHmHR-WFh5jNPpoBiwmYV6oDDnu72N4sOaWvynSeM0CtJsQr9NTLXVD-xkMcfjrt3sgxqGYoSibtebFjY0UAlABvsEmZeTa1-9A2QPdg9AxGdIzQR3pYo9bbkhGB1hD5jbtJbeFgeiz4oD4tE0AVXFoURxivCQYeFMRyTO5NTO1T0yjsCbLrexoSp7MjgtkNj7PRaKxwZFpJX8N5tU3ysU3xwFcDF7rKDZx9xUpz2vXaeCStJgebQTWvAc-VvM4VNWxdvTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مرحله ای رسیدیم که هوش مصنوعی، خودجوش، خودش از دیتای خودش ایراد میگیره. خیلی خوبه. تبریک میگم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/mohsentavoosiseo/685" target="_blank">📅 21:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-684">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPZwd6Q7n7DGaRGN6DA03v7RkwRpqMtSG574AkmdFAXg9pJ-3flk8_Iya-YcPoS3ZJrCEcQAkYaMv-DCndRtFT3RKmVagUr8K4vdsI3_aQB5cql1OsluwM4E79tRL7-mZWz1INWjBu-iyvrBVVSEZ6Z8vvmhEoCAyXWcKkVgxpIK3eHQS_5z6ksvP-xj-Y9Um17VayZP69J1aTGIy9QRVTFw4ngH1zo5hplIVZQK2p4udENrfzRuTyg6F6zJMN4KBJuqmFXDPTQbYS1TaKpyuSeOA2yBAlQskFDDAzL-rGKxEDgrKyMEfrnzrF0rvfETyPh0IJ9p-4s8U-LPpf80hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من یه معتادم! معتاد کلاد!
خودش پیشنهاد داد یکی از قانون هامو که بهش داده بودم تغییر بدم و پیشنهاد خوبی هم داد.
اصلا انگار بشره. توقعمو خیلی برده بالا. خیلی هم ریز بین و دقیقه. خیلی هم عمیق میفهمه.
آنتروپیک پس فردا مثل Horizon Zero Down و Forbidden West، ربات هاش زندگی انسان رو می گیرند و باید پناه ببریم به پناهگاه ها و ربات های Anthropic بشن موجودات اصلی زمین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/mohsentavoosiseo/684" target="_blank">📅 17:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-683">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔆
به خاطر شرایط جنگی، قیمت دوره از 12 میلیون تومن، به 4 میلیون تومن، کاهش پیدا کرد و این قیمت تا زمان ظهور دوباره امید به بهبود در دل مردم این سرزمین، این قیمت باقی می مونه.
❗️
هیچ وقت هیچ کمپین تخفیف و فروشی نداشتم. این هم کمپین نیست! کاهش دائمی هست تا برگشت…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/mohsentavoosiseo/683" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-682">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آموزش سئو محسن طاوسی
pinned «
🔆
به خاطر شرایط جنگی، قیمت دوره از 12 میلیون تومن، به 4 میلیون تومن، کاهش پیدا کرد و این قیمت تا زمان ظهور دوباره امید به بهبود در دل مردم این سرزمین، این قیمت باقی می مونه.
❗️
هیچ وقت هیچ کمپین تخفیف و فروشی نداشتم. این هم کمپین نیست! کاهش دائمی هست تا برگشت…
»</div>
<div class="tg-footer"><a href="https://t.me/mohsentavoosiseo/682" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-680">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تمام صحبت های من درباره هاست و سرور و دسترسی و Origin Rule و GEO DNS، پست های زیر هست. درباره sync بودن سرور داخل و خارج هم در لحظه نظری ندارم.
هاست های ایرانی که اخیرا میگن دسترسی گوگل بهشون باز هست(ولی از خارج یا باوی پی ان باز نمیشن)، دیگه چون فقط داخل هست، بحث sync نداره. با تست های من و بازخورد دیگران، بعضی از هاست ها اینطوری هستند و گوگل هم بهشون دسترسی داره(اما وریفای سرچ کنسول باید فقط با دی ان اس باشه).
چه هاستی؟ اسم نمیبرم. پس فردا بد میشه میفته گردن من.
این هم بگم که در تمام شرایط، اختلال وجود داره. الان اپ تایم 90 درصدی(به جای 99.9 درصدی) ایده آل هست.
راه دیگه ای برای هم sync بودن هم در دسترس بودن از داخل و خارج نمیشناسم.
البته که متخصصین devops روی سرور های اختصاصی با هزینه زیاد میتونن. یک سری پلاگین وردپرس هم برای sync دو دیتابیس هست. ولی من چیزی که خودم اجراش نکردم آموزش نمیدم.
تمام صحبت های من در این باره:
https://t.me/mohsentavoosiseo/620
https://t.me/mohsentavoosiseo/623
https://t.me/mohsentavoosiseo/624
https://t.me/mohsentavoosiseo/625
https://t.me/mohsentavoosiseo/628
https://t.me/mohsentavoosiseo/631
https://t.me/mohsentavoosiseo/633
https://t.me/mohsentavoosiseo/634
https://t.me/mohsentavoosiseo/639
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/mohsentavoosiseo/680" target="_blank">📅 18:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-679">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLuO82AEOuQmfuHPM-5ExnUFJ0acuIUVFJ6X6f-OAKjr_OsfVw7TC6IqyJsRG42yKS4YNu_c2OGiOFIyEoiT20uFR5x0A2ImRWFnV16y2Cxp-ymTZsiGhy4y1EhPjYs6dYns5VYLIwRI7p-6W6H7BRIJLCFbREUk34rc2DxkzqnlxapGonEc1uymvLhzNAGHYEfIwdPsmBsS5LEpDctq0P1FBJv3cHoV40hqiRh8pr7lBlxFCE0TyPWFgtHsXAfEP0wsk_UmKht8BdYmfK_xFHC0dfVm5gekiZ1mhLTExXxBy4Rw69VIkipOPkBDylL4ZkmZhAQJ75Qdxo5_w6umZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا خوشم نمیاد از این خسیس بازی بیش از حد کلاد. دوتا لینک کرد و خوند، یه دونه گوگل شیت دویست ردیفته و ده ستونه ساخت کلاد مکس(5x pro) شد 22 درصد!
البته با Sonnet کمتر مصرف میکرد قطعا. ولی حوصله خنگ بازیش رو نداشتم چون کار گوگل شیتش پیچیده بود. آدم هم مغزش از جا درمیومد با این تسک.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/mohsentavoosiseo/679" target="_blank">📅 14:32 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-678">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صحبت تلفط شد، خیلی ها خارج رو شامل چند تا دونه کشور خاص میدونن و ملاک ذهنیشون اینه: ایران و امریکا. ایران و کانادا. ایران و آلمان.
هرکس که مهاجرت کرده، ایران و کشوری که رفته رو راس میدونه تو ذهنش.
ولی بهتره ما جهانی فکر کنیم و کل کره زمین رو ببینیم. جهت خط خطی کردن ذهن هایی که ناخواسته محدود شدند، یاداور میشم:
خارج شامل هند، بنگلادش، نپال، سومالی، کنگو، هنگ کنگ، فیلیپین، میانمار، تانزانیا، گامبیا، بوسنی هرزگوین، مغولستان، لیتوانی، لیبی، مصر، غزه و رام الله و کرانه باختری، صربستان، مراکش، قرقیزستان، زامبیا، شیلی، بولیوی، گواتمالا و... هم هست و این ها هم خارج محسوب میشن و جمع کوچکی از سرزمین ها و کشور های غیر انگلیسی زبان هستند!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/mohsentavoosiseo/678" target="_blank">📅 11:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-677">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تلفظ Claude به انگلیسی با لهجه بریتانیایی و آمریکایی، کلاد هست. آ کوتاه. کلود نیست. حالا شاید با انگلیسی غیر اصیل مثل هندی و سنگاپوری و اماراتی یه جور دیگه بگن.
تلفظ Claude در بعضی زبان های اروپایی و اسپانیایی و کره ای میشه کلودی.
کشور های مختلف هم به مدل خودشون تلفظ میکنن.
تلفط Claude به فرانسوی میشه کلود. با صدای O. صدای اُ . بعد از d هم e گفته نمیشه. کلوده نیست. کلود. ریشه کلمه claude، فرانسوی هست. در نتیجه کلود هم درست هست.
مثل BMW که متولد آلمانه و آلمانی ها میگن بی ام وی. و آمریکایی ها میگن بی ام دبلیو. عملا اصلش بی ام و هست(نه دبلیو). پورشه هم درست تر و آلمانی تره. پورش رو انگلیسی ها میگن.
اما کلاد، فقط واژه اش ریشه فرانسوی داره. ولی شرکت Anthropic، که سازنده کلاد هست، یک شرکت آمریکاییه.
خلاصه: هم کلاد درسته هم کلود. آ و اُ . کوتاه.
نظر شخصی: برای اینکه با فضای ابری قاطی نکنیم، کلاد بهتره. چه برای مخاطب انگلیسی چه فارسی. تلفظ رسمی انگلیسیش هم کلاد هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/mohsentavoosiseo/677" target="_blank">📅 11:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-676">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZ8cRWEsDAR5WN4n0o28CIcaDmXkATbvzsbWaP1KE05CDMrnPHuIv8C1bpjqT364QiEwrq8C1__r1VfmfwxS5ZUIO93JjZyXVL4XGwjgSqPDVq0An5o18csyp2vQ2P6lS5HNwj6kioAAthKuLD3S8s6ECVw5b3BqzPhAnDPhwh4u9maBM9q0dO60cJvH58-SUPLSlJMexEWuATMKm7Yb0XCYlmoy0-FWjJqySCvpPvNhX3c98fCfl_b5a9VuzKGTUX_RSzd7XO7aIwNd5qAmLUMVRMa_z0IVa6XsdZcr4IGjhBVK3VVscHdhmA65clYcuWz5f5su-tuQ6Q3fUei_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همه خوبی از کلاد گفتم از بدیشم بگم. مثل chrome که اندازه اسب، رم می خوره، این هم خیلی مصرفش بالاست و گرونه.
کافیه یه کم تسکت متنی نباشه، نسخه Opus بسیار بسیار مصرف می کنه و البته بسیار هم باهوش تر از Sonnet هست.
این سشن ساعتی بشه 70 درصد برای کلاد مکس(5x pro) که ماهی 100 دلار پولشه واقعا زیاد هست.
کلاد پرو برای من اغلب کم میومد. کلاد مکس 5X اغلب زیاد میاد.
یک سری نکته برای بهینه سازی مصرفش از نظر زمانی هم تو
این ویس
گفتم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/mohsentavoosiseo/676" target="_blank">📅 16:16 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-675">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حالا من یه جوری از کلاد تعریف می کنم انگار اکانت کلاد میفروشم(اتفاقا پیام زیاد میاد برای خریدش).
درحالی که برعکس اکانت ChatGPT ارائه میدیم. چیزی که همش تو سرش میزنم
😅
ولی بهرحال اونم کاربرد خودش رو داره. من خود اکانت چت جی پی تی پلاس دارم اختصاصی رو اکانت خودم.
اکانت Cluade Max هم دارم که 5 برابر Claude Pro هست محدودیت هاش. ولی همه اعضای تیم ازش استفاده می کنیم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/mohsentavoosiseo/675" target="_blank">📅 15:51 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-674">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
اگر یکی از موارد زیر روی شما صدق میکنه، یعنی هنوز بسیار بسیار عقب هستید در دنیای هوش مصنوعی. راه حل چیه؟ برعکس موارد زیر رو انجام بدید و رویکردتون در تضاد با این ها باشه:
❗️
- تو سر هوش مصنوعی نمی زنید.
❗️
- از هوش مصنوعی ایراد نمی گیرید.
❗️
- تفکر نقاد بهش ندارید.
❗️
- به عنوان فکت چک به حرف هاش و بررسی هاش نگاه می کنید.
❗️
- حواستون به سوگیری هاش و مموری که با در چت با شما ایجاد میشه نیست.
❗️
- از حافظه و مموریش برای اینکه چیزی بهش یاد بدید استفاده نمی کنید.
❗️
- بهش فحش نمی دید یا تند حرف نمیزنید و سعی می کنید باهاش مودب باشید و احساس یه انسان باهاش دارید(جدی)
❗️
- در صحبت با شما گستاخ شده یا به شما تیکه میندازه.
❗️
- از بخش های مختلف و نسخه های مختلفشون مثل instant و thinking و deep research و agent و کانتکتور ها یا خوندن فایل و لینک استفاده نمی کنید.
❗️
- موقع پرامپت دادن برای تولید چیزی یا انجام کاری، بهش دیتا نمیدید یا دیتای کمی میدید و بعد از اینکه تولید کرد تازه یادتون میفته بهش مشخصات بیشتری بدید. مثلا برای تولید عکس، نه سایز میدید نه نسبت نه تم رنگی و واقعی بودن یا کارتونی بودن یا استفاده کردن یا نکردن از چیز خاصی و... . اما به محض تولید هر خروجی یادتون میفته که ااااا اینم باید بهش بگم. تصورتون اینه که مغز شما رو باید بخونه اون بدبخت.
@mohsenavoosiseo</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/mohsentavoosiseo/674" target="_blank">📅 15:48 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-673">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تفاوت کلاد و چت جی پی تی درباره اتفاقات 28 Feb 2026 یا 9 اسفند 1404.
چرا کلاد بی نظیره؟
یه گوگل شیت ساخت و دانلودش کردم. کپیش کردم. و تو یه لینک دیگه بهش دادم. گفتم بخون ببین چی میفهمی.
بهم گفت: این همون فایلیه که خودم برات ساختم!
✅
شما این کارو با Gemini و ChatGPT کنید میشینه توضیح میده. نمیگه این همون فایله.
✅
کلاد بهش گفته نشده هر سوالی رو حداقل تو انقدر حجم محتوا جواب بده. گاهی یه "نه" خالی میگه.
✅
کلاد علاقه ای به قانع کردنت نداره و سوگیریش به شدت پایین تره. سعی نمیکنه راضیت کنه الکی.
✅
از همه مهمتر، کلاد خیلی سریع تر میگه غلط کردم! این چت جی پی تی، یه موجود لفتیست دموکراتیه که کلا فکر میکنه هیچ اشتباهی نمیکنه و تاکید هم داره روش.
فاز اینم داره که نه فلان چیز شایعه هست. شما همین الان برو درباره اتفاقات 28 فوریه یا 9 اسفند ازش بپرس. متوجه میزان و درجه حماقتش میشی. وقتی جواب اشتباه داد بهش بگو برو سرچ کن. باز میره تو فاز اینکه نه شایعه است و... . و یه جوری تاکید میکنه و نقد میکنه که فکر میکنی حقیقت تو دست هاش هست.
بعد گیر میده که تو اشتباه میکنی. بهش میگی سرچ کن میگه نیازی به سرچ نیست!
حالا کلاد چی جواب میده؟
این سوال شما بر اساس فرضی است که نیاز به بررسی دارد. بگذارید جستجو کنم تا ببینم آخرین وضعیت چیست.
کلاد 100. چت جی پی تی صفر.
البته من دارم درباره Opus حرف میزنم. Sonnet بسیار خنگ تر هست ولی باز بهتر از نسخه 5.5 هست و گاها برابری میکنه.
بی انصافی نکنم، باگش تو 5.5 خیلی رفع شد. شما همین سوالی که گفتم رو برو بذار رو نسخه 5.4. کلا در حد ناندرتال ها خنگ میشه دوباره.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/mohsentavoosiseo/673" target="_blank">📅 15:36 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-660">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هزینه اینترنت ثابت فیبرنوری تو ترکیه 1100 لیر هست با سرعت اسمی 1Gb در ثانیه و سرعت واقعی 600Mb در ثانیه که دیگه Wifi 5G هم جواب نمیده این سرعت رو. و با کابل باید ازش گرفت که افت نکنه.
میشه ۷۰ مگابایت دانلود، ۴۰ مگابایت اپلود. در ثانیه. (هر ۸ بیت، ۱ بایت هست).
با وای فای 5G تا 300Mb میشه اگه نزدیک مودم باشید. با وای فای 2.4G تا حداکثر 100Mb.
یعنی با دلار ۱۸۷ هزار تومن میشه ۴ میلیون و ۵۰۰ هزار تومن.
بدون محدودیت حجم.
تو کافه ها بدبینانه(استارباکس، اسپرسولب) حدود 30 تا 70 Mb در ثانیه هست(حدود ۳ تا ۸ مگابایت در ثانیه). بدون محدودیت حجم.
هزینه کافه: رایگان. یک بار خرید که پسورد بگیرید فقط. بعدا تو هر شعبه ای استفاده کنید بدون سفارش. بدون خجالت. بدون احساس وظیفه برای سفارش دادن.
اینو گفتم که بگم انقدر ما تخریب کردیم بقیه کشورا رو حالا اینه وضعمون.
به خودمون گفتیم متمدن و باهوش و به بقیه گفتیم وحشی و عقب مونده و کم هوش و خنگ...انقدر که گفتیم هه هه ارمنستانم ادم شد واس ما؟ ترکیه که فلان. یونان که فلان. بابا ایتالیایی که خودشون دارن فرار میکنن. دلار دیگه به درد نمیخوره. دلار مرد. امارات بیابون بود برای ما ادم شدن. عمان؟ اون بیابون که هیچی نداره بابا. گرجستان شاخ شده بلیت برگشت میخواد از ایرانیا! ژاپنی ها که تا قبل بمب اتم وحشی بودن! چینی های حشره خور! عرب های سوسمار خور! اصلا همه جا ایران بوده. همش مال ما بوده.
عاشق توهم و چیز غیر نقدیم! هیچ کاری یا واقعیت موجود نداریم!
حله. فعلا کانفیگمونو بخریم
😏
...
ایران چراغ قرمز مخصوص عابر پیاده نداره. یه دونه به من نشون بده! یکی فقط!
چراغی که فقط برای عابر باشه ها! نه اینکه یه گروه ماشین چراغشون قرمز و گروه مقابل سبز بشه. چراغ مخصوص فقط عابر.
چون از نظر مهندسی عالی و از نظر کرامت انسانی بی نظیریم.
فرض کنیم موتوری هام تو چراغ قرمز رد نمیشن! (فرض محال کن).
ایران از این نظر، هم رده افعانستان و پاکستان و بنگلادش و ویتنام و هند و بخش هایی از عراق و کشورهای شمال آفریقاست.
تعصب یعنی نپدیزیم. خرد و عقل یعنی بپذیریم واقعیت رو که بتونیم تغییرش بدیم.
پی نوشت(بدیهی برای اکثر شما)؛
Mb یعنی مگابیت
MB یعنی مگابایت
واحد سرعت، بیت هست. چیزی که ما بهش عادت داریم و تو دانلود منیجر می بینیم، بایت هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/mohsentavoosiseo/660" target="_blank">📅 17:41 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-659">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کسانی که میگن چرا طرف رفت ارمنستان یا ترکیه؟ اونجا که ظرفیت نداره فضای دیجیتالشون. اونجا که اقتصادش فلانه!
باید بگم
قرار نیست برن شرکت ترک یا ارمنی کار کنند. ظرفیت اونجا مهم نیست! از دیجیتال مارکتر ها بعیده این حرف!
اونجا فقط یه نقل مکان سکونت فیزیکی هست که اینترنت داشته باشند و بتونن عین انسان با سیم کارتشون ثبت نام و verify کنند در سایت ها و ابزار ها و... .
ما انقدر خوشبختیم که کلا جز ارمنستان و ترکیه جایی نیست بتونیم بی دردسر سه ماه بریم و یا نسبتا ارزون و راحت اقامت بگیریم.
یک کم داره اندونزی و مالزی هم مد میشه برای دیجیتال نومد ها. ولی اون ها هم دورند هم سه ماهه نمیشه رفت هم پرواز پردردسری دارند.
بعضی ها که از اسپانیا و ایتالیا و یونان هم ایراد میگیرن! انگار قراره برن شرکت اسپانیایی ایتالیایی با حقوق های کم اونجا کار کنند.
چرا ذهن باید انقدر محدود فکر کنه که محل فیزیکی فعلی زندگی یعنی شغلت هم باید وابسته به همون بازار باشه؟ اصلا چرا اومدی تو حوزه دیجیتال اگه اینجوری فکر می کردی؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/mohsentavoosiseo/659" target="_blank">📅 11:19 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-658">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به زودی در شغل های در سراسر جهان و ایران:
استخدام متخصص فلان (گرافیست، مارکتر، تولید محتوا، توسعه دهنده و...)
ملزومات مهم (نه امتیاز!):
تسلط به کلاد
رسیدیم به این جمله که در آینده افراد شغل هاشونو از دست نمیدن. بلکه کسانی که بلد نیستند با AI کار کنند شغل هاشونو از دست میدن. (فعلا غیر از کارهای دستی مثل آشپزی و ماساژ و خیاطی و...)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/mohsentavoosiseo/658" target="_blank">📅 00:48 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-657">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">https://www.zhaket.com/web/speedix-plugin
این شما و این هم افزونه افزایش سرعت سایت وردپرسی در اینترنت ملی.
کسانی که سایت وردپرسی دارند(که اکثریت هستند)، می دونند درد کجاست.
این پلاگین درمان این درده.
✅
باعث کندی  با وی پی ان  یا از خارج از ایران یا زمانی که اینترنت بین الملل وصل هست یا اگه هاست خارج باشه، نمیشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/mohsentavoosiseo/657" target="_blank">📅 00:39 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-655">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۴
چیزی که بار سنگینی از دوش من برداشت
رها کردن چیزهایی که میخواستم حفظشون کنم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/mohsentavoosiseo/655" target="_blank">📅 17:20 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-654">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۳
مصاحبه بین المللی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/mohsentavoosiseo/654" target="_blank">📅 17:13 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۲
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/mohsentavoosiseo/653" target="_blank">📅 17:09 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/mohsentavoosiseo/652" target="_blank">📅 17:05 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پست بالا:
https://t.me/mohsentavoosiseo/649
درباره Opus بود. نه Sonnet یا Haiku
و من Opus در حالت Adaptive Thinking استفاده میکنم.
خود Opus مصرفش بیشتر هست. در حالت Adaptive Thinking باز هم بیشتر میشه مصرفش.
برای کارهای ساده در حد ترجمه و ویراستاری نقطه ویرگولی و...، اصلا نیاز به Claude نیست. مثل این میمونه که وسط آسفالت صاف، لندکروز ببری. سلطان رو سر چیزای بیخود بیدار نکنید.
تسک ساده هایی که خیلی هم ساده نیستند ولی پیچیده هم نیستند و فقط نیاز دارید خنگ بازی کمتری داشته باشه هوش مصنوعی، هم روی Sonnet. خیلی با Haiko  تجربه ندارم که بگم دربارش.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/mohsentavoosiseo/651" target="_blank">📅 14:02 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-650">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کاهش مصرف Session پنج ساعته و هفتگی کلاد.
مصرف دوبرابر کلاد در ساعت های Peek
چرا اشتراکی خیلی معنی نداره برای کلاد؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/mohsentavoosiseo/650" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-649">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چرا کلاد خداست؟ Claude خداست؟
بدی ChatGPT و Gemini و Grok چیه؟
۳ Anthropic فعلا
Google, OpenAI و
X.AI
صفر
سه هیچ به نفع انتروپیک(شرکت کلاد)
سطح این ویس مبتدی هست. بسیار مبتدی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/mohsentavoosiseo/649" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-648">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🏴
در جریان باشید
🏴
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/mohsentavoosiseo/648" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیامی از بچه ها:
خود ما از این روش اقدام کردیم و ۲ روز تقریبا سایتمون داون بود و هیچ پاسخی نمیدادن.
پیام دیگه ای از بچه ها:
من هاست خارجم نت افراز بود بکاپ داشتم ازش
هاست داخل هم از خود پارس پک گرفتم ریستور رو انجام دادند ولی سایت بالا نمیومد در نهایت تنظیمات رو خودمون انجام دادیم هم هاست هم cdn بعد اوکی شد الان هم خیلی خوبه هم سرعتش خوبه هم قطعی نداره
از داخل و خارج هم همزمان باز میشه
نظر من:
سایت Down میشه. برای من 24 ساعت down شد. ولی ارزید.
احتمالا پیام اول، مثل پیام دوم بوده مشکل فنیش ولی خودش از پس کار بر اومده.
جواب ندادن تیکت(بعد از فعال سازی) و... هم چیزی که بچه های پارس پک باید بررسی کنند که چرا چنین اتفاقی افتاده و چی بوده ماجرا.
من فیدبک رو میذارم اینجا. امیدوارم چه با روش من چه با روش خودتون، سایتتون رو در دسترس کنید و دیگه از وضعیت "در حالت انتظار" خارج بشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/mohsentavoosiseo/646" target="_blank">📅 15:25 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXzBZAgvj3JHRK7aKyF4MbVVGvDB__9hAA-4EcQfVoJeQSIEJJiFnkCzGkJGTmk4WOU5eoXob2MA56MnboQ8msBAzfdoifHMa1ftESigMY70x-cLn4YVwaenhaqFvLfuFxJKWZgTGo_m1eO_Hvh13mTgfUvS1vpRizBtxe5_01sGMvbSDqypfAMUhgLSRx4l4Lh4zsOEyuGmoMW_s_xAk3S3y1HePzPqlEO8p3DzWlfByOjA9nVPWvIDWpO9YOLFQ6NUOzoBh49o2CnRD3sY9ibqxkB9TSW-lGmxqXfRx6owqRRd6STAqmPP-3GWh22yFxNS6RvTfw-ONJcTJkWT_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و البته ادامه دادن، یعنی سرور اولی هم از خارج هم از داخل در دسترسه. آموزششم بالاتر گفتم رایگان:
https://t.me/mohsentavoosiseo/623
این که دوره نیست. این که دیگه پولی نیست! این که با این نقل و نبات شدن اینترنت بین الملل وسط قطعی، دیگه هزینه ای نداره عملا.
دلیلی که انجام نمیدی چیه؟ بیا با طناب محسن طاوسی برو تو چاه! چاه خوبیه! قبلشم رو سایت خودم و چندین سایت دیگه تست شده.
قدیمی ها میدونن من نسخه تئوری الکی، نه تایید می کنم نه نقض و انکار میکنم.
اون میزان کم جریان مالی و تراکنشی که برات یا برای کارفرمات میاره کافیه! همه چیزم صد درصد باز شه چیزی ضرر نکردی! وقتی بقیه بازارشون صفر مطلق خوابیده بود، تو یه سودی کردی.
از همه مهمتر! بعد روانی موضوع و امید به حرکت هست. بخوای مهاجرت کنی پول نمیخوای؟ نباید بگذره روزگارت؟ که بعدا بری؟ انجامش بده!
رایگان یادم دادم و واضح و قدم به قدم(
اینجا
).
هیچی مستقیم و غیر مستقیم تو جیب من نمیره.
هزینشم برای خودت در حد خرید هاست داخل و خارجه و پول اینترنت برای انتقال بکاپ!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/mohsentavoosiseo/644" target="_blank">📅 13:22 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">از اینترنت طبقاتی استرس نگیرید.
🔴
آبان ۹۸ بحث اینترنت ملی داغ بود و موتورجستجوی ملی. دو هفته هم قطع کامل بود.  خیلی ها ترسیدن و رها کردن. زمان مهسا هم همینطور.
🔴
الان که در وسط شرایط جنگ و برزخ رو به بدتر شدن هستیم، اینترنت وصله. وسط جنگ ۱۲ روزه حتی گوگل باز…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/mohsentavoosiseo/643" target="_blank">📅 22:43 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هوای هم رو داشته باشیم
✅️
چه قبلا قسط دادید چه قبلا اصلا پرداختی نداشتید، سعی می کنیم با شرایط فعلی شما در این شرایط ایران، بتونید تهیه کنید: @mohsentavoosisupport
✅
کسانی که قسط دوره داده بودند و مهلت تعیین کرده بودیم و قرار بود قیمتشون افزایش داشته باشه،…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/mohsentavoosiseo/642" target="_blank">📅 17:47 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-639">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">احتمال سوم:
قطع موندن اینترنت بین الملل و وصل شدن بعضی جاها بصورت لیست سفید و استثنا</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/mohsentavoosiseo/639" target="_blank">📅 15:29 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee89341378.mp4?token=udqlJy_-bWvYOxo9pVhtCwugGT39ylJ6oqbPbs7i8At3csf-oKaOp7v_4hYmngmhxl4IFrWdTeZbEfYn1Jp_YkNrp27IVaox53J4Zggg0dxlkQ5wXRA7pOxzu9JIleErHFAkHJuzF7YgvYetHk3xvKC12Fgzs7olOVJmacMmYvhNqeY23J5CtaZcheseQ1EIdGrs2lhY34HPlfFOs4MNo9jn4lankpcx007ZalHe1tVHt9EXr0CyvoaV9q9I1l2xOMwont-v9sFp000oCSOTitYrcxXnTMjL6mtoa1YldfSWXUeANRY12cfepV8J1fAwXjDEP5aYJveF96zbEIJlcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee89341378.mp4?token=udqlJy_-bWvYOxo9pVhtCwugGT39ylJ6oqbPbs7i8At3csf-oKaOp7v_4hYmngmhxl4IFrWdTeZbEfYn1Jp_YkNrp27IVaox53J4Zggg0dxlkQ5wXRA7pOxzu9JIleErHFAkHJuzF7YgvYetHk3xvKC12Fgzs7olOVJmacMmYvhNqeY23J5CtaZcheseQ1EIdGrs2lhY34HPlfFOs4MNo9jn4lankpcx007ZalHe1tVHt9EXr0CyvoaV9q9I1l2xOMwont-v9sFp000oCSOTitYrcxXnTMjL6mtoa1YldfSWXUeANRY12cfepV8J1fAwXjDEP5aYJveF96zbEIJlcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/mohsentavoosiseo/637" target="_blank">📅 22:07 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوستانی که نگران قطع موندن اینترنت هستند، این نظر شخصی من بدون قبول مسئولیت هست و من برنامه هام بر این اساس پیش میره همونطور که قبلا هم گفته بودم:  احتمال اول: وصل شدن دائمی اینترنت بین الملل بهتر از قبل یک بار برای همیشه بدون ترس مجدد از قطعی.   احتمال دوم:…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/mohsentavoosiseo/636" target="_blank">📅 20:49 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قبل از اینکه حرف اصلی رو بزنم این رو بگم که دوره از داخل ایران در دسترس هست.
✅
اما در این شرایط چیکار کنیم و خودم چیکار میکنم؟
✅
برای کسانی که ایران هستند: تولید محتوای فارسی و کمپین های رپورتاژ و محتوای داخلی وب سایت و استخراج عنوان ها با ابزار های داخلی…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/mohsentavoosiseo/635" target="_blank">📅 19:50 · 26 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-634">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خیلی ها نمیدونن میرور چیه کلون چیه.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/mohsentavoosiseo/634" target="_blank">📅 14:39 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-633">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟
mohsentavoosi.com</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/mohsentavoosiseo/633" target="_blank">📅 14:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">روش راحت بالا اومدن سایت از داخل و خارج! بدون پیچوندن بدون GEO DNS!
امیدوارم هیچ وقت به چنین چیزی دیگه نیاز پیدا نکنیم.
آرزو میکنم به محض اینکه اینکارو کردید پشیمون شید بخاطر وصل شدن ابدی اینترنت بین الملل. آرزو میکنم زحمتتون هدر بره! می ارزه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/mohsentavoosiseo/631" target="_blank">📅 14:21 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فاز امید الکی دادن ندارم. صحبت من فنی هست. انتخاب های متعددی پیش رو داریم. ولی من همیشه دست و پا زدن و یه کاری کردن رو ترجیح میدم به هیچ کاری نکردن. هیچ کاری نکردن و تماشاچی بودن و منتظر بودن من رو از پا میندازه. ته چاه باشم ترجیح میدم دیوار چاه رو بکنم تا بشینم منتظر باشم بالا رو نگاه کنم.
دست و پا برای بقا همیشه مثل فیلم Pianist  نیست. یکیشم مثل وضعیت الان ماست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/mohsentavoosiseo/630" target="_blank">📅 11:36 · 22 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
اما در این شرایط چیکار کنیم و خودم چیکار میکنم؟
✅
برای کسانی که ایران هستند:
تولید محتوای فارسی و کمپین های رپورتاژ و محتوای داخلی وب سایت و استخراج عنوان ها با ابزار های داخلی کاریه که میشه انجام داد و شما رو جلو میندازه. ماه های بعدی دیگه این مراحل رو تکرار نکنید. برای سه ماه بعد اصلا جلو جلو انجام بدید.
اگر هم سرور داخل هست، بهینه سازی داخلی هم میتونید انجام بدید.
✅
برای کسانی که خارج از ایران هستند:
دوباره باز تولید محتوای داخلی، استراتژی و عناوین محتوای داخلی و آف پیج! به کلی ابزار هم که راحت دسترسی دارید! بهتر نیست از رقبایی که فقط درگیر خوندن اخبار هستند جلو بیفتید؟</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/mohsentavoosiseo/629" target="_blank">📅 11:36 · 22 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">برای پارس پک origin rule هست روی سرویس CDN. و GEO DNS نیست! به گفته خودشون دقت origin rule بسیار بالاتره و ارزون تر هم هست کلا:
https://parspack.com/cdn</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/mohsentavoosiseo/628" target="_blank">📅 18:18 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">درباره یک سری ابزار های جستجوی داخلی از اونجا که دوست ندارم این وضعیت رو دائمی ببینم و عادت بشه و تبلیغ کنم، اسم نمیبرم.
ولی اون ها ترکیبی از گوگل و بینگ هستند به علاوه یک سری شخصی سازی ها و اسلامیزه شده.
شرط اول اینه که هم از داخل هم از خارج بالا بیاد سایتتون که تو پست های قبلی توضیح دادم.
چون اینا خودشون از بینگ و گوگل دیتا میگیرن، گوگل سایت شما رو نبینه اینا هم نمیبینن.
اگرم گوگل ببینه و کاربر داخل باز نکنه سایتتون باز نمیشه و بازم فایده نداره.
بقیش همون سئویی هست که بلدید ولی یک کم سنتی تر. مثلا اگزکت مچ بک لینک با عین کیورد مهم تر هست برای بینگ. و بینگ هنوز به متاکیوردز کار داره.
آموزش سئو بینگ و چت جی پی تی ChatGPT
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/mohsentavoosiseo/627" target="_blank">📅 17:15 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پست های بالا ویرایش شد. دوباره ببینید. تو اپ های داخلی هم برای کسانی که اینترنت ندارند بفرستید شاید مفید باشه براشون.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/mohsentavoosiseo/626" target="_blank">📅 17:09 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-625">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این متن هم محمدرضا زراعتی از بچه های پارس پک و دوست شفیقم برام فرستاد. با شما به اشتراک میذارم. درباره SSL هاست های داخل:
راستی محسن جان الان سایتهایی که داخل ایرانن به خاطر همین قطعی ها مشکل خطای ssl میگیرن چون احراز هویت دامنه پیش‌فرض از روش HTTP هندل میشه برای همین ریکوئست های از صادر کننده سرتیفیکیت نمیرسه به ایران
راهش اینه که اعتبارسنجی ssl رو از روش DNS انجام بدن دیگه مشکل حل میشه.
تو این اموزش یاد دادم چطوری با CDN پارس پک بتونن هندل کنن(برای ssl بر خلاف ارجین رول نیاز نیست دیگه ابر cdn روشن بشه فقط از رکوردهاش استفاده میکنن)
https://docs.parspack.com/ssl/free-ssl-issue-iran-access/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/mohsentavoosiseo/625" target="_blank">📅 17:00 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-624">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟  mohsentavoosi.com
1️⃣
اول انتقال بکاپ. که بسیار سخت بود. انتقال بکاپ 10 گیگی از خارج به داخل سخت بود از نظر قطع شدن و سرعت(الان راحت تره خیلی).
2️⃣
دوم خرید هاست در دوطرف. هاست من از قبل آلمان بود.…</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/mohsentavoosiseo/624" target="_blank">📅 16:57 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-623">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟
mohsentavoosi.com
1️⃣
اول انتقال بکاپ. که بسیار سخت بود. انتقال بکاپ 10 گیگی از خارج به داخل سخت بود از نظر قطع شدن و سرعت(الان راحت تره خیلی).
2️⃣
دوم خرید هاست در دوطرف. هاست من از قبل آلمان بود. ایران هم گرفتم.
3️⃣
سوم پیدا کردن جایی که بتونه تقاضای داخل و خارج رو هندل کنه و کار GEO DNS یا سرویس مشابهی انجام بده (مثل قابلیت origin rule). که از اونجایی که از قبل من مشتری پارس پک بودم، این کار انجام شد.
برای پارس پک origin rule هست روی سرویس CDN. و GEO DNS نیست! به گفته خودشون دقت origin rule بسیار بالاتره و ارزون تر هم هست کلا:
https://parspack.com/cdn
پس قدم سوم شد خرید CDN با قابلیت GEO DNS یا Origin Rule (که پارس پک اورجین روله ووبهتره و ارزونم هست)
4️⃣
چهارم دامنه من از شرکتی خریده شده بود که داخل بود و امکان تغییر DNS نداشت. سر اینکه بتونم دی ان اس دامنه خودم رو عوض کنم هم کلی مکافات داشتم و تیکت زدن و... .
5️⃣
و در نهایت با تنظیمات توی پارس پک(تیکت) که واسط بین داخل و خارج بود کار انجام شد.
‼️
راستی میرور و sync نیست! یعنی هاست داخل من عوض شه خارج نمیشه. اگه فروشگاهی باشید سبد خرید و سفارش های هاست خارجتون با داخلتون هماهنگ نیست. من روش هماهنگ رو بلد نیستم. برای من جداست. اهمیتی هم برام نداره.
اگرم فروشگاه باشید اکه بتونید سفارش هایی که با وی پی ان و بی وی ان مدیریت کنید هم کار تمومه. اکثرا دسترسی از خارج رو برای گوگل میخوان و سینک بودن براشون مهم نیست. ملاک رو میتونید دیتای ایران در نظر بگیرید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/mohsentavoosiseo/623" target="_blank">📅 16:51 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-622">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از عادی سازی نکردن دی، رسیدیم به اینکه چطوری درامدمون رو در حد بقا حفظ کنیم تا به شرایط عادی یک بار برای همیشه برسیم...
ادامه موارد زیر جهت کمک هست. دست و دلم به پست و تولید محتوا نمیره. ولی میدونم با همین چند تا پست ممکنه کار چند نفر راه بیفته.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/mohsentavoosiseo/622" target="_blank">📅 16:47 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-620">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رسید مژده که ایّام غم نخواهد ماند
🔆
شماره در زمان اینترنت ملی در پیام رسان "بله" (متاسفانه):  جهت موارد دسترسی به دوره، خرید، قسط و...: 0919-268-19-56  سایت mohsentavoosi.com از داخل و خارج حالا باز میشه(اپدیت فروردین ۴۰۵)
🔆
🔆
🔆
رسید مژده که ایّام غم نخواهد…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/mohsentavoosiseo/620" target="_blank">📅 19:27 · 08 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-619">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بیشتر از آمادگی بابت قطعی های مقطعی اینترنت ایران و دسترسی از خارج،  در فکر آمادگی برای تغییر قوانینی هستم که در سود و زیان وب سایت ها موثره و بازی رو عوض میکنه. آیا خدمات و محصولات شما بعد از تغییرات بزرگ همچنان تقاضا یا سود داره‌؟  بر خلاف تصور عموم، به…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/mohsentavoosiseo/619" target="_blank">📅 17:27 · 18 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیشتر از آمادگی بابت قطعی های مقطعی اینترنت ایران و دسترسی از خارج،
در فکر آمادگی برای تغییر قوانینی هستم که در سود و زیان وب سایت ها موثره و بازی رو عوض میکنه. آیا خدمات و محصولات شما بعد از تغییرات بزرگ همچنان تقاضا یا سود داره‌؟
بر خلاف تصور عموم، به عقیده من کسب و کار های مهاجرتی، همچنان پررونق تر و راحت تر پیش خواهد رفت.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/mohsentavoosiseo/616" target="_blank">📅 19:33 · 03 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-613">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آموزش سئو محسن طاوسی
pinned «
هوای هم رو داشته باشیم
✅️
چه قبلا قسط دادید چه قبلا اصلا پرداختی نداشتید، سعی می کنیم با شرایط فعلی شما در این شرایط ایران، بتونید تهیه کنید: @mohsentavoosisupport
✅
کسانی که قسط دوره داده بودند و مهلت تعیین کرده بودیم و قرار بود قیمتشون افزایش داشته باشه،…
»</div>
<div class="tg-footer"><a href="https://t.me/mohsentavoosiseo/613" target="_blank">📅 12:19 · 24 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-611">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ما نهایت همکاری رو داریم می کنیم همه جوره که دسترسی همه با مبلغ کم راه بیفته تو اسپات پلیر</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/mohsentavoosiseo/611" target="_blank">📅 16:03 · 12 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-610">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این پیام رو به کسانی که اینترنت ندارند هم برسونید: الان که شرایط جنگیه و نمیدونیم یک هفته دوهفته ادامه داره یا یکی دوماه تا وصل شدن اینترنت، اگر قسطی دسترسی به دوره داشتید، با مبلغ خیلی کمتر میتونید دسترسی رو کامل کنید یا اگر ندارید جدید بخرید. هم به خاطر…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/mohsentavoosiseo/610" target="_blank">📅 17:18 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-609">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این پیام رو به کسانی که اینترنت ندارند هم برسونید: الان که شرایط جنگیه و نمیدونیم یک هفته دوهفته ادامه داره یا یکی دوماه تا وصل شدن اینترنت، اگر قسطی دسترسی به دوره داشتید، با مبلغ خیلی کمتر میتونید دسترسی رو کامل کنید یا اگر ندارید جدید بخرید. هم به خاطر…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/mohsentavoosiseo/609" target="_blank">📅 22:26 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-608">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اگر سرورتون داخل ایران هست، الان از ایندکس خارج شده صفحاتش.  اگر سرورتون خارج از ایران هست، مشکل گوگلی و ایندکسی نداره ولی کاربر داخل ایران بهش دسترسی نداره.  راه حل؟ هیچ راه حلی نداره. راه حل اینه که کلا اینترنت بین المللی قطع نشه. اگر هاست داخل و سی دی ان…</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/mohsentavoosiseo/608" target="_blank">📅 19:19 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-607">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگر سرورتون داخل ایران هست، الان از ایندکس خارج شده صفحاتش.
اگر سرورتون خارج از ایران هست، مشکل گوگلی و ایندکسی نداره ولی کاربر داخل ایران بهش دسترسی نداره.
راه حل؟ هیچ راه حلی نداره. راه حل اینه که کلا اینترنت بین المللی قطع نشه. اگر هاست داخل و سی دی ان خارج کار کنه، باز اینترنت بین الملل یک کم بازه. چیزی که میگم در شرایطی هست که اینترنت بین الملل قطعه.
حتی دی ان اس هم در زمان قطعی اینترنت نمیتونید عوض کنید. چون دی ان اس هم با اینترنت بین المللی هست. ممکنه آی آر ها رو بتونید روی هاست داخلی. که در این صورت گوگل نمیبینه. کاربر میبینه.
در نتیجه، الان یکی از حالت های زیر اتفاق میفته برای همه سایت های با مخاطب ایرانی:
1- از ایندکس خارج شدن و حذف شدن از گوگل (هاست داخلی ها)
2- کاهش رتبه و عدم دریافت ترافیک از کاربر(هاست خارج ها)
امیدوارم یک بار برای همیشه این مشکلات ما تموم بشه و ما مردم ایران، بعد از چند دهه، نفس راحت بکشیم و طعم آزادی و امید و تکاپو و رونق و رشد رو بچشیم و دیگه کف خیابون کشته ندیم
🖤
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/mohsentavoosiseo/607" target="_blank">📅 20:45 · 30 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-606">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🟢
ساده لوحی در SEO
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/mohsentavoosiseo/606" target="_blank">📅 21:24 · 06 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-605">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔍
این به روزرسانی سومین تغییر هسته ای گسترده در سال 2025 است و مانند نسخه های قبلی، هدف آن ارتقای کیفیت و ارتباط محتوا برای کاربران در سراسر جهان است.
🔍
این به روزرسانی صرفا روی یک بخش خاص تمرکز نمیکند؛ با بازتعریف معیارهای رتبه بندی، توانایی گوگل در ارزیابی محتواهای مرتبط، مفید و رضایت بخش را افزایش میدهد.
🔍
گوگل بار دیگر نشان میدهد که ارزش واقعی در محتواهای با کیفیت و تخصصی است، به ویژه در زمینه هایی مثل پزشکی و سلامت که E-E-A-T (تجربه، تخصص، اقتدار و اعتبار) نقشی حیاتی در رتبه بندی دارند.</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/mohsentavoosiseo/605" target="_blank">📅 16:49 · 04 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-604">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/mohsentavoosiseo/604" target="_blank">📅 11:48 · 04 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-603">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW0SQnfzS6lW0dZeVBU5eF_jqnWSVhj48IQGNN14DwMqXBuN7WqzsLa9L69nOgBgn-yseEM-Vf42iuLgO90du3FRcNlbc4rG4gNf5ODE5g2ebTtXke_LyCnxq0OHP7LVi-9sVKKvuSzJv4Z3bxRWarVoqm4aSE6gpbgl7QC6BLTAP8R0xknth8L5wO6WN0QbQ1GNPCiD1ZrAS6QFScTzBCkhWoHBX2ebHQ_XkvGR5qUJHB8OLq19ikCJ6Qi0ARII5k9nSJSSED2RBxNN6mgdV24KNfNM1tBg06cfNKlenGBqdk-nKbWP-ZigsifrCawAskUak_3S9SNAgGHcssPaTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تو ویس های بالا توضیح دادم
✅
اینم سایت های من که تو اپدیت ها تکون نمیخوره. همیشه همینه. آخرین چیزی که من بهش توجه می کنم آپدیت های گوگله! چون مسیر من ثابته همیشه. به صورت کلی در دراز مدت رو به رشد بر اثر فعالیت های من و با توجه به رقابت موجود.
📎
اسکرین شات سرچ کنسول. شماره 3
💵
درامد این سایت: ماهانه + 40 م.ت خالص
⁉️
تو ذهنت اینه که سایتی که روزی بیست سی تا ورودی گوگل داره درامدش ماهی 40 تومن
نمیشه؟ آره با آموزش های غلط و بی بازده سئو و تحقیق کلمات کلیدی اشتباه و صفحه بندی و تارگتینگ اشتباه، کاملا حق با توست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/mohsentavoosiseo/603" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-602">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4IwCjHVrjfGPb7YbeLCAxTMzY0q5_T2VZCrhzH5mLz_uRRbLQhq8IDGsiBNnkgt8clCC6COeZsi--1f81CLGLzdhcTvkgNBrsNwiXhQU_O573WWu-t4YMkcSmh_A8aq4jS5KyYRbZoaLdB_tdmuzssswdRPgExmMFOcm4Qe8Ki-qP-A9CAm_J-wSAoFHhCNlzSUznuEBUS-gnBeFcP70jbF210Qzl0qyKP9D5vQ6TzlUjyjty7kawh3hG5wmFK52rtyFzRh8XAXV0dXcYwx8LGl53CFB6HJizgoX0ULo--e7_jgW4n43QhpZOZqhTm_sjqsQO6etT3l4AfR85gxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تو ویس های بالا توضیح دادم
✅
اینم سایت های من که تو اپدیت ها تکون نمیخوره. همیشه همینه. آخرین چیزی که من بهش توجه می کنم آپدیت های گوگله! چون مسیر من ثابته همیشه. به صورت کلی در دراز مدت رو به رشد بر اثر فعالیت های من و با توجه به رقابت موجود.
📎
اسکرین شات سرچ کنسول. شماره 2
💵
درامد این سایت: بالای معادل 200 م.ت. به صورت دلاری. غیر فارسی. مال من نیست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/mohsentavoosiseo/602" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-601">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuPwMyj--MTULF-7uANG-k81STsMjOx7L6j5ic8mrVxmCd3J1pIaqG5-gpwbOv4B4lXycsPq07gLbobesW1PUFh5n34GWDSPVNmsbe_xy0ogAs7-aklFA4kgX0S9t6yrGRGC_oCoexJycRQVvXEMrD5O7Ghyze_pMUy5Bogi1VBQllsSNFA9bv4a1T60tH5ws-B_XIbqwEW_JkWIv4ehFG4IhunyqfNrDVh_N21DHifvyJZ8KMJP4ofdTfWWvtTh2OnwrnWZ5cVCAoehgInma79yAGoMLtufHYXVkDeMaIFrEApaMAfbFNHsQ-lx-U4g3DPYDmK-AziT2Rjecz8jiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تو ویس های بالا توضیح دادم
✅
اینم سایت های من که تو اپدیت ها تکون نمیخوره. همیشه همینه. آخرین چیزی که من بهش توجه می کنم آپدیت های گوگله! چون مسیر من ثابته همیشه. به صورت کلی در دراز مدت رو به رشد بر اثر فعالیت های من و با توجه به رقابت موجود.
📎
اسکرین شات سرچ کنسول. شماره 1
💵
درامد این سایت: ماهانه + 300 م.ت خالص
⁉️
نرخ تبدیلش بالاست؟ درسته. این برمیگرده به استراتژی تحقیق کلمات کلیدی شما.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/mohsentavoosiseo/601" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-600">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کلا این صورت مساله که وای الان چیکار کنم گوگل آپدیت کرد، از دیرباز صورت مساله غلطی بود، صورت مساله غلطی هست و صورت مساله غلطی خواهد بود.
تمام پست های انگلیسی سایت های دیگه خیلی از زبان های دیگه هم از اون ها کپی و ترجمه میکنن و درباره راه کارهای افت بعد از اپدیت هست، کلیشه چرت و پرتی بیش نیست!
مثلا میگن تکنیکالتو چک کن! بک لینک های غیر طبیعیتو حذف کن! عنوان ها تو بازبینی کن!
ولی این محتوای بلغور چرت متقاضی داره بهرحال. ترافیک میاره برای اون سایت ها. می طلبه که بنویسن. چهار نفر هم بیان بگن ممنون از پست مفیدتون! اما نفهمن خب آخرش چیکار باید کنن! فقط ذهنشون مبهم تر میشه.
https://www.linkedin.com/posts/mohsentavoosi_aebaeoaew-activity-7409525124615348224-5vg8
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/mohsentavoosiseo/600" target="_blank">📅 13:19 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تو آپدیت گوگل چیکار کنیم؟
قسمت دوم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/mohsentavoosiseo/599" target="_blank">📅 12:44 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-598">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تو آپدیت گوگل چیکار کنیم؟ چرا افت کردیم؟ راه حل چیه؟ کجا رو بخونیم بفهمیم چه تغییری بدیم؟
قسمت اول
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/mohsentavoosiseo/598" target="_blank">📅 12:44 · 03 Dey 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
