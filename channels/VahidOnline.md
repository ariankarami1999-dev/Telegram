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
<img src="https://cdn1.telesco.pe/file/XMImS0FEYKL3bGXE0_98yS4bozDezsuiB_KB8HrJow3tPsti2h3bnfBV5zxGp5TqMiKp0WREaC3VI7nMJmHOAic7qLvqRwBeV8srTF7m2teai-E8AO-rUCzRTGKYHgCTPfC5fXWeDqLGBidE2VoogPIN9_gI0nyj43ti4MQCuoJDHeGiB1TZ7ISVS8WJwNzQ0k9NlgTOATzkW5NBWR33EydWB5aovRMna2MBHnPvgv3bZ2yRQzdAakzBOWuqj9RcUhyy5WXD4ytu5rVqUXBpEeyuXABqvLDyqNmwvfPsYfyujIT92X9FzuiPF_KFuGztqFSqXUdrYc8b2Nlyvd7P-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.37M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-76995">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پیام‌های دریافتی یک ساعت و نیم پیش:
‌
درود بندرعباس ساعت ۱۲:۳۱ دقیقه انفجار شد
بندرعباس انفجار ۱۲:۳۱
بندرعباس دو انفجار شدید
پایگاه هوایی 12:31
سلام بندرعباس ۱۲:۳۰ صدا انفجار اومد پایگاه هوایی فکر کنم زدن
سلام دارن بندرعباسو میزنن خداحافظ
آبادان بریم صدا اومد 13:19
صداش هم با لرزش بود ینی احتمالا درست شنیدم
صدای انفجار اومد تو ابادان
کجا بود و نمیدونم
هرچی بود اطراف پالایشگاه بود احتمالا باز پدافند الفی یا جزیره مینو
سلام وحید جان، صدای انفجار در آبادان
سه بار شنیدیم
ساعت ۱۳:۲۷
بندرعباس
ساعت ۱۲:۳۰ ظهر امروز دو تا انفجار بزرگ تو پایگاه هوایی رخ داد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/VahidOnline/76995" target="_blank">📅 15:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76994">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aad6931866.mp4?token=G-TTQE8Z3gomiipOOV_zhPZIl_MO12qbPqGeKMjMiTcT_x6p_S_Kd701PkmKyy7DJnnOdoGlEC1-Aden2Tbg_vQg8nz5hAfq-VjjhnDes3TMeeajb_FP3xd99ksVnst6lbKBlLmNUFTzonhVfe3-QwPYZ-K6KlvXzKTIbyA0lIjEacRzT8CLkr0qY6zuu1TVKSxZeA-V-EAvVc1EuQKyRFa2BQr2_NSrDnx7FfkFHrk5XD6-2ovoU3KSJQcX2nIhVk0J91Mf-809q7tAX9ImiJzZxJooju2higdeepqjboWaN7iVENVoAOb41yzG4oGWuTZH_5qxoI9_RZOA4330fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aad6931866.mp4?token=G-TTQE8Z3gomiipOOV_zhPZIl_MO12qbPqGeKMjMiTcT_x6p_S_Kd701PkmKyy7DJnnOdoGlEC1-Aden2Tbg_vQg8nz5hAfq-VjjhnDes3TMeeajb_FP3xd99ksVnst6lbKBlLmNUFTzonhVfe3-QwPYZ-K6KlvXzKTIbyA0lIjEacRzT8CLkr0qY6zuu1TVKSxZeA-V-EAvVc1EuQKyRFa2BQr2_NSrDnx7FfkFHrk5XD6-2ovoU3KSJQcX2nIhVk0J91Mf-809q7tAX9ImiJzZxJooju2higdeepqjboWaN7iVENVoAOb41yzG4oGWuTZH_5qxoI9_RZOA4330fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: سنتکام موج دیگری از حملات علیه ایران را به پایان رساند
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ۱۲ ژوئیه موج جدیدی از حملات تهاجمی علیه ایران را به پایان رساندند و با مهمات هدایت‌شونده دقیق، ده‌ها هدف را در چندین نقطه مورد اصابت قرار دادند تا توانایی ایران برای ادامه حمله به کشتیرانی بین‌المللی در حال عبور از تنگه هرمز را تضعیف کنند.
نیروهای سنتکام با استفاده از جنگنده‌های آمریکایی، شناورهای نیروی دریایی، پهپادهای تهاجمی یک‌طرفه و برای نخستین بار، شناورهای بدون سرنشین تهاجمی یک‌طرفه، سامانه‌های پدافند هوایی ارتش ایران، سایت‌های راداری ساحلی، توانمندی‌های موشکی و پهپادی و قایق‌های کوچک را هدف قرار دادند.
تنگه هرمز یک کریدور دریایی حیاتی برای تجارت جهانی است. ایران کنترل آن را در اختیار ندارد.
نیروهای ایالات متحده در وضعیت استقرار و آمادگی قرار دارند تا تضمین کنند که با وجود ادامه تجاوزهای بی‌دلیل، مزاحمت‌ها، تهدیدها و اعلامیه‌های خودسرانه ایران، آزادی کشتیرانی همچنان برای کشتی‌های تجاری برقرار بماند.
CENTCOM
سپاه: پایگاه آمریکا در بحرین را نابود کردیم
اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی به نقل از منابع حکومتی:
بسم الله قاصم الجبارین
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ كُلُّهُ لِلَّهِ
🔺
رژیم شرور و جنگ زیست آمریکا که از آغاز تاسیس تاکنون زمان‌های اندکی را بدون جنگ و شرارت نظامی سپری کرده و از شکست‌های اخیر در مواجهه با رزمندگان اسلام هم درس عبرت نگرفته و به تجاوزات خود ادامه می‌دهد.
🔺
در پاسخ به این شرارت‌ها، رزمندگان هوافضای سپاه در مرحله دوم عملیات مقابله به مثل خود مراکز مهم تعمیرات و نگهداری بالگردی، آشیانه هواپیمای جنگ الکترونیک پی ۸ و مرکز فرماندهی و کنترل پهپادی ارتش کودککش آمریکا در پایگاه آمریکا در شیخ عیسی بحرین را در هم کوبیدند.
🔺
عملیات مقابله به مثل ادامه دارد.
إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ وَيُثَبِّتْ أَقْدَامَكُمْ
سپاه: آمریکا را در کویت منهدم کردیم
بسم الله قاصم الجبارین
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ كُلُّهُ لِلَّهِ
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانه پدافند هوایی پاتریوت در پایگاه آمریکایی در علی سالم کویت و همچنین یک سامانه راداری راهبردی FPS در پایگاه احمد الجابر را به طور کامل منهدم کردند.
🔹
عملیات مقابله به مثل فرزندان غیور شما ادامه دارد.
🔹
تنگه هرمز سرزمین ماست و اجازه نخواهیم داد یک ارتش یاغی و کودک‌کش از آن سوی دنیا به دخالت‌های غیرقانونی خود در آن ادامه دهد.
إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ وَيُثَبِّتْ أَقْدَامَكُمْ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76994" target="_blank">📅 06:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پیام‌های دریافتی:
درود همین الان صدای انفجار بندرعباس
ساعت 5:47 یک انفجار بندرعباس
سلام وحید
صدای انفجار  الان توی بندرعباس
خیلی شدید بود
سلام بندرعباس الان صدای انفجار اومد ۵:۴۸
سلام وحید 5:47 دقیقه بندرعباس صدای انفجار اومد
۵:۴۸ بندرعباس صدای بلند
05:48 بندرعباس صدای انفجار، خیلی زیاد بود صداش
5:48 انفجار مهیب در شرق بندرعباس
فاصله یک ساعت و نیمی ازمون نهایی صدای انفجار مهیب بندرعباس
سلام ۵:۴۹ بندرعباس یه صدای انفجار شدید اومد
سلام همین الان صدای موشک در بندر عباس شنیده شد
همین الان بندر عباس صدای انفجار ساعت ۵:۵۰
بندرعباس
ما ۱۲ فروردین هستیم
کامل شیشه لرزیدددد
درود آقا وحید همین الان
بندرعباس انفجار خیلی شدید
بندرعباس الان صدای انفجار همرا با لرزش شدید
5:47تک انفجار بندرعباس
صدای انفجار نسبتا شدید بندرعباس
بندرعباس همین الان انفجار خیلی شدید از توی خواب پریدیم
وحید ۵:۴۸ یه انفجار خیلی بزرگ بندرعباس صداش ب شدت زیاد بود
صدا اومد  موجش خونه رو لرزوند همین الان بندرعباس خونمون نزدیک جاییه که موشک میزنن
سلام بندر امام از ساعت چند همینطور دارن میزنن
🔄
صدای یک انفجار دیگر ساعت ۵:۵۱
05:51 یکی دیگم زد
صدایی بلند تر همین الان
دوباره انفجارر
دوباره زدن ۲ تا انفجاز بندرعباس همین لحظه ۵:۵۱
دوبارهههههه
سلام همین الان دوباره صدا انفجار اومد بندر
بندرعباس دوباره صدای انفجار اومد ساعت 5:51
ساعت 5:51 یک انفجار دیگه بندرعباس
سلام ۵:۵۰ بندرعباس دوباره صدا انفجار اومد خیلی شدید بود
این دفعه چیزی تکون نمیخوره فقط صداش بلندههه
واییی دوباره زدنن
دومین انفجار شدید تر
نزدیکی پایگاه هوایی
سلام
صدای وحشتناک انفجار از سمت دریا، همبن الان بندرعباس 05:52
سلام میشه خواهش کنم بذارید تو کانال؟
الان دارن حمله میکنن
بعد ما باید یه ساعت دیگه آزمون نهایی بدیم اگه خدایی نکرده کسی خون از دماغش بیاد کی پاسخگوعه؟ جدی باید یه فکری به حال ما دانش آموزا بکنن
همین الان ۵:۵۳ بازم یه انفجار شدید بندرعباس
خونمون داره میلرزه
😳
بندرعباس
بندرعباس پشت سر هم داره میزنه بعد بچه های یازدهم یه ساعت دیگه باید مدرسه باشن آزمون دارن
نهایت نامردیه در حق بچه های جنوب شب تا صبح چشم رو هم نذاشتن از صدای انفجار
بندرعباس احتمالا مناطق نظامی داخل شهر (نیروی دریایی سمت صداوسیما) رو داره میزنه که صدا اینهمه واضح و شدیده
چون انفجارهای قبلی رو ما با اینکه تقریبا وسط شهر ساکن هستیم متوجه نشده بودیم.
🔄
صدای یک انفجار دیگر شدید ساعت ۵:۵۵
بندرعباس باز زدن ۵:۵۵
۳ انفجار دوباره ۵:۵۵ بندرعباس
05:55 از بقیشون شدیدتر بود
آقا دوباره انفجار
وحید بندرعباس همچنان داره میزنه
صدای سوم انفجار در بندر عباس 5:55
۵:۵۵ دوباره صدای انفجار
5و55 دوباره زدن بندرعباس
بازم زدن هر بار شدیدترر
بندرعباس انفجار ۵:۵۵ درگیری از سمت ساحله
۵:۵۵ سلام برای بار سوم صدای انفجار بندرعباس اومد خیلی شدیده
آقا وحید سومی هم خیلی شدید بود
۵:۵۵ یکی دیگه زد خیلی بد بود
دوبارهههه همونقدر صدای بلندد و لرزیدن شیشه ها
برای بار سوم
این بلند تر از دوتای قبلی
۵:۵۵ انفجار سوم بندر عباس
۵:۵۵ صدای انفجار ب شدت بلند و مهیبه خونه رو کامل می‌لرزونه
بندرعباس ساعت ۵:۵۵ سومین تک انفجار قوی
وحید جان قشم هم صدای انفجار حس میشه خیلی شدید نمی‌دونم کجا اینجا یا بندر
بندرعباس صدای انفجار سوم
خیلی شدید بود
هر بار شدتش بیشتر میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76992" target="_blank">📅 05:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cFDn-0-Q3stux-1hOnLmJ91jSzrvLjXmJGxZ0DcCYiDk-ckHrkt8rf4E2z-J89pBOZpGmAQf5IYm0rxMrULHS3Plaskzrb9esEE70mDCaUCc2vJED0KRBeaXOB8vZAQ0obShloIqioUaGduaudfFgXmclq-4IQa7_fNLNcpZZFSqV7BHkJtS8WtgT3qZnhlKGXT4We-Wa-d9cOV-lDgVxjyffLcGSHW9HOITFS06WOBB8Py5dX8PCJS4TuuORauNLsilX_WPRfGm1bNbRh2houn3ziuQISOHD3R8GWwZ7qpKC3pbvK4GqFrDv36JCCqkuGRdCHF1ZfvxsWu33cicug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HnteobKk2_Iq3oSSMJY_QBd5tT--pIq8FYhG5Rx5S9X9TbXZyf4GmSQMF5xdl_d-vh54aMIL4z8hq0V20Es_4ZWkZ4EQ5E1Q7FaSpHWz4yZKYi9WsT_h4lGre2D8BdZJPYlutSI_wQkJLYTkKg5DBt7v_hyTKKB_CWk6Ik6Z1OkAz6l9-Im4qp-bNo3dQ9dvHcnMCPBacKBzMZ6EkbZhGqXhpsB7Wq8u3yMb0w0BrDSZAXZM9aqMIIoIPdUe-tgDi-FHdQpOCnoDlmcsoAysBmFfJEUJiUgxxA1f8qhiv3p6euBHl87elmbnhnlfgfOLi8ySUTV5DzSZUluuwT6LDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/79d39aa187.mp4?token=i-3-Xw1u4Jt8PzqqoKSKv1U5BDgpfakz3eVCIIdAFZlI8K0Md-E4wuzcf5rAB2bHc658gJA1iT5pKhnVlth2DhIihIc6LVFZXMRYKua1QKudFHFqMNN9g0G-WiY7nyNUrFxxpXFFLaHJyb1oKmMIMFA-GyOViyo9tnjbrCTTobrBOyqCEfNPVOCeATJ5Le-SE41iwoqWssxBA-XEIIUyhYkBfo4CHHFIJKSGw-5ku6iPwbGXEZLwhyCioghaCEVW_cgLx7qNfyaPHNyi9hYkPke1Ym6vQzAkCo926oXr187qdYggw_2QFTidXX4ekDR86naEbVtYx5DEf5kbaK3RtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/79d39aa187.mp4?token=i-3-Xw1u4Jt8PzqqoKSKv1U5BDgpfakz3eVCIIdAFZlI8K0Md-E4wuzcf5rAB2bHc658gJA1iT5pKhnVlth2DhIihIc6LVFZXMRYKua1QKudFHFqMNN9g0G-WiY7nyNUrFxxpXFFLaHJyb1oKmMIMFA-GyOViyo9tnjbrCTTobrBOyqCEfNPVOCeATJ5Le-SE41iwoqWssxBA-XEIIUyhYkBfo4CHHFIJKSGw-5ku6iPwbGXEZLwhyCioghaCEVW_cgLx7qNfyaPHNyi9hYkPke1Ym6vQzAkCo926oXr187qdYggw_2QFTidXX4ekDR86naEbVtYx5DEf5kbaK3RtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره شلیک موشک از بوشهر
Vahid
سلام ساعت٥:٢١ دقيقه صبح از شهرستان جم موشك بلند شد
همین الان جم چهارتا موشک بلند کرد
سلام وحید
شلیک موشک از جم-بوشهر ساعت 5:21
سلام ساعت ۵:۲۰ از جم صدای پرتاب موشک اومد
همین الان جم چهار تا موشک پرتاب شد
ساعت ۵:۲۰ بامداد چهار موشک‌از شهرستان جم بلند شد
وحید جان سلام . همین الان از جم ۴ تا موشک زدن
پیام دریافتی:
direct impact in bahrain, smoke visible from far away
[اصابت مستقیم در بحرین؛ دود از فاصله‌ای دور قابل مشاهده است.]
🔄
وزارت کشور بحرین با انتشار هشدار فوری در اکس اعلام کرد که آژیرهای خطر در این کشور، صبح دوشنبه، به صدا درآمده‌اند. این نهاد امنیتی با صدور این بیانیه، از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش کامل، به سرعت به نزدیک‌ترین مکان امن و پناهگاه‌ها بروند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76988" target="_blank">📅 05:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FU9wQNlNIuu2BgyIGTViqCz9Dwaytaa_kup8Nh3jAIf47xapwEX6giKgxVnp9aaWDFtzYtqbSIt3clDCZI5Z7xcCSL59lppf45Eb0x_-DylBMuqKUjJy1gM0q5UGMT3UJSr5gTyHuXAWBMu_S3oNhCogWXxPY3CacmCXH5Dpdo8BPV6H-Q_4u5w6HXu2bscfNRpB-o_XgFp9Uu4iIA8hotL9gkMuMwtDieqYAy1GsVk3iUWjmJW321nhMC6-e0mVl58Zgvn351mbq-q55oqI71j1hSzRnmMGlfytmsl7vjIJpO1GaiiCD4UUMjKJs7IyZ4JMY3GvfxR1FzAwvVYAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در
تروث سوشال
عکسی از لیندزی گراهام منتشر کرده است با کلاه
Make Iran Great Again
سناتوری گراهام در این تصویر کلاهی بر سر دارد که روی آن نوشته شده است «ایران را دوباره با عظمت کن» و عکسی بزرگ از صفحه دونالد ترامپ در دانشنامه ویکی‌پدیا را بدست گرفته است.
دونالد ترامپ در این پیام غمگینی عمیق خود را از درگذشت سناتور لیندزی گراهام ابراز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/76987" target="_blank">📅 05:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ce9a9iPUoJISI1qVcCX0B8oUztAKPJvhINeznDVzvS9AE8OKs3JJld2K-K69J9DHJs2ss8b2w7q_So1ApL4KS-TQ_XumoJfH8TdSKSp8kqeDl7bT8HRAe8kd2cSGf7nZxUMJa4BBbKDHNRa9sOIHsJto6b8SoeyP7NbpY5OCP8N8aHMAbvBdbbF1j5XUpgQzI5cRumCZTcgqH-TiWQt4P5o429iADeEcCd6JCNyN114qXLp3QzQtMI3MO1OKwsoYEfREswQaDWCluhDSoaL6E6-CavWPfse8EKTmYq7DbRTX0wCAqMl-_EQCKRqkD10f_jvCjHueGQ9O0czzFpZ65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fKb1OR4YQs7ncILWu9ilTbG64q1x7-GNakpi2t-hojKn0uJjivee3euvXrZUu0upQqhtjJm35tacHzPa62jZy5kZDrxOueSuI8Pl9zpvzJ9b94iUa3d5e8Mzhnkd0vRyIHbl0OExgQl7k8hOQlytCepQUMdR83C0pE9IW345MC49j3Di9idrXW3nncGJbQ-6n2B0ch6FJCiaxU2jWsnTCNTyeYFtAIhmas21TxWAMH1CKxtXYHPI6paYISIrWkD5UEwsHCJjyWJqbM5GH9DZt0CCsrQl9oEHhKhce6YT9C7lr_EXwmt6PEcCnbiFC9hJ9VUb3EUNltnvb94NvjcZ7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان دوباره ساعت۴:۲۸ دوتا موشک از خمین زدن
شلیک دو موشک از خمین
درود ساعت 29 4  الیگودرز دو شلیک موشک
خمین الان دوتا موشک
وحید از سمت خمین و الیگودرز دوتا شلیک کردن ۴:۳۰
همین الان صدای انفجارزیادامد
من حوالی شهراراکم سمت خمین بود
خمین ساعت ۴و۲۷ دقیقه موشک پرتاب شد
+
از زنجان و ازنا هم پیام‌هایی دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76985" target="_blank">📅 04:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VSeSNEwm9ExvmwlIXIrL50mYGmBT0TDQHnUpWB4ry56cksBj-GfbGviu0VJKL18S9TPw5nJ5vIJv7BI7x5PVoatZnXlPTHBrC8Ko7Vr7jVBO_HG4IyTfV0sO-wU0Ie8Oc94BHFO_ZfTUpsvk9SXTtAHRKODob6-x1bhZqyeda7s33JA2YKxtgQcK5-j5h3eppixRXfmXWTXg6xCCGEIS28yRcqaXNYrkq9pHKK7BaLX99Qj6gCnMPKnfMpHnpKeq2MCCPjn2EZOIN-TNgyX8BWSL3jPP93gwJxH2CxPog06dmMbwFvfPEu8JB6ou6BknjQ449L_QopkoMCXMmX-keQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l2Ac4F8vfXUg7Of4CTW8E9ApF6FK3LY65QAlKCDm6vki9BS4v0_tuYDRK8isF7PsT3kapYqYYL3B5--LVpuyPzPZB2YTrU2wmWYBuF1hnwMf1-YI2CdWtbin1-MYF39SKy7VETIVzYRZNAJD5sJ4PEP2rZu2zCPky5udcjXxe1P2bIp3gFK_XUp2hvSQPnaCULGEWWa6oj3NX8q-p_dJIM1tDeJW7i_Z5A4SESQ5I5ipSuwtlzudr1oZ319sd9PyylCfAAC9PqTlbG4ZapBghUy09hkg12TwQD4gjIzjK7BmlKcxFlGX2ixSzFhvysrClLAsN9hH67689LoIqeqqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BgiFawh7I_5Z6jWh3EK4StxL6YXN2io86hcZu8E_D1VrxUoRGzt2u3zLE4oFYDlvRnl7qi4plU5CmIryarvvEzI4-hioLgV8r978cd5MPnLKZpdoAWsVHe4reRq2ogDY5oXNWBzaWPUdwnHXR89o8YBeT11T8X-VEnFx5pMsMLSwKTkdxaBWvzFcnDPCAiOLqqCJp7tgxnzWUFqRy9sFgSyDsj7tEiRlAlUNDNY9WJG3u870IWJFJ5qQstXDcQ3a8jLEx4Ci-9rJl5qIyLN4UyjSCJXCvPPiBt0u4geaBvfrGeeWZI5iOUuF7uQkfbRp_0DlszsUc6GhBzYVmvXpvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/892957aa92.mp4?token=dlaUHyLigSpG5Hj328Q4WYEL2O8QKQnp0GlChYZTTgECkTsVosukZfFiqzfexNKshuswLCRwuJxayjyq8os6dCENKsMocmpqYTutf8B2UNdfd3voEfw58AHZanbocLYS3-u_Jztcl0eZ1M6-KSlS192yngzuzw-Q_pQg5hJB6V2_IeGlctLxuFMbW2kuforUJB0uAqOCYVsEXHWV-s5YGwRu2L26zDXHiCBsIp-EDaRBSOB1T0nnvgsag0zaN4Q32j_GprvJ0BHqX_GdJDMEuKmsjLehnSzr3UoM0fCHMOCV3zwg8OwxlliHAxv96yOTTeMNXFe7MFG7PISj65MdYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/892957aa92.mp4?token=dlaUHyLigSpG5Hj328Q4WYEL2O8QKQnp0GlChYZTTgECkTsVosukZfFiqzfexNKshuswLCRwuJxayjyq8os6dCENKsMocmpqYTutf8B2UNdfd3voEfw58AHZanbocLYS3-u_Jztcl0eZ1M6-KSlS192yngzuzw-Q_pQg5hJB6V2_IeGlctLxuFMbW2kuforUJB0uAqOCYVsEXHWV-s5YGwRu2L26zDXHiCBsIp-EDaRBSOB1T0nnvgsag0zaN4Q32j_GprvJ0BHqX_GdJDMEuKmsjLehnSzr3UoM0fCHMOCV3zwg8OwxlliHAxv96yOTTeMNXFe7MFG7PISj65MdYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'انفجار و آتش‌سوزی [سمت] فرودگاه
#امیدیه
در خوزستان
دوشنبه ۲۲ تیر حدود ساعت ۳ بامداد'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76980" target="_blank">📅 03:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌های دریافتی:
‌
اهواز صدای خیلی شدید اومد
همین الان انفجار شدید اهواز
درود وحید جان ، همین الان اهواز صدای انفجار شدید اومد ساعت 1:31
اهواز ساعت 1:31 بامداد صدای انفجار
اهواز ساعت ۱:۳۰ صدای ۳ تا انفجار
هواز همین الان زدن ۰۱:۳۲
سه تا موج انفجار پشت‌سر هم ، شدید تر از دوران جنگ  بود ، من مرکز شهر ساکن هستم
سلام دارن اهواز و میزنن ساعت 1/28دقیقه
سلام وحید ساعت ۱:۳۰ سمت فرودگاه و گلف رو زدن خیلی وحشتناک بود
😭
😭
😭
سلام  آقا وحید. اهواز ساعت ۱:۳۰ دو تا انفجار پشت هم
وحید همین الان ساعت ۱:۳۰ اهواز رو زدن، کیانپارس خیلی شدید حس کردیم
اهواز دو تا محکم زد
ساعت ۱:۲۹
اهواز و‌همین الان زدن صدای سه انفجار اومد نزدیک سیصددستگاه/سپیدار
اهواز صدای انفجار
سلام الان ساعت ۱:۳۲اهواز سه صدا انفجار اومد
اهواز همین الان دو صدا همراه با لرزش ساعت ۱:۳۰
وحید جان همین الان ساعت  ۱:۳۰ اهواز صدای انفجار اومد.
وحید جان اهواز صدای انفجار شدید
وحید انفجار به شدت قوی تو اهواز خونه لرزید ۱:۳۰
سلام وحید جان ساعت ۱:۳۰ اهواز صدا دوتا انفجار اومد منطقه کیانپارس یک مقدار ضعیف بود صداش
سلام وحید
ساعت ۰۱:۳۱ اهواز صدای انفجار اومد
فکر کردم خیالاتی شدم، اومدم بیرون دیدم همسایه ها هم ریختن بیرون
وحید جان
اهواز ساعت 01:31  دو تا یا سه تا صدای شدید اومد
اهواز لرزش شدید و صدای انفجار
دقیقا نمیدونم کجا، اما زاویه‌‌ی صدا از سمت چهارشیر بود به نظرم فکر کنم سپاه چهارشیر
صدا انفجار ماهشهر
ماهشهر همین الان
ما اهوازیم کوی باهنر
صدای انفجار شدید
بندر ماهشهر صدا اومد.
اهواز ما سمت کیان آبادیم و واقعا صدای انفجار زیاد بود
🔄
همچنان خوزستان:
انفجار شدید ماهشهر"همین الان"
دوباره الان ماهشهرو زد،1:51
شش انفجار 1/52 قشم-طولا شنیده شد
سلام ماهشهر هم صدای انفجار اومد
دوتا تا این لحظه 1:52
سلام وحید جان اطراف بهبهان تا الان صدای ۶ انفجار اومد
همینطور دارن میزنن
سلام قشم همین الان صدای چند انفجار
صدای از دور از سمت غرب جزیره
همین الان صدای انفجار زیاد بالای ۵ تا داخل قشم شنیده شد
بهبهان ساعت 1:52 بامداد صدای چهار انفجار شدید
سلام وحید ما نزدیک فرودگاه ساکنیم حدود ساعت حدود یک و نیم دوتاصدای انفجار اومد همه همسایه ها ریختن بیرون معلوم نیست کجارو زدن
قشم ساعت ۱:۵۰ زدن ، چندین انفجار شدید
بهبهان‌رو الان چند بار زدن
روشمهر پایگاه موشکی ساجد
بهبهان خوزستان/ ۱:۳۲ ... صدای ۲ انفجار.
مجددا ۱/۴۵ تا ۱/۵۰ بهبهان خوزستان صدای ۴ انفجار
سلام وحید جان
امیدیه صدای بسیار خفیف انفجار
مشخصاً درون شهر مورد هدف قرار نگرفته
احتمالا دقایقی بوده
همین الان خوزستان بهبهان ۴ بار پشت سر هم زدن
نمی‌دونم کجا بود
🔄
ساعت ۲:۱۵ دقیقه دزفول رو زدن
در و پنجره ها لرزید
دزفول خوزستان
همین الان زدن
سلام وحید
دزفول رو دارن میزنن
۰۲:۱۵ دقیقه
سلام دزفول رو دوبار پشت هم زدن
🔄
موج بعدی پیام‌ها از دزفول درباره شنیدن شدن صدای انفجار در ساعت ۲:۱۹ و ۲:۲۵
🔄
امیدیه ساعت ۳:۰۲
درود امیدیه خوزستان همین الان صدای چندتا انفجار پست سر هم اومد
امیدیه خوزستان چند دقیقه پیش ۴ تا پشت هم زدن کل شهر لرزید
ساعت 3:02 دقیقه
صدای بشدت وحشتناک توی امیدیه اونقد که شیشه ها لرزید
پازنون هم زدن
صدای چند انفجار  در امیدیه شنیده شد
حدود ساعت 3 بامداد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76979" target="_blank">📅 01:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76977">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H6ImycqV23u-4MXMf-ZttpJnUcP-PO9Z2vwMjeWFWZoiCAMvM5cvf5ncepidRNR7R9aBMvXDk8Ai023uB4F1ZJiORH6ulx6P7n3SEKdlIVZb0OnAd5R0-7JylFdlEkF_Pk6gdcIdXJy1z6Jj4r83tf6raVTxJbXFdOmXi8VdZV_FISSBuX28tGZtCzN5HEqQnYoTlq7twJFJeadm-gLZtQxPQpBBIRNAxd8mMHl_ruzzAuTSKFAlsBIcfZi8rX5Q8eLT6N1d5mGcOe7IOKhlVzgUiXYvViF2CqsNSZiTEJuxwF-0hUnAcG-iJOiQDnSoJ7y_Tr_a8d5ggia0MDauxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cfc3526ac6.mp4?token=j1dmMb828NhgB8y5jhHiedPOOmRzmngjOIamQgTytmny9kTJEQuIjuCArVkoalX4HZy6g84b_nvNgGB9__lT2iq5xB3xX7itMSybP-1WfaSB-mxr7jqgsvABabqDq69-NngUbtazYkQxFjhkdOUbJ6vBLZsGUSoIuVHEAbliKs7n43TW-XysTREJbcKSdvd3geMrdea7gJBD0TDByLWi9Q4-toDeq1q0lWjx7z1ED3zvY2oluG5FnzRdBTFjnEXlx5cbHMgKwHpyIrBdZTUqUJez7-eBEYPNCNsZgnX9p1body-OvN4EXlnkgwfhCHJKbMrb63fCzSU3cnrjI-2FVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cfc3526ac6.mp4?token=j1dmMb828NhgB8y5jhHiedPOOmRzmngjOIamQgTytmny9kTJEQuIjuCArVkoalX4HZy6g84b_nvNgGB9__lT2iq5xB3xX7itMSybP-1WfaSB-mxr7jqgsvABabqDq69-NngUbtazYkQxFjhkdOUbJ6vBLZsGUSoIuVHEAbliKs7n43TW-XysTREJbcKSdvd3geMrdea7gJBD0TDByLWi9Q4-toDeq1q0lWjx7z1ED3zvY2oluG5FnzRdBTFjnEXlx5cbHMgKwHpyIrBdZTUqUJez7-eBEYPNCNsZgnX9p1body-OvN4EXlnkgwfhCHJKbMrb63fCzSU3cnrjI-2FVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: 'بندرعباس، ساعت ۰۰:۴۳ بامداد دوشنبه ۲۲ تیر'
Vahid
صدا و سیما:
بر اساس گزارش‌های اولیه، حمله امشب به دکل مخابراتی اطراف روستای طاهرویی سیریک بوده، همون جایی که در حملات قبلی هم مورد اصابت قرار گرفته بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76977" target="_blank">📅 01:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WRFjvEWNF5urDLBZdZAltarhyWf4gjKemV4x36qUogKkBYfh6LNzXpveWweUPRzLMcOjwfT4mLVxqWoFyJJy69xU5R6MkxsG7jun7LNpBycp9211vr-IKP50KlD2bAjjwsGy0dYX8f9XxJ0O37wy_0E3onrkmEJ0f_USmi5pn7JNBus82tXRNv6YTMF9d84FaP3JsLqy4ebU2bNfG-sLtVGWOLSNEUVsjOJM9d7AHcxnEeiXhdBNaBk8dqdOCM0dgdcU4bt4y7QyP8frWg3aUruh-gVf8ppwa6CV5Mxv8pYIi7s-tr7WSH6JbI3Hlj6KsLfyQIPoj14_q7CEHb6-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت سنتکام:
ساعت ۵ عصر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به تضعیف توانایی این کشور برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند.
فرمانده کل قوا دستور این حملات را برای پاسخگو کردن نیروهای ایرانی صادر کرده است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76976" target="_blank">📅 00:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیام‌های دریافتی:
00:38 صدای چندین انفجار در بندرعباس
همین الان انفجار پیاپی بندرعباس ۰۰:۳۹
بندرعباس ساعت ۱۲:۳۸ صدای انفجار چنتا اومد
باز هم داره صدا میاد
بندرعباس همین الان چهار پنج صدای انفجار پشت سر هم اومد
😭
صدای سه انفجار بندرعباس ساعت ٣٨ دقیقه بامداد
00:39 بندرعباس سه چهارتا صدا اومد
قشم الان صدای انفجار اومد
ولی از خود جزیره نبود، بندرعباس سیریک یا روی دریا بود
سلام وحید از بند عباس خبر میدم صدا ۳ تا انفجار شنیدم شدید بود شیشه ها لرزید
🔄
جنگنده الان بالای شهر جاسک
۴ تا صدا انفجار اومد
دوباره جاسک داره میزنه
همین الان
سه انفجار درجاسک
همین الان دوتا انفجار جاسک
صدای جنگنده هم خیلی زیاده
صدا و سیما:
🔺
دقایقی پیش؛ شنیده شدن صدای چندین انفجار در اطراف روسنای طاهرویی سیریک
🔺
صدای سه انفجار در جاسک شنیده شد
🔺
صدای چند انفجار در قشم شنیده شد
🔄
خنداب در استان مرکزی:
سلام وحید جان. همین الان سمت ساعت  یک بامداد صدای جنگنده شنیده شد.
خنداب.
همین الان صدای انفجاررر
سلام ۳ دیقه پیش خنداب رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76975" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXfhTa8f_7WKlopYIUb0tJTrt7es0VeD0QJVGHNcSZQN64f9yMeALvBS7eotgz6-ZGQNzYGaFEXD3RCH7rSu2No6F3zzTVa3cDoaUsAPwNCrFVGHQB-xJPQ9V2h6QyseTKwAA4XByPtZgd31p7YDOhMg085lXHIdUAKWWW-v7iUZHadn8HnahkH-cv6DyONq0ywslnArHE_B429CjSAYckuyNqFmZP7vugoKEamnZE1KGCjaY2s-6czLbFMbKALmkp33gDKbaetQtvIug2CE8odAU-gE5oN_fH0MTFbmrHlQ8NGbWor2ajrwwLmTKrwYFJN9xdxwhfRWwrmrAMqa5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی آمریکا (سنتکام) شامگاه یکشنبه ۲۱ تیر، ادعای رسانه‌های وابسته به جمهوری اسلامی درباره کشته شدن نظامیان آمریکایی در کویت را رد کرد.
سنتکام
نوشت
:
🚫
ادعا: تبلیغات ایران امروز مدعی شد که سه نظامی آمریکایی در کویت بر اثر حملات ایران کشته شده‌اند. نادرست.
✅
حقیقت: هیچ گزارشی از کشته یا زخمی شدن نیروهای نظامی آمریکا در منطقه وجود ندارد. وضعیت همه نیروها مشخص و تأیید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76974" target="_blank">📅 00:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76973">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبرگزاری مهر:
گزارش‌هایی از شنیده شدن انفجار در جزیره بوموسی؛ وضعیت جزیره لارک عادی است
ساعتی پیش منابع محلی از اصابت ۲ پرتابه به جزیره بوموسی در جنوبی‌ترین نقطه کشور خبر دادند.
در حوالی ساعت ۲۰:۳۰ امشب، صدای چند انفجار دیگر در بندرعباس شنیده شده است که به نظر می‌رسد مربوط به شلیک یا اصابت‌هایی در محدوده دریایی بوده است.
پیگیری خبرنگار مهر از جزیره لارک نیز حاکی از آن است که وضعیت در این جزیره واقع در تنگه هرمز کاملاً امن بوده و هیچگونه گزارشی از حمله یا حادثه‌ای در این منطقه وجود ندارد.
اخبار تکمیلی متعاقباً ارسال خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76973" target="_blank">📅 21:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76970">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z5mIE3ZgkI9eXiFu5RyVonNu1_DqwSwkXO_d8PF0Jc-xwOdHj8J8gmWbh68GNdSDmv6hISdpEil9W6VP-JOivRbaGxRHT9gY_vsuxFpB6z9TOB_D0bw9D5FFgQzh91v0x6ZSxkBUE6KEaf_ti-GU44BP-NJOTYI5q4S44XzIyVXTRp-efWC5AU6XfEuyLbIOuEeFc-7j9_A9OI34H6jNRmycbsLZNUv_3ofry45EKYVSucSfctMhk9ws4tP49-Oho4bt8n_EgaEwvQ7uEuA0AJSZxu_rEQcNEhacPD4z0CGZyJhuOdq6fW6jQazoeIhdMcjKunW59NK1iOLMTN3H1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v7MXxoapu_QGZNov4Sg7xeqwO0kf3WbrA-pvudddWHyqKEn4VTnCwJ2t3oFs4Vnou746C83x8AI8inEySJuc0QdqoLYQpYXGQf5bMc0maFNoDm7zfVyb27XKB1VgvNp-NF5QjuitW3jseB1mwX_p1NPGB0o8DUaUqKtwfsjRg9694-yGPfAK_yOzJAeiGTqYyRi4Mx-7Ewx2Ly60U4vUcyRoy_pl6OIK6YaEUmCvSw5Bkf11DJWVa3ak3tdsoVicAkjsD4aUcpsIqyWTjAV7rChEfesZlFKOt5uM6-mrQIGamEA2alMPzdstOJ2aJTJw4rQBfreFrERM_BgbIH5_dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83e7b96a5e.mp4?token=KfHrNDnXcPAvG2BJXWKDMMqfBeEkJizdvGhTx9fexNJFXREntfMRjtJ--PRClyftn0-rSOuGjsYrwGF76--pyGh8feKuVK3rIHQWOuJHGtJKKbymQGVVQvTVGyjqAG9hJfM1jsGuz0oakhRAReAXFXSNXvtFLQbB4eit3FWO2Ghv95p3FmvUj6w6by9-q_00DiEvOU7sZQ8z6eAkRxvbDDVMJPGwNEZZ9V6BJ6QfdhD2dGDzfbF3xg4IxYldboUQONmRE3oNLulqdKArVAyqXa8Ux3Xr_7cqgKb1AiSTTHT3ASwYN9LrpcPDcdWRLSb_iGRsR5NqvbLtCJOAYH4UMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83e7b96a5e.mp4?token=KfHrNDnXcPAvG2BJXWKDMMqfBeEkJizdvGhTx9fexNJFXREntfMRjtJ--PRClyftn0-rSOuGjsYrwGF76--pyGh8feKuVK3rIHQWOuJHGtJKKbymQGVVQvTVGyjqAG9hJfM1jsGuz0oakhRAReAXFXSNXvtFLQbB4eit3FWO2Ghv95p3FmvUj6w6by9-q_00DiEvOU7sZQ8z6eAkRxvbDDVMJPGwNEZZ9V6BJ6QfdhD2dGDzfbF3xg4IxYldboUQONmRE3oNLulqdKArVAyqXa8Ux3Xr_7cqgKb1AiSTTHT3ASwYN9LrpcPDcdWRLSb_iGRsR5NqvbLtCJOAYH4UMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای شاخ‌دار دکتر کلانتر معتمدی درباره رابطه واکسن فایزر با نازایی و عقیم شدن زنان
🔹
محمدرضا کلانتر معتمدی، دبیر فرهنگستان علوم پزشکی، در یک برنامه تلویزیونی گفته است: «بعد از ۸ ماه مشخص شد واکسن فایزر حاوی همان ماده‌ای است که در واکسن ابولا بود و دختران را عقیم می‌کرد.»
🔹
این ادعا صرفاً تئوری توطئه بی‌پایه و اساسی است که از سوی پزشکی مطرح شده که در جریان تحولات علمی روز قرار ندارد.
🔹
واکسن کرونای فایزر چه در ساختار و چه در عملکرد، شباهتی به واکسن‌های تأییدشده ابولا ندارد.
🔹
سازمان بهداشت جهانی تأکید می‌کند: «هیچ شواهدی مبنی بر تداخل واکسن‌های کووید-۱۹ با باروری وجود ندارد و هیچ مدرک بیولوژیکی وجود ندارد که نشان دهد آنتی‌بادی‌های ناشی از واکسن یا ترکیبات آن آسیبی به اندام‌های تولیدمثل وارد کنند.»
🔹
محمدرضا کلانتر معتمدی، پزشک و جراح است و به عنوان عضو، دبیر یا حتی رئیس گروه‌های علمی فعالیت می‌کند، اما اغلب اظهارنظرهای او در فضای عمومی جنبه اجتماعی و سیاسی دارد.
🔹
ما در منابع عمومی چند مقاله از او پیدا کردیم که عنوان موضوعات آن «اقتصاد مقاومتی در نظام سلامت»، «فقر و هزینه‌های جراحی»، «تجربه‌های دفاع مقدس» و «مولفه‌های فرهنگ ایثار و شهادت در جامعه سلامت کشور» است.
🔹
او یکی از امضاکنندگان نامه منتسب به «۲۵۰۰ پزشک» است که چند روز بعد از ممنوعیت واردات واکسن از سوی خامنه‌ای اعلام شد.
🔹
بررسی‌های فکت‌نامه
همان زمان توضیح داد که هم محتوای نامه بی‌پایه و اساس و تئوری توطئه است و هم نامه‌ای که به «۲۵۰۰ پزشک» منتسب شده کمتر از ۱۸۰ امضا با نام‌های تکراری و مخدوش دارد.
🔹
با این توضیحات فکت‌نامه به این ادعا نشان
«شاخ‌دار»
می‌دهد.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76970" target="_blank">📅 20:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76969">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8bbd214211.mp4?token=E7aVf6MmkrQAv0IZ0dQgCfMWmKMA2cGfLkITddRZqjuv0Vkjwhe3D6rtYRqgBLJsj7bHEWVWFOSk3CK49NVMqnsxUBnRFpupeSyE-MYL2ECEmWh0ePZ-Nz1JW8NneUsWzOVTTwUZvcNCSznuKWN7Bd29Q_zbrus1GhTeq8sTPI6M_ub0eoox-ru1FUVEFzEdmYtxhRxRkRkr7GpBpSMkay1ILKar7JXdlNbSh5mtBTovF4VkxatO71_6rTMT1hFKh0KAT1pqxQE4JCAkZ-Ufy_2wsPs3ripS8jNTGSeng6w4J4NGbfX8Gv5FHx5De4mVLexWz2x-YuVpculWMqXUIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8bbd214211.mp4?token=E7aVf6MmkrQAv0IZ0dQgCfMWmKMA2cGfLkITddRZqjuv0Vkjwhe3D6rtYRqgBLJsj7bHEWVWFOSk3CK49NVMqnsxUBnRFpupeSyE-MYL2ECEmWh0ePZ-Nz1JW8NneUsWzOVTTwUZvcNCSznuKWN7Bd29Q_zbrus1GhTeq8sTPI6M_ub0eoox-ru1FUVEFzEdmYtxhRxRkRkr7GpBpSMkay1ILKar7JXdlNbSh5mtBTovF4VkxatO71_6rTMT1hFKh0KAT1pqxQE4JCAkZ-Ufy_2wsPs3ripS8jNTGSeng6w4J4NGbfX8Gv5FHx5De4mVLexWz2x-YuVpculWMqXUIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت دفاع کویت شامگاه یک‌شنبه در بیانیه‌ای اعلام کرد که سه پاسگاه مرزی زمینی در شمال این کشور هدف یک حمله «خصمانه و جنایتکارانه» قرار گرفتند که در پی آن خساراتی به تاسیسات وارد شد.
وزارت دفاع کویت افزود همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت در آب‌های سرزمینی این کشور هدف یک پهپاد مهاجم قرار گرفت. این حمله خساراتی به بار آورد و یکی از کارکنان زخمی شد. این فرد در حال دریافت خدمات درمانی است.
ستاد کل ارتش کویت نیز تاکید کرد نیروهای مسلح این کشور همچنان در آمادگی کامل قرار دارند و همه تدابیر و اقدامات لازم را برای حفظ امنیت کشور و تمامیت ارضی آن اتخاذ کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76969" target="_blank">📅 20:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76968">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4ddjD7p3hQiCOWm85cLmU4Q8wFY9dNiK1uw_iRcSurhKEcaq54h2GCvyPAUk_X4myj3SRhHQeDekI7UGlMgVKKQLy9eIOKsNWMgC0uCsLWsN5P9YxzFd3VFBJQiuZGF4Wu0bTY94wk7lagKb6zYUK59kKmQx3O8Qz7FBtEs3P04SpjnhD7VNXhhLVdM_k2j6FDjk170CiZasAJBD-cCZ9baZtFDqNPYixu5CQjAEDn-eK6xMfUnJop5HWxq0TFhEpWEBE3u9oQbuMphuwg9M_xT8B1Po0JGbfE6v4jYXREvs0xKE1MNa3ln3Dgu33iiO53nsMxjRmWWydAOg2xeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی، یکشنبه‌شب ۲۱ تیرماه، به خبرنگار آکسیوس گفت ارتش ایالات متحده چند حمله را به سامانه‌های موشکی و پدافند هوایی ایران و همچنین قایق‌های تندرو سپاه پاسداران در چند مکان در اطراف تنگه هرمز انجام داده است.
حسین امیرتیموری، فرماندار قشم، تایید کرد یکشنبه شب حدود ۱۰ پرتابه به اهداف نظامی در این جزیره اصابت کرده است
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76968" target="_blank">📅 20:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1e454bd90.mp4?token=ECXsXoHEmKu1FWMMIbtLcJKK7_206O42bYoCvjt5ohuuzMBS8Bj62TuXjSwxWAs1Qns8O9cJyhXFoRQc3NJY-PQ9XzY4LeIu0bTVZahGYQTaZxouCM0szVrN37KgVmyGjymPiUvUIdXZZLMdJXtlToJdkXjBsGX4HRw_OPiVM9FQ6rKhPppIazZZW7Q95rcHYYN4feHVi_n5z7veNvbLT_MCY706t3lyjZGMmyieh-qBwHHb5e1dpSzFgRsvozdZO-2rdkYj8tOiBDXQ6c5cR_37C6yklE2_BfaFMwOPhvkjdM3I8pAF7v9QDI9Cno7AQpCQyhLYdpYqKbZkEGu6Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1e454bd90.mp4?token=ECXsXoHEmKu1FWMMIbtLcJKK7_206O42bYoCvjt5ohuuzMBS8Bj62TuXjSwxWAs1Qns8O9cJyhXFoRQc3NJY-PQ9XzY4LeIu0bTVZahGYQTaZxouCM0szVrN37KgVmyGjymPiUvUIdXZZLMdJXtlToJdkXjBsGX4HRw_OPiVM9FQ6rKhPppIazZZW7Q95rcHYYN4feHVi_n5z7veNvbLT_MCY706t3lyjZGMmyieh-qBwHHb5e1dpSzFgRsvozdZO-2rdkYj8tOiBDXQ6c5cR_37C6yklE2_BfaFMwOPhvkjdM3I8pAF7v9QDI9Cno7AQpCQyhLYdpYqKbZkEGu6Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
همچنین اهالی منطقهٔ مسن در جنوب جزیرهٔ قشم نیز صدای چند انفجار را شنیده‌اند.
ماهیت انفجارها هنوز مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
پیش‌تر نیز برخی رسانه‌ها از وقوع انفجارهایی در کویت خبر داده بودند.
@
VahidOOnLine
🔄
ایرنا:
اصابت پرتابه در جزیزه قشم
🔹
فرماندار قشم از اصابت 10 تا 11 پرتابه دشمن از عصر امروز یکشنبه در جزیره قشم خبر داد.
🔹
حسین امیر تیموری در گفت و گو با ایرنا افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76967" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4ea69d634.mp4?token=wBQT8G_asAypbU6xH0f4GryIbiRjXAx5mbpGlJE3BrXzW-R_455dNahRg-7NMoMPJvBmp5A0hgSPd78y9-ar4tztgXFsn-txsUoz8rMA4J30J2VX9EBodGhJMVqTuMEfDMsdrDLBRqoujfBQBzm5jMBpN95wO0XqYugwOKcTkGFIQ9VZ7Fj2RrBkuGrBiPKfPdUrLOjCEoAkWioqAUzxO8ytO2wX7ShW5HSmV2PMynMulxwVQUvgL3_COYM7Xq0go9InLtsAsoxwvkK_qHFmS9wc0tl-m6jN7DVCkO4DIqMNZjBUFQLYmXbq_qXK8RT_7MYBp0uQhD45aowPMW1Ksg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4ea69d634.mp4?token=wBQT8G_asAypbU6xH0f4GryIbiRjXAx5mbpGlJE3BrXzW-R_455dNahRg-7NMoMPJvBmp5A0hgSPd78y9-ar4tztgXFsn-txsUoz8rMA4J30J2VX9EBodGhJMVqTuMEfDMsdrDLBRqoujfBQBzm5jMBpN95wO0XqYugwOKcTkGFIQ9VZ7Fj2RrBkuGrBiPKfPdUrLOjCEoAkWioqAUzxO8ytO2wX7ShW5HSmV2PMynMulxwVQUvgL3_COYM7Xq0go9InLtsAsoxwvkK_qHFmS9wc0tl-m6jN7DVCkO4DIqMNZjBUFQLYmXbq_qXK8RT_7MYBp0uQhD45aowPMW1Ksg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
شما آشکارا دور تازه‌ای از حملات را آغاز کردید؛ آن هم شبانه. ایران شب گذشته گفت تنگه هرمز بسته است. سنتکام صبح امروز اعلام کرد تنگه هرمز باز است. کدام درست است، آقای رئیس‌جمهور؟
ترامپ:
نمی‌خواهم درباره‌اش صحبت کنم، چون می‌خواهم به زندگی لیندسی گراهام ادای احترام کنم. بنابراین نمی‌خواهم درباره‌اش حرف بزنم. پیش از تماس هم این را به شما گفتم.
بله، تنگه باز است. دیشب حسابی بمبارانشان کردیم. آن‌ها آدم‌های بسیار، بسیار شرور و بیماری هستند.
تمام روز گذشته با آن‌ها جلسه داشتیم. دیروز با یک توافق عالی برای ما موافقت کردند: نه برنامه هسته‌ای، نه این و نه آن، هیچ‌چیز. از همه‌چیز دست کشیدند و بعد از آن اتاق را ترک کردند و سپس، ظرف یک ساعت، پهپادی به‌سوی یک کشتی پرتاب کردند.
گفتم: «شما بیمارید؛ آدم‌های بیماری هستید.»
بنابراین ماجرا از همین قرار است. نمی‌خواهم درباره‌اش صحبت کنم.  می‌خواهم امروز درباره یک نفر صحبت کنم: لیندسی گراهام.
NBC
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76966" target="_blank">📅 18:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc9b71e145.mp4?token=LXpwiCR6I0-d3odhJIr8em3LeLIMsFHn9vyu8swpWL1nGEdXb1yGA4I0f7sTxGHPD0WlhCCmaTcsFAJ1WFGDxp7RvoFmnVInLCU6NoR25igTMWA7l1aGyFINCxb28_w_zWc-QEZdOVDl1WPqfUKl9gGLeGv9JkDwXIIRTW8Z_LRby34YEZnQWzB26fJmHdYkMmJXtQqD0uYVQxO6f9pKKbk_HMDsjV10fUUU8J2r-e2FgL46ToRHi87ofiC_ifLSpAb4LXVn8M7M_-Gjzbo7BFMkoPhmIorkFfK8shiVeppnHDvvhA6OUww7ar68NVprsrWfF_vedrtvQykAg3YtSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc9b71e145.mp4?token=LXpwiCR6I0-d3odhJIr8em3LeLIMsFHn9vyu8swpWL1nGEdXb1yGA4I0f7sTxGHPD0WlhCCmaTcsFAJ1WFGDxp7RvoFmnVInLCU6NoR25igTMWA7l1aGyFINCxb28_w_zWc-QEZdOVDl1WPqfUKl9gGLeGv9JkDwXIIRTW8Z_LRby34YEZnQWzB26fJmHdYkMmJXtQqD0uYVQxO6f9pKKbk_HMDsjV10fUUU8J2r-e2FgL46ToRHi87ofiC_ifLSpAb4LXVn8M7M_-Gjzbo7BFMkoPhmIorkFfK8shiVeppnHDvvhA6OUww7ar68NVprsrWfF_vedrtvQykAg3YtSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
مجری:
ایران اعلام کرده تنگه هرمز را بسته است. آیا این درست است، آقای رئیس‌جمهور؟
دونالد ترامپ:
تا جایی که به ما مربوط است، باز است. درباره‌اش صحبت نکن. درباره موضوعی صحبت کن که به خاطرش از من خواستی حرف بزنم.
مجری:
باشه. از وقتی که در اختیار ما گذاشتید ممنونیم، قربان. پیش از اینکه اجازه بدهم بروید، آیا حرف پایانی دیگری هست که می‌خواهید مردم آمریکا درباره لیندسی گراهام بدانند؟
ترامپ:
نه، فکر می‌کنم بهترین لحظه‌اش دفاع او از برت کاوانا بود؛ مرد فوق‌العاده‌ای که دموکرات‌ها با او بسیار، بسیار ناعادلانه رفتار کردند.
هرگز چیزی شبیه آن ندیده‌ام. شاید بدترین رفتاری بود که تا به حال با کسی دیده‌ام. من را هم شامل می‌شود. البته، شاید نه من، اما تقریباً همه را شامل می‌شود.
با او به‌شدت ناعادلانه رفتار شد و لیندسی، همان‌طور که یادت هست، آن لحظه را رقم زد. و می‌دانی، باید به تو بگویم، جیک، فکر می‌کنم یکی از ده لحظه برتر، شاید یکی از پنج لحظه برتر تاریخ سنا بود.
نمایشی باورنکردنی بود. و آن را از ته دل انجام داد. نسبت به برت احساس عمیقی داشت و آن را از ته دل انجام داد و کل ماجرا را برگرداند.
واقعاً شگفت‌انگیز بود. آن یکی را باید دوباره پخش کنند.
مجری:
خب، می‌دانم که از روی احترام به لیندسی گراهام نمی‌خواهید درباره هیچ موضوع دیگری صحبت کنید، اما ما دوست داریم زمانی دوباره شما را داشته باشیم، چون واقعاً پرسش‌های بسیار دیگری از شما دارم، قربان.
ترامپ:
حتماً. این کار را می‌کنیم. این کار را می‌کنیم.
مجری:
از اینکه تلفنی با ما همراه شدید متشکرم.
ترامپ:
می‌خواهیم CNN را در مسیری عادی قرار دهیم و این کار را خواهیم کرد.
مجری:
خب، من همین‌جا در مسیر عادی هستم، قربان، و از وقتی که در اختیار ما گذاشتید سپاسگزارم و ممنون که تماس گرفتید.
ترامپ:
باشه. خیلی ممنون.
مجری:
بسیار متشکرم. بعد از این وقفه کوتاه برمی‌گردیم.
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76965" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxO6IGYK05IF6DNxsRpGWYZTcDeaf2XB5SP8hBbfzsxoXY7UbeCjqNw3HAnUMmD0RgPtD4kC86f9v0eUzm03V2RNjXBuDr1AM32xwvF9tax4XGsQG8FkcR6dcN3VYXTo0QJoVHBaCQXZ08IktuAbcS_Cyu4kMBSwl7xxAtpqQBJpASywBgCHXRxwrII1LFjfL0jADkas9HKMhYZg1r8-fyXvGRyZJ3MnloGxgyLOUQqd0pJxc9wW6jbggFO5G4_AjYupctvjLyQ9TCgIbkunt0vLE7mqRgLrjaBhtrnEfrlT9j9rYzwiJlktzd61sfq7XFnBVsnECQFIjTPBsC0jTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس، نهادی که به‌تازگی برای اعمال مدیریت جمهوری اسلامی ایران بر تنگه هرمز تاسیس شده است، یکشنبه ۲۱ تیرماه با انتشار بیانیه‌ای اعلام کرد تردد از این آبراه در حال حاضر امکان‌پذیر نیست.
در این بیانیه، آنچه «تحرکات غیرقانونی اخیر نیروهای نظامی ایالات متحده در منطقه» خوانده شد، علت توقف تردد عنوان شده است. این نهاد افزود پس از برقراری ثبات و آرامش، درخواست‌ها بر اساس زمان ثبت بررسی و مجوزهای لازم صادر خواهد شد.
@
VahidOOnLine
پست سنتکام، ترجمه ماشین:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه دولتی گفته است هیچ شناور خارجی‌ای نمی‌تواند بدون شناسایی، ردیابی و نظارت نیروهای ایرانی از تنگه هرمز عبور کند.
✅
واقعیت: ایران تنگه هرمز را کنترل نمی‌کند. این تنگه همچنان یک آبراه بین‌المللی است. نیروهای ایالات متحده مستقر و آماده‌اند تا همین وضعیت را حفظ کنند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76964" target="_blank">📅 17:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76963">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fcwrn0GUjHaZPWcgCyfRh9JDLC4RGslhcu19fnZzaBVyETWNn1n8mwMb0-UDDIE0wSTCHcdbigRqr9ii2hcArh7TZ5Q7-42Dw3YxxeA7x8tuMj2Bag7zz2D-qpPeAlUvmyuY8uOP8iAHSmFIzhS-uBQ2i3evwXp5OAg0R6lzJPEgCqNDQFsMXBuu_75M5SPpCQZ5SNpvNOdS8oapsafCRUSVkT3bDc5nV1pChnrSTAhgRnXQZHwVRie7PbortWvUeaAddFuG_ZyAmZ2mDdaGkt6M9_OpSmK2AZ0O3KUB1W6NUgOZS9bxFIi9JV40mH7LPW38Up6T6KgmaS7Zx08J0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی نظامی آمریکا، ترجمه ماشین:
تنگه هرمز به روی همه شناورهایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای ایالات متحده مستقر و آماده‌اند تا اطمینان حاصل کنند که آزادی کشتیرانی، با وجود تجاوزگری بی‌دلیل، آزار و اذیت، تهدیدها و اعلامیه‌های خودسرانه ایران، همچنان برقرار می‌ماند. ایران کنترل تنگه را در دست ندارد. تردد در جریان است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76963" target="_blank">📅 15:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76956">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ak1XfI999Hv9d5stxhwyNQWdV0sK_Z7ICpJm72KjFpN6ucV8FQJRVDvEtJkOrJU0mSmTPYJ4rvAIjQnVRI3zCCeUgB_Y9kiADk6_MErkQu9mrWJ10W1i559RWkquf3T4wbE06JaUmjrxRAP4TGRY2FPdKznUdCBHsm1T2oQqFUPmXTjlpCi3t35cHVSX9-H-0_59Q49UTqdaW0X125mLPLT0aiqAC0iG1CVBJFPtPXdEr8Y0Cw6Il6THEUVbk5FU7imihCXlRia9YvSzn5uBHtDzQptaxSDr4sxmC66_7VoFRaq7e7IE9mVwBFaZHNd0461YwySxdeQI25Hokgir9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vP4D_g9uHo6ewkhTx3gqSRWm-7ZlQqhuyeK9X1ZhjpY9bqGoFhcK7iXgCCO_1R3KWAW7QxeQO7c6N65JrDpN5h8g59G965DBJa0q7QDMJW8a0oVzRmsG_-Ng-2RHa6p8WaqXqfU8V82LzvJtoP_5DqxfvfSOhgCtYd51lxH6gwhKG1VC7lhSzMOAXm4-JskWElFhjS33Z37mk8pnZaRI8cROW9MDF6LrhK2_7Ay9UfCrgkz503DnKrqa7BlL9TySZLoSeyzGCxcA2ksw-KyBUgMOSnUqOd7qFUilfAXT9TipspTgmXQckMsU3ZJyN0Ry53paAzB6HwJHhQdpCRG6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GHyLIBAtlrNNA7xvCF3NCO8xOiwqAUAOoGmfw2p1OtKRAOcO4xOIiv1SRHCyNM_Hatvnkd6PyhLshDDCsq6T5gsWwgUINVU4hwl8wg-WQpsVE5xjLNmq7PWmNlTfoZ4lBzY9dLsIVQ7V77INI9sthvmlIb2R1EThporfq9njrPCt7pdH5YWLwkUYOoTCB4PmQ6Wkftzr02xxpJaNYNgH1acMFv6bOKf-uzN5hHtAgYVlV3t-JeC06Bsgx9mFrXH3kycaVU0jY2rUdCMa5rAuNbum4fpzeU3YhOW9b7akgFromi_fqRCfrQ7BkkiVT8AKg4HLcGRzHHYbdHP_ouPNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HcGBkHM6x_CNnXFyjERb62ZHDEODcnTGQJ9LAgQqT9nMLlgDJogzmJCpLyN7bQ0sQpL6OvcCo5NLrjOF1tXI9IWLwESRPTKSfJ-GpRh5xqo-bTBNZ2IWfYPMYpVmByxB71IvUCX2nd9ZUZiH6hK7FXctI4Tv98BeR0Bc5XyUY5MmJV-JNvTUGEDrYEEGgrtJJwnCOku9cKyS3u4xTNATESAjhJAa1q_3a12Hc-cnBjQajHqcDtQvXwNubrMuMPnLsqFKWuseGrDvpEZ_MdmXXfYInsr8dYW9hvOionEdtVVGYZOL8XuGEjYHMcJYCoaLOdTu3raQlZt55jR6zx7DIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CI7SDOPuh30YQBk5PViz_Pswgp5nzLI9UTpe4rIM6RObtLbPlROnsz4as1D2y3p6UmnPPb09Vm2ml5J4_y4DiGG_-WNEngMsGwZ9TCCQ86TyhaidNxyUIDT8baGMXsqecgkfBYS4kZM-1dWVQgzGvSb_mPLEe3vRlZ9jfqdBFwU4R05yEaufkoy836HopGJdFbyANhavjusDW-jbmIz_9d3dnZItUBaFvhUF3Zqumxeb53Ducbq7IqJyK9srUjgbiZwGZIMONgoHrWgD9hlDHW3lLAzdEZYod8BUg_FMqYfUw0PEWrNE2bI7YTk03vLcqsn3CWe8pPAALRrNi02gQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XDmeWeYU-V8-qAgdaP5g_TgQ7T7sbsKQxouFTaiJDrRfZO3EDVmcCUm44SE7reA5WEFQ3wcRLiVnHyWoHGsARvNGsJxYpI_dbjXmsgoJM2KSItrTXgWLI8B7FJHUxYJwcHmpKps9wzNiz1JnLyV9n5b2gkMlZlC2Bv3gjWktoy-1pgFbNFhZ9-ryxPJ5WEVSWxsqNsGvDpg7-7NuYX9l5BKZjzsAi5TKUsC7ZdAGQpK5BuBJuy10h3Ms1eGUXhDUoAtU1hENz6c-8kXFYAEMiiTmOdPxCIfmLfN0van_YKFkeL8w3GHASF7YfhNMCpWRZEn0G4illdDK1MxKC2vo_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51caf6abe5.mp4?token=PbTtp2bLTaUtq87aysZ79V0vFEaKaPbAnYh6GecEag_5JeXbZvX5Eu3-6whz2Y3NNoyyxqmiVBf4QrODt-KiJwzBmwxqhj19BhEKySVEdbsIyKTp2OKDn_sVjyghZsZc3jG4-Ayok2Esm-lCBtBtGbNgZgQ7mXgMLrGQp-nT_hrbWmXjtMEj6IPICftIXakWRoy9LwGpyok9MYyMOrdSTxlay0eTdcrxz-UZyV3khZiNbNjB6WMJMr17aeROPbaRR4QFBRsGCQm95r5Z7WV-OatjjuVvZYkfY1l7DPlqFcgHWnyMDKXABe0g8HiGZNTDFpKgcMxdONTpl7gnlhIuew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51caf6abe5.mp4?token=PbTtp2bLTaUtq87aysZ79V0vFEaKaPbAnYh6GecEag_5JeXbZvX5Eu3-6whz2Y3NNoyyxqmiVBf4QrODt-KiJwzBmwxqhj19BhEKySVEdbsIyKTp2OKDn_sVjyghZsZc3jG4-Ayok2Esm-lCBtBtGbNgZgQ7mXgMLrGQp-nT_hrbWmXjtMEj6IPICftIXakWRoy9LwGpyok9MYyMOrdSTxlay0eTdcrxz-UZyV3khZiNbNjB6WMJMr17aeROPbaRR4QFBRsGCQm95r5Z7WV-OatjjuVvZYkfY1l7DPlqFcgHWnyMDKXABe0g8HiGZNTDFpKgcMxdONTpl7gnlhIuew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران و ارتش جمهوری اسلامی بامداد یک‌شنبه ۲۱ تیر۱۴۰۵، از گسترش دامنه حملات خود به پایگاه‌ها و تاسیسات نظامی آمریکا در منطقه خبر دادند و مدعی شدند هم‌زمان اهدافی در عمان، قطر، اردن، کویت و بحرین را هدف قرار داده‌اند.
هم‌زمان گزارش‌هایی از فعال شدن سامانه‌های پدافندی، به صدا درآمدن آژیر های خطر و شنیده شدن صدای انفجار در چند کشور منطقه منتشر شد.
این حملات در حالی رخ داده که عمان و قطر طی هفته‌های گذشته نقش اصلی میانجی‌گری میان جمهوری اسلامی و آمریکا را بر عهده داشته‌اند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، یک روز پیش از این حملات در مسقط با بدر البو سعیدی، وزیر خارجه عمان، درباره کاهش تنش‌ها و سازوکار عبور امن کشتی‌ها از تنگه هرمز گفت‌وگو کرده بود. عمان همچنین پیشنهادهایی برای حفظ امنیت کشتیرانی و اجرای تفاهم‌های مربوط به تنگه هرمز ارائه داده بود.
قطر نیز در کنار پاکستان از میانجی‌های اصلی گفت‌وگوهای تهران و واشنگتن در چارچوب تفاهم‌نامه اسلام‌آباد محسوب می‌شود. با این حال، سپاه پاسداران هم‌زمان با تأکید مقام‌های جمهوری اسلامی بر ادامه مسیر دیپلماسی، بار دیگر مدعی حمله به پایگاه العدید در قطر شد و اکنون نیز از حمله به اهدافی در خاک دو کشور میانجی، عمان و قطر، خبر داده است.
@
VahidHeadline
فرماندار درود در استان لرستان روز یکشنبه ۲۱ تیرماه از برخورد بوستر (پیشران) یک موشک به یک منزل مسکونی در محله بلوار تختی این شهر خبر داد.
به گفته این مقام محلی یک واحد مسکونی و پارکینگ بر اثر این اصابت دچار خسارت شدند اما کسی بر اثر این سانحه کشته یا مجروح نشده است.
@
VahidOOnLine
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۲۱ تیرماه با انتشار پیامی در شبکه اجتماعی ایکس، درگذشت شیخ حمد بن خلیفه آل ثانی، امیر پیشین قطر، را تسلیت گفت.
عراقچی در این پیام به زبان عربی نوشت: « صمیمانه‌ترین مراتب تسلیت و همدردی خود را به امیر شیخ تمیم بن حمد آل ثانی، خاندان ارجمند آل ثانی و ملت برادر قطر ابراز می‌داریم.»
این پیام عراقچی در حالی منتشر می‌شود که بامداد روز یکشنبه، نیروهای مسلح جمهوری اسلامی، مناطقی در قطر را هدف حملات موشکی و پهپادی قرار داده بودند.
قطر یکی از میانجی‌گران کلیدی در جریان مذاکرات جمهوری اسلامی ایران با آمریکا به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76956" target="_blank">📅 15:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NsASC61Yfe-PotkH8Rq83ThuhtgnsxhS_2MH_7UG4xLkHDafNP-zmq0gxd_SojrYpahodcwJIJT13_yY_rbXQXPuQwQRjcnzSC3N3_TA1q1qO_nvUKQuYJH0ciZ8XJsuy171T64R_xPRsk__Yv1s5s3Ry4kwKjh47SF6ldcD1xauA0fgu5tiroglv09uac3hWuQnjrvLAkanHCXsmNqJGl251NLIbh6Stv35j-exG67okQYRmzXXth4lZg9N0eyH8LWLqJEX1Qw5A0eweVXIILdS_KVJP_IWgJpHgqMEI_4wH7GCwakD3F1hsHr9OQFxX6pn_f4IsC5nYxVXss3lDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bYnRo0ZfgLlVvpo6-QG-xn-uij5T1DF2eWunt3nlFO94-MvbiwLKIEOJfGFUyv-JZOy8pvRDchJ4Z6iB0rloVv4fXJU_mt0rvuoENDoZFkcMhHypPWvF9_Vjhvv5i7CkviAorzDJl8N3f_Hgs-9T0ycxQSVEfSduCxc1Ek9L_wkaTn6bPWLgJ7d_idPpUzJ0Jr0SRFXVNEGS-UNdcpZkfL4FKJbZ4GBfGFn_bwvVp-9MVgRGyNkODfEDncFSSaml8YZdxBcRheJrHJVMWLLamhdNAx5MDx7HnRIxKS6sM2-Oimmj1ZC34YhmrgBSsvjUFXXIRI8p7jYqXX6riismAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون امنیتی و انتظامی استاندار کرمان روز یکشنبه ۲۱ تیر اعلام کرد ارتش آمریکا یک دکل ارتباطی در ارتفاعات جنوب این استان را هدف قرار داده است.
به گزارش خبرگزاری مهر، بر اثر این حمله دو نفر مجروج و با هلی‌کوپتر به مراکز درمانی منتقل شدند.
@
VahidOOnLine
معاون سیاسی، امنیتی و اجتماعی استاندار لرستان، اعلام کرد شهر ویسیان از توابع شهرستان چگنی در استان لرستان، صبح یکشنبه ۲۱ تیرماه، دو بار هدف حمله هوایی قرار گرفته است.
سعید پورعلی گفت این حمله تلفات جانی نداشته و شرایط در این شهر هم‌اکنون عادی است.
پیشتر و در پی حملات نیروهای آمریکایی به استان‌های جنوبی ایران، معاون امنیتی استانداری خوزستان، از اصابت «پرتابه‌های دشمن» به مناطقی در شهرستان‌های هندیجان، ماهشهر و آبادان خبر داده بود.
شنیده شدن صدای انفجارهایی در بوشهر، بندرعباس، سیریک، عسلویه، کنگان و بندر نیز از گزارش‌های مربوط به تحرکات جنگی بامداد یکشنبه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76954" target="_blank">📅 15:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76953">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CetLlqouxqHkrxTwPwjhQA3ObfzxQjb3eCx5NgWZMD2Ps5Rw_VAbD2lUanfItGfF9z8MU1Ti6lh0CYvWFIvtZ5paQBhwnPeX_WvuWQqDuk62Zu1v1WDD-30Bwe4OzxhL20LQQAb89euU6O7HVJ69ooDpBoAaibO_AqE2yWP65I4JkJ3jtcdXg6rliYDryzP9pvMySMq-5RcDoPUg_ZFI6O7Ur5DlMECjZXsuH2R9L7h04zZImZ65nd0_I9-r4V9HtpqzJJqHxebPo6Sn75NScum41wDSkiJuajFP96uZVSeDyn57leTSbr7719kOpxy8FK-Ep2gQgztzCQA5BYlu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیندسی گراهام، سناتور ارشد جمهوری‌خواه ایالت کارولینای جنوبی و از نزدیک‌ترین متحدان دونالد ترامپ، شامگاه شنبه ۲۰ تیر۱۴۰۵، در ۷۱ سالگی پس از یک دوره کوتاه بیماری درگذشت.
دفتر این سناتور با انتشار بیانیه‌ای اعلام کرد که گراهام شامگاه شنبه در گذشته و خانواده او از مردم خواسته‌اند در این دوران دشوار، ضمن دعا برای آنان، حریم خصوصی‌شان را نیز رعایت کنند.
گراهام یکی از شناخته‌شده‌ترین چهره‌های جریان محافظه‌کار آمریکا و از اعضای باسابقه مجلس سنای این کشور بود.
او طی سال‌های گذشته به‌ویژه در حوزه سیاست خارجی، از نزدیک‌ترین هم‌پیمانان دونالد ترامپ محسوب می‌شد و مواضعی تند علیه جمهوری اسلامی اتخاذ می‌کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76953" target="_blank">📅 15:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76952">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eWzM-yEqPmgIUs1U-GTv_M0nxYy6rRP5SclDOib09NWTp902gmXchtewrLI-X-GdCRhTZ18IHVophsHeq9LFMOAQcg4GXYcr0vUiOS_8BHTf-APweEQrKO0DODq6EpJtpTt0JjZ9PEXfduMvuyfw5XD9w2BwrM14RezBzhMnlOiDmETnEhETOWgOQDSykTiD8riLl1pM1dkhF_iMadaGKzPmR2JJqY083na8xIt9WUjVRg5uruw3f1tWDesOvWZK3b13PW3tH_wYFl4zsGXyuHwXJQNqD2pTNvZq3TuvH-L05X09Ku0zU2zZqO-3tJcfg32ajlxcXqt3QQ9buiMjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۱۲ حکم اعدام در پرونده "میدان علیخانی اصفهان" به مرحله اجرای احکام رسید
🔹️
بر اساس گزارش‌های منتشرشده و اطلاعاتی که به کمیته رسید، پرونده موسوم به «میدان علیخانی اصفهان» وارد مرحله اجرای احکام شده و جان ۱۲ زندانی در معرض خطر جدی اجرای حکم اعدام قرار دارد. گزارش‌ها حاکی از آن است که احکام پس از تأیید در دیوان عالی کشور در روز ۱۴ تیر، به اجرای احکام دادگاه انقلاب اصفهان ارسال شده‌اند.
🔹️
این پرونده به وقایع ۱۸ دی‌ماه ۱۴۰۴ در محدوده میدان علیخانی، میان ملک‌شهر و کاوه اصفهان، بازمی‌گردد؛ جایی که مقام‌های جمهوری اسلامی اعلام کردند چهار نیروی بسیج و یگان ویژه به نام‌های حسین رمضانی، محمد همتی، سید علی خشوعی و ولی‌الله صفری کشته‌ شده‌اند. در پی این رخداد، ۵۹ نفر بازداشت شدند و برای آنان پرونده‌ای گسترده تشکیل شد.
🔹️
بر اساس اطلاعات منتشرشده، رسیدگی به این پرونده در شعبه اول دادگاه انقلاب اصفهان به ریاست محمد براتی درچه و محمد توکلی (معروف به وکیلی، از قضات پرونده «خانه اصفهان») انجام شده و دادستان پرونده محمد نخجوان بوده است. همچنین گزارش شده که کل روند دادرسی تنها در سه جلسه یک‌ساعته برگزار شده است؛ موضوعی که نگرانی‌های جدی درباره رعایت اصول دادرسی عادلانه را افزایش داده است.
در میان ۵۹ متهم این پرونده، ۲۳ نفر با وجود تبرئه از برخی اتهامات، همچنان به احکام ۵ تا ۱۰ سال زندان محکوم شده‌اند.
🔹️
در مقابل، ۱۲ نفر با حکم اعدام روبه‌رو شده‌اند که در میان آنان چندین نوجوان و یک شهروند افغانستان نیز دیده می‌شود.
اسامی محکومان به اعدام عبارت‌اند از:
علیرضا سپاهی (متولد ۱۳۸۰) – محکوم به چهار بار اعدام
ابوالفضل سپاهی (متولد ۱۳۸۲) – محکوم به سه بار اعدام
علیرضا رئیسی (متولد ۱۳۸۳) – محکوم به دو بار اعدام
قائم حسینی (متولد ۱۳۸۴) – محکوم به دو بار اعدام
گل‌محمد محمدی (متولد ۱۳۸۱)، شهروند افغانستان که بنا بر گزارش‌ها به معترضان پناه داده بود – محکوم به دو بار اعدام
امیرحسین صفری (متولد ۱۳۷۷) – محکوم به اعدام
امیرحسین ملکی (متولد ۱۳۸۵) – محکوم به اعدام
علی دشتی (متولد ۱۳۸۵) – محکوم به اعدام
امیرحسین ابراهیمی انالوجه (متولد ۱۳۸۵) – محکوم به اعدام
شروین باقریان (متولد ۱۳۸۶) – محکوم به اعدام
عرفان اسفندیاری (متولد ۱۳۸۶) – محکوم به اعدام
ابوالفضل ابراهیمی (متولد ۱۳۸۶) – محکوم به اعدام
🔹️
همزمان، گزارش‌ها یادآوری می‌کنند که در روزهای ۱۸ و ۱۹ دی‌ماه در همین محدوده، شماری از شهروندان اصفهان در جریان اعتراضات با شلیک مستقیم نیروهای حکومتی جان خود را از دست دادند.
🔹️
نام محمد توکلی نیز در این پرونده بار دیگر مطرح شده است؛ قاضی‌ای که پیش‌تر در پرونده «خانه اصفهان» نیز حضور داشت؛ پرونده‌ای که به اعدام مجید کاظمی، صالح میرهاشمی و سعید یعقوبی انجامید و همچنان از پرونده‌های بحث‌برانگیز سال‌های اخیر به شمار می‌رود.
🔹️
با توجه به گزارش‌های منتشرشده درباره تأیید احکام در دیوان عالی کشور و ارسال پرونده به اجرای احکام، نگرانی‌ها نسبت به احتمال اجرای قریب‌الوقوع این احکام افزایش یافته است.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76952" target="_blank">📅 15:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ea07cb43fd.mp4?token=baTW-dAWusqx2Ld88IM4gnnlxcPJaS00TSUNsrcZQcX5FXuFkdJbswPGEPAaEc0ReYI6SI8XxlW5Di4SRVF1P50YbShfo_kPWVecgLhXhdxdXE1yACOUkQjSVXysMc15CyDPK-nu3w2fO5YT7nsgv6dvG445JBZfWKtnT5giRCR3fHMJbjvEM1OJLSX8DODV6_O6y_q5K-RPXOct3mKs9RfoM7fzDCX3xDPiS9L0ncd3hse0_hYinaKmneKk1B1F0HlyZkpJe-ETOIC3ziXZXbFhnP0kQ3mcdT1YdcHxzIK98d6prn7cshp07TtKlpE8WPuwvJx4tZlPM1g3NnslUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ea07cb43fd.mp4?token=baTW-dAWusqx2Ld88IM4gnnlxcPJaS00TSUNsrcZQcX5FXuFkdJbswPGEPAaEc0ReYI6SI8XxlW5Di4SRVF1P50YbShfo_kPWVecgLhXhdxdXE1yACOUkQjSVXysMc15CyDPK-nu3w2fO5YT7nsgv6dvG445JBZfWKtnT5giRCR3fHMJbjvEM1OJLSX8DODV6_O6y_q5K-RPXOct3mKs9RfoM7fzDCX3xDPiS9L0ncd3hse0_hYinaKmneKk1B1F0HlyZkpJe-ETOIC3ziXZXbFhnP0kQ3mcdT1YdcHxzIK98d6prn7cshp07TtKlpE8WPuwvJx4tZlPM1g3NnslUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام:‌ حدود ۱۴۰ هدف نظامی ایران را مورد اصابت قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) روز ۱۱ ژوئیه سومین دور حملات این هفته علیه ایران را به پایان رساند تا نیروهای ایرانی را بابت حمله به یک کشتی تجاری دیگر در تنگه هرمز پاسخ‌گو کند.
نیروهای آمریکایی با استفاده از مهمات نقطه‌زن شلیک‌شده از جنگنده‌های مستقر در خشکی و دریا، پهپادها و شناورهای نیروی دریایی، حدود ۱۴۰ هدف نظامی ایران را مورد اصابت قرار دادند. این اهداف شامل سایت‌های موشکی و پهپادی ایران، توانمندی‌های دریایی، تأسیسات ذخیره مهمات، شبکه‌های ارتباطی و مراکز پایش ساحلی بود.
سنتکام طی سه شب حملات این هفته، به دستور فرمانده کل قوا بیش از ۳۰۰ هدف را مورد اصابت قرار داده است تا توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تضعیف شود. عبور کشتی‌های تجاری از این کریدور حیاتی دریایی بین‌المللی همچنان ادامه دارد.
از اوایل ماه مه تاکنون، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۴۰۰ میلیون بشکه نفت خام از تنگه هرمز کمک کرده‌اند.
CENTCOM
منابع حکومتی:
دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز تعمیرات و نگهداری جنگنده‌ها و مرکز فرماندهی و کنترل  ین پایگاه در هم کوبیده شد
روابط عمومی سپاه پاسداران انقلاب اسلامی اعلام کرد:
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ
🔹
در پاسخ به ادامه تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در تنگه هرمز، پایگاه هوایی راهبردی آمریکا در العدید قطر در مرحله دوم عملیات مقابله به مثل هدف موشک‌های بالستیک قرار گرفت و مرکز تعمیرات و نگهداری جنگنده‌های و مرکز فرماندهی این پایگاه در هم کوبیده شد.
🔹
دشمن امریکایی - صهیونی بداند، استمرار تجاوزات او پاسخ‌های کوبنده‌تر را در بر خواهد داشت.
بجنگ تا بجنگیم.
روابط عمومی سپاه پاسداران انقلاب اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/76951" target="_blank">📅 07:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76949">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dnOmRQ9QsdsuexiuNBFGd7N6FSgf3a7Nbec1ioz-qZ1hRgvfAIfe7_GYga4NhGo_yJfQb5KJJF4Uq7Azwm6jccixdr-liVvhQz58nYzx2TdQ7uKSWbHNPPxfpcGPooQ9QOF461BDbMWk8RnXuXjn4exJaE9i0gk3JokahyBIttuTnS6-Y2dePVyZfcZM5N4vEojEVHOlOlVrHpWk3HUo_VaxfmOGQKLY4aEZUBm9-DaY9kQjcjzyJtEGbooN_0TmBFdTTIVXBDAm39GAONKrRUJVOr1kA4vWt7FXvvbra5shgw7Qqc6fLgTer6R0x35jaN-KuHCA06upnFM6ijY6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از شاهدان عینی، خبر از شنیده شدن صدای انفجار در دوحه، پایتخت قطر خبر داد.
پیش از این، وزارت کشور امارات متحده عربی با انتشار هشداری فوری، صبح شنبه، اعلام کرد که سیستم‌های پدافند هوایی این کشور در حال حاضر در حال مقابله با یک «تهدید موشکی» هستند.
همزمان وزارت کشور بحرین نیز اعلام کرد که آژیرهای خطر در این کشور، صبح یکشنبه، به صدا درآمده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76949" target="_blank">📅 06:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb22334a3e.mov?token=iqTWp5PiUlC2FlruiZhjaNoFtqLsNp98Uih7Xd5RPSFCHR0fToFyyifkCDtuyLX1nv-wT5WQEBpB-6WvzcWMLYbtAdrKeFTHbbSDYcHwVkWcgN34W3ZuAdDEqOgC61rk8Clplgm31q8UWcBppFv8K0BDgkdxnLNzlKDmLRap6XcshhabMoj9zknopG6kgbStNV5kNV8-E2afLkrrGrZymCiEpfUj-7NoHpOPFHVpgIlnxE8fEHba85RtyMmfJtEVMnO43OP9xWzCP1cB8ZUpDBTP9F9azZCF7SsWduCJTm9q30NfmXLC5UmbvF9hE-Os2dFye6PiQxeEW4931xOR1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb22334a3e.mov?token=iqTWp5PiUlC2FlruiZhjaNoFtqLsNp98Uih7Xd5RPSFCHR0fToFyyifkCDtuyLX1nv-wT5WQEBpB-6WvzcWMLYbtAdrKeFTHbbSDYcHwVkWcgN34W3ZuAdDEqOgC61rk8Clplgm31q8UWcBppFv8K0BDgkdxnLNzlKDmLRap6XcshhabMoj9zknopG6kgbStNV5kNV8-E2afLkrrGrZymCiEpfUj-7NoHpOPFHVpgIlnxE8fEHba85RtyMmfJtEVMnO43OP9xWzCP1cB8ZUpDBTP9F9azZCF7SsWduCJTm9q30NfmXLC5UmbvF9hE-Os2dFye6PiQxeEW4931xOR1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی (به همراه تصاویر مختلفی از رد دو موشک):
همین الان از خمین دوتا موشک شلیک شد
درود وحید جان همین الان از خمین دو تا موشک شلیک شد
سلام،،ساعت ۵ نی دوتا موشک از الیگودرز شلیک شد
زنجان
۲۱ تیر ۱۴۰۵ ساعت ۵:۳۲
صدای بلند و ممتدی هم اومد برای چند ثانیه
وحید این دفعه هم از سمت خمین و الیگودرز شلیک کردن صداش زیاد بود ولی ۲ تا رد موشک بیشتر نمیبینم.
شلیک موشک از خمین
درود وحید جان از حدود زنجان موشک بلند شد دوتا
🔄
شهرستان داراب استان فارس ساعت ۶ شلیک ۲ موشک
یه موشک از داراب فارس بلند شد رفت ساعت 6:05 دقیقه
همزمان:
آژیر در بحرین
sirens in bahrain
5 دقیقه پیش قطر صدای پدافند اومد و آلارم روی گوشیا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/76947" target="_blank">📅 05:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JnDNlkbkybiDAujkGUwlk8s-Ab7Ftqu3JLh1u3ZpujZy8uTYMpQssx7vGsuaZVp1wdiA22V_tpiv8ka1oSaB0zDRXUMEbaJVZzpKLgz8SaTOdytNMk1mlavPU-uHJ02QRf2VQFepCsF3QgVtEAiotTva8NQksUt9wk6s3badfjhjobf6tbPM4cWLvB3mw9GZjbYMwmZujHPiy6s8fg9khXSv9NG8MQloHiV8Kk9f8EMlw_UU7Jv9YGEF-5ZL__naHGpBPb2dxSPqQXb_KPoLN7Nf5f_6TeNR-bPZ8rsX15a9AiUWY5SsVtvG1LxTfBFsPpAuLr3TNUyUfBA7NWYKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی استانداری خوزستان گفته است که شهرستان‌های هندیجان، ماهشهر و آبادان هدف پرتابه‌هایی قرار گرفته‌اند.
هنوز جزئیاتی درباره محل دقیق اصابت، خسارات و تلفات احتمالی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76946" target="_blank">📅 05:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YfTAJ17iDaYEiVz9QRPxTiw4JLQGPCmmrGOMDkcF4JWsz_Udj52zLd1rlpphis9XiEJNnxLhchYH_eq8RFR6OWevqIquLdONHYpaYnJiZi1fp-eqFpgkFZBIlBAK7A9k-3Dz4A59m-lLOIKqVTy8VIrsZr-dPI-IdsSCiqViveWYxR7_cS4UDMPDZWxPD-T5XJcKcRrxdw7V9P71xbMKJXRYCSrFSEaz6uv_TLvLKcGXYbJcHEa27XLt9kMIiWV6XbP4N7mo3k_FP2j8I1DsbxJBoEy5eYLzLZR27UDsULpK6eDJ9mllqd2XbA-0VOvFG2V5LSOX1utf-Icdr2KmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر و پیام‌های دریافتی تایید نشده:
سلام باز بوشهرو زدن ۳:۴۶
سلام وحید جان بوشهر سمت سرتل رادار زدن
بوشهر همین الان 3:48 دقیقه دو بار لرزید
سلام وحید جان ۳:۴۷ دقیقه بوشهر سه تا انفجار شدید شنیدیم
اقای وحید ساعت ۳ وربع صدای انفجار شدید اومد عسلویه از خواب پریدم
صدای دوتا انفجار  الان اومد  پایگاه هوایی بوشهر
۵ تا زد سایت موشکی چغادک-بوشهر،۰۳:۴۵
سلام وحید جان
ساعت 03:47
بوشهر سه چاربار صدای انفجار اومد
سلام وحید جان الان 3:45 دقیقه بهمنی بوشهر صدا اومد دو سه تا که خونه لرزید
🔄
جاسک
وحید ۳:۵۰ جاسک رو زد ۳ بار
سلام وحید جان همین الان دو انفجار وحشتناک در جاسک
منطقه نیرو دریایی جاسک
3:50 صدای جنگنده و چندین انفجار از بندر جاسک
سلام وحید صدای چند انفجار شدید در بندر جاسک
🔄
جاسک
خدایا بازم داره میزنه
دوتا دقیقا همون نقطه قبلی زد
ساعت ۵ جاسک
۲ انفجار دیگه جاسک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76945" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dIzpjJoqy_IeagPeQOSH8yeHs77CK1_bBb1Z_ESV22XdW4IY0NU6BKQTF4T_n1gHc5TccTSQiQcKAQwLn4-G7Kmf_GdJS7Kc6JKcunzXBsK8V0VIMKIfRgg2m_iix7v7KVC4LU3i7D-OMDT4_ObsHE1qsW11Vnrx7aCLwxOs5wTo8fXHNc68JNXdFPiJFbHmk3FJE873Zbh3ZgRrI44gb587wDk9NO0pi6tPKiuttGgG_fDhuUnBgSf27cEPU7WPJXENAnq6CXPJZ1gMpnsj2YkOBj7ulFiUqLOIqxo5OzlIdhekB0TJzkemPkX-GsDE6NLcvtTk6JQmrBhqpmE-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا:
"ایران انتخاب بدی کرد. حالا تاوانش را می‌دهد."
PeteHegseth
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76944" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پیام‌‌های دریافتی:
دوتا سنگین زد کنارک همین الان  ۳:۱۸
چابهار الان دو دفعه صدای انفجار اومد
سلام وحید جان چابهار همین الان دو تا انفجار مهیب
ساعت ۳:۱۸ دقیقه دو انفجار با صدای بلند در کنارک
همین الان ساعت 3:30 دو انفجار شدید در جابهار و یکی هم صداش خیلی دور بود شاید اطراف فرودگاه کنارک. ولی دو انفجار چابهار واقعا شدید بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76943" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76942">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سنتکام: سومین دور حملات این هفته علیه ایران را آغاز کردیم
ترجمه ماشین:
امروز ساعت ۷:۱۵ عصر به وقت شرق آمریکا، [۲:۱۵ بامداد شنبه تهران] نیروهای فرماندهی مرکزی ایالات متحده پس از آنکه نیروهای سپاه پاسداران انقلاب اسلامی به‌طور آشکار به کشتی کانتینری «M/V GFS Galaxy» با پرچم قبرس در حال عبور از تنگه هرمز حمله کردند، سومین دور حملات این هفته علیه ایران را آغاز کردند.
یکی از اعضای غیرنظامی خدمه مفقود شده و کشتی به‌دلیل آتش‌سوزی در داخل و وارد آمدن خسارت قابل‌توجه به موتورخانه، قادر به ادامه سفر نیست.
پس از آنکه ایران به‌دلیل حملات پیشین به کشتی‌های تجاری پاسخگو شناخته شد، بار دیگر فرصتی به این کشور داده شد تا پایبندی خود به تفاهم‌نامه را نشان دهد، اما بار دیگر ناکام ماند.
در پاسخ، ایالات متحده با ادامه تضعیف توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، هزینه سنگینی به این کشور تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می‌شوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76942" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pNQivVnF8W0kKb6KQg5Ljz0y7JcDXD7QWkYRJHJb067jm1CzcCvW-9Zw2nT3gt628W6jTykOcNDNi95ilvEQMsmd0ZAzlIjMOlbCm0_p5DgZ8ygK-6ssvtcd0EC_7WhHOBgNX-evI8C7iNMZ8jOeycwjhf2I19uUFMdud1OXG43QbBItWIBmRIQFL7RETad0pCit8ZXX0ZQJGLOEOCDt19_VP0NhuGOuXlKUBbErmDoWXKj-VDo6GnD8OOkS1Nkm3xRsErhMBBw67Wb_cfgq9IauEs2ui1xSa7JDKaGj6EWiSLjY6gorPZD6jyEDzcwvnE-GDoS4XMO5x7H5WhEUDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
‌
بوشهر صدای چند انفجار لرزش زمین احساس شد زیرپام
صدای دو تا انفجار بندر دیر ساعت ۲:۴۶
۲۱ تیر
سلام
ساعت ۲:۴۰ شنيده شدن چهار تا پنج انفجار در کنگان و حوالی آن
وحیدجان
الان حدود دو و چهل و پنج دقیقه صدای چهار پنج انفجار بزرگ توی بوشهر
شبشه های خونه لرزید
وحیدجان سمت نیروگاهه
من تنگک هستم الان دود و نور قرمز از اون سمت می بینم
سلام اقا وحید ساعت ۲:۴۵ بندر کنگان چهارتا صدای انفجار اومد
سلام ساعت ۲ و ۵۰ دقیقه بوشهر صدای چندین انفجار
۲:۵۰ بوشهر صدا انفجار
صدای چند انفجار اومد در بندرکنگان
سلام.ساعت ۲/۴۵ دقیقه شهرستان دیر استان بوشهر.صدای دو انفجار مهیب با فاصله یک دقیقه از هم شنیده شد.موجش شدید بود
سلام وحید
بندر دیر رو زدن ساعت ۲:۴۶
تو جنک هم ۱۰ ۱۲ باری زد یا بیشتر یادم نیست الان
اسکله نیرو دریایی زدن
🔄
همین الان ستا انفجار دیگهههههه.
بندر دیر.
وحید جان الان ساعت ۲:۵۶ باز دوتا بمب دیگه بندر دیر رو زدن
۲:۵۵ بازم زدن بندر دیر رو
دو بار دیگه ۲:۵۶ زدن
کنگان همین الان دوتا صدای بزرگ انفجار اومد۲:۵۶
کنگان رو دوباره زدن
🔄
تایید نشده:
صدای انفجار شدید بندرعباس
همین الان قشم صدای یه انفجار مهیب اومد
دقیقا ساعت ۳
ساعت ۳:۱ بندرعباس صدای دو انفجار پشت هم اومد
صدای انفجار، سیریک.
🔄
استان بوشهر
سلام وحید جان بندر بوالخیر  رو زدن
سلام اقا وحید بندر بوالخیرو زدن
🔄
عسلویه بوشهر
یکی که در واکنش به خبر  قبلی درباره عسلویه پیام داده بود: "ببین ۱۰ دیقه پیش صدا اومد ولی نزدیک نبود" الان پیام داده که:
وحید اینجارو دارن میزنن
همین الان صدا و لرزش خونه ۱۰ تا انفجار
عسلویه
پیامی دیگر:
عسلویه
حدود یک ساعته نه یا ده صدای انفجار اومد که دوتای اخری خیلی شدیدتر بود
ولی منطقه پتروشیمی و پالایشگاه خداروشکر خبری نیست
همه‌ی صداها از  سمت ساحل حاله و ساحل بنود یا بندر تین هستن
تقریباً بین۱۰تا ۲۰ کیلومتر با عسلویه فاصله دارن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76941" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76940">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DAS08lLYtLXpAzDe9Cna-Iq1j3RGEJAzWPaMx18q2Qgekg7Clj3SHZMIQPm0pkAIu7EIMZ2168mTjy8jSqvF9z_lw_DAhCyM0s0h1uSKom3rpk6RJpRhx_Cw-uTRrurPutD0zgGDouk-tOLPPPxfVXqH82I0mPcrotIXfY67lwVhdu45fp9o4gX6nZBgMymbZSrDrwro1WWaaAAuNmS8g0pIHsyKgcmAPYgsAKPsfUywFq2rvFEkKm0ed3kQDbMLFqWaTDIYPYsM8XhhE0pn5r6LTkYtwSdpkRFbpa25Cd2trBzxawyY-bG94HLM-NLn3F6CzNevyh6Z4jhw_2ojVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با بیانیه سپاه پاسداران مبنی بر «بسته بودن تنگه هرمز تا اطلاع ثانوی و پایان مداخلات آمریکا»، یک مقام آمریکایی در گفتگو با خبرنگار آکسیوس اعلام کرد که سپاه یک موشک به سمت یک کشتی باری تجاری که قصد عبور از تنگه هرمز را داشت، شلیک کرده است.
به گفته این مقام، کشتی مذکور مورد اصابت قرار گرفته و دچار خسارت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76940" target="_blank">📅 02:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ReXtI1p6e_qe9_PhPBHIWsrkpzeeG06jameBRkJ5v4LZrv6g_QQz3JgJjNu2TYSe4M8PR73tLho6DGUe7CTyuDbs48zmP_f13Hq60ElgT4ZQvYkX8yXthy0WFFxX2RDcvD0GpMLV4j88VhYikYGKfAnVFlTb2XABAX4bIbXNaxMzXm9O-NJF56aFugKj_Pb8EDuQSssyFvyp8sL3ZVK86MNM_mHiVYw2GRVV9B67Yb-3RDm1bXKJMMUMltI65hbdbfD08npN_hJhgtUlditnk6RVjDAAMuBqOJtdChH9i6Bpbx8KOJLwZBjzGAjV4sExmE6un0RDto7cxw0uZOsQfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: یک کشتی را هدف قرار دادیم / تنگه هرمز تا اطلاع ثانوی بسته شد
ایرنا:
نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
بسم الله قاصم الجبارین
در اطلاعیه قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.
🔹
ساعاتی قبل، این تذکرات نادیده گرفته شد و با تحریک بیگانگان چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
🔹
به ناچار یک فروند کشتی‌ که با خاموش کردن سامانه‌های خود امنیت دریایی را به مخاطره افکنده بود؛ مورد اصابت شلیک‌اخطار واقع و متوقف شد.
🔹
به دنبال این حادثه، اولا با توجه به بروز این ناامنی به سبب مداخله غیرقانونی بیگانگان، تنگه هرمز تا اطلاع ثانوی و تا پایان مداخلات آمریکا در این منطقه بسته و هیچ شناوری اجازه تردد نخواهد داشت، ثانیا اگر دشمن متجاوز به بهانه این حادثه که خود، مسبب آن بوده است، خطایی کند و تجاوز جدیدی علیه ما داشته باشد با شدت پاسخ داده خواهد شد و پایگاه های جدیدی از دشمن در منطقه مورد هدف قرار خواهد گرفت.
🔹
عواقب چنین مداخله‌ای بر عهده دشمن آمریکایی - صهیونی و کشورهایی است که خاک خود را برای این تهدیدات در اختیار پایگاه دشمن گذاشته‌اند.
و ما النصر الا من عند الله العزیز الحکیم
نیروی دریایی سپاه پاسداران انقلاب اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76939" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76938">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرنگار اکسیوس:
‏
🇴🇲
🇮🇷
یک دیپلمات که در جریان مذاکرات قرار گرفته است گفت عمان در گفت‌وگوهای امروز مسقط پیشنهاد کرد که مسیر جنوبی در آب‌های عمان و مسیر شمالی در آب‌های ایران، هر دو به‌طور کامل فعال باشند.
‏
🇴🇲
🇮🇷
این دیپلمات گفت طبق پیشنهاد عمان، مسیر جنوبی بدون هیچ‌گونه الزام برای دریافت مجوز باز خواهد بود؛ همان‌طور که پیش از جنگ بود.
‏
🇮🇷
🇴🇲
این دیپلمات گفت ایرانی‌ها نتوانستند این پیشنهاد را در جلسه به تصویب برسانند و ناچار شدند آن را برای گفت‌وگوهای داخلی به تهران ببرند.
BarakRavid
سی‌ان‌ان:
یک منبع آگاه از مذاکرات به سی‌ان‌ان گفت عمان پیشنهادی را برای مدیریت تردد در تنگه هرمز از طریق دو مسیر با کنترل جداگانه تدوین کرده است.
بر اساس این توافق که هنوز نهایی نشده است، هر دو کریدور باز خواهند ماند. کریدور جنوبی که از آب‌های سرزمینی عمان عبور می‌کند، امکان کشتیرانی آزاد را مطابق شرایط پیش از جنگ فراهم خواهد کرد.
کشتی‌هایی که از کریدور شمالی، در آب‌های سرزمینی ایران، عبور می‌کنند، باید از ایران مجوز قبلی دریافت کنند؛ با این حال، طبق این توافق هیچ عوارضی از آن‌ها دریافت نخواهد شد.
CNN
علی قلهکی
:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/76938" target="_blank">📅 22:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hgAxllljWi-aza55dK5rDG7SwatVu8C6GZdfpVEg8rTZc2LY7AEc-yc9ZET0YpKWeEJSVD8l4s2_WR1mTFUVIX1e6AOAGZYaHBE32HURzmPpy3jw6VZRIgSpY5U1n_kd_-YqLt2cDC20-mpBwgrLMrLXgU8O5ul87AO22OdiHUAjbFqdYwL3FYfTKtMxsRx-no2goeyQ18M_eZK3yRS8jtKTZKAGF1G0IVwsZMT96hlx4212wqHwTyWtOqFEdB7gKZvrtBOyHE-rjo28j-tUawKzy8tgwD8rXGsT2oQZ9DXFd0t99_I91R73sHGgBeCYil2dIbhElbusZQqCHUvSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ایسنا، طی روزهای گذشته پیش بینی شده بود گرمای هوا تا هفته منتهی به دوم مردادماه با میانگین دمای بالاتر از ۳۹.۷ درجه تداوم خواهد داشت، از این رو تمامی سناریوهای بهره‌برداری شبکه بر مبنای نیاز مصرف ۷۵ هزار و ۵۰۰ مگاوات طراحی شده و مرکز ملی راهبری شبکه برق کشور و واحدهای عملیاتی صنعت برق در آماده‌باش کامل قرار دارند با این وجود بنا به گفته مسوولان شرکت توانیر  هیچ محدودیتی در تامین برق بخش خانگی اعمال نخواهد شد.
اما امروز  ۲۰ تیرماه برخی کاربران ایسنا [و بسیاری از دنبال‌کنندگان اینجا] طی تماسی عنوان کردند که در برخی مناطق  همچون محدوده ولیعصر، مطهری و قائم‌مقام فراهانی [و مناطقی دیگر و شهرهایی دیگر] با قطعی برق چهار ساعته مواجه شدند و با وجود پیگیری‌های ایسنا از شرکت توزیع نیروی برق تهران بزرگ تاکنون علت این خاموشی‌ها اعلام نشده است.
به گفته مشترکان همزمان، حجم بالای تماس‌های شهروندان با سامانه فوریت‌های برق ۱۲۱ موجب شده زمان انتظار برای ارتباط با اپراتور در برخی موارد به حدود نیم ساعت برسد.
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76937" target="_blank">📅 17:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76936">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qmSFsatqS1FGl_rPxy9lu2eqR9j0iLnJ5cVr5eOtyWYU-96oENx307_fOiTk7eVFY46ndeXhKpdvnCDW3_Sc2msRHYqVzRKbWXbOMTgbC9P03jFD_LMsZPPBc5U0LDo-vHlG5Q2jxPTXjg9DJ8NTnUGJLaVJwhE0d7QsMwtWSiR0puSq0fyifDazv3vbi7GuPr0VIw9QJCsW-scgkifWO_9Fd8p6-wCTXaH9-Ev-9ZjZIneExhnnBZn-MtQ0nginWAZHPemW9pXX4xiAknRlSUJ7u97XU60atT0KoQSLdlJSb7ll3ggbCbOge7b3BkwG5JVdUbgNm6CRBmgtxbFUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه امام رضا اعلام کرد دو نیروی بسیجی به نام‌های «سید سجاد علوی» و «مهدی هنرمند» در حوالی میدان سرافرازان مشهد هدف تیراندازی قرار گرفتند و کشته شدند.
بر اساس اطلاعیه سپاه، این دو بسیجی در زمان وقوع حادثه در حال گشت‌زنی در محدوده بلوار سرافرازان، در فاصله حدود ۱۵ کیلومتری حرم امام رضا، بودند. این حادثه همزمان با برگزاری مراسم تشییع و تدفین علی خامنه‌ای در مشهد رخ داد.
سپاه امام رضا اعلام کرده است که این نیروها در چارچوب مأموریت‌های تأمین امنیت مراسم تشییع و خاکسپاری علی خامنه‌ای در منطقه حضور داشتند.
در این حادثه همچنین یک عابر پیاده مجروح شد و به بیمارستان انتقال یافت.
اعلام کشته شدن این دو بسیجی در حالی صورت می‌گیرد که امیرالله شمقدری، معاون امنیتی [دروغگوی] استانداری خراسان رضوی، جمعه ۱۹ تیرماه
گفته بود
تیراندازی در بلوار سرافرازان مشهد «اقدامی تروریستی» نبوده و ریشه در یک «درگیری شخصی» داشته است.
خبر این درگیری مسلحانه همزمان با تدفین علی خامنه‌ای در شامگاه ۱۹ تیر منتشر شده بود. آن‌زمان اما جزئيات آن منتشر نشده بود. اگرچه ساعتی پس از این درگیری سازمان هواپیمایی کشوری از اجرای «مجموعه‌ای از تمهیدات ویژه» در مشهد خبر داده بود. همچنین گزارش‌ها حاکی از آن است که برای ساعاتی، مسیرهای خروجی شهر مشهد بسته شد و تدابیر امنیتی در این شهر به‌طور چشمگیری افزایش یافت.
این حادثه در شرایطی رخ داد که مشهد میزبان آخرین مرحله از مراسم تشییع و خاکسپاری علی خامنه‌ای بود و هزاران نفر برای شرکت در این مراسم به این شهر سفر کرده و امنیت شهر در بالاترین سطح خود بود.
@
VahidHeadline
شخص همون معاونی که اون طور صریح دروغ گفته بود امروز آمار هم اعلام کرده درباره تشییع‌کنندکان مشهد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76936" target="_blank">📅 17:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JhPqz1IbXO5fUmZx5aJ-mqHvpsPWECBMl-gi4meA2NAgByj5rKY-c4FFyH73R8CKtE1NByXqWyGQYhsWmOXVwuQKMTd7daR8cFgBJ21Y8SlWu16p60YIGGyylbYFfHeox6Faj4fWuvh363GQ0UtGSwrwirZ1gJ_Tv1Obw_qCAMmO6m5fz1fxu7pAiuKtAlFji6MNcVrQHAyTl-cTs9BpNkohW1E3MIdwG1bywrPOQG3NsQyn_HYlyMO_vuPenxuTujfqww3ePjmwC0BQf1Xq2KoiARcSzhSnCHuz3NQPI60ZbLLnBp7EpRJP0rZjZrdbH3Lp8Dbu4BR9rxtpXoRpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، رهبر جمهوری اسلامی، در پیام مکتوبی منسوب به او که روز شنبه ۲۰ تیرماه منتشر شد اما تاریخ آن مربوط به دو روز پیش است، اعلام کرد انتقام خون پدرش علی خامنه‌ای «به‌طور حتمی باید صورت بگیرد».
خامنه‌ای در این پیام همچنین به «قاتلین» پدرش هشدار داد که «این جنایتکاران که فهرستی از صدر تا ذیل‌شان موجود است، آرزوی مرگ آرام و در بستر را با خود به گور خواهند برد».
او در عین حال تأکید کرد که انتقام «متوقف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادِ آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد».
مجتبی خامنه‌ای در این پیام نامی از کسی نبرد، بخش‌های دیگر پیام خود را نیز به تشکر از تشییع‌کنندگان رهبر کشته‌شدهٔ جمهوری اسلامی اختصاص داد و به درگیری‌های اخیر ایران و آمریکا بر سر آتش‌بس، تفاهم‌نامه و تنگه هرمز نیز هیچ اشاره‌ای نکرد.
دونالد ترامپ، رئیس‌جمهور آمریکا، بامداد شنبه نوشت در صورت هرگونه اقدام یا تلاش برای ترور او، «هزار موشک آمادهٔ شلیک» به سوی ایران هدف‌گیری شده و ارتش آمریکا برای یک دورهٔ یک‌ساله، با امکان تمدید، آماده است «تمام مناطق ایران را به‌طور کامل نابود کند».
پیام عمومی مکتوب قبلی منسوب به مجتبی خامنه‌ای ۱۱ روز پیش به‌مناسبت هفتهٔ قوه قضاییه منتشر شده بود.
مجتبی خامنه‌ای در عین حال غایب بزرگ مراسم تشییع علی خامنه‌ای بود که بیش از چهار ماه پس از کشته‌ شدنش در اولین موج از حملات آمریکا و اسرائیل طی چندین روز با سازماندهی حکومت برگزار شد و نهایتاً ۱۸ تیرماه در مشهد به پایان رسید.
در جریان تشییع جنازهٔ یک‌هفته‌ای علی خامنه‌ای، بسیاری از شرکت‌کنندگان در این مراسم خواستار «خون‌خواهی» و «عدم سازش» شدند و گروهی نیز پارچه‌نوشتهٔ بسیار بزرگی با مضمون درخواست برای «قتل دونالد ترامپ» همراه داشتند.
مجتبی خامنه‌ای بود که کمتر از ۱۰ روز پس از کشته شدن پدرش در نهم اسفند ۱۴۰۴ به‌عنوان رهبر تازه جمهوری اسلامی معرفی شد، در هیچ بخشی از این مراسم حضور نداشت. در این مدت طولانی هیچ فایلی صوتی یا ویدئویی نیز از او که نشان دهد در چه وضعیتی است، منتشر نشده است.
این در حالی است که در مراسم تشییع جنازه علی خامنه‌ای تقریباً تمامی مقام‌های ارشد جمهوری اسلامی حضور داشتند، از سران سه قوه تا فرماندهان سپاه پاسداران و حتی سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از ۹ اسفندماه پارسال یعنی آغاز جنگ تاکنون خبری از آن‌ها نبود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76935" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fxf4mq74hHVm2Xm5Uv4CWDpOXFF7BZk166NaCOR48oc7ELE9dinpQt6V-C0AIRZrAKTl-Ag2BLXlkJ_Rby8uSx07wz9LvR-Zbwzcqpgdl1xzpimsmtb-rS_6PLe30ocsUdai671nIIr9RN-vK5iCRpT-28K3IaHbB57cqLVIRDDwbGdN48HjtrR42PZCb_vXpuwzUyyOmv2468IsdwHbNuKZen79IvpNojtqXYCS5pq96Y5YeGzJQcqATVVJol_6ragdrkA3jXoIJHvnWDzpGokIL-e4UTwT_e2eoamkHtqemBvX0MkuT-3_wux9WOy29HW5Z3Poml12iK-ahOOa5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، از صدور حکم حبس برای یک فعال صنفی معلمان خبر داد.
این شورا روز شنبه ۲۰ تیر اعلام کرد شعبه ۱۰۳ دادگاه کیفری ممسنی شکرالله احمدی، بازرس این شورا و عضو هیئت‌مدیره انجمن صنفی معلمان فارس، را در مجموع به سه سال و هفت ماه و ۱۵ روز حبس محکوم کرده است.
آقای احمدی به «اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی و خارجی» و «فعالیت تبلیغی علیه نظام جمهوری اسلامی» محکوم شده است. او ۲۰ دی ۱۴۰۴ در خانه‌اش بازداشت و چند روز بعد آزاد شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76934" target="_blank">📅 17:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brc3jNkZ46gz0q8BzDBcI43CiPvDPqz_8iA3BHxCbRpAOm_XP86TDcDmsYi-eSYLflGxq9pVXbtFMr__JK7Vm8V_JMxoMwXL_Py-u98KaGJ6JqL7L2qxRX721IgHD8oRJyujLTI8Npa8rvwdfmqjdT43v_QO0ibs0dKmNeomElEwlhdHDaAZTIQh4FlzDquUsXxQb7vWj_NEdqcfaAwbcl1jvfMLhgwbfRGFxuhAITG6Gsb29EJ-v7SwSnApKxWLvhTrV_zNp7f3Ocws9BHPtSFBvjI-X2guH6mrLsMnCiCu9PViT4ac0ld5C6EQZipw0lgvZKI0_Gp7fTT5nG-2qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کودک ۱۳ ساله در پی تیراندازی نیروهای مرزبانی به سوی یک خودروی خانوادگی در منطقه هو‌رامان استان کردستان جان خود را از دست داد. مقام‌های محلی اعلام کرده‌اند که این حادثه از سوی مراجع قضایی و نظامی در دست بررسی است.
تابناک خبر داد که این حادثه در منطقه مرزی «ته‌ته» هو‌رامان رخ داده است. اعضای یک خانواده پس از پایان کار روزانه در باغ خانوادگی، با یک دستگاه خودروی تویوتا در مسیر بازگشت به منزل خود در روستای «دره‌کی» از توابع شهرستان سروآباد بودند که نیروهای مرزبانی، به ظن آن‌که خودرو متعلق به قاچاقچیان است، به سوی آن تیراندازی کردند.
در جریان این تیراندازی، گلوله به کودک ۱۳ ساله‌ای که در قسمت بار خودرو حضور داشت اصابت کرد. او بر اثر شدت جراحات جان خود را از دست داد.
استاندار کردستان با تایید این حادثه اعلام کرده است که موضوع از طریق وزارت کشور، دادسرای نظامی و مراجع قضایی نیروهای مسلح در حال پیگیری است. او همچنین بر لزوم روشن شدن ابعاد حادثه، نحوه وقوع آن و اطلاع‌رسانی نتایج تحقیقات به افکار عمومی تأکید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76933" target="_blank">📅 17:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hJq_psHfmEAxk4YbB9vYKJYP3EHVXOglrVHD0MHSS26RkgY_eRDmsiR755elbNESHGVQUV4lfQNOz2EgrM0pwpFa-fW21-0kIetwGNRiohr2KIvYRiNbohPk5aTh5TZElngJMo2qNA-wfNW1mytTTcCXy-wf1O1nR1NZ1_ZT9J3wZsf_InvltGhFAt3XFlNSsLTkjcXfPBmVySg0-S0TwJjGfZfUT26KzVFfpLvr4eFBHc0s6RvjmeyAleYyd243D7sE3Ex2OmnZNpSwJw6L6EY6N8Vlh3BAImslxHLtIFhGejMnTeWdNMwmc1sQwIOPAsFo5rRZqQDTCvVp8nHS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GUkjLN4Fg_ybDUlBi7D4RMVRmvz3e18OMfNYXurQ9XZXmsAMZB1v0iVP1M13dVyaJOaITmDn69Fe-7cMHNGb8qd0F4qrLwjpE0xvHy-CBWR9ELAk2jAjPgsTBf7MSC9Dol8CxTLnFN9UhlKJGvgbIwcSHVAyMrJ6tTbxLBonj68vWFLiWMcPYX18O0kqMJa9Q7BhEPpTpS8PiJ_xv8OXFoPyY8O4nNmvSHX5_6p1JJN_T1ERpsR8-m0DlKYl2CdRRP1kkt5DW3n7oXtYZxoy31BiXd9qKHefcXIgMktSR4G89KX4vsbDEk0SdyONrtK46-q5Gh980Nsuo2BydnIrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qVZAC4T1F0-iXls6rAbUu1g9ny5ea1Tl2ppZmfZhFhpMxdFripe_vfbmik4ZGwjVwoP-HdWJdBaPv338fhTBJdKo74hq5vZKv_A15mRF-4-anm3c6VPb9slufQT-fMhcdGiNQOR1U_gq0ZWdgErP47kvA5o1wo1w8OF7HakqY3yadD3j7J8ig77mCnXA9cwVioyk_HazgCzfiJW3hIdHnyDeFe-yvCX0aDJvmOcbWHvYXQC9JF3JbcvRGz1dQ5GxgZ7vq7xCH6fgFy9PmX83TVdPYIidf1KRQPCMnDumyl7WjmGaJgit37xhocMdD4E95qSDUhagP6YapK07F-no3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=sSzjGC4MvoGUQ49OxzeSkVL2B5Tj56ncANrsxsjAu2yUj41L7s7ocyvdBEYJ6BUs6WP2r5AW7ZzBhB8CUcMbantBjnBHK01hlFtmqR6dYmVxreqM_wsn12k81JJMOpsy_7uOZDsIwJFmWDsdVERVeeuExD1F579lNGrkFFcM2eXbQQ3b_ES4wj1NoUBHN-6VctBkMPV4CuuaGNGeBgTEfhnpABV3HJl0-l98q2jRPuSjuAx99nLpeAIDweZYa_Go9o1B0CSZjDxRUywgmrGzdw3Vdv06bUyAwnrT83tI--ju4NeaKKEHYeCo2hu-DuepQzzr8__1E44YVaVGBV2o7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=sSzjGC4MvoGUQ49OxzeSkVL2B5Tj56ncANrsxsjAu2yUj41L7s7ocyvdBEYJ6BUs6WP2r5AW7ZzBhB8CUcMbantBjnBHK01hlFtmqR6dYmVxreqM_wsn12k81JJMOpsy_7uOZDsIwJFmWDsdVERVeeuExD1F579lNGrkFFcM2eXbQQ3b_ES4wj1NoUBHN-6VctBkMPV4CuuaGNGeBgTEfhnpABV3HJl0-l98q2jRPuSjuAx99nLpeAIDweZYa_Go9o1B0CSZjDxRUywgmrGzdw3Vdv06bUyAwnrT83tI--ju4NeaKKEHYeCo2hu-DuepQzzr8__1E44YVaVGBV2o7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده شدن صدای انفجار حوالی پارچین، پاکدشت و قیامدشت در جنوب شرق تهران و دیده شدن دود
شنبه ۲۰ تیر
Vahid
خبرگزاری فارس:
فرماندار پاکدشت: صدای انفجار ناشی از امحای مهمات بود
صدای شنیده‌شده مربوط به عملیات کنترل‌شده امحای مهمات باقی‌مانده از جنگ بوده و هیچ‌گونه حادثه یا تهدیدی متوجه شهروندان نیست.
این عملیات با رعایت کامل ضوابط ایمنی و توسط نیروهای مسئول و متخصص انجام شده و از پیش برنامه‌ریزی شده بود.
پس چرا اعلام نشده بود؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/76929" target="_blank">📅 09:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kSefMvZSw0BLTuIR7_5S2OgU6jxHx_vqsW_WPKGKTh9OzSGzGcpE2vG303vunzMsJpYPE7JusIu32_KQosAtc8rnOKD2fIIT_oE5qMzvdF60tf77MRIZ4-YcMJKRIJ-OczwkeTxNKbEuCbl0xUhRrrnkBgN_05DmtV2t_l_3xhjrLKabj04DjNw3jL2sINDbiGFocZGRn649zH8Sq6Xi4Wr37cGWJ_nn4Uf4e6M9SPitasDINzvAuyQJJldOUpz3OJzVGTMwVhFlseW3nC8e60SsGoBz5utvfip90JMPIdMfdAb7MqPPO9zzbcF_VHQQD9GBk7wOnLuCh6xC2r5cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار در پاکدشت پارچین
سلام وحید جان
پارچین همین الان صدای یه انفجار شدید ۹:۳۱
صدای وحشتناک قرچک. مغازه لرزید
کل قرچک صدا رو شنیدن
معلوم نیست هیچی
ساعت ۹:۳۰ صدای انفجار شدید سمت پارچین
دودش مشخصه
قیامدشت کلا لرزید
شهرک صنعتی خاوران
شیشه های مغازه لرزید ۹:۳۰
سلام ما خاور شهریم صدای انفجار شدید اومد شیشه ها لرزید
صدای انفجاری محیب از قیامدشت به گوش رسید
به حدی مهیب بود خونه لرزید
سمت شهرری هم لرزید حتی
درود ، عزیز پاکدشت صدای انفجار اومده دقیق ساعت 9:28
سلام ماهم صدای انفجار پاکدشتو حس کردیم از خواب پریدیم و ترسیدیم ولی یک انفجار بود
سلام اقا وحید ما تو قیامدشت چنان حس کردیم که انگار کارخونه خودمون منفجر شد
کل قیامدشت و چهلقز شیشه ها و خونه ها لرزید
سلام وحید جان ،پارچین انفجار شدید بود،ما قیامدشتیم،موجش تا اینجا اومد
سلام قرچک صدای انفجار اومد شیشها لرزید ولی دود دیده نمیشه
سلام ما محله ی ارکیده های پاکدشت زندگی می‌کنیم
و انقد انفجار شدید بود ساختمان ها لرزیدن
سلام پردیس  شنبه ۲۰ تیر حدود ساعت ۹،۳۰ یه صدای بلند اومد
ما پارچین هستیم همین الان صدای انفجار اومد تقریبا ده دقیقه قبل ،الان دودش هم میاد
وحید جان پارچین یه انفجار شد ستون دودش معلوم بود. پشت تپه های پارچین
تموم خونه ها شدید لرزیدن
سلام. نارمک ما صدارو شنیدیم تا قبل پیامها فکر کردیم توهم بوده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76928" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qjo9gLGX0UW20aACDW4fWb59pdhMuMTXx7XoawyE5TxQWmxEM9gZlWBYzqRfnCTkamGf7UwwWyA1Jm79pN8y2dsp8aWk9KiNHQoPM3t6uxMWR1qo5IPRa0O142zYa9FPgiWe5DlDzjlYS0bfhGUFeUZekIbsnyLvS-2lmoAF_i209fZe4_A7meZYlFg-6Hw-sE6JZ9wRkUcqzQT9hDUceyy0CuNZZR-w8y8RcazSmKFPErbGua8tHBiQXhPPyqnOmAxJ8QirYHkGR9upLq58RIL8FryVVqLoRgUp2iWuJTTycVw2VhPHr6jtyYlW_eZWcM8KJrC4F2UtlQbROZu5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر تهران برای ترور من تلاش کند، هزاران موشک دیگر شلیک خواهند شد
ترجمه ماشین:
هزار موشک در حالت آماده شلیک قرار گرفته و جمهوری اسلامی ایران را هدف گرفته‌اند و در صورتی که دولت ایران تهدید خود را ــ که در بسیاری از نقاط جهان اعلام کرده ــ برای ترور یا تلاش برای ترور رئیس‌جمهور مستقر ایالات متحده آمریکا، که در این مورد شخص من هستم، عملی کند، بلافاصله هزاران موشک دیگر نیز به دنبال آن‌ها شلیک خواهند شد!
دستورها از پیش صادر شده‌اند و ارتش آمریکا آماده، مایل و قادر است برای مدت یک سال ــ که قابل تمدید است ــ تمام مناطق ایران را به‌طور کامل درهم بکوبد و نابود کند — ستایش از آنِ الله باد!
رئیس‌جمهور دونالد جی. ترامپ
1000 Missiles are Locked and Loaded and aimed at the Islamic Republic of Iran, with thousands of more to immediately follow, should the Iranian Government act on its threat, pronounced in many corners of the Globe, to assassinate, or attempt to assassinate, the sitting President of the United States of America, in this case, ME! Orders have already been given, and the U.S. Military is ready, willing, and able, for a one year period of time, subject to extension, to completely decimate and destroy all areas of Iran - PRAISE BE TO ALLAH! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76927" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwLDlIvTCk_6m5cxez-f86Sf0i6rjN07NoYoyIvp8hoLXqH6kxSqQGD9M-ovcvGvZ9jSTjD-hN9DoZ-Ys-4aXUPpdqSOdO-ZPftGx0vrvGQiEdSGwOegPSMxpoMpQz0S7D9Km-FM1TyRebBjnWuHEGGGApCHp7SVHbsKQr2z_CaulNK6Kayrm260rFtCshTyPSnnzqRTYIsyW8AlZMNSkcEhBNUafzV-gtdQl4V-p95egnpf6lrzg9wziVxSu09GFBVE08xyqfYMMHdB_Orn1c2Mu61PAqROMwGaZk7vI_8vb24k9qKrbRzd0MFsPBpVIaeqz7l_I2xViY6L44l8ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «سی‌بی‌اس نیوز»، مقامات ارشد آمریکایی روز جمعه فاش کردند که مقامات ایران در پیامی محرمانه به مشاوران دونالد ترامپ اعتراف کرده‌اند که شلیک به کشتی‌های تجاری در تنگه هرمز یک «اشتباه» بوده و این حملات توسط یک جریان «خودسر» از تندروها با هدف تخریب مذاکرات انجام شده است.
با این حال، کاخ سفید این اقدام را نقض صریح آتش‌بس دانسته و خواستار اعتراف علنی تهران به این اشتباه شده است.
براساس این گزارش، تیمی ارشد از سوی ترامپ، شامل جی‌دی ونس، معاون رئیس‌جمهوری، جارد کوشنر، داماد ترامپ، استیو ویتکاف، فرستاده ویژه کاخ سفید و مارکو روبیو، وزیر خارجه، مامور شده‌اند تا گفتگوها را روز شنبه در عمان ادامه دهند. در حالی که واشنگتن انتظار دارد ایران پس از این نشست تعهد خود را به باز بودن کامل تنگه اعلام کند، مقامات آمریکایی هشدار داده‌اند که اگر ایران نتواند به این ساده‌ترین بخش توافق پایبند بماند، امیدی به حل مسائل پیچیده‌تر نظیر تسلیم ذخایر اورانیوم غنی‌شده نخواهد بود و در صورت ادامه اقدامات خصمانه، با پاسخ سخت نظامی و اقتصادی مواجه خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76926" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LZBSj7P7bLdf7zBcTVaBcDQwDapIZzcv7X6ioYMsFBK9s8eaau-rQMS7eEVt733ayX1bdCG07IvnYbvvhzzkmf_3zz--6LwdTw5FQ62NTUauWUf-XQprNrGK01yR91TUb4nK0pKshJFcznXOxP_9XUszjOmbElOVXRQjKVTlmTe9npic6Pd3bn1si5ljczZYdweK6DwFzF2DrF1AuozuFKY8ClzyNdp8tqX7y2r7O7j0e0vGVMlEcQPHqcBoCuKL1ovajTY9sfbTYRIsjej9pJyprTNKgBx0l7J1OTVACYG9jjS3bCCUUJHY6KbfbIOIxbv5UArWIQGRD_yVP5D6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از ایران خواسته است ظرف ۲۴ ساعت علناً متعهد شود که شلیک به سوی شناورها در تنگه هرمز را متوقف خواهد کرد
اکسیوس (ترجمه ماشین):
سه مقام ارشد آمریکایی روز جمعه در جلسه‌ای توجیهی با خبرنگاران گفتند ایالات متحده، هم به‌طور مستقیم و هم از طریق میانجی‌های منطقه‌ای، از ایران خواسته است امروز، شنبه، بیانیه‌ای علنی منتشر کند که در آن روشن شود تنگه هرمز باز است و ایران متعهد شود به سوی کشتی‌های تجاری عبوری از این منطقه شلیک نکند.
چرا اهمیت دارد:
ایران با چندین بار شلیک به سوی کشتی‌های تجاری در تنگه هرمز، یادداشت تفاهمی را که سه هفته پیش با ایالات متحده امضا کرده بود، نقض کرد.
این اقدام به چند دور تبادل آتش انجامید و توافق را در معرض فروپاشی قرار داد.
مقامات آمریکایی می‌گویند اگر ایران به چنین تعهد روشن و صریحی پایبند نباشد، این موضوع تردیدهای جدی درباره اجرای یک توافق هسته‌ای ایجاد می‌کند؛ توافقی که بسیار پیچیده‌تر و حساس‌تر است.
محور خبر:
قرار است عباس عراقچی، وزیر امور خارجه ایران، و بدر البوسعیدی، وزیر امور خارجه عمان، روز شنبه در مسقط دیدار کنند تا درباره وضعیت تنگه هرمز گفت‌وگو کنند.
عمان در هفته‌های اخیر، حتی پیش از امضای یادداشت تفاهم، با ایالات متحده و متحدانش در خلیج فارس همسو شد و یک مسیر کشتیرانی جنوبی در نزدیکی سواحل خود گشود که کشتی‌ها می‌توانند از طریق آن از تنگه عبور کنند.
ایرانی‌ها که معتقد بودند این اقدام اهرم فشارشان در مذاکرات با ایالات متحده را تضعیف کرده است، خشمگین شدند.
مقامات آمریکایی می‌گویند اعضای تیم مذاکره‌کننده ایران به آن‌ها گفته‌اند عناصر تندرو در داخل حکومت تصمیم گرفتند برای بازگرداندن این اهرم فشار، شلیک به سوی کشتی‌ها را آغاز کنند.
در مواضع علنی، تیم مذاکره‌کننده ایران، فرماندهان سپاه پاسداران انقلاب اسلامی و دیگر مقامات ارشد، همگی موضع واحدی دارند و خواستار کنترل ایران بر تنگه در آینده هستند.
پشت پرده:
یک مقام ارشد آمریکایی مدعی شد که پس از دو روز درگیری در اطراف تنگه در اوایل این هفته، ایرانی‌ها «دوباره به سراغ ما آمدند و خواستار گفت‌وگوهای بیشتری شدند تا برای حل برخی مسائل تلاش کنند.»
این مقام آمریکایی گفت: «آن‌ها به ما گفتند: “گند زدیم. اشتباه کردیم. بیایید به گفت‌وگو ادامه دهیم.”»
به گفته او، در داخل حکومت ایران بر سر اجرای یادداشت تفاهم و مرحله بعدی مذاکرات با دولت ترامپ، جنگ قدرتی در جریان است.
یکی از مقامات ارشد آمریکایی گفت: «افرادی در داخل نظام آن‌ها هستند که می‌خواهند به توافق برسند، اما ما نمی‌توانیم به‌جای آن‌ها تصمیم بگیریم. خودشان باید اوضاع را تحت کنترل بگیرند.»
چه می‌گویند:
مقامات آمریکایی گفتند انتظار دارند ایرانی‌ها پس از نشست روز شنبه در عمان بیانیه‌ای منتشر کنند.
یکی از مقامات ارشد آمریکایی گفت: «ما می‌خواهیم آن‌ها علناً بگویند که شلیک به سوی کشتی‌ها را متوقف خواهند کرد و به‌صراحت یا دست‌کم به‌طور ضمنی بپذیرند که گند زده‌اند.
در حال حاضر روی همین موضوع کار می‌کنیم. انتظار داریم ایرانی‌ها بگویند همه مسیرهای کشتیرانی در تنگه باز خواهند بود و هیچ عوارض عبوری دریافت نخواهد شد.»
یک مقام ارشد آمریکایی دیگر گفت اگر ایرانی‌ها از انجام این کار خودداری کنند، پیامدهای سنگینی در انتظارشان خواهد بود. او گفت: «اگر فردا موضع آن‌ها این نباشد، روز خوبی برایشان نخواهد بود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/76925" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eSU-UWCb2JFCcHZTVL0i5-2s1l7IX84Suh-eh2K0dqXs2eE4aCppFgmjNiDuVWseeJpw5GRmdPZVRsz_tsaKKbs7pNVO2YQT4OTEO_3OWEzY4PxLzU80hU6lJdaz-B1lgPGkShvIvdMg6xDHSrIw_bhKZw4jY7HsMqzNf4se90CFOj2gdlQXIoXcYJvTJIgRtrVFI5e5s6ER-KhqFj_5ru833RPWnHq6MnLdxm5e-8HIPLGPEOvxLmnfGLSminDqyO8lRYJgwttk6p8ZQLWAJ5EXzOQeK7ZxSnnH63s6QT7Vjb23AkAakUXS57nVRE3rLmkWlivD5n4kc2hBrb1WbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا در اقدامی که از بی‌اثر شدن تفاهم اخیر میان تهران و واشینگتن حکایت دارد، تحریم‌های تازه‌ای علیه جمهوری اسلامی و شبکه مالی آن وضع کرد. در فهرست تحریم‌های جدید نام علی انصاری، از چهره‌های نزدیک به مجتبی خامنه‌ای و متهم به فساد اقتصادی، دیده می‌شود.
وزارت خزانه‌داری آمریکا جمعه ۱۹ تیر اعلام کرد این تحریم‌ها در واکنش به حملات جمهوری اسلامی به کشتی‌های تجاری در تنگه هرمز اعمال شده است.
این وزارتخانه علی انصاری را «تسهیل‌گر مالی» جمهوری اسلامی معرفی کرد و نوشت او بر شبکه‌ای گسترده از دارایی‌های جهانی به سود مجتبی خامنه‌ای و دیگر مقام‌های حکومت نظارت دارد.
بر اساس بیانیه وزارت خزانه‌داری، انصاری با نهادینه کردن اختلاس در ساختار جمهوری اسلامی و انتقال ثروت‌های عمومی به مجموعه‌ای از املاک و دارایی‌های تجاری در خارج از کشور، خود، مقام‌های حکومت و مسئولان ارشد دفتر رهبر جمهوری اسلامی و سپاه پاسداران را ثروتمند کرده است.
وزارت خزانه‌داری آمریکا همچنین شماری از صرافی‌های کلیدی وابسته به حکومت ایران را تحریم کرد؛ نهادهایی که سالانه میلیاردها دلار را به نمایندگی از بانک‌های تحریم‌شده ایران جابه‌جا می‌کنند و با استفاده از شبکه‌ای از شرکت‌های پوششی، فعالیت‌های مالی حکومت را پنهان می‌سازند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پس از وضع تحریم‌های جدید گفت مجتبی خامنه‌ای «در حالی در انزوا پنهان شده که حکومتش در حال فروپاشی است».
او ادامه داد: «وزارت خزانه‌داری همچنان از همه ابزارهای خود برای جدا کردن او و دیگر مقام‌های ارشد حکومت از نظام مالی جهانی بهره خواهد گرفت. ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/76924" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb410e1088.mp4?token=mnva2QJeX88lLVMZ-vIxvZsxG_5sGtyhp4DcfP6ybVcwp2xtsXtDzGSlPDzjWy-aN8RGpj0YXTImpyliOGOOcpYbgv2aHNVdCsvROczGv29rde02Hfwc1Rqi05ohKxANJEjOo5lVZ2XuIh8kfZgAClbsru9GVJEBnGFIBtP6oq0EuKj4sqyWFhhaAeu9mGsTENwdNvWPsvFIk5H5Olrt2bja-M0uqki1ZS05IIAjkRmCp0JJFYXGm8WEXcB-R0eOg6EzF-_vNEQ1MqVHLqQP7hyuhIHdsgacIbo14n9qpD9mzjASqsQK61mAqS67YPXXW1pPR84ks0-_5zfEsyAWhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb410e1088.mp4?token=mnva2QJeX88lLVMZ-vIxvZsxG_5sGtyhp4DcfP6ybVcwp2xtsXtDzGSlPDzjWy-aN8RGpj0YXTImpyliOGOOcpYbgv2aHNVdCsvROczGv29rde02Hfwc1Rqi05ohKxANJEjOo5lVZ2XuIh8kfZgAClbsru9GVJEBnGFIBtP6oq0EuKj4sqyWFhhaAeu9mGsTENwdNvWPsvFIk5H5Olrt2bja-M0uqki1ZS05IIAjkRmCp0JJFYXGm8WEXcB-R0eOg6EzF-_vNEQ1MqVHLqQP7hyuhIHdsgacIbo14n9qpD9mzjASqsQK61mAqS67YPXXW1pPR84ks0-_5zfEsyAWhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رسانه‌های دولتی چین، ‌این کشور برای نخستین بار با موفقیت یک موشک با قابلیت استفاده مجدد را فرود آورد که این امر پیشرفت بزرگی برای برنامه فضایی این کشور محسوب می‌شود.
پیش از این، قابلیت استفاده مجدد موشک‌ها در انحصار شرکت‌های اسپیس‌ایکس ایلان ماسک و بلو اوریجین، متعلق به جف بزوس، بنیانگذار آمازون بود. حالا چین با انجام این آزمایش موفقیت‌آمیز می‌تواند برتری آمریکا در زمینه موشک‌های قابل استفاده مجدد را به چالش بکشد.
شرکت فضایی اسپیس ایکس در دسامبر ۲۰۱۵، برای نخستین بار یک موشک فالکون ۹ قابل استفاده مجدد را فرود آورد و پس از آن در نوامبر ۲۰۲۵، موشک نیو گلن شرکت بلو اوریجین به زمین نشست.
فالکون ۹ حالا حدود ۱۵۰ بار در سال با پیشرانه‌هایی پرتاب می‌شود که قابلیت ده‌ها بار استفاده مجدد را دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76923" target="_blank">📅 21:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76921">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ShSyrbSkRL0IQZOdUyH949V2skN0eOtSFEEAkRpSPWQZf7LevPIC5gC89Ge0yCQ5sQ-zdBGZmhHN6aUOZBF7DGPseuWPlLHTtSbZIWJMwKyHYA6E8KoM92RFkHGrjkMHIKStO-Ql793u2fO1owuT1goGj3cZVcICSKKKK6PMSR8RXVjFonDQFw2wg1oAJwNECN8tmCEOO-07Ib89hPuoU4duRBb18YtqQ8XFNT4VL75OtJhYuLexKj01xWOBJVLdfK9JLcsE3STIZEajiNgMLwEhQPQb_06GKbNve8MxErmOwrIECWvwoKaDpl2kpWSiGINFmBTUxyM4KmXYgW8-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf31c0a00e.mp4?token=pXuacsoYnkJTO-VhH3VVizBu41yNiBawrz5-agA8KVVInn2DMCyxtM__ZpoJCV6dJ0cWU24QPSj57fN7L2WLeAq3e8JxCIQgYbO0A8h3K4tfCRgUforu3-p6I-kXF-YKinyofSj04uRTQbvcXydpzifYxx5Sul6MtNg7U26hSOdpVD-KYYCd6IU5UF_rQ1fhom04Tkkp867Bq2raVNFndU7Kk31mB4H87SYOdiq-8zkfRFvhvniilUPYO8xpmqRC14qxHtwbDorS1yG8WojllrrpQUoBMFxVSEvViUNJnLU7XXvF9CWhSaz7AQFIVyyRT740KHU6jU_gDGQ0J0WRfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf31c0a00e.mp4?token=pXuacsoYnkJTO-VhH3VVizBu41yNiBawrz5-agA8KVVInn2DMCyxtM__ZpoJCV6dJ0cWU24QPSj57fN7L2WLeAq3e8JxCIQgYbO0A8h3K4tfCRgUforu3-p6I-kXF-YKinyofSj04uRTQbvcXydpzifYxx5Sul6MtNg7U26hSOdpVD-KYYCd6IU5UF_rQ1fhom04Tkkp867Bq2raVNFndU7Kk31mB4H87SYOdiq-8zkfRFvhvniilUPYO8xpmqRC14qxHtwbDorS1yG8WojllrrpQUoBMFxVSEvViUNJnLU7XXvF9CWhSaz7AQFIVyyRT740KHU6jU_gDGQ0J0WRfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخواست افتخاری برای حذف صدای خود از آلبوم "بدرقه" [بدرقه خامنه‌ای]
علیرضا افتخاری با انتشار ویدئویی علت این درخواست را ضعف فنی اثر عنوان کرد.
این آلبوم با صدای هفت خواننده از جمله محمد معتمدی، پرواز همای و ... به مناسبت تشییع پیکر رهبر جمهوری اسلامی ایران، توسط شهرداری تهران منتشر شده است.
Koronmusic
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/76921" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76920">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e9af1050e.mp4?token=JE080tFQCzujCfdYukHENy6Qqbl0U1rCTYa8efLso2l6MyW9xCimard_phjePvbY34q5tzmCLvqe_k4Jcou-BXlTNLBnZHDkyji25lJBaqQRTIoxCqUCLamPqzO49Q7V9Ci_xVg49rDkO7gs3Qj95oSJAGyLSxCkIFPJwqxLuVXRNsjDWK5NjkEk2jj51drKbvfOFmHmF6QtgxyYixQpUaU3AYrhUj_duSaMqKbaSN7fVGD0bdNs3uuv6ULG96hGHCnpHnpkPvTDUly8dECMEQTdLipoKZP0imFzW-ZL_dkRVFWHhiLGQ-W0qpuizB9kuUrxyt3Mp6Ta1F5iCOeOqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e9af1050e.mp4?token=JE080tFQCzujCfdYukHENy6Qqbl0U1rCTYa8efLso2l6MyW9xCimard_phjePvbY34q5tzmCLvqe_k4Jcou-BXlTNLBnZHDkyji25lJBaqQRTIoxCqUCLamPqzO49Q7V9Ci_xVg49rDkO7gs3Qj95oSJAGyLSxCkIFPJwqxLuVXRNsjDWK5NjkEk2jj51drKbvfOFmHmF6QtgxyYixQpUaU3AYrhUj_duSaMqKbaSN7fVGD0bdNs3uuv6ULG96hGHCnpHnpkPvTDUly8dECMEQTdLipoKZP0imFzW-ZL_dkRVFWHhiLGQ-W0qpuizB9kuUrxyt3Mp6Ta1F5iCOeOqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">PapiTrumpo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/76920" target="_blank">📅 19:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76919">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pFVOj-qUO5BaMhOsRAboopsQzeCNTDwvyNk1smmWBa0DwgLfJWH7JnAFHn74n8cY06JhiHyta2LOFfncg0k9wSbzplyaHe-Y90tPypEUJNe-_z4SsYwlezeqerZg_giZ62OhSGl50kn8xcvfbvtrbgvJQq6odL3mO2NpBLlNXue3X05HcZg_JVVzkGygtIOxf3s0j0_OG9jrG9qC0P77IXQKKgf3YhMponqqkXLz0Ctli3cDsYXNvnLI3k1zQH0eM0xLmQMWj-nqC0_hOzaIbWPot4auLTYCPUUvUIoxf5J6RrCFPpa8oByiO9NUEu8OOTysz9cWdk2FptYpdDc9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از یک منبع آگاه نوشت که دور جدیدی از مذاکرات میان واشینگتن و تهران، احتمالا هفته آینده و شاید در سوئیس برگزار شود.
مقام‌های جمهوری اسلامی تاکنون در این خصوص اظهار نظری نکرده‌اند.
همزمان دونالد ترامپ، رییس‌جمهوری ایالات متحده، در تروث سوشال نوشت که با درخواست تهران برای ادامه مذاکره موافقت کرده اما به آن‌ها گفته آتش‌بس پایان یافته است.
@
VahidOOnLine
خبرگزاری فارس:
درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76919" target="_blank">📅 19:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By0fZ-xEduRdPE_c53aC7HhbBoNPwIv75qffre-ssxcKMKYNnjiTvAUQ4xmm2P1WFRymHhIpPNYSl_l0DeOZD54WxNUVoOYq-q8VUvUvqAIgtTubDbLWtFncfLaOBo7m6Q9n0C4a466IUCkZt8o_XcFM5NNO4G3B6JCWoD-c-DTTTIThQIuTxFbXxGKiiE9l0NEPb2qspj4TRzi6InHdq9Ht7oM664zGLa9a4VJkeKdehn66GEmc5mqsmXMb595fS5lLakwojN9flafBEWJxj40kPn0zOAhfcDxXBeLRS8TKs75zKWkRmhde79ZtFr8Wr3zQ2wsltopUkjsbnrV_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگویی با «نیویورک‌پست» اعلام کرد که دستورات لازم را برای واکنش به هرگونه تلاش احتمالی ایران برای ترور خود صادر کرده و در صورت وقوع چنین حادثه‌ای، ایران با پاسخی ویرانگر و بی‌سابقه مواجه خواهد شد.
ترامپ اظهار داشت که مدت‌هاست در فهرست ترور تهران قرار دارد و به همین دلیل دستور داده است که اگر اتفاقی برای او بیفتد، ایالات متحده باید ایران را «به سطحی بمباران کند که هرگز پیش از آن ندیده‌اند».
او در پاسخ به گزارش‌های اخیر مبنی بر هشدار اسرائیل درباره طرح ترور جدید، با رد وجود طرحی تازه تاکید کرد که ایران سال‌هاست به دنبال حذف او بوده است. ترامپ گفت: «من از مدت‌ها قبل در صدر فهرست ترور آن‌ها بوده‌ام؛ زندگی همین است. امیدوارم دلتان برایم تنگ شود!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76918" target="_blank">📅 19:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnBP8260NIYsPvXPddiTKfl8BL2z1sBLbScDtgxZ_GwblBXs_JLV7AGVeFZldlfG1kmCxqDRA_KSyFlgTPrBLjqa9sBj7ABZAbhVIfuSwHx7YgwKu6bFeKpRWcomssESVYKAzXTjaXm4dcYxFKpqc-LBHy2qLqHgl_ehZhPAib0FWCCsfMdgjl0KCb8zduMOFP9_RqgwMZU2xMdEqtz-nxuPGBwqASnVrCiZpQtZBfqRTyFYeKO9OcjvKNrmPH9iB7vRF0nlRTMWocBjjThn9spH60o9uJLO-aoYL_YhPhQJw6R2dY2eUD7e2KlYI_o0NUTNDSb4fmHkgcr5gOqkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام جمعه اهواز گفت: فریاد ملت ایران انتقام است و از هرکسی که موشک و پهپاد دارد می‌خواهیم که زمین را از لوث وجود ترامپ پاک کند.
احمدرضا حاجتی  در خطبه‌های نماز جمعه گفت: سایه حکمرانی رهبر شهید همواره هست و آن مشت گره کرده او بر سر آمریکا فرود خواهد آمد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76917" target="_blank">📅 18:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromﻣﺎﻧﺎ ﻧﻴﺴﺘﺎﻧﻲ Mana Neyestani</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nf_vZSFCW62q4rB6xx1-GSydPjsI013WWCek8IlVnPqK4eqRg0itq-EMbsUP6VzA3uQJrBSFSP22GEyrjvOzQas_ysrmI_ZqOxj0v0Y8ej82viNE3yvcp140vW3p2EgQJdpiG0Em-LE6TK00SAfmCOhDMvW5FXLrPisul-YATB8P-o98adaQ02DjnRcFvq7b26yV3c3nTcGyztILoRNhfD1CXIFU3Y4AALsgPUsVmk0_KGNc42p46m4SggQ0_nHPSX1dvoWu3KaZJgAPyy2NFP9TwmcR8jYN55PtzyMyU32UrDDjgE_20ayZXx2cVCRJG4Fu2UYYTKWnII3D55r4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره زیر خاک رفت</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76916" target="_blank">📅 18:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76915">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qJkYOtztdGEOGT8Wi5dX7dkGqMhX9whXQTDmExT0iDs4MTWcUGQFC5gL8PFsrstqcKZUn0GuPBjbRMvpzWt4H-8bEsEibcbYkTiWacfKpM56UbnWooYvPpDi4A0xF0UiBq6J3pocNiurJGRSlAraen_nG8o1P8D3gt3zW0q8kxIQ6WUk63EsunEScFXp3LZBfntItLx5B6Uilk9yoV3kvFJn5rUIba7TXyT1HMMMkXP6_t4ekKy5bu4RcwqaF7KxnJJ0dRGkey4AtXFzyHl30GqbEKIGpEdnHopaDhkyI90Zr_axJrimEcB1zMrH2FaDz4l0vX4esrhc8lPfr1zkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران از ما خواسته است که «مذاکرات» را ادامه دهیم.
ما با این درخواست موافقت کرده‌ایم، اما ایالات متحده به‌صراحت و بدون هیچ ابهامی به آنها اعلام کرده است که آتش‌بس تمام شده است!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76915" target="_blank">📅 18:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jgSvBXrk4NJGnEeKKD45C-qwH9RjwWOGuxArm3LK92SqQsZ7U6KynGkUL9J-G53_IRY12vV9m0jDo7UjHCZiu-uiIDXoNIYK1LMkn9Dr0RCm9mtAEJyvamupHrBqYw_q6nGz7fBZ5R-m_ixpQvWxCNsbiQUGmp5_b62VlRCa13elnPcIKBR7HQ_R_t6DNhzQ-YDw_Hh41uVISzUassIt_s8Ga0_Tr82NBvlehRneObZzDVCqMjCbmQy7jSvROPknHEyZyaJXvAHGFbWYcTAYYLqJ2qLdK6XbqclHGXETpWKH6Pr06FbgYjImp5OTQ42vuDRNpqzWgF8p2SmC6fP0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت اکسیوس می‌گوید قطر، پاکستان و چند میانجی منطقه‌ای دیگر از جمله ترکیه، مصر و عربستان سعودی در تلاشند تنش میان آمریکا و ایران را کاهش دهند و مذاکرات هسته‌ای را از فروپاشی نجات دهند.
بر اساس این گزارش، با وجود آن‌که دونالد ترامپ روز ۱۷ تیرماه تفاهم‌نامه و آتش‌بس با ایران را «پایان‌یافته» اعلام کرد و دستور حملات هوایی داد، دولت او همچنان خواهان بازگشایی تنگهٔ هرمز و پرهیز از بازگشت به جنگ تمام‌عیار است.
یک منبع منطقه‌ای گفته میانجی‌ها معتقدند حملات اخیر ایران در تنگهٔ هرمز احتمالاً از سوی عناصری در داخل حکومت ایران انجام شده که با تفاهم‌نامه مخالفند و قصد تضعیف آن را دارند.
اکسیوس می‌نویسد مقام‌های میانجی روز چهارشنبه تماس‌های متعددی با مقام‌های آمریکایی و ایرانی داشته‌اند تا ابتدا بر سر کاهش تنش توافق شود و سپس تاریخی برای دور تازه مذاکرات فنی تعیین شود.
یک مقام آمریکایی نیز پس از نشست ترامپ با تیم امنیت ملی خود گفت دولت آمریکا همچنان به یافتن راه‌حل متعهد است و گفت‌وگوهای فنی برای رسیدن به توافق هسته‌ای ادامه دارد، هرچند واشینگتن حملات ایران به کشتی‌ها را «اقدامات تروریستی» و نقض عملکرد مورد انتظار در تفاهم‌نامه می‌داند.
@
VahidHeadline
خبرگزاری رویترز روز جمعه ۱۹ تیر به نقل از یک منبع آگاه اعلام کرد مذاکره‌کنندگان قطری برای دیدار با مقام‌های جمهوری اسلامی و با هدف کاهش تنش‌ها و فراهم کردن شرایط برای ادامه مذاکرات گسترده‌تر، در ایران به سر می‌برند.
بر اساس این گزارش، گفت‌وگو بین دوحه و تهران «با هماهنگی ایالات متحده» در حال انجام است.
این منبع گفت که هدف این مذاکرات، رسیدگی به اجرای تفاهم‌نامه میان آمریکا و ایران و همچنین موضوعاتی است که موجب تشدید اخیر تنش‌ها میان واشینگتن و تهران شده‌اند؛ از جمله اختلاف‌ها بر سر کشتیرانی در تنگه هرمز.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76914" target="_blank">📅 17:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kj3OT8MBMSuquz-B7F3X-DZvNb_HPQNe9qrHhW8pkMgjzlbyslDKnOaoJuFMGbO39hBY4LoW_qob2ghyiY3mI4-f0_mJz0igc5NBFIf3FQMfrUsz3zuA-MWUBNDg5oForWL-RVIDJZf5VnY8AXVu9ddPqvutsUYWj9x3eEQcMR94B6j4SEVLfxVbOHA313N1CIXezl0-ODXU22Vhh3li1LAWl2PPtEerqIfM9eAO0j5N5b6Cf5dkqGtcEWjRbUoBPo5w6KSH0iajHq-bx6CE7r-K1OvfTYRnVK2rTvB6i3bia_26nXzGQzEcz4eCtyS5hiAK4UKolL1EW_EXLNfT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KEZskgPn-xXrVMDJbJZ5IaCfI78rYzpvgz32MRCB_y4-m7Cyr6YCLShMEovvj12E80_DFlQ3hnDbzHXlT-ciFndXfnZiC3fPfczu6FdKTMkqpkI946B26nlbyaY3Lc-BelPZZISHfKOvZeJ7CPncF626YmiJ-VQs3bHUTApdg-mRGABtFqh_PlWCLsdZ08jkHPYzqtyjEC347D48LeMv2GCF2k4OEZU48MRGqaE350EZ78DQ7Ao7l35ylFfFAmaImnwBBS3zJggr7_0JrVcg1ac8pRCxkeN0uHDT9I0SClyGmW39dMwjlDSUiA2MXAJLYsLEYHsxj2vj0VuG6wRZpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش منابع حقوق بشری، نیروهای مرزبانی جمهوری اسلامی ایران با شلیک مستقیم به خودروی یک خانواده در روستای درکی از توابع شهرستان سروآباد، یک کودک ۱۵ ساله را کشتند و پدر او را به شدت مجروح کردند.
به گزارش هه‌نگاو، غروب پنج‌شنبه ۱۸ تیر ۱۴۰۵ (۹ ژوئیه ۲۰۲۶)، نیروهای هنگ مرزی مستقر در روستای درکی، بدون هیچ‌گونه اخطار قبلی، خودروی شخصی یک خانواده اهل این روستا را که پس از پایان کار روزانه در باغ گیلاس خود در حال بازگشت به محل سکونتشان بودند، هدف شلیک مستقیم قرار دادند.
هه‌نگاو گزارش داد که در نتیجه این تیراندازی، سام حسنی، کودک ۱۵ ساله، بر اثر اصابت گلوله به سر در دم جان باخت و پدرش، احسن حسنی، از ناحیه ران به شدت مجروح شد. به گفته این نهاد، پیکر سام حسنی به سردخانه بیمارستان بوعلی مریوان منتقل شده و احسن حسنی نیز در همین بیمارستان تحت درمان است.
شبکه حقوق بشر کردستان نیز با تأیید این رویداد از تشدید فضای امنیتی در مناطق مرزی مریوان، پاوه، بانه و سردشت خبر داده و به نقل از منابع محلی نوشته است که نیروهای مرزبانی و سپاه پاسداران در برخی از این مناطق، ضمن افزایش حضور نظامی، محدودیت‌های بیشتری بر رفت‌وآمد روستاییان اعمال کرده و در مواردی از دسترسی ساکنان به باغ‌ها و مراتع شخصی‌شان جلوگیری کرده‌اند.
تیراندازی نیروهای نظامی جمهوری اسلامی به سوی غیرنظامیان، در سال‌های اخیر بارها به کشته و زخمی شدن شهروندان، از جمله کودکان، منجر شده است. کیان پیرفلک، کودک ۹ ساله اهل ایذه، در حالی که شامگاه ۲۵ آبان ۱۴۰۱ همراه با خانواده‌اش در ماشین در حال گذر از خیابانی در این شهر استان خوزستان بود، هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و کشته شد. در این واقعه پدر او میثم پیرفلک نیز به‌شدت زخمی شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/76912" target="_blank">📅 17:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GNrlrfUof581k4N3z6JOMSqJu55_5U_KwhFfO14IKacSV9C4ORWcbdsH0jyqA-Up5djaTNsOCV31W877BGkzrnj57n90R7-CHrNpySPhdQY5t0rLBXO9Ec_725IUisarD4Eu_-ZsQZixJNU_-F-4cEh-2x1lFrzNpApiBmRGCmstVuADgTyp7g7DMmQoBJQcxmaMDFmx0lSDkDgGFZuH67XOCWFNgA0GImawj5x-Yfbacbt47WNp11YjQFHxiXXnb79BsJ0rf2xHXPeoQFLf1vx34OBtgW4ifY1aUvkL2W1h5s3LPf3KiNgPpGocqusdNSePIZueJX_BP3XmnpXc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از دو منبع آگاه گزارش داد اسرائیل این هفته اطلاعاتی را در اختیار آمریکا قرار داده که نشان می‌دهد جمهوری اسلامی به‌تازگی طرح مشخصی برای ترور دونالد ترامپ تهیه کرده است؛ گزارشی که هم‌زمان با تشدید تنش‌ها میان تهران و واشینگتن منتشر شده است.
به گزارش سی‌ان‌ان، یکی از منابع آگاه گفته است هشدار اسرائیل در هفته جاری به مقام‌های آمریکایی منتقل شده است. منبع دیگری نیز گفته نهادهای اطلاعاتی آمریکا در هفته‌های اخیر به‌طور مداوم اطلاعاتی درباره احتمال تلاش برای ترور ترامپ دریافت کرده بودند، اما اطلاعات ارائه‌شده از سوی اسرائیل جدید بوده و به یک طرح مشخص مربوط می‌شده است.
سی‌ان‌ان نوشت جزئیات این طرح هنوز روشن نیست و همچنین مشخص نشده که آیا دستگاه‌های اطلاعاتی آمریکا نیز به‌طور مستقل این طرح را شناسایی کرده بودند یا تنها از طریق هشدار اسرائیل از آن مطلع شده‌اند.
کاخ سفید در پاسخ به درخواست این شبکه برای اظهار نظر درباره این گزارش، که نخستین بار روزنامه وال‌استریت ژورنال منتشر کرده بود، به اظهارات اخیر دونالد ترامپ اشاره کرد.
ترامپ روز چهارشنبه ۱۷ تیر به خبرنگاران گفت: «آنها می‌خواهند رهبر آمریکا، یعنی من، را از میان بردارند. من در همه فهرست‌های آنها هستم. امروز صبح دیدم که در تک‌تک فهرست‌هایشان قرار دارم. تا اینجا کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد. اینها آدم‌های شرور و بیماری هستند و باید این سرطان را ریشه‌کن کنیم. سرطان را باید از همان ابتدا از بدن خارج کرد.»
سی‌ان‌ان همچنین گزارش داد تنش‌ها میان آمریکا و جمهوری اسلامی در روزهای اخیر، هم‌زمان با فروپاشی آتش‌بس ۶۰ روزه، افزایش یافته و دو طرف تهدیدها و حملات متقابلی را علیه یکدیگر انجام داده‌اند. با این حال، به گفته یک مقام آمریکایی، تلاش‌های دیپلماتیک همچنان پشت پرده ادامه دارد.
به گفته چند مقام آمریکایی، برای انجام حملات احتمالی در شامگاه پنج‌شنبه آماده‌سازی‌هایی انجام شده بود، اما مقام‌های آمریکایی در نهایت ترجیح دادند فعلاً به جای اقدام نظامی، مسیر دیپلماسی را دنبال کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 500K · <a href="https://t.me/VahidOnline/76911" target="_blank">📅 02:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHSimfwkPwvIRxCDtFevuhutKdLLxaCh2nm_5G8BESnVMGQWLzaeJQq3xhlyzyGLPIJhLEBPxifQA2A5yxoh90jTyOwXXbSgzxqhP0ae-qOmNRbByTb7yQ9zwmpTFaghI-yB2dstMS4zplqDBbhORspC24g8TZuP_uOeGwM5gagFt5nOpS91bXx-BM6RGFPWSruTW4ZthpWb6IxNJaOQX78LPDZ_TULJ8fP3uqus7EctjwScEXiBDl4vHbsJ555k4Qsrp4BB-he01zBSgDhuEnsn9hwTQgIhKI0SJBCXnvkETDnWj2biVUuHxgbJmB73XCKDyfGO_6Z1hpWS530KYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی،  پس از ۱۳۱ روز بالاخره در بامداد جمعه ۱۹ تیر در حرم امام هشتم شیعیان دفن شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 494K · <a href="https://t.me/VahidOnline/76910" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P0oRzq_573A_aYqbFPY0RqaNVGdPvJnVZddpCxth4qiKuyWOkbAgHEpOP4wQP3SDjwy7aH_m4ig_BtEQPM11mjcxR7Vhy-ob9RO0ecCEbOJG2M2AG-AYHIbFRNew_TU9TyLiHldikvctWF93p8WZoUWHDzOv3MawzZsOLOqhT-0A1ZAJVHzlYSgZcHU5fBlaP9xMJTHo3S_k7oaue5FN8qeTyyQpLJTtZua8P1SncIgSD0TxmAhO-qc5UCvQwkGetHoEC7YPP5MKS6V_j5HC01iWxKHvoayGsxfqGbymlLr065qXvI4B1M8fkHuolRhSXwe7-6xMFsyN2h-L5_hpCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/roVBb0RZzExTEz6t4h_Xvo4qc0sC-L0c2vxObR0BywGwvhdAOLSJzGWmeSeP_LlRq8i2GLdvPQ0kEB3W9ChZpLQnFhmD9BGYD5VrdIpCZCAprYdi4zqAb00tqPotenvDzbcrPwZGvjMI1WcoIMJs89Wel4P-biOxYlgRFPHN4G1yXyrYZkSQzLtwfJcEwX6UAjJ58TGN85hYMyyUq96srrPVQkobz6jxnbrskXK7_h8e3qeIdY4uDFLOgdminmaSPx5g8hg4FWkk7fBBveOGWrHq2-oTOY5fjRe8IitmtZUO955YDzPBJWPP1Tjfbi1dqErndoxEoSymoYXREDUABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DKcXGInj9j7r01PQWznYyKigXQ_2SPLi-vmwn3-_GjAOfypVbph-xm56yfBiR0V7xMMqYp6L0Dws8_fggDTx5mkfPXkqFx74lX6AyZpvN8SGzeZ_U_YPsbJCrjKN3RecD0widK24NJ1obaWrAPlgrsrX15_ULBWYdpiPkbyXVjyQOS3m3CaorvYqltMtmUoL9P9tKoVcINlxuQMNRsNgGyPrYjrHe_Q-OmNli_ehNxYwSpRkuQYC2WeHPL1mopsEgor8AvWmZgaKuDwL6d6-S2bu3o5mcR48yskA-wBK-lO9z5tvoixL_MmqWM6BO2MVNHS9MLYZooVPshRVFoVG7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش خبرگزاری جمهوری اسلامی، ایرنا، معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان در غرب مشهد و کشته شدن دو نفر را تایید کرده است.
ایرنا گزارش کرده که امیرالله شمقدری گفته است این رویداد تروریستی نبوده و انگیزه اصلی وقوع این درگیری در دست بررسی است.
معاون امنیتی استاندار خراسان رضوی به ایرنا گفته است: «براساس بررسی‌های اولیه ابتدا ۲ نفر با انگیزه شخصی با هم درگیر شده‌اند که یک نفر از آنها کشته می‌شود و با دخالت نفر سوم، نفر دوم نیز جان می‌بازد، هر دو نفر با سلاح گرم کشته شده‌اند.»
آقای شمقدری تاکید کرده است که حادثه در منطقه سرافرازان مشهد روی داده است.
او وقوع هر گونه حادثه تیراندازی و یا رخداد امنیتی در محدوده بافت مرکزی مشهد و اطراف حرم امام رضا در روز پنجشنبه را تکذیب کرده است.
ایرنا اضافه کرده که بلوار سرافرازان که تیراندازی در آن رخ داده، در غرب مشهد واقع شده است و حدود ۱۷ کیلومتر تا حرم فاصله دارد.
@
VahidHeadline
تصاویر هم در همون منابع غیررسمی که پیش‌تر این خبر رو اعلام کرده بودند منتشر شده بود. از درستی‌شون اطلاع ندارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 525K · <a href="https://t.me/VahidOnline/76907" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5Zz3xYTOqPKgecQEky6VZ-3ymc8HX2BtVPAr860Q5QkbNPmsDwnuatR61ZwRHK49kx38oXaFz5C6_ru0YUvvLeFwZgjobU1gHDyDvsZUkNyV42pYGMN9IaVXDBHmT16-I32O7tpHIGG2lZ5AUq8BSN6fLIVGtxLN07AyzrV16r3dk0-0qmG32kM91eqfL1Zjv7U9MJFbWN7SZSexibbSjzyHZTQXL6Iqeh6PsJbxcA3JmOK7HPP3pVmElEmMrFFIzEa_IbS7UiTeivtn6wbs80X8JPbY87w39LcErtyNwOq6m6qaH6uIv-M9YXvPaAIHPJvRpLs9jOIodEiNziYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
فرماندار کنارک اعلام کرد یک منطقه نظامی متعلق به نیروی دریایی در این شهرستان شامگاه پنجشنبه در دو مرحله هدف حمله قرار گرفته است.
🔸
محمدیونس حقانی به خبرگزاری ایرنا گفت این حمله توسط «جنگنده‌های دشمن» انجام شده و نیروهای امدادی، امنیتی و دستگاه‌های مسئول در حال بررسی ابعاد حادثه هستند.
🔸
ساعاتی پیش از این نیز معاون سیاسی و امنیتی استاندار بوشهر از حمله به یک مقر نظامی در حاشیه شهر بوشهر خبر داده و گفته بود صدای انفجار شنیده‌شده در این شهر ناشی از فعالیت پدافند هوایی بوده است.
🔸
این در حالی است که صداوسیمای جمهوری اسلامی پیش‌تر گزارش‌های مربوط به وقوع انفجار در شهرهای جنوب ایران را رد کرده و اعلام کرده بود «تاکنون هیچ انفجاری در جنوب کشور رخ نداده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 481K · <a href="https://t.me/VahidOnline/76906" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hywWd0Nl6pjZSzJAB6C8FtIPGb9pwSktC4KArXBNQNZx5fPGGiFdA0fgOYdqGhVWnXYuXUFVRn3Ikfnxh1X0cz-Co2TU1P5_Fd33ndWAyeaf8902kk0yRGZ0sd1Yc0qMQJQH8EkzvAk3-T59Rgw48CqPtuZNRi2X0hYpeVyxMySw2LATS-uRbvkN28bBDL3TLCj1DJUqqqgkiJFCa1zW_s6Iid6o6Ep42F9FEDEQTQsJ-odygZzItilU4b5bssrQ7CtgSzakSOR-bKzD9oI6Zc5WUaP9g-WTSa4T7q_jrAzLZnLKmnJUf8ta8dfGhSTj37Qv17td_7TcR0w3l-59ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ایرنا به زبان فارسی سخت تیتری درباره صدای فعالیت پدافند نوشتند، می‌ری توی متن خبر می‌بینی نوشته:
"لحظاتی قبل یک مقر نظامی در حاشیه شهر بوشهر مورد تجاوز و اصابت پرتابه دشمن آمریکایی- صهیونی قرار گرفت."
irna
به نظر می‌رسه از روی صدای انفجار برخورد پرتابه، مدعی تشخیص کشور پرتاب‌کننده هم شدند.
احسان جهانیان، معاون سیاسی و امنیتی استاندار بوشهر، شامگاه پنج‌شنبه اعلام کرد یک مقر نظامی در حاشیه شهر بوشهر مورد اصابت پرتابه قرار گرفته است.
همزمان صداوسیمای جمهوری اسلامی خبر داد تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 470K · <a href="https://t.me/VahidOnline/76905" target="_blank">📅 23:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ujnVraq13dCqsq5Ne21L-nXmfGvX4e86lIeITbdbsboJC34pmU6sTV6-NQiMLAzotUCLR3PSSDXE472XF50NcDQlVjRSwDIzHO74M5Nm-9adVbbs5-7oGfyd9Mkj8iNUeQFXdseVMx2U5XW92jc4-ejfeeupel0NLngkg-KOJN6Eero0VDctT-hqzuKPDFmg_FypnKBhSBzhIKoyAP964gQyzWWCML-7_3CI3qIkJUUJI04BxOpvV8Tb05hReT_GTWDPQ2ThCRu-lq4yyvSgxecS8inUnemCGi5lTdaaHH6aB2XFXu4XCgzadmkEuTh-0q-lvmZWwUmzYo1jwFmpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
همزمان آتش‌نشانی اهواز اعلام کرد انفجار شامگاه پنج‌شنبه ناشی از «نشت گاز» در یک ساختمان مسکونی در منطقه حصیرآباد بوده است.
@
VahidOOnLine
صدا و سیما بعد از تکذیب آمریکا:
برخلاف برخی خبرهای منتشر شده در  فضای مجازی، تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/76904" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOWeA6jdrvKWB8BfwnJqreofF0ZlW0rtp6q4ini-EOMq3Q870iTz_54oDnYW2GKfOqAPAMvE6N3BCeIB-RDDdfV96HYr_oRnGbP3cY3jowBnD9aDsueZpZ0pDnt_isndRhFlzEoUXTVI4JBmfpImNMNoUybElVsKkhVwm4KkGlBB4z2dntEhP0BvA7EaCwIsO5OLYwtxyn3SDJsyLPd2mZ_36EtqBUZq8y1_CeAVQ4MS62bV8ya1ccUmw-rMTWMz6cAgK3tWA8BvnFAuCU9gx2qyreqyQckUB4ug8TbdZcM1T-CVj8B65CenAtjpCuaJlkqutv4JEMnUiuC4EDH08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر صدا و سیمای جمهوری اسلامی ایران نشان می‌دهد که اقامه نماز میت علی خامنه‌ای، رهبر سابق جمهوری اسلامی، توسط مصطفی خامنه‌ای، پسر ارشد او، برگزار شده است.
پیشتر تلویزیون دولتی ایران اعلام کرده بود که مراسم تشییع علی خامنه‌ای، در مشهد با نماز میت به امامت آیت‌الله حسین نوری همدانی، به پایان خواهد رسید. دلیلی برای عدم حضور آقای نوری همدانی اعلام نشد.
خواندن نماز میت از سوی پس بزرگ علی خامنه‌ای، بار دیگر نبود مجتبی خامنه‌ای را در مراسم تشییع پدرش مطرح می‌کند.
مجتبی خامنه‌ای از زمان انتخاب به جانشینی پدرش، نه تنها در انظار عمومی ظاهر نشده بلکه پیام صوتی هم از او منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/76903" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qxysQ4S9xJvB-u6kCPw-vPnkXFf9XQyYe1jVv7dbdZhexugUaafAO5Q-a6XQygm1A3effY68oYXZUqE-LvAguumLGMVBGP8agQrNXO4Cdz9cp4dsZTLpzTEi44tT-vhz-f8chPJ3sEyKyiHZk3t-HNDp76F7qkvTzWpKDvI4Mt0gcwn9KVGCRDH7kRafFE85_FYRMsHXpn3DHY0wO_CNUTCgLHbr-3DLEJNj4cW4UJ28rJD1MnfACML9f0EhTB9WiLW1vJHa6rwkDQgthGYEFLpdNfdkIxI1xwoVid5CBoykbqFSZ1nfU05HM7fEG9z7AdnlzTj7cSatbAWVOLSghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر شامگاه پنج‌شنبه از شنیده‌شدن سه انفجار در کنارک استان سیستان و بلوچستان، خبر داد و نوشت: «از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست.»
خبرگزاری مهر افزود صدای دو انفجار در اطراف بوشهر و در نزدیکی شهر چغادک شنیده شده است.
@
VahidOOnLine
من از چابهار گزارش از فعالیت پدافند داشتم ولی از کنارک نه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/76902" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw0_aZkHm_UWYTxoLrC9oC_Ld-8EQ3PjRgVTyhpdzOZNM9faddgFS0HoSdmarNVqS_gCVqt1IzsJUXvKHnUR7lhS-Sd4qhqelFpnDIY--ODI7S0X8OI1KqM_4LricUQN5SmYcbYmawZJOP_nkmKygB2b7bxZ1Ji3V2SJ4vV1lqv8cy1RsVzKjfK4s6vDXag-E5foEwo1WSFq4DmM9PEKVMSwOKgOH3rkP-ogVEYiMGsxtaRHPTwKFRZ4tSa0kRQ5WqHP0mSSx4BIE7eOcwBbBiM5vz54vWsmnIeUzpODUe4RJTgVPck8FjisDQt_1vVewkvUW7EYDbnfFTBdyXcHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنج‌شنبه خبر داد که عمان رسما مخالفت خود با دریافت عوارض بابت عبور و مرور از تنگه هرمز را به سازمان ملل اعلام کرده است.
از آغاز جنگ تاکنون حکومت ایران بارها تأکید کرده است که مدیریت تنگه هرمز درنهایت با دو کشور ایران و عمان در شمال و جنوب این آبراه خواهد بود و آنها درباره نحوه مدیریت و دریافت هزینه عبور و مرور تصمیم خواهند گرفت.
حال عمان به سازمان زیرمجموعه سازمان ملل یعنی سازمان جهانی دریانوردی اعلام کرده است که با دریافت هزینه در تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/76901" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ARjxWbKHWJ9i8fgMgBDg6bIRoc0fDYTRi8gWGfaOtcsQo81xKL9eqPEN8Ai27ieoJepirFr5_HGtYOTXNACruXkgaBOxB5K-DHq5tGEPR3vN1aVxoOk-my3MF_LUIu58-VOh4Ark6He0Xv6CMA6Hbd8tVxhpZYno66ciqrozHK8d_eMYvUQX7Wz1ppaek3W0mKKxfQ_j8IZn9lmhZe9-rZCNhR-qW-71ePdVK_Sd6v2hQrBB58nHZJTSy0AeyA1NwZfLQCO40QG75c7ongWUAXmfJuqD927fjO3aP9a0fFK3rSi90oLMnIHCX_IDh0GZkHnbro33xAtTAlW9A06ZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lJIb3uA0vxG5Frpm9HvX1oc2vYW87zWkEZ5CXJS0OdpBfDbuJeal0I_sAENVvcG3L_syl0oDmHoJIC95BOiHLMYMt_3fPTYgOwJC2uTmLmJ63DSIxvDvI92J0T9gujbYcEHm3plVJfnmlm7iCWzab7Q_v2RWTKSrF7zuFTpne-BZgLCq0NSOD3cg5NZytkkecnc35PMg9HI1ryeI_7mIX3pYD-vgo-GFyKQwxXoOfcN7H-2Z6no42gs0UFMd_PBK1FHqsz0R0Mr5q2SOW8MfL-sWeZFGh7-ik_3Q3kDjfJAoJcbTfuW__ygTz_ypXU6XJsU5ALYx9WRCeZzsY23j9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک‌تایمز به نقل از فرماندهی مرکزی ایالات متحده (سنتکام)، نیروهای آمریکایی در طول دو روز گذشته بیش از ۱۷۰ هدف نظامی را در امتداد سواحل ایران در نزدیکی تنگه هرمز هدف قرار داده‌اند. این اهداف شامل سامانه‌های پدافند هوایی، انبارهای پهپاد و موشک، قایق‌های تندروی نظامی و زیرساخت‌های لجستیکی بوده است.
سنتکام اعلام کرد که هدف از این عملیات، کاهش توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز بوده است. این روزنامه آمریکایی افزود که تعداد این حملات، حدود ۱۴ برابر تعداد اهدافی است که واشنگتن در آخرین دور تشدید تنش‌ها در ماه ژوئن مورد اصابت قرار داده بود.
@
VahidOOnLine
سپاه پاسداران انقلاب اسلامی روز پنجشنبه ۱۸ تیر اعلام کرد که حملات نظامی ایالات متحده نه‌تنها «پاسخ کوبنده» ایران را در پی خواهد داشت، بلکه ترافیک دریایی حیاتی در تنگه هرمز را نیز با اختلال مواجه می‌کند.
سپاه در بیانیه‌ای اعلام کرد که تردد دریایی به ۵۰ درصد سطح پیش از جنگ بازگشته بود، اما «ماجراجویی و دخالت‌های» واشنگتن در تعیین مسیرهای تردد، عامل اختلالات فعلی است. با این‌وجود سپاه مدعی است که جمهوری اسلامی در تلاش است ظرفیت عبور شناورهایی که مطابق با «ضوابط امنیتی» از سپاه «کسب مجوز» کنند را افزایش دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/76899" target="_blank">📅 17:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oS95AZdUlg-n3-dHyFQQzaxnKdvivo4JD753cy6_Gcqd2hd3X-ojeUiLqeQLR5IG2scMqgTGiqTi43hD-BhWMYGUBpIOVTA3Gpyx3GT4GeuU2mULvvdMohPb-zl__P3ApM6ikrxlJ6W8qMBntbXi1K9RFMHPA0UPpoPDCUmbubfKmo5MudfMjhQRdSpemNm1Mjblh8_7bdiAmggn1Be-5IAn756tVfUj8Cb009zxo0t4vpvj8qkijZSfTDYH_O8V0RUaiL4GlZD6TTmeqPpQIxCr17CG_GXnzhTowOVGxEl1ilrojIAroyIdoVc8IBUxBUJh5I3fgqi_r6OyEzBpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q5doHvcMxmnb3NgzqHTDy7PHempZpe_hiCV_1APHyzKZJCkW0dICqJ77epzjcQ1RRD4RnyR8HYSr-LeL9vIkj5HHX5BuAeyt-GaSPsv8dKt0S6iY7BZorszlpqhYq9hz0r1NoptuaSqAzY_w8dc-4HQ3VcMxUjxwETxhwTCjSxEQ0OtSCWZShTjaEq2xLR4zTFQ8kR5e8ObUMD8xrpgFHmnMVmo-oOjK7MJjdui-mu5bXZYG0vNW9LBqItS35jGZlNnZA-gGO2AQzPildGJ4E-xlU1uRhdtne_ah0g2MTlLkRJGtelQEP-noPRO3DgRR-NzKWMCORqAOp8Ve6FhhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DVsVY0Jhl1yqC1Hf8-SdaYJd8_g0pfukqy3jPAzd10AowKR9FitHIsAOm8gz55T4_0QIyYJgkMSCO_jMBOpgsb-UJECB9aSpS-XyWTG78F7JDH9zs7rb3ZF26oOqgo69yvgYU-ASXGIXR3A6O_GzuzCgWhxa0auEh8XaOTAT0fMG957r59UOuYIaZjIpEEzEvzw6-cmBMLavqLtPSm71zsN9U1zdvUKdp3Y2ZEqVzaHtQbQT2_XosnKd5wnREvZoncr0jKuhBmzD2iROD_ZqUm6FbJcQ35z9W8DdDChTdCJznIubcfpgJVwhkEMsFOJJCYtNA0Md3cxKUfvaKNqK4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=OSWiw1eZxT3ocrmLBiB6IsH4uV4DI0_81mgFc7MTgHvnRgsewuM5g_dLa0PqxWRky38Cgj3k6fNnl0fFmxWy9vbxBXszmCjbPXUze7p8q5moPeQPVfucNcdiASpwsrei4GQpOvOQKmWVLayO2oItqLdZLWXaEm1kcifBPssNct2Ez0lF-pKI1Kgm0-69Cc-QrCCqJt56Y4RGyz6HykgBwXjY-u3pN_Q-8FRgUwfuuauzq2sy5YWokJNjfncJeDdzxEZ3T_G-1sFHEbLkPGN_Dwe6mB8DGX-pKWd2prX7j6INWEWCT89nqMP9HVqHEZxtFJwpwhK9hjKpIwjbfNHtrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=OSWiw1eZxT3ocrmLBiB6IsH4uV4DI0_81mgFc7MTgHvnRgsewuM5g_dLa0PqxWRky38Cgj3k6fNnl0fFmxWy9vbxBXszmCjbPXUze7p8q5moPeQPVfucNcdiASpwsrei4GQpOvOQKmWVLayO2oItqLdZLWXaEm1kcifBPssNct2Ez0lF-pKI1Kgm0-69Cc-QrCCqJt56Y4RGyz6HykgBwXjY-u3pN_Q-8FRgUwfuuauzq2sy5YWokJNjfncJeDdzxEZ3T_G-1sFHEbLkPGN_Dwe6mB8DGX-pKWd2prX7j6INWEWCT89nqMP9HVqHEZxtFJwpwhK9hjKpIwjbfNHtrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با ادامه درگیری‌های نظامی میان جمهوری اسلامی و ایالات متحده، روز پنج‌شنبه ۱۸ تیر نیز حملات متقابل دو طرف ادامه یافت؛ حملاتی که از جنوب ایران تا عراق، کویت و آسمان اردن را دربر گرفت.
رسانه‌های داخلی ایران از شنیده شدن چندین انفجار در استان بوشهر خبر دادند.
خبرگزاری فارس گزارش داد که صبح پنج‌شنبه مناطقی در استان بوشهر هدف حملات آمریکا قرار گرفته‌اند.
معاون سیاسی استانداری بوشهر نیز به خبرگزاری ایرنا گفت چند نقطه در این استان، از جمله حریم پیرامونی نیروگاه اتمی بوشهر، هدف پرتابه‌های آمریکا قرار گرفته است.
ساعاتی بعد، صداوسیمای جمهوری اسلامی به نقل از منابع محلی از شنیده شدن صدای چند انفجار در شهر چغادک، در نزدیکی بوشهر، خبر داد.
در همین حال، فرماندار عسلویه اعلام کرد بر اثر اصابت دو پرتابه به اسکله صیادی بنود، ۱۰ قایق صیادی دچار آتش‌سوزی شده‌اند. گزارشی درباره تلفات احتمالی این حمله منتشر نشده است.
هم‌زمان، رسانه‌های عراقی از به صدا درآمدن آژیر خطر در پایگاه نظامی «حریر» محل استقرار نیروهای آمریکایی در استان اربیل خبر دادند. همچنین گزارش‌هایی از فعال شدن آژیر‌های هشدار در پایگاه «ویکتوری» آمریکا در بغداد منتشر شده است.
در کویت نیز رسانه‌های محلی از وقوع انفجار در نزدیکی پایگاه هوایی «علی السالم» و منطقه بندری این کشور خبر دادند. وزارت دفاع کویت اعلام کرد در حملات تازه جمهوری اسلامی، دست‌کم یک نفر زخمی شده و وضعیت او پایدار است.
هم‌زمان، سامانه‌های هشدار در اردن از مشاهده چند موشک، پهپاد یا راکت در حریم هوایی این کشور خبر دادند و از شهروندان خواسته شد برای حفظ ایمنی، در پناهگاه‌ها یا داخل ساختمان‌ها بمانند و دستورالعمل‌های مقام‌های محلی را دنبال کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76894" target="_blank">📅 17:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AElBIRHIuN60g0k93b7jVi6gTV5rZ84LUm9tCUN30BRq2N9sAzrlUORod-O8eG34MsXHyxHfH-Pz-m1DfFRyZW0bFHuEZnTh5ss9M0bSVmdnPSo4M2IdJ3VTIn9LC05gGuCPg1ncD4hnjed5OodW6cDQ3nivBUg-0CAzgmG0SsMvkA8mqUfjMbU-X_Q_FUUBHX93gmOoQrBvz6Zx-TY8NeLgwfRTTGGTAs1x0qpRN_3yIj1UfK8SXh_3CFwCdGC9mmUdiBMroGDOtFfd7zyh1n1W-Oiwj_dsuIezncaeTlb6OEzWls8T38r__JXmBDQ_MN8pfPqICnSKDkrV4bR7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهران رئوف، زندانی سیاسی، فعال کارگری و شهروند دوتابعیتی ایرانی-بریتانیایی که در آستانه ۷۰ سالگی قرار دارد، عصر چهارشنبه پس از حدود شش سال حبس، با پابند الکترونیکی از زندان اوین آزاد شد.
این فعال کارگری در شرایطی آزاد شد که همچنان مشمول محدودیت‌های ناشی از اجرای پابند الکترونیکی است و وکیل و خانواده‌اش ابراز امیدواری کرده‌اند با توجه به شرایط سنی و جسمانی او، زمینه آزادی کامل از طریق استفاده از ظرفیت‌های قانونی، از جمله آزادی مشروط، فراهم شود.
مهران رئوف در مهرماه ۱۳۹۹ همراه با ناهید تقوی و شماری دیگر از فعالان مدنی و سیاسی بازداشت شد. با آزادی یا پایان محکومیت سایر متهمان این پرونده، او آخرین زندانی باقی‌مانده از این پرونده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76893" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XXQxwSZPpzNvHEm4bUiUKkH90Cpd7PpdGREJdjDh2hdw9AeW-uGt0Y0K5XxlvN2pD9Lteb2fU6yjbV4PNr32GnISJgm8AwtoHjrhOKqm5oOrCyMwoIfY4xQkbrfW1evmjgQrIuUwTPVIIMAqdM1rz_FALRvru7QkKP3g1_5Cs1BtUkmH_aQhaIsLq1H4A_Yc8VYQh23ChU0sj6DXisAY5UqmHYWGlm72FjIkXvc_yGO4JtB2MjRvbXISu2r-Kof4reIFZWP3nGb5e_uWYGvUVhrRW8FDs3C2lhTw9fc6Ze8Quywjflgpr2DQNxiFqw9Vf69vkJpnKHqo7tFkLdT3xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fO0cMJ4Npc0PRCfgo6OtKT1fUoIUfnu5Fqtxqv2u4C_gbOPm23wrCH0CnKMfoOsBI98dqVfP6_mwD4MmmK_32oN3Aq0w5xtCgH-4R7lnidYKkis0t-pcZSsrnuMYtVjiCTvmfQRFUs1owVtapVO1WiMnF9kszJBJz-gFqvmNwFGmcTqFS0Ua8z1o2Od6fVbHOrBFBKUZdrI3d-T1p-QPh1UOSRs3OMMdySnWbExMPwT7gDCHD2DBWGd5CBcNwUAqckN7F3NTkDYeoJVmUYq-kSQWHPvpp42Z7Dw6JAq3Fl_7ETCNUxZiBeNswI2aTq_S19KH2_6GXygfOYk4cYOw4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنجشنبه خبر داد که رفت‌وآمد کشتی‌ها در تنگهٔ هرمز پس از دور تازهٔ حملات آمریکا و ایران به مواضع یکدیگر، تقریباً متوقف شده است.
بر اساس این گزارش، داده‌های ردیابی کشتی‌ها نشان می‌دهد حرکت‌های قابل مشاهده در این گذرگاه حیاتی انرژی جهان عمدتاً در مسیری انجام شده که مورد تأیید ایران و نزدیک‌تر به بخش شمالی آبراه است، در حالی که کریدور مورد حمایت آمریکا و عمان عملاً بدون تردد بوده است.
@
VahidHeadline
راه‌آهن جمهوری اسلامی می‌گوید بر اثر حملات آمریکا به «یکی از ‌نقاط مسیر ریلی تهران–مشهد»، حرکت قطارهای مسافری در این مسیر متوقف شده است.
در بیانیه راه‌آهن به محل دقیق هدف قرار گرفته، اشاره نشده اما آمده که تیم‌های فنی و عملیاتی به محل اعزام شده و «عملیات بازسازی محل آسیب‌دیده در دست اقدام است».
توقف قطارها در مسیر تهران–مشهد ساعاتی پیش از برگزاری مراسم تشییع جنازه علی خامنه‌ای در مشهد رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 496K · <a href="https://t.me/VahidOnline/76891" target="_blank">📅 10:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=sgwXy2KXli1NydENbZO2qDOSNpwpJ-V_4hThwkO_26xj5wbgk0M0o_J5CcxMaJbfRTwzxroImoEk0M6pMaGypBJeaJl4MAzaRptGb6JPtXKNnsmYfnB5m33N-YdxIoE0A1HJZftTxZ5l6WKba2Qx-Fsi3MEnzRzx-jXfgqrTAytmoVExQnWAHjxG3NltPxHz1FAeEQFKPedaDL7mmIPLr-fyDK4PFPhBjTYEjvOsF1dLbJKVoaQpbuv5Znq1cXXdg59JZHFsdsaedpsIuVkFQ_XAjLBMzAfa5Cp75JD2aWrpcRscjydbOevIsrfadrpvDajo5-lXd3t-4NnkE7zcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=sgwXy2KXli1NydENbZO2qDOSNpwpJ-V_4hThwkO_26xj5wbgk0M0o_J5CcxMaJbfRTwzxroImoEk0M6pMaGypBJeaJl4MAzaRptGb6JPtXKNnsmYfnB5m33N-YdxIoE0A1HJZftTxZ5l6WKba2Qx-Fsi3MEnzRzx-jXfgqrTAytmoVExQnWAHjxG3NltPxHz1FAeEQFKPedaDL7mmIPLr-fyDK4PFPhBjTYEjvOsF1dLbJKVoaQpbuv5Znq1cXXdg59JZHFsdsaedpsIuVkFQ_XAjLBMzAfa5Cp75JD2aWrpcRscjydbOevIsrfadrpvDajo5-lXd3t-4NnkE7zcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در توییتر میگن 'ترامپ به محمدباقر قالیباف گفته محمد سامتینگ':
twitter
ترامپ: می‌گویند یک محمدفلانی دارد آنجا با بیل‌ یک کارهایی می‌کند. بیل‌ها شما را به جایی نمی‌رسانند. بزرگترین ماشین‌آلات دنیا هم احتمالا شما را نمی‌توانند به آنجا [محل دفن اورانیوم] برسانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 518K · <a href="https://t.me/VahidOnline/76890" target="_blank">📅 07:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=cgC3b37nRAaoNtPJMqyC8gmJdeKktuPgP2bJlHGmDJvPC1gE_SeGeWAUprQqPnoH6kDCxsmrObDeQmfqsSq91x9ph7dFLUf8uMM4Ie8zcyPk0ndctkb3EnfUQaBkfdxk2K290yURUjohTqjaVXHsd0StTcRQIwC7bf5TKN-XkvDZ_B05eR1rWIjC0vT1A36wUk7vLQHUqQf6N5r_4H-TWAyC9Fn71c82v7UGelAz1klCEI_jbd9wqNQgAdexDvZGx_GQUOMt_TbjEvFpYb4yTBMCioy_UGcAD1rk_tLQheMOYvITB1MQcn1p5Aqfs8E99LcdLyVWypzV5teudUX8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=cgC3b37nRAaoNtPJMqyC8gmJdeKktuPgP2bJlHGmDJvPC1gE_SeGeWAUprQqPnoH6kDCxsmrObDeQmfqsSq91x9ph7dFLUf8uMM4Ie8zcyPk0ndctkb3EnfUQaBkfdxk2K290yURUjohTqjaVXHsd0StTcRQIwC7bf5TKN-XkvDZ_B05eR1rWIjC0vT1A36wUk7vLQHUqQf6N5r_4H-TWAyC9Fn71c82v7UGelAz1klCEI_jbd9wqNQgAdexDvZGx_GQUOMt_TbjEvFpYb4yTBMCioy_UGcAD1rk_tLQheMOYvITB1MQcn1p5Aqfs8E99LcdLyVWypzV5teudUX8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا از حملات به چندین هدف مختلف نوشت: نیروهای آمریکا دور دیگری از حملات علیه ایران را تکمیل کردند
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۸ ژوئیه دور دیگری از حملات علیه ایران را تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
نیروهای آمریکا حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، محل‌های نگهداری موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
این حملات تازه در پی اجرای موفق حملات تهاجمی در ایران در شب قبل انجام شد.
نیروهای سنتکام در ۷ ژوئیه حدود ۸۰ هدف نظامی ایران، از جمله بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را هدف قرار دادند تا به‌دلیل نقض آتش‌بس از سوی ایران با حمله به سه شناور تجاری در حال عبور از تنگه هرمز، هزینه‌های سنگینی بر آن تحمیل کنند.
نیروهای آمریکا همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که از سوی فرمانده کل قوا دستور داده شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/76889" target="_blank">📅 06:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اکسیوس: با «پایان» آتش‌بس ایران، ترامپ به نبرد بر سر هرمز روی می‌آورد
ترجمه ماشین:
کاخ سفید خود را برای چیزی آماده می‌کند که می‌تواند به تبادل آتش چندروزه یا حتی چند‌هفته‌ای با ایران بر سر تنگه هرمز تبدیل شود.
مقام‌های آمریکایی به Axios می‌گویند طول و شدت کارزار جدید کاملاً به اقدامات بعدی تهران بستگی دارد.
چرا مهم است: جنگی که با هدف تضعیف توان موشکی ایران و نابود کردن آنچه از برنامه هسته‌ای‌اش باقی مانده بود آغاز شد، به نبردی بی‌پایان بر سر مهم‌ترین گلوگاه انرژی جهان تبدیل شده است.
یک مقام آمریکایی گفت تشدید تنش فعلی می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد؛ بسته به اینکه آیا ایران به حملاتش به کشتی‌های تجاری در تنگه هرمز ادامه می‌دهد یا نه.
این مقام آمریکایی گفت: «می‌خواهیم کمی بهشان سیلی بزنیم تا بفهمند ما شوخی لعنتی نداریم.»
محور خبر: دیپلماسی فعلاً متوقف شده و فشار نظامی دوباره در مرکز راهبرد رئیس‌جمهور ترامپ قرار گرفته است.
ترامپ روز چهارشنبه گفت آتش‌بس ۶۰روزه‌ای که در یادداشت تفاهم (MOU) ترسیم شده بود، پس از تبادل آتش ناشی از حملات ایران به کشتی‌های تجاری «تمام شده» است.
سپس آمریکا دور دوم حملات را در نزدیکی تنگه هرمز آغاز کرد، از جمله حمله به اهداف زیرساختی در داخل ایران برای نخستین بار در چند ماه گذشته.
ایران با حمله به پایگاه‌های آمریکا در کویت و بحرین تلافی کرد، در حالی که تأکید داشت از ادعای خود برای کنترل تنگه عقب‌نشینی نخواهد کرد.
کمی بعد، ترامپ علامت داد که آمریکا آماده کاهش تنش است و به خبرنگاران در هواپیمای Air Force One گفت مقام‌های ایرانی «کمی پیش تماس گرفتند» و «می‌خواهند توافق کنند.»
مشخص نبود ترامپ به کدام تماس اشاره می‌کرد و مقام‌های ایرانی نیز فوراً هیچ ارتباط مستقیمی را تأیید نکردند.
ترامپ اضافه کرد: «فقط نمی‌دانم شایسته توافق کردن هستند یا نه. نمی‌دانم قرار است به توافق احترام بگذارند یا نه. راستش را بخواهید، یک جورهایی دیوانه‌اند.»
طرف مقابل: مذاکره‌کننده ارشد ایران، محمدباقر قالیباف، آمریکا را به «قلدری و خلف وعده» متهم کرد و هشدار داد که تنگه فقط با شروط تهران بازگشایی خواهد شد.
قالیباف در X نوشت: «اگر بزنید، می‌خورید. تنگه هرمز فقط با «ترتیبات ایرانی» باز خواهد شد، نه تهدیدهای آمریکایی.»
تصویر کلی: بازگشایی تنگه هرمز و بازگرداندن آزادی کشتیرانی برای کشتی‌های تجاری، عمدتاً برای تثبیت بازارهای جهانی انرژی، به یکی از اهداف اصلی دولت ترامپ تبدیل شده است.
برای ایران، حفظ کنترل بر تنگه به یکی از اهداف کلیدی در هر توافقی برای پایان دادن به جنگ تبدیل شده است.
این مسئله یکی از بندهای محوری یادداشت تفاهم آمریکا و ایران بود و برداشت‌های متضاد از بندهای مربوط به تنگه اکنون باعث فروپاشی این توافق شده است.
این یادداشت تفاهم ایران را ملزم می‌کند اجازه عبور امن کشتی‌ها از تنگه هرمز را بدهد. اما اندکی پس از امضای آن، مقام‌های ایرانی آمریکا را متهم کردند که با عبور دادن کشتی‌ها از یک مسیر جنوبی در نزدیکی ساحل عمان بدون تأیید تهران، توافق را نقض کرده است.
پشت پرده: مقام‌های آمریکایی می‌گویند کاخ سفید معتقد است فضای بیشتری برای تشدید تنش دارد، چون صدها نفتکش در هفته‌های اخیر توانسته‌اند از طریق تنگه از خلیج فارس خارج شوند.
به گفته این مقام‌ها، همین مسئله نگرانی‌ها در داخل دولت را کاهش داده که درگیری تازه فوراً باعث جهش بزرگ قیمت نفت شود.
پشت صحنه: یک مقام آمریکایی ادعا کرد تشدید تنش فعلی ناشی از سرخوردگی عناصر رادیکال‌تر درون رهبری ازهم‌گسیخته ایران است؛ کسانی که معتقدند یادداشت تفاهم منافع واقعی برای تهران به همراه نداشته است.
این مقام گفت ایران می‌دید که اهرم فشارش در هرمز در حال لغزش است، در حالی که صدها کشتی از مسیر جنوبی نزدیک به ساحل عمان عبور می‌کردند.
با وجود معافیت‌های تحریمی آمریکا، ایران برای فروش نفت با مشکل روبه‌رو شد، چون مؤسسات مالی تراکنش‌ها را تأیید نمی‌کردند و کشورها تمایلی نداشتند به معافیت‌های موقت تکیه کنند.
هیچ‌یک از دارایی‌های مسدودشده ایران آزاد نشده است، چون ایران هنوز گام‌های هسته‌ای مورد نیاز طبق توافق را برنداشته است.
به گفته این مقام، توافق چارچوبی که آمریکا میان اسرائیل و لبنان میانجی‌گری کرد، بخش مربوط به لبنان در یادداشت تفاهم را غیرضروری کرد.
آنچه باید دید: این مقام آمریکایی گفت: «بخشی از رهبری ایران از همه این چیزها راضی نبود.»
«آنها شروع به تیراندازی کردند و ما تصمیم گرفتیم وقتش رسیده محکم بهشان سیلی بزنیم. این یک روند است. ما صبر داریم. اگر احساس نکنیم به توافقی که می‌خواهیم می‌رسیم، آن را انجام نخواهیم داد.»
جمع‌بندی: معاون رئیس‌جمهور ونس روز چهارشنبه گفت موضع آمریکا ساده است: تنگه هرمز باید باز بماند.
ونس گفت: «اگر تلاش کنند آن را ببندند، پاسخ ارتش آمریکا را در پی خواهد داشت.»
«یا می‌توانند از آن تبعیت کنند، یا دقیقاً همان چیزی را داشته باشند که دیشب برایشان اتفاق افتاد. این فقط ادامه خواهد داشت تا وقتی که آن مسیر را باز کنند و تیراندازی به کشتی‌ها را متوقف کنند.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/76888" target="_blank">📅 06:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rTevLNkRaK7iGqgFOXN2etJ_5HxrFzGu_D_R2ycUaHrqxl3CVgRU1SshIhuS4PteI0WvSrpoHvm3e3DiAEMKr-STe4cN7HW-mUw3FEIcJd1ixodpeoVtEXTpmgTLL0xbzUYrET6DbQ3wrvoSp_edTjLpOjuRPlt9TB52yRFziQIx6a6IvjP858nHuRLj75vOM04wHldJ5kahQJnM4kmFoc9ih3iSnJzQNeDesW7Qhy--MlQmArR0di_Y9B0Dv34qY__rmdNiHL_20mxRqQmucnLikgzSt0F2s5i2qddAmHABgxRZbDVuReUQKfU56K_SloC5QEpC97diD46KHiZDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای که از صداوسیما پخش شد، اعلام کرد نیروی دریایی و نیروی هوافضای سپاه در «یک عملیات مشترک پهپادی و موشکی، زیرساخت‌ها و تاسیسات آمریکا، از جمله اردوگاه عریفجان و پایگاه هوایی علی السالم در کویت، و همچنین پایگاه هوایی شیخ عیسی و منطقه جفیر در بحرین را هدف قرار داده‌اند.»
@
VahidOOnLine
متن بیانیه به نقل از ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
🔹
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
🔹
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید، سرزمین عراق حبیب، مستکبران کاخ نشین را وحشت زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
🔹
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی پاسخ نخواهند گذاشت.
🔹
در اولین مرحله از پاسخ تنبیهی علیه پیمان شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
🔹
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.
و ماالنصر الا من عندالله العزیز الحکیم
سپاه پاسداران انقلاب اسلامی
۱۸/تیرماه/ ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76887" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RtXv2A7dlpRoXHy1l72KM-IEzoaRT5YkpIxNbY0-2u7iRRee6Wj1tpmbmZj9g-3-f5VSsnyNpU0UUu4iCgYZAWxwXL89AjePbe_FbCEUDJQD_hbCgt40XdyuWhgHdmRS6Nco1v8UHgA6rYzMX7bfUseOwkPWQCK_EYOrP4WmPlVP4A24IXUW13QD-52BMg--9iHNnkCYhQDmGfjGNomb8xAYKR3s6xr_FG4EMGAS37dFFlCf-tiE52CdaAwl3dxJT0B9dk2exT1U8I3RBjHRmfMhda9TYEhixHb4Fm4dv72nUq5l1Yvu9mb1FeTcK-70aGNLBDE4TIvW9h8MvQ77jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی:‌ 'برج مراقبت ترافیک دریایی بندر
#چابهار
که چهارشنبه ۱۷ تیر  مورد حمله قرار گرفت.'
Vahid
چند دقیقه پیش هم دوباره از سیستان و بلوچستان:
سلام سمت کنارک الان صدای انفجار اومد
کنارک رو یه جوری سنگین زد از خواب پریدیم
۴ تا پشت هم
از بوشهر هم پیام‌های تازه‌ای می‌فرستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76886" target="_blank">📅 05:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=LOwqqQimEmNKsYn-XhInlc-Fgu_TYuklZ_Rh9m9P_Zi4sfSwu4oYU59L4l-eWoaXl1xqkNjuD62kURM8oFzl90NbQcgD2wMnvGnQyYOEZrg8sPhAdTOsUMFRbrf3JcyNPySDEnQ6V-I-3iGANpJTw6huErLoAELt_N141LMREB6dzxzG2zz1kGpP6vxbPgOhHURDxH4_bXHt1iE8smXg1LUW9TPWAEtpnVViGjGOmCvP9ARgsNQukqSHmj2urYqbjYwxP1_vrOnaRga3I9Pvkq1OKNS4PyaYLdQu3BpU9-zMHMi0uxWOOiMt4sBdKLSa2DuP2KID0I5IALZCXGeZTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=LOwqqQimEmNKsYn-XhInlc-Fgu_TYuklZ_Rh9m9P_Zi4sfSwu4oYU59L4l-eWoaXl1xqkNjuD62kURM8oFzl90NbQcgD2wMnvGnQyYOEZrg8sPhAdTOsUMFRbrf3JcyNPySDEnQ6V-I-3iGANpJTw6huErLoAELt_N141LMREB6dzxzG2zz1kGpP6vxbPgOhHURDxH4_bXHt1iE8smXg1LUW9TPWAEtpnVViGjGOmCvP9ARgsNQukqSHmj2urYqbjYwxP1_vrOnaRga3I9Pvkq1OKNS4PyaYLdQu3BpU9-zMHMi0uxWOOiMt4sBdKLSa2DuP2KID0I5IALZCXGeZTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد پنجشنبه ۱۸ تیرماه، در مسیر بازگشت از نشست سران ناتو در آنکارا و در هواپیمای ریاست‌جمهوری «ایر فورس وان» گفت آمریکا در برابر حملات ایران رویکرد «۲۰ به یک» را دنبال خواهد کرد.
ترامپ گفت: «همین حالا ضربه بسیار سختی به آن‌ها زدیم. هر بار که آن‌ها به ما حمله کنند، ما ۲۰ برابر پاسخ خواهیم داد.»
او افزود تهران سه کشتی را هدف قرار داد و تاکید کرد هر زمان حکومت ایران حمله کند، آمریکا «بسیار شدیدتر» پاسخ خواهد داد.
@
VahidOOnLine
پست قالیباف:
آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با «ترتیبات ایرانی» باز می‌شود نه با تهدیدات آمریکایی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76885" target="_blank">📅 05:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اکسیوس:
یک مقام آمریکایی گفت ارتش آمریکا در چارچوب حملات روز چهارشنبه، دو پل راه‌آهن را در شمال‌شرق ایران با موشک‌های کروز هدف قرار داد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76884" target="_blank">📅 05:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=DfIndH_SZ-5TI2jAoeh53xxZ5JKuV9JX_1zG5DOFuCPiWSA0B1_7Fn2obnxoludUWnz5uSea0f0IcndqhMYzzmXuX6Owl3dvlqmkLRGWtrPwTwKu1q2HDyrDH7BczDhRbMg4Mxq8HFxyIGyBeyVgfO9_V_AljExQUX8_ESfBEzaAMWyeMnltrxvNgYx9n1Q-jG7wXT0qRo9lxfU6Oml_vsoVaJogCTt7HkGcqyEFcF13yK-IGnr4I8ZRHDtXc5hhSb1OqvKdxT1c5Q8WfYOqbN_T_ERDmKnINHSxteJReJ7KdqaegfXuAIgRvsJFFRReTkvL6HJlJsXycRo5IyJd2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=DfIndH_SZ-5TI2jAoeh53xxZ5JKuV9JX_1zG5DOFuCPiWSA0B1_7Fn2obnxoludUWnz5uSea0f0IcndqhMYzzmXuX6Owl3dvlqmkLRGWtrPwTwKu1q2HDyrDH7BczDhRbMg4Mxq8HFxyIGyBeyVgfO9_V_AljExQUX8_ESfBEzaAMWyeMnltrxvNgYx9n1Q-jG7wXT0qRo9lxfU6Oml_vsoVaJogCTt7HkGcqyEFcF13yK-IGnr4I8ZRHDtXc5hhSb1OqvKdxT1c5Q8WfYOqbN_T_ERDmKnINHSxteJReJ7KdqaegfXuAIgRvsJFFRReTkvL6HJlJsXycRo5IyJd2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی پخش شده با شرح: 'بوشهر آخرین دقایق چهارشنبه ۱۷ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76883" target="_blank">📅 04:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YhyYelWS4QIADluPziWb-Y0Ynp9ehnLnPW3Y6AMVxCfzv9W9Qs0EtilA6Nq8KMFw5MOJEiNAdiJBM8rw4xfYidBbPN3Z_h2_BLVJ4lYBCF8Ck4fwKJQsT9ddbGXmF0bfHuUtzzgGJyaGTac_URh-J7DwLk6TwNiaWxCNgJENtJEVAt51Hm6LIjNKy55je3Bu_Ihco0Ns1n3fP3FrvTlfGJlKuEDZKsXiGgSVsE5EBbPr2PEOXlV-q2DwYDqFnrjKEWdp9ThboHRyCOqq2quSrCI4PggrEpNc5cpD5DZgXw2EpdbR24Ovb-PSpGGtRBxN3YC3r244xEEs_USs-MhssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی پیام درباره شلیک موشک از اهواز و امیدیه در خوزستان
و هم‌زمان درباره اعلام هشدار در کویت و بحرین
در خبری دیگر:
برای  نخستین بار در نزدیک به سه ماه گذشته چنین پیام‌هایی برای ساکنان قطر نیز ارسال شد.
قطر همزمان از میانجی‌های مذاکرات تهران و واشینگتن است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76882" target="_blank">📅 04:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=Y6av12c0uPx7ShHCXI_1H7n9mpNOzCM5tV4aAxht9d6_OURazQwCoy9rCT3NUUOaZzcQJR9fhEbZ5NEmgihC_0BR2wa-UUn20U2qnw0W_NpCc5N_9eYyA6j38nuDaXXLnYl3ktgLFYhSXdoKNjz3T2y2vv4TRG1Ltm4l9idIxnqAgUJ2zEDoDOLpRskkHV1YVyEvsjlsELCU13_-Hk6VqKHESeBZxArPO5JYv8n5P6Dmhxo_pXQLAe3FnP8dpE5_ygxGl4dtNZDI7uVkH33P-KWfBd3SS0LVFyFfge9IygT2TvkPAXt-uzhv6PDLt9QECBV0oTyVTDmEOiurRRM8AA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=Y6av12c0uPx7ShHCXI_1H7n9mpNOzCM5tV4aAxht9d6_OURazQwCoy9rCT3NUUOaZzcQJR9fhEbZ5NEmgihC_0BR2wa-UUn20U2qnw0W_NpCc5N_9eYyA6j38nuDaXXLnYl3ktgLFYhSXdoKNjz3T2y2vv4TRG1Ltm4l9idIxnqAgUJ2zEDoDOLpRskkHV1YVyEvsjlsELCU13_-Hk6VqKHESeBZxArPO5JYv8n5P6Dmhxo_pXQLAe3FnP8dpE5_ygxGl4dtNZDI7uVkH33P-KWfBd3SS0LVFyFfge9IygT2TvkPAXt-uzhv6PDLt9QECBV0oTyVTDmEOiurRRM8AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی و تصاویر منتشر شده با شرح 'انفجارهای حمله به آق‌قلا در استان گلستان'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76879" target="_blank">📅 04:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AIMWqof0_0jfR4w8HZbHHkkwkj4R9_zjiyjPyxRL-9LJMebwHWBZBMbLZeZHGNM0RScLQwqUUjfe9A1BEX1bN2F4tkOPaQtXoJhm5q30tRnWLnm1ynAA7qu1_RNJk1s2wlcfYBX-etyPHf2q_VSNMoZClbfvx1XZIaRjnCOdcyn2myYVWfOeFynGJtStgjv7c8nUvKEeZez-R3-Ba20ZHeXknsaikcAtYqxv8GoRWoN6ubJGSiyWmULxq38EiqKVjjgN0i70C_II_EY5Ayk_eonP7cuZiII0IJyfybjzGWnS-TWslGcLzFJa1M0aKsFu4pbTUKge1xg_8H1rE2ZVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=RijvKzIQoh7QQe4V0FpK__BnaiRh4vdM9l_gRxkAYIWqthzfWkf_i5OuZlEUVOoZCKkW5tyq37tNOzrI-O4D4bi6YkQ4tjDLuWoREUtIe1AdXKX9xZDKdrFEB3FtlBJZjpDn0vBSI1W-sEAnuCVHTNF0npKHy9jDr8v_wju3QlyLYyz47kfkPQAZpAP_biS0jKj1LFWBHB3A0VVbR_3ikILIjcgGbroDQGgjiWEGPfqOnWD4lmZ-GUQUOGNc1cuE8XlhEl7RqdB9uzWNVgYyU7Pt6CLLs6fKG7vFCzOOETV1wA3RmwNZc6IjhBPcvWSw10AJkhKAakkJsEiMluwapQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=RijvKzIQoh7QQe4V0FpK__BnaiRh4vdM9l_gRxkAYIWqthzfWkf_i5OuZlEUVOoZCKkW5tyq37tNOzrI-O4D4bi6YkQ4tjDLuWoREUtIe1AdXKX9xZDKdrFEB3FtlBJZjpDn0vBSI1W-sEAnuCVHTNF0npKHy9jDr8v_wju3QlyLYyz47kfkPQAZpAP_biS0jKj1LFWBHB3A0VVbR_3ikILIjcgGbroDQGgjiWEGPfqOnWD4lmZ-GUQUOGNc1cuE8XlhEl7RqdB9uzWNVgYyU7Pt6CLLs6fKG7vFCzOOETV1wA3RmwNZc6IjhBPcvWSw10AJkhKAakkJsEiMluwapQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'شلیک چند موشک از جم در
#بوشهر
پنج‌شنبه ۱۸ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76877" target="_blank">📅 04:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=vckVRUow-WP8amXCXWmGcxG1_vLg9eurRFlIFN3Cny-rod_bvkIRC7bP5hLC7yeMfW0i7_gAzWy8gdPBvhKBlhE5xAov35aZFdpVyhN-0hw8GhrYGfHqqnIWd55Bocc8ronNoBU7H3UUM4_3CfR1wT8QjkB7bO-vohRaRC9MBy2Zw5DK9zj24_Ui-jsj-YdTgUlS2FRouZAwJ5A9T5oeQCSAz6leg2LZmi-7pTDsELrvzt2YWckgUfpcgdta_UcjLjKbWrLRjP7GNYt9zfxUTHtpLNwopfy6q47Ynx1bUarAshl-tbFkEFovW6hvNvyXs0zFRaYvLV2ppjxa1_pgHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=vckVRUow-WP8amXCXWmGcxG1_vLg9eurRFlIFN3Cny-rod_bvkIRC7bP5hLC7yeMfW0i7_gAzWy8gdPBvhKBlhE5xAov35aZFdpVyhN-0hw8GhrYGfHqqnIWd55Bocc8ronNoBU7H3UUM4_3CfR1wT8QjkB7bO-vohRaRC9MBy2Zw5DK9zj24_Ui-jsj-YdTgUlS2FRouZAwJ5A9T5oeQCSAz6leg2LZmi-7pTDsELrvzt2YWckgUfpcgdta_UcjLjKbWrLRjP7GNYt9zfxUTHtpLNwopfy6q47Ynx1bUarAshl-tbFkEFovW6hvNvyXs0zFRaYvLV2ppjxa1_pgHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای ویدیو: هوافضا ی چغادک بوشهر رو زدند
ویدیوی دریافتی، نخستین ساعت 'پنج‌شنبه ۱۸ تیر'
Vahid
📍
گویا اینجاست:
GoogleMaps
via
Mitch_Ulrich
🔄
آپدیت:
پیام‌های دریافتی الان دوباره ساعت ۳:۳۵
بوشهر دوباره زدن…
همین الان پنج تا انفجار بوشهر
سلام وحید جان ۳:۳۸ صدای چندین انفجار، بوشهر.
سلام آقا وحید بوشهر سه دیقه پیش صدا انفجار اومد
🔄
آپدیت:
بوشهر رو خیلی بد زدن.
ناحیه‌ی بهمنی، چهارراه ریشهر.
ساعت ۳:۵۵
سلام
بوشهر همین الان بازم زدن سه چهارتا پشت سر هم صداش خیلی بلند تر از قبلی ها بود
۳:۵۶
وحیدجان الان ساعت 3:55 صدای 5یا 6 انفجار پشت سر هم اومد، احتمالا از پایگاه هوایی بوده
سلام وحید جان بوشهر الان ساعت ۳:۵۵ خیلی شدید زدن پایگاه هوایی رو
دوباره صدای انفجار اومد بوشهر ساعت 3:55
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
بوشهر از ساعت ۳:۲۰ تا الان ۳:۵۵ کلی صدای انفجار میاد، ۳-۴تاش خیلی صدای وحشتناکی داشت!
الان بوشهر ضداى انفجار ٤ ٥ تا
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
چند انفجار هم بعدش شنیده شد که بنظر دور تر میومد
🔄
آپدیت:
بوشهر ساعت ۵:۲۲
صدای دوتا انفجار پشت سر هم اومد
۵:۲۲ بوشهر رو همچنان دارن میزنن، احتمالاً پایگاه هوایی
سلام بوشهرو زدن
الانم صدای فعالیت پدافند و توپ سنگین میاد
وحید نیم ساعت پیش صدا انفجار داخل بوشهر اومد نمیدونم دقیقا کجا بود ولی خیلی بد بود صداش
🔄
آپدیت:
دوباره الان صدا اومد ساعت ۵:۵۶
اطراف محله بهمنی بوشهر ساعت 6:01 صدای دو انفجار مهیب شنیده شد
ساعت ۰۶:۰۰ صدای انفجار مهیب در شهر بوشهر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76876" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R9qJTzaVEMu_QMAYA-SnV0MqzzXF6JXyI8zCvXxFTkDEXrgz15liXY9RIF_-dlOJ4s_hv4XKomsRov30R2D5gA5EdpGUOfCSiPSiqj10GAcicgS4G7rr5I6N9RxnbapuPb-Fw3BZ7o08xfq_IFURwaCdbgHWli2EvIBPw0x3F6fUhw51MgsNeFUI0DFPeJl4dTmIZlpbsiv6RW0iCPUAORJralw76uPNBiH_y5IJg_vFzulrWJlbAbgifeDMykLxmIf3o2k-10J6AthcybuuNLGgMpukf4KxPEMHP3KJbL3v7AKzxMsQAQ4Itao9nj1W6qMyfql8Z36Fv6hCsuN_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uz18J0HlQ8wglVU97RzuQQXaEp3yEDDmBuD-3rf10tJdr-FnPl5phqHwZexIJXZiYVSTB6zCkEluUW4lwJlxWb1Nx9Vz9zE2sdT5C8HcCXIK48oWrGMWQYdRUQaZvKleN5YNLGbsi1TFtEzUuGp2sC0-3druppNrQRdRHgwrAGe7ulyn-H6-zFkvZhby1OEBO9_nyqK9Nrak5gIlj-jP3UzhBhnOIRH3XwMsorEWG3FbOrMI-4iPaHgBZHndjGuaOGMHe_aIPDvS15Q0lCmN5CBvyRcqEiKWT2tq3t3GGkexGQaHWAePjftr6iI2K2h5MBQlb9hN1Wk8QHfKh4uudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YPX2vAOpbrfhLOIysU-c5S0nHOA4C5XmR_j6nsl1ExtL3NEJuxJMQwzzYWsczmkoMooCKnDHWXFZkQDr6N5-n0XrrCO_vq84uXBvK2VuxwKiUfgb5ujHvN_KLpnHE7YJK5OcJ47fQCNvqcp-bWbxMXACphbSHBndB-K10jZgaiWMI1Qlrc4u0JpScOtf1MMCZlGjf9bwSOlupAki8r4Ppa3WjC-ewZ6QcVkJSGhwaQHyUD6o8Quc0gmQ_leEnyjOtb2LQBPLdS-gOgMq74kSeRJyiXkdhdxpHYQgF41oQv4xjR6UQfAuUbeCO9nlPzOFiJcG3xHQk3gwT_AHaN6GGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=P0tG9LtfUDFE3G6IsATe01nBdu4uJcaQpQNHgx_A_Df1G_hkXUcJplDQM14ThshNspCsAVgOVjQQGC8y9o-ZIlSTh5CFNXgLv3F5A_ai9nTCkBS338l4Sglj6gF-hDOngy6fm4Mwl2WKImffK2zRPXmVnNgWDMgtbo2-wnOYrx3GmRg9W8I4D1jNafKXgLzqXpbB0mLcC_h3g3lwIOuv59l13eGZ69gDsVry3oNFOVcx2JSHV7xB_alGAhZVmEJ-8zPWaPiyDrfkZjovMm8LLHqOscoQxiythcp511Fx2N_iwqwC4AQRcL9rMSIoGUYNyLFDEpIfVMLDXBhJdulFvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=P0tG9LtfUDFE3G6IsATe01nBdu4uJcaQpQNHgx_A_Df1G_hkXUcJplDQM14ThshNspCsAVgOVjQQGC8y9o-ZIlSTh5CFNXgLv3F5A_ai9nTCkBS338l4Sglj6gF-hDOngy6fm4Mwl2WKImffK2zRPXmVnNgWDMgtbo2-wnOYrx3GmRg9W8I4D1jNafKXgLzqXpbB0mLcC_h3g3lwIOuv59l13eGZ69gDsVry3oNFOVcx2JSHV7xB_alGAhZVmEJ-8zPWaPiyDrfkZjovMm8LLHqOscoQxiythcp511Fx2N_iwqwC4AQRcL9rMSIoGUYNyLFDEpIfVMLDXBhJdulFvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تصاویر با شرح پل راه‌آهن در نزدیکی آق‌قلا در استان گلستان دارند دست به دست میشن.
آپدیت:
منابع حکومتی:
براساس گزارشات منابع محلی اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر آق‌قلا در استان گلستان گزارش شده است.
براین اساس حدود ساعت ۱:۳۰ بامداد هفت پرتابه شلیک شده که دو مورد منجر به انفجار بر روی ریل راه آهن  شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76872" target="_blank">📅 02:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vWoGFmcThcg-iIW_3yvPoVD3h2VmCGgbPsYsW3DEE5fe73H66C3sZ1LaiPIRD-fLn4GCyQ4e8XFNfV8YWJLh7GGDXw5c-bBBmg_WH93ylUB-aJPQj4Hf_-f8nIh0Jf-0oeVXGJnUID93MtSu8z2bu43qn6h0RGGWIyTPqd5SIrpGdq-SjBgplLWittglF5QYQeZbwW1CMdSotLzQWSzRF9amYuvwmPDKsY8M4z4XmjGfbgzZVKVYwXUXFXJalsc9EGru6el-LVj08TfWlTJW2kaTcNbkvq4Y6Whj_-5PxuZpdhbm9eta0VfH1qOKsih1tgia_GZ9VgxbzZ3HWj6zfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در نخستین ساعات بامداد پنجشنبه گفت که حکومت ایران پس از حملات مکرر آمریکا در منطقه با او تماس گرفته و خواستار دستیابی به توافق شده است، اما او نمی‌داند آیا تهران «شایسته» توافق هست یا نه.
ترامپ در گفت‌وگو با خبرنگاران در هواپیمای ریاست‌جمهوری آمریکا، هنگام بازگشت از نشست ناتو در آنکارا، ترکیه، گفت: «آنها کمی پیش تماس گرفتند، آنها خیلی زیاد می‌خواهند توافق کنند. فقط نمی‌دانم آیا آنها شایسته توافق هستند یا نه.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76871" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
استان گلستان آق قلا پنج شیش بار صدای انغجار و نور شنیده و دیده شد
سلام وقت بخیر ، استان گلستان هم زدن ، بالای پنج بار صدای وحشتناکی اومد
سپاه شهرستان آق قلا واقع در استان گلستان و حومه شهر گرگان رو هم زدن
سلام وحید جان
۵دقیقه میش گلستان رو زدن
شهرستان اققلا بدجور لزرید
۵بار لرزید ناجور
سلام وحید جان
شهرستان آق قلا بدجور زدن و مکانشو نمیدونم
کل شهر ریختن بیرون
سلام آق قلا صدای چند انفجار و نور رو ما هم شنیدیم ساعت تقریبا دو بامداد
۲بامداد چهارتا انفجار پشت سرهم آق قلا استان گلستان اخری صداش و شدتش بلندتر بود نور یه  لحظه دیدم ولی کجاخورد رو نمیدونم احساس میکنم دور بود سمت گمیشان رادار داشت قبلا
شاید باز اونجارو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76870" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fb2iNwlBLRnacvHiZzo7A1qrgiSowRJNJ-BrERT_H93metbAj2PEbj5l1o-HxovurbpRBXy4EoFNGfWxQm-Tyub5Uet8QUJ7rxDnkXshR8ounNn_MoPvapC4XwklmS88lQ3oMnZcOTvcZtns3eByQLesqWqQTMDZ3bTpD3zoajpoM5hN7gZ9czTsSk2ra7DvpJdOuOsTbHUGc2geiLEDC3zps0tzmYx77Y4kk2UogZueM4HzMH-km2QNUQoUddvOx9_N-DpCoRKYy9PXM7hbiRrtHMGxRom_rPRB1cAGW8yBkM28y3mUm6oS8e7oByHf-3Ff3jc-JEKDrneRif_NgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f66b394713.mp4?token=JfBhiK4VL8w-X1ygTHFOeI6odhVNfd7_GfB4dLIY2LuU0cXcAzYDxISaJ7Hqt7Jcc79LXOnGHawXaZBZ9sWsRywZcg6CwOuxAnPBFHT5od7Q76OzawNPVaCYZQv7j3zFhyVQwIXrC09ZjU0gGq5yPMfVZ46rQiDYuXkBZeCWmKFhLtop-KKv0sUzJ1kohJ4urT0fD2D_JWBX5JDwWqlh2NoZlcM5d9aei8cnMozsMaDQGnIG5pMbyP6XWdIjnePJM54grsKBFp8V2vE90tlueXV2EVY2jealtolSaKAUf6ewAC88VeCptXJkp0qR53_Clmcl_sAnVl8yHCr0k4YQuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f66b394713.mp4?token=JfBhiK4VL8w-X1ygTHFOeI6odhVNfd7_GfB4dLIY2LuU0cXcAzYDxISaJ7Hqt7Jcc79LXOnGHawXaZBZ9sWsRywZcg6CwOuxAnPBFHT5od7Q76OzawNPVaCYZQv7j3zFhyVQwIXrC09ZjU0gGq5yPMfVZ46rQiDYuXkBZeCWmKFhLtop-KKv0sUzJ1kohJ4urT0fD2D_JWBX5JDwWqlh2NoZlcM5d9aei8cnMozsMaDQGnIG5pMbyP6XWdIjnePJM54grsKBFp8V2vE90tlueXV2EVY2jealtolSaKAUf6ewAC88VeCptXJkp0qR53_Clmcl_sAnVl8yHCr0k4YQuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر گزارش داد صدای چند انفجار در منطقه شمال شرقی «ایرانشهر» واقع در استان سیستان و بلوچستان شنیده شده است.
این خبر هم‌زمان با ادامه حملات آمریکا به اهدافی در جنوب و جنوب‌شرق ایران منتشر شده و جزئیات بیشتری درباره محل انفجارها یا خسارت‌های احتمالی اعلام نشده است.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
سلام شهرستان ایرانشهر روزدن
سلام ایرانشهر هم سمت فرودگاه زدن
سمت ارتش ایرانشهر انفجار شده
سلام ایرانشهر سیستان بلوچستان ساعت۱۲:۵۹صدای انفجار میاد
فرودگاه ایرانشهر میگن بوده خودم ندیدم ولی صداش خیلی شدید بود
سلام ایرانشهر سيستان بلوچستان همین الان ساعت ۱۲:۵۰ صدای شدید انفجار و پنجره ها لرزید.
فرودگاه ایرانشهر
پنج دقیقه پیش سه چهارتا صدای وحشتناک تو ایرانشهر(بلوچستان) اومد در حدی که شیشه ها تا مرز شکستن رفت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76868" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cw25DYoe8NuTZnqUtR0tl-WQuP3YsZ49mvyWPtBpMdn3wAS7UguVUuHW_psy42TokZRi6uL1BSER2PjoXXYlApR5KWoNOqUxWnIW2y5pk7NoQ-WNnmgG_qVvNMJ2DTFUKwNISsbkXY3ke6EXpqW0QNGzpURMGlCL4xKpRn6O9o-2nXBBz0X7cfk5XhrXToB1FrkGRCTzo1KQsIueXvFuXa_1KLfgssKuJG8Yp6-x-Zet83dYmDmUcIjcyB2msiqLLapwdBLjgWWDi2xZHSAOMWZkmPm7oyL0X49QwH6wcQ7ACO9MHFuDedpoLQbXPUiz5zNwMccin-RN40F2-QcELQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته "این در تلافی بمباران دیروز کشتی‌ها توسط ایران است. اگر دوباره اتفاق بیفتد، خیلی بدتر خواهد شد!"
بیشتر از ده تا عکس و فیلم با شرح حمله امشب پست کرده. حتی عکسی که اشتباهی بعضی از منابع پخش کرده بودند:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76867" target="_blank">📅 01:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=kceGpUkpg69iQJ40BPlBcFUxOjaQw8hgWQM4ov5KnsZ93HTpQLODKsxh0iw7HvKDe69faUuEYYcC4UsszGY79-DbZFSgmaKiymPQXE_ff74JH6ckOYN98y1K8yRlx6xux-IJA9ni6uByYAx5_xCI5xNLCdCVSfJLR5px1kAL52Wr8FeIG06Tcddf8jscszEfUIRR1o6MXRGYM4sVTogrhdXimJtHTJCKB4MOtK051C4HRNuKskbWbjVpZwcl44rvM-lGxziu9QTgBP6NAK793JhNCSS-8IR2K-_k-UlWVKmfg8iUhLAV7Q7ViTaFjCKJIqzp6oOfSaP5sbZUN2PsHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=kceGpUkpg69iQJ40BPlBcFUxOjaQw8hgWQM4ov5KnsZ93HTpQLODKsxh0iw7HvKDe69faUuEYYcC4UsszGY79-DbZFSgmaKiymPQXE_ff74JH6ckOYN98y1K8yRlx6xux-IJA9ni6uByYAx5_xCI5xNLCdCVSfJLR5px1kAL52Wr8FeIG06Tcddf8jscszEfUIRR1o6MXRGYM4sVTogrhdXimJtHTJCKB4MOtK051C4HRNuKskbWbjVpZwcl44rvM-lGxziu9QTgBP6NAK793JhNCSS-8IR2K-_k-UlWVKmfg8iUhLAV7Q7ViTaFjCKJIqzp6oOfSaP5sbZUN2PsHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'همین الان پایگاه نظامی بین چغادک و
#بوشهر
'
پنج‌شنبه ۱۸ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76866" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RXMZOZyCwrVZxB-mbABixj_eLCYf99d2dfrTV0U8S2RCq7xjTMPbxld9HL8KhA16krnqgEXy48WSjqWm0RMaKK6n3MqY-Fo5ftfTT0WN-AxVx4ZifJMmVedbS1dEEl4PmJQdkE4UHapjqdVDfGS024mZprstG9TqGKMierWJq0IaZbLF974n9tQ7ZKMSjSSxR1TvgFuistuuSjO43h-Bv1fjfGMoLj0yLZcYt4Vpcmh1JG0MYAtw74eitJOOVhVRHeN2PHYRukwjBvlZbLgpkqEtROb2jB_Q2QAaaujYAS6a2btqAxg04_13L7NnghHYUVfzGHOEoHVQpPxXXB77-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tUdidF00tTZkBhDm6adenmxKL7rSz_KN8KaEzWlWct35s5NVgyeF9wIki553OmKxVbjOUOcafdYj9RQ6f0k_vS7ptjPm1lQDDo4yEZQXCOMDgmKhhX5vQk45yanrJtWpNQUfl3Oly5mgRw_1HUNUPuiFJT-Q4s_VmsxkEv60_169MqwXS72FssizZC1cdVuCdJS-7Zpl_rcOlbiihMjLh2zIG0mX596SXG5GpcixEvfg0_nwdRhK_ixOYWPECU4W5yPHjuazo3XlhfsGTNmftNIQFJBwMRpD5ruERclGfViHu9s1GkZiCrwFE51DkCtNysf0ROCQjcESmsG1253I5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=DegoHbPJ1zMz0p-d3fPAXvIjX4BpG0KL0c0juWSsOsWIeO95UGOXlz0NuCrj4xSzZ9Vp0PeRxpATagN4PRRIBMDHjzLELBc_c3RVnwOenef8ABlpGlcvRGQvdPBZ2uJQJOIdLQdU3u_3zbDWdPQeM39R6gnkAPhMv8zJkXMImeDY1TSF-Ds_FiNhp2zgJRyehjCPDGnrBSu7I8-lkUXqHIUcqGyFH7zGOYq4CvRYyzHw0_XA4ja438jZWVSWYuQRwp598vtObz3oq9PsTpkK5D5JRkoSRQA1WLte2pFj6DwGFwEyaJYBz9GYWtDV2jYSeJJU6VTDcYPL7EamDOOdgw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=DegoHbPJ1zMz0p-d3fPAXvIjX4BpG0KL0c0juWSsOsWIeO95UGOXlz0NuCrj4xSzZ9Vp0PeRxpATagN4PRRIBMDHjzLELBc_c3RVnwOenef8ABlpGlcvRGQvdPBZ2uJQJOIdLQdU3u_3zbDWdPQeM39R6gnkAPhMv8zJkXMImeDY1TSF-Ds_FiNhp2zgJRyehjCPDGnrBSu7I8-lkUXqHIUcqGyFH7zGOYq4CvRYyzHw0_XA4ja438jZWVSWYuQRwp598vtObz3oq9PsTpkK5D5JRkoSRQA1WLte2pFj6DwGFwEyaJYBz9GYWtDV2jYSeJJU6VTDcYPL7EamDOOdgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر بالا با شرح
#چابهار
پخش شده‌اند.
در خبری دیگر:
خبرگزاری تسنیم گزارش داده است که جنگنده‌های آمریکایی پایگاه امام علی ندسا در چابهار را بمباران کردند.
تسنیم اضافه کرده که تاکنون صدای حدود ده انفجار در چابهار و کنارک شنیده شده است.
برق قسمتی از شهر چابهار نیز قطع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76862" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=lU3tvoMawea-7tSHXqpR3fCmiW3diVro4y9xuUzyMB0mAjzqGN3_jKrlSLLFddyZzwA8lXg0KZbEzaQxLagbcOWB3svVYqGy2j9VaU8G5EaGI9IbRCTDcA0SJSieZoxVtatEGxyOu1hVMXGcB1umP1AeTSx1V0Tv108CR6coPSKcbUzr4B0KecGKH-J_y2hQVRgWbJtO_JpBLq0-u2LRtImGjBZyl9FUC9O4w4iHxp27xcMeS5v_FfPO-TD3-eR5Zu5vkFCXHqtrL0qg2_vMJXq3CybfqJiJCHL3z7JaJs8AoJx4OfOX4MEq_49L-3JSVCsq2SBSq7znKEmO9RfLIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=lU3tvoMawea-7tSHXqpR3fCmiW3diVro4y9xuUzyMB0mAjzqGN3_jKrlSLLFddyZzwA8lXg0KZbEzaQxLagbcOWB3svVYqGy2j9VaU8G5EaGI9IbRCTDcA0SJSieZoxVtatEGxyOu1hVMXGcB1umP1AeTSx1V0Tv108CR6coPSKcbUzr4B0KecGKH-J_y2hQVRgWbJtO_JpBLq0-u2LRtImGjBZyl9FUC9O4w4iHxp27xcMeS5v_FfPO-TD3-eR5Zu5vkFCXHqtrL0qg2_vMJXq3CybfqJiJCHL3z7JaJs8AoJx4OfOX4MEq_49L-3JSVCsq2SBSq7znKEmO9RfLIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'
#چابهار
، انفجارهای حمله ۲۳:۳۰ چهارشنبه ۱۷ تیر'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/76860" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پیام‌های دریافتی:
چغادک بوشهر رو همین الان زدن چند تا انفجار خیلی شدید
سلام ساعت 00:28 دقیقه چندین صدای انفجار در بوشهر شنیده شد
00:30 هوا فضای چغادک 15 تا صدای انفجار
همین حالا بوشهر زدن
حدود پنج تا شش بار خونه لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76859" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76857">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sG99n_wWRbdnCVBEqAuQXyuv2tMdCyhC4jDUr8VtnbcG4cGttnOkHo33M2accrVEE02-UKet-6UEVyS4LO6TJ4cM0z1Jhw2BOXFdoEFKZDfTeiBdKG8dvlhzO0MzuLfRoD5_eAeBy2haqKmiYKCoKeROAvNSQa-6ra6EmjS22-qvOwg0qqfM26ZNS9QIepSDojJN4C_MtZOuMUxKQt8AVmfPTx6ICke1bWeSyLRNjn11lZIQeENA2VBJdMzlcFNGHCDQe2dzlTySm72_h-YwVtt6QIXJuUR52IvyV6afdZLgRsB6YK42UAMULAaOdXyRp_24W2EBC8HierjFKoUPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=tGFp9hJnGTK78w79pfYzZSqDKH8N-ALde32YkIsvMasoH_UEq_BqxDJLw8xJuroGdJL1CBCC2Pqhj_j0dnS-myULF8C-x_n20XDN9S4egceDUgB-BJVin11JQl2IV2fnFViSSFPm7rsH3jCJgwRhBmfx8ArTECRHIrMaqYNXc8QETUVM5wYFvst6skM5PaRvessU7W-nIG17edBcP304uNjNpwPQ7Phf2Omf-vx3I32v6tr3EjbhVRnNngyMMEM6Azu28It5wgVLJNOSqjqBXNeMGv0QDwTUcyXkhvRWd_W8De7UKm4Gj3QU9nv4KlUUmcBFoFejD_7IkqmN5Y4qlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=tGFp9hJnGTK78w79pfYzZSqDKH8N-ALde32YkIsvMasoH_UEq_BqxDJLw8xJuroGdJL1CBCC2Pqhj_j0dnS-myULF8C-x_n20XDN9S4egceDUgB-BJVin11JQl2IV2fnFViSSFPm7rsH3jCJgwRhBmfx8ArTECRHIrMaqYNXc8QETUVM5wYFvst6skM5PaRvessU7W-nIG17edBcP304uNjNpwPQ7Phf2Omf-vx3I32v6tr3EjbhVRnNngyMMEM6Azu28It5wgVLJNOSqjqBXNeMGv0QDwTUcyXkhvRWd_W8De7UKm4Gj3QU9nv4KlUUmcBFoFejD_7IkqmN5Y4qlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون ریاست جمهوری آمریکا درباره درگیری‌های تازه میان ایران و ایالات متحده، با تشبیه تفاهم آتش‌بس میان دو کشور به یک «معامله» گفت:‌ «توافق اولیه‌ای که ما امضا کردیم این بود که اگر آنها از شلیک به کشتی‌ها دست بردارند، محاصره [تنگه هرمز] را لغو خواهیم کرد، اما ۲۴ ساعت پیش چه اتفاقی افتاد؟ آنها شروع به شلیک دوباره به کشتی‌ها کردند.»
آقای ونس با تاکید بر اینکه در صورت ادامه شلیک به کشتی‌ها در تنگه هرمز آمریکا ایران را نابود خواهد کرد گفت: «حالا، رئیس‌جمهور ما گزینه‌های زیادی را در نظر دارد. بدیهی است که من نمی‌توانم بگویم امشب چه اتفاقی خواهد افتاد، اما رئیس‌جمهور خیلی ساده به آنها گفته است، تنگه هرمز باز خواهد شد. این بدان معناست که نفت و گاز به سمت مردم آمریکا جریان خواهد یافت. به همین دلیل است که می‌بینیم قیمت نفت و بنزین شروع به کاهش کرده است.»
او گفت که تاکید ریاست جمهوری آمریکا بر باز ماندن شریان حیاتی مهمی در حمل انرژی جهان است و «این چیزی است که ایرانی‌ها باید بدانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/76857" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان شش انفجار در بندر جاسک
ساعت ۰۰:۲۴
سلام وحید جان جاسک رو زد دوبار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76856" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kAbF4KtK0ecu6SW0JBrhYCJmGHWBPqFSA2F07BxD0nQ-36Z1wHztJpwQ2H9aaw-OTYce_KE9QjErFV3IwOQDlnImnXsdKK0tT7jCKbWjw5dNEFCjt7qafHTVR-tRBzRxsccZElwvSf3V_NUttInwPKKL4ScXsKH2BSjWT7CM1Zjuvcty3gsIjHsWxKuzUQxxcQ3ZGgaPwZocqcYRDYMwlM4hWl9_r5rLa9PmTkZoGuYxjEg62yxUFOeWt9YBScL53nzHkmaaQo4GOVZgldxPFwyi2y8-hBeP_9z5kjHCwXjH0_OFlDS6KlhIymxTe7pASC_kreTsc_L0y1s0Ocu7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=OFvhuZjz6gP94kMFa-HGm0WheT2yADI6NY2rB4cOeEiT8Fuww8tdAmEvBTfXki0ZQR_L8eU4HJJVm7U4ULI7Vnxoa026yFftzSu3AAezhkzqSLRTI4orKjgbBwWdwV0BmCCo_ZY36Anrv7qneiP5_Z7jOX0UmPd3cQH8yso1j2CXOWNdDfC7GzNTK_qcSgrRpqECebOSzuofOL1Y3GZZdQFZ8dzh2xL59coKTFi_YiJZzqoUQ6YlqIhY-9t_QzddtruanKtHOCwjD9Pl9haRrYf933jV1uKt1y_EBvZph0Lxm7RxUGQMJY1q_YIGtlWTSeQdf6sLsS_NKUsFfFfzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=OFvhuZjz6gP94kMFa-HGm0WheT2yADI6NY2rB4cOeEiT8Fuww8tdAmEvBTfXki0ZQR_L8eU4HJJVm7U4ULI7Vnxoa026yFftzSu3AAezhkzqSLRTI4orKjgbBwWdwV0BmCCo_ZY36Anrv7qneiP5_Z7jOX0UmPd3cQH8yso1j2CXOWNdDfC7GzNTK_qcSgrRpqECebOSzuofOL1Y3GZZdQFZ8dzh2xL59coKTFi_YiJZzqoUQ6YlqIhY-9t_QzddtruanKtHOCwjD9Pl9haRrYf933jV1uKt1y_EBvZph0Lxm7RxUGQMJY1q_YIGtlWTSeQdf6sLsS_NKUsFfFfzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'بوشهر، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۴۵'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76853" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=Y-WkwrZGVCJXzChyBW2gWbval7HqS0F76WG7HIgr_z-ejNYso1_6KnDBlXlBnN0ZzkvYDAoIDatPkFmMw8FUvMHr6u8E0osKwf0wG792KMko4Cy071lfq4gnlc-1YetBtPSwjDlPB8EOqQPAbxEwnwpv70dc2N8DH46R0AjrvYk_IqQo8JXVvXJmT3H-A8aFKvk4cg3w4HEddNo4orx3mvHo7dq0aP-C6lVQ4Jp7FPOvyOwVzAQJh87U7x0bpfSkfJZCufFK2WoTWbqDp3J3xfq9NE1sVgNU1roiA-lHX0C-fOuoS4jANK0ztC5fyZDmOe_W2e-2FlIEbHIsucGXmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=Y-WkwrZGVCJXzChyBW2gWbval7HqS0F76WG7HIgr_z-ejNYso1_6KnDBlXlBnN0ZzkvYDAoIDatPkFmMw8FUvMHr6u8E0osKwf0wG792KMko4Cy071lfq4gnlc-1YetBtPSwjDlPB8EOqQPAbxEwnwpv70dc2N8DH46R0AjrvYk_IqQo8JXVvXJmT3H-A8aFKvk4cg3w4HEddNo4orx3mvHo7dq0aP-C6lVQ4Jp7FPOvyOwVzAQJh87U7x0bpfSkfJZCufFK2WoTWbqDp3J3xfq9NE1sVgNU1roiA-lHX0C-fOuoS4jANK0ztC5fyZDmOe_W2e-2FlIEbHIsucGXmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'چابهار، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۳۰'
لحظاتی پس از حمله آمریکا
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76852" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان بوشهر ساعت ۱۱:۴۸ دقیقه بد زدن
بوشهر ۲۳.۴۸ یک بار انفجار
سلام وحید جان
بوشهر ساعت ۲۳:۴۸ صدای دو انفجار اومد که از صداهای صبح شدتش بیشتر بود
سلام بوشهر الان صدای انفجار اومد
اقا وحید بوشهر همین الان زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76851" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار بندرعباس
باهنر
بد داره میزنه
بندر دوتا صدای انفجار امد
بندرعباس منطقه ۴ انفجار های شدید و پشت سر هم
بندرعباس ۳ تا انفجار پشت هم 23:45
سلام الان ١١:٤٦ دو انقجار با موج بلند در بندرعباس
بمبارون بندرعباس شروع شد وحید جان
ساعت ۲۳:۴۷
اقا وحيد الان بندر عباس صدّا چند انفجار شديد كه پنجره ها لرزيدن
ساعت 11:45
چند صدای انفجار بندرعباس ساعت 23:46
سلام صدای سه چهار تا انفجار شدید بندرعباس اومد
بندرعباس الان چندین صدای انفجار پشت سر هم اومد
سلام
23:47
صدای 6.7 انفجار از دور
قشم
سلام بندرعباس صدای انفجار مهیبی اومد
بندرعباس سه تا انفجار پیاپی و مهیب
صدای بیشتر از ۸ تا انفجار این سمت باهنر و اسکله اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76850" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pvbUgRtfbD-e2pdInrghStoEeZhjJGZExqGvnoZ9Ttc_XLv-8_ggqbuyrjRXBvIGFOMOmjlyBuUisdcTC9zUU_-Z7Wu8ijLkQruak-jSWBqFAXdUZA_8uiWMtIPQKwewH7A5s5w_I9G-wj6YRjNwSem1rsTGXUNXrGMbNAMF1HwNtXgYVU6g_HmjHRt-5fkSNxSE5qiOxj0rP4f9HaM_ANYU6kuTSDdLwURSqoCKbbq8R3X3Q3nE0Xegmh32S6EhlHFoAAENTxwL9qdij4QZCOeEgpalb_aONRa6KGSxPm3vuxmS5HzUP6l-znPMA3UnGhlrnVtvLOZmk2-8-T5cDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
به دستور فرمانده کل قوا، نیروهای فرماندهی مرکزی آمریکا اجرای حملات تکمیلی علیه ایران را آغاز کرده‌اند تا توانایی این کشور برای تهدید آزادی کشتیرانی در تنگه هرمز را بیش از پیش تضعیف کنند. ایالات متحده ایران را بابت تعرض بی‌دلیل اخیر علیه کشتیرانی تجاری و خدمه‌های غیرنظامی که آزادانه در یک آبراه حیاتی بین‌المللی تردد می‌کنند، پاسخگو می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76849" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
صدای انفجار چابهار
فکر کنم کنارک بود
چندین صدای وحشتناک  10تا بمب زدن
۵ تا صدای انفجار شدید اومد
چابهار
داداش الان چابهار رو هم زدن
7 و 8 تا صدا اومد
ما تو روستای رمین هستیم برقا رفت و صداش اومد خونه لرزید
سلام کنارک وحشتناک صدای انفجار اومد
چابهار زدن چند تا انفجار شدید
ما کمب هستیم واقعا درهای خونه ما بشدت لرزید
صدای انفجار از زمان جنگ هم بلندتر اومد
دود غلیظی بلند شده که تو شب هم کامل معلومه
از سمتی میاد که پایگاه سپاه اونجاست
البته ممکنه نقطه زنی باشه
الان 3 4 بار دیگه صدا اومد
جدا از اون اولیه
مجدد زدن با جنگنده
فک کنم اسکله سپاه بود چابهار بود صدا نزدیک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76848" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
