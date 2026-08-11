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
<img src="https://cdn4.telesco.pe/file/WhhBM6f7AkA7Y29iNqYOcm5u7-34VwaAw3uTeaz8iFB6shMOp7MkHoIINx8QghLj1j7sJw3rKpZATo5lFn8bwo7PKXa_eSTJQwf7Ae9-aP09ngCkYAuKfuX8t9LdonEv7EHIUk1jo4ZmOBVFaIQwiWOa5BSjs4IeHdjl3VHMc677p5FV_61ZRk2krC4RkTTzwbHvZ2FhAZSSE9ppHI5qrCSKTXsDefXZdtcEc5BKgRHFb_Q4TpoJY87-a2E1CzvzJ8WRdM0f_axdmeKv4aJBvy-RfEKveve4K5gAWFH77dLQNkU89r3ZyDrsc87cAPw2jE4Cab3FQSWZZAzH4xsDKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 18:20:19</div>
<hr>

<div class="tg-post" id="msg-20831">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یوآو کیش، وزیر آموزش اسرائیل:
صرف نظر از اینکه رئیس جمهور آمریکا چه کسی باشد، حتی پس از ترامپ,  اگر لازم باشد به تنهایی اقدام کنیم، به تنهایی اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/20831" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20830">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGaJqVfjWXd9j7NivqA6deJ6a3SD16p7C74px9C3jTcycgMuAMB84abPFsYoKA1fZ6yUhaQ_y7fFxDS0OTERiDvOZ2OPvlVfO4WDz-1mSY-scex6p9jB-IITFLJQkTxrdLInQXwtTnzlYktR-B61Gno57U8zM67gpYjS3ddpXm1Hgw2UGJSHzsylrKPjCDvsl3eB1cm8fLnDXV0b3YNl6PUfd09iJP7tc6D-c0y6nSXfTH5zE7O1b0wscuwSJ2WRZpPURDJJb_keLsMtP-Y_SBsZ3laUXDKHQ2fy_D-Pxp5OzeToh7XmExP08IcFpC3OWJAYEBuTashqrbx3Q4ZCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه اسرائیل : ترکیه این جسارت را دارد که از اسرائیل انتقاد کند؛ اما واقعیت‌های میدانی چیست؟ هزاران سرباز ترکیه و ده‌ها پایگاه و موضع نظامی در سوریه، عراق و قبرس مستقر هستند. در حالی که تجاوز نظامی اردوغان مرزی نمی‌شناسد، ترکیه ۳۶ درصد از خاک قبرس، ۵ درصد از خاک سوریه و ۲ هزار کیلومتر مربع از خاک عراق را در اشغال خود دارد. در مقابل، اسرائیل به‌طور موقت تنها ۰.۱ درصد از خاک سوریه را در اختیار دارد؛ منطقه‌ای حائل که به گفته اسرائیل، برای حفاظت از شهروندانش در برابر تهدیدهای امنیتی اثبات‌شده ایجاد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/withyashar/20830" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20829">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به گزارش رسانه‌های اسرائیلی،
یوسی کوهن، رئیس پیشین موساد در نشست «مجمع جلیل» در شهر صفد گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک و شناسایی کنیم.»
او مشخص نکرد که این بازدیدها چه زمانی انجام شده یا دقیقا چه کسانی از این سایت بازدید کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/withyashar/20829" target="_blank">📅 17:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20823">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">روال هر روز پیج اینستاگرام در ۴ دقیقه ریکاوری شد
😁
عرضشی عر بزن
🤣</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/20823" target="_blank">📅 16:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20822">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8Y9WeNGQ14Os5rwFgbYG9h2H3S-NjQG_LpDfGbz2wLhrOfx6D4ZL0HhL6IJANFF5A8Oh7SC-ciQdM0Rd4iVzUjL4EVgGSEJD9GK_QjZDaj64N8ytVaMDIvsWnOE8gWew1FSq2pmnXgFEf9Ubm5tKumuZLb45C0wSI1UjZmuwACTei2llTEHFrH18tWULuwy66AcbJev76LXjCk9NpGWJStrRd1uZ6hyUCtj0lB5pg6hwptVtJmrlDqA5ucYhN9Jqf-JzZ5GkNJ1N5WtPGnZYQg5ELBdmEL0rZsOztn5RhGntS6YRZ5vygq1fzm6TYcmXdoXceTmXq9zfnt2hfdpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی بی دوزندهیاهو : آتش‌سوزی در کارخانه نخ اطراف بیدگنه،  ملارد
@WarRoom</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/20822" target="_blank">📅 16:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20821">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دبیر شورای عالی امنیت ملی ج.ا : ما در یکی از حساس‌ترین و سرنوشت‌سازترین مراحل تاریخ معاصر خود قرار داریم , در برابر تهدیدها، از حقوق خود و منافع ملت‌مان عقب‌نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/20821" target="_blank">📅 16:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20820">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وال استریت ژورنال : نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه. @WarRoom</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/20820" target="_blank">📅 16:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20819">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وال استریت ژورنال : نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/20819" target="_blank">📅 16:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20818">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزیر دفاع پاکستان به بلومبرگ:
نشانه‌های روزهای گذشته حاکی از آن است که به توافق صلح (یاشار: بمباران) نزدیک می‌شویم
@WarRoom</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/20818" target="_blank">📅 16:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20817">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">روال هر روز پیج اینستاگرام در ۴ دقیقه ریکاوری شد
😁
عرضشی عر بزن
🤣</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/20817" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20816">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آکسیوس
:
به گفته مقام‌های آمریکایی و اسرائیلی، دولت دونالد ترامپ در پشت‌پرده میان سوریه، اسرائیل و آژانس بین‌المللی انرژی اتمی برای خارج کردن مواد هسته‌ای از «سایت ۹۹» سوریه، مرتبط با برنامه هسته‌ای مخفی حکومت بشار اسد، توافق ایجاد کرد. این مواد شامل «کیک زرد» است که برای ساخت سلاح هسته‌ای کافی نیست، اما می‌تواند در بمب‌های رادیولوژیک به کار رود. اسرائیل پس از سقوط اسد با نگرانی از دسترسی به این مواد، ورودی‌های سایت را هدف قرار داده بود. عملیات انتقال هنوز انجام نشده، اما مقام‌های آمریکایی می‌گویند به‌زودی اجرا خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/20816" target="_blank">📅 15:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20815">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وال‌استریت ژورنال : خامنه‌ای با تغییر مقام‌های ارشد امنیتی بر ادامه تقابل با آمریکا تاکید دارد
@WarRoom</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/20815" target="_blank">📅 15:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20814">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش حمله موشکی به اردوگاه گروه‌های کورد در شمال شرقی اربیل
@WarRoom</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/20814" target="_blank">📅 15:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20813">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzM0AvsKTBU65iyzCJJpw3MosZqds3LBdNkj0zy83oOlRFXkbz99A0aqjDpwI9-Jo83mcJC0F_jffrpmPEEUOAi01ixbIDYOG_SMkdon0rVzsZWJvleAjvYmLwod8H_M_bb-M0bYlt4R1IlE7ATa8x9N_NinUvm9JMKg2G3kbNcxyaxTq6eZCx4rH-IbG90cwQ8O-Paf2jD50GZiQEdxvtWwGFKjZS1jxeZEIRUrSs71RWXJJwNQnEA8yfVq--4NWnniv24Q6d50RewpjzBxYePegS-YVq3EHCPGBPriIH0__B8jATjOfpkR3p8F7Yqsjcs22w8TFbY5oSZHsfNa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری رویترز، سازمان حمل و نقل دریایی بریتانیا (UKMTO) از حادثه‌ای در سواحل المخا، یمن مطلع شده است. گزارش شده است که یک کشتی باری در دریای سرخ جنوبی مورد اصابت یک موشک/پهپاد ناشناخته قرار گرفته و منجر به تلفات جانی شده است ، این در حالی است که یک کشتی سعودی صبح امروز مورد هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/20813" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20812">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سید محسن رضا نقوی، وزیر کشور پاکستان برای گفتگو با مقامات ایرانی وارد تهران شد.
@WarRoom</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/20812" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20811">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رسانه عبری : مجتبی خامنه‌ای، از احمد وحیدی، فرمانده کل سپاه پاسداران، خواست تا برای «عملیات تهاجمی قدرتمند علیه دشمن» آماده شود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/20811" target="_blank">📅 13:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20810">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ درباره ایران: ما سه راهبرد داریم , همین کاری را که الان انجام می‌دهیم ادامه دهیم؛ فقط به همین شکل پیش برویم و ببینیم اوضاعشان چقدر بد است، چون تورمشان ۳۰۰ درصد است. پولشان تقریباً هیچ ارزشی ندارد. حقوق سربازانشان را نمی‌دهند. سربازانشان در حال ترک خدمت هستند. بنابراین همین روند را ادامه دهیم، چون این وضعیت پایدار نیست.
خیلی، خیلی سخت به آنها ضربه بزنیم؛ یا در واقع، راه سوم این است که از نظر اقتصادی آنها را شکست دهیم. البته همین کار را همین حالا هم انجام می‌دهیم. این تا حدی بخشی از راهبرد اول است.
بنابراین از نظر اقتصادی، آنها در وضعیت بسیار بدی قرار دارند. نمی‌توانند پول قرض بگیرند. ما کنترل پول آنها، یعنی آنچه در اختیار داشتند، را در دست داریم؛ و مقدار آن هم زیاد است. آنها پول زیادی داشتند و ما کنترل کامل آن را در اختیار داریم.
من بانکدار آنها هستم. من بانکدار آنها هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/20810" target="_blank">📅 13:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20809">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ : می‌خواهید یک گورستان پرندگان را ببینید؟ گاهی اوقات به زیر یک آسیاب بادی بروید و هزاران پرنده مرده خواهید دید.
@WarRoom</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/20809" target="_blank">📅 13:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20808">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جورسلیم پست : ترامپ از حمله گسترده دیگری به ایران خودداری کرد ، با این امید که فشار اقتصادی بیشتر می‌تواند تهران را مجبور به تسلیم کند، بدون اینکه منجر به یک جنگ منطقه‌ای گسترده‌تر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/20808" target="_blank">📅 13:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20807">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJwa14lNoxMcWUtqA5-jgITPrzf9jSBkyxMqiEdbifXpIr756gcd84WBIrTJF7pRU5-9JuFlxUxNYi3X8m2unWdvVBHazlAxTcarE8RTwei4Bc0QjFQjfSnWyLww0I70K_1A3YrdlscUkUxi6dXzPxq3a-uhoRw1wxjGoRwEtdyOnUBqZqmGse3XoZSnQ-lE5REXZioHLNKlBpmcwy4L8hTga1X0OmNqMCjtYf9YJMl3fewSV_hS8Z-AvuPI3OpOGhNJcCiOAvSJrJDQkckUsdDVbqaBsHGqGnQ_pr6-BRUNLkYrHhSz7U9Ly2eJlYQU7wFQPK1yYP2sS5xKD9Y7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی درباره وقوع حادثه‌ای برای یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است. مقام‌های مربوطه در جریان این حادثه هستند و تحقیقات مرتبط همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/20807" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20806">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKefenrtjK3gcAV2aIMuifdQbaQ2_llbH21VF7I-RM6_93x4mj28mK8XqPKeW6ZRtUXGg7lOhB0ZrPHSArMqTlkGLjnX-lpvN1xZ0P3oekUBjMm690Sxm2sj3yeve-4QMEwa5w3UF9h4jsd4NJnBuedOJorhanRnRiLOrC0qTsJMRY3zdd52mx_TfimxCfpgrQgMnoQM7Z91_vYGvC22V8uKnfKt-Eru2_-NdiSOLVjk1dgshubHxNwkgs8SnltULedXSWYnvDThQJEFSA8g6KwHPdv5sQ6XTfy9UEsv_oZoJ2MxU0FecAaHgzxxBU1XQ7Y_mVn3tfqmywy3J_C2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی آمریکا از پایگاه‌های مبدأ خود در غرب ایالات متحده به پایگاه هوایی مک‌دیل در فلوریدا، در شرق آمریکا، منتقل شده‌اند؛ جابه‌جایی‌ای که می‌تواند نشانه‌ای از آماده‌سازی برای اعزام قریب‌الوقوع شماری از هواپیماهای…</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/20806" target="_blank">📅 12:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20805">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دادگاه جنایی دمشق حکم اعدام برای بشار اسد صادر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/20805" target="_blank">📅 12:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20804">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">https://www.instagram.com/reel/Db5HBuLozsg/?igsh=ajBqMW82djZrZW96
استوری که درخواست زیاد داشتید رو به صورت تریال پست کردم</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/20804" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20803">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارشهای رسانه های‌عربی حاکی از کشته شدن ۳ نفر در پی حمله حوثی ها به یک کشتی در تنگه باب المندب است
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20803" target="_blank">📅 10:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20802">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If_a-DPCFsPm0Vkd8X_54HfiwueUNoY4bxwP4ojvjZqsS3ZG6ABRSAOWh3KUFPb-kn6FkqXRKi4yygSz_7EsDQFzFlUULGItWFY7U_HND2vtw3HZy3HpbPh7BdRYXbt6LS83r_G-VrDWJ0C9M_KTk-RSHvQnh1SGIhttjQ7lxtgp_s2W-c7KUaa8-ZaZq1MaZHgURyyuxh6OwjsZLB6pWJwc0y0cMPFOjki3z34E12u9z82lggTqSMu_zYkka7-MA5KaL4oFpiPDEkB6PKluL7Le4ASz0-VvntzxPqhTLz9o9chyiQ6ZbAXKV39kF81GHDEkULyGMPX0tS3qMTsbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برای عبرو از ۹۰$ خیز برداشت
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20802" target="_blank">📅 10:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20801">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: ما بر اساس سه سناریو با ایران عمل می‌کنیم: اول، نظارت بر وضعیت نامناسب آن؛ دوم، اعمال فشار اقتصادی؛ و سوم، حمله نظامی قاطع. @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20801" target="_blank">📅 10:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20800">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏تام کاتن در برنامه مارک لوین در فاکس‌نیوز: مردم ایران باید آزادی و سرنوشت خود را پس بگیرند ‏سناتور تام کاتن با تأکید بر حمایت آمریکا از نیروهای آزادی‌خواه گفت مردم ایران نخستین و بزرگ‌ترین قربانیان حاکمان رژیم جمهوری اسلامی هستند و شایسته آینده‌ای بسیار بهترند.…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/20800" target="_blank">📅 10:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20799">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏رییس اتاق بازرگانی ایران و چین با تاکید بر لزوم پایان محاصره دریایی بنادر جنوبی ایران گفت : «چه با مذاکره،
چه با خواهش
، چه با تهدید و چه با جنگ باید این محاصره دریایی خاتمه یابد» و افزود: «تبعات محاصره از جنگ هم بیشتر است.»
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/20799" target="_blank">📅 10:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20798">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رویترز: تعداد کشتی‌هایی که از تنگه هرمز عبور می‌کنند، به ۶ فروند در روز دوشنبه کاهش یافته است، در حالی که میانگین این تعداد در ۱۰ روز گذشته حدود ۱۱ فروند بوده است. این کاهش در حالی رخ می‌دهد که امیدها برای دستیابی به توافقی بین واشنگتن و تهران رو به کاهش است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/20798" target="_blank">📅 10:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20797">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ: ما بر اساس سه سناریو با ایران عمل می‌کنیم: اول، نظارت بر وضعیت نامناسب آن؛ دوم، اعمال فشار اقتصادی؛ و سوم، حمله نظامی قاطع.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20797" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20796">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bdb30a06.mp4?token=l8J-vVmmnRB4NcICMZ8vmhfvHE-ShJLQr1O6TdNTIZUz1O72_ofO7Owlk9z_Pqf3aYZjDNc4hGovhLUctYgfCnA_gTVVnLj4va4gJepT0vqBCgPQn8jpPCtnnomecmMjvHZQ9nPeBwgjB3RQGFjzBycZLx5EV8Qe_K-p_ZDcNUtE6EWVbcPLEK0XQKLYZjdUW9buOLGLIcntHyzRttEzyJPSw3zJ9JyPUJJDrggFsuyuP9fkpN5jN5-5nA9hNBCDuOh_-ojasQLUmAcn4EM0ch3dEoEBxTQsFK7Bvn2o-jZWKTm3DZyo6TKyfDZTC1DTbq3nE83d5gZOUrKjjjbRBjLggHFuqkurukihvSH9xBGby0EZ-G9lfdDR9tg9fD43GsnILUQmIv_4FEmjESWz7PcGWnjoUjoTt4XIYTzupSbDIw988nNr4FgTid5oEweglpYF5AKRRVx_plGoEiPQRPBzmjF5sWksLuRfQ5kBKgRfDHDBDYYXVScpSmi4db-pxU2MJtyF2D7X6gmDUD8mkd3Zx3nAnc-89a3xN_vx5UK4dNGeUNFEMbk2L5e97iABURJ15WLSusRlm1bR6LmovE4YTwXFX5iuQ8Gv1Ygl_fzMPdc78N49XxGE5T0YMUfd34OumXUB41P4rC4jjV7vxsMhhYXwz9h0ubeCaNXXqSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bdb30a06.mp4?token=l8J-vVmmnRB4NcICMZ8vmhfvHE-ShJLQr1O6TdNTIZUz1O72_ofO7Owlk9z_Pqf3aYZjDNc4hGovhLUctYgfCnA_gTVVnLj4va4gJepT0vqBCgPQn8jpPCtnnomecmMjvHZQ9nPeBwgjB3RQGFjzBycZLx5EV8Qe_K-p_ZDcNUtE6EWVbcPLEK0XQKLYZjdUW9buOLGLIcntHyzRttEzyJPSw3zJ9JyPUJJDrggFsuyuP9fkpN5jN5-5nA9hNBCDuOh_-ojasQLUmAcn4EM0ch3dEoEBxTQsFK7Bvn2o-jZWKTm3DZyo6TKyfDZTC1DTbq3nE83d5gZOUrKjjjbRBjLggHFuqkurukihvSH9xBGby0EZ-G9lfdDR9tg9fD43GsnILUQmIv_4FEmjESWz7PcGWnjoUjoTt4XIYTzupSbDIw988nNr4FgTid5oEweglpYF5AKRRVx_plGoEiPQRPBzmjF5sWksLuRfQ5kBKgRfDHDBDYYXVScpSmi4db-pxU2MJtyF2D7X6gmDUD8mkd3Zx3nAnc-89a3xN_vx5UK4dNGeUNFEMbk2L5e97iABURJ15WLSusRlm1bR6LmovE4YTwXFX5iuQ8Gv1Ygl_fzMPdc78N49XxGE5T0YMUfd34OumXUB41P4rC4jjV7vxsMhhYXwz9h0ubeCaNXXqSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واشنگتن پست:
در پی تهدید به ترور از سوی ایران، دونالد ترامپ هنگام ترک نشست ناتو در آنکارا، ابتدا مقابل دوربین‌ها سوار هواپیمای قدیمی «ایر فورس وان» (بوئینگ ۷۴۷) شد، اما سپس به‌صورت محرمانه به یک فروند هواپیمای ‌کوچکتر
C-32A
منتقل شد. در همین حال،
هواپیمای قدیمی ۷۴۷
به‌عنوان هواپیمای فریب با شناسه «ایر فورس وان» به پرواز ادامه داد و خبرنگاران و حتی برخی کارکنان کاخ سفید تصور می‌کردند ترامپ داخل آن است.
در ویدئویی که از این عملیات منتشر شده، ادعا می‌شود
انتقال ترامپ با استفاده از یک کامیون خدمات فرودگاهی، احتمالاً کامیون حمل پول آرمور(زره ای) ، انجام شده است. این در حالی است که
هواپیمای
ایر فرس وان
جدید ۷۴۷-۸ اهدایی قطر
، هواپیمای رسمی جدید رئیس‌جمهور آمریکا محسوب می‌شود و با آن به آنکارا آماده بود و در این سفر، نخستین مأموریت خارجی را انجام داده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20796" target="_blank">📅 09:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20795">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M70cfwI6hEkz_XS5Qvnm3-1ztUFIpqXE6ksZ9oMba5txMOuPed66PMQnCdjrMB4rUYTA8Tl55zBQTezAGiKyvuvkiRTn-h104zK2UTCpqtO6Tl9DaN9sFq1JiPCjTDDTKGz9ADNhO_Nh3V1Q8mmoZtmqc75YFd2aBx1rgJoKOXbNHIt4G20qxrCLsQ0lQp3yWX8ornMcFsQDQUfePVElLn0KlOVeaZOdFaQqmvgi6wZzdCOSmDvHeK_gU4pNGPo7susvExHewP1anC1D4ttrJmCDouHD0DE413S0EmFgqH4LPvsdp_EgPC8OTUOHMFNasb3sPtV1HHRAFOa1MR3Txw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ آخر هفته را در زمین گلف خود در بدمنستر سپری کرد؛ در حالی که یک سامانه پدافند هوایی کوتاه‌برد
AN/TWQ-1 Avenger SHORAD
نیز در محل مستقر بود.
(سامانه AN/TWQ-1 Avenger SHORAD:
یک سامانه پدافند هوایی کوتاه‌برد آمریکایی است که روی خودروی هاموی نصب می‌شود و مأموریت آن حفاظت از افراد و تأسیسات در برابر تهدیدات ارتفاع پایین است. این سامانه معمولاً به ۸ موشک دوش‌پرتاب
استینگر (FIM-92 Stinger)
، یک تیربار ۱۲.۷ میلی‌متری و سامانه‌های دید حرارتی و هدف‌گیری مجهز است و برای مقابله با پهپادها، بالگردها، هواپیماهای ارتفاع پایین و برخی موشک‌های کروز به‌کار می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20795" target="_blank">📅 02:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20794">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ادعای وال استریت جورنال : مسئولان ارشد دولت و کاخ سفید به ترامپ توصیه کرده‌اند که تشدید تحریم‌های فعلی و اعمال تحریم‌های جدید علیه ایران، ممکن است موثرترین راه برای وادار کردن این رژیم به تسلیم باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20794" target="_blank">📅 02:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20793">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1faa6dd22c.mp4?token=KcC_PpB8WYb-B5RBYJ4Ve-Cfza92-VKk0nsDVBsN7IDYVTmOd0oVk6HRbL4n_8bkcEpeDkIaGCjqCXUyu4hhPTqiTuAidpAXuBH-Aj7hzQeuhfQZ_aVMZZHbFqDyxVtrEgqOPwevFsO3GjztotOxevRSprtycMoNlQzdULgvLGJMkQUDUwkOpqRLI3kOJCVLsCmJIyCIVkZ-v1VaMAEtHHj5xGj1frszcIs_L9TB-KbFpbtI5xEeL-dKwOWG2mwWgcJNKEHQwX5F9hsar7UlXU21x6Vk4n9if_XyJXGqYA-9szq0XnYxBkWJZkaqSJyZ1nn7ii4Ew9IUDdy0VrBzC5DdyiDbz6hjm66sezDMYXHYVxlu2aFtPRZnMMSmHECdtj4rDckRAEuWEoIETVLch9Q4ORxWVHzBCGONU4veVRs4x84uozdTpjLVHdwbIkjKGLR-AWKLfx3Xub-TSggPHCy8Wuhoz01TXml34K18XXmOeHFzRnoYcst5MJjl23LKPs7gg0u2hrjQvKTsG_VRjmaPvSNziqzR71xc16I7ZCUSMZPLhNErWE9oXMLMVqRHm-1eoxI3h3dZCoYS-SObgL_DaOxscxmPwoz0XtSuBV4NutjhRliemWPhjYmRkRS-kMHt_dUCmIabwjqL7OMgxXEQK7wv0sXi_KqXRMjocKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1faa6dd22c.mp4?token=KcC_PpB8WYb-B5RBYJ4Ve-Cfza92-VKk0nsDVBsN7IDYVTmOd0oVk6HRbL4n_8bkcEpeDkIaGCjqCXUyu4hhPTqiTuAidpAXuBH-Aj7hzQeuhfQZ_aVMZZHbFqDyxVtrEgqOPwevFsO3GjztotOxevRSprtycMoNlQzdULgvLGJMkQUDUwkOpqRLI3kOJCVLsCmJIyCIVkZ-v1VaMAEtHHj5xGj1frszcIs_L9TB-KbFpbtI5xEeL-dKwOWG2mwWgcJNKEHQwX5F9hsar7UlXU21x6Vk4n9if_XyJXGqYA-9szq0XnYxBkWJZkaqSJyZ1nn7ii4Ew9IUDdy0VrBzC5DdyiDbz6hjm66sezDMYXHYVxlu2aFtPRZnMMSmHECdtj4rDckRAEuWEoIETVLch9Q4ORxWVHzBCGONU4veVRs4x84uozdTpjLVHdwbIkjKGLR-AWKLfx3Xub-TSggPHCy8Wuhoz01TXml34K18XXmOeHFzRnoYcst5MJjl23LKPs7gg0u2hrjQvKTsG_VRjmaPvSNziqzR71xc16I7ZCUSMZPLhNErWE9oXMLMVqRHm-1eoxI3h3dZCoYS-SObgL_DaOxscxmPwoz0XtSuBV4NutjhRliemWPhjYmRkRS-kMHt_dUCmIabwjqL7OMgxXEQK7wv0sXi_KqXRMjocKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تام کاتن در برنامه مارک لوین در فاکس‌نیوز: مردم ایران باید آزادی و سرنوشت خود را پس بگیرند
‏سناتور تام کاتن با تأکید بر حمایت آمریکا از نیروهای آزادی‌خواه گفت مردم ایران نخستین و بزرگ‌ترین قربانیان حاکمان رژیم جمهوری اسلامی هستند و شایسته آینده‌ای بسیار بهترند. او گفت: «همان‌طور که رونالد ریگان در قرن گذشته در برابر کمونیسم شوروی ایستاد، ما نیز باید همواره در کنار نیروها و دوستان آزادی بایستیم؛ چه دولتی طرفدار آمریکا در برابر شورشی ضدآمریکایی باشد و چه مبارزان آزادی‌خواهی که برای رهایی از دیکتاتوری‌های کمونیستی یا اسلامی تلاش می‌کنند. همان‌طور که پرزیدنت ترامپ اوایل امسال بارها گفت، کمک در راه بود و مردم ایران باید آزادی و سرنوشت خود را دوباره به دست بگیرند. اگر مردم ایران به آینده‌ای بهتر دست یابند، آمریکا امن‌تر و جهان نیز امن‌تر و صلح‌آمیزتر خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20793" target="_blank">📅 01:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20792">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HktMPEgQil_dgNwi2qcr6yi15GtduENj4m9FVwj2CfttZmypWE5hZUi38hicE0b5dFL8ZFYoVbOpkHF88Mbc5bToLgCSdnz8HHGB7MLC-TmrxkjmIs8-PdvYsPrtl5Qqqk3U8D2ueHqnWeHxPrJ5ZbN2j98yrD68jJcSrPpn0bAjZfLVEQWZQURCGO1xa0O0KXjmuiUSnjqpuDKkkEFtbZ7R4SYsK6iAaTW1pHI1g_f1yZYzYWXQSNF3uyn5RPOwCv9peZPI-r_RFHOT1xzuxgb4GoRQdCILNyCeSM6-EGA-WJU7rwqQbx1Mbwev3chQzwrW1V_Ebf0bJN4jhOCeMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۵ نفتکش مرتبط با عربستان، که بیشترشان نفتکش‌های بسیار بزرگ و خالی هستند، در حال حرکت به سمت خلیج فارس هستند.
ترامپ همچنین امشب اعلام کرد که تنگه هرمز کاملاً مین‌روبی شده است. باید ببینیم میتوانند عبور کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20792" target="_blank">📅 01:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20791">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اتاق جنگ با یاشار : کنگره آمریکا در تعطیلات تابستانی قرار گرفت.
سنا از ۸ اوت ۲۰۲۶ تا ۱۴ سپتامبر ۲۰۲۶
عملاً در تعطیلات است و جلسه عادی بعدی آن
۱۴ سپتامبر (۲۳ شهریور)
خواهد بود. مجلس نمایندگان زودتر برمی‌گردد و
۳۱ اوت (۹ شهریور)
رأی‌گیری‌های عادی را از سر می‌گیرد.
حالا اگر آمریکا در این فاصله به ایران حمله کند، تعطیلی کنگره از یک جهت می‌تواند برای دولت ترامپ یک مزیت سیاسی ایجاد کند:
ترامپ همچنان فرمانده کل است و تعطیلی کنگره به‌خودی‌خود مانع دستور حمله نمی‌شود؛ اما نمایندگان و سناتورها برای تصویب قطعنامه، محدود کردن بودجه یا اعمال فشار فوری علیه عملیات نظامی، امکان بسیار کمتری برای اقدام سریع دارند
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20791" target="_blank">📅 00:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20790">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20790" target="_blank">📅 00:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20789">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کامنت جدید برای ترامپ (کارای اداری)
آقای رئیس‌جمهور، فن آخر استاد را اجرا کنید
🎯
https://www.instagram.com/reel/Db30SjjS-Wl/?comment_id=18183518170406206</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20789" target="_blank">📅 00:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20788">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏
رسانه‌های سعودی: اسماعیل قاآنی، فرمانده سپاه قدس، به بغداد سفر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20788" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20787">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">عراقچی در تماس تلفنی با همتای آلمانی خود: تضمین امنیت تنگه هرمز مستلزم توقف اقدامات تهاجمی آمریکا، به ویژه محاصره است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20787" target="_blank">📅 23:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20786">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ: رئیس‌جمهور بعدی بابت کارهایی که من انجام داده‌ام، اعتبار زیادی دریافت خواهد کرد.
لطفاً یادتان باشد که این من بودم، نه آن‌ها.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20786" target="_blank">📅 23:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20785">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرنگار: آیا پاسخی به نتانیاهو دارید؟
ترامپ: من امروز آن را در تروث منتشر کردم. من یک پاسخ دارم، یک پاسخ خوب. بله، رابطه خیلی خوب است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20785" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20784">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6383d52564.mp4?token=hHtSHoAekO9-IGNF2hwChxDPWK9nssUzaStgk4u5Rm4Pu3YMvIi6qXIF8KU197q5jE4RzwovfKEsIIiQVStbt9E4UrT7FcBx0xgMuxsM9nF7UBIkgYEw0aT7biJSEsNQUAiOWKoCg0uexMXK-yMBygP6IPVjBjuyys75DuqZYpMkfgYna26uzCVejkZBtOKFpUB5W1g9gj14IpUeEuH4125eOQqYiixihnd5EelnGkCPl0THbLbhIGDL7gSK3TUMTJoLAzPKx7MUOStmrx3bOhxlGzQBBz_TRghGwfTgKuIkwbUEust6tppTEkUolSilgSsQubbtSYiLwm9L69yt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6383d52564.mp4?token=hHtSHoAekO9-IGNF2hwChxDPWK9nssUzaStgk4u5Rm4Pu3YMvIi6qXIF8KU197q5jE4RzwovfKEsIIiQVStbt9E4UrT7FcBx0xgMuxsM9nF7UBIkgYEw0aT7biJSEsNQUAiOWKoCg0uexMXK-yMBygP6IPVjBjuyys75DuqZYpMkfgYna26uzCVejkZBtOKFpUB5W1g9gj14IpUeEuH4125eOQqYiixihnd5EelnGkCPl0THbLbhIGDL7gSK3TUMTJoLAzPKx7MUOStmrx3bOhxlGzQBBz_TRghGwfTgKuIkwbUEust6tppTEkUolSilgSsQubbtSYiLwm9L69yt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایرانی‌ها صدها هزار نفر را کشته‌اند.
حالا دارند تاوانش را می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20784" target="_blank">📅 23:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20783">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها می‌توانند دردسر درست کنند، اما ورشکسته هستند. آنها پولی ندارند.
ایران کاملاً ورشکسته است. آنها حقوق سربازان خود را پرداخت نمی‌کنند.
تورم آنها 309 درصد است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20783" target="_blank">📅 23:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20782">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43e103fdf.mp4?token=qRvmhlbTHgf02NIIdp6GB9OcRv7hQeEm6RMqclbM-L006O2Ou6WScT_JX6QzP4l-XF6WLh72prw7VUGx7oWi0ggk7q1sIv_oI7G5GKQj25outXBLjpASz9JracdMxNY-H8p0ZhHq2Sc96Ud7wH1vLjHuRgHC1u131GnG5fuuDzcYd7xwNwyRJvZT-Ynb-4U0lf0TUzgq6LbZ1Lgtu7BkVEvjq5GHxNKZoG-21_svV_7N7jHAdgF-plGpOzL5GhAdvMjV4wGhktMMCdG6poSUybuSyB3nbK61hSbS11TkGAEjBZ6dgkCxgaC9uhCrWKQphh7O2D5xFR-V3Fq5jATT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43e103fdf.mp4?token=qRvmhlbTHgf02NIIdp6GB9OcRv7hQeEm6RMqclbM-L006O2Ou6WScT_JX6QzP4l-XF6WLh72prw7VUGx7oWi0ggk7q1sIv_oI7G5GKQj25outXBLjpASz9JracdMxNY-H8p0ZhHq2Sc96Ud7wH1vLjHuRgHC1u131GnG5fuuDzcYd7xwNwyRJvZT-Ynb-4U0lf0TUzgq6LbZ1Lgtu7BkVEvjq5GHxNKZoG-21_svV_7N7jHAdgF-plGpOzL5GhAdvMjV4wGhktMMCdG6poSUybuSyB3nbK61hSbS11TkGAEjBZ6dgkCxgaC9uhCrWKQphh7O2D5xFR-V3Fq5jATT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: تنگه هرمز کی باز می‌شود؟
ترامپ: الان باز است.
ترامپ در مورد ایران:
همانطور که احتمالاً شنیده‌اید، ما تمام تنگه را مین‌روب کرده‌ایم. شاید نشنیده باشید.
ما ۱۰۰٪ تنگه را کنترل می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20782" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20781">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: اگر قرار باشد خسارتی پرداخت شود، ایران باید آن را بپردازد
ترامپ: تشدید شدید تنش‌ها همچنان یک گزینه است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20781" target="_blank">📅 23:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20780">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرنگار: شما گفتید این آخرین فرصت ایران است. حالا چی؟
ترامپ: خواهید فهمید.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20780" target="_blank">📅 23:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20779">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ درباره ایران:
هیچ اتفاق بدی در نتیجه اقداماتی که ما انجام می‌دهیم، رخ نخواهد داد. هیچ اتفاق بدی رخ نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20779" target="_blank">📅 23:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20778">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOA4keGb9aVVwirohPmXwdCemJAeNWZovVHqD8hTOkvRgrHWqNp42hlznRw5UwC-aMwOnKXmC50KU-DYy-HwfzJ5FemHfdA60uEpdgT9uPMcs1bnubr33AzxU_AIYu9pngzPMWMmPgkq0n30-7kQpcrxADOD8Aqofyhc6RMKpn1iDn3fVY_gxJKghu20I3jnw3wR8v2Szddo9gkHkqTUKDh6_LHPepICwB_JpzCE2ASC3LqGpiTmFAshU6GVDn8OW2IiigbDgGKD5N83Ada9OwOsVE2BvUz49J6OQHvLiGB9KjmmFgDegBh77SYi1kveXR_ijSi447OSqcyE4W5y7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج ماه گذشته به آن‌ها وارد شده است؛ درگیری‌ای که از آن‌جا آغاز شد که آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند. با این حال، چنین…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20778" target="_blank">📅 22:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20777">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20777" target="_blank">📅 22:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20776">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7OqoJTqrYJStDGYWL4vX1TJ__KbWl-M0KUx3zA8GRFDRas6etQN28MwoXbZRhqCPUqPkcOwrHrtHJ11YVjD3CqR_TOwxpZcLsSqX9JSSVM87uEM_zT7jPjUR0qyDtgwKKvLl1YFGFssRw8ubqS5-xg5opXOSd9eTjYSZxi2mmsNHohsnU3WU0Iv5Ia6JYqAH0EqeND8RpV5Kfd3Hg8YyJkH6Pmv82AERWlQrksHJoWDQVfu2HGgVJyjfaOUbINQ44M65PAxxsJIBa-a8-FGFndtOBU5IAPFRAxWopxesmENsp6PHCvoWZ_SxlUzHibrTzwB4yEL6CmWKOHy2IUZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی آمریکا از پایگاه‌های مبدأ خود در غرب ایالات متحده به پایگاه هوایی مک‌دیل در فلوریدا، در شرق آمریکا، منتقل شده‌اند؛ جابه‌جایی‌ای که می‌تواند نشانه‌ای از آماده‌سازی برای اعزام قریب‌الوقوع شماری از هواپیماهای پرمصرف (احتمالاً بمب‌افکن‌های بی-۵۲) به انگلستان و سپس خاورمیانه باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20776" target="_blank">📅 22:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20775">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏کانال ۱۳ اسرائیل گزارش داد که این کشور به آمریکا اعلام کرده به هدف قرار دادن نیروهای حماس که در حمله هفتم اکتبر مشارکت داشتند، ادامه خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20775" target="_blank">📅 22:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20774">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c44f7cd8.mp4?token=Za2ooU-u6EQQR_sk9RLQGrImOZADtMPVoG0g2THNxwr5-6jncdYtM_2mZtqnVfgk81KY7bOOAL5rWobvjTjKnGImAh1sU5wXf4WyA6AE4Xxa9ErgzETtOSO6dghXOjw3HoNpmRdZ8XIjInI7QUDRQEZiC7-eC82-1dtGHwAC0036tpcEotKSjCP9us_hdTvle7H_ZGuRa1cCRJO3TViSO_HYZGMXUB0dGDx5TTQ-x5wIQJqRb90lFGNCfJsxvfBpsd7pd6iyIKlxzLPo2-t2UHZA39lhd5TOCsb1RLW8uoo-S44ylkQNggcpdTcpu7LsrEnbs2wyCsYRVxIAZtCMSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c44f7cd8.mp4?token=Za2ooU-u6EQQR_sk9RLQGrImOZADtMPVoG0g2THNxwr5-6jncdYtM_2mZtqnVfgk81KY7bOOAL5rWobvjTjKnGImAh1sU5wXf4WyA6AE4Xxa9ErgzETtOSO6dghXOjw3HoNpmRdZ8XIjInI7QUDRQEZiC7-eC82-1dtGHwAC0036tpcEotKSjCP9us_hdTvle7H_ZGuRa1cCRJO3TViSO_HYZGMXUB0dGDx5TTQ-x5wIQJqRb90lFGNCfJsxvfBpsd7pd6iyIKlxzLPo2-t2UHZA39lhd5TOCsb1RLW8uoo-S44ylkQNggcpdTcpu7LsrEnbs2wyCsYRVxIAZtCMSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده ستاد کل نیروهای دفاعی اسرائیل در کنار فرمانده سنتکام: "ماموریت ما این است که بر واقعیت تأثیر بگذاریم، نه اینکه تسلیم آن شویم."
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20774" target="_blank">📅 21:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20773">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20773" target="_blank">📅 21:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20772">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جان بولتون : کناره‌گیری از رویارویی‌مان با ایران یک اشتباه است. ایالات متحده ضربات سنگینی به ساختار نظامی رژیم ایران وارد کرده و سال‌ها طول خواهد کشید تا آن را بازسازی کنند. صرفاً به این دلیل که نمی‌دانیم اهداف نهایی‌مان چیست، نباید با دادن یک پیروزی سیاسی به این رژیم، برتری بر تنگه هرمز را به آن ها واگذار کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20772" target="_blank">📅 20:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20771">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544e884864.mp4?token=BU24txsH2kM8UA6pHIBq32bN_NBpx_06Gfxz6pyB4blLsCjIWy97TU33AmiPHT1YfW_T7Jo6F1j_z2ls6ysqM6UDbTsNevHGG4PGuc74UuJi_8KsX4yUa22t8e_gU2zwIn4kvBUlQJsWHUjM_wqDSXftKHNpIJ9g_XKlCSmZq21-I3mhYytAG2sqV6eUX_IPDFoFQe132z93QcCteQ6Hz5YxO01cyjaIsIWvhU07u8XXWlzILXl3GYR_nksOydjgQxZjaSqj6rFy9ASEFxS6Uhnlcshq-WYAblgfx3Z6uT8SuFhe4SMhf_W0ZgiEhlb1-ZsjuexBvxOgi0BB7TbJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544e884864.mp4?token=BU24txsH2kM8UA6pHIBq32bN_NBpx_06Gfxz6pyB4blLsCjIWy97TU33AmiPHT1YfW_T7Jo6F1j_z2ls6ysqM6UDbTsNevHGG4PGuc74UuJi_8KsX4yUa22t8e_gU2zwIn4kvBUlQJsWHUjM_wqDSXftKHNpIJ9g_XKlCSmZq21-I3mhYytAG2sqV6eUX_IPDFoFQe132z93QcCteQ6Hz5YxO01cyjaIsIWvhU07u8XXWlzILXl3GYR_nksOydjgQxZjaSqj6rFy9ASEFxS6Uhnlcshq-WYAblgfx3Z6uT8SuFhe4SMhf_W0ZgiEhlb1-ZsjuexBvxOgi0BB7TbJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه مشترک چارلستون رسماً به پایگاه مشترک لیندسی گراهام تغییر نام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20771" target="_blank">📅 20:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20770">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRz29IPZXkYdvugGc-o9pEeCG8v1zt0VFRYaEd8nHBg_UyEqAdc1U01j3_HZ9nciGkWUNn9angQTgBvhEc2cJkDN8DCrIC16jQSRY2haME8lrWBjMvC-2rCBmEoEoZJVdhN7fCkxQHc_aGyJ-DIn5gMt0YhXTg4clVyIyt1OhHXp1lA7ApRYP86fxZTz-yjWJ9LWIYEu-gyBgT13567X72TMzgFthVHDxvI3iO7o1EmJyBoE5zWl5bwhX37hWcarjImhjA46HEG5mMQyQBwvUJurcwSV6T5dFx463R1hETvlaTQzxnmZF33m5QcvDh6_qzwmo8eZwL70LWmvIaO6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج ماه گذشته به آن‌ها وارد شده است؛ درگیری‌ای که از آن‌جا آغاز شد که آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند. با این حال، چنین موضوعی هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود! اما این ایده جالبی است، زیرا حالا من نیز از ایران درخواست غرامت می‌کنم؛ بابت تمام افرادی که با بمب‌های کنار جاده‌ای و درگیری‌های متعدد، که به آن‌ها شهرت دارد، کشته یا به‌شدت مجروح کرده است؛ اقداماتی که در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد. این شامل خانواده‌های کشته‌شدگان ناوشکن یو‌اس‌اس کول و هزاران نفر دیگر که در نبردها جان باختند نیز می‌شود. افزون بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه برسد به ۵۲ هزار نفری که در پنج ماه گذشته جان خود را از دست داده‌اند. به نمایندگان خود دستور داده‌ام که این موضوع را با قاطعیت در همه مذاکرات آینده مطرح کنند. از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20770" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20769">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مرندی ، مشاور تیم مذاکره کننده : جمهوری اسلامی آگاه است که نیروهای دولت ترامپ در خاورمیانه در حال آماده‌سازی برای یک حمله برق‌آسا هستند؛ حمله‌ای که ممکن است با همراهی نیروهای اسرائیلی انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20769" target="_blank">📅 19:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20768">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">با حکم مجتبی خامنه ‌إی آی، علی عبداللهی فرمانده ستاد کل، احمد وحیدی به سرلشکری فرمانده کل سپاه، کیومرث حیدری جانشین رئیس ستاد کل، ایزدی جانشین فرماندهی سپاه، عظمایی فرمانده نیرو دریایی سپاه و طائب رئیس بسیج شد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20768" target="_blank">📅 19:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20767">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yfmd0V0YuP0VbsXPSx6Hcsb9BCwjShX2dsoEckzzwiEXEJswL5JQymsrnyk7a6m8l2vqBhj8zLi4Yqoh98pEK3GFWAmRrkEaWHXOLpEGC8kfxek3QqcX7Ok-sImaynrJONOAV2GGq9dAkSm7KvSo2iqq0TXjpjy-ZkOP0rFdgF2vJy8zGjeywTzP_XXg0yjyxONqtWIbMeXzpKcK2X_vUCDRg0HXO79--tKUosMYN05W5WID2n1ln8kvWSDi8naISNpVOqEz-sDnI7PFWNqjYV2gwosyL5aNDiojrS3btl2i-HR-50-_jmYb9BoWrTjEhoLIm107ySKrcUsUkUQdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : جمهوری اسلامی متوجه شده که با بالا نگهداشتن قیمت نفت، حمله قریب الوقوع آمریکا را به تأخیر میاندازد. امشب، ساعتی قبل از باز شدن مارکت، این حمله ها را انجام داد و هم اکنون با باز شدن مارکت، نفت در لحظه نگارش این متنالان حدود سه دلار گران…</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20767" target="_blank">📅 19:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20766">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_MJmZc3F_xFFix0sgcR2RbPRM71ot6n5RYCZdQ_Z4Zd8000SsOSv8XsacL2OkonzMtqj1o1XWT939aUSQlnKiRH2QzL2jqp-2Trg4o1GTYmzRJUDM1JMRizsRAKH-X_FXQdE2ZDL6BtnTLtR3i-0_p-WgLDVLy4i7uzPkm9IcSPwH4eHtRTFNi3dMztqLO6hxD_udciER77LQsFNtqq6YqzvOplKkI69KwU_PxBLrak4DWn8C5GnIWHeeo3M77i8_AWwQx0hPa4nhWLQ0dnNFoZ2NqfJ3mnL_1lwvc3dEr2PHMk_BGXiSG-LD7fsY37CpFEZtr4HzsZhHhAugKWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ : عاملان کشتار جمعی اکنون کنترل ساختار نظامی و امنیتی ایران را در دست دارند.
ایران به‌تازگی قدرت را به‌طور کامل در اختیار دو فرد تحت تعقیب اینترپل قرار داده است. محسن رضایی اکنون با اختیاراتی هم‌تراز با رئیس‌جمهور، ریاست شورای عالی امنیت ملی را بر عهده دارد و احمد وحیدی نیز با اختیاراتی در سطح رهبر جمهوری اسلامی، فرماندهی سپاه پاسداران را در دست گرفته است. هر دوی آن‌ها به دلیل نقش ادعایی در طراحی و سازماندهی بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در آرژانتین، تحت اعلان قرمز اینترپل قرار دارند
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20766" target="_blank">📅 15:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20765">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وای نت : ‎نتانیاهو قصد دارد انتخابات 27 اکتبر کنست اسرائیل را تحت تأثیر حمله جدید به ایران قرار دهد تا ائتلاف لیکود متلاشی نشود
گزارش ynet می‌گوید نتانیاهو در شرایطی قرار گرفته که
تهدید ایران و بقای سیاسی شخصی‌اش عملاً به هم گره خورده‌اند
؛ زیرا اگر بدون یک دستاورد بزرگ وارد انتخابات شود، فرسایش قدرت نظامی و نبود موفقیت سیاسی می‌تواند برای اردوگاه او هزینه انتخاباتی سنگینی داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20765" target="_blank">📅 12:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20764">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfRLiszATFm_BMvN10bmtZo_VUz0rQU6Cf0QpwNBWqp9FY2HFHKWm6BNJ8YtjbPhoec29wq5giLqAcKKW7bNqfLC-dnNVED_ls8Q0_lJPSfmdO58wDzh_rp0ZfGxhwpqmONJ_1vkxtF0UBdhl_LQiQWCjmVHRnG0xq5Xr8SH7H_v4K2ODMNd7iG7W9fDmXhIMoF0AXtQBzk-kozFVePyFvYs4aLOW2c8GbWwzoY4Fm6konwmXCpGDa-eo9tOd0vrWDaNm3VnFO9a4dj8rHrwrKGTq0CAnnuWF0FdGKsiCjsKptEk_cT88bZIYBSt7sQlHwBb0tvRXsDIGUL2vG1KtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور محمود بوتاکس در جلسه دیروز مجمع تشخیص مصلحت نظام
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20764" target="_blank">📅 12:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مقام ارشد به کانال 14 اسرائیل: بزرگترین ترس دشمنان ما این است که نتانیاهو در قدرت باقی بماند.
خب،این به چه معناست؟
نتیجه بگیرید.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20763" target="_blank">📅 11:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مجید شاکری ،مشاور قالیباف :  ترامپ با ما توافق نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20762" target="_blank">📅 11:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">باراک راوید ، آکسیوس : یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «نگران یا ناراحت نیست» و آن را بخشی از فضای رقابت‌های انتخاباتی در اسرائیل می‌داند.
این مقام آمریکایی گفت: ما نیازهای سیاسی بیبی را درک می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20761" target="_blank">📅 10:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbe5WKlbEkxDQfpFUMkgsv8eQJq3a-V_bXfiy72P4ZtWGqE3TwF5Scm5jQbhGLXceryRPl0aomktruHDjQI7byzCrrk-3XyMP4T6E0ASyd76ukpqxdULpGVmt5LN9nlqdehql3crHB4ygKvzDT_8ffJZEU0IN_tdR2WgChCGEnnMztoHPBWBu4a2kOcNHF40QGB5xZWdXBEXI1ARc2O9ypajO6s6OvNLCqoziD_xyhwbSihn4gO9_wT4no76T03ptDNsCPhu2i12L0UlhSxrPSOfCyGnf3h7cX_tuUSRLTxrsCTxmwt9Th8xdu0SOtlgozIEjlPyazcKpVrrP19eDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیز نیست، بی بی داره خنثی سازی و بازکردن ورودی های تونل ها رو براشون انجام میده.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20760" target="_blank">📅 10:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">مهم نیست داش یاشار مهمات عمل نکرده دوران هخامنشیان هست</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20759" target="_blank">📅 09:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlQIvn53v4stPr_2vzmEzGvvutDRs2Xi9L4dmfv6EVGl0IJhEp1l9wZmPtJaj2IWUTXxQqfud1VjK7UEb9ZrsXVbozlZ8fjmLUODKAWiokWpYkd3BeJjChSoIP43qZQy02-TvGzPvrwjpdiNgaScNPiAid-PEBo80ryVs2mxanfU5wO_1QAESMxF_jdULqmgnnPjNOjWDnZpjBx8zbrwMcB8tYejxpBef4Aug89VIt3k32JB8lHmEr6O-Wr8SaIyCV2OXmEOJEmYQQKS0fe3xrcBZJVeXVNJe-6cU9Jt0OINtxunftWgOBxSE3eg3BOdbkOsnaQT2vUNwO1hwXUcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان سمت پادگان ۱۵ خرداد انفجار جدید
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20758" target="_blank">📅 09:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ9Yb9bUddRZeY6cqJpQh4dL46Y6KRB7sD8mZmYWlqJUHCTXCTdF6cCAiJH9fKqQO9_AKxCDrh0ixSME2KNLVvLTjzmXHa_EI-3TRD-Fdgpi1wU7c2663HFJBnROGhgW4R3QTxGVeacR8tpEv7_hdlOEPLt9Tie58VeTSL7aHCJd3jJsdDJ5UCwEEB1oQ8F-H_6hsefg4hHuvJn5KUQsi-jpzPzyly9qeR3hDHUiqbvoFlspzf38-od81YxfqOkyhIHu2WFb0svhHkB4lFE8FuXho7eJmqzgLptm6s93dyKCehKQqFktTO3DTAvFY1IS_ZDDCgeHuWMCQtWWe7N7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار شدید در اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20757" target="_blank">📅 09:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAOixLf9D72Q6zKTmjno6vOOzN_5x1MsgpxTE5bQtO-fLsJEdalBIY8TIbloTIZCLBRBY0zsx5Y2oL6Oh14a5WU_EUFuEGo4vUUVD6-SE86iXBDGJ00or_w3qPAaPEzPnTRxkqkN5Ez-gSAnyBYZicOW46yqzP2776HgunjmiJPiHGfkxKwaWRPNIdZiOosSKYbb6tKf8qa2LX7SIBoQ5LplRbfaqn63VCz2zPryjpsjFvMZJsA5UPTmvtZEIICN6HSqpJmboHH9pR2kk4O8nVxdlr4c0q4dmwamHcmwzwHIS6Q9q2Morc1jW1YwHDZORobq7g3efpmsWK0JWIrzMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز : زیردریایی جدید «روز قیامت» اسرائیل که با هزینه ۶۳۴ میلیون دلار در آلمان ساخته شده، توان بازدارندگی این کشور در برابر ایران را به‌طور چشمگیری افزایش می‌دهد.
این زیردریایی از کلاس «دلفین» است و شرکت آلمانی «تیسن‌کروپ» آن را ساخته است. همچنین، این بزرگ‌ترین زیردریایی ساخته‌شده در آلمان از زمان پایان جنگ جهانی دوم به شمار می‌رود و به جدیدترین موشکها مجهز است
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20756" target="_blank">📅 09:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20755">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4468b68072.mp4?token=vu401G2qkXeoWB3EzIFUn9tjftm-0gu4ONtTmvt7ajKD6k1RUoxESJrMoBqmf1FNeiv4n02F0Eyj9n3hn326GzVDhRIU8l4_1PsWMFIQeYoXbMJeRYhF34cPzPMEUSiX93anYhgIU6zxuKidZrdpPsd4AO74lPGeXNPoE9a4aABZ2-u7MWR0lTAYbwjZQ_XCvi8RS6ysh-gYfVwMwUFKqmUGbjamVPSsN0TNVBvON7IHSnl0nqqCvVnDBNRE8Fl2OZZh2rePUpWKLTbvcWkVyTvHq6HKdthQWXCi26V9aWtAIbivIrD7czCkzk6vPCMyhUNEDR_WAKXi44dwW1jAgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4468b68072.mp4?token=vu401G2qkXeoWB3EzIFUn9tjftm-0gu4ONtTmvt7ajKD6k1RUoxESJrMoBqmf1FNeiv4n02F0Eyj9n3hn326GzVDhRIU8l4_1PsWMFIQeYoXbMJeRYhF34cPzPMEUSiX93anYhgIU6zxuKidZrdpPsd4AO74lPGeXNPoE9a4aABZ2-u7MWR0lTAYbwjZQ_XCvi8RS6ysh-gYfVwMwUFKqmUGbjamVPSsN0TNVBvON7IHSnl0nqqCvVnDBNRE8Fl2OZZh2rePUpWKLTbvcWkVyTvHq6HKdthQWXCi26V9aWtAIbivIrD7czCkzk6vPCMyhUNEDR_WAKXi44dwW1jAgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در واشنگتن دی سی، در پایگاه اندروز فرود آمد و مصاحبه ای‌ نکرد که به نظر من بازی با رسانه هاست تا در خبر های‌ زرد و دروغین خود غلت بزنند تا غافلگیر شوند
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20755" target="_blank">📅 02:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20754">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewHWeejQYnC5EQa9AWrDQPq_tv23WTaoWi1Apemn3M_G6C2j399r_zByVEsWEAYIIPvdzBF9DO95zQCknZFKNft8qpmcoweKsRZQSHYrm7q4a-mh3DZ12BpwhRpSbkq0a-iTOhcNw51WBzshl_04Dej_CUDGt944WqbC1_ju5vgwfHH0iclpvoHJoIdvj17JZG1NkohTBiPpbrTkEmRlGWDbtQ31F6got0tVa4b8Snl1QfJRcsvd2KmtgdTy5Y7j6faLNpqoU6uQJCPLtya2Z8mxgxRFPa-5i4T7KcSRUwSmTUEEWOUiFbE0UN5aGu_ID33Zlv61ehRcq_SxVtMBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : تا اینجای کار امشب در حالی که در سراسر خاورمیانه آرامش برقرار بود، در ساعات اخیر، حکومت ایران تعدادی موشک به سمت یک کشتی که در حال عبور از تنگه هرمز بود و توسط نیروهای ارتش آمریکا اسکورت می‌شد، شلیک کرد. سپس، آمریکا و عربستان سعودی تعدادی…</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20754" target="_blank">📅 01:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20753">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با یاشار : تا اینجای کار امشب در حالی که در سراسر خاورمیانه آرامش برقرار بود، در ساعات اخیر، حکومت ایران تعدادی موشک به سمت یک کشتی که در حال عبور از تنگه هرمز بود و توسط نیروهای ارتش آمریکا اسکورت می‌شد، شلیک کرد. سپس، آمریکا و عربستان سعودی تعدادی پهپاد به سمت جنوب ایران پرتاب کردند که پهپاد سعودی توسط سپاه رهگیری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20753" target="_blank">📅 01:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20752">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bItmNcoP8VVDdp93iVBjWZ-f2aAWingtzGjZLyw2Ogv8zzOGUb0hNQMe5bD2Csvcz9Mt2nOiWPfXpYr7toGPOFFktnPt1chN9ku3zcUt3IiUlHpH1j6knCwDHJdszGjbYAyeYtDmy5qzxZFfVg2rdupxem2ubfuZW4iR4piIpfvvQ-CzCz59jWCiWREhHQ7JDn2d1lcVmueisiRky0DFkPJU4AIMgKyZQEVHnqHmFOwvhN_1FbkYJ0oOSMgaWTvKV83ZKzWD2epbAYRz5M4KuvHkwe6TmOjryMo09awcBK7XzoyyXKAmjMVRs1y4MP6rxJ0Nq2tydgAAYaR-9lXhzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام :
ملوانان نیروی دریایی آمریکا
بر روی پل فرماندهی ناوشکن
USS Ross (DDG-71)
در حال نگهبانی هستند. «راس» یکی از بیش از
۲۰ ناو جنگی آمریکا
است که برای پشتیبانی از مأموریت‌های نظامی در خاورمیانه مستقر شده‌اند؛ از جمله اجرای سخت‌گیرانه
محاصره دریایی آمریکا علیه ایران
. ما، تا
۱۸ مرداد ۱۴۰۵
(برابر با
۹ اوت ۲۰۲۶
) نیروهای آمریکایی
۵۵ کشتی تجاری
را تغییر مسیر دادهایم،
۲ شناور
را از کار انداخته‌ و برای اطمینان از اجرای این محدودیت‌ها،
۲ کشتی دیگر
را نیز مورد بازرسی و سوار شدن نیروهای نظامی قرار داده‌ایم
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20752" target="_blank">📅 01:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20751">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بلومبرگ: توافق هرمز همچنان دور از دسترس است، با توجه به اینکه ایران از مذاکرات مستقیم با آمریکا امتناع می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20751" target="_blank">📅 01:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20750">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20750" target="_blank">📅 01:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20749">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">روزنامه کیهان : اردوغان و شهباز شریف مثل روباه مکار و گربه نره بن سلمان را سرکیسه کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20749" target="_blank">📅 01:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20748">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead9f1f71d.mp4?token=fOVL61p-TqO2Mfn42ZoOBqX66f_mlfiIFnW1FZXVf1gOv2TDeaHdlV_wPlANBIXpOx6u1wg_HI-k3vf79ZCCKQy88-g2HnO-kA8XzZQH-2GAwG2uRy8N9BiMIY-hm9aHEVgrZfTPealhxxWN5g1bdHdIFihPReSrvPmdeFiGVhA-SwOukATlsXGr9f7JA9jJQBx1Z9Me-1xN2vUw-4XREefcJr2PUII31dAVpxyXLta9rEkZFaQchCw5ozIcv78ur8lDZIgpnEH0ksWju1P_7iaPUxDOso5amHHzpVRgpepLoSu3ES2Iw5z7zDEZ5SXic1q0hS7Kipn0_edbHex07Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead9f1f71d.mp4?token=fOVL61p-TqO2Mfn42ZoOBqX66f_mlfiIFnW1FZXVf1gOv2TDeaHdlV_wPlANBIXpOx6u1wg_HI-k3vf79ZCCKQy88-g2HnO-kA8XzZQH-2GAwG2uRy8N9BiMIY-hm9aHEVgrZfTPealhxxWN5g1bdHdIFihPReSrvPmdeFiGVhA-SwOukATlsXGr9f7JA9jJQBx1Z9Me-1xN2vUw-4XREefcJr2PUII31dAVpxyXLta9rEkZFaQchCw5ozIcv78ur8lDZIgpnEH0ksWju1P_7iaPUxDOso5amHHzpVRgpepLoSu3ES2Iw5z7zDEZ5SXic1q0hS7Kipn0_edbHex07Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پهپاد ساخت چین که توسط نیروی هوایی سلطنتی عربستان هدایت می‌شد، در سیریک، استان هرمزگان، ایران سرنگون شد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20748" target="_blank">📅 01:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20747">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بازهم صدای انفجار/پرتاب از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20747" target="_blank">📅 00:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20746">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-51a_hMZP-6aPwW_fyBg-93XJmQhZfQL0fL5MkgVIjA-hwzZRfp0JoUc6PNxkBU1sy3KuIINZHMCzNk8LjXMNbAViBXu4LhD6tFNvBJJEGZK8yTQRuFzgf6DQH2CNBB5IIOVTGMaQDHMLHhIVwJq_0kkm-qM5yXdKDCNIwrU4CCCSSZ2Nsr03QhcrN4B0psWa2pDR8yaEHs_Nn3eQynlrS2Tv1YpFPMtU8f0mK-U-Zw51DAiL67Q5_4WjqiKWCzet21b8SnVErGzvJwohME7pfVAn9kyAG-LU5QLUIOPH2acjMHjsxEiRv38yRI4xAGOU4zQkzRCrt1gj3W9pNnEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث
: 51 سال رفتار نامناسب ایران!
@WarRoom
حالا چرا ۵۱ !؟ ۴ سال آخر شاهنشاهی هم قبول نداشته ؟!</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20746" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20745">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766d8dae53.mp4?token=s6mNdycfVae2S9QAEcllC0ExtNJKIJA3iOAfZfOdWtOQ0aQZwyHS4Ab12AwfFrc-kQIjS3Gz4afdHYfLvR0kPlnUiAajs-UPhX0dIbu_oIH6aGp3oZ28p4qFGrK2fCC5qL28qOAw_zVyX87PtKlRbpr1Uv3S6-UY4LrT16HJS7nnnKKxEI38NrdjjWCnzrMEHJInEsl-f1SEuiCdpSfxJaZoz_WTWe7PrbXBt9ERnVvjY1TPvTATo4FKOq58BXCugIC2F4OKavQMEylf-_WXBO3879MOJ1rHa_ST0UmzEM-J5tJ-pkGhC8Fbc5ZE9JjNlHllQKbG0m_z64-2FGF7bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766d8dae53.mp4?token=s6mNdycfVae2S9QAEcllC0ExtNJKIJA3iOAfZfOdWtOQ0aQZwyHS4Ab12AwfFrc-kQIjS3Gz4afdHYfLvR0kPlnUiAajs-UPhX0dIbu_oIH6aGp3oZ28p4qFGrK2fCC5qL28qOAw_zVyX87PtKlRbpr1Uv3S6-UY4LrT16HJS7nnnKKxEI38NrdjjWCnzrMEHJInEsl-f1SEuiCdpSfxJaZoz_WTWe7PrbXBt9ERnVvjY1TPvTATo4FKOq58BXCugIC2F4OKavQMEylf-_WXBO3879MOJ1rHa_ST0UmzEM-J5tJ-pkGhC8Fbc5ZE9JjNlHllQKbG0m_z64-2FGF7bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش ۴ انفجار در تنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20745" target="_blank">📅 00:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20744">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش ۴ انفجار در تنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20744" target="_blank">📅 00:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20743">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوباره از سیریک موشک ول کردن سمت تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20743" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20742">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izeMhWswI7fjNnjpXUZt9z5L2Vbp8qD5NalHktsVO0H-0O6HyWFlyiCSM5KRei_Kb2Q7HfVDVPitNCF8sZPBkdjb4shY2FcyV9kUMBrW-W3Hasq7ntfih-w4lhU0s_vkIiQC_4sqSnQqWP9s5xxJ5UTuFzBVoJvECbGBbulaHOo3UXucqPtwD1Um6JCkjz6KZC9bQxQniJGRIbhoAQ04mOpTWyvbKBv98L1A7YwuUnvEp2SSJAw1fotEmMciEWNRAVdWDM2Jzs5dilmEek2Rtdvh6YLqNyALmVNQ9AD9jdlW_AliXjTIm_WT9MFaST9mKKg0STxo1a4wVzzZpie34g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک :
یه نفتکش میخواست از مسیر جنوبی
عمان عبور کنه مورد حمله قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20742" target="_blank">📅 00:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20741">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک @WarRoom
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20741" target="_blank">📅 00:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd95915a0b.mp4?token=eBWGBa7gRmNINuvhTA_W1ZkHYNE74J1TI-gihIcLFmA73GaxSJ5WRcfghPHBqdIaTw5eQh5bkkCwKpaEFfk-ho8PIGD0qcxRQ0JSwEdlCR2Hmlm212pl0ZAith_DWjYbV54wy1qtVMCx1syVJNgOeId9ALDAhIp4GvHvpiHsqKA609yuc_aMdqqKSrc3cfQizhuPCDLnlo2lUAUfbxF124qniznRDLiG_31_ilvferhU6Fn2RZDzveprf86dmZ1jQ2C0z28TPZDSRKqD5tyh73rmBpmvcTJcGxAvfaA-kIZ4vOWS2bPrV0yluSHqmTsay5xmpTgTKc_oSvOiIRY9LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd95915a0b.mp4?token=eBWGBa7gRmNINuvhTA_W1ZkHYNE74J1TI-gihIcLFmA73GaxSJ5WRcfghPHBqdIaTw5eQh5bkkCwKpaEFfk-ho8PIGD0qcxRQ0JSwEdlCR2Hmlm212pl0ZAith_DWjYbV54wy1qtVMCx1syVJNgOeId9ALDAhIp4GvHvpiHsqKA609yuc_aMdqqKSrc3cfQizhuPCDLnlo2lUAUfbxF124qniznRDLiG_31_ilvferhU6Fn2RZDzveprf86dmZ1jQ2C0z28TPZDSRKqD5tyh73rmBpmvcTJcGxAvfaA-kIZ4vOWS2bPrV0yluSHqmTsay5xmpTgTKc_oSvOiIRY9LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
نیوجرسی را ترک کرد و جواب خبرنگاران رو هم نداد، تا ساعاتی دیگه میره دم توالت شروع میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20740" target="_blank">📅 00:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شبکه i24 NEWS: اسرائیل فاش کرد که رهبر حماس، "باسل صالیه" را از دو سال پیش بازداشت کرده است. این خبر پس از دستگیری او در شهر حمد منتشر شد. این گزارش حاکی است که او پیش از این با سنوار و الضیف اختلافاتی داشته است. اسرائیل او را مسئول شلیک موشک کورنیت به یک اتوبوس در سال ۲۰۱۱ می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20739" target="_blank">📅 00:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v360OUe0QeVG2mQWGOI9mIDTFErHYh7VED7cHMIiRtutoD5ZQDcz7UfI6Qc-IcYmK-MMLQ63sOb7uZ1nYl3MVx3qnzv1zA3S5DZeoU0i_xrbihkcLBiZr7FJg4tboVTRxBWteJwDuf63LsCush_TFcNIDBvSdVsNvOJ0jJ9qjWC49NnwCjOsDrjRlUHMUuUARdVZdJdUy4ejNfWIsQzQQckdLK0VFS4ACPOP_tkeWV439jfeiruYXl1j2wiiM9uUtanjJhc6FoUi3YwX80-C1nK61fmaFMpBiePfut3Fa9p0yA7nZjCoXBgnpNI-IGZef-UBZ1rT7jkyQ8vXiH5kmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت پیشرفته‌ترین نسخه عملیاتی خانواده E3-Sentry (آواکس)  بوئینگ E-3G Block 40/45  از پایگاه رامشتاین آلمان به سمت منطقه خاورمیانه،
با مشخصات :
قوی‌ترین ارتقای انجام‌شده روی E-3.
رایانه‌ها و نرم‌افزارهای مأموریتی کاملاً نوسازی شده‌اند.
توان پردازش اهداف بسیار بیشتر از مدل‌های قدیمی.
لینک‌های داده و ارتباطات پیشرفته‌تر
و موارد بکلی سری بسیار زیاد انجام شده
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20738" target="_blank">📅 00:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20737" target="_blank">📅 00:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=Jkg_Q7OfUDYPkDexVsKdMtamjjjSxb1lhsz6JQoHiwPNkiRvhUUA1u9aeTYA08QN4VHSzD7cONSRcJ6VgPyEElt8WF277jgPGLNPEen0W-2DvtoXjY2MCFp2Ex9W2FgfcX99FB1JhIgAvC_-fkk-scIEv_w7g_tdsvQcgOnER810Dl5-O4VR_J0GgUYb8I-ladh3jXLXoBzGtJwh0JREQJxg9EPh6Gn9dMLnlqrnjrlQs0yR7s2jzcz1FI_06ujI1mBmnXLR9iwCkkc0V4vKTDpConkuQDIPl_9_HUrp4nHV7YSTAIsMHBHvhOweKQsxrN1J2_ZHRVG9AB4mXmRKxrJZNmGvqTPbIjdKMRDnHKTpMuVYCpluQTDGJqdDSidysqvs2yy6zY9gM_Lr7rq1Gfjc1nmKT5eQWDQXtIuDPgmBoCTkJfa5t1V_6EaWFjTJv8uv4_ClrVTjZnNk-BzcQRItRK29HsFe2vmzkgLjnDxeOP8v3bB-EHO4TOXPgj9pNEL8pPIS2_L6amZfqx3xKTq3Ut1cIqK99Eoj2PC37NaqeE7OXX4ZqkBwQXeZgyhOj6rxfglf4Adw0NEz7nZGJYNdlGMgHEflX1l9mUukw6U7JAd1uabVWyF3sx7Sr11rJSnFti5xzG9IMVJO_rzFoOnIe8LUv7Fve7CuZw6C544" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=Jkg_Q7OfUDYPkDexVsKdMtamjjjSxb1lhsz6JQoHiwPNkiRvhUUA1u9aeTYA08QN4VHSzD7cONSRcJ6VgPyEElt8WF277jgPGLNPEen0W-2DvtoXjY2MCFp2Ex9W2FgfcX99FB1JhIgAvC_-fkk-scIEv_w7g_tdsvQcgOnER810Dl5-O4VR_J0GgUYb8I-ladh3jXLXoBzGtJwh0JREQJxg9EPh6Gn9dMLnlqrnjrlQs0yR7s2jzcz1FI_06ujI1mBmnXLR9iwCkkc0V4vKTDpConkuQDIPl_9_HUrp4nHV7YSTAIsMHBHvhOweKQsxrN1J2_ZHRVG9AB4mXmRKxrJZNmGvqTPbIjdKMRDnHKTpMuVYCpluQTDGJqdDSidysqvs2yy6zY9gM_Lr7rq1Gfjc1nmKT5eQWDQXtIuDPgmBoCTkJfa5t1V_6EaWFjTJv8uv4_ClrVTjZnNk-BzcQRItRK29HsFe2vmzkgLjnDxeOP8v3bB-EHO4TOXPgj9pNEL8pPIS2_L6amZfqx3xKTq3Ut1cIqK99Eoj2PC37NaqeE7OXX4ZqkBwQXeZgyhOj6rxfglf4Adw0NEz7nZGJYNdlGMgHEflX1l9mUukw6U7JAd1uabVWyF3sx7Sr11rJSnFti5xzG9IMVJO_rzFoOnIe8LUv7Fve7CuZw6C544" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) اعلام کرد که جنگنده‌های اف-۱۶ این فرماندهی، چند هواپیما را در نزدیکی باشگاه گلف ترامپ در بدمینسترِ ایالت نیوجرسی رهگیری کردند؛ زیرا این هواپیماها بنا بر گزارش‌ها، محدودیت موقت پرواز اعمال‌شده بر فراز آن منطقه را نقض کرده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20736" target="_blank">📅 23:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانال ۱۳ : اسرائیل به فرمانده سنتکام اطلاع داده است که در صورت توسعه برنامه‌های هسته‌ای و موشک‌های بالستیک ایران، به ایران حمله خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20735" target="_blank">📅 23:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به گزارش اکسیوس، توافقی برای کنترل عبور و مرور از تنگه هرمز بین ایران، عمان و ایالات متحده مورد مذاکره قرار گرفته، اما چندین روز است که در حالت تعلیق مانده است.
مقامات آمریکایی می‌گویند اختلافات فزاینده‌ای در درون رهبری ایران وجود دارد. گفته می‌شود یک ساید به رهبری رئیس جمهور مسعود پزشکیان، به طور فزاینده‌ای نگران فروپاشی اقتصادی احتمالی است و معتقد است که تهران به توافقی با واشنگتن نیاز دارد. ساید دیگر به رهبری فرمانده سپاه احمد وحیدی، با امتیاز دادن به ایالات متحده مخالف است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20734" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20733">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دونالد ترامپ، به آکسیوس گفت که ایالات متحده در قبال ایران «فعلاً با سر و صدای کمی پیش می‌رود»؛ اظهارنظری که نشان می‌دهد واشنگتن اجازه می‌دهد فشار اقتصادی افزایش پیدا کند.
ترامپ گفت: «ما فقط به‌صورت نیم‌بند با آنها مذاکره می‌کنیم. ما فقط داریم ایران را زیر نظر می‌گیریم؛ با این تورم شدید و این واقعیت که پولی ندارد.» او با اشاره به وضعیت اقتصادی ایران مدعی شد که این کشور «در شرایط بسیار بدی» قرار دارد و در پرداخت حقوق نیروهایش با مشکل روبه‌رو است؛ آن هم در شرایطی که محاصره دریایی آمریکا فشارها بر ایران را افزایش داده است.
ترامپ درباره رویارویی با تهران گفت: «همه‌چیز درست خواهد شد. همیشه درست می‌شود. این مثل یک بازی شطرنج است.»
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20733" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20732">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اکسیوس: میانجی‌های قطری و پاکستانی اطمینان داشتند که این توافق روز
چهارشنبه
اعلام خواهد شد، اما از آن زمان، چشم‌انداز دستیابی به توافق کمرنگ‌تر به نظر می‌رسد
یک مقام آمریکایی مدعی شد که حدود ۸ میلیون بشکه نفت هر شب از خلیج فارس از مسیر کریدور جنوبی تنگه هرمز و با هماهنگی ارتش آمریکا خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20732" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20731">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl3_cVUJVd9dUteObx_9AkdEfBoLY9bY_p3-mNa8mbD0YHSelMteuhgEUmfarDcq9PXS3rxFJAo6Nag9B4hYUw3gJb16R4c_hm6V4VdCWOyROQAgmeOvIQ7Z0LSJgTnHnTj9ujib5yuxoUUGQ1gjBhI-l-WqA-ZlzkpDlXRQUYP46e2adgh3XL4nTITBpeSYdIw96cLSyyKEac-x-4VG5nYdungFyCLWt_3G_ajWj692A-aUADt5taJXnmqkwW7v-MjFGGkf5lme8o7qTR22dN3mN_oEkPzWfv8E2T1rOIKxLxPp5BpADbxBVBWuAVOsl32WHlaEVx0DgmO199X1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : جت‌های جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در آسمان خاورمیانه گشت‌زنی می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20731" target="_blank">📅 19:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20730">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حسن قشقاوی، سخنگوی کمسیون امنیت ملی مجلس، اعلام کرد کلیات طرح «اقدام راهبردی تامین امنیت و پیشرفت تنگه هرمز»، با اجماع همه اعضای کمیسیون حاضر در جلسه به تصویب رسیده است.
- کنترل بسیار بیشتری بر تردد کشتی‌ها در تنگه هرمز اعمال کند.
- برای برخی کشورها یا محموله‌ها محدودیت یا ممنوعیت ایجاد کند.
- برای عبور کشتی‌ها نظام مجوز و در برخی موارد تعرفه یا عوارض در نظر بگیرد.
- از تنگه هرمز به‌عنوان یک ابزار فشار سیاسی و امنیتی استفاده کند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20730" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20729">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رئیس مجمع تشخیص مصلحت نظام:
به هیچ قیمتی از موضع خود درباره تنگه هرمز عقب نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20729" target="_blank">📅 18:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20728">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=EriXZMRzyFQrLYIKJm_gvrHAhVmfK71mYq67QE699h0009Z7vDmHVU-cae7VemwiqYNY9IBSWGR5ANaMPoqDSYfU5cJtqbxBOEP4UvrWkett7hnbb2GDarLdQZuoarb-Ihs_UOTux8-CVJqrHyftdM2XIO8d3QoKqn5awzKBgPZxtJOvSMfyCfczu9J8C0KD0W-kg0WFkV0p9aqGLF3ih4d6hTt72RJIOVFEhH4hl-q6R3AfwDWpiCQLAI1CghRdK0KQuTzCcPo-sd3aMvGkMtSrFF7IFUc0oNQyh0IGKrpz5mFO5YSFyl6YFRC7-NAqZh5qoHxUeBW_MvE5z2JGJBJQXAOFsW1GIxfcRen_ye_32ZfoBN0u6yQ6j2JOJXvWk5UQ5ig0Mkc7fGlbvWUauKvet6oIcGJYfEeU2uBMsQDWg6WGjdUEmOP_lowI0ci9DT_IktiX6yT7kTGZKqjSR2jhiJlOf-1GfPsvi53KXEJzGtA0J4EMqWUs6lxBwAfJrHUyQdLItZZIu3ODp92yTKOTklrGVtF1xz-4PrETVKzFqK42_f46Pboe0KIDsEjNtZrafpnIJxPtfyh0G6nev1CYHiFupbZ_jNZvrqtkTlYdZX6Kz5hIumh6qv4eEjx9NME1er3vwvnbuaB90fhESCYdQgK4vsQX4Dh4BQZVBWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=EriXZMRzyFQrLYIKJm_gvrHAhVmfK71mYq67QE699h0009Z7vDmHVU-cae7VemwiqYNY9IBSWGR5ANaMPoqDSYfU5cJtqbxBOEP4UvrWkett7hnbb2GDarLdQZuoarb-Ihs_UOTux8-CVJqrHyftdM2XIO8d3QoKqn5awzKBgPZxtJOvSMfyCfczu9J8C0KD0W-kg0WFkV0p9aqGLF3ih4d6hTt72RJIOVFEhH4hl-q6R3AfwDWpiCQLAI1CghRdK0KQuTzCcPo-sd3aMvGkMtSrFF7IFUc0oNQyh0IGKrpz5mFO5YSFyl6YFRC7-NAqZh5qoHxUeBW_MvE5z2JGJBJQXAOFsW1GIxfcRen_ye_32ZfoBN0u6yQ6j2JOJXvWk5UQ5ig0Mkc7fGlbvWUauKvet6oIcGJYfEeU2uBMsQDWg6WGjdUEmOP_lowI0ci9DT_IktiX6yT7kTGZKqjSR2jhiJlOf-1GfPsvi53KXEJzGtA0J4EMqWUs6lxBwAfJrHUyQdLItZZIu3ODp92yTKOTklrGVtF1xz-4PrETVKzFqK42_f46Pboe0KIDsEjNtZrafpnIJxPtfyh0G6nev1CYHiFupbZ_jNZvrqtkTlYdZX6Kz5hIumh6qv4eEjx9NME1er3vwvnbuaB90fhESCYdQgK4vsQX4Dh4BQZVBWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فاکس نیوز آپدیت آخرین تحولات تا دقایقی پیش…
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20728" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20727">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mccumd3Hpiy8M1v1QgYgaHL15_fPT_EkU65B6P2d3lTrhBmwq_mDHj7TEU6ihccYb6kJL7cEZ08RjtMu_tCuNCcfg52_wFK_NFPcM2eMneHXvhepPCINrBSsX82LH2abWdMP2qK3-YGwthIMyzZHjcZKKrIxYmg-fBdsj67wruqUV4amfptAJXI6gR_Qrp6wKL_y_dgxzY-D3Gtiah58RxTP3vIiUpZ2FK8LulK2HHlVzZZrEACkE-g4IcgQaA1t-iJ15W5FaH9Oe8UqvNK922UCcbT8sWi2tUo4T0n1ltazGrXyJN7XLLS8SB8NusNA0hqX8aKlDv-_E72D2yzraQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود و صدای انفجار در اصفهان
چیزی نیست بی بی داره خنثی میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20727" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
