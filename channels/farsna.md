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
<img src="https://cdn4.telesco.pe/file/XWhGhTsSaTwA51xnpkJhel1-cY925AvHSfMT07ZnVCD4fBRGBpTjH69mWjSCTpGG_d6mJEscm0GuLNX1uZQTPBxQzPqJS3Z325svfw6YW1n7PINAan_7hJV-HEsJ7MqbrGYEno2BtLrPPtUiksfykdc319cE-kTGykW4N1_tGj7DQBCDKxAiC6T-aqhHWMy-wSmsjTa91sI9gjuKW1Lb-jYZQINsROuXcHV-wdEhSQsRdGu9TmJ3FEhYNVFnqODwsL0fltPh-9jCzjV89fKIi0iJZFIZ1fxSSIC__18a_aUW-n0JJiiqQq8NtAycWFyDdZAhZ3bOlKC5fRvJvEnAug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 18:01:45</div>
<hr>

<div class="tg-post" id="msg-445475">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFkPairSl8G1sAu8dZiCLymuNHbUTWPcqJ9wXQKFAgVanBtLS83zKrOJXCIB3XDFyyhOGBlDee8XReTsY-NIKbSoTClxfPjK9-DXj-DE3UtMpZx8Bm1KXPVBplaDwRkYIColDPeH0o553FtBlr7X_d_7vXwxrUwnlnaKo9yy3gavW6AU9oDl3gkKm_2RBW6SAwiah3SLofgBW0lc7F0nGDEWo-4VBVgTKMMkDTRIw2yI6IbCRuOVfb4D-S433lsncQSKC-sJICI0GyB38vSnUoyWUk_At-HAuPJs754fQQn-qGOiETGkuTPw9LE4T5tgvvWs8kT1vNIJvDjFed6EUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت کالابرگ ۱۴ سال به صورت یک‍جا به مردم
🔹
با مسکونی کردن فقط یک درصد از مساحت ایران، به هر ایرانی ۲۰۰ مترمربع زمین می‌رسد. با توجه به متوسط قیمت زمین در کشور، ارزش این زمین می‌تواند برای هر نفر به بیش از ۲ میلیارد تومان برسد. این رقم به اندازه ارزش ۱۴ سال پرداخت کالابرگ است.
🔹
در حالی که از ابتدای سال ۱۴۰۰ واگذاری زمین به مردم آغاز شده بود، فرزانه صادق مالواجرد حدود دو سال است واگذاری زمین را متوقف کرده و زمین‌ها در احتکار دولت باقی مانده‌اند.
🔹
حدود ۷ میلیون خانواده از جمعیت کشور مستأجر هستند و ۵ میلیون خانواده نیز اصلا خانه‌ای برای سرپناه ندارند و در خانه دیگران سکونت دارند. با واگذاری زمین و فراهم کردن بستر ساخت، می‌توان بخشی از بار سنگین اجاره‌نشینی را از دوش آن‌ها برداشت.
🔹
کمک به معیشت مردم هم‌اکنون از اصلی‌ترین دغدغه‌های دولت است و برای این‌ کار، کل دولتمردان بسیج شدند تا رقم کالابرگ را اندکی افزایش دهند، درحالی‌که زمین دارایی برای دولت است که می‌تواند بدون نیاز به بودجه بزرگ در اختیار مردم قرار گرفته و اساسی‌ترین نیاز مردم را رفع کند.
🔹
وزیر راه و شهرسازی فرزانه صادق جلوی واگذاری زمین به مردم را گرفته و معتقد است که به جای آن راهکارهای جایگزین مانند توسعه مسکن استیجاری برای زوج‌های جوان را دنبال کرد.
🔹
در مقابل معاون سابق مسکن وزرات راه هادی عباسی می‌گوید که زمین از جمله دارایی‌های دولت است که هم‌اکنون غیر مولد مانده و به اقتصاد کمکی نمی‌کند و اگر عرضه زمین شروع شود، بدون نیاز به بودجه می‌توان مسئله مردم را حل کرد.
🔸
طبق تجربه مسکن مهر و نهضت ملی مسکن، دولت می‌تواند با واگذاری زمین به مردم و راه‌اندازی سامانه‌ای که سازندگان را به‌صورت مستقیم به مالکان زمین متصل کند، تنها با عرضه یک درصد زمین‌های به هر خانواده سه نفر حداقل ۶۰۰ متر زمین بدهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/445475" target="_blank">📅 17:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445474">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOnRVjaURM8nUDiFpn1rk2gZmAyEFftgHlRQHdLsauhIPNeLUu9GO_L_-_sxu9oAgfIjB6qiToFKeDgzWr7FEsv_eSdo88fsnqQeJna3QYUQJMCIeGd-P6sB_f7TlzGzDsFlCHsE4TqUvkWD0NntRopWfRQgEJ1XNKqTdXrmdJcYYWJaIxO18qZ8Y9z_2oaD9oxXb4vv9Ntf-WcUY0iy7xrwT9lZB3l_QTdSbZU9CaQ2Kg-8a1_Fjm9P6hLvEP8ZHp4Ru4xYQcbvUYHW2ojUFWTKbXHpJ0V1fbUd_gNXiamUBzDipUfFEIcEQ1s6zE9NJO-F9sjAC_daBwtwbTeCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک شهر برای جذب نیروی «بانکدار» آزمون استخدامی برگزار می‌کند
🔹
بانک شهر به‌منظور تأمین بخشی از نیروی انسانی مورد نیاز خود، از میان متقاضیان واجد شرایط، در رده شغلی «بانکدار» نیرو جذب می‌کند.
🔹
به گزارش روابط عمومی بانک شهر، بر این اساس، فرآیند جذب از طریق برگزاری آزمون کتبی و با همکاری مرکز سنجش دانشگاه آزاد اسلامی انجام خواهد شد و متقاضیان واجد شرایط، اعم از زن و مرد، می‌توانند در این آزمون شرکت کنند.
🔹
داوطلبانی که در آزمون کتبی حد نصاب لازم را کسب کنند، به مصاحبه‌های تخصصی و عمومی دعوت خواهند شد. در صورت موفقیت در مراحل ارزیابی، فرآیند به‌کارگیری آنان مطابق ضوابط، مقررات و آیین‌نامه‌های داخلی بانک شهر انجام می‌شود.
🔹
بر اساس شرایط اعلام‌شده، دارندگان مدرک کارشناسی با حداکثر ۲۸ سال سن و دارندگان مدرک کارشناسی ارشد با حداکثر ۳۰ سال سن (مدت خدمت سربازی آقایان به سقف سنی اضافه می شود) و همچنین داوطلبان صرفا دارای سابقه بانکی با حداکثر ۴۰ سال سن، مجاز به شرکت در این آزمون هستند.
🔹
متقاضیان برای اطلاع از شرایط ثبت‌نام و جزئیات آزمون می‌توانند از روز سه‌شنبه ۹ تیرماه به پایگاه اینترنتی مرکز سنجش دانشگاه آزاد اسلامی به نشانی:
https://azmoon.org
مراجعه کنند. همچنین این آزمون استخدامی در تاریخ 9 مردادماه برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/farsna/445474" target="_blank">📅 17:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445473">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/445473" target="_blank">📅 17:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445472">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">زمان پیش‌فروش بلیت سفرهای جاده‌ای برای تشییع رهبر شهید
انقلاب
🔹
سازمان حمل‌ونقل جاده‌ای: با توجه به مراسم تشییع پیکر مطهر رهبر شهید انقلاب، پیش‌فروش بلیت اتوبوس به مقصد تهران، در بازه زمانی ۱۲ تا ۱۵ تیرماه انجام می‌شود.
🔹
پیش‌فروش بلیت برای حضور عزاداران در قم طی روزهای ۱۵ و ۱۶ تیرماه و برای سفر به مشهد نیز ۱۶ تا ۲۰ تیرماه انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/445472" target="_blank">📅 17:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445471">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">افشای تخلف میلیون یورویی یک شرکت دولتی
🔹
سندی به دست خبرنگار فارس رسیده که نشان می‌دهد گروه صنایع شیر ایران (پگاه) از سال ۹۸ تا ۱۴۰۳ بیش از ۱۵۷ میلیون یورو ارز حاصل از صادرات را به چرخۀ رسمی بازنگردانده است.
🔹
چند روز پیش نیز حسابرس دیوان محاسبات در نامه‌ای به صندوق بازنشستگی کشوری امضای مدیرعامل شرکت صنایع شیر ایران را غیر قانونی اعلام کرده بود؛ چرا که این شرکت شبه دولتی با وجود منع قانونی یک بازنشسته را به عنوان مدیرعامل به کار گرفته است.
🔸
شرکت پگاه زیر مجموعه صندوق بازنشستگی کشوری و وابسته به وزارت کار است که حدود ۳۵ درصد از بازار لبنیات کشور را در اختیار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/445471" target="_blank">📅 17:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445470">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-ozLAPI0Du1FuZEqRza-ImUrg21x1OpkC5daxjBGGvCJCWQIJyy9O1aBpArm1k8wKgBRLkHejTXXxIEkVinirC15lpzZNx8VqTvoWMrtQPdFmcMWBdgv8ndk_HYbJMG5r4qodY8O6hGM9UamkJVpYeNFJXhcFPNSmUIyw3SKZCFUj4NllcJGWDVb9xU4rLPDoQDYO0XQ6AuvnO23ZiCFsVQAVsiU77Gnpj-D4SrnhHXE1gI2vzj14kPYLQwOc3fraMY1GANiyKxAKWFlNq3ZeItQxm9IWTCEjPt2AL8rY_FQCSE46eiJ9DfnR2Wy0KUcPEYuxK4myh8KRjxQ6wdaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین نشست کمیتهٔ مشترک ایران و عمان دربارهٔ تنگهٔ هرمز برگزار شد
🔹
معاون حقوقی وزارت خارجه: در سفر به مسقط اولین نشست کمیتهٔ مشترک هرمز با وزیر مشاور امور خارجه عمان برگزار شد که ضمن مرور مسائل جاری در رابطه با تنگه، دربارهٔ مدیریت آیندهٔ تنگه در چهارچوب…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/445470" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445469">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73f3e58e4c.mp4?token=dXbo_uZ1Idnn3dXdEBGB_2EuQkNeHIosidKEj4FDQD2Ar-NWDImTxgNHYDT-MmIPeI1pijv1SRb-qkW9U98m62QZCXxgDM-IK2pATwgAlYbEVt3NJKtrwafjKjIRazATa5uYXZE4DhMOvfcLE4JodZsBTJAKab3M3a2hTxKkbNwuEe_LCRng5270CONqNfx2XUBHMaAhhvJ-m-2HiBxxL1UmSJ3EQX8EigX-ZtU6tPCYCE_FsEIwLC8rlXAXUbgAoUa89BxrdZf5REKYurTrVr9lo_-N1DxYDW-yWAABRjc7VIiDJe9891Fi1BG1R3fvXHRTrCRXKpg7zg4OjOkPjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73f3e58e4c.mp4?token=dXbo_uZ1Idnn3dXdEBGB_2EuQkNeHIosidKEj4FDQD2Ar-NWDImTxgNHYDT-MmIPeI1pijv1SRb-qkW9U98m62QZCXxgDM-IK2pATwgAlYbEVt3NJKtrwafjKjIRazATa5uYXZE4DhMOvfcLE4JodZsBTJAKab3M3a2hTxKkbNwuEe_LCRng5270CONqNfx2XUBHMaAhhvJ-m-2HiBxxL1UmSJ3EQX8EigX-ZtU6tPCYCE_FsEIwLC8rlXAXUbgAoUa89BxrdZf5REKYurTrVr9lo_-N1DxYDW-yWAABRjc7VIiDJe9891Fi1BG1R3fvXHRTrCRXKpg7zg4OjOkPjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های شنیدنی حجت‌الاسلام میرهاشم حسینی در خصوص موهبت داشتن فرزند
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/445469" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445463">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">عروج</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/farsna/445463" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
موسیقی رسمی تشییع پیکر «رهبر شهید» منتشر شد
@Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/445463" target="_blank">📅 16:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445462">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8Gok1OUZcPfZ04CE6CDt9-I1aUX07_mZ6oTKYmc-8kq7HZ5SHU4few5NERbvLRi3cTHWd6uK7_POIDL1bF-E1XiNLb1h0-h4ngxsxXi7sk_Q2DDD5Ivr7rDimGYwqd3YzdBJOH0M-_cYgB7LmkLTsd2qvmhY9-gQmN5lfWdxdNI9aAtXHaInXevdQaAlr32JPKonTiytveW1c_jWT7AKFfyL2oJts1fQ8Z9EXYlgclby2tGFQsIsYMIwSQvFFTLEHKpOky6kYAbzvBNc1ZLJYqu_Yje4gF5CUMlu9_FqjJFIBAzBnE__OdxrKUYDkowlpW-jVuePm0LKTBm3BR1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سوال از آقای مجری که حالا منتقد هیئات شده است
🔹
ویدیویی از رضا رشیدپور منتشر شده که در آن می‌گوید: مداحی‌ها چرا سیاسی شده؟ مداح‌ها چرا در هیئت‌ها نظر سیاسی می‌دهند؟
🔹
امام موسی صدر تعبیری دارند که هر سال در ایام محرم بسیار نقل می‌شود: «در هیئتی که دغدغه مبارزه با اسرائیل نباشد، شِمر هم سینه می‌زند.»
🔹
اما اگر بخواهیم با منطق خود آقای رشیدپور به موضوع نگاه کنیم(باز هم این نقد وارد نیست.) اگر معتقدید مداح نباید وارد سیاست شود، این قاعده باید درباره مجری و بازیگر و ... هم باشد.
🔹
در این صورت، یک مجری تلویزیون هم نباید در عرصه سیاست نقش‌آفرینی کند.
🔹
جالب آن‌که آقای رشیدپور در بخشی از صحبت‌هایش می‌گوید: «حاج حسین فخری را گوش می‌کنیم، گریه می‌کنیم.»
🔹
اما ظاهراً خودِ آقای مجری، چندان هم پای منبر و هیئت حاج حسین فخری ننشسته است؛ وگرنه می‌دانست که او تنها مداحی نمی‌کند. حاج حسین فخری در هیئتش از استقلال و آزادی می‌گوید.
🔹
بنابراین، اگر ورود مداح به مسائل سیاسی محل اشکال است، این اشکال باید به همان میزان متوجه هر چهره رسانه‌ای و مجری‌ای هم باشد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/445462" target="_blank">📅 16:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445461">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
🔹
سپاه هرمزگان: از فردا به‌مدت ۲ روز در حومهٔ بندرعباس عملیات انهدام مهمات جنگ رمضان انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/445461" target="_blank">📅 16:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حملهٔ حزب‌الله به مقر افسران ارشد ارتش اسرائیل در جنوب لبنان
🔹
برخی منابع لبنانی گزارش کردند که نیروهای حزب‌الله امروز یک بستهٔ انفجاری را در مقر جانشین فرمانده یکی از تیپ‌های ارتش اسرائیل منفجر کرده‌اند.
🔹
در جریان این عملیات، ۲ نظامی زخمی شدند که وضعیت یکی از آنان وخیم گزارش شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/445460" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOqYJUrFNrs1QvldTEYFHvISyIwFXAHBXQbpC4QEw0U_Es-liL6v1SkZePvpEV3CLmTfS2n_2vOBkecHfGOTJDUVkP6JckvX1wlbB4iShZm8a5COuomHkAZcBdoSt8SNwW614rXXGrvCBQGgmiK1_Qc3gSylI9i0ATIYtitdEYph3QV3eMS27k_YLvBoev89t6CDHLjEmHnF4ynZzRvstz4d39QyyTCaR2leCjYs1oSewqn4wnsn7IjSYGbD3sn8P1W-RPAsWrYsXdP2JPY6Cf3Y0Q04Yx0TuQkXee7V3sUhWUfvgEwWmDsE6WhBnggeZjx6LxRIDjyZ5d3rb-_XaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مامور نیروی انتظامی در چهارمحال‌وبختیاری
🔹
شهید احسان احمدی، صبح دیروز حین انجام مأموریت تعقیب‌وگریز متخلفان در مسیر جونقان به فارسان چهارمحال‌وبختیاری به‌ درجهٔ رفیع شهادت نائل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/445459" target="_blank">📅 16:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445458">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5cTCZqqTcQ2BeEHWHMbp8NPNqnhBK3VtgFwQAqg-VoddpBEi9KdDAqtQEt6UVzZX6EAa0DoHRW9t2t_NmD-TZUZuiaeRKx-5zT4AlrE_cKlmiyyX4RP6bJtMRNpU_EivexQXkUNot90xKLcI7BRH2K5p-fU5RWepQrDumD8cxoMLmTEZdZQ7w7AzJ4B-ujK5hr-hIOoUrre3JgxR0MiA3AvkqgTn33fIf_I0-waxQOE4C2_N14eJ0kGJ7d3EgC8uAMCMnu91Fdm0cCkXABCQSLv__mvOXvRp0FEd53juHaHsBl3lngLvbCe81Z08lqwY7MBKQJTHR-W3SIX3Blsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعهٔ جدایی ۲ پرسپولیسی کهنه‌کار صحت ندارد
🔹
پیگیری خبرنگار فارس نشان‌ می‌دهد شایعات مطرح‌شده دربارهٔ آیندهٔ عالیشاه و پورعلی‌گنجی مبنی‌بر اینکه «باشگاه پرسپولیس به این ۲ بازیکن پیشنهاد فسخ قرارداد یا انتقال قرضی به تیم‌های دیگر را داده است» صحت ندارد.
🔹
عالیشاه و پورعلی‌گنجی هر ۲ برای فصل آینده با پرسپولیس قرارداد دارند و طبق قراردادشان در جمع سرخ‌پوشان حضور خواهند داشت، مگر اینکه در ادامهٔ نقل‌وانتقالات شرایط جدیدی به‌وجود بیاید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/445458" target="_blank">📅 16:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445457">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab32ba603e.mp4?token=Ywwk_WeTKqtRaw4xMAtwtGutFE0hn9DC1no5Y_7ccoBhGfUOn1EDMJwixRMUvdKPmgYv7ZBHvUoZCt7us4ICwJ3nzE_Ybv8hV5ReI8dt2o-dJqDnzDRBPEcb8eWIT9613Ky9u6ovm0Iq4r7lqZP9dEZugrXJ_NRbgyDnWmSm-xCBZE6kIkl0n8jxWcWMaFbdsZC34wvykXIIkbKQGbMz5fyLuFstGH9ytTPCeMWWN5jWp_yeNZmTJSa4AcPMklxhcSz510dgEuHGRe8-yDyxPz9zdl7C5SzqGnB4DzWNrtY9sGmNgAFwzHrprg1Mcv5UeHa7Vw08FiqIBWMBfIYcLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab32ba603e.mp4?token=Ywwk_WeTKqtRaw4xMAtwtGutFE0hn9DC1no5Y_7ccoBhGfUOn1EDMJwixRMUvdKPmgYv7ZBHvUoZCt7us4ICwJ3nzE_Ybv8hV5ReI8dt2o-dJqDnzDRBPEcb8eWIT9613Ky9u6ovm0Iq4r7lqZP9dEZugrXJ_NRbgyDnWmSm-xCBZE6kIkl0n8jxWcWMaFbdsZC34wvykXIIkbKQGbMz5fyLuFstGH9ytTPCeMWWN5jWp_yeNZmTJSa4AcPMklxhcSz510dgEuHGRe8-yDyxPz9zdl7C5SzqGnB4DzWNrtY9sGmNgAFwzHrprg1Mcv5UeHa7Vw08FiqIBWMBfIYcLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندهٔ سابق کنگره: آمریکا در جنگ پیروز نشد و ایران کنترل تنگهٔ هرمز را در دست دارد
🔹
گرین، نمایندهٔ پیشین مجلس نمایندگان آمریکا که زمانی از حامیان ترامپ بود، از اقدامات او در جنگ با ایران انتقاد کرده و گفته که «ایران نشان داد هر زمان که بخواهد، می‌تواند تنگهٔ هرمز را باز یا بسته کند. تیلور گرین همچنین گفت: آمریکا در جنگی که به‌همراه اسرائیل علیه ایران آغاز کرد، نتوانسته به پیروزی برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/445457" target="_blank">📅 16:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHHe0aNlBYp0f0pctWwrIm7B-KGgp50R-oYvpBVTlbkTS8SbTxWIri6X22L-KviXaQ7DUfnzRD8jg-8dvaDvBMEn9ypLVcSCyQt6iXsdp-I29ci0roFg3Ywqz-a7h9ZralgKG1bKNadDG-Whn6HdigBowscbas-npEJ3ZC2d2wHBZprxTcW5NgPwehYZvK8qdZVZsuBMjKd06ls2yOrNXyYGvZvHu4VtirEJGRQtjV0bb87ivx9YSXUt2Z696DzqeZrcPvEXsbElHc62RWd_0TjStiYxYvGq2fE2aH5kC3oSduujHlOzePQClCyagRqEqY_wOYTWmam2arKU3tvg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادق زیباکلام بازداشت شد
🔹
صادق زیباکلام صبح امروز با دستور قضایی بازداشت شد. پیش‌تر دادستانی تهران از تشدید قرار نظارت قضایی او به‌دلیل نقض ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی خبر داده بود.
🔹
براساس اعلام مراجع قضایی، زیباکلام…</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/445456" target="_blank">📅 15:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d571babdf.mp4?token=N_IAy57IMPnX3NVljpkLiGgDK_OKJZYBR3ND7s1obHC7HiPtNwg_Tqn34rFQkoKN7fIJra103oZroEE38i0bUbHmyDbK6W1YdQa6J6nHSMd5y-mfTlA2rk7kqAJkUAtXVnsZNoGN1kN_9ez7PrNVaxfKtvduhEVw-bJRwSI-p3G4--VeT2VCKk0DvALIX5ufiQAkhTc_--yPclrUVzffQ-vIYPXeegzPo2W631F9s_bFxzW1eTpkeJe8hx7WBQAmcdsMrfkInL6BoXdOCqzu0hb1bzkjiZNXuth9GLoypBtEt0btsqpanrtfQaURHnq5FfrdOTQCgVB5DbRvtBchOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d571babdf.mp4?token=N_IAy57IMPnX3NVljpkLiGgDK_OKJZYBR3ND7s1obHC7HiPtNwg_Tqn34rFQkoKN7fIJra103oZroEE38i0bUbHmyDbK6W1YdQa6J6nHSMd5y-mfTlA2rk7kqAJkUAtXVnsZNoGN1kN_9ez7PrNVaxfKtvduhEVw-bJRwSI-p3G4--VeT2VCKk0DvALIX5ufiQAkhTc_--yPclrUVzffQ-vIYPXeegzPo2W631F9s_bFxzW1eTpkeJe8hx7WBQAmcdsMrfkInL6BoXdOCqzu0hb1bzkjiZNXuth9GLoypBtEt0btsqpanrtfQaURHnq5FfrdOTQCgVB5DbRvtBchOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: پیام رهبر انقلاب نیازی به توضیح ندارد؛ اگر حیاتی باشد سعی می‌کنیم تمام نکات این پیام را عملی کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/445455" target="_blank">📅 15:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a240d06.mp4?token=XttflS9UQGQ6fpCKOsCFC3TQDFV0Zw5i_A2a9LzB7_FAjpn62Z5um-kHqTP3ErPtROTwQrjEFXjr4pBGfqFfriE2H7n-GN6Z88PtE8XSP1y9txHrx9OQioiEY8Dn_n7tIUj_R7PO1bVz7-lD1QrAOX0Rp0IzRK4hyEyxcbHntkP6-leAvfz69Ywf_UUk2NrvCDZuB2rsGvtUTk2enIfdIm_FuM8iOy1hWZjB4dqs7pBKpa5OKryTIV1g9PFoKk9RUNDCutqilz8oT36feHzglOy6VljnS-QPFjDq6VFwagjM4SsR_x6zyw7UeLm57930Z6Ud5ohJ2-_h1vo1CqxBOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a240d06.mp4?token=XttflS9UQGQ6fpCKOsCFC3TQDFV0Zw5i_A2a9LzB7_FAjpn62Z5um-kHqTP3ErPtROTwQrjEFXjr4pBGfqFfriE2H7n-GN6Z88PtE8XSP1y9txHrx9OQioiEY8Dn_n7tIUj_R7PO1bVz7-lD1QrAOX0Rp0IzRK4hyEyxcbHntkP6-leAvfz69Ywf_UUk2NrvCDZuB2rsGvtUTk2enIfdIm_FuM8iOy1hWZjB4dqs7pBKpa5OKryTIV1g9PFoKk9RUNDCutqilz8oT36feHzglOy6VljnS-QPFjDq6VFwagjM4SsR_x6zyw7UeLm57930Z6Ud5ohJ2-_h1vo1CqxBOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: پیام رهبر انقلاب را باید چندین بار خواند و به تک‌تک کلمات آن دقت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/445454" target="_blank">📅 15:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c77f3062d2.mp4?token=LvZ-gZIoHui-jXReznjgGymXIryQWiGMfRkgeEYjH86kH1n6KLx0rZaBroTId9h58AhXOjYYILeaIIar2u56fmgcsj8VUfVO7yQNwbMxBR7wasC1Nt_4Ag5eSuuo3EE3FfDC_SISRGKi6uW6cM_-XlYwgadzayF_ZEIbGRHkfDfYQ5ugz14ReoXD2BvZQSe2wSlmapEBZLK_91oakgreY-uS5xVlUwAWFho03ii_yzOoVUdTea9uWgVFSBhm-43I6A0e8t7e2Ngsy883Au1K1tiZviR6PkQd3xLAwJULKqfVqKDoGaeLTsrJ8YS6SsDVpNsaGz7b31KnT48N4uvKMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c77f3062d2.mp4?token=LvZ-gZIoHui-jXReznjgGymXIryQWiGMfRkgeEYjH86kH1n6KLx0rZaBroTId9h58AhXOjYYILeaIIar2u56fmgcsj8VUfVO7yQNwbMxBR7wasC1Nt_4Ag5eSuuo3EE3FfDC_SISRGKi6uW6cM_-XlYwgadzayF_ZEIbGRHkfDfYQ5ugz14ReoXD2BvZQSe2wSlmapEBZLK_91oakgreY-uS5xVlUwAWFho03ii_yzOoVUdTea9uWgVFSBhm-43I6A0e8t7e2Ngsy883Au1K1tiZviR6PkQd3xLAwJULKqfVqKDoGaeLTsrJ8YS6SsDVpNsaGz7b31KnT48N4uvKMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام اژه‌ای به رهبر انقلاب: خود را ملزم به اجرای فرامین واجب‌الاتباع حضرت‌عالی می‌دانیم
🔹
رئیس قوه‌قضائيه در پیامی به رهبر انقلاب نوشت: برگزاری مراسمات مربوط به هفته قوه‌قضائیه آراسته و مزین شد به پیام نورانی و هدایت‌گر حضرت مستطاب‌عالی و فرامین لازم‌الاتباع…</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/445453" target="_blank">📅 15:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445452">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dea0f6b74.mp4?token=trWWBKxqzYRCmt3clg3bEiRKwb9hNgjB9dtydnvUw2xyMNaLkXCVLksHODPOd4hK28NN8xNU7H7j6tcdwePozlh5WHYDtTqZvciN5nlfCB0sUpkjjX_F3gKP1JlqQsZp--KNsypFcGJNPgqGHLTdjhkkOIIxFwkqKHQbOGgPR1uefpKlWDf1psOnVf9Q9SpDaoz2A3NsNivDWZRY_NWjT5oSF96vJJQKd-DBF-OIXIgottTreh_t6OJ2zSoi0m6XEW0K7qpLNom8q6qqcPRW7D1dfYVrbzkqgsB4ZqC_PP38Mh3rvTHXI29ccrUzxoVnWAWHkzZHqNwUd1mEJPE3NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dea0f6b74.mp4?token=trWWBKxqzYRCmt3clg3bEiRKwb9hNgjB9dtydnvUw2xyMNaLkXCVLksHODPOd4hK28NN8xNU7H7j6tcdwePozlh5WHYDtTqZvciN5nlfCB0sUpkjjX_F3gKP1JlqQsZp--KNsypFcGJNPgqGHLTdjhkkOIIxFwkqKHQbOGgPR1uefpKlWDf1psOnVf9Q9SpDaoz2A3NsNivDWZRY_NWjT5oSF96vJJQKd-DBF-OIXIgottTreh_t6OJ2zSoi0m6XEW0K7qpLNom8q6qqcPRW7D1dfYVrbzkqgsB4ZqC_PP38Mh3rvTHXI29ccrUzxoVnWAWHkzZHqNwUd1mEJPE3NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کولیوند: در اطراف چند مرکز درمانی که بوق زدن هم ممنوع است، ۳۶ بمب سنگرشکن زدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/445452" target="_blank">📅 15:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445451">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea32e5961.mp4?token=i3LaROKsmsi0iqttZ_iB5for8-jJuHDYuxF5T3RKccdLqcZ_n7Uqzz8cshKnf8dawIU7A2tEz1evolZvdmejtVzgCqwmspPqp9vq3FBfNgfbUGYO_Sqqn2CAKxQGXg49fz76kgrVlgDPIxZohQzdkTNYso2UFXQuBO68HUnG9qM0Vqjrtdh_OVxLw6wHIn87c1igtJce4XLtYN2FvuBXUGabgRC9EY1Jfo8a1c37fqiXdk0vWp2kVOxQOzG6wHlJVBcc-CFtzKK_0Z5jc3vKKcJt7DzlfUR_kYceJxPQxQx0qBrO_y7YbS8f6CmdJjoyL16FF5nHheYKruF-oIS7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea32e5961.mp4?token=i3LaROKsmsi0iqttZ_iB5for8-jJuHDYuxF5T3RKccdLqcZ_n7Uqzz8cshKnf8dawIU7A2tEz1evolZvdmejtVzgCqwmspPqp9vq3FBfNgfbUGYO_Sqqn2CAKxQGXg49fz76kgrVlgDPIxZohQzdkTNYso2UFXQuBO68HUnG9qM0Vqjrtdh_OVxLw6wHIn87c1igtJce4XLtYN2FvuBXUGabgRC9EY1Jfo8a1c37fqiXdk0vWp2kVOxQOzG6wHlJVBcc-CFtzKK_0Z5jc3vKKcJt7DzlfUR_kYceJxPQxQx0qBrO_y7YbS8f6CmdJjoyL16FF5nHheYKruF-oIS7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود دستهٔ عزاداری قبیلهٔ بنی‌اسد به حرم امام حسین(ع)
🔸
طایفهٔ بنی‌اسد یکی از قبایل اطراف کربلا بود که ۳ روز پس از واقعهٔ عاشورا با راهنمایی و حضور امام سجاد(ع)، پیکرهای امام حسین(ع) و یارانش را به‌خاک سپردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/445451" target="_blank">📅 15:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445450">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7baaf678ea.mp4?token=WhrQtUHTDirUfsTph2sCElonjVTUvTXhdXeh3URbuIj8ro4e1fraVJTg1Hp3Zt5J42c2lEZY4KEHk_v4arDYKq6QfwF7CbwFJZ1oO-0m870xRpBCWX2YOL5anXmer5nTLXYMYJDD4kuEno10lFYEtZZR_kkGTihFRQ6cyYyq-ZozSbAB2CEPIcs-WyjhF_mshAK1MwCa9d7z6sxchpZJSMpHbqvRAT8I36baTlBlYVIKaJ7jgr--1hGH87e_G-jl4OCLxVgcRJv65iGHxJozEDxYclZ6QGCjGh6e-vkfJlUZ9cH5T2hWj7l2ZFtjov3CHTf3PhofOZtnDHYNxbdqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7baaf678ea.mp4?token=WhrQtUHTDirUfsTph2sCElonjVTUvTXhdXeh3URbuIj8ro4e1fraVJTg1Hp3Zt5J42c2lEZY4KEHk_v4arDYKq6QfwF7CbwFJZ1oO-0m870xRpBCWX2YOL5anXmer5nTLXYMYJDD4kuEno10lFYEtZZR_kkGTihFRQ6cyYyq-ZozSbAB2CEPIcs-WyjhF_mshAK1MwCa9d7z6sxchpZJSMpHbqvRAT8I36baTlBlYVIKaJ7jgr--1hGH87e_G-jl4OCLxVgcRJv65iGHxJozEDxYclZ6QGCjGh6e-vkfJlUZ9cH5T2hWj7l2ZFtjov3CHTf3PhofOZtnDHYNxbdqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جنگنده‌های اسرائیلی در جنوب لبنان، بالن‌های حرارتی پرتاب کردند
🔹
منابع لبنانی خبر دادند جنگنده‌های اسرائیلی در ارتفاع پایین در جنوب لبنان پرواز می‌کنند و در مناطق جنوب این کشور بالن‌های حرارتی پرتاب می‌کنند.
🔹
بالن حرارتی نوعی سلاح مدرن است که در زمینه‌های نظامی به‌منظور ایجاد آتش‌سوزی و تخریب استفاده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/445450" target="_blank">📅 15:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445449">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd4d55793.mp4?token=CnuHtL8xz8XzdVlrTSr1Tu7Nmx4uOhjf8j08UT31bq22b_UGAQBuc-D0ShXyYJNfuwl1469KKc6iA9mihAKWk2EGZA3KIC24Bj4q7yCGjyguoEKytzue4RdgkIM2AphjWWU52qixMcxAb428qFHLpDyCJvqf_M5RKR1mKktBWhfdPoQUjY-mUnFPJy-585qKxpnR2vZtcfM_8-Ll33PktoOPsd4xP_vavR-Fii4h4uLKGMbFV9UzFlXQWUpMZVEwIezuj4MwMVqIhv6vR5CA_rOXdDalytTVboz4hNI2fCGO3yqmzZBdKoLUnLzsE0JgAnoz7kOGcLXsylyqT2ffPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd4d55793.mp4?token=CnuHtL8xz8XzdVlrTSr1Tu7Nmx4uOhjf8j08UT31bq22b_UGAQBuc-D0ShXyYJNfuwl1469KKc6iA9mihAKWk2EGZA3KIC24Bj4q7yCGjyguoEKytzue4RdgkIM2AphjWWU52qixMcxAb428qFHLpDyCJvqf_M5RKR1mKktBWhfdPoQUjY-mUnFPJy-585qKxpnR2vZtcfM_8-Ll33PktoOPsd4xP_vavR-Fii4h4uLKGMbFV9UzFlXQWUpMZVEwIezuj4MwMVqIhv6vR5CA_rOXdDalytTVboz4hNI2fCGO3yqmzZBdKoLUnLzsE0JgAnoz7kOGcLXsylyqT2ffPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اردوغان: کشور مستقل فلسطین باید تشکیل شود
🔹
رئیس جمهور ترکیه امروز گفت که ریشه اصلی تنش‌ها در غرب آسیا، مسئله فلسطین است و تا زمانی که اشغالگری ادامه داشته باشد، صلح پایدار محقق نمی‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/445449" target="_blank">📅 15:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNuHHSshby0pNqhApjPoLGyG1lYvzJvuw2oAKAYWjWiqn-IRjbbF2vR6T9MyripsHg8jIkzQF-XpyVrnE3bo0jAMbMVpH3T44TmVUkz3O8H2y_UrdpkAd7WJYib4By6gQ96vcP889OxAoF2bwE7Z0QWXSS9PyXTEZcJKWlwx-ExOwinRNYbebWUVgJW2LjkMtEJ8C5ohrcwy0asBUlLIXR8rG6EwuggpQ2VKHc0hK--1NqmBWjXXoDxDou5Bo5ASVRRCpY6bMAuAVIgO5NtkLASG6e3psAxQz4UYVnIz_OipbavKwZUReLTfezVqd6dtAFuhvgBedV_nbT2JmM6HPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالات خود درباره مراسم تشییع را از این شماره‌ها بپرسید
🔹
مرکز پاسخگویی ملی «ستاد بدرقه» با هدف ارائهٔ خدمات اطلاع‌رسانی و پاسخگویی به پرسش‌های مردم دربارهٔ مراسم وداع، تشییع و تدفین امام شهید انقلاب راه‌اندازی شد.
🔹
مشترکان همراه‌اول می‌توانند از طریق شماره ۹۹۹۲ و مشترکان سایر اپراتورها از طریق شمارهٔ ۰۹۱۲۹۹۹۹۲ با این مرکز تماس بگیرند و اطلاعات خود دربارهٔ مراسم در شهرهای تهران، مشهد و قم را دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/445448" target="_blank">📅 14:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34092159b.mp4?token=uKf4yvAUFakciD_P7Lc8U-xLM-3nJ7r_S5n-wRekjQRsClMkjmY2ZLynDaSf9fTLsFefztzJrl4d-hiTLeqcf8nn3By8BHv4cbczgojb36BtLx2v2rx0SmuXHYqM-FtLyM7wZD_VTGxj5zR3-IqKji0QmI1njuw06srQK1UgB-j4NdsQidEWW1oIcxL5RVmNN2iXyON-xNYVl-Oo1aZPzCzGCfFCF1s1pOWT4yhWOny03S8ViTRhg6wDlu4TTsQvEPAWpxdfZqN3g--CSX1-AWvAPCyB5ZSV4sJx9U4pJs2iG2lCt4bg_NEJ4Pvb-WrUR1vROmi9Q98S6EZdKExl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34092159b.mp4?token=uKf4yvAUFakciD_P7Lc8U-xLM-3nJ7r_S5n-wRekjQRsClMkjmY2ZLynDaSf9fTLsFefztzJrl4d-hiTLeqcf8nn3By8BHv4cbczgojb36BtLx2v2rx0SmuXHYqM-FtLyM7wZD_VTGxj5zR3-IqKji0QmI1njuw06srQK1UgB-j4NdsQidEWW1oIcxL5RVmNN2iXyON-xNYVl-Oo1aZPzCzGCfFCF1s1pOWT4yhWOny03S8ViTRhg6wDlu4TTsQvEPAWpxdfZqN3g--CSX1-AWvAPCyB5ZSV4sJx9U4pJs2iG2lCt4bg_NEJ4Pvb-WrUR1vROmi9Q98S6EZdKExl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متقاضیان عبور از مسیر تعیین‌شدهٔ ایران در تنگهٔ هرمز همچنان روبه افزایش است
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/445447" target="_blank">📅 14:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445446">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">مسافران کاراته به ناگویا مشخص شدند
🔹
اسامی ملی‌پوشان اعزامی در دو بخش مردان و زنان برای حضور در بازی‌های آسیایی ناگویا را اعلام شد.
📰
بخش مردان:
🔹
مرتضی نعمتی در وزن ۷۵- کیلوگرم
🔹
علی‌ اصغر آسیابری در وزن ۸۴- کیلوگرم
🔹
محمود نعمتی در وزن ۸۴+ کیلوگرم
📰
بخش زنان:
🔸
فاطمه‌ زهرا سعیدآبادی در وزن ۵۵- کیلوگرم
🔸
آتوسا گلشادنژاد در وزن ۶۸- کیلوگرم
🔸
فاطمه صادقی در کاتای انفرادی
🔸
فاطمه صادقی، زینب ‌السادات حسینی و سپیده امینی در کاتای تیمی نمایندگان ایران هستند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/445446" target="_blank">📅 14:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445445">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82751071bf.mp4?token=R_ZfXvt7F1DL2k75VUWF-4sibNbWKkry3aTstlhzy1A7r-uXzdWe8zsa4ZBHDYlEG9llD_yJORNlPh3tCSsBYGcfRoS_UWpwNex6RG62cE2LbF4cpQymPVlGJYN0U8OyBH1plPctCZlp-xc1gb7EYQ10d3F8VDEFz81EaMUhEL4i4HQN74Mw3G0wZYWuj14IKFgWs1JOzgwCsRNhSJvyE8RWuu3oJeqviQ8EmD9XuPqcR13wZx76jgN8UbfQws3tJ2mjVjJV0PjBOoB7MP0rSWVYd3nOuH5n4wjFsrfDNkfscu1dUbE2IgDu8rmbLmwDHCyQLfuVckGL-VCBU1BFXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82751071bf.mp4?token=R_ZfXvt7F1DL2k75VUWF-4sibNbWKkry3aTstlhzy1A7r-uXzdWe8zsa4ZBHDYlEG9llD_yJORNlPh3tCSsBYGcfRoS_UWpwNex6RG62cE2LbF4cpQymPVlGJYN0U8OyBH1plPctCZlp-xc1gb7EYQ10d3F8VDEFz81EaMUhEL4i4HQN74Mw3G0wZYWuj14IKFgWs1JOzgwCsRNhSJvyE8RWuu3oJeqviQ8EmD9XuPqcR13wZx76jgN8UbfQws3tJ2mjVjJV0PjBOoB7MP0rSWVYd3nOuH5n4wjFsrfDNkfscu1dUbE2IgDu8rmbLmwDHCyQLfuVckGL-VCBU1BFXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی راهی عراق شد
🔹
سیدعباس عراقچی وزیر خارجۀ کشورمان، صبح امروز برای انجام یک دیدار رسمی از عراق، عازم بغداد پایتخت این کشور شد.
🔹
عراقچی در این سفر با مقام‌های ارشد عراق دربارۀ مناسبات دوجانبه و تحولات منطقه‌ای و بین‌المللی رایزنی و تبادل نظر خواهد کرد.…</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/445445" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445444">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نرخ تورم در خرداد‌ معادل ۵۷/۷ درصد شد
🔹
بانک مرکزی: نرخ تورم در ۱۲ ‌ماه منتهی به خرداد‌ امسال نسبت‌ به ۱۲ ‌ماه منتهی به خرداد‌ سال گذشته معادل ۵۷/۷ درصد است.
🔹
شاخص بهای كالاها و خدمات مصرفی در مناطق شهری ايران (شاخص تورم) در خرداد‌ امسال به عدد ۷۱۶/۶ رسيد كه نسبت به ماه قبل معادل ۷/۴ درصد افزايش داشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/445444" target="_blank">📅 14:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445443">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZpHI9--y_6qL09ljAYRXv8pkOWOpjk1HXRGZ1c4K5jx8CVtRpX_nshIV_sghDziMsgtFliDf1V8kt-Mci6mTnQLrqB_MtosOPiVpxsWMCwcpeSnNnXlhl6TFsNGJe-jLPwUyYeVYdB04oSaKfWXwRoqX7vM2_LMo23vPro8-Zpc77YPmP7-6G7bIlZUotOuZiha1Uz7QUvayPVzKr5WyezyYCoPcEkv9zDEyuHTfS8_m8ia8xP0qKSUt4AX3klqJNCX_xO-Es5bawL1fRSSVMm1MYkJj8o1mJLv7hPwbCG5iIVLe5n3Ww81P4qtYY_PnNcV3wtL4pOk4sRKz6z8Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی: نشست‌های فنی برای این هفته برنامه‌ریزی نشده است
🔹
کاظم غریب‌آبادی، مذاکره کننده ارشد جمهوری اسلامی ایران و معاون امور حقوقی و بین‌المللی وزارت امور خارجه در پاسخ به سوال خبرنگاران درباره مذاکرات کارگروه‌ها در چارچوب یادداشت تفاهم خاتمه جنگ تحمیلی، گفت: برگزاری نشست‌های فنی کارگروه‌ها برای این هفته برنامه‌ریزی نشده است.
🔹
غریب آبادی تصریح کرد: هرچند رایزنی‌ها با قطر از جمله در خصوص پیگیری اجرای تعهدات طرف مقابل، طبق روال، در جریان است، اما خبر برخی رسانه‌ها مبنی بر برگزاری گفتگوهای فنی کارگروه‌ها در دوحه، تایید نمی‌شود.
🔹
غریب آبادی افزود: اولین دور گفتگوهای فنی در چارچوب کارگروه‌های تعیین شده، با فراهم شدن شرایط و پس از توافق در خصوص تاریخ و محل آن، برگزار خواهد شد و رایزنی‌ها در این خصوص از طریق کشورهای میانجی ادامه دارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/445443" target="_blank">📅 14:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445442">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d19d33b3.mp4?token=l7IyCgw6il0lYslHRrwVYPlS6uEhwvrtshj_3ayi8O5lOCTWTMcFyZ7yD4s2ksVFCCWTXoaGdKGxOBuoJaZFLheqgLVP_0eFCysh2GptWi49Zg12Ym7rXppCfGa4MYJAVUfnQr5iCKZn_gLgGJ09ao-YP8IcM1eBFeUoRiN3a_5MiUfr2Dy93XQQcxezVIWhWUbydH7rI2V8YqVuXKbEO_53Yw0ieIjX56DC9QCVkhH0qLIId9Nai5n4Z45532s0VM13Nb4Qkgpw0WULqNnhXyPU3XdUYlrI9I8MOWl9TfWePClcIcYN_5gyEfaWxQ_AT2szYMWGJVYhZdTKv2fKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d19d33b3.mp4?token=l7IyCgw6il0lYslHRrwVYPlS6uEhwvrtshj_3ayi8O5lOCTWTMcFyZ7yD4s2ksVFCCWTXoaGdKGxOBuoJaZFLheqgLVP_0eFCysh2GptWi49Zg12Ym7rXppCfGa4MYJAVUfnQr5iCKZn_gLgGJ09ao-YP8IcM1eBFeUoRiN3a_5MiUfr2Dy93XQQcxezVIWhWUbydH7rI2V8YqVuXKbEO_53Yw0ieIjX56DC9QCVkhH0qLIId9Nai5n4Z45532s0VM13Nb4Qkgpw0WULqNnhXyPU3XdUYlrI9I8MOWl9TfWePClcIcYN_5gyEfaWxQ_AT2szYMWGJVYhZdTKv2fKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظی رهبر شهید از مردم
🔸
صدای رهبر انقلاب در این فیلم با هوش مصنوعی ساخته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445442" target="_blank">📅 13:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445441">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d99a4b228.mp4?token=rwCPmJkmREmjyJptx9I2PY2cgKqif6xLVEoGjwEdQ67Jkm1gzmr2XnvUTkZWlsDNZkC-0XixCYmXOToOELhjJlRYlt5LxfllWrd4mPlfA3qBlxQIJTJE5yY4MrEN1QOLHahamSHOOaiLJ3U8DJgBqo6R_UJf-sd_TznKHK9PReWlNFLFU9c1CGmqODyJDWyAvOzx3pEDPwvmLt5cPz-B2hIQI_q-rIRRKi3dxsxVYsGZ47NwJ6WLazYRFMfnwzSgl5Q4Q9fEXWG9KE39UK_L8A5mdMZxHDWnhEq0RosPmxlehA53cm_BStLWH3EE8mif0BQjMT7kAlNMxeRJX5SrgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d99a4b228.mp4?token=rwCPmJkmREmjyJptx9I2PY2cgKqif6xLVEoGjwEdQ67Jkm1gzmr2XnvUTkZWlsDNZkC-0XixCYmXOToOELhjJlRYlt5LxfllWrd4mPlfA3qBlxQIJTJE5yY4MrEN1QOLHahamSHOOaiLJ3U8DJgBqo6R_UJf-sd_TznKHK9PReWlNFLFU9c1CGmqODyJDWyAvOzx3pEDPwvmLt5cPz-B2hIQI_q-rIRRKi3dxsxVYsGZ47NwJ6WLazYRFMfnwzSgl5Q4Q9fEXWG9KE39UK_L8A5mdMZxHDWnhEq0RosPmxlehA53cm_BStLWH3EE8mif0BQjMT7kAlNMxeRJX5SrgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سد کرج پس‌از بارش‌های اخیر پر شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445441" target="_blank">📅 13:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445440">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAFUuDqwD2xCaPncnUsIzOuEnJg8qz51FIB4OrUWb70hzRA_P_EVqCko3m1xbWj9WTtNR88xcu0bxv7LyMlb3ivndn-HUBVGp2Y9Eds417xTcObI1lVI2tm_HIwRmoRda25wX-j906Z-t7vVBGHN81zo6WmHQX8axpBMMOvCtV_vmJON_wzPOunsGnM6KCdPQCTvKst5OTz2mXtLL8z40-qs7gxVv_LXVt_kPyXRGvG1G4L7LVMB4ANq26rX1HTxOuwA83nveAEZJsKSLAi_KXhwTgT5YxEiCssRprvgBPWADi30jYfVFd1s50hFgQvEt2Rc5NvQfPwA45jKMucaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: آنچه مسلّم است گریبان جنایتکاران را بایستی گرفت و آنان را به سزای اَعمال مجرمانه‌شان رساند
🔸
از خون شهدای مظلوم جنگ تحمیلی دوم و سوم تا صدمات و لطمات جسمی و روحی و مادّی و معنوی وارد شده به کشور عزیزمان و هر یک از آحاد ملّت مظلوم ایران در…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445440" target="_blank">📅 13:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445439">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxC6YZCeQNXbeHM3QVZK2MbLKyepEWMT8q_5zUgHdlPMr4mLl0AN24L66NoYHLCsutfHFAmtHNGRdbe8cZHq0cBImWBkuHEEDoYUfGRXXEEqa6zW_BPfQIBdD08ynsC0z2mYkc2y1Py3Du2LwpoHVzdSF9gMvWYg8Brl1tjbgo4B9nISAiUK1al4Jh901jjzwsAV5AizrkPA8PHNOgfnd8Kqz3uRQQft-NTH2LDpIOj4BU_GR3672FXRqPmahoAPykZ4FxVCy0QZbZOlpZYE8mv9S2n2UKNzjNOSi-25fwKuS-D-hgXYf8UrwvNPgfxk8YylWmq5NpCRSBsUXGN42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۱۶ هزار واحدی به ۵ میلیون و ۵۹ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445439" target="_blank">📅 12:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445438">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
اعلام تعطیلی چند استان در روزهای برگزاری مراسم وداع و تشییع رهبر شهید انقلاب
🔹
براساس اعلام معاون اول رئیس‌جمهور، استان تهران در روزهای ۱۳ و ۱۴ تیر و کل کشور در روز ۱۵ تیر تعطیل خواهد بود.
🔹
همچنین استان قم در ۱۶ تیر و استان خراسان رضوی در ۱۸ تیر تعطیل اعلام…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445438" target="_blank">📅 12:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445431">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CV01SCoJ4VP5qEwdcmz6dYomjg1Gl6wvK5RA2L8rA7MiNY8wVEmUC72I9wKyd4c5ypRTpF1dpayI1JhpUrMcDnXliuRyDdlGzHQB8hDfsDLKZIwLc_11wsOeaMTkvokqKX8xNtfgOWaRu-7Ir8Ir_0Q-woaNGy1ozCH7a8_zwwFwQwTwrMbXz2BLbH965esghZpMdtIxHQTRwksuhDa6G2SfERvj4b1ORHNTQW1PgB4-5hlB1kdpoONsR7SrGWaAH0XNPxV96tAIASocoHFx3OCtzIhTiwL9_KgkBk99odVXqVO8z8TRQ1RsGnU5rYFN9rV_bqX4xgul_gYKbGYnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BM6XrFD6MercRXd_ZrQoaQgy9x546SaW6KKm1GciHA1w8wBh8I229PC4IPe8xbpYFi9OQfGSr-I-Hh3IsFDy-IDYuNZvfvjnfDh_lnWADAluh9boFTK0z8pP2mPz8NZDGMAwZlxsMJrs3UWYOtHowDuP9qoZpDcrU--7HB10dc9_1CVYL5Gz_7XlqopYs4KqFAmsIL2eLhhk4Y9P0ZhCjgA2Tb4pXFOseiVz6SWApGavwdhyp8O1cFsvfEar-hNQ2OkyJfLW5YsyGqCMUgXTP1VlSURKpq_Lc0ONCGlzpYJsH5bFpSvxj2Upnou7mX54eatPLb_5oUr4xafcHwGdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzWj7H01FSFpVVY6vMVsjmWrBdNh7Y2NWjPp43rIx5EzR0RAsKAQgDGMZo_iIfUBDD0U5Jb7qbhZnU4leBOIB3n7sbpiAwlAZ0eSUD81S_d00PCagUDM9e2fAoL9P_FC3Z3EHBvqN4hP65L5i_Dv6_ByVfWYqaUzYxtTmiRDHMfEEEDlwWTftPrmPVcUEX6HD9GLNATI5g9aW0SbEVaqflxwCanKlAPaX8MoJdL6N5GlP0vpYoA5TnuEIPAOvkRDHHwGyz1sEVUDmkoYHI8lT2GhJDibhN9u4yXZrVrxPN64uXN9EnUCty6RquGclV5GwQK4Lw5EQS_1fvtDNo6zjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nbma4PtP14dZGWCCV0aF4ohJDGTXYo0-zKP9BEigPWxZN5oxlvHxSEDWf4mDE5Mew9xRnO6qOEqKF5gqsXN9h921QxYfEl2f7_FD87SAqprNgLuvv4YEB_MG9QVzD4R2ajQ9Mqad8OdciY4th_yFl0LFq0KeN2S5ijEx-61E6f-Fc5tFWThqLecMpP4_IEJ3Zg90v8w3LOr7X9duoq-0RyOOy5A6YxlbTwNbnJwzJE0xCLxAFZieglVV-8k_kiRUCSD5kg9tXZUWh6b0uTlvDQfUuCsAtyuo4gH2xHL6595eWjBK1LmwwJejy0sNLQqpaATdV7wNrXpfgvcfrV0tAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6FyxdDCJ7lPvn_re1Bn_lDaDip-TYu80vz2FiP6uQUpwMjA3HkYHh0xvNq3geXG89veVqOmacmqQjbk0ibQbQd12PobqJml1zhNw2ZUvW-Vou5KIC6UR6R-VTMFKU1ieVV-gvNgJK6fIzmR-M-vI1-xJvjIyOW9KgDpjKcXqdoO2oeVjjUmXO6PZ2yYbGKfC78ybY1-OE44DFMGUZrnhs7ENYWCN0zMtQX8sYXmB2CixmFylQvii2jD51MhOhlF9cKB3zAo9C3FrEkPwCoaSk_iSmWInzqDYzemfcXE3HgQYOD7SkhV4CGaLwQcIQVgpoeEk0EGj6ggvaYg3nNrng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwwKRX1iKJFLftcOCja-p2y7oHYXzn3W-rOlbHJKEnE1eXBB_h0ZgoA0NwNxOfEL7ZWKZS683_yr55mbEMTA_oCQfcRcuXJN1NWAImVIiVBpxTTkXNDTs6VAUDG8dQFtYadPfrXAqQ8CHsabMu0m6qh7zjtHZuJM2OQ6patj5mQQlvcz_jvQsfXf57qvB1nObWoSSCbJ6Y6cSA2UzOzUi4n7_zBGtzbQezz5-Opdy6t5sTVGDsG2RGdaJG7vemI1PZigr_-uHrQ3HK_6nqFDz43lPcV0Y2ku90XjazETnsY1msoz9zecIboF8WkRSatEAImoDnxr-XkeqMCAz4dTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmvXIcwoQFRiBdybleieIsP0QmKQxS7fdCh6Pmelfa-x1cl-Tuyl1XeNLmct3FJ_hLibRTPjkV01uYkuuRNHUhaBXjwIdi1Dy3RK2xOHHS-89e4brn0RZ2h5c8sU5MU6Y09QuuxRil6Ao2WkhOmQcoBNYwxk_6ZvSdDevrlIFQt_eH9mJf1lejL-mdSzd3VWJq8R4SlcT0-c2YKwEl73SJFOQtCQleRBK7E6xWVWMcSyfXDr8oZvHAkqqoSW66d-R24TscO4mF56SG8nYNCVMoMt2pKIUAAI_PpmSybXlakCWkzt9QNSMaWrHJYBIx7vOFervw5YFf_IMmHVgrGQPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وضعیت کشتی‌ها در تنگهٔ ایرانیِ هرمز
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445431" target="_blank">📅 11:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445430">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNiWofSVPWgONHYT0J48gcBxk6ZBC2Qdv9Jj6TV7CmQb9bXTUtUfDM0YBgdTF1EIlNSWxGAtP3Ou7-Crf-ZPX9N9p-PgiMaKMi9mGTEZpVZHYzEn7RnlIGdBod0U9LTooadNpVKimWnbKDQsPV05cG4x81jOd0U3bcUfXUbktTRQ3KuEjYfLrbHRQ8Bq-Vo1-3Xd0aTVQmsBXhOO0_65njKzMlwZ1dfl7QMiAkiiFdmVOzLI1iFa0KI55ghP8gAKE-n34HzMkhb1TXmHHVNMmL9HbGIP9ERKnMwLqPSDuBBiLPpzOVs6LZEVcILZhnB8oqO-IAqXRdM687DjptPrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: باید برای مواجهه با سناریوهای احتمالی آماده باشیم
🔹
رئیس‌جمهور در دیدار با تولیت آستان مقدس حرم حضرت معصومه(ع): سرمایهٔ اجتماعی و انسجام ملی مهم‌ترین عامل ناکامی دشمن در تحقق اهداف راهبردی خود بود.
🔹
دولت نیز همگام با نیروهای مسلح و مردم، با بسیج…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445430" target="_blank">📅 11:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445429">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پیش‌ثبت‌نام حج ۱۴۰۶ از دههٔ سوم تیر آغاز می‌شود
🔹
سازمان حج: پیش‌ثبت‌نام حج تمتع ۱۴۰۶ دههٔ سوم تیر آغاز شده و همزمان این سازمان پیگیر تثبیت نرخ ارز زائرانی است که برای حج ۱۴۰۵ ثبت‌نام کرده بودند اما فرصت تشرف را از دست دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445429" target="_blank">📅 11:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445428">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa9c3ae25.mp4?token=rSmDmRoAXLNj6Zsd6NMneykBzLIDC13pe1d-ZgS18Ny4ZRgHRALa5WOT8bkVm-gmbSnmZe5zpuLPBG55vfDA9x3EZJOG0ugcX3WnhkTD25suas8rekfA7DEtWBnZxfe9jIrR_6D9zxh88yGthHM1OVy9Sg48mGVCFBPSe1jcZyfRzpxioEHs-1Urv2bCbLOuzeRgqYB01PT6qPfYIom9O4kOWaOpx-V9FY6na2NvfrZhPQ32eK-qPje1mUrcZ1hp-NWgddQysbqX5RQEENDQVyR-4ovk73PH3KsgTfpSBeiuA1bPuNJ56uHVPCHyh57J1QXDRVMsHRSJ9_hZXP7zKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa9c3ae25.mp4?token=rSmDmRoAXLNj6Zsd6NMneykBzLIDC13pe1d-ZgS18Ny4ZRgHRALa5WOT8bkVm-gmbSnmZe5zpuLPBG55vfDA9x3EZJOG0ugcX3WnhkTD25suas8rekfA7DEtWBnZxfe9jIrR_6D9zxh88yGthHM1OVy9Sg48mGVCFBPSe1jcZyfRzpxioEHs-1Urv2bCbLOuzeRgqYB01PT6qPfYIom9O4kOWaOpx-V9FY6na2NvfrZhPQ32eK-qPje1mUrcZ1hp-NWgddQysbqX5RQEENDQVyR-4ovk73PH3KsgTfpSBeiuA1bPuNJ56uHVPCHyh57J1QXDRVMsHRSJ9_hZXP7zKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چگونه از خود در ازدحام جمعیت محافظت کنیم؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445428" target="_blank">📅 11:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445427">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده در شرق اصفهان تا ساعت ۱۲ امروز، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445427" target="_blank">📅 11:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445426">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad1a89087.mp4?token=axeagLXN_SaODpfbkDChgwH4YMMveE9796CkgwacDY9Kw9hsUKOVgOHEJtjmmAAOnAxZPD9iKbeaETcVJXwAQOMVbrhoFmXzLjrgzPGfkhO7GhCujQ_z69wXnoNE9a_ys8MQ0HzrmENUuXKo2anN90P3C123SjyDlY2V3f-D4morEO5_aF4SaJExxaTskvkRL7WPk4f7jrRrkO7YFKDQb-7VXQ5jJWiB3IOiLr1ccf3YuDAk2OUpi5gg5hTiJBRUDLtdYZTGqjl4m6JtXBfYCpKTzvMfnlpKbGlQ15UmpWC-hKF9JGPnCVMIsjR5NE0oNm0nVNeVk6uzOn_PHZ40kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad1a89087.mp4?token=axeagLXN_SaODpfbkDChgwH4YMMveE9796CkgwacDY9Kw9hsUKOVgOHEJtjmmAAOnAxZPD9iKbeaETcVJXwAQOMVbrhoFmXzLjrgzPGfkhO7GhCujQ_z69wXnoNE9a_ys8MQ0HzrmENUuXKo2anN90P3C123SjyDlY2V3f-D4morEO5_aF4SaJExxaTskvkRL7WPk4f7jrRrkO7YFKDQb-7VXQ5jJWiB3IOiLr1ccf3YuDAk2OUpi5gg5hTiJBRUDLtdYZTGqjl4m6JtXBfYCpKTzvMfnlpKbGlQ15UmpWC-hKF9JGPnCVMIsjR5NE0oNm0nVNeVk6uzOn_PHZ40kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح آمریکا برای فرار از موشک و پهپادهای ایرانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445426" target="_blank">📅 10:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445425">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مدیرعامل شرکت توزیع برق اصفهان: امکان عبور از تابستان بدون قطع برق در شهرک‌های صنعتی فراهم شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445425" target="_blank">📅 10:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445424">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70548f94b9.mp4?token=TLW1GdQfJk05HPuEKHsy_6Cm0Wu9l8YkiZPzSggIByWHy1sJB3FzOK5G5n8vu6m7nDyJwhlYNUyPXvOZoI5z010PKyGYaNQbzdv4C3CfqkQLfGyciiW6DPQu5mwCHhOFX6Ee3-XrCz9HU7TjMAhHoQMEvWF5JIJx3OQbrXNfDVcPdZDG3n3LRcPZpto4NT4zUljEYLndROJQRLhEESs9-acug2UpoyCkikCUyzPQih6w4Y6C3IEgH6UheNnNzO9Bal6Kq5ImowmjgQ229v_AK2USMDG8err8WvhNlPxjKVbH0bmGiwUpkJx6sjS9cl1iKIEXT46MS-KKEBH1XRqEtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70548f94b9.mp4?token=TLW1GdQfJk05HPuEKHsy_6Cm0Wu9l8YkiZPzSggIByWHy1sJB3FzOK5G5n8vu6m7nDyJwhlYNUyPXvOZoI5z010PKyGYaNQbzdv4C3CfqkQLfGyciiW6DPQu5mwCHhOFX6Ee3-XrCz9HU7TjMAhHoQMEvWF5JIJx3OQbrXNfDVcPdZDG3n3LRcPZpto4NT4zUljEYLndROJQRLhEESs9-acug2UpoyCkikCUyzPQih6w4Y6C3IEgH6UheNnNzO9Bal6Kq5ImowmjgQ229v_AK2USMDG8err8WvhNlPxjKVbH0bmGiwUpkJx6sjS9cl1iKIEXT46MS-KKEBH1XRqEtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☀️
فرصت طلایی حفظ جزء ۳۰ قرآن در تابستان
تابستان امسال، با روزی فقط ۳۰ دقیقه، همراه با بازی، سرگرمی و یک روش آموزشی جذاب، خودتان و فرزندانتان جزء ۳۰ قرآن کریم را حفظ کنید.
با همراهی احمد ابوالقاسمی، میزبان برنامه محفل ستاره‌ها، در بزرگ‌ترین پویش حفظ جزء ۳۰ قرآن کریم شرکت کنید.
🏆
جوایز ویژه:
✨
سفر به کربلای معلی
🕋
سفر به مکه مکرمه
⌚
ساعت هوشمند
🚲
دوچرخه
🛴
اسکوتر برقی
🎁
و ده‌ها جایزه ارزشمند دیگر
📲
برای شرکت در پویش، اپلیکیشن محفلستان را نصب کنید یا عدد ۳ را به ۳۰۰۰۱۱۴۵ پیامک کنید.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445424" target="_blank">📅 10:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445423">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEZpzcFurjHg9Hld-jY_qXzaNOtwtLl_uyU7UgJJjBAWyjJDOOJeknxl0oeEAFypV3QsUldlPP-4dFd_xErGOJyefu2JBMzgp6SJbjYNooIc3rIY0aFDy536-tEWHHV-pekKQ5Ofr8F1oileCgsJmMKSEzyAFYWB9Eo154H0JtZ7BQOdB2TuqPttl5RqKYdXiNChBVY3W0CMk6rRBXc6Tjgb_-dcl_2tDtJTbUn0sATy_iPcJsl0TuUq9TE2c7DWQVIBBpmuELTxW6s5bY_osGhEC9wXiVN7wW7GeLdpxRcTPmveVxR17N-qn1rHWSHgVNOs8YdgI0fxSlyHx2N9Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/445423" target="_blank">📅 10:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445422">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/445422" target="_blank">📅 10:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445421">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcL_Yr24KyYWLutTSbnVdAxhORZQzHuGSlJSr5jRKzznQfeFg4_SvIeC2EEQhzBXL9VqaVlGOP2sjyCkiMv19Uy7D98NYIuJQKqGh5qX5X34kO15E12yV5huy9tRFE2cSh_QOW3Q-nOHyTYUpW6bIuV8olh3C6FxCbC1shKgI-lZe5bGGce3tYrcmU6NCRtPxAlbJWt_ohmHSeOpzc7mhy1y6BIxSu42p47hr0ovvqbQx0fd-RYDi9tl56iAkdRMnkb5XZwBfW2ciG2v48gDK2DZLyhPFO7WbSAgQC37TVTYT43uooZGFNw3O0GAoB3Te0kDskNY5vrShB3lFr7g6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌علت کسب نتایج ضعیف
رئیس فوتبال عربستان استعفا داد
🔹
یاسر المسحل، رئیس فدراسیون فوتبال عربستان بامداد امروز(دوشنبه) استعفای خود را داد اما طبق گزارش سایت سعودی اسپورت این مدیر ورزشی سعودی به تنهایی در ۶ سال فقط در انتخاب مربیان ۱۲۰ میلیون دلار به باد داده است.
🔹
المسحل از سوی رسانه‌های سعودی جزو بدترین مدیران فوتبال تاریخ این کشور لقب گرفت.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445421" target="_blank">📅 10:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445420">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5pvGqg6x3oxHeyhOm2D87Fs4FXDzqvEGCMsB9Vf_ThBLoF2b4FJGryoxjzx9Q45f4z38Sx7Xq1LgYd_cwIYR975MWXgIkJvCW78ON5PBHywgD_xTl3urySjtS2a01cZCneMd-ug1oRqL-9k9G0ntC-AGruVxehB-pLvXUS7QtOP851NrjY5qLBbeOBH9FompQAlTQX0XvL4nT61w2VHxAr1Vtl1689Bz8pVQB4Ig6dwkHN4Ol2OqCADK42yNsQ7o35Jo1dL_IVU9aP5ASS012csgpGLBrZP10aUkrUf1ndmxjQknOdGl81Ut0oU_eSSppHLcoI_KFbyian_8s66MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین نشست کمیتهٔ مشترک ایران و عمان دربارهٔ تنگهٔ هرمز برگزار شد
🔹
معاون حقوقی وزارت خارجه: در سفر به مسقط اولین نشست کمیتهٔ مشترک هرمز با وزیر مشاور امور خارجه عمان برگزار شد که ضمن مرور مسائل جاری در رابطه با تنگه، دربارهٔ مدیریت آیندهٔ تنگه در چهارچوب بند ۵ یادداشت تفاهم اسلام‌آباد و حقوق دولت‌های ساحلی تبادل‌نظر کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445420" target="_blank">📅 09:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445418">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWbO94BobX0vghLgFNL-iZjoRLHPxkg2AC8GQ8csxyTTKRQPENF4kScicNPhEGA__kusyYM-gGf1FbG7L4cxpOhyRay4nr49cUtoYtGBjNZo-eXA-T4z0CmjpIMRF_77wQWPcSMKnJNVvU9a4CFjQtWZ3YJbqmgDtEXhjRyWS9d8ZSmGyBFdLpyj2eExe4Z6Jle0EUzsLP-RKuUENBacwXxk8igEia2Lq5owMQPqNSCP8qkgMXEPOkiUWMvRheXtirQ1GXu9hSS8Q0FpTWqGi-wV4EAxYwwYDXvSOG6MUS4iJiOewclMJrgT2t8Tpv11K2u_WUfTMZqZLorSHb0mvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌کش ۲ منطقۀ غیراشغالی از سوی اسرائیل به دولت لبنان!
🔹
بر اساس توافقی که دولت سازشکار لبنان با اسرائیل امضا کرد، رژیم صهیونیستی اعلام کرده از‌ دو روستای زوطرغربی و فرون در جنوب عقب‌نشینی کرده و اجازۀ ورود ارتش لبنان را به آن خواهد داد؛ روستاهایی که اساساً…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445418" target="_blank">📅 09:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445417">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عملیات زمینی و هوایی ارتش پاکستان در امتداد مرز افغانستان
🔹
پاکستان از عملیات زمینی و هوایی ارتش این کشور در مناطق مرزی با افغانستان و کشته‌شدن حداقل ۲۹ شبه‌نظامی خبر داد. @Farsna - link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445417" target="_blank">📅 09:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNg7keI3MjV-8s6U6afWb-zefmraHGv02kJwUzEVsXrtO1OnB1XEenqA3C35Ca0c80oJMKFoPUp9bjMLA0bdczsewvMf81KL39yF6_j-eGc0dt6X_Bp6P16YEarEyxB47w0vBsmQDjk8jsic0ilnpbkDq44mzAFLkciJPbUwa7I1EL8yb297LTom-ngeMqWH9ghz4gVUlA4konjXBcambhhNRd_EIvLh4FFKBy6B2gTvSbhsdblUALECEywE-y_SGikFoSuZ65u2_Lby65XUm3monueI313pVm7DOQTEaQJE-XVETcCK8h0o5sXxMwHiY-QqvXUrPk_DASGDnIQqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا؛ آغاز ثبت نام زائران اربعین در سامانۀ سماح
🔹
ستاد مرکزی اربعین: نام‌نویسی متقاضیان سفر اربعین حسینی از روز سه‌شنبه ۹ تیرماه در سامانۀ سماح آغاز می‌شود.
🔹
زائران باید گذرنامه‌ای با حداقل ۶ ماه اعتبار داشته باشند.
🔹
با اعلام بانک مرکزی، به هر متقاضی ۲۰۰ هزار دینار عراق به‌عنوان ارز اربعین اختصاص خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/445416" target="_blank">📅 07:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">در این روزها برای ثبت‌نام به مدارس نروید
🔹
آموزش‌و‌پرورش: با توجه به همزمانی فرآیند ثبت‌نام مدارس با برگزاری امتحانات نهایی، ضروری است خانواده‌ها در روزهای برگزاری آزمون‌ از مراجعه به مدارسی که مرکز امتحان هستند خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/445415" target="_blank">📅 06:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUZnta0kVyDK-GY1NsGoBzdGQkPPnOHNAK46FvgwX3AQJ1cZcncgEdFCyHwQ8mbF2KjXyuIZoazEFI0V2ME1QuOb40KOAtQzI6Wj93kv4gcj1WENebaLxgsks7vHLCrDNGueW8L9BDnvik3lLqAiECy2Am7fvHIF6e6Cka9GVCsvzx7Nms1_KKORHH5HT35c9x7yWhYh5FsrW6xoTgSziQytURd6oOQZaVwvb8Q2lqvUi-66DbhbKnA3Ij-xasBEfI8TA5C79sVDbPuNNsmG4Ihc6_dZcLq302ipQrCk9G2FK9N72TnUs3G8IigqPIqOR_P2_w6kKgiUtfO6KLJmYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۴۴۰۰ شهید و مجروح در غزه پس از اعلام آتش‌بس
🔹
رژیم‌صهیونیستی از زمان اعلام آتش‌بس در نوار غزه که از آن بیش از دویست‌وشصت روز می‌گذرد، با تداوم تجاوزات خود هزار و ۱۴ فلسطینی را شهید و سه‌هزار و ۳۷۲ نفر را زخمی کرده است.
🔹
با اعلام وزارت بهداشت غزه، مجموع شهدا و مجروحان از ۷ اکتبر ۲۰۲۳ میلادی تاکنون، به بیش از ۷۳ هزار شهید و ۱۷۳ هزار زخمی رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/445414" target="_blank">📅 05:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">۹۰۰ مدرسۀ مشهد میزبان زائران تشییع رهبر شهید
🔹
وزیر آموزش‌وپرورش از آماده‌سازی ۹۰۰ مدرسه در مشهد برای اسکان زائران مراسم تشییع و تدفین رهبر شهید خبر داد و گفت: این مدارس به‌صورت ۲۴ ساعته خدمات اسکان و پشتیبانی به زائران ارائه خواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/445413" target="_blank">📅 04:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65422d2a3.mp4?token=fCHWZg9MhHB4XkcwsBf1LcMOxjprHEQA6NC4X7aCO4ThiulO0G7x3_8F2hVpgXrdA9URDNOE30NUW8yyaJTRJGFdYKVwrGQ4dh4zCQgsFUVbi4FMaNlGdOT7ma2aNCXma1dZLvmvnKLRqnrfqRDXbE4J9YDS6mFC9GlNWWGYjrrEVCF157NsCfbbprhF2YW1ChLng4mZmIUKFPlOs1Ms5zaHAcEAEz3wgBvF4ZO3xC-KfkDmjkFSNM7rUE3kLvAJfQ_L8eurZPRYsoSBQ11KM5mtGXVXWOioeqgc0t9963NtmTqm9e34GCX3AhjevKT8zo_0W55h10yzsiwDtmWYLnjJEgUvFDtreOEqKeQbxYnufK0-CLJDUTdb1whSKLuxkoEepQdWNkPNjZyjoXS8Jjx65gR7B7HMVmoMgcV5PID7xtqDM7Ywr2ykh-CZGK0Vhux1QMmk1GBTpyR3Y-hq0M1ZOQ4gPL9AHdtygGaQuXa4uhpgnWOz_0sbRrhLKa4A6cT9nBMqd3OKtilcznhE9BG1H1Lw_LT_qeO2oYsbbIQjoFIusYsCpYLFQ5-CZgWpU0qJz9porCdwcL_vvo7-Ov8T0BiBEeTEt3cjN66-t2tM9IWpGQCdsdkXTP9roDa6vmdyWdcq90bGXIKUaSja9RMryZ5jxjxVk_X6Ui2GZL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65422d2a3.mp4?token=fCHWZg9MhHB4XkcwsBf1LcMOxjprHEQA6NC4X7aCO4ThiulO0G7x3_8F2hVpgXrdA9URDNOE30NUW8yyaJTRJGFdYKVwrGQ4dh4zCQgsFUVbi4FMaNlGdOT7ma2aNCXma1dZLvmvnKLRqnrfqRDXbE4J9YDS6mFC9GlNWWGYjrrEVCF157NsCfbbprhF2YW1ChLng4mZmIUKFPlOs1Ms5zaHAcEAEz3wgBvF4ZO3xC-KfkDmjkFSNM7rUE3kLvAJfQ_L8eurZPRYsoSBQ11KM5mtGXVXWOioeqgc0t9963NtmTqm9e34GCX3AhjevKT8zo_0W55h10yzsiwDtmWYLnjJEgUvFDtreOEqKeQbxYnufK0-CLJDUTdb1whSKLuxkoEepQdWNkPNjZyjoXS8Jjx65gR7B7HMVmoMgcV5PID7xtqDM7Ywr2ykh-CZGK0Vhux1QMmk1GBTpyR3Y-hq0M1ZOQ4gPL9AHdtygGaQuXa4uhpgnWOz_0sbRrhLKa4A6cT9nBMqd3OKtilcznhE9BG1H1Lw_LT_qeO2oYsbbIQjoFIusYsCpYLFQ5-CZgWpU0qJz9porCdwcL_vvo7-Ov8T0BiBEeTEt3cjN66-t2tM9IWpGQCdsdkXTP9roDa6vmdyWdcq90bGXIKUaSja9RMryZ5jxjxVk_X6Ui2GZL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدا آقایی و بزرگی تو را می‌خواهد
🎙
شیخ اسماعیل رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/445412" target="_blank">📅 03:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445411">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCvE1P5jku7suR1ImxYUJjuggLrhlPKogqy5kSzxGmYdXx6cwJgO3mMpquoD_rmYOgg2nG_0YN66miTWAkhRAkRCE7q5Hqdmz9YZrWjU2KvZMQD6biEGgy_eztJYNs-seqtPVhJVAHoIRMEg8EzHZ7hz8a2djx4CBKTnEmoVvH6ZBo0FA_mAhqXB9B0puMOICmjgvMXOH7JQeP_sfxYUG5xKr1vUv05d80VYAFQhvF0IxUGqeOdQE_HLMMN3yDn3yZ1GH2rzOecUUlCzXq0ZfW33wO0GWxHNb38SofysG6S8Fa1kEeiq7TpbPYdWuBX--UmmLuD-mFrtUHTVuM6ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش‌مصنوعی جانشینِ کارمندان غول‌های فناوری شد
🔹
طی چند سال گذشته، مدیران ارشد فناوری با احتیاط از ابزارهای هوش مصنوعی صحبت می‌کردند؛ آن‌ها اصرار داشتند که هوش مصنوعی قرار نیست جایگزین انسان شود، بلکه قرار است همکار او باشد. اما گزارش‌های زنجیره‌ای اخراج‌ها در سال ۲۰۲۶ نقاب از چهره این ادعا برداشته است.
🔹
غول‌های فناوری از جمله گوگل، مایکروسافت، متا، دل، آمازون و... تعارف را کنار گذاشته‌اند و مستقیماً در بیانیه‌های تعدیل نیرو، از هوش مصنوعی به‌عنوان دلیل کاهش نیرو نام می‌برند.
🔗
اما چرا غول‌های فناوری به این سمت رفتند؟ شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/445411" target="_blank">📅 03:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌ استاندار تهران: ورودی‌ها و خروجی‌های مصلی تهران افزایش یافت
🔹
به‌منظور مدیریت پیک جمعیتی و تسریع در تخلیۀ جمعیت، تعداد درهای ورودی و خروجی مصلی تهران افزایش یافت تا از ایجاد تراکم و بروز آسیب برای مردم جلوگیری شود.
🔹
در داخل مصلی نیز کریدوری طراحی شده تا…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/445410" target="_blank">📅 03:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عملیات زمینی و هوایی ارتش پاکستان در امتداد مرز افغانستان
🔹
پاکستان از عملیات زمینی و هوایی ارتش این کشور در مناطق مرزی با افغانستان و کشته‌شدن حداقل ۲۹ شبه‌نظامی خبر داد.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/445409" target="_blank">📅 02:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445408">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">معتمدیان: تهران آمادۀ برگزاری مراسم وداع و تشییع است
🔹
استاندار و رئیس ستاد برگزاری مراسم تشییع رهبر شهید انقلاب در تهران: تمامی ظرفیت‌های استان برای برگزاری باشکوه و منظم مراسم بسیج شده و هماهنگی‌های لازم میان دستگاه‌های مسئول به‌صورت مستمر در حال انجام است.…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/445408" target="_blank">📅 02:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445407">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
حزب‌الله: ارتش رژیم صهیونیستی دیروز یک‌شنبه، با حداقل ۱۰ حمله به نقض آتش‌بس ادامه داد
🔹
مجدداً تأکید می‌کنیم که آنچه دشمن انجام داده نقض آشکار آتش‌بسی است که تاکنون به آن پایبند بوده‌ایم. ما این تخلفات را رصد و ثبت می‌کنیم و حق خود را برای دفاع از میهن و مردم خود محفوظ می‌داریم.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/445407" target="_blank">📅 02:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445406">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e6369c7b.mp4?token=V4C7SqPCtSM3RiIWSJ90nMpvgedNEEly1jWtz9YJp08bW8TsQ_Ju3TqpKjDmNxyGv5FBoYP5um77hB4IXL153hdIzmeXK54kv3YRuLQZRWJKUBdvVZu2rses1RXZwqL4QFKLhaV-pPNXcR0z5WcY_giAxmbrcsOz_YaARrbz2skpCHNALWjLqPmIyWXgEqkqnTA_Oi2ariBIg2NcdN5Qpi3woXF8nokIGBFmxsKCNgxnUMwpMeKCpwqBVOxBqU-NvEAIHzx5Qi4ju3p-2J8KJfOKhleRGy0qEnbB2qBfk4In2NoptmP1tde2bLl2M-txHqs0EKGWv_XgU8-F0CPBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e6369c7b.mp4?token=V4C7SqPCtSM3RiIWSJ90nMpvgedNEEly1jWtz9YJp08bW8TsQ_Ju3TqpKjDmNxyGv5FBoYP5um77hB4IXL153hdIzmeXK54kv3YRuLQZRWJKUBdvVZu2rses1RXZwqL4QFKLhaV-pPNXcR0z5WcY_giAxmbrcsOz_YaARrbz2skpCHNALWjLqPmIyWXgEqkqnTA_Oi2ariBIg2NcdN5Qpi3woXF8nokIGBFmxsKCNgxnUMwpMeKCpwqBVOxBqU-NvEAIHzx5Qi4ju3p-2J8KJfOKhleRGy0qEnbB2qBfk4In2NoptmP1tde2bLl2M-txHqs0EKGWv_XgU8-F0CPBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف رضا پهلوی به «عاملیت» در جنگ: کارِ من بود!
🔹
درحالی که پس از انزجار مردم ایران از دشمنان متجاوز و مزدوران فارسی‌زبانش، سلطنت‌طلبان در تلاش بودند تا نقش و عاملیت خود در حملۀ آمریکا و اسرائیل به ایران را انکار کنند، رضا پهلوی به تازگی وارد صحنه شد و با یک جمله همۀ نقشه‌های اطرافیانش را به شکست کشاند.
🔹
او گفت یکی از دلایل عمدۀ حملۀ آمریکا و اسرائیل، حاصل سفر دو سال پیشِ من به اسرائیل بوده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/445406" target="_blank">📅 02:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445405">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaksFw9MAwb-F37X-bIilicOHFvBZUzBIzqUdbvDO86la0I4FE53affm14J1-fvowdffx2Xu92KosYkH6O1nNQM5SdnBqciEwtpl03eA-mh1-olKOADeiMYattZFJ5WN-jE9S1nc8Rr8BDuhU0gZbDfTxq-mZ-Lnb7qyIpDoPwYEDEPLSC_Pxm-VuMSuUvvszVjZtCSVOmLZr2cORqxPRLpoBRb_XWCpsLnDOdJIJz_XVvUmOEhZNxSLxm2hBDkXU_kp6h396CtzFuTGzDv8DFkqHQWS1kDRO0ZOkqkYjFUgjMbPLPsQISXLapgiIB7BJck3_7i092zW-iewpC363w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس صهیونیست‌ها از بازسازی توان نظامی حماس
🔹
شبکۀ کان رژیم صهیونیستی گزارش داد که ارتش این رژیم از روند بازسازی توان نظامی حماس در نوار غزه و تداوم کنترل آن بر این باریکه نگران است و خواهان بازگشت به جنگ است.
🔹
بر اساس هشدارهای مقامات ارشد اطلاعات اسرائیل به رئیس ستاد ارتش این رژیم، حماس هر ماه صدها بمب کنار جاده‌ای و موشک ضدزره تولید، و همچنین نیروهای رزمی جوان جذب می‌کند.
🔹
طبق این گزارش، حماس اخیراً آموزش‌هایی را برای اعضای یگان نخبۀ خود آغاز کرده و تلاش می‌کند پهپادها و تجهیزات ارتباطی را از صحرای سینا منتقل کند. همچنین در حال بازسازی زیرساخت‌های زیرزمینی خود در جای جای نوار غزه است.
🔸
فرماندهان ارشد به رئیس ستاد ارتش رژیم صهیونیستی گفته‌اند، حماس در میدان قدرتمند است، هیچ‌کس تهدیدی برای آن ایجاد نمی‌کند و این سازمان آماده نیست کنترل خود بر غزه را کنار بگذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/445405" target="_blank">📅 01:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445400">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/POa9USSgugTFiC56ppMgHFXtHmEUhmePAhF9n6oyZ58_g9HA4hZknnX9Kpma7etObqD4ancl4oWNH8OwxNOETHjduDcMBvw5_feciIzlecTc_w1fAg-Jjla1ZYfYGPKGlNzGKwPJhNiGo4vCyfbjdiUrdqpY6O2Q0n9ZDd_4xUP3r-QiwVjvSql2wbvruopE1R_pi00awncOa3a2__q_rjpresG3iLm3A9N9opwWunUaMAf6K6TCxsHXytZC_FJQOKsVjBxRvXnMDlCZVtLmu9Gbv7NgK8NvV4MW5qFXE-gvse4qyudikjyLclJecnQc9wB02OBe-qXjZvpmzBmgUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oP_Ja0hGH1aiUda_9Jsw0dnfIC1Sj3O6hAVllsrFNqYMWw-V6vs_c_SX6aBn1-Gc8xfkPVrk4qMC87e3d4KELCxFVZj8lIlJb-6ps7zTI5epDK67vkxOpADVGR_iND73MZ_SPJ7hyKQQz6BwlrWtFkF0u9fNIK2zbCFeRhoPwLlPSgxD43X5byZiBH7CvFzeUesn35pz1u4BijfGLAkIl8WQWwRByZ1I5LuJZyJrCgE7DjCnYsQKpTc4HR5d1oLJ8s1OYlNOd45eBXlC_KkhjqLJCWwwHyEjILXE_2t0MuToDmrpOGVN5UtoJCx0kst7y7V1u8TqgjHQUMBJuHAthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epXSaLeoBvd5fQH1iv7ZhY2GPT1L-pAgPB1Zc6ituYCgqbyeWjtnVudsmc_Hsw4mJF1wAF_JSv_0399RNZMLiH7WVSn0SxA7f_TKfDmxSW-RndrAMnCSIEdrWST0Qwr-vGhcHlhDKfFlBDIPyuRtZEn38YHCQFO_0b58Lrp_Uc-zkjrdyV8ZCBDKnU-vtnwUfcYVb6_qfmyE7b_tVBEFShG-bdMZgf1gaklN6Ze-D6bg9zdfVFtM781PmYgp6SIQK3rE4DhO60mpyNjeWAjzw7dA4PKfwtAVisjagZ4TW0M7UHlFC7bqaiKetL_TkD3NBH89NRtavSD4pB7izf5KrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDE8ZtAvtMabURvItxW0qnMmsSb273K5uXOCOu_pfBfk0XYejUuaUH0JRIXhjB6nCwrX-sj8JgMTaOkK1JDAjBUdXZqIiBQRcz65HML4SfcEuos56Hz36bkmX9FSxG3RLvyWPB5GPsGpOLNpF4f77J3UEGSvzwmGWXigG9AMgYOIBCIITnCAg-vih4n94e3kcpQ_eKAYGHUjHTzqhWEcJPLU1z5IY_ZdWIATsdyg-wPLNi5xw7ALX2Xtw3M-8bDVaCNI-vffpztN2mClmLPPMJxlu0dcWzzxNCo2muEq-_6IjhdhWVJdSRkLZERXTSjGMa4xOIJPr5qrZfB82nxcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PeZjircco0qAh6tNuyTMTPq80KZhqn0NLwClGvZNcmIrv7qhiFFqgmyPC2vJwmiZad1M3k5DFGY9jLbIivb1ohu-ECjy4XMIPmrV6bnxGdoPlor1dHsl_m7BN33o8x8lnmiO2BnaWXQFyZLoLGNkeZMcRSXEhrKCe2vN-wWOG03mB2BZGkai-EO3H13MxwWPGe_8hfl7q3SJn08D7sULzp2MaC5IFTkgUN_sdEbF1Tc2BX9yiiKBntC4wB7S8poNtNbDn6Zf5QhsGCEA5XIRSGFxZ3MWSzilCVi-8FsVQs5IdWEfyNKouvbczYA_mqE5SOcurvGdlYQ6i6jf0S9_jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۸ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445400" target="_blank">📅 01:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445390">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WEOWIsm02lxP_fhPANInAo6QukQ3reiXjODF6UkwlOlLJOmz_1dZUrNNFU7ZUQsif4J2yECVEUDUpTfoQ0HbYesR9S6LJYmsX3VFasGO9VLwiOYF9si19-1ykLNTE-4gtGtqSDuUaU5CGU6yEraZl1zCcZJ2nEtBELpm05UqqLWLDT-28DgSclnH5D_72tjGQ0Ax6qpafOe1IbN_26T2qmM6resFwPCvPGgNgGrwbXzG3a4cpc1QBlss57Lz-FPsm3kyqlChArf4eZ6T9XTcV3ls60C9sNLc9bhrezJMpkelxLxJlkUmu4zLaBTNhgjfjNDiekfvpi78B_qPmCbqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCWt-BChP9YdlPICHmPvFyK-JKpiMf2ikt_SuXTZ3eB8bEJgqx63BZpMGrUMLCxOGCMQiQQBW_eoYlGvdlyBh4dHW9zoKwgtHam9J4CzXo2iHJrWc9mvGStGUvZM2XREIT4rfp-rscI73vuSqPpeePH4HVDnfdKBVA-yEbGGacmv6GOos2T6eLigcFsESf-8ZZXcheJE4M0JH2BTLudXwy_Ro0TqM5cQh-m97fazT5P6cWQNmI54OGAGukVBSDysp5xz0uXWf0A8a2q1RNTQy5mOrQUSOCAb8TKY6PuL7SDXDHb30DEJejcIhObZYXeGIUyPM4CrO_Co1M4fFUc8fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJsrr5p6iWPH4lxytADwWDOeKPvZ5IxcoyFbeShnBf1db3VghQSlTDnXeIGEDF5AVlUlDnf2PRa063Mt-hLpC84zfzgQqX_bJj9m1_7mD4pBPIjVTStCv6S7WyuEK_fMZOSyYaNM5Nz387r9GtGRL-oS1UilTDaARYDbW6VLmXzBh52SYEUIAgYGRfO05Wg6vKG4I9WU4f1vd6lhcRV8F4w2MAnwYOPuhqu19StTFARIxBoY-ptc4T2MTNlUjcrLCqkn4CoU_j8RGNMms-ejsJ1i_PJITsPcPu7pccwm0s0KN8-4yhK8Hau0dSeeNWdo9nPRMiWCUcEO3iNuDUCiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZ5114mcHLG1h9PxvlC9lw9Bs9Z-_7gRcIrwZMJaQBjGCTYfiyeycFrxqjXaN6iQcxCRecPgMGee08Vg2I5iyW3UkvVaM2XssxT--8s2f7KXPJMJy1lLfjImsN6TTgjWUadz8DSAY0COVdY3LsKEJJbJfuwPMg3-EShSSqwVAnF7JWoHp8qrLPBqhAIt1IkZW_GH4mn2DQP_x9_pdEOcR-HPBxHmucnwSWADHSMAf0Ea0_ehTjCTWkvNH71TLUHpW2Oh1WPZp2SNk-pz3ctMoO-TxkRlFUAgCx-zPUyBPkEh7c_OQ4dGXV2ynl3cWqjOhVfYfuHNHhglg-IQZ-ciqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRsyZxlapUjVCa7qtERclwQge9G4rgmoswRMHS69HJ8cXP8Kn1eVvkQ0glwk1CFr1PfQ0_AfJUmS_xApBfCmCRPrvrLJsMum688w4_ZMDvbP4tdTTgp_-sKgfDcogYZch1e16K_nLY_z7C8KtqJM6JHOFg3gVYfa164WCrmqEcGImI2kFoHLD1t83DlvvWYI1uCJgfojPGM33bXR6NgH0vLuSvCajBWzWecmgY_23MRukv8VulKtQq4LRuSOof_8IEDPg7Pc1kU2_te2kSoxocnBDpoEBZQ8C_EEBPZXrd5YRtR-RhADtp7DEJhxqE6aG_7a-qyzHGmWNlKQj_vtWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIW3UZRTBvv7WeHQRcMwgFlTRagCO-INXyeIlkBPkDrORl4bwecqgyh-E3EOJ_P6d6VxjbSaWK1yTbPjdcPi3zpy6-Z4N1X9IXHoEFAcpcTRA605j1nPfmky13JJDzD2JLn5cOgdjqApU0blKgiQ2Oc9rmZTyzxEm_2PRjhPWNwf-QQC1V14PYzxQpDJRT7FvAh9t6pmp_4vHTGpQ0Y84CwSIsJvhNZ7OwgVZONaYTrRz6WXsKhXWvr9jevh7n3Wmnx7E7dmb5HNaNRKQ4dVRHxxfKE8-fsrn_orRw4-rKbnLSoyArdOehPFuuU-Nw0RS97N9qbU25iHPZgnSMzg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZRy5Rp5Y4-_OuR6mGtNjuUF8SvQVcPh-twUW_qSA6Pjh9lPsEMO90a97roL_jyQ2Ey04SI8MD-6QbsoFJ_F-WIhzoP1yXB4uw9gJbeA89nhfyuF3RbQqIZU1fdX56fTdala32RKLLaQHOTpSXAaXG0Pq9MvHfTo-2QTgkDv6ITpIfzeXnyTncrN_IhYsqbpBEDCiaXhfcx2xYWCtZqsQ4rQrqgdCimRitAvcOqn5rI2mmyZy5nX-MxJeCVBKdPYidYaSw7rQmbcB1lskmiHgcdS-KvVkCiMb6OCOH0fFdrrRf8evzINl7Hf8ZplK1qlZIepDcXLofB2qnEkGmwWnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpalknaRO_m_gDTwu7IThu0gcVdkhw-P7ggbAJBBtYHnjSLuj6eZmbmOsGPazeNOtAXDYRsvF-_V-5ffqT3-MOggdrFOJ4_Lvp_hJm6aTKD3JXDJ8udbBZ4dFjZD0jv8rpAdVwyRtoq3FYYktKN9PWSV0rPdwMbdmHnRbUEf59Ad7B0_JDET7DJDKk34hl0915IatFCuaav_Zfhd7RieVLONUpRvL_TSoqyKgpOnEDlz45a9JKdOaOlA3sQU9peYDJJ68SsrYtbSSWLRxb-YTORRmL_QQaZNi6XmzVU28n5A852sn_KxmEToC63gQz-dAPffLZFujFxSn0XueufeKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2aLFqvJo-VLg6RfdsZhdlxgK7r0vncaYxOx-lz1xVu27qUO_1ZfPF7LxjNJg4VviHgp2kUePvdeFAtmfp7cCB2fbICslkRwYVDG9N2CL4rb12-0-WUGRclKzyhz27PPBcuAn0WPEqPa9ILbBplT_KrVV2kWnRoGDLD1zuvSCQu1gnJDiGXX-TnoUlJx5Cr2boE5idlE16UlKg-AjH8LdHVqT-5l1e4ATEspVJRSXwEYhL8r0vCsri4bPei2K1T1hL11saBLoaoqA7bZRDICPE6fbZr57DEx2M29P3OiAdwN6QI_LKcE5vSy4MRy-0hArD6jxezBBdiwJtGtsH0HCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRobVXrnfciKRJxgcqhYpqWDBevKnspQ7DJmWhSapQZMvMIE-Rhd5OngjoBQW4Oi4bHVU4AGHddn4akk188YXjmjSW57Rf6i5ErYpZojuAvXD_oa3LvUjcyZuXsaK6rBvXZYYjBFCcvbzX8PXpE1A0Md92KOoQ2QqvdCoJIyN7TvHAwjNYrjR3lBn3dBOjrmiXaIRN2w7V00E5hF4hvTRzV0eyd1-ES16zxrPybwgRRsW4anAiOBbuRDD71oJPeP7mUrvmErpzYkjUpIClW9ksazHD1KuQXxZlCF5nqlLozbwVrSmGC04NChqOWkLoQmZxs_25n1LcAU5e64ZaYPMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445390" target="_blank">📅 01:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445389">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ4AyXMST-PzpRZ4fjulmvUj1Xj-94KchAcX4od0lqrrnweHqYbC15Nd9LVbRvoUAv1xCwEUeGSokkRhYDRsN7uscKLX7uqHubQejoCtbfWuThHvnJzGCAH4O4Xg--AfRA_QbTo7b6iyiv42TZff16URc32pdTOVlk-Zuud5bDzZuwa2EvOYcHArJqJL9OCL5JuYKx-7U9AnoDMP3nqPpddEBrPb_ZNGFj2DOm0FCbDsqXTe5IayPdaQ1WIdFx01T3gBTwySCgc9hUMT1GN86CuaCH8OXMJVpQaJYD-kJ5pHygChlzyjhQd2nTvuwIFNk8y83OYeUq4wA-lSLm4cDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در دیدار با مشاور امنیت ملی عراق: ایران آمادۀ گفت‌وگو و تعامل بین کشورهای ساحلی خلیج‌فارس برای ایجاد سازوکار امنیت جمعی است
🔹
همه کشورهای منطقه با درس‌آموزی از تحولات چند ماه اخیر، برای شکل‌دهی به امنیت منطقه‌ای که شامل همه کشورهای منطقه و به‌دور از مداخلۀ قدرت‌های نظامی خارج از منطقه باشد، و همۀ ابعاد امنیتی، اقتصادی و توسعه‌ای را در برگیرد، تلاش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445389" target="_blank">📅 01:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445388">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJISdbIweFKg3tyxhyTZxTd4W-K1g-z9fXz6lZWh2q-WtCwqkqdoVubS7v57rOM_e4O2jyqlB58xxR41X1mDXHfJgS0ZSxV6BCYrYZebg4lNQoJfFDtHg6Ttnjb97MN_d0b-DeTQRLqF6AYdnWkEewCIIok45gDc0_2vcSs2c7yY_Typ0KW4tQbxEBGAntytmvvL6hTtQBOeymNYyn0ztC6DBvzTGSsEafJR8LPDp6WIBFGEnQd_I90JJ0XlH2HYqsIZYdeKclg4LNJappG_ZwDTQvP8LwRLsbR9A4vQk3qxDJkwmDoqe-FTV3i4JmYLNWOUX73fGB-lHEeEc6wl8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عراقچی در بغداد با رئیس‌جمهور عراق دیدار و گفت‌وگو کرد  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445388" target="_blank">📅 01:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445387">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_H1NcCwS1lMDEFNmyM1EXaumddr2rThbvbhs3x2gp9F-A35_QUSRHfUWnefyj_SCDiXePlcbIJKsdqyqyndBlyoRiC_ry-asTLLXiFGnC2IdwFMiO3te0L299sPWUQRImgNbnjKUE-fiPxKkPR2KPxt-VePybGTUMnPNPWAiuC--RrH56vQgnMlLyBqYz2kdJk8PKkKLdp_MFTaujEmwXP5EFFwlW125qUjIryVCPo_osj9KiDU4i9rTcbv04566eIyHNj04ZmyISMBa4wbGQVRvhEA7CsZBHjbkROCiRWSsGAOm2iYSu8G6ic_3XhbPDaMLCkGgRGCx-8Td-ZEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معتمدیان: تهران آمادۀ برگزاری مراسم وداع و تشییع است
🔹
استاندار و رئیس ستاد برگزاری مراسم تشییع رهبر شهید انقلاب در تهران: تمامی ظرفیت‌های استان برای برگزاری باشکوه و منظم مراسم بسیج شده و هماهنگی‌های لازم میان دستگاه‌های مسئول به‌صورت مستمر در حال انجام است.
🔹
سیاست کلی بر این است که مراسم وداع و تشییع در استان‌های تهران، قم و خراسان رضوی با اتکا به ظرفیت‌های مردمی برگزار شود و در کنار آن، از همۀ امکانات و زیرساخت‌های دولتی و حاکمیتی نیز حداکثر استفاده صورت گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445387" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445385">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319a000b0c.mp4?token=hgf7HI8ADWlRtZlgoR7uZZ0ABylGdZVhCNZS1aVVElkXkhVIixkCzaVoBMu9AQxNfiUz7Qf9L8vOzba5M1G9KN9Ls3Ib7meTV9R9GlOZkIgSHaDvwbU_tb118tHIkRbzTGj27XGusPU7Ei_Qqnuzr4lMrbWD5nwmaQmGAh8lq_TMK66ff0XCe456Z2Boq3RTzNdFfA_1gIGmvtRxyqSYomZ8Ab18qFjgcpcLqaevslTPOkHlTb0LzwMNpHGdfx37fiocxJT8PFxgcOn2VHeKfjlltdUCLwC4VCLQQNoCXNktTnxI99sXpArJYoeOTHu0PU3HoQVHHsdIsVnkxNGAIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319a000b0c.mp4?token=hgf7HI8ADWlRtZlgoR7uZZ0ABylGdZVhCNZS1aVVElkXkhVIixkCzaVoBMu9AQxNfiUz7Qf9L8vOzba5M1G9KN9Ls3Ib7meTV9R9GlOZkIgSHaDvwbU_tb118tHIkRbzTGj27XGusPU7Ei_Qqnuzr4lMrbWD5nwmaQmGAh8lq_TMK66ff0XCe456Z2Boq3RTzNdFfA_1gIGmvtRxyqSYomZ8Ab18qFjgcpcLqaevslTPOkHlTb0LzwMNpHGdfx37fiocxJT8PFxgcOn2VHeKfjlltdUCLwC4VCLQQNoCXNktTnxI99sXpArJYoeOTHu0PU3HoQVHHsdIsVnkxNGAIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کانادا با گل لحظه آخر به یک‌هشتم نهایی جام جهانی رسید
⚽️
کانادا ۱ - ۰ آفریقای جنوبی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445385" target="_blank">📅 00:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حملۀ هوایی اسرائیل به جنوب لبنان با اطلاع آمریکا
🔹
نتانیاهو و وزیر دفاع رژیم صهیونیستی در بیانیه‌ای مشترک ادعا کردند ارتش اسرائیل ساعاتی پیش یک شبکۀ تونلی و زیرساخت زیرزمینی متعلق به حزب‌الله را در منطقۀ مجدل زون در جنوب لبنان منهدم کرده است.
🔹
ساعاتی پیش شبکۀ المنار نیز گزارش داد که جنگنده‌های ارتش رژیم صهیونیستی شهرک میفدون‌ در جنوب شهر النبطیه‌ را بمباران کرده‌اند.
🔹
نخست‌وزیر اسرائیل ضمن تایید حملۀ هوایی ارتش این رژیم به جنوب لبنان اعلام کرد که پیش از حمله، آمریکا را در جریان آن قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/445384" target="_blank">📅 00:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOUiYK5VK9evRDCZlfnLG0o0ReyxynSorZht7ImtmquaK7d3GigLJeoR1S3sOW0N8BtgF7yWcJsDjTerJYrS3k4S-CPBehyw_w16B3pmqoplGaK1n2P6O7OfPQhiXZ31CBv-juHlHi90skcpJUMgHg8pViQIl7_mFtzHcRkjNYrBr-QHo5bBjw6WzePsgsUYnA1D0v2ayKBEQ6F1jPQPwnt50yBU4jvb9oheEGICSsTq4uUM0-_grpv9HDDBnY80XyDu65H4b9MVZX2Sj9RtBUccgy95n9LHJhIESoaTYwZMzkZjb3Z2X8bIcfGaT7LsY_HIG7ul9woJTxR-oXmJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیراندازی به سمت نظامیان صهیونیست در جولان اشغالی از سوریه
🔹
رسانه‌های عبری گزارش دادند که از داخل خاک سوریه به سمت نظامیان صهیونیست در جنوب بلندی‌های جولان اشغالی تیراندازی شده است.
🔹
در پی این درگیری‌ها، ارتش رژیم صهیونیستی از منطقۀ جولان اشغالی اطراف روستای عابدین در حومۀ غربی ‌درعا را با گلوله‌های توپخانه هدف گرفت و همزمان دو حملۀ هوایی نیز به این منطقه انجام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/445383" target="_blank">📅 00:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۴</div>
</div>
<a href="https://t.me/farsna/445382" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۳ – کتاب آه</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445382" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLr-odsufTQSxFn1InO614zK_1w46tZNHxIbe-Hay70UEA9M8UcWnTb4dOGpFG2y6Z3FVSuRRTzrZtcx0oPD_Giebkm5gjKgVi1Lv3BKBmGRequ9lB-ilGCH7IQ5WBQQk6cwE9Mo7N9lY_vLlowGIcZLvNi70IWFXtcFReFvASZui1_nOzGSfrtv-SfjHEKUgEGn6X-RCEFKqLfVe1NHvXm5E1Xp-PQTqADtxkxtFV7S_ftN5skwsHOgGW7pjp-ai5iPkZlIeAobbb_0kI8PQFFv_I3h4XO2VEAnrQ766TgYe1m3fkQrmQ-gLndyqygTXEdy2UJpLyBeJ7bV_ss0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت خودبزرگ‌بینی
🔹
«بزنطی» که از محدثان بزرگ زمان خود بود، نقل می‌کند که روزی امام رضا(ع) مرکب خصوصی خود را برای من فرستادند تا به دیدار ایشان بروم. من سوار شدم و به محضر امام رسیدم. آن شب تا دیروقت در خدمت ایشان بودم و از علم و دانش امام بهره‌مند شدم و سوالاتم را پرسیدم.
🔹
شب به نیمه رسید و من در دل خود فکر کردم که وقت رفتن است، اما امام(ع) به من فرمودند: «ظاهراً دیر وقت است و رفتن به شهر برایت سخت است؛ امشب را همین‌جا بمان.» من با خوشحالی پذیرفتم. سپس امام شخصاً برخاستند و بستری برای من پهن کردند و فرمودند: «روی همین بستر استراحت کن.»
🔹
وقتی امام از اتاق خارج شدند، موجی از غرور و افتخار وجود من را فرا گرفت. در دل گفتم: «من چقدر نزد خدا و رسولش مقام دارم که امام زمانم، مرکب اختصاصی‌اش را برایم می‌فرستد، ساعت‌ها با من هم‌نشینی می‌کند و بستر شخصی خودش را برایم پهن می‌کند! هیچ‌کس به اندازه من محبوب و مقرب نیست.»
🔹
در همین افکار غوطه‌ور بودم که ناگهان امام رضا(ع) دوباره به اتاق بازگشتند. ایشان بدون مقدمه، دست مرا گرفتند و فشردند و فرمودند: «ای احمد! امیرالمؤمنین علی(ع) پس از عیادت از یکی از یارانش به نام صَعْصَعه، به او فرمود: ای صعصعه، این که من به عیادت تو آمدم و به تو احترام گذاشتم، مایه افتخار و مایه امتیاز تو بر دیگران نشود و با آن بر برادرانت فخر‌فروشی نکنی؛ این تکلیفی الهی و اخلاقی بود که من انجام دادم.»
🔹
بزنطی می‌گوید: با این کلام امام، تمام آن خیالات و غروری که در دلم ایجاد شده بود فروریخت و فهمیدم که رفتار امام از روی تواضع و اخلاق الهی بوده است، نه مجوزی برای کبر و خودبزرگ‌بینی من.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445381" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkX_HBTgNYftvujp48kl8EAjFhU5ZSdGNRGVpjkIOKvJ8DccQRtbCyyjV4lBrw7QhxMfwJ3wtZH9HBo8gtd4J7tneRzzhpO44qfH-_UUPiuG9_KxjlE_LiLOznUr3gYqfMalv-KlwNpbvUuZShIQwEHO23pkHahsIvKLA3Ptz0L04-v0TlLfJtMUPdPXMU3gX98BhHW7e-NsuUQ5Gz4twTuTmiCDuZpUt_OeTGLYh46YfnePZfPOfHJwl1PFFPnUHmJubVejQsDTIHmOCQQo0SRqU_DVLWucz6b9lARALrC7KxS_F2mB8tNc-3yvi49A_dXQE-RNmJJeX8-2tPzr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد دانشگاه شیکاگو: جنگ ایران توهم آمریکای شکست‌ناپذیر را پایان داد
🔹
رابرت پیپ: ترامپ اکنون ناچار است که با یک واقعیت مواجه شود؛ ایران به وضوح در موقعیتی بسیار قدرتمندتر از ۱۱۶ روز پیش (قبل از جنگ) قرار گرفته است.
🔹
شما شاهد این خواهید بود که جنگ ایران تأثیر شدیدی بر محدود کردن آمریکا به عنوان یک قدرت بزرگ در بسیاری از مناطق جهان خواهد داشت و دیگر کسی آمریکا را شکست‌ناپذیر نمی‌داند.
🔹
وقتی که ما نمی‌توانیم از پایگاه‌ها و ناوهای هواپیمابر خود در مقابل ایران محافظت کنیم، تصور کنید که ما در مقابل چین چگونه خواهیم بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445379" target="_blank">📅 23:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvYzMj8Y8p-GlyKXW4fsIdCrq8vfBCA7SXShZxGs1i5oyrAGaLV2_PtYSDDfVD3UNtQoSytkQdnlway1BDrvLBW1L5Wsrx2sF7EI3h0iSLYPzoXxR_5S6uA4AZI3dTt1wmbzRQyZrULALZ1Sbp6Eq8IzbOiJZIDgybMzW2AMMt0DzVayVCFu1ClS9G0LnPFQYmbQ6K2KEbJ5avalbNhyTL_JZJlumMjI_xeAdekSBdLxpy2jQLhzQQq2iquIvavRs9mDrke02EbglQ_8R587BgFTHIHQ8qXPX_xHvX_emEetkHlQS7WBCph_Rsm8RM4f_PlF8hnXWIa5nWVtk4wF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقچی: در تنگهٔ هرمز دخالت نکنید و به یادداشت تفاهم پایبند باشید!
🔹
براساس یادداشت تفاهم، تنگهٔ هرمز تحت مدیریت ایران طی ۳۰ روز به ظرفیت قبل‌از جنگ برمی‌گردد؛ هیچ کشور یا نهاد دیگری دراین‌باره مسئولیتی ندارد و هر دخالت یا تلاش دیگری اوضاع را پیچیده می‌کند،…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/445378" target="_blank">📅 23:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445377">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b382afadf4.mp4?token=P1vSHVFXR8oydGiNzBEZiL1QJkx_k3EAxeyCZ3MsK-W6Rl0MkGqkb2sIMruAjJI7xQkWKdRD6J23GSRKgWxm1Pl5zTedMd2NpxE0JRIDCPBtR1mPGuoduMiFXFk92VxKRw3qeA_8AgF1aqt7YvyJmmsZ_JwDVcDNjqtbWxUb_f3m6EYxP5Ora11b1HbhuoodaXV80TKvucD_rRQKOSxXiI3UXKGx-prkvEJLJ_nRN1s5pxA-yWn8As92WmHPgKkkSUY0LqE7L4gQIEBG6UIqEh5h3yK54YWcmqjM3XGZBK4u5kmCQ_lFKajqNRwJzcoeStPjHBsf78tQ_S4iTk0q8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b382afadf4.mp4?token=P1vSHVFXR8oydGiNzBEZiL1QJkx_k3EAxeyCZ3MsK-W6Rl0MkGqkb2sIMruAjJI7xQkWKdRD6J23GSRKgWxm1Pl5zTedMd2NpxE0JRIDCPBtR1mPGuoduMiFXFk92VxKRw3qeA_8AgF1aqt7YvyJmmsZ_JwDVcDNjqtbWxUb_f3m6EYxP5Ora11b1HbhuoodaXV80TKvucD_rRQKOSxXiI3UXKGx-prkvEJLJ_nRN1s5pxA-yWn8As92WmHPgKkkSUY0LqE7L4gQIEBG6UIqEh5h3yK54YWcmqjM3XGZBK4u5kmCQ_lFKajqNRwJzcoeStPjHBsf78tQ_S4iTk0q8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۰ شب، ۱۲۰ سنگر در شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445377" target="_blank">📅 23:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445376">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f17b33ff1.mp4?token=nrqXQi6qLc9cFHsXRV2MOk8tc8eGitoePBkwxQQ_a-Acz_2bBqmNBb5Q_pqPNF5NWR0oV6PwIllSUBNwSSQzRNCBqQxzTTMF6qa2g1TZg7_EzvUJ3p7diQhzBot0BE7wpBcc7H8qVvWITL_5MUz6Xv4NFYibBTybcSmKEEOfrXDNhru7g2o2w70dVsMsRp_twbT65YcymBXftaWu8AaWWLsOWBsdy20sbypf02qUfRPh0z7UJG8B4pSDtyLXQt2pQsHHOI8fJb1sJEB-9oDLCMORWgC2dOUqix4OqlFAO70Ydl5B0Vgz0z0qpp-YjSJFqwHfZ3cQ4ULqpAYIGe4-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f17b33ff1.mp4?token=nrqXQi6qLc9cFHsXRV2MOk8tc8eGitoePBkwxQQ_a-Acz_2bBqmNBb5Q_pqPNF5NWR0oV6PwIllSUBNwSSQzRNCBqQxzTTMF6qa2g1TZg7_EzvUJ3p7diQhzBot0BE7wpBcc7H8qVvWITL_5MUz6Xv4NFYibBTybcSmKEEOfrXDNhru7g2o2w70dVsMsRp_twbT65YcymBXftaWu8AaWWLsOWBsdy20sbypf02qUfRPh0z7UJG8B4pSDtyLXQt2pQsHHOI8fJb1sJEB-9oDLCMORWgC2dOUqix4OqlFAO70Ydl5B0Vgz0z0qpp-YjSJFqwHfZ3cQ4ULqpAYIGe4-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع نیشابوری‌ها در شب صدوبیستم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/445376" target="_blank">📅 23:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445375">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
حملهٔ هوایی اسرائیل به جنوب لبنان
شبکهٔ المنار: جنگنده‌های ارتش رژیم صهیونیستی شهرک میفدون‌ در جنوب شهر النبطیه‌ را بمباران کردند.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/445375" target="_blank">📅 23:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445374">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976c416f95.mp4?token=HMy2WaHS26b6kYAnTcP1gCCUX1gdU3FB41toyRNeH2vuszXnEI9VXis610usF2yEFT3XgFMIJkx7TTnWvz_0vTQ53ECTjHJbJcOJPRcyZoaoPUimbiZNh68g73_jeSV8zDJJtaklbqJtuUyQM7linCrbpCga3gBEkDmPnv5idbvCRQXtFBAJvLMwQVcqjlY5v9sIOQDAK3mRxvLMzaACADJcvu2VOsP0Qebg8pC4O4KeGApjy2ScPf2WGQqirVJQYkeij8QanVDfKGY6oabP541MFO22kcgeB4OIJK0p9WMa27jrODPNlnCmQUF_4qX6xN5JLNpf1owIo48cJqKeBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976c416f95.mp4?token=HMy2WaHS26b6kYAnTcP1gCCUX1gdU3FB41toyRNeH2vuszXnEI9VXis610usF2yEFT3XgFMIJkx7TTnWvz_0vTQ53ECTjHJbJcOJPRcyZoaoPUimbiZNh68g73_jeSV8zDJJtaklbqJtuUyQM7linCrbpCga3gBEkDmPnv5idbvCRQXtFBAJvLMwQVcqjlY5v9sIOQDAK3mRxvLMzaACADJcvu2VOsP0Qebg8pC4O4KeGApjy2ScPf2WGQqirVJQYkeij8QanVDfKGY6oabP541MFO22kcgeB4OIJK0p9WMa27jrODPNlnCmQUF_4qX6xN5JLNpf1owIo48cJqKeBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شمر زمانه را بشناسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/445374" target="_blank">📅 22:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445373">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54c4b3eb9.mp4?token=uIMAbIekj7jsWBnU2Nez3h2dqMxxO7rGbBKNN2-YdoxwCPxElDOD3JE2eZugtBBk8uHCpbSqJGzB3oAZd-HkkkVoO9mhdWu35s9SoLS097D97AYiBPX0Z-RYhUIX3qX0GB1orMWyNb-53anfy1tLjafsVd3HTEQ9at5jV0a47953NUjD7zRNA3MZCvhtVyqxIj73SeK7lp1Z5RUQSCQzR_gWECVNyVUO_zZDJtc5virVDE6r9KxvLdClj6NF2MYTQexuuDTbUEDicInQLkspANqkcsGAxEPF57ohmtvs7K0MAo_ygqbTFgZhPzTHOkmuLVVq5BdQh_HDPO3BCcdf_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54c4b3eb9.mp4?token=uIMAbIekj7jsWBnU2Nez3h2dqMxxO7rGbBKNN2-YdoxwCPxElDOD3JE2eZugtBBk8uHCpbSqJGzB3oAZd-HkkkVoO9mhdWu35s9SoLS097D97AYiBPX0Z-RYhUIX3qX0GB1orMWyNb-53anfy1tLjafsVd3HTEQ9at5jV0a47953NUjD7zRNA3MZCvhtVyqxIj73SeK7lp1Z5RUQSCQzR_gWECVNyVUO_zZDJtc5virVDE6r9KxvLdClj6NF2MYTQexuuDTbUEDicInQLkspANqkcsGAxEPF57ohmtvs7K0MAo_ygqbTFgZhPzTHOkmuLVVq5BdQh_HDPO3BCcdf_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۰ شب همدلی و ایستادگی گرگانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/445373" target="_blank">📅 22:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445372">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام بقائی به تیم ملی فوتبال
🔹
سخنگوی وزارت خارجه: آفرین به تیم ملی فوتبال ایران که یکدل و متحد، «هدف» را نشانه رفت و اجازه نداد فشارهای غیرانسانی نامتعارف او را از «دویدن» باز دارد.
🔹
در روزهایی که فشار، تنگ‌نظری، تبعیض و محدودیت، ادامه دادن را دشوارتر از همیشه کرده بود، تیم ملی فوتبال ایران نشان داد که پیروزی، غلبه بر تفکر تسلیم و ناامیدی است.
🔹
نه محدودیت‌ها بهانه شد، نه فشارها باعث  تسلیم. به دل خطر زدند، دویدند و تا آخرین لحظه امید و مهر را با اخلاق و رفتار ایرانی خود روی زمین سبز زنده نگه داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/445372" target="_blank">📅 22:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445371">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسلوونی: جنگ آمریکا و اسرائیل علیه ایران اشتباه بود
🔹
رئیس‌جمهور اسلوونی: باید گفت‌وگو درباره یک سیاست دفاعی مشترک اروپایی آغاز شود و وابستگی به آمریکا کاهش یابد.
🔹
جنگ میان آمریکا، اسرائیل و ایران یک اشتباه بود و فکر می‌کنم ترامپ این موضوع را فهمیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445371" target="_blank">📅 22:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445370">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
در ۱۲۰ شب حضور، مراغه ایستاده برای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445370" target="_blank">📅 22:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445369">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9arJN-w4dhMGGfDily05LiRhrahToUzab8FFrE5dTrH3fn9cBplgTyD4QUyMpBwLlzbdZgQQmcS28lJPhqYr3ADUBzIRekJjR1BXhfiJ6lPTolnDIU8WnALUEurrbpy1_UHY5gVYZw9EddQfni8DGnpNxX3qANL3tNv27tyPXi5YRaHKMiVrBGkUyjkh45asxPCvkPlgw56tluLZVmkdHko8THUMa74TwrbyuNcAAfZ1A72Fya89IRkkA5OUj9zCTq26CAdu0RKbi3kaQYJ4OaoAPfHR4GuYTY6MzkzjmkAJHHWKQTT8IhhCYEWHRW4n-2elw3AZSYfL0Afh51Rcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاندار همدان در دیدار با مدیرعامل بانک شهر:
🔻
توسعه همکاری با بانک شهر، شتاب‌دهنده رونق تولید در استان است
🔸
استاندار همدان با اشاره به ظرفیت‌های گسترده این استان در حوزه‌های تولید، کشاورزی، گردشگری و صنعت، بر ضرورت گسترش همکاری‌های بانک شهر با بخش‌های اقتصادی تأکید کرد و خواستار توسعه خدمات بانکی، ایجاد خط اعتباری ویژه و افزایش حمایت‌های مالی از واحدهای تولیدی شد.
🔸
به گزارش روابط عمومی بانک شهر، حمید ملانوری شمسی در دیدار با دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر، با اشاره به نقش نظام بانکی در رونق تولید و توسعه اقتصادی، اظهار کرد: استان همدان با برخورداری از ظرفیت‌های قابل توجه در بخش‌های کشاورزی، صنعت، گردشگری و خدمات، برای بهره‌برداری حداکثری از این ظرفیت‌ها نیازمند پشتیبانی و تأمین مالی مؤثر است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445369" target="_blank">📅 22:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445368">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIUIlmk6Kh3S2HWdSKslZmz5WZe8zjVghjOMrAxsknBs0lKySZOieapGcDU15rHqOQtvJ05SQh_Ii59wxu1_qvKDz_Z0wBJXh85EihHxSjhFJ7loJvgf0FO2Eb5qf1ajRR4MyPJ7PzbVUogafQphPb2bbr7xJmGT5OeRRJ0rZeS8wiusg48VSxlPr7zcguXnvMNh0hGy1guvNUHoZfNvPa-x7bsxaadt_QMW1nRfs7cTOLWZNw-CnC5L8GBNg5AhHbxNhs4MzHB17uSdnjOdmMzXfbaMrhzn9WP2eMzb2h0iaPCV0iZIyE45f3g0FcL_P2UxQ_kvf7bWhRuUvNpqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
فرصت‌های ویژه اُپارک تا ۱۸ تیر!
✨
با خرید آنلاین بلیت، ۹۰ هزار تومان هدیه خرید دریافت کن.
🎡
بعد هم گردونه شانس اُپارک رو بچرخون و شانس برنده شدن:
🎮
PS5
🏊‍♂️
اشتراک سالیانه اُپارک
🎁
کدهای هدیه خرید
رو داشته باش.
هم از هدیه خرید آنلاین استفاده کن، هم شانس بردن جایزه‌های ویژه رو از دست نده.
👇
همین حالا وارد سایت اُپارک شو</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445368" target="_blank">📅 22:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445367">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445367" target="_blank">📅 22:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445365">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d5000e52.mp4?token=HNpM69vIJTynnuFe7WxxSiQEsSLcV9CPA6TlLiNz47k9su28HobYU9U8oAtRmqaFhY38DX69zcGQyvjOJ79fU46yiPSkNxYMSlnDGz1gWqirL2_dADf3xXIevCzD4oA5zH4FSu0Vd4INb1Emu2Ge914z89WzuoXKi4D1tQ89iECv-xs9VJMSXi_6QCV8HDAXY7OpK149xFxP4_hnc8UDxvNTQ4NwNo7g3-D5pEoEoZEaezq3WxajvMvU5Tf64yrrWD73F7kmsdGpOkTfh7mP6VyLK9MqxxRnRiOw0JpdDM6gknr5vNkuisiIdUQXYTH1ZYiFQk8wFc3z2S1-hxEvEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d5000e52.mp4?token=HNpM69vIJTynnuFe7WxxSiQEsSLcV9CPA6TlLiNz47k9su28HobYU9U8oAtRmqaFhY38DX69zcGQyvjOJ79fU46yiPSkNxYMSlnDGz1gWqirL2_dADf3xXIevCzD4oA5zH4FSu0Vd4INb1Emu2Ge914z89WzuoXKi4D1tQ89iECv-xs9VJMSXi_6QCV8HDAXY7OpK149xFxP4_hnc8UDxvNTQ4NwNo7g3-D5pEoEoZEaezq3WxajvMvU5Tf64yrrWD73F7kmsdGpOkTfh7mP6VyLK9MqxxRnRiOw0JpdDM6gknr5vNkuisiIdUQXYTH1ZYiFQk8wFc3z2S1-hxEvEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمعات شبانهٔ مردم بجنورد ادامه دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445365" target="_blank">📅 22:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445364">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL5Z42SKLjOzlXH1q5z-Rt-VFQXSe82H_zwYWsAFTk4ZpHBfTtOodwY4fDi-TJGvbF72N3UZuOwge3ix7O6U9Lu7f6dfzJPp1s6c_0gk80uB7-2l1pWXKewTQhpPSuqDwNei0kfyWCNEQO6NTSrqJJWQaaBpJZoBN7xJDJEYU4d6OF1_2mWQAGCDDMCwn7JMs_2MNQSaDaEubMwO67UxAy-SrICrswW45PVC899J0AO8nRO4MBh2Rzb4f_V33yl6pP-AADS0bgewk5DF9qxR5Bm1RsHFMC1P3aF3zrp93OziG5xwMO_j5BBD0RLQVQGr2r2kCpEOgv13Irl1T5jnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس دفتر نخست‌وزیر عراق: برگزاری مراسم تشییع رهبر شهید ایران در عراق و عتبات، افتخاری تاریخی برای ملت عراق است
🔹
دولت و ملت عراق از هیچ کوششی برای برگزاری باشکوه مراسم دریغ نخواهند کرد.
🔹
آیت‌الله العظمی خامنه‌ای(ره) جایگاه رفیع و ممتازی داشتند و خدمات آن رهبر بزرگ برای امنیت و عزت عراق و جهان اسلام ماندگار است.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445364" target="_blank">📅 21:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445363">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
سلام و ارادت. بانک ملی از روز ۲۴ خرداد تا به الان پول‌هایی که بابت فروش ماشین برام واریز کردن هنوز به حسابم واریز نشده. با توجه به اینکه بنده ماشین تحویل دادم و قرار بود پول واریز شود واقعا نمی‌دونم الان باید چیکار کنم. مگر می‌شود دو هفته پول ها معلوم نباشد کجا رفته؟ هرروز می‌گویند درست شده ولی فقط شما می‌تونید وارد سایت بشید نه پولی میاد نه پولی می‌تونی انتقال بدی.
🔹
کارمند قراردادی پایگاه سلامت برون‌سپار هستیم، حقوقمان ۳۲ میلیون تومان است ولی هزار بهانه می‌آورند و پیمانکار کم واریز می‌کند و برای بیمه هم ۱۰ میلیون تومان کمتر رد می‌کنند، اعتراض هم کردیم، جوابمون اینه که هرکسی ناراحت هست برود.
🔸
متاسفانه در شهرستان بوانات پیگیر مسکن ملی نیستند و به هر کجا مراجعه می‌کنیم می‌گویند به راه‌وشهرسازی مراجعه کنید، راه‌وشهرسازی هم می‌گوید به بنیاد مسکن مراجعه کنید.
🔹
از زمان افزایش قیمت بنزین هنوز سهمیه‌ای که قرار بود بر اساس پیمایش به رانندگان اسنپ پرداخت بشه اجرایی نشده، این سهمیه جوابگوی ما نیست لطفاً مفصل پیگیری کنید.
🔸
آموزش‌و‌پرورش تکلیف این مدارس غیرانتفاعی را در شرایط جنگی اعلام کنه چون با بدبختی هزینه می‌دیم اما آنلاین هستن.
🔹
من و همکارانم مربیان پیش دبستانی ضمیمه دولت هستیم که ۱۶ ساله داریم در دورترین نقاط در برف و بوران مشغول تدریس می‌کنیم. در جنگ و کرونا هم تدریس تعطیل نشد چرا وزیر آموزش‌وپرورش قول همکاری دادن اما الان انگارنه‌انگار! به خدا ما هم زحمت کشیدیم.
🔸
خوانسار تنها شهری‌ است که کمربندی ندارد و کامیون‌ها از داخل شهر رد می‌شن. لطفا پیگیری کنید.
🔹
وضعیت زائران در پایانهٔ مرزی مهران واقعا اسفبار هست اصلا اتوبوس تو پایانه نیست و هر کسی برای خودش یه قیمتی می‌ده لطفاً به داد مسافران و زائران برسید.
🔸
وضعیت اجاره‌بها در شیراز و استان فارس به یک «بحران» تبدیل شده است! ما مستأجران، زیر فشار قیمت‌های سرسام‌آور و بی‌ضابطه کمر خم کرده‌ایم. متأسفانه جولان بنگاه‌های املاک و قیمت‌گذاری‌های سلیقه‌ای، آرامش را از خانواده‌ها گرفته و خطر آوارگی هزاران نفر را تهدید می‌کند.
🔹
بی‌زحمت از وزیر کشور یا رئیس ستاد انتخابات پیگیر زمان انتخابات شوراها باشید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445363" target="_blank">📅 21:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445362">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0SnDr4p9ZnZ3nD_9oKL34oTZl0zO7CL8ERGEnxz09Zq_5650VtrbRh5Nfnj9bE3KJSP5tjRNDvvdvjsDoZxzzKRj1VEM3ZiWG-kiyIqb6CIQaDRIft289tqAWiCpqtccMZIxDEq5G3bhXVZTGZo7lfC6Tn0PA3swZKJmh-OSbIqnacUJ_A5e-snq5SN4yGJRtnqLSAYPg-Y6MI2xZOt2JaT-a-yFIMKYgyU8s-8EdKRfT78yr3T0zEl9_ToMCW7HAerg5Fs3xzH8o6OOmXEQym-VrGjULgLurXqpr9qPDDfz6E6YNztkkb1BtmBTlVKYqj2BWCxGkadHiYubsd80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جای خالی یگان تخصصی در نبرد با آتش
🔹
آتش‌سوزی گستردهٔ منطقهٔ بدیل بهبهان از شامگاه جمعه در تنگهٔ بالنگستان آغاز شد و به‌دلیل گرمای هوا، پوشش گیاهی خشک و وزش باد تا نزدیکی روستای پشکر گسترش یافت.
🔹
این آتش‌سوزی پس از حدود یک روز مهار شد، اما جان‌باختن یکی از اهالی روستای قالند که داوطلبانه برای خاموش‌کردن آتش وارد میدان شده بود، بار دیگر نبود یگان تخصصی اطفای حریق طبیعت را پررنگ کرد.
🔹
سردار رستگار، فرماندهٔ یگان حفاظت محیط‌زیست می‌گوید: پیگیری تشکیل یگان حفاظت محیط‌زیست پس از دستور معاون اول رئیس‌جمهور وارد مرحلهٔ جدیدی شده است، اما هنوز به مرحله اجرا نرسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445362" target="_blank">📅 21:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445361">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUBMz1qUiWn7k49Bl2Y9cddz_KcyWeSe00bSW5ryRqL-8oX5yMw-QipQdBpIu-q7La8KVvy1qsKKbiWtfYc9GNuyNJ2BSyqBm_GHu7FHE2jyNMV7QRGfwB3-NOQx6yizUXmXH-NOcNpkjrp-uSMKOcTiJino_RovJgK008zY__HDMHfGAFpJgI61p5SnY7m33NKWDOP9o0vbC6NrhlH0gSQHGfAQUhbns36ljcAk_Q3fQeBFnYGnmvPZgiJSzp2aB2eMDYNb80-gyWExrvdvnt4CWjzOH8mnfHA9WAyV09ad5-0gsFOoRO1GY1mJZ6bhrgMDDaP0_FLK3P5Y2mOGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در دیدار با نخست‌وزیر عراق: همهٔ کشورهای منطقه باید از استفادهٔ طرف‌های متجاوز از قلمرو و امکاناتشان برای حمله به ایران جلوگیری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445361" target="_blank">📅 21:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445360">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df4abcf2c.mp4?token=M0DHepLNdkZVVaJfdZt5rx1WobWc3YF9pvdldfVAixvJuTu7LF4HO0cIcWuCx7yhm5va4Eq-0cT0bi865tpM6yS0CNWsJ3UPiL8qvHRv6Kv2lezi98p9hIwzQagyeYvBLrWar9Ogo_75xe55n9v3JlvNLtoTYS0DQZMLOkLKpg8bI1bKR7E2rSmyRiKUwKBu3AJ44Pc_Uk30fyDvVzFtI1wlp8fvHz7azx4qV5XqBbzPk-ZObMHW7FVwTKqd7GsceJAYD2OzlNPLBGyPfMUMVfOnbjplcUO1UbgtQQm2Qlyrz56s8RGIye9CiViz9xm3y8jMwL3hnlO_n5P1qTMKhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df4abcf2c.mp4?token=M0DHepLNdkZVVaJfdZt5rx1WobWc3YF9pvdldfVAixvJuTu7LF4HO0cIcWuCx7yhm5va4Eq-0cT0bi865tpM6yS0CNWsJ3UPiL8qvHRv6Kv2lezi98p9hIwzQagyeYvBLrWar9Ogo_75xe55n9v3JlvNLtoTYS0DQZMLOkLKpg8bI1bKR7E2rSmyRiKUwKBu3AJ44Pc_Uk30fyDvVzFtI1wlp8fvHz7azx4qV5XqBbzPk-ZObMHW7FVwTKqd7GsceJAYD2OzlNPLBGyPfMUMVfOnbjplcUO1UbgtQQm2Qlyrz56s8RGIye9CiViz9xm3y8jMwL3hnlO_n5P1qTMKhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کار: ۸۶ همت از حقوق بازنشستگان احقاق شد
🔹
میدری: با پیگیری قوه قضائیه، ۸۶ هزار میلیارد تومان از سرمایه صندوق بازنشستگی با رای قوه‌قضائیه به اموال این صندوق بازگشت.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445360" target="_blank">📅 21:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445359">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da10dc61f3.mp4?token=BdNWkyS20yU8yqKyde6acnP8PL_gdEQ6kYEVTsGaDavZOhfdYF75X8F2fpLExFKpIbWmRwo772usuk042qNqJr-EfNlgHJJws0GUnM6-Orlke0NtlIa_bU7LUoLBVd5sDhCVos_0x3OXoqcSP0gZV3y_pv_6_rQzUAADAL2gr58DtviZ9zjFsvIh-vfOYPriGGlY6lMuQ-p4rx4_mNe4bA8cAZeTBU9kD5gl0jEte_lQKui4o_OoYlbn3oaaXcNKOgzhmGMQqnbZ0EqdTrCwZ38Zr0SRezkUmgI5XdObEkZyMrbeX3kLthwdqxk1B6P6UXxFZaw0MwZKhohqS2-R1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da10dc61f3.mp4?token=BdNWkyS20yU8yqKyde6acnP8PL_gdEQ6kYEVTsGaDavZOhfdYF75X8F2fpLExFKpIbWmRwo772usuk042qNqJr-EfNlgHJJws0GUnM6-Orlke0NtlIa_bU7LUoLBVd5sDhCVos_0x3OXoqcSP0gZV3y_pv_6_rQzUAADAL2gr58DtviZ9zjFsvIh-vfOYPriGGlY6lMuQ-p4rx4_mNe4bA8cAZeTBU9kD5gl0jEte_lQKui4o_OoYlbn3oaaXcNKOgzhmGMQqnbZ0EqdTrCwZ38Zr0SRezkUmgI5XdObEkZyMrbeX3kLthwdqxk1B6P6UXxFZaw0MwZKhohqS2-R1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور: جاده‌های تهران در روز تشییع رهبر شهید مسدود نمی‌شود
🔹
فقط به شکل مقطعی پیرامون محل برگزاری مراسم محدودیت‌هایی وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/445359" target="_blank">📅 20:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445358">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f1a8e7cd.mp4?token=frHFhmTE7QdLYKZlX-UHTcvIC7RXBn6GMPhh2eLuHSZwgIkqXBCv2qvCy01S5uShweCQCBL4O0Fi0hIJ4PLtBO0OIm-OJ-KBe9KcH6aWHcKAHfMtF1VPx22R_6jTwu4m4pmitIReB7prpt04sLeEhs2kxAGSyT4-QeMr4e5vrUPAujQqK7wg9qmJ50rrLaovfRumFB1BHXXOuqSo7e9ZIP7hLvOdRFcdlKEovzPWfR_mENSHslF5_Wm9841zrT7BK3C27lwsWpvZXBwox5LhHlhsQ2XrCAWT6vXoWatjPG2j923Tv7BKqVh28BNZBCVoXH4x5C5n7J2s-DHzqP4RGjkn3Ne0-QVCTbK7cog4sqvVqA2U1nlYaWHEkyZdmLiy04RvnI-B_GX7l6iSNxNQI3fjb4yKiQOJ6NVBNYzZ71vr2a2xBbSPFgQyxs-dno7Inpy63ieDeKz30iAdbOkbvPjuCgKAEuqLZ4J_Rb9EMeTJFstbkHe8848CzMKhEbXgjlYVK9jBPQGObm9uhxLmJGh5WxsKQ9jzI2ZMv5AitbGNBQsIrEyppHeyv61oKau1CZ4UtNX1R_bFHdpiuhWZc09wP-EuDpPxLQAWZ8lXfrp0x0UUE7fjpyQUMvsL5jVvDavwynNca47EPsP7elsPfXWQbVe96Nb_vt0g_kcb4LM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f1a8e7cd.mp4?token=frHFhmTE7QdLYKZlX-UHTcvIC7RXBn6GMPhh2eLuHSZwgIkqXBCv2qvCy01S5uShweCQCBL4O0Fi0hIJ4PLtBO0OIm-OJ-KBe9KcH6aWHcKAHfMtF1VPx22R_6jTwu4m4pmitIReB7prpt04sLeEhs2kxAGSyT4-QeMr4e5vrUPAujQqK7wg9qmJ50rrLaovfRumFB1BHXXOuqSo7e9ZIP7hLvOdRFcdlKEovzPWfR_mENSHslF5_Wm9841zrT7BK3C27lwsWpvZXBwox5LhHlhsQ2XrCAWT6vXoWatjPG2j923Tv7BKqVh28BNZBCVoXH4x5C5n7J2s-DHzqP4RGjkn3Ne0-QVCTbK7cog4sqvVqA2U1nlYaWHEkyZdmLiy04RvnI-B_GX7l6iSNxNQI3fjb4yKiQOJ6NVBNYzZ71vr2a2xBbSPFgQyxs-dno7Inpy63ieDeKz30iAdbOkbvPjuCgKAEuqLZ4J_Rb9EMeTJFstbkHe8848CzMKhEbXgjlYVK9jBPQGObm9uhxLmJGh5WxsKQ9jzI2ZMv5AitbGNBQsIrEyppHeyv61oKau1CZ4UtNX1R_bFHdpiuhWZc09wP-EuDpPxLQAWZ8lXfrp0x0UUE7fjpyQUMvsL5jVvDavwynNca47EPsP7elsPfXWQbVe96Nb_vt0g_kcb4LM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما هم خیلی دوستتون داریم  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445358" target="_blank">📅 20:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445357">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMHt2-3Uc1t6lHwCdJ98jza-sO_KIZOIme4xDd08-gzZ-gwNEf6tZpwMBn4xGk0jLRZ3pkQMQNcDBxcmIbGzYKeI87-d2yEi0dUQht74pw--rA9GD0LWXrTFv3ZYZq3fjHskMhHCF6LPda3vxNxiAb4yLZRy7wb_t_B9FJPpikKaF8pgmjAuL3PPDVjePT6jHnhj5q4gbY6ESRPa9gqgQeq-YBIlJWz0zDTv0oUaV0va0Xu38LyQJ3AxlV2tg4gQs8H3YeS2W6j5F9yyPUzkzPwR6l_8yRDMZPMWR9h3oNdez3I_6rewpO2EClL21ivpy7gMv3eann9itJsZsoEqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن‌کاری در تالاب میقان اراک متوقف شد
🔹
اداره حفاظت از محیط‌زیست استان مرکزی، دستور به توقف فعالیت شرکت‌های برداشت املاح معدنی در تالاب میقان را صادر کرد.
🔹
تالاب میقان اراک یکی از مهم‌ترین تالاب‌های ایران به‌شمار می‌رود که در کنترل ریزگردها تاثیر زیادی دارد و همچنین زیستگاه پرندگان مهاجر مانند فلامینوگو درنای خاکستری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445357" target="_blank">📅 20:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445356">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18ddfb9c4.mp4?token=PHykuGnnst5ln7NI4-ilhN-apqXM2htLsugO1d-_QB-JNtz1iXeWzH8nlicOV9MMFmXuafU89wKJBiai1mZe0fGsk8EUbyhqpaFegnuPpNDENA-WcaGUW3Gqg3AIVLcRqZXv-FUMm0RB3SHIW7NboP4oRrhTYuw5EdM71FUivkgTT9jlcJWVEttbBKKYrk0rzBlJSd6E0q1D_Sg9MuonbzxH7q-6vaV9DAgRe2v2zhzUu1NSXbodeOe0_3j84wNDPgcRULpSM4MSAq0YJ0DZ9mLHZQVuZoIkQwcgrKVk8rEV9i-BU1nxC7O8XW-Lw6NPxX0vVEGuYHvXEMArn0Bfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18ddfb9c4.mp4?token=PHykuGnnst5ln7NI4-ilhN-apqXM2htLsugO1d-_QB-JNtz1iXeWzH8nlicOV9MMFmXuafU89wKJBiai1mZe0fGsk8EUbyhqpaFegnuPpNDENA-WcaGUW3Gqg3AIVLcRqZXv-FUMm0RB3SHIW7NboP4oRrhTYuw5EdM71FUivkgTT9jlcJWVEttbBKKYrk0rzBlJSd6E0q1D_Sg9MuonbzxH7q-6vaV9DAgRe2v2zhzUu1NSXbodeOe0_3j84wNDPgcRULpSM4MSAq0YJ0DZ9mLHZQVuZoIkQwcgrKVk8rEV9i-BU1nxC7O8XW-Lw6NPxX0vVEGuYHvXEMArn0Bfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بخش‌های مختلف کشور باید همکاری کنند تا افشاگری‌ها در حوزه قضایی خروجی لازم را داشته باشد
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445356" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445355">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ادعای وال‌استریت‌ژورنال: مذاکرات این هفته ایران و آمریکا لغو شد
🔹
رسانۀ آمریکایی وال‌استریت‌ژورنال به نقل از منابع آگاه خود نوشته دور جدید مذاکرات ایران و آمریکا که قرار بود این هفته در سوئیس برگزار شود، به دلیل درگیری‌های اخیر لغو شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445355" target="_blank">📅 20:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445354">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj41UAv6bNEqx1Uqv-A4vFBRmTn3f7Gl6dyWphrH2NfP9dOTVrQp6vqUU9NDBChDGrAK71DGL1hmMRaKHl0Txo8U81zpDEoQsohlIVrD0dJuoj7YcJesMVFKPmdIQlpiOvuRP2WUAtBvNKPdJO_oSTeYTxEEqFUY-cZnl9D2AOYXAoBdGp-MiEUFYH4IsiUPVYShv8jgnY21skUILPTowF2x9MvIhT3PE90jNw6IbUjg-hzGstNmJ7yl1QYnPICnThHqnXQs5nIYlV2PqBAgqY2hsKGpRjgoElUIdf0nMEqY-pzaejRdxLHY2Xoh0a3VsE7nk30BvgaCfZgoRihTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکاپوی انتخاباتی نتانیاهو با هراساندن ساکنان سرزمین‌های اشغالی
🔹
«بنیامین نتانیاهو» نخست‌وزیر اسرائیل روز یکشنبه در سخنانی با محوریت انتخابات پیش‌رو در سرزمین‌های اشغالی گفت که بقایای محور ایران همچنان وجود داشته و باید با آنها مقابله شود و چالش‌های امنیتی سنگینی پیش روی اسرائیل قرار دارد.
🔸
نتانیاهو در تلاش است تا با هراساندن ساکنان سرزمین‌های اشغالی، آنها را ترغیب کند تا در انتخابات آتی به ائتلاف راست افراطی به سرکردگی وی رأی دهند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/445354" target="_blank">📅 20:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445352">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSZLyZ7c39UNllBJRDBMAeWXHFce4QoYvQvR-xHM3jt7LB7h1q8Y3sRiUg2osB6zVPDfyLqcHXytht7ALRPEc5cR3JWJXzuvPM_N5lsUuJIVBu_TPz0a5j3_KR96WVI-UBU97zD1pnRDO1G2f5eYDy_Wt3EeX2RrbP1AhaZRo42opnty9TJ_CIzyKsd8JFNoBJUKNDOghVcKA_oucskpss06xuPbCDBeb58iPpv69v61FnRgzo-SonOChiL-jhz-fibkvE8AgMBW8DZdiBDbvbf2vnapPaQgGxuVqHJwTi0Jcm0b_bxJc38ltGijcWP1Rwd-LYx3HsWKrp3UErgnSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی گیرندگان وام هزار میلیاردی بانک پاسارگاد افشا شد
🔗
اسامی را
اینجا
ببینید
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/445352" target="_blank">📅 20:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445345">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsx8iT7W07gxf64rrNkoWgnhYfgKRP2igp6V7sowgtig9Ip8Z-UjRY3dhvqVMfretG6HlY1qeGQ96jXJo-SFIyqwLCsdMjw9OrVv3sEyPlG8g6sQ9Pi7vEZ0EeZ1eelEXJhko84Fye3O2Sk1KASFMyp6RibJtrYg9WV22j9c0AqsKiCl7yBzGEZJ2CT3AEq3aCp5NYIZmcSxNDUxYFT8ImDjPrA_Yy60RCFezzrWC7eQ09DbUM8UQSCkPUmShyatTn1fihEIPvhxiS8xO7NGYKO4km-e75DCe133owtamP3pm2w9epWv3UubQebPUma6kWzrn5Ba6EqeWPp4iQYZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJVUYZhNfpFOFx94Tj5x97K8cYPGuMHwNcTQNbaNUT6XJTfql_QEYk9HEMfFcjIJgx9Z-wVeuHFVig-NOiQthny04lgWVJnvZJXV5Bs6RXZ0ThjNDYBxEHAuxHWcAx4yCcx4dxfR0FguezOb9hE9oUeJDwES0ce_ci8KkQXz3sjEx9s1TJS4bJheHZ8NZJJtN7EnNdCW48po2k8QFAmYi-VBEJPsv3QBd5Zi9U5iyFJtk9QEVR7m3S_9IP0S4FJhH0AaND4a6aRyzalLUYxSzgFq0xBswz1pDieZq7OOJpTCB_M6ofVbDvjahUEDaBpdYeVwQqoXtdSp9-y2w35KWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eslkqyq3XXLHjQsiycrML1Ke9oIwJbeYSdrDa_g7QxObPa7kHSqL77PBpsJHCPaLHraUZYe0sMQUbRFCCdWZ66IY7_bijDvumb-lJGNhmrAD8IgTaiwY-0RCXjfRvrhJy_xB7tozU2BuFSOKMgi0kIYPKY7nhs_8k9IfvEXqrzX2a5sY1cwN6ztf-fZPdhgXqE0crwZPPhbh0P35fG-c8_LFsfjJf6QKjudsYCdScnweqsVUeteV3U-Kl-HeRQX72GqaH9hIH15mhwS80DS8ZfxLog-qQiHk93g3PDMeozYy1cFSuysFQtsRH3gfRSuLS-7vXeVgkEfExDVXDRCRUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGHkyO3jtWT3qTLSE7SmVHHfh1yiZF_iPKWm2N5eV6XYCxjHdSzw3b407BagWMEdgXdmbHjJldqcjyB5nZ04mARhAXX-r6l-4ACEJV4TIXY6f9WCi87K-lu_Z5CwH6FwuKT_AQkR2AOACxh4TYTEfG5-wU0GgESwAlJ7eL-7T9fGz6qAOK2PDF1pLBmYHrbz6a_sl79N5LI9cO7HKAAvnr5hh2TAEXIN0zfLvtk4e8c1E4qR9OMslgEP-T0rsuO2AKKeRn7P8Zj-uWxy92uFO-JkBn6FPPLdy29TWT3qsBUJV6YraRaDko9R2kGTGM1HmAjcuhpBvdnhYZ1IEmjvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo5m11vCN5MhwGTJ8E-8q1od6kbkHoQ3_INhbPVuhASWB9iicGCMetDN3yY8hXj9MJlvQztVbczGr6rqXqT84HNwz0LBXPyAuRL69GKgZleHWPY16jLWO42HOPnZNoGaTyBmNlWaaHWnWLF9qV408eYuxtVO27eokKQgY2lm3kiw9NwZwHysWnQ-DLeK_IgxQo2Z7qfQrqJllxpF--SJUwX2KxtO2CT_--WkohsULbBxSrelkhsTmcvuVwrpZWIaWSOBsZYX9PYWVskAc5AnhnZirFqsVqvA00JxKtqYQRG72ztPQozvVy1PoWsochHe5a7h9nAChOf6-m5QIiunMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t37XcCskXElK--Wrj-Ta6EJIt1uTbqIjRKCCcgIWc7rt36cWbMSQdS4JmGlIT_IovANcXPyAMkhliFnPQF4w9ESoDBbKfbIf-t6WBqRwSoWAb9q3QjGhXm4NtwWeyaixG3FyaH7vBfclZ2EjqruiCvjfYRHAQBPbBR3RNcvc0taNssj6LOCNtOcd4HsODw4ZtDyZAvBKZjUGtQcjVBJrhtTUwYvIsPzmyIJW9xuqyOGe5d4lmJsdVCUB72DTb0x9nIvA38UpjjRVG-1kKnbp94o6-mm5QJ70Z4vEFZChe3kz8GeAD0XLW9SKC-p52pGuSPRHnqXOCzsjWMNgOf54sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gwp-iDN-ylvduH4bOEk-QLSntOsmBgfEW1wO3iOSRzlPxCxE4Xt-c9CE3ugkgr0v2WFRFyJ-xjFvv6m6r2Sf4gux2kD4-oIk3eViwLgf-lh9h4IVFfsoI2xsWPzIz6rYkE1YmnhpwRMixn2rj6kGaOWQiT2IymX1__QitkJBpNhq54EzjAJMWjYZTekNt98oIZlyszUVaXrS4ZG027PbWILMErp_7XtSl5q9fEkMLYXBroo7i32y4SHAZgCzSOUzoE5wx2cD7cXnqJLJu8IhTNXgKrsglLYwiEHVI8taKe9CdzPtejn7W102enIaupkRwr-AW3geuTmIMopvq9cH_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روضهٔ ۴۰۰ ساله در خانهٔ شیخ‌الاسلام اصفهان
🔸
خانهٔ تاریخی شیخ الاسلام به عنوان یادگاری به‌جای مانده از دورهٔ معماری صفوی و قاجاری است.
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445345" target="_blank">📅 19:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445344">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بستری رایگان کودکان زیر ۷ سال هنوز هم اجرا می شود
🔹
روابط‌ عمومی وزارت بهداشت: برخی در فضای مجازی مدعی شده‌اند که رایگان بودن بستری کودکان زیر ۷ سال لغو شده؛ این ادعا نادرست است.
🔹
مصوبهٔ رایگان بودن بستری کودکان زیر ۷ سال همچنان به قوت خود باقی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445344" target="_blank">📅 19:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445341">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۷۸.pdf</div>
  <div class="tg-doc-extra">3.4 MB</div>
</div>
<a href="https://t.me/farsna/445341" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۷۷.pdf</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445341" target="_blank">📅 19:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445340">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkY-4Rf1zU8W-2Mc-fcJSNOlnRvyqHmyYSPZF4LQZ1W9H0eHdLIYV2076XKoMQMolL1MyOCvc2x9PZ0gIPvMCe5oYhzc9zemHKX9bJQ8-g_BO0J7Uf7SoejSwSU_3LodeBP_kPK_wK6zKMcZewiQU9jS-PqcJQm5Mh8juC25ytHLKFIPF8gAESGx3ohBKQTrGJ5I2J7c9CoTaTaAyYsK324Rx2lPhQBQ5GhvoqxlEBe2iHWttX3oVmYeL-by1OgTrAyLE8rgM7EVJnjDI0RjCAZq3K9dAipBTTBIkSH4G1AUFGu9GH50dioOUpImWNQO92MzoXKscm3BfwM8xfPjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کاروان ملی سوگ میناب» به راه می‌افتد
🔹
صالحی‌امیری، وزیر گردشگری با اعلام خبر راه‌اندازی «کاروان ملی سوگ میناب» گفته این کاروان با مشارکت گروه‌های هنری، به‌زودی راهی در شهرهای مختلف کشور راوی مظلومیت کودکان میناب خواهد بود.
🔹
همچنین تولید آثار تصویری و فیلم‌های کوتاه و نمایش آن‌ها در نمایندگی‌های ایران در کشورهای مختلف نیز در دستور کار قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445340" target="_blank">📅 19:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445339">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVTOZjjo5Kop1wzJkKtLvNelJiWmLegm2pKzOJNCW2wcw6OyavXr1O5AS1dqTVCsG-Y9fYa8z2rS9oDWYnC1Om2JH2pQO76w-Vg5G4TevXD12T8MH90rtX-VUEve7EP0yTLGRQ_TkDhfiG9ZC0aod7AenDyPmmGCMKwxgSqpjLrYt3zOnSgURwIWOotIa9hgGpsJ_h3KUyg6vV-7-POfNJOL4-FtgkUSLPE7YX3hV5ISpcKxzW9YSfdh3QpOBqBAWjgGKGGW0-ZW_WUCjI3zsftset-o8NFvE2yC-ByOkF4EZWpDplM5Hwn2XFYm2YV5NUniPPLVBifVq0DpUosIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توضیحی دربارۀ مطلب یکی از کاربران فارس
درپی انتشار تحلیلی از سوی یکی از کاربران «فارس تعاملی» مبنی بر لزوم ساخت بمب اتمی توسط ایران برای دفع شر آمریکا، و بازنشر این مطلب در رسانه‌های خارجی، به اطلاع مخاطبان گرامی می‌رسد:
🔸
«فارس تعاملی» یک بستر شبکۀ اجتماعی است که به‌طور موازی با خروجی رسمی خبرگزاری فارس فعالیت می‌کند. این فضا برای ارائه دیدگاه‌ها، تحلیل‌ها و پرسش‌های کاربران در نظر گرفته شده و هیچ‌گونه ارتباطی با محتوای خبری و تحلیلی تولیدشده توسط خبرگزاری ندارد.
🔸
همچنان که پیش از این نیز اعلام شده، معیار تشخیص اخبار رسمی و مورد تأیید خبرگزاری فارس، نشان نقره‌ای خبرنگار همراه با لوگوی اصلی این خبرگزاری در کنار مطلب است. بنابراین، هر مطلبی که فاقد این دو نشانه باشد، نظر کاربران محسوب می‌شود و لزوماً بیانگر موضع خبرگزاری نیست.
🔸
همۀ مخاطبان می‌توانند با عضویت در پلتفرم فارس مطالب و دیدگاه‌هایشان را منتشر کنند.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445339" target="_blank">📅 19:29 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
