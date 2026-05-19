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
<img src="https://cdn4.telesco.pe/file/I3wwY59EwyQschm8mCui56P2nXu8-o_BY7UETGxAtT3-qcCE0nYJMErFeXddiGjAMjgZ6zgQip1ZTHWUO480Oi414uVaMk3CVRzv81D2ZmUO3PVkVBAeuaOBfKxhZa7tFaHfUrGlDneDrvpqfqp9ibhkDB2uE3SXaIn64hEhNMvXOjzNB2n4aM1YsUtwmTKhkNehbUiSJDUzmCRHJ6Uj0FggQup31Fx2g8hm_bY6SNxEroqegudLAMwxElQgya5ZsfxAfDMAr9d0qehmmlUmC5VGt-Gh0EkOc4sUPoTS7QL4W2hxTJ63fh80HXT5zyOgdCWLm9l0sEMGXflqXvu9DA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 947K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 20:16:10</div>
<hr>

<div class="tg-post" id="msg-121145">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
اسرائیل هیوم: نتانیاهو به دلایل امنیتی درخواست کرده است که فردا در دادگاهش برگزار نشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/alonews/121145" target="_blank">📅 20:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121144">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ادعای کانال ۱۲ اسرائیل: ارزیابی‌های اسرائیل نشان می‌دهد که ترامپ تصمیم حمله به ایران را گرفته است و اجرای آن فقط مربوط به مسئله زمان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/alonews/121144" target="_blank">📅 20:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121143">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فرمانده سنتکام : چند تا ناوشکن آمریکایی اخیراً از تنگه هرمز عبور کردن
🔴
ایران از هر نظر خیلی ضعیف‌تر از قبل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/alonews/121143" target="_blank">📅 20:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121142">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رابرت مالی رئیس هیات مذاکره کننده آمریکا در دوره بایدن: مدتهاست که زمان آن فرا رسیده که کاری را انجام دهیم که برای بسیاری از ما غیرممکن به نظر می‌رسد، و آن این است که به حرف‌های ترامپ اصلاً هیچ توجهی نکنیم.
🔴
این بدان معنا نیست که او حمله نخواهد کرد؛ به این معنا نیست که حتماً حمله خواهد کرد.
🔴
معنایش این است که حرفی که او یک روز می‌زند، هیچ نسبتی با واقعیت ندارد و هیچ نسبتی با حرفی که روز بعد خواهد زد، ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/alonews/121142" target="_blank">📅 19:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121141">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO7fVBlwUIRfOVf0BbchVZNC8-7Zm-__ddjneTJc-ohh_kEMF95S6skjXxqqye0U5kutW2UG75xVF385Lmzm2u_oHgjKSrYbLZmvYfZIIsq81MAPlKqOPW03zDJX9_KezL2jp5s7uA61Efc1I-1JSunmLmAg19ZGBCzAQ92fJCuHrVudPsT2PTThGZyHpBtgEPM4CwJG99zW2ox19L5Z7EE6BDW2GHuHK8ACLKsoRcyHYWvGtzhOr0P-2261l3jYkjkhD9g8yV9wgaGD2Zez84h_BvSPW2ExJCvLd6HnsmF8O9Nl1tgrm6sQyrg1sWRzoHBzjsOvSMVn195GI89JDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب‌آبادی
:
برای ما تسلیم شدن معنایی ندارد؛ یا پیروز می شویم یا شهید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/alonews/121141" target="_blank">📅 19:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121140">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
آتلانتیک: دو هواپیمای سوخت‌رسان KC-135 آمریکایی در تاریخ ۱۲ مارس بر فراز عراق با هم برخورد کردند و شش نفر کشته شدند.
🔴
پنتاگون اعلام کرد هیچ آتش خصمانه‌ای در کار نبوده است.
🔴
اما گزارش‌های اولیه اطلاعاتی، آتش پدافند هوایی شبه‌نظامیان تحت حمایت ایران را در آن منطقه در آن زمان شناسایی کردند که نشان می‌دهد خلبانان ممکن است اقدام به گریز کرده باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/121140" target="_blank">📅 19:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121139">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
صداوسیما: ایران می‌تواند اینترنت امارات و قطر را قطع کند/ایران می‌تواند شرکت‌هایی مانند اینستاگرام را با اهرم فشار اینترنت تنگه هرمز پاسخگو کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121139" target="_blank">📅 19:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121138">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0VFX0_jLdD1sfpOebP4svKhMMvw1BV9C_31aGrvfdb9MH-Qv8yKd8OYyqLQ2TF0zErgYbvBUsQpJ2q-MTOsDUBTdZhHO7gs19iKk4fVehoUexMQysxPyUt6-zYVATl7KZE6_yZRdjVhjRMQQmuu2IQShNnYWZGjL2rPPZl_6qvocTOshZcqphNYWYMX1EWZCGywmUWrpNHgyMhh7U0ycG8ZJtg5FadapceT5-9gWbFwfWdLnCVnrtHHRrtnYM_pLrdsDLuOwZ5r3hh68d44mI5p7xdJXDCGgY4iDSo0aCj_Q4WKizONvxBpT3CklPD-JsngtgeRFlXmGYXrVaf92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۱۰.۴۲ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/121138" target="_blank">📅 19:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121137">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ارتش پاکستان اعلام کرد ۲۲ تروریست را در عملیاتی در شمال غربی پاکستان کشته است.
🔴
این عملیات در وزیرستان شمالی صورت گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121137" target="_blank">📅 19:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121136">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بلومبرگ: به گفته یک مقام ارشد در ناتو، این سازمان در حال بررسی امکان کمک به عبور کشتی‌ها از تنگه مسدود شده هرمز است، در صورتی که این آبراه تا اوایل ژوئیه(اواسط تیر) بازگشایی نشود.
🔴
یک دیپلمات از یکی از کشورهای عضو ناتو گفت که این ایده از حمایت چندین عضو پیمان آتلانتیک شمالی برخوردار است، اما هنوز حمایت اتفاق آرای لازم را ندارد.
🔴
رهبران کشورهای عضو ناتو در تاریخ ۷-۸ ژوئیه در آنکارا دیدار خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/121136" target="_blank">📅 18:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121135">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: متحدان اروپایی باید با بستن شعب بانکی و توقیف دارایی‌های ایران، اجرای تحریم‌ها علیه این کشور را تقویت کنند.
🔴
متحدان آسیایی ما باید ناوگان سایه ایران را زیر نظر داشته باشند تا از حمل نفت توسط نفتکش‌هایی که مشمول تحریم نیستند، جلوگیری شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121135" target="_blank">📅 18:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121134">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ادعای نشنال اینترست: ناوگان قایق‌های تندروی ایران تهدید بسیار جدی محسوب می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/121134" target="_blank">📅 18:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121133">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رویترز: پوتین به چین رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/121133" target="_blank">📅 18:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121132">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cd783799.mp4?token=l0bGW1nc0dkV1pW9vTPSCgVt-jFgJ90tfpikEOcAiYlpHBvt3-nc4GRtZtbNOXXY4ys-WucCwqqAX6Hb-p83zRa0r5IqgDXdadIjz388_m12KFYJc8dsUz8BOwxVJ_7rEmtlJboaMOeeuJuxegBFS8lFpffL4CuBMTnhwUL7FOD_tgh839Amcek3Q-_7pIW_0Pr_kDJGWwNQSB5RzpcG4ahkKLhXfF6DdpmAMupGbDslX5hThnbKNL-hurOQ15Er5iu-7LOmxHEitt2bH4qixgBCSIvhrtSgCDN8V70RD4Y5icREoRq2sb8yoCHF2U_xSyj0beDO51CTNQMD0kCNbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cd783799.mp4?token=l0bGW1nc0dkV1pW9vTPSCgVt-jFgJ90tfpikEOcAiYlpHBvt3-nc4GRtZtbNOXXY4ys-WucCwqqAX6Hb-p83zRa0r5IqgDXdadIjz388_m12KFYJc8dsUz8BOwxVJ_7rEmtlJboaMOeeuJuxegBFS8lFpffL4CuBMTnhwUL7FOD_tgh839Amcek3Q-_7pIW_0Pr_kDJGWwNQSB5RzpcG4ahkKLhXfF6DdpmAMupGbDslX5hThnbKNL-hurOQ15Er5iu-7LOmxHEitt2bH4qixgBCSIvhrtSgCDN8V70RD4Y5icREoRq2sb8yoCHF2U_xSyj0beDO51CTNQMD0kCNbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا رئیس‌جمهور شی گفت که پوتین از حمله به اوکراین پشیمان خواهد شد؟
🔴
ترامپ: نه. او هرگز چنین چیزی نگفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/121132" target="_blank">📅 18:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121131">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcbe32ed97.mp4?token=bWHYsA33XOqm9vYmF0MD8rDe10jhXZBSmgGUDKQJ8vpvQlQJgFVhODZZ8d_J_xfEFpno7WB7BkHIMGdERKDqUQGhXav4jn_2eBaqGVD2Ozqrseki9AQPAAJtqMi_WVz4AN2hDRbTOaPxvdF87m1RgG2ksz0Q2LZHtSKYIf27BrwmXuKUJcpVLb8Cwaq2rWbZeHXT-rdFJNlgCHK-p26CdO5G2se1k9ZXBj6BqEJejsUOJRI-cBBlMJXZYt1p32nz5ObstNXEzF8Y2-RZApPM9-HbfwFZO9xtU5aVf0Bluc1yO5RANfL6kPO1IcruyBmTUix1MqKLUgq9guq1jEB-6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcbe32ed97.mp4?token=bWHYsA33XOqm9vYmF0MD8rDe10jhXZBSmgGUDKQJ8vpvQlQJgFVhODZZ8d_J_xfEFpno7WB7BkHIMGdERKDqUQGhXav4jn_2eBaqGVD2Ozqrseki9AQPAAJtqMi_WVz4AN2hDRbTOaPxvdF87m1RgG2ksz0Q2LZHtSKYIf27BrwmXuKUJcpVLb8Cwaq2rWbZeHXT-rdFJNlgCHK-p26CdO5G2se1k9ZXBj6BqEJejsUOJRI-cBBlMJXZYt1p32nz5ObstNXEzF8Y2-RZApPM9-HbfwFZO9xtU5aVf0Bluc1yO5RANfL6kPO1IcruyBmTUix1MqKLUgq9guq1jEB-6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر امروز می‌رفتم(حمله می کردم)، بازسازی آن‌ها ۲۵ سال طول می‌کشید.
🔴
اما ما در حال ترک نیستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/121131" target="_blank">📅 18:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121130">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ درباره ایران: تنگه هرمز مال ایران نیست. تنگه در آب‌های بین‌المللی است، این به آنها مربوط نیست که چنین کاری کنند! آنها درس خود را آموخته‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/121130" target="_blank">📅 18:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121129">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ درباره ایران: «رئیس‌جمهور چین به من قول داده است که هیچ سلاحی به ایران ارسال نمی‌کند. این یک قول زیباست.
🔴
حرف او را قبول دارم. از این بابت قدردانی می‌کنم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/121129" target="_blank">📅 18:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121128">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e7462ece.mp4?token=hmFSeuyeO_S3eqPdAWMY0Cmv1avvYs9WyV50OBWeGheWttUP_C2onB0ySZ9Xatpf6R__fR7BzNrdRNzVz-9cxTbOftEYGGUWPDLsVg90LOJgFCmuZxTT6HzMYPF26pBNTdnO9fvGq9k2kMpCUHwicgprVfZwZvJEn2SS0CcckPhNewG98NWUlyOS4HLPW4FkV54tnxMJJ_4Sv8jN4rR42LOhAewd4IDClVarcPGE1vLbo82Oh7V9u9oCjUDRUAfKHgYnypYg20o-FSlb3TjZi014qBPTqBu8kU5oremqC8_2bmNRcEWNlAj9pBC5noIglF_Mhqg-nFCyLtbDn-OWpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e7462ece.mp4?token=hmFSeuyeO_S3eqPdAWMY0Cmv1avvYs9WyV50OBWeGheWttUP_C2onB0ySZ9Xatpf6R__fR7BzNrdRNzVz-9cxTbOftEYGGUWPDLsVg90LOJgFCmuZxTT6HzMYPF26pBNTdnO9fvGq9k2kMpCUHwicgprVfZwZvJEn2SS0CcckPhNewG98NWUlyOS4HLPW4FkV54tnxMJJ_4Sv8jN4rR42LOhAewd4IDClVarcPGE1vLbo82Oh7V9u9oCjUDRUAfKHgYnypYg20o-FSlb3TjZi014qBPTqBu8kU5oremqC8_2bmNRcEWNlAj9pBC5noIglF_Mhqg-nFCyLtbDn-OWpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: توماس ماسی یک نماینده کنگره وحشتناک است. او از روز اول یک نماینده وحشتناک بوده است. برخورد با او واقعاً وحشتناک است.
🔴
فکر نمی‌کنم او جمهوری‌خواه باشد. فکر می‌کنم در واقع یک «دموکرات احمق» است. او لیبرتارین نیست.
🔴
او همیشه علیه ما رأی می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/121128" target="_blank">📅 18:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121127">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: چه اقدام نظامی علیه ایران با حمایت مردمی روبرو شود و چه نشود، من اجازه نخواهم داد دنیا جلوی چشمانم منفجر شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121127" target="_blank">📅 18:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121126">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=ZgEUwJC0N5BesdN_5OoRqvUlSLsczVdMTUR05wj9iyAKuDFtChmgXrbdWxsTs7r-bRwB-Q4uVz8dY4PZHBSyz0q9qUxdWZ9XKp1J1rOVM72NWeoCRefUP3QvLhL2XcLaswAOB7RxbIbpLnx9JveQLeYlB6pTCSiYOKE9KddueBqSOUda1H3gjdIVsgSucGjkeLPdS4DIwl3BWUdVbRkf0NU_Czv4VkwossP6Qcij6xt4lmsM_eLJlSdIJnWd_S5MtjTEmceRrgDSoUVNWYhXbUQy1OUQX8HNSPj7Tf1v_gywNAF3bsujbm0g4CF9KZlc-ulcymqQw4UTYHmzHB7qMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=ZgEUwJC0N5BesdN_5OoRqvUlSLsczVdMTUR05wj9iyAKuDFtChmgXrbdWxsTs7r-bRwB-Q4uVz8dY4PZHBSyz0q9qUxdWZ9XKp1J1rOVM72NWeoCRefUP3QvLhL2XcLaswAOB7RxbIbpLnx9JveQLeYlB6pTCSiYOKE9KddueBqSOUda1H3gjdIVsgSucGjkeLPdS4DIwl3BWUdVbRkf0NU_Czv4VkwossP6Qcij6xt4lmsM_eLJlSdIJnWd_S5MtjTEmceRrgDSoUVNWYhXbUQy1OUQX8HNSPj7Tf1v_gywNAF3bsujbm0g4CF9KZlc-ulcymqQw4UTYHmzHB7qMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ایران چند روز فرصت دارد تا به میز مذاکره بیاید؟
🔴
ترامپ: دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک دوره زمانی محدود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/121126" target="_blank">📅 18:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121125">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ درباره ایران: پس آنها (کشورهای خلیج) تماس گرفتند؛ شنیده بودند که من تصمیم به حمله گرفته‌ام.
🔴
گفتند، «آقا، می‌توانید چند روز دیگر به ما فرصت دهید چون فکر می‌کنیم آنها منطقی رفتار می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121125" target="_blank">📅 18:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121124">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ درباره ایران: «فکر می‌کنم گرفتن غبار هسته‌ای (ذخایر اورانیوم) مهم است، شاید از نظر روانی بیشتر از هر چیز دیگری مهم باشد.»
🔴
«همه به من می‌گویند این جنگ نامحبوب است، اما من فکر می‌کنم بسیار محبوب است.
🔴
وقت کافی ندارم که جنگ را برای مردم توضیح دهم. من خیلی مشغول آن هستم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121124" target="_blank">📅 18:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121123">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: ما باید کشوری امن داشته باشیم و باید اطمینان حاصل کنیم که ایران به سلاح هسته‌ای دست پیدا نمی‌کند.
🔴
ایران نباید به سلاح هسته‌ای دست یابد.
🔴
دموکرات‌ها تلاش می‌کنند مانع مذاکره من با ایران شوند
🔴
ایران می‌خواهد خاورمیانه را نابود کند و این اتفاق نخواهد افتاد.
🔴
رهبرانی هستند که در دو روز گذشته با من تماس گرفته‌اند و گفته‌اند که پیشرفت قابل توجهی در مورد ایران حاصل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121123" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121122">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
هم اکنون ترامپ در مورد ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آن‌ها بزنیم. هنوز مطمئن نیستم.
🔴
خیلی زود خواهید فهمید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121122" target="_blank">📅 18:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121121">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d31e39e6b.mp4?token=T2NPQRQSdHGhv_VI6uCoIUre5OIxAOZxmavbfywTy9eivpCNaOHQs0UMWzJuk7am9JOkY-WUoaC4dxNuFzeSTqwy-ouIChTy3DeQWZsvqqs_hbmpSH05SrLGX7fazxiyRUwgZ1ioEzQtd12VXTl5ktHWXPvDAkkTnq6JpcDpL18__uhiKYpJjJ-ByYJNlLMiEqqpeKVkaJ5a24LsSiQIWjwQ5iNRgSJ4VqwhH3stIVNX9TYrs-yBl9HwV8NoApeS4SXcoh0UsdkMvZxMZVuV_NAtDz_WM7IWMWW3b7s8RkmLTDhE6EewEcjNoYjd8knjJb1WAF23Qhp_SNpFtJS2Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d31e39e6b.mp4?token=T2NPQRQSdHGhv_VI6uCoIUre5OIxAOZxmavbfywTy9eivpCNaOHQs0UMWzJuk7am9JOkY-WUoaC4dxNuFzeSTqwy-ouIChTy3DeQWZsvqqs_hbmpSH05SrLGX7fazxiyRUwgZ1ioEzQtd12VXTl5ktHWXPvDAkkTnq6JpcDpL18__uhiKYpJjJ-ByYJNlLMiEqqpeKVkaJ5a24LsSiQIWjwQ5iNRgSJ4VqwhH3stIVNX9TYrs-yBl9HwV8NoApeS4SXcoh0UsdkMvZxMZVuV_NAtDz_WM7IWMWW3b7s8RkmLTDhE6EewEcjNoYjd8knjJb1WAF23Qhp_SNpFtJS2Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🔴
ترامپ: یک ساعت فاصله داشتم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121121" target="_blank">📅 18:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121120">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری /  ترامپ درباره زمان حمله به ایران: «۲-۳ روز دیگر، شاید جمعه یا شنبه، اوایل هفته آینده. یک دوره زمانی محدود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/121120" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121119">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزارت دفاع امارات ادعا کرد که سامانه‌های پدافند هوایی در ۴۸ ساعت گذشته، ۶ فروند پهپاد را رهگیری کرده‌اند.
🔴
تحقیقات روشن کردند که حمله پهپادی ۲۷ اردیبهشت (۱۷ مه) به نیروگاه هسته‌ای برکه از عراق انجام شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121119" target="_blank">📅 18:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121118">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56750e37ce.mp4?token=qA50KJHIRkcoH9HTJqs4M45uaMxUL9KxhvIoHhAK55REjJZIrgRvoiHRdNkyX2H8kTM9HgROC6LFydmRQsJvpoNImOfGTMVHi31cawita8u64NxU7w2prWKc2zcpthQnzU2rl9v3MzHkrJVTGt_ghUtS63mDL4RX98mlhhXISerSkjUFiOblToiRfqm1NV-OnXbD8zMqaQB9JJeRb9j02LKlHIpIndDS68r5PqEaoJQGiLWCY9cP-N19ugDCyaZwFzFun_F1dp5WXkhvOzyFLYHbRU4wLBuQU0BzFVpex83H5Kez0EqrY-lpFyL_i2QK93G3aAd6tVisaa32tKnYjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56750e37ce.mp4?token=qA50KJHIRkcoH9HTJqs4M45uaMxUL9KxhvIoHhAK55REjJZIrgRvoiHRdNkyX2H8kTM9HgROC6LFydmRQsJvpoNImOfGTMVHi31cawita8u64NxU7w2prWKc2zcpthQnzU2rl9v3MzHkrJVTGt_ghUtS63mDL4RX98mlhhXISerSkjUFiOblToiRfqm1NV-OnXbD8zMqaQB9JJeRb9j02LKlHIpIndDS68r5PqEaoJQGiLWCY9cP-N19ugDCyaZwFzFun_F1dp5WXkhvOzyFLYHbRU4wLBuQU0BzFVpex83H5Kez0EqrY-lpFyL_i2QK93G3aAd6tVisaa32tKnYjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره سالن رقص کاخ سفید:
تمام این هزینه‌ها را خودم پرداخت کرده‌ام. این یک هدیه است.
🔴
این هدیه‌ای به ایالات متحده آمریکا است
🔴
این بیش از یک هدیه است؛ این قرار است یکی از زیباترین ساختمان‌هایی باشد که تاکنون در کشور یا در واشنگتن دی‌سی ساخته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121118" target="_blank">📅 18:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121117">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b9680b69.mp4?token=MEdwlrfIdMtmMajGvbfU9Dg7V1E7rska3Vr32_N8-rzZej5hUBQtqNFHKDxPslZKv0WRAbQ5OgBQMZwYQY_i8kA02c1sH5gBQbqiyLh7NMU9M5cJ1EUp5jHITCIKJiO3TAaI2S9osH6o_wDm7AxuIxaHGC4M4UYgtg_DciEhKKKhciX5TEWP24YGYIVOjMU-K73JYCvsu06nSzlOvqzthLAvZo1AXOvxW2_fYHYhlOJb52KGcjMpazpCGkmRl6ha8YwxSdrZKb89gO6fuWSlLRGsoi6N21l7cq7OO-_YMN6xMWGQFAzt-tAwFwlUSfBt_GRTMJ9n8CCTfCNx8vBTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b9680b69.mp4?token=MEdwlrfIdMtmMajGvbfU9Dg7V1E7rska3Vr32_N8-rzZej5hUBQtqNFHKDxPslZKv0WRAbQ5OgBQMZwYQY_i8kA02c1sH5gBQbqiyLh7NMU9M5cJ1EUp5jHITCIKJiO3TAaI2S9osH6o_wDm7AxuIxaHGC4M4UYgtg_DciEhKKKhciX5TEWP24YGYIVOjMU-K73JYCvsu06nSzlOvqzthLAvZo1AXOvxW2_fYHYhlOJb52KGcjMpazpCGkmRl6ha8YwxSdrZKb89gO6fuWSlLRGsoi6N21l7cq7OO-_YMN6xMWGQFAzt-tAwFwlUSfBt_GRTMJ9n8CCTfCNx8vBTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده ارشد ناتو، الکسوس گرینکوویچ: در مجموع ۵۰۰۰ نیروی نظامی آمریکا از اروپا خارج خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/121117" target="_blank">📅 17:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121116">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزارت دفاع امارات متحده عربی مدعی شد نتایج تحقیقات فنی مربوط به حمله به نیروگاه هسته‌ای براکه در تاریخ ۱۷ مه ۲۰۲۶ تأیید کرد که هر سه پهپاد مهاجم از خاک عراق پرواز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/121116" target="_blank">📅 17:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121115">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ادعای امارات: طی ۴۸ ساعت گذشته با ۶ پهپاد که قصد داشتند مناطق مسکونی و حیاتی را هدف قرار دهند، مقابله کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121115" target="_blank">📅 17:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121114">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
معاون وزیر خارجه ایران : ایران آماده‌ست با هر جور تجاوز نظامی روبرو بشه، ما یا پیروز می‌شویم یا شهید می‌شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121114" target="_blank">📅 17:36 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121113">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ7K0a9VFfmmt6OCXARSg1mAMYirz55EmlF-PMF_cuVUsWupvuNgwNMwVwPVkmhzp9BdtD9tl7jWh3LzVViSm-u8lJK8P56x5IPxVwhgM00F4AlSgdv6fFaY3TSC8UDfRPRbah_ic1Is94GDVdG5tUXTxStdSWyLlX85oN4uA-HS8wW5efxLK-rkHNkM-_JA9838i0YqqXl1dAm3lqCk0FgbmarkjMXdjoyFnNfqCSkUtHMOsAOiCu8RmF3k0IPU1I7RRggK2FqHYmBkQDxPu1-vMJ0eGgrvQGnSK3fLV4Yx6fN_KVLB-jyxsz6s10fFza04XZm37Z0-L192LG2FBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نرخ دلار امروز، ۱۷۸,۵۴۸ هزارتومن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/121113" target="_blank">📅 17:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121110">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/ef61b8367d.mp4?token=YfkpZZqCxOEoSPUHkRwo37nD7Xx35t30Tvk3yDI3SdJ0y76ZZZUm-lqRvm2ZZYjFXkj0nDQQuzCyAeo5Qv5Tgd7dkPJsD2l4C7XmkWt4gDmMGG1F2ZwmSgFTXvFXhWQ5nQ5CZTRF2bEIiwzkrRFarjfN_cyszr3URgEmWKVIWB9s0CKu3o56PkADtwJEKEzX2xHH4Uxa4SuaQU1lLu_NFpDiREyaLgbIxmpo0dD9caQONLYoextsUTZW-eX4WRbMN3Fpp9w56o5iKFeo9hgfm1lykAobh-70x1qa5CoGv3El9EcoO_o67NjDKQzyFqINoQdc_FvOz1ZNFQpM3Gq1Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/ef61b8367d.mp4?token=YfkpZZqCxOEoSPUHkRwo37nD7Xx35t30Tvk3yDI3SdJ0y76ZZZUm-lqRvm2ZZYjFXkj0nDQQuzCyAeo5Qv5Tgd7dkPJsD2l4C7XmkWt4gDmMGG1F2ZwmSgFTXvFXhWQ5nQ5CZTRF2bEIiwzkrRFarjfN_cyszr3URgEmWKVIWB9s0CKu3o56PkADtwJEKEzX2xHH4Uxa4SuaQU1lLu_NFpDiREyaLgbIxmpo0dD9caQONLYoextsUTZW-eX4WRbMN3Fpp9w56o5iKFeo9hgfm1lykAobh-70x1qa5CoGv3El9EcoO_o67NjDKQzyFqINoQdc_FvOz1ZNFQpM3Gq1Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار یک وسیله نقلیه حامل بمب دست‌ساز در نزدیکی ساختمان وزارت دفاع بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121110" target="_blank">📅 17:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121109">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزارت بهداشت لبنان از آغاز حمله اسرائیل در دوم مارس، 3042 کشته و 9301 زخمی گزارش می دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/121109" target="_blank">📅 17:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121108">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سفیر چین در تهران: حمایت پکن از ایران، آشکار و بی‌چون و چرا است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/121108" target="_blank">📅 17:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121107">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
دراپ‌سایت: براساس داده‌های ردیابی کشتی‌ها از Lloyds List Intelligence، ترافیک عبوری از تنگه هرمز در هفته ۱۱ تا ۱۷ مه به ۵۴ فروند کشتی افزایش یافت که بیش از دو برابر ۲۳ فروند هفته قبل است
🔴
این افزایش شامل ۱۰ فروند کشتی متعلق به چین است‌. رسانه‌های دولتی ایران اعلام کرده بودند که تهران به کشتی‌های چینی اجازه عبور می‌دهد
🔴
همچنین یک کشتی حامل ال.ان.جی متعلق به ادنوک (ADNOC) که از طریق عبور مخفیانه (با خاموش بودن فرستنده ردیاب خود) وارد خلیج فارس شد. دو کشتی حامل ال‌پی‌جی نیز خلیج فارس را به مقصد هند ترک کردند.
🔴
این بهبود نسبی همچنان بسیار کمتر از میزان تردد قبل از جنگ است. پیش از آنکه آمریکا و اسرائیل در اواخر فوریه به ایران حمله کنند، ماهانه حدود ۳۰۰۰ فروند کشتی از تنگه عبور می‌کردند - یعنی حدود ۱۰۰ تا ۱۴۰ فروند در روز - که حامل ۱۵ میلیون بشکه نفت خام و فرآورده‌های نفتی در روز بودند، یعنی تقریباً یک‌پنجم تجارت جهانی نفت. در کل ماه آوریل، فقط ۱۹۱ عبور ثبت شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/121107" target="_blank">📅 17:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121106">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3607fd785c.mp4?token=Cc6vq12nW3Q8dl2cRLPs66XEg1cMb86DJ1s9RTdlxjQuM3yNrE350KPBZWDLfUePExMCNqPl_xCLBNyfVvZ5DQyp3V8rgqQw1bHF1faHcqsY_9n1mP5zRa78LGASHK42FRWw_encblxittZaCYePwH34OSCno8jd2zv9-Uk3SaI85mh-pbo_rgidapDWr_YfjLWDuUsyU-wuE_Qj6bCaexR117gcsGM3_WoxEuWn1SZQtuRbVcbUmIf8IqJhw-XSNaj50yolOf_iZSvSewWaCvh9nCykyxnFx48_fCfgPLjqvDIcqaIm_j0doAz_FDIj5cgOD7EbAz2SM77Y5PyY8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3607fd785c.mp4?token=Cc6vq12nW3Q8dl2cRLPs66XEg1cMb86DJ1s9RTdlxjQuM3yNrE350KPBZWDLfUePExMCNqPl_xCLBNyfVvZ5DQyp3V8rgqQw1bHF1faHcqsY_9n1mP5zRa78LGASHK42FRWw_encblxittZaCYePwH34OSCno8jd2zv9-Uk3SaI85mh-pbo_rgidapDWr_YfjLWDuUsyU-wuE_Qj6bCaexR117gcsGM3_WoxEuWn1SZQtuRbVcbUmIf8IqJhw-XSNaj50yolOf_iZSvSewWaCvh9nCykyxnFx48_fCfgPLjqvDIcqaIm_j0doAz_FDIj5cgOD7EbAz2SM77Y5PyY8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله همچنان داره تانک‌های مرکاوای اسرائیل رو تو جنوب لبنان میزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121106" target="_blank">📅 17:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121105">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
عراق: قاطعانه استفاده از خاک خود برای حمله علیه همسایگان را رد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/121105" target="_blank">📅 17:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121104">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
زنگ خطر آژانس بین‌المللی انرژی درباره بحران بزرگ سوخت به صدا درآمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121104" target="_blank">📅 17:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121103">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a498aecac.mp4?token=shu3CLpWaepxAem5JdRt5ZkepZeZOrpPB26OyZI_KHon7Y8Y1KrN1zbeAiy2-RQ8afBILI1_9v3p1N3MLDTFaOzB6e5B_sn_6kotbr_kxxWJ8TnzkpUc4Ab4iAW15Y8_FKqCOQqtOsuHQmtFsAz-UFkzhIvc4ooZF4y72IRe3PSVrvgRpX_AAtwEEvtLHs-08BqCbWZnSs3UM9pdprmYp3qXo3t58pONsWV1adkcEPtcgtIMU1KqkyNhQX_pKZT8Xe4Qmloq3gTIGG9Czx4IX9_tQ6Yp7eostiE75bcMGrnPkU21GrWa32lnbadiCg_53fUpyL9xwCktD2ZNDBIERU9LZt3rIS_Nh3ngKN2715hev-ZVojnf5iYVVPyIrQp0TNKB4r5eUbHtAL4MD9zi3Ai8WKeiUOgJj0U7Y_Y0UdZN5Nt9Ysc2LoCnyLd-AqjuHAQKedzrHw_l9st7aET5GCOX_rJ7pwJXH0SedSgFPN_tfy9aOFrkzeIbaYZCCGErBE5gd5m9jrFmaDuGUvniIR68QrcHoc3u1EyoJVAyuzknCw1XAoJidcdtxSi0oQbOKID2K4B7U0Hl7eIthtZ0YfxlAy6pequJp0f4uvQY9u9zfA_Q90F1EQHV1lGWVChZx-fq2KZ-sfqSWWEzgYPV6e0JAfdsNar7xT89csXXWrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a498aecac.mp4?token=shu3CLpWaepxAem5JdRt5ZkepZeZOrpPB26OyZI_KHon7Y8Y1KrN1zbeAiy2-RQ8afBILI1_9v3p1N3MLDTFaOzB6e5B_sn_6kotbr_kxxWJ8TnzkpUc4Ab4iAW15Y8_FKqCOQqtOsuHQmtFsAz-UFkzhIvc4ooZF4y72IRe3PSVrvgRpX_AAtwEEvtLHs-08BqCbWZnSs3UM9pdprmYp3qXo3t58pONsWV1adkcEPtcgtIMU1KqkyNhQX_pKZT8Xe4Qmloq3gTIGG9Czx4IX9_tQ6Yp7eostiE75bcMGrnPkU21GrWa32lnbadiCg_53fUpyL9xwCktD2ZNDBIERU9LZt3rIS_Nh3ngKN2715hev-ZVojnf5iYVVPyIrQp0TNKB4r5eUbHtAL4MD9zi3Ai8WKeiUOgJj0U7Y_Y0UdZN5Nt9Ysc2LoCnyLd-AqjuHAQKedzrHw_l9st7aET5GCOX_rJ7pwJXH0SedSgFPN_tfy9aOFrkzeIbaYZCCGErBE5gd5m9jrFmaDuGUvniIR68QrcHoc3u1EyoJVAyuzknCw1XAoJidcdtxSi0oQbOKID2K4B7U0Hl7eIthtZ0YfxlAy6pequJp0f4uvQY9u9zfA_Q90F1EQHV1lGWVChZx-fq2KZ-sfqSWWEzgYPV6e0JAfdsNar7xT89csXXWrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چی میشه که 57ی ها این سخنرانی ها رو شنیدن ولی گول ملاها و رجوی ها رو خوردن؟
🔴
دیگه چه توقعی از بچه‌هاشون و همفکراشون دارید؟
🔴
معلومه درکی از پیشرفت ایران ندارن و نمیفهمن سیستان و بلوچستان یا خوزستان و آبادان چقدر میتونند پیشرفت کنن.
🤔
ایران گلستان رو تو همه موارد چه اجتماعی چه اقتصادی و... به جهنم تبدیل کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121103" target="_blank">📅 17:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121102">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا : دنبال سرکوب جهانی شبکه‌های بانکداری مخفی ایرانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121102" target="_blank">📅 16:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121101">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
الجزیره: تعویق نشست شورای امنیت ملی در کاخ سفید
🔴
یک مقام آمریکایی به الجزیره گفت که نشست شورای امنیت ملی در کاخ سفید امروز، پس از آن‌که ترامپ حمله به ایران را به عقب انداخت، به تعویق افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121101" target="_blank">📅 16:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121100">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سفیر چین در تهران: حمایت پکن از ایران، آشکار و بی‌چون و چرا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121100" target="_blank">📅 16:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121099">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t06ImnqxwNUObOTvhT02pudxY7YV1i_mR8wejWL-z6nNTsOI-RAxwTutDpzs2BB7rjlmjliEEf5Y49JKgfxYxNTwQ3PvATDio5NFFdXqnWx-WUNoNDRt36_dMw8GmpWvt38Tbm1KW4-1tlX2vgqNnkan-hT3ecKeLbPV9iJTnU1tUK-q7DqnjHQVACy2nXa_CkgC25k6WUrhPWdSgPqVZG5TZ6bEQyd9JUH_SDg3wKxITwY02nvaUqAgAY8ZdwQBJd0NIvRKA4IQZL-7x-7Zp45L85Z0_IyoRl-bAzPY7rSlAAjDCc1RDgPZmzkiS9QI2tCVrkAdrysHoUx3Wfpkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین گزارش فایننشال تایمز درباره دیدار شی و ترامپ را «کاملاً» رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121099" target="_blank">📅 16:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121098">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وضعیت هوای تهران قرمز (ناسالم برای همه) شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/121098" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121097">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a474872a0.mp4?token=Vn_PlHfw-DqZj_xwX4Oc31NZbRb_A0qkGxq8eXpDIdFtul4XDxjK-dX3d3-OglMooB8AC-5TQfqQh5NUpCRnlYk92e7XyuZj-TvA4aBD1QoozsDAwjSkETro_YftmqwU7k54t8v7PjEn7RgfATGiVTWw8PWEtPiI0NBoDqPRplBOf3qvFU9ZbBI-JvVF6Jc8ro-gcXNKp2kve3L-ffQ63SRNfjQ8GFMAsuWHCULlbuJBiYCtZ0QFiIaMtX5CvuNhQLSQWKpgkcA4jXk1W6lYSFCazLDOn7gjzueJih2oTl5enWNCzVVT0Y4OO5TUrbyOCP3UPI8BOc2PAqL5RyVOeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a474872a0.mp4?token=Vn_PlHfw-DqZj_xwX4Oc31NZbRb_A0qkGxq8eXpDIdFtul4XDxjK-dX3d3-OglMooB8AC-5TQfqQh5NUpCRnlYk92e7XyuZj-TvA4aBD1QoozsDAwjSkETro_YftmqwU7k54t8v7PjEn7RgfATGiVTWw8PWEtPiI0NBoDqPRplBOf3qvFU9ZbBI-JvVF6Jc8ro-gcXNKp2kve3L-ffQ63SRNfjQ8GFMAsuWHCULlbuJBiYCtZ0QFiIaMtX5CvuNhQLSQWKpgkcA4jXk1W6lYSFCazLDOn7gjzueJih2oTl5enWNCzVVT0Y4OO5TUrbyOCP3UPI8BOc2PAqL5RyVOeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تلگرام به خطر افتاد
‼️
🔴
بابک زنجانی رسما فعالیت شبکه اجتماعی خودش به اسم «مای دات» رو استارت زد تا این سوپر اپلیکیشن با تلگرام رقابت کنه.
🤔
از جیب ملت به نفع حاکمیت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121097" target="_blank">📅 16:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121096">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نیویورک‌تایمز: اظهارات ترامپ درباره تعویق جنگ ممکن است فریب باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121096" target="_blank">📅 16:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121094">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjCh3jM5HAS7GbxGjLKkZKCf4JcmBYot8HcKMCDKBa0YtLlZU4cdnT3aDzM2utyeTbm_eURRuql6mZqxpegzCrtov3KB1nWsACeQ09fsGgNd2SfJqycq8L6b4fo1aPiSBJ0IxdrvKg2HMkO1xLGBKeGyOk1bbgGYRjbOdPATJHP_uRRYPA5Tp20NuIbRapgqs2bsxAPl5qy2rohy0lr3tqzBAdjQgDoruHP4AllfxBkSVUFInD4cRsak4kqDXNHG6rY_mlGy8YIL5dir3yR58EBvpfTX0pguEvp2iloqe5fV2Ztiky2-iNI7CKcW52GDFVx6aXkd1MRV_ecatyrnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با حضور کریس رونالدو
🏆
🇵🇹
لیست تیم ملی فوتبال پرتغال برای جام جهانی ۲۰۲۶
@AloSport</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121094" target="_blank">📅 16:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121093">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4iIwOvgS1IoTw5Etz76ey-KNT1UkooOUz36onHHv0lHa6BZDDNPO0ZlgVmCzDIuwUXiU78dHqOcuow1UMQBoZE4PZsWiHAv5dDBbdMSatnrTgnyevxbJtdNwaXWwMfI7tToMWl-L6i0yx3dGpr7i5xlFLUWGssNx-_pzyOh7FViQPxXB58yeLkqlCpgWgj-3azQggW6ldvHDp6w83q-JBpy_Z2_lO5SGCqcPt1UDGvwr1PQeo6WBu9-FBwJWW2smO_ugNJ2DSX2p49eTGLuzrs-PuapJpd0gKlMTajx6IXQd1_jR5fcfYczGFTQlAzjlrzPitKigHHgeGDFBnRI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: نیروهای سنتکام ۸۸ کشتی تجاری را تغییر مسیر داده و ۴ کشتی را غیرفعال کرده‌اند تا اطمینان حاصل شود که کاملاً مطابق قوانین عمل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121093" target="_blank">📅 16:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121092">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👑
مرگ بر سه فاسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121092" target="_blank">📅 16:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121091">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpzgLOigXXXEfFIYtezUNq090y-nLQx0tQzFE-NNyk5oma9mpfDn_Rte_934VUe7nj23tgz2CKRf5_3TmUQBjB9OIbLLjsy6-xuaIGZk_jQVvhMqLjbYTNHgINUkXLdWVA9VzQ83ErvGgITFfErYM-g1_t5oSxIN7H2iK8FgearFyFHrTQaCxGLgDDbbgraULZJIUDNZQwtnmgyk1Fej46_ElWLzi_FdhUv6ctqpcbPAH4uYcPPh2R1wKQuCwIi3kRUA9i1g7vf26P6te09dRY3zpjudITQh4jsmD-tJzVaRncpSijNo5KVlzjBKLsMDotiv-I5xeTtOv7MoMx8d5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار بلومبرگ: آمریکا هفته گذشته حدود ۹.۹میلیون بشکه نفت از ذخایر استراتژیک نفت(SPR) خود را به بازار تزریق کرد
🔴
این یک رکورد بی‌سابقه در جریان روزانه‌ی بیش از ۱.۴ میلیون بشکه در روز است.
🔴
دومین هفته‌ی متوالی است که نرخ تخلیه ذخایر استراتژیک رکورد می‌زند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121091" target="_blank">📅 16:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121090">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خوش چشم؛ کارشناس صداوسیما: موشکی که کنار دیمونا زدیم از جنس خاص بود و زمین رو سوراخ کرد و اسرائیلی هارو رو توی یک پناهگاه خاص کشت/ اگر دوباره جنگ بشه فقط از اون جنس موشک می‌زنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121090" target="_blank">📅 16:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121089">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رئیس مرکز ملی فضای مجازی: در ایام جنگ روزانه ۱۰۰ حملۀ سایبری به کشور می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121089" target="_blank">📅 16:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121088">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25a8ea39e7.mp4?token=j6_FE1NkeRhzB5l6AaYPAwtfpTrr7nRMKdgZoZFfcvBJ0JVklR4onIpc1A0pp4pXnMK1yryC25hKNAZcmrg2FJIAx-pG_E6rngMx0Y6KKZv37k39S6eJjsaNt7_FK9xMaev8KCJ060_O58qPsps3tHtfKE4TY-QnWEb26TRotRjAM8lL3VnCFG90GuJVu9hAqmcsCNh-MT5reADu1p4Z1oVZoAqIEbqPWlAJ6LmhjfZwpToBPBnp2zKKTVb2f3DpbjwMyx1U3KcGveL9vlW704S2CcSASasYoJTmxKoA_TBqrDb1Wslsy8tEmfMX1U3d_PWn9HfUiMjtUz3GF5G8XWuEJGQxuicIg8UCgVpEpxSOFyC5pSJzCz57xQq70O0gt4z05TwHX2-7kHB0j8IuEh3XcPIlXN-H8ofbg1Z8HVOPp7p30zSuGLPmNCHGQsRN4Seo442U7s1aejfu48YtT9HMlef0bXBzZQUsgMlisQmMIjzEsKGv-DYgCFw9yb6ZgVeN0-UBhrdRIC9oEM01XbJKO6WIC6NpMMqhm3XSGsvNO7ILLh8aFyuRgOjowNsZ2IK3zGX1O4EVUrAhKJ01ruv1I_uDukYAYAJVtgijNq9MEEzhyjhVgYu1yYyZ85M7VJpi7zu3EjckUKFgsRgJCx2VXUxo6QuLueg_00LAwVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25a8ea39e7.mp4?token=j6_FE1NkeRhzB5l6AaYPAwtfpTrr7nRMKdgZoZFfcvBJ0JVklR4onIpc1A0pp4pXnMK1yryC25hKNAZcmrg2FJIAx-pG_E6rngMx0Y6KKZv37k39S6eJjsaNt7_FK9xMaev8KCJ060_O58qPsps3tHtfKE4TY-QnWEb26TRotRjAM8lL3VnCFG90GuJVu9hAqmcsCNh-MT5reADu1p4Z1oVZoAqIEbqPWlAJ6LmhjfZwpToBPBnp2zKKTVb2f3DpbjwMyx1U3KcGveL9vlW704S2CcSASasYoJTmxKoA_TBqrDb1Wslsy8tEmfMX1U3d_PWn9HfUiMjtUz3GF5G8XWuEJGQxuicIg8UCgVpEpxSOFyC5pSJzCz57xQq70O0gt4z05TwHX2-7kHB0j8IuEh3XcPIlXN-H8ofbg1Z8HVOPp7p30zSuGLPmNCHGQsRN4Seo442U7s1aejfu48YtT9HMlef0bXBzZQUsgMlisQmMIjzEsKGv-DYgCFw9yb6ZgVeN0-UBhrdRIC9oEM01XbJKO6WIC6NpMMqhm3XSGsvNO7ILLh8aFyuRgOjowNsZ2IK3zGX1O4EVUrAhKJ01ruv1I_uDukYAYAJVtgijNq9MEEzhyjhVgYu1yYyZ85M7VJpi7zu3EjckUKFgsRgJCx2VXUxo6QuLueg_00LAwVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر فرهنگ اسرائیل، میکی زوهار:
کمپین هنوز تمام نشده است. ما هنوز در میانه آن هستیم.
🔴
دو روز پیش با نتانیاهو ملاقات کردم و از او پرسیدم: «چرا هنوز به پیروزی نرسیده‌ایم؟» به او گفتم که این چیزی است که شهروندان اسرائیلی می‌گویند.
🔴
و پاسخ او این بود: «ما به آن دست خواهیم یافت.»
🔴
ما تهدید هسته‌ای ایران را از بین خواهیم برد. ما حزب‌الله را شکست خواهیم داد و حماس را نیز شکست خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121088" target="_blank">📅 16:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121087">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رئیس روس اتم: قادریم برنامه بازگرداندن کارکنان نیروگاه بوشهر را اجرایی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121087" target="_blank">📅 16:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121086">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2718f30e4a.mp4?token=k1NDQuVvP3CerBxvMNM4zelNX2anFI4IpQkmY41B-av8W2IU8VIlkqRge5fPJLcjI4NviUr2wL9CybrVICgD_d4aE_aeNe4IMOtx1B-pb3_8s3knQTuboKnF1NQVlEH5ap3-fAr-wSjfuHj1o2x3XCQCg4QEaxYQnrpHSGuNPOrkwbPZpUxEyTGyjIyn8hSaghMuy2pB5J0l3jeYuWDedVgjnbxNDb4nA05Fve7nN66P1e7kTHAB4PdQeh2nIGM1Y7NeTImc9nQXD547BXuUDAdmLSE22iEyTnlgQCsUu_ZJsRpppSFg0A9rWLPHcER4Qj6giw6CziU9tBWyAalcfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2718f30e4a.mp4?token=k1NDQuVvP3CerBxvMNM4zelNX2anFI4IpQkmY41B-av8W2IU8VIlkqRge5fPJLcjI4NviUr2wL9CybrVICgD_d4aE_aeNe4IMOtx1B-pb3_8s3knQTuboKnF1NQVlEH5ap3-fAr-wSjfuHj1o2x3XCQCg4QEaxYQnrpHSGuNPOrkwbPZpUxEyTGyjIyn8hSaghMuy2pB5J0l3jeYuWDedVgjnbxNDb4nA05Fve7nN66P1e7kTHAB4PdQeh2nIGM1Y7NeTImc9nQXD547BXuUDAdmLSE22iEyTnlgQCsUu_ZJsRpppSFg0A9rWLPHcER4Qj6giw6CziU9tBWyAalcfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر فرهنگ اسرائیل میکی زوهار:
مسیحا چیز خوبی است.
🔴
این چیزی است که همه ما می‌خواهیم هر چه زودتر بیاید. حتی رئیس ستاد، فکر می‌کنم، می‌خواهد مسیحا بیاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121086" target="_blank">📅 16:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121085">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48fee383d5.mp4?token=lOPYWNjxQGEdw5WE9MMT-B42ZLy2eGIHAWyvKvRNm6iFeKaQP4HL7QNYsgBD5WlzIqRV77B-_7Yeo9GMATmsDpMTgoWfsjgn-2YE1uXkOPN5pqxzJ6EeoODFNER-BmEQRPlKA-Jw_hjNg0xtrcEx2gCvB2EsA9-vw4kgnKVLAWYVoW3svn2-LOlSf9xa5r7X6Jrbdy2kkG7aibbe62pkX6RS4s8JpqAm9pkQ14Z00J8ZB4WQ8hjvKxCBwO3PAbia0-_Mr2ddLJ68lAFEScdcYmzf9K9syaDNoAx2fpJY1mJES3KjvGCiwTN8y7i5jROH9a-lnr_hSd5aMlfJvpMs3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48fee383d5.mp4?token=lOPYWNjxQGEdw5WE9MMT-B42ZLy2eGIHAWyvKvRNm6iFeKaQP4HL7QNYsgBD5WlzIqRV77B-_7Yeo9GMATmsDpMTgoWfsjgn-2YE1uXkOPN5pqxzJ6EeoODFNER-BmEQRPlKA-Jw_hjNg0xtrcEx2gCvB2EsA9-vw4kgnKVLAWYVoW3svn2-LOlSf9xa5r7X6Jrbdy2kkG7aibbe62pkX6RS4s8JpqAm9pkQ14Z00J8ZB4WQ8hjvKxCBwO3PAbia0-_Mr2ddLJ68lAFEScdcYmzf9K9syaDNoAx2fpJY1mJES3KjvGCiwTN8y7i5jROH9a-lnr_hSd5aMlfJvpMs3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای کماندو دریایی ارتش اسرائیل به تصرف کشتی‌های ناوگان جهانی صمود که به سمت غزه در آب‌های بین‌المللی حرکت می‌کنند، ادامه می‌دهند.
🔴
کمتر از ۱۰ کشتی از ناوگان در مسیر غزه باقی مانده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121085" target="_blank">📅 15:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121084">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بریتانیا هشدار داد : اگه تنگه هرمز بسته بمونه، دنیا خیلی سریع داره میره سمت یه بحران جهانی غذا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121084" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121083">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هم اکنون زلزله در استان لرستان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121083" target="_blank">📅 15:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121082">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYPL1geXNk3GKbALs_bW081s1cNHfHe-TSf6kMcgCl4uMTQnGxyP-4kfsBqYUP_gNGNymytKG34aa4vviwr8UkaC1KQHhoMTA1oz5vtrMcu0FIdbzT0Mfw1cpHsjHiLnOasGdRRUSNzJCwAT6pg_NAUVJuyvcWDKJGvQJ6wGXNIn824wkLOvJ2tcNVSeOrHSUGQRBC_Z0wSAbW4DzPXMUBOWIP1lhgVsKhKCbc31aofo7MnIb-xW_Qf19NBhxtA1oovH2oHbSwc-CsyxMEeKIBzpCLs8XWIkrzi12fSRpS-JC9tdlyUQcF5zmLktZUZlPkeX9BRLbZD99E7ZoQtFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
"بریتیش ایرویز" پروازها به اسرائیل رو تا ۱ آگوست به حالت تعلیق درآورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121082" target="_blank">📅 15:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121081">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ادعای یک منبعِ اسرائیلی : یه هواپیمای مرتبط با موساد به ابوظبی، "امارات" رفته
🔴
درباره‌ هماهنگی برای اقدام مشترک در صورت حمله احتمالی به ایران صحبت کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121081" target="_blank">📅 15:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121080">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ گفت که پس از درخواست رهبران کشورهای حاشیه خلیج فارس برای زمان بیشتر جهت مذاکره، حمله برنامه‌ریزی‌شدهٔ آمریکا به ایران را متوقف کرده است.
🔴
با این حال، چندین مقام عرب خلیج فارس بعداً گفتند که از وجود هرگونه طرح حملهٔ قریب‌الوقوع آمریکا بی‌اطلاع بوده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121080" target="_blank">📅 15:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121079">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZoF8WVP7Kd-rlLSuiTtTRhs-GWNGEZa_gOQBO1TOuvmO150MEr0zGnVot22jaCGlEv4EmQRgagTk416e2qTgBq_RYclmkdn3Oq61NTiWGwKwufUwrwnXc1JQdNPGxaORwDp39mC3g5dOVNLXV7n_ovhYjqSPZgpPpRpCKalJvHIAt5c52Hrrul54iP838-B4rVzRWIs2JBuJGVjMuN4QDAKt2VBMoEGbQNuzBRuiwRptewp4uln8Bomm4IJ8mWw-ONF5k4Bhn--njtMU9mLnQlzphnJFACe-QHwcWlQ3HCxkREzHqbJ-rcyc8I1JG-BLnTYNcbz6EC0hUNqFMw0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده جمهوری‌خواه توماس ماسی:
من انتظار این را نداشتم، اما انتخابات من به نقطه عطفی برای کل کشور ما تبدیل شده است.
🔴
امروز ما تاریخ‌سازی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121079" target="_blank">📅 15:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121078">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
هم اکنون زلزله در استان لرستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121078" target="_blank">📅 15:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121077">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376babfab.mp4?token=aOSx1jsJNym5vRol4s4pDYSlXrE7vcq6h9a4INIZw5qRQY3L9SW52TCKDzth6bw6A2Sf91YFt9jRl_glVhWNH_zy8TphQ7FMUq7c7yS_ksQCqHMoMZM6ksMD8T78qpoOoA0hWv6KXfej9wrF29hsPyCvh8b1NkiTLMfPUNLR4CuoU9EPw_b6fGN69xx99cDcj7scUJRGbWFFLff4TfTbiAgsQoQKQRLLiWojmNyp4qquZSSXHl2cPOTjkKjtr_ImumKB9ODm3Q4m9tSqvkeTN6fYNHHEWc_i57XtJ080oWBgKi-MPUDMaFKibhJM1_QDVOLwmAEAv6YpH_Hy7IB_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376babfab.mp4?token=aOSx1jsJNym5vRol4s4pDYSlXrE7vcq6h9a4INIZw5qRQY3L9SW52TCKDzth6bw6A2Sf91YFt9jRl_glVhWNH_zy8TphQ7FMUq7c7yS_ksQCqHMoMZM6ksMD8T78qpoOoA0hWv6KXfej9wrF29hsPyCvh8b1NkiTLMfPUNLR4CuoU9EPw_b6fGN69xx99cDcj7scUJRGbWFFLff4TfTbiAgsQoQKQRLLiWojmNyp4qquZSSXHl2cPOTjkKjtr_ImumKB9ODm3Q4m9tSqvkeTN6fYNHHEWc_i57XtJ080oWBgKi-MPUDMaFKibhJM1_QDVOLwmAEAv6YpH_Hy7IB_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع نظامی گزارش داد که یک خودروی بمب‌گذاری شده در نزدیکی مرکز مدیریت تسلیحات سوریه (وابسته به وزارت دفاع) در پایتخت منفجر شده است.
🔴
همچنین منابع محلی از شنیده شدن صدای تیراندازی خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121077" target="_blank">📅 15:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121076">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وال استریت ژورنال : چندین مقام از کشورهای خلیج فارس که ترامپ هنگام گفتن اینکه تصمیم گرفته حمله‌ای که برای امروز علیه ایران برنامه‌ریزی شده بود را به تعویق بیندازد، به آنها اشاره کرد، گفتند که از برنامه‌های حمله فوری علیه ایران که رئیس‌جمهور ترامپ ادعا می‌کند، مطلع نبوده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121076" target="_blank">📅 15:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121075">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c489e1b78.mp4?token=uhM0S7tdbUwE96b4m0n5KauzwOwJ-ttm8NunzfWh32AIxXbVbniYBmGPazPUlic6KPS_RHlo4lZCW4ysBHLDW7Xwxmo_o1YtUIxkObc4rIux9aSstvtav8t9Zng67wwMBRWQo2wLuFtuZNWKOh1YfDWq1pAlM3kxmB9mqEUkhZ8Irn5ndQX1sV6WXMKyMcMPjxijiK9h1Hc6vmmBv36j9M_AKrf06TMpMkW1y6dbr-yInsH2rqEQX8O7Uw1WIE3KX2VQj9ytv5ZuwowZPSk-_vcEEzHyPOSsMgTFBSPj5qdeaH8Rv7HYLA1irHWf6sgnvFj09nGNmpK_3X17cygqOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c489e1b78.mp4?token=uhM0S7tdbUwE96b4m0n5KauzwOwJ-ttm8NunzfWh32AIxXbVbniYBmGPazPUlic6KPS_RHlo4lZCW4ysBHLDW7Xwxmo_o1YtUIxkObc4rIux9aSstvtav8t9Zng67wwMBRWQo2wLuFtuZNWKOh1YfDWq1pAlM3kxmB9mqEUkhZ8Irn5ndQX1sV6WXMKyMcMPjxijiK9h1Hc6vmmBv36j9M_AKrf06TMpMkW1y6dbr-yInsH2rqEQX8O7Uw1WIE3KX2VQj9ytv5ZuwowZPSk-_vcEEzHyPOSsMgTFBSPj5qdeaH8Rv7HYLA1irHWf6sgnvFj09nGNmpK_3X17cygqOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل بیش از ۲۵ هدف وابسته به حزب‌الله رو هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121075" target="_blank">📅 15:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121074">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نیویورک پست به نقل از منابع پاکستانی:
ما همچنان معتقدیم که مذاکرات غیرمستقیم جاری میان واشنگتن و تهران پیشرفت خواهد کرد.
🔴
نسبت به امکان دستیابی به توافقی دوستانه میان ایالات متحده و ایران خوش‌بین هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121074" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121073">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
صدای انفجار در قشم مربوط به خنثی‌سازی مهمات عمل‌نکرده اسرائیل و آمریکا بود
🔴
معاون سیاسی استاندار هرمزگان: صدای انفجارهای شنیده شده ظهر امروز در جزیره قشم، ناشی از عملیات خنثی‌سازی مهمات عمل‌نکرده متعلق به اسرائیل و آمریکا بوده است؛ ممکن است طی ساعات آینده نیز  عملیات انهدام مهمات عمل نکرده ادامه داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121073" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121072">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نیویورک‌تایمز: مقامات نظامی آمریکا می‌گویند که ایران تاکنون تاب‌آوری فوق‌العاده‌ای از خود نشان داده و هم‌چنان توانایی واردکردن آسیب‌های جدی به منطقه و اقتصاد جهانی را دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121072" target="_blank">📅 15:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121070">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qjad4gR7QIKG4frIkbQziWnvXUaDnoPX4In3ecC-Pv6ZaEKpayOuxw4LH8QCh-AXdz7yWakbFLnIIxGmKB9-xP1daoOwAujgbLE4tG0cUDO6Q8HgOESPHtmoQENpLhNvcv1IqU6lGsRr5OMXvGa18On2e1Mebhk37P3DOGEqcGezoRgdjbdV9sQcbEZALv3RRlaeN9SE2pARqqsKrWFH7tUp2hjj1lHifz9FveYWuaAlaLIgxDhuSBuFybapDCqutKUp-Li7e63F_YWmZWIPckepcLuykP2ELK5xvdtINKX_Aou9xex97Z9PUknk6OVwRdly8XV6JrSU34tKmJq31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-KyJWuhtxlMLb3OgyGMrye1OUlEkRS-uWloXIlok8TFowQJRlP7RXjc1EFC5kmLVLQVUithBTQNKPu5zPAYeFU85otrCtUJyF6OaSGjjwI1CXlzZppDn7xKl_tps-RPfOFEL0VEDstKLYBbS9Xc6UoTSKGUjT8BDi852hUwth68rxoBWlrRCCyss2IXS9bFjapAQWM9qGCP8LS43RmRCeOWawYPLXUrUNNEPlQRSQetjFdKbXFg6SZyLhwi21g0IgTaBFUtPM-dxRuaBHSgGT_xqUgkitb9ZhX5G12YxV6JnNZIg2JSApKHkm0pN3vsr8936434lP2TRC3BVzSEsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیروز هتل تاریخی عامری‌های کاشان به علت بی حجابی پلمپ شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121070" target="_blank">📅 15:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121069">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
آی ۲۴ اسرائیل:
انور قرقاش، مشاور رئیس‌ امارات طی اظهارنظری بدون نام بردن از عربستان سعودی و قطر به دلیل تماس‌های مستمرشان با ایران، این احتمال را پیش می‌کشد که ابوظبی برای درخواست از ترامپ جهت خودداری حمله علیه ایران، تحت فشار قرار گرفته است.
🔴
قرقاش گفت: «آشفتگی نقش‌ها در جریان این تجاوز(!) ایران حیرت‌آور است و کشورهای پیرامون منطقهٔ عرب خلیج فارس را در بر می‌گیرد. نقش قربانی با نقش میانجی و بالعکس در هم آمیخته است، در حالی که دوست به جای اینکه متحدی استوار و حامی باشد، به میانجی تبدیل شده است.
🔴
«در خطرناک‌ترین مرحله از تاریخ معاصر خلیج فارس، در میان این تجاوز(!)، موضع خاکستری از بی‌عملی کامل هم خطرناک‌تر است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/121069" target="_blank">📅 15:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121068">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر: عبور اخیر دو نفتکش حامل گاز مایع قطری از تنگه هرمز به معنای بازگشت دریانوردی به حالت عادی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/121068" target="_blank">📅 15:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فرماندار اسلامشهر: عملیات خنثی‌سازی مهمات عمل‌نکرده، چهارشنبه ۳۰ اردیبهشت از ساعت ۷ تا ۱۰ صبح انجام می‌شود؛ مردم در صورت شنیدن صدای انفجار نگران نباشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/121067" target="_blank">📅 15:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVMyx7FeI-0HpCsqT7ZvR4gGF_pHbxLYD5nCeRu32mYHEtqhvt5Wapcg-BvWv_4yEPBMkv9J0UItuP06Y0Yel39q5o7IjjwjfPJ0s2bSOjT_5plhzzHsciO-cH-dW4ccpZjoKcse2xKidRmYi0haXXViHezucJKpI4-heJpiCRDft7gc0lLb1mcYnNEzDgn0uTpXjvR21VcA0cKWuf9DOUY9H7DDJFCDize5sg9RtO8dqeXTRaoMpCVjSTYae4kzybtzJXbZR68g-GiRXWWiyg9yj4yM2efB4PdRI2nq5ltzSCS4Ut_LFbZwh5KXFjveL0Th1xJZ7bnkfM-NJ7Q8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری سردار آزمون و آرزوی موفقیت برای بازیکنای تیم ملی
@AloSport</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121066" target="_blank">📅 15:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121065">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3Zj7zeDb0aIwtg6J-aMblHsJ4GvVGGHdUFh1XIa7Lg6R5G4_5P9KW9GCp27s7dRy_66FzSnlg32Ri4ln3a_rwMU85VVFXEs7trJJWzY-B4BIgqRQO3BfwzabEA8BAFUblycvm5lD1t0TvYc4QSPyoDaPIYKJXMlb4Uk7ms6ISKRe55gZnu6fWgnT_zXtmASZyeaM5tv7rVXLrjUTl7QIqSPVUZ8aHXhf0sQ4ChuIjI6BVl9M-kILh7-9NzD_jq9VN4aDurMlEUV2oEBg9bO5Kf2qeJWDCk5MPSW8lyN3RiF6GL7XqbsKRDNaBd-qaPhE_NP6JLBjYx8arx78M2a1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عفو بین‌الملل:
تعداد اعدام‌ها تو جهان تو سال 2025 به بالاترین سطح ثبت‌شده تو 44 سال گذشته رسیده و
اعدام‌های انجام شده به‌دست جمهوری اسلامی
، اصلی‌ترین عامل این افزایش بوده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121065" target="_blank">📅 15:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121064">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وال‌استریت ژورنال: چند مقام خلیج فارس از برخی کشورهایی که ترامپ به آن‌ها اشاره کرده بود گفتند از طرح قریب‌الوقوعی که او درباره حمله به ایران توصیف کرده بود، اطلاعی نداشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/121064" target="_blank">📅 14:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121063">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0E3KEABWxLRSu2q-FnJmGEPV0DAxPyXzOOatrJPkPIk5gs2J3-oU4TULNhiElVber_e86OyJM7CbpxKfTDGgQOw3i8jRuIoPO6FWQ7dNqVACnOHk9OoPc4O6cnVTcnBIr5exj5E3OWdbDkXFhtd6M2rq8-8c_egir58CGn9mKLUeiNlMN-JnAMXrqLUG_IOpwEo1q2__YXdRTR1Eck1n7TgTq3X4jMTVH6-_VPkF3U44ttd-m3ET1wSSyzE1-F-DoAN7kaoOYyySC0SVNHY91TTYVdsVEkGzxl3BM65r8CdEb0rILwVTiKrdLXEScJrSwLqMnqkcarenp7s7wyxnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حیاتی، معاون امنیتی خوزستان:
🔴
امروز تو اندیمشک داشتیم سامانه پدافند هوایی رو تست می‌کردیم که یه پرتابه‌اش به یه ساختمون مسکونی خورد و 4 نفر زخمی شدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121063" target="_blank">📅 14:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121062">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/753ce7959f.mp4?token=REZZPz_FVHdFXy-QCngvw-eKR99D-xxGy-ktY4znSrj47I7Ey7QOn1BhitUwsHAz_Ze2nhNCL8ca-IfOco-H3ToUhG332wVwT8KKM7MWSPdX-mgJRSemLTbLVk7YFOnpFLyIhl3vEsIKJP0eP9dE1PuF7onp2j2bNMXYpvOljqI73EiRPSDIkRuYIwNeMXfcjRwVXryrkAyESoDh9T9lunuXR69xNgDtJaYc8Id9YaBsi3YPWwMFX2ZH7xgqIntv8z_JJ9iRVc1R0UASH-Yz4qK9ZfpuDajo3bcUfm-2w5Xe157-BZ3qlOZgmZy-eyDisb7zwCKcUaD2zvYp0DCWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/753ce7959f.mp4?token=REZZPz_FVHdFXy-QCngvw-eKR99D-xxGy-ktY4znSrj47I7Ey7QOn1BhitUwsHAz_Ze2nhNCL8ca-IfOco-H3ToUhG332wVwT8KKM7MWSPdX-mgJRSemLTbLVk7YFOnpFLyIhl3vEsIKJP0eP9dE1PuF7onp2j2bNMXYpvOljqI73EiRPSDIkRuYIwNeMXfcjRwVXryrkAyESoDh9T9lunuXR69xNgDtJaYc8Id9YaBsi3YPWwMFX2ZH7xgqIntv8z_JJ9iRVc1R0UASH-Yz4qK9ZfpuDajo3bcUfm-2w5Xe157-BZ3qlOZgmZy-eyDisb7zwCKcUaD2zvYp0DCWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دختر قاسم سلیمانی:
🔴
گلشیفته فراهانی پدرم رو‌ به عنوان قهرمان ملی بسیار دوست داشت و صحبتی هم تلفنی با پدرم داشت(که مشکلی که داشت پدرم برایش حل کرد)
🤔
ظاهراً بهزاد فراهانی معروف به بهزاد بیضه هم علاقه زیادی به قاسم سلیمانی داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121062" target="_blank">📅 14:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121061">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d09f4ac55e.mp4?token=HY_pnB2Y3aX5lAR2HJhYszQNZsS4fPoESI03-K3aoiuSmo-Eun6JwQ2rTNdfDMXPUIAATRIZ_CCBP_b5Frj_M0nBjz7KSJZhHHvp4d7O2usLyw7UDNKqL9_TyRk2817oDw1oSR1jSl80JLUrWq3pDxITKiCWgA-zmDBcBgQ_S9JVVGKdOi0S8LP2gGtxRQ5ZrlHhqm-do3l458jrqaHtKVrMG-aPFPQvSpvzOtG9o5lRwiiRKq-fsau6MrkYQ9pR43fT83jFsOp3-EkUrp4S4J_wR7UdrMdbaBjGA8o6886A-SRnx79m1jv1yThQZNtpXyOQtUsXfMlqeAfVv6xFug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d09f4ac55e.mp4?token=HY_pnB2Y3aX5lAR2HJhYszQNZsS4fPoESI03-K3aoiuSmo-Eun6JwQ2rTNdfDMXPUIAATRIZ_CCBP_b5Frj_M0nBjz7KSJZhHHvp4d7O2usLyw7UDNKqL9_TyRk2817oDw1oSR1jSl80JLUrWq3pDxITKiCWgA-zmDBcBgQ_S9JVVGKdOi0S8LP2gGtxRQ5ZrlHhqm-do3l458jrqaHtKVrMG-aPFPQvSpvzOtG9o5lRwiiRKq-fsau6MrkYQ9pR43fT83jFsOp3-EkUrp4S4J_wR7UdrMdbaBjGA8o6886A-SRnx79m1jv1yThQZNtpXyOQtUsXfMlqeAfVv6xFug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریمیکس «تو رستم تهمتنی» این روزا تبدیل به وایرال ترین کلیپ اینستا شده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121061" target="_blank">📅 14:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121060">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3115a5f2.mp4?token=fGpBhF5e1mJ_GLlryiLjt7iTUqkULJ7fE6Tt9UcOfa4wJ-ziTwGQqD5AiwWfrHm6EJ_wVIWgUVIEhutek4Js_913qGSCmWBEq5tZIUkDooaJ0fr7gCxMAbYM6rV-g9wttIbywxMrFNEZYhE9I81847FWDgK4R1kXxLeG37Rd00Zu2vB3ibLdIF5snSdYxJtfb2klLp93jrGRTU53KQFWDzdqO1rsR8SsVz9EO9UeF_jyZQ5FZMLo6a1tC3dUJ1ggG0Z2opfLxtlv3gkeqgFKh974VCwWggUrJjyibDv2iQhG-JtT23_MXnsS3VAVh6l7GkovG2Gjeek1SBDtnmuCLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3115a5f2.mp4?token=fGpBhF5e1mJ_GLlryiLjt7iTUqkULJ7fE6Tt9UcOfa4wJ-ziTwGQqD5AiwWfrHm6EJ_wVIWgUVIEhutek4Js_913qGSCmWBEq5tZIUkDooaJ0fr7gCxMAbYM6rV-g9wttIbywxMrFNEZYhE9I81847FWDgK4R1kXxLeG37Rd00Zu2vB3ibLdIF5snSdYxJtfb2klLp93jrGRTU53KQFWDzdqO1rsR8SsVz9EO9UeF_jyZQ5FZMLo6a1tC3dUJ1ggG0Z2opfLxtlv3gkeqgFKh974VCwWggUrJjyibDv2iQhG-JtT23_MXnsS3VAVh6l7GkovG2Gjeek1SBDtnmuCLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما:
هرکی جنگ نمیخواد جمع کنه از اینجا بره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121060" target="_blank">📅 14:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121059">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15ada8325.mp4?token=LyQhtd64JMrwDUKgmsBPa_RjubGnE-Ykzt3lx6zUoJOytAfA8yqEsQN18ZoZB3G0fZbKdYQxWx1VQ1L286aQffmAZjQDnEVg9rHXIpsC14ZhrTeB3sViA5h-wkOTQuyxF1C1o74i7i9BwRwXo0HAQZLuksraRySAB4vhDZ5W7rEmulESLZ3nAlV2aIF-WVxNFYOSjpmxebvYJBeOr4tLycsOkK_waLNhqwEvURS6Pzx6AAXOOMuBXLh0KDntnzICHZNofLfLMW-u4xXziCqMpIEMWjjOBPmbLDBwNI02tv9tSZZS4Lo0r-Tf4sIJUlLF9U7e5825FHMqXZDh9klNHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15ada8325.mp4?token=LyQhtd64JMrwDUKgmsBPa_RjubGnE-Ykzt3lx6zUoJOytAfA8yqEsQN18ZoZB3G0fZbKdYQxWx1VQ1L286aQffmAZjQDnEVg9rHXIpsC14ZhrTeB3sViA5h-wkOTQuyxF1C1o74i7i9BwRwXo0HAQZLuksraRySAB4vhDZ5W7rEmulESLZ3nAlV2aIF-WVxNFYOSjpmxebvYJBeOr4tLycsOkK_waLNhqwEvURS6Pzx6AAXOOMuBXLh0KDntnzICHZNofLfLMW-u4xXziCqMpIEMWjjOBPmbLDBwNI02tv9tSZZS4Lo0r-Tf4sIJUlLF9U7e5825FHMqXZDh9klNHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اگر فکر می‌کنید این اتفاقات را فراموش می‌کنیم، سخت در اشتباهید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121059" target="_blank">📅 14:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121058">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
مهر: تو قشم صدای انفجار شنیده شده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121058" target="_blank">📅 14:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121057">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مهر: تو قشم صدای انفجار شنیده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121057" target="_blank">📅 14:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121056">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر: عبور اخیر دو نفتکش حامل گاز مایع قطری از تنگه هرمز به معنای بازگشت دریانوردی به حالت عادی نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/121056" target="_blank">📅 14:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121055">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b81e83a5f.mp4?token=tws771VKe39aU9pr1hl0decBXhgamWqvHE3IBsBosjoa7UVZzn2CY2IET6SfJKR44I_l1A-JWtclJny6wV7Tvl5HcavzlBALU57kPU_6CXjNl7nFZKVVl2YJaGPvS72Y0O34xdOmAYLqXcA5CM7ShZDGeVoRUo3qE9XuKdoKKvCG8YAuuvYM1mGf5fTpEFV7Om_zXKcfTrNTBd3H5XOeg0G8ZkJHiI5SUEJESE5sAj-_3RDpPn8u8gzv6WREk1tbfcqHTXFPlCXW9V7CRWHe1XyPdCsJvBUsA4xd2bZM0MJp25MWtW33n4lz2N78UA1Ct53_RnNiz1iVZTBg9PrCKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b81e83a5f.mp4?token=tws771VKe39aU9pr1hl0decBXhgamWqvHE3IBsBosjoa7UVZzn2CY2IET6SfJKR44I_l1A-JWtclJny6wV7Tvl5HcavzlBALU57kPU_6CXjNl7nFZKVVl2YJaGPvS72Y0O34xdOmAYLqXcA5CM7ShZDGeVoRUo3qE9XuKdoKKvCG8YAuuvYM1mGf5fTpEFV7Om_zXKcfTrNTBd3H5XOeg0G8ZkJHiI5SUEJESE5sAj-_3RDpPn8u8gzv6WREk1tbfcqHTXFPlCXW9V7CRWHe1XyPdCsJvBUsA4xd2bZM0MJp25MWtW33n4lz2N78UA1Ct53_RnNiz1iVZTBg9PrCKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل: من اینجا به طور قاطع می‌گویم: اگر حزب‌الله تسلیم نشود، ما بخش‌های بیشتری از جنوب لبان را تصرف خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/121055" target="_blank">📅 14:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121054">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGWWAwCiKUwEwT7t1CtEOC5Q0Og3HsyE8FGu37xTj_-2xT2_MjL5X0R3CvxfADiEVWcKvBuDnPvmaH2JTSWaUEsryuv7wKQF39GRrQ6z120TvdJpzjZ-6oIEEyMVUYdqsZkueelG7NyIOXZ7xo75tn143Rq3oNXVAwY9RUIT5YdCe9ZDTQm3BGGCdPr1pFBzvVL4pLpmEYDWiwxScYhQTLnycmXUpTC2Kc46LFf9J0EgLjYGGvo56H58gkk2COlTvViLnET5_DgyX_EySexC4F-E2V2R8n9W2-lFNkroXuVf-kGI9ipEqDNVp-fh8B04mPT8mKi8qaHg-6lgY2Zljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت هوای اهواز امروز ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121054" target="_blank">📅 14:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121053">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
امتحانات مدارس در البرز غیرحضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121053" target="_blank">📅 14:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121052">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17b16a4f1.mp4?token=BhAxBbux5JLEVQ6ftY5Nia_sSsORuI5jhK2U6Hi6GLlCGnuBu2i9dX28afHkfi8kmRJspIAWKCcdEyNtndJYvsXwdYOu0iNB5xlfzBce2jV_lp1RePqnaWvn33UrvvwFcHszSIy5q4iUeKUuEYPtjtEmopkXyNtYBTolwV_Ju9wvtO4dA5Kmb0PzxQfEqufq5sNo5j8mf-s4Esy-C3JaZOFDR58_g0-OSyYgjFr_0Z3-y4F9S7LzM9JjHSHYfUEATbQLaMoMcxWWNponHFkUA8pHsuL3zCOUeHnt4X1BPJS-9psfsnMBZM_pepdD9m7p2OBdcMEwzz2QEcKG7OYcwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17b16a4f1.mp4?token=BhAxBbux5JLEVQ6ftY5Nia_sSsORuI5jhK2U6Hi6GLlCGnuBu2i9dX28afHkfi8kmRJspIAWKCcdEyNtndJYvsXwdYOu0iNB5xlfzBce2jV_lp1RePqnaWvn33UrvvwFcHszSIy5q4iUeKUuEYPtjtEmopkXyNtYBTolwV_Ju9wvtO4dA5Kmb0PzxQfEqufq5sNo5j8mf-s4Esy-C3JaZOFDR58_g0-OSyYgjFr_0Z3-y4F9S7LzM9JjHSHYfUEATbQLaMoMcxWWNponHFkUA8pHsuL3zCOUeHnt4X1BPJS-9psfsnMBZM_pepdD9m7p2OBdcMEwzz2QEcKG7OYcwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی شورای شهر تهران: از فردا مترو و بی‌آرتی در تهران رایگان نیست و مهمونی بسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/121052" target="_blank">📅 13:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121051">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
امتحانات مدارس در البرز غیرحضوری شد
معاون آموزش متوسطه اداره کل  آموزش و پرورش استان البرز:
🔴
با تصمیم جدید شورای تأمین استان، امتحانات در استان البرز بار دیگر به صورت مجازی برگزار می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/121051" target="_blank">📅 13:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121050">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
فارس: تخم‌مرغ از ۵۵۰ به زیر ۴۰۰ هزار تومان سقوط کرد، اما مرغ گرم از کیلویی ۳۸۰ به ۴۵۰ هزار تومان افزایش یافته!
✅
@Aloanews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/121050" target="_blank">📅 13:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121049">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt1Av4VTaXkCMu3R2Excn6mgd6fJKKpliMuSDhH4r5ZpKi5mdty-amK-HWpHYd_IxefF1OP6pwyVzwmshenSSeEF_MpbPvMOEAZnPJimb9yRKroDMP4a2XAkehtTBc2lRPYPRH6qKRi_lsI9MqxvdsRuxOmiBElHkjmp94oc0mkKhDHVi1zeCj85LX-Ck5boFFVRq3gLxEcbuSSCT2NKIbOrrpABjkirctCT66ul7tGeu2fg0WW4tdRmOhDoNQC_aCuJK75b0kYQYk3TTyCoO_sSYnpXWGFAqU75QENzdjTC3MHyuqlBbkS9eokJGRVvo8GyQty0RLYOwJedBK2NiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس اولین روز بعداز جنگ را مثبت تمام کرد
🔴
شاخص کل بورس در پایان معاملات امروز با رشد 2500 واحدی به 3 میلیون و 716 هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121049" target="_blank">📅 13:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121048">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f98735351.mp4?token=UB-r3daWX05uHPt5VwYkHH9NxB6XJBOrgDJZ4g528la8bE6nYJGvklqpbKVYrCr27hgcwF4kvP14Qv4J3lp8nlvuji8SmKw-q0EMtKAWcaR9qmrml3ecymq3Xln26m9iT9EZqebYeZwCWxPt6TIrh6Z2-6Wpdf9P4kEkHCdA3H2hGrph9SeOr9y1k31AuiC1NBZlVsGTq5HUbN3mvQvZPGx4DvTrIkKn7W5wziFu-G00HruAWb2r-NDwHsbnDY8hyEUwZDm0aTKIjOeSoc4YsNuNbf4Y5B20DLGJgEet3B8jOmJrahGJaGGxep5aWQsaNR7Hyt8QEKX19zwKKvDIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f98735351.mp4?token=UB-r3daWX05uHPt5VwYkHH9NxB6XJBOrgDJZ4g528la8bE6nYJGvklqpbKVYrCr27hgcwF4kvP14Qv4J3lp8nlvuji8SmKw-q0EMtKAWcaR9qmrml3ecymq3Xln26m9iT9EZqebYeZwCWxPt6TIrh6Z2-6Wpdf9P4kEkHCdA3H2hGrph9SeOr9y1k31AuiC1NBZlVsGTq5HUbN3mvQvZPGx4DvTrIkKn7W5wziFu-G00HruAWb2r-NDwHsbnDY8hyEUwZDm0aTKIjOeSoc4YsNuNbf4Y5B20DLGJgEet3B8jOmJrahGJaGGxep5aWQsaNR7Hyt8QEKX19zwKKvDIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌ی ارتش اسرائیل از صبح امروز، به لبنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/121048" target="_blank">📅 13:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121047">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW3G4iZJfxqUaR2OqR3CPPiMzEqnHLVYeuE6fJdqSfyvnfZ9R4d4AOT1Ivvd_XZzXYnvcVMLg6lW1T49tKcm5e6VyiAEdJaukVDR2i_MjFD4xYgDNz4e6awYWzYs7viggj2j84f9dZZSfBhWyf9hcF1rSv6dsPZPGEZOseStFhqRN8CgAuQA3p3dO_vE9YOGV88wQp3MJ7Vjks8YEAqGSfOBp1chskkau7Sdq_j0YMeQbZ_x-QZ4otoUaAOJH7oGXnUU6kGKxcyypzFpva8LeVJtiE7Cs63UFfLaXci28og3QgGbwZQA3vrXo4WxZqOFsC2zLp6KvLJmZMeckMDaiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه واشنگتن پست به نقل از یک مقام پاکستانی: ایران می‌خواهد پیش از اعلام توافق هسته‌ای، به توافقی برای پایان دادن به جنگ دست یابد.
🔴
واشنگتن می‌خواهد توافق بر سر همه مسائل را یکجا اعلام کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/121047" target="_blank">📅 13:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121046">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سخنگوی ارتش: ارتش ایران، دوره آتش بس را به منزله دوران جنگ تلقی کرده و از این فرصت برای تقویت توان رزمی خود استفاده کرده است.
🔴
اگر دشمن حماقت کند و مجدداً در دام اسرائیل گرفتار شود و دست به تجاوزی دیگر به ایران عزیز ما بزند، با ابزارها و شیوه‌های جدید جبهه‌های جدیدی را علیه آنها خواهیم گشود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/121046" target="_blank">📅 13:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121045">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
باید ایستاده برای این مرد و سخنرانیش دست زد.
🔴
تامی رابینسون از روز اول کنار مردم ایران بوده اما امروز سنگ تموم گذاشت و درمقابل ده‌ها هزار نفر از انقلاب شیر و خورشید حمایت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/121045" target="_blank">📅 13:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121044">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
اتحادیه اروپا کشورهای حامی روسیه یا ایران را به قطع کمک‌ها تهدید کرد
🔴
طبق گزارش یوراکتیو، کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا، کشورهای در حال توسعه‌ای را که از روسیه یا ایران حمایت می‌کنند، به محرومیت از کمک‌های اتحادیه اروپا تهدید کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/121044" target="_blank">📅 13:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121043">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
صدای شنیده شده در دزفول مربوط به تست سامانه پدافند بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/121043" target="_blank">📅 13:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121042">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر دفاع پاکستان : احساس می‌کنم جنگ ایران از سر گرفته نمی‌شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/121042" target="_blank">📅 13:12 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
