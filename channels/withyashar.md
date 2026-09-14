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
<img src="https://cdn4.telesco.pe/file/k6f-ERWH2kmJPX1BwWAfD9yYG7nbP_Wx2KhikuYyNLxTHbCic52kbnwWoPSECjl3WBMjJZCtb5jMzCsydQv0ERqcnIsKM6TkJGcQgO1x4CF2qLUDvPr8KAXhTFAVjqCSdmUHIaghuIzv2CO9WvryewyJBU9T6ZB-NuvezxwUwMIkoumweZFKeIRR2CnZ9Iai3LhY0HcZo7krFfX0bP3-sUejV4dlxmm4jEFSCIQ4NYsQfOASIk0VYtua5sB70d0l2PaG7-FAplUpeS2cpiMHE-WL_7zg5QSVmA_7oxNPjEthgUo5FszORijO8QSsFArmaykc8jCVzra0euV5yPUB8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 23:22:57</div>
<hr>

<div class="tg-post" id="msg-23137">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏ کادو عروسی برای داماد در یمن @WarRoom</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/23137" target="_blank">📅 22:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4ccf5e55.mp4?token=cykZ3JcPJFnT7zBPpruYiVkvLW2JnA2S7hu0FLHexPEOG-C9afTbR5rD0rCOzoZytIAv4gLDWPkqCCd4DoLO_S-R3boR32BDuN-nxruDK6OtavNp8md8S1_mjQXzyTt1WCmVS76c_xISiun5AABFfLpnCAdha2Z040lyG7EX6sssviumpmxAMJ-HEDDaTvSJe5Lh5fqiigBaTke0Hs2vb-RZeGG9II9GnP95blI46LmIjkZEa_r82EnQFYLmxQZ_MzkeRHrDPLUuo__MSvvJHxSKHr8YBbzH_aXi5OLt4JB6-O0RNyr-vX0ifXNmzDyLjbBaS4n3HUBws044AXJwlQ7j3Qy_ST8Jeb9bA3Q6d0KBQtwamxzFKM4gS_SqAaTemEiLpqDGTDSugeNQC4QdBYf3Rder5eDiHSu1AktcK5fCLuMlo0Eq04HdKZ19nfnWaklTCUPyvAP28e8pukOgsAHbZTmKnu_70sOo_XPWDs3i7UhvDEGqjTk3rY2NFU1aalmEIvIuWo8LIkYjmXE5kpPB6yiiRHBpcvOGe2TkiHBg0xlyLHdvIvYAjLKxXQn5DmHZ9P5T8AvpV31P96U7xINDFFTdGUXF_2x6ApzwiAcHSzeUW7t8YJMYprIWJb3X6t1BsaK_rMkCKMQsK9uPh4P-i5DpHst-u12EBUMvz-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4ccf5e55.mp4?token=cykZ3JcPJFnT7zBPpruYiVkvLW2JnA2S7hu0FLHexPEOG-C9afTbR5rD0rCOzoZytIAv4gLDWPkqCCd4DoLO_S-R3boR32BDuN-nxruDK6OtavNp8md8S1_mjQXzyTt1WCmVS76c_xISiun5AABFfLpnCAdha2Z040lyG7EX6sssviumpmxAMJ-HEDDaTvSJe5Lh5fqiigBaTke0Hs2vb-RZeGG9II9GnP95blI46LmIjkZEa_r82EnQFYLmxQZ_MzkeRHrDPLUuo__MSvvJHxSKHr8YBbzH_aXi5OLt4JB6-O0RNyr-vX0ifXNmzDyLjbBaS4n3HUBws044AXJwlQ7j3Qy_ST8Jeb9bA3Q6d0KBQtwamxzFKM4gS_SqAaTemEiLpqDGTDSugeNQC4QdBYf3Rder5eDiHSu1AktcK5fCLuMlo0Eq04HdKZ19nfnWaklTCUPyvAP28e8pukOgsAHbZTmKnu_70sOo_XPWDs3i7UhvDEGqjTk3rY2NFU1aalmEIvIuWo8LIkYjmXE5kpPB6yiiRHBpcvOGe2TkiHBg0xlyLHdvIvYAjLKxXQn5DmHZ9P5T8AvpV31P96U7xINDFFTdGUXF_2x6ApzwiAcHSzeUW7t8YJMYprIWJb3X6t1BsaK_rMkCKMQsK9uPh4P-i5DpHst-u12EBUMvz-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ کادو عروسی برای داماد در یمن
@WarRoom</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/23136" target="_blank">📅 22:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxGjy2tHhkS5zrH4v6VuAQav8zS45BOj5GHYD-Pu0Px2j8f1GToFE1-YsBkxTV8zWnlr9vs-jDpo5IoShoTknvIenL5jDhAEMa9GcgqD4ejw0AlIx84KnClZ1ACFyj2MWkm1l4HKYoe-D5x0lwKuKoCnLGJYe8XELp-XdauuA0FeNipJ2tRPnVJD7X_zOOkS7xmau9nTe0NPUNqAf2co_Pt_mB_HwzxUjzLtm2ie-TWhlldr3B1fhQkIOuEq420jkTM5Ao0quHyLwu-TDKUrObpS-I9WveNAoCDUQ_bizmit1gG3a6hdEWinIDjdBF89J2sQkPKJlERc8rLv_wnQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه :
تنگه هرمز مسدود است و همچنان تحت کنترل هوشمند نیروی دریایی سپاه  قرار دارد
یک تانکر نفتی بزرگ به نام «EL GAIA ال گایا» پس از برخورد با مین‌های دریایی در حین تلاش برای عبور از منطقه ممنوعه در جنوب تنگه هرمز، منفجر شد. تلاش‌ها برای مهار آتش بی‌نتیجه بود و آتش به طور کامل تانکر را از بین برد
پیش از این، از خطرات عبور غیرقانونی در این مسیر، هشدار داده شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/23135" target="_blank">📅 22:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا تحریم‌های مرتبط با ایران را علیه بانک «وی‌تی‌بی» (VTB) روسیه اعمال کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/23134" target="_blank">📅 22:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نخست‌وزیر بریتانیا در حال بررسی درخواست عربستان برای حمایت نظامی در برابر حوثی‌هاست»
طبق گزارش، درخواست ریاض شامل کمک برای
دفاع از زیرساخت‌های نفتی عربستان و جلوگیری از پیشروی حوثی‌ها به سمت باب‌المندب
است. بلومبرگ می‌گوید برنهام در واکنش اولیه، با
اعزام مشاوران نظامی بریتانیا به عربستان
موافقت کرده؛ اما این به معنای ورود مستقیم نیروهای بریتانیا به جنگ یا آغاز عملیات رزمی نیست.
@WarRoom
حقیقت یاب اتاق جنگ : نیروی دریایی سلطنتی بریتانیا از قبل در منطقه حضور داشته و در عملیات‌های دریای سرخ نیز ناوهای بریتانیایی مشارکت داشته‌اند ولی خبر
اعزام ناو بریتانیایی جدید مطرح نشده ایت و جعلی میباشد</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/23133" target="_blank">📅 22:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23132">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فاکس‌نیوز: حوثی‌های یمن طی سال‌های اخیر یک
شبکه مالی چندمیلیارددلاری
ایجاد کرده‌اند که به آنها اجازه داده با وجود تحریم‌های آمریکا، منابع مالی لازم برای ادامه عملیات نظامی خود را تأمین کنند. این شبکه شامل
قاچاق نفت ایران، کنترل و بهره‌برداری از بنادر و گذرگاه‌های تجاری یمن، شبکه‌های حواله و انتقال پول و استفاده از رمزارزها
است. بر اساس این گزارش، حوثی‌ها بخشی از درآمدهای خود را از مالیات و عوارض اجباری بر کالاهای وارداتی و فعالیت‌های اقتصادی در مناطق تحت کنترلشان به دست می‌آورند و از شبکه‌های مالی غیررسمی برای انتقال و پنهان کردن درآمدها استفاده می‌کنند. حمایت مالی و لجستیکی ایران نیز نقش مهمی در حفظ این ساختار داشته و این شبکه اکنون به یکی از منابع اصلی تأمین هزینه‌های نظامی حوثی‌ها تبدیل شده است
@WarRoom</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/23132" target="_blank">📅 21:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol8b72MEGWLr-3VZIcfdAsw7A1KbU_u6jd8eUgw_9euPX8Hh4cPvVdGrr5JswN1u2XABlrawsuq8F_S9_-cqwNEeGg3zHhtXWrNg7hQtX_zBSEVQUK947ZnHCsfdHnkJ4Onte_DhC-sAmPgXSfcS03He852YNzNWoEQke7nzq0Ob6q47vSP7dKaNcB1FTwLvRy4RBd-3YOA-1m8SoHCSteSEeAcQ9QlGn95O4vTJCQmU9pDwzao3J5SgRUWNkOgj-CdSLSz6A7gOyCvtUv0UVjEKlMRJ3-QtngH_7TXlLF-WR2j28Who_pIokGtaYq9J479zIK4ckF_Pmw4V_scFyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : قایق سپاه که تو سواحل جاسک هدف قراره گرفته بود رو معلوم نیست چرا از زیر اب در اوردن و دارن میبرن جای نامعلوم، ی طرفش کاملا متلاشی شده
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/23131" target="_blank">📅 21:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMJ_s_oN_Gc90W5Xy5ciXM3GV7bbe1sC7K_Nw9ZObYeT4JU3yLqdwdU1uRjdBeY--aGH8Gx7b4z71vEf9gKxs0nxh0PrluSNCbsEmUeu2ml7Ln0tNnmCikOBh7gSEEab4MuWDkT1KSjbGfzaXSRdub2QkaKye8AGjuSMu4qjc5CHmEsDSWAPU1vvndEgUrLwS055wjGR_xbDopdJElDhLUSMA8v1zLlHwlC_B5yQeu4Lpp6CX4V3_IxvnQq93bLt2iRRY5Ov4f2HHjcFu2efncJk-o9CGFPIU4sizQ8xoo--hlSl6rj4j00uBtroZgvYUOcGGFYbjPh5109aH-Hqag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به هلاکت رسیدن
امام جماعت مسجد محمد رسول‌ زاهدان
با نام
یوسف گرگیچ
توسط افراد ناشناس
گرگیج امروز کمی قبل از کشته شدن در مراسم تشییع شهدای امنیت سپاه پاسداران حضور داشت و این تصویر مربوط به آخرین مصاحبه وی است.
@WarRoom</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/23130" target="_blank">📅 21:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23129">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبرنگار العربیه: هم اکنون نیروی هوایی اسرائیل شهرک کفرتبنیت در جنوب لبنان را بمباران کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/23129" target="_blank">📅 20:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بعد از این خبر نفت رو به پایین شد هم اکنون ۱۰۸$  @WarRoom</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/23128" target="_blank">📅 20:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23127">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏نیروی هوایی عربستان سعودی تصاویری از حملات هوایی علیه اهداف حوثی‌ها در یمن منتشر کرده است. @WarRoom</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/23127" target="_blank">📅 20:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23125">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق جنگ با یاشار : در درگیری امروز گزارش شده از دیدبان اتاق جنگ ,
۲ قایق تندرو سپاه که از اهالی کرگان(میناب) بودند(اکثر این اهالی با حکومت هستند و پاسدارند) عصر امروز هدف حمله آمریکا در تنگه قرار گرفتن ۱ جسد پیدا شد و ۳ نفر  دیگه فعلا تا این لحظه نگارش این خبر مفقود هستن
ترامپ در روز های اخیر چندین بار تاکیید کرد که نیروهای آمریکایی روزی بیش از ۲۰ قایق تندرو سپاه را منهدم میکنند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/23125" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAqp2_Kzqs4uH9uw-H7Wsyl2XfvRg0EBT2MiB1FL0e4RFSJWATa9-LapKKd_0umjGpAPWsccJXRi1hfIX4IrjsM9yOw9jDJqx4b64DEsCRB2xgiP8dVPtziEeaIif3xF6qTMRoCF34cFpjwzfcgf0deObxejKAHoz19bVKEIndO8l6NPBsNp8e3nSI24Q46qDQSx5SmuAJnfTf0Xz8E7Rwwhusbh4YLDMTurMJUn6pncM5RhQlBYaBNlvxNMwJ612at-WyM1dqn7ydWohW1IxsCCeYjm-wwZbhBe029_O4ZnBoD3pipxY6iAIU7k1pkm5T9dE74ceJmsAvK3xvIWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث: «نفت در حال عبور از تنگه هرمز است. کشورهای جهان که هیچ کمکی به ما نکرده‌اند، باید و خواهند داشت که پس از پایان این
درگیری فریبکارانه
، هزینه‌های آمریکا را جبران کنند. ما در این ماجرا بسیار بیشتر از آنکه برای خودمان اقدام کنیم، برای دیگران انجام می‌دهیم؛ همان‌طور که نسل‌هاست این کار را انجام داده‌ایم.»
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/23124" target="_blank">📅 20:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P91_6PrqZzb_14E_X1QnjcGLbZTziNKmFjczGvVkmw43FABLcqJpMYFEGI9F6u5bRNyw9tXncegFsWeNG4DseunKJsCTD8bFi01simxE6GgrcdxVSciGdcPY1oORPRgCOj5crYopyUP_agM2C706y6LOtqeftt1vgbV4bzG4x1S5dPG1PluC5aal1lv_58V5dAXgcoG3l2jE5bJ4VhEz7XH2uu94MoCQB40RCe1KuQa81cQfYQcJPZI9a64O8QTqsd3n8ZlIvds2okOYWmZQHmVI0HOVmS175hGApIMFraq0n38SG_0BgI1e8kgwZFAI2gEORr2VoLom8cmBCTK7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : «به‌تازگی گزارشی دریافت کرده‌ام که نشان می‌دهد ایالات متحده در حال تولید
پیشرفته‌ترین و ممتازترین تسلیحات
با نرخی بی‌سابقه در تاریخ کشور است. این تسلیحات هر روز به نیروهای ما در خاورمیانه و مناطق دیگر تحویل داده می‌شوند. کارخانه‌های صنایع دفاعی ما به‌صورت شبانه‌روزی فعالیت می‌کنند و هم‌زمان، به‌طور میانگین هر شرکت در حال ساخت ۴ تا ۵ کارخانه بزرگ و کاملاً جدید است. تمرکز اصلی این تولیدات بر
سامانه‌های پاتریوت، سامانه‌های تاد (THAAD)، موشک‌های تاماهاوک و دیگر سامانه‌های موشکی استاندارد
است؛ تسلیحاتی که همین حالا نیز تعداد زیادی از آنها را در اختیار داریم.»
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/23123" target="_blank">📅 20:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J413rIHNM8WsHGwD6rNUu0ybUFZ_xWfGrE1JXDZFw02gcp4dxvbCdiuSSVzcKz12nspRYZGWN3k_pgEKSDc1b09MM4scoUcfy_Cmjc8VnMCwBul0S4FhL6wE2htC6-bse56TLBu018_2mT3TDMpYWr0NXvM1rqxhcRw20Z0MAusUpfd3UYVtQgHBiYy8uTiNQfULMmBmVXM8CUeFdGtcKxflPaBaxGGEHhCxzPHqyqTJQaje4507iz2om36GLexZx6r5OiOKHEzgHpJpKfIiMCEWjE1v2Jwa4dI60nCyyuH7mouMjRguDKwtpXgOXyOswOOebBn7oYJ9r4Epz9mV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای E-11A متعلق به سیستم‌های هشدار اولیه و ارتباطی، از پایگاه الامیر سلطان به سمت عراق در حرکت است. همزمان، یک فروند هواپیمای P-8A برای عملیات شناسایی دریایی در حال پرواز بر فراز خلیج عمان است. همچنین، سه فروند هواپیمای تانکر در حال سوخت‌رسانی هوایی در آسمان امارات و خلیج عمان هستند. علاوه بر این، یک فروند هواپیمای MQ-4C در حال انجام مأموریت‌های شناسایی و نظارتی بر فراز خلیج فارس است.
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/23122" target="_blank">📅 19:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23121">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l16bZEq5k9BIGeDhbL4JkFkurqjLiRMJbPQx7_17x4Q87I3jbj77FD_N2kGt9nNYHoCJKkF5-75FdNLj-E_SvjCc_4KPPJc_GeA8vzINXX74MjQRGfvf_jwBAUB902875IYfp1jdsn2tNREd6VDw1r0VRgHVT6eIFiyP5_2-B8faPwUrribPm6NGP0SzTiX9ykAo8Kq9UPZIl28PpbyVmPJL1o0UaVo4BPIXT_PGFhTD9T5LkD-Hd1LQWxXSsIKjycd44YQFwn6MSyD6dgHWxDhqpSYSwTzODnom7WHV3G4o2DF670hpd3fTLti7xcyBUdO-1VfP0LXh04S1K3J6Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب اتاق جنگ : این عکس امروز توسط ادمین های زرد تلگرام با عنوان جعلی تصویر ماهواره‌ای سنتکام از قایقهای تندروی سپاه منتشر شده بود.
این در اصل تصاویر ماهواره‌ای گوگل ارث مربوط به ۱۸ فروردین ۱۴۰۵، یک روز پیش از آتش‌بس اولیه جنگ ۲۰۲۶ ایران است، دو فروند قایق تندرو را نشان می‌دهد که به‌صورت نسبی میان درختان در جزیره خارک پنهان شده‌اند. این شناورها احتمالاً متعلق به نیروی دریایی سپاه پاسداران هستند.
لوکیشن : 29.261371, 50.318697
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/23121" target="_blank">📅 19:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بعد از این خبر نفت رو به پایین شد هم اکنون ۱۰۸$  @WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/23120" target="_blank">📅 19:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، اسکات بسنت: وزارت خزانه‌داری عملیات «طرد اقتصادی» را آغاز کرده است تا تمام شریان‌های مالی حکومت ایران و تسهیل‌کنندگان آن را قطع کند. به همین دلیل، من فراخوان جدیدی از افشاگران منتشر کردم تا اطلاعات خود را درباره افرادی که به اقدامات تروریستی ایران کمک می‌کنند، ارائه دهند. از هر فردی در سراسر جهان که درباره این شریان‌های مالی اطلاعاتی دارد: این فرصت شماست. اگر اطلاعات قابل‌اقدام و مفیدی برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید؛ مهم نیست کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند. اگر چیزی دیدید، گزارش دهید.
@WarRoom</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/23119" target="_blank">📅 19:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb3ch2ftZSxdcNfzRFT2PU6K4wCXfc_LMHpnvmaDhaTBSQjAwi0YqFtPtVHY-4kq233Lg_A8AqXiNFRwIiMROticr2-8kyZfJX_zfUZ_xNhmKCb8wPA3ge3fJf8-G4tqxsBPULkXAKedZ2Vz-jRbT7SEzzokCDQb3mUNpWTgtjYSncFA7jMC8a-TlBY1h4yR4bOAH_iXUXizQ2bDZy96charmd7rvMz1ibXTHNEOYB1-Ba8yVTfBFWY_nqg130DfKuiWdui3qKeyw6b5Do3aA1Vnyk47qQr-OHlqYkVhATV6wLtOdjyH7WdtTXnRmIb9dKVOdJqy0H6PqTQJB-sN_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: کشور در حال فروپاشی ایران می‌خواهد
سریع و به‌شدت
به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا تصمیم به ورود به مذاکرات خواهد گرفت یا نه؛ مفهومی که ما نسبت به آن
روی گشوده داریم
. از توجه شما به این موضوع سپاسگزارم!
@WarRoom</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/23118" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ در‌تروث : اوکراین و روسیه موافقت کردند حمله به زیرساخت‌های یکدیگر را متوقف کنند ، افزایش قیمت گازوئیل بیشتر ناشی از جنگ روسیه و اوکراین است نه ایران.‌‌ @WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/23117" target="_blank">📅 19:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4424213714.mp4?token=ZyiX4bNF5Z8OXL1u5aiiJrJwt6kiAEcN9IL_j8RPJdgzFQmZKxEvhhHV6WzRt38eYslt47yenBdfUALVFeHldmpMauB24INkdP3RpHGB96SFWKHcr-L0s0FBinTsGuSkE-w8rhUI2DXXiFMw5PHIC-mTy7oPTvteBn_x8Ja2SnwG0_P5-oh6YOgvsy_PmAjVpt8rkYZSVtDs8SOcKXuhveSB6g98CoBp-RXRCSBS-fMsuzqUvNZiw0c1sZN1qPGJk42OU1JNNl1uXjB-pEeLJSp2-UHqnPndifH8K15EeMEUDfJD4B-DwfRze-HMNsSu8oLO0TVOvmIiI7KpNIHFabLj4Pm3Q6xBP1OUuutZ1Z7lm4-v-ASeCiBXFxJV5qz6HBTmBwyCGh2K9g2Cn0ybvRZD-tnRdlDo_2Bv7MeKXXg9xV8OwJg6MMyWbXbHQawgbsztw6cMobi4qblTb4EolezbgegWL_mZO0-ITXs0qDEFgx4GHBRsY5VCfCsCkcDRhV-7Q_4NXTSN2qzpzpy2FdIJMbyzMVWoaNdOB-n34hQAP4wCrgv5HwnUBz4Lbvyqqf55CNrHPd3J4nGdJK4be_lWtotNpDSabTufCOjMzLCXyFtQul4IzrbKVmkQFb5jGVg_GKtDfw1V7Wl_GzB_APA0xLQOfOATmG30bVh7geE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4424213714.mp4?token=ZyiX4bNF5Z8OXL1u5aiiJrJwt6kiAEcN9IL_j8RPJdgzFQmZKxEvhhHV6WzRt38eYslt47yenBdfUALVFeHldmpMauB24INkdP3RpHGB96SFWKHcr-L0s0FBinTsGuSkE-w8rhUI2DXXiFMw5PHIC-mTy7oPTvteBn_x8Ja2SnwG0_P5-oh6YOgvsy_PmAjVpt8rkYZSVtDs8SOcKXuhveSB6g98CoBp-RXRCSBS-fMsuzqUvNZiw0c1sZN1qPGJk42OU1JNNl1uXjB-pEeLJSp2-UHqnPndifH8K15EeMEUDfJD4B-DwfRze-HMNsSu8oLO0TVOvmIiI7KpNIHFabLj4Pm3Q6xBP1OUuutZ1Z7lm4-v-ASeCiBXFxJV5qz6HBTmBwyCGh2K9g2Cn0ybvRZD-tnRdlDo_2Bv7MeKXXg9xV8OwJg6MMyWbXbHQawgbsztw6cMobi4qblTb4EolezbgegWL_mZO0-ITXs0qDEFgx4GHBRsY5VCfCsCkcDRhV-7Q_4NXTSN2qzpzpy2FdIJMbyzMVWoaNdOB-n34hQAP4wCrgv5HwnUBz4Lbvyqqf55CNrHPd3J4nGdJK4be_lWtotNpDSabTufCOjMzLCXyFtQul4IzrbKVmkQFb5jGVg_GKtDfw1V7Wl_GzB_APA0xLQOfOATmG30bVh7geE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: سیاست ما روشن است: ما به تخریب زیرساخت‌های تروریستی در «منطقه امنیتی» در لبنان ادامه خواهیم داد و به رفع هرگونه تهدید علیه دولت اسرائیل ادامه خواهیم داد. به دشمنانم می‌گویم: اگر تاکنون درس را نیاموخته‌اید و تصمیم بگیرید که دوباره به ما حمله کنید، ضربه‌های سنگین‌تری را متحمل خواهید شد. کارهای بیشتری برای تکمیل باقی مانده است و با کمک خداوند آن را به پایان خواهیم رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/23116" target="_blank">📅 18:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJG45jXT_iep1LaMr-gYVfbUSlrcNxPjfeT5kPzMyU-HlJrzyhvfU4DZVkORvUVT2IRsu07kZSLIbAUZ0u9YmFyg4LKvpQbPRoz81I3LAyEccGj10kfGp32uGsG_QsJGV_SRARRDSES148O0ZX2avn3k1dgXPW8vZI5vMzKjCK7G3kb7BUj4bzZaDBbeVyII9uzaoOxE1RfTf9e4g6huQmG7v1ZB_OF2B6_PbPsBqyeSRLB2PnM5hczw-YwBay-Hay4yLeLxqV6cuR7j8WSjWcNSZ4dyD8CmTTKvHwcUVio5x1vWG8rxX6Hk0BeABymjAjZ5v8A42t2f04VlDQJr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ
در‌تروث
: اوکراین و روسیه موافقت کردند حمله به زیرساخت‌های یکدیگر را متوقف کنند
، افزایش قیمت گازوئیل بیشتر ناشی از جنگ روسیه و اوکراین است نه ایران.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/23115" target="_blank">📅 18:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7da56100a.mp4?token=r5uvqFPY742Fzgm-2uZs5B5rNzusEPfvFPhPL4AIdje36v7K1AVoep779ryp2T3UwFrbl5jvnjZ_IK2VGe7Lik11KX2mSDmCZHRnMdbMj0caHCZ71Z6FlkziScG3nEL9x1J5jyCoLlGntzaeSEcWgXKsehwgLX3Cz_08YDOHRiI6ZKXBZ_2GZ0rKgtx25NIM0igmKS2bVfEKIrs9G0wOjcs8ZejZ3ro9x2zmf8gjZjjvYcqSixfA5NaKkE2lF2Y4pT3qoD5JqwfNV7HNXr6dxVMwgWVvTOttQc0Cysm4LCnkoJwVlfXLgc6ig1MScUdRtN_9r0wkOzfjsmSBXt-6GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7da56100a.mp4?token=r5uvqFPY742Fzgm-2uZs5B5rNzusEPfvFPhPL4AIdje36v7K1AVoep779ryp2T3UwFrbl5jvnjZ_IK2VGe7Lik11KX2mSDmCZHRnMdbMj0caHCZ71Z6FlkziScG3nEL9x1J5jyCoLlGntzaeSEcWgXKsehwgLX3Cz_08YDOHRiI6ZKXBZ_2GZ0rKgtx25NIM0igmKS2bVfEKIrs9G0wOjcs8ZejZ3ro9x2zmf8gjZjjvYcqSixfA5NaKkE2lF2Y4pT3qoD5JqwfNV7HNXr6dxVMwgWVvTOttQc0Cysm4LCnkoJwVlfXLgc6ig1MScUdRtN_9r0wkOzfjsmSBXt-6GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون آتشسوزی در بازار متل‌قو
@WarRoom
یاشار : حتما به بی‌بی مشروب تقل دادن شاکی شد</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/23114" target="_blank">📅 18:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش ۲ انفجار در جاسک و چابهار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/23113" target="_blank">📅 18:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6bvN4J4EJvDZS2AN-hQ_7xSs5_0KIU7kQs4KSBHyHuhKNDand6YNeYbhZCLSWvZJj9bBWAMLMAAFxx7wwSdEuAFj5WUyJvb1Dxas9zFCSbFeMK4H8JF8eaWnFwFq592emi6LoFtujvC6b1RRYqexNG7P_fbUFxh5pD94Yioin-g613OZiqyQXD4GBS2zqzLarIILHrFlms7chl2m1B-MW1tSenLF5CiCMr_4Dsytqu9qMfAVmli09YJI--PR2D5odGv-3O4y6talspoIM7SVyPS0LshDS9UOEeYFae1XrrwOIiGufpAFxgX-yvMBTwp-e8jaU8gEISBuYJa6xg8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: تنها چیزی که هوش مصنوعی به آن برای کنترل یا ایجاد «چارچوب‌های نظارتی» نیاز دارد، یک رئیس‌جمهور
قدرتمند و باهوش (با ضریب هوشی بالا!)
است، و ایالات متحده آمریکا چنین رئیس‌جمهوری را آن هم به وفور دارد! دولت ترامپ جلوی افراد فعال در حوزه هوش مصنوعی را که کارهای بد یا بالقوه بد انجام می‌دادند گرفته است؛ افرادی مانند داریو (آمودی، مدیرعامل آنتروپیک) که حالا وانمود می‌کند یک «فرشته کوچک و بی‌عیب‌ونقص» است؛ و ما به این کار ادامه خواهیم داد! ما همین حالا هم
قدرت‌های گسترده کیفری و نظارتی
بر این شرکت‌ها داریم! یک توطئه
بیمارگونه
علیه هوش مصنوعی و مراکز داده در جریان است و تنها کسی که از آن خوشحال است، چین است.
هرکس هوش مصنوعی را ببرد، برنده خواهد شد!
ما از چین و همه دیگران جلوتر هستیم و به این روند ادامه خواهیم داد. نظریه‌پردازان توطئه، خیانت‌پیشگان، خائنان و افشاگران،
مراقب باشید!
از توجه شما به این موضوع سپاسگزارم!
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/23112" target="_blank">📅 18:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPdfvuFa6YpQIg8QBAK71fEEsyxPJOW1HdLm-3L8OGwj_yu3FPQd_ZZ3WbcN5nW4HnNkS9-DO_1np8C2JRRYoq8LijJ1K8O9ms65qnM0Ktrs_uDOIXpwcd_fnSV8p57nc0ke2MevGwrTc-mXprNSEVvPIb3KwG91hAw6rfVgfySzPH-5S0cUZqsv3XueroJkmiXkNDkmVEwNl9L-iERrPgQ7pB5IF5WcMFWcJyqcxJXElO034bZnJL9SUHRiGz6lUzdqobYb1q01zcVKbK8EaoniFikjTTTesK3N416JMotVK0Q_ISLHL_J9eyGARtpKVTsRP6QdZ5NpgJB8LbcbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت رسیده ۱۰۹.۲۰$ با نمودار هفته های اوج جنگ برابرشده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/23111" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تنگه دعوا شد ، ۵ صدای شلیک/انفجار
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/23110" target="_blank">📅 17:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزارت خارجه چین روز دوشنبه ۲۳ شهریور گزارش‌ها درباره ارائه تصاویر ماهواره‌ای به جمهوری اسلامی پیش از حمله موشکی ۱۷ شهریور به پایگاه موفق‌السلطی در اردن را «بی‌اساس» خواند و رد کرد. مقام‌های آمریکایی گزارش داده بودند که جمهوری اسلامی پیش از این حمله، تصاویر…</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/23109" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23108">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">لحظاتی پیش دفتر نتانیاهو اعلام کرد: نتانیاهو هفته آینده به آمریکا سفر خواهد کرد @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/23108" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23107">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آبان ماه پادشاهان
۱ آبان — منسوب به زادروز نادرشاه افشار
۴ آبان — زادروز محمدرضا شاه پهلوی
۵ آبان — انتخابات سراسری اسرائیل
۷ آبان — روز بزرگداشت کوروش بزرگ
۹ آبان — زادروز شاهزاده رضا پهلوی
۱۲ آبان — انتخابات میان‌دوره‌ای کنگره آمریکا
۱۳ آبان — سالروز انتخاب نام «رضا» برای ولیعهد ایران
۱۴ آبان — سالروز فرمان شاهنشاه محمدرضا شاه و اعلام ولایتعهدی رضا پهلوی
@WarRoom
یاشار : ۲ آبان تولد پدرم هم هست
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/23107" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">زارتان زورتان</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/23106" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96df3d233.mp4?token=kK4yB3LfrCXdvkS6ZJNyp1Y_P6JKMfWxnfR3bPdguiCR9QHDGOfrcZ2Mo9uFNWiDg6ufUUsle7dpapx-mEQiuo4Ya2z6HvEAv2hqcP3PMbUfw_aVEbaB3vLcOxS7j6CNHRQmwmYYNXie9tFIlo2ig_ekdX1ZyQemJAOJ0OYa1yylEJzXO-bvPJEiSh0GLglCru8n3Rb-qUO7PgCrEdtrma0v5rk0YnmtDqiEwvm2Q7DiEaKRbleNAiD7PJpyq7GnCAaqWHZgGC7w6qPE67cM4UJEauw51oRlX_wpgqNg5H6sQD6Bmd4eCLDmPEuVDTjUfx94p_RwebOrpkLAYKW-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96df3d233.mp4?token=kK4yB3LfrCXdvkS6ZJNyp1Y_P6JKMfWxnfR3bPdguiCR9QHDGOfrcZ2Mo9uFNWiDg6ufUUsle7dpapx-mEQiuo4Ya2z6HvEAv2hqcP3PMbUfw_aVEbaB3vLcOxS7j6CNHRQmwmYYNXie9tFIlo2ig_ekdX1ZyQemJAOJ0OYa1yylEJzXO-bvPJEiSh0GLglCru8n3Rb-qUO7PgCrEdtrma0v5rk0YnmtDqiEwvm2Q7DiEaKRbleNAiD7PJpyq7GnCAaqWHZgGC7w6qPE67cM4UJEauw51oRlX_wpgqNg5H6sQD6Bmd4eCLDmPEuVDTjUfx94p_RwebOrpkLAYKW-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/23105" target="_blank">📅 16:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23104">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">لحظاتی پیش دفتر نتانیاهو اعلام کرد:
نتانیاهو هفته آینده به آمریکا سفر خواهد کرد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/23104" target="_blank">📅 16:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">باراک راوید ، آکسیوس :
ساده‌لوحانه است اگر فکر کنیم ایران اجازه می‌دهد انتخابات میان‌دوره‌ای آمریکا بدون ایجاد آشوب برگزار شود. برنامه ایران این است که هر دو تنگه را مختل کند، به خطوط لوله حمله کند و [با این اقدامات فشار ایجاد کند]…
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23103" target="_blank">📅 15:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23102">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer"><a href="https://t.me/withyashar/23102" target="_blank">📅 15:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارشات مردمی از ورود جنگنده اف ۱۸ آمریکایی به جنوب کشور - دقایقی پیش
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23101" target="_blank">📅 15:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزیر انرژی آمریکا در پاسخ به سوال الجزیره: عبور نفتکش‌ها از تنگه هرمز در شب و با اسکورت نیروی دریایی آمریکا انجام می‌شود.
ما کارت فشاری را از ایران گرفتیم، کشوری که تلاش می‌کرد تا کشتیرانی جهانی را به خطر بیندازد.
اطلاعات ما در مورد عبور کشتی‌ها از تنگه هرمز، تخمین نیست، بلکه حقایق دقیق هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23100" target="_blank">📅 14:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5acf092a81.mp4?token=VatXy-dYB3U6F2ruEdyY6rCYEPJ0Qgi9dvxe-jm0easpnNkm7vYr9WBG8ffSuf10AX5jx9CArUEc52uQp32MYRb5W4xMF9O9wwnxNppQm5zvyRLzuGXjEzGbeeieMYKXpjH6Vw0jE2o-xCRj66j2AH-SQxLvYPEM453_vsQMAdP_USe2_QlzvaPq1ThI4tauGZZMi9oPfrjfZXYJ4vFdKNwN_57zhLeT3FbOtJx0c7N8PM9rx5YsCzChn9u-UxANV9Tm2uMg02kq9ATSv3fe-iXQaC65MFVb1IhRqhFTvGMAleQCIVn2bqggFIX0yWaw2QezSvj31Kn38XtfHO-IsoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5acf092a81.mp4?token=VatXy-dYB3U6F2ruEdyY6rCYEPJ0Qgi9dvxe-jm0easpnNkm7vYr9WBG8ffSuf10AX5jx9CArUEc52uQp32MYRb5W4xMF9O9wwnxNppQm5zvyRLzuGXjEzGbeeieMYKXpjH6Vw0jE2o-xCRj66j2AH-SQxLvYPEM453_vsQMAdP_USe2_QlzvaPq1ThI4tauGZZMi9oPfrjfZXYJ4vFdKNwN_57zhLeT3FbOtJx0c7N8PM9rx5YsCzChn9u-UxANV9Tm2uMg02kq9ATSv3fe-iXQaC65MFVb1IhRqhFTvGMAleQCIVn2bqggFIX0yWaw2QezSvj31Kn38XtfHO-IsoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه هند در جریان سخنرانی بی محتوای پزشکیان در اجلاس بریکس در دهلی نو، به خاطر خوردن یک جعبه آجیل خبرساز شد؛ او مشغول خوردن و لیسیدن انگشتانش بود و مدام از ظرف آجیل برمی‌داشت تا اینکه سرانجام کارکنان تشریفات، ظرف آجیل را از مقابل او برداشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23099" target="_blank">📅 14:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رسانه های رژیم
:
با پیگیری‌های انجام شده مرزهای شلمچه و چذابه برای تردد مسافران بازگشایی شد
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/23098" target="_blank">📅 14:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رویترز:
محمد بن سلمان امروز در جده با دریاسالار برد کوپر، فرمانده سنتکام، دیدار کرد
؛ محور گفت‌وگو تشدید حملات حوثی‌ها و تهدید علیه عربستان و مسیرهای انرژی بود. این دیدار پس از درخواست‌های ریاض از ترامپ برای اقدام نظامی مستقیم علیه حوثی‌ها انجام شد؛ واشنگتن فعلاً حمله مستقیم را نپذیرفته اما حمایت اطلاعاتی و کمک هدف‌گیری به عربستان را در دستور کار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/23097" target="_blank">📅 14:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رویترز: پیشروی حوثی‌ها در امتداد ساحل دریای سرخ، موج تازه‌ای از آوارگی در یمن ایجاد کرده و از ابتدای سپتامبر بیش از ۸۲ هزار نفر مجبور به ترک خانه‌های خود شده‌اند؛ سازمان بین‌المللی مهاجرت درباره تشدید بحران انسانی هشدار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/23096" target="_blank">📅 14:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db1ad975d0.mp4?token=Biu9f6OjtgCqC7xqOzZAxdJUK-RIMdApQN6Aw5qLtym25TTB_KKXzv19BNuYsP-jpGCanh3VtPkKc1AKA5xdmjtailfPoLAMZ6NrrcWDvAVy3bFI44pQem_PjX5vYDvcpQ_msgHSLl5T9wqHMsDcCJvF2hvZbj9eMN4BL7Y3_DUu9imOeUb0OwCVwzILJJnT-kl-faic8snel8yWgT0wONRAfWRviHW3UWNQlz5IMlmjGjrpKGLaAHwyPyABFzYCFq-gnsiZikcuP7zHHWM7gxYztFOpwmT4z3nZJFkNOjDQM6zEEL3xbBlykgKmL4j0KNS4j8w4KJAhZih8xbxTgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db1ad975d0.mp4?token=Biu9f6OjtgCqC7xqOzZAxdJUK-RIMdApQN6Aw5qLtym25TTB_KKXzv19BNuYsP-jpGCanh3VtPkKc1AKA5xdmjtailfPoLAMZ6NrrcWDvAVy3bFI44pQem_PjX5vYDvcpQ_msgHSLl5T9wqHMsDcCJvF2hvZbj9eMN4BL7Y3_DUu9imOeUb0OwCVwzILJJnT-kl-faic8snel8yWgT0wONRAfWRviHW3UWNQlz5IMlmjGjrpKGLaAHwyPyABFzYCFq-gnsiZikcuP7zHHWM7gxYztFOpwmT4z3nZJFkNOjDQM6zEEL3xbBlykgKmL4j0KNS4j8w4KJAhZih8xbxTgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت ماهواره‌ای اسرائیلی ISI از پرتاب ماهواره جدید
EROS NOVA
برای مأموریت‌های اطلاعاتی، شناسایی و نظارت با دقت بسیار بالا (VVHR) خبر داد. این ماهواره به سامانه تصویربرداری پیشرفته‌ای مجهز است که امکان ثبت تصاویر با وضوح بسیار بالا و شناسایی اجسام کوچک تا حدود
۲۵ سانتی‌متر
را فراهم می‌کند. یکی از قابلیت‌های مهم EROS NOVA،
پردازش داده‌های خام در خودِ فضا پیش از ارسال آنها به ایستگاه‌های زمینی
است؛ قابلیتی که می‌تواند حجم داده‌های ارسالی را کاهش داده و سرعت دریافت و تحلیل اطلاعات را افزایش دهد. به گفته ISI، این ویژگی‌ها EROS NOVA را به ابزاری پیشرفته برای مأموریت‌های اطلاعاتی و نظارتی تبدیل می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23095" target="_blank">📅 14:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23094">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کاملترین نسخه و با بهترین ترجمه و خواناترین زیرنویس فارسی از گزارش ویژه «۶۰ دقیقه» شبکه CBS درباره عملیات نجات افسر تسلیحات یک فروند F-15E آمریکایی که پس از سقوط جنگنده در ایران، حدود ۵۰ ساعت در خاک ایران مخفی ماند و در نهایت طی یک عملیات ویژه نجات پیدا کرد. این افسر برای نخستین‌بار درباره لحظه اصابت موشک، خروج اضطراری از جنگنده، جراحات، مخفی‌شدن در مناطق کوهستانی ایران و عملیات نجات خود صحبت می‌کند. این گزارش همچنین تصاویر تازه‌ای از عملیات نجات و جزئیات این مأموریت را منتشر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/23094" target="_blank">📅 13:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23093">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e4f0e7504.mp4?token=g87nQ4eVcla33in9ZRibGjcKnM1SUI9AT4MR1xMeJ_ep-KcY7O7PHjCj14UOW8AHPAKLT-Ir3jnMu-VJuITVpw4wLlMhkTNRlRt7ScHcHi4Z5y9Y6d2naEQUyr5vk7p9GQ0b4sxehc9l-ZNlwZNu3BxGQLf_567BWrXb4tKIg2_gcnyO7w3mioX_KLPVjv7VHbOS1gV5ER7uaAHRN5IeRtHKbzLXjAiO-aUmjSEOhVfrp7RYSC9FymMIeuWVa-TTkIwYvitw1uzf76IrCw3O_sXT3uDqf0XvIxGjkGhNzV5RLn3R03MJzBIh3jEOk2yOLG4vs2ivT127eQ7LLI9TBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e4f0e7504.mp4?token=g87nQ4eVcla33in9ZRibGjcKnM1SUI9AT4MR1xMeJ_ep-KcY7O7PHjCj14UOW8AHPAKLT-Ir3jnMu-VJuITVpw4wLlMhkTNRlRt7ScHcHi4Z5y9Y6d2naEQUyr5vk7p9GQ0b4sxehc9l-ZNlwZNu3BxGQLf_567BWrXb4tKIg2_gcnyO7w3mioX_KLPVjv7VHbOS1gV5ER7uaAHRN5IeRtHKbzLXjAiO-aUmjSEOhVfrp7RYSC9FymMIeuWVa-TTkIwYvitw1uzf76IrCw3O_sXT3uDqf0XvIxGjkGhNzV5RLn3R03MJzBIh3jEOk2yOLG4vs2ivT127eQ7LLI9TBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏نیروی هوایی عربستان سعودی تصاویری از حملات هوایی علیه اهداف حوثی‌ها در یمن منتشر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/23093" target="_blank">📅 13:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf59f98ca.mp4?token=p4Q_2yiXQ90NpZ4jF4HIO7u5t39hYD4lVcnjzLBk4cPxLbn41fe0MxET5hjFwW1ZXHT0VCezLADoeTHUEe1OEkUMwpHXmOUgMT_77fqB_TaJlX8sLBJn3BhZbHnXyXjNG1ZEhfwahWPLD0zxLUY0eAJe3pfkAD31T7U6xtLX7PSv357eMueHqg0OP4eFnCWuZkjKPNUHRHHvdnzpiiU77uXvOXR4tJ-xf1OHUHd5GHg5VDh84viK3QdUp_02qMRpmfjg7Zhwi__fLG88Yw9SXXNxNCJGDlW5EQWxIyz9bcsudVqkg3Ivh8mS-uyBKH9M1_AfkK73AAm20YSVxydyDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf59f98ca.mp4?token=p4Q_2yiXQ90NpZ4jF4HIO7u5t39hYD4lVcnjzLBk4cPxLbn41fe0MxET5hjFwW1ZXHT0VCezLADoeTHUEe1OEkUMwpHXmOUgMT_77fqB_TaJlX8sLBJn3BhZbHnXyXjNG1ZEhfwahWPLD0zxLUY0eAJe3pfkAD31T7U6xtLX7PSv357eMueHqg0OP4eFnCWuZkjKPNUHRHHvdnzpiiU77uXvOXR4tJ-xf1OHUHd5GHg5VDh84viK3QdUp_02qMRpmfjg7Zhwi__fLG88Yw9SXXNxNCJGDlW5EQWxIyz9bcsudVqkg3Ivh8mS-uyBKH9M1_AfkK73AAm20YSVxydyDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در گوشه ای از مستند جنجالی نجات خلبان اف‌۱۵ نیرو های سپاه در نزدیکی او در خاک ایران هدف قرار گرفته میشوند ؛ حتی یک نفر از ۷ سپاهی سوت موشک که به سمتشان می میرود رو می احساس میکند و سعی می کنه به افراد خبر بده اما نمی داند به کدام سمت بروند. در نهایت انفجار…</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23092" target="_blank">📅 12:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سازمان بنادر و دریانوردی ایران اعلام کرد
۷۷ کشتی
در فهرست عدم انطباق (NCL) قرار گرفته‌اند و به بیمه‌گران، باشگاه‌های P&I و مؤسسات رده‌بندی هشدار داد از ارائه خدمات به این کشتی‌ها خودداری کنند. بر اساس این اطلاعیه، کشتی‌های متخلف در عبورهای بعدی ممکن است با
جریمه، توقیف یا مصادره
مواجه شوند. همچنین هر کشتی که از طریق انتقال کشتی‌به‌کشتی (STS)، ترانشیپمنت یا همکاری مشابه با کشتی‌های فهرست‌شده همکاری کند، به این فهرست اضافه خواهد شد. ایران اعلام کرده کشتی‌های قرارگرفته در این فهرست می‌توانند برای
حذف نام خود، درخواست فرم رسمی همراه با دلایل و توضیحات
ایمیل کنند؛ با این حال، در اطلاعیه منتشرشده
هیچ هزینه یا مبلغ مشخصی احتمالی برای خروج از فهرست اعلام نشده است
.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/23091" target="_blank">📅 12:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23090">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حمله بامدادی ایران به استان سلیمانیه با شلیک ۵ موشک:
آژانس امنیت اقلیم کردستان اعلام کرد حدود ساعت ۳:۱۰ بامداد دوشنبه ۲۳ شهریور، پنج موشک به سه منطقه در استان سلیمانیه اصابت کرده است؛ سه موشک در زرگویزله، یک موشک در نزدیکی روستای گرگه‌چیا در سیروان و موشک پنجم در حدفاصل داری زاین و میراسی سفلی در قره‌داغ فرود آمده‌اند. این حملات
تلفات جانی نداشته
و آژانس اقلیم از مردم خواسته از محل اصابت‌ها و بقایای موشک‌ها و پهپادها فاصله بگیرند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/23090" target="_blank">📅 12:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزارت خارجه چین روز دوشنبه ۲۳ شهریور گزارش‌ها درباره ارائه تصاویر ماهواره‌ای به جمهوری اسلامی پیش از حمله موشکی ۱۷ شهریور به پایگاه موفق‌السلطی در اردن را «بی‌اساس» خواند و رد کرد. مقام‌های آمریکایی گزارش داده بودند که جمهوری اسلامی پیش از این حمله، تصاویر ماهواره‌ای این پایگاه را از نهادهایی چینی دریافت کرده بود؛ حمله‌ای که به کشته شدن ۳ نظامی آمریکایی انجامید ولی نام این نهادها را اعلام نکرده و دولت چین را نیز مستقیماً به مشارکت در حمله متهم نکرده‌اند. پیش‌تر نیز در حادثه‌ای مشکوک ماهواره شناسایی چینی Yaogan-50 (02) در یک رویداد نادر در مدار زمین از هم پاشیده و دست‌کم ۴۳ قطعه از آن شناسایی شده است. علت این حادثه همچنان در دست بررسی است و تاکنون مشخص نشده که این ازهم‌پاشیدگی ناشی از نقص فنی، برخورد یا عامل دیگری بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23089" target="_blank">📅 12:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eda4cc06e.mp4?token=odtlmWCjAQrV2zbPzcTlcRhkB44Zq_Od6RFiehYsVr9puzFjHEgOwannvsoRiugEx5z6Ucqmy8iZ31NmPLetjjM5EcEvLAY-skuhg84Lx0WTY-OY3YEI7DA79SrzZqEFyBSV9AOXJnMDmqX8g4yBDBhgl7wvmBtrnRRqw3KoPJQTP6mi0J3EaHLIMpq9fSg5pxijpqxrtrBv5T-Wz1fYutqyHH1MgZ3B39E04Bmqn6bPBWCA5Ra9LiUBfxP7Ax6gkPPK_QLbUIFNgBvkktkmTxTIFQb9A-LBuS2kv2PtdCSpSvOg93k05G6lruwBFxbh7zngrWVony5YM4U-VwzYxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eda4cc06e.mp4?token=odtlmWCjAQrV2zbPzcTlcRhkB44Zq_Od6RFiehYsVr9puzFjHEgOwannvsoRiugEx5z6Ucqmy8iZ31NmPLetjjM5EcEvLAY-skuhg84Lx0WTY-OY3YEI7DA79SrzZqEFyBSV9AOXJnMDmqX8g4yBDBhgl7wvmBtrnRRqw3KoPJQTP6mi0J3EaHLIMpq9fSg5pxijpqxrtrBv5T-Wz1fYutqyHH1MgZ3B39E04Bmqn6bPBWCA5Ra9LiUBfxP7Ax6gkPPK_QLbUIFNgBvkktkmTxTIFQb9A-LBuS2kv2PtdCSpSvOg93k05G6lruwBFxbh7zngrWVony5YM4U-VwzYxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در گوشه ای از مستند جنجالی نجات خلبان اف‌۱۵ نیرو های سپاه در نزدیکی او در خاک ایران هدف قرار گرفته میشوند ؛ حتی یک نفر از ۷ سپاهی سوت موشک که به سمتشان می میرود رو می احساس میکند و سعی می کنه به افراد خبر بده اما نمی داند به کدام سمت بروند. در نهایت انفجار هر ۷ سپاهی را متلاشی میکند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23088" target="_blank">📅 11:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی : هنوز ویزای آمریکای ما برای سفر به ‌نیویورک صادر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/23087" target="_blank">📅 11:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23086">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23086" target="_blank">📅 11:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیویورک‌تایمز :
ایران تشدید تنش را مسیری مؤثر برای افزایش نفوذ و قدرت چانه‌زنی خود در برابر آمریکا می‌داند.
تهران و متحدانش اکنون بر دو مورد از مهم‌ترین مسیرهای انتقال نفت جهان،
تنگه هرمز و باب‌المندب
، نفوذ و اهرم فشار دارند؛ هرمز تحت تأثیر اقدامات مستقیم ایران و باب‌المندب تحت تأثیر پیشروی حوثی‌های مورد حمایت تهران قرار گرفته است. به نوشته این روزنامه، ایران تلاش می‌کند از شرایط ایجادشده در جنگ و اختلال در مسیرهای انرژی،
دستاوردی راهبردی به دست آورد که بتواند جایگاه تهران را در منطقه و در هرگونه مذاکره با واشنگتن تقویت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23085" target="_blank">📅 11:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سی‌ان‌ان: آمریکا خواهان تمرکز مذاکرات با ایران بر پرونده هسته‌ای است، نه تنگه هرمز:
به گفته سه منبع آگاه، دولت ترامپ به‌طور خصوصی به کشورهای منطقه اعلام کرده که ترجیح می‌دهد مذاکرات آینده با ایران بر
پرونده هسته‌ای
متمرکز باشد، نه بازگشایی هرمز. سی‌ان‌ان همچنین گزارش داد تعویق نشست عمان در شرایطی رخ داده که برخی کشورهای منطقه نگرانند توافق پیشنهادی درباره هرمز به ایجاد
وضعیت موجود جدید و دائمی
در این آبراه منجر شود؛ وضعیتی که برای عربستان و دیگر کشورهای شورای همکاری خلیج فارس قابل قبول نباشد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23084" target="_blank">📅 11:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اکسیوس ـ باراک راوید: عربستان سعودی در پیشنهاد ایران و عمان درباره تنگه هرمز اصلاحاتی ارائه کرده است.
یک مقام ارشد از کشورهای خلیج فارس به باراک راوید گفته است که ریاض نگران بوده متن فعلی پیشنهاد، عملاً به ایجاد
وضعیت موجود جدیدی در تنگه هرمز
منجر شود که برای عربستان و سایر کشورهای شورای همکاری خلیج فارس قابل قبول نباشد. این اصلاحات در حالی مطرح شده که
نشست منطقه‌ای کشورهای خلیج فارس و ایران در صلاله عمان به تعویق افتاده است
؛ وزیر خارجه عمان گفته این تعویق با هدف فراهم‌کردن زمینه برای دستیابی به اجماع انجام شده است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23083" target="_blank">📅 11:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23082">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_iAwEGQPGKtoCG-oi2c5uZWAbrLaL6WLISlkahJnA-ikZS_ASF-j0f8PRPWYXTXasD7_aByqURsgKoKkjrjLYilioetYjWs1SftaMwBTuHfFgngFoL02JlpKndIQmodRHqloE_JogxyIzY7JNWnMElsEqiZNTL2V44C6cKDvDYK1Rcgkq-ycHsDR4CfV9LripT_dRGPKzr08a2qK3rWWSsvWDdeS8qvxHqST3OEAak_f2tlsRoRdQC6hdCGbjurA1Q8-oWUZ-dXuMCC3BtNqo7yDzSjQEZ6lNqnmMQw__i0H9OiS2FvtVn0QI0N2VQQpheuvkxvFYXICsb3ApOOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت به سبک کامیک بوک
دوستون دارم
🙌🏾
❤️‍🩹
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23082" target="_blank">📅 05:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">روایتی_نفس_گیر_از_نجات_افسر_تسلیحات_آمریکایی.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/withyashar/23081" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">متن کامل روایت افسر تسلیحات اف ۱۵
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23081" target="_blank">📅 05:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پارت ۲: افشای جزئیات فرار و نجات افسر آمریکایی پس از سرنگونی جنگنده بر فراز ایران و گذراندن ۲ روز با استخانهای شکسته(فارسی)
برای نخستین‌بار، افسر نیروی هوایی آمریکا با نام رمز
«براوو»
که پس از سرنگونی جنگنده‌اش بر فراز ایران، به مدت
دو روز پشت خطوط دشمن
گرفتار شده بود، در برنامه «۶۰ دقیقه» جزئیات این حادثه را روایت کرد. او پس از اجکت، به دلیل آسیب‌دیدگی و باز نشدن کامل چتر نجات، با سرعت حدود
۱۱۰ تا ۱۶۰ کیلومتر بر ساعت
به زمین برخورد کرد و در این حادثه
کمر، دست و شانه‌اش شکست
. براوو که در یک دره گرفتار شده بود، برای فرار از نیروهای ایرانی خود را به ارتفاع حدود
۲۱۳۰ متری
رساند. طبق منابع نظامی آمریکا، نیروهای ایرانی در مقطعی تا فاصله
چندصد متری
او پیش رفتند. ارتش آمریکا برای عملیات نجات این خلبان/افسر، یک مأموریت پرخطر روزانه با مشارکت
۲۱ فروند هواپیما
انجام داد. براوو می‌گوید نخستین پیامی که پس از برقراری ارتباط توانست برای آمریکا ارسال کند این بود:
«خدا خوب است.»
او پس از دو روز سرانجام نجات یافت و توانست با همسرش در آمریکا تماس بگیرد. براوو همچنین تأکید کرد:
«بدون ایمان، این داستان را نداشتم»
و گفت اگرچه ایمان جایگزین آموزش نظامی نیست، اما «پشتوانه تمام اقدامات» او بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/23080" target="_blank">📅 04:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23079">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23079" target="_blank">📅 04:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انتشار نخستین تصاویر نجات خلبان F-15 سرنگون‌شده آمریکا در ایران شبکه آمریکایی سی‌بی‌اس تصاویری از عملیات نجات خلبان آمریکایی منتشر کرده که جنگنده F-15 او در جریان جنگ رمضان در آسمان ایران هدف قرار گرفته و سرنگون شده بود. این تصاویر برای نخستین‌بار لحظات عملیات…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23078" target="_blank">📅 04:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انتشار نخستین تصاویر نجات خلبان F-15 سرنگون‌شده آمریکا در ایران شبکه آمریکایی سی‌بی‌اس تصاویری از عملیات نجات خلبان آمریکایی منتشر کرده که جنگنده F-15 او در جریان جنگ رمضان در آسمان ایران هدف قرار گرفته و سرنگون شده بود. این تصاویر برای نخستین‌بار لحظات عملیات…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23077" target="_blank">📅 04:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انتشار نخستین تصاویر نجات خلبان F-15 سرنگون‌شده آمریکا در ایران
شبکه آمریکایی سی‌بی‌اس تصاویری از عملیات نجات خلبان آمریکایی منتشر کرده که جنگنده F-15 او در جریان جنگ رمضان در آسمان ایران هدف قرار گرفته و سرنگون شده بود.
این تصاویر برای نخستین‌بار لحظات عملیات نجات خلبان پس از سقوط جنگنده آمریکایی در خاک ایران را نشان می‌دهد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23076" target="_blank">📅 03:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer"><a href="https://t.me/withyashar/23074" target="_blank">📅 03:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ:
ما به سرعت ذخایر سلاح‌های خود را بازسازی می‌کنیم و در حال حاضر موشک‌های پاتریوت را با تعداد بیشتری نسبت به هر زمان دیگری تولید می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23072" target="_blank">📅 02:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بلومبرگ: محمد اسلامی، رئیس سازمان انرژی اتمی ایران، پس از آنکه اتریش تحت فشار دولت ترامپ از ورود او جلوگیری کرد، از حضور در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین بازماند.
قرار بود اسلامی روز دوشنبه در این کنفرانس سخنرانی کند، اما ممکن است یک نماینده رده‌پایین‌تر ایران در ادامه هفته به نمایندگی از تهران سخنرانی کند. انتظار می‌رود
کریس رایت، وزیر انرژی آمریکا،
در این کنفرانس هشدار دهد که «ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند یا آن را تولید کند» و هم‌زمان خواستار
همکاری کامل ایران با آژانس و دسترسی بازرسان آژانس به تأسیسات هسته‌ای ایران
شود.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23071" target="_blank">📅 02:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ درباره هوش مصنوعی:
مزایای آن بسیار بیشتر از معایبش خواهد بود.
ما با اختلاف زیادی پیشتاز هستیم. هر کس در حوزه هوش مصنوعی پیروز شود، برنده نهایی خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23070" target="_blank">📅 02:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرنگار: ممکن است نهادهای چینی تصاویر ماهواره‌ای در اختیار ایرانی‌ها گذاشته باشند.
ترامپ: آن‌ها در واقع همان کاری را می‌کنند که ما انجام می‌دهیم. به نظرم او معقول عمل کرد و ما هم معقول رفتار کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23069" target="_blank">📅 02:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbLeyxDK1ds9Cw4-YChJPD6VwZn17YBqxq2DJNXPMdqiJPCcZt0PuEskz_KaWN31sNICWLSv-saqU6opUV3lgkMA2Vct-kbcB8RJHb59JS0qIJpj8UcVmQa05FbxCsnuNqey-rkI0Nt6Lz0bvo4FHgaiKtG0aMEgLEX7DH4ifd9QRIqgukzKZpMQBPMIcIbqeW4JYs7KAy04xbUzlVdlf_yhqc8ypP0_o1WK1KapNqlgGKEWetlnoz3E1pZl1LSSHc6i649v35GlLW1XMBudaT3NuiX4XcANoXqt1in8zJ6z3MZfV0mhd_rd994F0G2VTu37HSiQbqdtoJ6LkjNRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بحران اقتصادی و جنگ، ایران را با کمبود شدید سوخت روبه‌رو کرده است
وال‌استریت ژورنال گزارش می‌دهد کمبود بنزین باعث
صف‌های طولانی در جایگاه‌ها، اعتصاب رانندگان کامیون و تاکسی و افزایش نارضایتی عمومی
شده است. دولت ایران برای مصرف خارج از سهمیه، قیمت بنزین را دو برابر کرده و این افزایش برای بسیاری از مردم که درآمد ماهانه‌شان حدود ۱۰۰ دلار است، فشار سنگینی ایجاد کرده است. اختلال در پالایشگاه‌های آسیب‌دیده از جنگ و محدودیت واردات سوخت در نتیجه محاصره آمریکا نیز بحران را تشدید کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23068" target="_blank">📅 02:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ:فناوری لیزر اهمیت زیادی دارد، چرا که هزینه آن بسیار کمتر از شلیک موشک‌های پاتریوت است.
فعلاً برد آن محدود است، اما به‌زودی برد آن افزایش خواهد یافت.
وقتی تجهیزات را در اختیار داشته باشید، هزینه خودِ پرتو لیزر بسیار ناچیز و تقریباً صفر است. لیزرها همین حالا هم برای مقابله با انواع خاصی از موشک‌ها به‌ویژه موشک‌های کندتر بسیار کارآمد هستند.
به اعتقاد من، آینده از آنِ لیزرهاست.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23067" target="_blank">📅 02:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ: ویتکاف و کوشنر دارند کارشان را عالی انجام می‌دهند.
به غزه به عنوان یک نمونه نگاه کنید؛ درگیری زیادی در غزه وجود ندارد.
حماس اکنون حاضر است سلاح‌هایش را کنار بگذارد. هیچ‌کس دیگری نمی‌توانست کاری را که آن‌ها انجام دادند، به سرانجام برساند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23066" target="_blank">📅 02:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBsBVxhB5NewbPXVGIqLKsQ7YpBjQQOdOyusolwr8UfWfV_oLfZ_1r9G6klnkV3x3tyV1NokSfNxmpFXV1D3f03vz6kigpnyCOb5lZF5Qfnk3yzRCEEauY-vUxfECQSrA27AJDPgEThCR1j1yYaUzD7BdbOu303zsK4vNST-bDnWIKMenQy9k2f1nQdDsyMKQ0VGzGmqh_Xr0Zj_X6876nlL-QFlK3kzqOwGyCoSiu6NvvMUFA7krTBaTQY_oL1wUrbNTaYrfFOdGRoPoWaEXJS8-GTNCZWi9gpTznQn2KrK4YXSUrmG9DNDYdMClbLEv-D_SgEPInANvhrvF0N-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با باز شدن بازار نفت به ۱۰۸ دلار رسید !
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23065" target="_blank">📅 01:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23064" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23063">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ja6F8yUNBZddgkLSrxRjrijG1d8s2rHkbbmEqSFKko7f_faaK-lA8pyWSVAxUycSaX1Eedjmvpg2xYVG8p8R6HA5DBVxD13nRvEPZh5uEy8oWWURtSWSg0GYj47rFDAcgN6dDvATdhchjPQJ6ExPO8Pfen_Ew3tjkqImymXvRErtQEI8DmWpEGfrBZZ3MbLfeZ3ynXtCZenmKY07M_DII6D4H_2-ghHHK706u3MBKvmrVBg6Qly9Jl-HdMK3RGOugylHUJT9zRB2QgaWhItIbQh6vPXfUkLkzl6Fr0LF1jkwc4EL4rK9aL93EP6a-lWpjyw-Oaa_qpudXLKa-2eAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۲۴ ساعت گذشته، نیروهای ارتش اسرائیل (IDF) ۳۸ حمله را در مناطق جنوبی لبنان انجام دادند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23063" target="_blank">📅 01:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23062" target="_blank">📅 01:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23061" target="_blank">📅 00:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23060">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23060" target="_blank">📅 00:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23059" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73711a45e9.mp4?token=UAIAJtqQz4v54RZ47f4S5G0XTHujjMg1ux2QH492XkHGiJyvFzTyUSC47M0P-WPgNiPjbzu5CTcSHSwHvp4l1dmkVkBOmmm_MxuukgUFAuhfeGnOZD8iN9vSRjs8tk0tXc421XLwUDk9fHWfA1ZE5zdbtN99p_F-Zykk79POH7pw70a53AXhQsyQb9lMsbv_6crHSElB5_KkOOz3AW75DB_EJCl2hbkpEvQSRZVtteCN07ahN-0XJOxPiByapY8ftHHv7b8xaELJcr0s7sW6L2pdsbyn40IDYPaHMFuwpO4ipwxrHWM5SXtd0QrO28WhZIToK2XS_SgH5KnGiPuypA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73711a45e9.mp4?token=UAIAJtqQz4v54RZ47f4S5G0XTHujjMg1ux2QH492XkHGiJyvFzTyUSC47M0P-WPgNiPjbzu5CTcSHSwHvp4l1dmkVkBOmmm_MxuukgUFAuhfeGnOZD8iN9vSRjs8tk0tXc421XLwUDk9fHWfA1ZE5zdbtN99p_F-Zykk79POH7pw70a53AXhQsyQb9lMsbv_6crHSElB5_KkOOz3AW75DB_EJCl2hbkpEvQSRZVtteCN07ahN-0XJOxPiByapY8ftHHv7b8xaELJcr0s7sW6L2pdsbyn40IDYPaHMFuwpO4ipwxrHWM5SXtd0QrO28WhZIToK2XS_SgH5KnGiPuypA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : امروز تهه یک کشتی دیگر هم چرخوندیم، سیکش رو زدیم، تعداد کل شد 101
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23058" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">@WarRoom
Level Up</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23057" target="_blank">📅 00:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23056" target="_blank">📅 00:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">@WarRoom
extrime car</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23055" target="_blank">📅 00:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23054">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23054" target="_blank">📅 23:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from➤ 𝗞𝗮𝗶𝘇𝗲𝗻</strong></div>
<div class="tg-text">یاشار چرا نمیری اینترنشنال تحلیلگر بشی</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23053" target="_blank">📅 23:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزیر جنگ اسرائیل : اگه میتونید تپه علی الطاهرو بیاین بگیرید، هرکی بیاد پسی‌خور میشه
@WarRoom
😂</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23052" target="_blank">📅 23:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">@WarRoom
Package movaghaiat
😁</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23051" target="_blank">📅 23:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان ایران برای ۲۵ شهریور فراخوان اعتصاب سراسری داد: این ائتلاف همزمان با چهارمین سالگرد کشته‌شدن مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی» از مردم در سراسر ایران خواست روز چهارشنبه ۲۵ شهریور با بستن مغازه‌ها و بازارها و خودداری…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23050" target="_blank">📅 23:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دیدبان اتاق جنگ : انفجار مهیب نزدیک ساحل سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23047" target="_blank">📅 23:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بدر البوسعیدی، وزیر خارجه عمان: در راستای دستیابی به اجماع، نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاده است. ما همچنان متعهد به تقویت گفت‌وگویی هستیم که از ثبات و همکاری پایدار در منطقه حمایت کند @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23046" target="_blank">📅 23:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b044a4166f.mp4?token=c6xcnPxFF5zlIOH596RY443CU34ZDu5tgpvUpfGDut8YbCRkmCW2SwotLr_wuzm9J40G0ZYG7E97HC30ILxoYcHpD2u-gKwZ4ANj1ixLqR62QTQO0HohsmJHQ7WEltJ7BXYlASPCrkyuLA5bEBHrPftTftgkRU_FRqzPxF-X0OpZ5euICLBEXFYaBJnyIgOfU0fUDLve30fHN8hf91mBz4Yjwe2H3oW1Dk9jXWlfkkcZgCR2gbO2steLHt9uMAuASglzMSnINupaG0-QmV6Zfv-60mw_cg81tzDiJMwL81wzvBFpucnsy0XumToncNO54xedpGtB5xbmKKgshnY5IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b044a4166f.mp4?token=c6xcnPxFF5zlIOH596RY443CU34ZDu5tgpvUpfGDut8YbCRkmCW2SwotLr_wuzm9J40G0ZYG7E97HC30ILxoYcHpD2u-gKwZ4ANj1ixLqR62QTQO0HohsmJHQ7WEltJ7BXYlASPCrkyuLA5bEBHrPftTftgkRU_FRqzPxF-X0OpZ5euICLBEXFYaBJnyIgOfU0fUDLve30fHN8hf91mBz4Yjwe2H3oW1Dk9jXWlfkkcZgCR2gbO2steLHt9uMAuASglzMSnINupaG0-QmV6Zfv-60mw_cg81tzDiJMwL81wzvBFpucnsy0XumToncNO54xedpGtB5xbmKKgshnY5IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک جانسون، رئیس مجلس نمایندگان ایالات متحده، درباره جمهوري اسلامي:
این جنگ ترامپ در ایران نیست. رژیم ایران بزرگ‌ترین حامی دولتی تروریسم است و آن‌ها در فاصله چند هفته از داشتن قابلیت هسته‌ای l یک بمب هسته‌ای قرار داشتند.پیشگیری از این امر، هدفی بوده است که برای ۵۰ سال، توسط هر دولت دنبال شده است.آن‌ها تا این حد به آن نزدیک شدند و رئیس‌جمهور مجبور به اقدام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23045" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بدر البوسعیدی، وزیر خارجه عمان:
در راستای دستیابی به اجماع،
نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاده است.
ما همچنان متعهد به تقویت گفت‌وگویی هستیم که از
ثبات و همکاری پایدار در منطقه
حمایت کند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23044" target="_blank">📅 22:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان ایران برای ۲۵ شهریور فراخوان اعتصاب سراسری داد:
این ائتلاف همزمان با
چهارمین سالگرد کشته‌شدن مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»
از مردم در سراسر ایران خواست روز چهارشنبه ۲۵ شهریور با
بستن مغازه‌ها و بازارها و خودداری از حضور در محل کار
دست به اعتصاب بزنند. این ائتلاف، اعتصاب را «مبارزه‌ای مدنی و پاسخی جمعی» به وضعیت امنیتی و اقتصادی کشور خوانده و با اشاره به ادامه بازداشت فعالان سیاسی و مدنی، افزایش احکام سنگین و اعدام‌ها، از احزاب، تشکل‌های مدنی و اقشار مختلف مردم خواسته است از این فراخوان حمایت کنند.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23043" target="_blank">📅 22:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ از لغو تعرفه‌های ویسکی ایرلندی خبر داد و گفت «همه مدام پیگیر این موضوع بودند»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23042" target="_blank">📅 22:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23041" target="_blank">📅 22:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from... ...</strong></div>
<div class="tg-text">درود آقا یاشار. السیسی وجود دارد در داخل رژیم؟ و بنظرتون اگه وجود دارد چه زمانی رو میشود؟</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23039" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سی‌ان‌ان: عمان پیشنهاد ایران برای دریافت اجباری عوارض را رد کرد و پرداخت‌های داوطلبانه برای ایمنی ناوبری و زیست‌محیطی را پیشنهاد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23038" target="_blank">📅 21:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5iJs-9ZCpUQvm5p5tl1NjTBUNbmaIgKIH5zy6eVm9JszcJpafPVJhRlP_10o4aQWxgnnkRQURnVaGHw7wz32F1mghVR5jWl8YvvibJxb-7XEOccO_o4WZY793y_b6uSyKd5n6CUEQtynXO3Nrkp2SfEXQPjrxvU4OIx1KJnyhM4v_cL1C34faAB_39YilAXaigbLLOQjbjFw8GopOqwcFrI_YX78FBRC7HHQZQbhmsnniIkfbjuD5qF5UY_6LTbNyFFQUhAwX4lKjUsTiP_jXvap4-E9NqxN8SKKxiDl9Ov43EvJ3cn-XDp8bhA8OaUz7QuxAB2YofvXpMBivYwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون پرتاب سه موشک از یک نخلستان نزدیک سیریک به سمت تنگه هرمز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23037" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f697ad6f42.mp4?token=EVYFmDRu3kic9ZpgdyCf4d5L0bT1kHHu7ISGgM9cMFKCzA0aSF80EcpsjkL-_0fa9CoISpPsCV8zeMU_CCL_rRWPRd0cPfF6NxYdue_M1lgMYVeZCyUOCHHSIqFpQXfnyd8juaXGwzU5GwP9EvX8qIdP_z70pg4WEngOiVomRvxc947kvDim-cI8YxGCfRIyrTCSAOYP_7YwHX6fAFZz4cjmybwYaNbA0zBVvH6s5LuM_ceeMZ_8Z5b5JorrU0ZAFpz3dPPpCtNisHzTDemVRxU8bEaoZ588MiXJefuRAgsOSnmeQwczQBaFfU4sIPosTkBNZIxDw0Lb0O3ANDm96Trk-1mMQEMACNdcAI6qY9NJbDvhFu2X8kN-Y-x4Yycja8sbFRQluZ8veyh5lItD3YPJQ1WiIo9jLvl10liG82FkINjX-K5Kln4WV-m9ugYd_lpEEv0SaNVSs5jwdCb7IUmwuyT6BYv8vcI3whGkmuagcEedTt4e8SFNFeG5yzHg4uHyNXtWOv9-oBQ8WQAxJyXlr3RtD7EgqqonFq0CjWxpYxcN5jmoBu5vetStjPzwOvKiy8kYLq-5p89sqbmvdKL_uK299lZ7JvWXKnox7LqHLCbhcaCSrSOWXUzQnYnPZCNNvBzqHCOzZrHDkDs2ZOkKTPrN651708OOiM9RuOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f697ad6f42.mp4?token=EVYFmDRu3kic9ZpgdyCf4d5L0bT1kHHu7ISGgM9cMFKCzA0aSF80EcpsjkL-_0fa9CoISpPsCV8zeMU_CCL_rRWPRd0cPfF6NxYdue_M1lgMYVeZCyUOCHHSIqFpQXfnyd8juaXGwzU5GwP9EvX8qIdP_z70pg4WEngOiVomRvxc947kvDim-cI8YxGCfRIyrTCSAOYP_7YwHX6fAFZz4cjmybwYaNbA0zBVvH6s5LuM_ceeMZ_8Z5b5JorrU0ZAFpz3dPPpCtNisHzTDemVRxU8bEaoZ588MiXJefuRAgsOSnmeQwczQBaFfU4sIPosTkBNZIxDw0Lb0O3ANDm96Trk-1mMQEMACNdcAI6qY9NJbDvhFu2X8kN-Y-x4Yycja8sbFRQluZ8veyh5lItD3YPJQ1WiIo9jLvl10liG82FkINjX-K5Kln4WV-m9ugYd_lpEEv0SaNVSs5jwdCb7IUmwuyT6BYv8vcI3whGkmuagcEedTt4e8SFNFeG5yzHg4uHyNXtWOv9-oBQ8WQAxJyXlr3RtD7EgqqonFq0CjWxpYxcN5jmoBu5vetStjPzwOvKiy8kYLq-5p89sqbmvdKL_uK299lZ7JvWXKnox7LqHLCbhcaCSrSOWXUzQnYnPZCNNvBzqHCOzZrHDkDs2ZOkKTPrN651708OOiM9RuOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23036" target="_blank">📅 20:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e431617c.mp4?token=KQ-nyN8gpqVsDb7ppd7scrh6Hrc_cZG5quZLKYitq1088uMa_c0xrSDZFwNwJ2YyIrRWZq0YpL4gtyGiZ98BFuj0h4w9grWJ4HiIs0Kh2r9IQ3LenL0cJeEn7c2PDZBX3Eh64PyO_L8CdptVLHRxkvgqd1qFQc89FBFABApC866bpyw0lR2G8-vCWECYK9CeeOSFMTqMDfpB0xecsMEgsR1X-VtOh-nnRYHjRrWdPCT9FdJLrYg_W0fL4lecTXWwZsyClQ9cGNuBHD6iWD9GpXYJd7FIWhQOpN_4f5G_8Ax_cmE7Zxm6icoc9Av8K4RuDcgTyWsEljMA_BOPLpYeuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e431617c.mp4?token=KQ-nyN8gpqVsDb7ppd7scrh6Hrc_cZG5quZLKYitq1088uMa_c0xrSDZFwNwJ2YyIrRWZq0YpL4gtyGiZ98BFuj0h4w9grWJ4HiIs0Kh2r9IQ3LenL0cJeEn7c2PDZBX3Eh64PyO_L8CdptVLHRxkvgqd1qFQc89FBFABApC866bpyw0lR2G8-vCWECYK9CeeOSFMTqMDfpB0xecsMEgsR1X-VtOh-nnRYHjRrWdPCT9FdJLrYg_W0fL4lecTXWwZsyClQ9cGNuBHD6iWD9GpXYJd7FIWhQOpN_4f5G_8Ax_cmE7Zxm6icoc9Av8K4RuDcgTyWsEljMA_BOPLpYeuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام، می‌گوید هیچ‌گونه نگرانی‌ای بابت کمبود مهمات آمریکا ندارد.
«ما به‌خوبی مسلح و برای هرگونه وضعیت احتمالی آماده هستیم.»
کوپر در پاسخ به این پرسش که آیا نگران تهدیدهای آینده است، گفت: «خیر، نگران نیستم.»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23035" target="_blank">📅 20:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23034" target="_blank">📅 20:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا تنها</strong></div>
<div class="tg-text">سلام .
میشه دلیل اینکه بنده رو از گروه بیرون کردید رو بدونم</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23033" target="_blank">📅 20:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23032" target="_blank">📅 20:31 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
