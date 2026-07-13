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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 08:01:41</div>
<hr>

<div class="tg-post" id="msg-76994">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 143K · <a href="https://t.me/VahidOnline/76994" target="_blank">📅 06:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 150K · <a href="https://t.me/VahidOnline/76992" target="_blank">📅 05:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 143K · <a href="https://t.me/VahidOnline/76988" target="_blank">📅 05:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 141K · <a href="https://t.me/VahidOnline/76987" target="_blank">📅 05:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 156K · <a href="https://t.me/VahidOnline/76985" target="_blank">📅 04:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/76980" target="_blank">📅 03:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76979" target="_blank">📅 01:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76977">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76977" target="_blank">📅 01:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WRFjvEWNF5urDLBZdZAltarhyWf4gjKemV4x36qUogKkBYfh6LNzXpveWweUPRzLMcOjwfT4mLVxqWoFyJJy69xU5R6MkxsG7jun7LNpBycp9211vr-IKP50KlD2bAjjwsGy0dYX8f9XxJ0O37wy_0E3onrkmEJ0f_USmi5pn7JNBus82tXRNv6YTMF9d84FaP3JsLqy4ebU2bNfG-sLtVGWOLSNEUVsjOJM9d7AHcxnEeiXhdBNaBk8dqdOCM0dgdcU4bt4y7QyP8frWg3aUruh-gVf8ppwa6CV5Mxv8pYIi7s-tr7WSH6JbI3Hlj6KsLfyQIPoj14_q7CEHb6-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت سنتکام:
ساعت ۵ عصر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به تضعیف توانایی این کشور برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند.
فرمانده کل قوا دستور این حملات را برای پاسخگو کردن نیروهای ایرانی صادر کرده است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76976" target="_blank">📅 00:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76975" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76974" target="_blank">📅 00:19 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
