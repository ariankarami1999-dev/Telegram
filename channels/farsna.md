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
<img src="https://cdn4.telesco.pe/file/S-2EFMzQGVX19sRpBdCmUZrykN_iwFmGpwyhL-A3p-CNqGhunzpvjCOVge9HY0uXpklIxHl03puvd3_XPCKFtgas8vsJMU6rYwN73KY-zEtYYLqw1_rWdlYoajYNyf1OL_HATq0Uo4H9Batpb7YoB6assDn3TcHcwdSI3xI1vzHr5b30QVbS2SaRZe1g1RV4j6ygJqSjQYXSzeiIgOf_oxwPGQfkuLKJzBeFh70mWZiuq__ptvUSNP3CjEghodgqSE0gDVrD2UgLknMdqS4y-2FJGGzqmyqkVg-GbG8W7XhoTmb38k73zpqvj-hehO5uqbJyyJQYm5Fe7tE5X-dZMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-465102">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌  حمایت سران حکومت عراق از بازگشایی فرودگاه نجف به‌روی پروازهای ایران
🔹
سران قوای عراق شامل ریاست‌جمهوری، نخست‌وزیری و سران دو مجلس از خواستۀ دولت این کشور برای معافیت فرودگاه نجف از توقف پروازهای ایرانی حمایت می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/farsna/465102" target="_blank">📅 21:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465101">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR21TA2HutZzVJHksCTZoGtJNFLyiaAaNen717GHnbc_yIUwW9Id2RrncIbpE0Y9uT1ankyueSfIwSLSZwz-uvSaOdkhMwle35DKgipzm8jjhcQXSXmbGs-bJx8f-u45H1Q8kX45eHw0xVh1WvWAQSSTyBxfHcedBMF_nqS7v4uVIPQWNypqPB1LqoSkSWE64sAAb89mLQfAA6JIa2SVzjIWiR3Ulc-3xw9lMuewBRqqDWiBY_2jBdOj2JVKIN6a4SC3ENLtK9OmdtOB9NklbMyvqICPvTaEMqqTFmsxbjgVG1Luyog9_EXSurJGhyV6isSyasnzN1j4Q2gIfJacQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر، عشق، پسر
🔹
نامۀ‌ای که رهبر شهید برای فرزندشان آیت‌الله سیدمصطفی خامنه‌ای  در هنگام حضور وی در جبهه‌های دفاع مقدس نوشتند:
بسمه‌تعالی
مصطفای عزیز
امید است سالم و شاد و در آن محیط صفا و خلوص، غرق ذکر و توجه و سرگرم خودسازی باشی.
البته لطف خدا شامل حال تو است مثل همیشه، و انشاء‌الله بیشترین استفاده را خواهی برد.
نامۀ تو را بعد از برگشتن از مشهد دیدم، ظاهراً تاریخ ۲۷ تیر را داشت.
اقامت من در مشهد هفت روز بود، نیمی به کار فشرده و نیمی به استراحت گذشت. جای تو در هر دو قسمت خالی بود، بچه‌ها را با خود به نیشابور و سبزوار بردم تا آیات و برکات الهی را در اجتماعات بزرگ و پرشور مردم ببینند و عظمت مردم را که رشحه‌ئی از قدرت خدا است درک کنند.
درباره‌ی خطّ و ربط سیاسی مواظب باش در دام بحث و مجادله نیفتی که نه دنیا دارد نه آخرت. گاه کلمه‌ئی ارشادی بی هر تعریض و تصریحی علیه این و آن بد نیست، مشروط بر آنکه امید ثمری باشد و الّا فلا.
اطرافیان را به تقوا و ورع و عبادت و یاد دعوت کن البته با توجه به این درس که کونوا دعاة الناس بغیر السنتکم.
ترا به خدای عزیز حکیم می‌سپارم.
در مورد توصیه‌ی مطالعه و کتاب، قدری توضیح بیشتر بده تا انشاء‌الله بفهمم چه باید کرد. ۶۵/۵/۷
@Farsna</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/465101" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465100">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA7sJvZNoARU9B5jFo_OEqD_IvWw3mUJRc4xt4kHgRPmPZlQr-8zkVqhrszT4GsaSnlBwxYPgRaER1CCJwfGo0t-RcagmQ14VEGlfjGoY7_1xz91meeTI-0vxfvDZp4MFJuCajau39ARRnZ9F5p--ejnBrgcQbLBM5hojWRteZILAEx5ZcDYro7nsUGE0TbYUhrirn2mhdZGC6DwdbFsOGCuUj8fXy8xy-Q5EJ9jPIYEpJ_i0DGRZm89710ePNEH0J24pPnOYgRs96JZuZ0NkJVQ2f7MAWURAhIsWs_PzykEnQ4mwuGrpy9-SAggKkrhbYwyeNH3lPpgaGyEytdlUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۱۱ خبر امیدآفرین در حوزه‌های اقتصادی، فرهنگی، علم و فناوری و زیرساخت‌های کشور
@Farsna</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/farsna/465100" target="_blank">📅 21:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465099">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q24RxBAq5PRPaP_KmwHaPgKUvDjsjWfcg3GKtjDiIOnjHrvoAG5IyN8YfBpYiES53XINzf6Ghr5Q51rCF2zKZUlbQHiWnCgqXoCUZw8UR_pyKaxezHythcDnmgo3yJo9EkL0ZBr2U4mah2HgsQFxtsO2gsecFESQ79pDoQBgZGayNtqms_6xJfpIdrAXIOP5CflM4KJ-ibkh_hdmQ92g3ekYBl4q8V0EF9vwHZEvQhjjE7mHxYL4HvxEZZwFafvvTojn9tC6xkocsWf8kOc16AEqYgDn7iLoLxH0KQGcoIhVGyYkKxNbBRsaRb8Wyre3-izHgkIUMuOcMyEEnrnhXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کُند بودن پاتریوت‌های آمریکا برای مقابله با موشک‌های روسی
🔹
بر اساس گزارش منتشرشده در نیوزویک، صنایع دفاعی روسیه در ماه‌های اخیر تولید موشک‌های بالستیک و پهپادهای جت‌موتور را افزایش داده‌اند؛ تسلیحاتی که به دلیل سرعت بیشتر نسبت به پهپادهای قدیمی‌تر، فشار بیشتری بر شبکه پدافند هوایی اوکراین وارد می‌کنند.
🔹
طبق آمار مطرح‌شده در این گزارش، روسیه در هفت ماه نخست سال جاری ۵۸۷ موشک بالستیک شلیک کرده است؛ رقمی که از مجموع ۵۱۱ موشک بالستیک شلیک‌شده در کل سال ۲۰۲۵ بیشتر است.
🔹
در یکی از حملات اخیر، نیروهای روسیه در شب ۲۶ تا ۲۷ سپتامبر ۱۷۰ پهپاد به سوی اوکراین پرتاب کردند که ۷۶ فروند آنها جت‌موتور بودند. مؤسسه مطالعات جنگ نیز گزارش داده است که روسیه در حال استفاده گسترده‌تر از پهپادهای جت‌موتور برای حملات دوربرد است و این روند در ماه‌های اخیر شدت گرفته است.
🔹
ورود نسخه‌های جت‌موتور به زرادخانه روسیه، معادله دفاع هوایی اوکراین را پیچیده‌تر کرده است. رویترز نیز گزارش داده است که این پهپادها با پرواز در ارتفاع حدود چهار تا هفت کیلومتری و سرعت بالاتر، فشار قابل توجهی بر سامانه‌های دفاع هوایی اوکراین وارد کرده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/farsna/465099" target="_blank">📅 21:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465098">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd110347b8.mp4?token=A6y0CQhNHuoamqyNfi44YcUiP5ME_5RGkpfWIEWMYLisyfS3fnnptUyTMRQByQit30b-PMlD8MemUVh4dyt05cwZLo0hCB2jL2fOC9IaXszIPtufPyI-YIBKxSqcOl_Jd5sUwfOQRmNVKL3Xhs_-lpNoV127NAYdQ1ZaXQHtBRKKcZum7CjYvdWDOmap358Mw-NgUSB9spUT4NbWq9vMK9TFMgE1Y_mAmUnn0KmaUE8xrIoCNIThCSUEB4mo8kQQi0A0Y5pwm_FnOoidDhIE1ZMc2fQeRJ3NGcJUMPRO1S21ht4SVdrdDxz7TvafMnzVrSTRAd9t1HrKDOrnSKItBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd110347b8.mp4?token=A6y0CQhNHuoamqyNfi44YcUiP5ME_5RGkpfWIEWMYLisyfS3fnnptUyTMRQByQit30b-PMlD8MemUVh4dyt05cwZLo0hCB2jL2fOC9IaXszIPtufPyI-YIBKxSqcOl_Jd5sUwfOQRmNVKL3Xhs_-lpNoV127NAYdQ1ZaXQHtBRKKcZum7CjYvdWDOmap358Mw-NgUSB9spUT4NbWq9vMK9TFMgE1Y_mAmUnn0KmaUE8xrIoCNIThCSUEB4mo8kQQi0A0Y5pwm_FnOoidDhIE1ZMc2fQeRJ3NGcJUMPRO1S21ht4SVdrdDxz7TvafMnzVrSTRAd9t1HrKDOrnSKItBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعضای دولت روزی چند ساعت در فضای مجازی هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/farsna/465098" target="_blank">📅 20:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465097">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93afcd2ffa.mp4?token=Do_U25MxRpOgm9tMVd8dO5yp0NJdK3-oksNhV16J_9CZIW4YAqF9MIm6G9sunibAkckvwi-rHkjuorHG8MZ9rXlghiWIM39s8IjdOmAMAcWji47EbREiDvTihojLxLGqAluWlk1V_R39r5Chn9dH6UAHIygL4fclNw22o29AtaD60omRez7RCmjJnJqqNsqR51o3hIdFIPVe8Z64jeZQXBCYCzLjOvY3QpqxL3aONhwFp31kyvnZhhG0d9A_l5L8B6oyBtW6spq-v8oHdGbsEcJyMT3Gxk4Efu9A8R_dt3GSvbv77zUcNoxPf1urj-nNTbwW8_WyK9hIa9c1iIOUbl3y8fx7PkSWo3NPVC-X8zTtZTVtx-A3KR6PQgYyzndUNsd25UJhFilvR1EyqUk45jXAxzEZy1JJ7UOgNe29cJhNDMdxac7YmDUcA92I6ZkW4fnNx8nWKjOTt3XhoNGmlAoolbdJndVixGIUY0-7rkkk6u8lbdD8gauAivlunkKEWAYUZKjKBz_UYv7bogOv5qa7ZSwMRt0HJ-nVQ6yPqhMW7-XUTTJwksphf1s4VtEjrjfvFczxAHBOSneUTs46SQl-FuCA-pv7nza-_waF-RRMcAjCpoA7OsNrga7MxxGKHtwMQQF0SPtWwJniFsFNxlXFeknS0OVx2E0PQRPSc3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93afcd2ffa.mp4?token=Do_U25MxRpOgm9tMVd8dO5yp0NJdK3-oksNhV16J_9CZIW4YAqF9MIm6G9sunibAkckvwi-rHkjuorHG8MZ9rXlghiWIM39s8IjdOmAMAcWji47EbREiDvTihojLxLGqAluWlk1V_R39r5Chn9dH6UAHIygL4fclNw22o29AtaD60omRez7RCmjJnJqqNsqR51o3hIdFIPVe8Z64jeZQXBCYCzLjOvY3QpqxL3aONhwFp31kyvnZhhG0d9A_l5L8B6oyBtW6spq-v8oHdGbsEcJyMT3Gxk4Efu9A8R_dt3GSvbv77zUcNoxPf1urj-nNTbwW8_WyK9hIa9c1iIOUbl3y8fx7PkSWo3NPVC-X8zTtZTVtx-A3KR6PQgYyzndUNsd25UJhFilvR1EyqUk45jXAxzEZy1JJ7UOgNe29cJhNDMdxac7YmDUcA92I6ZkW4fnNx8nWKjOTt3XhoNGmlAoolbdJndVixGIUY0-7rkkk6u8lbdD8gauAivlunkKEWAYUZKjKBz_UYv7bogOv5qa7ZSwMRt0HJ-nVQ6yPqhMW7-XUTTJwksphf1s4VtEjrjfvFczxAHBOSneUTs46SQl-FuCA-pv7nza-_waF-RRMcAjCpoA7OsNrga7MxxGKHtwMQQF0SPtWwJniFsFNxlXFeknS0OVx2E0PQRPSc3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از خبری که افتخار مردم شد
@Farsna</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/465097" target="_blank">📅 20:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465096">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39deba18cb.mp4?token=Uw6Z5FQBadQlMZOh8yydrGio--zQfEW19NjecUcN3uKRqTbob9l3xQO_p6O-Ff8OMZH-la7IQrjjvxJKoaG03xiY8i4yRKQ6f_zTDjkds_gCwr4orh1cyEmFtoXPat28X0bL1vUZi5UY6f8wBDeOSpsWp3n7SfVUa-Xher5MEpgBiztrvH6jPuMKo4Myr_kK7dbQq7M2xCT0K1aCFy1qsOnhmMFZzBz-r5GkdYwBqVdvO1l1TerbEb0qDKXKQt82qV-wHweRmMhN218s99dFbyG0ZjvTEhXCyHBkNerilvA8roRcEsPZ0c8L7ukm57_3ZfkrOnRJ7sy98WsGBr4zKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39deba18cb.mp4?token=Uw6Z5FQBadQlMZOh8yydrGio--zQfEW19NjecUcN3uKRqTbob9l3xQO_p6O-Ff8OMZH-la7IQrjjvxJKoaG03xiY8i4yRKQ6f_zTDjkds_gCwr4orh1cyEmFtoXPat28X0bL1vUZi5UY6f8wBDeOSpsWp3n7SfVUa-Xher5MEpgBiztrvH6jPuMKo4Myr_kK7dbQq7M2xCT0K1aCFy1qsOnhmMFZzBz-r5GkdYwBqVdvO1l1TerbEb0qDKXKQt82qV-wHweRmMhN218s99dFbyG0ZjvTEhXCyHBkNerilvA8roRcEsPZ0c8L7ukm57_3ZfkrOnRJ7sy98WsGBr4zKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دائم دنبال عیب‌های خودت باش
🎙
امام خمینی(ره)
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/465096" target="_blank">📅 20:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465095">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f50f2464.mp4?token=dP9AxQZeWmU3368yW-3esPP_8t2FM43lUY3C3CY_aeQ0i2gdDn6wcwPCN1ZxMiZDLPXaXH3e0aX_DUpBBWD7SqkB7-KqBtiTc8JCH0zhxBBHKEM4pLWb1CGefvAFTkOgJbRWENqX6Tqv53R_G49Ip2Jn_YJ88N2C4QXMWapp3TgN5fKDoiOuUUPPRBvfddlD66RI8JBKi4wKZIXCetFgtYVA9-z5Ho_9JsMnlUG-ho8VAdAowzJNOnaX6Y-uzJWkAmOGQP25OyfTb4bkcNx39xpotCQhJprcj0A7lpIp3Kbt2FpbSGFO3JM5teFpA91WpuEvqMreclmU32kN8zdmpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f50f2464.mp4?token=dP9AxQZeWmU3368yW-3esPP_8t2FM43lUY3C3CY_aeQ0i2gdDn6wcwPCN1ZxMiZDLPXaXH3e0aX_DUpBBWD7SqkB7-KqBtiTc8JCH0zhxBBHKEM4pLWb1CGefvAFTkOgJbRWENqX6Tqv53R_G49Ip2Jn_YJ88N2C4QXMWapp3TgN5fKDoiOuUUPPRBvfddlD66RI8JBKi4wKZIXCetFgtYVA9-z5Ho_9JsMnlUG-ho8VAdAowzJNOnaX6Y-uzJWkAmOGQP25OyfTb4bkcNx39xpotCQhJprcj0A7lpIp3Kbt2FpbSGFO3JM5teFpA91WpuEvqMreclmU32kN8zdmpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان‌فدایان در «بهار» همدان به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/farsna/465095" target="_blank">📅 20:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465094">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba3591ff8.mp4?token=myp_dz1Jp4zTs8dXu6XO3zPREFoBTKEZROYAg4IYzcETF8OATOghmQ-Fl_kzw_091S7g1sbw-y4z-Ctc0OAN2VMn6OHD-hh8r6zCeLoBJ4oCyE34yaxI0gFBdJTpLlDhOzKj7_AUFqCxzNhO0OEf_fDZivOPQ8k0X-fqDZSrka214Z5e-IajzYftX4vXwSE481WqUze1BXsudFJ7I65XNv-VZrhtsqFhTnunAFqPAR0Kq4QhBSlBhkphpZ6_YG5mqrMdSMl6zXIM8LddzZ4PMj109PxvqRzgPtqIMf5PprbNRoEu4zcPHATJy50DigertSRwRLwOUY5swVCVfTJglQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba3591ff8.mp4?token=myp_dz1Jp4zTs8dXu6XO3zPREFoBTKEZROYAg4IYzcETF8OATOghmQ-Fl_kzw_091S7g1sbw-y4z-Ctc0OAN2VMn6OHD-hh8r6zCeLoBJ4oCyE34yaxI0gFBdJTpLlDhOzKj7_AUFqCxzNhO0OEf_fDZivOPQ8k0X-fqDZSrka214Z5e-IajzYftX4vXwSE481WqUze1BXsudFJ7I65XNv-VZrhtsqFhTnunAFqPAR0Kq4QhBSlBhkphpZ6_YG5mqrMdSMl6zXIM8LddzZ4PMj109PxvqRzgPtqIMf5PprbNRoEu4zcPHATJy50DigertSRwRLwOUY5swVCVfTJglQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه‌نویی: با سبک جدید به مصاف روسیه می‌رویم
⚽️
می‌خواهیم از بازیکنان مختلف در فیفا‌دی‌هایی که تا جام ملت‌ها فرصت داریم استفاده کنیم تا مشخص شود آیا به عیار تیم ما می‌خورند یا خیر.
⚽️
متأسفانه در بازی قبل به‌خاطر شرایطی که نمی‌خواهم بازش کنم، فرصت حتی یک…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/465094" target="_blank">📅 20:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465093">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a929b803f.mp4?token=XRK6g6eNV2udpypNa0NSJaLsYkpLXzxks0kaZBVH3c_sEu1ggnmtnoQFPpjWO7heCeS4fY9s06ZgSs9AYxydQqwBi4_r8Bz2A-rZM0scklgWeM0DqOcUfddagTJcQpKVhUF5SwnNqK8Kf60jUnY27oa5ZliIw_bIF5pdTopcBbPm5Ax4ey2dCk_bVlr_RPez8hmWgxokhEvYiz1sk5vSMVCl4uQ4ZCD4geyGPACPilI_E1ARjqwJrDK_Mk0IZaIXEabP_5aZIREg0t0snO-HC5NgFL4MOjnN0dDiEorR3NxTYDWfFMV9VkjqTDMdBJZhVCg2Hz7yo9uVGPQkPHOjPWhICwf-yakHMnosqg_s8eDInrMs1E8qhy0VgqWOXB1o7O7zFjgCHPKimTJKP7hsObHQAidyoQKBQyfSsDnsddwv7H52R6ednI-EaHVS-7jsqyP0Z7aUCUYAcaNOMKhNDquSF_IxpEfUBMJGY1SmU8sYvFInFTQdPuvBmMT3YNtga0u56IsH0sDMiurG8Vcl0Q3sFuLw8Uy8F8QmBeJyv37mBpxJR-_JZ8Rse0Fzr2yPLm1CeUoetaWHs0n7x67jcWEcGcfUpdOHWsWdErlOiZuLpl3EeXRJbDi74CCnWvy1qKym5vq5a1ErBkggkWF53gd23FP6zqUV7V3IhPq4NEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a929b803f.mp4?token=XRK6g6eNV2udpypNa0NSJaLsYkpLXzxks0kaZBVH3c_sEu1ggnmtnoQFPpjWO7heCeS4fY9s06ZgSs9AYxydQqwBi4_r8Bz2A-rZM0scklgWeM0DqOcUfddagTJcQpKVhUF5SwnNqK8Kf60jUnY27oa5ZliIw_bIF5pdTopcBbPm5Ax4ey2dCk_bVlr_RPez8hmWgxokhEvYiz1sk5vSMVCl4uQ4ZCD4geyGPACPilI_E1ARjqwJrDK_Mk0IZaIXEabP_5aZIREg0t0snO-HC5NgFL4MOjnN0dDiEorR3NxTYDWfFMV9VkjqTDMdBJZhVCg2Hz7yo9uVGPQkPHOjPWhICwf-yakHMnosqg_s8eDInrMs1E8qhy0VgqWOXB1o7O7zFjgCHPKimTJKP7hsObHQAidyoQKBQyfSsDnsddwv7H52R6ednI-EaHVS-7jsqyP0Z7aUCUYAcaNOMKhNDquSF_IxpEfUBMJGY1SmU8sYvFInFTQdPuvBmMT3YNtga0u56IsH0sDMiurG8Vcl0Q3sFuLw8Uy8F8QmBeJyv37mBpxJR-_JZ8Rse0Fzr2yPLm1CeUoetaWHs0n7x67jcWEcGcfUpdOHWsWdErlOiZuLpl3EeXRJbDi74CCnWvy1qKym5vq5a1ErBkggkWF53gd23FP6zqUV7V3IhPq4NEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قانون‌های جدید برای مستأجر و مالک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/465093" target="_blank">📅 20:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465086">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JbBnij4wC4hnq7Vo1z3xHipRWNua4Z3ermvR7_jelA1oaSuAfss_sAMMQo6t2dmZMxlQ7O2lxysW_gOSJjnron-my5tslYrKxKYbiBvQ30v7D-w0_XhqDyAi5wQBFZUFN9QgrRqMZfMbH6xzH5wnMlk_0P-5RgPgmVPm4hhExmKP7jTukvzz0bEByqiaEI52Zsl_TqG7dRhKNU7v8PVWBnAZH1Pj38NinOdE26U7zmsNzqr9lKQuPmDK05Mko_9TnQOBhBVBuIZ9pdIWskugvFiCQEDMeEQakyqq5gvny71rS2q9f-s3YLOMojt7uGB3Qu4KdCggrAUsfezoNXF8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AAjbykief4osA65l3lf87pp-RH5yYVsSf55shKS7ezklYs45munCpVvEobYsg8lu8m_1mmmnqhLKEiYYlBGN05bgvgg2_zeB1cMOsL_S5KSNMVhWBNKTKeWDO7jQTV80oLNCmxHWPHC_qAwLwpW4qnD8KbyVnohprln2Zb-HIeaKsW3I8972nUr9Yel15p0ytID0X8v22CXgvFtjalanCBSNZWqCfqKGHAaxPuZL4foqV3vWhcQ3IK9fsdW32fOljLx6H1DZI_gw5yf_BtYdbSPPmg1bYtM4MyFLwmdG5mClDqZh0fN-gfdobBjdirSlIwFSx9pDB4QTf792W3U5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQZUgSKOO1Enwwt-H2FZh8UkC2gQUlGv8JBVT9Q5N4zI9g49Py6YMlSIwmMme0461BIqG8ocQ1EGsbutBcBg7LjovpG2YvgznAE_nJ1zLPe1cb49WnLTyZXgNYWwFPHu_vrADmlNbdtvaGUgNhiITsdLfj_B1z7agY6wOaSZh9Bh4qzwAu_BdIqtpZgdJALwGtzt7SrnxbEd6ujwcmuf8iNXOKu-L0EWYFPfOyiBHukrGgw-QzkRUJv_q5-YVD6jPafASgnm4kNnpnwm_kC24x7K6EaExz2T3Gy9_LmaE4IDLIO_ZRX6JmogMMEKtvYYEFl32RJwcQjiAzsIuwBMOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdCd2GoYOhGOivih2sEw74G9tANC8bqD19m2mrcTZyzgLVvz387lGhNYegUjBcftn-67PPyMDo7pijrz8aGTfJ3HjtqZous4c1p0POx2IaTECcAIuebu2k_C6rgRjopbGu7pC0Y6v45Pi-7WH4tqHz-hE0pudkGRLMNRDecMkpj5uK1fo3nlvQ6t9kGDG5UApHznLwbgfy22Qdv-aO801ADesyXj6FV_OqXGcqXTXl3vZqLU8lz3HQdP_EWambI9soY95hhc9SrgzWYvmuWeIdoJF5kvqyzKAzQpuvdF95i2Gk1ZCFlKEIGHBDx34grOImJ_6XKXeB9RVtEvGAj_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZcNxQ2BHzZmc_gBYervJZ-yw3K8AiYYrIqhYT_07P-HAoFQzZLkEax__FZNMRrNcviGPPBtvBK150Y-9L15akOScAd99z0c7ftu4TvxbAdE2VEh4IfLULBechsZXyyvxlvND8ARZxv_J4FJSBqiJ1U4k8CE7omH7F54_xarskAqy97H-WVbawDaKsTQT6oiq93AwtLWUHRLbjbWzbvWaRxkz8SnbWiAe-QlNErxyXjwBoA1QO54xtv5CtXalQHXRvIZs3py1LXTGFTHyGPqGUeam37qau4Twp4LHhEawXtMMi7oXfraaZ7xOB2uEAzPPo2VCHG5VmQ862cbgeh40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N46Nhi14yZ9QyFG3m0hiXqXpgVGSfI7yVwKQ6pHn1IbUfoyyOBySS46lYMFV0WRfcLTnSCKnHfCzrW5Yk8bnrDcApbpniVvJ1h_BGOQGSqqZpJJZOpMMuuFEiCyd38l9ONPEdVB5BWw-TJM9O7m_HZZkSD07-WRcLXXi8xHYMEuOgAE_a6RL3VwiaHh6ZONg5S0dbjy_m4r-0ui5E9hgJbCmb79BPiPIbuMLqOsCSgMXqLPv_-v1IjYGYSB26R2MgMMvOjFfNev0e7MjLujzeczmln3vWWJC53y_hw6aD6ggh_oFRiVEvnI14eWFk5S5f7mi9oRqO895OLrrqD9DKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTPy3f0_fxG4Pk55RZ7ki2LripMuGBCu_X7N2auf8SudtCjFc_XvRCyUp-WsEAExp39QZ4xzVNVJLRF-_h1CJIOVT8N7SIQqxgWNq6MTX_zseIQPhT5tVAiD_5DOZlWnJkyBShHUJznzNYRSyFOh5hZUumkZ68zhTUbUpW1VJyN-Na-PdMF9tWHZhzvmYSBQvis38J0ZZICCVOP0wQPYSS8nxgKyPyOpDbhycV9qZb-uQgaTHpFla6N1nZrHB7CpJthEtzDMXqC0Ncq7tP98KHhBEUthRnd-pGb9IkOwjQE5j4OtX-rCKkllAFBquR25RYxm4-WWrCv76kHSmjq3Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقۀ شهید جنگ ۴۰ روزه بر شانۀ مردم یزد
◾️
رزمندۀ بسیجی محمدمهدی رضایی صدرآبادی درپی اصابت ترکش طی حملات دشمن در جنگ تحمیلی سوم دچار جراحت شدید شده و پس از تحمل دوران سخت بیماری و کما به شهادت رسید.
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/465086" target="_blank">📅 20:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465085">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEEch-dgxoRm5XAuMsdwagOfZodQUMa_bcNTTkg1F3N3Oeps-d-VcwB9JFE1dEsigJ0jpexctiZVhXyb1gDqRBvPr9e2GlQwrqGU-fSt-Lj58zOAJ0Bn2G0c2QBY6kdMq9_jDk8DiZs5ByiZyFGSZJ9hrIfOSmlgJI6mT_mDHJX7M0J8BicrSp3v4ZIl18t459y8o1VkR8GsPNlk27wSdmSBjXl-Fh4J5BuIfj9vCdJ--X86lsqcmbQLm4H2C-OSIk-8mV4VWTzDlwz_2ZJGt6skkuxTaaOGG18P1v3IqK72yL0_1BtEPoiab96Zyn4Oh7tuUEla47WawcyUnMBhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درحالِ کاهش ذخایر نفت آمریکاست
🔹
درحالی‌که قیمت نفت در مرز ۱۰۸ دلار معامله می‌شود، وزارت انرژی آمریکا دقایقی پیش اعلام کرد که ۸۰۰ هزار بشکه دیگر ذخایر راهبردی‌اش را روانه بازار کرده و سطح این ذخایر به ۲۸۳.۶ میلیون بشکه رسیده است.
🔹
آمریکا ذخایر راهبردی نفت را برای مقابله با شوک‌های نفتی ایجاد کرده بود، اما پس از بسته‌شدن تنگهٔ هرمز، ترامپ ۲۸ هفته است از این ذخایر برداشت می‌کند تا قیمت نفت را پایین بیاورد.
🔹
با وجود این برداشت‌ها، نه‌تنها ذخایر آمریکا به کمترین سطح ۴۴ سال گذشته رسیده بلکه به کف عملیاتی ۲۵۰ میلیون بشکه نزدیک شده است؛ هم‌زمان قیمت گازوئیل رکورد زده و بنزین به ۴.۴۷ دلار رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/465085" target="_blank">📅 20:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465084">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌ ‌
🔴
سفیر عراق در ایران: فرودگاه نجف تا ۲۴ ساعت آینده برای پروازهای ایرانی بازگشایی خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/465084" target="_blank">📅 20:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465083">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb-lQR5chu5fPrLeeYO6oIHp80KBoUgq2jUAOOHKnlta16_-NoI38BwCr-rA0xa_vQ4ICOqtZx0mpapm9yGHVzrmIKJGLwnxnMJ7vDsttZghKaHSiLqn2oYqUfrMNDcfHh9cPV8lIaYEoV7Fo5tFQxW7Krv7IGGq0febs9-QYifozpW1wDHoRoeTKP5O3E7_cm5VQ2cicha6abhgBHfDml9giqdJppnT9Xn3MP8HE3nhjfy2prAasJUVsvXtpOM2bRLGOq_HL-Kx41tUqFeu4P_NTSczcN8-KhKEEcCz7zVxzxHtYXLk2gLPfMHWrfuL6ZS0fO8FT2EMpX3U6FzgKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگزاری جام حذفی به شرط رای مثبت مدیران تیم‌ها
⚽️
در فصل جاری به‌دلیل فشردگی تقویم مسابقات باشگاهی و ملی، زمزمۀ لغو جام حذفی شنیده شده است.
⚽️
مسئولان سازمان لیگ تصمیم گرفته‌اند که از مدیران باشگاه‌های لیگ در خصوص برگزاری جام حذفی «بدون ملی‌پوشان» نظرخواهی کنند.
⚽️
در این میان پرسپولیس گفته حاضر است حتی بدون حضور ملی‌پوشان خود در جام حذفی حاضر شود و سپاهان هم خواستار برگزاری این جام شده.
🔹
اگر اکثریت باشگاه‌ها با برگزاری مسابقات جام حذفی با این شیوه موافق باشند، این جام به احتمال فراوان برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/465083" target="_blank">📅 20:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465082">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56844090bc.mp4?token=OW4gXY4zRZ3DrCxhsVYhfCk_HPC-4NoNgH1TGLqzASKUJwhzeUvC-gRVJmmmxdnnXSsyxf4iMTyjMERcy4C1JJGO5SHLydZZvU-hcIDBM4U_q8JvyaULXrUKEB-46AAPQKxilqBy5OIFPIVN0yy8M1LUUPp8B-lmKBgkoek9MUXCHpbgfVEozlCZZG1omFM_8GnO8hxqWAnH3VJ4pflG59oJXvEPzIWgXpynxHDJV3gsGmfmoVrIAs3WZiupmTe5u-nUBaZzg7PwBk25o7IRIAGwMXTqPOD8ZZrQS-MtsTJgpPnLhGRo5GYKkZKAbcrxUpYyCDCD3hkki9N02dWAHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56844090bc.mp4?token=OW4gXY4zRZ3DrCxhsVYhfCk_HPC-4NoNgH1TGLqzASKUJwhzeUvC-gRVJmmmxdnnXSsyxf4iMTyjMERcy4C1JJGO5SHLydZZvU-hcIDBM4U_q8JvyaULXrUKEB-46AAPQKxilqBy5OIFPIVN0yy8M1LUUPp8B-lmKBgkoek9MUXCHpbgfVEozlCZZG1omFM_8GnO8hxqWAnH3VJ4pflG59oJXvEPzIWgXpynxHDJV3gsGmfmoVrIAs3WZiupmTe5u-nUBaZzg7PwBk25o7IRIAGwMXTqPOD8ZZrQS-MtsTJgpPnLhGRo5GYKkZKAbcrxUpYyCDCD3hkki9N02dWAHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید عهد سربازان نیروهای مسلح سپاه و ارتش با رهبر شهید انقلاب در رواق دارالذکر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/465082" target="_blank">📅 20:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465081">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca84a6939a.mp4?token=vV353Y6-HvtMJXJWNfq2vnea18UPPG7gglineYrHRmS92ttR8zG3e28Pgw8jDL6j8NpJdYN_-a2cWCav3WCGuikQEGlLHnah76pvRga36YvBXa98v1Xh_y7RQNQ5fA2mVW_oCJ-d_TmHfqSLvm8wVGwYxYrUrVjcm_So50_eHL9_p_SJJOeu6MLODPikxrIKDxQRvjdju2Yw3_putsfhW8q54RGKGKJ0tQL1UmJ-oHf4mhI3CF5_EeIlZ-UbuDi_IPbcdGnKrIPbh4wToU7DGy8S-VTMNpV38AM1knQDPi_1w0Jvk3vY7S01zRVOyMkH7PoxuoUAozpV_sM_1irKFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca84a6939a.mp4?token=vV353Y6-HvtMJXJWNfq2vnea18UPPG7gglineYrHRmS92ttR8zG3e28Pgw8jDL6j8NpJdYN_-a2cWCav3WCGuikQEGlLHnah76pvRga36YvBXa98v1Xh_y7RQNQ5fA2mVW_oCJ-d_TmHfqSLvm8wVGwYxYrUrVjcm_So50_eHL9_p_SJJOeu6MLODPikxrIKDxQRvjdju2Yw3_putsfhW8q54RGKGKJ0tQL1UmJ-oHf4mhI3CF5_EeIlZ-UbuDi_IPbcdGnKrIPbh4wToU7DGy8S-VTMNpV38AM1knQDPi_1w0Jvk3vY7S01zRVOyMkH7PoxuoUAozpV_sM_1irKFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تجمع عراقی‌ها مقابل فرودگاه نجف در محکومیت توقف پروازهای ایران
🔹
مردم عراق در پاسخ به فراخوان جنبش نجبای عراق در مخالفت با توقف پروازهای ایران مقابل فرودگاه نجف تجمع کردند. @Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/465081" target="_blank">📅 20:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465080">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3GqPdgAtvt965sOZJqCJCnDATeeRWmWrlQBxInlG-IYT-0YOLl6CKvRvb65WbYj_PF6WddPlDSwm3g02fmDVcd3FKHlSr-MOq_uKJKO7_n_Qy1qqJ4BljhKaa_Odc_7KxBmVAYH2NYQt1BU0VQ_2ABP6bCbExWyoB2OUxPWTLfiU2f0kguf9AmRJJN90yuAqozHMQyFqLgH1yREaO-nQqiOYHQ-IgUAzzWkjZ_TOJELIt_x5PGNkHjNmqZRsUsAdvrJwe58_9c0ldMvlRsaazrA6vn0cqe6UIgQESJu2unQHhGxfa0cRRXtb41ZNBAFoNCKoh8p5_mZaS645P_hgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: از زمان انبیا کسی به بزرگی شهید نصرالله در سرزمین شامات سر بلند نکرده بود
🔹
در این مجال بسیار به‌جاست که به‌مناسبت دومین سالگرد شهادت امیر قهرمان عرب و نماد بزرگ جبههٔ مقاومت، شهید عالی‌قدر جناب سیدحسن نصرالله قدّس‌الله‌نفسه‌الزّکیّه، یادی از…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/465080" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465079">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVgSJoqrWz_APDJZr00TeP8uM3KHyepdxTM6pItsAR68EIbkc41frKsFEnOu6D9nqVpxlyOY7K3Be3W5Ngo1bqYZtSjM_PdSSMYKnK6jG1Xi-9FOwE8CmLNW7lKwIJlqh_1nr44oGmTSPhnudjccsLWPfeTz7UIHgEJ_Q5e98h_BtsohBuusrgIaA29-JOmMMNpCW_mIcPaPLF5gci23o5QzTHkAmHcCAj496U6keBmSZGbvn8l8dd8XE2hoZRZrt2qiyrzokHRTfmDwyqvvI-e3Spp38_uFyDxM0bmFyqr2SrdX8pt2b6Ri-RYcIehBFcXaCuYUM9eg02D1XI2IFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران باز هم مغلوب گربه سیاهش شد
⚽️
ازبکستان ۳ - ۱ ایران  @Farsna</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/465079" target="_blank">📅 20:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465078">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJM-CGAInwtBr9XwD6BXg1McDyjCgTj_3sXrLw7Gal8I2aJmr450J37i2XWLYhfzwKkJRpUikl8Q3QHO42E4tYEL2I0m2HeN3to3jP18VQHTbbsgaaOmGeSAPJAOzg8wTwVseulIigVob6uFss0vlq6IIUuWADJdJ9_vO_HgQcVRMyJJKA8-YSs8mjTgEnqP07bbsrH63CE0j6dhiSLIGoeK_TRFfBNYzAf-Zb1DZa9-OZUQmJUNAQbyxTKudjtCEhWTqEOQ7z8siduoBr58F2RStFv8QXQ30VRm3X8a7hAmdE5HaMEIrEJrChgAcpEcwe5cnHSZkU43ULUlyciwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هند باز هم قربانی آمریکا شد
🔹
رویترز: درحالی‌که سال‌هاست هند از خرید نفت ایران به‌خاطر تحریم‌های آمریکا محروم مانده حالا هم به‌دلیل آتشی که آمریکا در هرمز روشن کرده، نفت ارزان روسیه را از دست داده است.
🔹
دهلی‌نو که ۸۰ درصد انرژی کشورش به واردات وابسته است حالا بازهم باید به‌دنبال منبع جدید نفت باشد و معامله‌گران می‌گویند که به سمت محموله‌های گران‌تر جایگزین رفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/465078" target="_blank">📅 20:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465076">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWLpqq6ZKbBMWCJMM4UW3DQDsh8-YQUOSREsG5oaPq_Lu8_KWOcsdI-Hmzq8M6LZnKoZkW3C7FgZtZJCenYGXbaQuHQuuTW2hzNUDvghZ9rCfZCx_tvYHdAXv3QStKsigptiKMoerUxtrCWIXZJxk2OE7Nmn3fRA760vaTp6-WmceDBp26DK8HXYmHDUHuI5iES65xOjyQ0BAPsPl6XkX5fskswcIAgHwC40e1S9j_9ptU7NJPO4EFP3QPv5OqdxRETIw7PMJpBq1npQoMe-3iCZBfEtmpNH573TZHHTFfQpoQplZ4aHkm_4siekxumD2vyTCCcwnphakZ5xQKs8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fd8c8a9c3.mp4?token=Q5KwrHHSjd_d6_fjGFbXBQGOZf0R64lY0ZKHr_8nqh1DErIqsccOLbo1UIABohhFk0KgGiHNeEdYOBKgHN4u1JaDqQnGYNvayw8GvVX5jxlAt9wU86DLacjFsUsPOJMPXAM2KED4pocyafanhXtmHMTOdpKDe3LEuwpPJ9nGX3D95WL2HUmE_90eo_Es1r44No7SbYYA3u5fjotIk9fsShK7bC-inczFkurdxIvdXD4w9UHjwKwYLzjIHPxzDOr31hEhn5gRMGTVGwaxvr6KdYyq6lzRYJV4ZFZgK-o4b6SGD8-I6ch24DVEb5YrHsR1LQG4qcbLBDK1UXskKm_VKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fd8c8a9c3.mp4?token=Q5KwrHHSjd_d6_fjGFbXBQGOZf0R64lY0ZKHr_8nqh1DErIqsccOLbo1UIABohhFk0KgGiHNeEdYOBKgHN4u1JaDqQnGYNvayw8GvVX5jxlAt9wU86DLacjFsUsPOJMPXAM2KED4pocyafanhXtmHMTOdpKDe3LEuwpPJ9nGX3D95WL2HUmE_90eo_Es1r44No7SbYYA3u5fjotIk9fsShK7bC-inczFkurdxIvdXD4w9UHjwKwYLzjIHPxzDOr31hEhn5gRMGTVGwaxvr6KdYyq6lzRYJV4ZFZgK-o4b6SGD8-I6ch24DVEb5YrHsR1LQG4qcbLBDK1UXskKm_VKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازیکنان ایرلند کفر صهیونیست‌ها  را درآوردند
🔹
در جریان مسابقۀ تیم ملی فوتبال ایرلند و تیم رژیم صهیونیستی، بازیکنان ایرلندی با انجام چند اقدام بازیکنان صهیونیست را تحقیر کردند:
🔹
کاپیتان ایرلند از دست‌دادن با کاپیتان تیم رژیم صهیونیستی خودداری کرد.
🔹
بازیکنان ایرلند به‌یاد مردم غزه با «بازوبندهای مشکی» در مسابقه حاضر شدند.
🔹
بازیکن ایرلند پس‌از گلزنی بازوبند مشکی خود را در دست گرفت و بوسید.
🔹
این دیدار با پیروزی ۳-۰ ایرلند به پایان رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/465076" target="_blank">📅 19:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465075">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5Qj87Fyi8FZudDncPQxbto1tD1AIjm2P2Rui4AQ90TQxOBCpEqA8zsurMX9u9soRSwGZI9iyBJej4UFIQZ1x-TMlTnrSYSQY9Sehi3L4PFhiPVI55T4a-IYK0NQXG2v-MvhmwtPTZ3mE9az29hgJMMI07Zdog8herjWZPcTcPGLTgQwqCYJvkAkCnIb-2pSbUeJjE1TNrt4eHK5ZwJJS8P0f4e_kkRIxOPmQoRNe9FrSFh2KQALpEr3abmgQokhBxutEE2owz760ukQ7nwx2qQGCi1a8FhiVBJGpDZsiMfbUA-zTjdw85oCY87ZXbjOeiqUSD4kPIj1V17llwyXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک
‌
صدایی احزاب اسرائیلی؛ اجازۀ تشکیل کشور فلسطین را نمی‌دهیم
🔹
یدیعوت می‌گوید احزاب صهیونیستی که در انتخابات پارلمانی اسرائیل شرکت می‌کنند، بر سر توسعه ساخت‌وساز و گسترش شهرک‌های اسرائیلی در کرانه باختری اشغالی، هیچ اختلاف نظری ندارند و همگی بر جلوگیری از تشکیل کشور فلسطین اتفاق نظر دارند.
🔹
به گزارش این روزنامه، احزاب اسرائیلی مخالفت خود را با راهکار سیاسی که یک دولت فلسطینی در کنار اسرائیل بتواند به حیات ادامه دهد،اعلام کرده‌اند و در این خصوص، هیچ تفاوتی بین احزاب حامی نتانیاهو و احزاب مخالف او وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/465075" target="_blank">📅 19:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465068">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6U4QBt1yi4lAltt4HohhNSh3_eBR6A8KX4fzf3qxYC-S8dnxC8vR2YvBDwCYpH3vp3oSBcMPUzE8iDbW871hZ3tZubGhVJtD99yS4naEAOJbJhOUb5SACdOAhD1hbW9f95vRLV7fAsQPS-aa7aLOmNEvlRdUGhAqn-Z_f_Q0y0GyrAWoUFkLwyLJdcScoAJS162CaGOa1UI2t6mPB_f4gvcf-VyBpKtTrIsTa23Cw3FfD1iuC4xi8fcxMbE68KpTjnm_XZUArVSNehAoUby3yP99LXCuWljJlXqDCb8JlNlwhr6HvJgPta8tspKaVBKFbtZys3a3EBu6grmxceGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1pbAkv1CZwNo-b7ZR7nxp7g50Uq8HwpRan3DY-sdCOO0UK-NIpaFeHrAaYpxmdIw7xcuvki9W79ucp99kjqYH1CnQJ-XWKDRz-x-4ymoHbM8ULdn0lpSBJwP7ZeihcSNJRjTYdGZo2EVyhEr1YNfqNaAnwmhry-jcfEBqRXocnFSsRoB2l2KgNtezLnbsyLJJinAbyMake38w27g8gwv9dJLMz6xH9TtlwEvI3bAubTaHQ2Ef3DzFiaA9SCVdG8IUoY9ARlsG5hjo-D6X41OixX06uYQpxtHyrDMs9sBgR78s4Avry1GnF1_3m_vNXgUFK-a07OoKyBh9_Sf3meXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDJ78pUsWknv4NU29mCFgzUoLeAEJ0uA-RW7LwY4c3rTu56etNc1bVJ9926eF_C9_mqZi07ogFi0ROX8cSU1ZtB-1Y2w_TSmaNjVGREnyfZmaecrS2bdYFhMqlgP7L2EMFd68HkASLutPP5uhnlyId02hetKc4VlVrPHdt2qMkv4H2aAVnGqKDf9oP4YILW4rosZt3t2e0mqgkW2D5k-_JVOUy-FjxP19A5j1cDJh4inns8iAptcBBfdpjnyaZfj7P6BYLrQQsYLBp03AyhsCkLHzqQSdHNs92k_uFAEe6U54SuLQlUvkUKzXuqNC0Yh6yRRiygXnRIcoVWtoHUkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUfx_Vgi9LbsqVkehCPxVHTOe32CfFaBLnFo6_u4Ek3yxT0oxaKwtlOmL1DXnqdOjaqnRSrcNc80va1GeHaATwPPKS5Busz251yiwXNyqB1hR1J0keF2dMZ_xXpF2sGvFibtwcW0uCaVMGNFOQwrr0-5oL2duwbSI6IKDNHrVpET0mOu82fFHRkJDXUO5cXA2yJhKqZ6AK9ivJ8GOwRM1STqmsfGHnqgETNJLOr-bH0r5nkbOSYKSHocfXYSF0rxO1fefEj209T_uNtIG67gWa5uwalSVMR7ah9QzhmP5B-95usaDjj3OgKOU-TiMYsD4-dC9LLrE7AjxdMM6XU7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdypMKeRzI3djOaC192-7V2dLd54fTJJYyfLCqIQ_-IuKH7A4T-6JPmp31Ry1uv-6t-S53-51rWDxyM2waX_kKoI3HlSrS6EuS8bSu9rpkaVOqxlvz52DWONNu9lyXIKnxDjbnYKOD1PQJIjvxDN3JbZ19a_iTP2-WcUR7UYR5PNcdl4GQ2tskyFJVgFERGy97juikImhksVHj3G4r0mOJELJX0hdQm_BPu2LqFgmS_zvTHDs3R--blUhiFr_aZSGEmYVCNqK5Jkv3aUthr5AxB_edLIOkd1g0RULsLZBp4K6fzr2hiGBusPQ2jhuxh6FykTtoTvOHu9M2l4hlUBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdy64perouQu9_zcx3i0nJ6sDi--RUPA05aJUocs42HVFJYHjyoxH-VheSWFi9L-usCuBisbr2RM0HvFWnRihtIPNjKJS0-32X8WGwurQin2YFv9SrQwZwuiU5b8zIwGglD_kpm8Ma4h10MN3dP22SEMBoURShYGkHNniKRfU-gpExPY7lMouzWsX0ALzLpji2I1siA_coWR318cmuOqGnBpf5bp2uFuXlbP6Z93B08qQivALA-nQqkT6NzwrSYWj1R7vHGNYFgVvWJXhFybA5DrBAKx2Q0nQUrrBg1CThuiG_7htyWbsV074Wq_aPlYC6X8aXgfjwQq8180sY7BGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhMBdSgq-klYfiQa0QcCLNH2JWVG6bT438oFoZQ-l9wYYOb5Gkg62eNUsTvbMTt2N6TIzjT5KMw9EoqSKVyWHYUtFD4-v_9Yot5PgEjOUEGY7e7UQ8fpTkA1lM35mtTbFWKhYCKtV-SvQOlaY2pIWfQg6-iLHrgvV-scdD779Uip1-RmSz-RoLVF3PyZkylU-OeE4q-E1a6V8ejcjXt18XY0hwq81CcI_i7SGCuG3dqlGCzIvrjQYhOITrFi2XfACtwW2GoWu37wCkWgyHwdudDEX2pU79CboOLRZYPkQuGD8Uj-fG9uTAKlAK-BFZQOjH4UnHkc-xCOyPa5iTfupA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اینجا ارگ کریم‌خان نیست
🔹
بنای تاریخی بارده تنها قلعۀ برجامانده از خان‌های ایل چهارلنگ بختیاری است که حدود سال ۱۲۷۸ هجری قمری ساخته شده‌ و از نظر شباهت در نقشه‌کشی و نمای بیرونی نمونه کوچک از ارگ کریم خان در شیراز است.
عکس:
عاطفه گنجی
@Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/465068" target="_blank">📅 19:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465067">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
تاج: سرمربی جدید تیم امید تا دو روز آینده مشخص می‌شود  @Sportfars</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/465067" target="_blank">📅 19:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465066">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpHbHL5Ysp-GdRov1bI3hpWhXiufz6ozFPwRDxPhkK8kg1O5WOVMOqOf93d1miotUs4c217D9j3amxxF1xeui-JWEYNrug6z_I8b4zIMOULPzAeh4iww65zgJRGVkw9detU5TICg5bjrbei9aaj66kfBm0xyIotzRS011mBVUbpiTOr6l0dduQmOBMShlv8w7Z9LVVrQWOq4r2HDtTh6oRpmB_rOywXvKgpG8ylltQK-W-_LPYhEHu-9Jeq9t0xsLTVOTT5TMccJaguHeDtOSvXHj6K6Gs0kg_TmK6wSaHppeRjzxlx5hMFgsL9XIGZeeUZa0qPBZwvqCDXwn2TgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست: پایگاه‌های نظامی آمریکا دیگر امن نیستند
🔹
روزنامۀ واشنگتن‌پست در گزارشی دربارۀ آسیب‌پذیری پایگاه‌های نظامی آمریکا در برابر حملات ایران استدلال می‌کند که جنگ جاری، یکی از فرض‌های دیرینۀ راهبرد نظامی آمریکا را زیر سؤال برده است: این فرض که پایگاه‌های آمریکا در خارج از کشور، به‌ویژه پایگاه‌های نزدیک به مناطق درگیری، می‌توانند در برابر حملات دشمن امن بمانند.
🔹
واشنگتن‌پست پیش‌تر نیز در بررسی تصاویر ماهواره‌ای گزارش داده بود که حملات ایران از آغاز جنگ در ۲۸ فوریه، دست‌کم به ۲۲۸ سازه یا قطعۀ تجهیزات در پایگاه‌های نظامی آمریکا در خاورمیانه آسیب زده یا آن‌ها را منهدم کرده است؛ از آشیانه هواپیما و پادگان گرفته تا انبار سوخت، هواپیما، رادار، تجهیزات ارتباطی و سامانه‌های پدافند هوایی.
🔹
به‌نوشتۀ این روزنامه، میزان خسارت بسیار بیشتر از آن چیزی بوده که دولت آمریکا به‌طور عمومی اعلام کرده است.
🔹
این روزنامه می‌گوید ارتش آمریکا اکنون باید میان ۲ گزینۀ دشوار یکی را انتخاب کند.
🖼
اما ۲ گزینۀ آمریکا چیست؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/465066" target="_blank">📅 19:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465065">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUU4OTEhwjULYztBdJK9C9rPADp4koAXaPo7qiD83i4E2Vs8i2FM3FG2whsK_lP2sqONUCZXp-YD_Juy36Qfnla9MmAimFN1QT6u_WR7ZQVmtq9WLTSJnJI3nIeeE03Y1Q9aTygMi8PcUeFtj-zKvPDXRFMmTYDGK8PyZlLSCRor8aMv3YNF4Y_k6zfKcxUo7Oq49eWtdgRJetKEH9J8QJ_ulmZ8llqh40XSk4NKpM-Eda-2hGXvAz71-FQAwgGAmyQoDbvhZWURmS-tQQOoG3ItPDonMJXwwRgw3NIBh-ymkL84UsCDsGtPZExIjeL8h98cUytmaEPbQ9eQu4EIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: کاخ سفید گابارد را مجبور به استعفا کرد
🔹
درحالی‌که ترامپ استعفای تولسی گابارد از سمت مدیر اطلاعات ملی آمریکا را به بیماری همسرش مرتبط کرده، خبرگزاری رویترز به نقل از منابعی نوشته کاخ سفید او را مجبور به استعفا کرده است.
🔹
گابارد در سمت مدیر اطلاعات…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/465065" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-oatZCWWMcPk63FxcHaBtwbsrMYrh5hr_W_3wVtG_kEem6BncMuu-XSycAiJ0ecCHp3QS3m_Lauyviez0Eb2IQ9WnxfxqB2F2My5_cDw6L3A6D7wu9mZtMT6J3UGx3qrvmETR_cE2CIGZ-f3ROwNRvArl2Kk_KOTKAPLvxhmC4vdCV0TzYtc-QPWBN8ybOAMQ18k-HDcWk-0UWAAXQU3VWdKVHW65hi_n2QemViXdYId3_tA2zSSJxeX4apnseUKkIA-6QwWHzfKz9wIeBPdcswdIRCYRFrSCvK1kriNoyL9YPWyMIJKX7wYXjiNxU3Eioaogajr8WOMFqj1iDaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستادکل نیروهای مسلح: رزمندگان ایران و مقاومت به هرتهدیدی پاسخ ویرانگر می‌دهند
🔹
سرلشکر عبداللهی: دشمن صهیونی-آمریکایی گمان کرد با حذف فیزیکی سید مقاومت، ستون خیمه مقاومت فرو می‌ریزد اما محاسبات دشمن، بار دیگر  به شکست انجامید.
🔹
جبهه مقاومت، نه تنها تضعیف نشده، بلکه به یکپارچگی راهبردی آشکار و پنهان رسیده و راه شهید سید نصرالله در لبنان، فلسطین، یمن و عراق و اقصی نقاط جغرافیای مقاومت و حق طلبی با صلابت ادامه دارد.
🔹
نیرو‌های مسلح ایران، در کنار مجاهدان و رزمندگان مقاومت اسلامی با آمادگی کامل برای پاسخ قاطع و ویرانگر به هر تهدیدی علیه امت اسلامی ایستاده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/465064" target="_blank">📅 19:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465063">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuYeTveG0bWCiXN3ooZzPRInxleHMMH6BPIVvvoRFuY3z1B8RfSJZDnaE4b4-0ZWxHnnH1saCm2Aon2g4wsk0zeeNKI1xiVz6R9xzO4veNs_2Dm6bDcpXXd5rwHPpPRWUbQSXxm_44PuPyCSuh2W2sqrbvcby9VKJK9J9FQhs-cYhpkqqhHMATQRsY8XwyM81McgaAfWdfg7sfRFXsz1Z-k_4HT_7lHNasep8nHzcNbFrgjo_FMMaGHqa_oXjl9zMO2Y1DMIQDGidHkGvc0oNNJ-bLsG8iUuEv2BVJh_R2kU92VVhevU-RQr4F37eBGnOgQ1ELjbice2Qp6F5BpCuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عالی‌پور طلایی شد
🔹
علی عالی‌پور با مهار وزنۀ ۲۱۸ کیلوگرم در دوضرب، با ۳۹۸ کیلوگرم در مجموع هشتمین طلای کاروان ایران را به‌دست آورد.
🔹
او ضمن دشت مدال طلا، رکورد یک‌ضرب، دوضرب و مجموع دنیا و بازی‌های آسیایی را به نام خود ثبت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/465063" target="_blank">📅 19:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmfXm9ILbqdaxku4ieQ0TvhB1hBqAd6rRUYn9FHhQQ-R7vpiShFUtWUsexuufZAtfQ-ocWEGQbi7N_GY7V59layO40p8TYXhR3fRPEVz7yqTtteeehDAWok_52hbiT6GJJYkqmt8Qe99JsYXik9Mrg5UO3h70a6k9T-1KDw2_f5i8hOXRgIkHQBCECn8d0R8KPOS_2TcSTa3HrxMGu2nD21iohw70B5RiuhM_qF9mTlwjrkVJoUxXwbepHZplLmyp1Qn2CdfsaGVFr_wodiiTLgMBLT7kOTCm_iD9YRHeOPVgIvsH6UmJNhLfVsq3DO0-4h3AJ-RSARjxHAtGdXelA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی اصلاح‌طلبان در پازل فشار تحریمی ترامپ
🔹
واشنگتن هرگاه اهرم فشار را در دست گرفته، به این امید بوده که بتواند در تهران، به‌ویژه در سطح اجتماعی، بازخورد و اثرگذاری همراستا با سیاست‌های خود مشاهده کند.
🔹
اصلاح‌طلبان هم بخشی از این پازل را در داخل ایران تکمیل…</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/465060" target="_blank">📅 19:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۰.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/465059" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۹.pdf</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/465059" target="_blank">📅 18:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab35bdcd98.mp4?token=VEE3eAc6IKrt4APBvpBSH3OZ6d9GuLnTWCfC16VGTBBwnayQIbsWACjQyRSdM1LqzM1x6fgeV1-BgTxAUCDqcb3QsFzU0HVLuDYIszX4VPoCll5cC5yeVY9CDOnoiFFEV160waAnFvfK50m9xPD50eX6nGODBopowLiztwkXzKTFO4nfF4ExRJ8m2S8-kq0jPn3OjmpUs3dk6FlUPqur5_c9weIYNj6gb82s7HS3KciQRCcC9exwSLnML8Sn1W-NlCAArmRUseTpkCWRax_LlTtNNXENFstvxHVCpyQxToG1H1igAsPhl9rVE8NmL3HJimma52JDdwCtTMYZCz_4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab35bdcd98.mp4?token=VEE3eAc6IKrt4APBvpBSH3OZ6d9GuLnTWCfC16VGTBBwnayQIbsWACjQyRSdM1LqzM1x6fgeV1-BgTxAUCDqcb3QsFzU0HVLuDYIszX4VPoCll5cC5yeVY9CDOnoiFFEV160waAnFvfK50m9xPD50eX6nGODBopowLiztwkXzKTFO4nfF4ExRJ8m2S8-kq0jPn3OjmpUs3dk6FlUPqur5_c9weIYNj6gb82s7HS3KciQRCcC9exwSLnML8Sn1W-NlCAArmRUseTpkCWRax_LlTtNNXENFstvxHVCpyQxToG1H1igAsPhl9rVE8NmL3HJimma52JDdwCtTMYZCz_4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیگر چشم صنعت به قطعات خارجی نیست
@Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/465058" target="_blank">📅 18:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a12cf0201.mp4?token=bb25JC4DCeXSDJWkhg5aQ7Q5JXEIxySo9rtTiR8PSBxyNxqvOsbGC2raenOxKWee6TKUQDcJ_dsjQ5E55T8D0qieqEYXN85AFmrHT628ptavsNnE-rEjQuaZq0XBRjA6daivg_GruuW1BBk5zCqRtQC4wBwFVHrMkAEir-nZY07CKrg02WmBYW-ZRXoGl_PTON4CVCrLhbKo-ygcHGJ8ceOFpR65E0XDKG7oxryUmzcHcZPwjlhsEciBtFKfIrDQde0B0GaeN37UTJBY924wfoq_8_hBitbNzbsSYejqWjMhjo9dXZ5f_VVyPaRkuKLKWqsE-zWtKTsP6-LZnxXy8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a12cf0201.mp4?token=bb25JC4DCeXSDJWkhg5aQ7Q5JXEIxySo9rtTiR8PSBxyNxqvOsbGC2raenOxKWee6TKUQDcJ_dsjQ5E55T8D0qieqEYXN85AFmrHT628ptavsNnE-rEjQuaZq0XBRjA6daivg_GruuW1BBk5zCqRtQC4wBwFVHrMkAEir-nZY07CKrg02WmBYW-ZRXoGl_PTON4CVCrLhbKo-ygcHGJ8ceOFpR65E0XDKG7oxryUmzcHcZPwjlhsEciBtFKfIrDQde0B0GaeN37UTJBY924wfoq_8_hBitbNzbsSYejqWjMhjo9dXZ5f_VVyPaRkuKLKWqsE-zWtKTsP6-LZnxXy8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کالابرگ بیشتر برای ۳ دهک اول؛ مطالبه‌ای که مردم مطرح کردند
@Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/465057" target="_blank">📅 18:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">دشمن چگونه روی دوقطبی‌های داخلی سرمایه‌گذاری می‌کند؟
🔹
دوقطبی‌سازی زمانی مسئله‌ساز می‌شود که اختلاف‌نظرهای طبیعی سیاسی و اجتماعی را به صف‌بندی‌های «یا این یا آن» تبدیل کند؛ مانند «جنگ یا مذاکره» و «معیشت یا مذاکره». در این حالت، مسائل پیچیده کشور بیش از حد ساده می‌شوند.
🔹
مهدی ترابیان کارشناس مسائل سیاسی معتقد است اگر پدافند انسجام و وحدت جلوی این دوگانه‌ها درست عمل نکند، ضربه می‌خوریم.
🔹
به گفته ترابیان ماندن در این دوگانه‌ها، ماندن در برنامه دشمن است و این دوگانه‌ها آسیب‌هایی است که ایجاد می‌شود تا تصمیم درست نگیریم. ما باید اختیار داشته باشیم در هر لحظه متناسب با وضعیت و شرایط، درست تصمیم بگیریم.»
🔹
جنگ و مذاکره لزوماً دو گزینه کاملاً متضاد نیستند و حل مشکلات معیشتی نیز تنها به یک ابزار وابسته نیست. سیاست خارجی، توان دفاعی، اقتصاد داخلی، تجارت و دیپلماسی می‌توانند همزمان بخشی از مجموعه راه‌حل باشند.
@Farspolitics
link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/465056" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجار و آژیر هشدار در عربستان؛ حملات یمن به جازان و نجران
🔹
براساس گزارش رسانه‌های سعودی، طی ساعات گذشته صدای انفجار در شهرهای ینبع، جازان و نجران شنیده شده است.
🔹
گزارش‌ها می‌گوید صدای انفجار در نجران و جازان پس از شلیک موشک از سمت یمن شنیده شده است. این دو شهر در هفته‌های اخیر نیز هدف حملات یمنی قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/465055" target="_blank">📅 18:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465053">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594628ec59.mp4?token=YkQ8rBCGBs7BLEk5C9uTaWZqN6DdZ3oIShkf5KJjteTxWSW_dgJAI5jDX6TCpHKME34TxVYAoTJ-I4DwhI37RodPj16m3q8idKm73W1pnfZC2-c4PXal8mVMPwaLCoG1AtCmjcxgfra0Z8BFFXmdeQlmT2t3XCp3vmH078mGqivX2eU5Aw1tsRgRoDD0OqSlonkj391wuF17gxOATtLHEEMAiIbuGwuYPv5g14XX02w9mfTU78EaVKjhtMc1lh_8oQ6jpbooB2GXGz9x7YDsOkAMKQy_JWFCtG-5x7Uv0JqXGAudNQc2DkwlvBbJByURBXE1c__IMjWYBNj0ccbTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594628ec59.mp4?token=YkQ8rBCGBs7BLEk5C9uTaWZqN6DdZ3oIShkf5KJjteTxWSW_dgJAI5jDX6TCpHKME34TxVYAoTJ-I4DwhI37RodPj16m3q8idKm73W1pnfZC2-c4PXal8mVMPwaLCoG1AtCmjcxgfra0Z8BFFXmdeQlmT2t3XCp3vmH078mGqivX2eU5Aw1tsRgRoDD0OqSlonkj391wuF17gxOATtLHEEMAiIbuGwuYPv5g14XX02w9mfTU78EaVKjhtMc1lh_8oQ6jpbooB2GXGz9x7YDsOkAMKQy_JWFCtG-5x7Uv0JqXGAudNQc2DkwlvBbJByURBXE1c__IMjWYBNj0ccbTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تجمع عراقی‌ها مقابل فرودگاه نجف در محکومیت توقف پروازهای ایران
🔹
مردم عراق در پاسخ به فراخوان جنبش نجبای عراق در مخالفت با توقف پروازهای ایران مقابل فرودگاه نجف تجمع کردند. @Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/465053" target="_blank">📅 18:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465052">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a637907dd4.mp4?token=bjUiLCkXvdAsDgnuu_fbNTjQgcqhDMGXoy4pLSV7a2XMfT9yrKmiwXggp0inqZyOhUwnalJDPjKZBAcvEQhbcMJ3cqGm8gbDRn8-vd8qo0HW5lg-4rV0ETKDxv2D2AMjm1kuHFNCka7EdmfuPMDEIdEgKinLpcSiFp_Hy3yPi1j3OFGjFKsUCpdRhLBgOiW4aiaUDg2Ae0R6kA1rJlEQauEhz8f-bCWdFZ5feZFBn3fAZmv9KCkF06VmYv0tBPE7XenazxxLX95_1hFMpVK8JeKFwoFeOReMN-dlpR9Me3hvOvClTCWMq6gkllPp4EHWYVBSAviH0echyjMekdzu0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a637907dd4.mp4?token=bjUiLCkXvdAsDgnuu_fbNTjQgcqhDMGXoy4pLSV7a2XMfT9yrKmiwXggp0inqZyOhUwnalJDPjKZBAcvEQhbcMJ3cqGm8gbDRn8-vd8qo0HW5lg-4rV0ETKDxv2D2AMjm1kuHFNCka7EdmfuPMDEIdEgKinLpcSiFp_Hy3yPi1j3OFGjFKsUCpdRhLBgOiW4aiaUDg2Ae0R6kA1rJlEQauEhz8f-bCWdFZ5feZFBn3fAZmv9KCkF06VmYv0tBPE7XenazxxLX95_1hFMpVK8JeKFwoFeOReMN-dlpR9Me3hvOvClTCWMq6gkllPp4EHWYVBSAviH0echyjMekdzu0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاندار تهران: خطوط ۸ تا ۱۱ مترو وارد مرحلۀ اجرا شد
🔹
معتمدیان: ۱۵۰ هزار تاکسی هیبریدی و برقی در حال انتقال به تهران است که این اقدام به کاهش مصرف سوخت، آلودگی هوا و ترافیک کمک می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/465052" target="_blank">📅 18:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465051">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7ZSjkRR5Sj3Ny4RQ0KOV_ExAWpZuvrMGysv2OjesfVNxv8q0Uzf_0SV1IrlR6fi_duQJJyrbXdkKpKFwZlLExb9crJPIHTAT9YAZnQAoI4nzvBHhgczqRSWn5Ez4M2W-heFL0Ox64MxH2jKY4cWrL3Ly8zoTSx3e55BcRCU596SZPH-aaXr4kWeh59UEsRYb2MmoTiy8FVtqBiB0_ddiXFLT1tWIjqalCW9LVvgrMOXks_dOVh2xEMPWIJcY4sAC_OzHbCfVgECToasQFzc_7XE1XUaaZNO6hzkAOQ85g0s2eGJrSnA4CYPc9v3xkBe-q6phvf4LzK7uY8PrB0-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان جنبش نجباء برای تحصن در مقابل فرودگاه نجف
🔹
در ادامه واکنش‌های منفی به تصمیم دولت عراق در توقف پروازها با ایران، رئیس شورای اجرایی جنبش نجباء خواهان برگزاری تحصن گسترده در مقابل فرودگاه بین‌المللی نجف اشرف شد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/465051" target="_blank">📅 17:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465050">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRmx9Sf2PHl-Hv5EdI_AK5K1PpE4TYEJu-2eUpxWuI34O489fh3Syj3vbsg4YZq1F4aOwDKw9MQJTp9C41AF1r4JsULRaNMroJmAoYMBicsZ6kRNZgIPxPyvaUsUsubica6wVZGBaVqErdJUpdHfFSMqijb5JKkLlkR0U3iVu2vVW2TJagkwNeU0eC_TvMUoEK-PRtrLizW0KDtBibBP3XmZhuZ4b5ILRqowqI6v3iEuKcJTBzDQpsKYnxiVqoPWqcjpgT0mlu92JmlqFwi1Jqp4Xhipn1p0F2MTBP5_MJXyragFEdDGtEGuEIDgP_k_vtGlL-x_vFwtXVP0FpvJwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: شهید نصرالله، مقاومت را از یک گروه چریکی، به یک دکترین بازدارنده تبدیل کرد
🔹
شهید نصرالله تنها یک رهبر سیاسی-مذهبی نبود؛ او یک استراتژیست و فرمانده میدانی و جهادی بود که حزب‌الله لبنان را به نقطه‌ای رساند که معادلات امنیت اسرائیل را کاملا تغییر داد.
🔹
سید حسن نصرالله میان میدان و مردم، ایمان و سیاست و آرمان و عمل، پیوندی ناگسستنی برقرار و «میدان» را به ابزاری برای تأمین امنیت پایدار تبدیل کرد.
🔹
دشمن تصور می‌کرد با حذف فرمانده، مقاومت متوقف می‌شود؛ اما غافل بود از اینکه شهید نصرالله، ساختاری را پایه‌ریزی کرده که متکی به فرد نیست و امروز نیز با قدرت، بازدارندگی خود را حفظ کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/465050" target="_blank">📅 17:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465049">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvvlgqVIUgJ_KXkEygaBuctxZtBpqRAzgK-rcNUJEnLXacbbrDgstQ1Y8n6qA-g9-xlfBcBma9Yyxujd-GlcdHPN3Ba4BI3YXThigPXaBFh-oCdoZt4OKWGRvIBh1x5djrXePEgTBatEDFFPzUgXOQucJZ62ofYgz-VNat7So6ZdEOY9wEidu9DC-DirHxcj6snZlNEbbUda723FMBkOT_TYzLBnh6uq2zp6rMNbq3Ea0vPC9SBvc8_dO0CS4DvQ1hNbVJPLA70f-WxLr7tcP0UE8CZNiNez_7HWLot-_bUUQ2v9ROVlksOTDcrJXw8yH4k1WXSxbz1fQxCyilnuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور ویژهٔ فرمانده انتظامی کردستان برای رسیدگی به رفتار مأمور خاطی
🔹
درپی انتشار تصاویری از برخورد غیرحرفه‌ای و نامناسب یکی از کارکنان واحد گشت در سنندج، با دستور فرماندهٔ انتظامی کردستان، بررسی موضوع بلافاصله در دستور کار قرار گرفت.
🔹
مأمور مربوطه به ادارهٔ بازرسی پلیس احضار شده و تحقیقات درباره نحوه برخورد او در حال انجام است.
🔸
در بررسی‌های تکمیلی پلیس همچنین مشخص شده که رانندهٔ خودرو فاقد گواهینامه رانندگی بوده و شرایط او می‌توانسته برای خود و سرنشین خودرو خطرآفرین باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/465049" target="_blank">📅 17:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465048">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYOPOX7-8zbsIvVK2wy9wMCmoHLR_CcyD27ZyYx73CXax-aoZEqom0FWl6YPWCsRn4lJ_DyKhux2o-r4-dfBW_wpD7Itqfwm3XNbuVm1vPHXnGT7C0qwi3QQsVJ9i6kdadCB7IN91UA6la-XesQthu2djm2SGEM4oj3j3Dba0nWUsDwAI7pCbwGAjhDfuuYJKsh0Rq2nqW1Dv6fvXCN8FWGL0ekq3kA9L-UoGVXx6ndor_ixh1lBWwXhtjY9G-RDO5NR4QImhcm-zQcHBlHAu4wL576f_IC0xCwEKJTAXKlSMXyumaT_-zxAuR24yt8g9Hxu9zH4jhKbhB1HbpfhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای مقام اروپایی درباره عملیات‌های خرابکارانه روسیه علیه این قاره
🔹
«کایا کالاس» مسئول سیاست خارجی اتحادیه اروپا امروز مدعی شد که روسیه در حال برنامه‌ریزی اقدامات خرابکارانه بیشتر و حملات علیه دموکراسی در کشورهای اروپایی است.
🔹
کالاس طی نشست خبری بعد از جلسه وزیران دفاع کشورهای عضو اتحادیه اروپا در بروکسل، گفت: «ما شاهد هستیم که روسیه در صدد ایجاد تفرقه و ارعاب جوامع ما با هدف منصرف‌کردنمان از ارائه کمک به اوکراین است».
🔹
وی با بیان اینکه اروپا باید اقدامات بیشتر علیه روسیه را بررسی کند، اظهار داشت: «کشورهای زیادی خارج از اروپا می‌گویند، با روس‌ها صحبت کنید نتیجه‌ای حاصل خواهد شد. اما این مذاکرات نشان می‌دهد که روسیه واقعاً به هیچ وجه به صلح علاقه‌ای ندارد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/465048" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465047">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc78520c8d.mp4?token=O_TVc44p1b641bmA4FHPnobFlBLuVX_Nv9b_3u0dFERX4goX5PD8rCurr3YUDCFirPOA969mAyX8-KQ0JfV9cI7BS6edQq5vqI-0lMKvUpjDMQRvXREeVEXeUJoSvbVuHwIqibHLQ85phAOtXu76FqA2kohWOlmt2NB1H53P7E74yiCnSOZzm7sBIpKJHesEyar0cVdyoimT_tsWB_uxaMId9yD2tXOkxK74GQOA_cgL0JDmbsU1TeeN-qjVdUrlLjIilBlkJTcjS4u1kG1I-KwdfWEgU5K7-vYHHmE3-_g9okGQa5vug54xn4-7l2eq8cXi4IpKSCr_AO5g82ixxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc78520c8d.mp4?token=O_TVc44p1b641bmA4FHPnobFlBLuVX_Nv9b_3u0dFERX4goX5PD8rCurr3YUDCFirPOA969mAyX8-KQ0JfV9cI7BS6edQq5vqI-0lMKvUpjDMQRvXREeVEXeUJoSvbVuHwIqibHLQ85phAOtXu76FqA2kohWOlmt2NB1H53P7E74yiCnSOZzm7sBIpKJHesEyar0cVdyoimT_tsWB_uxaMId9yD2tXOkxK74GQOA_cgL0JDmbsU1TeeN-qjVdUrlLjIilBlkJTcjS4u1kG1I-KwdfWEgU5K7-vYHHmE3-_g9okGQa5vug54xn4-7l2eq8cXi4IpKSCr_AO5g82ixxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاری‌شدن سیلاب در روستا‌های فیروزکوه استان تهران
🔹
درپی بارش شدید باران و صدور هشدار زرد در فیروزکوه، عصر امروز سیلاب در روستا‌های طرود و گدوک این شهرستان جاری شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/465047" target="_blank">📅 17:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465046">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌همه بازداشت‌شدگان طرح بمب‌گذاری فرفورد، تبعه انگلیس هستند
🔹
پلیس انگلیس اعلام کرد که ۵ مردی که در ارتباط با طرح مشکوک بمب‌گذاری در نزدیکی پایگاه نیروی هوایی سلطنتی فرفورد بازداشت شدند، همگی اهل لندن هستند.
🔸
روز گذشته رسانه‌های انگلیس مدعی شدند پلیس این کشور…</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/465046" target="_blank">📅 17:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465045">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKEwPaYEaUP1nJWsu6WBh5BbtsKo-GinH4HsSBiRjfjrtxcpPst_rOPqI2Il-h1x9dzTss6MxB2rq-1_5Y-9CnW_51z3vuKAdr16vLr1fAhy_YNUnOIqsGXxjIp5Rove1WDbN6qUQxD45HXUuuCKqgOKPmxR2yvMdVIWHGcO6FLOoomm6CgWbKm0lor_yL7rQZ7eHD1pKII2rdf5svabrQ0AzyFe1N94gv7YkdvusArKdWv4RXRV2FNO2U3oDx6Me8Gfk3DHY3vZvr97AN2Xw1S_eGEjv0nuTdm87bAcMD2reSbq1L75OCFsVvOT7p_hBT7IDSSjCVFsUmT3KGR7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام اسامی برندگان نخستین روز قرعه كشی جشنواره جایزه محور «دیما»
🔹
نخستین روز قرعه کشی جشنواره جایزه محور «دیما» از بین کاربران فعال و احراز هویت شده این اپلیکیشن برگزار شد و برندگان خوش شانس روز نخست این دوره از قرعه کشی ها که به مدت ۴۵ روز ادامه خواهد داشت، مشخص شدند.
🔹
در روز اول این قرعه کشی ها، یک برنده جایزه ۵۰۰ میلیون ریالی، سه برنده جایزه ۳۰۰ میلیون ریالی، ۵ برنده جایزه ۱۰۰ میلیون ریالی و ۹۱ برنده جایزه ۱۰ میلیون ریالی به قید قرعه انتخاب شدند.
🔹
جشنواره دیما در سه بخش روزانه شامل جوایز نقدی از یک تا ۵۰ میلیون تومانی، هفتگی شامل ۱۲ دستگاه موتورسیکلت و نهایی شامل ۲ جایزه ۵ میلیارد تومانی برگزار می شود.
🔹
در قرعه کشی های هفتگی جشنواره دیما، ۱۲ دستگاه موتور سیکلت (هر هفته ۲ دستگاه موتور سیکلت) به قید قرعه به کاربران این اپلیکیشن تعلق خواهد گرفت.
🔹
در بخش قرعه کشی های روزانه هم، ۴۵۰۰ نفر برنده جایزه خواهند شد که شامل ۴۵ جایزه ۵۰۰ میلیون ریالی، ۱۳۵ جایزه ۳۰۰ میلیون ریالی، ۲۲۵ جایزه ۱۰۰ میلیون ریالی و ۴۰۹۵ جایزه ۱۰ میلیون ریالی است.
🔗
برای مشاهده اسامی برندگان
اینجا
را
کلیک کنید.
@mellatbankiran</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/465045" target="_blank">📅 17:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465044">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I25VfkFpetPlqhQyMAPG83txpBHI08MCzHQydPZ-lwDMBB8o5UqeiBmpq6BIepXyZrHbJtr6aNCvq8Dt4LvSk3xh4q2Ci3v2egeYIX2Fke_NQUf2DH65QmdccxkSf1S4UKD4LHdiBcvGWqi0OKQXkzSog1etpXuyaylk4oprpvILRfTXzPFFZ89QIdZzPK-0kUKJ_VW6cn6W-02MYCv2h2yth2PkryWBYSW9gotDleRQC34iOUld0CJmBWe00iJi_5-Mwhqs-z49DM7FgWqzk4nvKSqrw-2KvwhQnOpsAQOv2aJIRN1K59q2pdmDdOhvU2JicC-VGTRy64fU3rW0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💍
پرداخت بیش از 50 هزار میلیارد ریال وام ازدواج از سوی بانک شهر در نیمه نخست 1405
◀️
بانک شهر در شش‌ماهه نخست سال 1405، با تداوم رویکرد حمایتی خود در حوزه وام های تکلیفی، بیش از 15 هزار فقره وام ازدواج به ارزش 50 هزار میلیارد ریال به متقاضیان پرداخت کرده است؛ رقمی که از رشد 72 درصدی پرداخت، نسبت به مدت مشابه سال گذشته حکایت دارد.
◀️
به گزارش روابط عمومی بانک شهر، حمایت از جوانان، خانواده‌ها و اجرای سیاست‌های اعتباری در حوزه ازدواج، فرزندآوری و تأمین مسکن، طی سال‌های اخیر در زمره محورهای مهم فعالیت این بانک قرار داشته و آمارهای ثبت‌شده در نیمه نخست سال جاری نیز استمرار این رویکرد را نشان می‌دهد.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/465044" target="_blank">📅 17:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465043">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/465043" target="_blank">📅 17:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465042">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnLrNd2-h6sxwksM-jXjmx8pDvepHs_takoR8HXdOuRbneGgmhl82V3T0Zr1eiP-W6nuRhM8Ekz0jBf4XmT4c6rAm_Y9dmJUu7Y3f6QB2-PdotrHEpmdAeeWMzxRuvVfsZ6GAnhORlsRYKLjjGvEE7sIw5yjqytPCDzBe0qH4Z0Dn5aO0ksz0PNWSQLMh9Sl1GeVZvlEG_24xTutL7bO0JLGQhG2Vb7U7NiRicCM5tbdc_D_GlhTinMgobuos4gnicvKCzLEjm40rXubUqivc55yaBlP2BBB8Nuyl3npXR5KsR_erkJrvrxmk_puPigiHjMirHgpIEoATYNU1aCf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات کوچه‌‌بازاری اصلاح‌طلبان برای تحمیل نسخۀ تسلیم
🔹
زمانی‌که ترامپ تازه از برجام خارج شده بود، برخی از چهره‌ها و جریان‌های سیاسی دلایل بسیار ساده‌لوحانه‌ای را برای این عهدشکنی مسلم دولت آمریکا مطرح می‌کردند.
🔹
تیتر «موشک‌پرانی سپاه» در آن دوران، شاه‌بیت…</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/465042" target="_blank">📅 17:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-LclmrIZEI3aEype0ucltH0Q5N-7PCEmvNGp7xhUfdK5NHwNWow5-q9ZGJalN_UoXOpvnMSXjSb1HFLCnyfk9T27j4hVu9QiLIuVYSNf68hMhWm3aNKj6RNFlHyO4S-ILdAuTLwG0OJrEfA10ZY2aLKi8f65Wwd5OzNDx7nrevjjSSJkNvdSvliXAr-XQg8Ly-PTSTgsRbL87VDi_E9g9odLmEeo-PjdKiSHhgpFEGP6Pfk5eKcs6YwkwTRHmmU-GeISLbmVOePlKtftIsBjP63GtAmxZLrWwD8AeBrttmAEWe9k34zsrcHm1AUbcIuT_wPVP5jk5uID36qFOvv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUfPmx0er9bogNKxmGp37gUg3rH-Lv5PEPVua_2EXxsje3De1bxIcVL4ztaikS6HcxsGHtI3dyAfI-iTBu2m3rUZ47DUezexibQqZaiLTaaTFs-SKbCGYcI4fDYn1Zpt-RTPAR9qI3RwTYNLFX2UC7vpG5r18HlSYp_uRjbl-ex66JQcUjx8CQjSNOC0VPZaU4ivDwqBBeU548JiVuL7VVgdqtPLQD1sdlYvPph14_m_lI_-aBz-qaVv0a0Kk-Gpv49ecCi_WdTUnNc1DIdW5U3Mw_49GtGM2oroYiRPiBCOB54jIhadL9NL1r8Bb0RcP7L69gGVKxtcSdaa-Ruf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCjemiEIzBQlQJVVExrQ1V7fC-4SJhXVtVqjUXAVWXKv9hJjrQDUI01b8sb0mE-5TC08g45evDvCm-4TFilfTeEtpDRA255mDA9h8NnYUOjwFLWaDpze7puk1I0SKg1Z9UmwI8U8aneog-NKeLw5rLIIChAhxJfPNOy9jbUWFT96f5MSRKzTYROdVi2ukJWPD2o7JlcNcx3V7ULA3IDAyZpCGWKD5x9vltU-jeiOpUn1gyjHzXsBkydZkfEU5zgeVg9XVc7syLQdrDpfelp9CyNpfuaJLpFinIQm0CnTBTebKRAmfWKsZF7fBgiUFZR4cBYKTF5OElnbKBxEJBRxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsIsDs4hdsT4Erlo4pCE5HSjnmVEMHrpptG2bSwSAV5fi-19uD9ItLrUeRv0YWOK8SwPUkmN_4kkrtwJ4Unx5hoDeeM9ygaP6u-cs6uZAHe070L5qNLcQ6eZEtGhI8ZBTO9bmKYAS5ilYKtNHNME2bc_sDs8OvsKxPMz5AoSEJJo2tkCndPFB0qsrEHp524wdO03vVyNlBGuzeVt7p3zIdIAIECKMMmGGwRGtvU9rY44itQC39nIkBCd-FSaHmeS_Mc4rZaInP4hWOBsIpiDbvjdJu5INT-txptZl8Bjslao_8wgbBOGDAE7orERTH1jBXOKHPgf_3VGdXhVcpkBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYX7lvuGO0otQdroUkc0Z1ML4qKoHeVkDswxOG5xfBirb_YspUrhc8pTq82_Za-rDFnhlvziLNr-cKBwbFVapDezn28au1RQMhOdLMaUdOlv7ZtELnCOt10PZTxqcGSwRIeGJRxAoc1PiAhTfHlIv8BE3d2QHfhPbR6vwMgZlLSpUjYBHpe_3BU1iW1Nrg7SEVbE_AmUhR7lHXU-o9p8MSC949NMidRFNvJRHwZaxbd2NWZ42OCd2i0Tx0nO0PzHEYULyDZTSRiUZgkv2JSdL9i6HdFV1PxPCvwS6e3MfYMw_UPAmI6abTKlUnkOt9lI2CsxFfrXmrD9Hqur37zs-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-LclmrIZEI3aEype0ucltH0Q5N-7PCEmvNGp7xhUfdK5NHwNWow5-q9ZGJalN_UoXOpvnMSXjSb1HFLCnyfk9T27j4hVu9QiLIuVYSNf68hMhWm3aNKj6RNFlHyO4S-ILdAuTLwG0OJrEfA10ZY2aLKi8f65Wwd5OzNDx7nrevjjSSJkNvdSvliXAr-XQg8Ly-PTSTgsRbL87VDi_E9g9odLmEeo-PjdKiSHhgpFEGP6Pfk5eKcs6YwkwTRHmmU-GeISLbmVOePlKtftIsBjP63GtAmxZLrWwD8AeBrttmAEWe9k34zsrcHm1AUbcIuT_wPVP5jk5uID36qFOvv6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار سرلشکر صفوی با خانوادۀ سپهبد شهید رشید
🔹
سرلشکر سیدیحیی رحیم صفوی، دستیار و مشاور عالی فرماندهی معظم کل قوا، و حمیدرضا مقدم‌فر، مشاور فرمانده کل سپاه، به همراه اعضای دفتر حفظ‌و‌نشر آثار رهبر شهید انقلاب با حضور در منزل سردار سپهبد شهید غلامعلی رشید، ضمن ادای احترام به مقام شامخ این شهید والامقام، با خانواده ایشان دیدار و گفت‌وگو کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/465036" target="_blank">📅 16:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fc1499b84.mp4?token=ny-nYqaGQaHU9eyC8ool5ByjkSN2NuIjuMTFl2EOGnFevNObqZww3f5p9n1YUNex9uNG-F3TILPlP37p7U3N0Obqs6RloK2CdoUFAVjxcANgKqO53m4fKEJGqzkub937_UVlV7FfQCexNpl57mrZSaGt566yQqDTLA_d-X1eTL2asahaO7Sm8nLXA1dVPJTNjMsLvlHYiQ51cVBybiyuLhqjlB64n8ZYyLverpRDkNNt6C36OFUq0SKhoZ3CVRyXlFBTCmQ5OAMxE_h_tOMcKN2-UF34MQ8PxKYL-F5boGHwXIZEnSO8NZEhs87qYlhDtmzozktDHaM1G0b3HVEJ_G5LTtztTr1GHXlYDQEYpLNJCCfp4XxmX_se6MOlXKU7Lgm2zqVER8zTKzgt1AV4VirVLNsNmXt6uUF3IbZ_lMfTsBEafNo0CC-lqB387SiMwSLJvo2x4TtjPXTBrjU2UC3g5ke95AIEZh9JWLVfBw_P3rlOjTY3fNbhGZ1rTPEjfhp434gAg5YUi3-RaHBVOziEZzwdh9Pq6KN0PmzT9JAltJlh4Xr6dZS-jp9gArYyO71gH8kGWIsT5kDRMiacfU_1oPxbi_tgwMeJjidQZDF9ZN_DNxjD8b7w5T7P8FFXePAdw4ocVFpEKj_C98R7qrxLa9wjAgtVikeJpeqeHzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fc1499b84.mp4?token=ny-nYqaGQaHU9eyC8ool5ByjkSN2NuIjuMTFl2EOGnFevNObqZww3f5p9n1YUNex9uNG-F3TILPlP37p7U3N0Obqs6RloK2CdoUFAVjxcANgKqO53m4fKEJGqzkub937_UVlV7FfQCexNpl57mrZSaGt566yQqDTLA_d-X1eTL2asahaO7Sm8nLXA1dVPJTNjMsLvlHYiQ51cVBybiyuLhqjlB64n8ZYyLverpRDkNNt6C36OFUq0SKhoZ3CVRyXlFBTCmQ5OAMxE_h_tOMcKN2-UF34MQ8PxKYL-F5boGHwXIZEnSO8NZEhs87qYlhDtmzozktDHaM1G0b3HVEJ_G5LTtztTr1GHXlYDQEYpLNJCCfp4XxmX_se6MOlXKU7Lgm2zqVER8zTKzgt1AV4VirVLNsNmXt6uUF3IbZ_lMfTsBEafNo0CC-lqB387SiMwSLJvo2x4TtjPXTBrjU2UC3g5ke95AIEZh9JWLVfBw_P3rlOjTY3fNbhGZ1rTPEjfhp434gAg5YUi3-RaHBVOziEZzwdh9Pq6KN0PmzT9JAltJlh4Xr6dZS-jp9gArYyO71gH8kGWIsT5kDRMiacfU_1oPxbi_tgwMeJjidQZDF9ZN_DNxjD8b7w5T7P8FFXePAdw4ocVFpEKj_C98R7qrxLa9wjAgtVikeJpeqeHzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
من هم می‌خواهم پاسدار شوم
🔹
آرزوی فرزند شهید جنگ ۱۲ روزه در نخستین روز بازگشایی مدارس
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/465035" target="_blank">📅 16:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz5SmoNtXKlhEAYom0FVkWPUD40JEcI-L_1dq0wgMkSUyHpHzUrp2iMlyZ5g4aTO0ayNwxaR4nLDV-G5ZcJh725KDF3ZGBAL34hUfVDnEV0Ux17nJPBSbTYNnY2hlmKssw0zcjrPFhA5OL-zeAMxMjbVUIwtwx2hXx7SX3FD2ZRBjR3Z-Np0JS68OvUjruBrB5HV_13v8sX0FvoYVD5D6_1J4Hi33iZ1UM1slix8a0qxLUrDI0TstI_9mZCHsW9mwKdxahqPkzKP2SlMo7IAM6jNtCpvqngZAuAHhWoMi788SgOUCwpuMEd5YVs9rY-gTfPE32X_jLsTX4wc35latQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتهام‌زنی علیه ایران پس‌از حادثه در محل استقرار بمب‌افکن‌های آمریکایی
🔹
رسانه‌های انگلیسی مدعی شدند که پلیس انگلیس در حال بررسی ارتباط ادعایی ایران با یک طرح مشکوک به بمب‌گذاری در پایگاهی است که هواپیماهای بمب‌افکن آمریکایی در آن مستقر هستند.
🔹
رسانه‌های انگلیسی…</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/465034" target="_blank">📅 16:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTAp4CL_9ybECp9Uqd3471Lt6IViPJ7vKQWx9eJ9vZlsnBCgqlphiQ7CtPeALhA54CwRdJNPz38G6JAUbdIZqSY32s01mYtDz7MdTk10ddDgKYUsal2xC8eyBdHBRcKzMCIGeTjEYOYqeodEy9586VHPvsLt-6g2P1sDERf8ZUebnuWgL5DytWZyFjQ105MC4f93OUbQbikhQQ3iKM8Ma2b-vN89SLOT6ap8PxhSmme3dYLv4J2t0OT6WePJnB-uYmVFQgC1iT9AYI0OXjoKFccDPwSRj-WR_gXSgtDX4gnW7-2YL6LEp7qjKLQ0MSCI6-bno7N528pWoW7uvkzk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دارایی راهبردی هرمز، نفت نیست
🔹
تنگۀ هرمز فقط مسیر عبور نفت و انرژی نیست؛ کابل‌های زیردریایی ارتباطی و انتقال داده نیز از این محدوده عبور و بخشی از ارتباطات دیجیتال منطقه و جهان را برقرار می‌کنند.
🔹
تجربه کشورهایی مانند مصر، ترکیه، اندونزی و سنگاپور نشان می‌دهد کشورهای ساحلی می‌توانند از این زیرساخت، علاوه بر اهمیت ارتباطی، درآمد، فناوری و ظرفیت‌های حاکمیتی ایجاد کنند.
🔹
در ترکیه، درآمد حاصل از کابل‌های عبوری از تنگه‌های بسفر و داردانل حدود ۵۰ میلیون دلار در سال برآورد شده است.
🔹
در سنگاپور نیز تعامل با صاحبان کابل‌ها صرفاً مالی نیست و انتقال فناوری و همکاری فناورانه مورد توجه قرار گرفته است.
🖼
اما کشورهای دیگر چگونه از موقعیت جغرافیایی خود در اقتصاد داده درآمد کسب می‌کنند؟
🔗
پاسخ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/465033" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35f1bf6a8b.mp4?token=Mq3Zb7asQIkawqcpxjRhNI9sBwlYAY-g_7y4AEDz1DWPQcNR3H7a0wW-Vhxj53OswQtDu39TGA0lfdGhCFw4r9jA22q7tBdGF05hpI6P85CUQa9gnVj6y6hzJhtJusG8dq0z3z2MGPEt8dEXIo51FvhvvjuVkPNcgTsOLWBtty8piwMdfycaY3rDTmMSj55LYCRvF1YVhpCwK3bdIGf1NQBtrPdVDMmvbcS-yVaoPvsR4QqflBBhNBixlYCqCrtIZGPBiyCXXzQIpN5SPUZrZWTE0FeL5BocPzDqUi-VSY6a_m5ju0-Pg3gADZanp98kX7BUDSNKeMtTx7qbo_Tn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35f1bf6a8b.mp4?token=Mq3Zb7asQIkawqcpxjRhNI9sBwlYAY-g_7y4AEDz1DWPQcNR3H7a0wW-Vhxj53OswQtDu39TGA0lfdGhCFw4r9jA22q7tBdGF05hpI6P85CUQa9gnVj6y6hzJhtJusG8dq0z3z2MGPEt8dEXIo51FvhvvjuVkPNcgTsOLWBtty8piwMdfycaY3rDTmMSj55LYCRvF1YVhpCwK3bdIGf1NQBtrPdVDMmvbcS-yVaoPvsR4QqflBBhNBixlYCqCrtIZGPBiyCXXzQIpN5SPUZrZWTE0FeL5BocPzDqUi-VSY6a_m5ju0-Pg3gADZanp98kX7BUDSNKeMtTx7qbo_Tn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوشاد حریف نفر اول دنیا نشد
🔹
نوشاد عالمیان در نیمه‌نهایی تنیس روی میز بازی‌های آسیایی ناگویا مقابل وانگ چوکین نفر اول رنکینگ جهانی از چین قرار گرفت و ۴ بر ۱ بازی را واگذار کرد و به مدال برنز بسنده کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/465032" target="_blank">📅 16:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465030">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌ ۴ دلیلی که عراق از تعلیق پروازهای ایران متضرر می‌شود
🔹
در پی فشارهای ناشی از تحریم‌های جدید آمریکا علیه صنعت هوانوردی ایران، پروازهای میان ایران و عراق تعلیق شده. دولت عراق درحال مذاکره با آمریکا برای دریافت معافیت و بازگشایی بخشی از مسیرهاست.
🔹
مهم‌ترین…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/465030" target="_blank">📅 16:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn2C35YGAhx9UQIeJU_YNGLveJyg9-YF-x0umy4lzmQgwD4csboyF3_LYuO7xBes3aOyn8IYbN18nB34udYB16Gv-gin4h9s2D2hcTpFIL18uZwTe_VhLQzCOdj9V5E-0qX-H6WdujjQ5dQ3s5aG9eUnbN0SF6Yhv-zQ_MA030aktYPqJDgZIiofWuOi78UzBF_sc2yoaRKp1LwJ7_ZDIj4VxbUZPsg5B8Ul7dmZfs6iHdlxlJjkcmr5LXbhB0ID2R-5kZrfsh8dk61t8zEQpWkc-x9eHdWgRMFP2fV3yXPkav_pY80VM7R3wA0ypjJ_7fTQvuyDm4n_4cVjAyEgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم صهیونیستی خبرنگار پرس ‌تی‎وی را ربود
🔹
پرس ‌تی‌وی: نیروهای نظامی رژیم صهیونیستی خبرنگار نقا حامد را در یک ایست بازرسی نزدیک به بیت‌لحم در قدس اشغالی ربودند. @Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/465028" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4540643c1.mp4?token=qLnWGBzXp1Xmj5h_kBhQjj3rrhL7RrGO4kULaW93Z5DckDtXyWYX4FySsUIPDUy5niq7XNFQubWJrKFosvyMencZlyXE-IllGGdRbGnHjEB8xCXQH68onwCqq44bbzZ5HosfcWVtdiFo_-aqkMwDnA6_MU4g9kWiMuZiWEXGRpG87s-G4g483Tq1SZNHf0-ZqyP0zl57doDLR4tiBuc6tw2wdd4htlsTHXr5jWzMn3Dei9Z9KFOdLKV22YJgPXS68cqFuArKrWq6Bz9WoLqIKl4i8LAc3say9iAshs0dD2QC_QiQ4I5pKEK4EfX5lRPZ5p1ldrU5ZPTftxzfMN4Q3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4540643c1.mp4?token=qLnWGBzXp1Xmj5h_kBhQjj3rrhL7RrGO4kULaW93Z5DckDtXyWYX4FySsUIPDUy5niq7XNFQubWJrKFosvyMencZlyXE-IllGGdRbGnHjEB8xCXQH68onwCqq44bbzZ5HosfcWVtdiFo_-aqkMwDnA6_MU4g9kWiMuZiWEXGRpG87s-G4g483Tq1SZNHf0-ZqyP0zl57doDLR4tiBuc6tw2wdd4htlsTHXr5jWzMn3Dei9Z9KFOdLKV22YJgPXS68cqFuArKrWq6Bz9WoLqIKl4i8LAc3say9iAshs0dD2QC_QiQ4I5pKEK4EfX5lRPZ5p1ldrU5ZPTftxzfMN4Q3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوشاد حریف نفر اول دنیا نشد
🔹
نوشاد عالمیان در نیمه‌نهایی تنیس روی میز بازی‌های آسیایی ناگویا مقابل وانگ چوکین نفر اول رنکینگ جهانی از چین قرار گرفت و ۴ بر ۱ بازی را واگذار کرد و به مدال برنز بسنده کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/465027" target="_blank">📅 15:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465026">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8YquxORgTQ635xwJnFqm4W6Je384rS9lJdVQb2rXvNlm3wQsqan1TBYMFJ17NblZZoCE7981Q73cQtxwwdlWwuYHkJV1gXzNtzzWi1idLoIXjQi5wyG5TPFf1CeqT-Vk8ZgYOBC0zZH2zh-KoqU947TujPEwTdYP6pVJoIMvIUOr_IO_9mDuZGuW8XHCosdbKNS3-1oltojurBBomu56ey-ssDcPnhopxOydSQxYFBTEmyjCyM-njH0nLdhlNRd53Z_YVQL3yyGQbyjt0-_ITCEhzyjH9FU3cfztvGqA26CuX8BGn5W3g5n4cRVlXnIMl-5IRI0be0eJBM6af_BlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار رادان: باید برای بدترین سناریوی دشمن آمادگی داشته باشیم
🔹
باید در برابر بدترین سناریوی دشمن، پیش‌بینی و مقابله داشته باشیم و ساختارهای نظامی و دفاعی را متناسب با شرایط ترمیم کنیم. سناریوهای دشمن باید پیش‌بینی شود و اقدامات پیشگیرانه نیز انجام گیرد.
🔹
دستگاه محاسباتی دشمن گاهی به خطا می‌رود و باید این مسئله را به‌درستی شناخت. دشمن در جنگ‌های اخیر تصور می‌کرد با ضربه‌زدن به فرماندهان و زیرساخت‌ها می‌تواند ساختار کشور را دچار اختلال کند، اما در عمل مشاهده شد که با وجود شهادت فرماندهان، ساختار و توان دفاعی کشور به مسیر خود ادامه داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/465026" target="_blank">📅 15:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465025">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faIDgHN-QSzQ1eyOACXPQQhzPaGsEMtHrIHghE2yT6vgL3DSJxH8jT3mTnsX8Xag2SYa81ORFAU9j_ljrRTTFeJI_6BVIvf1Oe6ys71l8ejIAGqUbj6tAM3pGQITrMBA8MobuypbXGarmQfmS1mBDIvZIuvWnZgpX4QP4JXCnye6PquSgdppIRYipw6AlwolNvf_HCm7viPnqdKIz1T7DFbgr8TH3RWeSVXn2WedmZsVMExwqLK-oZON923WokQsPJFUP7c60RXgDHToXhXsIryCt6EZUr3C51Ri5KEcXmuwpSM8yhGkg3lqTa9_aIAlMp1nlVdS47vMZHiI5qDRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور عارف برای تدوین بستۀ جامع تأمین منابع یارانه‌ها
🔹
در نشست تیم اقتصادی دولت با موضوع هدفمندی یارانه‌ها، راهکارهای تأمین منابع مورد نیاز برای اجرای هدفمندی یارانه‌ها برای بیش از ۷۵ میلیون نفر از شهروندان در شش ماه دوم سال بررسی شد.
🔹
معاون اول رئیس‌جمهور: تأمین معیشت مردم همچنان یکی از اولویت‌های دولت است. ظرف یک هفته بستۀ جامعی برای تعیین دقیق منابع و مصارف هدفمندی یارانه‌ها تدوین شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/465025" target="_blank">📅 15:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465024">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئیس کمیسیون شوراهای مجلس: تصمیم‌گیری دربارۀ تاریخ برگزاری انتخابات شوراها به هفتۀ آینده موکول شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/465024" target="_blank">📅 15:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465023">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d08816ce.mp4?token=i35UuyHbQqjYxiI5bscXFP8A7ijsL4ZpE-OgNuU04mO3VwGlhxrqN9vtP6ClpJ9GdYdqHNfh41AOH3ma3-EnBkZ06vX6aLOvb_WLGSf04J_QKz9X-_kdjvICmsS3fgtwiLthweRaVDXNQQHo7oXXfrqZCfNH6GOCAm3Xdkw-s5-QICo11XS49Z8YoJfqYGxCY7lh-6grJsjYjd9FIlyBLnab_KxJ1uGsIYrWjtJp3L61GH5rMzJnKErUqSf4YQSMxYrZNhjwAS_olFEzaIT0DaYkQcbO6LUXBohXeHYcPxM7tu2USKG3de6Sca3il74APGDnQ5p87ZrYr-z0QPcUfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d08816ce.mp4?token=i35UuyHbQqjYxiI5bscXFP8A7ijsL4ZpE-OgNuU04mO3VwGlhxrqN9vtP6ClpJ9GdYdqHNfh41AOH3ma3-EnBkZ06vX6aLOvb_WLGSf04J_QKz9X-_kdjvICmsS3fgtwiLthweRaVDXNQQHo7oXXfrqZCfNH6GOCAm3Xdkw-s5-QICo11XS49Z8YoJfqYGxCY7lh-6grJsjYjd9FIlyBLnab_KxJ1uGsIYrWjtJp3L61GH5rMzJnKErUqSf4YQSMxYrZNhjwAS_olFEzaIT0DaYkQcbO6LUXBohXeHYcPxM7tu2USKG3de6Sca3il74APGDnQ5p87ZrYr-z0QPcUfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: هرچند در شرایط جنگی قرار داریم اما نباید از مبارزه با مفاسد اقتصادی غفلت کنیم
🔹
پیگیری مسائل شرکت‌های دولتی که آغاز شده نباید رها شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/465023" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465021">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">پیامد دوقطبی‌سازی‌های موهوم برای ایران چیست؟
🔹
تقلیل مسائل پیچیدۀ کشور به دوگانه‌هایی مانند «صلح‌طلب و جنگ‌طلب» یا «مذاکره و جنگ»، می‌تواند جامعه را از گفت‌وگوی واقعی درباره منافع ملی، هزینه‌ها و گزینه‌های سیاست خارجی دور کند.
🔹
منتقدان این رویکرد معتقدند مذاکره باید ابزار سیاست خارجی باشد، نه تنها راه‌حل؛ همان‌طور که قدرت دفاعی و بازدارندگی نیز نباید معادل «جنگ‌طلبی» تلقی شود.
🔹
تجربۀ برجام و خروج آمریکا از آن، بحث دربارۀ تضمین اجرای توافق، امتیاز متقابل و حفظ قدرت چانه‌زنی را پررنگ کرده است. از این منظر، مسئله اصلی نه «مذاکره یا جنگ»، بلکه حفظ قدرت انتخاب و تأمین منافع ملی است.
🔹
دوقطبی‌سازی‌های کاذب، به‌جای تقویت انسجام ملی، می‌تواند شکاف‌های اجتماعی را عمیق‌تر کند؛ در حالی که در برابر تهدید خارجی، انسجام داخلی، توان دفاعی، قدرت اقتصادی و دیپلماسی فعال می‌توانند همزمان در خدمت منافع ملی قرار گیرند.
🔹
تحلیلگران معتقدند مذاکره زمانی می‌تواند به تأمین منافع ملی کمک کند که از موضع انتخاب انجام شود، نه از سر اجبار و نیاز. تجربه توافق‌های گذشته نیز نشان داده که اصل توافق، بدون ضمانت اجرا و قدرت چانه‌زنی، لزوماً به نتیجه پایدار منجر نمی‌شود.
🔹
وقتی افراد و جریان‌ها با برچسب‌هایی مانند «جنگ‌طلب» یا «صلح‌طلب» دسته‌بندی می‌شوند، امکان گفت‌وگوی منطقی درباره جزئیات کاهش می‌یابد.
🔹
از نگاه منتقدان دوقطبی‌سازی، جامعه‌ای که بتواند درباره اختلافات خود گفت‌وگو کند و در عین حال بر منافع مشترک ملی تأکید داشته باشد، ظرفیت بیشتری برای مدیریت بحران‌های خارجی خواهد داشت.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465021" target="_blank">📅 15:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465020">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌ رهبر انقلاب: براساس محاسبات الهی، ایران قدرت اول جهان است
🔹
آن روزهایی که آنان دوست دارند کشور ما را به آن برگردانند، روزهایی بود پر از عقب‌ماندگی، ذلت و خواری؛ وابستگی و بدنامی ایران در جهان اسلام؛ و این روزهایی که در آن هستیم پر است از پیشرفت، عزّت، استقلال…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465020" target="_blank">📅 15:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465019">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام رهبر انقلاب.pdf</div>
  <div class="tg-doc-extra">240.8 KB</div>
</div>
<a href="https://t.me/farsna/465019" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‌ رهبر انقلاب: کشورمان اینک به روزهایی رسیده که سلطه‌گران متجاوز در مقابل حملات رزمندگان اسلام، دست التماس به تَرک جنگ برمی‌دارند
🔹
از دل آتش جنگ [تحمیلی اول] که به‌دست حزب ضدّ مردمی بعث و با توهّم جنگی چند روزه و به دست آوردن پیروزی‌ای کم‌زحمت افروخته شده…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465019" target="_blank">📅 14:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465018">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
آژیرهای هشدار و انفجار در جنوب عربستان
🔹
سازمان دفاع مدنی عربستان از به‌صدادرآمدن آژیرهای هشدار در شهر نجران و جازان خبر داد.
🔹
منابع عربی هم از شنیده‌شدن صدای انفجار در این ۲ شهر در پی شلیک موشک از یمن خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465018" target="_blank">📅 14:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465017">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1556dce9.mp4?token=PqXS-1SyKEGxKuwGv5cHiiS3tHsyBasZyjbg9E0MXpo8P62YJ1Gb2hna1aid4jeH_L9BIRA0_tUAWXwy7Iys1qRYoC4C-7MVt4ZG4uYmXT4sU-M8JLDh0nbshtxUe8y-VXmiOiOkQ42ANkp78ufe-ROXGvAVwCBXTexvFjPWs6FWddXoBckImiQ6TBdbQN94ng8C9LbxNa3kMXlQAINYri8lT5X3oxeaOyMYAHHKhk-_TsBLVj8LATRcsQ1SfcYJJ6wDU18QtXhnvuhVCikJG1B6_4DxGDTGXXb4eA4uUIiNtG_OgaGE1S8YneHsOV4e-Esll6poJ7fy0HvqGiwGOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1556dce9.mp4?token=PqXS-1SyKEGxKuwGv5cHiiS3tHsyBasZyjbg9E0MXpo8P62YJ1Gb2hna1aid4jeH_L9BIRA0_tUAWXwy7Iys1qRYoC4C-7MVt4ZG4uYmXT4sU-M8JLDh0nbshtxUe8y-VXmiOiOkQ42ANkp78ufe-ROXGvAVwCBXTexvFjPWs6FWddXoBckImiQ6TBdbQN94ng8C9LbxNa3kMXlQAINYri8lT5X3oxeaOyMYAHHKhk-_TsBLVj8LATRcsQ1SfcYJJ6wDU18QtXhnvuhVCikJG1B6_4DxGDTGXXb4eA4uUIiNtG_OgaGE1S8YneHsOV4e-Esll6poJ7fy0HvqGiwGOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کار: شناور تجاری هوتن ۱ امروز به آب انداخته می‌شود
🔹
ساخت این کشتی ۲۰ ماه طول کشیده که ۶ ماه آن پس‌از شروع جنگ تحمیلی سوم بوده.
🔹
تجهیزات شناور داخلی است که توسط کارشناسان کشتی‌سازی اروندان و کشتیرانی جمهوری اسلامی طراحی شده.
🔹
این کشتی قادر است انواع مایعات را به کشتی‌های دیگر تحویل بدهد و از تکنولوژی به‌روزی برخوردار است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465017" target="_blank">📅 14:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465016">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMbrcWCvn_BiTdEcXgUP6R9pzX-bGVV-XQGVf0yvFt4uUJAKjkjNYlkjKRLPnFKU6BMmQBaQNv_eNyYvwYtZ0ZxuJjfn0Digi4VAbocZkExUfsXRd9h4HRsK9L-UZJ1KMmaLt09evZCuXLI01zaACRW0aNDUr0rHnQY98EOwqr0-f9KO0FJ50KbvVtdQEOoPGOfyFnaiGe9OStiYFx4zslI2rUkOq6jH6lRpAf0nL8rmq9pM6THgnJzQEcZ9xo-AIrdvP6PVH-KkQqT8BvohgdGnrNDZDoQ8ZAi2uCtPTnNJEEwlh28SSjvIhwDb5YnOBJzREMofS1N1W6I8vbzlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاکری: از امروز تا انتخابات آمریکا باید سطح تنش را بالا برد
🔹
مجید شاکری، مشاور قالیباف: تا زمان انتخابات میان دوره‌ای آمریکا یک گلدن تایم ۳۶ روزه باقی مانده است و جمهوری اسلامی باید سطح تنش را در این ۳۶ روز یا حفظ کند یا بالاتر ببرد.
🔹
تاکید می‌کنم که این افزایش تنش باید پیش از انتخابات اتفاق بیفتد و نباید این برداشت را داشته باشیم که تنش را تنها در نزدیکی انتخابات باید بالا برد، بلکه این اقدام باید از الان شروع شود.
🔹
استفاده از ابزار مذاکره به عنوان اقدامی در چهارچوب معامله با آمریکا و کاهش تنش صرفا به نفع شخص ترامپ خواهد بود.
🔹
یک ضرب‌الاجل مهم در چارچوب جنگ ایران و آمریکا، انتخابات میان دوره‌ای است و هر گونه فعالیت مذاکراتی که از مسیر کاهش فشار اقتصادی به آمریکا به نفع دشمن است.
🔹
این ۳۶ روز، از همه نظر چه برای جمهوری اسلامی و چه برای ایالات متحده یکی از حساس‌ترین برهه‌های جنگ خواهد بود.
🔹
احتمال دارد دشمن با استفاده از عوامل داخلی بازارهای داخلی را نیز ملتهب‌تر کند؛ صحبت‌های وزیر خزانه‌داری آمریکا مبنی بر فروپاشی اقتصاد ایران طی ۲ هفتۀ آینده نیز تأییدی بر این نظریه است و باید برای این مسئله برنامه داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465016" target="_blank">📅 14:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465015">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌ رهبر انقلاب: آن ققنوسی که از خرمن آتش جنگ تحمیلی اوّل برآمد، اینک در اثر فشارهای دشمن و به‌خصوص دو جنگ تحمیلی اخیر، آن‌چنان بزرگ شده است که سایۀ پروازش بر سرزمین‌های دشمن هم افتاده است. @Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/465015" target="_blank">📅 14:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0ef47123.mp4?token=qo1pfxrleNpz2i9E_Co96gRTL0vcCMsTz8e4VSg5oNwpyaROJZAXP5A99R1LdbsXnUK46H1XvfuutRN-SVs9lyH32o7KPmCyYvZD2ia56UhWpLM8P5GpfU2cZfZue1DSJe_Pgs0dnOhykQjeiM0dvIXNNUnnNnf90ssL4dMeeOtrTlxfjZ3pzU5yPelfT87znn6mPfCRBs0D-6Qeev8NCj5hlFVe3Vz0wTFVgeo3acAjkf5qtM9nVAl4s3MW-4ag7tO0N2gAbxn0sKaBaSliCUxl_9TfDOSC4W2lbkDOdjDW0ZoCeqEd1qSks0u2aeLh5SSJW_TfHWp6RsCysS1cmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0ef47123.mp4?token=qo1pfxrleNpz2i9E_Co96gRTL0vcCMsTz8e4VSg5oNwpyaROJZAXP5A99R1LdbsXnUK46H1XvfuutRN-SVs9lyH32o7KPmCyYvZD2ia56UhWpLM8P5GpfU2cZfZue1DSJe_Pgs0dnOhykQjeiM0dvIXNNUnnNnf90ssL4dMeeOtrTlxfjZ3pzU5yPelfT87znn6mPfCRBs0D-6Qeev8NCj5hlFVe3Vz0wTFVgeo3acAjkf5qtM9nVAl4s3MW-4ag7tO0N2gAbxn0sKaBaSliCUxl_9TfDOSC4W2lbkDOdjDW0ZoCeqEd1qSks0u2aeLh5SSJW_TfHWp6RsCysS1cmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنبش مسلحانۀ «حرکت یحیی» اعلام موجودیت کرد
🔹
یک جنبش مسلحانه با عنوان «حرکت یحیی» که نام خود را برگرفته از نام شهید یحیی سنوار، از رهبران حماس، عنوان کرده، با انتشار بیانیه‌ای اعلام موجودیت کرد و از هواداران خود در سراسر جهان خواست به این جنبش بپیوندند.
🔹
این گروه در بیانیۀ اعلام موجودیت خود، با اشاره به جنایت آمریکا و رژیم صهیونیستی علیه مردم فلسطین و دیگر ملت‌ها و با اشاره به حملات اخیر علیه ایران، وعدۀ «انتقام» داده است.
🔹
در کانال اطلاع‌رسانی منتسب به این جنبش آمده: «ای جنایتکاران، ما نه در سرزمین خودمان بلکه در سرزمین خودتان و درِ خانه‌هایتان به‌سراغ شما خواهیم آمد.»
🔹
این گروه همچنین اعلام کرده فهرستی از افراد موردنظر خود را تهیه و منتشر خواهد کرد و گفته شده از افرادی که قصد انجام عملیات یا ارائه اطلاعات درباره عوامل جنایات را دارند، حمایت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/465014" target="_blank">📅 14:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465013">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌ رهبر انقلاب: در یک کلام؛ ایران به دورانی که دشمن آرزویش را دارد بازنخواهد گشت
🔹
این مقایسه بین روزهای سابق و روزهای حال باز هم قابل بسط و توضیح است، ولی در یک کلام، بنده به‌عنوان خادم مردم عزیز ایران اعلام می‌کنم که آن روزهای سابق که دشمن ما آرزوی بازگشت…</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/465013" target="_blank">📅 14:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465011">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌ رهبر انقلاب: در یک کلام؛ ایران به دورانی که دشمن آرزویش را دارد بازنخواهد گشت
🔹
این مقایسه بین روزهای سابق و روزهای حال باز هم قابل بسط و توضیح است، ولی در یک کلام، بنده به‌عنوان خادم مردم عزیز ایران اعلام می‌کنم که آن روزهای سابق که دشمن ما آرزوی بازگشت…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465011" target="_blank">📅 14:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465010">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌ رهبر انقلاب: براساس محاسبات الهی، ایران قدرت اول جهان است
🔹
آن روزهایی که آنان دوست دارند کشور ما را به آن برگردانند، روزهایی بود پر از عقب‌ماندگی، ذلت و خواری؛ وابستگی و بدنامی ایران در جهان اسلام؛ و این روزهایی که در آن هستیم پر است از پیشرفت، عزّت، استقلال…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/465010" target="_blank">📅 14:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465009">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlORaViT_LUqiBfi7SVjx6D8a4tpCKqV2aYt_Bmo_5sszqIEQBK9-4YgI9P1lAL_VJgEDlwX3Gh4MQdGcuB4tfxTFUUK19-AXNT-Qu8B2BPJV1kQVZXhw-wypFmOmFFA4BLuPfgRHjh-UDZe1Ydqcc17X1J7_ouj_OB3gi5CNcUpCnz02kNkMKrMiykJFZEQVOR5SYHSlP4ky_FzZzcHMQHTioIq8c0HXZBkyXv9vtyzqKfucraWb95zDR4u8-mYUrVv-tMZPt5KZv6jZcHx0WpmDcYRhGmkFC7wIf6bBHFdWu3b1lVJX9yR1j7uTySlNVKgChv3hU6F1lTXGSFoNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خبری سخنگوی سپاه با خبرنگاران خارجی دربارۀ نامۀ مهم سپاه خطاب به مردم آمریکا فردا در تهران برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/465009" target="_blank">📅 14:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465007">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌ رهبر انقلاب: این روزهای لبنان، روزهایی ذلّت‌آفرین برای چشم‌دوختگان به وعده‌های دروغین سلطه‌گران است
🔹
این روزهای لبنان در پیشگاه تاریخ و بلکه از همین حال، روزهایی برجسته و پرافتخار برای ایشان و همۀ مجاهدان مقاومت، و روزهایی ذلّت‌آفرین و نهایتاً سرافکنده‌کننده…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/465007" target="_blank">📅 14:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465004">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌ رهبر انقلاب: از زمان انبیا کسی به بزرگی شهید نصرالله در سرزمین شامات سر بلند نکرده بود
🔹
در این مجال بسیار به‌جاست که به‌مناسبت دومین سالگرد شهادت امیر قهرمان عرب و نماد بزرگ جبههٔ مقاومت، شهید عالی‌قدر جناب سیدحسن نصرالله قدّس‌الله‌نفسه‌الزّکیّه، یادی از…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/465004" target="_blank">📅 14:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465003">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌ رهبر انقلاب: انقلاب اسلامی روزهای تیره سلطه مستکبرین را به روزهای پرنورِ جمهوری اسلامی تبدیل کرد
🔹
آغازین روزهای ماه مهر، یادآور ایّام الله و پدیده عظیم و ماندگار دفاع هشت ساله جانانه ملّت ایران در جنگ تحمیلی اوّل است.  در آن روزها تابش گرم خورشید انقلاب…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/465003" target="_blank">📅 14:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465002">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تا ساعتی دیگر پیام رهبر معظم انقلاب به‌مناسبت هفته دفاع مقدس و سالگرد شهادت شهید سیدحسن نصرالله‌ منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465002" target="_blank">📅 14:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq9_WadwrQfIiQcNd9gghE9OGj1vOJ3Bo15BVVQnXT37oPlc-dPHkfdWx8pxWL-RwlJ0KjFm1BK2Gocz0Z4-KY0iDQYqiW3Koxj6O9U6MtiCYgPDlgKB98g9-61slJoqf01SVZ-vo3UM0-e-vNuns_6O_d1EkHbiXHHFPUESB3jFhczP4REbZpEzAI9g7zQ6cz9hd7B8RUYFvdVHRGuP9iq4ERayeFkaoEZH1r9IJqlzCSydnLk4BfoKQ7y49OQXdHhTK4mosj-uuSMABc6xltXuf4pV1S2sro72TafT60Q2aOGGArmHFVG018HNA3jCUb8Hvh3ta1d4MMxtsBFfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیاده‌نظام بسنت، کف بازار دلار ایران
🔹
درحالی‌که نرخ دلار در بازار غیررسمی حدود ۲۳۳ هزار تومان بود، امروز قیمت دلار در کانال‌های غیررسمی به محدوده ۲۴۲ هزار تومان رسید.
🔹
این افزایش قیمت یک روز پس از تهدید اقتصادی وزیر خزانه‌داری آمریکا رخ داده؛ همزمان، فعالیت کانال‌های غیررسمی ارزی و انتشار سیگنال‌های افزایشی در بازار تشدید شده است.
🔹
بخش قابل‌توجهی از این کانال‌های تلگرامی از خارج از کشور هدایت می‌شوند؛ به‌عنوان نمونه، قطعی برق هرات در مقطعی باعث از کار افتادن برخی از این کانال‌ها شده بود.
🔹
همزمان با خط‌دهی کانال‌های تلگرام از خارج ، دلالان نیز وارد بازار شده و از راه افزایش معاملات و تقاضای هیجانی، بازار را ملتهب می‌کنند؛ التهاب بازار به افزایش تقاضا ختم شده و چرخۀ افزایش قیمت دلار تقویت می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465000" target="_blank">📅 13:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiaK-GS0UxbdH0rR__TNshjblgeJplUOB65dw-g8m7P4eArif7R-Nc1_M0La8FhktrYauOVmS_J_9NnFbqyasrG-DHRhdrVeGT9TNRlrlYxgkXFpenW84M7jooL_EXegfrSLd0EqRWS9Jk_MlNFla5EtLPkeavHCRnWOEUalXoBW94ejsvcbygqwpaT_P3xNRHuq46dBvZFCXK1kPeBgdqgEbkMWQgnWa0iKsHBjKBdfwK6_3m-DOgs-XCy6bHa1KDcLd9Yhs4khbhfKs2r6IXIyd98dtzjah3oHD5la_l_6qDhmCx-n2gvSg3EnGRuig8DjLWAG7TPborcAhXzCkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت فیزیکی به ۱۲۵ دلار رسید
🔹
بازار نفت باز شد اما نه‌ ادعای باز بودن تنگه هرمزِ ترامپ و وزیر خزانه‌داریش کارساز بود نه خبرسازی‌های آکسیوس در مورد مذاکره با ایران؛ در نهایت قیمت نفت با جهش قیمت ابتدای هفته غربی خود را آغاز کرد.
🔹
بررسی نمودار تفاوت قیمت برنت آتی یا همان نفت کاغذی و قیمت نفت واقعی که در بازارهای نفتی به برنت نقدی یا Dated Brent معروف است به حدود ۱۸ دلار رسیده است.
🔹
یعنی وقتی قیمت نفت برنت در مرز ۱۰۸ دلار است قیمت واقعی نفت در بازار حدود ۱۲۵ دلار در هر بشکه معامله می‌شود.
🔸
در لحظه انتشار این خبر، نفت خام آمریکا ۹۵.۹۰ دلار و نفت برنت ۱۰۸.۱۱ دلار در هر بشکه معامله می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464999" target="_blank">📅 13:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تا ساعتی دیگر پیام رهبر معظم انقلاب به‌مناسبت هفته دفاع مقدس و سالگرد شهادت شهید سیدحسن نصرالله‌ منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464998" target="_blank">📅 13:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
زاکانی: قیمت کالاهای اساسی در تهران را با حذف واسطه‌ها ۲۰ درصد کاهش می‌دهیم
🔹
۵۷ فروشگاه شهروند و ۳۱۷ شبکه میدان‌های تره‌بار، بخشی از ظرفیت ما برای کمک به معیشت مردم است. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464997" target="_blank">📅 13:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/221b8a105d.mp4?token=R4y8nBN7xsj96H-7V-n7hYr2QEWjDsPcG3aCKlC56IbYbnCjCG4Zi3S47ZnEaj0jOGKg9l6FvgAVouL0yTT0qRPJD_8yJjO1AjmLvfZB5o14mpsGuvAM1iS3QPZ6LYoazv6XXKJ8wXe5cFPWwPKWUVT0j4MZ4QYhoUq1rCrI-AoMA9eg3WKeXVW6544c_Nw1SKI7JI5UxrhPidNl8dsAw5FqSMF8ZYkQch_GYnCx-7NyFFswj-uVfPcoSQvYKjyYFqwQPKdqrsreWP8tjtAZtyiq9ilPM5qgOSB_Yj8_AtNQ8JLxMGbO9IIAGaHM-otYIkkRtadTHai9WvHT5yymBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/221b8a105d.mp4?token=R4y8nBN7xsj96H-7V-n7hYr2QEWjDsPcG3aCKlC56IbYbnCjCG4Zi3S47ZnEaj0jOGKg9l6FvgAVouL0yTT0qRPJD_8yJjO1AjmLvfZB5o14mpsGuvAM1iS3QPZ6LYoazv6XXKJ8wXe5cFPWwPKWUVT0j4MZ4QYhoUq1rCrI-AoMA9eg3WKeXVW6544c_Nw1SKI7JI5UxrhPidNl8dsAw5FqSMF8ZYkQch_GYnCx-7NyFFswj-uVfPcoSQvYKjyYFqwQPKdqrsreWP8tjtAZtyiq9ilPM5qgOSB_Yj8_AtNQ8JLxMGbO9IIAGaHM-otYIkkRtadTHai9WvHT5yymBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدال طلا بر گردن علی عالی‌پور نقش بست
🔹
ایران با طلای امروز عالی‌پور با ۸ مدال طلا به ردۀ هفتم صعود کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/464996" target="_blank">📅 13:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e46c6129f0.mp4?token=r_Lpx1laEYYmWThdc7EQB1rWzP2eyEnp-HH4fkiNQSziJKokv8GbBHEKTBBlsgZpoMTyt8YF59rUoCCniNall5YhJAfUIvyTeUmgUF7DZk4DJQ45vlt6RYHu4YADC6_EDWbM4J-Z5UqcUdvxqucmXFH0fOtTuSauTT088F8CwPyWqpmpNO6zUFEunfnQP2ZUMFBQP966m07X_DDwZw9hXNn_7aRncYQ4j4MSi8CNKWcdOPH_ovXWo2l2mEFLJXpfuYxhGD14KcYfAP9CK5KKdd_ZtgCIRdLx3-MsiqeqFK-n02V5RpR_8rduyIoGh_bFi7NvGqNZE8i9eeHY5pDt7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e46c6129f0.mp4?token=r_Lpx1laEYYmWThdc7EQB1rWzP2eyEnp-HH4fkiNQSziJKokv8GbBHEKTBBlsgZpoMTyt8YF59rUoCCniNall5YhJAfUIvyTeUmgUF7DZk4DJQ45vlt6RYHu4YADC6_EDWbM4J-Z5UqcUdvxqucmXFH0fOtTuSauTT088F8CwPyWqpmpNO6zUFEunfnQP2ZUMFBQP966m07X_DDwZw9hXNn_7aRncYQ4j4MSi8CNKWcdOPH_ovXWo2l2mEFLJXpfuYxhGD14KcYfAP9CK5KKdd_ZtgCIRdLx3-MsiqeqFK-n02V5RpR_8rduyIoGh_bFi7NvGqNZE8i9eeHY5pDt7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عالی‌پور طلایی شد
🔹
علی عالی‌پور با مهار وزنۀ ۲۱۸ کیلوگرم در دوضرب، با ۳۹۸ کیلوگرم در مجموع هشتمین طلای کاروان ایران را به‌دست آورد.
🔹
او ضمن دشت مدال طلا، رکورد یک‌ضرب، دوضرب و مجموع دنیا و بازی‌های آسیایی را به نام خود ثبت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464995" target="_blank">📅 13:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxdoMs-_zYYrNgU2FzM488IbBnC1JXZw8Blkc94PLELg2AwRNJNAHkXzt_rxUKKm3K3NXgaeHNj-c4W8jq_h7AAtB8Qqg7cp4pZp9ntQwV2GMwmfIEVAvgZ22IOpzYf5o7wuvUX6maV8BTPmP76HXq-eknth2DuPXvBg4avpGGyAxRULFM_3uwGCKwil4YIsWz_sgW61oZyRltl336ioiOmNiho_M5oEWNjLdFAZbpKBpC1sNGpb2pODldRZr_CewDapHtsH05wux5HO9pTfHoUFgRW8Su1gf8uCnOi92ce__Yg1NTTJWo8Qzlukx_MtzfuzuN6k9xyPNnCX0uhA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۰۰ هزار شامپوی تاریخ‌گذشته در تبریز
🔹
بیش‌از ۳۰۰ هزار شامپوی قاچاق و تاریخ‌گذشته به‌همراه مقادیری دارو و محصولات آرایشی و بهداشتی فاقد مجوز به ارزش بیش از ۳۰۰ میلیارد تومان در انباری درجادۀ آذرشهر تبریز کشف و توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464994" target="_blank">📅 13:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464993">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFXFKq0nYsJFkwSX0hoJgkoQCbp_yCCtFFFV0k2_ZrDk56RJ5X6-7KceAfvCmdrHRquiJ5U0r3aRQW7-W0kJW6yMOsvdUCcGR991fHp1uRSqEL1Y7JtNLhUAZi1zLPBp24kUktrjrDqfmS6DwGVio9hOtK7GpeOc7fywk6-I_vEdxq6NbAG8uDqujhgzbnmKdPWbcEVUZ2T4KcuwXMY2OABmxUmRP7GBiqQtNjgUz6WNmiwyJwHfYmcvUtUdYDMcxvdYcwod3KVFupH-JK4WM4f7oRSCZ0SxT_Xpw7FH1jSyBdnzzoCUAVjZz-F38liQh8xlrkgNKqvevJRCpnBA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازهم سر و کله داعش در عراق پیدا شد
🔹
از یک هفته اخیر اخباری از ظهور عناصر تروریستی داعش و ایجاد رعب و وحشت و تخریب در برخی مناطق از جمله استان‌های کرکوک، صلاح‌الدین و الانبار گزارش شده است.
🔹
در ابتدا در تاریخ ۳۱ شهریور روزنامه لبنانی الاخبار نوشت که دستگاه‌های امنیتی عراق اطلاعاتی درباره تحرک سلول‌های وابسته به داعش در نزدیکی مرز عراق و سوریه دریافت کرده‌اند. بر اساس این گزارش، تلاش‌هایی برای نفوذ عناصر و انتقال افراد میان دو سوی مرز مشاهده شده و همین مسئله باعث شده نیروهای عراقی سطح مراقبت و عملیات گشت و پاکسازی را در مناطق آسیب‌پذیر افزایش دهند.
🔹
اولین تحرکات تازه در یکم مهر گزارش شد و رسانه‌های عراقی نوشتند که تروریست‌های داعش قصد داشتند یک دکل برق را در بیابان‌های مابین استان صلاح‌الدین و الانبار منفجر کنند که با حضور نیروهای امنیتی موفق به این کار نشدند.
🔹
روز گذشته نیز خبرگزاری عراقی نینا گزارش داد نیروهای دستگاه مبارزه با تروریسم عراق در ناحیه تون‌کوپری، شمال‌غرب کرکوک با عناصر داعش درگیر شدند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/464993" target="_blank">📅 13:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464992">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3fca7d313.mp4?token=dnOopRkDwpF1x8fqoDkq6Ru8Ogo1uSMZpFy-uRunQX4VNAXlaliBzvOmKJIOMXx3vAvUtbNC6ia01LHTveKFLtFp_Pllnv-gj6WMZREVlYhjEVPakpuMDlaAruyn1_b9fPfNV2n_g6Np6hwA8-vOvL6sr8PJaTyAWEQJ8UI1l-4ZT86px-YFsaE1vNIYQ1gILLjj_0FjJgkSKCQpeyspzH3AZUFVWAAuedUNd8KNb7K3btD8BXW9L2dYoW2vzq9w1e44X-EWCNMRubZUureEj0o9mMZ3YEcFIlPMdLUIA6_fiDdO8vsZQIgmmoSdQWx5-FN2SXDQMjvYf2kFIphz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3fca7d313.mp4?token=dnOopRkDwpF1x8fqoDkq6Ru8Ogo1uSMZpFy-uRunQX4VNAXlaliBzvOmKJIOMXx3vAvUtbNC6ia01LHTveKFLtFp_Pllnv-gj6WMZREVlYhjEVPakpuMDlaAruyn1_b9fPfNV2n_g6Np6hwA8-vOvL6sr8PJaTyAWEQJ8UI1l-4ZT86px-YFsaE1vNIYQ1gILLjj_0FjJgkSKCQpeyspzH3AZUFVWAAuedUNd8KNb7K3btD8BXW9L2dYoW2vzq9w1e44X-EWCNMRubZUureEj0o9mMZ3YEcFIlPMdLUIA6_fiDdO8vsZQIgmmoSdQWx5-FN2SXDQMjvYf2kFIphz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عالی‌پور طلایی شد
🔹
علی عالی‌پور با مهار وزنۀ ۲۱۸ کیلوگرم در دوضرب، با ۳۹۸ کیلوگرم در مجموع هشتمین طلای کاروان ایران را به‌دست آورد.
🔹
او ضمن دشت مدال طلا، رکورد یک‌ضرب، دوضرب و مجموع دنیا و بازی‌های آسیایی را به نام خود ثبت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/464992" target="_blank">📅 13:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5O4ovDG6fEeX6tQJOcG4WPGnaf5enOoREMZNTMZ3wiHQ5DCe8wy7bYdF_lGhtRacQ3Fs30Y188lPZ1iH4i1WeRtRhDvvs49XjCtMdDCeGFd7MnaR_QByxpn5TJIAANyv41ewdYbJyt5VMXyS-JexUDqIzIJGpzsecTtr2Ipgfe2YqfcgnsK5ritFmE1CvqLp1tgGJ_6Adc9uJPsrlUB_p5zW5RFl7WqCuuyM5OtnKU8KEqXSsCao-5Ocrp9Wwf9ep0m23AcSS0OXkv03_z4K4CaoBMKvrM5BmN85qhYf--z9RyDeyDSC3XSrLLUPLp9qhkGLIfQWpwpNhmCz9FWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار سرلشکر پاسدار عباس نیلفروشان</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/464991" target="_blank">📅 13:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464990">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1a74251f.mp4?token=q_VI9y5MX-UBoqTTatcm4EAqv_htmC_m_wePwLpqJr8DfNMnD6cVJbZpOQ7ked80PGbRipvos7NEcsgUg-rWgh7I1662lFzolnypWKk5Zlx2N4Hafg2ig2BdO74RXIa2XEKG0-_pMFnKVQ74ZwMLnMTQVqPk8XyMHQ35l8gAsoOiidDjRABnIbcOx3pdK7LWCgmsrFsNSMuFct0U6Gn2tcYDGIbERhYV_vsO23JG2nFFxjdSflpglkfSp0T90pCO12RnE2JbyeYXebz170d0jsJOa2Kexh-B5e99IzKioNJai0w2B0EN_m7IUk46kSrpatQJIurp2-OGA2vq4qBonA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1a74251f.mp4?token=q_VI9y5MX-UBoqTTatcm4EAqv_htmC_m_wePwLpqJr8DfNMnD6cVJbZpOQ7ked80PGbRipvos7NEcsgUg-rWgh7I1662lFzolnypWKk5Zlx2N4Hafg2ig2BdO74RXIa2XEKG0-_pMFnKVQ74ZwMLnMTQVqPk8XyMHQ35l8gAsoOiidDjRABnIbcOx3pdK7LWCgmsrFsNSMuFct0U6Gn2tcYDGIbERhYV_vsO23JG2nFFxjdSflpglkfSp0T90pCO12RnE2JbyeYXebz170d0jsJOa2Kexh-B5e99IzKioNJai0w2B0EN_m7IUk46kSrpatQJIurp2-OGA2vq4qBonA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان یک‌ضرب با رکوردشکنی عالی‌پور
🔹
علی عالی‌پور وزنه‌بردار ایران در وزن ۹۵ کیلوگرم با مهار وزنۀ ۱۸۰ کیلوگرم رکورد بازی‌های آسیایی را شکست. @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/464990" target="_blank">📅 13:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464989">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZOdg4If93esMA6RBAi6aqrPiYAtNRhWSd_dceKF7I1hj0lmrH1DjZicXbi4FZ70trJ06nL06BexnQ-1gCr-u-QCec-RaaShbCCBJjnHA6I2LsPNWVVhnuYrC-GcHKO0dXLmlmdRCNLOfbeDmBx2MKU5EeaROtxUse9Y78x20sMiVXPxoLZPZ0HtwYTOqdUtIeWknVz32zTEGGUoolORbrjde-Z8lLswpqG1VHqKBpsH6lZMBuyU6wYHymXHJAoctNW1lTMXnmYlB9R6cX1cGJ8Eis6QQ8_nQZbnlhWW4kEvjOusURNJhWAs7M5zw0LbbwvCpiP8jcqjfodnS_vq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دریاچۀ ارومیه دوباره تماشایی شد
🔹
با افزایش آب دریاچۀ ارومیه، سواحل این پهنۀ آبی در روزهای اخیر بار دیگر شاهد حضور گردشگران و مسافرانی است که برای تماشای جلوه‌های دریاچه راهی این منطقه شده‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/464989" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464988">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ccc84e60.mp4?token=go4vZIFnaMRhDIpENl67orfjaXiOrQAdJsMzqK58L0PnIKEpSlIo2h829wQ9otLK5Rj7jhRMa1eIbvLGyqfY_Ks_zY6ZvUgvnDctCJB0clYjqRG3wqyTqmkNApB8nu958SyJlZEDqIzZNyXeqDySVJFZybmK4RBWVXZLcdlnxCgi_L2PP94vSTgk8Uh3C44WAXW28GfJ_Cl8vbnyWQWalGcp7B5ExuG4CMb3rKJ2cuUE-sEGEbqy8paqYN3PFKnSEWLLglT7aLODgpKXR8KzPtBDhklMtNx2M-gqlLsB1Gth99be6S8CaQ190UwjVbwUNXcNAjDRL_TgRUGFl522wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ccc84e60.mp4?token=go4vZIFnaMRhDIpENl67orfjaXiOrQAdJsMzqK58L0PnIKEpSlIo2h829wQ9otLK5Rj7jhRMa1eIbvLGyqfY_Ks_zY6ZvUgvnDctCJB0clYjqRG3wqyTqmkNApB8nu958SyJlZEDqIzZNyXeqDySVJFZybmK4RBWVXZLcdlnxCgi_L2PP94vSTgk8Uh3C44WAXW28GfJ_Cl8vbnyWQWalGcp7B5ExuG4CMb3rKJ2cuUE-sEGEbqy8paqYN3PFKnSEWLLglT7aLODgpKXR8KzPtBDhklMtNx2M-gqlLsB1Gth99be6S8CaQ190UwjVbwUNXcNAjDRL_TgRUGFl522wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: پرونده‌‌های ارزی و تراستی‌ها باید سریع‌تر به حکم برسد
🔹
این پرونده‌ها با روال عادی و بعضاً کند به نتیجه نمی‌رسد؛ باید مشخص شود چه کسی مقصر است.
🔹
مسئولان قضایی مربوطه چه در دادسرا و چه در دادگاه، پرونده‌های مرتبط با مسائل ارزی و تراستی‌ها که مشکلات…</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/464988" target="_blank">📅 12:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da76fbc261.mp4?token=Or3rjQRCkteWCtyWsm1sZFBnjlioI5oXT5_hsl9W8to8y9CsI2ZSqiaxnwaY7BXOFW8xKonDIbeFFIIQ6wjihTEjral8ozKDAtILg-BZuQS6lglduZptYfT3YUP7rACO_537rNy10jwr7K-ASWtmAkH27O_yiDmIERjvX1m86kWhhgD-xQ4ksOndIf4j_E_XjkF1xkSqy4SGH1naWZinJprUUpPzPdmYJ0D8_Krdn-wXAvSpA8s8RoMpv9s8jdOM_41IL4uel7MzVge35BhXRgJ93A92CYPbJdMBGf3p5RRAfv1la7K32Ub3RsLw3Fb4KDJ4tpVAY0nIwsUIuQVvCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da76fbc261.mp4?token=Or3rjQRCkteWCtyWsm1sZFBnjlioI5oXT5_hsl9W8to8y9CsI2ZSqiaxnwaY7BXOFW8xKonDIbeFFIIQ6wjihTEjral8ozKDAtILg-BZuQS6lglduZptYfT3YUP7rACO_537rNy10jwr7K-ASWtmAkH27O_yiDmIERjvX1m86kWhhgD-xQ4ksOndIf4j_E_XjkF1xkSqy4SGH1naWZinJprUUpPzPdmYJ0D8_Krdn-wXAvSpA8s8RoMpv9s8jdOM_41IL4uel7MzVge35BhXRgJ93A92CYPbJdMBGf3p5RRAfv1la7K32Ub3RsLw3Fb4KDJ4tpVAY0nIwsUIuQVvCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان یک‌ضرب با رکوردشکنی عالی‌پور
🔹
علی عالی‌پور وزنه‌بردار ایران در وزن ۹۵ کیلوگرم با مهار وزنۀ ۱۸۰ کیلوگرم رکورد بازی‌های آسیایی را شکست.
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/464987" target="_blank">📅 12:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464986">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnpkJfr_6IGR519kcQ8TmQf-Py77oVNnhhRp-cggV6bficOhu7tvIQLqNrg07surc3vHCNPhlY6_qTwRHLoOoHCY-nDlhwS7t75KCupKloB6dyzX16P_q6xZhxfAxTDuZbA0MgoVruBiw-LTITUQc5PIu6AxHxw7aKRoDAyPSuk9RgAOJjpWV-DgnNu6zHuvOz7I7jG1MykWPcj4S0CfUjh-JHJCH2iPXMqLijQab6N__Q-qGGycHSiyZZrI4lttJrh1clPdm5McUThO4xipKb6vYZ9lXRQnIBWXTB-FoE-NdQLPb1OgviPqUYQwPeAiUMfVdxOPoS4cTx5jP98wOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز خیلی سبز بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۸۹ هزار واحدی به ۷ میلیون و ۴۶۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/464986" target="_blank">📅 12:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464985">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ced4e753f.mp4?token=cz_TYRH9UvD28iohu9di0CraPHkOLwGXQcuVON17gkSW8elRME5-AORkaPshtQlRenFOPIYWzB8eGvfg1BI41Z5px2sUZPFyb36ldu4mCD1oehaqK77dVESio7U7f9Lp_T47HdLPZDlkm0KnIsh_hCDUwzY_8KmEGeZ05OPoevrXxrUjh_lQheVkpRozIWrGc9XMzmfXWHWCjEPgjnPUi8cO45LyJSmyXPEgKnp6BgujGIjHRbZOLeuCmAcjKhHeUTkrZydUEHptFYexAvp_8QqT-r0ZhS9zKLKA6nfw16OctghD5RlZnCw0PQe26Piz-1AJJAnle39Wzk34RBfDOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ced4e753f.mp4?token=cz_TYRH9UvD28iohu9di0CraPHkOLwGXQcuVON17gkSW8elRME5-AORkaPshtQlRenFOPIYWzB8eGvfg1BI41Z5px2sUZPFyb36ldu4mCD1oehaqK77dVESio7U7f9Lp_T47HdLPZDlkm0KnIsh_hCDUwzY_8KmEGeZ05OPoevrXxrUjh_lQheVkpRozIWrGc9XMzmfXWHWCjEPgjnPUi8cO45LyJSmyXPEgKnp6BgujGIjHRbZOLeuCmAcjKhHeUTkrZydUEHptFYexAvp_8QqT-r0ZhS9zKLKA6nfw16OctghD5RlZnCw0PQe26Piz-1AJJAnle39Wzk34RBfDOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مسئلهٔ کنجاله‌ها و گوشت‌های فاسد در انبارها را رها نکنید! مسئولان مربوط باید پاسخگو باشند
🔹
۶ هزار تن کنجاله وارد شده اما ترخیص نشده؛ محموله متعلق به یکی از شرکت‌های وزارت کشاورزی است و بخش زیادی از محموله هنوز در واگن است و تخلیه نشده است.
🔹
باید…</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/464985" target="_blank">📅 12:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464984">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e1645a3f.mp4?token=Fca2v4TrruKFMiXaYRGHP4PaG116x-8UcM-9nYyg0G-CUEEYhm4eZEcMZK3LE9MDMZ5Ajzo5iLtJpLCcGJwNQT4Cy5f0HWcy-9zNwy9OJ2y-z5WmiobeXH9A8pTofSaPaC__HzcXoxO5qzaqm_rJsXnmVbmpjPU1EV5UAwZ7JV94URsXzfnJWJfdi5uch65AiRXhWSlXjqxyCYrK1dhktwNQEKpXDIWxabjyf5WiRSYLS6mBGlCwzvsmIYizTCBGpLPtFCgwvox1n7MYsOzRGpZfUJ415bYUi3wz6tgf01mQ-iwMpq87yGTdGXVmfW4Fw9cU0IZ04EDaOn80-srqWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e1645a3f.mp4?token=Fca2v4TrruKFMiXaYRGHP4PaG116x-8UcM-9nYyg0G-CUEEYhm4eZEcMZK3LE9MDMZ5Ajzo5iLtJpLCcGJwNQT4Cy5f0HWcy-9zNwy9OJ2y-z5WmiobeXH9A8pTofSaPaC__HzcXoxO5qzaqm_rJsXnmVbmpjPU1EV5UAwZ7JV94URsXzfnJWJfdi5uch65AiRXhWSlXjqxyCYrK1dhktwNQEKpXDIWxabjyf5WiRSYLS6mBGlCwzvsmIYizTCBGpLPtFCgwvox1n7MYsOzRGpZfUJ415bYUi3wz6tgf01mQ-iwMpq87yGTdGXVmfW4Fw9cU0IZ04EDaOn80-srqWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مسئلهٔ کنجاله‌ها و گوشت‌های فاسد در انبارها را رها نکنید! مسئولان مربوط باید پاسخگو باشند
🔹
۶ هزار تن کنجاله وارد شده اما ترخیص نشده؛ محموله متعلق به یکی از شرکت‌های وزارت کشاورزی است و بخش زیادی از محموله هنوز در واگن است و تخلیه نشده است.
🔹
باید مشخص شود چه کسی کوتاهی کرده و چه کسی تقصیر داشته. باید مسئولان ذی‌ربط را پاسخگو کنیم.
🔹
۶۰۰ تن برنج در مدت طولانی در انبار مانده؛ صاحب برنج می‌گفت که ۹ میلیارد تومان به‌دلیل تأخیر در مجوز به هزینه‌ها اضافه شده؛ این هزینه را از جیب خود نمی‌دهد، بلکه قیمت‌ها را افزایش می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/464984" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPAIQC5XtLa5PD5lvscbVswiN003Jm9qBFOOLZ-rtsDmlMvNHrrNKGGMqAGoAOxF6OTH0r6VtnDUI891tcdsO52CrSy1CzgvakirfirLnGzi9bhDtyiw5EXwsyifN0KK5-pvPcpkkh8THE10JUyp_yb5pLoQ_G3chxNel87kTIEJXJKN3rmIfKBGrOuEeKzPU2fodHA2VJQ6vSweG7VDPkemwRmGqSPzc8STSQ2ORaNmrMHGMJgFT6FNCGn1vLgmW24sM0Rtif7D8KTxt5MUoBfLVWoHZ8BMO1qVCikbx3gGLxdCilbddeebb0hajmVDBCfh8bLvsSwq9e9lwJRbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو در سفر به امارات با بن‌زاید دیدار کرد
🔹
شبکه عبری کان: بنیامین نتانیاهو، نخست‌وزیر اسرائیل امروز در بحبوبۀ پرونده افشای هشدار ابوظبی دربارۀ عملیات طوفان الاقصی، سفری به امارات داشته و با محمد بن‌زاید دیدار کرده است. @Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/464983" target="_blank">📅 12:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0ec72a01.mp4?token=hzKr1YCPT-ojOea_9yb40PM1xw-X2OvOKuAPxGH_Oycy0rTRajS4-NJ0AaLFRH_Kk_CZMxEGRnN3I-hV4q3KC3vBNfFkgFsEMgObzvR4DgGHgloNUxQNgwJHpCQyquoSmryRUrng7YBrjQ-FAy67TWh_AhvO9FaKLXdxu0l9n6fxvjwc1you9V5retQ5WMLDlDn1eynVZa80WzVb7mV63w0EDzfwwcvbU-zR5ZypA6i1WPVmjAg6Gc0acypnPtANHPuRulZsake7ceC93Kn38RwNyaJ3rAcYje38V3hDoTMaqvQr3AlSwRl-ue7xQAZCJ7rTLfoEiQzNlR72V4iFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0ec72a01.mp4?token=hzKr1YCPT-ojOea_9yb40PM1xw-X2OvOKuAPxGH_Oycy0rTRajS4-NJ0AaLFRH_Kk_CZMxEGRnN3I-hV4q3KC3vBNfFkgFsEMgObzvR4DgGHgloNUxQNgwJHpCQyquoSmryRUrng7YBrjQ-FAy67TWh_AhvO9FaKLXdxu0l9n6fxvjwc1you9V5retQ5WMLDlDn1eynVZa80WzVb7mV63w0EDzfwwcvbU-zR5ZypA6i1WPVmjAg6Gc0acypnPtANHPuRulZsake7ceC93Kn38RwNyaJ3rAcYje38V3hDoTMaqvQr3AlSwRl-ue7xQAZCJ7rTLfoEiQzNlR72V4iFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شروع بی‌‌دردسر والیبال ایران در ناگویا
🔹
تیم ملی والیبال ایران در نخستین دیدار خود در بازی‌های آسیایی ناگویا، بامداد امروز مقابل قرقیزستان به میدان رفت و در دیداری یک‌طرفه با نتیجۀ ۳ بر صفر به پیروزی رسید.  @Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/464982" target="_blank">📅 12:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaNe5ehZ2yzkMLr7XdI8qvu_bGiPEZYte6fkFXuujOLxGuiF9EuZCvqECAVhKpA39jd4lHTlGEDA4LqIWXZxFJLGOGKVmnYvN-lojfdNDR1TufKk3aKv-WW6aE-WUQr7d1np0D5cPnSo5qUjhq-Az83_apqiZqrHgzMOwN7qBwMq7UFTcKoNMWExTHtd2XGH__D7HPZQVMpI6h-aeYmtTuDRvKPjyyL8jB5qzFbzoSwgBBscQMixuVb7lvDbWiO3hjbUZ8EdlKO7La1YuXPOzMbqQHtKAxHbEPHHD0UYpnU8HE4ltoauAVHYwRQkV7BcGr7My_R6kMNwv-_wYlCYtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت‌ عراق در محاصره؛ مقاومت تهدید کرد، پارلمان صف‌آرایی کرد
🔹
بغداد با موج فزاینده مخالفت با ممنوعیت پروازهای ایران محاصره شده است؛ مقاومت تهدید به قطع حمایت کرده، پارلمان، کارزار لغو را کلید زده و خیابان‌ها ناآرام است. دولت الزیدی اما می‌گوید این تصمیم برای فرار از تحریم‌های آمریکا ضروری است و در پی گرفتن معافیت است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/464981" target="_blank">📅 12:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464977">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVcHWpo7H2EW25eXZg6IBsMK6hs_pYYzj6cWhCgD-iqpkepNEvTDWqF-vrBEA4SMqbtMiLsu06nHaPtj7Vm6NVgTSGBaG2-j08aEuNCKwKCjqZkDvru-WUpxKI61ZjjgkQapTSC_bvcqCFGzpeK7WfxJ9SYoab9M1bx0rsbDPev1SfASa-wU6NIl_92qoIgSzoV55vMdJYID5CMtqa8LiaBk4fqZHxPl2JAWauESWZmm7oMiO3GEn2I4bT1YVdzNMSajwYttN7kF2T_BRxNt9olN1y8qwR4ZcXrDy7IGQGdB1khpeEE3CwkLRkUJ_ZUW4E4k0Rv3Zea21YYP-gdvJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUWx7pOVvZFRWbLjm3uWMCaEOKn-K9po8_QS0v1JiHmyprv-vbz7TdiMmXl8NCD5S4VmBVeOANJRfQ7U5zIoUWg8R9RZXN_xuOGO7lENAoQnWfAOdhF5qg5aqdQ8gmqLvp2NfD_cX8ThxiwY3AB2qBbTZ6TIPvkY04zH812v7fieuNvjWYF2EZ7pJnaNvhjWZpNwj_2rETBPlAdhkU-0xVUTXgTGrRxIrONBPgcBSUU1M9EfabfAX2q9k2NbJ6Qai4js6HES3EucPH8VEgEDjAkexul6nnK0yfh5VyhVqj9Fprd2682T-ZBE-Y7XxthTexPRPd-2GBuapO94kmCDFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfw0appzPnuPek_E6UeaRPWKtiyMoJEjS87plowLz9dirgITMQz0PfH8tQ0TBLyshdzrh4NKo2zf1MMKS_-xTt777R74gnF_ONEc-4aMoDWrOi4kMOiMOw8TJN5yuLcRoA0X89R8WPciBQP5jmTLr_rbiWs5eXcUFCAfemJC9Mo1ORz7O-pVWDRkt0ulHHkU6Zd8a4OkFdOYmfttd9QQKSL8MITNIzaE5MH37E7WhqABoUgtUVpKpyl93SxE6U0x8l6oFryZmwcxsOX3F4geqVoGWXOcp9tOWTpeMVwTWxHcAdw8KpVDOY6IXC5QNoo9Jzh7b_yGHXc1X2VCvRn0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbKSw4jmbRTu7KT6Sx9vy-nWqvItC4ZKQEaxa0cV4El8KGqubauMP8matqny0qbvdLXxzO82QZgnuURbYRBaMaHZPyRaCEcaoxKhX0UNnLO7SfF5uYGUwj17Vrc7GboQJKOCEDv9SnfTBAsL4elE1Nt-N4IZdJ66_R0FhFMONagDeQT1OnDKR2_4c-JpLCVACi3-TsMRfLs8dV5OuuW4FY9IYw8LmOEuuw1lq1zC9mmU_iAhpYWvLpLWVDt4l4Pa1Rh-oXgUAHeM06M0cYgz4JELKCpEm7EKF6N_ubmG52BJhmf_ISuW4LURVX9ygvQ0cPx4X6YgKbQeZ7B2SIRE2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۱۴۰ هزار جان‌فدا در سیستان‌‌وبلوچستان به میدان آمدند
🔹
در این برنامه که صبح امروز برگزار شد، ظرفیت، انسجام، سازماندهی و آمادگی بسیجیان استان که در کنار آموزش‌های مورد نیاز قرار گرفته به نمایش گذاشته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/464977" target="_blank">📅 11:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464976">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ثبت‌نام عمرۀ مفرده از شنبه آغاز می‌شود
🔹
رئیس سازمان حج و زیارت: ثبت‌نام عمرۀ مفرده برای پاییز ۱۴۰۳ از شنبه آغاز می‌شود.
🔹
میانگین پرداخت زائران ۴۵ میلیون تومان است که رقم دقیق با توجه به انتخاب کاروان‌ها به زائران اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/464976" target="_blank">📅 11:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464966">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lc7gkGbJY52PB9kL2fWai7jfCGmPN8BL9rNbAZZOlvGSX4aScR7S1-XTZnXvqAReBvbYCZHSXSq_ffewOk1yewb6RH7LXvIeT6qxnc2J_MMineWMZBsvd2PM3oHMUuqEFjDGR31etf0hdvJRohfa3xB3-w3FI2EdIDGUrQ4BD1QdksfuZi4bxORvK8XSc6e3_I7c7DS5FE0sbtqrrlyxCtXhNimGLdyXQUjldUpQLKDdzW4PClNM3VgMEqQ_M2d8WJOe4tXSG2Qe_cJXiVJsn9OHf0Kbz1OJDe42w403YD4eiuZPoghrrvf2_OWa5xcXG8TAUSLA6pOm3lM2HasAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNTLgrCcl4d_ApVQ4HWQj5EMEId-cOV0ldi-W0rl_yF6mpXIrsoWBdymyU-BF-xjKm6g5vN8AINc1EMatdfi9DHBNwJaN9D7_PUCWDY74Jc1oZ516Ahm2iq4yFIDmYELRKhIpcUxFbLpFWnRWyqrRV0uFC_KPvizBi_Cl-q9DQ84MwUDY9zqw1EjFJT_O554naeVgQe6anC7xSzqkGBlDWiLUPk87ipgrhvssfKML6iGShNmDJc5sQf-yy6YQ-EbdO2jOLbTUCCZVu0h06E42nWC7aFaO-rL5kfynrNqwR6pQgaPdO_FURj6L2QUjrh7W3KgzRefHjksNzgw6nqjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnIltablcRrvUfpMRUx_XynnBvuq612Ks4Um9d1NQSjaYAYxsWfskNdhydzT5QWc_gT6_okdpYUImc_JUyRaIPIEuyJ2yH_uIwHTASVwykEbfD8OXTHj0rZqMwBuaJlK9KoRoR8Bczff9am3I_W2dCq9ADiZpgDwspwBDsayybsBKvcEebN1BHZrtAnXdXgHn8Yu1aZRzZcU_3bKWwgB71GQcyJuaK-TUUgYjsuAcE9H9IDSbt9R-H8wUvr97yzOmYmfyWCzOufPi_rPdhRkTjqd1d9iKG2zBzH9H8CbxlozriG5ikqLEM03dI8gSs85fxBtDzwlkWs5a4LkL6YDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-BXcqTVCh9WpDcPwVoXRCjIH9hMy5oqvBUv6y7FDzhj8Ry4Voh6TS_I7w2FOe-yObvwqfFM90BUOP4jVc6_QpIqDxk9oEFNMPcL3oUtaI-Cq3y7ajNhqyUE76AvOM1jqMWbzmgrCTHTho6_g-osyuF4r0rAN02UfU0hDI91JP904hMiWInNfdnFicLL89mWLyDOvS4P-OlK0m6Ie2P9Mwao3hvgckVdwA_2ft_bYujT3Qq0wO5GBgKjmg4OytPX1JJ6enBZPiCQ7dt4miPNugJQqLnZ0tOLho6r68ReWHNLz_vXMJeWWTPk5MhjfyTrGqwPvInnDpzd9HPr0KfCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p--9coLk1ObZjcxaAwHrIeeKJngXR8Q5Y-MAN4zrcxdKfnjkeH9Ns0lQmmaTT2XIRC-MbPO4gMjngqQTl-DRWikud08TzbeR-1KjtwtPEUqnUpWp78lAtuwoCs9cbpITgQVmu9RipIW47Fy5Cp4Ch9VQdBhDXvUiHZvdnVDcPD3_6bTqAgqf1AqCdhSOmyxd0E1UhNhjQDEF3FZgHD2I8GsVOsgnwfFVYHvOMrPeUo2SwkYFwnPOFNUWKFuK5QyjV9w7Hi6_M-paWWudYlZpl69cYDRByR-hBhsS3zfXRoM1UaS_qLySrDuDx0poU62-QeV2QZw4TOqRrQAvFQi5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2sIl_4SX_X4AgOiyT5v1wiaoc4xy1HD946c74_93bZgFpjUbeE6JQf8O5Wk_o1dQdKKvMHOnlAjDYUf2EIj0zj6RwUnrq8KofABDlPH14r5J1DdfLDAijXg4QTAx1fyE3nxZPYz5AgK1BcIRF4NKZGAPcTQnieodzzeHzklAJDdlrqRVyYFveDR-KUaUYxcVDe_eHY31cm_G1f8COL6kT1qS2lt_TZ0T4vqnQw1sLzpxebkTBxOa9Nr0peGYwnjfIq9DTJr4eFk3PveBEfK2zAXCiKV8SZwM90WK5EQQ9hydzBNWYbZy47PZNqBjcL1wK4HS5Rdu5-EMmOVFFTq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1ySclKAWLC_DabkMVbpTsQYrxqA7TswLIQThggEiH_Kh42wWBaO5VGvLnqvYTlja4JkK4NoXmhdv8RY-KzxfjJbze9ER7juAhUuoVz919s-2BsfEJsuKDoCyn1q-T3YMfyGoejP4dBAcYoT8kaYBeRBkqgZz52vO_XMBx-QnN8Cm330ycQj2iq_5aXk3NpRCwVOUCnHmK09fXZgxbnx-DLL3a37gQ-jft4rZwHfPGNEu_dw3Z7H1faD7L2ZjZa73ueIIxJuenH4NNXVTfXx2F5DndsZ17-OtSQTYA_ysYfoaCE9-WgQJaRpY7_S-QQf0j8t0uwFZMZG8WtjygNv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Js8nZG_yJoIVIWKgYDWXk2T7N6mvL6ASg2dYNb4lNFdeUl4SAujytd_lSW205lgOfaoZd7gORZ8U3sJCvkCT5peg1VzIxjERuYz31QIErMDI2h43QIVqjRC8brYRpMZ3Gne9lf7NMQsB2pSf7TaFIovU228qsQsB4BZ40Np5DPU3HiMg8ft57vIV59gNRbztkLrM0Sc7-rcWnBHwl43tmPUOEBObQRpafQwy1ZuHjgxPcgNUVKSLe_1je4HlqrDt5jvC71kurIJKgNbhGY2AVl15lyR_o_TrbcbyQtEOUcP60ZJ7JoKfe5EWv5lQegZuwayvidpo8mQxkuouHTmAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3ztX0GOUShC3CKN4_Jxel1iUAVRu71l3BXlwyYlSQmyY1zJMYFyglWad1gGR3nZkUyKHaoF9mmdzvMU2OheeOjASkOkx4F8dDokB3DUUactNDIqj2_6gekqUQVQJfT3tvwon042HygqRzdqn5WTdGj4NWsmurVwChWIuiHXy2WgcYcpUt6wSOVW11LsXD3mILjfuZGsXxjS4FwB9h6s2Wv8EDopL-rieb0L-Z8ZCzchCFjGG1cbAJKD5QKGeaBv_7zIv2YEuAGWtFGFAkAulFVe7or3d5wFZuV1NjeIUbQ_SbOOhjBkcQrD6S7JhLxT7ZYShwVDAN_u9FA0QGU6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q95HVKqSdljfgFQAeCE9Ev3DElsV-7u_GOjMRbxTX83O5Q2Bk39Xfo-s0ESXJ-5IOesmPr4NiF1O7nhvp2dvEstog3n9_z_GvB-uyL3zJArxYja-z3TEMCz-dM3h6eDm785zmQLxIuRJMXPNYOSrJewCTX8U0dKDCbU2bIDRQVq5tPeSCopx4nNAPSTb2_IadI3yNxzr_JCc_5USWtcbvSds8LHu_riA5z03RXv7Ne55urtb4jW0bjqqZQxOyl0O6NyP5SYAbeqAUg-Rufud55qFhNA0uoaoSSboDpiazWdihiwiop5rK-1N1keNeTrvD_8eI8DWnM4hrf2crfYXrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصویر منتخب مسابقهٔ «عکاسی نجوم» سال ۲۰۲۶
🔹
برندگان مسابقهٔ «عکاس نجوم سال ۲۰۲۶» مجموعه‌ای از چشمگیرترین تصاویر نجومی امسال را به‌نمایش گذاشتند و جایزهٔ اصلی امسال به علی العبیدلی از کویت برای تصویری با عنوان «شکارچی آرام» رسید.
🔹
او در این عکس، سحابی تاریک…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464966" target="_blank">📅 11:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464965">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef8aa9c35.mp4?token=UejNmQaQjHxOQD6ZlKJ-GVhXenrwnn4btw28mhO-kfV1jXkr2t9XRchGW-6KSxobV4FX0NVHRZjERDl9l-NgW30vq-YQtRDr3-KqjMe7BN4jBbW2Dz6vdejSD1-9OUBTQHn9jZAgVzFEySG07ShnPc2KIjRJnPaJfz-cAPWsmyuBQNjTPQduRvc4AHCe27sejwwWm2i8swIPpC8g6LVX3HYIySANaJLoftf1kijIG9SZ6wMz6pi6b7T_BNofkOliEr5Ae5Br8JHhaZhk4ZKTD-zXNF46a3rokQl1ZVMVHalYq4J1lMpym3cBpVH1AaA9UpoovsbmgZrGzBvo_7ov0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef8aa9c35.mp4?token=UejNmQaQjHxOQD6ZlKJ-GVhXenrwnn4btw28mhO-kfV1jXkr2t9XRchGW-6KSxobV4FX0NVHRZjERDl9l-NgW30vq-YQtRDr3-KqjMe7BN4jBbW2Dz6vdejSD1-9OUBTQHn9jZAgVzFEySG07ShnPc2KIjRJnPaJfz-cAPWsmyuBQNjTPQduRvc4AHCe27sejwwWm2i8swIPpC8g6LVX3HYIySANaJLoftf1kijIG9SZ6wMz6pi6b7T_BNofkOliEr5Ae5Br8JHhaZhk4ZKTD-zXNF46a3rokQl1ZVMVHalYq4J1lMpym3cBpVH1AaA9UpoovsbmgZrGzBvo_7ov0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد خطاب به داخلی‌های طرفدار تسلیم: هیهات!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/464965" target="_blank">📅 11:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464964">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b56daa52e9.mp4?token=W1-vV46C0G84BLCCBNje-Jq4sQJPhmbTSflQpTknuiCMzKoHJmETMcYgU-GReAF3rbYahKDj41yd-OPFmu0DMAlNnvpJWGxZi8p0oywbTpqFOI4iOmKId47w-mR4m_a1KBGgkMpMwpAmNK_eVaRWxM-OfRi8KK6UJu9XFeLfjSWA3z_ipvR7vGLG4j3OdypOcn1szKli04FHIM9bjm5JMoOBLwCuL1hjDTtvkgcEaSWmvCOzM0Fz9odzKUXzmQ9r8S7KniLFGVjZJjrNlyS8segbfCEnDTJ-2OHupKnEskbObof2zk-mXWs89hcnb0Mx11fLv_vzWzSJxwY--mb4dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b56daa52e9.mp4?token=W1-vV46C0G84BLCCBNje-Jq4sQJPhmbTSflQpTknuiCMzKoHJmETMcYgU-GReAF3rbYahKDj41yd-OPFmu0DMAlNnvpJWGxZi8p0oywbTpqFOI4iOmKId47w-mR4m_a1KBGgkMpMwpAmNK_eVaRWxM-OfRi8KK6UJu9XFeLfjSWA3z_ipvR7vGLG4j3OdypOcn1szKli04FHIM9bjm5JMoOBLwCuL1hjDTtvkgcEaSWmvCOzM0Fz9odzKUXzmQ9r8S7KniLFGVjZJjrNlyS8segbfCEnDTJ-2OHupKnEskbObof2zk-mXWs89hcnb0Mx11fLv_vzWzSJxwY--mb4dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعلام «حادثهٔ بزرگ» نزدیک پایگاه میزبان آمریکا در انگلیس
🔹
پلیس انگلیس از اعلام یک «حادثهٔ بزرگ» در نزدیکی پایگاه هوایی فیرفورد که میزبان نیروی هوایی آمریکاست خبر داد و اعلام کرد که شماری از خانه‌های منطقه تخلیه شده‌اند.
🔹
پلیس شهرستان گلاسترشر انگلیس امروز…</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/464964" target="_blank">📅 11:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464963">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhw0b0XgnzKg7HkdOp-JNRVm0rmPn_5JC4H2PXNVj_1xeZAgzNSjUkEP8DhOdcbY_ynG7UB7u9x4i7IGAlPwbaiOQvbw2I_3IcgU9xQujNxbPEkJv6Nv8EtgxvF8TJHZN6vqH1ofn16trtRznB1jDXpWihcJhzVDBFKNjU2NYAs7P5BaT7jPK33Hp_GjzPeV1ge1l5GNNBsOYMoLqFI9Yu0GXykJgo7lQuJrT8wq6l1dAp9sYqkIzPGvLqqE8dR8sOchUH5vhR4MGoSo1AAJzc9T-olFXe9789C9iXgGzC6s5--H7XMDK_Ih6pnacnhpgSomHkXABBlHfPMy2-na_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مداح بحرینی پس از ۱۹۲ روز بازداشت آزاد شد
🔹
۱۹۲ روز پس از ناپدیدشدن، سید احمد الموسوی به خانه برگشت. آزادی‌ قاری و مداح اهل شیعۀ اهل بحرین درحالی رقم خورد که خانوادۀ او گفتند «سید محمد، پسرعمو و همراه روزهای بازداشت او پیش‌تر در زندان جان باخته است.»
🔸
سید احمد و سید محمد الموسوی بامداد ۲۸ اسفند پارسال پس‌از شرکت در یک مراسم مذهبی در ماه رمضان، هنگام بازگشت به جزیرۀ محرق ناپدید شدند.
🔹
مقام‌های بحرینی دربارۀ سید محمد اتهام جاسوسی و ارتباط با سپاه ایران را مطرح کردند. سید محمد کمتر از ۱۰ روز پس از بازداشت بر اثر شکنجه جان باخت و پیکرش به خانواده تحویل داده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/464963" target="_blank">📅 11:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464962">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITYbdq0He6OqGJDEpD3B1hhLALKh_D7uvpImM4CvjBReyIDZo9ClU3tBvi_MK7zuq1I-Upk2Tf65IhNqt0EsLQ_scQYBHAuOFFZpQL62qu9b4SzZUWv9H6t5x9GfseTM3G94bUUMWUrr9bSpYLzuiYDmbxQTQHxS7ovOYnQeTBpF7qrOZvEkcg7L9IXZcCBJySogQfl5uDq63fxb9YaRtiJ6FT2lrhVV9ZXnj57zXqFONBJ0WKt1mEaivrFHDkh_N34sOtRLSyia1DzwQlo1_bweTZLuD5lgC_-_46U8C2UxWbti24GpLxeFKfoLX4BnK1adoTduS3jG_42vUnvlag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر منتخب مسابقهٔ «عکاسی نجوم» سال ۲۰۲۶
🔹
برندگان مسابقهٔ «عکاس نجوم سال ۲۰۲۶» مجموعه‌ای از چشمگیرترین تصاویر نجومی امسال را به‌نمایش گذاشتند و جایزهٔ اصلی امسال به علی العبیدلی از کویت برای تصویری با عنوان «شکارچی آرام» رسید.
🔹
او در این عکس، سحابی تاریک کوسه یا LDN 1235 را ثبت کرده؛ جرمی که با فاصلهٔ حدود ۶۵۰ سال نوری از زمین و در صورت فلکی قیفاووس قرار دارد. شکل خاص این سحابی نتیجه وجود ابرهای متراکم غبار است که نور اجرام پشت سر خود را مسدود می‌کنند.
🔹
العبیدلی علاوه بر جایزهٔ ۱۰ هزار پوندی، مقام نخست بخش «ستارگان و سحابی‌ها» را هم به‌د‌ست آورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/464962" target="_blank">📅 11:06 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
