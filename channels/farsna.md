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
<img src="https://cdn4.telesco.pe/file/E51r2ihFDPB3LIor6PUirMpysPrcwBIoO_7sgc-jKRrXN7QHDOJP1usWsi_NZEAfSbMK5pSpjsDnZfJRvdtBZOrTWE3Vh6Koyn69Uu7VgrFLwoohDiFCAkANjEC5HHqGCe97a9tLs43eXKeGX4X_a87SPJFSlTTCBnsh6XGyNHfqXOSS9iRAb4AoLI-115utW2kXa75XFeEfHRlFldbUzn20S2IHflGBbpbzHcXL3XLT4KOHqH8zdP_dfLV7v51SdEvkBYKY91IK4CCQmZqBi71WjqAL71rHj175Y_qZQg2ojZabDSEpDNrYGqsH3irjPPKPfOQ8SZS5urNkxWFdMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-464753">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eff2052a.mp4?token=tGf2W9RxxELhMU-J0F-v3JbuGipZ0gC2Tw62Zr5w2AnBxf-A5_c9ozR2yW5TDkfV_a2lcpgbgs0Vggyy9gKsbitkarHAFcj40edo-4xfAE02Qb9TWNX2X6q0vC0X6J1VyKVtzHkr4hOuqdE6njSU0G7lLD3KwgSsIsp-CcV4FpzIG5-ZwtEgGrV873cfP5NScfpLcFKKnnuWk3GEuJNoiOAluMQZnU61iryDkYpTdw2xEaUrk9HTg06znR4N8S7v5vHbTuR2csvHrsxn0QCu647OJ8SZ324v9W4cI9aoBrsKcF1uvcE1e3EgvtwrGjE16PtFFmx5vH16aeIJNlNqPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eff2052a.mp4?token=tGf2W9RxxELhMU-J0F-v3JbuGipZ0gC2Tw62Zr5w2AnBxf-A5_c9ozR2yW5TDkfV_a2lcpgbgs0Vggyy9gKsbitkarHAFcj40edo-4xfAE02Qb9TWNX2X6q0vC0X6J1VyKVtzHkr4hOuqdE6njSU0G7lLD3KwgSsIsp-CcV4FpzIG5-ZwtEgGrV873cfP5NScfpLcFKKnnuWk3GEuJNoiOAluMQZnU61iryDkYpTdw2xEaUrk9HTg06znR4N8S7v5vHbTuR2csvHrsxn0QCu647OJ8SZ324v9W4cI9aoBrsKcF1uvcE1e3EgvtwrGjE16PtFFmx5vH16aeIJNlNqPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: به محض اینکه ایران تسلیم و جنگ تمام شود، قیمت نفت سقوط خواهد کرد!
@Farsna</div>
<div class="tg-footer">👁️ 999 · <a href="https://t.me/farsna/464753" target="_blank">📅 16:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464752">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌‎  خاموشی‌های شهر پرند با آغاز پاییز هم ادامه دارد
🔹
با وجود آغاز فصل پاییز و تأکید وزیر نیرو بر پایان خاموشی‌های برنامه‌ریزی‌شده، ساکنان شهر جدید پرند در استان تهران همچنان با قطعی مکرر برق، چه در قالب برنامه اعلام‌شده و چه بدون برنامه مواجه‌اند. @Farsna…</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/464752" target="_blank">📅 16:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIcB_ghjnViSRd9pGO5TZzMIUEIrw_vlC-ralMWJGRL2FoEHmi4Kea40ZdX2Lkto9v2tqxB-8V-hmZhlRldZKwE-sZYxVtd6aqS-1vo2cJClJv_FPepLTcSHdueBk8ZyKSUg9nSU9rS318nuC5kmfEg87KHbwHI_bsWLb6cEUk9shD8Oe1nBzhxN8vfl7XibEq_rAePGhsFc09aU2y2zEpBMMfaP_SHt31h8QD6atGv2_gBeLOP9Fp8C22U-xyDs6iui4BzMMys4DejVuBmHPsXHuWY3EHQ12Sl8ORz2zfIyu3h_VP1jm0cg8e9aweERrrQRMFm37_XjHHKAgdtErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس راهور: تردد خودروهای دارای پلاک مناطق آزاد کیش و قشم تا پایان آذر در سراسر کشور مجاز است
🔹
سردار تیمور حسینی: صاحبان خودروهای دارای پلاک سایر مناطق آزاد برای خروج از محدودهٔ مصوب باید با هماهنگی سازمان‌های مرتبط، مرخصی و پلاک گذر موقت دریافت کنند.…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/464751" target="_blank">📅 16:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464750">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOIxYKi47J0fIshXGnv_hB0rnE5-9K3rBRsoaI75D3GPgRBsnjHoWqJ3X1RkWvcBGKGxvDL5PQSjhLlD8kou9LIfw7j0rqsWUtn-pZqq-14d_QDBBgZ18T202HQ0Hu-pjNes5yQivhikRCkMEmnnQjzGHZ1D02momnZ0dOZpq6xn0ZQhJQJPHTmTCf259xYHYY1OfQKA0wDYFhko5hzPdRDEzm3sFuk3NJu6qxF6lZ7dteSI1lMD4LqlykgQFFsqSkgxEWG85tWvTH24tYuauAcnEuR3oD1N5HSnjXd2UvY0ffq0pJzNFsTfctG9reNlSjyZ4CovRIaN9FNbUVnS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: ۳ پهپاد و ده‌ها نیروی مزدوران سعودی را منهدم کردیم
🔹
مقام نظامی یمنی:‌ نیروهای دشمن سعودی که قصد انجام حمله در منطقه الوازعیه را داشتند را دفع کردیم.
🔹
در این عملیات ۳ پهپاد دشمن منهدم شد و ده‌ها کشته و زخمی در میان نیروهای دشمن سعودی به‌جا ماند. @Farsna</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/464750" target="_blank">📅 16:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464749">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un-VQh8O_aV3u3ax_8ICCSeKV9nVZWWv9rrHjuywurBWTN56Rnfk-Rh4Lqw2GtOp0W2x3ZH47QjyiEMmwp-mMxuv1sQFnC66_BWlpb2mQzN2GfIUnHeJvUO3f1Zb5lCFbXEMu-_z96NfMwlYBvg9tXTzXkrB9heUn9w33epjLPiq1SEfJxjEvAZDRlPknvlf4Iy4kns5d_JR6_KMLfLI49ZFLkhQbn0_cEbHbiGVbSz13CU7OJ6ZYBvsIfxocf1Da0aLXgvzCE8Y8uL6i9Kp-Z58_ctABBC44IzPfDkux-tvQa4wrPUBW7aTwK3n3jghqM3EptlRl7YQvRLAySV2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر صفوی: روند شکست‌های راهبردی آمریکا ادامه خواهد داشت
🔹
کنترل تنگۀ باب‌المندب توسط انصارالله هم یک گام دیگر در شکست بزرگتر آمریکا در منطقه خواهد بود و روند این شکست‌های راهبردی آمریکا ادامه خواهد داشت.
🔹
رئیس‌جمهور بی‌عقل آمریکا باید بداند که ایران شکست‌ناپذیر است و یک تمدن چند هزار ساله و یک ملت شجاع دارد.
🔹
آمریکایی‌ها رفتنی هستند و نمی‌توانند در منطقه بمانند؛ آنها صد‌ها میلیارد دلار هزینه کردند، اما شکست خوردند؛ این کشور در ترتیبات امنیتی منطقه نقشی ندارد و ایران ترتیبات امنیتی و آینده امنیت منطقه را رقم خواهد زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/464749" target="_blank">📅 16:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464748">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098ae7f6ba.mp4?token=KEHpMB5l40ownlFREpEFAlOFMKfqziqLWqF0M8V1NOhvTVTHZultmv9K9CaKdnq2kUvYiC7lF5ZaaH3kre3KcqwmBPJLC-OVm4-R_cuHBppx3Nk2hPuepGLKHo2GtvED8i4Qg7k2FH2-dSahhC725OzgSvXQ0gTlqhy9THO5zCcbwgRB1HMTkXJmr-yeNtNjh2NxMuDJSC1GKdUfB9mUxlWJj2r5vuspQfRNfxzsoTbL3GoX9hRpZwdDPybSEo3Y4pdwQGYeCdrEk8oYMVh3ldsLVBNZ9kkGkXy7Hp95e-jhFG2HP7DJxVv4_JqnPVv15fHQvGETbg_mJubqsCdLFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098ae7f6ba.mp4?token=KEHpMB5l40ownlFREpEFAlOFMKfqziqLWqF0M8V1NOhvTVTHZultmv9K9CaKdnq2kUvYiC7lF5ZaaH3kre3KcqwmBPJLC-OVm4-R_cuHBppx3Nk2hPuepGLKHo2GtvED8i4Qg7k2FH2-dSahhC725OzgSvXQ0gTlqhy9THO5zCcbwgRB1HMTkXJmr-yeNtNjh2NxMuDJSC1GKdUfB9mUxlWJj2r5vuspQfRNfxzsoTbL3GoX9hRpZwdDPybSEo3Y4pdwQGYeCdrEk8oYMVh3ldsLVBNZ9kkGkXy7Hp95e-jhFG2HP7DJxVv4_JqnPVv15fHQvGETbg_mJubqsCdLFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای فیلم جنجالی ورود اتباع به ایران چه بود
🔹
در روزهای اخیر انتشار ویدئویی با ادعای هجوم غیرقانونی تعداد زیادی از اتباع افغانستانی به مرزهای خراسان‌رضوی در فضای مجازی خبرساز شده است.
🔹
حالا مدیرکل اتباع این استان می‌گوید: «امکان تایید یا رد چنین ادعایی وجود ندارد و نمی‌توان دربارهٔ صحت آن نظری داد.
🔹
بررسی‌ها نشان می‌دهد در ماه‌های گذشته با وضعیت اقتصادی افغانستان، آمار ورود مهاجران غیرقانونی بیشتر شده اما حجم ورود مهاجران، آن‌قدر زیاد نبوده که در فیلم نشان می‌دهد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/464748" target="_blank">📅 15:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464747">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مهلت تعیین‌تکلیف وزرای ۲ وزارتخانه به پایان رسید
🔹
سخنگوی هیئت‌رئیسۀ مجلس: براساس اصل ۱۳۵ قانون اساسی، رئیس‌جمهور می‌تواند برای وزارتخانه‌های فاقد وزیر، حداکثر به مدت ۳ ماه سرپرست تعیین کند.
🔹
دولت از ۱۹ مردادماه با اذن رهبر انقلاب، ۴۵ روز فرصت داشت تا تکلیف وزارتخانه‌های اطلاعات و دفاع را مشخص کند.
🔹
این مهلت اکنون به پایان رسیده و دولت باید گزینه‌های پیشنهادی خود برای تصدی این دو وزارتخانه را به مجلس معرفی کند.
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/464747" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464746">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f1bcd111b.mp4?token=f6HHhb8Z_M9R4ett19H-Dq83zre89P7viPaZNBTmnRfL7ynoIVGRUPZhA9WSZmhf4s9viyLtkPLIFAhGJk1FjJcos2lKSIr6jtwr8GoVG6imvshsncdLypaV_3Cg5wW3AUXtM7xYYi3EmfB6uyvHjTJt7VNrxHtY1-zTGgx_2WRBTXTRF0-UAQM6ZYzB5Ew3OINMD63W3Gjgj0ERbPhmMLJ_4CGWu5EzWQtvrPH5YDtLGFXPtNUSX3MjoAMz5pZxUGP96jF3YIrpCH8slbMIoqyRcSW4KM5CR6Xscpph4OMBX6JKEH4j5aBxlUp5Skej5kubCKq89NpRpEYNtIAlDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f1bcd111b.mp4?token=f6HHhb8Z_M9R4ett19H-Dq83zre89P7viPaZNBTmnRfL7ynoIVGRUPZhA9WSZmhf4s9viyLtkPLIFAhGJk1FjJcos2lKSIr6jtwr8GoVG6imvshsncdLypaV_3Cg5wW3AUXtM7xYYi3EmfB6uyvHjTJt7VNrxHtY1-zTGgx_2WRBTXTRF0-UAQM6ZYzB5Ew3OINMD63W3Gjgj0ERbPhmMLJ_4CGWu5EzWQtvrPH5YDtLGFXPtNUSX3MjoAMz5pZxUGP96jF3YIrpCH8slbMIoqyRcSW4KM5CR6Xscpph4OMBX6JKEH4j5aBxlUp5Skej5kubCKq89NpRpEYNtIAlDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعی در دوی ۴۰۰ متر نقره گرفت
🔹
زهرا زارعی در فینال دوی ۴۰۰ متر دوومیدانی بازی‌های آسیایی ناگویا با ثبت رکورد ۵۲.۳۸ ثانیه در رتبه دوم قرار گرفت و به مدال نقره دست یافت. @Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/464746" target="_blank">📅 15:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZQI7TpRypBDRcBIJ_KvkSwObYgiv44aT4L6e6SHx2rAn3xwWwN2z9q5lpguvcq-2Z0ZKmsMy-1Y2eVLtkGzzgmRVzpigLfBfsaI5a4J4Igpqbr73DOAv2YbU2lqeGxy-FVyiSCywuXaoMvDoETHTNUfNg7kkaDUpvyn1KzDJ2uSZB8Y3ENpaAyjMCC2L8EpsUt9KJXTHUsvEVHNgsMMYst_sIZ0YCJu4w-vM_v5IL3la1JMqs3iYZIFazHO46-sSIDwJAK0SoDXi9o_otET78r5ff3gm2mqyF9Df28P68YmmA80SveE_vvsgvviGaFkK6eyMA8_CUqPW6Y7Hq0CDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور کابل‌ها از تنگه هرمز منوط به مجوز ایران می‌شود
🔹
نایب‌رئیس کمیسیون امنیت ملی: مادۀ ۱۰ طرح راهبردی تأمین امنیت هرمز به زیر و بستر دریایی، ازجمله عبور کابل‌ها و تجهیزات انتقال داده‌ها اختصاص دارد.
🔹
این ماده در یک کمیتۀ ویژه باحضور مسئولانی از وزارت اطلاعات،…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/464744" target="_blank">📅 15:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ada5d8dc1.mp4?token=FN5hxOl-tloJQF1qp7FC68H3Lxb7bKgJaRp8Mtu1I03VXEg4rxnOhjh6adj5WvIT6DZBdFTzbjbrvqL_Q4vYDIO4uBe8zj9tmRpS2Dvx4zzG03wiFjVrM7N7RufcsM2qdbRjR6dzEUTfeQs88aOYRDo-EWKv_LXB7JSIprXxpFvvSbyYbQfqJV1dMnI9N87qVkgJPpeGX3PgcThC__tDaze8Ww2gWP6m3xdPhbWdTEeM1djPXTsItZEZQJU7W6slPlXHXzC_DTQyKGVgYAL9KFKQBmU5P_ywm5iV1n9zwMv84gOruLpIryaeX3e2SwB3-xercjyjgdoAtPW614QWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ada5d8dc1.mp4?token=FN5hxOl-tloJQF1qp7FC68H3Lxb7bKgJaRp8Mtu1I03VXEg4rxnOhjh6adj5WvIT6DZBdFTzbjbrvqL_Q4vYDIO4uBe8zj9tmRpS2Dvx4zzG03wiFjVrM7N7RufcsM2qdbRjR6dzEUTfeQs88aOYRDo-EWKv_LXB7JSIprXxpFvvSbyYbQfqJV1dMnI9N87qVkgJPpeGX3PgcThC__tDaze8Ww2gWP6m3xdPhbWdTEeM1djPXTsItZEZQJU7W6slPlXHXzC_DTQyKGVgYAL9KFKQBmU5P_ywm5iV1n9zwMv84gOruLpIryaeX3e2SwB3-xercjyjgdoAtPW614QWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۷۰ درصد دریافت‌کنندگان پیوند سلول‌های بنیادی به‌طور کامل بهبود یافته‌اند
🔹
هم‌اکنون بین ۵۰ تا ۶۰ نفر در صف دریافت پیوند سلول‌های بنیادی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/464743" target="_blank">📅 15:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c38d61012.mp4?token=oRElhguQIA7pNpRrIyO7PHERFx3Zdq5HklSO_D_aPGCgD_A7bTBkWO1DuJAR-cJhLK_Xc2VuEGBIWM-pQX7iAsGg_TjS1WjwUR8YjKTWX18WCKPnEVhnECilc9U6OvNqnytZIXR2yuF70Un_8oNgaeMzb5KIEO6ifznJkx0LvkVR2eYUZzTiuJdcPUt2SSfS7fmOzhYiLUUrJBT3EDNZ6vYfBU_4yGO-aSHoOZvRELPDdo18EgCKROWb8yDoB1qvkFd_kfuTd_MdRIWeEPiJRmNqyw-Dp97fNmkRAbM6GN0WcOppBk4SkR0Zc7Yx6Q0dsR3gOysPQWcJ38cu--WwzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c38d61012.mp4?token=oRElhguQIA7pNpRrIyO7PHERFx3Zdq5HklSO_D_aPGCgD_A7bTBkWO1DuJAR-cJhLK_Xc2VuEGBIWM-pQX7iAsGg_TjS1WjwUR8YjKTWX18WCKPnEVhnECilc9U6OvNqnytZIXR2yuF70Un_8oNgaeMzb5KIEO6ifznJkx0LvkVR2eYUZzTiuJdcPUt2SSfS7fmOzhYiLUUrJBT3EDNZ6vYfBU_4yGO-aSHoOZvRELPDdo18EgCKROWb8yDoB1qvkFd_kfuTd_MdRIWeEPiJRmNqyw-Dp97fNmkRAbM6GN0WcOppBk4SkR0Zc7Yx6Q0dsR3gOysPQWcJ38cu--WwzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم آمریکا از اوضاع زندگی‌شان بعداز گران‌شدن سوخت می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/464742" target="_blank">📅 15:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxLrMvET5AetMugRdEe24_nTHYNTQcUcY2Ab4wJXQSWp5-iuy3grhMYb3yHerZvk7mcfqIzJTJvKGghSllsRUKRocQ-5gDQ-QVZBZz30ezPa3hFnAA4Qqlwfv6trG2mGhO2sov3J9pxh-kltNVAdguqZiAEa7ue6VJxOHFL14M7N_BEn8SOIP-F82g5dNqkr9HqjTMPJI-9eFh2BMi0V5tLxzx0QzAwo-A-9c81DYvci7MpjyCXOMkpXrhJ7sxWgRFIx2F1WiD-od4_oz0BknbPOfQ1_XmwCUXql5fLm4_WVLpDYbVyrRhBKQATVJz-1Cu0fZ7ScVl9vOWK-cOazpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
مسیر شتابدهی استارتاپ‌ها در ویستا آغاز شد
🔸
هلدینگ سرمایه‌گذاری ویستا، در ادامه توسعه فعالیت‌های خود در اکوسیستم نوآوری و سرمایه‌گذاری خطرپذیر شرکتی، بخش شتابدهی استارتاپ‌ها را به خدمات خود اضافه کرد.
🔸
ویستا که از سال ۱۳۹۶ در حوزه سرمایه‌گذاری در کسب‌وکارهای نوآور فعالیت می‌کند، با راه‌اندازی این بخش، امکان همراهی با تیم‌ها و استارتاپ‌ها از مراحل ابتدایی توسعه کسب‌وکار تا ورود به بازار و رشد را فراهم کرده است.
🔸
در این مسیر، حمایت از استارتاپ‌ها تنها به تأمین مالی محدود نیست و در قالب «پول هوشمند»، مشاوره تخصصی، شبکه ارتباطی، منابع عملیاتی و ظرفیت‌های مرتبط با ایرانسل نیز در اختیار کسب‌وکارهای منتخب قرار می‌گیرد.
🔸
تیم‌ها و استارتاپ‌های نوآور می‌توانند با مراجعه به بخش شتابدهی
وب‌سایت ویستا
، اطلاعات خود را ثبت کرده و برای ورود به فرایند ارزیابی و جلسات هدایت‌گری (Mentoring) درخواست دهند.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/464741" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464740">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمنطقه‌فرهنگی‌وگردشگری‌عباس‌آباد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE74KMA1aJdSib1QAFgprX-GNq2uaS9tWgQj2nOfMXa_MvH7BZR-8ZdZ5m4Hx8FI6JIg7Yej-OmNKLugH4DFwsmTgXvJvqC2gCEvdJF0re9r4C_Y0S2hPEQ9ADgEf6tVRvoeQmEXcCWafkRVeJAYH3XL0D1PuFppPpf_3LyaKkwJwU4vgiXtmBmA8FTHeTFvHMwpogKmEnZkHUPmjg3RH89NKav4tIq9xkcwrZsYCSwLlcLkhTWqqh51AZ1ZKdtoQV9FUvorXOsnqaqnKYTpv7QgiLgHkddfNeB_txFsfsBWLQ5v3EkKAUFwI3tXps3_xufpmBSQn70Ev6fvXO5Mew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
فراخوان نخستین مسابقه بین‌المللی نقاشی «سورنا»
با موضوع «ایران از نگاه کودکان»
🪅
کودکان و نوجوانان ۶ تا ۱۸ سال می‌توانند با موضوعاتی مانند فرهنگ و خانواده، خاطره، رویا، امید، دوستی، صلح و آینده ایران در این مسابقه شرکت کنند.
🗓️
مهلت ارسال آثار: ۲۲ مهر ۱۴۰۵
🏆
معرفی برگزیدگان: ۲۹ مهر ۱۴۰۵
🎭
تکنیک خلق آثار آزاد است و در بخش نوجوانان، امکان ارائه آثار مبتنی بر واقعیت افزوده (AI) نیز فراهم شده است.
📌
ارسال آثار و اطلاعات بیشتر:
sorena-competition.com
🆔
@abasabadecopark</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/464740" target="_blank">📅 15:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464739">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/464739" target="_blank">📅 15:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464738">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c25457b08.mp4?token=DT8qPc83qa_QuNw1LCjR8g5kJxnjt0l3k3y-xaAsCFqFZ3FXL7W9tLPmeYBFN535AkbqjyOUp9b5Z6LXxQvpueFEULSUT6KYJKWBJO5nVR24ga6zEDDZuU6XCXo-dxtbKIYkQ2xqcrIUQihG3C3IhdaOs3G43hvjUo-Lb8EIxvYW7vJYrUsQQlreXUQHuS-1oy9MoqfCpjfL2BmELBP6Txt4WzdmtmbE55lihi_5rujGBtRE9Pkx71EEv4eSvQCvn2F0kpto6BYe2WM8iDAz6mUL_Xysrv1sbryqCa05_59uD1sDvQF6dQI9WhaHgv9inYKZc9FjO0OpgW5H5T-USA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c25457b08.mp4?token=DT8qPc83qa_QuNw1LCjR8g5kJxnjt0l3k3y-xaAsCFqFZ3FXL7W9tLPmeYBFN535AkbqjyOUp9b5Z6LXxQvpueFEULSUT6KYJKWBJO5nVR24ga6zEDDZuU6XCXo-dxtbKIYkQ2xqcrIUQihG3C3IhdaOs3G43hvjUo-Lb8EIxvYW7vJYrUsQQlreXUQHuS-1oy9MoqfCpjfL2BmELBP6Txt4WzdmtmbE55lihi_5rujGBtRE9Pkx71EEv4eSvQCvn2F0kpto6BYe2WM8iDAz6mUL_Xysrv1sbryqCa05_59uD1sDvQF6dQI9WhaHgv9inYKZc9FjO0OpgW5H5T-USA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلنسکی بالاخره از غرب ناامید شد؟
🔹
رئیس‌جمهور اوکراین که از ابتدای جنگ اوکراین از آمریکا و اروپا کمک خواسته، امروز پیامی تازه درباره جنگ با روسیه منتشر کرد و این بار از چین، هند، برزیل و کشورهای «جنوب جهانی» کمک خواست.
🔹
به روایت ولودیمیر زلنسکی، «طی هفته گذشته، روس‌ها بیش از ۲۲۰۰ پهپاد تهاجمی و همچنین حدود ۱۶۵۰ بمب و ۳۸ موشک از انواع مختلف به سوی اوکراین شلیک کردند که بخش قابل‌توجهی از آن‌ها موشک‌های بالستیک بودند. متأسفانه دیشب نیز در پی حملات روسیه، شماری از افراد جان باختند.»
🔹
زلنسکی گفت: «ما به‌طور مداوم با اروپایی‌ها، آمریکا، کانادا، ژاپن، استرالیا و سایر شرکا برای تقویت توان دفاعی و پیشبرد دیپلماسی واقعی همکاری می‌کنیم. اما متأسفانه، آنچه جای خالی‌ آن احساس می‌شود، اتخاذ موضعی قاطع و پایدار از سوی چین، هند، برزیل، آفریقای جنوبی، کشورهای گروه ۲۰ و "جنوب جهانی" است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/464738" target="_blank">📅 15:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464737">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d71131b6.mp4?token=WOADt8qPF3ZjSNk2yxZwLGM9LR3nsIZbkFjGNjlB3TnSQOkd3p7HxTepahwtj7R2GsW5vRb7Yq8SfTW318nyxt6ytfuXZtiI44XftpY4Rbg5WcVhtDUhXt1iyRv-Tcw788Xf_BJtjPlaB0ZKBQzy1wXo_fSSefM0gTua6_Hl8oRiljTOKepQQL0pgM1q2-DyMzCDseqPGegjQx90vBOgrAwTqKC2Y4EdigFUhCx4uXyFUgmoTdTQeteBtUQUqWjnF7DFjf07kg8zDMFbiToxrXyGDsG-yBb-bJ-U_u356p4twl-O8uuNF-s5CDhikj-wQV5h_bBCIvIOXeJvbmWO9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d71131b6.mp4?token=WOADt8qPF3ZjSNk2yxZwLGM9LR3nsIZbkFjGNjlB3TnSQOkd3p7HxTepahwtj7R2GsW5vRb7Yq8SfTW318nyxt6ytfuXZtiI44XftpY4Rbg5WcVhtDUhXt1iyRv-Tcw788Xf_BJtjPlaB0ZKBQzy1wXo_fSSefM0gTua6_Hl8oRiljTOKepQQL0pgM1q2-DyMzCDseqPGegjQx90vBOgrAwTqKC2Y4EdigFUhCx4uXyFUgmoTdTQeteBtUQUqWjnF7DFjf07kg8zDMFbiToxrXyGDsG-yBb-bJ-U_u356p4twl-O8uuNF-s5CDhikj-wQV5h_bBCIvIOXeJvbmWO9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه: اگر تنگۀ هرمز متعلق به آمریکاست، پس ناوهایشان کجاست؟
🔹
معاون سیاسی نیروی دریایی سپاه: اگر ترامپ تنگۀ هرمز را تنگه خود می‌داند، پس چرا ناوها و شناورهایش اینجا نیستند؟
🔹
اگر آمریکا مدعی کنترل تنگۀ هرمز است، فقط یکی از ناوهای خود را به این…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/464737" target="_blank">📅 15:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d03fc573.mp4?token=CPfRYaD0fiJIoiudfCise3J_VVMblwEuGibS79iVuLGQ58NJ7XBz8P3Gnfvyabq0onbFM9FfbshsDGgjVvw_3FAK9fNHSJ0RZKIAwiCJIOa71UKrTjmdX8t0CtD4zBayiAKNxHUJW9tN2sx7ywIgXDMO84615qHhCB9b-2qodZKYXjyl8l8iRvInF95rGHCLwxAB7FBn9v9MPqbbT-4mwCfmiV6_g6xuPZOnvWkWEmOPd7hkfwPtuGZyL5KiITmgtSzmAs9LLTOvmNnNCDrZQaYcdx7ig6Iw1qemdWypt2vEuBe3giXQ-HCOhK8XE7tgc_cW4PfCWdrxB-QcNbAvlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d03fc573.mp4?token=CPfRYaD0fiJIoiudfCise3J_VVMblwEuGibS79iVuLGQ58NJ7XBz8P3Gnfvyabq0onbFM9FfbshsDGgjVvw_3FAK9fNHSJ0RZKIAwiCJIOa71UKrTjmdX8t0CtD4zBayiAKNxHUJW9tN2sx7ywIgXDMO84615qHhCB9b-2qodZKYXjyl8l8iRvInF95rGHCLwxAB7FBn9v9MPqbbT-4mwCfmiV6_g6xuPZOnvWkWEmOPd7hkfwPtuGZyL5KiITmgtSzmAs9LLTOvmNnNCDrZQaYcdx7ig6Iw1qemdWypt2vEuBe3giXQ-HCOhK8XE7tgc_cW4PfCWdrxB-QcNbAvlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران یک میلیون اثر تاریخی دارد؛ آمریکا چند اثر تاریخی دارد؟
🔹
آن‌وقت آنها می‌خواهند ما را با این سابقهٔ تمدنی و آثار تاریخی که ریشه در تمدن دنیا دارد، محو کنند.
🔹
ما این تاریخ را دوباره خواهیم ساخت و با سربلندی از این بحران‌ها خارج خواهیم شد.
@Farsna</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/464736" target="_blank">📅 15:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f5c577e62.mp4?token=hnxbHnos4HxWbyRzOHXcHAzrMFZ1BGBHrJE8acjI8nD9CbRjIzGPZWxDJhzYAlF7g3W1vmqWR7VEtlKUEADGzQhd4JxXEW2s30mnq5H7kJGMA-XASPjhwA5kxBZGfh_VPBm4cH6uLgbEhrRr2tf9Kbf10Qo0KowHr7IeadAVx9ToHDKE7R1bacXnjBoJb7-ZOzIgtSCC6NbAIaqvnOGuV4Slh78zPVKr5n5rGWt1DcITvPwsZIG2vmMADN3KOAKVrwLLGpKGgA9tTrMWYQPuf-g1lNC_4v5l271B6XieV6vdOIwsNcit1nSn5vqmOQSgyvkXiDxHISphFXFgMVV4uRkg_c1nTnq-9Xz0wm48NoDw-3kasOqyoT6uAGZMW3JfGf5tmVKtFdtsaVyFSbGbQadSMTeQFAJoMxHgsCkqo6yN-Q1DJeLwn0AKFq8oyPnZK-E1tADYocR7-gcq0_vj-Aw6UCc5XxAKNgr9R44gTRvxOVKajgFwT3RVUCcnniK6JCQRqw-38JTbQQBI8Pch6BPeAFilG3_X6scupRcV4sg_gwwpOXMD6P19VSq0JsX1YV70vqE0zvKjOYOIahXmGM-MwWtm11K-PKTSchPLggemJdaatS2U4Qz0Tb3uQ9HCA7MgsdNawaLcPhEunJhAcGUIhHVb6oX1hxnB7DvjcDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f5c577e62.mp4?token=hnxbHnos4HxWbyRzOHXcHAzrMFZ1BGBHrJE8acjI8nD9CbRjIzGPZWxDJhzYAlF7g3W1vmqWR7VEtlKUEADGzQhd4JxXEW2s30mnq5H7kJGMA-XASPjhwA5kxBZGfh_VPBm4cH6uLgbEhrRr2tf9Kbf10Qo0KowHr7IeadAVx9ToHDKE7R1bacXnjBoJb7-ZOzIgtSCC6NbAIaqvnOGuV4Slh78zPVKr5n5rGWt1DcITvPwsZIG2vmMADN3KOAKVrwLLGpKGgA9tTrMWYQPuf-g1lNC_4v5l271B6XieV6vdOIwsNcit1nSn5vqmOQSgyvkXiDxHISphFXFgMVV4uRkg_c1nTnq-9Xz0wm48NoDw-3kasOqyoT6uAGZMW3JfGf5tmVKtFdtsaVyFSbGbQadSMTeQFAJoMxHgsCkqo6yN-Q1DJeLwn0AKFq8oyPnZK-E1tADYocR7-gcq0_vj-Aw6UCc5XxAKNgr9R44gTRvxOVKajgFwT3RVUCcnniK6JCQRqw-38JTbQQBI8Pch6BPeAFilG3_X6scupRcV4sg_gwwpOXMD6P19VSq0JsX1YV70vqE0zvKjOYOIahXmGM-MwWtm11K-PKTSchPLggemJdaatS2U4Qz0Tb3uQ9HCA7MgsdNawaLcPhEunJhAcGUIhHVb6oX1hxnB7DvjcDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۱۰ شب از حماسهٔ ملت ایران می‌گذرد
@Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/464735" target="_blank">📅 14:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464733">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3wbeOMPJ8pHT1odIjyVcrH24Q7c_kVHMrTUzjxzyo6o4OphWP6W8DzyghS0BmNtAAGBNx9MMf1alLT716JY-gXB1RGv55TseSdq28fh3sgg6HuE_8vU6iiOfV1TsePoCDnIEGivAMxrD7i7uXI9x6PFyxzDaQqjmxUaGq0z3wD78xAHzeaqBb8Y7jodhrD0qarcwGVfpTn8comTKeYaaAgfXqmiCwWZ2rUDGB9sOs265uwIiIO8pl1OoVt0ee_f4dmOnypCPRaHbW1TCoQTctSDFqrlVrLzL2HkIfvocmcv9RUuRSChIAc6zOcDf8qaw9tv7BZec9hICN4yPq48wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7089848316.mp4?token=TWLi57L3uuDBB_CVFEeAvc94t6Xb1qrhQfkOUYH-pxGYS11svKADe2FO9pru9Yz0E6ZjXs9GHK7TwT5o6upnaefGimuclQZAdxlXDf236O4EoCemGQPe5VmV8tQ_JnG_8v8AN43mvVwmD2qn86xDVVvETk5NDncy_KL9ZWKw7sW7HmFt-5r3LyjKo_0xT_76llbgXApx7cj4DToAlY4Q8P8n3GCU8WkS_iWvWS-CZkyUzr973sX7oM-2_Sc2V6h0r0VWdyebi0lExSYeBQuM5Uy6TvEXaMMiVw1lRh8RnADwZIn2ZS5M34wSxbAJBk5T3saHeYB2BrGZG28eR0xueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7089848316.mp4?token=TWLi57L3uuDBB_CVFEeAvc94t6Xb1qrhQfkOUYH-pxGYS11svKADe2FO9pru9Yz0E6ZjXs9GHK7TwT5o6upnaefGimuclQZAdxlXDf236O4EoCemGQPe5VmV8tQ_JnG_8v8AN43mvVwmD2qn86xDVVvETk5NDncy_KL9ZWKw7sW7HmFt-5r3LyjKo_0xT_76llbgXApx7cj4DToAlY4Q8P8n3GCU8WkS_iWvWS-CZkyUzr973sX7oM-2_Sc2V6h0r0VWdyebi0lExSYeBQuM5Uy6TvEXaMMiVw1lRh8RnADwZIn2ZS5M34wSxbAJBk5T3saHeYB2BrGZG28eR0xueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژیم صهیونیستی شهرهای المنصوری و حداثا در جنوب لبنان را هدف حملات هوایی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/464733" target="_blank">📅 14:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464732">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433e887041.mp4?token=PDOcL4byf5bi9ZxrDnJ6acE4AI_S6POd39vGTozCDLEO8VL0WBOyH2tc8h2X3Q5EHoQ1yVfig8pG_PlCSZtjydekqFpoaRlno3XpAJDtZ1m5YshoEyOeG_PJWORU8Our4gUoQmu2uzxbtzRHE30cvHGj3GxBIH-O6hyTeEFbM0UNUOo2kqJGytKuzBjiS8rw7scMOqOZ4VZK2fTPd4Ojb4reElVRtDxVskI4ROvOsGGsiKF14LvefP-GGs-dUeV0myQ-yF_XZphbKZh9kXyr-AWdEcIR_THl81_VtDFHH6kTb6ac2V8CE2029YUVU95tg2YvaMe4GVQSA4ScKbOWyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433e887041.mp4?token=PDOcL4byf5bi9ZxrDnJ6acE4AI_S6POd39vGTozCDLEO8VL0WBOyH2tc8h2X3Q5EHoQ1yVfig8pG_PlCSZtjydekqFpoaRlno3XpAJDtZ1m5YshoEyOeG_PJWORU8Our4gUoQmu2uzxbtzRHE30cvHGj3GxBIH-O6hyTeEFbM0UNUOo2kqJGytKuzBjiS8rw7scMOqOZ4VZK2fTPd4Ojb4reElVRtDxVskI4ROvOsGGsiKF14LvefP-GGs-dUeV0myQ-yF_XZphbKZh9kXyr-AWdEcIR_THl81_VtDFHH6kTb6ac2V8CE2029YUVU95tg2YvaMe4GVQSA4ScKbOWyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: ایران از شروط هفتگانهٔ خود برای بازگشایی تنگهٔ هرمز، عقب‌نشینی نخواهد کرد.
🔹
هنوز از طرف میانجی‌ها چیزی به ما منتقل نشده و حرف‌های ضدونقیض از سمت رئیس‌‌جمهور آمریکا زیاد شنیده می‌شود.
🔹
ما منتظر هستیم تا نظرات قطعی توسط واسطه‌ها به ما منتقل شود و…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/464732" target="_blank">📅 14:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464731">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6fcbae90.mp4?token=TAXDTXOGilwBOLWwixStXVajGPoqH4Nx1QhvgklKbp8dyPmbYGYtaJGUvVEyCHlx_vZ9gcj9Ff5ghgkBKcIyUwexlfPsolkUlo3mTFIBw7AbqojMU9UlAYjBJHGT8AQ8Dk_Q-yfg5aE-hxAG60JcshxyIBWlKt2dOP5lT7dWZ0-WtWkwFAFIJRu1K2iq_505VY6eQhndgfL7321Z-jOtpnQBYGjwKgF9Y46D66yuvhb8NCvqHqbGWblskRe0ixm0RHsEx3qB1oZ2pSYGW1scTnC6bx-jf4VRhiWacmoPbP_IXvEAq1Kzfwq1wBFNwQQQutpNiKIQI1gtDV23mGT_nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6fcbae90.mp4?token=TAXDTXOGilwBOLWwixStXVajGPoqH4Nx1QhvgklKbp8dyPmbYGYtaJGUvVEyCHlx_vZ9gcj9Ff5ghgkBKcIyUwexlfPsolkUlo3mTFIBw7AbqojMU9UlAYjBJHGT8AQ8Dk_Q-yfg5aE-hxAG60JcshxyIBWlKt2dOP5lT7dWZ0-WtWkwFAFIJRu1K2iq_505VY6eQhndgfL7321Z-jOtpnQBYGjwKgF9Y46D66yuvhb8NCvqHqbGWblskRe0ixm0RHsEx3qB1oZ2pSYGW1scTnC6bx-jf4VRhiWacmoPbP_IXvEAq1Kzfwq1wBFNwQQQutpNiKIQI1gtDV23mGT_nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منبع نزدیک به تیم مذاکره‌کننده: ایران منافع خود را تحت فشار واگذار نمی‌کند
🔹
رئیس‌جمهور آمریکا اخیرا گفت که پیشنهاد توافق ایران را رد کرده است؛ حالا یک منبع آگاه نزدیک به تیم مذاکره‌کننده در این‌باره به فارس گفت که پیشنهاد اخیر ایران دربرگیرندهٔ مجموعه‌ای…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/464731" target="_blank">📅 14:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464730">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4fa82c1f.mp4?token=YB_iCUJRXgdJ3Y-PF_P-vJCd1cZdKZtr2yuAr6J_QuUQ7trN412jMqzfzHOybpxDwaz15TvdlM_ZHBVoWFbs1Lc47HZ3TdnXJuLlb9ltaPXiACx3kd-I7V803qIY2yd6XASgzPqjzNHkif5hg2kMOFWnmhE-L390upvRMli8WfjVEGcM9hrcTk-TM0vQtsR0MZsJ5EYtnOBz0t2pLs0ko8qbzlG0AJxDbFLzpYLkdwiy5Ln3kPrYrIGr5a4uKVddDVUOJ0A2pWxiXVmCVbyQ7tEFGZ8_BdvF_-CvJmB-PLCUTL5OwoLo18M5HQCkGOM5Ri3F_1Nm8BUJ8ZstexNdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4fa82c1f.mp4?token=YB_iCUJRXgdJ3Y-PF_P-vJCd1cZdKZtr2yuAr6J_QuUQ7trN412jMqzfzHOybpxDwaz15TvdlM_ZHBVoWFbs1Lc47HZ3TdnXJuLlb9ltaPXiACx3kd-I7V803qIY2yd6XASgzPqjzNHkif5hg2kMOFWnmhE-L390upvRMli8WfjVEGcM9hrcTk-TM0vQtsR0MZsJ5EYtnOBz0t2pLs0ko8qbzlG0AJxDbFLzpYLkdwiy5Ln3kPrYrIGr5a4uKVddDVUOJ0A2pWxiXVmCVbyQ7tEFGZ8_BdvF_-CvJmB-PLCUTL5OwoLo18M5HQCkGOM5Ri3F_1Nm8BUJ8ZstexNdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم ایران در دانشگاه تهران توسط وزیر علوم به اهتزاز درآمد  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/464730" target="_blank">📅 14:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464728">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بازداشت ۲۱ نفر و کشف مشروبات الکلی در یک کافۀ یزد
🔹
دادستان عمومی یزد: از یک کافه در یزد مقادیری مشروبات الکلی کشف شد؛ همچنین درپی تست الکل از ۱۰۰ نفر حاضر در کافه، نتیجهٔ ۲۱ نفرشان مثبت شده و این افراد دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/464728" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464727">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43abd7048.mp4?token=LVrB1UA5_gMo5tU7gUB4y-0RKz9_48tCZ8PLGqO8s0rb9x8kBLzqMsff-y_5aW_UzqkbQL1_dfDjy1BsA_Axx4NZcEI14Gh09i3cLwx0snUlSslBN3NpYZfAQwHw-oQadHeNl2pCipofOcLhm6YMRAJIoqI3PNc2Jh1CIXbx0r7jtNwfNkIrIfSqs7R0zbzmx_FNr2t3ctrgA_MwO52LZLde6Tuc05TFr9o4J7mmAepme_UahvQvcBoxRUZQDlYtN1zklJG2etuXRSZI501vvDqxJiworay8G8k_lVlVaDA_H_LjlLkGlMyUrfB_OWyR_iJmOWsRGudseCodZsV5ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43abd7048.mp4?token=LVrB1UA5_gMo5tU7gUB4y-0RKz9_48tCZ8PLGqO8s0rb9x8kBLzqMsff-y_5aW_UzqkbQL1_dfDjy1BsA_Axx4NZcEI14Gh09i3cLwx0snUlSslBN3NpYZfAQwHw-oQadHeNl2pCipofOcLhm6YMRAJIoqI3PNc2Jh1CIXbx0r7jtNwfNkIrIfSqs7R0zbzmx_FNr2t3ctrgA_MwO52LZLde6Tuc05TFr9o4J7mmAepme_UahvQvcBoxRUZQDlYtN1zklJG2etuXRSZI501vvDqxJiworay8G8k_lVlVaDA_H_LjlLkGlMyUrfB_OWyR_iJmOWsRGudseCodZsV5ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شکار دومین زیردریایی ارتش تروریستی آمریکا در تنگهٔ هرمز
🔹
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد: رزمندگان نیروی دریایی سپاه به‌یاری خداوند طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک توانستند یک فروند زهپاد پیشرفتهٔ ارتش تروریستی آمریکا…</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/464727" target="_blank">📅 14:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464725">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmLme-4_oDDV7dd2ugt0sHr7Pebl3ICELIYOg3r3ulegEpzKycsRmicure5L2B9Agu19gNq-PiduH8kLhdWjI4CMxPa4Vep_cveZfned-mB6XJzGKEasOq9pHLabrl0I3rdM8GLf4KTPzOatrcwz9-GWJQAwX3Sqs-mnr49B7tAiorHe_ghUn2ZG-Gz6hxC1XvTD3Td9jjZJZeriyq_7N3cYVtFCNx7ArXeNJ1tAXNMiSag7GoOOKVwi-h0Pkuo1wn0xsnXcezZXyCykc3HGZRsSlwEn-dZrpwd2wdzTZb0mP5TLPkpu_qe913IYcO5hmOEU8ZEj3-DemavM2kWbXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شکار دومین زیردریایی ارتش تروریستی آمریکا در تنگهٔ هرمز
🔹
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد: رزمندگان نیروی دریایی سپاه به‌یاری خداوند طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک توانستند یک فروند زهپاد پیشرفتهٔ ارتش تروریستی آمریکا را که برای جاسوسی در تنگهٔ هرمز فعالیت داشت، به‌دام بیندازند.
🔹
این زهپاد از نوع یکی از زیرسطحی های هوشمند و پیشرفته با نام «ریموس ۶۰۰» (Remus 600) بوده که توسط رزمندگان نیروی دریایی سپاه به‌غنیمت گرفته شده و اکنون در اختیار متخصصان این نیرو برای بازیابی اطلاعات آن قرار گرفته است.
🔹
نیروی دریایی سپاه با قاطعیت اعلام میکند تنگهٔ هرمز مسدود است و در برابر تحرکات خطرناک و تردد از مسیرهای غیرمجاز در تنگهٔ هرمز، با اقتدار و بی‌وقفه در حال برخورد هستیم.
«وَ مَا النَّصْرُ إِلّا مِنْ عِنْدِ اللهِ الْعَزیزِ الْحَکیمِ»
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/464725" target="_blank">📅 13:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464724">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl4K0J7znUoTHWirltD5HIQZ5XeYMN-157jZVpVp0M2LtaYYBxsti2zkQqUFN9HEJ1e1UcfdO5Sl7SlYPGgUARqJsz3K27wnP7XzOYfXgh7GcUbHkBI022IxouAjl13JFG7NfNxd4rtH5o4_PsteCCkZQT34bfR4xOWf2PxEi9Bpy2r9X4tA_XSSBoDDo5m0zVn5tDNgYyI-P442mUSu9zcbME3KtzzA7J-j3s_0PSMV4yseNI-5ESibo75ZUu_JmjA3aDXSpKFSbww5gqOUOox6FLsDh7U-cBwk6OkuTPAGnBV0pO61I-NfnIVGXib_Y4gkO-OfQYtCep0twKc4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات جدید از افزایش اعتبار کالابرگ
🔹
رئیس سازمان برنامه‌وبودجه: فعلا برای حدود ۴۴ میلیون نفر واجد شرایط پیامک ارسال خواهد شد تا با تکمیل یک اظهارنامه شرایط آن‌ها برای دریافت این حمایت مشخص شود.
🔹
افراد تحت پوشش کمیتۀ امداد و بهزیستی، و خانوارهای مورد تأیید…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/464724" target="_blank">📅 13:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464723">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b747c57d0d.mp4?token=VTkOCDPwLvk-Yb88HiwBX2CLA6NP5azrwhgJvVvjwM6YqcbY7CvZ12doJalHiaIEJFCUZtskHqTR3u4oFGFPgMW_88U_7mAPqq58jRqHPCNrSxIqprTeyz4Sp7na88nJKdv1RYzz2Hb4GXDIgwtNG0rnzlVvQTsfLG3dWtb8aPmPNR2yqm7b8zqh8MvGqrO-oSnVOOXwXf0LR73HrqDlNoyxgYZhqSumqqZzxHPFeZqQ2Pg5w7NC_HKIgtTvOfmzcnYqCysa-TSYTGRy40cKpiWFO8x1IgkWUFoPdO80t5SlfZoxRc6AAnH0j7ix62clx7IOi9K4ZfIaTtx1Tw0V3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b747c57d0d.mp4?token=VTkOCDPwLvk-Yb88HiwBX2CLA6NP5azrwhgJvVvjwM6YqcbY7CvZ12doJalHiaIEJFCUZtskHqTR3u4oFGFPgMW_88U_7mAPqq58jRqHPCNrSxIqprTeyz4Sp7na88nJKdv1RYzz2Hb4GXDIgwtNG0rnzlVvQTsfLG3dWtb8aPmPNR2yqm7b8zqh8MvGqrO-oSnVOOXwXf0LR73HrqDlNoyxgYZhqSumqqZzxHPFeZqQ2Pg5w7NC_HKIgtTvOfmzcnYqCysa-TSYTGRy40cKpiWFO8x1IgkWUFoPdO80t5SlfZoxRc6AAnH0j7ix62clx7IOi9K4ZfIaTtx1Tw0V3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم ایران در دانشگاه تهران توسط وزیر علوم به اهتزاز درآمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/464723" target="_blank">📅 13:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464722">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182adcc130.mp4?token=nVIsPnycY61KZMHf9_6uMX9mPALjXTSoJYppqJWnB-bEMCYixYXM8uLkXvwu3MynWgFombRFdPfbgP0DZuhNtBb6Cv9BEYGIfKLJnlVCeZyI1B7NZYSocbEJz826y2dJ0IkhY3y_AL2jprRPncZYOs167ldDOzjItq1did-f6U11AzCTk_h14V_MkoHTuQYkjri3bR68c7IFCKnE9fvS3DK_-wQwmRQVYI57BzcpsVrLTAqzOfW15LFlT9-eKVcKpnIlnaTCvMZtDlzLEBF8ETNT41uOZIrxlhS_zrdYnbX35vwNX0BG2_1JuHWp6C3rEkUo8BzMyl1j3pPbWABx4WPPtYjTFg32weLCg-1q_FflUv5MmRjwCJomKnAEAcvasGBRnBmKDI3ucXyAvcEdfxO43IKjCxBF_UIkxyZGEZFA5xbWPzX-bifSYgDfHSTz3JhnXTDC9yr_u6n0SxxVi4OTnbaKavCSHH_thOmyFnlH5uJRXbqe9f8xag9bGTJYx87uVw3703lnGpdqVNrY-XZb9cyCG0oNbUtTHNFI-mkYnaifyQAsjaQoAbBVo0_qtncqJIHLjr2IsXkHHtrUAPLG7fjhPOBR8b8riY0H6fV-ZHGRSL2hgmTHqdQ4bgqt6v3UDsRe_Xur8d65j0WzvjsCWerUnRxD_JLvdX9DlHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182adcc130.mp4?token=nVIsPnycY61KZMHf9_6uMX9mPALjXTSoJYppqJWnB-bEMCYixYXM8uLkXvwu3MynWgFombRFdPfbgP0DZuhNtBb6Cv9BEYGIfKLJnlVCeZyI1B7NZYSocbEJz826y2dJ0IkhY3y_AL2jprRPncZYOs167ldDOzjItq1did-f6U11AzCTk_h14V_MkoHTuQYkjri3bR68c7IFCKnE9fvS3DK_-wQwmRQVYI57BzcpsVrLTAqzOfW15LFlT9-eKVcKpnIlnaTCvMZtDlzLEBF8ETNT41uOZIrxlhS_zrdYnbX35vwNX0BG2_1JuHWp6C3rEkUo8BzMyl1j3pPbWABx4WPPtYjTFg32weLCg-1q_FflUv5MmRjwCJomKnAEAcvasGBRnBmKDI3ucXyAvcEdfxO43IKjCxBF_UIkxyZGEZFA5xbWPzX-bifSYgDfHSTz3JhnXTDC9yr_u6n0SxxVi4OTnbaKavCSHH_thOmyFnlH5uJRXbqe9f8xag9bGTJYx87uVw3703lnGpdqVNrY-XZb9cyCG0oNbUtTHNFI-mkYnaifyQAsjaQoAbBVo0_qtncqJIHLjr2IsXkHHtrUAPLG7fjhPOBR8b8riY0H6fV-ZHGRSL2hgmTHqdQ4bgqt6v3UDsRe_Xur8d65j0WzvjsCWerUnRxD_JLvdX9DlHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چگونه واردات کالا به کشور در شرایط جنگی سرعت گرفت؟
🔹
محمدحسین مصباح، فعال اقتصادی: سیاست‌های پیشین ارزی در کشور، تجار را برای واردات کالا زمین‌گیر کرده بود.
🔹
اما بانک مرکزی با ورود به‌موقع و اصلاح یک رویه غلط، گره کور تجارت را باز کرد و دغدغه دسترسی به کالا در شرایط جنگ و محاصره برطرف نمود.
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/464722" target="_blank">📅 13:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464721">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d2ab6808bd.mp4?token=nvj6SwLSU0KSjHHJp0YLHv6mqbJETEC6zTEtUGl7vfmUigzSlwumV1LuavjuhGeqOdLqWESnfozmnVymUK3495SGo10d3W3GBT9oB2RpcKzLQZ71alCvc9661mT-rgs_4JO787gvr8MQSjOrFiy7GDbpd7-6_2fmhwTzI1TXCTZguWlFC2P02Y1OcPTK85KFYhWf_vKQlNb_Y0sEoPgc1aVqW3n-gSSly3s9WGWp7zwecYDrqC_SgHw5MaEYH7EsT6zz4Kzu528WdvigCg5UARLhYCp_giZ0CcOw8A0_jwSN5qNzT5i7xSj-Grh6jeFZYoqX-hKg3_BIjBgRdSKjgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d2ab6808bd.mp4?token=nvj6SwLSU0KSjHHJp0YLHv6mqbJETEC6zTEtUGl7vfmUigzSlwumV1LuavjuhGeqOdLqWESnfozmnVymUK3495SGo10d3W3GBT9oB2RpcKzLQZ71alCvc9661mT-rgs_4JO787gvr8MQSjOrFiy7GDbpd7-6_2fmhwTzI1TXCTZguWlFC2P02Y1OcPTK85KFYhWf_vKQlNb_Y0sEoPgc1aVqW3n-gSSly3s9WGWp7zwecYDrqC_SgHw5MaEYH7EsT6zz4Kzu528WdvigCg5UARLhYCp_giZ0CcOw8A0_jwSN5qNzT5i7xSj-Grh6jeFZYoqX-hKg3_BIjBgRdSKjgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💍
حمایت ۱۳ همتی بانک تجارت از جوانان با اعطای تسهیلات ازدواج و فرزندآوری
🙏
بانک تجارت با پرداخت ۵۱ هزار و ۵۷۷ فقره تسهیلات ازدواج و فرزندآوری شامل ۳۳ هزار و ۳۷۶ فقره تسهیلات ازدواج و ۱۸ هزار و ۲۰۱ فقره تسهیلات فرزندآوری جمعا بالغ بر ۱۳ همت، حضوری موثر در حمایت از جوانان و خانواده‌های ایرانی داشته است.
🔵
این بانک با بهره‌گیری از زیرساخت‌های دیجیتال و سامانه باجت، فرایند ثبت‌نام و پیگیری تسهیلات ازدواج و فرزندآوری را به‌صورت غیرحضوری فراهم کرده است تا متقاضیان بتوانند آسان‌تر از خدمات مربوط استفاده کنند.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/464721" target="_blank">📅 13:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464720">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/464720" target="_blank">📅 13:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464719">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp9ywixh9VBPzSsnnbAbUrcngypFhmzEdcWwF2oD0JsprLhMWRcHhy7djCPPo-IJwhgzanJVOqDbNVZgPcLc5nkhNUcYO2HhlPQpdLj7PUt0HH9vfeea6bazpXbU8QM1bJ0EoSOx0HUH0eVAeVBWjM7TAJsy1-R2dzPGPQgY8q7M9yGkhkaOH2Sj-PrrByD1Gamp4ZVKv2lqjGFtqrrWuQyzr0iODIMvO6kgDsS2-fIesXY6zGRklqyYyQAn8FK9XRQoa5BVOVxPw0DPyhtIXDoORctVuFPQ4gUNQ6dWgD8VTwfcBOsxexolG1a3hKj9YFbWBRGgFhf5pTu9xmlzfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالی‌فروشی طلا مقابل چشم ۱۰ نهاد ناظر
🔹
با وجود حضور ۱۰ دستگاه از بانک مرکزی و دادستانی تا وزارت صمت و پلیس در سازوکار نظارت بر معاملات آنلاین طلا، همچنان موضوع دسترسی کاربران به دارایی خود محل ابهام است.
🔹
درمورد میلی‌گلد، این پلتفرم اعلام کرده طلای کاربران در خزانه‌های بانکی نگهداری می‌شود، اما محدودیت دسترسی به ذخایر طلای سپرده‌شده در بانک کارگشایی باعث تأخیر در بخشی از تسویه‌ها شده است.
🔹
میلی‌گلد همچنین از وجود ۹۶۵ کیلوگرم طلا مربوط به تعهدات کاربران در خزانه‌های بانکی خبر داده و گفته برای دسترسی به این ذخایر محدودیت ایجاد شده است.
🔹
بنابراین موضوع مطرح‌شده، طبق توضیحات خود پلتفرم، بیشتر ناظر بر دسترسی و تسویهٔ دارایی کاربران است، نه صرفاً ادعای نبود پشتوانه.
🔹
از سوی دیگر، سامانهٔ ناظر بانک مرکزی که طبق مصوبهٔ دولت باید ظرف ۳ ماه راه‌اندازی می‌شد، با گذشت بیش از ۸ ماه هنوز به اجرای عمومی و کامل نرسیده است.
🔹
مسئلهٔ اصلی برای خریدار، تعداد نهادهای ناظر نیست؛ بلکه این است که هر زمان اراده کرد بتواند طلای خود را بفروشد یا تحویل بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/464719" target="_blank">📅 13:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464718">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8oDv5BOkTSD1ztl63bYrsP5qN4210LKwHSdEMW4Iej6zhwx0GdQzJv5Ge9ST3BlMiyEmV4Shcbui0RxYN8cClArZ_WzzrsQsXpbqvsunu7sj5LYKHB5uaD4dyxCGDIqdL5x0G1aorso-B8fHYKmauC8Csl9xMme2kMck3uRu9vdKHxp6ybOG-f2FTc9hF-6BCvyutquvGWslOH2XUF_4jWqB_2KrJ6IJ3VOnGSKpi1Mve9s_8SPtOx4ZxH3W0hhB6ldWNfG34Bdrk3eZf_lxt1DZKuZHm_X5jpJHnBjaR8_O-AHqMWxtEdpT4e2s7IjtGBXRTYhCjb0eZcylIl4lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌های آسیایی ناگویا
تاریخ‌سازی دختر وزنه‌بردار ایران با مدال برنز
🥉
ریحانه کریمی با ثبت رکورد ۱۰۷ کیلوگرم در یکضرب و ۱۳۶ کیلوگرم در دوضرب و مجموع ۲۴۳ کیلوگرم، مدال برنز بازی های آسیایی ۲۰۲۶ را کسب کرد.
🥉
کریمی اولین وزنه‌بردار زن مدال‌آور تاریخ وزنه‌برداری ایران در این بازی‌ها لقب گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/464718" target="_blank">📅 12:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464717">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbca6bfdc5.mp4?token=IY_Ygtx1q2tzgA7drxyi2mIJKN_FsQ3pxZkTAsZ32Ygh3kcNloQDU7D6vXnzCEKVfbgTBqxw1LXMuVn3fgDsRJCF2TwBW1raou9TF-zOpMTpX_X8nildG7sueHgc0hCkUrh1DCTW8OEELxOLMGDzrTl3bYCElMjunI4fFIHhN52agiOB_5EAam3StXm18_NvdBaUBaISa9bU5YJqpRolgRk5pJz9qFiTH6OTJPi3kIADEJFmFiSLOOloDT9CHmS4zS-fMkjsyGBACB_Z76ZsnPkPo8leyzzbCkwDC81ncViVTcOr18tHiJcno61WGqZydf4U0ubLkCBGJXt4H8yaAHYvY2ImCa51lO_dQYVaLpaYS2x1ruDMMyB-3coPMe1ewlC5LXyoUOo_0UER27_vDTGb2GtvpjaWWoNLy1SY4-uXYZPi0KRXOXuKI7zkL4lmIlHaeZmQDyHyzI1XRjDsGrUqTa9xf_Ni4xHe5sq-MVFEo1LExJwuhGtZ6kuielG0FuEQ_DxAiWLj9DngWPf9jVhr8kmQzrzd_kO5OGifyP4_MF9Vz742OFspxdwYPbdghdHrPSThSqLOOWQoKJsDLJ8Xn0l_VojN0NfJBQyDCY9YgFk7YZlgSpyUEgs8r2zK_6oyMj5X3jV6_gIYrK8Z5EooCKI0NcKKDaMfWGBh0oI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbca6bfdc5.mp4?token=IY_Ygtx1q2tzgA7drxyi2mIJKN_FsQ3pxZkTAsZ32Ygh3kcNloQDU7D6vXnzCEKVfbgTBqxw1LXMuVn3fgDsRJCF2TwBW1raou9TF-zOpMTpX_X8nildG7sueHgc0hCkUrh1DCTW8OEELxOLMGDzrTl3bYCElMjunI4fFIHhN52agiOB_5EAam3StXm18_NvdBaUBaISa9bU5YJqpRolgRk5pJz9qFiTH6OTJPi3kIADEJFmFiSLOOloDT9CHmS4zS-fMkjsyGBACB_Z76ZsnPkPo8leyzzbCkwDC81ncViVTcOr18tHiJcno61WGqZydf4U0ubLkCBGJXt4H8yaAHYvY2ImCa51lO_dQYVaLpaYS2x1ruDMMyB-3coPMe1ewlC5LXyoUOo_0UER27_vDTGb2GtvpjaWWoNLy1SY4-uXYZPi0KRXOXuKI7zkL4lmIlHaeZmQDyHyzI1XRjDsGrUqTa9xf_Ni4xHe5sq-MVFEo1LExJwuhGtZ6kuielG0FuEQ_DxAiWLj9DngWPf9jVhr8kmQzrzd_kO5OGifyP4_MF9Vz742OFspxdwYPbdghdHrPSThSqLOOWQoKJsDLJ8Xn0l_VojN0NfJBQyDCY9YgFk7YZlgSpyUEgs8r2zK_6oyMj5X3jV6_gIYrK8Z5EooCKI0NcKKDaMfWGBh0oI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توهم تجزیه‌طلبان برای تصرف تهران با همراهی مردم!
🔹
طرح مشترک آمریکا و اسرائیل که به تشکیل یک مرکز فرماندهی با حضور افسران عالی‌رتبهٔ موساد و سیا و همچنین فرماندهان گروهک‌های تجزیه‌طلب کردی منجر شد، درصدد اجرای سناریوی تجزیهٔ ایران و تغییر نظام حاکمیتی جمهوری اسلامی ایران بود.
🔹
این طرح با حضور مردم کرد در صحنه و همچنین با اشراف اطلاعاتی و برخورد قاطع نیروهای جمهوری اسلامی، از جمله موشک‌باران و حملات پهپادی به مقرهای این گروهک‌ها، در همان مراحل اولیه خنثی شد و به سرانجام نرسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/464717" target="_blank">📅 12:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464716">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH1N6BZ2QH2hwwyIppyvE9cUWT3kZMvFcz-aOFbWpH1tgVj82Sz4aaGETaD4Qf5uZE_Ogri73O7zIQS1XjM5gCuY92CEa883hHzdwhUthgh4Y4tJJQ1APz6yUQb75n7aWOftKDgyOB1fyP6yXISzcQJBr6oYTX7CGEzPKA7Ow0-03LkmadKyVTzesrQcc-hC6lFE3qXdpBFsPqc0igZ3yZ0e6HS2880frBtkNdADfFyan1z4vJdHPSJt8qJjLrchX2MnkjusK9YyPoBB5Up7Ci14Jl2KhZT98AJQPjPXVV36Sve6rDHWceY7JdrN-MagZsJJAY_OUzqO2NTzxRyVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به بالای ۷.۲ میلیون برگشت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۱ هزار واحدی به ۷ میلیون و ۲۷۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/464716" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464715">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">منبع نزدیک به تیم مذاکره‌کننده: ایران منافع خود را تحت فشار واگذار نمی‌کند
🔹
رئیس‌جمهور آمریکا اخیرا گفت که پیشنهاد توافق ایران را رد کرده است؛ حالا یک منبع آگاه نزدیک به تیم مذاکره‌کننده در این‌باره به فارس گفت که پیشنهاد اخیر ایران دربرگیرندهٔ مجموعه‌ای از اقدامات متقابل و مرحله‌بندی‌شده است و ایران مواضع و ملاحظات خود را به‌صورت روشن به طرف‌های مقابل منتقل کرده است.
🔹
این منبع آگاه با اشاره به فشارهای ناشی از رویکرد و منافع رژیم صهیونیستی در سیاست آمریکا، تصریح کرد: وضعیت هیئت حاکمهٔ آمریکا در داخل این کشور با چالش‌های جدی مواجه است و نارضایتی نسبت به پیامدهای جنگ و هزینه‌های ناشی از آن افزایش یافته است.
🔹
این منبع آگاه در پایان خاطرنشان کرد: ایران همچنان مصمم است در برابر زیاده‌خواهی‌ها و فشارهای آمریکا و رژیم صهیونیستی ایستادگی کند و حقوق و منافع ملی خود را تحت فشار و تهدید واگذار نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464715" target="_blank">📅 12:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464714">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-peBbVa6j1uRuR4Lbu6YVB7XL1vrvvKamOobcQyydga5SmwAJvSo4gx2hHChsPzWijKAsQXP67OEZ7COBrWba3yX8YegfxX0E1nYrk-4Tzk_YCAmJJS2DZRvHT7igQgX2LkIMbHfNIa7eBFZU-VihZbtBIzaIGNsrMOvhBXY4ekhQyN-CdOUGOpvTwLVWnWm8muUgwT-WRfjy77rNRxFrvquTTkcwQlED7IP2F38Lh6mO_PRB-nrjHiRNOsnfab9aT1r1Wblgfl-EuRioJgYtEI_8xaceAt8EhBO8uJQeZUALrsqS5WKwKe_pU-O4dfeyymHC3zApg3WvtXsgDnfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واترپلوی ایران از دیوار چین رد
نشد
🔹
تیم ملی واترپلو در دومین بازی خود در رقابت‌های آسیایی ناگویا، نتیجه را ۱۲ بر ۸ به چین واگذار کرد.
🔸
تیم کشورمان در ادامهٔ رقابت‌ها فردا در آخرین دیدار گروهی به مصاف کرهٔ ‌جنوبی خواهد رفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/464714" target="_blank">📅 12:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464713">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
اعلام «حادثهٔ بزرگ» نزدیک پایگاه میزبان آمریکا در انگلیس
🔹
پلیس انگلیس از اعلام یک «حادثهٔ بزرگ» در نزدیکی پایگاه هوایی فیرفورد که میزبان نیروی هوایی آمریکاست خبر داد و اعلام کرد که شماری از خانه‌های منطقه تخلیه شده‌اند.
🔹
پلیس شهرستان گلاسترشر انگلیس امروز از تشدید تدابیر امنیتی در این پایگاه خبر داد و اعلام کرد چند نفر را به‌ظن ارتکاب جرایم مرتبط با قانون مواد منفجره بازداشت کرده است.
🔹
به‌گزارش اسکای‌نیوز، تیم تخصصی خنثی‌سازی مهمات و مواد منفجرهٔ ارتش انگلیس در حال بررسی شماری خودرو در این منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464713" target="_blank">📅 11:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464712">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOgyJPxrO5GtwoMo1MAYWcEd_aD3o1xo9We-qZJ6D_SXm_aFyOp1LXzXkEJ7xoYydbX8iRstwTlVYuibWZ9mfi-xtnXrJydcxDZWxUSQ-FqmIPfdvAs1gs1M918nLWSXuOkHyFNHmJgXF_4Wjcp-b7pKbJos4-lJbz86kY4LV0GmHbMl0dMXxg5RFo1v1zdrIkCSJHNt3jQA2gWskRH49lUPFVoQIwehQ28hlnN6ZvNdzf6wXs4veJTQTDQ0VgBML1dkE90LLP2aaE2HAl3fKB2jhUAPxCHUsn8DpX0i0h5HcGfU_vvC39wzutd7I73NW1DIYKYgpg5qGQ38m6LhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل راه ساخت حساب جدید را برای ایرانی‌ها بست
🔹
کاربران ایرانی هنگام ساخت حساب جدید گوگل با ردشدن شماره‌های +۹۸ در مرحلهٔ تأیید تلفنی مواجه شده‌اند و در بسیاری موارد امکان دریافت کد تأیید نیز وجود ندارد.
🔹
این مشکل فقط به ساخت جیمیل محدود نمی‌شود و می‌تواند دسترسی کاربران جدید به سرویس‌هایی مانند گوگل‌پلی، درایو، فوتوز و پشتیبان‌گیری اندروید را هم تحت تأثیر قرار دهد.
🔹
کاربران ایرانی پیش‌تر نیز از مشکلات تأیید و بازیابی حساب‌های گوگل گزارش داده بودند، اما علت دقیق محدودیت جدید هنوز مشخص نیست.
🔸
براساس پایش‌های شرکت ارتباطات زیرساخت، حدود یک‌سوم سایت‌های مهم جهان به‌دلیل تحریم‌های آمریکا، به‌طور کامل به‌روی کاربران ایرانی بسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464712" target="_blank">📅 11:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464711">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM8J1bWbklHhWvWPsGCrJln2pmrF3T026FTJ7rb9AmHN4JMwO2dwJ0P62W5kcYge0HWpIbt_fxKneEWIgaqQ6VNSJdiYtb4RQzLghacgT6-pS5sVoT3RwuxqQpcP9yk7U_tnTfH3wk20fPgQwx1oO79YFaL4pCLC0CXZ6puGfIkxcEC8d82gT1j3Gxmnxk43wqFHkFIYQDGnL_5aacLVI2OR0Fy8sB2a6qFwn1FV8q_IdjAmBBOtxrRlID6Z_hD_Uu4Rt1yrtLemwgS4rxnjp73ccWJ_785b2PiYLgqOyPX6dusw-0pld7uGeiR3uHd_VWMsexhEoyhmaRykJhJmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل ارتش: اگر قرار بر ناامنی منطقه باشد، این ناامنی برای همه خواهد بود
🔹
امیر حاتمی: هنوز جنگ تمام نشده است. همچنان باید آمادهٔ واردکردن ضربات سخت از سوی سربازان ایران عزیز به دشمن باشیم.
🔹
اگر قرار بر ناامنی منطقه باشد، این ناامنی برای همه خواهد بود. نمی‌شود ما در منطقه زندگی کنیم و سالیان متمادی صاحبان این منطقه باشیم، اما دیگران از جای دیگری بیایند و از همهٔ این موارد استفاده کنند.
🔹
من به‌عنوان یک سرباز ایرانی از همهٔ همسایگان و کشورهای منطقه می‌خواهم به این موضوع توجه کنند؛ دیدید همکاری با آمریکا امنیت‌آفرین نیست. امنیت منطقه در درون منطقه و به‌دست خود کشورهای منطقه است.
🔹
امنیت در منطقه جز با ازالهٔ آمریکا و زدودن آمریکا و رژیم صهیونیستی از منطقه اتفاق نخواهد افتاد و این اتفاق دور نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/464711" target="_blank">📅 11:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464709">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae1b2095f.mp4?token=YRS8wBAEyGRZGfH410zLA7Bk053q2bVm1Nle2ZFSv0GWuIXu5BZ7wI-hNVeN9gW61X3POr8ok03NOf82OsR7HZIqBkI3BMnnEfVKe0xKB5qSPQH_n5aXnLKr2VokyZj1RNXMxeTMVt9Ef-v37kkfaZJAbDKeFw3l0n5QDHJdRQ0cTW_i6SE1zSrWbn6y0WWtRJncT9dKptFmxmLKfS3xYhKxfUx_GoKVmSvqu70MWzO83Xk_8r3lNOFKbLzuxNzKiFIQP3A8Ve6jS5eVHvorzsWVOBoSw3iREWcspFtBQE6vqxflDylWsal5kIDALh_mh02Zlc5TrijflwZKbtcOUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae1b2095f.mp4?token=YRS8wBAEyGRZGfH410zLA7Bk053q2bVm1Nle2ZFSv0GWuIXu5BZ7wI-hNVeN9gW61X3POr8ok03NOf82OsR7HZIqBkI3BMnnEfVKe0xKB5qSPQH_n5aXnLKr2VokyZj1RNXMxeTMVt9Ef-v37kkfaZJAbDKeFw3l0n5QDHJdRQ0cTW_i6SE1zSrWbn6y0WWtRJncT9dKptFmxmLKfS3xYhKxfUx_GoKVmSvqu70MWzO83Xk_8r3lNOFKbLzuxNzKiFIQP3A8Ve6jS5eVHvorzsWVOBoSw3iREWcspFtBQE6vqxflDylWsal5kIDALh_mh02Zlc5TrijflwZKbtcOUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر عراق در ایران: دولت عراق تلاش می‌کند پروازها از سر گرفته ‌شود
🔹
یاسر الحجاج: دولت عراق به تلاش‌ها و مذاکرات فشردۀ خود برای بازگشت شرایط عادی پروازها بین عراق و ایران ادامه می‌دهد.
🔹
توقف پروازها بین عراق و ایران یک وضعیت موقت و گذرا است و به عمق روابط…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/464709" target="_blank">📅 11:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464708">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKadwjqaNY-_M_3uss9sZBaZ3Lk8iCSbtIH9wJ5grKitY0vynbl-uifBH3gg5ET6EOsfhHkpUyJWwBzgF96pfgPzVR6N-Q4oTyUHNbj-VTaINYh_ATRUlCiPxs9pkgukL8iZZZcumYrrb1qiAmFR2ZpcenY-C-Hp7Rgzg-jB3AU6BbtTNZvKwqbyCNxu9pni55guuKUpoLb25hYyox4uCaGsq3RGUG1iX-7J_NAiNWSFEi-RcHuLqkuzrcQYCB30jZKMCNxt6FFkv72pbghu4mO2xYAmgGsnz7wqCIeP2__T9DLGjdxk6qfg-wYofO_Zpcnnxma0kZ-LJ5WDET4O6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید؛ آن‌که از آتش برخاست
🔹
بعضی از آتش می‌گریزند و بعضی از آن زاده می‌شوند. موفق محادین، نویسنده سرشناس اردنی، در سالروز شهادت سید حسن نصرالله، او را تجسم همین برخاستن می‌داند؛ کسی که از نجف تا ضاحیه ایستاد و حتی پس از شهادت، اندیشه‌اش چون زبانه‌ای از آتش، تاریکی را می‌شکافد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/464708" target="_blank">📅 11:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464707">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SA1XsVFMG0hlnFsPSDPmnMbAL92okPVbv3FAiZxC5GjWo9PlKX3h6S1s7zwQEWCCmn_zv5tErB5Vfl4kNE8R-tXBBpkoZawEGclVYOjvOJioX2plpFJB8xqnwjQXZWSQYBMaE5zWN-y8Y90CGoLbQdTP9Y12aRD-7zTAocwYazD8BVf27_qUrvio2Ss-ngq4yJQ3m7yQg4AWxDapp8ppbycRW2__3c1dkEO2ViGj5LtQIwK_lETCvSrclxt-fx2LdJrImhWZT5OCJ4XAXIRJCl85GzkeFdv8ewGOd_3cm0hWnGP4Qb_tLKYkAAgwJZciHlZSwPB-Nus5KNtHrlLWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ثبت رکورد جدید جذب منابع در پیشخوان‌های شهرنت بانک شهر
👈
پیشخوان‌های شهرنت بانک شهر با ثبت رکورد 12 هزار میلیارد تومان جذب منابع، موفق به ثبت دستاوردی جدید شدند.
👈
به گزارش روابط عمومی بانک شهر، محمدعلی بخشی‌زاده، مدیرعامل شرکت توسعه و نوآوری شهر، با اشاره به دستیابی پیشخوان‌های شهرنت به رکورد ۱۲ هزار میلیارد تومان جذب منابع و تثبیت آن، از تلاش و همراهی همکاران و راهبران این پیشخوان‌ها قدردانی کرد.
👈
بخشی‌زاده اظهار کرد: دستیابی به این رکورد، حاصل تلاش مستمر، پشتکار و همراهی تمامی همکاران و به‌ویژه راهبران پیشخوان‌های شهرنت است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/464707" target="_blank">📅 10:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464704">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6_hS8f0LrcxHM-Op-rTQx2EJt8wPMNmpDIC7CHodQGg_zQ0-ZwugVx6MyNUSyiqC8S4U1OHABuDEJDK6tUA8Ia4JOAGr02tg5fT-RiQZ_SlFvo-rHw0Su7VBsqYkgtwDzB0_P37okejZyJ8EKiG0AAaRVuFDeqyGbM0PF5qD6cmEsi8uk_SvG8VzvaJoU6LccyAu3_m2F37ZdwK5LZ0Va6OHLXbzzpjjlslOypIgIN7R3iG1hWkJTX0H7BsV2lrdERwWWFnoDBe6cfwazYFhsmk8rGu-AANd0Xy9i4DgNSq8ct15zl0oItye4S0Em6y4odf30S3XH-IVNtyIl9EKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2RUNLPymOPI2DOj9ca_wszc1VHJpLh5nxWiEEeOMmwfvk8nfwhT6HRBACdQPvDoYbzih4oA_LkaN0_NQ91Z3KFy-UHpk6zLHB4qob3R1Sbu7rM2ww63qYZT5CyqDIyZH4LCW8uguBGHq2k_b7GvrbLS0qtROC6CffhglUO8vhnWgBHMLXqLAsIqkAxAY1kcbiG7xA6tQ_ru8pc2IYXll_zDmQPRkW88f7jzlAhfih_E9a8gc50aI5Zw7Qxo5QmMiK6EhIXN1wYBS8rwxcktaByWERE10D0E3hCZ-yhrBPTx02ioyHgvb5AW5S8DGKG6sviIHaeyh_ntWcbFWOFHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VYy3z1noBgSmRffxYYb7AmvPirFufOSGKrmcPfeVJJRjaPvKZzIUIqRObg9Io8Tvqbzaw0RWnHGiaxchV7jEXvxAqdrzrHw44o4bwbey7iTFbjcF3IywxsztTuyTOlNxLIBu1RznUMGoN03kZxf83PoBHZwAOmzkKkyi47gGKKN4HVK_OK3irKWW1gXpDi6RAwerb2OcYZRcBgcbnjG0V3-pWipECrxcgCHUtYLgMFCCGQjdd2qG5bnzRasIfi39qzfDnjh1tjZ4yF3lx9cJ5H6BbR-PwNlfm3qVYOrG0FjxVIuI5ZdSMtZLMTI3Kz9z3O0NrLJbMaL-Cf5-7h_oSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
مدیرعامل مس ایران در سونگون
🔰
هیپ‌لیچینگ مس سونگون به ۸۷درصد پیشرفت رسیده است
🔻
مدیرعامل شرکت ملی صنایع مس ایران در بازدید از مجتمع مس سونگون، ضمن دریافت گزارش از مجری پروژه هیپ‌لیچینگ و مدیران مرتبط، آخرین وضعیت این طرح را که ۸۶/۸۲ درصد پیشرفت فیزیکی دارد، ارزیابی کرد.
🔹
به گزارش پایگاه خبری مس‌پرس، دکتر سیدمصطفی فیض همچنین در جریان بازدید از این پروژه که با هدف تولید سالانه ۳هزار تن کاتد مس اجرا می‌شود، ضمن گفت‌وگو با پیمانکار و بهره‌بردار پیرامون اقدامات باقی‌مانده، از برنامه‌ریزی برای راه‌اندازی مجدد این کارخانه در سال جاری خبر داد.
🔹
براساس گزارش پیمانکار، عملیات نصب مکانیکال پروژه به پایان رسیده و پس از تأمین برق، تست سرد تجهیزات انجام خواهد شد و پس از تست سرد، راه‌اندازی گرم کارخانه در دستور کار قرار خواهد گرفت.
لینک خبر در مس‌پرس:
https://mespress.ir/x6TD
@mespress_ir</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/464704" target="_blank">📅 10:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464703">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/464703" target="_blank">📅 10:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464702">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwAcSrx7jiqzTuKd9fOIPHR8ZR12A8kxLdX08SBiSHRY1AvGCqsuMvCCrsOjFNPu8bnVSgDRe4X7nZackcyFD3WoOWtfB4T5l250GTtYu_PZhoCH6qPRPe14CI7wlerN0yLT1u-6eFjTf-jZjSKeI9j4YsIke6vcQ91zpdtGK4SWXACeo0iyQlp_vL9A01f0yu3ldxzCMEZXtlsvQq9RB2AZDMlTzTC7LfAevuyZLlsTbidqqzQZeRXtNXs7heXeB54UbmxK3WsY5qaGuo4BfpFRaQ5l5imWgCMz6coFRq7gevEF8xaTL15m4AaSaE6Jowr6pbVnv4V2GONaQETyQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوبیتکس هم در مسیر ماراتن‌ جنجالی بلوبانک می‌دود؟
🔹
پس از پایان ماراتن جنجالی کیش که با تامین مالی بلوبانک برگزار شد، حالا تبلیغات ماراتن نوبیتکس در شبکه‌های اجتماعی دست به دست می‌شود.
🔹
نوبیتکس که در زمینۀ رمزارز فعالیت دارد، خرداد امسال هک شد و به دنبال…</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/464702" target="_blank">📅 10:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464701">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCKa9kBoeSZ_Vu3RDqLH77tUuNHZE3M1Css-Xq5QoH8MB0-0s7SNUW3ngM6CMMC7YHAb9KGPYAMeJzaoCePVWOeM0AOA7vAzvzzMBaHKTK02U_9nw3-97t_c0ITYWsCU0VM3zB9LisNfzvgofvXudGqB7gBeetooh3Eduuy6bjipatP5FMs--9Wr9kfse3UKfjJpMVef_PG3zCPXhWspLNeJ_37mvX1p-iHCKZ8HanbvFM6LRmgwCb5AjOXq4V9Xk8YudiywopcCZx3NxOSINL9T_BtliWkuKgbpolLS0h34Qe3q8yG8Pb62NRPqQPJAZ7lMbvZcl48vw-eNMXvfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام جرم دادستانی علیه عوامل برگزاری دوی ماراتن تهران
🔹
درپی برگزاری مسابقۀ دو ماراتن در بوستان ولایت که در آن موازین قانونی و شرعی رعایت نشده بود، دادستانی تهران علیه عوامل و دست‌اندرکاران برگزاری این رقابت اعلام جرم کرد و برای آن‌ها پروندۀ قضایی تشکیل داد.…</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/464701" target="_blank">📅 10:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464700">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9CIz7C0-tzsGah-JlyPuT930BV1Ag0uCi9_L2kW26jS83t1AvZkq09hDzhDBdWQfp-o3h8RvIZaoJ8uBXgtXy8HhYvzaOv0hK_hW2Y8ovW05AoJhzdzKxQjrnjBFOrjUKL0_pSUaXn_Hngf2HXB1iXfe9IKycLN6DJ2HVCDVu8WWzMuWrBcyBfH2fIsjW_6k5OCOY7ZLhjHXMoZEx_SrqQDi7uSPSE3JbEwjkaSUkFro3lyWqf6eOgdX0Q1BPHXcqfUg1Tro8FbrXbrxdRWDMUhu26b7i-6MPOCsp2OgtJdGunaOI-WrpMqf-GMFu7D3_3eCfUujgXaPHg4TRjeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: هنوز رأی پرونده‌های عباس عبدی و صادق زیباکلام صادر نشده
🔹
برای عباس عبدی پرونده‌ای به‌اتهام «ایجاد اختلاف بین اقشار جامعه» و «انتشار مطالب خلاف واقع» تشکیل شده و در حال رسیدگی است.
🔹
برای صادق زیباکلام هم پرونده‌ای در دادسرای ویژهٔ امور…</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/464700" target="_blank">📅 10:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464699">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJuzXOHFqETXjnyvIFhmrMlLvnZbgY8jRcs9WVwml-Uw3Y7hm5rL53YLPUQnS4rNZouZ917dedovhpyyvBbDWHb5w_Frg4AnP5_1fzq9F25Hx8GKbrfHjIF8IihGMzT_XcdXneQ5wANDttWBfZm_weQ_6Qk12j8kcZFqrIRpDhZ_9gEaitJWklGUfeAdBK-QBDLp9YfratoPMGfbiWuCJQfgUBHs02oJPs20Qo6jm175rAjG4cEryva5QGgyuO5jwGjsHRWCTW99Azuu83cmiAiy880JDDeWG6Tb5r_M_L-l-wx73NTmWxYg_FEQyKI5uUFstgg7NSU_-aKnr9yw0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران علیه فلاحت‌پیشه و یک رسانه اعلام جرم کرد
🔹
پس از انتشار اظهارات یک نماینده اسبق مجلس که دوره‌ای ریاست کمیسیون امنیت ملی را در زمان نمایندگی‌اش برعهده داشت، دادستانی تهران علیه این فرد اعلام جرم کرد.
🔹
برای فرد مورد اشاره و همچنین رسانه منتشرکننده…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/464699" target="_blank">📅 10:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464698">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFRlz2bnpro61m5fEn2KuRMuvfQvNRrgsIFfCq9teUSEu5CmgQtlGto47zs510jem6V1WkXBnHdlFi736hKwaHhcbTnjqBokE17qckJCAb509dkfOP3qPqj18T4q4ynOrT7fLC6nFf0-FJNIW_Qx_J6SHfIVkONawEnlD_-Sj7bnf15ojyHSsnMmk2vc3qht88y3k29c1I9CsjfxwLmO68VqcrjaPTawd37Hu9putHmwJqtInmeNqVb3UPOgTwKZZSufyXUwXYACN95yysypNT_wRe4qWSTpu38aQ5iy56qXrManTHCVyPIYFNCbzactMrXO2ZbrdkJauESOx1wkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریاض سوختش را از اروپا گدایی می‌کند
عربستان که یکی از صادرکنندگان بزرگ گازوئیل و بنزین در جهان بود، حالا به‌دلیل حملات یمن و از کارافتادن خط لولهٔ شرق‌غرب برای تامین سوخت مجبور به خرید هزاران تن گازوئیل از مدیترانه و بنزین از اروپا شده است.
🔹
این اختلال‌ها حتی صادرات نفت عربستان به اروپا را تحت‌تاثیر قرار داده و آرامکو تحویل محموله‌های نفت خام برنامه‌ریزی‌شده برای سپتامبر(شهریور و مهر) را لغو یا به‌تعویق انداخته است.
🔹
همچنین اختلال در مسیر صادراتی عربستان، ریاض را مجبور به استفاده از تنگهٔ هرمز کرده است؛ مسیری که هزینهٔ حمل، بیمه و ریسک عبور نفتکش‌ها را به‌شدت افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/464698" target="_blank">📅 10:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464697">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کمیتۀ ملی المپیک پاداش بازی‌های آسیایی را به فدراسیون روئینگ واریز کرد  پاداش ورزشکاران به شرح زیر است:
🔹
کیمیا زارع، دارای مدال طلا و نقره: ۴ میلیارد تومان
🔸
زینب نوروزی، دارای مدال طلا و نقره: ۴ میلیارد تومان
🔹
فاطمه مجلل، دارای مدال طلا و برنز: ۳.۴ میلیارد…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/464697" target="_blank">📅 09:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464696">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انهدام تیم سرقت‌های مسلحانه در ایران‌شهر
🔹
فرمانده انتظامی جنوب سیستان‌وبلوچستان: درپی انهدام یک تیم مسلح سارق در ایران‌شهر، یکی‌ از اشرار به‌هلاکت رسیده و یکی دیگر از اعضای این تیم دستگیر شد.
🔹
در بازرسی از محل درگیری با این اشرار، ۲ سلاح جنگی کلاشینکف، ۶ خشاب و مقادیری مهمات جنگی کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464696" target="_blank">📅 09:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464695">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354f5d1489.mp4?token=DqGCVrBOAIY8qkxovYQoNDGYfRVbAyj1INeSuZkrTRrJmhfjctRTh0BN1S3dCXeAhIl4rvp8zKEOyOkdjZ9dNsaHV7VA2HK242nICIUnUZ0v-szwe0ByaDf2q5cccZ2XKBlABqS9QfbTScOF_UJ2BJ_OzZ010wieKuKJpugZq8uJHMLHx3lEjkniAAunl8_pw60He3kGo8mC_xEa7SCZiB0nt863mfG_UYFu5HH4WVMtV1lbAKPbUOA94fXO3e1Kd-M3jBiqJPxCvMrWwccq7h4Xlc2nzuCoIDAfACY4fpSqXEQyjv2vCDvHNzzPj42ajMQ7esiTTKVJgANW9ucz-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354f5d1489.mp4?token=DqGCVrBOAIY8qkxovYQoNDGYfRVbAyj1INeSuZkrTRrJmhfjctRTh0BN1S3dCXeAhIl4rvp8zKEOyOkdjZ9dNsaHV7VA2HK242nICIUnUZ0v-szwe0ByaDf2q5cccZ2XKBlABqS9QfbTScOF_UJ2BJ_OzZ010wieKuKJpugZq8uJHMLHx3lEjkniAAunl8_pw60He3kGo8mC_xEa7SCZiB0nt863mfG_UYFu5HH4WVMtV1lbAKPbUOA94fXO3e1Kd-M3jBiqJPxCvMrWwccq7h4Xlc2nzuCoIDAfACY4fpSqXEQyjv2vCDvHNzzPj42ajMQ7esiTTKVJgANW9ucz-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ساخته‌شده با هوش مصنوعی از نخستین لحظات جست‌وجوی پیکر شهید نصرالله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464695" target="_blank">📅 09:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464692">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JiOqvH40wN9aGt4J1q8B2SSCnewQwQ9OQYNMfV7QwwGYPGweMUuW_a2v6FMcH0d45aEi3xesc40TYyq_SrdDuakybaIf8POmlLhZm4M79NG6NFHn9Jo0ej6E0oiArf5JXyH2D7H1EPPsCfNcKuFyzDbbEoccCFwe8wA2ZgGHuICY_6HHAgzXE9LgNaksi3gMFfRLVvHwdx4icm6YQt12OJdcRTrdSQpRjqh7RCG2Jpk3WSIexc7n_sIEBs2Gh0GvUBsXHCSFujLdVn4h7QNI0r4w0VIxxVVBWk3Dyq7r1M2F75RGYBqMpaG6-h1KGSUvM9lFHPH0NdJRKX-FGjQ0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCZsydZFsC-I3_yElZS2i8VR7PmTLktT-g4jc3uNQQc976_F0geVt4wWNl29xjmZX2fADIWvVeo4qMIJzE0HmPky3d-0scjC4D0MspRPUFRwVqzgaP_F0yI0c8I6gsksoNUFjD5DutH2_40e9STh6b6L4DWz7x2FGDva_55zk6O-DxxBlaz5ZNxN-BgirQFg_e1xqLfsQe7UJp8Ttvaiw0fi8S64I-3S_ZqXoKtdx5asilFJ7nollKdzZ0SEwVmXassLiESVWI8Ca-V8ZRXzikZenL2A_6E_xuZXMLDPwe4s4d5kgLP4uvbtzLrRMSNlv8hf9Mj8OTEszx8eR3sjcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سقوط بالگرد در کانادا با ۴ کشته
🔹
پلیس کانادا اعلام کرد یک بالگرد در ۵۰ کیلومتری مونترال سقوط کرده و هر ۴ سرنشین آن در محل حادثه جان باخته‌اند.
🔹
مقامات کانادا هنوز هویت قربانیان و علت این حادثه  را اعلام نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464692" target="_blank">📅 09:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464691">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d4b39765.mp4?token=k3Ng7moizlSieU77e0wwvkYDz7xacwbjGw44T1rn1AIFEcktwo30BAHALZKSHm5OMfDCCFqS2aaaPJHuzIvj3BHVejtnFWLexdLRn20j04T0sbf25d5n07h_XjES3qOps1uoYIF1AfSEOimjrY0UWatKjDL46ueRw3c9FUauTD_FACFMIwMspkHBM-A4-G8wyPkLfGfQPY4ORyU0_53eDRUskrHMBS_CS8NL9PW4_xfJxoFfS_pqFqitR13wN7Tdxg1Diga88OEOu5byHZUZo7CQrJcmoDzbQAQIjYP_u6X73WSX0bMxskB1wVVmD2IR3otQZgIonyZGjHYV_wolwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d4b39765.mp4?token=k3Ng7moizlSieU77e0wwvkYDz7xacwbjGw44T1rn1AIFEcktwo30BAHALZKSHm5OMfDCCFqS2aaaPJHuzIvj3BHVejtnFWLexdLRn20j04T0sbf25d5n07h_XjES3qOps1uoYIF1AfSEOimjrY0UWatKjDL46ueRw3c9FUauTD_FACFMIwMspkHBM-A4-G8wyPkLfGfQPY4ORyU0_53eDRUskrHMBS_CS8NL9PW4_xfJxoFfS_pqFqitR13wN7Tdxg1Diga88OEOu5byHZUZo7CQrJcmoDzbQAQIjYP_u6X73WSX0bMxskB1wVVmD2IR3otQZgIonyZGjHYV_wolwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز برای شمال کشور رگبار و برای گلستان و شمال‌شرق سمنان هشدار نارنجی سیلاب صادر شده.
🔹
سایر نقاط کشور جو آرامی دارند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464691" target="_blank">📅 08:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464688">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UequzsC4Q3HEh4zuLZnpsUARo6qUeLtyvHmdf0T2hv5fkh7yRq6BwpN09zlmAdCeegBevO6eeoW2vQy_kL417KumxHfz9rM7mNdt7ky9IfpzwMAUs7sz62M1wLvATB-JMKPywCDiROSYMA--iRAeTtwLRdeFAUJ3UtCnnOsXZi-0AMrLpcTLjiIl3Z37p_iEwOg-m9V7VtUFy2heXLym7TRmK-TquUO3NaEIYjQaZI49pDTaZb0L_v1ijvoN0tFonJO-LLnpwH0hBBGu89o6Qm51QFsKnYkLKsUjU5zU47YipTP1QS7vb17Lqwy1PFzf7bbDqloPb00zCSB3Min_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6dsf9p87cp7aRmYjNGfUlxtlK5MxpMXaugZxBlK7nhZOc8wbvkaFoUYh0h5sy0bFBlpAmUfFtrYZYRrzELech9_vY6Gsq18VIVZvcdbmgw-HLzamsIlL-7QOqQqMmpybWO74rcvqLyaGDl9a9DmpLMTRXUnoIKQllw_f9KpeEcSkj2ECDtp8PpU272FqfBeGMpzsa0WVv3Sl38pItemTAvD8DaFnVlAneSCBrOdseNaabssyeYFby7wCv31sd5vEKXPajT81Gsu4l9OEAYWNtCkFATzlzLpbBEZe38Umhg2MSur6pwR-eYE8jh59Mufdzff8--EgGekC0PpbGYv7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onVA-NR8Urvld-hTJoNDyQPFVThMnN_isPjiTcZrCQesF_6VIhgJW-Wn2WRlSE4K3korwESjIkaSiwnMpMwZnL7OFmu23fG-aoz67KK_H-CVo94ZQTWtkZ_Gko04NH3pZ4vgg0X4LRv4H8gr4lPtqBSRrH8nx9Pg_NJt_Ke-bJSTt41725wDMO-a4Tsr1o_eokt_Ye6QI-x8wRjqGxb_H58M89B8Hsl4hgW0wzEoWhx_Mn_Zx9edzPW27QY6IoMn_njOO6dP2CVgPSmpiIiAzQAB8YzuSb0xMdw3N9Fu07rY0BMrnHiYvosoSCmb-5sp6ENjdUWsPnc_7PZPT_Lcng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عراقچی در نیویورک با وزرای خارجهٔ فیلیپین و نیکاراگوئه و معاون امور بشردوستانهٔ سازمان ملل دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/464688" target="_blank">📅 08:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464681">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPYdLVtJGHNNS4pITyjmFRsEvpAUun_s0U-DwEfL6D9FXA5TDWx3B4hfzu49xdGMjhh-A0Y-R01KT_tQQ3x7eOGpJTVfXhJihsPNxmV448fX6EgLY6BzElireWxsScPJjtyZRjrqhTeiOB7rXao4gkCcSBV1NoiJXcdegDXkb_VeVzwNwkXzxgE9pu9g6vRhG4U4NxGfIW4QfYVJZmrvGR93igv5BzsqdUGs1nGd0mcImuzB_fjQz_5FcTqJTLvkYx391E2O_BAUfJgihl_2evbGspBzprSfE7KF7cX0PsweHp7yv5woaASsaLKat8zqqVdwTxhMbqf5uwWm0oIeOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuacBHUdevWmjmoI0uX-HHVU4ssnOoT_LseG446uZqB_qy05O-nlRzP5EYZfhiX7I2EG1brdMNf8w7nfbFVf-voRvSfDn64SaraBOrd9tzKpZyo1454sYpRIz6O0R7Wsv0zcStI2hZjLhijsB92m_am7xNOMB9u1ltDZU8FIcvm34k2DJrT_usRGVxQ4Es1_S3Z3Ih_rf1cH47RsMKwNmD_fd7B5IMEbWOSZwZTIDE0mgfyczkaiJFT3OXzxGN9I_SCmSC3RqY39nvCDAXJUxSy7M5odckHTuNw98aE2VYT1JLRlKpxTq6FlipW-b7fcHSudz4IZrbiFX3QPoEKyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOTKDzoFGUengOTzp2Ekuc2eHhqe9-U4XhHyEpqBlTki2qK2_ZtBMHqj0dXIow4b9RhwY-d-2hO4oGnsHLtnFUWJA1RY3t7pEZLFmx5FwpVsoF7A7TsFIZ2tbXPzHmihDeSNENOWP4mbfw7Q7N4TzFDeSTw9aHjZMyxfzNR5jGLb2XnkZUWH55O-YiA1lPFP_f8ObFqY6ATACa5vdqlJaXYdu7Cyp1xYdtctng3z_sle3Ps0cXMSn0F45ftZJNgaLSDg8xOsF5fwMTuJIXgeP1NJpaNAIFKdL0Hlst2pLquCIdQ8aRoT76OjS8d1zGzU_LhK4nQmqZvvTBe2juDRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_kq4ZsZeY7yiMW-a6M5lvFKxYkGNYAFIcJOphMISHn-rpcLKTtBLk0_DZXXsOQ9VGk9rYaJIQ1mhRDtpW0piNXpzRrVkjwpkVkM49A1lhdpLVcLff7yBnQHZcsbfDWZP1ahzI9Ag_C3hbdUG5M4LfMf6W_QYJ_t0LjoEeU7HnhcmXu3iV5EFOkQMoXst96WuiA_F8VrC7eUvj0wNirQ8WD_9txTn3l2DHJkVXV18aF5QUHb2xYsCrWZGnzbYZe34LyTxc1zE7GrzLp3vTzdQf0HyPDNwqzks3ThcubbnDuypbxodvcbGknaQCdwdzT7AgxSpJcmlIYqxX2Fmjg5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KREt8BAX2sl8UcytMhV9fcl3d1fH7q_kvus0jCoUHY8u3WcMu8qAMGRZwzDd3gD_xvtetHtQB_xykwN6Gd97GyAkNZgwzl38-LJL0dOmJ7PTlksHh7CvZjfR3UUfsOzJsZuuyCv7jS-xal2guNnHUuUK_0jbc4RTHbxu0iCMEA9G-1TJhtZ_XEV6A4ERVN0YTjTfIx08LXwNwOnWd0bF_tMIoFYz-pP0VNhLBp8h4yUXjpdZW_pSVJ-KFd4INrpzOKBr6IipIkFNSPqL507t0m6yG1zLUWPPim_UWcFodqRWAEVwAaiW_G8KUpqk0IeNSEe5NMnYrL5SsYDcJNpjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgRSlqdzwVxodFZ8C3Ke74kZL5GuSI8ztRg4l-ys_yTJfpPqm9ogTLj1JzGl0zlz-X7U-z3w0KGyGRIRVoNhgsPO2AG6D3EfBAVtH1qZ-lUy0DpR3zP1xEFdOAGetCJAQA8flDolawA1D6t-GUDKzbIOeZNfhWAH3p4Qz2fcllA38hWed3zkFVFB6WR72qio6ZSaQDPlsCuTuZTAmiSzMRTtn5BgxG_yaQKrFu_P0FJOZ9QSa0Sd6Hj8VopkswPVJAGOwBGWAp4xDwVOxyTLmC6laH43u19UTw2Tpf1t_Khhb1_YODFRUFB0s9bvGJWEmCvIeIIQIQmOERX6dTAMMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyQCGvDSF5P-pqUAYxWe6NgJ4-AGUbW67C_5tqWpYUT2oLgUOGE_ZaTRzRREEjnowNv6aNoRhuGUfAkxsG6cKZYKpPL4nmvfNWY59JJlsBna_SxYivLe7mhQXeplpmZqSb3wZa3JOl_Kr3Pfv1sJnaccz7JhIgFBdHmy4sc3S4t9mAF4K6loyA9vIDczHBKU9pljW29EbEV6cDcMQ1uZNQr0AgChnElDsOOVqNGtgpP0NLWRgGfj2iNkA_gEu6NJ4lArkFJT7aKMOcJC73FbrOhsKn9xFXl_HrRv9cX5gsSRBmVssIlPlKcZZE7XJ0mHi1ETcR2QXbQ6PJM2uFP4fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اسکلۀ صیادی بندرعباس
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464681" target="_blank">📅 08:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464680">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09fc9366f5.mp4?token=ITL8y-surme4sNITJX-3D6U_70Wj-yXPWGK5ojjc_pkTULaAD6RSqGbff2lA9DExe-Q9n2woNqfiRVGd0Vaim3KOCWIpkBOp9K76QKi4jOcT7AGEb0WaCBzQOG5MvKiBRxaZ0qyiIelJgNZF2P4e9tOjqUD-kO70LyAKGIAWXF7JG8MRPpJVtEF__jHCBu0E8QVYIZ_6af4ivDv5beTyvi6HFW9-q_8qPn15qosf3YO9fUiorfvXgdSWgfaTat_EFWttEMQXu7bvAWxOoNEIvXZ03m57ftf19kIFDYGlF8tjBtj9tOizIQxvbBDwMUCMc0YvarJnZAuQtfwE_WvEEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09fc9366f5.mp4?token=ITL8y-surme4sNITJX-3D6U_70Wj-yXPWGK5ojjc_pkTULaAD6RSqGbff2lA9DExe-Q9n2woNqfiRVGd0Vaim3KOCWIpkBOp9K76QKi4jOcT7AGEb0WaCBzQOG5MvKiBRxaZ0qyiIelJgNZF2P4e9tOjqUD-kO70LyAKGIAWXF7JG8MRPpJVtEF__jHCBu0E8QVYIZ_6af4ivDv5beTyvi6HFW9-q_8qPn15qosf3YO9fUiorfvXgdSWgfaTat_EFWttEMQXu7bvAWxOoNEIvXZ03m57ftf19kIFDYGlF8tjBtj9tOizIQxvbBDwMUCMc0YvarJnZAuQtfwE_WvEEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکات نمایشی آریا مام‌عبدالله و محمد سعیدآبادی در فینال ترامپولین  @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/464680" target="_blank">📅 08:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464678">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a8898d3d.mp4?token=RU3Q9_rgw7OlJrozNOB0OqsmqiJ_Tpqa895nDtAtfbUs6yuDH66EtOs9hfQTUEOCR99tLV6a8SMmTHRfEftwWh9OCjXQQgQUYbi1px-CFUC1lPRZEOPfJFNj6RMhQZuG8S08z7FLA_hTo3wfGqxipX9lUTuDoesTP6ccaxe5BXZtU8PPd7iyprkQVhT86xLW-7dAOtfU4Xc0-o6DIrqIZw-vF03Du4-7kSnlKYZGclB14FXFU68A0RRTP_EDd4kx1VN-FVnEqLDmPQcBllan5ufBcNfAonNAozIuCvfAXOEDmFB7901Tgc8HhQoVGa2517jRcQt0UHUQWOJwPkSkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a8898d3d.mp4?token=RU3Q9_rgw7OlJrozNOB0OqsmqiJ_Tpqa895nDtAtfbUs6yuDH66EtOs9hfQTUEOCR99tLV6a8SMmTHRfEftwWh9OCjXQQgQUYbi1px-CFUC1lPRZEOPfJFNj6RMhQZuG8S08z7FLA_hTo3wfGqxipX9lUTuDoesTP6ccaxe5BXZtU8PPd7iyprkQVhT86xLW-7dAOtfU4Xc0-o6DIrqIZw-vF03Du4-7kSnlKYZGclB14FXFU68A0RRTP_EDd4kx1VN-FVnEqLDmPQcBllan5ufBcNfAonNAozIuCvfAXOEDmFB7901Tgc8HhQoVGa2517jRcQt0UHUQWOJwPkSkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صعود تاریخی ترامپولین مردان به فینال بازی‌های آسیایی ناگویا
🔹
آریا مام‌عبدالله با امتیاز ۵۷.۷۴ و کسب رتبۀ پنجم، و محمدسعید آبادی با امتیاز ۵۳.۸۶ و کسب رتبۀ هشتم، جواز حضور در فینال را از آن خود کردند تا نخستین فینالیست‌های تاریخ این رشته از ایران باشند.  @Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/464678" target="_blank">📅 08:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464677">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921f1bf341.mp4?token=aDDhOzpuMwF4XYAZIOBYZh80EEgSZRkCle1Ts9_R5IwDV6W6nT21jrYilfnu0IzQ0lEAPWCRP0wV9eW6yGq6FnQ2E3nUavDn5OHKRPCYc1GDrs1WhkiPhNovjySA4RrJ3938Ot_BffDbnO39wD4sOKH0dISwMUx_Uu457JqyOzfwfHSpxSOGgGzz4pCRDjftndl-vLteZEJnJb0C7B1WDrh4VTX5gu0vzzHvw1lHDTt-GsIjxWCxNVb9FeY6yJkfro5vl1Q9DAjHhUg3anGlBh2AgPHkIiwYbSQ2_NqZZPeuXh-wS8Z94vxaDgnoOog8RUp2cZNkB77JLuVpwYg7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921f1bf341.mp4?token=aDDhOzpuMwF4XYAZIOBYZh80EEgSZRkCle1Ts9_R5IwDV6W6nT21jrYilfnu0IzQ0lEAPWCRP0wV9eW6yGq6FnQ2E3nUavDn5OHKRPCYc1GDrs1WhkiPhNovjySA4RrJ3938Ot_BffDbnO39wD4sOKH0dISwMUx_Uu457JqyOzfwfHSpxSOGgGzz4pCRDjftndl-vLteZEJnJb0C7B1WDrh4VTX5gu0vzzHvw1lHDTt-GsIjxWCxNVb9FeY6yJkfro5vl1Q9DAjHhUg3anGlBh2AgPHkIiwYbSQ2_NqZZPeuXh-wS8Z94vxaDgnoOog8RUp2cZNkB77JLuVpwYg7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا می‌توان از ابتلا به آب مروارید چشم پیشگیری کرد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/464677" target="_blank">📅 08:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464676">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هوای پایتخت همچنان ناسالم است
🔹
شاخص کیفیت هوای امروز پایتخت با قرار گرفتن روی عدد ۱۰۵، همچنان در وضعیت ناسالم برای گروه‌های حساس است.
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/464676" target="_blank">📅 07:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464675">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg-NRjpGGmm6CTC2zNMwQCrNclivE8TVjmC5Xvzn7A6J2yECL9PGAo2VJeWQ47mwk457IkMkSfJUIxsodFDkrmvwRcPYPrjo_n9FhV9qxtUvoU67xWTs8lblQLcGnDjm9mPpRRjwK83kPzr4Tsk1b2Ip4X8lerim9SOfPnRVjPQpfTl7Rk83zNl4dldWAyEvtJ7TspdC_72C3nB88IltJNT0j3BOng1pUYl2ZApBY5a_W8l70VvZrUP7iy3DniNBG6dbUw-Xj3yoddnNPG9wDbsEN5riaErB8bnxlC2yJ1S4yO9VqKl9-kEVSvLdlYnxrUb-EazbBIB9-36kv-6VUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود تاریخی ترامپولین مردان به فینال بازی‌های آسیایی ناگویا
🔹
آریا مام‌عبدالله با امتیاز ۵۷.۷۴ و کسب رتبۀ پنجم، و محمدسعید آبادی با امتیاز ۵۳.۸۶ و کسب رتبۀ هشتم، جواز حضور در فینال را از آن خود کردند تا نخستین فینالیست‌های تاریخ این رشته از ایران باشند.
@Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/464675" target="_blank">📅 07:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464674">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240a3a3a6a.mp4?token=R2FY998xc4EJ_7s5JuLKpT25_4EFf7W0TdGEAy1Fufx2SfpX3hW-k6YAYjD4Irh0hHKS9pbXi5MyPrUJqEbIH9SIxE9R7kVslq69fnZJMmhE0wu7QFe9kfeuCbvHBJ6tx36LShlJdpGb2Sd-6xRtGICw7ouyO4NOQlKV1a_a7cJVxXM8qqXIa45NzSgSg0H1KMSgrihuOMxYkIiAgtRh_QWZoad-FdvdbbsABaeL1vYYAsTXj1lXpUTwxjhyDCH-SLgTeRYs5UrMg7PfvRg8t9ChOEuQ8NU1uf6sRHYm3C0c1-Aq1-qBc1_DEHmvrx6Q6wDLDGLnAUE4R8QSVKETyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240a3a3a6a.mp4?token=R2FY998xc4EJ_7s5JuLKpT25_4EFf7W0TdGEAy1Fufx2SfpX3hW-k6YAYjD4Irh0hHKS9pbXi5MyPrUJqEbIH9SIxE9R7kVslq69fnZJMmhE0wu7QFe9kfeuCbvHBJ6tx36LShlJdpGb2Sd-6xRtGICw7ouyO4NOQlKV1a_a7cJVxXM8qqXIa45NzSgSg0H1KMSgrihuOMxYkIiAgtRh_QWZoad-FdvdbbsABaeL1vYYAsTXj1lXpUTwxjhyDCH-SLgTeRYs5UrMg7PfvRg8t9ChOEuQ8NU1uf6sRHYm3C0c1-Aq1-qBc1_DEHmvrx6Q6wDLDGLnAUE4R8QSVKETyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پادگان آموزشی جان‌فدا در پایتخت افتتاح شد
🔹
در نخستین مرحله از طرح جان فدا، اولین مرکز آموزشی جان‌فدا در میدان امام حسین(ع) تهران افتتاح شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/464674" target="_blank">📅 07:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464673">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شکست تنیس دوبل مردان در گام اول
🔹
کسری رحمانی و علی یزدانی در دور نخست تنیس دوبل مردان، نتیجه را ۲ بر صفر (۶-۴، ۶-۴) به حریفان چینی واگذار کردند. @Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/464673" target="_blank">📅 07:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464672">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔸
کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۷، ۸ و ۹ شارژ شد
.
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/464672" target="_blank">📅 07:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464664">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3QtkCm5jkfKejkQOyho9oCX84SpqGqDALKAn4yQVjWFhXUgtCmfL4E_B-hhp-JQmTkJCRY0EPmg8q1m87ywRbaWiRYy1x68la0EStf30hnvr_BObr7oEujPE6pzgu7R_Yb7YWHKyw1R-4fZ4N08438E9l-O_h2I4rgIE2x7g78GtQAFW1G1xVSW1rVf1TcI4RCNAPl0UL-oFG4FkY6oA1GxALkbkVnZ9oYXfq6th3P4jiMuzcn9MZDCe_zEPS-QdO3rMj_Ah5LAK1JBGPy07eKR2UsNqrikSsxktCPxUJk8jn2V8TBJUgjUTEVIsbGqshOLtYn_qs1FC67mH-dVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سالمندان امسال به مدرسه می‌روند
🔹
شهرداری تهران: امسال درحال طراحی برنامه‌ای هستیم که سالمندان وارد مدارس شوند و به‌عنوان «زنگ خرد و تجربه» با دانش‌آموزان ارتباط برقرار کنند تا تجربه و دانش نسل سالمند به نسل جدید منتقل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464664" target="_blank">📅 07:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464663">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آذرپیوند به یک‌چهارم نهایی کوراش صعود کرد</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/464663" target="_blank">📅 06:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464662">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4iZ0oSRYUwmsce4i3SCT97k8qFbzHeCdysk1s3ugsTuq8u5P2_nzf-fMQi8DPz_xV26qDGAH2pjPtNUq3hTqoU9Ina_iEKjGbry1m-84WzKuzdaRH-1yzNuRTWuZWDLBF0PggV-fKTSUHlGbsZgyxtuGfLW_Bd3WZJOr9unsmt4z9HsbKzO1dCXY_kKDkzLtNFNpRgX9nyHL53Q1nkGFxuF7BkJkBYqe9t71F26RlOjJDcqRmYWnWsL6q0sckbqFtgxAVoAXvH5qDQHlvXEqQ0_mwCUj3b4UJ53t9fufzqJTYDRHDRHIop4rqyjYVaTQEGTw8iIERpVqILFK-5Ouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به گدایی رأی افتاد
🔹
در حالی‌که یک‌ماه و ۸ روز به انتخابات میان‌دوره‌ای کنگره مانده است، ترامپ به سبک خاص خود با کنار هم قرار دادن ادعاهای بزرگ، از شهروندان آمریکایی خواست به او و حزب جمهوری‌خواه رأی بدهند.
🔹
ترامپ مدعی شد که شاخص‌های مختلف اقتصادی آمریکا به بالاترین سطوح تاریخی خود رسیده‌اند اما رسانه‌ها از پوشش این دستاوردها خودداری می‌کنند.
🔹
ترامپ پس از دستاوردسازی‌های عجیب و غریب و در حالی که پیش از این مدعی شده بود انتخابات برای او اهمیتی ندارد، نوشت: «در انتخابات میان‌دوره‌ای به نامزدهای جمهوری‌خواه و "ترامپ" رأی دهید. ما آمریکا را دوباره باعظمت کرده‌ایم».
🔸
در حالی‌که ترامپ از موفقیت اقتصادی سخن می‌گوید، داده‌های اخیر نشان می‌دهند فشار هزینه‌ها همچنان مسئلۀ مهمی برای اقتصاد آمریکاست.
🔸
در این راستا هفتۀ گذشته آسوشیتدپرس گزارش داد تورم در ماه اوت افزایش یافته و رشد قیمت انرژی، مواد غذایی و کالاهای مصرفی فشار بیشتری بر خانوارها وارد کرده است. هم‌زمان نرخ وام مسکن ۳۰ ساله به ۶.۹۵ درصد رسید که بالاترین سطح در بیش از ۱۸ ماه گذشته بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464662" target="_blank">📅 06:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464661">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تیم میکس تیراندازی آمادۀ تقابل با کرۀجنوبی
🔸
بیتا عاشق‌زاده و میلاد رشیدی در یک‌هشتم نهایی میکس تیراندازی با کمان، بنگلادش را ۱۵۸ بر ۱۵۴ شکست دادند و به یک‌چهارم نهایی رسیدند.
🔹
تیم میکس ریکرو با ترکیب مبینا فلاح و محمدحسین گلشنی در یک‌هشتم نهایی ۶ بر ۲ مقابل…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/464661" target="_blank">📅 06:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464660">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd3qxrB59qiOUYh9Y8BRBLLRblN476OAaSsYsPgQ_VNtZU-yZmS2qMImAdmIM_xCzKy9vh-b1W5Z3oKXX1pMrlV2thJ0tVsiVqYjGWv8Pmx7sXST6-8EK2kNrpVbwgLKxYqH6UqxB9RtqaXhzdljP_KqVpMYQq6ofU8SL5LboS2zcckmP63iB1QtCHppHXLAu4Zesf_H6cI83sVzxVk2x2_l5CUsB3rbq0P7dwEdyIoTUGEbzKwmI4wealOYuvGiUMOFDxLbwoKOztcTddUYL4yZYdswAoQLflwE7ZJH8XxjiYBVYrlJukJm6vuGxhKumjyEXF9vSMyMFEFqgkIzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع بی‌‌دردسر والیبال ایران در ناگویا
🔹
تیم ملی والیبال ایران در نخستین دیدار خود در بازی‌های آسیایی ناگویا، بامداد امروز مقابل قرقیزستان به میدان رفت و در دیداری یک‌طرفه با نتیجۀ ۳ بر صفر به پیروزی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/464660" target="_blank">📅 06:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464659">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5CJJei7PBWh6o3k32phOTi9fCtb6V87TWfDtCSe_wI1ZftpeRlfKquJk54P9bW3gy4j5XXEfJQGMjKrhSaROd9PeYG4fZhQbrLr8C56gQfXqg_Mc6j_GVX90YoFznLQnTBDObsFGnbe-DwuOW_W-nS91SsccwBXTlOg5zd4q_JthJL71lwNl2lMTiQDL2n_-DC43mmAq5TtHjb6hc6SM_zPJKYzOfxpbV_f3zl4wTgzk08-pW_7sTUdlixoNuQmEKs3mwKYz5VKdeqIgRRXcRifJWE5dzZk8vjnfmmAYhWxXhtQQnPGlQ6wWIMykrHg-Hab630L8nMJE-052sY2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست تنیس دوبل مردان در گام اول
🔹
کسری رحمانی و علی یزدانی در دور نخست تنیس دوبل مردان، نتیجه را ۲ بر صفر (۶-۴، ۶-۴) به حریفان چینی واگذار کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/464659" target="_blank">📅 06:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464658">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کمیتۀ ملی المپیک پاداش بازی‌های آسیایی را به فدراسیون روئینگ واریز کرد
پاداش ورزشکاران به شرح زیر است:
🔹
کیمیا زارع، دارای مدال طلا و نقره: ۴ میلیارد تومان
🔸
زینب نوروزی، دارای مدال طلا و نقره: ۴ میلیارد تومان
🔹
فاطمه مجلل، دارای مدال طلا و برنز: ۳.۴ میلیارد تومان
🔸
مهسا جاور، سها فخری، ساقی ملکی، هنگامه کامیاب، امیرحسین محمودپور، دارای مدال نقره: هر نفر ۱ میلیارد تومان
📝
همچنین به کادر فنی ۵۰درصد پاداش ورزشکاران، معادل ۸.۲ میلیارد تومان تعلق می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/464658" target="_blank">📅 06:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464657">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آذرپیوند به یک‌چهارم نهایی کوراش صعود کرد؛ عیدی‌وندی حذف شد
🔹
طاهره آذرپیوند در وزن ۵۷- کیلو پس از استراحت، حریف هندی را ۳ بر صفر شکست داد و به یک‌چهارم نهایی رفت.
🔹
پردیس عیدی‌وندی پس از استراحت، به حریف فیلیپینی باخت و حذف شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/464657" target="_blank">📅 06:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464656">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90240f4664.mp4?token=HEYJaOlNmUQD3lwGCTEKpLatTyUpvj2V-rfbXBy582vYmqmMCjM0XOHifPUqScTnPmJ_KkC9xlUW2Jh1C2NzJosT10DzVu8dBGyATsEsWJd04NA1Y2HQQzl2SJwoepCpKeDxE0fZ7Bbvx905DVFcfxMDSrF3rum7itdKtsYRnjE_tZ6C3TTzywGs8Z_oAy_km3pHtOtvr2HfOmX5CCPPkcKbMgrN1k2ADKz3XGEjRz9VLXoJf-xBw2-CarYD57JiNj3MwWwlyppGqzSQusfNgahu8mZhMQVNHN6AGJLMlVrMrfS03dpZbgwuL7XTryh2FGwXdfyrQ7iyGRYDLispBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90240f4664.mp4?token=HEYJaOlNmUQD3lwGCTEKpLatTyUpvj2V-rfbXBy582vYmqmMCjM0XOHifPUqScTnPmJ_KkC9xlUW2Jh1C2NzJosT10DzVu8dBGyATsEsWJd04NA1Y2HQQzl2SJwoepCpKeDxE0fZ7Bbvx905DVFcfxMDSrF3rum7itdKtsYRnjE_tZ6C3TTzywGs8Z_oAy_km3pHtOtvr2HfOmX5CCPPkcKbMgrN1k2ADKz3XGEjRz9VLXoJf-xBw2-CarYD57JiNj3MwWwlyppGqzSQusfNgahu8mZhMQVNHN6AGJLMlVrMrfS03dpZbgwuL7XTryh2FGwXdfyrQ7iyGRYDLispBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف تیم‌های کامپوند مردان و زنان
🔹
تیم کامپوند ایران در یک چهارم نهایی به مصاف تیم کره‌جنوبی رفت که ۲۳۹ بر ۲۳۴ شکست خورد و حذف شد.
🔹
کامپوند زنان با ترکیب گیسا بایبوردی، بیتا عاشق‌زاده و شیوا بختیاری در مرحله یک هشتم در تیر طلایی مقابل تایلند باخت و حذف…</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/464656" target="_blank">📅 06:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464655">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxYi1aBpAGI8y3dzD7Cd1jfLt46HJhY40EjQT6bPFV0qFAEkiSryuCoInivOnJ4QQO86RQfhfsGQFv-v0OS1sLBVLCKo9WzXrfLjHF6FEcxim2UNTXR5xqcGbJ-fhCo3Tm1h8yWYTdOwUlTp4Mnj_3Yxbzn32AA8vms5jkTK77vfcnQWBhNPXAlhW4YN7PzI5yvyVDK-chlPflmSiI5kVdIBFMECgRs7uZES-zeHcmlt9Cu1F1CLaNi0Zi_-jdIYYUi4dMhSnJWSPQyDeipi-_yH3yd6yjzcqLeCfMDvZO6KTl6ePXBuDPM0_eUijSqLe1XOgsbQz_ZaBlvAG2E4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس اعلای اسلامی عراق: هرگونه همکاری با دشمن ایران حرام، و شکستن محاصرۀ ایران واجب است
🔹
همام حمودی، رئیس مجلس اعلای اسلامی عراق محاصرۀ ظالمانه و غیرانسانی تحمیل شده توسط ترامپ بر پروازهای ایران را محکوم کرد.
🔹
او گفت این محاصره مغایر با قوانین بین‌المللی و قانون اساسی عراق، به‌ویژه مادۀ ۸ است که بر حسن همجواری تأکید دارد.
🔹
حمودی تاکید کرد هرگونه مشارکت در محاصره و تجاوز نظامی، اقتصادی و رسانه‌ای علیه ایران حرام بوده و شکستن این محاصره واجب است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/464655" target="_blank">📅 05:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464654">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE8f935FQ0HU71YUKI2swAIgZaB0KCufX52x0r4pWLlDZGSDBpfQ9qCpvwUEzYt3ucfBBOlQwyAP3g1xzFG7LpHtc6A7YH7X1GfWsdBdd3YrpyQnVIE5TER3lpim4urhid-iUVokf6GWnYfwviKEmnRP1AHsRiUtc_NELCdLEoZy3hiRIvfkzWDk-_Exnzo5RFjDvX6ifjVDl2yoNfCp_RpGXEgssgrnvHQlVbglNKWMOp7zU7j50PdQEGaMj0kr8GsJLSRjB2oWVW8ILdsYKnhMA3m9UGzSW3zN2YeIEp6SwnfrEgSFvz3AF-coGZlyINaPwvXgXhenl0vpwLEAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ قاطع وزیر خارجۀ ایسلند به توهین نتانیاهو در سازمان ملل
🔹
وزیر خارجۀ ایسلند در سخنان خود در مجمع عمومی سازمان ملل در پاسخ به نخست‌وزیر رژیم صهیونیستی گفت: بزدلان اخلاقی آن رهبرانی هستند که بارها قوانین بین‌المللی را نقض می‌کنند.
🔹
نتانیاهو در جریان سخنرانی خود در مجمع عمومی سازمان ملل زمانی که با حجم انبوه نمایندگانی که سالن را ترک می‌کردند روبه‌رو شد، آن‌ها را «بزدلان اخلاقی» خطاب کرده بود.
🔹
وزیر خارجۀ ایسلند در سخنان خود گفت: «ما واژه‌های بزدلان اخلاقی را از این تریبون شنیده‌ایم. به نظر من، بزدلان اخلاقی آن رهبران جهان هستند که از نشستن پای میز مذاکره برای صلح عادلانه و پایدار خودداری می‌کنند. کسانی که دسترسی به کمک‌های بشردوستانه را برای مردم نیازمند انکار می‌کنند و بزدلان اخلاقی آن رهبرانی هستند که بارها قوانین بین‌المللی را نقض می‌کنند و به آن احترام نمی‌گذارند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464654" target="_blank">📅 05:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464653">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">حذف تیم‌های کامپوند مردان و زنان
🔹
تیم کامپوند ایران در یک چهارم نهایی به مصاف تیم کره‌جنوبی رفت که ۲۳۹ بر ۲۳۴ شکست خورد و حذف شد.
🔹
کامپوند زنان با ترکیب گیسا بایبوردی، بیتا عاشق‌زاده و شیوا بختیاری در مرحله یک هشتم در تیر طلایی مقابل تایلند باخت و حذف شد.
@Sportfars</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/464653" target="_blank">📅 05:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464652">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGPvtck52SrSqterEtS85bg0tclnYAL6m2E-LlzXL1Lt9o6ZoslBx_N0g-cr8cimFAnnsTnDi01vRLoh8ke1dF_E9EASb40UYAgU6xHitom_mENw79pLzp6YXxgrCD5v2QOf0HgAQXOycgy6Tdkw4HMRI0WsKdP5PVtiMGMdn3SsmGd4_DMcsxftOViip43FGFc05Mx5XJqRw7-lRKjvnPNvlxZBRtVahjpwPOqvDfKZh4C8dAlNy9WRuEfdQM13a-tJ4jRdhtuVJovC-FWnmQbUnaGLD-zk5ssM92qrHASvbrc-XmLwsSiXV1pqbHfbgvvLhge00jNlQea-Oq4Hww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیک‌تاک دادگاهی شد
🔹
برای نخستین‌بار در آمریکا، یک دادگاه در آلاباما موارد مربوط به آسیب تیک‌تاک به سلامت روان نوجوانان را بررسی می‌کند.
🔹
آلاباما می‌گوید طراحی و الگوریتم تیک‌تاک کاربران جوان را به استفادۀ مداوم سوق داده و آنها را در معرض محتوای آسیب‌زا قرار…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464652" target="_blank">📅 04:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464651">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObFwBR4cMfumj1NJmFqAxlmQRPq5e_e1pROH2txCzrr0txv-FO3Cg6gnmv0GsHmTjCXOPXX5dU6b0sHjH-v9v70iJ_BXMBa_liNVdaI1QZq245Y372G1SnEHGvS60NOUGqC5_NiDQ0TPSFw0_urpokpVzjyJZKywIFEjxPb3VAzrP8Oa9-53d6f8XzDpjKiOf2kWueB83YxcZpy487Q3TKpHVQg_CdhZ9gSu4TJaJkN5zY86dVJjBqjaDD_OSWFIbK-eYM4kuiEL3pSNCGAzhdnqHMr-XH0JjKNW8eNcSFe8f18wCVfyp0TqYBWzyVeNsj2SdK4fgFKNQ8p_x7cczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع گازوئیل اروپا؛ تازه‌ترین ضربۀ جنگ علیه ایران بر اعتبار آمریکا
🔸
تهدید دونالد ترامپ، رئیس‌جمهور آمریکا، برای کاهش صادرات گازوئیل به خارج از کشور، بر خلاف وعده‌اش دربارۀ غرق کردن جهان در سوخت‌های آمریکایی است و خطراتی برای این کشور به‌همراه دارد.
🔹
به گزارش پولیتیکو، کارشناسان انرژی می‌گویند که این اقدام تنش‌ها بین آمریکا و اروپا را تشدید می‌کند و در عین حال اعتبار آمریکا را به عنوان یک شریک تجاری به خطر می‌اندازد.
🔹
آن‌ها افزودند که این اقدام می‌تواند کشورها را وادار کند که به‌دنبال تأمین‌کنندگان دیگر بروند و در آینده، توانایی ترامپ را برای استفاده از انرژی به عنوان ابزار چانه‌زنی محدود کند.
🔹
یک مشاور دولت ترامپ که نامش فاش نشد، در این‌باره گفت: «این به اعتبار ما آسیب می‌زند. کل فرضیۀ سلطۀ انرژی این بود که ایالات متحده بتواند سوخت متحدانمان را در سراسر جهان تأمین کند.»
🔗
شرح کامل گزارش را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/464651" target="_blank">📅 04:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464650">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd5f86386f.mp4?token=mN0XltNvIhuP4dlC652U2AZHAV-hbLca_uEg8KLHhnFD5h5YHLotvDuJVaQ6aUgXLnMY7M8oZVaa1gmz5CNyU_EwCQHxOnUrfYYk08iEWedrs_NA9wgu3xt3qulhA0th_gVZrAfC7oT10vg6bcOkVp1SAhR-7UQKXQ5Ce1XBD_MOpr_4hzweJTYbj2FNEvNGsI0RO_0NKhgNL7BfNQwqxvd6ozlqTWr2jNoIZoZZnENzYOzra7y--LJcn8fYma6ELNISszL_BTZtDB4RuEURVP9yayKUZDBLu3HQi4vhrAUQPMVN0aJbxbnCRpJ-CztanjaFwCV3fwLRnghidmN48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd5f86386f.mp4?token=mN0XltNvIhuP4dlC652U2AZHAV-hbLca_uEg8KLHhnFD5h5YHLotvDuJVaQ6aUgXLnMY7M8oZVaa1gmz5CNyU_EwCQHxOnUrfYYk08iEWedrs_NA9wgu3xt3qulhA0th_gVZrAfC7oT10vg6bcOkVp1SAhR-7UQKXQ5Ce1XBD_MOpr_4hzweJTYbj2FNEvNGsI0RO_0NKhgNL7BfNQwqxvd6ozlqTWr2jNoIZoZZnENzYOzra7y--LJcn8fYma6ELNISszL_BTZtDB4RuEURVP9yayKUZDBLu3HQi4vhrAUQPMVN0aJbxbnCRpJ-CztanjaFwCV3fwLRnghidmN48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): برای حرف دیگران منظور خوب پیدا کن
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/464650" target="_blank">📅 04:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464649">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZvG61VYaN12GOPOF3ar5nvhmAZH6QxwqUcbf05iJPZI_nXI0Ip4YeMhhW8E9-PdCIvvVAMZRaHfAbwGaBBUBJ2qxem3wcCwkAa7VfT2Lx0SFAFN7BtZffV0RE6wgiZXVPj8x-V3nxx7ZXYWg86ffS-6LJWbQzfJn6X5BjAia_3ZMsnljo2RpGdTlN50pCYhk2MItBHQPPYnzravmYIJl4GHu1YXMtL2iOHNccbSRIPYHTd-lFkaJ3XLjJESFNfGjOw0DorjU_QvIqBipRP9e5UFsHWZrvQs1_NmcNHcxBVjAsH3QjFL6siYbI1Tga6vnWYxhoCZ-zOsdCBPLoSt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افسر فرانسوی: تنگۀ هرمز به بن‌بست ترامپ تبدیل شده است
🔹
افسر سابق ارتش فرانسه با اشاره به ناتوانی آمریکا در تأمین امنیت عبور کشتی‌ها از تنگۀ هرمز در برابر پهپادهای ایرانی گفت: این آبراه به «بن‌بست ترامپ» تبدیل شده و ایران از تنگۀ هرمز به‌عنوان اهرمی قدرتمند در برابر واشنگتن استفاده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/464649" target="_blank">📅 03:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464648">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کار طلافروش آنلاین به شورای عالی امنیت ملی رسید
🔹
پلتفرم فروش آنلاین طلای میلی‌گلد در نامه‌ای به محسن رضایی، دبیر شورای عالی امنیت ملی، خواستار صدور دستور فوری برای رفع محدودیت دسترسی به طلای کاربران در خزانه‌های بانکی شده است.
🔹
این پلتفرم می‌گوید محدودیت‌های ایجادشده از سوی پلیس امنیت اقتصادی و برخی نهادهای مرتبط، امکان دسترسی به بخشی از ذخایر و ایفای تعهدات به کاربران را با مشکل مواجه کرده است.
🔹
در روزهای اخیر شماری از کاربران میلی‌گلد در فضای مجازی از تأخیر در تسویۀ ریالی و دریافت طلای فیزیکی خود گلایه کرده‌اند. برخی کاربران نیز با طرح ادعای «خالی‌فروشی» دربارۀ میزان واقعی طلای پشتوانۀ معاملات این پلتفرم ابراز نگرانی کرده‌اند.
🔹
این نگرانی‌ها در حالی مطرح شده که طبق ضوابط بانک مرکزی، سکوهای آنلاین باید معادل تعهدات مربوط به طلای فروخته‌شده را در خزانه نگهداری کنند و طلاهای ذخیره‌شده نیز ظرف سه‌ماه به شمش استاندارد با عیار حداقل ۹۹۵ تبدیل شود.
🔹
با این حال میلی گلد مدعی است سازوکارهای حاکمیتی و بوروکراسی موجود، دسترسی این پلتفرم به ذخایر بانکی را محدود کرده و در نتیجه تحویل طلای کاربران با مشکل مواجه شده است. این شرکت پیش‌تر نیز اعلام کرده بود طلای کاربران در خزانه‌های بانکی نگهداری می‌شود.
🔸
حالا با توجه به نگرانی‌های اخیر دربارۀ دسترسی کاربران به طلای خود و ادعاهای مطرح‌شده دربارۀ پشتوانۀ معاملات، اتصال هرچه سریع‌تر تمامی پلتفرم‌ها و گزارش برخط موجودی و تعهدات آنها به سامانۀ ناظر، بیش از گذشته اهمیت پیدا کرده و می‌تواند بخشی از نگرانی کاربران را برطرف کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464648" target="_blank">📅 03:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464647">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464647" target="_blank">📅 02:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464646">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d41660dc6.mp4?token=LJh67KJgNlj96NbMPMZ2uklSaBUYC7OAMwSSXXCCm72KAqkcfsTn_bO_LVnHyxHQUdo0UxyYY9B5gsOMN3obQTb9eIequ5O73FWuetqjd68CiKjMfl-l2W5Dq_azrmZFIQE2usADudy2-GlulJ2Bd3OpZQILfYYQoXnOBODrphTuPNy9a2j15iT6TyUizeYAmsrm9SED93_bzi0qoGSsI8XPIO6unMAVPb3XbRW6aVcZnfRFArx7GWv-0By8vtyPHpCL5prKO26UORG1crn87FNv8Wyb5jqZwuFiCirMG8LSIw3FFr4X_oSA9fApp6CPRGvv5l6YCATsVBY9EWc5eV-n20Ow-Xr0CDqPKEIHaU7bn4_ivH_imuG5LsNwqFU5FAXkZhpXvWkhiBgHt7uD18ssXjLrQ2OWSauRQddJqbqpjxZl08rj8s3Dfz8fKeUvqdC0qTGFemGi05RQsCzSrZkEuFAJgjPeRfLRNSl1eq4KiKr-9Wlk1IaaQ7sOLmu_eBvGqGKyupGNZt03Cku-3PkXrhThnYIXZ6khCisctL99uEQoh94s0bLh7TX-FqPDdDG1Lwx13kXjMnr6KekNYT0Y1BdyPIzpZixOiT4MCUZWkBmBV_lsXAKNAPiw9R-kOc-xOCjtzKMao3YreGRYTVrNq2JmasXHVIaA4HT1_dM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d41660dc6.mp4?token=LJh67KJgNlj96NbMPMZ2uklSaBUYC7OAMwSSXXCCm72KAqkcfsTn_bO_LVnHyxHQUdo0UxyYY9B5gsOMN3obQTb9eIequ5O73FWuetqjd68CiKjMfl-l2W5Dq_azrmZFIQE2usADudy2-GlulJ2Bd3OpZQILfYYQoXnOBODrphTuPNy9a2j15iT6TyUizeYAmsrm9SED93_bzi0qoGSsI8XPIO6unMAVPb3XbRW6aVcZnfRFArx7GWv-0By8vtyPHpCL5prKO26UORG1crn87FNv8Wyb5jqZwuFiCirMG8LSIw3FFr4X_oSA9fApp6CPRGvv5l6YCATsVBY9EWc5eV-n20Ow-Xr0CDqPKEIHaU7bn4_ivH_imuG5LsNwqFU5FAXkZhpXvWkhiBgHt7uD18ssXjLrQ2OWSauRQddJqbqpjxZl08rj8s3Dfz8fKeUvqdC0qTGFemGi05RQsCzSrZkEuFAJgjPeRfLRNSl1eq4KiKr-9Wlk1IaaQ7sOLmu_eBvGqGKyupGNZt03Cku-3PkXrhThnYIXZ6khCisctL99uEQoh94s0bLh7TX-FqPDdDG1Lwx13kXjMnr6KekNYT0Y1BdyPIzpZixOiT4MCUZWkBmBV_lsXAKNAPiw9R-kOc-xOCjtzKMao3YreGRYTVrNq2JmasXHVIaA4HT1_dM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واردات سامسونگ و ال‌جی آزاد شد
🔹
سازمان توسعه تجارت ایران در نامه‌ای به گمرک اعلام کرد: با توجه به تصمیمات کارگروه ساماندهی مبادلات مرزی، واردات لوازم خانگی از مبدأ کره جنوبی دیگر با هیچ محدودیتی مواجه نیست.
🔸
با وجود آنکه تولیدکنندگان لوازم خانگی کره‌ای پس…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464646" target="_blank">📅 02:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464645">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d9a21acc.mp4?token=rwaV-MlJmDkLXTqQ5tW0EBvUSxmOcaT5sPQ2yX8rLh4ne9BuD-VkEdIVcx7htQBD2BgntwPvKt0DgcJhKV3fwWqeIPItzuPCS2Io8G1y__r1LFOYDv_e3WHW1j903LPhV6H2qGx1M2oLMKCjbO1EwjRNP2j4Ue4Ia-gE3pkNo3UoqUCvgitLbbmKuu3IBkJesZweCK9Mv4CLNHxBtHymsC28LvlH4uf_N0xwWYSwJ1DngJUvzvFl-qJb2BhR-BsVWPa2coJQtVGDSsraLcjGoh3Xng9MaT83sO681kttqxxzNdajZUmGwzJqlMHZXiVb8k5yi1mF1khIPW-1kMZsPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d9a21acc.mp4?token=rwaV-MlJmDkLXTqQ5tW0EBvUSxmOcaT5sPQ2yX8rLh4ne9BuD-VkEdIVcx7htQBD2BgntwPvKt0DgcJhKV3fwWqeIPItzuPCS2Io8G1y__r1LFOYDv_e3WHW1j903LPhV6H2qGx1M2oLMKCjbO1EwjRNP2j4Ue4Ia-gE3pkNo3UoqUCvgitLbbmKuu3IBkJesZweCK9Mv4CLNHxBtHymsC28LvlH4uf_N0xwWYSwJ1DngJUvzvFl-qJb2BhR-BsVWPa2coJQtVGDSsraLcjGoh3Xng9MaT83sO681kttqxxzNdajZUmGwzJqlMHZXiVb8k5yi1mF1khIPW-1kMZsPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر دیده‌نشده از شهید سید حسن نصرالله در ضاحیۀ بیروت
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464645" target="_blank">📅 01:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464644">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ab1fbf97.mp4?token=A5GrLyOWy6fI3Ady9hU67_5zXr-O_NonQ5kTBwiYIWGgBcGrDxTRA5itzQw_AxsKN4pth8SY3Hn3baGojG3aV7X3ely8yyAsUvNwRah_GZsUK2DvJCpa9t7xYZfLCF7DTdusufY4uj7bUxeTPyGje_cpqMJ0rVQaAYsYPBrVEVwmXDyS7QfICL7orTaD2g4JSvPshq2FvTGsMAFUHl-n_3iWDPBJOQJoKfFBVvod47we33llLPUCdcZXSHInflgCbIJ3z6NzzGancuCiRK8XgBBz0e71q31k9taJt2m7Xfqci5l6cHsZm0q3kK1hQB4kx6vtjqG5VdZRBnrlgsOulA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ab1fbf97.mp4?token=A5GrLyOWy6fI3Ady9hU67_5zXr-O_NonQ5kTBwiYIWGgBcGrDxTRA5itzQw_AxsKN4pth8SY3Hn3baGojG3aV7X3ely8yyAsUvNwRah_GZsUK2DvJCpa9t7xYZfLCF7DTdusufY4uj7bUxeTPyGje_cpqMJ0rVQaAYsYPBrVEVwmXDyS7QfICL7orTaD2g4JSvPshq2FvTGsMAFUHl-n_3iWDPBJOQJoKfFBVvod47we33llLPUCdcZXSHInflgCbIJ3z6NzzGancuCiRK8XgBBz0e71q31k9taJt2m7Xfqci5l6cHsZm0q3kK1hQB4kx6vtjqG5VdZRBnrlgsOulA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای اعتراض صنفی سلف دانشگاه رازی کرمانشاه چه بود؟
🔸
ظهر شنبه ۴ مهرماه توزیع ناهار در سلف‌سرویس خوابگاه پسرانۀ دانشگاه رازی کرمانشاه با اختلال و معطلی مواجه شد؛ اتفاقی که با واکنش اعتراضی شماری از دانشجویان و بازتاب در رسانه‌های خارج از کشور همراه شد، اما بررسی میدانی و شواهد عینی حاکی از ماهیت کاملاً صنفی این رخداد به دنبال تغییر فرآیند پیمانکاری و نقص فنی سامانه است.
🔹
براساس روال معمول دانشگاه، ساعت توزیع ناهار دانشجویان از حدود ساعت ۱۱:۳۰ تا ۱۳:۳۰ است. با این حال، به‌دلیل تغییرات اخیر در واگذاری امور تغذیه به پیمانکار جدید و ناهماهنگی‌های اجرایی، محمولۀ غذا با تأخیر و حوالی ساعت ۱۲:۴۵ به خوابگاه رسید. این معطلی طولانی در شرایطی رخ داد که دانشجویان برای حضور در کلاس‌های بعدازظهر نیاز به صرف به‌موقع غذا داشتند.
🔹
در پی این ناهماهنگی، تعدادی از دانشجویان در ورودی سلف‌سرویس خوابگاه در اقدامی نمادین، حدود ۱۰۰ سینی و ظرف غذا را روی زمین چیدند و خواستار رسیدگی فوری مسئولان شدند.
🔹
بررسی میدانی خبرنگار فارس حاکی از این بود، فضای اعتراضی کاملاً صنفی بوده و هیچ‌گونه شعار هنجارشکنانه، درگیری یا تنش فیزیکی شکل نگرفت. ماجرا تنها معطلی بچه‌ها بر سر نرسیدن به‌موقع ناهار بود و مباحثی که برخی شبکه‌ها دربارۀ بهداشت یا کیفیت غذا مطرح کردند واقعیت ندارد.
🔹
پس از این و در پی این ماجرا، معاونت دانشجویی دانشگاه رازی ضمن پذیرش مسئولیت این رخداد، از دانشجویان عذرخواهی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464644" target="_blank">📅 01:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464643">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f797003eb.mp4?token=dqatQm4NK5jV_xI3-AoYg6i3hfcj7N5pfsKNL9hWb0CbJ6zlQa_xA2xUxIh1kP4-WCt6AnhBEqVmt122y1cELFuF3jNqMS0sxu_kHp6H9AYioJMfupSGKfi_CAL40bF_49bOGNphiX_kyF6k4Zs7gaBJrBOskBX481d2MprlYVaMTC0DJRxZFXOMWsW2ajSma1i4JL_k2NlknOzBF74r-xU-rQAtRAo2ymeNCrEFQkHKRh729FohtYaE3WAhweXFzQL_t6Dx1BuTKnsOZ4F_9XsCfFImLXofafiSjiVvujd8pihs-Igvrkylyf0xjqFRtlIUvp50yyANun9NS1NXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f797003eb.mp4?token=dqatQm4NK5jV_xI3-AoYg6i3hfcj7N5pfsKNL9hWb0CbJ6zlQa_xA2xUxIh1kP4-WCt6AnhBEqVmt122y1cELFuF3jNqMS0sxu_kHp6H9AYioJMfupSGKfi_CAL40bF_49bOGNphiX_kyF6k4Zs7gaBJrBOskBX481d2MprlYVaMTC0DJRxZFXOMWsW2ajSma1i4JL_k2NlknOzBF74r-xU-rQAtRAo2ymeNCrEFQkHKRh729FohtYaE3WAhweXFzQL_t6Dx1BuTKnsOZ4F_9XsCfFImLXofafiSjiVvujd8pihs-Igvrkylyf0xjqFRtlIUvp50yyANun9NS1NXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پردۀ کوله‌بری در کردستان
🔹
ربایش، ترور و اخاذی گروهک‌های تروریستی و تجزیه‌طلب در غرب کشور از کوله‌بران
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/464643" target="_blank">📅 01:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464642">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfG-lJ0qHfQTxIXbMe46a8X6vIHvgK_tArq2fZzcJy2Cjr5ib4Gnk2Sb3EHN7aKqAjef__BO1xrK_MFpl9NYcSvbSxNFWJ1gfTfP8vrgql9o0a8FaQfGyoOaDzYgT6JPyl4vGZRURgzIz2eIZJ5UkhYzqLl7KMT5tsNNP-0l4IbknnuhRW-mQ7Pld7V_dxlAJlmKPBYfgtIgwGbK4bCZRGd6oDfqps9Z5pdwoTyJJ8hLvNw4mwYKhwbgKxSCvqOwOzxztLMxfxy8GZoccX0y_CW35ScSjJG1810WB4B6afpY0e4Df38OWgyosBrvPgGphXcs9-HM5jpMJoDFCM20kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هشدار نهاد مدیریت آبراه خلیج فارس به مالکان کشتی‌ها در خصوص الزام شناورها به تردد از مسیرهای نامعتبر توسط برخی چارترها
🔹
گزارش‌های رسیده به این نهاد مبنی بر اینکه برخی چارترها، شناورها را مجبور به تردد از مسیرهای نامعتبر می‌کنند. این کار علاوه‌بر ایجاد…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/464642" target="_blank">📅 01:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464641">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نیروی دریایی سپاه: اگر تنگۀ هرمز متعلق به آمریکاست، پس ناوهایشان کجاست؟
🔹
معاون سیاسی نیروی دریایی سپاه: اگر ترامپ تنگۀ هرمز را تنگه خود می‌داند، پس چرا ناوها و شناورهایش اینجا نیستند؟
🔹
اگر آمریکا مدعی کنترل تنگۀ هرمز است، فقط یکی از ناوهای خود را به این…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/464641" target="_blank">📅 01:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464640">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌ عراقچی: از شروط خود کوتاه نمی‌آییم؛ بازشدن تنگۀ هرمز منوط به محقق‌شدن این شروط است
🔹
شروط ما مشخص است و هرگونه حرکت روبه‌جلو برای بازشدن تنگۀ هرمز منوط به محقق‌شدن این شروط است و از آن‌ها هم کوتاه نخواهیم آمد.
🔹
اولین واکنش را از رئیس‌جمهور آمریکا دیدیم،…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/464640" target="_blank">📅 00:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464639">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
رئیس‌جمهور آمریکا اعلام کرد که پیشنهاد ارائه شده توسط ایران را که به موجب آن، تنگه هرمز ظرف مدت هفت روز، باز می‌شد، رد کرده است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464639" target="_blank">📅 00:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464638">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tz_2EQIodFy1nWk3Qw5qmsjbW_DJ4uuyKKT6dYgBzyLjtaQkWY0WgWQvNollXcciFm_fSJ3YN3slRL3uyt6ednYYhqc0NJ05xvHLNJep9u_-KKu33RtBIFCedPUlCsSLiZvrR_dGOKlkj0Iov1jmAiAhQLL8eWnwWzWzUIlZyga7ObHshnBCL4dYixF4iy-d-cXnbI9ZJ7TLJ7TjMEED4BLsoFCWIZfUa8ae3vZhcA-oL8i9DhCHzejKo1Bix41hF6JnYZ0smKPmJcLDZQsAboXBBO7fKKAYqOgUL1Q2NPv4mBAFhzTzNkt9s_xyNayL5kKb6If9UxyJ5iNg1bb2mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هشدار نهاد مدیریت آبراه خلیج فارس به مالکان کشتی‌ها در خصوص الزام شناورها به تردد از مسیرهای نامعتبر توسط برخی چارترها
🔹
گزارش‌های رسیده به این نهاد مبنی بر اینکه برخی چارترها، شناورها را مجبور به تردد از مسیرهای نامعتبر می‌کنند. این کار علاوه‌بر ایجاد احتمال وقوع خسارت‌های مالی و جانی برای شناور، مالک، کاپیتان و خدمه، عبور آتی آن شناور از تنگۀ هرمز را نیز با محدودیت جدی مواجه می‌کند.
🔹
در صورت احراز تحلف چارترها، این شرکت‌ها به لیست عدم سازگاری اضافه شده و عبور کلیه شناورهای مربوط به آن‌ها از تنگۀ هرمز با محدودیت مواجه خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464638" target="_blank">📅 00:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464637">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNY56bj6TsAEiTWsGdUNxny928syKGMqUkh0ZdvBoiIQ7BsdPpcfpQvrjEd4J_B_XJEgy3CS-9W85jTcnzzoL2yinyxtzEjOuUXgm5Gph2p-XNS1ExqpRB2hcTjlsybx00HbpFFRK9pDTRSdq2G1IrIgOdb6yjMTuzapBPUAHq-Co6bdvDTQuZIJgxg9d0bOOuYnuqo5-W5BphnjKjqBRO9ZvInAcq3B05OcaDtVs3eMR0XYT-gb1Mf4DqacrOPK3Bzo5NXrC-2CIss84UNYirAbw2z0mY4h2cyhgvR5tICovNndkrLDVAlZT6W-3B3C_XxuRAKux63FHe5n7oFsFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: احیای اعتماد به سازمان ملل، نیازمند خاتمه‌دادن به بی‌کیفرمانی عاملان و آمران جنایات شدید بین‌المللی است
🔹
وزیر امور خارجه در دیدار با خلیل الرحمن، رئیس هشتادویکمین اجلاس مجمع عمومی سازمان ملل: تحقق شعار «بازسازی اعتماد به سازمان ملل متحد» بیش از همه مستلزم توقف نقض‌های فاحش اصول بنیادین منشور به‌ویژه اصل احترام به حاکمیت ملی کشورها و منع توسل به زور مندرج در بند ۲ منشور، جلوگیری از استفادۀ ابزاری از شورای امنیت، و نیز خاتمه‌دادن به بی‌کیفرمانی عاملان و آمران جنایات شدید بین‌المللی خصوصا تجاوز، نسل‌کشی و جنایات جنگی ارتکابی توسط رژیم صهیونیستی است.
🔹
تجاوز نظامی آمریکایی-اسرائیلی که در روز ۹ اسفند ۱۴۰۴ در حین مذاکرات هسته‌ای شروع شد و تا امروز به اشکال مختلف از جمله محاصره دریایی و تحریم اقتصادی ادامه یافته است هیچ منطقی جز زورگویی و قلدری ندارد و وضعیت ناامنی موجود در تنگه هرمز نیز نتیجه همین اقدامات تجاوزکارانه و مداخله‌جویانه است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464637" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464636">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs1iBKhH3eYYPgjCw2IkwgsVujBhnebtqmI7IR_gkrVh2Ix-M_CtyWzo67h9b5EyYqbFIRtzJt6fOxFhLlDO6UzvHlEsJHdEsJ7vZwo2uHkmXHg4r9r6j8W4Ihz2zUbbN5HcQh_G5K1PhrzCSeVGzvAfkWOXzsqmj_0YlcLYICsRNmtnphsyipWOPkyaiLsXu4yKpGLXoguhc-cVgRmG0asTkak_tjaRXiRdubczHmxJboEMgPA15HMuKreMGj_GBzxykV0HyAK0Rc4olyd5u9U5M_GmZFprr0GGBkwJVwb0J5TpgQd_pWAk9dFqwGW6pmgV0WdF-TokqAlpotHfpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفره‌ای برای همه
🔹
حضرت ابراهیم(ع) در مهمان‌نوازی زبانزد بود و عادت داشت که تا مهمانی سر سفره‌اش نمی‌آمد، غذا نمی‌خورد. روزی یک شبانه‌روز گذشت و هیچ مهمانی نیامد؛ پس ایشان برای یافتن مهمان به صحرا رفت و با پیرمردی روبه‌رو شد.
🔹
وقتی از حال او جویا شد، فهمید که آن پیر، بت‌پرست و بیگانه با دین خداست. ابراهیم(ع) افسوس خورد و گفت: «ای کاش خداپرست بودی تا لحظه‌ای نمکِ ما را می‌چشیدی!» و او را مهمان نکرد. پیرمرد هم راهش را گرفت و رفت.
🔹
در همان لحظه جبرئیل نازل شد و پیام داد: «ای ابراهیم، خداوند می‌فرماید: این پیرمرد ۷۰ سال مشرک و بت‌پرست بود و ما روزی‌اش را قطع نکردیم؛ حال یک روز که سفره‌اش به تو واگذار شد، به جرم بیگانگی غذا را از او دریغ کردی؟!»
🔹
ابراهیم(ع) بی‌درنگ به دنبال پیرمرد دوید و او را بازگرداند. پیرمرد با تعجب پرسید: «علت آن رد کردنِ اول و این پذیرفتنِ آخر چیست؟» ابراهیم(ع) سرزنش و عتاب خداوند را برایش بازگو کرد. پیرمرد شگفت‌زده شد و گفت: «نافرمانیِ چنین خدای مهربانی از جوانمردی و مروت به دور است!» پس همان‌جا خداپرست شد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/464636" target="_blank">📅 00:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464635">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیروی دریایی سپاه: اگر تنگۀ هرمز متعلق به آمریکاست، پس ناوهایشان کجاست؟
🔹
معاون سیاسی نیروی دریایی سپاه: اگر ترامپ تنگۀ هرمز را تنگه خود می‌داند، پس چرا ناوها و شناورهایش اینجا نیستند؟
🔹
اگر آمریکا مدعی کنترل تنگۀ هرمز است، فقط یکی از ناوهای خود را به این محدوده نزدیک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/464635" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464634">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS4rAR8u3ENfKKoPIcOvsnKz8E66-Di831phkgw02a9ZvJY_PyJUYPUvBW8CxuzDX5WYab4gCr28hbRSJCft2qzjmVKWjpc_Kf4FWDBpXsdB0Dr3DcaloPLL9SUbBaZuuhHCx_MdABFa-77MCCRF3Xw_e2oVKUB_JPOZ6xPs1UAFBI25C6Er43yS2fTk_sfdBTNDMbIMFgCpw-gFrkP-RC1HKwbOezk_W7JPeyWOKBC2tUIBaa_BCLWZFY6NnOm0zgBs5i6_Fbe0pd_uawGH2zvatzCaJqxqL8zIhgCsVhlYH8abS6Z5TwIwgDM-Zktq0tpO_wSXtEDUU6WX4EZZLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/464634" target="_blank">📅 00:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464628">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tx2xiz6a4SuyPner6-Vjn1ShAE0FxDLC0InzxWu3ZG2fXRKygqLdkYWaw21-XmSb5SdYYckYDmv8dnxGFzV-f29iyYxRfoZmRdx751TKoOYBsEy86jgMbF_1Bnm2pxKmmkpsLMJCS7-MD2y7Wjwww4TLAw3sf_dbUC3J7RlOJbamdP22YY3-n-EYKXKLY09eKyYDp5JTNth17Y2nokrfUwaqOa1yQf_5l__tas4N8KX381H8246FnSFV7GXRHIjNZhtSUuq55es0_t1SWpX7LCwmPvH6dwXCudlPQqOdn2nE2CmuwuSi6fypbNaiYYJW3U2UgCQ7zNFcWI3e8nVivA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKdMfbUPfR6lwaRDMhgx1q8bwc0kKm0qfeMSdtFLDoS_x0LJt7cFWTVNOoLwt-m_vxD8NpViOQkjhTRSFnwd39hoKnmKtyKhMyJBCfKEEao6Uso2XoTWdlctxqA_ey0uKB0_vBE_KXJc2GisBa1rNRU-r5us_LeOj-tpEyA3AxaBL-7Rjt4HylCHDwRSQN6nXwXXOZcZcQ3jA4ymRpZO4UjXn51lkr__rtWFGynGPFEQ3KNzQBOpmZa50f64RX5acEa1imVXPGNkCcO-cwR6JqdWBiVFTY6odIpW2BMW7igKRiep1JTiht3P4fQTR3SNkp3v4_F-h1BpOWjbdQ3VuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S14QtXM2ZIGDbKfRotEMiOqZdhBLLY1_Detco_UH1X7MhSl1kM_ttlcm_Ar_3rD4V4eUn_Hx4awsWAPVyJ_sw9s5kXh06I-rC6vEySAMo8dzVQgokz_sW_ZXZ1ai85P13YaTKIC8LUgnRlvqdurEcDdhtG4Twu2PNFNBMsoG0ZgiZAVar6gRbHps1aGrx3vMF_ZavdjROpk4862VAf9ZYeQZmltTEyDux5KF_aNYKpU6IsPDOhrX-UjLVpUa1nvLVicUbm-RfDropAjWupDyA1436yxmMoIXYs07BvCx55w51KDH-VT8iS2z0NSmjbX8rnVVkWHR8TIC2twMQBSSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JktuMWYCUhQ0LRX7lsA7biCB-0EIJ5yaWYSDCYMxEFDnLzgbib9e_rqm90dlCwhO5_KGUOL5XBxjJM0JtMB-sMnJD7FG0-AKYUGzrtLFwBREWpuy879qlBBQ0RodQRTLd7zgAdOsg5lZL5pXb5ekum4PCw_2gde9kf7TCttq0iW-wpe__p-B4Uja6CU7x6mSJKY0iz1EZNnfs4556GeA7K5GFE2QP5Gw0fxB2C4YrhAhmsJW25jmf3MvU52WbBAuce-wZwjsHmNHJIuIvMdAnpg9AfZFQRwoR0MeyyMlHztr_cHKl5nPnKfLyMpQQpKaYLQbfCTJ4sp9g0RLkvhDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dh403N477eesB504JCrugduGZfLb1aIoJ0TkwUniVd1HpaDZtcegJQyskZwJ2AIfj3cF1DYH7l4PnEt6QqWYOD3J99O9hc_J9jKc5hQarB7xMMqfGzrqs28vwSqWByJxp3G7S49tKoyP7-IUNlTNtJDnFWIP5_vn6PQzrdHG_Ua9zXJB5uMF5r91bXcCDq4IayjXfPQji4wLhGdujWsHDxa_yg1Zi9HIThvofqqSE63w9r5pUR_KRLq9cbto5A7hk3a5fun9HT-k2Q87VcF_zmhS2_6_sqBZ6Yr66ol3IejPGvkYyxNnBhdzoX8-Qtl_8IOihe8i4pbYNgC7YL4dfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuoZU8BKOHkE4S4FL6RfDm_Yd_zCxo0Ey2KtIp226HWxL_PwWCb_prL4grJfNOssgXSIewOVO95JKLYLi4frxtCOcW1wr2lEnm8Vy8P1ibS7qNymRYzkgXG7v3kUSQlDkqliMMHQGiwXN8Ur494kyxi2HqnyenzFWvnteNBfBVqmk-n-f2w7et7UjpDNRIZ2A17NpXPCZdmt63xtsYBjb9VeXgp-yOmi6EIy0F1q6hYDLdivWPT4hI4mf5cEf_Nu9lcFm-LqqcSvEIePCxwUR5oJcSDHMft5A69XOwfwuQ1SB7WHRYWw_hLXNHk7JRYyxLnC-0Qpvdxt2J2WWZ7Xzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پیکر سردار شهید «حسین ظریفی» در گناباد تشییع شد
🔹
شهید سردار سرتیپ پاسدار حسین ظریفی فرماندهٔ قرارگاه سجاد سراوان در عملیات مقابله با اشرار مسلح که منجر به درک واصل‌شدن تیم تروریستی واقع در شهرستان سروان شد، به درجهٔ رفیع شهادت نائل آمد. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/464628" target="_blank">📅 23:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464627">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری فارس</strong></div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
لطفا برای
افزایش شدید قیمت داروها
چاره‌ای اندیشیده شود. چهار ماه پیش هزینه داروهای من حدود ۲ میلیون و ۵۰۰ هزار تومان بود اما اکنون برای همان داروها باید تقریباً دو برابر پرداخت کنم؛ آن هم برای داروهای ایرانی و تولید داخل. با این افزایش قیمت، بسیاری از مردم توان ادامه درمان را ندارند. خواهشمندیم
ارز ترجیحی برای دارو را برگردانید
.
🔹
من به‌عنوان یک شهروند ایرانی نسبت به
هزینه‌های تلفن ثابت
اعتراض دارم. چرا حتی اگر از تلفن ثابت استفاده چندانی نکنیم، باز هم باید هر ماه مبلغ قابل‌توجهی پرداخت کنیم؟ کسانی که بیشتر استفاده می‌کنند هزینه بیشتری پرداخت کنند؛ چرا افرادی که مصرف کمی دارند باید همان هزینه‌ها را بپردازند؟ ما این مبالغ را با سختی و نارضایتی پرداخت می‌کنیم.
🔹
اواخر سال گذشته شرکت
پارس‌خودرو
طرحی با عنوان «
مشارکت در ساخت
» ارائه کرد و مشتریان با پرداخت مبالغی مانند ۶۲۵ میلیون تومان، معادل ۵۰ درصد قیمت تمام‌شده خودرو در آن زمان، پذیرفتند خودرو در سال ۱۴۰۶ تحویل شود و ریسک افزایش قیمت را نیز بپذیرند. اما اکنون مشخص شده که شرکت قصد دارد در
زمان تحویل مابقی مبلغ را بر اساس قیمت تمام‌شده سال ۱۴۰۶ محاسبه کند
! ما می‌خواهیم بدانیم چرا سازمان‌های نظارتی (مانند وزارت صمت و شورای حمایت از مصرف‌کننده) اجازه می‌دهند که از سرمایه خانوارها در چنین قراردادهای ناعادلانه‌ای استفاده شود؟ من و صدها و شاید هزاران نفر مثل من تمام اندوخته سال‌ها کار و  زندگی خود را در این طرح سرمایه‌گذاری کرده‌ایم صرف کرده‌ایم. خواهشمندیم دستگاه‌های نظارتی موضوع را بررسی کنند و اجازه ندهند حقوق مشارکت‌کنندگان تضییع شود. ما فقط خواهان اجرای عادلانه قرارداد و حفظ حقوق خود هستیم.
🔹
به‌دلیل عدم مراجعه
مأمور گاز منطقه ۵ تهران
(ریاحی)، طی هشت ماه گذشته چندین بار به اداره مربوطه مراجعه کرده‌ام اما هنوز مشکل حل نشده است. متأسفانه
نحوه پاسخگویی و برخورد کارکنان نیز مناسب نیست
؛ حتی هنگام مراجعه یکی از کارکنان حدود ساعت ۱۰ صبح مشغول خوردن صبحانه بود و پاسخگو نبود و برای ثبت شکایت نیز به‌جای فرم مربوط، یک برگه باطله جلوی من گذاشتند.
🔹
چند روز است
امکان برداشت وجه از پلتفرم «میلی» برای کاربران با مشکل مواجه شده
و بسیاری از افراد نمی‌توانند سرمایه خود را برداشت کنند. این وضعیت باعث نگرانی و استرس کاربران درباره سرمایه‌شان شده است.
🔹
فاضلاب‌های
محدودۀ بیمارستان یازهرای دزفول
کاملاً گرفته و پر از زباله است و کسی برای پاک‌سازی آن اقدام نمی‌کند. پارسال با بارندگی، فاضلاب وارد خیابان‌ها و حتی منازل مردم شد و خسارت زیادی به فرش و وسایل زندگی وارد کرد. از طرفی کابل‌های تلفن نیز به سرقت می‌رود و مخابرات اعلام می‌کند مردم باید خودشان کابل را خریداری کنند تا برای اتصال اقدام کنیم. بسیاری از مردم توان پرداخت این هزینه‌ها را ندارند.
🔹
ما ساکن
تهران
هستیم و با اعتماد به
تبلیغات یک مرکز ایمپلنت
، پارسال برج هشت برای ایمپلت یک واحد دندان مراجعه کردیم. همان روز اول کل هزینه را پرداخت کردیم اما حالا با گذشت بیش از ۱۰ ماه،
درمان هنوز کامل نشده
و دندان نیمه‌کاره مانده و برای روکش آن نیز پاسخ روشنی دریافت نمی‌کنیم. با وجود پیگیری‌های متعدد، هنوز کسی مسئولیت این تأخیر را نمی‌پذیرد. نمی‌دانیم برای شکایت باید به کجا مراجعه کنیم.
🔹
چند روز پیش از
دیجی‌کالا
جت ۲ کیلو گوشت خورشتی و ۲ کیلو سردست خریداری کردم. گوشت بوی نامطبوع داشت و پس از وزن کردن، مشخص شد در مجموع حدود ۶۰۰ گرم کسری دارد و دو استخوان نیز داخل گوشت خورشتی بوده است. موضوع را بلافاصله با
پشتیبانی
مطرح کردم، اما
پس از ۲۴ ساعت گفتند
چون گوشت شسته شده،
امکان پیگیری ندارند
؛ در حالی که خود پشتیبانی قبلاً درباره نحوه نگهداری آن راهنمایی متفاوتی داده بود.
🔹
ما پرسنل مراکز بهداشتی و درمانی دا
نشگاه علوم پزشکی جندی‌شاپور اهواز
نسبت به
عدم تعطیلی پنجشنبه‌ها
اعتراض داریم. در شرایط گرمای شدید خوزستان، در حالی که کارکنان ستادی پنجشنبه‌ها تعطیل هستند، ما که بسیاری از پرسنل را بانوان و مادران شاغل تشکیل می‌دهند تنها یک روز جمعه را برای رسیدگی به خانواده داریم. با توجه به تعطیلی پنجشنبه‌ها در برخی از دانشگاه‌های علوم پزشکی استان‌های دیگر، از مسئولان دانشگاه تقاضا داریم با نگاهی عدالت‌محور و برای حفظ سلامت روان و بنیان خانواده پرسنل و با توجه به شروع مدارس، نسبت به این موضوع تجدیدنظر کنند.
🔹
فاصله شهرستان
قوچان تا مرز ترکمنستان
حدود ۸۵ کیلومتر و تا عشق‌آباد نیز حدود ۱۵ کیلومتر است. با توجه به اهمیت این مسیر، از وزیر محترم راه و شهرسازی تقاضا داریم موضوع احداث
راه‌آهن قوچان-اجگیران-عشق‌آباد
را بررسی و برای اجرای این طرح مهم اقدام کنند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsnaz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464627" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464626">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a148085b.mp4?token=hgm4nDv44KoafWtbBHUVD0HJ7kb6hs7Xa-2581ekrfY69NTefqs6NYJLShLtSvZvHWhS9NLBFbqGGtAoUFGrYNog1QAxdf_-aZ5LfdIISBq7YP58vfOjiPq70YWl016hDsxujMo-s9deG-3h0u63QxFjD6TLsWB7ClmSpAn4H1KjMBZFFfjZMsB3Kd6QViq7-Beu70o6p7Fe9y17qSDgfk8zBZ5PorXIs7v0IANnwNUkA2eDB4N6XxMLNt8p1eOLPRBGAEWtNuLyNdT_DB6ZMzrN4HBfTRLiqz2aCjxFVJOvhH8XsDvjix5_djIy9ygkIZfu3uT4La5zq2SuxVStuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a148085b.mp4?token=hgm4nDv44KoafWtbBHUVD0HJ7kb6hs7Xa-2581ekrfY69NTefqs6NYJLShLtSvZvHWhS9NLBFbqGGtAoUFGrYNog1QAxdf_-aZ5LfdIISBq7YP58vfOjiPq70YWl016hDsxujMo-s9deG-3h0u63QxFjD6TLsWB7ClmSpAn4H1KjMBZFFfjZMsB3Kd6QViq7-Beu70o6p7Fe9y17qSDgfk8zBZ5PorXIs7v0IANnwNUkA2eDB4N6XxMLNt8p1eOLPRBGAEWtNuLyNdT_DB6ZMzrN4HBfTRLiqz2aCjxFVJOvhH8XsDvjix5_djIy9ygkIZfu3uT4La5zq2SuxVStuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
سخنگوی ارشد نیروهای مسلح: آمریکایی‌ها باید خواب این را ببینند که در مدیریت تنگهٔ هرمز دخالت کنند و در صورت دخالت سیلی محکمی از نیروهای مسلح ایران خواهند خورد؛ آن‌ها باید از منطقهٔ ما بروند.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464626" target="_blank">📅 23:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464625">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594ed02de3.mp4?token=W2uXYtsJzX7IAHi4u7HA4FVASkAL7bs0dogALAzfv2WifbOcTc8Pqh-6_s-LCosgHbHKinYR_7_OXgCdH1fB1nKi7S6VQQ1ow4OfK3iVEYFaEStsPuvCpOZdPIZGSOA_AJ9Wdd-buQAX-OJkBL-n6dCnBRc0P-BAqJMpxGGaDFtHA01REOz74RjrGVW8hckrplmP4TC36LjibSyBI925b74t_lifZqi2JRz_THYB9smKFRJbW9wxKn0P7Qjx55ddeq-LJnm5JOGl547lZ85rP5fo-YZJnWAFjvuZOtV3nYnBxt63Bi0hcGHQU1Rz8nKSM0Sa3wB2vHnmNpjsCO4m8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594ed02de3.mp4?token=W2uXYtsJzX7IAHi4u7HA4FVASkAL7bs0dogALAzfv2WifbOcTc8Pqh-6_s-LCosgHbHKinYR_7_OXgCdH1fB1nKi7S6VQQ1ow4OfK3iVEYFaEStsPuvCpOZdPIZGSOA_AJ9Wdd-buQAX-OJkBL-n6dCnBRc0P-BAqJMpxGGaDFtHA01REOz74RjrGVW8hckrplmP4TC36LjibSyBI925b74t_lifZqi2JRz_THYB9smKFRJbW9wxKn0P7Qjx55ddeq-LJnm5JOGl547lZ85rP5fo-YZJnWAFjvuZOtV3nYnBxt63Bi0hcGHQU1Rz8nKSM0Sa3wB2vHnmNpjsCO4m8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: از ترامپ و نتانیاهو و دیگر قاتلان امام شهیدمان نخواهیم گذشت؛ این موضوع دیر و زود دارد اما سوخت‌‌وسوز ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464625" target="_blank">📅 23:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464624">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313b69d364.mp4?token=bnposFo26ybXEdtHCFhn8xb6dvL4dSbw5OCAgdlLYO7Uasg6WbudnUWgrNd-V3Dsq1iO_lugecLHWLrhlKj6_w1VQeY-aZY7nSuBehpPcElp9PCkr6B0qluxzk76C7nTLH6gk-42qj036i5TsrEOL6oGNIQNnjKbXdmtfaXSbFs6n-SGFS8Zv2n7WgectvG-Rd8Da9wsEOofB24xB7G_pcj4xsAUALchxjRgKdGSFz62NW69oL-Y8TT0YqNf6n8MAZqrzMLQcZ6LAb66g-zYzx2icWlpJhxK4wPtTJGGiwBu7z0UECDI_ROJrfsrlD3mFb4bIlPXLbH1nDoq88RfGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313b69d364.mp4?token=bnposFo26ybXEdtHCFhn8xb6dvL4dSbw5OCAgdlLYO7Uasg6WbudnUWgrNd-V3Dsq1iO_lugecLHWLrhlKj6_w1VQeY-aZY7nSuBehpPcElp9PCkr6B0qluxzk76C7nTLH6gk-42qj036i5TsrEOL6oGNIQNnjKbXdmtfaXSbFs6n-SGFS8Zv2n7WgectvG-Rd8Da9wsEOofB24xB7G_pcj4xsAUALchxjRgKdGSFz62NW69oL-Y8TT0YqNf6n8MAZqrzMLQcZ6LAb66g-zYzx2icWlpJhxK4wPtTJGGiwBu7z0UECDI_ROJrfsrlD3mFb4bIlPXLbH1nDoq88RfGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: هر کشتی‌ که خارج از مسیر تعیین‌شده توسط ایران از تنگهٔ هرمز عبور کند، امنیت نخواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464624" target="_blank">📅 23:21 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
