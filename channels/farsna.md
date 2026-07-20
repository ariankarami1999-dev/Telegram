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
<img src="https://cdn4.telesco.pe/file/MDIU6T8CK08QS04VHiR5X31iLq652x4LxbOPRMTq2RpjQ8rYVUxvH0nxcZm0QfxnUVU6QXEoSjuYm9z458MmBPkq8kfIHuKq3Qx4O7qO-IaLA4mPovXLlff4O6fPLfWsQ7zpuF98vuTSE0Vekbhh-J4-iY2YY4A-UCXvKXLxa_pP6YUpeA5XhzyvBhTM36cfIsGOE4EVDc_GptHDjS3vTQE1xDWD-S04YwqeYMsqgqXkTVFrOhBMn0B3IHuJmdg2C5_ZNFTwuWsx-p8xbc7Taj7Rr4urrtHUzQVlY7uTJBEv9xmA_iDzVtRJYJKWXbvH4cucHoLRK-qGbpxR-AuVQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 18:55:36</div>
<hr>

<div class="tg-post" id="msg-451439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/farsna/451439" target="_blank">📅 18:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/451438" target="_blank">📅 18:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id90Zd-TZOg1cY_tLF7Xc0g0VIlw-gVufwTx-sMwvwvRdIbdCwYAlCyETCbiNQb251lCz02_u22NgK6YCA4MMnaCr41r5NQavGvqttMhO2o2TapINkgOnliHe_GXV7xsPHaXr1BhBSGhrwh7zCljtPPGFBvazk8OoWTTDlZVT2GybkD3NX5MDuybbscEZkANwm0Kga1YLle-Zlsk63zk8usS8QzS3bIo7K8w8a4lFS8UH_V9MFzbVurNQZT67r8VTC4D9F9ccVHpzLlaRkIkeZqnCRGN-Ey45XWG6GZsE6d9AZJkoCsLv-91RKa7EyESnPqh_NfzVCJoIbWK6VD5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیرکل مدیریت بحران استانداری آذربایجان‌شرقی: در حملات بامدادی دشمن آمریکایی به اطراف تبریز یک هموطن به شهادت رسید و چند نفر دیگر هم مجروح شدند.  @Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/451437" target="_blank">📅 18:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">طرح دوبارۀ آتش‌بس چه هدفی را دنبال می‌کند؟
🔹
طرح مجدد آتش‌بس از طریق واسطه‌های قطری در حالی مجددا مطرح شده است که آمریکا هم‌زمان سیاست فشار و حمله به ایران را دنبال می‌کند. همین تناقض، این سؤال را ایجاد کرده که آیا هدف واشنگتن پایان جنگ است یا ایجاد فرصتی برای اجرای مرحله بعدی نقشه خود؟
🔹
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در واکنش به این پیشنهاد نوشت: «آمریکایی‌ها روی هوش ما اندازه آی‌کیوی مختصر خودشان حساب کرده‌اند. ما در شناخت این آمریکایی‌بازی‌ها به مرحله استادی رسیده‌ایم.»
🔹
این جمله، پیام روشنی دارد؛ پس از تجربه‌های مکرر عهدشکنی آمریکا، بعید است در ایران کسی آن‌قدر ساده‌اندیش باشد که صرفاً با یک پیشنهاد آتش‌بس، دوباره به واشنگتن اعتماد کند.
آمریکا منتظر چه اتفاقی است؟
🔹
تحلیلگران معتقدند هدف اصلی این آتش‌بس، خرید زمان برای ایجاد یک فرصت داخلی است، نه پایان جنگ.
🔹
در هفته‌های اخیر، هم‌زمان با مطرح شدن برخی مباحث درباره مدیریت ناترازی سوخت و احتمال اصلاح قیمت بنزین، رسانه‌های معاند نیز تمرکز خود را بر تحریک افکار عمومی و دوقطبی‌سازی جامعه افزایش داده‌اند.
🔹
واقعیت این است که دولت با ناترازی جدی در حوزه بنزین روبه‌روست؛ ناترازی‌ای که بخشی از آن ناشی از رشد مصرف، محدودیت واردات و تغییر شرایط تأمین سوخت در پی تحولات منطقه‌ای و جنگ اوکراین است. طبیعی است که مدیریت این وضعیت نیازمند تصمیم‌های دشوار اقتصادی باشد.
🔹
تحلیل غالب این است که آمریکا امیدوار است اگر این تصمیمات به اعتراضات داخلی منجر شود، بتواند از این وضعیت به‌عنوان یک فرصت راهبردی استفاده کند؛ یعنی پس از شکل‌گیری التهاب داخلی، فشارها و حملات خود را از سر بگیرد تا ایران هم‌زمان در دو جبهه خارجی و داخلی درگیر شود.
🔹
اگر این تحلیل درست باشد، پیشنهاد آتش‌بس نه نشانۀ تغییر رفتار آمریکا، بلکه بخشی از همان «آمریکایی‌بازی» است که قالیباف از آن سخن گفت؛ تلاشی برای ایجاد اعتماد کاذب و انتظار برای مناسب‌ترین زمان جهت اعمال فشارهای بعدی.
🔹
ازاین منظر، مهم‌ترین راه خنثی کردن این سناریو، بی‌اعتمادی به وعده‌های آمریکا، مدیریت هوشمندانه مسائل اقتصادی، گفت‌وگوی شفاف دولت با مردم و ناکام گذاشتن هرگونه تلاش برای تبدیل مشکلات اقتصادی به آشوب اجتماعی است.
@Farsna</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/451436" target="_blank">📅 18:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سخنگوی دولت: برنامه‌ای برای افزایش قیمت بنزین نداریم
🔹
مهاجرانی: دولت هنوز برنامه‌ای برای افزایش قیمت بنزین یا اجرای نرخ سوم بنزین ندارد.
🔹
در صورتی که برنامه‌ای در این زمینه وجود داشته باشد، به صورت شفاف اطلاع‌رسانی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/451435" target="_blank">📅 17:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7vtZhP1NxPQtZVZPgA3myFbhuwub6cErcHIKF7Zbd-aNXZwg4Xq3bqcaEc8CgSX7TdaH5O9uNozfUIes1eeDVUN_nbvzexSXIGq8MAmdjNfIZv-a7Ypt2XviOTnXJpdw9NWOJtwNF4COLh3jEP2d1pgTUM38UemyxHro4xs94Wg01YIBbiiO8XwD6PaZDDfzRKUaSJI9O9W9gIenqbvDpjcMs1Dxy4nKt9djppouPSHf9o6HxqvjvWmDDhfh3wmeFldJMgWBaJ0xbupr8rGmMXyHWBmI37hIc1LC57Gymac7ZDh5y6Jrd7prEioKMAH5TYpsgGDVx6u_EYf3lLUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت هومن حاجی‌عبداللهی و جناب‌خان به آنتن تلویزیون
🔹
تهیه‌کنندۀ برنامه «قصه‌های هومن و جناب‌خان» در گفت‌وگو با فارس اعلام کرد این برنامه از شب اول ماه ربیع دوباره روی آنتن شبکۀ نسیم می‌رود.
🔹
این برنامه پیش از ماه محرم نیز در قالبی طنز پخش شده بود.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/451434" target="_blank">📅 17:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در شیراز
🔹
دقایقی پیش اهالی بخش‌هایی از شهر شیراز صدای انفجار از محدوده شمال غرب این شهر شنیدند.
🔹
خبرهای اولیه از حمله به یک نقطه در شهر در جریان این حملۀ هوایی دشمن حکایت دارد.
🔸
به گفته استانداری فارس، این حادثه هیچ گونه خسارت جانی درپی نداشته و تیم‌های ارزیاب در محل حادثه حضور یافته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451433" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c258107e1b.mp4?token=CL2Q_5d3FTmVzejXhyv6CXvaOZMk9HzgDHHL0O1XipVchZ8JFuFmYJgk2LXTwqNookD0xzL7IGXUtDb-SlDJWMHzf4F1CU4GQKw5ZGSQT2jgk2oOjm05i8HTt_jdgfnKDaldw_PSJmq9H37D_z6j3LJ6wn2YB-SJ8TIC3tA1uF9uiIRRBj-nQZRf33u9JpvqDVICyA4yUhjAP5_6d10dqU4fNJdnI_QxbyiqzNIY3XuwPeO-gyNcfrcs3b-U9rvd69OlPCl5qpdW_uRmXsGx8IXWpYSQHVn-DOoZT4Ja1X9XJLHqnU_VBlaZLW__6cu9lpvgmSjmc3WNIMWtHOBsXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c258107e1b.mp4?token=CL2Q_5d3FTmVzejXhyv6CXvaOZMk9HzgDHHL0O1XipVchZ8JFuFmYJgk2LXTwqNookD0xzL7IGXUtDb-SlDJWMHzf4F1CU4GQKw5ZGSQT2jgk2oOjm05i8HTt_jdgfnKDaldw_PSJmq9H37D_z6j3LJ6wn2YB-SJ8TIC3tA1uF9uiIRRBj-nQZRf33u9JpvqDVICyA4yUhjAP5_6d10dqU4fNJdnI_QxbyiqzNIY3XuwPeO-gyNcfrcs3b-U9rvd69OlPCl5qpdW_uRmXsGx8IXWpYSQHVn-DOoZT4Ja1X9XJLHqnU_VBlaZLW__6cu9lpvgmSjmc3WNIMWtHOBsXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش‌هایی از انفجار در شهر نیویورک آمریکا
🔹
رسانه‌های محلی از وقوع یک انفجار در نزدیکی یک ساختمان دولتی در شهر نیویورک آمریکا خبر می‌دهند.
🔹
طبق گزارش‌ها، صبح امروز به وقت محلی صدای تیراندازی و انفجار در شهر نیویورک آمریکا شنیده شده است. تصاویر منتشر شده از دستگیری یک مظنون حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451432" target="_blank">📅 17:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0451456d.mp4?token=YVykqmOGxfvv6Mm3XfUgp9QSE_DvVLnMq5_Ntaxl6ZiyGfK1Rj8_v4KgbVWDqB8jecHePCHGqUrQqXX6d1jGyDg1J3M5szoxjfruw4zUSW-BIqwpBUBalzl-M_L0hnn2jfpuoAzHMEjCZiLNgOeSJCY4bjP_WICttZPA0en0LeO4LsoXDYYRXDP-Fr4Yxd4TYMP3JPcecFJzkXHXXg-z2JfpT7C4mTWg2d1tDwiQcP_46buer4hZ4DaOHfUAr6maYnAqPgiugs0MgkfetwwopSadIpp9qupyo9Fui6Xy47GlRqP_6At84bsMeGaYO0APdPTK3lPT5dcinf_PzBS1ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0451456d.mp4?token=YVykqmOGxfvv6Mm3XfUgp9QSE_DvVLnMq5_Ntaxl6ZiyGfK1Rj8_v4KgbVWDqB8jecHePCHGqUrQqXX6d1jGyDg1J3M5szoxjfruw4zUSW-BIqwpBUBalzl-M_L0hnn2jfpuoAzHMEjCZiLNgOeSJCY4bjP_WICttZPA0en0LeO4LsoXDYYRXDP-Fr4Yxd4TYMP3JPcecFJzkXHXXg-z2JfpT7C4mTWg2d1tDwiQcP_46buer4hZ4DaOHfUAr6maYnAqPgiugs0MgkfetwwopSadIpp9qupyo9Fui6Xy47GlRqP_6At84bsMeGaYO0APdPTK3lPT5dcinf_PzBS1ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی حسین طاهری برای مردم جنوب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451431" target="_blank">📅 17:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960a5e081d.mp4?token=DT8YDRxVOg21MS6pU4WhtWaW1vsD45hham32L0ZBSQkhymSBSAyQf0aWNX_120O5OAOVmfco18e3IvQnYRzct55EnMCMvvSchT9nrv6frFTZAr1dph1f97RvsiYgyFSlED-aW2jHydzyPoP5CuMBDBrV8kaoCAXxVNB-n1g44cnt3PnYuCC7KaZtZ05fwWxLKOTFlT5i1qXOLBCivnyps_saqm2xJfSg7z6zckL074JP2ivU2x0U7NC-ZGGO-SdUOrLAMqqaHsuT-R_p4ElRPes3AGxBzw_VoTpyCkjLxxmwkC1cc4kJJZGzbKnxak7Sq6CzYVFRdTAQXbnBxDXsXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960a5e081d.mp4?token=DT8YDRxVOg21MS6pU4WhtWaW1vsD45hham32L0ZBSQkhymSBSAyQf0aWNX_120O5OAOVmfco18e3IvQnYRzct55EnMCMvvSchT9nrv6frFTZAr1dph1f97RvsiYgyFSlED-aW2jHydzyPoP5CuMBDBrV8kaoCAXxVNB-n1g44cnt3PnYuCC7KaZtZ05fwWxLKOTFlT5i1qXOLBCivnyps_saqm2xJfSg7z6zckL074JP2ivU2x0U7NC-ZGGO-SdUOrLAMqqaHsuT-R_p4ElRPes3AGxBzw_VoTpyCkjLxxmwkC1cc4kJJZGzbKnxak7Sq6CzYVFRdTAQXbnBxDXsXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجات معجزه‌آسای موتورسوار نوشهری از برخورد لاستیک سرگردان تریلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451430" target="_blank">📅 17:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4ac0667a.mp4?token=d0h1JKq1AbFxbyFm-HE-fZ5cj-2A5JjQXdHnNAatTrhDRmGkqTT6Q9x10sr1egLWLEgGOTfcNxk72UE8Ffj3yqghDw0spewdsKMtcdr46CKjdCjpB6b4tmvlHSTEmOzMsDprw8HEkE8-FRyOSNvpMAIQ90lwuJlOrvVJIIYF0phiUbO33ZA4cT-wGLusgQMVI2sf3UwtNlLacdHcnM6MOrY4adn1refI-xPv2Ip7OKTUhamFNw8J9BvQD9ngMjAx96T48pKB81rSDiUsRXGEF3atwpHRDVTJs2UNvR8mf9K1765XndUWWs7HEy4-38nuEN9r-pnW4IHCPu1OAIefTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4ac0667a.mp4?token=d0h1JKq1AbFxbyFm-HE-fZ5cj-2A5JjQXdHnNAatTrhDRmGkqTT6Q9x10sr1egLWLEgGOTfcNxk72UE8Ffj3yqghDw0spewdsKMtcdr46CKjdCjpB6b4tmvlHSTEmOzMsDprw8HEkE8-FRyOSNvpMAIQ90lwuJlOrvVJIIYF0phiUbO33ZA4cT-wGLusgQMVI2sf3UwtNlLacdHcnM6MOrY4adn1refI-xPv2Ip7OKTUhamFNw8J9BvQD9ngMjAx96T48pKB81rSDiUsRXGEF3atwpHRDVTJs2UNvR8mf9K1765XndUWWs7HEy4-38nuEN9r-pnW4IHCPu1OAIefTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ضربات سنگین نیروی دریایی سپاه به ارتش کودک‌کش آمریکا با حمله همزمان در سه محور
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451429" target="_blank">📅 17:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451428">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
وقوع چند انفجار در کویت
🔹
در حال حاضر، آژیرهای خطر در کویت فعال شده است، برخی منابع از حملات همزمان پهپادی و موشکی به مواضع آمریکا در کویت خبر می‌دهند.
🔹
ارتش کویت ضمن تأیید این حملات، ادعا کرد که موشک‌ها و پهپادهای شلیک شده را رهگیری کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/451428" target="_blank">📅 17:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av4lxxwcfxqIKlRTJqC-TaWI9OZuVo2TtE75v9p6uYW2cl-IQBcjTYqGq8laPHp7gzX_HNVB2F3jyYXh83PuY7tC6K94Tn8IdbjvRLjsRp_BghI4p8vykpFUfMhLEcj_bWGkGaEeNrF3SQvp6x_lyTDQT6IV4czTRTk8zH3NOn1EWhuLR9IUr8qCcVO4Pml3spDywSCBFBLo4taTiWMAq9PD6xlntvmmooD3HCWo09eX8Q0GZ1E7k3apHf0anyFi_eIER3647OLpZ9L0vReJuH5aQwiTDh9y2Gn4RsyKL91UmW58w5uqojtJMyU6OLoTb7Q7PUtu9A-NOoh6AHSVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07f18e551.mp4?token=e-7Ij7flrW5YmuiYxpGPj3FcQ63hqzDk0Ya-ROPBWrXNIQgzPMuqGCMqjj6vJ2ONa9-2-GKeMkspMH3lZI9UDoyka7mLWKxbzTqss63C2tf84lJ2FC4YffeXBWG1f_OYJGuH7bwU7EL5G4c8oYbwAahSVyauDwIRjDuz7_9NJih2glKLQQc7maKHYYJUMF81d-x9gDw4uuf0BVmTHJzYVY9oAjpTRuqZqOFyzRr6HygEbIsRBDnoLjPMHaPC91J8ngunC4yVQdM0K7pDG1fTeyhOty-Yri6L6S9dFXOlNOEHOnkjBNQL1f_iP8Gppk39itAgpR_bJ-KWJDE08M-qZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07f18e551.mp4?token=e-7Ij7flrW5YmuiYxpGPj3FcQ63hqzDk0Ya-ROPBWrXNIQgzPMuqGCMqjj6vJ2ONa9-2-GKeMkspMH3lZI9UDoyka7mLWKxbzTqss63C2tf84lJ2FC4YffeXBWG1f_OYJGuH7bwU7EL5G4c8oYbwAahSVyauDwIRjDuz7_9NJih2glKLQQc7maKHYYJUMF81d-x9gDw4uuf0BVmTHJzYVY9oAjpTRuqZqOFyzRr6HygEbIsRBDnoLjPMHaPC91J8ngunC4yVQdM0K7pDG1fTeyhOty-Yri6L6S9dFXOlNOEHOnkjBNQL1f_iP8Gppk39itAgpR_bJ-KWJDE08M-qZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲ کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و ۲ کشتی دیگر از ادامه مسیر ناایمن منصرف شدند
🔹
نیروی دریایی سپاه: ساعاتی پیش ۴ فروند کشتی متخلف با شیطنت و حمایت تروریست‌های امریکایی و با خاموش نمودن سامانه‌های ناوبری و بی‌توجهی به اخطارهای پایگاه کنترل تنگه…</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/451426" target="_blank">📅 17:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451424">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ضربات سنگین دریادلان نیروی دریایی سپاه به ارتش کودک‌کش آمریکا با حمله همزمان در سه محور
🔹
ملت به پا خاسته و حماسه آفرین ایران اسلامی، با توکل به خدای متعال و دلگرم از حضور هوشمندانه شما مردم بصیر در صحنه، دریادلان نیروی دریایی سپاه با حمله همزمان در موج ۲۳ عملیات نصر۲ در سه مرحله با رمز مبارک یارقیه (س) ضربات سنگینی به نیروهای تروریستی آمریکا در منطقه وارد کردند.
🔸
مرحله یکم: حمله به سوله‌های نگهداری و تعمیرات پهپادی واحدهای آمریکایی مستقر در فرودگاه اَلصَّخیر بحرین که منجر به انهدام آنها شد.
🔸
مرحله دوم: حمله به سوله‌های آماده سازی شناورهای تی‌اف۵۹ در بندر سلمان بحرین که منجر به تخریب آن گردید و خسارات سنگینی به شناورها وارد آمد.
🔸
مرحله سوم: به آتش کشیده شدن سوله‌های محل استقرار و پشتیبانی و تجهیز نیروهای تکاور ویژه دریایی در پایگاه عریفجان کویت و منهدم شدن آن به صورت کامل.
🔹
حملات کوبنده رزمندگان اسلام با انبوه موشک‌ها و پهپادها در مقابله به مثل و پاسخ به تجاوزات ارتش کودکش آمریکا ادامه دارد.
🔹
رئیس جمهور بی‌خرد آمریکا که بارها به ناآگاهی و بی‌خردی خود از اوضاع عالم، اعتراف کرده و می‌گوید بدون اطلاع از عمق نفوذ امام شهید ما در مردم جهان و عشق و علاقه عمیق مردم ایران و سایر کشورها، ایشان را به شهادت رسانده و اینکه می‌گوید بی‌خبر از اهمیت تنگه هرمز در اقتصاد جهان در این منطقه، جنگ به راه انداخته است، شب گذشته باز هم بی‌خردی و ناآگاهی خود را آشکار کرد و اظهار داشت تعداد موشک ها و پهپادهای کمی برای ایران باقی مانده و رو به پایان است.
🔹
رئیس‌جمهور قاتل آمریکا بداند اگر این جنگ چند سال طول بکشد به اذن الله تعالی تا آخرین روز آن موشک ها و پهپادهایمان بر سر جنایتکاران آمریکایی خواهد بارید.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451424" target="_blank">📅 16:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451423">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7Gb600dWlAN0GOWRUr3xiXsTCarpDR-t5cvdO-r7F6kJKRmTSEDPckBwVDHR72rvUMl_kpn6zFG73C1Vkakzs4Xizf8RO_Mxxr_pERQazVMdu5g-Bfm1WeX5BL1N7AFwgvXZ1pcMkLS6psSOy7ucVAbdgR1kt-i9hjVaujb4wdlDJV5b9ShgOFKMleRfgLlUSwvR9gSheDMuoJDEVdyz1Z-RwbE4Ljata9HCWAxrKOp0k0YtS81iUuZLcbs6NwY2U0YugE972pzKtHDdL7aU0aoPqG0u13Qgx0T2EIJnjtZAkRRdqUpSn304QUdok_TlJDSEurokZaSVcigksKjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور عازم پاکستان شد
🔹
وزیر کشور، در رأس هیئتی متشکل از دستگاه‌های اجرایی به دعوت همتای پاکستانی خود راهی اسلام‌آباد شد تا راهکارهای توسعه همکاری‌های دوجانبه را مورد بحث و تبادل نظر قرار دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/451423" target="_blank">📅 16:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tm-Aj9ZwO5M7-4F4C0BE6efvpoJkdVW6ZAKx8kLC8c-IDQQiU3VTzY4b31Vx5lDJS6R-WlFfkDhOCsZFiqmug8zfkJzFtpqRw4jXodsyd00YCtjQMDEj-FnHll-dGvqwQGjrAZALRD7ojfEhx2P7yD9z5tG1leI0b86KOtxZfuW1lCdfwvDI9O0OhMvO8yqkV1GjSUCtzU5D8BbMzEqQ6HjifXSxvHEqRUmg695470GdSIndpVpL9pWVC_3Y1PEZiMsj0mc6PBbpqTeEdhgciX3aAqXS6pkKu8fhUJL_ew_ivd_Ifw5dL3LKo9PNBOmbKNp0dZ7MF1rH7zonMfs_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzYRd35THDbE-MUi9xKBSOORpyfBynt3TyWBl4GXExAANVLB4J_AGuivHWiLqfFY70khVZvvd0EtrYR5vbyOeWY19EjOImQ1x84m8S39wN9CgAZb_LbAC3nd0N6VQPQVr-eMSScESndSHMgCj_QLtO_btnruWAnAHDxJoznP1Xr9IvumFwrcRWi0mFeg9oprv8ZxNc_7ziiRSxSTmDMJbhdLTtCrr8UBFv2cymjpFlyAoLliJIBxQfCof912WG97SzOet1YdRbJOaMr6OzA7tQqBjz6545_dabF0tedW21GIraqz8s04qTvMtOBofFKdhGZ4P1iuJljBjmrOhYICUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQeBOdugb9lW2DCX8GAe_zWOR37N8XU_G5Doj-YJOC6ZOxVo3gmIzgwlz8kf0Jl5pGO78llyAMbNPhnsB3bCBVtS5CVSaecFPuTNAytC36BxreXcI1uOj3t0GBoblZ-gKE-Az4ApBQJY6OLxgz8SLe32DOKhjP9ROLIzzDoqDenEje-H_3Q49Uhk8jgdqBih9DEBMynwtCDcEy_oB2VcdfkEfxTXjD1VbkZqPekfNAMgiMEgz7mNTK5dyTR5cj7KPdKR5Bvjzk3r3h7w0_NidLZV-4ZyCiaPi5lvL387JRI4morjIeIUvkVcsaKikoIoVIjBkgwKr3tPmV21df3uHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjJNEZm-D0KWk3QJ2q2jEXhorISeZO5BJuO8FAXtdq34CXYGfzfShyv9ssGdLOTp5uX1T6Ipt7SyUBrjcKZWH0NZw62kVciTI_PhHymfQSCep1VRY_dW9vzvmPF28rAo-Bvqml5Y54Ysa2BJ2HE9IWMvTn9dKfdKUZXjATM15Q7tLW-Ex9_C6Yv3JnXOm5kDF7xF7ir_gY6VYvvhgizg_FeOyo1Hr39PBRqqTAL37mgYAjfa6XO9yG3KWUnP_QktIRKKFHbPzwf_wyowLsRixOMjHu7E8YtaHf_NQbOsxD2SLK6h6tt7RHZu67HLVFl9e7fSZFYP9BdmS-c9t5g0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThNMnzZ2qz6sM5P19CvnfK1FMpR6QrwMMyVytvF4azk3tmqpq0Ed-i6K8JiR8daHHQ2PIYlf2ThtBTJBXgfBTzqRPcX0EyKMg2XWwOnEpmfjOQcqeD9lmufI60raRloY2zm4HsRguTDk9UdoZutnpCEeU4bU0Opbso5Z7HPiIB-6A_nSJ0mW-llt7-51RfcWg1DPf5TYlrIel4Yh9BkWsjGL8vahpKAtwBxrtGdHLvMdcE35Pe7W_HpiowFWIUJeVLzMfGj-ujWYtt4pKupAf5aa8WyemPXAmZCRLmdnGZYalT55QfxkdR1ahdx2zxZq0R5U_NOeWnCVmGcwxS2_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlI-dQmyeEnrMzJhhpflMpFT099rLwPslnD10JIcvfSFJnsqiVvQB5aW7ofG-65SD9Oclruh94KCErfwOSmXwrN3XkalhH5Z92RDeZ-X6FhW6IT4dq6d7L88idhyjtobkw1eIXVhzKkSMjqDnc9SbsagS4szrSebrp0rtMZzqimwNnQYCM9sPxOglyjpOvxazC0_WM0Y36fBLC2BW_H8Rs3K3Z559pIaG1y24sXVEkqHyJhLJ_2o3ZC0PmPxCiXT18sw-y5qwLkFaqSwscleHU1lyxacoQXoar4dYVCcH2pmVDfgp2NfIPG0d1Jr0rz23wC8elNnvCMraDA2Kh8TGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WoU80MeGVRWk5tNse731aHvQmV3G0hCg182_TFRpgCOoVoBY8cAGSpaz0SOTbbCNYvUWq_PoDmbqV9OhzYVb5i35JWwj93Rv_W6CpBgaAZfAKkBTtb6uwgCBhDx0SxjHlIx4xyivvYweU6GcPaLlDOrXovrB5-B6zgeeGDmkGyTteP4A7re9CI9u7vV4pWNRSCOL5SAZEZvDG3UMWDU8bmALqWPwVT6xS0xsTtX7YWkf0o1MQCoe8ZLlNoagBO5tz8uCnywVV3fYHqdd1-TAiE7Li3sdXMSfANua1-uDh86ms5PSID86jNftJzml4x6HJVGaoO7-SR9DohColyf8dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفر چهره‌های فرهنگی، هنری و ورزشی به جنوب کشور
عکس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/451416" target="_blank">📅 16:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
وزارت کشور بحرین: هشدارهای حملهٔ هوایی فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/451415" target="_blank">📅 16:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451414">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCIlXHvzVeQYH7OAtTugd31U4Tdkf1ktEItbK12Hk6YtMKO130ZMOhCSnrN1wStdF6RiUarddmoXxgNPBeEe6IgPAWY5Khkqk0PTYGrFiJBAkPVQVIj7yyLxBHao-YE1utRF-MRr5liMNTWyyvkvEGLEOD06d52BSnPfSygpcxFqr0LUqUhL1axoXYQVNtPe8yWZDYDh5xjKaYuEaT0Fwki3skHtJVYreNbOlYZ5MN0WMIbVwRpVa0IsnZ1Qt00TYZn_iasd1VMSyRZ8UAK1IvSaHtZ3526ntyvPCIBqvcUPXLqQCBRBz7kwEUVVVdZQ9234M7Q96I_jzwUL6JZuIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش دمای هوای پایتخت تا پایان هفته
🔹
هواشناسی استان تهران: کاهش دمای هوا از فردا آغاز شده و این روند تا روزهای پنج‌شنبه و جمعه در بیشتر مناطق استان ادامه خواهد داشت.
🔹
از روز جمعه به بعد، روند افزایش دما آغاز می‌شود و پیش‌بینی‌ها نشان می‌دهد این افزایش تا اواسط هفته آینده ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/451414" target="_blank">📅 16:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451413">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE_3TDI05lY8Aaqc4Q_khK7QXoV-9L2XJj62spaIZMlIPSiZZ575kYN1r7vwevTuEXEpOPXVoFU9ajWjGtMMSV4GXtvG8hZOTgTN3Wv8Y9efie4_QJEwSDKwsI5j08CSEVghkTR52vJzlr9gGr6Ph7Doa-9qoR_5cgTupMNolxNnUaMfGKvRNYmCXV1hf8rBZ6U0cnn1utZ3mTpiftAGYXq1UugVPFs5Ccu58Hs3Yu66aKpLCRt561mwOKfHdwqQXFr9aUwjcpDcdlGGrlElOJ9XVAEHIXACHbeuhmA2QbIHzyNkyEqSzvJ0l_fWgIdgYNx1hChYhmrRkqW-Ge8Isg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با آغاز فروش بلیت قطارهای مرداد سامانه از دسترس خارج شد
🔹
طبق اعلام شرکت راه‌آهن پیش‌فروش بلیت در تمام مسیرهای ریلی از ساعت ۸:۳۰ امروز آغاز شده که در حال حاضر سامانهٔ فروش بلیت از دسترس خارج شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/451413" target="_blank">📅 16:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451412">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4ZPJUbNI_Hl-3Ju7UaAfP8O2zrWEWD1folMUa9SGNu2r5Hp58EqPZiM-Ub02JxzOnt0JM-ClpVPL_yD7ZBs1rMyAAxnBueyJADdgf1RdUxPBJp-37RtGEdjhAoQrowseoAOkUQupKG2iZ42P8742u45MBeoQe3ktkWG__SwAnH7aRr8g0ZEZ8MC1UQSj5G9BuwV8i2VRNwZh8mBvVhQtg9O7hDLmNxjhGI1kPwnnHz_xKWGMoJeX7n3WEwDbuFlchFxjzAfN_jzYhAKGrSBGYidvqrBpmjtof2RJo9qXvqzKyBpUvPkXttwBZ3NPnQooLxXOChdizxbsj6cD7_yjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
افتتاح باجه بانک شهر در زنجان؛ گامی تازه برای توسعه دسترسی شهروندان به خدمات نوین بانکی
👈
باجه بانک شهر در شهر زنجان با حضور دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر و جمعی از مسئولان استانی، به بهره‌برداری رسید تا با توسعه شبکه خدمت‌رسانی این بانک، زمینه دسترسی آسان‌تر شهروندان، فعالان اقتصادی و واحدهای تولیدی به خدمات و محصولات نوین بانکی فراهم شود.
⭐️
به گزارش روابط عمومی بانک شهر، دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر در مراسم افتتاح این باجه بر رویکرد توسعه‌ای بانک در گسترش خدمات‌رسانی به هموطنان تاکید کرد.
دکتر احمدی اظهار داشت: یکی از اولویت‌های اصلی بانک شهر در سال‌های اخیر، ارتقای کیفیت خدمت‌رسانی، افزایش رضایتمندی مشتریان و ایجاد دسترسی آسان‌تر، سریع‌تر و مطلوب‌تر مردم در سراسر کشور به خدمات متنوع بانکی بوده است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/451412" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451411">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYSpMQWL-fJBOnXYBsb2IKiXQ2HzMZMOWK17g70W4wLRsnfVVBHphJLOj5HBKg-8PFnkUkoz_mwvfe3quLWc03e6eH50ip8Em2wej78j1ECqSMhGtkiwSylr1z8AkHRqjN2DNhyfh_ov8dfO4-ZLKUYJaiIKfKi52nOiR2_3u8CcT2ECuGRyH0ClNnYuGitHcrP8BlXeQnkMj4nWJlJqm4b8z5Y29jZ957Ub-jPBNSdC8J7Z9VMvFqC0eOrs9KyjUF9DodzR3DepxUFA70qHz8qLPBcq_Iw-5mJNgThvYf_KmTcKJh0e1_fsIrFq3Md899vS00ZpFQ_x0rkm9kM7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/451411" target="_blank">📅 16:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451410">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/451410" target="_blank">📅 16:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451409">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فرماندهی کل سپاه: با همه وجود، هم‌صدا با ملت بزرگ ایران، فریاد «لبیک یا خامنه‌ای» را از ژرفای جان سر می‌دهیم
🔹
فرماندهی کل سپاه پاسداران انقلاب اسلامی در لبیک به پیام راهبردی فرمانده معظم کل قوا: ما سبزپوشان حریم ولایت در سپاه پاسداران انقلاب اسلامی، پیام حضرت‌عالی را فرمانی نافذ، میثاقی الهی و نقشه راهی روشن برای استمرار رسالت دفاع از عزت و استقلال کشور می‌دانیم و با همه وجود، هم‌صدا با ملت بزرگ ایران، فریاد «لبیک یا خامنه‌ای» را از ژرفای جان سر می‌دهیم.
🔹
میثاق می بندیم که پیوسته امنیت، استقلال، عزت و پیشرفت این ملت را ستون‌های ایمان، توکل، خوداتکایی، اقتدار ملی و تبعیت از ولایت پاسدار باشیم و هرگز سرنوشت این سرزمین را به وعده دشمنی کودک‌کش که کارنامه او آکنده از عهدشکنی، فریب و کینه با ملت ایران است، گره نزنیم. تجربه‌های بزرگ این ملت، ایمان ما را به این حقیقت راسخ‌تر ساخته است که راه عزت، از مسیر مقاومت، هوشیاری و اقتدار می‌گذرد.
🔹
فرمان حکیمانه حضرت‌عالی را نصب‌العین قرار داده‌ایم و اینک که آمریکای جنایتکار بار دیگر راه خطا، تجاوز و ماجراجویی را برگزیده است بر این میثاق استواریم که ، «درس فراموش‌نشدنی» را که نوید آن را فرمودید، با قدرت، قاطعیت، حکمت و اقتدار به او خواهیم آموخت؛ درسی که هر متجاوزی را از تکرار خطا بازدارد، هر طمع‌ورزی را در هم بشکند و حقیقت اراده شکست‌ناپذیر ملت ایران را در حافظه تاریخ و ثبت کند و مسیر حکومت جهانی مستضعفان را هموار سازد.
🔹
در اجرای تأکید حضرت‌عالی بر حفظ وحدت و انسجام ملی سپاه پاسداران انقلاب اسلامی در کنار سایر نیروهای مسلح، صیانت از همدلی ملت، استحکام جبهه داخلی، پاسداری از سرمایه اجتماعی انقلاب و جلوگیری از هرگونه رخنه دشمن در صفوف به‌هم‌پیوسته مردم و نظام اسلامی را از مهمترین وظایف در منشور پاسداری از انقلاب می‌شمارد و بر این باور است که اقتدار دفاعی، در پرتو وحدت ملی، استوار و نافذ خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/451409" target="_blank">📅 16:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451408">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
🔴
یمن محاصرۀ دریایی بر عربستان اعمال کرد
🔹
سخنگوی نیروهای مسلح یمن از ممنوعیت کشتی‌رانی و محاصره دریایی بر عربستان براساس معادلۀ محاصره در برابر محاصره خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/451408" target="_blank">📅 16:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451407">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8280446ccb.mp4?token=ZQmeVa9RZtdYSmXti3yWxpGBQnte6vT3rEkUWNkyte_RQ7E9aqnbw50Q0sQ08BhIaWUvzY90Vu-ujSqtGlrc8v9Z9CxBfPcEDG7mjoPzrCqL1aC8gPLxL17iYDyh6O_f6JLeYIO5YSnL7Ijh8531tPNv8RbM_Zgc59EqG3mIPxVI0h9sd-0TRGHTojcy15iVF5L7vBdp0-P4kjLscqRIIN7r09s_lgLCAFRvt0O5d87dt_Ee4cGO9_h6jXmXM9Rbp0MJo_HTs_zgnZgx_aIZri3cVWoIwv1HU7txkigrl49vlyoxoFvObvv45U50_GKoswEs0tpgxGmwe858uy1jFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8280446ccb.mp4?token=ZQmeVa9RZtdYSmXti3yWxpGBQnte6vT3rEkUWNkyte_RQ7E9aqnbw50Q0sQ08BhIaWUvzY90Vu-ujSqtGlrc8v9Z9CxBfPcEDG7mjoPzrCqL1aC8gPLxL17iYDyh6O_f6JLeYIO5YSnL7Ijh8531tPNv8RbM_Zgc59EqG3mIPxVI0h9sd-0TRGHTojcy15iVF5L7vBdp0-P4kjLscqRIIN7r09s_lgLCAFRvt0O5d87dt_Ee4cGO9_h6jXmXM9Rbp0MJo_HTs_zgnZgx_aIZri3cVWoIwv1HU7txkigrl49vlyoxoFvObvv45U50_GKoswEs0tpgxGmwe858uy1jFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ علیه ایران به روایت کارشناسان آمریکایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/451407" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451406">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c00107617.mp4?token=S2yjcs7hyKXvbNmLBW0KYaZVcgivsBhXlptMuZIc989JfHJU3GhQzAYIk72J95pNq4dn03U2ztObCip-EKUo7fGaDX0xUJSrnWEIsr7vpmhdKdfLCMmZz2wsHyKRWGD5mYZFXqSbsykQ7uRKHl_uyMtT75j5yMi3y2wXh_nHi7uOG6wigZ4e14v9Fl-ygu3_9irp8NPsoSxlD3qjUG_t7nFxSzVzEw1awaHYm1whm96y0vwos9MHZhayj6-nMd9hWgeFNA6nYjoBj51ZX-g6Gum9cIsDx8DAYqiK9KHRv7U9hTLqBlzbwbbCkzai7a2NWwrv1sOGQKwNAZuii0bsoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c00107617.mp4?token=S2yjcs7hyKXvbNmLBW0KYaZVcgivsBhXlptMuZIc989JfHJU3GhQzAYIk72J95pNq4dn03U2ztObCip-EKUo7fGaDX0xUJSrnWEIsr7vpmhdKdfLCMmZz2wsHyKRWGD5mYZFXqSbsykQ7uRKHl_uyMtT75j5yMi3y2wXh_nHi7uOG6wigZ4e14v9Fl-ygu3_9irp8NPsoSxlD3qjUG_t7nFxSzVzEw1awaHYm1whm96y0vwos9MHZhayj6-nMd9hWgeFNA6nYjoBj51ZX-g6Gum9cIsDx8DAYqiK9KHRv7U9hTLqBlzbwbbCkzai7a2NWwrv1sOGQKwNAZuii0bsoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: سامانۀ رادار اخطار اولیۀ دشمن آمریکایی، یک سوله تجهیزات و قطعات هوایی، و یک آشیانۀ پهپادهای MQ9 آمریکا مورد اصابت قرار گرفتند
🔹
نیروهای رزمندۀ شجاع ما در موج ۲۲ عملیات نصر۲  در پاسخ به تجاوزات مکرر آمریکایی‌ها به خاک ایران، طی حملۀ پهپادی، یک سامانۀ…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451406" target="_blank">📅 15:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451405">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رهبر انصارالله یمن: عربستان باید مجازات شود
🔹
نقش عربستان در همکاری با آمریکا، اسرائیل و بریتانیا برای ضربه زدن به هرگونه موضع واحد و یکپارچه امت، اکنون کاملاً آشکار و شناخته‌شده است.
🔹
تجاوز عربستان به یمن سال‌هاست که ادامه دارد، هیچ‌گونه توجیه قانونی ندارد…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451405" target="_blank">📅 15:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451404">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47acd4d38.mp4?token=RsTpzgtNiOUVSf0GcrQeenRfhmaV76YgwsGonxCFBuIdddbiykNoN-fmiaBgw1-MnG7fecngoOxe1Hjt5x-oMGIlPIaXqJCvxlh0dBkIw6M_sOHoH7XEVEeBCv7rZ0KXrNAZ1_Bvkig1Bl9dht9nAsUmWkAyWoudFt0QO2un9GNFkBjnQ28nxIPlpM5JbSfoQR37GWkGVTBgkG-P5DGd_G9Y7a9Y-sif3lm_gBJOcwnchT0FtyZAl612wrIuF0P_HfnAQtNSRE5_I0H7ICBzoSXaWV68THdvhHpVq0VYaMRGWE_nQNmAjG4CbwWsYzUzaLY7sSzRGJF3_F4ymnxAKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47acd4d38.mp4?token=RsTpzgtNiOUVSf0GcrQeenRfhmaV76YgwsGonxCFBuIdddbiykNoN-fmiaBgw1-MnG7fecngoOxe1Hjt5x-oMGIlPIaXqJCvxlh0dBkIw6M_sOHoH7XEVEeBCv7rZ0KXrNAZ1_Bvkig1Bl9dht9nAsUmWkAyWoudFt0QO2un9GNFkBjnQ28nxIPlpM5JbSfoQR37GWkGVTBgkG-P5DGd_G9Y7a9Y-sif3lm_gBJOcwnchT0FtyZAl612wrIuF0P_HfnAQtNSRE5_I0H7ICBzoSXaWV68THdvhHpVq0VYaMRGWE_nQNmAjG4CbwWsYzUzaLY7sSzRGJF3_F4ymnxAKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از امشب دما در نیمۀ شمالی کشور کاهش می‌یابد و بارش‌ها‌ آغاز می‌شود
🔹
در تهران تا چند روز آینده دمای بالای ۴۰ درجه خبری نیست.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451404" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e596dbd9d.mp4?token=uXgxt6QhvQJ0OwCh2LG9OSDFKeP3GsspUr23I-rjir5CBvThOd2j9Cbu4u-RgCKM_m62nGAvnvG6j2r0iYofy3H7vh55FXhJ2iHnZEEiYXbcfmgNxzUsPDje70-UlU-4ptU1zruYzVo8JgX1ZSIryfjwwMKGatlkyIIEy3rUCkEg31z9oVVTOz4Tc1ffrJBR4PTdDMLvJznXT10p7yyGdo7Bugry8t7cOSq-RDajErvN9-EIZV2FQoP2D5B8kLNb1wr7qseTdf4mIlVFexLIAmZ1SQ26vwbcxCc-q2xWiR7AXq_HmVe6N7Vjko3a6T955fjYYEEWJw2cgXLq_thGbCtOn9JuJVaHLmzJuzOYTjYNrQZoQ-R0cTtQRtj-93Ji1RM1ssJCzoU2veuhIBFUu50OQ7-_cuuW659PIISrJd32dqMRCwuFCNsKarLqnvT2MDyHsWYumFlGHYIMDyWrEmn-Rn2q7HG44mjStlHbdMgw6KL72b2su3AAsY66kSR8QQgjb3i3sa1CA3GB-QJ7kTGHiw2bbViG4z8Dr3FAMcVs7kEryhOg7gKLyDQsXw-tEBUvYcKPVZv1TCZ6mtRq7d3HwB7dTPbXSpCBQxrs-fmBFKBH8OpPZCKg-FyjPCIVDamzaW2Vgl9_vmCcK5iljx4xhq2HePumi03ziMOpA_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e596dbd9d.mp4?token=uXgxt6QhvQJ0OwCh2LG9OSDFKeP3GsspUr23I-rjir5CBvThOd2j9Cbu4u-RgCKM_m62nGAvnvG6j2r0iYofy3H7vh55FXhJ2iHnZEEiYXbcfmgNxzUsPDje70-UlU-4ptU1zruYzVo8JgX1ZSIryfjwwMKGatlkyIIEy3rUCkEg31z9oVVTOz4Tc1ffrJBR4PTdDMLvJznXT10p7yyGdo7Bugry8t7cOSq-RDajErvN9-EIZV2FQoP2D5B8kLNb1wr7qseTdf4mIlVFexLIAmZ1SQ26vwbcxCc-q2xWiR7AXq_HmVe6N7Vjko3a6T955fjYYEEWJw2cgXLq_thGbCtOn9JuJVaHLmzJuzOYTjYNrQZoQ-R0cTtQRtj-93Ji1RM1ssJCzoU2veuhIBFUu50OQ7-_cuuW659PIISrJd32dqMRCwuFCNsKarLqnvT2MDyHsWYumFlGHYIMDyWrEmn-Rn2q7HG44mjStlHbdMgw6KL72b2su3AAsY66kSR8QQgjb3i3sa1CA3GB-QJ7kTGHiw2bbViG4z8Dr3FAMcVs7kEryhOg7gKLyDQsXw-tEBUvYcKPVZv1TCZ6mtRq7d3HwB7dTPbXSpCBQxrs-fmBFKBH8OpPZCKg-FyjPCIVDamzaW2Vgl9_vmCcK5iljx4xhq2HePumi03ziMOpA_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451403" target="_blank">📅 15:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451402">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc1570a063.mp4?token=hBeYbmkn_d4iGeDUa8Ak_9pLYKOOyig_wHRNtFcyGUy1Qvqu4k9uSNhC1d6L1SVO95sQC53gDCfvKDQA3hshScPIM4fiPewkVwyaX6n_WPZz8wy0dpnJ171LUP3X9iA3zqAC9ikNZMElldZCpGnNnVQ1yPYvKpzTpgx9WQ3VznFe4JXuFaFPfcV7pm26ASe6xAy5TRGktwztnt5FRJFoOpCaEO9CQ6QpJnat1LgUZsTb5Lfn4lRVHk9c9PnpIrljKrbzm6NihTgpnDMKtOYsDVTuXpUFAoyPuxsB4MWZijNK6mSivA6cmAK7tIHwlQ5OoB_V3bJbccLDR33D4J3CLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc1570a063.mp4?token=hBeYbmkn_d4iGeDUa8Ak_9pLYKOOyig_wHRNtFcyGUy1Qvqu4k9uSNhC1d6L1SVO95sQC53gDCfvKDQA3hshScPIM4fiPewkVwyaX6n_WPZz8wy0dpnJ171LUP3X9iA3zqAC9ikNZMElldZCpGnNnVQ1yPYvKpzTpgx9WQ3VznFe4JXuFaFPfcV7pm26ASe6xAy5TRGktwztnt5FRJFoOpCaEO9CQ6QpJnat1LgUZsTb5Lfn4lRVHk9c9PnpIrljKrbzm6NihTgpnDMKtOYsDVTuXpUFAoyPuxsB4MWZijNK6mSivA6cmAK7tIHwlQ5OoB_V3bJbccLDR33D4J3CLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلزلهٔ ۵.۶ ریشتری در عمق ۱۰ کیلومتری در پرو دست‌کم جان ۶ نفر را گرفت و صدها نفر را آواره کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451402" target="_blank">📅 15:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451401">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuy8Evdy2QU6jJGs40lffL-hTZwvzv2fjsB-xhsWKk1nMPwHY79bEvloKQW3dUTDlQlD7HBG0sijLuAQN3fiLhkiCMX-Wxy5hfSUZUvD8w7GUfFRAk7EdbXaBTlzUcHCImiTdm4GceRDV0tJO57ei4ylGiMXu5sQeu8GO6tBihg50oMPi3EJkUqE3Xf2KgJuE9i0M7ft-WcWx1IPXrvoLUuXzhyOAGw5IrTAR_yw0B1mkD7dTsZD71CEqyqN9o3caIJht84PnP4UPVCJGWaxq_BG1dJtsd8D76QWT2mX4gBnDWzJ4jffDt_SwEPW1OWzAENJhdgqI6vseZ8q1ZNFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام نخست وزیر جدید انگلیس می‌شود
🔹
اندی برنهام به‌عنوان رهبر جدید حزب کارگر بریتانیا انتخاب شده و قرار است روز دوشنبه رسماً سکان دولت را در دست بگیرد.
🔹
برنهام که پیش‌تر شهردار منچستر بزرگ بود، با حمایت نمایندگان پارلمان، اتحادیه‌های کارگری و شاخه‌های…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/451401" target="_blank">📅 15:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451400">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678a1a6d1b.mp4?token=vSTncFNjF387dtk8rR9qp_WxZMIQwNHH8884idqC73mi2LFuTG-WGHZvL0-zoIYbR7V1fPimr2PQMzcCZQrCDuS_0-zfLc2emgl7njX39nk8LPVeHl98nEzWezKUnjgarMFZDqs1x1g0laq6Xr9gpGU9lrKPhBfNmozUPMTeasJnKjQ12WogLPyhYllq-lnMWFxvaSHccNTNgFfF3GDMG9FiCRwEDCaut9dsKD80vSMdKuqkHd0zdM5QyiovOXHcgdGVw4KSfQw0c4BS-3L-veiZzv0gXK1-Dn43jLBUMHb9MKwXtwmz0BC-vXzRAEYTe3uWLjAkWzqVZ8CnRzMMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678a1a6d1b.mp4?token=vSTncFNjF387dtk8rR9qp_WxZMIQwNHH8884idqC73mi2LFuTG-WGHZvL0-zoIYbR7V1fPimr2PQMzcCZQrCDuS_0-zfLc2emgl7njX39nk8LPVeHl98nEzWezKUnjgarMFZDqs1x1g0laq6Xr9gpGU9lrKPhBfNmozUPMTeasJnKjQ12WogLPyhYllq-lnMWFxvaSHccNTNgFfF3GDMG9FiCRwEDCaut9dsKD80vSMdKuqkHd0zdM5QyiovOXHcgdGVw4KSfQw0c4BS-3L-veiZzv0gXK1-Dn43jLBUMHb9MKwXtwmz0BC-vXzRAEYTe3uWLjAkWzqVZ8CnRzMMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هو شدن ترامپ در مراسم اعطای جام جهانی به اسپانیا
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/451400" target="_blank">📅 15:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df42e9bf4.mp4?token=cYk2Tb9AQq5Cus5dUDn8jC6Sk5X3c-k9iuXkehMERB8i8fAkvME0GbSe5RykGel1rHKKOnbCFn-U3YJaqHm2t0mvHVEEwOy8w8Qy1vG2zcJyvCJBnTJdp9c2BTio3-j-GgJJ6CAyvre6LNOhe7ZtZ0qhymPWO-G9xonZprYn45oj1j9Jnc770PsG_FPk2e0KDJFb3ohr0Ri7alLiO1Ny1lX8w7T5LiMhU9NAYNQu_4johHqgPzNfExczVI5l06fdA_m5Fd-NGq2g5LZ7AG_iedvofq7fOLhNVaIxkDKWjQDK2HO_Y7nx1YQ-AddX4IdowjRFH72OQWPNfQMuRJMm8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df42e9bf4.mp4?token=cYk2Tb9AQq5Cus5dUDn8jC6Sk5X3c-k9iuXkehMERB8i8fAkvME0GbSe5RykGel1rHKKOnbCFn-U3YJaqHm2t0mvHVEEwOy8w8Qy1vG2zcJyvCJBnTJdp9c2BTio3-j-GgJJ6CAyvre6LNOhe7ZtZ0qhymPWO-G9xonZprYn45oj1j9Jnc770PsG_FPk2e0KDJFb3ohr0Ri7alLiO1Ny1lX8w7T5LiMhU9NAYNQu_4johHqgPzNfExczVI5l06fdA_m5Fd-NGq2g5LZ7AG_iedvofq7fOLhNVaIxkDKWjQDK2HO_Y7nx1YQ-AddX4IdowjRFH72OQWPNfQMuRJMm8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو: در هرمزگان خاموشی نداریم
🔹
در جریان حملات دشمن ۵ خط انتقال برق آسیب دید، اما این خطوط در کمتر از ۶ ساعت بازسازی و وارد مدار شدند؛ هم‌اکنون مطلقاً در منطقۀ هرمزگان خاموشی نداریم و همه مناطق درگیر کشور نیز در اولویت تأمین خدمات قرار دارند. @Farsna…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451399" target="_blank">📅 15:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451398">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
زندگی در چابهار، بندرعباس، اهواز و بوشهر مثل قبل در جریان است
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/451398" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451397">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85dce6c68.mp4?token=JFk4sbmOpwV2-c4pHIr3jvDVl0ZAQxFPrbJAHVOvG8bdNXB25z1HbavKWKKFPcmkKjcHjHrw8ZGGmkiG08k0MPFY9emR9braR3ksQWrtJm6AEt7vHmujy6Rj4fMfuPaMxfOMjrNU4gdsfyRRMDgbM-usdqmVxW_vozcH3lIrDCe2C6o70SbQeAOdGg86aW3OlyroUVqOPzgDcUhwLxsBCW5qWm_HqgRwlTU3pjTfHbf-jqxFKqnyWG6XBZ_Tol7Ps9rCitKAIAWk7Py9_aHQCoQfNr0wx0GJ8ZSdmhj9Wmex-QPVerRirxDQcoRZ841OX8B0HnKlLF-2iFDfUsinmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85dce6c68.mp4?token=JFk4sbmOpwV2-c4pHIr3jvDVl0ZAQxFPrbJAHVOvG8bdNXB25z1HbavKWKKFPcmkKjcHjHrw8ZGGmkiG08k0MPFY9emR9braR3ksQWrtJm6AEt7vHmujy6Rj4fMfuPaMxfOMjrNU4gdsfyRRMDgbM-usdqmVxW_vozcH3lIrDCe2C6o70SbQeAOdGg86aW3OlyroUVqOPzgDcUhwLxsBCW5qWm_HqgRwlTU3pjTfHbf-jqxFKqnyWG6XBZ_Tol7Ps9rCitKAIAWk7Py9_aHQCoQfNr0wx0GJ8ZSdmhj9Wmex-QPVerRirxDQcoRZ841OX8B0HnKlLF-2iFDfUsinmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: به دستور آقای پزشکیان برای بررسی و ارزیابی آسیب‌های ناشی از جنگ به استان‌های جنوبی کشور آمده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451397" target="_blank">📅 14:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c184fefca.mp4?token=ihX_mBTIHSdBvo5u5XHbiM3WDHOoIBx9lyqf9lxOjseWjMLr550SkTxxyW7R-q3E_QRrftZCVIw9KAAhOwLBsCt8xq8gRMi6knmwADx414yzx1UORmL0M2is5Kd0VwdslwDLoFFiigMYKBu0fURY4tLuP1Ye8hevcvNGV-ywkMUMo7rhkiBqikpUbN83q4RZ2q2MWzcFjVtbkVqtridmlHMsXzulFm8fS4h0D6gboRIn0jLRgXQsloF8fVHe2AQtoIvDmAJZTQ9iutlA6oKED7epq3GNfgzcqtrnYFUH2nBE-5YUSUIuZTsl7QVc9iww6xx1rqessy7A51p4NcjukA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c184fefca.mp4?token=ihX_mBTIHSdBvo5u5XHbiM3WDHOoIBx9lyqf9lxOjseWjMLr550SkTxxyW7R-q3E_QRrftZCVIw9KAAhOwLBsCt8xq8gRMi6knmwADx414yzx1UORmL0M2is5Kd0VwdslwDLoFFiigMYKBu0fURY4tLuP1Ye8hevcvNGV-ywkMUMo7rhkiBqikpUbN83q4RZ2q2MWzcFjVtbkVqtridmlHMsXzulFm8fS4h0D6gboRIn0jLRgXQsloF8fVHe2AQtoIvDmAJZTQ9iutlA6oKED7epq3GNfgzcqtrnYFUH2nBE-5YUSUIuZTsl7QVc9iww6xx1rqessy7A51p4NcjukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارگردان «قمارباز» جایزۀ فیلمش را به شهدای میناب تقدیم کرد
🔹
شبنم قربانی برای بازی در فیلم «قمارباز» موفق به دریافت جایزه بهترین بازیگر زن از جشنواره فیلم سازمان همکاری شانگهای شد.
🔹
محسن بهاری، کارگردان فیلم، این جایزه را به ۱۶۸ دانش‌آموز و معلم شهید میناب تقدیم کرد.
🔹
«قمارباز» تاکنون در جشنواره‌های بین‌المللی مقدونیه و قرقیزستان حضور داشته و دو جایزه بین‌المللی کسب کرده است.
@Farsnart</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/451396" target="_blank">📅 14:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7b82dcd6.mp4?token=eS8qg9LHCkNQLS4BMoZ5fxuT_Sen1EJsK4AypTa093E4L95038bOe93UbVxmUmb4hQ9oBG2VxIKmf5D2EZsNhUtwY0dfuKXvDLI8WaGcOuK3alCu6bk8SA20PhL0UGTUf1jDbf78g76Hbj9NEAVHWcNtTEOAsoOgy3lznM1WxL197NEDRbW53J0K8IJ4Yna8QrTJg3SJX5FKt8v4W0CDl82F1OVG1pdodjUELJ6aLsbqHXmZF-vUtyLlciRoAJ9EygA0SbHy6otfTUhlBTk8ZjturIw1cdnTjVuYgFpORcOqrdXqi1fL-VvFqaPdctOREyM-J_oCLtMXrO0A16oZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7b82dcd6.mp4?token=eS8qg9LHCkNQLS4BMoZ5fxuT_Sen1EJsK4AypTa093E4L95038bOe93UbVxmUmb4hQ9oBG2VxIKmf5D2EZsNhUtwY0dfuKXvDLI8WaGcOuK3alCu6bk8SA20PhL0UGTUf1jDbf78g76Hbj9NEAVHWcNtTEOAsoOgy3lznM1WxL197NEDRbW53J0K8IJ4Yna8QrTJg3SJX5FKt8v4W0CDl82F1OVG1pdodjUELJ6aLsbqHXmZF-vUtyLlciRoAJ9EygA0SbHy6otfTUhlBTk8ZjturIw1cdnTjVuYgFpORcOqrdXqi1fL-VvFqaPdctOREyM-J_oCLtMXrO0A16oZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: هر کشوری که با آمریکایی‌ها همراهی کند، قطعاً کشتی‌هایش در عبور از تنگۀ هرمز با مشکل مواجه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/451395" target="_blank">📅 14:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎥
سخنگوی سازمان مدیریت بحران: تاکنون خسارت قابل‌توجهی در زلزلهٔ کرمانشاه گزارش نشده
🔹
شبکه‌های آب، برق و گاز پایدار است و ۳ نفر بر اثر خروج از خانه هنگام وقوع زلزله دچار مصدومیت سطحی شده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/451394" target="_blank">📅 14:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a54248017.mp4?token=fu8Tob3Zhg47uPUIgOXohgaob0bQkZYS5yJyix8-j_GdYkHPg01jUdD9HEZSEmkdS2OP6QLzW8xJ5v8S2HCW0hHJdwJCLubvUPmOfqoqx8Rle9oOjt6OPG0nqnIoTOdgoi9KzHeTgm5gGs9_cJUQQM7bZsVS8g2RRCW3d6PlHSiLBQ913OfRriIFLGwcVXSg7m6Gz1_4msawVEPUe8I-GGzhRNDjEtIqDgDhPiRd_w8aiwvaVj5B-32vUQIljQuYpunD5G0rexgxx294anyLW04m36e6mv6Y200ZF_OzV6gtJGqQu2ALmpHhPeFPA3vtWpDZdSKXu70DLnX5s5QlTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a54248017.mp4?token=fu8Tob3Zhg47uPUIgOXohgaob0bQkZYS5yJyix8-j_GdYkHPg01jUdD9HEZSEmkdS2OP6QLzW8xJ5v8S2HCW0hHJdwJCLubvUPmOfqoqx8Rle9oOjt6OPG0nqnIoTOdgoi9KzHeTgm5gGs9_cJUQQM7bZsVS8g2RRCW3d6PlHSiLBQ913OfRriIFLGwcVXSg7m6Gz1_4msawVEPUe8I-GGzhRNDjEtIqDgDhPiRd_w8aiwvaVj5B-32vUQIljQuYpunD5G0rexgxx294anyLW04m36e6mv6Y200ZF_OzV6gtJGqQu2ALmpHhPeFPA3vtWpDZdSKXu70DLnX5s5QlTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربات کوبندۀ موشک‌های ایرانی به پایگاه‌ها و منافع آمریکا در منطقه
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451393" target="_blank">📅 14:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSS9Awd314S-fq8WQwW5JlIHQ9FLI9dbCqi5waPynDMRnhoagSxs6iVo9c6slfByp1lp50ZBIYnns1M4RXu70p1ubePbSH_c7JJShKFwI7XnrXzTCen1ZDJ7NAXcXtt2lQPfY7QXCw0q9mbIgM3jm9_XEQxEC3w1aIY7sXTbZJ5-zpEToJFNYXUrza-M0hUZtGlvr1LKCiZP5FmOAkb6D1qgGnn4FJZGf-r_g3_dsk4rnqG2M0MZtgrAf74oVW9b0i7gfqcONLQsioZR7Ul9iIU1VteXfHFlwFdsK4Sn-QTPzRo6tQ3DPqi8G6wio479OrnsvKzFnxxapOls2nI7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خليل الحيه رئیس‌دفتر سیاسی حماس شد
🔹
جنبش مقاومت اسلامی حماس از انتخاب خلیل الحیه به‌عنوان رئیس‌دفتر سیاسی این جنبش (عالی‌ترین مقام) و جانشین شهید یحیی السنوار خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451392" target="_blank">📅 14:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
قالیباف: آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند
🔹
آمریکایی‌ها روی هوش ما اندازهٔ آی‌کیوی مختصر خودشان حساب کرده‌اند.
🔹
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/451391" target="_blank">📅 14:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451384">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4imlSh_OKpuvOF2bMnCJGSKCLhSkwRzPaGuSaAIyywHyJgDUW0s1aOE3uZjpcBa3sR2ekyaAO-cyS8C31f6IoApnrVPzWnraH1NtLeJqS8OE_ZiG4OTAENlY_ZI2DeFisIq2HKpGXCAoWYFjjAteqgeYYddA7RlBeXAvrK79fgMm6Z5ySzXAgA4B3avmBZtZBB1K6WbPzjjt_ZZsO0AdhJBK66e6cMoFD0GpYU7aEcjIp4uTz7UmwhdkHwRnAXPfUxYZzTD2c_nbQnoaFcvDLGH-rYHE-Rsd7TOAtJpYUjI93m9Ho8Ws8U4GdSsNbKlieX9xec37G4yClbKRtADJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPgyeav9pyH_FnPf36zPUC7-GDOcK5SC6vOd35YDo-5TXLbloGyv6N_JFsibaAPaXPLg3nS6RHRaV9Ey5M9txT9TP52TJ-HfKIvuyukDKSN5wZ1znZEK9bNLou1JODwyFxFmaFXnazfGBaPEqlinGdyYDzJaS1IUbjVeAXZK4CaoQnahDhAO162ggMg_R4R4XHwodkmiz7uqon1IZFgsh5xIfIhSsa8xHr1A65M3LfcjbsjKXWkfnReOtKUOFGfev0XrhGpWy9P12h1Vb3R47R6zrk0sJKlPQAZKuI0yJ87RSzMjF5Utq9Kt7gUCq5QzBdb0TCF2sLiSQgoTu4sHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9AvmKaFRSKyiCIFLRLooYcjT0CmOzfPhb0jkWidjrwhWlbDLLUtrgZ9zWfFzCEkofEkn32i7cINFZdRh7SFRtSTfudNxQebhs6JukCEkLAHSIfSzAdptIWlODongaKve5BU63Oh75HaznaTYH4eKjtfAdNtoCYY3FSfJ-EaNdGY1ihpX7dHYblqBlywcxZbK8ll7S2PKe9W94zN1J3GtI3rNnOSq4EIWnGi1Cb9RbOWG6naYuxCiIO_-vBd2MBJUJWZMsoZIJhbrnHw8R-h5DvX3OW21yp-gG6tjQSh-uD4IB-CyaA6am13i1of9n7nvoZZ4E3kOL7FIzEd0rTmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrzyybA3Xhh0ARbZmDKYIrEfy5JoqFZTIhRBXEY_cIuSp11kWJfhIpz6buts9x37kLz-U7sBLgLjihLNtoRNkm8HtNqPwz7WzhFAEspkPndQDofvbB4x8fmNO55M13pnZVBnElhlaPM57Tu4deIiItKG76sChW5H-ak-gQRwSyOnW2ZSM0_R60zoqdeu6SNjD_GJH7zWYSQaY9W68WlMSxsMk2L0cHPu5sJWDJXi8DZ6tPrpoUwEzE5NnDJxOfwKXgz4VjLAd8fVlNxJzKVf__iLcHm7-6XpN2GoJiR8hUrTejOJElle9vMWz6aH_bEg7GctpYqoK5fY8HyE3SRQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lR_4NHtYBSeKMnw3SJJ-8faQhftpcGTkifZLyARq15OkrDl72TJYMCgyNeSgPA5LpC6z_FIvK5FewWgOGzulJTowc0B_8BCqcJ4G6Cam5pC-4HRfDvRs2Cbx-vO5QQZXXOVW5ceFnI5OEjxhfPByi94KScQYc1Wcp7L5R_-z3k7LXoYS5X8HrndHjdVPnGiiTNNNsF1TYglV35EZw1BdZw_zJyz_jsMT7R0JvxKTl8tqwnRZH9pYrMKN0kZpFBTUL9cdHl-TUAyCkaZQsRnI7DBj-JPJDHTnRBe6me1VZOApxo4gxVB_cqPoiGTXk8XaFGHQb8w-IG1qLEFWOqhfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBxQe_aHkQDwBgikJSgv9tnUnRz2r5GrGblDm0ugI3_LI7vok0VpVZUK8R8gQlI302LNvetyEnjWRxoNEfwUvWLXhNeqOQWycurV402CtBUXkaLZTQMX58b4-1MEypIdIoUVYNlkiVffrLaak8gQ8Mwo3fpHT7e7y-CeC8PVWAu1pfzZaA3xM0VIRgUOZ_TBOhSqobsFL-sJ2JxQ4Ub9K8Y_ogB2wI06nERzZLyKfI0YT1lNvdEwWc90v0iW0NYOmDypwyt1eTC5cZUrkNscQrKyNPpewzqj5nl68DYm-VhWfyxjMrvQfM5XyGPNTP-X7FfkL97hqTsGwXr6IYSanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qG9X48JdAWFU_bqwnATZcmVSkZBgD5c_AFHxp51gUwVMJmxDsZoj_SJAaDNsIJTPkhPO73LiiRfZMN8BfbY3pyfFIyjLZQmcH9KMiuGZozQ6XVN8uOAkZBtew67GI2K8HRTHu0nCWUr8xd4TgBXlHoF_EDX_UsTVc3eKxWW86zAazHFDSlnyijq-pVBLs8p8zILdoiIbHFuj-oW6r82EnVZAWiLsgjZojCxzIe3H-cnIDokzBeNCThULhdDR1FXZ1NHxe7Qt0UV0StSNDaurEUSlmg_gEWjYdDt2Pa3M0hEQM4KJJtE2CyW91ih7hH3Mg_QehnZh_7P-rD51_JkHIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
درمان موفق تومور مغزی بدخیم
عکس:
زینب حمزه‌لویی
@farsimages</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/451384" target="_blank">📅 14:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm4PWGNS5cWv_o5aQgskia0fBhiX06BEuZ-jy26isG527_e83UbkXaZuy65CcBaQPzKHNCNFQoomf3VFWNHgyM6Wtyxn6j-pr5zypSu5T57mgv0xiz4A4KJJD1oVp8gnXLzCf-xErOWV2IhMxMLRp2C7RUqgjewysQIvfWwtCCaQ6hAyB2zvMEw5cKWUy_VLFiTRh6AjMlu2GOf_y_Xt7MpPmb6Rbi7vr2ig1e0oAo51wD8dggQit1hFnxC-xKKj3vSDVbraggFDmBdkx_r4FU-KxQFsRurEAAMhliqhL93aSSoNtMYoK-h9maEXblu7WnqIryUUwIbeT3TPOFC0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پزشکیان: همۀ ارکان حاکمیت باید از سیاست‌های کلان کشور پشتیبانی کنند
🔹
تصمیمات و سیاست‌هایی که اتخاذ می‌شود باید به گونه‌ای باشد که حمایت و همراهی همه ارکان حاکمیت را به همراه داشته باشد، زیرا در صورت فقدان این هماهنگی، نه‌تنها دولت بلکه کل نظام با دشواری…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451383" target="_blank">📅 14:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پزشکیان: مهم‌ترین میدان نبرد امروز، عرصه اقتصاد و معیشت مردم است
🔹
واقعیت این است که امروز ایران درگیر یک جنگ تمام‌عیار است. جنگ امروز صرفاً جنگ موشک‌ها نیست؛ دشمن به این نتیجه رسیده که با حملات نظامی نمی‌تواند ملت ایران را به تسلیم وادارد.
🔹
در میدان نظامی،…</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/451382" target="_blank">📅 14:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNKB3vNEX26BNbPfOEDn1CW3M4LpqoubnLjX-q2OEf0qffCSh_nrdAKz1fq0Qkm5j1EPg1MAz74LtZHfneVgmS0SDrQgLIj3w0gELkekPJBP3Ke8Ry-ZynHcZlksg-RW91dPi1I_mlSSUnwkm1R1m_x2ohOKeA3dv4jG9n9ykTgE0qcImGbr5i5hFWynRwWjxZtc_0WCDopUfbXQuCWDSUApxTmFZtAPFllh-FX1sSENpg9IFGjcY6O94aDG2V1BBrnxtzExH4y3XNSR1pR2FC_O3i2bfBo8gHO5LQGvuKfzWq8UUbBizjA0gUYLYEyMq3uyPdQLSKbVzISgLGG7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGhE_BDFnlZYLqtEI_gfqG4X8wH5GU9RKfbQCE8lOXV451AlegJzzlpx7P_MkbSxHCm4Eq_RFhWDApD4XLFZOBo-92L1PzhxafEYFY4fTGJJJT_PIOmANaBcr6j2clxlorB1wp5gtb65IYr1yJjMNaP4Suf-WqtPsES7JTFUn643nismnG9SXf60Ra9UWRtgahuu884kg95k4C9_I_jS8szUpuE7pf5RyBHe_WOoi4vY0SlNCCEXpi7Rwl6iKGJpn5egk5RzKIPXvVp-Zhtw9rFoHuKsyq8TpfkRuJT79EDe4flyjPQGxln8pP_E-pqR4gmlch2QeDNu7JBHVDaayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJ3NDdk7mG9DJ5R-tgzZ8cb10oQX8-5o702F7prSfmmQSx3oV1-HPKY5dVB-bETpZsgA5bDcNUv9CFhjgS34SWTnGxtqTR9fPLiIyO7o_ltFgRNeX3lJ2GkGNGjEZLWctVLTOjyEZPR3Y5LPoWh1RBpJUWAEZ9mALRCVVT0dN52sy8N3q2di9bdt3802cMjkQ1EQhby892dx5idykQtUThikJCh54nvg1wayJDhRmqVrb9SvmV3pB-2lzoJM29xzrGkT0d-zoM3o2H0wion6NVAkbCF8v39Yu-9y-u8M0hapl76Is0xhIp-4-PjlDMIgx33N_ByMVeJGvD9BdMneuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuWMBecf_po9IVLbPZNHS6cx_1xvbpInWlWxYfCgPSiwf4bKrm3rh1J2aA5xafNUmXj0BYju0P4adRf6n_607L6Xv1GKFIV9wWoZXOeE5930HrcNeF6qckcIWQEfbCXqfl5vdpDSnA6aqzBpuZKVBANfA1jtiXbLQQz7s4nOL0A0-5D1CX4XaGxHXI9z6A53r2VVeN9rsSu9z0WkiXHe_0GcvXStWH443V7g7s1qbHTNMaH-zAcezamsSEUn81GIk0_Ul9GzxlJETm9Yrx7fzFKjopfeZEN_hyyWq_eN8zeFaqFuqu11SJhbm8k5AFX1Y-SMSi8g-O-DF_6HobqOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_gytnKD_yoGpoG4r6fCi-ZzHGfPMa81Lg03t79A6DCwJBvsKWJs56UvNT8gu6-c6g6m1q7aOBuvDwkRuMNdoqcgJOMm8yaxlQIoQWdF6wuiPjzJt_R8ZdcAvJTYUCZyLjpLOcke7f5QW7-rzI-bx669dfHQR5FfEX_bE2ta15JG2fKKZx1ydrTRpuvcsHpJEa8Cc2E_i1Dw1WxEqckzLgCHx_ntKgCRaMqtco6ZJS3pj-RJdyxH5XEeNS0knvPUT4q23bCbm8Y-NrcFfjB5-Y4-R39KNEtr3p6YP0RqulYiG-yaM-tIRwwzwJKxP6S9j7juKSav-MGdSEw-eV29eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTNu_gnNG4ED7PLhLGs1gEr8nDXDuMvzV3-ZqdVMXjhEjyeT1IqWQ1teUsIfXJ726zMWTnjKIWDSCACt50ZMq9iaSlmyZPAaDgEjXGaFP57vxmVVZbordIyhNFI90W-sYPKPpDCGYWpbyof5vmSL2EKb0uGx-we7CzYgr_voJRAcEvWNPBxeQ5j-Xpg-NI4dmaeYlqn-R6yTON__dhT0uGEgL832DamBekiTId_3-wUoNJdMXcu9SxK5KO19Kn8Aue6XRIdqfGjVCTBejpvdIL9HVvVlz1PpnGm-Z6C5BRgye0KQIH-plUY8e8wyMrQhEO2joSaJIYuH8aO5cSV3sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر جدید از خسارات ایران به دارایی‌های آمریکا در منطقه
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/451376" target="_blank">📅 14:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پزشکیان: مهم‌ترین میدان نبرد امروز، عرصه اقتصاد و معیشت مردم است
🔹
واقعیت این است که امروز ایران درگیر یک جنگ تمام‌عیار است. جنگ امروز صرفاً جنگ موشک‌ها نیست؛ دشمن به این نتیجه رسیده که با حملات نظامی نمی‌تواند ملت ایران را به تسلیم وادارد.
🔹
در میدان نظامی، نیروهای مسلح با اقتدار از کشور دفاع می‌کنند، اما اگر فشارهای اقتصادی موجب شکل‌گیری نارضایتی‌های اجتماعی شود و این نارضایتی‌ها گسترش یابد، سرمایه عظیم اجتماعی که مردم در حمایت از نظام ایجاد کرده‌اند، ممکن است آسیب ببیند.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/451375" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52f4bb1e8.mp4?token=XwK2domPm6xmqIk428pJcDPWxLjT3BLS_KEz10hsmYyvuXKDIMTkv2Oh5qBTCtSVREdcBt_IA3LSaETz-nj_0YrqM5pevKRHmU_hS3q1e6eYf1Jrdj2yb2sbnNP6Q68ueqg8aEQGmoZM2Nai9PJzWQZrEMZ2XdJURgsx3PGe1YeO4I4IqXmtRdK46nOHMPRETMiQFR_59Rv4DSx-II9bDzp_nBi-ZZUBL2VanKJQxYnAJnIrZN3ZTCcGLRmPJsKQLfwR1pV3gZF4o2pTPunZ8OMkOlGuqwsPAjlm8PNv515VMV2sO1vDVTF3NJlun40ebpbxHuRX8jlFJTkabhsbcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52f4bb1e8.mp4?token=XwK2domPm6xmqIk428pJcDPWxLjT3BLS_KEz10hsmYyvuXKDIMTkv2Oh5qBTCtSVREdcBt_IA3LSaETz-nj_0YrqM5pevKRHmU_hS3q1e6eYf1Jrdj2yb2sbnNP6Q68ueqg8aEQGmoZM2Nai9PJzWQZrEMZ2XdJURgsx3PGe1YeO4I4IqXmtRdK46nOHMPRETMiQFR_59Rv4DSx-II9bDzp_nBi-ZZUBL2VanKJQxYnAJnIrZN3ZTCcGLRmPJsKQLfwR1pV3gZF4o2pTPunZ8OMkOlGuqwsPAjlm8PNv515VMV2sO1vDVTF3NJlun40ebpbxHuRX8jlFJTkabhsbcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: بخشی از افزایش نقدینگی در ماه‌های اخیر ناشی از افزایش ذخایر ارزی کشور است و این به معنای «نقدینگی باکیفیت» است
🔹
سیاست‌گذار برای افزایش تاب‌آوری اقتصادی کشور برنامه‌های متنوعی در دستورکار دارد و کالاهای اساسی و نیازهای مردم تأمین می‌شود.…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/451374" target="_blank">📅 13:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70933c45cc.mp4?token=a5HNlSfigkxebeHQc2okBcuu5SYIvR6z2wafoyEPdWjcApQDjFnkBcy0_dD1KbBhIfcqBen14Bg48bwQC77Su2ToULOiSUEBK9mszA21kF15XCCj2l2cpViPT3K7bJ-LqkQ9-QS-0nLzNLmOGuiPN51_RNPA-w9LEKTEUACfbigmUBtfmxUxH7bMm-Hjb2PqgLbbxICOfZ97R2iOsdv4GD1FJW5_qcfrQ3cdka2bLGl3VD6AH48uf5vOgS76GfWUdKIdvxZF6KKnt2Ti06YiwmhHX2xIrukAgX934Zl3tBvE4BrSRcKCiu39nnV1UbKVunqKGfzLuwTjp1-HajJFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70933c45cc.mp4?token=a5HNlSfigkxebeHQc2okBcuu5SYIvR6z2wafoyEPdWjcApQDjFnkBcy0_dD1KbBhIfcqBen14Bg48bwQC77Su2ToULOiSUEBK9mszA21kF15XCCj2l2cpViPT3K7bJ-LqkQ9-QS-0nLzNLmOGuiPN51_RNPA-w9LEKTEUACfbigmUBtfmxUxH7bMm-Hjb2PqgLbbxICOfZ97R2iOsdv4GD1FJW5_qcfrQ3cdka2bLGl3VD6AH48uf5vOgS76GfWUdKIdvxZF6KKnt2Ti06YiwmhHX2xIrukAgX934Zl3tBvE4BrSRcKCiu39nnV1UbKVunqKGfzLuwTjp1-HajJFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: ادامۀ فعالیت بانک‌های ناسالم و ناتراز را تحمل نمی‌کنیم
🔹
مهم‌ترین ماموریتی که برای همکارانم در بانک مرکزی تعریف کردم، کنترل ناترازی بانک‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/451373" target="_blank">📅 13:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c95d9957.mp4?token=DqnVTzGzck8dJYoY9JrvSfPnOD93UTZAwFFtj891EWgimQvA0gU8cXqc71t9tlaOr_Ykrsqi14YYIMRqcJ8j3Vr9gQDwGOjz0zAkKjdzqfeqVOpdWjA_d_Skv9ZZpZjfj2Ic6qXRlQmx213mcWfTSuwktkyQ-Zgb0f50YfZDhQ4qyzA6ui7Um3L9A1516cNrup6wveQO_Szbah_DHmp3vUB4lh4pxjbo17wJy1iR7C2MnOCQlnVgxnCdz3VHMaCzQ2pLwL0_pi_nrebdMn8H7XLwiEdX9XAa_2Rv4NxXtisvN9AmCkKRJYVWpjnAK2d65tNw3gG0L7OqMrCo2w4Eag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c95d9957.mp4?token=DqnVTzGzck8dJYoY9JrvSfPnOD93UTZAwFFtj891EWgimQvA0gU8cXqc71t9tlaOr_Ykrsqi14YYIMRqcJ8j3Vr9gQDwGOjz0zAkKjdzqfeqVOpdWjA_d_Skv9ZZpZjfj2Ic6qXRlQmx213mcWfTSuwktkyQ-Zgb0f50YfZDhQ4qyzA6ui7Um3L9A1516cNrup6wveQO_Szbah_DHmp3vUB4lh4pxjbo17wJy1iR7C2MnOCQlnVgxnCdz3VHMaCzQ2pLwL0_pi_nrebdMn8H7XLwiEdX9XAa_2Rv4NxXtisvN9AmCkKRJYVWpjnAK2d65tNw3gG0L7OqMrCo2w4Eag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: بانک مرکزی منشأ تحریم، جنگ یا کاهش درآمدهای خارجی نیست اما این بانک مسئولیت دارد از تبدیل این شوک‌ها به بی‌ثباتی پایدار جلوگیری کند.  @Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/451372" target="_blank">📅 13:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451371">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c90d5c5af.mp4?token=oM6wNMAtu1ey2EVAnJsQ1IJSBYzbjm8mTPuSGp1AxAHuexcdZSfLNMCBlDQ6R2cgGm1BeUVkpZcHPgw-utswb_dZR8B9v3WB7GelaaWdKmR9hj3FwhfSmk73nxvLxClEvI7HFh9puHsBKTH-a707kUEiiUNabb-a_mRatz5V0Z-0XEhXSqBvIlLASRKKhoC0G57JRUrbhFCgeW24hJVzOC2LoNnMdmhwAEi8VcOjaX1gPnNAQz_dJh46jRQ6ah4ARCyeWW0CPkNxoU94KYnMnXFpBnDvJ2WLHLK-ZBtaLgERN7ziweY0v_zNfXELYeoWQYV8hj2b3Cmw885vP77TCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c90d5c5af.mp4?token=oM6wNMAtu1ey2EVAnJsQ1IJSBYzbjm8mTPuSGp1AxAHuexcdZSfLNMCBlDQ6R2cgGm1BeUVkpZcHPgw-utswb_dZR8B9v3WB7GelaaWdKmR9hj3FwhfSmk73nxvLxClEvI7HFh9puHsBKTH-a707kUEiiUNabb-a_mRatz5V0Z-0XEhXSqBvIlLASRKKhoC0G57JRUrbhFCgeW24hJVzOC2LoNnMdmhwAEi8VcOjaX1gPnNAQz_dJh46jRQ6ah4ARCyeWW0CPkNxoU94KYnMnXFpBnDvJ2WLHLK-ZBtaLgERN7ziweY0v_zNfXELYeoWQYV8hj2b3Cmw885vP77TCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: بانک مرکزی منشأ تحریم، جنگ یا کاهش درآمدهای خارجی نیست اما این بانک مسئولیت دارد از تبدیل این شوک‌ها به بی‌ثباتی پایدار جلوگیری کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/451371" target="_blank">📅 13:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451369">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjTLUH1_cGsdG1jz_SzzKI91pHAohS-f5fxjAstgIk_EI_TMfUfdldRpldWWQOReZhFyGDvjs8G7bXY09AP4IJsc3LEtbZwye7Q1faHv1ZyhqFBILhI7RKlZY8VEMRIXgGULNT0veU5R64wG0HFjFyyuOdODapdeV8RGk8bsuWAANIeBhvw9edAxb2bQReKa7NfiFaMgH_idEIBn0qB1_uHPC6sCi4lTph9ZKcb0Fc0ljweorwergSXE2fA74gGvbwEH5gZPeFi3icsWG86hDc7KZdnbGVy5SwxX6XkXlqGTaM6YtATq-xsIPtEmisgUG5wnzak8Hbbp82zJWOv1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LayDOjZ_irQCgMsbDsH-4_sT_wQhgFT0pCRTD0SlcRqLHkLUbMb5vi1HhYoE_vhV__lpcDW1KKFY0ThDZSsqUuqasFge8oHZXNyajB00kV5XvypetTbgNMbdJGEtwvI4gmkmn3i0VGTwVTm46LYLB4nlcStmEWc2mUh7f8Dcnnom8RXsEOM4_YzgpYwxfgX6PtpcwqREp-PPabWqEh-CUxJjjQfYC5Ya1MtShEMDPT2X2D_0VJu44dPakdxuxLgLujyYY68kS7OX3LHb3jCHydgZSu2wXxluQPFbNnbzQEPn7_aICNNf16diFulRGT-r4mkUI3lm1vqhyhEZ6h8m9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر فتوشاپی از عکس معروف مسی و یامال، پس از قهرمانی اسپانیا در جام جهانی ۲۰۲۶  @Sportfars</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/451369" target="_blank">📅 13:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451368">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65616cf8d8.mp4?token=IGs09kotExFmKwUBFIo0fHLsBhzs0FkPwGNpDuFsMMvNVwwNiLOSnAy_ahHx5pPDHtbwWhaFyyCvao7DPqLHaqs38_CtgIEGazub6IOrHmh-fTgKWTIIpEOCdiYk4pya1iWTlGiCXYR32F6eHoFS7ibL-9yqkNKHkz_NlfM1Y13mfmHakSyzrcoYndanSx0YcMOFOch4A6CYbOPYbwVp0kk_FL2TGAmLGz7XuhC9qUtOhaZ43-PhIrergh13BcHPvaMeOCoL6Im9-MawKtjO-CaHKELHwCJhEtDRv-4q1BNEGnFJEQYWgT5c7G3ZSu8K3XliCV6XqDvDfKKBxZHiAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65616cf8d8.mp4?token=IGs09kotExFmKwUBFIo0fHLsBhzs0FkPwGNpDuFsMMvNVwwNiLOSnAy_ahHx5pPDHtbwWhaFyyCvao7DPqLHaqs38_CtgIEGazub6IOrHmh-fTgKWTIIpEOCdiYk4pya1iWTlGiCXYR32F6eHoFS7ibL-9yqkNKHkz_NlfM1Y13mfmHakSyzrcoYndanSx0YcMOFOch4A6CYbOPYbwVp0kk_FL2TGAmLGz7XuhC9qUtOhaZ43-PhIrergh13BcHPvaMeOCoL6Im9-MawKtjO-CaHKELHwCJhEtDRv-4q1BNEGnFJEQYWgT5c7G3ZSu8K3XliCV6XqDvDfKKBxZHiAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اصابت موشک‌های ایرانی به اهداف آمریکایی در منطقۀ عقبۀ اردن  @Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/451368" target="_blank">📅 13:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451366">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt9L0yA_Yb-TdKxW38lsAGsZR5VUvaFSovwppRaER8XD89DNY9rja6KAKSv5wITEZ9qh5iXdX7f5UNiRcjn72mkCNrtozBGuK_FX3KhypAEsKtSEGJNv3ey1xt3ozmpdaMj0a2vzWlBDpHTt3CB4S6p8j2sLHOmO7qtWOkdbl1rMET1nArDymFNcWY-G0ERmpkkH6l6cTEVF6G940hOi5gCw15A57IciaKCGPU5RXKLvkXzzR2buW9P6-Kr1fmqTfNtOPSuJImXY8Ja2Sh_EO2wfgpBZ-d8-PFXqw-CMQUdEVCN_nDZk5ot7LAkRXaNuitSa0sw1HLms5ekyOOlTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سابق دانشگاه شریف: ایجاد دوقطبی «جنگ و صلح» کمک به دشمن است
🔹
در شرایطی که ایران مورد تهاجم دشمن متجاوز قرار گرفته، انتشار بیانیه‌ای از سوی افراد و جریان‌هایی خاص که بدون هیچ اشاره‌ای به متجاوزین، جنایات بی‌پایان آمریکا و اسرائیل و محکومیت آن‌ها، صرفاً بر «صلح» تأکید کرده، واکنش‌های گسترده‌ای را برانگیخته است.
🔹
رسول جلیلی، رئیس سابق دانشگاه شریف در این مورد می‌گوید: در شرایط جنگی که ایران مورد تهاجم سوم قرار گرفته، انتشار چنین متن‌هایی نشان‌دهنده بلندکردن پرچم ذلت‌جویی است. کلماتی که در این بیانیه به‌کار رفته فقط کلمات ذلت‌بار است‌.
🔹
تعجب می‌کنم چرا این آقایان و خانم‌ها در این شرایط حساس که امروز شهرهای ما مورد هجوم قرار گرفته چنین متنی را منتشر کرده‌اند.
🔹
این متن به خواننده منتقل می‌کند که نکند ایران به آمریکا تهاجم کرده که توصیه می‌کنند دست از تهاجم بردارد؟
🔹
آیا انسان با شرافتی می‌پذیرد که وقتی مورد تهاجم قرار می‌گیرد، از خودش دفاع نکند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451366" target="_blank">📅 13:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451365">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۲ مرز جدید به مسیر تردد زائران اربعین اضافه شد
🔹
رئیس ستاد مرکزی اربعین: امسال مرز سومار در کرمانشاه و چیلات در ایلام، در برخی ساعات و به‌صورت محدود برای تردد زائران استان‌های هم‌جوار فعال می‌شوند.
🔹
سال‌ها ۴ مرز مهران، شلمچه، چذابه و خسروی، مسیر اصلی بودند که در سال‌های گذشته تمرچین و باشماق نیز به این جمع اضافه شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451365" target="_blank">📅 13:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0D7uZCUFK8f28ojXiOykBmqGt3IDRDQ2H9G8957q0Y3idVsRQPsuSEpnUDg1A-JT3G5njj53-okdfHMb6Ff7Lnm3DwHUGMJH3Vp9I-z86dkHaOwkXnPu45iXJxRASFiXEPu5sImOTJXYZGHo1XSp95cPoPGcwlP8N9KKHGCfZFR-M2SeD2UgXBQwqG_jCjf5PtgX1MwAoMBzwchN7OEJEGGNI-51Wp7oxhs9TphfTl7IhevWSpjxU-Rd3UYJSJn_tZrHjPOM6xlIvQ0PwUBLZUJyz2KjctVN0SG69tWSp867epdR2LSFCbBlgPX_eXpQSq5AqS7SyjphTOcrT7FOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر الهامی: به‌روزرسانی توانمندی و آموزش پدافند هوایی ضروری است
🔹
فرمانده قرارگاه مشترک پدافند هوایی کشور: نیروی پدافند هوایی ارتش همگام با تحول مستمر تهدیدات هوایی و پیشرفت فناوری‌های نظامی، برنامه‌ریزی‌های لازم برای ارتقای توانمندی‌ها و تجهیزات و به‌روزرسانی آموزش‌ها را در دستور کار دارد تا افسران آینده بتوانند متناسب با شکل و شیوۀ تهدیدات آتی، از آسمان ایران حراست کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451364" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451363">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF1WCbFjsPEtZIRwYOXYkJJGlWXq7RS3GenbJ0JOVYGZS1xswbcafy-WDQyLwdNJMaYWjncwSoqyEk8wHITPDwk7aSYM4AeH8hWDLWZWpdBGtTNxsW20uJeSgCLWL5LlxkvaB3O6jniwS6Vn59N46IAqP6tOyygxlbHbvw8q1EdWjGHjJUofXlpK-Rules-s-WDhFS5Qr7rdLQ1YyxCVHEfg6TtjRqQLPvMdWU7hrNbspnrWnYuKQ0CkYWJSoge-0DLS3zuxuRRhKIMoLKq5zg4GcOk3SBJS-uxD5dIG6dO9_iMJC7LSW2Oe6mifoek-f4kmHz5is7SU-cqFQF4q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به کانال ۴ میلیون و ۸۰۰ هزار برگشت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۵۸ هزار واحدی به ۴ میلیون و ۸۱۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451363" target="_blank">📅 12:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451362">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7187234822.mp4?token=oiwVmhXrAI5Un41ZQcy0dva_qEZuRxejb8at_fZkwNpvFRaKsIsJoJIRkX1Mm4nbLQNvS6pikDTlgfAbZyH6yEDwqRQLlEMcnvI88yfrGCWI7UoknTEVjAFFXOgQfAhWJ5e1aM5z_L3P6GQXURxeBt_GmRGriWwJ_d9jFE8PJ8Kr40_oY6DtrltsXzS9p7EJhWR8wZeRQoJhSy_6cLI57A1aXTo5OMcAV4gQKBJ6O_6a804O8Zlg4e0R9iJyos1z_nBObFeBlYGMUCxCFLVpMhX5SxyegOGj_2n2aMF_TL5t5dbvu1mvyLKCHfy8MgcTHdhV-U9hTtLR0BvV4oFncA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7187234822.mp4?token=oiwVmhXrAI5Un41ZQcy0dva_qEZuRxejb8at_fZkwNpvFRaKsIsJoJIRkX1Mm4nbLQNvS6pikDTlgfAbZyH6yEDwqRQLlEMcnvI88yfrGCWI7UoknTEVjAFFXOgQfAhWJ5e1aM5z_L3P6GQXURxeBt_GmRGriWwJ_d9jFE8PJ8Kr40_oY6DtrltsXzS9p7EJhWR8wZeRQoJhSy_6cLI57A1aXTo5OMcAV4gQKBJ6O_6a804O8Zlg4e0R9iJyos1z_nBObFeBlYGMUCxCFLVpMhX5SxyegOGj_2n2aMF_TL5t5dbvu1mvyLKCHfy8MgcTHdhV-U9hTtLR0BvV4oFncA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: منافقان و نفوذی‌ها می‌خواهند مردم درگیر مسائل دست‌چندم بشوند
🔹
یک فرد نفوذی و منافق با تابلوی دشمن به‌میدان نمی‌آید؛ او با پوشش خودی در داخل صفوف ملت قرار می‌گیرد و تلاش می‌کند با نشر شایعات و طرح مسائل سست و بی‌پایه، مردم را به‌جان هم بیندازد و…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451362" target="_blank">📅 12:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451361">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4528a984.mp4?token=lpsiYXI-xxq3ivmDEBunerp10itt8qMf1xvOcpYI5r6GXueotdFNRHLk0zvOh1ln4vutGxY3KgNsKMp-FrAG1OITt8VKtRr0sdORhC54jx4eMBNvEYwFxZuUI6XEIgtj40vVBLlZjdNZ_mZWS0ShVQ4U-WgCPkUnDZ11EoJezL22E5HPXVnaLh4d80Bc-mPA3rAAQcIZir5bN4kSaSUV7HgohzgkjXfAM8xhiM7XBYy6WFJfe-MNdA6-5ugyQNQ9DqWd-hk_OX3hLbPyGmakdYlCjeWp7zuYk_gF3xDUONrjueCMYzi46gIix5LjZzYEIYlaQKMKYzXYbM-YfgKglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4528a984.mp4?token=lpsiYXI-xxq3ivmDEBunerp10itt8qMf1xvOcpYI5r6GXueotdFNRHLk0zvOh1ln4vutGxY3KgNsKMp-FrAG1OITt8VKtRr0sdORhC54jx4eMBNvEYwFxZuUI6XEIgtj40vVBLlZjdNZ_mZWS0ShVQ4U-WgCPkUnDZ11EoJezL22E5HPXVnaLh4d80Bc-mPA3rAAQcIZir5bN4kSaSUV7HgohzgkjXfAM8xhiM7XBYy6WFJfe-MNdA6-5ugyQNQ9DqWd-hk_OX3hLbPyGmakdYlCjeWp7zuYk_gF3xDUONrjueCMYzi46gIix5LjZzYEIYlaQKMKYzXYbM-YfgKglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: تصمیم‌گیری در زمان جنگ نباید با تأخیر انجام شود
🔹
بدیهی است که در زمان جنگ و شرایط اضطراری، تصمیم‌گیری در زمان مشخص مهم می‌شود و ممکن است اگر همان روز تصمیمی را نگیریم، دیگر فرصت نباشد.
🔹
باید همراه با نظارت، به مجریان قانون اختیاراتی داده شود تا…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451361" target="_blank">📅 12:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451360">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3f84a931.mp4?token=APp5tg-hxT-UaIwLv9pmft7o2ZXkLm4FHnD7YBnwEzqAe43k_PRvRmGMfIW7qX-PRZBoVY2-5UtzGkTykpwdTvCKbKJT40kwQ-nBf7uXZPauM5JN3jESWxf8iktzkq3LaW8PzgraQI5Q6ZCJIvJc-MUe1a-dMctQ_1NdTSXHj_LPeBe6UEggLhrTai34oKxrNujDGOeGvCDCWaYp8dBLdIcDxBMyEAEgc93LNAjZmRTbNLKeihjquIKOkGOyLMwriEygak_QUZnfocG8Bgcyj-joe3QA6cIw3jU1K_sZD8J2RkHEEj0gCOY93mBigL8PpSWFXZSrhA2J9C-gjJcMkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3f84a931.mp4?token=APp5tg-hxT-UaIwLv9pmft7o2ZXkLm4FHnD7YBnwEzqAe43k_PRvRmGMfIW7qX-PRZBoVY2-5UtzGkTykpwdTvCKbKJT40kwQ-nBf7uXZPauM5JN3jESWxf8iktzkq3LaW8PzgraQI5Q6ZCJIvJc-MUe1a-dMctQ_1NdTSXHj_LPeBe6UEggLhrTai34oKxrNujDGOeGvCDCWaYp8dBLdIcDxBMyEAEgc93LNAjZmRTbNLKeihjquIKOkGOyLMwriEygak_QUZnfocG8Bgcyj-joe3QA6cIw3jU1K_sZD8J2RkHEEj0gCOY93mBigL8PpSWFXZSrhA2J9C-gjJcMkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نشست شورای‌عالی قوه‌قضائیه امروز با حضور پزشکیان به‌عنوان مهمان مدعو برگزار شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451360" target="_blank">📅 12:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451359">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUrRW9HaHK0241nJ3c0j8sRR--YI_aD_AmtyW6vrisDLq3NuM3x0CqKQc7Ivwt0CPQacQTDNTTVyVqJpKaC-6h4qpSvGSU7uF5CJTJXLi4nqu1z0SnBOD70sgWArBN7bJPSpN6syaELxiq0VD1DIvJlpz5HRbprk9foax0kvS7VnYhCwvU8FrkqNfN-MwHP5wZ8Ppzubv2Si0B12I56iR367Gc5fyf4DJZKFiJUZVQkHK-HfqcgkctxdK6m1uO5S8Ncj_cce-MK3EdqvVlmce9pD9f_AbqrPRk6FhKrWkewzqQnmuB-Er9RowG_Yqo6eCXzToYdjpVWlHEdLBSvz8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تبریک قالیباف به روسای مجالس اسپانیا به‌مناسبت قهرمانی در جام جهانی فوتبال
🔹
پیام رئیس‌مجلس به روسای مجلس سنا و نمایندگان اسپانیا: قهرمانی تیم ملی اسپانیا در رقابت‌های جام جهانی فوتبال ۲۰۲۶ را به شما، مردم و دولت اسپانیا تبریک می گویم.
🔹
دفاع شما و بازیکنان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451359" target="_blank">📅 12:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451358">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4M0IcXZv2FqC8Tdf53wxudanDtvD5HKq-U_dbrFD9hoIS138vAMRbznh2sWxLrE1iI7Sr_EgQddigS3dRYs8vG4hENKWdL5z4WknA1oX05sdBlH9K0HIz8CEugRMRZ1MQOQfTO6bTGcppQ1ZX8gFw-thjRSbMJ67nKQDaPG7ERJ3rXxNcsVnt_17991URbgCECKGBoLMIm06kBznT1D4LbF_4fppIX6XaZM7is7FAgZ1dnC-FCSc6sJDZOQzCaaUmgoyYrpUh-JJ7sisol5SR7_kDgxNVaEYU63qO_bp8o1BzZCJCbQNUDxudsAimnjLWN4siksBk6N23ZHxB075Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی در بیمارستان نیایش خرم‌آباد
🔹
دانشگاه علوم پزشکی لرستان: لحظاتی پیش طبقهٔ همکف یکی از بلوک‌های بیمارستان درحال ساخت نیایش خرم‌آباد دچار آتش‌سوزی شد که با حضور به‌موقع نیروهای امدادی مهار شد.
🔸
دود مشاهده‌شده در خرم‌آباد مربوط به این آتش‌سوزی بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451358" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451356">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6739b20d2b.mp4?token=B6pR-BYRznWv_qAoaGIQ_vFqdLDpD_oG2XCZBs17hqvyFgnkMOsWjLDzJQXUqhixw8qZR6hx-M40N3NFMNi6NYrOoeoEz3SOt1GKxs-WtBhAel4Id3VdTinkSu1c5o99NQnDgOR4KvFLzNOfyswaR2SbpObWg6EbQRh3d6gNS6g5IFrMdpNf3QbwmlV1TNhIfERqRumy7sZ7mySM3ZV3yLDIBBEqijhgIb_xY4eqYQSVMcxSxQXg0pb9JnMAy8ndzpGJ0XKE0sB_ZgwtPutTBfsYrzu-kRzw5mlPYJ1QW8DKKMDOFUP_MlLUYvvOND5EoKECwF4-_v1doF3p-CGsJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6739b20d2b.mp4?token=B6pR-BYRznWv_qAoaGIQ_vFqdLDpD_oG2XCZBs17hqvyFgnkMOsWjLDzJQXUqhixw8qZR6hx-M40N3NFMNi6NYrOoeoEz3SOt1GKxs-WtBhAel4Id3VdTinkSu1c5o99NQnDgOR4KvFLzNOfyswaR2SbpObWg6EbQRh3d6gNS6g5IFrMdpNf3QbwmlV1TNhIfERqRumy7sZ7mySM3ZV3yLDIBBEqijhgIb_xY4eqYQSVMcxSxQXg0pb9JnMAy8ndzpGJ0XKE0sB_ZgwtPutTBfsYrzu-kRzw5mlPYJ1QW8DKKMDOFUP_MlLUYvvOND5EoKECwF4-_v1doF3p-CGsJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجربهٔ ایرانی‌ها این‌بار هم جواب می‌دهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451356" target="_blank">📅 12:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451355">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تکذیب دستور تخلیهٔ چابهار
🔹
فرماندار چابهار: تاکنون هیچ‌گونه دستور تخلیه یا هشدار رسمی برای شهروندان چابهار صادر نشده و شرایط در این شهرستان عادی است.
🔹
برخی رسانه‌ها و جریان‌های معاند با انتشار اخبار نادرست و فضاسازی‌های هدفمند در تلاش هستند با ایجاد رعب و وحشت، آرامش روانی شهروندان را برهم بزنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451355" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451354">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkYZzvVEvd6nIWmQkUm-ivfiIGMgr9oXhBiXMBzkMatuD2C5Vr1aeZt6DyXNI21k6jRtWVwz8Ql3a7XEOqV4tAiYy_fbI9DvNctEsYZcNoDcV8k7_NeAQbM4cVkYEbjnRO63e2pqVfFgpg3lQ5J6x5Bj_bB3kSMbAVLM260KT1mi640A9hXu6IoeTov9Ws1PhHh8b7zVk6NL_U6XI6BZfKnEdoMgA_s2VMoia39rcGfh5LXxjyQpQ3-DPM7i9u80nnNjrtQi5vrN6-WiXWA9sZJqRWULS2bcZ63ys5jajr1RMznPSmI-2SjwyzaMYstGOg3a4PGTA8ScQ6QLXYXXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نشست شورای‌عالی قوه‌قضائیه امروز با حضور پزشکیان به‌عنوان مهمان مدعو برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451354" target="_blank">📅 11:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451353">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
جشن قهرمانی اسپانیا و شکست آرژانتین در ضاحیۀ بیروت  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/451353" target="_blank">📅 11:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4868e6348d.mp4?token=T_N23QWPyCH7FZV0cD7tNYvw6US0HlYwT6ESBIE1mK9pBUhDpKwrvOPZ6gsO-3VZfCgFdLd1uV0gmZydSSE8HS3cWmwi-9kg591-oQrFjSFEQcmMWn2rZZkCQ9vywnuuFaqwYYOFngwwdnKrF7xx49Mf3cv2se32NeAWSPAva96WKoA5QtnDWEtEMIfILS5tGctvtAOEA95j62-rHIA1Evh4H6iB-XrjTEvw5zST8nmdcxpHiHnUnQav1-CDMiHKnEQkrLvB_zT141EazIyIvydlK2upXmNkLJBwQafIHqwVI_oYHjcjHrliqBm3fdLoqN4NCvPfFRcdYdKRdxSNbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4868e6348d.mp4?token=T_N23QWPyCH7FZV0cD7tNYvw6US0HlYwT6ESBIE1mK9pBUhDpKwrvOPZ6gsO-3VZfCgFdLd1uV0gmZydSSE8HS3cWmwi-9kg591-oQrFjSFEQcmMWn2rZZkCQ9vywnuuFaqwYYOFngwwdnKrF7xx49Mf3cv2se32NeAWSPAva96WKoA5QtnDWEtEMIfILS5tGctvtAOEA95j62-rHIA1Evh4H6iB-XrjTEvw5zST8nmdcxpHiHnUnQav1-CDMiHKnEQkrLvB_zT141EazIyIvydlK2upXmNkLJBwQafIHqwVI_oYHjcjHrliqBm3fdLoqN4NCvPfFRcdYdKRdxSNbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای دروغ جدید ترامپ دربارۀ آزادی یک تبعهٔ زن ایرانی-آمریکایی
🔹
از ساعتی قبل، تصویری از یک تبعۀ ایرانی-آمریکایی به‌نام دنا کراری، هنگام ورود به یکی از فرودگاه‌های آمریکا، خبرساز شد. پیش‌ازاین، وکیل این زن نیز با توییتی در شبکۀ اجتماعی ایکس، ادعاهایی درباره…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451352" target="_blank">📅 11:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451351">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f878972977.mp4?token=bAxAO9oddRNjAYlVsC1Vxnf8_kgrhQC0I6y8Bd3n8GhzfhCtt0QfXwqnC470GRpSlS_AVryUlfl2iPAIr3LrTBCnJ0oQGQlBPXcfFjN58HrUs5SDTy9jJsCbKPL-TlZhcwvURi09dgq9sP6-zhFBmooyEigWWyA9iYFn6BV6Q3jcSzQ-AjCMvQnMIs23aCBimIbIY-8lhtCu9Ga_G0XAUQ-Cbk7tOYOlITtLT5LAu6diILVnuLXBBZQTZqyC1cwSBxywS6wuljpmFVhKEmR-_vfi9tILBKDvVm3pxExPdScKmENzqXSgPhOCNZTGVrKKuOwW-9Z4cXhwrdTFa3OWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f878972977.mp4?token=bAxAO9oddRNjAYlVsC1Vxnf8_kgrhQC0I6y8Bd3n8GhzfhCtt0QfXwqnC470GRpSlS_AVryUlfl2iPAIr3LrTBCnJ0oQGQlBPXcfFjN58HrUs5SDTy9jJsCbKPL-TlZhcwvURi09dgq9sP6-zhFBmooyEigWWyA9iYFn6BV6Q3jcSzQ-AjCMvQnMIs23aCBimIbIY-8lhtCu9Ga_G0XAUQ-Cbk7tOYOlITtLT5LAu6diILVnuLXBBZQTZqyC1cwSBxywS6wuljpmFVhKEmR-_vfi9tILBKDvVm3pxExPdScKmENzqXSgPhOCNZTGVrKKuOwW-9Z4cXhwrdTFa3OWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: فارغ از تفاهم‌نامه، نباید اجازه بدهیم که از تنگهٔ هرمز برای تهدید امنیت ایران سوءاستفاده شود.  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451351" target="_blank">📅 11:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2ee38c75.mp4?token=doGgD38a3zCWCgzqF3M9oiQP1MWXfI-bWnBYFe9iV-eX3HBlM4MPgp6bdVP6NBQZ2agGtUwU2ydcTCz6gFm0SXpiiF0F34seLvTHxXqXjFZvhWrTK-FKs1LzYZFMlBZQFjEIHMBJE-9bbgFGUBc9zABikjFuP5Cgn7X-jkYLa6lUbhSADvEpGSZtaCUqZwySNnrvuah7unymvHbMuJGXc_XTh37Y2qpp3_yQ0hVodAwIFXvNz2Pmg7mKdrwfhztzT_bK49mfHHvVflHHqyWsD98f80lvnR9v0Vvj8ZP7vNjcNe52Al9t4JduBa653aITgHuncAaqg-J0wq0rr7hp3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2ee38c75.mp4?token=doGgD38a3zCWCgzqF3M9oiQP1MWXfI-bWnBYFe9iV-eX3HBlM4MPgp6bdVP6NBQZ2agGtUwU2ydcTCz6gFm0SXpiiF0F34seLvTHxXqXjFZvhWrTK-FKs1LzYZFMlBZQFjEIHMBJE-9bbgFGUBc9zABikjFuP5Cgn7X-jkYLa6lUbhSADvEpGSZtaCUqZwySNnrvuah7unymvHbMuJGXc_XTh37Y2qpp3_yQ0hVodAwIFXvNz2Pmg7mKdrwfhztzT_bK49mfHHvVflHHqyWsD98f80lvnR9v0Vvj8ZP7vNjcNe52Al9t4JduBa653aITgHuncAaqg-J0wq0rr7hp3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: از نظر ما چیزی به‌عنوان «تحریم هوایی» در یمن وجود ندارد و اصل تحریم‌کردن یک ملت را ظالمانه می‌دانیم
🔹
هواپیمای ایرانی حامل هیئت یمنی حاضر در مراسم ادای احترام به رهبر شهید و جمعی از مجروحان یمنی بود که در ایران درمان شده بودند. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451350" target="_blank">📅 11:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451349">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2438504620.mp4?token=kZRrZJcKb17F3yU-fJSwWCEcxBTC2YdRmtBNgxWCLJWKkqZBzZxP_4KrKj5PmDKwSanYXs_a6WMSPHH93B5GqkzJEkiHkEW_SBbQIam_W-aZ-e1faZwDIczrvg2HbjB_UjbJcenjgqjo704nzTbKtbIfK1A4UUVvbPT5TzotDpeYsv64lKG8GYub9ntHESA3RlNtpanrkkI9WbybXwrSiWSJ_vbUusXZzT1rnab1kPszVpGxQJbSRxDmPXED7wKNDWziKLH7l7F5RxMi9R1nijeZnLmbbN0j0kBPKlv1U6M0gMmtuCQD5suMKO7NYFCk1jfX0XqfJGDz6keFmWAWCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2438504620.mp4?token=kZRrZJcKb17F3yU-fJSwWCEcxBTC2YdRmtBNgxWCLJWKkqZBzZxP_4KrKj5PmDKwSanYXs_a6WMSPHH93B5GqkzJEkiHkEW_SBbQIam_W-aZ-e1faZwDIczrvg2HbjB_UjbJcenjgqjo704nzTbKtbIfK1A4UUVvbPT5TzotDpeYsv64lKG8GYub9ntHESA3RlNtpanrkkI9WbybXwrSiWSJ_vbUusXZzT1rnab1kPszVpGxQJbSRxDmPXED7wKNDWziKLH7l7F5RxMi9R1nijeZnLmbbN0j0kBPKlv1U6M0gMmtuCQD5suMKO7NYFCk1jfX0XqfJGDz6keFmWAWCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تا جایی که طرف مقابل تعهداتش را اجرا می‌کرد، ما هم اجرا می‌کردیم
🔹
ما هیچ‌وقت پیشگام در نقض‌عهد نبودیم؛ اما زمانی که آن‌ها تعهداتشان را نقض کردند، ما هم اعلام کردیم که تعهداتمان را اجرا نمی‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451349" target="_blank">📅 11:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451348">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جاسک
🔹
سپاه هرمزگان: عملیات انهدام کنترل‌شده مهمات عمل‌نکرده امروز از ساعت ۱۲ تا ۱۶ در محدودهٔ بندر جاسک انجام می‌شود و به‌همین‌دلیل احتمال شنیدن صدای انفجار در این محدوده وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451348" target="_blank">📅 11:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451347">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbf440b549.mp4?token=BE4m3-rAVGNYjmj0ygzMJFPUHD7UYmV4lAezQ3B9X5yFM_d8ZoZ4cZHS-zyLaNZqSnSK5r070xRVQWRiL1zdQ5eNYykPznHgD2hwcDD1SZK4NEId2tJDoDrIaIeLvSKUl2bvdCtWmcLBDC2vDOzJrsNFsdzBBym4q9mtVSlnAOm4rXEmNfTrdQcKPi6QNiEeIXZXAgQqavUGVazT5_lXyOytGa5MqN_HAHw_aCdeKu7b7FautON35hGeUvw1W3CvkSJg6fLwvfzu_CaXCqFDDASsMlKkkWm02R4h5mqqkm6IgM95sZYr2MT6bEazkwuyLZmU26HAWXepVbXtKMa8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbf440b549.mp4?token=BE4m3-rAVGNYjmj0ygzMJFPUHD7UYmV4lAezQ3B9X5yFM_d8ZoZ4cZHS-zyLaNZqSnSK5r070xRVQWRiL1zdQ5eNYykPznHgD2hwcDD1SZK4NEId2tJDoDrIaIeLvSKUl2bvdCtWmcLBDC2vDOzJrsNFsdzBBym4q9mtVSlnAOm4rXEmNfTrdQcKPi6QNiEeIXZXAgQqavUGVazT5_lXyOytGa5MqN_HAHw_aCdeKu7b7FautON35hGeUvw1W3CvkSJg6fLwvfzu_CaXCqFDDASsMlKkkWm02R4h5mqqkm6IgM95sZYr2MT6bEazkwuyLZmU26HAWXepVbXtKMa8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: منظور آمریکا از دیپلماسی، تحمیل، ارعاب، تهدید و تحریم است و تا وقتی که در این فضا باشند، پاسخ ما دفاع از کرامت و حاکمیت ملی ایران است.  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451347" target="_blank">📅 11:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451346">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d272ea39a.mp4?token=T1DY_VZs3iJalzP6wRxPky9IC_bJvoXJxtLZ_AXcHOdOY4oPAL7d1Pd8OpVyK_81Ac7Me7bOyUfr5ecZHyT1v39zJH4mBySLMNBAGgHx6bhlTIqvEOu_N2RYQs4d6LPn9D3LNMhGDCBvEXKIuzotsdjNYPr05do5GISErPQGq9lUZRi970OnuW-_LTaDXTIPWSQbOURVsTmIjKrYlqf0jmDZhY0qFWieF0FpFjiDZZWJ1kxyQRVbEePyPguIG1lXQkrD58JXfzXOj13Dn7Nw5FSpysuAznZWa0gdh4cgltgkms4C0p3lI3CUQjJjB4wGxl5AmbqGSG4FSfZTFio4Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d272ea39a.mp4?token=T1DY_VZs3iJalzP6wRxPky9IC_bJvoXJxtLZ_AXcHOdOY4oPAL7d1Pd8OpVyK_81Ac7Me7bOyUfr5ecZHyT1v39zJH4mBySLMNBAGgHx6bhlTIqvEOu_N2RYQs4d6LPn9D3LNMhGDCBvEXKIuzotsdjNYPr05do5GISErPQGq9lUZRi970OnuW-_LTaDXTIPWSQbOURVsTmIjKrYlqf0jmDZhY0qFWieF0FpFjiDZZWJ1kxyQRVbEePyPguIG1lXQkrD58JXfzXOj13Dn7Nw5FSpysuAznZWa0gdh4cgltgkms4C0p3lI3CUQjJjB4wGxl5AmbqGSG4FSfZTFio4Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: صلح را در طاقچهٔ روابط بین‌الملل تقدیم نمی‌کنند؛ برای صلح، باید جنگید!
🔹
ما بزرگترین انسان‌هایمان را برای برقراری صلح پایدار برای تک‌تک مردم ایران تقدیم کرده‌ایم؛ باید از تصورات فانتزی دست برداریم.
🔹
آمریکایی‌ها خرداد پارسال گفتند «برای…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451346" target="_blank">📅 11:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451345">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331f15255a.mp4?token=WqKjAfLH3IBC9EPnumaU6rLBt9CEd0WyrdvU2Pu1skXy0DAr2T6SIU5bEqOuIvkk4qgREkLMBJ-ONvG6bcf1_Oxkdo9tqV7F7pKhPDSxsgMHAuySSsQ57malJl69He1irn4aALP1YV2TijhXWhqjP3ydQAwjsjONgwF901O7M5764XrDBxS5suHU8nSdzuezXUoFfpNPTlwUefqz2AE5JpjBuwElLKBgbseyE_9wY5Sun5Rpzy7kfZvd2Oy2Mty8WDYdsCjcdPTu2nOruCdSxA4VH_zM-vBjxqQy4rCfO6batonA2ci_T0WKQ_Y_9u1WByGg3jDtGiUXOPR02KGjXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331f15255a.mp4?token=WqKjAfLH3IBC9EPnumaU6rLBt9CEd0WyrdvU2Pu1skXy0DAr2T6SIU5bEqOuIvkk4qgREkLMBJ-ONvG6bcf1_Oxkdo9tqV7F7pKhPDSxsgMHAuySSsQ57malJl69He1irn4aALP1YV2TijhXWhqjP3ydQAwjsjONgwF901O7M5764XrDBxS5suHU8nSdzuezXUoFfpNPTlwUefqz2AE5JpjBuwElLKBgbseyE_9wY5Sun5Rpzy7kfZvd2Oy2Mty8WDYdsCjcdPTu2nOruCdSxA4VH_zM-vBjxqQy4rCfO6batonA2ci_T0WKQ_Y_9u1WByGg3jDtGiUXOPR02KGjXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: همزمان با درهم‌کوبیدن منشأ تجاوزات آمریکا توسط نیروهای مسلح ایران، از هیچ تلاشی در دیپلماسی برای توقف جنایات آمریکا فروگذار نمی‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451345" target="_blank">📅 11:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451344">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e384a7c28a.mp4?token=HwLrUlT074tuXpyRTzOey-p366q4cjNfRSNHj0gERX8QQPH3OvSMHl1RmL_SDdZ73a8-R4W3fzyyfoKj15EMncCXoYutfu2hmDqOLu0mrYAwBapoRZ0TMfm-93EmsvIaueVGlDU9XRM6NxJ7WcuBp1FeAvcDMcR0UdSoP_n5BSpsU-xpjfmFQtctXKr2b5qNUxRAtFEjt86sF2gOC0ps3Jwr3VU6qFY2-54Qq8--Y_n_blYtmSLW1GBAFP7V4yytPn95q_f7XunfQnbhlwCRXGPtL0i17ZYbohOsJM0wqs50Dc_VjTcdbOpW8dx4wgBNQzHsZHd3gnOwi7kAP7oHyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e384a7c28a.mp4?token=HwLrUlT074tuXpyRTzOey-p366q4cjNfRSNHj0gERX8QQPH3OvSMHl1RmL_SDdZ73a8-R4W3fzyyfoKj15EMncCXoYutfu2hmDqOLu0mrYAwBapoRZ0TMfm-93EmsvIaueVGlDU9XRM6NxJ7WcuBp1FeAvcDMcR0UdSoP_n5BSpsU-xpjfmFQtctXKr2b5qNUxRAtFEjt86sF2gOC0ps3Jwr3VU6qFY2-54Qq8--Y_n_blYtmSLW1GBAFP7V4yytPn95q_f7XunfQnbhlwCRXGPtL0i17ZYbohOsJM0wqs50Dc_VjTcdbOpW8dx4wgBNQzHsZHd3gnOwi7kAP7oHyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مقامات آمریکایی این‌قدر در معرض گزارش‌های ساختگی هستند که هر خبری دوست ندارند را هوش مصنوعی می‌دانند
🔹
آمریکایی‌ها خودشان هم می‌دانند که جنایت میناب کاملاً عامدانه انجام شده است. مقامات آمریکایی با برجسته‌کردن موضوع میناب می‌خواهند نشان…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451344" target="_blank">📅 11:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451343">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9uH5IoH-nM8Mn-p8H7n5IZU1PwBDtsmRGyTYxxdL66S3EUQfVsBdQEctZGcG-4pfosISY_Xec9Iu4DwQAl1lmwt9XGj2hQEzba4NX6RAaPZaKThk01vVLbe6KMRB_1kkDrJcnLu2xXzQeRSbEhtmAJc6l-UQFYdSqwwSJOHqZEyU3w4F0atpELgfwF1cyr6YYbMHQUntdWDXF-YB37Wi0l4FP52EKMm90kEDduaHttdO7iM5E2eQfdLc7YgUZShxAm1brVNy3BssBNAT-V7pfRrh0iMdQWDMRRBKopRHsdHf5COhZgBV8ac90U_VApwrWJT1sQL1mpvuc7Zje_AGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندازۀ تخم‌مرغ‌ها هم آب رفت
🔹
قیمت تخم‌مرغ در بازار تهران به شانه‌ای ۴۸۰ هزار رسیده که نسبت به دو هفتۀ گذشته حدود ۸۰ هزار در هر شانه افزایش داشته.
🔹
در یک فروشگاه بزرگ منطقه ۱۹، یک خانم میانسال در حال خرید تخم‌مرغ می‌گوید: هفتۀ پیش شانه‌ای ۴۲۰ هزار تومان خریده بودم. شانه‌ها با وزن ۲ کیلو قیمت‌گذاری می‌شوند، درحالی که این‌ها آن‌قدر ریزند که معلوم است وزن کمتری دارند.
🔹
پیش از این، تولیدکنندگان کمبود و گرانی خوراک را عامل افزایش هزینه و گرانی تخم‌مرغ می‌گفتند. این درحالی است که مدتی است وزارت کشاورزی از افزایش واردات و ترخیص خبر می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451343" target="_blank">📅 11:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451342">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597a7bb75c.mp4?token=Qs2BI7gkiezjz_EqfxhHcJBDeV6aoVJcb_m3c0-KC214WHMe57p0RjtLu5yML_uNZPCFEcrHyfKjCK0Pi-rdWiGu8UrzB2nv-Kig2GopNpQ0LiowfZpDiqxkJ8YblsjqOuGZ_OTLMA_D6ALP4LILMYrgnjHrkzsSiGnIuZWUgE4NKmj6ELVJKG-zcb4TQbz4TNRpF_uxEvUVr6p6iEVRgK8nWWvl_4vRr3x2dmK9lLiSQna8r8Vmhx_3_BlzeHskUuMEwk0kFC4Gom7nNm9qaG6FdBA_Qz3MNDrgtTUh8CCWpl5ZhpgQQhpI4WWLdpEIj9CioXBiMTlfHsUyKxzLkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597a7bb75c.mp4?token=Qs2BI7gkiezjz_EqfxhHcJBDeV6aoVJcb_m3c0-KC214WHMe57p0RjtLu5yML_uNZPCFEcrHyfKjCK0Pi-rdWiGu8UrzB2nv-Kig2GopNpQ0LiowfZpDiqxkJ8YblsjqOuGZ_OTLMA_D6ALP4LILMYrgnjHrkzsSiGnIuZWUgE4NKmj6ELVJKG-zcb4TQbz4TNRpF_uxEvUVr6p6iEVRgK8nWWvl_4vRr3x2dmK9lLiSQna8r8Vmhx_3_BlzeHskUuMEwk0kFC4Gom7nNm9qaG6FdBA_Qz3MNDrgtTUh8CCWpl5ZhpgQQhpI4WWLdpEIj9CioXBiMTlfHsUyKxzLkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: متن تفاهم‌نامه روشن است و تفسیرپذیر نیست؛ آمریکا جایی نگفته که «به‌دلیل اختلاف در تفسیر» به ایران حمله کرده  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451342" target="_blank">📅 11:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451341">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYuHkz10sDYKfWS9lmEQpwNKR3-8PVRAmyu00j66Kq8L95fBA7lpV4h3005W1uXpvzBQuBZMPlIwbxb1auos3WvBHVqmmBmKW7RruqXsdwz1GrqufiNto1p452iAqcFNBkzgt3ZIwipnEYj-SIC6pqt3fX2nemcpHKbsT9xj4xlRlyvAhkD2dxdLgt6ZcXX4kYY6m4KkdHFUiKMgIksryR5VItcaEyHRudsMMRiL-2al6Q8zZaQo4AMnQzFXcVR3fcWilpCjWRs-vuAnDAi0VrdZaqcr8R-buruXEYp6JtwEVh7QF7CPAttV7vaTZXITt8j8HcMIcp4gao8RhD-bFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم بزرگداشت شهید زهرا حدادعادل از طرف خانوادهٔ ایشان
◾️
پنجشنبه ۱ مرداد، ساعت ۱۷ الی ۱۹
◾️
میدان فلسطین، مسجد امام صادق علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451341" target="_blank">📅 10:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451340">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ea164fb5.mp4?token=AmVQ-EPKAoRzA3FAHc1IcFWxpEHEMvpIRPvO2of4ZhGQU9LkVQas02qWQjHkZAvo58TFEzQoZs8tIH4EiADdjoCMwTCesw31M4lVHN7k_4iOc76PkHvf4cNP3f2mxBJmKBMUdS2O2ouAi0pTp_6h_Im88uCF4r-6h4tNFmRGrHJk3_2oVd6nqLSt_TiaYWO6Uzqeij4OcJLw2FcTlNT02bnnph0w8MkyVXux5VPa-Ncgn_cswUpra5RB41rfYxfuDfG2G8jdICiaw1gZUzAJzGFJBDhvRvlDqqmrLwOOoEMPh0g6jD_GhNlF7AxT2wO7DyXU5K6vNgmIjDEZ3fAEuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ea164fb5.mp4?token=AmVQ-EPKAoRzA3FAHc1IcFWxpEHEMvpIRPvO2of4ZhGQU9LkVQas02qWQjHkZAvo58TFEzQoZs8tIH4EiADdjoCMwTCesw31M4lVHN7k_4iOc76PkHvf4cNP3f2mxBJmKBMUdS2O2ouAi0pTp_6h_Im88uCF4r-6h4tNFmRGrHJk3_2oVd6nqLSt_TiaYWO6Uzqeij4OcJLw2FcTlNT02bnnph0w8MkyVXux5VPa-Ncgn_cswUpra5RB41rfYxfuDfG2G8jdICiaw1gZUzAJzGFJBDhvRvlDqqmrLwOOoEMPh0g6jD_GhNlF7AxT2wO7DyXU5K6vNgmIjDEZ3fAEuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: متن تفاهم‌نامه روشن است و تفسیرپذیر نیست؛ آمریکا جایی نگفته که «به‌دلیل اختلاف در تفسیر» به ایران حمله کرده
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451340" target="_blank">📅 10:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451339">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Snw1na8As3LAb0PRLICbiCDQK1EK-5mVGRcXQL3HFMnCoxn9K0lJjwHsEsSaDFSsBOqskZEkvOa8hilI1cHQGLTY8DxEm6XYVCCX02-Gt5qi139Rm_-QXxki52Jdzby-fIyxc9DbLS-nMVyEpq6UP6i3hQLRjunnFA0i0XZ1uiY26SAJ0EOKYptorf_BGizfZ9pDRVROY4sGBYjIFP_FhCh5gGeXluG3yXBJ3RiWvXMlz5hp5wEdo8oRyo3Sh9YumJF1-DzoHgHqhUruc1dlap5je007NWUUHBok9g9Y9blvanm_q0GKW7MOTIutd6IV9NdqI6MLSKoFDZrYwpcRuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسب ۴ مدال توسط دانش‌آموزان ایرانی در المپیاد جهانی اقتصاد
🔹
تیم ملی اقتصاد ایران در نهمین دورهٔ المپیاد جهانی اقتصاد موفق به کسب یک مدال نقره و ۳ مدال برنز و کسب عنوان بهترین نمرهٔ مالی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451339" target="_blank">📅 10:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451338">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785f2fdeb8.mp4?token=UP9fNWXGxxoQjSbc8FAnpDGtYjPovlKopu0VODV6ytMzsX1dg0yNjAfaOhPtkv1x-fz2I0dznVBgwDlQo-5vyTtNSZYEIAaIjAh7NlmMus6YVjL9P4PJaLGUSRG2YzLzYa-uwyIzdvj1ziIF4ts42ZwXkyuErX0eOiDnxrJy1pI118GDG8D-YxDWytpp-TPnDaAdKqkdNcRaAQ2xfDOqSoeLz6E6xdYJkyLUcGmjlYjmNM9rYtEdujVMCLY36rI82Z4DhGBLdLhwsFWy63OrkFswv3PU-lG2IAHwdw61MJ3ThMNk364e0bYIlRZs9-BtLZbRQxyrLw3x9tBxI0AhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785f2fdeb8.mp4?token=UP9fNWXGxxoQjSbc8FAnpDGtYjPovlKopu0VODV6ytMzsX1dg0yNjAfaOhPtkv1x-fz2I0dznVBgwDlQo-5vyTtNSZYEIAaIjAh7NlmMus6YVjL9P4PJaLGUSRG2YzLzYa-uwyIzdvj1ziIF4ts42ZwXkyuErX0eOiDnxrJy1pI118GDG8D-YxDWytpp-TPnDaAdKqkdNcRaAQ2xfDOqSoeLz6E6xdYJkyLUcGmjlYjmNM9rYtEdujVMCLY36rI82Z4DhGBLdLhwsFWy63OrkFswv3PU-lG2IAHwdw61MJ3ThMNk364e0bYIlRZs9-BtLZbRQxyrLw3x9tBxI0AhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوشحالی اسپانیایی‌ها بعد از سوت پایان بازی  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451338" target="_blank">📅 10:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451337">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
🔹
استانداری اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در جنوب و غرب اصفهان، بهارستان و صفه و ابریشم تا بعدازظهر امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451337" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451336">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a52bc34670.mp4?token=VL5LOhRwIRvH6Qwy4F4u85Fge83ajMcJTw8NYnrup7JgzQtPoGzL9hgekeos6xKF-Ku8ydIXGkdyog49u4oAly8deBaVj_g5W091wS7kOO1SpVNJzUh83jqj-3308IIJXI2VxtTrJ9lP22biUk4Xrbqy4YvL9xfaq69hYAH9vk0FeaCIgrqrn_cW_ErNhKkibeMvgW1IHoeeTHGoKOOjuvP_XZlL8fTN1TAvSK9GPfLVkW0X0hP5zAp9PM8cr8m5zkVj6kqJVoS2WRNBHhK6lhm_GXAdz7VG2vqn0V3t_oNy2td5B-2pAGq6Q5voInMVagKM8mVVEGQ8HtNhpNpxkHCrTl86niYznLRwEbnYf-BtKdlzeIZfMws1LCXjWXhPLEvOO3Ac4oxI04LY3OSQT-MEkWz1tCua9vjs1JsHZ4E0kJwP_7FcOiYdEUuLz3lfY_J-Zbcr0w8vW4YnszrqHrJq7OjUnpis5N9emzzhIqt9JUWnrMZ5TFPeJCBebRAuIF-OYE8D7I7FyUs8MrE4uTX7XU3ib0kGAwiHWZckgHXUtZgNjNvJSK7_wKCIeqfVUyJXH-XujC2r__XVehJdhz6D72hu7Q9bN0oCSOuAPFr1Zh3qpOmELDM1A39DJ65PAMjifhZz7xyA23SPsZicSbrFk9AX9-xP8KhUPwlClFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a52bc34670.mp4?token=VL5LOhRwIRvH6Qwy4F4u85Fge83ajMcJTw8NYnrup7JgzQtPoGzL9hgekeos6xKF-Ku8ydIXGkdyog49u4oAly8deBaVj_g5W091wS7kOO1SpVNJzUh83jqj-3308IIJXI2VxtTrJ9lP22biUk4Xrbqy4YvL9xfaq69hYAH9vk0FeaCIgrqrn_cW_ErNhKkibeMvgW1IHoeeTHGoKOOjuvP_XZlL8fTN1TAvSK9GPfLVkW0X0hP5zAp9PM8cr8m5zkVj6kqJVoS2WRNBHhK6lhm_GXAdz7VG2vqn0V3t_oNy2td5B-2pAGq6Q5voInMVagKM8mVVEGQ8HtNhpNpxkHCrTl86niYznLRwEbnYf-BtKdlzeIZfMws1LCXjWXhPLEvOO3Ac4oxI04LY3OSQT-MEkWz1tCua9vjs1JsHZ4E0kJwP_7FcOiYdEUuLz3lfY_J-Zbcr0w8vW4YnszrqHrJq7OjUnpis5N9emzzhIqt9JUWnrMZ5TFPeJCBebRAuIF-OYE8D7I7FyUs8MrE4uTX7XU3ib0kGAwiHWZckgHXUtZgNjNvJSK7_wKCIeqfVUyJXH-XujC2r__XVehJdhz6D72hu7Q9bN0oCSOuAPFr1Zh3qpOmELDM1A39DJ65PAMjifhZz7xyA23SPsZicSbrFk9AX9-xP8KhUPwlClFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشن‌گرافی| سودای تجزیه
🔹
روایتی مستند از طرح آمریکایی‌صهیونی برای تجزیۀ ایران و نقش خیانتکارانۀ گروهک‌های تروریستی تجزیه‌طلب.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451336" target="_blank">📅 10:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451335">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzNJUmAnTAXmjeQ7MDGv_seIQpApOiJzD46cEIWnv4bMrWLUbxg9ls20VBVghbkx003tL9oWHa4t0w-LbUeMlgy72QfffdshsqOLbk16T1EfX9Cx03M9ZDDIYgKQdQKPzlIJObwefL0ec4qKfJZJrP2JtzZ3AdqQtnWl3sfGoxzmMQ2bxdl--ipghwU5WNE0gKW_lDENFVmZkfdzluJTaryXVzxrrANSa94BKKhD97ffNzKM9JHp8noAnincX97O-mLDkFOkckFY2h2cuDVdkrLVnvKDEHhVmUnfstC2qbVlFJQ_YY_DgclFk6u0sHI0r_t-DvbDp4bq3y9BE1_WDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلا فوئنته: به شاگردانم افتخار می‌کنم
⚽️
سرمربی اسپانیا: به این نسل از فوتبالیست‌ها که با تکیه بر این فلسفه همواره در حال پیشرفت بوده‌اند و الگویی از یک گروه، یک تیم و یک خانواده را به نمایش گذاشته‌اند، بسیار افتخار می‌کنم.
⚽️
این تیم شایسته قهرمانی بود. از ابتدا تا انتهای مسابقات شخصیت، کیفیت و جاه‌طلبی خود را نشان داد.
⚽️
فران تورس همیشه آماده بود. وقتی وارد زمین شد، همان تأثیری را گذاشت که از او انتظار داشتیم و گل قهرمانی را به ثمر رساند.
⚽️
آرژانتین تیم بزرگی است و مسی یکی از بهترین بازیکنان تاریخ فوتبال است. قهرمانی مقابل چنین حریفی ارزش این موفقیت را بیشتر می‌کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451335" target="_blank">📅 10:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451334">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌
🔴
سپاه: دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند
🔹
اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک‌کش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگۀ هرمز را داشتند منفجر شده و از حرکت باز ماندند. …</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451334" target="_blank">📅 10:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451333">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فرماندار بوشهر: دقایقی پیش بوشهر ۲ بار هدف تهاجم دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/451333" target="_blank">📅 09:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451332">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ea928e59.mp4?token=S5r8RChGdcqZPIxmo0No-4IKHRpNiukZ_33ZTPAugTPL1X6jniUowsi4ew8GkeRwJN5YZuqLcnq_tS_RK_4-NWqlQjfC9mKMiPFaRlGMU56AzAsMZJzVJNwHhpjs5_OhUdLVxdKglWGuxa7m0pdgyG72n3QAPQP_GT-qrSJnefkP9gyN_v-wTjB5EpwPkCPr77TxnXL-xASIzO_2a6d6I_IDNpfNNTslI_Vt5-oSdxDmTwCAPyJ413NJ3O-TmM0QiRyOjJqOLLRlv_7oC6nuyoF-EvxAob7odWkrFTTqwF7I2hq5RLWAyZ9T6h3jJGbeeA32V7kJUrImLNSukZKPXIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ea928e59.mp4?token=S5r8RChGdcqZPIxmo0No-4IKHRpNiukZ_33ZTPAugTPL1X6jniUowsi4ew8GkeRwJN5YZuqLcnq_tS_RK_4-NWqlQjfC9mKMiPFaRlGMU56AzAsMZJzVJNwHhpjs5_OhUdLVxdKglWGuxa7m0pdgyG72n3QAPQP_GT-qrSJnefkP9gyN_v-wTjB5EpwPkCPr77TxnXL-xASIzO_2a6d6I_IDNpfNNTslI_Vt5-oSdxDmTwCAPyJ413NJ3O-TmM0QiRyOjJqOLLRlv_7oC6nuyoF-EvxAob7odWkrFTTqwF7I2hq5RLWAyZ9T6h3jJGbeeA32V7kJUrImLNSukZKPXIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ لرزش‌ زمین‌لرزۀ کرمانشاه در ۵ استان احساس شد
🔹
لرزش ناشی از دو زمین‌لرزۀ بالای ۵ ریشتر کرمانشاه، در استان‌های ایلام، مرکزی، همدان، کردستان و لرستان نیز احساس شده است.
🔹
سازمان مدیریت بحران تأکید کرد که این زمین‌لرزه‌ها صرفاً پدیده‌ای طبیعی ناشی از فعالیت‌های…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/451332" target="_blank">📅 09:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451331">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌
🔴
رسانه‌ها از اصابت مستقیم موشک به منامهٔ بحرین و بلندشدن ستون‌های دود خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451331" target="_blank">📅 09:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451330">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glpZCzalW-yrx4XrARvrdrOhpGjRfqd3cSABgiZ3zwSc_N9QdGMGUFM567ibI3zviIN6U3XaIVaMd75XHKEwxGZrWHrnlJQm5q-Ink5ancJ4ZNjB66IF0R6VX_Fkw0eoHmkKEhPYNaNixTVTSrGP0VNGNIiRlmWp-GflljVCLiP8nzzl3E3xrn7t3GO2xsg7S-87dyJ9x_l88lusZdLUOWLp0-s9PFPZ5JSISCYrkdnPAfCUA-OvEAeZrrBYaq0EkO-zeYAJzV4IbuUvbOvSCR-du8FZuuRLCzCBcsE0T1QaZFBFydvdniGNqqdkuKbEqYitWuiM4M6jJZUg274Vlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌فروش بلیت قطار اربعین از فردا
🔹
رجا: فروش بلیت قطارهای مسافری برای ‍۱ تا ۱۶ مرداد، فردا از ۸:۳۰ تا ۱۱ صبح به‌صورت اینترنتی و از ۱۱ تا ۱۳:۳۰ از طریق آژانس‌ها انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/451330" target="_blank">📅 09:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451329">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌ جزئیات حملهٔ ساعاتی پیش دشمن آمریکایی به اطراف تبریز
🔹
بامداد امروز یک منطقهٔ نظامی در جنوب‌غرب تبریز هدف حملهٔ ارتش تروریستی آمریکا قرار گرفت. صدای انفجارهای این حمله در بخش‌هایی از تبریز هم شنیده شد.
🔹
مدیرکل مدیریت بحران استانداری آذربایجان‌شرقی: این…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451329" target="_blank">📅 09:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451328">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین از فعال‌شدن مجدد هشدارهای حملهٔ هوایی خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/451328" target="_blank">📅 09:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451327">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امام‌جمعهٔ اهل‌سنت میرجاوهٔ سیستان‌وبلوچستان به شهادت رسید
🔹
سحرگاه امروز «محمد انور ریگی» امام‌جمعهٔ مسجد علی‌بن ابی‌طالب(ع) شهر میرجاوه در استان سیستان‌وبلوچستان توسط افراد ناشناس هدف سوءقصد قرار گرفت و به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/451327" target="_blank">📅 09:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451326">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
همزمان با کویت، منابع عربی از وقوع چندین انفجار در شهر منامه پایتخت بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/451326" target="_blank">📅 09:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451325">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5a63e91.mp4?token=BKvOgcMBKl2CF14E7vCgYbWJTuaXpOsRjJFkSSAl5bHD7DrGa-uvgX0xKMVXxWln1fRjddRN568dSnlRJCt5KUmpUGT5LWGoIXg4N-iiPXRqnIjUkbR8AChi_3SHfo98mqQer7Xx4pKN_nruv-W-t5eY91TTv-U-X9Kd8O6EwM8egdxqtVq6QlT5kqoN3BblXMlxV5Zt0gCMurBJhYZKXMNm2ftHx50NAg24byC09mI7jzZqTm-ZDclloTtrVks_ci2_pKwtyVssXNPLr_yNlhrF-_n-7yIneRcd8vRarboRsepiFBTkEuEec6NEznSRBqXtOV_ONGSnOVRJ6idgvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5a63e91.mp4?token=BKvOgcMBKl2CF14E7vCgYbWJTuaXpOsRjJFkSSAl5bHD7DrGa-uvgX0xKMVXxWln1fRjddRN568dSnlRJCt5KUmpUGT5LWGoIXg4N-iiPXRqnIjUkbR8AChi_3SHfo98mqQer7Xx4pKN_nruv-W-t5eY91TTv-U-X9Kd8O6EwM8egdxqtVq6QlT5kqoN3BblXMlxV5Zt0gCMurBJhYZKXMNm2ftHx50NAg24byC09mI7jzZqTm-ZDclloTtrVks_ci2_pKwtyVssXNPLr_yNlhrF-_n-7yIneRcd8vRarboRsepiFBTkEuEec6NEznSRBqXtOV_ONGSnOVRJ6idgvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریای خزر تا فردا مواج و تعطیل است
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریای‌خزر، تمامی فعالیت‌های تفریحی، صیادی و کشتیرانی را از صبح امروز دوشنبه، تا بعدازظهر فردا سه‌شنبه ۳۰ تیرماه ممنوع اعلام کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/451325" target="_blank">📅 08:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451324">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4665c76a3.mp4?token=SPClbd9CpYFr9azQM4PhTmauEEga35cpYa4ShSzpZ9AHdq-Z6sJxtJEF_K--bAVcbNb2QsVD_AV1KtrYJqX56jQ4TyFxbPE7-qBvD7gMOoJSWNo2zDbiTSjCGKUL-ssoxK-pi2Ey4TXl5uxYF0vj6_qAU8qcAVHcKEE_-AuFK9PAPbMNd8MA7r7yPIUSLOhx5vOOX_Z2oHK4LfaK_C2zD50Mpr1WrBe0FnuCMGp3hdtmWiZtWPqPAtXEtI8oFkG_wuHzxriocu3PgN9R0N9uAQk6hudUfJxmp5V4c1dG0qFgYOnWupPmmMmKWKagOrGKBA4R5rFOw0UdiObtbhA9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4665c76a3.mp4?token=SPClbd9CpYFr9azQM4PhTmauEEga35cpYa4ShSzpZ9AHdq-Z6sJxtJEF_K--bAVcbNb2QsVD_AV1KtrYJqX56jQ4TyFxbPE7-qBvD7gMOoJSWNo2zDbiTSjCGKUL-ssoxK-pi2Ey4TXl5uxYF0vj6_qAU8qcAVHcKEE_-AuFK9PAPbMNd8MA7r7yPIUSLOhx5vOOX_Z2oHK4LfaK_C2zD50Mpr1WrBe0FnuCMGp3hdtmWiZtWPqPAtXEtI8oFkG_wuHzxriocu3PgN9R0N9uAQk6hudUfJxmp5V4c1dG0qFgYOnWupPmmMmKWKagOrGKBA4R5rFOw0UdiObtbhA9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ لرزش‌ زمین‌لرزۀ کرمانشاه در ۵ استان احساس شد
🔹
لرزش ناشی از دو زمین‌لرزۀ بالای ۵ ریشتر کرمانشاه، در استان‌های ایلام، مرکزی، همدان، کردستان و لرستان نیز احساس شده است.
🔹
سازمان مدیریت بحران تأکید کرد که این زمین‌لرزه‌ها صرفاً پدیده‌ای طبیعی ناشی از فعالیت‌های…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451324" target="_blank">📅 08:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451323">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
گزارش زندۀ صداوسیما از تبریز: صدای ۳ انفجار از غرب تبریز شنیده شد.
🔹
این اولین حمله به تبریز در دور جدید حملات دشمن آمریکایی به کشورمان است.  @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/451323" target="_blank">📅 08:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451322">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">معاون امنیتی استانداری خوزستان: بامداد امروز آمریکا به یک نقطه در اطراف شهر بندر امام‌خمینی (ره) حمله کرد.
🔹
این حمله تا این لحظه خسارت جانی در پی نداشته و اخبار تکمیلی اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/451322" target="_blank">📅 08:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451321">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
همزمان با کویت، منابع عربی از وقوع چندین انفجار در شهر منامه پایتخت بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/451321" target="_blank">📅 08:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451320">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
انفجارهای دوباره در کویت
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در کویت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/451320" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451319">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌ کوزران کرمانشاه دوباره لرزید
🔹
به فاصلۀ ۵ دقیقه از زمین‌لرزۀ اول، پس‌لرزۀ دیگری به بزرگی ۵.۷ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند. @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/451319" target="_blank">📅 08:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451318">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سیریک و خورموج
🔹
در ادامۀ حملات دشمن آمریکایی، دقایقی پیش مردم استان هرمزگان از حوالی سیریک صدای چند انفجار شنیدند.
🔹
در استان بوشهر نیز صدای ۲ انفجار از حوالی خورموج شنیده شده است.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/451318" target="_blank">📅 07:45 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
