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
<img src="https://cdn1.telesco.pe/file/vVqdbjKiX05vPzjY3uPi-mkVyhkGChjpE8YxtUF4zwbBcys8JAishiCDVeuazcdbx07-EyYYufxsGdT0zXwMvZ7g2NXGgHs0RtuyeCNaIQdJdBM2GUMBYPtCJwWvIBe4KQDl3D5R_Kebge1EZJKkfIhJabNOAi4BixsiCfEGo6cGJ0_kHvrVLsGme9Tk7_b6aMWews2ArT2BDfN0T3YnLdvJzLvBwHUWCA0a0mulVdAsJhRUuBEF5HPwLAp_dVXy6bXZCNfb40fmX6gA3RuCET-9I8ZbiqXCPN4OFzQEJJ8Rw481v9dudOVdoJWJyedqmsYvc-loAs3z8ZJHDFIksA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 23:44:36</div>
<hr>

<div class="tg-post" id="msg-77543">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ویدیوی مصاحبه ترامپ با زیرنویس فارسی در پایین همین پست
متن بخش‌هایی از مکالمه، ترجمه ماشین
:
🔺
خبرنگار:
درباره جنگ ایران؛ آیا از پیت هگست، وزیر دفاع، به‌دلیل توصیه‌هایی که در اوایل جنگ به شما داد و نتیجه‌ای که جنگ پیدا کرده، ناامید یا عصبانی شده‌اید؟
🔻
ترامپ:
نه، به‌نظر من او کار فوق‌العاده‌ای انجام داده است.
ما ارتش آن‌ها را تقریباً نابود کرده‌ایم.
آن‌ها می‌خواهند دیدار کنند و ما هم داریم با آن‌ها دیدار می‌کنیم. خواهیم دید چه اتفاقی می‌افتد. این احتمال وجود دارد که بتوانیم به توافق برسیم.
بدون کاری که ما انجام دادیم، حتی حاضر نبودند با ما صحبت کنند. آن‌ها هم از طریق واسطه‌هایشان و هم مستقیماً درخواست دیدار کردند و ما داریم با آن‌ها مذاکره می‌کنیم. می‌دانید، ممکن است اتفاق‌های خوبی بیفتد.
فکر می‌کنم قیمت نفت امروز به‌شدت پایین آمد. تا حدود یک ساعت پیش هم بازار سهام سر به فلک کشیده بود. اما نه، آن‌ها درخواست دیدار کردند. اگر عملکرد ما ضعیف بود، درخواست دیدار نمی‌کردند.
تنها دلیل اینکه می‌خواهند ملاقات کنند این است که ما ضربات بسیار سنگینی به آن‌ها زده‌ایم.
🔺
خبرنگار:
چقدر دیگر در برابر ایران صبر خواهید کرد؟
🔻
ترامپ:
وقت زیادی دارم؛ وقت بسیار زیادی.
تمام نوار ساحلی‌شان نابود شده است. تنگه در وضعیت بسیار خوبی قرار دارد و همین حالا هم در حال مذاکره هستیم.
می‌دانید، آن‌ها می‌خواستند صحبت کنند. افرادشان گفتند: «لطفاً بمب نریزید. دیشب و شب قبل شلیک نکنید؛ دو شب این کار را نکنید.»
می‌دانید، گفت‌وگوهای خوبی داریم. بنابراین خواهیم دید چه اتفاقی می‌افتد.
فکر می‌کنم احتمال خوبی وجود دارد که اتفاقی بیفتد. اگر چنین شود، خوب است. اگر نشود، دوباره به همان کاری برمی‌گردیم که دو روز پیش انجام می‌دادیم.
🔺
خبرنگار:
آقای رئیس‌جمهور، ارتباطات با حوثی‌ها درباره دریای سرخ چگونه بوده است؟ آیا نگران...
🔻
ترامپ:
حوثی‌ها؟ این مشکلی بود که مدتی پیش با آن روبه‌رو بودیم و همان‌طور که می‌دانید، حسابی آن‌ها را درهم کوبیدیم. بعد از آن دیگر هیچ مشکلی با حوثی‌ها نداشتیم. اما در حال حاضر در آن موضوع دخالتی نداریم.
البته ممکن است دخالت کنیم. می‌دانید، اگر مشکل‌ساز شوند، احتمالاً مجبور خواهیم شد وارد عمل شویم.
🔺
خبرنگار:
درباره عربستان سعودی؛ آیا نشانه‌ای از عربستان دریافت کرده‌اید که به پیمان‌های ابراهیم بپیوندد؟
🔻
ترامپ:
هنوز درباره آن صحبت نکرده‌ایم.
🔺
خبرنگار:
در صورت گسترش درگیری، آیا نگران کاهش ذخایر مهمات هستید؟
🔻
ترامپ:
ذخایر زیادی داریم. انواع مختلفی از مهمات در اختیار داریم. می‌دانید، بایدن مقدار زیادی از آن‌ها را به اوکراین داد و ما اکنون در حال بازسازی آن ذخایر هستیم؛ اما همچنان مقدار زیادی داریم.
از تسلیحات رده‌میانی هم مقدار زیادی داریم؛ بیشتر از آنچه در هر شرایطی بتوانیم مصرف کنیم. مقدار زیادی داریم. صادقانه بگویم، دوست دارم مقدار بیشتری داشته باشیم، اما بایدن حجم بسیار زیادی را به اوکراین داد.
وقتی من رفتم، انبارها پر بودند.
وقتی پس از اوباما به ریاست‌جمهوری رسیدم، او مهمات نخریده بود و ذخایر بسیار کمی داشتیم. من آن ذخایر را بازسازی کردم. اما به‌محض اینکه رفتم، آن‌ها مقدار زیادی از آن را به اوکراین دادند؛ ارقامی که هیچ‌کس پیش از آن ندیده بود.
بنابراین اکنون با سرعت بسیار زیادی در حال تولید هستیم. کارخانه‌ها در حال ساخته‌شدن‌اند و تجهیزات بسیار زیادی تولید می‌شود. به‌خصوص تولید سامانه‌های پاتریوت در حال افزایش است.
ذخایر زیادی داریم. هرکدام از پیمانکاران ما همین حالا در حال ساخت چهار یا پنج کارخانه هستند. وضعیت بسیار خوبی داریم، اما قطعاً دوست داریم از برخی تجهیزات پیشرفته‌تر مقدار بیشتری داشته باشیم. بایدن مقدار زیادی از آن‌ها را بخشید.
...
🔺
خبرنگار دیگری:
شما و نخست‌وزیر نتانیاهو درباره ایران هم‌نظر هستید؟
🔻
ترامپ:
تقریباً. بله، تقریباً. اختلاف کوچکی داریم، اما در مجموع تقریباً هم‌نظر هستیم.
می‌دانید، ایران طی ۱۴ روز گذشته ضربات بسیار سنگینی خورد و آن‌ها خیلی مؤدبانه از ما خواستند: «لطفاً متوقف شوید. بیایید مذاکره کنیم.»
اکنون در همین نقطه قرار داریم. خواهیم دید چه اتفاقی می‌افتد. اگر به توافق نرسیم، دوباره همان کار را از سر می‌گیریم.
🔺
خبرنگار:
رئیس‌جمهور زلنسکی می‌گوید روسیه تصاویر ماهواره‌ای پایگاه‌های آمریکا در خلیج فارس را در اختیار ایران قرار می‌دهد تا به آن‌ها در هدف‌گیری کمک کند. درباره این موضوع چه کاری می‌توانید انجام دهید؟
🔻
ترامپ:
بررسی خواهیم کرد که آیا این موضوع حقیقت دارد یا نه. از پوتین درباره آن سؤال می‌کنم. خواهیم فهمید.
اگر چنین کاری انجام شده باشد، تأثیر چندانی نداشته است، چون ما آن‌ها را حسابی درهم کوبیده‌ایم. این‌طور فکر نمی‌کنید؟
ببینید، روس‌ها تجهیزات زیادی در اختیار ونزوئلا قرار دادند. تمام تجهیزات ونزوئلا روسی بود. نتیجه‌اش چه شد؟ چندان خوب نبود.
بنابراین ممکن است تجهیزاتی داده باشند، اما اگر چنین کرده‌اند، موفق نبوده است؛ چون آن‌ها دیگر ارتش، نیروی هوایی، نیروی دریایی یا هیچ‌چیز دیگری ندارند. بنابراین نتیجه خوبی نداشته است.
فکر نمی‌کنم روسیه چنین کاری کرده باشد؛ دست‌کم نه در سطحی گسترده. اگر هم کرده باشد، بسیار بی‌اثر بوده است.
....
🔺
خبرنگار:
درباره دارایی‌های ایران؛ گفته بودید دارایی‌های ایران برای پرداخت خسارت کشتی‌هایی که در تنگه هدف قرار گرفته‌اند استفاده خواهد شد. آیا ایالات متحده مستقیماً به شرکت‌های کشتیرانی پول پرداخت خواهد کرد؟
🔻
ترامپ:
نه، نه.
از پول ایران برای پرداخت خسارت‌هایی استفاده می‌کنیم که خودشان ایجاد کرده‌اند.
به‌عبارت دیگر، پول ایران که تحت کنترل ماست برای پرداخت خسارت‌ها مصرف خواهد شد. خوب به‌نظر می‌رسد، نه؟ بد نیست، درست است؟
همین‌طور هم باید باشد.
🔻
ترامپ:
بسیار خوب، سؤال دیگری هست؟
....
صادقانه بگویم، با بسیاری از کشورهایی که بدون ما دوام نمی‌آورند بسیار مهربانانه رفتار می‌کنیم.
می‌دانید چه کشوری بدون ما دوام نمی‌آورد؟ اسرائیل.
بی‌بی دارد می‌آید؛ خودش این را به شما خواهد گفت. اگر من دخالت نکرده بودم و آن تأسیسات هسته‌ای را که عملاً در آستانه تولید سلاح هسته‌ای بودند، به قول خودم، به خاک تبدیل نکرده بودم، اسرائیل چند ماه پیش نابود شده بود.
سال‌ها پیش هم اگر آن توافق وحشتناک اوباما را لغو نکرده بودم، اسرائیل نابود شده بود.
🔺
خبرنگار:
نخست‌وزیر نتانیاهو درباره فروش جنگنده‌های اف‌ـ۳۵ به ترکیه با شما اختلاف‌نظر دارد. نتانیاهو با تحویل اف‌ـ۳۵ به ترکیه مخالف است. آیا قصد دارید به او بگویید...
🔻
ترامپ:
نه. ببینید، ترکیه برای من متحد بسیار خوبی بوده است. فکر می‌کنم او [اردوغان] کار بسیار خوبی انجام داده؛ در سوریه هم عملکرد خوبی داشت.
او دوست من است و هیچ‌کس به من نمی‌گوید چه چیزی را باید بفروشیم یا نفروشیم.
ترکیه برای من متحد فوق‌العاده‌ای بوده است. البته ترکیه طرفدار پر و پا قرص اسرائیل نیست. این را می‌دانید، درست است؟ او طرفدار بی‌بی هم نیست، اما ترکیه برای من عالی بوده است.
ضمناً ترکیه کشور بسیار قدرتمندی است. ارتشی عظیم و بسیار قدرتمند دارد و تجهیزات بسیار خوبی در اختیار دارد.
🔺
خبرنگار:
آیا نتانیاهو از شما می‌خواهد با ایران توافق کنید یا می‌خواهد حملات را ادامه دهید؟
🔻
ترامپ:
بی‌بی واقعاً عالی بوده است. نمی‌خواهم بگویم کدام گزینه را ترجیح می‌دهد. او نخست‌وزیری در دوران جنگ بوده و ما در کنار یکدیگر عملکرد بسیار خوبی داشتیم.
اگر امروز به ایران نگاه کنید، قدرتش فقط هشت درصد چیزی است که چهار ماه پیش بود؛ هشت درصد چیزی که چهار ماه پیش بود.
خواهیم دید در نهایت نتیجه این وضعیت چه خواهد شد.
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/VahidOnline/77543" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77542">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: اگر مذاکرات با ایران شکست بخورد، آماده «اقدام نظامی شدید» هستم
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز دوشنبه به اکسیوس گفت که تصمیم گرفته است حملات آمریکا به ایران را متوقف کند تا فرصت دیگری به مذاکرات بدهد؛ اما تأکید کرد که اگر دیپلماسی شکست بخورد، ممکن است دستور ازسرگیری عملیات نظامی گسترده را صادر کند.
چرا مهم است:
مذاکرات کنونی بر دستیابی به توافقی جدید متمرکز است که تنگه هرمز را بازگشایی کند و گفت‌وگوها درباره یک توافق جامع هسته‌ای را از سر بگیرد.
▪️
مذاکرات عمدتاً میان ایران و عمان انجام می‌شود؛ اما قطر، پاکستان، مصر و فرستادگان ترامپ، استیو ویتکاف و جرد کوشنر، نیز فعالانه در آن مشارکت دارند.
آنچه او می‌گوید:
ترامپ در این مصاحبه گفت: «ما در حال مذاکراتی بسیار جدی و عمیق با ایران هستیم. اگر این مذاکرات به نتیجه نرسد، بار دیگر به اقدامات نظامی بسیار شدید روی خواهیم آورد.»
▪️
وقتی از رئیس‌جمهوری پرسیده شد تا چه مدت حاضر است به دیپلماسی فرصت بدهد، پاسخ داد: «زمان زیادی نه. یا باید سریع پیش برود، یا اصلاً پیش نخواهد رفت.»
پشت صحنه:
ترامپ گفت روز جمعه تصمیم گرفت حملات را متوقف کند، زیرا کشورهای میانجی از او خواستند فرصت دیگری به مذاکرات بدهد.
▪️
ترامپ گفت: «همه کسانی که با ایران سروکار دارند از من خواستند: "حمله نکن."» او تأکید کرد که به باورش ایران خواهان دستیابی به توافق است.
در میان سطرها:
ترامپ در توضیح اینکه چرا با درخواست میانجی‌ها موافقت کرد، گفت: «نه چیزی به دست آمد و نه چیزی از دست رفت.»
▪️
او خاطرنشان کرد که پس از توقف حملات، قیمت نفت کاهش یافت و بازار سهام رشد کرد.
آنچه باید زیر نظر داشت:
ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
▪️
ترامپ گفت: «می‌خواهم با بی‌بی درباره این واقعیت صحبت کنم که اگر من رئیس‌جمهوری نبودم، ایران تا الان به سلاح هسته‌ای دست یافته بود و اسرائیل نابود شده بود.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/77542" target="_blank">📅 19:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77541">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZAUnaGSRaikqwdtshQUj_I2ot43q_aYmxi6_yCGu0_wH3i1R3m40XjBa9ze9HuHRPZfaJ6gX5ijtcTk7qxrOLAPAV8HFL8j-QVrLPgKn5koS_t_2t3ShNjGRfEelRmmYgH5ig3U8v29rn0BM1pjGnmBfdmgvYnEhv4-ApqCOo9VQ7ftW_9fTENdAuwz13d-XEmCmbg5tMLGkrjALhEkN4wQyPvHC_dgn98rmtlBHymWZalIetpOi2ohjhpF6mwtRFWXrKBDEV_LbSe382zUmpMqkx6ApmlLon-riuibHr5bmONlo8nKEXNufDTHwTX3jaCFVOdQ6Uar0j7kJe3f3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای «حوثی» یمن، وابسته به جمهوری اسلامی اعلام کردند با استفاده از پهپاد، تعدادی از مراکز انتقال نفت خام عربستان را در مسیر انتقال نفت از شرق این کشور به بندر ینبع هدف قرار داده‌اند.
«یحیی سریع»، سخنگوی نیروهای مسلح یمن، دوشنبه ۵مرداد۱۴۰۵ مدعی شد که این حملات در واکنش به آنچه «نقض حریم هوایی یمن توسط پهپادهای سعودی» خوانده، انجام شده است.
در مقابل، وزارت دفاع عربستان سعودی اعلام کرد پدافند هوایی این کشور تعدادی پهپاد مهاجم را که به گفته ریاض «از سوی گروه‌های مسلح مورد حمایت جمهوری اسلامی» و «از حریم هوایی عراق» به پرواز درآمده بودند، رهگیری و منهدم کرده است.
به گفته این وزارتخانه، این پهپادها قصد حمله به تاسیسات نفتی در منطقه شرقی عربستان و شهر ریاض را داشتند.
وزارت دفاع عربستان تاکید کرده که براساس «حق مشروع دفاع از خود»، پاسخ به این حملات را در زمان و مکان مناسب، حق محفوظ خود می‌داند.
وزارت امور خارجه عربستان نیز این حمله را محکوم کرد. این وزارتخانه از دولت عراق خواست تمامی اقدامات لازم را L«برای جلوگیری از استفاده از خاک این کشور به‌عنوان سکوی پرتاب حملات علیه عربستان سعودی» انجام دهد. درخواستی که به نظر می‌رسد اشاره‌ای غیرمستقیم به نقش جمهوری اسلامی در حملات به عربستان دارد.
همزمان، خبرگزاری‌های نزدیک به سپاه پاسداران، از جمله تسنیم، با انتشار تصاویری مدعی شدند حملات ترکیبی پهپادی و موشکی حوثی‌ها موجب آتش‌سوزی در تاسیسات نفتی بقیق، یکی از مهم‌ترین مراکز فرآوری نفت جهان، شده است. تسنیم این حمله را «ضربه مهلک نیروهای یمن به اقتصاد عربستان» توصیف کرد.
با این حال، مقام‌های عربستان تاکنون وقوع حمله موفق به تاسیسات بقیق یا آتش‌سوزی در این مرکز را تایید نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/77541" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77540">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gdflrCPvQTl3BmFeVSkda_kaoLjOebHlQzeDJ_QPE3iiF_t3VvRfSiCrK4CK-pqLp1uMYrctWsrDLx-74IWgsytAPjDRkc3TeQQOFSNSzF_45mML4HFlYIRN8dSWgJioEN8hUtq-ce0mvGcPRrYUkNfyfCaNGo_ob24GcJrZADiZQVsPXM8xVTVClIcyt8fIzR7ikx1bC4UejrG869EXaw-ZxbqEOlb3IysMoe_jFTY51ly3t1ii1PgkrbMypKNtl7C8EjJOMxopbo4k1IbQBIp8N7t2_u_GgSxNEONMoy1V82wDpC0YyBjzp2AlZavo8oS2S6AazJfojP5qc7ndAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر امور خارجه اوکراین  در واکنش به
پست عباس عراقچی
ترجمه ماشین:
تهدیدهای ایران ناموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین سلاح برای جنگ جنایت‌کارانه مسکو ــ سلاح‌هایی که از سال ۲۰۲۲ تاکنون اوکراینی‌ها را کشته‌اند ــ به آن دامن می‌زند.
ایران هیچ جایگاهی ندارد که خود را قربانی جلوه دهد، چه رسد به اینکه بخواهد تهدیدهایش را با ارجاع‌های مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات می‌کوشد توجه‌ها را از اقدامات تروریستی روسیه علیه کشتیرانی غیرنظامی در دریای سیاه منحرف کند؛ اقداماتی که امنیت غذایی جهان را تهدید می‌کند. اما موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنشی قاطع از سوی جامعه بین‌المللی داریم.
andrii_sybiha
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/77540" target="_blank">📅 18:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77539">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5HFL5c-Uct-ugkiWspb5hqxeL8eOx1L-HQlWBxJfwbxupFZo3xkI1VyO-rHdST13LhGsp7ZA-30o4L3ed_9cl2IPepcx3NMx14J6Eryy999WGdEd9lzd6aKaJ2cvH1K_ILJ1OI1_1grnBiXrE6iMCNolnYBTXPlNthVTkTrN1hBFqmlOjFshfAswITLAxn-X_83v9b4xOMWlfmmbbbGhyQNu-yKa5qCtPBNGpdM76t-U9nofhSxox1eFJYE9JeFjl2xsO3to87auxr-CZUnXf83q9gqDKNb_9M1LcyMvcsgkblMsq81Pq1tJb1gRpjFXbGWIrPCpVQd1P775QPkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی روز دوشنبه اعلام کرد که سامانه‌های پدافند هوایی این کشور، پهپادهایی را که از عراق به‌سوی تأسیسات نفتی در استان شرقی عربستان و همچنین شهر ریاض پرتاب شده بودند، رهگیری و منهدم کرده‌اند.
این وزارتخانه اعلام کرد که این پهپادها توسط گروه‌های شبه‌نظامی مورد حمایت ایران در عراق به پرواز درآمده بودند.
وزارت امور خارجه عربستان نیز این حمله را محکوم کرد و بار دیگر بر حق این کشور برای پاسخ به منشأ «تجاوز» و بازدارندگی در برابر عاملان آن تأکید کرد.
این وزارتخانه همچنین از دولت عراق خواست تمامی اقدامات لازم را برای جلوگیری از استفاده از خاک این کشور به‌عنوان سکوی پرتاب حملات علیه عربستان سعودی انجام دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/77539" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77538">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UwCZvWhKDIuTeknagEVVSQmFNslHgZWofW5dACYIk4fK7RvzzJtkbcQuc-4qS7_W5-VYRCKIjpNs05yK6rOGh5hZuilXXejt5csA3I2p6ECSA82CGcSWi-0J2aQUTSxiI8NncpED5Uwfm4Kw3A4lsdcqYwzmGpAACs0yoafvbMdkEdphDNPeEPIstoqmK4flqlYJuec06dIwf0SdJ_A5XxaFKdLEXmdGdIzVIwbjxlnIGQZJKerU3sYtdW2FhvTRnDFEggQVuHEdq-oq7UOnB3B0t62z1E10ppYQ_sbs8i6IIoO0_WIr5d4_389U9n8Al8c5GhAMqbzVKPCIa7bh7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای مسلح اردن اعلام کردند که صبح دوشنبه دو پهپاد را رهگیری و سرنگون کرده‌اند.
این بیانیه مشخص نکرده است که چه کسی این پهپادها را به پرواز درآورده است.
کمی پیشتر، تایمز اسرائیل گزارش داد که ارتش این کشور دو پهپاد مشکوک را بر فراز مرز اردن رهگیری کرده است.
در آن گزارش نیز درباره منشا شلیک این پهپادها و زمان دقیق رهگیری آنها توضیحی داده نشده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/77538" target="_blank">📅 17:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77537">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOyLI1ervmMdNyAd2teH-VyfvcOmmec_Lha4604PXoPB2Ej6OP0q4xUzAdojNCESRDtpokglLxncPNryuntGzMnjAQzaAuOPx_YluGVFhomd57zvrlxgY_sNfk1U3un6MTUOGw858fPRi4HYz2Bq3a12TZ43GxHLIwhAF0YSsF8Kj2uGVTiHgAwfnNs_dk4S8D0M0agSrXNxpccb9ZMe8F9bHxCSr4D2aIQowg_oAfWjFuwO7HfaCH76vUowIq_mB5A0RMbe0_J34BDLB5MjYM1jO2TGTfKu1l90-GOKPS337_fpYY9gr7TVkDMk6tXm05ky8xj5doKA1OXezNV_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«احمد الشرع»، رییس‌جمهور سوریه، روز دوشنبه ۵مرداد۱۴۰۵ در گفت‌وگو با شبکه «الجزیره» اعلام کرد دمشق با مشارکت چند کشور در حال تلاش برای دستیابی به یک توافق امنیتی با اسراییل است.
الشرع ابراز امیدواری کرده که چنین توافقی بتواند زمینه را برای دستیابی به «صلحی فراگیر» فراهم کند، بدون آنکه «حق سوریه بر بلندی‌های جولان» نادیده گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/77537" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77536">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZf3rskBzCB4OSC6PKorH4jWXj2KfW9S4Xn0e6wO0-bqlNyvVkROga1C_vlJQ_eLN6sJ9spZshQYvPDiFEzo0fdnwQs2tHlsBNsJQQhVWYqDZ5ExLZJA6DgkNsn-M1hqKzctIt0z4hpiXtVfCg_ubXXnG_WTwb2_9O6SK95Ue6f1xiruAKh67wpNuRrogD3wOqx1weESL40aGiwoUHzwUPpB14U9qOldJPCJwJaSrdJfO5Ss1VwKx5jRcWBZ7cE2gsFbf4befsLmYx78lOuXV4Fu-XMumbnE5nwgGTl0nmtQ2pc0JLGBQxngJGVsvfsGOMLAg0speTeVDPLt1YJDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر پیشین اسرائیل، می‌گوید هرگاه دوباره به نخست‌وزیری برسد، «فورا» قطر را کشوری «متخاصم» اعلام خواهد کرد.
آقای بنت در شبکه ایکس، دولت قطر را «خشن» و «سرطان یهودستیز» توصیف کرد که «شاخک‌هایش را در سرتاسر غرب و حتی در دفتر نخست‌وزیری اسرائیل دراز کرده است.»
او همچنین مدعی شد که در دوران نخست‌وزیریش، اطلاعاتی را دیده است که نشان می‌دهد قطر به سپاه پاسداران کمک مالی می‌کرده است.
این سیاستمدار راست افراطی که از چهره‌های اصلی اپوزیسیون اسرائیل است، قطر را متهم کرد به‌دنبال «نابودی» اسرائیل است.
آقای بنت نوشت که قطر «کشور پیچیده‌ای نیست، میلیاردها دلار در یک شبکه نفوذ قدرتمند جهانی سرمایه‌گذاری کرده است که صدمه زیادی به اسرائیل وارد می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/77536" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77535">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iki6E22Zb9WwkN_9PEFsuqDP8jRRAnXd3g1_JiZW2wZWBLOER3TqVCqOEjOaFp1kNzrGhIk05IRIqQjbTRy9aNpqwSw7osRI9u-fICeR7VG4wut-Och2-mJ1Wq34ojVmBLXJDC-su8HyQAsF_9IczhOBYej2dt1WuY-kJQJAZ2R1OyNBj-w3nHmbm8vioZfLPGCxGgpuVBW9Z1j41NPEJ6tmkPUxNmFUlmRlYpPyyOxrelVMAAL_YZIkLpEGU7-BYzNRhy7A6V9UnPfzFhMEEoE4pegSJ9Tj5eOvrMpgU6OqWH-WbRJQP8SSDcg3dQ4ah-oQfiCUIKt0i9k-BNW17A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع بریتانیا گفت کشورش از اقدام تهاجمی در برابر جمهوری اسلامی حمایت نکرده و نخواهد کرد.
وس استریتینگ در مصاحبه با شبکه اسکای‌نیوز افزود این موضع را در نخستین هفته کاری خود صریحاً به پیت هگست، همتای آمریکایی‌اش، گفته است.
استریتینگ روز ۲۹ تیر و در جریان تشکیل کابینه اندی برنهام، نخست‌وزیر جدید بریتانیا، این سمت را بر عهده گرفت. او در همان هفته با هگست درباره امنیت دریایی در تنگه هرمز و تعهدات ناتو گفت‌وگو کرد.
او گفت با وجود این، زمینه‌های فراوانی برای همکاری دو کشور از تأمین امنیت تنگه هرمز و جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تا سرمایه‌گذاری در توان نظامی بریتانیا و ناتو وجود دارد.
استریتینگ همچنین گفت اروپا روزی از دونالد ترامپ، رئیس‌جمهوری آمریکا، سپاسگزار خواهد بود که قاره را از رخوت بیرون کشید و متحدان ناتو را وادار کرد مسئولیت امنیت خود را بپذیرند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/77535" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77534">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vPhUMRzA_uhkOuPD11Kii7nfzrnrUCG1gaXMKGVJO7hDG_u3oEJpsS7mKjSydLMuZbRYbWz5TbszK0iBzNGdbH6gFHnAbfO4xavnRQzZqvRMmBvfz6YYMei4nGvlmRIU5yzZsEhzsbUNoat9NzS5OlB9p7FqDbV6qrRyQkDFkpiJDD_8jeCPf6RnRYbD7z6143yzElHolXhXUuZbQ492NyncwY-u9WODY-QIE7b2VNLAkU9vHZXXDgxD5n_4KYfr5XH6rrR9XwnDR9fflOdf4isFoLRUWl4wZszDtoS2Laa8pdh1q2_8qjucvgFn0-RZ-UahK1D-drAvwObguXqkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.  زلنسکی روز شنبه، سوم مرداد، در پیامی در…</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/VahidOnline/77534" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77533">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmnM8kfmTfBb6UWvsLlFhXwnDAVuvN5DdjGyQfmSZF3vVxdJgd1ANWEuJ93chZukp54Zn3T6LYnuKrYV0M-5tjg9V_2Z5vu6KGTqaCE6vFrdfi2aQMfBO1hQJjb_6VA55qj5lI1bi3B11DfUm7SZrSWon1abqxrXdEiDywEJeiawGaXIKiSJNfzq55Vlb1th45TFHOV88wFoXuSnhmWDMrx8H40dkh0MDVuP9s3gf3HHFE_YE6r0eZ1Ju7R4jV0fc8gzkGCudpqUTYINAtA5bY3p2KS0CKuCDvks6Nb9lq9ODuM6TzN1hn1JMBI-cyTKOtl5NMknNPF-3v6aQVaUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، دوشنبه ۵مرداد۱۴۰۵ در نشست هفتگی خود با خبرنگاران، گزارش‌ها درباره درخواست ایران برای مذاکره مستقیم با آمریکا را رد کرد و گفت: «درخواست مذاکرات مستقیم با آمریکا اصلا با ژن ما همخوانی ندارد.»
او تاکید کرد که در حال حاضر هیچ مذاکره‌ای میان تهران و واشنگتن جریان ندارد و خبرهای مربوط به درخواست ایران برای مذاکره، «خبرسازی» طرف‌های مقابل است.
بقایی با بیان اینکه جمهوری اسلامی هرگز از دیپلماسی برای صیانت از منافع ملی خود گریزان نبوده، گفت در شرایطی که آمریکا به گفته او همچنان به اقدامات «ایذایی و تجاوز» علیه ایران ادامه می‌دهد، تمرکز جمهوری اسلامی بر دفاع است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/77533" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77532">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpQPEWzpYnEQV6m9N6oDE6LNRYC2YaIdwEwcv4IV5avdzA4nZ-cT9Z29KWS9foBcxtTaA2bJlp6g9tvBypmF0omor2EL22uH9sSZW-3NLSPeuc6CHYpswnTv4NRvDdFmQmqpUr2d6DPesAx_XgeOTC80JWs6UhoSgdnpt4N-NJb8sCt9pgRI7Tst-h5c78hNMozHaCHNuYorud7nky5K6YSi5YBbiydihH8z1ZODIA7KQUjFoSWNpCQgK2RnNUWslewJLVw34I2mh7-Tblokm2PyP0nPWAqY8pwVpjKygAuFJD2drJ-nB65MCkvqAqr32dxCgLLKqh_TD5ESvZ9mYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون حکومتی ایران روز دوشنبه پنجم مرداد خبر داد که سپاه پاسداران در بامداد همین روز مانع عبور شش کشتی از تنگه هرمز به قصد خروج از خلیج فارس شده است.
خبرگزاری صداوسیما در کانال تلگرام خود نوشت: «در ساعات اولیه بامداد امروز دوشنبه ۵ مردادماه، ۶ فروند کشتی متخلف با خاموش نمودن سامانه های ناوبری و موقعیت‌یاب خود... قصد عبور از مسیر غیرقانونی و نا ایمن جنوب تنگه هرمز را داشتند.»
اشاره این خبر به بخش جنوبی تنگه هرمز نزدیک به سواحل کشور عمان است که اعلام کرده تابع قوانین بین‌المللی برای استفاده از آبراه‌هاست. ایران در مقابل اصرار دارد که کشتی‌ها باید از مسیری که سپاه تعیین می‌کند عبور و مرور کنند.
خبرگزاری صداوسیما همچنین نوشته است که یکی از این شش کشتی‌ «دچار حادثه شده» است، اما تاکنون هیچ منبع دیگری این خبر را تأیید نکرده است.
روز یک‌شنبه هم خبرگزاری تسنیم، نزدیک به سپاه پاسداران، مدعی شده بود که یک نفتکش در تنگه هرمز پس از برخورد با یک مین دریایی منفجر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/77532" target="_blank">📅 16:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77531">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxftTUR3V4e8td0Ryo_btWTHbMtNJcugvY231SQvq7T2HgO6qz_MUHfRD34tPH9jLVIHF_MHpacbNL5dXcaQcc8Ju4SOB0Yp2_bz9R1Kp8SDyN1vKQKhxHgrcjNzLYiYzHBZZRObX2imZT5jftCezagNeik1UjhXols2f2L-b-y3Iclf3enRUNC-DotvTEmgqCZHseLHp31f2iOZrKpqup67IgzGBnF-NMOJtGIbtwm6m1399GCJu_7JhUw1PSC7DsGZTz1h7Q5nxm0ZMd_UhX8SRtsgMXp-HRwRYjLl0pGCXWjBlI50t-hB6iwdhMeQSbSxCbCe5dMkqHpI4MxTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت امتداد گزارش داد حکم محکومیت پژمان جمشیدی به تحمل ۹۹ ضربه شلاق به اتهام «رابطه نامشروع» پس از رسیدگی در دیوان عالی کشور به طور قطعی تایید شده است.
الهه محمدی، خبرنگار امتداد، به نقل از ملیکا پارسا دوست، شاکی این پرونده، نوشت شعبه نهم دادگاه کیفری یک تهران این حکم را صادر کرده و پس از اعتراض و فرجام‌خواهی، شعبه ۲۹ دیوان عالی کشور نیز رای صادره را عینا تایید کرده است.
بر اساس این گزارش، اتهام مطرح شده در پرونده بر مبنای ماده ۶۳۷ قانون مجازات اسلامی (بخش تعزیرات) بررسی شده است. طبق این ماده، مجازات رابطه نامشروع تا ۹۹ ضربه شلاق است و در مواردی که عمل با اکراه و عنف انجام شده باشد، این مجازات تنها برای فرد اکراه‌کننده در نظر گرفته می‌شود. به گفته امتداد، دادگاه کیفری یک و دیوان عالی کشور در این پرونده تنها پژمان جمشیدی را به تحمل ۹۹ ضربه شلاق محکوم کرده‌اند.
ملیکا پارسادوست با اشاره به قطعی شدن این حکم گفت صدور رای نهایی نشان می‌دهد «فضاسازی‌های دروغین» درباره این پرونده، پایه و اساسی نداشته است.
او همچنین تاکید کرد اجازه نخواهد داد آنچه بر او گذشته با روایت‌های دیگر بازتعریف شود و گفت از ابتدا این اتفاق را «خشونت جنسی» توصیف کرده است.
پارسادوست در ادامه گفت هرچند این حکم از آسیب‌های وارد شده به او نمی‌کاهد، اما در شرایطی که به گفته او اثبات خشونت جنسی در ایران دشوار است، احراز این موضوع از سوی دادگاه که رابطه «بدون رضایت و همراه با اکراه و عنف» بوده، برای او و دیگر زنانی که تجربه مشابه داشته‌اند اهمیت دارد.
او در پایان با اشاره به کاستی‌های قانونی و دشواری‌های پیگیری چنین پرونده‌هایی گفت با وجود مخالفت شخصی‌اش با اجرای مجازات‌های بدنی، پرونده را تا پایان پیگیری خواهد کرد و ابراز امیدواری کرد این پرونده زنان دیگری را که با خشونت جنسی روبه‌رو شده‌اند، به شکستن سکوت تشویق کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/77531" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77530">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMyT1UwBD7omhpcKNB1jUpVrcx7RcUHOkmesw-hG7NUZ53xEL373WwTdVKKXZdZyjuW-pDfZw9J55r-GcFsGdosmxCE1CYnAf8PNL_xBZAnAqLntPp5ATlaaN2TjXr7w8I1LSkE7qi_X95CYW9mm9b0NlEyp851omcQ6j3NIV1wt43yHBySLzHi19cPBjy3B1Nwse4JbPTCEeth4lV5S6QoFJx6R6McNYy8pNwllHO8wOXp78SE_8uH_WiiPFNvANSAkbMDyRrYdYkUPRePy-Ky2uKr7AgpkzTG-HVPnaZB4tXDqli-UrbC7VarWtiPfQBCCD2v6fmP0CK76BNKfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش خبرگزاری «رویترز»، همزمان با ادامه وقفه در درگیری‌های مستقیم میان ایران و آمریکا، بازارهای جهانی روز دوشنبه با «کاهش قیمت نفت»، «افت ارزش دلار» و «رشد محتاطانه بازارهای سهام» واکنش نشان دادند؛ در حالی که داده‌های حمل‌ونقل دریایی از ادامه اختلال در مسیرهای کشتیرانی منطقه حکایت دارد.
بهای نفت خام برنت بیش از چهار درصد کاهش یافت و به حدود ۹۲ دلار در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز بیش از پنج درصد افت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/77530" target="_blank">📅 16:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HtzlpP369ELuEHr3SNl_0aI8bCAL4L65SN3HZONA0UEYJy_-Nl-HHdO7Fwsp_GDnGM-Ppr4lncT4KN2vIDzfCNJcCOw1GTUoC3B5u_ImBX7r921MK6zkWknzfkz0E7jczuW8GeAKcHyxq7gN41HjL_twVdTR9VETWOL-o8ReSWf2kHNhzcTzo2Mbt1JgcwzAo-8tpR9Gk9Z8Kp_B5vtwmeC5fMzTeh-B-9VlZ9T16LaChe-p8OjhiYJD83R5Lh86YIG460dQF_2dT3P56u4ZatSWq2QAiZYwCJEEEok_UNHy49LhLFELjYBBOng2l8GDycYOEkDQ6xjdZbCqn1nYSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در بیانیه‌ای که به روزنامه وال‌استریت جورنال فرستاده، گزارش‌ها درباره کاهش ذخایر مهمات این کشور را رد کرد و گفت ایالات متحده «بسیار بیشتر از هر کشور دیگری» مهمات در اختیار دارد و میزان آن نیز «بسیار فراتر» از نیازهایش است.
بنابر گزارش‌های دو روز اخیر، ژنرال دن کین، رئیس ستاد مشترک نیروهای مسلح آمریکا، کاخ سفید را در جریان کاهش ذخایر موشک‌های رهگیر پدافند هوایی قرار داده است. این موضوع برای او نگران‌کننده است، هرچند معتقد است پایین بودن ذخایر مانع ازسرگیری عملیات رزمی گسترده علیه ایران نخواهد شد، اما خطرات آن را افزایش می‌دهد.
چند مقام آمریکایی نیز به وال‌استریت جورنال گفتند دریاسالار برد کوپر، فرمانده سنتکام، معتقد است آمریکا می‌تواند با محدودیت ذخایر پاتریوت و دیگر رهگیرهای پدافند هوایی کنار بیاید، زیرا در صورت تأیید ترامپ، افزایش حملات آمریکا توان ایران برای شلیک شمار زیادی موشک را کاهش خواهد داد.
کارولین لویت، سخنگوی کاخ سفید، و شان پارنل، سخنگوی ارشد پنتاگون، تأکید کرده‌اند ارتش آمریکا برای اجرای هر مأموریتی که ترامپ انتخاب کند، تمام امکانات لازم را در اختیار دارد.
وزارت دفاع آمریکا شامگاه جمعه کارزار تازه خود در بمباران مواضع در ایران را پس از ۱۳ روز حملات هوایی شدید متوقف کرد و تا امروز، بامداد دوشنبه حمله‌ای از سوی آمریکا گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/77529" target="_blank">📅 16:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2CdvtUsUq1DSwZHnEtM_zgjYZ8u37-nYZeKaQ2VRf1X_EU9zdNfcCnFWoWVVWgBqOameY7Dur6Zkb-3gewlo_FaODLsAuWg17HJrVoBIR0VnqoetN_tniAqmDGBitWIO3wGot8tJDx7cBKOHc0gFDFBFTk4A2MhCUyrRjSIde57-HHdkB-f5MtGg3mWVP0hHz0ih2guzMcz02AE_sc1Oh1ojDvhnkqwrS2v7fqaDml5S0Tu11y-9QQsDTA-ZkzVrC5iU5Ermb7IDyMwJJ3xD76JzBZvoEPGCWEdysypMYK_rbmVsjUXE_2BCrKb8QonOAlFqywR13A1t7yAKuRX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اجرای قریب‌الوقوع حکم اعدام دست‌کم دو نفر از محکومان پرونده اعتراضات دی‌ماه ۱۴۰۴ اصفهان افزایش یافته است.
«علیرضا سپاهی» و «ابوالفضل سپاهی»، دو پسرعمو که در این پرونده به اعدام محکوم شده‌اند، برای «آخرین ملاقات با خانواده» آماده شده‌اند و احتمال اجرای حکم آن‌ها در صبح سه‌شنبه ۶مرداد۱۴۰۵ بسیار جدی است.
همچنین به ایران‌وایر گفته شده است که «سمیه افشار»، مادر علیرضا سپاهی و مادر همسر ابوالفضل سپاهی، در همین پرونده به پنج سال حبس محکوم شده و هم‌اکنون دوران محکومیت خود را در زندان سپری می‌کند.
اطلاعات موجود در حال حاضر تنها درباره وضعیت این دو محکوم تایید شده است. با این حال، از آنجا که چند متهم دیگر این پرونده نیز با حکم اعدام روبه‌رو هستند، این احتمال وجود دارد که افراد دیگری نیز برای آخرین ملاقات فراخوانده شده و در معرض اجرای حکم قرار گرفته باشند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/77528" target="_blank">📅 16:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77519">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r7awIUrq7c0VdEZc3NO23ZTE11pYwqMv-rI-mW7JrFtrmPQinpFqmlTDAkEzIPoydahLEl7WuB0UJ8vhXaN42rrK9m16LmejJ5gBIiuivNF4lXQzU77Z5jTLbUGX_9S9EGcv8K0p8kditQaUxOT5YQ4e4vk_kEoyemB3RgVSwR_Dti6QgxlaFS2RT-Vdj4yRo3YsunqIE3uZ3ybaR-Olj_PxVdUMAAqaULdKIRRXEGRLcbKsTJ0wX56iGb3JCryFQumMd_eWsl9O_kA9X2ud7tRlThJQLXXNcb8mId9MFoyR3AngCl7kLpeQjmJ2CLDLL4AKLFZRH0QGzFJMC6gEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lNj_L_LNVG39nkmGMuPQ4slTtny-eN3wvuBUglRnV4y7BdPWjmEQuZmvapvO3LLHCwPDm0ZVQ5nCpfcIByXJ5BChMtd9gC3LNEf7FqrzerD5G9jj0YA9Hyp4cOhBp0ybPem9vmJf2_-VEWhelhL_ib50eq2lepihe2ILKaZDfwJgvWFNYBeHhPgJfMZDojaqnzEDPTnIIlaSJ3jL4jGRlHifoo4QcdMBpCn4My8V2LyjW1WMqYirr9_EJkCVvn58fY9s1EI1gV_viaJ8l7hh1MU0tYi3cYifq5dkziFhPJHaYaKVuauApQIeFWDNEi2_JaTlGvnLfUE6FJlGdGLomQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hMaamAnjuQtesIgKeUtLhnkh4N6EAAKhpeMC3zPwUdyXu9g0zM-G40ejJMHcdqgzGRpA0kHOS9m68HiPc2z-Wg6_jEEQfy8guelssgwZv75ncnI3r6DTbYII7JfqEQPQ55kv-8a4vi_k3uJzJRWDoE3O3onOZzkznIKyqs5pScSfAvvxImXin0w3GURP2jkGf8ihXP9ZIv9TNeoRTGBvwG1bxxeOaeU8Blc1Bkh4C7WPZC8qwVrrVP1azoJhws8tACtkflL2vyo5vI7OqDVs54_eqYBP625AKc5wHqi_4Uikjn89JnSXeAN9kmni4G081ewBy9NupVckOMk8V4QjNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NTUkJZhoLNQPLiYHW5qJSpcijyD2LMvfEbPDzV0cvIbece8Y1rBa-AOonyEfp6YmA4D43uoaf3hSaLvCNyrv5cUH1dsiwv0Nkdi2eRKidgB8Q_bwmCh040uIJylTXslKl2BhuxpWSbdRLW50F0guUpnT5-zKr5dNKNricuCizFYo4ajVCTWuNqM7W1XhrVvcOkWg8jdQzIz6CYV_-sPolQN9LLiJ6VSn-aE6YUOTi0is_hICNMcehKVMfpOwBgPZNRNDYs74l6Gfjk1X5zO4F9GK5oMMeRrrl9Lad_dlr6rQXNAPyBy9NT5SZtR-mu0b5HGxun2vQwhEjkPj_dqb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EyqWKuTKy3VZ3lHuizrfsEqACLsk7AAsobJIzKNdnFv0JPdln5ogIdfEy9U1wc68wG8_Yoj-E-zN_5tcamVeYfP3oGTU0B3qQ9OPiQ1ooMdOLhob3BVfEklVnAnSPI3gMGtnxTp6pe2ca6O9DbvMtdtxDipHOQc6Rw2FuUPTnESCVGuMP8_uCzAr-KppDVvKCXiNeNfpEqvkKX_5e2gm-bUdR0n8jLPVq38gEfCyb423RMCCKNL5dlzrz1aNiIJEbUdLDnq8SPOZtP7EhL1keqy5xc1efFdOxU_JlCs-4NZkIGShObqyTkzk3VA9KPx1KpHlhVwx-RzYQrgfKdU8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nQpOwvXBPgRiDKKpvxcmRceQpFX_rqgJSITtN5kV0Y0Gf0XAW9YYZSO5g_EJYMYB6fqVJFLeVGlOdk7T992yttZua6tDHR5P4bcH9DegQex94rl3XtarzQa2PJLFmbK0z_sHpfNXw59SWzzWqa9b7dO_nAPFOOZEDNx1cpFTGjJlsfjwr1ak6dXaViQhaZZr9QMEpgMU7FNWzCryDtmGpaypqc5dkQcxi26wEDOZUrSwm_ipRjklT4cO2KoyCQLXy89iImqPIP1WTBcVlKUC2sJAj8AKkR70u5xE-GipeKJBnHmkd4U5NLBkDVl0-FqWHP58eWQt4SPKIho33-zB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L9sQ-LUq-cDayPzRP5N0hv_qE_75CgkuH2aEayMetL2qcVCJNWdP9LhMUSLmtRaGNsvcrpSs2AWYZG2dJyLav3mbKrbn2zX0Hi2yByTyCv_4-eeCJWAiQbOpzeZLYEqGkLLpWfD81Pgm_T5-OlYIO8z9NtIagoPCS_huIAmNNX_c2BbZ05V558yC7UurPup3gEhEfxli_8eu4Eb9vwK3XVy8HPtv-X6EsF8xcZCjlNVodu9MssdNhaPXLf3hhtAvAqSBbdFbWQ7xFRQj7iCfUDaL4IulPUBJ2WfzCsUIjmJChci1hkIxuxP29K92RSTN8HetZ3IYzL9dME3S7eHPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s9SCyobMPCTGTWYh_XrLyrYkOXxYM9mXcQqOZUzHG-jhzI2NkjN5a_R-5mI1BF5iTX7YgG3hqbL9HCkW_OWXoZ5rnUPHy6hR17bioxqMmtr16rkYahFp446gi5mmwDyUcOSNXjJH0NGPDjKWj6JIa64fU4JazS19Q-V38N9rzHPDJSZW4aRZPlfAo1vooXA7WzGis4gMrSLblnk6u7UDIZ4MFbxz3ViEMtWlgcB7UvK1eavCwypDB-vubVseqdVKNRVzutTNOotEoBSohQumZ6Lkx4Ir21lEAddBRshXIRbjkOUHD2OBu0oyvn0Pv2GuJtSoI659X3ClNcqedHxiKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B8ODDnjduGjnVyyOPaBi_EdMZeoeQyPiG3yFMiOqdlPYTQWqsi0cN4DW6asq79ixUWAOjrUUK3stf-jcNvsjV8oWGYULmDR8h9MVqOQCVRepuK-oOUNKT9tG2lNNeuTq8W27Xve9OWUIT9W6lBcSgV-GCFdJPs7tqsK116s0FqKoMN21bgph2PILql32v4YhaBzWXwYYsW1HJdjhc6eYorsR33-pzbQ4QOLIeoM6nVQFn1U_BtkNnsfwQo19Sv57a4SdwzDJtOf_xYDeEpHAnZpWzwfnqxNG3ZkWGxomig0_KQDBUCgprYvF_oVJyqa1MD7FQe0AbvmFz1Yg5HFPaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز یکشنبه تصاویری ساخته‌شده با هوش مصنوعی را در «تروث سوشال» منتشر کرد.
در این طرح‌های گرافیکی که با عبارت‌هایی نظیر «این نفتکش اکنون متعلق به ماست»، «خداحافظ اتاق موتور» و «دیگر موتوری در کار نیست» همراه شده‌اند، صحنه‌هایی از انهدام و آتش‌سوزی ناوها و نفتکش‌های جمهوری اسلامی ایران و حضور نمادین او به همراه نیروهای آمریکایی بر روی شناورهای توقیف‌شده شبیه‌سازی شده است.
او پیش از این نیز تصویری گرافیکی از «حمله به خارگ» منتشر کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77519" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77514">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jfh8v18IEMeQckN_4U9fYjlKWJG9d9doOVaV3zx6qqy_Sidva8xiyOHEzODW-4OJiLnQWiSNacTN6M1liH5c1Zro4S6Soafamog8DKE1p_a37nb-Y7LPgxKuM8TttY4rdbBvDBTjCPcBw0SwS9NI1zb-Q-KrA0JQVcEFgKST-W0t-oUAkUg1fJ2aqPNuMG5S72OqR3zC9kAqKCGZndS-UhMyHrApFNBlnyFjIij5V-nk1FY9KYRg66W96VWOdfsOtpqV_n-NopKavKHgwEL99QMwU63oTCI9OzZ73FH-0A-iTEJTBpkX2OUQ2iZGROqsef-WOmC5RenQ8U_2Br0grA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UbXs4PD1SqFdwPKADvDF202G2H7qAZV56XQCgEM3d6FnlIxHvs5C5tZUe4D5lQVcluvQDRQD-mEhSFmxFP4pYX7KMb9ogTXnNEgWLNhwIJ3RPmxBdhfuDy_jRMETi5kg-8IlVTDbLiGBw1aWoE9mAlcSwnw5hSj6PJWxi1Y8N_rNYhNEafYG7BzWWKaKEgLNye2wqHt51AQ-8SwPPrc9umIbqgBSkOB30nA3fBkx3EkJusjUz2a1P4zQbfrMEy6zvS9L2jyq5gfy60nztJ36VUlW103X0Dq-DRp-HKHAC5ovr5uoYStg6TKH3z5V_qwesfIr86MxfXW4lWmvOixYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ewBH5CTOHLi8AOGc7qmouzgURYDAzAbYl9KOa0uQ8t1rjKzTMyMT1tdNVcZ4Z3qao8HOzN8aEz9fm-uWAXm8bF4NXt010SIYKXSRG5JWLDofk4Ypjp0JnkdiYCYdNKlp0cj037RSdFtk2A1KGEA67BjToRqaU-s0KHzUhWM0R6OnkzK4MBQNyXH2SXK6pDjoHl9498EjuWEF3JMrhcCuhPInnaypw_d5QmlQLKxTiPBkDxy-Sv6U4HQ86FaHiLo1I_hwn3YO-RzofM3ixlXtiJb6LxzHKa2805yn92CGI5ipx9GzWw3zmHrhyPScm52oiRaOXY-3wgSaoey17THtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UUX03o05Ur7TctnUUlW00ZP8WhpAZgNRn5FG-7FU7sBKB_4gF6PQAwimW102vTTgszAFm6nVCOoMrcsqUcT8gXip6fJTyWxsf88leWB9sNStY0LkszNaHlqOqwxkHOcEon3aPR8dbTxVnq5C3OqU7JFmn4JGQQPGU9uI_zYMrON4a-ljTpyjIFNtaHpU5dJ7ZQ7PN1nstmw_V0W-PAeSI2oi2vCgDRKO345nlQgCS0GaVlpNrczGg_ao4yFe6DliM3Ly9VU7bjPsnlfA5fbPaMLPQyy3_wLBMg9M1BfXZLexCOOVNuio_-6ysqIEiUXZmM61sb5axdwsf3CMVItjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eaAlSFH86QV6-Y7VZy7YIeXSKmOEonJ9dd_VWmbCkZ9NvaXIAX9vWuhCNPk6uld4gL5ox-7Le0GQG5V09qhNyhIklUN_dJlW9WpHGv_h-mfTbYxOuev0_y_QVNtK9iQHVPZ0Zf71j3EyBGY1RsTpPCLtciUCFpspfCTto4SSHDAikD_DbDs5LDpvEzdRe3QE9GuYL31zLCQpBamBgMABeTGSBCBAEOoXO9pWMdAH022bTf69pmg5w7HVUNHhviZaqYrMPwg1iEGxlAmimvz9j_CgeQlTfZ_WD6VeyVXN-kB0KLncFz7pGAywuE_0H68w2iwZ443WnZNQlIwP-iTJTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در حساب کاربری خود در شبکه اجتماعی «تروث سوشال» تصویری ساخته‌شده با هوش مصنوعی منتشر کرد که یک جزیره شلوغ و ویران‌شده در میان آتش و دود را نشان می‌دهد.
روی این تصویر عبارت «حمله به خارگ» درج شده بود.
ترامپ تصاویر دیگری هم منتشر کرد که با هوش مصنوعی ساخته شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77514" target="_blank">📅 00:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxAUpZhLK5wVWGNIAMS0tK-sM5LCirjKBRHOq27lMpAGkqO4jCY_OxyWFUChZGm0eHTnZ7LmtTyZXUwF5drSLVDsu0hRSWLSxOb3_TxA1ZIOO9s7-YNv07vqizLoJGtc73CTNJ3KFiNuk3E8WWcW2mxbsXfN2zle8mCetx2N3vmLse0_3Zrjt1SZJnLI8l7KtPeSBO9KlVXFC7U1KknZhpp-ehle4fSat1D3hiL9zLpP8SWGLziRwCSe0E4oor97SE33eNDZme6_1qfm304UIerO9ehTUHTg7HeDE3_KDKBH5p4LqWhEIqMFHJnAxrJ_gAbZ1wXrxqQG6fdAxvYKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از منابع آگاه گزارش داد برد کوپر، فرمانده فرماندهی مرکزی ارتش آمریکا (سنتکام)، به دولت دونالد ترامپ توصیه کرده است کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا به اعتقاد او این عملیات به سقف اثربخشی خود رسیده است.
به گفته این منابع، کوپر ارزیابی کرده است حملات دو هفته گذشته توانایی جمهوری اسلامی برای هدف قرار دادن کشتی‌ها در منطقه تنگه هرمز را به میزان قابل توجهی کاهش داده و بیشتر اهداف تعیین‌شده برای حملات هوایی نیز از بین رفته‌اند.
منابع آگاه افزودند کوپر به مقام‌های آمریکایی گفته است در صورت تصمیم برای از سرگیری عملیات گسترده نظامی، آمریکا می‌تواند ۲۰ درصد از اهدافی را که در عملیات «خشم حماسی» هدف قرار نگرفتند، مورد حمله قرار دهد. با این حال، او تاکید کرده است اگر تصمیمی برای بازگشت به عملیات گسترده گرفته نشود، ادامه کارزار بمباران دو هفته گذشته توجیهی نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77511" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edX7Hjy3jMfmDHLt-mh3vf2YLFtCUCOQpdzNJO1x_8cfICpqWDH4IZQkFHwub1WIv6pGp1RrrMpaQu4AVo4AmlQ25-DpUbHI6fEuM6tC7fWMmLCSVmSftn8WX1JZOD89vBTiQrObCZnU4BzYAtrZ46YEa2I2CeBSfMKsluFx39QRgH08OKCciqJmJNx0-FJ-qLhoRWHWGA6IJGF2rhRXcCFXTRBV5giXDbigP4aszMntsrAPKvHpEwDMhI7FsrPgqKtVFu0BthXkSgToUC1HRK9QrZ9prnohUm39oFhXDTEbSEfu6gpbbpy71e_bX1u_Qd9-Pn5Nx9JAWrMD2OB3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران با انتشار پیامی در شبکه اجتماعی اکس، حمله اوکراین به یک شناور «تجاری» ایرانی در دریای خزر را «نقض آشکار منشور سازمان ملل متحد» خواند و اعلام کرد این اقدام «نمی‌تواند بی‌پاسخ بماند.»
عراقچی در این پیام نوشت که ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، با حمله به یک کشتی «تجاری» ایران که به کشته شدن یک ملوان ایرانی انجامید، به گفته او «به خواست اسرائیل» تلاش کرده است اروپا را وارد جنگ کند. وزیر خارجه اسلامی افزود که در گفتگوهای تلفنی خود با کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا و سرگئی لاوروف، وزیر خارجه روسیه، تاکید کرده است که این اقدام نباید بدون پاسخ باقی بماند.
ولودیمیر زلنسکی پیش‌تر اعلام کرده بود که نیروهای اوکراینی در عملیات‌های دوربرد در دریای خزر، کشتی‌هایی را هدف قرار داده‌اند که به گفته او برای انتقال محموله‌های نظامی مرتبط با ایران مورد استفاده قرار می‌گرفتند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77510" target="_blank">📅 19:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDo2sW1043bihROY0q_OcAu8A7uV-99AEW3HoXymqsxIMMViEb7tRF2rrMdgHWXWy32NpAHCdlEsJ0mzQykOeIzef27yPkb6bigGJZnxY0svTf8MAiDysPAW-iQ1q-M20HhRxK-W-fGkEe8GDkRO82vuhvyVLy98KccJBK9v8w8RTVNNZXTDq5Ky6G8OC8WCA1tf3cgfHzkPLmHbLW3uGohoMceDCZLwgzj_4186_adX-7fBqJB5H_XzjQzPNfSjUddtia6HwVtiDOcC1DNvjYgmZSSi_cQCk7PYXc0jGAJ6nS1809UfFprdAukPZS3Irc7zDJhA_0RTue2QUf6W2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسراییل، گفت درگیری با ایران زمانی پایان خواهد یافت که حکومت جمهوری اسلامی سقوط کند یا آن‌قدر تضعیف شود که برنامه هسته‌ای خود را متوقف کند.
او در گفت‌وگو با شبکه فاکس نیوز مدعی شد جمهوری اسلامی باید به این نتیجه برسد که ادامه ایجاد «آشوب اقتصادی در جهان، کشتن هزاران شهروند خود و حمله به دیگران» هزینه سنگینی دارد. نتانیاهو تاکید کرد که برنامه هسته‌ای ایران «چه با توافق و چه بدون توافق» باید پایان یابد.
نخست‌وزیر اسراییل همچنین هشدار داد اگر ایران یا گروه‌های هم‌پیمانش به اسراییل حمله کنند، با پاسخی «بسیار قاطع» روبه‌رو خواهند شد و افزود تهران در صورت انجام چنین اقدامی «اشتباه بزرگی» مرتکب خواهد شد.
نتانیاهو درباره سفر پیش روی خود به واشینگتن و دیدار با دونالد ترامپ، رییس‌جمهوری آمریکا، گفت قصد ندارد اطلاعات تازه‌ای ارایه کند، زیرا به گفته او، همکاری اطلاعاتی میان دو کشور بسیار نزدیک است. او افزود مشتاق است دیدگاه ترامپ را درباره آینده درگیری با ایران بشنود و گفت: «در بسیاری از جنبه‌ها، این تصمیم اوست.»
او همچنین اعلام کرد که «قطعا» برای شرکت در نشست مجمع عمومی سازمان ملل در ماه سپتامبر به نیویورک خواهد رفت و گفت قصد دارد از تریبون این سازمان درباره اسراییل و ایتلاف اسراییل و آمریکا سخنرانی کند.
نتانیاهو در ادامه از زهران ممدانی، شهردار نیویورک، انتقاد کرد و او را به دامن زدن به نفرت علیه یهودیان و حمایت از حماس متهم کرد.
او همچنین گفت از کاهش حمایت حزب دموکرات از اسراییل «بسیار نگران» است و مدعی شد شماری از چهره‌های اصلی این حزب تحت فشار فعالان سیاسی به مواضع جریان‌های ضد اسراییلی نزدیک شده‌اند.
نخست‌وزیر اسراییل در بخش دیگری از سخنانش از موضع دونالد ترامپ درباره عربستان سعودی حمایت کرد و گفت ترامپ به درستی تاکید کرده که در صورت عادی‌سازی روابط ریاض با اسراییل، تنها باید با یک برنامه هسته‌ای «غیرنظامی» برای عربستان موافقت شود. او افزود آخرین چیزی که اسراییل و آمریکا خواهان آن هستند، شکل‌گیری یک برنامه هسته‌ای نظامی در عربستان سعودی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77509" target="_blank">📅 19:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEk28fjsSgwZxJ4I3gXwN1bNRFl9aqFV1wJBBP77JJU2X-VARUnpVM7IJee5tjNZTevovM8REed3hCinl9VdR3wzGH4lhAB0qsP1CDFegzJba8MBQ1Nk7MUxWaq3U4Gwo3L8GKTLutnxddKjsAb6hWKp8ZLP_JmZRses6SPvXIy-7AVX3wuDcUuJt8NvPcszZx7cklCsVvG7YpZtECjtaHG24AdBvulgenYH1viDD6yXrnp2NPTS8GrpzKnfxlVTE0ouRDzJNy7Rsgmw9XAlmFlYedPIKcjfbV0bIPmlHH6Ft_SnkQDLKhCvAv3FO1HDDaZqvu8uyaIcsYGEnjrggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک والتز، سفیر ایالات متحده در سازمان ملل، اعلام کرد که دونالد ترامپ، رئیس‌جمهور آمریکا، حملات علیه ایران را به‌طور موقت متوقف کرده تا فرصت بیشتری برای پیشبرد دیپلماسی فراهم شود.
والتز روز یکشنبه در گفت‌وگو با شبکه فاکس نیوز گفت: «او دارد به مذاکرات فرصت می‌دهد؛ کمی فضا برای پیش رفتن گفت‌وگوها فراهم کرده است.»
سخنگوی ارتش جمهوری اسلامی نیز گفته که در پی توقف حملات آمریکا، ایران نیز حمله به متحدان واشینگتن در خاورمیانه را متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77508" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77507">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkj569AsHe8RaFRvFqPdu4nYb4JmzW01XZwFb3ZB9NszrEoAEOGPVcFXvRVIJemkCAUlj0iSnaviRWaR4RbzsChRclMLOsfGaA7I3i2z5rCd_faDMo1FBU1SLxwNTbjE92eN166Om37HKIzbsejhBxIM7UGZV1rO2BqZiW-HsZz6RrYjWIup5n89JhCcIV_wjr0BHv9zmp2dvMauzc8T4U48pwmgC3tcrpKyYwQ87-4VvbFQVwZWYa67WrTwNsq3abooOl0S9WxwNWHuV0PjykVmX5ciHsjHHcybL2wR5TIHczGlVTt23pI6LFXifyI0LIQ9TQXZFNPD1DLkCcUAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز یکشنبه مدعی شد که یک نفتکش در تنگه هرمز پس از برخورد با یک مین دریایی منفجر شده است.
بنابر گزارش تسنیم، این نفتکش پس از خروج از مسیر دریانوردی مشخص‌شده از سوی ایران در این آبراه راهبردی، با مین دریایی برخورد کرده است.
بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد که اواخر خرداد بین ایران و آمریکا برای تمدید آتش‌بس امضا شد، ایران متعهد شده بود طی ۳۰ روز در تنگه هرمز مین‌روبی کند تا تردد کشتی‌ها آزاد شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77507" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77506">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ru3nxCHlVjPJpKQ7OewwvSGaxMPEkzZfY7CMAeYkK87MnFFmcyoKao80c3tH2EDv29tz2gwofGuwWYrI6s3vmnrCN_INuSyygOuuybfz4M9s1edm7tvatdaDk-w33zAkq5CzGI5iyI19KhJW-Fm2Eld5jvzqLM4iz_wiPr1e1QFvEmYtQmiIwS_79NZZvNRdNdhW7xzSfGnRfydG1w3tym-DPFlnKUfGjOEYVlf-pZPR5pfiq2wDX89RrV_Hpe21mDkEt0jy-iiPz-4lyflPMY_cqcVQbmPNQG3lVu8fO_jyPjhm_mH-9omq_rdwj4W6968zPJt0OYoEuXSxtbiKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری العربیه، روز یکشنبه چهارم مرداد ماه گزارش کرد ایالات متحده آمریکا و جمهوری اسلامی ایران پاسخ‌ خود به پیشنهاد مشترک پاکستان و قطر را که با هدف ازسرگیری مذاکرات میان دو کشور ارائه شده بود، تحویل دادند.
بر اساس این گزارش، منابع آگاه در گفتگو با العربیه تایید کرده‌اند که کشورهای قطر، مصر، پاکستان و دیگر میانجی‌گران منطقه‌ای طرح جدیدی برای برقراری یک آتش‌بس ۱۰ روزه به واشنگتن و تهران ارائه داده‌اند. این طرح با هدف ایجاد فضای مناسب جهت حل بحران در تنگه هرمز و احیای توافقات پیشین تنظیم شده است.
العربیه نوشت، این پیشنهاد دو شرط اصلی برای بازگرداندن دو طرف به مسیر گفتگو دارد که شامل توقف فوری اقدامات خصمانه و بازگشایی کامل و ایمن تنگه هرمز به روی رفت‌وآمد کشتیرانی بین‌المللی است.
بر اساس جزئیات این طرح، مقرر شده است که مسیر جنوبی دریانوردی از طریق آب‌های عمان از حملات نیروهای مسلح جمهوری اسلامی در امان بماند و مسیر شمالی از طریق آب‌های ایران نیز از محاصره دریایی آمریکا خارج شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77506" target="_blank">📅 16:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77505">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vMeGASEF9fKa4QJV6aq0jywmtWtmRv2qol3m8V-e6kPQVmdGto7J0TDECTx6NbGtSJNfvmFleWA-MMpbpe-CIj4tFp1LRi45lb_bhFFr_e_zto5ZTwUl8UBD4tpbQIQFAimUSe_59i2PJ4seJBIYOQ6sOQIrH00PQ4YxKAT4HT7uPEiZw6FfewwZC00ZBDpfOuMFtf1RKbn8-4dE-gAgCLWvLC9gHpNnxIopGV8GkCOWcwIuI4Veo5r0Jvtmn42mFfjDzhMnUpPoa-PfnTDPlzoZzaD5eNFiQt560ZAHTEyhkuhoCn4tgOjMIXbsUs_BHeHwYkiZbILPBEEOKA3vPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان اویس‌قَرَن، پژوهشگر ایرانی علوم رایانه و استاد دانشگاه واشینگتن، مدال آباکوس سال ۲۰۲۶ اتحادیه بین‌المللی ریاضیات را دریافت کرده است؛ جایزه‌ای که به دستاوردهای برجسته پژوهشگران جوان در بخش‌های ریاضی علوم رایانه تعلق می‌گیرد.
کمیته این جایزه می‌گوید اویس‌قرن با وارد کردن ابزارهایی از شاخه‌هایی چون هندسه چندجمله‌ای‌ها، نظریه احتمال و نظریه طیفی گراف‌ها، شیوه تحلیل الگوریتم‌ها را گسترش داده و برای حل چند مسئله قدیمی علوم رایانه راه‌های تازه‌ای گشوده است.
پژوهش‌های او به‌ویژه در دو زمینه مورد توجه قرار گرفته‌اند: یافتن مسیرهای نزدیک به بهینه و نمونه‌گیری تصادفی از مجموعه‌های بسیار بزرگ و پیچیده.
مدال آباکوس هر چهار سال یک‌بار اهدا می‌شود و ادامه جایزه‌ای است که تا سال ۲۰۱۸ به نام رولف نوانلینا شناخته می‌شد. نامزد دریافت آن باید در آغاز سال برگزاری کنگره جهانی ریاضی‌دانان هنوز به ۴۰ سالگی نرسیده باشد. این جایزه از مهم‌ترین افتخارات بین‌المللی در علوم رایانه نظری به شمار می‌رود.
اما اهمیت کار اویس‌قرن تنها با فهرست کردن اصطلاح‌های تخصصی روشن نمی‌شود. بخش مهمی از مسیر علمی او به یکی از مشهورترین پرسش‌های علوم رایانه بازمی‌گردد: چگونه می‌توان کوتاه‌ترین مسیر ممکن را برای سفر میان چندین شهر پیدا کرد و در پایان به نقطه آغاز بازگشت؟
این پرسش که «مسئله فروشنده دوره‌گرد» نام دارد، در ظاهر ساده است. یک فروشنده، راننده یا مأمور توزیع باید از چند شهر یا مقصد عبور کند، هر کدام را یک بار ببیند و به نقطه نخست بازگردد. با افزایش شمار مقصدها، تعداد مسیرهای ممکن چنان سریع زیاد می‌شود که بررسی همه آنها عملاً ممکن نیست.
در چنین مواردی، پژوهشگران به جای یافتن پاسخ دقیق، الگوریتمی می‌خواهند که در مدت معقول مسیری نزدیک به بهترین مسیر را پیدا کند و بتوان تضمین کرد که نتیجه آن از حد معینی بدتر نخواهد بود.
...
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77505" target="_blank">📅 16:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6B3FeTPGgGaRpGfe_Q2Qod1K0GNn3n5F_hetTaTypQeiwfGZFd3aM0pwehMs4_0Tu0Ppla5cPY5J95ipSlrLpUbF6ECTJ4OaCUiBpFNEe7ezCbYfkNp6yb8V_A8vLEQp5A-Br11p1xE7rHuy3Pv5hT9dm1jAD-H4YhTGYBiY2Yj_tyXWNzQ-ju2vr5S_it_Moym7b7ltwtWc-9vd948CTU_9mrYgMFm6s3KX6R3K8c0uFsw4-Og6LcdZZ15rME2sTM2rYmDs2yWe4txf3vP6AOU56EGzWeMuIxD3p-yfRnZprumZHdHZIHSeBwC-6u9wVQxpL6U6BAmHQUrISiiKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید
گزارش نیویورک‌تایمز
درباره کنارگذاشتن طرح تشدید عملیات نظامی علیه جمهوری اسلامی را رد کرد.
استیون چانگ، مدیر ارتباطات کاخ سفید گفت دونالد ترامپ، رئیس‌جمهوری آمریکا، همواره گفته است راه‌حل دیپلماتیک را ترجیح می‌دهد، اما اگر جمهوری اسلامی به اقدامات تروریستی در تنگه هرمز یا علیه متحدان ادامه دهد، همه گزینه‌ها را حفظ می‌کند.
چانگ افزود پس از تحریم‌هایی که اقتصاد جمهوری اسلامی را فلج کرده و سیزده روز پیاپی حمله به اهداف نظامی، عاقلانه است که این حکومت به سمت توافق حرکت کند. او گفت در غیر این صورت، طرف مقابل می‌داند چه اتفاقی خواهد افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77504" target="_blank">📅 16:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77503">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s3PGDq5HIY5nG5JXeGPLgGnRstdvShboArCE49CqH4-yPA1qm7r8AyPiOcusEa2-dWR1Z0roI7-DlNzt6iEMaqjGYTpvKKh6okA9MOVz_uX1jQKFCrqDU_Kshb9o2gmAWSvV6q8dRyIhCxlvFV-oOfMT3dmihvVis8DSMha9FsgWq13b_WcKRUVmm0iRxCHx0JZJyMWZdbrFKnKZAnmv2UIWW-mB7xsQhV2117v61OjukYer5ePRy7Nx24cNNn5bouVM0X1h15zsGsEY_joX3zYtoDwVmn_TrTbE4LsNGYbOD9iNAXcmgWKBm_YKaJlPFrSsTagW4w1REESmr4A28w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، روز یک‌شنبه چهارم مرداد بدون اشاره به جزئیات از «پیشرفت‌هایی» در مذاکرات و تبادل نظر تهران و مسقط خبر داد.
این مقام جمهوری اسلامی پس از آن در این باره اظهار نظر کرده است که یک هیئت عمانی که برای گفت‌وگو درباره مدیریت تنگه هرمز به تهران آمده بود شنبه عصر ایران را ترک کرد.
بقایی درباره این مذاکرات این طور توضیح داد: «روزهای جمعه و شنبه چند دور گفت‌وگو بین ایران و عمان در سطح معاونان وزرای امور خارجه در تهران برگزار شد که طی آن دو طرف در مورد اصول مشترک و سازوکارهای عملیاتی برای مدیریت تردد ایمن کشتیرانی در تنگه هرمز با رعایت حقوق حاکمیتی دو دولت ساحلی تبادل نظر کردند.»
مقام وزارت خارجه در ادامه اضافه کرده است که «در حال حاضر تغییری در وضعیت تردد در تنگه ایجاد نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77503" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77502">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uehjNRBrBctF-PlaXOn1txRA3VrNa_zy7QJsgd0LqPFSV-xZf-I0eoJt8xGfaMWm5SMk8E-DSc3eStKYTvokB4G3sxTpZzd6BgEuv3ktHMmc5ZaxjiAh_1I6HhFMBvxsOYno9vmiGlmFFY8GrXS86TRcLJ1jGP3AalxhgGJ-vjQ_5pcymqD5mIvgUlzYzcMjUWy0VBkw94KW6i8s134ebddacOdXUD4NT_NyP1q7qACG1__FYtjqi_hmQNLdhAYfVvvjZGwQ6ovPNZtUBiqa41xmB_4Eh85YveXkb0tC4rul3q3nCSt0wXEyu5HZ7OsnsHK3QeTkSnc7uZDcC1MOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردی که سال گذشته دختر ۱۷ ساله خود به نام فاطمه سلطانی را مقابل آرایشگاه محل کارش در اسلامشهر با ضربات چاقو به
#قتل
رسانده بود، با حکم دادگاه کیفری تهران به هشت سال حبس و پرداخت دیه محکوم شد.
در قوانین جمهوری اسلامی ایران، مقرراتی وجود دارد که پدرانی را که مرتکب قتل فرزند خود می‌شوند، از مجازات‌های سنگین معاف می‌کند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77502" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77501">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MmyM2zZst5xzicUvNGV0WHV83PYlYKhpV7T-n0LqrYwm06BbjiXAKgKxA4MAEGsBHUrYPjHvzlsugAVhc213IdbibwnWLpwMJT6LBYlQaOWELyO4uxFZ1AtXXy6NmTOLUv1y1McYUlVlrVx7GGtyyNuy5rZJ_sR2btf7FlG7vTyd2JLYRKgPYaqIfNDdjXZIsFCSqGFjh6DZyWB6-kN70KIOUQt8YB3evr2-EoiRQqGzH8B9wYPyzUBPI3V9NISemUnK98vL7b1jq7t3s314hw9ORu6skdVFQTXeP15ROiADml62v6Cj5vSTkKT7u6Rx_UcWKyLcnNoHn1ZXvtsQCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: منابع می‌گویند ونس و کین درباره تشدید جنگ در ایران ابراز نگرانی کردند
ترجمه ماشین:
یک منبع آگاه از موضوع و یک مقام آمریکایی به سی‌ان‌ان گفتند که در حالی که دونالد ترامپ، رئیس‌جمهوری آمریکا، در نشست روز جمعه کاخ سفید احتمال تشدید جنگ در ایران را بررسی می‌کرد، جی‌دی ونس، معاون رئیس‌جمهوری، و ژنرال دن کین، رئیس ستاد مشترک نیروهای مسلح آمریکا، هر دو درباره این اقدام ابراز نگرانی کردند.
جمعه‌شب، پس از نزدیک به دو هفته حملات هوایی پیاپی شبانه، به نظر می‌رسید آمریکا کارزار بمباران ایران را متوقف کرده است. یک منبع در وزارت دفاع آمریکا روز شنبه به سی‌ان‌ان گفت: «عملیات فعلاً متوقف شده است.»
به گفته منابع، کین روز جمعه به‌طور مشخص درباره ذخایر مهمات آمریکا و دیگر پیامدهای منفی احتمالی ابراز نگرانی کرد. یکی از منابع گفت کین به ترامپ اعلام کرد که ارتش آمریکا می‌تواند گزینه‌های پیش روی او را اجرا کند و موفق شود، اما سپس درباره پیامدهای احتمالی آن هشدار داد.
هر دو منبع گفتند نگرانی درباره ذخایر مهمات، یکی از چندین نگرانی مطرح‌شده با ترامپ در این نشست بود. در حال حاضر مشخص نیست که آیا این نگرانی یا هشدار درباره تشدید جنگ، دلایل اصلی توقف حملات پیاپی شبانه آمریکا بوده‌اند یا اینکه این توقف ادامه خواهد یافت.
استیون چونگ، مدیر ارتباطات کاخ سفید، گفت: «با توجه به تحریم‌های موفقی که اقتصاد ایران را فلج کرده و ۱۳ روز پیاپی حمله به اهداف نظامی در پاسخ به تجاوزهای مکرر این کشور، عاقلانه است که ایران برای دستیابی به توافقی از طریق مذاکره تلاش کند. در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/77501" target="_blank">📅 06:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77500">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G7TZtIXwfg8YlvCNPOfz-Hftajw0vEjmQFNazP3HlyZIGaG6tzT7u_hrNls_GunTNndsUoeu51TwKFvjcKAq0JyplT3sudm-oeM5qNLWHGglF4Wlerjqt7Z-GaATWEdR9SUVF-X78RB_1QV3Sg_wxPgnl40LFc3PDWtWuGe9lEWEEnFxHHHrRKmfuFXWA-RfCXHe776LzVGE2W6dAffCRQjnWiN7PifTKwZXxXd3J6eW6LPqISNUwhZJ-EqbAu1zhe5y7CrlGo2EQxzXdTmUuvT8TcI8UWkCwk_aHdAD1-ryJjBhUZi_9ZjDtM0x6nh071zg0RI1DkdmAsREspajdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز:
ترامپ در پی ابراز نگرانی مشاوران، فعلاً از تشدید گسترده حملات علیه ایران خودداری کرد
یکی از نگرانی‌ها این است که گسترش درگیری‌ها ممکن است ذخایر کاهش‌یافته مهمات پدافند هوایی در خاورمیانه را به‌طرز خطرناکی تحلیل ببرد.
ترجمه ماشین:
رئیس‌جمهوری ترامپ، دست‌کم فعلاً، برنامه‌های تشدید شدید حمله نظامی آمریکا علیه ایران را کنار گذاشته است؛ به‌ویژه به این دلیل که نگران است تشدید جنگ، ذخایر از پیش کاهش‌یافته پنتاگون از موشک‌های رهگیر ضدبالستیک پاتریوت و دیگر مهمات پدافند هوایی در خاورمیانه را به‌طرز خطرناکی تحلیل ببرد.
به گفته مقام‌های دولت، تهدید متوجه ذخایر موشک‌های رهگیر یکی از ملاحظات متعددی است که بازگشت به عملیات رزمی گسترده را به اقدامی بسیار پرخطر تبدیل کرده است. آقای ترامپ و دستیاران ارشدش همچنین از احتمال گسترش جنگ در خاورمیانه، دور شدن متحدان کلیدی در خلیج فارس که در برابر حملات ایران آسیب‌پذیرند، فشار اقتصادی جهانی و تشدید بحران‌های انرژی و پناه‌جویان نگران‌اند.
به گفته دو نفری که در جریان این گفت‌وگو قرار گرفته‌اند، تازه‌ترین چرخش در نحوه مدیریت مناقشه با ایران از سوی آقای ترامپ پس از جلسه‌ای در روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه او رخ داد.
به گفته این مقام‌ها که برای گفت‌وگو درباره مسائل عملیاتی خواستند نامشان فاش نشود، رایزنی‌های محرمانه بر کاهش ذخایر موشک‌های رهگیر پاتریوت و دیگر سامانه‌های پدافند هوایی پنتاگون متمرکز بوده است. یک مقام ارشد آمریکایی گفت جمعه گذشته، هنگامی که یک موشک بالستیک از پدافند هوایی آمریکا ــ که در حال مقابله با موجی از موشک‌ها و پهپادهای ایرانی بود ــ عبور کرد، سه سرباز آمریکایی در اردن کشته شدند.
به گفته این مقام‌ها، ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، در محافل خصوصی هشدار داده است که ازسرگیری عملیات رزمی گسترده علیه ایران امکان‌پذیر است، اما ذخایر موشک‌های رهگیر در دسترس فرماندهی مرکزی ارتش آمریکا را ــ که مسئول عملیات در خاورمیانه است ــ به‌طرز خطرناکی کاهش خواهد داد. سخنگوی ژنرال کین از اظهارنظر درباره توصیه‌هایی که او به رئیس‌جمهوری ارائه می‌کند خودداری کرد.
استیون چونگ، مدیر ارتباطات کاخ سفید، گفت رئیس‌جمهوری «همواره به‌طور ثابت گفته است که راه‌حل دیپلماتیک را ترجیح می‌دهد، اما اگر ایران به فعالیت‌های تروریستی در تنگه هرمز یا علیه متحدان ادامه دهد، همچنان همه گزینه‌ها را روی میز نگه می‌دارد.» او افزود پس از تحمل تحریم‌های فلج‌کننده و حملات مکرر، «عاقلانه است که ایران برای دستیابی به یک توافق مذاکره‌شده تلاش کند؛ در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
آقای ترامپ درگیر این بوده است که در جنگ نزدیک به پنج‌ماهه خود علیه ایران چگونه پیش برود و به‌طور مشخص چگونه تنگه هرمز را دوباره باز کند؛ آن هم در شرایطی که با ازسرگیری درگیری‌ها در دو هفته گذشته، قیمت بنزین بار دیگر در حال افزایش است. دیپلماسی شکست خورده و به نظر نمی‌رسد تازه‌ترین دور حملات گسترده آمریکا توانسته باشد ایران را از لحاظ نظامی بازدارد.
به گفته آن دو نفری که در جریان گفت‌وگوها قرار گرفته‌اند، در حلقه نزدیکان آقای ترامپ، افراد بسیار کمی ــ و شاید هیچ‌کس ــ معتقد بودند طرح تشدید درگیری عاقلانه است. یک مقام ارشد آمریکایی دیگر که او نیز به شرط ناشناس ماندن صحبت کرد، درباره اینکه ازسرگیری عملیات رزمی گسترده بتواند ایران را به میز مذاکره بازگرداند، ابراز تردید کرد.
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77500" target="_blank">📅 03:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77499">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a2f96f5fb8.mp4?token=PEPkoD2etqTGCDke9nFEt8w1VuDm09ea4P857bv4eUBcbbD_RVCVWpAJT4ct6oW3tI1cq5orsX2mmGwNQfdlv9rK6qwMIbAl0R6Ie4y1ebFXfR20pq_brkQjUz1bQ0-asP1LGO-Nu4cqjHbxzpE5_fbZ2Isu7kym2Cph4Q7IxvuFitzVgRuRhHwWs5NvU13ArKHRA9UYzCmuRlmQU7GIgji6LXheGCycZK8fi2EM2PVOKuSoLW7T-lunBtsjt7LeI5VfBN6HCUiF77chOFP3_VrXR6NHvknrQlUUfYEZcikdwuCfiaaczAAZwYGxr77GDfRt1x49yaczbT9_vhW6rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a2f96f5fb8.mp4?token=PEPkoD2etqTGCDke9nFEt8w1VuDm09ea4P857bv4eUBcbbD_RVCVWpAJT4ct6oW3tI1cq5orsX2mmGwNQfdlv9rK6qwMIbAl0R6Ie4y1ebFXfR20pq_brkQjUz1bQ0-asP1LGO-Nu4cqjHbxzpE5_fbZ2Isu7kym2Cph4Q7IxvuFitzVgRuRhHwWs5NvU13ArKHRA9UYzCmuRlmQU7GIgji6LXheGCycZK8fi2EM2PVOKuSoLW7T-lunBtsjt7LeI5VfBN6HCUiF77chOFP3_VrXR6NHvknrQlUUfYEZcikdwuCfiaaczAAZwYGxr77GDfRt1x49yaczbT9_vhW6rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین: 00:32
محاصره دریایی آمریکا علیه ایران همچنان به‌طور کامل برقرار است. تا ۲۵ ژوئیه، سنتکام مسیر ۱۲ کشتی تجاری را که قصد شکستن محاصره داشتند تغییر داده، ۲ کشتی را که از دستورات تبعیت نکردند از کار انداخته و برای اطمینان از تبعیت کامل، وارد ۲ کشتی شده است.
صبح امروز، نیروهای آمریکایی عملیات ورود و بازرسی برای راستی‌آزمایی را در نفتکش M/T Charminar با پرچم کومور، در دریای عرب، به پایان رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام روز ۲۴ ژوئیه، نفتکش M/T Lavine با پرچم موزامبیک را در دریای عمان از کار انداختند؛ پس از آنکه خدمه آن چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به‌سوی ایران در حرکت نیست.
نیروهای آمریکایی
🇺🇸
همچنان کاملاً هوشیار، متمرکز، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/77499" target="_blank">📅 01:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77498">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_VtOMXd8mrHlu74uJIPxhO7jvAgqNW8mXpZT86vrGL_RKdlPk4ZpJa9guAxzf9HYqEMGMe2BZUC7OQFYTY6xMAcqExhZGgNXEJGndlogJZc50HIALVWnW0-GoEN5i3verG8pxwYbPw4uKG1ueX9-YBU-2W-aEnnGVTPToZKcnDHhKKOGD3oI2bIOxGh83UM47z1O81aTdw0O4OWK55c1qs96Nm-VbR_QTf5CJqNGKbyUMt7m1gqZWJXD8sj_Yg0WJOlcjM7RH0IkTLKY8t7cIqNxQFjRTXDc_NIn8KVfH5yoyElVIMv4bmjqZg6jE2GEURBeUxkKrOaQJdLlzQz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه هشدار داد که اگر دولتش به چیزی که در مذاکرات با ایران می‌خواهد نرسد، قطعا حملات گسترده به این کشور را از سرمی‌گیرد.
خبرنگار شبکه فرانسوی ال‌سی‌آی در شبکه ایکس نوشت که در گفت‌وگوی تلفنی با ترامپ از او سوال کرده که آیا در حال بررسی ازسرگیری یک جنگ گسترده علیه ایران است یا نه.
رئیس‌جمهور ایالات متحده در پاسخ گفته است: «اگر به صد درصد آنچه می‌خواهیم نرسیم، قطعاً.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/77498" target="_blank">📅 23:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77497">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PoGfd0NvrSp-fP7w5KaL_qKEg7ktoFfqBWcXMUhn2SCs1CKnoSgRamyzCwCMr5QPEHLq4-ytV8JMIxQoXL1sidaSDbHKromQnVieCQnDM-1dMINrvcYiMaaJE6b5x7i7_fpbfV9HsGrevKQtBKdDOwpRHVKDAT10DjbktecIU5e6HO-TLLTBdpPMqsOw7iptxU12FMSDMS5DAZGoTCsZKnHVgm9FQBJqrV_Rsal7pItfYKKfQgfPjE1iFTO3sSBmhINImHYac-QMBMGMADwUkidhX_VRMNyWY5eOsThmeqNrT_59jn5WkMjhxR_x93aO5fSwxnfqE9ZaMek8RKY7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.  زلنسکی روز شنبه، سوم مرداد، در پیامی در…</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/77497" target="_blank">📅 22:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77496">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1bueSmX64pCyP0RSqYap5HD1N-JpDKq0GWxIIrKsdWFZSjYcXQjOq_EWy2HXsPD3vALf-n9SscyCHghBIpHAmN9BfxbRBURJEQBXhqjIOyPu-BCtKQzd50ezpkav8Xqj5hxoNrgdYdgCIgjH6pUhi2hnzpQ1h5qyoGfdQ81EPt6TMQPupl2ghAjeOis_eWpA6G6glm5zJDtn6VBESFVXqA7wcn2VLxreCd0k8gB7dY_Zs49VHZOEH7TQnACMj8f_g2AbqmUAH_ZU6Zh9VxnhIakUbT7OWlx_8avJGDwdOu0TQSaGcNqlhS72Nlod6Pyl6EXMwAXm1CCO0dfZW_Ocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی پری، خواننده آمریکایی، از استفاده کاخ سفید از آهنگ «Firework» (آتش‌بازی) در ویدیویی از حمله آمریکا به اهدافی در ایران انتقاد کرد و گفت این استفاده بدون اطلاع و رضایت او انجام شده است. او افزود که از این اقدام عمیقا شوکه و خشمگین شده است.
کاخ سفید روز پنج‌شنبه ویدیویی در حساب رسمی خود در تیک‌تاک منتشر کرد که در آن بخش «boom, boom, boom» آهنگ «Firework» با تصاویری از حملات آمریکا به اهدافی در جنوب ایران هم‌زمان شده است. کاخ سفید در توضیح این ویدیو نوشت: «به ایران هشدار داده شده است.»
کیتی پری روز شنبه در شبکه ایکس نوشت: «از اینکه آهنگ "Firework" به‌عنوان موسیقی پس‌زمینه ویدیوی حملات نظامی در حساب کاربری تیک‌تاک کاخ سفید استفاده شده، عمیقا شوکه و خشمگین هستم. من این استفاده را تایید نکردم، از من اجازه‌ای خواسته نشد و به هیچ وجه آن را تایید یا حمایت نمی‌کنم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77496" target="_blank">📅 22:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77495">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JYvfHQXgv9TX2d64uEWpbbCxUk2UYH8R_UvLOOT58Is42MA2A-8Nu9goGt8kqP7KfcXWzCrWU1shIFGrONR61GPSAnSzg22oHfRJTQsCJmNnU52DATaGmfkrQHYc_tSWwn634VQXjMeZdbRQl4htwyNeE1_F1nTitBv1LeK4HvGpjTDLu9avQEYOe-nWvQ_BsgZdzGM5yoa4O_wcQUzaOyr06UZUnZGN09meNGMkxyOBy30TuzLu_wam7Nmk2mYLXSzjujUQSHzwE-gO0YXYjZHfNORKbdFcOStiN_tOQGNVNAPpwEY_ZfjfDztC-ILscgpOa5qCPTQfpOlUaGaa_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: ترامپ دستور داد ارتش روز جمعه در ایران حمله‌ای انجام ندهد
ترجمه ماشین:
دو منبع مطلع از این تصمیم گفتند دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه به ارتش این کشور دستور داد حملات جدیدی در ایران انجام ندهد؛ دستوری که به رشته‌ای نزدیک به دو هفته از حملات روزانه پایان داد.
چرا مهم است:
دستور رئیس‌جمهوری پس از آن صادر شد که او طی ۱۳ روز گذشته، هر روز حملات را تأیید کرده بود. هنوز مشخص نیست که دستور روز جمعه ترامپ تصمیمی یک‌باره بوده یا این وقفه ادامه خواهد یافت.
▪️
تصمیم ترامپ هم نشان‌دهنده تمایل او به فراهم‌کردن فضای بیشتر برای دیپلماسی است و هم حاکی از این ارزیابی که سطح کنونی حملات آمریکا ــ مگر با بازگشت به عملیات رزمی گسترده ــ به مرز اثربخشی خود رسیده است.
▪️
اگر ترامپ دستور ازسرگیری حملات را صادر کند، ارتش آمریکا می‌تواند در مدت نسبتاً کوتاهی برای انجام آن‌ها آماده شود.
▪️
به گفته منابع، ارتش آمریکا همچنان در حال تهیه طرح‌هایی برای بازگشت احتمالی به عملیات رزمی گسترده است، اما ترامپ هنوز دستوری برای حرکت در این مسیر صادر نکرده است.
▪️
کاخ سفید به درخواست اظهارنظر پاسخ نداد.
آنچه خبر را رقم زد: ترامپ طی دو هفته گذشته، هر بعدازظهر طرح‌های حمله ارائه‌شده از سوی ارتش را تأیید کرده و این حملات ظرف چند ساعت اجرا شده‌اند.
▪️
روز جمعه نیز طرح مشابهی در اختیار ترامپ قرار گرفت، اما او با آن موافقت نکرد. در عوض، به گفته منابع، به ارتش دستور داد حمله‌ای انجام ندهد.
▪️
اندکی پس از صدور این دستور در روز جمعه، ترامپ به خبرنگاران در کاخ سفید گفت که می‌تواند حملات را ادامه دهد یا حتی آن‌ها را تشدید کند؛ از جمله با «نابود کردن هرچه آن‌ها دارند».
▪️
اما او روشن کرد که به نظرش «راهبرد هوشمندانه‌تر» این است که با ایران «به توافق برسد».
▪️
ترامپ گفت: «همین حالا با [ایرانی‌ها] در حال گفت‌وگو هستیم. فکر می‌کنم با گذشت هر روز، جدی‌تر و جدی‌تر می‌شوند. ما کاملاً مسلح و آماده‌ایم، اما در حال گفت‌وگو با آن‌ها هستیم.»
▪️
ترامپ بعدتر در روز جمعه، در سخنانش در شام انجمن خبرنگاران کاخ سفید، گفت تصور نمی‌کند ایران در حال حاضر آماده توافق باشد، «اما من آماده‌ام گوش کنم».
وضعیت کنونی:
دستور ترامپ برای توقف حملات، چند ساعت پس از آن صادر شد که یک هیئت عمانی روز جمعه برای گفت‌وگو درباره ترتیبات جدیدی به‌منظور بازگشایی تنگه هرمز وارد تهران شد.
▪️
دو منبع منطقه‌ای مطلع از مذاکرات گفتند در گفت‌وگوها پیشرفت حاصل شده و ممکن است توافقی میان عمان و ایران در تعطیلات آخر هفته به دست آید.
▪️
پس از آن، رئیس‌جمهوری ترامپ باید تصمیم بگیرد که آیا توافق پیشنهادی را می‌پذیرد یا نه.
axios
:باراک راوید
تصمیم ترامپ هم نشان‌دهنده تمایل او به دادن فرصت بیشتر به دیپلماسی است و هم حاکی از این درک که — مگر با بازگشت به عملیات رزمی گسترده — سطح کنونی حملات آمریکا به نهایت اثربخشی خود رسیده است.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77495" target="_blank">📅 20:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77494">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/136e1a65b9.mp4?token=G_DS4ZUt5DjtrRCeg6veSpCYxKEqQ4Tb8LenA3q2GBwKVJvkLicYdWSDjKYGx1CI62_nlNBwJyvBJ1mLMoiTFReGxiNUCH8cxL0sXasgNSdp4Smca-KNQHv472JaEMdoxTShtoQEWJvIhn-b_DThhIkFJv9Qbk3XkhTiSXC_Wa01xy5pJLAfKpKD-33azQ7RYX18NyILuKh39z0fvgyMHEbTU2PK4sY1L2ImNqlsPLkqNUtBDazm7Wtolt5GxSxpov4EWwiGrv1tcw0swCaBLpsURRbx0wpOp00RgTNohfnwm0XXrQUCbIWQgCMHcyoSo0LryOVSaKY6kIYhutgY-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/136e1a65b9.mp4?token=G_DS4ZUt5DjtrRCeg6veSpCYxKEqQ4Tb8LenA3q2GBwKVJvkLicYdWSDjKYGx1CI62_nlNBwJyvBJ1mLMoiTFReGxiNUCH8cxL0sXasgNSdp4Smca-KNQHv472JaEMdoxTShtoQEWJvIhn-b_DThhIkFJv9Qbk3XkhTiSXC_Wa01xy5pJLAfKpKD-33azQ7RYX18NyILuKh39z0fvgyMHEbTU2PK4sY1L2ImNqlsPLkqNUtBDazm7Wtolt5GxSxpov4EWwiGrv1tcw0swCaBLpsURRbx0wpOp00RgTNohfnwm0XXrQUCbIWQgCMHcyoSo0LryOVSaKY6kIYhutgY-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت: تغییر در قیمت یا سهمیه بنزین قطعی است
سخنگوی دولت مسعود پزشکیان اعلام کرد که تغییر در قیمت یا سهمیه بنزین قطعی است و دولت برای مدیریت مصرف این سوخت ناچار به اتخاذ راهکارهای جدید خواهد بود.
فاطمه مهاجرانی گفت دولت همچنان برای بنزین یارانه پرداخت می‌کند، اما با توجه به ضرورت ایجاد تعادل در مصرف، تصمیم‌گیری درباره نحوه عرضه این سوخت اجتناب‌ناپذیر است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77494" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77493">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B86ukP7l0JHLd1mekd7HZi5kmBNmBrRZlZunPjsRVCbjJ0fQvOgOkB2cllwApzhOWCobPJGhbEKY42zTLqYiS7kPK57i8bon7OKz8MHddfCZ31PtrqStJe8nYYCPSJNk_0cawi0mNqoD196uzfr2K2vHyRinPFlGQ0PfIetM44B4_Zw3x84cXyIyaaC74_KsbFLS63SKKpSLj9lkXqtkg_4L9FI2q0nYfvccDvsPwpLMNZ9DaWkO2oYz8FMZObaZ803d8vXH40EXBTZLyiw4bmqqqfVIIeTP8IFzj15RjVecYhWz0KxKrGM2lPtwhE1aDfb_VSbNm4TelItEki5r6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت خبری وای‌نت گزارش داد مقام‌های اسرائیلی برآورد کرده بودند حمله گسترده آمریکا به ایران، که دونالد ترامپ، رییس‌جمهوری آمریکا، گفته بود در حال بررسی آن است، شب جمعه تا بامداد شنبه آغاز شود، اما با پایان روز جمعه به این نتیجه رسیدند که ترامپ فعلا حمله را متوقف کرده و فرصت دیگری به تهران داده است.
بر اساس این گزارش، در پشت صحنه، قطر و عمان فشار قابل‌توجهی بر جمهوری اسلامی وارد کردند تا مواضع خود را نرم‌تر کند و از وقوع آنچه یک عملیات گسترده و تقریبا قطعی آمریکا به نظر می‌رسید، جلوگیری شود.
این گزارش افزود مقام‌های اسرائیلی همچنان معتقدند تفاهم میان تهران و واشینگتن عملا از بین رفته و احتمال دستیابی به توافقی دائمی که حکومت ایران را وادار به پذیرش خواسته‌های آمریکا کند، نزدیک به صفر است.
بر اساس این گزارش، از نگاه اسرائیل، فرصت تازه‌ای که ترامپ در اختیار تهران قرار داده، تنها به جمهوری اسلامی امکان می‌دهد برای مدت کوتاهی زمان بخرد و تغییری در ارزیابی کلی اسرائیل ایجاد نمی‌کند.
@
VahidOOnLine
🔄
باراک راوید:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشدند، بلکه برای حمله‌ای دقیقاً هم‌اندازه حملاتی آماده شدند که طی دو هفته گذشته هر شب انجام می‌شد.
BarakRavid
رسانه‌های جمهوری اسلامی درباره این توییت نوشتند اکسیوس خبر «رسانه‌های عبری» رو رد کرد ولی باراک راوید خودش هم اسرائیلیه و علاوه بر اکسیوس خبرنگار واشنگتن شبکه ۱۲ اسرائیله.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77493" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77492">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSRihX5JtiqA62VcWuY7fe8DVjUbMBZJiLMrL3zVldGvoz-WHKhIx6M86BaerGkiowEavIDrUcsgQhdleYs9MOtVxtnfWvfl9pnWq0EIYtRPOGICiZGbLV0c61Sfi9U4-WkJBC5-5zWL2LuYGQofMUuZoktY6fTdoVKpX5Pe_GuaHF2B01u2SOLIxakvFkB8rQTL4t3ATFH5FoxrsG1yeJljKaQX9aUYjPaEdOckpqwztuCaw5qE68ndYyXGMVI7W5SWavt8chtQ4s9d6VHS8fQdUJraBnan8Yh9FqWIqq6Nx3RzQ4CFLG9G1cubIwBsPRp8P4x-xStlwUx09u5ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.
زلنسکی روز شنبه، سوم مرداد، در پیامی در شبکه ایکس نوشت که اوکراین در حملات دوربرد شب گذشته در دریای خزر به نتایجی «بسیار خوب» رسیده است. به گفته او، در میان اهداف این عملیات، کشتی‌هایی نیز بوده‌اند که «با مشارکت ایران» برای انتقال محموله‌های نظامی استفاده می‌شدند. رییس‌جمهور اوکراین اطلاعات دقیق‌تری درباره هویت ناو جنگی یا کشتی‌های هدف قرارگرفته منتشر نکرد.
سرویس امنیتی اوکراین (اس‌بی‌یو) نیز همان روز گزارش داد پهپادهای اوکراینی سکوی نفتی «فیلانوفسکی»، متعلق به شرکت روسی لوک‌اویل واقع در دریای خزر، را هدف گرفته‌اند. بر اساس اعلام این نهاد، دو کشتی باری با نام‌های «پورت اولیا ۲» و «بگی» نیز در همین عملیات مورد اصابت قرار گرفتند؛ کشتی‌هایی که به گفته سرویس امنیتی اوکراین در انتقال محموله‌های نظامی میان روسیه و ایران نقش داشته‌اند.
تا کنون نه مسکو و نه تهران واکنشی به این ادعاها نشان نداده‌اند و گزارش‌های اوکراین نیز به صورت مستقل تایید نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77492" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77491">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0ae743c97.mp4?token=JCCqqi7P0l2l1ccmIcm6QdA82v5RUa9zw8nouESFLJHuoO22H97BO301k0HcRJ7o99efPQa7IwJY_WKZZxYwJUjmsj7TDB5C6wlspAp4em4XKOskDuys5r0vMX9GrHegQhnXzV_SO1PjOlTQ-EfO6jeioqQxxDlThoSF8Bkp_UsTsUOafJnlBJa4xv-LLJAw-UV0Kdq60Ktx1fCkumjEtudlYlGuMZDGlbQc0IxlRdX0wnmoXM6nD6FJaedwPK7jjkuMra3jEHhSqk8hi1lV7hyO1s4odwv65ArMCJWMioGtkTK6D9jXOVUnweirqgjDVk8--3y3tuYMJ7IFOhP_wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0ae743c97.mp4?token=JCCqqi7P0l2l1ccmIcm6QdA82v5RUa9zw8nouESFLJHuoO22H97BO301k0HcRJ7o99efPQa7IwJY_WKZZxYwJUjmsj7TDB5C6wlspAp4em4XKOskDuys5r0vMX9GrHegQhnXzV_SO1PjOlTQ-EfO6jeioqQxxDlThoSF8Bkp_UsTsUOafJnlBJa4xv-LLJAw-UV0Kdq60Ktx1fCkumjEtudlYlGuMZDGlbQc0IxlRdX0wnmoXM6nD6FJaedwPK7jjkuMra3jEHhSqk8hi1lV7hyO1s4odwv65ArMCJWMioGtkTK6D9jXOVUnweirqgjDVk8--3y3tuYMJ7IFOhP_wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ در مراسم شام انجمن خبرنگاران کاخ سفید، بخش‌هایی مربوط به ایران، ترجمه ماشین:
... آن‌ها پرسیدند: «می‌مانی؟»
گفتم: «بله، می‌مانم. یعنی، فکر کنم بمانم.»
اصلاً چه کار دیگری دارم که بکنم؟ ایران را دارم؛ این را دارم، آن را دارم. همهٔ این‌ها هم فوق‌العاده خوب پیش می‌رود. اخبار جعلی را باور نکنید.
پیش‌تر داشتیم صحبت می‌کردیم. گفتم: «ما ایران را به‌شدت هدف قرار داده‌ایم. نیروی دریایی‌شان از بین رفته؛ نیروی هوایی‌شان هم از بین رفته است. ۲۵۰ جنگنده دیگر وجود ندارند. ۱۵۹ قایق؛ قایق‌های خوبی بودند.
در واقع گفتم: چرا آن‌ها را برای خودمان نگه نداشتیم؟ می‌توانستیم از آن‌ها استفاده کنیم. اما هر ۱۵۹ قایق در ته دریا هستند.
آن‌ها هیچ راداری ندارند. برخلاف آنچه می‌بینید، پهپادهای بسیار کمی برایشان باقی مانده است. هر از گاهی چیزهایی را به نمایش می‌گذارند، اما چیز زیادی برایشان باقی نمانده است.
ضمناً همین حالا با ما در حال گفت‌وگو هستند. آن‌ها خیلی دوست دارند توافقی انجام دهند. فکر نمی‌کنم هنوز آماده‌اش باشند. فکر نمی‌کنم هنوز وقتش رسیده باشد، اما حاضرم گوش کنم.
ولی آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. نمی‌خواهیم واشینگتن دی‌سی، هیچ‌یک از شهرهایمان، اسرائیل یا، صادقانه بگویم، خاورمیانه با یک سلاح هسته‌ای نابود شود؛ چون من قدرت سلاح‌های هسته‌ای را می‌دانم. آن را می‌بینم؛ اجازه دارم آن را ببینم. نخواهیم گذاشت چنین اتفاقی بیفتد.
بنابراین، همهٔ این ماجرا دربارهٔ این است که نخواهیم گذاشت آن‌ها سلاح هسته‌ای داشته باشند.»
[تشویق حضار]
«و اگر آن را داشتند، از آن استفاده می‌کردند. اگر داشتند، استفاده می‌کردند.»
---
ما دستاوردهای بسیار فراوانی داریم که رسانه‌ها هیچ‌وقت درباره‌شان حرف نمی‌زنند.
برای مثال، در دولت من، رژیمی قدرتمند که زمانی هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شده است. رهبران سابقش برکنار شده‌اند و اکنون دیکتاتوری همجنس‌گرا آن را اداره می‌کند که با اختلافات داخلی روبه‌روست.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 476K · <a href="https://t.me/VahidOnline/77491" target="_blank">📅 06:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77490">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7cf983c2ea.mp4?token=iyxd_qY2j2JqSZuY95wRVLd4oNGjL_gjjH3ojTPlt-_Dz9JWP9RBkajSGC_33epDdMdloRxiOd2T94S8Xx5RzKClkaFHrDVprfe5EtrUlA8PGLaLeO7-WZI823nn38NirSV1a0rJGmj2R0sEBbEe2nfYf0aX07jRZDhDaVYfvj7q7MjCl41RVPBV25ATgZUF9Ta7dec0VF8ZWk6IQpFO9ue5DlaThEPn4cmm52ll_l740pb2HX-ipC-4CHFhkMxeMkT-IC-b24diwDxbsfiak4lNlDYD9na7v0scc3B5rBEyX_xKQ84xrnkrxpUaKaOyKTfcZ5Iu9Zqkpzw4WyEkjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7cf983c2ea.mp4?token=iyxd_qY2j2JqSZuY95wRVLd4oNGjL_gjjH3ojTPlt-_Dz9JWP9RBkajSGC_33epDdMdloRxiOd2T94S8Xx5RzKClkaFHrDVprfe5EtrUlA8PGLaLeO7-WZI823nn38NirSV1a0rJGmj2R0sEBbEe2nfYf0aX07jRZDhDaVYfvj7q7MjCl41RVPBV25ATgZUF9Ta7dec0VF8ZWk6IQpFO9ue5DlaThEPn4cmm52ll_l740pb2HX-ipC-4CHFhkMxeMkT-IC-b24diwDxbsfiak4lNlDYD9na7v0scc3B5rBEyX_xKQ84xrnkrxpUaKaOyKTfcZ5Iu9Zqkpzw4WyEkjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم شی‌هی، سناتور آمریکایی [و افسر سابق یگان ویژه نیروی دریایی]، با انتقاد شدید از اقدامات جمهوری اسلامی، حکومت ایران را «گروهی افراطی و تروریست» خواند که ۴۷ سال است کشور را تصرف کرده و ایدئولوژی نفرت‌انگیز خود را گسترش می‌دهند.
او گفت: این رژیمی که با آن می‌جنگیم، اهمیتی به سیاست‌های حزبی یا اینکه به چه کسی رای داده‌اید نمی‌دهد. آنها می‌خواهند همه ما را بکشند. ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
این سناتور آمریکایی در ادامه تصریح کرد که حملات موشکی پراکنده یا تحرکات قایق‌ها در تنگه هرمز نشانه قدرت نظامی نیست، بلکه «دست‌وپازدن‌های یک امپراتوری در حال سقوط» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/77490" target="_blank">📅 05:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77489">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HbF9zSCDb7Ynxmw46D0ZFH9Cpbfha73kv_UTwh68lyf6jrzkwBHL_mLrbsYfPioOhuNYMunQaRpfNSPaQFAvm5TPe5wpKD86Qpfwpkj4OL0LalrGS7ip9W0vwCj0_tbA7Midu7yjr9tY07q7wQCk4g33o3G7-p6yVdMqvJuqlJJ2_6Rf3Fv65oYkDpid44wokR3R9a2_DIuuL_9oTehg3Cu6IsQIPQON2uUaFP7Uhp6Ocybh3dlB6FIeXBZDBE9Qm8Y40JRBh9g1xUGsRFt51OkntNZ0l9SfTUbzx1eDl5GgZkJwdy5q6UWoHnOL2_qH-dhnrcrVyKDd_sw2GoIEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت فرانسه در تهران با انتشار پیامی در حساب ایکس ادعای روزنامه انگلیسی‌زبان «تهران‌تایمز» مبنی بر برگزاری جلسه محرمانه دیپلمات‌های اروپایی و آسیایی در اقامتگاه سفیر فرانسه را به‌شدت تکذیب کرد و آن را کنایه‌آمیز پاسخ داد.
تهران‌تایمز پیش‌تر مدعی شده بود که در ۲۰ ژوئیه، نشستی با حضور سفرای چند کشور اروپایی، ژاپن، کره جنوبی و نیوزیلند در اقامتگاه سفیر فرانسه برگزار شده که در آن موضوع خروج دیپلمات‌های بریتانیایی و هماهنگی برای فشار سیاسی بر ایران مطرح شده است؛ اما سفارت فرانسه با رد کامل این ادعا خطاب به «خبرنگاران تهران‌تایمز» نوشت:
"به خبرنگاران محترم روزنامه تهران تایمز، دفعه بعد، لطفاً اطلاعات خود را با دوستان‌تان در سرویس‌های اطلاعاتی ایران که حدود ده دوربین برای نظارت بر سفارت فرانسه دارند، بررسی کنید. متاسفانه، هیچ مراسمی در سفارت ما در تاریخ ۲۰ جولای برگزار نشد !"
FranceenIran
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77489" target="_blank">📅 03:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77488">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2fWppX599joeOft6X-4yHDm_zwukXbYM8uA-L9q31QqYiVowArJTLaEhVeHDvNVD9ZU3IWABIhWRj-TbeyC_Sq-kId0ER3vTBxtJcgCOtvUhtOaZ5LQrkx6PrK-kUjMy4JwWEXIdmjVC24jZq0XbcJZH7FhwuXERjnRXizaBn3Yll3bMbj22K2tQaPPN2uTCd23Uw_4_NEIR00_i8_AxK5ezELro9jEiBaYk0jUbIKYw2Xwd68caWOYWh_PeWkBWWHLPX2sZYjDwEPGtf5JHgCyWvPH2wrHsutrRGluBttLqe3biPB7oT2qOr-kvuQKgRSQIcng5yPF53Z_PBB-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریم خان، دادستان ارشد دیوان کیفری بین‌المللی، در پی تحقیقات دربارهٔ اتهام «سوءرفتار جنسی» از سمت خود تعلیق شد.
نهاد ناظر بر دیوان کیفری بین‌المللی شامگاه دوشنبه ۱۸ خرداد ضمن اعلام این خبر افزود تصمیم به تعلیق کریم خان پس از آن اتخاذ شد که روند رسیدگی انضباطی به اتهام «سوءرفتار جنسی» در پروندهٔ او به مرحلهٔ نتیجه‌گیری رسید.
کریم خان، وکیل برجسته بریتانیایی، بارها این اتهام‌ها را که نخستین‌بار در سال ۲۰۲۴ مطرح شد، رد کرده است.
نهاد ناظر بر دیوان کیفری بین‌المللی می‌گوید کمیتهٔ اجرایی این نهاد رأی داده است پرونده خان به نشست ویژه کشورهای عضو ارجاع شود تا آن‌ها دربارهٔ آینده حرفه‌ای او تصمیم‌گیری کنند.
کمیتهٔ متشکل از نمایندگان ۲۱ کشور عضو دیوان با اکثریت لازم به این نتیجه رسیده که خان در ارتباط با اتهام‌های سوءرفتار جنسی مرتکب «تخلف جدی» شده است.
این اتهام‌ها از سوی زنی مطرح شده که در مقر دیوان در شهر لاهه برای خان کار می‌کرد.
طرح این ادعاها در سال ۲۰۲۴ باعث آشفتگی و بحران در دورهٔ مدیریت او بر بخش دادستانی دیوان شد.
تصمیم ارجاع پرونده به ۱۲۵ کشور عضو دیوان اقدامی بی‌سابقه در تاریخ این نهاد قضایی بین‌المللی محسوب می‌شود و می‌تواند در نهایت به رأی‌گیری دربارهٔ برکناری دادستان از سمتش منجر شود.
نهاد حاکم بر دیوان در بیانیه‌ای تأکید کرد که تعلیق کریم خان «به معنای تعیین نتیجهٔ نهایی پرونده نیست».
خان پیش‌تر نیز به‌طور موقت از مدیریت بخشی از دیوان که مسئول تحقیق و پیگرد افراد متهم به جنایات بین‌المللی است، کنار رفته بود.
در این بیانیه آمده است که کمیتهٔ اجرایی تصمیم خود را بر اساس گزارش یک نهاد نظارتی سازمان ملل، نظر هیئتی از کارشناسان قضایی و همچنین لوایح کتبی ارائه‌شده از سوی خان و فرد شاکی اتخاذ کرده است.
این رأی تازه‌ترین تحول در روندی است که نزدیک به دو سال دیوان کیفری بین‌المللی را درگیر کرده است.
@
VahidHeadline
کریم خان ۵۶ ساله که به دنبال بازداشت بنیامین نتانیاهو، نخست وزیر اسرائيل بود، به سوءرفتار جنسی با یک دستیار زن متهم شده است.
پیشتر آسوشیتدپرس در مجموعه‌ای از گزارش‌ها به اتهامات جنسی علیه کریم خان پرداخته بود، اتهاماتی که خان آن‌ها را رد کرده است.
طبق اسنادی که آسوشیتدپرس دیده است، خان با دستیارش وارد رابطه جنسی شد و سپس تلاش کرد مانع پیگیری ادعاهای حقوقی او شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77488" target="_blank">📅 02:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77487">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qtdr4cgalUQqx-MHLGlFp5SnwDmNU0s_P6AaVo_UjW_beYpCh4lD90IvMANBZpu7KDrIaE9-zAGSuWGeJNDDuKf-MSuwn69zX5Q9x7-Z2y57KwcSvscwWPYkm2zdBsjZWXfkKoEuK_T56KBvR7BlZIxrJH5Qz-TzH0lRqTjmVodopqSYLBaD-F6vvAbVNva9puLF5YvGiwKJ8Oqgg3jYx5PQd2aMLbUHFlmetBNZzFzGR9cN9A4-NILL0wLEuVVuqhUHcLxH2-2LHGqJ5xjGGPQdyL6JDDRZGSAuk3hK1KD9r7VdPxKa49lShsub33FDjQKgoGC20Dhr9wG-MqkebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مشترک نیروهای ائتلاف، جمعه‌شب، با انتشار بیانیه‌ای اعلام کرد که در پاسخ به اقدامات «بزدلانه و شتاب‌زده» شبه‌نظامیان حوثی در هدف قرار دادن کشتی‌های تجاری در دریای سرخ، عملیات نظامی متناسبی را علیه اهداف نظامی مشروع این گروه در استان الحدیده اجرا کرده است.
ترکی المالکی، سخنگوی رسمی ائتلاف، با تاکید بر اینکه عملیات پاسخ نظامی طبق قوانین بین‌المللی و با تحقق کامل اهداف عملیاتی به پایان رسیده، تصریح کرد: «بندر الحدیده هدف قرار نگرفته و تمامی بنادر یمن از جمله الحدیده، راس‌عیسی و الصلیف برای کشتیرانی، ورود کمک‌های غذایی و سوخت باز هستند.»
او همچنین افزود عربستان سعودی همواره در کنار ملت و دولت یمن باقی خواهد ماند و هشدار داد که در صورت تداوم اقدامات خصمانه حوثی‌ها، فرماندهی ائتلاف برای حفاظت از کشتی‌ها و منافع ملی «بدون هیچ‌گونه اغماضی» مجددا دست به اقدام خواهد زد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77487" target="_blank">📅 01:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77486">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vtky4SgC04kYUul3q_c-Uv0cbkY3UcrCHRGL3VFQBzHww1h4tAgfRpEVtIXHi0NMr_-iKv9i8O4SdpSbumaEdpsBO0AcKTA2ZYz7q7atlNAoADCiDeTPHm3DEHGk4W8QFRqlZDOzHhWQc3G1lwQP0sItGhE-mL4Z_j5_kwXQsiG87KGGRy86v7Ea7F5GV2ikB2oYPM7Zcd84CFNt6864vVSAGc27LuE97db4XCb0bLqJj4zQmjqg2NOd4iCJIbiAr-WHpTLWmzFGEMZMMxJAjBBvBEzOEWN6uY2JfzhE58zXmoLXjui7e7ibSZ3I5Amu0FH8kFX-uPaKKj9dQpjWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
اربیل، عراق (خبرگزاری آسوشیتدپرس) - ارتش آمریکا روز جمعه اعلام کرد که به یک کشتی تجاری دیگر که سعی در نقض محاصره بنادر ایران داشت، شلیک کرده است....
...
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی ایالات متحده، به خبرگزاری آسوشیتدپرس گفت که نیروهای آمریکایی کشتی M/T Lavine را در خلیج عمان پس از آنکه کشتی حداقل چهار بار تلاش کرد از محاصره عبور کند، از کار انداختند.
هاوکینز تأکید کرد که به خدمه کشتی هشدار داده شده بود و آنها از دستورات پیروی نکردند.
سپس ارتش به موتورخانه آن شلیک کرد.
این دومین کشتی تجاری است که از زمان اعمال مجدد محاصره توسط ارتش از کار افتاده است.
فرماندهی مرکزی ایالات متحده اعلام کرد که 12 کشتی را نیز تغییر مسیر داده است.
....
apnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77486" target="_blank">📅 01:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77485">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سخنرانی ترامپ، بخش‌هایی مربوط به ایران، ترجمه ماشین
متن زیرنویس ویدیوی بالا
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه دوم مردادماه در کاخ سفید به خبرنگاران گفت به‌نظر او جمهوری اسلامی ایران در جریان مذاکرات با واشنگتن «هر روز جدی‌تر» می‌شود، هرچند تاکید کرد نتیجه این گفتگوها هنوز قطعی نیست.
او با اشاره به اینکه مسیر مذاکره را ترجیح می‌دهد افزود: «دو راه وجود دارد؛ یکی را عاقلانه‌تر می‌دانم، اما راه دیگر احتمالا ساده‌تر است.»
رئیس‌جمهوری آمریکا با اشاره به حضور مقام‌هایی چون جی‌دی ونس و مارکو روبیو در روند مذاکرات، گفت موضوع اصلی «پیچیده نیست» و تأکید کرد که ایران «نباید به سلاح هسته‌ای دست پیدا کند.»
ترامپ همچنین مدعی شد در صورت شکست مذاکرات، آمریکا می‌تواند اقدامات خود را «به سطح بسیار بالاتری» برساند و افزود تهران در شرایطی قرار دارد که «عملاً مجبور به توافق» است.
او در عین حال گفت عجله‌ای برای رسیدن به نتیجه ندارد و تأکید کرد که باید این روند «به‌درستی» پیش برود.
@
VahidOOnLine
گفت که به سخنان شی جین‌پینگ، رئیس‌جمهوری چین، و ولادیمیر پوتین، رئیس‌جمهوری روسیه، مبنی بر ارائه نکردن کمک و فروش سلاح به ایران اعتماد دارد.
این اظهارات در حالی مطرح شد که پیش‌تر پیت هگست، وزیر جنگ آمریکا، در نشست پرسش‌وپاسخ سنا گفته بود چین و روسیه در سطوح مختلف در حال «تسهیل» اقدامات جمهوری اسلامی هستند. با این حال، ترامپ به خبرنگاران اعلام کرد که رهبران هر دو کشور به او قول داده‌اند در این موضوع دخالتی نداشته باشند و افزود: «فکر می‌کنم به آن‌ها اعتماد دارم. آن‌ها نمی‌خواهند باعث ناامیدی من شوند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77485" target="_blank">📅 01:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77484">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qLTzBig98QPy-gzn18mleRQaXv7VU2RBz8uElT4cDjLjQVspxyMLnPjkxtiYbe1C0W_o57UXVz3xwNGhmUG6_Z4DOI1fOMMQ6npeY6C-0MjbjS99i0quiQMJ6aMeULS6pi1vH_mHBjGwVkbPPMPJkcadd2N3yXvxr1BT5XKfwKrGvCnxz1fsgdHz4IsNULwxC9FqBDWQ_Nel4BBpnlPRTSWqFPQLUdvcUryQjt2anVxK4w6nx-0qCgqYAAx5p8uh9zVkpB0Yv7KPdzdAoOCUrvhDrOvG5xmEohGQDaBkO_jk58uyCgo5PZNUYuZI-b99WzJqvyC46nr5RrqaWa_Zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون روز جمعه دوم مرداد در ۶۶ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77484" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B-orADxVj6QtNjrR4LAtf4W5DcZV7rWWlRWgumH7DCHqkxjRmMo-t4muDFGStcCCaQYvCsJ_QSvq-D1m11Rwz3Za6IItC0HVqJe19rZu32C6xFnhkQm4MDKZaKLtiwFGDjAEl-edwHOYDdxksBALZLr69bRbCLgklTu4rwoY7gSy-RJROiXuryavJic8AfQNTwVDNMyGR6RYBonTpV2uv_D0bQbBxhpSlMrWPmdQusvgfTUmmxRztZJUNxBSk8kdQ64Sa8fNTDAJvBW8f11I37bj5CBOGqKpiNSI3w6-V632qJ5owh98HNcLUwpQoMZDdUGNisBUJgGXEM_uZqP7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/utmzGrXay5X--8fpjj6QLaVDGcFZsizxdhB-KzyMQoCNtbooKFI9YLnXBmN6PRbieBBny6ekUfqrxH0y5G0R8DNu21-k1HkfHuRdPjWBp-g1szQgNtp5u9hkvmGXUWp4yliAA0qokYLK0VnMzRviwGjXtTjMfiyCqY6_gapewzR6H9cY5-NsVirP5M9ntGzsZ0ZRCpY9a-FOogPK9aMBiSwJTPLhGAU4X6vq0eP4dOn5j2GqwmVQvcOMPwS99rsY3dROz3bqL0MVfnN3-xqje3elpbraGPFfGkPMxXJKRMXskPPj36bwrsf4gdSPf6WF24WqbS12KqARxVoOtZxQ2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده روز جمعه دوم مرداد، از اعمال تحریم‌های جدید علیه ۹ شرکت و ۴ فرد مرتبط با بابک زنجانی به اتهام دور زدن تحریم‌ها خبر داد.
بر اساس بیانیه دفتر کنترل دارایی‌های خارجی (OFAC)، این تحریم‌ها فعالیت‌های وابسته به هولدینگ «دات وان» (Dot One) زنجانی در ایران و چند شرکت پشتیبان صرافی‌های ارز دیجیتال او در ترکیه و امارات را هدف قرار داده است. خزانه‌داری آمریکا اعلام کرد که زنجانی با بهره‌گیری از سبد سرمایه‌گذاری متنوع شامل خدمات مالی، تجارت دارایی‌های دیجیتال، طلا و پروژه‌های زیرساختی، اقدام به پول‌شویی و انتقال مخفیانه وجوه برای ایران کرده است.
@
VahidOOnLine
تبلیغاتی که در کانال‌های تلگرام نمایش داده میشن به خود تلگرام سفارش داده میشن و صاحبان کانال‌ها ازش بی‌خبر هستند.
دیروز ده‌ها بار
تصاویری
رو دریافت کرده بودم که نشون می‌دادند مجرمان تازه‌ای حتی از آوتار خودم برای نمایش تبلیغ‌شون در اینجا سوءاستفاده کردند. ولی من امکان جلوگیری از نمایش اون رو هم ندارم.
تبلیغات مجرمانه رو میشه با کلیک روی اون سه‌نقطه عمودی که زیر علامت ضربدر در گوشه کادر تبلیغ دیده میشه به خود تلگرام ریپورت کرد.
فقط کانالی که تا سطح پنجاه Boost شده باشه می‌تونه نمایش تبلیغات رو متوقف کنه. چیزی
نزدیک به غیرممکن
.
بوست‌های این کانال در
سطح صفر
هستند. حتی نمی‌تونم رنگ لینک‌های اینجا رو عوض کنم چه برسه به استفاده از ایموجی‌های اختصاصی.
باید هزاران نفر با اکانت پرمیوم کانال رو Boost کنند که برسه به سطح یک و بعد هزاران نفر بیشتر از افراد قبلی دوباره کانال رو بوست کنند و....
این رتبه‌بندی ربطی به تعداد دنبال‌کننده و میزان بازدیدکننده و آمارهای اینجوری نداره و فقط باید هر روز از بقیه التماس کنی که کانالت رو بوست کنند.
یعنی حتی اگر به سطح یک هم برسم باز برمی‌گردم پایین چون باید هر روز بخواهی دوباره بوست کنند.
با روحیه من سازگار نیست.
خیلی زور بزنم، برای درخواست ریپورت سوءاستفاده تبلیغاتی از عکسم می‌نویسم: ریپورت هم میشه کرد.
از این رو محکوم به سرنوشت مشخصی در این زمینه هستم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/77482" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLTtjmFBs3--f0ueQ1Sa8I0TQvWijxmhwSR07hsHX-Sw_UHai_FZs0PAsNhqwYbBRjq7tHCmYv1QyWTD_zcCVHBDTCZHyo_abdAJ9fYUesNZGC6QxnTp9dKlwxjwuZhRxYaHkmGi2WzAJj2x6pHGhyftKYlu5VRwevuCIpAQhw4E-hGcAlEHjaSmlPYpxXHbZWi6FVvNcnLLk5QcQVuc08uf-EtbOCab_Z3gytOUB2yVvSvj0Jb0JSmCZmYSbG129uA3y_6Wxi1tCPcBvqJ3XGEo_3azGI3iXjYZByfw2bvZfuaxB17mvobSkAsKQdLxZncx8yAf3Y0m_02OBRhXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رئیس‌جمهور شی، در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت — و این اظهارات شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، حرف او را باور می‌کنم و علاوه بر این، من نیز لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
همچنین، رئیس‌جمهور پوتین، با وجود جنگ وحشتناکی که در اوکراین جریان دارد (روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز برقرار است)، به من گفت که به ایران سلاح نخواهد فروخت. او می‌داند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را پرداخت می‌کنند و اینکه آن سلاح‌ها چگونه توزیع می‌شوند، هیچ اطلاعی ندارم.
بنابراین، دو کشور بزرگی که مردم اغلب در ارتباط با ایران از آن‌ها نام می‌برند، به نظر من، در این موضوع مشارکت نمی‌کنند. اگر چنین می‌کردند، برایشان بسیار بد می‌شد — و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77481" target="_blank">📅 19:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuASlR4LVxTr6NCO42f5OMved7SdnApbQqmp4C2IhZBUqw2eYkCLrWgYYU4Bi1TOeo_hKr23tiYfej-7GF1UjjdoQcDd2uOTTuOGG2e6fDK6Y_HySIE7806KxZt-E_ZPEHzt0gI5CXqqWE8dmOBLEG95ZhMQa1SBwqgDu346p3Et3BuszkrcJL1z9jpJazdvIYszeeGGfO8leGqMPp5XEnq4SpwZpu9U6_KEZA7amT4qlWFKtfCfaj2pcKCyWMtFx7m-m8ZmkOKgKXwwg021nl03P7jxswZX9IdjNYu2p5BKF-7urOQ1fhux6iKL-h9vxUhzfnGniBjKiGtSxwOMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای اطلاع‌رسانی دولت روز جمعه دوم مرداد، با صدور بیانیه‌ای از اقدام سازمان صداوسیما در سانسور بخشی از سخنرانی مسعود پزشکیان در روز ملی صنعت و معدن، درباره اجازه رهبر پیشین جمهوری اسلامی پیرامون مذاکرات، به‌شدت انتقاد کرد.
در این بیانیه با اشاره به سوابق مشابه، از جمله پخش نیمه‌کاره مصاحبه رئیس مجلس شورای اسلامی، سانسور سخنان رئیس قوه قضائیه و پخش نشدن مصاحبه‌های وزیر امور خارجه در طول جنگ، رفتارهای صداوسیما «گزینشی و مبتنی بر سلایق سیاسی یک جریان خاص» توصیف شده است.
شورای اطلاع‌رسانی دولت تاکید کرد این اقدامات وحدت‌شکنانه دقیقا پس از پیام رهبر جمهوری اسلامی مبنی بر لزوم «وحدت کلمه» صورت گرفته و نه تنها شایستگی این سازمان را به‌عنوان «رسانه ملی» زیر سوال می‌برد، بلکه تهدیدی برای امنیت ملی و انسجام اجتماعی محسوب می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/77480" target="_blank">📅 17:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v7mEPJwGA8VZUAnxN2gYLUFYjBVSxMPi9D3fYvQdetoml6SJq5OiZE5RGtqIgouLpPx4oOrcxAOizqCIoqP7pfoqznaEj3cusRIaBgG6KOSJq0x83dJPBoT8deq5EGYuZtOHWGV-3bkRhNub2RlRys1gDdufLDVYMDojtTWZEWOYeU8UEZm3WdWuhAfAbcscMIizKv9UH-CaSaqLtTLda81MCr4Cw75ocA3Ur8tOgR7MBMJw5hJyVGlaBhkT1dc-0QdqnPETW5wAPD0CSDHy9t8fHoCo8Hu72iky4XYh5xPSP5O9RGkKj8yERM4x53BRHhCJXIL7O4DIf778QvmsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین (شاهان) علیزاده آذر، زندانی سیاسی، با اتهامات سنگینی مانند «توهین به رهبری»، «تبلیغ علیه نظام» و «سب‌النبی» به دلیل «توهین به آدم و حوا» روبه‌رو شده است. او دی سال گذشته نیز بازداشت و به «تبلیغ علیه نظام» متهم شده بود.
این شهروند ۳۸ ساله و مهندس نقشه‌بردار، با قرار وثیقه آزاد شده بود اما بار دیگر در ۱۳ تیرماه مقابل منزل خود در اسلامشهر به دست نیروهای امنیتی بازداشت و به زندان تهران بزرگ منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77479" target="_blank">📅 17:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VONWLrX-VrFw-vE00-7ds6KPaUfdc8FzIBWcmAb8gC0WcW8UreQsmsTS_sRyk80BL2zaHIHcyQzih2N15xo5zMlfQylVX82HCyY2RyEquOd9WcKKqJXaOaxeTB6M0VUpwNJbwJ3494juy-ScPUYJU388vDX4PErJKQUJXYjar36EiXeSOfapyCNJFfsnnStxjdr0t9Dqg5TS4xC7aRMa1I-JAm3Mj9sHWoP0T719wb4MjPu7DrZb3OSrk77NBCbssuqZV8NOloARSZeBkJThbKvdmkgvz4QapK_EpN3c1bd8e3OV9UIc8ihp3vUUEz84Mg6IwMRExxITKIiV-xqYsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی وال‌استریت جورنال روز جمعه دوم مرداد به نقل از «منابع آگاه» نوشت که دونالد ترامپ، رئیس‌جمهور ایالات متحده، در روزهای اخیر نسبت به این‌که مذاکرات با ایران بتواند به صلحی پایدار منجر شود، بدبین‌تر شده است.
یک مقام ارشد دولت آمریکا به این روزنامه گفته که «ترامپ معتقد است تنها چیزی که ایران می‌فهمد، فشار نظامی است» و افزود او در برابر تهران در «حال و هوای انتقام» قرار دارد.
این مقام همچنین گفت رئیس‌جمهور گزینه‌های مطلوب چندانی جز ادامه حملات نمی‌بیند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77478" target="_blank">📅 17:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I91gAgRyMtevNGDSfRcO8CflMNaEebBMgIM7iKnyn-uH6grkis2i-BRLOkJHUGFkMEkXdTGV22oHifjxtfdFXzltTI1_u6tu1EPp98Owi2bXZv8M3T_xln0n6IeMox1QsgenAr84tZC3L2EL2qGxrR5dIN1b0liQBbfJOZaf_lXh2QV_221lv9erD-nlcx_Kyc32aPkQxOyWEzU0YxPy4ma60Fo4Q2JNGx_zxpXXKo_ZeFHJePaze5qWIgkzyFNT0-P6tK1QDl3ZxVsmyOGsJ3inWcVLT7ZJANNuX3f3XgbtK0ECXrjKeQqpLn0P_R0edCFi3H1-2evVr6EWaeWMAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت بریتانیا اعلام کرد نیروهای مسلح آن برای حفاظت از کشور در برابر هر حمله‌ای آماده‌اند.
این موضع پس از آن بیان شد که سپاه پاسداران انقلاب اسلامی هشدار داد نباید به بمب‌افکن‌های آمریکایی اجازه داده شود از پایگاه‌های بریتانیایی استفاده کنند.
سپاه در بیانیه‌ای در روز پنجشنبه اعلام کرد آمریکا از پایگاه فرفورد در جنوب‌غربی انگلیس برای انجام مأموریت‌های بمباران علیه ایران استفاده کرده و افزود هر پایگاهی که برای چنین حملاتی به کار گرفته شود، هدفی مشروع خواهد بود.
اندی برنهام، نخست‌وزیر جدید بریتانیا، هفته گذشته در جریان این خبر قرار گرفت که لندن بار دیگر به توافقی با آمریکا برای استفاده از پایگاه‌های بریتانیا در چارچوب آنچه «دفاع جمعی از منطقه» خوانده می‌شود، رسیده است.
یک سخنگوی دولت بریتانیا گفت: «نیروهای مسلح ما آماده‌اند از بریتانیا در برابر هرگونه حمله‌ای، چه در داخل خاک کشور و چه خارج، محافظت کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/77477" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77476">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGsw_-2kaoNmnFbEzlKEtoUimHbfWRx3tul-8YHlfBgxCASSjPQW7gXejumsD1F92NgQNWz3qw8TSNIvjy6glcFv1IqK54ubMkpGb0K68RnaWrfuVPPZCVd2OqXNMHhPvXvi0_s5mHC-u1UCuSPILpLVwTEjrH7H3QyHoc4m6SLfDGNC--Mjxy1wyvoIipFJRM7s45ktgCXP1msL0SSDRGZ3SIPc5IzpMApx3WxEylL10STBRJZ-IwVLmNb1q7Y9mivQ_ESAzZ2y5pozWnpG1TUJ2WMnmqYMyt9rYTvpDiIBaplMN5MmbuOP-QQs43mk_d3Gd23T0Uv_27BjhrHaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران روز جمعه ۲مرداد۱۴۰۵ با انتشار بیانیه‌ای مدعی شد در جریان عملیات موسوم به «نصر ۲»، ساختمان باقی‌مانده مرکز داده‌های شرکت آمازون در بحرین را هدف قرار داده و منهدم کرده است.
سپاه در این بیانیه ادعا کرد مرکز داده آمازون نقش اصلی در تکمیل اطلاعات ارتش آمریکا را بر عهده داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77476" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77474">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IxQFmarlR_e4Pk1zXxs5KfJDvO5FdIOl02TdBbn4QLruMdDVTS-mYsHQRtdE65t2pZ_0T54J0FXPXPbzs670G65K8u24vCg_1L1-GW-ZSBE4H33ECPMZEluHPwYYzHVuxnjteK4TQAZv4wjZTH3YUEY5GIww76u_rDf0cBTSCjkjyXRw-xUwjZWl4vXg044rLsEJj1reR3fjRkv8q6u2tyrA5hXP-2tTQcSKvEwYUK6stIIVQk1O5yb8BA8yInBCO0ZP7H9jPACRE3v5xha_9fDVsmAkPaPVtQ9l05kNtDzqpGR4uVAz0Ze-DCUfJFAP8T2fDMafgKBIIH6b4Rv8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/doyUmWj6FXgrYpBGmjPBYugNWzyZyfzzd_H1adgXiXHJ6LtLIdHVmVxPQ-m5pgYS2AOEOS7pGFIZP1ALRoLRAgnhHk5gmJ98tzmJw_lw5Y_2gwmpQNHihBAONamLXcZSzJaNFLsSk_sBwubwZ0Sodxm8oKeIl93uoO4WvKwxI_fL_a59fggEjPGmNFnaW-t7g5iVMS2kJGr9uOsxy1vQ31TVKqiliTKpQIqfOCDcHhHmh19zcIcIf_dW0LMf0IWBxZbA-Q3s28e4iT4yTSCsCd5aHQb-VYfFHwSHsCIZ8stCikc27QH5REu57Z8UziNNTbW9TAelFMcNKM8z5TPPpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه نیویورک‌تایمز به نقل از چند مقام ایرانی و عراقی گزارش داد که جمهوری اسلامی ایران پیشنهاد آتش‌بس از سوی دونالد ترامپ، رئیس‌جمهور آمریکا را رد کرده است.
بر اساس این گزارش، پیشنهاد یادشده در جریان سفر علی الزیدی، نخست‌وزیر عراق، به تهران به مقام‌های ایرانی داده شده بود.
آقای زیدی در جریان سفرش به ایران از جمله با مسعود پزشکیان، رئیس‌جمهور و محمدباقر قالیباف، رئیس مجلس شورای اسلامی دیدار کرده بود.
جزئیات این پیشنهاد آتش‌بس مشخص نیست اما مقامات ایرانی به نیویورک‌تایمز گفته‌اند که این تنها پیشنهادِ روی میز است و آن‌ها علاقه‌ای به توافق موقتی که مسئله کنترل تنگهٔ هرمز را حل‌نشده باقی بگذارد، ندارند.
@
VahidHeadline
دفتر نخست‌وزیر عراق گزارش روزنامه نیویورک‌تایمز مبنی بر انتقال پیشنهاد آتش‌بس آمریکا به ایران از سوی علی الزیدی، نخست‌وزیر این کشور، را تکذیب کرد.
دفتر رسانه‌ای نخست‌وزیر عراق روز جمعه دوم مرداد در بیانیه‌ای اعلام کرد ادعای مطرح‌شده در گزارش نیویورک‌تایمز «کاملاً بی‌اساس است و هیچ ارتباطی با واقعیت ندارد».
دفتر نخست‌وزیر عراق در بیانیهٔ خود مشخصاً گزارش مربوط به انتقال این پیشنهاد از سوی آقای الزیدی را رد کرده و درباره وجود یا عدم وجود پیشنهاد آتش‌بس آمریکا به ایران توضیح بیشتری نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77474" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77473">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0055dbc0e3.mp4?token=aE-ESdc8k8bRyVqEhoxDA8zGXt5z7is7GI-cQtDgEFGcWQHn8nXbDVlYZu1Ea5V1JF6yvljiQmQ6UDOSp2gbi2MEfdLLFAOasl52Bvabjk2Mkeydcc70jAcx2AsHSITc6v5OrVSjQFf0k01TSgxz783SXYyUsVRSXM5cLXk2aNsCvk1yfGyUw0MnzBDbQHW9Fh4Qz1XuMJgS4cMmdVWoHAb_CN41W36JoF0mNXPLQgJ1IVR6jZtHx7Y4CkTZIj-utLgqm52SsyQ2Ialb_BWM9yQRqfUamtclO0_YL4-2Av62Kxe9N5QqEbIoeFhb_DfrTfIS5J03u_oIL4rtxY2z-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0055dbc0e3.mp4?token=aE-ESdc8k8bRyVqEhoxDA8zGXt5z7is7GI-cQtDgEFGcWQHn8nXbDVlYZu1Ea5V1JF6yvljiQmQ6UDOSp2gbi2MEfdLLFAOasl52Bvabjk2Mkeydcc70jAcx2AsHSITc6v5OrVSjQFf0k01TSgxz783SXYyUsVRSXM5cLXk2aNsCvk1yfGyUw0MnzBDbQHW9Fh4Qz1XuMJgS4cMmdVWoHAb_CN41W36JoF0mNXPLQgJ1IVR6jZtHx7Y4CkTZIj-utLgqm52SsyQ2Ialb_BWM9yQRqfUamtclO0_YL4-2Av62Kxe9N5QqEbIoeFhb_DfrTfIS5J03u_oIL4rtxY2z-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون سیاسی و امنیتی استاندار گیلان از حمله موشکی آمریکا به مقر نیروی دریایی سپاه پاسداران در زیباکنار، در صبح جمعه دوم مرداد خبر داد.
باقری گفت: «حدود ساعت ۷ و ۳۰ دقیقه صبح جمعه، بخشی از تجهیزات مستقر در این مجموعه در حمله موشکی آسیب دید.»
معاون سیاسی و امنیتی استاندار گیلان همچنین افزود بر اساس بررسی‌های اولیه، تاکنون «هیچ‌گونه گزارشی از تلفات انسانی» دریافت نشده است.
@
VahidOOnLine
مدیرکل مدیریت بحران آذربایجان‌غربی اعلام کرد حوالی ساعت ۹ صبح جمعه ۲ مردادماه، یک نقطه در شهرستان پیرانشهر هدف حمله هوایی آمریکا قرار گرفت.
پیشتر اخباری از حملات هوایی و موشکی آمریکا به اهواز، قشم، بندرعباس، تهران، امیدیه، اندیمشک، خرم‌آباد، خنداب در استان مرکزی، نایین در استان اصفهان، تفت و شیرکوه در استان یزد، فیروزآباد در استان فارس، کنارک و زیباکنار منتشر شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77473" target="_blank">📅 17:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77471">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOgHH1SWiL035k6_tJSMzqJ7dMV0rXD6o84AMdVcjrSBFd5Q7rec15zcDqL0GYtvKbAbZDagI2OP0IGm2kSnoXXaBcVV4Nn2z7RmPVbhsbRrz255KiZh4KlNI9vyuygNW0Aao21ilIA4HYElnbmTLGmv2-mxlIJ8rygkBzz_HV1dq8NspHrJ9sk0RpjDLvsoSHgXHKZJZ47Yrpa17uEY7TCWdRjy_ANsMzo65if_fewOImj4t3vqOWZXXUVgDdAnbC4yoqCnD6nsRha0SjJYu2o6IY6tPJUB7Bguu_RE08UOKgl-uuUSnkgak2Cr0-aEzD-Bh2_3lqOze24AGMkcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceDopN25rX3QkEWo1tHovIKyfs-2rBhDbYap2t1g7bLCeDGw7lJWjoY9VFTdDCZ6OTDYDkowytWLMaH3zVI1qOEuk2MT63cDCGfE8U66Wmc9uU_QQ0jCCzvHEJbFJCqUE29A-uh2vdFImy7O6U8GWXuEGq6qQ01MniLzY303Qkcp62CLdoIXp1WWb-xRzdCKKx9PwkS8B80nT5xIuEYN6GHKlZ_eliuJWpG-jpNRKpuiR2ifgamJlFu5sb61BGYqQvZ2Cu7frTNZQS474iWHb702r-JyGSP7slFWnG2zaZTT5rbqHZ6MLZnG99H70E-U4QEFgV6hza9izxwaWxc8rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عفو بین‌الملل روز جمعه دوم مرداد از مقام‌های جمهوری اسلامی خواست که فوراً هرگونه برنامه برای اجرای حکم اعدام بنیامین نقدی، ورزشکار، را متوقف کنند.
بنیامین نقدی ۱۳ دی‌ ۱۴۰۴ در شیراز در ارتباط با اعتراضات سراسری بازداشت و به‌مدت ۵۳ روز به‌طور قهری ناپدید شد.
رسانه‌های دولتی ایران یک روز پس از بازداشت و پیش از برگزاری دادگاه، «اعترافات» اجباری او را پخش کردند.
این ورزشکار بعداً در ۲۲ اردیبهشت امسال به اتهام «افساد فی‌الارض» به اعدام محکوم شد، با این ادعا که از کپسول آتش‌نشانی علیه نیروهای امنیتی استفاده کرده است.
عفو بین‌الملل می‌گوید که حکم اعدام برای بنیامین نقدی پس از «محاکمه‌ای به‌شدت ناعادلانه» صادر شده است.
این نهاد حقوق بشری با استناد به الگوهای پیشین مقام‌های جمهوری اسلامی ایرانی در گرفتن اعترافات اجباری «تحت شکنجه و سایر بدرفتاری‌ها»، ابراز نگرانی کرده که «اعترافات» بنیامین نقدی تحت اجبار گرفته شده باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77471" target="_blank">📅 17:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77470">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVeGKODUBBWeqm8VNiViDgWFIUK-2voeileGzcRcfMEgizi0eSMVtmVgOLYrT9Y09BmkiqC2t5Rim1z2cDXj-5p_AwJyJzTsi-9lPTPMJw8ydmvPI1QAj9b2LAPZ5Xsd64wfc0bbzbIuLHHBVm2E9wxMThiA-tO1JXoxiVhuOoRQYsvgcvI-mQHHgGMVLioirfemokhc5M1u2dS7KJWEgBKNUGRNm5IGhvh4Id1GucseGodV_g9CICz3guG3MMVj6iiaBvQea0SMPFeU28XYAl5lgmF-qlAQLt9YXZYSrmSpTiY_tE25QoRiS8ui0vmnVm84B0sj_QwxIjbDOlmBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته بود:
از این پس  خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
واکنش عراقچی، ترجمه ماشین:
مصادره دارایی‌های یک کشور دیگر برای پرداخت مطالبات نامرتبطِ آینده، بدعتی آتش‌افروزانه است.
کسانی که از چنین منابعی استقبال می‌کنند یا از آن سود می‌برند، باید به یاد داشته باشند: وقتی دولت‌ها مصادره را به امری عادی تبدیل کنند، دیگر دارایی هیچ‌کس در امان نخواهد بود. هرج‌ومرجِ متعاقب آن نه زیبا خواهد بود و نه مسالمت‌آمیز.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 476K · <a href="https://t.me/VahidOnline/77470" target="_blank">📅 06:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77460">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CJQuVXnMqhS_aMIzXNL0N-Uvb9gmInbTCmQ7boSLFKuyPhvS2QSLytYQ6GbSkYOSEgrsdVv34RvpV1Wn48HyEkKbc7Tbw8tjFr_7QQ76EYpmEZpf752Bmkz9fmmTtTENuq7kRdrg0X0A7vyqgrxOtUTGq4A9Ur79fCdzLU1KDPjPFl8MJ5gMuAGN8NJZZBIQ5n95T0vQ_AFOJ0TyMmVutAHp1EWluxECCQkvGrVQvojlhF2wtQK8xR3JF35HNPsZo75f9NPIJKSFR2pE0zf0DM37LuvpOJpOmgfRvQafx5qgMS7sP-uiqg11cWnBvS_XljfGgHQ7p5MBJzYPg11tXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dSJMvfPAetf-MpUokmkASNrF8pH7H6BWp4sP9TC-2nw3S4rU4pl1GunYrfOFwgrv0RYJTRqFl53V7qvbZTvJ0qnduXA8IFd0U-TUFvXunPNEKepSzUM2dvUwFyuDVSbyOaTyMRgHdrhxykekOcJzZhqWtRnJD13Kyf3Oj-iXeRXOJG-UZxhZs3y3UO1-zmCFiOELAqxbKVQmcn8Szl0_WwOqGbo9olluotFIJwWT7q0zfs-6ov4fuaH-2_5cp9Obr9UTwD9M---LRjbspGY8101V6fdNLUD_jNPsbbbQfQzWy_BmivAkgMppSVX6ZSJjhYJ402QgmF91WBtFzY4wlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f-U_R5TpyoDIP0x_dEgJNIeE8G9MNBaBQuUPnX4-w81JDIJ9hGDK4xY7PeOZ-hc2-rpJFwRplrDbDATPL5m5RDEW8eOhLoub3x45oQQnSvVms46jqeM0DxCUODc7xLgJ2frVtstwRCNOqp9Hbb0857nGDRXU7j4yWka-V7j_98qoh2oAje_e3oDRw6fYL1WfwnY8oW8CysQhGY9wg7F4y5QkcS2MWxqdYt6_gqOkQ2gB21DCa2Zn4Bs-SBayBcjDsKgv9X_wIq-UOGqyvbTV-7h2D33M7MpkB6MI2JEhXONbv1Ip52OoXLyU04gi8nMcLr19w-AHqTgWcMzJBUMkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sjsflcCoWk_CK5x5d_xDMBY0Ea4f9zQu6blp3V3_GN6aoa4ZtU__3hrE6qHZiJgJsOcqFZKN6NGVVXRxAkuyGFgklzp0v1lxU5X7kOa0TBGOeZdhzyuIeVEqtVP0Ulg4t6gCFAn2WjCfVQkWYbWk4fWrdr8V72a5RiHxPRJTkR2bThwGC7q_qdb8mPT_nif7UBq0h1vSaUOKhfN1ALO1i0S0ha23D8HCJyKLrM8weZD75m1gK7XFTlSwCS_UAqEW2DrAPpRlGlxymbkDHzH9FejNa0GL3b7r1GpHNzGxQX57lioIxjPbrjCeHNXNxpKft5-q82BwQanSZbteqWkRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ATuLxoJMafRWbegOYZI-9xjR-2BGFYftPBymEr-yJFF6W8CaubSx83FG82m8pI3UTtTiQkuPsX97B9eg7QQ0u6X3PgMQ1weMFOIqYodtWCRI8zrP3ocObZaNvOyUiyDflQdwUFFkqtm748aJ51oPUG2WA4rXzM95ABtY-wMPXGTMEFz05HR8e4TeVE2yVsbdAySeKvsy3dcbPekvU0GslWIhqYF9JVtWi5UpQ6lYikiMLJEk7PgJfp2CQiGai6z1ZWwe1LPADgOGHGhutr0eFomDkHPqJQ7QKrG_bb1FNsmbAtArLro4KmSGVc5UqV8x7t0Qzs8nkZGO-ugG_rdEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SrcYtYtsH3WlLPGOewQ2ZE11EpQM3uca96KdiTkx6o2GKfG5BNog26BhRVD-vBbk_07IKwOKbz663USdkWr2sOUJPVZX4JwgLyDkWL70UOj-L68PSQSKmIi8sVxNnEtEkDz1eO4X9elPrpLe-LipLZWvM1Bfz5F74nx-wK2VIDE6VSnHiyTulNVgtaxwXSS02KaHlk8C7tpfGcMwJCAe1tIah1AUpba_4w99nSXudwFRl_eW875CBCaOZcAbxD2IeOyqR53pnhR4euU7A1FHYNxvpmdtcHY9i0iBFMw3k6cBSJkue8x-eDXNdY2u96LSIscHbxN8G-WlL4KCcmZx8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=F2KXCUUwxtsrPp7b5dEaGlS45uhPgDGejavImaQKtkNUqzdzjhdcY0rpUQXvCW0JjUp4EpGwqEECysg9K_KksL04rDxOo-Yj2PMb_RBD62YThOUFlbGdalN_kEgnIHRnPzoD-VAw48Uq3aYYfYNWot8m6jJyz4DCz4iryKR6okWByIVra5Ls3LSeZ5BzqFaLV73mf1OYKG3YFor5qy6FHpNcaLbyO0WKgH6xFfvfub29uyRvEE-_VM--J49T0YXWOxt1xN0OstMEgIz-sckIluAVCTVLTHVtWhzF2HzWnyBUmSAk5RyU0mCBBQJ0UbeSZ6FXWLmwc7tGgjY3OVKUfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=F2KXCUUwxtsrPp7b5dEaGlS45uhPgDGejavImaQKtkNUqzdzjhdcY0rpUQXvCW0JjUp4EpGwqEECysg9K_KksL04rDxOo-Yj2PMb_RBD62YThOUFlbGdalN_kEgnIHRnPzoD-VAw48Uq3aYYfYNWot8m6jJyz4DCz4iryKR6okWByIVra5Ls3LSeZ5BzqFaLV73mf1OYKG3YFor5qy6FHpNcaLbyO0WKgH6xFfvfub29uyRvEE-_VM--J49T0YXWOxt1xN0OstMEgIz-sckIluAVCTVLTHVtWhzF2HzWnyBUmSAk5RyU0mCBBQJ0UbeSZ6FXWLmwc7tGgjY3OVKUfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: پرتاب موشک از بیدگنه، خمین، نجف‌آباد، شاهین‌شهر و...
تصاویر بالا و پیام‌های دریافتی از استان تهران:
همین الان از ملارد موشک زدن
همین الان ساعت ۵:۵۲ از بیدگنه موشک زدن
سلام وحید جان همین الان موشک از رو پرند رد شد
سلام همین الان 5:51 از ملارد موشک شلیک شد
از بيدگنه موشك فرستادن الان ساعت ٥:٥٠
شلیک موشک از بیدگنه ملارد ساعت 5:50 بامداد
۵:۵۰ دقیقه از بیدگنه موشک زدن رفت بالا
سلام وحید جان از [....] بیدگنه الان موشک هوا کردند بعد جنگ ۴۰ روزه این دومیش بود
سلام وحید ما فردیسیم همین الان از سمت بیدگنه فک کنم موشک پرتاب کردن و صدای شدیدی اومد و لرزید ساعت ۵.۵۱
5.52 از کرج موشک فرستادن ردش هم تو اسمون افتاد
اشتباه نکنم از بیدگنه
وحید جان سلام.  رد موشک از سمت اندیشه  شهریار خیلی صدای مهیبی داشت همین الان ساعت  ۵.۵۲
آقا وحید سلام ساعت 05:50  از بیدگنه ملارد موشک رفت
سلام. روز خوش از بیدگنه موشک فرستادن
جمعه دوم مرداد ساعت ۵:۵۳ شلیک موشک از [...] بیدگنه واقع در ملارد به سمت جنوب غربی
🔄
وحید جان همین الان دومی هم فرستادن ساعت ۶:۰۰
سلام وحید جان همین الان موشک از رو پرند رد شد
شلیک دومین موشک پیاپی از ملارد
از ملار یکی دیگه شلیک شد  6:00
دوباره موشک زدن از ملارد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/77460" target="_blank">📅 05:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77459">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=EeE-OrXyvCueLPJNSZcUBovyEtSIr5Px8ZvN-_BzrSZUR2w9ODXVS9XNWfYPH-GT0-DzhiJylsj5SLUI6hsUWltopo4uwS14b6gTYOU59vaxZ6hGhc7Y0--16sruF1u5v_as3Dfw0vG5Dj8R6TpiMHO13sMWl5cw066FcjVR-FMfnOeKPCrd90EoqpzSCmN0sllFl5KEqFom-5w_9UheWDvIjokkWSbQX6B2fg_-EiGgeTxWhNCHmWNKnZW4mUrg3PLiu-afyryTcK_QkzyaMbmZj2EUAQQs6kfumqJa0D0qH--OZFdAy7KoQyhP0BRD_AeAva0soibdHu6gOtLoKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=EeE-OrXyvCueLPJNSZcUBovyEtSIr5Px8ZvN-_BzrSZUR2w9ODXVS9XNWfYPH-GT0-DzhiJylsj5SLUI6hsUWltopo4uwS14b6gTYOU59vaxZ6hGhc7Y0--16sruF1u5v_as3Dfw0vG5Dj8R6TpiMHO13sMWl5cw066FcjVR-FMfnOeKPCrd90EoqpzSCmN0sllFl5KEqFom-5w_9UheWDvIjokkWSbQX6B2fg_-EiGgeTxWhNCHmWNKnZW4mUrg3PLiu-afyryTcK_QkzyaMbmZj2EUAQQs6kfumqJa0D0qH--OZFdAy7KoQyhP0BRD_AeAva0soibdHu6gOtLoKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند"
پست سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۹ شب ۲۳ ژوئیه به وقت شرق آمریکا [۴:۳۰ صبح به وقت تهران]، سیزدهمین شب پیاپی حملات علیه ایران را با موفقیت به پایان رساندند.
سنتکام مراکز فرماندهی نظامی ایران، تأسیسات نگهداری پهپادها، شبکه‌های ارتباطی، سایت‌های نظارت ساحلی و توانمندی‌های دریایی را هدف قرار داد تا تهدید ایران علیه دریانوردان غیرنظامی و کشتی‌های تجاری در حال عبور از تنگه هرمز را بیش از پیش کاهش دهد.
این آبراه بین‌المللی، با وجود حملات اخیر سپاه پاسداران انقلاب اسلامی ایران، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با پشتیبانی نظامی ایالات متحده همچنان آزادانه در این تنگه تردد می‌کنند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه در حال فعالیت هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77459" target="_blank">📅 04:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77458">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان همین الان صدای انفجار خرمشهر
درود خرمشهر صدای انفجار ۴:۴۰
خرمشهرو زدن
سلام وحید خرمشهرو همین الان یه موشک زد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77458" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77457">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان یزد صدای انفجار اومد
سلام یزد رو الان زدن
یزد یه صدا انفجار اومد ساعت ۴/۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77457" target="_blank">📅 04:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77456">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چند پیام دریافتی از فیروزآباد در استان فارس:
سلام فیروزابادو هم ساعت ۳:۴۵ زدن
صدا اومد فیروز آباد فارس خونمون لرزید
نزدیکی فیروزآباد فارس چیزی شبیه انفجار رخ داد و موجش بد جور گرفت مارو
الان صدای انفجار فیروزاباد
ساعت ۴ صبح
انفجار مهیب
سلام  فیروزآباد در خونه داشت از جا کنده میشد
دوسه نفر  میگن پل احمدآباد بوده که راه ارتباطی هستش به سمت جنوب
آپدیت ۴۰ دقیقه بعد: صدا و سیما
شنیده شدن صدای انفجار در فیروزآباد فارس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77456" target="_blank">📅 04:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77455">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت 3:43 صدا پدافند شرق تهران اومد ولی کم بود
ساعت ۳:۴۵ صدای پدافند شرق تهران فعال شد. از حکیمیه صداش میاد
پدافند شرق تهران فعال شد
سلام صدای انفجار در پردیس تهران [لابد انفجار شلیک‌های همون پدافندهای ضدهوایی است.]
الان هم پدافند زد
پدافند پردیس فعال شده.
شرق تهران صدای پدافند
[+ پیام‌های دیگری که با تفکیک اسم محلات مختلف شرق و شمال شرق تهران دارند فرستاده میشن و دیگه نقل نمی‌کنم چون همین محتواست که هی داره تکرار میشه.]
آپدیت:
بعد از چند دقیقه تموم شد.
🔄
ساعت ۴:۱۰
دوباره صدای پدافند شنیده شده در شمال شرق تهران
🔄
ساعت ۴:۲۲
پیام‌های دیگری درباره شنیدن صدای پدافند در شمال شرق تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77455" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77454">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s45olh-A6z-6krwhbtvT73GWkB_dn3Jy4tscU_8qyRjTbUuvGYBJGS5Z0KVird-UYs2O4Mioem9c2WE-2rXisxBE4Gl-o63KrES8_AxEBNl3Lpnld32h8x3jRxZLElryFET8Y1-yiMcHJNNTbNoC_AHeKYHbKjwgxSFlc8cx8g_LELt3nH4gXoJbdxvJt8LbQsFRIyxFtLlmNpGeQW9XTpZfcunhClnGIX-Lf5QF8jrbjtk7pxe7vVS4DhP3s8UzSzcM8tCmGMLJSZG73FTTXmzRZdN-QIp0_38texP_PdBP4MOQ_im61uotXyRN9UQ90BWUDFTjqfoh-YOttQfWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: تفت در استان یزد
پیام‌هایی دریافتی و تایید نشده درباره مناطق مرکزی کشور:
ساعت ۳.۰۵ دقیقه شهرستان خنداب صدای انفجار خیلی بلند اومد
سلام خنداب و زدن 3:05
نزدیک خنداب صداهای وحشتناکی میاد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استانداری مرکزی گفت: یک نقطه در خارج از شهر خنداب دقایقی پیش هدف ۲ پرتابه دشمن قرار گرفت.
———
سلام وحیدجان همین الان پایگاه نیروهوایی انارک نایین را زدن
آپدیت چند ساعت بعد: منابع حکومتی
معاون استانداری اصفهان: ساعت سه بامداد امروز منطقه‌ای در شهرستان نایین مورد تجاوز دشمن متجاوز آمریکایی قرار گرفت.
———
تفت از یزد هستم
از سمت بام تفت - شیرکوه رو بد زدن
خیلی صداش بلند بود
ساعت ۳.۳۰ دقیقه تفت صدای انفجار امد.
دکل تفتکوه رو منفجر کرد
سلام ۳:۳۰ تفت استان یزد صدای انفجار مهیبی اومد که از خواب بیدار شدیم. از کوه های اطراف نور و گرد و غبار شدید بیرون آمده.
داخل شهر نبود
سلام وحید جان .ساعت ۳.۳۰ تفت یزد صدای انفجار شدید اومد و خونه ها لرزید.
صدا از تفتکوه محل منطقه گردشگری در حال ساخت بام تفت بود که از اول جنگ کلیه نگهبانان و پرسنل را سپاه تخلیه کرده و هیچکس اجازه رفت و آمد ندارد
خبرگزاری‌های محلی میگن موشک بوده و جنگنده اصلا صداش شنیده نشده
آپدیت: صدا و سیما
صدای انفجار در خارج محدوده شهر تفت در استان یزد
———
بروجرد انگار زدن صدای انفجار اومد. دو انفجار پیاپی
بروجرد زدنننن
صداش وحشتناک بود
بروجرد صدای انفجار شدیدی اومد
دو تا پشت هم
آپدیت:
در بروجرد فقط صدای عبور جنگنده شنیدم
اما صدای انفجاری نشنیدم
از باقی همشهریان هم پرسیدم نشنیده بودن.
صدای جنگنده شبیه  جنگ ۴۰ روزه بود که بعدش خبر بمباران خرم آباد اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77454" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77453">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjFUMhOLqejkWUt54ZWeqUnYL09bJd_TQayrGjEH7W-ivFf2gKHKACNXNpv-XLtHTkhVCjuJPWeyfETdr6upx3h58oAD-bcTewGW8wSdm3ZklcfTQ7RJ3deVHO4H-yQQissaVtkMzCQDwjnxmRtI8Zz6JpqRSvjiMbos0TG--WjA0ZJaHwTfAW-AuBOun3Udv7IZzElqH67aDpQvbNdd7buBRS2Ql8JMcWXyVCARk1oqlrQhwuzyVqOzf8HtN6jFeIXSTF7gKkZxkysU3G8ntwV6wIQjvkHKWUsixbss2V3sDXE-MOpmxgwG3SRu0Aja5F-gW3E3MAIA4mZjmJAtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، معاون امنیتی و انتظامی استاندار خوزستان اعلام کرد که ساعت ۲:۵۰ بامداد جمعه، نقاطی در اطراف شهرهای اندیمشک و امیدیه هدف حمله موشکی آمریکا قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77453" target="_blank">📅 03:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77452">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیام‌های دریافتی:
خرم‌آباد ساعت 3:19 دقیقه صدای انفجار شدید.
خرم آباد الان انفجار شدید
همین الان صدای انفجار خرم اباد ۳:۲۰
سلام خرم آباد همین الان ساعت 3:19 دو انفجار شدید
سلام خرم اباد وحشتناک پنجره لرزید
خرم آباد زدن یه حالت لرزش هم داشت
خرم اباد وحشتناک شیشه هامون لرزید
سلام همین الان از خرم اباد موشک پرتاپ شد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استاندار لرستان گفت: یک نقطه از شهر خرم‌آباد دقایقی پیش هدف پرتابه دشمن قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77452" target="_blank">📅 03:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gS0Rv_LMO-p5NgQIJn8KL03xEviXkZpgklb1T5GFAWpjiMdK71rPqV6jftRROuRRba30sTp4qkepb4t73njh6SLI_PoH260N-Q0K-gq2nU5g0Ad4Fhi7qfKUs53Ae3p4OrotZi74oUVYmX6Fd1-6WUT-mP5DthnRl4AyMixP7UUKdPb81MOD9uuuoihLISRD_RNihHXsKvmLrWj95gbFQ4zoRTUYMECHKYNNfbka3uuTsMW4m6Jibenbid4A2Fqz7UpPOm3dGsOkH_Tgx9opSJc2WHYsYYcpcklFExsa-ICYjUfinkMdeMKuT7NC3he2kVbgcPoWSOITaHgByrwC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77449" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B4UuSJPL390DClB_yi7edZZLXgYwEwXMvMBI3f9FMiw6SByhJ-uzkwBsPAT351sVNfucV3jlRiaqK1p6uJmVm-5Wwc0roQe-8IOUP8z-MBiqE-Sejy0lafcFAymokvT08AJcNZVL07WPRnpqn9Hr8NN72iy8tzaXJAU0ANc3kwMZgMQGk5qvOcflGsLiqTTJsKjxkIsvSuQpKHpa8ChDEcXI7fVfaLLlZIIenNoE1Z32BgMZuJTrqPyYuEnMQznlRkDGO7msT8u5rvb4DvKz_wMlcivPhjm2xVVSugaGF7slkEAc2REH7-DK8z5nbJ5CDpjAjHFbmcAaZI9kj-RXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: سیزدهمین شب حمله را آغاز کردیم
ترجمه ماشین:
نیروهای آمریکایی امروز ساعت ۶:۴۵ عصر به وقت شرق آمریکا [۲:۱۵ به وقت تهران]، دور دیگری از حملات شبانه به اهداف نظامی ایران را آغاز کردند.
این سیزدهمین شب متوالی حملات است که با هدف پاسخگو کردن ایران و کاهش تهدیدهای سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77448" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=hidlKxNWHtd5k-wZaqNyLHTH2i7X3U8gQZSHkgg5TLDa39E-nQJNAXN3Y2ViY1ZeK7y6TRWy87-tenTRZ41TYix3cS0X9tNAgclah6nKfn5XVd92tXg45Zkw-ntftX2qG_Zj4Ru6Ba2qDncU4nXKzV4smqlinm7EQgLWYkpM-Nptq0t1YRglAZEsWEtpCsL7DU2reP79dwhXR65v08cPEbzkxQp6U_mpb_v5uXP745lodNa0mhez6pKQR8aHl7bswtNd33lDyyb1tz85rKUSUXIYWKUR4Ok1lonA_XZ35bAfotasUsmZCV-NKXMVPD2dLxoir1GEhM04hIFp-Dv62A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=hidlKxNWHtd5k-wZaqNyLHTH2i7X3U8gQZSHkgg5TLDa39E-nQJNAXN3Y2ViY1ZeK7y6TRWy87-tenTRZ41TYix3cS0X9tNAgclah6nKfn5XVd92tXg45Zkw-ntftX2qG_Zj4Ru6Ba2qDncU4nXKzV4smqlinm7EQgLWYkpM-Nptq0t1YRglAZEsWEtpCsL7DU2reP79dwhXR65v08cPEbzkxQp6U_mpb_v5uXP745lodNa0mhez6pKQR8aHl7bswtNd33lDyyb1tz85rKUSUXIYWKUR4Ok1lonA_XZ35bAfotasUsmZCV-NKXMVPD2dLxoir1GEhM04hIFp-Dv62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
داداش
بندر
زد
همین الان
بندرعباس
سلام بندرعباس همین الان صدای چندتا انفجار پشت هم اومد
ساعت ۲:۴۱ دقیقه صدای انفجار بندرعباس
سلام بندرعباس انفجار های شدید پیایی غرب منطقه ۴
بندرعباس 2 انفجار
سلام وحید بندرعباسو زدن 2:41
بندرعباس ٠٢:٤١ يه صداي انفجار خيلي بلند كه مركز شهر  قشنگ حس شد
سلام بندرعباس همین الان چندتا زدن خیلی بدد برق قطع شد صدای انفجار بد بود
🔄
بندرعباس صدای انفجار بلند ۲:۴۱
2.42 چند انفجار بندرعباس پشت سر هم سنگین
3تا دیگه
٠٢:٤٢ سه تا ديگه پشت سرهم
صدا و موج زيادي داره
سلام وحید بندرعباس انفجار وحشتناک
دوباره داره میزنه خیلی بد میزنه
بندرعباس ۲:۴۲ صدای انفجار دی در پی
دوتا دیگه پشت سرهم زدن
۵ تا انفجار شدید  بندرعباس مجدد منطقه ۴ ۲:۴۳
سلام یه صداهایی میاد بندرعباس فکر کنم صدای انفجاره اما دوره
وحید بندرعباس ۲:۴۲ صدای انفجار بدجور میزنه
ساعت ۲:۴۱ در خونه دوبار لرزید
غرب جزیره قشم
بندرعباس همین الان هفت تا هشت انفجار خیلی قوی داشت
آقا وحید بندر خیلی شدید بود بیش از ۵ تا بیشتر.</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77447" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77446">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=ndNntxJW1XqMUjCEowQddVwwkVIn5vT8XmmwAAwGPVQLbPcDR_aH28GRd15uxjpPVOPyzo-nfHFlvKNvq3VbpJEzIou3H8k8Yd1DcV2bgFnWrPsapIqRrWMQfUEiXaHjZm56eYQ84iABmNmhVfdX9x11bASsHFPp4yHIQsRJmUIqhUupLWidy9I2zwKd8kXQ73lL_dQzAflA5B1NKGAqxQcrey0gOYfHDynEYytnJoR3TegrBjasTS9K4casoOBOmvzQRObAeFR4FDQBC2FtGYgNYkSQsfejQ3SHm26uoycA8qYLzgSANc6Tp5I_WsTzZclAn_cI-z2JnxV9cq_KEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=ndNntxJW1XqMUjCEowQddVwwkVIn5vT8XmmwAAwGPVQLbPcDR_aH28GRd15uxjpPVOPyzo-nfHFlvKNvq3VbpJEzIou3H8k8Yd1DcV2bgFnWrPsapIqRrWMQfUEiXaHjZm56eYQ84iABmNmhVfdX9x11bASsHFPp4yHIQsRJmUIqhUupLWidy9I2zwKd8kXQ73lL_dQzAflA5B1NKGAqxQcrey0gOYfHDynEYytnJoR3TegrBjasTS9K4casoOBOmvzQRObAeFR4FDQBC2FtGYgNYkSQsfejQ3SHm26uoycA8qYLzgSANc6Tp5I_WsTzZclAn_cI-z2JnxV9cq_KEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌‌های دریافتی:
اهوازو زدن
شدید زدن
سلام وحید صدای برخورد اهواز
اول ۳ تا خیلی دور بود
الان هم ۳ تا نزدیک بود
اقا وحید همین الان اهوازو بد زدن
اهواز انفجار ولی دور بود
اهواز ساعت ۲:۲۰ صدای انفجار اومد
اهواز صدای برخورد اومد 2:21
وحید رگباری زدن اهواز
ساعت ۲.۲۰
ساعت ۲:۲۵ یک انفجار شدید اهواز
سلام وحید ساعت ۲:۲۰ اهواز رو زدن
داداش اهواز صدا انفجار قطع نمیشه تقریبا ۲  دقیقس پشت هم داره بمبارون میکنه یجایی رو
اهواز ساعت ۲:۲۱ خیلی زدن بیشتر از ده تا
۰۲:۱۹ اهواز زدن
آقا وحید اهوازو شدید بمبارون کردن هنوزم ادامه داره
ساعت ۲:۲۵ یک انفجار شدید اهواز
انگار یه چیزی خورد زمین و ترکید
انفجارش طنین داشت
چیزی مثل رگبار
انفجار در اهواز 2:25
سلام ۲:۲۱اهوازو زدن از گلستان اهواز پیام میدم دور بود خیلی ولی کاملا صدا و لرزشش اومد
سلام وحید جان، اهواز رو زدن
خیلی شدید بود ساعت ۲:۲۲
سلام اهواز شیشه ها کامل لرزید مثل یه باد شدید بود
🔄
ساعت 02:24 مجددا شروع شد.
مجدد ۲:۲۴ انفجار شدید
یکی دیگه دوباره زد
انفجارش موج داره
ساعت ۲:۲۴ یه انفجار دیگه شدید بود
۲:۲۴ دوباره اهواز زدن
وحید دوباره صدای چندین انفجار
اهواز هنوز داره میزنه
اهواز رو پشت سرهم دارن میزنن
درود وحیدجان، ۴ ۵ تا انفجار عجیب در اهواز رخ داد، انفجارهاش با همیشه فرق دارن، با اینکه دورن و صدای کمی دارن ولی زمین و شیشه‌ها رو میلرزونن به یه صورت دلهره‌آوری
سلام اهواز ساعت ۲:۲۴ دیقه فرهنگ شهریم صداش اومد هرچند کم بود صداش ولی مشخص بود بمبه
انفجار ها توی اهواز همچنان ادامه داره
خیلی شدتش بیشتر از روزای قبله
کل خونه و پنجره ها دارن میلرزن
اهواز زاغه مهمات انفجارات پی در پی
اصلا تمومی نداره
۲:۳۲
۲:۳۳
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77446" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77445">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FAJ7EJEnqR0YY0-Er_X_kUANgYLrFThnXzsu1H4Z0PUaNCS6BkacAsz0zxaot1uQwzboQFSUIgeGG9zMAw0_oT_LNbWVx-PO9H8F5lzsUL7ilbcwt5fu2ShrLns_lVqq2w8f869illOSzA51PltGoIwzTzlbe99kPnx_jWUtTHldYAjMoz3l4pytgFNNl0ujdCyRpHxG-mXg8ko4ODHUzSQdTS3YFrhH4srldDQqS1hac74ItYIV4FdIld5CWTNvadIue2Zi3bhcoQRbrf9l8GC5LC-cgV8uFvXIh4ncV5djgFsX1IKIuXoIhalXYZDD9B6KWzvLzgRbWdJDyiCtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
ترجمه ماشین:
لطفاً این بیانیه را تا اطلاع ثانوی به‌منزله اعلام این موضوع تلقی کنید که
از این لحظه به بعد، هزینه هرگونه خسارت واردشده به کشتی‌ها، محموله‌ها یا هر چیز مرتبط با آنها، از محل پول‌های ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
این خسارت‌ها ممکن است بسیار قابل‌توجه باشند، اما با وجود این، این کار منصفانه و عادلانه است.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77445" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77444">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tWrEmRzwvBXkg0CA-vFX47l5s5PEei6kgvrejIMDf0spjUjhxgjvS57BuRRo73Vj9pOCboNYoQMBcVykwWwvMQAh--upFGu8OpumsssL7IwDvxwgpGIHtm4ezNG6_kLpbtpEhIMHmxS5OLFJs32KBv3F08h8RXNG-uCAQowrvEstMuP9R4b_-iuzubH2BtWcOKrNgNvIi0dAlkfRUsns4mjQI9SZ1StiOg6ukqepYTOWhIVgUSzocrn-DCNfCSkHEpM_JK2h6f1cLpDo7gAkCoTTK32xXlDC6XlCrIiFNYI0NfD6lW72CZz7x00VzFbj3rnh6z584newsYWr9zNQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم: اصابت ۲ موشک آمریکایی به محدوده روستای مسن قشم
گزارش خبرنگار تسنیم:
🔹
ساعت ۲۳:۵۰ دو فروند موشک در جریان حمله دشمن آمریکایی به محدوده روستای مسن در جزیره قشم اصابت کرد.
براساس اطلاعات اولیه، این حمله در محدوده روستای مسن رخ داده و دستگاه‌های مسئول در حال بررسی ابعاد حادثه و ارزیابی خسارات احتمالی هستند.
من یک پیام داشتم ولی اون رو هم ساعت ۲۳:۳۳ دریافت کرده بودم:
سلام وحید جان
ساعت 23.30 صدای دو انفجار شدید  ذوالفقار قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77444" target="_blank">📅 01:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77443">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77443" target="_blank">📅 00:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77442">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=VyHiZMcmkZT3lGGSqV0VtsdPvYZ8KqAfQFNko65Rpz2OZPm84m18t7XW1dUeaju9Ww_-5TkQAvk2yZosxd_-hak7iPXxI5gqBqwzmmS-gB2iHlxT12pyGEBdLbezaiqUG6AH784Ptx9X12oGjBh0pqfHDJFG5d5yjLMVs84hI6Q43TH5uf3kjvJbQMm-gREUTrOTLFTccK39a82Na0LYC64XiZ_Nym32gkPlOyLQ3xmEMytDGCrVFkrLvhe3WRKqRLNZEui8BWK-5cNfnE15BBE_tvRuWhzvrOL8boZAsi4HriCbjGXYdcSJoqGwkzLsjixNRBW1Vij3VthhscWzvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=VyHiZMcmkZT3lGGSqV0VtsdPvYZ8KqAfQFNko65Rpz2OZPm84m18t7XW1dUeaju9Ww_-5TkQAvk2yZosxd_-hak7iPXxI5gqBqwzmmS-gB2iHlxT12pyGEBdLbezaiqUG6AH784Ptx9X12oGjBh0pqfHDJFG5d5yjLMVs84hI6Q43TH5uf3kjvJbQMm-gREUTrOTLFTccK39a82Na0LYC64XiZ_Nym32gkPlOyLQ3xmEMytDGCrVFkrLvhe3WRKqRLNZEui8BWK-5cNfnE15BBE_tvRuWhzvrOL8boZAsi4HriCbjGXYdcSJoqGwkzLsjixNRBW1Vij3VthhscWzvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش‌هایی مربوط به ایران، ترجمه ماشین:
ما در برابر جمهوری اسلامی ایران بسیار خوب عمل می‌کنیم. عملکردمان فوق‌العاده خوب است. آن‌ها دوست دارند کاری بکنند، اما من می‌گویم هنوز آماده نیستند. به مقدار بیشتری از همین رفتار نیاز دارند. هنوز آماده نیستند. نیت‌های شومی دارند.
نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند. اگر همهٔ این کارهایی را که درباره‌شان صحبت می‌کنم، از جمله کارهای مربوط به مراکز دادهٔ شما، انجام دهیم، مگر این موضوع مهم نیست؟ وقتی شروع کنند جوامع را یکی پس از دیگری نابود کنند، نمی‌توانیم اجازه بدهیم حتی به داشتن سلاح هسته‌ای فکر کنند. دقیقاً همین اتفاق در حال رخ دادن است. در دوران من هرگز سلاح هسته‌ای نخواهند داشت.
ضمناً، این کار باید به‌دست دیگران انجام می‌شد. تقریباً سه سال است که می‌گویند ۴۷ سال گذشته، اما این کار باید ۵۰ سال پیش به‌دست رؤسای جمهور دیگر آمریکا یا کشورهای دیگر انجام می‌شد. لازم نبود ما این کار را انجام بدهیم، اما ظاهراً اگر ما انجامش ندهیم، هیچ‌کس دیگری هم آن را انجام نخواهد داد. من انجامش می‌دهم و هیچ‌کس دیگری توانایی انجام آن را ندارد.
ما در دورهٔ نخست ریاست‌جمهوری من بزرگ‌ترین ارتش جهان را ساختیم. کمی بیشتر از آنچه فکر می‌کردم از آن استفاده می‌کنیم، اما اشکالی ندارد.
ونزوئلا را داشتیم. کریس در آنجا کار فوق‌العاده‌ای انجام می‌دهد. هزینهٔ آن جنگ را چندین و چند بار جبران کرده‌ایم. میلیون‌ها و میلیون‌ها بشکه نفت برمی‌داریم و آن نفت به هیوستون و لوئیزیانا می‌رود. خودتان می‌دانید؛ آن کشتی‌ها را می‌بینید که صف کشیده‌اند.
باز هم می‌گویم، هزینهٔ آن را بارها و بارها جبران کرده‌ایم و رابطهٔ بسیار خوبی با ونزوئلا داریم. مردم ونزوئلا اکنون خوشحال‌اند و نمی‌توانند آنچه رخ داده را باور کنند. بزرگ‌ترین شرکت‌ها و بزرگ‌ترین شرکت‌های نفتی جهان وارد آنجا می‌شوند و به شکلی تجارت می‌کنند که هیچ‌کس تصورش را نمی‌کرد.
ما هم سهمی برمی‌داریم؛ باید هم برداریم. آن‌ها هم سهمی می‌برند. بسیار جالب است که اکنون پول بیشتری درمی‌آورند. کریس ارقامی را به من نشان می‌داد. ونزوئلا اکنون بیشتر از هر زمان دیگری پول درمی‌آورد. ما هم پول زیادی درمی‌آوریم و فکر می‌کنم حقمان است.
بنابراین واقعاً اتفاقی بود که [نامفهوم]. یک جنگ یک‌روزه بود؛ یک روز طول کشید. مردم می‌گفتند: «قرار است آنجا برای همیشه گرفتار شویم.»
اما می‌دانید، ما ۲۰ سال در ویتنام بودیم و در آن جنگ هزاران و صدها هزار نفر را از دست دادیم؛ دست‌کم هزاران و هزاران نفر. سال‌ها در افغانستان بودیم. در تمام این جنگ‌هایی که درباره‌شان شنیده‌اید، سال‌های سال حضور داشتیم. این‌ها همان جنگ‌هایی بودند که من آن‌ها را جنگ‌های بی‌پایان می‌نامیدم.
اما این بار چهار ماه است که درگیر هستیم. دیروز روز بسیار غم‌انگیزی داشتم. به دوور رفتم. چهار میهن‌پرست بزرگ آمریکایی کشته شدند. این یعنی ۱۸ کشته در دو جنگ. حتی یک نفر هم بیش از حد است، اما شمارشان ۱۸ نفر است.
در حالی که در ویتنام ۲۰۰ هزار نفر را از دست دادیم. هزاران و هزاران نفر را از دست دادیم. در افغانستان و در هر جنگی هزاران نفر را از دست دادیم. در جنگ کره نیز هزاران نفر کشته شدند. همهٔ این جنگ‌ها سال‌ها طول کشیدند.
ما می‌خواهیم این را تمام کنیم و می‌خواهیم درست انجامش بدهیم. اما باید کاری را که برایش آمده‌ایم انجام دهیم. نمی‌توانیم اجازه بدهیم این افراد بسیار خشونت‌طلب به چیزی که می‌خواهند، یعنی سلاح‌های هسته‌ای، دست پیدا کنند.
[...]
بنابراین فقط می‌خواهم در پایان بگویم که حضور در اینجا افتخار بزرگی است. اکنون می‌روم تا دربارهٔ موضوعات گوناگون صحبت کنم. یکی از آن‌ها جنگ ایران است که باز هم می‌گویم در آن بسیار خوب عمل می‌کنیم؛ بسیار بسیار خوب. می‌گویم بهتر از چیزی که هر کسی انتظار داشت قابل انجام باشد.
نیروی دریایی و نیروی هوایی‌شان را از کار انداخته‌ایم. تمام رادارهایشان و بخش عمدهٔ توانایی‌شان را در زمینهٔ تولید از بین برده‌ایم. توان پهپادی‌شان ۸۴ درصد و توان موشکی‌شان ۹۱ درصد کاهش یافته است.
بعد روزنامه‌ای نوشت: «آن‌ها اکنون در موقعیت قوی‌تری نسبت به چهار ماه پیش قرار دارند.»
نه، این حقیقت ندارد. درست نیست. باورم نمی‌شود حتی اجازه دارند چنین چیزی بگویند. نیویورک‌تایمز نوشت: «آن‌ها اکنون در موقعیت قوی‌تری قرار دارند.»
آن‌ها ارتشی ندارند. نیروی دریایی ندارند. کارشان تمام است. ۱۵۹ کشتی داشتند که همهٔ آن‌ها در کف دریا هستند. ۲۱۲ هواپیما داشتند که همه از بین رفته‌اند. رادار ندارند. پدافند هوایی ندارند. هیچ‌چیز ندارند؛ جز اینکه خشن و باهوش‌اند و هنوز مقداری توانایی دارند.
اما چهار ماه پیش، باور کنید، بسیار بسیار قوی‌تر بودند. متوجهید؟ می‌خواهم خبر واقعی را به شما بدهم.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77442" target="_blank">📅 23:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77441">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
افراد نفوذی در دولت آمریکا سرشان را زیر برف کرده‌اند.
آن‌ها واقعیت‌های میدانی را نادیده می‌گیرند و به نظر می‌رسد فقط روی سال ۲۰۲۸ تمرکز کرده‌اند.
تجاوزگری بی‌فکرانه‌ای که از آن حمایت می‌کنند، تنها باعث خواهد شد رئیس‌جمهور آمریکا برای توافقی که در تلاش برای دستیابی به آن است، بهای سنگین‌تری بپردازد.
Compromised individuals in the U.S. administration are burying their heads in the sand.
They ignore the realities on the ground and seem focused only on 2028.
The mindless aggression they advocate will only ensure that POTUS pays heavier price for deal he's trying to achieve.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77441" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77440">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bztwXLDbaZVKAfXkDeXLpOEfb4XoDWGKTPrQ9hjc0z4Py-kKHIAHus1pLY9B9n6B-laCeh0WK5Y4eoHMFS8BGu8d78WMmlJpk8GKmHFuHOfwOLfl2rzBm5bgCjVBhal7ixtWwJHwloEazZ7AFHieTx6sfD4cy0h-moEXypH_Z45cUYZ4u3VNy3gMtfHc9DEE6j58-fOuiGM4TekqYBhaz_Imvg8pQZ7JKJ9YZxYE2zfM9OxdPCgqsho173eKLxLwV1LORVdZazvrBy-ZZu1D29CkWqBPC_9cxwjZeDcyArYGBBa1zcTFwwB6WyGZEdYUY3XoI54QxFnW8oZJaMn60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
هم‌زمان با پیام‌های دریافتی درباره پرتاب موشک از اهواز
آپدیت:
ارتش کویت پنج‌شنبه شب اعلام کرد که نیروهای نظامی ایران بار دیگر خاک این کشور در حاشیه خلیج فارس را هدف گرفته‌اند.
رسانه‌های حکومتی در ایران نوشته‌اند که هدف این حملات تازه پایگاه علی السالم کویت بوده است.
در همین زمینه ارتش کویت در شبکه‌های اجتماعی از جمله شبکه ایکس خبر داد که موشک‌ها و پهپادهای ایران توسط ضدهوایی‌های این کشور رهگیری شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77440" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77439">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=SzgSPmPfqsS8lxbVzHIa_gdgbsH8iNTGik-vAHZD4lSYyb8N8wIXQjoIaDmphunBpN0HY9h9Wz4A3zAcIQQRJeXl3R9z8N3hu6FvG0zA0D3_eZHY9neAnI3gnjNkuM1ahmZJjZEAlXhYLdplwGQYmc796fLYX2ouaT8RsFtCFLEIdjVVp6Swkqtj9LYsIlhZViuZpbNShnpKSzIz7k5CtMXhpx9SpOf_olm80VFlA6iV6UKD26HX0ALLe-1Vjh-LHzD2R6KYsXpGje01BcwCRUINna6ev-rXrHE06DqrSMZUZzny8fSjZI-FcDMJv6yPHmhbjx_TBQfxeIOdtxD7BEHi6QQ9xs1JuB_Pk2XaXnfzJfpPYF60xYIFrQfYVKRWRgMTR8g6a6luajsMhtRagfzr2NvDFhh_5Ihocc5Y_77maEowrwe6ZTZG6LZRyibx2yIVLGJVRjV8dqHW4MpKBoUaeK-BjX8YNrPmaIOuAeAWxdMn_Pf83S-CiH6En8hO3PA2TCT5juV28Ns0W29fXUGyfzCVD7Ie7KA_8mRfKzfn5ElhxXriRgHJ5T8-3U7TikCF3hRFQTFWqRmG4zoCn93mbmUWvzjVEr7nNNLNbCjbWlD5ilT1dIDZ8EXgW1es4ZZYI2fgXJUK7a5dNKfcUKoeNJNyRwzLWmQtCRLRkOs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=SzgSPmPfqsS8lxbVzHIa_gdgbsH8iNTGik-vAHZD4lSYyb8N8wIXQjoIaDmphunBpN0HY9h9Wz4A3zAcIQQRJeXl3R9z8N3hu6FvG0zA0D3_eZHY9neAnI3gnjNkuM1ahmZJjZEAlXhYLdplwGQYmc796fLYX2ouaT8RsFtCFLEIdjVVp6Swkqtj9LYsIlhZViuZpbNShnpKSzIz7k5CtMXhpx9SpOf_olm80VFlA6iV6UKD26HX0ALLe-1Vjh-LHzD2R6KYsXpGje01BcwCRUINna6ev-rXrHE06DqrSMZUZzny8fSjZI-FcDMJv6yPHmhbjx_TBQfxeIOdtxD7BEHi6QQ9xs1JuB_Pk2XaXnfzJfpPYF60xYIFrQfYVKRWRgMTR8g6a6luajsMhtRagfzr2NvDFhh_5Ihocc5Y_77maEowrwe6ZTZG6LZRyibx2yIVLGJVRjV8dqHW4MpKBoUaeK-BjX8YNrPmaIOuAeAWxdMn_Pf83S-CiH6En8hO3PA2TCT5juV28Ns0W29fXUGyfzCVD7Ie7KA_8mRfKzfn5ElhxXriRgHJ5T8-3U7TikCF3hRFQTFWqRmG4zoCn93mbmUWvzjVEr7nNNLNbCjbWlD5ilT1dIDZ8EXgW1es4ZZYI2fgXJUK7a5dNKfcUKoeNJNyRwzLWmQtCRLRkOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجریان فاکس‌نیوز، متن زیرنویس، ترجمه ماشین:
مجری:
بیایید نگاهی بیندازیم به نیروگاه‌ها و مکان‌هایی که ممکن است بتوانیم هدف قرار بدهیم. لوکاس، وقتی به این‌ها به‌عنوان اهداف احتمالی نگاه می‌کنی، فکر می‌کنی اول از همه کجا را ممکن است بزنیم؟
لوکاس:
خب، نمی‌دانم نخستین هدف باشد یا نه، اما نیروگاه دماوند ۴۰ درصد برق تهران را تأمین می‌کند. نیروگاه هسته‌ای بوشهر هم احتمالاً هدف قرار نخواهد گرفت. روس‌ها آن را ساخته‌اند و هنوز هم اورانیوم با غنای پایین در اختیار ایران می‌گذارند.
مجری:
چون، لوکاس، باید بگوییم که منفجر کردن یک نیروگاه هسته‌ای خطرهایی دارد.
لوکاس:
بدون تردید. میدان گازی پارس جنوبی هم روی بزرگ‌ترین میدان گاز طبیعی جهان قرار دارد. نیروهای اسرائیلی در ۱۸ مارس، در آغاز جنگ، آن را هدف قرار دادند و ایران هم با حمله به بخش قطری همین میدان گاز طبیعی پاسخ داد.
مجری:
اگر بخواهیم در همان تنگه‌ای که آن‌ها در آن به کشتی‌ها حمله می‌کنند پیام بفرستیم، آیا آنجا جایی نیست که باید سراغش برویم؟
لوکاس:
چرا؛ فقط سؤال این است که پاسخ ایران چه خواهد بود. دیده‌ایم که ایران تلافی می‌کند. تأسیسات گاز طبیعی قطر و میدان‌های نفتی امارات، نگرانی اصلی همین است.
مجری:
یعنی اگر ما یک نیروگاه را بزنیم، آن‌ها هم پاسخی مشابه خواهند داد؟
لوکاس:
بی‌تردید. تمام این مدت ماجرا همین مقابله‌به‌مثل بوده است. نکته قابل توجه درباره اسرائیلی‌ها این است که آن‌ها پاسخ‌هایی نامتناسب می‌دهند. احتمالاً یکی از دلایلی که اسرائیل دوباره وارد جنگ نشده همین است. ایران از اوایل ژوئن به اسرائیل حمله نکرده است.
مجری:
ارزیابی تو از شیوه‌ای که اکنون عمل می‌کنیم چیست؟ فکر می‌کنی پاسخ ما نامتناسب است یا می‌توانست نامتناسب‌تر باشد؟
لوکاس:
پاسخ ما نامتناسب نیست. نکته قابل توجه این است که نیروهای آمریکا، پس از آنکه یک پایگاه آمریکایی در اردن هدف قرار گرفت، به پادگان‌های ایران حمله کردند؛ همان حمله‌ای که سه سرباز ارتش آمریکا را کشت.
مجری:
پس این همان نیروگاهی است که ممکن است هدف قرار بدهیم. این مهم‌ترین مورد است. برویم آن طرف نقشه؛ اینجا «کوه کلنگ» یا Pickaxe Mountain است.
لوکاس:
ارزیابی اطلاعاتی آمریکا این است که ایران احتمالاً چند روز پیش از عملیات «چکش نیمه‌شب» در یک سال قبل، بخشی از اورانیوم غنی‌شده خود را از فردو به کوه کلنگ منتقل کرده است.
این محل بسیار عمیق‌تر از دیگر تأسیسات هسته‌ای است. همچنین اینجا کوه‌های زاگرس است و با سنگ دولومیت بسیار سخت روبه‌رو هستیم؛ بنابراین حمله هوایی به آن بسیار دشوار خواهد بود. این یکی از دلایلی است که شاید از نیروی زمینی استفاده شود.
در واقع، چنین مأموریتی برای نیروهای مأموریت ویژه ارتش آمریکا است؛ نیروهایی مانند دلتا، تیم ششم سیل و اسکادران ۲۴ تاکتیک‌های ویژه نیروی هوایی.
ریسک ماجرا این است که هیچ‌کس دقیقاً نمی‌داند داخل آنجا چه وضعی دارد. هیچ نقشه فنی‌ای از داخل کوه کلنگ وجود ندارد.
مجری:
درست است. همین را می‌گوییم.
لوکاس:
آژانس بین‌المللی انرژی اتمی هرگز به این محل دسترسی نداشته است. بنابراین با اطمینان نمی‌دانیم آیا سانتریفیوژها و اورانیوم با غنای بالا به کوه کلنگ منتقل شده‌اند یا نه؛ اما این محل زیر نظر است.
شنیدیم که رئیس‌جمهوری ترامپ گفت به‌زودی کوه کلنگ را هدف قرار خواهد داد. بمب‌افکن‌های B-1 را دیده‌ایم که از بریتانیا پرواز کرده‌اند و البته بمب‌افکن‌های B-2 از پایگاه هوایی وایتمن در میسوری برای همان پرواز دور دنیا که در عملیات «چکش نیمه‌شب» دیدیم، برخاستند.
مجری:
و نطنز هم هدف قرار گرفته، درست است؟
لوکاس:
نطنز هدف قرار گرفته است. فردو و اصفهان هم هدف قرار گرفتند. این‌ها سه محلی بودند که در عملیات «چکش نیمه‌شب» در یک سال قبل هدف قرار گرفتند. با این حال، کوه کلنگ تا این لحظه دست‌نخورده مانده است.
[جملاتی که در ویدیو هست ولی برای جا شدن متن در پست، اینجا نقل نکردم.]
مجری:
و حالا تا جایی که می‌دانم، این نیروگاه برق [دماوند] دو میلیون نفر را تأمین می‌کند.
لوکاس:
بله.
مجری:
و خارج از تهران قرار دارد.
لوکاس:
اگر رئیس‌جمهوری بخواهد پاسخی بدهد که تا حدی نامتناسب تلقی شود، نیروگاه دماوند را هدف قرار می‌دهد. باز هم می‌گویم، این نیروگاه ۴۰ درصد برق تهران، یعنی برق پایتخت، را تأمین می‌کند.
تنها سؤال این است که آیا می‌خواهید برق میلیون‌ها ایرانی را قطع کنید که با آرمان آمریکا همدلی دارند؟
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77439" target="_blank">📅 21:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77438">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6KNEuKnFq93aSnSJclcBbgz06HfKToOehyr4RWUxDX5KzGrV7gTSMqEJi6oKEG7DFfIt3s-chIobRVUvoA2dwEjczvmzpIZeXVh1nYjPaTr1zB9In2fRke1Qye9zZmTzePeQh1LUD3XJELaa-4h9YtH-TC_PU2Gw35Iv8hg8ANkpG5P6Oa6LHr6vuYXcTaCIfAWZ50t23FYUL2xXwb6itRKo9rirlZBHeazpdh6RgFw3FnKbycia0fcvEhF23a3IFujFyNhtuflplfWGoZJlxepdS8X9_PIu2T8LRH4nmZ1tuMUIEqzAoSzJ05F_-ObsVmPIFzP2LDpm7M7ZWhizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش کویت عصر پنج‌شنبه اول مرداد اعلام کرد که یکی از گذرگاه‌های مرزی این کشور با عراق برای دومین بار در یک روز، هدف حمله پهپادی قرار گرفته است.
ستاد کل ارتش کویت با انتشار بیانیه‌ای در شبکه اجتماعی ایکس (توییتر) اعلام کرد: «گذرگاه مرزی العبدلی عصر امروز بار دیگر هدف حملات پهپادی دشمن قرار گرفت که خسارات مادی بر جای گذاشت، اما هیچ تلفات جانی نداشت.»
ساعاتی قبل کویت اعلام کرده بود که آتش‌سوزی ناشی از حمله صبح پنجشنبه، مهار شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/77438" target="_blank">📅 21:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77437">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oE5wm1pjQ9sK7LUFWXvtf-6XZjn-eJSamdsCgIwmZy5Nb_NfwoWw87bczaQ2VgUY7gzoaH28cf1Ld5tMm6Qy-_ja7uOFy34er3lF3g6D8-nvqKkWZzhdFsqO3Rb9HDuA1gucepxKrgjDco72BWFuUF6wJHjjXIlzYiXWmci8fFQBWejnSUVJ-8GH-LH6orefSjmd2FBepvv-WGLVG7ZCEVx8D9rQc3I37OtRLNcNhBRJpHZSrc-F5E5w38PZWGaKpjJ-4lvmF8haS49VKiNTS42d4TQjPIPf67_K5-wADW8wW08hAX_eXgF62Zw2cqb3kO4u6snUp4rJ4i8Cr0JR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره
این پیام‌های دریافتی
:
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد ساعت ۱۸:۵۰ عصر پنجشنبه در پی حمله ارتش آمریکا، یک فروند موشک به نقطه‌ای در ساحل شهر سوزا در جزیره قشم اصابت کرد.
تسنیم نوشت که بررسی ابعاد حادثه و میزان خسارات احتمالی از سوی دستگاه‌های مسئول در حال انجام است.
خبرگزاری صداوسیما نیز از شنیده شدن صدای انفجار در قشم خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77437" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77436">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcc5tcyYeHDKtAl1Xs99GkkJrmIrSUqPBpTZ4ikLiBHSIFg4FIO5xBMninWFJZyPYktl5qMxM7dtT5L01bBbJT-ir_M9OGbBIAyCWtly4blROpv1w7n55wjTogLNqLtTPmQmmJpZe6d1s0DiSsnbZZI4_1x06isr9Jb0Ntl08nNYLG5Ka7GyY7wAJW9sbJfMD1NlxMXSu69KHaJKUW0i5jnALTSWjvvEyyiRScbhF2AAGLyE_Pxk3q0iylotOIHZkGs6FWE1QaCBQXmCkqMjWtlUbaHURMN2bFmfOFtCu_fdC8oVzGersO8e4nQ7Dd_5As9G8L_qXGIlU5FpXBA39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران روز پنج‌شنبه ادعا کرد که پایگاهی را در خاک بریتانیا که بمب‌افکن‌های ب ۱ آمریکا از آن بلند می‌شوند برای حمله «هدف مشروع» می‌داند.
وب‌سایت اکسیوس پیشتر به‌ نقل از مقام‌های دولت آمریکا نوشته بود که ارتش این کشور در دور جدید حملات به ایران، روز سه‌شنبه برای نخستین بار از یک بمب‌افکن دوربرد «ب ۱» برای حمله به اهداف متعلق به سپاه پاسداران انقلاب اسلامی استفاده کرده است.
اکسیوس نوشته بود که بمب‌افکن به‌کارگرفته‌شده در این حمله از یک پایگاه هوایی در بریتانیا به پرواز درآمده بود. اشاره این سایت خبری به پایگاه فِرفورد در جنوب غربی انگلیس است که در حال حاضر ۱۸ فروند از بمب‌افکن‌های ب ۱ آمریکا در آن نگهداری می‌شود.
حال سپاه پاسداران در پیامی این طور نوشته است:‌ «هر پایگاهی که برای حمله به خاک ایران از آن استفاده شود برای ما هدف مشروع است.»
سپاه در پیام خود ادعا کرده است که در پی ازسرگیری حملات، آمریکا ابتدا با موشک‌های کروز از روی ناوهای خود در اقیانوس هند به ایران حمله می‌کرده، اما در پی خالی شدن انبار موشک این ناوها، به استفاده از بمب‌افکن‌های خود در بریتانیا روی آورده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77436" target="_blank">📅 19:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77435">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LFlr-lrYISUW1ltjJaIOyfcsrbXdI6amGXyFziu3OZO0gqfbp624W_kJEvygG5JXaFRhqR7hCEUaiKIdrmgQ8k5wyjSymRVIdclNvrtFreWLwID6Zh5WNgjRn90FLBA471GNOr6DpXGS0OrgMlI_k3PkuB3YJHtGyhiPkmeCmNUwxosiMKe1Ee5SlUflr11V9Z6dxCgcrpWDJFQWwYvrybAe_bdl0XCqgYChjxHY2FAAiB3Uhi77c0870sQvADlS56DBhr-dIQ_9MYFe3--POji7vqGsvy817fB-W6h20Pwkw5TrhRNw887Trl7zylWNYuqJtGh58ieGjWtEZEFiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: ترامپ می‌گوید به تصمیم‌گیری درباره «حمله‌ای عظیم» علیه ایران «نزدیک» شده است
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنجشنبه به آکسیوس گفت که به‌طور جدی در حال بررسی ازسرگیری عملیات رزمی گسترده در ایران است؛ از جمله حملاتی که از عملیات «خشم حماسی» بزرگ‌تر خواهد بود.
چرا مهم است: ترامپ در مصاحبه‌ای کوتاه اذعان کرد که چنین تصمیمی پیامدهایی خواهد داشت و تأکید کرد که هنوز تصمیم نهایی را نگرفته است.
ترامپ برای تصمیم‌گیری خود مهلتی تعیین نکرد. دو مقام دیگر آمریکایی نیز تأیید کردند که هنوز هیچ تصمیمی گرفته نشده و هیچ دستور تازه‌ای به ارتش داده نشده است.
تشدید تنش‌های کنونی تاکنون باعث شده قیمت نفت از بشکه‌ای ۱۰۰ دلار فراتر برود. بازگشت به جنگی تمام‌عیار در آمریکا به‌شدت نامحبوب است.
آنچه او می‌گوید: رئیس‌جمهوری آمریکا گفت: «من در حال بررسی یک حمله عظیم هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام شده است. به تصمیم‌گیری نزدیک شده‌ام. ما کاملاً برای آن آماده‌ایم.»
ترامپ گفت اسرائیل «اگر از آن‌ها بخواهم، ظرف دو دقیقه وارد عمل می‌شود»، اما افزود که برای آغاز عملیات تازه علیه ایران «به هیچ‌کس نیاز نداریم».
او همچنین گفت پیوستن اسرائیل به این حملات «پیامدهایی» خواهد داشت و تلویحاً به احتمال تلافی ایران علیه اسرائیل اشاره کرد.
تصویر کلی: ترامپ گفت ایرانی‌ها «می‌خواهند مذاکره کنند»، اما در حال حاضر آماده توافق نیستند.
او گفت: «هنوز به اندازه کافی درد نکشیده‌اند.»
دو منبع منطقه‌ای مطلع از تلاش‌های میانجی‌گرانه گفتند رهبری ایران تازه‌ترین پیشنهاد ارائه‌شده را نپذیرفته است.
یکی از آن‌ها گفت: «داریم تلاش می‌کنیم، اما ایرانی‌ها همکاری نمی‌کنند.»
محور خبر: آمریکا طی ۱۲ روز گذشته حملات خود را تشدید کرده است تا حملات ایران به کشتی‌های تجاری در تنگه هرمز را متوقف کند.
ایران تاکنون هیچ نشانه‌ای از تمایل به تغییر مسیر نشان نداده و خود نیز حملاتش در منطقه را تشدید کرده است.
شورشیان حوثی مورد حمایت ایران در یمن حمله به کشتی‌های سعودی در دریای سرخ را آغاز کرده‌اند؛ اقدامی که تنش‌ها را در یکی دیگر از مسیرهای حیاتی انتقال نفت تشدید کرده و بازار جهانی انرژی را بیش از پیش بی‌ثبات کرده است.
ترامپ در حساب خود در تروث سوشال نوشت که اگر حوثی‌ها بار دیگر به کشتی‌ها در دریای سرخ شلیک کنند، «ایالات متحده ایران را مسئول خواهد دانست».
او گفت حوثی‌ها نیروی نیابتی ایران هستند و بنابراین «مجازات نظامی سنگینی علیه ایران و البته خود حوثی‌ها اعمال خواهد شد».
آنچه باید زیر نظر داشت: ترامپ جداگانه گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، قصد دارد هفته آینده در مراسم وداع با سناتور فقید لیندزی گراهام در واشینگتن شرکت کند.
ترامپ گفت: «روابط با بی‌بی بسیار خوب است. اگر او اینجا باشد، با او دیدار می‌کنم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77435" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77434">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید قشم صدای انفجار
الان دریابانی سوزا رو زد وحشتناک
جزیره قشم ۱۸:۴۰
ساعت 18:40 دقیقه قشم صدای انفجار شنیدیم
وحید جان قشم صدای دو انفجار از راه دور اومد ..
🔄
صدا و سیما:
شنیده شدن صدای انفجار در سوزای قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77434" target="_blank">📅 18:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77433">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xtf_6pPZI-z8ewLV0ykhRfaaKnEk2Gu35bD1NaOJ1ZqNysI629CYGv4zoFLjP9u3QhPgO4aDJtG7JD4HJ00qDn5V3b2RY473-ohevwZJIoEbmFOJwrFi3_P0cf7KvtAP6d4f_0qDFp0t0osvgSekbdI-ORDurr6CDwb4-a-WAb-D0AYsvS3KYeVwnM0XA6lXDLUuwVoEkR_xOfAcyNkr9VV-zq--q6V4AjWdu7W-t-Rc6mnXsjOMsJKiCmUlIuPztbTnvDz_WAIvC5J2v0X6V9pdNHKxTBqpe7Y3ZHOqujyaT8OQzXjrn5hLJ5I_dbxh8wEJq5PD60Rm_KfVUFzxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
می‌خواستند ایران را تنبیه کنند.
در عوض، خودشان را با قیمت سه‌رقمی نفت تنبیه کردند.
استراتژی ۱۰ از ۱۰
👏
👏
👏
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77433" target="_blank">📅 18:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQRCjR9l59Ey84iEPSnbwWeSQ0dVjT4eXtBBPzds5eTOv2MZ6nhSism66Jfb6PSclhU7crts2yn90SFS705WR3PwjD7GKX-ElL2LQyr-PGND4hU1ubq-5Z4bnqKfl3Idz07COgzwgVFTLFess2UlZXo5_62Nyrfm-n6SByoZoOHV07SdfSAO6NrbY_WfmgOvJZ7DRWG5QIdbUO57doHISkxS6XdRAIZTzQy55hmUoizv9xI--bjGSHtiHecNaiudR9P6G9fC1o4mzqYh3n9PTPL9n74jLRKhrBrIey7id_UOUR8RbhCqH4HlU18hXOh_xACcxdRtDSUoYGXMoa6hWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ روز پنجشنبه اول مرداد، در پیامی در شبکه اجتماعی تروث سوشال با یادآوری حملات نظامی ایالات متحده علیه حوثی‌ها که سال گذشته انجام شد، نوشت: «حوثی‌ها از آن زمان و در جریان درگیری با ایران، رفتار مسئولانه‌ای داشتند، اما متاسفانه با تیراندازی شب گذشته به دو کشتی عربستان سعودی، بار دیگر دست به حملات زده‌اند.»
ترامپ هشدار داد که اگر این اقدامات تکرار شود، آمریکا جمهوری اسلامی ایران را به عنوان حامی حوثی‌ها مسئول خواهد دانست. او تاکید کرد که در این صورت، مجازات نظامی بزرگی بر ایران و همچنین خودِ حوثی‌ها تحمیل خواهد شد؛ گروهی که به گفته او، تا پیش از این حرفه‌ای و هوشمندانه عمل کرده بودند اما اقدام اخیرشان مایه «تاسف» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77432" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g710Puled_Fl4WVQwvbPeYkDF0iG03UgFpRF46bSwaV3KQv6gVBcwSYVDa9FOH4-WRtnWK4HAunOgAl3_tVfcnSweBfmwBF7y9yxpgTGcKGvSg_MIK-VuupFENhW9ER27MgshAr4MOcVGh9RTBGLoE6uxoTgcvmxlnQ7LyCd3py1TnoCbbzd65873qFEX7DYQn05KyRu524hCYjB34FGQWQfn2qjJ6Q9bd676RrU24dCSMvZnrzAp_0fic_Ihel37wOZILGMs-qJazm0l0RNP1GV_Z4yf2y47rf110E0URNKpUyQ8XC7qLuR0vfROt-hvzN_PS8nkFkwBnfApw40OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد امیرحسن اکبری‌منفرد، زندانی سیاسی ۲۷ ساله محبوس در زندان اوین، با حکم شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، از بابت اتهام «بغی» از طریق عضویت در سازمان مجاهدین خلق ایران به اعدام محکوم شده است. بر اساس این گزارش، حکم دو روز پیش به او ابلاغ شده است.
هرانا همچنین گزارش داد امیرحسن اکبری‌منفرد زمستان ۱۴۰۳ همراه با پدر، برادر و خواهرش در کرج بازداشت شده بود و سه عضو دیگر خانواده بعدا با تودیع وثیقه آزاد شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77431" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mRKJ4_sq2-Sz504app93bFnVg1xOv5iEBX4RQVIfUwxXehiMfwWUQ9ROilh75ISxfGZPTlCzrU77TeXn7k8E3jiZk2r_Ocs1HjCIK-AKNZRnDz0L_3uSnVps326icxfNGn1OOj7WcLU4AA1kwJ0Ao2zebwbONip7WX03Ht-zlvnbt3kIpswb_kjAnNbK_FJNgRCOvkbjgD2TIyEvq8LthtaW8GntDgl0uuCkpzcbfID2HtGiEtKPxoIWOQuBfO2mqk852GPu5VP53nOWdMNJFiQUzSbcMLjcVFBSRiTlBrt0WsPL3urDvNe_m2dWyGGOI85uYUxf4qAmyZsZiyj_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qZuzzYY5SMoQksvyv-4OuWjIhqHCUv9pfzmh_styR4fswceZcmaReLbcIXm5eaY6KjNOtL1pwuEnbNO0Z2Ip52iQbwZIkn4RWqHeob5Smgiw8xZMpEBbwpnz-Zv85e-rS0KrA1n-t4446LdnRbrFm73p6tbzdSNQVoXblfpm-2pkT1SzjXiub3156vHU40j03TzaRp1HHwSk-6Pu2MJlF0G_xUm-DLRIQo0M1_VTsgb8oOjtYiwNTPvohKSFOsgr0IusHZygKxGNUXx7Pwf5PsYrgIhn1uVl8LDUNPY-c3eX8X9jcYzwrwBC8yteUdbYmmsTNjWjnOuDV2ZRE9gr-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اول مرداد ماه، در پیامی در شبکه اجتماعی ایکس اعلام کرد توافق هسته‌ای غیرنظامی میان وزارت انرژی آمریکا و عربستان سعودی تصویب خواهد شد، اما این توافق مشروط به پیوستن ریاض به توافق‌های ابراهیم است.
ترامپ در این پیام با اشاره ناگهانی به «غیرنظامی» بودن برنامه هسته‌ای ایران نوشت: «توافق هسته‌ای غیرنظامی که میان وزارت انرژی ایالات متحده و عربستان سعودی در حال انجام است، تنها به استفاده‌های غیرنظامی، مانند برنامه‌هایی که ایران، امارات متحده عربی و دیگر کشورها دارند، مربوط می‌شود. اما این توافق کاملا مشروط به پیوستن عربستان سعودی به توافق‌های ابراهیم است.»
رئیس جمهوری آمریکا کرد در این توافق «هیچ غنی‌سازی مواد [هسته‌ای] وجود نخواهد داشت» و آمریکا با تاسیسات هسته‌ای غیرنظامی و بدون غنی‌سازی مخالف نیست
@
VahidOOnLine
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل پنج‌شنبه اعلام کرد پیوستن عربستان سعودی به توافق‌های ابراهیم، تحولی تاریخی در مسیر صلح در خاورمیانه خواهد بود.
دفتر نخست‌وزیر اسرائیل افزود اقدام نظامی مشترک آمریکا و اسرائیل علیه جمهوری اسلامی و تضعیف محور «تروریستی» تهران، زمینه را برای گسترش دایره صلح فراهم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77429" target="_blank">📅 17:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVdcCAfIGLHPelwPx5soE2d-hY9qWZIoRs3MOhuL3zMuO3D-jKPzojCdV54yuJiQHfjREGGAUgUyCt97WL2dKf90orXcoW5ND-coy4LkcQQ3h-wXs1VzvzrrBhWDJB6EdKN6Pu3OKj-rX3PYhltcEB3QMew8XKT-6B6nxxxMgw6IYzjDDFZ__bENrKweV-yiKkUhupqIfdzoZVuLiGJVDfwhjO0yFI9rK88OoV8-YKRWEDiA1FIu_cricBbcHB9A2kIPI9qDHKFaHmh7EnILpdZeLSbm5GF_hPkVPgLzStJ9n6YNGke9SkyiS7vXpmkUWI2z2yaoDV_s9BdpXMH1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایلنا در گزارشی از ادامهٔ بحران کم‌آبی در زاهدان و برخی مناطق استان سیستان و بلوچستان خبر داده و نوشته است که شماری از شهروندان در برخی محله‌های این شهر با قطع آب تا سه یا چهار روز متوالی روبه‌رو هستند.
بر اساس این گزارش که روز پنج‌شنبه یکم مرداد منتشر شد، بسیاری از خانواده‌ها برای تأمین آب ناچار به خرید آب از تانکرهای خصوصی هستند و برای هر بار پر کردن مخزن خانه بین یک تا یک‌ونیم میلیون تومان پرداخت می‌کنند.
ایلنا همچنین به نقل از شهروندان گزارش داده است که برخی خانواده‌ها به دلیل ناتوانی در پرداخت هزینهٔ خرید آب از تانکرهای خصوصی، ناچارند چند روز را تنها با چند دبه آب سپری کنند.
محمدرضا کوچک‌زایی، عضو شورای اسلامی شهر زاهدان، نیز در گفت‌وگو با ایلنا با تأیید بحران کم‌آبی گفته است این شهر با کمبود حدود هزار لیتر آب در ثانیه، معادل نزدیک به یک‌سوم نیاز آبی خود، روبه‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77428" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77427">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCzsMAerUoe4EMN02UvEmqUMZxoNEImZHcCtjJk-Hw2Ro-4HuU5j5X5G_Xyz5KkcjxgpugW4fWMDNuf58FAvNksA9JOqBnVzqDPyIy_orJNZAdPWx2bSqxIL0B0HeAKZAWuDZL_MLwUuByiZHSk_x9Eqs-9Trw6EkIt0Qo5bVMrIIKeamEAJHxEv5wviALJ_-xsmxXVXH2u2jjasYQdNDrh70MSmCX-dK_UVqv9Mrk3RnbUoJ-BTF1nUyWucbtGq4acIoxstM7J3CrG4y5kasX3HtG0_wTRmqyHJ6AXyUYOj3DS7-V6QrW4n6eXrS4kjC_kQgvmuLwrs4X1FCeN7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما و خبرگزاری تسنیم، روز پنجشنبه یکم مرداد ماه از شنیده شدن صدای چند انفجار در شهرستان کنارک در استان سیستان و بلوچستان خبر داده‌اند.
خبرنگار صدا و سیما در گزارش زنده اعلام کرد، صدای پرواز جنگنده‌ها نیز در این منطقه شنیده شده است. به گفته این منبع خبری،َ انفجارهای روز پنجشنبه، اولین حملات آمریکا در طی ۲۴ ساعت گذشته به این شهرستان بوده است.
@
VahidOOnLine
من هم حدود ساعت ۱۰ صبح پیام‌ها و عکس‌های مختلفی درباره کنارک دریافت کرده بودم + کلی پیام از چند شهر دیگر درباره پرتاب موشک
پیام‌های زیادی هم از دزفول و اندیمشک داشتم که در اون مورد پیش‌تر اعلام شده بود قراره  مهماتی کنترل‌شده منفجر بشن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77427" target="_blank">📅 17:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77426">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNUwDTNwmMKT-98GWsL8HplPLYtJkzoPvFB7xuu8cdh0pims-2krRM-6TxIv3ezYmstJkN0IIawDMNLwNCWh0pJcjWuqUH9zyhUZ28i24umbbJOzUHbIiAuwqBkEOw9jheL7VpIg18V2sqEWyC-g3tvoPjF5bTNYXq3i8kE9SHsISRf-KSnJ1Tj4QHYFoCfsRxKFEG-1gQOEg-bTVIROZXvVx5TcilN5l9B_KDCCM54QzKXpk9aPBl1umurlh2PvmOBalusgKc2FBTLXXj63-oLNXBj4MndU8m0ViAzonEQpasoeqNQHtSM0_4Li6V_LGZiN5EB1nM1RV_dM3QBzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماری
از داوطلبان آزمون کارشناسی ارشد در شهرستان‌های بستک و بندر خمیر استان هرمزگان به‌دلیل تخریب پل‌ها و بسته شدن مسیرهای ارتباطی پس از حملات آمریکا، از حضور در جلسه آزمون بازمانده‌اند. به گفته آن‌ها، با وجود اطلاع مسئولان از وضعیت منطقه، هیچ راهکار جایگزینی برای برگزاری آزمون یا انتقال داوطلبان ارائه نشد.
کانال تلگرامی «
دانشجویان متحد
» خبر داده است که شامگاه ۲۶ تیرماه ۱۴۰۵ و هم‌‌زمان‌‌‌ با برگزاری آزمون کارشناسی ارشد، پل‌های محور بستک–بندر خمیر–بندرعباس در حملات پهپادی سنتکام هدف قرار گرفت و مسیر ارتباطی این دو شهرستان با بندرعباس به‌طور کامل مسدود شد.
در حالی که حوزه امتحانی داوطلبان این مناطق در بندرعباس تعیین شده بود، بسته شدن جاده‌ها باعث شد هیچ‌یک از آن‌ها نتوانند خود را به محل برگزاری آزمون برسانند.
به گفته این داوطلبان، آن‌ها تا آخرین ساعات پیش از آزمون بارها با اداره راهداری و دیگر نهادهای مسئول تماس گرفتند، اما هیچ راه‌حلی برای انتقال یا تغییر حوزه امتحانی در نظر گرفته نشد.
این دانشجویان می‌گویند ماه‌ها برای شرکت در آزمون آماده شده بودند، اما در نهایت به‌دلیل شرایط جنگی و نبود تدبیر مسئولان، فرصت حضور در کنکور را از دست دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77426" target="_blank">📅 17:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77425">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phpu1rMkP-ZCi6WblI09HfZrR391GyOvCg1iwvw8mBQJDDsylEjxzff4304lILkyo7cX5CLFi6FsGayh9WG2tu3VllSLafHF6mADvPY4NumrYC9xp-ae6kBJHRQTN4Yke76Ak-zPWj_w6hh9BrYTJDUABC2Y9VxQYXfj4IICUG39_2JBLDkjxuwiT-5xlIfpRiSyj9mh_6KLfI0RYf68pzJxDpbgcJ8gjmxHbfzbGC0SpHN9BIjAzOcc7a_AtAt1OdWD1qVnY0VJFRESO6UxFV0fX5o0oN_3j0FuMmdTcBkWwqtpfoAYNHJQIJ4fBiSy3WE3YI8Z0yyhhf98FzvLQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا، در حاشیهٔ نشست آسه‌آن در مانیل، با تکرار اظهارات پیشین خود مبنی بر «آماده نبودن ایران برای توافق» گفت: «آن‌ها هزینهٔ این موضوع را خواهند پرداخت.»
مارکو روبیو روز پنج‌شنبه یکم مرداد گفت «هزینهٔ ایران هر شب بیشتر می‌شود تا زمانی که به خود بیایند» و افزود: «با وجود جسارت ایران، آن‌ها به‌شدت در عذاب‌اند و این رنج همچنان ادامه خواهد یافت.»
وزیر خارجه آمریکا در عین حال ابراز امیدواری کرد که حکومت ایران «احتمالاً به‌زودی» آمادهٔ توافق شود، اما تأکید کرد در حال حاضر به‌وضوح آمادهٔ توافق نیستند، «حداقل نه توافقی که حاضر باشند با آن کنار بیایند».
روبیو در پاسخ به سؤالی دربارهٔ اظهارات اخیر دونالد ترامپ دربارهٔ پرداخت هزینه از سوی ایران در ازای کشته شدن سربازان آمریکایی و حمله به کشتی‌ها در تنگهٔ هرمز نیز گفت سیاست ترامپ «سر در برابر چشم است و ایران هزینهٔ سنگینی خواهد پرداخت.»
وزیر خارجهٔ آمریکا همچنین با ابراز امیدواری نسبت به توقف حملات حوثی‌های یمن گفت: «امیدوارم آن‌ها تنش‌زدایی کنند، ایران آن‌ها را فریب داده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/77425" target="_blank">📅 17:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77424">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcqIjIcREXWA2w7oNL4MU25OdjUiMZhaClkEIIFbDdRChEDhsDsrPpxoxLSJrlAUpIOMW0GvpSgQFfB91TdIoVotUV1n4fqBNWMnKv-Qb8TV-zhpnpxsKkM6eVkZPGPzwM5GILMfLBH_q45C8zEL54mIAlNMnZaqV_226CasFUGDUUWMaKuh2XNXjiIbXegQIa9JjXMTsOW95wL7bZ8KPTXnFLGtLlajO2yZpSSpTVLW4sgAFxIpZx4zTPKDOodQDtXcadYf2-gsWh-bZ0bCfWsRKGwbT0Aa5sB1oqeUiB6hrLpX3QT__1-Z6OlWs-O0a1sY1mzZINgZaMQhtyHGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگاه قضایی جمهوری اسلامی برای دو نفر از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ احکام سنگینی صادر کرد؛ مهنام نواب‌صفوی به اعدام محکوم و حکم ۱۰ سال زندان علی صانعی نیز در دادگاه تجدیدنظر تایید شده است.
مهنام نواب‌صفوی، محبوس در زندان دستگرد اصفهان، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد با اتهام «محاربه» به اعدام محکوم شده است.
در پرونده او اتهام‌هایی از جمله «محاربه از طریق مشارکت در تخریب اموال عمومی»، «تبلیغ علیه نظام»، «اجتماع و تبانی علیه امنیت کشور» و «تشویق مردم به کشتار یکدیگر» مطرح شده است.
هم‌زمان، حکم ۱۰ سال حبس علی صانعی، دانشجوی ۲۲ ساله رشته کامپیوتر، در دادگاه تجدیدنظر تایید شد.
صانعی اسفندماه ۱۴۰۴ در ملارد بازداشت و به زندان تهران بزرگ منتقل شد. شعبه ۲۸ دادگاه انقلاب تهران به ریاست قاضی عموزاد او را با اتهام‌هایی از جمله «توهین به رهبری»، «اجتماع و تبانی علیه امنیت کشور»، «تبلیغ علیه نظام» و «همکاری با اسرائیل» به ۱۰ سال حبس محکوم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77424" target="_blank">📅 17:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77423">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UgTT5bFLdG3788E1oEMzSvooLUlrN0AOQeck2_YKTd2iVbcFCc0daqCKTF-EJiECaIIHGLKDNSLjYRdfwH1yFTYx2MmBpyzK4SMaTFw3mefqdHo_yfwGSpdxxDMA2-hsD-yIr56GxGcF1hk1K661maU8eGWtdsWOHARQ1olI7VDGDfU3HDWx6avr7VvT66tjQkG4n2jbS6ueA7VR_i9OrI7q04fPBYakp688J39FPbeGVvL1ARfaLk1lS4hRwG3e2TqSdmTzlV5xFzdDGfzdb7HqxsuyzSZgTH0w7ZPp5hS7SpP-5q8LJJnF1awUrstZOqo72NV7cBr1l5qj8JJdiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: آمریکا هم‌زمان با تشدید حملات به ایران، بمب‌افکن B-1 را به‌کار گرفت
ترجمه ماشین:
مقام‌های آمریکایی گفتند ارتش ایالات متحده روز سه‌شنبه برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران از یک بمب‌افکن دوربرد B-1 استفاده کرد.
چرا مهم است: این نخستین بار از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش بود که آمریکا مأموریتی با بمب‌افکن B-1 انجام داد.
استفاده از بمب‌افکن‌های B-1 که می‌توانند ۲۴ بمب ۲٬۰۰۰ پوندی یا ده‌ها موشک کروز حمل کنند، نشان‌دهنده تشدید و گسترش قابل‌توجه کارزار نظامی آمریکا بود.
‏B-1 می‌تواند در ارتفاع پایین با سرعتی بیشتر از سرعت صوت پرواز کند و در میان همه انواع بمب‌افکن‌ها، بیشترین محموله بمب را حمل کند.
هم‌زمان با ادامه افزایش حضور نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان در حال بررسی بازگشت به عملیات رزمی گسترده علیه ایران است. مقام‌های آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
اصل خبر: بمب‌افکن B-1 مأموریت خود را از یک پایگاه هوایی در بریتانیا آغاز کرد و در وب‌سایت‌های آنلاین رهگیری هواپیما مشاهده شد.
فرماندهی مرکزی ایالات متحده (سنتکام) در بیانیه روز سه‌شنبه خود درباره حملات آن روز، به مأموریت B-1 اشاره نکرد.
در این بیانیه آمده بود: «دارایی‌های سنتکام مراکز عملیات نظامی ایران، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز بیش از پیش تضعیف شود.»
مشخص نیست B-1 چه هدفی را مورد حمله قرار داده و آیا این مأموریت عظیم از دیگر حملات چند روز گذشته مؤثرتر بوده است یا نه.
آمریکا در جریان عملیات «خشم حماسی» چندین مأموریت با B-1 انجام داد و پایگاه‌های موشکی، مراکز فرماندهی، تأسیسات نگهداری سلاح و سامانه‌های پدافند هوایی را هدف قرار داد.
وضعیت کنونی: با وجود گسترش حملات آمریکا، به نظر نمی‌رسد حکومت ایران موضع خود درباره تنگه هرمز را تغییر داده باشد. ایران همچنان به حملات علیه پایگاه‌های آمریکا در منطقه ادامه می‌دهد.
برخی مقام‌های دفاعی آمریکا می‌گویند توانایی نظامی ایران در اطراف تنگه هرمز «تقریباً از بین رفته است»، اما برخی دیگر می‌گویند ایران همچنان قادر به حمله به کشتی‌ها در این منطقه است.
رئیس‌جمهور ترامپ روز چهارشنبه تهدید کرد که اگر ایران به حملات بیشتر علیه کشتی‌ها در تنگه هرمز دست بزند، پل‌ها و نیروگاه‌ها، از جمله تأسیساتی در تهران، را بمباران خواهد کرد. ایران نیز در پاسخ، زیرساخت‌های کشورهای حاشیه خلیج فارس متحد آمریکا را تهدید کرد.
نمای گسترده‌تر: همچنین روز چهارشنبه، شورشیان حوثی برای نخستین بار از زمان اعلام محاصره بنادر عربستان سعودی، به کشتی‌های سعودی حمله کردند.
یک مقام دفاعی آمریکا گفت حملات حوثی‌ها، پس از چند ماه که تقریباً به‌طور کامل از جنگ دور مانده بودند، ممکن است با تحریک ایران انجام شده باشد.
این مقام گفت ایران می‌خواهد با استفاده از حوثی‌ها، علاوه بر خلیج فارس جبهه جدیدی در دریای سرخ ایجاد کند و بر یکی دیگر از مسیرهای حیاتی بین‌المللی حمل‌ونقل نفت فشار وارد کند.
روز چهارشنبه چندین کشتی تجاری در حال عبور از دریای سرخ دیده شدند که از بیم حملات حوثی‌ها، مسیر خود را تغییر دادند تا از تنگه باب‌المندب عبور نکنند.
آنچه باید زیر نظر داشت: مقام‌های آمریکایی گفتند میانجی‌های قطری همچنان با مقام‌های آمریکایی، ایرانی و عمانی گفت‌وگو می‌کنند تا به توافق جدیدی برای بازگشایی تنگه هرمز و توقف درگیری‌ها دست یابند؛ این موضوع را منابع مطلع اعلام کردند.
یک منبع منطقه‌ای گفت رهبری ایران تازه‌ترین پیشنهاد ارائه‌شده از سوی میانجی‌ها را نپذیرفته است.
مشخص نیست ترامپ چه مدت به تلاش‌های دیپلماتیک فرصت خواهد داد. ترامپ چهارشنبه‌شب در سخنرانی‌ای در جورجیا گفت: «آن‌ها به‌شدت زیر ضربه هستند و می‌خواهند توافق کنند.»
«اما من می‌گویم آن‌ها آماده توافق نیستند، چون هر بار توافق می‌کنند می‌خواهند آن را عوض کنند و همه‌چیز را تغییر دهند. آن‌ها آماده نیستند. خیلی زود آماده خواهند شد.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77423" target="_blank">📅 07:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77422">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZxpoyulXAszZCTWrw34OXgZB-kq1y5bHSZat0ClPHiKdfJ15QFXmQnFnqQa2Rey3ea7Y4EEtjMBqUG4c8eFeKiA8lxSq-u9GqbkNkY3o6Mh_Gqg-w2XtRE5q3RzBhrwaozJmVfmMYugKSkgNO9_kgdiy7h_khsTD3OzeY28OVaTql88Bzl1wmF5LXxgg_qscm0SqHgsWNMYWsLsfMGTQAcHjcbe6_Uz-cF13CJFivVDk-g1QU76A5FVgwfjXa11kfMMkbDw6aCOsyqcPLN7j7skeqIZnfcQVtSEIMpoetP11y9xCYwdksJz81dGGUR2J5iESo5dPwAiEENXtaQ-yKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان (واس) تایید کرد که کشتی «انسیلیا» متعلق به یکی از شرکت‌های سعودی در دریای سرخ هدف قرار گرفته است.
به گزارش واس، در پی این حمله، آتش‌سوزی در بخش جلویی کشتی رخ داد، اما همه اعضای خدمه سالم هستند.
یک منبع در سازمان حمل‌ونقل عربستان نیز اعلام کرد نهادهای مسئول اقدامات لازم را برای تامین امنیت کشتی «انسیلیا» انجام داده‌اند.
پیش از این، حوثی‌های مورد حمایت جمهوری اسلامی اعلام کرده بودند که دو نفتکش عربستان سعودی را هدف قرار داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77422" target="_blank">📅 07:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77421">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/111a8149da.mp4?token=f2UVCq6WKuQFFqYC1HKt2FYrrSjJVOCAVXXMJlfutbFrU0DDwvsWqByk2sbZo-Pcqzmcgo2WJXRn_ATQTMC4E0weu5KCZf08TFYFQ4TonfaI60QMj6Nx9H4CE2__hW-DshD6FzVc0prZap5lH7uqzt0PAzZl2o4uIYDSYrJEQ5nMvdy1Oan9aD7ggGHaluGryaxgJYJJo8V35VhiF8SLrXknaeuNkyPekynHIv6n7GUXaWPRJH5TqhzGalocSzCq1VgGXEqTVgU7G5kQEF81FGH-DWpMzffrzXczOkAX807Fuo_Dycu2UY07D5tA0vA7CgR9W0JjQGSONRL6GrMNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/111a8149da.mp4?token=f2UVCq6WKuQFFqYC1HKt2FYrrSjJVOCAVXXMJlfutbFrU0DDwvsWqByk2sbZo-Pcqzmcgo2WJXRn_ATQTMC4E0weu5KCZf08TFYFQ4TonfaI60QMj6Nx9H4CE2__hW-DshD6FzVc0prZap5lH7uqzt0PAzZl2o4uIYDSYrJEQ5nMvdy1Oan9aD7ggGHaluGryaxgJYJJo8V35VhiF8SLrXknaeuNkyPekynHIv6n7GUXaWPRJH5TqhzGalocSzCq1VgGXEqTVgU7G5kQEF81FGH-DWpMzffrzXczOkAX807Fuo_Dycu2UY07D5tA0vA7CgR9W0JjQGSONRL6GrMNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام تازه‌ترین حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰:۳۰ شب به وقت شرق آمریکا [۶ صبح به وقت تهران] در ۲۲ ژوئیه، برای دوازدهمین شب پیاپی، دور دیگری از حملات علیه ایران را به پایان رساندند.
نیروهای آمریکایی اهداف نظامی ایران، از جمله توانمندی‌های دریایی، تأسیسات نگهداری موشک و پهپاد، مراکز نظارت ساحلی و تجهیزات پدافند هوایی را هدف قرار دادند. این حملات توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری را بیش از پیش تضعیف می‌کند.
در ماه جاری، نیروهای آمریکایی ده‌ها مرکز نظامی ایران در خشکی را هدف قرار داده‌اند و هم‌زمان محاصره دریایی علیه ایران را از سر گرفته‌اند. تا امروز، سنتکام برای جلوگیری از ورود کشتی‌ها به بنادر ایران یا خروج آن‌ها از این بنادر، مسیر ۹ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته است.
بیش از ۵۰ هزار نیروی نظامی آمریکا در سراسر خاورمیانه در حال فعالیت هستند و همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77421" target="_blank">📅 06:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77420">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/neD9JRr65DQYVOr632v5PtYJJafKsMuxH1kOvvZfpMgdgap4AsXK6TKdYkrT__myo8L2qM-zbpLdinv7wBVuExlMLmnucAMysMNMTwa4tY7qvtNAqswZi86coSEBIJCfMkyCELhBO409NovmHvqjFFjXxNzOXcclS8lvmuW_xXq0Bvxxjy7zyc5GTiD5A9hTMWoXDJjTTB6zxYewuN_5aPE1a4UJt7egB2zrX6_YCLFCOeSmwcsqQELjmhuz0pV2-KBFhi95i5iqsrYFJrEXLpOL0N3WUTQhMrDUHWprIJUa6F9hRKQTgdXCoTYU1uOuaLmH9yuPx2z0jVPxBU4tEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه پیام دریافتی از ساعت ۵:۱۳:
دوتا انفجار سنگین پایگاه دریایی ارتش جاسک
جاسک ۲ بار زد
جاسک چند دقیقه پیش دوبار زدن . سلام
🔄
دوباره زدن
صدایی شبیه به جنگنده هم میاد
یک صدای وحشتناک انفجار جاسک 5:30
همین ۱ دیقه پیش دوباره جاسک زدن، نمیدونم دقیقا کجا ولی صدای خیلی شدیدی داشت
باز انفجار مهیب در بندرجاسک ۵:۳۱
جنگنده بالای سر شهر در حال چرخیدنه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77420" target="_blank">📅 05:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77416">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JJNmEjQ6om1XuRT2fO3wDNB2Q03p9lS2DLYLKirGglbwxpnFkMxc59PSqvZNQPFwyKU6QqYPNCSSHbh-7Lxy3EAigK2_24QNjzX7c7K0XY6LQ45RVzY-Td-gQhSKMlHqCy846YDqcNZBRUKc67igTL1Oq-gTQuemkL7APN7HKELWpVmmWCJsiPsVLy9fxUr1xfY2Cq_b13A2U0q0P66UI3qH6_OMYpp6yo3OXwWtkz-TMH9bkTFQSBU4lvPbTb7_4YZrsaefXjQ39fWpcDi443cWN8HSkQ1CUR3QbySOPYiZy4MsA_NFUHE5_NfWZe-Q3I_U-xF7UR1uTkD7Guludg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pfnps9_XoA--iP59p5-6gTKM0Or1DydOw1QrCm6RGdx33EwwPo2xQrrMl41Na7jYXieD-NGDAURinDHi62rdeVd9Ush-rbVAb1UfTZALzsuloMYMusNIE8dPTV5K-axVv4C09tpo7L4qUyFOwkaxq5Ty7mghzUmx05YQM9CiwfjAJ9Ynme5wJ1oIFyRoh3rNDceqFUvXiMkxwmFjxxF1K7YlOP-wIzK4_Slcgxz_DGxtZFD3cn3XnL8TStfU3D5IN-bIdxyJ9KqTCUAjfX7Pp9Xt-XFCiLLhWIEDi7KfX5f2mb_TtTWULdxzGKTokk0XqKApNgj7OFaGzv4Om6bPlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HIO0mH5HoRX2YfybghvyCxri3e55BXRrzS6X50IJsUcbeTiXczAuASavU7db1jbTpul6tjnOw8lMp3s2Beso-DdvT6VjsZcWZxtjOwgXN04EQxBFWSbtakSqWYPfY2Bysb-1v4hot2usi8ARM9yCruZACKoHywCOKjur158nl6-PWNP06fOdRF60aSWwtrNUL-eFQ3iBmZ3Pqck8Rn6kZOZ9kUQfU4Uo3lmz2w6U5KEUR4rUApAUsMZ66mIN6SCWglCL-t9cA6qex3udfMvd2L1UDDrTxr-wDzYnIkkzEpfgXVP5vZDfG96GAFiuyN5yJwrJhLSU8VYO6z6GrVNgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uRMOrs8EUgeDkBKiJDuuUp5PO89GTJqQNfk218UA4MYQy6O8rg2REx3h-zjzQWA_H9ZjG7Tr3ptJIFvADrh3hw_sD2dAQ0WC4zuyd-8jQyPRTSH0Dm2IWaHgVcpYz2_MLVJyDBQxnJRwlm4JpqO5onNqy3FZvTcrs0l_O-rXI1UUyNb9YpAT3MnERRwO2owmQwRROWf2LLoFbuFXI2trYjSAY2_U_asD5SHXKrjP1qjwQ6xxKfKkEMC8JL6bdgLY7DRLu8-2wxu_RDYPTKRf6ROsDJW6-O8Upcw44gA8r8mujTPZ3ep-8qLjaF9NUY7gfARnmJgw0fLmt12OjgfP4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر پخش شده با شرح: انفجارهای حمله به  اسلام‌آباد غرب در استان کرمانشاه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77416" target="_blank">📅 04:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77415">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpFyId4T6zHKSKNeukZiAnsvmROiPJcYrYV-QWVY6eDbOZn0EsRZ0Q8hZaBlPOSz2MKqm2lUhUn1q37MOzD7qLFripTiYIHLr5HervqJJrjOdHDyBP_53npxepGOlV6JzMDjIbS5d0Osfg3RFDxs7bK1lEgCG3P2uBg5ykq7YzYXkaN9nGgufyXmPSzZtPD9Jil1R6BRmYFPUyL2IsbTRw6uY0MTOZHWG085EhLNhnV7J8pxjle7naG9_4ws9y6c64GJKbU71MAd2O0WcMsJBhO6P8iDu0o1dg1FxUpfqY-lP-8ftRMFTCK79Lrzhc-89Z0PkyG5IuXBt0K6ZDcHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش تسنیم، معاون استاندار خوزستان اعلام کرد یک نقطه در اطراف شهر اندیمشک هدف حمله موشکی قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77415" target="_blank">📅 04:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77414">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9aaff68657.mp4?token=gUWRkdICsSHYniHzAgCvuqpimdLj6pI1Asc7CZNnz16n1gX-MWdvdURKOddpHZrCva8CqO8iRPqLfkuBvX4Sq_9C3xP9d556-Lnr4vaUFF7cf95dOtg-tuxcq1sT7RZM82EFbulfCzjjPajE4k3dIBPOCyvuTw9NRYRFg3hW0vpFUOidtsY0Bn-Zq08Uun2Gw2Qes1Uuo_VF1d5gaYw8jyqFQHZf5rXOqX7HiL2QD2zblu0av3pHz_610g2beRkayaeh8tqRUeHNLtjzB1r2Rb3UBSSgs1KTJR79v3yf4TU64UZEPxGimuiUJNfO2cmzTIZQ1e0hBdl-TeI5Jgs7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9aaff68657.mp4?token=gUWRkdICsSHYniHzAgCvuqpimdLj6pI1Asc7CZNnz16n1gX-MWdvdURKOddpHZrCva8CqO8iRPqLfkuBvX4Sq_9C3xP9d556-Lnr4vaUFF7cf95dOtg-tuxcq1sT7RZM82EFbulfCzjjPajE4k3dIBPOCyvuTw9NRYRFg3hW0vpFUOidtsY0Bn-Zq08Uun2Gw2Qes1Uuo_VF1d5gaYw8jyqFQHZf5rXOqX7HiL2QD2zblu0av3pHz_610g2beRkayaeh8tqRUeHNLtjzB1r2Rb3UBSSgs1KTJR79v3yf4TU64UZEPxGimuiUJNfO2cmzTIZQ1e0hBdl-TeI5Jgs7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
وحید بوشهر زدن بدددد
بوشهر انفجار خیلی شدید
😐
دستم میلرزه بزرگترین انفجار
سلام وحید همین الان انفجار خیلی شدیدی بوشهر از قبلیا خیلی بدتر بود
وحید بوشهر زد ساعت ۳:۵۹
بوشهر چند انفجار وحشتناک همزمان ساعت ۰۴:۰۰
بوشهر زدن ساعت ۳:۵۹
سلام وحید الان بوشهر رو زدن و خونه لرزید یه صدا خیلی زیاد هم اومد
انفجار سنگین شهر بوشهر ۴:۰۰
سلام وحید جان
ساعت 3:59 بوشهر رو زدن صداش متوسط بود
بوشهر صداش خیلیی بلند بود
همین الان وحشتناک بوشهر زد
همین الان بوشهر زدن ۴:۵۸
وحید جان بوشهر پایگاه هوایی باز زد الان
درود، همین الان
3:59
بوشهر رو زدن صدای مهیبی داشت
وحید جان بوشهر
همین الان زدن دقیق ۳ و ۵۹
یک انفجار نسبتاً شدید ساعت ۳:۵۹
۰۳:۵۹ بوشهر صدای انفجار خیلی شدید و خیلی نزدیک اومد
سلام بوشهر رو الان زد
همین الان یک دقیقه پیش انفجار وحشتناک بوشهر خونه لرزید
از بوشهر همین الان یه صدای خیلی بلند انفجار دقیقا نمی‌دونم چی بود اما خیلی بلند بود همه از خواب پریدیم
ساعت ۴ صبح انفجار مهیب در بوشهر
چندین انفجار بوشهر
یکیش خیلی بلند بود و لرزش داشت
داش بوشهر بغل خونمون انگار بمب اتم زدن
بوشهر صدای وحشتناک انفجار، گمانم پایگاه هوایی بود... ساعت ۴ صبح
همین الان خیلی شدید
از خواب بیدار شدیم
بوشهر
صدای انفجار خیلی شدید از پایگاه هوایی بوشهر
سلام همین الان بوشهررر صدای بدی اومد که همه بیدار شدن
تک انفجار ساعت ۴ ولی جوندار زدن
آپدیت:
پیام‌های ساعت ۴:۴۱:
صدای پدافند بوشهر
وحید بوشهر انفجار
ضدهوایی هم کار می‌کنه
بوشهر پایگاه هوایی صدای پدافند
بوشهر ۴و ۴۰ پدافند پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77414" target="_blank">📅 03:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77413">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">استان کرمانشاه
فقط سه پیام دریافتی در ده دقیقه:
انفجار کرمانشاه ۳:۳۶
اسلام آباد کرمانشاه رو زدن
سلام ۵دقیقه پیش اسلام آبادغرب در کرمانشاه را زد ۲تاانفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77413" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77412">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T85MAztINr7cOOjBhME0SrrAZqeqtTWtKpKNrDAc8DjKLSykJ1OSuhAdaH492qg8Fo_I55TLmehBH4uqXxnwPdGiUQP_A82LPBQSpLFmJhitaxXs77CdSrNTAPFtLtK091dkibKhBgdk8l-NBocmGVe-QnKc9VDiM4eHnehGpb0ZzgV8fJRJXjnKmD1U0zrlsqIfj_3_luJ_EYP6i6OOzjw6hivtXvMTVfvhQvvokOaZdtHW6yH6BS69CWQILcIY1E4t8Xegff62ajGDw-lfBaS_fCXp-jB_souzZo06zl4ZJLLz_QSFTK-xLg9UOFKGq-2gJgRc1g5lI2ufnKpiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران صبح پنجشنبه در اطلاعیه‌ای گفت که سه کشتی قصد عبور از تنگه هرمز را داشتند که یکی از آنها آتش گرفت. سپاه دلیل آتش گرفتن این کشتی را برخورد با مین عنوان کرده است.
سپاه در این بیانیه تاکید کرده که کنترل تنگه هرمز را در اختیار دارد و هیچ کشتی از این تنگه عبور نمی‌کند. در عین حال ارتش آمریکا می‌گوید تنگه هرمز باز است و هفته‌های اخیر ۹۰۰ کشتی از آن عبور کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77412" target="_blank">📅 03:46 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
