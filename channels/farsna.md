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
<img src="https://cdn4.telesco.pe/file/tL4PrONFlb9XBXACl9nhLr6KAzjkq6VCdCCkcH7jOlK7icl5eRQa78Z9nIl2G9gvgWy5_xUqDwZErEjdZsklDz0_FvQZVJ6yHhbUIdlj91nkMx22XFoJQVKLlDsJc2uRBvOB2VGvvUALYVgOmYu1BKJmkToFem09mWDk_5qaGLN5VxC-bJ9OB6-CdpZMCdI9tPgDgnxtVLLESlmr3_NiTjrnOFlWforThTjZzd_24Xdj7P3riy7xuKfuNfO7t7daAEPcFPzUrruWKnyIgq1ZfQ66h7koA5N_RXI4V1KZeMNdXB_6HOHPrYy5kcRSsrJEEZJECysWtp43X5O8Dn_XiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 08:58:46</div>
<hr>

<div class="tg-post" id="msg-460618">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سپاه اصفهان: عملیات انهدام کنترل‌شدۀ مهمات امروز در جنوب اصفهان انجام می‌شود
🔹
احتمال شنیده‌شدن صدا در محدودۀ صفه، بهارستان و اطراف آن از ساعت ۹ تا ۱۴ وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/farsna/460618" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460617">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6398035fdf.mp4?token=Hd3mDWXzmvsa6pUo2ArBxjTCxlnosyzg1ZzLqm9eBbMywSh-5ifGleUF07E1CSNq5LtSi_nGUWxD6XtmKCKNuXBDoYUvQ9F9W3m4MsQGuoJhyOelqby4sWItOLf_lcTi8O2WU_lvp0ppoFU1RZmvRrXHnookO_SxDO_tlh0MW3oSHIpoayIEVVUlmGLR8bpvRNi4aMh3u6CN3f8HhhtLACw1bxSIwiD9ovJYNJaNno021TJC_8u8_t2tdUGbEr161eWXwn-QFGp0EG0WCR2Qyrvbkr-KmTQuIk1IQwdyMsbMMif2aKG2UUuQgMcyfEyBQTcHjvTAlGDjE4HJvxNqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6398035fdf.mp4?token=Hd3mDWXzmvsa6pUo2ArBxjTCxlnosyzg1ZzLqm9eBbMywSh-5ifGleUF07E1CSNq5LtSi_nGUWxD6XtmKCKNuXBDoYUvQ9F9W3m4MsQGuoJhyOelqby4sWItOLf_lcTi8O2WU_lvp0ppoFU1RZmvRrXHnookO_SxDO_tlh0MW3oSHIpoayIEVVUlmGLR8bpvRNi4aMh3u6CN3f8HhhtLACw1bxSIwiD9ovJYNJaNno021TJC_8u8_t2tdUGbEr161eWXwn-QFGp0EG0WCR2Qyrvbkr-KmTQuIk1IQwdyMsbMMif2aKG2UUuQgMcyfEyBQTcHjvTAlGDjE4HJvxNqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی از حملۀ پهپادی به مقر تجزیه‌طلبان تروریست در سلیمانیۀ عراق، و برخاستن دود از این محل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/460617" target="_blank">📅 08:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460616">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZE9HufZnjg9oWscPVzziONa5w1xxY_PIhX0ymVkCMPRzM-Opt1Dm6SizI4mfEMqR0yW24FEu5_80SfRfurean21MmoZpQMe7dJTB0chJ95TiO1jb4kJZR4KEGKwXr6gcmgCa8X1Cutfye6ElOFYMe3NxHkvRW0uteYEs3IdQhEF6Al8gA20ci-SlwBBJUPkLzQwk5a6xyt_hVkqirructKpoGVyZ3imnk-pWALjqXHktXGNHuiJy8CZ9oFBkvfWt59lSLobGscql9mv2Q37EeOClmxJI0evTe0U_4dAGPRHr3f4kqn8_loWb06T_ybIjfo3xj0PBcPIV-012oDMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس علیه استقلال تا دادگاه عالی ورزش CAS می‌رود
🔹
پس از هفتمین دربی پایتخت که با تساوی استقلال و پرسپولیس به پایان رسید، باشگاه پرسپولیس به دلیل آنچه حضور غیرقانونی یاسر آسانی در ترکیب استقلال می‌داند، از این بازیکن شکایت کرده است.
🔹
مسئولان باشگاه پرسپولیس معتقدند مدارکی در اختیار دارند که نشان می‌دهد آسانی به‌صورت غیرقانونی در استقلال حضور دارد و به همین دلیل پیگیری‌های خود را از طریق مراجع قانونی و فدراسیون فوتبال آغاز کرده‌اند.
🔹
شنیده شده مسئولان باشگاه پرسپولیس قصد دارند در صورتی که از فدراسیون فوتبال به نتیجه نرسند، پروندۀ این موضوع را به دادگاه عالی ورزش CAS ببرند تا شکایت خود را از طریق محاکم بین‌المللی پیگیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/460616" target="_blank">📅 08:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460615">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk0qfkt8vrYwpTx0Lvs3WraOCd-pH_Vj75l81yVKX4ZJ7VQ-au1qffgf2o6REBON8BGf18a76mS-Qnjdif1uWIqmVX7SDmlb8wS1b73oy5y97odQaUiDBHsBZFbxAutwLk-qpAXhKfBVnG8kqjYjJl5TU0wkQQoSvEXc7eauq_-lA-lAFVYQHt5cbFqFFU-rbq6Uqj2-HLZ7Ln6xBRWGGZV_Y-d5Vh3iBoiy8TtHeGjF9rMfYn857FThREtqa139LGN58yK50OV-GLT9NfBOUlRGtfq3tc_TGM-uWVxxbruyER2uquJirqI7BBF-D4nIomu8pvoZYYHiUllDqfKSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی‌ها از هرمز گریختند
🔹
داده‌های جدید شرکت رهگیری کشتی‌ها «کپلر» نشان می‌دهد که میانگین تردد روزانه کشتی‌های باری در این آبراه استراتژیک به ۱۰ فروند در روز رسیده که رکوردی بی‌سابقه در ۳ تا ۴ ماه گذشته تاکنون محسوب می‌شود.
🔹
کاهش چشمگیر تردد در تنگۀ هرمز درحالی به‌قوت خود باقی است که وزیر انرژی آمریکا دیروز ادعا کرد به‌طور متوسط روزانه ۹ میلیون بشکه نفت از تنگۀ هرمز عبور می‌کند.
🔹
اما براساس داده‌های امروز کپلر در روز شنبه تنها ۲ فروند کشتی از این مسیر عبور کردند که ناچیزترین تعداد در روزهای اخیر است.
🔹
روز یکشنبه نیز ۶ فروند کشتی تردد داشتند که اکثریت آنها از مسیر آبی تحت کنترل ایران گذر کردند.
🔸
یک مدیر کپلر گفته به نظر می‌رسد وزیر انرژی آمریکا عدد ۹ میلیون را از هوا بیرون کشیده است. واقعیت این است که ایران کنترل تنگه را در دست دارد و تنها نفتکش‌هایی از تنگۀ هرمز عبور می‌کنند که از مسیر آبی تحت کنترل ایران حرکت می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/460615" target="_blank">📅 07:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460614">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هوای پایتخت همچنان در وضعیت «قابل قبول»
🔹
شاخص کیفیت هوای امروز پایتخت با قرار گرفتن روی عدد ۹۴، در وضعیت قابل‌قبول است.
@Farsna</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/460614" target="_blank">📅 07:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460613">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌ روایت برادر همسر رهبر انقلاب از مأنوس بودن ایشان به قرآن
🔹
در یک سفر با هم بودیم، من می‌دیدم جایی که هیچ کاری ندارد، قرآنش را باز می‌کند، دو صفحه می‌خواند و نشان را جابه‌جا می‌کند و دوباره می‌بندد. قرآن مخصوصی دارد که اصلاً از خودش جدا نمی‌شود.
🔹
ایشان…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/460613" target="_blank">📅 07:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460612">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">امروز، آخرین مهلت ثبت‌نام آزمون کارشناسی به پزشکی
🔹
داوطلبان آزمون پذیرش دانشجوی پزشکی از مقطع کارشناسی سال ۱۴۰۵، تا پایان امروز فرصت دارند نسبت به ثبت‌نام اینترنتی و ارسال مدارک مورد نیاز اقدام کنند.
🔹
دانش‌آموختگان همۀ رشته‌های کارشناسی مجاز به ثبت‌نام هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/460612" target="_blank">📅 07:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460611">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تردد در نقاط حادثه‌خیز و فعالیت‌های دریایی مازندران ممنوع شد
🔹
مدیرکل مدیریت بحران مازندران از احتمال وقوع سیلاب، طغیان رودخانه‌ها و رانش زمین در پی فعالیت سامانۀ بارشی در سطح استان خبر داد و گفت: گردشگران و فعالان دریایی از تردد در مناطق پرخطر و فعالیت‌های تفریحی خودداری کنند.
🔹
همچنین هرگونه تردد و فعالیت غیرضروری دریایی از عصر دوشنبه ۱۶ تا صبح چهارشنبه ۱۸ شهریورماه ممنوع اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/460611" target="_blank">📅 06:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460610">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سه روز بلیت نیم‌بهای سینما از ۲۰ شهریور
🔹
به‌مناسبت روز ملی سینما، بلیت سینماها از جمعه ۲۰ شهریورماه به مدت سه روز به‌صورت نیم‌بها عرضه می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/460610" target="_blank">📅 05:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460609">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxbezPPb2CDnZZm9tmozC6432-ufEs-TngaS3UzIQuTIWgsuXcDg3WnpxHsWkOp5ApOMeyXpjJt5kJ1DIbvqqDKcHnrtWNtyrGldpBQsqImESgyQlTNDGK-0zI3ZvgyghENXGFaTf7por4HSOqFmr0GSWnuVtXjXq3Vppoq6gV57zfuaRSvK_IwnF6fUw0dUt1ii7shnKxdCs2Nus48o2NJ5QrE2J1dDcl8yfKot3EmDIUWPoRjoJ_3ehyoIVHQYdPvrgxRnarNKj7zwPl_ffxI8kSheKnmgEv-qVT0w6T2OybklHq1tdbGAP1R8wcxw1J5jnBTxpt8QqZv1zN17TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دردسر جدید ایلان ماسک برای حذف فرمان و پدال!
🔹
ورود تاکسی‌های بدون فرمان و پدال تسلا به خیابان‌های تگزاس، با واکنش تند پلیس راهور و سازمان ایمنی جاده‌های آمریکا روبه‌رو شد.
🔹
علت این واکنش پلیس آن است که تسلا بدون گرفتن مجوزهای رسمی، فرمان و پدال را به‌طور کلی از خودرو حذف کرده و قوانین ایمنی فعلی را که بر اساس رانندۀ انسانی نوشته شده، زیر پا گذاشته است.
🔹
این جنجال قانونی در حالی آیندۀ تاکسی‌های خودران را در هاله‌ای از ابهام قرار داده که حذف امکان کنترل دستی، ترس و عدم اعتماد شدیدی میان رانندگان و سرنشینان ایجاد کرده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/460609" target="_blank">📅 05:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460608">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عرضۀ واکسن آنفلوانزا اوایل مهر
🔹
سازمان غذا و دارو: با وجود تأخیر تولیدکنندگان خارجی، افزایش قیمت و مشکلات نقل‌وانتقال مالی و حمل‌ونقل، واکسن آنفلوانزا از اواخر شهریور و اوایل مهر در دسترس قرار خواهد گرفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/460608" target="_blank">📅 05:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460607">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ المیادین: تیم‌های امدادی تاکنون ۱۰ مجروح را از ساختمان مورد حمله در نبطیه در جنوب لبنان پیدا کردند. جست‌وجو برای یافتن افراد دیگر ادامه دارد. @Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/460607" target="_blank">📅 04:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460606">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نجات بیش از ۳۰۰ نفر در آتش‌سوزی یک هتل‌آپارتمان در مشهد
🔹
سخنگوی سازمان آتش‌نشانی مشهد: حادثۀ آتش‌سوزی گسترده در طبقات منفی یک هتل‌آپارتمان واقع در خیابان آخوند خراسانی مشهد به وقوع پیوست.
🔹
بیش از ۳۰۰ نفر در محل حادثه گرفتار شده بودند که با حضور نیرو‌های آتش‌نشانی و انجام عملیات امدادونجات، از محل خارج و نجات یافتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/460606" target="_blank">📅 04:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460605">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8ec87ac3.mp4?token=CD8qNngYzRhwxo_ODE9O6dngXOWhMErhdU878LwOqRmezA5KVmXLjN1KuxN5IWJSktRql3Jv2878Viuh11hqUF1OdNWGv2YPiCF5k_Sga8nh8QvS9D_xpJ4IuSwyjXqhZvOUczS5LrUEw2qbx07uJkxV6IGt3rvW7Jwe1ml_aXK-Ty5WVnnnHKogXE46bmObBLYJWnpNaISIaFZnhhtNAfq9WyrXgwzVQsVyagZOOO5mGBrdJp_Lm_3swFSY0Q-RiuQ-h4XXfoTsKAr4LgOq7lzg3W6IccSZDo5WyWl9jmdf_YHwDkDVsbgdC-JB9DbH8UCFNxD6AP1QTgLKgc3MLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8ec87ac3.mp4?token=CD8qNngYzRhwxo_ODE9O6dngXOWhMErhdU878LwOqRmezA5KVmXLjN1KuxN5IWJSktRql3Jv2878Viuh11hqUF1OdNWGv2YPiCF5k_Sga8nh8QvS9D_xpJ4IuSwyjXqhZvOUczS5LrUEw2qbx07uJkxV6IGt3rvW7Jwe1ml_aXK-Ty5WVnnnHKogXE46bmObBLYJWnpNaISIaFZnhhtNAfq9WyrXgwzVQsVyagZOOO5mGBrdJp_Lm_3swFSY0Q-RiuQ-h4XXfoTsKAr4LgOq7lzg3W6IccSZDo5WyWl9jmdf_YHwDkDVsbgdC-JB9DbH8UCFNxD6AP1QTgLKgc3MLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): در زیادکردن دوستانت تلاش نکن
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/460605" target="_blank">📅 04:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460604">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌ خاطرۀ برادر همسر رهبر انقلاب، از تولد اولین فرزند ایشان
🔹
فریدالدین حداد عادل: برای به دنیا آمدن اولین فرزندشان در بیمارستان رسالت، چون ملبس نیامده بود، کاپشنی که مادرم برایمان آورده بود را پوشیده بود. جفتمان شبیه به هم شده بودیم.
🔹
ایشان وقتی در بیمارستان…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/460604" target="_blank">📅 03:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460603">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌ المیادین: ساختمانی که دقایقی پیش از سوی رژیم اشغالگر اسرائیل تهدید به حمله شده بود، مورد هدف واقع شد.   @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/460603" target="_blank">📅 03:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460602">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌ اعلام حملۀ هوایی اسرائیل به جنوب لبنان؛ صدور دستور تخلیه برای ساختمانی در نبطیه
🔹
ارتش رژیم صهیونیستی برای چندین ساختمان در منطقۀ دیرالزهرانی در جنوب لبنان، هشدار تخلیۀ فوری صادر کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/460602" target="_blank">📅 03:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ادامۀ جنایات اسرائیل در غزه و لبنان
🔹
منابع محلی از تداوم حملات وحشیانۀ رژیم صهیونیستی به مناطق مختلفی در جنوب لبنان، و همچنین نوار غزه خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/460601" target="_blank">📅 03:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnNB9p4CVFxhVy2IDeFRmaQAEqSEz5N6gR5LgquNI4gzg0LUjqn4zNsB_WECHzuwtFgmUu8p1A8JRu5Bj3FhOwb0oPnwQFCQ0viVzeDRj2DiOgAWE4j7_QAgwRMWrKabpwh4c-Tjp1uVtHlfJbMF1WkKUFteAFu1yg7f_yUWDzLB27lMULPNDd1P4-xar8rKas6RMB3GcG_cBv93jZvsUJ_jN5PXjhLgpwlGVUFDbs6_c9GbW3VUmMxgYTVm8bXdByMlQTux9FPtN7MBMdH1xADDTqL7DLSZFXXGm8Waibz5CE0ofaYVVQO3RRm-0f8ZrGK5Zmn2s0QRtTZdonynXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنجیرۀ «پاسخ هسته‌ای کرۀشمالی» مجهزتر شد
🔹
رهبر کرۀ‌شمالی در مراسم آب‌اندازی و ورود رسمی ناوشکن جدید این کشور گفت که این ناوشکن بخشی از سامانۀ پاسخ هسته‌ای پیونگ‌یانگ خواهد بود و می‌تواند حملات تلافی‌جویانه «ویرانگر» انجام دهد و استقرار این ناو در آب‌های شرقی شبه‌جزیرۀ کره، پیام روشنی برای دشمنان پیونگ‌یانگ دارد.
🔹
رهبر کرۀشمالی همچنین اعلام کرد که طی هشت ماه آینده مرحلۀ دیگری از تقویت توان دریایی خود را به نمایش خواهد گذاشت.
🔹
کیم همچنین از ادامۀ ساخت پایگاه‌های دریایی در سواحل شرقی کره شمالی خبر داد و گفت این کشور قصد دارد یگان‌های جدید دریایی ایجاد کرده و انواع مختلفی از ناوهای جنگی را تولید کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/460600" target="_blank">📅 03:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460599">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39055cd071.mp4?token=fteVMwln9fB1baOpbt_orgpWFCMHvgpR6k-082L8Hl3RXzICDvE9aiOuAPcVSUyT-TwB4NM9X2TQnw-MjUFjQDB_8ApC_vNAhcuj4dH1_v1QdtirNnSWfyPgxngufoBt-_SC0yeIKZr2wWUQ4uVRKRP_blFiwuO-VCcyRUCMiYkKnEEHh3mlvtds0czR7C4oZsMCVVX3_LFhcy7Zgb5OB88aJ83BPadySPkYv5qrju034M30qXZZ9AxkNatF-n1sp3hyEl9jRpWVopofoMyp3bZ6uiHWh1fDH-HizOdaIB6ABBUvJgspDDwKG_EOuEWvOhoKf4vaXolTTUp2Aerx-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39055cd071.mp4?token=fteVMwln9fB1baOpbt_orgpWFCMHvgpR6k-082L8Hl3RXzICDvE9aiOuAPcVSUyT-TwB4NM9X2TQnw-MjUFjQDB_8ApC_vNAhcuj4dH1_v1QdtirNnSWfyPgxngufoBt-_SC0yeIKZr2wWUQ4uVRKRP_blFiwuO-VCcyRUCMiYkKnEEHh3mlvtds0czR7C4oZsMCVVX3_LFhcy7Zgb5OB88aJ83BPadySPkYv5qrju034M30qXZZ9AxkNatF-n1sp3hyEl9jRpWVopofoMyp3bZ6uiHWh1fDH-HizOdaIB6ABBUvJgspDDwKG_EOuEWvOhoKf4vaXolTTUp2Aerx-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر شهید مدافع امنیت در تنکابن
◾️
شهید امیرحسین سلیم‌زاده در حملۀ دشمن خبیث آمریکایی به خوزستان به شهادت رسیده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/460599" target="_blank">📅 02:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460598">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">روایت فریدالدین حداد عادل از زندگی و شخصیت رهبر انقلاب
🔹
برادر همسر رهبر انقلاب: زندگی آقا مجتبی بسیار طلبگی و ساده است. در قم که بودند، خانۀ ساده و وسایل محدودی داشتند. کف خانه هم تنها با موکت مفروش بود. وقتی هم که برگشتند به تهران، رفتند و در یک خانۀ ۷۰،…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/460598" target="_blank">📅 02:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460597">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ادامۀ جنایات اسرائیل در غزه و لبنان
🔹
منابع محلی از تداوم حملات وحشیانۀ رژیم صهیونیستی به مناطق مختلفی در جنوب لبنان، و همچنین نوار غزه خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/460597" target="_blank">📅 02:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460592">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVfk1eWYYiRwyYoCZ-uLtRKFum3r37QV6Y40qBClt-6W5DXUzlMmd2w9QwH8Jq069BAoXhIUHJsCg-oMCwRQ3D18ZhTuAAMlO_QMIs3_e1ZhB0NwMmDAe97oAfaXM1Rur2zBh39TIBWQsdcjjTZWZf3kS-kVXw38qZszggRj9a2YttrMoYWcuQtmSJtQTwwUgF7iDnSXmYa7Ib1O-AQBAsvuzlvy3E3KOsIwemjlPTvDyjRrHE-q5Ne4RMGeHDcNoEI6jpJLzx8ThNitHa0WOWyLjYTYVW0tYMLaM1BH2YFt8RrhzpfroAmhsNGRxk7kfC1xQu5gE-QjMeiUHqV5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vH9OYvtLnixX4Kj-PgypmXFufnzvgb9qsuQ5IXGVskkORJG_I0c8FX5hKidsGMALFe9SMCNZSCiAI47gHT7gCWL06PzB-Ot_Mp4nSdsreNY0ZIKB-0oIpxAhrUeICsJgdOfhNb10RqFCTxhhgq7FB8gTldw7KG36sfaIiJXYltZM3ETqFWH5U7BCDf3pUr5P2IVUhnXXQWbRXVlmKAkLw_yVQtdF0XbwNtugMKswTJiRaLY3hdg5pplXJVgZHUqf6XriBib2l789TJyeOkpSHcyKYkxhkBl3pa2szp67osFsnzJOGN1_n_UEUiKqslQgEQ8HaCvTGG66NevDOyvC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOg02nyykBdYZp9zZOAeJEI_8d-BJsWRRX0WejROhojjOJ7yseXvBiOjmGomWf14Gjxs90OcSE4ulvbrJghsSdDROC7YhLKF4bIDNN60UVSWLcakzc9crXeYFQB-l0Lyc1Kekl-dO5bHTV2hwg9MkgiIUGOTvA1Z3myTNtvEC73D4a91JdUxLuZppRO9u7Iw4BrySehHSv64iG15wxqaGDF3hWBTjhpstGcv7Y__5pXKUukqe-auz9pxuyU3BIaJTeQ9SJos_XhF3uysQ4Mn3wt-RR8B9FgafSvmDoORiGQyLjJWjtPRXfogCIGnkWf7ZFsvpKBeDJoCuXMShO3G1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqsqeSxaQ67FskSiOgmLFbE-oXcGYxR5OvVnEwouLUQDhmE3BiLrh6Zgtpy6M-X8qcnyC4ueuBDOnu12V2iZZbzOtKMtcX6mfo68QJmIUzbklmwXbJ0OylE-fPLU4HXumZh0Q9ospcw28FQWSXh1yWsLhhQ-_B42y_3qAsgdjxXGgS6bqy1lOcY9ssHtrLlqvZSg9R7khN49cVZk06ob3fOByjJtObCGNrT-HBd8JOPhN1C4OeC3O7g5gh2VH1B57BP_B192W65WhzD54wa6ekfQ1pNosHgujKDme8zXiWFRCd9LNaID0FcGKO7aqCDB6DFPHrOJNils-iecswiU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2lhY0St5I-BTRLGqrVjgyinBOOdwBGqcRb8bC0fJZdsvR33LaKT5yGfJSvw9REYZS2Po2Sw7ULoIx0AId1sAB9scsnAB5crU1-fjbfLnlvlJ8k0KO2C5lHJqCRUKcPwxXkOfXV2HIq5QwKJNF_Th8ZKG4987xjv7cxwwGxB6N2Lxqa2Lb38Rn8xCfquohFbfbMIkEpZ7rHRYILeWUE2pHTumtCVecwiGJZ8uqCvQqls_0BC9wDAmC2l_oSm3444H8PJYFGk-2OStsG9HwkQYUwUhMpFsnSPvog0FKeKRTcKgCbe2YyanblaXSALanjR5d6gjQ1kqfwjLFgDEHkJ-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قطعات موشک به‌جا مانده از جنایت آمریکا در عروسی سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/460592" target="_blank">📅 02:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460591">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">روایت فریدالدین حداد عادل از زندگی و شخصیت رهبر انقلاب
🔹
برادر همسر رهبر انقلاب: زندگی آقا مجتبی بسیار طلبگی و ساده است. در قم که بودند، خانۀ ساده و وسایل محدودی داشتند. کف خانه هم تنها با موکت مفروش بود. وقتی هم که برگشتند به تهران، رفتند و در یک خانۀ ۷۰، ۸۰ متری ساکن شدند.
🔹
خواهرم در مدرسه کار می‌کرد و خردخرد فرش ماشینی و مبل راحتی تهیه کرد. مبل سبزرنگی بود. با شوخی به خواهرم می‌گفتم آخر این چه رنگی است گرفته‌ای؟! و این‌طور سر به سرش می‌گذاشتم.
🔹
یک بار خواهر بزرگ‌ترم گفت: فرید! دربارۀ این مبل حرف نزن! زهرا بعد از مدت‌ها پول جمع کرده مبل خریده و تو مدام به رنگش گیر می‌دهی، او هم اذیت می‌شود. قبول کردم.
🔹
حالا بعد از بمباران، این مبل بزرگ‌ترین چیزی است که از آن خانه باقی مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/460591" target="_blank">📅 01:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460590">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌ المیادین: در اثر تجاوزات رژیم صهیونیستی به نوار غزه، از بامداد امروز ۴ شهید از جمله دو کودک به شهادت رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/460590" target="_blank">📅 01:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460589">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=AIzk9VmLravLyafOXpwuQCvmeyFDjoMdL5k3hW5FOwBopc4gDJULI73nIe1KfImKK1WLCmi20GDAWRe4Ofv0Xu7is68I66ySt38cEANvlQBYLijs1Pph-QqmegqLvSgb42ILZtHWeW-NCiGhycDM2WAexg0_qBntmWBX6KypZE_pygLlXljUo-Xx68pc58m3w5VAtlUusue7BQWL6R2Djoly2N3awrJvj6326BXnOkcKEAjvX6SNXCxvD7a0sq406fbkjSzTekJxuA7yk9Gdenxr7Em0Onm4XmkxjfRogAedUW4iXTLZJFLQJI9ZHLQ9HDsGbEwISoeazMqdoSD0pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=AIzk9VmLravLyafOXpwuQCvmeyFDjoMdL5k3hW5FOwBopc4gDJULI73nIe1KfImKK1WLCmi20GDAWRe4Ofv0Xu7is68I66ySt38cEANvlQBYLijs1Pph-QqmegqLvSgb42ILZtHWeW-NCiGhycDM2WAexg0_qBntmWBX6KypZE_pygLlXljUo-Xx68pc58m3w5VAtlUusue7BQWL6R2Djoly2N3awrJvj6326BXnOkcKEAjvX6SNXCxvD7a0sq406fbkjSzTekJxuA7yk9Gdenxr7Em0Onm4XmkxjfRogAedUW4iXTLZJFLQJI9ZHLQ9HDsGbEwISoeazMqdoSD0pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهران رجبی: حضور در تجمعات شبانه وظیفۀ ملی، دینی، دنیایی و اخروی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/460589" target="_blank">📅 01:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460588">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do9w_K_5pu3Uzy7TOlM52mOxoXFlEfxs_s8xyxA5mvVmiewMnswT1Y8HKk-2DyTtlO_q_uJEL4WJkMdXrb5TyljCr9HRB3-KKCN60d1EqC7C_-JCXdx54LdckFeNn9rzs0JnxaSFNd4YjpcDmwejKRBpV8UxsSNi0h0kNtn826Xm4bCzDFUROD8o8eKIAkxYQaTdMj6nacQs27CiVOk_U9ManaP_plz-evPHTB57Phv25JnJVzWkVHJmsbG_eeXBM7dAlwTNK9nM79vk_WMY7dcvRvvDsg1pxl2xUihUmOd3iJMhFZwXeYJR_pV5mI-1quvI4cG-REPDZAMaXbnCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سانحهٔ هوایی در آمریکا؛ ستون عظیم دود در آسمان میامی
🔹
پلیس و واحدهای آتش‌نشانی میامی پس از سقوط یک هواپیمای ۷۶۷ پرایم ایر در فرودگاه بین‌المللی میامی به منطقه اعزام شده‌اند.
🔹
گزارش‌ها حاکی از آن است که این هواپیمای باری امروز بعدازظهر به وقت محلی از باند…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460588" target="_blank">📅 01:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460587">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyKuI-dtBRa8IZ_mmOg7D5xNO1tJ6ZDkBb9ajrTRd3LmPtLjdP7LS6YhT1tb3K5pOxv8lpI_g9zV100NhKnFz9E6CL4uODSq3435uvTw8A37N2lYfu1VOfS8dTL4q96uxb-fO3UpKU86jKl1s9YaeLudf090XzfxyyLxJYTu5I90XiW9nyumKzL_B-uv--h96AbYBAeJ0PwefIx_T-tChDZggMUoAundiJ0u4PQaQUWUX0OAO21pAa56s8OfNEIzo4hQ-b96HeYlMS0H29TrBONAuq1aYje-sQk2RP-08b24lfeg09nyEmDVrY_FOEm25RFQJ3XKq4onUrE2n-Ep7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: اقدامات تجاوزکارانۀ آمریکا عامل ناامنی در تنگۀ هرمز و اختلال در کشتیرانی تجاری بین‌المللی است
🔹
سخنگوی وزارت خارجه: تنگۀ هرمز تا پیش از ۲۸ فوریه که آمریکا و رژیم صهیونیستی به ایران حمله‌ور شدند کاملا باز بود. واشنگتن جنگی غیرقانونی و وحشیانه بر منطقۀ ما تحمیل کرد و جریان عادی کشتیرانی را مختل نمود. نفت‌کش‌ها متوقف مانده‌اند، تجارت مختل شده و بهای انرژی سیری صعودی پیدا کرده است.
🔹
اکنون واشنگتن تقلا می‌کند ایران را عامل این اخلال و ناامنی که آمریکا خود مسببش بوده است معرفی کند و کل دنیا را مجبور به پرداخت هزینه‌های گزاف اقدامات غیرقانونی‌اش نماید.
🔹
براساس روایت واشنگتن، جنگی که آمریکا آغاز کرده باید به نحوی وارونه به‌عنوان هزینۀ رفتار ایران برای جهان قاب‌بندی شود.
🔹
آمریکا جنگ را آغاز کرده، اما انتظار دارد تمام جهان هزینۀ آن را بپردازد و همزمان ایران را مسبب آشوبی جلوه می‌دهد که خود عامل آن است.
🔹
این وارونه‌نمایی، به‌غایت بی‌معنا و بی‌اساس است!
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/460587" target="_blank">📅 01:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460586">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ9cDXa5Lo6RxsNpW7312u4gjH1AdU56nepEpQLH8ha-JMaw1a-dOMellqKd3xWWtG3-9RKjTeEKATxM5WAIuNTU_2gmrsjEBtP14qEsIkMTIeVq7OYsEadR3Y5O502PTKzMNM_jf1sznJ-B_syx16iRbnphBvu0DZ643wBbwSzs0wqOT2r5e1HnM6QPMqKzkNLQ_Riw-N2m0mu-rYdRoNHY_Mzu1dnX95nKo7JaeOz9FYQ_HqHrd61-8oCwwixeSAobcr7HYvE6FcVXQc0So8xTta06G8T0DW582In1zaanPj5YVJ8qVFbUGaBeY7MCmVKt82x4E-VmgAN3yVhBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پینوکیو» فرماندۀ جنگ اقتصادی علیه ایران
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا فرماندۀ جنگ اقتصادی علیه ایران است. او در هفته‌های اخیر عملیات روانی را کلید زده و گفته‌هایی نظیر «افزایش صف بنزین در ایران» «رسیدن دلار در ایران به ۳۰۰ هزار تومان» و «تمام شدن نفت روی آب ایران» مطرح کرده است.
🔹
با این‌حال افکار عمومی در آمریکا و رسانه‌های رسمی او را یک دروغ‌گو می‌خوانند و معتقدند او دست پینوکیو را از پشت بسته است!
🔹
معرفی خود به عنوان کشاورز، ادعای سقوط قیمت نفت به ۴۰ دلار، و ادعای عبور ۱۳۰ میلیون بشکه نفت از تنگۀ هرمز، تنها نمونه‌هایی از دروغ‌ها و ادعاهای اسکات بسنت است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/460586" target="_blank">📅 01:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/di4ixeGzX4-SDdNtjXBAdY3kBBxtJv5XPIYsNyMxQ7_BQ0aO8KvKAK3D2bkQPfSha57-mQ9iFM6OFXXjmBLPbAGYANw6-isftbAaJ-DL4leKyZiXA_KIW-fI09KaSnK1olE2SiDN-fEoBszo3LVRxcoBJaTmDr-akhvVgZ999iH3316mq9Rk5POvLdFRounCNn4wZwlHG5MxYOSpjHtZOVpjLe-zSmXI8kIcamk6F2L3rZzFkOxRa-AoKbHx26jcU_-x0ASMCw5FZW2ZPCnTsbjqXZq53Q1IaEHQXjGuhYIpiWFALwSA4bp-Yy4faXMNuEQ1HicMvywex8TfDCg1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROFQIpRPPeruoUwLV9zgjbWtmx6TdiearridvIxy486kInjMY8quM-1ZTey_xL9yWME7diMOfJhaBww43YZdf9KyJRmMmwQxe1nHsh0-AWbjJW_3NwhHbtGevmEWi6ScsGqX1giZEOerqb_fpG6lJ3e6inPeSqe_g6f2mlyCZNuwTpXt252zfOURnt3l_4pjdCwHeJEQ44AwxHnOc6HhqDnYBcuamNyVS2K9N5fpHaOSDnNvNae0FlVIBkmHuGsRS0_VnGIqA9f8kXHrCn9KnSwMcqEFlSet2BzNotqd42coTtaCDBiE9A3LDi65UuWmEVcNgyzZkkABnr9DUKz4Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9UKf9yhbOYUGdKOd5NIOYUpIMIaLJtk9RbAP8x4gEwtVGmjK6H6bgsWGZ9jQLY7zMZWlMOAnsYCBq-mp1-O68WzZwcIZUSO-ApzPcN7WZrq4ACXk4N99tmvb4xbh3UC6l1QDSwpf5EPLrH4UnieVv1eX0-oiANimPcvryvARDNhCqDRBst4yncgI00X3YuamTHfNwJU6AUllCgTiohhBfFPlFKAOs4SjEjrD-2TQ4xkf5ZyuGl1voPXxZ0ARDuGkAEEUROPCOI0QXrZSyWeGyRYymf6sCRDsrLAlAJoyP6muOYjXSDdw0ph_cBmYe5j45sVgHqR26aOOeDTBAvEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjzcLxA9TqEKoexB4HaO_-8P7cMyDan_lNPM2R6LVCGP_PzIlP3WL5cxl_ZyEQKUzxRzbakEJe-XzOBmM-BBVxqc4Uy_p-5ZtHZsyNNyF3UmOBQcPXZHV3dt231K44IePeUX7isP0FvoGWJ-ig4weBbcgC6QZl9oh8MKFiyqE0tI3PeAWVoxM49U8MKwbaTeFjt4Az4NHR98vDY8JFzZZ7kiA6V5IWLmuIqkngbR_LZUf8iR2Q-hU8HQ4ASuNJNSZ5tsdL1KIOj1NK7vc495umo7Kp-KHeXY2YNdzEgbXILAdiI_vYI0IRnuCMB7Z18OIQz5HqxmsgtDLtB4V26M6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWWhSo6GhoNNbTxqFphkqdkKYt6p1qwM1dfeKoLkPSl9ydfc9QnKZDasjWJJNVEMOxxZQGs5yG5ZcBINwsDfWsmnevYpeT0KzHNYDK4f_mbRwQdteccUiolhVvhl0KVhDRUjl0gw4-PLkEr315yeQ0sWvvEUF7Fg0JKfopW7jnt82AEuNKGa5jRGP7B8Z_V5NZT1vDAA-dVjWrNHNe4iIrxH15s_C3Mzndp73wheNfga8WmWQBGXCne7p5h18eWb_DuUDoMdmG9Obh667eWovOoIq6NEpBG1sr__5seT2niv0mROzs-1KL8B5L6F9v1NgVbG0BTOiAtupmKpTmcNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTf0cxIPje-5GfUSWfQo239jfnb0AP74QA8ZCvxC9z0Uk9cQR6Mf53FIqclpUE4uYGiLffIcD0OE0ImJH3H3jVQFEvFouqJVxbG-GJ9dPIDByBge_QN3MEqNxwP86il3WndBMZnPVWs94ta1I6hGzHn7ZaiOCVtt7un9aXdunpS27n3z-yqDMdAL8qFluvfFqvisZtUGhoccZh35CtuiJRWrzv87vC_W993cM70Onx2_Xg2cmnMsUWhO4fW050EYCzvslpMLwE6IFhK42y8FPQUpwhHgF1-y7JzHffTCkkaXPRAJ5_dLQOc6NC1dQu9d6cQUNV5rqLTQ2aj7a-oybQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۶ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/460580" target="_blank">📅 01:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WibLpB6MSifJh97u4qRWfDThb44K6l0a3PZF78ikL9GnxtbvsbxEvLKBT-Uvm5Co2gbGFAcWIf802p77ifQuAZqmE61s6anpstfQUZnciAgajk1sAy63pL6kOIMDqQBozY2n6Rk5h0eY-EsXMn-yO5Z9x9PPJS8JXIecsWwuJvb8HPydXxgW3891RPOv0AHPEFtG6ZVsae-yRxPK3XUQYmcNwEDpKMtHpPEOV_Wd39AJS2TC4CPxamjp-colhpwcsboAqtjbVAxOr1Ehhc-YFUYGc2OpiCZBykBiceByKDlQYKaU0IGdsuykxNEkhSqGF4u0Ree5i8rDemVELBalTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSzdFv-mWJf3kVQQ6sxh8u6kvrGK3DY3yKSKLb0rn3m3w2StUPhBQqajKJ0HJX-tMeLZw80_1a-sGziaY7UaR0vBk7pfI6L2cbg76ZBWLkwI5MLbzJ-BjbNwFYnswpu9S3psL74a3s1zNJcWqEvQ2Q66lWxdDCXwDCGfUIzYUJOhqkGxTSjJcWis9eB7aFMyn3EbV6XtITw88YN2GnCBTpkUjYYKeMaNd7aFfsF8JHfirk9hnJHtBUENRIzy9590HRicN_LV_nGf3NR5_MN1M8dMF5bEwBTX8I-boW79KFst1RoAp8Peo5h44DVseFNe2I2WGCX9hh3eL_mbWxfPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B142DOhiZbvEUWFpOwOHKFaAcNIdrFEbVCndrhYrThTkFRmaUfydSVLyvEifEdWL5iCNn75HTDpVJ7SHX5-FztcQIEGT56nX_pLnA9bdUfuVWQ0iE58hyfgNj9fugbdHbxtUPcrFRMulHzozg3OvJM4LHl7aCiw7_wJvya-QqqnGAMkJQOh906nKmzJC0isfNzb7xjSwNueeEABsm1fK11Eq1LO7c-NNA-ftzMv4V-Ftsc0B9YFcm1YS3cuSmaRa-kKCURMaH74dpQBsEk9dzgDWtns3GBYFhFCYFaV43ZHJVXiEtFcCQdLl-cy2T2o9fhL-eZ8ArXh8lfWaSYU74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkOAbb1eL09f_iFIawtMonCzfDiadUsitad5NZQknAyKnFMx7FjTngYgyuzpTLyzlDbnsnYzNTvEJyyE616i0moeNIxeZdXuumZUVMGclnBDLYbPKKb5D6Eythh8ZTnt_vGy246djsikWpRUOvImdb2YCCxd_aA08HUqgLExPd9cw8eNT-YpWEihp5D0hcVbmIlfpUK98J70-TIqEj8mtxOhALi_8jOFVRbzuK_aEZ-NRdd_7YxuEQ9lzt2dzMUMrAdLqlZniYLV48khhA4zAMjMKjG-l_unHrGTDtufJyJ0Buo3HAEHMuyf20Zpa2mCNCaAlLuE7xGwtFrYV-K4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWrpS35gqRBPFpZ87xLOoUC5XZmuukEGOCt_eY63FBZ_VEEk5hh6DtYGs_p_NziC0DeLlPC5AzLjnlBXKww8uzSWlVU0kfbWLGNXQFp2AfmGAzhFMPndR-x9-BaKEtr7fwbEDundF2Hin5N3qyvopjVpqgdYdQ5Sw_oB97muH5l2hk-uH-L9_1goGUm44z4zGhbCS60lAGdvTDxvFWydxGv8-IdggeYuRNwSV07o-J87IY1hhGl7hVEdiZqYOqF4PDWCboabgUkzjhkF-bTM_VKijbIsbl8jQZLvy2Tctpqg_QZpU0jhLGyE8p2c9xHY8NBoIhfX5X_XHGCdciAT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbLPQ6SVjLGHwiQJwfjl3XSJVKP2yhHyI-dBN6WYGaXvB4fN8sKLebDrIvuEjqMIfhEBYvrnevstm_p9iAbKzblyBZetsRcD5crgL_G3cRZtKybbmHs4RnRsdsKP4ZkdZLpfMzWLt8DziMP_iKaj-kby_VCXORW6auTvMQV5RG99gpyXfRa9ahUyX-YNN6VU7Ht0BfmmbnurDGH_RVdJXyAUvJK2Trs_Gv6YDt26UhBt0U0s81qsz4HeJHh71NokshnI6ln3-k-TJlahUHCstO8O3oOFQLckCpx0Pf_SSBMtwGnhwHGH1Ma3yG1HEQU4YJXcjwwz8S6ySu2_kMyx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSvM3DlrIhvUAa2rtjsvndwJzFO6WvI9W-uCu7s-J5ROC2FX40FrsbN5z-raTc91W83DeJze6RXQSLpEpWqNZNT-MnKcdoMo7Ieeu8TeyAR7t2sDEC24m7nQO7FGkQjtPyQ85ojGDflLkOuX0dv9oTM4h75PaHHHjUBa3CHH16Uwq51TY6MAq3gQJrWuhfFKQop-yPDScsnIJ5BsqrGPtB6V_royMB4OHr6Fz_-GBni2hotw2zthLUyxn9DqdTvKFrJssmXiDWTZFei6wUPMiINJq0ZaqazN6ljkEJdWj3g3tDso5WQvfUGoG53aPDQ0PAAZod5uJ_CzbkuErqSl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIBcvI-D0PwygkD1Hy10RVAoKqDqUikcEfb72tqckM_lf0zRGDCI5RlEHo3_5DQxNe6Kb8QGqYX4YSQOijlaiXa6tKyGl3ON--7rLv8CQMHn-aSGn6fHTjjzfj3ikeFe0U8eB656ut_PI8_EG5Z8kyTbf-yb0JqrpPqUxtpuNXMvx8EvPZpJfU6GIJe5Sxu01FfmaD2dkWdC0B2XTiA5Phb3sXt6oRLmx8plYnsqxiwJsfwR0FaeL2YkHZV1kr6Tq7BcLdVoKIXnRJ215Y0__0bz0_NN2klknhABZopD0whTXn9CoQgTA4CZG-AokXQ3gXtkzVz9zfesaP8FTOTooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0vo_et-2KUfAzlDZWCYzHAziW28PVQKFLFSvy0x9onpFgI4aRtUlG3clEr7tGMx_ltn6D18MpFYNy-Az9ugrTQbpSJ69mg87XPx3oVeJujrNQCeBrMhnXKQOOvgKs2NkpBJ1olSIL6ZM9SMC3nQCfww6gwoJFWvKWl2UJJwvh6XthDdgKr9Pqpf9OcgWFmxI5A7H441dbkx7SnJCiqM15HScZb3Kutc5HtpoZWXxgxEX1lbccO5D5M90I_Wf_DeEuDfcNKpUZmuRIJAeIO052UeRGNGdexIr4WkdFjbzJ3upDJ1LLwWpVBcRfOkqWvZykfIKkGEuoF0IiVodQoUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akPSPeJWgQ6yxVbDw1efjI-T_jwTa1l__GMivF62W3YRjSkpHnB2BMQHGxzxXvBkEoor7e9ZJrkq7wHnQch99SFBCNRa0LiKdlqKWSIn3sksCFu4etvhrz0YmpDvJHxAmeRIfHx74WKRNPrfIa7niDXFydNiqCCnrPyFSyqTnRtOC02bX7AdimXbHSbkN9JvD97pMfXD3B6n1WZhJNhYVof7KdcRvvvMmYN8z8j-Jn189qBOVYkvM1ovdr1Qg0fxC7J6ESNzz2VFxsZ__AMpGUccSLwIoeZGS4Cn8-E7qUkGVJBtbJgCfUnp0yrn2OD3EcIE0ysn8tBmkN-MxtvEnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/460570" target="_blank">📅 00:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">زلزلۀ سیاسی در آلمان؛ پیروزی چشمگیر راست‌های افراطی در انتخابات ایالتی
🔹
برای اولین‌بار از زمان جنگ جهانی دوم و سقوط نازی‌ها، یک حزب راست‌گرای افراطی در انتخابات آلمان به یک پیروزی مهم دست یافت.
🔹
برآوردهای جدید حاکی از آن است، حزب راست افراطی آلترناتیو برای آلمان (AFD) با کسب ۴۴ درصد آرا همچنان با فاصلۀ زیاد در صدر قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460569" target="_blank">📅 00:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">در پی حملۀ هوایی اسرائیل به محلۀ الرمال واقع در غرب شهر غزه، تاکنون یک نفر شهید و چندین تن دیگر مجروح شدند.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460568" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460567">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a393542d86.mp4?token=dG4r0SuNIJO_QMX1MHJZd6b3dZ3IAFFnJvA_gjnx7OgekvjdQk9Sz8TxRsn-erArLhDuQ5J2X5ITKk1ZLw_Byd9FvR4edBgTaRrpQ_Hj5RILrX6tHSkAlNnRjnztWkcffgIM1yGZ6eD0HqzxHeKkNp2jquumFHTmbjxXOl-8xUbvQEOArGy8VjBoSgIG8cRWB2H5-2iAxEGlnpTOWzHdhGQOMRTzkmPsuoft2dfXYg-4c72mHGkacO1xWb0XSny4KWbOAOZfItMMis9xNrAKpvlNIJX-iVzvIDWNHEpx1E4Z3SIFSolEBCmfQQsKfReiTc1-d3Gdq2vu4lUOZ9FD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a393542d86.mp4?token=dG4r0SuNIJO_QMX1MHJZd6b3dZ3IAFFnJvA_gjnx7OgekvjdQk9Sz8TxRsn-erArLhDuQ5J2X5ITKk1ZLw_Byd9FvR4edBgTaRrpQ_Hj5RILrX6tHSkAlNnRjnztWkcffgIM1yGZ6eD0HqzxHeKkNp2jquumFHTmbjxXOl-8xUbvQEOArGy8VjBoSgIG8cRWB2H5-2iAxEGlnpTOWzHdhGQOMRTzkmPsuoft2dfXYg-4c72mHGkacO1xWb0XSny4KWbOAOZfItMMis9xNrAKpvlNIJX-iVzvIDWNHEpx1E4Z3SIFSolEBCmfQQsKfReiTc1-d3Gdq2vu4lUOZ9FD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرایان در ۱۹۰مین شب، روایتگر تداوم حضور مردم شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460567" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در پی حملۀ هوایی اسرائیل به محلۀ الرمال واقع در غرب شهر غزه، تاکنون یک نفر شهید و چندین تن دیگر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460566" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460565">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80db7c1466.mp4?token=jpEuxJdntwjHP7Cbxn26k-PVjJYL-Y10lwaa0eB6d1jaY2o2oN6TCg7tgyIt3L6pFpm5zbJaEY6zWLYnDvxkNcKDJZJ1rE6GCuNvh9oGTLJaNdL_AgN1THsp4Krjn4oOAGSWvj5KiLKxy6KBYugKAiL5NdUAUtgX-dI1UhzGITanchExBFxBNYolE7zxaoMLZEWGiiCz3UpU4F58iIGfjORQL8BeJbaxBWS3vCRAVCJzp9gTJUpI_ROxiqMDA1hM1OmbJxzsEjSO7XsFdlDJYdIQSsjZPf9BTZ83LInqC4tn_yPtSN6fFjReQQFyiVlfQD3Z5JYujgy_4BUjWOYKHGI3xBTRTYi5BL33S_bj6oDZ7ln3ZL0VXEhLSGc9Jmo_DdlOw4UO8AR1fC60jV5KvNftbsYZy82--XKN9x0sfH9DJkyK6kwByDhVmZxtDm1nSJM1S9-kshabTLgqVhgq8CyMkk-gyrnUKVXY8DEfeDZ_0ctlwRPXBDQvOocAeMRv-ouC8t3QBnJHwaqyhWAAfKxXQZzf19Bq2VgI4iByifA5rfIdRbc3VLOOwtxqGPvhylY_64q8VXuyKSj60KNejrFYC1bnSDPvYaTFVPWhprIHfTfKWMgplo1h4z_zjiqeNNsRWu4tDkdcKFnjdQ-_DhpdqIJL-txWaZKO7hUjPaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80db7c1466.mp4?token=jpEuxJdntwjHP7Cbxn26k-PVjJYL-Y10lwaa0eB6d1jaY2o2oN6TCg7tgyIt3L6pFpm5zbJaEY6zWLYnDvxkNcKDJZJ1rE6GCuNvh9oGTLJaNdL_AgN1THsp4Krjn4oOAGSWvj5KiLKxy6KBYugKAiL5NdUAUtgX-dI1UhzGITanchExBFxBNYolE7zxaoMLZEWGiiCz3UpU4F58iIGfjORQL8BeJbaxBWS3vCRAVCJzp9gTJUpI_ROxiqMDA1hM1OmbJxzsEjSO7XsFdlDJYdIQSsjZPf9BTZ83LInqC4tn_yPtSN6fFjReQQFyiVlfQD3Z5JYujgy_4BUjWOYKHGI3xBTRTYi5BL33S_bj6oDZ7ln3ZL0VXEhLSGc9Jmo_DdlOw4UO8AR1fC60jV5KvNftbsYZy82--XKN9x0sfH9DJkyK6kwByDhVmZxtDm1nSJM1S9-kshabTLgqVhgq8CyMkk-gyrnUKVXY8DEfeDZ_0ctlwRPXBDQvOocAeMRv-ouC8t3QBnJHwaqyhWAAfKxXQZzf19Bq2VgI4iByifA5rfIdRbc3VLOOwtxqGPvhylY_64q8VXuyKSj60KNejrFYC1bnSDPvYaTFVPWhprIHfTfKWMgplo1h4z_zjiqeNNsRWu4tDkdcKFnjdQ-_DhpdqIJL-txWaZKO7hUjPaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهید سلامی از دستیابی به تکنولوژی انهدام ناوهای هواپیمابر
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460565" target="_blank">📅 00:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460564">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9012d9a6.mp4?token=YUYCuBZvmCFntdUx0dSKYO0i_Vj8lL5VBllohJO8nS1rTTj57c-4pezTb5zF4LZZCu4XcZmiPJZv4Jys8oQQU0FxuO00aFRtr_KHNRGe5olYVYsjF6rxU9DTEx07K5xfEOL22naLL6319TrUtxXNlkrPTRjXQ9l8OS3_JH0FZwazqI2yDyfouxBz-Mt_pbZbdeG6aF07Z4nb6H8Vbx0F8vyc2qN9DymycuHhacyWEM5O2GPAPkE9kgSd8bkk4oiknpDVPi5GiMSbYrELQPcwfTBxY0oWo4RAy7-aVo8Dm6j36XJ-yIJ-QR_W7NHMATeQedcvEdV2f0dJ4f4UZLsjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9012d9a6.mp4?token=YUYCuBZvmCFntdUx0dSKYO0i_Vj8lL5VBllohJO8nS1rTTj57c-4pezTb5zF4LZZCu4XcZmiPJZv4Jys8oQQU0FxuO00aFRtr_KHNRGe5olYVYsjF6rxU9DTEx07K5xfEOL22naLL6319TrUtxXNlkrPTRjXQ9l8OS3_JH0FZwazqI2yDyfouxBz-Mt_pbZbdeG6aF07Z4nb6H8Vbx0F8vyc2qN9DymycuHhacyWEM5O2GPAPkE9kgSd8bkk4oiknpDVPi5GiMSbYrELQPcwfTBxY0oWo4RAy7-aVo8Dm6j36XJ-yIJ-QR_W7NHMATeQedcvEdV2f0dJ4f4UZLsjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا و یک رسوایی دیگر؛ تسلیحات کمپانی ریتون در حمله به عروسی سیریک  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460564" target="_blank">📅 00:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460563">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تیراندازی در آمریکا، این‌بار پس‌ از مسابقات دانشگاهی
🔹
در پی تیراندازی جمعی در ایالت کالیفرنیای آمریکا روز یکشنبه دست‌کم ۳ زن هدف گلوله قرار گرفته‌اند.
🔹
پلیس محلی اعلام کرد که در تیراندازی صبح زود در ساکرامنتو پس از یک بازی فوتبال آمریکاییِ دانشگاهی، چهار نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460563" target="_blank">📅 00:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460562">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193a0b1649.mp4?token=o2okKgC6khaIyRHhrEGvsfpbuh-q3RBxJWjd8HVkl7IQA44S9z6xxaa6RweazehPI0B3y8HbJ4Ze91idHaKe7aIXwE1PbgX8T7dV09CBa30TIFnIZ-1m3Si4ilnk9XukEuhbgLSB1uKOLQ4ZDQpN0y6Urqh-_YHnePJwhR-IyuG_Jr2Tj_qFc8U3425FrnSP9bCF56VD-CZZIzfk7UQFDEi6sfcNU6OovUZ9ze-jzsTLyDG_Sf2YU4LERzHcfCP7CEfZepLrlOMiUg6icV8JSUhB4WweHrKNL-QbdvQLVGsQ5xDVuG4s9b0bfWBEh-FD1dUe4W3WIAJ-frdJ-A8v-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193a0b1649.mp4?token=o2okKgC6khaIyRHhrEGvsfpbuh-q3RBxJWjd8HVkl7IQA44S9z6xxaa6RweazehPI0B3y8HbJ4Ze91idHaKe7aIXwE1PbgX8T7dV09CBa30TIFnIZ-1m3Si4ilnk9XukEuhbgLSB1uKOLQ4ZDQpN0y6Urqh-_YHnePJwhR-IyuG_Jr2Tj_qFc8U3425FrnSP9bCF56VD-CZZIzfk7UQFDEi6sfcNU6OovUZ9ze-jzsTLyDG_Sf2YU4LERzHcfCP7CEfZepLrlOMiUg6icV8JSUhB4WweHrKNL-QbdvQLVGsQ5xDVuG4s9b0bfWBEh-FD1dUe4W3WIAJ-frdJ-A8v-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین مدل اپن‌ای‌آی یک بدن انسان ۳بعدی ساخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460562" target="_blank">📅 23:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460561">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f79baf2e1a.mp4?token=jgXNqx2hE7jlAZZuk0uFrg6yly4PbZs6ye2LDe0xBt-if2KG59RX6H5FX90wvZlU-26WRp4vUBBR8VgQQ8xGZala7Ok5feGgsulVorCOqdX7p9i3USaTnMv72zHHuBo5ulcyhJHyFhsHhm96LhEVn37WPibwv0MohJ3PY6ZgYt8oHiDKct3cm1gXqSJR00RUyV2J1JL0pAErCLFKVvOzfoMbz0-dHDQ7-AjfaPwuudZIPFifxaQyDeIXCqGwOJ9CLf36fxTo4Q7tjchwYkyUxfE2vApA0_S2w6A0mc5Jz7HrSdqX8y4IvmJEylPO1FtZY65EWRyr_HjGrBPAj_MvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f79baf2e1a.mp4?token=jgXNqx2hE7jlAZZuk0uFrg6yly4PbZs6ye2LDe0xBt-if2KG59RX6H5FX90wvZlU-26WRp4vUBBR8VgQQ8xGZala7Ok5feGgsulVorCOqdX7p9i3USaTnMv72zHHuBo5ulcyhJHyFhsHhm96LhEVn37WPibwv0MohJ3PY6ZgYt8oHiDKct3cm1gXqSJR00RUyV2J1JL0pAErCLFKVvOzfoMbz0-dHDQ7-AjfaPwuudZIPFifxaQyDeIXCqGwOJ9CLf36fxTo4Q7tjchwYkyUxfE2vApA0_S2w6A0mc5Jz7HrSdqX8y4IvmJEylPO1FtZY65EWRyr_HjGrBPAj_MvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم گردانی مهران رجبی در تجمعات شهر قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460561" target="_blank">📅 23:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460560">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1a55c75f.mp4?token=teLAKo8vrLmWsz4QMLOU2OHbEKDqoI0qiXgLjDrso9ITZ5dEUpZnQ5ovcOzpBuaKXY7EI1Qmug8CUC28v1OupOUUZ7Lc4m5t8fxeIEVz3UHjkQPL1gpqCKQCauMFFjMjWWV6_NMgNavO9-se2jX3slcjIL2kALR__XizIwQC-PgGinuDAAV7NCwxIiUj3iJEiOpFxU3MiIP_kUbGLaLHWYTo-X0-vUr-eySKUyeY_Ip6dOZeQcn4I68ug6msOGc0M9R3HGOCX2-fpX153MG2ooDcUNDwdNJk7EJiHAVrkh5ijmXpV3LCk4u_0SUuvrhb9x0s3QBcndnKLdRbnYzhvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1a55c75f.mp4?token=teLAKo8vrLmWsz4QMLOU2OHbEKDqoI0qiXgLjDrso9ITZ5dEUpZnQ5ovcOzpBuaKXY7EI1Qmug8CUC28v1OupOUUZ7Lc4m5t8fxeIEVz3UHjkQPL1gpqCKQCauMFFjMjWWV6_NMgNavO9-se2jX3slcjIL2kALR__XizIwQC-PgGinuDAAV7NCwxIiUj3iJEiOpFxU3MiIP_kUbGLaLHWYTo-X0-vUr-eySKUyeY_Ip6dOZeQcn4I68ug6msOGc0M9R3HGOCX2-fpX153MG2ooDcUNDwdNJk7EJiHAVrkh5ijmXpV3LCk4u_0SUuvrhb9x0s3QBcndnKLdRbnYzhvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام خلج در برنامۀ سمت خدا: تفکر فرعونی، قدرت و تجهیزات را عامل پیروزی می‌داند
🔹
همان تفکری که امروز در آمریکا و رژیم صهیونیستی دیده می‌شود.
🔹
قرآن پیروزی را از آنِ اهل ایمان و تقوا می‌داند، نه صاحبان قدرت و ثروت.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460560" target="_blank">📅 23:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460559">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5362dd7c43.mp4?token=bAZHEtSFgKKCDDtQOo0PzFYlzLzew--xuImLDA38uyV4cR0nZh-eZYQrHnjfFCW3kmANRs1H9D1wXExdx8JV79eX66LNEimXSoe3kUkes0Vm_ZcdjoT8ZrvmHtGCWd7n2ltMZkV_OX1bgGhgk2pfPrM-WdWbQEXdwaC9c4MxAKUDCrf6-RoL4KdQ7v6tioth44QSp0IKSukdXu1fULT9GA7o6jubkyfqw-GnSgTUeJRPz1aYGT4dQPLzqXOQ5Bxk-IO13ivq0tOhn-6q9dxjWcA3CHQgEKI_mFlpweohWrRZSkiJ88PWQqE0UMwvByv8v3vhxpImZ077ljKfQP6dAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5362dd7c43.mp4?token=bAZHEtSFgKKCDDtQOo0PzFYlzLzew--xuImLDA38uyV4cR0nZh-eZYQrHnjfFCW3kmANRs1H9D1wXExdx8JV79eX66LNEimXSoe3kUkes0Vm_ZcdjoT8ZrvmHtGCWd7n2ltMZkV_OX1bgGhgk2pfPrM-WdWbQEXdwaC9c4MxAKUDCrf6-RoL4KdQ7v6tioth44QSp0IKSukdXu1fULT9GA7o6jubkyfqw-GnSgTUeJRPz1aYGT4dQPLzqXOQ5Bxk-IO13ivq0tOhn-6q9dxjWcA3CHQgEKI_mFlpweohWrRZSkiJ88PWQqE0UMwvByv8v3vhxpImZ077ljKfQP6dAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا این فناوری را از ترس ایران خاموش کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460559" target="_blank">📅 23:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460558">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
لحظۀ انهدام جلسۀ فرماندهی مزدوران وابسته به سعودی توسط موشک بالستیک یمنی  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460558" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460557">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb6cdf6f4.mp4?token=gsx7_TSW79RK5ZsEWhMqZwk-4z2pGX2hL23TfQa0bmH-7p9fawAVWvjsPJTNhHFTJ_fFZgumvEcv5afi6eCEx-wnkdiZ3GeGEiVmQjzFC2wn5RD7toE-HPGQ60QAgssRfuCKk67sowoJa3_iMFvlF-Btzl3dRJcemROh-aBgs1hgSBbwc4icoOvsC2FlszoeSl-VgP6Ro6lLm_Od0DK_1x6mU7HiId9N2gVngI2TectBdpPp49hU9hJfpgIsqrUM7LTGLNgfiX-nv3bbTKl2Ly_xAqSF_PIt36YLBtegP6F8DzlCgnxP5-Fqi2A9rNMVXJ2f3jirKOyZDN7A2NR6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb6cdf6f4.mp4?token=gsx7_TSW79RK5ZsEWhMqZwk-4z2pGX2hL23TfQa0bmH-7p9fawAVWvjsPJTNhHFTJ_fFZgumvEcv5afi6eCEx-wnkdiZ3GeGEiVmQjzFC2wn5RD7toE-HPGQ60QAgssRfuCKk67sowoJa3_iMFvlF-Btzl3dRJcemROh-aBgs1hgSBbwc4icoOvsC2FlszoeSl-VgP6Ro6lLm_Od0DK_1x6mU7HiId9N2gVngI2TectBdpPp49hU9hJfpgIsqrUM7LTGLNgfiX-nv3bbTKl2Ly_xAqSF_PIt36YLBtegP6F8DzlCgnxP5-Fqi2A9rNMVXJ2f3jirKOyZDN7A2NR6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: در بنزین ما متانول نیست
🔹
در دنیا استفاده از متاننول در بنزین گسترده است و تا ۳ درصد هم استاندارد است اما ما استفاده نمی‌کنیم.
🔹
تنها در یکی از پالایشگاه‌ها به‌صورت آزمایشی از ۰.۵ درصد متانول استفاده شده بود. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460557" target="_blank">📅 23:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460556">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/he1-b2UmHLkXOLK0MqE1hGIVRoCJNq-tApMywGbcw62-0AYFA3eE0F-TenLbIO_MEH_h_WHRqzXhQF6ennRqKfbK1OWSfTuiAFhzKgFF2R5By0OItTbGdgtKikB6D-Zy9h4nqrbcauejt-bV9qgrwVAifzz-GVkRT3pp-Du-kuRFrSUYluOuM1ZT9myUF6PbNEsksKIr3ZzM6LDLkaS5KkHVT75Jzit9wGBad2nf-Dw7bXPc0BffFn799I1Hsf2DnRP-N8dB1HLreddplpBLozPpqU7Oo17BaQsEgEduC1gvubbQtqVhugUpgJbRzbw90Rih3l-cG1lvXAB_tsqZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ شهید طی درگیری با اشرار در کورین زاهدان
🔹
یک منبع آگاه در زاهدان: در جریان درگیری امروز با اشرار مسلح در کورین از توابع زاهدان ۲ بسیجی به نام‌های کیوان رامرودی و ابوالفضل عودی به شهادت رسیدند.
📝
اخبار تکمیلی متعاقبا اعلام میگردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460556" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460554">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686281167c.mp4?token=ANfpr_kvuIr1TYDLOKFUn3TlfWGCdN9T5Y4PsmS2X7694trV_NMKBN0_MjUEj1A-J_kFI2qY48UqR6Gx_Tj2-MJKULpkH2Pn-1xoCHsVb9dBOOl0HMXYdfDXnHLugurZyINfmeElbBN5Nyu3OBQoVLxofLeZKA2ai__u5LOfmlcMr8bKoSbhOcWNndtS50jqL4ZghGrft8X70c8R_XuRbWEcqCo-ry4Z2YjEtukyrCy5jmM2uvfL9VZ1F74Ndt9EEE7xOONm42smv0ZDO3lUy_on8kSq45w15lYrYD0xW-rh9F-O6kpN1VJUIxU2Rzpf5f2hYglp53OoG2dylHiM9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686281167c.mp4?token=ANfpr_kvuIr1TYDLOKFUn3TlfWGCdN9T5Y4PsmS2X7694trV_NMKBN0_MjUEj1A-J_kFI2qY48UqR6Gx_Tj2-MJKULpkH2Pn-1xoCHsVb9dBOOl0HMXYdfDXnHLugurZyINfmeElbBN5Nyu3OBQoVLxofLeZKA2ai__u5LOfmlcMr8bKoSbhOcWNndtS50jqL4ZghGrft8X70c8R_XuRbWEcqCo-ry4Z2YjEtukyrCy5jmM2uvfL9VZ1F74Ndt9EEE7xOONm42smv0ZDO3lUy_on8kSq45w15lYrYD0xW-rh9F-O6kpN1VJUIxU2Rzpf5f2hYglp53OoG2dylHiM9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: کارت آزاد جایگاه شناسه‌دار می‌شود
🔹
در این طرح که در آینده اجرا خواهد شد هر نفر که با کارت جایگاه بنزین بزند با کارت بانکی احراز هویت می‌شود.
🔹
این طرح به‌صورت آزمایشی در چند جایگاه تهران درحال اجراست و احتمالا تا اواخر مهر در تمام کشور اجرا…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/460554" target="_blank">📅 23:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460553">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02b05b065.mp4?token=PAib0dHBZ2j_yjx_X9hAt-SIt59BPLi2rKa3l1ulFtelkPk7MYTcRiifGy3Iqt6XV_k3mvrfN-JKEYX_8JpyIBxqsdvgh8pCsE_YZZNes37g9NNEqATSHHuHqrA5Tt2ca3RZyulU5lnGXN0SbcuFgbaojbYZyBY5eZGNuLiD8tcVGALUMrqTLT66Swh84hnc46v1O6kae5UUM-8j6KJkS1mphqI94CZTXU6FWve4hwdHbic64Qx3HpDVVk0IC2R0VvftduGc0U3aj7_3hVtCo-17j-7sZ6e5XSOf1Hzp8bhG5QqfkYolZwShkD4yhwZqGDXExDkSorYRudLCYDkyDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02b05b065.mp4?token=PAib0dHBZ2j_yjx_X9hAt-SIt59BPLi2rKa3l1ulFtelkPk7MYTcRiifGy3Iqt6XV_k3mvrfN-JKEYX_8JpyIBxqsdvgh8pCsE_YZZNes37g9NNEqATSHHuHqrA5Tt2ca3RZyulU5lnGXN0SbcuFgbaojbYZyBY5eZGNuLiD8tcVGALUMrqTLT66Swh84hnc46v1O6kae5UUM-8j6KJkS1mphqI94CZTXU6FWve4hwdHbic64Qx3HpDVVk0IC2R0VvftduGc0U3aj7_3hVtCo-17j-7sZ6e5XSOf1Hzp8bhG5QqfkYolZwShkD4yhwZqGDXExDkSorYRudLCYDkyDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سانحهٔ هوایی در آمریکا؛ ستون عظیم دود در آسمان میامی
🔹
پلیس و واحدهای آتش‌نشانی میامی پس از سقوط یک هواپیمای ۷۶۷ پرایم ایر در فرودگاه بین‌المللی میامی به منطقه اعزام شده‌اند.
🔹
گزارش‌ها حاکی از آن است که این هواپیمای باری امروز بعدازظهر به وقت محلی از باند فرودگاه بین‌المللی میامی (MIA) خارج شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/460553" target="_blank">📅 23:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460552">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed1c55e0c.mp4?token=bG_Nbc8LjkYCg3oR0flLCDJONTacA6BRZI0KSN8CCXXccsMBULTMMeSGnm-PK1oxdF63JyoujFJ6YnJwIfhpjHSKE0w6npnmOabSo1hePOoWQ4oBrH_6G57PK_DZIoEznZlRUobfrlNpa7U6Vmf5G2DjtZ9kvHQmgdwEVfU9A6uAXB_1iRq4MzL00IU1sXGLUY1AQ9clzbvaEVe9XNTySWU85k7E0i2-sMnSRJS3F3RLasKeR20InN8OlmDu3SKR0aPNFCw-NcPcKghUkUZFjAQ0r0ERmSNzW7tnuxRMesDSeWCZWHIOULwDbOciLsXJHaqfTSbUFw1ED46W_TF53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed1c55e0c.mp4?token=bG_Nbc8LjkYCg3oR0flLCDJONTacA6BRZI0KSN8CCXXccsMBULTMMeSGnm-PK1oxdF63JyoujFJ6YnJwIfhpjHSKE0w6npnmOabSo1hePOoWQ4oBrH_6G57PK_DZIoEznZlRUobfrlNpa7U6Vmf5G2DjtZ9kvHQmgdwEVfU9A6uAXB_1iRq4MzL00IU1sXGLUY1AQ9clzbvaEVe9XNTySWU85k7E0i2-sMnSRJS3F3RLasKeR20InN8OlmDu3SKR0aPNFCw-NcPcKghUkUZFjAQ0r0ERmSNzW7tnuxRMesDSeWCZWHIOULwDbOciLsXJHaqfTSbUFw1ED46W_TF53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: با جمع‌آوری کارت‌های جایگاه در کرمان مصرف سوخت‌های جایگزین مثل سی‌ان‌جی ۳۰ درصد افزایش پیدا کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460552" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460551">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af729e4ee.mp4?token=dCOz_PCmOBiXPXwcUvgH5cTtJWVOAT5hbVhPQelMJs53vm5f9IwZ0TtiSHeDlVhkXapuIHEydQIXIIvOjIORrxkYhxuC1MVKunJRd2i7Bg_Z1gInEFjwQkhWAYJt3b_NDaGwie8_xQVX2V4Buz9p4Q1v-JDABgXg8gCWyIg-s6-rRLFENakSz1LNv3FlKRIiLy5q_uFaOARuMVLVwlMjjMGRwwUYBBx5XkfKzsURDpiLKtN-O5tGDn0FQdcEQK7J6B_m7KKpYyadwFWWr9guNSyw9i9_8kNh7QgGtbB4TQlYw1zbq_A1OVfqL0ECexdVlcJ5PwgrIHHdURuC0veDCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af729e4ee.mp4?token=dCOz_PCmOBiXPXwcUvgH5cTtJWVOAT5hbVhPQelMJs53vm5f9IwZ0TtiSHeDlVhkXapuIHEydQIXIIvOjIORrxkYhxuC1MVKunJRd2i7Bg_Z1gInEFjwQkhWAYJt3b_NDaGwie8_xQVX2V4Buz9p4Q1v-JDABgXg8gCWyIg-s6-rRLFENakSz1LNv3FlKRIiLy5q_uFaOARuMVLVwlMjjMGRwwUYBBx5XkfKzsURDpiLKtN-O5tGDn0FQdcEQK7J6B_m7KKpYyadwFWWr9guNSyw9i9_8kNh7QgGtbB4TQlYw1zbq_A1OVfqL0ECexdVlcJ5PwgrIHHdURuC0veDCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: قرار است یک روز در هفته مدیران دولتی ملزم به استفاده‌نکردن از خودرو بشوند  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460551" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407cfd0892.mp4?token=uWQ8e0k9pUGM1AntTlT1W_j7t7N09nLzYUU_UHwEWGF9_vi1wQNTGGTwf9Th7jbvFc9Ovn0jQe5ewvLrBOZHU9loqade88j123V3tkXmwGpaGXARnrp79tf8277eHHLHv-rdbSGM6n3Bs9WuXrI8Yp4eg2CvFYn_-MJxl6zWTt4TTlVG-CxuHiVzZATsB0Cm2HMJn4Ltmzm45ql2Ov4-Y1kA-HBDmyJ4-kWpOpCWhjO1MQjsV4oqagHV_nbfUWTXzxBdlIbb5wo6U2TZ9FjxCttCFq285ehFGqiDAslRBv3accC32JN9xb4NQFV0i61BYZzxId52bVN42bitvtcbCVnR-hbvKdyRjbfWPrc9OSu3JebJAh89kFL3PZ0oCVTIxTVq-8yMaLrsQla0xdPixSm7huIQyECXMEes9X2HxFr0-Q0YGWCJOVQRVgJLQcJN9Jk-0ugyICBITbc7r4bPvCqUsrjipc0Z9TsX1XjuNe7AdzR-ko-bILsoPzVBjoFuuLV-soISOqwfT5froEUF7i635qLKcCqJjIHJu-r7Ya0SpjPHSJ7thSP4X8irdCHkCsKiYZDggM3N-hLmRJv_OfOMVmv-qO2xDOHAnCQPzFN_wgyZwRIPlig7Vf3jK2QNzLN48duxVmYy0eVUlWz0uMQ8GCuGwoQKGoNmd4ptWec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407cfd0892.mp4?token=uWQ8e0k9pUGM1AntTlT1W_j7t7N09nLzYUU_UHwEWGF9_vi1wQNTGGTwf9Th7jbvFc9Ovn0jQe5ewvLrBOZHU9loqade88j123V3tkXmwGpaGXARnrp79tf8277eHHLHv-rdbSGM6n3Bs9WuXrI8Yp4eg2CvFYn_-MJxl6zWTt4TTlVG-CxuHiVzZATsB0Cm2HMJn4Ltmzm45ql2Ov4-Y1kA-HBDmyJ4-kWpOpCWhjO1MQjsV4oqagHV_nbfUWTXzxBdlIbb5wo6U2TZ9FjxCttCFq285ehFGqiDAslRBv3accC32JN9xb4NQFV0i61BYZzxId52bVN42bitvtcbCVnR-hbvKdyRjbfWPrc9OSu3JebJAh89kFL3PZ0oCVTIxTVq-8yMaLrsQla0xdPixSm7huIQyECXMEes9X2HxFr0-Q0YGWCJOVQRVgJLQcJN9Jk-0ugyICBITbc7r4bPvCqUsrjipc0Z9TsX1XjuNe7AdzR-ko-bILsoPzVBjoFuuLV-soISOqwfT5froEUF7i635qLKcCqJjIHJu-r7Ya0SpjPHSJ7thSP4X8irdCHkCsKiYZDggM3N-hLmRJv_OfOMVmv-qO2xDOHAnCQPzFN_wgyZwRIPlig7Vf3jK2QNzLN48duxVmYy0eVUlWz0uMQ8GCuGwoQKGoNmd4ptWec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: تاکسی‌های اینترنتی از تبعات افزایش نرخ بنزین مصون می‌مانند
🔸
قرار است با دوگانه‌سوز کردن ناوگان و اختصاص سهمیه مازاد مبتنی بر پیمایش، از افزایش هزینه و کرایهٔ تاکسی‌های اینترنتی جلوگیری شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460550" target="_blank">📅 23:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879f852b1a.mp4?token=b3Or5CCTRbKaDlfCjH5qomdCVeoykk6pWgq4NupxJNnX3UktlV2owGmPFh4ePwR9x5Rk_RlFs_WlCmHi6VpjTB91tJyDid3nQrvWGCuOACXN6taQlF29feZKt0WX-3H8r-U-HayCs-Y4VmtI87GymPoAQqEO-s58eUIc53SQuzIrrJsJfmzqpJ-uMXnqmJjZPhiEEnP7rT-Wd4mwMTjodvZmOS3Bz7ZJtHMu8lm9mFdUIGVAnUzhZAySdyBjIL7uNtmbnAr6iWLkHBoe0rUETaqRLl5RoUfm7cBqUgrZqFKp7QMScxkIMIxDVhfyJiDhFf4HNXN-VShky8Fzt2BLqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879f852b1a.mp4?token=b3Or5CCTRbKaDlfCjH5qomdCVeoykk6pWgq4NupxJNnX3UktlV2owGmPFh4ePwR9x5Rk_RlFs_WlCmHi6VpjTB91tJyDid3nQrvWGCuOACXN6taQlF29feZKt0WX-3H8r-U-HayCs-Y4VmtI87GymPoAQqEO-s58eUIc53SQuzIrrJsJfmzqpJ-uMXnqmJjZPhiEEnP7rT-Wd4mwMTjodvZmOS3Bz7ZJtHMu8lm9mFdUIGVAnUzhZAySdyBjIL7uNtmbnAr6iWLkHBoe0rUETaqRLl5RoUfm7cBqUgrZqFKp7QMScxkIMIxDVhfyJiDhFf4HNXN-VShky8Fzt2BLqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: توانستیم با برخی تدابیر ۵ درصد افزایش تولید بنزین داشته باشیم  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460549" target="_blank">📅 23:07 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
