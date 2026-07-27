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
<img src="https://cdn4.telesco.pe/file/ngeaSjEY-Bk6lkVQrM2DNVsS2TFr68xIjm-N_h19ntFQSn_JI8um0gSyj-Jqk81FnpG0uZ5EPEkuX63CpgE5nVjVWUBUMHLvDCNFhzmWtzX8RVVMCAUaEV4hJkbR0PODEu9axZ-Cu4XFiF2UQFVIvnsFkoOkduRpame_MM4yJZ_CuWWAMkMNsz09MhavSOab4434WFPtUzSvJ5OxleDfR55qJa8ril9AlIoblo1sGywD1hkxPH1ZifQP53m5aFmPnmhJJuBxl9bzvugJj00Lo6EKjFF3yD5CuETAqBkdNlwZDxKW_f57ZiniybA29AnTGpVFYh7ovIR3fbpkhPERFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 15:42:25</div>
<hr>

<div class="tg-post" id="msg-452928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/farsna/452928" target="_blank">📅 15:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74255f8ed.mp4?token=meP5XYp8Ixcw1Yxno7TsfJCZUBI2ugm764zB4FNyuQKMuoBIKfpvbbmvPOI0vbvM-9H6-k26USU1fY2Kc-bV8kPB0L8NJO-2Ec4-RCnltr0tZ5ImWoFM-g32jT6jKw3IZ0NTZZTo9Aegdy9hAG_l33n8dMx9Zkp_Eq0-PBYs6W3WXdXMpw2JzKE7N5QCLazM_Q7H_pGmgMf35XWqizmrFWUYacu0tAfG-bqROPN1DBalXh1gY3Y40U7u-3XEAwM_ydXqNFUDkAl3Thxiigj1Y1BV0JLwweVx9HUifHs1UoH-QVH8TFbLQ8UWfJdtyI5Js2Qd_h1d0DeeNWud5U1sFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74255f8ed.mp4?token=meP5XYp8Ixcw1Yxno7TsfJCZUBI2ugm764zB4FNyuQKMuoBIKfpvbbmvPOI0vbvM-9H6-k26USU1fY2Kc-bV8kPB0L8NJO-2Ec4-RCnltr0tZ5ImWoFM-g32jT6jKw3IZ0NTZZTo9Aegdy9hAG_l33n8dMx9Zkp_Eq0-PBYs6W3WXdXMpw2JzKE7N5QCLazM_Q7H_pGmgMf35XWqizmrFWUYacu0tAfG-bqROPN1DBalXh1gY3Y40U7u-3XEAwM_ydXqNFUDkAl3Thxiigj1Y1BV0JLwweVx9HUifHs1UoH-QVH8TFbLQ8UWfJdtyI5Js2Qd_h1d0DeeNWud5U1sFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در سمت خدا: اربعین دو بال دارد؛ محبت به امام حسین(ع) و بغض به دشمنان
🔹
در اربعین امسال، قرار است خون‌خواهی به عنوان بغض به ظلم و ظالم به اوج خود برسد.
@Farsna</div>
<div class="tg-footer">👁️ 342 · <a href="https://t.me/farsna/452927" target="_blank">📅 15:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📷
زائران اربعین، استوار در مسیر
🔹
باوجود افزایش دمای هوا در مرز شلمچه، موج حضور زائران اربعین همچنان ادامه دارد.  عکس: فرید حمودی @Farsna</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/farsna/452926" target="_blank">📅 15:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCIpknsggGHijmUQmGl9WY06yEIUV1AepOKq4xpZYkM82YR5M2ZX3oNldsiXfUkaIpMRu_d5YyX7_isJiqAwHIrPcdECAt01KXF-11-tgVcFeJbkbyrly8HQgZ2xkj_06DpcwL7lho6DhXS183Mn_x-z4jQlgJb0Hst-HGwpF8D5Y2nD68GeLHzmO5B6xwuReoTHgsQtfEipobtOPwO-0a1ldUDC8zCm5Kd0WOh_c723lAUhm30OUI0TyHmIctY6gt645MkupiBe2otpCAk5QVB-BWzhKBhUpW1UUfcn_cZ8QCjQbaZ44DUXFUXAM8vH0x5qSY8vAzmpLU8Hd5GDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام بسته ارتباطی اربعین برای شما مناسب‌تر است؟
با نزدیک شدن به اربعین، انتخاب بسته ارتباطی مناسب به یکی از دغدغه‌های زائران تبدیل شده، به‌ویژه برای کسانی که می‌خواهند در طول سفر بدون نگرانی از هزینه‌ها به اینترنت دسترسی داشته باشند یا با خانواده و همراهان خود تماس بگیرند.
مقایسه بسته‌های همراه اول و زین عراق نشان می‌دهد برای اغلب زائران ایرانی که به اینترنت، پیام‌رسان‌ها و خدمات آنلاین نیاز دارند، بسته‌های همراه اول انتخاب کاربردی‌تر و به‌صرفه‌تری است، درحالی‌که بسته‌های زین بیشتر برای تماس‌های محلی داخل عراق مناسب‌اند.
همراه اول بسته‌هایی با ترکیبی از اینترنت، مکالمه و پیامک ارائه کرده است. در میان این گزینه‌ها، بسته ۵ گیگابایت اینترنت با اعتبار ۱۴ روزه و قیمت ۸۰۰ هزار تومان، برای زائرانی که در طول سفر به اینترنت بیشتری نیاز دارند، انتخاب قابل‌توجهی است.
در مقابل، بسته‌های زین عراق تمرکز بیشتری بر مکالمه دارند. برای نمونه، بسته‌ای شامل ۱۰ دقیقه تماس بین‌الملل و ۳۰ دقیقه تماس درون‌شبکه‌ای زین، با قیمتی حدود ۶۶۵ هزار تومان عرضه شده است.
زائرانی که بیشتر از پیام‌رسان‌ها، مسیریاب‌ها و خدمات آنلاین استفاده می‌کنند، باید حجم اینترنت را در اولویت قرار دهند.</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/farsna/452925" target="_blank">📅 15:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeTsv3JEzOaFEH5gwNiRIR48x-T-HUYXxRYA1xa7xuq5h-lTCVU976A4eBVUcUiPZeupELnJ6b6gRiMe9kN_UbzEl1_MoyKcqPv0kAyvmJeVKYn59Y4yNyogzGBkiKzUJQb0YLID1KB3qqd2XfhNen2oeZEk0jD83fcCcIW5YZKMo_y_ENKrO0CN3L2ynaEpEWsPCEDjaahUbFJCkilFw_u-bDiON6FKx0Zux2j8E5tdoUP_0pHnfKKJZvYoxZulIUzLe7FEXD03HSbqkLlNEtxI2VaUgkgE1oEvDjSKNIFp5DTE22KfFU1a4XdRj5_9yEXp1gTEAPGzxw74cQJuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
خدمت رسانی شعب کشیک بانک کشاورزی در مناطق مرزی به زائران اربعین حسیني
🔻
به منظور رفاه حال زائران اربعین حسینی و سهولت دسترسی آنان به خدمات بانکی، شعب کشیک بانک کشاورزی در شهرهای مرزی غرب و جنوب غرب کشور از ساعت ۰۷:۰۰ تا ۱۹:۰۰ دایر و آماده خدمت رسانی خواهند بود.
🔻
شعب کشیک در استان های آذربایجان غربی، کردستان، کرمانشاه، ایلام و خوزستان تا ۱۵ مردادماه از ابتدای وقت اداری تا ساعت ۱۹:۰۰ به صورت مستمر آماده خدمات رسانی به زائران و مراجعین خواهند بود.
اسامی شعب کشیک بانک کشاورزی در مناطق مرزی در روزهای ۵ تا ۱۵ مرداد ماه
🔗
مشروح خبر</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/farsna/452924" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/farsna/452923" target="_blank">📅 15:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP_bqZIKg01MTa5amaXqcqr7dwQguNXSc64u7Qi3Ou9ICPSx9VuB5LXa9L6qz1CuNt431DnYkSse2G39Emsu-R9jIT41G-o6S7AbjL_V-bJG-GjPBv7iDDXY_qVjX-yu9CbV9lmVXp8Eb-M7AMxOelqRHeDEO6ZBgpZDHnX-x0MNjMRNb8x4hWKldrXFNRBDDwXVYyrpObpfbT772l3Yk3tPN2nj4eSZ9uRJBnWUsEGBIB9J6YDYIjYTQwMkEmUpziJp4-rFg9d8sOS4vVgJFd7w3JaGusALUtWNffr5vf7c6hzeoNJOR1jKGNI6EThaB9Wib9O608gzP8yptj9z7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قلعه‌نویی: بی‌وطن‌های ایران‌فروش گفته‌اند که خوب شد تیم ملی صعود نکرد وگرنه ما بیچاره می‌شدیم.  @Farsna</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/452922" target="_blank">📅 15:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9419b58485.mp4?token=nNRhWKBF5Vf1MGLFs-Ypu84-sazc7rYAVVjiFPHWCpTbKfY0WhwpEwKf4Q_ABqNXQR9mGIpXV37bUbDLUi5xBYd7kHlwIIS-_JK0quezCulFsujlN2_VVe64utvjavEOlraMstHdRFDAFV-dd6RxcJk0BtI6IBVftdt6kGBQxFAYLuVmlo8tpAU4so6Q98FacTHiFgH_YbgIcYNVgksitHq6JDrArYxDrDJvsg7ViSZNNQm97iYa2HmAKTqWRYqaRc11AnB7CeSzl8JiF9LFk5hzGVYD3dLUGpJ0_QFyeyHp62IAzk4NNkfAcot7iWrUUatOTjnIVj2uYGTcV33emQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9419b58485.mp4?token=nNRhWKBF5Vf1MGLFs-Ypu84-sazc7rYAVVjiFPHWCpTbKfY0WhwpEwKf4Q_ABqNXQR9mGIpXV37bUbDLUi5xBYd7kHlwIIS-_JK0quezCulFsujlN2_VVe64utvjavEOlraMstHdRFDAFV-dd6RxcJk0BtI6IBVftdt6kGBQxFAYLuVmlo8tpAU4so6Q98FacTHiFgH_YbgIcYNVgksitHq6JDrArYxDrDJvsg7ViSZNNQm97iYa2HmAKTqWRYqaRc11AnB7CeSzl8JiF9LFk5hzGVYD3dLUGpJ0_QFyeyHp62IAzk4NNkfAcot7iWrUUatOTjnIVj2uYGTcV33emQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرامکو همچنان در آتش می‌سوزد
🔹
تصاویر ماهواره‌ای نشان می‌دهد که تاسیسات پالایشگاه جازان آرامکو که ۹۹ درصد ذخایر نفت خام عربستان را در خود جای داده، پس‌از حملات یمن همچنان در آتش می‌سوزد؛ احتمالا این دود عظیم ناشی‌از آتش‌سوزی یک مخزن ذخیرهٔ نفت خام است. @Farsna…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/farsna/452921" target="_blank">📅 15:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرمانداری بندرلنگه: صدای انفجارهای امروز ناشی‌از خنثی‌سازی مهمات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/452920" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f433f1e1.mp4?token=GjyYdeMSeP0wXUo8W8HjnB5h4sP0D0KVpXqlIzw4Vpxx6V5omEKJHOHXbF0dzL2d0bOPEby605u7GBWtmvhpkOCPk5DXtMUk9Mik8JHRadEQDgXIoGzvw4i1fTMljay-0piiufeSi6NqPVnMAV4ozo8Gt7MSGMdIISBezV7NvAk4wmX3WLAwxnCHgAqR3LjPMdsj6FSQFhAKkmSYlWGCE5LvwOR_FcFS-WQRCD5pvm3tINeB8I6k82mLcRYG_9_lO3Tl39QdZECqzzhmTRNR3Nj8hX7UDFQ_WS_ZuLIX9Ez3Iyu9cGqFo-kydB_1KqFyD_azQ6MiHlq4riYi-XtCOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f433f1e1.mp4?token=GjyYdeMSeP0wXUo8W8HjnB5h4sP0D0KVpXqlIzw4Vpxx6V5omEKJHOHXbF0dzL2d0bOPEby605u7GBWtmvhpkOCPk5DXtMUk9Mik8JHRadEQDgXIoGzvw4i1fTMljay-0piiufeSi6NqPVnMAV4ozo8Gt7MSGMdIISBezV7NvAk4wmX3WLAwxnCHgAqR3LjPMdsj6FSQFhAKkmSYlWGCE5LvwOR_FcFS-WQRCD5pvm3tINeB8I6k82mLcRYG_9_lO3Tl39QdZECqzzhmTRNR3Nj8hX7UDFQ_WS_ZuLIX9Ez3Iyu9cGqFo-kydB_1KqFyD_azQ6MiHlq4riYi-XtCOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اندیشمند آمریکایی: هیچ راهی برای تسلیم ایران وجود ندارد؛ ما بازندهٔ این جنگیم!
🔹
مرشایمر، نظریه‌پرداز و دانشمند علوم سیاسی: هیچ مجموعه‌ای از اهداف وجود ندارد که بتوانیم آن‌ها را هدف قرار دهیم و ایرانیان را مجبور به تسلیم کنیم. این اتفاق نخواهد افتاد.
🔹
آن‌ها تا پای جان خواهند جنگید و توانایی زیادی برای این کار دارند. ما در جنگی در حال باخت هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/452919" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GchwRmJ0Khloo-_ZAjLH06hX-ktYOX0quL0DBVV-n9vMH9XdpKY5AJjBhf76SVqYxNYZUNd7GxqAAtUdGztrI_YTPYaryIJ-5dmDb7j98VBFME6IdAH9xLtUxioNIUkl2fNvijnupbfsll-fgMntKQqDp1cC0Mp2DMJCHKWysMyLVEHX0UE51_QicHLglvjGrZn3X7Fu4YlhfeY3IAx53eaUFijeGbhKK3flLS47Y7d4pGYGLiunzPYCnO4yYo7juSKu1TvTJOyDRI0T1CNYx1KIhUD-gVSvzo57ilDMk8bnBqSf9aDWBYsLy5RivrYg4mCTwnODH4APGzP4EUxi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ استاندار ایلام: تردد زائران اربعین از مرز مهران از ۶۶۰ هزار نفر گذشت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/452918" target="_blank">📅 14:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d783b974e.mp4?token=KyDsM_BAlxJrG148B6N4yOZyk4mFLKf46F5ZUFV2HIAOF77QDj8uqZx4AVClLRE-Ss66w9bL71DmT9SquP3fUlVFsA61pabihQWWYa9MqYQVWe5lvB5zKwsVOWYdQF12KpkAWe84-PQYUDgq0m3Zoi-zfrIQN6cBPlxfv9HdSHbNZ5CUJA_oFxzd0JmALfqXHMD6b58eJlG7x38ydkJYBoXF9Kw-b7FbrOadjlez0x3tRmC0RN6A3q2GKDUgHv9KSGO_hNUluSzu-al76kKxMotUTBwoxkIjr3dFzuRGtNmIqwl1FGn-LL7KwVJpdIfOFpSU8AS7W9oZN_D0mgwH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d783b974e.mp4?token=KyDsM_BAlxJrG148B6N4yOZyk4mFLKf46F5ZUFV2HIAOF77QDj8uqZx4AVClLRE-Ss66w9bL71DmT9SquP3fUlVFsA61pabihQWWYa9MqYQVWe5lvB5zKwsVOWYdQF12KpkAWe84-PQYUDgq0m3Zoi-zfrIQN6cBPlxfv9HdSHbNZ5CUJA_oFxzd0JmALfqXHMD6b58eJlG7x38ydkJYBoXF9Kw-b7FbrOadjlez0x3tRmC0RN6A3q2GKDUgHv9KSGO_hNUluSzu-al76kKxMotUTBwoxkIjr3dFzuRGtNmIqwl1FGn-LL7KwVJpdIfOFpSU8AS7W9oZN_D0mgwH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاهدۀ پلنگ ایرانی در منطقۀ «شکارممنوع» لار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/452917" target="_blank">📅 14:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fc7819224.mp4?token=WwPIeTTbFS15M7_9DeDk4c9rluGOZnbdfMXjoJmq-JwsFOjxoBQgQ5VsiwqomEkvDnugqCGmfhep_Rx38ud4WINhC6RH0ip18jVuTnd0SqQ8Q0p5M9U1fmkjo1EWvkD-xsrN_-hO9odALaXD1lJWnQ62Q1E0uvjjIAsLu3R6eaE7utrwFmxG1_M1m2n0CMEe70j6HVIkeDp4WF6jTH5pV0FamhMyMDVi8-MeSvT3GRkm_DguLxCWNbKlLlTqJK4tEWK9PNPYcn1QHXhtKs7NKBGRVqLLPsNgHPVyDnxvdtVNLty8TSL4w0x9sT58qPQSgfm1-alBAmbhSpweEYSzrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fc7819224.mp4?token=WwPIeTTbFS15M7_9DeDk4c9rluGOZnbdfMXjoJmq-JwsFOjxoBQgQ5VsiwqomEkvDnugqCGmfhep_Rx38ud4WINhC6RH0ip18jVuTnd0SqQ8Q0p5M9U1fmkjo1EWvkD-xsrN_-hO9odALaXD1lJWnQ62Q1E0uvjjIAsLu3R6eaE7utrwFmxG1_M1m2n0CMEe70j6HVIkeDp4WF6jTH5pV0FamhMyMDVi8-MeSvT3GRkm_DguLxCWNbKlLlTqJK4tEWK9PNPYcn1QHXhtKs7NKBGRVqLLPsNgHPVyDnxvdtVNLty8TSL4w0x9sT58qPQSgfm1-alBAmbhSpweEYSzrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نگرانی زلنسکی از باز شدن جبهۀ جدید جنگ با ایران
🔹
رئیس‌جمهور اوکراین، در توجیه حملۀ پهپادی به یک شناور ایرانی در دریای خزر که به شهادت یک ملوان منجر شد ادعا کرد ایران قبل‌تر با ارسال تسلیحات به روسیه، علیه کشورش اقدام کرده است.
🔸
البته این درحالی است که ایران…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/452916" target="_blank">📅 14:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpvKYA34e2k542nyRC5SvpOmP0vWOHjhM8obBRN6x40pO_jLr5zybFw9KTNQ2PaC5jq8YhM5lCpOXsEsmOBKe8yMRU0jiutXVGDR8EK7nII-w-bOqRO46ESVCa2KrhlPjmGhwl7nwth1zBv7kpyB-wNos85eBE4UcVV4KPtzhgFt0alQV8lMe9FpCY1nMMj4lUSkO9pmL5T7hmdtcoRyVQk2fC3MlyWENYzF6lRjElVuo-zrajLLI70ya9xPt8_KK_mmRpQ-Ez7MOSFKzyUxem297h42WwIg5QkAKsWwAetZQFqi5A9ky_3KHWWmPfi2qBQc-CFwTPebG2bQ5NbBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: نبرد هرمز، نبرد برای آیندهٔ ایران است
🔹
‏نظرسنجی یک مجموعه رسمی و معتبر: «ایران باید مدیریت و کنترل خود بر تنگهٔ هرمز را حفظ کند حتی اگر این موضوع منجر به جنگ مجدد با آمریکا شود»
"موافق ۷۸ درصد"
این نظر ملت ایران است
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/452915" target="_blank">📅 14:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452912">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZA3naY0KbPpHM4Vi9Ef-iTCU5oS_F6Ydcm0qQJ4IY_GkZiHfn7Hjjg9u_cXOsDy8kFHZAbTbm_nYTaPpaYln7Z8m_PUZyZScCJYZRlGfnOufWclxa7tSXxdxdx37s8FjWGboGC7Pm2XrKNWg5WDCAsKli_3FzQ0IA1Ls88Ld-EYiPzuJnP01iarQ-l2AdumjuM2NvgBR9lcYZNM8lFCYeqYUZjAqFjB03h3fXW5y3grKxPFu8rvbBrt6GcU6_tihVKurr08dy_rqNC1m4BQVhIiRJaeEKFecg4OVZ5IE-eT_ANxrS28v2UAQSgbCwsb6-y1Yp60T8XfXedJWZiepkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnyXhrGAUTfP7xz8OoH-BbThjAjaUJwZPd81M7gSgnl6zq-zz7zI_C5xKakme0czFmTH8iwksdMMXeNdWEgCQNoAjYtpoKjeGsZe4pZU8nPSOcy-hl7HxhUHwMcvnixxSrEILRegRs6TntFoR_06Ev5sMTs-5iIkIzHaBuyqM6xj8LBYmUUPSnE2USha4f_d2Vj8gv5SUbG9FUh16BhuTYAlMBfFakERBb04OxrtcRanNWU1fTNNOTsDHgt62hlKCGikkKnVsnf-kwu-dHc_MKLdAp1zxlCkbXCYW1dIN3odY-v0ZUy-RuWWhxVnizrAdPiS8ssxKbMBwMLUcHAwgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EItK5lFV8DsMaQq7SUAhKFzyZ7VNLKMUaJ_9RTObi8H65aBVe9qSnfycKlhkZvp3Uby1aE7whoLpETUnqQTVdyadg2MHcoDpz766frWrwxr4Go_yI3_pT1P1Xy-M9ZyISvrLF2X9fw4MElLUrRnVDEThYi_HA8on1IA4G_cj1D-lhbHwud4ziRU318A-ix2aDGpJY8btZyPeZVw61sGADa27E3seyTHDYlE7IgwmSbJ5lP8Zzb6E6JZ6nYwbxk_jUoiUwfocvDeHEuNfg5APIqfEZyy8hfQfvru2lrtTuUhlVD9jx7Gd4bwfU6VOeWTmTZ9hiQMFYXqFodynV4mTEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
آتش‌سوزی در هتل پارسیان تهران
🔹
سخنگوی آتش‌نشانی تهران: آتش‌سوزی در یک مجتمع اقامتی در هتل پارسیان در تقاطع بزرگراه چمران و خیابان ولیعصر باعث شده شعله‌ها به‌طور کامل این بخش را فرا بگیرد.
🔹
عملیات امداد و نجات همزمان با اطفای حریق در حال انجام است. آتش‌نشانان…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/452912" target="_blank">📅 14:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452911">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1668f513a8.mp4?token=UCsQVb9_ChE1OOBU3U7lONLMF-NdEU2OhEb5xl2uJ9U3UczTLnLWrDT8V_FtungAz_CQvr6gEOmswByivwN_G-tHFGs98K0uGZwpYw0EY_L4123lxSY0K_ZouoD8Sr1bcdsaTtiO4EwtY9YXYyKT3nZ-cOamacHxoZcRc8htiLd92pMmLFWYXE22lRywqjifIrwXJKgdXR3oOg3qL-Kwbh_kQiUnDCFrEIELREWyDIOdLVFGGnIvcD_nx_cpVuI-8ZuRrYgHbl1Lw-sa_M-2akE-KNTkYYfjiuSJ6Z_rk973U4Zbywp7o-wFsl6SBSL1GmRNkTJGb0Bim5jFkEx0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1668f513a8.mp4?token=UCsQVb9_ChE1OOBU3U7lONLMF-NdEU2OhEb5xl2uJ9U3UczTLnLWrDT8V_FtungAz_CQvr6gEOmswByivwN_G-tHFGs98K0uGZwpYw0EY_L4123lxSY0K_ZouoD8Sr1bcdsaTtiO4EwtY9YXYyKT3nZ-cOamacHxoZcRc8htiLd92pMmLFWYXE22lRywqjifIrwXJKgdXR3oOg3qL-Kwbh_kQiUnDCFrEIELREWyDIOdLVFGGnIvcD_nx_cpVuI-8ZuRrYgHbl1Lw-sa_M-2akE-KNTkYYfjiuSJ6Z_rk973U4Zbywp7o-wFsl6SBSL1GmRNkTJGb0Bim5jFkEx0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب زنگ‌زدۀ استعمارگران در جزیرۀ هرمز
🔹
در ساحل شمالی تنگۀ هرمز قلعه‌ای فرو ریخته و توپ‌هایی زنگ زده وجود دارد که پرتغالی‌ها در قرن ۱۶ میلادی آمده بودند بمانند اما حالا فقط قاب استعمارگران است که در ذهن تاریخ جا خشک کرده.
@Farsna</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/452911" target="_blank">📅 14:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452910">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRfENQ9aHouSct6L1V7TKt7bGeIODsVgIKN9k79wR6G-W41yueWQ1mxct6YqhSEs8TXvB8Ihbsy5WbL4HAdeo0sjNv9KTgNwfXV_i2S-00yrKelpj08BqCajG1QHh3bqODDlZXybXUTjiorfcVTGEbLHessQE4KavBUjh6s8HiXjWoXhoyU4Gfepi8iSZ1IDg4S7OkH8sKUDQ6U7l9FWUhv-miTVq5qT_FcssotGh4hvV9BAcKyTgeAme9lxwkyX3801OLwQ61lMWZfR6l6HOf3QvV9MbwcOe_Gv6CcvpkDDOFN92Pu2qQx7ZuZseWWhhHCo-UUVFC598KC48SW9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان رویداد آموزشی اربعین‌نگار
🔹
مکان: دانشکده رسانه فارس، خیابان انقلاب اسلامی، زیر پل کالج، کوچه سعیدی، مجازی: اسکای‌روم
🗓
تاریخ برگزاری: پنجشنبه ۸ مرداد ساعت: ۱۳ تا ۱۹
📰
سرفصل‌های کارگاهی: عکاسی خبری، روایت‌نویسی و ویدیوی موبایلی
⤴️
مزایا و فرصت‌ها: اعطای گواهی معتبر پایان دوره، انتشار آثار برتر شرکت‌کنندگان و اهدای جوایز ویژه به برگزیدگان
🙍‍♂️
ثبت‌نام و نذر فرهنگی:
https://tavana.news/auth/arbaeen-register
🙍‍♂️
عضویت در کانال اربعین‌نگار ۱۴۰۵ در پیام‌رسان ایتا
eitaa.com/arbaennegar1405
@Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/452910" target="_blank">📅 14:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452909">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFSL-QcUI0g4lyxQkb9-vdMbtDKlfNKZOWkgH4t6vqDFvRQKRsNSzMzlsoGDoBnd0CXc9HgTtygOYsOigkhhcXP9sZuXdmk30ebDjGTmMiF2HMCSHLu6DC4mvLlThPJhVmnckvTOPxUtzHiwxA22TjlRzxphuhdejAunvnV0o69iSEYW07szScOh74QEVPmwhuaGrvFvTaVART1ldZzTmhctXwcKYkPdtcdwrXftV_1CCyt-kh4KU6z0oeOj6PY-i21EsjW5Pp9P4cE5_4ZPY-JFwIIgWtKJIqvPp7d4yBY9g8ZbXN3oytco9QMjqDYBYqP5vB2tMQ9WzqwlFIEs3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاوره درمانی ۴۰۳۰ با تماس رایگان از عراق برای زوار اربعین
🔹️
سامانه ۴۰۳۰ به صورت رایگان و ۲۴ ساعته آماده مشاوره در زمینه‌ سلامت، تغذیه، لیست داروهای ممنوعه و معرفی نزدیک‌ترین موکب درمانی به زوار است.
🔹
زائران می توانند با شماره گیری 4030 بدون نیاز به پیش شماره از عراق به صورت رایگان، تلفنی تماس بگیرند و یا با شماره گیری  *4030# (ستاره چهل‌سی مربع) اطلاعات را به صورت پیامکی دریافت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/452909" target="_blank">📅 14:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452908">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=SCJfgpqU1Obadf0FeV0LG05CFcolY2dftmtFYmcONR2fjJMVa-tCXoo2ecbQoHnelNbXzfb8BhWgitlw6gSLcMxfvX1OknL7e8iSfyomraY501Axs5POkyanTzi_cJ4IHeddhWkWlJ-m_Zp175rZ1t7fEEnNWGIiRcWx2GCyTYXQsUgMNBFE70TjF03A4jVTeqh8xsi3tnPEe-2dPCQ02S2zb_qdYFs9Y0dPHMoipA2GKakLBHfG-Ry1FDg4itepqf36L-leLhdLiDAqTgasbRueq2DHcs1ARsY_DSHJqBy8zEcmpSlspufs4Wd5daQ0v-D3KljV9EqgiZp0kbHfbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=SCJfgpqU1Obadf0FeV0LG05CFcolY2dftmtFYmcONR2fjJMVa-tCXoo2ecbQoHnelNbXzfb8BhWgitlw6gSLcMxfvX1OknL7e8iSfyomraY501Axs5POkyanTzi_cJ4IHeddhWkWlJ-m_Zp175rZ1t7fEEnNWGIiRcWx2GCyTYXQsUgMNBFE70TjF03A4jVTeqh8xsi3tnPEe-2dPCQ02S2zb_qdYFs9Y0dPHMoipA2GKakLBHfG-Ry1FDg4itepqf36L-leLhdLiDAqTgasbRueq2DHcs1ARsY_DSHJqBy8zEcmpSlspufs4Wd5daQ0v-D3KljV9EqgiZp0kbHfbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
✨
✨
حسابتو طلایی کن
✨
✨
✨
‌
🟡
۶۶۶۶ سکه طلا برای ۳۳۳۳ نفر
و میلیاردها ریال جوایز نقدی دیگر ...
‌
✨
جشنواره بزرگ قرعه‌کشی حساب‌های قرض‌الحسنه بانک سپه
✨
‌
#بانک_سپه
#نخستین_بانک_ایرانی
‌
🌐
https://omidbank.ir
‌
🌐
https://banksepah.ir
‌
📲
@banksepahofficial</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/452908" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452907">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/452907" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452906">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تعویق سفر نتانیاهو به آمریکا
🔹
«تایمز آو اسرائیل» گزارش داد پرواز هواپیمای نتانیاهو به واشنگتن، بدون ذکر علت تأخیر به تعویق افتاد. @Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/452906" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb14c46a0.mp4?token=qmX1zRTMMpEVfH_i_sjUlsh-ZqCKKu3GFSKAXTE3f3E2d2KKf1NbXZztbjyUJQVPHmahqpcDJ14zx7yEfZKBgiwQ12JY_cy-_7utpEeDbIyNIcwO5S702jADAbO0-FlBaSLYCSYIu5CrSFIJJVr3R1Rxmuvhj4HXRTuJDOWSdMEV5KOklgs1yov5z7npQyZxhHzDeY2YlriAxgBIgEOKfcAZ3EtBfi4eoAjBZQqBpzJd3UuBhQtifmID7AvD7UKsb46mfJ4eohQP7KyuoSPRJCtm06uf4got9h45Y0mzqPldiyc_ILeqRavp-VNtoNGU5SfIiURt1HpBAKs0G8z_4aZL-pGatHU5jkLm471_7OYUUuRPCPZ4AKFNJ8h-V8tZTYkHzGAvCo3pPO1AdciB0NKAgmPF38AHlKd-iLuwaHhkXHuxdGO0oGle34ZmHvhI_6cgVQFsWvu3erAn2Lw8SbFHQRakW2ozdAn05GlAlTpLIId7YRs-phFwuOjSNng2A8HENQy5NnO_AOTU0I6FhQ_f-ZAIYDNMg8pcmyFLYVsUbJ3oG7rpkqLLRGxF3AqqNFbD9w9OBW71ehv7wUXgMLA2LzebmmowvkGv8RtuejnNefpBlmd0aBXrEHxSlwhxu6e42JJCEzC_LDZB-DSZ2CcsrRDMJUzPBI7faerbwlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb14c46a0.mp4?token=qmX1zRTMMpEVfH_i_sjUlsh-ZqCKKu3GFSKAXTE3f3E2d2KKf1NbXZztbjyUJQVPHmahqpcDJ14zx7yEfZKBgiwQ12JY_cy-_7utpEeDbIyNIcwO5S702jADAbO0-FlBaSLYCSYIu5CrSFIJJVr3R1Rxmuvhj4HXRTuJDOWSdMEV5KOklgs1yov5z7npQyZxhHzDeY2YlriAxgBIgEOKfcAZ3EtBfi4eoAjBZQqBpzJd3UuBhQtifmID7AvD7UKsb46mfJ4eohQP7KyuoSPRJCtm06uf4got9h45Y0mzqPldiyc_ILeqRavp-VNtoNGU5SfIiURt1HpBAKs0G8z_4aZL-pGatHU5jkLm471_7OYUUuRPCPZ4AKFNJ8h-V8tZTYkHzGAvCo3pPO1AdciB0NKAgmPF38AHlKd-iLuwaHhkXHuxdGO0oGle34ZmHvhI_6cgVQFsWvu3erAn2Lw8SbFHQRakW2ozdAn05GlAlTpLIId7YRs-phFwuOjSNng2A8HENQy5NnO_AOTU0I6FhQ_f-ZAIYDNMg8pcmyFLYVsUbJ3oG7rpkqLLRGxF3AqqNFbD9w9OBW71ehv7wUXgMLA2LzebmmowvkGv8RtuejnNefpBlmd0aBXrEHxSlwhxu6e42JJCEzC_LDZB-DSZ2CcsrRDMJUzPBI7faerbwlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر: کتک‌ها را می‌خورم اما باج نمی‌دهم
🎙
رئیس فدراسیون کشتی:
🔹
در این چند سال کسی اگر به من بی‌احترامی کرده باشد امکان ندارد او را به کمیته انضباطی برده باشم اما هر کسی تو کار کشتی گذاشته باشد جلوی او می‌ایستم فرقی نمی‌کند معاون وزیر باشد یا کمیته ملی المپیک.
🔹
با شخص خودم کاری ندارم اما برخی‌ها باج می‌خواهند حالا مربی باشد یا هر کسی. من کتک‌ها را می‌خورم اما باج نمی‌دهم.
🔗
صحبت‌های دبیر را
در فارس بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/452904" target="_blank">📅 14:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452903">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
ارتش اردن مدعی شد که ۲ پهپاد را در آسمان این کشور ساقط کرده و خساراتی در پی نداشته است.  @Farsna</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/452903" target="_blank">📅 14:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452902">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea5c211d7.mp4?token=en1KU1s8klcLVHbDVMzXaPQxj0AKKCtj-et3p1C8YCKosGbETnveVnIMZU6RmtYYAw_7EFlt3oDkFR8w9uOOrvf3VLMs-Gaj6e2MTXL2PkxseXllJGBfNjDyLygGl_NPytZWlz1OwkSrhypzbkrThN9xWAzmZdiiNYtztCmHNR6p_E9Y-SC_hDCOswsatziefQAU83cxnbdLtS4kfGI1Rv9iq1OwyCPC6znAlyeJBskI77oMB2iOUMwgLR2IJQzj47dHQ9xJP4GWPPjgoCqw0cS8hJfByY3CStxJeNWhMolObbls_sgS9id6dmjhIQgvGmp_mZyLU5kDkOEyFHrczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea5c211d7.mp4?token=en1KU1s8klcLVHbDVMzXaPQxj0AKKCtj-et3p1C8YCKosGbETnveVnIMZU6RmtYYAw_7EFlt3oDkFR8w9uOOrvf3VLMs-Gaj6e2MTXL2PkxseXllJGBfNjDyLygGl_NPytZWlz1OwkSrhypzbkrThN9xWAzmZdiiNYtztCmHNR6p_E9Y-SC_hDCOswsatziefQAU83cxnbdLtS4kfGI1Rv9iq1OwyCPC6znAlyeJBskI77oMB2iOUMwgLR2IJQzj47dHQ9xJP4GWPPjgoCqw0cS8hJfByY3CStxJeNWhMolObbls_sgS9id6dmjhIQgvGmp_mZyLU5kDkOEyFHrczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از حملات پهپادی به مقر تروریست‌های تجزیه‌طلب در شمال اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/452902" target="_blank">📅 14:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452901">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGhmhhrNb1J37HHVKNU6xNJpT9Wodsm8Iy3g0du6Z-8kIhrde4klFDIqA4kvZxBI5OJfPQT-t4ZgnYGlmt1Cot0rJjw9Mh66SuVnImWkBLhzvUkvsU4uKYKFpNmxCBaHvV6LIEPFKzizhyJHNcnYaPNSXIvhJTRf12SA4siHSkN6V6kljINhYmLeEq7CDqczonfuWta_b_aHkdwoL0bGwg3nFXpisGkep5xLg1HullLnqv19rKa21XfSmXnK8IoA5bCw3uSwAWCzMKXqnVwDZ2D92axWN0EFPONGOPPlsXZCxrKrcw5nB16y9L2SW0YTAYO-OGOw5daKz2c8VfWjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خشم قلعه‌نویی در جام جهانی پیچید
🔹
شرایط نابرابری که آمریکا میزبان جام جهانی برای ایران بوجود آورده باعث اعتراض مجدد امیر قلعه‌نویی در نشست خبری امروز قبل از بازی بلژیک شد که نشریه تلگراف انگلیس در گزارشی به اعتراض سرمربی ایران به سکوت ۴۷ مربی دیگر جام جهانی…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/452901" target="_blank">📅 14:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452900">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf17741d4.mp4?token=KaVE0eBWwpRzgqhx3X6pdI4WjiGrVceQQqXxQDuW_bbSEB-ssPpJWFQFKAqdmC1WCrQbc__SP43yMeDaM6a_6GKKCIrlCgfl8-KVvty7NI464iv-1wGws_3Jse8FBbOcwnWYzX3FRlF1uwaUdndy_xZ35LLCCaCE0eBaRneH1L-k43-c5tRy9ejE-T1n4hfyZxuZF9XdkYt1IAtem6gmzBFoOPCJE2qSbqLnyVYAx-TaA58wq5oT-se4MiTX8omxjM34JVLkjIOvD9uwpWyBFyeY-zkcop9N2-2P4ysM8M6FnNfDsTfhqYORz967k_WepS7yE5Yy9nNTAC8UzsPPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf17741d4.mp4?token=KaVE0eBWwpRzgqhx3X6pdI4WjiGrVceQQqXxQDuW_bbSEB-ssPpJWFQFKAqdmC1WCrQbc__SP43yMeDaM6a_6GKKCIrlCgfl8-KVvty7NI464iv-1wGws_3Jse8FBbOcwnWYzX3FRlF1uwaUdndy_xZ35LLCCaCE0eBaRneH1L-k43-c5tRy9ejE-T1n4hfyZxuZF9XdkYt1IAtem6gmzBFoOPCJE2qSbqLnyVYAx-TaA58wq5oT-se4MiTX8omxjM34JVLkjIOvD9uwpWyBFyeY-zkcop9N2-2P4ysM8M6FnNfDsTfhqYORz967k_WepS7yE5Yy9nNTAC8UzsPPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خارگ برای شما زیادی گرم است
🔹
انیمیشن لگویی خطاب به تروریست‌های آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/452900" target="_blank">📅 13:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452899">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57c07bae2.mp4?token=An29oQV3GgGlwj4XyIRgsZ0sGUyKeWu_wS1lbE2nwlCjSLaG3J7tXUcKFWdVW5jiXYF9cV2pPOUbO604uSJ5UhKqxblmqLLpr98xTq8gB3zzp1xcSyJEEMs9ERvRzMV1ROZvK4-yF0sKeboTYTJ9oUNpnNr6WteUidGvJqPv2Vt5V1aMRKeVlT8xTvjufV0WLtGgGyd33alY86CKwL2zlt_qfu3k8_Z4thX-eEgqed9zQj_lo4NMKd5xfFH6o2w88hPOhHWLNzYkn6OmLkYsgQ3YtKHp8Cxbe3daEIenPWRH5RJ6v_C0daXPeSms5j_Rxf4P5q1T_UbYKflWXogDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57c07bae2.mp4?token=An29oQV3GgGlwj4XyIRgsZ0sGUyKeWu_wS1lbE2nwlCjSLaG3J7tXUcKFWdVW5jiXYF9cV2pPOUbO604uSJ5UhKqxblmqLLpr98xTq8gB3zzp1xcSyJEEMs9ERvRzMV1ROZvK4-yF0sKeboTYTJ9oUNpnNr6WteUidGvJqPv2Vt5V1aMRKeVlT8xTvjufV0WLtGgGyd33alY86CKwL2zlt_qfu3k8_Z4thX-eEgqed9zQj_lo4NMKd5xfFH6o2w88hPOhHWLNzYkn6OmLkYsgQ3YtKHp8Cxbe3daEIenPWRH5RJ6v_C0daXPeSms5j_Rxf4P5q1T_UbYKflWXogDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در مورد شکایت از زیرمجموعه‌مان باید حساس‌تر و مسئولانه رفتار کنیم
🔹
اگر مردم نسبت به یک فرد در دستگاه قضا بی‌اعتماد بشوند، آثار خیلی بدی دارد.
🔹
اگر کسی از کارگزاران سطوح مختلف قوه‌قضائیه خلافی کرد، نباید به او رحم بکنیم. @Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/452899" target="_blank">📅 13:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452898">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e51a5e67.mp4?token=GAV2dghyPaifv_G4rfrPSJh_wX8xdLtoLt3eegZKS_CC4iTML0wpRJB5ZgBb0f7rxqTc07qfaD7PjCRoMbvgL-fjy2Mttj2mjR4JJJ9h8pjg-4hU-v6INMu9jt8dVxLDl1RR-aXnDkM-QucO8EfOLLCr_wghOpgxIixZDtYvHdovluLUPcn4dbOauYt9rc6KXf7AdWXZ2JW0irC8kH2f1H9ILRommCaIZ3SlXma9w9eWwKojd9OZMmquFjYGOUTY_7dkdHq3MwBDH1wrmlzKZJsPP3TTRJXxe6ho4Riz5USF6ps8N8-neefKqb2wvcdNZ39xjRyUGc8fb4xBZnJ33A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e51a5e67.mp4?token=GAV2dghyPaifv_G4rfrPSJh_wX8xdLtoLt3eegZKS_CC4iTML0wpRJB5ZgBb0f7rxqTc07qfaD7PjCRoMbvgL-fjy2Mttj2mjR4JJJ9h8pjg-4hU-v6INMu9jt8dVxLDl1RR-aXnDkM-QucO8EfOLLCr_wghOpgxIixZDtYvHdovluLUPcn4dbOauYt9rc6KXf7AdWXZ2JW0irC8kH2f1H9ILRommCaIZ3SlXma9w9eWwKojd9OZMmquFjYGOUTY_7dkdHq3MwBDH1wrmlzKZJsPP3TTRJXxe6ho4Riz5USF6ps8N8-neefKqb2wvcdNZ39xjRyUGc8fb4xBZnJ33A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در هتل پارسیان تهران
🔹
سخنگوی آتش‌نشانی تهران: آتش‌سوزی در یک مجتمع اقامتی در هتل پارسیان در تقاطع بزرگراه چمران و خیابان ولیعصر باعث شده شعله‌ها به‌طور کامل این بخش را فرا بگیرد.
🔹
عملیات امداد و نجات همزمان با اطفای حریق در حال انجام است. آتش‌نشانان در قالب چند گروه عملیاتی وارد ساختمان شده‌اند و در حال کمک به افراد محبوس هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/452898" target="_blank">📅 13:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452897">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae297a55a3.mp4?token=mb_TJUb1qd3xgFGdoYO1bSFPPCAnyiBNsPjakUJg39hBY4s4UfHelNPHAF_IoQTcJgLNut5KvElj24mVdtw_NOLLScnE3bnH0_8PPcpSpZT0weVrFA_o-tpDFUcIiUe0yvBBDb_etHhgpdzOZBkPqwShS0yhcf4lvoUFEH5fPcBMAn8_wdqT6wOcb0fp1Lsex-2nAnIwWhmV7lpBHDNTvUzHc8NT0-RLCe_BfYyTYHpgHLsl9CdZLnrmmoUciFl7RYR7Yg1XB2ws4UA4LfvY0qkV1cyPXGOb4vtU_2mN242LvadiBRG7ZOlIPH2R9efg3mygN0QE12sCa3t0OQ8G9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae297a55a3.mp4?token=mb_TJUb1qd3xgFGdoYO1bSFPPCAnyiBNsPjakUJg39hBY4s4UfHelNPHAF_IoQTcJgLNut5KvElj24mVdtw_NOLLScnE3bnH0_8PPcpSpZT0weVrFA_o-tpDFUcIiUe0yvBBDb_etHhgpdzOZBkPqwShS0yhcf4lvoUFEH5fPcBMAn8_wdqT6wOcb0fp1Lsex-2nAnIwWhmV7lpBHDNTvUzHc8NT0-RLCe_BfYyTYHpgHLsl9CdZLnrmmoUciFl7RYR7Yg1XB2ws4UA4LfvY0qkV1cyPXGOb4vtU_2mN242LvadiBRG7ZOlIPH2R9efg3mygN0QE12sCa3t0OQ8G9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای: اگر کسی در قوه‌قضائیه دچار فساد بشود، در برخورد با او رحم نخواهیم داشت
🔹
اعتقاد راسخ ما این است که هر مسئولی باید در قبال زیرمجموعهٔ خود نهایت صیانت را داشته باشد. باید نظارت‌ها و هشدار‌ها و تذکرات به‌قدری وسیع و عمیق و سازمان‌یافته باشد که اساساً…</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/452897" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452896">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG3rc37O3b_Cqvz1O2Ik7mEdK4zMYtettmPyf-7IFzab3JJXAagMwEIbBrqAEiUJD45tH_KhfWj7l4gSRWlPD7nOGDkTpanIzSMvyqlUFh592HSFxwK8XhJGDhSzJjl-XyXhiHr2MHIvyenn37U3Qs0s-9Er4u230tUQ8iOa5tlX7WlUaOSVzvlfihHDmgPlRaatRLcUhn0pWuvrq__tZ2we774ZLea0djmJmWl-boB0oxin6PMy84lGOCm_v6HPzNqEWpB9R7v8VQTkOOd4qvNyMRFLN63ZS6pQcLbStyqxoKGjLGM5ED1i3JDvx-h6EPmvbLGIA4CWJij8jZhUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نتانیاهو در طول حضورش در آمریکا بازداشت نخواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/452896" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452895">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3f8067ef8.mp4?token=UOy3qgL4wQiNhR4nZ53L2na0PpSSxVVmekFVajMWzKvCJcRfNqNS-h9hTjQEQY2y1a1bW15zdcLraO49UdrMEOA6Z2pDtSA_4T2ubgFB0TfMLHnxQMIwgID2sL8KQc6igMwjUvw-E8XILOKaHzhbVNfCaYRBmrqhkTGBxgPWiyRAWCCWwhUWM5rk_7WPsnj_S9gZssC7kpAnfvn8N78lhA1CzezLrmnYuUGChq1jduJtLSP6NsQrnZgfrUcXjpFYXogShZy_jBeXIIPQe-F4bp2s2CjQ_FnChVBwf6FnZcPD5OP-1uoOS3AZDmd9D7XIdBapxaIwyAr30OuZugKc2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3f8067ef8.mp4?token=UOy3qgL4wQiNhR4nZ53L2na0PpSSxVVmekFVajMWzKvCJcRfNqNS-h9hTjQEQY2y1a1bW15zdcLraO49UdrMEOA6Z2pDtSA_4T2ubgFB0TfMLHnxQMIwgID2sL8KQc6igMwjUvw-E8XILOKaHzhbVNfCaYRBmrqhkTGBxgPWiyRAWCCWwhUWM5rk_7WPsnj_S9gZssC7kpAnfvn8N78lhA1CzezLrmnYuUGChq1jduJtLSP6NsQrnZgfrUcXjpFYXogShZy_jBeXIIPQe-F4bp2s2CjQ_FnChVBwf6FnZcPD5OP-1uoOS3AZDmd9D7XIdBapxaIwyAr30OuZugKc2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فتاح، اولین مهمان اتاق گفت‌وگوی جدید خبرگزاری فارس
🔹
رئیس ستاد اجرایی فرمان امام (ره) امروز در خبرگزاری فارس حضور یافت و علاوه‌بر گفت‌وگو در جمع مدیران خبرگزاری، در استودیو و اتاق گفت‌وگوی جدید فارس خاطراتی از رهبر انقلاب گفت که به‌زودی منتشر می‌شود.  @Farsna…</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/452895" target="_blank">📅 13:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452894">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
ارتش اسرائیل مدعی انهدام ۲ پهپاد در مرز اردن شد. گزارشی درباره منشأ این پهپادها منتشر نشده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/452894" target="_blank">📅 13:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452893">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmOwDE4IPlJqj3eRtuF5QgUIWGheEowoTgG2frlMHlBBXKgrOMjXubDzLhUnygrRllO0CxYyngQl9R4udEmv_TLh1g_1HCvYm06-b9LXOQidrciR_IEeooI2WJGP6t6FM2ndrohxdFb4rVhawNEnE23c5Dcg61YP0JPZftdUMK3A-hFz9ozDIhCTH9TQ9DhP-DhdcP4aj7Kf8cCynNYkXvTw38cpvV-tvIG_N9KOcxFFI39Nd21IOAGE3SnGv4WDIyKYcVAHcBzdRMy_mNZCCSSOeH8K_xr27iC4d178XCjDhW9DQg6G3RNOeFvY2c2hp65B9vNIJNHtMwJ_94Aa4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ارتقای ظرفیت بانک صادرات ایران در اعطای تسهیلات/ وصول ۸۴ همت از معوقات بانکی در سال ۱۴۰۴
🔹
بانک صادرات ایران با هدف افزایش توانمندی در اعطای تسهیلات به مشتریان، فرآیند وصول مطالبات را با شتاب بیشتری پی گرفت و در سال ۱۴۰۴ بیش از ۸۴ همت از پرونده‌های معوق را تعیین تکلیف کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/452893" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452892">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BElSk3yfA_yXljL630nAKfbRn3kzF9zAOPoVYb6owf5E0bFsOGsYYrEPN4802ekZOlRJ7Ds_wx0XGQA84KiJyw9aDhBcG8gSaMgtt1w063KoURnoYbuvmtG6PAh8gpHxX3W63xy5tokGsGta2sTM8ZvlXxW3W-G7z4AZj_3Z6X67dbjtFDkUI760gDWwuVQAP8xzmHoc0vyU0jTfQHu4aKM0I_C2JNfv5iKYmMGqbrga9Hx17V3g8R02dgf6Cca4R5xLIefYx5gzpWdoHfExFXYiUnZed27YTCxO0F9iGHMnoRXYBdBAYane2sb6XeewFsUa8fF5Jp8_KPoXiuY-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
۱۰ پروژه مس ایران در میان ۵۱ پروژه توسعه‌ای مس جهان
🔻
شرکت ملی صنایع مس ایران با در اختیار داشتن ۱۰ پروژه از مجموع ۵۱ پروژه توسعه‌ای در حال احداث صنعت مس جهان، در صدر شرکت‌های جهان از نظر تعداد پروژه‌های توسعه‌ای قرار دارد؛ جایگاهی که با قرار گرفتن تمامی پروژه‌های توسعه‌ای ایران در سطح اطمینان «Committed»، کشور را در رتبه نخست جهان از نظر ظرفیت پروژه‌های قطعی توسعه مس قرار داده است.
🔹
دکتر غلامرضا ملاطاهری، معاون طرح و برنامه‌ریزی راهبردی شرکت ملی صنایع مس ایران، در جریان مجمع عمومی فوق‌العاده این شرکت با تشریح جایگاه صنعت مس ایران در عرصه جهانی گفت: براساس آخرین ارزیابی‌ها، مجموع پروژه‌های توسعه‌ای صنعت مس جهان در سال ۲۰۲۶ شامل ۵۱ پروژه در حال احداث با ظرفیت مجموع ۷میلیون تن مس محتوی است که ۱۰ پروژه از این مجموعه متعلق به شرکت ملی صنایع مس ایران است.
◀️
ادامه خبر در مس‌پرس:
https://mespress.ir/x6S7
#در_مدار_آینده
#مس_ایران
#فملی
@mespress_ir</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/452892" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452891">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/452891" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452890">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0151cde69f.mp4?token=Glybqjs-vakqvuxzHfIdD_067k2jE-Kuyb1mHiUaggbOO_uvNuuuxEqNBzumvLC3FLxf1dmTTlJ9FUshg71ap2bNJD0hIhxuLcmhx5TOWGJrsJnQEkqNImt3vAbx-wi67zt8uFDfNBBH-ry0olbO06g0gvI4eV8ioI2zyZmDohyVvlj_jP4gT4idxrIJ-qcX1ZCahnuSVgfQSQXw69GiseDimD2VdyEoSIK0S3cJKDssm5f3zc3kNQ60k7lklYPEELdge_cyVaPl08Rid0Cuwzd_qgjSjb-p3k4UDDujv2ByqgRxyRBttjJHzUXkl6EJ4EU1_BmCORPJXXTIOFcsew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0151cde69f.mp4?token=Glybqjs-vakqvuxzHfIdD_067k2jE-Kuyb1mHiUaggbOO_uvNuuuxEqNBzumvLC3FLxf1dmTTlJ9FUshg71ap2bNJD0hIhxuLcmhx5TOWGJrsJnQEkqNImt3vAbx-wi67zt8uFDfNBBH-ry0olbO06g0gvI4eV8ioI2zyZmDohyVvlj_jP4gT4idxrIJ-qcX1ZCahnuSVgfQSQXw69GiseDimD2VdyEoSIK0S3cJKDssm5f3zc3kNQ60k7lklYPEELdge_cyVaPl08Rid0Cuwzd_qgjSjb-p3k4UDDujv2ByqgRxyRBttjJHzUXkl6EJ4EU1_BmCORPJXXTIOFcsew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ دستگیری باند سرقت موتورسیکلت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/452890" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452889">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Blpqo4POVBa_E-npVU6HgBLd9fSmAqeCe48obXrlJA_WoDqj92JnVfYY2ZnGiksnaWLM1rXnXFz0mhkXla2c3DR6Yk1oH68tGR07KXg1b4K7yBNI_gxbqogsjjKq2yO6jS9O3MrhgPoKbq35SFtt5Y5hamk5tvEE6j4ljAUfCCEfd0SEjO5aL-aGSNbsUQNGkU1vUEH8BQakPDK5kk4i1qET6n81xaae8gINC1XcBeLXBMA1I9CIqtsLUWaOxcnY50iqEkrRM4I7Jo4rOnAAKjd5mLFTzo0AGtgQT-RKQlSYpB1BfRh8AgsEWd2MKNhYAH7NQ58rQVQFhRXyjxBEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۵۰ هزار واحدی به ۵ میلیون و ۵۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/452889" target="_blank">📅 12:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452888">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e85XE_g8ml58aeSkF_McIokf4vUzc_jrIIFNUlH-y3nztD_bRSM-NHGfZkdbmgXx_KXxSbFF47DBsItLdLMSmM25X4N4RBPT5dlwAw7vb12KWs8WAkGrpx2QbMJKVwHuqkRRY6mXTYZrjV1qm9VfKRerrBxzywlVAtVsmbq7v8ELjrpbcLx3tqSoGVsAMAhF_AuU_9RCbxk6hDJm_0JV73ItpaUvtyD-mjtstEgEGv6VVQNLcn8qlebSc-bT-I0AMZyzrvNWraNgfHWpyZ6rLpC4LbiBuLysatpfuvF6y3dEfgeqseUGpmYqw1ErXRA-W1nNJUVPKE7Pg-qTeQp7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خروج اولین زائران حسینی از مرز سومار به عراق  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/452888" target="_blank">📅 12:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452887">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در خوزستان
🔹
فرمانداری امیدیهٔ خوزستان: درپی انهدام مهمات عمل‌نکرده در شهرستان، احتمال شنیدن صدای انفجار در امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/452887" target="_blank">📅 12:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452885">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d96a362192.mp4?token=BuCKqNJnARzG0lJKWB9JtkmjcOt71FAMRg_o9_nZe--kkcJSk448rZZXQgR7cwcCuRRefR060AUGiA6-eiwLhKeQWTsDOW85J1abrFUsRHPsPT9KKoZhJ7ZOV_vN7hv9NX60jk3WHrVqzpHEM3S0wcFP94bxY2s4PwUKWbzhbnHr4bGcipv4-UMzM2Py-MKU7u_GHAXasrXaRbkxpemrpjI5M1iYzqLBKBAZBfquE5wxNYEHQYWaToAqiV_qyeg9gSZLkIjfdlPvwO-U91mlwftmGzdrJ00qoArtEy4_D029xnmY-mScTqwFmE3uD2HYbNFgEJnO9Gm5-L_oqKI9Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d96a362192.mp4?token=BuCKqNJnARzG0lJKWB9JtkmjcOt71FAMRg_o9_nZe--kkcJSk448rZZXQgR7cwcCuRRefR060AUGiA6-eiwLhKeQWTsDOW85J1abrFUsRHPsPT9KKoZhJ7ZOV_vN7hv9NX60jk3WHrVqzpHEM3S0wcFP94bxY2s4PwUKWbzhbnHr4bGcipv4-UMzM2Py-MKU7u_GHAXasrXaRbkxpemrpjI5M1iYzqLBKBAZBfquE5wxNYEHQYWaToAqiV_qyeg9gSZLkIjfdlPvwO-U91mlwftmGzdrJ00qoArtEy4_D029xnmY-mScTqwFmE3uD2HYbNFgEJnO9Gm5-L_oqKI9Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیاده‌روی عشاق اباعبدالله(ع) در مناطق جنوبی عراق
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/452885" target="_blank">📅 12:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452880">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxyrq5p2-sNsfJVhwj0DqN9LtqyJ9zQKLQZGOiMvjky7IiABF8_RaDxASGOUZrtzJWsVhQsIxCcdZVFj8acHJwEf1axHeOlBTmj2vy07VPp7p1zRcfHOyNsH5ZAy4u4M0OgtIH4mTm53TUQ5X6l_xNYISKvUlQMKE3CNCodz1Yo110i2QezfHIYN9XJIjj2LYGv6cidm2LGnlh-jQi4npAPuYCJlCL0WPiCd8pKyZNMU-PUjv2Dp0MDLfT1gCcm9mT0aE2LtbDCvn7JJ_KB0RM6sR1eQoId6a3AwX52GIPn7xD2lCk2H-R8pZ4GxlnhAK7POTuPgT915wczDJHay5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای: اگر کسی در قوه‌قضائیه دچار فساد بشود، در برخورد با او رحم نخواهیم داشت
🔹
اعتقاد راسخ ما این است که هر مسئولی باید در قبال زیرمجموعهٔ خود نهایت صیانت را داشته باشد. باید نظارت‌ها و هشدار‌ها و تذکرات به‌قدری وسیع و عمیق و سازمان‌یافته باشد که اساساً امکان حرکت به‌سمت فساد برای یک مسئول و نیروی یک نهاد حکومتی و دولتی وجود نداشته باشد.
🔹
چنانچه باوجود تمام این نظارت‌ها و هشدارها، فردی در درون قوه قضائیه یا بیرون از آن مرتکب فساد شد، فی‌المثل رشوه‌ای دریافت کرد یا آلوده به سایر مفاسد شد، مطمئن باشد که هیچگونه ارفاق و اغماضی در قبال او وجود نخواهد داشت.
🔹
ترحم به چنین فردی، در درجهٔ اول، ظلم به خود او و دستگاه متبوع او و در درجهٔ بعدی، ظلم به مردم است و ما هرگز چنین نمی‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/452880" target="_blank">📅 11:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452879">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e21ed4d2f.mp4?token=QS2WSyDGDwP3T5OV8UwxK2fVpMVTM2RJrLYKPCiuSABZDbxUjfC-b5wfmqX5IGEReSb1R22jDkyA1DF-aLdpqdD58QmXrz-5L_MDkA-Jj3NvJIueI1NCAxe5-xgmQUKXYsfcbZl7zV2kKlq3xU-JuIMpRVeLdcEbjNsbu1qkkOqocBNvbb5aNqaiLqsQJzrSJUj070Mf0iKRnea8gsLmupneP21dTUDtYX9gkZQKfO08ezsNc6d82bHKzJfr0BuJGpKIHJAvv3Uy7cG-FyzempqPyd41MLKg7_MzLKjLgDJq2C7hLXpOvtQxMUpWUjVcKhAvxGhsth7u-CbHpHVtRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e21ed4d2f.mp4?token=QS2WSyDGDwP3T5OV8UwxK2fVpMVTM2RJrLYKPCiuSABZDbxUjfC-b5wfmqX5IGEReSb1R22jDkyA1DF-aLdpqdD58QmXrz-5L_MDkA-Jj3NvJIueI1NCAxe5-xgmQUKXYsfcbZl7zV2kKlq3xU-JuIMpRVeLdcEbjNsbu1qkkOqocBNvbb5aNqaiLqsQJzrSJUj070Mf0iKRnea8gsLmupneP21dTUDtYX9gkZQKfO08ezsNc6d82bHKzJfr0BuJGpKIHJAvv3Uy7cG-FyzempqPyd41MLKg7_MzLKjLgDJq2C7hLXpOvtQxMUpWUjVcKhAvxGhsth7u-CbHpHVtRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا در ۲۰ روز کل تفاهم‌نامه را نقض کرد؛ ما از اصول امنیت ملی‌مان کوتاه نخواهیم آمد.  @Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/452879" target="_blank">📅 11:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452878">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d6db134c.mp4?token=Kj_CMVfT-3zv2CpInQG11HGUrOgFvDLZ3WQlpb3UelMggDpDOvgU7e3j1FnVtE6DorOYGm17Hkbyoq0XEWVhismoUfzg1uERx_md0fn_Db6vNvmJqjWqxu2YFjXLkQA6QPXgtRZu_Z-ljaP69bmgDdyDsLGGCmbPgq5_5Y6EKUhw60qrlHb-DEUV4-9Ngkba6DPnJLs_qQ6UJcwljWOOLc7_KcYkk2ZJWeEdwyVfmBbAaR5B9zBbU5fZAatIaGRnzWRZgacJOLH2Ji8akAUaM76Hoxzv36fBGtiIAu0AcvtlkyENOKwrFUK2HM6ifMuV3PqpxOqz7VCfRKMqWZUtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d6db134c.mp4?token=Kj_CMVfT-3zv2CpInQG11HGUrOgFvDLZ3WQlpb3UelMggDpDOvgU7e3j1FnVtE6DorOYGm17Hkbyoq0XEWVhismoUfzg1uERx_md0fn_Db6vNvmJqjWqxu2YFjXLkQA6QPXgtRZu_Z-ljaP69bmgDdyDsLGGCmbPgq5_5Y6EKUhw60qrlHb-DEUV4-9Ngkba6DPnJLs_qQ6UJcwljWOOLc7_KcYkk2ZJWeEdwyVfmBbAaR5B9zBbU5fZAatIaGRnzWRZgacJOLH2Ji8akAUaM76Hoxzv36fBGtiIAu0AcvtlkyENOKwrFUK2HM6ifMuV3PqpxOqz7VCfRKMqWZUtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: جمعه و شنبه چند دور مذاکره بین ایران و عمان برای مدیریت تنگهٔ هرمز برگزار شد که مذاکرات خوبی بود؛ وضعیت تردد در تنگهٔ هرمز هیچ تغییری نکرده است.  @Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/452878" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452877">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b543b1687.mp4?token=H7OLdT4VUvSAg7vCXrfqMqFor-R8bSgsFuEiGRFiWJV3lWl3nVnukh3plxT7mU6lHzPtzMZ_b_7GaJMWX1502F6yfPyjZqgigsP3yuoaj3N7Powl3x0oBNRRT2246mDuA-ASTjna3frvjRp9DHu1MrnFRAxWZK8F5xOE-RZWc5iUziazx0OajQV6pGXX0a4pbWehb-nfNtJPWA1V94qG_lYKL1wOS14imlnyD4bzbK5Nq6f_7_LDXxVK3ahFldO1elYr4Xd8pG2OQ2U7Uaq8nrlsIdRpZfG7GNIb3wuMydfuRYvVuDZeZesLTTbebKxw_H_yTjB4E-8KZYlvW7OoVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b543b1687.mp4?token=H7OLdT4VUvSAg7vCXrfqMqFor-R8bSgsFuEiGRFiWJV3lWl3nVnukh3plxT7mU6lHzPtzMZ_b_7GaJMWX1502F6yfPyjZqgigsP3yuoaj3N7Powl3x0oBNRRT2246mDuA-ASTjna3frvjRp9DHu1MrnFRAxWZK8F5xOE-RZWc5iUziazx0OajQV6pGXX0a4pbWehb-nfNtJPWA1V94qG_lYKL1wOS14imlnyD4bzbK5Nq6f_7_LDXxVK3ahFldO1elYr4Xd8pG2OQ2U7Uaq8nrlsIdRpZfG7GNIb3wuMydfuRYvVuDZeZesLTTbebKxw_H_yTjB4E-8KZYlvW7OoVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: فرانسه با پوشش سفارتخانه و به‌بهانهٔ ارتباط با جامعهٔ مدنی در امور داخلی ما دخالت کرده و باید عذرخواهی کند
🔹
دیروز هم سفیر فرانسه به وزارت خارجه احضار شد و صراحتاً اعلام کردیم که این کشور باید از چنین مداخلاتی در امور ایران با عنوان‌های…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/452877" target="_blank">📅 11:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452876">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
ارتش اسرائیل مدعی انهدام ۲ پهپاد در مرز اردن شد. گزارشی درباره منشأ این پهپادها منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/452876" target="_blank">📅 11:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452875">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0f6ac7d6.mp4?token=EWAo79GT6DGHSK898mQs-u2KVFwynQ7dyr5hOXcuob6rOp9SpNvu-XtaR4FQM4wdFaO5C6EC1G29cyGyYlOCQn2BmRt7VrvVgEsb0pi8FSSUJmnJNz_A-DAknDjzvFtNhFlFoQyCz-lhZMqOBuP-JXEJjymVMx0Kbz3zC-cwr6FvwTxdfyq73aZMRUzx_q4gLX324IM4JkZU_ZA-yq9tN9Sv_V07kPnXBcm53e9IbT-ERylsNhiA_1MnunjruyeMBDsQ8nqT18OQFtFx5jGFKpDQywNmCFWWvgACzO9ZZ975E0LqR1CEBTj84NVuR1xuy2Pi1kcBCfT4a7JEJ7GxUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0f6ac7d6.mp4?token=EWAo79GT6DGHSK898mQs-u2KVFwynQ7dyr5hOXcuob6rOp9SpNvu-XtaR4FQM4wdFaO5C6EC1G29cyGyYlOCQn2BmRt7VrvVgEsb0pi8FSSUJmnJNz_A-DAknDjzvFtNhFlFoQyCz-lhZMqOBuP-JXEJjymVMx0Kbz3zC-cwr6FvwTxdfyq73aZMRUzx_q4gLX324IM4JkZU_ZA-yq9tN9Sv_V07kPnXBcm53e9IbT-ERylsNhiA_1MnunjruyeMBDsQ8nqT18OQFtFx5jGFKpDQywNmCFWWvgACzO9ZZ975E0LqR1CEBTj84NVuR1xuy2Pi1kcBCfT4a7JEJ7GxUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: بزرگترهای زلنسکی مراقب باشند که پیامدهای اقداماتش دامن‌گیرشان نشود
🔹
رژیم اوکراین از ۴ سال پیش کشورش را در حد ابزار دعوای ژئوپولیتیک بین قدرت‌ها پایین آورد و به‌جای نجات کشورش از جنگی که بر شرق اروپا تحمیل کرده، مدام دیگران را شماتت کرده…</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/452875" target="_blank">📅 11:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452874">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b0f07414.mp4?token=HSUyG79PYUQNyLfxJOQXISu8u1UEmYpVtG3IPHzUymrV5gnnsfOwnqF5oeQ22UzzGO_moQvfNEKEuxHbD8XS3MUh2ujPQQ_YzNuh3JuJESMnwFGU0tPrOAyg31LwjQy7GZi5FnsatkDllvwXbDCS7YT1N9qW8YFuBmd204iy--FkiqxpD2UuIksQ0Nd215QQ38-A5BrymmpOVxQpzyK3FgoNIHeoN00JvYG4cmKrsmjHupmNl2EOwOY4p6EF1bmuJrxD6DD926M6MmPAOlrU7RmpjPg9RT1RFO-0SXDv61fw9TT0sVfBvdYWpdpLtfHYuCi0DZ87zMkpQqmrVLxdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b0f07414.mp4?token=HSUyG79PYUQNyLfxJOQXISu8u1UEmYpVtG3IPHzUymrV5gnnsfOwnqF5oeQ22UzzGO_moQvfNEKEuxHbD8XS3MUh2ujPQQ_YzNuh3JuJESMnwFGU0tPrOAyg31LwjQy7GZi5FnsatkDllvwXbDCS7YT1N9qW8YFuBmd204iy--FkiqxpD2UuIksQ0Nd215QQ38-A5BrymmpOVxQpzyK3FgoNIHeoN00JvYG4cmKrsmjHupmNl2EOwOY4p6EF1bmuJrxD6DD926M6MmPAOlrU7RmpjPg9RT1RFO-0SXDv61fw9TT0sVfBvdYWpdpLtfHYuCi0DZ87zMkpQqmrVLxdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ کارخانه‌های اسرائیل در نزدیک غزه
🔹
آتش‌سوزی مهیبی صبح امروز منطقهٔ صنعتی شهرک صهیونیستی سدیروت در شمال غزه را فراگرفت و با سرایت شعله‌ها به چندین کارخانه مجاور، خسارات سنگینی به تاسیسات تولیدی این منطقه وارد کرد.
🔹
برخی منابع محلی احتمال می‌دهند که این حریق بر اثر اصابت ترکش‌های موشکی از نوار غزه رخ داده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/452874" target="_blank">📅 11:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRaThNNDMoDrbts0ME7KekQrCWJ7j8wVgefNSO6YSVqmWTRyDgk_ZemGoH7Lfb7ZBNL3BKAPEsE4J69dssJDJsdZALZ8MiT4CfPqxxp-lC1Fit6uLKiNjO8MNy1F9Qpdq82AP5ld1pIZRyu-RkCxzB6lGrx1vW1nZmQMtIcHdivtyyyE9YuV--sVmcPvNbMJ3MWJ-rkGyREFP_VyPt6be1gT5mbM4kUzBsdTfxY7UWL8K6ty8sGrAQM7Pj9hE08hff4iuVMhLHMuiFMmaOCmOz9XTHDwVIm9VlruGpwl7PSeq5TRyz6BfAiOpRpuBV-4XJniYERZ88ornSnxBrdIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجمع هلدینگ خلیج فارس لغو شد
🔹
مجمع عادی هلدینگ خلیج فارس که بنا بود امروز هیئت‌مدیرهٔ جدید را معرفی کند، به‌دلیل آنچه عدم اعلام حضور نمایندگان سهام عدالت عنوان شد، از نصاب افتاد و لغو شد.
🔸
این درحالی‌ست که نمایندگان سهام عدالت ساعتی قبل در مجمع فوق‌العادهٔ هلدینگ برای افزایش سرمایه حاضر شده و رای داده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/452873" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452872">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f262d61d8.mp4?token=OSaDtDBkSfn1-edeofTQZrbT8T-XshuzgdiDVWnhtsTZCQa-QKgusj8LGG4OSJvwyKv31KATtnA0w8JQTG3UkcPVbfbEq8Y08rRKVTFF4H_R8rvgp3D3QEi3-VePFx63qjnvI3MLDhxf3-bfC6eZxIeymF0mdWWvbQm2NFRCghYpgVpbOWoHcoLfJ8LdsSVjkJcw3EYsHKUEeV6NfC-tArMCDZd5DudEppBEussahpZTiUD6dfJ0dLsr-nAXFamtsGQfih-gx8F5kNBUFjiTRJTIajfJ7nffbdDGCJEkg7JaILof_76W4eKedslg1enwbpI-K8fwb8VvIrx-8aLwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f262d61d8.mp4?token=OSaDtDBkSfn1-edeofTQZrbT8T-XshuzgdiDVWnhtsTZCQa-QKgusj8LGG4OSJvwyKv31KATtnA0w8JQTG3UkcPVbfbEq8Y08rRKVTFF4H_R8rvgp3D3QEi3-VePFx63qjnvI3MLDhxf3-bfC6eZxIeymF0mdWWvbQm2NFRCghYpgVpbOWoHcoLfJ8LdsSVjkJcw3EYsHKUEeV6NfC-tArMCDZd5DudEppBEussahpZTiUD6dfJ0dLsr-nAXFamtsGQfih-gx8F5kNBUFjiTRJTIajfJ7nffbdDGCJEkg7JaILof_76W4eKedslg1enwbpI-K8fwb8VvIrx-8aLwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا می‌خواست در ۳ روز ایران را تسلیم کند اما حالا بعداز ۵ ماه در باتلاق خودساخته گیر کرده
🔹
تصمیم‌گیری دربارهٔ منافع ملی کشور معادله‌ای چندمجهولی است که در یک روند مشخص با مشارکت همهٔ دستگاه‌های تصمیم‌گیر انجام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/452872" target="_blank">📅 11:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452871">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op1kY1Fo5fJL_lvYxconhmaDL_HoiNLBwWiAvlYtEhbdJINJIbdMocMloNqDm201ckKzRF5LkCx_SRALSlgYjYPccWxTVDW16WE1m7Upf5eF8D1OycDgA2VEKjdMsj7TmM0aoKIpR9peFxhCbX35N8zs8v83h-garpOcGsD3aVwp6oKuFloHABZ2o3FAxGHHpsGMsicOle9ZlRSanJdx9NGN06hgwzYviKMXaAhZS13iAbRB3HelJZp6V4HpWQ8bpqe67lMtiYzZtXDBoCcSgy1ITcUfm8mkv_3uyEF8cg6LSw7KLuWtnKxFSyoFZVNC9vIoqEM1m5rUlNmJ5GiTLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ مسیر ویژه برای زیارت مرقد رهبر شهید ایجاد شد
🔹
با تغییرات جدید و گشوده‌شدن رواق دارالذکر به روی زائران ۴ مسیر ویژه زیارت مرقد رهبر شهید در حرم رضوی ایجاد شد.
🔹
در مسیر نخست، زائران آقا از صحن آزادی وارد رواق دارالسرور شده و پس از عبور به روضۀ منوره مشرف می‌شوند و در ادامه از مسیر دارالعزه به رواق دارالذکر هدایت خواهند شد.
🔹
مسیر دوم نیز آقایان از طریق مسجد گوهرشاد و شبستان گرم، به رواق دارالعزه و سپس رواق دارالذکر هدایت می‌شوند.
🔹
برای بانوان هم زائران از صحن بعثت وارد رواق دارالعباده شده و سپس از طریق رواق دارالزهد به رواق دارالذکر مشرف می‌شوند.
🔹
مسیر دوم بانوان نیز از طریق مسجد گوهرشاد، شبستان گرم و سپس رواق دارالزهد، به رواق دارالذکر ختم می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/452871" target="_blank">📅 11:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=czy7XaZwxDIv-6CrgV_2pw4DWg5DK9bWCzyuADwGcgqqHyPao4aM3OW19DUsWL5-Rnwe0JlHBTTylaenkUJCvYoHVN27hlz38oSqaxQu_xIeTEj9HR9k3Q2k7qs4-NAFjQP3-Xu7gVZkDwgIC1IF3uMdnXYzs05VRqJfB6eAvk8b9Te1sai36_JZIRoCFM1xPwjpWNxM_VuKYo0Ycg0Tm_i6o70zwzjajYd-KfKjFh7afWSR4e0EwOH9HrhU4uZ1lRjGLOXVx75MxM8WfRappyRUu42W9JLmWYtNxCVMSWDg4e7YriVfB5W0IbLjaFv-8nK0QZEkHDmjXgNicFH_2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=czy7XaZwxDIv-6CrgV_2pw4DWg5DK9bWCzyuADwGcgqqHyPao4aM3OW19DUsWL5-Rnwe0JlHBTTylaenkUJCvYoHVN27hlz38oSqaxQu_xIeTEj9HR9k3Q2k7qs4-NAFjQP3-Xu7gVZkDwgIC1IF3uMdnXYzs05VRqJfB6eAvk8b9Te1sai36_JZIRoCFM1xPwjpWNxM_VuKYo0Ycg0Tm_i6o70zwzjajYd-KfKjFh7afWSR4e0EwOH9HrhU4uZ1lRjGLOXVx75MxM8WfRappyRUu42W9JLmWYtNxCVMSWDg4e7YriVfB5W0IbLjaFv-8nK0QZEkHDmjXgNicFH_2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه خطاب به اتحادیهٔ اروپا: شما که هرازچندگاهی به بهانهٔ حقوق بشر بیانیه‌ای علیه ایران صادر می‌کنید! آیا کودکان میناب ایرانی نبودند؟!  @Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/452870" target="_blank">📅 11:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452869">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da97f47adf.mp4?token=EH_USHbJQUsyLp1zXwZWQe9_awZIbZmkDtVvHZ_bSuu1N-UCpSs6g_OFaBP9yC0ejQJfs0re8CFm0h1s_ySKr7pB5VKlEDdqMGRvSFO5IC3MCCft-coghmPumHQLxBH0zDwXqWEssZeCZiojTmJut0KV7g6XlXy5xJ7VSVisuogJ6Ie0Y1mAjhta7ldUQSv552vGhtkRpxNb2sGrqut1zl8scFeSKl-Fpgxx5ZXVM9UDLK973YZAiJgzZU78gwOhTC2RIJCKONy9_8ozq74uFzLEUQYJapOGS-F3o3R1zB56loR7R8osyQ_FLfKMoOqOz_Ze8aJC8TK5kJJkeu0rGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da97f47adf.mp4?token=EH_USHbJQUsyLp1zXwZWQe9_awZIbZmkDtVvHZ_bSuu1N-UCpSs6g_OFaBP9yC0ejQJfs0re8CFm0h1s_ySKr7pB5VKlEDdqMGRvSFO5IC3MCCft-coghmPumHQLxBH0zDwXqWEssZeCZiojTmJut0KV7g6XlXy5xJ7VSVisuogJ6Ie0Y1mAjhta7ldUQSv552vGhtkRpxNb2sGrqut1zl8scFeSKl-Fpgxx5ZXVM9UDLK973YZAiJgzZU78gwOhTC2RIJCKONy9_8ozq74uFzLEUQYJapOGS-F3o3R1zB56loR7R8osyQ_FLfKMoOqOz_Ze8aJC8TK5kJJkeu0rGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه خطاب به اتحادیهٔ اروپا: شما که هرازچندگاهی به بهانهٔ حقوق بشر بیانیه‌ای علیه ایران صادر می‌کنید! آیا کودکان میناب ایرانی نبودند؟!
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/452869" target="_blank">📅 10:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کشف جسد یک نظامی زن در مرکز فلسطین اشغالی
🔹
پلیس تحقیقات نظامی رژیم صهیونیستی از کشف جسد یک نظامی زن در پایگاهی در مرکز فلسطین اشغالی خبر داد؛ به گفتهٔ این نهاد، تحقیقات در این باره آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/452868" target="_blank">📅 10:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452867">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40df3041a.mp4?token=J_U13S9JmeMvT0ojMEsQPEa3i2UjC1UAyXwRr7I6W8GJMnOr_hOTRWcPZmD-Q1VcgmQGfxzyLgkli64GSJivfXhmBmzWUtfrApmQooFPTmsvsQr8u5EPXjWRlYKpVVnZSEl6ECGq1g8v3sQDCeA6seepRhjTGezFb7h-wCcfYTgxi5fMrP2-WUA4qqx7hqJMxpIC5aCkuqUo2PGvCYMPa-LF_hje9YILNs3ebwFLIMDngOVVIPhUJwR9yDwGNU07I52ujfHDg7xjOfN4_t46pJ0dx4UvhDzAO1YJzuUr4Gbm6XlanXoWITjXxtTOYWvmH5aQTd6xnD7aFB3nk0TfCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40df3041a.mp4?token=J_U13S9JmeMvT0ojMEsQPEa3i2UjC1UAyXwRr7I6W8GJMnOr_hOTRWcPZmD-Q1VcgmQGfxzyLgkli64GSJivfXhmBmzWUtfrApmQooFPTmsvsQr8u5EPXjWRlYKpVVnZSEl6ECGq1g8v3sQDCeA6seepRhjTGezFb7h-wCcfYTgxi5fMrP2-WUA4qqx7hqJMxpIC5aCkuqUo2PGvCYMPa-LF_hje9YILNs3ebwFLIMDngOVVIPhUJwR9yDwGNU07I52ujfHDg7xjOfN4_t46pJ0dx4UvhDzAO1YJzuUr4Gbm6XlanXoWITjXxtTOYWvmH5aQTd6xnD7aFB3nk0TfCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدم‌زنان به‌سوی نینوا
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/452867" target="_blank">📅 10:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452866">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ابلاغ نسخهٔ جدید دستورالعمل واگذاری اموال مازاد بانک‌ها به شبکهٔ بانکی
🔹
براساس اصلاحات جدید بانک مرکزی، علاوه بر مزایده، روش‌هایی مانند استفاده از سازوکارهای بازار سرمایه، واگذاری به شرکت مدیریت دارایی‌های شبکهٔ بانکی، توکنایزکردن دارایی‌ها و در برخی موارد مذاکره و معاوضه نیز برای واگذاری اموال مازاد مجاز شده است.
🔹
همچنین امکان فروش نسیهٔ دفعی در کنار فروش نقدی و اقساطی پیش‌بینی شده و بانک‌ها موظف شده‌اند دستورالعمل جدید را به تمامی واحدهای مرتبط ابلاغ و بر اجرای دقیق آن نظارت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452866" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452865">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72e331961.mp4?token=SeFnXVEgkq2d4QRdJveT1cH4zfKCMHF-r3nLgxfvIj989Wsv46tKGQ8gKF4FCget7HC3j9dq_6Kd3AlaBvzyZtl27kgrjUrzcqAsGAwXzmw0TL_lMwzY--hHzeBU2Up8AYbWO2ISQeH1XofPp5qCQsUbnHdV5yxY8PoB5OyxZ1Txc5jerulNvXg5k20OHlnxno_LpZlgGPD4IcmHaqxT3JKTuFxzt-q6opk4xf2Cv_7bKTCPxSOHQiHwH4UiqwlPY3LU1xFJw6QdkXNotXVtkfVU_hPl7_maQMVpg9n8HtNQMJa56vRxml9w5ea59Jk9HmY46dJ6-bgh7_BjfOdExw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72e331961.mp4?token=SeFnXVEgkq2d4QRdJveT1cH4zfKCMHF-r3nLgxfvIj989Wsv46tKGQ8gKF4FCget7HC3j9dq_6Kd3AlaBvzyZtl27kgrjUrzcqAsGAwXzmw0TL_lMwzY--hHzeBU2Up8AYbWO2ISQeH1XofPp5qCQsUbnHdV5yxY8PoB5OyxZ1Txc5jerulNvXg5k20OHlnxno_LpZlgGPD4IcmHaqxT3JKTuFxzt-q6opk4xf2Cv_7bKTCPxSOHQiHwH4UiqwlPY3LU1xFJw6QdkXNotXVtkfVU_hPl7_maQMVpg9n8HtNQMJa56vRxml9w5ea59Jk9HmY46dJ6-bgh7_BjfOdExw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ زنبورها یک مسابقهٔ فوتبال را متوقف کرد!
🔹
حملهٔ ناگهانی دسته‌ای از زنبورها، فینال فوتبال زیر ۲۰ سال برزیل را برای دقایقی متوقف کرد و بازیکنان و داوران برای فرار از نیش حشرات روی زمین دراز کشیدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452865" target="_blank">📅 10:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452864">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سپاه: عملیات مرصاد درس بزرگی به خائنین داد که هوس هرگونه تجاوز را از سر بیرون کنند
🔹
سپاه پاسداران در بیانیه‌ای به مناسبت سالروز عملیات مرصاد: در پنجم مرداد سال ۱۳۶۷، ملت ایران با تارومار کردن منافقین فریب‌خورده، درس بزرگی به خائنین به ملت و میهن اسلامی داد…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452864" target="_blank">📅 10:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452863">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انهدام ۲ مرحله‌ای مهمات عمل‌نکرده در پاکدشت
🔹
سپاه استان تهران: انهدام مهمات عمل‌نکرده در پاکدشت امروز در ۲ مرحله از ساعت ۹ تا ۱۱ و ۱۴ تا ۱۷ انجام می‌‍شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452863" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452862">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-Vvh9KmwWcecI697_GvkdWojVtIAk4s1Y5ZiQ5F38JjSHcat7G6ZW8z1R0sWiIBgOcJ2hBy8ouPpuo_nn08T6YVZ6KMEDjz8zTl3ZUe6SldeeFG1NgwDrbwrB0yOrujnjcPUsTweMPfYOFsOysYGPYb9EVo_6qLgQvagIAFpRRv1i5MebBj5xJqj64A4Z2MQf__cuKOzcIIiBfvXxvM0janooON0bETCh_caDqhriKahE_Nt6uojSG66BS_ZKTB-1IVMi5wew147IFeJ_96HM19DJZP2Q0jTUu9968FCjLDcTUFjcB26_KYX9RcoxsjeU7hM6xpvAXOqIkBz9kTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن ۳ نفتکش سعودی را هدف قرار داد
🔹
المیادین: نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
🔹
تعداد کشتی‌های عربستانی که از دوشنبه گذشته تا امروز برگشت داده شده‌اند به ۱۶ کشتی رسیده است.
🔹
این منبع همچنین خبر داده که  از زمان آغاز محاصره…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/452862" target="_blank">📅 09:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452860">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xt0MUbpMjaiJJtf6nZOwMBfpxunNDoBuRT-LQ6q_7vznQ7TDyJkppzEmgFpT0JUkp5QMK18JFF-d5MqSUMem_GgnJ-I7dMKEn3iUrHNxuoYnwUvZr0wVoNxSWtcM7s9DfM79KTjBfp0dOhY_mM759gu1btC1CJmEaotcK44DrEoUZWWd-eEs_33dA5AnafJfzsntRi7Nrvzfo5ryniWeKma1A-njCeZPhVv_E45rsdQ95XSjRePPLspWBZY2vnc-A1juORU1M2Kw6KbH9WujWMaggBjaYRMznoDIlt4Ppt20umPSPcRyZKQfL7MLoDmfwBMHN7xP_x9SS05xk3PEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnLNZ_FaNtlsBK1WmznQSnId0DyEmZ7a4BNZz1NlqjyXDpMvEWPntbdHw4F1EeuqCyGNloVdy7UVMUcRiXzg4Lr9NKQtCJymtd6Oi9kYFQmchluU1cOuoJM1r_L2dPDPgtsw6w2DXkH1d5v_hNtmStY06FEYVjrrcR8vbCUE1dmB8k7N2yNpfJJn-Y-pYDUY5nPHpP6jhucQ1eyj8-PPRmYV2ZvT406v8d4Wktd_1U_XYEsN4lqUyBxulgxMSQca2GN2DMD-HheM4fh8L0AduKiQ5I2Q1jGJgHTFzIpLAHYbPvXlBmvrW0IBm7L6iDWc3a1ZGaApDahVzQ-l6fJjEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ضرر ۳.۸ هزار میلیاردی مدیران دولتی روی دست بازنشستگان
🔹
طبق جدیدترین صورت‌های مالی شرکت سرمایه‌گذاری تأمین اجتماعی (شستا) این شرکت نه‌تنها در پایان سال گذشته سودی کسب نکرده، بلکه زیان خالص آن از ۲.۲ هزار میلیارد تومان به ۳.۸ هزار میلیارد تومان افزایش یافته است.
🔹
معاون پیشین وزیر کار علیرضا عسگریان می‌گوید شستا بین ۲ تا ۳ هزار عضو هیئت‌مدیره دارد که «۸۰ درصد آن‌ها سقف حقوق را دریافت می‌کنند و برخی حتی با تخلف، بیش از سقف حقوق می‌گیرند.
🔹
گزارش تحقیق و تفحص مجلس از شستا در سال ۱۴۰۳، ریشۀ تخلفات و سوءمدیریت در تعدادی از شرکت‌های زیرمجموعه را به‌کارگیری مدیران فاقد صلاحیت، تعارض منافع و ضعف عملکرد هیئت‌مدیره‌ها عنوان کرده بود.
🔹
شستا در مجموع ۶۲ شرکت زیرمجموعه دارد که از جمله آن‌ها می‌توان به بانک رفاه، شرکت ملی صنایع مس، شرکت ملی نفتکش ایران، لاستیک ارگ کرمان، پتروشیمی ایلام، شرکت نفت ستاره خلیج فارس، سیمان شاهرود و سیمان فارس و خوزستان اشاره کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/452860" target="_blank">📅 09:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5z-YOkjU2BqHU7dTTnrPRtGvztd9ZFuvRRRK_yGmVr8LLlJLvp0qJQn4F6oeivgp3pUEo7Qo2qUl5lY4PrzJEbbiyt1m8YVO-0v4daRWG3arg9VkZ2HGE5sDDQMMxVVdLy_0c3C8iSwATS783y-h9TbvcYI9NMS4ikulfrdy3bWx0zmca-OO4UA3-2BP95fRXsXR8VmP7djeWi7nnme9aUQ-OHXPYXOM7h8240qDad27Z0ZP6ldcvYiPHgRHq6dpnWugqaO28DM40dptvrjhh4hfEejKp9m8Ofhc0k69ohp6gKbe7qCa_dr-GQfdaFkejMkFl4pTpm7DcQWiTuMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ ساعت صف برای چند دقیقه زیارت ضریح امام علی(ع)
🔹
ورودی بانوان حرم علوی به یک مسیر محدود شده و زائران باید ساعت‌ها در صف بایستند و از میان مسیرهای نرده‌کشی‌شده عبور کنند تا به ضریح برسند.
🔹
حسین العباد، یکی از خادمان حرم می‌گوید: برای اینکه جمعیت یک‌باره به‌سمت ضریح نرود، زائران را مرحله‌به‌مرحله وارد می‌کنیم.
🔹
بانوان پس از ورود به مسیر تعیین‌شده باید صف‌های طولانی و چندمرحله‌ای را پشت سر بگذارند که در روزهای شلوغ اربعین، این مسیر گاهی بیش از ۴ ساعت تا رسیدن به ضریح طول می‌کشد. پس از آن هم زائران باید بلافاصله محدودۀ ضریح را ترک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452859" target="_blank">📅 09:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ffb7c01e9.mp4?token=cVdNtEtD92aPr2BI1iywDuCFxO2_vMhP3OtneXdnQM4UnlHCUye1cBuKmSO3n4lc5lGT6n27mef-8g0fBkON6LNULXeG-cYRa9pRTdM5_aTbwOSAaNfbaiD7D3w8CGavNT_G9fHox0jyt104oI7FfCrxkCK26AxuKKbVcDpmOSOq9OXXa0yMh6_boJY_pJkgzNSzbNjMmMzOn0B3yqR0d-qGrJS1wklUghdMmYD8SyV7ky9WtF8pgucNO0S6SPH-YAEB1X9b4rMJS7h84Q3fskFGtehKH8TvkwpvZtIBH-d3l8c4Vhd6oB249Eoi78Z_0rifTDaG5S1RfbxGc8xnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ffb7c01e9.mp4?token=cVdNtEtD92aPr2BI1iywDuCFxO2_vMhP3OtneXdnQM4UnlHCUye1cBuKmSO3n4lc5lGT6n27mef-8g0fBkON6LNULXeG-cYRa9pRTdM5_aTbwOSAaNfbaiD7D3w8CGavNT_G9fHox0jyt104oI7FfCrxkCK26AxuKKbVcDpmOSOq9OXXa0yMh6_boJY_pJkgzNSzbNjMmMzOn0B3yqR0d-qGrJS1wklUghdMmYD8SyV7ky9WtF8pgucNO0S6SPH-YAEB1X9b4rMJS7h84Q3fskFGtehKH8TvkwpvZtIBH-d3l8c4Vhd6oB249Eoi78Z_0rifTDaG5S1RfbxGc8xnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از فردا باید منتظر کاهش دما در نیمۀ شمالی کشور باشیم
🔹
امروز در بیشتر مناطق کشور هوا گرم خواهد بود. دمای هوای تهران به ۴۰ درجه می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452858" target="_blank">📅 08:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452857">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f62fbaa4.mp4?token=gDUhT5CMWjCSllyFG4BN1QK-oT8g3o69llWPT9nCm8nx7kO6WK0sxgY4UfeeIo6OIspOcuB1Lb-3KSJS01Xr5Gssx-lOEcnwz19vShYsrMtaLOoMS3R82v-Irl8xgx86UGatQTR0tRlPI_Eqpj6k2YO_voKsJ5IObAf0ckNbfGW9pzNakU5ec3fkrijSMCk1K6sarfpByxrdkVTfyD_ARFtQcUB6fGRBKlC_tEccHrWKvGPuTL5zLJpz1buf8CCMyUW3P0Py6ebn4l7q40YZCPz-gk-DCIY3JdS2SuYjyEy-Y4EeIUcn802KutAExSirtsE9YtZKIbkK_C85QxoYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f62fbaa4.mp4?token=gDUhT5CMWjCSllyFG4BN1QK-oT8g3o69llWPT9nCm8nx7kO6WK0sxgY4UfeeIo6OIspOcuB1Lb-3KSJS01Xr5Gssx-lOEcnwz19vShYsrMtaLOoMS3R82v-Irl8xgx86UGatQTR0tRlPI_Eqpj6k2YO_voKsJ5IObAf0ckNbfGW9pzNakU5ec3fkrijSMCk1K6sarfpByxrdkVTfyD_ARFtQcUB6fGRBKlC_tEccHrWKvGPuTL5zLJpz1buf8CCMyUW3P0Py6ebn4l7q40YZCPz-gk-DCIY3JdS2SuYjyEy-Y4EeIUcn802KutAExSirtsE9YtZKIbkK_C85QxoYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنل‌های خورشیدی به دادِ کشاورزان بویین‌میاندشت اصفهان رسید
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452857" target="_blank">📅 08:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452856">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
مدیریت قاطع ایران در تنگۀ هرمز/ حادثه برای یک کشتی
🔹
یک مقام آگاه: ساعاتی پیش و در ساعات اولیۀ بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن سامانه‌های ناوبری و موقعیت‌یاب خود و نیز با تحریک ارتش کودک‌کش و تروریستی آمریکا قصد عبور از مسیر غیرقانونی و ناایمن جنوب تنگۀ هرمز را داشتند که یکی از آن‌ها دچار حادثه شده و بقیه تحت مدیریت قاطع ایران به خلیج‌فارس برگردانده شدند.
🔹
همان‌گونه که قبلا هم اعلام شده بود مسیر تردد در تنگۀ هرمز مسیر مشخص شده توسط ایران است‌ و مابقی مسیرها آلوده است و راه به‌جایی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452856" target="_blank">📅 07:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452854">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa96a9605.mp4?token=pLyd_SJyQfpBCTLXu5_f-fl2S82RQGTnf9AtX4VUn5q6iC9tvNa6-TqwABLtjEMzA8acFirBZdOs20erM98-DCuJDZdK2_NuyQXfcV1aXUejCtAkatSXO9ziuRxh5pvQfTVQeMy-PErCjYl9IuVsUYZr8oDEwTsz4Q229ltQCZgQzIs8I7NTkit0_lZy76WCGGImunSyvb6-snHdIo_AzvB2nGDMPiYVSLFs6QYfRizYvsdeVbcZ5AnWsg7lbYBwShAzZM1JvlIZBxpgXySh9RRsvp8eh_TJbpMFtAXUs1vUjM51BhQ8XVbVR-cWBvBUMPZtOfphcwhbn_9x7s59KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa96a9605.mp4?token=pLyd_SJyQfpBCTLXu5_f-fl2S82RQGTnf9AtX4VUn5q6iC9tvNa6-TqwABLtjEMzA8acFirBZdOs20erM98-DCuJDZdK2_NuyQXfcV1aXUejCtAkatSXO9ziuRxh5pvQfTVQeMy-PErCjYl9IuVsUYZr8oDEwTsz4Q229ltQCZgQzIs8I7NTkit0_lZy76WCGGImunSyvb6-snHdIo_AzvB2nGDMPiYVSLFs6QYfRizYvsdeVbcZ5AnWsg7lbYBwShAzZM1JvlIZBxpgXySh9RRsvp8eh_TJbpMFtAXUs1vUjM51BhQ8XVbVR-cWBvBUMPZtOfphcwhbn_9x7s59KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی مرگبار در سیاتل؛ ۲ کشته و چندین زخمی
🔹
در پی تیراندازی در یک جشنواره غذا در شهر سیاتل آمریکا، دو نفر جان باختند و دست‌کم چهار نفر دیگر، از جمله یک کودک دو ساله، زخمی و به بیمارستان منتقل شدند.
🔹
به گزارش سی‌ان‌ان، مقامات آمریکایی تاکنون اطلاعاتی درباره هویت یا انگیزه عامل تیراندازی منتشر نکرده‌اند و مشخص نیست که آیا فرد یا افرادی بازداشت شده‌اند یا خیر.
🔸
بر اساس آمار سازمان «آرشیو خشونت مسلحانه» (Gun Violence Archive)، این تیراندازی دست‌کم دویست‌وهفتاد‌ویکمین تیراندازی جمعی در آمریکا از ابتدای سال جاری به شمار می‌رود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452854" target="_blank">📅 07:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452853">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امروز هوای پایتخت ناسالم است
🔹
بر اساس اعلام شرکت کنترل کیفیت هوا، شاخص کیفیت هوای پایتخت امروز روی عدد ۱۰۳ قرار گرفته و در وضعیت ناسالم برای گروه‌های حساس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452853" target="_blank">📅 07:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbdFyAKyj68FB6nZtjyMmHdDCClfey9paqlvbOeSnFaTGmz3BHPNzMxfu25BCCc60RokO-vepzXoJQ7yjcoTKVUMInshwZdswGtvS8QOcASJD-tAUwtIfLEfhSo5cgSfg8QZqOYK1JMm_IaN72jcQtC9KldhF5EtLSYHlCh2fzndmIHvmA73JSy1PgZNTSCKrCKC-Z16fNXl5Prhq-bMVU-EodYIjtFT0C65u2ChTDHUptxY5pl7C2PlcLkjvjl_DiDFsNVFbTjxfzxGeZe_uUmwAfyFdC2-ddj55tbl3s_eUZr9nc2FaYiW0IxJ5A-tqBXHhrHjwIR_mAq_Ad2SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وسایل گمشدۀ زائران اربعین به خانه پست می‌شود
🔹
سال گذشته برای نخستین‌بار، وسایل گمشدۀ زائران در عراق که دارای کد شناسایی سماح بودند و صاحبان‌شان در مسیر پیدا نشده بودند، به نشانی ثبت‌شده در سامانه ارسال شدند.
🔹
امسال هم این طرح ادامه دارد؛ زائران باید پس از ثبت‌نام در سامانۀ سماح، کیوآرکد شناسایی خود را روی وسایل شخصی و حتی تلفن‌همراه نصب کنند تا اگر وسیله‌ای در عراق گم شد، یک اسکن ساده آن را به صاحبش برساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/452852" target="_blank">📅 06:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452847">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uh52dQlzT0pO6YBxyIIVKYkx2WcSkswY4x7J_Osd_jUVYoXCFCEWoZ57-XIcixz3Xj4oCBrAfs-5nRjxoPstsi9FeVuNrVUlqKP-sV2Wrt8cvLmxichM5mVQaeSsjdF1u6xgdPLiydNTHQ0rovy6MWAGRQOi0dS99n-qJYR7rjdCT9vZxwKHzpJzMBWx4t_FJR3WPTxCOMORCmOH2xgwRci78ze4crYFDXpAf-SlsOcDdoV2riRbHzsihfjK9G8EcErIdnPZ5kF5LtSxtBwV3TWVcynotwdT_nTKDWWZCgNbRSIn072RTFb7iRozMUBOzPIx1aTrzcdcwO76qNss_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVZNq9vkD6OYIneO2KCMSxZ5YkE7NTEhSQMaGyXfZhDpeCCCM-QnFlnKoCV96SM3tVExtAoEtZ5SfR6eet6B2VODGEZ3LAV-l-DS7Tdl9ZFsxsdQQ_4BkvRpzLgZxfqrt_bCrjdwwZJYqRiKyKmm29cFceYs3-JxHMAeIs6rI8Nf6PuABoD8ePFnNmJSDAJPR6iMhz9_ScoQwsa3YAA4-pntckITblOoX6bTrpgyS_fToBBZ_g7MGWGVgurAVQcuwxpBmGSLZeUxxo7wRmvjb06pnD3o_yK_3bGjX2GAeeh6QgyvuJCi7TReoKzcgM3d5Eues8eH3PdPde4OsTz2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIJSboXnDBV50nZXyo_EC5YrlprOTZQfCRJj-5Bsu5CeCrJtGtQgdKxRt5SkhXTB2eqCZfy80vBpwT0QxnZZreK0vpx1G3oQHYoHk3DKnrkokMYkR8EZkiSDFYkPnTovrIwP0Oh3nmgm2HnT5sP7binJ2YeaFFyy59GGC_icKAh8Qq1qvH4XSFOgEFuTejwMjPGcWI8_giIqc5yZeooSpqD-FoXG0StkTLOJEczxnSJ_X2ctxHf5t3txUVDEw0_sR6lklMsxgsRY3YWs8m5zIhCJaP2xVT1MPqzeMzNuLInrLYgZQz_oL--Xdd2mPnISFJKKUHzrkcFxXZLF8t0n4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoyyZnwDHSoB9q06B84dUM8rTVjepyEO2VdU268zVHQiBv6PTmThzvE8CYrPpk6XmyDwN3Ilo17TMWQBmCfCx-1mFRT3Jl3TIinK3zpdBKwZWmVr1OisVICmUQKIiM0li543jwvbN0cT1Kqt630dO7Sw8KY6st68cbWIHCFDTpFg4z9hiqlV9nNKrOp48_9aWzarPgncwUESuwfS04BQrqysIi62zAVDIFp7N-NlaeG0-QnwnCZfMtbTt9USQ17XodrwEWgx_-dzqbPc1IVHGQMIAlJQrc4U1riWhbw5zNPNKjFZq_YpObjGAt_jQsGx_mR-7yxTJ-3yvmfBtQrFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N41IFuWC_cTSrD_j5OPx-04TgEaxLB8jEKhdiak_FsAN1KbfnuN0F9d-lMDWqcLayGV5TrK64jlvXp9zSPKu0S4hZdh97m7wVBdzl0ykz7-oSRJuYEeYJdSMKkHkiOw7r7M5QeOM-UpyQsE8JP28F-tItBOYZTUH2WcfAdiJltREorZI2GmxiqnPE42B0RoZGxNrDMwrTjoAT_22SDmIaFfct7vudOgG612IVOB7GaGWpv-0fq_igpFqmVIKxCXBlKKa3LuVt-FI4U_IYhN5doJnvxYkS0E-CSV0Eeq6g4TcLvJRUqnbEhn3sheIE_BLS48p7TsHxjD5Uz7sg-gpRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زیارت خانه پدری
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/452847" target="_blank">📅 05:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452846">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-oe5GyyVjGMEiUyXIz71W7foAJjmOfjhz-uu3fh-dO0ch6pAMDRvXpvsA7wzny7_XDX2M0XHSuPvgcBIw6inMxx6TYtIYJBxDmId28ap99FixfrR_E9rUTZ54llrQ-A1rDrdOs8hNaMLU05pjnA7OK0rVDTP-yC1hJpvqT0WuZEJgwqHeF40RUNEaDJQzDq0BWe3ZvCt9kkV90LPmx3N0SfTplV7b3fzsypxhQ7LIxeZWW3nTlMyGVoWSAm6mG_zSuQL0ghiGhG9CJoesPOaeEbiol854qwaBxsyqKaTsIueIC2jbItRw5ersEwxDJEVZYumY9yz6pIl2nIbvT7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی زلنسکی از باز شدن جبهۀ جدید جنگ با ایران
🔹
رئیس‌جمهور اوکراین، در توجیه حملۀ پهپادی به یک شناور ایرانی در دریای خزر که به شهادت یک ملوان منجر شد ادعا کرد ایران قبل‌تر با ارسال تسلیحات به روسیه، علیه کشورش اقدام کرده است.
🔸
البته این درحالی است که ایران تاکنون بارها هرگونه مشارکت در جنگ علیه اوکراین را رد کرده است.
🔹
زلنسکی با ابراز نگرانی از هرگونه حملۀ ایران به اوکراین گفت: باید محتاط باشیم و هر کاری انجام دهیم تا جبهۀ جدیدی در جنگ گشوده نشود، اما باید واقع‌بین باشیم. امیدوارم ایران حملات خود را افزایش ندهد، با این حال باید برای هر احتمالی آماده باشیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452846" target="_blank">📅 04:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452843">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5PaX55NpEYHjeAj5A-4uWw5ZSIrvaSzBV5AhTC_JoZD97KeS-FP2Kp6VyS6r7qixgCValQAG_jAx4FWyfqIHJHle01xuPzKpyXGbsPI2bJ8XwYlHKDqjovLAr43rstBCeEZi-mU08uqX2ZhgS_8oQy9oZflFdomNvuKJgzydW6qc3KGwoMJSe4qkQNkkfAOWvdWl8JyLo70tzbGP6M5EyRjd3qeYqT_WtWssvx1zvinkTOzzJcWynjx06r0mwMD1itdQsczMS6YHMKYwoJJenT4MPCt1FyLIQ919kQ4ia5xzjB2wH2oq1HGxUTDbj2YbJc9e3k_W9W4trw3D2PyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZcbSwhaVXN74h4bE4KZEUclvhG0c9mCBE5QTJ3dIwy3VN653s4OYcTzNY5WPAhv1Hu4vnMg6flo8965euKx6-PFs7cwBXVNNqMF_XFk8RiJd8pPKGo7cRAAG-4cd5uN4kYhGfW4-eCfmEDOffHJQa3tP8un0tnLJn54GBIcw0QuixOuKNdEV0bDFAfQpdjt49FtJkm4pJeuORQE6HVvasKaS7bu--R2xb6AKVKDdaRZURuYZezMXRUA6XxtRY4dXDKK7NLZghDig6kaG8nJrdhUStJyP9OyNkBSJho26kmKWyZWJRaLzNdqxrEQR9WyAgWQxid_3lUmwWMcT5oawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ac7IFDpjvRIFkYXwAuQh3-nmmdcT1Hl1nirSFRtMJksflBV27LUIQtU_9jgjH-FBguMohfh_htiI75yO6TNpydBfOp0yoHrEkNPg-VlWbtqc-7g1cJUTZMU7OgHuGZdMRTjz7ebjxAz7HP6Bfaeo10wanL_VkZ7D8iLlzC2VaT76F1Yu6Cf4T6plZ_J3AbabSRKSQtYjKvllTgrFtqEEwqBAtAwGxRoFDyGxRgOnGxwCBdzcZWPWU2Vwspt82NCTlx72ki6Cwrc9-uTDMxFkwxpEB8ZSgQVS1CZTy3ZYcTEebfmx5wo6pPMYbTTM_OMc4TAucIk_NbCw6-hZatA8MQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک تایمز: آمریکا در باتلاق ایران گرفتار شده است
روزنامه نیویورک تایمز در تحلیلی درباره گزینه‌های ترامپ در قبال ایران نوشت، رئیس‌جمهوری که تصور می‌کرد قدرتش هیچ مرزی نمی‌شناسد، اکنون دریافته است که با محدودیت‌های متعددی روبه‌روست؛ محدودیت‌هایی که او را بیش از گذشته سرخورده، آشفته و در تصمیم‌گیری و رفتار، غیرقابل پیش‌بینی کرده‌ است.
مشروح این گزارش تحلیلی را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/452843" target="_blank">📅 04:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7231578114.mp4?token=fuvnPhpPsgCk0YZ9V3Jp1r5bvtYsEBlLlSNKuAPn_kDciQy3C6NCnnkwEJYMkly0hyONL2Kgd90CzZ8JVj5x2SiTJDWyEwpcTMdQ3z-uLtnbHsoVZMNtKDewdIfhyQ3vuTExf9DuTOStd-xwPdczU5HW6EEmvSmp9rSpPTHaUybdSIl3SM_fKQGkbDYePWlEl69s70g65BBe9HkueYWR1fZqng6fn9aYQJnjuqd5h5l6kHpsZNswvXE-WA7RJoh_GSC9V3sg_X0PdsUPp6m8JIlXHSGQGzsatvQ8kG87g3kDfTRXtq_c5FiCXaNOL5nysaFAgre1Vaiqf3zBgsxnmYkBik1kwzajSCzI6u6jj_xVJlJNQ31tKWjcgfqVOSrsZLdRGtEP0nUQ4ZNjNKcBMAU_9ANXmLTD6z-BbdonBN7YkG0t1yOEaJHL6johTocei3EXC9_pXhweRIhmPhwiYTtdoB4vItKS4-Uxr7iCouhl8JihWRt7e6jxUjJnL_WIAc2bkuOKy2E6UZ5PpTxB7xymdvHNKjF7YhS-zTAq0GwOYxz_-Uy_PND9QxTv_2ZBwmgGgZ3pubQyMjbE66QlGFiszENdOwTlSk6hdTUwzLEitvcGqU0vCIG8nQOpMyVZbraMjj5pasIYbZHMmgz4yaDF8i9DTX2Usas3ss8payo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7231578114.mp4?token=fuvnPhpPsgCk0YZ9V3Jp1r5bvtYsEBlLlSNKuAPn_kDciQy3C6NCnnkwEJYMkly0hyONL2Kgd90CzZ8JVj5x2SiTJDWyEwpcTMdQ3z-uLtnbHsoVZMNtKDewdIfhyQ3vuTExf9DuTOStd-xwPdczU5HW6EEmvSmp9rSpPTHaUybdSIl3SM_fKQGkbDYePWlEl69s70g65BBe9HkueYWR1fZqng6fn9aYQJnjuqd5h5l6kHpsZNswvXE-WA7RJoh_GSC9V3sg_X0PdsUPp6m8JIlXHSGQGzsatvQ8kG87g3kDfTRXtq_c5FiCXaNOL5nysaFAgre1Vaiqf3zBgsxnmYkBik1kwzajSCzI6u6jj_xVJlJNQ31tKWjcgfqVOSrsZLdRGtEP0nUQ4ZNjNKcBMAU_9ANXmLTD6z-BbdonBN7YkG0t1yOEaJHL6johTocei3EXC9_pXhweRIhmPhwiYTtdoB4vItKS4-Uxr7iCouhl8JihWRt7e6jxUjJnL_WIAc2bkuOKy2E6UZ5PpTxB7xymdvHNKjF7YhS-zTAq0GwOYxz_-Uy_PND9QxTv_2ZBwmgGgZ3pubQyMjbE66QlGFiszENdOwTlSk6hdTUwzLEitvcGqU0vCIG8nQOpMyVZbraMjj5pasIYbZHMmgz4yaDF8i9DTX2Usas3ss8payo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در مسیر کربلا مقصد یکی، اما نیت قدم‌ها و سختی‌ها متفاوت است؛ شما به چه نیتی قدم برمی‌دارید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452842" target="_blank">📅 02:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b00bd17c.mp4?token=O0_kwwY8Sad9J06QZeOqPqdu3a6bAMKsevIKJcVnfG4Cvj4B15xwcQSWFYiFwqN70RvIlddhI05LqKRzdG5vdATJOE0WFD_1UtK50n_7mi2BxZicT5HcPnM55Wuu0seel8cosyxpfphQTC9meuPMOKPqOWB-C5MysF5_4zXFjvRO9HkUABQAoM6PoskMqpsl6ZBz-54_ohmH18HI62mQyZyxDqOob58iutJbcKG3a_nXBJmCZiWQrGOhx2YxqmTqY8qx2P-hN9PHOZhT2_B_74-o5M85Nf-6shtIooIsqtccYfpsh2O0P1NAZmPOULGqVbqO_Oie6TF2aQhB9GSTFjw1_wb8hQkQwzNiQCfDQQvWCdl-xAIVlJnkP0EHUsJyqFmjXkZ7creiJl611wXxA2CM-xD1Iywz8LMgtLNWoCn8zGRcwc_lPC47EZowxNbFw1UhHzOFSCVY-E3-VqSGdgr_4gG3ckAZ-rrV7aML06vdtpfsn7q-V_6qwKUisTUIIyzICM1SqEx02cE4UlyNh8hvNkmBhqfKFQVY5su0ZGE_-yxGefJyMpOE05DN9Pk7ojm3pRyn9jM6W2UzHspy5EUyptvI8pgMMgIhclaCLKWjEOG4jjHJCh-dBiP3pLcYs2948ozS5PTR2kqRCnx71pAfTL0xCVdx62_a0TP50nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b00bd17c.mp4?token=O0_kwwY8Sad9J06QZeOqPqdu3a6bAMKsevIKJcVnfG4Cvj4B15xwcQSWFYiFwqN70RvIlddhI05LqKRzdG5vdATJOE0WFD_1UtK50n_7mi2BxZicT5HcPnM55Wuu0seel8cosyxpfphQTC9meuPMOKPqOWB-C5MysF5_4zXFjvRO9HkUABQAoM6PoskMqpsl6ZBz-54_ohmH18HI62mQyZyxDqOob58iutJbcKG3a_nXBJmCZiWQrGOhx2YxqmTqY8qx2P-hN9PHOZhT2_B_74-o5M85Nf-6shtIooIsqtccYfpsh2O0P1NAZmPOULGqVbqO_Oie6TF2aQhB9GSTFjw1_wb8hQkQwzNiQCfDQQvWCdl-xAIVlJnkP0EHUsJyqFmjXkZ7creiJl611wXxA2CM-xD1Iywz8LMgtLNWoCn8zGRcwc_lPC47EZowxNbFw1UhHzOFSCVY-E3-VqSGdgr_4gG3ckAZ-rrV7aML06vdtpfsn7q-V_6qwKUisTUIIyzICM1SqEx02cE4UlyNh8hvNkmBhqfKFQVY5su0ZGE_-yxGefJyMpOE05DN9Pk7ojm3pRyn9jM6W2UzHspy5EUyptvI8pgMMgIhclaCLKWjEOG4jjHJCh-dBiP3pLcYs2948ozS5PTR2kqRCnx71pAfTL0xCVdx62_a0TP50nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای رواق دارالذکر حرم مطهر رضوی و حضور زائران در جوار مزار مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/452841" target="_blank">📅 01:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452840">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shohFFtIFUodKhTtKZWTLdpFQGbtuvhp5ayjG_Qf9PCKfZT14M2_o_WWZofr4t5XJhmttCanj-PuBFRpRaU70lUOYmhkV7JF0aG2mh9HT4xN4EEEq3siCUtGrWvUUik8hr_kW7vC9Hmb_yn2tw2kqNf6ujGfBOqFiVIGjKgVg5usRejHph151DWDMyZlW5TGzK1mv-x6uZz7T6bIYgOJLQu3Q-PMVVhDUM84ER7pYB7xE2quvo6N89E7b4mrgDHDnI0os-WT-iEqrpbxfhZmUEDML8_ffi-3vM5dkSrUq3axWfJIQEtmBck3oQfO4V_9hUdQrdyqF2BcG4BefaXtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز دلایل اصلی توقف حملات آمریکا را فاش کرد
🔹
روزنامۀ نیویورک‌تایمز به نقل از مقام‌های دولت آمریکا گزارش داد که دونالد ترامپ، دست‌کم در مقطع کنونی برنامه‌های خود برای گسترش عملیات نظامی علیه ایران را کنار گذاشته است.
🔹
زیرا تشدید جنگ می‌تواند ذخایر…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/452840" target="_blank">📅 01:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452839">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b0730aca5.mp4?token=Wt_J4SUpApnEVmt3IG5nCV3jDe5gvP1Njo3HNhrzx3ztSbDX-B57hAIvDi1aRhJGFfJvT3SYLgz8JV2DocoFFQwNdboU1qR2KZGUKtqyt46Lb6xOeWG2IGvyP2XrpkYmuexW87-FGoFqGegWZD4o4ZSGDejY6VomdxRXw6vpee6-1BYjL52Pu6aIbIKC-AV5IWGF61Jg51_7584pdRmrygk5LndUXQX0HEu8J8j0SQET-vcl_9X-IvCFN2rfBkGoFg2X6koezQpSBfTkP6cmXXBiHPkZfxMZIby3mrMxg2rGWutvVAAisoXKZ4c9572EOkfi5iLTMrXCFqM1snCozZ2s69JxZYZTtW-OStvdsxZ_kMQ2DGzPtWrlIEIzoxgE2oCytPpa0FvdP3jqe9ft7IqNLir0fZjKln-TTdqXurqXTvXMMfHqfd1pEiVL1yNIPEL7tQ4p-He1xZ_PyI_gOyviqm2BxkpfhsO0gtaX3HLxr6PNWMOITYK-GTEb0_ZjlO2dp3RQQxOMvcX1ZsFQex2YOllPCq0EO58U6_ghAMCBsDje6oDyuvTxstnphdkfEK84CxdtEqg7xLF84wKTqUou4nyVClvYpM_XHeAUQl4mSgILh2eMypTffAjs27WxrgRtkh0p_nZXA0vQVRvihk13Js8QCb2cBpe-xJnBshE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b0730aca5.mp4?token=Wt_J4SUpApnEVmt3IG5nCV3jDe5gvP1Njo3HNhrzx3ztSbDX-B57hAIvDi1aRhJGFfJvT3SYLgz8JV2DocoFFQwNdboU1qR2KZGUKtqyt46Lb6xOeWG2IGvyP2XrpkYmuexW87-FGoFqGegWZD4o4ZSGDejY6VomdxRXw6vpee6-1BYjL52Pu6aIbIKC-AV5IWGF61Jg51_7584pdRmrygk5LndUXQX0HEu8J8j0SQET-vcl_9X-IvCFN2rfBkGoFg2X6koezQpSBfTkP6cmXXBiHPkZfxMZIby3mrMxg2rGWutvVAAisoXKZ4c9572EOkfi5iLTMrXCFqM1snCozZ2s69JxZYZTtW-OStvdsxZ_kMQ2DGzPtWrlIEIzoxgE2oCytPpa0FvdP3jqe9ft7IqNLir0fZjKln-TTdqXurqXTvXMMfHqfd1pEiVL1yNIPEL7tQ4p-He1xZ_PyI_gOyviqm2BxkpfhsO0gtaX3HLxr6PNWMOITYK-GTEb0_ZjlO2dp3RQQxOMvcX1ZsFQex2YOllPCq0EO58U6_ghAMCBsDje6oDyuvTxstnphdkfEK84CxdtEqg7xLF84wKTqUou4nyVClvYpM_XHeAUQl4mSgILh2eMypTffAjs27WxrgRtkh0p_nZXA0vQVRvihk13Js8QCb2cBpe-xJnBshE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناگفته‌هایی از چگونگی انهدام اهداف آمریکایی
🔹
چطور هواپیماهای آمریکایی روی رمپ هدف قرار می‌گرفتند؟
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/452839" target="_blank">📅 01:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452834">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZlpuhfKo5SmanHTZYy17H0N1y6T17DwIVYnax0laRh3LfeUBlr4Nr4lkMSmYB42lOBmpEbYZhmtL8jj-h_Ufj41SRIfQiTPMLHB4RH2NurM4bn7im7YJpht2DpTn8R9vCGxXdSX__o61Oc7WPnK6j4bzbibSgw9ZaDxLjdyOukLr5uXXupXoI1umCqc2WgB9F_qxVn3GBmh0guC8UABqQsvfmemUIP1vAT5EPdGdqpKSa6kitsJZ7ecsw4HSU68hfzN5zVB0Pt2z9zwjwJ8H0XrfinJEekL8-Uki7N_sML9csoKh3dgpkMbykJSF0FBi_5g7AU8oJx82XW6MswXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGV9A41K2Zs5dupJY8CNlcy7iL4coUvGnoT1eGZDWiqkutlF9M0cSRv-rKGX2kzVcGiVA2Ro489Y6PqcColQ4QF3L5gbM49PHjK0GzUinrkc70lTaat4tlrAgbs-Gwt5qWwAadZW0em8CWVibiGXZEucECZXv6CQ9IYmd9GFSy56n4oK34A92H8zk78ChtJbjozhdrFtlKmG50sL0_HRDFG6X9P6wyTI4S0OROpBfDvE9sRobPRFlK0DODiEZeXLnWYtw_eFsDE5T3fKf-25Xp5DcYXbD8Suk1q5x4DZ6mn_Pklu4dopj75fZfR32QfiXKCDIxMk714zfDo9_H6zmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJ6kG4QtQJ1p2FK9pdX-nemka-CH3ss92D4RD5GwPCmQXdl90YxsHjot1iJ4Djn0As2Zm6-7oT5032l5E4ycMjAKSqXDoenpepmH1u2BmTt6sxSAwsTvsFWRQBTgDqwtkdv79sHkjaEhSNplxcYDuwf59gNd3YxbduNwyvLP2c3tkc9NNKaLqXLOARYvqZfj38cBwYHZqYq_JpIuwqQ_wQJAddLWkANRky6pabKa9s02vRDawyjaw7RQx8PaR8Oc3jxP8AvwnxecUZOpnjCAQfLvFyMOTyIDfU3g--k9_0vh-3-gjBQMrlq2NV9gkapq8QalX1jax8p3y67tbr9ZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dw0gv3RE8pFUphxuEBQYLYNPZ3IToNJ0u8_Yq7a-sEmIf3D_K34onS_3xgW_xc0mhzQfFsJvPoyOSh4_kY2ktyaU2o2HSD6BIwmfncVxzJr-CYPid5189Z2cBV1ARHz5bZrs8hwjCN7RELNLMJ6FIvNqX4iIYGzNDccektknxW97dtWmI2i45UP3qrfSUXwCeFfn7o_3IPK-WkoyUOc_5Dw8UaXdWiD4E_cTHXNza_Jc1ZJWbRL07cnLRilcgnZGFcgvHNvSt0_Dv_gtAm-weQY6TdVbz-kyXAEEtwrMVP4Pl55sAvnbXOniijFdLaKnf2aLGP0GTNg5HqRoTwk9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVG80nPfjgwpRCju4o-FWfw7_qpPGydzq_5LUqkMp-89UuWIm3Aa9JNPyz3x4KLgEfgaHHUnduy1rcwYFtTj6BpSIVL8HlNBN0f6ozAq4DqH-5Xn9nBj2svee6Je8TBh7HTa5WjqSqcJ7gBFnaMo6xzRurzl_mB26l5gRCvegscmLg_6tluwrXQqUO8DkGWMRT-eMxCCma8IZkddihWgWe_Zc87v-Duab6-63a9R4JaafXqAuCs1WQCJBYMT3Rn9-lvlTXVrI-enpyZLGvDz0oQqtdzuqf4cI5YRMtx4StiPjjggWrvrEM1iQidRI80xKmTOzE6lFHMwC6prFV8LWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۵ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452834" target="_blank">📅 00:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452824">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwnuSC37F_0NO53vLPtXjTI6sHmt5cyOTQQfaubW5sMqzMSQJ4h5Mt8SyTOGmz2BIfeiAaLFXNO3hS-zIB9y2PLtTKQi7dxBCudp7ckYpLrOBnXcwVVA5Fyo6RQPcQrYimc-D7RmgcFXiTknkr-RgGXF3eiv8JDnOvcLglZEaMrCCwA7uZze0B4v7vDyLo3S6pjTTQoSDBSwschlz2BCaXedu38YXnVNEVtQtI5myCkGjzfTWj9XcK4S1rfLJgPp5nYfyk3ZuCPUaQShGFWWzC8GKojm4NxBUh3Gd-0l2sN7_MZngCHOlZttrEE6E78GZVSV5MBnA3J2xQyc_29r-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTLOkpM2BtKnMpMe4TXIDtvEGNoPTaHQf-YWUC3SDUvh-KSevBQ683SOaOtPPewYh2dMCa7BjYNlk2dLe9hVTa1EXElqPhAWCuzVTf-VtGzp3-f9DZ_JYqTLT6_sCxdIerDPo7My3GmKe0PkPUznJ9q42X2fk0Pmo9HgqbCHrEJunt1GMfpd_X0s-VjJo-sl_wS7vJv7OVc0i_dEPe_dz_Mv6kofAz-osDxAUuf1XYvDeWoZzLIFut0aJQXrZo_mUFD4rJSQOao0xDvB4vkLWtosBmkCxaXnR_JIM-hfmZqWWmnYDn_3igpVFv1PkC0EV0kvTPqettWW5ZnHHpcN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1rQW8Lf9Z-eTSXD4EG2ITFu6IdHGgku_nGYqg-50-yxp8_OsB0q0PdXkkXOcF5kTnVKlWEffQIqqBat1YJpVpjaETTNKkQutUmMbkrjPD5To4btxBVjdjcmysf9pfPScmKaddmu73EXqSUOaloKDJxs6oxhlkvBMop5og2jxAkJnXZWY8adIrbHs5of2xk950lCqy2It6WQE_2szBy4wFItnHgq4tdfURAkNE_Q0Ii2s-IB2ZNn9tiM3n-E5zfbvdAz3Kef9QTnXfEjVA6_CyK7ZLie2JX8tvA4pGJIyfdp0JXxkKNkF-P7J79AvV--ol6M2ZdkvTad865VDegtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYqNtLx9o0pM1Z_55oMo7QplO1TmDjbTD1wNvrw2mqbpX2OdG7_wjf9WW80R_WCJB-dbPtFYMWJEuJQ4gSPcPoV9Zu8N3M8AwpH-QU2Gm2yKvPel4HIRfzp523CzXgqrpX1PnydAznUwMLofwx9tLQx2YqQEaeh24hoLNaYTW6edQAj3EmmR7r7ygpqI5MvADe6iP6zoeDfvvJyQuNkQBkSPe6TVpaMtIzFSFZ1TT4esa3wixTCT548jYQo3F0bvodSaXTLVMcsIIeQ05BT_liA9UJ3HJUCfmUtQ3oGzxMoEPXL9J9HKNG2SpqQKbtabseHDER-TV0h7DSKtrUQjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCL23lmQQa3e5i_6ix1HXoE316xZAF1uN7SKhy0S_TmoAtECjLjp0nnm8znZyVs6mg4_wH7hbP80ZxdoGzBUqsir8-nerY64sz2XLDWI6pz_HMj_kPhy3-s2AKzZ2Kl9_zqPuA3IgcaMQSeBhv94QKXsCn2l-ZQsIBiJPaojD3zoQtILwopi60CXKeVCO9OnJyKNR4kG0XK_hZt9Q4uefni3uaNBnacVJ4hlu7elMJQrfSPOcAqbNlvMTfGV2RqQkx1JUddUjoPLq_EhRKRwBxPYmIF63UVNJ0Jt9psWcEZHUtpA-GFaCRfq9uPw9kZdYgIynDMBKLXf--POITgzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rw1qBmyStSJdAB1tRBe-pn4mC4vlY_Lj8eV2QnJzzFVZeYD5VnYt0Qi3J5XKAT5IhhJWV2Xnxt4UYOuiAg7Mi1tZJkGr51ozj9vyG_adqOuiKBPpFl4HdIdR2GqwhxtEs1XUTz9IttBM-3J9mPJbcClrno20fX2yKDg-PD8M7pUqGSVmh2IUnM0HETbiAxm9HLkOLVPyVTE4DHRCylyjNUx4DNNdC9HZM9X1hT38MsmdvBRDwU5lVFRFL7BJgMDJGuuMuE1X45ZyKwl1OxnRC-iHFCRYHKOlUqzjYgFvrE96wjX42HRPSJDkRrLNjNpl1wSuOmBFbbDUzxAVQVWEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-3j4WN-rSS0Kp-65TundbzCbClTz4CDbZfCbFTFXV7aDj1AbiQObJifb1T0Up7hmyry56xSvI18Vx0Zk4qd8JG79lUgGrvjo6aeMBMSFTVRUQvPsS2kMIbwmmup5Knhgo_aBlGkJeneoUcF8zTLYz0Xc3_SpugnNgrFMqbeyWu9PBtPYcKM4ocl6aFXmn2tCbLiiWU5OUPLSRxx9plej3HeBwEMNCFhd4SHJcdZn3jj_34Wam33_xh_HY_LfWtsv0dYf0p71VHjGowmhnMPNzMLfvBVUfGV_55J0KekH19G62slHB1GikIzkEpy57ofWEjZwo60iIXBbm3NJ0wE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfEKrE1k4EJQwyPp6UKHvJzj_HqZXxtHr5fGWtDpmi9e9m5SbuJQRayO3Dow2npE5rCATAj_KqQ7Sc-zELHHV5UvVKfHO9tiy_oowCx9m63C_B-Hcciqx_pOstnyf8QL8WPPk5rue3gk6Og8A0y_yEkykXAovoKoAQrd3ejyLMDh_0nkVPLAoa8EsXCbBFIh_48etc6x5uoOFr-MEMWbO6aKOtA4o2EIb5aTop0WQ3RvpmGcSPpzy1MGvtzANqjrKr7pFnbpI4rqyhx1eEz_mSPhLOXOMQQLBWFrzXB-xsijR0nxdBryIiQ9DeV0wfkmm1qaXc9ISOmxYXR8so0VBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRtzY3CA8Yav3d9jDqhntf1XHlR2Z2kIqLKFH2ven9el9nNwmz4LyRnWyfJqzN-iNPv55negLg4QZx8o-Zg_-fEksow0wTUxBGzNVkfTgBtmwIXvmn3X_LtnZERyxpzqoTXpDuq7UupzPEEBCngJ7qkJzqo_D5goELL8NrdVOyLSCQ7tFb_S1OZS8bcpxUg-PIjiYS7b6WmpZY7FOWCJzg4sUKMw84prlU9ZsT1Ox55pR8OfkaO0fcq0YicMkQKzPPtypYaphbadFEnaGSQ2NI6JhoFNX5gXcY0_2z_Pl4ArU6Fnufa9u8JykGG7qUeBDgP5u6uT880gxUgyLXIvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4NXkg9cKb3sG67mKupE4OKlK-0GLxQ-s2cAML9GyutJL7BG_7BP8zAk5zvRGtiADD2opqygX_DuqglvwQ49ui0UtDqlh7gqmlNHiOaW-spjit7387_66b7B7FSfwr04ZSSowsczTNvG4sYRn6bG8RuVO8QjqlsQQqWTkARN9dDMryj0qgnttQa6dpPhwXCygUnlvpnuGf8c_yWDnhD4AGaFUrGB97KfA74WV2o9FR86eC0xZ4R4fZ1EwM4ugmZfp8236_vbRew29cziA4rvW2zY_GlPx6AV32IAE2E5YhTrr7909CkijN9mcI42W-ghGZCn_OID14OFKqq3Pxq7oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452824" target="_blank">📅 00:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452823">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTKwEPWNhkDCC3-csdleasqGauwgo3R1rBCnWVz4aaCnv6zLH-4JT34jonzZ3dqAqJeVJ-QlD1ZxznlriiAHKJYva7PQL58Maasstxu4HM6KrYo2BhxVxmUSnsWFLishsAaCsECDMFUMFd2bjCVtz8Bmmbhnupg4Z2Ly5Ik0tNscIayvM2lfZccsDCAu7BKsGD3o_eve-SqqLufdcmJ4DZeCCMxU5mNQK2RpJQglNMben1yseTruUI1Q0I8ZzNdlKRPTRrTcuOKhsAP7giBFHJg4TNISlz4LX0xKP9OaxUNFak9rr8QFxNMdoKY794oBYGUQ5YQJsPXr83y7J5OmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات معوق کالابرگ، سرمایه فروشندگان را قفل کرد
🔹
طرح کالابرگ الکترونیکی که با هدف حمایت از معیشت خانوارها اجرا شد، حالا برای برخی فروشندگان به دغدغه‌ای جدی تبدیل شده است.
🔹
مغازه‌دارانی که کالاهای اساسی را در اختیار مردم قرار داده‌اند، اما به دلیل تأخیر در تسویۀ مطالبات، با کاهش نقدینگی، انباشت بدهی و حتی چک‌های برگشتی مواجه شده‌اند.
🔹
فروشندگان کالابرگ حالا بیش از هر چیز خواستار شفافیت هستند؛ اینکه چه نهادی مسئول پرداخت است، دلیل تأخیر چیست و مطالبات چه زمانی به حساب آنها واریز خواهد شد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/452823" target="_blank">📅 00:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452822">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8CB_jN5iWEC9pWZLXgBYiiwidyhwvJS7_6QSIMm9w3Szo7CBql1gYe3gHQNZGCd8OJnXpwF7P1HiWos2lVDVtZkLumTA1oX5d3w8Z9Nt4ke-jbCYkWWssmEjrUWXtppqDjWmN8GNHlHkPl69Uw7TYherYUwkfj5jhIOyCvLunbiJ8jM1hjoyKLflWkpsRC2K0DJtwV75LTnnM5ndTHKXxeu8dwWJ_uvEFyjyE-aqtKpPOs2HWOT5oaX4t3qrxlXVVQFxZbmhZBrkxxZtmQvMikewXNMizAGzS1HuOU0vGnnlhQMfEhB5AM821WbBuDvJh9KkhI1Xuxfp9wS9xLEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با کمک هوش مصنوعی از تنگۀهرمز عبور کرد!
🔹
رئیس‌جمهور تروریست آمریکا طی ساعات گذشته پست‌های مختلفی با کمک هوش مصنوعی در حساب خود در تروث سوشال منتشر کرده است.
🔹
انتشار این پست‌های مضحک، ترامپ را به سوژۀ شبکه‌های اجتماعی تبدیل کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452822" target="_blank">📅 00:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452821">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تردد ۵۰۰ هزار زائر از مرز مهران
🔹
استاندار ایلام: مجموع تردد زائران از مرز بین‌المللی مهران از ابتدای ماه صفر تاکنون از ۵۰۰ هزار نفر گذشته و خدمات‌رسانی در این مرز به‌صورت شبانه‌روزی ادامه دارد.
🔹
ظرفیت پارکینگ‌های این شهر برای پذیرش حدود ۱۵۰ هزار دستگاه خودرو…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/452821" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452820">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f4ecd59a.mp4?token=rBcEBqN0PJXTx3FV06ICCLxPncEF5C3beMFY3WLRQvEa5aKAXYCXUbZLTTjctrS1d5WmS7l3MjNCPXxcGp59lGPl5qoB-w1qQo9FhLC23vBs0nLRrsvbWJ_QYNsqHgdZDOYCLh6HD7BdJdy5onM5Rj81_F-h7QEpM-05QoVz8x5rATh8TQIXHCrpXMVzDqypzn36QQLPNj8oyFbLydLi-DgvSWgInDd1ZmtEgCcPytVXtGDR2c_vQSDm-MXCRhfBd8Bs7HCSZ3r9q9Hyo2kLFYYbQoDOHHX0mld9QkI1tUfqclbZnHe3CKPvxVUv9AF5k_2-w70L919W06e6FknYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f4ecd59a.mp4?token=rBcEBqN0PJXTx3FV06ICCLxPncEF5C3beMFY3WLRQvEa5aKAXYCXUbZLTTjctrS1d5WmS7l3MjNCPXxcGp59lGPl5qoB-w1qQo9FhLC23vBs0nLRrsvbWJ_QYNsqHgdZDOYCLh6HD7BdJdy5onM5Rj81_F-h7QEpM-05QoVz8x5rATh8TQIXHCrpXMVzDqypzn36QQLPNj8oyFbLydLi-DgvSWgInDd1ZmtEgCcPytVXtGDR2c_vQSDm-MXCRhfBd8Bs7HCSZ3r9q9Hyo2kLFYYbQoDOHHX0mld9QkI1tUfqclbZnHe3CKPvxVUv9AF5k_2-w70L919W06e6FknYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدرالحسینی، کارشناس روابط بین‌الملل: اگر اروپا در اقدامات آمریکا علیه ایران همراهی کند، جمهوری اسلامی آمادگی پاسخ متقابل را دارد
🔹
تهدیدهای ایران در مورد برخی کشورهای اروپایی معتبر است و توانایی داریم که پاسخ دشمنی آن‌ها را بدهیم. @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/452820" target="_blank">📅 23:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452819">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b72f70b.mp4?token=XiOPYvWoKyg3Uora3_8AV6x8uqSyOkRpxIDEhlt5uZ47BRtaO042jej-8mavkWU1oYXPCPiYlTcd4EkHgXitdIurqK2C9b8LjGqBu3czgvA4tqnqiWH0-kQ3iWT8vMlbUjITgrsjTA13mEcqRZG5MdOpHWRH8o5dp-0I5twWjlsTW5Hexb0u-2-TPgEvmgzy2nRZum27ExaIspfWDcNTRHbQ7vu48v0H_dKdwqQxfTFBGUvNBqzaSBjfECV9dIGQaCTt7Mu_Pns9S16LiKBL0HxAwplRRT6jucO4p8SB8vGBfpXAVTyTCVNrYrJwj4JKnscvVuXwb1c66wNgGPDLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b72f70b.mp4?token=XiOPYvWoKyg3Uora3_8AV6x8uqSyOkRpxIDEhlt5uZ47BRtaO042jej-8mavkWU1oYXPCPiYlTcd4EkHgXitdIurqK2C9b8LjGqBu3czgvA4tqnqiWH0-kQ3iWT8vMlbUjITgrsjTA13mEcqRZG5MdOpHWRH8o5dp-0I5twWjlsTW5Hexb0u-2-TPgEvmgzy2nRZum27ExaIspfWDcNTRHbQ7vu48v0H_dKdwqQxfTFBGUvNBqzaSBjfECV9dIGQaCTt7Mu_Pns9S16LiKBL0HxAwplRRT6jucO4p8SB8vGBfpXAVTyTCVNrYrJwj4JKnscvVuXwb1c66wNgGPDLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدرالحسینی، کارشناس روابط بین‌الملل: اگر اروپا در اقدامات آمریکا علیه ایران همراهی کند، جمهوری اسلامی آمادگی پاسخ متقابل را دارد
🔹
تهدیدهای ایران در مورد برخی کشورهای اروپایی معتبر است و توانایی داریم که پاسخ دشمنی آن‌ها را بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452819" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452818">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp7vW8S3xvw_ze39oC38bYPAnQ_tzoS_DKawvCLWWNz77Mxl7buyymMJO2ZPU6Sf_DN8NiYYlTnetSFjcsqWRuNq5_Nyjn9HHu8oXn-20cL93sw7fm5ysik7OfexhzI767GtdghvRn76qPUA8_PBHYNNVS--hMUzhvO3obumvKPTglzaEqGUZKgJ5HQDy1zRucMIzrHWwgPUBDH1UFA6GHSN1uDO9yHsP2eX1ZUSoUOGYorlfBkTA7yXx5g-FfXsU15y8m5csm50J3SoBp0KYeZnL8WVhzP9K4L_AMx7xoIPM3_AoO4dCGUDZ-SAltDRFuAFJ1k6eEpjF6QtTW_PUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹️
رضا شاه، بزرگترین زمین‌خوار ایران
@Fars_plus</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452818" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452817">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4de6a51b.mp4?token=oE2iozIeNH1Fkmre3NCspAmlxzJqoe3audEtfNkcFR99oPFCqOFXhWVvFvZWM2a78hyOXFd86UPkkMe5WvZhmC-Qn4t284JibInOccm0NRdU2NXt9A4EBKIykNwv4GY2jSOQevup3Fe17i-drhD5h4NlLy8vHGeNAXBv1DfTeC_sXzk5Shs_RpS9wfQ0ZgXy1RPqQDtByOyHRy9yhUTxCTVR3PgvvZBt17ssd5ZXDWwaAmQFwctjnGKk__fxo3_iv2PG8zyyKvi0rr2bGIzOFQmTHCNto9RYb35G0wyajG5CBNw-5wwvSOdX5ow8g_DB8LJJSkvQOKl64mdge1zKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4de6a51b.mp4?token=oE2iozIeNH1Fkmre3NCspAmlxzJqoe3audEtfNkcFR99oPFCqOFXhWVvFvZWM2a78hyOXFd86UPkkMe5WvZhmC-Qn4t284JibInOccm0NRdU2NXt9A4EBKIykNwv4GY2jSOQevup3Fe17i-drhD5h4NlLy8vHGeNAXBv1DfTeC_sXzk5Shs_RpS9wfQ0ZgXy1RPqQDtByOyHRy9yhUTxCTVR3PgvvZBt17ssd5ZXDWwaAmQFwctjnGKk__fxo3_iv2PG8zyyKvi0rr2bGIzOFQmTHCNto9RYb35G0wyajG5CBNw-5wwvSOdX5ow8g_DB8LJJSkvQOKl64mdge1zKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک: رژیم صهیونسیتی از صبح امروز حملات توپخانه‌ای را علیه جنوب لبنان آغاز کرده است
🔹
در این حملات ۵۵ شهرک در جنوب رودخانه لیتانی کاملا از بین‌ رفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452817" target="_blank">📅 23:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452816">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a2d1b2945.mp4?token=GOGOzhuM3aCQUdwz7JZnDFh7fL-theHeBTpqaWj1Ghtgyu67-AslaNIqw9fU_T97nDO71UjLGqM5wDKwZpdzjzp7CuFheucC9wrCET3xUr3Ux0K5rpxOCnW8y3byvRTOXjh1Fqpa_aVv44Rvg52MJOURuJxX8uMwUs4Hk-iUCcHO6O5LhYXJEFNOXTGy5AVRIIyN55_xjcBc67QNJLAPbc9z_2_nrFE0H_gIAwFTNQ87_d8a-RheCJtVBTsNZJ0i_xs_vWz1HtK-JeVt8BnhlRdaX1Z2IgEQ6bMzVkTIadaxc5iAXipov4P1ZBsrtcPYVv7xKnZJttMEeax6_5lav0R_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a2d1b2945.mp4?token=GOGOzhuM3aCQUdwz7JZnDFh7fL-theHeBTpqaWj1Ghtgyu67-AslaNIqw9fU_T97nDO71UjLGqM5wDKwZpdzjzp7CuFheucC9wrCET3xUr3Ux0K5rpxOCnW8y3byvRTOXjh1Fqpa_aVv44Rvg52MJOURuJxX8uMwUs4Hk-iUCcHO6O5LhYXJEFNOXTGy5AVRIIyN55_xjcBc67QNJLAPbc9z_2_nrFE0H_gIAwFTNQ87_d8a-RheCJtVBTsNZJ0i_xs_vWz1HtK-JeVt8BnhlRdaX1Z2IgEQ6bMzVkTIadaxc5iAXipov4P1ZBsrtcPYVv7xKnZJttMEeax6_5lav0R_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴۸ شب میدان‌داری مرزنشینان آستارا در حمایت از انقلاب و رهبری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/452816" target="_blank">📅 23:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452815">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/605deef080.mp4?token=Ixnt8MwCEe1ECwO2-zzdyo5s5DJmlEUN1nv9Q82fykuwj-vQ15C1fHsTVF1Za8J7hoqYdPvJQWNJ4VQ2kD6KhlaP3YCN1ARc7cnxGN1rfk-FhJXJZCvPsk7R4vHaZDB1D5ezDu6F_oZSCZbfHu89iDzdUMjZBD8ugiG0VwdugLMFOj5hOsj-2VTt2yxRqUInmxoY7OnhqETkKA6f1V8_wBm2c_nDwijf3Io8fNVdfvK1UfvAnv3qjUSxExRiUmsMwHgFF5T_YLolSbTbV_umW1O2itBIwUzAkyCypmdSDpFXE2amZe3L1lSh6qOGCSb9aZgygpmZNdTMYMpP-sikb37HzOfe4rg7xmy4g9cLqscHQMv3Eo9Be1K2iY52JE8JOAiRwXJslyJt0_FPkNj0KlSgKsPEMndPq82bwah-RVJUJnS0nliqb5u1r-zAfgTxRHDW8dT2pUuriQkJrIAO-4ny8c-vUXTP7x4ZK3Bxu7ABneYtKSlhxHMvN2dWVlE2t0IZcLR5U3hSmpxLHW68DnXNGsZ3dusQjJXwQW_AnPLtcrYHh3zFvypTO2GsgqFaZxTESwi3t6PCYllnGCDYZRIjzqIGZI98QcpWguVaMONKVNsgL3mC1AXVf2xoq1vueG8cPI5gnso5odeumpMlZ83U4OUg8TIRmsYfarTMbxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/605deef080.mp4?token=Ixnt8MwCEe1ECwO2-zzdyo5s5DJmlEUN1nv9Q82fykuwj-vQ15C1fHsTVF1Za8J7hoqYdPvJQWNJ4VQ2kD6KhlaP3YCN1ARc7cnxGN1rfk-FhJXJZCvPsk7R4vHaZDB1D5ezDu6F_oZSCZbfHu89iDzdUMjZBD8ugiG0VwdugLMFOj5hOsj-2VTt2yxRqUInmxoY7OnhqETkKA6f1V8_wBm2c_nDwijf3Io8fNVdfvK1UfvAnv3qjUSxExRiUmsMwHgFF5T_YLolSbTbV_umW1O2itBIwUzAkyCypmdSDpFXE2amZe3L1lSh6qOGCSb9aZgygpmZNdTMYMpP-sikb37HzOfe4rg7xmy4g9cLqscHQMv3Eo9Be1K2iY52JE8JOAiRwXJslyJt0_FPkNj0KlSgKsPEMndPq82bwah-RVJUJnS0nliqb5u1r-zAfgTxRHDW8dT2pUuriQkJrIAO-4ny8c-vUXTP7x4ZK3Bxu7ABneYtKSlhxHMvN2dWVlE2t0IZcLR5U3hSmpxLHW68DnXNGsZ3dusQjJXwQW_AnPLtcrYHh3zFvypTO2GsgqFaZxTESwi3t6PCYllnGCDYZRIjzqIGZI98QcpWguVaMONKVNsgL3mC1AXVf2xoq1vueG8cPI5gnso5odeumpMlZ83U4OUg8TIRmsYfarTMbxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبض مقاومت مردم کاشمر در ۱۴۸ قرار شبانه همچنان می‌تپد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452815" target="_blank">📅 23:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452814">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0NIyqCO3hDzTa99vwHNaNz-dAF3E55dUTTv_ntnk_i0nRx4finJc23GL2MTMdudKQ-DFbkrPMiHMlm4DrYFishYhJRHemCvHJYXfiP5OixHCpwU_UXNmnDCifCPagwWhVLQiE7bHJn1y3EMfPO3ZAJ3reVTwEFXHN2JSnjUeeLkHCDxyQxxzqPgJ1LcFdbLNuEVqBOmOCrXw77EU7wDqmTeonCxYGt4mCual5f_jpxR9rgbfhSWct7CN82NR3c-JLtqyz4YuPEsU_alX3ud67gQk8rNXWwatqVZaTfDm3gb6SQOXjRcRtVNGZey1eLp5iecJ9Z1xCj3UlQx3cj3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت ما دفاع از ایران است
🔹
سخنگوی وزارت خارجه: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت برای ما دفاع از حاکمیت، تمامیت ارضی و حفاظت از مردم‌مان در برابر جنایت‌های جنگی است که آمریکا مرتکب می‌شود. @Farsna…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/452814" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452813">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cb366f32.mp4?token=Opgf4qsofHvgkc23Pieb7LlL1W4G7yQiJudccQwL377L9pb4GDuD9mV9MiOZjC4hucDVYMx1_AdW5AYBr4U4lmcqLLu8jeGnqjng_QJ9eUR0KhLez5fQZIkiv-cX3puXA3I0zliojJKmO8vya6OzQRIashcgxfRFugQKdJ22Z_dhkv9lGB2q7fcyBhXYMKyW93L34SpG-Xkfk25K-f-wglabaFCHYi6OAm8vj3mt_GukxnzfN6qqPbHA7wEuel_pfAlPq8Hj1G1ysBRQwBL07_6zpyHSLbnTfjmMCPbkaTbV-3kLoTOcMHWAxekoGVLAgXNM4UZlcadCDfeSP0LBeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cb366f32.mp4?token=Opgf4qsofHvgkc23Pieb7LlL1W4G7yQiJudccQwL377L9pb4GDuD9mV9MiOZjC4hucDVYMx1_AdW5AYBr4U4lmcqLLu8jeGnqjng_QJ9eUR0KhLez5fQZIkiv-cX3puXA3I0zliojJKmO8vya6OzQRIashcgxfRFugQKdJ22Z_dhkv9lGB2q7fcyBhXYMKyW93L34SpG-Xkfk25K-f-wglabaFCHYi6OAm8vj3mt_GukxnzfN6qqPbHA7wEuel_pfAlPq8Hj1G1ysBRQwBL07_6zpyHSLbnTfjmMCPbkaTbV-3kLoTOcMHWAxekoGVLAgXNM4UZlcadCDfeSP0LBeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: ۲۱۹ شرکت خصوصی به‌دلیل عدم رفع تعهدات ارزی ۲۳ میلیارد یورویی به مرجع قضایی معرفی شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452813" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452812">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVgXRfAjlR4KlGosbdSBUhKnlBeCg0OKZATMN_uXcSH567Z7m1e7ZJWBSfIq2Rn8ELmJN3Ujnt4VUi9pln9QhBm_SS_sYwUl5knN5kar2x-VyhWrJLwbYQ17lSXHVdKCbf-w9I1ZgIe-YqfD4bPH2x_M20sutPR4p_evuC6Kdnho1FteaYhVE5n_UlDJwTuhYE4c47B-TOmVFGnTLTYBh4sYiVCVim8tcAm_y57gdLA6VVpdY_xNaV_PlP4IXTwTwuaCiFSIdkIfjFVNFXKY-3nZItlHf-q6mrybUhluWw1Pg_6RCBKucjMeiFmKhoosR0A8OjpZ-kT4y9rbo8_mWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت ما دفاع از ایران است
🔹
سخنگوی وزارت خارجه: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت برای ما دفاع از حاکمیت، تمامیت ارضی و حفاظت از مردم‌مان در برابر جنایت‌های جنگی است که آمریکا مرتکب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452812" target="_blank">📅 23:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452811">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87101cb2e0.mp4?token=kc13o4qCeOD5cmcf-4C7g3STRmMyP5cVPvPYs6dNZ5VC9e-yOzLD_jTdk-qGcwtEjxe_F419aX4jwIQ_tX7LqpqIx9HfDfbOHq38vqiC_3TURz0SGREiUpLjx_GBEQTVeojmK0vsLArI4AR-WpRWwHg9um_-ASorHJSsMlRofZNutXMcNZYhuz-RDqDgBXuc9ESjnMz3vFzsHKtLx7dU7vjSERy0-njqH0gHAxXItJvS-sbZIrOX5eLFlo2umv2iucWovx_ZMzjGGN7OqbmWsmSZpqHQU8piwZGihpnPpigiW6ejBHQThUXXFbFgySRRreTlbol-BJR7R0Li8tNykJLRcYxuaLWSHh88D5kh_241bG6hu-h5Bs65fLgJpBdCNwLRDljkKRLfLEDIrry0iB06Zyf38-ZetecY5hTrwxfRGkNWotdSMaEXOCyOf8f9nZ7uvtANDeUXhmSXmsC7u09S_zdtdUEALxEku_qS97qWoOMB5vvCNRMDif0WZghledX5N6Q-nj4ki-HOCk4gY03TQl4iPOeyqn1Aq9Jzgv-uYINMrkKuY9zNjX4TyNjuxe5Oj-t1KtTCqCohjZbpld2fBPV3DwvGxDMD43d9-_WLYSthVm-Aa_ME3cLnZZ9vF6uk8xlL70NxjqU-z7GKtm1ekzN0TYpI2qKK0TlPwzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87101cb2e0.mp4?token=kc13o4qCeOD5cmcf-4C7g3STRmMyP5cVPvPYs6dNZ5VC9e-yOzLD_jTdk-qGcwtEjxe_F419aX4jwIQ_tX7LqpqIx9HfDfbOHq38vqiC_3TURz0SGREiUpLjx_GBEQTVeojmK0vsLArI4AR-WpRWwHg9um_-ASorHJSsMlRofZNutXMcNZYhuz-RDqDgBXuc9ESjnMz3vFzsHKtLx7dU7vjSERy0-njqH0gHAxXItJvS-sbZIrOX5eLFlo2umv2iucWovx_ZMzjGGN7OqbmWsmSZpqHQU8piwZGihpnPpigiW6ejBHQThUXXFbFgySRRreTlbol-BJR7R0Li8tNykJLRcYxuaLWSHh88D5kh_241bG6hu-h5Bs65fLgJpBdCNwLRDljkKRLfLEDIrry0iB06Zyf38-ZetecY5hTrwxfRGkNWotdSMaEXOCyOf8f9nZ7uvtANDeUXhmSXmsC7u09S_zdtdUEALxEku_qS97qWoOMB5vvCNRMDif0WZghledX5N6Q-nj4ki-HOCk4gY03TQl4iPOeyqn1Aq9Jzgv-uYINMrkKuY9zNjX4TyNjuxe5Oj-t1KtTCqCohjZbpld2fBPV3DwvGxDMD43d9-_WLYSthVm-Aa_ME3cLnZZ9vF6uk8xlL70NxjqU-z7GKtm1ekzN0TYpI2qKK0TlPwzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بندری‌ها ۱۴۸ شب همچنان در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452811" target="_blank">📅 22:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452810">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/847aab2d4f.mp4?token=lCR_nX8O78qZ9FTx44G-YfCS9d9DZio6WM9QTXFPbodDtvNsAhsoG5Cmne4vONzZbj2RGUfhxPdIbtxIc1JWvsFcmYbiEmctGbohNrU3AMIuONk6ucS7mr1ol77MTP3PQdJ1OWtD7ypqndHdMkT3RukQ3E1TrVzG72qgCGzRjwY3JWaUPGOIR49NzcQ3gYVMRSrnPWgPW-3LJXubzK6eiK6mlnGuDgAF5LOjA_zesxvd8tqFb0LfxLy6FfjI6C0emADPL_bOo1DQaDKfaQMwNs9gG6DVKlNwV1OZoES12hy7DQi0v6_6CMd7h_wAwcw45CDxOOWMYxNU-eK0M5hBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/847aab2d4f.mp4?token=lCR_nX8O78qZ9FTx44G-YfCS9d9DZio6WM9QTXFPbodDtvNsAhsoG5Cmne4vONzZbj2RGUfhxPdIbtxIc1JWvsFcmYbiEmctGbohNrU3AMIuONk6ucS7mr1ol77MTP3PQdJ1OWtD7ypqndHdMkT3RukQ3E1TrVzG72qgCGzRjwY3JWaUPGOIR49NzcQ3gYVMRSrnPWgPW-3LJXubzK6eiK6mlnGuDgAF5LOjA_zesxvd8tqFb0LfxLy6FfjI6C0emADPL_bOo1DQaDKfaQMwNs9gG6DVKlNwV1OZoES12hy7DQi0v6_6CMd7h_wAwcw45CDxOOWMYxNU-eK0M5hBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: برخی تراستی‌ها خیانت کردند
🔹
یک تراستی ۲۰۰ میلیون دلار از سرمایۀ کشور را برنگرداند و از کشور هم خارج شد. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452810" target="_blank">📅 22:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452809">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf60d3589.mp4?token=CjrN3EXrhulXmMOHXJe4U_pPnpeWEZ1WWR-NLxC_7ETGGM-YKrCeW4zuOuw-791yVXs7m8UO3Fy_kDJG8ucF7PZDStv8i-yFXkZnYRurHfhl-ytbIONKgxzeFnMVerbd4sZIVwjLBjoBeoSE8RAeQopPuEZfoVPThunVEq4J4HWwnMBe68tBPEzxkTR6MPobjuwAkBIS_JaTipfQU2pe7_WhUaYrSkGVrzeMmzszhoVFvbOSDHekNFgwYUH9V09ODyJOUtqVI87igLGiIwNeEmG_KO9n4pIw_GS0sl_0fr6nRPXMfSzsaollK_KuiOp9dX8-5lsdUndXOMZ3hZz9cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf60d3589.mp4?token=CjrN3EXrhulXmMOHXJe4U_pPnpeWEZ1WWR-NLxC_7ETGGM-YKrCeW4zuOuw-791yVXs7m8UO3Fy_kDJG8ucF7PZDStv8i-yFXkZnYRurHfhl-ytbIONKgxzeFnMVerbd4sZIVwjLBjoBeoSE8RAeQopPuEZfoVPThunVEq4J4HWwnMBe68tBPEzxkTR6MPobjuwAkBIS_JaTipfQU2pe7_WhUaYrSkGVrzeMmzszhoVFvbOSDHekNFgwYUH9V09ODyJOUtqVI87igLGiIwNeEmG_KO9n4pIw_GS0sl_0fr6nRPXMfSzsaollK_KuiOp9dX8-5lsdUndXOMZ3hZz9cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: بیش از ۲۰ هزار شخص حقیقی و حقوقی در مجموع دارای ۹۴ میلیارد یورو تعهدات ارزی رفع‌نشده هستند.  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452809" target="_blank">📅 22:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452807">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def8f2e12f.mp4?token=dxiqmcVjmt_RjHWWRm5m_3oKXxx8THw2bCj9gRZdF5ev52iizFLX7IWjkN6EOoDyN0d-cB44wB-jXmpT8q5U1smAKnrjP0n8RD0Vn5Jt3ggWCbRoYdv4PhTJcRzyJotIm7N8VRI2hs5xE212aGnGhmhmJ2yEu63irkyXd3f8FhnxekFVT7hybyoIRTI6_kt56e8O1j-lsWEvxh59UWRqbHGzHf9_RWwq1UaSTfQVM4T89c-1QtzDTsRl4GumF2OFLP9yZbQYCprwHKspclX2mm2A107K-q20q2G1Oj3n2vsvir8QSLvb6pg2tbwJg0uj5Uj2AcTpTwEZrZjFQ5VbgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def8f2e12f.mp4?token=dxiqmcVjmt_RjHWWRm5m_3oKXxx8THw2bCj9gRZdF5ev52iizFLX7IWjkN6EOoDyN0d-cB44wB-jXmpT8q5U1smAKnrjP0n8RD0Vn5Jt3ggWCbRoYdv4PhTJcRzyJotIm7N8VRI2hs5xE212aGnGhmhmJ2yEu63irkyXd3f8FhnxekFVT7hybyoIRTI6_kt56e8O1j-lsWEvxh59UWRqbHGzHf9_RWwq1UaSTfQVM4T89c-1QtzDTsRl4GumF2OFLP9yZbQYCprwHKspclX2mm2A107K-q20q2G1Oj3n2vsvir8QSLvb6pg2tbwJg0uj5Uj2AcTpTwEZrZjFQ5VbgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: بیش از ۲۰ هزار شخص حقیقی و حقوقی در مجموع دارای ۹۴ میلیارد یورو تعهدات ارزی رفع‌نشده هستند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452807" target="_blank">📅 22:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452799">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRJQZgQHZ40QQH1Flls6SAKsPSP3TD9q_TGZ7LAZMJkXCAl1abxmYacM7vQjW8JCnCcbgV061DW4pp90g8aoOJuzeVxMDZx4i_HQblAirQvLGQZXVvr0sOhO1nSej4ry2CixHsK5HkSwiGO4lCSaEz3xOm2QZiYZ9Jov2tg22AuHUrQGmN_eAWmVS_0NfvWCLXMglEN5Fn2CA6nPryZd_l52RrW9T0kpK4rpdT617LMlJBp3rBhk3oCs1YPyuJEFJg9wfLNBlxqVSOnq4kI_tME6iAW28TBsOQG_vFtKSFd1Jm_WRRfbRhb_Gd7KTj_MWcXxvZwu1xHq07QnPlAH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/su5Bblta4zMnBUWCn3aboS01OkEdTjv6Qr4A27DkqLVkg_8rNz4WNs9ze50ZK5UUJBCt9lVBNjOxA9Rj84Oy8gaj1jyUaHNCD_vHStUPhij5mO6uz3A1SHKHEQXj6JWMTndHYTycPSGxMQeuNuzYUgbTE2N52a9DSG55dLSgLEs5bpxRr6-V9HA1tcMioyV3DK6wThoKrYla11alkTzUk_JjBASyqYMB5mYbWDzBgAQ7uCDHgG6iV801s8U3qZI-BqgdgVM_l8zOO4BsX9ZvZuZWBY0MRj0LFWvPPO7gIaOPTFE_DPvsTQt0HbALZHwuP4n-QAjaUmuewdZWEJ4SOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIMB-PJKj6550zPvnsjrU_m_442XytWAfRK9qvvki9NR086a_kQzuB095FyZFmU-mnB0Tuzd68CtF2-ZyZ8_2ONQk4uB8Ou7RpP6jG36p9U6x0h7Tb2C-dP7iN7plnzajuPuv4Ixa4tEa76C3CgfKUyhAAFGSoiKf4w6PpTjccb67mVlyiRpKHeEF5REy5vRqNXW35EOqIVYxo95ph9p6isPDmLaAtesth41wuYiS4nuCn1vOGbeZGrlbITeo-XgDtUp-B21gQEBSxQ5wcwADPf9FGjIyLjG9x2Rf8T1qh-WWdRtQvBE08NGivuLkRC7fQzePI6oJFuyETxOsD4K7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uL9grupyuwhnNgMVrHF-aKSBXpP94ktp0TgtMZiIOvfsIYApSWUYwhjCOGNECPWRpx4LRQwz6oKe7J4ib_ONwWh0p_Fu3bZ_W5XHn-4rgwX0GuZgRoxY5mRnduZ9f78tKI1SO_xVUibqXVIB8f9MNsKDP2p2T-CnnEn7W6axG8rCUMvsAicEgRzbuB3FLn5vYW48YJFhIuGljeLC0TgT2xY4zDJcAKx7dEFBHNZaFvKeWAyvImUBiy5Mr72o_P3oYVaRTJgiDZNP7eoyAF6lyPta-nu5VfumbTDlRDjb_ykUDef-6F5eJ0lYNCykqVozudtCSV8lDb-aGU-5_-8yHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/enLoERWrs6GO_5roakQ0GENNFe_PYI4c31cENrrdaAaeJAuptik3v0MDynUQDgq3GV6AFvWDHnimO1n7nc2CwU5GlYA1_KHrLlOv7sAQzvVQksLdPS-8GmBBvNIhS76Fg4MrfBFgbCfKIFajS7_pie6arfPXaawEBt8JgiS7BLFtjEv4jl2qQ6_-YbtNsIQsFW6jOt0WzoR4oYQqMiQpXuo-nKUWHSnTXKeOMraoUGtS1supvjNgS5BmH6SH58oR7_nQHIjuuRZr0KeakZqOsbwOBh5BS-2NSTD-lv1y9fDEGUfVCecoHZdlw8g5oMJMRKe2wB4R0eWBF0tJlSA8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6ufPCTgS4WDHSP2Go9rDhJQCozPLXH2yvFpk4Qu5htwhwoMcy83lK4n8VDpMf2jLIak8-5Bx34U8QNHz3xb0f769p9gOwzj1WoloR-snGIorZkVuGh2X6BUx-63lhQglzD9Pi_opxogWUmcn3RP2Yjz-quGHLp5x-ChwDRw8xzK8_zWQMtFnBeORteL-m4ez31S83yyOL5Shnh8SQDcCy4E81A-ldjontmSdXvkuNh5hE1jL4hUy2D5Hu0dVm1-EPfOBYK9IVMmA9LutfJp9Dgh9nYghWTWDeVEcJq9zdO57BZv1zapGfAC07l0zsPFXzXUCkRakGWbibBxU3bXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMkHOsQqFOh-DkSVKV2spOAi2dZY7oHdVJpZfeS85yimv4EfmNP1Af_a1WEgGe-HzFpC3LF3GpqijEiVKGq06XspUaf0PHceX2PFd5ema3sKZTt8ZDUuTP0wGgvdm10751HYgoBBm60mL8pmQAi9VDr-p2A22-bststMZqSHkFxBB5EwGsxYuul60aT2yPDoJSVjihnHH3q9u7efs5LovgjDtpKnvg67spgcn3eUzM6BtOkN3y11ll2KTx7b_G8OB8VGRTfJS6At8ytZeP8TmTgKE_QZdbNujhvexnyPyNn6HkUqH6nKWmPaRpsC5NEKLbOABioG48fSXGOWHq2huQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تجلیل از پهلوانان زورخانه‌ای تهران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452799" target="_blank">📅 22:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452798">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe770a69f.mp4?token=DzfFDrZnyNoboQcwsQo_eHwVK5IPzRC5bJ-8EO77r8Q1BiK7rEvwd0iYeZ41CXgSrv_Q5cJC8JEjHdqPOPU8-1mWW24S5BggYvMNTffsLGKADRbXMqo9JaopUBQOcNxEqcweJ3OsbaCyeHUY6tr6BEkjFLaW4Fk8XMNf9BSNiDNd8OJMywhIi0ey3vo4pO6ajkO8S2moy5t1bs11gF8QYqLm-6JtTnyWE7UBZW0eIhHFinjejIMfUZoRkHv2eA1yOQp7TTuGhyk8FzCrg5Z_hFP1wAlqXipFF-ceafcjWZ8YiAMrlYcAxYCTwswqSZq1d-F50T1DRti-MgjFTQJ4FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe770a69f.mp4?token=DzfFDrZnyNoboQcwsQo_eHwVK5IPzRC5bJ-8EO77r8Q1BiK7rEvwd0iYeZ41CXgSrv_Q5cJC8JEjHdqPOPU8-1mWW24S5BggYvMNTffsLGKADRbXMqo9JaopUBQOcNxEqcweJ3OsbaCyeHUY6tr6BEkjFLaW4Fk8XMNf9BSNiDNd8OJMywhIi0ey3vo4pO6ajkO8S2moy5t1bs11gF8QYqLm-6JtTnyWE7UBZW0eIhHFinjejIMfUZoRkHv2eA1yOQp7TTuGhyk8FzCrg5Z_hFP1wAlqXipFF-ceafcjWZ8YiAMrlYcAxYCTwswqSZq1d-F50T1DRti-MgjFTQJ4FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بجنوردی‌ها امشب: لبیک یا خامنه‌ای لبیک یا حسین است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452798" target="_blank">📅 22:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452797">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4689a10913.mp4?token=Ag10z6Gp3lDMMA9kUWdm53rVIVknK1q7FLGlNxXQktjomy-zs6B_P0kEwXMr3Rtf809LyRzDmDfIs_fQhAgoA0mxzFHLzB1dLSmU0DL9lx1ERf3Pi8_JUlN91wua9EnnVPon3neTC-j-nfgTAsVIK48nymNOP6RD1hjnJoU3amrTL2Rp_4XFxyqc1tm2kdcQrquf1EZ-OcdDTNYZ1VsB0a6FKhnldbHAjMSQ45Yo1y2Gx9Ud80TfXMLv4_7AiUEKvMSmY1mvi0WHSnXQPmMYstNPB6A0yZcrHzaOL9XlkX1Op2QhzrP8o1i8g12_YARVc6Ftu05qASxoShvhnYGV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4689a10913.mp4?token=Ag10z6Gp3lDMMA9kUWdm53rVIVknK1q7FLGlNxXQktjomy-zs6B_P0kEwXMr3Rtf809LyRzDmDfIs_fQhAgoA0mxzFHLzB1dLSmU0DL9lx1ERf3Pi8_JUlN91wua9EnnVPon3neTC-j-nfgTAsVIK48nymNOP6RD1hjnJoU3amrTL2Rp_4XFxyqc1tm2kdcQrquf1EZ-OcdDTNYZ1VsB0a6FKhnldbHAjMSQ45Yo1y2Gx9Ud80TfXMLv4_7AiUEKvMSmY1mvi0WHSnXQPmMYstNPB6A0yZcrHzaOL9XlkX1Op2QhzrP8o1i8g12_YARVc6Ftu05qASxoShvhnYGV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ سقوط پهپاد ترکیه‌ای «بیرقدار» متعلق به نیروهای سعودی در یمن
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/452797" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452796">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf4462493.mp4?token=ACvL6Z1VGpFi3vl7rzEMXv7oGL6vkjC-LdSyw7DumtP1hdC-ht8jMweOybpMExffIqd-hqplkSlXCrmdgnYR7s2T5ZJH1sUP-0Nj6yFDfJ5YVnehoO6wlyqsw-UTvdGs_KdGRvDI13cQGgipsWJ_OVo2ZcYM7t0hsgoFk-CMkLzqeDb5C-2fgMHZE9uVSDl2_YoYkY4hUIlwX3rST2Jm7ebkQ3SaYNUq_5AdPbLqSfcXgku0iJe0HIBOws1Z601CgfU-00iF8WAAo5Lth7GWdLi9RQ__SoGjgOeFgcDOWnaRAaom9Uszc0hn_5ESbTTBRNqUr_yXhS752z2yecFUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf4462493.mp4?token=ACvL6Z1VGpFi3vl7rzEMXv7oGL6vkjC-LdSyw7DumtP1hdC-ht8jMweOybpMExffIqd-hqplkSlXCrmdgnYR7s2T5ZJH1sUP-0Nj6yFDfJ5YVnehoO6wlyqsw-UTvdGs_KdGRvDI13cQGgipsWJ_OVo2ZcYM7t0hsgoFk-CMkLzqeDb5C-2fgMHZE9uVSDl2_YoYkY4hUIlwX3rST2Jm7ebkQ3SaYNUq_5AdPbLqSfcXgku0iJe0HIBOws1Z601CgfU-00iF8WAAo5Lth7GWdLi9RQ__SoGjgOeFgcDOWnaRAaom9Uszc0hn_5ESbTTBRNqUr_yXhS752z2yecFUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد انتقام‌خواهی مردم بسطام استان سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452796" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452795">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJP8xZ7rSuD_SX_gtzkk3_3wVc_RxaOlZnZoGpEjxlcWap_sYISGzFucvUVP-4x8Z283I7v8ZOCwqy4Tbjk78PMRFR2aoEPbgqg9pWsBS1mX9ShbVL-DaAbeq4MNSIj_SnQoPyRjLbYwa2d0dZfqBgjoMC3X-0ZqS3Jb-n3LIA0kINOYMXsIyZeh3HDEgFsPj50s1K0_iU3L35F6vNufMuLxCLxpJUnXpI1lMKznZBtTYfWCmLrtHZ17YPXTPPGDEEpNiL4jbY9AuC-47J7gogu89_iDhl3zM05jAQ-aEmtFOm2aTLwQdNpukS0TAl7JxjTSfo6TtlPBk61-UV_cDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار رئیس سازمان بازرسی به متخلفان تعهدات ارزی
🔹
رئیس سازمان بازرسی: با کسانی که به تعهدات خود در موضوع بازگرداندن ارز عمل نمی‌کنند به‌شدت برخورد خواهد شد و دستگاه قضائی در این زمینه کوتاه نخواهد آمد.
🔹
تاکنون ۲۱۹ نفر برای بازنگرداندن ارز به دستگاه قضا معرفی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452795" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452794">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc9526c05.mp4?token=CPfqEyJtqr5qLy-zDF2uLv7pl_NrlTBPIMuWMrzLSuUjNECYI0OPzmaY5DPP75MFLDC1ZUwWhzC1pXkjXcmUGqV0o2b17uaxbgF_YhDhiJAKj0_FNUW9veSz2fKtaiw_ZqNqSoW622PSgDhO3ZSwDmNuMGizjXtlAZwI3D2fEWTDzGBTwJjKR2Ey9K8F3IVLNM_xd82uR2W0GGBV0kzQRJJeKmVo17Z6DcmmB6Kq4i-weWA9dUDB_eKB-p2H7ifTBYa9YnLDzquvBfnlkcgZjvsintXauhhxYnOpIrrEgipR19TuVsS6jYvTR_yCkHXjwKo-GX6cSUbui7y7sEISAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc9526c05.mp4?token=CPfqEyJtqr5qLy-zDF2uLv7pl_NrlTBPIMuWMrzLSuUjNECYI0OPzmaY5DPP75MFLDC1ZUwWhzC1pXkjXcmUGqV0o2b17uaxbgF_YhDhiJAKj0_FNUW9veSz2fKtaiw_ZqNqSoW622PSgDhO3ZSwDmNuMGizjXtlAZwI3D2fEWTDzGBTwJjKR2Ey9K8F3IVLNM_xd82uR2W0GGBV0kzQRJJeKmVo17Z6DcmmB6Kq4i-weWA9dUDB_eKB-p2H7ifTBYa9YnLDzquvBfnlkcgZjvsintXauhhxYnOpIrrEgipR19TuVsS6jYvTR_yCkHXjwKo-GX6cSUbui7y7sEISAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حواشی دیدار یک یوتیوبر با هوادارنش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/452794" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452793">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ac8177e97.mp4?token=p3E1P2dHgVZMajsLKpyDnjtHfxql3T48oMKlDI_aletzcn9w3SPkEi63mqJZ1atBUt4833apM_4cTxgYnQcIGiUBTm30lgglhBO3MOZ_zFY9_MZwPkFwb8N1X5WK6p-cr1coDLrEBB2VlCIeoMojhrnfXaakHlv3Ssn7wPVmEMicy9u1kY-2A2oP_HPLiOIHlNdjOiZloR6FwmjtfmM_KwG4ygxzvWb_6CKeY-EWWfw6zxJ5gEGmW6JcpkRcRRjxsh89iZXSPtiC_evWzlvrCSrI7aDgTpUDMAw4J7F1YzAXuJgf15rEj5g8gwt3axJY5zjLain4tVVoo2rSaeFBFCAzW6AcSfiauUZV-P3IbPGJskVQg20sqn3Bt8YSZ_gWpxv7rxjUe6qkfeC5algk4Xv5HDb4MpNzex-EoeiwCxV7x-P2XbCOd892sG3TXBfG_PH3oKxbk77KfbTzaGvLUxpWxr-7BRY9GkkbPiOAbnQzYbTx8bqtrsS-5_vRND65lgxv3C6WE6PXiZgrqJ0yIXSIw7jGnwplvUJgI1Wtk_A9-NLfldjJfp9CW3VOn8Q18RkL_hXgm3YtFKht0a3MabBk9hjFe6YxeAYRYLXZfSOhhDNSjTBRToaMwkRqOFsgA8xKzQXNP4y6qs_zXG3tjqnWn6qxl1kVXPLd8y4wjJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ac8177e97.mp4?token=p3E1P2dHgVZMajsLKpyDnjtHfxql3T48oMKlDI_aletzcn9w3SPkEi63mqJZ1atBUt4833apM_4cTxgYnQcIGiUBTm30lgglhBO3MOZ_zFY9_MZwPkFwb8N1X5WK6p-cr1coDLrEBB2VlCIeoMojhrnfXaakHlv3Ssn7wPVmEMicy9u1kY-2A2oP_HPLiOIHlNdjOiZloR6FwmjtfmM_KwG4ygxzvWb_6CKeY-EWWfw6zxJ5gEGmW6JcpkRcRRjxsh89iZXSPtiC_evWzlvrCSrI7aDgTpUDMAw4J7F1YzAXuJgf15rEj5g8gwt3axJY5zjLain4tVVoo2rSaeFBFCAzW6AcSfiauUZV-P3IbPGJskVQg20sqn3Bt8YSZ_gWpxv7rxjUe6qkfeC5algk4Xv5HDb4MpNzex-EoeiwCxV7x-P2XbCOd892sG3TXBfG_PH3oKxbk77KfbTzaGvLUxpWxr-7BRY9GkkbPiOAbnQzYbTx8bqtrsS-5_vRND65lgxv3C6WE6PXiZgrqJ0yIXSIw7jGnwplvUJgI1Wtk_A9-NLfldjJfp9CW3VOn8Q18RkL_hXgm3YtFKht0a3MabBk9hjFe6YxeAYRYLXZfSOhhDNSjTBRToaMwkRqOFsgA8xKzQXNP4y6qs_zXG3tjqnWn6qxl1kVXPLd8y4wjJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رایزنی عراقچی و لاوروف درباره حمله اوکراین به کشتی ایرانی
🔹
وزیر امور خارجه در گفت‌وگوی تلفنی با همتای روس اقدام اوکراین در حمله به شناور تجاری ایرانی را ماجراجویی خطرناک‌ و تعرض آشکار به اصول بنیادین منشور سازمان ملل خواند و گفت: «قاطعانه از امنیت و منافع…</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/452793" target="_blank">📅 22:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452786">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjNPvjUFHWvr-Am7sKi9Ruho1y-DCLaAX0nJf6p66mslX4MDCgDCWyv5_2T8vcJKp2xQCsBNUHsTXtwgrO9BgDjvoXujtGx1xUGZwJktYGV2PypNm1eTsmsxhWqP3dY_tuezjFRnqPiuajq1CULaz8gp2ksx26BAEFV0OuoyR5ljh2_-2gmI1N63JuItpFCPIXhyNDwMDSW_reCpjqDcMNceCN_5htLRkTrp3ae192VDIsIa-NvfFqPVyZDeyzT3VwMhl448kTAKtXt3N8uq4tuzK0gOiqkcv1icoaxDitHJU8EbZQtPUSpbZ7S4CCMfuRfIQen5M2lUbZX0QFf2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKo_XRnDYm59wu9NviqUPCe7wMiR37BAMRvi5bEJqDPq9Rid2HnhIahOCYgmRNnjaCraY7wfaUepL1i3A5N7psIg1ezLg__xPVrjpRpcxHyNlpf4ksqNssElMYa4z3jQYHf0CGOFZSx5XCH2y749PvJeyVWmyaFleN4axhBn67Gp5htZ3a0FLKp4G1qZ8JD1BuevgVTIV3XS1HfldfgYQGCVovRQrpmd-99nDAoz84nqRQ7TO2M6OcMkQ7lTuhD71hrsZqaRqA7cP7687NkV5IKCiqrfFEPFBrdEsv78Audd9roiFpALiGTramiUvNdZ0VlkNH9KwmdY3ePgX49LJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKWlzJwVGCEGd9HTeTmtSgEPvBdW1jfRu21R-mOGlBj4me9KGVdJcPc7qZ6iyUB-0zrZbC6tdQzB79yL2sXUDMNBMA6i2To2tnrawFYkdcj_hwJxQWMs25KIa3Ot-gsuoDyJ_RCBt9i4ZmOm0XTsb1nO_t2_LnIRvVc2WIFckyyJseaZ32ulj99zFsiXdsL5N2dllGcT73-pYxi2PWhI3tfSes_W-lAp-qNrz_DymjQklmWgbgPfH3k8hwuZgNvBv1HtYYCaEgIOxe4IHQAOxTObxxd-uqn_7rQ5DoYVozn1hDN1bPmXpkAwJUxIfP27YpusQS_Qd_ySCwOcqa1rVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikkwn570r-ZlbkiSFYIP60LkoH32eOI7pA1EWyUAo8wfty2HAYcfsiXS0dSHrI8-2k6rPwoMv_9aex2I5B5SfYewzY9PP70ta9h_GbIvHRePj1FQfQUhZ4VTXZYpRSwGVswmKMAOpqx3KYcBF784ERXf0eWLz_q7O7f30UgQNsDNutG6faV6whiKfftELLTvr25ZD6XQa8kIq_Z5puuVRZyZBDWQGtdUbm312ePPfSkVUBpFFyInQIE55wUxuZf9NBEYYOHiL78ZtXvq3MvY_Kc9Uc5UAb3veoTq8A9iwOMWnahhVcJfxdmjzUjn04vZU-_8Or1gNfmgVJhNt6-BRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6s81vaY8IINRxxO7TKx_CY7kQZy2QhABjHKMwuoAOQmQAgV_DbKD20mdh5KkqUteULF1JD0ZJaVgglAaa-5DM_n-2n7N1IQNp0vqnz9KSiw3ZB1bVJloeS8d1N-7YeWVjt6nOKlJWJEGoEEumlcG-TkryXj1x-oDhNkXpN4L7ZxW1Xkw69JTbqczbyVSc2sn5-2nMzMLtqfJbAvjnDC6JxLLHBlCBlhbWWDZl9bcG0SVbGYvZpKhgZpbt6onny2xKVVDW0PX7qDnD3c3jMd1xYdXSr88OO_5eWVd2r-9-p6PKq8fOBgbfEQTQCVuDpd5a09RY6kQIUORnrvkKmz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDei53wh85AiNhrY_breAD-QcnZoXLhdqhMExXF0wwaPR80_rFqLNhC-yTixeHp3j9qSv88_gqZpPDJf-bH9xxSWox8g1BjP4scMoOXFy6YAH_3Zz0vO3kjK8KI71ZTN0gCk86MtfjEv_vewbnOttwwumykvpmMR5A_O7ymkVzeDsnz1ElVYGCvyyU9hMa6s5LmUmno_Zy4vieLmHnR_UX7DAWe4n6ZN9HPx2tm1UV_1CWK64IyroVM3Czt6OLK5joO0PiR6eKmxZ6hkJDASP2JRbWyzNMC9fdCAevGMucKGPELcsxspj4blsbpKkkZPvHcoidASxN9Dfzi4fBMung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXQagv95EsaI6nGuKSvtK6ZqVaMZ2Ragbk-pDSMtnid1dC9hCVyAqmiACr7gdoNGY1jvLodncfVVcw50f1AOu3B5UpVaaXmqDTAwRm5m8-1d77MyypSmYkYKAd_0FyNyoY-vUzhYulW6TITSZjoLCPdsFKxrDkc7V2yg5cFgaJQd5hAlMIDuBwcMFutoOJBGu6nSloScxutil9M5VqUbBGnuIeGPZp0iP0Qym4z13u0C0_-VScxZ-5GkyN5vLZCFF9i05KcOY64Lh9pzTUqopI4ml9Qms6RYfbGjT6EsU3c6NQh-xya_7ZrPdwAmi0sC3EfuZecT4njDLMp_7jMYNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
ثبت جهانی دژی که قرن‌ها شکوه معماری ایران را روایت کرد
🔸
امروز در اجلاس جهانی یونسکو، قلعهٔ الموت و استحکامات وابسته به‌عنوان سی‌امین اثر ایران در فهرست میراث جهانی به‌ثبت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/452786" target="_blank">📅 22:14 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
