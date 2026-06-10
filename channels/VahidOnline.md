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
<img src="https://cdn1.telesco.pe/file/L-Nv1sQHRBgGzLFTmRvxT6jnIwhrhqhAZHdlA09P6NusykDvqr9Vw8uIBZ6CpoSrLsw2mszoyTr27MNWEWkT-5eRKfLKNUdAa0HB6kwQ8yBQpeHI4LRlY__fK-ZdpCwud0v54z0DCX2nCFetRCJ5CQharleht8m5iIx-f2NXGHpKLsE-4VzbAys5G6C4kwNxXo7qAu2neAOHlHpog8DUPWGZBSK45qPVXHmUxxGHH0K6m29WzfviJpW362YAtW7bvmfS4WAq_vNDKjj-Juj1znaN74cf3ANTioCWVvX3RRhQakUrlMk53KdgjcI6nyqlpE3didstW0DXHxfOW1H7mQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 10:30:37</div>
<hr>

<div class="tg-post" id="msg-76132">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2b79c4913.mp4?token=Hr-3iqeKtvXzbJF1ulUzl9BoRxdHG1C4LHU0UgoH6mHl755WRVY_yF1DvEf6IRvCQfLD5jakw3dpkpD5HmMPlq-PhCe_6EiP7EwrWIKRR07R9U0RxtnH4xL3KzhK3bt08-ZWT_yHu237YodXRtyBtKmskNfryVSC-WKsaawWNQGru_DxWwsYLi48G2eoLW7tuxzOSsFL8mup2doMuSkQOONEw8cMNb8gORFYaX4IABKLJUEj9NyVWSu-yUH38wfGtfkPV3dcB6pysuTnbmGJmQ2Z-Da6ATIsV-_lFt82VVTneJkZGNntMGLoszK6k2xIAIAAq01I85dKuZ4s3InQdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2b79c4913.mp4?token=Hr-3iqeKtvXzbJF1ulUzl9BoRxdHG1C4LHU0UgoH6mHl755WRVY_yF1DvEf6IRvCQfLD5jakw3dpkpD5HmMPlq-PhCe_6EiP7EwrWIKRR07R9U0RxtnH4xL3KzhK3bt08-ZWT_yHu237YodXRtyBtKmskNfryVSC-WKsaawWNQGru_DxWwsYLi48G2eoLW7tuxzOSsFL8mup2doMuSkQOONEw8cMNb8gORFYaX4IABKLJUEj9NyVWSu-yUH38wfGtfkPV3dcB6pysuTnbmGJmQ2Z-Da6ATIsV-_lFt82VVTneJkZGNntMGLoszK6k2xIAIAAq01I85dKuZ4s3InQdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
realDonaldTrump
چت‌جی‌پی‌تی:
ترامپ سکانسی از سریال معروف سیاسی The West Wing منتشر کرده است؛ سکانسی که برای مخاطب آمریکایی معنای کاملاً مشخصی دارد.
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
اهمیت انتخاب این سکانس در این است که ترامپ پس از حمله‌ای که رسماً «متناسب» توصیف شده، پیامی دوگانه می‌فرستد: از یک طرف می‌گوید پاسخ فعلی کنترل‌شده و محدود بوده؛ از طرف دیگر هشدار می‌دهد که محدود بودن این پاسخ نباید به‌عنوان ضعف تعبیر شود. پایان سکانس با تهدیدی روشن همراه است: اگر آمریکایی کشته شود، پاسخ بعدی می‌تواند از چارچوب «متناسب» خارج شود و به «فاجعه کامل» تبدیل شود.
با این حال یک نکته مهم در خود سریال وجود دارد: بارتلت در نهایت توسط مشاورانش از واکنش نامتناسب بازداشته می‌شود و به پاسخ محدود تن می‌دهد. بنابراین ترامپ با انتشار این بخش، بیش از آنکه کل پیام سریال را بازگو کند، بخش خشم‌آلود و بازدارنده آن را برجسته کرده است؛ پیامی برای تهران، و همزمان برای مخاطب داخلی آمریکا: «فعلاً محدود زدیم، اما گزینه بزرگ‌تر هنوز روی میز است.»
گراک:
**این سکانس از سریال تلویزیونی «The West Wing» (نام فارسی: بال غربی یا اتاق بیضی) است.**
دقیقاً فصل اول، قسمت سوم با عنوان **«A Proportional Response»** (پاسخ متناسب).
### زمینه داستان چیست؟
این صحنه ادامه مستقیم قسمت قبلی (قسمت دوم فصل اول به نام «Post Hoc, Ergo Propter Hoc») است. در قسمت قبل، یک هواپیمای آمریکایی که دوست شخصی رئیس‌جمهور **جوزایا بارتلت** (با بازی مارتین شین) داخل آن بود، توسط نیروهای سوری سرنگون می‌شود و چند آمریکایی (از جمله دوست رئیس‌جمهور) کشته می‌شوند.
رئیس‌جمهور بارتلت که معمولاً آدم آرام، باهوش و اخلاق‌گرایی است، این بار بسیار عصبانی و دنبال انتقام شخصی است. او در اتاق وضعیت کاخ سفید (Situation Room) با دریاسالار **فیتزوالاس** و مشاوران نظامی‌اش جلسه دارد.
### معنی و مفهوم مکالمه چیست؟
نظامی‌ها گزینه‌ای به نام **«پاسخ متناسب» (Proportional Response)** پیشنهاد می‌کنند. یعنی:
- سوریه (یا نیروهای مورد حمایت آن) یک هواپیما را زده → ما هم چند هدف نظامی محدود مثل انبار مهمات، پل راه‌آهن و ساختمان اطلاعاتی‌شان را بزنیم.
- این کار «عادلانه» و «متناسب» با خسارت واردشده به نظر می‌رسد و جلوی escalation (تشدید درگیری) را می‌گیرد.
**رئیس‌جمهور بارتلت** اما این منطق را قبول ندارد و با عصبانیت می‌پرسد:
> «فضیلت پاسخ متناسب چیست؟ چرا خوب است؟
> آنها یک هواپیما را زدند، ما یک فرستنده را می‌زنیم؟ این پاسخ متناسب است؟»
او استدلال می‌کند که:
- دشمن دقیقاً می‌داند ما چه کار می‌کنیم (چون همیشه همین کار را کرده‌ایم).
- بنابراین اهداف را از قبل تخلیه می‌کنند (مثل همان انبارها و پل‌هایی که سه روز است خالی هستند).
- نتیجه؟ پاسخ ما بی‌اثر می‌شود و دشمن جری‌تر می‌شود.
بارتلت می‌خواهد **«پاسخ نامتناسب» (Disproportional Response)** بدهد:
> «اگر یک آمریکایی را بکشید، هر آمریکایی، ما با پاسخ متناسب برنمی‌گردیم.
> ما با فاجعه کامل برمی‌گردیم.»
یعنی ضربه‌ای آن‌قدر سنگین و غافلگیرکننده بزنیم که دشمن برای همیشه بترسد و دیگر جرأت حمله نکند.
### در نهایت چه اتفاقی می‌افتد؟
وقتی نظامی‌ها گزینه شدیدتر را پیشنهاد می‌کنند (بمباران فرودگاه که هزاران کشته غیرنظامی دارد)، بارتلت عقب‌نشینی می‌کند و همان پاسخ متناسب اولیه را انتخاب می‌کند. این نشان‌دهندهٔ تعارض درونی اوست:
- از یک طرف خشم و احساسات شخصی (چون دوستش کشته شده).
- از طرف دیگر مسئولیت ریاست‌جمهوری و ترس از کشتن بی‌گناهان و شروع جنگ بزرگ‌تر.
### چرا این صحنه این‌قدر معروف و مهم است؟
- نوشتهٔ **آرون سورکین** (نویسندهٔ نابغهٔ سریال) است و دیالوگ‌هایش بسیار قوی و فلسفی هستند.
- نشان‌دهندهٔ یکی از تم‌های اصلی سریال است: تعارض بین **ایده‌آلیسم** و **واقع‌گرایی** در قدرت.
- مارتین شین در این صحنه بازی فوق‌العاده‌ای دارد و عصبانیت، ناامیدی و در نهایت پختگی بارتلت را به زیبایی نشان می‌دهد.
- خیلی‌ها این صحنه را نمادی از سیاست خارجی آمریکا می‌دانند: آیا همیشه باید «متناسب» پاسخ داد یا گاهی باید قاطع و بازدارنده عمل کرد؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76132" target="_blank">📅 07:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76131">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdGP6mmtfx-60iH0S7MN-5lUjK-YDth49Qh3lyPl9-v36ObJiqL6mfyq6vPDOFxxmadvHOYUJT_LCPCNRMqoO9qE_ebqE6N5n3lGNCyyftDiHdnYzfWmaQ0ceygrgDxnbt_qdbH_mvZ3vB6EsbLJ7SVJ69jS9tdP6DoQ1Yn25uKFwcmOUnFx1S2GVnT-sSNYzdmDjRy8ed5k1e4xRzdL5tVBRpe38UQG_8t2v5ZLplxz69Zrx8jgRmwJ-SX4qNkOD2CMISPnGkS7XcF4DxTY2IH_bg4mLdUU3GhmwFLJa7PU_22cjWcNMH9ZUbo-bB8cFor6w_9F-v3t2rKI2m5asw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درحالی که سپاه پاسداران ادعا می‌کند ۲۱ پایگاه آمریکا را در منطقه هدف قرار داده است، نیویورک‌تایمز صبح چهارشنبه به نقل از یک مقام آمریکایی نوشت که برآورد‌های اولیه حاکی از آن است که تقریبا همه حمله‌های ایران رهگیری شده و هیچ گزارشی از خسارت به پایگاه‌های آمریکا یا تلفات نیروها مخابره نشده است.
یک مقام آمریکایی دیگر نیز به نیویورک‌تایمز گفته، ادعای سپاه درباره حمله به پایگاه‌های آمریکایی صحت ندارد. هنوز مقامات سنتکام به‌طور رسمی در این زمینه اظهارنظر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/76131" target="_blank">📅 07:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76130">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omgBAO31N2F9eibAz5kIlmyubz3JTc30TCiUGjBIzZcMpizfjXwRdb6KMVUpNU3Fpj5CnkfQT9NhIorlD2ecBL5KhIjMLbjMBw0mR_JaBTqF9MeoFd2T7BzMb8FgpIXWDlvQla6lsZ0krR7u2Wabwy_p8wK5WVJm83Hc0oZqnqrmee54Z2RsV5ajKZ67txVmyv_-ztMQM919ZchRhzr_YluhpREFRSBzd8LSQhwtM0EAmKYHaZkStrH9PPd5BUKqBGr50DPzKR_B4zEJ2vPANVeeeSk1e3HsOSSjQeUZ0AIYXMZY7-IdXNLMi372J0LAx58xMAUrFcJJKOdWhvdmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش ایران و سپاه پاسداران اعلام کردند که «با موجی از حملات پهپادی، پایگاه‌های آمریکایی و سامانه‌های راداری ناوگان پنجم ایالات متحده را در بحرین هدف قرار» دادند. همچنین گزارش‌هایی از حملات سپاه و ارتش به پایگاه‌های آمریکا در اردن و کویت منتشر شده است.
ارتش ایران می‌گوید این حملات را «اقدامی متقابل» در پی «مزاحمت‌های» آمریکا برای ساکنان جنوب ایران خوانده است.
خبرگزاری فارس گزارش کرده که سپاه پاسداران به پایگاه ارتش آمریکا در اردن حمله موشکی کرده است.
سپاه پاسداران گفته که با «موشک‌های سوخت جامد دور برد خود ۴ هدف مهم از جمله آشیانه‌های جنگنده‌های اف‌۳۵ در پایگاه هوایی و مرکز فرمانده کنترل ارتش» آمریکا در الازرق اردن را مورد هدف قرار داده است.»
باراک راوید، گزارشگر اکسیوس به نقل ازمقامات آمریکایی می‌گوید که دست‌کم ۴ موشک بالستیک و چندین پهپاد به سوی پایگاه‌های آمریکا در بحرین،‌ کویت و اردن شلیک شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76130" target="_blank">📅 05:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mmEIkHlkoLNrH6QWysJQ7giB0xcUYENFXv4jbor_ba4SJgYF9IDZW2lN2tKgntAT6fJv0YKpZbd28XNzn0goz4uQ2YHYzthR6H0OdxGHQjJu4vplWR3w86BX8n5nfVYASqbkK0rRcsdaWicOFWAOGLVdC6FbSH2BDaxt3n3HATuyYI5rE6bTpyvWF0VmmDOzn8d5LyvFyd964k-rOYy1pevfuMwzpz8tCWH_FTCRQspz_Enw35v43gjBX4Dgvpdih4XS6E-B66e9ib8wLgnmiQQJrfCFKCQesIrt9gn03ViOx2_txAQKsBNDsm4XI2yqb3rTc4ymGYxGu-s7CovcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه از حمله به ۲۱ هدف در پایگاه‌های آمریکا در منطقه خبر داد و گفت نیروی هوافضای سپاه با موشک‌های سوخت جامد دوربرد، چهار «هدف مهم»، از جمله آشیانه‌های جنگنده‌های اف-۳۵ در پایگاه هوایی و مرکز فرماندهی و کنترل ارتش آمریکا در الازرق اردن را هدف قرار داد و منهدم کرد.
@
VahidOOnLine
توییت اکانت وزارت کشور بحرین، ترجمه ماشین:
آژیر هشدار به صدا درآمده است. از شهروندان و افراد مقیم درخواست می‌شود آرامش خود را حفظ کنند، به نزدیک‌ترین مکان امن بروند و اخبار را از طریق کانال‌های رسمی دنبال کنند.
moi_bahrain
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76129" target="_blank">📅 05:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n3ejOe0R1FUWSV_rWT0iJjFf_hP9Y9rtEAq0AuxDeB0iGuJHMGzeHeqBmnj2M-zDSPO70StDz2o1LzmlOzevZMzMzbCL1XsUwGok86nlCO89jOdK6eGgDRIw0_czXdkPpMJzfDqZbVe1VWUM_kl7PnlYIoKIKtLvS_l8X7ERkroW0Qg0tF6UKW4blcXVczgZFyau9RLXbsP8i82lXdd3h4iSPIGY3OjZqNlpDNII7M_2Xy1bz_mE-wyAB_1yr1arz2rdb-xheXKy6CI6mKJx5tYUvyq5p0k7L2jCoWEnsjUTyN8EpPPF01n-4L9clVx3Eqiwti8jNSZXUmzTrCKVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار فاکس‌ نیوز، جنیفر گریفین می‌گوید که یک مقام ارشد آمریکایی به او گفت که سه‌شنبه شب به وقت واشنگتن ۲۰ هدف در داخل ایران هدف قرار گرفت. این مقام گفت اگرچه حملات آمریکا به گفته سنتکام پایان یافته است، ارتش آمریکا آماده است تا در صورت تصمیم جمهوری اسلامی برای تلافی، واکنش نشان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/76128" target="_blank">📅 04:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkendx6_btI-p2YnlIhJVkQJmB5EoYAIHgzvD4sfSCm2Rmfam6yD_9Y2SG5KysWa46fnuCHc7Q4UyyqVDmpXrESXaoN4bcAc1deHIJhXyFaa-npv9x0RHvZ_l7fp6MOAmsRRW9dQQbXcFqcrjcwHYXr1BLT3xEL1RwjT03Cj5t-PlrZYOxezZ7HFuzVeY1NNnKWamDu_n9d01ER7IwGtjkA7ImR0kCsmwdrXDBhp8LpdqeoOQirJzjTfe7wc7quMhAUrrgYqAlYZUbdwOss0Mbbghqt7Yisc-fl8sMGmGuaibtSBcPzNXS5RiLeOD8mnN78PzKlEnQT7QeH3TNAssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم الانبیا اعلام کرد ارتش و سپاه در پاسخ به حمله‌های جدید آمریکا علیه جمهوری اسلامی، برخی از پایگاه‌های آمریکا در منطقه هدف حمله‌های قرار دادند.
این قرارگاه تاکید کرد در صورت تکرار حملات آمریکا، جمهوری اسلامی «حملات سهمگین و گسترده‌تری» علیه بانک اهداف تعیین شده در منطقه انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76127" target="_blank">📅 04:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2fc27bcc31.mp4?token=brF4lEjsSDW-cQCqZ6pgU61vhmPjIdcspRPmOABGRMyshDQsK00_12lmEEBShwbYTlo_kKz7WnS-c8UN8KJEBSO-urKzw0cbtgHx7kBvlaHcUDE59mIHaQGJwdsXJdEr91KvnIBU7Jas-BZDyDSirlWs7Xbeo0Lz4uut4BMNBQ9ccHD102nfhTf_wgSnF9P-MsJhDTd53H42DqrWhvGzsPJXAFr0OHWte9mgT65lbtX6cR_sTaCJU6JVR_3SNVapyDeoh-iIz-frQDgectHs-oUZw_d8nCrc8UH6kwcbvX7OAht_W3xhqG4vRMBhETsmH5_ae7WyeJgWvKRnZet4dg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2fc27bcc31.mp4?token=brF4lEjsSDW-cQCqZ6pgU61vhmPjIdcspRPmOABGRMyshDQsK00_12lmEEBShwbYTlo_kKz7WnS-c8UN8KJEBSO-urKzw0cbtgHx7kBvlaHcUDE59mIHaQGJwdsXJdEr91KvnIBU7Jas-BZDyDSirlWs7Xbeo0Lz4uut4BMNBQ9ccHD102nfhTf_wgSnF9P-MsJhDTd53H42DqrWhvGzsPJXAFr0OHWte9mgT65lbtX6cR_sTaCJU6JVR_3SNVapyDeoh-iIz-frQDgectHs-oUZw_d8nCrc8UH6kwcbvX7OAht_W3xhqG4vRMBhETsmH5_ae7WyeJgWvKRnZet4dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید  ساعت ۴و۳۶ دقیقه
خمین ۳ تا موشک پرتاب شد
همین الان پنج تا موشک از خمین شلیک شد ساعت ۴:۳۵
سلام وحید جان  همین الان ازنا لرستان زدن
ساعت4:37
ساعت ۴:۳۵ از خمین چهارتا موشک زدن
از خمین حدود ۴ تا موشک فرستادنننن همین الان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76126" target="_blank">📅 04:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iB2H3EtH4wMjuC-SRHszUl8Psdu7WcMzQwr2x64tw3lxGmVt7Rw9tNI_TPyhR31NWtx1BMUv3tHIc2xEV-k0AC7zPTfhf73-b5TfabAJXBXOcki5PLCPqgqrgrISi6sUz894HskqOS5zbfrprjqrpMokwK15nLogeTJJsj6fAFxgCzVRKYPfHHCfRg-SjfHqAzzjAqaa2Gjc4we92DaDojcD1YJ6Mtdx4OrvJkVgC9YbtucxGqggoFch4Wri1YAIgqm1Vr7C-1UtmbJxgGl_zFqNiPtncaqwKTwo92XvM4d0Gc29naG7PwTtgGXlYfmllJ4gBdmpzLL10LMUZdo-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
آمریکا حملات خود را در پاسخ به حمله ایران به آپاچی تکمیل کرد
"
پست سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده، سنتکام، روز ۹ ژوئن به دستور فرمانده کل قوا، حملات دفاعی خود علیه ایران را در پاسخ به سرنگونی هلیکوپتر آپاچی ارتش آمریکا در روز گذشته تکمیل کردند.
نیروهای سنتکام با استفاده از مهمات هدایت‌شونده دقیق شلیک‌شده از جنگنده‌های نیروی هوایی و نیروی دریایی آمریکا، سامانه‌های پدافند هوایی ایران، ایستگاه‌های کنترل زمینی و سایت‌های راداری نظارتی در نزدیکی تنگه هرمز را هدف قرار دادند.
این عملیات پاسخی متناسب به حملات اخیر علیه نیروهای آمریکایی و کشتی‌های تجاری بین‌المللی در حال عبور از آب‌های منطقه بود.
نیروهای آمریکایی همچنان هوشیار و در موضع آمادگی برای دفاع در برابر تجاوزات توجیه‌ناپذیر ایران باقی می‌مانند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76125" target="_blank">📅 04:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه:
"
سپاه پاسداران: یک فروند پهپاد MQ9 دشمن رهگیری و منهدم شد
در جریان درگیری‌های هوایی جاری در تنگۀ‌هرمز یک فروند پهپاد MQ9 که از آسمان شمال خلیج‌فارس قصد نزدیک شدن و مداخله در صحنۀ نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش رزمندگان قهرمان پدافند هوایی نوین سپاه قرار گرفت و منهدم شد."
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76124" target="_blank">📅 04:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76123">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d621f55f6.mp4?token=AUTC0RYXou8BURYeI_aNC-rj75W0PGM49jjoBf7RMh21ag5bz59A0-2HBSJQhnXri1zVZEc1VXAZmYR41VVBgP5J7LlbFC1KOscLdwX3sialHZ3Gqg_BMxRjlQTiYTVW6-G9OGi03ELo9WE3CvB1TYRNYhSWTHy9DWFXaJWGtn-E8T_TueCwgSYKITqLkQa05DmPTYC4_2ZIAwflakhdU_sMBfjIxtbwsuIczYjTGMZSVE66bIOfxzYlR9xXmbmjioQEAkdMxC76k9U6YWoeh9pt9HoC2VUYNhrvXIDm2JJsMn8fpd9jKYr3sTrY1-nns1hpw0baBfZ3rqFcO2NsVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d621f55f6.mp4?token=AUTC0RYXou8BURYeI_aNC-rj75W0PGM49jjoBf7RMh21ag5bz59A0-2HBSJQhnXri1zVZEc1VXAZmYR41VVBgP5J7LlbFC1KOscLdwX3sialHZ3Gqg_BMxRjlQTiYTVW6-G9OGi03ELo9WE3CvB1TYRNYhSWTHy9DWFXaJWGtn-E8T_TueCwgSYKITqLkQa05DmPTYC4_2ZIAwflakhdU_sMBfjIxtbwsuIczYjTGMZSVE66bIOfxzYlR9xXmbmjioQEAkdMxC76k9U6YWoeh9pt9HoC2VUYNhrvXIDm2JJsMn8fpd9jKYr3sTrY1-nns1hpw0baBfZ3rqFcO2NsVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:  دو انفجار در بندر عباس
هنوز درباره محل دقیق انفجارها و جزئیات اصابت‌های احتمالی، اطلاعات دقیقی در دسترس نیست.
دو‌ مخزن آب در سیریک و‌ بندر کوهستک بطور کامل تخریب شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/76123" target="_blank">📅 04:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
یک صدای انفجار هم تو اهواز اومد 03:53
سلام وحید جان، اهواز ساعت 3:53 صدای بمب شنیده شد.
سلام همین الان اهواز رو زدن
همین الان اهواز صدا انفجار زدن پنجره لریزید
یه صدای شدیدی اومد که خونمون لرزید همه همسایه ها ریختن بیرون
سری قبل کولر روشن بود اصلا صدا نمیرسید این خیلی شدید بود
آپدیت:
خبرگزاری مهر: صدای انفجار در اهواز شنیده شد
منابع محلی از شنیده شدن صدائی شبیه به انفجار در اهواز خبر می‌دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/76122" target="_blank">📅 03:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76121">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
از جم شلیک کردن ساعت ۳:۳۳
نصفش تو هوا منفجر شد،بقیه‌اش هم نمیدونم کجا قراره فرود بیاد.
بعد از انتشار پست: وحید جان نزدن،تو آسمون منفجر شد،صدای اون بود.
سلام وحید جان شهرستان جم رو همین الان  ۳ و نیم صبح زدن، یه صدایی اومد ولی چون پنجره‌ بسته است لرزشش خیلی بیشتر بود
ساعت ۳:۳۴  شهر جم رو زدن
اول فکردیم موشک بلند شد
ولی بعدش خورد زمین ترکید
سلام فک کنم جم رو زدن یه صدای انفجاری اومد الان 3:35
توی جم این پدافند بود فعال شد اون صدای انفجار هم پهپاد زدن باهاش
قشم: دوباره یه لرزش دیگه ۳:۳۹
احتمالا بندرعباسه ما داریم حس می‌کنیم
وحید هنوز صدای انفجار قشم داره حس میشه
همین
الان پشت سر هم
سلام وقت بخیر ۳:۳۸ بندر عباس پایگاه هوایی رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/76121" target="_blank">📅 03:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76120">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBaZ7yMivsi5G0m2DMGB1rCXV5JBpUozmgAqUpt_MmHKLdzX2MCxAti8cPEzdWJW_7UCLmlBX8jup2A--4p6aZH7vDrCaAb9_80Z9-pYbT8oKB95HxiN5Z24-gD_n4qRHUF54Ali4mPDnH2CTSu1dzJ0RcjnSYheSmxmgiw7J4dpbNIwso7EXQ4Q0byr4Cwfa14EZOKalKgLlbGQWyJcmiyIg_vnBWES23erqzjJSY6c9ygWPApD_E7ka0GupdWDRriVxQ2-Slz0yP8f88WeLHUhjV7RmCBlhMBl4sDUtJiZ4xQHRqwXTD-HssVdy_gqCv0DEXJeazrkvzbwdqyZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک جانسون، رییس مجلس نمایندگان آمریکا، گفت پیشاپیش از دور جدید حملات آمریکا به جمهوری اسلامی با خبر شده بود. او این حمله‌ها را «متناسب و محدود» توصیف کرد و گفت این عملیات سامانه‌های راداری، موشکی و مراکز فرماندهی و کنترل را هدف گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76120" target="_blank">📅 03:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76119">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیام‌‌های دریافتی تایید نشده:
سلام وحید جان، ۰۳:۱۸ و ۰۳:۱۹ دوتا صدای انفجار اومد بندرعباس
الانم دوتا وحشتناک تر
🤯
همین الان بندرعباس صدا اومد ۳:۲۱
سلام وحید همین الان دوتا انفجار شدید بندرعباس
وحید بندرعباس انفجار شدید
همين الان بندرعباس صدا اومد ٣:٢٢ دقيقه
درود بندر ۳.۲۳ انفجار پیاپی + ۳.۲۲
و مجدد ۳.۲۴ بندرعباس
دوتا صدای وحشتناک ۳:۲۳
همین الان بندرعباس
سلام وحید سیریک سمت روستایی طاهرویی صدای انفجار شدیدی اومدم فکر کنم نیرو دریایی سپاه رو زدن
سلا وحید جان، همین الان بندرعباس صدای دوتا انفجار پشت سر هم اومد، ترسناک بود
صدای انفجار بندرعباس همین الان دوبار صدا اومد
صدای نسبتا شدید و خطرناک
وحید ساعت ۳:۲۴ بندرعباس صدای دو تا انفجار
بندرعباس ۴ انفجار
قشم ساعت ۳:۲۳ بامداد ۲۰ خرداد
در محدوده طولا یه لرزش نسبتا شدید احساس شد ولی صدای انفجار خاصی نیومد، شاید زلزله شاید هم انفجارات حمله‌های اخیر بوده که لرزشش رو حس کردیم، خونه کامل لرزید
سلام وحید جان همین حالا قشم ۲ تا صدای انفجار اومد ، دومی نزدیکتر یا شدید تر بود
بندر دوتا انفجار خیلی شدید پشت سرهم اومد سمت پارک جنگلی
ساعت ۳:۲۳ بامداد بندرعباس یه چیزی منفجر شد
سلام سمت پایگاه هوایی بندرعباس رو میزنن
#قشم
، 03:23، 20 خرداد صدای بلند انفجار شنیده شد. (شاید صدای انفجار بندرعباس بوده)
سلام بندعباس صدای انفجار الان چهارشنبه ۳:۲۴
نزديك  پایگاه هوایی بندرعباس خونه ماست به فاصله پنج دقیقه چهار انفجار بزرگ صدا اومد
اقا وحید بندر خیلی صدا  انفجار میاد
سلام وحید جان بندرعباس 3:24 دوبار زدن صدای خیلی زیادی اومد همراه با لرزش
وحید جان درود
ساعت 3:24 دقیقه بامداد چهارشنبه 4 انفجار شدید سمت فرودگاه و پایگاه هوایی بندرعباس
۳:۲۳ دقیقه ۴ ۵ تا پشت هم زدن بندر رو
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76119" target="_blank">📅 03:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76118">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdW0pJqgekdoZdU37_HSAGQ4Zzmui479mJmafYXZ5oBNoHbJUpcB3FvfiukikiKsuCh6zEEbT2r1s0Cj1gN-moJ3JVE2V8eN5eIve10rNDfSlzG9BcySwSM4axgQ0Fcxl4jETeERbjQpsxBGcXKv78vbOuvURu8SSqGtntLrhw9DRLlQGNYDbW1STul7sXmT1mdoRv4LgTGeA9iMG6HGvHrrqxRRRe00Ee8Df5PFProL-3nPgHyuViPrACmgkVdGZqdHABqIscR4eMVGzCvCZZ3jql-Hidt0p31nZtAeVmL8ttzv4F0Y3fDaSl-R3hIf0MH2r622FVxiVBdNuDIQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر به نقل از منابع محلی و ساکنان روستاهای اطراف، از شنیده شدن مجدد صدای چندین انفجار در محدوده شهرستان جاسک خبر داد. پیش‌تر حملات نظامی به بندر جاسک و کوه مبارک توسط منابع آگاه تایید شده بود و این حادثه، دومین موج از صداهای انفجار در این منطقه از آغازین ساعات بامداد چهارشنبه به شمار می‌رود.
@
VahidOOnLine
من هم حدود ساعت ۲:۳۰ چند پیام از جاسک دریافت کرده بودم.
خبرنگار آکسیوس هم به نقل از مقام آمریکایی گفته یک موج حمله دیگه انجام شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/76118" target="_blank">📅 03:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76117">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">موج حملات آمریکا «فروکش کرده است»
رسانه‌های ایران از «فروکش کردن» موج حملات آمریکا خبر دادند که می‌تواند نشانه‌ای از «مقطعی و محدود» بودن این حملات، تلقی شود. چنانچه سنتکام آنها را «متناسب» خوانده بود.
خبرگزاری تسنیم  همچنین تصاویری ویدیویی منتشر کرده و مدعی شده که یک پهپاد شاهد ایران در آسمان عراق مشاهده شده و آژیرهای خطر در کویت و بحرین که میزبان پایگاه‌های نظامی آمریکا هستند به صدا در آمده است
اما هنوز جزییات رسمی در این باره از سوی رسانه‌های بین‌المللی مخابره نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76117" target="_blank">📅 02:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76116">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرنگار صدا و سیما در سیریک: در پی حمله امشب آمریکا به سیریک، ۲ مخزن آب بخش بمانی مورد اصابت قرار گرفته و آب آشامیدنی این بخش قطع شده است.
"خبرگزاری صداوسیما" در خبر دیگری نوشته: هیچ بندر تجاری در جزیره قشم هدف قرار نگرفته است. در پی شنیده شدن ۶ انفجار در قشم برخی کانال های خبری از حمله به یک بندر تجاری در قشم خبر داده بودند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76116" target="_blank">📅 02:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76115">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TfjUyXrucMq82jDT45RdU97z0PdppMeWwxJo6PJ2D6l2ayKmgmSUxF4Kbe0aP3ekVs4_2U_GqGs0UrlzYeNkXL-B4K6ANTQdvlEYLxHgk6AzD7hhOdJSSOEb43kqXR_wvi9FBid_9o_b8tU9iK0yhdL_c8771TsH7HVYioLobBySt7hyGt_kQDf7CyKJHaLxPhYQNg7zcC6vfEC4ZgJhvptTwRVmMKFmo2kW4NRGQpOHTk1IwEl-VS0YV3UeSnUIFHHgzG4cqYn18LGGhEAD4Z3BxBU_cjSUlGYIvbY-CtAmJFoU1Mh0-ONRTipTT-Wdawv1wsZY3igLIAj8FrJGCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت تازه عباس عراقچی، ترجمه ماشین:
با وجود شکست‌هایش در میدان نبرد، ایالات متحده تصمیم گرفت عزم ما را بیازماید.
نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نخواهند گذاشت.
اگر می‌خواهید در امان باشید، منطقه ما را ترک کنید.
تاریخ خلیج فارس فصل‌های بسیاری درباره سرنوشت‌های شومِ بیگانگانِ مداخله‌گر دارد.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76115" target="_blank">📅 02:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76114">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HxHx168HB76_EZ0CWyi8uwNrII1qpTk0PxhrkLecJ57VZdwyILVjJ3LO2elxiiAdbyE8FNqgVLZwTWuptMZh4Ios2e64a2ZN4kOFcspHNFi6sG-pkDcFTeVEEMvVu7xVkmn_R-UItPk1Wbyg5sHqKV3qAxgs54BbSh_UZyBC8f5yhWZRpp5_Q61gO8CnkQle6IXv8jUfT3WjdJ_3EnPcc1CwjBugkrHsSHDlBnK3VffUaHLkSUFiJr51c1c-7v8cISoZ5csMcPPOxFoHAy-JTLNLRiU5Ercz4tn7mtKQtN3_u2lvHkTKqAvCnKPfg8-8Lxb1w0rH7cQfqKWEq5ocZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان گفت که حملات جدید سنتکام با قصد هشدار دادن به جمهوری اسلامی است.
او گفت ایالات متحده معتقد است که این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76114" target="_blank">📅 01:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76113">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41278e3d2c.mp4?token=SAOYRSYs9SAqk1SezOeaYLJTL7IEN0hsq23SuWmX7VPXP8aU-mcub363zQGTOYHiatHvT9SuxHGtHUIpEV-6NsIrHtrsSD0ThU6OwdkcyN3extykcrxF4eBL-D38tzMgjoit6pmNkMnWHkuS0uj1FnCQQeVaQ-66jFNuFi__o5K0LZCIpP_0YV5NwfTSBI0biuqpRdSDpGsDxQ1Yd-MFL1cNxhjIi0ymYUPlStoCNXlh1_QM-00kJu8gxvCn5TNbiW_Cd1UPvkavL_tO4ltBiGua4sFDh6mC1yjgcev61aSUmnX_Oam18FQPCzg9ZAiC6Pb5A5CUKdQvlvTv8Y--UA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41278e3d2c.mp4?token=SAOYRSYs9SAqk1SezOeaYLJTL7IEN0hsq23SuWmX7VPXP8aU-mcub363zQGTOYHiatHvT9SuxHGtHUIpEV-6NsIrHtrsSD0ThU6OwdkcyN3extykcrxF4eBL-D38tzMgjoit6pmNkMnWHkuS0uj1FnCQQeVaQ-66jFNuFi__o5K0LZCIpP_0YV5NwfTSBI0biuqpRdSDpGsDxQ1Yd-MFL1cNxhjIi0ymYUPlStoCNXlh1_QM-00kJu8gxvCn5TNbiW_Cd1UPvkavL_tO4ltBiGua4sFDh6mC1yjgcev61aSUmnX_Oam18FQPCzg9ZAiC6Pb5A5CUKdQvlvTv8Y--UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام آمریکایی گزارش داد که حملات آمریکا به جمهوری اسلامی ادامه دارد و اهداف شامل سامانه‌های پدافند هوایی و رادار است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76113" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76112">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPORqQOxprVkgjoKxbTf0clKo3PkWsLNEpoEpmT52O8NHD58v560G5Kb2W-AdVy7sTFEICftIRGrU5RSLsN5t5Z-XvEcMHOaKCxxDaLY-galGrIFPbTSwtj-3ol-A2cMqZWxdFd7x5OOsE0pvXLFxHz19V7OBFOEctfQ_9j52I4Rvag5bE8-9VS6hha-jx-f34JJUycKdstRWEKQ0oHfkONzxSI0vThPsHFz1-HG1_wBTKJibZ7fHUvNpKrfPVOGRCWlAvFk6jGgCi_HOVxQC--gYh43SAuI03yz90aW_yB2jAHrevLFgbPPNwtCbjTUodVZ-AcapR735qIQ7rOfmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، سه‌شنبه‌شب، در گفتگو با شبکه خبری «ای‌بی‌سی» (ABC) درباره آغاز عملیات نظامی واشنگتن علیه ایران گفت: «من فکر می‌کنم پاسخ دادن امر بسیار مهمی است. آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین حالا که صحبت می‌کنیم، در حال پاسخ دادن به آن‌ها هستیم.»
ترامپ با تاکید بر موضع قاطع خود افزود: «این اقدام پاسخی به کاری است که آن‌ها شب گذشته با هلیکوپتر ما انجام دادند و من معتقدم این واکنش باید بسیار قوی و قدرتمند باشد و حملات جاری نیز دقیقا همین‌گونه است.»
@
VahidOOnLine
"خبرگزاری صدا و سیما":
سیریک اصابت یک پرتابه تایید شده اما مکان و نحوه اصابت مشخص نشده است
برخی منابع از شنیده شدن صدای انفجار و فعالیت پدافند در بندرعباس، قشم و سیریک خبر می دهند.
"به گفته یک منبع آگاه ۶ صدای انفجار در قشم شنیده شده که بر اثر پرتابه های دشمن بوده است.
ظاهراً این پرتابه ها از جنگنده شیلک شده است."
من از جاسک هم چندین پیام داشتم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76112" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76111">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HA_cdnODD1waQ7iQ5v2dmGGyUOfoclbFYm4WIGADHUj1q9h8iRdovrDbNJ6dZSkk-DWD3-whllueewlK9AUD0OYDlAB1yg9Ilj2fuMy3yMr1ip7tFkFyCJH7XSi1LnBb-fgXEflEQt08KS2PLIJfbzw5JcGjcLqTfVohxlkxCBYs0BS7ldLT_HblTi9_PPGtLBkvCr-i5WxCpKCW9orfWappfb4qeaCPsypdOWLEGSd705djbwj9apF-V0PTuOgwIb46sNT2ctTDqZL0ZXduLLeX-HZWqpjIylGQIUabCBfMP7wzw9WvKvYGx71D-gWtJFfSg-G-uzKidY347f18vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
سنتکام: حملات در پاسخ به سرنگونی بالگرد آغاز شد
ترجمه ماشین:
فرماندهی مرکزی ایالات متحده آمریکا، سنتکام، اعلام کرد نیروهایش امروز ساعت ۵ عصر به وقت شرق آمریکا، به دستور فرمانده کل قوا، حملات دفاع از خود علیه ایران را آغاز کردند. این اقدام در پاسخ به سرنگونی هلیکوپتر آپاچی ارتش آمریکا در روز گذشته انجام شده است. این مأموریت پاسخی متناسب به تجاوز بی‌دلیل ایران است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76111" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76110">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پیام‌های دریافتی از ساعت ۰۰:۳۰
صدای چندتا انفجار بزرگ پشت سرهم شهرستان سیریک
وحید جون سیریک صدای  انفجار اومد
وحید بندرعباس صدای انفجار میاد
چهارتا انفجار سیریک هرمزگان سه تای آخری کناره های ساحل
وحید بندرعباس صدای انفجار اومد الان
صدای سه تا انفجار شدید از سیریک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76110" target="_blank">📅 00:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76109">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ep5lf03Uy2W_3b2oKCxwe-pndW-xhTCxVDHQVRYz8J3EHy_Rz2Mw3xzGI96ld7ZubTSjjNmUnFDktrxmB_45_p6i_LJf0tST9o1MiIfEgve8rqiR0ofwUWrSVbZbf6qbDRFQ_JtSQrfbwBxHc1RvJ3_GcxwKk0zDp11HHq5IX52-X4ci5a75MThPPxQi2PnbmwiTuw5O7EQLSg4KFgarbboE3uMfqRY5kzk19TqkyiS-j1VUnafjw_uqRT9Fe7iZ0IrL_Iak95rab_CkhD3PDkp7kp74tE3diJbYwfx4mbisqJ3Us7vzbe_jgl9lrcIoElGZLX1fe-8AW1SQUksPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نظامی نوشت: «در ۲۴ ساعت گذشته هیچ عملیات نظامی هجومی هوایی در تنگه هرمز انجام نشده است».
@
VahidOOnLine
پیش‌تر خبری بدون ذکر نام پخش شده بود که:
معاون وزیر خارجه جمهوری اسلامی ایران، روز سه‌شنبه، ۱۹ خردادماه، در گفتگو با «الجزیره» اعلام کرد که هلیکوپتر آپاچی ارتش ایالات متحده که روز گذشته در تنگه هرمز سقوط کرد، به طور عمدی توسط ایران هدف قرار نگرفته است.
این مقام رسمی با تاکید بر اینکه ایران پشت این حمله نبوده، در عین حال هشدار داد که به دلیل شرایط به شدت ملتهب و متشنج منطقه، ممکن است بروز چنین حوادثی در این فضا «عمدی» تلقی و تعبیر شود.
همزمان، دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگوی تلفنی روز سه‌شنبه با روزنامه «وال‌استریت ژورنال» با کوچک جلوه دادن حادثه سقوط هلیکوپتر آپاچی گفت این اتفاق «مسئله چندان مهمی نبود» و تأکید کرد که «حال خلبان خوب است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76109" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gJevVMV9h87aSuJ5su3CUyQZ8QyUO1-CXZsOKRrAPJKe8zVxHhSN0-YQqlMGOZe_MY73jGKubwDlubdTiIXyPHSpriwQzdI1waNJQYoZ6siixrpN3GoNmsENZpLhyEYApDIldnh6jwFuzOXMJeRdBXS_iRLr_UJt_9CtU2vAZtZL1Rr53t720UO8V9kgakQ7WeyMDixUPn_E8SIlFJwNpvpXEA5FUB7RJd2IaBgY70oTVp6tr0hKFidI_GBL-s_2ZQLSirwA8bw6Q4XG1vfP8qKKYZDmiPrKr-SwEvyU2vwyyMRfPycGuGzPtAzJZ_4zptf_95YAXYFWFp6IMDMbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PXqqxlSGzzUXlNLr4eyJEE4AuOSUjwPXZhhRJUOvWAwn8c4dUoC26d8ONWxWdHFs27T7KM7V52ePJKSiIlvzjvasdswk0pPaprzma8hVNUqEqzdC0tSqpi3541jlGpHVDbDvoC_luqiORpbUFgQF6mLTyWhSrXa9zcdFiQ6_ksmJr3On2WBYREFEzZ32kGY_LgGNI-k_u8e9LQayxG4xonIeLyJX17ugnKLzgETQcCwtx-FrkK0JjhZ-VcLTuXscBq53kDWULP_MqAbuKQY-7hU4Hq_o4c18DQ-bsAmhhu7IK6u-8ZGTVDOkHMGfDqkH4sUkcTc20dr5imZaFlrJww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگوی تلفنی روز سه‌شنبه با روزنامه «وال‌استریت ژورنال» با اشاره به اثرات شدید تحریم‌ها اعلام کرد که محاصره دریایی بنادر ایران باعث شده این کشور «بسیار فقیر» شود و واشنگتن این محاصره را تا هر زمان که لازم باشد حفظ خواهد کرد.
ترامپ همچنین با کوچک جلوه دادن حادثه سقوط اخیر هلیکوپتر آپاچی آمریکا گفت این اتفاق «مسئله چندان مهمی نبود» و تأکید کرد که «حال خلبان خوب است».
بر اساس گزارش سنتکام، سرنشینان این آپاچی پیش از نجات، دو ساعت را در تاریکی شب روی آب سپری کردند و یک مقام ارشد آمریکایی فرار آن‌ها از این سانحه را معجزه‌ای همچون «دست خدا» توصیف کرده است.
@
VahidOOnLine
وال‌استریت ژورنال نوشت که حادثه سرنگونی بالگرد آپاچی در تنگه هرمز برای ترامپ «کم اهمیت» بوده است.
این در حالی است که پیش‌تر ترامپ در تروث سوشال تاکید کرد که «ایالات متحده ناگزیر باید به این حمله پاسخ دهد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76107" target="_blank">📅 00:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LXOkTSZDfCM5P65vBD-yRJGv4-eMONhxIuc42BdPm0w3r6-ouA2s91SQPr5PJT23Mc5-TzgAYnol8SgjVk6hqtuQrReW0FvLUcAx8tB3IU4DyZi5ykAUC-k725-7c4C6y-LBfdyqYkRmxT2PZj3xWzUPHQy3WZJb_LXE3OqE3aPzrt2cHVxfH2ZboFxmPP7JQrrOH_J9zUw7NjIFSThdqCMxxq6AZaXWZjdsUNFYlaOGXwVAtMDZ1tqXoTYuSjpXn92tfk94_W8IoMY7LkhVI8glYQiseYWEKxoi6kf7QR6PxJeEdPu3TIEaixVkteN93faA6NqeHZb2WVRn7c6iYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عراقچی، ترجمه ماشین:
نیروهای خارجی در نزدیکی قلمرو ما همواره در معرض خطرند؛ چه به‌دلیل خطاهای انسانی خودشان، چه حوادث ساده، و چه احتمال گرفتار شدن در آتش متقابل.
برای کاهش خطر، بهترین راه‌حل این است که آنجا را ترک کنند.
ما زبان دیپلماسی را ترجیح می‌دهیم، اما زبان‌های دیگری را هم بلدیم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76106" target="_blank">📅 22:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/spOQ1ik9CPP3wK9T3k_oQd3HrS26U0Q8hSnf26HI990kwb1ryJYQjYZl4FfSC0XbY3q9vDb0t2HNJmiWjaCZuynWdFE2W9JhJGnZvoVZjEHUn2Oc9b7On2N9YGEcesxo45QnwoThrIPCRlqcs-o49UtAxy-d4hDlzPwNdHlWXW_GAwTv9ynTM4lVgFYJrEMPoUfxP19sXCOs0pzy_wfQmPRF-sr__3JWXlOh6jtNT_weFl-EaWBrYgWpdXqgtBgLiSkY2lvhE9GCgbHHPzOEBjHjMWlLN9OKBl0YLag2DjFZVa7naGJO0IVx_jrPSLLiYzAoTSqnK9OsNnNYoy_gag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری سی‌ان‌ان به نقل از دو مقام آمریکایی گزارش داد که هلی‌کوپتر نیروی زمینی ارتش این کشور که در سواحل عمان سقوط کرد، توسط یک پهپاد ایرانی سرنگون شده است.
یک منبع آگاه دیگر  تایید کرد که یک پهپاد از نوع «شاهد» به این هلی‌کوپتر آمریکایی برخورد کرده است.
یک مقام آمریکایی به اکسیوس گفت تحقیقات هنوز مشخص نکرده که آیا این برخورد عمدی بوده است یا نه.
😱
‍
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76105" target="_blank">📅 21:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F8ARwItN2DuxoPGrYluy2y1Ehk8R_J5Ss9vuGjkFnHwvEWTYXIskoubVe0oSWGNHCHQA2QVOEv6MkxEoqNipY2xhZM5-diH6CRTeAYQo_e__B_7C6ub07BV5xA9f-2NR5qBK_6DvlzdfWLyRFCl5JPmzZrlPk-zSNEmDttzbjvh2hP9lsBvwYy5nPcWvYxjwCZPENFMWtu48MPADVrz1tkyxkDfM3SiTnGzn32CzwayH7pzaJsKPA5Ac9YYFu2L_vyZr9LAqgUWMTLbHlAXqsH79ezJV1tfWkJP4SsOPWlZCvxYBkcPazvaQh5CrRtGg7MZCyo5lyJ1fY_D7LXPj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
ما زبان دیپلماسی را ترجیح می‌دهیم، اما به زبان‌های دیگری بسیار روان‌تر سخن می‌گوییم. تعهداتتان را زیر پا بگذارید، آن‌وقت ما به زبانی روی می‌آوریم که در آن بهترینیم.
خودتان بر اسبی سوار می‌شوید که زین کرده‌اید!
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76103" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76102">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KsUj1L8t9W7rsoUv--y2F8KEqZodjmtbkSwGzO5I8mn_kKKxTF_eMDhDPp_Y9Zbpf_9vjLE19FOjKKeaj-1aPI0J1mVEWE7T9FWxgBYuzKlQ7p4Vp8q8QvyIEu8Zvy1KhzBXQ2zV83ccs07eoVbSm_R2MLiQtbRrxucXy_3FE0Sk58-X4tMUPTCIveLlHyIjYce3uhhDu1xiRrqppwU86120ibmVk-uhOm1GbeIG-VxVy7uArxGdizA8SPJgimIGnNR0Q-xewY4dVnFLZIxOSXipgZaafK6Wv--OBNCanRMggb6xqcPIzFtZBT4N2zlwszZ0WaKVEGmZovZ0ck5nFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: ایرانی‌ها بالگرد پیشرفته ما را سرنگون کردند، ناچاریم پاسخ بدهیم
ترجمه ماشین:
به‌تازگی از سوی ارتش بزرگمان به من اطلاع داده شد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی بسیار پیشرفته ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کرده‌اند. دو خلبان در این حادثه حضور داشتند که هر دو سالم و بدون آسیب هستند. با این حال، ایالات متحده ناگزیر است به این حمله پاسخ دهد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76102" target="_blank">📅 20:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76100">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TXsmDhodT6bQ7pJz4mOnhnZW6JeBvZFGxgp3MsYtLEMoHv9muQSYZViMi7Hx2yKCq2lhoBUheljvpTVCVxsZGDeRF7cFB7Tc_aYJnHjPoXvsrlsjGP2yPf_g8mzOrYR7c95VWipTn_Q05c8C57wzHJwVzCD-wra88etgJ3vOnHraZMOjU0TA-k_fcJcQPlSoLtztejo-I7ZxiDS2Ny5yWB4_dnz-BVp3wQ3aELQGm0hRLQUzq5oXEoN9Nvtb92sAyRtyUeST7xDDCtcN9FFslMIuSkIw-P5v8VJztMvxgrP58Z82D_3BbdQCoB6MofeSM6fsjLjtQRSpEwr-n7DCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f396691769.mp4?token=gwZUtaSpQ-6tzxKTkHX3wr4jBO-PAgdf-yohMiFcUj7bOglXQywrMZ8xppbApAH8qKm83Pv6ubcdENKUut8_qBQv_yQNKga7lzX2wUsyPBWXh9Rd3EBj4jUOo_cLmFZBli-Ja8FYozX5TcaVEpXUYRJFVtFGgthHFGIWYTPc0bOaJx52Xfbf-mwQEcYrT1d-V935XFnEeY5Xy38Jq-6WT-YUprwyZ2ixNvPEDYVnudN9BZKSigYvCq8RXyae1fkpdJ2ppt36UJVUf6v1btQBRETk24gQlWTeDKiaHMEfmw5ivl-y7tvNhN6IpZb_iZCFRbRFrQhOTQ_YMTPDJ7sB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f396691769.mp4?token=gwZUtaSpQ-6tzxKTkHX3wr4jBO-PAgdf-yohMiFcUj7bOglXQywrMZ8xppbApAH8qKm83Pv6ubcdENKUut8_qBQv_yQNKga7lzX2wUsyPBWXh9Rd3EBj4jUOo_cLmFZBli-Ja8FYozX5TcaVEpXUYRJFVtFGgthHFGIWYTPc0bOaJx52Xfbf-mwQEcYrT1d-V935XFnEeY5Xy38Jq-6WT-YUprwyZ2ixNvPEDYVnudN9BZKSigYvCq8RXyae1fkpdJ2ppt36UJVUf6v1btQBRETk24gQlWTeDKiaHMEfmw5ivl-y7tvNhN6IpZb_iZCFRbRFrQhOTQ_YMTPDJ7sB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طالبان به تجمع مدافعان حقوق زنان و مخالفان حجاب در غرب افغانستان حمله کرد
AngelaGhayour_
مقام‌های امنیتی افغانستان روز سه‌شنبه ۱۹ خرداد تظاهراتی که در حمایت از حقوق زنان را در ولایت غربی هرات برگزار شده را متفرق کرد.
این اعتراض پس از آن آغاز شد که پلیس امر به معروف طالبان گروهی از زنان را به اتهام نقض قوانین اجباری پوشش بازداشت کرده بود.
به گزارش خبرگزاری رویترز، شاهدان گفتند که در جریان حمله طالبان یک نفر کشته شده، چندین نفر دیگر زخمی شده‌اند و ده‌ها نفر از جمله زنان و دختران بازداشت شده‌اند.
..
به گزارش رویترز، هرات که مدت‌ها به‌عنوان یکی از پویاترین شهرهای اجتماعی و فرهنگی افغانستان شناخته می‌شد، دستخوش تغییرات قابل توجهی شده است.
...
شاهدان گفتند اعتراض‌ها زمانی آغاز شد که مأموران امر به معروف تلاش کردند زنانی را که با الزامات پوشش اجباری مخالفت می‌کردند بازداشت کنند.
برخی از ساکنان گفتند مأموران حتی زنانی را هدف قرار دادند که از پیش نیز پوشش مورد نظر، شامل پوشاندن کامل صورت و بدن، را رعایت کرده بودند.
@
VahidAfLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76100" target="_blank">📅 19:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76099">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M0hTVGzhAom7OQxwSBTnc6-D0bZJ1UD9RuQboj38Ew9EDA961NsTKyUlYCCwkKtUFz-Nmlf0pOgnIJBEuq56V3puBONbJyljjwf9ZxzUBKSXDkkgXrnocF1F7q1QdiwQo1igLo7b2n2T5G0a997q63kyW2Xo-Hm_sBs7JxCsn7w0gd0GI2QEsrUEFjf_jCH2fUt_KwbMkS8Iwmf6bwd4Sok3HPIgBWTJjlj7g_BYpCqUlBqysUigFyIuFP3uOVjFcXfqEYdPTLBeVdFVp96ou66YPeTjhrvVkQMJWvKvXayoRR1D5Mtg5m9wUyhSabi9itG-HXa5ttGTn5JkPz7vWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا پیغمبری، جوان ۲۶ ساله و از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴، توسط دادگاه انقلاب تهران، بابت اتهام «محاربه» به اعدام محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76099" target="_blank">📅 18:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76098">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/677a13e326.mp4?token=CCI-o-Lw0fXTRK5TpDMqZ50OviALaYLDkHa56tHGsyvhEG9fhL-9vJFBdevJ7B8zl7Qvb8jUcts-zuAGYCR4M-mONbMICGcKMDDxKKM8ZAEaCd8npZnCOwhxN7kDSKMcG8m2kabiS870lcnzyDb55DLVLySoei6b3ZblzykT1Y1wxwpiwFmKDWmDi8SQLlGdRW6V3vyuA7BjMvKBhDdaXgD69IBmNBdoz6aSrwx1iX71hjqxhhb6tf7ARXv4HrzYjuIcu9yhh9dKhe0ljt9kjtBLUs79cBvd4R_co9mBIxOpzjkH7FWe5dl-nU8gA_5Zn7g_yKFGcxYGY5Ql2Q0wuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/677a13e326.mp4?token=CCI-o-Lw0fXTRK5TpDMqZ50OviALaYLDkHa56tHGsyvhEG9fhL-9vJFBdevJ7B8zl7Qvb8jUcts-zuAGYCR4M-mONbMICGcKMDDxKKM8ZAEaCd8npZnCOwhxN7kDSKMcG8m2kabiS870lcnzyDb55DLVLySoei6b3ZblzykT1Y1wxwpiwFmKDWmDi8SQLlGdRW6V3vyuA7BjMvKBhDdaXgD69IBmNBdoz6aSrwx1iX71hjqxhhb6tf7ARXv4HrzYjuIcu9yhh9dKhe0ljt9kjtBLUs79cBvd4R_co9mBIxOpzjkH7FWe5dl-nU8gA_5Zn7g_yKFGcxYGY5Ql2Q0wuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه شب هنگام بازگشت از نیویورک به واشنگتن، در گفتگو با خبرنگاران اعلام کرد که ایالات متحده به دستیابی به یک توافق بسیار خوب، محکم و قدرتمند با جمهوری اسلامی بسیار نزدیک شده است.
ترامپ با رد وجود هرگونه نقطه اختلاف بزرگ در مذاکرات، گفت: «اگر بخواهید حقیقت را بدانید، شانس خوبی داریم و باید بتوانیم ظرف یک ساعت توافق را نهایی کنیم.»
رئیس‌جمهوری آمریکا با ترجیح راهکار دیپلماتیک بر گزینه نظامی هشدار داد که بمباران ایران در مقطع کنونی، به قیمت جان انسان‌های بی‌شمار و بسته‌شدن چندماهه تنگه هرمز تمام خواهد شد و فرصت توافق را کاملا از بین می‌برد.
او با تاکید بر موفقیت راهبرد واشنگتن افزود: «سند امضاشده نهایی، کارسازتر از بمباران خواهد بود. ثابت شده که محاصره دریایی اهرم بسیار قدرتمندی است و بسیار قوی‌تر از بمباران عمل کرده است.» ترامپ در پایان اشاره کرد که ترکیب تهاجم اولیه و محاصره، ضربه سختی به اقتصاد ایران وارد کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76098" target="_blank">📅 17:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76097">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta6C1AhFROjynFropgZs9oidjj_ho5xYptgdJw5AEveRb9tCIpPe0EU2DkymfTAwwn_69gTAvuT0TzuKw9FOLuAg5ea9bAT1tU6E2HPz7BbIiZ1vh6Hc0mRTVm_dfV0k4qXwpx99r7a4ePl3huCoijs83CU2AnllGoYXUt13oyfheoGMLG0Vacrw5dgY5BYDKUo0fVpIy6AZpva3xRUBZBVLv7kLHPMf0tS5_WhU1gzElDxw8E_R21u9qvp8ovrrhgwnRd_m93ute_SlGjYprX_IrKrOC5yqsBXZnurMgghQH1b8TrOTZIJCHeEUQS624oXtco7TNVOHMsyQ7UEp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو عضو نیروی پدافند هوایی ارتش ایران در حمله دیروز اسرائیل کشته شدند
تاکنون در حملات دوشنبه و سه‌شنبه اسرائیل کشته‌ای گزارش نشده بود و ۱۵ زخمی اعلام شده بود.
ارتش اسرائیل دیروز گفت حمله «همه‌جانبه‌ای» به سامانه‌های پدافندی راهبردی ایران کرده است.
بنابر بیانیه‌ ارتش اسرائیل، در جنگ ۱۲ روزه پدافند ایران ضعیف شد اما بعد «سامانه‌های پدافندی در نقاط مختلف ایران» مستقر شدند تا توانشان را بازسازی کنند که در این حملات این سامانه‌ها منهدم شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76097" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76096">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHYNSaIK4Qi7SL7U8RPx134nvMMZMI9TYQ-rFfid9o7FAWCRhy464lZGl-dVZfSsu4z3JWPXLbZqFyMnGLuc0CrtKLckgpI-nUtDjJSLjRyMBJnJfCD1XHVvrWsJk1KMSuxiwmonGRVWyDLlwtDKZMBKYKcbB0aKp-y_vhroVIr1E0ZLh_lC9j2PlNf7lJ9d6vM-IgAGr6QuFRkISYDBg0p_rAMrTlQDyoxJ7JVo6S2-Lx0LPTZflCavhL4OFJR2yHYKYFZybGD5D1EQLopSeguWST-qlefNypAjfXsMrV-eKN2Q8v8KHL7wkDZrudo1eExB6wJDxvNz3MrffPhm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، در بیانیه‌ای اعلام کرد دو خدمه یک فروند بالگرد تهاجمی «ای‌اچ-۶۴ آپاچی» ارتش آمریکا که در نزدیکی سواحل عمان دچار سانحه شده بود، توسط نیروهای آمریکایی نجات یافته‌اند.
بر اساس بیانیه سنتکام، این حادثه ساعت ۷:۳۳ عصر به وقت شرق آمریکا در روز ۱۸ خرداد ۱۴۰۵ رخ داد. این بالگرد در زمان وقوع سانحه در حال گشت‌زنی بر فراز آب‌های منطقه بود.
سنتکام اعلام کرد دو نظامی حاضر در این بالگرد ظرف حدود دو ساعت نجات یافتند و در وضعیت پایدار قرار دارند. این نهاد همچنین افزود که علت وقوع حادثه همچنان تحت بررسی است.
یک مقام آمریکایی به شبکه ای‌بی‌سی گفت دو خلبان این بالگرد پس از سقوط در آب، توسط یک شناور سطحی بدون سرنشین یا پهپاد دریایی از آب گرفته شده و به خشکی منتقل شدند.
به گفته این مقام، پهپاد دریایی مورد استفاده در این عملیات طراحی مشابه یک قایق تندرو داشته است.
@
VahidHeadline
هنوز مشخص نیست که آیا این هلیکوپتر بر اثر آتش نیروهای ایرانی سرنگون شده، دچار نقص فنی شده یا با مشکل دیگری مواجه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76096" target="_blank">📅 17:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76092">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EgNZVczGrfeD0pGCHJgXFYtaMwvri-F9fyjY_DBzUBW6AkGnKaNCaAoh3kQEAR3QSqbxqrzKE_wQT0bsv01pn20eTrBC--hTM70EoKWtr04FzfZMIy1UDNQCqmOizcf9PdDVZZxVfjoqK1BTzQnqkrA8OhkdVeQ06Px77xoQg37gcYKS7-IUCPwPrIbOtQniAXQ4TOrZD71WQq6kldi2ifXRQp42agGkcaIXafU62SKZ9WyQjoQaA_jQ6Y70ed_4r5P9daSbPV0c9AVcR7Zl-twfVcbQoM_n_eJs-hiQAtwNAbuC64afKtXUmBTJf8nvzZzTSLX2xhnE2VHtqjFwRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NJopRTIHM8loYB5NmG2fpyZsqZBPYthexAkDkBkYJc97VkHmTa3zlbjZrmeNdJ4FZe3dgAT2gVdCA0iA7NChi4EKD5uVdOQuGiFOy5TLThEOEYsdb0N5ifaKW99c-rRKpzFhH1GiIv_Kh6zKKkKetRaBVWjZ41SYFW7D1B48HFjORUjkvS6pWyOEiDW6v54Llx6HjPhAo-8kf8oC_V94Ql6Bgwh6KZjTnJqQ3mqn43VkgP5PX1DvlcIGRYeQSmXW0PS1JVTIAhDOj46TIlmOjCT9B839qImAd8mPMIysAUOah8AEqagk_9Q_fMP7qcBTWL5vl_La0mcxQTOPa3GDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NYA516Uk9VuL3_XnK-PcZzNmHr4j6zS0cH5DO87shj0Zvy6shgOPAQMOfmwJ8k8Lk2TszbenGhcXLiviNRp9samwIfs2Z1fZWVokF381oErqr4MyIpLtK6pwIp0eeDUcK3iT4xihv1Ifaucf3hSDwXGR-KkbQ9_J1yYRLzv-B_5SFXxN7p8CF29Ux-n3VPr9bePbHMyefPNMMqMj06kE5AzEslrUi_gqMuVlCk_NWNKZzbxxHe4A33kBSUw5hRyCD6r5fjHfE_cFJi6xc9EEqqUsNJFykJkZFJkJuBNY0iE4KesI2aBg91VztXV2uLRSEEIOqptLQAyMHvyNf_nMRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8642136842.mp4?token=G0tk89foMeuO5C7y6M-t8rPsNBrJZph3eZC4EoJykS1xbh4bb0Zir4OdirzJvj_JbitocxIpUsEJKgyWjh0qiHVpD8dV3G0Nmx3-etcbGtnCY260JBXIbHlEjOQvagiZZHtpmu83lKyoplXUF4xLcBXMyuWgjFfDfOtI3--1INDe0KvVdUv8rt94b8fg4htapiaRRkpYJMJKBV-784FzpA2JQA8i8Fakvf_Pl8R2jWPRcaVCKIFpcw8VqQyOgVk2i_R9ex6TNRJX1laLe84Qb9-bQpT140LBqUjKQA7YIV0O-B55AccCFAc7r6eMskjWASSs2dgZq9kpeEoE5bTIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8642136842.mp4?token=G0tk89foMeuO5C7y6M-t8rPsNBrJZph3eZC4EoJykS1xbh4bb0Zir4OdirzJvj_JbitocxIpUsEJKgyWjh0qiHVpD8dV3G0Nmx3-etcbGtnCY260JBXIbHlEjOQvagiZZHtpmu83lKyoplXUF4xLcBXMyuWgjFfDfOtI3--1INDe0KvVdUv8rt94b8fg4htapiaRRkpYJMJKBV-784FzpA2JQA8i8Fakvf_Pl8R2jWPRcaVCKIFpcw8VqQyOgVk2i_R9ex6TNRJX1laLe84Qb9-bQpT140LBqUjKQA7YIV0O-B55AccCFAc7r6eMskjWASSs2dgZq9kpeEoE5bTIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از برقراری تدریجی دسترسی به اینترنت در ایران، ویدیویی در شبکه‌های اجتماعی منتشر شده است که فرزند جاویدنام نسترن زارع‌منش را در حالی نشان می‌دهد که پشت پیانو نشسته و هم‌زمان با نواختن ملودی، یاد مادرش را گرامی می‌دارد.
نسترن زارع‌منش، ۳۹ ساله و مادر دو فرزند ۱۰ و ۱۵ ساله، ساکن تهران بود که ۱۸ دی ۱۴۰۴ در جریان انقلاب ملی با شلیک گلوله نیروهای سرکوبگر جمهوری اسلامی به سینه و گلو جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76092" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76091">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TH7TQbunFKGv4b5VAgfcc24PbHy5mpnwoGwBbCgnLU4DJ0NjvDrRGRaD1HwjclfEwnuekksEwmJcAhO7wQHjW1fXXlbK_FGCD-fU5G3gzZmCargWioBNuzHSxcgIN0OZk_Pm2-srXIddHlYP9yNbGVCBOZhACEE9l5ikjZvvrupShnEmIVtoVMUQT2OZ74LbEd77udauM6COsUU2i9DWGLFWjaM1qAQsAios42_6yrIL3UHSej0KRhfq1WioUckYo2wEajytCRzBM8R7mRuWsU0g_XbGJ8T75y2AYs3SFi4zYc0P8OPPh0Fokyc3FC-_Vw2fn76S6Sg_mQmzOyaYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون ترامپ، در مصاحبه با فاکس‌نیوز ابراز اطمینان کرد آمریکا و جمهوری اسلامی می‌توانند درباره پرونده هسته‌ای به یک توافق بلندمدت برسند.
او گفت صرف‌نظر از اینکه اسرائیل از این موضوع خوشش بیاید یا نه، چنین توافقی به نفع آمریکا است و واشینگتن به پیگیری آن ادامه می‌دهد.
ونس با اشاره به نگرانی درباره اینکه تهران ممکن است در حال بازی دادن واشینگتن باشد، گفت: یکی از مهم‌ترین عوامل موفقیت این توافق نهایی این نیست که جمهوری اسلامی چه چیزی روی کاغذ می‌نویسد، بلکه این است که آیا واقعا به برخی از الزامات توافقی که به آن می‌رسیم پایبند می‌ماند یا نه.
او با تاکید بر اینکه آمریکا تعهد جمهوری اسلامی به چنین توافقی را در بلندمدت راستی‌آزمایی خواهد کرد، گفت
:
بیایید صادق باشیم. ایرانی‌ها نمی‌خواهند این جنگ ادامه پیدا کند. ادامه جنگ به نفع آن‌ها نیست. آن‌ها پای میز مذاکره آمده‌اند و پیشنهادهای واقعی را مطرح می‌کنند. اگر به این توافق برسیم، یک موفقیت بزرگ برای مردم آمریکا خواهد بود.
@
VahidOOnLine
جی دی ونس در گفتگو با شبکه فاکس نیوز: موضع رییس‌جمهوری کاملا روشن بوده است. اسرائیل اهداف خاص خود را دارد، اما هدف اصلی آمریکا در قبال ایران این است که اطمینان حاصل شود ایران به سلاح هسته‌ای دست پیدا نمی‌کند
جی دی ونس: در ماه‌های گذشته و در واقع طی حدود یک سال و نیم اخیر، شرایطی ایجاد شده که رییس‌جمهوری معتقد است ــ و من هم فکر می‌کنم درست می‌گوید ــ می‌توان به یک راه‌حل بلندمدت برای مسئله هسته‌ای ایران دست یافت
ونس: ممکن است اسرائیل از چنین توافقی خوشش بیاید یا خوشش نیاید، اما ما معتقدیم این مسیر به نفع ایالات متحده آمریکا است.
به همین دلیل به دنبال آن خواهیم رفت، زیرا این همان چیزی است که رییس‌جمهوری آمریکا برای انجام آن انتخاب شده و همان کاری است که برای خدمت به مردم آمریکا باید انجام دهیم
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/76091" target="_blank">📅 06:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76090">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yor7IqOMJ2fv1g47pN5Pl8xiw-Ch_7QbKQa8CIe5nDb1rHUeLTDcjc1Tba6VQslDDiiqL4ETuPDd3NuKy_mz0m0Owf8-psiDts9OIBru_DM96vsWUuPS-aN8L_XwR8mimuxNy3Ff_riguJFSDc-W8hld1lysErCOU0tfqhvadlm4uifNTJpVbqOjMhPNf80K5-5K0d8IqJPIJsnBd6ee6ogBpjX1KZuv7h5BySLD8ks-_CfgyMeJSmQ7vyx7tkqunXgdYreLabGfEmNU0xfaBcNjQWXe2A2oC_dK-7BPMR6hfXgkZNLGC6MAicisCz4_yHgYBEI_4S2UJLaESBs1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه با تاکید بر موضع سرسختانه واشنگتن در قبال برنامه‌های هسته‌ای تهران، با تقدیر از همراهی لیندزی گراهام، سناتور برجسته آمریکایی گفت:
«لیندزی در تمام این مسیر پابه‌پای من جنگیده و ما تیم بسیار سرسختی بوده‌ایم. من فکر می‌کنم در حال پیروز شدن در این نبرد هستیم، اما طی دو هفته آینده با اعلام پیروزی کامل، برنده واقعی آن خواهیم شد. این یک پیروزی کامل خواهد بود که بسیار زود رخ خواهد داد.»
رئیس‌جمهوری آمریکا در ادامه با اشاره به نابودی گسترده زیرساخت‌های نظامی ایران، این وضعیت را مصداق تحقق «صلح از طریق اقتدار» دانست و خاطرنشان کرد:
«ما در حال حاضر مشغول مذاکره هستیم و آن‌ها به شدت می‌خواهند یک توافق بسیار خوب انجام دهند. آن‌ها اکنون حاضرند همه‌چیز را به ما واگذار کنند و توافق کنند که ایران هیچ سلاح هسته‌ای نداشته باشد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76090" target="_blank">📅 02:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-yy9ad6XtWKjSoyfy1WfJ2K45npBR1POHFIXHA_aNv4dF9BeaGDYGYqVcOTC15uK4TVCvo50OHYoargqBC-kVXHsPCYhm1wV0kGbdsxgMoIKSFl8QNg2-tp3m9UeboecxkDuCaRQQ2jXYM5hsr40pym3kLWSSBwwDCe3a-V5niQlxvFvmCOekSkA304Z6o58veYub6-qeD31wJXv6tsSgxCFd1OwCGJGfsYOvVcCJTy1ffjj7qQX3mbtb8DZofoYOirrr1mcEOzPb4ci-5f0ggEH0wnNjgqSTcaT6TxmmDK40Yn62RUdywXrxavMM5HBgIZsHhmPuxBe2icZ0g0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران در اظهاراتی جدید به حمله موشکی شب گذشته از خاک یمن به سوی اسرائیل واکنش نشان داده و آن را نشانه‌ای آنچه «هوشمندی جبهه مقاومت» خوانده، دانسته است.
آقای قاآنی روز دوشنبه گفت: «اقدام به موقع و با اقتدار یمن قهرمان نشان از هوشمندی جبهه مقاومت دارد اگر لازم شد دیگران نیز می‌آیند. شرارت‌های رژیم صهیونی و آمریکا در این منطقه عکس‌العمل جبهه متحد مقاومت را در پی خواهد داشت. رزمندگان بدون مرز مشرف برگلوگاههای عبور شما هستند به تعرض ادامه دهید گلوی شما را خواهند گرفت.»
یکشنبه شب ارتش اسرائیل اعلام کرد که پرتاب یک موشک از خاک یمن به سوی اسرائیل را رصد کرده و کمی بعد از رهگیری آن خبر داد.
کمی بعد حوثی‌های یمن حمله به اسرائیل را تایید کردند و گفتند که «منطقه اشغالی یافا» را هدف قرار داده‌اند.
حوثی‌ها همچنین در بیانیه‌ای «ممنوعیت کامل و مطلق» تردد دریایی اسرائیل در دریای سرخ را اعلام کردند:
«ما در قبال محاصره ناعادلانه تحمیل‌شده بر مردم خود و مردم محور جهاد و مقاومت در فلسطین، غزه، ایران، لبنان و عراق ساکت نخواهیم نشست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76089" target="_blank">📅 02:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76088">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a40e8ba.mp4?token=pX0q9EEHg5NjFj3ZlcFdByRN7GSiV_y8JkBnu391_lsN3uVgcUoOTFb4ia1Ia-e9Ohox6COGPbkIOujPvyrKmWZp0REJ0oQrMT14qaEiPKnE34GhDR2yzU-5awwbz7TWjatlspePFFOlVbrTpaGxmz7OnMqKgOtuEXpjM56I99iftl0s1VnKKsYnlQfQ_FsrJ9JPZ6ewkqRTkFJw7Uk_-cXCNPctonW7Gp7apRY6gGNrxPq_Gzdu85mqiIynJcA5ps76d_gK3g3Bukyo47IBblXS47d4UXDi2YQaz6wsV4to9grez1aRbehWIGxD3LLgKgsA6LjRwkUAzwVDGYekPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a40e8ba.mp4?token=pX0q9EEHg5NjFj3ZlcFdByRN7GSiV_y8JkBnu391_lsN3uVgcUoOTFb4ia1Ia-e9Ohox6COGPbkIOujPvyrKmWZp0REJ0oQrMT14qaEiPKnE34GhDR2yzU-5awwbz7TWjatlspePFFOlVbrTpaGxmz7OnMqKgOtuEXpjM56I99iftl0s1VnKKsYnlQfQ_FsrJ9JPZ6ewkqRTkFJw7Uk_-cXCNPctonW7Gp7apRY6gGNrxPq_Gzdu85mqiIynJcA5ps76d_gK3g3Bukyo47IBblXS47d4UXDi2YQaz6wsV4to9grez1aRbehWIGxD3LLgKgsA6LjRwkUAzwVDGYekPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسی حکومتی در صداوسیمای جمهوری اسلامی مدعی شد آمریکا در جنگ ۴۰روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته است.
او گفت: «برای ما کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها هیچ کاری ندارد» و افزود جمهوری اسلامی به درخواست «عالمانه و عاجزانه» کشورهای منطقه خویشتن‌داری کرده است.
پیش‌تر، دونالد ترامپ، ریس‌جمهوری آمریکا، چهارم خرداد در مراسم «روز یادبود»، یاد ۱۳ نظامی آمریکایی کشته‌شده در جریان جنگ ایران را گرامی داشت و گفت آن‌ها جان خود را فدا کردند تا اطمینان حاصل شود که ایران «هرگز به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
"روایت فتح"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76088" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76087">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">زمین‌لرزه در هرمزگان
پیام‌های دریافتی:
سلام وحید جان
زلزله همین الان بندر عباس ساعت ۱۲:۴۰
آقا وحید بندرعباس همین الان زلزله اومد
قشنگ زمین لرزید
00.39 بندرعباس زلزله شد
زمین لرزه نسبتا شدید ساعت ٣٩ دقیقه بامداد بندرعباس
داداش همین الان بندرعباس زلزله‌ اومد
🔄
آپدیت:
‌
خبرگزاری فارس: زلزله‌ای به بزرگی ۵ و در عمق ۲۲ کیلومتری زمین، منطقۀ سرگزی احمدی در شمال هرمزگان را لرزاند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76087" target="_blank">📅 00:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76086">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPscJAwfqru5w-ClTr0RY1Ngdh5j0q9KVS7tvNtI-_48eH_YOz1qR53-vu8pBrUW86ZQA2Zy531TTFolNT_W4emY_rYDxC3gvTVGva2pHBPXUndCkfuaGrkpS_HLslXCWVFh-IyOB3bdVUMRDErXULnUKPoufGnftHsBEzn1m3a9OySxQw6ZV_pdqIOpTAE9ikYBsb8z-isde6IrFS57FhEvaJYvGP_UetTizHtQmQWZlL6W714YC9NgFpsGUyA9X9kmBSKVuyNEfPzPxcn4RawMLcHu2ude5gT_L1dsNrZ9AJoY1qWSWhUq5q6RUp24em_ven1rkpvLdDTZi09aiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سارا اسمیت، سردبیر بخش آمریکای شمالی بی‌بی‌سی، در یک تماس تلفنی کوتاه با دونالد ترامپ درباره گفت و گوی تلفنی روز گذشته او با بنیامین نتانیاهو، نخست وزیر اسرائیل، پرسید.
وقتی از آقای ترامپ سؤال شد که آیا نتانیاهو با حمله موشکی به ایران در روز یکشنبه از درخواست او سرپیچی کرده است، رئیس‌جمهور آمریکا این موضوع را رد کرد و گفت: «نه، نه. موشک‌ها از قبل شلیک شده بودند. آن‌ها از قبل در راه بودند.»
او سپس افزود: «اگر به او بگویم کاری انجام دهد، انجام می‌دهد.»
این تماس کمتر از یک دقیقه طول کشید.
در بخش دیگری، سارا اسمیت از آقای ترامپ پرسید که برای متوقف کردن حملات اسرائیل به ایران به نتانیاهو چه گفته است.
«تنها چیزی که گفتم این بود که باید از عقل و منطق استفاده کنیم. ما به امضای یک توافق بسیار قدرتمند و بسیار خوب نزدیک هستیم. بدون سلاح هسته‌ای، بدون هیچ چیز دیگر.»
او ادامه داد: «می‌دانید، باید از مقدار زیادی عقل سلیم استفاده کنیم. همه چیز خوب بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76086" target="_blank">📅 00:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
وحید جان گیشا یه جارو زدن یه انفجار وحشتناک بود
[از روی صدای یک انفجار چطور میشه تشخیص داد که دلیلش حمله بوده یا چی؟]
وحید جان ۱۲ و ۱ دقیقه صدای انفجار خیلی خیلیییی بزرگ
گیشا
سلام از گیشا
یه صدای خیلی بلند انفجار اومد
همین ده دقیقه پیش
همه ی همسایه ها اومدن دم پنجره
نمی‌دونم چی بود خیلی عجیب بود
همه جا لرزید
📡
@VahidOnline
۲۰ دقیقه صبر کردم ولی پیام‌های زیادی دریافت نکردم.
آپدیت:
ما وسط گیشاییم و خونه هم ساکته، کوچیکترین صدایی نیومده
وحید جان راست میگن دقیقا ۱۲ و یک دقیقه در گیشا صدای انفجار بزرگ اومد،اما فقط یکی و واقعا نمیدونم چی بود، ضمنا برخورد به زمین و یا عمیق نبود.
من گیشا زندگی میکنم ، با اینکه امروز ظهر هم گفتند یک جا یک جای گیشا را زدند متوجه نشدم
حتی الان هم که پیام گذاشتی داشتم می‌خوندم اما متوجه انفجاری نشدم
من گیشا هستم چیزی نشنیدم
آپدیت:
بعدش کلی پیام دیگر هم در تایید و تکذیب شنیده شدن صدا دریافت کردم ولی چون بعد از انتشار پست بودند نمیشه خیلی روشون حساب کرد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76085" target="_blank">📅 00:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzsmHCTqI_E865F8mn33D19NlBtDp-xHXfhdAaEw4tPCqr9_DfMzuHRjZkZsVlm_3xGhNgrTfMMuqhXyVMlqyWY7Kqm9FDJz6g1XmiD9xh59-elC-GNLkqYZJzuzpAPTCmKCpsoQfoZ4Zm0HZ7reLaop7_Jc0B9Lft1G53ntkQSyuycu-icp_Lq9-bLk_3-NHDh5Ea5OHYLpvZqey-OKkgCDYFXQJtbSgQeEWtHLXU3SHoWCMG1_fZmQ39YK5BEyUZ9SSeTNrMkLhVqpam7iVLvG0tiZeiQklNKACN1IaIzHeMcFgM-bY221miiNBit3V-mzmlLiVXV9jFRga82U3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبری سی‌بی‌اس، روز دوشنبه ۱۸ خرداد ماه گزارش داد، دولت دونالد ترامپ قصد دارد روند لغو تابعیت ۱۷ شهروند آمریکایی را که به تقلب در پرونده‌های مهاجرتی یا برخی جرایم متهم هستند، آغاز کند.
بر اساس این گزارش، وزارت دادگستری آمریکا این افراد را به پنهان کردن اطلاعات مهم، ارائه اطلاعات نادرست در روند دریافت تابعیت یا ارتکاب جرایم مختلف متهم کرده است.
سی‌بی‌اس نوشت این اقدام بخشی از کارزار گسترده دولت ترامپ برای استفاده از سازوکار قانونی سلب تابعیت از افرادی است که به گفته مقام‌های آمریکایی، شهروندی این کشور را از طریق تقلب یا پنهان‌کاری به دست آورده‌اند.
در میان افرادی که هدف این اقدام قرار گرفته‌اند، نام چند نفر که به جرایمی از جمله سوءاستفاده جنسی از کودکان، کلاهبرداری مالی، پولشویی، تقلب مهاجرتی و استفاده از هویت‌های جعلی متهم یا محکوم شده‌اند، دیده می‌شود.
تاد بلانش، معاون دادستان کل آمریکا، گفت دولت در برابر سوءاستفاده از روند دریافت تابعیت «هیچ‌گونه مدارا» نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76084" target="_blank">📅 23:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76083">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ02TdcB8M8b4g5eKebKtUbHBtkk5cpO5_nSnSNd42pymJtlTWimLbauGK2wIPoHkSy16_P3IlxbPSKsBu3kUED4kw1o5aoad3cDjuAnT5IUUlarPw2jSAUxfI-wlUF7B-6FnY-eu2yjdI23Al8cgoJopqhOxP2kii_XBdiOpMQLXzQd83qpahKCl3Bm8_gh9Mb5ireOteWsNr_1sZSiIaRnZqr3bj14d7xGFHAZPkZ2FxjZfjzCJjo9HEKnvnfspNfkxsxH511XRr_rM2N5RGOsyXvLIR5rQfBklQOPz9KnC98N-7wp8s0dO6RYAnAs8_TBGVtllZBT1Jy6-3JV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری سی‌ان‌ان، شامگاه دوشنبه ۱۸ خرداد ماه، به نقل از یک منبع اسرائیلی و یک مقام آمریکایی آگاه گزارش کرد اسرائیل در حال آماده شدن برای حمله‌ای گسترده به تهران بود، اما دونالد ترامپ، رئیس‌جمهوری آمریکا، در تماس تلفنی با بنیامین نتانیاهو از او خواست از انجام حملات تلافی‌جویانه بیشتر خودداری کند.
به گفته منبع اسرائیلی، ترامپ در این تماس از نتانیاهو خواست دامنه واکنش اسرائیل را محدود کند تا از تشدید تنش‌ها جلوگیری شود.
بر اساس این گزارش، نتانیاهو در نخستین تماس که شامگاه یکشنبه به وقت آمریکا انجام شد، در برابر درخواست ترامپ مقاومت کرد و اصرار داشت اسرائیل باید به حملات ایران پاسخ دهد.
با وجود اخطار ترامپ در گفتگوی یکشنبه شب، ارتش اسرائیل برخی اهداف را در ایران، از جمله یک مجتمع مهم پتروشیمی، هدف قرار داد.
این شبکه همچنین نوشت لحن گفتگوهای اخیر ترامپ و نتانیاهو به اندازه تماس‌های هفته گذشته تند نبوده است. به گزارش سی‌ان‌ان، در تماس‌های هفته گذشته تنش میان دو طرف به حدی رسیده بود که ترامپ با الفاظ تندی با نخست‌وزیر اسرائیل صحبت کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76083" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qttqmcMHp5CH9q2W6b36PtAB37SKQPJaG-IGwkf6HafJsIIpyP9CEJMZA02f4bWbKCxxScSsU9Ks7jah85ArTbmNYACnb3a324oTDs61zjwpLsItIW14FLL6KysbGzT-MIhfxFrj6X5ebgSuAbrJFtq1yusyA9P0Ks66h7uhkmyaavIvPAiuIca-dsDZ4bFAf9x80U1evaQ_cCI6mPXOB3TrXTpQsktdePWwwTa7hHvQINkdqiA1mIepMsLqFUdXLZCkyKYHXgKu9voJ2fhy7iSQnYF4E7Naj8EzMGBEv1EK_DlDBVyKJ43YdkPHmRnEvN72dI0zfehr0uHUvfS6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان، درباره حملات موشکی اخیر جمهوری اسلامی به اسرائیل نوشت که دشمن در کوتاه‌ترین زمان ممکن ناچار به التماس مجدد برای پذیرش توقف آتش از سوی تهران شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76082" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r6Szcm9XDNJuZcaYFPalESyyltbeMEy5p7czzEEXCTo_xUVIq57hA-sqh3NNIZqmMXL-bBrCYmntLiWDzJ8-CqjaMIEgAP5GadgRoBfqHY5nO7iZEgDcknouOS0kWQYAipr_1SfmIpeum2dUKMYMUUEtAqYcHJfiZ1RJ0JvIEFTDhEh9QAVCeA5v0FSWG1LoVtOw6riNd6dq5u5A-WE6wrQTpEPRqN7esd8eVDXg-d_2nfrncdmYTf-u5F-DFxIIzPZkcvd2CdOCl_XdjRqZv6MLOWN9rLA6RU8dWYHlS6u4MMe_fVQrCYOK2Wg3tafYVzuC7cYYHLUhALK2s3NaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kAiAVanRo-lOrASSmvA6DOEdLUIO1hH4Nj7I5nYNlsyanLM1PJgkO-98EMU8zZMDzSP-GpwBum4rEWLJhHODWoZ-bseKylMiHivrVsqvd_nfDPwVYn7Xp9_z2sbDvrZZ9CiT8Po8Btr_HI6-vzqqZ4Q4c5LO-OAberd8VAgc9LLT3oiBu7Hj7xR7nr761XrkzuJdBSDz8ue2X7IEWdHVZmUvGEJffuwk09fSIsmN8-eEK5rW7KV6gUOb-ttNAgGGp0AIxhBnsznV8Al0NgHiuWnpiE7pXgvq_iwPUu7tPrPxTijzSWmTrZLDIcrMKD8gbbhCIC6ZCA0cRRxG6-Ztqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ گفت: «به بی‌بی گفتم خیلی مراقب باش چه کار می‌کنی، چون ممکن است خیلی زود در برابر ایران تنها بمانی».
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز دوشنبه در گفتگو با کانال ۱۲ تلویزیون اسرائیل اعلام کرد توانسته دامنه حمله اسرائیل به ایران را محدود کند و بنیامین نتانیاهو را برای کاهش تنش‌ها تحت فشار قرار داده است.
ترامپ گفت: «من موفق شدم شدت حمله اسرائیل به ایران را کاهش دهم.»
او همچنین افزود شماری از کشورهای منطقه از او خواسته‌اند بر نتانیاهو فشار بیاورد تا از تشدید درگیری‌ها جلوگیری شود.
رئیس‌جمهوری آمریکا در ادامه گفت در مورد حمله به ایران به نخست‌وزیر اسرائیل هشدار داده است: «به نتانیاهو گفتم خودت را در برابر ایران تنها خواهی یافت.»
ترامپ همچنین گفت نتانیاهو «با تاخیر مرا در جریان حمله به ایران قرار داد، اما من موفق شدم این حمله را کاهش دهم.»
کانال ۱۲ تلویزیون اسرائیل عصر دوشنبه ۱۸ خردادماه به نقل از یک مقام رسمی دولت نتانیاهو اعلام کرده بود اسرائیل حملات به ایران را به درخواست دونالد ترامپ متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76080" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XWWvh9NtvEr0rL3P4f54GmYTI4K9NKg5btGxlPb-0iBkas2bbIlIVS3VeOkRvkw4Sn6c_rtcCrva2EjYz4dv39gDIQrxYh3-StKx-r8xO1RpILOVqzivnG1_rc-ygiJYEMY483L5TRI0yYtVS2oBcEb_vcVh1c8aBkogIaoLt0ScBGJIGLrdmwd4rGQVqiSq0Qa0O26kHARkLT_wEVD093kKwQxE5pXtZqawIMYkhIBwCbMIBBaLCEi1FLwVpybUB6IRTyuRdSAF_MSo6P8DvRbmtrLc3ioHi6i8BnOXKqIFJ4QQcpBPy9UgdiWrfdWF4f9aDmp8XPqcFk7Hv5GBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: نیروهای آمریکا نفتکشِ متخلف را در خلیج عمان از حرکت بازداشتند
پست اکانت فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
تامپا، فلوریدا — نیروهای آمریکایی روز ۸ ژوئن یک نفتکشِ بدون بار را در خلیج عمان از کار انداختند؛ پس از آن‌که این کشتی با تلاش برای حرکت به‌سوی یک بندر ایرانی، محاصره جاری علیه ایران را نقض کرد.
فرماندهی مرکزی ایالات متحده، سنتکام، نفتکش
M/T Marivex
با پرچم پالائو را هنگامی که در آب‌های بین‌المللی خلیج عمان به‌سوی ایران در حرکت بود، از کار انداخت. یک جنگنده
F/A-18 سوپر هورنت
از ناو
USS Abraham Lincoln (CVN 72)
پس از آن‌که خدمه کشتی از اجرای دستورهای نیروهای آمریکایی سر باز زدند، یک مهمات دقیق‌زن را به بخش‌های مهندسی و هدایت کشتی شلیک کرد. کشتی Marivex دیگر به‌سوی ایران حرکت نمی‌کند.
از زمان آغاز محاصره در ۱۳ آوریل، نیروهای سنتکام هفت کشتیِ متخلف را از کار انداخته‌اند، ۱۳۴ کشتیِ فرمان‌بردار را به مسیر دیگری هدایت کرده‌اند و اجازه عبور به ۴۲ کشتیِ حامل کمک‌های بشردوستانه داده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76079" target="_blank">📅 20:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgSm2lweuGNn81SikrMmbRD6PIVBrj1B_An4UvTAEkqu75KCmAr5-LR8zWkDcE68_rYtNba2oo6PC7nnqfChmSX544K0Ey6gGcIX_atiRuWWci2FwRwAl7MeNuK_YLJz1_UIaWr6Rc2sNODaRwYVeop9Q-pRBWfjRXUy_PFWj3Vt-kc5GnvfAuxH74mMqn09xEPqdwf37GoDisLiJinPOAGNxo8t3Ii2vXWpflSk7Q6g6-FhOvJqBZF4gj1_m2byAWyZ6Nr9cZqtk78IaMvd9AeV5rBoUtp8mq3WWTE_tOwEhncoRR9AJQRrrbDaxeI-l4nIotiHHVHMR5vtb4uc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.  به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.   اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع…</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76078" target="_blank">📅 19:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lY2i4oP1tZj91nryditD6L8LEebJkX8dnBNaMkoTeDyR6b2EHax2TAzjiq0pycayG1pI9ZqZNMFcZs8zXESsJTnjxCVPaISpGosvq8XvkTOEY5ktKbJYXc3CXRbXJNBZ3diFpJA9DWuK-NEEqR-tEtJCFM3-8MXP0cb35dUKgzjrGntF-D-iHHBguvA7eu5eQt44_QZ9f8gD6Om3JwvQCZn4r_JvbdD7C8nw8BVeA1UTkQGhZ5_ai1cp2GYANpokttCdeVDcG0oqLsOuGI9YpJQTIiH2VywErbtXn48Da6OCokGl4J6OhW6IRpHg-52KZOJWwcGLksccsE0haF7sTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران وضعیت پرواز‌ها به حالت عادی برگشته است
سازمان هواپیمایی کشوری ایران عصر دوشنبه اعلام کرد که فضای هوایی کشور به شرایط عادی بازگشته و عملیات هوانوردی مطابق با اطلاعیه‌های هوانوردی (نوتام)، از سر گرفته خواهد شد.
ایران ساعاتی پیشتر گفته بود که تمام پروازها از فرودگاه‌های کشور لغو شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76077" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oB4fN1RTXLUxlsJbiJzU6ny0UOTC3z58ExhpzT2whZD8ZuO7J5HlfkjxF0tFSDVtB5iC0ZezGzFLMUjfBSVVkBjGWWWYGnUP3X1HCO970FVX6VVgfnXTsrJjV-myDzLkU1Hw0JQfRjHDhKr5OW0tqS-76NKG_LLTSuM07unLxcdwGxn4ainZjoMA2sNbpYgCYTf3ODyhtf1D4zNlZltLl_-y8m1VEU_BTDVsVKrxsvt79MK_1m9HuygMjA6rTrnpQm7KNSDnYSPVg4s2bcc0WK8RBguXEBV8pZQD9aBW60SPAKQ_4-bd9PTcT0p4bPr302YDloIfRsrjHA-Yh9bt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد یک موشک بالستیک که از یمن شلیک شده بود، در منطقه‌ای خالی از سکنه در نزدیکی مرزهای عربستان سعودی و یمن سقوط کرد.
به گزارش رویترز، وزارت دفاع عربستان سعودی اعلام کرد این موشک به سمت یکی از کشورهای منطقه در حرکت بود.
همزمان حوثی‌های یمن، تحت حمایت جمهوری‌ اسلامی، اعلام کردند دوشنبه یک حمله موشکی به منطقه یافا در اسرائیل انجام داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76076" target="_blank">📅 19:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYKZwl0pTk0WGwLmtdHqHYnrSmEr6sf21EOddbefU7zGpgP8BVEFOWGPpK3ssI5Y1YZRJY-dt0kqIgZ0GS3qmVTG9htmz8Ow_qWsW5OQ7iIdKNtaU9iMk9E1ejoWrBl7Z7iPvGhoXVnNnrl5f0SpPb5oP0Ni22R9W_vu5j84tCZ0Jw7oDjqW8FCstaN9xF-H9AU4tvRkBhkpQY-Gxdqd_BMoJQnRb-qQ2n4u8MlMeWIPGfYKEHRAfx3-GD2P4xYPEpswgopVaaV51xwNHA2xyzd_5XK91V7Y3bERhsAgeWz_lgvz56eAsbBsQVFycbc7TftbB4EqhNqXEK0pdjHubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اظهارات مطرح‌شده از سوی ارتش اسراییل مبنی بر مشارکت ایالات متحده در رهگیری موشک‌های بالستیک شلیک‌شده از جمهوری اسلامی به سوی اسراییل را رد کرد.
به گزارش سی‌ان‌ان، این مقام آمریکایی گفت ارتش ایالات متحده هیچ‌یک از موشک‌های ایرانی که بامداد دوشنبه به سمت اسراییل شلیک شدند را رهگیری نکرده است.
این موضع‌گیری در حالی مطرح می‌شود که در دورهای پیشین درگیری میان ایران و اسراییل، آمریکا با استفاده از سامانه‌های دفاعی خود در رهگیری برخی موشک‌های شلیک‌شده به سوی اسراییل مشارکت داشت.
@
VahidHeadline
نباید اینجوری نگاه کرد که تعداد موشک‌ها چقدر بوده و نیاز به کمک داشتند یا نه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76075" target="_blank">📅 19:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76073">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aB3m9UE0yHfbD3vQ89rRwrNG1xGexc28Z_G3X9eGpWCkQagIvZLWXxBCn9zC8TOH3WKY3CFLQ7dm-ddrnY_1HZ6xX3brR2c2mezSAqQSNxa8BDzkkysUwy_DaHl3WOngmt_L3rHSAxJvNFrROYBqI9xyN-ieEnsYFPXd9gS8CZCahkVDpWqxhATMDmLLmaI42Vn0IJepvjG2QLX_ZfAWBi95CEU4A_U9Bv3-1Z08onY5BbKF_agIAKmPyMKmGzQSs3xBhYryJIjkIMeBAX69rObXUy_HDCfcHgmI3L4Ltv_XQ55oSbgpiAnV7dN_ni2ZzXfoC3Ho7JB2H_NYpXPU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fca0bb1962.mp4?token=k4uQO_FCz2TlUKLvUvF7KTleHDByhdbfn9wafm2HCttTyGSGnPLmcZoSWbQp6NaBO9V1ejYgaQtG_zmkgna3DMEbX9amsf4sOckp8wE-Q7ndyTcs5vHkDp83FYmer-22I8wcetZ5ZT7UVZoL-uQy3UVR1iCQHwmo5418PorB9pe_TmmOvMnEZjBN5St-fH6HlyhcOlfnVLYWJ3fENLlIFgVhoXfnKeYAWB76s-EWnscLwsqI5Rehtmo6KiYDAgWr-F6pQnDOIc6wdPCuAS3h-eU9S-EeKNfg-nouYqJ27_L2NJGMf1wyIj7hCFnlXuGNf6vd8LePtqNBc4pUO4JAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fca0bb1962.mp4?token=k4uQO_FCz2TlUKLvUvF7KTleHDByhdbfn9wafm2HCttTyGSGnPLmcZoSWbQp6NaBO9V1ejYgaQtG_zmkgna3DMEbX9amsf4sOckp8wE-Q7ndyTcs5vHkDp83FYmer-22I8wcetZ5ZT7UVZoL-uQy3UVR1iCQHwmo5418PorB9pe_TmmOvMnEZjBN5St-fH6HlyhcOlfnVLYWJ3fENLlIFgVhoXfnKeYAWB76s-EWnscLwsqI5Rehtmo6KiYDAgWr-F6pQnDOIc6wdPCuAS3h-eU9S-EeKNfg-nouYqJ27_L2NJGMf1wyIj7hCFnlXuGNf6vd8LePtqNBc4pUO4JAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل روز دوشنبه ۱۸ خرداد با اشاره به توقف حملات متقابل اسرائیل و ایران گفت «آتشباری متوقف شده اما اگر رژیم تروریستی (ایران) اشتباه کند، ما به شدت پاسخ خواهیم داد».
بنیامین نتانیاهو در اولین پیام ویدئویی خود پس از آغاز موج تازه حملات ایران و اسرائیل، افزود: «ایران و حزب‌الله از همیشه ضعیف‌تر و ما قوی‌تر از همیشه هستیم».
به گفته او، «ایران و حزب‌الله تلاش کردند معادله جدیدی را به ما تحمیل کنند که از نظر ما غیرقابل تحمل و غیرقابل قبول است. آن‌ها فکر می‌کردند که از خاک لبنان و از ایران به اسرائیل حمله می‌کنند و ما سکوت خواهیم کرد. این اتفاق نیفتاد و نخواهد افتاد، نه در زمانی که من رهبر هستم».
نخست‌وزیر اسرائیل تصریح کرد: «ما حمله خواهیم کرد، با قدرت پاسخ خواهیم داد. به نابودی تمام زیرساخت‌های تروریستی آن‌ها در جنوب لبنان ادامه می‌دهیم، و امنیت را به شمال باز خواهیم گرداند. اگر به موقع و با قدرت اقدام نکرده بودیم، امروز این‌جا نبودیم».
نتانیاهو همچنین گفت که ایران به سلاح هسته‌ای دست نخواهد یافت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76073" target="_blank">📅 19:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LosybnwIWD7SmNK4xprcUN14bjDv6NmEz-kUB3o2n-zoQbFX2no_WTCYkSF4VMkVCKrl074ygwoNOKSUEJP3dhl4r2s0QfHAbm62ygUXqsNuH4Vd0cTyx1HUkVecdYSp0C8S2w2HumvWeew56webhxKUR0XONREMTURZ7dK5oVNDq1UOSkWEyy0JTkUC1JMeXeG9gyVU0ZHmr_rEFL_6TqCa6Z8tOum2uDnf6DuP5KLQUz7mBWbJNbpDFSNgQbKeFXRvlxXUpMAt74wisSlQekJbpyKaTodBdp2D7pcgIjUz-_eumNyjXoAFP_rmLVCcY-5UsW7Y9XpqO-MVe8WDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هشدار تخلیه فوری برای مناطقی از لبنان صادر کرده.
J74wabx
ارتش اسرائیل با صدور یک «هشدار فوری» از ساکنان جنوب لبنان، به‌ویژه در منطقه «زقوق المفدی» خواست خانه‌های خود را ترک کرده و به سمت شمال حرکت کنند.
آویخای ادرعی، سخنگوی عرب‌زبان ارتش اسرائیل، در شبکه اجتماعی ایکس نوشت: «در پی نقض توافق آتش‌بس از سوی گروه تروریستی حزب‌الله، ارتش اسرائیل ناگزیر است با قدرت اقدام کند. ارتش اسرائیل قصد آسیب رساندن به شما را ندارد.»
او همچنین هشدار داد: «هر فردی که در نزدیکی نیروهای حزب‌الله، تأسیسات آن یا تجهیزات و امکانات رزمی این گروه حضور داشته باشد، جان خود را به خطر می‌اندازد.»
این در حالیست که ایران امروز گفت عملیات جنگی علیه اسرائیل را متوقف کرده است اما هشدار داد اگر حمله به لبنان ادامه پیدا کند با شدتی بیشتر از قبل پاسخ خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76072" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/puk4m700tIVQgskTxrAtVVsx3ySTv3aGWSUrTCZLiS8d-a5AgtEXBjSc3faLvfToG1AHYqcJzvRSGqchFO60USAvqVG02fxlppNF4DBGTZAWCreybtBGRr5uGmuyJmmQENs27bbV19kQsTLm4h8O0QiIuv1HJUSkgmEzgnusEnMP-7gksATdvQ7m_KDM3Ew8sH3jRxiP-np04WNSlEtJPuvgl34xMlCVFaYQcjMfSE3rmLcdVwnIFbRgV6zwS8VT_-hBZ0UoXY_gtyr5fQDBoeeRqIEucfoNbU86iyK67OjZMemozDNuHH0Ewm-fUoJB0UMG3JIvCmRyLW2lqCzsWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranSaat25
(وطنه*)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76071" target="_blank">📅 18:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76070">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mK7YdSzm7IzXYciC98vdGFVNdrTCTP3oIB6f5ZrO09GNrKrf2EAvqjBP_OcOIGpmc28cHJhO-j6ReM-3gMqKbsu9MIuDmcbf-LwRxeJJ6oiG-fT6wMybZmFtSyqn3RC2WDc-X1EtF4Pad9JxwRSC6WA3PpqwfX02wiuoslpWGOUqzYHuvwo4VwChWz3uOG-9VOjSFjVqMh0nLvdljLglLr7dYos-xsrX69KtWqrz1TyPBEi60O32umteY8fWJRZoOFmGbCAyGt2kAd00ZAgybqQ8LbzE1DNhSWgSnnE9LbN_Ex-mqWyDk-bwuSQb6_TDCcfVn6ZDIQQI5BziO9C9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Atlansick
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76070" target="_blank">📅 18:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76069">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XaBYk8Cr5o2027Qb2Iz-e3iTn2XsTUFMnb-0mYhXg4d-4xiIfnzlAAf8Le2CreGcS-X8_x8trRGcgJw3QuOlM6pSTAixCfZ9Gd-KmucTxRJFcIY8yXR6NoLplxYYnefimpjsQYxtVJjlUW9fzgum3J4l5HfBXWnS4SThI7HiFGKiQbVvhhAprWkpeSOXqnfmyDs1XT8lvDAEdfsvLgE2qGuGARONvN-DV8PtZ7t1bw2KU8CDsFYBmkrYRDfqOkx_Dlr2EmWYkSJZAMvcLbG0SeRy2JTxp6SNL46p998SV7h0jNTn1kN_1VoUw4gz5e_x57Zyqzz1Om_f3FVvUqIrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی جمهوری اسلامی ایران، در پیامی که روز دوشنبه ۱۸ خرداد منتشر شد، هشدار داد در صورت تکرار اقدامات آمریکا و اسرائیل، منطقه با پیامدهای گسترده‌ای روبه‌رو خواهد شد.
ذوالقدر در این پیام نوشت: «تهدید معتبر را از جایی غیر از واشنگتن و تل‌آویو جست‌وجو کنید.» او افزود: «اگر ائتلاف شیطانی صهیونی-آمریکایی دیگر بار دست از پا خطا کند، منطقه برایش جهنم خواهد شد.»
دبیر شورای عالی امنیت ملی در بخش دیگری از این پیام مدعی شد که جمهوری اسلامی طی «چهل و هفت سال و صد روز مقاومت»، از میدان جنگ تا عرصه سیاست و دیپلماسی، معادلات امنیتی جهان را تغییر داده است.
این پیام پس از آن منتشر شد که قرارگاه مرکزی خاتم‌الانبیا اعلام کرد عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل پایان یافته است. رسانه‌های رسمی اسرائیل نیز از توقف حملات این کشور به ایران به درخواست دونالد ترامپ خبر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76069" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76068">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fzqsz_qR1ltcONVFJkR0LrDRCjlAkpnD-2TNm30-4FUmU-R89lkP2shqezyy85UFxjQl0aTHp7RYDfHhswOyn0iQJheihbnMnJ5e0-qmJWZGeIPXovbxtkwOQPUdIMhA34T9FN-Rp4Q98LGRXg9bpvKuRlsYtqRjO8qpgEYtYpg1-mPBoIEazYkR6IXlFVPsHtkB_DaYobczWnGE3-G3pO21NE3o44V56jq5LPXG89UzWTgP9cv4DwmzgYiXQzi0dqaDvrQyY5tQu-QrAQrGyY_flYaHK0mfHPThr0oMXQbcFtprqiEahdWCrONq1V7zqbWwDRpA9Boe9oUwKiIqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، اعلام کرد هرگونه حمله به شهرهای شمالی این کشور با حمله به ضاحیه در جنوب بیروت پاسخ داده خواهد شد و ارتش اسرائیل به عملیات خود در لبنان علیه سازمان «تروریستی» حزب‌الله ادامه خواهد داد.
او افزود: ما تهدیدات جمهوری اسلامی را کاملا رد می‌کنیم. هرگونه تلاش تهران برای پیوند دادن لبنان و ایران و حمله به اسرائیل، همان‌طور که یک‌شنبه اتفاق افتاد، با شدت زیادی پاسخ داده خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76068" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76066">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c3ab90b1c.mp4?token=auFxRQXmVeFPQsWoZINJsoCuqrozGc6X-bTFi4LcFaDnhE3dvyrAryVlLbf6T3NeW-xTPj4VVOEr-EV8t1X9CDjPW8bdiDuzdhh74y2centlDAC_h2FDkFo5J1oa-K8CpN94Blyuphl24_b7Q-MrcdTf9NEP0nl3AsD-Jfzd4C_WqmE02okSsgFUAHoa6QAtp7h0Rv_K6JSlirJsVmbnl3pHLyfUoKjgH4G6plu-FsjvUk166U_pjkhdPcg5qLE790bioMy0vSepAoyDanJaTbWkMQt71T28xoStAYqirybPF1T7Cw69sskTrAgEm2V-sJsI7xg0BdPdkwZ4s1vsyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c3ab90b1c.mp4?token=auFxRQXmVeFPQsWoZINJsoCuqrozGc6X-bTFi4LcFaDnhE3dvyrAryVlLbf6T3NeW-xTPj4VVOEr-EV8t1X9CDjPW8bdiDuzdhh74y2centlDAC_h2FDkFo5J1oa-K8CpN94Blyuphl24_b7Q-MrcdTf9NEP0nl3AsD-Jfzd4C_WqmE02okSsgFUAHoa6QAtp7h0Rv_K6JSlirJsVmbnl3pHLyfUoKjgH4G6plu-FsjvUk166U_pjkhdPcg5qLE790bioMy0vSepAoyDanJaTbWkMQt71T28xoStAYqirybPF1T7Cw69sskTrAgEm2V-sJsI7xg0BdPdkwZ4s1vsyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسراییل، روز دوشنبه ۱۸ خرداد، ویدیویی را از لحظه حمله به یک سامانه پدافندی جمهوری اسلامی منتشر کرد.
ارتش اسراییل گفته نابودی سامانه‌های پدافند هوایی ایران، آزادی عمل هوایی بیشتری برای عملیات‌های بعدی فراهم می‌کند و بخشی از تلاش این کشور برای مقابله با تهدیدهای جمهوری اسلامی به شمار می‌رود.
@
VahidHeadline
و در پستی دیگر ویدیوی دوم بالا رو درباره مجتمع پتروشیمی در ماهشهر منتشر کردند.
بدون هیچ شرحی درباره اقدام نظامی خودشون نسبت به اون مجتمع پتروشیمی
نه در متن پست نه در خود ویدیو
اگر قبلا تایید نکرده بودند که به اونجا حمله کردند این طور پست گذاشتن بیشتر شبیه به تهدید به نظر می‌رسید. شاید الان هم همینطور باشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76066" target="_blank">📅 18:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76065">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GnBK1F_mtJi9-CvhhBc9SNcvuaycQ8FS_49Qdn72F9hM1qq5b95FvqACYYySHaqTh0wt9etiMKW0p1RnpVPArjydVbylXj-induHayINPkIS21yO1jjU5W8lEDcajBHSBOs6_3SEaE_42hVT-rwfo63I9WQYR9hRqFyBd63skcOtgZaxqTlrdfZoczZxgFwVa_AZjEnuVfRdk2_etv_MtLBLaVtUaMMyNTX9uywj66Lm0qsnuur0WwCvhEQTdzm2pe6O8MMaiXCLET1s27MafcVheJ3I4FOBMHIiorfofcuZH8N2YlQGzsk5nCsqtLEqW98yMeT75iR-Dle0fEb8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت محمدباقر قالیباف:
"معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را بر هم زدیم.
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود."
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76065" target="_blank">📅 18:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkr3IYWWfgbfNJLCKx46QZQ6PbADwC9i-jMrCy_kueMqMc_CG7jqnvokdujWVSPiDASBHqSIXKRHIQyRySUrjbG55uY2TgmdVeNwDaL2vSr8FKRTveksmcfFvAQ703JNFmK5LMcupX7GkM71isr7mX_b4J78xVMk1gwOd66sog26Ha5OOyfoEQQNBnPvN0Lh3boZ2w8qnvxRR9PeWbtIc4xuz_TDOxdmvZJomvJghO5Ww7CMiqkoWNLOoeBEi8-ZSHe98SEeU8VHbkYXGdOQL-ScwN3DZeB4Dco1hKoIXc4j2WC0P5Z85z2u1Svc5BlWkQHB1rD4hTmQx-uujxOLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های دولتی لبنان گزارش دادند یک حمله هوایی اسرائیل روز دوشنبه ۱۸ خرداد یک خودرو را در شهر صور در جنوب لبنان هدف قرار داده است.
خبرگزاری ملی لبنان اعلام کرد: «یک حمله هوایی دشمن، خودرویی را با موشک در شهر صور و در نزدیکی ساختمان صلیب سرخ لبنان هدف قرار داد.» تاکنون جزئیاتی درباره تلفات احتمالی یا هویت سرنشینان این خودرو منتشر نشده است.
این حمله ساعتی پس از آن صورت گرفت که جمهوری اسلامی ایران و اسرائیل پس از ۱۶ ساعت درگیری نظامی اعلام کردند حمله به یکدیگر را متوقف می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76064" target="_blank">📅 18:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHkVvmjJZ941eXGiT8YbeV5ZC7DbyCWyb6_mlANOuSe5szmBFthOaUvQFvy6hrExuM7Z9vgfYYzuj3Lep1lVPYiB59PM8qCGhNBJqzFdgC0EX6LrsPTIKeem_vxw5sW6KWRXndwqx2NbVcPbXs64t3kBUf9J8WpSERRyhEQL3KyNVguQ90Pc3k4XDWXvDswS3TY3XdPex5sfTnAgIq1baa-TXeMAPovzVw4NQcGvZWtVYRxYx0qxa23EPuSNz6-sSNgNMLsEHaSS3PiLb7J68OpDu06Boj3eRs955ZUjPWGQxBPVnf4ndf9RQFo3gK3R-WOKHTGs2HJqUM2mvOKcqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس سازمان اورژانس ایران، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اعلام کرد در جریان حملات اسراییل به ایران، ۱۵ نفر مجروح شده‌اند و تاکنون هیچ موردی از جان‌باختن شهروندان گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76063" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAxljtLlzVKwGiP2a_ynOLhZryNRMaWbl16Rxd4C8_lJl_YgYAZE7C2ZpQHONkREyTVR4okqAvJ3OKksjy9fQj2YXNnh0M4cvTR5hmm3tmmtR--GhI3oteArn5T4nC_wgPWKGBB1asuKKp4fELm1YEoFPajPwv8TnNHmIrADpYbZxf0JGYq6dBaIqTwOV3uNUJYRXS4FFa1i3ziHLiwzPPc3YXOHTaYKZPWHPKrG72djfddkxa0_THA5Fgc5klzyqt79kf00a-1nLnfVP3dEnK7_tufdIK3mNYtzngSi8diDeoSTBqBTXD1L730v00b5Uh1qbp2G1sD7D4-IZcsWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایسنا عصر روز دوشنبه، ۱۸ خردادماه، به نقل از شرکت فرودگاه‌ها و ناوبری هوایی ایران خبر داد که «همه پروازهای فرودگاه‌های کشور تا اطلاع ثانوی لغو شد».
این اداره همچنین از تمام مسافران خواست تا «جهت حفظ نظم و پیشگیری از هرگونه سردرگمی، تا زمان اعلام وضعیت عادی از سوی مراجع ذی‌صلاح به فرودگاه‌ها مراجعه نکنند».
این خبر ساعتی پس از آن منتشر شده که قرارگاه مرکزی خاتم‌الانبیاء سپاه در آغاز بعدازظهر روز دوشنبه با انتشار بیانیه‌ای از توقف عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل خبر داد.
همزمان رئیس سازمان حج و زیارت خبر داده است که «با توجه به شرایط پروازهای بازگشت حجاج احتمال تأخیر در برخی پروازها حتی تا ۷۲ ساعت وجود دارد».
او اضافه کرد: «برای فردا (سه‌شنبه ۱۹ خرداد) ۱۰ پرواز پیش‌بینی شده که امیدواریم بخش عمده آن‌ها انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76062" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXJXWTBpoYFB9VyL50YGtquUDl_bj5j6JeFBqZCJnnvFCreGjUG3bNM1YOEj3E4KNKEpKJvijNLIWqVMoomI62JYlFRYpJ5AiIjbIk3tQ0mrvdTLlbJd427Vd57iyfOr_4LKsorTRmclYaEVhetEyz-pyBSt226nZVhCARL7MSLqf9a66T2PQJlSQQ3oO523uSofCIYl6vRwksAYwZZqFDFKLRNuu2eDeaR9lvw9m974vqDMItms4aAihh9Fq-A36KqGzQgx1GscCLET4HKjU0zSLWaL-Qqzppu4fWctXjentBrrAtsh9_ZJrGAsXfyvPkUUHFa5JNzeAclW2egw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا، روز دوشنبه ۱۸ خرداد اعلام کرد که اتحادیه اروپا به‌دلیل تهدید آزادی تردد دریایی توسط جمهوری اسلامی، تحریم‌هایی را علیه شماری از افراد و نهادهای ایرانی اعمال کرده است.
کالاس این اظهارات را در جمع خبرنگاران و در حاشیه نشست وزیران دفاع اتحادیه اروپا در قبرس مطرح کرد.
هنوز جزئیات بیشتری درباره این تحریم‌ها ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76061" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b31564948.mp4?token=E2TQUdogCRrnxCw2nnzS7SSSluADiP_nQzRRB9jHJBUekWP7TLEoOaL0CtD83FtQWSfrRHYppqWx0rkTSNscGmg7zFLMoShvtLdHXYGTbR-Bhw_B8DJT2cAfO9aI5Yi49m72WMxad6u0ExbyzjOHHc3pbAIsPRsdoj7kFTYR9xDDv7ZYray4JeJd5P0IK2OfFcHJj-CJlBiigJ8UaeIwu-JIIEY7arwXRRlzxBg62rtaN5jDpqClJZv01JrSFRX79RZOphVlxtDFxBmEk_6cupju798EG7ObhkJrsBXLAEOnFv5ok3OlSsSl3aS1LaKVz7l7EA8dMdyuHH9g5A7cnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b31564948.mp4?token=E2TQUdogCRrnxCw2nnzS7SSSluADiP_nQzRRB9jHJBUekWP7TLEoOaL0CtD83FtQWSfrRHYppqWx0rkTSNscGmg7zFLMoShvtLdHXYGTbR-Bhw_B8DJT2cAfO9aI5Yi49m72WMxad6u0ExbyzjOHHc3pbAIsPRsdoj7kFTYR9xDDv7ZYray4JeJd5P0IK2OfFcHJj-CJlBiigJ8UaeIwu-JIIEY7arwXRRlzxBg62rtaN5jDpqClJZv01JrSFRX79RZOphVlxtDFxBmEk_6cupju798EG7ObhkJrsBXLAEOnFv5ok3OlSsSl3aS1LaKVz7l7EA8dMdyuHH9g5A7cnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی از لحظه حمله‌ الهه و شهربانو منصوریان به اتاق ریاست فدراسیون ووشو و شکستن دوربین مداربسته منتشر شده است.
طی سال‌های اخیر
خواهران منصوریان
بارها به ساختمان فدراسیون یا کمپ تیم‌های ملی حمله کرده یا با مدیران درگیر شده‌اند، اما همواره از حمایت نهادهای حکومتی برخوردار بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/76060" target="_blank">📅 15:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf21K7092vzdDPbQFPg2MoMUoAeSWUmWd1_gwHuFkSuwss8uw1aMuIQmtK3Rgw12ZOMVXd3OEHN8WOXD1Ynv85cUd441BedAL-TkakTKKQgl8DGZNQCl1RxvTMwfkblE2myGS8dEH8A4tFu8Zn8aRu7plhQmFcDa0hvLZ42148kDWRotQux1n0HUVZ9Y4y6wFVVG53hVKvD1HNbdB9xDOz4GJdSVGUYRNNesoce2rWOGZUg8-5ss-CPhWELHra5ibbKiO8BnalIqwpw2CDE5u27c7vvsVYKltRnToP8GGvfERGPA87DtIz3p1PIW5PE23Gztf9A0jWSXNAe-F66Arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سپاه پاسداران از «توقف عملیات» علیه اسرائیل خبر داد
♦️
قرارگاه مرکزی خاتم‌الانبیا سپاه پاسداران، روز دوشنبه ۱۸ خرداد ماه با اعلام آنکه نیروهای مسلح جمهوری اسلامی ایران در واکنش به حملات اسرائیل به منطقه ضاحیه و جنوب لبنان «پاسخی دردناک» به این کشور داده‌اند، از «توقف عملیات» نظامی خبر داد.
بر اساس بیانیه قرارگاه خاتم‌الانبیا، پرتاب موشک به اسرائیل «در راستای حمایت از مردم مظلوم لبنان» توصیف شده است.
در این بیانیه آمده است که این پاسخ برای اسرائیل و حامیانش باید «درس عبرت» باشد.
قرارگاه خاتم‌الانبیا همچنین اعلام کرد «توقف عملیات نیروهای مسلح» در دستور کار قرار گرفته است.
با این حال، در این بیانیه هشدار داده شده که در صورت ادامه حملات و اقدامات اسرائیل، به‌ویژه در جنوب لبنان، جمهوری اسلامی ایران «اقدامات بسیار شدیدتر و کوبنده‌تر از قبل» انجام خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/76059" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76057">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PeTxH4asAwxzWmEb0KYtfjSJ7LgWCMthbEu04YaDCfit3vy-RWy7AcWyOYHMDl1WOXmpSEDO9mUIfq6gv25qgLBmxr__LpdJHNBPsnT4W_Kx2lmYJWufqv-VoUK8qNF7UNtO8wDPGO79waGeb46gtCX7I0p62c6R7ji1unSimMZJ1lZ60tRHNTmvum4Q4_sQ3Y_NKf1Jp99hTwsHAeFCCAPu7iic4TrO6jL6Yqu3MTStkqCn9H44hIl7WvmBmhiZzbKUuX1qv8sKKj8K6K1ALnWtFQ5TPDDUu1x9gXaEkTNKPpx6HONo0FiLcsyufXVjfjVbw3jsTp8AsJ9OV5oesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tvBPqg49BwlM5Z41VWp3FDYKy_f4PYy6HkWxc9-Nvwcxbb6nftTdidJBnADMvIxh26Bn3dYjNFTruEK5a9n9ULVQyHfTGm6jlmgvmfnt9tDs52h4FHr_CNSlvYqtotxX8IRpi_y4QFFEhqR2oADT54vf3YH4eWjyts9SgKcZjmPZSiyjS56BDdbcjnR9B5NDp4TFlFNp85eX-hYmcAIOXjwe-SQKPkmSFcITDteGSihEf-btTX7ME4UtyL7qLN8P21i7KTZSyA53nK2e3KM8-0zz0YRuUbF-ZRm7yBIawPt-Ssi-lFOm4q8PuYrkG3Ss-wUb23M4K8HoQhcTZB4kmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «تیراندازی» را متوقف کنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دو طرف، اسرائیل و ایران، به دنبال برقراری فوری آتش‌بس هستند! مذاکرات نهایی درباره «صلح» در جریان است، مگر آنکه نادانی یا حماقت مانع آن شود. محاصره تا زمانی که «توافق نهایی» حاصل شود، همچنان برقرار خواهد ماند و با تمام قدرت و اثر کامل اجرا خواهد شد. امور باید به‌سرعت پیش برود. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/76057" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMiBHXuOni0h5ePpOtvSP5C_K_KH6jpPToyi9TBjY19J9X4DWGQ1Q-pSU-BJiZXq2xiOxmmLwO17YrT0uYoe2WbznHbWIyVdiiLAhfVxTtPjRCdS6y8V5KHeu_TUwSNNQtjUIzsXAo3J0EMtQykwqukldQMMSF7rZb_8E6sI1Y4GMGcpFbMcTjicwMgBm4CWSavNQpzNjmPFSkA2PLbC-pL-f_KIBxmlcir6qwHG2ErHOSQilMj6jm43bjEyvoQP7Txm66DZ9Uq7Tcgw_F_1IpErI1ReTgCJ_L0fEGXZVZ4XjuZMnxfw-XlHRZridPi_FoCYdPkON5GVw4jx3C9j_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی گزارش داده‌اند که نیروی هوایی اسرائیل همچنان حملات خود را در نقاطی از کشور ادامه می‌دهد.
بر اساس این گزارش‌ها، فرودگاه شیراز در جنوب کشور نیز در میان اهداف حملات اخیر قرار داشته است.
هنوز جزئیات دقیقی درباره میزان خسارت، وضعیت پروازها و تلفات احتمالی منتشر نشده است.
@
VahidHeadline
در خبری دیگر:
خبرگزاری مهر وابسته به سازمان تبلیغات اسلامی نوشته:
"پهپاد متخاصم دشمن آمریکا_صهیونیستی توسط پدافند هوایی در آسمان تهران هدف قرار گرفت و منهدم شد./ مهر"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 510K · <a href="https://t.me/VahidOnline/76056" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-h8toECyVXn4mwM4ren5uUVtA1gQOOxF9F7ek0l8dkmmOXdLHmfUa5iJS80Tq02qeQMPXbr3n8tBQa7BFvJPkO6AWMxs-1ORBj3_-xFCCGmus2_v1MnA5GV5l7Q5aUiQJlNVn2ECRDKvuswuQTaOZ5Y6lsl5qm3YmHjs7L-lLnAVS9KFD3l6aONCMaqy9wihO9NvLZlJFrUjSzeDyHvBFN1CtrUKrX8cQwm3ld1qkEzDp_vBd2j7p9g6crkyjgHh11s1_oE_aYj1yZARrLwEfVJXnri-5XeyOeGtLgH8bxTNqTZUErDCXNd1cHGA71cNGwK-xNhfQfQi8VFXuKWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای گفت در پاسخ به حمله اسرائیل به صنایع پتروشیمی ایران به صنایع پتروشیمی حیفا حمله موشکی کرده است.
بنابر این بیانیه، هدف قرار دادن اهداف غیرنظامی و تاسیسات نفتی «بازی خطرناکی» است که زیرساخت‌های انرژِی منطقه را تهدید می‌کند.
پتروشیمی کارون ماهشهر که در بیانیه سپاه نامش برده نشد، تاسیساتی است که هدف حمله اسرائیل قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 504K · <a href="https://t.me/VahidOnline/76055" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پیام‌های دریافتی:
‌
وحید تهران صدای مهیب وحشتناک
ساعات 11:33 دقیقه جنوب تهرانسر صدای انفجار اومد
سلام ساعت ۱۱:۳۰ رباط کریم صدای انفجار
تهران صدا و موج شدید انفجار ۱۱:۳۲
همین الان صدای تک انفجار غرب تهران
زدن تهران صدا واضح انفجار
ساعت ۱۱:۳۳: صدای یک انفجار شنیده شد - تهران آزادی
صداش خیلی زیاد نبود حوالی غرب باید باشه احتمالا
اسلامشهر صدای انفجار ساعت ۱۱:۳۲
تهران الان صدای انفجار اومد
تهران غرب ۱۱:۳۳ تک انفجار بزرگ
سلام وحید جان.۱۱:۳۳ تهران صدا انفجار اومد.من غربم صدا دور بود ازم
۱۱:۳۳ دقیقه صدای انفجار ملارد فکر کنم زدن
ما سمت مهرآبادیم ساعت ۱۱:۳۲ صدای انفجار اومد
صدای انفجار در اسلامشهر ساعت ۱۱:۳۴
وحید ما غربیم 11.33 صدا انفجار امد
یه صدای تک انفجاری اومد الان انگار سمت یافت اباد
بهشت‌زهرام. از نزدیک اینجا صدای انفجار اومد. ساعت یازده‌و‌سی‌و‌دو.
همین الان اسلامشهر تهران ۲ تا صدای انفجار
سلام وحید جان، صدای انفجار در فردیس
غزب تهران سمت پونک همین الان صدای انفجار
تهران اطراف اتوبان نواب صدای انفجار
شهرک غرب
صدای مهیب انفجار از دور اومد
وحید قلعه حسن خان دو تا صدا انفجار قوی
سلام باقرشهر کهریزیک صدای انفجار 11:33
وحید داداش سمت دریاچه ۳ تا انفجار ولی دور بود
11:32
گرمدره صدای بمی داشت تک صدا بود ولی دلم یجوری شد
سلام وحید جان من سمت مهرشهر هستم ساعت 11:31
صدای انفجار خیلی وحشتناکی اومد
از شرق کرج یا غرب تهران
ساعت ۱۱:۳۳ سمت ملارد صدای انفجار وحشتناک اومد
سلام ۱۱:۳۳ صدای انفجار اومد از جنوب تهران از دور بود
تهران سمت شریعتی ساعت۱۱:۳۲ صدای خیلی دور انفجار اومد
از ملارد ساعت ۱۱:۳۳ یدونه صدا اومد
وحید اسلامشهر دوتا صدای خیلی وحشتناک اومد
ساعت ۱۱:۳۴ اسلامشهر ۲ انفجار با فاصله یک دقیقه
ما سمت چهارراه ولیعصریم دقیقا ۱۱:۳۳ دای انفجار از دور اومد
سلام ما عظیمیه کرج ساعت 11:33 صدا شنیدیم، دور بود
سلام من نزدیک مهرآبادم یدونه صدا اومد بنظرم بلند بود اما خیلی نزدیک نبود
بازم هم مهرشهر کرج صدای یک انفجار
ساعت ۱۱:۳۵
درود گلشهر صدای انفجار اومد همین حالا
ما تو یافت ابادیم صدایی که اومد نسبتا دور بود ولی خیلی مهیب بود
سلام وحید جان من سمت شمال تهرانم ۱۱:۳۳ دقیقه صدای انفجار دور ولی سنگین اومد
آپدیت:
پیام‌های زیادی درباره فعالیت پدافند در مناطق مختلف تهران دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 513K · <a href="https://t.me/VahidOnline/76054" target="_blank">📅 11:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKzBdURTKuLwI0Hy_YOfkOOOc7CknKcfjGV_1NbeymxEofPs3nVUElk5evN5ESztrZ_bLGlB4bNGL0Z25juxsVCKpW7vekzdbMWBR3jZU5Id3BAtxHrXpOP_5W1dEXqDwkyuHwNIRDIAmlKSIMhwgXDikh0ulEDzmB8jTUTgB1jLDtiXQlN_ySMAx5VSN-CDyiKnaQflFF_57wEJKprVZm16t1YAusQNFXotCQfoA05LYi97PKfzFy3oCoY_Yi8eoWeZyzz2u445RYXQhFoAkfGjQi8rvY-M6mJhz8bmyY6qpyXE6yHWkJuEZeRbY0dFfjwtToviy72wJOMfbY5rQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ایلان ماسک: "تنگه هرمز به نام اهورا مزدا از آیین زرتشت نامگذاری شده است."
elonmusk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/76053" target="_blank">📅 11:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76052">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOBe4gx7ghLCFad-o7396r48TiT08IPjCz_njorYOSp8AfaMqsRVWM7T50TZ0UwDEutJAxDLOYDafMsPpL-ivFuknZ--1fy3gwFf1BiPVbusO3IR8zjiwLp9xeAX8cj_RDCIv2S9VHBsUyvNvDjM6nmKH0befetm2nJmaXa_1p3sJTpRU_U1rUvz6adcI8KKsp5h1yX5kPhiCfs77YKW4ynO5PystzQXo1XYPd4pLFH_vDFxgy2EcvtMm68myiL2iN0lEb00itVEiYmSLzxVWFP2oNgtb_-p97pyibyOtnl6xstwIciPCo50KRovyETAEIC9pYjn1lzEuznF4Ut9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نخستین کنفرانس خبری خود پس از آغاز حملات ایران به اسراییل گفت که اتفاقات ساعات‌ گذشته، به بی‌اعتمادی موجود میان تهران و واشنگتن دامن خواهد زد.
بقایی در نشست خبری خود گفت تبادل پیام میان ایران و آمریکا تاکنون در فضایی لبریز از بی‌اعتمادی انجام شده و به گفته او، آتش‌بس نیز «به طور مستمر و مکرر» از سوی طرف مقابل نقض شده است. او تاکید کرد جمهوری اسلامی هر زمان که لازم بداند برای دفاع از «امنیت کشور» اقدام خواهد کرد.
سخنگوی وزارت امور خارجه همچنین آمریکا را مسوول تحولات اخیر منطقه دانست و گفت اسراییل بدون هماهنگی با واشنگتن اقدامی انجام نمی‌دهد.
به گفته او، وزارت خارجه آمریکا حمایت از اسراییل را دلیل اصلی جنگ علیه ایران دانسته و جمهوری اسلامی از همکاری و هماهنگی کامل فرماندهی مرکزی ارتش آمریکا، سنتکام، با اسراییل در حوزه‌های دفاعی و تهاجمی اطلاع دارد.
بقایی با اشاره به تفاهم آتش‌بس ۱۹ فروردین، آمریکا را مسوول هرگونه نقض آن دانست و گفت پیامدهای تشدید تنش در منطقه متوجه واشنگتن خواهد بود.
او همچنین از «رافائل گروسی»، مدیرکل آژانس بین‌المللی انرژی اتمی، انتقاد کرد و گفت در صورت تصویب قطعنامه‌ای علیه ایران در شورای حکام آژانس، تهران «پاسخ مناسب» خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/76052" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76051">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/025351cf82.mp4?token=WkekflisnLiPnKmRO1XVHG8Kb1Y4LL0VuihEbAMqgI3e_HDqp2PXv1jiYbThdF6Uh10ZRK4DsKVuUDrtv5sxiL_5dQbMzp0ydLVGpADLf5m2JN1GlaDQXb-kryyR06qKWry9CNu-CQiUUZX-YiVmtaPU6A4Ss3BDvAobHZMG-xuA-JvIq1UWHonJQLqMDsAwNNtSTy9xK6CJ17RemvuTTbDiLraL8_SCRhRyKEEsx_paJ2dvO7xeJjZ8sP2cI9qjORDflqu4CmeE8OCdWlFv4oh-yuFnbmBJgxibstRekyFrjlceIcBVpV4mOx1-QFd1yRifxnJZbFKgM77cQ8Sh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/025351cf82.mp4?token=WkekflisnLiPnKmRO1XVHG8Kb1Y4LL0VuihEbAMqgI3e_HDqp2PXv1jiYbThdF6Uh10ZRK4DsKVuUDrtv5sxiL_5dQbMzp0ydLVGpADLf5m2JN1GlaDQXb-kryyR06qKWry9CNu-CQiUUZX-YiVmtaPU6A4Ss3BDvAobHZMG-xuA-JvIq1UWHonJQLqMDsAwNNtSTy9xK6CJ17RemvuTTbDiLraL8_SCRhRyKEEsx_paJ2dvO7xeJjZ8sP2cI9qjORDflqu4CmeE8OCdWlFv4oh-yuFnbmBJgxibstRekyFrjlceIcBVpV4mOx1-QFd1yRifxnJZbFKgM77cQ8Sh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت ارتش اسرائیل با انتشار ویدیوی بالا نوشت: "در دوره اخیر، سامانه‌های پدافندی در چندین منطقه مختلف در ایران مستقر شده بودند، ... این حمله منجر به انهدام این سامانه‌ها شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76051" target="_blank">📅 11:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76050">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3Eha1MlObpKS5OagZpM1KRj8n7aWCsI9qkDbLEAQR0m98lUPy210vP-UC7paeIptMVJBHZwLSuNHPqQLRJo9m83ftvxh0Yu_5pr0ea9EbyVJChKYU_2YfOgE6lSrsYefvoI7i-WuQ56pSQj03tiTyR9iP71Px_kSzi2zCo8PNK-hl5iNlrZcxhJXFE8zd4o9mKb9xJ-3CbyOeehR9ZlPJqJtuLLP9efF0tNs_DHFNBPewW9uhWCylLOyx4WKApR64zFTLFyC4ednxx_5gWOyY9utpdd0ikmSPrumuscy9emkEGoLolu5KXi6DaSaW6XJ2KufeJHOCePcwE6_MK8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه قطر اعلام کرد «محمد بن عبدالرحمن آل ثانی»، نخست وزیر و وزیر امور خارجه این کشور، در تماس تلفنی با «عباس عراقچی»، وزیر امور خارجه جمهوری اسلامی، درباره تلاش‌های میانجیگرانه میان ایالات متحده و ایران و همچنین تحولات لبنان گفت‌وگو کرده است.
بر اساس بیانیه وزارت امور خارجه قطر، نخست وزیر این کشور در این تماس بر حمایت دوحه از تلاش‌ها برای مهار تنش‌ها و دستیابی به توافقی جامع که به تقویت امنیت و صلح در منطقه کمک کند، تاکید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/76050" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FuKtJDcK4_mPZfH6XLi3GVjgPEsqeDSjqwVTSaRmvCMXz0lu7b650_nXf8uSC2uOLiBMU8Ak9OxdY4OPiW1OKoxIl9QbDApqPFL5FJvmDtPSo2X_q8u1YJidzqd84X3eX0V8dogm9DM-hMU_ttHDP5tqLWs1JNMLE2ONusPc2WGOd_0mMH_8TZoAVZMsQ2pvIIB-p0gIv0IJHG75A1Eejh8GiLY1xid3WdbQT2MGnVs5_7rK3JHNSD8k79Qr3wmc26ma29WpSf9LlmT5_JGZNBFmgOLzEuKfYZsqrwEAwSBfSymxn6291m-VGHP_i_uxxbJkybYKhGvqMc3RVl13KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TpT_-kEu6pivCGlWa1SpsGKZzMTfhfPFDm8tdsQML18eOWBB0DcySipW2bCokyFsJpJXC6BOCH14AEvQeNo0dpZIQLxR5eSvyhdljZ2jdP6i0VAJsFLdZrE4Iohf1N5-h3WHvtQBCOZHEDRHp65axApp1XsOvjhDiH4WOTGpJ0HNLbt0F8Uubj7CK1ZKBKR8oA0NuuzOzi5g5HnYjEp9DoAcgIG3CFvobo563ULTQZ4UmVR60lEsiAz_OtdzgUjBmpk11aTVAVX6eithtaTMvDqvlZ7jhmb86P7TpInIIbnJ38NWb0_p02VCAQh-ORtldoyMrsT1VoJwwzWwlOP4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qk4s88oo_0n2C1TcUDkNGTV9P-uOcSd8CKUcbz8KqHeJLNZ4xeHbcrNXzwK76HRk_yuZ8AzHEDOabEjCRZvuUaM00HTP8miX32UxttS46rhW8Yz_42Jg-KTtkMgdMX5XdoOfOBhVz6QPi6puGzgOpLTGldsvDruXO_S1mQoVR-7cvAG8_-hfvNGZS5IWuUCtoXI3GVoVdQK9r03SidfoyMMCquiX8J2rwFvCjTQ4CUZDxRPEaNESGPuK1oydflFhcDK1nxp6eG9XVY3mCxOJMEbhEs0rJIt9DVwQSEogr7hRDTjOO8af4c1V1MYO2YJFrFglCAvaXkkmoe2zV91g-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/551c6649bd.mp4?token=Rhc3YB376RqvUe2eK6u7VaVlFheCWBg68ofFM4_sLWD-gWQQpnK7_F1s7k8djdFLRJObS9WhF4WmtbTB5nwIvWkNWpMO_Ro35ii_EboO1ajVRf0bDld6PY0c8tSnCLcuW50DoBeSkhefpNKOc-_c-Avnp1iL94qmQrmgLGMx7wXCtzOu97C94asM9cyWfFnxhe68Mluuy9ysqQkmSjJN9ttzWFlPHpsGu14qnRoAmLXZUW4pZY7gAgXECFdK3oSpAxWA2WyDmdZU7-gWUl9mSuB7IpLUnZOXiHcgyu2VPt9qnzQwbzZV6cgTXVxGW3G0shDrPWXYuA_X7cse9emWxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/551c6649bd.mp4?token=Rhc3YB376RqvUe2eK6u7VaVlFheCWBg68ofFM4_sLWD-gWQQpnK7_F1s7k8djdFLRJObS9WhF4WmtbTB5nwIvWkNWpMO_Ro35ii_EboO1ajVRf0bDld6PY0c8tSnCLcuW50DoBeSkhefpNKOc-_c-Avnp1iL94qmQrmgLGMx7wXCtzOu97C94asM9cyWfFnxhe68Mluuy9ysqQkmSjJN9ttzWFlPHpsGu14qnRoAmLXZUW4pZY7gAgXECFdK3oSpAxWA2WyDmdZU7-gWUl9mSuB7IpLUnZOXiHcgyu2VPt9qnzQwbzZV6cgTXVxGW3G0shDrPWXYuA_X7cse9emWxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
ما کاشان هستیم
اینجا قشنگ صدای موشک رو حس کردیم که داره رد می‌شه
همین الان ساعت ۱۰ و ۱ دقیقه.
از خمین همین الان موشک زدن
شلیک موشک از ابهر ساعت ۱۰
خمین ۹.۵۷
وحید طرفای ابهر خرمدره ازناب زنجان موشک زدن ساعت ۱۰.۰۲
سلام شلیک موشک از استان مرکزی
وحید جان سلام ساعت ۹.۵۸ دقیقه یه موشک از ابهر زدن
سلام از کاشان هم همین الان موشک زدن
شلیک موشک از زنجان ده صبح
سلام از خوانسار صدای موشک اومد، رد موشک هم توی آسمون هست.
همین الان از زنجان دو تا موشک بلند شد
هم‌زمان پست ارتش اسرائیل:
ارتش اسرائیل شناسایی کرده است که مدتی پیش موشک‌هایی از ایران به سمت حریم کشور اسرائیل شلیک شده‌اند.
سامانه‌های پدافندی در حال رهگیری این تهدید هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/76046" target="_blank">📅 10:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76045">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e62b7f335.mp4?token=Zh5QDsk2lb7Q_Bndh_l6qCsdv5iktAP4Esa7HFL96KmxQaeBgEpwMXF0yM-x7CIEpOn5zlayHWOnkxTo1B4EBpwKduvPwueKzFZlERzt9Sudeck9dhy2IvjnxLih3PNZfHSMpZPJA1jbTU3ZJlRYiO6uou1jb2mpdxN_2pOAvTygG7buhS0o2fgYMuKOTUdODwJZsEiHskDB3TZB9HPHLhf-mq7_l6gmSJBgZMocEsEZTsQbIJEwYBDwitFB1Xl2hhc6JFFBsBxw97IvlwnsZdStWI3ps9UHKtab-qb-64wqKmBMg9NSV_QPzWgmQ8oDDyZacO0ArlrD8nlvFkLDJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e62b7f335.mp4?token=Zh5QDsk2lb7Q_Bndh_l6qCsdv5iktAP4Esa7HFL96KmxQaeBgEpwMXF0yM-x7CIEpOn5zlayHWOnkxTo1B4EBpwKduvPwueKzFZlERzt9Sudeck9dhy2IvjnxLih3PNZfHSMpZPJA1jbTU3ZJlRYiO6uou1jb2mpdxN_2pOAvTygG7buhS0o2fgYMuKOTUdODwJZsEiHskDB3TZB9HPHLhf-mq7_l6gmSJBgZMocEsEZTsQbIJEwYBDwitFB1Xl2hhc6JFFBsBxw97IvlwnsZdStWI3ps9UHKtab-qb-64wqKmBMg9NSV_QPzWgmQ8oDDyZacO0ArlrD8nlvFkLDJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اعلام خبر حمله موشکی به اسرائیل در تجمع هواداران گروه‌های مسلح شیعه در تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 475K · <a href="https://t.me/VahidOnline/76045" target="_blank">📅 09:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dT8xUQ6-A0FUjl5hORKu4Sx8L_93CYoEEJAJ7tB-6uyuEHSLmNkD3fQO5otnDjlik9M1t9KF9R9O9vqwCe-8DaylpjiX2fzTnW_5egAFkITw9g5IwPm4OftQWCXUtsBtT9lQ2LFF0k8Ti2WRiAdSKku7wnamJCCwCWLE9bXJmmlTo8Yoqfjy0SQedk8AfgSEHee7D6w35YWYLgczJSp4cTBN5cnuZArYDU23FfNf_B8P6LttEmj6wPIa1yRxMPfY6Ym1Q6GSyJOVRRR_TMxtglI8_r4W0Zn3oay8Sng27vs7_7VBTuNR1AtNnNO5BKSClasCRQHkMD8MNqZgQJdS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که تمامی موشک‌های پرتاب‌شده از سوی جمهوری اسلامی در صبح دوشنبه به سوی اسرائیل رهگیری شدند.
ارتش اسرائیل افزود که پرتابه‌ای که به یک زمین باز در کرانه باختری اصابت کرد، احتمالاً یک قطعه بزرگ باقی‌مانده پس از عملیات رهگیری بوده است.
در همین حال، پس از آنکه هشدار اولیه در اورشلیم درباره حمله موشکی جمهوری اسلامی صادر شده بود، برای این منطقه وضعیت پایان هشدار اعلام شد، زیرا موشک جمهوری اسلامی موفق به رسیدن به خاک اسرائیل نشد.
@
VahidHeadline
به گفته نیروهای امدادی اسرائیل، اصابت یک قطعه از موشک‌های شلیک شده از ایران، به چند خانه در یکی از شهرک‌های کرانه باختری آسیب وارد کرد.
در این حادثه مجروحیت گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/76044" target="_blank">📅 09:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e89e6ed06.mov?token=vMS_F_T1VOXXCcmZzoTaJ4x-uajDI5eYUX4DFLQhneNiYabwa6Y1-TB4Z68z6JrHfIuSNezI1cYPvm84p9-Z9Ttudsuul_o-zU2yrrmuJ_qAkNZXxx7pjFfaECQJVRD2V2c6ZZpUskkAnrKEvZ-iYAOOTazJ-2KaCo_MAW6yfZC_cAYQnL9Oi9HbnT2q-Un5cGpcvq5qMhrPv7YenGySMMar2xKOvloSNJx1VZ4XbEajttVyuolyPqfoqHy7vxn_Knua6IcVCzByTdfhij2THB4BdWw0G8c6cZcKXldWROAMW2vDfMoxU0H_7DSNpE0k6KHCeNIK_p289lx1zibo7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e89e6ed06.mov?token=vMS_F_T1VOXXCcmZzoTaJ4x-uajDI5eYUX4DFLQhneNiYabwa6Y1-TB4Z68z6JrHfIuSNezI1cYPvm84p9-Z9Ttudsuul_o-zU2yrrmuJ_qAkNZXxx7pjFfaECQJVRD2V2c6ZZpUskkAnrKEvZ-iYAOOTazJ-2KaCo_MAW6yfZC_cAYQnL9Oi9HbnT2q-Un5cGpcvq5qMhrPv7YenGySMMar2xKOvloSNJx1VZ4XbEajttVyuolyPqfoqHy7vxn_Knua6IcVCzByTdfhij2THB4BdWw0G8c6cZcKXldWROAMW2vDfMoxU0H_7DSNpE0k6KHCeNIK_p289lx1zibo7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@
iliaen
ارتش اسرائیل حمله به سایت‌های پتروشیمی در جنوب غرب ایران را تایید کرد
به دنبال گزارش خبرگزاری فارس مبنی بر حمله به مجموعه پتروشیمی کارون در ماهشهر که خساراتی به دنبال داشته، ارتش اسرائیل حمله به سایت‌های پتروشیمی در جنوب غرب ایران را تایید کرد و گفت به اهداف متعددی در مجموعه پتروشیمی ماهشهر حمله کرده و جزئیات مربوط به این حمله را به زودی ارایه خواهد داد.
ارتش اسرائیل پیش‌تر گفته بود که مواضع حکومت ایران را در غرب و مرکز ایران هدف گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/76043" target="_blank">📅 08:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac9a29e4c7.mp4?token=fZ6Xq_mpDUbzDnwP-DIpc8nauDddk2NVwE4jvLBYJPmgKXDYeSkh2wXutMq9UDE6uEkKnwxHH9oLc8kPFhwjLvXy1ceGBSIED-nbrXPFjXkqj9wXXoTpxpKljMcBBcTPvaEQ7LQDODdyGP33xQfXsU7BGKYjLi3fR_2gtiddR13voztG7nXbZEF7ckk4sATHjTnqspoY6OUUq8tAm7wiHyr9sahBfZ_qBOlvGKxLBPTWLUaUZJFf5MHSSSJlvMr0xmd5B2PAuqAu9O8JSKvKxnhwJaRQFpLGoXJqBk8mYqK_Tij0w23w4a4t4FHMiKN8PZeCTq5SLcySNO1dM7_iWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac9a29e4c7.mp4?token=fZ6Xq_mpDUbzDnwP-DIpc8nauDddk2NVwE4jvLBYJPmgKXDYeSkh2wXutMq9UDE6uEkKnwxHH9oLc8kPFhwjLvXy1ceGBSIED-nbrXPFjXkqj9wXXoTpxpKljMcBBcTPvaEQ7LQDODdyGP33xQfXsU7BGKYjLi3fR_2gtiddR13voztG7nXbZEF7ckk4sATHjTnqspoY6OUUq8tAm7wiHyr9sahBfZ_qBOlvGKxLBPTWLUaUZJFf5MHSSSJlvMr0xmd5B2PAuqAu9O8JSKvKxnhwJaRQFpLGoXJqBk8mYqK_Tij0w23w4a4t4FHMiKN8PZeCTq5SLcySNO1dM7_iWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابت موشک به شهرک یهودی‌نشین ایتامار نزدیک شهر نابلوس و در بخش شمالی کرانه باختری رود اردن
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/76042" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URNLj_q49X2HCz_HG66b7OT4JY5w_jsX5NtyqcJovyWSS9XLLNgOhprltD0-jZ8AhF4xAtfojm-Blanflpqw6kP_xYJ4A9t8oNsX8julX6f5CmKAOTyQKyFSYtqiCq82tX9eo7YwiVLCPy-aq7lf7ko7HecMq0EQQr59IIq632TPqw3dKk5Chpzt80gUIri53YiYcV4zvHk189klaoYrkdWxQwXsP_8mt87vymhYtb-tbGVEFvptCwQhmLrGOtTesKj90oJT5pgl5NmzIpsbHAjN2qmrTAC1paa2Q3N4C5fLUArCgrPGFUyUSwY4TQf09wTM6NMEDh6GCSc8KTl0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بامداد دوشنبه از رصد موشک‌های پرتاب شده از سوی ایران به سمت اسرائیل خبر داد و اعلام کرد: سامانه‌های پدافندی در حال رهگیری این تهدید هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/76041" target="_blank">📅 08:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76040">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پیام‌های دریافتی در پی گزارش‌ها از شنیده شدن صدای انفجار در ماهشهر:
وحید پتروشیمی کارون تو ماهشهر زدن
آقا وحید سلام پتروشیمی کارون منطقه ویژه ماهشهر زدن دستور دادن کارگران و پرسنل برگردن خونه هاشون
سلام ماهشهر پتروشیمی کارون ساعت ۷:۳۰ یک انفجار رخ داد
وحید جان منطقه ویژه ماهشهر صدای وحشتناکی اومد. میگن شرکت کارون رو زده
آپدیت:
پیام دریافتی: کانال ماهشهر هم اعلام کرد
پتروشیمی کارون رو زده
اما صدای انفجار مثل انفجارهای قبل نبود
همه نشنیدن
معلوم نیست با چی زده این بار
🔄
آپدیت:
خبرگزاری فارس، نزدیک به سپاه: " تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
حیاتی، معاون امنیتی و انتظامی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
خبر تکمیلی در خصوص خسارات و تلفات احتمالی متعاقبا اعلام خواهد شد."
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/76040" target="_blank">📅 07:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76030">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KYsAwDT8C3qfwgIsd9Zh6e9iwPPQFuR4ZpVqVp1_qaaVEqxmNYxMa70Nys6G3MD4IBzOyCgoWnroHb2YvT8XQUpcjkKFoOLb58P64AL_7zCGS9spbGw4X1jrL_9QdZVdxugjdaeBeTgH9MEhbZHuICttiC8kWrWbuljeTapDiKbdNo51HN2KLmTV2ijDabNvJ3-3l4QoF9VoQ8pD8al10lZ0RMU_ygP9nGfl6FF-ypdToqgO1M1Lh_RJ3PYc1QH7MWnviGvqU4JL9kg9PBNJtl-kR2QAOjFq0vZVhH8fgWWQQYS79NETgw8GbSqVLBxCYBDuSl2vkKn5_Vwvny5R-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eq3ZYbcKUJThn7YBa9AoZWRsnnXwjg3M5VYVk_CGhCCwtukGFsjO7CERaVhcOWHq4DDblcj9Sog_NXwd9ptkcmUAbEUHw5zEsh4oLxoU68WklppqKXKg2N3IFDdiQX5VaNeQPpm8RY3T8b8YAn5XyikGSVtJz0sbjtQyoBWudKZ79-dNSNPcz5GExEDbv1Z8Tx99j4JK-2tJ8shszGv9nYbCVKc7uPP29toZGh_roGYryIXe9YWCwB9cqA-1hR1z2JfvUmAYhyRCnDpSKKMoovqdefOV9jmpjgqCk647G9JIXMH8X9roqMCMmhma1MyAn0EHThcV_eZM0TZZA6zGLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iLhtgJKt93p9U4ZUpOpKz16ngLp-E9vSd2sYThrmEl0yOQvOzArxDnFwVHp27ms9nRnRnkPCwhvN6_Lf1UO3ABrME4jMmZfCzt1V0hgdq0iDC0pdiH4uLMWiapeD4DmLsH1AkT9ksNr2AMKTWR9XG61OHtg8VuDTmybmXsFJTjpEr8_IjWxTEluI_283Tl0uC9FD5HQQx_OvYybks-eu228A85w4_7IeWsnVjyePm0R9ILQNK1tNNkVT79FRMBbIO0DJM2ZayP3xFdWijq8qRw9AM0vtroUTDq8oN22NdEn1jFspJQqdrCwfTkYXBahMS8KSZnsRW-LjufT4qTYaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QEol8xXiFZRxtCsQUJv9mTu89ep2e0UAwiVpyTq42iWQNkS4fLXqY4VmBjDdkURPUh06Jtmq4WzfLOuXWRJwrqcrzugkcvWpzTgrlx4Rf2JR6OyCpNSnPscgcTMRDSqXkC4FPeRUGxkah9YAIPz1Yfvk7D01ccAlYK_RtWXoMC5dr_TRHtujJ2bPoQR3wTd1RLEDn_fHTGs_ck06E_4yb6LalbN3hJzxHYA_eE3TxALSSxEgj-8xDNvkv6n2qDr6LhqmA3x2pqM2yQZHdWx037mHrRccsu4pYuKl69wn5ZFu45Jdt8Zy6sMguXbaFCn0iT0vALYE8olMdFKCPBJtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YACIlHb_DKRTVpo588bRMzMlaGdyEloIqQVAvuzCtJohcPQNBQLHVWpcUobeGZRQwGlfUbLXpNBZw0okeEFhdKg30VmKkL2qIUbirPp-S4G36mltrUVyjW1HQwblWUlNQ9VfiNEdf3Fsn9r4AVBvHe47X41bIxSClTxV4ptC5OVpWw-J0CTllKRzE3jtZukxSXKUl8j9VCaffyNImK1uFY6SYRCEQzW8LZVK3KJOvm6ONTf3ypq_x7lArFgxpV3OiAmEwOtphaUFwKkCd_SCybr5hjtCkOm5Lcda82McXqYrs05Co63ydFC4Nwz9wsg2xm7hTQj1_VSio3RJgz0WlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08feac2b13.mp4?token=ogKSqAk7M_rV6BUVaMcTuYpeqmdPvwwAajBKyjHWHC29OT7FXESL_VxDKeeXdxd5XqHGEJQGsda3A-H9p7uTKSXpMGz0nmV1Ng_tt6XqhVKGfWj5qx61ZCIhQv-6LSSoDuEYUQ0CShTUdm6vkxgiy5-YNVowQlCJ-9G8Bpry3Tmdf8K-AAndtjTn-UpYbOg8JouuEtrggGvnpqQVGCCKBahTXmb5ttkey26yABnMSsTcDs88ve_FCuFjoDGZXRMU_R0lf8wphao93nRHdHErKR5gCRPWKxr217J960L2KVpEBknAyj0Qntuu8g9qAqmTujMU1sRu5QMKluhD3mp6Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08feac2b13.mp4?token=ogKSqAk7M_rV6BUVaMcTuYpeqmdPvwwAajBKyjHWHC29OT7FXESL_VxDKeeXdxd5XqHGEJQGsda3A-H9p7uTKSXpMGz0nmV1Ng_tt6XqhVKGfWj5qx61ZCIhQv-6LSSoDuEYUQ0CShTUdm6vkxgiy5-YNVowQlCJ-9G8Bpry3Tmdf8K-AAndtjTn-UpYbOg8JouuEtrggGvnpqQVGCCKBahTXmb5ttkey26yABnMSsTcDs88ve_FCuFjoDGZXRMU_R0lf8wphao93nRHdHErKR5gCRPWKxr217J960L2KVpEBknAyj0Qntuu8g9qAqmTujMU1sRu5QMKluhD3mp6Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
۷:۴۰ پرتاب موشک از بیدگنه
بیدگنه شلیک موشک بالستیک همین الان
همین الان ۷:۴۰ موشک از بیدگنه رفت
دوباره از ویلاشهر نجف‌آباد موشک زدن
وحید جان همین الان از کرج موشک پرتاپ کردن
7:39 دقیقه از ملارد صدای پرتاب موشک
یکی دیگه همین الان اصفهان
شمال اصفهان یدونه موشک دو دقیقه پیش پرتاب شد
الان دوباره موشک زدن ٧/٤٢
اینجا،اصفهان یک بار ساعت ۷:۳۰ دقیقه یک بار هم الان،۷:۴۰ موشک پرتاب کردند.
۷:۴۰ از سمت ملارد انگار یک موشک زدن.
وحید همین الان از جهانشهر کرج صدای پرتاب موشک میاد خیلی صداش شدیده.
سلام وحید 7:40 صدایی شبیه به برخواستن موشک از نزدیکی مهرشهر کرج
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76030" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ecMozzZcRHFPu4ageVP8do39bsbJ_XJpr8JG8NcDTbEGxcV42AWyi3hwd34qQ9QGHfvSheNkfJ0hKj2T-SIRTAYEWZHmppkpalFBt2Tpfe-A4dx6CAQLHcRNkm5LWsw35picsJ2euvLAMNCMVM_TMyv2_ht6hpKc_hMqBxluHtAkASrXrhgAudbbzMElRkhnxFHx2qybwFOHOkVBpgK3Dhu6B3FOwTKD2AjJgp8fJkHXRAaoA42w6fKjp-kOa9fbQC06_VAwQu76ufab41AItRLEbFex67huxariZESNdSc7cxh6DmVTgtzdfQePkwaBiHFqvnDp6QAOMceczMe99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
۳تا موشک از کرمانشاه همین الان
وحید کرمانشاه همین الان صدای وحشتناک اومد
سلام ۷.۳۰ صدای انفجار از کرمانشاه . احتمالا پرتاب موشک
سلام وحید جان
7:28 بندرماهشهر صدای انفجار اومد
وحید 7:30 دقیقه ارومیه یه صدای سنگین اومد
الان ۷:۳۱ از ویلاشهر نجف‌آباد موشک زدن
الان کرمانشاه صدای انفجار شدید
شلیک موشک از ارومیه
خرم آباد 2 تا موشک از پایگاه امام علی انداختن
از ارومیه موشک فرستادن
پرتاب موشک از نجف آباد
اصفهان شلیک موشک
سلام وحید جان از خمینی شهر یکی زدن
آقا وحید همین الان شلیک موشک از فلاورجان اصفهان
شلیک موشک از ارومیه
با صدای انفجار زیاد
سلام وحید آنلاین همین الان ساعت ٧/٣٠ از اصفهان موشک زدن
سلام وحید جان همین الان موشک زدن سمت اسرائیل از اصفهان
موشک الان زدن از پادگان پشت ویلاشهر نجف آباد
سلام ماهشهر ۷:۲۶ دقیقه صدای یک انفجار شدید اومد
از کرمانشاه ۴ شلیک، نه ۳ تا
ماهشهر حدود ۷:۳۰ صدای انفجار اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76029" target="_blank">📅 07:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ly-ZWonNxFVLhbOcEYHDN1VCoVpaEQHbE5RG5C1Co7KBYkba707iMxZlDskbFfVfnk55YLiSR7gS-mr_p-UEXO5zr0VC0rTVoOFjdabkCzOjKrbb6qOztk5CECxwrvHkmhen8evzVRwsjE0D1qSb36gR78yYp2IW9wLy6O5h10NXutDt7rO5eV_GjbuwgvhZ7SIHaXj8GrC_JLQYfj5Y6SuOPj0hNuBSNlBTmMONhG18BuxX0Rg-HfffMNJ9DnB5fVBKBUIxk9Blvg82g23ERBqLAbRWodVy8EGtTKfThAmq-LFGJ_CxinOOl4HaCzjl9Vimzr6b5P6jnWt8xGsCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی بعد از موج حملات موشکی ایران به شمال اسرائیل، خبرگزاری تسنیم، نزدیک به سپاه پاسداران، در تحلیل و تفسیری درباره ابعاد نظامی این حمله گزارش کرده که در حملات موشکی و پهپادی یکشنبه شب، سپاه پاسداران از «پهپادی ناشناخته» که از موتور جت بهره می‌برد، استفاده کرده است.
کارشناس نظامی تسنیم همچنین از شلیک موشک‌های خیبرشکن با کلاهک‌های خوشه‌ای در جریان این حملات خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76028" target="_blank">📅 07:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76027">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFHTRhZzyIYuBzBBg4z2TNBcX8D5JHtkm5FJUMAlF-vYm0FD-KpHq-_tLG7EU724DjWiMzI4zfjnFki4i5XMCnAOMVzUp7ZlpQrthfkSRgmFczTiTJTlRwoRbPDovfmW7WdTlC2U8PwFUq4T2LyPNLZPzbN7JTviZkBaUZGgiynlHlyQNVwe4a6lpqE9J2mz94KxPMapXCx9TgM-UhJr8m1745SLOopUaBILBHPh5R8N3g3TSyZRtMeWV20qBsrEDjTKuZyXhx_FP75kCWcDoSe9mrH0DJ94D8AMxvPHGphsG5FuSO53mKcD1SKtdmQ4VFT7c0YTaVUvZTvlaphKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یخیئل لایتر، سفیر اسرائیل در آمریکا، در پیامی در اکس نوشت: ارتش اسرائیل پس از شلیک موشک‌های بالستیک ایران به سمت اسرائیل، سایت‌های پرتاب موشک زمین‌به‌زمین و همچنین زیرساخت‌هایی را که به بخش انرژی مرتبط نبوده‌اند، هدف قرار داده است.
لایتر افزود: «ایران امروز ۱۱ موشک بالستیک به سمت اسرائیل شلیک کرد. هر یک از این موشک‌ها می‌تواند یک محله کامل را با خاک یکسان کند و صدها نفر را بکشد. هیچ کشور دارای عزت‌نفس در جهان چنین حمله‌ای را تحمل نمی‌کند و اسرائیل نیز نخواهد کرد.
سفیر اسرائیل در ادامه نوشت: «مردم لبنان، حزب‌الله به‌عنوان نیروی نیابتی ایران را رد کرده‌اند و به ایران گفته‌اند از کشورشان خارج شود. اگر حزب‌الله به اسرائیل شلیک کند، مراکز فرماندهی آن در ضاحیه به‌شدت هدف قرار خواهند گرفت. این موضوع هیچ ارتباطی با ایران ندارد. همه از این رژیم ایرانیِ دیوانه خسته شده‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76027" target="_blank">📅 07:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76026">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRxS8cWRCXtjkrEWyEe1F1qVrFgGuX8Caf3MDZfjrPmfGFCxH4hq9fmYj4xVtMMP-o1Gy7aAukS35XwF914XFI3G_oq4oduHUQULDYhvPsge0snO5AH0kwz83RFKI7ShtVTxuZ38gSBujPb4L0aL58zkPOP8EizqcllYEfT_G5BUQ7DzUbtReMcCW0OhyESa4iQmHDHw-pDfiEYJobrF1_wLt0DTRMzCNtP52JFvsUkhwljviPSH9-b80N5xP0dTiRc0xRKFf8TxGQeR1TLPsSFWqufLm1wKkhkaCKDpOnNZ9ZCdiyiwm0KbtfDyIHBch5qkiQN9EUiWWb2mRvWPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
یک مقام آمریکایی به رسانه‌های این کشور گفته است که ارتش ایالات متحده در حملات شبانه اسرائیل به ایران هیچ نقشی نداشته است.
نشریه آکسیوس به نقل از یک مقام وزارت دفاع آمریکا گزارش داده که این حملات اسرائیل «نسبتا محدود» بوده است.
این گزارش در حالی منتشر می‌شود که دونالد ترامپ، رئیس جمهور آمریکا، پیش از حملات از بنیامین نتانیاهو، نخست‌وزیر اسرائیل، خواسته بود در بحبوحه تلاش‌های دیپلماتیک جاری از اقدام تلافی جویانه علیه ایران خودداری کند.
آکسیوس پیش‌تر گزارش داده بود که آقای نتانیاهو به صورت غیررسمی یا به تعبیر این رسانه «تلویحا موافقت کرده بود» که این درخواست ترامپ را بپذیرد.
حملات شبانه اسرائیل ساعاتی پس از شلیک موشک‌های ایران به شمال اسرائیل انجام شد و در حالی صورت گرفت که واشنگتن همچنان می‌گوید در تلاش برای نهایی کردن توافقی با تهران و جلوگیری از تشدید بیشتر تنش‌ها در منطقه است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76026" target="_blank">📅 07:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ki7Hk3mdnn8Fl7R0DY5K9G90gByp_isVshp7ZUaRzdXA0tOYU-Ocxgysfbttl4qCatVSZzl-4kUPxq4Yd_KpnDHftMJpke55QXbolEUa7xNLZXEM-zZEPIy3KoBmJHf98XdGVJk-66ZLJh6GeWzqxVQAcTSEsPlXOfebKIa0J8UudceHdYmoL6nNarSEYxM-jLk_R7E29qJs13Q0d8nAZ1FZR9bQK1ZdLyQ6EZSxNnp6lDgffP35ZdEpmKHSwQvdYLRXIvNYX3lcgVo36_Ojyj2YUscBDzPSLdC9H6y2MISb5OM2r9r5lA-CrcyMykrfEuOOdgr3ele5HNOlzcRZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل پس از حمله‌های یکشنبه شب سپاه به شمال اسرائیل و حمله‌های متقابل ارتش اسرائیل به غرب و مرکز ایران در بامداد دوشنبه اعلام کرد که ارتش اسرائیل یک موشک شلیک شده از یمن را رصد کرده و سامانه‌های پدافندی در حال رهگیری آن هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76025" target="_blank">📅 06:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UIN9hsTDdRjM7-Qff0XJUeKE8VIokpijLQyiUDA5gBkpifGydMUu5dAUMnNjoTfI9qyCePs0ESvoSXkc7-ftO_G2SiwF-vkw_v7tY4l_xlnRK6NkX5lA1wDLcwuq_rDjTHaLjfu33C7DSS98NCezdeQ_OmQj7fAci5dj-GPJ9-X4IgEHsF8nFQ_FHByiZg851FrLlUuSwH5MMT6mgqj6qfJGQZc1CBrWGeY2bm-wXUGpiUy55JVdi_Adqx19eklwhUqRY0HJ20ErLik5ppj6B0TdzC_oiHKTpXnn3v0q8vo_LXcliuxxJnGRJxifihkiVIYDHNiPROq7GbtOaUWvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس گزارش داد که عربستان سعودی در منطقه‌ای که پایگاه هوایی شاهزاده سلطان، میزبان نیروهای آمریکایی است، آژیر خطر موشکی به صدا درآورد.
@
VahidHeadline
آپدیت:
خبرگزاری صداوسیما، وابسته به رادیو و تلویزیون جمهوری اسلامی، به نقل از «یک منبع نظامی» اعلام کرد که جمهوری اسلامی هیچ شلیکی به سوی پایگاه هوایی در الخرج در عربستان سعودی انجام نداده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76024" target="_blank">📅 06:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2QnYPX34tmY1wPG8gxDnGfmvq0E0c0RshzEVNI4g_FR-xf25KdtXz73-CE_daK2hD9p7-LO6WxP1bhtyV6RQ7SFJ0nocUpbLgBoXqwA0rv6ESIIR_4cUFSgQBy9ZixSsm27RUam772A_7GhBBQGI3gUWd2KX4FVkvHOAmWTQAThCnoU3Vsbb8qSEJ7ZRF-ZvrN8JlT7vozFGIggR80mPJcYU1--RIBLxHAQ4-SyeVx7Jp_zWHZYueSdWerUHOjB0Ya5iyCHmcdPKbZ7tNe_-Tod9tRe8BtJ5ouhIrf_ksyZpXecdzDTsxjnlgWC6r3qrews-rFhH_IRPMFEihJ96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌نشانی تهران اعلام کرد: صبح دوشنبه دست کم صدای ۲ انفجار حوالی ساعت ۴:۴۳ و ۴:۴۵ در نقاط مختلفی از غرب تهران شنیده شد و ادعاهایی درباره هدف قرار گرفتن فرودگاه مهرآباد منتشر شده است. سخنگوی آتش نشانی تهران از آماده باش آتش‌نشانی خبر داد، اما اعلام کرد که نقاط شهری در تهران هدف قرار نگرفته‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76023" target="_blank">📅 05:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76022">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FnlheAtfN-qIrg_fm0JiZV2RTa_GOlPKrO5waG4Um6gIEeZyFdX5rIh5YbfcBRtmp_ihiPU4UfdAqkovVrfMyoCzK6QQ6ft9mMrLHBonjxmbuMz4aBIMAE2bzhk_HlqJ8bFK4m5LPjAR9tw-srW64FhAgS0qL21jQGvE_acTVt6jiHf9Q2KpSD0ox2D5tdcOJBVsWy6RD68Wlj3-NVHaGWCi7EXA5798sFQXiJGLQT3MLHGdRNpmY3MmSsIUpVBWV5pwxQLjYrgsqy1azQZQMyLtnTbmZVMDoD-7fv-F_Iwhru7OWjzEwGtGjiDrGjY8slCN6xE3OQTFf91pUIA1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک خبرنگار اسرائیلی حوزه دفاعی به نام امیر بوخبوط می‌گوید که نیروی هوایی اسرائیل صبح دوشنبه به ده مکان در ایران حمله کرده است که از جمله سامانه‌های پدافند هوایی و موشک‌های بالستیک در آن‌ها قرار داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76022" target="_blank">📅 05:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76021">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cbBv8F8aEtV5cHwuPDF42IEIZ4q4ZjrND-IBmcIs0Gbks0LRkUfqZA0b3MsRiRmiT-WaDodJ356r9WXV7JhDeRs2A4D-hXlXzoy4n4P5_oKFgMfd9UWkVAbOBoSIwpQDFaEVkxPHRFdiM8ZunfsjMYRBdRxQ3OgGR6c7BKIAlhtt-SvYaZdi6AZZMckOdFB8r2K1rYmh9ymLeb4sa4IPXhFBbKVdHZeew4PW8ngyUVD2w0cAaE8e4Jkm1WEkbbB-ci6oLfdaJ6xgGa6-SiBYqjd_jRq8-6pCsE7CAXvJgf2H0sWc5coi-Gbb1DjEVlqZn6JFgEon0AB-x9ambJx0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درپی اعلام حمله هوایی ارتش اسرائیل به نقاطی در غرب و مرکز ایران، سپاه پاسداران انقلاب اسلامی بیانیه‌ای صادر کرد و نوشت که اسرائیل «با استفاده از موشک‌های بالستیک هواپرتاب اقدام به حمله به اهدافی» در خاک ایران کرده است.
ارتش اسرائیل حمله هوایی به مرکز و غرب ایران را اعلام کرده اما هنوز نوع سلاح‌های به‌کاررفته در این حملات را اعلام نکرده است.
خبر این حملات درحالی منتشر می‌شود که یک مقام آمریکایی به اکسیوس گفته بود دونالد ترامپ، رئیس‌جمهور آمریکا، روز یک‌شنبه در تماس تلفنی با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از او خواسته بود فعلاً از حمله تلافی‌جویانه به ایران خودداری کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76021" target="_blank">📅 05:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KuQC7bGU_ktGq6g67VnbDwBwx3rxqjFVRnTErIrMWY3Ha2d8yj3fcjmAmyB-u06Y989gkd2kKWvJyKfcymZlVnkG5rPzqHBMWPlajCJlakanz6hbNH4BCCSnZoqWtyfS5g7waVN-K2jzlU3qXgsQzLtc_m33AHdr6gBuIdI5uEPBuwAcGD3Tr3gW9GTBBpV5Iy9jWo-9qO3b2vOyw6cKZuhCMae-AkKBs8Lu2kLrQUpZhddaMSZZBEceFTCy3snoFXEd0mXi_3G_EVIw_37cl66SPC-t82eSf7rd9Nn7s1phsK31BKEAYPEbHKNyErLRMEz0DkuDfVYtAqqWHv945w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c2hGVItuRHOli3sAFNEYAvc1C6a_5cGrDxakNpnZMFElECjW1QDc5IuiRx_9SfBwXoDf74PAJIdyTR_a88NXTbZ76RXIKhtVbN6SzbOZp2p2C4oW52GdCnrp4FAox8PvfbcmYh0-iExWjTFiVq3MPIrZ21sbTv4z0_fM1sDoUlsYe4E2YpF-QOQ53Fa2u7x2o55P75Gh9o2yWIE7Y3OhA71fi4nx4iXLWurX0cSV-EptvbG3w8WAfoIVmHMS2lD26I9257Il9fnkxwXQ0ydp_iAUVUwX1R2-J2ZSTN_lkX5qS0M5BYjdjPyl4bIJ-e30VJ9qkgvk4BLHTmCyFFypYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کانال ۱۲ اسرائیل از حمله نیروی هوایی این کشور به فرودگاه مهرآباد تهران خبر داد.
@
VahidOOnLine
درحالی که هنوز ارتش اسرائیل اعلام نکرده حمله‌های بامداد دوشنبه در پاسخ به حمله‌های یکشنبه شب سپاه پاسداران به شمال اسرائیل را با چه تجهیزات و تسلیحاتی انجام داده است، کانال ۱۴ تلویزیون اسرائیل گفت که جنگنده های اسرائیلی اهدافی را در ایران هدف قرار داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76019" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJ3wsSqWJYOjSRMtFOLiqPXfpJYbU9zc0xcCy6WdaePbo3210dulflhGh3VLIBZnkoedf-ub-Gfokvczg0w9-zJM0TnI-3CtPqDy2VSQpGYfMGU2EGjpmDtE-CsLBxampVJRyDmwkAkOip4-t330g5qRJzTRA0Sgyo4BPC14LLtUUt85kZdN4c-pPL0w8kBiIpiSydTNiDHjlOmPwsRdrUfmfen2-NaMsAtWrqADwBhD-ttZv0OUqdM_Xjh3ji-Qv1pS3jYotj7vKGsoLe1UA7fAF0FPvQtNuFlnBznKnFlhfCkFxkwl5v4eLbkaWd4Uk3iF0idksuO8SIaSIyTRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👆
نجف اباد ساعت ۴:۴۰ فکر کنم با پهپاد زدن
سار پیام‌های دریافتی:
کرج هستیم الان  دوشنبه ساعت ۴:۴۳ دقیقه صبح  از راه دور صدای انفجار بسیار بزرگی اومد
سلام وحید سمت شهرک غرب ۴:۴۳ دو بار تا الان صدا اومد خفیف بود
ما رباط کریم هستیم
ساعت ۴:۴۵ صبح ۴ بار صدای انفجار اوم
وحید ساعت 4:44 صدای انفجار نزدیک سمت جنوب تهران (باقرشهر)  شنیده شد طوری ک خونه لرزید
سلام،چهاردانگه دوبار صدای بلند اومد ساعت ۴:۴۳ دقیقه
سلام وحید سمت مهرآباد ساعت 4:45 دو تا صدای انفجار شبیه دوران جنگ اومد
ما شمال غرب تهران چند دقیقه پیش و دقایق قبلش صدای انفجار مهیبی شنیدیم ولی دور بود. صدای جنگنده هم نیومد
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76018" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LHEamGc0u3M0ujbWZA5QQWRJ_JA0oQ0nrtpUBpS2VO1v0wZDGmpqd6tKWEJwzKhtSx8PCIx5ydF3ePf_CEfloa5Xxw77hcjLQdyoUV9sMZ8PilFQZSKLp_F6TZhiwcDCgaMr45fy-Mki_INBY85uPO4HdMHZ49OV0A98cI1Dg3sQ69PWcdeifj1MGVwZswRa-yBz-5H8gnrJNZRCMna2wps8TzaGJuBw6YMQB-yWbCDijhyJv0pRC4BAOZfAP5G9xZAVlVLHCuWB6dVt5FLxJ5rLs44X5oxx_d-hgoQWFU3R2aeBmRpmf153YmGgKkp9zn5yigSlpPXn7wfMJrKCkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👆
دریافتی با شرح: نجف‌آباد
سایر پیام‌های دریافتی ساعت ۴:۴۵
سلام ساعت ۴:۴۵
سمت خزانه دوبار صدا انفجار اومد
صدای بمب جنوب تهران ۴:۴۵
سلام همین الان صدای دو انفجار از میدان المپیک
داره میزنننه
فردیس کرج ۴:۴۵
همین الان صدای مهیب سمت مهرآباد
ساعت ۴:۴۴ سمت غرب صدای عجیب و بلند اومد ، لرزش خفیف سعادت آباد
تهران اندیشه
دوبار صدای انفجار همین الان
سلام اصابت موشک غرب تهران تا الان دوتا انفجار 4::44
صدای دو انفجار با فاصله کرج
ساعت 4:43 دقیقه غرب تهران صدای تک انفجار
دو دقیقه بعد دوباره صدای انفجار اما دور تر
صدا انفجار داره میاد سمت غربه انگار
دوتا صدای انفجار غرب تهران
تهران زرگنده ساعت ۰۴:۴۳ صدای دو انفجار اومد
الان ساعت 4:43 دقیقه و 4: 45 دقیقه صبح غرب تهران صدای انفجار کوبنده شدید
همین الان دو تا صدای انفجار در اصفهان شنیده شد.
سلام وحید. شهرک اکباتان. صدای انقجار اومد دو بار همین الان. ساعت ۴:۴۳ و ۴:۴۵ دقیقه
صدای انفجار , کرج , ساعت ۰۴:۴۲ , ۱۸ خرداد ۱۴۰۵
صدای انفجار , کرج , ساعت ۰۴:۴۵ , ۱۸ خرداد ۱۴۰۵
کرج صدای انفجار 4:45
جنوب غرب تهران دو سه تا صدا مثل انفجار از دور اومد
صدای دو انفجار مرکز تهران ۴ و ۴۵ دقیقه صبح
یه صدای گروم مانندی اومد اما دوره مرزدارانیم ساعت ۴:۴۳ بعدی ۴:۴۵
سلام وحید جان ساعت 4:40 دقیقه رباط کریم حداقل 4 تا صدای انفجار اومد
ساعت ۴:۴۳ و ۴:۴۵
۲ تا صدای مهیبی اومد نمیدونم چی بود
سمت خیابان زنجان
زد صدا اومد شهران ۴:۴۳
دوباره زد
نزدیک نیست ولی صدا میاد
۴:۴۵ تهران شهران
وحید ۴:۴۳ صدای انفجار دریاچه چیتگر
کرج مهرشهر دو تا انفجار به همراه لرز ساعت 4:40
احتمال میدم سمت فردیس باشه
وحید تهرانم سمت شرق یه صدا هایی میاد شبیه انفجار ولی نمیتونم تشخیص بدم
۴.۴۵ دقیقه تهران سمت غرب ۲ تا صدا انفجار
سلام غرب تهران دو بار صدای انفجار اومد
سلام وحید ساعت ۴:۴۵ دقیقه شرق صدای انفجار اومد.البته دور بود.
وحید ۴:۴۲ پرند صدای انفجار مهیب حداقل دوتا
سمت م معلمم یافت اباد
همین اطراف بوده صداش همراه با لرزش بود
دوتا صدا انفجار 4.43
وحید جان ساعت ۴:۴۵ سه تا صدا شبیه انفجار سمت غرب شنیده شد.
وحید جان شهرری همین الان دوجا رو زدن شیشه ها لرزید
ساعت ۴:۴۵ ۱ انفجار دیگه شنیده شد
دومی صدای مهیب تر بود
جنوب غرب تهران سمت تهرانسر همین الان صدای دو تا انفجار اومد حس میکنم موشک بود
سلام تهران سمت شرق و غرب صدای خیلی بدی اومد
۲ تا پشت سر هم ساعت 4:43
مرکز شهر سمت ۷تیر. ۳تا صدای انفجار از دور اومد الان ساعت ۴:۴۵
وحید جان صدای دو تا انفجار به فاصله یکی دو دقیقه حدود ساعت ۴:۴۴ از نزدیک ستارخان شنیدم
سمت صادقیه تهران تا الان دو بار صدا شنیده شد
از ساعت ۴:۴۰ تا ۴:۴۵
اما بنظر دور بود معلوم نیست کجا بود
سلام مرکز شهر تهران ساعت ۴:۴۳ دوتا صدای انفجار پشت سرهم اومد ولی صدا دور بود
سلام اسلامشهر ساعت 4:42 بامداد صدای خیلی بلند اومد
صدا انفجار تهران ساعت 4:44 سمت پیامبر مرکزی
دو تا صدای انفجار مانند اطراف اصفهان چند دقیقه پیش( فکر کنم نجف آباد ۴:۴۲)
ساعت ۴:۴۵ و ۴:۴۰ دوتا صدا انفجار اومد
سمت مهراباد
سلام اقا وحید ، سمت شهرری رو فکر کنم زدن خیلیی صدای بدی اومد من از خواب پریدم
سلام وحید جان  الان
دو بار بیدگه ملارد رو زد
کرج مهرشهر
صدای دو انفجار ۴:۴۳ و ۴:۴۶
وحید حوالی ۴:۴۰ تهران صدای انفجار شنیدم
دو مرتبه بود، اولی اومد بعد از ۵ دقیقه دومی ترکید
4:45 فردیس 2 صدای انفجار از دور دست
دوتا صدای بدجور اومد ساعت ۴‌.۴۰
سمت خانی آبادم ولی صدا یکم دور بود
ولی زیاد بود مثل غرش بود
شهریار صدای چند انفجار بیشتر سمت رباط کریم می خورد باشه
درود وحید جان ساعت ۴:۴۳ دقیقه ۳تا صدای انفجار توو پرند شنیدیم
سلام ساعت4:42دقیقه صبح صدای انفجار در اشتهارد شنیده شد 2مین بعدش هم بازم صدای انفجار صدای بمی داشت
سلام اقا وحید من اسلامشهرم با صدا انفجار بیدار شدم
صدا صدای زدن بود،سه تا انفجار شنیدم
وحیدجان سمت شرق اتوبان بسیج صدای 2تا انفجار اومد ساعت 4:45
رباط کریم صدای شدید انفجار
چهار پنج تا
غرب تهران ۴ و ۴۰ صبح صدای دو تا انفجار اومد اولی شدید بود از خواب پریدم
ساعت ۴:۴۵  دو بار صدای انفجار اومد کرج
تهرانسر ساعت ۰۴:۴۳ صدای انفجار شنیدیم و از خواب پریدیم.
اصفهان چند تا انفجار شنیده شد
ساعت ۴:۴۲ دقیقه، از سمت غرب تهران دو تا صدای تک انفجار اومد. یکی دور و یکی نزدیک
درود صدای چهار انفجار شدید اومد ما سمت نسیم شهر هستیم جوری بود از خواب بیدار شدیم
ما نزدیکی اکباتان زندگی می‌کنیم و توی پنج دقیقه ی اخیر سه تا صدای انفجار شنیدیم
کرج صدای انفجار میاد
قطعا حمله شده
رعد و برق و غیره نیست
اصفهان دوبار صدای انفجار 4:42صبح
هیچ صدای جنگنده یا موشکی نیومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76017" target="_blank">📅 05:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌های دریافتی از ساعت ۴:۴۰
سلام وحید جان
4:40 دقیقه انفجار از سمت سپاه تبریز طرف متظریه اومد
۴:۴۰: وحید ارومیه یه صدایی اومد نمیدونم چی بود
صدای انفجار شدید در ار‌ومیه
مشخص نیست صدای چیه
سلام آقا یک صدای مهیبی همین الان از ارومیه اومد ساعت ۴:۳۹. شب هم البته چندین تا موشک از اینجا فرستاده شده بود.
سلام وحید ارومیه ساعت 3:39 صبح صدا اومد و انگار زدن چون خونمون لرزید و دقیقا مثل موقع جنگ بود
وحیدجان نجف‌ آباد صدای چند انفجار شدید. ۴:۴۲
وحیددد
دارنن  اصفهانو میزنن
نجف اباددد  سمت ویلا شهر
دوتا زدن همه جا ترکید
لرزید داریم سکته میکنیم
شاباد موج انفجار شدید
سلام وحید غرب تهران صدای انفجار شدید اومد همین الان ۴:۴۳
وحید اینجا صدا انفجار اومد ۳ بار
خیلی بلند و نزدیک. ما کامل از خواب پریدیم
بدون صدای جنگنده بود.
نجف آباد اصفهان
خمینی شهر دوبار صداری انفجار اومد
وحید زد الان تهران رو
یوسف آباد ۴:۴٣ صدای انفجار از دور شنیدیم.
مجدد ۴:۴۵ صدا اومد.
۴:۴۲دقیقه همین الان دو انفجار پی در پی اسلامشهر
انفجار مرکز تهران ساعت ۴:۴۳
وحید زدددددددد
بالاخره زد
همین الان ۴:۴۳
غرب تهران سمت جنت آباد صدای وحشتناک اصابت موشک یا بمب
صدای جنگنده نیومد
دوباره الان ۴:۴۵ دومی  رو زد
توضیحات اینکه چند دقیقه قبلش برق نوسان شدید کرد
صدای دو تا انفجار همین الان نجف آباد اصفهان
انفجار لرزش شیشه صادقیه تهران
غرب تهرانسر یدونه صدا
اسلامشهر همین الان صدای انفجار مهیب شنیده شد
سلام ساعت ۴:۴۱ صبح، صدای انفجار شدید تو تبریز اومد، جوری که از خواب پریدم، قطعا پدافند و اینا نبود...
وحید جان از سمت قروه کردستان صدای سه انفجار شنیدیم با فاصله ۱۵ دقیقه، به نظرم موشک خوردیم چون لرزشش زیاد بود
سلام وحید جان
ساعت ۴:۴۴ صبح اسلامشهر مرجان آباد
۲ انفجار شدید پشت سر هم
جنت آباد جنوبی صدای انفجار - ساعت ۴:۴۴ صبح - ادامه دار نبود در حد دو سه تا بود
۴:۴۵ مجدد زدن
ساعت ۴:۴۴ دوشنبه صدای ٢ انفجار با فاصله ١ دقیقه از هم غرب تهران
الان صدای دو تا انفجار شدید اومد . اصفهان
سلام از انديشه
وحيدجان فكر كنم ٢تا صداي انفجار بمبي اومد اينجا
صدای انفجار از دور
غرب تهران ۴:۴۳ حدودا
ساعت ۴:۴۲ دو تا صدای انفجار توی قائمیه اسلامشهر  اومد
پشت سر هم
آنقدر شدید بود شیشه ها به شدت لرزید
ساعت ۴:۴۲ صدای انفجار خیلی خفیف شمال اصفهان
انگار خیلی دور بود از ما
فکر کنم ۳ تا بود
اسلامشهر ساعت ۴.۴۴ دقیقه صدای  سه تا انفجار اومد
وحید حان مرکز تهرانیم، ساعت ۰۴:۴۴ صدای ۳ تا انفجار شنیدیم.
وحید سلام. صدا دوتا انقجار ۴/۴۱ نجف اباد
صدای انفجار فردیس
وحید نجف اباد صدای انفجار بلند  چند تا شیشه های خونمون لرزید مثل چی
بیدار شدیم ۴.۴۳
یه جارو زدن داره مثل چی ازش دود میره سمت همین نیرو انتظامیو اینا که توی جنگم زدن
الان صدای دوتا انفجار اومد
شیشه ها لرزید
مثل صدای لانچ موشک بود
شاید جای رو زدن ولی صدای جنگنده نیومد
خمینی شهر
سلام نجف آباد الان صدای ۱۰ تا انفجار اومده و جنگنده
سلام نجف اباد ساعت ۴:۴۲ دو تا انفجار خیلی بزرگ کامل مثل وقتایی که میزدند بود. صدای زیاد و بعدم موجش اومد
سلام وحید همین الان صدا انفجار اومد سمت تهرانسر در حدی که شیشه لرزید
دوباره الانم اومد ولی دور بود
4:41 صدای انفجار اومد
04:44یکی دیگه.
فکر کنم بیدگنه رو زدن
چند دقیقه پیش تو استان کردستان شهرستان قروه سه تا صدا اومد آسمون صافه ولی اطراف رو زدن احتمالا
غرب تهران صدای انفجار
مجدد
وحید داداش صدا انفجار کردستان
سلام كرج ٤:٤٣ صدا انفجار طوري از دور اومد. رعدو برق نبود
بازم الان صدا اومد
ساعت 4:42 صدای انفجار خفیف و لرزش زمین سمت صادقیه تهران
4:44 صدای دوم شدید تر بود. صادقیه
توهم زدم یا صدا اومد؟ سمت ملارد
زدن وحییید زدنننن
انلاین شو وحید بد دارن میزنن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76016" target="_blank">📅 05:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76015">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eUGZYRzJ1vq5qwEm-CF5vP8kU_5JcSUHODVrbCLjSG0lyH3zhrgO_wsxBwtck5BuIno6xaZFMAl3E2vP6CBdKZfi8CQavTC3EhzbIrZLRpUQkwjvuGJY0RLpxM5_RRsreKzAukdtet_465kTnEcnZ2UTXUUyHRjyuGLZAJj88Rlt-rr9l2P164PmOETfj6ekX87qrExxLRkaZiNFjjvQ4oeyJqipK07Y4-ovAAHzLG4fay35YCJqh11Oh7yE5Mp6pV0TvLeHi45_9Egvk-wyKmXmaCR-hXtNdJ8_ZQzRSl0DiPgBJt08q3XB-jW5vnsZB7DKBxLAPjLFbxrWonTf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل با انتشار بیانیه‌ای از حملات هوایی به چند نقطه ایران خبر داده و گفته است: «نیروی هوایی اسرائیل، تحت هدایت رکن اطلاعات ارتش، اندکی قبل به اهداف نظامی رژیم تروریستی ایران در غرب و مرکز ایران حمله کرد.»
پیش از این سپاه پاسداران هشدار داده بود که در صورت اقدام متقابل اسرائیل با شدت بیشتری واکنش نشان خواهد داد.
جزئیات بیشتری درباره ماهیت اهداف مورد حمله، میزان خسارات یا تلفات احتمالی منتشر نشده است.
این حملات پس از آن انجام می شود که ایران ساعاتی پیش چندین موج حمله موشکی به شمال اسرائیل انجام داد و سپاه پاسداران اعلام کرد این حملات آغاز یک هفته عملیات مستمر خواهد بود. همزمان، مقام‌های اسرائیلی هشدار داده بودند که در برابر حملات ایران واکنش نشان خواهند داد.
این تحول در حالی رخ می دهد که دونالد ترامپ، رئیس جمهور آمریکا، در ساعات گذشته از بنیامین نتانیاهو خواسته بود از اقدام تلافی‌جویانه خودداری کند تا روند مذاکرات و توافق احتمالی با ایران آسیب نبیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76015" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd9OLI_RFj2II-T0ECFUfguZ2wlJVnrOzDVmv8ldWkvRyeyYqzzNIf1ySmW4qhn6W26YFQ8yCexrwsFNSbEwOKYq4ZqFDq0LANbxHbJI-ObTsawzLkxRrD3ycx-g-tfOqpQXcEd0hYHlfXTXeRsqgHkHOQtAwvSAf8fGvbd8mlm-vRkSzIQGyXH1Lb4W1J3kvp04MptqkNFaSBGpaPR5Qf2kxfv-uKdrizSaQNoR7S9IxSXvw89TWjVfZYY0PXuzN33QrKMHYYQAOOFKjPuz1wjvqBa8brhe37e49QWkcTHGSNBs2DiUktAv0yIb9OSS_tlA3B0slhjSZETdXtDSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه‌های رسمی ایران از شنیدن انفجار و حمله هوایی به چند شهر ایران از جمله تهران، اصفهان، تبریز و نزدیک به کرج خبر می‌دهند.
bbc.in
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76014" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtTevW1Pcg3pXk_coTL1TMJpi_7PSri-tDn9_orOBSfQkpqwIuDLwW6rSGIqqIkMTKC6vG7QLuzV0WWYIMDIzpd_zrNPKQnQBCCecUXdmLypuT8SNyK7mTtWC-V08w7cm7P-iJROpUXq7bDQxxe0y9MEJau7oomT4vox0h1X-uFiYB6jrwwlKNGJC_fVHV0XFn58Ylcbg8-wTnfW0RuV94vtW2my-2BAn9gL7fcqR887fdf-qtzJYY6MNfWBAHMvcogOSCA2lEajnHn253s3dU3w1o3P_zp9CMv9XfN11CPj7wwK3ho0MnI9cL3uayYHlJH9X64PxR7jDYhe67dGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در تهران، اصفهان و تبریز در بامداد دوشنبه خبر داد. خبرگزاری تسنیم از وقوع انفجار در کرج در بامداد دوشنبه خبر داد. ارتش اسرائیل نیز اعلام کرد نیروی هوایی این کشور «مدتی پیش» اهداف نظامی متعلق به «حکومت ایران» را در غرب و مرکز ایران هدف قرار داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76013" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YBgsIq0DyOzuXXheY9ysEljdnTxorubXCbCTW2F-8BZbKikiRQDpJ4VqgyTRPUGhpBZHmdZ5tOQ7sZP09taFB6HrCLejCg99slhOXihBdtnzZT6Qz9bXoTafq1fsnHjJqgnevr_zCmSCRNfrhOYPAXtYBF-m0RP2wK8AlXE85sinHrfg4uT1qI6ufwnt6ZShXkxJS2VhhkmHfF783tgSmuDmDy9_Q0ai63_nTWPRmzzEIBZwBGXUk9lHsx1p9h4ugFwOcVhdQ2pyTfRQangwDaWME90OsIQ4M1Zx_m7YX0uqF1g_WIekE_WbpV4kbEjPtMuJIIUi69Ecs6RfcW7z9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش اکسیوس، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با درخواست دونالد ترامپ، رئیس‌جمهوری آمریکا، برای به تعویق انداختن پاسخ به حملات موشکی بالستیک ایران موافقت کرده  تا به واشنگتن چند روز دیگر فرصت داده شود تلاش‌های دیپلماتیک برای دستیابی به توافق با تهران ادامه یابد.
بر اساس این گزارش به نقل از یک مقام ارشد آمریکایی و یک مقام ارشد اسرائیلی، ترامپ در تماس تلفنی یکشنبه شب از نتانیاهو خواسته از انجام حمله تلافی‌جویانه خودداری کند، زیرا به گفته مقام آمریکایی، او معتقد بوده «ما به انجام یک توافق خوب نزدیک هستیم».
طبق این گزارش، نتانیاهو تلاش کرده با این درخواست مخالفت کند و ترامپ را متقاعد کند که اجازه حمله به ایران را بدهد، اما در نهایت «تا حدی به‌طور غیررسمی» با درخواست رئیس‌جمهور موافقت کرده است.
این مقام آمریکایی گفته است که این گفت‌وگو بسیار آرام‌تر از تماس پرتنش هفته گذشته درباره طرح‌های اسرائیل برای حمله به بیروت بوده است؛ زمانی که ترامپ به‌طور علنی اعتراف کرده بود بر سر نتانیاهو فریاد زده و الفاظ تندی به کار برده بود.
پس از این تماس، این مقام گفته است: «فکر می‌کنیم رئیس‌جمهور کمی زمان خریده است. او بسیار قاطع است که ما به توافق با ایران نزدیک شده‌ایم. فکر نمی‌کنم در حال حاضر حمله اسرائیل قریب‌الوقوع باشد.»
او همچنین گفته است: «ما در یک لحظه حساس هستیم — چرا باید وقتی در راند چهارم هستید، یک توافق احتمالی را به خطر بیندازید؟ رئیس‌جمهور فکر می‌کند سه ماه است درگیر این موضوع هستیم و اکنون زمان پایان دادن به آن است.»
با این حال، هنوز تصمیم رسمی در اسرائیل گرفته نشده و طبق گزارش شبکه ۱۲، نتانیاهو تا نیم ساعت پیش همچنان در حال برگزاری نشست با مقامات ارشد امنیتی درباره این موضوع بوده است.
@
‌VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76012" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76011">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u-Yr7h2pKY3RY2xmw0XuDzJ_CTukW69sZVHuvpgbkJ_n7eM9FTOAPswvGrUWDMNzFbOEvYc2aPvt9h0-OzPAKNUfN2BAycxCia3NnW7ObXbDMefMGpDMpMvo_XZHHf8zOgTJmQBzRwJYYfnu-C727jOr7EKUR44Y6qwIEFlAla-oypcCzyVOPXkRlAafXYMuMV8Aw32PK5FM3Qgei6jPwOd391TPgEs0jXpAEe25dTmVRNTSUYkTaDRA3OmJ-mvSUriQwjfcL8LlV1M1Nn1FUKTc89b8abFX3eC9xsW1M7J9Va-KIiU18LQNr3JNMPEv18ScZhygWlIUkusVuuV-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید هر توافقی که او با حکومت ایران کند نخست وزیر اسرائيل خواهد پذیرفت
رئیس‌جمهوری آمریکا در گفت‌وگویی تلفنی با فایننشال تایمز گفت که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، چاره‌ای جز پذیرش هر توافقی که آمریکا در مورد آن با رژیم ایران مذاکره و نهایی کند نخواهد داشت.
دونالد ترامپ گفت زیرا «تصمیم‌گیرنده اصلی رئیس‌جمهوری ایالات متحده» است.
دونالد ترامپ به فایننشال تایمز گفت: «او (بنیامین نتانیاهو) هیچ انتخابی نخواهد داشت. این من هستم که تصمیم می‌گیرم. همه تصمیم‌ها را من می‌گیرم. او (نتانیاهو) تصمیم‌گیرنده نیست.»
به گزارش فایننشال تایمز، آقای ترامپ این اظهارات را اندکی پس از آن مطرح کرد که جمهوری اسلامی در جدی‌ترین نقض آتش‌بس از زمان توافق آتش‌بس در اوایل آوریل، چندین موشک بالستیک به سوی اسرائیل شلیک کرد.
آقای ترامپ تأکید کرد که حملات موشکی جمهوری اسلامی تغییری در تمایل او برای به نتیجه رساندن مذاکرات میان آمریکا و حکومت ایارن ایجاد نکرده است.
او به فایننشال تایمز گفت: «این موضوع هیچ تأثیری بر توافق نخواهد داشت.»
ارتش اسرائيل به صدای آمریکا گفت که جمهوری اسلامی یازده موشک به اسرائيل شلیک کرد. ارتش اسرائيل پیشتر گفت که حملات موشکی جمهوری اسلامی را دفع کرده است.
در همین حال در واکنش به حملات موشکی جمهوری اسلامی، ارتش اسرائیل در بیانیه‌ای به صدای آمریکا گفت که رئیس ستاد کل ارتش اسرائیل، ایال زمیر، در حال ارزیابی وضعیت در مجمع ستاد کل است. ارتش اسرائيل به صدای آمریکا گفت: «نیروی دفاعی اسرائیل به محض صدور دستور، با قاطعیت به دشمن حمله خواهد کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76011" target="_blank">📅 02:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76010">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری تسنیم: "صدایی که دقایقی پیش در تهران شنیده شد مربوط به رعد و برق است و این صدا ارتباطی با پدافند یا موضوع نظامی نداشته است."
من هم پیام‌هایی گرفته بودم که بعدش با «ببخشید انگار رعد و برق بود» آپدیت شدند
.
زیاد پیش میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76010" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
