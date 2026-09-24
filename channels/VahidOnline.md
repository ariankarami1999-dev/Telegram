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
<img src="https://cdn1.telesco.pe/file/aAIPYp73_FmxNCdL4iYnWczLMmmqUyYG4GL0pNPJOHhTSYQkE90gNKkltN5gIt80WGGY9ssyfr-uEj4sYlBKxA07b6MUJKXXWNkucjNorlV_M-lOnoWH6FUAdvBI72pJ4FXCrgAvU4QX82CIBcS7o_KHPeLAtUOO5kFL7omSwKxj6riwbHGjiau5z7Q3rm9aj_InGdYXD6BQ13CA1sJZ06KceHluzViLX2qNf5jF1qYFneJBl3y9l_Fa_vjKD5kJrAku_gVf-jQ-tz9AnseYNz6boUEaaM9t-BUkqrW1eF7k_y9YRKspkbSs-_5iKkfRs1DWfjW-5J9cyAKydZ72aA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 09:10:22</div>
<hr>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۰۰:۱۳
انفجار شدید بندرعباس
همین الان بندرعباس موج انفجار حس شد
وحید قشم لرزید
انفجار دریا بود
00:24  بندرعباس، صدای خفیف انفجار از دور
سلام حدود ساعت ۱۲ یه موج شدید پنجره های ما رو تو بندرعباس لرزوند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78505" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rWtU70fU6RaLLnKfZ-7xssrWCaTM8IBpUVCkFzRFeTzG5uiRVVCJZluR9-Sa0dygAoFb-G9ViCFXR1Q57nAw41KmJKvanbFBRcR4Ia4-fuZgKaBNOxXYfhrw8-qSTiNUyTx6v_uXhamOtabQ9IHdFJ5ILiUNU4TLE6m4d8IKOdJwj1SqG_SRReD7NpqIP0ZXIRvbbh49GrgiBcWTnCnZ6v1Me85-LUrTJcMY1TmOwygcz03QEAaIevkMiUWD_3rX7HCvYWlIY9cXfX5Alm17vmjDrwTjO9F50fOA9THGSpufZlRfEruF2C1i8EJPCe9-uTtJekAz22loNt9NWg8D5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه پاسداران، از کشته‌شدن سرتیپ حسین ظریفی، فرمانده عملیاتی قرارگاه سجاد شهرستان سراوان، در جریان یک درگیری مسلحانه در این منطقه خبر داد.
روابط عمومی سپاه، روز اول مهر ۱۴۰۵، در بیانیه خود نوشت ظریفی در جریان «آخرین عملیات رزمندگان این قرارگاه در منطقه سراوان» کشته شده است.
همزمان، حال‌وش گزارش داده است که احمد هراتی زراعتی، مسوول اطلاعات قرارگاه عملیاتی سجاد سراوان، نیز در جریان درگیری نیروهای نظامی با افراد مسلح در منطقه جهاد آباد سراوان کشته شده است.
بر اساس گزارش حال‌وش، این درگیری روز چهارشنبه یکم مهر رخ داده و دست‌کم ۱۳ نیروی نظامی و امنیتی دیگر نیز در جریان آن به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78504" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/813923332b.mp4?token=itYYTc0nG4o56iSELqqKl0ugKR6oozezOa7ixVM21kxi0ro2SVfI-vxrowpbVzvcyhReUB7AAtRIn9wC8TD7VcwnNKt7zUc3iC7UWx_3Gv5SrZDZA86dquas2seVurBaHB2N4W8hTEu4XaPUxeG2toUFOntTN9BzxJnnHLz1yMma1PzjEB0YVlFiZJWdvCQLX-UvHaSEyTbTdazpmxx3F5Ma1IfVpCLObAcMtuT98K5z8i0POrtuQFHFNOpfoKH0ckkatKeJDRicmpTUNzEUh78vilzNUiAGro3scWNK15lD-AC7ocu3oq7rTHlCrO-dr9oxVct-p-dK4YtBYbym8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/813923332b.mp4?token=itYYTc0nG4o56iSELqqKl0ugKR6oozezOa7ixVM21kxi0ro2SVfI-vxrowpbVzvcyhReUB7AAtRIn9wC8TD7VcwnNKt7zUc3iC7UWx_3Gv5SrZDZA86dquas2seVurBaHB2N4W8hTEu4XaPUxeG2toUFOntTN9BzxJnnHLz1yMma1PzjEB0YVlFiZJWdvCQLX-UvHaSEyTbTdazpmxx3F5Ma1IfVpCLObAcMtuT98K5z8i0POrtuQFHFNOpfoKH0ckkatKeJDRicmpTUNzEUh78vilzNUiAGro3scWNK15lD-AC7ocu3oq7rTHlCrO-dr9oxVct-p-dK4YtBYbym8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز چهارشنبه، اول مهرماه، در حاشیه نشست‌های مجمع عمومی سازمان ملل متحد در نیویورک، از ادامه رایزنی‌ها با میانجی‌گران درباره ایران خبر داد و جلوگیری از دستیابی تهران به سلاح هسته‌ای را مهم‌ترین موضوع در هرگونه توافق احتمالی دانست.
به گفته روبیو، دونالد ترامپ همچنان برای دستیابی به توافق با ایران آمادگی دارد، اما چنین توافقی نیازمند مذاکرات دشوار و فشرده با مشارکت میانجی‌گران خواهد بود.
وزیر خارجه آمریکا همچنین با اشاره به تنگه هرمز، از ادامه عبور نفتکش‌ها از مسیر جنوبی خبر داد و حفاظت از کشتی‌رانی و باز نگه داشتن تنگه را از ماموریت‌های ارتش آمریکا عنوان کرد.
روبیو درباره جزئیات رایزنی‌های دیپلماتیک توضیح بیشتری نداد و تاکید کرد: «اگر قرار باشد توافقی حاصل شود، این اتفاق در یک نشست خبری رخ نخواهد داد.»
@
VahidOOnLine
روبیو در واکنش به سخنان مسعود پزشکیان که ایالات متحده را به نقض قوانین بین‌المللی متهم کرده بود، به شدت از تهران انتقاد کرد.
روبیو با اشاره به کشته شدن هزاران نفر از مردم در تظاهرات، حمایت مالی از گروه‌های تروریستی برای حمله به همسایگان و تاسیسات انرژی، و سرپیچی از قطعنامه‌های هسته‌ای تاکید کرد که جمهوری اسلامی ایران بزرگ‌ترین ناقض نظام بین‌المللی در جهان است.
او تصریح کرد: «نمی‌دانم ایران چه حقی دارد که به کسی درباره حقوق بشر یا نظام بین‌المللی موعظه کند، در حالی که خود به طور مداوم آن را نقض می‌کند.» وزیر خارجه آمریکا افزود که حکومت ایران با قتل‌عام مردم خود، نقض حاکمیت کشورهای همسایه و بی‌اعتنایی به قوانین جامعه جهانی، صلاحیت اظهارنظر در این زمینه را ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78503" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=kUHUDvLlbGYtYZZXQ1878zCr6yKmMdw69MoOmjRz8gvEghrL1Bq5tGHGXumNZwGvO0y6VR7Y_-25MEUvbcmW5-Gn74wE9f_B07Ru88BRbqF-UB5B103TnbElnfPOktzxPSjXcAMQmuk2wgOKSheFoWeHSw1yoWFoRTj-p5EKri0tkiRj_PY95WkEM2SGBSnnJA9hK_juo1_zXDhxn62XQY5Yn7BROlQuDQM0uxSAnjCO2o56eVoB2b3Dl3F9Hfl2oJYyN9JMgCjygrXWIpI2GbjQDXXXLlrhIkgQiQBjo1d7X9sUTadOG7AmNXe2k_8FVTG1VBz4WqGHlftC1iew5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=kUHUDvLlbGYtYZZXQ1878zCr6yKmMdw69MoOmjRz8gvEghrL1Bq5tGHGXumNZwGvO0y6VR7Y_-25MEUvbcmW5-Gn74wE9f_B07Ru88BRbqF-UB5B103TnbElnfPOktzxPSjXcAMQmuk2wgOKSheFoWeHSw1yoWFoRTj-p5EKri0tkiRj_PY95WkEM2SGBSnnJA9hK_juo1_zXDhxn62XQY5Yn7BROlQuDQM0uxSAnjCO2o56eVoB2b3Dl3F9Hfl2oJYyN9JMgCjygrXWIpI2GbjQDXXXLlrhIkgQiQBjo1d7X9sUTadOG7AmNXe2k_8FVTG1VBz4WqGHlftC1iew5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: اگر کشورهای همسایه پروازهایمان را ممنوع کنند، پروازهای آنها نیز متوقف خواهد شد
محسن رضایی، دبیر شورای‌عالی امنیت ملی جمهوری اسلامی، کشورهای همسایه ایران را در واکنش به محدودیت‌های اعمال‌شده علیه پروازهای ایرانی تهدید کرد و گفت اگر این کشورها پروازهای ایران را ممنوع کنند و وارد همکاری با آمریکا شوند، پروازهای فرودگاه‌های آنها نیز متوقف خواهد شد.
رضایی گفت: «اگر کنار آمریکا باشید، ما شما را تماشا نخواهیم کرد» و هشدار داد در صورت ممنوعیت پروازهای ایران و همکاری کشورهای همسایه با آمریکا، «فرودگاه‌هایتان پرواز نخواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78502" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پزشکیان: از مذاکره برای صلح نمی‌گریزیم
مسعود پزشکیان، رییس دولت در جمهوری اسلامی، چهارشنبه اول مهر در سخنرانی خود در هشتاد و یکمین مجمع عمومی سازمان ملل متحد گفت متن سخنرانی‌اش را از پیش آماده کرده بود، اما پس از سخنان دونالد ترامپ، رییس‌جمهوری آمریکا، و «تروریست» خواندن جمهوری اسلامی، تصمیم گرفت عکس علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، و دانش‌آموزان مدرسه میناب را به حاضران نشان دهد.
پزشکیان همچنین گفت: «هر کسی را که می‌خواهند تخریب کنند، نام تروریست بر آن می‌گذارند. ۲۰۰ سال است که ایران به کشوری حمله نکرده و فقط از خود دفاع کرده، اما ما را عامل ناامنی می‌خوانند.»
او در بخش دیگری از سخنانش گفت: «آمریکا و اسرائیل با آخرین تجهیزات به ما حمله کردند و ما با قدرت دفاع کردیم.»
پزشکیان گفت آمریکا و اسرائیل جنگ را به ایران تحمیل کردند، اما جمهوری اسلامی «با قدرت» دفاع کرد و در عین حال «برای صلح از مذاکره نمی‌گریزد».
او درباره برنامه هسته‌ای جمهوری اسلامی گفت: «برای دفاع از کشورمان از هیچ‌کسی اجازه نمی‌گیریم. ایران نمی‌پذیرد که دانش هسته‌ای در انحصار چند کشور باشد؛ سلاح هسته‌ای را عامل امنیت نمی‌دانیم.»
پزشکیان در ادامه درباره تنگه هرمز گفت: «نمی‌شود همه از تنگه هرمز بهره ببرند و راه کشتیرانی بر ایران بسته شود. استقرار ناوگان‌های متخاصم و گسترش جنگ باعث امنیت کشتیرانی نمی‌شود.»
او درباره شرایط منطقه نیز گفت: «در منطقه‌ای زندگی می‌کنیم که جنگ مرز نمی‌شناسد و بحران یک کشور به همسایگان سرایت می‌کند. از این رو همسایگان خود را قوی می‌دانیم.»
@
VahidOnLive
پزشکیان: یا امنیت را با هم می‌سازیم یا ناامنی را با هم تحمل می‌کنیم
مسعود پزشکیان در مجمع عمومی سازمان ملل گفت: «صلحی که برای همه نباشد، صلح نیست. یا امنیت را با هم خواهیم ساخت یا ناامنی را با یکدیگر تحمل خواهیم کرد. ما آماده گفت‌وگو هستیم، اما زبان زور را نخواهیم پذیرفت.»
او افزود: «سخنان ترامپ نزد افکار عمومی جهان و اندیشمندان، نشانه بارزی از خوی قلدری و منطق زور و مغایر با منشور صریح سازمان ملل است.»
پزشکیان گفت: «ترامپ بداند که این سخنان ملت ما را منسجم‌تر می‌کند و باید بداند که ملت ما در برابر زور سر خم نکرده و متجاوزان را پشیمان خواهد کرد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78501" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78499">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NgtwKCzxgmnUsT2pA3ZB9_iO5PhBz62YcT7sa9CmP9eQTKMPI6xXxdArQ4BGZqzcWv8pJkaDCs5IIO2MeVd_b7Bw4A96amLhkHc2-MLAKrWdYsDG6UH1TgtdTl7Dh867w0xt7L7Jju6nQKVvBq7dUhqg9egNvZdQRLYhVWo2F3D1r3IifKtrKfiYqsFrUe6SzK-Ca9LV0SBp4WT9Pubg2-hfpJc6QhnL4elRyVfEC7eB8jidFOYk__K-hKqDQnn8xkPS252UMp6BpuoRbVO0GAq0ChiRZ7RbvWs0A_PtmiiNgXjuXQAIq1-oeR7fmYOqa23idR3VWb8VM9rdB-ts9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/612763335d.mp4?token=PpJifZ904L7V3FsShPXRqtNsGK2KjhND-5vjkteZky1iezpwpXxiBG7XYAOa3L52lN4xd0trdfIXeS5O0SoD-OQ4qZwQUixVOiynvQud2GbBCpsaU71JZjy_wy8RbmZES5uz4gp7Ry2QxZCGs7Opdv--MpOWxtBiuo9gh6guiillHKGGn0DYvxMh-BkIO22rDwGiOG0KrOCBe_du-xTJNpleiRFlYbQdruxSQc6CerJTCt_yN0aH0hw4vXMhgggH35vps3H3_CHEp9fl9WZuo8jdCNo3-eX4XxQuep4XLSZQ8ZeR88UQ80BpJJ_FRD-RDZhZzhtzZIGxouOlPjKV6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/612763335d.mp4?token=PpJifZ904L7V3FsShPXRqtNsGK2KjhND-5vjkteZky1iezpwpXxiBG7XYAOa3L52lN4xd0trdfIXeS5O0SoD-OQ4qZwQUixVOiynvQud2GbBCpsaU71JZjy_wy8RbmZES5uz4gp7Ry2QxZCGs7Opdv--MpOWxtBiuo9gh6guiillHKGGn0DYvxMh-BkIO22rDwGiOG0KrOCBe_du-xTJNpleiRFlYbQdruxSQc6CerJTCt_yN0aH0hw4vXMhgggH35vps3H3_CHEp9fl9WZuo8jdCNo3-eX4XxQuep4XLSZQ8ZeR88UQ80BpJJ_FRD-RDZhZzhtzZIGxouOlPjKV6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک کشتی باری چهارشنبه یکم مهر در تنگه هرمز با یک پرتابه ناشناس هدف قرار گرفته و پس از آن دچار آتش‌سوزی شده است.
بر اساس این گزارش، همه خدمه کشتی تخلیه شده‌اند و در این حادثه دو نفر آسیب دیده‌اند.
@
VahidOOnLine
کشتی که امروز در تنگه هرمز، هدف حمله سپاه پاسداران قرار گرفت یک کشتی فله بر هندی با نام Cape Dao بوده است. در نتیجه حمله، یک نفر کشته و یک نفر زخمی شده است و کشتی تخلیه شده و در حال سوختن است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78499" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO8EB3xbWk-LRrYRHqbNti7pIpZILxUXAx1E6IpE87sUv8AvwW6QsCR_HXwx8Di2F58inBK_wNuqo_um52lx-PFWrke3oa3J3QI2IqwIDFTIUAtwqwxyOFkQi1oNq1tmejzsH6yiPFsoJoZC-5astd2BlH1R_a-uPrgkIFw5CpBXOnLvYsnd6jTxnRKovp-Z8J3vNZFHzPFF8hjKIeGm2I5JMBTW-tjMlBBlpo3WnRuJ4zCu-u84PHCQhXymp87jwd_4Phsy1WAM6dgy_D2QgYFtvYC578o-4INbVK0uOv_gR3VveieaBpaCUsu0mHFK_haUVRXB4p85rKY43-d-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تشدید فشار و آزار شهروندان بهایی در ایران، یک شهروند بهایی به نام رومینا گلی، از سوی دادگاه انقلاب ساری به زندان و محرومیت از حقوق اجتماعی محکوم شد.
بر اساس گزارش رسیده، شعبه دوم دادگاه انقلاب ساری، رومینا گلی را بابت اتهام «فعالیت آموزشی یا تبلیغی انحرافی مغایر یا مخل به شرع اسلام»، موضوع ماده ۵۰۰ مکرر قانون مجازات اسلامی، به پنج سال حبس و ۱۰ سال محرومیت از حقوق اجتماعی محکوم کرده است.
این شهروند بهایی همچنین بابت اتهام «تبلیغ علیه نظام»، طبق ماده ۵۰۰ قانون مجازات اسلامی، به هفت ماه و ۱۶ روز حبس محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78498" target="_blank">📅 18:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=PSHm5jR5DNo3qM_GgIbGz7n2EDL_u8htyeBbiYr8Dq4G4x4cay-0zWXNZtDLsB9XJAvPC7DD-Yq2L0c1ibyrVAVPIUKSJ5QIqTHy_9-Lf0djzDcz7b2Yad0moFfRQCGPGwKvh89PL_-GXDSRvhUUaLFP_bWDMogWb2ZvZ4oq9OiYIJIG-TW6Ni4U3pAMjoQ72Jkz4ti39eVSvHEiIheO0YqdU3cCbAA7MDTKz5k0o9SsKzjkGZorFg8DynByEToMTfN781xzMh8MbgMgY1e__Q1qQ_H8lj1oQTwvPdHGHB_m6EeHx7aFmC4sdxNon2XCd18iiAsJNrHDS2uoNRLnxj4NumJEg_YtKuriOcs-JlZaM_9gTnv1032pUS9vhhZ_4f_l-Rm4ulD6fD188-Bte1TLWrGAgoBN4KFLe0EYZD0Id6ZJa2R9ts7dx8NhMEudYeFwil2hSEVWx5tn3kqsS1lPYWtk8MbOBbTsWFDlLniWp_5UXNOoGU5KM5TpmpS2kgDkyw3nUcb_gXgYALjuec9AkOP6WZc4lfQ0pxUxKU71NsFnLFlj01ou5TbGXBJYMfiLxYjXIzMmhqScU18YuCWyDe9v8Mac-76h-at84E49i0Q1c3XmVVPz8SOSx6FHWM6NJXwbKWR2dlsnK1vhI3Gt40KZorMi8Q7BUML8kGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=PSHm5jR5DNo3qM_GgIbGz7n2EDL_u8htyeBbiYr8Dq4G4x4cay-0zWXNZtDLsB9XJAvPC7DD-Yq2L0c1ibyrVAVPIUKSJ5QIqTHy_9-Lf0djzDcz7b2Yad0moFfRQCGPGwKvh89PL_-GXDSRvhUUaLFP_bWDMogWb2ZvZ4oq9OiYIJIG-TW6Ni4U3pAMjoQ72Jkz4ti39eVSvHEiIheO0YqdU3cCbAA7MDTKz5k0o9SsKzjkGZorFg8DynByEToMTfN781xzMh8MbgMgY1e__Q1qQ_H8lj1oQTwvPdHGHB_m6EeHx7aFmC4sdxNon2XCd18iiAsJNrHDS2uoNRLnxj4NumJEg_YtKuriOcs-JlZaM_9gTnv1032pUS9vhhZ_4f_l-Rm4ulD6fD188-Bte1TLWrGAgoBN4KFLe0EYZD0Id6ZJa2R9ts7dx8NhMEudYeFwil2hSEVWx5tn3kqsS1lPYWtk8MbOBbTsWFDlLniWp_5UXNOoGU5KM5TpmpS2kgDkyw3nUcb_gXgYALjuec9AkOP6WZc4lfQ0pxUxKU71NsFnLFlj01ou5TbGXBJYMfiLxYjXIzMmhqScU18YuCWyDe9v8Mac-76h-at84E49i0Q1c3XmVVPz8SOSx6FHWM6NJXwbKWR2dlsnK1vhI3Gt40KZorMi8Q7BUML8kGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در جریان دیدار با رهبران و نمایندگان کشورهای عربی خلیج فارس، ترکیه،‌ اردن، سوریه، مصر و لبنان، ترجمه ماشین:
فقط می‌خواهم این را اعلام کنم که استیو و جرد امروز جلسه‌ای بسیار سازنده با میانجی‌های ایران داشتند؛ عمدتاً میانجی‌ها. ببینیم چه پیش می‌آید. آنها مدتی است که میانجی‌گری می‌کنند، اما فکر می‌کنم شتاب زیادی برای رسیدن به توافق وجود دارد. این چیزی است که از همه می‌شنویم.
و سخنرانی مرا هم شنیدید. لازم نیست دوباره مرورش کنم، اما ما ضربه سختی به آنها زدیم. قصد فخرفروشی نداریم، اما اقتصادشان واقعاً در وضعیت بسیار بدی است و امیدوارم کاری بکنند که واقعاً به نفع مردمشان باشد. و فکر می‌کنم واقعاً همین کار را خواهند کرد. واقعاً همین‌طور فکر می‌کنم. گزینه دیگر برای هیچ‌کس قابل قبول نیست.
جرد کوشنر... [بخش نامفهوم] اما استیو و جرد، دو نفر بسیار باهوش هستند و دارند کارشان را انجام می‌دهند و فکر می‌کنم این ماجرا را تمام خواهند کرد. هر دو طرف احترام زیادی برایشان قائل‌اند. ایرانی‌ها برای هر دوی آنها احترام زیادی قائل‌اند و فکر می‌کنم این مهم است. اما فکر می‌کنم کار را به سرانجام می‌رسانیم.
...
می‌دانید، زمانی خواهد رسید که دیگر خیلی دیر خواهد بود و ما دیگر شاید فرصت این را نداشته باشیم که بگذاریم به‌عنوان یک کشور باقی بمانند. من مایلم بقای آنها را ببینم. می‌توانم بگویم افراد دور این میز هم دوست دارند چنین چیزی را ببینند. بعضی‌ها از شنیدن این حرف تعجب می‌کنند، اما آنها چنین چیزی را می‌خواهند.
همان‌طور که می‌دانید، نیروی دریایی آمریکا مین‌های ایرانی را از مسیر کانال‌ها در تنگه هرمز پاک کرده است و اکنون در حال تسهیل ازسرگیری جریان نفت هستیم. اخیراً اعلام کردیم که بیش از یک میلیارد بشکه نفت را از خلیج اسکورت کرده‌ایم. حالا این برای تمیم رقم زیادی نیست، اما برای بیشتر مردم هست. یک میلیارد بشکه؛ این نفت زیادی است، درست است؟ از هر طرف حساب کنید همین است.
اما اخیراً اعلام کردیم که دوباره بیش از یک میلیارد بشکه نفت را فقط در همین مدت اخیر اسکورت کرده‌ایم و هر شب ۲۵ تا ۳۰ کشتی را خارج می‌کنیم؛ گاهی روزها هم، اما بخش زیادی در شب انجام می‌شود.
محاصره قوی‌ترین چیزی است که کسی تاکنون دیده است. اسمش را «دیوار فولادی» گذاشته‌ایم و نیروی دریایی ما شگفت‌انگیز است. ارتش ما شگفت‌انگیز است. واقعاً شگفت‌انگیز است. و حالا نفت بیشتری از تنگه عبور می‌کند، نسبت به هر زمان دیگری، با فاصله زیاد، از آغاز درگیری تاکنون.
و باز هم، بخش بزرگی از کاری که کرده‌ایم، شاید ۹۹ درصدش، برای اطمینان از این بوده که ایران سلاح هسته‌ای نداشته باشد. آن سایت‌ها منفجر شده‌اند. شاید مجبور شویم یک سایت دیگر را هم منفجر کنیم؛ کوه پیک‌اکس. فعلاً فعالیت زیادی آنجا نمی‌بینیم، اما اگر ببینیم، فوراً آن را منفجر خواهیم کرد.
در حالی که همه اینها خبرهای بسیار خوبی است، حملات تروریستی ایران به کشتیرانی تجاری و کشورهای همسایه نشان داده که لازم است زیرساخت انرژی خاورمیانه را از گلوگاه‌های تحت کنترل ایران دور کنیم. به همین دلیل دولت من قویاً از کریدور اقتصادی هند–خاورمیانه–اروپا حمایت می‌کند و همچنین از راه‌های دیگر برای انتقال نفت، چه از طریق خطوط لوله یا هر راه دیگری.
و با همکاری هم، در آستانه غلبه بر چالش‌هایی هستیم که دهه‌ها این منطقه را گرفتار کرده‌اند. این وضعیت دهه‌ها ادامه داشته است.
پس آنها ایران را به مدت ۵۱ سال «قلدر خاورمیانه» می‌نامیدند. من می‌گفتم ۴۷ سال، اما چهار سال است این را می‌گویم، پس عدد واقعی ۵۱ سال است. و واقعاً دیگر قلدر نیستند. می‌توانند مشکل ایجاد کنند، اما دیگر قلدر نیستند. ولی قلدر خاورمیانه بودند و همه بسیار نگران و به نوعی ترسان بودند. شاید هم حق داشتند، اما دیگر نمی‌ترسند.
بنابراین فکر می‌کنیم که وضعیت ایران ممکن است درست بعد از انتخابات میان‌دوره‌ای پایان یابد، شاید هم قبل از آن. نمی‌دانم. هیچ‌وقت نمی‌شود مطمئن بود.
اما آنها درک نمی‌کنند. چیزی که واقعاً درک نمی‌کنند این است که من انتخابات را با اختلاف بسیار زیاد بردم. هر هفت ایالت چرخشی را بردم. در رأی مردمی، با اختلاف میلیون‌ها رأی پیروز شدم. در شهرستان‌ها ۸۶ درصد بردم، چیزی که قبلاً هرگز اتفاق نیفتاده بود. این بالاترین میزان تا آن زمان بود؛ و در کالج انتخاباتی هم با اختلاف زیاد، اختلافی بسیار بزرگ.
و من نامزد نیستم. افراد دیگری نامزد هستند. جمهوری‌خواهان دیگری نامزد هستند. آنها آدم‌های فوق‌العاده‌ای هستند و من کمک می‌کنم انتخاب شوند. اما خودم نامزد نیستم.
و اصلاً به انتخابات فکر نمی‌کنم وقتی که به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم. فقط به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم و تمام. فقط به همین فکر می‌کنم. و هیچ ارتباطی با انتخابات ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78497" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VhoL3sc5OmsNIplYqt2w6VN8gYd7iG1QSdl8mQyaDPO3mKP7nDEODR4XNmBDA2RRAph2pNKUPMKsbJDpNj4tUazi1wWP5sFPaXqbzQ6tBUxplsR0hTht4ayFs8N7UdG7y0tkA-AkS2rBEsaF--f_9I2MXzkLNH8jIm8TouNCM76iejOyl76EM7__85JrNdiK4PlP_Mo27CKCIPhJ_tyDTWkocZomd537WWMBEhrniVxwNi3dqEYIEHhKhAptNKoa46M-lsKUlJ8y2ngFkiLCi5BekGoQPFXLJKPjUzDgsXOM1tmoSG9plp6hXTc9rTdBhn3Ea4lcSgdTZJLHQmoW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما: عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78496" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=ZV-Ev18_1DcqpESZ7FkD7PQt82Oz9rI6xPeOI-fnfzFTN7JccEbraDRU-4ZVfUQs6XgkFvVbWv91mUUynTQtJ5rPbQalhM07_BEgztB46lERSmATlzuA0yCNu0Hpyyw3e4M3uQ4wg9QJ3jJx4QELyK3wF673M_Fxi0WN94v9SXmMxec2UCx3UzVaPmAx2DR0Uvr1Q_dDEjcS7imMZomv-ZJ8f_szqDEj_QsMP5ZRPwIufEafu9k9dmcyZ5Tox45nsOpD8p_OPnZSiGQUKFSw9ttitdIqnCrfnRj6us4w-S0fD48zwWRw9_jhG2OQoCMKH0itWjJwTHOUWJ3Ja5axng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=ZV-Ev18_1DcqpESZ7FkD7PQt82Oz9rI6xPeOI-fnfzFTN7JccEbraDRU-4ZVfUQs6XgkFvVbWv91mUUynTQtJ5rPbQalhM07_BEgztB46lERSmATlzuA0yCNu0Hpyyw3e4M3uQ4wg9QJ3jJx4QELyK3wF673M_Fxi0WN94v9SXmMxec2UCx3UzVaPmAx2DR0Uvr1Q_dDEjcS7imMZomv-ZJ8f_szqDEj_QsMP5ZRPwIufEafu9k9dmcyZ5Tox45nsOpD8p_OPnZSiGQUKFSw9ttitdIqnCrfnRj6us4w-S0fD48zwWRw9_jhG2OQoCMKH0itWjJwTHOUWJ3Ja5axng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
در دیدار با ایران، آیا آقای کوشنر و آقای ویتکاف شرکت داشتند؟ درست متوجه شده‌ام؟
ترامپ:
می‌خواستم همین را بگویم؛ آنها دیداری بسیار خوب و بسیار سازنده داشتند و دیدار دیگری هم برای آینده بسیار نزدیک برنامه‌ریزی شده است.
استیو، اگر می‌خواهی... جرد، اگر می‌خواهی چیزی بگویید؛
آنها دیدار بسیار سازنده‌ای داشتند.
حدود یک ساعت پیش.
خیلی خوب پیش رفت. یک ساعت پیش تمام شد. دیداری بود که سه ساعت طول کشید. یک ساعت پیش تمام شد.
دیدار بسیار خوبی بود. یعنی باید بگویم، خیلی خوب بود. اصلاً نمی‌توانم تصور کنم چرا آنها نخواهند به توافق برسند.
یا عظمت است؛ عظمت بالقوه... یا نابودی کامل. دو انتخاب وجود دارد. یعنی، در یک حالت نابودی کامل است و گزینه دیگر، عظمت بالقوه است.
ایران می‌تواند کشور بزرگی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78495" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ectjNA81h0cZ6TL5_ZJbLfJPey3OG2qs-cM2nzJUH6C_iPbqtT3EAAMA9eDzg-QENsG7q6JI9MigY4DKZrjDkQaVuS32uzu4TWDJxdPH5-Y0LLYhx3IsMBXEz0SsywfICga0X9TtiaWvWrP7iYR-ksybomYAb2-INbM6uR_I3ZdkJ0PNh8AmCEAHKPZCDmNMXyhsS_-yeQEzdelzZUmE_1XKZRn_2LQecuNDXaAGIMC2ag9Es10a3vKFQod68DnHakYXol_nR20xsiQDF8FhQQsXBQBuhiKmjVuW9aQyCElyjvv3iDsJh8kh4EAg7IFDfpSIuoFydf-e1jCwE5QPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۱ شهریور اعلام کرد استیو ویتکاف، فرستاده ویژه آمریکا، و جرد کوشنر، داماد او، ساعاتی پیش در حاشیه نشست مجمع عمومی سازمان ملل به مدت سه ساعت با اعضای هیات جمهوری اسلامی دیدار کرده‌اند.
ترامپ که در دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با خبرنگاران صحبت می‌کرد، گفت این دیدار «خیلی خوب پیش رفت» و افزود نشست دیگری میان دو طرف در «آینده بسیار نزدیک» برگزار خواهد شد.
ترامپ درباره احتمال توافق با جمهوری اسلامی گفت: «نمی‌توانم تصور کنم چرا آنها نخواهند توافق کنند. انتخاب آنها یا رسیدن به عظمت بالقوه است یا نابودی.»
استیو ویتکاف نیز در پاسخ به پرسشی درباره ارزیابی خود از این دیدار، ابتدا از اظهارنظر خودداری کرد اما سپس گفت: «در حال حاضر احساس خیلی خوبی دارم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78494" target="_blank">📅 22:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZEx2lZFq4Q2Kj-c03hP8ZizE9w2FfPIgHcHDgLCHOwCncTSt9Bi8sz3nxawRon7vUk97kvVeAzt66vkDNvNOtYp-MjvFm67M6c_qt2Z90qp0_QvaJU2uyg79PcXtSono_kUzfWXBtlOpn2OkDJGPiWXNWGKby5n7OSN7b8fRxnV9KXheDO6XnNqYXP5OdPaqVlWDIMTjIi5Wdl5Kg5vLqV1eyR5hdYAsp1F4F52obsa9nfX4CZHSOdr-4WE0lL8dmqqQhVGrOQHJqxmxmvJeg5PhX7x6gHjHQnfbBgODtIVypP2s76Nn0TVThueNcDH5L96vhZbwYF4okbSAyP_9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از بیش از هفت ماه غیبت کامل از انظار عمومی و در حالی‌که هنوز هیچ صدا و تصویری از مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی منتشر نشده، روز سه‌شنبه ۳۱ شهریور، دست‌نوشته‌ای منتسب به او در رسانه‌های جمهوری اسلامی منتشر شد.
بر اساس تاریخی که زیر امضای این نوشته وجود دارد، متن مورد نظر در دهم مردادماه، یعنی بیش از ۵۰ روز پیش نوشته شده است.
در این متن که خطاب به مجید موسوی، فرمانده هوافضای سپاه پاسداران نوشته شده، نویسنده از او بابت گزارشی که محتوای آن مشخص نیست، قدردانی کرده و خواسته است که تلاش‌ها در زمینه زنجیره تامین ادامه یافته و گزارش آن مرتبا به او ارائه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78493" target="_blank">📅 20:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSgz_QoImxJKames634Zh2WsH2TOCGxfsy9zX8wbR3aFKJTd8YpJzaFIIzD14i-x_SCzzMSX3_JKPELEp0-S0JOcVCxmc5IPlAXOGUe4_lDhXOXkORu-GYZSvXsITbgxMrsRGoPgcjGtdnrbbBDNFIclQ0C0z54EBiUS7KjizAYpjc57K4ofXpdBISNmMJn5eJEYla-AyXXpwWkN443dhYKepxlsxU54YWHbUdLLswHsW7zqipLomVmJpVhTATd83M_G_77tmelpT6JoIZZTllC5AQXD3-T66BoJNhyHy685QlyqEWApM0Khi12i7D2HULNEvfT9s3dWrjdX8PPicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در دیدار با اندی برنهام، نخست‌وزیر بریتانیا، در سازمان ملل در نیویورک گفت تهران و واشینگتن روز سه‌شنبه نیز در حال گفت‌وگو بوده‌اند و افزود: «فکر می‌کنم توافقی حاصل خواهد شد.»
ترامپ گفت: «ما مانع دستیابی آنها به سلاح هسته‌ای شدیم. واقعا جلوی آنها را گرفتیم. آنها سلاح هسته‌ای نخواهند داشت و خواهیم دید چه اتفاقی می‌افتد.»
برنهام نیز گفت در نخستین دیدار خود با ترامپ «ارتباط خوبی» با او برقرار کرده و دو طرف درباره خاورمیانه، جزایر فالکلند و مسائل تجاری گفت‌وگو کرده‌اند.
او خطاب به ترامپ گفت بریتانیا آماده است نقش خود را در خاورمیانه ایفا کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78492" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jgHcCvU0_-A6eTupWx81j-FxYFDv4pCUsgIi-tWGXIz_xHOBDPdWDcIEl-MfejaU87PZNIaOkEG72h4UTPkWZZSUugjG9_Wv8BEqFv6wHrIghyBvIs5uDpelySEcnyMIPxKmefRvdNHussTbTvH5ekxFfUl3QRjzgAEPcebSDdRfaSvCELo2g2YMHP2Y45a3DWFfQ7VkOJMAgYDby3G4KBVzbswNGXijCc_xCKiR8ytH60lnyuDxQNLeoKMfFhb0r9Nm932_fXFatki-cDn0Eygv5SHWadymIamZJ2-Jih_kLfmj6EIOlZAmzOkkm3HqIBlQFE69w3-bskAOLKKVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه ۳۱ شهریور در جریان سخنرانی در مجمع عمومی سازمان ملل متحد، با اشاره به درگیری‌های جاری، وضعیت کنونی منطقه خلیج فارس را «یکی از خطرناک‌ترین مراحل» تاریخ این منطقه توصیف کرد.
وی ابراز تاسف کرد که بسته شدن یک آبراه بین‌المللی حیاتی که نزدیک به یک‌چهارم تجارت انرژی جهان از آن می‌گذرد، ممکن شده و شریان‌های اقتصاد جهانی به ابزاری برای فشار و چانه‌زنی تبدیل شده‌اند؛ موضوعی که هزینه آن را مردم سراسر جهان می‌پردازند.
امیر قطر با اشاره به اینکه این بحران قیمت مواد غذایی و دارو را افزایش داده و معیشت مردمان بی‌ارتباط با جنگ آمریکا و اسرائیل علیه جمهوری اسلامی ایران را تحت تاثیر قرار داده، تاکید کرد که دوحه همچنان بر حل دیپلماتیک این بحران پافشاری می‌کند.
وی خواستار بازگشایی تنگه هرمز به روی کشتیرانی تجاری و بازگشت به میز مذاکره شد تا از گسترش جنگ جلوگیری شده و زمینه برای رسیدن به یک راهکار پایدار جهت تضمین امنیت و ثبات کل منطقه، از جمله ایران، فراهم گردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78491" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMP392pneW__5NjS3Rx6T1bsVge9u8VWoJm4qJ78n4FmDJX9W1-MDDaCBW5iquvyeTZYI_dfreVjwuEg2vBIvyngyml8fzb_sY3Ugn5IId4A2ECgQTEaIXgyCWpB1e_4SQ9bVAaxqKP__G3U5sLfXDlLVNTi8po3HqR5FWOamfHXIftokfEnkIGa8U4MZ4f19W8bAaKNlNqynjxHb0xu1UWyvaexwEl2VgpswXWARk8nR1TkUAlX3PLlLzbsTsYWpsVq2iZNq1wJZPxRUU3fyrLvO1L4g0Lnh2JDq9MHjoWqCOw_-cenhiOV7LwN5rDjWNjE_0p4ITv44vK50SIwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز سه‌شنبه ۳۱ شهریور ۱۴۰۵، گزارش داد چند کشور عربی که میان آمریکا و جمهوری اسلامی میانجی‌گری می‌کنند، در حال رایزنی با دو طرف برای برگزاری یک دیدار در سطح بالا در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک هستند.
بر اساس گزارش اکسیوس ، کشورهای عربی تلاش می‌کنند از حضور مقام‌های ارشد دو طرف در نیویورک برای شکستن بن‌بست در جنگ میان آمریکا و جمهوری اسلامی استفاده کنند.
مارکو روبیو، وزیر خارجه آمریکا، روز سه‌شنبه به شبکه ان‌بی‌سی گفت دونالد ترامپ برای دیدار با مقام‌های جمهوری اسلامی در نیویورک آمادگی دارد، زیرا به گفته او، گفت‌وگو با طرف‌های درگیر برای حل مشکلات اهمیت دارد. روبیو در عین حال گفت هنوز چنین دیداری برنامه‌ریزی نشده است.
ترامپ قرار است روز سه‌شنبه با نمایندگان ۹ کشور عربی درباره جنگ دیدار و گفت‌وگو کند. منابع منطقه‌ای گفته‌اند شماری از این کشورها از ترامپ خواهند خواست از تشدید تنش با جمهوری اسلامی جلوگیری کند و برای دستیابی به توافق تلاش کند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز صبح سه‌شنبه در نیویورک با محمد بن عبدالرحمن آل‌ثانی، نخست‌وزیر قطر، دیدار کرد. قطر یکی از میانجی‌های اصلی میان تهران و واشنگتن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78490" target="_blank">📅 20:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPp7asRS8oRvfgkTZOj4o71DRm-sjEFibFOXGs99aOXDizQ21HuwB88QM8nk70Z_rHqwvMRbTPbyyyhm6b9xGf8kDRKEz67tCbXeKo2dklL6mA1woLaTj3_ZOOk8jxpHaeqtdZQVuSyObxMjNzUKKLyh8kpY096E1UZftpYlYJxSOyYJ6QSRnicUKLFvdKMiC28PiMhdBR95OufFE7zYxMzFuCfBYXDegxx2ArVlJrD_cLH0KYumtQ55n_GEChiKuQYAfa-8QOBDPHjRfynxhlhBM0q3HHO9EhhX2y5UCecrnEi2FenE_C3PvTG_OrecUOq_m8v9bqJmet3xw7p4NgRlI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPp7asRS8oRvfgkTZOj4o71DRm-sjEFibFOXGs99aOXDizQ21HuwB88QM8nk70Z_rHqwvMRbTPbyyyhm6b9xGf8kDRKEz67tCbXeKo2dklL6mA1woLaTj3_ZOOk8jxpHaeqtdZQVuSyObxMjNzUKKLyh8kpY096E1UZftpYlYJxSOyYJ6QSRnicUKLFvdKMiC28PiMhdBR95OufFE7zYxMzFuCfBYXDegxx2ArVlJrD_cLH0KYumtQ55n_GEChiKuQYAfa-8QOBDPHjRfynxhlhBM0q3HHO9EhhX2y5UCecrnEi2FenE_C3PvTG_OrecUOq_m8v9bqJmet3xw7p4NgRlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ در سازمان ملل
با تشخیص و ترجمه ماشین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78489" target="_blank">📅 19:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c08589429.mp4?token=lObeJHp5DFYp5zHaxaewFUAegzWw-T3r8qh-P9BS2ShfxUI3_xLPhX4qVDWv_QEwTDgTz8WgSwOh5IonY8G9I9cvbhh4EEtMuvZJM0w_DIaX7Lv3Pf6em7q4_ptnTO66xY17Oypqh2bjLGGUlzMOq9Hbp3pbO_helVY5t66yZBccjK6HJFmRwYwiH4eY0uQJBVC5zFk7oHrjm_91tgCWJTdjaCGCgpy1QxxEeJj1W4_BpGb_2WE1n0zbXJ0BDHRWdL0zK-LbcO5oUZOrX5PRvXfw3BnJLC7jsOUb-aUpc4NlpBNflgdnDd42RdB1SPZhh5FtAGXIW_mDO2bGf7ol_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c08589429.mp4?token=lObeJHp5DFYp5zHaxaewFUAegzWw-T3r8qh-P9BS2ShfxUI3_xLPhX4qVDWv_QEwTDgTz8WgSwOh5IonY8G9I9cvbhh4EEtMuvZJM0w_DIaX7Lv3Pf6em7q4_ptnTO66xY17Oypqh2bjLGGUlzMOq9Hbp3pbO_helVY5t66yZBccjK6HJFmRwYwiH4eY0uQJBVC5zFk7oHrjm_91tgCWJTdjaCGCgpy1QxxEeJj1W4_BpGb_2WE1n0zbXJ0BDHRWdL0zK-LbcO5oUZOrX5PRvXfw3BnJLC7jsOUb-aUpc4NlpBNflgdnDd42RdB1SPZhh5FtAGXIW_mDO2bGf7ol_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"جمعیت ایرانیان برای رد شدن از مرز زمینی رازی."
شهرستان خوی- مرز زمینی بین ایران - ترکیه. میرن اونجا شهر "وان" فرودگاه
.
Sam1Kia
پیام دریافتی: ابی در وان ترکیه کنسرت داره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78488" target="_blank">📅 18:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
ترامپ: ایران در پی ساخت موشکی بود که می‌توانست اروپا را هدف قرار دهد
▪️
رئیس‌جمهور آمریکا در سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران به ساخت ذخایر گسترده موشکی و پهپادی ادامه داده و مدعی شد تهران موشکی ساخته بود که توان هدف قرار دادن اروپا را داشت. او گفت هدف ایران این بود که در پوشش چنین توان موشکی‌ای، به سوی ساخت سلاح هسته‌ای حرکت کند.
▪️
ترامپ همچنین با اشاره به حمله هفتم اکتبر گفت عاملان این حمله از سوی ایران تامین مالی شده بودند و افزود حکومت ایران «چنین خشونتی را جشن گرفت». او سپس حکومت ایران را به کشتار گسترده شهروندان خود متهم کرد و گفت چنین حکومتی نباید امکان فعالیت «در پشت سپر هسته‌ای» را پیدا کند.
@
VahidOnLive
🔻
ترامپ: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند
▪️
︎ دونالد ترامپ در سخنرانی خود در مجمع عمومی سازمان ملل، جمهوری اسلامی ایران را «بزرگ‌ترین حامی تروریسم» خواند و گفت که حکومت ایران سال‌ها در خاورمیانه «مرگ، ویرانی و هرج‌ومرج» گسترش داده است.
▪️
︎ او گفت: «هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند» و افزود پس از آغاز دوره ریاست‌جمهوری‌اش، مذاکراتی را با ایران آغاز کرد و در مقابل پایان برنامه هسته‌ای و حمایت از تروریسم، پیشنهاد همکاری اقتصادی کامل داد، اما به گفته او ایران این پیشنهاد را رد کرد.
▪️
︎ ترامپ همچنین گفت که ارتش آمریکا در عملیات «چکش نیمه‌شب» برنامه هسته‌ای ایران را هدف قرار داد و پس از آن نیز از تهران خواست توافق کند، اما ایران بار دیگر نپذیرفت. او سپس ایران را به ادامه انباشت موشک‌ها و پهپادهایی متهم کرد که به گفته او امنیت نیروهای آمریکایی و دیگر کشورهای منطقه را تهدید می‌کرد.
@
VahidOnLive
🔻
دونالد ترامپ: تصور کنید حکومت پلید ایران پشت سپر هسته‌ای حملات تروریستی انجام دهد
▪️
︎ دونالد ترامپ گفت: «فقط تصور کنید اگر چنین حکومت پلیدی روزی قادر می‌شد در پناه یک سپر هسته‌ای حملات تروریستی گسترده انجام دهد. این واقعیتی بود که باید با آن روبه‌رو می‌شدیم؛ واقعیتی که افراد بسیار زیادی ترجیح دادند آن را نادیده بگیرند.»
▪️
︎ او افزود: «در حالی که دیگران حرف زده‌اند، من عمل کرده‌ام. در حالی که دیگران از صلح سخن گفته‌اند، من آن را برقرار کرده‌ام. در حالی که دیگران تهدیدها را نادیده گرفته‌اند، من با آنها مقابله کرده‌ام.»
▪️
︎ ترامپ گفت: «من از آن برای تبدیل آمریکا به قدرتمندترین کشور جهان استفاده کرده‌ام.»
@
VahidOnLive
🔻
ترامپ: امیدوارم پس از انتخابات با ایران به توافق برسیم
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت که آمریکا باید فشار بر ایران را حفظ کند و افزود نیروی دریایی آمریکا تاکنون بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت کرده است. او گفت اکنون نفت بیشتری نسبت به هر زمان دیگری از آغاز جنگ از این مسیر عبور می‌کند.
▪️
︎ ترامپ سپس گفت که در برابر ایران با یک «تصمیم بزرگ» روبه‌روست: یا توافقی حاصل شود که به گفته او به ایران امکان بازسازی و تبدیل شدن به کشوری «بسیار بزرگ‌تر» را بدهد، یا آمریکا مسیر نظامی را در پیش بگیرد. او در عین حال گفت: «فکر می‌کنم درست بعد از انتخابات به توافق خواهیم رسید، چون منطقی نیست که آنها توافق نکنند.»
@
VahidOnLive
🔻
ترامپ: نیروی دریایی و نیروی هوایی ایران از بین رفته‌اند
@
VahidOnLive
🔻
ترامپ: انتخابات در تصمیم من درباره ایران تاثیری ندارد
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران ممکن است منتظر نتیجه انتخابات میان‌دوره‌ای آمریکا باشد، اما تاکید کرد این انتخابات در تصمیم او درباره ایران «اصلاً وارد محاسباتش نمی‌شود.» او گفت: «تنها چیزی که اهمیت دارد این است که ایران هرگز سلاح هسته‌ای نخواهد داشت.»
▪️
︎ ترامپ همچنین گفت برخلاف ادعاهایی که به گفته او مطرح می‌شود، آمریکا با کمبود مهمات روبه‌رو نیست و ذخایر تسلیحاتی این کشور با سرعتی بی‌سابقه در حال افزایش است.
VahidOnLive
🔻
ترامپ: اگر توافق نشود، جمهوری اسلامی ایران را نابود می‌کنم
▪️
︎ دونالد ترامپ در مجمع عمومی سازمان ملل گفت باید تصمیم بزرگی بگیرد که اگر توافقی حاصل نشود جمهوری اسلامی ایران را نابود خواهد کرد. او گفت فکر می‌کند ایران بعد از انتخابات میان دوره‌ای با آمریکا توافق خواهد کرد.
▪️
︎ او بار دیگر گفت جمهوری اسلامی ایران بزرگترین حامی تروریسم در دنیاست اما اکنون دیگر تهدیدی نیست چون آمریکا برنامه هسته‌ایش را نابود کرده است.
▪️
︎ رئیس‌جمهور آمریکا بار دیگر گفت اخیرا ده‌ها هزار معترض اخیرا در ایران کشته شده‌اند.
▪️
︎ او از اروپا انتقاد کرد که متوجه تهدید موشکی ایران نبوده است.
▪️
︎ آقای ترامپ بار دیگر گفت تمام قوای نظامی و اقتصاد ایران نابود شده است.
▪️
︎ او همچنین گفت دولتش در ۱۲ ماه گذشته بیش از هر دوره‌ای در تاریخ آمریکا در زمینه نظامی سرمایه‌گذاری کرده است.
@
VahidOnLive
🔻
ترامپ از همه کشورها خواست ایران را «به‌طور کامل از نظر اقتصادی منزوی کنند»
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل از همه کشورها خواست به آمریکا بپیوندند و «انزوای کامل اقتصادی ایران» را اعمال کنند؛ تا زمانی که به گفته او تهران حملات به کشتی‌های تجاری را متوقف کند، از «جاه‌طلبی‌های هسته‌ای» خود دست بکشد و حمایت از تروریسم را پایان دهد.
▪️
︎ او حکومت ایران را «ضعیف و مستأصل» توصیف کرد و گفت اگر کشورها متحد بمانند، به گفته او «تهدید ۵۱ساله تروریسم ایران» پایان خواهد یافت و قیمت نفت نیز کاهش پیدا خواهد کرد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78487" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZG6cAhMAanMcBHJ2a1KHPcaRLUJvrmD4o-js8sj7F1QPrtv-16su2fwGHNEn5GiratqEXUhFSCZzSoqdHJR7n9nOQHG0hYTIRDtN7qHdyiDhq4HSDCyvxgtxDijcDw94HrUpQEQ8NnlTUioJ_EuCw3OAlB6nf_Rbhd6OwFYDTgmLqWzghzUieFf14IahsyWKRLESKhTD58aYfb8qB2Lz6LmkYI0HHnDHIqmRFRzCzxi9WB2e2C0Vu8f-ctuQ3MN89RHXRS0J_Y01PZgV5KnSB1c-pj-H4tSqmsIfLtStDc6VIExA2PhVhFNPLmImW2QUkRsDgt2qO1GpQFhyxgERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد جمهوری اسلامی گفته است تهران پیشنهاد کرده در صورت کاهش فشار نظامی آمریکا و برداشتن گام‌های اولیه برای پایان محاصره بنادر ایران، تنگه هرمز را ظرف هفت روز بازگشایی کند و به مذاکرات با واشنگتن بازگردد.
خبرگزاری «کیودو» روز سه‌شنبه۳۱شهریور۱۴۰۵ به نقل از این مقام، که نامش اعلام نشده، گزارش داد این پیشنهاد از طریق میانجی‌ها به دولت آمریکا منتقل شده و بخشی از تلاش تازه تهران برای احیای مذاکرات با واشنگتن است.
براساس این پیشنهاد، جمهوری اسلامی خواهان ازسرگیری مذاکرات با هدف رسیدن به توافقی برای «پایان دائمی مخاصمه» میان ایران و آمریکا است.
این مقام گفته است تهران در مرحله نخست انتظار دارد واشنگتن نشانه‌هایی از آمادگی برای بازگشت به مذاکرات نشان دهد و اقداماتی را برای پایان محاصره نظامی بنادر ایران و توقف عملیات نظامی مرتبط با تنگه هرمز آغاز کند.
در صورت برداشته‌شدن این گام‌ها، جمهوری اسلامی آماده است ظرف هفت روز مسیر عبور کشتی‌ها از تنگه هرمز را باز کند و به میز مذاکره بازگردد. این مقام تاکید کرده است آمریکا برای پیشرفت دیپلماسی باید «جدیت و تعهد» خود را نشان دهد.
کیودو نوشته است پیشنهاد تازه تهران به تایید «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، و شورای عالی امنیت ملی رسیده است. مقام ایرانی مشخص نکرده که آیا این پیشنهاد به معنای عقب‌نشینی تهران از بخشی از هفت شرطی است که پیش‌تر برای مذاکره و بازگشایی تنگه هرمز مطرح شده بود یا خیر.
براساس گزارش کیودو، شورای عالی امنیت ملی ۲۵مرداد تصمیم گرفته بود اگر آمریکا ظرف ۴۵ روز محاصره بنادر ایران را پایان ندهد، جمهوری اسلامی گزینه حمله دوباره به نیروهای آمریکایی را برای خود محفوظ نگه دارد. این مهلت اکنون به پایان خود نزدیک می‌شود.
هم‌زمان، یک مقام ارشد ایرانی به «رویترز» گفته است هیات جمهوری اسلامی در مجمع عمومی سازمان ملل در نیویورک اختیار کامل برای احیای گفت‌وگوهای دیپلماتیک با آمریکا دارد و جزییات توافق احتمالی می‌تواند از طریق کشورهای میانجی در نیویورک بررسی شود.
مقام ایرانی احتمال دیدار «مسعود پزشکیان» و «دونالد ترامپ» در حاشیه مجمع عمومی را رد کرده، اما گفته است همچنان «امکان حرکت به‌سوی توافق» وجود دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78486" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJOABMFDpdkxyUiTyLTFbX9TucQqXMQvKFefRvJL-UiRboupFvvQQQoiUb02bpkNgsE4nkJE9qlDRU-ohH6Dt6pWTDLLOCTgO8bVTJVKn9vtya96JagVdfIztppGD-TrPQ5PxF9PGaL648t-VPDmvaZIfpKtnrlunN8EY1AbtCbiJ_AC8fpri9O4fTVAcdKA4AfRI1eXQE8OZulRzNVKUQNkkujpcMOdXhpQ-nDq1u4ULDRiF2qZ1FH-sLKtVuNGgdM9MFL9jlgWCIpG05N2IZMQY624tlTKd_480h4PH0IbjuymnjwrQEdytAbPPHjezFjTANyPEyvC5C2hIAAG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدرضا رادان، فرمانده کل انتظامی جمهوری اسلامی، با اشاره به حملات آمریکا گفت که جمهوری اسلامی بر دشمن پیروز خواهد شد. رادان گفت: «به اذن خدای متعال، صبح قطعی پیروزی نزدیک است و ما حتما بر دشمن پیروز خواهیم شد.»
او همچنین از اقدامات حوثی‌های یمن علیه عربستان سعودی تقدیر کرد و گفت: «امروز اراده یمنی‌ها موجب شد تا رزمندگان انصارالله هزاران کیلومتر پیشروی کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/78485" target="_blank">📅 17:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wqag88-RF7LRGlFuGyBIjeIgHNCztStEK7VYNi6sgLE6sk2xx19TalSgD42tXu9nQCx8UWHmGAnJluS2J3Ggeo2FnYSidFaK0J62mPJPcfK39h-V7VcmgECVL13et65VsEgd01NWj_h6fHN1gTM32cRbqFC4KqdSz2Dts6-HCr0K770t0VJB-Ws52rmz1QtAHpIa0Jr7hDsuBzlGFyQGRUe9o4NNA3kV92GV-BkoOYR0TqdRVhPUJkMaSeYTKxaFwR5yxhbi_d2zqqFh7TAZ1PQLoSPCWG2TpvaSRYGZbimzELDW7581z4W0gRIEzpy9ro0wJvpUciZ8M4yl4-Omkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران روز سه‌شنبه با نزدیک یک درصد افزایش نسبت به روز گذشته به ۲۳۳ هزار تومان رسید.
بر پایه داده‌های شبکه اطلاع‌رسانی طلا و ارز دلار روز دوشنبه ۲۳۰ هزار و ۸۰۰ تومان بسته شده بود. بهای دلار در ساعات نخست معاملات امروز تا ۲۳۵ هزار تومان نیز بالا رفته بود.
یورو ۲۶۷ هزار و ۴۴۰ تومان، پوند بریتانیا ۳۱۱ هزار و ۴۳۰ تومان و درهم امارات ۶۳ هزار و ۴۷۱ تومان معامله شد.
در بازار سکه، سکه امامی با یک و نیم درصد افزایش به ۲۳۸ میلیون و ۴۸۰ هزار تومان رسید و سکه بهار آزادی با یک و هفت دهم درصد افزایش ۲۳۴ میلیون و ۶۷۰ هزار تومان قیمت خورد.
نیم‌سکه با هشت دهم درصد افزایش ۱۲۱ میلیون و ۴۰۰ هزار تومان معامله شد. ربع‌سکه ۶۳ میلیون و ۸۰۰ هزار تومان و سکه گرمی ۳۳ میلیون و ۲۰۰ هزار تومان بدون تغییر ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/78484" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHF4O7GH13Ja1R4PrM_FQjw2aHclGZLSE1TTI1mNtMsg0RPURIwGd_ZrR63V7OkWM668HLwKQE81sMi-KajSiSGBaLvTnvulmM6e9PYvUHU2tq9Pap5anrjBZCTZ-6jESvdP25hl4hE69DSQi9qYfSNnmJxPJn8FvxdtH9mqHhgnB4LbO0xiBrrwKiuG1cThGp7QD3Ao79LKGQPFt-ptXEquYyaZU3CE5_GztDGkHhixneXh5Zka4S9CuM7Z6z3dW4xTN9Xv101HvtV-IC7OEFHgDtgppyRyq7uU8P6csklFfboIVA65PU_GDy-XpH5rAmfZ7Z4BMImS-KFrZtqorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهور آمریکا می‌گوید این کشور «بیش از آنچه حتی بتوانیم برای استفاده تصور کنیم مهمات» دارد و به گفته او «اکنون نیز در حال افزایش ذخایر مهمات خود در سطوحی هستیم که تاکنون هرگز شاهد آن نبوده‌ایم.»
دونالد ترامپ روز سه شنبه، ۳۱ شهریور در پیامی در شبکه اجتماعی تروث‌سوشال با رد وجود کمبود مهمات در ارتش آمریکا از کسانی که آنها را «بزدلان و خائنان» نامید نوشت آنها دوست دارند بگویند که ایالات متحده با کمبود مهمات مواجه است. این درست نیست.
نوشته رئیس جمهور آمریکا می‌تواند واکنشی به گزارش رسانه‌های مختلف درباره کمبود مهمات در ارتش آمریکا به‌ویژه پس از جنگ اخیر با ایران باشد. در این گزارش‌ها به‌ویژه از کاهش ذخایر موشک‌های رهگیر سامانه‌های پدافند هوایی خبر داده شده بود.
این در حالی است که شرکت لاکهید مارتین روز ۲۴ شهریور اعلام کرده بود که نخستین محموله از قطعات حیاتی موشک‌های رهگیر «پاتریوت» را از شرکت «جنرال موتورز» دریافت کرده است؛ این تحویل کمتر از یک ماه پس از امضای توافق‌نامه تولید میان دو شرکت صورت می‌گیرد، آن هم در شرایطی که پنتاگون بر تسریع روند تولید تسلیحات تأکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/78483" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlZSA6ObbsHLgNmCZkc9LoQFJAlo4OEgf8bavRTkQy78KIYUnpRSSM33x-AbcOYShWF1q3Z-wLres0kbk_7bFzmCvcKUEDYKxNAy02gnnHemf7la9Z6G1cHmDGDd47L4EnfrQ6zjGa1n8UkgEDdY6TjgtKWuuFHTYQqmNbzvRFRhdmqN-IIXSMPFpTs34vZ-XsMgnsPXIM2tGbnOw0pZP2kaPtOFfqlHOvYJmbTw4zh6c2G6Hejf0BUsbv_OOBd713BtQOiwjgn69Imc0mVyanRPjri5PW7ygNJAtwRckoglTTQxnaqLrhxSp193WR07z53gDp_BYUpm4Sf0Ik0-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو گفت آماده ملاقات با مقام‌های ایران در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک است.
وزیر خارجه آمریکا گفت: «فکر نمی‌کنم در حال حاضر چیزی برنامه‌ریزی شده باشد، اما قطعاً برای چنین دیداری آمادگی داریم، به‌ویژه اگر چشم‌انداز آن نتیجه‌ای مثبت و در نهایت تحقق هدف اصلی باشد.»
آقای روبیو گفت منظور او از چنین چشم اندازی این است که «ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد.»
عباس عراقچی، وزیر خارجه ایران از دوشنبه در نیویورک است و مسعود پزشکان هم عازم این شهر شده است تا در مجمع عمومی سخنرانی کند.
دونالد ترامپ دو روز پیش به شبکه فاکس گفته بود که آماده دیدار با مسعود پزشکیان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/78482" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78481">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZvDfu2j15J2-CcCiysqxe-rAli0TvzoApvuht5MLQzv-OSB7EixNtnN2Op-HtILkQy8M2VmbQca_y-1RgH-RX9QKZNjV6kDULEpM4JEAU_RHfrxzMIMU08thNC4hOtBHAN0Z9zPMjWe-SJjYO6E7gCg7IMo8XWweP_S40_8FJbO3S6vrnV-0Sc70TDD1dBN6pgP0ubKesbYkcNnU7je_D6T_eYC4ldhzPh69Ufe6WrsEC38ctO2QSYYjBlARjeNCVNVMHB3zqJt4ARVN8fGhFI85X4QkJsuXbdARtxn-WOrPyhfZYJF2WPelTv163jTb2k8FRvtQRfucwPVWDVvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین روز سه‌شنبه، ۳۱ شهریورماه، رسما اعلام کرد که با تحریم «یک‌جانبه» خطوط هوایی ایران توسط واشینگتن مخالف است.
گوئو جیاکون، سخنگوی وزارت خارجه چین، در نشستی خبری گفت که پکن این گونه تحریم‌های آمریکا را «غیرقانونی» می‌داند و با اعمال آنها مخالف است.
این موضع‌گیری یک روز پس از آن رخ می‌دهد که اسکات بِسِنت، وزیر خزانه‌داری آمریکا، روز دوشنبه گفت که تمام شرکت‌های هواپیمایی ایران از تاریخ ۲۳ سپتامبر (اول مهر) «در سراسر جهان تعطیل خواهند شد».
او در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «وقتی هواپیماهای ایرانی در فرودگاهی فرود می‌آیند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛ در غیر این صورت از سیستم دلاری کنار گذاشته خواهید شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/78481" target="_blank">📅 17:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihg1nxm4lBYO-KgGs7BVSvMkmoLizYgHjt41mUplgWJJWn1HKEapyAKNTGH96umSnmG3nz4b7TXgxs31tMLxMm1rGo6IB4-uwRUxT29AIFY23Tj0tvSmq8pG2QwTVNIxZLnwuwOd2hcl4x4v6a940od6fZVcJC4XfQpQqHeCPFA87gwCiE8trdJ1J2eEh3DldD8BrAG37cMaas5oth_lpSF3D0akKqWpIF9GRtxDGNQZImq4IKefnI-G-ALQ4LhMPPv2doAaoWsCBU8fMJtbCJi22CfejYn7-EAMd0Qi4VIkImLhDFIBCvoF4pcNY0smPLn1eFtQvDc5_ajKjH3Tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت نمونه‌های مثبت کووید-۱۹ در ایران برای پنجمین هفته پیاپی بالا رفت و به ۱۷ درصد رسید.
به گزارش مرکز مدیریت بیماری‌های واگیر وزارت بهداشت درباره هفته منتهی به ۲۷ شهریور، این نسبت در هفته مشابه سال گذشته هشت و نه دهم درصد بود. نسبت نمونه‌های مثبت کرونا هفته پیش از آستانه هشدار بالا گذشته بود.
وزارت بهداشت بر ضرورت تشدید مراقبت از عفونت‌های حاد تنفسی تأکید کرد.
این هشدار در حالی است که نگرانی‌ها از شیوع همزمان کرونا و آنفلوانزا تشدید شده است.
از طرفی واکسن آنفلوانزا با وجود نزدیک شدن فصل سرما هنوز در داروخانه‌های ایران توزیع نشده است. به گزارش روزنامه شرق، سازمان غذا و دارو از تأمین محموله‌هایی از چین، روسیه و برخی کشورهای اروپایی خبر داده، اما داروخانه‌داران می‌گویند خبری از توزیع نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78480" target="_blank">📅 17:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMJlqwWW8r9Xn2Vh72sOVOcotmNt8BQnCpGDvVVC6QbEpXsRVg4HlyM9mX4xuafQofAwjWECVsKldLKCv-KhJ4zgPSl0LQeIb8wFhd-o2q7jEa3-4QUqjk-qmmufcMYczBLarJIyC2r64WcxMfuUR_7V_-gPGLlTgceTgceNd1EO38hu-4BbjvhfiIXEB-wFvTGvHg_VG9lMYkiNUxtMl4U8y1r3nsaXsPFBOv7eSqGnu1V2XjEcPXzJfydupUoC2Ql0vSRkPbkSZK48XonCDqfKkqU4Pi9xYLjTZ7tlyuvsf6Lg8P6tZcDgGgmlQotueuiuGLsdcdWgjKK9yswKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر بریتانیا، می‌گوید با ارائه «پشتیبانی دفاعی و سوخت‌رسانی هوایی» به عربستان سعودی در برابر حملات حوثی‌ها موافقت کرده است.
اندی برنام روز دوشنبه ۳۰ شهریور گفت که این اقدام در پی درخواست عربستان سعودی برای دریافت «حمایت نظامی» صورت می‌گیرد.
دولت بریتانیا اعلام کرده است که زمان این طرح «محدود» است و براساس آن قرار است نیروی هوایی سلطنتی بریتانیا به جنگنده‌های نیروی هوایی عربستان در سرنگونی موشک‌ها و پهپادهای حوثی‌ها کمک کند.
برای ارائه این پشتیبانی، بریتانیا طی روزهای آینده یک فروند هواپیمای سوخت‌رسان «وویجر» را به منطقه اعزام خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78479" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9GoSkuBRaB5Rkm46bDOHpU_dmFYAdMgvXQmMkZroKaygyyXgBYzoOJqcZUJNMTZ-YGG9hN0zGm6rsiQZ72X6latKev4__F_qMt9rWj30ofZIdwJTiH2HDFB0qWKLrhU9AyeR4ia-e5mM0GUXeNU9gs9L89z4RbAhQ6Bwk4cdzg2uTaWFqNc3eTUREn6Ltz38s7w3XGCZ3qKGTjdYubVL6xxr4--kNIZJORFm9QfC42E7EoW_I97JjY4wkD_qdk0--topklrTq_WB1BIytpeq3ew51Q4ZzErcta-V7GRGwUm1UEQ5Vr7Cc0D01NLtP6zZdBoSBJ7I8QWkhhldyMV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهوری فرانسه، روز دوشنبه، با انتشار تصویری از دیدار خود با دونالد ترامپ در اکس، از توافق پاریس و واشنگتن برای اقدام مشترک در زمینه امنیت انرژی و بحران‌های بین‌المللی خبر داد. مکرون در این پیام نوشت: «به محض ورودم به نیویورک با ترامپ دیدار کردم. ما تصمیم گرفتیم با همکاری یکدیگر برای کاهش تنش‌ها در بازارهای انرژی، از طریق حفاظت از زیرساخت‌های حیاتی در خاورمیانه و تضمین آزادی دریانوردی در تنگه هرمز، اقدام کنیم.»
رئیس‌جمهوری فرانسه همچنین با تاکید بر تحولات جنگ اوکراین افزود: «ما تلاش‌های خود را مشترکا به کار خواهیم گرفت تا توقفی در حملات علیه زیرساخت‌های انرژی و تاسیسات غیرنظامی اوکراین به دست آید. جمعیت غیرنظامی باید محافظت شوند و ما باید هرچه سریع‌تر مذاکراتی جدی درباره شرایط صلح میان روسیه و اوکراین را آغاز کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78478" target="_blank">📅 05:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6qTepuUAeznJwTzjVUcArZFlVkwvH_BUIAr5uOyoHEE2ZsvQKxj6GtTeLTcfqTrm481jjSQ9526JboBwLhiHUiHCbPZcZcKqDirarixvV5PK50sJ_v0wkFInVyblmo7cDSIX6vCbyFSyj58Ck2OaYVeZmTtaJP8DEFD7DoM5otW5skmLT2lQqJ8K67zAqj8Cw89Eyr2BCpcM2DlGSYPqtdVMFPmPs0zRHZHK7CDiTGyMJxH5Y_Ix7clQa_mocVNwb1InJW74lOcwPR0cfSSwYKmpsqnl7H3qEixACihWyGlCADrM7v_UH1pEj2wFXQFkBWkLZ2uTAVeJx-qkCp_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع دولتی عراق به خبرگزاری فرانسه گفتند بغداد در پی اعلام وزیر خزانه‌داری آمریکا مبنی بر اینکه شرکت‌های تحریم‌شده ایرانی ظرف دو روز در سراسر جهان «تعطیل خواهند شد»، پروازهای شرکت‌های هواپیمایی ایران را متوقف خواهد کرد.
یکی از مقام‌های عراقی گفت: «عراق از بامداد سه‌شنبه، مطابق با تصمیم وزارت خزانه‌داری آمریکا، ممنوعیت فعالیت شرکت‌های هواپیمایی ایران را اجرا خواهد کرد.»
منبع دولتی دیگر نیز این اظهارات را تأیید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78477" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhpkShzppmWZtnNLX2Rgmz-WyGeIUoMHrN_LlmnhwzzA1qtLBMiNbD_AKQKhubYNuJZcAQ_O97EYL_JUT47WxlZ5_sfIvt_D-VZiQguJo0-LbGjYHZ5Ut5wfZUdcG011lqc3GRx8XiRLmxtdiT9kXoCyvppOZ12gC_h1CBDyfqUQt8uQfHDgAyg4sfNbwhMfF2vI-NjA9pDLcbYNPB11NYppxvehXhfLY7rsYUX9Z_hadr3IRVd9lJXSI-Hx5NG1yxnJ1I3M3imF2SktD6QtU5msXSn5heOwoxxWE8ThJDw_7bGmg8r-O6cu5My2Oh_evwSv4hyWNFL8-D42DJ_cyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز، روز دوشنبه ۳۰ شهریور به نقل از منابع آگاه گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، آخر هفته گذشته حمله به شبه‌نظامیان حوثی وابسته به جمهوری اسلامی ایران در یمن را بررسی کرده بود، اما در نهایت اواخر روز شنبه از اقدام نظامی منصرف شد.
بر اساس این گزارش، ترامپ ابتدا در جلسات چهارشنبه با مشاوران امنیت ملی متمایل به اقدام نکردن بود، اما پس از تماس تلفنی شاهزاده محمد بن سلمان، ولیعهد عربستان سعودی، در روز پنجشنبه به پنتاگون دستور داد برای حملات هوایی آماده شود. با این حال، با اکراه کاخ سفید از گسترش میدان نبرد در مقطع کنونی، تصمیم بر آن شد که فعلا از اقدام نظامی آمریکا خودداری شود.
رویترز نیز گزارش داد که ترامپ روز دوشنبه با رشاد العلیمی، رئیس شورای رهبری ریاست‌جمهوری یمن گفتگو کرده است. حوثی‌ها طی هفته‌های گذشته و در جریان تشدید درگیری‌ها، توانسته‌اند مناطق راهبردی مهمی به‌ویژه در امتداد ساحل دریای سرخ را از دولت یمن تصرف کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78476" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=IBrfuKcOwlN9yBOmtLuXtRobXZBew4c1rjvLQECOsP1DOA0yeqgJMNFfD0oNL36jipPcVXusQPFMplhZSqbiugzL62ITZeme5ZDc7BnCC_FvyWBHsJLOkxXkpTaVpR3psiB-afOgAZd630xUCe2NS7gL0oFtVCI3S9gmyW8TU2sKQKlp7OH67AOlNm30JFi8fsFLH6KRqCNgoxIXz8zWHNp9DJ0FwrdhdQTB561FzI3MC0E-50SSXif0svSG7rvQI_GRxAQlp1qd6uxH-LHSXXui6ZyIhWplKPaAhVXvXTRuFj0k81CLiQM5m1KYF7mteiNCMVls8mD7Ag-3wrVAjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=IBrfuKcOwlN9yBOmtLuXtRobXZBew4c1rjvLQECOsP1DOA0yeqgJMNFfD0oNL36jipPcVXusQPFMplhZSqbiugzL62ITZeme5ZDc7BnCC_FvyWBHsJLOkxXkpTaVpR3psiB-afOgAZd630xUCe2NS7gL0oFtVCI3S9gmyW8TU2sKQKlp7OH67AOlNm30JFi8fsFLH6KRqCNgoxIXz8zWHNp9DJ0FwrdhdQTB561FzI3MC0E-50SSXif0svSG7rvQI_GRxAQlp1qd6uxH-LHSXXui6ZyIhWplKPaAhVXvXTRuFj0k81CLiQM5m1KYF7mteiNCMVls8mD7Ag-3wrVAjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره جنگ ایران گفت: به دلیل اینکه ایرانی‌ها در حال ایجاد رعب و وحشت در کشتیرانی بین‌المللی هستند، قیمت انرژی افزایش یافته است. ما هم، طبیعتا، تلاش خواهیم کرد در برابر این اقدامات مقابله کنیم.
معاون ترامپ افزود: وقتی ما برای اطمینان از اینکه ایران سلاح هسته‌ای نخواهد داشت اقدام کردیم، آنها در واکنش، با ایجاد اختلال در کشتیرانی بین‌المللی، به این اقدام پاسخ دادند.
ونس افزود: ما، البته، تا حد امکان تلاش خواهیم کرد از جریان آزاد تجارت محافظت کنیم. این همان کاری است که نیروی دریایی ایالات متحده انجام داده است.
معاون ریاست‌جمهوری ترامپ گفت: ما همچنان شاهد عبور حجم قابل‌توجهی از نفت و گاز از تنگه هرمز هستیم، با وجود اینکه ایرانی‌ها هر روز و به‌طور مداوم برای کشتی‌ها ایجاد مزاحمت می‌کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78475" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kZgnEm1aLYO2UmvtUjmScIyxujAnFqMp17LpIGjvRW_uOEsOIvH32w1uC9RnBujmASf4_T89aCJi8PUKRz2sMbiDHsU_iabR5LbMigC_wl7C_Vgd6-2PWFzX2PnqBxeUP6FlCBffx86SHcuJ-a8RTXmkvBxYwC431sRXgO3J_CoJQDMP72othX4aXvw_73KsltLZPfdoSeACMkei-FoREFfh4d2JkWmZ3patuzI_dWtaIm_Y6WjmQW8hfQEtaPdlksPCZOqZ44HJcUkrufhOGvSVLQ--fJm4phTXOoyimhjOTcoKLdDbXKv2fX9DlhxAwGORmByfoQF5Tr_PtGV1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HCYi7SRtWaVDlxZpGjITpHt5KK9FnOei6Ovfze_nS3QiNKlcKtOSO6piK3m7aq_ikWiIIeTdx0d0QUDnnoZwz7kE45eRnguqv24aKMkJdHJnFxW9llaU7Z-6mCQI8fORheb_qk9-VnH1GCchT-YPpUXGW74kXadelNGgUOk3P3zjEgXST0zZ7T9FxETvBINLj73Z6A8t20iipgIyMSf997W_ssNgFBrrSl3HqLvVlJvQ5qNVvk9tGeiUXpabknr0OGdtyJ3akFcQIjcRREBeaXnTMucZSA-pZMkjVr8YgwdEP_-EqIWYhQAkYwokbMP_IhqnmFjx8mLJ0j5w5gWmJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tAoJ0BV28FJ3xpNFPQr6v39ocQp-Yx8ZBG4kiVKdk2Qwpw_8V8kl9uXeHFoJogwt_LLZfsg6Jnw2MXzUsHoYLAsm2VXHZd0SgA-77eR-VFnjKWXPO_nYAlFB0wokoO-b7I2Y2r_cIh-SCm5wCslNEOF4hrwGgYVTrIffyFmr98nm8OL9jMEuI1wMnE8WqaWzBKglEmLQ1u-qWylUJ_xtXvIB1C7D64voWCZcLECoFH1W13xlMsGpLN4eVZ48Li9Mxo9va7HwOn22hkNNkruCWCPm_E3_ExGUC6JwEHKkI_CthcWvRARKVOJlxfnqJOsB0nI50996uHIJvkpEHJUhVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oGHNYoj3UercLKuDVSBJdcd_HbhMmLeXzndLru8NLtU2jyD6oniwFOrLz2uV93an4Sc-2VBMiRAKvzIGVXtQ3H_Wx4CJ1F8CEA71Z0qBXqztgokEDy6NagYrYKbj3QNhlueFOwcsw-3kGEr8mGjULUC7GvEK0ZbQRoqImIc39vC2QaOxP-WRxoFPuOUzdQJ65FmbiA0yeHzBSfKspAT-BesMcnDVXw0JTh2Z3tTZrpBh5dqx3Aj4vNI5xhcC_RUFXdxGTwfGJ89sqkUDw_TMdej994tJZQlqal7OqquTZWTKB9fkswZlWlIvJYE_PPGZOac_l-J1rwgS52scHL6SNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هواگردی که توسط ارتش جمهوری اسلامی ایران در نزدیکی تنگه هرمز ساقط شده بود یک موشک فریب آمریکایی ADM-160 بوده است که به اشتباه پهپاد اوربیتر تصور شده بود.
آمریکا با استفاده از موشک MALD به دنبال شناسایی موقعیت سامانه های پدافندی ایرانی است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78471" target="_blank">📅 18:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78470">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jam1UTsWABWn9WCYCYv4fScqd-iN4zV8VBjVKsOxF9ZkqPusooYjQr9MbkSZA2MBjxW8zkeE-IUao2XjuYAmNR5PfIPKBPB4eRfj6ggOXWUPslUrQv6_g7YmUdNsxjsqsKwhKpnMTzYtdDVYugZpIgeSglMWp2CspJmoGS8XgqZJHUSJQ0frLypAb1ZcB69Fmvpwv-jwp0DNHBHpQj-E0pvuR--tQXyY3DLKzRprS8QW_jQGUKKO-9Fy87r4qjxwaJYifJEfXpL90Finc8rLhoYQmkwx3uTKuU9kiV-CrNdaAPKA1EtERXueXvlaxRbvKrSPoIt4YPj9ohI0ltVzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز دوشنبه ۳۰ شهریور، در گفتگو با شبکه خبری «سی‌ان‌بی‌سی» اعلام کرد که فشارها بر جمهوری اسلامی به بالاترین سطح رسیده است و از ۲۳ سپتامبر (اول مهر)، تمامی خطوط هواپیمایی ایران در سراسر جهان متوقف خواهند شد.
بسنت با اشاره به اقدامات جدید وزارت خزانه‌داری از جمله در حوزه‌های هواپیمایی، دریایی، ارزهای دیجیتال و طلا، تصریح کرد که طبق این تصمیم، در صورت نشستن هواپیماهای ایرانی، ارائه سوخت، خدمات فرودگاهی و فروش بلیت به آن‌ها ممنوع خواهد شد و هر نهادی که این مقررات را نقض کند، از سیستم دلاری آمریکا خارج خواهد شد.
او همچنین از برخورد با حامیان مالی و «تسهیل‌گران» منطقه‌ای و بین‌المللی این رژیم خبر داد و افزود که سه بانک از جمله دومین بانک بزرگ مصر (شعبه دبی)، سی‌امین بانک بزرگ ترکیه و دومین بانک بزرگ روسیه به دلیل انتقال میلیاردها دلار به نفع حکومت ایران تحریم شده و فعالیتشان متوقف خواهد شد.
وزیر خزانه‌داری آمریکا تاکید کرد که دولت این کشور با تمام توان در حال بستن منافذ اقتصادی حامی تهران است.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا همچنین گفت مقام‌های چین در گفت‌وگوها درباره کارزار فشار اقتصادی علیه جمهوری اسلامی حضور فعال داشته‌اند.
به گفته او، آمریکا مذاکرات مثبتی با مقام‌های مالی چین درباره رعایت تحریم‌ها علیه جمهوری اسلامی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78470" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOLLVcCY6cjQD3aelHk5dKeNP2a4aVhpdGzIGtCtZbmwV64vATYtGnqmG3AmdIH8MzSM3cMBbBp8iL3KU-vwFJVYG0ZYwzlW5HkEDZgg2oOgmyJaz7krsG-gsLZBHYZ1fHXRI6dwc1-NfjLtNEbYzDCiwvnmUyGARO4Gv0hL5hQrCvOIHqWhxJavZsl-TZo78PWui25ZyVXJDydeQeYUsD_9Y1HMLWRjglNFzGLxxaKpAy9BXKWRufb_dlT-Vb9t4rR0bkkyktycA_Fysewv4toKBsCwNMYZyKaytydaRS-hiR4gQyARjCYt5K8OVZJ_6IvTdu-H9j2N_v39q1M45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه اعلام کرد در واکنش به اقدام حکومت ایران در پلمب یک مرکز آموزش زبان فرانسه که به سفارت این کشور در تهران وابسته بود، سفیر ایران را احضار می‌کند و «اقدامات مقتضی» را انجام خواهد داد.
پاسکال کُنفاورو، سخنگوی وزارت خارجه فرانسه، روز یکشنبه، ۲۹ شهریور، در بیانیه‌ای گفت: «این حمله جدید علیه حضور فرهنگی فرانسه در ایران، پس از تعرض به دو کارمند سفارت فرانسه در ژوئیه گذشته، غیرقابل توجیه و غیرقابل قبول است.»
خبرگزاری نیمه‌رسمی تسنیم روز یکشنبه، ۲۹ شهریور گزارش داد که مقام‌های ایرانی این مرکز آموزش زبان فرانسه را بر اساس دستور قضایی دادستانی تهران تعطیل کرده‌اند.
مقام‌های ایرانی مدعی هستند که این مرکز، با وجود هشدارهای مکرر برای دریافت مجوز، سال‌ها بدون مجوز و تحت پوشش آموزش زبان‌های خارجی فعالیت می‌کرد.
روابط میان دو کشور طی سال‌های گذشته بر سر برنامه هسته‌ای ایران و بازداشت چند شهروند فرانسوی توسط جمهوری اسلامی پرتنش بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78469" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGHgpghTrXyBh0Sa50odK0RmfyKuN8z4tjzHJZBLiP05pP3gC0RNkJX-ntWBom3q4F1ttxu5KENJs3QdSyrUT9bjDhAEKRoqkwp9IJvoPqlwCfULE1WicRQ9dmzKfN6lYR7QmsJg5jk7b3Puqag2YHJZHSIH-bz_WY2iXDauxDuZV9JMlTlb-IIXXwXb8kK1ZvEB66as76WSf8eqRej1Zwni-QdydlOU1RJ7aY_dQAI5tSHSZPKuCTsL8lX-AtDUGuPOGoWhmUnun7J2u1KPlxku3_POKhYW3pM_gplMOOmkOjVfcwAoPe0D817Fmei9H1WlX3Ok3F1AGfooYmzjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»، وابسته به سپاه پاسداران، گزارش داده است سفر «محسن نقوی»، وزیر کشور پاکستان، به تهران ارتباطی با انتقال پیام یا میانجی‌گری میان جمهوری اسلامی و آمریکا ندارد؛ روایتی که با گزارش شبکه «الجزیره» درباره هدف این سفر متفاوت است.
تسنیم امروز دوشنبه ۳۰شهریور۱۴۰۵ به نقل از یک منبع مطلع نوشته است که سفر محسن نقوی به ایران در چارچوب همکاری‌های دوجانبه تهران و اسلام‌آباد انجام می‌شود و ارتباطی با مسائل میان جمهوری اسلامی و آمریکا ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78468" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVbCgfbfQ7zGU_n9XAYRizyh617lclJS7uNw-WfFcXUXdMP8-q-Z0-MXgUEyhpxq1SmWeNLuRx5a-PJVBXJINhTEUayOfUW32XnasQQ-nXPs9LLP-7aNBU56vIC4r6Wccv4OKzrCdVQd8EALrpZ_k9322SQQiHRXar4cmrFXo806Gcu1HLIdRcn27R1VpzzbUQJTcH2n20eHdSv3vIeJ5fcLGrOucOqOvzibdgZSyA7PA3jt657Mero4lBGwepI2CWEvPFJ5iWEeVX2TBmPMiz_a-CMmt2VQyRuSkbxDq6I5UZ-MgN3KgkP2bsgVWSY8-8KFFqnAnQ_FJ4mZZRvwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌های منتشر شده، امروز دوشنبه ۳۰شهریور۱۴۰۵ یک نفتکش هنگام ورود به تنگه هرمز هدف یک پرتابه ناشناس قرار گرفت و دو نفر از خدمه آن زخمی شدند.
«آسوشیتدپرس» به نقل از ارتش بریتانیا گزارش داده که این نفتکش هنگام ورود به تنگه هرمز هدف قرار گرفته و دو خدمه آن جراحات سطحی برداشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78467" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG8MBft9TdrfmyX5FVEUP2Tdo3vBQdQqqMUJofUesUZTU0SObZuMTyAC5bdNOD3rWY0PfJfBI4KjQUXJQBUiDXXWgx1qC_syEtnmzL6I5j_E5stPimg7rUR6Aiiwn-NB_XzXALrOFYTyJgS4eA29U0qJhe1d_b8_GfsoKjU5lwY6qFo-6G_V-nA50GoSXhdxIXbC1tBvtLVexVRt8lZSGzRyO87y1BuvOuvn8lBjq3S1OJTwoemxcHl0p5NUS8Yt0Dv7XJorX718GNBk-iOX1SXClojVcu1aQDu85UANbUGASugnGFbTPjA9AA9sDZiqt-1CWe9X-36vhK32J-Kvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQBppvGhbyUtx1nBHWlzd9UOmN30pgj2bmC8FpS5RV2tV8JZjVNQ3CwtUUE0krmi4jfvuwv_zEaXW7_R5IT7HdkTx-xMAOoeuUXwOp4kzx5uYCp5O-6LGFGCqimKcRhnS6ku6Ru7EgU-yjZ4cpmF5Xb0zVVDWu4nxq__qv_I2bKJHJ2P4z30liZYhTyi6Mq3bIdOAPow5YM5kNxruItHhfF56YkOWwvI6Y9cbs6AFZOhUAUYj6WptfcH04ZcGZSi9o4RlBYJM_q4eZhcf0TkQrj_D6uRrtUR-ZPwK2krXhyXE5yMlOjI74r81shUBsnOnxhYOedJGoY5mMiuibaacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPAI2Qj2iboXuK02v2ze1wNAPaz37ydJnuhtDYkTOq2SpB6_Qllaxs2MPXwe0ZNxvbzTn32ggkNq69RbuhlhNalVbigBE6RkiHgqRwz-qESqQOoEoQ_WpsqKRrn2FGhyhTstjZihjPNSMot_JmB49FTj9uHb2QAamCAQUCDgJOV2Ku64lZBOmsH84OuiMhFbT2Qk1wAeORfh-eN6d03lJTKU4mw3OxX7SuzeX3BcESdIoJqzng3_5LquGfJocRyb8aVSqlZiHgaZKewmHXm5QAyoll2dUeOBHAwBRc0u-pmn3m4QIY1d5H-qNZCY5sSTFCQM-7-7dJKFcM1b7Qa9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQCaL-Rn4ZKG8KkzscFVAo9LN3de7U7NqYxM3r1KkQbV-gSmw22VBI9XWJb-l2YUPR_c4kJxXVgCbGaX_nWjQyVmn2BU__Gk_IH-Fj86QAkekBkyd2gMXjEA2EhrO8vXEtVMqLAQpLqkHAcdh9SWny-hSVuu9zdpSW0luE3bf1dumUSJRPODm7_R8yPqE37EFRFqIPQ-wpnAUbQaDpXDgA2nupmZhBgXf_ld1GWgCghwOH6TdPE59UROqym4wIN_Qt19wyIiZ6HVTqao_JRuGBycN4TeIbTnOBytpiSrPemEaANmaYEC4B6z7F-ZCWqueqhLRZM0a9dZ_6A3htkTkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
پدر و پسری که قربانی قتل‌های زنجیره‌ای شدند.
🔸
آقای حمید حاجی‌زاده و پسر ۹ ساله‌اش کارون، نیمه شب ۳۱ شهریور ۱۳۷۷ در منزل خود در گلدشت کرمان، به اتفاق با ضربات متعدد چاقو به طرز وحشیانه‌ای به قتل رسیدند. آقای حاجی پور با ۲۷ ضربه چاقو و فرزندش کارون با ۱۰ ضربه چاقو کشته شدند.
🔸
خانواده حاجی‌زاده در تمام این سال‌ها برای روشن شدن حقیقت و پاسخگو کردن عاملان قتل حمید و کارون تلاش کرده‌اند؛ پرونده‌ای که با گذشت نزدیک به سه دهه، همچنان بدون پاسخگویی و اجرای عدالت باقی مانده است.
🔸
سرگذشت کامل حمید حاجی‌زاده و کارون را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-7014/hamid-hajizadeh-pur-hajizadeh
https://www.iranrights.org/fa/memorial/story/-7010/karun-hajizadeh-pur-hajizadeh
@IranRights</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78463" target="_blank">📅 17:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWGJuc7jfH-RnKBAmxzbCFfIyB7DgTFCTp6fRfn26U6U1TLM6wYYyFk7r_Xp2VE9OCCO5MRxYDAYpT4zfHfaI6jtplvRv1wXCrjUwLMs40MUf_uywaOcrC8t4ZIkwgaplhmNyje4vhQxRc3VsN3U-7JdkTNHqisY-AQLTekBuGthVsivekNJTr_wNFx5Rm0-vnazIcd-9TzZ2Bx10PdEIpemSdFwHh-iHQtA58V1-oKigx154M7h5DNVT6l1Sf4t5BMCFfdy4vIKrcxlJx8J1wb-YC-FiFHPsr4LiMTbHvWtg42VW3Hs09NmoHp-0aLuqyNElgs0NM-oyBY7BDlRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز آمار ایران روز یکشنبه ۲۹ شهریور نرخ رشد اقتصادی سه ماه ابتدایی سال جاری را منفی ۱۰.۱ درصد اعلام کرد.
بر اساس گزارش این مرکز که در خبرگزاری جمهوری اسلامی، ایرنا، بازتاب یافته است، تولید ناخالص داخلی کشور در این سه ماه ۲۱ هزار و ۷۹۵ میلیارد ریال بوده که نسبت به مدت مشابه سال قبل که ۲۴ هزار و ۲۵۵ میلیارد ریال بوده، بیش از ده درصد کمتر شده است.
کاهش قابل توجه رشد اقتصادی ایران در حالی است که نرخ رشد تورم در کشور نیز به شدت افزایش یافته و بر اساس آخرین آمار اعلام‌شده به حدود ۸۰ درصد رسیده است.
از سوی دیگر ارزش پول ملی ایران نیز در شهریور ماه به شکل مداوم کم شد و قیمت دلار آمریکا رکوردهای تازه‌ای را ثبت کرد و از سوی دیگر مقام‌های ارشد دولت نیز از محدودیت شدید در صادرات و واردت و کسری انرژی خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78462" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78461">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgNbnnBTLgHxj4Dpj51vQq1wpJd9lWgPmb2IMxnO0ioF2valRDBtQWrdD65_c9KJgmUxnLOyydTEDHobkJiLaz2XHShPs9h6ctJzsWAtI-XLr9xHUt6GoKXSID3M77wLlZASCfihMiBoy4-nmgCVFORLYxJ9NJ8WXENUncEA6eloEm_k4x1uiWnW7Gl3CIuxMejHqkQrB2-fDddWNSgMgjqxVLMT6akA1DLlvSgC29xLHQF9-Rr2cVHIKh4QRQWSsdSvkekl4RrfRshCzP8B4dPZfGuQ1hC5ez-GWvuslOl4CS3TBhLVIkd1qJLWCjbmgJyXgIu_WrQgXbRxdyp_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید موسی شبیری زنجانی، از مراجع تقلید شیعه، یک‌شنبه ۳۰ شهریور در قم درگذشت. خبرگزاری فارس گزارش داد او از روز جمعه به دلیل خون‌ریزی معده و عارضه ریوی در بیمارستان بستری بود.
شبیری زنجانی متولد ۱۱ اسفند ۱۳۰۶ بود و در سال ۱۳۷۳، پس از درگذشت محمدعلی اراکی، از سوی جامعه مدرسین حوزه علمیه قم به عنوان یکی از هفت مرجع تقلید مورد تایید حکومت معرفی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78461" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78460">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=hBA5--j9WUDI9c-MIR-3Fo0P1-7hJjjy6T0ZD9UgQwlVEB6yLFm6IO0RZKLsWGtKufHbnfITqSsCkJ7i4gPy10G5al6JQTFzEZD1iOIIv7KcYu0g-s_XEUWKgC6dXrZnsRPCA3Mzvrqmlz_cAwLXNPUR8IKTrKteijk8EmYqZqvpt7blidjbd3icLuJmDO5WiQj2x_AOIneySv9EJzdlmhodoCjyWWdMOg5aYRB5D7g32TkO2XyT2DHgqMvScXmx0Xh8w-4foYvy_ENE961cvSawTHsw4Y_GBHqyHyY0vRxN16x3dQK6J71Fs_Aq091AWS1ofRab2s3UxZsOlYM16w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=hBA5--j9WUDI9c-MIR-3Fo0P1-7hJjjy6T0ZD9UgQwlVEB6yLFm6IO0RZKLsWGtKufHbnfITqSsCkJ7i4gPy10G5al6JQTFzEZD1iOIIv7KcYu0g-s_XEUWKgC6dXrZnsRPCA3Mzvrqmlz_cAwLXNPUR8IKTrKteijk8EmYqZqvpt7blidjbd3icLuJmDO5WiQj2x_AOIneySv9EJzdlmhodoCjyWWdMOg5aYRB5D7g32TkO2XyT2DHgqMvScXmx0Xh8w-4foYvy_ENE961cvSawTHsw4Y_GBHqyHyY0vRxN16x3dQK6J71Fs_Aq091AWS1ofRab2s3UxZsOlYM16w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: ۲۹ شهریور، ساعت ۱۷:۳۰، اربیل عراق
هم‌زمان:
رویترز به نقل از منابع امنیتی عراق اعلام کرد که سیستم پدافند هوایی، یک پهپاد را در نزدیکی فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق رهگیری و سرنگون کرده است.
@
VahidOnLive
آپدیت:
نیروهای ضدتروریسم اقلیم کردستان می‌گویند که صدای انفجار شنیده شده در نزدیکی فرودگاه اربیل ناشی از «تمرینات نظامی و فعالیت‌های امنیتی» بود و «هیچ خطری ایجاد نمی‌کنند.»
این فرودگاه میزبان نیروهای ائتلاف به رهبری آمریکا در اقلیم کردستان عراق است.
رسانه‌های محلی کرد گزارش دادند که ائتلاف به رهبری آمریکا مهماتی را در این منطقه منهدم کرده است.
یکی از خبرنگاران خبرگزاری فرانسه گزارش داد که شاهد برخاستن دودی خاکستری از نزدیکی فرودگاه بوده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/78460" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvoiSalfgLm9PK2zdT5BKYpXQQEHC9OpryrQkklwBJaKcN83JrRVtz7OG3nsd90ndL4XlUzCrnj3wc1QZfJAENPQKx7HJ3dCC36dso7NCEeAMJaqE0rxm9Cx5e11QuFy3jYeX4g8jpy4ZDbpW0ifK3nWvQ_xepZqqrucyeWnhZFl_mAw93craBAa9lnQijm-2b4IJW_9UJgyaW_DO5-iG0nK-A9yGRBhxaiPFmM_j3DEFD7z5-rfIcNh03pH1NkMupNcXtVyd1ZL3IDNbivcUPIP9O-0uhgu8p78TF-Cj3_Gg8n-vth-PTAs3Crnv9_kp0wexzvk13ctXxmgE7880g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز یکشنبه ۲۹ شهریور ماه در گفت‌وگو با شبکه خبری فاکس اعلام کرد که در حال تصمیم‌گیری درباره ایران است و «در آینده نزدیک اتفاقات بسیار بزرگی» درباره ایران رخ خواهد داد.
ترامپ گفت گزینه‌های فعلی روی میز شامل «محو کردن ایران»، «رها کردن آن برای فرسایش اقتصادی» یا «رسیدن به یک توافق» است.
رئیس‌جمهوری آمریکا همچنین گفت: «سؤال من این است که چه زمانی و آیا قرار است کل ایران را منفجر کنم» و افزود: «بهتر است آنها رفتار خود را اصلاح کنند.»
ترامپ گفت برای دیدار با مسعود پزشکیان در حاشیه نشست مجمع عمومی سازمان ملل متحد در این هفته نیز آمادگی دارد.
او در ادامه گفت برخی مقام‌های ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به دستیابی به توافق باشند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/78459" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_OTQVcDmyfInizquG8xtYhEnZfnx_SRITAV6XhOamYg35DKlC1ZywzWnZjVFkIejrcET9kt9wKlHIROyCQrXp8ovNZhwJrQ8DR0c8wM_GLGMoU7d9LanMLpl8uhhApR6uygKhrczRpw0nYgFFIc5r2GnuW9-_PpPWQ2nPKHlN9IqRYdOouau01JHDOBzpCIfGPvfNvlWebABfx7voc2JC35GEUtUl5lxuqd4kxddDgMQC3KYsjoAJylprzxTJMC9XLASL4qgjfjZpjjJKyxPGbWtuwH31q8JosQK46Y0J1Rcq-8NG8uzI5eU33YRhgzGLQuAQwX6T0qBxVQ_9XuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا با انتشار بیانیه‌ای نوشت به اطلاعاتی دست یافته که با آمریکا با حمایت برخی کشورهای منطقه، برای ازسرگیری حمله به ایران آماده می‌شود.
در این بیانیه آمده است: «براساس اطلاعات دریافتی، آمریکا بار دیگر تصمیم گرفته با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران را از سر بگیرد.»
قرارگاه خاتم اطلاعات بیشتری درباره شرکت‌کنندگان و یا کشور اروپایی میزبان ارائه نکرده است.
این نهاد عالی نظامی به کشورهای منطقه هشدار داد که اگر با حمله آمریکا «همسو» شوند، «همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.»
قرارگاه مرکزی خاتم‌الانبیا همچنین به آمریکا هشدار داد در صورت حمله، «تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78458" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SvTE5y2hpS3xSwniJXgDOC0TwlFKdk2XXFs5_RLLjpwwxgytdkU97-jTO5bV4l4_79QPahzPCHFI7JLzcifQutoG470eacN9hNKyMmy4gWNVf6blKxh0OngZEgCqcXEFCj9TSM-qvhFyR9REOrIGzxnGRNBdhDWcU8lPxiCeDLz0Rs1VX6aWPm0nWOkryIYvPuvoK-zCRZar_6jISCd1A6kjU-iT_z0s9Ra9_JdtrDNL9Febr6tYS5S47nbpkE6QGUMa2_t4Gvu42-b7F9luf-Bb-WLPrQoevWzmarmEiXg0oJnZcIy0UwTj_jlhdyVpR_2T-B3Un2FZTeh2a3PDAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی از جریان‌هایی انتقاد کرده است که با رد هرگونه تعامل و دیپلماسی، ایران را به‌سوی «فرسایش و جنگ بی‌پایان» می‌برند. او هم‌زمان تایید کرد که تهران شروط و پیام‌های خود را از طریق میانجی‌ها به آمریکا منتقل کرده است.
@
VahidHeadline
محمدباقر قالیباف روز یک‌شنبه، ۲۹ شهریورماه در نطق پیش از دستور خود گفت: «انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده... و تا زمانی که این شروط محقق نشده و حقوق حقه‌ ملت ایران به رسمیت شناخته نشود و تعهدات آمریکایی‌ها اجرا نشود، هیچ روزنه‌ای برای بازگشت به شرایط پیشین مذاکره و باز شدن تنگه‌ هرمز وجود نخواهد داشت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78457" target="_blank">📅 16:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcbfpjDANoUH3_uc39WqlukBfDVGS7Vh15d1YI-hET-Te6Xai6esizTgfnDlf6qNqoaPl_F40zcQGg94-MHhMjt5lcdsUEu3tNXFfzusy9_diGcbQvEd7mTnS6BdMp5ubHvx62A1uhUCD9TCN5y3K3BLNLwQut0AJUpNokTTlqszjzbSS2SefGMCNYv0Mer4Ipe1Qpd5gRv3GI6BZYRwN8y0rBeU0Hw1Cedoh0sXrQzCyiCY6dIz4KyiRvFhEjfoIAiwjebfgaMI3oLRXs8UQItx2kxy6-Bd9M4hbbBRF3ErCCgAa_pl85vu9gmLWXZ1Gq2jeJBzqhPj7PfViQpSeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه یک دادگاه تجدیدنظر استان البرز حکم مجموعا ۱۸ سال زندان «منوچهر بختیاری»، پدر دادخواه پویا بختیاری، از جان‌باختگان اعتراضات آبان ۱۳۹۸، را تایید کرده است.
براساس رای صادرشده، بختیاری با اتهام «تشکیل و اداره گروه در فضای مجازی با هدف برهم‌زدن امنیت کشور» به ۱۰ سال زندان، با اتهام «اجتماع و تبانی برای ارتکاب جرایم علیه امنیت کشور از طریق همکاری با یکی از گروه‌های مخالف نظام» به پنج سال زندان، با اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به دو سال و با اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم شده است.
تایید این حکم کمتر از سه هفته پس از آن صورت می‌گیرد که شعبه اول دادگاه انقلاب بندرعباس، منوچهر بختیاری را در پرونده‌ای جداگانه به ۱۰ سال زندان دیگر محکوم کرد.
در پرونده بندرعباس، او‌ با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «تحریک مردم به جنگ و کشتار» و «ارسال فیلم به شبکه‌های مجازی بیگانه» روبه‌رو شده است. این پرونده با شکایت دادستان بندرعباس تشکیل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78456" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=PDqMIUI6WQQm9vs2McunCTwbJlNt3ZRYEw7IP4kuZ2qNYLWL0xn-Q2y6Q3oUpCu-7ETt7Z4yj2QIW8cEW9zYokSDr-m9xtTKWD7B0nehxMQxlR2vtSLonFz4TeemuTDfJXxeQT7jmw-ybB6_VN9HrKVCFevYP1E4tB_97VY2-qjaYZtc7gzL2EkNo06xnEn3k_xcy-sYcnZ1GSLfPPwLIEu8-UJnYJaHJ5-ISFQV1ynaYQFNH5dzANRxj-XHL-m3Xdnj8Nm5zl68oaRxPLqYCC_6ebb4SWuNmI-HufU3AC70UaydoCy3oO137MW8g_gP4IE4F4--9LuIEMYPnDt3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=PDqMIUI6WQQm9vs2McunCTwbJlNt3ZRYEw7IP4kuZ2qNYLWL0xn-Q2y6Q3oUpCu-7ETt7Z4yj2QIW8cEW9zYokSDr-m9xtTKWD7B0nehxMQxlR2vtSLonFz4TeemuTDfJXxeQT7jmw-ybB6_VN9HrKVCFevYP1E4tB_97VY2-qjaYZtc7gzL2EkNo06xnEn3k_xcy-sYcnZ1GSLfPPwLIEu8-UJnYJaHJ5-ISFQV1ynaYQFNH5dzANRxj-XHL-m3Xdnj8Nm5zl68oaRxPLqYCC_6ebb4SWuNmI-HufU3AC70UaydoCy3oO137MW8g_gP4IE4F4--9LuIEMYPnDt3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«نجمه امینی»، دانشجوی حسابداری و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در پیامی صوتی از زندان وکیل‌آباد مشهد اعلام کرده است که دادگاه انقلاب  روز ۲۵ شهریور برای او حکم اعدام صادر کرده است.
او از سازمان ملل متحد، وکلا، فعالان مدنی و نهادهای حقوق‌بشری خواسته است پرونده‌اش را بررسی کنند و برای برخورداری او از حق دادرسی عادلانه اقدام کنند.
هرانا پیش‌تر نوشته بود که او با اتهام‌های «اجتماع و تبانی» و «توهین به مقدسات و ائمه» محاکمه شده است.
نجمه امینی روز ۱۱ بهمن ۱۴۰۴، هم‌زمان با اعتراضات سراسری دی‌ماه، در پاساژ فردوسی مشهد بازداشت شد.
امینی ۲۳ ساله، دانشجوی رشته حسابداری و ساکن مشهد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78455" target="_blank">📅 15:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onOHx2EpFGdtHkf9j9XYF14mmb6iIgZo6PIvJjib-QlRSmcUtxD0CiGZNmwz74eB7DKfkh1LdQ42dZLvLT_JVo5S2iNwkao41c36_El3mO6cFUFTPbCliHO-fn5Di9_v_qieGTvVjfj-lMmdpY-QlM0OFY18ts8fXDExJkTZS6Ns8joUj57e4P0N0Heg3ajtBXriCTx4v_g1zybopJ3I5MJfFPBXCE6Yrtlv16HEdy5A0DRbfYuFNXCxUfcL0ejUaAPd369tMR1X2-4xn_lSoV67NBTaBKe2oQpVraedoIBVNCVys56JTcm1TrF7PoJBnXa2rm-qL80OqUOWD2XifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی جمهوری اسلامی، شامگاه شنبه ۲۸ شهریورماه در شبکه اجتماعی ایکس نوشت ۷ شرط ایران برای آغاز «هر مذاکره‌ای» به دولت آمریکا اعلام شده است.
رضایی در این پیام نوشت: «پیام تهران روشن و بدون ابهام است؛ اگر واشنگتن می‌خواهد از مخمصه‌ای که خود ساخته خارج شود و بیش از این در آن گرفتار نشود، راهی جز پذیرش حقوق و شروط ایران ندارد.»
ساعاتی پیش از انتشار این پیام، رسانه‌های دولتی ایران به نقل از گفتگوی محسن رضایی با شبکه الجزیر گزارش کردند، ارتباط میان تهران و واشنگتن به وسیله میانجی‌گران قطری و پاکستانی ادامه دارد و شروط تهران برای بازگشت به مذاکرات به کاخ سفید اعلام شده است.
رضایی با اعلام آنکه تهران منتظر پاسخ واشنگتن است گفته بود، پایان دادن به جنگ در همه جبهه‌ها، آزادسازی دارایی‌های مسدود شده ایران و پایان محاصره دریایی شروط ایران برای آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78454" target="_blank">📅 23:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EyKunlhOsNf-5Dc1jpjMdzA5ZtjZz1kg2Rfp-mBrH9zgab_YYEVlgvOFITbY4AiZidbmU9QO08JU3mg_Jc4RztGd0pNIOzQ8uiqZYjD7019r4N8Zrtsb0sfRtpbniD8x95pgOaUBkasv-ujqxcASeE2FT7AgpoarK-HCFCmUqNEBTuzBfgrDv5zm1y4FcRJSCeRT0XEbPNaZEUylWFk9Sh2hnWAbZPoo1-un3A79pwSuw6UlXXjcJUAceB-Z_8C_GnJIzKCy_n0ZTE0aDnu3iwL7Isyi0enW9oxAwN72E2bKQL-LJu6-_2-I8pBEaDQTzJez4yrqDVHDvugvJQ6xlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکان فیدان، وزیر خارجه ترکیه، گفت در پی حملات حوثی‌ها، عربستان سعودی ممکن است در برخی زمینه‌های فنی نیازهای نظامی داشته باشد و ترکیه برای پاسخ به این نیازها در چارچوب «ائتلاف دفاعی مکه» با عربستان سعودی و پاکستان مشکلی ندارد.
فیدان شنبه ۲۸ شهریور در گفت‌وگو با شبکه «ان‌تی‌وی ترکیه» گفت حملات به تمامیت ارضی و حاکمیت عربستان سعودی جدی است و ترکیه در چارچوب توافق میان سه کشور در کنار عربستان سعودی قرار دارد.
او همچنین گفت عربستان سعودی تمایلی به ورود به جنگ آمریکا و جمهوری اسلامی ندارد و کشاندن این کشور به این درگیری «غیرقابل قبول» است.
فیدان در پاسخ به پرسشی درباره ارزیابی برخی منابع اسرائیلی و ایرانی مبنی بر اینکه «ائتلاف مکه» تنها روی کاغذ است، گفت: «ما به این حرف‌ها می‌خندیم. ائتلاف مکه به یک سازوکار بسیار تاثیرگذار و تغییردهنده معادلات تبدیل خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78453" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/205953bb15.mp4?token=LJYNLH7Z3Rf-6Y1MD9Tvth1PtFqZhionpYeSZQr_jtcUEMK525W-skQya2LTStA1rurpcU4pLhIeOYSIwYoY-xjwaZhsuB2SSj-KTnsXAl7lTnQob-UngY8ACgFOGfq0ceoDdLsNDyHDO-HOgwuSgvSW8T_wp3U5aQmBtAdNBW4jgCotLuY21WTYjgqb42zKTHZTHwjJ7r3ICVeed8lZsZ8hzdLv4Owh4o_xJLix4-DlCiwkOImLcD318FuQqImWILlHYJyBATwqIRuYj2DK5lWFacNb5CZoufyP_j82J3NHjx1_h5MDSyVE7oV2J6c2zUcIAwJMgitmWiS92nja3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/205953bb15.mp4?token=LJYNLH7Z3Rf-6Y1MD9Tvth1PtFqZhionpYeSZQr_jtcUEMK525W-skQya2LTStA1rurpcU4pLhIeOYSIwYoY-xjwaZhsuB2SSj-KTnsXAl7lTnQob-UngY8ACgFOGfq0ceoDdLsNDyHDO-HOgwuSgvSW8T_wp3U5aQmBtAdNBW4jgCotLuY21WTYjgqb42zKTHZTHwjJ7r3ICVeed8lZsZ8hzdLv4Owh4o_xJLix4-DlCiwkOImLcD318FuQqImWILlHYJyBATwqIRuYj2DK5lWFacNb5CZoufyP_j82J3NHjx1_h5MDSyVE7oV2J6c2zUcIAwJMgitmWiS92nja3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، روز شنبه ۲۸ شهریور، در پیامی ویدیویی خطاب به شرکت‌کنندگان در «مجمع گفتگوی جهانی ۲۰۲۶» به میزبانی انجمن سیاست خارجی اندونزی، با انتقاد از رویکردهای مداخله‌جویانه در خاورمیانه تاکید کرد که دهه‌ها حضور و فشار نظامی نه‌تنها کمکی به ثبات نکرده، بلکه چرخه‌ای بی‌پایان از تنش را رقم زده است.
عراقچی گفت، ریشه بحران‌های منطقه را باید در یک حقیقت تلخ جست‌وجو کرد؛ چرا که سال‌ها مداخله خارجی، فشارهای همه‌جانبه نظامی و درگیری‌های پی‌درپی اثبات کرده است که مداخله نظامی امنیت نمی‌آفریند و اعمال فشار و زورگویی هرگز به صلح ختم نمی‌شود.
عراقچی در ادامه این سخنرانی ویدیویی خاطرنشان کرد که در شرایط کنونی، جنگ به‌جای آنکه آخرین راه‌حل باشد، عملا به ابزاری معمول در روابط بین‌الملل تبدیل شده است. رویکردی که نتیجه‌ای جز عادی‌سازی خشونت و تداوم الگوی درگیری و تقابل دائمی در منطقه به همراه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78452" target="_blank">📅 16:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INqU2m7y5rdIRFXWhA_dnDX_QOw0mGOf-G4yzmDYpgdbvsVUXngmxE51jLl4LRwvoK-47bQqzus24o2bQA1RCMnNh3lMQwul0wTciYgqV1MT8uHYZAiXcZOy-TaBvw486BEcAN3K4YAPxZMrCnMesPLOmbnLZp1ZbTfr1V6a47ooaIXIBpPgQPZaaktdzbio7oQkI6MAo-6u5AXgYGpbBD815s4J7P1gM5EHOoEwcphK5TuwWZQzH-95yUl_WS7YX3fqkB6baWUmQX9HaTJiFwvWXBG4Wb3w0HhT63b7S71qTkfeAERvwRvcNTo9XELyOaJaNRbTsymWT2Kob6ugIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است. دادستانی مدعی است که در این رقابت «موازین قانونی و شرعی رعایت نشده بود».
مسابقه دو ۱۰ کیلومتری بامداد جمعه ۲۷ شهریور با حضور زنان و مردان برگزار شد. انتشار تصاویر شماری از شرکت‌کنندگان زن بدون حجاب، رقابت را به موضوع بحث در شبکه‌های اجتماعی تبدیل کرد.
بنابر گزارش خبرگزاری فارس، برگزارکنندگان اعلام کرده‌اند مسابقه با مجوز وزارت کشور و هیئت دوومیدانی استان تهران انجام شده است.
هیئت دوومیدانی تهران گفته پیش از آغاز رقابت از شرکت‌کنندگان تعهد کتبی برای رعایت «حجاب و شئونات اسلامی» گرفته شده بود.
حبیب ستوده‌نژاد، مدیرکل ورزش استان تهران، به خبرگزاری تسنیم گفت مجوز رویداد از شورای تأمین استان صادر شده بود و با ورزشکارانی که «خاطی» شناخته شوند برخورد قانونی و انضباطی می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78451" target="_blank">📅 16:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7ptV4Egk5u517wudCA1mnrMENROvN8mdNiQGemEytYAQ4LOt4pUGb7ZXI2EAKlkuyUTtbxOpeCey0uP9HQ3QeGyONz9jJPytLqJ308XJmlyBXu5pHJbQZZwFW89er2fogF5vj0-_3i8TrArq6xPOkWJceq9bvtw_3WAZoPbs-Omi39mkSrPImIvMIUmHFrtDiDK3BJ0kazZDMaE1zNOV5WlxCWUQ7HNxeNRiP9ZQTbuE5qnHoXZdXH_f6b9N_8pQbiIqcWuAZEA0b4-GTFv0bGfNf7geUdhIvd-L2Cv0_C8CvMbuoKe6H40xK6hlr3IWxig1pn6B-kw1lf6724IuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد تنظیم مقررات و نظارت بانکی ترکیه مجوز فعالیت شعبه «بانک ملت» ایران در استانبول را لغو کرده است؛ تصمیمی که پس از توقف پروازهای شرکت هواپیمایی ماهان میان ایران و ترکیه و مداخله نهاد ناظر در مدیریت یک بانک تحریم‌شده دیگر اتخاذ می‌شود.
براساس اطلاعیه منتشر شده در روزنامه رسمی ترکیه، هیات نظارت بانکی این کشور روز جمعه ۲۷ شهریور ۱۴۰۵ لغو مجوز «شعبه مرکزی ترکیه بانک ملت مستقر در استانبول» را تصویب کرده است. این تصمیم روز شنبه ۲۸ شهریور در روزنامه رسمی ترکیه منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78450" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9dj_TGOjTGEKAhBIkrQi4AzmvnBKRzQecux4vAnUzFBe1vpEDhA6J4SeJaXuvJx40L-PywkFi_hkkV2GbC5jqPaZTr_NjuHSLJntkNkllrtGLe_2N9amZH97G_L4_lSztjokwOfzerbh9XaLcorBq8zxUwjupWXEO-g--Bz9pPix9F9lqxwR-elER2VoFjYdItaA2dwW4GsgmIu9e43ScP4dWjzO0kqn3vwWsgD1WKQaGHpena1N-Zy2Q5EnkSew7YCwh2y3u2divwnRkQDqiQMYADPzZEBc9TtHgI-LkGQ7QmSOtRLZEYigO8CR29Y3uiS5tCzq9qeFcKUCSZfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز جمعه ۲۷ شهریور و اندکی پس از تایید کنگره در هفته جاری، لایحه‌ای را امضا کرد که مجوز اعمال تحریم‌های جدیدی را برای تحت فشار قرار دادن روسیه بر سر جنگ در اوکراین صادر می‌کند.
این قانون همچنین تحریم‌های مرتبط با ایران را نیز تمدید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78449" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWglF3UIdRoUVMf8P96Nsp72i4hBK3uj9ZFrSbXU4g-Snr9R2oOqCil0fC7S8oFvg4-csVV0QqSMlJHWrvKYa6LIeT1v5t3qgmlXZgyPaeZvFMLVoEtPhSfTqFn3M4K32ATgNjzJ_NRZs08SzJ2x6OS56jKNgQ2ZA-B1whLm8qex2jvOCYoVqIO8WEQQO5c_hFobq3t8_3nfHTB4xU0gyXQtM1aZmdiJK7z6j3mJkzHRGTk4RYpY4vLhuoqiZ79zKYR_lZqg28MF89uNyIHqHYtkTLe6EsUy8JsC89LJ3tv-8U9wtJNYffL-5dw0VjjjcCpZCLvPXE9IXX0-cZBq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اعدام «حسین پدران» با اتهام «جاسوسی و همکاری اطلاعاتی به نفع اسرائیل» خبر داده است.
براساس گزارش رسانه‌های حکومتی در روز شنبه ۲۸ شهریور ۱۴۰۵، حکم اعدام پدران پس از رد فرجام‌خواهی و تایید در دیوان عالی کشور اجرا شده است. محل و زمان دقیق اجرای حکم اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78448" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiGn0PahqbRBexEaBt8Vetnn6VoymhOlhEJOfLSKG3kee34RlLAW9ZB6UmP1nlyM-hoRBRoBjPvE-bmVcFVKs7u5ZpIdsHQq_k75yQqBFMkOkTnRkgy7GWcYsbB7ANbwjblhFv93-wx6Ww5SKTn174S3upxW3YmDUuUi9QFUEZQ3Lq2Oly0MQ6GsCu9ebKQt-rPhVhJlfmBjhlbP9b5pHba3vIkV6zOTnxTg88UqiURD0S72rKunpf_LNvNrM12VXtcQHa_WWkOA4_jwnp8UM9MaUDeV2lgxbEtfuzAUFSOIdvWVIwDOSeGICHJM9W-_96wpMy8zpPKuNexSJXRpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌سوشال اعلام کرد آمریکا با دانمارک و گرینلند به توافقی دست یافته است که کنترل دایمی امنیت و تمامی نیازهای دیگر در گرینلند را در اختیار آمریکا قرار می‌دهد و به تمامی نگرانی‌های متعدد ایالات‌متحده رسیدگی می‌کند. او گفت این توافق هیچ هزینه‌ای برای آمریکا نخواهد داشت.
دفتر نخست‌وزیری دانمارک نیز اعلام کرد انتظار می‌رود که گرینلند، دانمارک و آمریکا هفته آینده توافقی را برای تقویت امنیت در منطقه قطب شمال و اقیانوس اطلس شمالی امضا کنند.
ترامپ گفت: «از این پس هیچ دشمنی از سوی آمریکا نمی‌تواند بدون تایید کتبی صریح ما در گرینلند پایگاه ایجاد کند، حضور نظامی داشته باشد یا سرمایه‌گذاری‌های حساس انجام دهد.»
پیت هگست، وزیر جنگ آمریکا، نیز گفت: «ما بلافاصله روند حضور نظامی گسترده در بخش مناسبی از گرینلند را آغاز خواهیم کرد؛ بخش‌های مناسب زیادی برای این منظور وجود دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78447" target="_blank">📅 04:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=MHFjOY0ZB2xZZG7LvueWyjA1zfrB8ToPm8c5cHDq1ySRP47yGQ2xGQM3WA9SBu-JJxLYDuajBAbeCj499Cdbvs2Gdl5i_tgaIdYpdBsvkDT0k703iJYM9nxIOpBjThSlpbpJxeGFPugmq0R0-zUJDCm9zKB5yvt_T3G6e9kl7lIcL_6PgBmrINDDuwon46HgUprSDZjFRwboR6HCaVUJijUUcTiJq67rIa-R1jxjiOONKILR97ofRz2UCnlkO6wAEU7tNAYM1Oytf0Gqgm-dYhI6f2rQw0C926aceIXMe_xQJxv5-jAh4CtPN4tLa9cxlhI2Oou-1EXQaz1W6568dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=MHFjOY0ZB2xZZG7LvueWyjA1zfrB8ToPm8c5cHDq1ySRP47yGQ2xGQM3WA9SBu-JJxLYDuajBAbeCj499Cdbvs2Gdl5i_tgaIdYpdBsvkDT0k703iJYM9nxIOpBjThSlpbpJxeGFPugmq0R0-zUJDCm9zKB5yvt_T3G6e9kl7lIcL_6PgBmrINDDuwon46HgUprSDZjFRwboR6HCaVUJijUUcTiJq67rIa-R1jxjiOONKILR97ofRz2UCnlkO6wAEU7tNAYM1Oytf0Gqgm-dYhI6f2rQw0C926aceIXMe_xQJxv5-jAh4CtPN4tLa9cxlhI2Oou-1EXQaz1W6568dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۲۷ شهریور در گفتگو با خبرنگاران در کاخ سفید گفت جلوگیری از دستیابی ایران به سلاح هسته‌ای موضوعی است که به آن «بسیار افتخار» می‌کند و ایران دیگر سلاح هسته‌ای نخواهد داشت.
ترامپ با اشاره به افزایش هزینه سوخت گفت تحقق این هدف ممکن است مستلزم آن باشد که مردم برای مدتی هزینه بیشتری بپردازند.
او افزود: «اگر مردم می‌توانستند بین قیمت پایین‌تر بنزین و اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی بدهند، فکر می‌کنم نتیجه با اختلاف بسیار زیادی روشن بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.»
رئیس‌جمهوری آمریکا همچنین گفت انتظار دارد جنگ با ایران «به‌زودی» پایان یابد و پیش‌بینی کرد پس از پایان جنگ، قیمت بنزین به سطح پیش از درگیری بازگردد و «شاید حتی پایین‌تر» برود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78446" target="_blank">📅 04:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=YSSGXAkzgqdSzf-x0Iul5NaX7251XQ6wEvk6_4uNnDNi8zmKZgU4YaiDG7YKyfmkm5CWC5SUabJRMz2zW9BH0TJvWWaAejjphfH4JCde5too68zvWIfmkCdmg0askd5OOvqSiY_begHz_20gnNXAsbOvlh-kOUSEYdyR7GAtjytPZYup5qZD2tMtsAs0bo8hSQkH-O7xrLlifHoyPgjFY3GAwy0L6pKokXGU508HUhGBp-SHAQeW1aAfsv5wDfQ_q5lbp92Ux8x5mo5OMytKHbSN_ZA4mShF1dL2DYY5sunknIYrdaruFlfn9azl3v4LtPoIEsNqF4kdVE1iis2Jvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=YSSGXAkzgqdSzf-x0Iul5NaX7251XQ6wEvk6_4uNnDNi8zmKZgU4YaiDG7YKyfmkm5CWC5SUabJRMz2zW9BH0TJvWWaAejjphfH4JCde5too68zvWIfmkCdmg0askd5OOvqSiY_begHz_20gnNXAsbOvlh-kOUSEYdyR7GAtjytPZYup5qZD2tMtsAs0bo8hSQkH-O7xrLlifHoyPgjFY3GAwy0L6pKokXGU508HUhGBp-SHAQeW1aAfsv5wDfQ_q5lbp92Ux8x5mo5OMytKHbSN_ZA4mShF1dL2DYY5sunknIYrdaruFlfn9azl3v4LtPoIEsNqF4kdVE1iis2Jvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HC_qz3VZeAstwqH2RoDHArdUOXbu9q2OnRuYP_iSBCQHt_i_H3gg5bTIkYmXegfVmCmn-C6bAgeZbK8Du5pR8-hBodpxEw23TQOSJEmkeqoKKFZVLjl73lgrNcJIrTHZrFySzJ5xqIPnmFjN2o65nu3tahtRCWvO-yRjqSPsEksD6ov6cVR-dQJ8e1gUHGWnggRBWQ7zcyBHPIX26Jr6qoID3X-hUM6RBIA9pQZ76LS0WZF6SiSjx0QJ61MT6bPgeICSCjchB-M9YJC7OtInalIH9kOB94bNbsZlpi5dX9UHpg8Qmv-D1IbfGxaDSrMnu1RZwrF3sZyJLYUEi1Q0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lyyuFxf8mD_9DFI-gTsPKvc3aCwv-h-_yRtq_vK_GhR__MN-UIUaI_MAAN6rKVxEmry2hr--KhTD8CQNrRvci4OkWDhO3cKo5Y7Dxo_jw9TxDZAPLdsZi6-rxlBbgfNwBsFSDpu37hvI2brpVEdXT-XgEJMabi9cyUtE47OqPlmgXWaDrJcquphVzMg_o2GKmdvLYfoiZn8OTOlOvunlH347FAFkYFXDVNpFd_ZQb6YqAzOXoBxXXUZWkohd9J4W3v0smiokd8JNuYC9cUmgwgzze8B1kI3laa1FrAPdAvQuwAtY1wL58P5uUTnIImAT5rTlafK1WqCMzLlP4kj6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jFrz7EzFGjbseYoj3tAl2lXVXp5P8LS-V-vGK9818OyGWzKG-S398TcIcRHe2wO_-rF9WbxbA0TPaqjCtPbX_lDMx7rEBB12WAntEtsyNjw09mGX8k-FjJCdr_RUKsgx4BMVGzWLkeF9iBxEABuRtymQqEYyifL-B482vO_vEbB4nFZZ7SysJLHyJf2LonxOPtRqYhbLtV_hsLEJbcYCFMvBV8FR_K9vwYllWSG9qJGYSEEXxpCteo51ZZ-dr3FqWMBNEOGHqV1d4_jva-FUdBWIrkmCrsinI7pPxLAVv82_Bz8y287_iP1XXcVhQfx6Q8VEazHQ17WaswnUqpod_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c2XQRaXA1sDqWK3bqitXyYDLDXe6kI2xxVQKPu3RkrVeT8kVFuccZz7LboCNs1PWSXk3z94z_lgQJsO_A_0z4SA_INbnISE0bLCvWg5WyC2eXUGbm0oh_szMOWEOrbrvVaXqqMW-BTAj9zPmLuWqqKIveRpyDq3ZADGU5XPn12O4VdHzYHQYQr2a80QN6DHTOFp7RtsQdGcPfCLBGSeWoannQiV-livlLevVocl2SBWPKJZAD8H1BJHunKnv01HR-Sq0J00P8AFSR5q-Jxy_80OdS4gaLrCaR3vSBYqHY8Ey8NmBoLaB97Yd_Q6fhlx8xj0N73A5gUUau8Ne7acRfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qjxpZ7ETD5gJEBPOZ-bYf09zajHosrkXs8Cq4key1_DfmQ_dU-7LWz1bSnhEQ2bP4I-p7bw5-McwpNg9O8VhUco2IGzJTs_N-xVQj5kTulXNf9oFkbhKj3p5AhSJQW-Zqr1w1pw2PDebtHb2DyiOVtj82PnI1DzwdnflrnbDZfWSNMUZEaMSPPSRdBNHtXqHB47ygIzPTYHmGR4GbmOUZVldjOHc_BLVgkwRf3XjjhGKTX-o3LQWD9ny2XLNuIOspB3V8yfpLPayRk_Xmhwr1Rc8xhr9ZfhnrypcYg8lxkmA7wAe91GYW7i9qQbPRSuLZ0VCsxjRM_fmp0oQY4pCjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=POFgi5-EuKobbVZUdeJoj8l_xQbTfaIKdV-XbnCYyOYP5RV1ilipV8dXv0RKFLK6A2kw8-ozq1pbnUikJlTEHwo431zHH8J5Uz3L7cOk00zkTHT9q1uoAoPdbRzBYOuBtBOXgMzUNIPPE5sviP1Ynov-i2VGRHDFQl2stxSUCl1mB-9bQCdPECb9QIQ2hrer_WzRK9bA6SYnXZTFim_s5QbtmelYkR1bVt4b_6ewsPUK5nUS60CBiZxctX-jaL4W9m2yJ95Eotem8jZN2sJr1vIHvDmYOthRTFgRzcnt-koVRf2VRGT-UxLheLZbKZ246DmGEnTonXTaCP-lfjy3cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=POFgi5-EuKobbVZUdeJoj8l_xQbTfaIKdV-XbnCYyOYP5RV1ilipV8dXv0RKFLK6A2kw8-ozq1pbnUikJlTEHwo431zHH8J5Uz3L7cOk00zkTHT9q1uoAoPdbRzBYOuBtBOXgMzUNIPPE5sviP1Ynov-i2VGRHDFQl2stxSUCl1mB-9bQCdPECb9QIQ2hrer_WzRK9bA6SYnXZTFim_s5QbtmelYkR1bVt4b_6ewsPUK5nUS60CBiZxctX-jaL4W9m2yJ95Eotem8jZN2sJr1vIHvDmYOthRTFgRzcnt-koVRf2VRGT-UxLheLZbKZ246DmGEnTonXTaCP-lfjy3cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین طائب، رئیس سازمان بسیج مستضعفین، اعلام کرد صدها هزار نفر از ثبت‌نام‌کنندگان پویش حکومتی «جان‌فدا» در تهران سازماندهی شده‌اند و روند الحاق آنها به گردان‌ها و یگان‌های دفاعی جمهوری اسلامی آغاز شده است.
طائب روز جمعه ۲۷ شهریور در جریان رزمایش موسوم به «۳۱۳ هزار نفری جان‌فدایان ایران» در تهران گفت برای این افراد دوره‌های آموزشی مقدماتی و تکمیلی در حوزه‌های زمینی، هوایی و دریایی در نظر گرفته شده است.
این رزمایش از صبح جمعه در مسیر میدان امام حسین تا میدان انقلاب تهران برگزار شد.
@
VahidHeadline
حسین طائب، رییس سازمان بسیج، جمعه ۲۷ شهریور در همایش «جانفدایان ایران» اعلام کرد نیروهای آمریکایی «به‌زودی با شکست از منطقه خارج خواهند شد.»
رییس سازمان بسیج گفت: «جمهوری اسلامی از تمام ظرفیت‌های راهبردی و تنگه‌های دفاعی خود، از جمله تنگه هرمز، با قاطعیت حراست کرده و دشمن را وادار به تسلیم خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78434" target="_blank">📅 16:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGOD15V43XCeZKX8mqhoJazRlyf11MG89m4UMp0FAli29NE1HOdvmKCN4diW2S8ItEtGOnXDuthJRVdLHE4rIM1wwXgc3AhNTZfDmG22glNdSulg6gfPJekIYBcKmJOLz4pkjIpUKi98UGJCdNGHl7BNLS0egQZDlMAp4zzymhiG4S_kTOY-WYAUko5nmgzP9ebi95zSo_IgIa8Jnnyu6CztAUuwI2HxgTvQIgQHgzXAS9qlzAQFdXfFkyAGXjyWJ1eU6rf36zhjHPP40vQXV3Nm5Z162c8C0dOjcGjaXYKuA1dejcPUWKiibgYUNwp4xaieoc6Gn3Ujc0YsT32iJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کره جنوبی اعزام نیرو یا تجهیزات نظامی به خاورمیانه را در صورتی که به مشارکت سئول در جنگ منجر شود رد کرد، اما گفت کشورش ممکن است برای حفاظت از کشتیرانی تجاری و انتقال نفت در منطقه نقش بیشتری بر عهده بگیرد.
لی جائه میونگ روز جمعه ۲۷ شهریور در یک نشست خبری گفت: «هیچ اعزامی که به ورود یا مشارکت در جنگ منجر شود، انجام نخواهد شد.» او تأکید کرد کره جنوبی برای چنین هدفی «به هیچ شکلی» تجهیزات نظامی اعزام نخواهد کرد.
او در عین حال گفت سئول باید مانند دیگر کشورها «حداقل اقدامات لازم» را برای حفاظت از کشتی‌های تجاری، انتقال نفت خام و امنیت شهروندان خود انجام دهد.
دولت کره جنوبی در هفته‌های اخیر در حال بررسی احتمال اعزام نیرو یا تجهیزات نظامی برای کمک به تأمین امنیت کشتیرانی در تنگه هرمز بود.
دونالد ترامپ، رئیس‌جمهور آمریکا، از سئول به دلیل آنچه حمایت ناکافی از تلاش‌های آمریکا در ارتباط با جنگ ایران خوانده، انتقاد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78433" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LgNTIHSQBA_WdVBOa_gIIxk7buAsxIe3tGqtQ0fD-x9N5KyGytjdPsjQP-TpOQhXh1TD3n54i_zq3Esb7PGAsOkyd3egZLX0_1I8JBMaTnoAIwJJ7d3twBwofSIzoksupNwFghmXUStH89uw4fL_OXxVFYLeZA8iNyu91XNLwCGUInsA49KNXyJs-fHY9Sjh7YwU_HGySVyeiTNJ0pIQRrrOt-QPr2aY_cFtGmNdBvT5TV_-OUu6CKqI7u6JLKzSUjw-K2-dnYTPSn-vzR2y3DNGtVSHEjIpLXTsFBlbcVginkaLzRAFs7qvX7saBbAcPfMBkpSQ52q7xNES0QrHXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد یک نفتکش با پرچم توگو را هنگام عبور از تنگه هرمز هدف قرار داده و مدعی شد این شناور پس از اصابت و آتش‌سوزی متوقف شده است.
@
VahidHeadline
UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت (CSO) یک شناور گزارش داده است که یک نفتکش با پرتابه‌ای ناشناس مورد اصابت قرار گرفته و این برخورد باعث آتش‌سوزی در عرشه شده که اکنون مهار و خاموش شده است.
گزارش شده که همه خدمه در سلامت هستند و در حال حاضر تأثیرات زیست‌محیطی این حادثه تأیید نشده است.
UK_MTO
در گزارشی دیگر نوشتند:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) یک گزارش تأییدشده اما با تأخیر زمانی درباره حادثه‌ای دریافت کرده است که در ۱۶ سپتامبر ۲۰۲۶ رخ داده و طی آن یک نفتکش هنگام خروج از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
گزارش شده که خدمه در سلامت هستند. گزارشی درباره ارزیابی خسارات و تأثیرات زیست‌محیطی منتشر نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78432" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSjQOwDhQnsxMpnjEcmlusSZRiQad6jZZpDM4OT7R0s10EBfBnYB98tiCns9QGhWFX3dBteBDeVQ30AkreYoKKDCH5Vl3wMIrfH7_9bQLABXPPKZQ2IkjSOiVnzD75Mu16rV8nnK2xITubx6LnNWwEx8LObTkcQjt44dgSSPJjM4_moV8gs1diCPKtV_B9W4H_gif0Ak5OWt8P3XcheBAiPxqTSx6UkmU4M_CInszs1Lz9SWP4DAgPcZQanE6Fw11i-mKPaAX6Iqx67PITqckSpprfkHH9zPfwh-n7xg_Q2DaKmaJFSz4Pd4MB9SmiolfmiVH-LMk3RmaEfHvvq0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد کرمی‌اسد، جانشین پلیس راهور فراجا از جان‌باختن بیش از ۱۶۰۹ نفر در تصادفات جاده‌های برون‌شهری در شهریورماه خبر داد.
به گفته این مقام فراجا، این آمار به‌طور میانگین به بیش از ۵۰ نفر در روز می‌رسد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78431" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJEsHWaafNW5j4ib_kFm7g1_kqQnmUeb-nVc6i-lRm-fhYQnE14-wQ0jJrtoyY1hnUQ4A2t3ogU59NAbx0QJlueL3k9PqIemAxYL7hthJIEDstPl1BxPPl0P-uj9I_MckWdjklGJLg-KjKSMvgNcjS4XpL7KpRVe4TowU2Ktaeif6M9ZYFWKZHda7onu_V3Es7chqLmpuj2eKLR4Ayyqf6wNafrdTIdNWapmrO3_8_9ULGZM0NRs69zKQsiMHXsKGs32pAEjAttTvgg2d6wVb6ezm44jciHXPZ8Y3NjRqKTriliO5KETSy6mHOGt_6nw3nqSKjC-COOrK_838ciSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=nt_81akdeDXkaupu0za6keP_jQZTxXldbc4CMOnPfzPJrJ3vnOoSUuv1Ny1QeAjcc02jZEKxafN8RdYtnaR9AvT9iTn02TxtHzDiBcet89SYSxj_0yS3QuIzDrd_Fqz5C_nS1g2zJcq7hdlVHRTBkXgTui3jwG6df4Kye2Ign1GLJWUVMFAVYfSYiibFQ8qgqiR9HmsV0-kmYkPhe9nFPknI5JDaMvsS1Rw5SqN_FYH4fe-OI_mjb9zEyvHi9jrGFQ8b92oJpjX9SjALbHq7ZQ9Xkl_uQJQNynZrvYOl2fPGU08uzuCWReM6a4cDqZyCcm_Dp5Rk_l-BFyaSjkpN1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=nt_81akdeDXkaupu0za6keP_jQZTxXldbc4CMOnPfzPJrJ3vnOoSUuv1Ny1QeAjcc02jZEKxafN8RdYtnaR9AvT9iTn02TxtHzDiBcet89SYSxj_0yS3QuIzDrd_Fqz5C_nS1g2zJcq7hdlVHRTBkXgTui3jwG6df4Kye2Ign1GLJWUVMFAVYfSYiibFQ8qgqiR9HmsV0-kmYkPhe9nFPknI5JDaMvsS1Rw5SqN_FYH4fe-OI_mjb9zEyvHi9jrGFQ8b92oJpjX9SjALbHq7ZQ9Xkl_uQJQNynZrvYOl2fPGU08uzuCWReM6a4cDqZyCcm_Dp5Rk_l-BFyaSjkpN1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با انتشار ویدئوها و تصاویر مختلفی در شبکه‌های اجتماعی از وقوع درگیری مسلحانه در بامداد جمعه ۲۷ شهریور در شهر زاهدان، خبرگزاری برنا از کشته شدن یک مأمور نیروی انتظامی در این درگیری خبر داد.
ساعتی بعد خبرگزاری فارس اعلام کرد که در جریان این درگیری دو نفر از مهاجمان کشته شدند و یک نفر از آن‌ها دستگیر شده است.
وب‌سایت «حال‌وش» هم که اخبار سیستان و بلوچستان را منتشر می‌کند، می‌گوید از حوالی ساعت ۳۰ دقیقه بامداد جمعه در محدوده خیابان دانشگاه و اطراف خیابان دانشجو زاهدان به مدت دو ساعت تیراندازی رگباری رخ داد و سرنشینان یک خودرو پژو ۴۰۵ هدف حمله قرار گرفتند.
این رسانه به نقل از منابع خود همچنین افزود در این درگیری «یک فرد مسلح، سه نیروی نظامی و دو زن رهگذر مجروح شدند و چندین آمبولانس به محدوده خیابان دانشگاه و اطراف خیابان دانشجو اعزام و در برخی خیابان‌ها ایست‌های بازرسی برپا شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78426" target="_blank">📅 06:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApUAN1YLupB-8P35Mb4PRXM2hNZgxcNrPg26iVmzWpKNnKqnN4k-3fut_uFh7XDVi59NjNP9djxCb3IPE13EvwvyfO6mQtBvj4okgCCpp8EzGw4WfowyL3pJHviVC9bZoynnkRkouoYZUgrUOD5V-egl8IdcPYtPac-Lvlbsp32ZSotZhV5kCU1rzvl7-eMVP81hhbEBuzZOVxl8Q8GYVgySILigNyLrgG7yHee82hpW3tOSmz8XthZZk0K9cPMzD0kP2vTi1tG53GiuZBQrCzJysSkOte4T5E4CaUzkSrRv-oqS9q7WuVd58b6Al5G5oKh5bWx927Utnaf6i2V9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OrBcipMR4lBhke_uRcoIpJDfOHPBk8SWq55Llq0bDfQ1t_sI9x15V4rZ5eSHO-3TWoVWF1UekCXGzLGhswX-5vN9-aF3i9tJ5lZu_OQauRT1tmiDfi1Q_ylpI3xq81UGcqJc8adTaGZD9m30nw34d-FR1epr8zLbtsSAg3ky7zR3qcNYZFykLcI_8_WTsiOQegiOwbzHEdT1QO-8ZLlfNpToZRmk0xHWBBhccUCdGnNpSS6g1FlpQn4PqpeVCByy7bDjMEppap9-WNou4l_lcWigr2Jh783ZOU-Nx4zsKKdUSSs4KsH0KOPbNf8KNihWmZ8f73ZeQqJZX4W1JCcb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KBD2QEnM5q2UOLej9qgygFO9Gv7tEWzDMA24IiQZMTz9cT2GRa_VElq07B_L_5XusUyEF9SPGsI6N2YhVflojz8q3wi4e35jboPiDTkYIwNGu0WAQAc3XSpj_ka-c40OV9hGJkAuyXt2L5tEZPXUApT3ny_4rD67Gr3RN3ImudO0MkFga_SwDVDWLMrQhf7nOiSy-bzN50pI9vdI8JriX4o_0aIyIsH9z40yTX9l6oaUv_WLDct055Ub-ZjAfakl2exlq8lwvomIJ1f-4kLQ7FR9mMAHyOw0tQNZPRwjp0yCLoJTDJTdAza6WxGZhYv7yRSP4ovs-HX-Jwh8_KVRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس می‌گوید در جنگ ایران به یک دوراهی بزرگ نزدیک می‌شود
ترجمه ماشین:
رئیس‌جمهور ترامپ روز پنج‌شنبه به اکسیوس گفت که در جنگ ایران به نقطه‌ای حساس نزدیک می‌شود و باید تصمیم بگیرد آیا برای پایان دادن به درگیری، حملات گسترده را از سر بگیرد یا نه.
▪️
«تصمیم بزرگی پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر اتفاقی ممکن است برای من بیفتد.»
چرا مهم است:
اگرچه ترامپ پیش از این نیز تهدیدهای مشابهی مطرح کرده، اظهارات تازه او در آستانه دیداری برنامه‌ریزی‌شده در روز سه‌شنبه با رهبران شش کشور خلیج فارس در حاشیه مجمع عمومی سازمان ملل متحد در نیویورک بیان شده است.
▪️
این دیدار می‌تواند مرحله بعدی جنگ را شکل دهد، از جمله اینکه آیا بار دیگر برای دیپلماسی تلاش شود یا اقدامات نظامی تشدید شود. اگر ترامپ بخواهد عملیات رزمی گسترده را از سر بگیرد، به همراهی متحدان منطقه‌ای خود نیاز خواهد داشت.
▪️
رئیس‌جمهور در روزهای اخیر چند بار گفته است که جنگ به‌زودی پایان خواهد یافت. برخی مقام‌های آمریکایی هشدار می‌دهند که این درگیری به بن‌بستی ناپایدار و «نه جنگ، نه صلح» رسیده است و معتقدند اگر تا آن زمان توافقی حاصل نشود، ترامپ ممکن است پس از انتخابات میان‌دوره‌ای دوباره به عملیات رزمی گسترده روی آورد.
آنچه او می‌گوید:
ترامپ در این مصاحبه روشن کرد که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای درباره گام‌های بعدی جنگ استفاده کند.
▪️
ترامپ گفت: «می‌خواهم بفهمم در چه وضعیتی هستند و اوضاعشان چطور است. ما خیلی از آن‌ها محافظت کرده‌ایم.»
▪️
کشورهای شرکت‌کننده عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان هستند.
▪️
ترامپ از گفتن اینکه تصمیمش درباره مسیر پیش رو را قبل یا بعد از انتخابات میان‌دوره‌ای خواهد گرفت، خودداری کرد.
زمینه خبر:
در اوایل اوت، ترامپ پس از آن از ازسرگیری عملیات رزمی گسترده خودداری کرد که عربستان سعودی و قطر ابراز نگرانی کردند ایران در اقدامی تلافی‌جویانه تأسیسات نفت و گاز عربستان را بمباران کند.
▪️
از آن زمان، ترامپ رویکردی «کم‌سروصدا» در پیش گرفته است: تعلیق مذاکرات با ایران، آغاز کارزار تازه تحریم‌های اقتصادی، ادامه محاصره دریایی بنادر ایران و متمرکز کردن ارتش آمریکا بر بازگشایی تنگه هرمز و افزایش جریان نفت به بازار جهانی انرژی.
▪️
ارتش آمریکا عبور نفتکش‌ها و کشتی‌های حامل گاز از تنگه را به‌طور قابل‌توجهی افزایش داده است. با این حال، ترافیک همچنان پایین‌تر از سطح پیش از جنگ است و قیمت نفت نیز همچنان بالاست.
وضعیت فعلی:
به گفته مقام‌های آمریکایی، ترامپ و پیت هگست، وزیر دفاع، به ارتش دستور داده‌اند سطح نیروهای خود در خاورمیانه را تا پایان سال حفظ کند تا برای احتمال بازگشت به نبرد تمام‌عیار آماده بماند.
▪️
این مقام‌ها می‌گویند ترامپ باید به‌زودی درباره مسیر پیش رو تصمیم بگیرد، بخشی از دلیل آن این است که ارتش آمریکا نمی‌تواند خیلی بیشتر در وضعیت فعلیِ انتظار باقی بماند. یکی از این مقام‌ها گفت: «بالاخره در مقطعی باید تصمیم بگیرید که هدف نهایی چیست.»
▪️
ترامپ به اکسیوس گفت از اینکه محاصره دریایی مانع صادرات نفت ایران شده، بسیار راضی است. او گفت: «از وقتی شروع کردیم، حتی یک کشتی هم به ایران نرفته است. تلاش کردند و ما آن‌ها را منفجر کردیم.»
▪️
رئیس‌جمهور افزود که ایران مستقیماً با آمریکا در تماس است و گفت ایرانی‌ها همچنان خواهان دستیابی به توافق هستند.
تصویر کلی:
کاخ سفید همچنین در حال کار روی یک راهبرد پس از جنگ است که خواستار تلاشی منطقه‌ای برای مهار ایران و هم‌زمان گسترش عادی‌سازی روابط میان اسرائیل و همسایگانش است.
▪️
هرچند این طرح هنوز در مراحل ابتدایی تدوین قرار دارد، هدف آن هدایت رویکرد آمریکا در خاورمیانه پس از پایان جنگ ایران و در دو سال پایانی دوره ریاست‌جمهوری ترامپ است. دو رویداد بزرگ بر این برنامه‌ریزی سایه انداخته‌اند: انتخابات ۲۷ اکتبر در اسرائیل و انتخابات میان‌دوره‌ای آمریکا در نوامبر.
چه چیزی را باید زیر نظر داشت:
وقتی از ترامپ پرسیده شد آیا هفته آینده در نیویورک با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد، گفت: «شاید.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78423" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8Z9M-KzkeQl1nogEHJQTWsvyCnW1wObMFyQqmpePtzYgckG-tt46ro8NBbLJbZV23XIvQnEbqRYFtj3rcR6lAvkDlBE4Ftuk9qh1h8kcA41wbtF2qAQtCw1cPMzI6RaZev_sDJb3WWPjqdFYy4MOsFV9VeZloFlYnUvhZnILo3BtXPZqiAUTcc-_HLjFIssYgUS3dx_tChykY4eWbnjaqS8vCOJ3V9MrQoSCxV8hpX_hKSrNquuK6_qBc-_gihYS8wpgk5UVZWpDk1i7QKOfnLMGjwyWYBKfy8dYg5nlhVk3qbRBYa0GKeRbdZLSDUV6wz-NoLyMvlSPSymB2Uqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز پنج‌شنبه ۲۶ شهریور به نقل از مقام‌های آمریکایی گزارش داد نیروهای جمهوری اسلامی در روزهای اخیر دست‌کم دو پهپاد ام‌کیو-۱ آمریکا را سرنگون کردند.
مقام‌های آمریکایی که به شرط فاش نشدن نامشان با سی‌بی‌اس نیوز گفت‌وگو کردند، مشخص نکردند این پهپادها در کدام بخش منطقه سرنگون شدند و از کدام مدل ام‌کیو-۱ بودند.
این پهپادها برای ماموریت‌های اطلاعاتی، شناسایی و نظارتی طراحی شده‌اند و قابلیت حمل موشک‌های هلفایر را نیز دارند. سی‌بی‌اس نیوز نوشت این پهپادها در تنگه هرمز می‌توانند برای نظارت مستمر بر آبراه، رصد فعالیت‌های نظامی جمهوری اسلامی و شناسایی تهدیدها علیه نیروهای آمریکا و کشتیرانی تجاری به کار گرفته شوند.
بر اساس گزارش دفتر بودجه کنگره آمریکا، از آغاز جنگ آمریکا علیه جمهوری اسلامی دست‌کم ۲۴ پهپاد ام‌کیو-۹ ریپر به ارزش تقریبی ۷۲۰ میلیون دلار از دست رفته‌اند. یک پهپاد ام‌کیو-۴سی تریتون به ارزش حدود ۱۵۰ میلیون دلار نیز منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78422" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wADzXdAedJU4uJRrbLrqp1rlpVWWfhQ1Mi3kK5RB3BECGK_lo8F6CEKAzBVmgbBQIHOqpeRsejl3VjGq6jjmKQ-xFm0ts2Uv44cAr40gT9p0ctohooyZOzsxJpjdqGuorHjszeKhneaY-W-J3_1gh7HZC6qWzzXK_4Qk5ZJDhIiWZ3YQ-Ntasbr6mjl9sGwASEElPls_j8v44UV46hikgpryLSjsE9uI_Vn_5UPd-qZocpW0GeVjfZOolUsZvdDiJghXn4uwukTvQyRfhEfaCjbDw_dDLt3fcJiobMoZYN9Fc9qipiErcj2RvaWY5CG-4F3nSCBn683hUrbNUh213A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=YJL9om_Cba08BtUku3Lkh9fHAK52Ux1Dm1o_1KoXC_1SQ23m9lqEiNmAMrTTJ0s3oKdi6rSw1VB49Ygf1Nc0rrzmE91_-IP7PnJP_sUpJDo9QU4baANorcnJw2bI2kAhqjVmAbvuzl9oMAZLqt2X28PhbcTdvaWQc1DU2w1tcaIp7fNBcjCHbyEwE2ZWDbrRoh16iANqsUQC1LKnwM_UN_fvd1dkJyRzTWshd2WK-_9RFrE8q9L_fZYy0Ir1UjmGWqPyJriY13Dh7I08ezD3Ed6RlAr1jZBeqVok-E1AjEFN9x4UnpUaE9Wb9Sjg58panpk58RDkStS0UIuMu2McxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=YJL9om_Cba08BtUku3Lkh9fHAK52Ux1Dm1o_1KoXC_1SQ23m9lqEiNmAMrTTJ0s3oKdi6rSw1VB49Ygf1Nc0rrzmE91_-IP7PnJP_sUpJDo9QU4baANorcnJw2bI2kAhqjVmAbvuzl9oMAZLqt2X28PhbcTdvaWQc1DU2w1tcaIp7fNBcjCHbyEwE2ZWDbrRoh16iANqsUQC1LKnwM_UN_fvd1dkJyRzTWshd2WK-_9RFrE8q9L_fZYy0Ir1UjmGWqPyJriY13Dh7I08ezD3Ed6RlAr1jZBeqVok-E1AjEFN9x4UnpUaE9Wb9Sjg58panpk58RDkStS0UIuMu2McxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز پنجشنبه ۲۶ شهریورماه در مراسم تقدیر از کارکنان برگزیده شاباک در بیت‌المقدس گفت اسرائیل بخش عمده ماموریت خود در برابر جمهوری اسلامی و گروه‌های متحد آن را انجام داده، اما این ماموریت هنوز به پایان نرسیده است. او گفت توانایی ایران و متحدانش برای آسیب رساندن به اسرائیل به‌شدت کاهش یافته است.
نتانیاهو با اشاره به ادامه عملیات اسرائیل گفت: «هنوز کارهایی برای تکمیل باقی مانده است و ما آن را به پایان خواهیم رساند.» او سپس تاکید کرد که اسرائیل حماس را از بین خواهد برد و در مورد جمهوری اسلامی گفت: «حکومت ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سرنگون خواهد شد.» او همچنین گفت اسرائیل به اقدامات خود علیه حزب‌الله ادامه خواهد داد.
نخست‌وزیر اسرائیل همچنین گفت خواست ایران و گروه‌های متحدش برای نابودی اسرائیل از بین نرفته، اما به گفته او، توانایی آن‌ها برای تحقق این هدف به‌شدت تضعیف شده است. این اظهارات در مراسم تقدیر از کارکنان برگزیده شاباک برای سال ۲۰۲۵ مطرح شد که با حضور اسحاق هرتزوگ، رئیس‌جمهوری اسرائیل، و داوید زینی، رئیس شاباک، برگزار شد.
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در شبکه اجتماعی اکس نوشت کارزار نظامی اسرائیل هنوز پایان نیافته و این کشور «اهداف مهمی» در برابر ایران و جبهه‌های دیگر دارد.
او گفت اسرائیل برای دستیابی به این اهداف «با قدرت نظامی و تدبیر سیاسی» اقدام خواهد کرد.
کاتز روز پنجشنبه ۲۶ شهریورماه با اشاره به غزه گفت سیاستی که همراه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دنبال می‌کند بر سلب توانایی گروه‌های جهادی برای حفظ قلمرو، زیرساخت‌ها، فرماندهان و تجدید قوا متمرکز است. او افزود اسرائیل این رویکرد را در غزه، لبنان و شمال کرانه باختری اجرا کرده است.
وزیر دفاع اسرائیل همچنین گفت این کشور فرماندهان «سپاه فلسطین» در ایران را هدف قرار داده و اجازه نخواهد داد ایران یا هیچ طرف دیگری حماس را دوباره مسلح کند. او تاکید کرد اسرائیل به عملیات خود برای تحقق اهداف امنیتی و جلوگیری از تکرار حمله‌ای مشابه هفتم اکتبر ادامه خواهد داد.
کاتز همچنین رجب طیب اردوغان، رئیس‌جمهوری ترکیه، را خطاب قرار داد و گفت اگر می‌خواهد به همفکرانش در غزه کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما «قدم به غزه نخواهد گذاشت».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78420" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqtzRZvhloj4uo81NI8EHqPCjyZerGYHand_MkIZBwd2i36Gh7yk5MQvk-H97IKrDYDzSFWZ8rJZ3Hyk4ubFv2_K1M4uvHsLUheMKELO_K_yfU20dKi84Fu-62-zhAMTsrOi-_DP3EFB7XNX6NVB6-sF-TwkgKOfNssmedqjzcIj9SAwraEVFGAmBOQRQnm-opS7scFE6CVAS-3WuzxufW1RJ_ZQGk86R13nvXQVr-tqu5xRK_xb07l58y5hWK3uPjIUSL5tA1y-OOAbdoH9P_7isyjnNb7MiCHLEomej1LBv63HuYPuCGkb3699LLmDUDxokbjmue3OOf6Uegsxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیات حقیقت‌یاب مستقل بین‌المللی سازمان ملل درباره ایران در تازه‌ترین گزارش خود اعلام کرد دلایل معقولی برای این باور وجود دارد که آمریکا در جریان جنگ با جمهوری اسلامی، در دو حمله هوایی به ایران مرتکب «جنایت جنگی» شده است. بر اساس این گزارش، این حملات دست‌کم ۱۷۸ غیرنظامی، از جمله زنان و کودکان، را کشت.
این هیات در گزارشی که به شورای حقوق بشر سازمان ملل ارائه شد، حملات آمریکا و اسرائیل به ایران در ۹ اسفند ۱۴۰۴ را بررسی کرد و به این نتیجه رسید که آمریکا در دو مورد حملاتی بدون تمایز انجام داده که به کشته یا زخمی شدن غیرنظامیان و آسیب به اماکن غیرنظامی منجر شده است.
بر اساس یافته‌های هیات حقیقت‌یاب، در یکی از این موارد، موشک‌های تاماهاوک به دبستان شجره طیبه در میناب اصابت کردند. این هیات اعلام کرد این مدرسه به وضوح قابل شناسایی بوده و در این حمله بیش از ۱۵۰ نفر، از جمله حدود ۱۲۰ کودک، کشته شدند.
در موردی دیگر، آمریکا با استفاده از موشک‌های تهاجمی دقیق، ساچمه‌های تنگستن را بر فراز یک مجموعه ورزشی و منطقه مسکونی در لامرد پراکنده کرد. بر اساس گزارش، این حمله ۲۲ زن و مرد غیرنظامی را کشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78419" target="_blank">📅 21:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl_KIlwJp1RdAjb8pNqlhGb_SCdtsdNgsUNNAsSvVg6VpnPOQyVsCzmyP2USFcn_vdZc4aNcJ8I6d-7m4n52lLvuIoy5uB7bHXigiGxncMKtaW0xfD88-bEhu_MSDyysAGzerSiB16pkFmHMTTv9c46s3XNs7EmZ_a1i1X_lsHq33tH8yeTthNEjPoh6kBEgniJcv_Wb-q6b0Phm01ZGWMhnobr27xXCGH_c1B1OdzZoTAc01YxnXHZRW75qQqMbU8vSxv24PjEce2lOlBQpaZ7CyY9FRZIvC_1WerdYt-41ym-mpuhzN44CORknWSNYJK_JSufjpE6JfiO1OQCkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه و چین روز پنجشنبه، ۲۶ شهریور، در نشست شورای امنیت سازمان ملل متحد، پیش‌نویس قطعنامه پیشنهادی ایالات متحده برای تمدید ماموریت هیات کارشناسان کمیته تحریم‌های ۱۷۳۷ علیه جمهوری اسلامی ایران را وتو کردند.
این نشست با ابتکار فرانسه که در ماه سپتامبر ریاست دوره‌ای شورای امنیت را بر عهده دارد، در چارچوب دستورکار «منع اشاعه» برگزار شد. در جریان رای‌گیری میان ۱۵ عضو شورای امنیت، این قطعنامه ۱۱ رای مثبت کسب کرد، اما با مخالفت صریح (وتو) مسکو و پکن و همچنین رای ممتنع پاکستان و سومالی مواجه شد. برای تصویب یک قطعنامه در این شورا، علاوه بر کسب حداقل ۹ رای موافق، وتو نکردن اعضای دائم الزامی است.
دیپلمات‌ها پیش‌تر از مخالفت قطعی روسیه و چین با این طرح خبر داده بودند. مسکو و پکن معتقدند که با انقضای قطعی قطعنامه ۲۲۳۱ برجام در اکتبر ۲۰۲۵، تمامی سازوکارهای تحریمی پیشین از جمله کمیته ۱۷۳۷ فاقد هرگونه اعتبار و اثر حقوقی هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78418" target="_blank">📅 18:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/caed21affc.mp4?token=V-JqbVdD6kJ2A7-zI1Sbhv1zyGi3nnZbMXGRTnsEVUMhAbovCyiyRyypsuKPXYOfGd7VRqdYt_rjgUc5TIIsM_XIM8npNj8kpCcEhccMie9taZBDEIzZhdJLFFDfLK_WEqP4sorVmn0geyL1s-RPfTnN_oUJ31atNCYZyFl5jEgJPkQYiv2oq9CxvQsrFEYtSceJT5Wc_sQdZ-XnmvWh4AMPH55anmK09annIZlHMWHTIEzwBCMgERjrFogFHxdiKJQBVE7WKfG6Y9ROAaTO1NLB5-sVwkT2_dIBkPdJ8Yialkq2fHgQLmWVZrKnu2fQ7gmlopOsuc8E_pUo_vkvyg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/caed21affc.mp4?token=V-JqbVdD6kJ2A7-zI1Sbhv1zyGi3nnZbMXGRTnsEVUMhAbovCyiyRyypsuKPXYOfGd7VRqdYt_rjgUc5TIIsM_XIM8npNj8kpCcEhccMie9taZBDEIzZhdJLFFDfLK_WEqP4sorVmn0geyL1s-RPfTnN_oUJ31atNCYZyFl5jEgJPkQYiv2oq9CxvQsrFEYtSceJT5Wc_sQdZ-XnmvWh4AMPH55anmK09annIZlHMWHTIEzwBCMgERjrFogFHxdiKJQBVE7WKfG6Y9ROAaTO1NLB5-sVwkT2_dIBkPdJ8Yialkq2fHgQLmWVZrKnu2fQ7gmlopOsuc8E_pUo_vkvyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خشونت و آزار جنسی)
ویدیو نشان می‌دهد ماموران فرماندهی انتظامی جمهوری اسلامی ایران یک نوجوان را مورد ضرب و شتم و آزار جنسی قرار داده‌اند.
این ویدیو خشم بسیاری از کاربران را برانگیخته است. برخی  گفته‌اند که «وقتی پلیس مقابل دوربین دست به چنین کارهایی می‌زند، معلوم نیست در بازداشتگاه و پشت درهای بسته چه به سر بازداشت‌شدگان می‌آورد.»
فرمانده انتظامی آذربایجان شرقی گفته که این اتفاق ۱۴ خرداد ۱۴۰۵ در جریان یک نزاع خیابانی در تبریز رخ داده است.
برخی هم با اشاره به انتشار این ویدیو در چهارمین سالگرد کشته شدن مهسا (ژینا) امینی در بازداشت گشت ارشاد، به تداوم خشونت پلیس در سایه نبود قوانین بازدارنده اشاره کرده‌اند.
پس از پربازدید شدن این ویدیو، فرمانده انتظامی استان آذربایجان شرقی گفت که ماموران حاضر در ویدیو «تنبیه انضباطی» شده‌اند.
علی محمدی به خبرگزاری فارس گفت که این افراد «تنبیه و انتظار خدمت» شده‌اند و «اقدامات تنبیهی تکمیلی» در مورد آنها در دست اقدام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78417" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OLKO-31gB3maRQjFQTXJBxfsGhF7WDyAXe-doEPFGm2jXECZdbBoIsxpoOIrD-Id9DYdGin17w3hCVmtczGfzdMJaOBb4hwjYYnqeyTGIkngIHBCmes6JS78MRKg4QT2uM29foex8DRwHhLVqGEgpdQPeKxUCWIseXwgoiylXxpUa6laVWldiSksP0t6uaBBZ2ab_wh3V6ZIzampG5alsITclDKmjnhvcUruMjNpwABoDxNg69i15ThDV591fjNqIbYy6ao5HL-ixeoGsuEezgannh9ktAKg1eqQt35AY_vhMfqkGyjfu2ojD4nh0PcAtLONIuOTTXQ69WY7oUFmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، مدعی شده است جمهوری اسلامی مستقیما با دولت او تماس گرفته و «بسیار» خواهان دستیابی به توافق با ایالات متحده است. او همچنین ابراز امیدواری کرده جنگ نزدیک به پایان باشد.
ترامپ بامداد پنج‌شنبه ۲۶ شهریور ۱۴۰۵، پس از ورود به ایالت کارولینای شمالی، در پاسخ به پرسش خبرنگاران درباره مرحله کنونی جنگ گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم.»
او سپس درباره احتمال دستیابی به توافق با جمهوری اسلامی گفت: «آن‌ها می‌خواهند توافق کنند و خواهیم دید چگونه پیش می‌رود.» ترامپ در پاسخ به این پرسش که آیا پیام ایران از طریق میانجی‌ها منتقل شده یا تماس مستقیمی صورت گرفته است، گفت این تماس «مستقیم» بوده، اما درباره زمان، سطح و محتوای آن توضیح بیشتری نداد.
رییس‌جمهوری آمریکا ساعاتی بعد در یک گردهمایی انتخاباتی در شهر گاستونیا در کارولینای شمالی، بار دیگر گفت جنگ با ایران به‌زودی پایان خواهد یافت و «پایان واقعا خوبی» خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nKFA7rs4hN6r7wzxxw1DGRBcV6yGZO_1UzcU-fi4htiymxMBFZQosrmSHkct7To-mQxkAKJCPP5VacX8rCdFAapzOz2XZpSVUvFoysWDtnogFCh0J7o-MwxqHoPd67Au3VuMYfMtlDhRi0XXK3zFjvuAbPEJ4eS4Zk4WVC4qYavd1OixGrn1dySvQEpfJui1me5s5Fhg15y1k12GfPDZqTjrtZ_w8g7Ytk86HKRcoLV9Plxx8aaP8xuh7jNbIcLxY_ds2nKx_6umyxnOv-BwI3oRTkSH6lgB9w_12ACaBiGf_3Tc8tCGEGdgbPB11H-imcO4vj_OhesJpxeuTpqkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی ماهان چهارشنبه ۲۵ شهریور در اطلاعیه‌ای اعلام کرد پروازهای این شرکت در مسیر تهران-مسقط-تهران از ۲۶ شهریور، برابر با ۱۷ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان دلیل لغو این پروازها را اعلام مراجع هوانوردی عمان عنوان کرد.
این شرکت همچنین در اطلاعیه‌ای جداگانه اعلام کرد بنا بر اعلام مراجع هوانوردی ترکیه، پروازهای ماهان از ایران به مقصد ترکیه، شامل استانبول، آنکارا و بالعکس، از ۳۰ شهریور، برابر با ۲۱ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان افزود آخرین پروازهای این شرکت در مسیرهای تهران-استانبول، تهران-آنکارا و بالعکس روز ۲۹ شهریور انجام خواهد شد.
خبرگزاری عصر ایران نیز سه‌شنبه ۲۴ شهریور به نقل از یک منبع آگاه گزارش داده بود دولت گرجستان در پی تحریم‌های جدید آمریکا، پرواز همه شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه آینده متوقف می‌کند.
عصر ایران افزود بررسی این رسانه از چند آژانس گردشگری نشان می‌دهد فروش تورهای گرجستان نیز تنها تا یکشنبه ۲۹ شهریور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GGcxeighQrar_gmaIofmBL38GvMXEf7E508PZtbR1Z7ON5nDWZJ8tvZUUfXESGpdbblsCKkLoCII4a5lWnOsCDjDpfC8jwS-Zknt8Kr8hmFHwO0k-jsJ5WTwaUkR6v632Jz6Lb-98AVk6qLnGQ2cWd4X_6DJlYAM4MILM-1m8WGQPjFzMKa6I3f1N4vsXuqpMHzmTmYYQH_jEwgg7n6lr7GiXKq0wZbzdBxgJv9mBWVES2mLq-vG1lgi4ZBTGF9el7b7Vp1wz7CUcExwcaO06LM2OAunjniFvhp8PsWwVR7Q6t2-Ak-JRRETGmFxVYK2FwGvRLbS7UDzb7vI-ja-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfqbDDHKdBv2596E5l_3vd7YvuupUcDuL81s7NXbBqht7TmcFMeJ-MsB2oCBIg0PasIparkCgOvSKbmtiAcAJUvB49f98hDfzRGJfSpDKT_sqxDQ-0fUHMBV6cTke3a6b_M5IgSoIVOzPU9cXVfDGunV20Bzqc3qCNwJQAruyVlgEuoZIcftx8EcNBvOVaVpksu2z24F4rWdkTuHBgy_KIen4EuQ6h7YktugIywr6NHbesYkVcHiNvEV9gO40u80ktmQHD1uzJdzdf2QgGk50nhMS1nbURW1RWoBD8bFLddy5QtejCW77gu9_uSmDL74sxJm8S2PaKkVxRqDAwLXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین با صدور بیانیه‌ای اعلام کرد که وانگ ئی، وزیر امور خارجه این کشور، روز چهارشنبه در دیدار با عباس عراقچی در پکن گفت:
چین، ایران و ایالات متحده را تشویق می‌کند تا عقلانیت خود را حفظ کرده، خویشتن‌داری نشان دهند، به یادداشت تفاهم اسلام‌آباد بازگردند و «در گفتگوهای ماهوی درباره مسائل مورد علاقه طرفین مشارکت کنند.
براساس این گزارش، وانگ با بیان اینکه چین «نمی‌خواهد شاهد سرایت بیشتر تنش‌های منطقه‌ای به یمن و دریای سرخ باشد» افزود: «ما از همه طرف‌ها می‌خواهیم اقدامات موثری برای بازگشایی هرچه سریع‌تر تنگه هرمز انجام دهند.»
وانگ همچنین گفت که سیاست چین در قبال ایران همواره ثابت و پایدار بوده و چین مایل است ارتباطات و هماهنگی‌های خود را با تهران تقویت کند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، چهارشنبه، ۲۵ شهریور در سفر به پکن با وانگ یی، وزیر خارجه چین، دیدار کرد و بر گسترش روابط تهران و پکن در چارچوب مشارکت جامع راهبردی تاکید کرد.
عراقچی شرایط کنونی منطقه را ناشی از حملات نظامی آمریکا و اسرائیل به ایران دانست و از مواضع چین در محکوم کردن اقدامات این دو کشور قدردانی کرد.
او گفت: «جمهوری اسلامی ضمن آمادگی کامل برای دفاع مقتدرانه از حاکمیت ملی و تمامیت سرزمینی و صیانت از امنیت و منافع ملی ایران در مقابل متجاوزان، از راه‌حل‌های دیپلماتیک که حقوق ملت ایران را تامین کند، استقبال می‌کند.»
عراقچی همچنین گفت شرایط منطقه پس از جنگ ایران تغییر کرده است و در نظم جدید منطقه‌ای که با گفت‌وگو و همکاری کشورهای منطقه همراه خواهد بود، جایی برای حضور و دخالت نیروهای خارجی وجود ندارد.
او با اشاره به آنچه نقض مکرر تعهدات از سوی آمریکا خواند، گفت جمهوری اسلامی خواهان بازگشت آرامش به منطقه و روابط دوستانه با همسایگان است و در همین راستا گفت‌وگو با کشورهای منطقه را آغاز کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sDPFuS0YXSgQgjYMs5R5JnHMXyTY1cezcZZsZ8QMJxN-kDIvoZh6H5FU-ftiYF6UPZh48FEjJZHoeha0tMvd6-QmN5KuI__R0bnFG4j6UxrbP7-h5Ic9VMCk5ndPYJsPfe1TzybosPeOVcneCW2A2sRHduyxPfA3zh-iBZt8FA9AVkOavkGZ6lLmSTH3xo8JaPerhgsPyjOeK4WjbnULIIdBtuuSgNO8mQLiwNE7aiT281I8HGmAOUdtlyE5n9z0JMiV5fcvxsXzBrG5nISNiY3utQEjjdzb8fCV2qexUg1eqAC0r1qlJX6naVTZaEg83Z9FpgNmZl3eigMvpy083A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز چهارشنبه ۲۵ شهریورماه به نقل از پنج منبع آگاه گزارش کرد که مقام‌های ایالات متحده آخر هفته گذشته (روزهای شنبه یا یکشنبه) با نمایندگان شورشیان حوثی مورد حمایت جمهوری اسلامی ایران، دیدار کرده‌اند.
براساس این گزارش سه تن از این منابع که خواستند نامشان فاش نشود گفتند این دیدار که رسانه‌ای نشده بود، در سفارت آمریکا در مسقط برگزار شد. دو منبع دیگر نیز اشاره کردند که دولت عمان، به عنوان میانجی باسابقه منطقه‌ای، به برگزاری این نشست کمک کرده است.
دونالد ترامپ در سال ۲۰۲۵ و پس از بازگشت به قدرت حوثی‌ها را در فهرست «سازمان‌های تروریستی خارجی» قرار داد و هرگونه حمایت از این گروه را جرم‌انگاری کرد.
ترامپ روز شنبه گفت حوثی‌ها با دولت او تماس تلفنی داشته و از ایالات متحده خواسته‌اند از جنگ یمن دور بماند. جی‌دی ونس، معاون رئیس‌جمهوری هم روز دوشنبه بدون ارائه جزئیات تاکید کرد که ایالات متحده در تماس مستقیم با این گروه است.
دو منبع آگاه اعلام کردند در این نشست که به گفته یکی از آن‌ها روز یکشنبه برگزار شد، حوثی‌ها به مقام‌های آمریکایی گفته‌اند قصد حمله به شناورهای آمریکایی را ندارند و به آتش‌بس سال ۲۰۲۵ با آمریکا متعهد هستند.
یکی از این منابع که یک یمنی است، گفت این گروه همچنین اعلام کرده‌اند که به کشتی‌های اسرائیلی یا هرگونه کشتی تجاری دیگر، به‌جز کشتی‌های متعلق به عربستان سعودی، حمله نخواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvHQyrKiQrVQcG7xo8YUiivvwjWOVgkuFEzqGCrC05nEsl0SU481WFViBdKzMlNbGNZV0qUidbkq9hPZtTvE2NWRvmg74j3LDb0s9PYs0dRPB0OpHnyW_bQgamKTU5P6oiRfmvx1tGKkbyihrNo5dbpjPZFl8p56cgDiFhhCu8lqmq0dCkiOYuygjPqQEkqe7GTX3eF2la8wHxNCEYaP2E8jsXQLapEAuIyD8WuS19lINEhpQ_s-LUQFMMrOSXRUO06Vdf0VILhffRQ_1ZfcTEYd1XOq6EaULbTfqIYvoQZTqQidDjFH4dV0Il4VuAgx1I4FFk7EyDK-qIKTPeiDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gmv1Un6EmZKDPWkH3fwgbF4mDPi9QGT08QsfHqHEb0GTSu6KRJ1-62VCDhDiLXIjzM-LvvSxEnlzPhKpMNnrdBpMTkVoYHX4n2xjBBRvkpinm04Ptb8iQT8priPrpv9rwLXTqIQ9TN_Jv0L2kVNqR6y4gufbis2bB-87ggAkWudZyBiLwsIJN-adUCJkPY3phBr0ZQUy6sjidpwxVF9nFR2lOExXMMB9mmgWTfDeK-6dmKKCMub5fq8pyGD9jvT3oeYgQfnO8r2tiARNG7GLkMhQ3ppjYWtt--SRmoIdJA09Kg0OOsbBVUeuZrAMbMONuRqpaHQsiSjgkkISTfiZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین قشقایی، همسرش سارا شمسایی و ابوالفضل قشقایی، برادر حسین، از معترضان دی‌ماه، پنجشنبه ۱۹ شهریور بازداشت شدند.
حسین قشقایی و سارا شمسایی در لاهیجان به دست نیروهای وزارت اطلاعات بازداشت و به اراک منتقل شده‌اند.
محل دقیق نگهداری آنها مشخص نیست و احتمال می‌رود در بازداشتگاه اداره اطلاعات اراک باشند.
ابوالفضل قشقایی نیز همان روز در زرندیه ساوه بازداشت و به اراک منتقل شد. به گفته یک منبع مطلع، ماموران هنگام بازداشت با خشونت وارد منزل شدند و گوشی‌های تلفن، تبلت و لپ‌تاپ اعضای خانواده را با خود بردند.
حسین قشقایی با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «اغوا و تحریک به جهت برهم زدن امنیت کشور به جنگ و کشتار»، «نشر اکاذیب در فضای مجازی» و «اجتماع و تبانی علیه امنیت ملی» روبه‌رو است.
درباره اتهام ابوالفضل تاکنون اطلاعاتی به خانواده اعلام نشده و پرونده این سه نفر هنوز به شعبه‌ای ارجاع نشده است.
از دی‌ماه، سیم‌کارت‌های حسین و سارا و حساب بانکی حسین نیز مسدود شده بود. آنها ماه گذشته به دادسرای عمومی و انقلاب زرندیه احضار شده بودند، اما در مهلت پنج‌روزه تعیین‌شده حاضر نشدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=K8HK28IWo6Odm9D7eUYzzJ9k9HBPGnuQFM5A5upGwcnjaTgH4pC96n2svxB9pZRecGmUEJ8VRwOmNqnO0DNAGdBqf4C1ndQfj_zRm2Rn3NHb6vgQDKD4xHrpCjpzB9q-g18-ZVzJnb4DV6LkQyubZun-ZoQ_O4kY4bgeyCFOv3mWZ04T_ozCx9WIPrJpHV4khxqbIVB9tLhBy3bis5n5e_8AODRF5FYeersX4RXsCzKXt8A4vrBXOAzGdOO4izYiscVJw1Tm-Puv1OiiX3LhnTPd2ip5hAcCoURflieZT2MkAbvOGz_I84wYCtMy0FMqV5nEL741Le7bYvjzEEI8rToFWIZsDaGkr28r65qbTZs2tfqcMBibaCdEDfO0AZ3kvlqVcByUB5P42RY6VhEOf9n211kM41UkKiPSu978LjpjkyqoXrGP1CtA3mV_Lde3EtvIllY0wdlxZyiuoiigOWo7nt7tvpFOVYsf1s7djSGLGQ3uKWBLQr0bng1tCjk_6q3wqVNzW4-353V7QwxkN-V92kHgcAvKVTV9_SQARGlcAvxk_BuJhfbApBRy7ZE8q51U3keygqX85OWHYuyuu6Z-wjHFmh9Nyqk9Kn8gUC77ZvDnyK0PvPjcAevjszAurvBaWyUvEeCmaaKNeBpLoIrwg-zXwTr0Q1XBe6cLjyk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=K8HK28IWo6Odm9D7eUYzzJ9k9HBPGnuQFM5A5upGwcnjaTgH4pC96n2svxB9pZRecGmUEJ8VRwOmNqnO0DNAGdBqf4C1ndQfj_zRm2Rn3NHb6vgQDKD4xHrpCjpzB9q-g18-ZVzJnb4DV6LkQyubZun-ZoQ_O4kY4bgeyCFOv3mWZ04T_ozCx9WIPrJpHV4khxqbIVB9tLhBy3bis5n5e_8AODRF5FYeersX4RXsCzKXt8A4vrBXOAzGdOO4izYiscVJw1Tm-Puv1OiiX3LhnTPd2ip5hAcCoURflieZT2MkAbvOGz_I84wYCtMy0FMqV5nEL741Le7bYvjzEEI8rToFWIZsDaGkr28r65qbTZs2tfqcMBibaCdEDfO0AZ3kvlqVcByUB5P42RY6VhEOf9n211kM41UkKiPSu978LjpjkyqoXrGP1CtA3mV_Lde3EtvIllY0wdlxZyiuoiigOWo7nt7tvpFOVYsf1s7djSGLGQ3uKWBLQr0bng1tCjk_6q3wqVNzW4-353V7QwxkN-V92kHgcAvKVTV9_SQARGlcAvxk_BuJhfbApBRy7ZE8q51U3keygqX85OWHYuyuu6Z-wjHFmh9Nyqk9Kn8gUC77ZvDnyK0PvPjcAevjszAurvBaWyUvEeCmaaKNeBpLoIrwg-zXwTr0Q1XBe6cLjyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فراخوان ائتلاف نیروهای سیاسی کردستان ایران، همزمان با چهارمین سالگرد قتل حکومتی مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»، کسبه و بازاریان شماری از شهرهای کردنشین اعتصاب کردند و مغازه‌های خود را بسته نگه داشتند.
از صبح تا ظهر چهارشنبه ۲۵ شهریور، اعتصاب و بسته بودن مغازه‌ها و بازار در دست‌کم ۲۰ شهر، از جمله ارومیه، اشنویه، بانه، بوکان، بیجار، پاوه، پیرانشهر، ثلاث باباجانی، جوانرود، دیواندره، روانسر، سقز، سنندج، قروه، کامیاران، کرمانشاه، کرند، مریوان، مهاباد و میاندوآب گزارش شده است.
@
VahidOOnLine
وب‌سایت‌ها و منابع خبری مختلف که اخبار کردستان را منتشر می‌کنند، از جمله هانا، کردپا، کولبرنیوز، زاگرس ۲۴ و شبکه حقوق بشر کردستان نیز گزارش‌ها و تصاویری از تعطیلی مغازه‌ها در شهرهای مختلف کردنشین منتشر کردند.
در همین حال تصاویر و گزارش‌های مختلفی از برقراری فضای امنیتی شدید و استقرار نیروهای نظامی و انتظامی با سلاح‌های سنگین در شهرهای مختلف کردنشین منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rRKOkP8-R4Yq3k7KnJYF7jLgfYh2hvBrl72skv41_BJtx5ho7reAvaZOC-2fEuR4sX63PEAHW2CL-X_Hcz09EEVGPNO1eqHHsS1JAaVO8PLD32SmVQUq1Ha21sgP63IH3fMU5qZiTiUt09iOlDM-r-A5zbTITM0gtl_G62FXZ_k2d9MwMv3VzThjEUtYi2vyBtANW5oAxJLyFEkWPhB64zDJsoexV9efvKPUmNyV93mmodnM9rez25z6XzrSgyJUnX7FI-7D7ZM5UBJhZ5lMF-mELtTVdICNedof6Mtt2MQL7RN6FaJ3mgUGxg2imhccsh0-gaHwTSu824-ztptNKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qj-3F0Bd8cL998vQDXe2zurALxW29MHhXw7qCJEA2R5SrvoNEJagubZ1-wR9lOhCQFPSKZJeKGOCxQY7IvM-Qz0bJdvFUujEHLHKnXk9uh2ZpF24ym5uKh3C8e5u3-9Q5NRjBbQw1fPX7qiqsctpEUlV7JVrfQwyasYeFUGDGX3Wid26fK_BYumiKNz3scButRhQNVI6Z1toEsr-XvgIQCTn1mjIHh4MuMnAcam1kg5SI45K20B1Q_DLDGWQH_H7LIorXpiGq6UZHlX4ZbsAYJIqka1LhvPMi-S_SiR43twD4GUyQK9CThlYJZg1AlD6QSVdU-yYid30BN5npoCKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JJ9tUnly9AkKNrSQN-e_mgDfObzIvpPa0A1-qNa9T5j0ztPA86rrD_iobuMXWOV2bjj8VDIafjfzQRTyMbEc6Tx4WPnNChlbXL3IlwDOenaIPVrsNWYYydbXMbu86kQU4QUGRtY3zeghzZjvlIBAsh9ObUNfauqYWwGXaSgoZQy64hvHUz0L-1_saWFvNPfsNKS8pbzaRJNSOTjdGs7RxlUVFWTOz6827c0OVQ0CgL2YdfOFXSbfCP3YmWsZ0RSpMJnh-EktQgBnXx717hHLidympdhszS5TV8_1jdqnQ5UsTn5MPCx56_Lu1uc2ejEwMNN3mMkxzk1VR89HDIeulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/boOD6CUjoc4g8lTEaoAGXlaa4-eSny6XcymNDkN2ZDy5n1NeIZ79jk_4TgWLIy1ZMcnfU0DNDLmHOHqLBOw-mTEQi2fAX4lVy3cNc-0fVp9Bg3QvejSTsJGpeNYxq1nIgEfGkDWWXkO2xsKtj4BXpOszWqYynBRQRGWv9vX_SByENBrP40ksiSsbyjk3MGaASdsgJhGjIuM2gtlv_sXDqM-uDFeBCL_YXlpnHOFemT_6XIJbZXEy_qoMSaxbwJmrK-xxeA8pLjO1rV690ip2M6d7WhxQmCU4RBqBfaVw4ePq6od0-ti2JWuOtsw2hMMHEnDBeZr7lEIOjfF5w8W3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bsuckNUVUQRIbjWbNmtIC87o4XDpmVCjnO9FnAWxsrFun6PkAhyY_vVegQOLZdKLq6nMzGNny_4yqPG_S8Lq76PwMATNxP3qduo1LtKj9ekPGaLjYkX3aDlB8V10Oj2HkufDOamA8icxduYSj_2qRt6fhCPJklK65g26sCVQtzapdn6jc1_0KBKw3YopnGrrVzc867PduJKMha8KCvpsVn7JXlkMWpZvyP5pyKFtajFC4TOQvx3xqJJUr0JuYGtvS_9u3Av2S1IbJkwcDcLrzsdrRPl2ESyKwvqiLtwxyRicAn7xvmhSsd843mDsdQMB3BWc-YfACag5fe8JdyQuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XSZc1vQeGDt8HfX3oNFtcSyVnd__jkKgjmoo5ZyeRwt0XRF8zK0nos0DRdRTogN2lveNDJbcas0kNVTgxSPkbxCt2Ilr67LMe5KLnL7i6pWjn23NwowAtwPFxu1QAiBTqgcHv3pHL0p5enCtgsV1Le9BtUtdAUr0xCIIP7FasU_fj-j-m_hidXprzvKQTTkLtd1F4hw7tPy8_LJqZjVK3w6Os5d-xcgobNv5eKVVUQtAAwHN_E5R55XAHh5glUcfCtY3pG4socyo-hAk6DOOCj29PSaY07ATBZ-QAyrSPJXWUkjQ9yqurvVkEAJX0S6zpyRxl8M4mbHKM7TndFpUpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkxjvBUmqw0NlqTW7P8uXAU6CS9laTvBB4LvyVIHchL17PhAw7XvS3pLcA8rpcCKwg7B0rm6q4_iIbcsM25QaBlW6-wCrM_96A_-S0yXo8gyPOJ0cQidqQTleLm87XdvmRNLknh8TEb21uOwWefK8jqWDbYPx3A5x2vYw9RMpql-i4YitemgEijEiE3HxUpgHgAW8Yg8GnbtJIhiqfZGYhkvC5QBUP8IZ53OWjAlBu47x070H7DNPEU8qsRmQmWZpxR70sfgwYRFW-j2jCaYKvFX6jKln96Hr-wsPzjTD9XgH_ouzueYC4D6vQLgwexqvCW0Nhmooe1oU5HnfMcR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZQX8wKcXqrTvNd5FifxnBpjmgM32AKh7rnhW3bWlvwZqP4zyW_ofp0Fql0JALmGN7Zk78GzfE1nNq9rnqjPUdkgElG8bVpA11-UUcnJCIq29KFHLLS2HxQ0HrHSTgQDeLzjU4bJ1nvAYvpJVqcvMx2QoutInIHDMmONHZll4qgsQVq1Mgml4qAJ0W_tWfdAMVAh8zO6c0HMonb84n04tqgUJbUXdedUgy4hvu2qYdpPCWLdXj9xqr3ncAF8VtAz69K12JtbC-aeKgEKrGcbCIELrv6v4QN6OLD3O2Zk3MRGxbGaFfHKzq9Ukv-kPQ7NqECRsbo7NudSRdz0cFERrAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=DMDSEv2vDLsAOVmlEp_4OO_LQBgtDECa5KWpLKSHuQW3EktBP-XIwRM4pRGAuA9EESPgiLj_si-d7VSKtzBbfm-x1s5PE2YE75HUW86uU3otwgZbZD45n8-7lmB8OOcpsBbXELuvt_Sc79KD-21p6uc8vgMKEk_I044yo6pUXxJIgWQlW2IZJcEGJAcKNul3ovoiaMrl1zQaN40gL7QtZ-MYABQ4nRUwILh938yxl4yqEsm6QQYeF8NBvWGGFZ33i3TCxdogm2iGACcFBcrtlOy0QiF2em8eLq-qMsRln3wGjcKAOCzv5V4-Gzd8Lt62wj8GuUV2c01MoA-xcEmGow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=DMDSEv2vDLsAOVmlEp_4OO_LQBgtDECa5KWpLKSHuQW3EktBP-XIwRM4pRGAuA9EESPgiLj_si-d7VSKtzBbfm-x1s5PE2YE75HUW86uU3otwgZbZD45n8-7lmB8OOcpsBbXELuvt_Sc79KD-21p6uc8vgMKEk_I044yo6pUXxJIgWQlW2IZJcEGJAcKNul3ovoiaMrl1zQaN40gL7QtZ-MYABQ4nRUwILh938yxl4yqEsm6QQYeF8NBvWGGFZ33i3TCxdogm2iGACcFBcrtlOy0QiF2em8eLq-qMsRln3wGjcKAOCzv5V4-Gzd8Lt62wj8GuUV2c01MoA-xcEmGow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/anhvprmgzhn9cNfyOX1fXCj6zEVTBtaAbF0EmHlnCDaLvBaffWcKCXHhUEbkvw9R-sIeKxWe_9Dn1w_DVsxQ6tA2t5AHFHfywOM6F6tCRKAO4AG1hNXo6CY2VqI-clsbXbJbaqw_bP4w-tibylQsK43MUbY66aylTx_zGq8YlAWdjNFBG0sK4acfIcsPUXiCSXkKpve4nAYRqdKSOasGKkG-HDZsJ7SGZlG7fS3wnBDtzizHpQzs2bYeQrlApSs4Xyyf3OZmn-cchC29QEzgCQFAtHKj4TxzbZ9YcCk_OvfBayDVBBLql_rtsdMPr_xwpLUp7wuqvkwGUOjZaXF73A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره خبری که تسنیم با شرح
حمله به قایق‌های صیادی
منتشر کرده بود:
وبسایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده روز دوشنبه ۲۳ شهریور ۱۴۰۵، دو قایق کوچک ایرانی را پس از تلاش نیروهای سپاه پاسداران برای تصرف یک پهپاد نیروی دریایی آمریکا در تنگه هرمز منهدم کرده است.
به گزارش اکسیوس، نیروهای سپاه با استفاده از این قایق‌ها تلاش کردند یک شناور بدون‌سرنشین آمریکایی را که برای گشت‌زنی در تنگه هرمز مورد استفاده قرار می‌گیرد، تصرف کنند.
پس از شناسایی این تلاش، یک پهپاد آمریکایی دو موشک به سمت قایق‌ها شلیک کرد که به انهدام آنها و کشته‌شدن بیشتر سرنشینان منجر شد.
تیم هاوکینز، سخنگوی سنتکام، تلاش نیروهای ایرانی برای تصرف شناور آمریکایی را تایید کرد و گفت این قایق‌ها «تلاش کردند یک شناور سطحی بدون‌سرنشین آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام موفق نشدند». او تأکید کرد این شناور همچنان تحت کنترل عملیاتی ارتش آمریکا قرار دارد.
این در حالی است که رسانه‌های ایران حمله به دو قایق را به شکل حمله پهپادی به «قایق‌های صیادی» گزارش کرده‌اند.
به نوشته اکسیوس، این دو قایق در نزدیکی بندر کرگان و جزیره لارک در استان هرمزگان هدف قرار گرفتند و احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، حمله را به ارتش آمریکا نسبت داده و از مفقود شدن شماری از صیادان و آغاز عملیات جست‌وجو و نجات خبر داده است.
این حادثه در شرایطی رخ داده که ارتش آمریکا تلاش می‌کند با افزایش تردد کشتی‌های تجاری در تنگه هرمز، عبور و مرور دریایی در این مسیر را به وضعیت عادی نزدیک کند.
یک مقام آمریکایی به اکسیوس گفت ارتش آمریکا و کشورهای عربی خلیج فارس در ماه‌های اخیر تردد نفتکش‌ها از تنگه را در طول روز نیز آغاز کرده‌اند، در حالی که پیش‌تر این عبورها عمدتا شبانه انجام می‌شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=bJcl3h3zXxMg3y_GSaTH9hZ4NwjIqLw-Jl_f5_rxUO4V3QhV9GxTJSOveGX4b1vry4SUAz7IYCU9gmIABoYbpMdMkDRgYI8tg3YG9OmNxcBRFtkeB8UrGRIsuZWhKdY1g-bnasSY_JYI-gDT0CL0h2aWxCYr6kcotGVg0RjW0cIoEWhrpti5RcdMSL4lwnljs0blMC4VyeBOfQVpwcbqL0weNDbVAfLRWRngcq9Axaa_jDhtHuiIO6dV7yN0SGIZhd3SsunNZSqSvbRC02zNN70xHyeXsfO_KFAA7bl0_drbWl1DVNZRcDDPb6tyjqOk6TBcY-oIUxIsfqgTd0FkbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=bJcl3h3zXxMg3y_GSaTH9hZ4NwjIqLw-Jl_f5_rxUO4V3QhV9GxTJSOveGX4b1vry4SUAz7IYCU9gmIABoYbpMdMkDRgYI8tg3YG9OmNxcBRFtkeB8UrGRIsuZWhKdY1g-bnasSY_JYI-gDT0CL0h2aWxCYr6kcotGVg0RjW0cIoEWhrpti5RcdMSL4lwnljs0blMC4VyeBOfQVpwcbqL0weNDbVAfLRWRngcq9Axaa_jDhtHuiIO6dV7yN0SGIZhd3SsunNZSqSvbRC02zNN70xHyeXsfO_KFAA7bl0_drbWl1DVNZRcDDPb6tyjqOk6TBcY-oIUxIsfqgTd0FkbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/blGitUkyQPqV5vuphxihIYv8i-M_EiLchBGleK9Y8YdYZx3CYgHb_gSFaxtMUmuupCVO39TfEe1Gjp_bE711_XmdIpTvuVdmfaFkJ6z3wgXl17496aCMa6xCw1BXTh3mP85Hvd3pzcncdyLWz3-ZIf6f_5Yj_Knjx_LxirFuG5vqtvmF1HRTm7CKaYqXLYbgzFBtKyZsAiuehW-amze9xNZ7Kh5Sttr2s4D-lYKgoIE3jVDjW6h5LC3ADO_uRiyPzhuUdYRLCcLAdh9oMtIY4_jApnld66N0TiW9xRjp1QQA06V06X8eZDQMDj3NtijkXAlDQjSgx4rV2tePvOws5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9fx7ndlURTs-H5JcHst-7hi1-TbVIQr7cIpSTPn1YwGrX8qHBPmNsWCmR2N0i2CDrzAzpIkdMgrh6UrV1K7lT2ouJCyxFI_xof9l0adQ5zKQgwIrxtbc_xokXq03CbV7ZxiEWobnCcxeonuoMwaF5gtAf3HZRmZoVNu14rY2R2T8IP8yHDyzF6hJUwZVi7NPBgeb9CPZqfnUXuF-N2tvoElNiE1yMCH7awzmyjpdNbBmw3d6IQRVIWJNsPV__qKiFBYzX6tGfeqkeWbsv8pAyxBumpdGOikL7aMHAOyY4xdp8rUK9-EgIMo6Y6GXke4tE6sTWqk084ELAiU14n5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9EiWp_dh06RH6wnwBuvg7jGilkMtV0okhnSmIGsjLyZNOATJGzUvgY4G4-3gxdWgXpcUjLc_WD082NotOFvL-Q728PKkFGjc18kqT5AwmZg4coFdw25-hpnNN9Pa2RIc0yZucUlaVia0mUOn_yFQeC-2ztiCryxByCKH20VYIFOxoj7iNoYXuyvn8j2MDMATiuMTcL4wesVcADXj1JfOI2iqlGn5nkB96CQ0OaTgGXGcHqz35i7vUgHK1aiJYtuTShprncqr_3_oaaojS2wIcZhv83fP4bPbRZslQatnTQ2IWvvkX-SCSLooBV_DtARK8WOTI8n0O_WbEtZ9VsMzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lyc-aUbWMl_a9_g-z9mvpVeKjxEtbllVGVyFF-uESP2ZvMj9HEdebgTvBiIabi6t8gg4KBri1tSg9m5v-NhqFbG7w-z0KV_tncXUkQ1zYLfdTGJ7scqmnY5CTRjWFcrRb5v0hy4xQrvcfYhGUBoEH2Fw88CffaoeSPPXkzbxzuengayfNOE_8ZoEPEMIdwwwvX-n7AT68gxSytpi3DItS22W8pKsnOsoWQiDgEoGSTgKIfSt4V1KgjumaD9j6mhY4Cvw5W1OqCdqLfBNrNXL3hmexxPRiSSPMN0HS5GoQO_ep1Q73cfZCuKnB3RyNztw7uHGAyWHOv54kxNCpRJcgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش رسمی آمریکا از هزینه‌ها و خسارت‌های جنگ با ایران منتشر شد
یک گزارش رسمی نهادهای نظارتی دولت آمریکا می‌گوید جنگ با ایران به «کمبودهای راهبردی» در ذخایر برخی تسلیحات پیشرفتهٔ ایالات متحده منجر شده است.
نخستین گزارش رسمی نهادهای بازرسی دولت آمریکا دربارهٔ عملیات «خشم حماسی» که روز دوشنبه ۲۳ شهریور به‌طور عمومی منتشر شد، می‌گوید مصرف گستردهٔ تسلیحات در جنگ با ایران «به کمبودهای راهبردی در موجودی‌ها منجر شده و گلوگاه‌های پایهٔ صنعتی برای تأمین مجدد مهمات را آشکار کرده است».
بر اساس این ارزیابی، پنتاگون برای مقابله با این مشکل در تلاش است روند خرید تسلیحات و زمان تولید را کاهش دهد و ذخایر مواد و قطعات حیاتی و برخی مهمات را افزایش دهد تا در شرایط اضطراری امکان افزایش سریع تولید وجود داشته باشد.
این گزارش همچنین نشان می‌دهد آمریکا تا ۲۹ ژوئن (۸ تیر) حدود ۳۳ میلیارد و ۴۰۰ میلیون دلار برای جنگ هزینه کرده است. نزدیک به دو سوم این مبلغ مربوط به مهمات مصرف‌شده بوده و ۳ میلیارد و ۷۰۰ میلیون دلار به تجهیزات از دست‌رفته اختصاص داشته است. بر اساس این گزارش، ۷ میلیارد و ۴۰۰ میلیون دلار دیگر نیز در ردیف سایر هزینه‌ها قرار گرفته است.
پیت هگست، وزیر دفاع آمریکا، اواخر ژوئیه (اوایل مرداد) هزینهٔ جنگ تا آن زمان را ۳۷ میلیارد و ۵۰۰ میلیون دلار اعلام کرده بود. شبکهٔ ان‌بی‌سی نیوز نیز پیشتر به نقل از مقام‌ها و افراد مطلع از برآوردهای داخلی گزارش داده بود که با احتساب هزینه‌های گسترده‌تر، رقم واقعی جنگ می‌تواند به ۸۰ تا ۱۰۰ میلیارد دلار رسیده باشد.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه و همزمان با انتشار گزارش ارزیابی «عملیات خشم حماسی»، در شبکهٔ اجتماعی تروث سوشال نوشت آمریکا اکنون بیش از هر زمان دیگری در تاریخ خود تسلیحات پیشرفته تولید می‌کند و این تجهیزات به‌طور روزانه در اختیار نیروهای آمریکایی در خاورمیانه و دیگر مناطق قرار می‌گیرند
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgS21h-Ag8RRMAfxc5tjx_6PpU0n6wNYRi3ljyqjFPMHRkMXSBdmg2AOJPZUarfzC5FxR_GmnIqXNebF7HBs9vHHky-hJu52zvF9iYaWji01Z3Cw-QvgCxZgTxxLXTDIEfadDrU9MM4_Qbsf1tOWeasQW9hvv_xTgxlNVjVkBH8uAEoNTQNwv4rtgGUIV0d_fxqO7jfXw9gngr0YDqZmjRB2VbAtLbiJSJ0Apa7JCSD1fbJflD8rCuzfkjKr7SkxiYwIP3ekYszeQsDlW3JTjRzUIdDNGDaT6VtN0r08x0GidoBeIFB8jQ5glCk1nYirx86VjbnUTbU9tTiwnWYVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eeepsAF-S8kyayIr8lfN1shRm4TS63Q4FKJDvQOL9T9STCyLVT9Irgdo0om99KGYxqB2C_ikzcrreL83YhFl3R11rJDCdRM77N4ELZ6zY6runb0QWVy5n4D5KV2V3-XLiEHvcAgg_H-j1NAmvS4tClMMXjIzfpgdqCMatFED-i_YP2RzCDY6pXUazcrRNZ6ErbWQT8VtoKTkJjcLFsSaecCDwEPbmel6w14V6lsQ4rZA2i4Kq3flTgEdBdDh0FpvUQxYPjLd0fHT98pK1ZuXQx73utZe3BSEMovLT4bR5J0npkm2RGGeKzISa0ckTlG9ochvRBSmioIKId8H2Z5tdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uwf-jxiGgUC655BZdZNIByNfkcM_FVYKUOiZc9DwAY6Hor0-crttqH2G27IoaaSqTHcuN2PKGTIJzzHIJ0Pj7oZiUxM2r3ztOEqUKgpX2EiCeo1Bnj6Qgxa7Gv3Ug5k5T09_OwLALhoc6Ir2IfOsigLMcxMnBmvcCT789PikTOnvY4QgVAOEIES6Zcx-Mzw4njwEINH41TOctcxPHY-buP-GTkX0hx-3sM7M9TgLsxS5fXAAqKApmJAQrOHBi76IhBehh0XLttNDtUUnBm-2WNHUlLc7FJfZ2_dD65ONB2DalawCNz47yz1ZYoBF-TpqpVSqIoa_tMbcuOEIPvVIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sOt-BOiukEs9y5Eb2m24qdz-qwaoluwKJOyISzA0CviUVOZfcRsNfl7pF9DcLFfNS1eIBR3lw4oPBc-aoKkT8OYxH-JIWUTBcqPCgdTJxpDekTfMo9g7H11L9Tkh7DYDNfMIw6qrE9BarQBn7q6ba35WJG0rlBxYIDbOkJ4YPnusScFOLqPP8bXl0iztS22ksSF-5gFA6kWSm4rtrqPTb7E8oGO3M_ysQ0UymFsjerXmaauswN_Tof7c0c_ey4P8JrRTqgTOBkHiTfMRpvHsoKzmPqLWIMgmN_R5hMWAfmx-plNqjxcgVgE17ICwvcgg8oTIeb7mDLJaOR2u5BTf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iNnNQyl1Nx6dQyhtm9X0TNRnt9i_CEnIDVmjOdJ232_vysTq30diuZMpohRU6XdnXSmD44m2uTkqK5cEHinyrbn3gZjLQyRpSY0JaTV1ABJcDrQ_Q1ec0m8YKH3JQND3Zn56sCY0XrIU3H7hK7iGZ27aJC3F1ifHv44qEn4KXV17kL1YJ_-GfsqZ3IXDjMSCqIEhxzEXj0sp8N2nnhkjNVjTeLOuWm_sFzqNRugsn0adGS5BGo_5mcfXMmog8q4jnZ15NkTNsZmbthNBU0wmiJx503rzWLLmGr1KpyIKsWUD9oUzjwZ0RjqEN4NTSGNCBshdAno-NeetwkswnosfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L5S5wZG1N6qupkqeNSSoA8vv2tA6dgPsFbf9Qc-sg0pfxNcHQWLomCB2EOZmjEXpIRrZWKX8X1LIeNlHdjb66wCmq-peUtMnVztUfeIxCyRmFkHsr8dfw7Vc-t2lB1chLi5rR-FMAIqVjOgBfCAjw58c5qlBpIoST_Kh0W7ofdwkm_MnB6r9f55egGWdb26FKgr89BwocRj4XLoY-JCP-QpYrMiFWdBrcVqQhrCC0c5no9M0bjMYY9Vx1oHPyQjhinktxMLV-u9CmdoShliQ6__NpGjQKwyoN38S_FC9e4uy7gF_bcfaEc4pJOWGuLLlVDRUmfkNj8AtmkjRqEa9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lGsXgk5G-7pbn8sonSp_mN7EATc4atJS09uBg6RN_XDV-Ojyc-B1jrgatqRT4SA5WLq267-6ZxnpJZvAOYJdFs-NrbqN7uV9BJtaLTjJOAjdbtop3XI64IhqJ7UPVuIm_aXny2ISFCumTsRSifR9Vm9RU4rVFwmIzMSM85Mi6Eqc099BUljw3jpactarDaLgk0p4aa33enTZr14l_u_9a2kSS3QGH3ykoOnfI3VC_y2nhYOthf-AMOJLH9ymlczezZ9CBgKlsmCSDpHJl6w-8YZBKsq5MGT2T91RaROak4ZQwKwvU6rwZokb-hDXVJWm_JzZTRcsDitmJ6Td6VRuVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbBRubYf6dbXb0dm4_FEF69bAH-UQrz7jbO_09LJoYK0ZYTPwhW29PMTRaLSKgOH-A7phQ37Z0BJ9uIExjo44P_iBSZ1hFsj-otETqq8Xe08oyx8ZAY3oky6X5gnL9l25EiwA_Gp9WeF2ZiZp08YdCCRjLRVsZL-OfJUcc7yn8B3wB1XIgd0hcLO7fooY2nVzRDyuFV58OAtB_ilFuXZl2mWrgi_DCrGazPNpER2Bhy5MrePWlIaiaD-kOBMGFN9CwLdeWSVtF2XJs3vjIto5UD1rJRXLu1fPjLmqotIMbVTa-VEvI4yV5t1vNOKLY81QTb_lHl9PPfSha8NFxgLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دادگاه فدرال آمریکا روز دوشنبه، ۲۳ شهریورماه، به عدم اجرای دستور دولت دونالد ترامپ برای محدود کردن مدت اقامت دانشجویان و خبرنگاران خارجی در ایالات متحده حکم داد.
‌این دستور که به گفته قاضی دادگاه به دلیل «استدلال‌های بسیار ضعیف» دولت صادر شده، قرار بود روز سه‌شنبه به دست وزارت امنیت داخلی آمریکا اجرا شود.
‌بر اساس قانونی که دولت ترامپ سعی دارد به اجرا بگذارد، روادید دانشجویان خارجی و روادید افرادی که با برنامه‌های فرهنگی در آمریکا اقامت می‌گیرند، به چهار سال محدود می‌شود.
‌این قانون همچنین می‌گوید که روادید خبرنگاران نیز نباید از ۲۴۰ روز فراتر رود.
‌هر سه گروه، بر اساس قانونی که اکنون دادگاه جلو اجرای آن را گرفته، برای اقامت بیشتر باید بار دیگر اقدام کرده و روادید خود را تمدید کنند.
‌به گفته قاضی دادگاه فدرال، اجرای قانون جدید تعداد دانشجویان خارجی و روزنامه‌نگاران و خبرنگاران در ایالات متحده را به شکل قابل توجهی «محدود خواهد کرد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KugOpOInxznjKLWrX-o-HVtcdKP1kSUEHenyAZXsMJZ-GN-VPVk0IL227A3ulo8hYftnCNbR7NBCaB6sZ4L25TyxaUqrSnkzlTTLkNmhSEHcE2sIXuiArTLgdkAV9hCj78bTeV0McfTNg3U3Bp2FIXvy8Pj3mVEBeTPYdirqM_rBrBLHd8bFuURGaTh7wl-TBf1O_w5df6J9gV-nDizrX2F09YiS03izsFaevIW4ZyCwLsaQZbXM9Rn51rDlZ_pJqyg7qxmco9dMXsrBGNgXx_qekEr1ndJ8EBnAE9d3lMhAS2lnF2pgxj3DQCiTyEq9sMHKsZEFd_afJekLry4bLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgNRZBPU5gCELO0_DA-Pbi5hZh8_yG9KDUcheuOWvymI4T9mUrJTIGl62KnfwS15eAwK9VYasN0i87UW5uFViHriRcsMmj2wGJnoe-ssGWVK1SeiUySf-rnoViA4TX3HI7VqFzezyS5FdqyeJerOobnl_q6etbF5fJyEno3JYgQig1JoFuLsfsr9CkhmtFoHBAy764uCRuKLS3x7yS4g1APRt8jWfJU7CAOoHkiKCSYg3XU4-qssezt4K52CjaDx0hRWfQPyvfT5yEdmTwe-an_0pz52AgrMJ5V2U85tQYxv3Bz81SdwHvQz9AqWa9MtjhvxlSydf4QOYPNSg_8R9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش الغایا پس از حمله در سواحل عمان و آتش‌سوزی در موتورخانه، به یکی از بنادر این کشور یدک‌کشی می‌شود.
بر پایه گزارش رویترز به نقل از مقام‌های عمانی، ۲۳ خدمه از شناور تخلیه شده‌اند و دو نفر همچنان مفقودند.
روایت‌ها درباره علت حادثه متناقض است.
سپاه پاسداران اعلام کرد الغایا با پرچم پاناما هنگام عبور از «منطقه ممنوعه» جنوب تنگه هرمز با مین دریایی برخورد کرده است.
فرماندهی مرکزی آمریکا ادعا را نادرست خواند و گفت شناور «ماه گذشته با موشک ایرانی زده شد و از کار افتاد».
سازمان بین‌المللی دریانوردی گزارش داده بود الغایا روز شنبه آسیب دید، بدون آنکه علت را مشخص کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/78380" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lhBAS7QikY0vLVJeXZuQZLLDvEgGw2V1IaC0ICn94cip6RPoq91uiaratpe2ZJuVlKISr_EZTQUJDkmVZNES0zVu9vsqBHh9tWSONz0bDltNUBFkrXiVOl8B-lfLz6I7e-1ryfNpRQgV1CHFltutfg-k90n0m8VQG_lLFXo4vNGHQopgJdeEUmhK-N2kWj_lB1D5ni6iMD38gwdKOFknpBW8ZXnU4Ev4rkb8fXR2NdtfmD5OamoOTizWbTbjer52WPcCXCmz7nrOx_aOLZovy8zt0cAXTwekb4zsmf6ftIyHV8Pqv7cSqcYs4CuObq4jnLEDtwj2VOIrnyPt55m1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qcl8o0VUp6DwXU4uFBHHLWImvcarGUwAoHUthNrHMxYixSEZ_vZUOJ_jFse-f6zrTjrjfhDtnF59klwAABqhul0eurU9RPXApHwt48e_Pfl3fEk19MeDgQZjQ9d4KfGKg565FZEBC2pUPMC47_bcvE8YO6O6Jr3GPwuCRySWQbMoM_b2-vTizOFb1XdqNWiqfGmA6uDFH34tUckBqNsh-Msjzfg4uWnisdRheWohOtGtse1tCW7Z8Wf0o1miah8bqRW2CqLltP8K4CtNYglnTExQwaGYXIFxJ7YLOtyecXF1_OUcM_PE1w5RS0yYbw9KlrLm5ioh_EW6t9P9sXw6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، شامگاه دوشنبه ۲۳ شهریور ۱۴۰۵، از حمله پهپادی به دو «قایق صیادی» در حوالی بندر کرگان در آب‌های خلیج فارس خبر داد.
بر اساس این گزارش، در پی این حمله که تسنیم آن را به «آمریکا» نسبت داده، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند.
عملیات جست‌وجو و امداد رسانی برای یافتن مفقود شدگان آغاز شده و نیروهای امدادی و دستگاه‌های مسوول در محدوده حادثه در حال جست‌وجو و نجات هستند.
تسنیم نوشته است جزییات بیشتر درباره این حادثه و وضعیت صیادان پس از دریافت گزارش‌های رسمی اعلام خواهد شد.
@
VahidHeadline
آپدیت:
اکسیوس: آمریکا دو قایق سپاه پاسداران را منهدم کرد
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cn-3ZI_fy_8rDDsh8-KYgIbIUiSpmoAbYfrITddy_tY8v5iYK5VgCNF9pv9gYFriUgDynlYI05w_1LoshDwmQ0JLxYXwf_xxfuEtlFpEnNiXaGNjhCohAowl8UvCtG4XA7RzDywzfNZMKfEQhLXXMjU0dskSw1LHs6hyoFSU8xbWfLJklA0urK8DtN0BVh1mxEBWuE7khABq_-QbsaWrPXCg17lHI9I5_2VFZUu6fYhPfccQ4u7vI__1Lyppb5EJHcNd2_82uIIewPNwHROhpKxWzTCv8vhAtc3mbmoBRS2vlWssYpvaYy_BbMvbhZ_BK5gQqV_SGlaQvgyY2sZNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی نیروی دریایی سپاه می‌گوید یک ابرنفتکش که به گفتهٔ آن قصد عبور از «منطقهٔ ممنوعه در جنوب تنگهٔ هرمز» را داشت، «بر اثر برخورد با مین دریایی منفجر شد».
خبرگزاری‌های ایران شامگاه دوشنبه ۲۳ شهریور با انتشار بیانیه سپاه، نام این ابرنفتکش را «اِل گایا» به شماره دریانوردی «۹۳۲۵۳۳۶» اعلام کرده و افزودند که «تلاش برای مهار آتش بی‌نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است».
فرماندهی مرکزی آمریکا (سنتکام) این ادعا را «نادرست» خوانده و گفته که نفتکش «اِل‌ گایا» که با پرچم پاناما حرکت می‌کرد، ماه گذشته هدف موشک ایران قرار گرفت و از کار افتاد.
@
VahidHeadline
پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است یک نفتکش با پرچم پاناما اخیراً در تنگه هرمز با یک مین دریایی برخورد کرده است. این ادعا کذب است.
✅
واقعیت: نفتکش «El Gaia» با پرچم پاناما ماه گذشته هدف یک موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، ایران بار دیگر این نفتکش را در حالی که در آب‌های ساحلی عمان قرار داشت، با یک پهپاد هدف قرار داد. این نفتکش در حال حاضر توسط یکی از شرکای منطقه‌ای یدک‌کش می‌شود.
ادعای کذب سپاه پاسداران نمونه دیگری از دروغ‌ها و تلاش‌های آن برای ارعاب است؛ آن هم در حالی که می‌کوشد مانع تردد کشتی‌های تجاری در تنگه شود
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WIgeT8blteWiM-obgzAJE_wMFsD7wXQyhghfpbFCohgBscMg-0EcQH2vE74_B4DaaIXdic8qBqNnjdW3xxmnvQXVeg0Qp-794ZoAJzq5UoZ7O5k3JAVd0rxdaHyqvQSuWztxPh1Yl0YPr2Gb_RL_G9w6_ifVXeW54H2UiAl9RAdYKAt_izc3gqYQz4JP-_Yp2TsDnp8EeNoVxtQL2YknGhLKkKQSV1fG7F9HpElnVBsDbc4gSIZoQPNEo08pOxWxAH56M9jAG71u9_6DUmLOh1mfGdMXmQGaTWFbQHsxFo0Ck07FyeUA71-wf6MkeSvJXTCotYXdmqgokklU33VIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hw677o7CebfLvtMGHQeqowAb34KEJj7xJrFgLmByFJmP1iBS5xenpsWIXkFAOZ_rPv_g_hEV2V8JtgJyHTiSRdLXXQ-k_67802tOYuDu3SmigdjwMwTy4X3JPwh1grH-TavBhWpErqBbUeQ7upnZz0kMeDED7-NmdDoRgT8uO64aILSKQITduMQoJ8oSuylUMnUgk-toCwpw0h2MUv0DheYhaE0h4gf0TkYv4iB6TTMjoFQquQd1u4LjVnS3VDIQe5BDh2XRbdVR68nxoMSlHtLCzWq9KZb57d9bKU-Xuit_EH2-ogq0wdNc6GQ-0RGwbugMWv_GGz_RfVuCaD0s2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پیامی در شبکه اجتماعی تروث سوشال تاکید کرد که افزایش قیمت‌ها در سراسر آمریکا ناشی از سیاست‌های جو بایدن و دولت او بوده است.
او نوشت که حتی بهای نفت نیز در دوران بایدن بالاتر از سطح کنونی بوده و دولت او مانع از دستیابی جمهوری اسلامی ایران به سلاح هسته‌ای نیز شده است.
ترامپ با اشاره به اینکه قیمت سایر کالاها به شدت در حال کاهش است، افزود که بهای نفت نیز به محض پایان یافتن درگیری نظامی با ایران—که به گفته وی زمان زیادی تا آن باقی نمانده است—مانند یک سنگ سقوط خواهد کرد.
در دوران ریاست‌جمهوری بایدن، به‌دنبال وقوع جنگ روسیه و اوکراین و بحران‌های بازار انرژی، قیمت نفت در بهار ۲۰۲۲ به بالاترین سطح خود رسید؛ به طوری که قیمت نفت برنت تا حدود ۱۲۷ دلار برای هر بشکه افزایش یافت.
@
VahidOOnLine
رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال از کشورهای جهان خواست پس از پایان درگیری‌ها، هزینه‌های ایالات متحده را برای حمایت از کشتی‌ها و کمک به عبور محموله‌های نفتی از تنگه هرمز بازگردانند.
ترامپ با اشاره به اینکه نفت در حال عبور از این آبراه است، تاکید کرد کشورهایی که هیچ کمکی به آمریکا نکرده‌اند، باید خسارات و هزینه‌های این اقدامات را جبران کنند؛ زیرا واشنگتن این ماموریت را بیشتر به نفع دیگران انجام می‌دهد تا خودش.
پیش‌تر کریس رایت، وزیر انرژی آمریکا، اعلام کرده بود میانگین تعداد محموله‌های نفتی که با حمایت نیروی دریایی این کشور از تنگه هرمز عبور می‌کنند، رو به افزایش است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g4rzNCc7SZXhIUEdZg2hRsCmU3AO3UsC_aefnxgehGpchcLqoSmmd78vYZLAzyRfkiNSYKoGXvZK_nmeGV3u_dJetSn45_LVTI5TzeVbuLBfiGvf5YrSros2GfBcxZ52s0UzOtScLeR8zvl0CG36AuBNsuE8VNcwjItzV4aQ49K2KWNRgLJoQQqHAFuhib7cGTNPafm-s53RNWEQ-wmuQH7uDYtujhZl4ZmeUbmSsRip7xIfqYiHxlR-fur1YnHoVvdoyN00g3VTOnkDnsbfbqW_XfdTXGMNHJUnu-Ceg-TkvZseKQMgMnmiqm-2uWkwSNeCkGY-ZTj8PJmeFLPvgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایرانِ شکست‌خورده می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
من تصمیم خواهم گرفت که آیا ایالات متحده آمریکا وارد مذاکره بشود یا نه — ایده‌ای که نسبت به آن آمادگی داریم. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
ترامپ نوشت: کشور در حال ورشکسته‌شدن ایران می‌خواهد سریع و به‌شدت به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا وارد این داستان خواهد شد یا نه؛ چیزی که ما نسبت به آن نگاه باز داریم.
پس از انتشار این پست قیمت نفت اندکی کاهش یافت.
اظهارنظر اخیر رئیس‌جمهور ایالات متحده در حالی است که ایران گفته برنامه‌ای برای مذاکره با آمریکا ندارد و شروط متعددی را برای توافق با واشینگتن اعلام کرده است.
در همین حال، اسکات بسنت، وزیر خزانه‌داری آمریکا در راستای برنامه فشار اقتصادی بر ایران موسوم به «عملیات طرد اقتصادی» از همه افشاگران خواست تا چنانچه اطلاعاتی درباره «تسهیل‌گران تروریسم ایران» دارند در اختیار وزارتخانه تحت امرش قرار دهند.
او با انتشار پیامی در شبکهٔ اجتماعی ایکس خطاب به کسانی که در سراسر دنیا اطلاعاتی درباره شریان‌های حیاتی اقتصاد ایران دارند، نوشت: «این شانس شماست. اگر اطلاعات قابل پیگیری برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت جایزه باشید، صرف‌نظر از این‌که کجا زندگی می‌کنید یا چه کسی فیش حقوقی شما را امضا می‌کند. اگر چیزی دیدید، بگویید».
او همچنین بار دیگر تاکید کرد که وزارت خزانه‌داری آمریکا عملیات طرد اقتصادی را «برای قطع تمام شریان‌های مالی رژیم ایران و حامیانش» آغاز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=vTCguMlw9b6tMsV6QMmVtQMEZVjkRe1N-jFpvPebHZDUI8zlK0ySA9kcVjs2ZNdcNQ8D3JBi6oCbv5IpZ9joYGtVMJh7gzV-rJnQQe2o1o_ubGBjuX3qXdMo4cGIvoKQQIX8Dq9cGrawg0UNRa6yL94zX8J33eWP5fD2ZFGALEvB6yqTuIwDE-jsk_aORVmzSDs5jcrEK2qah2DjUJsPEJL6sCDxuzzCEtbl0ZpM0gtzPF56IdZ2jVpRkKHQXsz7mRREh5amnNC3fEhJ5iqvJAnIORsV_LTDbXrNdGdaEoGNDAzWzcOL9kxeY8FWj6Xfdexf81kn47RiExXHcc4wXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=vTCguMlw9b6tMsV6QMmVtQMEZVjkRe1N-jFpvPebHZDUI8zlK0ySA9kcVjs2ZNdcNQ8D3JBi6oCbv5IpZ9joYGtVMJh7gzV-rJnQQe2o1o_ubGBjuX3qXdMo4cGIvoKQQIX8Dq9cGrawg0UNRa6yL94zX8J33eWP5fD2ZFGALEvB6yqTuIwDE-jsk_aORVmzSDs5jcrEK2qah2DjUJsPEJL6sCDxuzzCEtbl0ZpM0gtzPF56IdZ2jVpRkKHQXsz7mRREh5amnNC3fEhJ5iqvJAnIORsV_LTDbXrNdGdaEoGNDAzWzcOL9kxeY8FWj6Xfdexf81kn47RiExXHcc4wXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuliKLqKhEnyNZdm7nGvBAgKWjNOggqDJod4Hve0HbLIuhymCg9Wco3-t5SsJ3RXWDRkqgs6FSpcJyg7mYN7XAeejX-E0eje5_mFUU6LrhPTkW8fHYHe9I5U1aILWjTw2gYMFnCi0iHwsUxD8_vY68oMrRaAZKVVSL0Ai087aaRsdoEKfINcitJuA4cm6cMf-RB3NzGsTfp3JnyruT0CBkMWjCXkFfh6sMwr7FvfF4Lu_d0yCHm51lv57r_UYFJ1Pl12aJNaX5sJ04K3I-YxcjclYUYaknzns6RYiznwuv5zwiL2IciKCoHusuzzGyB3pCYquc_dHA5bkrmrNMExkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=jmYC1t17K6yfI4TQJS9Jht7cpSHH6ffLW4u75cwiAVLhTatAXt3wAL9ZpGw2QLOrvwB7JfX6OnGtAZHc6hUXHcD4mm9HIXqfFcjRy9TiNikHSOZyVlWARS-KoWWEwhiMjZI_LnyVT9B5YWqAOUt0x6nlO-ub8biOylXLid1KFajuIxzlUyB0r2YGOtNdfhTZxB5zhJieseukQRR0dQjm0np9QaYHYtyWYwIIj1Jfr8E5Xw4A6YdSOeTR9ByDOKvyRbvO7SvMMj8T9AdWwoLlNwgGBpFVPJCbz3eJLfpcmNtW48l4stHGle5WezDDIotU670nwduTm4hXJsh_H0w9eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=jmYC1t17K6yfI4TQJS9Jht7cpSHH6ffLW4u75cwiAVLhTatAXt3wAL9ZpGw2QLOrvwB7JfX6OnGtAZHc6hUXHcD4mm9HIXqfFcjRy9TiNikHSOZyVlWARS-KoWWEwhiMjZI_LnyVT9B5YWqAOUt0x6nlO-ub8biOylXLid1KFajuIxzlUyB0r2YGOtNdfhTZxB5zhJieseukQRR0dQjm0np9QaYHYtyWYwIIj1Jfr8E5Xw4A6YdSOeTR9ByDOKvyRbvO7SvMMj8T9AdWwoLlNwgGBpFVPJCbz3eJLfpcmNtW48l4stHGle5WezDDIotU670nwduTm4hXJsh_H0w9eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A76QBlY_v4ZlCpVUtjvpCgMNW17rgXHDfium6EeO_4lFr65hIcs6sur5KjtBCqLbPK0qeuOWXDiwMp7FhK-OLsNBwrGPGvnLoMpPZKlbj3JaZ-v5ApMgLEOerq9ZEfRNwvDYIt7fJiQ1RcRRA6hpEVSmwgT-JAnl1HkcGxtiBkP519Ul9VO0LlzK2U4Ok5ZoFAjubzcX7ibRGdf8q2MmAEVeYg9FpUkh3wC4st4kAVLNuVVWqhqZBSl9NxL3YcvIcnpEis3P3FUq87zBi4WkCv9-5ASs601wTtNM7jCfVJeABcCv3OOkG77Vup6VB8_uPoYVHzqyzP2aa7iMHHbIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rNUqs1RprwqamTrkmJ5gOvj6rVTFWdx5BX8TizmiLuj4Woq16sHSw0IQKB-FiwVzcxwKylY7wy3WDrdqJaFe8XjYlP_8ka68ERCxv64_pYOO5t9_WVtNNm7XxBbFPiaG2eh1ezY8GJiZA-S_0hN9gSX-vB-slm1fs3XW0-GfW8u8mNnITTxKIH1TKAmQxWT5mv207_3D5dR3BDlPtEGdK2gaP75Vv7ESDdUaB99IqiX0lQ2K4YKrOb4xFISwO5uxanAM2K3aLehzRrmct_mdcTzOP4C9XN-xlbRWb9wqaZt9cpT-pfVJ4w3FbbQbaJFiXt6ca8O1wEZrqvKdm51ygQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilmhu7bb2XOQB1GEPv9uT1PLWS8EDVtVslexHjrej7Q4YDBN7IR6KgS_A73TkQM9DC2TnZN5EcHt8NrVJC9ykIizYWoGDhlj_Cidvn94VCYttieNhIaFIFPIMDg6XXWKzymFYLqqMVrnGv25KeimgbxCQ3zKuz9miQe9B3xRMmmU9-mA5eqv4jy_NOT1jPsh8lWDIsm7kqeRrHU3hLIof5_X0OtBd2Zw794B0Ako6HZyMh3yZCddXQMpyUZaBb-mlO5rBVxiQFoj0QfgbEb79Jgx5Ft1LJY82-udStR21lmg59abdWdUPqUwAJyk9xqH4sX6V0t4xe72dHfHbPGW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
