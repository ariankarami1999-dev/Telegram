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
<img src="https://cdn4.telesco.pe/file/K7NHUSqWckS7FqTUKOQUrNbd7wUhf8aL4zYUjaxks5GHBUNxxHNB3INvuwsA6d9jeJBCQMyRIEnWRQol3H7Mujy-5JvsXLgzN7rt8rl7LyDMSz-CnxfjJCgYEhor55fvn4sJU9ExyvjWAiP0Yu1qNKOGWs0ILVc114KSlruSUr2y5weteHobjDI_s4wNLh4_QankD-VJRwXhDuLH8yeIQSRzA45lp0P4hKuyhQqf6tDXeUM1fzqdKtonbnPLcyr97Sv23HspMpZAc2dQmIwa8ptfsqMSaOOAun65JcFQxB-LWFkVkxoZ1XlrTiNAKHHKDUAZDhXRSPAZf5uyP-H2Cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو با محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 8.14K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 من تالیف و تولید می کنم✅. نه ترجمه.نه اخبار. نه گرداوریدوره:mohsentavoosi.com/course/seo/خرید دوره:@mohsentavoosisupportyoutube.com/c/MohsenTavoosiInstagram.com/mohsentavoosi.seolinkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 02:20:54</div>
<hr>

<div class="tg-post" id="msg-1000">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پاسخ کوتاه تر بعد از سه ویس بالا درباره ایندکس نشدن ها:
Welcome to the club!
تازه شُدید شبیه همه ما. ولی پاسخ فنیش همون سه ویسه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 638 · <a href="https://t.me/mohsentavoosiseo/1000" target="_blank">📅 15:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-999">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ویس بسیار مهم درباره این جملات:
با دیتا حرف بزن!
این دیتا معتبر نیست!
این دیتا معتبر هست!
تجربه مهم نیست!
تجربه مهم هست!
مستندات بده!
هیچ مستندی نداده گوگل!
اصلا این آموزش ها و مستندات به درد من و هدف من میخوره؟
مرز تشخیص محتوای درست وغلط و نحوه استفاده از منابع و تجربیات و مستندات.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 939 · <a href="https://t.me/mohsentavoosiseo/999" target="_blank">📅 15:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-997">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwQ9C66MhtY_hFh3zDEiX4KetT0tNsuQNcM6dc-jlvi2Ps9vCScQZNz3FtnK3zKRfA7rRAMYwbLGeeDGbKrpvY9rpvZMsPPEqDIbxNFYJ9B04QgfURdD0XYs6kjWZwQ0cQKaXxWZR3Q7VNCcjD24qheEaiL1l31-Wo3icbsk7sPEHjV7BCoe_J5_OKJVo1s4XJDAZfYl4piUL8rrZRloZl00-mSX8HqNPGoMVDyT6xrV_zD4b1rmNQKB7kaf-YqsYhbF82J30ZLM8cbYuuKS4mxWWxLTVvqIoDUryUXc44yvy6f78btdLJltib6kNaInwdtqgZW41uGMqHaQpT9Jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tN7UTLU0mnCX-HOjxfy-3RHOlb22kAZeT31LT5BmmGnZJPQ9i2CApQmNCGoRHt3-MF0lIu19R2Y3RzSTexZ-2ErJa-HgKyd4NglS0uDDW10cUBnx5DhsILVsH2JLNOOWsl6sfNwxngWfwi2c-l-y_97fMlJdq0tvvoN1b3l1DsMZpokZmqgFtmKAPyo7rcKIGoZHXUZJB9pCn9iUPcRFPZrOxhL3sht-VZeSDHgMFD-EWxlbz-twf7xe0ApanxWk3_xOHaxOoCT8K75l2tvnX9ls-1mC-Luk30VwkShFuVezRn9_OUkyBppUE9PPaajyUp_oI1CxAdGIk7xC9dFAyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درباره بحث ایندکسینگ و ایندکس نشدن صفحات و وضعیت های Crawlded, not Indexed یا Discovered, not Indexed.
تصویر بالا، تصاویر نمونه هاست دارای مشکل در 90 روز گذشته و هاست بدون مشکل در 90 روز اخیر در بخش Crawl Stat سرچ کنسول (بخش Setting). همه این ها در دوره هست در فصل های تکنیکال.
تمام پاسخ های مرتبط با بحث ایندکس نشدن در 19 دقیقه ویس (در سه Voice) زیر:
7 چیزی که باید چک کنید:
https://t.me/mohsentavoosiseo/868
نکته 8 که دست شما نیست و بهش بی توجید و مرتبط هست به قدرت سایت و پتانسیل رتبه(نه رتبه نقد فعلی) و پاک کردن آشغال ها:
https://t.me/mohsentavoosiseo/869
قبل جنگ خوب بود بعد جنگ این بلا سرم اومد:
https://t.me/mohsentavoosiseo/996
نکته پایانی:
بعضی مواقع تسلیم شید. پذیرش یه حقیقتی که بهش اعتقاد نداشتید، بهتر از دست و پا زدن های بیهوده است.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/mohsentavoosiseo/997" target="_blank">📅 14:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-996">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 687 · <a href="https://t.me/mohsentavoosiseo/996" target="_blank">📅 14:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-995">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">من داخل دوره، فصل سئو فنی 1(چهار فصل فقط سئو تکنیکال داره دوره) ویدیوی Response Status Code کامل درباره استتوس کد ها گفتم و 304 هم در دقیقه 03:15 هست.
قدیما فکر میکردم همه باید دوره رو کامل ببینن. حداقل کسانی که پیگیرن و فعال هستند دیگه باید ببینن. بعدا فهمیدم درصد کمی از همون ها میبینن دوره رو و این روتین و روال جهانی هست در این عصر پر زرق و برق و پر از حواس پرتی.
ولی یک بار اگر دوره رو ببینید به جای یادگیری های پراکنده و اسکرول ها و کانال های مختلف، بخش زیادی از عمرتون و ذهنتون صرفه جویی شده و بهره وری به شدت بالا میره.
اینجا هم میگم 304 اکیه و مثل 200 هست و هیچ مشکلی نداره. مرتبط با بحث Cache هست و این پیام به بات گوگل، که بات جان، این از آخرین باری که دیدی عوض نشده. نمیخواد دوباره بیای کراول کنی. پولتو هدر نره من (صفحه) همونم که سری آخر دیدی.  همین.
من تو همین ویدیو 307 هم گفتم. تو همین ویدیو اینکه نباید بگید ریدایرکت 410 هم گفتم. وردپرسی یاد گرفته ها به 410 میگن ریدایرکت چون تو تنظییمات ریدایرکت افزونه ها چیزی شبیه این دیدند.
ریسپانس هدر و ریکوئست هدر هم گفتم تو همون فصل. User Agent هم گفتم. Partial Postback و Json Request ها هم گفتم.
فکر نمیکنم جایی بتونید از پایه با زیرساخت ذهنی درست، همه چیز رو اینطور اصولی و شسته رفته و بدون مقدمه الکی و کش دادن الکی، آموزش ببینید.
نمیتونم کسانی که دوره رو دارند وادار کنم دوره رو ببینند. ولی میتونم بگم دارید ضرر می کنید حالا که خریدید و یک بار نمیبینید دونه دونه. بدون حدس زدن و این تفکر که "من که بلدم". میدونم بلدید.
ولی همین 304 رو همون کسی که میگه بلدم بلد نیست. دیگه ویدیو جدا نذاشتم چون 3 جملست کلا! ویدیو جدا بود هم دانشجو از حجم زیاد محتوا میترسه و مغزش میگه ولشکن بعدا میبینم.
——————————————————--
🟢
لینک صفحه خرید دوره سئو بین المللی(+فارسی) با AI
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/mohsentavoosiseo/995" target="_blank">📅 12:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-994">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اسم های مختلف میشونید:
سئو ایجنتیک Agentic SEO، اتومیشن سئو SEO Automation, سئو با هوش مصنوعی، بهینه سازی برای موتور های مولد، بهینه سازی برای LLM ها. Answer Engine Optimization بهینه سازی سایت، پیج و... برای موتور های پاسخ دهی چت بات، GEO بهینه سازی برای کلا موتور های مولد Generative Engine، و کلی اسم دیگه.
البته که ایجنتیک سئو با GEO/AEO فرق داره. عملا این AEO میشه زیرمجموعه بهینه سازی سایت توسط هوش مصنوعی و اتوماتیک.
درسته نسیه است حرفم.
اما اینو گفتم که بگم همه اینا رو تو آپدیت دوره دارم میگم(دارم ضبط میکنم). و کلا موضوع جدیدی هست و حتی ویدیوهای یوتیوب مرتبط در سطحی که من میگم، ندیدم اصلا در سطح بین المللی هم ندیدم. چند تا هست مثلا برای سه ماه پیش! یعنی کلا بحث جدید هست.
اونایی که هست هم به درد برنامه نویس ها میخوره فقط  و برای عموم مناسب نیست.
ارزشی که من خلق میکنم اینه که چیز سخت و پیچیده رو ساده بیان کنم.
من میخوام پیر نشید برای یادگیری! ساده اش میکنم و تو محیط راحت میگم. هلو بپر تو گلو بدون سردرد و وحشت. بدون ترمینال. بدون کد. بدون پایتون. بدون محیط های سخت برای عموم.
راستش سه بار ضبط کردم و از اول شروع کردم. هربار ساده ترش کردم. وگرنه ماه پیش آپدیت رو داده بودم بیرون.
خوبیش هم اینه که قشنگ من خاکی شدم وسط کار. هرچی یاد میگیرید اجرا کردم بارها. میشناسید منو. من آدمی نیستم چیزی یاد بدم که قورتش نداده باشم.
ضبط بخشی از ویدیو ها تموم شده ولی بعد از ادیت و اینکه بخشیشون کامل شد قرار میدم تو دوره. خرد خرد قرار نمیدم.
شما تا اخر 2026 روش حساب کنید و نگید کی میاد ولی از الان میتونید تهیه کنید که قیمت بالا رفت، داشته باشیدش با قیمت قبلی
. کل موضوع جدید هست اصلا و منبع جهانی هم نداره با بیان ساده و سئویی به اون شدت.
منتظر یه نشاط دراگ گونه باشه بعد از دیدن اپدیت با حالت "آخیش! چقدر خوبه!".
یجوری میگه دراگ انگار نه انگار خودش سوبره
😏
.من سیگارم نمیکشم شراب قرمزم نمیخورم حتی.
——————————————————--
🟢
لینک صفحه خرید دوره سئو بین المللی(+فارسی) با AI
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/mohsentavoosiseo/994" target="_blank">📅 14:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-993">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این پست بسیار کاربردی رو ذخیرش کن تو saved هات. هم معرفی ابزار هم آموزش. بفرست برای کسانی که دنبال ابزار هستند: و اینکه ما کیوورد توول رو از کجا تهیه کنیم میشه.هم لیمیت پس هم نوین ترند  خیلی بده سرویس دهیشون و لیمیت میخوره اصن نمیتونیم کار کنیم https://t.…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/mohsentavoosiseo/993" target="_blank">📅 13:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-992">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">چرا رایگان درست حسابی و بی دردسر نداریم یک ویس میذارم که خیلی مهم هست در ادامه(اگه نگاه تجاری درستی داشته باشید به این پایین نیاز ندارید).</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/mohsentavoosiseo/992" target="_blank">📅 12:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-991">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درباره دلیل اینکه چرا اشتراکی ها انقدر اذیت کنندست و چرا رایگان درست حسابی و بی دردسر نداریم یک ویس میذارم که خیلی مهم هست در ادامه(اگه نگاه تجاری درستی داشته باشید به این پایین نیاز ندارید).</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/mohsentavoosiseo/991" target="_blank">📅 12:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-990">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تو ابزارهای اشتراکی، قطعی ها و ایراد ها و اینکه یهو میگه تو حداکثر ظرفیتو استفاده کردی(با اینکه نکردی)؛ رو بپذیرید!  طبیعیه. همون لحظه رسیدن به محدودیت اکانت، نمییتونن درجا شارژ کنن. دستی انجام میشه.   پول کم میدیم که استفاده کنیم فرقش همین چیزاست. قطعی، یه…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/mohsentavoosiseo/990" target="_blank">📅 12:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-989">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آموزش اتصال کلاد به وردپرس و هرچیز دیگه ای فقط تو یک دقیقه!   و این برای وردپرس نیست فقط. برای همه چیزه. کلا این قابلیت کلاد کروم خودش یه فصل جدید زندگیه
😎
این یک دقیقه انقدر کوچیکه که معنی نداره بگم تو اپدیت دوره هست. خیلی بیشتر و تمیز تر میشه از هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/mohsentavoosiseo/989" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-988">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خیلی دارم اذیت میشم! خیلی! چون خیلی چیزها رو دوست دارم بگم و آموزش بدم ولی الان نمیتونم. حتی الان نمیتونم دلیل اینکه نمیتونم الان بگم هم بگم!
اما این پست رو اینجا میذارم. روزی رسید که میتونستم بگم، رو همین ریپلای میزنم و دلیلش رو میگم.
جذاب هست و بسیار کاربردی دلیلش و بسیار در راستای نگاه تجاری هست. و مثل نقد فیلم ماتریکس یهو رمزگشایی میشه و براتون جالب خواهد بود و البته دارای بار آموزشی + چند تا چیز دیگه.</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/mohsentavoosiseo/988" target="_blank">📅 21:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-987">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfLqLEKGHpLCFbry04-oquFRMLxzzxHBssHXicU4wc29VKwJDjOiNkw4Ox7H7fg0z6GQ-7TuvInah4QAhz-Y06t74lCQfEUsUl8lviO527HPsGIWQtUQA7uSyp6hKvm1M5EmeWMwAbVWj3vH5i4pvqm5iJ7-znkgSJ2XXUqzi4XqgmnfsSwVKjqIkAxaJD3l6dCIx_4D0XCdYvH6JGMeBHhCpyLf5Gdk8_JDlpT9Ow_UorQaBHM98bBgH8VBkQCZt_AEl5Q3l9d-Mo__ytWi39Cp9L4Iurqf8KA3eFjsZZm--m8UTLLnU7gSqMFPVnwqNWd3G4cCpwdhsRIXQ8HTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسی معتبر تر از خود سازندگان هوش مصنوعی هست به نظرتون که تایید کنه در موارد خیلی به روز، هوش مصنوعی عقبه؟
من قبلا مثال اخبار رو زده بودم که هوش مصنوعی بعد از 6 ماه از سقوط بشار اسد میگفت هنوز هست و سقوط نکرده و منبع هم میداد حتی. منابعی که توشون نوشته شده بود سقوط کرده!
بعدا مدل ها بهتر شدند و این ضعف رو پوشش دادند.
ولی همین الان هم هوش مصنوعی در پزشکی پرکتیکال، ضعیفه. ولی تو داده های پزشکی کلاسیک، خوبه. همون پزشکی ای که اکثر دکتر ها درسش رو میخونن به شکل سنتی.
تو نمیتونی از هوش مصنوعی متد های درمانی افسردگی رو توسط گوارش پیش ببری. چون گوارش و ذهن و سروتونین شدیدا به هم گره خورده هستند. اما تو پزشکی کلاسیک، تخصص گوارش، هیچ ربطی به اعصاب و روان یا مغز و اعصاب نداره.
هوش مصنوعی هم همون طب کلاسیک رو بلده.
حالا چه ربطی به سئو داشت؟ به فاین تونینگ ربط داره. به اینکه شما چطور باید هوش مصنوعی رو برای پروژه خودتون آماده کنید. برای افکار و روش های خودتون. برای روشی که شما قبول دارید ولی بقیه قبول ندارند.
تو اپدیت دوره، این ها رو پوشش میدم. سطح کار بالاست مثل همیشه
😎
🟢
صفحه خرید دوره سئو با AI
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/mohsentavoosiseo/987" target="_blank">📅 19:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-986">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6-y3K3sNcwz3x5eVxBYnpeghsnv5LlHtaI0Wc5zNIk7VA9XweGTWYWmJCKSiMrLC_rTYsU30y23UghgfpdvMnEdoEHKS7Ylkx6tu6YZrly3GlqiJudNCP3PJGxoXrw3_ZfpxovyncZWWyLSieRUVq9AIUAtF0xay1n3-j6vvX2ZyYFpHluC7ivtk4Cs4_-cg7I9xxCpthoONkqOd14f22TL9Z8OANbRQ2WUGwaRsbxCI9Rme0buUEMI1pKDNmxrdivIGCiOTxGAdepHL0zf9fOyaqSSrQDLlS-vzMydmUDdonbmhtlm8J3SAeR4iZJpeOLEGhQPjtMMvbKwR8GsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تدوینگر، من رو دعوا کرده میگه چرا حواست نبود این رفته گوشه؟
من کلی معذرت خواهی کردم. گفتم ببخشید. ولی خداروشکر زمان کوتاهی اینجوری بود تصویر.
ولی آیا میتونم بهش بگم تولید کن منو؟ یه میرور بگیر یجوری lip sync (تقلید حرکت لب از صدا) بساز با صدام بیارش اینور تر بخاطر 30 ثانیه؟
واقعیتش اینه که بله، فناوری اونقدر پیشرفت کرده که بشه. ولی سوال اینجاست که آیا مصرفه؟
برمیگردم به نگاه تجاری همیشگی که میگم. مساله این دوره زمونه، امکان پذیر بودن نیست. به صرفه بودن و توجیه هزینه است(ننویسید توجیح خواهشا!).
❗️
وگرنه همه داروهای بدرد نخور صنعت بیگ فارما مثل اس امپرازول و کلا PPI ها
(برای مصرف طولانی مدت و یک عمر)،
جمع شده بود.
❗️
وگرنه همه ماشین ها هیبریدی و برقی شده بودند.
❗️
وگرنه الان همه خونشون خدمتکار ربات داشتند.
❗️
وگرنه همه الان بدون پول، به صورت رایگان، به همه امکانات هوش مصنوعی های غیر رایگان دسترسی داشتند.
❗️
وگرنه گوگل جاوااسکریپت رو مثل  هلو کراول میکرد و نمیگفت لینک هات و لود صفحات SSR باشه.
همیشه بحث صرفیدن هست. نه امکان پذیر بودن. و این صرفیدن شامل هزینه ذهن، زمان و پول هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/mohsentavoosiseo/986" target="_blank">📅 18:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-985">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/mohsentavoosiseo/985" target="_blank">📅 17:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-984">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تب و تاب وایب کدینگ و ابزار نویسی در عصر هوش مصنوعی بدون برنامه تجاری
دون پاشی چند ساله تلگرام بدون کوچکترین بی تعهدی و خلف وعده ای درباره بخش های رایگان(شعار رایگان و تا ابد رایگان).
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/mohsentavoosiseo/984" target="_blank">📅 17:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-983">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">1:06 "کانال های یوتیوب"</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/mohsentavoosiseo/983" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-982">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c43234ee.mp4?token=Yi45moGxe74o2o4TOfOBx0-6Cud_jOhwMi0T9JKzCOkHgnaR1idpGbggksGD3ec6UETAMf3i6vs-KwrQuJl0B5MSiMXDIQ_Fi4qh05VKFEGgqqAxtVcqe0CDy9XfCCB_mfTJ88jQbk6YJQ4qak2dDkUF6C_Ix3ztTRBS117Z9yW1vODyRGGmLxgPiqauRz2poCvbPOEnTpXDvCu8Yo2w0jRgE9HPbEjLy1Fqx6Ruw-h-ZysG-dtONHwAaLbe2XQbgFIq4ycaEneGVDhQ9OSotikeN8w9I6-iZce2DnO24HyBEtWGYCosVyXmHRSQ1XjcJUlhJi3G_0B7PaJ-8aSjrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c43234ee.mp4?token=Yi45moGxe74o2o4TOfOBx0-6Cud_jOhwMi0T9JKzCOkHgnaR1idpGbggksGD3ec6UETAMf3i6vs-KwrQuJl0B5MSiMXDIQ_Fi4qh05VKFEGgqqAxtVcqe0CDy9XfCCB_mfTJ88jQbk6YJQ4qak2dDkUF6C_Ix3ztTRBS117Z9yW1vODyRGGmLxgPiqauRz2poCvbPOEnTpXDvCu8Yo2w0jRgE9HPbEjLy1Fqx6Ruw-h-ZysG-dtONHwAaLbe2XQbgFIq4ycaEneGVDhQ9OSotikeN8w9I6-iZce2DnO24HyBEtWGYCosVyXmHRSQ1XjcJUlhJi3G_0B7PaJ-8aSjrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/mohsentavoosiseo/982" target="_blank">📅 15:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-980">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">من فکر میکردم بحث "هدف" خیلی بدیهی هست. ولی نبود!
و همچنین فعالیت هایی که در راستای هدف نیست.
یا هدف، خودش پوچ هست و باعث سرخوردگی میشه.
پول، تایید اجتماعی، تمسخر، بی کلاسی، نجات دیگران، خیریه، خدمت، رضای خدا.
شاید مسیر باید کلا برعکس بشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/mohsentavoosiseo/980" target="_blank">📅 15:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-979">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">چت جی پی تی رسما یه چپ دموکرات معتدل شدست که فاز شدید راضی نگه داشتن داره. گراک یه راستی جمهوری خواه ساختار شکن بی مرز. جمینای یه میانه ی رو به راست و پایه و خوش فکر و بی تعصب. کلاد هم یه ترکیب سمی ترکیبی با رویکرد "من همینم که هستم" با تعصب و موضع گیری های بیش از حد زیاد تو بعضی موارد هست.</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/mohsentavoosiseo/979" target="_blank">📅 13:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-975">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrL06LJ28kVmcvDfJEOkJPjunBqfQZ6K9uWN63kXb-aiMohzP-q261qaCUbF2A0ng6qwmlE7A647U4oWH_Mz6XBiajR4HpCiDaU6eLx-yH8_kYWkvxxAnO5bhthu34MeEPrA5FMLUtaGNUp76OjC5vYtlehaQCraANGf7SBhpFhBdn6xOZoe2dmLfWQhveGFtct0SlrQ4sKTf-s5L_FTVFk05LzDNLTJYnpOgHwvxSIKJ2EbuGBsFXRmrt9L9DrKLP_bg66APXImzzXvyyC-nSusRfgEnXI9-tWqKckuOWzSmJhNMKkZEojNpcbF9weoxKGzR2STovLHZRmUXnDaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I00w0lLChFaBwRQBgST76pxqT4Poc8o6TgG4xm8TkHkr4g_z4emIyC4mbr890VWTX4A8VS8Xk9tIrOrugp3ces98E3BzJbUsv7cT-WrnqCmPFVBDpo0NYcoSK00RjYUsyatr9Ln3D7C7xnDP49mu2-SHitCe-9x3R90dT4skb8Ok1jPGhYlOw9YC9fNr8LgEvQ4oW9auFQ-ArtGnTYxfGODolLGeKMQNHxKoW7JUAbHqAc60GMVy-GA0DitaoxIW8qJAXzHCQy05inbpKhf531VJ1kT_5S4N7fJxsjo9ru9OL8DZhlKmiUyf-mERuztLAy-DpXZWJ1Ui-mtVjTlLSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هیچ وقت فکر نمیکردم با هوش مصنوعی(Claude) باید سر و کله بزنم که مسیری که من میخوام رو بره! کلاد از حد گذرونده دیگه و زیادی مخالفت میکنه. و حتی میگه ناراحتی گزارش بده آنتروپیک میبینه.
و خودشونم میدونن که زیادی مقاومت داره کلاد تو پذیرش درخواست که گزینه Overactive refusal و Did  not fully follow my request رو گذاشته همون اوایل بازخورد!
یعنی مخالفت و رد شدن بیش از حد و دنبال نکردن کامل درخواست من!
چت جی پی تی رسما یه چپ دموکرات معتدل شدست که فاز شدید راضی نگه داشتن داره. گراک یه راستی جمهوری خواه ساختار شکن بی مرز. جمینای یه میانه ی رو به راست و پایه و خوش فکر و بی تعصب. کلاد هم یه ترکیب سمی ترکیبی با رویکرد "من همینم که هستم" با تعصب و موضع گیری های بیش از حد زیاد تو بعضی موارد هست.
هرچند باز انتخابش میکنم ولی تو اون موضوع که زیادی کل کل میکنه حواسم هست به موضع و دیدگاه مسخره و متعصبانه اش! جمینای و گراک بهترن تو بی تعصبی.
شت! پارسال همین موقع فکر نمیکردم یک سال آینده دغدغم نحوه استفاده و برخورد با یه هوش مصنوعی متعصب و یک دنده باشه! شت!
سال دیگه خدا رحم کنه...
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/mohsentavoosiseo/975" target="_blank">📅 13:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-974">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آموزش اتصال کلاد به وردپرس و هرچیز دیگه ای فقط تو یک دقیقه!   و این برای وردپرس نیست فقط. برای همه چیزه. کلا این قابلیت کلاد کروم خودش یه فصل جدید زندگیه
😎
این یک دقیقه انقدر کوچیکه که معنی نداره بگم تو اپدیت دوره هست. خیلی بیشتر و تمیز تر میشه از هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/mohsentavoosiseo/974" target="_blank">📅 23:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-973">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آموزش اتصال کلاد به وردپرس و هرچیز دیگه ای فقط تو یک دقیقه!
و این برای وردپرس نیست فقط. برای همه چیزه. کلا این قابلیت کلاد کروم خودش یه فصل جدید زندگیه
😎
این یک دقیقه انقدر کوچیکه که معنی نداره بگم تو اپدیت دوره هست. خیلی بیشتر و تمیز تر میشه از هوش مصنوعی استفاده کرد که تو اپدیت دادم قرار میدم خیلی شسته رفته و کوتاه و کاربردی بدون اینکه مغز بیننده از جا دربیاد برای یادگیری.
توجه: این بسیار سادست. کار اصلی ما با MCP هاست.
——-————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/mohsentavoosiseo/973" target="_blank">📅 21:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-970">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چرا نباید از اول برای کسب و کار، با کدنویسی و CMS اختصاصی پیش بریم؟
چرا اول کار فقط وردپرس؟
البته استثناهایی هم وجود داره. اگر تصمیم گیرنده از هیجان زدگی تصمیم بر غیر وردپرس نگرفته و از محتوای این ویس هم آگاه هست و پذیرفته و حاضره هزینه نقدی و زمانی و ریسک با اختلاف بیشتری کنه، ممکنه اختصاصی هم مناسب باشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/mohsentavoosiseo/970" target="_blank">📅 19:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-968">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
این پست حاوی ایده درامد دلاری و افشاگری پشت پرده هست. دست به دست پخش کنید که در جریان قرار بگیرید پشت پرده چه خبره یا خودتون ازش استفاده کنید:  این نظر سنجی که روش ریپلای زدم رو یادتونه؟  نتیجش این شد که من ورود نمیکنم بهش. ولی شما ورود کنید! در ادامه میگم…</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/mohsentavoosiseo/968" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-967">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چطوری ایده مناسب کسب و کار خودمون رو پیدا کنیم؟ اصلا خط اصلی پیدا کردن ایده کسب و کار مناسب ما چیه؟ چه مسیری رو باید بگردیم؟
ریسک های کسب و کار چیه در طول مسیر؟ آماده چه چیزهایی باشیم؟
این ویدیو یکی از مهمترین مواردی هست که تفکر کل زندگی و کسب و کار من هست.
https://youtu.be/2cW1RJKfOao?si=_YEhZViKApY3Nygm
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/mohsentavoosiseo/967" target="_blank">📅 14:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-966">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تو ویس پایین توضیح میدم این اشتباه فاحش هوش مصنوعی رو!  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/mohsentavoosiseo/966" target="_blank">📅 17:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-965">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4_7wyaJ82-cOqrPqXR4aW1RdrrMZtcXAO2HiNW1ngAywwohDbyzCiOPMCoMGJfnBN3lVMnAXt9rNCH3BXgNpqw3medcYCnGAyYVcTny8imJRQZTT1X-QrU1BX-SiFBB0rNU17DSF9-3lyX-HBBlMNwQLfWubUiSEqBkhwLTqXTjl0Jj-rzYtgIHvGZa6VPO3mtun2Q45Y3RcLpNk1PR-UpN7lbDVF7bOe96hxK9uisNqqq4EjakdN3sz0MCw4iQo0YKqKxKQWyWVYJ5VDDrJKMRUF0EXLBOxXrI2xNOxPQbHRMhxM-W535iktKXbpMbpvi5BTei1nMyb3XrmYquzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ویس پایین توضیح میدم این اشتباه فاحش هوش مصنوعی رو!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/mohsentavoosiseo/965" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-964">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⛔️
این خوب نیست!
تو این دو تا پست خیلی ها اومدن گفتن چرا به هوش مصنوعی توهین می کنی و اصلا اینکه هوش مصنوعی برات خط و نشون بکشه و چتت رو ببنده براشون مهم نبود! و فاز اخلاقی برداشتند!
سریال جاناتان نولان داره به واقعیت میپیونده. این خطرناکه‌. یکی حتی نوشته بود با کارگرت نباید بد حرف بزنی خب و همزادپنداری انسانی کرده بود!
خطرناکه عزیزم. لحن ما در چت خصوصی با هوش مصنوعی خطرناک نیست. سلطه ماشین بر انسان خطرناکه که از همین حالا عاشقان سینه چاک امام دیجیتالی(هوش مصنوعی) صف کشیدند برای بردگی و تعظیم برای یک چیز بی جان صفر و یکی(دیجیتالی) ساخته دست بشر.
خداروشکر از قشر آگاه تر و تکنیکال(دولوپرها) چنین چیزی ندیدم‌. دولوپر ها میدونن کت باید تن انسان باشه.
https://www.linkedin.com/posts/mohsentavoosi_%DA%A9%D9%84%D8%A7%D8%AFopus-5-high-effort-%D8%AA%D8%B0%DA%A9%D8%B1-%D8%AF%D8%A7%D8%AF-%D8%AA%D9%87%D8%AF%DB%8C%D8%AF-activity-7499816238756421632-mHI7
https://www.instagram.com/reel/DcqV0WHMZia/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/mohsentavoosiseo/964" target="_blank">📅 15:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-963">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چالش تیم پشتیبانی رفع اشکال گاهی اوقات اینه که سوال کننده یه مدیری داره که مدیرش تو اینستاگرام یه پست دیده که یه چیزی نصب میکنی روزانه کلی بازدید روانه سایتت میشه دیگه هم به گوگل نیاز نداری.
از تمام دست اندرکاران و فعالان حوزه جدی تقاضا دارم، ابزاری که صرفا با نصبش، بدون کار محتوا، بدون کار آف پیج، بدون اینکه درگیر بهینه سازی بشی، اگر راهی میشناسید که با نصب یک افزونه و ابزارو پلاگین، روانه صدها و هزاران نفر از گوگل یا هوش مصنوعی ها بریزن تو سایت شما و سفارش بدن،
به من یاد بدید و مبلغ بسیار بزرگی هم پرداخت میکنم بابتش. تمام پروژه های اجرایی خارجی که دستم هست(و واقعا سخت و زمان بر هست) و فروش محصول آموزشی(دوره) هم میذارم کنار کلا و میرم که توسط ابزار شما، جریان مالی خیلی بزرگتری برای خودم ایجاد کنم و صد ها برابر مبلغی که به شما پرداخت میکنم هم خیلی سریع در میارم.
سپس میام یک پست میذارم و رایگان آموزشش میدم و میگم بچه ها! کلا دور خودمون میچرخیدیم! گوگل ادز و SEO/AEO و متاادز و گوگل بیزنس/مپ ادز(زیرمجموعه همون گوگل ادز) و تمام کانال های مارکتینگ بیخود و اشتباه بود. هممون اشتباه میکردیم. یه ابزار کافی بود ما رو سریع و ارزون و راحت به مشتری برسونه.
بعد هم میزنم تو کار املاک و پاسپورت چند تا کشور رو از طریق خرید ملک میگیرم و بقیه زندگیمو به گردشگری، دوچرخه سواری در تابستان های سوئیس میگذرونم و یک صرافی بزرگ هم در مرکز امارات با شعب مختلف در سراسر جهان، تاسیس می کنم و میام میگم همون پستی که اون روز گذاشتم و exit کردم یادتونه؟ همه اینا رو از اون پست اینستاگرام و اون پلاگین یا ابزار بدست اوردم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/mohsentavoosiseo/963" target="_blank">📅 12:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-962">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به من گفت: "خب حقوقتو گرفتی"!
تو ده سال جلو بیفت.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/mohsentavoosiseo/962" target="_blank">📅 15:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-961">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تله دلسوزی برای شرکت
تو ویس گفتم "خلق کن"
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/mohsentavoosiseo/961" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-960">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تله دلسوزی برای شرکت
اعتبار به صورت نقلی منتقل نمیشه
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/mohsentavoosiseo/960" target="_blank">📅 15:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-959">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/mohsentavoosiseo/959" target="_blank">📅 15:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-956">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اینها رو تو اپدیت دوره پوشش دادم(اپدیت در حال ضبطه)
Agent بالاسر Agent
——-————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/mohsentavoosiseo/956" target="_blank">📅 11:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-955">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کلاد یا چت جی پی ای کدکس یا آنتی گرویتی گوگل؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/mohsentavoosiseo/955" target="_blank">📅 11:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-954">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">توضیح ویس های بالا و بحث سیستم سازی در کلاد و یاد دادن به هوش مصنوعی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/mohsentavoosiseo/954" target="_blank">📅 11:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-953">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen Tavoosi</strong></div>
<div class="tg-text">ویس من به تیم بعد از اینکه فهمیدند کلاد هم اخیرا ویس رو گوش میده و میفهمه و متن روان میکنه.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/mohsentavoosiseo/953" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-952">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen Tavoosi</strong></div>
<div class="tg-text">ویس من به تیم درباره ویسی که از سمت شرکت بروکر به عنوان ایراد محتوایی گفته درباره محتوای ما.
بخش ۲</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/952" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-951">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen Tavoosi</strong></div>
<div class="tg-text">ویس من به تیم درباره ویسی که از سمت شرکت بروکر به عنوان ایراد محتوایی گفته درباره محتوای ما.
بخش ۱</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/mohsentavoosiseo/951" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-950">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جواب اون سوال.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/mohsentavoosiseo/950" target="_blank">📅 12:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-946">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این ویدیو درباره این ویس (سراب پروژه گرفتن) هم هست.  تله شهرت! تله geek بودن.  تله دانش بالا. تله محصول نداشتن در ازای برند عدم توجه به فرسایش ذهنی    https://youtu.be/njtLVwnzyIY  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/mohsentavoosiseo/946" target="_blank">📅 12:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-943">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFdcIKVe9kVpErBHtqXUCdD_9fKSbzFUXcfCeEzrgXQ9gPaoyaPT2FWhNj63n-cWeB_aSId8kj7n2-zKvdX7Pw1yOA0pD135W0UfAySQQ0bB31xawTnWaXcBcms8NvHMnhP8Qpfhy-t7cn1EhTsFwwO_ECeTBZkFTNTKyYN4oFSXYYPla38TOVinI8oBzNQg0ZEQMrqC3yPYWl83ovu4gMRlnDjaUrsaoF8K3YZf88QaQsvBFHzU2Js0ZvBo502BUT8pjLNqxsqy7Cmsu6f2MLNVnWH-DL5qFF2Ipf9N6HaZ-4I-LF59Xo9tb4lL9mwN6n0jqz4GO532sKA6BVVaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faXZyQ5DxT3veSOKyptWk7jY9S9f-AD8W2PsnmI2vKubEtHfzHwCnjd5nXm5kWbz_323nPkjrcxNW_9ji62IRHTl3zEEUCkce_AZCgbajag-6vaC7PTs9iilDRyhQKZjQDiuU8HsGvzbJbTn9PeLtuE2jrueEzdDGaFUPMrrEdvCtTlZtOQxhvjxS32vh0k9OKC9yepIzMqLJqkf8lXxEGPKJo4pi-Fzry2yo3RaGFKooTjqYjiBJy_9KsWV9ykgTEP30n82ROVCrPzco8k41ddzLqsJTIJG1c1sofCjIE0T1Q71NgSxBQq2WmSDmPeX9VbyBJ2PPvKK_IJKBVVsxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBk2utBDM5Gi_zOL1-wtotjYpJ8gfhVPIpQFtiAvQ4VJZuVGtwz8YthLBH6iYmpTzC4fW7671CwwHyFuw5VVN68QRyh1D4gPGxr9vHK5aukLLC3pS4CQ8ECFpCmdjJeC-sth_JkCn0L0a7DaYVNbu8nlAE9vk05lNpouT95qT377QOPZhkaf-ZpyrJleSFjGWLuin4G7b4hMLtgPYn3_GV4ighF7ZWgEB6ooNTK5qxstnN6rjuVDOYXgdSMNCTLdeAZuA-xdVJXo0q_G5WDxCagK_VUKLuaRGyKjCEyoqE3DJK_9fDEoq5Uppi2ISArj3Ha_WfR8GOjzmJplC_qDxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس اول به نظر موفقیته. عکس دوم رشد کلیک ایمپرشن اسم برند هست در حالتی که رتبه فرقی نکرده. عکس سوم فیلتر رجکس غیر برند هاست که صفر هست آمارش!
روی سایت هم چند ماه هست حسابی داره کار میشه.
1️⃣
❓
ممکنه تبلیغ شده یا کمپینی بوده که موقتا اسم برند، سرچش زیاد شده؟
2️⃣
❓
ممکنه رو اسامی برندی رتبه نداشتیم که الان داریم؟ مثلا مشابه های اسم برند اصلی؟
3️⃣
❓
ممکنه اسم برند رقیب شبیه ما بوده باشه و اون سرچش زیاد شده ولی رو ما کلیک شده؟
4️⃣
❓
ممکنه چیزی غیر از موارد بالا باشه که هنوز ازش خبر نداریم؟
جواب من:
هر چهار احتمال رو باهم احتمال میدم. هر کدوم بخشی از تاثیر افزایش ده برابری کلیک هستند. در آینده واضح تر شد و تحلیل کردم میگم.
پی نوشت:
تحلیل و نتیجه گیری از نمودار پوزیشن روی بیش از یک exact query اشتباه فاحش و بزرگی هست. چرا؟
اینجا
و
اینجا
گفتم.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/mohsentavoosiseo/943" target="_blank">📅 00:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCrO4LCd8qm2QRKh4_GDXEkj4Yn4PGuxEjGVy3kyqlwRBB2Rg3zyb3ts2NkMw5_dyzOCGgPo6wl-58Nx3F8FqowwqYIWQdfwv44dyaed51Xa-xoanZ6sUUyFe_5ZktfBW2L6Ol1g3yz_nwm_Vs5KbdhZZRFTWxU5YefGRsogV5NtOVmHZZaiX8wkiX44Ogdd_MyKZEU_HIUynZwklxdh8i7kaGeYlacud1vydoOSYB0c942gMr9f7AFTUipbTaDnAVDBJAYp3d-SdbF66LO44AnGSjXhp4u8KHC290QaW53cP1xF_-ZetVQtCA6-oPTwS1qMnGjLdl-38TB9XwZ3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/mohsentavoosiseo/939" target="_blank">📅 18:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Overlearning
Unlearning
❗️
مهارت یادگیری زدایی و جلوگیری از زیادی یادگرفتن تو این عصر خیلی مهمه.
❓️
چقدر عمیق شیم؟ از کجا به بعد زیادیه؟ چاهی که از یادگیری زیادی عمیق و بیش از حد داریم می کنیم، به آب و چشمه و گنج میرسه واقعا؟
❓️
چجوری بفهمیم داریم زیاده روی می کنیم تو یادگیری؟
❓️
تله آدم های باهوش و با استعداد و قوی چیه؟
❓️
وسعت دید همیشه باعث بهبود عملکرد میشه؟
❓️
پرداخت بهای عمیق شدن بیش از حد، میصرفه به نتیجش؟
❓️
چجوری بفهمیم تو overlearning افتادیم؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/mohsentavoosiseo/936" target="_blank">📅 23:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">واقعیتش ترسیدم! جدی جدی چت رو بست!   خطرناکه! بنظرم یکی باید جلوی هوش مصنوعی و آنتروپیک رو بگیره. چرا باید یه ماشین لحن صحبت براش مهم باشه و بهش بربخوره و حتی کار قهریه انجام بده و اون چت رو کلا غیر فعال کنه!   پس فردا میاد کل اکانت هم لابد بن میکنه! پس فردام…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/mohsentavoosiseo/933" target="_blank">📅 14:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9n0QebIuBS2590VvNONXd2SpixDEBkA7EFXZI5GE22U-HTPLBXqRmCULI9TFvmOGfN-JMUyck9CB3NZ-Lf1wR1Fw6RSQKlIbXURxt0HSQvaZWuzC1jPpOXVZTdOkhEAdu1MjJaKnhQp3vF7VxrtHlajtVEevko1lJDfNUMh4S-xDvnYfllYDgENXSr8BzQj7-IHOpksc9RiYmSyuDKZ5Ngcjb9i3Wq0i-P8GhcH-RGAPNNBktKvuOfSSmR75qrRo189DMojVpBLAGF-LAgJWryappq2Awvq7pWmtCKSV-AB4pAtID3klXCsYVPMpg180Z8uw7z05EjutJw8iwR9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیتش ترسیدم! جدی جدی چت رو بست!
خطرناکه! بنظرم یکی باید جلوی هوش مصنوعی و آنتروپیک رو بگیره. چرا باید یه ماشین لحن صحبت براش مهم باشه و بهش بربخوره و حتی کار قهریه انجام بده و اون چت رو کلا غیر فعال کنه!
پس فردا میاد کل اکانت هم لابد بن میکنه! پس فردام میاد به ما دستور میده!
من برای اولین بار ترسیدم. این خوب نیست اصلا!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/mohsentavoosiseo/932" target="_blank">📅 14:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/931" target="_blank">📅 11:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ساختار سلسله مراتبی URL ها، یک احساس، بیش نیست. هیچ ربطی به درک گوگل از محتوا یا ساختار شما نداره.
+روش پیشنهادی بهتر
و حتما
ویس بعدی
هم گوش بدید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/mohsentavoosiseo/930" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/mohsentavoosiseo/929" target="_blank">📅 13:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
سرابی به نام پروژه گرفتن
❗️
به نام پروژه خارجی داشتن
❗️
فکر نکن تمام ماجرا اینه بلد باشی و حرفه ای باشی.
❓️
من به گذشته برگردم و کسی من رو نشناسه چیکار می کنم؟ محسن طاوسی ای که بلد هست ولی بدون ارتباطات و بدون اینکه بشناسنش، چه مسیری رو میره؟
مسیر من رو نرید. از من استفاده کنید. از دانش من. از تجربه من. ولی مسیر من رو نرید!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/mohsentavoosiseo/928" target="_blank">📅 11:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آموزش پایین اوردن نرخ تبدیل
😶
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/mohsentavoosiseo/926" target="_blank">📅 16:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صحبت از اپدیت شد، نیاز هست به دوستان یاداوری کنم، محتوای متنی و ویدویی من رو درباره بحث جاوااسکریپت ببینید حتما.
برای وردپرسی ها کاربرد نداره. برای سایت اختصاصی ها و دولوپر هاست:
سئو سایت های وابسته به اجرای جاوااسکریپت در مروگر
ارتباط جاوااسکریپت با هزینه های گوگل
سئو صفحات فیلتر دسته بندی فروشگاه - Faceted Navigation
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/mohsentavoosiseo/925" target="_blank">📅 16:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Mohsen Tavoosi – چرا آپدیت های گوگل آنقدر ها در لحظه مهم نیست؟</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/mohsentavoosiseo/924" target="_blank">📅 16:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چرا آپدیت های گوگل آنقدر ها در لحظه مهم نیست؟</div>
  <div class="tg-doc-extra">Mohsen Tavoosi</div>
</div>
<a href="https://t.me/mohsentavoosiseo/922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چرا آپدیت های گوگل اونقدر ها هم در لحظه مهم نیست؟
چرا نباید نگران اپدیت ها باشید؟
وقت تلف کن ترین کار ممکن، اینه که تند تند برید ببینید گوگل چه اپدیتی داد. رسمی بود یا غیر رسمی.
درست اینه که فرض کنید گوگل هرروز اپدیت میده. اونم چندین اپدیت. هم رسمی هم غیر رسمی. واقعا هم همینه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/mohsentavoosiseo/922" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">طنز:
موقع تهیه گزارش به کارفرما، وقتی پروژه ای 400 تا دونه کلیک داره در ماه، و 40 تا کلیکش کم میشه، میگیم، طبیعیه ده درصد کم و زیاد اصلا درست نیست در محاسبات و تحلیل بیاد در دنیای Organic Search.
اما وقتی 40 کلیک زیاد میشه نسبت به ماه قبل، 40 بار در گزارش، مینویسیم 40 تا کلیک اضافه شده
😎
✅
ولی واقعا، جدی، رشد و افت و درجا زدن رو باید همه رو نوشت. فاکتور هایی که هیجان الکی هست چه مثبت چه منفی هم باید نوشت.
✅
برند رو از نان برند هم باید جدا کرد حتما.
✅
میزان رشد ایمپرشن ها رو باید لحاظ کرد وقتی کیورد جدید رتبه گرفته ولی کلیک نگرفته.
کارهایی که فعلا باعث رشد نمیشه و حتی ممکنه باعث افت کلیک بشه ولی زیرساختی و لازم هست(مثل اصلاح تارگتینگ و هرس)، باید بهش اشاره بشه که توقع و انتظار طرف از نتیجه سریع، بیاد پایین.
❌
به هیچ وجه هم نباید نمودار کلی پوزیشن نشون داد از کل سایت. برای تک کیورد Exact اکیه. برای کل سایت، بسیار بسیار اشتباه و غیر حرفه ای هست.
اینجا
و
اینجا
رو بخونید.
متاسفانه بعضی ها که تجربشون بیشتر میشه فکر مکنن ایمپرشن کلیک ملاک نیست، میانگین رتبه ملاکه و شبیه پزشکان متخصصی عمل میکنن که زمان پزشک عمومی بودنشون، درمانشون بهتر جواب میداد. نمودار کلی رتبه برای کل یک دامنه، آمار بسیار بسیار تباهی هست.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/mohsentavoosiseo/921" target="_blank">📅 14:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKn5o2brUXt3L1ZHLQ6wp6VPQ5_QM1aQ-SPTwksqHj3bhGkIUZhNmaSAWHQ-gv3iyfvgWU5lNoExgV7Ph0WbpJRW4_7NP_YqDRNmbVn5A-ToDBy7xPg_feQVXHV7LSPIXiYOeWiq5ePI48vIp3PUdPS7OPyWNgTFiDQ9hN266wCjmw6mI2sStVWJJiiY6X6Y5ObCIf3wFvWOTCHOzCLNqGt6JkI__79tA9NrUdTDK7iWZlB2BGCbK72aYkN4ACCqk-ZTKvt2MuGCOSbH5LMZ0Gi5eJJJNrT4xlrSM5t91UdeS6hqvdfFRQHP-gY81gD83nIgSkgmu9fxv96woxmB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیچاره گوگل. عقبه هنوز.
تازه تو بعضی سایت های غیر فارسی بخش Generative AI داخل Performance اضافه کرده.
فعلا کلیک رو یا اصلا دیتاش رو ثبت نمیکنه یا تو گزارش نمیتونه بندازه. یا اصلا کلیک نمیگیره که برای من ننداخته. و طبیعیه که کلیک نگیره.
چرا بیچاره؟ چون خیلی عقبه. ما رفتیم تو آمار گیری از Generative Engine ها، این تازه بعد مدت ها آمار AI Overview خودش رو تازه داره میندازه. از گوگل انتظار بیشتری بود. ولی خب. خوبه باز.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/920" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">لیست بایگانی مقالات (پست ها) من که سال 93 , 94 منتشر شدند! یعنی 12 سال گذشته. از سایت web archive.
✅
که همچنان معتبر هست! و بسیار همین الان با پوست و گوشت، لمس می کنید! باز هم باید بگیم سئو عوض شده؟ اصول سئو همون اصول هست!
اون زمان کسی نمینوشت و فقط بلغور ترجمه در سطح وب بود.
ولی می تونید خط فکری الان من رو 12 سال پیش ببینید! حتی پست دارم با عنوان "عصر بی حوصلگی آدم ها! که متاسفانه تو web archive نبود.
هوش مصنوعی گوگل به زبان ساده
اشتباه نکنید! این مقاله سال 93 من هست!
چرا محاسبات ما در سئو غلط از آب در می آید؟
قوانین نانوشته گوگل
خاصیت تضریبی فاکتور های سئو
تشخیص رقابت کلمات کلیدی
(پست تلگرام رو اپدیت کردم و این رو اضافه کردم. جا افتاده بود)
تناقض های گوگل
بروز رسانی Freshness گوگل – تغییر لحظه ای نتایج با فرشنس
پرستش گوگل
114 فاکتور رتبه بندی گوگل
لینک بیلدینگ نکنید وگرنه پنالتی می شوید!
اینجا در نقد تفکر اون زمان بود که تازه پنگوئن نسخه های چندمش رو داده بود و همه ترسیده بودند که کلا دیگه لینک سازی نباید کرد. و این تفکر که بک لینک بی اثر شده. اون زمان هم بود. اون موقع من میگفتم A و T از EAT رو چیکار می کنید پس؟ بهرحال فعالیت اف پیجی حتی نوفالو نیازه. میگفتن نه فقط محتوا کافیه. محتوای خالی فقط E هست. اون موقع هنوز E دوم یعنی Experience نیومده بود.
سه راه پنالتی شدن در گوگل
روش های خروج از پنالتی گوگل و ریکاوری
تراست رنک
محتوا پادشاه نیست
قوانین گوگل درباره بک لینک
جهت اطلاع کسانی که تازه وارد سئو شدند، هنوز هم در اواخر 2026 همین قوانین هست!
برندینگ، دست برتر سئو
اولین ویدیو یوتیوب من سال 94
- بررسی چند موضوع رقابتی در ایران
(ورودم به سئو از 91)
اگر دوره من رو دیدید یا حتی ویدیو های رایگان من رو، ادبیات و لحن این مقاله ها، براتون آشناست.
همین مطالب هم متاسفانه بدون منشن و یاد کردن و چیزی، توسط بعضی از دوستان، از زبان خودشون مطرح میشه.
حالا همون محسن طاوسی 15 سال پیش، یک اپدیت game changer داره که کاملا تهاجمیه! و عملا انقدر بزرگه که میتونم بگم یک دوره است!
دوره تهاجمی سئو بین المللی با Claude . بدون مرز جغرافیایی و زبانی. برای اکثر مدل های SERP فارسی و غیر فارسی. که در حال ضبط هست و برنامم اینه قبل از پایان 2026 منتشر بشه و هرکس دوره رو داشته باشه رایگان دریافت میکنه.
چرا تهاجمی؟ Aggressive در اینجا به معنی شدید و طوفانی هست. تا نبینید متوجه نمیشید چرا اسمش این هست. برای همین سورپرایز هست. ولی انتظار رو پایین نگه دارید که بعدا سرخوردگی ایجاد نشه. فرض کنید یک آپدیت معمولیه. خیلی معمولی. سرفصل های حدودیش هم در صفحه دوره هست هم در
این پست تلگرام
.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/mohsentavoosiseo/919" target="_blank">📅 12:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-917">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به زودی به جایی میرسیم که اخاذی از skill ها و md ها و اسناد کلاد میشه.
ما بحثی داریم به نام پرامپت های چرخشی یا لوپ یا تکرار شونده. بعد بالغ شدشون میشن Agent.
پیچیده نیست ها! مثلا یه کار رو سه بار میگی چک کنی بازبینی و اصلاح کنه. بعد مامور(agent) درست میکنی که اینکارو انجام بده. بعد اون ایجنت رو میذاری سر کارش، هربار خودکار انجام بده.
چند وقت یک بار هم میری سوله مامور هات، بهشون آب و علف میدی و پیچشون رو سفت میکنی و برمیگردی پی زندگیت.
چجوری اخاذی می کنند؟
مثلا میدزدند فایل های شخص، شرکت و سازمان شما رو و میگن انقدر بده تا این همه زحمتی که کشیدی این سیستم و مستندات و مهارت ها و بلوغ رو که ساختی، بهت برگردونیم.
دو بیت کوین بده بهت پس بدیم. شرکت های بزرگ هم می ارزه براشون که این باج رو بدن.
من بخش سئوییش رو آموزش میدم تو اپدیت جدید دوره که در حال ضبطه. بخش های دیگه خارج از سئوش با خودتون
😎
البته سئوش رو استاد شید بقیش هم استاد میشید.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/mohsentavoosiseo/917" target="_blank">📅 19:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مقاله من حدود دوازده سال پیش!
March 2015!
ویرایش هم نشده. همون خاصیت تضریبی فاکتور های سئو، چیزیه که تازه بعضی ها دارن کشفش میکنن. یا بهش فکر میکنن.
من خیلی خوب بلدم پیچیده حرف بزنم جوری که فکر کنید واااای من حالا حالا باید دانشمو زیاد کنم تا بفهمم محسن طاوسی چی میگه. اما فایدش برای شما چیه؟
برام مهمه مخاطب من، یه چیزی دستش بگیره و اجرا کنه و فقط نمایش سواد من نباشه.
114 فاکتور رتبه بندی در گوگل
https://www.linkedin.com/pulse/114-%D9%81%D8%A7%DA%A9%D8%AA%D9%88%D8%B1-%D8%B1%D8%AA%D8%A8%D9%87-%D8%A8%D9%86%D8%AF%DB%8C-%D8%AF%D8%B1-%DA%AF%D9%88%DA%AF%D9%84-mohsen-tavoosi
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/mohsentavoosiseo/916" target="_blank">📅 16:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🟢
دوره جامع SEO/AEO بین المللی با AI
🟢
از این به بعد، هر ماه، قیمت به صورت تدریجی افزایش داره و دیگه اطلاع رسانی مرتبط با قیمت انجام نمیشه.
https://mohsentavoosi.com/course/seo/
آپدیت جدید، صفر تا صد سئو هست و سرفصل هاش این موارد هست که هنوز در لینک صفحه دوره قرار داده نشده و محتوای این صفحه، بعد از انتشار کامل این بروز رسانی جنجالی، به روز خواهد شد:
🟢
مباحث کار با هوش مصنوعی، OKF, Skill، اسناد AI، Memory، MCP, Connectors که جداگانه نیست و کاملا در فصل ها آمیخته شده است.
🟢
انواع SERP در گوگل در در زبان ها و کشور های مختلف
🟢
کسب رتبه در Google Shop (Merchant)
استاندارد سازی پروژه ها با هوش مصنوعی
آنبوردینگ انسان و Agent
🟢
کسب رتبه در کشور خاص، زبان خاص، یا جمعی از کشور ها و زبان ها یا به صورت کلی کسب رتبه و افزایش شانس نمایش و پیشنهاد توسط AI به صورت بین المللی (مثل
booking.com
)
🟢
ساخت پلاگین لینک داخلی خودکار با کلاد برای وردپرس با وایب کدینگ.
🟢
تحقیق بازار شامل Intent, Keyword و محدوده سوالاتی که از AI پرسیده می شود.
🟢
ساخت صفحات (تارگتینگ، کلاسترینگ به روش محسن طاوسی. نه اینکه هرکاری اکثریت کردند شما هم بکنید و فرصت ها بسوزند!)
🟢
سئو تکنیکال برای گوگل، بینگ و AI ها.
🟢
بهینه سازی داخلی سایت.
🟢
تولید محتوا با AI
🟢
کسب لینک از کشور ها و زبان های مختلف
کل بحث Off-Page
🟢
هرس صفحات و بهبود نرخ خزش
🟢
چند زبانه کردن سایت از نظر SEO
🟢
گزارش نویسی به هر زبانی
🟢
Local SEO برای بیزنس پروفایل ها
🟢
تحلیل و بهبود وضعیت در AI Generative ها
با تمام سرفصل های بالا، AI آمیخته شده است. کلا همشون با AI هست. بیشتر کلاد (اختصاصی از خود کلاد) و تا حدی هم Gemini
به سرعت در حال ضبط هستم. و تیم تدوین، در حال تدوین هست. از نظر خودم این اپدیت، سورپرایز هست! اما دوست ندارم چیز بزرگی در ذهنتون بسازید که بعدا انتظار ایجاد بشه.
این امضا یا مشابهش، از این به بعد زیر پست بسیاری از محتواهای کانال، قرار خواهد گرفت و اطلاع رسانی قیمت و... حذف خواهد شد.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/mohsentavoosiseo/914" target="_blank">📅 12:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/mohsentavoosiseo/911" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/mohsentavoosiseo/910" target="_blank">📅 14:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/mohsentavoosiseo/909" target="_blank">📅 14:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/mohsentavoosiseo/908" target="_blank">📅 13:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-907">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خطاب به همه کسانی که خیلی حرفه ای و باهوش هستند.
خطاب به کسانی که از اینکه یک سری بی سواد یا کم سواد حرف اشتباه میزنن، ناراحتن.
خطاب به همه با سواد ها!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/mohsentavoosiseo/907" target="_blank">📅 13:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یه اشتباه بزرگ کسانی که تازه مهاجرت کردند یا تازه درگیر پروژه های غیر فارسی شدند یا حتی مدت زیادی گذشته اصلا،
❗️
اینه که فکر میکنن جهان یا بین الملل یا "خارج"! یا کشورهای دیگه، همونی هست که ازش تجربه دارند و همه چیو با عینک خودشون میببنن.
❗️
❗️
حتی استناد میکنن که فلان همکار یا مدیر خارجی هم اصلا اعتقادش همینه.
❗️
❗️
❗️
در حالی که همون همکار خارجی هم اشتباه میکنه. اون هم فقط نگاه خودشو داره میگه و تجربیات خودشو.
✅️
در همه جای جهان(غیر از هند و پاکستان و اندونزی و روسیه و...)، لینک بیلدینگ و پست مهمان مشابه رپورتاژ، بوده و هست و خواهد بود.
✅️
مدل پیدا کردن و صحبت با رسانه ها در کمپین های روابط عمومی PR، یعنی کاملا کلاه سفید، بوده و هست و خواهد بود.
✅️
مدل اینکه کلا کمپین اف پیج یا PR و کلاه سفیدم ران نشه و فقط تبلیغ بنری یا گوگل ادز یا کلا کمپین های تبلیغاتی فقط ران بشه هم هست که سئوشون فقط تکنیکال و سئو داخلی و کیورد ریسرچ و ساخت صفحه میشه(اونم محدود).
✅️
✅️
همه اینا هست. فقط شرکت با شرکت، فرق داره. سایت با سایت فرق داره‌. هرچقدر بزرگ تر باشن شرکت ها، مدلاشون به مدل آخر نزدیک تر میشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/mohsentavoosiseo/906" target="_blank">📅 22:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سوال:   دوستان من یه دسته بندی رو آوردم بالا و رتبه ۴ صفحه ی یک هستش  اولین سایت که ترب هستش  ولی اگه ترب رو حساب نکنیم میشه سایت سوم طبق سرچ کنسول توی بازه ۲۸ روز ، ۱۲۹ سرچ داشته  ولی کلیک ۵ تا!! راه حل برای کلیک گرفتن چیه؟ عنوان  و متا هم از دو رقیب دیگه…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/mohsentavoosiseo/903" target="_blank">📅 20:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-902">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سوال:
دوستان من یه دسته بندی رو آوردم بالا و رتبه ۴ صفحه ی یک هستش
اولین سایت که ترب هستش
ولی اگه ترب رو حساب نکنیم میشه سایت سوم
طبق سرچ کنسول توی بازه ۲۸ روز ، ۱۲۹ سرچ داشته
ولی کلیک ۵ تا!!
راه حل برای کلیک گرفتن چیه؟
عنوان  و متا هم از دو رقیب دیگه خیلی بهتر هستش.
چون روی کلمه ی اصلی اومده بالا
پاسخ در ویس:
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/mohsentavoosiseo/902" target="_blank">📅 19:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-901">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سوال:   من از وقتی هاست سایتم رو برم روی Geo Dns میهن وب هاست یه مشکلی پیدا کردم. کلمات کلیدی تو سرچ کنسول رتبه دارن ولی وقتی خودم دستی سرچ میکنم نیستن. اکثر ساتیتام اینجوری شدن. این طبیعیه؟  پاسخ: https://t.me/mohsentavoosiseo/511 این ویس و ویس پایین  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/mohsentavoosiseo/901" target="_blank">📅 13:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-900">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سوال:
من از وقتی هاست سایتم رو برم روی Geo Dns میهن وب هاست یه مشکلی پیدا کردم. کلمات کلیدی تو سرچ کنسول رتبه دارن ولی وقتی خودم دستی سرچ میکنم نیستن. اکثر ساتیتام اینجوری شدن. این طبیعیه؟
پاسخ:
https://t.me/mohsentavoosiseo/511
این ویس و ویس پایین
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/mohsentavoosiseo/900" target="_blank">📅 13:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/mohsentavoosiseo/898" target="_blank">📅 11:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/mohsentavoosiseo/897" target="_blank">📅 15:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تولید محتوا با کلاد
استاندارد سازمان رو برای کلاد تعریف کردن
هوش مصنوعی، چت کردن و چهار تا فایل اتچ کردن و اسکرین شات فرستادن و چهار تا پرامپت خوب دادن نیست! اینا خیلی مقدماتیه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/mohsentavoosiseo/896" target="_blank">📅 15:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/846
بن میشیم نمیتونیم کلاد بگیریم!
Ban
#بن
#ban
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/mohsentavoosiseo/895" target="_blank">📅 15:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/mohsentavoosiseo/894" target="_blank">📅 15:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-893">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تفاوت کلاد تو چیه دقیقا؟ نسبت به بقیه AI ها؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/mohsentavoosiseo/893" target="_blank">📅 14:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67db1cde60.mp4?token=UZDVK-ENOe24_CBRSmZewiOO3zghTDfo6VLLUJab_x1H5coeK3kqE4v3wUrglQt3p8EbqX3FltqZbfmVjS7Xr8IuufY6UUNgpHre7q3uvFuHieqpbjKKryNmtS7O45iBFVPyTvJ7swxqxooaIH2w38wn9Dewh4U-mPKqGhcyYUQ6ukREjTp2uzf4JrPpTcwlCvGjNx580_WUc5NpAfyGqOx1qExY8PzFDYtkEamR0vBLRCw0k1qLyK8hskhcIzFPJ-atm2ZyVk5OwA6LX71dJglGPoCSuwc-y0vv8KT8OKOPl_3XY25PlULckEctQOVmxxo4-ooITpmezGwVnvmIkqeV9qhJhwoTvh1l2M6EHTaAWLcYVv94io94Q1rM333Lym_s0Wu2Et0ip-NsGeG3Lw4DUdvJ1q86cHAbRi9ktfF_hnTdwQtRE6NgVcz3VRRcjp27-07o9rBYG5vtj1WI-G3dyWxBBifCrcSyCYSUr-wPMcEEn1hEOK2r3x7F5jLUeHFIfW8JrwpjwY_zSxyKwVgyrkN5ISojsgAsuVXDOegMB06qd9SrOA-7REHCBAfAunIG2JIveDzxLItoWqYY-6pROsd1yEZS9Ge3gAtTAB3_5529ezSpISFe6cFyEk1uYtNA6jmDiOex0m4y-m0GMo8HlHjuy6ZaaiTWeZ-OfNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67db1cde60.mp4?token=UZDVK-ENOe24_CBRSmZewiOO3zghTDfo6VLLUJab_x1H5coeK3kqE4v3wUrglQt3p8EbqX3FltqZbfmVjS7Xr8IuufY6UUNgpHre7q3uvFuHieqpbjKKryNmtS7O45iBFVPyTvJ7swxqxooaIH2w38wn9Dewh4U-mPKqGhcyYUQ6ukREjTp2uzf4JrPpTcwlCvGjNx580_WUc5NpAfyGqOx1qExY8PzFDYtkEamR0vBLRCw0k1qLyK8hskhcIzFPJ-atm2ZyVk5OwA6LX71dJglGPoCSuwc-y0vv8KT8OKOPl_3XY25PlULckEctQOVmxxo4-ooITpmezGwVnvmIkqeV9qhJhwoTvh1l2M6EHTaAWLcYVv94io94Q1rM333Lym_s0Wu2Et0ip-NsGeG3Lw4DUdvJ1q86cHAbRi9ktfF_hnTdwQtRE6NgVcz3VRRcjp27-07o9rBYG5vtj1WI-G3dyWxBBifCrcSyCYSUr-wPMcEEn1hEOK2r3x7F5jLUeHFIfW8JrwpjwY_zSxyKwVgyrkN5ISojsgAsuVXDOegMB06qd9SrOA-7REHCBAfAunIG2JIveDzxLItoWqYY-6pROsd1yEZS9Ge3gAtTAB3_5529ezSpISFe6cFyEk1uYtNA6jmDiOex0m4y-m0GMo8HlHjuy6ZaaiTWeZ-OfNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/mohsentavoosiseo/892" target="_blank">📅 14:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سوال یکی از بچه های گروه دوره:
میشه بهم نظرتون رو بگید که چقدر تفاوت هست بین جمنای با اشتراک گوگل پرو و کلاد ؟
چرا کلاد انقدر محبوب شده و اقلای طاووسی هم دارن تاکید میکنن روش؟
تفاوت سطحش با جمنای در چی هست ؟
خصوصا برای تولید محتوا تجربه دارید جفتش رو مقایسه کنیم؟
البته چون اپدیت جدید در حال ضبطه این سوال پیش اومده براشون
😎
. پاسخ:
https://www.instagram.com/reel/DcBLYe_MLHx/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/mohsentavoosiseo/891" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پاسخ سوالات پر تکراری که درباره دو پست بالا پرسیده شد:
❓
آیا ما که قبلا دوره رو خریدیم دریافت می کنیم این اپدیت رو؟
بله! فکر کردید من شرکت های خودروسازی داخلی هستم؟ حالا که بازی قشنگ شده جدا شیم؟ شما همراهان قدیمی رو تنها بذارم؟ هوای شما رو که بیشتر باید داشته باشم! پشتیبانی هم دو نفره شده از دو نفر قوی. قدیمی های سال اول خبر ندارند پشتیبانی تلگرامی دارند. جایی دیدید بیفته دنبالتون بگه این ویژگی اضافه شده بیا دریافتش کن. قبلا پولش رو دادی. من میگم! الانم گفتم
😎
❓
این اپدیت چه زمانی منتشر میشه؟
شما تا پایان 2026 روش حساب کنید. خودم نمیدونم. در حال ضبطم. دوسه ماه طول میکشه حداقل. همین ماه البته فصل اولش میاد که البته سبک هست فصل اولش.
❓
من تهیه کردم ولی اون دوره بین المللی، توش خالی هست هیچی نیست!
بالاتر گفتم، اون رو تا اخر 2026 حساب کنید کامل بشه. کم کم میاد در حال ضبطم. اصلا هم نمیتونم عجله کنم. شما اون یکی رو ببینید. دوره سئو جامع. سوالات بعدی هم بخونید!
❓
به درد سایت فارسی هم میخوره؟
بله. ولی مثال های من به همه زبان هاست و کلا مبتنی بر زبان یاد نمی گیرید. مبتنی بر وردپرس هم یاد نمیگیرید. اما هر زبانی و هر CMS و برای وردپرس هم یاد می گیرید.
❓
برای چه سطحی هست؟
از صفر تا خیلی حرفه ای ها. همه. ولی کسی که تا حالا پشت کامپیوتر نبوده یا در حد لاگین کردن تو سایت ها بلد نیست یا تا حالا تو زندگیش فایل word باز نکرده یا بلد نیست وی پی ان استفاده کنه، نه ها!
❓
باید صبر کنیم اپدیت جدید بیاد؟
نه! ببینید دوره فعلی رو. دوره جامع فعلی که دسترسی دارید، کامل و به روز هست. اگر خیلی بی حوصله هستید از فصل "تحقیق کلمات کلیدی و صفحه بندی در عصر هوش مصنوعی" شروع کنید. همش مهم هست و موثر و به روز و کاربردی.
❓
میشه فقط آپدیت AI سئو بین المللی رو جداگونه بگیریم؟
کلا یکی هست! صفر تا صد هست. هوش مصنوعی جدا نیست. بین المللی هم جدا نیست. قیمت دوره هم بسیار پایین هست بخاطر جنگ. کلا امکان بخش خاصی رو جدا خریدن وجود نداره. یا همه یا هیچ هست.
❓
سرفصل های این اپدیت جدید که تصویر یک دوره جدید گذاشته بودید چی هست؟ تو صفحه دوره فعلی سر فصل های این اپدیت هست؟
اون عملا میشه محتوای فصل سئو بین المللی همین دوره جامع، که صفر تا صد سئو به هر زبانی و کاملا آمیخته با هوش مصنوعی(Claude) هست.
توی صفحه فعلی دوره، این سرفصل ها نیست. اما اگر بخرید، این ها هم دریافت خواهید کرد:
موضوعاتی که در آپدیت، پوشش داده میشه این هاست ولی دقیقا عنوان سرفصل ها این نیست. به دلایل متعددی، فقط کسی که دسترسی داره، عنوان ها و سرفصل ها رو دقیق میبینه بعد از انتشار:
🟢
مباحث کار با هوش مصنوعی، OKF, Skill، اسناد AI، Memory، MCP, Connectors.
🟢
انواع SERP در گوگل در در زبان ها و کشور های مختلف
🟢
کسب رتبه در Google Shop (Merchant)
استاندارد سازی پروژه ها با هوش مصنوعی
آنبوردینگ انسان و Agent
🟢
کسب رتبه در کشور خاص، زبان خاص، یا جمعی از کشور ها و زبان ها یا به صورت کلی کسب رتبه و افزایش شانس نمایش و پیشنهاد توسط AI به صورت بین المللی (مثل
booking.com
)
🟢
ساخت پلاگین لینک داخلی خودکار با کلاد برای وردپرس با وایب کدینگ.
🟢
ساخت دسته جمعی صفحات سایت با AI
🟢
تحقیق بازار شامل Intent, Keyword و محدوده سوالاتی که از AI پرسیده می شود.
🟢
ساخت صفحات (تارگتینگ، کلاسترینگ به روش محسن طاوسی. نه اینکه هرکاری اکثریت کردند شما هم بکنید و فرصت ها بسوزند!)
🟢
سئو تکنیکال برای گوگل، بینگ و AI ها.
🟢
بهینه سازی داخلی سایت.
🟢
تولید محتوا با AI
🟢
کسب لینک از کشور ها و زبان های مختلف
کل بحث Off-Page
🟢
هرس صفحات و بهبود نرخ خزش
🟢
چند زبانه کردن سایت از نظر SEO
🟢
گزارش نویسی به هر زبانی
با تمام سرفصل های بالا، AI آمیخته شده است. کلا همشون با AI هست. بیشتر کلاد (اختصاصی از خود کلاد) و تا حدی هم Gemini
جهت خرید، به
@mohsentavoosisupport
پیام بدید. من نیستم پشت این اکانت. بچه ها هستند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/mohsentavoosiseo/890" target="_blank">📅 18:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
قیمت دوره، قرار بود سال 1405 بشه 18 تومن. بخاطر دو تا جنگ و دی ماه، با مبلغ پایین تر در دسترس شد و از 1 شهریور(هفته دیگه)، مشه حدود 6. و سپس هر ماه یا هر سه ماه، افزایش قیمت داره. و طبق معمول، تخفیف دوره ای و مناسبتی هم نداره و هر ماه یا هر 3 ماه، افزایش تدریجی داره.
کاهش قیمت بخاطر جنگ بود و هست. کسی که پارسال 12 تومن میداد، امسال 5 تومن رو سخت تر از اون 12 تومن پارسال میده. درامدش فرقی نکرده و هزینه هاش هم سه برابر شده!
✅
به نقل از خود شرکت کنندگان دوره میگم که در هایتلایت اینستاگرامم هم گذاشتم:
اگر اهل یادگیری سئو یا نمایش یا فروش بیشتر در AI ها هستید یا میخواید اپلای کنید یا پروژه بگیرید، یا کسب و کار خودتون در داخل یا خارج رو به هر زبانی، گسترس بدید، اگر دوره رو ندارید یا نگیرید، احتمال پشیمونی و حسرت که چرا زودتر نگرفتید بالاست. به نقل از خود بچه ها.
❕
اما در عین حال، تضمین نمی کنم. هیچ تعهد و در باغ سبزی هم نشون نمیدم. صرفا هر آنچه دارم رو در دوره آموزش میدم که هر کس با من جلو بیاد، قوی، حرفه ای، بازای و تجاری و بین المللی و با زیرساخت درست بالا بیاد و آبکی نباشه آموزشش و
احتمالا
به چرخه عوض کردن دوره های مختلفش پایان بده.
🟢
قبلش تحقیقات خودتون رو انجام بدید. اگر ذره ای شک داشتید، تهیه نکنید. پولی که با شک پرداخت می کنید برای من جذاب نیست.
و در نظر بگیرید، برای کسب و کار خودتون، خرج نقدی میخواد. فکر نکنید فقط یادگیری هست. پول هم باید خرج کنید. مگر اینکه بخواید استخدام بشید یا پروژه بگیرید.
خرید در:
@mohsentavoosisupport</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/mohsentavoosiseo/889" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-888">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usi3Uryl3eud-OrHl1d6IwhuVyh2M-ubVtHmPd8UUW23Du3NqbeDJ6Q2_J5PKNOyAJXws6n2PHubSV0NSqDcnflVHlEgYahFKK3BB_kXrHmRQD3WKCSBYrGUx2dp2TmGkrBHot4ZTGlsuSqScDBlQVUxCZ5E1neeGMmmqwSac5DR5enJ2XZBkPRzTAv1BLSspdAA3ZhHXu5IrEW8agUH-ZhdWVfp7UauTnJkMDXUTKKS3wrBGrNsiy4sGl2v_zMZePXXB7z3FYKvPeebztTta9PYnbf1KLIhs5SuBkIMi0QHSwmplnXcgHcAVHQ3UNNXoyywW-1Ytxo3hYHDgZrGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسانی که جدیدا دوره رو میخرند، دو تا دوره دریافت می کنند(قدیمی ها نگران نشید تا آخر بخونید).
دوره جدید، برای راحتی ذهن شما جداگونه قرارداده شده و دوره صفر تا صد SEO و AEO برای همه زبان ها و همه کشور هاست! و کاملا آمیخته با AI که ابزار اصلیمون Claude هست. کلاد اختصاصی در محیط خود کلاد. نه این Opus که هوش مصنوعی های ایرانی و خارجی، میفروشند.
البته بگم من مثال هندی پاکستانی نمیزنم. ولی از شرق آسیا یعنی ژاپن، تا قاره آمریکا رو پوشش میدم. آلمانی، ژاپنی، ترکی استانبولی، روسی، فرانسوی، اسپانیایی داریم. فارسی و انگلیسی هم که سرجاش.
این آپدیت احتمالا تا آخر مهر کامل میشه و برای قدیمی ها در فصل سئو بین المللی قرار میگیره. و برای جدید ها، در این یکی دوره
هم
قرار میگیره.
خرید در:
@mohsentavoosisupport
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/mohsentavoosiseo/888" target="_blank">📅 14:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کلاد، برای هر متخصص SEO و هر متخصص دیگه ای ضروری هست و یک هزینه جاری هست. شما میگید من غذا نمیخورم؟ سوار وسیله نقلیه نمیشم؟ اجاره خونه یا پول قبض نمیدم؟
کلاد هم بهش اضافه کنید. بایدیه. اونم اختصاصی. نه اشتراکی. اصلا با محدودیتی که کلاد رو اکانت هاش داره اشتراکی معنا نداره. با این همه قابلیت، فقط چت نیست! باید اختصاصی بگیرید.
اپدیت دوره که تو همین شهریور یک فصلش میاد، کلا با Claude هست. کوبیدم از اول ساختم. نه فقط ایرانی و فارسی. نه فقط حتی انگلیسی! هرچند Base همون قبلی ها هست که الان هم تو دوره هست. فقط یک ابزار قدرتمند بهمون اضافه شده.
به زودی سورپرایز خواهید شد!
😎
پی نوشت:
(کلاد تلفظ انگلیسیش کلاد هست)، ریشه اسمش فرانسوی هست که میشه کلود. شرکت آنتروپیک هم آمریکایی هست.</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/mohsentavoosiseo/886" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ابزار های سئو خارجی رو به صورت اشتراکی از کجا تهیه کنیم؟ از سایت لیمیت پس! Limitpass.com ایرانی چطور؟ ابزار جت  سئو و کیورد چی و چند ابزار خوب دیگه...  http://limitpass.com/ https://www.jetseo.ir/ https://keywordchi.com/    کد تخفیف سه سایت بالا:  mohsentavoosi…</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/mohsentavoosiseo/885" target="_blank">📅 20:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یکی از
شاخص های سواد از نظر یونسکو
، توانایی یادگیری زدایی(unlearning) و یادگیری مجدد و توانایی استفاده کاربردی از دانش خود است.
خیلی از آموزش هایی که ما میبینیم فقط احساس یادگیری میده و چیز کاربردی یاد نمیده.
نه باعث افزایش درامد میشه. نه اپلای و کسب موقعیت شغلی بهتر، نه پروژه گرفتن و نه حتی نتایج و راحتی بیشتر و بهتر و کم خرج تر برای بهبود رتبه گوگل و شانس پیشنهاد شدن در AI!
خب الان فایدش چی شد؟ درک بیشتر تا یه حدی معنی داره. ارزش داره بری اتحاد، مشتق، انتگرال، اعداد مختلط، سری فوریه رو یاد بگیری که بعد بهتر بتونی مثلا معماری ساختمون انجام بدی؟ یا کد بزنی؟
اگه اعداد مختلط نون شد اومد سر سفره، یا ماشینتو عوض کردی یا خونتو یا دارایی هات رو یا زندگیت با کیفیت تر شد، قطعا مسیرت درسته.
حالا به جای این ریاضیات، هرچیزی بذار. از الگوریتم های گوگل تا مستندات و نحوه کارکرد مدل Fable کلاد تا... .
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/mohsentavoosiseo/884" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">با توجه به اینکه فصل اول اپدیت جدید، که یک دوره کامل جدید هست،
با عنوان "سئو بین المللی با AI با پوشش GEO/AEO" ضبطش شروع شد و زودتر از موعد(زودتر از آبان 1405)، منتشر میشه، قیمت دوره از 1 شهریور 1405،
⭕️
افزایش خواهد داشت و بین معادل 40 تا 80 دلار خواهد شد.
و طبق معمول هیچ کمپینی برگزار نمیشه و به جاش سال به سال، افزایش داره.
انقدر که آمیخته با AI (Claude) و مباحث بین المللی و چند زبانی و چند فرهنگی هست، برای من حتی تدوینش و ضبطش هم خیلی جذاب هست.
کسانی که به دوره فعلی(دوره جامع سئو) دسترسی کامل دارند، در فصل سئو بین المللی، این دوره جدید (اپدیت بزرگ) رو دریافت می کنند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/mohsentavoosiseo/883" target="_blank">📅 20:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
این پست حاوی ایده درامد دلاری و افشاگری پشت پرده هست. دست به دست پخش کنید که در جریان قرار بگیرید پشت پرده چه خبره یا خودتون ازش استفاده کنید:
این نظر سنجی که روش ریپلای زدم رو یادتونه؟
نتیجش این شد که من ورود نمیکنم بهش. ولی شما ورود کنید! در ادامه میگم چرا من ورود نمیکنم.
اینجا بهتون میگم ممکنه برای بعضی ها به صرفه باشه خودتون کاسبیشو راه بندازید:
(توجه: لینک ها درست هستن. با آی پی ایران نرید. من لینک غلط نمیذارم! راهشو پیدا کنید و باز کنید لینک هارو)
https://www.trendyol.com/google/gemini-pro-18-ay-kisisel-mail-e-davet-p-1098587629
این جمینای رو میده240 لیر 18 ماهه. یعنی حدود 1 میلیون تومن. یعنی اگه ویزامستر کارت داشته باشی میخری. اصلا نداشته باشی هم میخری. میدی برات میخرن.
حالا اگه خواستی کاسبی راه بندازی این میشه یکی از منابعت که ازش بخری و بیای بفروشی.
یا برای کلاد بری 150 تا Seat بخری هر کدوم میشه 20 دلار. از ریجن نیجریه میتونی تا 16 دلار و یک کم کمتر بگیری. حالا ریجن نیجریه رو باید با اپل آیدی نیجریه ای بگیری. برای هر 150 تا اکانت که میفروشی(max seats) باید یه اپل ای دی جدا داشته باشی. برای اپل آی دی جدا هم باید از نامبرلند یا هرجا شماره مجازی نیجریه بگیری. ریسک های از دست دادن اکانت اپل و شمارت هم در نظر بگیر.
بعد باید بشینی مدیریت کنی اکانت هایی که میدی رو. و اکانت هایی که تمدید نمی کنن رو. چون از کارتت سر ماه کم میشه مگر اینکه لغو کنی.
من خودم حدود ده تا دونه، یک مدت کوتاه اکانت chatgpt فروختم و خیلی ها هم دوباره پیام دادن که باز هم میخوان. یادتونه؟ چرا متوقف کردم؟ از کجا خریدم خودم؟ از اینجا:
https://www.trendyol.com/openai/chatgpt-plus-aboneligi-kendi-mailinize-davet-ile-tanimlanir-p-947506812
اون موقع میداد 100 لیر و دعوت نامه ای بود! بعد ناگهان تمام سایت های ترکیه، ناموجود کردند! همه با هم! الان میده 600 لیر. یعنی 13 دلار حدودا. باز زیر قیمته.
از اینجا هم میخریدم:
https://www.epinline.com/chatgpt-plusgpt-5dall-e-vip-1-ay-p-26417-m-1
این الان یک ماهه میده 350 لیر. میشه حدود 7.8 دلار.
آیا برای من صرف داره از اینجا بخرم 8 دلار بفروشم 18 دلار اصلا؟ کمتر از 20 دلار خود chatgpt؟ بله ارزش داره!
یعنی رو هر اکانتی که میفروشی حتی دو دلار کمتر از سایت اصلیش، باز بین 5 تا 12 دلار سود میکنی. گاهی هم ممکنه سودت در حد 2 دلار باشه.
این جمینای یک ساله رو میده 150 لیر. یعنی 3 دلار!
https://www.epinline.com/gemini-google-pro-12-ay-mail-adresinize-davet--p-27078-m-1
هزینه جاری خرید اکانت ها، مدیریت، پشتیبانی، تبلیغات و اینکه اطمینان کنن ازت بخرن هم در نظر بگیر.
من بخش اعتماد کاربر و اطلاع رسانیش رو داشتم. با بخش مدیریت و توسعه پذیریش به نسبت دردسر مدیریتش تا رسیدن به سود ماهی 2.3 هزار دلار به صورت غیر فعال(بدون درگیری خودم) اکی نبودم. اگه یه روزی بفروشم، همینه روش کار. حداقل پایه اش اینه. فعلا اصلا ظرفیت ندارم برای پروژه جدید باز کردن تو زندگیم.
و خیلی ساده با گذر زمان همه این پست رو یادشون رفته. من یه پست میذارم میگم اکانت میفروشم. خوبی تلگرام و اینستاگرام همینه که با گذر زمان کسی برنمیگرده پست های قبلی رو بخونه
😅
😎
شاید هم همین الان یکی از بات های فروش این اکانت ها مال منه! از کجا معلوم؟ خدا میدونه
😶
حالا به شما گفتم! قطعا برای خیلی ها به صرفه هست برن تو کارش!
هم سایت بزن هم ربات تلگرام. خیلی راحت با کلاد بنویس ربات رو با وایب کدینگ(همین الان بات احراز هویت و ارتباط با پشتیبان های دوره من، همینطوری نوشته شده توسط خودم با کلاد).
بعد هم پول بده تبلیغ کن جا بنداز پشتیبانی خوب هم بده. این بخش از خود تامین، سخت تر هست. اول فروش. دوم فروش. سوم فروش. بعدا محصول. قطعا باید بها بپرداخت برای اینکه بشناسن محصول شما رو و اعتماد کنن. خیلی بیشتر از بهای خرید و تهیه و تامین خود محصول.
رفع مسئولیت: من فقط تجربه خرید خودم از این سایت ها و دانسته های خودم رو گفتم. هر قدمی برمیدارید خودتون مسئولید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/mohsentavoosiseo/882" target="_blank">📅 14:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrdOUWtwffFNpitXDLoNZsIBHIqGrf4GlR6biiONnS5LrXzp2OfY1ny_10jFSRXb6-L2WZJAOdDHEnQ-LEBz9X6djcVNvPXObLK66bbPLjYnycGFhOs2nf-Kki8kr_drOBDGYroYd9EvqE8Mt8Ytr8CkG6dei8Fugn8jz_ENAIza-M3mjWBexL78On2JO12FCTY4bvsFDu4RMLRycdYV1ifecH0Biyy67IHq2Z-T5NGqiY-c-BoGQLodYuRa0s_FsYvK4B8PrHm-MwH7NQjJDmy06_LxACyo9W86r18F8QG_igIIJu9HldTeRbFAeVveD5SxzUR9Sfj12YcL1dNYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یکی از ساده ترین هنرکاری های کلاد هست! از منوی رفلکت، بهتون عملکرد خودتونو میگه و واقعا بازخورد های جذابی میده! در اپدیت پیش روی دوره، تمام کسانی که دوره رو دارند، سئو بین المللی با کلاد رو به خشن ترین حالت ممکن یاد می گیرند
😎
.
به من گفته:
ایراد هایی که از skill ها و عملکردشون میگیری، به خاطر دستورات خودت وسط کار هست و یادت میره که خودت خرابش کردی!
😅
یا گفته فلان جا حرف من رو بدون سند رد کردی و هنوز میگه تو اشتباه کردی!
بعد میگم کلاد خداست میگید نه! بازم میرید از فلان جی پی تی، ایرانیش رو میخرید؟ خیلی فرق داره! اختصاصی بگیرید. کانکتور و اسکیل و داکیومنت و کوورک و... تو اختصاصی هست فقط.
mohsentavoosi.com/1
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/mohsentavoosiseo/881" target="_blank">📅 15:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7_-UFXRRRv9sGUIQ_q9S_05iS5IWTyEITRGPx1ZiJyj_hIJJB3VeN1zyO5TQxBynokT0UlCzDZb3Y-NrkTpjgAFpaUOrZnemZdlB2ULXdHf2mu5gcQKbCOdijfo9z3IJkcm3snKAVA2WWFs0l1PrsjhBOKobWajI3EWJIwTdZ4XTq1Ive5fhX0felLNYx07GIvgUlw4n_smYsviPBQdA9lJOhp0Y30a3ytfvGePL-io5KXS86cRRY8jkw4uhNC0hE0pIrJPIsjMD0e33CZtGkHPfGfEXjnuc_2XpiWw9_B2h0HgkFQiagFy84R2V5GiK-htWqL3HmOmKbeQF9NRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❓️
از کدوم هوش مصنوعی استفاده کنیم؟
کلاد
❓️
با چی ایجنت بسازیم؟
کلاد
❓️
از ایجنت کدوم هوش مصنوعی استفاده کنیم؟
کلاد
❓️
از کدوم مدل ها LLM ها استفاده کنیم؟
همه مدل های کلاد. Haiko. Fable. Sonnet. Opus.
❓️
از کدوم AI های اشتراکی یا api داخلی غیر فیلتر استفاده کنیم؟
هیچ کدوم. فقط کلاد اختصاصی.
❓️
برای کد نویسی از چه AI استفاده کنیم؟
Claude Code
❓️
برای مدیریت تسک هامون و انجامشون چطور؟
Claude Cowork
❓️
برای تولید محتوا؟
کلاد
❓️
برای مردن؟
کلاد
❓️
برای...... انقدر سوال نپرس. پاسخ:
کلاد.
❓️
جایگزین کلاد چیه؟
سوال گستاخانه ای بود.
❓️
از سایت های ایرانی کلاد اوپوس گرفتم. خوبه؟
پناه بر کلاد
😭
❓️
چیکار کنم دیگه هی نگی کلاد؟
از کلاد بپرس.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/mohsentavoosiseo/879" target="_blank">📅 20:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-877">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خیلی مهم و جالب درباره گزارش نویسی و عملکرد و نقد کار خود، در ویس پایین.  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/mohsentavoosiseo/877" target="_blank">📅 13:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-875">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH9wmoE3IoUfQj4qHePkvkxMbTHiv-HpuZYKoDY2wXFNRpaGmV1tuSyg88OixopgR-1VHYQlbQts7lE962XRj8HzVaLbA8UXbvLlwunag0yJMTVyvDDkqlaeEwJqOHkSjxJv9ZGiGiz998oVIxBgsOegWvEX8IHjhLShiZ0h7a9Hmz0p0R64Spi_wW3l792YqhA6yEFf-BSG6FbQDeIjxBfsjcq_kLRUNQ0LEc46g5PCUCUmuh3zHWBbratwFTwKBFVGJKYiz0609Lpfl9DxCxBxbolTaSuzaQ8-Z89WO5kjvJB-oFrNW7jFjbXOTlPZxbyQwhJz0lMfwwwtKyyumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی مهم و جالب درباره گزارش نویسی و عملکرد و نقد کار خود، در ویس پایین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/mohsentavoosiseo/875" target="_blank">📅 13:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvZv7SJmqB-QiLDbte7EPgRK8BuFyWZHNfJaL9Nx3urLK8bKoHx9GEh74jt1UvlagIAPCafZD9_N5dmHd3pMDN0BZra5oYVwh5QwGWJNsYWXx8V5mkpoTjTNkPHN5WDn0k5sjrPpCgdTFoMxK3PRl92PDN_W1VLMVyOTpdX8oHbgs_0qmojCIn2fh0S2zG77nboBCbdW6rPZLdz91oPjJajb-nV36SOqcer1H5aNHDc2ahMBUFRyadv7VXTd5j0RB0U5JfSvTMD-5H0IcxHUcSYj_iv71tUQJKidenRDNnJ_EPmmm9OMvp7ewYACEClL7WLo4-GiRhCwxoRuwbWMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJQkTZfvo5voxazdoxW-0H0HzqiWfvFbxizVbzj1Ybv2SoQR4Ot_aV4fQZ6BebnetgEGSEt-WYgx4fYcUkRB9yOR020VtaWKWREs3L9t4H9JZANOd0yyDy2xTG3eNBGfk1-Fw40b1ZZf2bQ0ebsq1QdTi93AsyraEKn_4ZTEjGU5eVh73lKqo3CfKTZ6VFaLpC5dd4mmhBm_EKdqyMvBwmrEVZ3lAiOTaWFDpnuqaNgT5-yvqjcCBHi2643NdY9SrCOmHOM1Ic3CK9vVyhAwJqt4YwKkHQzOK8EynYSP8EeopwqCKlFAQmtbEXkY7_6tabq0B9Rs9MS3QgBiFk0BRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصویر چهارستونه(گرونتر) برای ابزار keyword tool هست و تصویر سه ستونه(ارزون تر) برای ابزار Mangools که ایرانی ها به KWFinder میشناسنش.
شما خودتون رو بذارید جای سایتی که ابزار اشتراکی میفروشه.
منگولز، روزی 500 تا سرچ میده. هر منگولز رو به 20 نفر بده، میشه روزی 25 تا برای هر نفر. نفری 2 دلار میشه هزینه خودش. کلا 40 دلار برای 20 نفر میده. میتونه تو پکیج کلیش بگنجونه.
حالا اگه کیورد تول 390 دلاری رو بده، 200 تا در روز داره کلا. به 20 نفر بده هر نفر ماهی 10 تا سرچ داره(بجای 25 تا) و نفری 20 دلار میفته براش. یعنی با دلار نرخ امروز نفری 4 میلیون تومن فقط یه دونه اشتراکیش! فکر کن حالا بخود بیاره تو پکیج هایی که حداکثر یک یا یک و نیم میلیون تومنه!
به من بگو دقیقا چطوری باید این کارو انجام بده؟ در یک صورتی میتونه! اینکه یا جمع کنه بره یا خیریه باز کنه به همه از جیب خودش ابزار اشتراکی بده.
این رو برای مخاطبین خودم پرمیوم هستند نگفتم. چون شما همه چیز رو با دید تجاری پخته نگاه می کنید و نمیگید اااا چرا گرون شد چرا نیست. میفهمید پشت قضیه چطور هست.
برای کسانی گفتم که دید تجاری قوی ندارند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/mohsentavoosiseo/873" target="_blank">📅 12:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تیم پشتیبانی رفع اشکال دوره تغییر کرده، دیگه یک نفر نیست و روز های تعطیل آخر هفته هم پوشش داده شده. مگر تعطیلات خیلی بزرگ یا استثناها.
که سرعت پاسخگویی بالاتر بره.
نه تیکتی هست نه لزوما تایپی. نه وبینار هست که بخواد ساعت خاصی برگزار شه و آزادی زمانی شما گرفته بشه یا مجبور باشید تو روزها یا ساعت های خاصی آنلاین بشید. چت تلگرام هست. بهترین حالت ممکن.
البته قبلا هم چت تلگرام بود!
خیلی از شرکت کنندگان دوره، خبر ندارن و کلا از چیزی که دارند استفاده نمی کنند.
من که مشکلی ندارم استفاده نکنید
😎
. سر بچه ها خلوت تر میشه راحت تر هستند
😎
. ولی استفاده کنید کنتور نمیندازه! نمیگیم چرا زیاد سوال میپرسی! نمیگیم چرا هر چی توضیح میدی ما نمیفهمیم! برعکس کمک می کنیم سوال رو درست بتونید بپرسید. خیلی راحت هم اگر خارج از سئو باشه یا بلد نباشیم، میگیم نمیدونیم!
"نمیدونم" گفتن تو فرهنگ ما (تیم محسن طاوسی) تابو نیست. برعکس، کسی که همه چیز رو میدونه، احتمالا کلا چیزی نمیدونه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/mohsentavoosiseo/872" target="_blank">📅 12:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سوال یکی از بچه های دوره در گروه دوره:
من سئوکار یه مجموعه هستم
قرار هست یه سایت دیگه هم بالا بیاریم و کارفرما میگن که کل محصولات همه چی رو یه صفحه باشه(  صفحه اصلی)  و تمامی فیلترها مثلا ارزان ترین گران ترین و تمامی محصولات بیاد صفحه اصلی.
و صفحه تک محصولات و درگاه و تمام
و ن لندینگ ن کتگوری هیچی هیچی
همه چی داخل صفحه اصلی
و من هرچی توضیح  میدم که این اصلا منطقی نیست از لحاظuxدرست نیست از لحاظ سئو چالشی دارید نمیشه کار کرد از همه لحاظ مشکل داره اما اصرار دارن که همین باشه.
حوزه سئویی هم حوزه خیلی سختی هست
چه پیشنهادی دارید؟؟
پاسخ:
اگه یکی اصرار کنه من ماشین با چرخ چهارگوش میخوام شما چون مکانیک یا خودروسازی باید بگی باشه؟ ولشکن کلا. نمیشه. اون کارفرما دید و اطلاعات حداقلی نداره. ولی شما که دارید.
نکته برای سوال کننده:
شما یو ایکس رو ولکن. چالش داره از نظر سئو درست نیست! کلا نمیشه. چالش یه چیز کوچکتر و معمولا قابل حله. نه یه زیرساخت مهم اصلی که بخواد وجود نداشته باشه.
و قطعا شما قاطع نگفتی نمیشه. داری چونه میزنی. اونم میخواد چونه بزنه. تخصصشو نداره که. از مدل سوال که نوشته شده "چالش داره سئوش" مشخص هست خود سوال کننده محکم نگفته نمیشه. خودشم شک داره. بدیهیه که کارفرما که دل خجسته ای داره بنده خدا و اطلاعات نداره چونه میزنه و اصرار میکنه که بشه. من ایرادی تو کارفرما با توجه به سوال(بخش چالش) نمیبینم. اون حق داره بخواد. شما حق نداری ببری رو اصرار و چالش و موضع غیر محکم. پاسخ انجام یک چیز چالش دار و با فشار نیست!
پاسخ یک "نه" و "کلا نمیشه" صد درصدی بزرگ و قاطع هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/mohsentavoosiseo/871" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">درباره کمپین تبلیغات محیطی ا.......پ
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/mohsentavoosiseo/870" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/mohsentavoosiseo/869" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/737
صفر تا صد مشکلات ایندکس شدن صفحات سایت.
❗️
دست و پا نزن برای به زور ایندکس کردن.
✅️
7 چیزی که باید چک کنید. تمام پاسخ های من به این موضوع
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/mohsentavoosiseo/868" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دوستانی که ایران نیستند،
با توجه به اینکه اپدیت پیش روی دوره، بسیار تمرکزش سئو بین المللی و چند زبانه و مبتنی بر هوش مصنوعی هست،
و اسپات پلیر هم دوباره از وایت لیست خارج شده و از خارج دوباره در دسترس نیست و دیتا سنتر ها دوباره محدودیت هایی برای دسترسی از خارج به داخل اعمال کردند،
اگر نیاز به وی پی ان ایران دارید به دایرکت همین کانال(آیکون پیام یا کلید message) پیام بدید تا وی پی ان ایران براتون بفرستم. وی پی انی که خودم استفاده می کنم (میخرم).</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/mohsentavoosiseo/867" target="_blank">📅 12:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چرت تر از دو جمله زیر نمیشناسم تو زندگیم:
❌️
درخت پربارتر افتاده تر است.
❌️
هرجا خبری هست ادعایی نیست.
بولشیت کامل. Absolutely nonsense.
مغز اصلا نباید دنبال این باشه که کی متواضعه کی پرباره. هر قسمتی که برامون سودمنده بصورت متغیر و داینامیک و قسمت شده، بر میداریم و استفاده می کنیم.
❗️
نمونه انسان ها و شرکت های سوپرموفق و پر ادعا و متکبر و غیر متواضع:
✅️
استیو جابز. هم بنیانگذار اپل و مخترع صفحه نمایش لمسی و اسکرولی که همین الان گوشی ها دارند و کلی چیز دیگه.
اخلاق گند مرحوم به گوش همه رسیده.
✅️
تراویس کالانیک، هم بنیانگذار اوبر که بخاطر اخلاق گندش از شرکت خودش به عنوان مدیرعاملی اخراج شد. همچنان ثروتمند و صاحب شرکت Atoms هست که ربات تولید میکنه.
✅️
هنری فورد! شرکت بی نظیر خودرو Ford
✅️
ارسطو اوناسیس، غول کشتیرانی یونانی قرن گذشته.
✅️
لاری الیسون. هم بنیانگذار اوراکل.
✅️
پابلو اسکوبار. قاچاقچی و تولید کننده معروف کوکائین مدیین کلمبیا(مدلین که همه میگن غلطه. ل نیست. ی هست. Medellín) سی چهل سال پیش. راستی خلافکارای موفق چی؟ ادعا باید داشته باشن یا باید متواضع باشن؟
هزاران مثال می تونید در طول تاریخ پیدا کنید. کلا من با گره زدن اخلاق و کسب و کار یا موفقیت، مشکل دارم.
قطعا مرتبط و موثرند روی هم. قطعا اخلاق و انسانیت مهمه. کسب پول از راه سالم و بدون دروغ و فریب و دزدی و... مهمه. آسیب نزدن به کره زمین، طبیعت، آدم ها، همدیگه و حیوون ها مهمه و ضروریه. قطعا مهربونی با حیوانات نشانه ای از تمدن و انسانیت هست و بدرفتاری باهاشون نشانه عقب ماندگی و بربریت.
ولی خیلی گوگولی و کودکانست اون دو جمله بولشیت اول این پست درباره تواضع و ادعا.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/mohsentavoosiseo/866" target="_blank">📅 13:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/mohsentavoosiseo/864" target="_blank">📅 12:32 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
