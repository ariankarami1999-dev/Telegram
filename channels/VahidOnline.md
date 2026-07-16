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
<img src="https://cdn1.telesco.pe/file/cK_1IPQgnb8RIQdiZaGcAsZcOB4c2nkdkT3inUgAu9xqBxFliDbaDAsJGf5m8t2UhZLMHuKbSJlW3LjePJExrW9VqsKX2LBB1iNtmaqor_Ofd-7qyjiYXBxemR9nvN3uqNxQ5CR4kRgr7nIEA7aY2l0n8tmGuBbNKNzxStTa49LMT03aRQTWB59MKyJ3ysI-o1rs_2f8-ahXEbfoZwCrkmhqvJbUrPPwHqoQN7Ukx8wDPbND8Rg8AKYYlFKU7795cqBkS2W5Xo-Ch5926sh_vbRRl2GwuoK87d9aHOwpqsccN2Rz5URgeft46iY0jpbJsSEw0ZCAj4ZKdQgwZstgNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.38M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 14:20:03</div>
<hr>

<div class="tg-post" id="msg-77142">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81194af4f8.mp4?token=WHrEAwTTQoexbVOe9_Em4yiqS2XNJVaMSuJldmpeodEUUPfyEOh8LfVkvEnT-Sd2-Th54XkhqM_QB6-JTmsewegNVvQxHckXKZH4UGAONdZh5rWKfKU-gCKceWf56u0sjEhVNjBefdY5l1Lw0wYCi04082FIfnErvA2Djhz3TwWoXV55PzmJVB3g0d4LgulHyHLVqPISHTVS-CxgMpKVCT2dVFKJ7bWl-cpAvk92b2Wuqj35roeHxObxznjKfFOhbL5ODCAO-WOFIy7kH12d5dOd_lmzIJKJTXaB5f9bQRAHzUBXizeL6RdfYzCUZbKYgMAXHqLaXZtmhCJBQo89TA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81194af4f8.mp4?token=WHrEAwTTQoexbVOe9_Em4yiqS2XNJVaMSuJldmpeodEUUPfyEOh8LfVkvEnT-Sd2-Th54XkhqM_QB6-JTmsewegNVvQxHckXKZH4UGAONdZh5rWKfKU-gCKceWf56u0sjEhVNjBefdY5l1Lw0wYCi04082FIfnErvA2Djhz3TwWoXV55PzmJVB3g0d4LgulHyHLVqPISHTVS-CxgMpKVCT2dVFKJ7bWl-cpAvk92b2Wuqj35roeHxObxznjKfFOhbL5ODCAO-WOFIy7kH12d5dOd_lmzIJKJTXaB5f9bQRAHzUBXizeL6RdfYzCUZbKYgMAXHqLaXZtmhCJBQo89TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در پاسخ به پرسشی درباره تهدیدهای مطرح‌شده از سوی ایران علیه جانش، گفت که به این موضوع «اصلا فکر نمی‌کند».
او در گفتگو با فاکس بیزینس تاکید کرد: «اگر به این مسائل فکر کنم، دیگر نمی‌توانم مؤثر باشم.»
ترامپ افزود این کار را دیگران انجام می دهند و به نظرم در این زمینه عملکرد خوبی دارند و تاکید کرد خودش به این موضوع اصلا فکر نمی‌کند.
@
VahidOOnLine
او همچنین تاکید کرد که می‌تواند سپاه پاسداران را به همان شیوه‌ای از بین ببرد که در دوره نخست ریاست‌جمهوری خود داعش را در عراق و سوریه شکست داد.
ترامپ گفت: «ما در وضعیت خوبی خواهیم بود. آن‌ها تضعیف شده‌اند. تسلیحاتشان ۹۱ درصد کاهش یافته است. توان پهپادی آن‌ها به‌شدت کاهش یافته است. هنوز مقداری دارند، اما زیاد نیست. ظرفیت تولیدشان کاهش یافته است. پرتابگرهای راکتی و پرتابگرهای موشکی آن‌ها به‌شدت کاهش یافته‌اند. موشک‌هایشان هم به‌شدت کاهش یافته‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77142" target="_blank">📅 09:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77141">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیم ساعت از
سه ساعت
گفت‌وگوی جی‌دی ونس با جو روگن، بخش مرتبط با ایران
جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با جو روگن از آنچه «جنگ‌طلبان» در آمریکا و دیگر کشورها خواند، انتقاد کرد و گفت این افراد با صرف هزینه‌های گسترده تلاش می‌کنند مذاکرات دولت دونالد ترامپ با جمهوری اسلامی را به شکست بکشانند و افکار عمومی آمریکا را تغییر دهند.
ونس با دفاع از رویکرد دولت ترامپ، تاکید کرد دیپلماسی برای حل بحران حمله‌ها به کشتی‌رانی در تنگه هرمز ضروری است و گفت در کنار اقدامات نظامی، گفت‌وگو تنها راه رسیدگی به این بحران است.
@
VahidOOnLine
بیشتر متن زیرنویس ویدیوی بالا:
telegra.ph/Vance-07-16-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77141" target="_blank">📅 06:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77140">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/858e125a28.mp4?token=kt1YBLIeldKBoQVUd6hpL9FS6PX5IanwaWHEFuuxdCAcDRI2fvHuo8p2EiRjdNuj_PFZvgAG8Lh7_owz53jmIqX_D6Y0BzOn7NkhS2tAlSvwQFDSBfZCjIumED_d7FE2d7-An4vDK_Tf4YqEnVzp3_tWRZBE8B2Ase8lbKLDvMQxZ_Su12ko60A4cb3fb-EbY_6j1-5qOrmxaPOY8gExzMfarGP57Jgn1sziSX2XUiGWE7FYjFnQJVdgSGnhli8lKs8bYf1VUVCJcd22jV8LATzLTB1nFbUKAbzN0YeClshQeWLOMVwbPVQDrXEoo45-cNAjm2pK5pG3gOOjwUYJ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/858e125a28.mp4?token=kt1YBLIeldKBoQVUd6hpL9FS6PX5IanwaWHEFuuxdCAcDRI2fvHuo8p2EiRjdNuj_PFZvgAG8Lh7_owz53jmIqX_D6Y0BzOn7NkhS2tAlSvwQFDSBfZCjIumED_d7FE2d7-An4vDK_Tf4YqEnVzp3_tWRZBE8B2Ase8lbKLDvMQxZ_Su12ko60A4cb3fb-EbY_6j1-5qOrmxaPOY8gExzMfarGP57Jgn1sziSX2XUiGWE7FYjFnQJVdgSGnhli8lKs8bYf1VUVCJcd22jV8LATzLTB1nFbUKAbzN0YeClshQeWLOMVwbPVQDrXEoo45-cNAjm2pK5pG3gOOjwUYJ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام،‌ ترجمه ماشین:
تازه‌ترین موج حملات آمریکا علیه ایران پایان یافت
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) موج حملات شامگاهی علیه ایران را ساعت ۹ شب به وقت شرق آمریکا [۴:۳۰ تهران] در ۱۵ ژوئیه پایان داد.
نیروهای آمریکایی مراکز فرماندهی، مواضع پدافند هوایی، توانمندی‌های موشکی و پهپادی و تأسیسات نظارت ساحلی ایران را مورد حمله قرار دادند تا توانایی ایران برای تهدید دریانوردان بی‌گناهِ خدمه کشتی‌های تجاری عبوری از تنگه هرمز را بیش از پیش تضعیف کنند. سنتکام برای حمله به مواضعی در چندین نقطه، از جمله بندرعباس، از مهمات هدایت‌شونده دقیق استفاده کرد.
پیش‌تر در صبح امروز، نیروهای آمریکایی طی یک موج حملات ۹۰دقیقه‌ای، مواضع دفاع ساحلی و موشک‌های کروز در جزیره تنب بزرگ را هدف قرار دادند.
ارتش ایالات متحده به دستور فرمانده کل قوا، ایران را پاسخ‌گو می‌کند.
CENTCOM
منابع حکومتی:
اطلاعیه شماره ۱۵
🔸
رادار پیش‌هشدار سامانهء C-RAM در پایگاه علی السالم کویت و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا آماج حملات ترکیبی قرار گرفت‌
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
مردم غیور و بپاخاسته ایران!
🔹
در پی تجاوزات شب گذشته دشمن به نقاطی از سواحل و شهرهای جنوبی کشور، فرزندان دلاور و قهرمان شما در نیروی دریایی و هوافضای سپاه، در موج هشتم عملیات نصر ۲ بارمز مبارک یا زینب کبری (س)، در یک عملیات ترکیبی با استفاده از توان موشکی و پهپادی خود، رادار پیش‌هشدار سامانهء C-RAM را در پایگاه علی السالم و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا را آماج حملات خود قرار داده و درهم کوبیدند.
🔹
بار دیگر به مردم شریف کویت یادآوری می‌کنیم که این جنایات توسط آمریکا با استفاده از خاک شما علیه ایران مسلمان انجام می‌شود.
🔹
از شما برادران و خواهران مسلمان انتظار داریم کشورتان را از وجود متجاوزان پاک کنید و با عمل به وظیفه اسلامی، شرف و عزت تاریخی خود را حفظ نمایید.
سپاه درباره
صدای پاکدشت
: پدافند بود. هیچ اصابتی نبود
🔸
اطلاعیه سپاه حضرت سیدالشهدا علیه السلام استان تهران درباره صدای شنیده‌شده در پاکدشت؛
روابط عمومی سپاه حضرت سیدالشهدا علیه‌السلام استان تهران:
🔹
دقایقی پیش صدای انفجاری در محدوده شهرستان پاکدشت شنیده شد که بررسی‌های میدانی و نظامی نشان می‌دهد این صدا ناشی از عملکرد سامانه‌های پدافند هوایی در منطقه پارچین بوده است.
🔹
ضمن تکذیب قاطع ادعاهای برخی رسانه‌های معاند و جریان‌های سلطنت‌طلب در خصوص وقوع هرگونه اصابت، هیچ‌گونه حادثه یا اصابتی در منطقه صورت نپذیرفته و فعالیت‌های مذکور در راستای آمادگی و عملکرد پدافند هوایی بوده است.
🔹
از مردم عزیز ضمن حفظ آرامش، اخبار مربوط به این رویداد را تنها از طریق رسانه‌های رسمی دنبال کرده و از توجه به شایعات هدفمندِ رسانه‌های بیگانه که با هدف ایجاد التهاب و ناامنی روانی منتشر می‌شوند، خودداری کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77140" target="_blank">📅 04:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77139">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پیام‌های دریافتی از تهران
احتمالا همگی درباره صدای پدافند:
صدای پدافند میاد ساعت ۳:۵۱ یوسف اباد تهران
تهران انفجار 3:50
پدافند تهرن داره کا میکنه ۳و۵۱
تهران یوسف اباد صدای پدافند
نارمک صدای پدافند ۳:۵۱
سلام وحید جان مرکز تهران صدای پدافند میاد الان شروع شد
.
تهران صدای پدافند
همین الان صدای پدافند شرق تهران
سلام خرم اباد صدای یدونه انفجار اومد
تهران مرکز شهر صدای پدافند
۳:۵۰
البته زیاد نبود، چندتا بود
وحید ساعت ۳:۵۱تهران نارمک صدای پدافند
داداش تهران سید خندان صدا پدافند ساعت ۳:۵۰
پدافند تهران میدون شهدا داره کار میکنه
صدای پدافند ساعت 3:51 مرکز تهران
تهران سهروردی صدای انفجار از دور تقریبا
صدایی شبیه پدافند از دور شنیده میشه، اختیاریه، ۳:۵۱
تهران عباس آباد پدافند ساعت ۳:۵۰
پاسداران تهران صدای پدافند
سلام همین الان پدافند سمت میدان امام حسین فعال شد
۳:۵۱ دقیقه
من ميرداماد تهران هستم
الان دارن ميزنن
٢ تا صداي بلند و بعدش ٥-٦ تا  كوچكتر
سلام.تهران پیروزی صدای پدافند ۳:۵۲
وحید سمت سهروردی صدا پدافند شنیدیم 3:52
سلام سمت سیدخندان همین الان صدای انفجار شنیده شد
سلام ! ساعت ۳:۵۱ دقیقه سمنان صدای جنگنده میاد
الان ساعت ۳:۵۱ صدای سه تا انفجار اومد تهران
سمت غرب صدا شنیدم
وحیدجان سلام الان ۳:۵۲ تهران محله نیروهوایی صدای پدافند
مرکز تهران. یه صدای انفجار اومد (دور بود) بعدش صدای پدافند ۳:۵۱
سلام وحید جان شرق تهران سمت فدک ۳:۵۲ صدای پدافند به گوش رسید نمیدونم کجاست
سهروردی سه تا صدای بلند متوالی اومد ولی منشأ رو نمیدونم و دور بود انگار
سلام وحید جان غرب تهران سمت فرودگاه صدا پدافند و جنگنده میاد
فعال شدن پدافند در تهران محله دبستان ساعت ۳:۵۰ بامداد
سلام ۳:۵۲ دقیقه سمت گیشا هم صدای پدافند میاد
من میدان سپاهم
صدای انفجار یا پدافند! من تشخیص نمیدم از دوره
ساعت ۳:۵۰
سلام‌وحید جان سمت امیر آباد شمالی صدا پدافند داره میاد
سلام وحید جان تهران شریعتی سمت میرداماد صدای پدافند اومد نزدیک نبود خیلی
سلام وحید جان ساعت ۳:۵۱ دقیقه میدان شهدا چهار پنج بار صدای پدافند اومد
صدا پدافند بود فکر کنم
تهران محدوده خیابون امام خمینی
ساعت ۳:۵۰
وحید سلام توانیریم، صدای پدافند ونک دو دقیقه پیش
سلام تهران الان ساعت 3:53 هم صدای پدافند میاد هم روی اسمون نورش معلومه
سلام وحیدجان سمت شرق پدافند زدن اما قبلش یه صدای بلندی اومد اما نمیدونم زدن یا نه چیزی دیده نمیشه
3:50صدای پدافند شرق تهران
سلام ، غرب تهران (پونک) صدای انفجارها پشت هم و خفیف از دور میاد
سلام وحید جان
شرق تهران الان انگاار صدای انفجار اومد . مطمئن نیستم چون خواب بودیم ولی شبیه صداهای اسفند ماه بود
ساعت ۳.۵۱ صدای پدافند تهران خ شریعتی
کوتاه بود
سلام وحید جان الان ساعت ۳.۵۴ صبح ۲۵ تیرماه صدای پدافند گیشا
تهران شوش پدافند ٣:٥٣
غرب تهران 3:51 چندتا انفجار پشت سرهم شنیدیم
الان باز شروع شد ساعت 3:56
همین الان ساعت ۳ و ۵۵ دقیقه دوباره صدا اومد سمت هفت تیر
۳:۵۶ دوباره صدای پدافتد یا شلیک سمت نارمک
۳.۵۶ امیراباد شمالی دومین بار پدافند
از اختیاریه، ۳:۵۶؛ چند تا صدا شنیده شد با صدای قبلی فرق داره که پدافند بود [پدافندها انواع متفاوتی هستند با صداهای متفاوت]
وحید ۳:۵۶ شرق تهران صدای پدافند - تو ۱۰ دقیقه گذشته دومین باره
تهران شمس آباد  نزدیک کلانتری مجیدیه همینطور صدای پدافند میاد
سلام مجیدیه شمالی صدای پشت سرهم پدافند میاد  حدود ۴ صبح
سلام وحید جان. مرکز تهران صدای پدافند مکرر اومد.
وحید جان ، ساعت ۳:۵۱ دقیقه بامداد اتوبان حقانی صدای پدافند بسیار کوتاه
داداش همین الان  ۳:۵۵ حدود ۱۰ بار صدا امد  ولی زیاد نزدیک نبود یوسف اباد
+ ده‌ها پیام مشابه دیگر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77139" target="_blank">📅 03:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77138">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پیام‌های دریافتی:
خرم آباد صدای انفجار
سلام ساعت 3:48 صدای انفجار در خرم آباد
وحیدخان از بروجرد انگار موشک زدن صدای غرش سریع و شدید تو آسمون اومد
خرم آباد ۳.۴۷ صدای انفجار یهویی و نسبتا شدید
خررم آباد به شدت صدای انفجار اومد
کل ساختمونمون لرزید
سلام وحیدجان ۳:۴۷ خرم اباد صدا اومد
سلام وحید جان خرم اباد لرستان ساعت ۳ و ۴۷ دقیقه انفجار
🔄
دوباره زد خرم اباد رو ۳:۵۷
سلام وحید جان همین الان صدای افنجار اومد دوباره خرم اباد
سلام وحید جان بروجرد الان ی صدای مهیب امد. من هدفون داشتم درست متوجه نشدم بعدشم صدا موشک یا جنگنده امد
آقا وحید بروجرد صدای خیلی قوی صدای واقعا عجیب و قوی،واقعا نمی‌دونم انفجار بود یا دوباره شلیک بالستیک،صداش از رعد و برق بدتر بود
خرم آباد دوباره صداي انفجار
دومین انفجار در خرم آباد ساعت 3:57
بروجردو ۳:۵۵ زدن
انفجار خیلییی قوی
سلام وحید جان از بروجرد صدای شدید و یهویی اومد (ساعت ۳:۵۰ صبح)
طبق تجربه، صدای شلیک موشک بود
داداش الشتر لرستان دوبار صدا اومد معمولا از اینجا موشک پرتاب میکنن یبار 3 و 47 دقیقه یبارم حدودا 3و  56 دقیقه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77138" target="_blank">📅 03:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77137">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان تو ارومیه صدای انفجار اومد از سمت کوه های اطراف شهر
همین الان یه صدای انفجار با لرزش خارج از شهر اومد (ارومیه) بعدش با صدای بلند مثل صدای موشک یا جنگنده تو هوا
ارومیه صدای انفجار اومد دقایقی پیش با صدای جنگنده [احتمالا صدای موشکه]
خارج از شهر ارومیه نزدیک مرز صدای جنگنده میاد همین الان
سلام وحیدجان، دوباره از تبریز موشک زدن
سلام وحید. الان ۳:۴۶ از تبریز موشک زدن
۳:۴۶ دقیقه همین الان یه موشک از طرفای اسکو آذربایجان شرقی بلند شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77137" target="_blank">📅 03:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77136">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">استان تهران، صدای پدافند:
سلام وحید جان الان ساعت ۰۳:۲۷ صدا انفجار اومد سمت پاکدشت
اقا وحید همین الان پدافند پاکدشت کار کرد بدجور
صدای انفجار پاکدشت ۳:۲۵
۳:۳۰ سمت پاکدشت داره صدا میاد
سلام صدای انفجار و پدافند حدود دو سه دقیقه پیش داخل پاکدشت
پارچین و پاکدشت انفجار سنگین
خیلی صدا شدید بود
فکرکنم پارچینو زد
۳/۳۰ چندین انفجار در پارچین
سلام وحید
ساعت۳:۲۰ پاکدشت صدا پدافند اومد شدید
دوباره الان ساعت ۳:۳۰ داخل پاکدشت صدا انفجار میاد
دارن میزنن پارچین رووووو
صدای پدافند میاد
۸ بار صدا اومد
سلام وحید جان پدافند پارچین فعال شد همین الان و صداش پاکدشت شنیده شد
سلام دوتا ویکی الان3.31دقیقه.صداتا قرچک ورامین امد
البته اول چهارپنجتا انفجار شنیدم که احتمالا انفجار گلوله.های ضدهوایی بود
شریف اباد پشت پارچین صدا شدید پدافند میاد ۳:۱۸
ما صبح امتحان نهایی ریاضی داریم یه دوازدهمی همینجوری از استرس دارم میمیرم
و یه صدای انفجار اومد همین الان پاکدشت چند بار 3:30
صدای پدافند میاد آقا وحید شدید
🔄
همین الان پدافند رگباری سمت پاکدشت ۳:۴۳
همچنان ۳:۴۲ ضد هوایی شدیدا فعاله
ساعت ۳ و۴۳ دوباره فعالیت شدید پدافند توی پاکدشت
🔄
دوباره صدای پدافندا شدید تر شد
از سمت پارچینه
۳:۴۵ شدیدتر
دیگه همینجوری هست
هر موقع تموم شد میگم
😂
صدای جنگنده ساعت ۳ و ۴۶ دقیقه
بازم انفجار شدید خرم آباد ۳.۵۷
سلام وحید  دوباره خرم آباد زدن ساعت ۳:۵۷
خرم آباد بازم صدای انفجار اومد ساعت 3:56
انفجار مجدد خرم آباد خیلی شدید بود
تهران صدای انفجار سمت آزادی الان
وحید جان 3.48صدای شدید خرم آباد دو مرتبه به فاصله 10دقیقه کل ساختمون لرزید
لرستان. الشتر(سلسله)
صدا و لرزش شدید اومد نمیدونم اونا زدن یا ما موشک شلیک کردیم
3.50
دوباره 3.56 همون لرزش و صدا..
لرستان الشتر وحشتناک دارن میزنن
خرم اباد
سلام وحید جان ساعت حوالی 3:55 از بر‌وجرد موشک زدن صداش خیلی بلند بود
آپدیت: منابع حکومتی
فرماندار پاکدشت: صدای دقایقی پیش در شهرستان پاکدشت به علت فعالیت سامانۀ پدافند هوایی بوده است.
روابط‌عمومی سپاه سیدالشهدا(ع) دربارۀ صداهای شنیده شده در پاکدشت: این صداها صرفاً ناشی از عملکرد پدافند هوایی بوده و هیچ اتفاق یا اصابتی رخ نداده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77136" target="_blank">📅 03:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77135">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌‌های دریافتی تایید نشده:
۳:۱۵ سمت «شهرک صنعتی سمنان» یک تک صدای انفجار بزرگ اومد.
سمنان، دو موج خیلی شدید انفجار اومد
جوری که خونه لرزید
ولی منشاش نا مشخصه
همزمان با پخش اذان از مساجد هم بود وحید جان
سلام وحید جان 3:18 هست ساعت و صدای بلندی در شهر سمنان اومد
آپدیت: منابع حکومتی
مردم در بخش‌هایی از سمنان صدای انفجار شنیدند.
استان مرکزی:
خنداب دوتا انفجار
آقا وحید 3تا انفجار سنگین خنداب
آپدیت: منابع حکومتی
معاون استاندار مرکزی: یک منطقه خارج از محدوده شهر خنداب ۲ بار مورد حمله پرتابه‌های دشمن قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77135" target="_blank">📅 03:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77134">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLgo8YhOETKjRyM4fcK-d3p9aWlKK6WSNnmmP22ceIUsOODvay1MgKR9KxsUMzn_td7hj6zmQR8xb9eCtOPgtvi6vbqymu98ciSHrDETMKcx0CG-X5y5HNZXnK7vsygT4JshsO9XeZcYvoUenbMX6FsoWDhlEVqpZuamQFgPR9635cVC8gbQu0CpKCuwBC57AwAIQ0SOwIN0Dt7PmfXnH9JdqshlG_YG1aBvBoIy46ZX1jricGKP4qCLdpXfCP7BAZ58MsZ9Ycrgvxk8bqPttMUtxBlgVOJDC4vGRnIClzDT0E0BEc14CvHAsnce_a_IOlHxChFGfovfaEq17b_XCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران یک شهروند بازداشت‌شده آمریکایی را آزاد کرد
پست ترامپ، ترجمه ماشین:‌
ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴، در دوران «ریاست‌جمهوری» جو بایدن خواب‌آلود، به‌ناحق بازداشت شده بود، اجازه داده است کشور را ترک کند.
او اکنون به سلامت از ایران خارج شده و حالش خوب است.
ایالات متحده آمریکا از این حسن‌نیت ایران قدردانی می‌کند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
گویا اسمش "دنا کراری" است:
twitter
آپدیت:
جرد گسنر، وکیل حقوق بشری مستقر در واشنگتن، در بیانیه‌ای
گفت
«من خوشحالم و با هیجان اعلام می‌کنم که موکلم، شهروند آمریکایی دنا کراری، که از دسامبر ۲۰۲۴ به دلیل اتهامات بی‌اساس در ایران گرفتار شده بود، اکنون آزاد است.»
او افزود: «این اتفاق بدون تلاش‌های فوق‌العاده و پیگیرانه رئیس‌جمهوری [آمریکا،‌] دونالد ترامپ ممکن نبود. دنا اکنون در امنیت است و در حال بازگشت به ایالات متحده آمریکا است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77134" target="_blank">📅 02:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77133">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس الان ساعت ۱.۲۶ دو تا صدای انفجار
سلام
بندرعباس ۱:۲۷ پایگاه هوایی ۲ تا انفجار شدید
درود وحید جان
همین الان شرق بندرعباس پایگاه هوایی صدای دو تا انفجار اومد
سه تا انفجار بندرعباس
احتمالا یکیش پایگاه هوایی
سلام وحیدجان چند انفجار سنگین در مسن لرزش شدید برقم قطع شد نیم ساعت قبل
جزیره قشم
یکی دیگه الان خورد 1.29
🔄
فعالیت پدافند بندرعباس ساعت ۱.۵۱
لرزش پنجره و صدای پدافند شرق بندرعباس شنیده میشه
فعال شدن پدافند بندرعباس همین الان
درگیری پدافند هوایی تو بندرعباس نزدیک پایگاه هوایی
فعال شدن پدافند بندرعباس همین الان
پدافند توی محله [...] بندرعباس جاساز شده
بین خونه های مردم ، محله [...]
وحید جان اینو کامل بفرست عزیزم
🔄
صدای بسیار بسیار شدید بندرعباس
دیوار صوتی شکست
یه صدای وحشتناکی از آسمون اومد
۱و ۵۸ بندرعباس
همین الان مجددا ارزش و صدای وحشتناک، ۱و ۵۹
نمیدونم انفجار بود یا پدافند ۱:۵۸
صداش شدید بودسمت پایگاه هوایی
وحید جان صدای عجیب تو آسمون شرق شهر بندرعباس عین غرش ولی منبع نا معلوم
وحید سلام بندرعباس ۱:۵۷ ی صدای خیلس بلند طولانی اومد انگار ی چیزی بخورد کنه و تخریب بشه
🔄
انفجار شدید ۲:۲۱
شرق بندرعباس ۰۲:۲۰ زدن شدید
بندرعباس انفجار سنگین
بازم پایگاه هوایی بندرعباسو زدن
شدت انفجار خیلی بالا بود ساعت ۲.۲۰
الان ساعت ۲:۲۱ گلشهر جنوبی بندرعباس صدای انفجار بسیار شدید،مثل غرش
سلام بندرعباس ۲:۲۰ سمت فرودگاه صدای بسیار مهیب
سلام ۲:۲۰ انفجار مهیب بندرعباس
صدای انفجار شدید اومد بندر وحید ۲:۲۱
🔄
۳ ۴ تا انفجار دیگه ۲ و ۲۶
وحید ۲ انفجار سنگین همین الان پایگاه هوایی بندرعباس
سلام ۲:۲۶ انفجار مهیب بندرعباس
بندرعباس پشت سر هم داره صدای انفجار میاد الانم 2 تا 2:27
۲:۲۷ دوباره انفجار
این دفعه دورتر یا ضعیف‌تر
بندرعباس دو صدای دیگه ۲:۲۷ بازم فرودگاه یا پایگاه هوایی
صدای قبلی شدید تر بود
سه تا انفجار پایگاه هوایی بندرعباس
ساعت ۲.۲۷
سلام وحید جان 2:27 بندرعباس صدای دو انفجار
الان بندر دوباره دوتا صدا ۲:۲۶ ، اولی زد دومی انگار پدافند بود
2.26 بندرعباس
دو انفجار شدید به فاصله ۴ثانیه در منطقه گلشهر شنیده شد.
منابع حکومتی:
استانداری هرمزگان: در ساعت ۲:۲۰ نقطه‌ای در حوالی بندرعباس مورد اصابت حملات دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77133" target="_blank">📅 01:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77132">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S8pRM0HMzTPL9qZ_Gae_v1KiEpXX4Ote-liIkf6IFCC_qs5OUYQX45H7bRTlXd4KzuUmwqsOW7inxwc7Ug4AO2jljIdnRsMavSc4u9nn75ezCCuk1IPzzpz0UqW8yMow92DvOEEUgpO1pRvld8-D1i-TpCsyA-po4-ffteFd65nEaMztXZf51le33qnVD7Eot2M8IA0YtLUnOA19EYxxpxnobYc8vNOiUx544ZODPLVpNr0CeLSABryyodzUx_NpJOPpLBoknPrfHRFW6jZ0mOgt9kxyfodBTt_lrZjlTyi5GRbywgJ8zxbXOFyPl-Peh8MHoZtrPh69Nc6EHJsvgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز چهارشنبه ۲۴ تیر در سخنرانی خود در «دانشکده جنگ ارتش ایالات متحده» در کارلایل پنسیلوانیا، گفت ایران «به‌زودی شکست خواهد خورد.»
او با اشاره به حملات اخیر آمریکا علیه ایران گفت با وجود آنچه «عملیات نظامی» خواند، بازار نفت دچار جهش شدید نشده و برخلاف پیش‌بینی‌ها، قیمت‌ها افزایش چشمگیری نداشته است.
ترامپ افزود بسیاری انتظار داشتند قیمت نفت تا ۳۵۰ دلار در هر بشکه افزایش یابد، اما این رقم در حال حاضر حدود ۷۹ دلار است و حتی چند روز پیش به ۶۸ دلار نیز رسیده بود.
رئیس‌جمهوری آمریکا همچنین گفت اقداماتی که به گفته او در واکنش به «عدم پایبندی ایران» انجام شده، محدود بوده و در صورت آرام شدن شرایط، قیمت نفت ممکن است به حدود ۵۵ دلار یا حتی کمتر کاهش یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77132" target="_blank">📅 00:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77131">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b248f4653d.mp4?token=EtcIdkqtqDyp3gv7MbzIJgpUsp4sGlRWc6OCUG_RzJyz3Oo_6X7W-NOUMfDIYmFdjO7bOYhmju_Dh7wJnSAkn-6TV6TOEw4qwz34IMY_ejGdv8jJnoaN-099Y21anvSRycSg2GS3mxpq5e4aNr-6Y-MaR3ms-EkZx4ONn9iz8UaSwl4bkFkbf5f3L-u85uPANjNra7fM36vLkKtt5Xu3WaXZeku3b_DHHFnoY918jkOjnAWzvJC2tUvqxXM38Wp3s6hE76lCU65y7Osb-qIFRbX81RwQiVJeHpkzqy-bU2AD5mA_cCREBSzF-byhnrViZPKeND5_MSfDH3wd_nyxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b248f4653d.mp4?token=EtcIdkqtqDyp3gv7MbzIJgpUsp4sGlRWc6OCUG_RzJyz3Oo_6X7W-NOUMfDIYmFdjO7bOYhmju_Dh7wJnSAkn-6TV6TOEw4qwz34IMY_ejGdv8jJnoaN-099Y21anvSRycSg2GS3mxpq5e4aNr-6Y-MaR3ms-EkZx4ONn9iz8UaSwl4bkFkbf5f3L-u85uPANjNra7fM36vLkKtt5Xu3WaXZeku3b_DHHFnoY918jkOjnAWzvJC2tUvqxXM38Wp3s6hE76lCU65y7Osb-qIFRbX81RwQiVJeHpkzqy-bU2AD5mA_cCREBSzF-byhnrViZPKeND5_MSfDH3wd_nyxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکایی یک شناور متخلف را در خلیج [فارس] از کار انداختند
تامپا، فلوریدا — نیروهای آمریکایی در ۱۵ ژوئیه، در اجرای تدابیر محاصره دریایی علیه ایران، یک نفتکش بدون محموله را که تلاش داشت به‌سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند.
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) مشاهده کردند که نفتکش «بلما» (M/T Belma) با پرچم کوراسائو، در آب‌های بین‌المللی به‌سوی جزیره خارک در حرکت است. این شناور تجاری هنگام تلاش برای نقض محاصره آمریکا، چندین هشدار را نادیده گرفت. یک هواپیمای آمریکایی با شلیک موشک‌های هلفایر به دودکش کشتی، آن را از کار انداخت. این کشتی دیگر به‌سوی ایران در حرکت نیست.
نیروهای آمریکایی در ساعت ۴ بعدازظهر به وقت شرق آمریکا در ۱۴ ژوئیه، محاصره دریایی شناورهای در حال تردد به بنادر و مناطق ساحلی ایران یا از مبدأ آن‌ها را از سر گرفتند. در نخستین ۲۴ ساعت اجرای محاصره، سنتکام مسیر دو شناور تجاریِ مطیع را تغییر داد و یک شناور متخلف را از کار انداخت.
نیروهای آمریکایی همچنان هوشیار و آماده‌اند تا از رعایت کامل محاصره اطمینان حاصل کنند.
CENTCOM
سنتکام به جای «خلیج فارس» چیز دیگری نوشته.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77131" target="_blank">📅 00:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77129">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c3872dd08.mp4?token=CCNfFAmol8Jhia8yMLDyQP0mnbfb3kHGIijdsVtr2E88M6-qVQrIp_gNZy7p_RzuvWkIoNACXuYY6XPuAIAF5UJJE_uo2dIPtW-QNw6f8IOP7gBj_gudpewKQJKYcqpsNNBWlGAQKxVrXbtvVjmECjqJRRwSHg1UwAtoNG3bIwTyivahZdrQ9_eFc2peKJFRsZRotw9RFGkXD0mdHJ1NTZTqJ_JuX-AbYzAjhtonzxqvb9UqXolwCnmmnacyKZAhzKtonZ73HVa8XqZ8HFTyeuQAke7hgveJ-9UcOfEnv4kQ4pe6awqV43uFZbI4E_tbkeI11YScgV2RSggSe_zp4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c3872dd08.mp4?token=CCNfFAmol8Jhia8yMLDyQP0mnbfb3kHGIijdsVtr2E88M6-qVQrIp_gNZy7p_RzuvWkIoNACXuYY6XPuAIAF5UJJE_uo2dIPtW-QNw6f8IOP7gBj_gudpewKQJKYcqpsNNBWlGAQKxVrXbtvVjmECjqJRRwSHg1UwAtoNG3bIwTyivahZdrQ9_eFc2peKJFRsZRotw9RFGkXD0mdHJ1NTZTqJ_JuX-AbYzAjhtonzxqvb9UqXolwCnmmnacyKZAhzKtonZ73HVa8XqZ8HFTyeuQAke7hgveJ-9UcOfEnv4kQ4pe6awqV43uFZbI4E_tbkeI11YScgV2RSggSe_zp4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی با شرح: 'پاسگاه احمد ریزه
#چابهار
، شهرک بهار ، جاده‌ی رمین و چابهار' در سیستان و بلوچستان
پیش‌تر هم‌زمان با آغاز حملات آمریکا پیام‌هایی از شنیده شدن صدای چند انفجار در این منطقه دریافت کرده بودم.
چهارشنبه ۲۴ تیر ساعت ۲۲:۳۸
#Iran
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77129" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77128">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWJ2V6eZoalMkt8qg1MzvW_SkmogxdOtQXwTYG_GpcjlSc2YXYUaDokUH42jOVud-TR6GHGpr6ipLF4ESQOXkjPEpefF99QpFBpDlRjvrcEEBtpDE9m8y8h1ba2sMLGYMek0S9A6AgEoS-0pfPXC_hffNTaiXD6q4DaOKVRWQUiAtyAtkLNye-S5cc3JxVwRscQ5gMrux8SSbq_pEP8axb5jzK-NGeN9FnJgJRdP8FMauYxoRgv6cEycHDIsq9BwOr8l2hlTLltuNhLp1z5NeLGKaefZrTXOD8qokKAppHMNaXS1bFB4ZZGToOW107PGQhrgx9ahjbjnm7IvI9NNGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های داخلی ایران از شنیده شدن صدای انفجارهایی در اهواز و چابهار خبر داده‌اند، اما تاکنون جزئیاتی درباره علت این انفجارها یا اهداف احتمالی حملات منتشر نشده است.
رسانه‌های ایران به نقل از استانداری هرمزگان از انفجار در شهر بندرعباس خبر داده‌اند. برخی از گزارش‌ها نیز حاکی از اصابت به شهر راسک در نزدیکی چابهار است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77128" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77127">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ۲۲:۵۷ دوباره انفجار
یکی دیگه وحید 10:57 بازم سمت گلستان
دوباره اهواز رو زد ۲۲:۵۷
بازم سمت گلستان
۲۲:۵۷ گلستان اهواز بازم انفجار کل خونه لرزید
تو خونه میلرزیم خونها میلرزن
همین الانم دوباره زدن ۲۲:۵۷
اهواز ۲۲:۵۷ پشت سر هم ۳ تا سمت گلستان و کوی مجاهد خیلییییی نزدیک
انفجار شدید ۲۲:۵۸ اهواز
اهواز دوباره زد شد پنج تا
همین الان دوباره فکر کنم واسه 7-8 امین بار بود واقعا از همشون خیییلیی شدیدتر بود
اهواز ۲۲:۵۷ این هشتمین صدای انفجاری بود که شنیدم
۲ انفجار خیلی شدید همین الان
اهواز ساعت ۲۲:۵۷
دارن مداوم‌ اهواز  رو میزنن
سلام اهواز و سه چهار بار زدن آخرینش 10/58دقیقهصدای بلند که شیشه هالرزید
اهواز ۲۲:۵۸ یه انفجار دیگه.ما بهارستانیم صدا خیلی بلند بود
از ساعت ۱۰:۳۰ اهواز رو داره میزنه
🔄
الان باز گلستان زدن
بازم صدا انفجار ۱۱:۰۹ گلستان اهوا زشنیده شد
۲۳:۰۹ بازم انفجار گلستان اهواز
همین الان دوباره اهواز ۲ انفجار پشت هم ساعت ۲۳:۰۸
وحییییید ۲۳:۰۸ ۲تا پشت هم داره بقایی رو میزنه اونجا پادگانه
23:09 دقیقه خیلی بد زد
سلام ، اهواز سمت گلستان دوباره  ۲۳:۰۹ زدن
۲۳:۰۹ دوباره انفجار شدید اهواز
اهواز رو زدن دوباره
اهواز ساعت ۲۳:۰۹…سمت کیانپارس صدا شدید احساس شد.
وحید اهواز پشت پادگان بقایی و پادگان ملاشیه رو داره میزنه ۲۳:۰۷
ساعت ۲۳:۰۹ اهواز سمت گلستان صدای انفجار این چهارمین صدای انفجاره که میشنوم
اهواز همین الان دوباره انفجار داشت
نقاط مختلفی بوده و من دیگه نمیتونم تشخیص بدم دقیق که کدوم پایگاه بود، اما انفجار ها زیاده
تا ۲۳:۱۰ بالغ بر شش صدای انفجار شنیده شد. در اهواز هستیم. که جمله از صداهای روز گذشته بلندتر بودن.
اهواز ساعت 11:10 محدوده بهارستان* رو زدن
شش هفت بار دیگه هم از اهواز صدای موج انفجار رو حس کردیم. با سوت شروع مسابقه انفجار ها هم شروع شد
🔄
ساعت ۲۳:۱۶ موج بعدی پیام‌های مشابه درباره انفجاری دیگر رو دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77127" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77126">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i3MAXb4vGJ2upoMuSx2tR5QoF11n57uTtqe99WsCpv8Hpphsu7jte2_tmSxOVw24GJ4mnpiWX4rkVI5eoWhBvhYlp3qXEwOENyppGRwHOCI-KsTCMIEmhOK26plp6A8X4HxXWgLsfsCgwBgJe-B0o-9OMT3JvD_r8YWe31XtVBgXT3g-6W97eXyQVrjCDzUkKbQcacV_KtDQJ4P9Cf63hfHZyIJrLW1n6OC0UGHb6kiLLJo1syz1CAQDplFDzjau3AF2gY8VHkXNr7fDJV2OGeZ_QV9iRqt_oHK1QDzzolARpdlVkgKGY0o4vRmE9twbCoL7iILW_dR42iFseUpmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام، ترجمه ماشین:
ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ به وقت تهران]، نیروهای ایالات متحده عملیات دومین موج حملات امروز علیه ایران را آغاز کردند. این حملات توانمندی‌های نظامی ایران را هدف قرار می‌دهند که برای تهدید کشتی‌های در حال عبور آزادانه از تنگه هرمز به کار می‌روند؛ آبراهی بین‌المللی که برای تجارت جهانی حیاتی است. ارتش ایالات متحده به دستور فرمانده کل قوا، ایران را پاسخگو می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77126" target="_blank">📅 22:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77125">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/416beb8ba4.mp4?token=A4J4Wv2o-N-yvZ3BbrXo07AOuuzBGclkX7qOU0kJR-eh3g-JcbaTzD-OaiPjmu3rhB7j0UY36adhzR8fgvYJxpoAJozhH8IDeX_HTx-BNzLNOh0XmmHqMgu_XsppqscnQF9Gk78-E4rWRUrD6abWgwSuhickC16yj3LBes3MiPJhVfwBjXEVz4INWVS8A8J29rnoBr-YKdC4DmUo-ReR-E7Tfnkq85mMm876-DZkdqYYAgYeMoGtJmqzH1iHPnGkIKxlKluUF-pCFDfJUEQgoxj-TWt7DTWO4MJ8wku9zwELTxozuXQOYdZzUYN0BXCz2Fn_XT8rRXi-Rn3C-CUYXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/416beb8ba4.mp4?token=A4J4Wv2o-N-yvZ3BbrXo07AOuuzBGclkX7qOU0kJR-eh3g-JcbaTzD-OaiPjmu3rhB7j0UY36adhzR8fgvYJxpoAJozhH8IDeX_HTx-BNzLNOh0XmmHqMgu_XsppqscnQF9Gk78-E4rWRUrD6abWgwSuhickC16yj3LBes3MiPJhVfwBjXEVz4INWVS8A8J29rnoBr-YKdC4DmUo-ReR-E7Tfnkq85mMm876-DZkdqYYAgYeMoGtJmqzH1iHPnGkIKxlKluUF-pCFDfJUEQgoxj-TWt7DTWO4MJ8wku9zwELTxozuXQOYdZzUYN0BXCz2Fn_XT8rRXi-Rn3C-CUYXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: ویدیوی منتشر شده در منابع محلی
پیام‌های دریافتی:
اهواز ۲۲:۴۸، جنوب اهواز کامل لرزید
وحید جان الان زدن ۲۲ ۴۸ اهواز لشکر
۲۲:۴۸  خیلی شدید تر از قبلی ها صدا انفجار اومد
انفجاری وحشتناک ساعت ۲۲:۴۸ اهواز
وحید اهواز کوی مجاهدیم ۲۲:۴۸ دوتا خیلییییی نزدیک زد
دوباره 22.48 اهواز، این سنگین تر بود.
همین الان سمت گلستان اهواز انفجار
اهواز باز شروع شد این بار صدا از سمت لشکر ۹۲ میاد
انفجار اهواز ۲۲.۴۸
صدای وحشتناک انفجار اهواز
ساعت ۲۲:۴۹
خونه کامل لرزید
دوباره اهواز رو زدن ساعت ۱۱ و ۵۰
اهواز 22.50  دوباره
اهواز بازم زد ۲۲:۵۰
دوباره زدننن خیلییی نزدیک بود 22:48
صداش خیلی زیاد بود
براى دفعه چندم اهواز ساعت ١٠:٤٨ انفجار بسيار شديد، انگار تمومى نداره
سلام شب بخیر
همین الان  اهواز ساعت ۲۲:۴۹  صدا  اینقدر زیاد بود انگاری سنگر شکن بود سمت گلستان
ساعت ۲۲:۵۰
بکی دیگه هم زد همین الان  قشنک خونه ها میلرزه
ولی صدای هیچ جنگنده نمیاد
یکم پیش اهواز رو زدن فکر میکنم ۹۲ زرهی باشه
همین الان سمت گلستان اهواز انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77125" target="_blank">📅 22:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77124">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjsIrVZ_qZRybFYI2SdXtPnvaIA0BoVQ38ycBZjf33kjMk2fjTDlMpb8eMx9ikd766Vgj5rlN26fTiZmGeRhS4B35gWfpfcgGq-iAz7DkDEBbzcEaeV2A-uiLRLGJCMLYIGOpjNsww1f6Tx_PSWZK26GUN-5gxZcFszCs3d35Q2Ti4vDdjPKe8wyQ_mVoW8xFETC65Aj0gRA40f7LHdmVmDDdKizF9G0YBSpSBxN_kAucKn47hoHmjVtDKONvkDjLkow6AzZuIcVtfPe9EkC8fw5EWcACF9aUHElvX7NWKJzso1nnyENW5F64JcNB8FBAjHVrpIfS2w--t9fy6JvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه در پاسخ به پرسش خبرنگاران درباره این‌که آیا پیش از آغاز حملات آمریکا به پل‌های ایران، مهلتی برای تهران تعیین شده است، گفت که علاقه‌ای به تعیین ضرب‌الاجل ندارد.
ترامپ گفت: «من دوست ندارم مهلت تعیین کنم، اما آنها تقریباً می‌دانند؛ آنها از ماجرا خبر دارند... بهتر است رفتارشان را اصلاح کنند.»
این در حالی است که رئیس‌جمهور آمریکا ساعاتی پیش حکومت ایران را تهدید کرده بود که اگر تا هفتۀ آینده با واشینگتن به توافق نرسد، نیروگاه‌های این کشور هدف قرار خواهد گرفت.
او به برنامۀ «گزارش ویژه» شبکۀ خبری فاکس‌نیوز گفت اگر تهران توافق را نپذیرد، هفتۀ آینده حملات را به نیروگاه‌ها و پل‌های ایران گسترش خواهد داد: «هفتۀ آینده وضعشان واقعاً بد خواهد شد؛ چون نوبت نیروگاه‌ها می‌رسد؛ نوبت به پل‌ها می‌رسد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/77124" target="_blank">📅 22:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77123">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در لابلای ده‌ها پیام از اهواز این چند پیام رو هم درباره چابهار فرستاده بودند:
همین الان صدای دو انفجار شدید در چابهار ۲۲:۳۸
چابهار ۳ دفعه صدای انفجار شدید اومد
درود
چابهار صدای انفجاری مهیب اومدددد الان
سلام
۲۲:۳۸ دقیقه ۲ بار چابهار زد
هنوزم صدای جنگنده میاد.
همین الان چابهار زدن
چابهار رو الان زد سه انفجار ساعت ۲۲:۳۵
آپدیت:
سلام ، چابهار رو سه بار زدن ، خیلی بد بود ، احتمالا یه پاسگاه مربوط به دریابانی به سمت جاده رمین
ده دقیقه پیش دوتا انفجار چابهار
سلام وحید پاسگاه کنار خونه‌ی مارو زد
چابهار
پاسگاه احمد ریزه
جاده‌ی ساحلی رمین
سلام چابهارم زد
📡
@VahidOnline
آپدیت
:</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77123" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77122">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#اهواز
پیام‌های دریافتی:
انفجار اهواز ۲۲.۳۱
سلام اقا وحيد
10:30 اهواز دو انفجار بسيار شدييددددد
اهواز دو انفجار خیلی شدید ساعت ۲۲:۳۱
سلام وحید جان
۲۲:۳۱ اهواز صدای سه تا انفجار اومد
سلام، اهواز ساعت ۲۲:۳۰ صدای چنتا انفجار پیاپی اومد
اهواز ۲۲:۳۱ صداش مهیب بود
ساعت ۲۲:۳۵
صدای انفجار مهیب اهواز
اهواز شروع شد با شروع بازي
یک صدای انفجار خیلی ترسناک با لرزش زیاد اومد تو اهواز ۲۲:۳۰
دقیقا دیشب هم همین موقع بازی زدن
ساعت ۱۰:۳۱ صدای سه انفجار از  اهواز
ااهواز همین الان زدن
اهواز دوباره ساعت 22:31 دو انفجار پشت سر هم
وحید جان سلام
اهواز ساعت ۲۲:۳۰ همزمان سوت شروع بازی فوتبال ۲ تا انفجار
سنگر شکن بود احتمالا
زمین لرزید
سلام وحید جان،
اهواز ساعت ۲۲:۳۰ صدای انفجار اومد
شیشه ها لرزیدن
اهواز صدا انفجار اومد موجش زیاد بود
سلام وحید اهواز رو زد ساعت ۲۲:۳۰
ساعت ۲۲:۳۱ دوباره با شروع بازی اهواز انفجار
اهواز وحشتناک بود
۲ انفجار سنگیننن
ساختمون بد لرزید
🔄
الانم زده ساعت ۲۲:۳۵
دوباره انفجار اهواز ۲۲.۳۵
دوباره زد
دوباره خیلی شدید تر ساعت 22:35
دور بود خیلی اما اینقد سنگین بود خونه لرزید چندبار
صدای دو انفجار همین الان ساعت ۲۲:۳۵
۲۲:۳۵ اهواز بازم زدن بار دومع
۲۲:۳۵ یکی دیگه اهواز زدن
اهواز یه انفجار دیگه ۲۲:۳۵
همین الان یکی دیگه زد. سنگین بود ۲۲:۳۵
پشمام دوباره
زمین میلرزه، اهواز ۲۲:۳۵
دوباره ۲۲:۳۵ انفجار اهواز
سلام وحید جان
همین الان دوباره ۲۲:۳۵
ساعت ۲۲.۳۴ انفجار دوم
اهواز
این یکی شدیدتر بود
دوباره زدن، نمیدونم نزدیک تر بود یا انفجار قوی تر بود، سمت جنوب اهواز ساعت ۲۲:۳۶
۱۰:۳۴ دوباره یه موشک دیگه زدن غیر از اون دوتا این یکی از اون دوتا هم بدتر بود خیلییی بد بود
🔄
بازم زد ۲۲:۳۷
این دفعه سه تا بود انگار
۲۲:۳۷ الان هم
10:37 اهوازو زدن
بازم انفجار پیاپی اهواز ۲۲.۳۷
بازم زد ۲۲:۳۷
این دفعه سه تا بود انگار
آقا وحید بد گیر داده
۴ تا دیگه
۲۲:۳۷ باز هم اهواز دو تا صدا پشت سر هم
اهواز دوباره زد الان دو بار ساعت 22.37
اهواز ۲۲:۳۷ بازک زدن صداش بلند بود
سلام دوباره دارن میزنن ساعت 22:36
۳تا دیگه پشت سر هم ۲۲.۳۷ اهواز
خیلی محکم داره میزنه
یا خدا ۳ ۴ تای دیگه زد
یکی از یکی ترسناک‌تر
اهواز ۲۲:۳۸
با سوت شروع بازی ، انفجارهای پیاپی.
اهواز روی لرزه‌ست وحید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77122" target="_blank">📅 22:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77121">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JEdIsyZuvr97HodyyYhojT7aqjOUD-2_zrBtlNModdMdzInA56GCPmlDjXrxgxCHAD-katSVUDYNc930R1iPh1mD9y69GlEBek1wG6u_hi7km0aVnsEXwEDS_1sfnRhsbnHf0DF60mPmwaY7MWh8W0arvgXVWUhdGAQE4k2M5rAI6_Fsv7VdTQqb7TlE1Ry7AlP8PgBNrBgBpx_e-tNPTVooJamgUNsTLwi8wVHNpgEkKy4q4NqLSBAGzSw4NIXWVx6djHl0MepXLqQWtv1qVGFuRnlq2MaT6ivQvpw6OtrC064w4AgOVsO0UCufxZ-KwAGpAwwyyPkOEXAwBdhK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام عارف خوشکار، از بازداشت‌شدگان اعتراضات سراسری ۱۴۰۱، سحرگاه امروز چهارشنبه ۲۴ تیرماه، در زندان قزلحصار کرج اجرا شد.
masoudkazemi81
یک منبع مطلع نزدیک به خانواده این زندانی سیاسی به هرانا گفت: خانواده عارف خوشکار حدود ساعت هشت صبح امروز از اجرای حکم اعدام وی مطلع شدند.
همچنین به خانواده اعلام شده است که برای رویت و تحویل پیکر، صبح پنج‌شنبه ۲۴ تیرماه حدود ساعت ۹ صبح به بهشت زهرا مراجعه کنند.
این منبع مطلع در ادامه افزود: عارف خوشکار روز شنبه ۲۰ تیرماه به سوئیت ۳۵ زندان قزلحصار منتقل شده بود و خانواده‌اش روز یکشنبه ۲۱ تیرماه آخرین ملاقات را با او انجام دادند.
خانواده او با درخواست اعطای مهلت یک‌ماهه و برگزاری جلسه‌ای برای جلب رضایت خانواده مقتول، در تلاش برای توقف اجرای حکم بودند، اما این تلاش‌ها به نتیجه نرسید.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77121" target="_blank">📅 21:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77120">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بیانیه محمدباقر قالیباف، رئیس مجلس شورای اسلامی
،
به نقل از منابع حکومتی:
🔹
این روزها که دوباره آتش جنگ شعله ورتر شده سوالاتی در بین مردم و گروه‌های مختلف پرسیده می‌شود و هرکس به فراخور نگاه خود به آن پاسخ می‌دهد. آیا ما به دنبال جنگ هستیم؟ آیا جنگ و سایه جنگ پایان می‌یابد؟ آیا با مذاکره می‌توانیم به اهداف خود برسیم؟ وقتی با آمریکای بدعهد طرفیم اساسا مذاکره چه فایده‌ای دارد؟ و در نهایت موضوع مهم این است که چگونه حق خود را بگیریم و پیروز این جنگ باشیم؟
🔹
اگر با نگاه منافع ملی، امنیت ملی و به‌دور از نگاه جناحی به این موضوع بنگریم می‌توانیم به پاسخ‌های صریح، روشن و دقیق دست پیدا کنیم. اول باید بدانیم ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است.
🔹
دوم، همان‌طور که قبلا نیز بارها گفته‌ام، آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست. پس نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد. لذا راهی جز تکیه بر توان خود و قوی شدن نداریم.سوم، مقاومت یکپارچه ملت ایران و نیروهای مسلح ما، این نقشه شوم دشمن در جنگ  40روزه را باطل و آن‌ها را مجبور به درخواست آتش‌بس و انجام مذاکره کرد ولی حتماً راهبرد غلط آن‌ها را عوض نکرده است. آمریکا همیشه خوی استکباری دارد و هیچ‌گاه ایران قوی را نمی‌پذیرد.
🔹
با این فرض‌ها باید پاسخ سوالات بالا را داد.ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم. در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم.
🔹
تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد، در غیر این‌صورت اگر قرار باشد جمهوری اسلامی ایران از این متن انتفاع نبرد ما نیز براساس سیاست چشم دربرابر چشم که قبلا گفته ام، دلیلی برای پایبندی به چنین تفاهمی نداریم و همانطور که این روزها شاهد هستیم، نیروهای مسلح ما مثل همیشه برای مقابله با تهاجم دشمن آزادی عمل کامل دارند.
🔹
ما بر خلاف جنگ 12 روزه، به درستی در جنگ 40 روزه تنگه هرمز را بستیم چرا که باعث ناامنی و به خطر افتادن امنیت ملی ما شده بود. امروز هم امنیت ملی ما در حفظ «ترتیبات ایرانی» بر تنگه هرمز و عبور و مرور حداکثری ایمن و بی‌ضرر کشتی‌های تجاری از این آبراهه است تا برای ایران امنیت‌ساز شود.
🔹
حالا برای تحقق این موضع ما چه فرایندی را طی کردیم؟ با شروع جنگ تحمیلی سوم در اسفند ماه، نیروهای مسلح ما کنترل خود را بر تنگه اعمال کردند. در طول مذاکرات نیز ایستادگی و ترتیبات ایرانی تنگه هرمز را در بند 5 تفاهم‌نامه تثبیت کردیم و آن را اهرمی برای اجرای 4 بند دیگر ستانده‌های خود، از تفاهم‌نامه قرار دادیم. حالا هم که به مرحله اجرای تفاهم‌نامه رسیدیم، آمریکا که به لحاظ حقوقی و دیپلماسی دستش خالی است، می‌خواهد با زور ترتیبات ایرانی را کم ‌اثر کند، ولی ما بر پایه دستاوردی که در تفاهم‌نامه به دست آوردیم، باید بایستیم تا حقوق ملت محقق شود. دشمن برای جبران شکست خود فشار وارد می کند ولی ایران با اتکا بر قدرت خود اجازه تحمیل اراده دشمن را نخواهد داد.
🔹
ما باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم؛ جنگ و مذاکره دو  روش حفظ منافع ملی است. مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ،  بخشی از راهبرد مقاومت و صیانت از منافع ملی است. این هماهنگی و استفاده همه‌جانبه از ابزارهای دیپلماسی و دفاعی، برای حفظ ایران عزیز نه تنها یک وظیفه بلکه یک ضرورت اجتناب‌ناپذیر است. جداسازی و انتخاب یکی از این دو روش  به‌عنوان تنها راه حل، خطای راهبردی است. ما در جنگی پیچیده با بزرگ‌ترین قدرت مادی جهان مواجه هستیم و در این جنگ افتخارات بزرگی کسب کردیم؛ پس باید فکر و عمل ما همان‌قدر بزرگ، پیچیده و مقاوم باشد.
🔹
این مثال را می‌توان در مورد  لبنان، رفع تحریم‌ها، آینده پایگاه‌های آمریکا در منطقه و انتقام وخونخواهی امام شهید انقلاب و سایر شهدای این دو جنگ تحمیلی هم تسری داد.
🔹
راه پیروزی و احقاق حقوق ملت در این جنگ و شرایط حساس، پیروی از رهنمودهای رهبری و حرکت  براساس یک  نقشه‌راه دقیق بر مبنای مقاومت، عقلانیت و استفاده هوشمند از همه ظرفیت‌های دفاعی و دیپلماسی در جهت تحمیل اراده خود بر دشمن و کم اثر کردن تبعات اقتصادی جنگ به مردم، است.
🔹
مرز بین جنگ یا مذاکره با دشمن، براساس امنیت و منافع ملی مشخص می‌شود و تشخیص استفاده از هرکدام از این ابزارها، متناسب با اقتضای زمان و شرایط، با ولی امر و فرمانده کل قوا است و همه ما وظیفه داریم متناسب با تکلیفی که نایب ولی عصر (عج) معلوم می‌کنند، برای جنگ یا دیپلماسی یا هردو تلاش کنیم.
🔹
بر همین اساس از همه ملت ایران با هر نگاه و سلیقه‌ای می‌خواهم در تبعیت از اوامر رهبر معظم انقلاب وحدت را حفظ کنند، در میدان باشند و این حضور و وحدت را به رخ دشمنان بکشند. همه می‌دانیم که مسیر دشواری پیش رو داریم. آن‌ها قبلا هم ما را با ناو و حمله هوایی و زمینی و ... تهدید کرده‌اند، نتیجه‌اش را هم دیده‌اند پس نباید از تهدیدهای دشمن ترسید.
🔹
همچنین به اخباری که توسط عده‌ای منتشر می شود تا شما را از مسیر طی شده پشیمان و نسبت به آینده ناامید یا نسبت به خادمین ملت بی‌اعتماد کند، نباید توجه کرد. دشمن به ناامیدی، ترس، اختلاف و بی‌اعتمادی‌های متقابل طمع کرده است. حتماً حمایت و اعتماد شما به سربازان عرصه دفاعی، دیپلماسی و خدمت، دست آنان را مقابل دشمن برتر می‌کند.  مطمئن باشید آن‌ها جان خود را ضمانت امنیت شما و منافع ملی ایران گذاشته‌اند و با تدابیر رهبر معظم انقلاب و مسیری که طراحی شده، نتیجه این اعتماد و حمایت خود را به فضل الهی خواهید دید.
🔹
اینکه ما امروز از موضع قدرت در تنگه هرمز سخن می‌گوییم، نتیجه‌ همان قدرت میدانی است که مردم برای ما ایجاد کرده اند، و برای ما مسجل است که انتقام خون آقای شهیدمان را نیز به ثمر خواهیم نشاند و دشمن باید بداند که هیچ کوتاهی در تحقق مطالبات خود نخواهیم داشت.
🔹
بنده به سهم خودم در دوران جنگ تحمیلی سوم، هم در میدان دفاعی و هم در مقابل طراحی دشمن  در جنگ رسانه‌ای بودم، بعد از آن هم با علم به تمامی مشکلات و تخریب‌ها در سنگر دیپلماسی حضور پیدا کردم و هیچ‌گاه از زیر بار مسئولیت شانه خالی نکرده‌ام.
🔹
هدفم اعتلای ایران عزیزتر از جان، تحت هدایت‌های رهبری معظم انقلاب است. عمرم را صرف مبارزه با دشمن کرده‌ام و هراسی نیز از جنگ با دشمن یا تهمت و تهدید و تخریب نداشته و آرزو دارم در این راه به رفقا و رهبر شهیدم بپیوندم.
🔹
در انتها به مردم جنوب کشورم که این روزها در خط مقدم جبهه قرار دارند، می‌گویم که از ابتدای جوانی دوشادوش شما خواهران و برادران عزیزم اسلحه به دوش گرفتم و جنگیدم، شما عزیز جان ایران هستید، جان ما هزار بار فدای شما، در مهم‌ترین سال‌های جوانی من و خانواده‌ام پای سفره‌های مهمان‌نوازی شما در مناطق عملیاتی جنوب نمک گیر شده‌ایم، گرمای عشق و محبت شما به هموطنان خود و به ایران را هرگز فراموش نمی‌کنم.
🔹
بدانید که ما سرمان برود، پای قولمان هستیم، شاهرگمان را برای دفاع از این مملکت گرو گذاشته ایم. به فضل و منت خدا بدانید که پیروزی ایران عزیز نزدیک است و مقاومت تاریخی شما ماندگار خواهد شد.
🔹
مردم عزیز ایران! ایمان داشته باشید که این بغض‌های فروخورده شما و این وحدت بی‌نظیر تک تک ملت ایران در کف میدان، پیروزی ما را تضمین خواهد کرد. ما نه تنها از تهدیدها و جنگ با دشمن نمی‌هراسیم، بلکه تحت ارشادات رهبر معظم انقلاب، پاسخ قطعی این جنایت‌ها را به دشمن جنایتکار خواهیم داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77120" target="_blank">📅 21:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77117">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خبرگزاری فارس با انتشار تصاویر بالا مدعی شد:
انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
این پهپاد متجاوز ساعتی قبل با رهگیری و شلیک موفق سامانۀ پدافندی رزمندگان سپاه در بندرعباس منهدم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77117" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77116">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YGCo4bjZx-MRHuD-Frxf4xzhrrymcAYFxdIM2C-Jq_lJEFzzF5hO1HusL_TaN3beCccXvoHHLk82_Q2uZJJXowOXJwV_i4izBZWRTJ9WyZqSaPucQh7t8xkoQoCDFiGLFFpY7Z_hTq_NvPYa7M2kk05Odm3nf9tlnEcEb9espPm8Xtyc8u2QwBVaUcBhOCRGTzqpc1f0xL8e16SoYcpf7IIVl4IDGQbyGb9k69GVGClTUeXVD-DrQJR3hA8G7c65KpkYf-t0ZV68qkEODoA4T9VTwH-as7rcrlGHxDUJFNKbauUB1pLtioY-gMaJ54rAvu1FC-fawvIhH7g-SCtxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام، ترجمه ماشین:
🚫
ادعا: رسانه‌های دولتی ایران مدعی شده‌اند که نیروهای آمریکایی در ۱۴ ژوئیه یک تأسیسات غیرنظامی ذخیره‌سازی گندم در هویزه را هدف قرار داده‌اند. این ادعا نادرست است.
✅
واقعیت: نیروهای آمریکایی در ۱۴ ژوئیه اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. هم‌زمان، ایران غیرنظامیان بی‌گناهِ در حال عبور از تنگه و همچنین غیرنظامیان در کشورهای همسایه خلیج فارس را هدف قرار داده است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77116" target="_blank">📅 19:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77114">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BYVwaqfZgfWcu2diIiFuPanQll9Csku6H8rXOkI00LV4173sSiijokDaEvFuPOuumM5eVIyU59-TzSZ3CWR_p8kmeIvEBPnv8LnfnLxl7NAkOC0V4y5qWLNy3yxQY469MAqpE81hggKIjo-J1zXmlgfUQoDoBuJQoEAYVqcTlMEmM_RX_fHz1G2PPd3vKjgifVHD1MXcUYzvZix5j1k8bZVhT8kwWeyElTIkb27UtRUT4zUTgKPqtZS4mXtZd7FHke2MSh3IdLDN81iyG5gZcdeMQJ5cjId4-tVIIM1KT6VKnSmhZCrH0zSuxWegmu0T0jpwlH648z69TrwG5-Xz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/32acbd8d90.mp4?token=GIwxk437djYB7no_3DTblXH474XMymU5nomnfY6IpmsJyyYDBxvdRzjrGZ9Ebog-M-YhURn_ZAWtjPo1UGokj_JczRX1vovrK97UuoZQzCh1WP_pCFp1om6RShAQ7-t-dZISpiA_Aq02FQCJ57jcrxZqRnzuHYREQdvgFV16P_RznFx_PD74YIZ6fUpTMZ_NP2B-jB7Hw4SYYV39Lkw66nlFV5ZSEJLdfNtlcxx-HvCSZSsu4ku51zfPLBTwIyd-hIvXQ3j0csan1tsF-PJ7m_K0eFsNJJG3xA_gIiHwcXwaj9IOwfWfVZwWxB1bZKT6BDIhGLEnFdxWPpO7FGCsuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/32acbd8d90.mp4?token=GIwxk437djYB7no_3DTblXH474XMymU5nomnfY6IpmsJyyYDBxvdRzjrGZ9Ebog-M-YhURn_ZAWtjPo1UGokj_JczRX1vovrK97UuoZQzCh1WP_pCFp1om6RShAQ7-t-dZISpiA_Aq02FQCJ57jcrxZqRnzuHYREQdvgFV16P_RznFx_PD74YIZ6fUpTMZ_NP2B-jB7Hw4SYYV39Lkw66nlFV5ZSEJLdfNtlcxx-HvCSZSsu4ku51zfPLBTwIyd-hIvXQ3j0csan1tsF-PJ7m_K0eFsNJJG3xA_gIiHwcXwaj9IOwfWfVZwWxB1bZKT6BDIhGLEnFdxWPpO7FGCsuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو پدر سام حسنی از محل واقعه منتشر کرده.
کودکی که در میان جعبه‌های گیلاس کشته شد.
پنج‌شنبه ۱۸ تیر:
نیروهای هنگ مرزی مستقر در روستای درکی، بدون هیچ‌گونه اخطار قبلی، خودروی شخصی یک خانواده اهل این روستا را که پس از پایان کار روزانه در باغ گیلاس خود در حال بازگشت به محل سکونتشان بودند، هدف شلیک مستقیم قرار دادند.
@
VahidOnline
در جریان این تیراندازی، گلوله به کودکی که در قسمت بار خودرو حضور داشت اصابت کرد. او بر اثر شدت جراحات جان خود را از دست داد.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77114" target="_blank">📅 18:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77113">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۱۷:۳۸
[جزیره] هنگام، الان صدای ۲ تا انفجار بزرگ اومد سمت وسط جزیره
جزیره هنگام رو همین چند دقیقه پیش دوبار زدن
📡
@VahidOnline
🔄
ساعت ۱۸:۳۹ خبرگزاری مهر
:</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77113" target="_blank">📅 18:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77111">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a0AEOyvTIfZBpr9wTfoM4ci7GAMOqsiDbptduEaOTL_0d0H93unLKQnQlRhttOb7JfiofdTK8GmAZ1FajpvhuMuzBUahtVJMVlLTAJZgwZ6_t2dBtvqdaEAHrKQSW4fcjB0jyu4qtWXdve8mA6b6fNcKMtcn-YTBjYTC58RgiS1WOYN59xQO-jy6utX5afLAqWI9CqZ6TecFrTbX68-MrH0ILuCAm0GF5IYojMvmjwAeIGW04eud4F-jQYCTPbUmla_XHdSKVcknFA1Nc-aC3UBY6xHbN85-v-2e2Js8XVbYrK6lQL3zLUJRtTGkCdhFkNdgTgPKbVyWyNbRmQfxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/op24aoc77GhOIdNNmBrq5h7UlFDa3YkTZzdLI13XNMxWb_M5bOP0G83Dn0qlmTiuPPXnm2ETPakJKslaY9sUeKd9o7o2yFb-RXDOvzmw4WKos-6kJW3y1UaA0oo3-h4rANLYysYoakXenV-5ud9Je5iKiYxxVvmlJ93pUF1qf3r37EOxoxEANQdOxmAw8_gTZju3zIUONo5oBtR8niHhbSRL5zRQVXcSPqttS_YXMXWI1bNTmG0r89eQaSJAHBvRf76TCQQjDpCnjSzu1mhGtK5_-xO2DdcrIMtRKajE2ufVs0pGBLMWoIMirwhfn0JQ7gNmq7d2eaLmpZRiKbWtrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در بیانیه فرماندهی مرکزی ایالات متحده (سنتکام) آمده است: از زمان ازسرگیری محاصره دریایی بنادر ایران، ۱۷ ساعت پیش، نیروهای ایالات متحده مسیر حرکت دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند.
@
VahidHeadline
صدا و سیما چهارشنبه ۲۴ تیرماه گزارش داد که در ۲۴ ساعت گذشته دست‌کم دو کشتی که به گفته این رسانه قصد داشتند بدون هماهنگی با ایران و به‌صورت غیرقانونی از تنگه هرمز عبور کنند، پس از بی‌توجهی به هشدارهای اولیه، با شلیک اخطار نیروی دریایی سپاه پاسداران متوقف شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77111" target="_blank">📅 17:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1ECT7pD7AcWyBVABi4ARfZk9TYjonuDjFW9lv8xglfowqgAMEyndDSvhElWTMFYifUvJ6MfWiagoqGJDpMlhQaFR0lullylKpN4e9HcNSra17BhvpDUFYZA_r44ImZOipEEBpIWIVkV7XGV4frYvFWJfUs5oWJJXlwbngtVSmKpl9ki5n7mgvNQqXnQlcc_Am12fZnxBR0TqsW_qJ9CDaVOnCOKhZvP3f7c1Lz0qdccx6kYJsHu52mJzYSgePaOIqIxHnUMKX-PIY66rgPwSEZNR3EnsfdKmtHiVLwU5ROo_-_zHQkVM7tRi1-3lRjdbeJNcr24PvqfdgIR6DVLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده کریگ فورمن، شهروند بریتانیایی زندانی در ایران، روز چهارشنبه ۲۴ تیر اعلام کردند که او در زندان اوین به دلیل انجام مصاحبه با رسانه‌های خارجی، به دو سال حبس اضافی محکوم شده است.
کریگ فورمن و همسرش، لیندزی فورمن، در جریان سفر زمینی با موتورسیکلت از اروپا به استرالیا، در ایران بازداشت شدند. این زوج اسفندماه سال گذشته از سوی دادگاه انقلاب به اتهام جاسوسی هر کدام به ۱۰ سال زندان محکوم شدند؛ اتهامی که همواره آن را رد کرده‌اند. مقام‌های جمهوری اسلامی نیز تاکنون هیچ مدرکی برای اثبات این اتهام به‌صورت عمومی منتشر نکرده‌اند.
پیش‌تر وب‌سایت حقوق بشری هرانا گزارش داده بود که  این زوج ۵۳ ساله در اعتراض به رد درخواست تبرئه و جلوگیری از آزادی و بازگشت به بریتانیا، اعتصاب غذا کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77110" target="_blank">📅 16:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77109">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mfjGOSFXoIsnFn8BkloqwehwSU0u-N36Ih9ohWefvo82FlqvtXcscQDp25g6lBfjp1Ai6Lp2clk2RfPJ1bKodxBXt8lBE-AqEzb1hNEyWuZIMHwpTpSPoDffsnWExvQqOK_dRoU040fJRAo1hYWhgoX0QTgfILFBEysaNotF8E6PPo7NBqnHzqynOKDWEzOQEMDBOWzGju4CU5lYtNLO6yqAhX68MULt4V3FZ7ovSv59XFq5rFO8quwSbLqSXpzbHN6Iv8Rv4j46W7ox00AmJW-IK-ofmfWBJ4hvGmOrDW-ltw9-koJyiPGaOVMEEbiT9GcuFGTKnHRrPcRpUNABvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت دولت:
اطلاعیه ستاد عالی آزمون‌ها در خصوص برگزاری امتحانات نهایی در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
ستاد عالی آزمون‌های وزارت آموزش و پرورش در اطلاعیه‌ای اعلام کرد:
🔹
بر اساس تصمیم ستاد عالی آزمون‌های وزارت آموزش و پرورش و با توجه به شرایط خاص کشور در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته‌های تحصیلی پایه دوازدهم در روز پنجشنبه؛ مورخ ۱۴۰۵/۰۴/۲۵ و پایه یازدهم در روز شنبه ۱۴۰۵/۰۴/۲۷ لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
🔹
بدیهی است امتحانات نهایی سایر استان‌ها و امتحانات بعدی استان‌های مذکور، بر اساس برنامه ابلاغی در موعد مقرر برگزار خواهد شد.
dolaat.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77109" target="_blank">📅 15:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77108">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b87d0cf0d8.mp4?token=hy6AisJeZIEfPBMXIlIDTpEiDP3__-bvdt5RrjzHRQNXDQox11h4DLg6GpEx2GMySyZNWMX6ghGykXssZ5eVZOommWIE72s-tcOSY-G01P1_W2TeWnAYlfPmpiZkx2qsLhURyZoQmlDtR1GG7eVixmWBgRa5W8ot-iI3s_vERIRtoGAxX-Mv9Ahac0966nMJWqEcQ7qIMQDABA3CnfJ2201SxfP-iMG3ItTJadxT6V-dvHMrT0Wo4t7D97c1g6fVGLS7omR5LWd9XQef9XcTVQxc-x1O84XocTqWUBpd0U6oBr2XQu8Cg5NIaoNGdeXZ3-phpzFRfE3uJQz7WJfPmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b87d0cf0d8.mp4?token=hy6AisJeZIEfPBMXIlIDTpEiDP3__-bvdt5RrjzHRQNXDQox11h4DLg6GpEx2GMySyZNWMX6ghGykXssZ5eVZOommWIE72s-tcOSY-G01P1_W2TeWnAYlfPmpiZkx2qsLhURyZoQmlDtR1GG7eVixmWBgRa5W8ot-iI3s_vERIRtoGAxX-Mv9Ahac0966nMJWqEcQ7qIMQDABA3CnfJ2201SxfP-iMG3ItTJadxT6V-dvHMrT0Wo4t7D97c1g6fVGLS7omR5LWd9XQef9XcTVQxc-x1O84XocTqWUBpd0U6oBr2XQu8Cg5NIaoNGdeXZ3-phpzFRfE3uJQz7WJfPmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از دکل مخابراتی بندرعباس پس از حملات نیمه‌شب سه‌شنبه و بامداد چهارشنبه آمریکا در صبح چهارشنبه ۲۴ تیرماه در شبکه‌های اجتماعی و رسانه‌های داخلی ایران منتشر شده است.
بر اساس این تصاویر، بخشی از تاسیسات مخابراتی در این منطقه آسیب دیده، اما هنوز جزئیات رسمی درباره میزان خسارات، اختلالات احتمالی ارتباطی یا هدف دقیق این حمله اعلام نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77108" target="_blank">📅 15:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77107">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9180947e9.mp4?token=CNmTkw9Kf0vK58eECeDCWk9aoFqhQLerdu9cp3jdVI_Lfd8O3c6aVzmYiUp2xlq_c_f-UA5oeBjT60pd7WKVE0ZJrDD6sZ4x2x-ws1jsdwHDNUHYDGWQfGLPqiq6rOjQzntid5hOwPp-iYAF0DfrSnbr0Bg79pKAe5RsvNVjY8uV5JGur2DakQBCHNFtYE8E0KL3u1yWokhe_6jXyne1l1tY2IDVtmeD3AzBe20q5zZX3_Gu-VGXvasGvMxDyD2_ci-kngrV7JDtwjIU_uTobxHbkpnBBHVJfKxk95KtGvJVY4Pe3IMA8rBnaPoMM_PRMDxxx9beuXURqAYBwhTwGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9180947e9.mp4?token=CNmTkw9Kf0vK58eECeDCWk9aoFqhQLerdu9cp3jdVI_Lfd8O3c6aVzmYiUp2xlq_c_f-UA5oeBjT60pd7WKVE0ZJrDD6sZ4x2x-ws1jsdwHDNUHYDGWQfGLPqiq6rOjQzntid5hOwPp-iYAF0DfrSnbr0Bg79pKAe5RsvNVjY8uV5JGur2DakQBCHNFtYE8E0KL3u1yWokhe_6jXyne1l1tY2IDVtmeD3AzBe20q5zZX3_Gu-VGXvasGvMxDyD2_ci-kngrV7JDtwjIU_uTobxHbkpnBBHVJfKxk95KtGvJVY4Pe3IMA8rBnaPoMM_PRMDxxx9beuXURqAYBwhTwGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام دور تازه‌ای از حملات صبحگاهی علیه ایران انجام داد
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دوری از حملات صبحگاهی علیه ایران را ساعت ۷:۳۰ صبح به وقت شرق آمریکا در ۱۵ ژوئیه به پایان رساند.
سنتکام در جریان این موج ۹۰ دقیقه‌ای، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد. این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77107" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77106">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G38pX8WbRQXOc6BmNpW979b5Dq0vXD4aGztfMEcxkkI4Wy0CN7AkhKnL_94Xr6d5Kyt-eo9YifazE-LfUk9HJUEwZS45NpBy9sSuS6X2RXADbo7n2Xq_qlWHZxS5pd-ULQ1cs2wOiFZU6IivDknmpL3Bjy6hUdmNf_OVmhCacmZmVnMoy5sLSS5YbpQ659L-xyQFvUUBMdiEC7gCvSke9PdYpucT1PLZdTBjYPzcMIs81Q8pUN5AszYOJkYog-6VDFPwaYZqb2nX-36EdHSVlZ0xhb8BznXPHuciCMyENJI1fhDzPUmaenDEhxyLvQzADZUVezU2J-NhfmrxJTR0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپیده ابطحی، مستندساز، تدوین‌گر سینما و از اعضای خانه سینما، صبح امروز، چهارشنبه ۲۴ تیرماه ۱۴۰۵، با یورش ماموران امنیتی به منزلش بازداشت شد.
خواهر او با انتشار مطلبی در صفحه اینستاگرام خود از بازداشت این مستندساز خبر داد و نوشت که مأموران امنیتی علاوه بر بازداشت سپیده ابطحی، تعدادی از وسایل الکترونیکی شخصی او را نیز با خود برده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77106" target="_blank">📅 15:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77105">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwhvyUjbhp0ObGIU8Xt7rRl_0PBmq9VjrazmXkWLQTezMj0xlTdttww-sCP107axm56alzsnc386FTjpB03Cepvwm3apd77AuAkYk1HUXPoOfmLgvOhBUDFPV7NsZ6MaF2wYtVdx5nu4wYbsYkQL_6wM1wlkpb77XxEAPemeSUIho5XSsXwbO2MzFgj_l_uocKFRKy5bN3Gri7lnR_VLsqBEOfAjyxHG1DjncjUrKd4f7cUfPCr8CQDf2QqCveqhQlrp_2zKxT6R7Gjjz0GCXKPdYqUaA-sSO_Pfl4Ku3EVT_rCZ2uDvb_27U2BvTGN0MHsSXxzItNkJRy-jWfixAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای هر دلار آمریکا در بازار آزاد ایران با افزایش سه هزار تومانی نسبت به روز گذشته، از ۱۸۷ هزار تومان فراتر رفت.
براساس اعلام سایت‌ها و کانال‌های اطلاع‌رسانی طلا و ارز، قیمت هر پوند بریتانیا به بیش از ۲۵۰ هزار تومان و هر درهم امارات به بالای ۵۰ هزار تومان رسیده است.
برهمین اساس بهای هر سکه بهار آزادی طرح جدید با افزایش چهار میلیون تومانی، بیش از ۱۸۴ میلیون تومان قیمت‌گذاری شده است.
این رشد هم‌زمان با تشدید تازه جنگ و بازگشت محاصره دریایی آمریکا بر بنادر جمهوری اسلامی رخ داده که نگرانی از افت بیشتر صادرات نفت و درآمد ارزی کشور را تشدید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/77105" target="_blank">📅 15:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77104">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmlPISZV0ZOQyzYRQG1tY94nkGW5dUE6Rw-mVBqVmFCzaglAU680Pq9N2s--U9aMXrNMhf2z1UzzWmTTl3ETd_GNDGMMTrqgtQjUwTDPQsqEIJymZNjDPusw2gvxvyeoijtFGQJCscKtzxUYlDjcLFbTtdR-eX_hf8vNI0ANvgsll6EBZqpwMP7DNj8YtGnWt2zjWqCW9wSOaWUBg0yTnTum0-ng4JHlbR9zv_A6GAdCLEMr-4qIsyWxAjNgGemCLk4JbqzHYvK-yTipEHRD8Ua1PgOtLIFuWSXn20D4I-68QxCs-2AXYT5yVLnmM5FS6D2PHOJF6NFYePCgwhsWxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک زن ۳۱ ساله به نام پروین الله‌دینی بامداد ۱۶ تیرماه در محله هشت‌بنگله شهرستان مسجدسلیمان به ضرب گلوله کشته شد.
متهم که از آشنایان او بوده، پس از ورود اجباری به منزل، مقابل چشمان دختر ۱۲ ساله مقتول به او شلیک کرده است.
عامل این قتل مردی به نام جهانگیر معرفی شده که پیش‌تر بارها از پروین الله‌دینی درخواست ازدواج کرده بود. گزارش‌ها حاکی است که او پس از شکستن درِ خانه، با یک قبضه هفت‌تیر وارد منزل شد و زن جوان را هدف گلوله قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77104" target="_blank">📅 15:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77103">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpSt4Wh66Bo6h3ukFmn_BARhf9sz1xTXxEW-izSc9Osz7JJrTWkZPh9JRkGKPm-SR5lsfY7oGhgbDwo-AzUl4QUWYCspdrJhlORmA8M8a_BuEGBNJS7H_LBgSKQAgBERkoEB5U_bn79CAt1CbNgFatFPvA1rPbMlkmxGQuaeKhuHifHNLqcjlBzfruNf9jHg6LGdGUti0VTymAAF5Ew6D8QvASsPqybqQH_3-XsGN6Tp-DOoS4wx44NppFYi_KIlsQgh1OpKdEOc-JbVqdxSOURht1ZBGM13Pnko-TbGJNksLuv7ufQm-wteSigGMhyxXVtyozgeA7wPnsB3LkySaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های هند به نقل از خانوادۀ خدمۀ هندی گمشده در جریان حمله به یک کشتی قبرسی در تنگه هرمز، گزارش دادند که جسد او پیدا شده است.
این تبعۀ هند با نام هرامب کارمارکار، مهندس دریایی شاغل در کشتی کانتینری «جی‌اف‌اس گلکسی» بود که سه روز پیش هدف حملۀ سپاه پاسداران قرار گرفت. در جریان این حمله ۱۱ نفر هندی دچار حادثه شدند که ۱۰ نفر آنها نجات پیدا کردند.
سپاه پاسداران انقلاب اسلامی در بیانیه‌ای با تأیید حمله به این کشتی گفته بود به دلیل «حرکت در مسیر غیرمجاز و نادیده گرفتن هشدارهای مکرر»، با موشک به آن حمله کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/77103" target="_blank">📅 15:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77102">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idYJF9tUjNRl6PyknEpKTENKNGvfCW4qCrLBCDzNFpe0exu5LusA8_yxSxV48upno0xqTI2lMH673xrk8oywRWean7KmlR1QQAmTEWm4IihT-fHAl4ROyLtWwC0iL9UaYS66-nolSFwhtClKLnXXhc4F3qkOXFGDjgKtgfkrxgC5YiT2s3ngeuXTr1gd01trXI8XrDfa9U_CeZTyNKyhNRlTqIJzj7gyG7YjymaAIQvtpUo_kXUgLnHMsqkn9rgXAM_7yNdyKXVFafwtM5ioH_88wzQGK1AOi7AGD9Gk9hfP50h0xkpVsIlFIYEZwMHYomCumEezVP2ZGxHYEXSzcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی صبح چهارشنبه ۲۴ تیرماه اعلام کرد هفت نیروی پایور و سرباز وظیفه ارتش در پی حملات آمریکا به پادگان نیروی زمینی بمپور ایرانشهر در استان سیستان و بلوچستان کشته شده‌اند.
در اطلاعیه ارتش آمده است که ارتش آمریکا «با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش جمهوری اسلامی ایران در بمپور را هدف قرار داد.»
نیروی زمینی ارتش جمهوری اسلامی تهدید کرده است که پاسخ این حملات را در زمان لازم خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77102" target="_blank">📅 15:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77101">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/139d0c2397.mp4?token=dZTJ_iVqd0xSQyvr19x2ZhkvVHn5VatnaDsu7A9K0TuLmZ-nxSIVEpQsNFIwdAg65_NTzeyujKUpaIa0HRFb5_5QrhuiD6lC590eLpeo0zj3g0vWrZzgGMcBKFdYX8d6PryYsmBihxtquOv2Dg_3fmYed1r7PHdP1ouXtRdxmC54Y62lvq6RK-TWsjS46hm6IjQbPZVfKB8CJqN7AR2sGKJ-SM6ynZ-kBtBTmbaN0sHg1iQQKL4vSmqvy1nwzP7YYUuCdHu2YdCuCHa33bPkHq1GUufzlYx5ZZHWVi9nsKJDQBSH0v0LJZlZXodIRl2lGxUHVHmCEsjNb-oK8nJP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/139d0c2397.mp4?token=dZTJ_iVqd0xSQyvr19x2ZhkvVHn5VatnaDsu7A9K0TuLmZ-nxSIVEpQsNFIwdAg65_NTzeyujKUpaIa0HRFb5_5QrhuiD6lC590eLpeo0zj3g0vWrZzgGMcBKFdYX8d6PryYsmBihxtquOv2Dg_3fmYed1r7PHdP1ouXtRdxmC54Y62lvq6RK-TWsjS46hm6IjQbPZVfKB8CJqN7AR2sGKJ-SM6ynZ-kBtBTmbaN0sHg1iQQKL4vSmqvy1nwzP7YYUuCdHu2YdCuCHa33bPkHq1GUufzlYx5ZZHWVi9nsKJDQBSH0v0LJZlZXodIRl2lGxUHVHmCEsjNb-oK8nJP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
صدای انفجار در شیراز مربوط به عملیات معدنی کارخانه سیمان بود
🔹
صدای انفجارهایی امروز در برخی نقاط شهر شیراز شنیده شد.
🔹
براساس اخبار رسیده به خبرنگار مهر، این صداها ناشی از عملیات انفجار کنترل‌شده معدنی در محدوده معدن کارخانه سیمان شیراز بوده است.
🔹
بر اساس پیگیری ها این انفجارها در راستای فعالیت‌های معدنی و برداشت سنگ در محدوده معدن کارخانه سیمان شیراز انجام شده و با هماهنگی‌های لازم و رعایت الزامات ایمنی صورت گرفته است.
🔹
شنیده شدن صدای انفجار موجب نگرانی برخی شهروندان شیرازی شده بود که بررسی‌های انجام‌شده خبرنگار مهر نشان می‌دهد این صدا ارتباطی با حادثه یا رخداد امنیتی نداشته و مربوط به عملیات برنامه‌ریزی شده معدنی است.
پیام‌هایی که من دریافت کرده بودم:
انفجار وحشتناک شیراز ساعت ۱۳:۱۷ دقیقه
وحید یک صدای عظیمی اومد الان شیراز
شیراز
همین الان ساعت ۱۳:۱۸ صدای سهمگینی اومد
من سمت زرگری هستم
درود وحیدجان
۱۳:۱۸ شیراز سمت ما یک صدای شدید امد، فکر کنم زدن، چون چندتا از دوستامم از جاهای دیگه شنیدن صدا رو
انفجار اطراف دلیران تنگستان شیراز ساعت ۱۳:۱۷
سلام شیراز  ساعت یک و نوزده دقیقه صدای توافق اومد، جاش رو نمیدونم ولی صدای مهیبی داشت
وحید جان کارخونه سیمان شیراز رو ساعت ۱۳:۱۹ دقیقه زدن
ساعت ١٣:١٠ صدای انفجار سمت محله فرهنگیان شیراز اومد. برق هم که نداشتیم از قبلش
سلام وحید جان شیراز یه صدای  دور امد که شبیه برخورد موشک بود ۱۳:۲۰
سلام شیراز یه صدای انفجاری اومد
طرفای صنایع صدای انفجار مهیب
صدای انفجار در شیراز مربوط به عملیات معدنی کارخانه سیمان بود
من که این قسمت شهر زندگی میکنم هر از چند وقت، محدوده معدنی کارخونه سیمان انفجارهایی دارد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77101" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77100">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Px1M2v89naq4B5c47htlrdAI6UbK3nMshm4fRgCPBBCyHYMdTwkfcp7SLXLaNauG99yEtYxlJA9_ZxfYLcFkmZEkh7HdjrTHg1PAt_29ftLmmyOkN-TS4n1o8Zfcf00JIFV8oCVoK1b7JHSEWOxCJP-CDgVeTUbew3zU6nrRLO6DtIf_TFHNpQIiTJladlLWTbsrm6xycWw7WA5HA2Jc77d0FbGjOhjf9AZQ3OXJXTB5MtS83XNA6LLOI1RjhteCSIJNsIStzKzDqJJvQO4als1EVmBGc_62CjY5b5wcJ3fDDd0Da4_dTPv2jzhDfdhwOS7xbn5UxhHXYn7Ka8rZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ارتش ایالات متحده، سنتکام، بعدازظهر چهارشنبه اعلام کرد که نیروهایش از ساعت شش صبح به وقت شرق آمریکا (۱:۳۰ بعدازظهر به وقت ایران)، موج دیگری از حملات علیه ایران را آغاز کرده‌اند.
در بیانیهٔ سنتکام آمده که این حملات با هدف تضعیف بیشتر قابلیت‌های نظامی ایران در حمله به کشتیرانی تجاری در تنگه هرمز انجام می‌شود.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه،‌ ۲۴ تیرماه، به برنامۀ «گزارش ویژه» شبکۀ خبری فاکس‌نیوز گفت دور جاری حملات به ایران «تا زمانی که من بگویم، ادامه خواهد داشت».
او تاکید کرد: اگر تهران توافق را نپذیرد، هفتۀ آینده حملات را به نیروگاه‌ها و پل‌های ایران گسترش خواهد داد.
او گفت: «هفتۀ آینده وضعشان واقعاً بد خواهد شد؛ چون نوبت نیروگاه‌ها می‌رسد؛ نوبت به پل‌ها می‌رسد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77100" target="_blank">📅 15:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77099">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGaSLAi4SfgfI3CpVcS5Hl1Gx1y5frn3oNn6mCT1uhIAcPD7Kc7FVOWIE9NfE7w0xhyVFIzJiNTGGdnHJIDwoAAJ7aIACpv-9lavuEQtFSJrx6TAMJxXTncAiWLW4MkYdGlQAym7j06Q1Sv-nsujCD9xTVjQ334i8lsK-sqBVUsCyW3-RZU3IGhF0aXijUXVm6Ih7jgQFHB9jWzEsQiilQNzX3tRTX5Ij6eT9vJbg3zpZ1Krudd_0OQmxExjbYlfsLgv8Ceg7rGMrL-iaJhAgg3xekLnREYBNN9MeWFh9G-25-vdZEUy2P7USFsBV7I8Nq5-xQYlR3aud_lpYPQ3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77099" target="_blank">📅 15:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77098">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd0e6fce01.mp4?token=M90FjG9-8MmEP9J2kXEeXD_wnFXqM-8aiva_vgAiVlQYeXTF1R3Q8-zfn2MTzTtAr-E1dd-Hr67toM0MW0T9i3lqbgn1CS7nW3jJYzURNgbxM6sh_FqUl8XPiM27Qx4_BtgEMMtBXJX5Ka6Vucrmx8yI6nbTOUeOZHDUTqPNI76VQxMAWyOiwiqGRk8EBjnIFG8nCTjmNdLFi3Jjl3cHZvh2AnkY76i8QrvwnQs2qoyxk1kza-Fmk7Jod19kx4q0UK503sVzWOwp7Ysrvl1-fdytdgtLqBdhCZYBH7Gunj3Sjd0TOgnZBRaWU4KDJAgiwcSql_0z6OZXn5xtdt6S0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd0e6fce01.mp4?token=M90FjG9-8MmEP9J2kXEeXD_wnFXqM-8aiva_vgAiVlQYeXTF1R3Q8-zfn2MTzTtAr-E1dd-Hr67toM0MW0T9i3lqbgn1CS7nW3jJYzURNgbxM6sh_FqUl8XPiM27Qx4_BtgEMMtBXJX5Ka6Vucrmx8yI6nbTOUeOZHDUTqPNI76VQxMAWyOiwiqGRk8EBjnIFG8nCTjmNdLFi3Jjl3cHZvh2AnkY76i8QrvwnQs2qoyxk1kza-Fmk7Jod19kx4q0UK503sVzWOwp7Ysrvl1-fdytdgtLqBdhCZYBH7Gunj3Sjd0TOgnZBRaWU4KDJAgiwcSql_0z6OZXn5xtdt6S0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: '
#چابهار
، چهارشنبه ۲۴ تیر، ساعت ۵:۳۰'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77098" target="_blank">📅 08:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77097">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67211d7671.mp4?token=tRsWpfEbP2JpGj51AUNxhrlrVxRC_ghEXb1gGobRX-A-77xOD8rmUItFTYPuadOtEhsfi6_Ayy-diedWSn2N8qweYCqHwAdr7RHoh5z8xgCwbmnsy-i8zzCBy9ZYHiXUvmGUpd19sbwAKwOFE3RuwokZNhZNN0lKhACG7oz3FNVqqr_agEXHioiXfq_fsT6aLbf4M8kL8C_0QHk4vjf0LgNVskKRImeohxgswCyzlC6Eog0yScRAfMUooRgSumWXoOuVajnXZ9afoQf5s6NGRzMeIUH9tSN-WSxyhyTTUeGc66LrlNVux9IPp5DvVF9smh9wo8-2qU-LMwGESOJ0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67211d7671.mp4?token=tRsWpfEbP2JpGj51AUNxhrlrVxRC_ghEXb1gGobRX-A-77xOD8rmUItFTYPuadOtEhsfi6_Ayy-diedWSn2N8qweYCqHwAdr7RHoh5z8xgCwbmnsy-i8zzCBy9ZYHiXUvmGUpd19sbwAKwOFE3RuwokZNhZNN0lKhACG7oz3FNVqqr_agEXHioiXfq_fsT6aLbf4M8kL8C_0QHk4vjf0LgNVskKRImeohxgswCyzlC6Eog0yScRAfMUooRgSumWXoOuVajnXZ9afoQf5s6NGRzMeIUH9tSN-WSxyhyTTUeGc66LrlNVux9IPp5DvVF9smh9wo8-2qU-LMwGESOJ0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: ده‌ها موضع نظامی را در نزدیکی تنگه هرمز و مناطق ساحلی ایران هدف قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰ شب به وقت شرق آمریکا در ۱۴ ژوئیه، دور دیگری از حملات علیه ایران را به پایان رساند و ده‌ها موضع نظامی را در نزدیکی تنگه هرمز و مناطق ساحلی ایران هدف قرار داد.
جنگنده‌ها، پهپادها و شناورهای نیروی دریایی آمریکا در جریان این موج حملات هفت‌ساعته، مهمات هدایت‌شونده دقیق را علیه سایت‌های موشکی و پهپادی ایران، توانمندی‌های دریایی و سامانه‌های دفاع ساحلی به‌کار گرفتند تا توانایی ایران برای تهدید کشتی‌رانی تجاری و خدمه غیرنظامی را بیش از پیش تضعیف کنند.
این حملات در همان روزی انجام شد که نیروهای آمریکایی محاصره دریایی علیه شناورهای در حال تردد به مقصد یا از مبدأ بنادر و مناطق ساحلی ایران را از سر گرفتند. این محاصره امروز از ساعت ۴ بعدازظهر به وقت شرق آمریکا به اجرا درآمد.
نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که فرمانده کل قوا دستور دهد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77097" target="_blank">📅 06:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77092">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZzXkNhwf79rdmGV-KD8XE1zvuL3GK75xTzCkMrf8BF60lH_sHzn0NUpGeZuMHOc2BM4OZ9vosGaxFteD7JloYIQBYgJqA-NBmODkVMgcT1QcOjxZRjc1l7Od9qsCmbpA7Y_jWZDlx-qHyRZLW1Up6aO4fu6JmMFEcTSRhKUg1WUSBrKXoOnwRXw5JYv353BpVLKIxxl_fgkoMJf5XLoDuHbx7PRuG-hIflx-aMjfiejHY7pJTcucsIq6AFXRyctv4xjee1SJDrXdN6x745UzrDTTaA0y-E5jLX0bMXnKYap5xYhguJht2S5yBEylmnLMFgkmOAZ68LWeNEsXNG17Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iYohBY3S2l8entr6dTg-bUSc7TJfuIYCGDaH_-L0hvXICVyuCP8YBAw12glniboN0hOsYLD4a-Q3ZzLhxjMtkWmUJw9vkimy6v56nzPOAuzJLhGRlo-3KJ2YGnRlrf9-arcDVqf3WNEirakC4cRp0gqqldz7edKPnGh6RyrJJJJgm9Kktw4H6IE_FBtN-8y6gcYnGcFQGY72WXO4KdlLD7aC4BDqXlwSV0qYXtvgGJ8NtkzjM2tTF8VFL9eLrnGngi5Sk1GuTu33qTrBK6Tb1k6YpekJf9cEQ2ZpuqCCFdRjLYA2Y1eYRKi3sQ0Ur9vIOllEH4s2IasfjRlnhkuLJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4e711947a.mp4?token=aF5qaVS3pmUUKd7lHZvKVfgO9NXO0s1wsvR0NKhQvoQ1HULDAGZads5he0pl6J7Hulq1ZBKnk-v5v8650Rgigmi-bWpQXID9g225cp8PeNXWhb519fne4dssu_CYV0fgNSd-31ERUu6tdzOk4RxwVPD1JA9BotQFGoM8fI-cd1oAspvluGTEt9a7BsMlUE7xM8IUP4Jk8qT_K_XJL72zKm1WKWIs6T3eLVMtA2glx0buLARvvS-PEZvMoMJtv5G8sFZN-qe6n-_XFXRs9mK2IuG-R12CIJuieU_vAtaJeDmf_lBpoO4-9WVbvo79Tm_OARNJ6mqtyUEAqqVYgPlMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4e711947a.mp4?token=aF5qaVS3pmUUKd7lHZvKVfgO9NXO0s1wsvR0NKhQvoQ1HULDAGZads5he0pl6J7Hulq1ZBKnk-v5v8650Rgigmi-bWpQXID9g225cp8PeNXWhb519fne4dssu_CYV0fgNSd-31ERUu6tdzOk4RxwVPD1JA9BotQFGoM8fI-cd1oAspvluGTEt9a7BsMlUE7xM8IUP4Jk8qT_K_XJL72zKm1WKWIs6T3eLVMtA2glx0buLARvvS-PEZvMoMJtv5G8sFZN-qe6n-_XFXRs9mK2IuG-R12CIJuieU_vAtaJeDmf_lBpoO4-9WVbvo79Tm_OARNJ6mqtyUEAqqVYgPlMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح:  انفجار حمله به چابهار حدود ساعت ۵:۳۰
چهارشنبه ۲۴ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77092" target="_blank">📅 06:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77091">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YI9iA-kGZSAFYvvz8a14lI0c_wa5hp6nHxU2nTmpDc3vbk_DCIF9LVzvOXyxH5vrG4Z_F2CWEyRnBz6ut0I5CYlEqzPojOtUGEP1DTns5Wn8I6Ju-HTwkavhpq8A0E4Dx_9mqjTXj2QrWHKC_2BDrpLjqsZb7e-ydSNMgLLCew26xXXbwhHHX6ALc4jBr1JAQmmjETDG5Ct6w_maBRdnHVeCnfioJmF4PTSPqdLsqhiqjm9UDIXeRh32soEaLBpwjYrpkp3ZSQyc2dZk3ThGyzKsDsxnBTCbwq2oLuuJA2txTaz0wWMS22r1pFH9iw-bR7sml9n10I1To71y8k1P2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از سیستان و بلوچستان:
چابهار پایگاه مستقل امام علی همین الان دوتا زد
سلام کنارک الان دو تا زد
سلام همین الان صدای چهار انفجار در کنارک
۵:۳۰ دقیقه چابهار سمت دریا کوچیک فکر کنم زدن. صدای جنگنده ها میومد.
ساعت ۵:۲۰ صبح جنگنده وارد حریم چابهار شد پایگاه امام علی و کنارک زد
کنارک دوباره یکی زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77091" target="_blank">📅 05:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77090">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پیام‌های دریافتی دوباره هم‌زمان از سربندر و ماهشهر:
همین الان بندر امام خمینی‌ رو زدن سه بار
یا خدا سه تا انفجار وحشتناک سربندر
بعدی
وحید جان سلام ماهشهر صدای چندین انفجار متوالی
سلام ماهشهر الان زد نسبت به قبلیا موجش بیشتر بود
همین الان صدای شدید ماهشهر، نمیدونم کجا رو زدن
سلام اقا وحید سربندرو همین‌الان‌چهار بار زدن
ماهشهر الان ۴تا زدن
۵تا شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77090" target="_blank">📅 05:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77089">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/REX8Kj31UpofN3Ug3auvkXDHXpB6hGR7Y8wztX-Cw-wK903xC8XGN-DY1sVWVm8VSZIf02B-anknAOYNTcaT0VK_XIEKYM44DOzXE7TqZYgEJx5ekVdqmkAakP0aBl2f3tXG-AYprvJq9hVOUa_bZdpB1Z2XoRl-rrWXLReT1HV9QJ9D9rsC7c6vQezl3ax2swKwIpQoCSWTfHJt30NoY-bHNjYOd1i59W8L6YD__KTefRvOkTTtT1drVe7HEwccNYYnJkIZS4y-XWxG0xzmpcCkHJkkTghQApdouhHWbAkm3GCBpUHD6faSjTmCaF2tPYM4QssZ8qJHeAY-MdOZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از پیام‌های مربوط به شهر بوشهر، پیام‌هایی از شهر جم در استان بوشهر داشتم درباره شنیده شدن صدای انفجار:
۴/۲۵ همین الان ۳موشک به فرودگاه جم برخورد کرد قبلن از اونجا موشک میفرستادن
جم بوشهر
فرودگاه جم
الان صدای چند انفجار در شهرستان جم استان بوشهر شنیده شد.
دیشب هم همین موقع صدای چند انفجار شنیده شد.
همین الان فرودگاه جم رو زدن
درود وحید همین الان جم سمت پایگاه چمران نه سمت فرودگاه توحید دوتا صدای خیلی آروم اومد بعد دود سفیدی بلند شد و نورانی، معلومه موشک خواستن بفرستن نرفته
جای همیشگی نبود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77089" target="_blank">📅 04:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77088">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر صدای انفجار همین الان
انفجار ساعت ۴:۳۸ خورموج بوشهر
سایت موشکی را زدن
بوشهر ششم شکاری هوایی [رو] زدن
ساعت ۴:۴۰
سلام وحید جان شبتون بخیر ساعت 4:41 بهمنی رو دو بار تا الان زدن و همینجوری دارن میزنن پشت سر هم پایگاه هوایی
انفجار خیلی وحشتناک بوشهر ساعت ۰۴:۴۱
وحید بوشهر ۴:۴۱ پایگاه هوایی یا دو طفلان مسلم
😂
بوشهر الان زدن ۴:۴۱
درود وقت بخیر
بوشهر همین الان یک صدای انفجار بشدت بلند اومد
سلام ساعت 4:40 صدا بزرگ انفجار از بوشهر اومد
۴:۴۰ بوشهر یه انفجار بزرگ
وحید ۲.۳ انفجار سنگین در بوشهر ۴:۴۰
وحید بوشهر ناحیه‌ی بهمنی صدای شدید انفجار
😭
😭
😭
😭
😭
😭
بوشهر زدن الان ۴:۴۰
شهر بوشهر ۰۴۴۰ زدن
سلام وحید الان بوشهر رو خیلی بد زدن مراقب خودتون باشید خیلی میزنن مراقب باشید ساعت ۴.۴۰ بوشهر بیسیم
وحید ما سنگی بوشهر هستیم صدا خیلی شدید بود درحدی که انگار صدمتر کلا فاصله داشت
بوشهر دو تا صدای بلند اطراف تنگک اومد
آقا وحید پایگاه هوایی بوشهر و زدن 4:40 صدای انفجار خیلی بلند بود
داداش بوشهر شش دقیقه پیش یچیز سنگین زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77088" target="_blank">📅 04:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c6ee4fb2.mp4?token=ARuA5PU5jFniL66e6yqkIrwA5rW1CY7TNh5psRR2y3tiaaBJz3u6Vw5BTLFkSUaLTkSCWRVeC-Jac4pfKs9Cf8OSof6e7Z9NIu_cl0gTMOs__srz8_D2UwRSJKCL76o_gtQtSdRtDOW9FHIXK2gVZiAXVRhm7Y__HgYxtltVN8EYeaLxMUw2L-_SEibS96UHEkTAMixmirYf2WCP-n8F8ipsRlykQlw9_czW0_9zxncQR5OBByfTx4cFX7llr7otFspfuSQUHTjhJiIJRzoM7a9VQsrVF90BuaoLIdgM0kZzzhd-Fnx4sdyITGUPSNL59B7yqOom5jZtxfgVzwBlaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c6ee4fb2.mp4?token=ARuA5PU5jFniL66e6yqkIrwA5rW1CY7TNh5psRR2y3tiaaBJz3u6Vw5BTLFkSUaLTkSCWRVeC-Jac4pfKs9Cf8OSof6e7Z9NIu_cl0gTMOs__srz8_D2UwRSJKCL76o_gtQtSdRtDOW9FHIXK2gVZiAXVRhm7Y__HgYxtltVN8EYeaLxMUw2L-_SEibS96UHEkTAMixmirYf2WCP-n8F8ipsRlykQlw9_czW0_9zxncQR5OBByfTx4cFX7llr7otFspfuSQUHTjhJiIJRzoM7a9VQsrVF90BuaoLIdgM0kZzzhd-Fnx4sdyITGUPSNL59B7yqOom5jZtxfgVzwBlaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
تصاویری که بنا بر گزارش‌ها پیش‌تر در جریان حملات پهپادی و موشکی ایران به کویت ضبط شده‌اند، لحظه اصابت یک پهپاد شاهد-۱۳۶ را نشان می‌دهند. آمریکا همچنان با ایران به تبادل حملات ادامه می‌دهد و اکنون اهدافی در بحرین و کویت زیر سنگین‌ترین آتش ایران قرار گرفته‌اند.
sentdefender
,
MenchOsint
ستاد کل ارتش کویت، بامداد چهارشنبه، با انتشار بیانیه‌ای اعلام کرد که پدافند هوایی این کشور در حال مقابله با حملات پهپادهای «متخاصم» است.
این ستاد با تاکید بر اینکه صدای انفجارهای احتمالی ناشی از رهگیری این پرتابه‌ها توسط سامانه‌های دفاع جوی است، از مردم خواست تا دستورالعمل‌های امنیتی صادره از سوی مراجع مربوطه را رعایت کنند.
@
VahidOOnLine
وزارت کشور بحرین، با انتشار هشداری فوری در حساب رسمی خود در اکس، اعلام کرد آژیر خطر به صدا درآمده است و از شهروندان و ساکنان خواست آرامش خود را حفظ کنند و به نزدیک‌ترین مکان امن بروند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77087" target="_blank">📅 04:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77086">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری جمهوی اسلامی ساعت ۲:۵۶
حمله به یک واحد تولید آب معدنی در موسیان
🔹
دقایقی قبل، یک واحد تولید آب معدنی در اطراف روستایی در بخش موسیان (استان ایلام) هدف سه پرتابه دشمن قرار گرفت.
🔹
مراد یگانه فرماندار دهلران بامداد چهارشنبه به خبرنگار ایرنا گفت که این حمله هیچ تلفاتی نداشته است.
🔹
وی اظهار کرد که در این تجاوز به تجهیزات کارخانه خساراتی وارد آمد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77086" target="_blank">📅 03:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77085">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c0dd68356.mp4?token=Xo3Si2IVKmqHNkbKMCXecr8m0eSNayY8SmcWM9aWnLq7uc4udrj6brBIUyceIfkuwM8FLyVi1ORGHmFJgNCntBD74ky3v_Fk-d0alIE1kvefuoDYAevFentC4rx0-y-y_UWrBFUwprA3Xf1x0d8splP9lKrLmH76jx21Xco-n0DN5xyA5a1Khdz63g7FvryiItN6GGsNodYb3IZB-t2ZU6jYf2wQEs5lFNSDsh1_RXgnJvdJm7Fb2ZE9edE8c5hZ2UDOLRN9ZLOPd981sELoUUbEl4VNDKohYyvlyWseABpsLedtJgA0bFUqglCmXis_OvFH9qAO0BUNwdaBgefGMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c0dd68356.mp4?token=Xo3Si2IVKmqHNkbKMCXecr8m0eSNayY8SmcWM9aWnLq7uc4udrj6brBIUyceIfkuwM8FLyVi1ORGHmFJgNCntBD74ky3v_Fk-d0alIE1kvefuoDYAevFentC4rx0-y-y_UWrBFUwprA3Xf1x0d8splP9lKrLmH76jx21Xco-n0DN5xyA5a1Khdz63g7FvryiItN6GGsNodYb3IZB-t2ZU6jYf2wQEs5lFNSDsh1_RXgnJvdJm7Fb2ZE9edE8c5hZ2UDOLRN9ZLOPd981sELoUUbEl4VNDKohYyvlyWseABpsLedtJgA0bFUqglCmXis_OvFH9qAO0BUNwdaBgefGMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش:
منابع محلی از افزایش آمار مجروحان حمله به تیپ ۳۸۸ ارتش در
#بمپور
خبر دادند؛ دست‌کم ۵۰ مجروح، دست‌کم دو فوتی در بیمارستان و گزارش‌هایی از تلفات گسترده در داخل پادگان
بر اساس تازه‌ترین اطلاعات دریافتی،
تاکنون دست‌کم ۵۰ مجروح به مراکز درمانی، به‌ویژه بیمارستان خاتم‌الانبیا ایرانشهر، منتقل شده‌اند و حال هفت نفر از آنان وخیم گزارش شده است.
به گفته منابع حال‌ وش: «از میان مجروحان منتقل‌شده به بیمارستان، تاکنون دست‌کم دو نفر بر اثر شدت جراحات جان خود را از دست داده‌اند و وضعیت هفت نفر دیگر نیز بحرانی است. روند انتقال مجروحان همچنان ادامه دارد.»
منابع افزوده‌اند: «همزمان گزارش‌های متعددی از داخل تیپ ۳۸۸ حاکی از آن است که
شمار کشته‌شدگان در محل حمله بسیار بیشتر از آمار منتقل‌شدگان به بیمارستان است و ده‌ها نفر در داخل پادگان جان خود را از دست داده‌اند.
با این حال، به دلیل محدودیت‌های امنیتی و جلوگیری از دسترسی به محل، امکان راستی‌آزمایی مستقل این آمار تاکنون فراهم نشده است.»
به گفته منابع محلی، بخش‌هایی از آسایشگاه سربازان و سایر تأسیسات داخل پادگان در زمان وقوع حملات هدف قرار گرفته و همین موضوع موجب افزایش شمار تلفات و مجروحان شده است. همچنین تدابیر امنیتی در اطراف تیپ همچنان ادامه دارد و از نزدیک شدن شهروندان و خانواده‌های نظامیان به محل جلوگیری می‌شود.
حال‌ وش
پیش‌تر
از وقوع چندین موج حمله، شنیده شدن دست‌کم ۱۱ انفجار، ورود آمبولانس‌ها به داخل تیپ، خاموش شدن کامل چراغ‌های پادگان و انتقال مجروحان به بیمارستان خاتم‌الانبیا ایرانشهر خبر داده بود.
تا لحظه تنظیم این گزارش، هیچ‌یک از مقام‌های جمهوری اسلامی درباره آمار کشته‌ها، مجروحان، میزان خسارات و جزئیات این حمله اطلاع‌رسانی رسمی نکرده‌اند. اطلاعات منتشرشده در این گزارش بر پایه اظهارات منابع محلی و شاهدان عینی است و حال‌ وش همچنان در حال پیگیری و راستی‌آزمایی ابعاد این رویداد است.
haalvsh
همزمان با انتقال شمار زیادی از مجروحان حمله به تیپ ۳۸۸ پیاده مکانیزه نیروی زمینی ارتش در شهرستان بمپور به بیمارستان خاتم‌الانبیا ایرانشهر،
مرکز انتقال خون ایرانشهر با انتشار اطلاعیه‌ای از شهروندان واجد شرایط خواست برای اهدای خون به این مرکز مراجعه کنند.
haalvsh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77085" target="_blank">📅 03:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77084">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mgwS7WXiS0JKIsJ0Yh4pfi6nkOUWCpxJiWeEv0W_2jXZ8-18fJphOuBaN8KMLnALTIHH0C8WVzNHOtLUyTAXaRssLeFCmRGMHZxyoE47JsJ9DLsq7tPwoXP2nLiiaMkupp9cXN27BCe1dTcgjOfdvKk_paSlHwDz04wR5jV56f_PLUf6vMcTIoQ1GnwKFNy0u2j7V2KO5mOHkj66FKq5VOz4crFcnCTKMLr1MMdKQVWsm3EDTqDa9jGPbvMPBD5fHCtTL0xb_MzpQtIV7_xacK8CabwoLM-54NaMk5k-lr9s1pLAqzx5sNls2HgaAkvwPvDnUgDKHCKcHva32gCfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام، با انتشار بیانیه‌ای اعلام کرد جمهوری اسلامی طی هفت روز گذشته با حمله‌های عمدی به غیرنظامیان در سراسر منطقه، هفت کشتی تجاری را هدف قرار داده است. به گفته او، در نتیجه این حمله‌ها نزدیک به ۱۲ نفر از خدمه غیرنظامی کشته، مفقود یا زخمی شده‌اند.
@
VahidOOnLine
تصویر انگلیسی رو سنتکام منتشر کرده متن فارسی رو بالاش اضافه کردم. ترجمه ماشین:
بیانیه فرمانده ستاد فرماندهی مرکزی ایالات متحده
«ایران طی هفت روز گذشته با حمله به هفت کشتی تجاری، عمداً غیرنظامیان را در سراسر منطقه هدف قرار داده است؛ حملاتی که در نتیجه آن نزدیک به دوازده تن از اعضای غیرنظامی خدمه کشته، مفقود یا زخمی شده‌اند.
نیروهای ایرانی همچنین ده‌ها موشک و پهپاد به‌سوی کشورهای همسایه در حاشیه خلیج فارس پرتاب کرده‌اند. نیروهای ایالات متحده، ایران را به‌دلیل این تجاوز بی‌دلیل که همچنان جان افراد بی‌گناه را به خطر می‌اندازد، پاسخگو می‌کنند.»
دریاسالار برد کوپر، فرمانده سنتکام
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77084" target="_blank">📅 03:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77083">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d1f952110.mp4?token=XIHm0ydQNm7x3078akVVuDlxl9M1moVy0LRhBLG7lFd9A13bRI4712jKrUoYy7cTMCxTvdHGYv-gwommpJLnz5nb0gdYOlt9FdxnVySyG5x5JW8aOwfuq-tn5iN6CnmOAaCyJoNEcADn60JOezgY7lkvvW0uuWA8H3PHhDaP4v3NwllkoeDkCxMQCk-wTsGgBuG6u-D94SB1TTpe3c4I18UsgWY0JsTxLBn2OTCZxc6bdhfzCBAM1HOKqstvsCfqToRjIBg6Dg8QNj4_wFZyeeAxJLanvRLX4dzCIxowQYNh0_pQdet_HH2sKEVwX0DYnioMMZEXWW2ylO_89iubtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d1f952110.mp4?token=XIHm0ydQNm7x3078akVVuDlxl9M1moVy0LRhBLG7lFd9A13bRI4712jKrUoYy7cTMCxTvdHGYv-gwommpJLnz5nb0gdYOlt9FdxnVySyG5x5JW8aOwfuq-tn5iN6CnmOAaCyJoNEcADn60JOezgY7lkvvW0uuWA8H3PHhDaP4v3NwllkoeDkCxMQCk-wTsGgBuG6u-D94SB1TTpe3c4I18UsgWY0JsTxLBn2OTCZxc6bdhfzCBAM1HOKqstvsCfqToRjIBg6Dg8QNj4_wFZyeeAxJLanvRLX4dzCIxowQYNh0_pQdet_HH2sKEVwX0DYnioMMZEXWW2ylO_89iubtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Vahid
پیام‌‌های دریافتی:
وحید جان همین الان تبریز موشک زدن باز
سلام وحید از تبریز موشک فرستادن ۲:۱۰
سلام آقا وحید ساعت ۲:۱۲ دیقه از تبریز تا الان که ساعت ۲:۱۴ هستش دوتا صدای موشک اومد
سلام وحید جان همین الان ساعت ۲:۱۴ صدای های انفجار میاد از ارومیه
مشخص نیست پرتابه موشکه یا چی
پرتاب موشک از حوالی تبریز به جای نامشخص، صدای غرش خیلی شدید و بی سابقه
سلام وحید دو سه دقیقه پیش از سایت موشکی [...] دو موشک  پرتاب کردن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77083" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77082">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c39cdf8b03.mp4?token=M-m63Kql5Qw3ilMLGFaa332ZXTDlTRDVfc7GKfNsff_Vcd4UkUJYh8l3xyZzRJoRiusEPXeRVMUG6d2esKcTAsBMJXGPdWIwCWnxJdW54lQjHhEwogfPzLioWMEVVwkU8IICkIcVT5C7OxUqmhxKFp2z7XGg--qVSTT6Vip5BBgELwfDTO9AwQdOanGYwrVq8Lx8rYHDHlAx-RepbarU5gKRLssVAfV552Z9gkNIivHs1Roaz37bHI_r_y4tlFkJfGhx0giOayN4srQwdGiHMQLSdaJX5ZkLPaakS8iXkNOIQGcI-TuWPExkVbNrj95othIqVVi_qXMaqrnTysNKxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c39cdf8b03.mp4?token=M-m63Kql5Qw3ilMLGFaa332ZXTDlTRDVfc7GKfNsff_Vcd4UkUJYh8l3xyZzRJoRiusEPXeRVMUG6d2esKcTAsBMJXGPdWIwCWnxJdW54lQjHhEwogfPzLioWMEVVwkU8IICkIcVT5C7OxUqmhxKFp2z7XGg--qVSTT6Vip5BBgELwfDTO9AwQdOanGYwrVq8Lx8rYHDHlAx-RepbarU5gKRLssVAfV552Z9gkNIivHs1Roaz37bHI_r_y4tlFkJfGhx0giOayN4srQwdGiHMQLSdaJX5ZkLPaakS8iXkNOIQGcI-TuWPExkVbNrj95othIqVVi_qXMaqrnTysNKxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز سه‌شنبه، در گفتگو با «فاکس‌نیوز» در پاسخ به مجری که از او پرسید حمله‌ها تا چه زمانی ادامه خواهد داشت، گفت: «تا زمانی که من بگویم کافی است.»
او گفت آنها (حکومت ایران) هنوز تا حدودی توانایی جنگیدن دارد اما چیز زیادی برای آنها باقی نمانده است.
ترامپ در پاسخ به مجری که از او پرسید، اکنون وضعیت را چگونه توصیف می‌کند، آیا جنگ از سرگرفته شده، گفت: می‌توانید هر نامی روی آن بگذارید اما ما ضربه بسیار سختی به آنها زده‌ایم. ترامپ بار دیگر بر اهمیت باز ماندن تنگه هرمز تاکید کرد.
ترامپ در پاسخ به مجری که از او پرسید آیا جنگ از این فراتر می‌رود و اهداف مرتبط با انرژی ایران نیز در فهرست قرار دارند گفت: انرژی را برای بعد نگه‌داشته‌ام.
ترامپ افزود: امشب و فرداشب و پس‌فردا‌شب، ضربات سنگینی به آنها می‌زنیم و هفته آینده برای آنها خیلی بد خواهد شد. هفته آینده نوبت نیروگاه‌ها و پل‌ها است.
رئیس‌جمهوری آمریکا گفت: هفته آینده همه پل‌ها و نیروگاه‌های آنها را از بین می‌بریم مگر اینکه پای میز مذاکره بیایند.
رئیس‌جمهوری آمریکا پیش‌تر نیز این تهدید را مطرح کرده بود اما پس از آن اعلام شد که مذاکرات از سرگرفته می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77082" target="_blank">📅 01:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77080">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/203d452dd4.mp4?token=tVdMLDni7if4cKteHFsUk5NsxUsdtO-ZAjzyrtfVxVuzWs_Ern9DRuAs2c2epsW6fJ55ZJo7KUcNfdntmKoEFRpn8ROmOqHxX5m-zbWYTtt5w1H_lANVvD_mpYT-S7GRudsUlEfQiFtYLpm83s_k6-jdhCyxeDg7YND7saGqSPIraUqGLXnvM5phubX00oEi1g5DJbaCG5WxP1GsHY5NgUwoPTcm1caCedshNiSdVsx6ELyTPvF6dp11O1AUKCmiYGeDxMz8Gua55_uADkStXyjaqDe485VvmTV8D0uqsf8YCu6vXe5-tVKzSyX4uUwPOLi6OCks0BmZO7PvPmm90w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/203d452dd4.mp4?token=tVdMLDni7if4cKteHFsUk5NsxUsdtO-ZAjzyrtfVxVuzWs_Ern9DRuAs2c2epsW6fJ55ZJo7KUcNfdntmKoEFRpn8ROmOqHxX5m-zbWYTtt5w1H_lANVvD_mpYT-S7GRudsUlEfQiFtYLpm83s_k6-jdhCyxeDg7YND7saGqSPIraUqGLXnvM5phubX00oEi1g5DJbaCG5WxP1GsHY5NgUwoPTcm1caCedshNiSdVsx6ELyTPvF6dp11O1AUKCmiYGeDxMz8Gua55_uADkStXyjaqDe485VvmTV8D0uqsf8YCu6vXe5-tVKzSyX4uUwPOLi6OCks0BmZO7PvPmm90w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش:
ویدئوهای جدید از حملات و انفجارهای شدید در محدوده تیپ ۳۸۸ ارتش در شهرستان بمپور
بامداد امروز چهارشنبه ۲۴ تیرماه ۱۴۰۵، ویدئوهای جدیدی از حملات و وقوع چندین انفجار شدید در محدوده تیپ ۳۸۸ پیاده مکانیزه نیروی زمینی ارتش، واقع در نزدیکی روستاهای ریکپوت و کلاهدوز از توابع شهرستان بمپور ، به دست حال‌ وش رسیده است.
به گفته منابع حال‌ وش: «در این ویدئوها، صدای انفجارهای پی‌درپی و نور ناشی از اصابت‌ها در محدوده این مرکز نظامی مشاهده و شنیده می‌شود. شدت انفجارها به اندازه‌ای بوده که صدای آنها در روستاها و مناطق اطراف نیز شنیده شده است.»
منابع افزوده‌اند: «حملات در چند نوبت انجام شده و ویدئوهای تازه، بخش‌هایی از لحظات اصابت و انفجار در محدوده تیپ ۳۸۸ ارتش را نشان می‌دهد.»
حال‌ وش پیش‌تر گزارش داده بود که حوالی ساعت ۰۰:۰۵ بامداد، دست‌کم هشت انفجار شدید در محدوده روستاهای ریکپوت و کلاهدوز شنیده شده و منابع محلی از هدف قرار گرفتن تیپ ۳۸۸ پیاده مکانیزه شهید حیدر شهرکی خبر داده بودند.
تا لحظه تنظیم این گزارش، اطلاعات دقیقی درباره میزان خسارات و تلفات احتمالی منتشر نشده و مقام‌های جمهوری اسلامی نیز درباره جزئیات این حملات اطلاع‌رسانی رسمی نکرده‌اند.
haalvsh
لوکیشن دریافتی تایید نشده:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77080" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">در میان رگبار پیام‌های اهواز سه پیام متفاوت درباره جاده تهران-قم حوالی فرودگاه داشتم که نمی‌دونم چقدر درست هستند. هرچه صبر کردم پیام دیگری نیومد ولی اون اطرف کلی نقطه نظامی در بیابون هست که لابد کسی بهشون نزدیک نیست:
پیام ساعت ۲۳:۲۰
هم اکنون انفجار فرودگاه امام خمینی
صدای انفجار دور بود ولی لرزشش احساس شد
در پی مکالمه اضافه کرد: من اطراف فرودگاه هستم. چون اینجا بیابونه و نزدیک ترین لوکیشن بهمون همون فرودگاه هست اون  رو گفتم
پیام ساعت ۲۳:۲۳
سلام وحید جان جاده قدیم قم نزدیک اتوبان غدیر هستم صدای انفجار و لرزش اومد
زدیم ماشین رو بغل
پیام ساعت ۲۳:۲۶
سلام حسن اباد فشافویه نزدیک فرودگاه امام میشه صدای انفجار شنیدیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77079" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RykkYZQolFoPfAnf5MyONhBYAu8EpeXI0-v0DdaQD50pBxshWkn41CcsTLBBWCNxdMxSgrchhCpRbGjy0wd7l_95EGhN_eIlWxy_kqatcX9syybP9ERlXSAFa2v1Y7pCxPQb6IczT-sSyzvY-25V4xePZ1GQ0L3wJpdZx5c0vGHRhMHBk2ZSmShhH6m6EH-s4GcRSuh4CVU79T-j1-3FS8Fw2AlUCsD6ux0kE6Khl1ZJxLw8m5xsTrmYmGe5lTc1Jp3AdsJSJboQ6go2ghIXxIpwU5X8VsMqEH8p25cgROOAuPznUtsY1gdFxPzOcwIZXyxiAfR95xhAAza58DyIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، [
در پستی تازه
] اعلام کرد نیروهای آمریکایی از ساعت ۴ بعدازظهر به وقت شرق آمریکا [یعنی دقایقی پیش]، محاصره دریایی کشتی‌های در حال تردد به بنادر و مناطق ساحلی ایران را از سر گرفته‌اند.
سنتکام در پیامی در شبکه اجتماعی ایکس، این اقدام را پاسخی به آنچه «حملات اخیر و غیرموجه ایران به کشتی‌های تجاری و خدمه غیرنظامی» خواند، توصیف کرد و افزود آمریکا جمهوری اسلامی را مسئول این حملات می‌داند.
بر اساس این بیانیه، در حال حاضر بیش از ۲۰ ناو جنگی نیروی دریایی آمریکا و صدها هواپیمای نظامی در سراسر خاورمیانه مستقر هستند و نیروهای آمریکایی «هوشیار، آماده و دارای توان رزمی» باقی خواهند ماند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77078" target="_blank">📅 23:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77077">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ساعت ۲۳:۱۸ یه انفجار دیگه
ساعت 11.19 اهوازو زدن
۲۳:۱۹ ، اهواز صدای انفجار اومد
وحید جان سلام
دوباره اهواز روزدندساعت ۲۳:۱۸
ساعت ۲۳:۱۹ اهواز صدای انفجار
سلام وحید جان 11:19 اهواز، زدن
اهواز الان زد سه راه باهنر موجش اومد ۲۳:۱۹
همین الان ۲۳:۱۹ اهواز دوتا پشت سرهم
ما کمپلوییم! خیلی نزدیک بود فکر کنم لشگر ۹۲ زرهی بود!
سلام اهواز صدای انفجار نمیدونم کجا ساعت 11:19
اهواز  الان  ۲۳:۱۹
سلام ما باهنر اهواز هستیم با اینکه کولر روشنه و فوتبال میبینیم ولی صدای دو انفجار حدود ساعت ۱۱.۲۰ شنیده شد
و کلی پیام مشابه دیگر که بعضی‌هاشون فقط نوشتند: همین الان یا دوباره
که چون ساعت و دقیقه نمی‌نویسند نمی‌دونم کدوم باره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77077" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار در بهبهان
بهبهان رو چند دقیقه پیش زدن خوابگاهمون کامل لرزید
سلام
چند دقیقه پیش شیشه های خونه وحشتناک لرزید
نمیدونم انگار تو شهر رو زدن
بهبهان زندگی میکنم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77076" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nmAfafe04JLY5qCHU10fN8lXaXGK4V2N8RK7ZFe0MqRgkrW0e-3yWPHoqs_7Zukr8BreNTomT-L3SLLZBwpIQK2Aweh5HEGX8AqlMOAiJ2KsNeB8myQzZGYERPUOuigpkhwGO_J5tdiwLnb_IlijEhPoY03IJlxXCaib2nhMQQvVlG-DCXTP8eDdym5-exsthnNKGlGCRA-GZM1G_Owetd4wjlc1pa2117V4ZdfDtdIfS7Il2_qjjbmDJMCIOx2NlCL9XvjCb4yas9KK_C45gc6jyqebuPpM69HacLhSmEJLWmcXqex70JQX5_kzz7EInIppfWHIORCTYXy4WAdG0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ تهران]، نیروهای فرماندهی مرکزی ایالات متحده دور دیگری از حملات علیه ایران را آغاز کردند تا به تضعیف توانمندی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز استفاده می‌شود، ادامه دهند.
این حملات در حالی انجام می‌شود که نیروهای آمریکایی خود را برای ازسرگیری محاصره دریایی بنادر و مناطق ساحلی ایران آماده می‌کنند. این محاصره از ساعت ۴ بعدازظهر به وقت شرق آمریکا [۰۰:۳۰ بامداد چهارشنبه] به اجرا درمی‌آید.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77075" target="_blank">📅 23:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
بندرعباس ۲۲:۴۴ صدای چند انفجار
بندرعباس ساعت 10:45 چهارتا صدای انفجار اومد
چند انفجار ممتد ساعت ۲۲:۴۵ بندرعباس موجش زیاد بود
ساعت ۱۰.۴۶ صدای انفجار خیلی بددد تو بندرعباس
درود وحید جان بندرعباس سمت باهنر چهارتا انفجار شدید بود
🔄
سلام بندرعباس انفجارهای پشت سر هم سمت منطقه۴  ۲۳:۰۸
بندرعباس ساعت 11:08 دوتا صدای انفجار دیگه اومد
ساعت ۲۳:۰۸ بندرعباس ۳ انفجار
باز بندر رو زدن 23:08
دو سه تا انفجار مهیب ، لرزوند ساختمان رو
۲۳:۰۸ صدای دو انفجار شرق بندرعباس
سلام آقا وحید بندرعباس دوتا صدا پشت سر هم اومد ساعت 23:08 دقیقه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77074" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77073">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ساعت ۲۲:۳۰ صدای ۲ انفجار
سلام اهواز رو الان زدددد
سلام وحید جان اهواز ساعت ۱۰:۳۰ صدای ۳ انفجار مهیب
همین الان اهواز صدای دوتا انفجار اومد
اهوازو زدن
درود وحید جان همین الان  صدای دوتا انفجار اهواز شنیدم. ساعت 22:31
اهواز ساعت ۲۲:۳۰
۳ تا انفجار
سلام وحید الان اهواز [رو] زد ۳ تاشو من شنیدم۲۲:۳۲
سلام اهواز [رو] همین دو دقیقه پیش دوبار زدن
سلام وحید جان اهواز همین الان دوتا صدا انفجار اومد. زمین لرزید.
ساعت ۲۲:۳۱ دوتا انفجار اهواز
سلام اهواز [رو] زدن خونه لرزید
سلام وحید اهوازو زدن ساعت ۱۰ نیم دو تا
سلام اهواز دو انفجار شنیده شد
وحید جون 2 انفجار اهواز 22:31
انفجار مهیب همین الان در اهواز صداا از سمت غرب اهواز بود. اونقدر شدید بود که زمین لرزید
سلام الان اهواز سه تا انفجار شنیدیم
سلام آقا وحید اهواز الان زدن صدای 2 انفجار نزدیک خونمون صدا مهیب بود
سلام وقت بخیر اهواز سمت کیانشهر صدا اومد ۲تا صدای زیاد
ب[ذ]ار فوتبال نگاه کنیم جون مادرت ۱ ساعت
🔄
۱۰:۳۵ دوتا انفجار دیگه اهواز
سلام اهواز [رو] زدن خونه لرزید
یکی دیگه زدن
۱۰:۳۵ دوتا انفجار دیگه اهواز
اهواز رو الان دوباره زد
هنوز اهوازو دارن میزنن ۲۲:۳۵
همين الان ١٠:٣٥ مجددا دو بار صداى مهيب توى اهواز
ساعت ۲۲:۳۴
۲ تا دیگه انفجار شدید اهواز
اهواز  . از ساعت ۱۰:۳۰ تا الان ۴ تا صدای انفجار
ما کوی نیرو هستیم اهواز
صدای دو انفجار اومد
حدود دو دقه پیش
وحید اهواز رو دوباره زد ساعت ۲۲:۳۵
سلام ساعت ۲۲:۳۴ سه انفجار در اهواز
همین الان اهواز برای بار چهارم انفجار مهیییب
با اینکه کولر روشنه ولی صداش خیلی بلند میاد
اهواز ساعت 20:37 چند انفجار پشت هم
۳ یا ۴ انفجار ، صدا از سمت ارتش 92 زرهی بود
صدا سمت  زرگان  کوروش کوی عابدی کم تر و بیشتر سمت کمپولو هست احتمالا لشکر باشه
سلام وحید جان.
تا ۲۲:۴۵ صدای ۵ انفجار شنیده شد که یکی از باقی بسیار صدای بلندتری داشت برای مایی که در نزدیکی پایگاه گلف و الحدید هستیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77073" target="_blank">📅 22:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77072">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgbLh2JNAi8TQJJQnRgRy7qPl-Vv5b7M0BdtjMEnIInhBV_H7YrzFj3utXigH2VhxjOZnDQcV1lvIaC_B0N7E5kXjJJSnjXNMquk9rP_B8oAgAvaEe8WE-lE7byXdUd-nDevtlqZegd4P9Q_SRIsQ_NGdjufukSm9L-5UYQ_2fEHzyOU_23PjRl6tZSZoPkW7FlyQVXuxh2HyY3u1ePMaRBs3qVF5kyPPt2RWk_wRQKfOmbpxI7lFzWZB3sqyWU66swizdRr4ZF9OXfrsF0G9px1XGb9k2qxLZffNGabeZnJ6H4u6JDFaMQtSHSMgT5XTLpXxUJOHud_Bo4wovVEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس به نقل از مقام‌های آمریکایی و اسرائیلی گزارش داد که رئیس‌جمهور آمریکا روز پنج‌شنبه در یک تماس تلفنی، به نخست‌وزیر اسرائیل گفت که این کشور باید خروج تدریجی نیروهایش از سوریه را آغاز کند و او را ترغیب کرد که اقدام مشابهی را در لبنان نیز انجام دهد.
بر اساس گزارش روز سه‌شنبه ۲۳ تیرماه این وبسایت، یک مقام آمریکایی گفت دونالد ترامپ به بنیامین نتانیاهو تأکید کرده که حضور نظامی اسرائیل در خاک سوریه تنش‌زا است و می‌تواند به تشدید درگیری‌ها منجر شود.
به گفته این مقام، ترامپ به نتانیاهو گفت: «آن‌ها شما را آن‌جا نمی‌خواهند. باید نیروهایتان را خارج کنید» و افزود که همین موضوع درباره لبنان نیز صادق است.
در مقابل، دفتر نخست‌وزیر اسرائیل اعلام کرد: «نخست‌وزیر بر ضرورت ایجاد مناطق حائل امنیتی در امتداد مرزهای اسرائیل تأکید کرده است».
این تماس، یک روز پس از دیدار رئیس‌جمهور آمریکا با همتای سوری خود، احمد الشرع، در حاشیه نشست ناتو در ترکیه انجام شد.
به نوشته اکسیوس، سه ماه مانده به انتخابات پارلمانی اسرائیل که برای بقای سیاسی نتانیاهو حیاتی است، بعید به نظر می‌رسد او گام‌های مهمی برای عقب‌نشینی نیروهای اسرائیلی از مناطق تحت کنترل در سوریه بردارد یا فراتر از آنچه پیش‌تر در لبنان پذیرفته، با خروج بیشتر موافقت کند.
ارتش اسرائیل در حال حاضر بخش‌های وسیعی از جنوب لبنان و جنوب سوریه را در اختیار دارد.
اعضای ارشد دولت اسرائیل خواهان کنترل نامحدود بر این مناطق هستند و برخی حتی از ایجاد شهرک‌های یهودی در آن‌جا حمایت می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77072" target="_blank">📅 21:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77071">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnP1Ja4OGLTq1w7K7w3jurOBrEAjdpMmbLL0isp7eEl8ALALqH32MmRUHaY-LjhbPRFnqwdanVt3mg0ueBzQ_1cK7mDfOR4bYWCcDHhDXbetmOnT9964Rgn_9bIj7Res0zXg666_ncA5N00NK4QYGOd9VA3430hwzt5QtlBC22Cf2JLSLxq0qh0zIKMsnj5qvq0zTodPJcE61D_lTgOBC_YJiIE2AAL2u3PqOaBNSDSzQUK2m1Rev4gbmBOUs6cTyXb_qWq-6HRkQGs0_zdS-BCnzhJT6T6C_Hc3rVNP2IJ9WFMYiDWCsBT974rbU0dgSvxWMVsy9yKoOQHFAlf4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه عربستان سعودی روز سه‌شنبه ۲۳ تیرماه با «محکومیت و انزجار شدید» از حملات ایران به چند کشور عربی، تهران را «مسئول عواقب ادامه این حملات ظالمانه» خواند.
در بیانیه این وزارتخانه، از هدف قرار گرفتن تعدادی از پاسگاه‌های مرزی کویت، یک سکوی حفاری دریایی متعلق به شرکت نفت کویت و حملات به سرکنسولگری کویت در شهر بصره عراق خبر داده و با اشاره به حمله ایران به اردن، بحرین، قطر و دو نفتکش اماراتی هنگام عبور از تنگهٔ هرمز، از «تداوم تهدید امنیت و ثبات منطقه توسط ایران» انتقاد شده است.
وزارت خارجه عربستان در این بیانیه «مخالفت کامل» خود را با آنچه «نقض حاکمیت کشورهای برادر توسط ایران، ادامه رفتار بی‌ثبات‌کننده آن در امنیت منطقه، و نقض اصول قوانین بین‌المللی، منشور ملل متحد، منشور سازمان همکاری اسلامی و اصول حسن همجواری» خوانده، اعلام کرده است.
عربستان ضمن درخواست برای توقف حملات ایران، بر همبستگی کامل ریاض با کشورهای هدف قرار گرفته، تاکید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77071" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77070">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GED4Rr6M1Pt4HQ3KuJZf37JSVy_MVrSOdbj-WxNID6v_gwPVDqjA44uaPIOJAQAQMvtfKjmSeyhu8DT8e8JVofaICxDirzxpRjZ5NxiF1w-kRWMRugvKbkQV5bg9Auc-t0bFP1wgVwtgx0XnGY3Ux8rafFtmlWgAWxYilCxBA0yor3JRPDTCaCZ9qneQfWVFISWPEaOo3VxKMOeLkpECeR25EO19fSnHM8WnSrYzhpQIpqHNddAHD6H96ZCHCXO0BHj1GXDV8IEOpkOcefYjFH-wrgQ_Pkocj3kkgDkGJiW5Tm6tjA68T3tCrL9F4zxqh_mjgYM4PBCyNBy7b64zvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا عصر سه‌شنبه ۲۳ تیرماه و ساعاتی قبل از آغاز رسمی بازگشت محاصرهٔ دریایی بر بنادر و کشتیرانی ایران گفت هیچ‌کس نباید برای عبور از تنگهٔ هرمز عوارض یا هزینه‌ای دریافت کند.
دونالد ترامپ در یک نشست خبری همراه علی الزیدی، نخست‌وزیر عراق، در کاخ سفید گفت که پس از اعلام قبلی‌اش مبنی بر دریافت ۲۰ درصد عوارض بر کشتی‌های عبوری از تنگهٔ هرمز، کشورهای مختلفی با او تماس گرفتند و گفتند به‌جای دریافت عوارض برای عبور از تنگه، مایل‌اند در آمریکا سرمایه‌گذاری کنند.
او با اشاره به کشورهای حاشیه خلیج فارس گفت این کشورها قرار است در آمریکا سرمایه‌گذاری کنند و فکر می‌کند این موضوع راه‌حل بهتری در مقایسه با دریافت عوارض است.
رئیس‌جمهور آمریکا با تمجید از علی الزیدی گفت اگر عراق به حفاظت نیاز داشته باشد، ما در کنار آن خواهیم بود.
او گفت ما در بخش نفت با عراق همکاری قوی خواهیم داشت و به زودی آن را اعلام خواهیم کرد. نیروهای آمریکایی عراق را ترک می‌کنند و شرکت‌های آمریکایی وارد می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77070" target="_blank">📅 20:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77069">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f1ccf9a2d5.mp4?token=mTJ0h_aM1b-tJUsdDC4SkqnkW6d0TpYFOVLZkKsJq6qSmE9kzXtMya8wfBSXDhyW9_BlPEKrbHUwB7_oXSMBz7rqh0oMj__MFHpqHdt97E_qVyj3ml0whzEh2UimfveEXysP4dt4Ffuv8MCUmxDNSQmeGLUCYKvNRw_3uHexPi0ZL3_YQGmH54PBCGHK3FhQwH7k0PJNmlf5IiQHwMPOsUvLL_YRUkHb5byo1nOQpFP9Qf6ReVHObdZo4HVLS5FfOkzZz0uPCjQYDASxF4rT3Bf_SoRAq-oLpPI8pFmCRumZBmeQqkR3ssUA2EIuFKlQmpaZ1OnK0L5Y7UbGVrl7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f1ccf9a2d5.mp4?token=mTJ0h_aM1b-tJUsdDC4SkqnkW6d0TpYFOVLZkKsJq6qSmE9kzXtMya8wfBSXDhyW9_BlPEKrbHUwB7_oXSMBz7rqh0oMj__MFHpqHdt97E_qVyj3ml0whzEh2UimfveEXysP4dt4Ffuv8MCUmxDNSQmeGLUCYKvNRw_3uHexPi0ZL3_YQGmH54PBCGHK3FhQwH7k0PJNmlf5IiQHwMPOsUvLL_YRUkHb5byo1nOQpFP9Qf6ReVHObdZo4HVLS5FfOkzZz0uPCjQYDASxF4rT3Bf_SoRAq-oLpPI8pFmCRumZBmeQqkR3ssUA2EIuFKlQmpaZ1OnK0L5Y7UbGVrl7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز سه‌شنبه ۲۳ تیر، در نشست خبری مشترک با نخست‌وزیر عراق در کاخ سفید، اعلام کرد که خاورمیانه در حال تجربه وحدتی بی‌سابقه است و دیگر خبری از ترس و وحشت ناشی از «قلدری» ایران در منطقه نیست.
ترامپ با بیان اینکه ایران پیش‌تر با رویکردی سلطه‌جویانه، کشورهای منطقه از جمله عراق را تحت فشار قرار می‌داد، تاکید کرد که اکنون توان نظامی این کشور درهم‌کوبیده شده و آن فضای رعب و وحشت از میان رفته است. او در بخشی از سخنان خود به سرکوب معترضان در ایران اشاره کرد و یادآوری کرد که آن‌ها ۵۲ هزار نفر از معترضان را به قتل رسانده‌اند.
رئیس‌جمهوری آمریکا در پایان ضمن اشاره به نزدیکی کشورهای منطقه به یکدیگر، نخست‌وزیر عراق را به عنوان یکی از رهبران بزرگ آینده در خاورمیانه توصیف کرد و افزود که این اتحاد منطقه‌ای، در سایه پایان یافتن دوران سلطه‌گری ایران، اکنون به واقعیتی دست‌یافتنی تبدیل شده است.
@
VahidOOnLine
دونالد ترامپ در نشست خبری با علی الزیدی، نخست‌وزیر عراق، در کاخ سفید گفت: «نخست‌وزیر عراق در انتخاباتی پیروز شد که بسیاری تصور می‌کردند فرد دیگری برنده آن خواهد شد. من هم در این موضوع نقش داشتم و برایم مهم بود کسی روی کار بیاید که بتواند این مسئولیت را به‌خوبی انجام دهد. اکنون یک قهرمان جدید و فوق‌العاده داریم و حضور او در کنار ما مایه افتخار است.»
ترامپ افزود: «شرکت‌های نفتی آمریکا با حجمی بی‌سابقه وارد عراق می‌شوند، با این کشور شراکت می‌کنند و همکاری گسترده‌ای خواهند داشت. روابط ما اکنون به سطحی رسیده که دیگر نیازی به حضور نظامی آمریکا در عراق نیست. ما برای کمک به عراق حضور داریم و اگر لازم باشد از آن حمایت خواهیم کرد، اما فکر نمی‌کنیم چنین نیازی پیش بیاید.»
او درباره جمهوری اسلامی گفت: «ایران رقیب اصلی عراق بود و بار سنگینی بر دوش این کشور گذاشته بود، زیرا قلدر خاورمیانه محسوب می‌شد. اما اکنون ایران تا حد زیادی تضعیف شده و توان نظامی آن تنها بخش کوچکی از چیزی است که چهار ماه پیش بود. این وضعیت به عراق آزادی عمل بیشتری داده و یکی از دلایل ورود گسترده شرکت‌های نفتی آمریکا به عراق نیز همین موضوع است.»
@
VahidOOnLine
ترامپ با یادآوری دوران فعالیت خود به عنوان یک چهره غیرنظامی، گفت: «من همیشه می‌گفتم به عراق نروید و به آن حمله نکنید».
او با انتقاد از این مداخله نظامی و با اشاره غیر مستقیم به ایران، افزود: «صادقانه بگویم، آن‌ها به کشور اشتباهی حمله کردند و آسیب بسیاری به بار آوردند».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77069" target="_blank">📅 20:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77068">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BM0PmHC7Xv6rk52uWhlw26V6qGCUGWOIVeo43N1B_OFnLZmvRIyexu3vi-SxEPkwiDOPYdLVsnNVMZcR1Hwf4xPuULPXKHeizCBZrN00cWtpRtfWfKvqyzYdbz9Rez2RBW0TAk3ZgHLJB4BCN_kSCWgtzY_TCcBDvb4itt7WAftKwK2Zn4-KGK4zxGKnq3wWUVahX2HBEVF7v20iSMD_L5YJe099vOcHKNhJEhKf8KjQWqFNvIAXbdt5AY8SUZ3EHjPJXm5X3YhpgQj5e7ni_T2AjXyxwgTryBzP1hgJsYvUlzT5Inu5KiL_moXm7dOl-uLcCE366WYqEZ15OrTjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: صدور هشدار خطر در کویت، همین الان
رسانه‌های ایران عصر سه‌شنبه بدون بیان جزئیات بیشتر از شنیده شدن صدای انفجار در اندیمشک و جزیره قشم خبر دادند.
صداوسیمای جمهوری اسلامی به نقل از استانداری هرمزگان گفته که ساعت ۱۹ به وقت محلی، «نقطه‌ای» در جزیره قشم هدف حمله آمریکا قرار گرفت. صدا و سیما همچنین از شنیده شدن صدای انفجار در اندیمشک خبر داد.
هم‌زمان، ستاد کل ارتش کویت با صدور پیام هشداری از رهگیری «اهداف هوایی متخاصم» در این کشور خبر داد.
در بیانیهٔ ارتش کویت با درخواست از شهروندان برای رعایت دستورالعمل‌های امنیتی گفته شده که صداهای انفجار احتمالی ناشی از فعالیت پدافند هوایی در رهگیری حملات متخاصم است.
خبرگزاری فرانسه هم از شنیده شدن صدای انفجارهایی در کویت خبر داده است.
@
VahidHeadline
سپاه پاسداران در بیانیه‌ای حملات شامگاه سه‌شنبه به «مواضع دشمن» در خاک بحرین و کویت را تایید کرد و گفت عملیات «نصر۲»، پاسخ به حملات عصر سه‌شنبه آمریکا به تعدادی از ایستگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی بوده است.
در این بیانیه آمده است، در صورت تکرار حملات، مقابله به مثل جمهوری اسلامی ادامه خواهد داشت و این «تجاوزها» نتیجه‌ای جز تاخیر در بازگشایی تنگه هرمز ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77068" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77067">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIr7N0g1xM7iBTt0sfpW7mdywG6RF3y92k5vWYVlVyiXAhvBKlKKV2XJ6iG688ekoSFaYFc1eI-Xs2KBUfvBryN9Gpc-50-LTUEcrzCPMDy5-jyowTcvheFcEcWIMth4bP12H-LAsBA4WomXd8AAxh7rj0DBFlVU3cyBysJYkNLVh0N05JilJlwQYG9DdKJtJJRROmUMOcquRvHmglyJoTEfXOpFU71A1_ynRcVFPOUCFcJ7-kdKVtgKshYbfhIzrBc7LK201n62z33PQZ4lNQdes8xET_GLWGQBqRAcpy7T1qD6hXBsLjHHrADbxcifRX0eU7TkJyL3fCxKLSq72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تنگه هرمز به روی تردد همه کشتی‌ها، به‌جز کشتی‌ها و محموله‌های مرتبط با ایران، باز است
ترجمه ماشین:
نفت به لطف قدرت شگفت‌انگیز ارتش ایالات متحده، بیش از هر زمان دیگری در جریان است. درود ویژه به وزیر جنگ، پیت هگست، رئیس ستاد مشترک نیروهای مسلح، دن کین، و فرمانده ستاد فرماندهی مرکزی ایالات متحده، دریاسالار برد کوپر. به لطف آن‌ها و همه اعضای قدرتمندترین ارتش جهان ــ با اختلاف بسیار زیاد ــ تنگه هرمز به روی تردد همه کشتی‌ها، به‌جز کشتی‌های ایران، باز است؛ و این به‌دلیل رهبری دروغگو، خشونت‌طلب و بدخواه ایران است که این کشور را به مسیر نابودی کامل می‌کشاند.
بنابراین، ما یک محاصره کامل خواهیم داشت، اما فقط علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هر چیزی مرتبط با محموله‌های ایرانی حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده با رهبران خاورمیانه،
تصمیم گرفته‌ام «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌های تجاری و سرمایه‌گذاری جایگزین کنم که کشورهای مختلف حاشیه خلیج فارس در ایالات متحده انجام خواهند داد.
این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.
همان‌طور که همه می‌دانند، ما بیشترین میزان سرمایه‌گذاری دلاری در ایالات متحده از سوی هر کشوری در تاریخ را داریم، اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهند کرد و شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطوحی تاریخی خواهیم بود؛ امری که میلیون‌ها شغل پردرآمد دیگر برای آمریکایی‌ها ایجاد خواهد کرد!
آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای بی‌سابقه. دوران کشته شدن صدها هزار نفر، از جمله ۵۲ هزار معترض، به دست ایران به پایان رسیده است و مهم‌تر از همه، ایران هرگز به سلاح هسته‌ای دست نخواهد یافت!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77067" target="_blank">📅 18:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77066">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4730c53847.mp4?token=LqvlpICuiReDNT-y4X8Ab5ium0p4nkK5L1iUbLuVgUqkZhV4fuThEMPUOgyM3F4zDzlIeq-ph9XSkmL6mq8f29SWm9iOQB13O7lI6Ss9kA-r7LKjWhC6ssOnpyfMa1Gldy7hgNnN8A0eXILd6tKsAte16K0Ua5xXcg-FhKYLxLVNm6o-nvRcS5b_6tAuGPq3VwtT08kB9SgmppDlWks65zPGA4oi0gzpY6RZYRR6QQUYtVm7rDgJBhviB3xsGYhc95KXmVTsrNUxAyNgpA8Y1lT0V6mZ1lz8sCsYj-qZonlL_cbT_RWYlHgFseuJPbTB0twVUv5v5VoWMAQbVDyC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4730c53847.mp4?token=LqvlpICuiReDNT-y4X8Ab5ium0p4nkK5L1iUbLuVgUqkZhV4fuThEMPUOgyM3F4zDzlIeq-ph9XSkmL6mq8f29SWm9iOQB13O7lI6Ss9kA-r7LKjWhC6ssOnpyfMa1Gldy7hgNnN8A0eXILd6tKsAte16K0Ua5xXcg-FhKYLxLVNm6o-nvRcS5b_6tAuGPq3VwtT08kB9SgmppDlWks65zPGA4oi0gzpY6RZYRR6QQUYtVm7rDgJBhviB3xsGYhc95KXmVTsrNUxAyNgpA8Y1lT0V6mZ1lz8sCsYj-qZonlL_cbT_RWYlHgFseuJPbTB0twVUv5v5VoWMAQbVDyC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۲۳ تیرماه هشدار داد که اگر تهران حملهٔ جدیدی به کشورش انجام دهد، اسرائیل با تمام قدرت به ایران ضربه خواهد زد.
@
VahidOOnLine
ویدیویی که دفتر نتانیاهو منتشر کرده، ترجمه ماشین:
ما برای هر سناریویی آماده‌ایم. فقط یک چیز می‌توانم به شما بگویم... نه، این را به رهبران ایران می‌گویم:
اگر به ما حمله کنید، روی آرامش حساب نکنید. تصور نکنید آنچه در گذشته رخ داد، دوباره به همان شکل تکرار خواهد شد؛ زیرا این بار، تکرار گذشته نخواهد بود.
حمله قبلی به‌اندازه کافی قدرتمند بود؛ حمله بعدی بسیار قدرتمندتر خواهد بود.
دورانی که کسی به ما ضربه بزند و ما با ضربه‌ای چند برابر پاسخ ندهیم، به پایان رسیده است. این کار را در برابر محور شرارتِ ایران انجام دادیم و در برابر هر کسی که به ما ضربه بزند نیز به همین مسیر ادامه خواهیم داد.
روش ما همین است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77066" target="_blank">📅 17:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77065">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYGIzrWSGZoEataKUjf24sQclXdO85DUrMD5fAq7tOvsLqQcnQ0mXx567lxayGMWNXWfJHlN6GrOEs4v3ij-inHJohQuXy11YFXXl5n--YSjtrWXkqj5O1QY-KGkONKYW4c5VXL_MmTVr9hLlJe6-quRnRMYjSy70RBGQiOIUdd6yASCbrzIKSQkvyxZm_7GdX7WwRkCE0D9vK1Ci0Wxnx1_TO8SJ6G1v2tzrWmBgWOm83NHZ5bYddWE6XdFk2mmDSQujQGJrjQIZE2S6yU2Wc89ahkBXJ2n-eP7xtP_MOgxWbsvHWQVqSbImN56o8rYX4-l3ViMwchU2LgQnh0Ohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع ارشد در تهران گزارش داد که اگر دونالد ترامپ تهدید خود برای حمله به تأسیسات زیرزمینی موسوم به «کوه کلنگ» را عملی کند، جمهوری اسلامی «پاسخی ویرانگر» خواهد داد. این تهدید در حالی مطرح شده که کوه کلنگ طی سال‌های اخیر به یکی از مهم‌ترین و امن‌ترین مراکز هسته‌ای ایران تبدیل شده است.
دونالد ترامپ، رییس‌ جمهوری آمریکا، روز گذشته در گفت‌وگویی رسانه‌ای اعلام کرد که واشینگتن یک مجموعه زیرزمینی عمیق در ایران را به‌دقت زیر نظر دارد. او مدعی شد هرچند در حال حاضر نشانه‌ای از فعالیت آشکار در این مجموعه دیده نمی‌شود، اما آمریکا ممکن است به‌زودی «ضربه‌ای سخت» به دهانه ورودی این مجتمع وارد کند.
کوه کلنگ گزلا که در رسانه‌های غربی با نام Pickaxe Mountain شناخته می‌شود، در استان اصفهان و در فاصله حدود یک‌ونیم کیلومتری از تاسیسات غنی‌سازی نطنز قرار دارد. به گفته کارشناسان، این مجموعه به دلیل عمق زیاد و استقرار در دل سنگ‌های سخت گرانیتی، یکی از مقاوم‌ترین تاسیسات زیرزمینی ایران به شمار می‌رود.
برآوردهای فنی نشان می‌دهد سالن‌های زیرزمینی این مجتمع در عمقی بین ۸۰ تا ۱۰۰ متر و در برخی نقاط تا حدود ۶۰۰ متر حفر شده‌اند؛ ویژگی‌ای که آن را حتی از سایت غنی‌سازی فردو نیز عمیق‌تر می‌کند. به همین دلیل، برخی تحلیلگران غربی از این مجموعه به‌عنوان «دژ هسته‌ای» ایران یاد می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77065" target="_blank">📅 16:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77063">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J9_apNyVUrQIcXymTGq5gDh6XX7wH1OMdt1hpn75vtaQi6f8XBK5Y-kTVhl1aoXSrVlrQZNV0KdCf2_ar_H9oB7KE2YSNM9mA21NzKnEGb5ujGupP0BLQmpeJUft74ZbaeQEnLWbLFs6ri0SiCYIgubPE9Gsxxx2uR7fBGWM4RQUZe0WsvdxFGjJPXw20l6VI2k9AR3Gws5SfWHx595FHOK9YEOF53gmTC1SL9M_jPv10UYFat4xUwxNTwoTXRG0MtqtwWegKUp02GS3HoC6Td57AhMrKkylMvK8tQBAK6e9EJQI7jrs0Dge92CDVlo4ntt5Tcu-Y7SkolTgMI3s1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NolYo7kYqdMwGvtKD_nBaYwzBhQYWIbn4LDefVdJtlUnzkJ-XiK4f_WC51DMOirB5rYB8GX47vTU35mNL9f2vv_rrXBJpvVJHME9oDVNRP9_xT4eKmpLmuF1VeFYZoOEf0rwaDzdu9ZzT1z_ndYUOnfyRKT9v-9mYO69zysR89LWLUMVJ6NMHiSpTnKGzBrJEuLh0CJO5Me-7Ft3NWlvq0y5r8Rz3oYG25CB_PbmGH7FW-SzdqZh3DlOuWv6TLL1mJnHTHbc5PNXIjPx-n0D9A1WQ6v9fBZOhSxDwXsmFTWnzV1SQZQ97AT0rBVtphgNTeI0bkZOTU1YvUEw9mlG5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت نفت در بازارهای جهانی روز سه‌شنبه ۲۳ تیرماه و همزمان با تشدید درگیری‌ها میان جمهوری اسلامی ایران و ایالات متحده آمریکا در تنگه هرمز از ۸۵ دلار گذشت.
@
VahidOOnLine
قیمت ارزهای خارجی در ایران در روز سه‌شنبه ۲۳ تیرماه افزایش قابل توجهی پیدا کرد و نرخ برابری دلار آمریکا به ۱۸۴ هزار تومان رسید.
قیمت سایر ارزهای خارجی هم افزایش یافتند و قیمت یورو به حدود ۲۱۰ هزار تومان رسید.
در کنار ارزهای خارجی، قیمت سکه طلا هم به ۱۸۰ میلیون تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77063" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77061">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pe0cBxsPUMTBTzUua0eAJFSnE-yuHc7z70JcU-NNhI50LthZhLBQMON4fFH4fS1P2r2qVpTEc8uCmGv9gTS21r77cLHsfbOQwtToi3gBjc10omSH7Yo6x5wM67EplpgNLRhqVGSGZR6ghWCoDDxRL_lSeulEnse2R_mcZgL5ypWMhd9n7uGYUsRKhqV7B0g1opKsPsABi42HXDE-G0ELRSd8O-fwFXSZzgx-NgAhcP8TmDW96ceQHs-tcwQOrGHGEnn9n95oR7DjgU7eSEsOurrAKEiT5EFG1T3TRQ6sB1N4TfpRepEN7plHnsL4I5hxgnyhJ_l-f5faY5Hu2QoURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X-Ny5OpbjReo7Rj2aLpsjAY3tZLTagp0dT3Os_vel0iIZls7pF941Mx-qp7D5jHAOCWrdtauHgepyJngOgBUN2_EndhlDdSH7GEgjOiK833A_z1YbI9nU_PtCbpmP3YtggGQ6881vhB7x4mkdqOrdBBoJR3qheyeqNCLEuswwb5LTE7CI0B05VWyOVUnP4mswDtfnHye-IANzgyPm9cEu9MYd588Bu6F0i8m3xW9EgXm-hOymD19V5yHmg21PLQXxFL0Lwk_c0RMj0-IH2mr4ljdGPKwsOxUP65U3CXQrIoo8PtDPgk3BSndhKcGpItHSVJpqyLFPwxOerYanN3Oow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز در گزارشی اختصاصی که روز ۲۲ تیر ۱۴۰۵ منتشر کرد، از تلاش چندساله سرویس اطلاعاتی اسراییل برای جذب محمود احمدی‌نژاد، رییس‌جمهور پیشین ایران، به‌عنوان یک عامل اطلاعاتی خبر داد؛ طرحی که هدف نهایی آن، به گفته این روزنامه، نصب او در…</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77061" target="_blank">📅 16:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77060">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXwiD8Osspi3qQ00sZ53qm5dYBcOEkDa_VvbpTByHDeschFESIYhTTSl-znXBCRjXFn-CZAex1ifkncWbfkUkP1RkZeS64_SODKtLVep0Tfi_-SFYBP7RrIf4XSJyF3FuG8yr9rLVwUwfVoVTO3_FYi39q6OLgj13WRsfjtc8ioM5lPt0QS3wauQSJe7EMu390qdct-VW-iKLM3dxS8LQYykIB07at9_VTivPSue-g8xmxJAtNYaLILqbpqTNGrouuGg-EftsFFUUs0ld2fnCgajRBa6MZXSgDRltLuDJvwFSKuQuY00Tq37aBCRbtA2IV3PH45SwwfboGs5AK6iNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگاه قضایی جمهوری اسلامی صبح سه‌شنبه ۲۳ تیر از اعدام دو نفر به اتهام «بغی و قیام مسلحانه علیه نظام جمهوری اسلامی»، خبر داد و و آن‌ها را که آن‌ها را از اعضای گروه داعش معرفی کرد.
قوه قضاییه نام این دو را محی‌الدین عبداللهی و حسین پالانی اعلام کرده و می‌گوید آن‌ها اعضای یک «هستهٔ وابسته به داعش» بوده‌اند که در ارتفاعات بمو در نوار مرزی ایران و عراق و پس از یک درگیری که به کشته شدن سه عضو سپاه نیز انجامید، بازداشت و محاکمه شدند.
جزئیاتی از روند این محاکمه منتشر نشده و شرایط برگزاری دادگاه و دسترسی آن‌ها به وکیل و دادرسی عادلانه نیز مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77060" target="_blank">📅 16:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77059">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddf664d6f9.mp4?token=XEPOeMhwkxLW-Net0E27b-f_C4HQemwunZBiw6ih2kpDGn25xawFbtRPcNunTq8XHSalIJbnFN4riboeADQtOMN0_3bwV8B2G6yi2pE0AvcwpvPTcmI3x4VWXrQOg2r1b37VBdr7JrHjf6pXHGshp3dXu1dLjkcOzzUfg7e8boiYnwhGUBUFw3tb7H_nwa8fvAvzljdxwYAI663ZxXil5JiVTSxtB45SENP2aVKDynGAY_wZI_pVvswk17sSjNbP6ubztVfPBm2pJLa0qX9I2CTvDtOykIazF4UI4KINkFOpsQHXx8kybrb03VQAwNjMHjJpY9iBra9qznR05sfl9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddf664d6f9.mp4?token=XEPOeMhwkxLW-Net0E27b-f_C4HQemwunZBiw6ih2kpDGn25xawFbtRPcNunTq8XHSalIJbnFN4riboeADQtOMN0_3bwV8B2G6yi2pE0AvcwpvPTcmI3x4VWXrQOg2r1b37VBdr7JrHjf6pXHGshp3dXu1dLjkcOzzUfg7e8boiYnwhGUBUFw3tb7H_nwa8fvAvzljdxwYAI663ZxXil5JiVTSxtB45SENP2aVKDynGAY_wZI_pVvswk17sSjNbP6ubztVfPBm2pJLa0qX9I2CTvDtOykIazF4UI4KINkFOpsQHXx8kybrb03VQAwNjMHjJpY9iBra9qznR05sfl9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتشر شده در منابع حکومتی:
'حمله هوایی آمریکا به ساختمان سازمان تنظیم مقررات و ارتباطات رادیویی در بندرعباس'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77059" target="_blank">📅 16:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77058">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fuWblmLq7PBOLjyTXdfbMZ0q-v4VkxmmxEPKfxufvV_akWauWkjNSiZY9TA6iqEXIjoISribfsvTQRoThEJu17DXb8TtofdmqDqrTI__B_tPG5hP6Z3D6CTKc_YLXsogewpElDHOdoCo2jeW3ZgXuaaQBQX_kcqOwAdX4jnYXnagofZuZbv0IhQLe_7eYshI3SYvfzKtWyU-gUEpDVz3dXT952BEEY1Dp5pWpBue8qmet7gULvnaZW-wtbqtip3RfK4Jdmd9Lj2eQlMHvdJId4or49-gPBPujH3H4TWglOKwge_u5W4z64L0RXwbPDRU0dugDOumdCbSAGVfeTY8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'مرکز آماد و پشتیبانی دریابانی نیروی انتظامی بوشهر محله بهمنی، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77058" target="_blank">📅 15:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77054">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J__6rJfbSK3tsebTDhGr8zwQ1nCMtQxMlB66C2euxZ1NN4QIFxDNaUK4MdhTdQRccwdnMKS3E0iLw7I2TvPXYE3F65Q_lWdbrx3rrw7A6g4H150IRe5CbrTdkRMv-w-MhTqnkAewESbXr94zqkkuYkjGQUM2rEKebQxlFAboqNXD7kpVxwpUTuPl8N_mbOUS7ZRTy8GYlNBfX5QAeu2mo8IGfKrs_0JvKiVzmA7u7s2WG8x463xTx-7F3PJ3orfP6R1VvreY-w__OjEd4-JjaFn8TnEgU4DIW8KuGJKl014mWIQNZll2hhatuRxP09-UJxl_ssuHA_8QaF3kW-_7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31d98f9c91.mp4?token=HKaNFf5i1bzTkSWheLKm_hBQDUorLCoKSax7banS7rNtY05RdQsbSpfFVdRr5D4COOYUPS07unz04N0cQqWfRvET1dABkPPrEtJPODNfuyom_72JgOoHrA7dg88xzldDtF4Tmel0WmJALQMsrSrxaX_ubQD98EjVGWY8cvgo5VdzGhI0lUqO4D8jI9V0Ili_PTeiQ-0iwSjnLW6pEkU3cilMiVljZ97WQKN6nQVVYRI7RlfHJan16BL5Ylj8zmMt2NduAiNerLqQIdUFdRpIgD_wJxWlbUSMeyVcjpZHruUm4VCd1o0FCf2SY-OlgrLVM8IVtO1DiyJvYWcEjc48gw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31d98f9c91.mp4?token=HKaNFf5i1bzTkSWheLKm_hBQDUorLCoKSax7banS7rNtY05RdQsbSpfFVdRr5D4COOYUPS07unz04N0cQqWfRvET1dABkPPrEtJPODNfuyom_72JgOoHrA7dg88xzldDtF4Tmel0WmJALQMsrSrxaX_ubQD98EjVGWY8cvgo5VdzGhI0lUqO4D8jI9V0Ili_PTeiQ-0iwSjnLW6pEkU3cilMiVljZ97WQKN6nQVVYRI7RlfHJan16BL5Ylj8zmMt2NduAiNerLqQIdUFdRpIgD_wJxWlbUSMeyVcjpZHruUm4VCd1o0FCf2SY-OlgrLVM8IVtO1DiyJvYWcEjc48gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا برگزارش شهروندان از حدود ساعت ۱۲:۴۵ بار دیگر به نقاطی در
#بوشهر
حمله شده و بیش از ۱۰ انفجار رخ داده.
تصاویر دریافتی، سه‌شنبه ۲۳ تیر
#Iran
Vahid
از بوشهر پیام میدم
ساعت ۱۲ و ۴۴ دقیقه صدای انفجار امد اما کم بود
سلام وحید جان
ساعت 12:45 دوباره بوشهر رو زدن
بوشهر ساعت ۱۲:۴۵ ظهر منطقه بهمنی صدای انفجار خیلی نزدیک بود. خونه لرزید
همین الان ساعت ۱۲.۴۲ بوشهر منطقه بهمنی رو زدند(احتمالا پایگاه هوایی ارتش یا پایگاه دریایی سپاه ریشهر) زدند. صدای دو بمب شنیده شد.
سلام بوشهر ۱۲:۴۷ شدیددد صدای انفجار میاد.
درود وحید جان ،بوشهر الان دوتا محکم زدن
الان بوشهر و زد ۱۲:۴۴
به نسبت اخیر صداش نزدیک بود پس میشه حدس زد فرودگاه بوده دوباره زد ۱۲:۴۷
الان زد باز ۶/۷ تا انفجار بزرگگگ کارخانه جاته چون خیلی نزدیکه ۱۲:۵۴
۱۲:۴۷ بوشهر حدود ۴، ۵ صدای انفجار اومد. نسبتا شدید بود.
۱۲:۵۳ دوباره دارن میزنن.  حدود ۷، ۸ تایی زدن الان.
سلام   بازم بوشهر داره صدا میاد از ۱۲و ۵۲ دقیقه چندین صدای انفجار اومده
ساعت ۱۲:۵۳ دقیقه حداقل ۱۰ تا موشک به بوشهر زدن
از ۱۲:۴۰ دقیقه نزدیک به هفت هشت بار دارن میزنن بوشهر رو. خونه می‌لرزه!
وحید جان بوشهر رو ده دقیقه یک ربعه دارن همینجوری رگباری میزنن…
خیلی میزدن انفجارا همش دنباله دار بود مشخص نیست چنتا بود
حدود ۱۰-۲۰ ثانیه یه کوب صدا انفجار قطع نمیشد
وحید جان  رگباری باز بوشهر منطقه ریشهر رو زدن وحشتناک بود
ساعت ۱۲۵۸ دقیقه اسکله والفجر بوشهر را با ۸،بمب زدن، انفجار شدید
سلام ساعت ۱ ظهر صدای انفجار مداوم بوشهر
از ساعت 12:30 تا 13:15
بیش از 15 بار صدای انفجار مهیب توی بوشهر شنیده شده و موج خیلی زیادی داشته
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77054" target="_blank">📅 15:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77053">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام‌های دریافتی:
باز بوشهر رو زد
سلام دوباره بوشهر رو زدن
دوبار بوشهر زدن ۶و ۷دقیقه
حدود ۶:۰۷ باز بوشهر رو زدن.
بازم زدن ولی صداش به مراتب ضعیف تر بود.
🔄
سلام وحید الان ساعت ۶.۱۳ دقیقه باز کنارک زد خیلی بد زد
چابهار ۶:۱۴ زدن
بازم چابهار همین الان ۴ تا شدید زد گفتن تموم شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77053" target="_blank">📅 06:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77052">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd0e2facea.mp4?token=keuWV3uPiKm4h3HMIEH2EY87Hd07v23yR2IpTADlnWH61aQBND_MDl6slqxhoD1e2d81jvkHbVciI899j-79_BnRA29dc81YyhjjEx68r5NzFZkTXVfce22D4oBS3aciUi6PJQ67_FXU0qyB6_pWMDTa69v02yLHTEzw_Ol7S9UCOYwno6z5KS9yOyPrdIb-DmtrefSU1cb7qp1YBOf5jl6Z-AcgMzEqsUZFxFDDOeo7ZPiJWvIwtMvM_RT6eFEp1tl8HB3bZadR3ijCF2rTJwM0pjCbAUCZ5s3eZ6AAWd6WmqaSfI5SY9MQyAlWE7XRYMDzt4cX2X8P9iSwAtClzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd0e2facea.mp4?token=keuWV3uPiKm4h3HMIEH2EY87Hd07v23yR2IpTADlnWH61aQBND_MDl6slqxhoD1e2d81jvkHbVciI899j-79_BnRA29dc81YyhjjEx68r5NzFZkTXVfce22D4oBS3aciUi6PJQ67_FXU0qyB6_pWMDTa69v02yLHTEzw_Ol7S9UCOYwno6z5KS9yOyPrdIb-DmtrefSU1cb7qp1YBOf5jl6Z-AcgMzEqsUZFxFDDOeo7ZPiJWvIwtMvM_RT6eFEp1tl8HB3bZadR3ijCF2rTJwM0pjCbAUCZ5s3eZ6AAWd6WmqaSfI5SY9MQyAlWE7XRYMDzt4cX2X8P9iSwAtClzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا نوشت: نیروهای ایالات متحده حملات جدید علیه اهداف نظامی ایران را به پایان رساندند
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) تازه‌ترین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب به وقت شرق آمریکا در ۱۳ ژوئیه به پایان رساند.
در جریان این مأموریت پنج‌ساعته، نیروهای ایالات متحده با موفقیت اهداف نظامی در نقاط مختلف ایران،
از جمله بوشهر، چابهار، جاسک، کنارک،  ابوموسی و بندرعباس
را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری را بیش از پیش تضعیف کنند. نیروهای سنتکام با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران را هدف قرار دادند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند. نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/77052" target="_blank">📅 06:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77051">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aff0de23f3.mp4?token=RmL1grl1mzYfcMt9HbVUV2NbADNmdfnuMcDsztaNZFtbrPFOU-gnSxhmUwUU15sn35i6VR5Iks5x7ij6576v9GusfFXbs6gXvihTjDgj__GBr7vNxgfI4t3W6lRZ-aszr1gc4TFb5K4KkFtlB9DfazCDIYLr3jA12d5zCUdT1-OppdnNAIjpy7GJAnWrKF-IDK7h5NWZKihQFvGWMYcqXP9QExgVs5chCtUs2nsl3AEiU1UxzExRklAhJUOp_ATr0H_7A3iDpZDZYCiVugNQvZOLtTgWlJwE1SvqhNGaRUgnotsqlsLUYQif3_FcHycD1kCtfzv3W96Zb3VEgUKpAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aff0de23f3.mp4?token=RmL1grl1mzYfcMt9HbVUV2NbADNmdfnuMcDsztaNZFtbrPFOU-gnSxhmUwUU15sn35i6VR5Iks5x7ij6576v9GusfFXbs6gXvihTjDgj__GBr7vNxgfI4t3W6lRZ-aszr1gc4TFb5K4KkFtlB9DfazCDIYLr3jA12d5zCUdT1-OppdnNAIjpy7GJAnWrKF-IDK7h5NWZKihQFvGWMYcqXP9QExgVs5chCtUs2nsl3AEiU1UxzExRklAhJUOp_ATr0H_7A3iDpZDZYCiVugNQvZOLtTgWlJwE1SvqhNGaRUgnotsqlsLUYQif3_FcHycD1kCtfzv3W96Zb3VEgUKpAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش: حملات به مقر سپاه پاسداران در سراوان
haalvsh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77051" target="_blank">📅 05:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77050">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
همین الان ساعت ۵:۳۹ صدای انفجار اومد چابهار و خونه لرزید
الان چابهار رو رو زد خیلی سنگین بود هنوز نمی دونم کجا بوده
سلام ساعت ۵.۳۹ دقیقه دو انفجار شدید چابهار
همین الان دوتا دیگه هم زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77050" target="_blank">📅 05:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77049">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پیام‌های دریافتی:
الان بوشهر [رو] زدن
دو بار
باز بوشهر رو زد
پایگاه هوایی بوشهر [رو] زدن سنگین الان ۵.۱۲
باز بوشهر رو زد
وحید سلام  بوشهر [رو] باز زدن 5,11
سلام بوشهررر رو زدننن
ولی الان باید بریم امتحان بدیم توی این شرایط
😐
😐
🔄
ساعت ۵:۳۷ موج دیگری از پیام‌ها رو دریافت کردم که از شنیده شدن صدای حدود ۱۰ انفجار پیاپی در بوشهر خبر دادند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77049" target="_blank">📅 05:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77043">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sV0AtlkIRi4bKNG1LeA3erPL5vGYn3qomskROWwEiIMJSta1sWy6m6oCl9xx5CLbtX0d7WpsIBc8YePHAx3yTpqnipLWWmLsJSn5FRuA05hhHgkCcU3-QrNSQl2J80Ye5bNis3fv2afyGGxpMpw-ADePxcddG9zSfuNVXuo00wYb86JTwEzzkFtfrO-RxNNwAW_UKcHvNBq71-ehNEwCK8vHGFdp6LqEAxu2gAPAkKwMfBnCOeiBgHeGbNviYAoZ9phi_kNFlN5rCYHp0623ENWRovvmJPmMOSmAS7IN07tYOzN0MaomO4DQc4nELdWZBLLi3y-3hyepqfsEfLAsqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCwCZj_vgUG1FHzdDDx5I6XOgsLVJkfkhragt1rW8DNd3Cp0nbODLdcXhzjo2HBHm7xwJdlbWxiTXQ5iwrUXSJtnG-ibh4eSEHpqpUNlCWV4Hdx43KQ9S0nfbwjD7hKdCqeUS5aEDLqOb8GNBszLwQagWy4MiEI4rg6QjLxjTTqi5yH97S9ZeHYk7i0LvdRgl9ImwTmap4b4FephZpBTpZkgk0kcT7XcRimEsGR4ns1Zpk0UjI4g8vjDrPZAf-qm6lwq17DBNYxIsbj_0Qs_y-ZbQHTYqRxUi0LN_cpTvkdlGvcrG7I16tyc5_BHDAb1jPnr8_rgDmck63tgXfeoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnAa5fsdEUeXfdLgvq3x6KcZDkm-V9qJ82f1cHdvTORcyWpL5WsCTho1nYeMH-3R1D42DhUZJfh55__A35om4GXF_P_jCBjqrai27WrgFMCgtnt216HMKBf5FISA_EQ_c6BvoEZUEITB-jkdmAlBQ1M54CIFptWGrlWaq1z6fihn89cGAp7IS6hREIQp8RBmT6_0id8y28RmTlH3VRAsrhO3phnHHUyzZvnA8FpUDKw4dUrDR2TnW4RBgnEDMPH2b7m5sjl8IhYQDY5oOqYzjMSVJpHq489wHc8E9S5E0fgIiyXGycMk_hLQPnOqI7pxtsK9jA-Y2fGeCCa5zwlJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8E1g85biwvgjO-MIX3UDpnbfRgOrXhZmsw8Qg_zRuK5V9-Cddo0nPhWdQEIgQFQ-2AWIeUU5C39wkbaME7io-L5E1zvC26XsiJhPfSXhhqFgl7DwzAUVhYNqeEoi-_DCqCZK3-WHGQzqwtRNK-e5oQFzm8bs6oMwF7B9NwPL6S6KHnhNlGsjikP5W5Y-bq5UBALEiNSMJ4w4VZQ69hU7p02t1dqCNFHpYh31psi4eYqw5rWAlqghloD7o7d6hA9VvGl2M4kgK0wT4ZS_RnSFrdKwxZfVkZwZcqUtDCWK3kTJLSRwe1PPjA6PpXQtPUZU0NhhW2m9k4eKpK8AmfzKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9GUluoEJCal03F39ahE1LDTBhrfjPFTYskeTrnQ0gn5loTVBzuz6Bbn3-HhNg7dz75Txxmmw9zZtFfBWfkfJXuv5_ZDqPqk1End4Vto5zpL_VXekifkpGB00l77ZLic5e5ybTM20KpCBYGTGGZmweegokT5LeADkIq4_CqPb2rcNyeCqU_kgbfgj_jMIViwovRB7Mpd3tB0aquTDmUZkA_nozJPKAm2qq5NISPHg2yLUaO-7yL35AFG_aUZR0dy63vywUans6WqNHy4FLBYcsHLYPfWGKl-KHKnvn9qjlDzj177dZLThKCLSbECr44Tji0X5kZAp561W_apQ0q6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pf6bMMBnzsp6EzZfW6gXqVAoz07lTWWT05cgaK22046eE_U0bkFDealQt0nP1xRqLRz7jLlArRME0qXH70chIMwz4cucI-UUlw-fc5_B4OCX2CO5ipJzG1KYC6McnP_VdCO1bg2_BvjurqS6xljpVZz77C_ZSR9DSMTSZPQXe6-JVaFc9cXSYVQaZFEThBLKujXHYoOxG-N4Pe6xypdYaqZTdhl9qFLJF6ERgO5MZegA4ypVA1kZIlcKfOA9FJOLpECM4o42mBQSd6wNb3O0ydpXFZRI2yvM40xktfdbYuB76Q9ij2YLY_sytZXi3kdK59qSfItbTOwdt8FkTHwORw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجلس [شورای اسلامی] پس از ماه‌ها تعطیلی، شب ۲۲ تیر اولین جلسه علنی خود را برگزار کرد.
به گزارش خبرگزاری خانه ملت (خبرگزاری مجلس [شورای اسلامی])، بیش از ۲۵۰ نماینده مجلس با حضور در ساختمان بهارستان جلسه خود را به ریاست حمیدرضا حاجی بابایی، نایب‌ رئیس مجلس، آغاز کردند.
نمایندگان مجلس با شعار دادن خواستار «انتقام از قاتلان» علی خامنه‌ای، رهبر پیشین جمهوری اسلامی ایران، و فرماندهان و شخصیت‌های سیاسی کشته‌شده در جنگ شدند.
در این جلسه مقرر شد که در مواقع اضطرار و شرایط خاص ایران، جلسات مجلس می‌تواند «در فضای مجازی یا خارج از بهارستان» تشکیل شود.
از نکات جالب توجه در جلسه امروز مجلس، نصب عکس مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی و همچنین غیبت محمدباقر قالیباف، رئیس مجلس در صحن علنی مجلس بود.
تشکیل جلسه علنی مجلس پس از ماه‌ها تعطیلی، آن هم در ساعات غیراداری واکنش‌های زیادی را در پی داشت و توجه رسانه‌ها را به خود جلب کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77043" target="_blank">📅 04:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77042">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIolldxMD5L8SkCRXu0Jlfr1HgFGdXo-wGGAGxkNTRXvkDZl_esGYyz-p8gkDdJGDeNM_06PRGoMUGpbHrh_4no8B-AaNXaKkOTsxwTWrC7LPqFSpNdBpIcmRH7c3BE089bmL6UITaSXOUe0P0I3s1bJ9FRimj67Fzd14X5cMRdfyv7g1Kyv7CNtk9NyDvOhRI_CAiIxKFJmNIQQXgPNPZHZCpDP6OB1k_6ij1ahhL1dmE1RbSjm2VbfNKK3OTRsiIJcPE8cnDMXqnTGWu6ZBg_YsMehHCreQOtZvPPl5MGu7adkRRgCmRlYjwlN42DKU4Ub8kDGQwQ8QsniZQ5E4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی و انتظامی استانداری خوزستان گفت: در ساعت ۲:۱۰ بامداد سه‌شنبه، نقاطی از شهرستان امیدیه مورد اصابت پرتابه‌ها قرار گرفت.
به گزارش مهر، ولی‌الله حیاتی گفت: بر اساس ارزیابی‌های اولیه از وضعیت مناطق هدف قرار گرفته، تاکنون چهار نفر در این حادثه دچار مجروحیت شده‌اند که اقدامات امدادی در حال انجام است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77042" target="_blank">📅 04:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77041">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S4M1hpAxl_7Uqdw3u83nCQpzRsFOWsAnG69w2DtIwFzl82xAXqCY1V5h70CdSsXQsJ5onaBTWFzTuLi_eHA9CPLRGDB-3F5Kbk1vo2RKVQXyc-ENcw0QWZ8ER22NM1S9UwL1RRi2f0-rvzHomUrfCPxKlVVlU2kDWt31nEjayA8MM5XbBI0ADfDoXSUsLFVAeKCKUgsoxeSfXQ3mwm9t-QbkGj2xBQWAZCmc66ZS_PePAJ-_56Xb2_ZEwjMuF9osZroCnqiVWR5RV6IbXDK-d68p3z5kbUTiLAGa6TEl9QvzFTR-AkekoDNWUwwXLpci8qFUdeF3XCFerBgPtJ-C-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع امارات متحده عربی اعلام کرد که جمهوری اسلامی ایران به دو نفتکش در نزدیکی سواحل عمان حمله کرده است. به گزارش آسوشیتدپرس، در این حمله یک نفر کشته و هشت نفر دیگر زخمی شده‌اند.
@
VahidHeadline
" اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی"، ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت قهرمان و مومن ایران عزیز؛فرزندان شما در نیروی دریایی سپاه بر عهد خود در حفظ حقوق ملت ایران در تنگه هرمز تمام قد ایستاده‌اند.
ساعاتی پیش ارتش کودککش آمریکا که از شکست های مکرر عبرت نگرفته است، با تحریک شناورها تلاش کرد تعدادی از آنها را از مسیر غیر قانونی عبور دهد. دو فروند سوپر نفت کش متخلف که فریب آمریکا را خوردند و با خاموش کردن سامانه های ناوبری و بی توجهی به اخطارهای مکرر مرکز کنترل امنیت تنگه هرمز کشتی رانی در این مسیر را به مخاطره افکنده و عبور از مسیر مین‌گذاری شده را ترجیح دادند، مورد اصابت واقع شده و از کار افتادند.
نیروی دریایی سپاه به همگان اعلام می کند همکاری با دشمن متجاوز که از هزاران کیلومتر دورتر آمده تا حقوق مردم منطقه را تضییع کند و عبور از مسیر مین‌گذاری شده جز پشیمانی، خسارت و تاخیر در بازگشایی تنگه هرمز و ایجاد بحران انرژی در جهان نتیجه ای ندارد.
و ما النصر اِلا من عندالله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77041" target="_blank">📅 04:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77039">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d09iL4SCK7uu6qDKc8kwmvT6Qa7BPXsIWU9DOMdxiaETB0rvFLu6pgthjkWWsgaJV_R52NNC8OPnfAX-RdBk6hP6wm_OzJblAl5LU4126hxfGPTDYKqSJ7ZJuepvqT6SOGDQVrZkbmC3_5IaMoUrPQBkR8XRNsPa-QBa4wtpFhQpFYGv6An57OtbA2bicFepgtET4b2i7aGbfbkSTEzdqlMy5Z36WfPNbquE7rOYiXtAqhpf4ORtkHbKORI9Y72VCK5VKT93NsxYlya-ka0XYTn6xikl-enFUOsV4PfTc0HKyj3VBbYnHtkuiUpGGZt4Fm7IY5gjCBZWXaFPMEDBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MgZZrh2nb_cgoW-75Xgm03MRGKclVaP7lh3kZkHTydM3tAlE2Nm3EghuhKJZhzJFJKcDZdKsNPAOhLXBdkbBN-mSB86t68fYCLUKC38JlkQ5kZmzGdpEUfuB2Km69WXXVrXDAzXRYX0vDs7uSONu1E8IFZLEbn1lHSjp6pzULIsmaxKPGM2sOjXsjQkgd6tbG8n8vgUXahO4Dk533WWG8mRO4fQ9d_ELbuy4PxN_SYOdbrggjXiDgO5FelCMJxgTJ3Dhk08A9IOw0vLvliCu5yO8qrLBS3ADyfSi5kP9RjvG9pQy-8Lt2oX4aKVzsujC7du6uRSl4bJwvfUFG2OUdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: کرمانشاه ۲ تا موشک شلیک کردن ساعت ۴
آپدیت: ممکنه تصاویر مربوط به پرتاب از تبریز باشند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77039" target="_blank">📅 04:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77038">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان تبریز
از سمت شمال شهر  دوتا پرتابه با نور شدید قرمز به سمت جنوب غربی دیده شد
سلام وحید جان، تبریز صدای جنگتده میاد [احتمالا صدای شلیک موشکه]
سلام اقا وخید همین الان صدای دوتا انفجار کرمانشاه
سلام
صدای دو انفجار در کرمانشاه
ساعت ۴ و دو دقیقه
ساعت ۴:۲ نردیکی هرسین تو استان کرمانشاه صدای ۲ انفجار سنگین اومد
سلام ساعت ۴:۰۳ کرمانشاه دوبار صدا اومد احتمالا شلیک موشک.
سلام وحید کرمانشاه شهرستان هرسین دوتا صدای وحشتناک مهیب
سلام کرمانشاه ساعت ۴:۰۲ دقیقه صدای انفجار از سمت تنگه کنشت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77038" target="_blank">📅 04:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77037">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e3d542753.mp4?token=aWvk3m0e2dEFwEdchA532V6CNaajLlPMQG8UiyPzoHAvie3DJ01I31ayTTYiGU9rUgukDbeH8ACHnp-4YZwDdqVZyfKzAy_Mhy76vUouhjc9l9GgCPLnoeEHp3hpINTriU2Y9Dc60x9t6E8cOMIWcSIylyFL0-bLIIQX3yL9V5vBYVIvLnLV3sZeuWS4YX9gaUOc4xjZZTfFW4sDQLy16nufvIbolDn7dc8UD9bMG7_8LdVkeWOEGEsdgftMBQ7z_z1q652PeTQd9MzB2L9ni-MXu5uo01fumzEByVR_boPSU3i4dT3wxm2cSN782LEGC40yzcOu9-wD_nIW5Ikfhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e3d542753.mp4?token=aWvk3m0e2dEFwEdchA532V6CNaajLlPMQG8UiyPzoHAvie3DJ01I31ayTTYiGU9rUgukDbeH8ACHnp-4YZwDdqVZyfKzAy_Mhy76vUouhjc9l9GgCPLnoeEHp3hpINTriU2Y9Dc60x9t6E8cOMIWcSIylyFL0-bLIIQX3yL9V5vBYVIvLnLV3sZeuWS4YX9gaUOc4xjZZTfFW4sDQLy16nufvIbolDn7dc8UD9bMG7_8LdVkeWOEGEsdgftMBQ7z_z1q652PeTQd9MzB2L9ni-MXu5uo01fumzEByVR_boPSU3i4dT3wxm2cSN782LEGC40yzcOu9-wD_nIW5Ikfhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منتشرشده با شرح: سراوان سه‌شنبه ۲۳ تیر
پیام دریافتی: اینجاست
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77037" target="_blank">📅 03:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77036">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hdpnxJxYh0FPl23tWn2d2BSutq3U1-EMrHZGHVuRgl59Xvw1ByYLLDTX1P53MbeYAZSlJC7VBeK52KaQaP_FLIE79D2nUIUOihXLxqBv4tA1rpXRwjgbAnGgDA1J_hfxCMVgIRE7sCDE9krMHXClPPqBLDJ4KXCpdmYaw-gx-fenxMaGO55MfBiJ_Zb5dpNAHoDcZAip0wAyP5qyQe9lBSZabRaZtcOWBjVIIR2ALpaEcBBZthsZg5N6Iaw1bcnmUh1zObLAdqHIQjyAZ4GdtCeTod5rr-jz3pz698Qfv3f7-eW6Fcc2i3wlvXa3j5iykvruM6yHTgGMKyeWKs-Jaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۳:۳۰ بوشهر دوتا انفجار خیلی شدید صدا توی بهمنی اومد
بوشهر 3:28 مجدد صدای انفجار
بهمنی زدن 2 بار سنگین بود ساعت 3 نیم دوباره زدن
وحید جان دوباره صدای انفجار اومد بوشهر ۳:۲۹
سلام همین الان بوشهر رو دو تا پشت سر هم زدن فکرکنم انبار مهمات یا همچین چیزی بود
دوتا انفجار مهیب پشت سر هم شهر بوشهر ساعت ۰۳:۲۹
سلام دوباره زدن با صدای انفجار بدتر
بوشهر تا الان ۴بار زدن
چهار تا صدای ترکیدن دیگه ۳:۲۹
پایگاه هوایی بوشهر ۳.۲۸ سه انفجار
سلام وحید بوشهر همین الان سه تا انفجار خیلی شدید پشت سر هم
بوشهر رو زدن ۳:۲۸ نزدیک به اسکله جلالی گمونم، پایگاه هوایی
سه تا تا حالا
الان بوشهر صدای بلند انفجار ۳:۳۰
3 تا انفجار سنگین
بوشهر ساعت ۰۳:۲۹ صدای انفجارهای خیلی شدید و نزدیک میاد
بوشهر ۳:۲۸ ۳:۳۰ هردو انفجار بلند خونه ها داره میلرزه سمت بهمنی
بوشهر صدای ۳ انفجار همین الان بهمنی
بوشهر همین الان ۳:۲۸ تا ۳:۳۰ ۵تا انفجار شدید ! خونه میلرزه
سه تا دیگه زدن
تو پایگاه هوایی
سلام دوباره زدن با صدای انفجار بدتر
بوشهر همین الان باز زدن
دو سه دقیقه پیش هم زده بودن
بازم زدن سه تای دیگه
بوشهر رو دارن میزنن
انبار مهمات اینا نیست فرودگاه دارن میزنن
و پایگاه هوایی ششم شکاری
و موشک های تام هاواک هستش ک صداش بلنده
یعنی جنگنده نیست مثل سری های قبل
بوشهر خیلی بد دارن میزنن تو این چند وقته اینجوری نبوده باز خونه هامون لرزید چهارتا پشت سرهم زدن
بوشهر - اولین انفجار پایگاه هوایی بود ۳:۱۳
انفجار های بعدی شامل دو انفجار در همون حوالی
دو انفجار مهیب دیگر در اطراف شهر بوشهر بود. احتمالا چغادک. حوالی ۳:۳۰ تا ۳:۳۲.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77036" target="_blank">📅 03:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77035">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پیام‌های دریافتی:
سربندر همین الان دوتا پشت سر هم
یکی دیگه
همین الان بندر امام خمینی‌ رو زدن سه بار
ماهشهر ساعت ۳:۲۳ صدای ۲ تا انفجار پشت هم
[احتمالا همون انفجارهای پیام‌های بالایی]
سلام ماهشهر تا الان سه بار صدا اومد
وحید جان ماهشهر ۳ تا پتروشیمی سر کارم لرزیدیم
سه انفجار پیاپی در ماهشهر داشتیم
😔
بچه ها صبح امتحان نهایی دارن
😭
سلام ماهشهر زدن 3:24 دقیقه
شیشه اتاقم لرزید
همین الان ساعت ۳:۳۰دقیقه
بندر امام خمینی سایت موشکی رو زدن چهار بار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77035" target="_blank">📅 03:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77034">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر 3:06 صدای انفجار
سلام ساعت ۳:۰۵ بوشهر صدای انفجار
ناحیه بهمنی
سلام وحید جان ساعت ۳:۰۶ بوشهر صدای انفجار اومد
الان بوشهر و زدن ما پایگاه هوایی هستیم خیلی بد بود
ساعت ۰۳:۰۶ دقیقا انفجار مهیب شهر بوشهر
سلام . همین الان بوشهر رو زدن . صدا خیلی مهیب بود
سلام وحید جان ساعت 3:05 دقیقه بوشهر رو زدن پایگاه هوایی بود فکر کنم
بوشهر زد ساعت ۳:۰۵دیق شب
همین الان وحید جان زدن بوشهر رو ، لرزش و صدا خیلی خیلی بیشتر از روزای قبل
ترس و لرز وجودم فرا گرفت برعکس شبای قبل
واقعا ترسناک بود این یکی
سلام
پایگاه هوایی رو زدن الان
صداش وحشتناک بود
تمام بدنم داره میلدزهه
همین الان بوشهر نزدیک فرودگاه صدای انفجار بسیار مهیب
سلام بوشهر بهمنی زدن ساعت 3:06
سید جان ۳:۰۶ بوشهر صدای انفجار (فکر کنم پایگاه نیرو دریایی بود)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/77034" target="_blank">📅 03:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77033">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1b221ac38b.mp4?token=mQWdDfbyauFm9n4753MS5lLeSnwe1fPrAFBe9CY_2r8W6QWqa6Ldc6uRQNDktFdHD1y25QTxLjnxUfSyg8tYrbS1gzAhF28F3j1VYseCzPiFW3UE-lHRoBvaFAHU3MPkFGZDjVMc-ksywKeyxODBG65Q0Um5MN7plourxVcrZZWlw8UY9rU_MFF9iFu4eyOuiZ-11anyYz_h_yvVzPIojQi7yjXwEr9LULTaC7ggWC5XfJZVBk1ftcibYGoYgFSPxRw1HSAYz4Vf4bYGbnwt4bDsbUqO-rL2XsDFJE9brQr6YxwcV87o-46iTB-z946DGM-2FKqpcQeIMk3oHnhZgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1b221ac38b.mp4?token=mQWdDfbyauFm9n4753MS5lLeSnwe1fPrAFBe9CY_2r8W6QWqa6Ldc6uRQNDktFdHD1y25QTxLjnxUfSyg8tYrbS1gzAhF28F3j1VYseCzPiFW3UE-lHRoBvaFAHU3MPkFGZDjVMc-ksywKeyxODBG65Q0Um5MN7plourxVcrZZWlw8UY9rU_MFF9iFu4eyOuiZ-11anyYz_h_yvVzPIojQi7yjXwEr9LULTaC7ggWC5XfJZVBk1ftcibYGoYgFSPxRw1HSAYz4Vf4bYGbnwt4bDsbUqO-rL2XsDFJE9brQr6YxwcV87o-46iTB-z946DGM-2FKqpcQeIMk3oHnhZgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح:
#سراوان
ساعت ۲:۳۰ دقیقه [سمت] فرودگاه رو زدند.
سه‌شنبه ۲۳ تیر
Vahid
پیام‌های دریافتی دیگر:
پیام ساعت ۲:۳۵: سراوان رو ۴ بار زدند
سلام سراوان سیستان بلوچستان ۵ تا انفجار پشت سرهم
پیام ساعت ۲:۴۱: سلام، سراوان بلوچستان رو زدن، ۳ تا صدای انفجار اومد خونه‌ها بد لرزید، حدود ۲۰ دقیقه پیش.
همین الان سراوان سیستان و بلوچستان رو زدن
سلام ساعت 2:20 سپاه شهرستان سراوان سیستان و بلوچستان رو زدن
4 تا انفجار بود با صدای خیلی وحشتناک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77033" target="_blank">📅 02:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77032">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30da9372f8.mp4?token=msaX4A3E1jpqdm5KmcRgwqzaP2diDHlJxx38OWAWw7dmA9aHyKcbwUHY9dOmQug3RDuG3LUKk7H9xu4vc5vKKZ2zMRLXyUM4ckmOn6lzUI3IOSCFj12wIjkHorSkMVbfTGhyiu2hR1orNXZep0DWwutLrJy6yHmg0yN_kVy9Nt21HrEGRwx5FU44aoib_pIUBfiRvs2YijsOckYdgzhj2ewFjAakKq4QcDz0Pm0kaoCguEwqyr4Ca8zakQCXmqetg2s9ifZap_MZLPVO2wO50jhUNvRuYxBIsRrNzR1Fij6EuRJ3SrVvIJTLHu-0Eew1K7uQEsJMoO4Cxrnbug4-yTpu9xDHpp2qJQlMEAsnmZN9XztMkamtCHRdOINoQx0viP484Yugk-rndfUp8eO2kvbGRctyTMdxLf_ShWmJm5HmIcJ-6dwUOBZm-yjU-4W0UGCBSRirM9X-LwpFKQxF-t31FNOczrxLQKt0Ogmmwfb_moAO7giF7osPsJqm1DtoOpSLxiN24F0ny_I7GeqWEIWX1AMz0-zBs6XZDqb4d3BlxLbYhUoqsNEG_y1MxZGNXWGr1K1Z6GfHw464Y7E7HqafAB70iOPhqH4_JJT5cQbaMllgTFLUrMwpMLYo1Ks3dQ4BodntzfZZdg13U8tUtGtV59fikJTZ5DY0SlF8ZgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30da9372f8.mp4?token=msaX4A3E1jpqdm5KmcRgwqzaP2diDHlJxx38OWAWw7dmA9aHyKcbwUHY9dOmQug3RDuG3LUKk7H9xu4vc5vKKZ2zMRLXyUM4ckmOn6lzUI3IOSCFj12wIjkHorSkMVbfTGhyiu2hR1orNXZep0DWwutLrJy6yHmg0yN_kVy9Nt21HrEGRwx5FU44aoib_pIUBfiRvs2YijsOckYdgzhj2ewFjAakKq4QcDz0Pm0kaoCguEwqyr4Ca8zakQCXmqetg2s9ifZap_MZLPVO2wO50jhUNvRuYxBIsRrNzR1Fij6EuRJ3SrVvIJTLHu-0Eew1K7uQEsJMoO4Cxrnbug4-yTpu9xDHpp2qJQlMEAsnmZN9XztMkamtCHRdOINoQx0viP484Yugk-rndfUp8eO2kvbGRctyTMdxLf_ShWmJm5HmIcJ-6dwUOBZm-yjU-4W0UGCBSRirM9X-LwpFKQxF-t31FNOczrxLQKt0Ogmmwfb_moAO7giF7osPsJqm1DtoOpSLxiN24F0ny_I7GeqWEIWX1AMz0-zBs6XZDqb4d3BlxLbYhUoqsNEG_y1MxZGNXWGr1K1Z6GfHw464Y7E7HqafAB70iOPhqH4_JJT5cQbaMllgTFLUrMwpMLYo1Ks3dQ4BodntzfZZdg13U8tUtGtV59fikJTZ5DY0SlF8ZgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان تامی بروس، معاون سفیر ایالات متحده در سازمان ملل در جلسه اضطراری شورای امنیت، ترجمه ماشین:
بار دیگر، این شورا برای برگزاری نشستی اضطراری فراخوانده شده است تا درباره تلاش‌های حکومت ایران برای تهدید همسایگانش در خلیج [فارس] و تضعیف تلاش‌ها برای برقراری صلح در منطقه گفت‌وگو کند.
در ۳ ژوئیه، یک پرواز ایرانی از تهران وارد صنعا، در قلمرو تحت کنترل حوثی‌ها، شد. هدف این پرواز، انتقال نیروهای سپاه پاسداران، از جمله کارشناسان پهپادی و موشکی، برای حمایت از تروریسم حوثی‌ها بود؛ آن هم با پوشش انتقال مقام‌های حوثی به مراسم خاک‌سپاری رهبر جمهوری اسلامی.
این نوع حمایت، حوثی‌ها را قادر می‌سازد مردم یمن را به وحشت بیندازند و آزادی کشتیرانی را در دریای سرخ و آبراه‌های پیرامون آن تهدید کنند. از زمانی که پروازهای ماهان‌ایر به صنعا در سال ۲۰۱۵ متوقف شد، شاهد تلاش ایران برای ارائه چنین حمایت آشکار و گستاخانه‌ای از حوثی‌ها نبوده‌ایم. در واقع، رهبران حوثی آشکارا از این پرواز اخیر به‌عنوان دورزدن موفقیت‌آمیز تلاش‌های بین‌المللی برای منزوی‌کردن این گروه تروریستی تجلیل کردند.
این اقدامات نقض قطعنامه ۲۲۱۶ شورای امنیت به‌شمار می‌رود. ...
افزون بر این، صبح امروز دومین پرواز ایرانی با وجود دستور صریح و علنی دولت جمهوری یمن مبنی بر خودداری از این اقدام، وارد یمن شد. بی‌اعتنایی عامدانه جمهوری اسلامی ایران به حاکمیت یمن و تصمیم‌های جمعی این شورا، به‌سادگی غیرقابل‌قبول است.
به همین ترتیب، بی‌اعتنایی آشکار ایران به قطعنامه ۲۸۱۷ شورای امنیت را نیز دیده‌ایم. ....
هفته گذشته، ایران پهپادها و موشک‌هایی را به سوی سه کشتی تجاری غیرنظامی که در حال عبور از آب‌های سرزمینی عمان بودند، شلیک کرد؛ اقدامی مغایر با حقوق بین‌الملل. این حملات می‌توانستند دریانوردان را زخمی یا کشته و خسارات زیست‌محیطی قابل‌توجهی ایجاد کنند. یکی از کشتی‌ها، یک نفتکش قطری حامل گاز طبیعی مایع، در حال سوختن رها شد و تردد دیگر کشتی‌ها در تنگه را نیز بیشتر به خطر انداخت.
سپس عصر شنبه، ایران یک کشتی کانتینری در مسیر امارات متحده عربی را هدف قرار داد. یک تبعه هند همچنان مفقود است. این حملات از هیچ اصل مشروعی سرچشمه نمی‌گیرند. بلکه همان‌گونه که یکی از مشاوران رهبر جمهوری اسلامی روز یکشنبه گفت، این اقدامات از تمایل ایران برای تصاحب غیرقانونی یک آبراه حیاتی و استفاده از آن به‌عنوان ابزار بازدارندگی راهبردی ناشی می‌شود.
فراتر از عرصه دریایی، ایران در هفته گذشته پهپادها و موشک‌هایی را به سوی بحرین، اردن، کویت، عمان، قطر و امارات متحده عربی پرتاب کرده است. وزارت کشور قطر گزارش داد که سه نفر، از جمله یک کودک، بر اثر سقوط بقایای عملیات رهگیری پس از حملات روز یکشنبه ایران زخمی شدند.
...
در چند هفته‌ای که از امضای این تفاهم‌نامه گذشته، ایران بارها این توافق را نقض کرده است. تا زمانی که ایران به تهدید عبور امنی که این تفاهم‌نامه از آن حفاظت می‌کند ادامه دهد، ایالات متحده آن را به‌طور یک‌جانبه اجرا نخواهد کرد.
به زبان ساده، اگر ایران به سوی کشتی‌ها شلیک کند، ما فوراً با نیروی نظامی پاسخ خواهیم داد. عملیات نظامی ایالات متحده پاسخی به این تهدیدها در چارچوب دفاع از خود و دفاع از دیگران است.
...
ایالات متحده در کنار شرکای خود در خلیج [فارس] ایستاده و همراه دولت جمهوری یمن، در برابر تهدید تروریستی حوثی‌های مورد حمایت ایران خواهد ایستاد. ما همچنان متعهدیم با اعضای شورا همکاری کنیم و از همه ابزارهای موجود، از جمله تحریم‌ها، برای حمایت از راه‌حلی مسالمت‌آمیز برای درگیری یمن و حفاظت از صلح و امنیت بین‌المللی استفاده کنیم.
و در پایان، بار دیگر از شورا می‌خواهیم با صراحت و بدون هیچ ابهامی به ایران اعلام کند که این اقدامات آشکار، مغایر با حقوق بین‌الملل و غیرقابل‌قبول‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77032" target="_blank">📅 02:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77031">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c6082c82eb.mp4?token=FMgCVKn_bPRhl8ESO0HmA6X3XtlzxQQqMr2HWmOAtAPjz8_GOlpRi8Qx6u_o-YnlmPqzTytAUnjS4kDz4Phj2kVjXYGYKfFy-sAMW7rwqKuw6nt2Oe5xMvJ-3emfvXEhrSYw2aFR9Gvn66OkUGMt1OeghDly_X4hDS4flQcHEX05QrocopnAU_EWSKd-mp7cqsLub1MeLqOsM5sjZlbtmZogMIkGK8FEmvGLLkPup-aIk5JqjiaOnafrDIJODpfbtSkkDB6_Coen7klydxtwEToz1cSNzBB1PhFeIR_mPp8PoESQv3kBccgK6x_Ua-FkJpqW1oa6fkwzT-fSThMRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c6082c82eb.mp4?token=FMgCVKn_bPRhl8ESO0HmA6X3XtlzxQQqMr2HWmOAtAPjz8_GOlpRi8Qx6u_o-YnlmPqzTytAUnjS4kDz4Phj2kVjXYGYKfFy-sAMW7rwqKuw6nt2Oe5xMvJ-3emfvXEhrSYw2aFR9Gvn66OkUGMt1OeghDly_X4hDS4flQcHEX05QrocopnAU_EWSKd-mp7cqsLub1MeLqOsM5sjZlbtmZogMIkGK8FEmvGLLkPup-aIk5JqjiaOnafrDIJODpfbtSkkDB6_Coen7klydxtwEToz1cSNzBB1PhFeIR_mPp8PoESQv3kBccgK6x_Ua-FkJpqW1oa6fkwzT-fSThMRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: '
#کیش
، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77031" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77030">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده از حدود نیم‌ساعت پیش:
سلام وحید جان
امیدیه رو ساعت ۲:۹ دقیقه زدن
سلام همین الان امیدیه خوزستان زدن
شهرستان امیدیه خوزستان
صدای شلیک دوتا موشک شنیدیم
بعد هم دو تا انفجار قوی خیلی نزدیک بود فاصلش
تونل موشکی که در روستای نمره یک امیدیه ازش استفاده میکنن همین الان بمب بارون شد و تخریب شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77030" target="_blank">📅 02:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77029">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پیام‌های دریافتی:
حدود ساعت ۱:۳۰ چابهار یه صدای انفجار اومد
سلام وحید جان همین الان ساعت یک و نیم صدای پنح انفجار در چابهار شنیده شد
سلام وحيد جان ، چابهار صدای انفجار اومد 1:34 بامداد
#چابهار
: فقط باید تهرانی باشیم کسی به فکر ما باشه؟
[آپدیت: در واکنش کلی پیام حمایتی از تهران دارند می‌فرستند. زحمت نکشید و ننویسید لطفا.]
صدای انفجار ضعیف کنارک
انگار فاصله زیاد بود
وحید الان چابهار رگباری زدن نزدیک 10.15تا
سلام ساعت ۱:۳۳ چابهارو دارن بد میزنن
کنارک همین الان نزدیک ۱۰ تا زد 1 : 34
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77029" target="_blank">📅 01:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77027">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VKGL3tDo2g5ZiRIaToUgNMj3OqKTiiShapzEHyrOfK2SgZWZEbhyfdevk8rr7ZJrlqW2bpeiykUer4MAahhrDE6Jv1mwH2Y3LANoxSVecKTpIwgQg-lhe0QFvZTZO7vc3bOT8H9I5mjVy3kOysiLzMQ6oa1vwbL52aOk6OI2YqIPy1LkC_rYsLBPpDIOjvYLHke5mSUqb6M7YYbXRMRHqPiebwGbl880tMKdmOXsG4lsYSjENF5sEaq0xbxBIXmE-wyWAMxbcywPyVG7nfesZWHInGxf6kn2G1NR_HZPWVg-b2cuFunwpJnMFLvF48_GfGmWj6gl7BWhvklTTZB36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ExAmPdNZUYZyQAkXfffOZVFnJRMqvUSwxcc2JXMoTDulMkIcMlm4t6qnX4voWijlpX4fE1-eSu1tWkKkziqqZRILhpxbBfuqxWMBydxOpiHXDNFWEwVEySeZL1szyPzkHZfHhkDAs6sp3G1Xr3Ue9ikLxMf-4iIoaL5Kz5GatWY5a6Ipo2D9s4Icgqpck6Cdt75RKKfewIS5RHU9Lclft7I8iFdsHQ3Zg94-tXW14mr42OFt9eIdcHykZGylclbY2ahEVK_OnuRbqx6bJ7t76JEreA3r6v0PhkOu1ES0ZeFPSTSR-3zsCqlqIkl90hP--JkZkpmENPbFuOayc22U0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: '
#کیش
، سه‌شنبه ۲۳ تیر ساعت ۰۰:۳۸'
Vahid
بعدش هم حملات و انفجارهای دیگری بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77027" target="_blank">📅 01:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77026">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام‌های دریافتی:
کیش ساعت ۱:۰۲
۲ انفجار دیگه
صدای انفجار داره میاد تو کیش
کیش دوتا صدای انفجار دیگه
دوباره کیش رو زدن وحید
الان دوباره دوبار کیش زد
کیش رو دوباره زدن
البته صدا دورتر بود ۰۱:۰۳
دوباره زد کیشو
وحید جان این دفه دوتا زد
بندرگاهو داره میزنه
مجددا کیش را زد صداش از قبلی ها خیلی بلندتر بود و شیشه ها لرزید.
🔄
سلام همین الان کیشو دوباره زد این بار هم دوتا بود ساعت ۱:۹
الان سه بار دیگه زد کیش رو
وحید جان دوباره یکی دیگه زد کیشو
و مجدد صدای انفجار در کیش
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77026" target="_blank">📅 01:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77025">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f01979093.mp4?token=XSswE2SNkLeuFEpvHjfjxNBukS8N1l8rOxpZAxfmWrN3vyedqEv_q8IeOAZI1wRYRU-Uz202VVUlpx7rC-qfwj4UDB8siFQZZL_FK1F_8TE3m3R6tuakp9T63_fvxq1XAG3l61KsiCsPK6BTlnMe9GGDTBqLLVyKvTtd5eDsdXCsi2j_6F9oA_0y_-Jp7x2TfelHiMnJtEu6jwpJbTYNAsMvAgV9tkDB91Lzy9o0hK2LeWsfCMDhEer6fmlMatQlzAZddgsXHp0k6bNcWIBJKDg_TfgA5UxgJ_lG4dy60rcwqS0Pa4MiPQO8t5SY1og8MIWogTprzQQVdT_PBbbymw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f01979093.mp4?token=XSswE2SNkLeuFEpvHjfjxNBukS8N1l8rOxpZAxfmWrN3vyedqEv_q8IeOAZI1wRYRU-Uz202VVUlpx7rC-qfwj4UDB8siFQZZL_FK1F_8TE3m3R6tuakp9T63_fvxq1XAG3l61KsiCsPK6BTlnMe9GGDTBqLLVyKvTtd5eDsdXCsi2j_6F9oA_0y_-Jp7x2TfelHiMnJtEu6jwpJbTYNAsMvAgV9tkDB91Lzy9o0hK2LeWsfCMDhEer6fmlMatQlzAZddgsXHp0k6bNcWIBJKDg_TfgA5UxgJ_lG4dy60rcwqS0Pa4MiPQO8t5SY1og8MIWogTprzQQVdT_PBbbymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: انفجارهای
#کنارک
الان، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77025" target="_blank">📅 00:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77024">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UlNIOLUbmmDnXhA1UV_1U4lsoR9nnHsB2lEa8YrzSyp1ZyAZHi_xaK-LXvW8mHfQbHj9Q0naaZ4Wy1hKB-EuaQ1bjgT695K5_4FNRaGwS6kMT7ghkgWiSiK1_Y-D-0nzbggtTCAEvHjQOlOaBeINyP76BOwZFu0jfd8wOIHFkbsPMKy7XpchN9fPogLpyLESPAqVT2RZcdr0GYvlGZ217m1Z07ri8wgwAWaZdMVTB3__1pi86lGTUri3HbW3PqW7bIEgpdFQhZ6XconQscYe_8YL0N1u23Wn3a0XtD3u9IlnYNHdbXsgCdcg1Iq2QzFUZ6BiL_IqVBJjVBK_hTawkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام:
امروز ساعت ۴:۴۵ بعدازظهر به وقت شرق آمریکا [۰۰:۱۵ بامداد سه‌شنبه ایران]، فرماندهی مرکزی ایالات متحده به دستور فرمانده کل قوا، سومین شب پیاپی حملات علیه ایران را آغاز کرد.
این حملات همچنان هزینه سنگینی بر نیروهای ایرانی تحمیل خواهد کرد و توانایی آن‌ها برای حمله به غیرنظامیان بی‌گناه و کشتیرانی تجاری در تنگه هرمز را کاهش خواهد داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77024" target="_blank">📅 00:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77023">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیام‌های دریافتی:
سلام همین الان توی جم صدای ۴تا انفجار اومد
شهرستان جم استان بوشهر
چهارتا تا الان زدن
همین الان جم رو  زدن سه تا انفجار12:40
درود شهرستان جم استان بوشهرو همین الان دوبار زدن
درود وحید جان، جم بوشهر ۴ انفجار پشت سر هم، خیلی شدید بود.
حاجی جم همین الان ۴ تا انفجار شدید ۱۲:۴۰
وحید جان جم بوشهر ۳ ۴ تا صدا اومد
همین الان ۴ تا صدای انفجار مهیب سپاه چمران شهرستان جم
خیلی مهیب
سلام وحید جان همین الان ۴تا صدای انفجار در کنگان شنیده شد ۰۰:۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77023" target="_blank">📅 00:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77022">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام‌های دریافتی:
وحید جان زدن کیشو پنج‌تا پشت هم
کیش رو زد
سلام وحید جان
همین الان کیش صدای دو انفجار اومد
دور بود صداها
سلام وحید جان کیش صدا انفجار پنج تا
همین الان ساعت ۰۰:۳۹ کیش رو زدن
نمی‌دونم بندرگاه بود یا فرودگاه، اما مطمئن که شدم، بهت میگم
سلام آقا وحید کیش رو زد ما نزدیک فرودگاهیم پنجره ها لرزید
جزیره کیش ۴ بار پشت هم زد و صدای جنگنده میاد.
کیش ساعت ۰۰:۳۸
۳ انفجار متوالی
درود
کیش، ۵ صدای انفجار، ۱۲:۴۰
۴.۵بار کیش صدا زیاااد پنجره ها لرزید همه تو بالکن خونه هان .. نمدونیم کجا بود
شاااااید رو آب بود ولی خیلی نزدیک ... هنوز کسی خبر نداده کجا بود..
انفجار در بندرگاه کیش بوده شناور سپاه یا نیروی انتظامی بوده…
بچه‌ها میگن حوضچه بندرگاه کیش رو زدن
شمال جزیره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77022" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77021">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پیام‌های دریافتی:
وحید جان مشهد زلزله اومد
مشهد لرزید
یا زلزله بود ، یا زدن یه جایی را
سلام
مشهد نمیدونم زمین لرزه بود یا چی؛
زمین لرزید!
همین الان ساعت ۰۰:۳۵
زلزله بود گویا مشهد.
وحید جان مشهد لرزید
مشهد زلرله اومد
مشهد لرزید ۰۰:۳۵
دو بار با فاصله ۴۰ ۵۰ ثانیه ای
سلام مشهد ساعت00.35 زلزله یا یه موج لرزه‌ای شدید اومد با فاصله سه ثانیه رفت برگشتی بود
مشهد یک لرزش خفیف حس شد ولی صدایی همراه نداشت.
مشهد چند دقیقه پیش دوبار لرزید
سلام وحید آقا
مشهد یه چند لحظه ای لرزید
فکر کنم زلزله بود
سلام فریمان هم از زلزله مشهد لرزید
من تربت جامم اینجام همون تایم در حد دو سه ثانیه یکم لرزید
فریمانم لرزید(شهرستان60کیلومتری مشهد)
حتی یکی از اعضای خونه از خواب بیدار شد
چند ثانیه طول کشید
سلام وحید جان. ما طرقبه نزدیک مشهد هستیم اینجا هم لرزش رو حس کردیم.
🔄
سلام آقا وحید زمین‌لرزه‌ای با بزرگی ۳.۶ حوالی سفید سنگ در مشهد را لرزاند.
بزرگی زمین‌لرزه ۳ و ۶ دهم بود. مرکز زلزله سفیدسنگ خراسان رضوی بود. بیشتر نزدیک فریمانه تا مشهد
[دو تا پیام هم درباره احساس زمین‌لرزه در یاسوج داشتم.]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77021" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
