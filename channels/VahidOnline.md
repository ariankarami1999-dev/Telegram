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
<img src="https://cdn1.telesco.pe/file/VCnuBJjL4Fx_GtBtZoCzBZgQFurfBT4kEczeQ05ZLvksmH3ysHB9F1DFfCXMjupOxgfoZ3WhzD1S2cX9XiqEWmB8-_VG8zA1dZd7yn_N3Vh7Nf6bk74cxNDZ9pgXygaDNApoL7x_-ZDD01BoJVhLfudcLjqtRBowqXvUR9zmjZ7wBWgvdh7DYpqoPMnf4Fluk7iGZEOzkzg07ld_t-8iSS059zr7F1XBUXYOIxZkdlvj4FsRjIQF9Wa41pKXZr_auzWKRj_S3Aq97ou1qPjldwHH6a4_2vUdp6Zhh8evhIqyEI20wso-kFy0ZtZ5dOo-kbblpy8-lJblgoo41LMZiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 11:37:42</div>
<hr>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kK3Yd63KSy5SA0PmTUz1Zvfjm8Fy6jQruPjwjunQkPd1BaI3PCCl6tIhzhQSF8YYKR-OrdvPId-HdyLmdwyj84FPY8_7CB1zdeJLi_wUBFj8MqtWs4d4Uxu-IQkx5w-BKqFt6CqQdLmCvSiTAYdHVJAUP7tv4FlWCuoHPbYzmEU5b5f72Ku4DOJBRgES6QZD0-WBR4nSJ0BBlWHULgurzGfHXx51O_mS7tQ8ONXACOOA3Imp9pZj5YbbnWjRDKDSYcZaC1rUAgYBKxlgKzaNInO1i_fnhfDv6TbvfZt0_lkWitHZ9bHkvwzpNPuO6iPaiLIu-xjKIlxK6Hd1M-dzQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ها در کرمانشاه!
آپدیت: دو زلزله به بزرگی ۵٫۲ و ۵٫۷
📍
در عمق ۸ تا ۱۳ کیلومتری
کورزان
پیام‌های دریافتی:
الان کرمانشاه هستیم
کل خونه لرزید
زلزله بود
سلام وحید همین الان زلزله اومد تو ایلام
کامیاران سنندج زلزله هنوزم پس لرزه میاد
خیلی بد زلزله اومد
کرمانشاه
کل خونه لرزید
اینجا جوانرودزلزلە اومد شدید بود
سلام ایلام حدود ۱۰ ثانیه خیلی بد لرزید
سلام وحید، زلزله سنندجم حس شد
سلام وحید همین الان ایوان غرب زلزله آمد خیلی شدید بود
کرمانشاه زلزله اومد
درود کرمانشاه چند ثانیه به شدت لرزید کاملا حس شد
سلام وقتتون بخیر همین الان زلزله اومد استان همدان ملایر ۷:۱۵
زلزله نسبتاً شدیدی سمت کرمانشاه اومد
همدان هم ۳ الی ۴ ثانیه لرزید
سلام همین الان زمین لرزه اومد جوانرود استان کرمانشاه
سلام اقا وحید، ما پاوه هستیم تو کرمانشاه خیلی بد لرزیدیم معلوم نبود زلزله‌ بود یا چی. از شدت لرزش زیاد از خواب پریدیم. ساعت تقریبا ۷:۱۴ صبح
کرمانشاه اسلام اباد غرب زلزله شدید
سلام کرمانشاه خیلی شدید لرزید حدود ۶. ۷ ثانیه
سلام من کرمانشاهم حدود ۱۰ ثانیه شایدم کمی بیشتر کل خونه لرزید
آقا وحید ما مرز مهران هستیم، استان ایلام اینجا هم لرزید ساعت 7:15دقیقه
🔄
دوباره لرزیدددد
یا خداا بازم
دوباره اومد
دوباره ایوان داره می‌لرزه
وحید خیلی شدیده
وحید بازم داره زلزله میاد، ایلام
همین الان سروآباد استان کردستان لرزید
همین الان ۷:۱۹ هم پس لرزه‌ش اومد
پشت سر هم زلزله بالای 10 دیقه کامیاران داره پس لرزه
سلام وحید جان
مریوان دوبار اومد ۷:۱۴ و ۷:۱۹
وای دوباره اومد اینقد شدید بود
سلام وحید دوباره کرمانشاه لرزید خیلی شدید تر و طولانی تر
سلام ایلام دوباره لرزید
۳ ۴ دقیقه پیش پاوه لرزید
یه دقیقه پیشم لرزید و قوی‌تر بود
درود دو مرتبه پشت سر هم داره زلزله میاد هنوزم ادامه داره
خرم اباد ساعت 7/20
همدان دوباره بدتر لرزید
کرمانشاه زلزله بود
همین الان کرمانشاه زلزله خیلی قویی امد
کرمانشاه بازم زلزله شدید و طولانی
سلام آقا وحید کرمانشاه زلزله قبلی حس نکردیم الان ۷:۲۰ خیلی شدید و طولانی لرزید
ساعت ۷:۲۰ همدان لرزید
زلزله بود
اراک همین الان ۷:۲۰
چنننند ثانیه لرزید
سلام 7:20 اراک خونه لرزید در حد تکون شدید
همدان الان کاملا لرزید برای زلزله
قوی بود
وای ایلام بد لرزید
عجبيه اين زلزله خرم آباد حس شد
جالب اينه چقد ادامه داشت
سلام وحید خرم اباد لرزید خیلی کم لرزید
سلام،همین الان پشت سرهم دو بار زلزله اومد همه مون از خواب بیدار شدیم،جوانرود
نهاوندم لرزید خیلی عجیب بود
دوباره کرمانشاه زلزله،
از دفعه اول طولانی‌تر بود
۷:۱۸
زلزله شدید دوباره کرمانشاه
سلام وحیدجان همین الان اراک لرزید چهار پنج ثانیه شدید بود مثل گعواره خونه میلرزید چه خبره همه جای ایران میلرزه...
سلام وحید ..زلزله خفیف ساعت ۷:۲۰ همدان
همدان شدید لرزید چند سال بود چنین زلزله ایی نیومده بود
وحید جان سلام
اینجا الشتر، لرستان، ساعت 7:19صبح لرزید و قشنگ حس کردم لرزش زمین رو
سلام وحید جان ۷و۱۷دقیقه ب مدت۶ثانیه زلزله خیلی شدید از کرمانشاه همه رو از خواب بیدار کرد
کرمانشاه با زلزله بیدارشدیم
سلام وحید جان زلزله خیلی شدید همین الان کرمانشاه
سلام داداش کرمانشاه برای چند ثانیه وحشتناک لرزید
سلام بروجرد هفت و بیست دقیقه لرزید
سلام ساعت ۷:۲۱ همدان شهر همدان یه زلزله خفیف اومد
سلام بروجرد هم زلزله اومد
زلزله یا چیزی شبیه به آن در خرم آباد احساس شد
کرمانشاه زلزله وحشتناک اومد خیلی شدید بود
کرمانشاه زلزله آمد
منم قروه کردستانم
خونه یه ذره لرزید
آپدیت:
گزارش مقدماتی زمین‌لرزه
زلزله ۵.۲ ریشتری در استان کرمانشاه
مرکز لرزه‌نگاری کشوری مؤسسۀ ژئوفیزیک دانشگاه تهران:
محل وقوع: استان كرمانشاه - حوالی كوزران
تاریخ و زمان وقوع به وقت محلی:
۰۷:۱۳:۱۷ ۱۴۰۵/۰۴/۲۹
طول جغرافیایی: ۴۶.۴۳
عرض جغرافیایی: ۳۴.۵۶
عمق زمین‌لرزه: ۸ کیلومتر
نزدیک‌ترین شهرها:
۱۷ کیلومتری كوزران (كرمانشاه)
۲۳ کیلومتری گهواره (كرمانشاه)
۲۶ کیلومتری روانسر (كرمانشاه)
نزدیکترین مراکز استان:
۶۵ کیلومتری كرمانشاه
۹۸ کیلومتری سنندج
كوزران کرمانشاه دوباره لرزید/ اینبار زلزله ۵.۷ ریشتری
مرکز لرزه‌نگاری کشوری مؤسسۀ ژئوفیزیک دانشگاه تهران:
محل وقوع: استان كرمانشاه - حوالی كوزران
تاریخ و زمان وقوع به وقت محلی: 1405/04/29 07:18:49
طول جغرافیایی: 46.48
عرض جغرافیایی: 34.57
عمق زمین‌لرزه: 13 کیلومتر
نزدیک‌ترین شهرها:
13 کیلومتری كوزران (كرمانشاه)
22 کیلومتری روانسر (كرمانشاه)
25 کیلومتری گهواره (كرمانشاه)
نزدیکترین مراکز استان:
61 کیلومتری كرمانشاه
94 کیلومتری سنندج
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77299" target="_blank">📅 07:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QlF0-kAQ5ZegkKGcnWUlVj4q11ezU9tk4D6hnZ-JIZl3lAhuSyuj6lu9KhBfaQNJB8JZWO0by6mqXHWbTkr02BHjTzHh7dWLvG-6vs-AETc7pst0shsS398sx-PT0TDqq0iF5IZL24BUkF39Onmw6aXKx100hWV0xHIU83nG4vsX9xacZwVj1o7fyVNGQdhDK7AHuz2QzFblbftFPFwbDFU57j79KJLHMqVACmrYf3Y5m8EchdnazARbyR0JtoITUDrR9TPxHQxiZHlFnyRjybvnMEaZePd5nX4q8nMwnRp63Ih8WJPjFA0-NnSjAWMHdMGdefGF8wEpvYiyEdw3jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
مارکو روبیو، وزیر خارجه آمریکا، روز یکشنبه گفت ایالات متحده آماده دیپلماسی با ایران است؛ هم‌زمان ارتش آمریکا نهمین شب پیاپی حملات خود را آغاز کرد.
روبیو پیش از عزیمت به مانیل، جایی که قرار است در اجلاس اتحادیه کشورهای جنوب شرق آسیا شرکت کند، به خبرنگاران گفت: «ایالات متحده همیشه برای رسیدن به یک راه‌حل دیپلماتیک آماده است. ما چندین بار با ایران تلاش کرده‌ایم و به تلاش خود ادامه خواهیم داد. اگر آن در باز شود، از دیدن آن خوشحال خواهیم شد.»
روبیو از ایران به‌دلیل حمله به کشتی‌ها و ایجاد مانع در تنگه هرمز انتقاد کرد. تفاهم‌نامه‌ای که آمریکا و ایران در ماه ژوئن به آن دست یافتند، با هدف گسترش آتش‌بس و ازسرگیری تردد در این آبراه کلیدی تنظیم شده بود.
روبیو گفت: «اگر آن‌ها مفاد این تفاهم‌نامه را نقض کنند، نمی‌توانند انتظار داشته باشند که این تفاهم‌نامه همچنان پابرجا بماند.» او افزود: «آن‌ها همچنان پیام می‌فرستند که می‌خواهند گفت‌وگو کنند و مذاکره کنند، اما آنچه ما به آن پاسخ می‌دهیم رفتارشان است، و رفتارشان این است که موشک‌ها و پهپادهایی را علیه کشتی‌ها، از جمله همین امشب، پرتاب می‌کنند.»
کیت ماهر، خبرنگار سی‌ان‌ان، از روبیو پرسید اگر تلاش‌های دیپلماتیک شکست بخورد چه خواهد شد. روبیو پاسخ داد: «فکر نمی‌کنم برای ایران خوب باشد. منظورم این است که اقتصاد ایران از هم پاشیده است.»
CNN
مارکو روبیو، وزیر خارجه آمریکا، گفت حادثه‌ای که روز شنبه در شمال عراق به کشته‌شدن یک نظامی آمریکایی انجامید، یک «سانحه» بود و این نظامی هنگام خنثی‌سازی یک پهپاد سرنگون‌شده ایرانی آسیب دید.
روبیو روز یکشنبه به خبرنگاران گفت: «هیچ کاری که ارتش انجام می‌دهد بی‌خطر نیست. همه این کارها ذاتاً خطرناک‌اند و ما فقط سپاسگزاریم که چنین آمریکایی‌های قهرمانی با پوشیدن یونیفرم، در خدمت کشورمان هستند.»
روبیو درباره حمله ایران در روز جمعه در اردن که به کشته‌شدن دو نظامی آمریکایی انجامید، گفت: «یک موشک عبور کرد. تقریباً همه موشک‌ها را سرنگون کردیم. یکی از آن‌ها رد شد... این دلخراش است.»
روبیو گفت که «برای خانواده‌هایشان و آمرزش روحشان دعا می‌کند.»
تعداد نظامیان آمریکایی که در جنگ نزدیک به پنج‌ماهه با ایران کشته شده‌اند، اکنون به ۱۷ نفر رسیده است.
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77298" target="_blank">📅 07:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان چابهار 5 بار زد 5:50
باز داره چابهار رو میزنه  لرزش ها وحشتناکه
الان دوبار صدا اومد ساعت ۵:۴۸
5:49 دیقه کنارک صدای انفجار اومد
هنوزم صدای هواپیما میاد
به عنوان آخرین مقصد اینجا رو میزنه
کنارک صدای جنگنده و انفجار هم اکنون
۲انفجا کنارک نیروی هوایی ۵.۴۹
صدای هواپیما بازم شنیده میشهه چابهار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/77297" target="_blank">📅 05:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ddbd450c.mp4?token=j8k5ZSSHMwkCUjkQNthItppf2NbgEInoYKTCiMtQ3hZ5hTMyERNl7XksXgKXyBnYajrURs0I1SApXmKUdhIXdztNTtwYSKc0iQLvBzEfMdIwXBRyb30SwDjiGMgV0NUoABbaZINJlz1OpLtbxCjOt5WWuuk8_lNK7LoZUxC3osEE_B-5TSPHjg-aRWNM__dOey7RxjSDuowWboHQIzdfIT2GOG22bAd76yGvREep8XIBcG45IzZk1mdazliAPofR2Ym3niMJPyiwXxowz1mr0dLPZDEFVa9Vm_3w8oe4fqK88F2Aq8swK5TtkBKlCcUqzEE_40XL1cJGrIm92Pa81w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ddbd450c.mp4?token=j8k5ZSSHMwkCUjkQNthItppf2NbgEInoYKTCiMtQ3hZ5hTMyERNl7XksXgKXyBnYajrURs0I1SApXmKUdhIXdztNTtwYSKc0iQLvBzEfMdIwXBRyb30SwDjiGMgV0NUoABbaZINJlz1OpLtbxCjOt5WWuuk8_lNK7LoZUxC3osEE_B-5TSPHjg-aRWNM__dOey7RxjSDuowWboHQIzdfIT2GOG22bAd76yGvREep8XIBcG45IzZk1mdazliAPofR2Ym3niMJPyiwXxowz1mr0dLPZDEFVa9Vm_3w8oe4fqK88F2Aq8swK5TtkBKlCcUqzEE_40XL1cJGrIm92Pa81w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام موج حملات آخر هفته علیه ایران را به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) نهمین شب پیاپی حملات علیه ایران را روز ۱۹ ژوئیه، ساعت ۱۰ شب به وقت شرق آمریکا، با موفقیت به پایان رساند.
تجهیزات و نیروهای سنتکام مراکز فرماندهی نظامی ایران، مواضع پدافند هوایی و نظارت ساحلی، توانمندی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و شبکه‌های ارتباطی را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی عبوری از تنگه هرمز بیش از پیش کاهش یابد.
ارتش آمریکا به دستور فرمانده کل قوا، ایران را پاسخ‌گو می‌کند. نیروهای سنتکام همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی می‌مانند.
CENTCOM
منابع حکومتی:
اطلاعیه شماره ۳۰/ دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند
روابط عمومی سپاه:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی؛ اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک کوش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگه هرمز را داشتند منفجر شده و از حرکت باز ماندند.
🔹
اینجا سرزمین ماست و دخالت ارتش تروریستی آمریکا از هزاران کیلومتر آن طرف‌تر هیچ وجاهت قانونی ندارد و با قطعیت با آن برخورد خواهد شد و تا زمانی که شرارت های آمریکا در منطقه ادامه یابد این معبر برای عبور کود شیمیایی و حتی یک قطر نفت و گاز امنیت ندارد.
🔹
ارتش متجاوز، آماده عملیات تنبیه ما به خاطر این تخلف غیرقانونی باشد.
قدردانی سپاه از اطلاعات مردم اردن؛ هواپیماهای بزرگ ترابری C17 و هواپیماهای فرمانده کنترل P8 ارتش متجاوز امریکا در فرودگاه عقبه هدف موشک بالستیک قرار گرفتند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
إِنْ نَکَثُوا أَیْمانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَ طَعَنُوا فی دینِکُمْ فَقاتِلُوا أَئِمَّةَ الْکُفْرِ إِنَّهُمْ لا أَیْمانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ
🔺
مردم شریف و ارتشیان مجاهد اردن، با تشکر از همکاری صمیمانه و اطلاعات دقیق شما که موجب هدفگیری دقیق رزمندگان اسلام و انهدام ۲۰ سوله محل استقرار نیروهای ارتش کودک کش آمریکا در منطقه الازرق و کشته شدن ده‌ها نیروی تروریست آمریکایی شد.
🔺
رزمندگان نیروی هوافضای سپاه در موج ۲۱ عملیات نصر ۲ با رمز مبارک یا رقیه (س) و تقدیم به دختر بچه های شهید جنگ تحمیلی سوم، با کمک شما، هواپیماهای بزرگ ترابری C17 و هواپیماهای فرمانده کنترل P8 ارتش متجاوز امریکا در فرودگاه عقبه را هدف حمله موشک های بالستیک قرار داده و به تعدادی از آنهاخسارت سنگین وارد کردند.
🔺
نظامیان متجاوز آمریکا که طی چند دهه اخیر به بیش از ده کشور اسلامی حمله کرده و میلیون ها مسلمان را کشته اند و حامی اصلی رژیم کودکش صهیونیستی در کشتار عظیم مردم غزه و ویران کردن کرانه باختری هستند، از لحاظ شرعی مهدور الدم هستند و هر مسلمانی، هرجا دستش رسید باید این قاتلان وحشی را بکشد.
🔺
با تشکر مجدد از تلاش‌ها و همکاری‌های شما که با انجام تکلیف شرعی راه را برای آزادی قدس شریف هموار می‌کنید.
«إِنْ تَنْصُرُوا اللَّهَ یَنْصُرْکُمْ وَ یُثَبِّتْ أَقْدَامَکُمْ»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77296" target="_blank">📅 05:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94bb518d25.mp4?token=mYBsPhgOa6kKbEtXAnI1_tcLVpU3WSmwSYjbXpfnpx9boxfrdw1iIY0VZVbHVuP3nMMjZqwxuxZtTSoAqga-UDEXe3mbzcVwfJjHSaUxiYoqJNXpu3v6Q3YlC5yb6Ie_TI4kN3hRsDNxAd76XJO9IW8ymSEp7-UG2q4vrdAU2dtRA_qtiGH7re6Naip5_thWs63UKskHfIHdm9qsc1pPFkWzr2l63PYJ3YmktYmFQNBjslJaGr3XoJU2x0c9kECdP76zdsy7725i1YOR3ttV4kWAkR2JhO1WNDT9te4oENWyJJg4CJnvZonc2s_fjOpfEWd64f_g7yUc8iVcRUZ6UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94bb518d25.mp4?token=mYBsPhgOa6kKbEtXAnI1_tcLVpU3WSmwSYjbXpfnpx9boxfrdw1iIY0VZVbHVuP3nMMjZqwxuxZtTSoAqga-UDEXe3mbzcVwfJjHSaUxiYoqJNXpu3v6Q3YlC5yb6Ie_TI4kN3hRsDNxAd76XJO9IW8ymSEp7-UG2q4vrdAU2dtRA_qtiGH7re6Naip5_thWs63UKskHfIHdm9qsc1pPFkWzr2l63PYJ3YmktYmFQNBjslJaGr3XoJU2x0c9kECdP76zdsy7725i1YOR3ttV4kWAkR2JhO1WNDT9te4oENWyJJg4CJnvZonc2s_fjOpfEWd64f_g7yUc8iVcRUZ6UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: کاری که اکنون می‌کنیم این است که هرگونه امکان دستیابی آن‌ها به موشک هسته‌ای را از بین می‌بریم
مصاحبه ترامپ بعد از مراسم فینال جام جهانی، ترجمه ماشین:
ترامپ:
به کشورمان افتخار می‌کنیم. به کاری که همه انجام دادند بسیار افتخار می‌کنیم. به جیانی اینفانتینو و تمام کارکنانش برای کار باورنکردنی‌شان تبریک می‌گوییم.
این یکی از بزرگ‌ترین رویدادها از هر نوعی بود که تاکنون برگزار شده است. بنابراین خیلی خوشحالیم که این‌قدر موفق بود. مردم از سراسر جهان آمدند و کشورمان را دوست داشتند.
می‌دانید، این رویداد کشورمان را از زاویه‌ای متفاوت به نمایش گذاشت.
اتفاق فوق‌العاده‌ای بود؛ یک رویداد عالی بود و خوشحالم که همه شما از آن لذت بردید.
خبرنگار:
شما گفتید آرژانتین باخت.
ترامپ:
این را شما می‌گویید؟
خبرنگار:
شما گفتید آرژانتین باخت.
ترامپ:
نه، چنین چیزی نگفتم. فکر می‌کنم هر دو خوب بازی کردند. من می‌گویم اسپانیا واقعاً بهتر بازی کرد.
هر دو خوب بازی کردند. منظورم این است که به فینال رسیدند و واقعاً بسیار هیجان‌انگیز بود. به نظر می‌رسید اسپانیا مسلط بود، اما مسابقه بسیار نزدیک بود. بنابراین عالی بود؛ یک رویداد عالی بود، بله.
خبرنگار:
[پرسش خبرنگار نامفهوم است.]
ترامپ:
خب، احساس بسیار بدی داریم. اما می‌دانید، آن افراد بزرگ، آن میهن‌پرستان بزرگ، در تمام این مدت جنگیدند تا ایران نتواند سلاح هسته‌ای داشته باشد.
ایران به‌شدت، به‌شدت آسیب دیده است. تقریباً همه توان نظامی‌اش را از دست داده است. چیز بسیار کمی برای آن‌ها باقی مانده. تعدادی موشک و پهپاد دارند. مقداری توان تولید هم دارند، اما زیاد نیست.
ما تنگه هرمز را در کنترل داریم. آن‌ها هیچ‌چیز را کنترل نمی‌کنند. پس خواهیم دید چه اتفاقی می‌افتد.
امشب دوباره ضربه بسیار سختی به آن‌ها زدیم و این کار را به احترام آن میهن‌پرستان بزرگی انجام دادیم که احتمالاً سه نفرند، نه دو نفر.
خبرنگار:
پیامدهای دخالت چین در انتخابات آمریکا چه خواهد بود؟
ترامپ:
بعداً درباره‌اش صحبت خواهیم کرد. با آن‌ها گفت‌وگو می‌کنیم، مطمئنم.
خبرنگار:
می‌توانم بپرسم آیا با کارنی، نخست‌وزیر کانادا، گفت‌وگو کردید؟
ترامپ:
بله، کردم. بله، صحبت کردم.
خبرنگار:
گفت‌وگو چطور پیش رفت؟
ترامپ:
خوب پیش رفت. اما به او گفتم باید جلوی ورود دود این آتش‌سوزی‌ها را بگیرید، چون هوای ما را مسموم می‌کند. هوای ما مسموم شده است.
من رابطه خوبی با مارک کارنی دارم. اما می‌دانید، باید آتش‌سوزی‌های آنجا را متوقف کنیم. اگر بتوانیم به آن‌ها کمک کنیم، کمک می‌کنیم. اما شاید باید بابت خسارت‌ها چیزی به ما بپردازند، یا شاید ما باید تعرفه‌ای وضع کنیم.
وضعیت وحشتناک بود. کسب‌وکارها تعطیل می‌شدند؛ به‌ویژه در میشیگان. اگر به دیترویت در میشیگان نگاه کنید، مجبور شدند همه‌چیز را تعطیل کنند. مجبور شدند کارخانه‌های خودروسازی و بسیاری مراکز دیگر را ببندند.
من هرگز به یاد ندارم چنین اتفاقی افتاده باشد. در چهار یا پنج سال گذشته این وضعیت کم‌کم آغاز شد. پیش از آن هرگز به یاد ندارم چنین اتفاقی افتاده باشد.
خبرنگار:
آیا فرصت کردید با نخست‌وزیر اسپانیا هم صحبت کنید؟
ترامپ:
بله. با مقام‌های اسپانیا صحبت کردم و بابت داشتن چنین تیم بزرگی به آن‌ها تبریک گفتم. با افراد زیادی صحبت کردم.
خبرنگار:
پیش‌تر با اسپانیا تنش داشتید.
ترامپ:
نه، هیچ تنشی ندارم. با هیچ‌کس تنشی ندارم.
خبرنگار:
[پرسش خبرنگار درباره اسپانیا نامفهوم است.]
ترامپ:
خب، [نامفهوم]. می‌دانید، توانایی زیادی دارد. اما تا جایی که می‌دانم، ظرف حدود یک ماه [نامفهوم] تا آن را به حداکثر برسانند. بنابراین قرار است آن را بفرستند و به حداکثر برسانند. فکر می‌کنم حدود یک ماه دیگر.
خبرنگار:
آقای رئیس‌جمهور، آیا با نخست‌وزیر کانادا صحبت کردید؟
ترامپ:
بله. همین حالا داشتم پاسخ می‌دادم. درباره‌اش با او صحبت کردم. گفتم: «باید جلویش را بگیرید.»
مسئله در اصل مدیریت جنگل‌هاست و آن‌ها باید بدانند چگونه این کار را انجام دهند. اگر چهار یا پنج سال به عقب برگردید، به یاد ندارم هرگز چنین مشکلی داشته باشیم. اما حالا این مشکل را داریم.
فردی در محل:
از این طرف بیایید، آقای رئیس‌جمهور.
خبرنگار:
شما گفتید جنگ را ظرف چهار یا پنج هفته پایان می‌دهید.
ترامپ:
[آغاز پاسخ نامفهوم است.] کاری که اکنون انجام می‌دهیم بسیار بزرگ‌تر است. قبلاً کار محدودتری انجام می‌دادیم؛ می‌خواستیم مانع دستیابی آن‌ها به توانایی خاصی شویم. حالا داریم کار را تمام می‌کنیم.
بنابراین واقعاً همان موضوع قبلی نیست. کاری که اکنون می‌کنیم این است که هرگونه امکان دستیابی آن‌ها به موشک هسته‌ای را از بین می‌بریم.
اگر نگاه کنید، پس از یک هفته و نیم ــ نه چهار هفته؛ یک هفته و نیم یا دو هفته ــ جلویشان را گرفتیم؛ احتمالاً... اما نمی‌خواهم از واژهٔ «احتمالاً» استفاده کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77295" target="_blank">📅 04:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WyHLj_3zWnuj5yGO8I9xBeYuP59LUmZXxNiu-PT58RaDla3dr3YVsSVOjA1IFm8cBcfZbx0hppnlNWzDphTOogfOOKTsd9gLRYC1-quISPoscPTr_cXgjQB3iuYjMs_5q3C5j3AWsEH9LVQB8QQo_HYnLMsN8OBtXzeJ2I94r1YMimZHx2hLO1vqcyz19l5-PnPB_WYFaFmcwpfq5GuPgf1aXiQD4lB5QVGnmfJ8OgcKKVlzve4eQbu7XIr1oLlzOUd3svnR7t0QRrV2wR6uDcfSkap8j3oJTK5FH37wvOYH1CTSwhnjVzPCkG5whH_Y8gj7L6qU713kN2ur940_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت: تصویر منتشرشده با شرح کنارک
پیام‌های دریافتی:
بازم یه انفجار چابهار ۳:۵۱
کنارک صدای انفجار(دور بود)
و همینطور صدای جنگنده
نیم ساعته از بعد جام جهانی داره چابهار و کنارک رو سنگین می زنه. جاهای مختلفه و نمی دونم کجاها بوده فعلا
دوباره خیلی سنگین زد
چابهار ۳:۵۱ صدا اومد
همین الان چابهار دوبار زد 3:51
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77294" target="_blank">📅 03:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riQHxaBGDjaNRK7oHsG9HZEnFnWdvs-7YaDAVwVAN_CuymeAed5O2LJ9qApSzEi2US5ORRkZA_pC8YpT-N36WURh29pv7WmYuVt7fIs9GI8AYSwxMSE7ITpw9pzcBTxuO_aGXcGHz98eCwoP6lIXOXkO-ho4kGohdB6H95oo4cxpDju_AnAHgwGOIx4_E4HJKmn4i_cBc3h_5-EdLfpT4TBUd9v5Ueq-sS4KZ3HCLDbKsPfIHVX3KI6iP292k9jecIK8YdOS29RPlPtgw5N56GA1ukH7P3yB2gQpcWhJidf6yFhothULEaJxCH4HMoI71YQgIyTJy1y2tWIAB7ggoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با آغاز نهمین شب حملات متوالی آمریکا به مواضع نظامی در ایران، بامداد یکشنبه، فارس از اصابت چند موشک و شنیده‌شدن صدای انفجارها در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر و بندر خمینی در خوزستان خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/77293" target="_blank">📅 03:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌های دریافتی:
سپاه خورموج توی استان بوشهر رو زدن برق ی منطقه هم رفته
سلام وحید  ساعت ۳:۰۷ دقیقه
خورموج پنج انفجار شدید
همین الان خورموج پادگان سپاه زدن برق هم قطع شد
همین الان سپاه خورموج زدن ساختمانش کلا صااف زمین شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77292" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پیام‌های دریافتی:
چندین صدای انفجار پیاپی، سیریک.
ساعت سه و پنج دقیقه بامداد شهر سیریک ده ها انفجار بسیار سنگین
سه تا آخری خیلی بد زد موجش زیاد بود
احتمالا اسکله بوده باشه
۳:۰۵ تا ۳:۱۰ چند انفجار سمت سیریک (طاهرویی) خیلی شدید
سیریک صدای انفجار پشت سرهم خیلی بلند، صدای جنگنده‌ها هم میاد
بندر عباس ساعت 3:11 دقیقه چند انفجار پشت سر هم و طولانی رخ داد و تا دو دقیقه ادامه داشت
بندر جاسک همین الان دوتا صدا اومد
بندر جاسک دوباره صدا اومد صدا خیلی وحشتناک بود
سیریک حدود ۸ انفجار شدید شایدم بیشتر  شیشه های اتاقم نزدیک بود بشکنن
جاسک جنگنده بالا سرمونه
۳تا انفجار تا الان
بیشتر از ۳تا شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/77291" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eMyk6YUF2whqi2v1QuxB8wr1gEhJhKLl0j74mnQimvHAKqesE-5FiysQp68XhDAygAC2p9gk0QrGg9X8G8nbIx6zdp_t4WlRWIgNwxNnNqT9C4qwsNsJcoZiq_NK4uZtNHLV5gcOMKLtvtxkanqvlORBtLpG7zN68qpZKAZFWd9L51QHqAPvA8tJo5r2Tsv1FtFVg-QsB_dMLsL5o_xwwhhVBFCS7FIlKw5o1ruS3C13dpozlgpZJYF-qFcxB85971r3ZXO8_NqrnFx2_fzvmmPwZzQDtnXdNV8uWOduCZuRGsvtQRg9MTfkVCTg8FgVYQXgfYR4nOWcWYySvTSpUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'سربندر ("بندر امام خمینی") ساعت ۲:۴۰ دوشنبه ۲۹ تیر'
Vahid
دوباره زد
سربندر خوزستان 3:08 دو صدای انفجار و لرزش شدید خونه
وحید جان دوباره سربندر دوبار محکم زدن
وحید سربندر رو باز هم زد
تک انفجار، ولی خیلی سنگین ۳:۰۹
۳.۰۸ دقیقه سربندرو بازم زدن
اقا وحید ماهشهر دوباره زد
شیشه اتاقم لرزید این بار
صدای انفجار قبلی رو فقط شنیدم
خود ماهشهرم، سربندر نیستم ۳:۰۹
وحید ماهشهر یکی سنگین زد
سربندر دوباره زد صداش بیشتر از قبلی بودد
ماهشهر دوباره شدید ۳:۸ دقیقه
ماهشهر رو دوباره زد ۳:۰۸
همین الان باز ماهشهر دو انفجار شدید
سربندر ساعت ٣:٠٩ دقیقه دوباره انفجار شدید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/77290" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=QekG2voUa5Ae-vXG9VBOd88wPWFGhnIe2WfK2nLoRowopeKEeo_Gc1yxkq1hsXix--RvotaL-E694AGxR0zaH3oRAyzAigTEMDGwtuV1zmz0S2Rz6iJQ86Mpalk1AbYGBGxpxI3RLm5nYvKt9ygYi2Ash0JgmTuUSvT-KhTpW8lv_TAVdJQnbHhB8TNZY3G0esZcxVfWvPZx_MZ8iNUymRG3bI0pB1f7iZgGf9Np0A4G5Uja689c2TzCB4nHy8Lrhlo9Wrp7u9DYVcqhiot9MRMB0dE3lzXQQ-Aj-cOCbEk6ZGkOBYi3Ab2VqY8stWY2WFT9X-CL0o7H03SV1UIhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=QekG2voUa5Ae-vXG9VBOd88wPWFGhnIe2WfK2nLoRowopeKEeo_Gc1yxkq1hsXix--RvotaL-E694AGxR0zaH3oRAyzAigTEMDGwtuV1zmz0S2Rz6iJQ86Mpalk1AbYGBGxpxI3RLm5nYvKt9ygYi2Ash0JgmTuUSvT-KhTpW8lv_TAVdJQnbHhB8TNZY3G0esZcxVfWvPZx_MZ8iNUymRG3bI0pB1f7iZgGf9Np0A4G5Uja689c2TzCB4nHy8Lrhlo9Wrp7u9DYVcqhiot9MRMB0dE3lzXQQ-Aj-cOCbEk6ZGkOBYi3Ab2VqY8stWY2WFT9X-CL0o7H03SV1UIhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'سایت موشکی تبریز'
دوشنبه ۲۹ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/77289" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/028b9087f7.mp4?token=gnEhl3cZLDLucO4DwwIT7Dbjbuek1UPcVNAjeU0WD8zpN_VPmI4e82X3lowS0ASr_F7vQxG2AQJdeVrn10XPnB87AjpqF8aW8GuGFvGS-Yz46eivwfr1fDf6q7Ca7MUMNtImoReRRC2-jOD5vWQ09sOQnloZk8PSa9kflHcQpuXwhDTa1KDDFFl9Y4eacCxH0MBwPRBEPQQVvcrfK_-Uqaayg1Wo5U26-ZKcHE7c6VPiAdKu3Ya2mkP2jnsjv2lIQl9Z7B3v86PoSaEHT7yZcZSs2fUY0wXcwCXmKQOXOp6E8U9DX_OaX8VmxmUuL1vMI4h5JUKUAt72ZsyPma6Inw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/028b9087f7.mp4?token=gnEhl3cZLDLucO4DwwIT7Dbjbuek1UPcVNAjeU0WD8zpN_VPmI4e82X3lowS0ASr_F7vQxG2AQJdeVrn10XPnB87AjpqF8aW8GuGFvGS-Yz46eivwfr1fDf6q7Ca7MUMNtImoReRRC2-jOD5vWQ09sOQnloZk8PSa9kflHcQpuXwhDTa1KDDFFl9Y4eacCxH0MBwPRBEPQQVvcrfK_-Uqaayg1Wo5U26-ZKcHE7c6VPiAdKu3Ya2mkP2jnsjv2lIQl9Z7B3v86PoSaEHT7yZcZSs2fUY0wXcwCXmKQOXOp6E8U9DX_OaX8VmxmUuL1vMI4h5JUKUAt72ZsyPma6Inw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'انفجار در
#تبریز
'
بنا بر پیام‌های دریافتی از شهروندان حدود ساعت ۲:۳۷ دوشنبه ۲۹ تیر صدای چند انفجار در تبریز شنیده شده.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77288" target="_blank">📅 03:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77287">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W5CUnfkQVX1IAJCkBBVuWY7CR0DXtZUwrEbl1k192ppDcnB1hUEnNW3JCuHetbN8W8aM5nzBtRf3IvZju743uWG6MFfvVV2H3Lr6pLirKmE38UEheww4eteyRZi_YpNV9WE5Mddqq4FI6wQKRdpXH1Vt1vAqug9eUUpKoHs4ravmhiRX03Dao07VFYTuEsrBHBKEJcPbAjsP5UEUvQWFWPNzGzJqhq8ycXrFlvoUm1mZjEP0o48uhK6-UYM0Gr13PdMTx05SgYytdR4VQSmNPCgfB-S0usvGl-Dy02CYgRSiTfmg8drxaKxrf3eGti-4mL3TY4g1QdXHUgLJDlRjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
سنتکام امروز ساعت ۷ عصر به وقت شرق آمریکا، برای نهمین شب متوالی موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات به تضعیف بیشتر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی در حال عبور از تنگه هرمز به کار می‌روند، ادامه خواهد داد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77287" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیام‌های دریافتی:
۵ ۶ تا همین الان کنارک
خیلی خیلی شدید بود هنوز داریم میلرزیم
۳ تا دیگه همین الان
چابهار الان صدا انفجار پی در پی اومد
2.43
چابهار 4تا صدای انفجار شنیده شد دور بودن
چابهارو الان زدن ۲:۴۴
چابهار صدای انفجار اومد
کنارک 2:42 سه انفجار پشت سرهم
کنارک ۳ تا انفجار
سلام بازم دوتا قدای انفجار ساعت ۲.۴۵ در کنارک
خیلی بد داره میزنه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/77286" target="_blank">📅 02:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پیام‌های دریافتی:
ماهشهر صدای انفجار اومد میگن سربندره
سلام وحید جان
ساعت 02:40 سربندر صدای وحشتناکی اومد.
آقا وحید ماهشهر همین الان چندتا صدای مهیب و لرزش شیشه ها رو داشتیم
همین الان ماهشهر رو زدن
سربندر ۲:۴۱ انفجار شدید
سربندر دو سه تا پشت سرهم یکیش خیلی نزدیک بود یعنی پدافند رو زدن
چون تازه دود دیدم از سمت سایت پدافندی  نزدیک خونمونه
وحید جان همین الان سربندر خوزستان  شدید زد
وحید جان 2:40 سربندر انفجار بسیار قوی
بندر امام خمینی، خوزستان
من ماهشرم، هیچ صدایی نشنیدم، شاید سربندر رو زده باشن، اما ماهشهر هیچ خبری نبوده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/77285" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/czsiuE21amDzNXZeqhx47v6TKSF2GGz1jQ4e4FHXVukUtz1QH9ZSomoWQk7LBE5yCVQ2Y3PoajqFvIX1ugRWLo2C03O_w3j3wNBaSui9r6DASCoAZUw0JOZa4kqXn8K_OdwWyM0SYoWQlHg0YbgKPr7RQeK_6utzt2flqFTLiJjY4fL_VVFn8X6LsLw5q2Z7iLhhdYGXxNrdGUwL-zs5udA76CF4-Cm4-L76IPWQIA_d8tOULFBcgS_6C_OYz5Nqs_YBZ4x8af0sPOHDSzdE8PcuB5Fd2-HCZZ4Ox2nfYHd9fJJ3ReyHuE6Z9F2-x9SV6YuUk9U76HYYV6pBSBVJmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
وحید همین الان صدا اومد از تبریز ، ۳ تا
تبریز همین الان ساعت ۲.۳۸ صدای انفجار شدید اومد
صدای چند انفجار وحشتناک از تبریز همین الان
تبریز سه چهار تا صدای انفجار ا‌مد
سلام تبریز الان صدای ۳ تا انفجار اومد
صدای چند انفجار پیاپی - تبریز ساعت ۲:۳۷ بامداد
وحید جان تبریز 3 باز زدن شدید
سلام آقا وحید 2:37 صدای ۳ انفجار اطراف تبریز
سلام وحید. ۲:۳۷ انفجار در تبریز
ساعت ۲:۳۸ تبریز
چندین صدای مهیب انفجار
وحید تبریز یه صدای مهیب اومد نمی‌دونیم چی بود ولی انفجار بزرگی بود
همین الان تبریز پشت سرهم ۴ تا صدای انفجار اومد
سلام تبریز زدن ساعت ۲.۳۷ دقیقه
مکانی که ما بودیم قشنگ لرزید صدای انفجار هم اومد اما سمتش نمیدونم دقیق کجاست
سلام آقا وحید. الان ۲:۳۸ تبریزو زدن.
سلام وحید جان چند انفجار پشت سرهم در تبریز ۲:۳۷
خیلی شدید بودن
سلام تبریز صدای ۲ تا انفجار اومد
سلام صدای ۳ ۴ تا انفجار پشت سرهم  اومد تبریز
وحید  ۴ انفجار پیاپی تبریز
همین الان صدای انفجار تبریز ۰۲/۳۷
تبریز صدای ۳ انفجار پشت سر هم،ساعت ۲:۳۷
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77284" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/668363f045.mp4?token=hUjAqGwTn6AFKtpdcVZamd_ihd9VF1f5F2lz-pM2pNKUDVxBwOgULmrpwPGCVjB69kjIY5bv_yyA7ceQj2m7ZRGMjHM0iCHS1l6kphGcuIbLkzA0i5NN72-pcdf3NI9w5z6Y4X5GCqZJVWN-vu3oEEsqGicJQ3Qm6jfubtvhs1EOROq_ZW1a-X5eg1WgSFCGBJeU-oJlOfCQ6Krm5_iEHCTwz30Xudmg_ZxyexrqRFIFgEymbEDRl27-ySpvSzTq3-W4jWwx6-QvbCkWU8NVuvWO6tulsfzkqP2HTE2QmH_z48aAozF7CbOt7iLC0EXA6MbEpo5Ksrm1j4b3PjW-BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/668363f045.mp4?token=hUjAqGwTn6AFKtpdcVZamd_ihd9VF1f5F2lz-pM2pNKUDVxBwOgULmrpwPGCVjB69kjIY5bv_yyA7ceQj2m7ZRGMjHM0iCHS1l6kphGcuIbLkzA0i5NN72-pcdf3NI9w5z6Y4X5GCqZJVWN-vu3oEEsqGicJQ3Qm6jfubtvhs1EOROq_ZW1a-X5eg1WgSFCGBJeU-oJlOfCQ6Krm5_iEHCTwz30Xudmg_ZxyexrqRFIFgEymbEDRl27-ySpvSzTq3-W4jWwx6-QvbCkWU8NVuvWO6tulsfzkqP2HTE2QmH_z48aAozF7CbOt7iLC0EXA6MbEpo5Ksrm1j4b3PjW-BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال اسپانیا با تک گل فران تورس در وقت‌های اضافی آرژانتین را شکست داد و قهرمان جام جهانی ۲۰۲۶ شد.
این دومین قهرمانی اسپانیا در جام جهانی است که این بار با پیروزی مقابل مدافع عنوان قهرمانی به دست آمد.
@
VahidHeadline
تلویزیون سراسری در ایران مراسم اهدای جام جهانی فوتبال رو به خاطر حضور ترامپ پخش نکرد.
ترامپی که حتی موقع ثبت لحظه تاریخی بالا بردن جام هم حاضر نشد از کادر دوربین‌ها بیرون بره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77283" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c82cf41e.mp4?token=hAs-Md4kz7NTkwC3ptU5uks6tyVU_9AOmz89VzZtBOR9IEgQbLmGK5oZpDubIl92_C-peubOmMumSZmcSMva8Uq5zRnqmC7ah83xV1WrFpG5x4MgcAEkrwjoMpXTDC6Us4vN1PKubacuK9HcjnFKzb_eFjP0gjBcfP5O2z2MoRj1qsci9l9TNR4pHunJXYUGF9_QcVmk_TjEF_7TxjmC6P9s9-npJSKjEZuIealjaSxpegy3GQhXDGuxM_zvFjJQfsh1q2kfXkp3IeJilLOgk7W_k1cIKZ3E107nTiocnQCcm2yvsZ-SM2qbuRJ_EOIiNKh44gj8NhdfIf_vgNMdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c82cf41e.mp4?token=hAs-Md4kz7NTkwC3ptU5uks6tyVU_9AOmz89VzZtBOR9IEgQbLmGK5oZpDubIl92_C-peubOmMumSZmcSMva8Uq5zRnqmC7ah83xV1WrFpG5x4MgcAEkrwjoMpXTDC6Us4vN1PKubacuK9HcjnFKzb_eFjP0gjBcfP5O2z2MoRj1qsci9l9TNR4pHunJXYUGF9_QcVmk_TjEF_7TxjmC6P9s9-npJSKjEZuIealjaSxpegy3GQhXDGuxM_zvFjJQfsh1q2kfXkp3IeJilLOgk7W_k1cIKZ3E107nTiocnQCcm2yvsZ-SM2qbuRJ_EOIiNKh44gj8NhdfIf_vgNMdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی از قم با شرح پرتاب موشک
سایر پیام‌های دریافتی که شاید درباره پرتاب موشک باشند:
وحید شهرستان محلات صدای انفجار مهیب اومد . همه جا لرزید
23/44 صدا انفجار از دور ساوه
ساوه ۱۱:۴۵ دقیقه
صدای انفجار
سلام وحید جان صدای انفجار ساعت ۲۳:۴۰ ساوه
نزدیک قم یه صدای انفجار اومد
سلام وحید  الان صدای جنگنده خیلی نزدیک  دلیجان
صدای دو یا سه تا انفجار شنیدم اما خیلی فاصله بود. فکر کنم خمین با اراک بود.
ما خنداب هستیم.
قزوین صدای جنگنده [که معمولا با صدای پرتاب موشک اشتباه گرفته میشه.]
از دلیجان موشک پرتاب شد
ساوه صدایی اومد. مثل انفجار. ولی انگار از دور بود
اراک هم صدای یه انفجار از دور شنیده شد
وحید جان ما اراکیم یک ربع پیش سه بار صدای انفجار اومد اما بار اول صداش خیلی خیلی بلند بود
🔄
منابع حکومتی:
فرماندار اراک اعلام کرد که صدای شنیده شده مربوط به اقدامات آفندی در یکی از استان‌های مجاور است و جای نگرانی نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77282" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSVnFN_D3yQbcPuC6492X_t8yd-gvU5eAx7zsj_EtN3PgcyTlLzuKNegwfRJsXvu22Lb-kvij81rICiKfK4IiUFAKmRJ6h-GIAeBOxG1Ld4C4Z-EGeD6dML1-2ZodVa_DGEkUXD8dQTScxK2Le9Ww5nFT6rHyyMOZ4uOAaO88-d5Xf382wZvkiXtIrbdPy0N0J6O78Z816M9TCV-Hinfup-HA4mKhnS8DQnseSeWoR6BIAySy_Yf0t9xdzCVN9aY-yGWkCgS7-_MI6eFrceUp2JUFknlEXL1KCD6KRFV1dWhlV4SCy5JJXqUVWRcW8EIP3qtZsGNY8VDnow7fcMZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
به‌روزرسانی سنتکام درباره نظامیان آمریکایی جان‌باخته اخیر
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دیروز اعلام کرد که در پی حمله ایران در ۱۷ ژوئیه در اردن، دو نظامی آمریکایی جان باخته‌اند و یک نفر نیز مفقود شده است. پس از جست‌وجویی گسترده، نیروهای نظامی آمریکا اوایل امروز بقایای انسانی ناشناسی را در محل پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق روز ۱۸ ژوئیه هنگام انفجار کنترل‌شده مهمات منفجرنشده متعلق به یک پهپاد انتحاری سرنگون‌شده ایرانی، در جریان عملیات کشته شد. یک نظامی دیگر نیز زخمی شد و همچنان برای جراحت جزئی خود تحت درمان پزشکی قرار دارد.
سنتکام به احترام خانواده‌ها در جریان روند اطلاع‌رسانی، از انتشار اطلاعات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77281" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tnuyt8JoEShyBJqFDM24Yt6XgZXGiT05ItU2yFwztD2dwp-OV5ovgTNlSeh2d7UFUHHBsgdtnq9lyHJwLqc4hQ1IvQKWxEH3DIj3L0Hf8fC_1Jwf9Fo4eGbq1afEErEF4OU3u0kBzEyDEi7mHyHvL8gL-ncmSK0QTkfgLmx9xFCHbs6yExFxu9BBz3Gpc4Qho_Kt9VLdPgKLXLPCu2TAZdt5Q_CA32I-BBd4cLiW5lqHdxDbR1lQ9qznb40SBO6feHszo9rpXekaVMzRxsJ68_MjvhJuRoPg-HbIEvDsgxKHhe6r7NBBhpWLla3fKL2JY40IFbO2qvRssIgQ1858cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران گفته است آمریکا بامداد یکشنبه با «تعدادی پرتابه» به سایت در حال ساخت نیروگاه دارخوین حمله کرد. دارخوین شهری در بخش دارخوین شهرستان شادگان در استان خوزستان ایران است.
آژانس بین‌المللی انرژی اتمی اعلام کرد که در حال بررسی این گزارش‌هاست و یادآور شد که این نیروگاه «در مراحل بسیار ابتدایی ساخت قرار دارد و در آخرین بازدید آژانس، هیچ ماده هسته‌ای در آن وجود نداشت.»
آژانس افزود که این حادثه «احتمالاً هیچ خطر پرتوی ایجاد نمی‌کند»، اما رافائل گروسی، مدیرکل آژانس، با انتشار پیامی در شبکه ایکس «خواستار خویشتنداری نظامی در اطراف همه سایت‌های مرتبط با فعالیت‌های هسته‌ای» شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77280" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWt9AECqz_rREKo0AJMhVqfmAP6TV39MREdFJyCyZK5SnXxl2l1hve1f7BBVPJirLyt2jb8xwSktz7Gd5SNmbGG5S4B74KJLNkOXYt1lohi0euYZyTuO2dRu4prFua5GProH8rmfGl0sPjk9AJCgpXcOBDfdQ14xx4SMgaIZxGtLUG9Bxpc0rFVQElGbnSospKTzDhhEnrF3y-vnMAOFfpkcYbp8wZ57SHvanYuhM90QyVGqyhWazvTuIdH8UMsLIeOFp3_5CEXwkbkovFU74CKCXLayCD76gl15RfBSFvsFZgTALvZd3NJj2qAs2Vcu1-9DfnDLPn5uVhHrUOvZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی و انتظامی استانداری خوزستان عصر روز یکشنبه از «حمله موشکی آمریکا» به نقطه‌ای در اطراف شهر آبادان خبر داد.
ولی‌الله حیاتی اضافه کرد که این حمله کشته و مجروحی به جا نگذاشته است.
سنتکام، ستاد فرماندهی ارتش آمریکا در منطقه خاورمیانه، [هنوز] درباره این ادعا بیانیه‌ای منتشر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77279" target="_blank">📅 18:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1Z0zwXCEj6eP4ULNLCSxXpzwu0-doSqfH0t6A1C6NtSMTHWqO8yXP9hR0cTG6lMTtv372-gafDFkXOkoHWCKNRAks92drQTUY0r27vbgmPJXdNHYqNBFExBX-UkIZ6sJW_RxXe_Xk8h7XcKWhumqhBEArJLvo9bmaMcaU9swQoyFA4Bs7PsAot3DNpH1JUZd4q0oc0CqbTSf3ra63CHUGN7_PEYHpOW6NLCNDah4CeVg6vQ5SELhliJuelKKYDY8sFcz94XJmARG_0ifeZPyKwI437DOPxTpChU8XbHfXo-xPj9fRM24q6RMTTVHmvhnW6QMWeHfFa1ujzAVzfPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز یکشنبه اعلام کرد که نیروهای اسرائیلی و اردنی یک موشک ایرانی را که به سمت شهر عقبه در اردن شلیک شده بود، رهگیری کرده‌اند.
دقایقی پیش از این رهگیری، ارتش اسرائیل اعلام کرده بود که موشک‌هایی را که از ایران به سمت عقبه شلیک شده‌اند، شناسایی کرده و نسبت به احتمال «سرایت» حملات به خاک اسرائیل هشدار داده بود.
سخنگوی ارتش اسرائیل در پاسخ به پرسش خبرگزاری فرانسه دربارهٔ گزارش‌های مربوط به شنیده شدن صدای انفجار در نزدیکی شهر ایلات در جنوب اسرائیل گفت که نیروهای اسرائیلی و اردنی به‌طور مشترک یک پرتابه را رهگیری کرده‌اند.
در همین حال، ارتش اردن اعلام کرد که «سه موشک ایرانی را که خاک این کشور را هدف قرار داده بودند» ساقط کرده است و یک موشک دیگر نیز در منطقه‌ای بیابانی فرود آمده است، بدون آنکه محل دقیق آن را اعلام کند.
ایران در دور تازه درگیری‌ها با آمریکا که در هشت روز گذشته ادامه داشته است، اردن را در چند نوبت هدف قرار داده است. ارتش ایالات متحده اعلام کرده که در جریان حمله روز جمعه ایران به اردن، دو نیروی نظامی آمریکایی کشته شدند.
@
VahidHeadline
آپدیت:
اکانت ارتش اسرائیل، ترجمه ماشین:
⭕️
ارتش اسرائیل شلیک موشک‌هایی از ایران به سوی شهر عقبه در اردن، در مجاورت اسرائیل، را شناسایی کرد. چندین موشک رهگیر به سوی بقایای موشک‌ها شلیک شد تا از اصابت این بقایا به داخل اسرائیل جلوگیری شود.
هیچ خسارت یا جراحتی گزارش نشد. مطابق دستورالعمل‌ها، آژیرهای هشدار به صدا درنیامدند. این رویداد پایان یافته است.
آپدیت:
صفحه رسمی وزارت خارجه اردن در ایکس، از احضار کاردار سفارت جمهوری اسلامی در امان در اعتراض به حملات تهران به خاک اردن و اظهارات تحریک‌آمیز مقامات جمهوری اسلامی خبر داد.
در این بیانیه آمده سخنگوی این وزارت‌خانه به کاردار جمهوری اسلامی اعلام کرده است تا پیام روشن اردن مبنی بر توقف فوری حملات را به تهران منتقل کند. ...
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77278" target="_blank">📅 18:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/224ff6e0b2.mp4?token=OVrrJ_q1wlh9-glmbBxaaZv5F7bPbqmuRf7Sz_8wNCUT0dN5pWVy1im3VraxmfxXvVUxGMBAS96WyAvgzkSw8bdMMXvThdwRdJ7X9wNFwb5xVslNMuQRlX1hMVVEylehL9pvW67MmjUBbyjYDPR977Q_hxGar8rGXHrOhYLD7TAs5yyralb5GuhVBRbfrlcChnBIq2Le9-LOWf114PjpQn9r3oY3HEYNy3Nc-qyzSAUyQnqMnRhsFLY3AWAoZQBwXkCsDbVV_TcX9HeNhv77VDi_8KL9FPhQ0VlmaoP-GBX3iwhgqQxIZberTeBiczquN6cve-L0fKyKvRmASsU0c1mYLRSricXHylXEbxJMIlIxmDdPdcPyQGbOjpnD0FylpfEkUzxpvq-UzPtt2RVh-vRLY1lj8XAPeI6AKzGDFONrG1iECZsbdIUHZTfb4Ebprfeg93bLYqkWvijy_UXh2_Z88N2t3Dkl4UxFKTiJ0cfAb4llAnNZwCbhGr7RkWD-HjCxVmRzOZoZri1MCGUA-Zxr_55erOuSHBRLdIxSqVjdmwYY5ZRMV9cFm1mATTOGnG9kWmeTl4L_ThpYLi44gJgFejbyJcZSOVk3fMTd06LknT4_dpMtFo4R-s-AwSIv81JJAzQxrEgtycos4vd7KB6BT1PSZymeu0vZq4Z9ga8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/224ff6e0b2.mp4?token=OVrrJ_q1wlh9-glmbBxaaZv5F7bPbqmuRf7Sz_8wNCUT0dN5pWVy1im3VraxmfxXvVUxGMBAS96WyAvgzkSw8bdMMXvThdwRdJ7X9wNFwb5xVslNMuQRlX1hMVVEylehL9pvW67MmjUBbyjYDPR977Q_hxGar8rGXHrOhYLD7TAs5yyralb5GuhVBRbfrlcChnBIq2Le9-LOWf114PjpQn9r3oY3HEYNy3Nc-qyzSAUyQnqMnRhsFLY3AWAoZQBwXkCsDbVV_TcX9HeNhv77VDi_8KL9FPhQ0VlmaoP-GBX3iwhgqQxIZberTeBiczquN6cve-L0fKyKvRmASsU0c1mYLRSricXHylXEbxJMIlIxmDdPdcPyQGbOjpnD0FylpfEkUzxpvq-UzPtt2RVh-vRLY1lj8XAPeI6AKzGDFONrG1iECZsbdIUHZTfb4Ebprfeg93bLYqkWvijy_UXh2_Z88N2t3Dkl4UxFKTiJ0cfAb4llAnNZwCbhGr7RkWD-HjCxVmRzOZoZri1MCGUA-Zxr_55erOuSHBRLdIxSqVjdmwYY5ZRMV9cFm1mATTOGnG9kWmeTl4L_ThpYLi44gJgFejbyJcZSOVk3fMTd06LknT4_dpMtFo4R-s-AwSIv81JJAzQxrEgtycos4vd7KB6BT1PSZymeu0vZq4Z9ga8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی در یک مصاحبه ویدیویی اعلام کرد که از زمان آغاز دوره جدید رهبری، شخصا با مجتبی خامنه‌ای دیدار نکرده و تنها افراد محدودی موفق به ملاقات با او شده‌اند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، با اشاره به دلیل کشته شدن رهبر سابق جمهوری اسلامی می‌گوید هنوز این احتمال هست که در رده‌های بالای حکومت «حفره امنیتی» وجود داشته باشد.
او در گفت‌‌وگو با یک مستندساز حکومتی در تهران که بخش‌هایی از آن روز یکشنبه ۲۸ تیر منتشر شده است، با اشاره به «وجود عوامل نفوذی در بالاترین سطح نظام» گفت:‌ «نفوذ فقط در گرفتن اطلاعات نیست، بلکه در تصمیم‌سازی هم هست، در جهت‌دهی به فضای روانی هم هست.»
او تأکید کرد بمباران «بیت رهبری» که در جریان آن علی خامنه‌ای و شماری از فرماندهان ارشد نظامی ایران کشته شدند، از طریق یک «حفره امنیتی» صورت گرفت و افزود که این حفره همچنان وجود دارد.
به گفته عراقچی، در روز ۹ اسفند ۱۴۰۴ که حمله مشترک اسرائیل و‌ آمریکا به ایران آغاز شد، علاوه بر دفتر علی خامنه‌ای، دفاتر علی شمخانی و محمد شیرازی، دو مقام نظامی، و علی‌اصغر حجازی، مقام امنیتی بسیار نزدیک به خامنه‌ای، هم هدف قرار گرفت. از این میان، فقط حجازی زنده ماند.
جواد موگویی که با عراقچی مصاحبه کرده است، در جریان این گفت‌وگو توضیح می‌دهد که علاوه بر جلسه خامنه‌ای با مقام‌های دفاعی کشور، در آن روز یک جلسه بسیار مهم دیگر هم برقرار بود: جلسه شورای معاونین وزارت اطلاعات در نقطه دیگری از تهران.
به نظر می‌رسد اشاره او به جلسه‌ای است که اسرائیل اعلام کرد در نخستین ساعات حملات مشترک با آمریکا، آن را هدف قرار داد و چند تن از اعضای بلندپایه وزارت اطلاعات جمهوری اسلامی را کشت.
ارتش اسرائیل روز ۱۱ اسفند پارسال اعلام کرد سید یحیی حمیدی، معاون وزیر اطلاعات در امور «اسرائیل»، که به گفته آن «فعالیت‌های تروریستی علیه یهودیان، بازیگران غربی و مخالفان رژیم در داخل ایران و خارج از کشور را هدایت می‌کرد»، جزو کشته‌شدگان است.
جلال پورحسین که از او به عنوان «رئیس بخش جاسوسی» وزارت اطلاعات نام برده شده، نیز بر اساس اطلاعیه ارتش اسرائیل ازجمله کشته‌شدگان است.
رسانه‌های ایران پیشتر خبر کشته شدن محمد باصری، از مقام‌های ارشد وزارت اطلاعات، را در حملهٔ روز ۹ اسفند اسرائیل تأیید کرده‌ بودند.
@
VahidHeadline
عراقچی همچنین ادعای منتقدان مبنی بر اینکه مذاکرات زمینه‌ساز جنگ شده است را رد کرد و گفت جمهوری اسلامی در مذاکرات بر موضع خود درباره غنی‌سازی ایستادگی کرده و پس از ناکامی مذاکرات، طرف مقابل گزینه نظامی را انتخاب کرده است.
عراقچی همچنین گفت برای احتمال کشته شدن رهبر جمهوری اسلامی نیز سناریوهایی طراحی شده بود و «این سناریوها حتی کد مشخص داشتند»، هرچند به گفته او در جلسات تصمیم‌گیری کسی تمایلی به طرح آن‌ها نداشت.
@
VahidHeadline
عباس عراقچی درباره فرایند تصمیم‌گیری درباره مذاکره با آمریکا گفت: «آن زمان [بین دو جنگ] کمیته هسته‌ای را در داخل دبیرخانه شورای عالی امنیت ملی تشکیل دادیم که اکنون به کمیته مذاکرات تبدیل شده است و به کمیته شش نفره معروف است.»
«تمام بحث‌های مربوط به مذاکرات، در این کمیته صورت می‌گرفت و مصوبات آن، عینا همان روال مصوبات شورای عالی امنیت ملی را طی می‌کرد.»
به گفته عباس عراقچی، ریاست این کمیته ابتدا بر عهده علی شمخانی و سپس علی لاریجانی بود که هر دو در حملات آمریکا و اسرائیل کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77274" target="_blank">📅 18:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77270">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWjt5h9nVP-_fgZzrWr8RNq6bZnqzyyANzJijvmBOCdiBT1jpewI4dpQ5D6e2-FEiEM5Adtzj0GQagf5ebAdjfTRe3-hXKxtqCYPcO9dQBOgZVGBPSIPYbHYkiZO526v4eGZQmX8Scxj4faSTQkcCQXDyg89Tr6AtQMTXYOx-rO_F3PTC-Ki4i6822u8zIgRCMdtCpk0elOi28V8axowYwxAy9G3xx0ikgzg2V5oMSMkystvPHDw3RWtzmMrQFrvRtXu-ydCyhBUN3zaDmAW-Qj4XwiShTVXWlW1z9Vg4bpso_Jupbf01fWwZSiPWGsxLaQrqVKre6qXlZH_u8ekzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d80bc4cf46.mp4?token=LUgNIcYFzUIp1vai3YTSiAi9m8fY3tuNPvzAZoXH0OdTydQm9W6Rlw-IkDSrOmDPYytlCPgGKNW5b7wybtXusRDPW-C1Q6JmYs20yuGsKhdlwi7PkI4y5VnvE7CubwuN3x_FOkkyC6N93dpapXRM5-bLQdbgY8NMMOqnznPoW-wXXDYXXGuDILrvgIXIKw-q_pbMsc956S_bFT0PzpIVwK-fVXySF-D2nI4hFyLA7wY7AWHwdl-h6CiM_RCUVG8t6hX6cegbyo-OoEKvIseY1DlSqt0cMHz_egx-fhFm23-AikiXO5FGxtqZBgiMnroKLzbbx1mGYVivs-Hvez0S0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d80bc4cf46.mp4?token=LUgNIcYFzUIp1vai3YTSiAi9m8fY3tuNPvzAZoXH0OdTydQm9W6Rlw-IkDSrOmDPYytlCPgGKNW5b7wybtXusRDPW-C1Q6JmYs20yuGsKhdlwi7PkI4y5VnvE7CubwuN3x_FOkkyC6N93dpapXRM5-bLQdbgY8NMMOqnznPoW-wXXDYXXGuDILrvgIXIKw-q_pbMsc956S_bFT0PzpIVwK-fVXySF-D2nI4hFyLA7wY7AWHwdl-h6CiM_RCUVG8t6hX6cegbyo-OoEKvIseY1DlSqt0cMHz_egx-fhFm23-AikiXO5FGxtqZBgiMnroKLzbbx1mGYVivs-Hvez0S0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خواننده زیرزمینی زن که با نام «آنیتا پاپیست» در ایران فعالیت می‌کند روز شنبه با انتشار حکم قضایی‌اش خبر داد که در دادگاه به ۷۴ ضربه شلاق محکوم شده است.
آنیتا که ویدئوهای آوازخوانی خود را در شبکه‌های اجتماعی منتشر می‌کند، طبق آن چه در این حکم آمده، به دلیل «جریحه‌دار نمودن عفت عمومی» به این مجازات محکوم شده است.
این خواننده همچنین تصویری از رسید توقیف پاسپورتش در فرودگاه را منتشر کرده و خبر داده است که خط موبایلش هم مسدود شده است.
یک ماه پیش دادگاه کیفری استان قم پرستو احمدی، خواننده، و هشت نفر دیگر از دست‌اندرکاران و نوازندگان «کنسرت کاروانسرا» را به‌ طور جداگانه به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال ممنوعیت از فعالیت هنری محکوم کرد.
این خبر به‌سرعت در صدر اخبار قرار گرفت و واکنش سازمان عفو بین‌الملل را نیز به دنبال داشت، اما خبر حکم شلاق برای دو خواننده زن دیگر و اخبار این‌چنینی این روزها به دلیل اخبار جنگ و حملات بی‌وقفه به جنوب کشور مورد توجه قرار نمی‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77270" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8YIL2qCSnCbHYau2AUws66okddCRTbksYmSbtBZs2r7-1CBuaOOsPf_oYcRr5yJOc_c2vhxJcdK7Ob7ZIegOqK-TQl8PDJmlmFSG0h6YnYUowR9omIvxelToUoAZw777moz5JFVFxUnnsGWcIAxYDzTNFLw28SdzNKBkecepQ-zAnR7-Tek9UE_QXPewy0UXK4pvUkHiVgiVoNtvtjOwJ6JD6OH1DMfmpqH8kPhRMoI_FxEh5wGBoJuYkDwW7oj1yBvCHONwsJdt8pAo0sLRZdXTpNnsarTJggKoXLiBFF02d-KG98f-n5lqBgDCqUGMYpPItThGVbIOj_R_QHP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنا کراری، شهروند دو تابعیتی ایرانی-آمریکایی که پس از حدود ۱۹ ماه ممنوع‌الخروجی و محدودیت‌های امنیتی سرانجام ایران را ترک کرده بود، به ایالات متحده رسید. هم‌زمان، مقام‌های جمهوری اسلامی همچنان روایت منتشر شده درباره آزادی او را رد می‌کنند.
جرد گنسر، وکیل دنا کراری، با اشاره به «۵۶۶ روز بازداشت ناعادلانه دنا کراری توسط حکومت ایران» از همه افرادی که در آزادی او نقش داشتند قدردانی کرد و افزود: «اکنون باید تلاش‌های خود را برای آزادی سایر شهروندان آمریکایی که همچنان در ایران هستند، دوچندان کنیم.»
خبر خروج دنا کراری از ایران نخستین بار روز ۲۴ تیر از سوی دونالد ترامپ، رییس‌جمهوری آمریکا، اعلام شد. ترامپ در شبکه اجتماعی «تروث سوشال» نوشت ایران به یک شهروند آمریکایی که به گفته او از دسامبر ۲۰۲۴ «به ناحق» بازداشت شده بود، اجازه خروج داده و این اقدام را «نشانه‌ای از حسن نیت» جمهوری اسلامی توصیف کرد.
اندکی بعد، جرد گنسر هویت این شهروند را تأیید کرد و گفت دنا کراری پس از ماه‌ها محدودیت امنیتی، در مسیر بازگشت به ایالات متحده قرار گرفته است.
با این حال، خبرگزاری میزان، وابسته به قوه قضاییه، گزارش‌های منتشر شده درباره آزادی یا مبادله یک شهروند آمریکایی را تکذیب کرد و مدعی شد هیچ «زندانی محکوم یا جاسوس آمریکایی» از زندان‌های ایران آزاد یا مبادله نشده است.
با وجود این تکذیب، میزان به اصل خروج دنا کراری از ایران یا لغو ممنوع‌الخروجی او اشاره‌ای نکرد و توضیحی درباره چگونگی ترک ایران از سوی این شهروند دوتابعیتی ارائه نداد.
دنا کراری، ۵۳ ساله و ساکن کالیفرنیا، سال ۲۰۲۴ برای دیدار با اعضای خانواده خود به شیراز سفر کرده بود. به گفته وکیلش، گذرنامه او در ایران ضبط شد و اجازه خروج از کشور را از دست داد. هرچند او هرگز به‌طور رسمی زندانی نشد، اما طی ماه‌های بعد بارها از سوی نهادهای امنیتی بازجویی شد و تحت محدودیت‌های شدید قرار داشت.
بر اساس گفته‌های وکیلش، مقام‌های جمهوری اسلامی او را با اتهام‌هایی از جمله «همکاری با دولت متخاصم» و «جاسوسی» مواجه کرده بودند؛ اتهام‌هایی که کراری و وکلایش آن‌ها را بی‌اساس دانسته‌اند.
گنسر همچنین گفته است حساسیت نهادهای امنیتی نسبت به موکلش به فعالیت او در «بنیاد کودکان مهر» بازمی‌گردد؛ یک سازمان غیرانتفاعی ثبت‌شده در آمریکا که با مجوز دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) و با کمک‌های مالی خصوصی، از کودکان کم‌برخوردار در ایران حمایت می‌کرد.
برخی رسانه‌های بین‌المللی نیز گزارش داده‌اند که کراری علاوه بر فعالیت در یک شرکت فناوری آمریکایی، مدیریت این موسسه خیریه را برعهده داشته؛ موضوعی که به گفته نزدیکانش، به افزایش حساسیت نهادهای امنیتی جمهوری اسلامی نسبت به او انجامیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77269" target="_blank">📅 17:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HgucFNe2n3rrKTqpVcDJbrktzrv2bgj5W_T4hFd9eVS3_5lYwYOESlXNqY0Ujm7it-nO82ukNKKS23ObNd73xhREnz0h5USMpCCc3D-Jq8uUhhdPyvCnMM2y2LmFH1TgARbHPh6zzdYbk_TKAZ20A0eUJAHJJabhsEOcympJ2ADqjHdfyE2nhXoa-cr-4NJ61aj4A3gAcPbJCno4kYobCaeqkpjxdxEAXmHBjXjSQuXx14Osh96WnxAh350NuigyEHiJJMv1Fczjo5Vj691Ayx7TuaWxnB1-rQRZ89zwmQtVb198hOTzBOuVE2j0e7d_aUfnR_n7AHdW2pkC9ttqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه، روز یک‌شنبه خبر داد که حکم اعدام عرفان اسفندیاری و گل‌محمد محمدی، دو تن از جوانان معترض دی‌ماه ۱۴۰۴ متهم در پرونده موسوم به میدان علیخانی اصفهان، در بامداد همین روز اجرا شده است.
هفته گذشته کمیته پیگیری وضعیت بازداشت‌شدگان در ایران هشدار داده بود که حکم اعدام ۱۲ نفر از معترضان دی‌ماه در اصفهان در پرونده موسوم به «میدان علیخانی» این شهر، در دیوان عالی کشور «تأیید شده» است.
در میان این ۱۲ نفر که برخی از آن‌ها به دو، سه و حتی چهار بار اعدام محکوم شده‌اند، چندین نوجوان و یک شهروند افغانستان نیز دیده می‌شود. بنا بر گزارش‌ها، گل‌محمد محمدی شهروند افغانستان بود.
این پرونده به وقایع ۱۸ دی‌ماه ۱۴۰۴ در محدوده میدان علیخانی، بین ملک‌شهر و کاوه اصفهان بازمی‌گردد، جایی که مقام‌های جمهوری اسلامی اعلام کردند چهار نیروی بسیج و یگان ویژه به نام‌های حسین رمضانی، محمد همتی، سید علی خشوعی و ولی‌الله صفری کشته‌ شده‌اند.
در پی کشته‌ شدن آنها، ۵۹ نفر در اصفهان بازداشت شدند و برای آنها پرونده‌ای گسترده تشکیل شد.
@
VahidHeadline
این رسانه حکومتی معترضان را به «آتش زدن ساختمان‌ها، تخریب تابلوهای شهری، دوربین‌ها و چراغ‌های راهنمایی و رانندگی، تخریب پاسگاه و کلانتری، آتش زدن لاستیک، مسدود کردن خیابان، حمله به مردم در حال تردد در خیابان و تخریب مسجد» در جریان تجمعات ۱۸ دی در میدان علیخانی متهم کرد.
بر اساس این گزارش، «عوامل دشمن» در اعتراضات ۱۸ دی به «انواع سلاح گرم، چاقو، قمه، قداره و کوکتل مولوتوف» مجهز بودند و در جریان درگیری آن‌ها با نیروهای جمهوری اسلامی در میدان علیخانی، چهار مامور انتظامی کشته شدند.
در پرونده میدان علیخانی ۱۲ نفر به اعدام محکوم شده‌اند.
در زمان اجرای حکم اعدام، اسفندیاری ۱۹ سال و محمدی ۲۴ سال سن داشتند.
۱۰ متهم دیگر این پرونده که زیر حکم اعدام قرار دارند، به سلول انفرادی منتقل شده‌اند و نگرانی‌ها درباره احتمال اجرای قریب‌الوقوع حکم آن‌ها بالا گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77268" target="_blank">📅 17:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اگر صدایی شنیدید و خواستید به من هم اطلاع بدید لطفا فقط بگید صدا شنیدم. یا نور دیدم، زمین لرزید... یعنی لطفا تفسیر نکنید که: زدند!
آبادان تک صدای انفجار از دور ۱۶:۳۸
سلام همین الان ابادان رو زدن برق هم نداریم
صدای انفجار آبادان همین الان
همین الان صدای انفجار یا شلیک موشک از آبادان
نمیدونم دقیقا کجای شهر بود
سلام ابادان همین الان ۱۶:۴۰ صدا شنیدیم
سلام وحیدجان همین الان صدای مهیب انفجار از آبادان
همین الان آبادان رو زد نمیدونم کجا بود ۱۶:۴۰
آبادان صدا انفجار
صدای انفجار ۱۶:۳۹ آبادان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77267" target="_blank">📅 16:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیام‌های دریافتی الان درباره شنیده شدن صدای انفجار که می‌تونه انفجار پرتاب موشک باشه، انفجار شلیک پدافند باشه و...
سلام وحید جان
الان ۴:۳۱ صدای انفجار اومد، کرمانشاهم
کرمانشاه صدای انفجار اومدددد
وحید جان (۱۶:۳۲)  کرمانشاه دو انفجار مهیب. احتمالا داخل شهر یا بسیار نزدیک به شهر
سلام وحید جان
کرمانشاه 4:31، دو تا انفجار بزرگ صدای جنگنده خیلی نزدیک و زیاد
همین الان کرمانشاه صدای وحشتناکی اومد
صدای پدافند نبود
الان 2 صدا انفجار آمد کرمانشاه
سلام همین الان کرمانشاه صدای وحشتناکی امد
ما شریعتی هستیم
وحید الان کرمانشاه ساعت ۴:۳۲ زدن
سلام وحید جان الان صدای ۱ انفجار از کرمانشاه اومد
صدای شلیک موشک آسمان کرمانشاه ساعت 16:30
دو تا موشک کرمانشاه خیلی نزدیک بود.
انگار تو شهر بود
صدای سوت موشک کامل پیچید
کرمانشاه ارسال موشک ساعت 16 و 32
دو پرتاپ موشک
[هنوز از اخبار ساعت‌های گذشته بی‌خبرم]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77266" target="_blank">📅 16:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h9BX8r6pu3bo5UR3Nv9Q2OzUcZmK-zMagE1bHWazOB6vlukgMicnDnKDv8pUvk6bqFGWfIxJAx2WeMgRirPlOXLs6iII5PfY46V3-QxajZrvJd_pmL9-mHnY4EwgnCkUsfHjh_s4WihpQ181QEAmKskRee8s3q__Ww2a7GkA1uWpn3E9U82cztl0d5ygJcuA59f-q68l75nr2nMhyPUHJfbyqQNA0dy9ip7WUUptY3SaTzBbFtVnfcCuAQ9aneIehUqkbVYVrN1GP6mlbes7gwH9ryKOLoyw7vbo2f6v25WXyW7rb6o5OAVH3nTx-5XVtw-yCXmQxz2aJ1EV_CyPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار در کویت هم‌زمان با پیام‌ها درباره پرتاب موشک از خوزستان
آپدیت:
ستاد کل نیروهای مسلح کویت در بیانیه‌ای رسمی اعلام کرد پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی «متخاصم» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77265" target="_blank">📅 10:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیام‌های دریافتی:
صدای یک انفجار چابهار اومد دور بود فقط موجش بود
09:42 بدجور زد الان چابهار رو نمیدونم کجا بود
چابهار یهو صدای انفجار اومد شیشه هامون لرزید
🥲
قبلا تو روز روشن نمیزد
چابهار یچی زدن همه ریختن بیرون ولی نه سمت اسکله نه پایگاه امام علی اصلا هیچ دودی هم نیست به شدت لرزوند
آپدیت: منابع حکومتی
فرمانداری شهرستان چابهار: صدای انفجار شنیده‌ شده در روز جاری (۲۸ تیر) در حوالی شهر چابهار، ناشی از عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77264" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bXy3GlVI39CcC_eBlIYPcEmq-JsQaTzSunjCW5lczBiBldMsgN5jrdQCf9issxzLV7jJdoDL0l6vfuaxFPj2utHgOP6s_aWZasR_zbMhgU58rjqEvV-vl9qIx7VEKYhJXDcHGUALWjIt9KQQrCQINt2yqm7UBEiu54lxZWiElK8QC4k0AdQyg4EAj88QeG-Kqe4PX1E3QT3SqnTAwZfSOf0xEOo3n_vlevsXMR9URS17f3rwL4Rkxl344pkTIa8GSZ4snlvjiJF1qtvhj3fAnGQU5yMEW8CDQpmOQvDSQQHnC3V9AxZikNM2Fkdcz1rfe1cZu6Osl5GP7EhS-y8egQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های ساعت ۹:۰۹
سلام وحید همین الان گرگان زلزله اومد نسبتا شدید بود
آقا وحید گرگان گلستان الان ساعت 9:09 صبح هم لرزید، زلزله بود
سلام گرگان الان زلزله اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77263" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rb2yjM3VtREgjBJJVN-dn9gPi1ZIHBkQktsHOp8jbKKgVnuceBY53TQgl1Ep7eFVoLUINjUfrRTnj4NleVeJV_VA0gG2hPYWdHPlQKsgJ8H4DrFOghGCckGvrDbNuN6K1L3eD4EKxFJM_UfE-BGqExmm2geo8NlQwDBOG4ja-oAG9C1m8yD-RyCWGC25Aemy8EJRyuNumAjIE3uvaVbvmZ9rWcvbpNlahWeQ1jQQnznu3zEbeFu0GNW2YHCvfoPE3VdaqQoNRascRvazKTob4PUM6mVIv5FTUHkTFwXYohEhkHoNEWgH8b6hQb4Z_ea-aZqjFZNVhBgho8tTgHjehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت: زمین‌لرزه به بزرگی ۴
دوباره
در سالند خوزستان
پیام‌های دریافتی:
۷:۵۷ اندیمشک دوباره زلزله اومد
دزفول لرزید دوباره
اهواز دوباره زلزله اومد
دزفول لرزید بازم فقط شدتش خیلی کمتر بود
زلزله ۷ و ۵۷  دقیقه باز هم دزفول با شدت کمتر از قبلی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77262" target="_blank">📅 07:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77261">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj8qZVOnhx_nPxJRrGXBoKkBFTO_ppsFwJFO_6jxeW9cLFvHJ_gEG-KuT5s_pUnIukWSPOiVFEFQiqFf1uH77mKYuXeT1lXbVD5kUstMD-eqmFn5YFcOFstV9dIbtI0wCRqKGKrnN7BRRDmHrgCC2AWAa5Vjkz3qEeGg3vp0Y08zQ7m_-pR1He45KZ5DrIW0BbsCUMbiOb82GJ1sD4i02tVkgqP3wbgpHKRx98dDzKRkgZEH7Vyn6YhcwSOMMqET_HEPtYKtLs64WJZRlMIyCULnBon3Oa7hCxQsxccstZYh01m0WHTEO_Xa8qQlWzz95Qe_SjMPNsou0eFO9fTQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه سقوط ارزش ریال، قیمت ارز، طلا و سکه در بازار ایران به سطوح تازه‌ای رسیده است.
براساس نرخ‌های ثبت‌شده در روز ۲۷ تیر، قیمت هر دلار در بازار آزاد به حدود یک میلیون و ۹۴۵ هزار ریال، معادل ۱۹۴ هزار و ۵۰۰ تومان رسیده است. یورو نیز حدود ۲۲۳ هزار تومان و پوند بریتانیا بیش از ۲۶۲ هزار تومان قیمت‌گذاری شده‌اند.
در بازار طلا، قیمت هر گرم طلای ۱۸ عیار به حدود ۱۹ میلیون و ۱۳۸ هزار تومان و هر مثقال طلا به حدود ۸۲ میلیون و ۸۹۵ هزار تومان رسیده است.
قیمت سکه نیز یک میلیارد و ۹۰۰ میلیون و ۵۰ هزار ریال ثبت شده که معادل بیش از ۱۹۰ میلیون تومان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77261" target="_blank">📅 07:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b791da5472.mp4?token=tnDixhDyfnny_uo5xzc0jHPbZ6BxHsUJ49EscSFzh5bl1kr9pHKaCAZ8CdgombDrPMu_XnSFaY9Yp_olbUaflNHdfTWfYYSt1E0y0n7LKGKiVXlPu_w4xASBOdzWjLZJd3PB9sn98Q7gmKlxdUNIaCfIhJbuCg4yvyCjxXPRLFEJ6YmJzqHRG4qnMoFZw0INPVPGv3eu_XXXY16h6gWqeuoKOTzo-26MyMTMWVjUFy7AuHN0mYemuENuJrWR_1XfC8BfOBLndFcfmROc6dLQYP7xEngwpznN9mdEAwgeLZ6qwwM2XSS7RLvqRA_A80VZqL0xLmI5dwYhhEnnbQAP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b791da5472.mp4?token=tnDixhDyfnny_uo5xzc0jHPbZ6BxHsUJ49EscSFzh5bl1kr9pHKaCAZ8CdgombDrPMu_XnSFaY9Yp_olbUaflNHdfTWfYYSt1E0y0n7LKGKiVXlPu_w4xASBOdzWjLZJd3PB9sn98Q7gmKlxdUNIaCfIhJbuCg4yvyCjxXPRLFEJ6YmJzqHRG4qnMoFZw0INPVPGv3eu_XXXY16h6gWqeuoKOTzo-26MyMTMWVjUFy7AuHN0mYemuENuJrWR_1XfC8BfOBLndFcfmROc6dLQYP7xEngwpznN9mdEAwgeLZ6qwwM2XSS7RLvqRA_A80VZqL0xLmI5dwYhhEnnbQAP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا هشتمین شب متوالی حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) به دستور فرمانده کل قوا، دور دیگری از حملات علیه ایران را در ۱۸ ژوئیه ساعت ۱۱:۳۰ شب به وقت شرق آمریکا به پایان رساند.
در هشتمین شب متوالی حملات آمریکا، نیروهای سنتکام با موفقیت تأسیسات نظارت ساحلی و پدافند هوایی ارتش ایران، توانمندی‌های دریایی و محل‌های ذخیره موشک و پهپاد را هدف قرار دادند تا تضعیف توانمندی‌های نظامی ایران ادامه یابد. تجهیزات نظامی آمریکا همچنین نیروهای سپاه پاسداران انقلاب اسلامی را که در ۱۷ ژوئیه به نیروهای آمریکایی در اردن حمله کرده بودند، هدف قرار دادند.
بیش از ۵۰ هزار زن و مرد نظامی آمریکایی در سراسر خاورمیانه مشغول عملیات هستند. آن‌ها همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77260" target="_blank">📅 07:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">منابع حکومتی:
‌معاون امنیتی ‌استانداری خوزستان: ‌جنگنده‌های‌ آمریکا ساعت ۰۵:۵۵ دقیقه یک نقطه در اطراف شهر شادگان را مورد اصابت موشک قرار دادند.
ساعت ۶:۱۰ صبح امروز جنگنده‌های آمریکایی بار دیگر مناطقی در جزیره قشم را هدف حمله قرار دادند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77259" target="_blank">📅 06:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77258">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پیام‌های دریافتی:
الان دو تا افنجار بندرعباس ۶:۹
اصلا تا حالا این ساعت حمله نمیکردن!
وحید جان ساعت ۶ و ۹ دقیقه قشم صدای چند انفجار اومد باز
وحید ساعت ۶:۰۷ دقیقه دو بار قشم صدای انفجار و لرزش
دو سه ثانیه قبل از زلزله،صدای بمب سنگرشکن اومد،قشنگ از دوران جنگ تو گوشم صداش هست
بندر عباس ساعت 6:09 دقیقه مورد اصابت قرار گرفت دوباره
سمت پایگاه هوایی دو انفجار بلند
یکی دیگه هم الان زدن ساعت ۶:۱۰
سلام بندرعباس رو زدن ۳صدای انفجار پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77258" target="_blank">📅 06:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sISLIhVQ-xt1kVbPEZMiZvzSDyFx1TVecwNq9Q9qP72kHdTDlvqVlHHUuYzSB80XrDPAo1puQ1HGSSE9YqNqIuNy5APlSizAwQ_6h-wnN795dsY_xUn0JripPxNzVFLf1a3lC6fmDie4bW2xsF6szYRsAhpJd0zMQuD6DjioEelVFPk99pwDnpaHIOTOXErZHqjcovfa1F8MICva30GKbDtaX17NBtHmgBqKlLaRxcAeCIHJNzyzISd4Zwx2dGBeLkFrZB8xBKpLHmlcRK-Cx8qkAEXYL0ufa0mSA2ILqFkuUgOA47fzmHcOZA9fLvSBhDWnw6B64U3DQ-AMoH0X9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
زمین‌لرزه به بزرگی ۵ در عمق ۱۲ کیلومتری زمین در سالند خوزستان
پیش از آپدیت:
پیام‌های دریافتی درباره لرزش زمین:
وحید جان همین الان زمین لرزه شدید شهرستان شوش
خیلی بد بود
دزفول  رو زدند
همین الان تکون خورد همه جا مثل زلزله بود
زلزله اهواز
خونه لرزید بد جور دزفول چ خبرههه
همین الان اهواز زلزله اومد
5:55 دزفول
از توی خواب پاشدم،تخت و خونه و تمامی وسایل داشتن با شدت بالا میلرزیدن
اصلا نمی‌دونم زلزله بود یا جایی رو زدن
اقا وحید اهواز همین الان زلزله اومد 5:56
اهواز ۲ بار پشت سر هم زلزله اومد
ساعت ۵:۵۵
یکم ترسناک بود
اهواز زمین لرزه اومد
خیلییی شدیدددد تمام خونه لرزید
سلام اهواز زلزله شدید ۶ صبح
همین الان اهواز خیلیی بد لرزید
زلزله اهواز ساعت ۵ و ۵۵
اندیمشک هم زلزله شدید امد
ماهشهر زلزله نسبتا خفیفی اومد
سلام زلزله اهواز شدید مثل اینکه از دزفول بود
سلام آقا وحید اهواز الان زمین لرزه حساس کردیم،ساعت ۵ و ۵۷ دقیقه صبح
وحید جان دزفول همین الان زمین لرزه شدددد
زلزله اهواااز
از خواب پریدم کامل تخت تکون میخورد
زلزله اهواز اومد وحید کل خونه لرزید
ساعت ۰۵:۵۵
از خواب پریدم از شدت زلزله
اهواز چندبار لرزید بدون صدا
وحید جان الان اهواز زلزله ساعت ۵.۵۵
سلام زلزه اومد اهواز‌
وحید از خواب بیدارم کرد
و طولانییی بود
سلام وحید جان ساعت 5:56 دقیقه زمین لرزید ویه تکون خیلی شدید خورد خونه دزفول
سلام وحید جان ساعت ۵:۵۶ صبح زلزله فوق شدید اهواز همه چی داشت تمون میخورد
همین الان اهواز زلزله ، وحشتناک بود
سلام اهواز زمین لرزه بزرگی اومده حدود 10 15 ثانیه خونه داشت میلرزید
زلزله خیلی شدید اهواز ، ۲ بار تقریبا پشت سرهم ساعت ۵:۵۷
اهواز ساعت ۵:۵۵ خونه بد لرزید انفجار نبود انگار زلزله اومد
اهواز ساعت 5:55 دوبار زلزله اومد
آقا وحید زمین لرزه شدید اهواز در حدی که مبلا از جاشون تکون خوردن
سلام زمین لرزه اندیمشک هم حس شده
سلام شوش دانیال همین الان لرزید. انگار زلزله بود
دزفول  ساعت ۵:۵۶ صبح چند دقیقه ناجور لرزید
اهواز زلزله اومد هنوز لوسترها تکون میخوره
سلام وحید خوزستان لالی خیلی شدید زلزله اومد۵:۵۵
مسجدسلیمان هم زلزله حس شد ۵:۵۶
درود ایذه دو بار لرزید الان‌
سلام ساعت 6.55 شوش بدجور لرزید اما خیلی کوتاه ولی خیلی ترسناک بود
سلام ساعات 5:55 گتوند خوزستان زلزله احساس شد لوسترا تکون میخوردن
سلام زلزله سمت دزفول خیلیییی شدید بود یکم دیگه ادامه میداشت من خودمو از تراس پرت میدادم
اینقد طولانی بود که موقعی که بیدار شدم رفتم توی تراس هنوز قطع نشده بود توس عمرم اولین بارم بود همچین چیزی حس کرده بودم
🔄
پیام دریافتی به نقل از مرکز لرزه‌نگاری کشوری:
گزارش مقدماتی زمین‌لرزه
بزرگی: 5
محل وقوع: استان خوزستان - حوالی سالند
تاریخ و زمان وقوع به وقت محلی: 1405/04/28 05:55:21
طول جغرافیایی: 48.61
عرض جغرافیایی: 32.58
عمق زمین‌لرزه: 12 کیلومتر
نزدیک‌ترین شهرها:
23 کیلومتری سالند (خوزستان)
27 کیلومتری اندیمشک (خوزستان)
29 کیلومتری دزفول (خوزستان)
نزدیکترین مراکز استان:
103 کیلومتری خرم آباد
140 کیلومتری اهواز
📍
آمریکا هم
میگه
بزرگی زلزله ۴٬۹ بوده در عمق ۱۰ کیلومتری همونجاها:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77257" target="_blank">📅 05:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77256">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس همین الان صدای چهارتا انفجار اومد
03:33 سه تا پشت هم صدا اومد بندرعباس ولی فکر میکنم دور بود
همین الان بندر عباس صدای 4 انفجار
الان وحید جان ۳:۳۳ چهاتا انفجار شدید بندرعباس
همین الان قشم
صدای ۶ تا افجار پشت سر هم
خیلی بلندو قوی بود
کل پنجره ها لرزید
سلام ساعت۳:۳۴ صدای سه تا انفجار قوی اومد بندرعباس
سلام بندرعباس ساعت ۳ نیم صدای ۴ انفجار شنیده شد
بندرعباس ۴ تا الان زدن
#بندرعباس
28 تیر ساعت 03:33
صدای 4 انفجار سریالی،محدوده پایگاه هوایی
۴ تا انفجار سنگین در بندرعباس
بندرعباس 3:33 تقریبا سه تا صدا اومد
🔄
سه تای دیگم زد 03:35
مجدد انفجار ۳ تا در بندرعباس
دوباره زد ، شدید داره میزنه
یه صدای خیلی وحشتناک تر الان اومد۳.۳۵ بندرعباس
دوتا دیگه هم الان زد
سلام صدای ۴ انفجار به همراه لرزش از قشم
بندرعباس وحشتناک صدا انفجار میاد مشت سر هم داره میزنه
بندرعباس صدای انفجار 3.35 شدید بود
وحید قشم رو الان ساعت ۳ و ۳۴ دقیقه دو بار زدن
بندرعباس همین الان 3 انفجار جدید3:35
#بندرعباس
28 تیر ساعت 03:35
صدای 3 انفجار سریالی دوباره ،محدوده پایگاه هوایی
وحيد جان قشم هم صدا مياد
٤،٥ بار پشت سر هم
همین الان ساعت ۳:۳۶ چندتا صدای انفجار شدید در قشم
الان ۳تا افنجار دیگه اومد، کل خونه لرزید، خیلی بد بود ۳:۳۶
تسنیم ساعت ۴:۴۵
گزارش ‌خبرنگار تسنیم از بندرعباس:
🔹
براساس اعلام استانداری هرمزگان، تا این لحظه ‌بر‌اساس گزارش‌های دریافتی، هیچ‌گونه اصابت موشک یا پرتابه‌ای در بندرعباس ثبت نشده است.
🔹
در حال حاضر آرامش در منطقه برقرار بوده ‌و با وجود شنیده شدن برخی صداهای نامشخص، طبق آخرین گزارش‌ها تاکنون هیچ موردی از اصابت موشک در بندرعباس تأیید نشده است.
🔄
ساعت ۵:۳۰
صدای انفجار اومد همین الان
4 تا پشت هم
وحید الان ساعت ۵ و ۳۰ دقیقه قشم دو بار صدا انفجار شدید اومد خونه لرزید
بندرعباس الان دوتا صدای انفجار اومد ۵:۳۰
ساعت ۵:۳۱ دوتا صدا انفجار اومد بندرعباس
دو انفجار الان بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77256" target="_blank">📅 03:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77255">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیام‌های دریافتی ۲:۱۷
درود وحید جان همین الان بهبهان اگر اشتباه نکنم سمت پالایشگاه بیدبلند رو زدن ما تو حیاط بودیم  که اون سمت آسمون سرخ شد
سلام بهبهان صدای سه تا انفجار اومد
سلام بهبهان چندین صدا اومد
صدای عبور جنگنده در بهبهان شنیده شد ولی تا این لحظه هیچ  صدای انفجاری من که ساکن شهرم نشنیده‌ام.
خبرگزاری مهر:
برخلاف فضاسازی رسانه‌های ضدانقلاب، تاکنون هیچگونه حمله و بمبارانی‌ در بهبهان صورت نگرفته است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77255" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oJe6fapZkJM_jCsle_MzKz_gY4chfW5bIGGA8zLiLxg3T3lKCf7Rn07N8NKwL1P7iiy39vFyP2sPM6toJ9cjE-Va7l8keoDnYJLz7uDBQJFxh2Gzag_B9izWCtHdwAqRS5yCtZV4fd8SK_e0GyEtMxOJ3F5De3DmvodFIG6t8JEKlWjvqHgE429085tWolfraaK42aYM8NmeoBHEWztZ86z_VVFtP6Vl7Y5n1aMWvMso3IOtVklDpiHfpglQiI2XA0RDAZzLMn77X1IFFm-toRPTTcbTduzr_ngWBdDf1tyQksWWuPE5qqIapl-EKgzwOcfD32hO5fmcmvlAMjo1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۶ عصر به وقت شرق آمریکا [۱:۳۰ بامداد یکشنبه به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور تازه‌ای از حملات هوایی علیه ایران را آغاز کردند.
این حملات با هدف تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی انجام می‌شود که شب گذشته به نظامیان آمریکایی در اردن حمله کردند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/77254" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RVkvFXFgkouJCj1UZ5eixUo-tU5bj-SHZ_qBwQIo0ZQFoqPp82WA7KbuNPziDVdVwjMSrv4b5iwUJTQYpRSxTgo4dsp99ed6cnVW5RKOQHifc6Xtam4yfoKIMgN0l-2cvsfNNQPz7lLHiF08sfeShzNc_Fn_jBBN2UX8sBLEGGPNgRUBMd5r32Z5LfpmAWPu6maU3VpC6fuYjl5FHO-uJFeJVulITohI6HQlKSYbEcwe-7uEu8WdSgedUCLdTOQaVakdBqyN3hFQA86hpoRIIk6hgyGg-05QqdWmscfcUAYp3H8iSDaRS3ifQeWZ-lDpGC5snWfUphMGJ5KhFMWItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IK9TGmwJs52ccxH5JpbQNTJj_HFUwAF9EJsEpfJeeq5m0_r4JrANchzAVnVk7pyq5AzLYXDKKoPCddaZ9Ij3eKA2_mGc0O4JUJyKl8L4BnY-CHFsEPJYNkSp1PzNvA-O9TLMGQ21L6mYoma96Pq_bnMUc3plKSgn9QpkbbMkdXojxoja1-vZuACnPA8uzcXgPx4xigW6Ma_Y843npB6El0zVk0aNOZh5D5xjeWfCX83OxEO-e6-cZojcqOOUQHrh7fD-Efpwid2lZSsdd2nI8pTRhf5jfAccErQfDlHRiGdLlYOsc0O5_bk0s8W9xY0L_R1xuC2up5rHfqSqo6d6nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری ایالات متحده، در واکنش به کشته شدن دو سرباز آمریکایی در اردن به شبکه «نیوزنیشن» گفت: «بسیار غم‌انگیز است، واقعا رویداد بسیار غم‌انگیزی است. ما از دیدن چنین چیزی متنفر هستیم. آنها در راه خدمت به کشورمان جان خود را از دست دادند.»
@
VahidOOnLine
ترامپ در بخش دیگری از این مصاحبه با مواضعی قاطع، بار دیگر تأکید کرد که «ایران نمی‌تواند و نباید سلاح هسته‌ای داشته باشد.»
او همچنین در واکنش به اظهارات مقامات جمهوری اسلامی مبنی بر تعلیق تعهدات تهران در قبال توافق موقت یک ماه پیش، با بی‌اعتنایی کامل اعلام کرد که اهمیتی به این تصمیم ایران نمی‌دهد.
پیش از این، کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه جمهوری اسلامی، شنبه ۲۷ تیر، گفت آمریکا همه تعهدات خود ذیل تفاهمنامه اسلام‌آباد را نقض کرده و ایران نیز اجرای تعهداتش را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77252" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwK-4IQ5m6ISsDDiffKNUzitYeGxifXLBcMuzYXMoyx2-V07QHHKAT3YI11BHEpc6pA5LiycwJcn6omKO8jojk1mLf2SNz_R4v2kKcCIsot_ZPjoErf5-wX6nEp1amr4oG1DUZErHb3dEY1Wvk5olg7k0kiK0VMWUKcKvDSl4WnBTHAnQ9SfcFHJI_qFhV2FRAKxiXwz1vnJjioaHpA-BWHBvkEIp1xnZnp9QaRIwckZ9qphLHVYBXKO2sL9ob4hT4IA8t_9lDx2ndyAcnyDK4-nBXsw9qrIPDRDWa3JSUq5gc-6Dl1eJbuEkx6XeNv1ynlR8-iK3dSLrwJE4194SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز به نقل از چند مقام آمریکایی نوشت حمله جمهوری اسلامی به اردن که جمعه به کشته شدن دو سرباز آمریکایی و مفقود شدن یک سرباز انجامید، چهارمین حمله به نیروهای آمریکایی در این کشور طی پنج روز گذشته بود.
به گفته این مقام‌ها، این حملات در مجموع ده‌ها سرباز آمریکایی را زخمی کرده و به تعدادی بالگرد بلک هاوک آسیب رسانده است.
این مقام‌ها گفتند حملات و خسارات ناشی از آنها نشان می‌دهد نیروهای جمهوری اسلامی همچنان ذخایر موشکی قابل توجهی دارند و در عبور از سامانه‌های دفاع هوایی آمریکا نیز ماهرتر شده‌اند.
نیویورک تایمز نوشت اهمیت اردن برای عملیات آمریکا افزایش یافته است، زیرا پنتاگون پیش و در روزهای نخست جنگ، بخشی از نیروهای خود را از بحرین، امارات متحده عربی و قطر به اردن و اسرائیل منتقل کرد.
به گفته مقام‌های آمریکایی، محدودیت‌های اعمال‌شده از سوی برخی متحدان منطقه‌ای آمریکا برای استقرار نیروها و پرواز هواپیماهای آمریکایی بر فراز خاکشان نیز نقش اردن در عملیات واشینگتن را افزایش داده است.
پنتاگون از اظهارنظر در این‌باره خودداری کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/77251" target="_blank">📅 01:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHRuk-hctF3CQU8GC9QlZSxRPg_S9es-2oVsBCcfNerVRWmGYMqwEtmYVSrnc_zL_IiZHFjt6sYKc2MvQGKE9Ey0_I9Gy7Dagt27eTXDPskbfSR5lN09whmDXahT98etgCUmIQAuIwURLLXpA0DTpt0Km1Ijpf9yacy8LdL9sfGsDvFmFVmsrX3sGJ9-QIq-ayJnv4f9LxjL8HQMY5XvA00Jaat0w4MkbxGI8E8ZWfyXKrMGXC0gZVe33HwJ-_OKF_iqR2hRsIpDbBz0UD_Hc9y0BIBCRxPy7vjgD5gGepkyuqJlp16qzIrvnj2_btU_tQs9boo560yNAM3k-J2_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، بامداد یکشنبه، ۲۸ تیرماه، زمین‌لرزه‌ای به بزرگی ۳.۷ حوالی سرگز در هرمزگان را لرزاند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/77250" target="_blank">📅 00:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چند پیام دریافتی در ساعت ۲۲:۱۳
بندرعباس ۳ انفجار
اقا بندرعباس رو زد
۴ الی ۵ تا
زدن داداااا
بندرعباس
اقا وحید الان بندرعباس زد صدا اومد معلونم نبود کجاس
[ولی فقط همین‌ها بودند و انقدر هم صبر کردم که دیگه پیام‌های دریافتی بعد از انتشار این پست فاقد اعتبار محسوب می‌شن.]
آپدیت:
گزارش خبرنگار تسنیم از بندرعباس:
🔹
از دقایقی پیش اخباری مبنی بر صدای انفجار در بندرعباس منتشر شد، اما مسئولان استانداری هرمزگان ضمن تایید این صداها می‌گویند هنوز گزارشی از اصابت موشک یا حمله جنگنده‌های آمریکایی نداشته‌ایم.
🔹
از سوی دیگر برخی منابع خبری به خبرنگار تسنیم تاکید کردند احتمالا این صداها مربوط به هشدار نیروی دریایی سپاه به کشتی‌های متخلف در تنگه هرمزگان باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 485K · <a href="https://t.me/VahidOnline/77249" target="_blank">📅 22:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/77727bb200.mp4?token=E0Mb_uZCastixuuQixgqan8cjs-uDgoFJeAXrw6Ap4Vqo-BvYWKZLHK_pHdEi_hqfDb1XLhXHI4Mtpl8lX0yNIHlzggQ1rPdSoGs6lZMN7UbIYVGJFSUea92NrVxYBxrIqPIg2ET_rMH18GfBmBHLTp_6JIkGwq3pwigOOwTAroMP6xKwgedhJ0DeRgvR1LD8t29h_982iVXW4avvZNmx8dt6ejd9eUd8BIelL9erBqoR97Mtgin3dPTFfubBnUrLy4hs6Ng7I89V1aOsSdtv-L7DFK-GvDmn8gnZDVyzwqV9J7gkd0mz7P5fvmxZRBpZ9Wh3mdjgE85rKrvpzxWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/77727bb200.mp4?token=E0Mb_uZCastixuuQixgqan8cjs-uDgoFJeAXrw6Ap4Vqo-BvYWKZLHK_pHdEi_hqfDb1XLhXHI4Mtpl8lX0yNIHlzggQ1rPdSoGs6lZMN7UbIYVGJFSUea92NrVxYBxrIqPIg2ET_rMH18GfBmBHLTp_6JIkGwq3pwigOOwTAroMP6xKwgedhJ0DeRgvR1LD8t29h_982iVXW4avvZNmx8dt6ejd9eUd8BIelL9erBqoR97Mtgin3dPTFfubBnUrLy4hs6Ng7I89V1aOsSdtv-L7DFK-GvDmn8gnZDVyzwqV9J7gkd0mz7P5fvmxZRBpZ9Wh3mdjgE85rKrvpzxWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توییت، ترجمه ماشین:
این ویدیو لحظه اصابت چند موشک بالستیک ایرانی با برد متوسط تا میان‌برد به پایگاه هوایی موفق‌السلطی در اردن در طول شب را ثبت کرده است؛ حمله‌ای که دست‌کم دو نظامی آمریکایی را کشت و چند نظامی دیگر را مجروح کرد.
sentdefender
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 475K · <a href="https://t.me/VahidOnline/77248" target="_blank">📅 21:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PdPjglNVUCNcAzWexNAg3Zc89JECnBAuiOnHnFGh_6FuWJYeqK8kYgM_ZTivCpwlCBKEawJHMGfXEgaa8oXm-xupEpstEUftgmkWj_Z_ogShfZHHdOcGRm3KgsA4hzlAfvUTvc2D34eXd7PFj59W9pVbLkItTOACOEhKbJOFk-LZhJxc7SVJt3btQBdcuvUCP9SONswoYYmoZkgoyNi492BIRmyMTW2IuteVV7BU5cIIBwid8UelB0ivOUIXLZ5cweZfdDQlyvRY5YpO8vBHyL0Qcvjz69ATSo-X7c4_QnX5dYzHpSqs_PKZ2a5vPkB2DFNfWd-sxkUcSwRx4eJh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: دو نظامی آمریکایی کشته شدند و یک نفر مفقود است
پست سنتکام، ترجمه ماشین:
بیانیه سنتکام درباره نظامیان آمریکایی جان‌باخته و مفقودشده
تامپا، فلوریدا — در ۱۷ ژوئیه، در حالی که فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای شریک در برابر حملات موشکی بالستیک و پهپادی ایران دفاع می‌کردند، دو نظامی آمریکایی در اردن در جریان عملیات کشته شدند. همچنین، یک نظامی در حال حاضر مفقود است.
چهار نظامی آمریکایی برای دریافت خدمات پزشکی به بیمارستان‌هایی در اردن منتقل شدند. آن‌ها از آن زمان مرخص شده‌اند. سایر نیروهایی که به‌دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به خدمت بازگشته‌اند.
سنتکام از سر احترام به خانواده‌ها، تا ۲۴ ساعت پس از اطلاع‌رسانی به نزدیک‌ترین بستگان، از انتشار اطلاعات بیشتر، از جمله هویت رزمندگان جان‌باخته، خودداری خواهد کرد.
CENTCOM
پیت هگست، وزیر جنگ آمریکا، در واکنش به کشته شدن دو نظامی آمریکایی در حملات جمهوری اسلامی در اردن در شبکه ایکس نوشت: «خدا نگهدارتان، قهرمانان. فداکاری شما فقط عزم ما را راسخ‌تر می‌کند.»
پیش‌تر سنتکام خبر داد دو نظامی آمریکایی روز جمعه ۲۶ تیر در جریان مقابله با حملات موشکی و پهپادی جمهوری اسلامی در اردن کشته شدند و یک نظامی دیگر همچنان مفقود است.
سنتکام افزود چهار نظامی مجروح پس از درمان از بیمارستان مرخص شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77247" target="_blank">📅 21:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/863eecb938.mp4?token=khJkHuEHHYaju5Qp578gpO5IUdirinY-hkcyLQQ-GySkG2nhyyRq9tvMXpGqRvAB744WH0YyiaLPmPlm0PrPMnoLKWTw-B07nULqcoyUIYLs3uN4Sor7PtUDXq_mzgFPaE0vCfLjaDepOdMzHHh6pqlPWAInD6jWYqYc6pl2avcrmgA7pdQuts7oWii30Kwxl60BP_iQ2KPd9mJZCl2bdTG8VsxkMufxcYuDlGRpq2bv5rpnpUQ7gnfJcb08mswHesdAJQY2I3AZJ7YSWO8Nlttpk04T5waEHVOiSRm5eSZPe7cP54fL7Mx6eLfFCT4CVLRjEc50m8YAqy9BH0A2xqQRF2Ss4CmMWHXt4rEKMnSObsdNXaNussm8G_3hfQvoYIabnQlRI5LCESVsrmJD7a64csu8vAqI3Zgh-uQ1YL7yduEgYhcV5QOSo0LcSqs8cAvHCC1Yjl6wsqrd43Tly1GxqMm0TrQeq-VttQNojC9-vaYZed9AzUS4tP42Ew0bZ7BOpg9LtTghOG4RiBJeB2rph9vJCVMwveskMOetqF52j7wQPoBT3FMD-60XF3r7QyvtepQ-eMo_PCQspAx6IsVLMzHo4FrZo0gUWY_lBq6sT3SMt618vgD8QNU35476V3NFserBpj36YetGFmjwDa-9JccXr7uD-hDBsA3yai4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/863eecb938.mp4?token=khJkHuEHHYaju5Qp578gpO5IUdirinY-hkcyLQQ-GySkG2nhyyRq9tvMXpGqRvAB744WH0YyiaLPmPlm0PrPMnoLKWTw-B07nULqcoyUIYLs3uN4Sor7PtUDXq_mzgFPaE0vCfLjaDepOdMzHHh6pqlPWAInD6jWYqYc6pl2avcrmgA7pdQuts7oWii30Kwxl60BP_iQ2KPd9mJZCl2bdTG8VsxkMufxcYuDlGRpq2bv5rpnpUQ7gnfJcb08mswHesdAJQY2I3AZJ7YSWO8Nlttpk04T5waEHVOiSRm5eSZPe7cP54fL7Mx6eLfFCT4CVLRjEc50m8YAqy9BH0A2xqQRF2Ss4CmMWHXt4rEKMnSObsdNXaNussm8G_3hfQvoYIabnQlRI5LCESVsrmJD7a64csu8vAqI3Zgh-uQ1YL7yduEgYhcV5QOSo0LcSqs8cAvHCC1Yjl6wsqrd43Tly1GxqMm0TrQeq-VttQNojC9-vaYZed9AzUS4tP42Ew0bZ7BOpg9LtTghOG4RiBJeB2rph9vJCVMwveskMOetqF52j7wQPoBT3FMD-60XF3r7QyvtepQ-eMo_PCQspAx6IsVLMzHo4FrZo0gUWY_lBq6sT3SMt618vgD8QNU35476V3NFserBpj36YetGFmjwDa-9JccXr7uD-hDBsA3yai4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پیامی منتسب به مجتبی خامنه‌ای، سومین رهبر اعلام شده جمهوری اسلامی، او با اشاره به نقض تفاهم‌نامه میان ایران و آمریکا تاکید کرد که این اقدام بار دیگر «بی‌ارزشی و نامعتبر بودن امضای رئیس‌جمهور آمریکا» را نشان داده است.
مجتبی خامنه‌ای همچنین، آمریکا را به «جنگ‌افروزی» متهم کرد و نوشت: «اکنون که دشمن امریکایی به دنبال جنگ‌افروزی و تحمل هزینه‌های سنگین‌تر و بی‌آبروئی بیشتر است، بداند که ملت عزیز ایران و جبهه مقاومت، درس‌های فراموش‌نشدنی برای او دارد.»
@
VahidOOnLine
متن پیام بنا بر فایل PDF منتشرشده در منابع حکومتی:
پیام رهبر معظم انقلاب درباره‌ی حماسه عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور
بسم الله الرحمن الرحیم
ملت عظیم‌الشأن و شگفتی‌ساز ایران!
سلام و درود و سپاس بر شما که با حماسه‌ی بی‌نظیر و تاریخی خود در رستاخیز بی‌سابقه‌ی بدرقه‌ی آقای شهید ایران، نصاب تازه‌ای از جلوه‌ی بعثت و اراده‌ی مستحکم هویت اسلامی ـ ایرانی را در قدرشناسی، وفاداری، بصیرت، و ابراز محبت فوق‌العاده به زعیم امت اسلامی و رهبر شهید انقلاب ثابت کردید.
گرمای دل‌های گداخته، چشمان اشکبار و عزم‌های استوار جمعیت ده‌ها میلیونی و ده‌ها کیلومتری در تهران، قم، مشهد، و سایر شهرها و روستاها، دوستان ملت ایران و مردم آزاده‌ی جهان را به تحسین و دشمنان مستکبر ملت ایران را به حیرت و سرگردانی و خشم و وحشت انداخت.
همزمان با این حماسه، نقض عهدهای مکرر شیطان بزرگ نسبت به تفاهم‌نامه امضاشده بین رئیس‌جمهوران ایران و امریکا بار دیگر این حقیقت را به همگان ثابت کرد که امضای رئیس‌جمهور امریکا چقدر بی‌ارزش و نامعتبر است و زورگویی، تمامیت‌خواهی و وحشی‌گری، اجزاء لاینفک مرام و مسلک امریکایی می‌باشد. امروز شیطان بزرگ بار دیگر چهره‌ی واقعی و بدون نقاب خود را آشکار کرده تا این تجربه‌ی تاریک از جنایت و بدعهدی، سند محکم دیگری بر دروغگویی، غیرمنطقی و غیرقابل‌اعتماد و پلید بودن امریکا باشد.
اکنون که دشمن امریکایی به دنبال جنگ‌افروزی و تحمل هزینه‌های سنگین‌تر و بی‌آبرویی بیشتر است، بداند که ملت عزیز ایران و جبهه‌ی مقاومت، درس‌های فراموش‌نشدنی برای او دارد که رشادت‌های رزمندگان اسلام و غیرت مردمان شجاع خطه‌ی جنوب در این روزها نمونه‌هایی از آن را نشان داده است.
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدس در همه‌ی سطوح مردم و مسئولان و در تمام عرصه‌ها برای تحقق آرمان‌های بلند انقلاب اسلامی و تأمین عزت و استقلال ایران عزیز خصوصاً در برابر دشمن جنایتکار و حیله‌گر امریکایی است. همان‌گونه که پیش از این مکرراً و مؤکداً تذکر داده شد، صیانت از وحدت و پرهیز از تفرقه و تنازع، اختلافات سیاسی و برجسته کردن تفاوت‌های اجتماعی وظیفه‌ی همگانی است و البته نقش مسئولان و عناصر دلسوز و دلباخته‌ی انقلاب و امام و رهبر شهید در انسجام و یکپارچگی کشور، مهم‌تر و حساس‌تر است.
بر این اساس ملت عزیز، با تداوم بر اعتماد به مسئولان دلسوز در هر سه قوه که تلاش ایشان برای رفاه و سعادت ملت، مشهود می‌باشد، همچنان برای تضمین صیانت از منافع ایران اسلامی، هوشیار و فعال در میدان خواهد بود. ممکن است کسانی با اخلاص تمام و از سر خیرخواهی، انتقاداتی نسبت به عملکرد بعضی از مسئولین داشته باشند. به نظر بنده، در عین اینکه این اهتمام و نگرانی ایشان برای نظام همچون اشخاص خودشان، سرمایه‌ی ارزشمندی به شمار می‌آید و فی‌نفسه امری مطلوب قلمداد می‌شود، این عزیزان که بعضی از ایشان از زمره‌ی پیشروان بصیرت هستند باید مراقب باشند تا این رویکرد، اولاً ظلمی را بر بی‌گناهی روا ندارد که آن خود منشأ محرومیت از برکات و عنایات می‌گردد. و ثانیاً موجب شکست در وحدت و انسجام اجتماعی نگردد؛ که با حفظ این جهات، انتقادها موجب رونق و شکوفایی امور خواهد شد.
دشمن نباید هیچ علامت ضعفی و از جمله این ضعف را از ما دریافت کند؛ که هرگاه ما این مراقبت‌ها را به طور کامل مراعات نماییم، او به ناچار رو به هزیمت خواهد گزارد.
بار دیگر از یکایک مردم عزیز که خود، صاحب عزای پدر شهید امت هستند و با وجود دشواری‌ها و برخی محدودیت‌ها و ناملایمات در رویداد عظیم بدرقه‌ی آقای شهید ایران، حماسه‌ای تاریخی خلق کردند صمیمانه قدردانی می‌کنم.
همچنین از مراجع معزز تقلید، علما، اندیشمندان و نخبگان، فعالان فرهنگی، اجتماعی و سیاسی و از اقدامات و تلاش‌های نهادهای کشوری و لشکری و نیز حضور مقامات و نمایندگان جبهه‌ی سرافراز مقاومت و نهضت‌های پرافتخار اسلامی تشکر می‌کنم. امید است همه‌ی کسانی که در این حماسه‌ی تاریخی به هر نحوی حضور و همراهی و همدلی داشته‌اند، مشمول عنایت و دعای خاص سرورمان عجل الله تعالی فرجه الشریف باشند.
سیدمجتبی حسینی خامنه‌ای
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77246" target="_blank">📅 20:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrvsXOCOt4t6kqifUnRBg-WINX3HnR6yadV4D7kUSS_h1S8LEoRFJdDaqvPG2x7yG7rF0gEmdpBBwM6FPaK6HfbpPkMgJ6Q5Ztq02lJDLa39Wjs2uB9GyvihnnL7ep3I2FApVrauemB_HbuuNmoBKOIiEXeHjK27sCValXOLOUqzJln-AqAYWx_fjImCAq40IaPS255fJk9OFRBdYCOWxHV7zbRDAJUCWSM2nDiUK7pl9pbZhwrjb4N0BokIusaIA_YLluvG8ndmEOXsX1_ce0qCpsvSx092iasBWPBz4p4eR4EdzcGOeCjtzhlfD3piUcZI8YJRWjvbLeFVrMKkig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران به نقل از استانداری هرمزگان خبر دادند طی ظهر تا عصر روز شنبه چند حمله موشکی به حوالی شهر سیریک در نزدیکی تنگه هرمز انجام شده است.
استانداری هرمزگان اعلام کرد: «در ساعت ۱۲:۳۰ و ۱۶:۳۰ و ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت.»
در این بیانیه آمده که «هیچ مصدوم غیرنظامی» بر اثر این حملات گزارش نشده است.
سنتکام، ستاد فرماندهی ارتش آمریکا در خاورمیانه، درباره چنین حملاتی به ایران گزارشی اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77245" target="_blank">📅 19:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oDzExpchaeaAx45v01cK1pTX-GHt77rbdMjzSdg25ppbNP3s89Fx9zjW3aMXMuI3ohLsZQRLouKVLAPNLrx0roh41zu0UmbkxK_lBBQ50AsbdK-27fHi-6eRRfpby4IeKdnTHDyNloOV1_ayQFO-nj7diOGracGoocjz8FaQRK-MqiYkKNpbPWo6LhYpVscr-m2zJs552nMpEYBRccJ7ZbnCnTBg9MBrCKLJUhW4BibiiiTy-KZalApTebMLWI4GJ9dfL_CjJyB4qF29EbIPoETvHcT-uvVE5q8GbgJXmOfJhOl4OL-6W8im-hTIyD9dbEedsYbrORtsZiDPV_xj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FV_-JFEgNahNUZIrdvMCXKdI4Etc2f9TpYjaoUtecJqp5Q2iYTCnkqNX6Ch_yLPVecKnod13A7kfjMI9vD7sCy0MSja1oJOxo4dpgfQTUlvqysRvA_ciaAMcw2Syj6Zb4URVdoNFQIQjmdH3MX4WidHN51ghcSDmQOimT-0WnSlnj92TWC67B1wWbT61VYHbWK1Bp2aSZcyUXRgcrR7UMcps2xNG1_Kvf4skKCxnGFJ-7K-5MRayMMz3x-kgsWWWgD_zowUf3fZFt5IM_u7eKwtnN_mSzTg_89iWlzQgBczuuWUH8zC_eOIdom5UfqlWqNVH8Pl43TAjGqy2A0QzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cgvUcBIYyJtNPIuPSM025BT446ndlvQI5pkyzhxvItEGtBha6U9_A9wDKvfKlBKUPDMMAywD9Ug2maAfTxOeNLsjNTfoxdtNUY835O_rzIhWPt5lNhT-asbdEluVGZn4q9kncBAbwcmhVu_5PFmMCFo91QbBDMJ4eML6fcctnSlgsI9K-OneGdxQhsqNMDZajw9PdjsQBBihppT1YlCj_UW64k0rjXRmZBtIBxCoMEuKrLQSvu0DgjQo_zK3sejf7ZpmsBXk-bul_-G0GQmczSnGxfJ_fGy-XIFVL5lZCKhD9jBVyiD4Ex-elyO3WSqGrUwXk6nhtGc5__OI73JSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZYW_DxE7UKZYSd57OxFwBWkQxUN0JZrew-jsYyV0q-AkK3h-dXukFijkPYTNz25VwGCLjZl-uJjYAu4ACTb7L_7dBkNT3qnr1Tk95YoWQAl0YkF2-dMilA7aQ5wjURt7rY4xASuoT4KZfEAfDh11LCF2hBVxx8-l0rnT4xDAcSfROqL_NsItWspUxtRgJueJoN3BUrGvPnUO1QyYYFg07q8kjN90dNKLdgQSb1xeFqEpWdKQgMjzaTlvFGtI_lq0R1wOHS6tcCik3NWUi2pO7A8OgByDvHSxyZiG_nUjhhQXDv9g1OC-7FAljukWSQocfBRGm97M5nVZDPfNFVQteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KISJL_JBPRfJrA3R_vuqjLGnOuqbZrbEJc4gTfC4AzFQ_uQnoPrrb8f_RCo3XwRPvM4_px3nQMqq22MdRiAd6-1mfUMSNRmOcqyx6ezIf6QBwb3te8f88snn_rlK-92gOnXTLMVeTePqxblULaiPZ4Fxoi11dDztY0os2woEH73c-UuUb99p8quDBT-JgLPgW4RySgFxbWUSSp41WZxQhvc2_E7Dj3tAjAOQN4hTeF8nJ5eif81b21AEGXF5QEmCODWoQAXIaj46ROzIIx2ktxHr1xMGLEw1U1AfLXT8L0zyxUnZkbSvHGuAMbxZN6ayyXqm_DZ-KGcfhRWJRr4T4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jVPz_wolpqTcgpjFRCvHuRg7N0hXyuMt6uNWevjvisqLgGx5z-jSuZANkwUNS56QDYJN4QHJz8Shr_bVx50UQhcMJj0cJGteD9Elf07p5JdUc--cX4fMVSmb6BTskW9F04SIYIUwWJh5Gg9yqJEP8YYkKWHsAHhIbr5t21MwTgHnZ_x9xp8KUTm8T5_INiOvlmH8tjZdRXFYWYlgM4w25Gr_OigHWL72Xzc3lwKgozR-t20ev9lCmC0vYuKhTtDmivHD6es7U8xsREaBRc1VumI7DV7C5c96S3FDL_cZw8pRhJw8gdqJaYCaD-2Lf-NmjDmHQT_Wm_5XDcQ686jkjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارتش جمهوری اسلامی ایران اعلام کرد در ادامه عملیات موسوم به «صاعقه»، پایگاه‌ها و تاسیسات نظامی مرتبط با آمریکا در بحرین، کویت و اردن را با پهپادهای انتحاری هدف قرار داده است.
روابط عمومی ارتش در بیانیه‌ای مدعی شد در مرحله پانزدهم عملیات «صاعقه»، پهپادهای انتحاری «آشیانه هواپیماها، محل استقرار جنگنده‌ها و مخازن سوخت» در پایگاه شیخ عیسی بحرین را هدف قرار داده‌اند. این بیانیه همچنین از حمله به چند پل ارتباطی در بحرین خبر داده است.
ارتش جمهوری اسلامی ایران پیش‌تر نیز در بیانیه‌ای درباره مرحله چهاردهم این عملیات اعلام کرده بود که «چند پایگاه و تاسیسات نظامی آمریکا در کویت و اردن» هدف حملات پهپادی قرار گرفته‌اند.
بر اساس این ادعا، انبار مهمات نیروهای آمریکایی در اردوگاه العدیری، ساختمان‌های ستادی و انبارهای مهمات پایگاه علی‌السالم در کویت و همچنین مخازن سوخت پایگاه الازرق در اردن هدف قرار گرفته‌اند.
ارتش کویت حمله به چند مرکز نظامی و تاسیسات حیاتی این کشور را تایید کرده است.
ارتش اردن اعلام کرد سامانه‌های پدافند هوایی این کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده بودند، رهگیری و منهدم کرده‌اند. به [ادعای] مقام‌های اردنی، این حملات هیچ تلفات جانی یا خسارت مادی به دنبال نداشته است.
@
VahidHeadline
روابط عمومی سپاه پاسداران انقلاب اسلامی، روز شنبه ۲۶ تیر ماه، با صدور بیانیه‌ای اعلام کرد «اسکله پشتیبانی سوخت ناوگان آمریکا در بندر الاحمدی کویت» را هدف حملات پهپادی و موشکی قرار داده است.
بر اساس این بیانیه، در این عملیات «محل تجمع پرنده‌های جنگی» آمریکا در پایگاه شیخ عیسی و «مرکز داده‌های اطلاعاتی در بحرین با عنوان باتلکو» نیز مورد اصابت قرار گرفته‌اند.
در بخش دیگری از این اطلاعیه آمده است در جریان این حملات، «یک مرکز سیگنالی و مخابراتی آمریکا در کویت» نیز منهدم شده است. سپاه پاسداران در این گزارش بر «کنترل قدرتمندانه تنگه هرمز» تاکید کرد.
پیش از این، نیروی زمینی سپاه پاسداران در بیانیه‌ای ادعا کرده بود، مرکز پشتیبانی نیروهای زمینی آمریکا در منطقه عریفجان کویت را هدف قرار داده و این حمله منجر به کشته شدن چند نظامی در این مرکز شده است.
@
VahidOOnLine
وزارت برق، آب و انرژی‌های تجدیدپذیر کویت، روز شنبه ۲۷ تیرماه، اعلام کرد پس از حمله نیروهای مسلح جمهوری اسلامی به یک نیروگاه تولید برق و آب‌شیرین‌کن در این کشور، آتش‌سوزی در این تاسیسات رخ داده و چند واحد تولید برق در پی این حادثه از مدار خارج شده‌اند.
وزارت برق کویت روز جمعه نیز از خسارت و از کارافتادن یکی دیگر از تاسیسات تولید برق و آب این کشور در اثر حملات جمهوری اسلامی خبر داده بود.
@
VahidOOnLine
ارتش کویت در بیاینیه‌ای اعلام کرد از ساعات اولیه روز شنبه ۲۷ تیرماه، موشک‌های بالستیک و پهپادهای «متخاصم» را در حریم هوایی این کشور شناسایی کرده و آنها را رهگیری و منهدم کرده است.
سرلشکر سعود عبدالعزیز العطوان، سخنگوی وزارت دفاع کویت، در بیانیه‌ای که نیم‌روز شنبه در ایکس منتشر شد اعلام کرد «تجاوز» جمهوری اسلامی همچنان ادامه دارد و شماری از تاسیسات نظامی و امنیتی، همچنین زیرساخت‌های حیاتی و غیرنظامی این کشور را هدف قرار داده است.
به گفته این مقام کویتی، این حملات تاسیسات مربوط به بخش‌های نفت، برق و آب را هدف قرار داده و موجب آتش‌سوزی و وارد آمدن خسارت‌های گسترده به شماری از زیرساخت‌ها شده است.
ارتش کویت افزود نهادهای مسئول عملیات اطفای حریق و تعمیرات را آغاز کرده‌اند و در جریان این عملیات، شماری از نیروهای آتش‌نشانی و کارکنان بخش نفت هنگام انجام وظیفه مجروح شده‌اند و تحت درمان قرار دارند.
در این بیانیه همچنین آمده است رهگیری موشک‌ها و پهپادها باعث سقوط بقایای آنها در چند نقطه و مناطق مسکونی شده و خساراتی به اموال وارد کرده است، اما هیچ تلفات انسانی در این مناطق گزارش نشده است.
ارتش کویت در پایان تاکید کرد نیروهای مسلح این کشور با آمادگی کامل به انجام ماموریت‌های خود ادامه می‌دهند و تمامی اقدامات لازم را برای حفاظت از حاکمیت، امنیت و ثبات کشور در دستور کار دارند.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک مقام امنیتی جمهوری اسلامی نوشت اگر آمریکا به زیرساخت‌های غیرنظامی ایران حمله کند، فرودگاه‌های دبی و ابوظبی و بنادر فجیره و جبل‌علی باید فورا تخلیه شوند.
این مقام امنیتی گفت این هشدار با هدف حفظ جان شهروندان در برابر حملات متقابل جمهوری اسلامی، صادر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77239" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ppLKYwnBcV4p4clvzyCvyXRweK4IjVjyf3SAikd6EgCKstdywFRwCYORuHB48Qds7ao_gbaLZ0-dCK4C8Ak2Dp_HybnU_ohzzPNGAwPskAzBzdawGUGq70clBBRvz7sI2FE1fcFBcOV4GCA2eUUPur8YGzat86wZofwg2ydUQB4Fheow2wq90DzyTtf9SywlE1LwWVCYarEnFENZmFJYr6hsnelqGZBPVzc1BO9AB2lt4caKhRq20Mk-tPi4Hcvd0m0SiNbOsArh96Oei_x9iQA51Z-ewG3crjuP4W94iCqinlkofrdKSRwKiQMVm6Lra-a95N5JTRr8ILcnMPI1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NCQM_IwwTrYYyO0xuBzgMUecRhKDFuIQG4Y1esT_PkUDAy7weGH-zd15nmJaU-C07hYQVqGFdTlpsfxiICEDwKCoHPiH8XkCkcTrVsc07CkmJx4UOQUTNyaQ_-C6VtJquBOoZgrIPNPOesY4ewtLyyJ-wTJZdaPVSaXCA6Qh8PN09k43MNC7q6QTTnIMJRq3YhSOKEiiwrjf3FLfg3nEaY0FRay_D7IrlmXrrYEtz4C3HV2ZqvbRBxGj6Hvpk3UIoCD9QJA1JoE_b90Qs_KPKQFVpuGAeC4IRn6OfW4fGnINX9QWupQ56km1-fV1qeQC8cIrsEfiG05fvOTE0Xdz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KTEEgPvrQi4Ec0yqx8L32nY6nR30VX25KKOON1un4OmbRuWVx-tqbFXT2qClj3TuvpCIOpE3J4r4vTYli4U1f-GVmwaMjTeYiy-oGYgmb4CTF5FtKQVHiqr0Oiy35QZYchgS3azLShqkER3DTZofqnndvVdnLcbqNOgtbTQ6FtT4T2zdXB_tWk9ICjCvHAbngBEokZGAGGpSs9xPhlTrOUsYr5eGn4CIKhws1Dx4Wv3JXcSf40CQ9Lgi-OkHPn6noa9B7L-eowySBBPejUl55ItMDTRl7n196oxhil4j9qbZmCeYetl8Prws5lIjKj_LPufRFGwA8sxX9U7Xn3ZiYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sW17EBh2j_gbiVZ-5IRDpS58rQTMTEoVB_feCsqe1UkQvYPkXCI9isTPjSTZC1Y7BxV5qxZmEujo0AeUEvYAxx0-Vp7OryjLYACv93m4vaDyeqP-b4qvUHFPDDgrD1AFRVlTMz5AtcKKVxPtK2-zQiMWybFODb6EKfbxMXqqQtDrCdzBKeU3haZXwiUbz58Hil1yRb_0wIVGcM88JEgAkGl_v0BLC_N-qbpWa0PB8DE_LnSI_c-K6ftpNHuf0-Y4ky4HSittoAyji9PF-Vp2IohRhgFfr7LjO4y02A_4jD-OSntDVNRcoxHM7psvvGyptXTth9HnU69TnOHOMELGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H0IZwDaY2yCJHyLRK0FhmKTOXo0LGRQ2jkMelTiZ1vl7qau6RoAo9rp66QDllNwIaRjv_pU8wVJUKK4swZYrd7R3DFVZcmdj3MaQ8SEQsQtovdsBjBEuu1Rnf2h5LW0T4RgusDZ10tfRJvJ502MvNhwHTIMzlJtRFK_FpVSvXNgCsocZYidnzOCUVb98QLFLd0Aobwb7Z6h1JJsty4MWr4ESDrzK6GvgkrG_V1dgUT-UVADfJA_q9tpgt-r4Y2l7JcIiHWnicpasuggVuyRHN3ctxc71MH4GtfFGopRdfPrFqUtB6CS8wm9IEBTMD6SNWY72uM8Qh_DCNAIB96KmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GFT77HSVxU-MQwJQDUmF8zf-2W5pjBg2OkPeV7Pu_GfVTSxH0VKcoTj0aICPqjZzcv_dJ602MS9H9t-holmSMVmUEvAHd1IlpGFRGMHP7wYQmSk5gZv9JTQgqKFXcsbWwYGcYKS1VXPWqJb3VFre9DDIoG6CwsmDp7YTiyIe5kfhFYtIIZU4_bwCOIQhASOOrU_HtC7e_WkgudAGfL1liNK_BdwAr7sjf4rqvCg_0El_LfxU9YOopuEBUatuQTpkZo9o8PrXUbU2ByvHkvgnx1xhImEE0N4MENqBlK7ttIWSk1ZXoQwEBibkbAOje1O0F3_1AMGpnbNCJmtvzI5FYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌زمان با پایان هفتمین شب حملات آمریکا به ایران، مقام‌های جمهوری اسلامی از وارد شدن خسارت به بخشی از زیرساخت‌های حمل‌ونقل، آب و برق استان هرمزگان خبر دادند؛ حملاتی که به گفته مقام‌های محلی، باعث انسداد موقت برخی مسیرهای ارتباطی و اختلال در خدمات‌رسانی شده است.
احمد کرمی‌اسد، رئیس پلیس راهور فراجا، اعلام کرد در پی حملات بامداد شنبه ۲۷ تیر و همچنین حملات چند روز گذشته، بخشی از مسیرهای خروجی استان هرمزگان به سمت استان‌های فارس و کرمان به‌طور موقت مسدود شده است.
به گفته او، پلیس راه و سازمان راهداری در حال تلاش برای بازگشایی دست‌کم یک مسیر عبوری هستند. کرمی‌اسد افزود در حال حاضر تنها یک مسیر فرعی برای تردد خودروهای سواری از بندرعباس به سمت فارس و کرمان فعال است، اما تردد ناوگان سنگین تا اطلاع ثانوی امکان‌پذیر نیست و بازگشایی کامل مسیرها به پایان عملیات ایمن‌سازی و ترمیم زیرساخت‌های آسیب‌دیده بستگی دارد.
استانداری هرمزگان نیز اعلام کرد حملات شب گذشته به چهار نقطه از محورهای ارتباطی این استان خسارت وارد کرده است. بر اساس این اطلاعیه، تونل شهید میرزایی در مسیر رفت و برگشت، پل رودخانه شور در محور بندرعباس–سیرجان و دو پل در محور سه‌راه میناب به سمت رودان هدف حمله قرار گرفته‌اند. استانداری از شهروندان خواسته است تا اطلاع ثانوی از تردد در این مسیر‌ها خودداری کنند.
هم‌زمان، معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از اصابت چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در شهرستان جاسک خبر داد و گفت در پی این حمله، آب چندین روستا قطع شده است. تاکنون گزارشی رسمی درباره میزان خسارت یا تلفات احتمالی این حمله منتشر نشده است.
خبرگزاری تسنیم، نزدیک به سپاه پاسداران، نیز از آسیب دیدن دو پل در محور بندرعباس–رودان و همچنین هدف قرار گرفتن دکل مراقبت دریایی جزیره لارک خبر داده و نوشته است که در این حملات چند نفر کشته یا زخمی شده‌اند، هرچند آمار دقیقی از تلفات ارائه نکرده است.
@
VahidHeadline
مدیرکل ارتباطات هرمزگان اعلام کرد در پی حملات دیشب آمریکا «۱۱۶ دکل مخابراتی» در این استان از مدار خارج شده و ارتباطات مخابراتی در بخش‌هایی از شمال بندرعباس و شهرستان حاجی‌آباد دچار اختلال شده است.
احد قویدل روز شنبه ۲۷ تیر با اعلام این خبر افزود در حال حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که علت آن آسیب واردشده به مسیرهای انتقال ارتباطات در محدوده تونل میرزایی است.
بر اساس این گزارش، «مسیر انتقال دیتا که با کمک فیبر نوری از بندرعباس به سمت حاجی‌آباد می‌رود، شب گذشته زمانی که به تونل میرزایی و پل رودخانه شور حمله شد، دچار مشکل شد».
@
VahidHeadline
سخنگوی وزارت بهداشت جمهوری اسلامی اعلام کرد در حملات هوایی آمریکا از ششم تا ۲۷ تیر، دست‌کم ۵۰ نفر کشته و بیش از ۵۰۰ نفر مجروح شده‌اند.
حسین کرمانپور، سخنگوی وزارت بهداشت گفت پنج زن و دو کودک و نوجوان زیر ۱۸ سال در میان جان‌باختگان این حملات قرار دارند.
به گفته او، ۳۲ زن و ۱۸ نوجوان نیز در جریان حملات مجروح شده‌اند.
سخنگوی وزارت بهداشت افزود ۳۷ نفر از مجروحان همچنان در بیمارستان‌ها بستری هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77232" target="_blank">📅 19:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77231">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lx0CSpboON55JrCCHEvMkVX3-Z88MQC-uzHi9SnHaWo5N5tczvHgbJrQvKhLu7lHY6qWQEJNwYLKP7wgcM_euKbLFnCl2d1AhHAzadf9oCy4LNriJKX45uRnxoq-x3GK_fOXbG2sbgHU_yGpwaYQl2cxxMlRmqyk0cPpXzSng8nJCayEaMaGFslV1nQrSqKTMDRKHsklPeiTPQOJUr8NAxZsd2HlGY2mUfAaEZO-2JfUIzciLltHA0w8bxjSpl6tgX3_g5zBUYOwwpXewqxT8IwyRLhB2x9KQ5cRUkq_nGLmOOaxmgwt1WsI-mbny-xoz0NgcY5hXolU2MxTA_VEHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت آموزش و پرورش اعلام کرد آزمون‌های نهایی پایه‌های یازدهم و دوازدهم در روزهای یکشنبه و دوشنبه، ۲۸ و ۲۹ تیر، در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان برگزار نخواهد شد.
این وزارتخانه روز شنبه ۲۷ تیر دلیل این تصمیم را «استمرار شرایط ناپایدار در جنوب کشور» عنوان کرد و گفت زمان جدید برگزاری این آزمون‌ها متعاقباً اعلام خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77231" target="_blank">📅 19:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EkshC_16kc7rmg_Mk8NkzQJTXqjcjBvM6X1ANsFGZoSd9UbdZUcCUrGTyHhQOkBfGpnynTcUqRSL4rVwd9_UvB_FJH7jpqU8NgQDHmrh3olKDSYOMaWurXmhX6RlVdWC-CpOXBNfnu3xVUnog0i8HQn82_q8PLJsPD52sYhBwE9qhxVKEaoggNqb_Pa672XAhdS_q7Za86IE1TM8swF0RkOW6Uuyv6smS2BB6gbgQkifUF18Mmj3z8i0_NG9iJbQNDNzardncFHZHorBDtifA2fbf4vxDrSvwwRxqS1UOJNhrYZHWKQQocgxDr2KojxDj5JymxuXvkkJFxxjPqEmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: پرتاب چند موشک از استان بوشهر
شنبه ۲۷ تیر حدود ساعت ۶:۳۵
Vahid
آپدیت: ساعتی بعد هم کلی پیام و تصویر از امیدیه اومده بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 486K · <a href="https://t.me/VahidOnline/77230" target="_blank">📅 06:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f9ac6ccc3.mp4?token=X_QtSEtrumRSkCNlzS0jFNgvxBt4v3no0diOfn3kPPC2QH4-EKupm3oOQjinKMAmj8nvHj2Y54SVqCooncxw81Um82NR0bnmEA2WywZSTFLy_517MITHuv7WQoHPtapHQA1MjSt9x5CqEFNe_gHIlKsPIvmmCukEItDSv38-UAgVBEvHjKSxE5b_JTSnHYzjJoSI8RSQHY8nlQwOwdZcxHEnseTlFo1t5oGND5g49zZgzsaNedG9svZt-CqlnEm0c4cpXz20ixu5E7B3576k6naYXuphG6_Cp4-PAketfsOv2zhx47pAxFiap6-VCQLSWf0xCFvMh2J9byWIBiRUtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f9ac6ccc3.mp4?token=X_QtSEtrumRSkCNlzS0jFNgvxBt4v3no0diOfn3kPPC2QH4-EKupm3oOQjinKMAmj8nvHj2Y54SVqCooncxw81Um82NR0bnmEA2WywZSTFLy_517MITHuv7WQoHPtapHQA1MjSt9x5CqEFNe_gHIlKsPIvmmCukEItDSv38-UAgVBEvHjKSxE5b_JTSnHYzjJoSI8RSQHY8nlQwOwdZcxHEnseTlFo1t5oGND5g49zZgzsaNedG9svZt-CqlnEm0c4cpXz20ixu5E7B3576k6naYXuphG6_Cp4-PAketfsOv2zhx47pAxFiap6-VCQLSWf0xCFvMh2J9byWIBiRUtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم با انتشار ویدیویی از محل حادثه گزارش داده است که دو پل در محور بندرعباس–رودان هدف حمله آمریکا قرار گرفته و این مسیر آسیب دیده است.
این خبرگزاری می‌گوید که در این حمله شماری کشته و تعدادی نیز زخمی شده‌اند، اما آمار دقیق تلفات و میزان خسارت هنوز اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 481K · <a href="https://t.me/VahidOnline/77229" target="_blank">📅 06:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77228">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/de9YXHH_5oWfNzIrtXGKytDcJIxv1zRagn-CfZO0Qw8hOGjBlf1KIp-KyshpmP0NcEtNDXDXqXe_1STiJ0l2Ki3bJ0M40YxzoCyjXRJ_0_onzc-NrXXQd5VgS-WnoC6y7qcEAcMgCzJT8Txzala9dv9cWxpDoR-UICmd6SaYivpDePI55Qm6NhT_uOeHmsZEoM0srYeOplFkj4YZgTnmTh_TUDnqM_7hHrQq4RhJDQr7vbBK-L6ge84tMrhPFKDDUlb3ud2P3ACY4hReyUq9dwGuJ7t2-RnFDPBumQ0K7Ylsle6_ACrt1Hj-LXvKdJGPOdw4U-wldZ-TbN1Guh2Sag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت: نقشه «راه‌های مسدودشده» در نزدیکی تنگه هرمز
شامل دو پل و خروجی تونلی که در حملات هوایی امشب آمریکا هدف قرار گرفتند.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 469K · <a href="https://t.me/VahidOnline/77228" target="_blank">📅 06:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77227">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c159c5a2e1.mp4?token=epWzV6DuQM4N73uRmBFVRmdCpeCZaN5lZkkE2qWswMzgHNCsStF_kSNCIjBWahdAPpCTtIBVdJelv7HcbeYcc1XmhWsuoTX1uEYO7St-pMGvkZo41zRcfPzoN4A3i7inV6brfNiz_bxwRMGT1UuYpLKV5ZmDE0QpSkNdAQCpai5dnk7FFO1pDB1l360gDWg3Tz9igj0G5VTF-7Fl_rTwCIWee3Ev-zdvBu1bYgzPdPkm_N6t9vsW-rHFDQpt8E02R-KXl4XC885Sc7UfLkEsQpp7GpfiVojnYG4YVyOOwOR7AJ59QuXYm70HTX24qXcdqFci07eQRBYuSBVnX6I2Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c159c5a2e1.mp4?token=epWzV6DuQM4N73uRmBFVRmdCpeCZaN5lZkkE2qWswMzgHNCsStF_kSNCIjBWahdAPpCTtIBVdJelv7HcbeYcc1XmhWsuoTX1uEYO7St-pMGvkZo41zRcfPzoN4A3i7inV6brfNiz_bxwRMGT1UuYpLKV5ZmDE0QpSkNdAQCpai5dnk7FFO1pDB1l360gDWg3Tz9igj0G5VTF-7Fl_rTwCIWee3Ev-zdvBu1bYgzPdPkm_N6t9vsW-rHFDQpt8E02R-KXl4XC885Sc7UfLkEsQpp7GpfiVojnYG4YVyOOwOR7AJ59QuXYm70HTX24qXcdqFci07eQRBYuSBVnX6I2Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام تازه‌ترین موج حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — نیروهای آمریکایی در ۱۷ ژوئیه، ساعت ۹:۳۰ شب به وقت شرق آمریکا [۵ صبح به وقت تهران]، به هفتمین شب متوالی حملات علیه ایران پایان دادند.
فرماندهی مرکزی ایالات متحده (سنتکام) تأسیسات نظارتی، زیرساخت‌های لجستیکی نظامی، انبارهای زیرزمینی تسلیحات و توانمندی‌های دریایی را مورد حمله قرار داد. نیروهای آمریکایی علاوه بر دیگر تجهیزات، از جنگنده‌ها، پهپادهای هوایی و ناوهای جنگی استفاده کردند.
سنتکام به دستور فرمانده کل قوا، همچنان ایران را پاسخ‌گو می‌کند و هم‌زمان محاصره دریایی بنادر ایران را به‌طور کامل به اجرا می‌گذارد.
بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه در حال فعالیت‌اند و همچنان هوشیار، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 470K · <a href="https://t.me/VahidOnline/77227" target="_blank">📅 05:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پیام‌های دریافتی:
انفجار شدید همین الان خرم آباد
خرم آباد لرستان ۴:۵۷ بامداد صدای دو انفجار شدید
سلام وحید انفجار در خرم آباد لرستان خونه لرزید
خرم اباد دوباره صدا اومد ۴:۵۷
خرم آباد دو صداي انفجار پشت سر هم
همین الان دوتا انفجار  شدید خرم اباد
درود وحید جان خرم آباد همین الان دوتا صدای انفجار خیلی زیاد بعید میدونم اینا شلیک موشک باشه
خرم آباد دوتا صدای انفجار
سلام
داداش خرم آباد انفجار نبود
دو مرتبه صدای شلیک موشیک بود
[پیش‌تر پیام‌هایی درباره شلیک از استان بوشهر دریافت کرده بودم.
آپدیت: پس‌تر هم ساعت ۶ از داراب]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/77226" target="_blank">📅 05:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T3ZU0Hkc5c54MpcnawN3bMnV4OYKcdJttiF07KlxEElanzUwOApwDjdFDA0u-zRzjWnGcU5k3K4Vj6djFgzORY3ybwEtKqyucqHMo38YkkrILoX84HxGZjgZVgDOAt31YgrOzkjdUVj8rMUFb1clt0b8Pg58J2GBEwlmPjhEYmVydO8VoEByV-lSVioaLVYekb-LvlfL13u4PS0hphh0uMqBBk5d7LeEgkFtCz9d8ru0T6U6A_ySRq1iS8OtbY43S4c_3cU-R1Ha6KGzKgY2VGi2-wI7qau8dfA8lUTfJ0TlVFk577-tUt-CBL_ZZeObueL5D6SWuGrX4-ELpMCpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، خبرگزاری وابسته به سپاه، بامداد شنبه، در جریان حملات موشکی آمریکا به جزیره لارک، دکل مرکز کنترل ترافیک دریایی اداره بنادر و دریانوردی این جزیره هدف اصابت قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77225" target="_blank">📅 04:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XKdNNWdqbVPcgEum4jHNvBMkO1y4BHC8kKDPBkXjLal5sFBh7qGeLWjLyNJsuYOI_I-CA1zm3-71rIYDyb2vLgfliA7qRjPlNB2KR4oBnIWfFdHdSgA4pRZvjJpLrirBRwzOuW3fWtL2HE6fqFqydqo7dqvK9j0hP6GZvdyIVR1jqGjZLeHtDYIJi1C6_y-oqL10Iw1TL2zAmvjPWQqk48sTjXHdTW-EO4zCTx7_x50p79F9M_v7MnWR3TIsIH79grlJJlhg8vVQo9arE0W91MW1QAYSWj35T2v9M0i7oI-MZORkgC758vqrlkkRI8JQ71DUobFphflAu-iDxWznsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است دو نفتکش پس از برخورد با مین در آبراه بین‌المللی تنگه هرمز منفجر شده‌اند.
✅
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران نادرست است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77224" target="_blank">📅 04:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77223">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام‌های دریافتی از ۳:۵۰:
بندرعباس دوباره چهارتا انفجار شدید بود
باز داره بندرو میزنه
۴تا انفجار پشت هم
هفت تا بندر
بندرعباس کلی صدای انفجار داره میاد
سلام بندرعباس
از ۳:۴۸ تا ۳:۵۰ حدود هفت بار زدن
همین الان انفجار در قشم 3 انفجار پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77223" target="_blank">📅 03:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77222">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرنگار اکسیوس، ترجمه ماشین
:
🚨
مقام آمریکایی: ایران یک موشک بالستیک به‌سوی یک پایگاه آمریکا در عربستان سعودی شلیک کرد
🚨
چرا اهمیت دارد: این نخستین حمله مستقیم ایران به عربستان سعودی در نزدیک به چهار ماه گذشته است.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77222" target="_blank">📅 02:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77221">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lFTJ1-4VkBekB3n-0CTyqlx8E-nRFBmhvbdpiKnlKnCcSEWMf-5Pq04F9WbgpAgO0uEihCc5E80FqW9kApeSRXLTN5dGit9BY8zCNeKRwFA9q8ffoDIAaMRUzafItSMrcDocP3ikTqcSR94ttAgXceOSMaYCmWtsVSCJo8Hza70tvxxz-qve7xJ-cTCXqedUfwDIVYdNv4RkEdkYot5TNnm9jbYrhQdshjrPBZVzmTEAIiIVfmqQp0lzI9YnG0UQ2OQKwCVCKB1ZxcCyWTh39KMbWqwvVCtAacYm4W29Fl5w7Bv3muvTuEsri4s7uZaNce8AUgOeJhg0vkqX-1iY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی با شرح: پل جاده رودان به بندرعباس
شنبه ۲۷ تیر
Vahid
منابع حکومتی:
حملۀ دشمن به ۳ پل و تونل دیگر در هرمزگان
🔹
استانداری هرمزگان: تونل شهید میرزایی در مسیر رفت و برگشت به دلیل حملات دشمن مسدود است.
🔹
پل رودخانۀ شور هم در مسیر بندرعباس به سیرجان مورد حمله هوایی دشمن آمریکا قرار گرفته است.
🔹
همچنین پل محور رفت سه راه‌میناب به‌سمت رودان بعد از دو راهی سرزه مورد حملۀ دشمن واقع شده است.
🔸
مردم از تردد در این مسیرها خودداری کنند. تلاش ها برای ایجاد راه کنار گذر و راه‌های جایگزین در جریان است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77221" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77220">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/daa140a498.mp4?token=YdsFEoT9RqmoA6AQ9rjeYV-hgtYzNT7p7DumZYNIgKo-8Y3R1-leMX55v2smXRZ5eDH05lFJAYSED1DMRW0JqW3ff4OhRmeyQMVc5zs50n99E3WYMMqhEBhD6oTGr4XK2jzsFSTa49MF27eg3G36Oc4A7Dp-hQRWiaexKndoRx6_MbwQD8bTcwIT31SvC6Fc5bHnG3kiXCrdeCfaut7yV5GPq2EoDE4jS6jdCt63_ABKszmDtzqBfD61w8Rounigwxe1hxu2-zqYWzIfUOM7WhTJYt-rM3DoGIqKzVMirGEd55d5khg4A6jIoYJHuNO8hGBkMhlcJGit716oiK-aJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/daa140a498.mp4?token=YdsFEoT9RqmoA6AQ9rjeYV-hgtYzNT7p7DumZYNIgKo-8Y3R1-leMX55v2smXRZ5eDH05lFJAYSED1DMRW0JqW3ff4OhRmeyQMVc5zs50n99E3WYMMqhEBhD6oTGr4XK2jzsFSTa49MF27eg3G36Oc4A7Dp-hQRWiaexKndoRx6_MbwQD8bTcwIT31SvC6Fc5bHnG3kiXCrdeCfaut7yV5GPq2EoDE4jS6jdCt63_ABKszmDtzqBfD61w8Rounigwxe1hxu2-zqYWzIfUOM7WhTJYt-rM3DoGIqKzVMirGEd55d5khg4A6jIoYJHuNO8hGBkMhlcJGit716oiK-aJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
شلیک از خرم‌آباد و زیر ۵ دقیقه بعدش ۲ تا انفجار
وحید جان صدای دو انفجار در خرم‌آباد
زمین کامل لرزید صداش هم مثل ترکیدن بود
تو کانال استان زدن شلیک موشک نمیدونم صحت داره یا نه
خرم آباد زدن
دوتا شد دوبار انفجار ساعت ۲:۱۵ دقیقه خرم آباد
وحید جان خرم آباد ساعت 2:15 وحشتناک زدن
سلام وحید همین الان خرم اباد۲ صدای انفجار اومد
همین الان ساعت 2:15 خرم آباد دوبار صدای انفجار اومد
خرم آباد۲.۱۶دقیقه انفجار
۲ و ۱۵ خرم آباد صدا انفجار اومد
خرم اباد چند بار صدا انفجار اومد
سلام آقا ما خرم آبادیم مارو همین الان دو بار زدن صدا انفجار اومد
سلام همین الان خرم آباد صدای انفجار
سلام ساعت دو پانزده دقیقه خرم آباد صدای دو انفجار
۲:۱۶ صدای انفجار خرم آباد
خرم آباد ساعت ۲:۱۷  دوتای صدای انفجار  اومد
خرم آباد دوتا انفجار پشت سر هم ساعت ۲:۱۴ صبح
همین الان سه بار خرم اباد صدای انفجار اومد
دوتا زدن تو خرم آباد لرستان خیلی سنگین بود
سلام خرم اباد ۳تا انفجار داد ساعت ۲:۱۵صدا خیلی دور احتمالا پادگان امام علی
[ساعت ۳ هم چند پیام دیگر دریافت کردم.]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77220" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62a2ad38dd.mp4?token=excwv7gX4ztWiS4tYTAbgBtLFZSApb26IlqR5X0onq21jwR4blWZ4F4dgKHhEmq88ARYCS4zOUinHELtBIAWIdDYhZUN1253D3YxcP4le0RCFEqnio7V12tYKpLdGraxmj6wBCCEDAjPQhnGsurIosKza8uX3mklQO00q1ZOLqQqJ01X5NNPq-KmRFFId8X2ZADB7z4Qjy55Jjd3-ntzAikWatPODWm8I08y65-WoCUP8_KRQZNyQTkb3BhtQz6EwOYAXKkMBfO18E1VOX_m6ARGtTQVw6TzBVU34vd0Q7ZGGPWCH5jEX-ispwgAO4nC3slEbCv0BmjBd8BcM3mLaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62a2ad38dd.mp4?token=excwv7gX4ztWiS4tYTAbgBtLFZSApb26IlqR5X0onq21jwR4blWZ4F4dgKHhEmq88ARYCS4zOUinHELtBIAWIdDYhZUN1253D3YxcP4le0RCFEqnio7V12tYKpLdGraxmj6wBCCEDAjPQhnGsurIosKza8uX3mklQO00q1ZOLqQqJ01X5NNPq-KmRFFId8X2ZADB7z4Qjy55Jjd3-ntzAikWatPODWm8I08y65-WoCUP8_KRQZNyQTkb3BhtQz6EwOYAXKkMBfO18E1VOX_m6ARGtTQVw6TzBVU34vd0Q7ZGGPWCH5jEX-ispwgAO4nC3slEbCv0BmjBd8BcM3mLaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر پیام‌های دریافتی گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند: 'پل گلوگاه بعد گنو
#بندرعباس
و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
شنبه ۲۷ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77219" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/087c286f67.mp4?token=eqpfbqLxOZz3l3bJUWzU2HoLqE8SXeL9g_26R2BY1jDCuw6513yFt17ZbDocqFFyECPXCrg9djLwihe5SEub5Nbi-eekhYbt-g90buhU3lCG2irbB9ULJm7M4Tlp0MtGWwjQwDasjKxNl2iYK4jOYrMFhChgxBjbCIVwzNVyr9LDzylpSbE56HNyUOq3pPCAdLTyq7jJJBiYauztsQag0W45eT4cy_gAMwqAsC5Vr6VKC8a3XAJpCsWACPK0TqJXF2YhSARelAvLyof0ZQGeNNOv-h2jLANPS4rkunMBzhON8TBNwylkU0FWM-gEGaxv9P-2eNtVLjGRrPdvl0Ttvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/087c286f67.mp4?token=eqpfbqLxOZz3l3bJUWzU2HoLqE8SXeL9g_26R2BY1jDCuw6513yFt17ZbDocqFFyECPXCrg9djLwihe5SEub5Nbi-eekhYbt-g90buhU3lCG2irbB9ULJm7M4Tlp0MtGWwjQwDasjKxNl2iYK4jOYrMFhChgxBjbCIVwzNVyr9LDzylpSbE56HNyUOq3pPCAdLTyq7jJJBiYauztsQag0W45eT4cy_gAMwqAsC5Vr6VKC8a3XAJpCsWACPK0TqJXF2YhSARelAvLyof0ZQGeNNOv-h2jLANPS4rkunMBzhON8TBNwylkU0FWM-gEGaxv9P-2eNtVLjGRrPdvl0Ttvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از تبریز کلی پیام فرستادند که دو موشک شلیک شده.
و مطابق معمول از ارومیه و خمین و خرم‌آباد زنجان و داراب و... جاهای دیگری هم پیام‌های مشابه میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77218" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77217">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر سه تا
شد پنج تا صدا
بوشهر زدن الان ۲؛۳
بوشهر - دو انفجار مهیب با فاصله ی زمانی ۵ ثانیه ۲:۰۴
سومین انفجار مهیب ۲:۰۵
چهارمین انفجار در فاصله ای دورتر ۲:۰۶
سلام اقا وحید بوشهر ساعت ۲:۰۶ صدای انفجار شنیده شد
وحید جان همین الان بوشهر پایگاه زد صدای سه انفجارپشت سرهم
سلام وحید جان همین الان چغادک را زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77217" target="_blank">📅 02:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سپاه: دو  کشتی نفتکش با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند
منابع حکومتی:
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
🔹
ملت قهرمان و بصیر ایران اسلامی؛
حضور شما در صحنه و حماسه آفرینی خیابانی شما، همانگونه که قائد شهید امت فرمودند سوخت موشک‌های رزمندگان اسلام و دعای شما تضمین پیروزی‌های درخشان آنهاست.
🔹
ساعتی پیش دو فروند کشتی نفتکش که با فریب سازمان‌های جاسوسی آمریکا قصد عبور از مسیر مین گذاری شده جنوب تنگه هرمز را داشتند، منفجر و دچار حریق گسترده شدند.
🔹
نیروی دریایی سپاه با قاطعیت اعلام می‌دارد تنگه هرمز به خاطر شرارت‌های ارتش کودک‌کش آمریکا به شدت ناامن و به طور کامل بسته است و تا زمانی که تجاوزات آمریکای جنایتکار پایان نیابد، امکان صدور کود شیمیایی و حتی یک قطره نفت و گاز از این منطقه وجود ندارد.
🔹
شناورها برای حفظ سرمایه و مهمتر از آن جان خود فریب نخورند و وارد مسیر مین‌گذاری شده نشوند.
و ماالنصر الا من عندالله العزیز الحکیم
پیش‌تر:
🔹
سپاه: لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77216" target="_blank">📅 01:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58eec30bb8.mov?token=afVA6KOd3UWvypNlNbbfWjQookLK_69MikvpOZvPDDTYmFsAvD8zmGbkE89NkX1su1AHB5saKymeAAXbS-MhEQ-UnEae1OfT4jvV5sr64R0YZ1fJzPlN5GE1ibCh6VDXY-Pvm0apVKJodkE0tSqKkvZsXHj4c_K8b6Vhp7-JyYqwKwYA68IEXJfkb_8x240UHpVEcUpY2Hzv_2T5EEyHZcTeDTV907aa-fKdHKFZPILVurW2BsSR0pxPlNiVKHTfv7Nz0ezK9XNc43ZqyGVLhp_0uHzYi7A0qCmryQcHoGZgIdNW3T2_MqnVBned36ptA5xKYuaY4eyr64dNZQlLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58eec30bb8.mov?token=afVA6KOd3UWvypNlNbbfWjQookLK_69MikvpOZvPDDTYmFsAvD8zmGbkE89NkX1su1AHB5saKymeAAXbS-MhEQ-UnEae1OfT4jvV5sr64R0YZ1fJzPlN5GE1ibCh6VDXY-Pvm0apVKJodkE0tSqKkvZsXHj4c_K8b6Vhp7-JyYqwKwYA68IEXJfkb_8x240UHpVEcUpY2Hzv_2T5EEyHZcTeDTV907aa-fKdHKFZPILVurW2BsSR0pxPlNiVKHTfv7Nz0ezK9XNc43ZqyGVLhp_0uHzYi7A0qCmryQcHoGZgIdNW3T2_MqnVBned36ptA5xKYuaY4eyr64dNZQlLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پیام‌ها میگن در بندرعباس صدای پرواز جنگنده و انفجار می‌شنوند.:
صدای جنگنده بندر
لرزش و صدا انتجار هم  میاد
وحید جان الان سمت بندر رو زدن
بندر عباس دوتاشو شنیدم
۴ صدای انفجار بندرعباس
سلام سه انفجار بندرعباس
صدا جنگنده هم میاد
بندر داره میزنه
سه بار پشت سر هم
4 صدای انفجار بندرعباس
ساعت ۱:۰۵ صدای انفجار بندرعباس
تا الان دو سه تا دیگه اومد
تک انفجار با صدای کم، شاید بندعباس بوده، توی قشم-طولا حس شد ساعت ۱:۰۸
صدای جنگنده بندرعباس
بندرعباس ٥ تا انفجار جنگنده خيلى پايينه
بندرعباس به شدت صدای جنگنده 1.11
ساعت 1:11  صدای جنگنده اسمان بندرعباس ارتفاع پایین
صدای جنگنده میومد بعد از ۲۰ ثانیه صدای انفجار اومد بندرعباس
سایت موشکی خورگو بندرعباس رو‌ زدن ۳تا انفجار بزرگ با جنگده
بندرعباس ساعت ۱:۰۷ صدای انفجار شنیده شد
🔄
این بار پیام‌ها رگباری بودند نه پراکنده:
بندرعباس همین الان انفجار وحشتناک
وحید جان اینجا رو وحشتناک زد بندرعباس
بندرعباس ساعت 01:16 صدای انفجار شدید
انفجار سنگین منطقه ۴ بندرعباس ۰۱:۱۶
بندرعباس دوتا انفجار شدید الان به جز دوتای قبلی
سلام شبتون بخیر آقا وحید
الان صدای انفجار بدی آمد طوری که پنجره ها لرزید
همش صدای جنگنده تو اسمانه
بندر عباس همین الان چند صدای انفجار ۱:۱۵
سلام بندرعباس همین الان صدای یه انفجار شدید خیلی نزدیک بود که همچی لرزید
😭
این شدیدترین صدایی بود که بعد از آتش بس شنیدم
زددد الان زد بندرعباس
سلام وحید جان همین الان ساعت ۱:۱۶ دقیقه ی انفجار شدید  بندرعباس نزدیک پیامبراعظم که خونه ها لرزید
سلام وحید بندرعباس ساعت ۱:۱۶ دوتا انفجار شدید صدای جنگنده هم خیلی میاد
بندرعباس اول صدای جنگنده میاد بعدش انفجار ده دقیقه پیش اینا سه تا با هم زدن چهارمی رو با فاصله ولی شدت خیلی بیشتر زدن چند دقیقه بعد دوباره صدای جنگنده و پنجمی
الانم دوباره داره صدای جنگنده میاد یه بیست سی ثانیه دیگه میزنن
بندرعباس الان بالای ده دقیقه چند جنگنده روی شهر می چرخند
🔄
همین الان ساعت ۱:۱۹ زد بندرعباس
بندرو رگباری میزنهه
برای بار نمیدونم چندم صدای انفجار
انفجار دوباره پشت هم بندر عباس
بندرعباس الان زد وحشتناک
همین الان ۱:۱۹ دوتا صدای انفجار شرق بندرعباس
زدن وحید بندرعباس ۱و ۲۰
الان دو تا صدا انفجار اومد
سلام وحید جان دوباره صدای انفجار دوتا
بندرعباس ۱:۲۰ دقیقه صدای خیلی زیاد انفجار
قشم همین الان صدا انفجار شدید اومد
سلام  وحید بندرعباس ۱:۲۰ فرودگاه انفجار بزرگ از سمت فرودگاه
بندرعباس الان ۱:۱۹ دقیقه صدای انفجار بلند اومد. قبلش هم جنگنده داشت می‌چرخید.
بندرعباس دوباره زدن
فک کنم تپه الله اکبر دوباره
خیلی شدید بود از دیشب هم بسیار بلندتر 1:16
زدن وحید بندرعباس ۱و ۲۰ پایگاه هوایی
همین الان سمت مسکن مهر طرفای بلوار هرمزو زدن صدای خیلییی شدیدی داشت خونه لرزید
سلام آقا وحید من از داراب فارس پیام میدم تو آسمون داراب هم امشب مدام صدای جنگنده میاد
من بندرعباسم صدای بدی اومد ما محدوده بهشت بندر هستیم
وحید صدای جنگنده در بندرعباس قطع نمیشه خیلی پایینه پشت سر هم صدای جنگنده
دکل مخابرات رو تپه الله اکبر رو امشب یه موشک خورد توش همین الان
برعکس دیشب که ۵تا زدن
منابع حکومتی:
استانداری هرمزگان: در ساعت ۰۱:۲۰ نقطه‌ای در بندرعباس مورد حملۀ نظامی دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/77215" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77214">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3939b6f6d.mp4?token=ddU6r6viPJr1m9U16ss1PhNWCgKSjf9HQElR2fyi5SPZXP4NH5dll5wiDgskJt84EPxGtDP3ri4gpqCJhyUEVWnZxjvPxXwaE-zhsab5WMt07uQ16E_hpVQ78JPqxV5SOQXBZ2weJ2Oo4GHWX_NifFcDREMRKgAI5LwQlUyzxYZh7Y99MdZUWtXhCn979YsbY3TX9SujBTlsB9sdjonQnFBf9rJpKEOl-uu0MqnShVxEWFZbYFJPvkT_-8eBOsaSzM57yQFfkEm1RRZtfuy2ZgGPJsjtzAbsQUDMVYQnEjQMNXPhj0249qqFIpI3ypYstHL-VY0m4Qw6y0STSIsMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3939b6f6d.mp4?token=ddU6r6viPJr1m9U16ss1PhNWCgKSjf9HQElR2fyi5SPZXP4NH5dll5wiDgskJt84EPxGtDP3ri4gpqCJhyUEVWnZxjvPxXwaE-zhsab5WMt07uQ16E_hpVQ78JPqxV5SOQXBZ2weJ2Oo4GHWX_NifFcDREMRKgAI5LwQlUyzxYZh7Y99MdZUWtXhCn979YsbY3TX9SujBTlsB9sdjonQnFBf9rJpKEOl-uu0MqnShVxEWFZbYFJPvkT_-8eBOsaSzM57yQFfkEm1RRZtfuy2ZgGPJsjtzAbsQUDMVYQnEjQMNXPhj0249qqFIpI3ypYstHL-VY0m4Qw6y0STSIsMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: سمت نیروی هوایی
#لار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/77214" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77213">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PC9rjQ_xViwVXLy82jsTKZaA5KnqbqKKbKhzqx9vniEJM6jFBRxIYMygdE40GghO9FLK7uGPg6u_aCbMDfLXE8wNTF4l27YBxOjeQPhyX7dAfaGi6ouN3q-k9P0fTK1Z0tpR4L377Iy2b6ux1gspkpt1ZPhE6tvacu6xZJ8fy3mLrEPC7sxROFPt-I9QdxFtwXPcJGkKom1sAQbdPFBdm37mAmxNYOjctrUnVGN--zO3zE-V3d452saMobDbkfFdBXO-JS--mKwUZz5Y2005Klpn-3lAvVi-comYggjuQojHhC75Ljex2Rm1h3CUoPrB2jHOnigOmCWomNJhVUW4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
۱۲:۳۰ اهواز رو زدن
صدای انفجار ولی زیاد نزدیک نبود
اهواز رو زدن 00:31
اهواز صدای انفجار ۱۲:۲۹
ساعت  ۰۰٫۳۰  اهواز  ۲ تا انفجار  پشت سر هم
منابع حکومتی:
معاون امنیتی انتظامی استانداری خوزستان: دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77213" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77212">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=at6nrC8Z5sUtOUsuCaH5Ov_qHwAwz_Ul1Y-d6mkk0W7PJTifEsXRyK9kzeundlnJ-33MCxIHCtwAQMcuIZRZue1bTqVgjNvvbqglFUDT8cHP4HACPUNoTbZMBL5gSGKb0ee5cl4tiM7bB2JhwaMg_0IcldZibSdPIAEdWk-Jxk-Y9xQBEGFdKJ1XZsJZUvovkBxs7V-_sgFygMdvZksa-eInymaptfcK6SNyivrx3_ajTRUYZNMW9cOjKHJZTJ8bUT98q5gbbxgeglORyr1MBIb6om0sYookWfZG6CdPy3gwE311Qo8mDXNE7NnA76s1bktOA4vtgPE7i4UyOKMqmA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=at6nrC8Z5sUtOUsuCaH5Ov_qHwAwz_Ul1Y-d6mkk0W7PJTifEsXRyK9kzeundlnJ-33MCxIHCtwAQMcuIZRZue1bTqVgjNvvbqglFUDT8cHP4HACPUNoTbZMBL5gSGKb0ee5cl4tiM7bB2JhwaMg_0IcldZibSdPIAEdWk-Jxk-Y9xQBEGFdKJ1XZsJZUvovkBxs7V-_sgFygMdvZksa-eInymaptfcK6SNyivrx3_ajTRUYZNMW9cOjKHJZTJ8bUT98q5gbbxgeglORyr1MBIb6om0sYookWfZG6CdPy3gwE311Qo8mDXNE7NnA76s1bktOA4vtgPE7i4UyOKMqmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
وحید یزد الان 12:30صدای انفجار میاد
5 مرتبه صدا اومد
من تفت از یزد هستم
تا الان ۵ تا صدای انفجار شنیدم ولی دوره
۵ انفجار شدید پارک کوهستان یزد
یزد الان ساعت ۱۲ و نیم چندین صدای انفجار
وحید جان یزدو بد زدن چهار بار
سلام وحید دارن یزدو میزنن
وحید یزد چند تا صدای انفجار اومد ۱۲:۳۰
صدای ۵ انفجار پیاپی در یزد ۱۲:۲۹ تا ۱۲:۳۰ بامداد
من 4 تا صدا شنیدم
یزد ساعت ۱۲:۳۰
بیش از سه بار صدای انفجار اومد و زمین لرزید
وحید یزد رو زدن، ۴ تاشو من شنیدم، اخریش شدیدتر بود.
آپدیت:
منابع حکومتی:
معاون استاندار یزد: حملات آمریکا به خارج از شهر یزد بود
🔹
نیمه شب با حمله جنگنده‌های آمریکایی، صدای پنج انفجار در خارج از شهر یزد شنیده شد.
🔹
پنج موشک در حاشیه شهر اصابت داشته که تاکنون هیچ‌گونه خسارت جانی در پی نداشته است.
🔹
اکنون آرامش برقرار شده و دیگر صدای جنگنده‌های متخاصم شنیده نمی‌شود و آسمان یزد کاملاً امن است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77212" target="_blank">📅 00:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=vzlWH1N9N289K4H61DS5JDBe2A7PsKEmuHzhiEAJmaofQafdNCo0_4-GnVo41hHcNOTCE9WYGjojsMfSpC-w8kSJMu-_NPgra7yVfhb_4jBsaV3IGBR7b7xAz-fC-9WVEhxVdRx_SISKrS7zeBOYirnLmQrhpO-hVwAr4N8FKL0eJb_GV5PnM_iOLBLIwC7D7y-rLX-SjyjypENljRxvfml0f8l9rt1-PDveXtQMOWqT56oe9txMa1vdFOe0CUjl3yOoiVdOHDk3AF7GfirmWL47SPVd0eAuAbTEnWxsKlxfooF8vUFm1WeFPNZuLWMD_JmmOPjg7vxKy3cCVC-jvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=vzlWH1N9N289K4H61DS5JDBe2A7PsKEmuHzhiEAJmaofQafdNCo0_4-GnVo41hHcNOTCE9WYGjojsMfSpC-w8kSJMu-_NPgra7yVfhb_4jBsaV3IGBR7b7xAz-fC-9WVEhxVdRx_SISKrS7zeBOYirnLmQrhpO-hVwAr4N8FKL0eJb_GV5PnM_iOLBLIwC7D7y-rLX-SjyjypENljRxvfml0f8l9rt1-PDveXtQMOWqT56oe9txMa1vdFOe0CUjl3yOoiVdOHDk3AF7GfirmWL47SPVd0eAuAbTEnWxsKlxfooF8vUFm1WeFPNZuLWMD_JmmOPjg7vxKy3cCVC-jvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'حمله به سایت موشکی در جاده گراش
#لار
'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77211" target="_blank">📅 00:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
پیام ساعت ۰۰:۰۷: لار داره پشت سر هم صدای انفجار میاد
سمت جاده گراش
حدود ۱۴ تا صدای انفجار
سلام اقا وحید الان لار دوبار صدای وحشتناکی اومد فک کنم سایت موشکی رو زدن
سایت موشکی لار [رو ] ‌بیشتر از ۱۰بار زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77210" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
سنتکام امروز ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ به وقت تهران]، برای هفتمین شب متوالی دور تازه‌ای از حملات علیه ایران را آغاز کرد. این حملات به دستور فرمانده کل قوا و با هدف ادامه تضعیف توانمندی‌های نظامی ایران انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77209" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77208">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ae40102b43.mp4?token=IZsTJKcfeiCzUFadbkKyGoT5uurqBBGApf3FX4xJpwsAE4_CCt20NcQHnapl6LVguewJNKaTj8b9oDsmzgopTakmdkeVSeZK0rmYxiNbb0hT6D9hSg-eon7U4Y3VNVl3Du06K68FPgy-CF9KDtIDnygLHvgPIUsKvRVN7GnsN6mZMm-5nz0ey2bzq9GXnyVM_4tamReKBGVitejSbUklHvviYK7XqB3V8SYQwtCmGxZ2XzCI1EPLr095aLOJ-1LTDZzQvs4DlhHaq3uM-7jUcsjr7uvX97Y-HAF6jlKJWJw82YgTSZDr7OnJA0CK7YldUPMVA-OJi3BuiEBmHr656w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ae40102b43.mp4?token=IZsTJKcfeiCzUFadbkKyGoT5uurqBBGApf3FX4xJpwsAE4_CCt20NcQHnapl6LVguewJNKaTj8b9oDsmzgopTakmdkeVSeZK0rmYxiNbb0hT6D9hSg-eon7U4Y3VNVl3Du06K68FPgy-CF9KDtIDnygLHvgPIUsKvRVN7GnsN6mZMm-5nz0ey2bzq9GXnyVM_4tamReKBGVitejSbUklHvviYK7XqB3V8SYQwtCmGxZ2XzCI1EPLr095aLOJ-1LTDZzQvs4DlhHaq3uM-7jUcsjr7uvX97Y-HAF6jlKJWJw82YgTSZDr7OnJA0CK7YldUPMVA-OJi3BuiEBmHr656w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، بهمن ۱۳۸۹:
حکومت وراثتی بود. یکی می‌مرد، یکی را به جای خودش معین می‌کرد. مردم هیچ نقشی نداشتند؛ می‌خواستند، نمی‌خواستند، ناچار باید قبول می‌کردند
hafezeh_tarikhi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/77208" target="_blank">📅 23:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d59582925b.mp4?token=czeVBq0p3i1EODdtBcEK-YYTyCZZHdd8EJ1G768D5E7cjv-C6NWrEjuP_GwPpJ9uB5-jV4J5tXSk2Q8qAs4_iG1MIrldmF0mDQXLkt4rp7-nk4oG3mu8ol89vq8qcozUQsxzPqIQZJakYSCkG5UzkEq24SEWs4jZGzVvqUjvcUiFtrWeqSzHrTeQr3oSw37wWtBvvr0NQyhRJGT5C2VlQl3aNEOKgcpBEQ9wNg9izclpNiLJnNVWMsUdRr0GSrTwvQ9GGerNl-np-9_k7df9MOM_m-lLJuOx4fPSUUdNS4bYN_hyxgAK5Zku6m0t5QlOVgKXRpBCvyEd1uKIWi_izQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d59582925b.mp4?token=czeVBq0p3i1EODdtBcEK-YYTyCZZHdd8EJ1G768D5E7cjv-C6NWrEjuP_GwPpJ9uB5-jV4J5tXSk2Q8qAs4_iG1MIrldmF0mDQXLkt4rp7-nk4oG3mu8ol89vq8qcozUQsxzPqIQZJakYSCkG5UzkEq24SEWs4jZGzVvqUjvcUiFtrWeqSzHrTeQr3oSw37wWtBvvr0NQyhRJGT5C2VlQl3aNEOKgcpBEQ9wNg9izclpNiLJnNVWMsUdRr0GSrTwvQ9GGerNl-np-9_k7df9MOM_m-lLJuOx4fPSUUdNS4bYN_hyxgAK5Zku6m0t5QlOVgKXRpBCvyEd1uKIWi_izQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، در صدا و سیما گفت: اگر آمریکا دو سه روز دیگر به حملات خود ادامه دهند، وارد فاز تهاجم و انهدام کامل خواهیم شد و هیچ مرز سیاسی‌ای برای حملات خود نمی‌شناسیم.
او ادامه داد سیاست «هم جنگ، هم مذاکره» به طور کامل پایان یافته و اکنون راهبرد ما بر پایه بازدارندگی، مقابله به مثل قاطع و پاسخ «چشم در برابر چشم» به حملات موشکی دشمن استوار است و ما موشک در دهان دشمن می‌زنیم.
@
VahidOOnLine
مشاور نظامی رهبر جمهوری اسلامی می‌گوید هم اسماً و هم عملاً چیزی به نام تفاهم‌نامۀ اسلام‌آباد دیگر وجود ندارد.
محسن رضایی گفت که پیشبینی می‌کند که اگر مذاکرات شروع شود طرف مقابل قصد دارد «اصلاحاتی در متن ایجاد کند و در واقع تفاهم‌نامۀ جدیدی بنویسند». او در ادامه گفت که اوضاع تغییر کرده و چنین چیزی ممکن نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/77207" target="_blank">📅 23:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77206">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c044eb7a7e.mp4?token=DSFVT3TfHARjwLBnlNRmtpw8JZ8K43kqMwXkXO7AUYU3elMOUp7smzovCjqQRWHvetbFZ8Jhm2ZZL_DskCDvFaIsyCKJkM7tbH7Xie82Sxx1kr6bH5yA7cAuxH-eOc6-mJcWWmdgPhAs9TXLglXA7U7rZPAzvG7wFblKigULPnB8ywYF3F8Zx03Ps1jImAiNHK8F5XXatJnoJmim1kpxx29sNOWdXyE2j4cHgAJk7yr_WFcnuAsFwitwU9SwCde9lUq19xgGW6amQlUe-6dCEM0c2ub_vgube-84eN65XuZ08mUNLHQU-nGLpMPddu4r_M49VAJaNVULzx71Tn7jFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c044eb7a7e.mp4?token=DSFVT3TfHARjwLBnlNRmtpw8JZ8K43kqMwXkXO7AUYU3elMOUp7smzovCjqQRWHvetbFZ8Jhm2ZZL_DskCDvFaIsyCKJkM7tbH7Xie82Sxx1kr6bH5yA7cAuxH-eOc6-mJcWWmdgPhAs9TXLglXA7U7rZPAzvG7wFblKigULPnB8ywYF3F8Zx03Ps1jImAiNHK8F5XXatJnoJmim1kpxx29sNOWdXyE2j4cHgAJk7yr_WFcnuAsFwitwU9SwCde9lUq19xgGW6amQlUe-6dCEM0c2ub_vgube-84eN65XuZ08mUNLHQU-nGLpMPddu4r_M49VAJaNVULzx71Tn7jFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار ویدئویی‌هایی از قرارگاه سپاه پاسداران در راسک نشان می‌دهد که در پی حمله هوایی آمریکا، سقف یک سوله بزرگ در این مجموعه به شدت آسیب دیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/77206" target="_blank">📅 20:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LZZ_a6Ow7bGqTISJkvxI3aXg-Hrr1So6v3i-xh3R-CD0vSc265cHZ0zabdVhmSxy6i7Ouz02iqD6Cq946B4DesVjkBRgJHBYrpvC7QODJjEefgID_9-QbEqd4CFiQcARow87krd50R62ugX-Mfb7kH4asEHEitbwkSGoMFIlWXIDiIBGeXNNo3ljQh5aRb1dEpf0gMHMF90TgPDD4RB2wbFcftz4OIBI-yFLWiskUGkEWfBtlxYxqEA1O0Wlv2pzL6AeVKwOKHKMcQ1hh7fdWzCf28RA9PrhtOXWo-2QzqsbRIKkQ1CdgM2enrD7ijyWa-MhdmoJSCCw5X0nVmkvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس روز جمعه به نقل از سه مقام آمریکایی و اسرائیلی خبر داد دولت دونالد ترامپ به اسرائیل اطلاع داده که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند دیگر هواپیمای سوخت‌رسان را به این کشور اعزام می‌کند.
بر اساس این گزارش، سه‌شنبه این هفته در نشست «اتاق وضعیت» کاخ سفید، چندین طرح جدید نظامی به رئیس‌جمهور آمریکا، ارائه شد و او در حال بررسی اجرای یک «حمله گسترده» علیه ایران است؛ حمله‌ای که دامنه آن از حملات کنونی در اطراف تنگه هرمز «فراتر» خواهد رفت.
اکسیوس می‌گوید «زیرساخت‌های ایران مانند نیروگاه‌های برق، انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف دفن هرچه عمیق‌تر ذخایر اورانیوم غنی‌شده، و همچنین بمباران سایت زیرزمینی کوه کلنگ‌گزلا که گمان می‌رود یک تأسیسات هسته‌ای در حال ساخت باشد»، ازجمله گزینه‌های در حال بررسی در دولت آمریکا است.
دونالد ترامپ روز ۲۲ تیر در یک مصاحبه گفته بود که ارتش آمریکا احتمالاً به زودی به کوه کلنگ حمله خواهد کرد.
گزارش اکسیوس در عین حال یادآوری می‌کند که ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد آماده تشدید جنگ باشد تا خسارتی در حدی به ایران وارد شود تا جمهوری اسلامی تنگه هرمز را باز کند و خواسته‌های او دربارهٔ برنامه هسته‌ای ایران را بپذیرد.
در حال حاضر، ایالات متحده حدود ۳۰ فروند هواپیمای سوخت‌رسان نظامی در فرودگاه بین‌المللی بن‌گوریون در نزدیکی تل‌آویو و تقریباً همین تعداد نیز در فرودگاه رامون در جنوب اسرائیل مستقر کرده است.
مقام‌های اسرائیلی به اکسیوس گفته‌اند آمریکا قصد دارد طی روزهای آینده چند ده فروند هواپیمای سوخت‌رسان دیگر نیز به اسرائیل اعزام کند تا شمار این هواپیماها به سطحی برسد که در آغاز جنگ ۴۰ روزه وجود داشت.
به گفته این مقام‌ها، ارتش آمریکا ترجیح می‌دهد هواپیماهای سوخت‌رسان خود را از فرودگاه بن‌گوریون به پرواز درآورد، زیرا سایر پایگاه‌های هوایی منطقه در برابر حملات ایران آسیب‌پذیرتر هستند و امنیت کمتری برای هواپیماهای آمریکایی دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/77205" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3253e7746f.mp4?token=C3hwZbezglQXLcRS6OosngL0OMkzAxQC67bRjXm66F_3Lx1t0XGiohRGlGjEV0HtpI8C6nI_kdi1l1cI4R0FYaZq-jiljDbsUyyDQQl5oceJKB_YhF2Hg3sW15xV4aCr_pNcyQts4f5JU3nxcErbH6wcG6Wh7TrKF3ZKOT7W-GfoWs3wnpVCwgAP7qEcDn2un0oDqXYoz1Pq1HrJecxQlW2_zvB8vDq649sAHDw1TB2pNddlWqMwLnct7NZ2AJFCgnA8kf4wJVJXa_06NH1EkMQYrFqYxrCFKJq9TeSdj6R07C69SsH-68UtMpJKGGv3eyvKPzJL7CckJbEd0bnIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3253e7746f.mp4?token=C3hwZbezglQXLcRS6OosngL0OMkzAxQC67bRjXm66F_3Lx1t0XGiohRGlGjEV0HtpI8C6nI_kdi1l1cI4R0FYaZq-jiljDbsUyyDQQl5oceJKB_YhF2Hg3sW15xV4aCr_pNcyQts4f5JU3nxcErbH6wcG6Wh7TrKF3ZKOT7W-GfoWs3wnpVCwgAP7qEcDn2un0oDqXYoz1Pq1HrJecxQlW2_zvB8vDq649sAHDw1TB2pNddlWqMwLnct7NZ2AJFCgnA8kf4wJVJXa_06NH1EkMQYrFqYxrCFKJq9TeSdj6R07C69SsH-68UtMpJKGGv3eyvKPzJL7CckJbEd0bnIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا: برج مراقبت چابهار را منهدم کردیم چون سپاه
...
پست سنتکام ترجمه ماشین:
در ۱۶ ژوئیه، نیروهای آمریکایی برج مراقبت بندر شهید کلانتری چابهار را با موفقیت منهدم کردند. این برج بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود که سپاه پاسداران انقلاب اسلامی دهه‌ها از آن برای ردیابی و هدف قرار دادن کشتی‌های تجاری عبوری از تنگه هرمز استفاده می‌کرد.
انهدام این برج مستقیماً توانایی سپاه پاسداران برای هماهنگی حملات علیه خدمه غیرنظامی بی‌گناه را تضعیف می‌کند. افزون بر این، این حمله از آزادی کشتیرانی در آب‌های منطقه برای همه شناورها محافظت می‌کند، به‌جز کشتی‌هایی که در تلاش‌اند محاصره دریایی جاری آمریکا علیه ایران را نقض کنند.
CENTCOM
پیش‌تر پیت هگست، وزیر جنگ آمریکا،
این تصویر دریافتی
رو بدون هیچ توضیحی
توییت کرده بود
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/77204" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77203">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qHFtkWMzJSAbATmLihpmiKsYibHJpgIgPE70aT_8Iwd6lGOtQ7V1-BwxQGc7NojybwDGLYLPG2tKO69aOgU3Z66sErx8j5T9CybbsmhGA-CX5uTi4WH576vUhVpxI7OzdURx4R0A-LGICeG48Pv3Jv5F_QniFrXPBQmClOWGxZEB4NjkkjeC7r5xBLT2_7yGN2PVKbP3448_D33kVeqnzAvJVEtuD74cE5lMJsCtSkYSlxcKrfkHwA49UYUdRV0h2dM7SaPCq5QckMfghTsHnozSifuI6soTi1_JaMpeHoNpUMGNShUfuqEGVlP5tfna31_8rPIINmBeGuh5_9_I-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: "پل و خط تخریب شده دیشب ایستگاه انشعاب راه‌آهن
#بندرعباس
"
هم‌زمان با حملات آمریکا در بامداد جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/77203" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77194">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n_NLqZtnjlt8dqduDqYF8lHMtR1RAmbIjvlPyLX-aTPGq8Q9boWRxoRdAJj41qqDVud_sMWyEZGFDMXByt9md7KfWkDr7FUn7gxiUJJEEnSMTEJBi5xfBC4A3W3rBQ0gi53_YFMyLgdJGKBR-OOnidRbGp7_pKHpnCy8ghNiko3b2rcCW9AS19R62DAm-V9KhNuxJ7HL97ER-Bu3gAuvQ61ENC4nzYiZemobQDbfZ3OXiN9Cy8pNjQx1aQIgoCdD2CdFSxYpMbNUIsBBJt0cjTJ2miW-UVovcw0txMH0Ys_W2TlKI7Ovcz3vrPdkrZtXeezptXkDRI84lQxskqHo9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NQT94NNqTB7_i8USGUgDD1YGPIRaeooWptWcWLhk-pWhzg2bmiFyQXyOtGJvjrepc5_V8tLHJqO9B8nxEgRHsRXfGuB-YsNq6h_X2cmNQA3RtI3RliqM0A3-RYucZ12GvzJ0z63L5IRhjx9pVY9WHuzr1PRAG6TXavpLifSb5-zgRmFgddR18BZuRa65mY1_VcViHMs6ATEiLv4PB1T1V8elZSX0TWGVvfDLtFYyLNTYk-XoIYgV-h7GhkU3byPegdfHBlJXvYah394b3XY-f6NvnTXinPkOInZefWO7YgtAjZ0j6m9Asgb-vnXidXSro2iZGtuuhc6xrPy-tySDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bzJq7sDYDobYiVVcuDju6G5XukNycEf_KeXzs7GMm9JoDTyQEMvf9U9cWikqLcVZz2l1ibBECW944eGZf5tJUvCqSEIpJA471CoFTu6NOUw183Kw3PqQiVS8vHDvKbl-yHtWjFHl7pTl_CeplcG_DwoRUG3XSUiZDLS3aiSGzBjeuZ2AfF9AaElJ26fxw7fYxjtbw5CZZ8dsm5HVN_a1r-AaZVNLzUccTqcTKpjpYgJZgfOe1ccpvy26CflATYZfeK0J0_qstSyqiL8ZpyFCfCSr1tNqlF7mxu9d97fR9bhR2DFuqvXXOsLR2d1seHjuBO_WtJngEczpBZTs-Vk5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DxgTQ8v4uMkVAK4Z9Mk__lNhCno5BHaDrCxOZ1epjmh2SaIw_EEwpiw5zh8PP6s1OMQlS82vmR1-qHztcK-z8iifeQNOLVmzSlc2UqRltScMMvJiJVIRyrxinsBXcb4-PZMF1BfPvLcR8NRz9WFDmTv-Vmhk3SrQVdsMtiAwmwYsHWHxvTp7IqcOGo1behp3mrtnAFj3ca3UcDvI-NGNZ77I10wADaneQNL9VgCZX1jQ9W5jWrRI4WRS6r3KuvjanAo9Rk-IVLGakHzBy8_eX0IqvB_AhAdTA49vQZDmO8NPkH58top-qNC-x8s_sP2F9fNnPySCarPD6LU-sopnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NQeLcpdS3QFjAaxJJQ8a3BHJ2mIunRLOwIfya99cknqqwpENcoh4NUTF5mDX2v-_m-dgUNJsoM81uK2pbN-42s34P5LZug5enm5uHMK9_pqdZHk8Y3zphNjNAhtDDKfioVHAD-SsDvuO1dDiPqHNZQ00z9L0zJgNm5IlU5efBGLTSWxQXLOyvCDhHbVX1MZ2NWHblHcuB-16zi3ORuFdXpO_5HHCzb4W3mUCQH2DB1mJzgKvlkYgvlLZYBZgmGgIa_o9bSVmnox8y1X1LtWdNCe2wwAg3jGhzyGgj5K3pof0jfQajlHOyPe4lh6gzAt1vEDdJY9z2hO92DG9XxSiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/slczZURo-k_-Y_ufgyMnw5tTA5q65g0u1qqeMBViPb4G_iVgwYAsuvjB0wHjToqKWZpUmAa0EB9C-wgm0HW3i-SHb8pqQE_b9jOgpgUWA1atpnxusP2tOqI2pNae3s2PkCtAHEmasJUDRfNCD-RXEZCGYYvoEN8jfKMY0gcyx9guu2mR0QIXwmbYJVf9UwsCaKRby-WiHL4VS09twDxTrzbIKPeV9YAov_aLwAyvnK0JMN0PlRdfQW2uD6SfHfe74tewIwgQdCWQsAfPR0gFevxgHgEEnFAX6qz8MXqs8_TCJc48l8qpV5kzYnrjXQt9FAhyEUsLPAvK3y6ChDCojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NB-3pP3cvLczmnTuJRv5MElaZEL4PU2XSu0NdzcaikBk3ZH-KTmW3F1EHj-nMYH_z2AGTwXAoVB2_JSQXmNGUDdUViilCv1cukd6shawJVk1CNCesDRZ__zky3sW0Cp_0oMUkhpSEuuE_Hv1fRA2kEECsrWSIgYdE_R4hR9iNphSAd4cM2ikTV05RaszRjX6iHPLPzwxtT-2Ya03tDqK9uHkN5cI7ckrgxpwCOrFljeuqfIWPMyKp8TGUkwK_4rIPO3_KIOE8IeLrjLQb1a620qlOKgT3c_Uv1wrJIZl57O4BuLhFB_-_6CRLymhJkybtPGjChkzDP22Bbfyo6qnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/il-AkHddwYFFEqkl7W53g8FQfmhSDAKvXp-q7TTag9A98Ovan9aCePtGq3HeUr0oE03IdYIFffLKNIvnS2ovhylpXRDVcTFpHPqFmoHDA9dfK6k6bPriyxs_-u4zYxUf6Z-dwDaKNz4SKXGDVgJAN0phrMbuz5NfJho95NlAnkJ1A9wL_9Qmu0nI8rjihhml9gH2y_xcK0UOix-ozQ1VzwBu_8e44wqIsBGGEKPAvvap1iAYPB62zjkkUUUfHlwpDjs1RJCwrqphScHBipN-XB4cgmzTEQMQoi3JUhap_SgPRgg7qxUCWLc9WwzkFnvxRlgMab1EB7aQTyD1-6KhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L0qdqX4zxZXALZLz2muix_ohe8i4bUbUschtaPJXtlcGaTkFwk_0-37CTaiakrBygf07EtsXrVibBfO6kbIjl_H9Z4YF2omRZRIDnzjqO6b9iN0RIb303DiI-SH-U03_1grCLYxi0icVxWZrxKRbQ_yYca1q6UqwlQ3eDJdFesg0adVVZmo9UhbjUtG-OQSqD6lax9-OFsLhlwtTE4_n1gjpo7DU0iQSmXRHa1Nv723sB7HR7yaumQwiRozteENUZAcqt3hE_nUmRMue1644ERuxwEQ-aV_0efGBnlo5PsxVQeSdAPm_brSEToSHmdTZgsRIkHCNyJkwxJYVlyKNng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده در منابع حکومتی با شرح:
تصاویر هوایی از حمله آمریکا‌ به پل‌های بندرخمیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 470K · <a href="https://t.me/VahidOnline/77194" target="_blank">📅 17:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77193">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: نیروهای ایرانی مدعی‌اند که به پادگان التنف در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را کشته یا اسیر کرده‌اند. نادرست است.
✅
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در منطقه کشته یا اسیر نشده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77193" target="_blank">📅 17:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77191">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuZu45Lf7njeYCn9QngBelPQp-SwLIAc34WMXzZHqoCxHbHwDvtzsofV2c61lVD4idkSvAWOpOnOkzsMOQ75RzmOJVKTYqe4zt-bdiqExaYYDL8BdT5oEuioRh5NPYjV7twonl47jNHEmoKWueZ952e9DHeybrcpT5WQWiOApieeKAA8pIb0SiOVCgFCytk34yxXebFFUdbueyZRS_JeeHShtQ9WSIyJHNGdvimTgtK-bI3HYvkp_o7-KPKVmRR0X9crYlpD3RJeLU5-f7yjlM2HlpQ8RsZmG721vFzEmN3h106UUks_08TW0KX9uO_j21-Y8VFNTMZeQZottODTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه دور تازه درگیری‌های نظامی بین ایران و آمریکا در خاورمیانه، روز جمعه ۲۶ تیر قیمت ارزهای خارجی در بازار آزاد ایران بالاتر رفت و نرخ دلار به ۱۹۱ هزار تومان رسید.
وب‌سایت‌های اعلام نرخ ارز همچنین قیمت یورو را بیش از ۲۱۸ هزار تومان نشان می‌دهند و بهای پوند انگلیس نیز از ۲۵۶ هزار تومان گذشته است.
از سوی دیگر، قیمت سکه بهار آزادی در روز جمعه ۱۸۰ میلیون تومان و سکه «طرح امامی» به ۱۸۵ میلیون تومان رسیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77191" target="_blank">📅 17:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77190">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMMFCHe8C-ySqkg9wEmmHEeJLz1WCFftdxbpc_HO3c5badz_YHxXBGFMUan4f3AAkpnDo0denfRiHVgWcrwsnOZJJSviWVvp0D-D10-9JT8PXs8Ou4O4psGs4bDsVR4mdZY7J7qPuk8cIZjFDKBfljMH3uYiCv-aSLOOFz_fzy671P7CmC0GxHwTQWrBA5ZbXkvhVvhVboOEPQSTPRlH7d1OtJ4UHeHODKX1gsghiqY9krVNUS0-wbJGv95WdOAEfUPE4LU_qB7beDFyLvsWyjulg7ErIbRBN-s9vI__7vk5td4FHK2BPKqI3cyG4LclEuOVpSfiPkomaqOpWykltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت برق، آب و انرژی‌های تجدیدپذیر کویت اعلام کرد در جریان حملات جمهوری اسلامی به این کشور، یکی از نیروگاه‌های تولید برق و تاسیسات آب‌شیرین‌کن هدف قرار گرفت و در پی آن آتش‌سوزی رخ داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77190" target="_blank">📅 17:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77189">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulMqAydM_uG0G271tkJpI2dKiEPyXnnt92APmWaEMdanT9CGe5-g20a2Anm4eIg813PcG5m3e1K-dW9-FKmCHL-2pk3PQ4vcNXGzpQkqtUYPsXY04GJuFk-Wm_PCRug5BbqvTnC6MDufJsyy8dkpTgtddJh1Q7RJJheOmMlD8xRpeoolLHvNGu213a2bu-XR7skobja1_ieqDnOJsTOX3kaR9vp4FnfuaHV8WMdoAMyrGqCvG5XcMO0usM-0JP58MXmyi9qEYqyxkF8r-aAe4735xKHKe8onC1isDEDS0UECbfCzFitaIdFbTVey8Q2Qkjp_TqSWJO6CvdvUssrrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی و امنیتی استانداری هرمزگان می‌گوید که از شب گذشته تاکنون، هشت نفر در حملات آمریکا کشته و ۱۹ نفر زخمی شده‌اند.
پیشتر وزارت بهداشت ایران اعلام کرده بود که تاکنون ۳۸ نفر در ایران در حملات آمریکا در تیرماه کشته شدند.
بنابر این آمار، در همین مدت بیش از ۴۰۰ نفر هم مجروح شدند.
دور جدید حملات آمریکا به ایران از ۱۶ تیرماه و در واکنش به هدف قرار گرفتن چند کشتی در تنگه هرمز آغاز شد؛ از آن زمان، ایران هم حملات تلافی‌جویانه‌ای را انجام داده است که می‌گوید هدفش منافع و پایگاه‌های آمریکا در کشورهای منطقه است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/77189" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77188">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=PgJw_Spe3pRw8-3LDLq0MyYOpii_kdYbbu-5nnKwmKCEHcgLpFBd6m4gtsA5asOMumwdcXU0JV_Ua6NrRZhkpNGCviFzlgqpQmkXxw3dX7vqEhGOwuQPZ85Heuqp3b9crIcYtOH7xSIG2GZgg2HAkhp-_F2NKmkKReHxAB4-PaJMNSiyxKlSHCrclPn1dbeP8awCzAYD5jzUdJscY-KsmP2DckRCW9kxiPtNItwvDkamDGbOHdKvBIDU7kKiVD58eLmKIKcS_2CRWh0V0uIC6Zz6vt17kObmDui9NYT388iWvqX_RIMG6coFRl7X5U0JhaCdAjrVXFZePUdyHg0f8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=PgJw_Spe3pRw8-3LDLq0MyYOpii_kdYbbu-5nnKwmKCEHcgLpFBd6m4gtsA5asOMumwdcXU0JV_Ua6NrRZhkpNGCviFzlgqpQmkXxw3dX7vqEhGOwuQPZ85Heuqp3b9crIcYtOH7xSIG2GZgg2HAkhp-_F2NKmkKReHxAB4-PaJMNSiyxKlSHCrclPn1dbeP8awCzAYD5jzUdJscY-KsmP2DckRCW9kxiPtNItwvDkamDGbOHdKvBIDU7kKiVD58eLmKIKcS_2CRWh0V0uIC6Zz6vt17kObmDui9NYT388iWvqX_RIMG6coFRl7X5U0JhaCdAjrVXFZePUdyHg0f8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: پل تخریب شده در کهورستان شهرستان خمیر استان هرمزگان
بنا بر گزارش‌ها شب گذشته، پنج‌شنبه ۲۵ تیر، در حمله هوایی آمریکا هدف گرفته شده.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 495K · <a href="https://t.me/VahidOnline/77188" target="_blank">📅 08:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77187">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">استانداری هرمزگان:  ۵ پل مورد اصابت قرار گرفتند
خبرگزاری فارس:
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
🔹
پل گریوه؛ مسیر بندرعباس، خمیر، لار
🔸
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
🔹
دو پل مسیر کهورستان، لار
🔸
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
🔹
پل روستای مارو شهرستان خمیر
⤴️
از مردم تقاضا می‌شود با عدم تردد در محورهای ذکر شده و مناطق مجاور آن، راه را برای تیم‌های امدادی و انتظامی باز نگه دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 494K · <a href="https://t.me/VahidOnline/77187" target="_blank">📅 05:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77185">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v4XeYE2uShTCTZAO0XzdTd8Qk8dD7CAvxH02nriSuaJrMUU5WSbNNbxIOED9AXwhG4WXui7zil1L3wXErlXXZcJsSLDQvryXXKzPwft-KigPA1cCLre9qKE7YHX7ZNJydA2cpvhPvlo4IUtOaD3sOI8fD1Q151zDl2C1XDx1w7aG-WwEyAHq9tpPwAqw_kwLz5RzZcI-ivKUP6PTmqidwAihMoNy0ChHU51dRiXmznwNPiJcOGUE6n0EDu2WFAjhbXH65ANZ0wZi-Viua4b_ewWppVcewUbvj8ITCPww8TS3JsJEX75VwEv6I5SiNtsM70w9vk5ynApDHdp2pTstMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/907635e197.mp4?token=dJFcCmrtsrkuMG53evYSAPn8dgKy4dyEX4hr5sg4ATeaNwHWU1GZnoGALTLhOYKfD7rd_Cu1DYaHP4379sH0HgmSuRf0zrRB-g1sC4MOQU6UUVXh2IvVZOMpPSkfY2dIEUrM31Vz9jqrcwbojmSs5k_MU7M4zaz5q4XNjqGzx-ExrHFwgDl8OLyBjF0qECPuzW3kc21A13XsdyqdQnbxEmc4qzNb5FmTZXkBNRbSfXjc1hTBpazHFUQe1W6ISM5DdhjCIV-WNcgkyruwCWFusM9Mwt6C4FXrQLJlSSTiWdWUj7_GMS1t-p8mIno8SKlpIyFLdmrqTYzkZjMcZCtRlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/907635e197.mp4?token=dJFcCmrtsrkuMG53evYSAPn8dgKy4dyEX4hr5sg4ATeaNwHWU1GZnoGALTLhOYKfD7rd_Cu1DYaHP4379sH0HgmSuRf0zrRB-g1sC4MOQU6UUVXh2IvVZOMpPSkfY2dIEUrM31Vz9jqrcwbojmSs5k_MU7M4zaz5q4XNjqGzx-ExrHFwgDl8OLyBjF0qECPuzW3kc21A13XsdyqdQnbxEmc4qzNb5FmTZXkBNRbSfXjc1hTBpazHFUQe1W6ISM5DdhjCIV-WNcgkyruwCWFusM9Mwt6C4FXrQLJlSSTiWdWUj7_GMS1t-p8mIno8SKlpIyFLdmrqTYzkZjMcZCtRlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از 'پهپاد دیده شده در آسمان
#چابهار
'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 488K · <a href="https://t.me/VahidOnline/77185" target="_blank">📅 05:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77184">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f0b92b95e.mp4?token=aD6MUvVHudZP68ZaYCOUU7pL4jyyMPTDBdoNyhgaZjQbJsPt1UwIC-z4IwBWIS4PwPv_Q1wTCEv-9kbsQ4OxIP2GSmF502WoTvFmd34pjRQp5bZ_roPu3rJPmG4i8xV1wFBjOJlZzlcBWvqGztsfYpM23zEvUQ8ynC0PTsSuKSYTY85YOrNN-l9JKo-6fv6zTykjs09VliwSKepDemMGfO5vT3ro1VZd6yypuD_080VGZmCA-Am9XsgCOwTkap8hevYgsgj-_2wwEKcZdQo9QOk9MMRoVgqEcOKpU0OTAVzmb4rTKZP3nyJpJpjXKTqSn8cXZ1DHdTqu8t59E2lQbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f0b92b95e.mp4?token=aD6MUvVHudZP68ZaYCOUU7pL4jyyMPTDBdoNyhgaZjQbJsPt1UwIC-z4IwBWIS4PwPv_Q1wTCEv-9kbsQ4OxIP2GSmF502WoTvFmd34pjRQp5bZ_roPu3rJPmG4i8xV1wFBjOJlZzlcBWvqGztsfYpM23zEvUQ8ynC0PTsSuKSYTY85YOrNN-l9JKo-6fv6zTykjs09VliwSKepDemMGfO5vT3ro1VZd6yypuD_080VGZmCA-Am9XsgCOwTkap8hevYgsgj-_2wwEKcZdQo9QOk9MMRoVgqEcOKpU0OTAVzmb4rTKZP3nyJpJpjXKTqSn8cXZ1DHdTqu8t59E2lQbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا حملات جدید در ایران را با موفقیت به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) امروز ساعت ۹:۴۰ شب به وقت شرق آمریکا، تازه‌ترین موج گسترده حملات خود علیه ایران را به پایان رساند.
نیروهای آمریکایی، از جمله جنگنده‌ها، پهپادهای رزمی و ناوهای جنگی، با استفاده از مهمات هدایت‌شونده دقیق، ده‌ها موضع نظامی ایران، از جمله تأسیسات پایش ساحلی و پدافند هوایی، زیرساخت‌های لجستیکی نظامی و توانمندی‌های دریایی را مورد اصابت قرار دادند. این ششمین شب متوالی حملات آمریکا علیه ایران بود.
سنتکام به دستور فرمانده کل قوا، به تضعیف بیشتر توانمندی‌های نظامی ایران ادامه می‌دهد و این کشور را در قبال حملات اخیر به کشتی‌رانی تجاری پاسخ‌گو می‌کند.
بیش از ۵۰ هزار نیروی نظامی آمریکا در سراسر خاورمیانه در حال فعالیت‌اند و همچنان هوشیار، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/77184" target="_blank">📅 05:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pz4ribC70EIx4hZhTvvdCr4sNjRLeGasNwdtsXHKjVPbhTEnZFxIIafkQJXPcPss4wkFwDS2W8PBJIBFSkQtvs-VIUY2vBFRt9bWrPpU1KSKjvj3byKNn9ghIQNFIgFQShTeeSQNxE6SAjT766pig2BJcI2e7eOPqMMPPPrZnH2Cirrl_ZLQ2OHpc5pV_1CEFor8cx1TSS2rbLb_7g3VklzvoxMz1b2FP9hMl9B6xQzGevlyXpwRXtshGYUYxorv_QOqxQboj2r-3UWv3XofnNT5o8jYw5KV8GVCdSlThsZrU3ekAr6JpsLWxQggPr7B3U2d1rbZXKdQZRwk1vaq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: 'لحظه انهدام برج مراقبت دریایی چابهار'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/77183" target="_blank">📅 05:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77182">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lISOzF5ruo7ohKTge9X230OiDPBHB4QWU2dK1IVlyfu75-p-si4mpbXsQ4sdG6uSs_KU6bUmDhRNxWmZgeTzNXOj_nFPxKCG-9EpnYtlOWDMt4xOZOp3qD44x2ugBUfjqo6olhZnyqNfMlrLbqGmrzzxgrgiiuJ4j1JC6_6Zlmxg3AmX1FcVNOms_TmS2daojdi5R5rbn4kZ2UBe4qQHwD2OMBXU4x4DXsA5XV16EMeT5jkU0V5VGF7yeugqb5MIroz7w-Aesjoqh_hdnXvDKv2EvduusHwjU4VMM8DHBl78HnmtOcD8obYMJW2Z_HWnuaTqgFXLrJKH1428NJqhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس و پیام‌های دریافتی: در حمله اخیر آمریکا به چابهار باقی‌مانده ساختمان برج مراقبت دریایی فرو ریخت.
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77182" target="_blank">📅 05:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77178">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JK-SxID6qt-RPEnS0g0aizrplkTZSO7xrtdqVbwSQKb6pYeMr8rfK6jE2IUwWNAOJ1k1teDKDHtkWdzgyrp3f2pNjAln5gowqOgqOVdOZnVhrjJ6ws1s_quXKSrF5nbtbQA_osZGTJvHJtlqXLPaU_sDz0kPZVDzcvw4OWrgKfaSnpa5EkJ-9sOAvXqRCUU2eiWzp62aONyb733ekVZ9LVZP71YOQEK59V5hL2tyvBa-2hHYxYdEnQTEuqiy7HU_nZGT13S6p0r-Zxp1aPLrIrJspEejgbcUoRxhb79OmDpK-oMNdPUfqZLbDMSUFDjfmrLGhN4mJ-rmY4fkAizUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9b8ff5804.mp4?token=M7AQySekLs3BTK0b-OvuRJS0_IQIWphaeaBbLgZbdU8XUwAfTDbbCDbAEmYGIC9IXm-cn-8omL7ON2R2pKH75atiDmdkMzN9d33jEvKQe1Pg-b6bcb_IWs7vPAC3DlkFsaCidSlO1vJcZtxtjNB0bYvLWIV2Pvbwkr7LBVZrdU2Ip9dOg_QoLnktDX8kEAtSI8ff_Hvxv1d4IecPPX4uNGAdLybSiBT6QQJaQdd0hUgFJnI36fsud4ksK0AsLvkJ3_neXoQrFJ1KD3ht_QzzFKeKMcZhhIZS-l1sFjH2b6BjsQY9sQE0eSQuPH4iJLKimxIhXoe6b-AFb6PjNvNkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9b8ff5804.mp4?token=M7AQySekLs3BTK0b-OvuRJS0_IQIWphaeaBbLgZbdU8XUwAfTDbbCDbAEmYGIC9IXm-cn-8omL7ON2R2pKH75atiDmdkMzN9d33jEvKQe1Pg-b6bcb_IWs7vPAC3DlkFsaCidSlO1vJcZtxtjNB0bYvLWIV2Pvbwkr7LBVZrdU2Ip9dOg_QoLnktDX8kEAtSI8ff_Hvxv1d4IecPPX4uNGAdLybSiBT6QQJaQdd0hUgFJnI36fsud4ksK0AsLvkJ3_neXoQrFJ1KD3ht_QzzFKeKMcZhhIZS-l1sFjH2b6BjsQY9sQE0eSQuPH4iJLKimxIhXoe6b-AFb6PjNvNkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: دود انفجار حمله به مکانی در چابهار
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77178" target="_blank">📅 04:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77177">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jZcr_MJDEDrRFf8HN1VHFd-OkYtTHauIvxFA7snsZYVoCceJ6OwltpibORNw2Rhgfb6yNVXyUKqsPnubYLun_LDtAU0vwT_NycMFj1jN4yEtluaMtDvXEOZ3le_NCLV0V4wr_SEjNMPWGNePtDSqObu-Kd-VeIgEfc-VPGibk0BczIjTlWLmthw9uo652vYiS-O9jN2WxKTWKjG9YlGW8ddkD0spvFMHg3OyiIEXOO_cC6CjtOXp3aWE9kn4cIKB4Ip8F-5VtPKesK-gLOW1-hb-edDP1wxXxiG161aurU2Q_w0aPmSR-67g4ujB3MZ4ySaNrmslVrtIFC-xwKmkIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری هرمزگان اعلام کرده حمله به پل‌های گریوه و کهورستان در بندر خمیر ۷ کشته و ۹ زخمی برجا گذاشته است.
خبرگزاری تسنیم گزارش داده که پل‌های گریوه و کهورستان که بخشی از مسیر اصلی ارتباطی بندرعباس به شیراز محسوب می‌شوند، هدف قرار گرفته‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77177" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77176">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7aQh9d4TuXVg8I59CM6ge7dKge2LBwG5lvJeHG5LcM2Tx9RbhaRZle0q4T5RVCjGFfKP9hbDv2NZ11A4t2wKDZiIJfY3ZRwwqGvuyEwcNC1srCYXU5lwj7LGrcrU-J9AgkX_QVFIIZbw3-eR0cSa00vaFzlaLJNqcVzgINxOIEiAPVxnvvI5TnWeEYwmhcRwjmus5Vmm9cGhLJws7oRsF8YNuuCP9NQWgQ-NS2UEk8ocy-TuQxuJNQCi_fZUdmYabeEie_yaFHnfnpjDFALK_Ps6TLTkqUltO-SSbo_cx_-f4HwWVc8ZpavQ4t1EbFA1zs-kQaU5-DjpzBnT8OTAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گزارش‌ها درباره دریافت پیامی از جمهوری اسلامی که در آن استیو ویتکاف و جرد کوشنر به سوءاستفاده از مذاکرات و کسب سود از اطلاعات محرمانه متهم شده بودند را تکذیب کرد و گفت هرگز چنین پیامی دریافت نکرده است.
این واکنش پس از انتشار گزارشی مطرح شد که مدعی بود جمهوری اسلامی در پی مذاکرات سوئیس، ویتکاف و کوشنر را متهم کرده بود از نوسانات بازار ۹ میلیارد دلار سود برده‌اند و خواستار اختصاص نیمی از این مبلغ، معادل ۴.۵ میلیارد دلار، به حکومت ایران شده است.
ونس این ادعاها را «کاملا بی‌اساس» خواند و گفت ویتکاف و کوشنر از اعضای مورد اعتماد تیم دونالد ترامپ، رییس‌جمهوری آمریکا، هستند و ادعای سوءاستفاده آن‌ها از اطلاعات محرمانه «مضحک» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77176" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77175">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌های دریافتی:
درود وحید جان چابهار سه چهارتا موج و صدای انفجار و صدای جنگنده
۴:۳۷ دقیقه
۴:۳۸ دیقه چابهارو زد
چابهار زد
سلام وحید جان صدای دو انفجار ساعت ۴:۳۷ دقیقه در چابهار شنیده شد
چابهار ۴:۳۸ پایگاه سپاه امام علی و اسکله سپاه توسط جنگنده ای که خیلی پایین پرواز میکرد بمباران شد.
🔄
باز هم زد
دوباره زد الان ۴:۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77175" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77174">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام دریافتی 'از قطر':
ده دقیقه پیش صدا انفجار و پدافند، دوحه.
Still no threat cleared message.
آپدیت ۴:۲۳:
Security threat eliminated.
هم‌زمان از تبریز پیام‌هایی درباره شنیده شدن صدای پرتاب موشک دریافت می‌کنم. قبلش هم از شهرهای دیگری پیام مشابه فرستادند
.‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77174" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77173">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/146830ca4d.mp4?token=KZF-jvis9c_WILWsY44wQ4ZfKy3FCgLRmMY5IF0WEEMONPBDWhzX03XERtMWCSwRD3Ye5Il5GhS_5f1kBvGGcOBz3mV0NlCAXFCGxoNk2f2eppaNFtqWbUNksYvKUMXHXnGT6Xn6HrewMmn1OY4XEt5ikALqe6d0zhiNCv-95LfzM0yTI85CgIoOcgWYr5maAmE7kXSjZOZaU95RhOPALW3PqHVFMDdCHreV0Vgyu2FV82HSche0ypQwhgSM9RUKTL_hnduKC3FE5VBHTGIu7eXh5HyItGiAksNIrk0_C3u_SOxXd1YEnsFzNcf_8dOfJWU22vPMbqbXOK1vwNQRKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/146830ca4d.mp4?token=KZF-jvis9c_WILWsY44wQ4ZfKy3FCgLRmMY5IF0WEEMONPBDWhzX03XERtMWCSwRD3Ye5Il5GhS_5f1kBvGGcOBz3mV0NlCAXFCGxoNk2f2eppaNFtqWbUNksYvKUMXHXnGT6Xn6HrewMmn1OY4XEt5ikALqe6d0zhiNCv-95LfzM0yTI85CgIoOcgWYr5maAmE7kXSjZOZaU95RhOPALW3PqHVFMDdCHreV0Vgyu2FV82HSche0ypQwhgSM9RUKTL_hnduKC3FE5VBHTGIu7eXh5HyItGiAksNIrk0_C3u_SOxXd1YEnsFzNcf_8dOfJWU22vPMbqbXOK1vwNQRKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منابع حکومتی از
محل حمله آمریکا به پل جاده دسترسی بندرعباس – بندر خمیر و جنوب استان فارس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77173" target="_blank">📅 03:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QQgQk0QqtYCFk1kbflwaIlKTmkQy8hDxKUUkAZzfEPXzZ3HZ1oywtojwR88J-rmXV5xqCJZssKKO1TkiLDHbwlmLWjh76vO6L53iTmXLI7UKrkVMfvFKhH4ESl0Zm4xVF9YHocQ1mr9dIwgO1_pMp8tgmCs4KfKlNwpkzT-ydQvU716mFnyfED9F9tPDVXyIvV_lN1En4PCCm1-ITu40-Oqb8wfHPF_DDXsyFXf3r20bbB7Nz_G08eFhq3AshviFd16M-lI41NKAGqUftsVwxI_hhIGTLTtz05TPx0F-z09Q5_9JPrzeeGt-Ftlne4TpozLQxfiV6dTC81K9z6YvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به روزنامه وال‌استریت ژورنال گفت ارتش ایالات متحده چندین پل در ایران را هدف قرار داد تا مسیرهای تدارکاتی منتهی به بندرعباس و پایگاه دریایی واقع در تنگه هرمز را قطع کند.
آمریکا می‌گوید جمهوری اسلامی از آن پایگاه دریایی برای حمله به کشتی‌ها و نمایش قدرت استفاده می‌کند.
تلویزیون حکومتی ایران نیز گزارش داد که چندین حمله به پل‌هایی در بندرعباس و مناطق اطراف آن انجام شده و بزرگراه‌های منتهی به بندرعباس از استان‌های همجوار مسدود اعلام شده‌اند.
رئیس‌جمهوری آمریکا، سه‌شنبه ۲۳ تیر در مصاحبه‌ با شبکه فاکس‌نیوز گفته بود دامنه حملات آمریکا به جمهوری اسلامی در روزهای آینده گسترش خواهد یافت. دونالد ترامپ افزود حملات سنگین ادامه خواهد داشت و اگر جمهوری اسلامی وارد مذاکره نشود، هفته آینده نیروگاه‌های برق و پل‌های آن هدف قرار خواهند گرفت. او تصریح کرد: «تمام نیروگاه‌های برق و تمام پل‌های آن‌ها را از کار خواهیم انداخت، مگر اینکه پای میز مذاکره بیایند.»
ترامپ در آن مصاحبه همچنین تاکید کرد عملیات نظامی آمریکا علیه جمهوری اسلامی ادامه دارد و این حملات «تا زمانی که خودم بگویم کافی است» متوقف نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77172" target="_blank">📅 03:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3729a1df42.mp4?token=Z32ASZRjicNA7qnDoOwTxBSVr9tbk_zq1MAQnU-kzS2AezbsjAUN1dYPJb11zww0Oe1wVKMbY4VBSlF01-gc0hyS2C20PLX6LDpNlPedaTOVVuaXBcEmd7qZQosLFea419almMEiljYGj0F31Wvu1ZgBN9RakS2lsA2rKziqJYYy-FchDkZeuoOIWz1rMA0qsGAqJnbEVDIZCTSHr5SMUxkerWdZdX7P-iFwkavOlflFwaoQgucOlFxXyy_cqXxBkQImuk47kEY9JJPasZv8GSUtLjchb1SpSiwNG6svyrML6D_dedENT5F-loeDr6SgIvC4ZY4SK09pWouYdhxmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3729a1df42.mp4?token=Z32ASZRjicNA7qnDoOwTxBSVr9tbk_zq1MAQnU-kzS2AezbsjAUN1dYPJb11zww0Oe1wVKMbY4VBSlF01-gc0hyS2C20PLX6LDpNlPedaTOVVuaXBcEmd7qZQosLFea419almMEiljYGj0F31Wvu1ZgBN9RakS2lsA2rKziqJYYy-FchDkZeuoOIWz1rMA0qsGAqJnbEVDIZCTSHr5SMUxkerWdZdX7P-iFwkavOlflFwaoQgucOlFxXyy_cqXxBkQImuk47kEY9JJPasZv8GSUtLjchb1SpSiwNG6svyrML6D_dedENT5F-loeDr6SgIvC4ZY4SK09pWouYdhxmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
سلام موشک از شهرستان جم استان بوشهر فرستادن
سلام همین الان از جم موشک بلند شد(۲:۵۶)
۵عدد موشک از جم به سمت خلیج ۲/۵۷
سلام وحید جان از جم موشک بلند شد
سلام همین الان پرتاب موشک از جم 2:57
سلام وحیدجان الان ساعت ۲:۵۷ از جم موشک بلند شد نمیدونم به سمت کجا
همین الان ساعت ۲ و ۵۷ دقیقه موشک از جم بلند کردن
ستاد کل ارتش کویت اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی جمهوری اسلامی هستند.
ارتش کویت همچنین اعلام کرد صدای انفجارهای شنیده‌شده ناشی از رهگیری اهداف مهاجم توسط سامانه‌های پدافندی است و از شهروندان خواست دستورالعمل‌های ایمنی صادرشده از سوی مقام‌های ذی‌ربط را رعایت کنند.
@
VahidOOnLine
پیش‌تر:
وزارت کشور بحرین اعلام کرد آژیرهای هشدار در این کشور به صدا درآمده و از شهروندان و ساکنان خواست آرامش خود را حفظ کرده و به نزدیک‌ترین محل امن بروند.
این هشدار در حالی صادر شد که پیش‌تر جمهوری اسلامی اعلام کرده بود پایگاه ناوگان پنجم آمریکا در بحرین را هدف حمله قرار داده است. مقام‌های بحرینی تاکنون درباره علت به صدا درآمدن آژیرها یا وقوع هرگونه حمله جزییات بیشتری منتشر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77171" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBq48wmfHYc0YTHtyJwUSp2zIk4KlFYBzH0aMKaHgc-CVjUC_FX-5tqFpDzcKgxcgdM9Ifk5GiZ_7DmeL5Z6asZPTxoW4XYF6DDi3fZubQN5lHN1ZIrEpyy39GRenLbxDJYg8HolsV7Crl4wVeGq7FJ3fDv4ApGFpREjgdDhYJ1scoDyg11b7fI3qpixK1Fctqt1Zyr9FmXHmauPvGAe8LufcW5C1rFuX0mKBQRWaOxUvP3anXBUvllEk1sn__sq16t7CWqYX_bwjlswLqLciS-_bDgAYrVMF3KhF2Dr38hxOP3s1F71ydr_vX2OAInoV_Ei3KqZz8Zn1FJFZBIlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع حکومتی به نقل از استانداری هرمزگان:
در ساعت ۰۱:۳۰ نقاطی در حوالی بندرلنگه مورد حمله آمریکا قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77170" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77169">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/033b4ebf1c.mp4?token=CesuSZA_fMGYqJsW3R7MeFOFvPvKuNljUb_uwk_hR_G_ju-K8VlW7B_owd3STPNOILCwbvrCBuJN2RVfo1j0eF3XJW87tN_0cym0YrlTUQxg1i5DtyRiC9Jm-z3Q5WraC5taLn8_rqDtGCtXkoKo_JAhIjDayVRRdyZLKgmYtHfuaS9CTWWusPkFIt3Qqg0y5Rgh_594_mm_a1_y0w2XGsSJXxB4CE3ABIi-FXPp23_betaRicuPPA1i9fbJqt06qO8WcEzmZTxQLrLNzf79YhRW_ZYtMZu2fbPuF5pZXglWwJybHGG8NRal5zq7CzFHdMem5nL2YlNfXcvT3Jc4-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/033b4ebf1c.mp4?token=CesuSZA_fMGYqJsW3R7MeFOFvPvKuNljUb_uwk_hR_G_ju-K8VlW7B_owd3STPNOILCwbvrCBuJN2RVfo1j0eF3XJW87tN_0cym0YrlTUQxg1i5DtyRiC9Jm-z3Q5WraC5taLn8_rqDtGCtXkoKo_JAhIjDayVRRdyZLKgmYtHfuaS9CTWWusPkFIt3Qqg0y5Rgh_594_mm_a1_y0w2XGsSJXxB4CE3ABIi-FXPp23_betaRicuPPA1i9fbJqt06qO8WcEzmZTxQLrLNzf79YhRW_ZYtMZu2fbPuF5pZXglWwJybHGG8NRal5zq7CzFHdMem5nL2YlNfXcvT3Jc4-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
فرماندهی مرکزی ایالات متحده تفنگداران دریایی آمریکا از یگان اعزامی یازدهم تفنگداران دریایی، ۱۶ ژوئیه در خلیج عمان برای راستی‌آزمایی، سوار نفتکش «وِن یائو» شدند.
تا امروز، نیروهای آمریکایی مسیر ۳ کشتی تجاری را که تلاش داشتند محاصره را بشکنند تغییر داده‌اند، ۱ کشتی را که از دستورات تبعیت نکرد از کار انداخته‌اند و برای اطمینان از اجرای کامل محاصره دریایی جاری آمریکا علیه ایران، وارد ۱ کشتی شده‌اند.
تنگه هرمز و آب‌های اطراف آن همچنان آزاد و باز است، به‌جز برای کشتی‌هایی که تلاش می‌کنند «دیوار فولادین» محاصره آمریکا را نقض کنند.
🇺🇸
CENTCOM
ویدیوی دیگری رو هم توییت کردند. میشه از ثانیه 00:20 ویدیوی بالا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77169" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
