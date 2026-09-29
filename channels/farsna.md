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
<img src="https://cdn4.telesco.pe/file/qUbg_NQRHjPEsrj-I_y_DA3bPo_qpmWkhU6JpUDt4EbqnoegZT3p3LwMFBxg7UX80rcHLDEC1ifps5UTo3LbLizTg97BZkbvs9PGFz4VJu6HGErsi5JLyZzzVh4S33yXLeGcxkNBI67wXkq5t6-3woGaNKMEYAONocA6C0VQUcLqe82oa5fsJwkEmHHn0sr_YkcyMcL4UDSZCgQZt5AKuPT2w-TcqYva3DPO-FQJ_8FuXkrybH5szuU3Io_iiUjNTbLQ11Q9kUGbcXLMA2e_lU3qq79gWsNL8tV-KCqu01fDWRZiWzKgmNbA9ClB5wgjDZs8lCy-27dD8M_-wIfXnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-465313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بانک مرکزی سراغ ۱۱ رئیس شعبهٔ متخلف رفت
🔹
بانک مرکزی: در ادامهٔ بازرسی‌ها و  رصد تراکنش‌های مشکوک به پولشویی که منجر به اخلال در بازارهای پول ارز و فلزات گران‌بها می‌شوند ۱۱ بانک متخلف نیز جریمهٔ نقدی شدند.
🔹
با هدف ایجاد بستر لازم برای فعالیت‌های اقتصادی…</div>
<div class="tg-footer">👁️ 337 · <a href="https://t.me/farsna/465313" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3bcb2e5e.mp4?token=baFPevZv0b2Bdxd_5UWXo2qgRq4pPsACTGr_ORHD6FMV2zPIfrNhHAAp0AMUGPG3uIAOibH587F0d4Sz6rq3i1wNEma-OTUeX8BlQZpOK8W3a79b_KkJGmeQchMJzVCcJy4AApuQPKBr54PvERQ5vCRfukJi3qew9W9JIv5PDI6ksEgSvJb4UhtSWk4XEgAW7S-__Y1bGs-N414hf60TRGuaZNtSPv8DR0FXC0P-XMkrNY7SMgCjVp0PKKYf0gCtN9N9pZaSJOfd7v5HhFpOVIGPSkkf1HIReEhD0hSlBkWXnplnU7hxcdWDYsgWoHsw-gFfG5QZKclHLxIrAGybvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3bcb2e5e.mp4?token=baFPevZv0b2Bdxd_5UWXo2qgRq4pPsACTGr_ORHD6FMV2zPIfrNhHAAp0AMUGPG3uIAOibH587F0d4Sz6rq3i1wNEma-OTUeX8BlQZpOK8W3a79b_KkJGmeQchMJzVCcJy4AApuQPKBr54PvERQ5vCRfukJi3qew9W9JIv5PDI6ksEgSvJb4UhtSWk4XEgAW7S-__Y1bGs-N414hf60TRGuaZNtSPv8DR0FXC0P-XMkrNY7SMgCjVp0PKKYf0gCtN9N9pZaSJOfd7v5HhFpOVIGPSkkf1HIReEhD0hSlBkWXnplnU7hxcdWDYsgWoHsw-gFfG5QZKclHLxIrAGybvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کینۀ انقلاب از دل سیاست آمریکا خارج نمی‌شود
@Farsna</div>
<div class="tg-footer">👁️ 369 · <a href="https://t.me/farsna/465312" target="_blank">📅 18:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyulXv0fn2RTEUf6OrZN6KUxK3IDUH2kPEEYYAGOg0cd0qENTVn6epsAMpY8-CfOgWEfAOnuQtf-uMacSiW7eGNTk9FGmQEZMcJtgWEPkmwYvI62V7Y6l7kwAl5YVMuF8yzmQl-nl7H1tggKWiJLaWEDyaR2bodm5PmA8fkmhIs96zVgQVszZPg1kRXliSYx9vRHEBvBvBT-TStnyee644iHcug1nvKmbNT2y5LbFYYvY-pw9EVC1HkmaGx5N1j7l4aMBiogqftCpE1xf8mw3wy7isPoYarzcJkJtNzZnDH85BMbkxK3LTLNPRqnUzDU_zMpcxk80ZgI6V__YFi1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق: پروندۀ حضور نظامی آمریکا تا دو روز دیگر بسته می‌شود
🔹
سخنگوی نخست‌وزیر عراق: نیروهای آمریکایی و ائتلاف بین‌المللی قرار است تا ۳۰ سپتامبر (دو روز دیگر) روند خروج خود از عراق را تکمیل کنند؛ بغداد همزمان بر کنترل کامل اوضاع امنیتی و پایان حضور نظامی خارجی…</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/farsna/465311" target="_blank">📅 18:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTKAUuqAbEcwwwOBXM1WB-CweTCFmjdVHVbpm6cUOcmSgAIQkO1KdabExqmokHk9QUMRPCIL7vQ-GerQlSs2wcIMNvprfbUEa7ihDPIOCu22qggMIM1QlITT9pzqMhQP561yEu2fi_XbRkGpQpHTS4nzpmg7TQTUPWBc20Db1apNrk4MQm8cuH8H_c7Hh06OkV6yQPxeVbbeNjQaD1rjMj8dOiJypgJZ3y9kxruEG66WVDUp-EieOhJirdWUXdkFNMn0O5UpU9UviFfsBlmhytpWf9fTzwQUir862a5rJwUiqb8s0de9mMdMix9N2fNib4vXpdb-rhB6ERvwrE-xcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالیفرنیا ترمز ارزهای دیجیتال ترندی را کشید
🔹
انگجت: کالیفرنیا با امضای قانون جدید، مقام‌های دولتی را از ساخت و عرضه میم‌کوین منع کرده است؛ ارزهای دیجیتالی که معمولاً بر پایه شوخی‌ها، چهره‌های مشهور یا موضوعات داغ اینترنتی ساخته می‌شوند.
🔹
میم‌کوین‌ها نوعی ارز دیجیتال هستند که برخلاف پروژه‌هایی مانند بیت‌کوین، معمولاً با یک شوخی، تصویر، شخصیت یا موج اینترنتی شکل می‌گیرند.
🔹
محبوبیت آن‌ها می‌تواند به‌سرعت بالا یا پایین برود و همین ویژگی باعث شده استفاده از نام و تصویر افراد مشهور در این بازار به موضوعی بحث‌برانگیز تبدیل شود.
🔹
قانون جدید کالیفرنیا که به امضای گاوین نیوسام، فرماندار این ایالت، رسیده، صدور میم‌کوین توسط مقام‌های دولتی را ممنوع می‌کند.
🔹
علاوه بر این، شرکت‌ها نیز نمی‌توانند بدون توجه به ارتباطشان با دولت، میم‌کوینی را با استفاده از نام، تصویر یا چهره یک مقام دولتی عرضه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/farsna/465310" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU90eplKiRmxGMqXSr6OxFkWD0YT4VDJ1nghgxYc5wdMS4_DA159Baxvy6EVLmx3YJFHdP67rUeNr5G5umtWn5TpsZy7dp03fluJnLjEN2Us4p1S4R8RHjyjpktk-2wssMdxiQAfsXKDFZf6UsetlN-xdEm2oMIkG2hXw5C1l38rZnEwo_XBM7juzRKMBjIByNiHBYjKXF8182SD6RQiqf4kcIDw4skg-dD_BR1IM8MRp-J_Rs7ddj5tlYqhDvcEFYqhGOgr7wqVpCAfSgqGTrwxaYJ5yd8XX4Bmso44FKxLg2SbudWDEbQ4X6RH7VrqykMuq27vFh7ZEKmcs6yAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: اگر بفهمیم حملۀ دشمن نزدیک است، حتماً عملیات پیش‌دستانه انجام می‌دهیم
🔹
امیر سرتیپ اکرمی‌نیا: شهید سپهبد سید عبدالرحیم موسوی با جدیت این راهبرد را دنبال کردند که راهبرد نظامی ما یا دکترین دفاعی ما به سمت آفند پیش برود؛ از پدافند به آفند. ما در این جنگ عملاً این راهبرد یا دکترین را عملیاتی کردیم، آنجایی که مواضع ضد انقلاب و تجزیه‌طلبان را در اقلیم کردستان عراق مورد هدف قرار دادیم.
🔹
این در واقع نوعی جنگ پیش‌دستانه محسوب می‌شود؛ قبل از اینکه دشمن دست به تعرضی بزند، مورد هدف قرار گرفته است. و شما ملاحظه فرمودید تا امروز ضد انقلاب نتوانسته است که عملیاتی را علیه مرزها و مرزهای زمینی ما انجام بدهد.
🔹
در آینده هم به همین شکل است. در واقع اگر به این نتیجه برسیم که دشمن حمله قریب‌الوقوعی خواهد داشت، ما حتماً جنگ پیش‌دستانه یا عملیات پیش‌دستانه انجام خواهیم داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/465309" target="_blank">📅 18:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNmnWEFoZfF-KL-4SafzwdtwcRT_QrYz9ObAKP_CAtcR-amTbBmhQlMbj03szZHD1MQwHwQavgS5Sofor3nuvNOBoX7V_Kzxt5qN33PrcZZCCVGhRy15Zvn6RO1-jxc6R45xbdJb71nVTIrA0U6xOcNI5nQun704W8DI1XBzhjRlo2IrPPFmo6ujpvjfvvgphojmQTdulwBPcPF1Jpj-lw6ClYf1ksU2WnnDu5El6v4RxPKtjYRVRE-ntBUPfzTvCE0k5ZQr5eW5brgB_e_8Q0hz7WhPEffJz1eZZMDZObpTAUZS7oNiVGIrSWzUNDL5K8efOCnC_D53HvorKmQRKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک میلیارد فوت‌مکعب گاز به ایران رسید
🔹
فاز ۱۱ پارس جنوبی با اتصال چاه دوازدهم، اکنون به ظرفیت تولید یک میلیارد فوت‌مکعب گاز در روز رسیده است.
🔹
پیش از این، معاون برنامه‌ریزی وزیر نفت، از بازگشت حدود ۵۰ درصد ظرفیت آسیب‌دیدهٔ پارس جنوبی به مدار تولید خبر داده بود.
🔹
پارس جنوبی حدود ۷۰ درصد گاز کشور را تأمین می‌کند و از مهم‌ترین ارکان تأمین پایدار انرژی کشور، به‌ویژه در فصل سرد سال، به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/465308" target="_blank">📅 17:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdumRRhwxayflojaTFMNpKbTe-u1rylvbqaxj0Oyg0_pwDHN_HJzh5cw0gTkKca72czQGUNOwGaDsgCaOcrLHQwlrSxTOVn5IZxd4bWWKAiNTGjlzj6Qkklpj9Smt784BvOlImhXWUYqyZua0-A-R5ALMf0kcZMbcej1zgtv_X2Mu-WlJoEoDkQ_bs-EEKoVOWZ7sXyI01c7zVQkGCY06k9z98BFtX8ez2Rwqj5dJ2g0Xjz6-kqkWxz93d8lqkkZhcvIVv0GpdgLbr0jmHk302bP5ovZifd7iqL4tNGBfup7CiP0hfciD9R4xJIIPQF8Eql3O_rYkqlVi_dfIy8nyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد هسته‌ای روسیه روی میز ایران
🔹
رئیس شرکت روس‌اتم، گفته است که روس‌اتم درحال بررسی چندین سایت جدید برای ساخت نیروگاه‌های هسته‌ای با ظرفیت بالا و پایین در ایران است.
🔹
از ۳ سال پیش عملیات ساخت واحد ۲ و ۳ نیروگاه اتمی در بوشهر وارد مرحلۀ اجرایی شده است.
🔹
ایران در «برنامۀ هفتم توسعه» ساخت ۳ هزار مگاوات نیروگاه اتمی را هدف کرده و قصد دارد ظرفیت تولید برق اتمی خود را ۳ برابر کند. رقمی که ناترازی برق ایران در صنعت را صفر می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/465307" target="_blank">📅 17:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ماجرای انفجارهای پیاپی در مرز ایران و آذربایجان چه بود؟
🔹
فرماندار خداآفرین: صدای انفجارهای پیاپی در نوار مرزی، ناشی از عملیات مین‌روبی نیروهای جمهوری آذربایجان در خاک این کشور بوده است.
🔹
این عملیات در نزدیکی مرز انجام شده و به‌همین‌دلیل صدای انفجارها در برخی مناطق مسکونی خداآفرین شنیده شده است.
🔹
هیچ خطری متوجه اراضی ایران و مرزنشینان نیست و وضعیت مرزها عادی و تحت رصد نیروهای امنیتی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/465306" target="_blank">📅 17:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd93667ac.mp4?token=eHi_fQAEjj8lu4tMFN3BLNNA6mNbFqChTI9d1g8L2yRL7eUkzxspX1e5_NTLhZFgvMfHwC7zNXZM3wVVQ2Jo766BAzUwBAsXTaN094p0SUeQ0kOa_6VKqK-l3ofIkBN4eIZWKlOclwBK0kxcngOfZPD1ITdgAGBI3Slsr4Czp13tKy7oHqS8z6CFlqyiEGnCR4vtogXdoPbJgpEtmYkAK28P62KctowixF9GVPTN1fL3-2X41C3Py-kmuHyjVQz8NnwRZLutofvr2r9UeOBg4X530WoEBRRCKYlPw_pEiD0DzwaNhFKlxZyhnhRUHbxoy_NZtsgKZQ6aJJgIReupgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd93667ac.mp4?token=eHi_fQAEjj8lu4tMFN3BLNNA6mNbFqChTI9d1g8L2yRL7eUkzxspX1e5_NTLhZFgvMfHwC7zNXZM3wVVQ2Jo766BAzUwBAsXTaN094p0SUeQ0kOa_6VKqK-l3ofIkBN4eIZWKlOclwBK0kxcngOfZPD1ITdgAGBI3Slsr4Czp13tKy7oHqS8z6CFlqyiEGnCR4vtogXdoPbJgpEtmYkAK28P62KctowixF9GVPTN1fL3-2X41C3Py-kmuHyjVQz8NnwRZLutofvr2r9UeOBg4X530WoEBRRCKYlPw_pEiD0DzwaNhFKlxZyhnhRUHbxoy_NZtsgKZQ6aJJgIReupgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسکو سقوط بمب‌افکن روسی را تأیید کرد
🔹
وزارت دفاع روسیه با انتشار بیانیه‌ای اعلام کرد: در ۲۹ سپتامبر، یک فروند هواپیمای تو-۹۵ در جریان یک پرواز آموزشی در منطقه آمور سقوط کرد.
🔸
این هواپیما در منطقه‌ای خالی از سکنه سقوط کرد. بر اساس داده‌های اولیه، ۶ نفر از خدمه جان باختند و یک نفر مجروح و به یک مرکز درمانی منتقل شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/465305" target="_blank">📅 17:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📽
از زمین خاکی تا تیم ملی
روایتی از استعدادهای فوتبالی کشور که از محلات کم‌برخوردار انتخاب شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/465304" target="_blank">📅 17:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d60pqWksPQM-CKqAECosAIWX7BaJzZ6VDse9THmrLab51wvMO2Zf1azXoQGr_-fihqIpI2vf2vzLkKEvJjdHSM6UaKiXrm9Uh46B1T-JSl8YQ9C1jBbx_ohKSdvOdZQeA2cLO8X5mh9QbP-6oBBwYmunRhbX9Bfl6TuyfNbU2zaxNFu5DFuPIwOqN8e7RZMprl8LDN2TO7xNL5QQ4Qx5WZt0RAJbuOfawUoYM9VlgUPnoGizLzMI9mePn3cFLVq8sHmDWrXfWRvDiJjRvSj2pDb5RPyEokg1kRKSGu4IKKGiwfCWPxzOwI7RCLnqxIywxYfXpu_OFI4RRzlCOt7kYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZ7fhR_FpD7gqMQmnwzvIZY2JfSuHPtfjrhHSSVefzWU-5-M9QycYHUQO3OMrpJNdOeeIj2mNZKmkZV_rjmh5F7lHfqOV9SV2hj-XVk1Xfi19TuiBk3yq8yID75Hrno1YX72zIYK1m6WI4us2buLc-CJgnKxYqlTL9D0K-oc8Do86T62JA1jWGYj6tYErcIb4ea9CPWz97kzFn7yVRsXIXLu3-1wJlU9mZsagIkKL6UAcBrlU_XYdyFYFCEC0OXBWO5nRwEE-na4tZG5SsBxA2kbfr-Djy2hB7W2155UCmE8Td5fVsZ6ROp55BNOqiuOmvEvK_mMwW_nNT8O_1NODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osX8Kn2br1D8J9EtbMCPez4LZ-X-6HSp6bc03G1FztajJeBCI59bb397-OXK7WsGevqN7CA0urJ-La--dLTO_Lp0PVsmNB-qK8W6d16xA5OAfnx03xqmpH4gDTp20p4noToy--zF7BOn45HNEW049tSvmtzFSO5_wyD-x4-03dyFk1o5C51c8_VpgcVAZh3AyGhMIIG0neq7I1c-xBuZmkkQS-Z6U1biILNHNofQ1mmH0jaVQF3cxTaSnTRP4r9PjtdmZKNDlJs2ll_B-fHUV5-Wo_n4Yfm_9a-IWSxu5_NKt42WDfrcRFssfqDeFykgzKmE22Mr7GFgA0CzKxlq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez6Bcs2l9CYuCRtQJV-dtdj5vac-8_2q12Hs2GWpSZ5Jw1bmL7Swz7ZHp5lAcuKVU5OzNToo7aJH1A_Coj6QLv1KOhI6MeJBCrwJ0VFa0jMbxYhaqVrn3QwbQifnrFkAOPCncrbaKnEJgMROVRHgvVFYsVhMxc9kODzX-fch_S8K2pp6pAjnLUZTi_1wO9a8sD2MfcF3EEIRGTqdzO_psmWs9EvVs5hkO7NTsPKmsy7uFuA315TFdOf6-33aI-T3FSKXbF52ioPHCOpldNzsJsvWq3G0V_8wc2GGn93atSoLA5Xzm9zgdQ5DADt7IV8uC1E7dAZeEPEbpuxVT1HrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKzZlxeuRsoeLLvT5BqHhTOIKyJ8MXXk7zMBOpAEFWFtISrpOxRmcD0iIF6C6Jb2Oth7la9AXJYmDnwsz7okQm9_qs7oqvNOR-xkstIpgLp52Hjf5tcALgi33kS8dqL7ReAult4xi1ZfJjHy4asjxSIi9c4zXlWIEpmd95MHMSz1wCN7Cgp89kYGCS5EQdSjoudjmMSEiKLyiNIRADqlQP53eXLqDD8wOtkM11XIZK3xRI4x5zYMRwjh7HJFqdy43aF_nPRmdA9QFw2VqYW78-tiZCOaCkWimC8qY8QZ89QLBLnZnwnCITpSWkuelfBhFoXozUsuQK537F3BC6oG6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMIS84i9slxh3lcnTighWI9ue0horLGcKJI3v7rVKyaGdKfHmBhT-uQV0BbLpZu766AfCkG7Zap_Etos5dbFdAJMZd3DyOf-jAVVfudROuzSG1J0Z9AlKzFN-cgEpkJDG7bHwTpszi5QrQkDoY-XlBciSxAlhfoT5Z7P2z14p9_RSr9NUn5scAMfkEHwknbv51vS3KMk_yCGxFng0qOa7V2rkWKX6vg1Kb5aZOii4gk30QoCNEVl6V9JbVP8Z3zPsRzhV7d8smCUGTyZ8XnykWejjjdvw2zV2OhqJROrhs5MC3y9fJAw4pJRzyEk1kH0cOm7FF0UZPGop3t1e-3yWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ec_IJwJtynwQai3JV_V-nyFHOSomssiZO7GJ8icxIhXTAdccuXQTPTuTXtVTMR7zrRb1zWApg8vqiReXk00C43s5yHyZxWR-ghFo_eaMeIqz7X90R_RSx0jM4Tgh0kCvjkQ7ZRDw6feBOwFs2O1eJkC38_ozsGzcr3V-yNEfAYuNUhdcGIKZK70Fh3esM5BdEXsRelsUFSvZ4y5dQa3c-CAq2z4CBNQtXzjZb5nB0M-4Gq_giJT2xcdytjM3m_dZHNIWKgoInKs4mIF_Ep0UWS4P-qh58xu9WMMqKYRhlOPML6y1XBbm0r1_-iPXa3T-mVwn9SKFYrOCmrHVN9ODkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZeXJmuVunAtccln2iGtHX1GhpdSNGqIh3uAVD0oDWAbO-tNcqEPYkuDlkoESHgihnhwDoDF2eKwS_yTZClL8zGD5Aj6fFSyW198Q9GK5hEkRprmUtggqNgreUv4m6iQpgT78-XfvhVVcclNsr8p9esTXD9N2EG4wUqMHiH2uuCg5S6bWNw0BSqicTfqLViqE0ozZ69xsmAFuEQF5RVDw6biYzLXMCfWnQI_M0wv83vHCDGJbg8RxQ_tMXJ1kF9kBDooAUP-k9sET0KO_DZWMOWLB9yQvNyHm4r2OJ3t1WPKN4Fc1oIw_Vii6R5AwOZPKscb4bQeGb2oLY0GUptHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W35KC0astzGQN38MNOBC-n5zuzP8KlCQZK1m_m3u_PNU1V1hxpLG-2kNpzQ2af-P_MmM6EB7bN0eDtf94Tn8l4sDzZ2CgljN6CSea_1k-1XYt643e-8n9ZO2efo8FVsl2tC8zoZGUz72e7NSvzvyK8-dkHMKfTHpqwDGliQyY5m96jAfwczQc6BMP5iUjmsBjoc8PGQrih61tuPOSGnTe7ZbW5yUJKSywjkz0CBISLMYuosyoKp_B12zdNzzHHq8kVeYbiDbuFLELM0Ixan66Ec_eQghEdEZsBXAbXyzw7LF5_RPdLzN3YnEOgu5yawV86N5asFwdv2FeyOv5l_0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJoFpHhRWjKFGaKO87kVYxPVdVWoaL-9ewQ2KpviC69V-vTalN6w4rtynfv9montZHugDjsVHFAYyP64anPVwugmcbXL_oGxY8fR7XrBVsJNEaLZogRJOWeImKMLNhrPOq8N7han8oTlwNE-4AomP6e2veaaw82oUMuPDv3MSHEaImXDwG6ZPi_LPmOuv4lu1ivkmR10xI13nIcLYGJPi6mfwL8FJpw8AH2BJfoD-e9rMaRDkIQZrjptKx2aHtc0bYCgsyuPifSAdVkY6TUMV735vLSD9YSnQ_9STo31XobJbw6UqjKIKU9WF356WcrRPvskI0UnspusdPBTVFpKfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در راستای پاسداشت مقام والای شهدای ارامنه
آیین رونمایی از نمایشگاه "شهدای ارامنه
"
🔸️
با مشارکت
بنیاد شهید و امور ایثارگران استان تهران
و با حضور
خانواده‌های معظم شهدای ارامنه و اصحاب رسانه،
نمایشگاه
جانم فدای ایران «شهدای ارامنه»
روز دوشنبه ۶ مهرماه ۱۴۰۵ در ایستگاه
حضرت مریم مقدس سلام الله علیها
رونمایی و اکران شد.
@metro_farhangi
|
ایتا
|
بله
|
اینستاگرام
|
زیلینک
|</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/465294" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/465293" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEbRi9Dd23klSqsXwZ9ic0QWN5U1Ln4zQEur61-MOSVooJaCNVyJPRc-aT7xs_IJaCosHHQBg47cVIuIRwM_d98vcVggE9Idm30lg8CNpwITf9iHberhuw7dI9eOSZx0YxAiZb5MZV917r7PwF7ERXHc80JXBV8V36BeTyWcOVbIqs085yQuJM0Z_hDXzjMAJYCboAfJMBp_Zod4AADOu3R8m1SUK-GnXyyHL-Hxw30BIXkGeUN_HV2S-hhClS_SkWGyrvZX1YekvxBUCF1oTHcb7s7Z0bcs8cAGh9y6VglXGykOecuyztYDSQOC_b7sSJkcrsCVVOfuj0MuWXMiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: طرح «تورم صفر» با ۱۲ قلم کالا آغاز شده و قیمت این کالاها ۶ ماه ثابت خواهد ماند
🔹
برای هر قلم کالا متناسب با بُعد خانوارهای تهرانی سهم مشخصی تعیین شده؛ برای نمونه، هر فرد می‌تواند ماهانه ۲ کیلوگرم برنج با قیمت ثابت خریداری کند و خانوار می‌تواند از میان…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/465292" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8YAtsucavSU5aBJOuYC7UEzv4wkzMCpT08UA-CgPHRIBJL6EqDDv-5MthkCI2HO163jKs99FsFuuha8x8lBNLphNcu3zLrQ9De6dMNEeKbYILBBGSjATvqHNpcWLLaKWxRjADWtv4IqR44mFtAM4y8qk97UXahU68Eck6yoqC2lg70DS4_8SHiTMvwBWnAwEBdKWiHn7BowGZvEgMojqSSFqTd4YwlkxinhyzTVpn1t30h7U_tnX_gfaP4YstvsapLESHwlrxMS4B7DccWQhdYvYOitYdFRlLJWUClZsYtslobi-EzxhILBDn68S9NSjvbUMiRH9KNvZyZEW-i9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط توهین‌آمیز آمریکا برای ازسرگیری پروازهای نجف
🔹
وزارت خزانه‌داری آمریکا با صدور مجوز موقت، شروط عجیبی برای ازسرگیری پروازهای نجف اشرف اعلام کرد.
🔹
طبق این مجوز، تنها شرکت‌های هواپیمایی عراق می‌توانند اقدام به جابه‌جایی مسافران کنند و شرکت‌های ایرانی همچنان…</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/465291" target="_blank">📅 16:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maWJ_rLG-F9Itpn6NICrZiqLmMUIe50Y_SauVruE5rrppKYwLaJYafs8ckMjOAEJj49UE0IWhZdgB8uRHDENhrnixgL2jy-J_KMYKAK2DEQeIQvPnYRcWHjKbr3I43QXlMKv5aCcZ5VtMtLIjj4SlY0EoJ0l3bTOlXF5DGVXxxSEp-phcEd1FoxOQ5720vvfnxDnKJnfgfihvYl7Wi7JDHwUHDabukyZM9iEQnZ-PXUlRCZXKwiuh-_o6PfMPB23WbAyvzWOGEKhHYmOlF8t0AcQLrcZr9rFszB_G1CxMkWyw16nXrTF6w101mlEEKp8VaKRN-kcccgkZxIQvdai6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۴ درجه‌ای دمای تهران از فردا
🔹
هواشناسی تهران: امروز دمای هوا در استان کمی افزایش می‌یابد؛ اما از فردا تا پس‌فردا، به‌طور میانگین کاهش ۲ تا ۴ درجه‌ای دما در استان مورد انتظار است.
🔹
در بخش‌های شمالی استان، به‌ویژه ارتفاعات، رشد ابر، بارش پراکنده و وزش باد شدید موقتی مورد انتظار است.
🔹
از هفتهٔ دوم مهر تا دست‌کم پایان آذر، انتظار افزایش گذر امواج بارشی از استان نسبت به میانگین بلندمدت وجود دارد و به تبع آن افزایش رطوبت و بارش نیز پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/465290" target="_blank">📅 16:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465283">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAOt3gFd9DLli2akEt00CFFtQzo4cEmituGTKWuHqdqj4PdXIEUYuQp6I9bhQEFCDLY37DFyP_9tKMix9mbnWDlcb87SKUmtzHvwwMp5JlbOr9Wd_GEYxqBwCH66golNMpBsH2G0TLnVw24dhF8UkP3KBoVhgJsC0fRNebp-vR1DEcKwfitUMefEweVWo_954R7-6uS7JI50XM5VPFRM0Ozxa1Bjzl9yEr_e3PMV8tpL-MgIRjiaoUfrnHBCtFGO86FhsICyoKJmmFhILNJwIuS9NF194GuGwq3mHaAXuqUDLgAWKVxtKl_tbyjk3lJjRc4VdTLbK82WawMMIi8I1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twyzaM9Q5seS55eNAbiwLmoXnONK-2oCFxvhfoPRhEW6_uvI2zoHS_notUDo4QQMmNlBFIzsMAOnw_NTHuCcr_SC7EfXJGqFdKWUENgwSrP9X-G2jenOf83IQSr0lZE_Nl4jLitmy7nDfMZpMPhUGJPbpb1_DNmIis5-_iIVtfIgtLIB5N7gFVS2IJqUGgkRVYN47YaYK0nWN4tbL6HS3AH4gH7q2ShpPLzFDK7OisEMT5jWa3sOrIS9mpl1Xn7XTBrg5g5RFY362kdQOCesxvu9tx7Fo6K7FaZwNaiiH9ZRluNGszeWvlu_obyxZAyFqH9R89Zp48K6waaLaYl5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhCN1WbSAV-jFiPAfgJi-hLbMOPYbhyXqE64fSsWSW0jaz8AqZUfsz-GKi8ivpgwYkKyhoF2iads2gPizMc2ffnUkX-6_-kybsaAS9eN6-nolrq-WnZrtgmxosfuc7HzcRFpJ_siO45Xl6JtTHGgKtbMlKumf-b_iGnkRZH0sNGUgj2XfvCyJW42wV0Cu5vRksRSUdXZnp6y9DZk-1xzBdA_biA55CqNCXs797_4PTaigdO63-5XPyYioOneLwgUUwxk6UEqU_Z-12FN7IsockRVpxefiJuM7MbJZRljj1nZltqqp1DF9uzAT27-IEN_fr4sgjTR_n7NGUt9H2Ux5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3d1_bySFiEVUuGIOIFagqtZlO6eNgNQ7BC3WOZbEnbPfaa6hQOvbLIvQELWQ5h0X-B_DSt4K-sYUCmdnBI-m8IXPZeBgxzfPt4dz4TopcK1-rFIYph78Bh4WDRKE9eTfYGwdLN-a3YwjjPEXlKatjkZzmX2GOURwQqReFbymMjyw_m8EoAp57IqeJmni21_qqXyJu-pakLOfVy8ZBLlOZLGvbGgqcP9c0B8fvgYnUtTUD3jSpfDsO5rY0YrW1DFHtIR1tiJk-o5e1qwF1ODUJpZz3o8UGpvWPVFGsug2cARIG52cTDyqADCW6TYC1VegOOWPCM-yOf-Rqi9aW9gyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eImyUYZ_TFFQvGY5h7kGkiTvyZ4NFrMGX7kaVv-eZFhHJL4o68mhpUAvxenDGk2Oox6NVNs2J_u4PWMByapYvHAG3wPJfXTnxeduX1QiDbHUUfRptEn8C--N_pFInJNjgcs0ekD0FrN-zLg1TlQhgBplGtuDJac9hHjyR-dIJS11soJJrdrsyEYT-rgWizGSOhvASW_CNxNxeFSCLM3arVQr5tM03ywGV2Gy6LQvFcb82FM64R0ILjvWRUhVG_CJBHz4VCcvr6AD63BgH7cAT9FIB4M7Y-j-Mnk3Y5qAj2XhOf6WVAh8T_SlSwzv43OocfMaLUtTz3yzcJWiKonLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzPwHHTL0A9-8QnpL2_jTWDriAeAC64JMW8o2cCiMWiebYVxBnv5JPGswXkGDHDao6GXs76hNQ1LmX7WOjYczmeQCWjvauhGlc19fAINz3IBCnc2-T5qNCOnKj6bN7fNuRzLilTdhakxjUlwH4ddwTVu11zx4uSopDE6gCz2lGrIMsvadu2FMU589EwKRrAAJmXHnz4h27LRUyEWRxe_UJiSrBcaPZBn3HexZUuTzZSf6kCsx2sWqth12R1KTy282XaooiqsGCXCO8OLRv8-AaVOzXeiePIfawHwQOUHtPIG_d0jejUbmyYmDKch0odyZGNlEKQz7NSqHkypZllouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4QHwXYV7MaM8l7T5isKyL6x2UjbIb1viyXIsl3evWgm46DOjZcgHucUYJbjngGgISZldaXnzXbGr0qNdKTdAvkKNUs7wliFvGtIfeKq725CslNmf2SJoDMUSgMnt7GfFWFUghIZeiCvejxQjFRK3GgetxpWhv5bui4NKNokyEpe9wPadyUM6cTo2XQO3Y8PwVN1i35AHpZwHPwTUIsiWm1FgeAuICntqLm1bNP7fN-5KsNccQBFeKy9o6YZgIpMjYHLc71nV4u5JNAXKrmJvEHtMtKTZl_O2IPwMYQfpzNkas_dc8HvLLQ6elWqitBK7dQZq9hqX0sU_27fJpTcsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردانی که به دل آتش می‌زنند
🔹
هفتم مهر ماه روز جهانی ایمنی و آتش نشانی است.
عکس:
غلامرضا شمس ناتری
@Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/465283" target="_blank">📅 16:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465282">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOfxtUDTsrTBDcd3BaEVRs4jDK6pDOkdplpEJ8Bcs26lOn5pyCg68SQirxGKZQ1HLITpUGOw9Ku0ala3tU6AjcRI_HINYfqlsGbPMsf8Hw4WuFIEiCHtYK_RG9hLYkSzhdb_hqjhsPZuTxxDRgJ52XTg7z1QTta82X1xQt-1Dw0en_8j87Ft7d1yvHl9DNwRJdh9etgI90NaugTA_5WDBAxD_1Yhp9UFIysOrW86jfWFFLJW-CILYZ9HXOzNs11Gff82RAQUc5ZNytNo2QPjqRU25oFj52oY8IDEiwY2ZESk20_F8KeUg_eeyF5dPOL0IFTxE9QZlmXFWzRQvJAkVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ اصلاح‌طلبان به نقاط قوت ایران
🔹
ایران در شرایط کنونی از مؤلفه‌های مختلف قدرت برخوردار است که در کنار یکدیگر، این کشور را به بازیگری مؤثر در عرصه منطقه‌ای و بین‌المللی تبدیل کرده‌اند؛ مؤلفه‌هایی که مجموعه آنها می‌تواند جایگاه ایران را در معادلات جهانی…</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/465282" target="_blank">📅 16:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465280">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5065b7d248.mp4?token=n9Fb124YPzoY03Es7Ipxr0vJ2mMWVs-7B5be5CT3z9Eyn_TN9o3xoENoi_v1ku26egsPggHPkBsNrCzBhwmKPBcWQ_ljWzWdk-h0FTtqumAZd9EU31adE3M67H2f8hyrfOi_bKYbxzcT0zAK80O0mKYarqmHvF27xtMy3lm7HZI4Q4K6R0eb6QfaXrX7_-ef_xCzSJDtpbNDCE1EycwKGuowa6VvLJ48Sa26UOFPtVGOGrgpliN05ArDuvw6MRhscXL39vu36Nwxfx9w8OhDSvvLarRkm_JCUBypLa3_Cfdjw-QyLBrUaGzvhG6wR5Bjd3hQ7pwEa2U1-ztbbb0S2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5065b7d248.mp4?token=n9Fb124YPzoY03Es7Ipxr0vJ2mMWVs-7B5be5CT3z9Eyn_TN9o3xoENoi_v1ku26egsPggHPkBsNrCzBhwmKPBcWQ_ljWzWdk-h0FTtqumAZd9EU31adE3M67H2f8hyrfOi_bKYbxzcT0zAK80O0mKYarqmHvF27xtMy3lm7HZI4Q4K6R0eb6QfaXrX7_-ef_xCzSJDtpbNDCE1EycwKGuowa6VvLJ48Sa26UOFPtVGOGrgpliN05ArDuvw6MRhscXL39vu36Nwxfx9w8OhDSvvLarRkm_JCUBypLa3_Cfdjw-QyLBrUaGzvhG6wR5Bjd3hQ7pwEa2U1-ztbbb0S2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طلای دهم شیرین‌ترین طلا شد
🔹
علی داوودی نمایندهٔ ایران در دستهٔ ۱۱۰+ کیلوگرم وزنه‌برداری مردان، با مهار وزنهٔ ۲۰۶ کیلوگرمی در یک ضرب و ۲۶۰ کیلوگرمی در ۲ ضرب با ۳۶۶ کیلوگرم به‌مدال طلا دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/465280" target="_blank">📅 15:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465278">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTen2bEL9zOpYVrg2a5NOP9cJlY4FTSn9SznwNYNTK_HBDUJw4c9sl0820MtlbjBi3Jv4YYjYax8pH1qg-wiyVXhKR8ZSfjtWqDooP5QBUK-2mHQRVhCr4ab2Be-svst2iLEx2pT29G7FnT8EXIYQxavpzxVQp6R4AkwHhVK9sLJ1Z3TRTnkRPi9lVyiC7lPa2YpZhvxzn8adexetszh3LfA79ZsQerQSEvjNr-gatkIJBR01zlthqCx-8sINqkjGK8Ntrm0F6KCiNExR48XKlIlu0K3rGafdKREj-pd1RMuJYnkxkKupskVpRbeIcvQndshEX3juZAtO404vlVqyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی انگلیس هم اعلام کرد که دیروز در تنگهٔ هرمز یک کشتی با اصابت پرتابهٔ نامشخص دچار آتش‌سوزی شده است.  @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/465278" target="_blank">📅 15:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465277">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB2IK1bIpp0OQM_dHnL8wUcKIEdJJfG4AjO9kzVYuE4T_bCdCbfSJ1ft_ux7DD6ltgmKq_2l-s0szQ5Ele9ISSt8-UowgswOEy4mP8C1ZIjuHz6X0ZByK_dAmMrDmeoQCl2raeRdK1EjDCUy4vPr5Ns4rJMFhpYSSt5Aa1hrzxkiudomI9uYRfJ0Ex9Wbaxv0GQvWRHkGYUxAsgpl4qSxlUThC_XBrHFe3gEo83ts2ka1efPdQv4p0NxXlGNGjLcnYXKifendZDOlglIbBTg4ClNeuTvr-xw0wWJCvhbA6CufnxJELCeQ8xO60nG9i_SJa__8HINsX7BaYY1WnkgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید بنزین سوپر مشخص شد
🔹
در معاملات امروز بورس انرژی، هر لیتر بنزین ویژه(سوپر) وارداتی با قیمت ۱۱۱ هزار تومان کشف قیمت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/465277" target="_blank">📅 15:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465276">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678142e59c.mp4?token=KT6L0j37CcHNqCY-r-EGE50SP0OMwH8zomM6utNYFqZxpsmKXXYxDgmC-h4R5oHBx3L122LqS_kN-cP-anGd6ADieKaM-EFb-WMeX8UyjloIfXKdAWYvbtejZUW7HFyV-gD9TlyNXYb9KmcWg9V4RMswrc6EH82Vlwc31DI8k2-luFtXxqyrtSWLlAZ7TBY5gvWXbacPt0AFAhltMN7Mhl3eKef_rppwWG2d8IdDFK9KaYoYuP-E3zajsEvOb3SfA-C2teMNAI7TaeM48RnmCZlpuIb479oJw7gO7RG8YOEBeLmuSfoPyon-TiuKKYXMV5GA6Z5bKHaZBGn2NdwFLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678142e59c.mp4?token=KT6L0j37CcHNqCY-r-EGE50SP0OMwH8zomM6utNYFqZxpsmKXXYxDgmC-h4R5oHBx3L122LqS_kN-cP-anGd6ADieKaM-EFb-WMeX8UyjloIfXKdAWYvbtejZUW7HFyV-gD9TlyNXYb9KmcWg9V4RMswrc6EH82Vlwc31DI8k2-luFtXxqyrtSWLlAZ7TBY5gvWXbacPt0AFAhltMN7Mhl3eKef_rppwWG2d8IdDFK9KaYoYuP-E3zajsEvOb3SfA-C2teMNAI7TaeM48RnmCZlpuIb479oJw7gO7RG8YOEBeLmuSfoPyon-TiuKKYXMV5GA6Z5bKHaZBGn2NdwFLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترس سربازان آمریکایی‌ از تلویزیون ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/465276" target="_blank">📅 15:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465275">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853b0a4d36.mp4?token=Fza9apmj6i4ivCRDKAtWNesn6AKm07p8ArW5_lHGIR4OHIQQWoKfjOoR8UTnpgvEUNpSE8QAScyUl4Op6o-MDzaMqELTazAKfEzGmtRGvEJyjL1nIsPtIxUHNYSUS90bqm2ywvQkzbDuEYnMKI55jaZNxKJbx6Xu7UOHRFuXelwpItIwHYqFameaZZRiaVRYpWTA0J9ewOPPOQAhiNYDnXjjLknzUIFQIYuuXnlvVioleaDb6ZWqo62f3zpmgWDM0p1-8_g8TXlgxTLXS90meq_-Gfir3z_G5eEZQabooEqv9WDkjqElA3IaXw0-hkXbVLLsFdu1m6Nzk033gzVRAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853b0a4d36.mp4?token=Fza9apmj6i4ivCRDKAtWNesn6AKm07p8ArW5_lHGIR4OHIQQWoKfjOoR8UTnpgvEUNpSE8QAScyUl4Op6o-MDzaMqELTazAKfEzGmtRGvEJyjL1nIsPtIxUHNYSUS90bqm2ywvQkzbDuEYnMKI55jaZNxKJbx6Xu7UOHRFuXelwpItIwHYqFameaZZRiaVRYpWTA0J9ewOPPOQAhiNYDnXjjLknzUIFQIYuuXnlvVioleaDb6ZWqo62f3zpmgWDM0p1-8_g8TXlgxTLXS90meq_-Gfir3z_G5eEZQabooEqv9WDkjqElA3IaXw0-hkXbVLLsFdu1m6Nzk033gzVRAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیین استقبال از ورزشکاران اعزامی به بازی‌های ناگویا در زنجان برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/465275" target="_blank">📅 15:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/facc0d5c41.mp4?token=j7t6m835y4vBg-GfQwEhTeHUMnKPPLmVd-5L8SLw9ZDVrW1cOTj1LD0HRVQnbLIBbpMMU36MfiMzPbqZZFCYt7Nmfq6MdoOvA9wpzZha9-bhVBxAWPd_IJeDlWL68etSkbiKrwCsd6ZcSI2oO-M2YkN530lUatOaqMpnw5EiObKsvpO210nq1fUmT33SjrG3CNPOGPC9083XHPoqlYdHX-V6ASDI09nqdbGBK3xGS-UnvUhabcTv9j8thwhPW3kE_Z_XtmaxNz0a0ZdN1veoPJU1nmcoNYdOx-VlWA40yOBHIP0BX0qXc5v67n7_WINlVgPW04J6ShGnJu2_BECFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/facc0d5c41.mp4?token=j7t6m835y4vBg-GfQwEhTeHUMnKPPLmVd-5L8SLw9ZDVrW1cOTj1LD0HRVQnbLIBbpMMU36MfiMzPbqZZFCYt7Nmfq6MdoOvA9wpzZha9-bhVBxAWPd_IJeDlWL68etSkbiKrwCsd6ZcSI2oO-M2YkN530lUatOaqMpnw5EiObKsvpO210nq1fUmT33SjrG3CNPOGPC9083XHPoqlYdHX-V6ASDI09nqdbGBK3xGS-UnvUhabcTv9j8thwhPW3kE_Z_XtmaxNz0a0ZdN1veoPJU1nmcoNYdOx-VlWA40yOBHIP0BX0qXc5v67n7_WINlVgPW04J6ShGnJu2_BECFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رادیوداروی ایرانی برای تشخیص انواع سرطان‌ها تولید شد
🔹
این رادیودارو که با دقت ۹۵ درصدی، سلول سرطانی را تشخیص می‌دهد، تا پایان سال به مراکز پزشکی هسته‌ای توزیع خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/465274" target="_blank">📅 15:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465272">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c03dde89d.mp4?token=svdHWgDVlnl7xS_hHLluxL99ZKSZ-ISKaWEtRcR0iPTJrWpsuXuL0C4fHPdU0i8Ml4deXmKCTzys0Y6MuvQxXLH52948AP0kK3rKcXcwbQpt5okLeS5DdmUIohKD47xyqqZi5XrLAJKlaDfoomjROW25_0YgO3xiu7bPDZP5yj8ZjmBmRwJtYVv0zcapYngDKjeGMghDUqUi_AUrX5_m1oB8hgKKx7QStbO4lyF5--VKNNVUJZcwx1NGP2uacvRqDn9S_UHHEtvCbtWxdgrWEvSTU62eK5A0ndyr5IJA9pJstetFmJ6IH5BBhpvMnqnbIR7elQ13nioLL0AOlagJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c03dde89d.mp4?token=svdHWgDVlnl7xS_hHLluxL99ZKSZ-ISKaWEtRcR0iPTJrWpsuXuL0C4fHPdU0i8Ml4deXmKCTzys0Y6MuvQxXLH52948AP0kK3rKcXcwbQpt5okLeS5DdmUIohKD47xyqqZi5XrLAJKlaDfoomjROW25_0YgO3xiu7bPDZP5yj8ZjmBmRwJtYVv0zcapYngDKjeGMghDUqUi_AUrX5_m1oB8hgKKx7QStbO4lyF5--VKNNVUJZcwx1NGP2uacvRqDn9S_UHHEtvCbtWxdgrWEvSTU62eK5A0ndyr5IJA9pJstetFmJ6IH5BBhpvMnqnbIR7elQ13nioLL0AOlagJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: هیچ تغییری در مواضع ما رخ نداده است
🔹
درحال‌حاضر موضوع ما فقط تنگهٔ هرمز است؛ بازشدن آن هم منوط به شرایطی است که به طرف مقابل اعلام کرده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465272" target="_blank">📅 15:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465271">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
تصاویر واقعی از عملیات‌های عجیب‌وغریب آتش‌نشانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/465271" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465270">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5oqXuT8IAmh8gDQwAeXYhRuw-Vuj_YhTrBGh6HYLltdBablR6G7pxlUzoWwV5CY9tP1pviV4Z81-fBRM6_WtTzRy9biASiX6TAb60oWfNm0iIJMHh3Xv6sUCVzFqMBAyvaTHxCS7IWmcJvuvOCa4pCPcLVQh0tz-BvkNgmGzN-Xkgshfzoo-WI7900jZ6bWZBJH6a3BS_LGf0tofa88vw0zBqnuQKTkyuhbsyu2Tzjnj99N2IiVhDORLALQ4dx8KLdYwQlBxMtQBlotcTjtI2ldA0J59tINjGZpDM327Ypem_GMUo5NjmmqT29IagoSyaDXXjZu0Zv0kGMP4rw9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط توهین‌آمیز آمریکا برای ازسرگیری پروازهای نجف
🔹
وزارت خزانه‌داری آمریکا با صدور مجوز موقت، شروط عجیبی برای ازسرگیری پروازهای نجف اشرف اعلام کرد.
🔹
طبق این مجوز، تنها شرکت‌های هواپیمایی عراق می‌توانند اقدام به جابه‌جایی مسافران کنند و شرکت‌های ایرانی همچنان حق ورود به آسمان عراق را نخواهند داشت.
🔹
بر اساس اطلاعیه وزارت خزانه‌داری آمریکا، این مجوز تا ۲۸ اکتبر ۲۰۲۶ اعتبار دارد و آمریکا حق لغو یا اصلاح آن را در هر زمان برای خود محفوظ دانسته است.
🔹
وزارت خزانه‌داری آمریکا انتقال مقادیر عمده پول نقد، محموله‌های مربوط به دستگاه‌های اطلاعاتی، نظامی و انتظامی ایران و همچنین انتقال افراد تحت تحریم را ممنوع کرده است. یعنی طبق این مجوز، مقامات و شخصیت‌های ایرانی که تحت تحریم آمریکا قرار دارند حق سفر هوایی برای زیارت عتبات را نخواهند داشت.
🔹
همچنین عراق باید مانع ورود یا عبور پروازهای ایرانی از حریم هوایی خود، خارج از موارد مجاز، شود، در غیر این صورت، مجوز صادر شده لغو یا اصلاح می‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/465270" target="_blank">📅 15:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465269">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a988378ca.mp4?token=lby_bDGxdAOpUsh4_K2RxXYEuaqQlTOSTchPSlbMoNxGbaX2s_R9cyU6lMdSVlcbcvNQM5iOspUzgg3nqq2rsPx06zDrsQJFWej1d4838m_ckSXIdf43IjmH9JpdgKN95-ZV2pIbreDyE6MkbyC3Q7MkoMYXUwBKsqwwfRk8ANvLXKaKLOyr2gOu7YzVd8Gbn4TYuufFIe9bYI4r98cNiL9mhUftP48RXtjBvurZGJbG8JMpeHvWK_oDo1RTbyx8Lmm4JSImheDli-SNBykJpgY_AjyyX0QudGTKp-fTMmPmk-O1dyM4Q0TXM9t2X7qwkIwSSgpSFV3ai9t5pTUK2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a988378ca.mp4?token=lby_bDGxdAOpUsh4_K2RxXYEuaqQlTOSTchPSlbMoNxGbaX2s_R9cyU6lMdSVlcbcvNQM5iOspUzgg3nqq2rsPx06zDrsQJFWej1d4838m_ckSXIdf43IjmH9JpdgKN95-ZV2pIbreDyE6MkbyC3Q7MkoMYXUwBKsqwwfRk8ANvLXKaKLOyr2gOu7YzVd8Gbn4TYuufFIe9bYI4r98cNiL9mhUftP48RXtjBvurZGJbG8JMpeHvWK_oDo1RTbyx8Lmm4JSImheDli-SNBykJpgY_AjyyX0QudGTKp-fTMmPmk-O1dyM4Q0TXM9t2X7qwkIwSSgpSFV3ai9t5pTUK2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: هیچ تغییری در مواضع ما رخ نداده است
🔹
درحال‌حاضر موضوع ما فقط تنگهٔ هرمز است؛ بازشدن آن هم منوط به شرایطی است که به طرف مقابل اعلام کرده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/465269" target="_blank">📅 14:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465268">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a31b4653.mp4?token=e7L6cDsp9KS3ln0GBmicRPryys5yfjL_uwZBepi591AlCU8n6s_Cs1N5MMjBUYQsOSwBPGBIEne288pjeyCro5zBBaNISsPukc-I2YOk2SOb-m7YE51nJqFjJfFZ9XVvr6jEXEcIBN-UumAT4z2kFm2gpZMifBsz6BBVJJ9Wdi_1TXlVl1C5SbZk8q3_VrobdAaAxOIY38xkNAsvUf8YwwVjNCFv5j5rP0GoDY38DZLNiElaAO23SpMn72oHc2ElJy1vNCK2zlL8yqv9qeVp4VtKj_Ljd-YM5EJs-D1hoXc_1UItsAMiDLreO8tCTRMjzEBI16E2qNxizONiqYgsQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a31b4653.mp4?token=e7L6cDsp9KS3ln0GBmicRPryys5yfjL_uwZBepi591AlCU8n6s_Cs1N5MMjBUYQsOSwBPGBIEne288pjeyCro5zBBaNISsPukc-I2YOk2SOb-m7YE51nJqFjJfFZ9XVvr6jEXEcIBN-UumAT4z2kFm2gpZMifBsz6BBVJJ9Wdi_1TXlVl1C5SbZk8q3_VrobdAaAxOIY38xkNAsvUf8YwwVjNCFv5j5rP0GoDY38DZLNiElaAO23SpMn72oHc2ElJy1vNCK2zlL8yqv9qeVp4VtKj_Ljd-YM5EJs-D1hoXc_1UItsAMiDLreO8tCTRMjzEBI16E2qNxizONiqYgsQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلاس درسی که در محل جنایت آمریکا برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/465268" target="_blank">📅 14:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465267">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/707df41be6.mp4?token=eJEmpJxbiQMW82nbW82PvqmEoS25c20WUJkHD02UBaxD4WFolPlhIXNycIBZ1f7WCTtEyCmniMfXBlqqqR0pCNfJEIKSMbE3VtN5Te3IGy8_xdCfCZf4D714885BOB_WpVxnfgcYznmjy_sfQJnMBlqL3V7V2X9OVANeCNBpuIYcUIXstOrdC-7eqR0FAK20PYxjA-b_GcPO5d5pmeRPojBQb0Zq5rqlNB-ZL7-Hp1DoBRLyf5m9TRETCkB16KBIVoQmwc8lp-jB94UcBjoCdWspT_sw4G-SxfJ6Tew0lsN0CDf40PNsbwUHwttqbXhBUIqAhhs5L0s5E6pNcKw2LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/707df41be6.mp4?token=eJEmpJxbiQMW82nbW82PvqmEoS25c20WUJkHD02UBaxD4WFolPlhIXNycIBZ1f7WCTtEyCmniMfXBlqqqR0pCNfJEIKSMbE3VtN5Te3IGy8_xdCfCZf4D714885BOB_WpVxnfgcYznmjy_sfQJnMBlqL3V7V2X9OVANeCNBpuIYcUIXstOrdC-7eqR0FAK20PYxjA-b_GcPO5d5pmeRPojBQb0Zq5rqlNB-ZL7-Hp1DoBRLyf5m9TRETCkB16KBIVoQmwc8lp-jB94UcBjoCdWspT_sw4G-SxfJ6Tew0lsN0CDf40PNsbwUHwttqbXhBUIqAhhs5L0s5E6pNcKw2LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نامهٔ سپاه به مردم آمریکا منتشر شد
🔹
سپاه پاسداران در نامه‌ای به مردم آمریکا نوشت: حساب خودتان را از اشغالگران فلسطین که خواه-ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.
🔹
در این نامه…</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/465267" target="_blank">📅 14:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465266">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90885e52ae.mp4?token=o5BHGfDdF7piCn_1zeOz6INy-3V2su9MHqx0asJNzRInje4_2mzNBrvbWsScSiXR2nsXGmuNmIMs1BFKTKNxLWBkFT7S-7raZbqcreCKOnBDjQmjs0YDj2xEUbpb5mfsG_Na6nNhLLE5fn3OMTgk9Bye-aXPCNPA9ioDAAsNSKYWJQUbcTo8cKMe9OQ7wYVyDRWMuci2TvOfX-1xKoX5vctWKYqwNPQMXNrCB50BqA-4jIAvovMEUVSYurAD9wBni2dSA-yOyJp0YKbgQ71Ndj0h0wRzBufbF_uuYRu402ulKHY3sUzJSFifh5el3bvwturqU4y316C5S2tRW09c1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90885e52ae.mp4?token=o5BHGfDdF7piCn_1zeOz6INy-3V2su9MHqx0asJNzRInje4_2mzNBrvbWsScSiXR2nsXGmuNmIMs1BFKTKNxLWBkFT7S-7raZbqcreCKOnBDjQmjs0YDj2xEUbpb5mfsG_Na6nNhLLE5fn3OMTgk9Bye-aXPCNPA9ioDAAsNSKYWJQUbcTo8cKMe9OQ7wYVyDRWMuci2TvOfX-1xKoX5vctWKYqwNPQMXNrCB50BqA-4jIAvovMEUVSYurAD9wBni2dSA-yOyJp0YKbgQ71Ndj0h0wRzBufbF_uuYRu402ulKHY3sUzJSFifh5el3bvwturqU4y316C5S2tRW09c1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: زود است که دریای عرب هم خود را از حضور دشمن خالی کند
🔹
آن روزها (روزهای سلطه‌گری استعمارگران بر ایران) ۲ دریای جنوب ایران، جولان‌گاه نیروهای دشمن بود؛ ولی این روزها آنان به‌خاطر ضربات دردآوری که از رزمندگان دلاور و محافظان تنگهٔ هرمز خورده‌اند،…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/465266" target="_blank">📅 14:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465261">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twaA3m44zwILkpvZrHCVMYu6d71XzqdcxXRmRM_kcPm0dD27vo2O_eTh_VRgufvCjRP9h7llLvneUqq4xc7coX7Svz4zCm52iPHJq8AKzLSJCZkvV04oquCKYAMQlQIixKqCSZ_6j32RQN-oUMdUyigkO4fRL5znF0BRuOSd3bSAQS6nNRlzBwBlum6zmqKQObascvq1iKggJA54QyLgffDAz9Q183e6HTKCwHp4AtVNPDU1UGUXqfnhkbBdB7vlEcKofOWComN8xP54K2qJiyjOsDQx8lYZnUS7eetMORZwTn6nKPIgdZMSagwwk4_TiMWQ7o0G8BQ13m3o8qfBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDHBrzb70hahhpKlEaglChA-uvhvWv8HPFiZwkrJfuBMlvotFdFhPCF6ZsQeiPhcWBLHrHq4LFCMPE1ZW8Bofg9UyqBrhA7Ao7UjGHsnIIAuE4DNyq8GM3JMGL5Emqscu47qo6LUktYB3p4jhrkLXwC2MHARdp5qOfwADwnkUFOg4uU7QIDsB7LARXnUg20gcQGmTem940yXdjfvFvHQPFlboTO1lSuFB6DUuVyS5R7XWIP_vimPF5SJsLKKsNaJA43cT2qavAUl91g_xE517-EkvcCuk9WC1Svk0-nIE_KMHsQ69rYxbhZzff9UxyGZ5M4pX17PX1VKjqNgCTyaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpgHsVhoACl6teQy4iFQtOi3F6ZHJEYbRsQerHPZ8IYmvWVKZEFTruxDFgzvjxWXcebfrRIqnaEdWX94ee4Iy5r1X12RJ48VqaV9Fc3QHnJE0DVYDnXIpo5Oln4jGIs7uibW-GOcDkSHqOYJJfwO61IMGOEWfQlGqX3N3Fj8IUjit3NTPrrlWWQSGeT_LPIVeKdAUzE3a8ucbRlyQh3uJepFengi6tzmopccV_4rQl5WWt3T-2zqvJD5nRGj8sVFu9mcxlspVwHH-VL2TqHCSTTMA5_OdwN5b3Lvx8E4fS9Yk5gfauWVvm06j7E2YpHhy17Kg1bMxJTw_TPPLTSj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1YWnP1_OG2eI8Q0AxaZDdgwEcgTRpFUiOT7YGc0FvzwtDv4OG3RCoM_4mFF6FJH9oawnR83oHAyWO_uj3Id3HBNfVihwCWVKHCh_8T_X1JUgULGMMLR19LNIr0isljsV-4GEdKvuj5MG-iwtnHp1HwL4uphUpkOneHmvvWREuEGSyBYn3tCai35OXx0E8LaLdzgo_VXyGLKs8LkJscWKSxspQja3VK2Gu06mA7nPJudPik4EvWaYjx_mrnaj1pqLDI80izY-JrUoJaxWRqXbf4cq5C8AFiLU3slGHYYSFR7QiozPBu5CquYYFBSJPrlmqpDa11E1ohL_VzGWW7BjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaD5C55RUiwS31XVXJNb9lsHku7a2WZhuox-0A34qW9WBH5bd7HfabLpO_OYAJwW5SsSphFdNRSrHpsk9CUSOU09urZnEhMId2JiIAw2U-BEdvUpH2uGw5-woK9_IKCMM6eTid--m0XC69vtPx9daRirzlMsOfB9__T3jufZdbzzg1MkIYvsUnGdLTPyiPlWW-Ar3hpvtiQlCafLU2p7hG6p0nwQHcgDPUSqyYBiVM57Qi9_9O1SiVF4PIDyOd9DIXOZvZdc_SWSPe3TljTuLX9c6a_qxORIn-r3W0cTw91gBd3XO31BWC8YoLpJeS3qEB0O3OxN-96cUHQrF4TfNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست رئیس‌جمهور با شهرداران کلان‌شهرها و مراکز استان‌ها
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/465261" target="_blank">📅 14:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465260">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuNlYdkNgk27jaVtzxWZ9lgg4caoFkcOUcUzYQbcx7WPEuVqPE3ZCIfMXyzr8OZo2Az0mkZT2VrYEiOUwYy8AHgSnRZoMQe-v0nvJ6KGmorcXwEgJvjjCn-5CU5BHcHB68WIjB2C2lFSTNsq6HWxQlJq3f07OGlbz6hirVloRBT1hm5bgl85G1OI5kiXfELg0kMdi17rNbP5xHNShU8ffc6CYjdkQCgO3rSYvk4ZlwIYMcLBVaMtzhyUgfUyLOn_NlPWfknRnGaKu-bvTX027elVblRVFAq87cGc7u58aVGldqtJsZ-rmoi6C-cpI8kHJZlpaKBmMpfhnW65sOLwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚢
استقبال صادرکننده‌های کالا و خدمات از بسته اعتباری سکو/ اعطای تسهیلات برمبنای عملکرد صادراتی در بانک صادرات ایران
💵
بانک صادرات ایران در قالب بسته اعتباری «سکو» به فعالان اقتصادی برمبنای عملکرد صادراتی‌شان تسهیلات پرداخت می‌کند؛ در چارچوب این محصول جدید، بدون نیاز به شرط معدل حساب، امکان دریافت اعتبار در هر ماه فراهم شده است.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بسته_اعتباری_سکو
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/465260" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465258">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت پارس خودرو</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M60RGcFc-WUYLh73QuJz3BD86bf0U8nyKukEJ0tYZu2SaOx-gWbMubD1GV1yTpN_2LJ1nen-wq6mSVf1wAbhBbMhUDoY06gynz1dh6vVQuWfVZWU7jXGwyFSNiExZVKhH7_tuC12q9PCag8XcfcljRp1PtL3Zq4c_UkL24-BmzM9h8sI0rdPadUBpMKNzcLyXuDS6LfoYeH2Emw2OWk0HzNPZ-zoRIv8hZTJ-i5F3u3jmwY2rhILsqc6BBx4ITbaV1swYoQHj8NBf1uLYnUuyob7JQDNk98W2V0HiQVrwRSW3FsJMhTaBf6nAleLvy6zqfNn2iKhtOE-S1oiUCciow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8IMpKID8qBGocwLRf59YWFC8EQLoKA7_CuNPEI0lfMOIfmhA7BGyVt30Cu1IAuuhc3jeu37SeOwJYx3AXX_XlWwvUTQIY4pnxCJ-HfFMnI-uCg0laH6lMAefYJqb_4IV0PKM_CmVjOd5k8doTi_BCxQUWmzOGAtJyzu0I1VC1ExlPLfXMHg9KSqzv2GTtORelyisqcLM33GzDCItt-kmPWd2xg-U66FFASAfuip6WUURuKbfkkaNVBTdpGYPAg5MXATjHNXWdTQLtIKwO1Vko1o96-pAB9TtbHiI2Dos7zHY0dY8TXSN8HNH0fDKM7ZaKlEnPCFPAT0dagLTtCw1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
#فروش_مشارکت_در_تولید
محصول شرکت پارس خودرو ویژه متقاضیان طرح‌ عادی، حمایت از خانواده و جوانی جمعیت و جایگزینی خودروهای فرسوده
🚗
خودروی قابل عرضه: پارس‌نوآ با گیربکس دستی
📆
آغاز ثبت‌‌نام: از ساعت ۱۴ روز چهارشنبه ۸ مهرماه
🔹
بر اين اساس متقاضيان محترم می‌توانند با مراجعه به صفحه فروش اینترنتی محصولات گروه سایپا به نشانی اینترنتی
https://saipa.iranecar.com،
نسبت به خرید خودرو تا زمان تکمیل ظرفیت اقدام کنند.
❗️
جهت تسهيل در فرآيند خرید، قبل از شروع زمان ثبت‌نام، در سامانه فروش اينترنتی مذکور نسبت به ثبت و يا به‌روزرسانی اطلاعات شخصی و دريافت كد كاربری و رمز عبور اقدام کنید.
▫️
شرایط کامل بخشنامه را مطالعه کنید
👇🏻</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/465258" target="_blank">📅 14:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465257">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/465257" target="_blank">📅 14:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465256">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n39kIXgLLbN2H-497bbT341TM_kbd9DxRQisZ2VumSvfEapLNuQQtX2RKeW06HzNiYqrKyNkkMOGCEh534c4kvpPuI23xvBFyVb1jsxuLgnejzmhD6JK1dfP9X-sHBw0Kg4QBgB93rsoxoOr3iddByjEYQJ8K2RZQ7FdUof8h9cGuIvqVzfbqhHoyIFqi3UOjRhDwL4LM7GVOJqODw6HND988hqpbtTTtIK9wb_zHuMoK4CpI4Jd46gM8m0R-SA6u6qHJy3UNeD9ikuPmE4yEMdB6xLdZ2vIs2GwZfUYlQYj8A61gfduvSH20fNAo1-IQDhtd47Eb6HzK1pLtDUS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار کشتی در تنگه هرمز
🔹
شرکت امنیت دریایی «امبری» اعلام کرد یک کشتی تجاری هنگام عبور از مسیر جنوبی تنگهٔ هرمز، در شمال «خصب» عمان هدف اصابت قرار گرفته و دچار آتش‌سوزی شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/465256" target="_blank">📅 14:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465255">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
آژیر هشدار در نجران عربستان به‌صدا در آمد
🔹
سازمان دفاع مدنی عربستان از اعلام وضعیت هشدار در شهر نجران واقع در جنوب این کشور خبر داد.
🔹
منابع عربی هم از شلیک موشک‌هایی از سمت یمن خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/465255" target="_blank">📅 14:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465250">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItK5BxWatGFcjbpQ8HpAnnpKkJCx3-Fv9dgCoIHNEucV-oi7CaEsbCJNwTWjrhWKRCLMwygrNqJuaVqN32D7db2QMF9eHkY9rxvuWTMCg4fD-T0udwm7bHs7HeEtljHpHOxZyaKNmv67t0DuKt_25QnLSlbc-XV5vYeHreSZVqSn6aZCiW0YLoLXV2-eZhUnj9sKln3c0n6gJYamfAmj7cpuwSxl2JDn2EdOuS7d9JSxfHAiA_8ln0lygf512Zlxqu4jb7uiLRDo1uiYXnRpybIw87by47KRzV2URWcZfMEo-_L_H17hZ1ObAKUCOp7YSjkGqKKSOtLNeRobiVF0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwF0k95DSi2ENYOJ9uCC4HNH2Pvy4T_-PQIkgvMC3rhT1-sJr5aLzhNRv10ufo_PBdFK-93z9fXIuA2srAvVciRvPqZt9Stxr2Sj6xeQ0fbbGabPPshskcWLj06qM4LuTO5UInpgYHuxO0jFPJUdEVpLo6rgLuJAvFHj9KxSTbao7cMiGZFTLmxTq9x-7_ur1ra7DiW8DsclTUFqabBFF3S7lC63fXuID7lU3x1Hy-bqQLU0Q4lX6xNGsZvK2S_mYGdQmMWxedsAuQCsm-6CbsSEfUbCKX3tKO-jh7_h-gXFq9KWh2HKuRE2FMCViD3WvFgO0cl-rmqABXsDTqKe5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQH0jhmfUprVobn7pZ8J0sTg8RnURxejdekZAicDk_fNtwpfz3_IpmYgfN_RP6LsU-aeTN0kX5rJQao3pDvB5CzliJT7id4-4nS5fPpenkzz4nOuTbpWwm0TNnbZZASa3R69BTaz3JtznMo8ZJYh_yVur94rgi0QLrtgx3ju3CzBBoWW5A0EmuRlIRmCdAVQYEYj33faI7wLm2unW75aQ5ECw9KFJREh6dkaYQVqGy2xwiEqLibjSbJ1u0WY7LMYlFI1S-2pbU2q3ycYK6M9DJl2Llno0KB2Ke-e1O9UemUS-pG5UbggaC5ZtOZm81q_SGaF3by9-PJpVsMpvJ5CaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVgQSz6IogpsgQG9IWpM0fwJAx_RntIjrcyN9DB_eEl3Ns79PlIBwLi5Il4JFHvvAz9I4sF2ZbHmZaEi2oDzoJZlS1BeeMDZ7uFSkcu0Ho_UqsW2OBivEI9dDwJqzXjYcBlU6vUF5A_foWXvnJ1hYZyLaXqBZl5A4KA8QmxkJE-XTW7j4X3cMuHxWsRX47YVPxVxwotjnP5slSHq9FFFzT8_Gb8EYYcGLbf5cVWlE4_muFe2I6uyW1Tlw9yFBf9rhsN1Hr3jouGUyXvi0IIQKruDiMtUTXGo6PpBwqAh-FeVir-a8EerrGldTrP2R-tvj-nOiSv3LZnOJBwE3S8jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFiwcX9rYC5R4qEAUtZWH83n8RXN3vvSQl-zwIPQv1WH1MHlHYevfWaYEDQrHd1RLdYCdwuGhofrT9FqUgGP5_0cgTHQLMeYjiJW6dWnVg7CcZyGeg_YTQD4huHH6S4oM1-sewhNqbs66yHXwgCpVZBviRaETsULBUgxL-sdg04vjgvEqST8iITtm5NTRjdd4BgpTHgLNaVCoUcuaYhNuiRs2Nf8yqjdZwqpeLIQcewILp620NWIr5dWC4JRN2gQAUAxcCwWYJRG5CNezPtCknyBORVYXn4W2hAiwczueslcdUa41BRsIxg34t4tVS0DPTa03aoA5A9yuiOmC7rebw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست کمیتهٔ راهبردی انجمن مهندسی گاز ایران با حضور رئیس‌جمهور
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/465250" target="_blank">📅 14:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465249">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gytoqXM_EConMWdyytAE_QtBAFVpxF56KwgaX76DrHfBtaip2ruvh2FhaRZfgch9k3kNZCrlsloqjwc2-GJwqcRBowp0o3aDvutKUPSUww_RemmsZibugifHaX_bGiyoAjsUuCxz2tK2G-sp-SandEgD2NAVGgzwM4IGCs6Yu-HeL8UxmnAzrGiVAG3vgwpoR5-1nQdWL61ngHWwNXVMQlbFdwDgpYafKNS-s6RtwvkfCUpMFp1_RSmhgeUbuRvj0KJUxsAFN7Dn-FGkMnOmfHCMiNpjw49hWnZI4_aJf8FEpzRp7iriV-8zkGI6RxpHjmSRrGygv4xW0k2tdlHCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت پیکان از ماشاریپوف رد شد
🔹
کمیتهٔ انضباطی فدراسیون فوتبال شکایت باشگاه پیکان تهران از استقلال دربارهٔ استفاده از جلال‌الدین ماشاریپوف را رد کرد.
🔹
براساس استعلام سازمان لیگ، قرارداد و کارت بازی این بازیکن پیش‌از آغاز محرومیت نقل‌وانتقالاتی آبی‌پوشان صادر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/465249" target="_blank">📅 13:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465248">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2038aea258.mp4?token=g7Hx1EcsPc_E6a63i0gDZQ3J_swYpWYDYqZNRVRo3B2P0TBXcNvIBia24lgaiS4ex2HPb9fWUh2GxivBvLTlHhJY0Q_OrPYgNY1DjV3k9BtLPkDHcxZ_gsN3s9KmvsgPB6o7xBPv6PZ0HmoNIgTGepf8U8eMN4rPbVjlweqcIY8EpkenSHg2DN9LBPTy6ouYWXaK1ZUZtogY1_p3ohG5Wfk6BfTQU7Jnkyo9n8UNVXjzmr6WtgYyvyq7oAJsj0OefHRo5_jKTq8zDLuVgIGzM2CEOdfMRUgcvPjbL0-bXHWu-ypo2sXcYlm5oIJM0O7Ic34eZCHe72abe4X8iOQsmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2038aea258.mp4?token=g7Hx1EcsPc_E6a63i0gDZQ3J_swYpWYDYqZNRVRo3B2P0TBXcNvIBia24lgaiS4ex2HPb9fWUh2GxivBvLTlHhJY0Q_OrPYgNY1DjV3k9BtLPkDHcxZ_gsN3s9KmvsgPB6o7xBPv6PZ0HmoNIgTGepf8U8eMN4rPbVjlweqcIY8EpkenSHg2DN9LBPTy6ouYWXaK1ZUZtogY1_p3ohG5Wfk6BfTQU7Jnkyo9n8UNVXjzmr6WtgYyvyq7oAJsj0OefHRo5_jKTq8zDLuVgIGzM2CEOdfMRUgcvPjbL0-bXHWu-ypo2sXcYlm5oIJM0O7Ic34eZCHe72abe4X8iOQsmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حجت‌الاسلام میرهاشم حسینی از جایگاه ویژه حضرت معصومه(س)
@Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/465248" target="_blank">📅 13:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465246">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">An_Open_Letter_to_the_Honorable_People_of_the_United_States_of_America.pdf</div>
  <div class="tg-doc-extra">367.7 KB</div>
</div>
<a href="https://t.me/farsna/465246" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامهٔ سپاه به مردم آمریکا منتشر شد
🔹
سپاه پاسداران در نامه‌ای به مردم آمریکا نوشت: حساب خودتان را از اشغالگران فلسطین که خواه-ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.
🔹
در این نامه…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/465246" target="_blank">📅 13:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465245">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXY4g3qpqVf-ddtG7wkF66WWw5l6pE0mpXhwKPWKfyZwxZK-fmLIgw2EGEnbKgKMZ5udh7C5NgX48jyraFwpSc2y6-sjg42SBHSAFfmo1OFlrgJD5oJoawKHmDZeGk-u0HNN59sKWGI2-z8qpKNGWO9eTN-LVS9-E_MI17jbcz6VT87L2RllPIFDPlJ9TScdofrgTSCdVwsE-IBaqu1EfHzRzYikVHwS0ZPzzkn9snpLLSV5dT3RnArioR45BAKqrX2b72bPZfMeLoDVJjQdD6BOQkEgwtLbQIajbY0k7pxmAxr6JmedqOughl8QFvC7uyf6CkW0gG7JkFWhj5M2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی سپاه: دشمنان حتما سناریوهای دیگری هم دارند
🔹
ما از آن سناریوها بی‌اطلاع نیستیم و خودمان را آماده کرده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/465245" target="_blank">📅 13:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465244">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sukuj3JNgCxEBXUwh8pW8L18-IwTdJKvVxMzwzV_Yqj3tdlWpPb-PlE63bYqu4xpXVhHBMxfyUJpean9xPO-XC-hWX4Ad0aT_wCSTGxagPV6rbaNJR6UD4RBDPlr01ZrC_AYf1isKwf9xZ6AUeCwCkD-d4KPRCtjgf6aqoxhy6WjiSg0iJnWhCFyyUzPcAKzwneRousSy3YLps8MHturEVzXHibJ4sgEcOczGB2eqxN1d6T2XMj_lBmYZOQ75EZX6m563xy8lQel6q7H6tWhGoAF1_rvU2Ugs7hWGWZzglyK8dOKR1sYQ7RUz4URuhMm22LsW5MAGyld8_9NmKGV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت توقیف بوئینگ ایرانی در استانبول مشخص شد
🔹
باحکم دادگاه ترکیه، یک فروند بوئینگ ۷۳۷ شرکت کاسپین به‌دلیل بدهی ۳ میلیون یورویی بابت خدمات فرودگاه استانبول توقیف شد و مسافران مجبور به ترک هواپیما شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/465244" target="_blank">📅 13:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465243">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5MDoKZISEYdxuM-d8_weBILOsJkR606lTGxDcQKnxxRWruiQlowpaRtDYye6RIxvl1V6cWNUt0u0n-KKGcnayzQb5CKmNsDNFpSVDGI6uHPKkmzDJelTV_iC68guJlENNMo_Ga2-9eA4OFg8Tkw5C9qhqdHDwsh-HGOceqIBVFbPip3Wf_5QdNa2R2pKbFULg6q22JlxmukFL3u-BiygGfKDA8McDuBgvp-_38NhlEdjQO6FJdcxyU_-2R1ei8dQmNCxu_af-Vl_N0a3lfzYFMoekOzk0hqmSvs8yuVt0kWzxJ5ozMsv73KkuhBD2QaxG66U95IHm8P0KxymFddyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۶۲ کیلو تریاک در اصفهان
🔹
جانشین فرمانده انتظامی اصفهان: درپی بازرسی از ۲ خودروی توقیف‌شده، ۱۶۲ کیلوگرم تریاک کشف و ۲ نفر دستگیر شدند.
عکس: مجتبی گرجی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/465243" target="_blank">📅 13:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465242">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5447a0d6.mp4?token=gY_8GJzQ4ysTUIe0lqU08i9nXiWeovhnZApjN-H9IXS07gtQ41K-_-40lNAiIaVTv8jQsRV7I-d8ntG7AqW3xphztTjxfTbKrX_8h14zPrUT_J6XbyAglqHdAYq2fFHA89brGQvz84BGaI7Ip0OILlszrzxXBK_7R3K-_LVfHOTNXIy4rvdXsyVILPh-P8qJmXzGI2MYrqNoo1IFiY3NBg-O45Mb4bPmYz7OgjClo-1Adn11HaQKmahkD5bQrI0KBQmSan6YzODZXg1mVhFo4xEH6aV-T-xm5RsgRcUncE7E39k6oiquMrtodZxSY03Or2w6N_qdnF_VDHOvMxd2TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5447a0d6.mp4?token=gY_8GJzQ4ysTUIe0lqU08i9nXiWeovhnZApjN-H9IXS07gtQ41K-_-40lNAiIaVTv8jQsRV7I-d8ntG7AqW3xphztTjxfTbKrX_8h14zPrUT_J6XbyAglqHdAYq2fFHA89brGQvz84BGaI7Ip0OILlszrzxXBK_7R3K-_LVfHOTNXIy4rvdXsyVILPh-P8qJmXzGI2MYrqNoo1IFiY3NBg-O45Mb4bPmYz7OgjClo-1Adn11HaQKmahkD5bQrI0KBQmSan6YzODZXg1mVhFo4xEH6aV-T-xm5RsgRcUncE7E39k6oiquMrtodZxSY03Or2w6N_qdnF_VDHOvMxd2TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان آتشین موشک استارشیپ در اقیانوس
🔹
استارشیپ، موشک شرکت اسپیس‌ایکس، در چهاردهمین پرواز آزمایشی خود برای نخستین‌بار از مرز مدار زمین عبور کرد و ۲۶ ماهواره «استارلینک وی۳» را در ارتفاع حدود ۲۶۹ کیلومتری زمین مستقر کرد.
🔹
این مأموریت با وجود خاموش‌شدن غیرمنتظرهٔ یکی از موتورهای استارشیپ در میانه پرواز، ادامه یافت و فضاپیما پس از انجام مانور ورود مجدد به جو، در اقیانوس آرام فرود آمد اما بلافاصله پس از برخورد با آب، در یک انفجار بزرگ آتشین منهدم شد.
🔹
اسپیس‌ایکس در مراحل بعدی قصد دارد فرود و بازگشت موشک را روی زمین در تگزاس آزمایش کند.
🔹
این موفقیت گام مهمی برای برنامه‌های اسپیس‌ایکس در زمینه ارسال انسان به ماه و در نهایت مریخ محسوب می‌شود؛ هرچند انفجار هنگام فرود نشان داد این سامانه هنوز تا پروازهای کاملا عملیاتی و استفاده مجدد فاصله دارد.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/465242" target="_blank">📅 13:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465241">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77a777410.mp4?token=LiBMEORkFOFKl-HC8vpArYTzctEhTAWhpdkzKYJi1rKQQm8t3DYh69RjYGwPvEqu7XHQ4CHmDFs6F_EAkAByTTBJqMavwANaMhs7USfT6PsARo4tMsvg95h9RMI76SlxKaLPDLWVdSuWMRni8ZET24Bo9x-N8SdeAgEiBCm50LRiUOVcDmaqm1gbFjIb5goSIbJjPeQgneQ8BqIJQt0i2JxwUNJxSCVs4vHOtSWAYhpDPDtiny2g8J8MZusUX_Ehn0pg2MT7w86iR-_b3cyW3SkLg6zUp5JMDFCppui5zzT0YAMFucM2oeAkZV3XAO64s3z4ahxv2fjbVPORiyf-lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77a777410.mp4?token=LiBMEORkFOFKl-HC8vpArYTzctEhTAWhpdkzKYJi1rKQQm8t3DYh69RjYGwPvEqu7XHQ4CHmDFs6F_EAkAByTTBJqMavwANaMhs7USfT6PsARo4tMsvg95h9RMI76SlxKaLPDLWVdSuWMRni8ZET24Bo9x-N8SdeAgEiBCm50LRiUOVcDmaqm1gbFjIb5goSIbJjPeQgneQ8BqIJQt0i2JxwUNJxSCVs4vHOtSWAYhpDPDtiny2g8J8MZusUX_Ehn0pg2MT7w86iR-_b3cyW3SkLg6zUp5JMDFCppui5zzT0YAMFucM2oeAkZV3XAO64s3z4ahxv2fjbVPORiyf-lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تبریز به میدان ۳۱۳ هزار جان‌فدای ایران تبدیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/465241" target="_blank">📅 13:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465240">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBKFCUZqRaDeN-oZkIJd7HrCVBgpO_oqFNm2L_VB9WU2wm0e1rDTjQIGoWf9d7VO21LQ-QLB5EEEjQx1q95kvXt6swp9cfMdZRWDnxH9A7gz3jV-NTDpVjCcbC8l1gFgoGv45dtbnnIvut1IOk5Zxh3vBcGLVXIjxe41bLlJSVpYrUVbRJdt1gdVFirisgItxDXOIaViEsy_afrjgLiDko1papyWRBKGx0gqkvriaUHSpnNa_LUIxHdJZljJAz6YxslW_e1w6xCUTg-6Nx4z1KJeAAxArT_B9dOfzwKBO4Wx4E6q7t4xhd9o0MAe9_wmhJrWjhZEC9Dh6XH_h99utA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب مجازی پای صادرات میوه رفت
🔹
دولت برای جلوگیری از خروج آب از کشور، برای صادرات محصولات آب‌بر عوارض تعیین کرده بود؛ اما وزارت جهاد کشاورزی در نامه‌ای اعلام کرده برخی از این محصولات مصرف آب زیادی ندارند و خواستار لغو عوارض صادراتی آن‌ها شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/465240" target="_blank">📅 13:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465239">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03c135011.mp4?token=eBu6uI12mmr-111PsMLZPXIUR04VDCHNYIGQt-V7EiCNxKa7NuJnI1t_uhr1xG1_XLy0LdwM9p7sfk5aECvTBFAzbYAP8GsjY4N5WRAz1VaX56dkaoMTEg8xONZeUtkuK1bTE0NhvBNenCb-4-EI2sfhvhgx31LnElD9UT6H9vejQHeHbavhrMusQeRgE5jQUehq20MfVeNQ4uImh-0AQYV-Z7EpHzQovD3gaNWCE6IwOMdfIVkhaaREm_kw-5k0f3-iJN_hr0KMj5ksqNq293NHUn9udqCPEMSlehCabWHhzLY-5iAXNvfgu9uILo6FAnI5unlzcr5WCezZQ6ZuwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03c135011.mp4?token=eBu6uI12mmr-111PsMLZPXIUR04VDCHNYIGQt-V7EiCNxKa7NuJnI1t_uhr1xG1_XLy0LdwM9p7sfk5aECvTBFAzbYAP8GsjY4N5WRAz1VaX56dkaoMTEg8xONZeUtkuK1bTE0NhvBNenCb-4-EI2sfhvhgx31LnElD9UT6H9vejQHeHbavhrMusQeRgE5jQUehq20MfVeNQ4uImh-0AQYV-Z7EpHzQovD3gaNWCE6IwOMdfIVkhaaREm_kw-5k0f3-iJN_hr0KMj5ksqNq293NHUn9udqCPEMSlehCabWHhzLY-5iAXNvfgu9uILo6FAnI5unlzcr5WCezZQ6ZuwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا
🏐
کامبک ایران امید اندونزی به صعود را ناامید کرد
تیم ملی والیبال ایران، ۳ بر ۲ اندونزی را شکست داد.
صعود ایران قطعی بود اما اندونزی برای گرفتن جای تایلند در رتبۀ دوم گروه و صعود، به امتیاز این رقابت نیاز داشت.
🇮🇷
۲۲ | ۲۱ | ۲۵ | ۲۵| ۱۷
🇮🇩
۲۵ | ۲۵ | ۲۱ | ۱۹ | ۱۵
@Sportfars</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/465239" target="_blank">📅 12:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465238">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49dcec5a0b.mp4?token=cY3clFTLb7_Bc-dyxxRdi4jfiQpVl0rb2yz3ynEcdQxr5E7ICMjb3YNKKcVn9R4CjYaXQpq-iG0ki6xtDPJA7fOn-H05QJPWaJr7Cvoy8GGYrCKluuje2YJFhGkooOoXqJOVyZsVV6UuJED1JL1SnwDABavi7LZEBs884gGgP7CReIkhXx9e1qdCxBJ2aVsoyrL7v6SIJJ2_tXOId3oIUb_-fXeLB8nD8wT0V-HtA2-axku3KH07IbShjfXhk8UMsJmvs7egwCJnbV6tIbKVXftu4FxcwiFv1EhA9OoGeQafA0LBV-lANflzBEErJxOTT9lBV4h3uniRRZuWAVuTuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49dcec5a0b.mp4?token=cY3clFTLb7_Bc-dyxxRdi4jfiQpVl0rb2yz3ynEcdQxr5E7ICMjb3YNKKcVn9R4CjYaXQpq-iG0ki6xtDPJA7fOn-H05QJPWaJr7Cvoy8GGYrCKluuje2YJFhGkooOoXqJOVyZsVV6UuJED1JL1SnwDABavi7LZEBs884gGgP7CReIkhXx9e1qdCxBJ2aVsoyrL7v6SIJJ2_tXOId3oIUb_-fXeLB8nD8wT0V-HtA2-axku3KH07IbShjfXhk8UMsJmvs7egwCJnbV6tIbKVXftu4FxcwiFv1EhA9OoGeQafA0LBV-lANflzBEErJxOTT9lBV4h3uniRRZuWAVuTuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین دارایی ما توی این سال‌ها چی بوده؟!
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/465238" target="_blank">📅 12:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465237">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXf4g9TC0mptilJhO_alNOqXwUcX7py2CfYZsQgwFADmbGuClT-hi0Kcfoie0DAiAoZzXvush_PJnibh4mUorYVCHZvuy_M_A5rlIvEhIIKAwcN9XswsmLtND-KCGzQ6q3dVt4EwBO07tjrrIJ26nsXS964CZ1Cy-J7WK4okZ9nsHBtm_q_kfFX0ReRFnjtOGNngwmqbCWOGOCwQZjKX45vtCGekhTFzo-1i4_BBmaEZa3uS5echAY8NoFSFz4LluFwZrpRCppHxYFL-Al53VUPCmbKQ5KsH3BBovePHZioEjJIXDJ4uCNRjO7DOV6okY3P_rttwUqdkcRQNS8S8UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به مرز ۷.۶ میلیون رسید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۶ هزار واحدی به ۷ میلیون و ۵۹۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/465237" target="_blank">📅 12:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465236">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c788b51378.mp4?token=GSnHVupzY6ln7EO6TXvAAuNN2ioK1LdAnSBj08xP-UmAKjgK1qrV2Jba95rD5bK6zv3Hoaaw_5KHYuDEKSlZYXY1QCFXkKCHlekoISBwRhR68nRf53W38Xms_0ire3IIlhuR9ZpVVdVf81TeBVbNQFnLfEj86ogSINkHLrs7XCsIH6fkYPNQ0NE2t8qjGV5oEk6G09x36f2p0KoRe_PsD0TqL1NLkiNSm_xhScAMDuuvTgMGzjzXncX0VI5f6NOUGi7b3Mdi3v-JknYceoI6IfZdFUCuHVcTwnJQTMl0qjRkgvcoYn0S1TXdbOiJIiJh7L9AYpZ4YXvZOdiGno3cuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c788b51378.mp4?token=GSnHVupzY6ln7EO6TXvAAuNN2ioK1LdAnSBj08xP-UmAKjgK1qrV2Jba95rD5bK6zv3Hoaaw_5KHYuDEKSlZYXY1QCFXkKCHlekoISBwRhR68nRf53W38Xms_0ire3IIlhuR9ZpVVdVf81TeBVbNQFnLfEj86ogSINkHLrs7XCsIH6fkYPNQ0NE2t8qjGV5oEk6G09x36f2p0KoRe_PsD0TqL1NLkiNSm_xhScAMDuuvTgMGzjzXncX0VI5f6NOUGi7b3Mdi3v-JknYceoI6IfZdFUCuHVcTwnJQTMl0qjRkgvcoYn0S1TXdbOiJIiJh7L9AYpZ4YXvZOdiGno3cuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای ساخت شهرهای موشکی به‌روایت مشاور فرمانده هوافضای سپاه
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/465236" target="_blank">📅 12:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465235">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a16f9106b.mp4?token=CMh11Fd-a9wxIHnisr9WKoojBbB1YCOgRmRxJwXUnIy60qeIOBX6lyCDW_S_JA6ILhp_9nynP2S8xRlbcvJadvsKhRYvhl6q1dhW6tp0V2CA-KGiPskMhk9TX1UpP7Ls6j5gaAinVff1fEEg7XS-hc08G3xkcQLMrqa7GJPXV12cohAh4CNIw2R-mcfA2JP51ElIpQ7Ef3be0VeOvOJgI7BuRYCz7_XttJXe4rY69_ESy1DYT8OYwMF-0HgYQ7Ifi4kjL3kKk1bITUHdgwkmBY9yUU2bdZIhitjF_dRpof-idU-FnS2vVt932L5Qx_7c7LP9gM6TlEg9Fg3U5JJKHkPcQbuDuFOEsNDYnZ7LD0eAX68_AYzLYEqnp0O5V39b5uNdzX9m-7c4HQIEUFwUcRuTkEx1DQoEpi-LM99eKlsY6vZqNiVV-1T4UYmgvzUKxonMpozJsfpRlbYPpOGS3hP4jHc9ryWYD_Cp0-kErHNL4ZAkeOhIIODAz9VlN6-5NK3F3WS3rPU6DXqC_mPZuxXAh8NlqawNNvYbg7kfq_wKYCIOR1eriCJpaO2R9peyOgeVDTwSdSZG4IAEMp2D2XXzbrR0C9rUpYN3a6pTOEl_0F8xFewse4mbKIg2DLVq7ijq-ALwR4HnUMEcITmj34JhAF-WFYB2H8vj-ptLmNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a16f9106b.mp4?token=CMh11Fd-a9wxIHnisr9WKoojBbB1YCOgRmRxJwXUnIy60qeIOBX6lyCDW_S_JA6ILhp_9nynP2S8xRlbcvJadvsKhRYvhl6q1dhW6tp0V2CA-KGiPskMhk9TX1UpP7Ls6j5gaAinVff1fEEg7XS-hc08G3xkcQLMrqa7GJPXV12cohAh4CNIw2R-mcfA2JP51ElIpQ7Ef3be0VeOvOJgI7BuRYCz7_XttJXe4rY69_ESy1DYT8OYwMF-0HgYQ7Ifi4kjL3kKk1bITUHdgwkmBY9yUU2bdZIhitjF_dRpof-idU-FnS2vVt932L5Qx_7c7LP9gM6TlEg9Fg3U5JJKHkPcQbuDuFOEsNDYnZ7LD0eAX68_AYzLYEqnp0O5V39b5uNdzX9m-7c4HQIEUFwUcRuTkEx1DQoEpi-LM99eKlsY6vZqNiVV-1T4UYmgvzUKxonMpozJsfpRlbYPpOGS3hP4jHc9ryWYD_Cp0-kErHNL4ZAkeOhIIODAz9VlN6-5NK3F3WS3rPU6DXqC_mPZuxXAh8NlqawNNvYbg7kfq_wKYCIOR1eriCJpaO2R9peyOgeVDTwSdSZG4IAEMp2D2XXzbrR0C9rUpYN3a6pTOEl_0F8xFewse4mbKIg2DLVq7ijq-ALwR4HnUMEcITmj34JhAF-WFYB2H8vj-ptLmNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موتورسواری روی پل عابر!
🔹
تصاویر منتشرشده در فضای مجازی، حرکت عجیب یک موتورسوار در مشهد و استفاده از پل عابر پیاده با موتورسیکلت را نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465235" target="_blank">📅 12:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465234">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a0a2ddb6.mp4?token=u96_oCFfyRgiE-7BA2mIw1yjKdbNW2tBIfprsvTpFJUsAKi--Trp7x_06Ol8WgUIfvgEzjFLCL0Zee42xo4AgvfdJjr-nqEI6JYqavjFPAQbHiMpGw-ZRx1a5ntIO9L_j11LfCFohFIElv9P3n5oDKStmmLQIzb16lgKcGaiw3a-WQf_HSRjAyLUg0nfTr8czsK_2MaUg0JJSMpJlUR_RFEFgVhWy26O5Cn3gP6n-pIIHzN9STOMiDa8GF_xJi47TVK7RuKMmnHRHSJ3Gtoj-6TRkpYb4vhgG2nEzZuge_SGWJoeVZVdfA8TwAzbW_-KWWIenvJtAlBuzA6_YY8nBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a0a2ddb6.mp4?token=u96_oCFfyRgiE-7BA2mIw1yjKdbNW2tBIfprsvTpFJUsAKi--Trp7x_06Ol8WgUIfvgEzjFLCL0Zee42xo4AgvfdJjr-nqEI6JYqavjFPAQbHiMpGw-ZRx1a5ntIO9L_j11LfCFohFIElv9P3n5oDKStmmLQIzb16lgKcGaiw3a-WQf_HSRjAyLUg0nfTr8czsK_2MaUg0JJSMpJlUR_RFEFgVhWy26O5Cn3gP6n-pIIHzN9STOMiDa8GF_xJi47TVK7RuKMmnHRHSJ3Gtoj-6TRkpYb4vhgG2nEzZuge_SGWJoeVZVdfA8TwAzbW_-KWWIenvJtAlBuzA6_YY8nBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانوی تبریزی در رزمایش جان‌فدایان: آمده‌ایم همانطور که رهبر شهید جانش را فدای وطن کرد، جانمان را فدای وطن کنیم و انتقام بگیریم.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/465234" target="_blank">📅 11:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465233">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f862792ca1.mp4?token=J64d_o-CwrofQnq6ZeSkLFwuE9ha28ZszAzc1b2m600gjeVKSbS6Fz1ZLZXFuMMsSZRcxrvFqcbVxrT7nK-5206Q_ELMppkhR2l5lDYlzh-zfkVzs4DdC6kkoX9LsMR4ZPeWZw-ybbxox_U8AqFReGv2cl3BQ3IKmmYJEdYgwZwOKqCuiNKXa0KCOVcr4TbgK72NOkzmqAHiSCjM6IPRTjNmTQJFgQEsbsYritDUz-wOpc3_uKkckznzBkKeIjtf-6XtztQQ7qh_OAnoqryAZMQPrigtKiheFlW33CN_bMkdqpC4JG3L3M3pl899TCRUElqbH-Rlb4Fxy0YqtFfUJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f862792ca1.mp4?token=J64d_o-CwrofQnq6ZeSkLFwuE9ha28ZszAzc1b2m600gjeVKSbS6Fz1ZLZXFuMMsSZRcxrvFqcbVxrT7nK-5206Q_ELMppkhR2l5lDYlzh-zfkVzs4DdC6kkoX9LsMR4ZPeWZw-ybbxox_U8AqFReGv2cl3BQ3IKmmYJEdYgwZwOKqCuiNKXa0KCOVcr4TbgK72NOkzmqAHiSCjM6IPRTjNmTQJFgQEsbsYritDUz-wOpc3_uKkckznzBkKeIjtf-6XtztQQ7qh_OAnoqryAZMQPrigtKiheFlW33CN_bMkdqpC4JG3L3M3pl899TCRUElqbH-Rlb4Fxy0YqtFfUJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانوی تبریزی در رزمایش جان‌فدایان: آمده‌ایم همانطور که رهبر شهید جانش را فدای وطن کرد، جانمان را فدای وطن کنیم و انتقام بگیریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/465233" target="_blank">📅 11:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465232">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c80cd563.mp4?token=JsKOpTq-aiWDtYy8vj3RW6S4333k9rpRptky5C7n1vSD2QiAw7fuIwSNsTjiVhBK1lPuFB3Y9rj-GyZaFOgOBycOo91gvgnvTZRElmDc2PggAHcXjFf-XQRmfs-f-QgJkHz2RTsO6dRMAxs2eg1S5_cmaZrtDiWc5EEao8vlx1RjEQ8JglIP7tgReC6WYvEnlTBrMNWRA9yzG7SxzWQEx_SegQdT5mWPLb1_OzF4_uByspTXmRIyJCjUkhmOiopF2oyba9GvqdhCC8g86onxQllRTkQTkSzc92ZIn_iavwquznTJvlcXIDDuiNi-gNJBHy06VOZcZnqRn0WntNwX7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c80cd563.mp4?token=JsKOpTq-aiWDtYy8vj3RW6S4333k9rpRptky5C7n1vSD2QiAw7fuIwSNsTjiVhBK1lPuFB3Y9rj-GyZaFOgOBycOo91gvgnvTZRElmDc2PggAHcXjFf-XQRmfs-f-QgJkHz2RTsO6dRMAxs2eg1S5_cmaZrtDiWc5EEao8vlx1RjEQ8JglIP7tgReC6WYvEnlTBrMNWRA9yzG7SxzWQEx_SegQdT5mWPLb1_OzF4_uByspTXmRIyJCjUkhmOiopF2oyba9GvqdhCC8g86onxQllRTkQTkSzc92ZIn_iavwquznTJvlcXIDDuiNi-gNJBHy06VOZcZnqRn0WntNwX7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظی با صف‌های ارزی؛ تجارتِ بی‌واسطه به جریان افتاد.
🔹
مصباح، فعال اقتصادی: پیش‌تر اجبارِ صادرکنندگان به فروش ارز با قیمتی پایین‌تر از بازار، منجر به شکل‌گیری
صف‌های طولانی تخصیص ارز
شده بود. از طرفی تجار نیز برای تامین ارز مورد نیاز خود لَنگ بانک مرکزی بوده و نمی‌توانستند با یکدیگر معامله کنند.
🔹
بانک مرکزی اخیرا
مسیرِ مستقیمِ معامله میان صادرکننده و واردکننده
را هموار نموده است؛ گامی حیاتی که در شرایط فعلی، سرعت چرخه تجارت را افزایش داده است.</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/465232" target="_blank">📅 11:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465231">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLxr9K52LnvfnTQpdaLAAb7ml8aOfowV-vnJTIDQgU-r5cwsNWqBZF1-IHYz-BBORXF4ZXObym5v9oWty_SwkdragH7QtmW0hgC_HhPVPpla0UoVefZrLbshZSG2YWoWP3YuCRMo43vcZSE6mmaQzOfJ4cWwBu2ZOUTHlFzCkfiLpR1SY7OTOLnuipDCM6HAE3t7GPxoQPsYwn0vgOKwgM58axdim6XbbsbCdphV9JWI2L03jGcqlwZcOsiIWr9w9RU1NUOPMtptcTQeD11YCyCPU43lOHC8I4AKmCtnOrN5aUJcFmLaKinJSAxk6jeALlRhTSL4EXHNZ4_nAZgU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
در شش ماهه نخست سال جاری بانک کشاورزی ۶۷ هزار میلیارد ریال تسهیلات قرض‌الحسنه ازدواج و فرزندآوری پرداخت کرد
🔻
بانک کشاورزی در شش ماهه نخست سال جاری، مبلغ ۶۷ هزار و ۳۸۱ میلیارد ریال تسهیلات قرض‌الحسنه ازدواج و فرزندآوری به متقاضیان واجد شرایط پرداخت کرد.
🔻
شعب این بانک در سراسر کشور با هدف تحکیم بنیان خانواده و حمایت از جوانی جمعیت، از ابتدای سال جاری تا پایان شهریورماه، در مجموع ۵۶ هزار و ۲۶۷ میلیارد ریال تسهیلات قرض‌الحسنه ازدواج و ۱۱ هزار و ۱۱۴ میلیارد ریال تسهیلات قرض‌الحسنه فرزندآوری به متقاضیان واجد شرایط پرداخت کرده‌اند.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/465231" target="_blank">📅 11:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465230">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/465230" target="_blank">📅 11:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465229">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a502f723d.mp4?token=dGgoU7lUr6Lk1MxRT8JPTzQtZ1an2rNP7xisN1NldUmlNRDHtcZ6BgU7AbCLpQ7Pe49WhF-mcmrMCLdLOYKLpFRRqLhMT5PUfu0e6BU1lAh1Fie34YOzZRwB_qeqak1ygwMZ6dbuh5S7u30sajqiMX4yf5gHohC4p4UDmzZ859WShm-R7CUkeEppk2CNFJ6EHrDJqxaLmzG9OYtJJwVbu3JMDoSaFgxxSh1-bEqlcgUTIs0wMtYbEWNm-SZCJQW4rGdgkF8IldyKytnOCy5BMH8e7FBUJQlWGZFGr_nW2aqjOP5GzcuP8azWCe0kBNIDYYsD38Q2bG7Vayi9676_IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a502f723d.mp4?token=dGgoU7lUr6Lk1MxRT8JPTzQtZ1an2rNP7xisN1NldUmlNRDHtcZ6BgU7AbCLpQ7Pe49WhF-mcmrMCLdLOYKLpFRRqLhMT5PUfu0e6BU1lAh1Fie34YOzZRwB_qeqak1ygwMZ6dbuh5S7u30sajqiMX4yf5gHohC4p4UDmzZ859WShm-R7CUkeEppk2CNFJ6EHrDJqxaLmzG9OYtJJwVbu3JMDoSaFgxxSh1-bEqlcgUTIs0wMtYbEWNm-SZCJQW4rGdgkF8IldyKytnOCy5BMH8e7FBUJQlWGZFGr_nW2aqjOP5GzcuP8azWCe0kBNIDYYsD38Q2bG7Vayi9676_IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۱۱۰ هزار جان‌فدا در بندرعباس  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/465229" target="_blank">📅 11:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465228">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1928c304e1.mp4?token=oy9E8RuHsn-f6mw6bi7V9EPc4rVLsXcRsIAT2R_wErtJ6TslqEh2QU9FhC97ywH9DIdKzdzBHw_3_0CTSJO8hwZAJd0jRTHWyUC7TVki2XZbnGd-ANFVo1cFeFh8inGgkSCKVmr93dVBiJCZLQiH48daS0N-2r8Zymor3cNE-bWUF9ShZscWnkY4frwKZf4KgVr218kLmWnQrIMDJnHksPDV0ZzmGDYwa-ow8vbmkPbXk4OXVV5qhg4mLS_ALp4ndn-6bhQmQypBQQ_eiOjdtp6LzRCFL4MsnzG8MTl1TVDpL6D6FduSdsc_C_29aCh7cQ8jC6GexuKBhKc1qitcgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1928c304e1.mp4?token=oy9E8RuHsn-f6mw6bi7V9EPc4rVLsXcRsIAT2R_wErtJ6TslqEh2QU9FhC97ywH9DIdKzdzBHw_3_0CTSJO8hwZAJd0jRTHWyUC7TVki2XZbnGd-ANFVo1cFeFh8inGgkSCKVmr93dVBiJCZLQiH48daS0N-2r8Zymor3cNE-bWUF9ShZscWnkY4frwKZf4KgVr218kLmWnQrIMDJnHksPDV0ZzmGDYwa-ow8vbmkPbXk4OXVV5qhg4mLS_ALp4ndn-6bhQmQypBQQ_eiOjdtp6LzRCFL4MsnzG8MTl1TVDpL6D6FduSdsc_C_29aCh7cQ8jC6GexuKBhKc1qitcgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رهبر انقلاب: در یک کلام؛ ایران به دورانی که دشمن آرزویش را دارد بازنخواهد گشت
🔹
این مقایسه بین روزهای سابق و روزهای حال باز هم قابل بسط و توضیح است، ولی در یک کلام، بنده به‌عنوان خادم مردم عزیز ایران اعلام می‌کنم که آن روزهای سابق که دشمن ما آرزوی بازگشت…</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/465228" target="_blank">📅 11:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465227">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7719ab050d.mp4?token=UrcIm_Fg_Q_tDNKWvBY1XcofXMaECjRdfe4O77NvQdIS3MYY7qDMIPWk9B4JTkEykme3j00W662DKNLq_1V2NcdrVu7GVomPX-6T-cT9P0yxmMtgdTsE2WkMxhxhKbj8MH1W59P7ZaRAAEJNR4xfQ0etfGdYhL-juDCwNuKC1OVb90ryx7hiQRv6fAR_t6lfPUz3MiyOWqIy0p0y-qkRZrlt_jBjFFbdxNH7NSnfHZUMANJ8ORCJhf25CzX0P3-5XaZEtwmmp23kWM_v_CvCp_IrAwx84RixglJtiZqecbHRCnC59Hn-rm3FLhutIW1zBr2XWxL9AqyPd3QpLCSpww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7719ab050d.mp4?token=UrcIm_Fg_Q_tDNKWvBY1XcofXMaECjRdfe4O77NvQdIS3MYY7qDMIPWk9B4JTkEykme3j00W662DKNLq_1V2NcdrVu7GVomPX-6T-cT9P0yxmMtgdTsE2WkMxhxhKbj8MH1W59P7ZaRAAEJNR4xfQ0etfGdYhL-juDCwNuKC1OVb90ryx7hiQRv6fAR_t6lfPUz3MiyOWqIy0p0y-qkRZrlt_jBjFFbdxNH7NSnfHZUMANJ8ORCJhf25CzX0P3-5XaZEtwmmp23kWM_v_CvCp_IrAwx84RixglJtiZqecbHRCnC59Hn-rm3FLhutIW1zBr2XWxL9AqyPd3QpLCSpww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: اگر درگیری‌ها شکل دیگری پیدا کند، ما هم سلاح‌های جدیدی را به میدان خواهیم آورد
🔹
برای دفاع از خودمان، همیشه در حال طراحی سلاح‌های جدید هستیم، سلاح‌های فعلی‌مان را ارتقا می‌دهیم و به تولید انبوه سلاح‌هایی که بتوانیم با آن‌ها از خودمان دفاع کنیم…</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/465227" target="_blank">📅 11:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465226">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dedcbeb03.mp4?token=RjJS7YfZ7W1T3Y3uM-5rNzk80kWrpgXXA0nDXEHTdosta6OdIGNAdzqf0Sw8bk-C5ektaad7cgYuslh8SHAlvUrMqUqDrAompxT8RicX-ga71bDqzW_bq0h3Gl2yXvDk63Oxatt9APKB5eznZfnuXlu7UJGWeG5aTR62DYloWIzXqgXQ_414_4R3jERDBS5Ne1oS1dPupUIM-2yPuBRgehOQmIciVEF46qvHAJ-Z5_4DO7uYo0dl1sPcnz4HHcI2pBUQObgb0tpZWGQs2Z8vmmWUkBwoRpKEgfnnN9dEs3ms_9aKp8OcOwDfj9tFnTfmZwZ8u9SgNkOO1Z2G2fYrAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dedcbeb03.mp4?token=RjJS7YfZ7W1T3Y3uM-5rNzk80kWrpgXXA0nDXEHTdosta6OdIGNAdzqf0Sw8bk-C5ektaad7cgYuslh8SHAlvUrMqUqDrAompxT8RicX-ga71bDqzW_bq0h3Gl2yXvDk63Oxatt9APKB5eznZfnuXlu7UJGWeG5aTR62DYloWIzXqgXQ_414_4R3jERDBS5Ne1oS1dPupUIM-2yPuBRgehOQmIciVEF46qvHAJ-Z5_4DO7uYo0dl1sPcnz4HHcI2pBUQObgb0tpZWGQs2Z8vmmWUkBwoRpKEgfnnN9dEs3ms_9aKp8OcOwDfj9tFnTfmZwZ8u9SgNkOO1Z2G2fYrAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار محبی: سپاه را تروریست اعلام کردند چون مانع غارتگری هیئت حاکمۀ آمریکاست
🔹
وقتی که می‌گوییم مرگبر آمریکا یعنی مرگ بر سیاست قتل و غارت و آدم‌کشی؛ مرگ بر افرادی که این افکار را دارند.
🔹
از مردم آمریکا می‌خواهم از حاکمانشان بپرسند که چرا سپاه را تروریست می‌دانند؟…</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/465226" target="_blank">📅 11:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465225">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a2e48fa4e.mp4?token=EUBNj-ipw3JlGrdfZ5VFcEXjtdhFwReR_2kaUauKL_9FerS6iZ3zQtM_cRhEpm8nHnBmxOpZY1-ESW0C08jKPt3Rjl76lhJw-Pp-wisDLGIvDyMPDNjt6vNGAPoPFAkrbhXFky3bmzeczz99ahYarTTYjHq45X27gkRXD8NgS62JNhwh2oRcLm7PKdVs0GEs-Uz8ciugUm1ou7NfiH0eRtZrNgAc4ADN-XWpW1Uu006scw9GfZj9xVznFuJp8LfDciXejIbhsUWuh4fnxyjCw4wWMiQzi1_Sh8aA5-2xLsQUjp-gEF4BRJpJidCBYWHdivQLtZVIJLeYfc_yabrmJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a2e48fa4e.mp4?token=EUBNj-ipw3JlGrdfZ5VFcEXjtdhFwReR_2kaUauKL_9FerS6iZ3zQtM_cRhEpm8nHnBmxOpZY1-ESW0C08jKPt3Rjl76lhJw-Pp-wisDLGIvDyMPDNjt6vNGAPoPFAkrbhXFky3bmzeczz99ahYarTTYjHq45X27gkRXD8NgS62JNhwh2oRcLm7PKdVs0GEs-Uz8ciugUm1ou7NfiH0eRtZrNgAc4ADN-XWpW1Uu006scw9GfZj9xVznFuJp8LfDciXejIbhsUWuh4fnxyjCw4wWMiQzi1_Sh8aA5-2xLsQUjp-gEF4BRJpJidCBYWHdivQLtZVIJLeYfc_yabrmJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منظور: امسال ۲۵۰۰ همت کسری بودجه پنهان داریم
🔹
رئیس سابق سازمان برنامه‌وبودجه: از حدود ۶۰۰۰ همت منابع پیش‌بینی‌شده در بودجۀ امسال، حداقل ۲۵۰۰ همت کسری وجود دارد و برآورد می‌شود ۳۵ تا ۴۰ درصد منابع بودجه محقق نشود.
🔹
برای بودجه حدود ۱۰۰۰ همت اوراق پیش‌بینی شده، در حالی که این رقم در بودجه ۱۴۰۳ حدود ۲۵۰ همت بوده و طی حدود دو سال حدود ۴ برابر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/465225" target="_blank">📅 10:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465224">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b604a918.mp4?token=BKJunaMVA1mICifgrvJ4I1T0ckfvSQHkXaNDPQ7gM-aR6d7j9U-bzTA0jpBLnMBs1EEzDMJnwPEIgpxoZHpk8tHgpfG42-TOILoJeFsYEZzMP0jeNw0v3tdTI4nLTriX9YI_dHdtXnRIhKbg3OO0QKtJCi8G3W2kQleqM4W1WStnk5WEbxUKuQLkAsMM6o5op-ALF-WFjOXbQGsoutNhof3s4h9uPZ-dpr_OMuthEPRN6NOsl6RerXffowuwCmHmKGSJke0G65APW_GufODRDqYzNHq1cNSSzFcA88T63pvrU9ekjIEr7w0riiiXTtiOb9nJ1v4XC3Mfah4vAwBGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b604a918.mp4?token=BKJunaMVA1mICifgrvJ4I1T0ckfvSQHkXaNDPQ7gM-aR6d7j9U-bzTA0jpBLnMBs1EEzDMJnwPEIgpxoZHpk8tHgpfG42-TOILoJeFsYEZzMP0jeNw0v3tdTI4nLTriX9YI_dHdtXnRIhKbg3OO0QKtJCi8G3W2kQleqM4W1WStnk5WEbxUKuQLkAsMM6o5op-ALF-WFjOXbQGsoutNhof3s4h9uPZ-dpr_OMuthEPRN6NOsl6RerXffowuwCmHmKGSJke0G65APW_GufODRDqYzNHq1cNSSzFcA88T63pvrU9ekjIEr7w0riiiXTtiOb9nJ1v4XC3Mfah4vAwBGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاکری: از امروز تا انتخابات آمریکا باید سطح تنش را بالا برد
🔹
مجید شاکری، اقتصاددان: تا زمان انتخابات میان دوره‌ای آمریکا یک گلدن تایم ۳۶ روزه باقی مانده است و جمهوری اسلامی باید سطح تنش را در این ۳۶ روز یا حفظ کند یا بالاتر ببرد.
🔹
تاکید می‌کنم که این افزایش…</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/465224" target="_blank">📅 10:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465223">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKDRqt2NyEKDJ29DMWV143qx6uBVPZ2CvJnsjtGl4KpeS15sgaxFQUGn9BT-HaCMXfHjyScR2ZqFp7Tq3EnXOKHtRMXFST7b-tBx7zwttHnQi1JV7I9cavCBnE1vhrJTYjxuSMHg1406nB6-XHOMjg7W7VoR1-LzqgzMfgZarwW4z2oHseykvhdn-BWCpL99dg_KHIQgXhk9zAptsu8FyHsJGMUu9DJT2DhENNDMD-z-XHZB0RSu_7gv7y79ayO7rcxtopAzS5C7hTl29R3WihnSpopI-OzuoAuVMEOPijc-hn_K4Y1rnbh6Q_23bSZI4JICP1sBPAaAfiAdpeKq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سخنگوی سپاه: در نامه به مردم آمریکا حقایق ژئوپولیتیکی را برای آنها روشن کردیم
🔹
ما از مردم آمریکا خواسته‌ایم که این نامه را حداقل یک بار مطالعه کنند. در صورت تمایل به پاسخ، انتقاد یا درخواست توضیحات بیشتر، آمادگی کامل برای مکاتبه داریم و آدرس رسمی جهت این…</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/465223" target="_blank">📅 10:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465222">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUsrq8NXP592SVcEhveKrRiBr2wiJOmCXTW1OnxHrdj9JFVEYByzNDUegmJeKXMOuhVxhS40kqXxM1ByXU-gzrsMT0VK8-CBuuk-jyUJZ3Uy1M46oSZpX1X9-B96hl_8ZR73qP1QJdp_QnYxNIodxGtUjjPrxYkhwaeh2li9nkUBUrZ70Q-FO8Mr1jgXSrp_F9_9dDc5d8JdARbLEujDdSPvLi532mvlrcb_hXMnX2nFS-M-7l04GAmq88rntF5jNpSV7zBEsLCZBXDTXFhSxh3yAF-znFYrjgi3fLXgcy5vZ9l7r8zvlWp3BAzNRm2Rf1Ufgus7_sY7BRhZJ4mHlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ طرح معیشت شهرداری تهران از امروز آغاز شد
🔹
شهرداری تهران قیمت ۱۲ کالای اساسی از جمله شکر، برنج، قند، روغن و شوینده را برای شهروندان تهران از امروز ثابت نگه می‌دارد و به‌گفتهٔ شهردار تهران، قیمت برخی از کالاها ارزان هم می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/465222" target="_blank">📅 10:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465221">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سخنگوی سپاه: نامۀ خیرخواهانه و دلسوزانه برای مردم آمریکا نوشتیم
🔹
هدف ما از ارسال نامه به مردم آمریکا، فراتر از تبلیغات رسانه‌ای و ایجاد آشنایی با منطق ایران است. این اقدام، یک حرکت تبلیغاتی و کوتاه‌مدت نیست.
🔹
بنیان تشکیل حکومت آمریکا بر مبنای دروغ است. با…</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/465221" target="_blank">📅 10:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465220">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MELWtObSV6_ykVVMvvduhqasZIlVaMxtKOgXKMhVCG4j1C4Do3ZjepUZrNSDD8Y98GXScWQ1r5VfbvP21rRZA2DvwiR5nad75I7UpQFQ2l_mmjt1NiERrgxpquS5L-OoN5JhT8lgQ3IWgzn2D-YYxC_6cYzfjJF_O9rdGc48mtRYJ6sfwAVxHyrcGsnLb9rqJe3fZL35oCxeouNd08vn8WRxCppjkFlLgC2c5SE8Lfh_pCBftU8EcP7rMj2PsLSxZyWY_7lYHUeUypNFgoV4BDBhcOnOPd8qcAev5BfDCF_hVxKbKaKJ0ZO94fEJYjepqcxdaLZOalzQjKBErwIdzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خبری سخنگوی سپاه با خبرنگاران خارجی دربارۀ نامۀ مهم سپاه خطاب به مردم آمریکا فردا در تهران برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/465220" target="_blank">📅 10:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465219">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0C4Scs-HiVe-Je9Z0vdIL586D-vCE_XDMY-AKy4890CKewjaBUVg_BG56vvrJWH_hdGLZwZzUrxeyWx3Piawz7EXkx0nLjbVVUc3rdbvYriEmZzbX-wJATdPL2T4-P7V9c1JJkqlxaoUhrkXxr7gVmuXwtp2U4nkSKD6IS7NDTvhtC1vEKVHo-1lUbhA-5PEBlj8AXL-i38wfgmqn5mdRLDq6HQ0Z3Yjyr_-Xm7ZcepagXd1NJ8hmeYxgGAMyHtLPxbPziDrMKE_OeMwIDvkFQpx1nCjKrSSpiKsg6wV9b31Hrt3dFKm00L9PEF-d5nHlfTkpnHuMW6Op9maG1VzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندگان از توضیحات خانم وزیر قانع شدند
🔹
در جلسۀ امروز صحن علنی، سوال عبدالجلال ایری در خصوص وضعیت مسکن از وزیر راه‌وشهرسازی مطرح شد که نمایندۀ دهلران قانع نشد و سؤال به رأی گذاشته شد؛ در نهایت نمایندگان از توضیحات فرزانه صادق قانع شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/465219" target="_blank">📅 10:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465218">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c31cedce.mp4?token=IYZpXFUliSKLqMzDAZ7QYcRO1hdV-yjPayelh-YTpDlt9yBVNkZNki2bCpQWZOPx62CX5jHCb1zbh6Bv4pmmEqVw8XKptf4wO1tgtKZZ8_ZVQNwpGPe9xuKeYssuiJVZu5YfetHkkuph1vPdadyat9gNZ4Wi0W8T56LmSqDCphLW-JKMIw3o4UrojXKPXDh6ZctXcgBsGI9K_O93tY0031wOrM0WV5RcsxvAPoytLBnvxlytNq0K3kVVIztG-iQkw0PawEd6FgFr872O_xlMcwWogOIWEerK6b86co42NGegPmBEfU_5ezSQec2_pvCB8CuP54nwtwlPhJb2DsgsNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c31cedce.mp4?token=IYZpXFUliSKLqMzDAZ7QYcRO1hdV-yjPayelh-YTpDlt9yBVNkZNki2bCpQWZOPx62CX5jHCb1zbh6Bv4pmmEqVw8XKptf4wO1tgtKZZ8_ZVQNwpGPe9xuKeYssuiJVZu5YfetHkkuph1vPdadyat9gNZ4Wi0W8T56LmSqDCphLW-JKMIw3o4UrojXKPXDh6ZctXcgBsGI9K_O93tY0031wOrM0WV5RcsxvAPoytLBnvxlytNq0K3kVVIztG-iQkw0PawEd6FgFr872O_xlMcwWogOIWEerK6b86co42NGegPmBEfU_5ezSQec2_pvCB8CuP54nwtwlPhJb2DsgsNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلای نهم برای کاروان ایران
در یک دقیقه ورق را برگرداند
🥇
مجیدوحید بریمانلو در دیدار نهایی وزن ۶۶- کیلوگرم با برتری یک بر صفر مقابل یاسین بوباکالونوف از تاجیکستان به مدال طلا دست یافت و نهمین مدال طلای کاروان ایران را کسب کرد.
@Sportfars</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/465218" target="_blank">📅 10:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465217">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cafd39d87.mp4?token=IlKKOYqfrU013QgGsZ5sj8MSlEzQhFsWoKK6CPW4aGytJTEjW9oquhQ94Rl8bwKaZ2S7GK4OJFnoApkhNUZiJ3Ra3POHyLBXBIVBbhvzM89G0xyiLCC_fSWebP3vIN3qN67vvOEk2iNYx5a6fA78BOEFw2PrYZJo9PTnKZDN1f68NyPSWfLWS2ACp5YgVM4MqUZe-obh55a3NThfLLpDnWMDx2BRXWGeJswHQb0zgOuyczeIOoko5aTwhfIvQIC9uQzKdYz3PpLDcDAhmTqVs8AVydxyv9_Ef3RyPfrBRiQG2zEGo60pyqCbXFIRJHeDtht1GbRRQVGJeu6Yo4aezQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cafd39d87.mp4?token=IlKKOYqfrU013QgGsZ5sj8MSlEzQhFsWoKK6CPW4aGytJTEjW9oquhQ94Rl8bwKaZ2S7GK4OJFnoApkhNUZiJ3Ra3POHyLBXBIVBbhvzM89G0xyiLCC_fSWebP3vIN3qN67vvOEk2iNYx5a6fA78BOEFw2PrYZJo9PTnKZDN1f68NyPSWfLWS2ACp5YgVM4MqUZe-obh55a3NThfLLpDnWMDx2BRXWGeJswHQb0zgOuyczeIOoko5aTwhfIvQIC9uQzKdYz3PpLDcDAhmTqVs8AVydxyv9_Ef3RyPfrBRiQG2zEGo60pyqCbXFIRJHeDtht1GbRRQVGJeu6Yo4aezQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مانتوهای کمیابِ بازار ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/465217" target="_blank">📅 10:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465215">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac07bd7731.mp4?token=kUK-ZsIV5jOaE1NJGWYGs2fx4lBSv945tOjnGfQWYYClq5_OfCJf8AgH2Zew2g3Rik6Z3sSxc9GGwifokqaxJvuuQnD-NLh5BsgU6nkotlSLZAgtKEj_7KQJSowxULatDyF276is1QSz6ptWXrz5KWIQliFavSL8ZjagZeQtEpxldl61btUEfza7JyaeeU7b2_yyxEUKwdP9ZLoC9pC_v9w5ZreYWrj5vMWTuAvZzK209gZHaUDDsYvmoVlVm9h17HPkuSBTJX0b08EFFyYgIRnBWKwJpK9T7DNbGju2KtaDViXmMnw2OeCNAPU4HlYqn1gOInqsZEHgSYqfmyIUFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac07bd7731.mp4?token=kUK-ZsIV5jOaE1NJGWYGs2fx4lBSv945tOjnGfQWYYClq5_OfCJf8AgH2Zew2g3Rik6Z3sSxc9GGwifokqaxJvuuQnD-NLh5BsgU6nkotlSLZAgtKEj_7KQJSowxULatDyF276is1QSz6ptWXrz5KWIQliFavSL8ZjagZeQtEpxldl61btUEfza7JyaeeU7b2_yyxEUKwdP9ZLoC9pC_v9w5ZreYWrj5vMWTuAvZzK209gZHaUDDsYvmoVlVm9h17HPkuSBTJX0b08EFFyYgIRnBWKwJpK9T7DNbGju2KtaDViXmMnw2OeCNAPU4HlYqn1gOInqsZEHgSYqfmyIUFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌مجلس: وظیفۀ ما مسئولان، حفاظت بی‌قیدوشرط از معیشت مردم است
🔹
ترمیم قدرت خرید کارگران، کارمندان، بازنشستگان و افزایش اعتبار کالابرگ یک اولویت فوری است.
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/465215" target="_blank">📅 10:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd555d2e1.mp4?token=j8Q7_L67Nm1iKmmODZSMHcQ68G_Btt8EyVQxoFlHwsCPhkxTZVaakeD9_EKaxvcOmQqFUGL6nckYrJtLfI_P3OkQtAjfbDzxS1kV4u1F2M3LysZDvgXSsYEEmpqWkyCO6RBxvkzEounnujrHf7WMmVL0wPna4KnGzrhduSYZre07feycmK9bg_Kwgl3thA3hVkG4UrCpnPadP-8L_b72a2-zabzuzS70-2q-m8aYaXHmhyk9pk6cEakUPnyjJHAugP0PJhxYnWa80tundeisau2AMFi9AW0OXr0FrFqTm3rkW2Qz0OSf26fBhv5ZfWp3yC0hJwtB_yJAkEkRSXesRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd555d2e1.mp4?token=j8Q7_L67Nm1iKmmODZSMHcQ68G_Btt8EyVQxoFlHwsCPhkxTZVaakeD9_EKaxvcOmQqFUGL6nckYrJtLfI_P3OkQtAjfbDzxS1kV4u1F2M3LysZDvgXSsYEEmpqWkyCO6RBxvkzEounnujrHf7WMmVL0wPna4KnGzrhduSYZre07feycmK9bg_Kwgl3thA3hVkG4UrCpnPadP-8L_b72a2-zabzuzS70-2q-m8aYaXHmhyk9pk6cEakUPnyjJHAugP0PJhxYnWa80tundeisau2AMFi9AW0OXr0FrFqTm3rkW2Qz0OSf26fBhv5ZfWp3yC0hJwtB_yJAkEkRSXesRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توهین دوبارۀ ترامپ به ایرانی‌ها
🔹
رئیس‌جمهور تروریست آمریکا با تکرار آرزوی خود برای پیروزی سریع در جنگ با ایران، مدعی شد که اگر تهران سلاح هسته‌ای داشت، به اسرائیل، و سپس شهرهای آمریکا حمله می‌کرد.
🔹
ترامپ در ادامۀ ادعاهای بی‌اساس و نخ‌نما‌شده‌اش گفت من جلوی…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/465214" target="_blank">📅 10:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e5f09fee.mp4?token=ZvVDgouTqVMStDbURQiXWfRiSiB8RY7vN89NzRio1s_w6y3p30q0ndPn3o8vSWTOA6qMzlYMptqZvhLvfKzMaATC7eCWR3qFialLZsjxtFJ3U3UnBYRFSjF2ZLA53vUDWZvHoY1i5-CQ5tZutuBOnxe6gNCbGZ9ZaO-e2EvcBqTVPozMqpaDzvqG5bQIK-L9FMzCVIEjqeR9aGrnkEf8nmpXXpUveCOBaiQexz7WYCoVEjtu7p-ywiBC7X7Bt4bMNO9Kofccb3uL6MWWy1reh1cnvbNQ1tYOe-l1FF1RbNRIid88sxBFuJcIhO5yrinzoCvG9LjkASPUSa_zFbvN7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e5f09fee.mp4?token=ZvVDgouTqVMStDbURQiXWfRiSiB8RY7vN89NzRio1s_w6y3p30q0ndPn3o8vSWTOA6qMzlYMptqZvhLvfKzMaATC7eCWR3qFialLZsjxtFJ3U3UnBYRFSjF2ZLA53vUDWZvHoY1i5-CQ5tZutuBOnxe6gNCbGZ9ZaO-e2EvcBqTVPozMqpaDzvqG5bQIK-L9FMzCVIEjqeR9aGrnkEf8nmpXXpUveCOBaiQexz7WYCoVEjtu7p-ywiBC7X7Bt4bMNO9Kofccb3uL6MWWy1reh1cnvbNQ1tYOe-l1FF1RbNRIid88sxBFuJcIhO5yrinzoCvG9LjkASPUSa_zFbvN7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رهبر انقلاب: در یک کلام؛ ایران به دورانی که دشمن آرزویش را دارد بازنخواهد گشت
🔹
این مقایسه بین روزهای سابق و روزهای حال باز هم قابل بسط و توضیح است، ولی در یک کلام، بنده به‌عنوان خادم مردم عزیز ایران اعلام می‌کنم که آن روزهای سابق که دشمن ما آرزوی بازگشت…</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/465213" target="_blank">📅 10:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efad563516.mp4?token=R9OtsXlLWiTdi_TEPoG9QJXiEoVcskUOPCizgRsq4lz5o8UiTIt1k2yGaXp3zNqq_Fnll33sXqBL18PLVCAqdcRpOCKbgmyfz9OMGrMZcTjYEKfbFxGcOM2CKhsGQNC613FvC-KLrd7nZJ0Cd37EbqdKDMJkMzroEU5KNiAPslB8VR9ZD5DoClpl9R8Tcz4iWEZQ8FzsXSaEmu97YllTU3w6OYUKnJo3VkIYCI8R3qbaKi24EXztrR6NHe8ENSttL_gcYIDZRzn-g16xdbE-JvvdFNaejtfJN_7_RUGXVsc_u5vDq52YqQnjZBEscni579dUofb6euse8t8ggpx59w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efad563516.mp4?token=R9OtsXlLWiTdi_TEPoG9QJXiEoVcskUOPCizgRsq4lz5o8UiTIt1k2yGaXp3zNqq_Fnll33sXqBL18PLVCAqdcRpOCKbgmyfz9OMGrMZcTjYEKfbFxGcOM2CKhsGQNC613FvC-KLrd7nZJ0Cd37EbqdKDMJkMzroEU5KNiAPslB8VR9ZD5DoClpl9R8Tcz4iWEZQ8FzsXSaEmu97YllTU3w6OYUKnJo3VkIYCI8R3qbaKi24EXztrR6NHe8ENSttL_gcYIDZRzn-g16xdbE-JvvdFNaejtfJN_7_RUGXVsc_u5vDq52YqQnjZBEscni579dUofb6euse8t8ggpx59w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: آمریکا بداند در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت
🔹
رئیس‌جمهور متوهم آمریکا به‌تازگی لفاظی‌هایی دربارۀ تنگۀ هرمز و عبور کشتی‌ها از این تنگه مطرح کرد که تکرار ادعاهای پیشین است و حقیقت این مواضع واهی برای همه شناخته شده است.
🔹
هم آمریکایی‌ها و هم سایر کشورها بدانند: همان‌گونه که قبلا گفته بودیم در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت و اگر امنیت ما تامین نشود، هیچ زیرساختی ایمن نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/465212" target="_blank">📅 09:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05caa8272e.mp4?token=FgxJMIBOxCJEbtzcrLVH_mM8lVm6kE-3dXCh3xPt9uxXZb70_IlsibA80AtUcBihoNdTTJBbo-larDt2FsMSiNWoloPCDAAFzcJevfyJBlCMV6f21UFw2PvWHdy8wbQIZhq550TRXjsK7wauYEqeIEODLcBI2Xj9GhcmEEfihnMN-jgvhu9YnnObU1vAXa2mUhyOTQzBwgpPd855FQSYuNvYngGCTNTVy5cAZb4OKfyVm-saPoOzTIhIL6rg4beP9FonSytBPFXj7C1lMsSsI1LVDM5USxdWwXIOE18zh7ygrzO7V4YB0baXrsg8deNydxr83FZFqo0Y7BBpbSEPgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05caa8272e.mp4?token=FgxJMIBOxCJEbtzcrLVH_mM8lVm6kE-3dXCh3xPt9uxXZb70_IlsibA80AtUcBihoNdTTJBbo-larDt2FsMSiNWoloPCDAAFzcJevfyJBlCMV6f21UFw2PvWHdy8wbQIZhq550TRXjsK7wauYEqeIEODLcBI2Xj9GhcmEEfihnMN-jgvhu9YnnObU1vAXa2mUhyOTQzBwgpPd855FQSYuNvYngGCTNTVy5cAZb4OKfyVm-saPoOzTIhIL6rg4beP9FonSytBPFXj7C1lMsSsI1LVDM5USxdWwXIOE18zh7ygrzO7V4YB0baXrsg8deNydxr83FZFqo0Y7BBpbSEPgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس‌مجلس از شکست حصر آبادان در ۴۸ ساعت
🔹
امروز نیز محاصرۀ دریایی و بستن کریدورهای هوایی با برنامه‌ریزی در حوزه‌های اقتصادی و پاسخ‌های نظامی شکست‌ خواهد خورد.
@Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/465211" target="_blank">📅 09:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8267e0c2dc.mp4?token=PYQJQPr_zqijurMrxirvhKGPIPiYeghjnMlcC7gLIhsYOw2aknsQUbnrWUiNuN6iBcDR3Z2kP2AxMuoMHRXzBxJWx4TVN9BDffJOkqLPXB8H2jR_U1NcMSuGJc4_Nfn6GfEDxNHCc6pKtT36fJhG_KWnyoJUA42stQbmqM_2i8h-9OB4EszpZJW_TJOcXqcU14gPld8t8GyNwJDD94SnYjmwp_dBKsCjWef2kKLBSiCS4_GRN-CIYs8zsfUVeN-FrgLnDoNOeLUbVtqRU7ol5nrGnoIFZ0erSoUhAcd_alkiPI1GFOJ1idRWPufNqWRPTC-pDMK0ZySrLtolgscfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8267e0c2dc.mp4?token=PYQJQPr_zqijurMrxirvhKGPIPiYeghjnMlcC7gLIhsYOw2aknsQUbnrWUiNuN6iBcDR3Z2kP2AxMuoMHRXzBxJWx4TVN9BDffJOkqLPXB8H2jR_U1NcMSuGJc4_Nfn6GfEDxNHCc6pKtT36fJhG_KWnyoJUA42stQbmqM_2i8h-9OB4EszpZJW_TJOcXqcU14gPld8t8GyNwJDD94SnYjmwp_dBKsCjWef2kKLBSiCS4_GRN-CIYs8zsfUVeN-FrgLnDoNOeLUbVtqRU7ol5nrGnoIFZ0erSoUhAcd_alkiPI1GFOJ1idRWPufNqWRPTC-pDMK0ZySrLtolgscfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: شهید نصرالله حزب‌الله را از یک گروه چریکی به یک نیروی بازدارنده تبدیل کرد
🔹
در دومین سالگرد شهادت شهید سیدحسن نصرالله هستیم. او نه فقط یک فرمانده نظامی یا فقیه دینی، بلکه یک استراتژیست بود که موازنه‌ی قدرت در منطقه را به نفع مستضعفان عالم و نهضت امام خمینی(ره) تغییر داد.
🔹
او حزب‌الله را از یک گروه چریکی به یک نیروی بازدارنده تبدیل کرد که معادلات امنیتی منطقه را باز تعریف نمود. امروز، ساختار مقاومت، با همان انضباط و نگاه راهبردی، تحت هدایت جناب شیخ نعیم قاسم، مسیر خود را سرزنده و با قدرت  ادامه می‌دهد.
🔹
دشمن تصور می‌کرد با حذف فرماندهان، میتواند مقاومت را در لبنان متوقف کند، اما تجربه و نیز تحولات ۲ سال گذشته نشان داد که مقاومت، متکی به فرد نیست؛ بلکه یک ساختار شکل گرفته است که دشمن را در هر سناریویی به بن‌بست کشانده و مستاصل کرده است.
🔹
دشمنان و همۀ مردم دنیا دیدند که خون پاک فرماندهان شهید مقاومت، این جریان را زنده تر و قدرتمند تر نموده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/465210" target="_blank">📅 09:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c55d0d2b94.mp4?token=ae_tYB6XOEuRuYJoHjGVH06d9YUh9o_nk649lXEoohNeGBckluRqyWP9uMw78Jd22kGZQhR21dKrIl5mCNBd8ucz3RIGPx3kS-ZjP31WxICx7thvcGjTyTqyB1edNuULgnUA3pLDNFKtDIwh12V827UbFpjQT8-GP9K6lUB9Yg5KAGsv2vfFN649DoO8t-IT5TLOhk2u939I4CaoY27o2NYrF4OwH7krRyHZt2tjDjfitEfpp4imZrg8Telhc_nuP5Yn6who96rsstpo1s42_FNXgInfkPm8yu3MlrlVtm8LGb2Gef2KH109sId5gGfbb4yC50WkMWQBHg1PupYYOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c55d0d2b94.mp4?token=ae_tYB6XOEuRuYJoHjGVH06d9YUh9o_nk649lXEoohNeGBckluRqyWP9uMw78Jd22kGZQhR21dKrIl5mCNBd8ucz3RIGPx3kS-ZjP31WxICx7thvcGjTyTqyB1edNuULgnUA3pLDNFKtDIwh12V827UbFpjQT8-GP9K6lUB9Yg5KAGsv2vfFN649DoO8t-IT5TLOhk2u939I4CaoY27o2NYrF4OwH7krRyHZt2tjDjfitEfpp4imZrg8Telhc_nuP5Yn6who96rsstpo1s42_FNXgInfkPm8yu3MlrlVtm8LGb2Gef2KH109sId5gGfbb4yC50WkMWQBHg1PupYYOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدردانی رئیس‌مجلس از سربازان جان‌برکف وطن و آتش‌نشانان فداکار که در خط مقدم صیانت از جان و مال مردم ایستاده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/465209" target="_blank">📅 09:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجار کشتی در تنگه هرمز
🔹
شرکت امنیت دریایی «امبری» اعلام کرد یک کشتی تجاری هنگام عبور از مسیر جنوبی تنگهٔ هرمز، در شمال «خصب» عمان هدف اصابت قرار گرفته و دچار آتش‌سوزی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/465208" target="_blank">📅 09:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🔴
خبرگزاری رسمی عراق: هواپیمایی عراق پروازهای خود بین نجف و فرودگاه‌های ایران را از سر خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465207" target="_blank">📅 09:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lymesHLDQ06Yu5pwxw8kMYZGlIXa197PnOqQiHnvpWm_pX4zKcnSdFw-U__SdH8hptPwTKa53fZNMI0Yae-m3q0wpe0Hvi0jdXEPToz2ESqgYAXhQ3q28eUqXF_IaPEdtcJISEpIaE-I7K9oWEb9krrdKCmzlMysZSchoLu1l1BrYzj4BZTbrolOgUQ0veTT-rQoUyzYsb7_M7GpfaH8vhGZpZQ8kl-DJqgTwCtZVX07Z6NNxIOVNAzG-Or4y97dUV9w8NKfhGggW6CeCZ3oKfjDRf4ZnCaiJ5jpif8XPMDbt5Dtxc_CtZ1LnE3G0KfFZeOxzqKvhRWEzbCOmKo8Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای ناو هواپیمابر آمریکا و جراحت ۴ نظامی
🔹
نیروی دریایی آمریکا اعلام کرد ۴ خدمهٔ ناو هواپیمابر «دوایت آیزنهاور» در پی وقوع «یک حادثه در جریان عملیات تعمیر» در نزدیکی سواحل ویرجینیا زخمی شدند.
🔹
مقامات آمریکایی می‌گویند که «این اتفاق حوالی ساعت ۱۸:۱۸ دوشنبه به‌وقت محلی رخ داد و در جریان آن، ۲ خلبان از هواپیمای خود به بیرون پرتاب(اجکت) شدند».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/465206" target="_blank">📅 09:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465205">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">۲۷ پاساژ بحرانی تهران در آستانۀ پلمب
🔹
سازمان آتش‌نشانی تهران: بیش از ۹۰ هزار ساختمان ناایمن در تهران شناسایی شده که ۴۷ ساختمان در شرایط بحرانی قرار دارد.
🔹
۲۷ پاساژ بحرانی (خلیج فارس، ساختمان پیروزی، بازارچه سنتی ستارخان، خلیج فارس ۲، مهستان و سرای حاج ولی) روزانه هزاران نفر در آن تردد می‌کنند و ممکن است در کسری از ثانیه بریزند.
🔹
دادستانی اعلام کرده ساختمان‌ها را معرفی کنید کارهای پلمب را انجام می‌دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/465205" target="_blank">📅 09:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465204">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4f04ea36e.mp4?token=MfbJ0S2VD71TbA_q7exD07Cg__Jc7Y8wmdHOnisXgZewOsQC1DcTl5VgpO2ujglvIC-lO3dUatUOWv528KGmOTZJhLTyHVJDiDO3dqRL42mLgWrsd2Ehmhx7Qm43W6fiAorge7aq1b-ZJe0yZ3C0EA17QnWpYKWX6DmOUunDEI3SMeUvRrCBQ2DIeN2H2dKgz5d9JL6J0sF1CZpNMC_DTSACH34605fjHGXfMGvSzmDn0VggrckuWdQ0RpEHGiuA07P1Mt_6lQ6UhJUVBo55V7V4eyWEvBjhRg27zXWAqWz_UdT4Pug65VvgpPDSuvWykqjo1fqM0n5-sXB0Zej-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4f04ea36e.mp4?token=MfbJ0S2VD71TbA_q7exD07Cg__Jc7Y8wmdHOnisXgZewOsQC1DcTl5VgpO2ujglvIC-lO3dUatUOWv528KGmOTZJhLTyHVJDiDO3dqRL42mLgWrsd2Ehmhx7Qm43W6fiAorge7aq1b-ZJe0yZ3C0EA17QnWpYKWX6DmOUunDEI3SMeUvRrCBQ2DIeN2H2dKgz5d9JL6J0sF1CZpNMC_DTSACH34605fjHGXfMGvSzmDn0VggrckuWdQ0RpEHGiuA07P1Mt_6lQ6UhJUVBo55V7V4eyWEvBjhRg27zXWAqWz_UdT4Pug65VvgpPDSuvWykqjo1fqM0n5-sXB0Zej-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فاطمه برمکی به برنز کوراش بازی‌های آسیایی بسنده کرد
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465204" target="_blank">📅 08:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465203">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc16f82aaa.mp4?token=r6DgfvQWezcRT7LuDnEERwMDcb_N1i1-ya7QtSNYksnBSan9URHwIvLEN-FYAHrplbSe8_-2u6jfxr7DAO6B7nKRl9FAS8mGfylxqWjDugfrMEaHkTOXAWzUjFxgRrLCAzDC3dpuILCOZex0RMyQ1tcCB5_llfckb9VAJf-8gAET44ISNDW-vEB0pxooq-yOr20KR8jUwSzU-mEQkhZZVhD8fuMK9yHBYLeEJriImRsbp5vIRZltWgEWGyCfOHPbsrHcqPUbieqNL30_t6yvEKg2vtyInU5Ofb5lUapjccCGtpOjBUuKyJO7yZ4gUW84HCokcC6BOCnM7OuvpxRGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc16f82aaa.mp4?token=r6DgfvQWezcRT7LuDnEERwMDcb_N1i1-ya7QtSNYksnBSan9URHwIvLEN-FYAHrplbSe8_-2u6jfxr7DAO6B7nKRl9FAS8mGfylxqWjDugfrMEaHkTOXAWzUjFxgRrLCAzDC3dpuILCOZex0RMyQ1tcCB5_llfckb9VAJf-8gAET44ISNDW-vEB0pxooq-yOr20KR8jUwSzU-mEQkhZZVhD8fuMK9yHBYLeEJriImRsbp5vIRZltWgEWGyCfOHPbsrHcqPUbieqNL30_t6yvEKg2vtyInU5Ofb5lUapjccCGtpOjBUuKyJO7yZ4gUW84HCokcC6BOCnM7OuvpxRGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار نارنجی سیلاب برای شمال کشور
🔹
هواشناسی: روزهای پربارشی در برخی استان‌ها پیش‌رو داریم.
🔹
هشدار سطح نارنجی هواشناسی به‌سبب شدت بارش‌ها برای گیلان، مازندران، گلستان، آذربایجان‌شرقی، غربی و اردبیل صادر شده.
🔹
برای روزهای پایانی هفته، سامانۀ بارش‌زایی از غرب وارد کشور می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465203" target="_blank">📅 08:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465202">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ce5b3c4c.mp4?token=HId_RtM1UUQQummnWXZtJiBOuRO6uLvNqjkLpOZ96wUA3SynIiJE2LQ0u-Imx7zDy0MN-wWpDwLFwuFDAH2GvgbU1PvEpXQjXWj58Tu-DWZFDeVZIB3DzEQHPiiwYKyETash6UgvzmAjSlGCOkZjXxRH4NSWC3aDr9-jG_5K1BfT2JkyDWVhwZbI6crPm6FBXl7ogmS5K9os_qdE1BVYHZ2fyyq1JYCwbBnbapWldGMry93dsWnvKAPsvTJafAGHKPvPIhp6X8iH_vXVU9zeHtATQgrqaYfTtAcmu4HETdjwO90odxwoyNCRAPEP1Ysh-Y1XSiPKgaQy9rm8S6Zv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ce5b3c4c.mp4?token=HId_RtM1UUQQummnWXZtJiBOuRO6uLvNqjkLpOZ96wUA3SynIiJE2LQ0u-Imx7zDy0MN-wWpDwLFwuFDAH2GvgbU1PvEpXQjXWj58Tu-DWZFDeVZIB3DzEQHPiiwYKyETash6UgvzmAjSlGCOkZjXxRH4NSWC3aDr9-jG_5K1BfT2JkyDWVhwZbI6crPm6FBXl7ogmS5K9os_qdE1BVYHZ2fyyq1JYCwbBnbapWldGMry93dsWnvKAPsvTJafAGHKPvPIhp6X8iH_vXVU9zeHtATQgrqaYfTtAcmu4HETdjwO90odxwoyNCRAPEP1Ysh-Y1XSiPKgaQy9rm8S6Zv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از لحظات کشف پیکر شهید سید حسن نصرالله
🔹
مستند «آن شب» برای نخستین‌بار روایت افرادی را بازگو می‌کند که در جریان جست‌وجو و پیدا کردن پیکر سیدحسن نصرالله حضور داشته‌اند.
📺
مستند کامل را در تلویزیون ببینید:
🔸
امروز ساعت۱۲:۳۰، شبکۀ چهار
🔹
فردا چهارشنبه ساعت ۲۱، شبکۀ مستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/465202" target="_blank">📅 08:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465195">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KisOxsuMJGQ05OkAMD2HysPnnkxkt2X9Is_9T2EUA6hhfxxMmCfifrhTzmmjBsN0rq6Yp5TWaKZDmyW9FtYB9swuBV61rZC1rKCmwQLY0w6bu287zkUwFZ4vcPdVqWwRtg1Plq3or7nd33x7Cw73c7eoScxw3L-QX3bctC8E_ZJdf4ErHr2HQ5FsQKgHyR_eewhfnX4HOhdZ6HZaWHiu2717CFusfHaiQ3B57chQuhPxr50MTZzpj2dZpslQoZ4Eeq_vkuY1HtlUP0hkEI68Xfv9YBjk9tBkGmjXZJ0eNrsyLiuoMP1cYN0Eyl8YeOY3KNgzMIrRXyNC2oNtw0QSjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTKjHrns2aUVP1h0I1eQntQd9iRAo6Abkn6lE2U9G8WUKRi3oyXKPXpUV5FFZ0DuVPZQEZekiTIK2xQPSpd9ifh7TysNi6IfzyLJvzpZETbpZhZrLjydr1Vd6RWGQbMG3t2rNNM8M7ufpOtF8LYgA9KEp_oSSjJmLw3EFur6Jkw2KhInzGR_C9fu6w6ZZZJfEiqgvwoDzA51rJ7TGQuGjwrW1oXvw8htTIH5oV5qqBdKZuYhPxnURh0Bq0-NYzZtD4-7ZzXv5ueaaZlvaikwC_2BuTFR8jehtywz4r6C5MJ_j-Im8RCsi7TCFP9lrpo0h_H8HAxYTwdD69Itaig9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OR9g04gZh4kAF_SR81CbP2O3ENngZkXYAdjWDq1hE9qN64jOU-s_V3hFkHzPsM6XTRToFzTPYZuidQZBMOnEnWf9u1ajqs1ZZn5boKm-VkqnyVz2p134AlWzouRa1cJMdGgbmXguzQPRQVaevTrzor6k6DAP8gfCVauCSzhvach9Vg7ekySwO0iDl7M5AIc2raas5llfp2jvb5GVz2XPeqvpyR_5bHN6cBwm6m6LFhRP8NfG57oADW6WFTyd4OH4DH3aK48IRE5Goe3ikC4mse_K0YitqoDaHb4Z-yYgpv79gEu-0cK9cYdjIqrU6pCB8T2X51gssSVBFJPtbGa2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUDOAQBGM9LHWY-oRKtfauLjlFSao8jw9rqllcoPWUq80UXK5jjMw5aaLxB-UWF4cvClWME2fIBUEwsOEkO-6g5lUvIGO_max2WLX7aPi-4BDTKScnEQy9V6y6QDwzqbpE0EjMpOS1CH00CxSdtJ-TgUIaBeEdvGYNSt6agI33PI_crzAQBb9qjn9HOfcBJg2ujzwzp3TCd3KwDG3wadB-48St_dvPIQLz6vKjXh-m4QowCeXVWYFnZzj32d60eYvuh9DR2b28IyzTnoMfNa5dwxOpEtANqU_i93L4EQZZgchBnothM1ExMSqYgf5vdgg3nalve9biTlmf-kwIRH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZLgieKRIQc8DGQEmNRUgsS9maghGrRlNSuPrsmX0OzezyyJxfZMw1FKX_6djZc6eEAEOlXi_TYfvWClVgGkh1pPJBZSAmfKj7zjm10hihJGfp9N5wEyFIEkg6u_l2k86hij5njIUPOLCanJdnabA9Jr9WayjSpvNd5JQeWH2YVhx309XQ5qQ3gw7qt-Qedlm1OvemMxePW5Uwj0gFeUqpAJKB1kR5wn4EaZr18WD4Eh2Twgu9gW9oLfEhIeFhJ9VObnibqwYaJXgRT_ZHHnEKBtNeNWcO_QIRNDVniWvbegdEmXD5-pO8Q2rNVAeiVLnPhVp6epWts0uaki-sIbvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4OxCdndpLnXlRZ2clfVanaI_PJccF0ZRe_dt_BDAtskZSJlHwjeTumTIDmu9z6gkHUo1QrmJzOTxVK1FZ1GP98RCaW_RWf-D_z8uUMye5644aHwqQfzrj9OTrksm3Osw2ZJjn60XZskB1-7uoXXM_M9Jl9HbImfCDSaY1Om3G4g1_f3pqY6NrwpkdEC7zf0qbL4PqOvhKYoiHOGtuAQ0MgK1mV7jmlKQRyj7OremjkzdL4QJfgHqAxPQWwqNYXdPzIGdCXr9LaXI9aOq_N2rPaMCNjsaS5zK7QfQY4Dnm3BeVP-hyYfbL9XpvXyU1HBUAYXiU_shA3adoogW67vbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQQzr3Fw4cU8jgZ6cnQvoyWUNYKTCAs7olfoPgfWhHJNAEZZ34pQ6wrnywTDjM59h8PWHfClQYqkaM3KY2m51oRR4Lb2lLt5lZyzTg-rcryBTT-JfzMxRiEx1y9nq0Y4MpBCfMqfQQw2X3WdKW9MCu5Rm49fBBITsRQXTB4rpIstK3wsJXaz_-QYx1IadUh4vKuLEc0iwfCnEMnPJ1N521hK8CjV9c9aXT6gUVsOdmBRxBTfZ6cBIHrbYCLt-xDKhip0ov_ygcuBFgkjrPq0wINsxR844-N5dmR9GN8KPuW7acNN0VLI6vUNraNk6-Lc1SvXnuiFh-EnR5thvZ-oYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خراطی میراثی زنده در دزفول
عکس :
علی صاحب‌محمدی‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/465195" target="_blank">📅 08:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465194">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39f2d07eb0.mp4?token=QE8JjT4I6CondTwuv3uoXfRoqMtkAFdI8qkK1-rq2ArjjqiEFqcQltI3NvdKTG59FoGiEWxNztaL5LJB9xcC6Ye1-nlrMIGl-_P5F0UlbCEu9VBzK9rQzdcBjk_X4b903TCmBZmFc4DnQ6ykIjQ7zDxqNDMbaviWZmejqs6HU_sYqOhesQkH2hEPuPSHHgdtWg5YJIIdyZ8GeTwsX67ZlUGXXPVUTNRgc3vkyrW9OM-1OdWWf7aF9QOnZQ2baIv2CTjdpa946uLpuJemCvxgldhHW-1ZRWOgfmXKhozOSBJndFEd5ayWHCniMrWkLwBmLhITcLESb_1YsZWx9R2JdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39f2d07eb0.mp4?token=QE8JjT4I6CondTwuv3uoXfRoqMtkAFdI8qkK1-rq2ArjjqiEFqcQltI3NvdKTG59FoGiEWxNztaL5LJB9xcC6Ye1-nlrMIGl-_P5F0UlbCEu9VBzK9rQzdcBjk_X4b903TCmBZmFc4DnQ6ykIjQ7zDxqNDMbaviWZmejqs6HU_sYqOhesQkH2hEPuPSHHgdtWg5YJIIdyZ8GeTwsX67ZlUGXXPVUTNRgc3vkyrW9OM-1OdWWf7aF9QOnZQ2baIv2CTjdpa946uLpuJemCvxgldhHW-1ZRWOgfmXKhozOSBJndFEd5ayWHCniMrWkLwBmLhITcLESb_1YsZWx9R2JdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عینک بزنیم یا نه؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/465194" target="_blank">📅 08:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465193">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پاداش جداگانۀ فدراسیون وزنه‌برداری برای مدال‌آوران ناگویا
🔹
فدراسیون وزنه‌برداری پاداش‌های جداگانه‌ای برای مدال‌آورانش در بازی‌های آسیایی درنظر گرفته است. این پاداش، غیر از پاداش‌هایی است که از طرف وزارت ورزش و کمیتۀ ملی المپیک برای ملی‌پوشان پرداخت می‌شود.
🔸
برای مدال طلا: ۳ میلیارد تومان
🔹
برای مدال نقره: ۱.۵ میلیارد تومان
🔸
برای مدال برنز: ۱ میلیارد تومان
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/465193" target="_blank">📅 08:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465192">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دستگیری سرشبکۀ معاملات کاغذی
🔹
سخنگوی پلیس: سرشبکۀ سابقه‌دار در معاملات فردایی و کاغذی، به‌همراه ۱۰ نفر از مرتبطین دستگیر و ۵ فقره از حساب‌های بانکی اجاره‌ای نیز مسدود گردید.
🔹
بررسی‌های به‌عمل آمده، از گردش مالی ۲۴۰ همتی مجرم رديف اول حکایت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465192" target="_blank">📅 07:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465191">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هوای تهران «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۹، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/465191" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465190">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsNkwunlyPEBBJRrrRDbAXxEi3mLexgdSyFvAzndbYLMu8a6rSabpQ_nsYrPwEXGIaQ-RsD_sA-mn4iF8XLbC9hhe4Wg6yxnqZlHevkTbSyTRs4d5SC6KWvXfX4BRCoRjzx-sY7aqRIDU72RdonZHFjm8mwDI_SsYcMbX175BJp1cVEwpAnazkviNPdgl8BbtTg78txa5woUPBUPDKOycOZiI8F6so1sf9hK1VBlITLRJSK_qtnFIIZsh2OaRWSzPygXI7JbllN_f_2_i7IsZMiKIxON3srfMBj0c7fNfbDw3ReDKYSaftiYdKOFcc6mmm2r86dMqoXjaYxDLWAcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال سرانجام به جام لیگ قبلی می‌رسد؟
⚽️
قرار است فدراسیون فوتبال با رای‌گیری بین اعضای هیئت‌رئیسه، تکلیف درخواست استقلال برای دریافت جام لیگ بیست‌وپنجم را مشخص کند.
⚽️
پیش‌بینی از آرای هر کدام از اعضای هیئت‌رئیسه باتوجه به سوابق آن‌ها نشان می‌دهد احتمالا…</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/465190" target="_blank">📅 07:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465189">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نمایندۀ ایران در تراپ زنان، از فینال جا ماند
🔹
مرضیه پرورش‌نیا در بخش انفرادی تراپ زنان با کسب ۱۰۸ امتیاز در جایگاه سیزدهم قرار گرفت و تنها با ۲ امتیاز اختلاف از فینال باز ماند.
🔹
فردا او و محمد بیرانوند در تراپ میکس رقابت می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/465189" target="_blank">📅 07:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465188">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">صعود دختران پدل‌ ایران به مرحلۀ یک‌ شانزدهم با شکست قطر
🔹
تیم دونفرۀ پدل بانوان ایران با ترکیب صحابه فرد و زهرا کهریزی، با پیروزی مقابل قطر در جریان بازی‌های آسیایی ناگویا ژاپن ۲۰۲۶، جواز حضور در مرحلۀ یک‌شانزدهم نهایی را کسب کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/465188" target="_blank">📅 07:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465187">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌ عراقچی: مأموریت ما این بود که شروط خود را به اطلاع طرف آمریکایی و جامعۀ بین‌المللی برسانیم
🔹
شروطی از سمت مقام معظم رهبری وجود دارد و این شروط باید اجرا شود تا تنگۀ هرمز باز شود و مأموریت ما این بود که این شروط را هم به اطلاع طرف آمریکایی برسانیم و هم به…</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/465187" target="_blank">📅 07:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465186">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌ ‌عراقچی: مواضع ایران هیچ تغییری نکرده است
🔹
از چندین ساعت قبل ادعاهایی مطرح شده که با قاطعیت عرض می‌کنم که هیچ تغییری در مواضع ایران رخ نداده است.
🔹
شروط ما برای بازگشایی تنگه مشخص است. در خصوص سایر مسائل نیز موضع ما مشخص است.
🔹
درحال حاضر فقط موضوع تنگۀ…</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/465186" target="_blank">📅 07:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465185">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎥
مصاحبۀ عراقچی در پایان سفر به نیویورک
🔸
تلاش کردیم صدای حقانیت و مظلومیت مردم ایران به گوش جهانیان برسد، از منافع مردم ایران دفاع شود و نشان داده شود که ایران همچنان قدرتمند و با اعتمادبه‌نفس در عرصۀ بین‌المللی حضور دارد.
🔸
در ملاقات‌های انجام شده مشهود…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/465185" target="_blank">📅 07:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465184">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
مصاحبۀ عراقچی در پایان سفر به نیویورک
🔸
تلاش کردیم صدای حقانیت و مظلومیت مردم ایران به گوش جهانیان برسد، از منافع مردم ایران دفاع شود و نشان داده شود که ایران همچنان قدرتمند و با اعتمادبه‌نفس در عرصۀ بین‌المللی حضور دارد.
🔸
در ملاقات‌های انجام شده مشهود بود که جمهوری اسلامی، برخلاف آنچه آمریکا و رژیم صهیونیستی تلاش کردند نشان بدهند، اصلاً منزوی نیست؛ بلکه به‌شدت مورد احترام است.
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/465184" target="_blank">📅 07:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrFbF-Ttw5kF0pRc9CkGrMyVZsdPQIoDlSoG8eXxaTy9BmKvjEV372AWZeFBbXKL6gu93YylAntuj057Bfixr5nZFvMh7MbA_UAoy6aeFJxQiQCKJxRHVL8UNYJ80giRSgoe_gGLIC-no8QZtPh6SH64JtAzqEET8J0drdxrx5HOXFDy58A1l0NambqpJrYWI_Cb1B9PBeTBeIAd9Ti-ZPn0iNbE3m8IT3B1GKKEeZzPhgtwSK0fKU3fX83FjJrrAuqRElaA762bD7D1gDQF2qGhXYXqUj3nGQVu1mC2IAPd-DJ7bc2uoeh7jPKuka1S-YjpFdlu8kvfXThdb8dY1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنوعیت صدور چک رمزدار از ۷ مهر
🔹
بانک‌مرکزی: در راستای حذف چک رمزدار و جایگزینی آن با چک­‌های تضمین شده، صدور چک‌های رمزدار از سه‌شنبه، ۷ مهر ممنوع و همچنین پذیرش (واگذاری) چک‌های رمزدار در سامانه چکاوک از اول دی‌ ممنوع می‌شود.   @Farsna - Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/465183" target="_blank">📅 07:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465182">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG36kOshHfMLu3_8HNeFzIDSJBFInMQgloxB3moaeClT4H0whhq0f2UrTTltPgZzCaI7_9Sh95kdQ_7sv6DbHpSUg_DhC4NIk7Ou6b3cZw41kbkU4GPSEhnuYuV8kejO2xAtq1txMuv657O28Ouc86yGVn6AoeFAgc8zLwaWcS7ahlItnKf7_ZRhPqjoChIsyEbRPu3pQs8od0suPZcCVbeRNiWEMIna9vRX5iu2dbpqsYoNpCes19KgPp2tPZQ9MI7gLj_qLrA1vJjCjtOTbMVd5ay77y7HzklkSlIEvG2kzpQ83vfdBBYkkYi-JbZtrgKTSymt0yC5On1LvCQECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدالی که پس از ۵۲ سال دوباره به ایران رسید
🔹
محمدرضا طیبی در بازی‌های آسیایی ناگویا با ایستادن در جایگاه نخست پرتاب وزنه، طلایی شد تا مدال این ماده پس از ۵۲ سال بار دیگر به ایران بازگردد
🔹
طیبی با پرتاب ۲۰.۸۱ متر، بالاتر از تمام رقبای آسیایی خود ایستاد و علاوه بر کسب مدال طلا، رکورد بازی‌های آسیایی را نیز شکست تا قهرمانی او رنگ و بوی تاریخی پیدا کند.
🔸
آخرین طلای پرتاب وزنۀ ایران در بازی‌های آسیایی به سال ۱۹۷۴ تهران بازمی‌گشت؛ زمانی که زنده‌یاد جلال کشمیری با رکورد ۱۸.۰۴ متر قهرمان این ماده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/465182" target="_blank">📅 06:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نمایندۀ ایران در تراپ زنان، از فینال جا ماند
🔹
مرضیه پرورش‌نیا در بخش انفرادی تراپ زنان با کسب ۱۰۸ امتیاز در جایگاه سیزدهم قرار گرفت و تنها با ۲ امتیاز اختلاف از فینال باز ماند.
🔹
فردا او و محمد بیرانوند در تراپ میکس رقابت می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/465181" target="_blank">📅 06:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465180">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSaz93dWChihBBcCvBVr6gOgGPn4h-QGf7EZ6gHEeszEEiBBou-Z440JxT0LdxXhNRVRoPXogO2H9SL2LQC1tBD58u1tmRWSWr1UFS-B-r39vNPC-3wwMq8sKaTBBfVH8Q4NPpV_r80CxrznANimd692y0vegIS_X1Vm4wvICsjnd6sfu4BxOWKP9m_Daqkpv0dZrPKzHwW7WdgqKhgpCYarqaXYto-iM9i4wOE7F0X9-w6evw1azP7iW6g-RbjUU4IRy5qSurYXI8kkgQhAGkL5y80OesHx3qkz1hDLnwbd8U2b8TKPJxUSnrrQUyvAtm4IrOX-u_omsZF5W-xKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمل ریلی چین به ایران ۱۰ برابر شد
🔹
ظهوریان، عضو هیئت‌رئیسۀ مجلس از افزایش ۱۰ برابری حمل ریلی کالا از چین به ایران پس از اعمال محاصرۀ دریایی خبر داد و گفت با فعال‌سازی مسیرهای زمینی و ریلی، امکان صادرات روزانه حدود ۴۰۰ هزار بشکه نفت از مسیرهای غیر‌دریایی نیز وجود دارد.
🔹
گفتنی است این رشد با فعال شدن سه مسیر ریلی و افزایش ظرفیت بنادر شمالی ایران رقم خورده است.
🔹
ظهوریان تأکید کرد اگرچه این ظرفیت نمی‌تواند به‌طور کامل جایگزین حمل دریایی شود، اما در شرایط اضطراری می‌تواند به‌عنوان مسیر جایگزین مورد استفاده قرار گیرد و حتی در شرایط عادی نیز به امنیت تجارت خارجی ایران کمک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/465180" target="_blank">📅 06:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465179">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تیم اسکواش زنان حذف شد
🔹
تیم ملی اسکواش بانوان با نتیجۀ ۳-۰ از هند شکست خورد و حذف شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/465179" target="_blank">📅 05:55 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
