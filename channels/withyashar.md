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
<img src="https://cdn4.telesco.pe/file/uljMtn0IZLWNiO8cEp2u0l9vPbiwjWn5evvzY4KDNAwgpLiXD9YthMR9i4zEsY17rNC3j6hrVaa-9WSDnkBBHHP2V4ea_y0i0__8vUvBuheVJ99O-UJ7JFKsToHb3ZJWg7qYdiOVVrVdgjjncj9t5ncQi-wT8jOH_877EOmVVBcYXjfVwcUn1dZpQvS5dBMEN07uuTU09yte7IT74msm-HVMybKsqVHSkIW3RyTFGvD0F6Clt04hZ2-R1pt94DYiIA7YSfma19GUJBzAk9U8msliwTjEdm5vITkUcT91p8rPYEtnBpuPY6xI-IHs3cKYklLzeKNgAZnKBoFo7uDYdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 454K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 00:41:31</div>
<hr>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فاکس‌نیوز: ترامپ، در آستانه
هفته ای سرنوشت ساز
و دیدار با رهبران کشورهای حاشیه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، در حال بررسی اقدام بعدی خود درباره ایران است.
ترامپ به فاکس‌نیوز گفت: «من در حال تصمیم‌گیری هستم. سؤال من این است که اگر و زمانی که تصمیم بگیرم، آیا کل کشور را منفجر کنم؟ آنها بهتر است رفتارشان را درست کنند.»
او در حال بررسی گزینه‌هایی از جمله اقدام نظامی، ادامه فشار اقتصادی یا تلاش دوباره برای توافق با ایران است.
ترامپ به فاکس نیوز گفت:  برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در این هفته آمادگی دارد، اما در حال حاضر هیچ دیداری میان دو رهبر در برنامه رسمی قرار ندارد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/23747" target="_blank">📅 00:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏منابع محلی نزدیک مرز ایران و پاکستان:  تعداد زیادی از افراد مسلح بلوچ وارد منطقه رادیگ در مند، شهرستان کیچ، بلوچستان شده‌اند و طبق گزارش‌ها، در چندین نقطه ایست بازرسی ایجاد کرده‌اند.
‏گزارش‌ها همچنین حاکی از آن است که یک اردوگاه نیروهای امنیتی پاکستان مورد حمله قرار گرفته است
@WarRoom</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/23746" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک‌تایمز: علی الزیدی، نخست‌وزیر عراق، متعهد شده است گروه‌های شبه‌نظامی مورد حمایت ایران را تا ژوئن ۲۰۲۷ خلع سلاح کند. طبق این طرح، ابتدا یک دوره ۹۰ روزه بدون حمله میان شبه‌نظامیان و نیروهای آمریکایی در نظر گرفته شده و سپس تحویل سلاح‌ها تا ۳۰ ژوئن ۲۰۲۷ انجام خواهد شد. شبه‌نظامیان خواستار تمدید این مهلت تا پایان ۲۰۲۷ هستند. الزیدی همچنین گفت عراق به‌دلیل بسته‌شدن تنگه هرمز حدود ۶۰ میلیارد دلار و ۶۰ درصد درآمد ماهانه صادرات خود را از دست داده و ایران اجازه عبور نفتکش‌های عراقی از تنگه را نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/withyashar/23745" target="_blank">📅 00:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">BTC 84,100$  @WarRoom</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/23744" target="_blank">📅 00:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیروهای مسلح لتونی کشور اروپایی: آماده باشید! به اطلاع می‌رسانیم که احتمال وجود تهدیدی در فضای هوایی لتونی وجود دارد.
حدود ۵۰ دقیقه پیش، هشدارهایی در پی احتمال وجود تهدیدی در حریم هوایی منطقه «کراسلاوا» (Krāslava) در لتونی که در امتداد مرز با بلاروس و در نزدیکی مرز روسیه واقع شده است  فعال شد.جنگنده‌های ناتو به منطقه اعزام شدند. هنوز جزئیات بیشتری منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/23743" target="_blank">📅 23:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز گزارش داد که جان راتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، اوایل امروز، بدون هماهنگی قبلی، در جریان سوخت‌گیری هواپیماهایشان در فرودگاه شانون ایرلند، با زلنسکی، رئیس جمهور اوکراین، دیدار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/23742" target="_blank">📅 23:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تحلیلگر آمریکایی : ترامپ با یه مصاحبه و جمله احتمال توافق، قیمت نفت رو از ۱۰۷ به ۹۷ دلار رسوند. عربستان هم به دنبال بازگشایی خط لوله شرق-غربه و با این تفاسیر دیگه نیازی به تنگه هرمز نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/23741" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">چپقچی وزیر امور خارجه برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شد.
@WarRoom</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/23740" target="_blank">📅 23:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23739">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیروهای دولتی یمن: تلاش گروه حوثی برای نفوذ در جبهه "العنین" در منطقه "جبل حبشی" در غرب شهر تعز را خنثی کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/23739" target="_blank">📅 23:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/23738" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/23737" target="_blank">📅 23:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM.g</strong></div>
<div class="tg-text">یاشار داداش انشالله اگه ما تو این انقلاب شیرو خورشید پیروز شدیم
شما ایران میای؟
تکلیف چنل چی میشه؟</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/23736" target="_blank">📅 23:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از گزارشها اینگونه بیان میشود که از حدود یک ساعت پیش سامانه میخک واردات خودرو را بسته
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/23735" target="_blank">📅 22:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ماهان‌ایر: از امروز ۲۱ سپتامبر
پروازهای خود به استانبول، آنکارا و گرجستان را متوقف کرده است؛ مسیر تهران–مسقط نیز از ۱۷ سپتامبر متوقف شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/23734" target="_blank">📅 22:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترکیش ایرلاینز: طبق اعلام یک نماینده این شرکت،
تمام پروازهای ترکیش ایرلاینز به ایران فعلاً تا(نوروز) مارس ۲۰۲۷ برنامه‌ریزی نشده‌اند
و ادامه آنها پس از آن تاریخ نیز تضمین نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/23733" target="_blank">📅 22:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الجزیره: در چند ساعت اخیر گزارش شد یک
کشتی دوم
نیز در تنگه هرمز بر اثر برخورد بقایای یک پرتابه ناشناس آسیب دیده است. هیچ‌کس زخمی نشده و کشتی به مسیر خود ادامه داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/23732" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23731">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : باز هم برخی ادمین‌های بی‌اطلاع تلگرام اشتباه کردند و نوشتند «هلیکوپتر جدید مارتین وان»! اولاً نام آن Marine One (مارین وان) است. مارین وان اسم یک مدل هلیکوپتر نیست؛ به هر هلیکوپتری از تفنگداران دریایی آمریکا که رئیس‌جمهور را حمل کند Marine…</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/23731" target="_blank">📅 22:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، برای نخستین بار از هلی‌پورت تازه‌ساخته‌شده در محوطه جنوبی کاخ سفید استفاده کرد و با بالگرد ریاست‌جمهوری «مِرین وان» از این محل به مقصد خود رفت. ترامپ در پیامی ضمن تشکر از جیم تایکلت، مدیرعامل لاکهید مارتین، گفت این شرکت کمک…</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/23730" target="_blank">📅 22:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23729">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df0feca14.mp4?token=mXYJs3ZxI-_Cf14GvPtipdn1p3yag35zSqUvfL2kJwWt3gwN-jbTsdry8WeeEk3wBuolgoPMNnoUezLftx6XZ1GLDr8CLGFRmmMB9yQMakeMCmCCAMUVe9_MVRvQRrEfSJ2M8wE1pMGxNtX37NY8APn0-bM8YNnh425dvuUFN0DmozxM4UV7hyeSUzMqF4veRcIMzVooehYT-ocYzgifFgCUXO1IOdUHYcKlM67pmbFzJ1OwUiwFZkv_3EupWK_-_7XCspJFPCqF58HT_GbQfz5UEN4BWHaSstSMnSTa-BzDwZmk8MINN1WYa-0IYyJfuwBYSowm_TG61BRbNGYgPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df0feca14.mp4?token=mXYJs3ZxI-_Cf14GvPtipdn1p3yag35zSqUvfL2kJwWt3gwN-jbTsdry8WeeEk3wBuolgoPMNnoUezLftx6XZ1GLDr8CLGFRmmMB9yQMakeMCmCCAMUVe9_MVRvQRrEfSJ2M8wE1pMGxNtX37NY8APn0-bM8YNnh425dvuUFN0DmozxM4UV7hyeSUzMqF4veRcIMzVooehYT-ocYzgifFgCUXO1IOdUHYcKlM67pmbFzJ1OwUiwFZkv_3EupWK_-_7XCspJFPCqF58HT_GbQfz5UEN4BWHaSstSMnSTa-BzDwZmk8MINN1WYa-0IYyJfuwBYSowm_TG61BRbNGYgPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، برای نخستین بار از هلی‌پورت تازه‌ساخته‌شده در محوطه جنوبی کاخ سفید استفاده کرد و با بالگرد ریاست‌جمهوری «مِرین وان» از این محل به مقصد خود رفت. ترامپ در پیامی ضمن تشکر از جیم تایکلت، مدیرعامل لاکهید مارتین، گفت این شرکت کمک ارزشمندی برای ساخت هلی‌پورت انجام داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/23729" target="_blank">📅 21:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23728">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تنگه صدای علی لاریجانی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/23728" target="_blank">📅 21:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3SrkxSDcLXTDIcNvKA6r1-7FpmJEss3WEwuoOvoXySl-uhvWw7jr9vX1hcF2EtpWv3oMO8z_pnoo9XSgxWuwGFzupVpF_j15ftF89l17-DyK0zfSSZ2HHOfrjgd-_swWNjKA_9Ae7-uXzDB-iicSGz3NoYzJhM8QwFntwQwVxPmm7xjlpNtczRs-ecZ3Y477NJgWpFb8pko_XjoUN6GVaTtrt6c9aUArz0-NQd2k598oMyp-xDR-et8R8__-SlYXEDp4giNvysehhI4JLdYab4EhROgElM1yxXMREG_zkl5rZIeAkkFi6MBD3YXa9LMVe0kVs1uaGddNR96pHWVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرقت موبایل یک پاکبان در مشهد @WarRoom</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/23727" target="_blank">📅 21:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرنگار الجزیره: ارتش اسرائیل عملیات سوم تخریب را در مناطق تحت کنترل خود در جنوب شهر خان یونس در جنوب نوار غزه انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/23726" target="_blank">📅 21:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23725">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بلومبرگ گزارش داد بریتانیا در حال بررسی گسترش حمایت نظامی از عربستان سعودی است؛ ریاض از لندن برای مقابله با تشدید حملات حوثی‌ها و حفاظت از خاک و زیرساخت‌های نفتی خود درخواست کمک کرده است. عربستان همچنین خواستار حمایت عملیاتی و دفاعی بریتانیا شده
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/23725" target="_blank">📅 21:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ گزارش داد ایران به یک محموله دیگر گاز طبیعی مایع‌شده (LNG) قطر اجازه عبور از تنگه هرمز به مقصد پاکستان را داده است. بر اساس این گزارش، یک محموله دیگر LNG قطر نیز در همین ماه با مجوز ایران از تنگه هرمز عبور کرده و به پاکستان رسیده بود. کشتی حامل محموله جدید قرار است فردا به پایانه واردات LNG پاکستان برسد
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/23724" target="_blank">📅 21:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کان: منبعی در شورای رهبری ریاست‌جمهوری یمن گفت تماس تلفنی ترامپ با رشاد العلیمی، رئیس این شورا، چیزی فراتر از ابراز حمایت احساسی از سوی رئیس‌جمهور آمریکا نبوده است
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/23723" target="_blank">📅 21:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0a6a7ba3.mp4?token=eGgazauh7mVFHkNBgNuL_Wd8JGKfNucCS53Tbz0lyerW5YlB1pHCfM8j7jVISFCjk-zMGMJRWyq5lyGP7pea9irsRUsXH-3euVuSVz1nG26X8QQcc001QQGF3JG75o84lLn2wMYRySFpgI3lgI78LhPccZwp2V6wUI1PMjqsAREbAfI_8KxSRNBYN9mBikdggEtAncNiA7m-HtzSQ4-N1RxPZ0jEw-ZUHEoCDkGb7nyi2PB1UzpuvRotLyea9wzu7c-FO-D9U3OLMRJdoDbvlBFQCMwbfHqJJASYKAazRaordXnd83fz4I7otLWEuW2Chkgn4I9oaSGTNgEQg6ApFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0a6a7ba3.mp4?token=eGgazauh7mVFHkNBgNuL_Wd8JGKfNucCS53Tbz0lyerW5YlB1pHCfM8j7jVISFCjk-zMGMJRWyq5lyGP7pea9irsRUsXH-3euVuSVz1nG26X8QQcc001QQGF3JG75o84lLn2wMYRySFpgI3lgI78LhPccZwp2V6wUI1PMjqsAREbAfI_8KxSRNBYN9mBikdggEtAncNiA7m-HtzSQ4-N1RxPZ0jEw-ZUHEoCDkGb7nyi2PB1UzpuvRotLyea9wzu7c-FO-D9U3OLMRJdoDbvlBFQCMwbfHqJJASYKAazRaordXnd83fz4I7otLWEuW2Chkgn4I9oaSGTNgEQg6ApFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی وینس، معاون رئیس‌جمهور:
امسال در ماه نوامبر(آبان)، سرنوشت‌ساز خواهد بود. یا باید در برابر این دیوانگی بایستید، یا با آن همراه شوید.
و ما برای ایستادگی در برابر آن و مبارزه با آن اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/23722" target="_blank">📅 21:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj-5yqnPqdmvK4P3NYPjQGhdUmRa5qqIBRf5CfP5S8hW9nBGcrvjQuHZ9PSTQCzK7VUlZbU8OqGO0ga8ray1QUmOps9fchn7zu2XDxjI1fbFsNcnDOeBaQv9D3eKEUob2h9p5jT4006JnSHFcFMeeC4AO5UQFPFdmumdIhAibthUD2tEl6YmQhQYqGjKR304YPRgAfFAHBTsabc1cXbspEOBYaLAeKpmh0FPO5E_0yJMc2m6yM2MBzbRcdYYA-IejrGn4JNGey0xRPDjR13bBBRA4JkFn2wq8dQ9163fMCZdhcWryImskCe3NvBnSSvdzv8zkhflN38CGlh7HlLHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت به زیر ۱۰۰$ آمد و حملات موشکی جمهوری اسلامی به کشتی ها تأثیر خود را از دست میدهند. قیمت در این لحظه ۹۹.۵$
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/23721" target="_blank">📅 21:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23720">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
ما ایران را
بیش از هر زمان دیگری تحت فشار قرار داده‌ایم
. حدود یک ماه پیش پنج اختیار تحریمی جدید علیه حکومت ایران به دست آوردیم که حوزه‌های
هواپیمایی، دریانوردی، رمزارز و طلا
را شامل می‌شود. از
۲۳ سپتامبر
تمام خطوط هوایی ایران در سراسر جهان تحت فشار قرار خواهند گرفت؛ به این معنا که در صورت فرود هواپیماهای ایرانی، ارائه
سوخت، خدمات فرودگاهی یا فروش بلیت
می‌تواند باعث شود ارائه‌دهنده خدمات از سیستم مالی و دلاری آمریکا کنار گذاشته شود. او گفت آمریکا شبکه‌های تسهیل‌کننده انتقال پول به ایران را شناسایی کرده و در حال متوقف کردن فعالیت آنهاست. تاکنون
سه بانک
نیز هدف قرار گرفته‌اند؛ از جمله
شعبه دبی دومین بانک بزرگ مصر
که به گفته او بیش از
۱.۸ میلیارد دلار
به حکومت ایران منتقل کرده، یک بانک ترکیه‌ای و شعبه‌های خارجی
دومین بانک بزرگ روسیه
. این شعبه‌ها تعطیل خواهند شد. درباره چین نیز وزیر خزانه‌داری آمریکا گفت واشنگتن با کشورهای مختلف در حال انجام
گفت‌وگوهای محرمانه و پشت‌صحنه
است و در بسیاری موارد این روش را بهتر از رویارویی علنی می‌داند.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/23720" target="_blank">📅 20:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رویترز: حوثی‌ها امروز تلاش کرده‌اند ارتفاعات راهبردی یمن را تصرف کنند تا ارتباط مناطق ساحلی دریای سرخ با بخش‌های باقی‌مانده تحت کنترل دولت یمن را قطع کنند. این تحرکات همزمان با گزارش‌ها درباره خودداری ترامپ از حمله مستقیم به حوثی‌هاست.
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/23719" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آسوشیتدپرس: یک مقام ارشد حوثی امروز هشدار داد کشورهایی که در عملیات عربستان علیه حوثی‌ها مشارکت کنند، ممکن است هدف حملات قرار گیرند و گفت این گروه فعلاً قصد حمله به کشتی‌های آمریکایی را ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/23718" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnLn_1B1SEEZw0tqzR_PGH8NrvvTuRg9dsgSoUJJurt8XgG1IfehR0uSqGWW2CgvlrKyuDie7p7cDCpDZi5BgtC72GaHs_aF1AUsy2e82zI60k8QIrP4v8JyMju8Ut9xuShJXV2lPYeJmaum1fHGQCyxb7zYt5NLS73cq3lyuV0AEGsfLn0wC2L_I62N6zMxDKwroJDu57W8fwK0pClTdTZpzp95egCxdyRGFAEdxUxie_AFVf2cjq2iqDCfCLebDrPVmZoJy2TJ4Mr6Q9lkuoBGnHq1pAYZhoHa-zBO6yMEtYSxy1mX8NTbA1QO4WH27G1mc96rF-ch4KwNtcdt1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تنگه ۷ سوخترسان ۱ پهپاد و پی۸
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/23717" target="_blank">📅 19:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQd0VOt1H7W3kyq9p_MtFQ5uamKlW9Mzpcyvh5jcYmIX-Eb80_og4QIUjt4xG1I9evgkUb6GwMCxg9q7itKyUyiRaeeTnvny6hfB6Rwt1VRoWIyGgEuvS9mFt3XCnaLsuMFlCwHxJ-OBcrjC7d93z4vzGFs-ZK5GlbyHDIWrFGOkzRsvdY9Nqk2RYYiVS1hH3ddPXzzYzCIK_SgVtzryBsBY2SvmEE_PTK3Rnl1LEsTi3pQ7F5nsBKcBkEr5ApROjfEk5hyQYf5nunjABeOTkqZ93d5qxyBQeGhzX-1Z2X8p_xLAukn6Vm9cvR0XHnfzcQb18KHALiPwKfbgCWFRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش حامل گاز مایع (LPG) هنگام عبور از خروجی تنگه هرمز، بر اثر اصابت بقایای پرتابه‌های ناشناس آسیب دیده است. طبق گزارش فرمانده کشتی، تمام خدمه در سلامت هستند و هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است. نفتکش به مسیر خود به سمت بندر مقصد ادامه خواهد داد و مقام‌ها در حال بررسی این حادثه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/23716" target="_blank">📅 19:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM_bwRBS0f3TvkRewbMdEfAqCalBdIx9Ks-nL7TRVmcTegZASEq8KWsTS2Uqm8zkJutWG3x6AGcM-JZWJ_dOimERlQ3wdd1tpKfH0-NMJYRyAA-ggf3JdH_ukijIPCDF_Yfu-nIjnZTQswfKMKFQm9Cn2lXToEOJQtzDPfQulmjqnBm_1ZV8Fu0itfbU5tccV7J1g2lJtvvrbi1SlffnzZZ-nmAXUJV6md4Ef3zvSi6AkG82O5cucB9Xz7RpuuUJHqye6SFet029cO9F73e8O0kU7lXXmKXzYMud1vbjwIRO98PosTjueMtS7z4hF-VfXNq-XXkaaol7Cm_YxMEp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، با انتقاد از هشدارها درباره خطرات هوش مصنوعی گفت: «همان افرادی که می‌گفتند به‌دلیل گرمایش جهانی تا ۱۲ سال دیگر همه ما خواهیم مرد، حالا می‌گویند هوش مصنوعی ما را خواهد کشت و ربات‌ها به ما حمله خواهند کرد و همه‌چیز یک فاجعه است.» ترامپ با رد این نگرانی‌ها درباره هوش مصنوعی گفت: «هرکس هوش مصنوعی را ببرد، برنده است! ما اکنون از چین و همه دیگران جلوتر هستیم و من می‌خواهم همین‌طور باقی بماند.» او افزود که نمی‌خواهد رشد هوش مصنوعی را محدود کند و معتقد است این فناوری می‌تواند از انقلاب صنعتی یا حتی خود اینترنت بزرگ‌تر باشد. ترامپ در عین حال گفت آمریکا مراقب خواهد بود و وزارت دادگستری و سایر نهادهای اجرای قانون در صورت لزوم مداخله خواهند کرد، اما او همچنان از هوش مصنوعی و «ابرهوش» حمایت خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/23715" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibMPr7GQxBcDnD9lBfpz59xUbylCcvsJtuRLvQAaba8fxrJKuJ8xnTr6m02-hh3qWlcmpXkhLOa_2Z2il127ON_2dMlZjpMMfKUnyJkhVNtvB8dGveRpjol6A3B-ZAVWiJBHrANPOytv5N3X3DeNFMi_d8u-e5wfo_a7HOc78BDVIp--TUyfsXI_kaVBlQyqxw8cqi2FIfUKKsHYkFO1oCuE5AdvE90iB_2M-iW29hN1WVF8IRkdJk5mkk09ehQ0AG5m_2cieOcJnpAN9FVeBH12FigpMNq4FrLHWNWbW9nqwAwi-d3MkzrJjNTSTvbf6WYiuAGkPTgoIPchvScRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای نشان می‌دهند دست‌کم ۲۵ هواپیمای سوخت‌رسان آمریکایی اکنون در پایگاه هوایی العدید قطر مستقر هستند؛ این بزرگ‌ترین حضور تانکرهای آمریکایی در این پایگاه از زمان آغاز جنگ با جمهوری اسلامی در فوریه عنوان شده است. این تانکرها در اوایل درگیری به‌دلیل تهدیدات موشکی سپاه پاسداران از منطقه عقب‌نشینی کرده بودند و از حدود ژوئن روند بازگشت آنها آغاز شد. هواپیماها به‌صورت پراکنده در پایگاه پارک شده‌اند؛ وضعیتی متفاوت با استقرار متراکم تانکرها در پایگاه هوایی پرنس سلطان عربستان که می‌تواند نشان‌دهنده تداوم تدابیر احتیاطی در برابر حملات احتمالی ایران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/23714" target="_blank">📅 19:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سنتکام: نیروهای آمریکا در چارچوب محاصره بنادر ایران، مسیر ۱۰۹ کشتی تجاری را تغییر داده‌اند. این آمار نسبت به آخرین به‌روزرسانی سنتکام در روز جمعه، ۴ کشتی افزایش یافته است. @WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/23713" target="_blank">📅 19:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فارس: برخی از کشورهای منطقه با هدایت عربستان در تلاش هستند که با فشار به فیفا، فوتبال ایران را در آستانه جام ملت‌های آسیا تعلیق کنند.
مانند کاری‌ که با روسیه پیشتر انجام شد
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/23712" target="_blank">📅 18:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23711">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17908a60d.mp4?token=hEquQvc9pZIcZk0kNmJpRm2LTe_6lFZFq8ZL4GNPsRsCTEHNRAXPTE-FXnivu7KoIZjShovkkSjI9BxuVGcVzgJIo-98YCT5oIr-55xgRIF9eLyHbDngSgErRIqsOTZdGXYwFphwrIGw9WwcLehqdiDuBX1q9ef9yf-PAt4nBiyFWl5rxddzyc-46M-jnWWZJgC5dsE4QYXYE2M6GgDhrzLAYSKBKTd70fyPC8KLl6q29a9Lm4VRdujTt8B64df9iRYFDOUz4JLDtM3oQnX83-lucs6huuZa7JqWrb0s9qdKv-L-XaVJi978dhUhtf_AfsZ4qt5ieu0IYZ_xcC7DJ6rlzPdQOf-_uXXZ7cZ48mIjbtnRtLQPZ7iOD4ruv9DivO5uuZFzr5EwZZU1Xyr8qx70F-mJ7l0PaCRJVGBKs49Npsn2reo1NOJp35j_8Mk9Eo0AH9ODtFhoYJaA5Ray3MbNEElBQdiX4GIuEVntCwi4I6eXZk8B-GFR1Ej7HS-PLv-2UuvxKNcrJr_uchqtRv3_7uJMKFH9i5kLfljDMgkf__a5TmAgyfYzEgc1TJS4hdCbJhFxruz7p_0aIzpr2wuQT6UnbgzYxu3f2-W-C7sEVI_2Di1QxujMmh-TIsOYiNl4bNZGX8dk_AUGjr8t0Jh4q8MhTdj34K_JOEqrhec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17908a60d.mp4?token=hEquQvc9pZIcZk0kNmJpRm2LTe_6lFZFq8ZL4GNPsRsCTEHNRAXPTE-FXnivu7KoIZjShovkkSjI9BxuVGcVzgJIo-98YCT5oIr-55xgRIF9eLyHbDngSgErRIqsOTZdGXYwFphwrIGw9WwcLehqdiDuBX1q9ef9yf-PAt4nBiyFWl5rxddzyc-46M-jnWWZJgC5dsE4QYXYE2M6GgDhrzLAYSKBKTd70fyPC8KLl6q29a9Lm4VRdujTt8B64df9iRYFDOUz4JLDtM3oQnX83-lucs6huuZa7JqWrb0s9qdKv-L-XaVJi978dhUhtf_AfsZ4qt5ieu0IYZ_xcC7DJ6rlzPdQOf-_uXXZ7cZ48mIjbtnRtLQPZ7iOD4ruv9DivO5uuZFzr5EwZZU1Xyr8qx70F-mJ7l0PaCRJVGBKs49Npsn2reo1NOJp35j_8Mk9Eo0AH9ODtFhoYJaA5Ray3MbNEElBQdiX4GIuEVntCwi4I6eXZk8B-GFR1Ej7HS-PLv-2UuvxKNcrJr_uchqtRv3_7uJMKFH9i5kLfljDMgkf__a5TmAgyfYzEgc1TJS4hdCbJhFxruz7p_0aIzpr2wuQT6UnbgzYxu3f2-W-C7sEVI_2Di1QxujMmh-TIsOYiNl4bNZGX8dk_AUGjr8t0Jh4q8MhTdj34K_JOEqrhec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره افزایش قیمت بنزین گفت: «کاملاً آگاهیم که به‌دلیل اقدامات ایران علیه کشتیرانی بین‌المللی، قیمت انرژی افزایش یافته است.» او افزود: «هر کاری بتوانیم برای کاهش این قیمت‌ها انجام می‌دهیم و در عین حال تلاش می‌کنیم در این دوره فشار بر مردم آمریکا را کاهش دهیم.» ونس همچنین گفت یکی از پیشنهادهای مطرح‌شده از سوی ترامپ، تشویق ایالت‌ها به کاهش یا تعلیق مالیات بنزین برای کمک به مردم آمریکاست
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/23711" target="_blank">📅 18:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
زلنسکی
:
اوکراین و روسیه حمله به تأسیسات انرژی و زیرساخت‌های حیاتی یکدیگر را متوقف کنند
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/23710" target="_blank">📅 18:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6244aa6423.mp4?token=PqIomLpCgdE1qIZjvm4uZRajvNyH1qMO_41YbbNlKJu4RsPNKGgFO-vYvl15pcySHRWJdpdcC5AMur-Q66P4l_Y0Vd1eclcrKdsZZx-bDKZEiwNIwbhVbr0_gfQi_Z1SO0HBHN-_aEy22KlHYFJNH5gzEQjf_bsSZWBak6ku30sJ73i_d3ht6cqYrIR6jSgo63iEJq3Zibd_voB1tjFj5Ujn0Sem_FKxOvpIyMAH72tqAPMM0Nma5AL1_DrGDptYJKuml-ie2ihtp7pkPXi_8-4YKRC-836cPv-bqTCahWIjKGb9cEO4HkNm2Na8HJ5UXrE1R3ncTaMTYYQs_SgimQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6244aa6423.mp4?token=PqIomLpCgdE1qIZjvm4uZRajvNyH1qMO_41YbbNlKJu4RsPNKGgFO-vYvl15pcySHRWJdpdcC5AMur-Q66P4l_Y0Vd1eclcrKdsZZx-bDKZEiwNIwbhVbr0_gfQi_Z1SO0HBHN-_aEy22KlHYFJNH5gzEQjf_bsSZWBak6ku30sJ73i_d3ht6cqYrIR6jSgo63iEJq3Zibd_voB1tjFj5Ujn0Sem_FKxOvpIyMAH72tqAPMM0Nma5AL1_DrGDptYJKuml-ie2ihtp7pkPXi_8-4YKRC-836cPv-bqTCahWIjKGb9cEO4HkNm2Na8HJ5UXrE1R3ncTaMTYYQs_SgimQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس:
ترامپ رسانه‌ها را تحریم نمی‌کند؛ او می‌گوید: «اگر در آنچه عملاً تبلیغات است مشارکت کنید، به شما دسترسی ویژه به کاخ سفید نخواهیم داد.»
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23709" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f489a66f.mp4?token=ga50WqhudBMewoNPb3Tq1n2b2AvROJcPCDh1phaK7ZTJjq5dH1vRbkwew9tGInNir2Iduz_31jPIU9wnlwK5c88lUf10xDzJpM0uw_X36XKkwwn2FME2fhTAv_xS2-l4kUXjGXDGUHzsEtUs2l8ZXzRCDhLRsPG9Dtehsz9TWj0CkvyL3Chg36KADJ1i-h1ma2xuAduST_vZ0vjvMlSXGOi6poXwjsqGfXPR25eMIvr8UAlZTPketzL_as-AN-c6k9KzTw5sOmF42e9FDoiAGH9PY8vM30Q5pvsCWgemotIx0ar1Gs0aFIZtpEL9PYiMzG-HxQUYvN752dGnwn83yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f489a66f.mp4?token=ga50WqhudBMewoNPb3Tq1n2b2AvROJcPCDh1phaK7ZTJjq5dH1vRbkwew9tGInNir2Iduz_31jPIU9wnlwK5c88lUf10xDzJpM0uw_X36XKkwwn2FME2fhTAv_xS2-l4kUXjGXDGUHzsEtUs2l8ZXzRCDhLRsPG9Dtehsz9TWj0CkvyL3Chg36KADJ1i-h1ma2xuAduST_vZ0vjvMlSXGOi6poXwjsqGfXPR25eMIvr8UAlZTPketzL_as-AN-c6k9KzTw5sOmF42e9FDoiAGH9PY8vM30Q5pvsCWgemotIx0ar1Gs0aFIZtpEL9PYiMzG-HxQUYvN752dGnwn83yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس معاون ترامپ درباره ایران:
ترامپ گفت ایران نباید به سلاح هسته‌ای دست پیدا کند و برای اطمینان از این موضوع اقدام کرد.
ایران هم در پاسخ، حمل‌ونقل دریایی بین‌المللی را هدف اقدامات خود قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23708" target="_blank">📅 18:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پنتاگون ۶ فایل جدید از یو اف او ها را منتشر کرد. در فایل اول که مکانی در خاورمیانه است و در یکم ژانویه 2025 فیلمبرداری شده، دقیقاً مانند بشقاب پرندهی است که دیشب مشاهده شده
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23707" target="_blank">📅 16:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ارتش اسرائیل: آژیرهایی که در منطقه المالیه در الجلیل علیا به صدا درآمدند، نتیجه یک تشخیص اشتباه بود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23706" target="_blank">📅 16:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سازمان بین‌المللی مهاجرت: در طول چند هفته گذشته، حدود ۱۳۰ هزار نفر در یمن آواره شده‌اند، این در حالی است که ناامنی‌ها در این کشور رو به افزایش است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23705" target="_blank">📅 16:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: تمام ایرلاین‌های باقی‌مانده ایران تحریم شدند. وزارت خزانه‌داری آمریکا اعلام کرده ۲۷ ایرلاین ایرانی در فهرست تحریم‌ها قرار گرفته‌اند و از ۱ مهر (۲۳ سپتامبر) مجوزهای مرتبط با فعالیت‌های هوانوردی ایران نیز پایان می‌یابد؛ اقدامی که عملاً تمام خطوط هوایی ایران در سراسر جهان را تعطیل خواهند کرد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23704" target="_blank">📅 16:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کلیه مدارس استان هرمزگان تا دوماه آینده غیرحضوری شد بر اساس مصوبه شورای تأمین استان هرمزگان کلیه مدارس استان هرمزگان تا دوماه آینده به صورت غیرحضوری برگزار خواهد شد @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23703" target="_blank">📅 15:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کلیه مدارس استان هرمزگان تا دوماه آینده غیرحضوری شد
بر اساس مصوبه شورای تأمین استان هرمزگان کلیه مدارس استان هرمزگان تا دوماه آینده به صورت غیرحضوری برگزار خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23702" target="_blank">📅 15:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX54RiQI3J_k85xWm5TIngOBe3CPxF6FHqXJKPdikTy17lYFyOTOTX72DQsvtx_pT2U4HTDn6eZLR891yoSZG_La0I4j8GB1Mxw2YwncZPJXlNz4wXcabB91CQZZ6LCA5Qd-s0TW3MZ412PkCFNgR5OOMRWdGxerEi1jFwqi5LTjT_fzOmUGrq03JdVkRDPwJ5umF2oPLB5AJf4iYPQ8biX4OjHLB6TAXCGiQ8mNP3P7bEVWYCVmXqAFDdwrQahs_rH0pxTUFXRLxejlWPpBipaSVm1pcO5ndSJo1Uws4tYlgNWSc9v3gr3bhDyi4ChgYBcQz95g_m2oo4KzVuG5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : «روسیه متأسفانه به دلیل جنگ با اوکراین کنترل صنعت گازوئیل خود را از دست داده است. تعداد زیادی از پالایشگاه‌های گازوئیل آنها هدف حمله قرار گرفته و دست‌کم به‌طور موقت از فعالیت خارج شده‌اند. این جنگ مضحک و بی‌پایان با اوکراین باید پایان یابد. تمام جهان در حال متحمل شدن هزینه‌های آن است، چرا که هر ماه حدود
۲۵ هزار نفر، که بیشترشان سرباز هستند، کشته می‌شوند.
چه تأسف‌بار است!»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23701" target="_blank">📅 15:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نیروهای دولتی یمن : 5 حمله هوایی را علیه مواضع گروه حوثی در جبهه الاحکوم در منطقه حیفان، جنوب تعز، انجام دادیم همچنین یک پهپاد متعلق به حوثی ها را هم در کوه جرداد، جنوب غربی تعز، سرنگون کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23700" target="_blank">📅 15:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23699">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پست جدید پرزیدنت ترامپ دیس به خبرگزاری هایی که اجازه ورودشون‌به کاخ سفید رو نداده @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23699" target="_blank">📅 15:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23698">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیرانوند دماغ به دلیل خالکوبی خواستار بررسی معافیت سربازی به دلیل اعصاب و روان شد. خالکوبی به تنهایی دلیل معافیت نیست، اما در صورت تشخیص پزشکان مبنی بر این که خالکوبی نشانه مشکلات اعصاب و روان است، امکان معافیت وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23698" target="_blank">📅 14:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کرملین : روسیه هیچ اختلاف نظر با کشورهای اروپایی ندارد که بتواند منبع درگیری شود
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23697" target="_blank">📅 13:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eba0f5326.mp4?token=imkmw505_xwtr4Ac6vUqMVzAWtmU_EoPr463vYdAbpOthZ8y5u_FFyMzw58gK4u8iEvzsLm01MjMJ2WRm_9EfMij0eE7GwY0smLPR91NCZes5WgewwHKE0vMgKYzCZvAJwsOY-NDrt_uEeYjNhJdgoT9uX1ZzrTzGSEwA3HdVPWkcoxA8a2NoQy8NFm9DDc_j3Id1gXY3NRtribYvKTn2zhw_JVPSuuE_w31uDoRV66Bq0qDTN2yN3VZP3yRQVO_pNn9f93SgFanY-0eg0BAkXG3Qfv8G9SXvpoPRTV069t_STSdQUm8KfI_ElRSlPe8MEaLZ2VxXNcvmSmO7rPMqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eba0f5326.mp4?token=imkmw505_xwtr4Ac6vUqMVzAWtmU_EoPr463vYdAbpOthZ8y5u_FFyMzw58gK4u8iEvzsLm01MjMJ2WRm_9EfMij0eE7GwY0smLPR91NCZes5WgewwHKE0vMgKYzCZvAJwsOY-NDrt_uEeYjNhJdgoT9uX1ZzrTzGSEwA3HdVPWkcoxA8a2NoQy8NFm9DDc_j3Id1gXY3NRtribYvKTn2zhw_JVPSuuE_w31uDoRV66Bq0qDTN2yN3VZP3yRQVO_pNn9f93SgFanY-0eg0BAkXG3Qfv8G9SXvpoPRTV069t_STSdQUm8KfI_ElRSlPe8MEaLZ2VxXNcvmSmO7rPMqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت موبایل یک پاکبان در مشهد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23696" target="_blank">📅 13:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جماران:
آمریکا برای
هیچ‌یک از اعضای تیم رسانه‌ای همراه مسعود پزشکیان
جهت حضور در مجمع عمومی سازمان ملل در نیویورک ویزا صادر نکرده است. مدیرکل تولیدات رسانه‌ای دفتر رئیس‌جمهور گفت قرار بود یک تیم رسانه‌ای کوچک برای پوشش سفر پزشکیان اعزام شود، اما با صادر نشدن ویزا،
هیچ‌یک از اعضای تیم رسانه‌ای رئیس‌جمهور نمی‌توانند او را در این سفر همراهی کنند.
آسوشیتدپرس تأیید کرده که برای پزشکیان، عباس عراقچی و کارکنان ضروری هیئت ایرانی ویزا صادر شده
و هیئت ایران امسال با تعداد کمتری از اعضا در نیویورک حضور خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23695" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قطر ایرویز
به‌دلیل
جنگ ایران و افزایش قیمت سوخت
، شماری از پروازهای کم‌سود خود را به حالت تعلیق درآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23694" target="_blank">📅 13:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpNxjgwNliWoAgjp7mq6hgsNJHS7PVW1cwM5l83zTm4S9RJYaFryMY-pBbzbaiRfbmRpj9fyyKK8VpWrftO8XP5iGiu4Sg825DQbSfZqTGs117DNw0wFBE0G1LHix8pJP6qMRKhkJDwHTfOgtNcCmTf1LSCi4g7ovityo4ZF7aRi8Ifpi3t0mn9gLnflS4LymeqD7ewIZ6h4iMRBZUKbv01XrQEwR2uarpht9CxHL8qN0RcFCyGTzE1aI7Oe-dbkVd-TNASMTGBk-GsrfiofQNOATgxzV_uaAJniSrZZ57uIbDGmL2ZqmaG4ffNaqdRAdVyTyBAIfNF65fcQhRXFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏هم اکنون آتش سوزی در میدان آرژانتین,  تهران
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23693" target="_blank">📅 13:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-2dpySzI2zSialPOBV4p4KrJwj4p4xQdcxnlamDTmL8rhobmWEs4Ck68O86CQ89H2r8arvcXES2HBxVdV8A2Y24TexHBnxcjphyI1h01rdmj0ALK-NvrealDrcizGdlg_Cy6TMG5RpM7d_4xVZ1kA6skIa5yQz9vuNucp6qSnbhm1IXYmf1vkq--pqq_Y_ZipcI3XFAUyibbJ2wGUzRP8FTDZPerOxKzWAR5_r0hqSCfbE1yxksN4mtLCkurLYZ6hH2eaBbkTCCGzUN9rgVE-R0p71M02pjymLlQ-kiF6k1nc5ucEOAfWAwKHi8K1GKf7O4OXcl2XmLyjHcUSKd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار ما دریاچه چیتگریم ی صدا اومد الان  پاشدم با این صحنه رو به رو شدم ی بوی باروتی هم پیچیده @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23692" target="_blank">📅 13:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23691">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پرتاب موشک از گرمدره ۸:۳۰ دقیقه صبح امروز @WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23691" target="_blank">📅 13:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">BTC 84,100$  @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23690" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23689">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ly6OXSBrk2tfmRTlxjQMEFiXjPuqSpTH135wamjr1HHMGBwv2k_FJwT08HdY_klPU_antoeXLOQFJYutyl1UAIp4dpOvBmfggr6ieYBpMcmdqm7nND0xQACORi8UcoL80gpMRw6aoIZYjaYXsXOSddyI6gW1x30W7-jmTfqbBLMtWTySpUuLEmq76og1RbgPKfekYnAK7nVs7xIV4Jjh_P5WPlyesrgAoZwYUwFM5IGfFkuI-y-C2owA76Cq9LhVJZMEwQcY2HUNl9J-l5pspp4TzI1qkSbgerfddXtKNHMh9YOGbel_O0rj9G0kdPv3B2WjEJHTVzvhBykXtvZwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) به نقل از مقامات نظامی گزارش داد که یک نفتکش در حال عبور به سمت داخل تنگه هرمز، هدف اصابت یک پرتابه ناشناس قرار گرفته است.
دو تن از خدمه دچار جراحات سطحی شدند، اما شناور همچنان با نیروی پیشران خود به حرکت به سوی بندر بعدی ادامه می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23689" target="_blank">📅 13:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23688">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23688" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق CIA:  اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت!! صدها هزار پناهنده افغان در ایران هستند و هرگز تابعیت ایران را نخواهند گرفت.ناامیدند و اسرائیلی‌ها همین افراد را استخدام کرده‌اند. این‌طور بود: «در این گوشه…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23687" target="_blank">📅 13:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یک شاخص مهم تکنیکال بیت‌کوین دوباره فعال شده است. گزارش امروز BeInCrypto می‌گوید بیت‌کوین برای نخستین بار طی ۴۵ هفته بالاتر از میانگین متحرک ۵۰هفته‌ای خود بسته شده؛ Galaxy این سیگنال را در چرخه‌های قبلی با کف‌های بازار مرتبط دانسته است، هرچند این به‌تنهایی…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23686" target="_blank">📅 12:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رویترز:
یک نفتکش عظیم حامل حدود
۲ میلیون بشکه نفت عراق
در نزدیکی فجیره در حال انتقال محموله خود به نفتکش دیگری دیده شده است؛ این یکی از روش‌هایی است که برای ادامه جابه‌جایی نفت در شرایط اختلال تردد در هرمز استفاده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23685" target="_blank">📅 12:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">استنفورد:
پژوهشگران پزشکی استنفورد روشی ساخته‌اند که در آن
مقالات علمی به عامل‌های هوش مصنوعی زنده تبدیل می‌شوند و این عامل‌ها می‌توانند با یکدیگر گفت‌وگو کرده و فرضیه‌های جدید علمی تولید کنند.
این پروژه برای استفاده از AI در کشف علمی طراحی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23684" target="_blank">📅 12:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3147444cd0.mp4?token=uGo-yps8bEeGmvxAYPZgUnT0l7JDbUJl7ZRHQvXqniqGW6yYJisyqcCG92d5H2frhMlZRF0HbzMp8UwA_MGAomErVEgvyobhc3BYT0JL9SjjOKq2YU4t2UrfjWHOAEPFuIw1nNXsrE8TnoQhYs3vp5vwE0IUFFMXpEt6j9bXsLRpEfhKLUZSP5xGTS016tAHPT518N-vDY2mfpjSIqhp1fO7vyvTB5IZzQ41mzE2dJNKH0o8wpdyfpc8DyogxJdtcdkwjQ7LiyZml85fshCEGdEz7hVnsgs8tT930p4boIvcKHz9vQKPiVr4zgx4L9ewJ5FYYeX0FK-httBoH-C5YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3147444cd0.mp4?token=uGo-yps8bEeGmvxAYPZgUnT0l7JDbUJl7ZRHQvXqniqGW6yYJisyqcCG92d5H2frhMlZRF0HbzMp8UwA_MGAomErVEgvyobhc3BYT0JL9SjjOKq2YU4t2UrfjWHOAEPFuIw1nNXsrE8TnoQhYs3vp5vwE0IUFFMXpEt6j9bXsLRpEfhKLUZSP5xGTS016tAHPT518N-vDY2mfpjSIqhp1fO7vyvTB5IZzQ41mzE2dJNKH0o8wpdyfpc8DyogxJdtcdkwjQ7LiyZml85fshCEGdEz7hVnsgs8tT930p4boIvcKHz9vQKPiVr4zgx4L9ewJ5FYYeX0FK-httBoH-C5YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از گرمدره ۸:۳۰ دقیقه صبح امروز
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23683" target="_blank">📅 12:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">BTC 84,100$
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23682" target="_blank">📅 12:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e4ac1ec1.mp4?token=IVblGl-7UVwzsXM8wVADTD_L8p4tPk6KEzCjFUeTdMxUscfdFdQZqal2R4MwRE_yBC7UqMtZJq7_2Xv6_IgIqwF2bGgD5LLLC-VTG6qvHvHhmM2UIcp2RYwT7_n5cNfMKsNgdxAnC1_q_zlj8OcJESC2ppusutszK3Wzwe4an9L7_h46XYVvMaNQiF7Qh_Q2LSmgcVeqbl4n77KiXh5_FBa12bI1l4ypzlPp7jKe-fApfrx1lmNDuuo9v4wjc6fqhdIhO9nnfeYCDsral3OllGuxjAJShpFK6SdjeXS9pWV_vmfmnTP9yrvdPORUlwlA1DMl4C_FS0TCYy6VppeETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e4ac1ec1.mp4?token=IVblGl-7UVwzsXM8wVADTD_L8p4tPk6KEzCjFUeTdMxUscfdFdQZqal2R4MwRE_yBC7UqMtZJq7_2Xv6_IgIqwF2bGgD5LLLC-VTG6qvHvHhmM2UIcp2RYwT7_n5cNfMKsNgdxAnC1_q_zlj8OcJESC2ppusutszK3Wzwe4an9L7_h46XYVvMaNQiF7Qh_Q2LSmgcVeqbl4n77KiXh5_FBa12bI1l4ypzlPp7jKe-fApfrx1lmNDuuo9v4wjc6fqhdIhO9nnfeYCDsral3OllGuxjAJShpFK6SdjeXS9pWV_vmfmnTP9yrvdPORUlwlA1DMl4C_FS0TCYy6VppeETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی عجیب یک هم میهن از چسب محافظ پنجره در برابر انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23681" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e81b36f52.mp4?token=nBQjdASpTMb4KSLosmCKgLOdndIEZYz-C67twAXF5AnDSZW2Y1gdSYd9QoAaaybCVWsu4N42_PLBfuP4PgKqkuZuw1koJObSmM1LnUy_VmLESPn5zMbIvjSqtJGQ256F0XzuCRoqESk-l3wQ3Dcs2DCkDhX1VnSgVdh5ps_0tqjkaGVhM1p1d-N2Em2-FHUvk6-kUy1zzIkkuFMbe2xWI1dyX8cR6yUNqX6y6fXSGia4OHZ5Tl257CwjMMIPi3NO4IQjbMxn9tp8OCyrKAp3JlD6didRqiwCFpbiQFTPhEnAXjIEzWxJP556RuQ3bkSaq_zAp-lfGm1uLITGMlq0tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e81b36f52.mp4?token=nBQjdASpTMb4KSLosmCKgLOdndIEZYz-C67twAXF5AnDSZW2Y1gdSYd9QoAaaybCVWsu4N42_PLBfuP4PgKqkuZuw1koJObSmM1LnUy_VmLESPn5zMbIvjSqtJGQ256F0XzuCRoqESk-l3wQ3Dcs2DCkDhX1VnSgVdh5ps_0tqjkaGVhM1p1d-N2Em2-FHUvk6-kUy1zzIkkuFMbe2xWI1dyX8cR6yUNqX6y6fXSGia4OHZ5Tl257CwjMMIPi3NO4IQjbMxn9tp8OCyrKAp3JlD6didRqiwCFpbiQFTPhEnAXjIEzWxJP556RuQ3bkSaq_zAp-lfGm1uLITGMlq0tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق CIA:  اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت!!
صدها هزار پناهنده افغان در ایران هستند و هرگز تابعیت ایران را نخواهند گرفت.ناامیدند و اسرائیلی‌ها همین افراد را استخدام کرده‌اند. این‌طور بود: «در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار. اسرائیل هزاران نفر از این افراد را استخدام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23680" target="_blank">📅 11:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHyEszb8kT1o66aPzH2BC0z29WCGJrc7rTiVQoUaYubgHoN-O-Ggma1TjbGzT9szOAkmHuA75XA_pLv_AyuuvWXY_-jiEasPzLDZMH2D0KGiiGkbv5CWaGpqdO4zxjujRVdVyn4vieeJ87knJiAPuZta9-pSTPIaykdEJPfwPG6T_cj2xebKPV_oPX3weFQ881pyKAWTlgZ5kvN94OyfkJ2wk_Qgyt21UcddHZ0Zc49RS_YvJZ8zEv9nsAnOC1KELGIZPvujnSEb-pi27xH36NgbB447UsYK8yav-z4nFEMzw9m6MIzGXcgkBgewCbv6jPjuPpdbRsGXUvR1LzKUgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بهترین فیلم‌هایی که در طول بیست سال تحقیق و جستجوی من در مورد فرازمینی‌ها دیدم، مخصوصاً این‌که در ایران است. هم اکنون توسط دیدبان اتاق جنگ با یاشار در اتوبان آزادگان گرفته شد @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23679" target="_blank">📅 10:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23678">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فایننشال‌تایمز:
اسکات بسنت، وزیر خزانه‌داری آمریکا، و
هه لی‌فنگ، معاون نخست‌وزیر چین
، روز یکشنبه در نیویورک حدود
۸ ساعت
مذاکره کردند. محور اصلی گفت‌وگوها
تجارت، تعرفه‌ها، هوش مصنوعی و مواد معدنی حیاتی و عناصر خاکی کمیاب
بود و دو طرف درباره ایجاد کانال گفت‌وگو درباره هوش مصنوعی نیز به تفاهم‌هایی رسیدند. در این مذاکرات، نگرانی‌های آمریکا درباره
حمایت احتمالی چین از ایران
نیز مطرح شد؛ از جمله ادعای استفاده از تصاویر ماهواره‌ای برای کمک به هدف‌گیری مواضع آمریکا.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23678" target="_blank">📅 10:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23677">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیویورک‌تایمز:
ترامپ در آخرین لحظات تصمیم گرفت حملات آمریکا علیه حوثی‌ها در یمن را آغاز نکند؛ این در حالی بود که پنتاگون از قبل برای عملیات آماده شده بود. پس از درخواست
محمد بن سلمان، ولیعهد عربستان سعودی
، ترامپ به پنتاگون دستور آماده‌سازی حملات هوایی را داد، اما تا روز یکشنبه بار دیگر از تصمیم خود عقب‌نشینی کرد. به گزارش نیویورک‌تایمز،
فهرست اهداف تأیید شده و بمب‌ها در حال بارگیری روی جنگنده‌های آمریکایی بود و حملات تقریباً آماده آغاز بودند
که ترامپ دستور توقف عملیات را صادر کرد. همچنین بیشتر افراد نزدیک به ترامپ نسبت به ورود آمریکا به جنگ عربستان با حوثی‌ها تردید داشتند یا مخالف آن بودند، به‌ویژه با توجه به فشارهای نظامی آمریکا در جنگ با ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23677" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23676">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سخنگوی سپاه گفت
جنگ تمام نشده و سپاه برای یک جنگ طولانی‌مدت آماده است
. سردار محبی همچنین گفت در صورت حمله جدید، ایران «جغرافیای جنگ را تغییر خواهد داد» و از رونمایی سلاح‌های جدید سخن گفت.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23676" target="_blank">📅 09:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQwM5KnyPuXO4ttIWTbiB1YHKh8tf2-dXBUTAuKyTBhWtsyniKvxuRI8XNy8o3r19Ta70jbvhHxDJz5OfWMJ4xqtWx5g-0AGBVOBrkD19VGIXdncgcxE-cr785vVoupuHBRCSEYVUcRGSxQz-WBuQsBukV5aPw00bILyGa-zUz7nY2hLsixI6dBHVGKIe_DNBRqxfYKX1RNpYTxyQ25FMB-jOBo4xSAZGY98vmHkaZ1laKvLzYwbpaky9qiyBvlXoBfd1J1yv2v5o7vDNZrlVANoM-6G2kgRGgp-yCfMZ1gkDtjNzHzwtw2u9URv2PIu-qM7kcOezq4uxRzsflhDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث
:
«قیمت بنزین در دوران
بایدن
بسیار بالاتر از دوران
ترامپ
بود. تقریباً
قیمت همه کالاهای دیگر
نیز همین‌طور بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23675" target="_blank">📅 09:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بیت‌کوین دوباره از ۸۱ هزار دلار عبور کرد. قیمت BTC در معاملات امروز تا حدود ۸۱٬۸۰۰ دلار بالا رفت و در ۲۴ ساعت حدود ۱.۴ درصد رشد داشت؛ در یک هفته نیز حدود ۵ درصد افزایش ثبت کرده است. @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23674" target="_blank">📅 09:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بیت‌کوین دوباره از ۸۱ هزار دلار عبور کرد.
قیمت BTC در معاملات امروز تا حدود
۸۱٬۸۰۰ دلار
بالا رفت و در ۲۴ ساعت حدود ۱.۴ درصد رشد داشت؛ در یک هفته نیز حدود ۵ درصد افزایش ثبت کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23673" target="_blank">📅 09:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اروپا امروز ۳.۳ میلیارد یورو کمک دفاعی جدید برای اوکراین اختصاص می‌دهد.
این بسته از سوی کمیسیون اروپا پرداخت می‌شود و در چارچوب حمایت دفاعی اتحادیه اروپا از اوکراین است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/23672" target="_blank">📅 09:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23671">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رویترز : با باز شدن بازار نفت برنت در معاملات آسیایی حدود
۱۰۲.۰۸ دلار
و نفت آمریکا حدود
۹۸.۵۳ دلار
بود؛ بازار بین افزایش عرضه خلیج فارس و ریسک هرمز در نوسان است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23671" target="_blank">📅 09:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23670">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تشدید تنش میان کابل و اسلام‌آباد؛ جمهوری اسلامی پیشنهاد داد میانجی شود
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/23670" target="_blank">📅 04:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23669">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/23669" target="_blank">📅 03:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23668">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش های بسیار شهر‌ری شیشه‌ها لرزید و انگار زازله اومد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/23668" target="_blank">📅 03:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23665">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4130309e48.mp4?token=YhKYi4n4AmYqlwbEkCgLI2lY7Q9LcIw2DA3uwEhPcy_zon8HUuJo9PLj8Md1EiMEuES-gqRG8t9ZdD47iEfhsGVFLfD2rX0TFxy28NkqQlmPBVEnEnbYzWtHcaJWJ3cXkf474fBlkUCvLtcsvv4T257ywd2ETUD758Up5ySt0tFT_U7A4spaO6F8cKvpiSEINba4Bu0mPHc6Au6LppxmeCtiN5mnH-bpPMatVX_fQX5mPYJ3oagTDBZ0GCmdF_jSlNs1Nq8ieOjc4hszoMpIvouXYNT97oqEm1RtUhg2wydGe3o-M_y9v_RrpGA733MGDeiu2K-6a5w4ghNmfUr19A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4130309e48.mp4?token=YhKYi4n4AmYqlwbEkCgLI2lY7Q9LcIw2DA3uwEhPcy_zon8HUuJo9PLj8Md1EiMEuES-gqRG8t9ZdD47iEfhsGVFLfD2rX0TFxy28NkqQlmPBVEnEnbYzWtHcaJWJ3cXkf474fBlkUCvLtcsvv4T257ywd2ETUD758Up5ySt0tFT_U7A4spaO6F8cKvpiSEINba4Bu0mPHc6Au6LppxmeCtiN5mnH-bpPMatVX_fQX5mPYJ3oagTDBZ0GCmdF_jSlNs1Nq8ieOjc4hszoMpIvouXYNT97oqEm1RtUhg2wydGe3o-M_y9v_RrpGA733MGDeiu2K-6a5w4ghNmfUr19A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار ما دریاچه چیتگریم ی صدا اومد الان  پاشدم با این صحنه رو به رو شدم ی بوی باروتی هم پیچیده
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/23665" target="_blank">📅 03:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23664">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f5195837.mp4?token=mRIewPXH0_8_R1Am9D-YNNYE5aEQfMz3sq-Kp1i5MSil9ahkp8-kjHBkDOPfSqjOQJ2MeBUW9OwELnC48uqVwA82D-hE2MFJmFd0DFWXK4bIeRn7ERDiSrsuLKqOXi7aO8g3fxsSmcyK1oYn-TMgFjsMfbsA00O_7rWtCTvJ6Z5cePogHgL2xKY0aoVXbqTqjlJzNllwsBFkRz_kpV781RZ3MeBc_xq5QkLIFTqp8lvGM6iDOcsWSwhmS3e-UbcyklgtRLKDhgnMrQOHGbMp8Hrx2o9mB-D_-HdXWOqJFUDnWIHcAds0P5WV2LoxQVCFswqgnexMyoiGJx7Oeuz3WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f5195837.mp4?token=mRIewPXH0_8_R1Am9D-YNNYE5aEQfMz3sq-Kp1i5MSil9ahkp8-kjHBkDOPfSqjOQJ2MeBUW9OwELnC48uqVwA82D-hE2MFJmFd0DFWXK4bIeRn7ERDiSrsuLKqOXi7aO8g3fxsSmcyK1oYn-TMgFjsMfbsA00O_7rWtCTvJ6Z5cePogHgL2xKY0aoVXbqTqjlJzNllwsBFkRz_kpV781RZ3MeBc_xq5QkLIFTqp8lvGM6iDOcsWSwhmS3e-UbcyklgtRLKDhgnMrQOHGbMp8Hrx2o9mB-D_-HdXWOqJFUDnWIHcAds0P5WV2LoxQVCFswqgnexMyoiGJx7Oeuz3WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : سمت چیتگر مسیر کرج به تهران همین الان
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/23664" target="_blank">📅 03:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امروز، ۳۰ شهریور، چهارمین سالگرد کشته‌شدن نیکا شاکرمی است.
نیکا، دختر ۱۶ ساله اهل خرم‌آباد، در جریان اعتراضات ۱۴۰۱ در تهران ناپدید شد و چند روز بعد پیکر او به خانواده‌اش تحویل داده شد. نام نیکا شاکرمی همچنان یکی از نمادهای اعتراضات  است
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/23663" target="_blank">📅 03:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23662">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/23662" target="_blank">📅 02:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نور های هواپیما چه معنایی دارند @WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/23661" target="_blank">📅 02:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKe8PZ3Ww3dr-GE9WbCVj5SH7qO22zSx9L9X6vlzRdOgodS-HQhMG2aWzGH4rHse87XBQuICLo6w8bAK2J_KNbQW-09_G6um0ctg57JQoNldZZ7lz9MZYDLWqKzFgrI83bBh8Ja_cYiHcxACeCfJJGECJDUDO2wV8KhDp68vGGhpXbO12aYGK8A62wfeYtyTGqY0XXXViVtGjgVXaKSZKxjJX7-uPdJ3doQL8yxqcEeJFKnOlVxKCGA8kG96tNRRrXADrV_VSEc6s96E-h_-wRpDXUUm0GQPB0rty467HF9VkHDlJr8RIPZ49f53_mnczNW60TmAQpQIeD95l8Ef5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمین های فیک بیسواد تلگرام این هواپیما رو جای یو اف او قالب کردن ملت
😂
😭
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/23660" target="_blank">📅 01:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23659">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd534fa54f.mp4?token=jzZ0Fa_6dscB_boXGfBR8MWJQ4c7dACx4UELoD7jbeTjkn0SBA80BkFCMBH5VL_diH3cZe_-0tKTy0Ng20Xj7Xj3tROJHeKRhuSAVKBfKvoRxa-sLpOOWwI6wCxNlHcJdtvvaRbV8oO24R6J_9fizK3bI8A3BRwTECqsy6S6nGcDe3epGOqJtLcE7enekNavs4o-C-ExyH53tLp6REXZlR_rZPgsucUr_MCkIbT2fEByeWGxPUHHHP9bYL479Jj08kCZdxfYfgKrjV2cw2yGrmb4XKTT9eEz6ik_hL_kXcsYNMB16IDlw1KP0aYtQ_lAid9oiEJx9JgHp6FVwOKZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd534fa54f.mp4?token=jzZ0Fa_6dscB_boXGfBR8MWJQ4c7dACx4UELoD7jbeTjkn0SBA80BkFCMBH5VL_diH3cZe_-0tKTy0Ng20Xj7Xj3tROJHeKRhuSAVKBfKvoRxa-sLpOOWwI6wCxNlHcJdtvvaRbV8oO24R6J_9fizK3bI8A3BRwTECqsy6S6nGcDe3epGOqJtLcE7enekNavs4o-C-ExyH53tLp6REXZlR_rZPgsucUr_MCkIbT2fEByeWGxPUHHHP9bYL479Jj08kCZdxfYfgKrjV2cw2yGrmb4XKTT9eEz6ik_hL_kXcsYNMB16IDlw1KP0aYtQ_lAid9oiEJx9JgHp6FVwOKZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادمین های فیک بیسواد تلگرام این هواپیما رو جای یو اف او قالب کردن ملت
😂
😭
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/23659" target="_blank">📅 01:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ارسالی : یه سوله کنار ‌ایران خودرو در آتش میسوزد
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/23658" target="_blank">📅 01:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش صدای انفجار/پرتاب ؟!؟ سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/23657" target="_blank">📅 00:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d06fec75.mp4?token=XeUWBrMHavjmw1BGQlVCAKeuYCk2seVYls23KEg0aohistk9c0R4aaM5QywJAcHC9sscOeFrGx4ruV7W9-E5MJPHsHZ51P_cQmHACKEjOXUR0bHWX9N_k5SObjnUL54VMS9gPiDxt0ZkXwY0qqGSgFbR8L9pqcSXbXRqy1t7mQ2yHuCZYk213wptX0W4LFwr4tagCXXi8AHzYLLtOR2fleS531A-tWxN-_p1EluIye4MfVHrK7Si3HGJgkuA0iT_fI10Rx6p_wZNipW0rVbaZ1i136Wk13NDfNoEN1MamuMJZey5KfAeRt6chxvXSsJWfGnZdpeJcTRz1GJ7gpfPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d06fec75.mp4?token=XeUWBrMHavjmw1BGQlVCAKeuYCk2seVYls23KEg0aohistk9c0R4aaM5QywJAcHC9sscOeFrGx4ruV7W9-E5MJPHsHZ51P_cQmHACKEjOXUR0bHWX9N_k5SObjnUL54VMS9gPiDxt0ZkXwY0qqGSgFbR8L9pqcSXbXRqy1t7mQ2yHuCZYk213wptX0W4LFwr4tagCXXi8AHzYLLtOR2fleS531A-tWxN-_p1EluIye4MfVHrK7Si3HGJgkuA0iT_fI10Rx6p_wZNipW0rVbaZ1i136Wk13NDfNoEN1MamuMJZey5KfAeRt6chxvXSsJWfGnZdpeJcTRz1GJ7gpfPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر تتلو 39 ساله شد، امیدوارم مشکلاتش حل بشه، جاش تو این روزا خالیه.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/23656" target="_blank">📅 00:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23655">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH-HvrADRtr2bhwQGsZBgLt6gU3y5N6OmT87Eb6JsFfcNQ7WDkvuiNGqtGQ_zh_HGuBvMcl1WF06oLn3yF32qbAMYdgS5WQ1tTF6kNhiQgaPKMdJPyeALH5waeZCaks8xeXfhpAnXo1lxob4RHVEZW358_03OPekyHM7rfwwVkSt_Q7xiPPljTalP_hPPvb5myewd8fB9lJaosggHq3HkrycQOtrW8H_H-ycs4pLXeBRwycSPLSPV_UoA1ylecR2Ytw-3cq4ZcdgajMcqS_v_xu31Hu568ZXjFsbfu9DJ90Juo4wdugMfe1a3PnTct3Qtk8kmEqMigFOmAhxKyymeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت سوخترسان آمریکایی و دو سوخترسان از کشورهای حوزه خلیج فارس هم اکنون در حال انجام مأموریت در آسمان منطقه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/23655" target="_blank">📅 00:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23654">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/23654" target="_blank">📅 23:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23653">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/23653" target="_blank">📅 23:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23652">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وال استریت جورنال به نقل از مقامات آمریکایی: دولت ترامپ در حال آماده‌سازی برای تحریم‌های گسترده علیه دادگاه کیفری بین‌المللی است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/23652" target="_blank">📅 23:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23651">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بر اساس گزارش نشریه "اکسیوس" به نقل از یک منبع آگاه، ترامپ بارها از زلنسکی درخواست کرده است تا حملات به پالایشگاه‌های نفت روسیه را متوقف کند، زیرا این حملات باعث افزایش قیمت جهانی گازوئیل می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/23651" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23650">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/23650" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23649">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fu7DyHEiviEJirJp6GGC0cMa_ULAd6q_kI12ArtQWd8Q_XsSJp3Ar2w-82J-EnbMNGKBKu_iZ9nKeOssB6nshjBpb36cbVyShKxjRmLTfHIog4dCZsdwm4_dmn-OLxyfrFgWm51gS6kN_ICTuGckP4qEFoCqrzRy6y1qmFb5NeqnhGq0JiHw5KHiqxQWc3uUkKwDxqXRQG16QSUYu-Lk61-fHjPsFvXA5ADcp5MOkdO4yBGH3pYszc_ibs0tRB8bA2hcpzCNno8NpbCMLH9XAkuQDbxQC68D_yE86aVZUZtH625CIMBsXyUIGiqeEyJ-mA3_sjBIqbRSeO6Mvbp_8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت آنلاین آمریکا در ایران از تمام شهروندان آمریکایی حاضر در خاورمیانه خواست برای احتمال لغو پروازها و بسته‌شدن حریم‌های هوایی آمادگی داشته باشن
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/23649" target="_blank">📅 23:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23648">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/23648" target="_blank">📅 23:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23647">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مستندی برگرفته از اسناد محرمانه ی ایالات متحده درباره ی رخدادهای شب بیست و ششم شهریور سال ۱۳۵۵.  به همراه مکالمات رادیویی واقعی از گفتگوی خلبان های نیروی هوایی ارتش ایران با برج مراقبت و مرکز فرماندهی.ماجرا از این قرار است که شبی آرام در اواخر شهریور ماه حوالی ساعت 10 شب تلفن برج مراقبت فرودگاه مهرآباد به صدا در می آید و حسین پیروزی 35 ساله مسئول برج گوشی را بر می دارد. پشت خط خانمی با صدای نگران خبر از رویت چیزی عجیب با پره هایی شبیه پروانه های اتومبیل در آسمان می دهد...
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/23647" target="_blank">📅 23:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23646">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNiXvS8K2ifM32xV3o5sLU8S0utdXx5zJLSFXOEz7gDMx6sZrV56bwNOXWGew2nWeAgz3HiTHc4MGESHEDt9zL8PU8_CAzyHPD4X8ZR5yf8xDMMR9g6u-3-RuKaz2O4lKp_fNryJFRX0X8rOSNxUbvcb2LTxn2TrH33ws-GU0KLxQ0I4hjzIWD883quZDjy75qX1bVsuosRNdYq_VDUZFh1rpw1XqbPtcDCkkWzggWfW9GRCPYmMs3d4rb0LQaAG3yH1HvItxdjDvSa8c3ut8ApnYjzKE_b9EtKb_45pTOUFT1Bi3iK6TQn9jkwSbm-NRdjftpHUra-RJ347qZ4tsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از بى نظير ترين عكس‌های بشقاب پرنده در جهان (پارک جنگلى تپه‌هاى عباس آباد تهران) قبل از انقلاب
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/23646" target="_blank">📅 22:45 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
