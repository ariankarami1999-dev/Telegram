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
<img src="https://cdn4.telesco.pe/file/mon6z4Tw1Kd2xTiRtlkn-koiRDrd2enpKo9z3vIgfA6tG1DO8RBmXIt31rCqrzay6LFx--5u6khrx-R3FzOSDAIIKR66IO6fxKiqYmeR9iiRCYwRrZCOD6M56IU2y7oEocTVYlLtnVR_Xv3hOrQsACHAY9wOzkMS0c3gvQYsI5xEaQwFsm1u3eUpJ5oD0XCOenal3OfC66fpxIx4AvbHRptAB6i8uPDc8SB4iY1W9lwIDEhi4BUji-FGQvm70VeWyylVQY-Qz_gNNRPbORApaGuFoTn0GE0e5x17JwwcqKslpG96Kd9aoihY--cST40_63eQb5wiKvX6NoBfUwMPyw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 440K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-21615">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBynbyirFY1AoG73xLL927CsKHfp_YpEtASuLIdPfbGmChnyY4BEYolCPXkuzPTe2s4IQC9jlBGkfAuEUbXFhb9mzKxYRWHVLYDGhKg_fcwQHWB4ETqMQBi9aj7kMH8gUDIz8KryP_t_RfZoE23ooaCkkWP7wehgKJ-izxS4W4XEoucgSLwMr8lVLlDGwVMdARUOyhYm_tpWIp4MTqMw9Wu-yctYe4j84a_XApqHyw7g4fmItgI_By18m1Bmq4hG_IbHRXgoP7nhShY0OhZPX2XK_1CsoOB47Mzoj4dT-yiQ_JCprm3pnbC-wLUo3hp4Qo1f9Ltiq3V3D9sDRE_wVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ سوخترسان آمریکایی و ۲ پهپاد در خلیج فارس در حال مأموریت هستند ، بعد از مدتها این حجم مشاهده میشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/21615" target="_blank">📅 00:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21614">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6860a3c4.mp4?token=OPzw2Z6mzmtGotxljioGPvA3jWhRHTUDSzWRwVdk9ZM3pVg86yED2T7qxEKKVPuTAMZGdeGYpAIHh2zLxCrOK-rgvWOqptiDb-hpi_Hjt0uYdPYs-hmsEOQa_N-ZGEyo_Byfo9NINqhoTmm_393yHdyqXlKmMPwGRMgUoC1Q_U4uSWCMk38SNny_JHrg2tRDWCbHpBxeaIPpXUlLwzDBJH9n0NH6DLyHr3E9YpF_84nmdnjVe4Rhc4MPr8ELF1t2rTHsGsai4P1ehRhBUpFo6IyvKDFoc63UXydPljHprK2qUiKZFVk5UnWdQiVfK7Db0TZAG3d8mwmNaMEIqksZlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6860a3c4.mp4?token=OPzw2Z6mzmtGotxljioGPvA3jWhRHTUDSzWRwVdk9ZM3pVg86yED2T7qxEKKVPuTAMZGdeGYpAIHh2zLxCrOK-rgvWOqptiDb-hpi_Hjt0uYdPYs-hmsEOQa_N-ZGEyo_Byfo9NINqhoTmm_393yHdyqXlKmMPwGRMgUoC1Q_U4uSWCMk38SNny_JHrg2tRDWCbHpBxeaIPpXUlLwzDBJH9n0NH6DLyHr3E9YpF_84nmdnjVe4Rhc4MPr8ELF1t2rTHsGsai4P1ehRhBUpFo6IyvKDFoc63UXydPljHprK2qUiKZFVk5UnWdQiVfK7Db0TZAG3d8mwmNaMEIqksZlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : هر کسی میخواد برقش قطع نشه میتونه از بورس برق با قیمت آزاد خریداری کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/21614" target="_blank">📅 23:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21613">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">محسن کج بند رضایی، دبیر شورای امنیت ملی، ادعای وجود توطئه ایران برای ترور پسر دونالد ترامپ را «دروغی بزرگ» دانست و گفت این ادعا ساخته بنیامین نتانیاهو برای فریب و ترساندن رئیس‌جمهور آمریکا است. او مدعی شد نتانیاهو با انتشار گزارش‌های جعلی درباره «توطئه ترور ترامپ» او را ترسانده و بر تصمیم‌گیری‌هایش اثر گذاشته است. رضایی افزود: «اگر تصمیمی بگیریم، هیچ‌چیز مانع اجرای آن نخواهد شد؛ اما این گزارش‌ها صرفاً یاوه‌گویی‌های نتانیاهو هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/21613" target="_blank">📅 23:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21612">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دیوید بارنیا، رئیس پیشین سازمان اطلاعات خارجی اسرائیل «موساد»، می‌گوید جمهوری اسلامی در نهایت در اثر ترکیبی از فشارهای اقتصادی، عملیات علیه حکومت، و اعتراضات مردم ایران سقوط خواهد کرد، و تحریم‌ها به تنهایی برای رسیدن به این هدف کافی نیستند.
@WarRoom
🚨
🚨
🚨
حتما چنل رو دنبال کرده
🤣
🙌🏾</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/21612" target="_blank">📅 22:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21610">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش پرتاب موشک زد کشتی از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/21610" target="_blank">📅 21:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21609">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داده است که دونالد ترامپ با بازگشت به چارچوب اولیه توافق ژوئن با ایران مخالفت کرده و ترجیح می‌دهد با تشدید فشار اقتصادی و تحریم‌ها، تهران را به دادن امتیاز وادار کند. در مقابل، ایران تأکید دارد که بازگشایی تنگه هرمز باید بر اساس همان چارچوب ژوئن انجام شود؛ چارچوبی که شامل کاهش تحریم‌ها و محدود شدن فشارهای آمریکا بود. پاکستان، عمان و قطر نیز برای میانجیگری و نزدیک کردن دو طرف تلاش کرده‌اند، اما مذاکرات تاکنون پیشرفت چندانی نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/21609" target="_blank">📅 21:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21608">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ به شوخی می‌گوید:
ما یک خلیج(مکزیک که شد آمریکا) داریم. ما یک دریاچه(انتاریو که شد آمریکا) داریم. حالا چیزی که نیاز داریم یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا اقیانوس آرام را تغییر دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/21608" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21607">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرنگار: با کدام رهبران در مورد قطع روابط با ایران صحبت کرده‌اید؟
ترامپ: چیز زیادی برای صحبت وجود ندارد. ما نمی‌خواهیم با آنها صحبت کنیم. تنگه هرمز باز است.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/21607" target="_blank">📅 21:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21606">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: ایران در وضعیت بسیار دشواری قرار دارد و نمی‌تواند حقوق سربازان خود را پرداخت کند.
اقداماتی که ما در مورد ایران انجام می‌دهیم، به این معنا نیست که ما از گزینه نظامی چشم‌پوشی کرده‌ایم.
ما نمی‌خواهیم با ایران صحبت کنیم و قصد نداریم جلسه‌ای با آن برگزار کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/21606" target="_blank">📅 21:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21605">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شرکت روکِتسان ترکیه موشک کروز «چاکیر» را با موفقیت از یک پرتابگر زمینی آزمایش کرد
. این آزمایش نشان داد چاکیر علاوه بر پهپاد و دیگر سکوها، قابلیت شلیک از خودروهای زمینی را نیز دارد و می‌تواند اهداف زمینی و دریایی را با جستجوگر تصویربرداری مادون‌قرمز هدف قرار دهد. برد این موشک بیش از ۱۵۰ کیلومتر اعلام شده است.
جنرال یاشار گولر، وزیر دفاع ملی ترکیه،
نیز درباره تسلیحات جدید روکِتسان گفته است: «ما این سلاح‌ها را عمدتاً برای بازدارندگی می‌خواهیم، اما اگر استفاده از آنها لازم باشد، ترکیه بدون تردید از آنها استفاده خواهد کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/21605" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21604">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ: هیچ نگرانی‌ای از حمله روسیه به ناتو ندارم
دونالد ترامپ در گفت‌وگو با آکسیوس گفت که «اصلاً نگران» حمله احتمالی روسیه به کشورهای عضو ناتو نیست و تأکید کرد: «هیچ مشکلی وجود ندارد.» او همچنین گزارش‌ها درباره سفر محرمانه جان رتکلیف، رئیس سیا، به مسکو برای هشدار به روسیه درباره حمله به اعضای ناتو را رد کرد و گفت این سفر «یک کار معمول» بوده و «هیچ پیامی در کار نبوده و هیچ چیز غیرعادی‌ای» رخ نداده است. با این حال، گزارش‌هایی از جمله گزارش وال‌استریت ژورنال و CBS مدعی‌اند که رتکلیف در مسکو به روسیه درباره حمله به ناتو هشدار داده است؛ موضوعی که تاکنون از سوی مقام‌های آمریکایی یا روسی به‌طور رسمی تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/21604" target="_blank">📅 20:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21603">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس سابق موساد اسرائیل:
اجتناب از یک جنگ دیگر با ایران غیرممکن است
@WarRoom</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/21603" target="_blank">📅 20:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21602">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏ انفجار در اربیل عراق , منابع عراقی از حملات پهپادی به گروه های کورد در منطقه سوران در اربیل خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/21602" target="_blank">📅 20:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21601">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob8_svB0pyG-THsAB-TV6TnBwBwC8KOmCpOU80O9ZSDsic03vI2eo7SBoje40cmazUEZCPkOkvF1Oeg1slbDEX8q8RIA6jIEm9GO-W8ufFxdckDkLcWX2c3gKIw1FDYhS0bmfnLjw9NFCE_fcpHVe6DzroP4vFk8i5TKAN7nKup15eniuaIRyr85j6wcPkyBUYmfTFMnb1Vda14_RZMi0OYqm3UGZ3zz7NdcHN4Gu_8es-z4KV2MO1Ou7erFgWmzg8t_G846KFAcWMGaskJgOWIWotVYQJyS6kX8_VBY4f3TVApY5Bo0TyTs6-RygZ_SJ0rtLPApHICpbmIgu0S1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امبر اولر، ۴۱ ساله و دختر شایسته میشیگان، امشب در مسابقه میس آمریکا ۲۰۲۶ در میامی روی صحنه می‌رود. اما تنها پنج سال پیش حدود ۱۳۶ کیلوگرم وزن داشت و پزشکش به او هشدار داده بود که در مسیر یک «مرگ زودهنگام» قرار دارد. پس از این هشدار و تجربه‌ای تحقیرآمیز در یک پارک ترامپولین، تصمیم گرفت زندگی‌اش را تغییر دهد. او طی بیش از سه سال با رژیم غذایی و ورزش حدود ۱۷۰ پوند، معادل ۷۷ کیلوگرم، وزن کم کرد و در سال ۲۰۲۴ وارد دنیای مسابقات زیبایی شد. اولر که مادر سه فرزند است، امسال به‌عنوان میس میشیگان آمریکا انتخاب شد و اکنون در میان ۵۱ شرکت‌کننده میس آمریکا ۲۰۲۶ قرار دارد؛ و در ۴۱ سالگی مسن‌ترین شرکت‌کننده این دوره است.
@WarRoom</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/21601" target="_blank">📅 19:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21600">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مقام آمریکایی به فاکس نیوز:
توافق ایران و عمان برای ما اهمیتی ندارد؛ فشار اقتصادی را ادامه خواهیم داد و مذاکره‌ای با ایران نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/21600" target="_blank">📅 19:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21599">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزیر انرژی آمریکا: به ایرانی‌ها گفتیم می‌توانند با همکاری با ما، فقط برای تولید برق انرژی هسته‌ای داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/21599" target="_blank">📅 18:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21598">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش اسرائیل: دیروز، یک فرمانده از شاخه نظامی حماس را در حمله به منطقه خان یونس به هلاکت رساندیم.
همکنون نیز ارتش اسرائیل در حال حملات هوایی به جنوب لبنان می باشد
@WarRoom</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/21598" target="_blank">📅 18:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21597">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxBsTMkpjAjbS2ayD5R_9bMdRUlYwpGFS4xv5Wq1Qass4iPaOPAcrOdQ6uie2v5yha_wnJKNrLahLtEkh5EmCdQOtvT3G3i_N9FcF_lMZwDtKjhibv1Cm27aJUqeGvP0tdbiK7JltSuarcjKiAUYb1djWhoaU2W_kHwtBDBrl69Mm_qPHtQUsWLJJceVesZnr4UtYiR7Mxlxu9ZnC3S5UC3koHrFcR2oo2RsQzi8ILn_E09xeQq2GYbkyR8WHp7chfDKai3horACVfnxab0e-SvmjfeetrnL1wZWUtlnsvPVUhXyciZMdS48CKTQXok_b0CDti_FRZBwR6gdvnmxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای جنگ الکترونیک E/A 18G نیروی دریایی ایالات متحده در حالی که ایالات متحده همچنان به اعمال محاصره علیه ایران ادامه می‌دهد، بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند. تا ۲۷ آگوست، نیروهای سنتکام ۷۵ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/21597" target="_blank">📅 18:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21596">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21fec76a7.mp4?token=c5OaOfmqYjVE4HNukE4urUA1Ca3xRCI1cbgxHrihaZrJjFG-lS6PTWRlNlnvok2F0y8cXzjsrN0o3zJfHH4IlkKr17rvh1duwmtRyOwbnGMpEL2tyUILlnXQZNuJBAPN1Va3SKrWLYy20HazajoN3ktJMvOOlehW5LEKPIOCeONf6m2EEEICW5pj5GGHr7U0ZNsYWXnyyq-51nS0bceJwmQXTkzOeyYk-DmIVfSBgjOfop9QWlLNYdkHc4ELmHQMx8knZjUzDo5UvEEzErOK7uvT4fn0FTbZwAo6q9wnvl28TJZ61BnWwDTLwYvVpSTleD0PqhOoj9sbH2gnV7RCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21fec76a7.mp4?token=c5OaOfmqYjVE4HNukE4urUA1Ca3xRCI1cbgxHrihaZrJjFG-lS6PTWRlNlnvok2F0y8cXzjsrN0o3zJfHH4IlkKr17rvh1duwmtRyOwbnGMpEL2tyUILlnXQZNuJBAPN1Va3SKrWLYy20HazajoN3ktJMvOOlehW5LEKPIOCeONf6m2EEEICW5pj5GGHr7U0ZNsYWXnyyq-51nS0bceJwmQXTkzOeyYk-DmIVfSBgjOfop9QWlLNYdkHc4ELmHQMx8knZjUzDo5UvEEzErOK7uvT4fn0FTbZwAo6q9wnvl28TJZ61BnWwDTLwYvVpSTleD0PqhOoj9sbH2gnV7RCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو در ویدئویی از پیش ضبط شده مدعی شد که هنگام پخش این ویدیو او در ایران یا در پرواز ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/21596" target="_blank">📅 17:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21595">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏یسرائیل کاتس، وزیر دفاع اسرائیل، در جریان ارزیابی امنیتی با ارتش اعلام کرد: «مهلتی که تعیین کرده بودیم به پایان رسیده است. از این پس هرگونه پرتاب بالن یا بادبادک از غزه به سوی شهرک‌های جنوب اسرائیل با پاسخ سخت روبه‌رو خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/21595" target="_blank">📅 17:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21594">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">معاون وزیر نفت ایران: حدود ۴۰ درصد از ظرفیت آسیب‌دیده میدان گازی پارس جنوبی به تولید بازگشته است
@WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/21594" target="_blank">📅 16:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21593">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">@WarRoom
losing my religion</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/21593" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21592">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وال استریت ژورنال به نقل از منابع آگاه گزارش داد که هدف از سفر جان راتکلیف، رئیس سازمان سیا، به مسکو در روز سه‌شنبه، هشدار دادن به روسیه  بود که از حمله به ناتو و کمک به ایران خودداری کند. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/21592" target="_blank">📅 15:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21591">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b30ac12425.mp4?token=p1bXj-PLBYTrjn1KjBYFjIk6fq0rORaloLGRyIvM0o0l7kaCGvQDsOLpqqE8L8apxJxrkEiDWyuHIqOBrd5vhQza2Aq7Jm72hHcNPwBhjXPhHh0kts6gT0wEMowjKQbjApuBymXVsh370l6luOtkQmIrgf60OK57-D6-BHdPF3QYYJM7nZzmMRutshdfB30qrbDalOBHHmr9fJx9yKzsX2C-QXWZXp832eDSMZrP-9a7ozG4iOblJVSsfXcK24ypLovKGU8PuMKotlCFTHQeC7qYeM-164RhO_dFQbQjWEJEHzUhxEgJP10QvNjzOXNoHNRw5TSR4ctgBCJQU69M5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b30ac12425.mp4?token=p1bXj-PLBYTrjn1KjBYFjIk6fq0rORaloLGRyIvM0o0l7kaCGvQDsOLpqqE8L8apxJxrkEiDWyuHIqOBrd5vhQza2Aq7Jm72hHcNPwBhjXPhHh0kts6gT0wEMowjKQbjApuBymXVsh370l6luOtkQmIrgf60OK57-D6-BHdPF3QYYJM7nZzmMRutshdfB30qrbDalOBHHmr9fJx9yKzsX2C-QXWZXp832eDSMZrP-9a7ozG4iOblJVSsfXcK24ypLovKGU8PuMKotlCFTHQeC7qYeM-164RhO_dFQbQjWEJEHzUhxEgJP10QvNjzOXNoHNRw5TSR4ctgBCJQU69M5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/21591" target="_blank">📅 15:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21590">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شیخ محمد بن عبدالرحمن آل ثانی، نخست وزیر و وزیر امور خارجه قطر، امروز در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، دیدار و گفتگو کرد
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/21590" target="_blank">📅 15:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21589">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آتلانتیک : کاخ سفید به‌جای تشدید عملیات نظامی، به سمت تحریم‌ها و فشار اقتصادی بیشتر علیه ایران رفته تا هم فشار بر تهران حفظ شود و هم جنگ به موضوع اصلی انتخابات میان‌دوره‌ای تبدیل نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/21589" target="_blank">📅 14:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21588">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">روزنامه نیویورک‌تایمز گزارش داده است که عربستان سعودی در پی هفته‌ها حمله حوثی‌ها به اهداف سعودی، خود را برای احتمال آغاز دور تازه‌ای از جنگ در یمن آماده می‌کند. بر اساس این گزارش، حملات متقابل میان حوثی‌ها و نیروهای مورد حمایت عربستان شدت گرفته و خطر تبدیل‌شدن تنش‌ها به یک درگیری تمام‌عیار افزایش یافته است. ریاض در حال تقویت مواضع دفاعی و نیروهای یمنی متحد خود است و در صورت ادامه حملات، احتمال اقدام نظامی گسترده‌تر علیه حوثی‌ها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/21588" target="_blank">📅 14:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21587">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCSa7HmXMY94LQuke873js9IspIpWElId0aK53faDsQwTQ1ci2sBoLqjxyYqrxqWE6aio8LnTvGZIlUBQ9eQYwGNxjsDY5gBZcgvY1CKWc1wpr4SFWV0oJlrXM7hNtmCsuyMPEgPKvZZJpxApQzAlOjSk2pP5oxypVtPKyEfnuLvtBZz8wTGKm8HdV9Km26IcVr4CovtxFGeIbdcpg0qw4smRbSDtPn5DPwSGrL6qXjnJNTcZz149tzcCLf4l2prQ3G53XBMldZqZHG9jtpejyLBzliGowVGBkI7NPPDsoDMHDDg4Zo4Oi1v56p0H3g9goMUJPHvkd3DG4bW3pMvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون گزارش آتشسوزی بزرگ در پادگان سنندج
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21587" target="_blank">📅 12:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21586">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Bitcoin = 80,080$
🚀
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/21586" target="_blank">📅 12:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21585">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرنگار: آیا می‌توان گفت که در حال حاضر حملات نظامی علیه ایران متوقف شده‌اند؟  پیت هگست: نه. اگر لازم باشد از حملات نظامی استفاده کنیم، این کار را انجام خواهیم داد. اگر ایران آن‌قدر احمق باشد که زیاده‌روی کند یا با ارتش آمریکا درگیر شود، ما هر کاری را که لازم…</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/21585" target="_blank">📅 12:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21584">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به گزارش MS NOW، یک ملوان ۱۹ ساله نیروی دریایی آمریکا از خدمه ناو هواپیمابر «آبراهام لینکلن» در ۳ اوت ۲۰۲۶ به دریا پرید؛ همسر ۱۹ ساله‌اش هم این اقدام را تلاشی برای خودکشی عنوان کرده است.
او پس از حدود یک ساعت در آب نجات یافت و حدود پنج روز در مرکز پزشکی نیروی دریایی سن‌دیگو تحت مراقبت بود. همسرش می‌گوید او پس از تولد دخترشان در فوریه، چند بار درخواست
مرخصی پدری
کرده بود که رد شد و پیش از حادثه نیز درباره وضعیت روحی خود با فرماندهی و کادر پزشکی ناو صحبت کرده بود. به گفته او، پس از حادثه مراقبت‌های سلامت روان محدودی دریافت کرد و پیش از نخستین جلسه درمانی، دستور بازگشت به خدمت گرفت. اکنون این ملوان با
اقدامات انضباطی نیروی دریایی
روبه‌روست و طبق اسناد اتهامی، به
تمارض (Malingering)
و
غیبت بدون اجازه
متهم شده است. نام او به دلیل حفظ حریم خصوصی منتشر نشده است. این زوج یک
پسر سه‌ساله و یک دختر نوزاد
دارند
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21584" target="_blank">📅 12:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21583">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه ویس های دیروزم رو گوش کرده باشین ، خودتون صحبت های همه را میشنوید بعد تصمیم میگیرید به هر حال ،ما در راه شخص شخصه، فقط شخص خود شاهزاده ادامه میدیم و با اطراف کاری ‌نداریم و این بحث اینجا به پایان میرسد و تحقیق و تصمیم بیشتر با شما است
🙌🏾
اتحاد باید حفظ شود و رمز اصلی است همچنین انتقاد هم اگر محترمانه و درست بیان شود نیز باید شنیده و پاسخ داده شود
@WarRoom</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/21583" target="_blank">📅 12:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21582">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ایرج مصداقی مشاور شاهزاده رضا پهلوی: علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره. حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی…</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/21582" target="_blank">📅 12:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21581">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ایرج مصداقی مشاور شاهزاده رضا پهلوی:
علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره.
حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی مثلا؟! داریوش که میبینی که بلایی سرش اومده تو انگشت کوچیکه اونم نیستی.
بهش گفتن جهان پهلوان باورش شده. اخه مردک کسی که دوتا لگد به توپ زده پهلوونه؟! همین مونده بود تو برای ما شاخ بشی. فکر میکنه چون فوتبالش خوب بوده سیاستم میفهمه. ما اصلا تو رو حساب نمیکنیم ابله.
اینا رو ارزش دادنی فکر میکنن خیلی بالا هستن آقای کریمی با تو یا بی تو فرقی نمیکنه زیاد حرف بزنی صداتو میبرن
@WarRoom</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/21581" target="_blank">📅 11:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21580">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اتاق جنگ با یاشار : به نظر من علی کریمی باشرف است و جنگی ، ‌ابتدا باید با چهره خودش برگردد و این موضوع روشن شود ، افراد سمی دورش را عوض کند ، بعد بهترین فرد برای بخش جمع کردن کمک مالی برای مردم و کسانی که اعتصاب انجام میدهند باشد و این روند را مدیریت کند و از پتانسیل بالایش استفاده درست بشود باید در پست درست قرار بگیرد و بازی کند همچنین نیاز به همکاری بیشتر شاهزاده با ایشان هم هست و نباید ترد شود ، ولی باز میگم باید با چهره خودش برگردد اول
@WarRoom</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/21580" target="_blank">📅 11:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21579">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">علی کریمی : ‏از اين لحظه به بعد؛ از هيچ شخص يا حزب سياسى حمايت نميكنم. در حد توانم به مبارزه‌ام عليه رژيم اشغالگر شيعه ادامه خواهم داد. این تصمیم من به منزله سنگ اندازی در راه مبارزه دیگر افراد با رژیم اشغالگر آخوندی نیست.به اميد آزادى ايران و مردم نازنينش
@WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/21579" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21578">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یاسمین پهلوی : آدم‌هایی هستند که برای یک روز جنگیده‌اند، آنها خوبند. آدم‌هایی هستند که برای یک سال جنگیده‌اند، آنها بهترند. آدم‌هایی هستند که برای چندین سال جنگیده‌اند، آنها خیلی خوبند و آدم‌هایی هستند که تمام زندگیشان جنگیده‌اند، آنها اصیل‌ترین هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/21578" target="_blank">📅 11:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21577">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تحلیل الجزیره : توافق زمانی شکل می‌گیرد که ایران و آمریکا به اصل «امتیاز در برابر امتیاز» برسند؛ یعنی هر دو طرف چیزی بدهند و در مقابل، چیزی مشخص به دست آورند.
در غیر این صورت با پافشاری مانند تکرار شکست‌ها و بن‌بست‌های مذاکرات قبلی ، احتمال جنگ وجود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/21577" target="_blank">📅 11:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21576">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مدیرعامل شرکت ملی نفت : چندین پیمانکار در حال انجام عملیات بازسازی و نوسازی مخازن خارک هستند. بازسازی اسکله‌ها و مخازن و همچنین پروژه‌هایی که از قبل تعریف شده‌اند، بدون وقفه در حال انجام است و هیچ‌کدام از کارهای جاری متوقف نشده است. در حال حاضر برخی پروژه‌ها حدود ۲۰ و برخی حدود ۳۰ درصد پیشرفت دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/21576" target="_blank">📅 11:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21575">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lelb0SN2Ht5_mSn54ACr2naQpbib1xrnWfCVbfL1Cph8t1g8oqyL9kqiFmC1R8sgTmCBximfZU4WeVrOSn176icPP5-7ZU-BQ8Lcw6HqYtn5E5Poon4RRA4NWfLzZGMDDhvhANtCHkIsfVkRd7IdcwCrB3sfpOm825JXt2G_qLoBgWsnzYc8L5IOCEhkVfMpm4BxHCEYFHuIEr7yhl9SDm0vnwixa-D0mRQE6vpGygpwIngP2BIc80qMwwObCge37tgzl4tdYuqKx5RBZCTjtcUK2XE6eU6dNo09c2CULwIFqZSOFXvZEyEFqIEyQc4-Qfg4g10yLWvvOgLu9vYz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : همین الان قلعه حسن خان بغل ساختمان مربوط به دانشگاه که در جنگ قبلی مورد هدف قرار گرفته بود
@WarRoom</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/21575" target="_blank">📅 11:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21574">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سخنگوی کاخ سفید در واکنش به سفر وزیر خارجه قطر به ایران اعلام کرد که هیچ مذاکره‌ای با تهران در حال انجام یا برنامه‌ریزی‌شده نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/21574" target="_blank">📅 10:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21573">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a3060c7b.mp4?token=I71w4tP5AktEJgnsQf5R593yCOKR4oWSEjR457arX15CKj0bsn1utW1oUujGqSdpQbJkP1dsLBSz43OJxtYSh_SW9JW5H4Tcjt18klfxLQXFwkWxPqu7DXK5gf5ryj22XUb4grlfPRiIjO2hAx_CGOXTWmbscs5QuZgj45KWbEYKhzKGn3jJW0kdmnFX2Zbadc4ijVdUrRC6IYhFt7h-CAvuze95j6HE5saLDAKD5JZRoq0ywlnF3yIF6lV_gENOE59WKlbN1JxP4rd4e2G95H-JBKBbH6f4RQ-_4sjeg_ZsMEg_-9wCc3tyVVi-b8W052QgkwfSpWEv-88KzjqFsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a3060c7b.mp4?token=I71w4tP5AktEJgnsQf5R593yCOKR4oWSEjR457arX15CKj0bsn1utW1oUujGqSdpQbJkP1dsLBSz43OJxtYSh_SW9JW5H4Tcjt18klfxLQXFwkWxPqu7DXK5gf5ryj22XUb4grlfPRiIjO2hAx_CGOXTWmbscs5QuZgj45KWbEYKhzKGn3jJW0kdmnFX2Zbadc4ijVdUrRC6IYhFt7h-CAvuze95j6HE5saLDAKD5JZRoq0ywlnF3yIF6lV_gENOE59WKlbN1JxP4rd4e2G95H-JBKBbH6f4RQ-_4sjeg_ZsMEg_-9wCc3tyVVi-b8W052QgkwfSpWEv-88KzjqFsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بحران گازوئیل؛ صف‌های کیلومتری و سرگردانی رانندگان کامیون
‏گزارش‌ها از تشدید کمبود گازوئیل در جایگاه‌های سوخت و اختلال جدی در ناوگان ترابری جاده‌ای حکایت دارد؛ رانندگان کامیون در شماری از استان‌ها ناچارند برای دریافت سهمیه پایه سوخت ساعت‌ها و حتی روزها در صف‌های طولانی بمانند. کاهش سهمیه‌ها از سوی وزارت نفت رژیم جمهوری اسلامی، معیشت رانندگان و روند حمل و توزیع کالاهای اساسی را تحت فشار قرار داده و نگرانی‌ها درباره گسترش اختلال در حمل‌ونقل جاده‌ای را افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/21573" target="_blank">📅 10:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21572">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مؤسسه نیروی دریایی آمریکا USNI : گزارش داده است که ناو هواپیمابر تئودور روزولت CVN71 و ناوگروه رزمی آن در هفته‌های آینده از سن‌دیگو حرکت کرده و برای استقراری بیش از هفت‌ماهه در خاورمیانه آماده می‌شوند. فرمانده ناو نیز خدمه را برای مأموریتی حدود هشت‌ماهه آماده کرده است. این ناوگروه قرار است به حوزه فرماندهی مرکزی آمریکا اعزام شده و جایگزین ناو «جورج واشنگتن» شود؛ اقدامی که در ادامه حضور طولانی‌مدت ناوهای هواپیمابر آمریکا در منطقه و هم‌زمان با ادامه درگیری با ایران انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/21572" target="_blank">📅 09:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21571">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5D5nB0SEq3_eVQmaao6ErJKu3palx4PfB93hBdhaE0mPqxoA86MD7c89F-kmFUm7U_ImmUbqhwGG1-FZv5taRnVCxAShG9zEMr14MSvtHOJC4V05fKP2pssGdah2vg-JubNUZwEKzdz6-mFSoyeKAbzSsFZORebsPZprL5f0Qldwr0qpi3TvmD39yK_Lr7qVIA3OOOc8bAjZLE4u8AUHOtUlMN-H-DFkCpiEH191jcqir52ufq8dxJc4JpvamqF2PY5EHCpYVh3SjUK_xfqSZOeoV_VDPocXHkFJY1VGiwjXrtLIwdGkR5BqY2V0Ed4PkVxsdeT_lv--xs5Qh9ggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات دریایی بریتانیا بامداد پنجشنبه گفت که یک نفتکش در آب‌های نزدیک منطقه «الخصاب» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21571" target="_blank">📅 09:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21570">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وال استریت ژورنال به نقل از منابع آگاه گزارش داد که هدف از سفر جان راتکلیف، رئیس سازمان سیا، به مسکو در روز سه‌شنبه، هشدار دادن به روسیه  بود که از حمله به ناتو و کمک به ایران خودداری کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21570" target="_blank">📅 03:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21569">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnnD0Wc6WhJUqTYEoU7RWC9EHIHKymrbkEzxz3Bt7HK0zq9JjGp5R6myRAw9ypeTmDuQyOl3lCIAY2ZtmJxACnYNVWLg7ImD-Y6ldoedcu8oBaQGcvjVRXMjtG-SGduzz8U8vpMbz7BhXYJbdZIkT1TrHsO0Zn4KKltI1Dc0GgfVFzSvdI7OdX-FbLFTDyezgdiZNU86APiSHuepnMJXScKc3tETMWXRniRTKc7u5O0VXvh2vMOu0JJrmKN3ulqvcJDWF8SfZ6RVHI8xBy2HVwqpMtnCIEidTF7IjqN0jyxp95lh8fE6isvblNNGvNQo9jQOeIGrOpgIC7qGBF1w1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیونه خونست! صفحه اول روزنامه نوبنیاد امروز
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21569" target="_blank">📅 03:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21568">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">در منطق دیکتاتور مردم دو دسته‌اند: آنهایی که باید گول بخورند و آنهایی که باید گلوله بخورند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21568" target="_blank">📅 01:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بلومبرگ: وزارت دادگستری آمریکا در حال احیای «دادگاه غنائم جنگی» است تا بتواند نفتکش‌های ایران را به‌عنوان غنیمت ارتش مصادره کند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21567" target="_blank">📅 00:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تنگه دعواااا شد
🚨
🚨
🚨
🚨
پرتاب چند موشک از سیریک و صدای انفجار از تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21566" target="_blank">📅 00:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21564">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21922cc89d.mp4?token=n3RDsZJhcjc8Np2vl93K2dYGkQskcBnLlsARCCV0xW4Dw94ifRvJjwy4MKNIx9SYPNNLj0Wf1u3PW6NXCZ0iOzcNb-N6GUsoa-cp3hngFDojKFlZBotY1dxsGNpidDavF6h1zQfVlzbzNvpA_QUt3KhtOVtY2XSd6kZQVU0nggCEIcb_Tns87sfe06hSRsO4emYA06rnL5NjcmiC6Q-s6K9C_TUa8Wnx54nCS4HIt8bdrwoQ_KjJJiR-pkot3bwLB1LHsl_ARHeNvlPNx4Qi-N4XnYSnuokRtQYOdJp3Nvl1SA7YyVPVaVVYkoIR_ZzS8cHG_l_QJnMLf36rXP1I05O5BMYg9fFJ__NiL5FoOX5sVIh8oN6Pn1um3atmqlDQrRIqVZXRADkz3z2IHW5xLZILc_IAUU_aet_QiK4Y-hvwa63gbzsovcskSlbUs06YExZpamrDRq7XnXIBjD0G94PC1QxFT4SKpRlLCQf2AqUv4kHOiKKiGEQfLmS0hUa6jD9mjzsHwujGdACV7WJtawI6lbzdpbR9emRQUalkfoQXwTa2X5ynmHsan4kAPFkJhJRBuaz7lpXcm77-1qgU0JfsCcohFYfx6kSwgYpvLZuP_vQdOi6VHvYJ2hEKt0TFE59E9Qq2YiZER2_FL-9quKAn5E_5mwP2QFjlTMWpq9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21922cc89d.mp4?token=n3RDsZJhcjc8Np2vl93K2dYGkQskcBnLlsARCCV0xW4Dw94ifRvJjwy4MKNIx9SYPNNLj0Wf1u3PW6NXCZ0iOzcNb-N6GUsoa-cp3hngFDojKFlZBotY1dxsGNpidDavF6h1zQfVlzbzNvpA_QUt3KhtOVtY2XSd6kZQVU0nggCEIcb_Tns87sfe06hSRsO4emYA06rnL5NjcmiC6Q-s6K9C_TUa8Wnx54nCS4HIt8bdrwoQ_KjJJiR-pkot3bwLB1LHsl_ARHeNvlPNx4Qi-N4XnYSnuokRtQYOdJp3Nvl1SA7YyVPVaVVYkoIR_ZzS8cHG_l_QJnMLf36rXP1I05O5BMYg9fFJ__NiL5FoOX5sVIh8oN6Pn1um3atmqlDQrRIqVZXRADkz3z2IHW5xLZILc_IAUU_aet_QiK4Y-hvwa63gbzsovcskSlbUs06YExZpamrDRq7XnXIBjD0G94PC1QxFT4SKpRlLCQf2AqUv4kHOiKKiGEQfLmS0hUa6jD9mjzsHwujGdACV7WJtawI6lbzdpbR9emRQUalkfoQXwTa2X5ynmHsan4kAPFkJhJRBuaz7lpXcm77-1qgU0JfsCcohFYfx6kSwgYpvLZuP_vQdOi6VHvYJ2hEKt0TFE59E9Qq2YiZER2_FL-9quKAn5E_5mwP2QFjlTMWpq9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏وزیر انرژی ایالات متحده، رایت: در صورت شکست بازرسی‌ها و مذاکرات آژانس بین‌المللی انرژی اتمی، زیرساخت‌های هسته‌ای و صنعتی در ایران به صورت نظامی نابود خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21564" target="_blank">📅 00:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21563">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23dd6e08b2.mp4?token=fwmD0RZoIyI6MZH1KvxYl55C3G5rgIZpeks4RJ7liHCvMDCCTH5xsXpBDKGdfvFYY0IekYkU5HjTUXhK5jy8x9mHuxz2vdM_lqFM60QUVYJH4ECehN2aeYftBdr4t9XfHm81ReYcZ1Gb17PS2ACZGL3AB8Qnxu0J8qpkayblUoGpub1M8Zd17RJ3monxVoO2jm4EInWzB4Y8ypsYtaO8sYh2-jjtYL4Y7WjMubP0xxOihph9lKMw6OT8syXf5281yQYsiFYVG9TNS5UKHUggNzM_6zGERbBzggaZ5anqCzhx2EE3UfBZUyD5zHKNoa-HRWCsjYd5oh8OV21CfdEoEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23dd6e08b2.mp4?token=fwmD0RZoIyI6MZH1KvxYl55C3G5rgIZpeks4RJ7liHCvMDCCTH5xsXpBDKGdfvFYY0IekYkU5HjTUXhK5jy8x9mHuxz2vdM_lqFM60QUVYJH4ECehN2aeYftBdr4t9XfHm81ReYcZ1Gb17PS2ACZGL3AB8Qnxu0J8qpkayblUoGpub1M8Zd17RJ3monxVoO2jm4EInWzB4Y8ypsYtaO8sYh2-jjtYL4Y7WjMubP0xxOihph9lKMw6OT8syXf5281yQYsiFYVG9TNS5UKHUggNzM_6zGERbBzggaZ5anqCzhx2EE3UfBZUyD5zHKNoa-HRWCsjYd5oh8OV21CfdEoEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : سگ‌های نظامی در کنار نیروهای آمریکایی در سراسر خاورمیانه خدمت می‌کنند و ماموریت‌های حیاتی متنوعی را انجام می‌دهند. این جنگجویان چهارپا، هم‌تیمی‌های قابل اعتمادی در کمک به محافظت از نیروهای نظامی آمریکایی در برابر تهدیدات هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21563" target="_blank">📅 00:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21562">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21562" target="_blank">📅 23:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21561">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">@WarRoom
Ai</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21561" target="_blank">📅 23:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21560">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi ...</strong></div>
<div class="tg-text">درود یاشار جان بنظرت الان رو چه حرفه ای تمرکز کنم و یادش بگیرم که در ایران آینده بتونم کمک بزرگی رو انجام بدم</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21560" target="_blank">📅 23:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21559">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">@WarRoom
Final Battle</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21559" target="_blank">📅 23:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21558">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaha</strong></div>
<div class="tg-text">جنگ قبل انتخابات هست یا بعد ؟
بنظرت خودت؟ و با تحلیل و دیتا هایی که الان هست
❤️
🔥</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21558" target="_blank">📅 23:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21557">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21557" target="_blank">📅 22:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21556">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
نخست‌وزیر و وزیر خارجه فردا برای بررسی تنش‌زدایی و فراهم کردن زمینه‌های گفت‌وگو به تهران می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21556" target="_blank">📅 22:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21555">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دیدبان اتاق جنگ با تاخیر : درود من چند وقت بود میخواستم یه چیزی رو بگم ولی شک داشتم بگم یا نه  من ……….. این قسمت پیام  حاوی مشخصات دقیق فرستنده پیام بود و سانسور شد ……  برج مراقبت مهراباد یه تعدادی ادم بودن خیلی مذهبی و عرزشی بودن جوری که انگشت نما بودن  اینا…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21555" target="_blank">📅 21:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21554">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دیدبان اتاق جنگ با تاخیر : درود من چند وقت بود میخواستم یه چیزی رو بگم ولی شک داشتم بگم یا نه
من ……….. این قسمت پیام  حاوی مشخصات دقیق فرستنده پیام بود و سانسور شد ……
برج مراقبت مهراباد یه تعدادی ادم بودن خیلی مذهبی و عرزشی بودن جوری که انگشت نما بودن
اینا چون رادار نداشتن تو جنگ میومدن با بقیه ی برجای غرب کشور با عرزشیاشون هماهنگ میکردن که جنگنده اومد خبر بدن
میگفت ما ۹ اسفند یه ربع زودتر خبر دادیم که جنگنده و موشک دیدیم اگه میخواستن رهبرو پیاده و با پای خودش ببرن بیرون از بیت یا ببرن پناهگاه تو یه ربع میتونستن ولی اینکارو نکردن و گذاشتن بمیره حتی مدرک و اثباتم داشت که زنگ زده بود پدافتد و حفاظت بیت  میگفت حتی از زمان جنگ ۱۲ روزه رابطمونم خیلی خوب بوده با بیت چون خبر میدادیم بهمون اطمینان داشتن
و خب این یعنی ممکنه باقر قالیباف رهبرو با لابی و کودتا قربانی کرده باشه؟
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21554" target="_blank">📅 21:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21553">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانال 13: رئیس ستاد ارتش در دو روز گذشته توصیه کرده است که تعداد عملیات ترور هدفمند در غزه افزایش یابد، به عنوان پاسخی به "پرتاب هواپیماهای کاغذی"
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21553" target="_blank">📅 20:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21552">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرگزاری تروریستی فارس : یک نفتکش هند هنگام عبور از تنگه هرمز توقیف شد
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21552" target="_blank">📅 20:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21551">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfnErQdaMvKjFvrR5dmNIjDGj4V3oHKK-m0k3RzAkoj3zyZkOMGJu8AJgA3fMshuhS-4k1qxy2v5oBt7mlnJqFCXIfbI-RsttmNxjmj9hfxBfhdErC_q9QhSHKaux-gymhxxcea7922Zl_tN3XIoKgWfeSgqvNtWPrOE544rL0mn_911rN81NNSFjals32Wu2SarTyFiFVbanp3IoYecWFxXHdVQdckBy1gm0YF66D4Va3baJEM-g9dbQuYtodnRczKy6vQ9aNqRYnosFsTBY_ZiPlACVKt2rupMYuLJjEb5K1yH7tCoDKdxhh_q3np7XHxXgkvcmWDRWmTcToAgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در سال ۱۹۶۴، در دوران تحصیل در آکادمی نظامی نیویورک، در کنار پدرش «فرد ترامپ» و مادرش «مری آن ترامپ». ترامپ در سال آخر تحصیل به درجه «کاپیتان دانش‌آموزی» و شمشیر افتخاری دریافت کرد و همچنین فرماندهی گروهان A را بر عهده داشت. این تصویر مربوط به دوران فارغ‌التحصیلی او از آکادمی نظامی نیویورک است؛ یونیفرم او لباس تشریفاتی یک دانش‌آموز نظامی است، نه یونیفرم ارتش آمریکا.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21551" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21550">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLsn5_Bdm_CbhjM5ihH-mB8ztDSp4wQnV6T7BptjdJ3m6zFBf3nHhu_jaxOfh8LD5zIlxo0OL9OwWEBFgonJm7bdUmaYd9EuUeOGYoiezgj7j1bbr9TmXAhLsQ95Gb_DNQhvqczUpO8Xz88FB7pf8V9DxveCZ2mpWuZjJ3_olULu4p28yG2uift-U24UqwIRqZVCDvV8H-dMkguDAlNTvZiC1oHY5CUcxTDbRPDaHX6PYcKYnDeCLvT1FB7pEPKWIMOsOO3yY0Nw5lOOiLKLEqjfyuZ953rbgC1bWgQlW-7Q7vPFSW62fVV4Jg5Xzjj9X7Kg80skBjX5r90HPPNukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث مدعی است امسال کار رو جمع میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21550" target="_blank">📅 20:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21549">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrhlVDFHaIZOCWRYSYwfmvaMQ-8cHSgSSDibUVCBvDfYkqYTRQ7hHWtmOpIgkzocx5GdknAiwvAJEr0yoBhRJVn7Qa7IX9gnMwD0AL-QrTDZ8QqFustJ1569lps6swHExvYu7JO8vomA6fMSObBHKzluXwl5svtPR09XjMciobDRg0X0I5LNy7bgI0zOCLouTsLk-gNKXLtscPyidzeEonZgyxtNSUNXFe4OsqO5w9R7pxyR4gG5uniGBNc6FxIPyP9BM6ljAtb82zIp2fkEvh-IRASvyYIgsJwHnVjpqYl1IrXq2LYG4z3wNio24_lrsq1VdPjo2H1_AjRFSIR4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث پست عکسی از خودش و پدر مادرش را بازنشر داد که در کپشن آن نوشته شده : والدینی که دنیا را نجات دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21549" target="_blank">📅 19:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21548">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانال ۱۴ به نقل از آتلانتیک
:
منابع داخلی ایران به این نشریه گفته‌اند که
مجتبی خامنه‌ای، جانشین تعیین‌شده پدرش، یا از نظر بالینی مرده است یا در وضعیت نباتی به سر می‌برد
؛ موضوعی که پرسش‌های جدی درباره اینکه در حال حاضر چه کسی عملاً ایران را اداره می‌کند، ایجاد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21548" target="_blank">📅 19:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21547">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ در گفت‌وگو با الجزیره
گفت او گفت برای ازسرگیری مذاکرات با ایران «عجله‌ای ندارد» و برای انجام مذاکرات نیز «هیچ جدول زمانی مشخصی» تعیین نکرده است
همچنین گفت «ایران با مردم خودش بسیار بدرفتاری می‌کند. آنها تعداد بسیار زیادی از معترضان را می‌کشند.»
من شنیده‌ام تورم آنها ۹۰ درصد است، ولی من فکر می‌کنم تورم آنها در حقیقت ۳۰۰ درصد است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21547" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21546">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2699b93394.mp4?token=fK79L_S7hBSXwBEHHjScYEWshBty0BR5qqLirV4KDSFAovyrLwbaexu2bBZPrbUXPYJU0LMpJJqWZS9LuLQPqofmg0p3Bq7KsguEzfSLciHDvbjz-Tb18R_zBCvR8Vdq3hu1DaV-cs9F8-bSpdBliferXbMUHvMV_ftcU-gx_aIvSewD4oalKYR3cjCD10rgSjfuv-ThuyCiyjxhEoYBGi-TR_9SXO95GEdfjh6WdcX5YdJI2KpXuM06_2ILclwrSllToINjkXM45k61Pu_r0ZtQv3xb_cnWezcppKvdvz-2RUVqj6PKMUa6KF1Bfp6OxoF6rDeGjF3cgqQdIv0EhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2699b93394.mp4?token=fK79L_S7hBSXwBEHHjScYEWshBty0BR5qqLirV4KDSFAovyrLwbaexu2bBZPrbUXPYJU0LMpJJqWZS9LuLQPqofmg0p3Bq7KsguEzfSLciHDvbjz-Tb18R_zBCvR8Vdq3hu1DaV-cs9F8-bSpdBliferXbMUHvMV_ftcU-gx_aIvSewD4oalKYR3cjCD10rgSjfuv-ThuyCiyjxhEoYBGi-TR_9SXO95GEdfjh6WdcX5YdJI2KpXuM06_2ILclwrSllToINjkXM45k61Pu_r0ZtQv3xb_cnWezcppKvdvz-2RUVqj6PKMUa6KF1Bfp6OxoF6rDeGjF3cgqQdIv0EhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: وقتی افرادی هستند که حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است. به همین دلیل است که آنها اعتراض نمی‌کنند.
اما اکنون این احتمال وجود دارد(اعتراضات)زیرا آنها (رژیم)بسیار ضعیف شده‌اند... بسیاری از سربازان آنها حقوق دریافت نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21546" target="_blank">📅 17:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21545">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAbraham</strong></div>
<div class="tg-text">یاشار جان درود و ارادت
نمیدونم این پیام رو میبینی یا گم میشه لابه‌لای پیام های دوستان
فقط میخواستم بگم دمت گرم که توی این شرایط سخت و پیچیده که این بیشرفها برای ماها درست کردن تو پیشمون بودی و همیشه توی شرایط بحرانی بیشترین انرژی رو برامون میفرستی خدایش دیروز نشسته بودم توی پارک محلمون و به همه چی فکر میکردم ولی هیچ وقت به خ کشی اصلا فکر نکردم چون ماها حقمون این نیست که بخوایم بخاطر یه مشت چاغال بیشرف که بویی از انسانیت نبردن زندگی خودمون تموم کنیم
به هرحال همه ماها یه روزی می‌میریم ولی حداقل با شرافت بمیریم ن بخاطر این پیشرفا
پاینده باد ایران و ایرانی
❤️</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21545" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21544">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBehzad</strong></div>
<div class="tg-text">سلام یاشار جان عرض ادب
من تو کرونا پدر و مادرم رو تو یه تایم ۱۷ روزه از دست دادم و الان تنها ترینم
حرفات کاملا درسته ولی نمیدونم اگر شما ، مثل من ۳ ماه فقط سیب زمینی و نون لواش میخوردی بازم میتونستی اینجوری حرف بزنی یا نه.
برادر اوضاع خراب تر از چیزیه که میشنوی
منم دارم بین خود….. و ادامه دادن میجنگم</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/21544" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21543">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به گزارش خبرگزاری کم اعتبار مهر، ایران و روسیه قراردادی ۲۵ میلیارد دلاری برای ساخت نیروگاه‌های هسته‌ای جدید امضا کرده‌اند. انتظار می‌رود مسعود پزشکیان، رئیس جمهور ایران، و ولادیمیر پوتین، رئیس جمهور روسیه، هفته آینده در قرقیزستان دیدار کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/21543" target="_blank">📅 17:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21542">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/492b9e7ef3.mp4?token=GODf3G3Af_eAZ8TmW3rK3b7Mg6v4H2_VjVhof9xGGLBLa4ITZgeSy9tI7aIohT6b_mA9GM63JsA28iBmRgB5XSlpLv_TRGyMYV94JlJ-IuvSoQIWk6-6K-rLnHICiVpySvCtUw3s0h-JGGQ5xGGIHoXZDzOsPnKaFVgN9ToDuRwnzxYJ8Z2EOh8HFEB1i9R_pVdCofyv6y5DBt7aKZQp-bvgn9EHyuilQs3pvgHcQvxDdryj2g6_tN6bh1b00eAVg8k__sIPODPTDC6CIAe0QA-Mos1V4JuinNFpfg6PMH5MZ_EofrDDaKJ8-vFlR0NfJHOuRpXiXs7m1tEAOtgG3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/492b9e7ef3.mp4?token=GODf3G3Af_eAZ8TmW3rK3b7Mg6v4H2_VjVhof9xGGLBLa4ITZgeSy9tI7aIohT6b_mA9GM63JsA28iBmRgB5XSlpLv_TRGyMYV94JlJ-IuvSoQIWk6-6K-rLnHICiVpySvCtUw3s0h-JGGQ5xGGIHoXZDzOsPnKaFVgN9ToDuRwnzxYJ8Z2EOh8HFEB1i9R_pVdCofyv6y5DBt7aKZQp-bvgn9EHyuilQs3pvgHcQvxDdryj2g6_tN6bh1b00eAVg8k__sIPODPTDC6CIAe0QA-Mos1V4JuinNFpfg6PMH5MZ_EofrDDaKJ8-vFlR0NfJHOuRpXiXs7m1tEAOtgG3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
«ما مین‌ها را پاکسازی کردیم. اما تنگه [هرمز] باز است؛ تنگه در حال فعالیت است و کشتی‌ها از آن عبور می‌کنند.
بله، هر از گاهی ممکن است یک پهپاد یا یک موشک یا چیزی شبیه آن شلیک شود، اما تنگه کاملاً در حال فعالیت است.
حجم زیادی نفت در حال عبور است.
دیروز ۱۰ میلیون بشکه [نفت عبور کرد].»
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/21542" target="_blank">📅 17:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21541">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ درباره ایران:
این گروه حاکمان ، آن‌طور که باید، گروه چندان شرافتمندی نیستند؛ این را به شما می‌گویم.
ما خیلی زود در ایران به یک پیروزی بزرگ دست پیدا خواهیم کرد.
ما واقعاً، حقیقتاً، از همان ابتدا ایران را کاملاً تحت سلطه خودمان داشته‌ایم.
من قطعاً با اجرای قوانین شریعت مخالفت خواهم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/21541" target="_blank">📅 17:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21540">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f639ee98c9.mp4?token=QGEfazf-n9ynPU2ObNXEnyUUt_1LqiUUfXoCO3oi_hM06EkDFtvbFDozsbVWdBVjtsKclwkVQ3OaV66KcdF6pIV_0_Gqo8MngyxdZUaSq4ws5jUVSPP3VpJ7UDQKvqEEvnIfl-jMHKOCuw-L5SZ3xyDA8I3CDIEPWCWC6lyG-fSbosveQ8YKSJ-9zPrG3q0WdExd60DNnVEoA9WEtqBz5DK10LzXm3_i4fCyOT4WVrWeL8DK8dncwt4rGjUJlf8TCUZ72RsjcV62EGrnFZE4Cm6EQzSG-4I65cwEkjunW7Bcu5NdHTobHmgj8QPhwiHWzybrIBuKgC7u7QCD1u60vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f639ee98c9.mp4?token=QGEfazf-n9ynPU2ObNXEnyUUt_1LqiUUfXoCO3oi_hM06EkDFtvbFDozsbVWdBVjtsKclwkVQ3OaV66KcdF6pIV_0_Gqo8MngyxdZUaSq4ws5jUVSPP3VpJ7UDQKvqEEvnIfl-jMHKOCuw-L5SZ3xyDA8I3CDIEPWCWC6lyG-fSbosveQ8YKSJ-9zPrG3q0WdExd60DNnVEoA9WEtqBz5DK10LzXm3_i4fCyOT4WVrWeL8DK8dncwt4rGjUJlf8TCUZ72RsjcV62EGrnFZE4Cm6EQzSG-4I65cwEkjunW7Bcu5NdHTobHmgj8QPhwiHWzybrIBuKgC7u7QCD1u60vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:فکر نمی‌کنم مجتبی خامنه‌ای مرده باشد.
او به شدت زخمی شده بود، سمت چپ بدنش، بازو، پا، کل بدنش به شدت زخمی شده بود.
اما فکر نمی‌کنم مرده باشد
اگر مرده باشد، آنها نمایش خیلی خوبی اجرا می‌کنند، زیرا مدام در مورد بازگشت و صحبت با او برای گرفتن آخرین دعایش صحبت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/21540" target="_blank">📅 17:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21539">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">@WarRoom
Apple</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/21539" target="_blank">📅 16:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21538">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتانیاهو:
من به ترامپ گفتم ایران رو تشدید محاصره کن
!
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/21538" target="_blank">📅 16:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21537">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ac4e3799.mp4?token=tZB6eetF-LWZpjxV1ggoH7JPt6mGVN2mhXrql6BbAuliqLPKjDqa3u9ROLsAa0S8M320PoxuJuYD0ne5cPXqOSLDJGNQIOPpe4_M2hKGPbvcnfvKd4plYHkx05ekNMOxUhdIctqok-TbcEgLUUxQWrxiAoRTRhm5mIILMBan9FSMTSQop5APzszdde6rd_-KM-iRTSEAUOe5fQQ-u5JIugK_KZOeNinsyPqWPb-V4qPENMdMtbrxNclLyaTHpce86ocvMbUqQmS4JYRffu2hOtaS7wfLp0_RitU174p-TbPj_neOQkWm8skFA_B4Q3pJ8Vyqfg3_2guTcErI7ekbVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ac4e3799.mp4?token=tZB6eetF-LWZpjxV1ggoH7JPt6mGVN2mhXrql6BbAuliqLPKjDqa3u9ROLsAa0S8M320PoxuJuYD0ne5cPXqOSLDJGNQIOPpe4_M2hKGPbvcnfvKd4plYHkx05ekNMOxUhdIctqok-TbcEgLUUxQWrxiAoRTRhm5mIILMBan9FSMTSQop5APzszdde6rd_-KM-iRTSEAUOe5fQQ-u5JIugK_KZOeNinsyPqWPb-V4qPENMdMtbrxNclLyaTHpce86ocvMbUqQmS4JYRffu2hOtaS7wfLp0_RitU174p-TbPj_neOQkWm8skFA_B4Q3pJ8Vyqfg3_2guTcErI7ekbVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون فردی در بالای پل طبیعت میخواد خودشو … آتشنشانی در حال مقابله و کمک است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21537" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21536">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21536" target="_blank">📅 16:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21535">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شرکت راک‌استار گیمز سکوت خود را در مورد لو رفتن گیم‌پلی GTA 6 شکست و آنها را «دلخراش» خواند و عذرخواهی کرد که «بدیهی است که این آن چیزی نیست که ما می‌خواستیم شما از بازی ببینید.»
آنها تأیید کردند که بازی «تقریباً آماده است» و فردا یک نمای کلی از آن نمایش داده خواهد شد.
تاریخ انتشار تایید شد: ۲۸ آبان
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21535" target="_blank">📅 15:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21534">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرنگار الجزیره در تهران: بر اساس گزارشات آمریکا با ۱۶ کشور هم‌مرز ایران برای قطع روابط اقتصادی با ایران تماس گرفته!
۸ کشور درخواست آمریکا را دشوار دانستند و ۸ کشور دیگر پاسخ دادند که در حال بررسی این احتمال هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21534" target="_blank">📅 15:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21533">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ریزش قیمت خودرو در بازار
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21533" target="_blank">📅 14:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21532">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هادی لومپان امسال نمیتونه ویزای آمریکا رو بگیره و در مسابقات آرنولد کلاسیک شرکت کنه ، او با قرار دادن یک استوری گفت : جشن بگیرید هادی چوپان از ایران امسال نیست اما پایانش هم نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21532" target="_blank">📅 13:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21531">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فاطمه مهاجرانی ، سخنگوی دولت : مردم منتظر بهتر شدن وضع اقتصاد در شش ماه یا یک سال آینده نباشند. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21531" target="_blank">📅 13:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21530">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فرمول جهانی حاشیه برای معرفی کالای‌جدید
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21530" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21529">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd86e564c.mp4?token=us30JR8_LYHQwScNPFgCP4nhQv76_rZhb-IafC4b5QJP_uxSGUCcL9SSJfK_Echjb8fhdZWcFw3e8FEWje2dEhUXUczb_dCFFoKs_DzoUXZN-tOvNBCj2dVdSzFrNCOOlG3JMCzqUZsIdX4QNZdzvAIwIKzdSfWFG6oA2z583rZgj3p6mcwzjaZuCTQx2vPY7_lsBihO9CZnlwuU3Gu80VYewRaFGyKpHHXvdtHUxrmti3nHRX1ASx8l-co8EsF7xqX9wII5pHfqr6Dw07RG3ujvJ9Nwci5jDJYaCydytmz6aqtG4BcdRipyRTNnfwok5LNNkPQAJV5Ho9dZXGrSvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd86e564c.mp4?token=us30JR8_LYHQwScNPFgCP4nhQv76_rZhb-IafC4b5QJP_uxSGUCcL9SSJfK_Echjb8fhdZWcFw3e8FEWje2dEhUXUczb_dCFFoKs_DzoUXZN-tOvNBCj2dVdSzFrNCOOlG3JMCzqUZsIdX4QNZdzvAIwIKzdSfWFG6oA2z583rZgj3p6mcwzjaZuCTQx2vPY7_lsBihO9CZnlwuU3Gu80VYewRaFGyKpHHXvdtHUxrmti3nHRX1ASx8l-co8EsF7xqX9wII5pHfqr6Dw07RG3ujvJ9Nwci5jDJYaCydytmz6aqtG4BcdRipyRTNnfwok5LNNkPQAJV5Ho9dZXGrSvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21529" target="_blank">📅 12:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21528">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fffd91f0.mp4?token=CJ2eTypEsGXhiDmIUrQYwtGTKOioEpkw3oXlsVBbajip1VCrP76geRU7mc3ahT4Dfw8-ofKSEyvdEy40PJXyCvgPlsEvs-6v0lJv7VlmJ_Z8a4nN8rDfSrc0-Vpcu4JbEOAuz0dzCVlUbHK6pS53TundJvrpNc_wxyFoMQWubkfpF8qImWsKNWtHrN8R-FLhTM0FgWaEmbp_pXxBeKsNFrBWX1Zt-SZCyEL8Vjy5UC-nwXwxWeQ-WvJulDLOW3g9mQXUi0ddZDVvfSB_CQE-s9PuwXK9rCjW8tBlPK5xgUeHYmUTHKs-_1ko2FvpZ4i5TTawZi5MrnULwzneqZqhyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fffd91f0.mp4?token=CJ2eTypEsGXhiDmIUrQYwtGTKOioEpkw3oXlsVBbajip1VCrP76geRU7mc3ahT4Dfw8-ofKSEyvdEy40PJXyCvgPlsEvs-6v0lJv7VlmJ_Z8a4nN8rDfSrc0-Vpcu4JbEOAuz0dzCVlUbHK6pS53TundJvrpNc_wxyFoMQWubkfpF8qImWsKNWtHrN8R-FLhTM0FgWaEmbp_pXxBeKsNFrBWX1Zt-SZCyEL8Vjy5UC-nwXwxWeQ-WvJulDLOW3g9mQXUi0ddZDVvfSB_CQE-s9PuwXK9rCjW8tBlPK5xgUeHYmUTHKs-_1ko2FvpZ4i5TTawZi5MrnULwzneqZqhyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
می‌خواهم به شما بگویم: ما هنوز چالش‌هایی پیش روی خود داریم.
چالش ایران تمام نشده است.
ما همچنین باید چالش غزه، لبنان و سایر عرصه‌ها را به پایان برسانیم و مصمم به انجام این کار هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21528" target="_blank">📅 12:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21527">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296e867e7b.mp4?token=kYcN9fMET8BwEpj6gNgdbNjf22qtld9K4DHL91Mcr7IHAeIdjIpqp3qDO2dSmOWzMYGgsVYv2cTB2L3ANZAmTiYVYNxWLXMlanQs-PFf3vLXM3kskXLPLG7QVohbzs_OYAwVhX5KhUrRpCfASZMgsa6CF3GhEgtO7RvfDTKxOGdQUIFX94fte7pPxo4fJajqVJxrTAyxeT75wVrhEnvd_r7ydq7cON6cASq2iTU5_aEYCiVg2Ue01jyRMRynhRNMWYXB7i2sC-hJMOb3Y8MLW7E3FYUaq2WJSOEKr1RiXJGtIrcw9-_Mk4RgVhK7R9S6RXTvSB5Nl6Sx_We6et60VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296e867e7b.mp4?token=kYcN9fMET8BwEpj6gNgdbNjf22qtld9K4DHL91Mcr7IHAeIdjIpqp3qDO2dSmOWzMYGgsVYv2cTB2L3ANZAmTiYVYNxWLXMlanQs-PFf3vLXM3kskXLPLG7QVohbzs_OYAwVhX5KhUrRpCfASZMgsa6CF3GhEgtO7RvfDTKxOGdQUIFX94fte7pPxo4fJajqVJxrTAyxeT75wVrhEnvd_r7ydq7cON6cASq2iTU5_aEYCiVg2Ue01jyRMRynhRNMWYXB7i2sC-hJMOb3Y8MLW7E3FYUaq2WJSOEKr1RiXJGtIrcw9-_Mk4RgVhK7R9S6RXTvSB5Nl6Sx_We6et60VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو : دستیابی به توافق با ایران ممکن نیست‌‌ @WarRoom
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21527" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21526">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بنیامین نتانیاهو : دستیابی به توافق با ایران ممکن نیست‌‌
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21526" target="_blank">📅 12:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21525">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نرخ دلار ۱۹۹،۰۰۰ تومان
دلار کف بازار  ۲۰۰-۲۰۵ هزار تومان
تتر۱۹۷،۵۰۰ تومان
بیتکوین ۷۹،۰۰۴ $
انس جهانی طلا ۴،۶۲۸ $
نفت برنت ۸۵،۵۴$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21525" target="_blank">📅 12:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21524">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXihZg98U1_61VBJc2Z4rkJziZA5C6YjvANklsubs-g2phl0o1PEtWqAmJqnt5AkYm5d0iOOiW4toiCqcJNF7cLnQ7VNf7GXAlz-sqcl5xBvfBm0yE1aI5Hd-wnV2W18ldz6Hpscp_9Trd0ccxJgN_nc0OgKwxr70yUw0BePAmK2WjtdCfyCI-yEBqwzb0KyB8yu_WutBKe8OdjMAFvOGzjsATsWuVz5tJugCIoNr4EUpCaYKGnPiiZDmT6dzzayr9VC-JZD9Hm1AnurJulemOr5irJAAN_ITYxpAHhz9awUTzMUgFElorlJzg6CjAJ6V9dXHbNVqOv_p8KgsXaB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط با یک دیپلم ساده، می‌توانستی
رایگان خلبان شوی، مدرک معتبر بین‌المللی بگیری، برای آموزش و کار به خارج از کشور بروی، تمام هزینه‌های زندگی‌ات را دریافت کنی و حتی ماهانه حقوق و کمک‌هزینه بگیری
؛ آن هم در شغلی که در سراسر دنیا مایه افتخار و احترام بود. امکاناتی برای ساختن آینده یک جوان ایرانی که امروز باورکردنش برای خیلی‌ها سخت است…
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21524" target="_blank">📅 11:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21523">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تانکرترکرز : امروز دریای عمان حسابی شلوغ بوده و حداقل 15 عملیات انتقال نفت از یک کشتی به کشتی دیگه در حال انجام بوده.
در مجموع حدود 25 میلیون بشکه نفت خام به‌علاوه مقداری فرآورده نفتی در حال جابه‌جایی بوده.
ایران در بین صادرکننده‌های نفت خام این لیست دیده نشده؛ نشونه‌ای از این‌که کشورهای منطقه دارن با انتقال کشتی‌به‌کشتی، مسیر صادراتشون رو تو شرایط فعلی حفظ می‌کنن.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21523" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21522">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیوزمکس: یائیر نتانیاهو هدف طرح ترور رژیم جمهوری اسلامی در آمریکا بود. بر اساس این گزارش، در ماه دسامبر نگرانی‌هایی جدی به وجود آمد که مأموران رژیم جمهوری اسلامی وارد میامی شده و یائیر نتانیاهو را تحت نظر گرفته‌اند. شدت تهدید به اندازه‌ای بود که به او حتی اجازه بازگشت به آپارتمانش برای برداشتن وسایل شخصی داده نشد و تحت تدابیر امنیتی از آمریکا به اسرائیل منتقل شد؛ جایی که بنا بر این گزارش تاکنون در آن اقامت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21522" target="_blank">📅 10:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21521">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کارولین لویت به نقل از
بسنت: رهبران ایران در برابر فشار اقتصادی ترامپ «دچار وحشت شده‌اند» او وعده داد «تمام راه‌های حیاتی اقتصادی» ایران را قطع کند.
﻿
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21521" target="_blank">📅 10:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21520">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آکسیوس
:
انتظار می‌رود سیاست افزایش فشار اقتصادی علیه ایران تا بعد از انتخابات میان‌دوره‌ای در آبان ادامه یابد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21520" target="_blank">📅 09:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21519">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">معاون اول پزشکیان : هنوز مسائل مهمی در حال مذاکره هستند ولی ما در صداقت و تعهد طرف مقابل به وعده‌هایش تردید داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21519" target="_blank">📅 09:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21518">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دارلین گراهام در دور دوم انتخابات سنای جمهوری‌خواهان کارولینای جنوبی پیروز شد و با حمایت قوی رئیس‌جمهور ترامپ، نماینده رالف نورمن را با ۵۲٪ در مقابل ۴۸٪ شکست داد.
گراهام که پس از مرگ برادرش لیندسی گراهام به این سمت منصوب شده است، اکنون در ماه نوامبر با آنی اندروز، دموکرات، روبرو است و به شدت شانس پیروزی دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21518" target="_blank">📅 09:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21517">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">منبع مطلع به آکسیوس : استیو ویتکاف و جرد کوشنر، قرار است
روز چهارشنبه
برای دریافت گزارش درباره وضعیت میدانی، به منطقه فرماندهی مرکزی آمریکا ، سنتکام بروند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21517" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21516">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هم اکنون حملات ارتش اسرائیل به علی طاهر، المنصوری، تزربین و الکنترا در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21516" target="_blank">📅 00:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21515">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کاخ سفید در واکنش به گزارش‌هایی از پاکستان مبنی بر پیشنهاد آمریکا برای پایان دادن به محاصره دریایی ایران در ازای بازگشایی تنگه هرمز و مهار نیروهای نیابتی تهران در منطقه،
انجام هرگونه مذاکره یا تماسی با ایران را رد و تاکید کرد که محاصره دریایی اعمال‌شده علیه ایران «با تمام قدرت و اثربخشی» ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21515" target="_blank">📅 00:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21514">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کاظم دستکج، معاون عراقچی :
چرا باید همیشه منتظر حمله آمریکا باشیم؟
ما می‌توانیم اقدامات پیشگیرانه انجام دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21514" target="_blank">📅 23:52 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
