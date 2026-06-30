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
<img src="https://cdn4.telesco.pe/file/GoxK92jFV1TD4kSacUT0namVFn_4mZHzbld4AdeZRTyZUvQK3LX8-qrXbdECKfsvB8KxpghfmuK2m5h9R5A5dAqdT4tcQtdUrUuXqOnhzmTZSeT3GzPjn_0UO6DKWkILbfUlaPbtww67hdjGMpe7EeYQByyydbTSLOqRtqGxxXEzzgprf5DK1mJm6pUI0NlsdXNX2H22kIiMsD401o0VH8il0UBaDjBFSWLNpXjKy-MfUr9K7tXgFOcL8PUcDufH8xGSWGtGtVpCjhLWNxmfHqezdOjrLn8eFO8IuqsFTmRt9kLMzxr3m-OAjt4xkG_PK6-huLK-8CkZr_AXKZ3o9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.17M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 13:56:39</div>
<hr>

<div class="tg-post" id="msg-664921">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
قطر: هیچ دیدار سطح بالایی بین آمریکا و ایران برنامه‌ریزی نشده است
سخنگوی وزارت خارجه قطر:
🔹
ویتکاف و کوشنر در دوحه هستند و مستقیماً با مقامات ایرانی دیدار نخواهند کرد.
🔹
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است./جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/664921" target="_blank">📅 13:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664920">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc7a470172.mp4?token=TwBLcXBGbeUOXGZjSXy3BoCpuUewQKaSqpCzBHYEPvzA8rbHxNHwU23X8s3sakREnw4bZcHDUY8yw0W3iC7puk1yrXyW_x48o0tOhq-HuTHqE0w08zvBBy-ZzThwQxygz278CGqvVyiVcAiPyoYmbU--gv8L1WtebVgtB7AOM9K0-U_u0GbhM4fm6ky9Gbay51mRvdeAo9vN-3WCTxvg9T9Q5nUj8dr4g6F8atga66k87HTxNVRt1L5PqaI-0Kp-6TDFfIidiuz1rnObApZBYNxve5RB5aEqTcHGAD1R6K6aRTj1JOK0zZDmh_lxx2MPhmlc_XDj8c5kw4Ytg7LpTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc7a470172.mp4?token=TwBLcXBGbeUOXGZjSXy3BoCpuUewQKaSqpCzBHYEPvzA8rbHxNHwU23X8s3sakREnw4bZcHDUY8yw0W3iC7puk1yrXyW_x48o0tOhq-HuTHqE0w08zvBBy-ZzThwQxygz278CGqvVyiVcAiPyoYmbU--gv8L1WtebVgtB7AOM9K0-U_u0GbhM4fm6ky9Gbay51mRvdeAo9vN-3WCTxvg9T9Q5nUj8dr4g6F8atga66k87HTxNVRt1L5PqaI-0Kp-6TDFfIidiuz1rnObApZBYNxve5RB5aEqTcHGAD1R6K6aRTj1JOK0zZDmh_lxx2MPhmlc_XDj8c5kw4Ytg7LpTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شب سقوط غول‌ها؛ آلمان و هلند حذف شدند، برزیل در دقیقه ۹۶ از کابوس فرار کرد
▪️
قسمت دهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/664920" target="_blank">📅 13:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664919">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
اطلاعیه شماره یک قرارگاه برگزاری آیین وداع و تشییع قائد عظیم الشان شهید امت (تهران)
🔹
از هموطنانی که قصد حضور در مراسم را دارند، درخواست می‌شود اطلاعیه‌های رسمی را دنبال کرده و با عوامل اجرایی همکاری کنند.
🔹
برای کاهش ازدحام، زمان حضور خود در تهران را کوتاه نگه دارید و در صورت نیاز از امکانات اسکان و خدمات پیش‌بینی‌شده استفاده کنید.
🔹
همراه داشتن وسایل ضروری مانند دارو، کارت شناسایی، آب، خوراکی خشک و پتوی سبک توصیه می‌شود. از لباس خنک، کلاه یا چتر استفاده کنید و از آوردن کودکان، بانوان باردار، سالمندان و افراد دارای بیماری‌های سخت به محل‌های شلوغ خودداری شود.
🔹
اطلاعیه‌های بعدی از طریق رسانه‌های رسمی منتشر خواهد شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/664919" target="_blank">📅 13:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664918">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg5YDEz05N2n583WdPicuyU0UFmR9VEU6rHOdPQhGaNwx06drZwb4bXG6KmIVf5MEA7UV8-shKsHpuVPe9JvFWLHaakIK9i5NdQNGzDyhrHPosDusbiUQUsJ_PXdEICmrtbumT5JZ4cjxBn0-Ore2LOo6UigfgiyFq01-vwZh74yAYlLXRgW_uZAwCbmL8-tMxjAglAA3sv28_p9W3Gc3ezK-p53THTMlyDb0zyBXhOfm-ZMEM8We6x0iKJb6QyOAHSUCk5QrBz4B5eerti_2G4Lb039SGR34-1NvH-gZFkCZuRsyiT9RwGVZrrLHTyxMHjM8X6vBVslWQE20kBEjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنان در کدام کشورها به‌طور قانونی حق موتورسواری ندارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/664918" target="_blank">📅 13:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664917">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد  دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید:
🔹
در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/664917" target="_blank">📅 13:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664916">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
هشدار سیلاب و آبگرفتگی برای ۸ استان صادر شد
سخنگوی سازمان مدیریت بحران کشور:
🔹
در ارتفاعات مازندران، سمنان و تهران و همچنین در استان‌های آذربایجان شرقی، اردبیل، گیلان، البرز و گلستان احتمال بارش‌های رگباری، نقطه‌ای و وقوع سیلاب وجود دارد و این بارش‌ها می‌تواند باعث طغیان رودخانه‌ها و آبگرفتگی معابر شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/664916" target="_blank">📅 13:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664915">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نخست وزیر عراق: اجازه استفاده از خاک عراق برای حمله به کشورهای همسایه را نمی‌دهیم.
🔹
وزارت ارتباطات عراق از برقراری اینترنت رایگان در مسیر پیاده‌روی اربعین -بغداد به کربلا خبر داد.
🔹
ترکیه: آمریکا قصدی برای خروج از ناتو ندارد.
🔹
کاروان تیم ملی فوتبال فردا به کشور باز خواهد گشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/664915" target="_blank">📅 13:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664914">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
قیمت جدید شکر و برنج اعلام شد
🔹
قیمت هر کیلو شکر در بنکداری‌ها ۹۷ هزار تومان
🔹
قیمت هر کیلو برنج ایرانی  ۲۹۰ تا ۴۶۰ هزار تومان
🔹
قیمت هر کیلو برنج پاکستانی ۱۹۰ تا ۲۶۵ هزار تومان و برنج هندی ۲۴۰ تا ۲۶۵ هزار تومان /باشگاه خبرنگاران جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/664914" target="_blank">📅 13:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664913">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون انرژی اتاق بازرگانی: مردم دو ساعت کمبود برق را تحمل کنند تا برق صنعت قطع نشود!
آرش نجفی، رییس کمیسیون انرژی اتاق بازرگانی ایران در
#گفتگو
با خبرفوری:
🔹
پیشنهاد ما این است که به جای قطع برق واحدهای تولیدی، مردم روزانه دو ساعت کمبود برق را تحمل کنند تا تولید کشور متوقف نشود؛ چرا که تداوم تولید، ضامن درآمد و پایداری اقتصادی است.
🔹
به دلیل نبود رگولاتور و نبود نهاد تنظیم‌گر، وزارت نیرو در قیمت‌گذاری، سیاست‌های حمایتی و مدیریت برق هرطور که دلش بخواهد عمل می‌کند و این عدم شفافیت باعث می‌شود مطمئن نباشیم که رویکرد و عملکرد کاملا صحیحی از وزارت نیرو دیده می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/664913" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664912">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
تهران ۳ روز تعطیل شد
🔹
به مناسبت برگزاری مراسم وداع، نماز و تشییع پیکر رهبر شهید و خانواده ایشان، تهران به مدت سه روز تعطیل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/664912" target="_blank">📅 13:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPfVX4zu520_Yr4HJJ6ErCzzUKfo2slAOp3B2xgTN0hvMkbRa0yEJDuOL6q_5xdiQcLVIuAnYgkLo1m1RYIPN-u6VTiOTStyZrD2P8vYmK5vzwNmE7zPNGyPwmn8ynlLGk83SeCU1hHjnuayhHI9PrsIjTP1OP-EQDNDADuKxZhR0I45s8jIrHpt2MEiRIla5P7w09p1TxeTb1mmBCYYlqOMhxu3Fy38jfYh3g2mzHRjrYdFe2r5N3GbtDtipvdf-7QQPGOv0ZODerWVOts7qrRIc0xWFbotDP_DVct_sf8twqiqDvh96ZDlP6iAUnfwXxQbvIAdmTfWsEX9uzuJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرونده جنایت‌ شیاطین زمان نباید مشمول مرور زمان شود
🔹
مسئولان موظف هستند عاملان این جنایت را به میز محاکمه بکشانند؛ عدالت و تقاص، تنها پاسخ معتبر به این تعدّی آشکار است.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/664910" target="_blank">📅 13:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664908">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huTQHTdOH29c43jEiTHWFSKXM3p-x1vD8HZShMQl-wdj7JWPaJNVNtAkXT-f7bXYQ6XQS07jZrSDJw5sjirmBuwdMX-x2pr3PXMBmtjKmIVqMxBGftbmOJJ3JZG7Bvv2Ikpn5hB0uMP1lueHLArdGQ5QD3UwUK3P0wgWzuD9ss_nrYx4bwGoWNL7bciFya7enLqPvv79rJeSvQzWufkDv58elivIL6corKJ7u3zFeYlAzugPhZNo0rNzW3mYE89NpTGSFIbXlal1XXdJq7bR2lgAiQ8qeJ5U5RaWcNzz2rpu3dwsY4n7R6YGj1bRsHodDjCGUJ03_62Rvp_lUnWLCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله‌ تظاهرکنندگان به دفتر هواپیمایی اسرائیل (ال عال) در تهران؛ ۱۳ آبان ۱۳۵۷
🔹
کاوه کاظمی/گتی ایمجز
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/664908" target="_blank">📅 13:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664907">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f984c921ab.mp4?token=scaJshaWOLjJOlfkqbav8RGuEtJ7YC8yiKtlv6h7abwGWZwZKYsCodQ0kMnWOxP3j9zQJT3kSSqULvlr-JJjl3tQNQgHpToDz9KW92M_OFt0bWETkv6e2himWI-1qeEy4xnfLghPILzFhUgaDx3gnXpodGZ_Z_g7gDNPL6SrOepJpG9AmWwf3TZhknHKtcBuquwtFGXUoDcB_CYFPz-RfILZJXm6vMWRPKU9wRpSl2c0-XS83FUStVwDImkl2wXPUiUr5mKT9VT2XU1ktlm20SIcgHGZ28I5G1aRoHYm8037rqMd7FA6fjobEwSUiwHNJH6awzIRKP2kry2EgZhF-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f984c921ab.mp4?token=scaJshaWOLjJOlfkqbav8RGuEtJ7YC8yiKtlv6h7abwGWZwZKYsCodQ0kMnWOxP3j9zQJT3kSSqULvlr-JJjl3tQNQgHpToDz9KW92M_OFt0bWETkv6e2himWI-1qeEy4xnfLghPILzFhUgaDx3gnXpodGZ_Z_g7gDNPL6SrOepJpG9AmWwf3TZhknHKtcBuquwtFGXUoDcB_CYFPz-RfILZJXm6vMWRPKU9wRpSl2c0-XS83FUStVwDImkl2wXPUiUr5mKT9VT2XU1ktlm20SIcgHGZ28I5G1aRoHYm8037rqMd7FA6fjobEwSUiwHNJH6awzIRKP2kry2EgZhF-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت زن سالمند حامل پرچم فلسطین در تظاهرات برلین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/664907" target="_blank">📅 13:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664904">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDGOC1raNiRFzu3zHZ0YWTG49MZzfcQrSuhGJmBWNVHzDa383BdqrINeAxTPlinaDKh9lgcjnWEpwumBrPS0dDtj4YYtnLp5XvKbLk5RWiAmIFrY8IOz8bzHOp02txgaYybr0xqNni998S-lSZLLSn1_J_j844a-IOQhUiJY8jTb9zhmycVJEgin7QjXWOdlVvsH4o_sBjwFT_VJYztkZExnDNbcDVLJZMoDeF1HwXgc5AFz74zsX-fBYHfymR1I0qtr554rFHVEfgiEucga4p531jH__yeyosfBhsEN7M6TlyYgWvcHCgNyiFv2oSz0XKvsE8fr-ETaJvMbtusejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ حرکت کششی ساده برای رشد قد کودکان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/664904" target="_blank">📅 13:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664903">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8b1240f7.mp4?token=Tggjb0lhV-I_Kse0VRwBKb0rwQ89L4rWnRGyDzRIswQhHOJgko89akSNP6OsD2ZuoWSomLAP6AO_pHIjCn3IelQVHLob9Z7hX3F5OhMk4tYhNHyeHgmCL3N4tdtAo-sH9o_SFDY7miBUlaqTIRcpkFfIFFISrDQJTVBqjXIAvZuA5sN6_vloIm4yKEO4m0mpsc20vlGPneNGixOswF9E_x_t0HsTpQJeWmMQV-SssUMZ0oabU_fBDunQfpOHxdQnHvhLZxA2rxyIrNrowixQMcm5AN_qKso-5o-e_AsHW9SEvWGsy3GAEPEuUOj9BfrJcjb7zneSSuuFAMarhqraHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8b1240f7.mp4?token=Tggjb0lhV-I_Kse0VRwBKb0rwQ89L4rWnRGyDzRIswQhHOJgko89akSNP6OsD2ZuoWSomLAP6AO_pHIjCn3IelQVHLob9Z7hX3F5OhMk4tYhNHyeHgmCL3N4tdtAo-sH9o_SFDY7miBUlaqTIRcpkFfIFFISrDQJTVBqjXIAvZuA5sN6_vloIm4yKEO4m0mpsc20vlGPneNGixOswF9E_x_t0HsTpQJeWmMQV-SssUMZ0oabU_fBDunQfpOHxdQnHvhLZxA2rxyIrNrowixQMcm5AN_qKso-5o-e_AsHW9SEvWGsy3GAEPEuUOj9BfrJcjb7zneSSuuFAMarhqraHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسینی، سخنگوی اتحادیه صادر کنندگان نفت، گاز و پتروشیمی: مدارس و دانشگاه‌ها در سال تحصیلی جدید، فقط یکی دو روز باید حضوری باشند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/664903" target="_blank">📅 13:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664902">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a798239640.mp4?token=jkGQOOFjw23o5IKSMHyXKg-1I38n-Zx8Jhso3qIAdTw2yp8MP6jDdVnNAtSexOPUq9Gvbf01jMKJF4nddDRi50zhD7ykoNjR0ra_ZbhzUO_ERWfJlCZXQxmmgg_oWck-_mEsn538643FdCi55-DNr_mtFWA4IFgBYPBll3t5DUy3MGwIiHU1bYSXcFDe9BkihC6Ob_0CFNcui0byRNHslluOTx-imUYVZMzTZ7gfgziiERL_MrPYR512r5iZf06EN0qZwAgxbctkphg-zpfNKQupvKqY7Y3hTnvp-36oyjzip41ISFAMZcWcjo3Vjfsk_MO2DAV0-_zcv_SdVVuBag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a798239640.mp4?token=jkGQOOFjw23o5IKSMHyXKg-1I38n-Zx8Jhso3qIAdTw2yp8MP6jDdVnNAtSexOPUq9Gvbf01jMKJF4nddDRi50zhD7ykoNjR0ra_ZbhzUO_ERWfJlCZXQxmmgg_oWck-_mEsn538643FdCi55-DNr_mtFWA4IFgBYPBll3t5DUy3MGwIiHU1bYSXcFDe9BkihC6Ob_0CFNcui0byRNHslluOTx-imUYVZMzTZ7gfgziiERL_MrPYR512r5iZf06EN0qZwAgxbctkphg-zpfNKQupvKqY7Y3hTnvp-36oyjzip41ISFAMZcWcjo3Vjfsk_MO2DAV0-_zcv_SdVVuBag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پلیس راهور: ممکن است نیاز شود برای تخلیۀ جمعیت برخی آزادراه‌ها مثل تهران-قم یا بالعکس را یک‌طرفه کنیم
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/664902" target="_blank">📅 13:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kS7xv_47l9lkvsAHcx-hZzbewynaWzId71TQ88xJoXeFtjM07FayQKb9bVHlmGfAPSYJ2DnwrNO_Aw0Q7A5iTQ7bz5FA-9cb6aJwv21fL-UpynibNG7FpHz9lfZ_uS9Aext-ogL4a7Rs8b8ZElugna7O1mV8znNB2Y3eEfwa1VVGxccRJNDB2BT6Jjl3QH0Ce3S1tqYDyiRdSx556o_uzTXG5LGbcHIA19E5afXQA6_oQgk-FbD-3O1ZuFOpNFW5Zt69nTyYkHUzkDSDkzGdjt_o3J4vLYXehYOHZH-UngOyT36EPx17lelsLrNSC2O6dxa8wBsMrgYfWAkq6lJrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
▪️
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/664901" target="_blank">📅 12:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250d698f21.mp4?token=HlQFbdYmUJdsSGx3BdDNjcVldbYQW-B7MIzmSatvOAhyumK4XyWvHl2Zk-3cM4KtRniDxtXiV2aCH0WXD6ZC-tHVi94lpohJIm3v6kBCHAnqs72yOelRw5peR2hsNHPgdsNEiRp0DS01nCMzCTMJDYxOYVhFdAKi_VSAaFiBIFk1SL7mpQSt-1XRJsnbmZR3FfVfhVJMvCET5QQqditTRscmvZY99SYV1PsS578MvwXyc1fdy2h0HeQep3KH50HKLbm6645-aazx5qP_F0bMu95eeGSmpAbCVZWC9YHBKrbB6nPaSGKONqd1CFJd4mMhdQkAj7PUFN-D2o9ODLaQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250d698f21.mp4?token=HlQFbdYmUJdsSGx3BdDNjcVldbYQW-B7MIzmSatvOAhyumK4XyWvHl2Zk-3cM4KtRniDxtXiV2aCH0WXD6ZC-tHVi94lpohJIm3v6kBCHAnqs72yOelRw5peR2hsNHPgdsNEiRp0DS01nCMzCTMJDYxOYVhFdAKi_VSAaFiBIFk1SL7mpQSt-1XRJsnbmZR3FfVfhVJMvCET5QQqditTRscmvZY99SYV1PsS578MvwXyc1fdy2h0HeQep3KH50HKLbm6645-aazx5qP_F0bMu95eeGSmpAbCVZWC9YHBKrbB6nPaSGKONqd1CFJd4mMhdQkAj7PUFN-D2o9ODLaQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیزنکوت، رئیس پیشین ستاد ارتش اسرائیل: نتانیاهو در انتخابات شکست می‌خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/664900" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265ebc810.mp4?token=Rs0vlNGwkB00Bz-r43SC6mtRFT0EdGd9xXJghqJoECK4gWk47M_pTGYtS-tgf_n0Ic3bSoWy33F7_3J1g5uQWTtRthR_BzKa8yWv-HCI9zx_jBQn9JWPl9_vXXqYhbdOgI5jRb60fQZkTpHrb4ASk9fl-tnMfQlT56-FIOM5qKKgizD3VGuqFYeP35n0D_Pljgl9BWidVKyXM4MCwS_nQilHSGym0kuVH4yVow6rQciFm7-mK69wnnCQEGnP7RUtIdX-caySxo-JU-lxWQrbb4I3_nVZvlkMBEaeYKYDOFZLlf6RErbcU8FcGsT3HEQ7YLWXNtl9g581knMQ5bwqgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265ebc810.mp4?token=Rs0vlNGwkB00Bz-r43SC6mtRFT0EdGd9xXJghqJoECK4gWk47M_pTGYtS-tgf_n0Ic3bSoWy33F7_3J1g5uQWTtRthR_BzKa8yWv-HCI9zx_jBQn9JWPl9_vXXqYhbdOgI5jRb60fQZkTpHrb4ASk9fl-tnMfQlT56-FIOM5qKKgizD3VGuqFYeP35n0D_Pljgl9BWidVKyXM4MCwS_nQilHSGym0kuVH4yVow6rQciFm7-mK69wnnCQEGnP7RUtIdX-caySxo-JU-lxWQrbb4I3_nVZvlkMBEaeYKYDOFZLlf6RErbcU8FcGsT3HEQ7YLWXNtl9g581knMQ5bwqgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن صعود تیم ملی مراکش به دور بعدی رقابت‌های جام‌جهانی همراه با شعار فلسطین آزاد
🇵🇸
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/664899" target="_blank">📅 12:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqWveFj_JerTFU1I0lvemaElrHa51U7ZtKsp7CTLE84YAFi-fHazHh9PquO46e1eJNXnkgYPMIDI0pi2BekLpNlgQ-Vg5XZ_7P3rMoXSdqbwIwr6KOcX53BMhwWcqaoHckt4uxqdHMtw4IQu2hWkmxkcotwTuXmYRb-hD2iTCyBjzUJSHIYRz9cCb5Rqno4dQNjMsmz-Kini0x5rCBHb11XnqWugd3-r-FxVw2Pc7_NagHbhggzM8_tJQ-rWFR0N6a2q977fcXZ9Oc3u_6TH7gVxsz9NeECY1HwRGO5XUgsmEBkkyuLDv3q2GsYcPhbl3R6eXKGa9fBUS71GfubV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در پایان معاملات امروز با جهش ۶۸ هزار واحدی به ۵ میلیون و ۱۲۸ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/664898" target="_blank">📅 12:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75235e49d8.mp4?token=UJuY9CICTR1JE3lGFNKEdrbv4awLlBs-aFnGU5-vy5IViIcEBjk-Ko-8sbUXa0a_tHzCfppONjGHmrHAuz2Jixq9iLM53T63xgmZTdDvt8Wjukgp71dC8LwhLhOuI43-vCMPZxrM09ZyUSF56wdWFi4s-RxSGQNSeBlWicuGHlKtvavsaLEN0JR97WL8qIIsQLDosd4vcxe35JfzL8Pdr0Y8hugzUCv4AH3IxTjUs06zkWNFI2H7fSPDtdTRo7fOkR2NYOmFDsQKWsu2XEx2uwZbyV1nLbbyM_bQqS36pL5aWsnAZWdWp190Mv0KZvuJ_fe7DdiZKgAcGmTgytEUAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75235e49d8.mp4?token=UJuY9CICTR1JE3lGFNKEdrbv4awLlBs-aFnGU5-vy5IViIcEBjk-Ko-8sbUXa0a_tHzCfppONjGHmrHAuz2Jixq9iLM53T63xgmZTdDvt8Wjukgp71dC8LwhLhOuI43-vCMPZxrM09ZyUSF56wdWFi4s-RxSGQNSeBlWicuGHlKtvavsaLEN0JR97WL8qIIsQLDosd4vcxe35JfzL8Pdr0Y8hugzUCv4AH3IxTjUs06zkWNFI2H7fSPDtdTRo7fOkR2NYOmFDsQKWsu2XEx2uwZbyV1nLbbyM_bQqS36pL5aWsnAZWdWp190Mv0KZvuJ_fe7DdiZKgAcGmTgytEUAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات مادر و نوزاد پس از ۳۲ ساعت زیر آوار زلزله ونزوئلا
🔹
نیروهای امدادی ونزوئلا یک مادر و نوزادش را ۳۲ ساعت پس از گرفتار شدن زیر آوار زمین‌لرزه‌های اخیر، زنده بیرون کشیدند؛ عملیات جست‌وجو در مناطق آسیب‌دیده همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/664897" target="_blank">📅 12:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h27Z2rgRLtt-3tH_1s1FBEBF0tIVCt3TXyNHybVBlZHrLf4z6831plJsqlSABkiN-XwGB1sl32CvoeGK-L_S-a8T1ttDAsavm3iCsjc54sWWui_uGwL1hf4FXxPyFLnkYZC3DT5LLGJ_XcVMwxswxlkAOlMInVed5OdU3YIbjn__TS3dZVj0Mc64ypEPEpN24Hr3YFxFRCABjc_pV7nOT9uHZESYMQ18dK2j638BdGgKhuuli72yxlriYd8ku8gZWCQbcaDdWtnx5GSRxK0cJnzW4mn3onSAluXg_lUjPI9gHcQX5QZM6x90TgZLppNwaX3tMifqInhmqL26rinxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر امنیت داخلی آمریکا: پس از حذف ایران از جام جهانی رقصیدم
نشریه اتلتیک:
🔹
مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/664896" target="_blank">📅 12:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664892">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbWrFYIrnOPH1fVCrJYyRFfsiJbDs8XunOT0kIj4wYKYLUCWHvBeSFTOtHxJGvNbAhOHp_AzdDg8WN1Ur51_xxjNEX8riI2fSceWxKQP36vvZAClQlWzd78NIMCcniZX3mrv99_TaUqpQsrw7GRa0AbxV2vq7JqRSRHZu9ODwIuwNLtJajSkW1hjcOgs6-_9UWtOkdsBQEKUy5wRA9bw7u6KNkPCdBAjRAvdCEByyre3BRmgs2v8WNTIit9SH6z0_aB9u-Hk4DfYbqejwg-dgXQIp9UQXu6Ikg_oL74z-MGsUa0jv0f_Z4eA73dnQIFKstc4ilVf5Ojcla2UOQuoOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7dQgteooT-dW6_34bYCSYRAjK03w5mEZoNsHNp_U7G0c4RAl4ZkY9WLuxproAXQg1xEYnHYmTxDQmeqLoZzXj9K23IA3yPahuwnBOlEkRC0N8lMZFvRFPLo3Lj4bm4E2P-KMPe5T_8vOwPDaKBDIU3dlL9UHgcfviqGBdjfLvd1ua3svWaDZDfXLzI6jdGC5HbnkZDgkd867smau5e7mbtboja4OhEefq2SnxbGRy7SE3naj1Hs79Fd3v1vk6PQJICJXBFzkkYmRIehgI5hAka8V6xvezz8pJ3b6Ymxo4IYLbhgU3aZ7byYQia07dzA0aT8IFxZJ0VNI4uBsAO9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdxA5NVreAFqN_6Cbgv818xu8XrhGLAFVQVgg1shOPbrsnXlE6U8v3Ir51b_OHqtxmXYwBHeEnVvHCkCfGiqM5YhuL0GGREOx0CUiVfPhVsG7qfNnJJisxqsUCaS7pAb7JXlfp-gFVm8shBtQBNu82K-IAZ14tN1J71tPsLbONFoLBd_fAEfHYzQCaskDHknFN3UGVRVBMpoO87cN18nLkU0NHJ7tbY8vxxq6aW0w22KGaCutXq5W7OwFkUXIGX29yeBHflB-GpWARSRmxww7i5uWhHVJW2NUjn2ftYQpWzL29RMQ52KikHjKPI5XhvgKHi4YWL8lvUKIAvm7pgUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VudF7RjjcXjolpSADw-BLU1Maa5yQ1M4L1rWp-OKqBqB5uptD-RyeokGfs94u7FdBO5c5xw36zWVqr_JbFRFiRjv-JWOcVjabzu0GX9qWwDo8dGkMfsE1t5LoOHVWi0BsBeaCPG0qn95U52H0aAFCK7x9e0XmCnl_RtWgdigeQQhD6xEBPrMP2hqxiUCVnWZq0pZhQ9hMTQYky23v3j2__dylGUJTbNLHK3Wwbe4u3O1aRnNAaVADB_7OzNAkesGHf1mNcTLNAa_OCDeubZ1gN6F1hBxeM5FJJlvNtEQIJy0XZ5T4STFIkPRqtTdpNqbCQAA4WJtNxm9N3TyiOBrGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رازِ میزهای مجلسی؛ ۱۲ ترکیب جادویی سریع و خوشمزه با نان لواش
😋
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/664892" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664891">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTA60Ffh_J-EKxVzfd2dWk4T6I93aEgtxndqHhMf0_HOmyY1QQPiFw4PxWhQ8P0aO0cGRoT6P0CHU22q0PAIXF4iXwKn6D13zo0neEC63Y1Gh7Re4_9yZZHM05PklAbliX8_DwFiFC8lGuQO7dm2YykWlJSJtGzmAI0Q1WAiw-j7jJGueWQJfP1ts2ELV0GolNYPQCGqXF8ENVBo6D5gixPP8ehUP8OfYB_8nOXBBpbDZG20JcBZ-GRXDSlQpuqeXLVWLhtBd1THrQysHudrDZeqgGm7Mz-w-DScati_n5DQgAWKIlcVX61m_CM3UFIcPzQXiyugCr3L79J0tzAYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تداوم حمایت بانک تجارت از خانواده‌های ایران
🙏
💍
پرداخت 4.8 همت در  قالب19 هزار و 345 فقره تسهیلات ازدواج و فرزندآوری توسط بانک تجارت در بهار 1405
🔗
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/664891" target="_blank">📅 12:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664890">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9381c0dfa0.mp4?token=fy8pNwWNnrxop0xVUY5q2_CK7si2WA_8FgPmwSorVJjyJIm4E9_IIvLgVbuGY8m0dJHoQJ11zWpCymUmTTUKb8Xx5xUWRuF8CDa0Xu2NLYSyny1ctTzot3ZJNSmMhtnBz2CCdPCnOM6x2pyN_vtscjzNLLQit0bcNX0m1fyeAwy23HSK7asPgoDP1060uyyGiMYBopzZnDcZ3nUZl5ayr8N-M9B78Pcv8dbPt5b7_s1KARH6-SVCqJWSKtho6Ua2iBfdCizKHWyYN5vYwOOeDcktxjUYUovpYgLh_F3f0q_k9KK2qTZOCvuzG6CafCpxe5_xluRSIBytxTZFudxZnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9381c0dfa0.mp4?token=fy8pNwWNnrxop0xVUY5q2_CK7si2WA_8FgPmwSorVJjyJIm4E9_IIvLgVbuGY8m0dJHoQJ11zWpCymUmTTUKb8Xx5xUWRuF8CDa0Xu2NLYSyny1ctTzot3ZJNSmMhtnBz2CCdPCnOM6x2pyN_vtscjzNLLQit0bcNX0m1fyeAwy23HSK7asPgoDP1060uyyGiMYBopzZnDcZ3nUZl5ayr8N-M9B78Pcv8dbPt5b7_s1KARH6-SVCqJWSKtho6Ua2iBfdCizKHWyYN5vYwOOeDcktxjUYUovpYgLh_F3f0q_k9KK2qTZOCvuzG6CafCpxe5_xluRSIBytxTZFudxZnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
مارکو روبیو، وزیر خارجه آمریکا، در اظهاراتی افشاشده توسط یکی از نمایندگان کنگره:
🔹
تفاهم‌نامه جدید با ایران را فاقد محتوای اجرایی است و این سند تنها توافقی بر سر «ادامه صحبت درباره صحبت کردن» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/664890" target="_blank">📅 12:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664889">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
امین زندگانی، بازیگر: جلوی لوکیشن، ۳ بار موشک خورد، اما به عوامل می‌‎گفتم کار در این شرایط ادای دین‏ ما است و نباید تعطیل کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664889" target="_blank">📅 12:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664888">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZnYTkTM6SWGR1FKieQ7R4Ysv7cvEOWUSsjjJWDqVbMR_gDMkWjE5r1KelBnKqcMMVxdTMIxWORMLOO7QTfXJK6zCnFAnDxVpozfm2nNYWjqcY-HkQzfen2TVfgE6wcuPl4-_BD-gLEAfA-uLUH6UPTg5BwJX7hjUphFr3SglmSj4L4wJlT6YSp2A1XHOAAtbBEsZ-offP7ujZy2xbvkPz8W6v4J34NR3PEsOKHiPAmUkKo-FOA_L8Q4h_qj37l-eFtcZyMStvIZDvOm-b2Y_dzmo0E-UYI-KUJ5iwDMQ3Ku8Cb-B6Sk6GdqiyGFwFLqadYIYx9maoVaE1n074YrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام تیم تروریستی در مرزهای شمال‌غرب
🔹
قرارگاه حمزه سیدالشهدا(ع) از انهدام یک تیم ۶ نفره از عناصر گروهک‌های معاند در ارتفاعات میان مهاباد و پیرانشهر خبر داد؛ در این عملیات چهار جسد به‌همراه سلاح و تجهیزات کشف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/664888" target="_blank">📅 12:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664887">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: چهاردهم تیرماه برنامه نماز بر پیکر مطهر رهبر شهید انقلاب اسلامی و خانواده گرانقدر ایشان در مصلای حضرت امام خمینی(ره) در شهر تهران برگزار خواهد شد
🔹
مراسم اقامه نماز بر پیکر رهبر شهید در قم ۱۶ تیر برگزار می‌شود/…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/664887" target="_blank">📅 12:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664885">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdpMP9YD9CxIJ2EkAZSLpkV3_YNvYotNn7VTIAnlk2PcKs_IAtdff7kWCyMuFYQ8-jURjEXk5rQvz4j1LOccPYjaN0osJ769Q_fyFaNtzoygJvBXP6EzUZcdRLRjpIUbGkz6IXRz7bt9eWSpmtLPqL7RhrLcGythZTBXmmD4HjMH-4mQF14ZaLIKe4hy3wqBfRipkcc6pQF5UzhikKNPAMdWnan67HhFLcf0rGmtfPv74ocglJCrCR6iMkhIfG0wnl7bhF56LR3ISa3aKYtgZ8Pt0cCt1t1zmyWXtOJjPkDRS_SRI8KshsHLQrYVcRyTK6vsH9cJ_QCQ7uFaVtEjcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برزیل؛ همچنان گلزن‌ترین تیم تاریخ جام جهانی
🔹
تیم ملی برزیل با ثبت ۹ گل در جام جهانی ۲۰۲۶، جایگاه خود را به‌عنوان گلزن‌ترین تیم تاریخ جام‌های جهانی حفظ کرده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/664885" target="_blank">📅 12:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664884">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9a84eb55.mp4?token=lkAPjfI-Imt8r9fKZpTnWbSiLa-8VG96nFyB9wb-QQwXkYhvrNTyCSjNK02wKvk76hoAApFfAdJEI5TIsCrGRy9X4ma1lkGDhG6rs96XhgNXtmM4VSfJEHAIzesmeoOkpa5iCqZccA15tm2owvrk2nMFnlF5vnnjLoJjWuiwfqnYRaH_L-bIcUarhozBseUH-dMF0B07jo68rwwT6109wIU6QpkWDjoJ1vZX_deocSmCxeyWjwqDx7ap9GqX8ORj7WRTsaSWzRy4I-kB5TtRQ9qPPykfH3a236NZb3yGs-tPGWkqNCaTj1wNkD__mT7NrP55RT6_mK7QGnfX_yokHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9a84eb55.mp4?token=lkAPjfI-Imt8r9fKZpTnWbSiLa-8VG96nFyB9wb-QQwXkYhvrNTyCSjNK02wKvk76hoAApFfAdJEI5TIsCrGRy9X4ma1lkGDhG6rs96XhgNXtmM4VSfJEHAIzesmeoOkpa5iCqZccA15tm2owvrk2nMFnlF5vnnjLoJjWuiwfqnYRaH_L-bIcUarhozBseUH-dMF0B07jo68rwwT6109wIU6QpkWDjoJ1vZX_deocSmCxeyWjwqDx7ap9GqX8ORj7WRTsaSWzRy4I-kB5TtRQ9qPPykfH3a236NZb3yGs-tPGWkqNCaTj1wNkD__mT7NrP55RT6_mK7QGnfX_yokHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: برنامه تشییع در استان‌های تهران، قم، خراسان رضوی و کشور عراق اجرا می‌شود #بدرقه‌‌_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/664884" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664879">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P6XyIQgSSNdFIfXIeGkNpbXNqAb0Pp1nKUh6FMF8SpIscPtyY_1tiSKmyJy5spW_0A4Z47pMzsfk4KeikD_ZpQjIzPkxKhkHGsCYusGlhksGcq8VUSji4Sb_o-yjwaPbJecEMHj1SljEEtmju0-hPJvomnz4vZ9FoJWjIqZy5O2spvW4grz_UbAQacUQtKguyAqga3kvc_5xFUD8URE6vTqJdQQiArCbjFY_Qql5gom50IxAXukHlbWS5M3KEaFC7pSxI4NyhfB8Hg1JR8K7w7dO8sAWKTkSoXTQjjlqSLVt1vlZ1c-XnS3Spoept2hWZrsihdET5mlvhAem6KcZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ct1oiBIjGSsKo8pk1KBYEJqT8FsS1WR_hZ_IDyEJ0M16PYFrEu2zflw2fFxVfS8IijENHL_OlRVWXltzuat0g9OBeE0LQFXAM0XQOpVceY0w-OLVdLl_im2oWiUghNlxM2_umAXjp3jUlCDt7RFFOfTNDtEZ8vjFnbVCTWM6xxS3kql9k7jkekNws5TsVn3m15vODdZbkm677y5RBTS_EiiWCOJLPgiKyvqUHWdhZcdIWJXxBvmd_OQQwKCrM6WmNv0OTDDJRLxbkTRLP1jPmbOUhfpWBL6ST3qHnTtzv8RtepWqjHjylXH_qtsXY_LYPOv5HObGJ0oMPZsk2VZpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZ0am5xArNQhn3VbNFeVKU-UGbj24atO5EoOHoT4QmNr6-yn3yysasDN8wp1q381KWo0GUKP0_lfcQkFiQ9si4mT15fAgomWv4cMBCwFsAaNfTlDnHUil3ajesgSXhL5T8aahhOD3Cu_vgqRYuA7sbr1dqeJ3yFBHQAlldmVYCGUB62iu_At0I9eHaaJ7X5wz1mwbu9Z7jaibf36RLjFGITk4fsilQzHDSJ7Y_ooGGWM3v0yZPsiq2QXwvWtRfHD1ZKc5Cp49p2yj8cbAdHkGKm1-SD-K8rSa9u2k9kGQvf0SCNqquqno4ShkkAS6hHtj6VGIMcH8EOc19i5T64nzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crh7nvyWh21kX2BOu-6M_Eux3nnFJFu9cu-kJTKm-m9Wp2ur3sSt0VHwD3HB7r35dXMtK7S77nXNz4oauOXzXX4yOEmaZ4J55twJaEY5vPIGt3lGohi5hQ4tl2H90mPhpHrWzRouwDkW6gh1d8AEAIjhhUkON7nQ-YYQglKI5PHK4mtFKB8wPqVl3Q5tW-liVE2LWxtJ1jb8Qm4IbIDIre4f6LxYGKKsu7H50Dl71gm45aMfT_wjnh6HoihgiCR4A5HmFhUH4Z9-iAI24wjvwa-jQ0tErMtuJlc1Gt7cv2_xnImba70n3SlbLZcYXj7MW5-B_69DVVGt_rQXG07Opw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4804f04f.mp4?token=QQ495zn9PXEEp6qVIu-d9Te8ZNIoy_OWGkp0k6QV1uLiyaro2wy2gjW9FCrZqmzhOmc3A7wy7_ismpMzTRw7WXrQ3JY57lGFm3GW6TAbasN0x0790vcAmahDgpUVBRyuGOYXFrv5YRngzbwDOwhht_sHxjxyu55yO2vpqJaw2yGeahzmRSJSpUlON1OJ4QyeJx69W-4_0enMGi_XI_RIyDjKdTZ1mGIxCykRecatF51duxL7cFdFJg2w9Fkb76n0HUDqfVE-yAJLMi1auAuA28e8C5O7c0Z0g6g8FSx17__mzRYNrn5c0YqavQgKhlJz0jgxbd2AB8VsK10zJaNdpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4804f04f.mp4?token=QQ495zn9PXEEp6qVIu-d9Te8ZNIoy_OWGkp0k6QV1uLiyaro2wy2gjW9FCrZqmzhOmc3A7wy7_ismpMzTRw7WXrQ3JY57lGFm3GW6TAbasN0x0790vcAmahDgpUVBRyuGOYXFrv5YRngzbwDOwhht_sHxjxyu55yO2vpqJaw2yGeahzmRSJSpUlON1OJ4QyeJx69W-4_0enMGi_XI_RIyDjKdTZ1mGIxCykRecatF51duxL7cFdFJg2w9Fkb76n0HUDqfVE-yAJLMi1auAuA28e8C5O7c0Z0g6g8FSx17__mzRYNrn5c0YqavQgKhlJz0jgxbd2AB8VsK10zJaNdpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شورش در زندان کارولینای شمالی
🔹
شورش حدود ۸۰ زندانی در بازداشتگاه «برتی-مارتین» کارولینای شمالی که منجر به گروگان‌گیری دو نگهبان شده بود، با ورود نیروهای امنیتی و اف‌بی‌آی و انجام مذاکره، ساعاتی بعد با آزادی گروگان‌ها و برقراری دوباره امنیت پایان یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/664879" target="_blank">📅 11:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664878">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
اولین شگفتی جام در دور حذفی/ پاراگوئه، آلمانی‌ها را به خانه فرستاد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/664878" target="_blank">📅 11:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664877">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1531e58b.mp4?token=pyxOGeV1_J-hLz-a5YBVy5fon-q2x4dQ7wDfSDOzMtQltjfEGxL9nxA60RtjNz3qn52Jk7DAAcuqTeeaCYM7to4lQouEKjb_ZPxDoRZP3rTVP1SLfLJg-P9rdmkXEiZmHsyrr6yqSY5ytBYWDMFQFafECWarpUXMtc8V53y3XsZROmEiP6AFeYh7u_JYENDnXjC3DS6CZHSPbukDqX3UMlGA0d7Pa4ba845_Ky8CHV8yoPgnJEtkUG5SiOJcmaI3VrB57r53xu6zhKfyN5MchgRAWAjhsyXEYKPfzecS07O8dx5B6lgf5VQhAN6x8G7ci3rdX9Oah0vLqwMtoaD9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1531e58b.mp4?token=pyxOGeV1_J-hLz-a5YBVy5fon-q2x4dQ7wDfSDOzMtQltjfEGxL9nxA60RtjNz3qn52Jk7DAAcuqTeeaCYM7to4lQouEKjb_ZPxDoRZP3rTVP1SLfLJg-P9rdmkXEiZmHsyrr6yqSY5ytBYWDMFQFafECWarpUXMtc8V53y3XsZROmEiP6AFeYh7u_JYENDnXjC3DS6CZHSPbukDqX3UMlGA0d7Pa4ba845_Ky8CHV8yoPgnJEtkUG5SiOJcmaI3VrB57r53xu6zhKfyN5MchgRAWAjhsyXEYKPfzecS07O8dx5B6lgf5VQhAN6x8G7ci3rdX9Oah0vLqwMtoaD9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو پربازدید از تست ترشی توسط پیرزن خراسانی
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664877" target="_blank">📅 11:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664876">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPX2bK-y3Ykv-uc9MdjP-zbBamBAI_3JB4hieoBrBoDx0bXBCuwvEbyCH2GfVO2ti24kdNJsHnoSNEQiUSiTQkH7GI1uOZ6HNLGvjU1RWzDwXKvpVAjj_9XuJ3PI1aqn7EQmIrl0DO6g2iylywuYgxqhb-Siy9FplhQzS_fXS4Qe-Ja655P-D_Vh0ejoXheT7yQif1HdC6ikBk4NViCMQRI9Xb3642P_UY2BL8MMcKwfTaQZn46Q6hww8ALB3emzOGlfbXplz1r27bEMyF5TrpOZA4mx-VnY8wb6iyv1cEWhktO2DJO-O0xL1ppzgtNE8J0TOCjJr-MQaKxXL7wKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی برق می‌رود، دخل مغازه هم خاموش می‌شود
🔹
قطعی برق فقط خاموش شدن چراغ‌ها نیست؛ برای بسیاری از مغازه‌های کوچک، یعنی توقف فروش، اختلال در کار و خسارت روزانه #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/664876" target="_blank">📅 11:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664873">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DedkrrO7hhqBLju9up9270X_yXGkiNI2nSd4MqJF6ioNJ_nNvU2hZybezWpUDqXfgQJsSXOhYwzM9wj5R8Q3P2KJXMJV6DzhIMIIy4ZBsYEzorDB0OZCJadRCS6NvFOpUpuPVS7kD496V-WUWUE9udHTmcvoCFcRWqGwdwGmY2ChnXGlN2WD98FwF49TuGTHBYiZcwo1umTVT3JeY_1r3vGo8uo9oUYJsQfjyRG9R9kDSsbozOjTlQDfGLWzVX06tyE4IlaoX_WN05sb_hKXZSebjxmBpYDCly8qWqs7IncYv1GqWowdOBbOqU336Ml2sRvFVYvPTXhsUlVWuFDUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهی یک بدرقه تاریخی؛ تجربه‌ای شبیه پیاده‌روی اربعین...
🇮🇷
🔹
اگر قصد شرکت در مراسم تشییع رهبر شهید را دارید، پیاده‌روی طولانی، گرمای هوا و ازدحام جمعیت را در نظر بگیرید و با آمادگی کامل راهی این مراسم شوید.
🕊
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/664873" target="_blank">📅 11:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664871">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_qIJhtL1niLoejC7M3xwnNZpecWmBFkgYZy5v4qI_xqHwQo4DfRxQFNS1d054kVpnYeGKVq6xC-fko7lTo9atAK602rPf1YPeKa0IR4QAEXhEX-ggzoH54-rTw0OIUjwQ_BTIrnotMVZ7IpZxzOJGRA_Mmx3P8gV9MJuwVSkw1IBEc4uTR7YVdokq-wdC9aSgS018CPPnQyMVX34wvkhIHPgR9jVrZJDTegxQrd_1n50_OqgFZ9nX-E-ERv8BPe8yZUT2ZfwZSc09SqcpEhwehrMM16lFR9Z73gekqdxkNrkOiCH8eRMuljsR9ZTHeK-w2UEI0YyKBGu9XJRBpezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرزاد جمشیدی درگذشت
🔹
او صبح امروز بر اثر سکته قلبی درگذشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/664871" target="_blank">📅 11:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664870">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c592c0d3d4.mp4?token=n-Kh6hXsU6zGmNW8IHxsLSS9mo8UK2g3G_g5vlqSvQYw6N6WD-haDDTarILFHFYkyYiiBFs9eiPCl9GyWFmbUjNVgWHkXJAZzPKc8Zl9wJJXSSRw58Li4x4gr3fuvPgQ-yDm7ImnONUnYj86fNfXZCZhxiy3tBVf7Iv7d6y3p9bXoL3RDNl_GHh_5rOtPJs2RNE93E8p4iQO0lfVE8xlODUypPqW0pAX_sl0slTV9QApLQLD-mrvTORfcDb7Jin5C31pUD1HKahXuMS1auziy-gA6LoWNF2s3FezU6SeC5rl8arSBz2yS-QjTLv2sIXa6JnJuNh69fGQtXTn52whxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c592c0d3d4.mp4?token=n-Kh6hXsU6zGmNW8IHxsLSS9mo8UK2g3G_g5vlqSvQYw6N6WD-haDDTarILFHFYkyYiiBFs9eiPCl9GyWFmbUjNVgWHkXJAZzPKc8Zl9wJJXSSRw58Li4x4gr3fuvPgQ-yDm7ImnONUnYj86fNfXZCZhxiy3tBVf7Iv7d6y3p9bXoL3RDNl_GHh_5rOtPJs2RNE93E8p4iQO0lfVE8xlODUypPqW0pAX_sl0slTV9QApLQLD-mrvTORfcDb7Jin5C31pUD1HKahXuMS1auziy-gA6LoWNF2s3FezU6SeC5rl8arSBz2yS-QjTLv2sIXa6JnJuNh69fGQtXTn52whxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درب کارخانه‌های خودروسازی را ببندیم و کارمندانش را در هتل پنج ستاره اسکان دهیم، خرجش از این مبلغ زیان سالانه کشتارجاده‌ای، آلودگی محیط زیست کمتر می‌شود؛ مردم هم راضی‌ترند
/ مدار
گفتگوی کامل را در آپارات ببینید
👇
https://www.aparat.com/v/jmrz2dg
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/664870" target="_blank">📅 11:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664869">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vbg315yeLkVrBy8nmQqoGCcXF8bDLjs-erWiAhb1nu27myvR9Usl7Paj9YYIz5W831t1KiZjAmPSa-tci0VKgoyyHtXl81F_mtC-f7RFgAA_The7Do8TGdAiKS7qf_AoctArNEfg3xf1P84kgGexGt8bBIKtc6SzI0sPUkcWp4r0JuZm50UmoOpVEnBEf9XaA5pnp6eFb3hTzIiKIlpe5czddf7ROC-khTNi14a8Pol1eQtwRN6zfZKnQBIAmzSDMXSlDU5cJJvRepQNafpJngfESomEz3RAeGPCth7a08oLlRmRAElWq28DwHoknYBaROyXINupjbRhiKBCEPFvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه مترو و بی ار تی برای روزهای وداع با رهبر شهید انقلاب
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/664869" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664868">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1be5d8473.mp4?token=uGG6xWxnAnwUYPCxbyZaK1PRxfYS774WMcoqODaoC3lRAOkQYXe0b-sXMB_NXkfNKTw8QiZTNLhPPprGIUxtcVrNNLBPunIgU7tlmPMeNUVQBNFWTvR198pKzlCkjErs0-FVBxdJPXNSd-sIAqchSkkT8kqrWB-tRYq42FC6vxOYVmXAL9hmsxIkTb3pMz3SqjmoHd8DcXPuqzNGFvc2Z0suRiIgO6Y0AgxFgbffBYPqyVQRaKcUV8g0WICB3dPuiHtOi5PiCr3dPy-s9HRFbd1wMSqMwc52pFIpaIrN7y087MuHwWaDiajiJ3bN6zhBk3xER88YSeAXH0aR7yRs4D6jScEur7dggcn3rOxthf08ZPFuWWD0W2DIIoeA4KjsRLSpHbsfLoYJy7ivLafbqJNaxF-47thwXU4p92oRK69lMEyRsq36nk0WRfGLWeKIu3F1Er3ZfNAWt1Wrsy9JOT5ZWJ7G7jvDw6jrncA0QsBAvXxT3qfUkHPDBo8xELO3dS0QJexEYLzovVikUP4xBnKGO5Yr5tFe-MwgaopmHrbQVmNRteaC_nQojINOOB8rFfvyKjnDgxMMrE3ET7DylE1QF-hNDbAv5K48SBElCU847uHUtZMSxzceWGgafcohbdCvVmJkZgtao1NDmxtm7B2763to5NMWfgEqPHRf7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1be5d8473.mp4?token=uGG6xWxnAnwUYPCxbyZaK1PRxfYS774WMcoqODaoC3lRAOkQYXe0b-sXMB_NXkfNKTw8QiZTNLhPPprGIUxtcVrNNLBPunIgU7tlmPMeNUVQBNFWTvR198pKzlCkjErs0-FVBxdJPXNSd-sIAqchSkkT8kqrWB-tRYq42FC6vxOYVmXAL9hmsxIkTb3pMz3SqjmoHd8DcXPuqzNGFvc2Z0suRiIgO6Y0AgxFgbffBYPqyVQRaKcUV8g0WICB3dPuiHtOi5PiCr3dPy-s9HRFbd1wMSqMwc52pFIpaIrN7y087MuHwWaDiajiJ3bN6zhBk3xER88YSeAXH0aR7yRs4D6jScEur7dggcn3rOxthf08ZPFuWWD0W2DIIoeA4KjsRLSpHbsfLoYJy7ivLafbqJNaxF-47thwXU4p92oRK69lMEyRsq36nk0WRfGLWeKIu3F1Er3ZfNAWt1Wrsy9JOT5ZWJ7G7jvDw6jrncA0QsBAvXxT3qfUkHPDBo8xELO3dS0QJexEYLzovVikUP4xBnKGO5Yr5tFe-MwgaopmHrbQVmNRteaC_nQojINOOB8rFfvyKjnDgxMMrE3ET7DylE1QF-hNDbAv5K48SBElCU847uHUtZMSxzceWGgafcohbdCvVmJkZgtao1NDmxtm7B2763to5NMWfgEqPHRf7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: برنامه تشییع در استان‌های تهران، قم، خراسان رضوی و کشور عراق اجرا می‌شود
#بدرقه‌‌_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/664868" target="_blank">📅 11:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664867">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
نفس سامورایی‌ها در لحظات آخر برید/ شاگردان کارلتو به سختی به یک‌هشتم رسیدند
🇯🇵
1️⃣
🏆
2️⃣
🇧🇷
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664867" target="_blank">📅 11:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664866">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9454900b44.mp4?token=euApx-CN_KWmtjo4qoZVYOS9fGPHCAQ5_Cm_I1gj_SkOWJVPalYG005Xi0y08YPfOUqb7XKj1f78xYYRD5H4Zg1ygycw0JhWs5G0qMfom6IEMXLvO1tf1IzYXKVxBgaYfwMKLIf_DmsCcuc09R6pnuDeBSSTSI13zaQr7nyt3nt0wc_XkaKJuA_wvDAe0VUu_uOdpH-Tb4UamkqEOCpZCvY4GxQIFjnk8VTVhXUSeoG1gZsIujh5MvDY3-Efqap6cbWirO7BsE2SMTJk9tpObNWefX5hW81WXTJWCxv80apO6BmRskKBSYbsUC1HJbQqG1RJezaqkAfsc7zGWhp-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9454900b44.mp4?token=euApx-CN_KWmtjo4qoZVYOS9fGPHCAQ5_Cm_I1gj_SkOWJVPalYG005Xi0y08YPfOUqb7XKj1f78xYYRD5H4Zg1ygycw0JhWs5G0qMfom6IEMXLvO1tf1IzYXKVxBgaYfwMKLIf_DmsCcuc09R6pnuDeBSSTSI13zaQr7nyt3nt0wc_XkaKJuA_wvDAe0VUu_uOdpH-Tb4UamkqEOCpZCvY4GxQIFjnk8VTVhXUSeoG1gZsIujh5MvDY3-Efqap6cbWirO7BsE2SMTJk9tpObNWefX5hW81WXTJWCxv80apO6BmRskKBSYbsUC1HJbQqG1RJezaqkAfsc7zGWhp-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروفسور گرگ سایمونز، استاد
دانشگاه و پژوهشگر سوئدی: آمریکا یک امپراتوری در حال زوال است و توان شکست دادن ایران را ندارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/664866" target="_blank">📅 11:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664865">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/664865" target="_blank">📅 11:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDsZkiybF5I7UfkvHub0zCg9YCXIv_BCFHxyVuP-GNT2Wwd9tJ2tNNpk4XDW43UF85z4sw7t24C85Kq-myZRYEGsfI_ohyfcpo8pi2_oniZfKe-y3ZnzQNX3RS0c-qwrYfLKY4HWTDzsvfk0Inr8xB5EjduIlnzOoXKkLZEVQViKsxmpEwbRYriiXmg45TJHu4fq4LyyyvIDk7NAQD-kSHpkxu3JRGPLZPZyQ1VmuO7I2UzyzfVwvAvGhTrpj9G_PfGLdKUsmd4c4o-CimiZe0BkvQxdjtWahNgOmx1BclZicJGQyy1esITNboyfBL2cbx5GIY2jIQNbsbHJ4IRDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعویض به‌موقع قطعات خودرو را جدی بگیرید
🔹
تعویض به‌موقع قطعات مصرفی، علاوه بر افزایش عمر خودرو و کاهش هزینه‌های تعمیرات، ایمنی رانندگی شما را نیز تضمین می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/664864" target="_blank">📅 11:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de30243299.mp4?token=AqTP4Q45ZyA_WOQl-ghohgMLpjQHIgeX5nWlr9O2cBQ1Gxrzkq4jHKeEOE1yAWxOzKwDzuT9U-UbSLi8IU7ozTbSD4zbZAncALYqIG9CVe2C4aYHuQJjh32zSJuON0EjLNi85Ym2m-nk5tLYe88volDXRD5NmB_vAzGgkmhT7p5O1EFkqoOnfJDIPOueUQrGWVLZLjreDbH0FwkK5KEv_3furKO40NjMlmdMkV3brm0oiepOqi99D36T8RLbWyeCMAmm32NcWwpKtV0NFDM8dPOtlrofFXF2OXNY9L359BoFFtynitztwBSRqOAt_FXJYAC1nyN2g7hwIklp8tzD94WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de30243299.mp4?token=AqTP4Q45ZyA_WOQl-ghohgMLpjQHIgeX5nWlr9O2cBQ1Gxrzkq4jHKeEOE1yAWxOzKwDzuT9U-UbSLi8IU7ozTbSD4zbZAncALYqIG9CVe2C4aYHuQJjh32zSJuON0EjLNi85Ym2m-nk5tLYe88volDXRD5NmB_vAzGgkmhT7p5O1EFkqoOnfJDIPOueUQrGWVLZLjreDbH0FwkK5KEv_3furKO40NjMlmdMkV3brm0oiepOqi99D36T8RLbWyeCMAmm32NcWwpKtV0NFDM8dPOtlrofFXF2OXNY9L359BoFFtynitztwBSRqOAt_FXJYAC1nyN2g7hwIklp8tzD94WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: باید نگاهمان را در بعضی بخش‌های حکمرانی تغییر بدهیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/664863" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e8403a8a.mp4?token=YtCP2oBRaFPKCwv4-SQS0Nps8w7jQ2u8GBpUh1JPYRvOlzSVNM8q1zOTNCW9vFqPZdjsr8N7_fu1GKk_wcBJr-RNoJrVY5cAAvsIrWnZ_X5trPKDgRlYF0ROIHfHyIUs9NNR9Czd1i2HM5JJ3b8lMeIwZ7P8HCHAcmVkOSgRnSM_OFVYz_PglE-KW2Urf7VtEKfan9EczmV1LZtj3LWAiAjA4V4YaHGfgFDaqyu3f9POpCw5TRSsXdjBpXhUOBn5UggyTUb2jDEMhcP6F9jnUvJC3oxiRlyGa9quogw6O21RcH66UdNIZYQ8Am8vi6UrZPxniQ8crmVo2i2rwW7B4Ui6tDUmbEY3sS9mb8i_ql1GbMpgknwPhYUJ7TF0ml_NT6kTGElHApOerXdnlAwtkzx3iJDKI6u29uB4HfmJq9FoU5er8wGYdQbiTcmHfubj8kQmAEF8glCJssZsMdoU7LYyoAl8JksEL31MEztHXTpSZyii-2e9dLcNL1J1RtAmYwAfw9DqSWOdU4N-rKFLpw0Ms86jEg9sRtVszGuN9BC9GXmsfCsJqyEyY8498VM3DwT4xfKpbWza_9xbafmpCeOFMepvL1DcisJAuS_X8PtFtaIDKgDdohkhQJOPE2cBFT5cZryndAHNyiuM0TSkSizyRvssDJyI3xBN3ARLj1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e8403a8a.mp4?token=YtCP2oBRaFPKCwv4-SQS0Nps8w7jQ2u8GBpUh1JPYRvOlzSVNM8q1zOTNCW9vFqPZdjsr8N7_fu1GKk_wcBJr-RNoJrVY5cAAvsIrWnZ_X5trPKDgRlYF0ROIHfHyIUs9NNR9Czd1i2HM5JJ3b8lMeIwZ7P8HCHAcmVkOSgRnSM_OFVYz_PglE-KW2Urf7VtEKfan9EczmV1LZtj3LWAiAjA4V4YaHGfgFDaqyu3f9POpCw5TRSsXdjBpXhUOBn5UggyTUb2jDEMhcP6F9jnUvJC3oxiRlyGa9quogw6O21RcH66UdNIZYQ8Am8vi6UrZPxniQ8crmVo2i2rwW7B4Ui6tDUmbEY3sS9mb8i_ql1GbMpgknwPhYUJ7TF0ml_NT6kTGElHApOerXdnlAwtkzx3iJDKI6u29uB4HfmJq9FoU5er8wGYdQbiTcmHfubj8kQmAEF8glCJssZsMdoU7LYyoAl8JksEL31MEztHXTpSZyii-2e9dLcNL1J1RtAmYwAfw9DqSWOdU4N-rKFLpw0Ms86jEg9sRtVszGuN9BC9GXmsfCsJqyEyY8498VM3DwT4xfKpbWza_9xbafmpCeOFMepvL1DcisJAuS_X8PtFtaIDKgDdohkhQJOPE2cBFT5cZryndAHNyiuM0TSkSizyRvssDJyI3xBN3ARLj1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: باید نگاهمان را در بعضی بخش‌های حکمرانی تغییر بدهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/664862" target="_blank">📅 11:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ارجاع پروندۀ تخلف یک بانک دولتی به دیوان محاسبات
🔹
در بررسی عملکرد شرکت‌های زیرمجموعۀ یکی از بانک‌های دولتی ناتراز، مواردی از عدم رعایت صرفه و صلاح دولت در اجرای تکالیف قانونی مرتبط با مولدسازی دارایی‌های مازاد شناسایی و پرونده جهت رسیدگی به  دادسرای دیوان محاسبات کشور ارجاع شد.
🔹
بررسی‌ها نشان می‌دهد در فرآیند انتخاب کارشناس، قیمت‌گذاری و تصمیمات اتخاذ‌شده برای تهاتر دارایی‌ها، اشکالات موثری وجود داشته و در یک مورد بالغ بر ۱۰۰۰ میلیارد تومان انحراف در قیمت احصا شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/664861" target="_blank">📅 10:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzasCjLt4gSC7zlRK5IMEhrDpnDRnj4yIdaRX-b2sdev-nE5dptkTYJcGy1Q0pAv3I7QAYgmAoN1dm5CeR7FXTOJ28vOAdqn1kiB1wZ6tGe0P9PhKFO9sSK3q_07_effEc6PHcFHlOdsrV_VQj3iZeesbTl27TCx_el2pTTbzCDmDz5E_YDcrBuHSEpJOsRKptbRCB6eanfX37mBNyaaGLe7eQrvllLyOAeb8qtdDBhFpDyH_RX25UhOIUVcAyAhvUDbdEFtpuWGIFyO9rvw9btlby8C-NY4q2toJs8sgKE20EeraVBf-dR3HfBHzAw791EVsqWAd_tH6I3b1vJN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این روزها که جنگ خبری و رسانه‌ای اوج گرفته، این ۳ کار را تمرین کنید تا فریب نخورید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/664860" target="_blank">📅 10:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664859">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316b8b1ceb.mp4?token=OIqLoL8tz69HhkHUkoOO_f5R2q73FkPBK2xPFx5lYnKCFcji8iefhLiQCFCaoE7O9LDpBd_Ezl9-chALFnzKTniYYjjebG2RCC8TSPFEG7hr4ccbKmC-h8ZfcaohZp91eCGR4-wxyHhQw2VECA6-SMi0go3kt5YUI7w2LZGaOSXsNZKhJx2POmoJHKWWD1jrjbzHtmjvdABDwxou53C8EgqYIgqVGvq3ztM6Xk7vX5u3AaCjp_fRSjTGxB8w5fNDC6xkGFc6lvsEF42Mz_iFTUAxgFv7qYUuK7iSPCrxrfTlc8bboWOsfdZfPyGvVfIMkMdPelFFwlCcU_Dp6gy4LmD3ZnPJ9Jw5UhBdgRaEl6RKo9pP40JD1qF9lHWCVzKKoX1RqbgJrJFe6Hft2pKHK1OG7Q_Z18hWLKYfvTzXMAC7fnI4BQzFoZhN9XpO2iB2kBvpTfid50QZA4SggCgfIwc65OLT-wcC_bI0c83J4fckvr6tXX1pc67mmVYGpSMC0tkdwdTiY7g851xqTCZBStIS6SbymAZILZGGNgCHUoCkKHSpQAYVXVOi5vgESV5RXD1Mau-lxhFM4-OJBWqS8ev1jFJO1edl_m0GkiGwVmjVEv4pZrWNC8KrZ4R3QwhisNFdWsH8iuHDEtS3rBImXTJ8m99jQ_hBl4dHiobuVdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316b8b1ceb.mp4?token=OIqLoL8tz69HhkHUkoOO_f5R2q73FkPBK2xPFx5lYnKCFcji8iefhLiQCFCaoE7O9LDpBd_Ezl9-chALFnzKTniYYjjebG2RCC8TSPFEG7hr4ccbKmC-h8ZfcaohZp91eCGR4-wxyHhQw2VECA6-SMi0go3kt5YUI7w2LZGaOSXsNZKhJx2POmoJHKWWD1jrjbzHtmjvdABDwxou53C8EgqYIgqVGvq3ztM6Xk7vX5u3AaCjp_fRSjTGxB8w5fNDC6xkGFc6lvsEF42Mz_iFTUAxgFv7qYUuK7iSPCrxrfTlc8bboWOsfdZfPyGvVfIMkMdPelFFwlCcU_Dp6gy4LmD3ZnPJ9Jw5UhBdgRaEl6RKo9pP40JD1qF9lHWCVzKKoX1RqbgJrJFe6Hft2pKHK1OG7Q_Z18hWLKYfvTzXMAC7fnI4BQzFoZhN9XpO2iB2kBvpTfid50QZA4SggCgfIwc65OLT-wcC_bI0c83J4fckvr6tXX1pc67mmVYGpSMC0tkdwdTiY7g851xqTCZBStIS6SbymAZILZGGNgCHUoCkKHSpQAYVXVOi5vgESV5RXD1Mau-lxhFM4-OJBWqS8ev1jFJO1edl_m0GkiGwVmjVEv4pZrWNC8KrZ4R3QwhisNFdWsH8iuHDEtS3rBImXTJ8m99jQ_hBl4dHiobuVdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش بخشی از وصیت‌نامه منتشر نشده رهبر انقلاب در سال ۴۲ برای اولین بار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/664859" target="_blank">📅 10:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srsOs3Y8W3tq0BkENjKVcnwCVmsCtrASPyEuYnQ5WgGoUhFMvEydL4I9jwYcFwCLq_saxwNXpHMVG61byIFY4h8VcrWvnJQUYRyiWYeNluUniYhPL3sO3emAjOAqhKnFIOtiHypUxhGbkeI7nijIonVMYLVtqanPCcJR9X_zssKlmcfZXgwshy6PlNotmmn-nYslSOsGhYBVEi-lF5V21NaDtR7ZtkDDFfNhbogjl0Iv-5-Cpvb97tGDNXOFNUJ3CzbXdVvIJ01SG9Sv5iQE1vS95JxOaA4GybuUzZnbUDo5rQkNG8G-BA2BdSg94AA2qvvlUcp_UxXsxi-t7THVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز عملیات طرح جامع پایانه مرزی نوردوز در آینده نزدیک؛ توسعه مبادلات تجاری و ترانزیتی ایران با همسایگان
‌
🔹
معاون وزیر راه و شهرسازی و رئیس سازمان راهداری و حمل‌ونقل جاده‌ای در جریان بازدید از پایانه مرزی نوردوز در استان آذربایجان شرقی، از آغاز عملیات اجرای طرح جامع این پایانه در راستای توسعه مبادلات تجاری و ترانزیتی با کشورهای همسایه خبر داد.
‌
🔹
رضا اکبری گفت: با تأمین اعتبار حدود ۹۰۰ میلیارد تومانی و تعیین پیمانکار و مشاور پروژه، عملیات اجرایی طرح جامع این پایانه پس از ابلاغ قرارداد و در کوتاه‌ترین زمان ممکن آغاز خواهد شد.
‌
🔹
وی به اهمیت راهبردی مرز نوردوز در توسعه مبادلات تجاری و ترانزیتی اشاره و اظهار کرد: توسعه زیرساخت‌ها، افزایش ظرفیت پذیرش و تسهیل در  تردد ناوگان حمل‌ونقل کالا و مسافر از مهمترین اهداف اجرای طرح جامع این پایانه مرزی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/664858" target="_blank">📅 10:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664857">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af34e16564.mp4?token=N2ioBhIiON2BhjU2uoa7m8zuATxMA0MI4RIAwn1N_dyze_6W7xzTDNddLAo64hTdyDzFKh8pmpYsx5sSKPmkr9KPA63LPagAl9c_qfv2WERWE_vfX22xZibzGePfNNZM-Z8CKOPGIuHVtzeYeBLhaIDUydUJIFf-8u6p0Z76NrnlGfc9BMLFT3XlJKygah1zhI-atVbrVEfA-CXof5mOkdSiV4wRyvImlJKpslXDi9pbZdN9U7c2csctWFzCvju7bScOuSqtkgqt2EQPCicVKvk0MO-z8GzWDlD9ykDFJtuvcqwngmKzcsTQyrG44zAsbRxJAdSpVJX0FwU_ZpqiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af34e16564.mp4?token=N2ioBhIiON2BhjU2uoa7m8zuATxMA0MI4RIAwn1N_dyze_6W7xzTDNddLAo64hTdyDzFKh8pmpYsx5sSKPmkr9KPA63LPagAl9c_qfv2WERWE_vfX22xZibzGePfNNZM-Z8CKOPGIuHVtzeYeBLhaIDUydUJIFf-8u6p0Z76NrnlGfc9BMLFT3XlJKygah1zhI-atVbrVEfA-CXof5mOkdSiV4wRyvImlJKpslXDi9pbZdN9U7c2csctWFzCvju7bScOuSqtkgqt2EQPCicVKvk0MO-z8GzWDlD9ykDFJtuvcqwngmKzcsTQyrG44zAsbRxJAdSpVJX0FwU_ZpqiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی روزگاری نوکیا
🔹
نوکیا N95 در سپتامبر ۲۰۰۶ معرفی و در مارس ۲۰۰۷ عرضه شد. این گوشی پرچم‌دار چندرسانه‌ای نوکیا با فروش بیش از ۱۰ میلیون دستگاه یکی از موفق‌ترین گوشی‌های دوران خود بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/664857" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664856">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
معاون وزیر نفت: از کارت سوخت شخصی استفاده کنید و کارت جایگاه فقط برای شرایط اضطراری مانند پایان سهمیه یا نداشتن کارت شخصی به کار گرفته شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/664856" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664855">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb57cd5f5.mp4?token=MjAAyHzd5JXn4K42-PmwPv85nYnPlwZBelADitzz_UCoibIsNEETtx_pJtPwXx-GHLi8AgqL00F1JZSsnaWxjz2R1aTHc6xWoj_fEpcLQhb53GMzIaiQOI0AR59lcznvu9LEP3FJb4lg2ef2FZ0QWt8iyqcFaFSlQieFV4L9P7ZD8kp_hFqtlMq6nccqa4sxWE_pnnUy2FRjbeCpN5XqSHUqAokQEql7vZHYi1-caRzUlMKjnsBhugIFOAJ9DJu2RbWWqMFPuIiwWYbPhSleQmW8GaE-Ee4Cexjyayox_20LTRrE431UWAwhzGvvKChe_cdOqOM-ygzCBvGvaRjYxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb57cd5f5.mp4?token=MjAAyHzd5JXn4K42-PmwPv85nYnPlwZBelADitzz_UCoibIsNEETtx_pJtPwXx-GHLi8AgqL00F1JZSsnaWxjz2R1aTHc6xWoj_fEpcLQhb53GMzIaiQOI0AR59lcznvu9LEP3FJb4lg2ef2FZ0QWt8iyqcFaFSlQieFV4L9P7ZD8kp_hFqtlMq6nccqa4sxWE_pnnUy2FRjbeCpN5XqSHUqAokQEql7vZHYi1-caRzUlMKjnsBhugIFOAJ9DJu2RbWWqMFPuIiwWYbPhSleQmW8GaE-Ee4Cexjyayox_20LTRrE431UWAwhzGvvKChe_cdOqOM-ygzCBvGvaRjYxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در
مزرعه پسر یکی از نمایندگان زن عراق میلیون‌ها دلار که در زیر شن‌ها دفن شده بود، کشف شد. همچنین تعدادی اسب و خودرو مدل بالا نیز توقیف شده
است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/664855" target="_blank">📅 10:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664854">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اعتراف دبیرکل ناتو به همکاری با آمریکا در جنگ علیه ایران: هزاران پرواز از اروپا به سمت ایران بلند شد/ آمریکا بدون اروپا قادر به انجام این عملیات نبود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/664854" target="_blank">📅 10:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664853">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: بدون تردید به نقض آتش‌بس پاسخ می‌دهیم
ابن‌الرضا در گفت‌وگوی تلفنی با وزیر دولت در امور دفاع قطر:
🔹
با اعتماد به برادرانمان، به دشمن اعتماد نداریم و دستانمان روی ماشه قرار دارد و بدون تردید، در صورت هرگونه نقض مفاد آتش‌بس، اقدام و واکنش متناسب و لازم را خواهیم داشت.
🔹
تنگۀ هرمز نباید مورد سوءاستفاده کشورهای فرامنطقه‌ای قرار گیرد. حضور نیروهای بیگانه نه‌تنها امنیت‌آفرین نیست، بلکه موجب افزایش سوءتفاهم، بی‌اعتمادی و ناامنی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/664853" target="_blank">📅 10:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664852">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUkooBD_Hk4kBuwesi3dQaFfTY4K-ToV_7i999bgLXFO5jJdXLJ-M8tM58LCiQGNb5R5csgoC87TRlKnNkbtgf6EdnB3CwtQqe5VQgdHjZg8J7fMdVDTukECXk9o1KHH-DONqzoH-FIZdJzfv4dFstIvUl3LVjTSARihiZ9ZaOzSyF42PzKfe-P_g7GBFhB6sv0nsVLkya7NdyBtYdPcJDdvmN4oxZ87cx8Z9w58KpCsdJLV4asONUd6SG_axwDcNIxmiF4kSfQHRNOTbk6cieH1pjXw4wXqcxuNXooEBz97vsIGQd1bFP32SEx7Tv5tLcpigeNhavirJvryWjtISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ: هدیه‌ای طلایی به کاخ سفید به مناسبت دویست و پنجاهمین سالگرد تولدش
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/664852" target="_blank">📅 10:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پاداش استمرار خدمت فرهنگیان مربوط به سال ۱۴۰۴ به حساب مشمولان واریز شد.
🔹
نخست‌وزیر ارمنستان برای مراسم تشییع پیکر رهبر شهید به ایران می‌آید
🔹
امارات ممنوعیت سفر به لبنان را لغو کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/664851" target="_blank">📅 10:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
انهدام مهمات عمل نکرده دشمن در بندرعباس
🔹
انهدام مهمات عمل نکرده تجاوز آمریکایی - صهیونی در شهرستان بندرعباس محدوده دهستان سرخون و ایسین امروز صورت می‌گیرد.
🔹
احتمال شنیده شدن صدای انفجار، ناشی از عملیات فنی وجود دارد و جای هیچ گونه نگرانی برای شهروندان نیست.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/664850" target="_blank">📅 10:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664849">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41fd695a5.mp4?token=hvbb5Oz23Skdj3FjHQVDUUVxJdEVKFWp96jn8mdKrP80GdQ_9EOJrOM1N5ITH10ZFDXITF7oaZFu9QRt2-bQiS0iXxX5JSY0mt2uMyrynfisRb9JeDmOg08rBoAmcLZ2SczXjTTmqKmCbo3T4G8jARKCH4WMiVh4iKAEmikOXMZaENODGqfofiQnA7oltXKe8MYwXNHzyQzRyZjeh28Wjkt0JfmqFiMgIj2a2EgpztYsw86ddlYv8UsbjwSrPZIReelgOcO4oC-EuYvKKW3P2dKZyMD2qp0Y8ZdjHhocYCYCHombjJCznSK4ALUR7N_Qq1vA1h3pVaxT9HGP15KveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41fd695a5.mp4?token=hvbb5Oz23Skdj3FjHQVDUUVxJdEVKFWp96jn8mdKrP80GdQ_9EOJrOM1N5ITH10ZFDXITF7oaZFu9QRt2-bQiS0iXxX5JSY0mt2uMyrynfisRb9JeDmOg08rBoAmcLZ2SczXjTTmqKmCbo3T4G8jARKCH4WMiVh4iKAEmikOXMZaENODGqfofiQnA7oltXKe8MYwXNHzyQzRyZjeh28Wjkt0JfmqFiMgIj2a2EgpztYsw86ddlYv8UsbjwSrPZIReelgOcO4oC-EuYvKKW3P2dKZyMD2qp0Y8ZdjHhocYCYCHombjJCznSK4ALUR7N_Qq1vA1h3pVaxT9HGP15KveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول مراکش به هلند توسط دیوپ/ مراکش با حذف هلند، ‌حریف کانادا در یک‌هشتم شد
🇲🇦
1️⃣
(۳)
🏆
(۲)
1️⃣
🇳🇱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/664849" target="_blank">📅 10:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6f773f03.mp4?token=ksAeDuauS1Uq8WmNGDUNyzdE7ntzD-VDsp3jQnCvThSSWG0i-AS7j8H6h5HdIFjpumdT9Zn6t84vo8Q2Y0QDAiL1r2Nwv_tINk6rx4JfwHH3jcy2qNekBQsvRtP1jIEzl_A9uXx--0gQ0x8ieLaV_hxP9FWpEY4E7AVe83PWR9UhN2Vtbzp5UzjbQWaObN9PlmG8NZKi20X8caVJv-j0lJb2IfPi3MiOimWg7sZ39rkgbdGa4NIOP_xasr3v5JH-HZysjeOA65BumJyfe9Vdwime66jKpzwrBeYB5fL4sdq6BoXO8LxX6udqp-ZMP-0jcVDZ02fAn4H6vQQOr3U8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6f773f03.mp4?token=ksAeDuauS1Uq8WmNGDUNyzdE7ntzD-VDsp3jQnCvThSSWG0i-AS7j8H6h5HdIFjpumdT9Zn6t84vo8Q2Y0QDAiL1r2Nwv_tINk6rx4JfwHH3jcy2qNekBQsvRtP1jIEzl_A9uXx--0gQ0x8ieLaV_hxP9FWpEY4E7AVe83PWR9UhN2Vtbzp5UzjbQWaObN9PlmG8NZKi20X8caVJv-j0lJb2IfPi3MiOimWg7sZ39rkgbdGa4NIOP_xasr3v5JH-HZysjeOA65BumJyfe9Vdwime66jKpzwrBeYB5fL4sdq6BoXO8LxX6udqp-ZMP-0jcVDZ02fAn4H6vQQOr3U8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خطاهای شناختی در یک نگاه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664848" target="_blank">📅 10:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664847">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp8C97t-43EJ1sUhiU8oYHeu_P-dFUIND8ht6Phg81Tlwbj8Qki2fTxXOitQer-En0hH5OUIAlXqoKluqF4pfhahjsUq-rLIaOqwcidHrkgdJWDEqIA3rX5W1gx6tdRiKOUHTz7pIQ-EdSdMLVJdAd6rjex91EZOSD-5Kc3bj9jHjK9vZkgkRa3V54ZYogrXpf8MG5-3KYV_YN8ZUH4PC55br2NUImZVAOw75wx82qglZc36cumEkJ9uhkUDGY3Y04MRSqYXCwHXMQhk6CxrEmR7HDBrjdT4z1ty36wo1-LuAQpKXvMCwhPXEgDC3uM7N04girvhKY1qdfjb0kDENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه زیبای جمعی از ایرانیان مقیم خارج از کشور به تیم ملی: اگر صدای بی‌احترامی از عده‌ای را شنیدید، لطفاً بدانید که آن صدا، صدای همه ایرانیان نبود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/664847" target="_blank">📅 10:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664846">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ایازی: برخلاف حواشی، علما با مذاکره مخالف نیستند
ایازی، دبیر مجمع محققین و مدرسین حوزه علمیه قم:
🔹
برخلاف فضاسازی‌هایی که گاه در برخی رسانه‌ها و تریبون‌ها دیده می‌شود، بخش قابل توجهی از علما، روحانیان و اندیشمندان با اصل مذاکره و تعامل سازنده با جهان مخالفتی ندارند و آن را راهکاری عقلایی برای کاهش فشارها و حفظ مصالح کشور می‌دانند.
🔹
آنچه گاه به عنوان مخالفت عمومی مطرح می‌شود، بیشتر صدای گروهی پرهیاهو است که به دلیل برخورداری از امکانات رسانه‌ای، صدای بلندتری دارند؛ اما این صدا، الزاما بازتاب‌دهنده دیدگاه اکثریت نخبگان و روحانیت نیست.
🔹
مهم‌ترین سرمایه هر حکومت، اعتماد عمومی است و این سرمایه جز با احترام به کرامت مردم، شنیدن صدای آنان و مشارکت دادن همه جریان‌های دلسوز کشور بازسازی نمی‌شود./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/664846" target="_blank">📅 10:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664845">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a72040862.mp4?token=VjkCF_rC__24MYQQYeHsgP9QrBcfOXQld5RF1tuddc0iDkoy2sWriGPJkRkTqMkWQj9urjy0vrknN5vm3Bd8_mrrm94UqnC9aZSrENToEFrFSxBo04ry6A3YiBeL3vqAZaJw-ycdETEwJVh4A2iGNFa-ErH17jnmbrv10TrXAdxNIE-T7wcN5U9xiPO0LMS9SNIGiqNx89Em1WCxXZ1uM_ILEr-qrKan1EkKANP5IIIWn4NrxGeOA0gDAZ49ROBQGupunzukfWkTiTD0KIeDDgk2Sn3Ppk5WShU5m2BvHVZycX1GQaWs9Tf64e6II7b97KKApSRjcHaXqPx5v7q4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a72040862.mp4?token=VjkCF_rC__24MYQQYeHsgP9QrBcfOXQld5RF1tuddc0iDkoy2sWriGPJkRkTqMkWQj9urjy0vrknN5vm3Bd8_mrrm94UqnC9aZSrENToEFrFSxBo04ry6A3YiBeL3vqAZaJw-ycdETEwJVh4A2iGNFa-ErH17jnmbrv10TrXAdxNIE-T7wcN5U9xiPO0LMS9SNIGiqNx89Em1WCxXZ1uM_ILEr-qrKan1EkKANP5IIIWn4NrxGeOA0gDAZ49ROBQGupunzukfWkTiTD0KIeDDgk2Sn3Ppk5WShU5m2BvHVZycX1GQaWs9Tf64e6II7b97KKApSRjcHaXqPx5v7q4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول هلند به مراکش توسط خاکپو
🇲🇦
0️⃣
🏆
1️⃣
🇳🇱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/664845" target="_blank">📅 10:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664843">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
پزشکیان: توافق اخیر در هماهنگی کامل با رهبر انقلاب و حمایت شعام به‌ دست آمده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/664843" target="_blank">📅 10:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664842">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1970246926.mp4?token=hgI48mwr3Dj3PznGoDkWQlPGNpg6fnMWYkvMfLmZr_4yKdiVEGkK93rQWIbsL2ufpnKqleQiEWLU7QVzv5MTTic0ophwzm-zwtzz1Em7adsk_PUSbE_whG-jjGcg3eltxUOvtz0x8ulZgv2dzFTzQGHwYFnQN_M16j6FgnZANv7xZopzxX2A97jbN7Mq4b7KHAkS16FfLpf5i-8R9GUpSaR3udQ2i66MdUgw6-hJsJbqDPGugnsA7hLGBnW5jzVFCozJGfyRQP7tnyO18-IRUfRbvyDjmFzUL_934CsALmhdsnFz6bJxLghTK7ii2Tw8CaIBJX3_AXQK3d7M5O66vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1970246926.mp4?token=hgI48mwr3Dj3PznGoDkWQlPGNpg6fnMWYkvMfLmZr_4yKdiVEGkK93rQWIbsL2ufpnKqleQiEWLU7QVzv5MTTic0ophwzm-zwtzz1Em7adsk_PUSbE_whG-jjGcg3eltxUOvtz0x8ulZgv2dzFTzQGHwYFnQN_M16j6FgnZANv7xZopzxX2A97jbN7Mq4b7KHAkS16FfLpf5i-8R9GUpSaR3udQ2i66MdUgw6-hJsJbqDPGugnsA7hLGBnW5jzVFCozJGfyRQP7tnyO18-IRUfRbvyDjmFzUL_934CsALmhdsnFz6bJxLghTK7ii2Tw8CaIBJX3_AXQK3d7M5O66vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شادی راهبه‎‌های برزیلی هنگام بازی این تیم و گل سلسائو
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/664842" target="_blank">📅 10:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664841">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سرقت اطلاعات آیفون ۱۸ پرو مکس از یک شرکت هندی
🔹
اطلاعات محرمانه مربوط به گوشی آیفون ۱۸ پرو مکس از یکی از شرکای تجاری اپل در هند به سرقت رفته است.
🔹
رویترز گزارش می‌دهد که اپل به‌ شدت نگران نشت این داده‌هاست، زیرا جزئیات فنی محصولی که هنوز سال‌ها تا عرضه فاصله دارد، در دسترس افراد غیرمجاز قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/664841" target="_blank">📅 09:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664840">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQhxL0jvEAU_C8Kbz9KZUeN8BSt34fizKlMytMllLh7-ef_PEQiy4_SWonUHcwcfFeeiDJybWX7N1Q7s7Tg6rKsXfLeJEDI04-AgD_lvgiIGV9y4zfcB_YRG-emYAY2pKGG0S8hHMgrf9MpPr2QU63HaXkkgAUtWE5Dbij7alfNmYtJsF-yDjrJ4-CG8RC5EmE5bxFuRuiosEeGHUW2ZhXPhgiFvd-oemiZQ4Nfu2RyDvMJyE_U3XnFQtu99bRv-VQokr7NhOT4ermi0t8s1Rq8193uXR5eeQace6UHFA43kX5mLLUC-GRYEc1CMVoc_e5cVkyKFgpe57ODw9G5_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار تند ایران به فرانسه و مکرون؛ دخالت بی‌جا نکن!
آناتولی:
🔹
ایران با رد پیشنهاد مکرون برای همکاری در مین‌روبی تنگه هرمز، به فرانسه هشدار داد که هرگونه دخالت یا سازوکار موازی در این آبراه راهبردی را تحمل نخواهد کرد. عملیات مین‌روبی در تنگه هرمز تنها در چارچوب تفاهمات موجود و توسط ایران انجام می‌شود.
🔹
تهران از پاریس خواست از تحرکات بی‌جا خودداری کند چرا که این اقدامات می‌تواند وضعیت حساس منطقه را پیچیده‌تر کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/664840" target="_blank">📅 09:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664839">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
کیهان: این روز‌ها طرفداران «یک شخصیت سیاسی» برای اثبات نگاه خود در‌باره اینکه رهبر انقلاب گفتند «بنده علی‌الاصول نظر دیگری داشتم»، با بدترین شکل مسئولین نظام را مورد انتقاد قرار می‌دهند
🔹
رهبر شهید می‌گفتند «نقد کردن با تهمت زدن فرق می‌کند؛ مراقب باشید که کسی را متهم نکنید»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/664839" target="_blank">📅 09:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664838">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdmtZwCFgQWwdTJx6_s59Da1Ttle6h46B6s28ltwAHLNkQhrw_7IUGRTGK9Xf5mj3ZR7Rw402VlYP2_3RGyxoUR5ZZmyGo9IjvNdz5ncJgntRGZ93kUJlMQ0dwwM7Abx-LDvxLwKqRYY_rds9_U7QAI723dBuUh9FX5d6BXzyS0E4r3L2UesX41emfpILYgc1V2hYXRLJuiTtmP2EgWkJLqoi43wqVVTedWceo-RHXVbuDGa8jgwryfeaQDwZh0UBMZQYxQZFPEoECIq4dRfb2UjQVx-8bdryo0o76wM6FrnqdnM_aMEH74hCHf8c1b__CdDrFyQIrzc2J3I3P-onA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر نمی‌تونیم بخوابیم یا صبح‌ها احساس خستگی می‌کنیم، چی بخوریم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/664838" target="_blank">📅 09:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664835">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66fb2b0eb0.mp4?token=lGuSfdbGmTO_OvL4znDAlZ33xnQJXJV3h6HqSMICaKFdVHCNbhdvp2e4tdHSHj47kujLKrQ1srhEAMSxMFNkKSbKlUrwE5oHd2ZUEfYroT_Fesftbg3Cf8nInHGAQxrhRpBFZl46wkl37Yy1x1TU1LeIRjq1WE_o17ELpa7SvpAMp-P1wLAMiUXwjdkQ6HAXvQapzLfzJo8my41WjzUPr7h1EFW8UbjabsY5MdITlTiVnKM7UrCcewkvGptM9axvqj9xxQm56_4GZ0vkPN24FupkOTwrI2DwdfRg5cTpbmoYDjCMgTFIHkO04ZakGU6FqoRVP5cBioKwaFr3EqbKVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66fb2b0eb0.mp4?token=lGuSfdbGmTO_OvL4znDAlZ33xnQJXJV3h6HqSMICaKFdVHCNbhdvp2e4tdHSHj47kujLKrQ1srhEAMSxMFNkKSbKlUrwE5oHd2ZUEfYroT_Fesftbg3Cf8nInHGAQxrhRpBFZl46wkl37Yy1x1TU1LeIRjq1WE_o17ELpa7SvpAMp-P1wLAMiUXwjdkQ6HAXvQapzLfzJo8my41WjzUPr7h1EFW8UbjabsY5MdITlTiVnKM7UrCcewkvGptM9axvqj9xxQm56_4GZ0vkPN24FupkOTwrI2DwdfRg5cTpbmoYDjCMgTFIHkO04ZakGU6FqoRVP5cBioKwaFr3EqbKVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
قاب احساسی اسماعیل صیباری، ستاره مراکشی‌ها بعد از صعود به یک هشتم در آغوش مادرش
🥹
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664835" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664834">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bapW7JdEBGrgkuLMkvWB9t4Ey8hhWzKbwhxmkLdk1-ccbaS3-ioU5nkYgh1JcdnJy6tFo1zxLVrsDNbaIPW3_C9FTvAEzWkznrq18t3TWMpGNvr331w9NW0s6r4iaBe6VKuMyQN4xYZwg8z2G7aqI0DSb9CZ74wj-1b_0yJvG-M5K66UY5wYWuAaeWNgvZWi6sjbDCS5gjfjQqz-aXLpJfKWErDu7wRKYieDnWs7CmGEfWcK3UEXZvbtmYoU_B2WzoAVxXCeD6G7GlcY5AzOats6pESHMHMgRbnfjSZxFaSVsUpH5FPJnlpVNUnBKs3vk26pNaBMePwCvFFzHTkBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاراگوئه تعطیل شد
🔹
رییس‌جمهور پاراگوئه، در یک دستور به نهادهای دولتی و خصوصی این کشور، روز شکست آلمان را جشن ملی و تعطیل رسمی، اعلام کرد.
🔹
آلمان در بازی مقابل پاراگوئه، در ضربات پنالتی، شکست خورد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/664834" target="_blank">📅 09:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664833">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg0EhvCyG5d3aGXf-Y3t_1OhkFO204Lant0PBjGyRhdgfJ76rNSetAKK7NlMs4srEek_NMx02nknZibPaLQP1jbolM0GwiFAgvK7HRBiHe57Zd3OhATNiwg3F9crUJKwulcl0h1aDO3i5NYrVb574tzzR6U6RiUuHxOZu6lLMNy-YYFhP4UEPHiJ5dtumFqk9KoZx9hWJBuTR9Qr_6omFSUvtLHGIPojH95G9gWoZvQnRofH1GTGecBdKesdHs8PTEO54L6jLq0vBL-0V4BZnKtxPBgTSpGCKPELHqyDRhUYM-0SK_v-ZRljy6LrWdn3i7cqS2lMDvEXfuOsAMaY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی برق می‌رود، دخل مغازه هم خاموش می‌شود
🔹
قطعی برق فقط خاموش شدن چراغ‌ها نیست؛ برای بسیاری از مغازه‌های کوچک، یعنی توقف فروش، اختلال در کار و خسارت روزانه
#برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664833" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664831">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c44222d.mp4?token=IKO5uvQWT9S3b8y2ecyCKiDMAowC1ryIHokROjqP9tn6yXf-f61G4OJR34KXtKBU5ETj17ErBWqW2R2uKkJL_bLmmBlMjwx0gJ_yVYn5h3tLAjlmEyv99NSQL-ojr79DFdnanrab8-pwlS6DyFEYmhWViqoekita-OjTva5TxAVukU47TwOkIUYtONzzfXUfd-b8lKVVlzikni6lcEJGJ6Stj3txt0YLVScJD2dlxHTfRXjvFOjVWonSVffU1KVzde1WXKTaroKOaTufb8ag_QJvriyR7g-Mij9c4FFIWNo-TFwj67eZvZOELErTLyD6noKjXGbvepfRi2EIUCXXVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c44222d.mp4?token=IKO5uvQWT9S3b8y2ecyCKiDMAowC1ryIHokROjqP9tn6yXf-f61G4OJR34KXtKBU5ETj17ErBWqW2R2uKkJL_bLmmBlMjwx0gJ_yVYn5h3tLAjlmEyv99NSQL-ojr79DFdnanrab8-pwlS6DyFEYmhWViqoekita-OjTva5TxAVukU47TwOkIUYtONzzfXUfd-b8lKVVlzikni6lcEJGJ6Stj3txt0YLVScJD2dlxHTfRXjvFOjVWonSVffU1KVzde1WXKTaroKOaTufb8ag_QJvriyR7g-Mij9c4FFIWNo-TFwj67eZvZOELErTLyD6noKjXGbvepfRi2EIUCXXVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پاراگوئه به آلمان توسط انسیسو در دقیقه ۴۲
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/664831" target="_blank">📅 09:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664829">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LG7BUS3rW-GLIDdkeWZXZMRfg7-TYnxab90tf9yL9KdnYrzLd5PgUSWnYEQR8ho2WZxuHJsVAgwf5sjC50Qz0lYdWfgRwg_RdNtF9mCy8I3lJxqhX5q0DS8PT8l-wPTk9_jMX2Ud36R188l31c0LMJDZABlKmGBa70EeYF48OJ7fUz9-mNKO-Ul0ldFqK-OcN9gZamnH9Rhf6-SjUiZA5kq6hamQiS6j22Qjk1fIGoUE0MhLVQKRsCvfdnVBhqUHemWGkwCvpFVxYbPHDBRyLcFtcpgBiVFpCFHKlBKKryD5hwaUn4C4_pji04Ln4TPlBn72quNHRnPXqG9Ms3YhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLvwaAnIMfne9VQHWPR88n_PCNzuDAm6hQWC2DDY7VysbY4J6mz3R4TVQqx9Q6QXdrKQR_Vn8MFMg2fQojF5SvCrAHyoSIrv1pfs-K-EGQ4XDcoWCFViai_AQ5TGdMvipUIy2beKXJ9D0HkSHW3wtwk_rbXCYDVijgbjUF6XtyH6-Ve3_slPkwneCLYpPzpSgh28FLmSN4ox54ganJItPGdkuDGdKo0CAnS7STZW7hc0xyC5mPllJs6-KmILspb6jOsP8van91-LB5hkEIcyGrGjrV_K7cIRZRRxhCbGs4ZBTO7lZy0jBbj9zY9V0ixNSe7W2isHbfNNgwd0k-lXVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
بازیکنان تیم ملی بعد از جام جهانی رفتن مرکز خرید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/664829" target="_blank">📅 09:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664828">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq2G04fmDEq_YlwxxBT9gugw1x4HDVKoA67Ac73z3l0O36tVYESvFegA7Lww2x-nTap6qEst-2EeFKCqpNJoP5Z-A7knvZvC4KEp743ArzmnKQL_ra5htI3abulpjDnMcwxcnUERugaq135UHnNtQi9VCwy6naJskzFYMum41-5ekUvDSxDvInGgdYe9iKF3KfIv6S54UH5zChzXkW4K9cu2Zi8_QNmQLz2MkHH-L_roYNRUiQ-wTWEgryD_1zr2n5ivkW7yIOFJiZVVTg4UIObPwRBaYaf349fA9fOq8GVODw1dQ-JIrFKkvmlMu3vvyg1rX1kYCni40HNWVtP7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین دیگر برای تو جای امنی نخواهد بود. این سرانجام ظلم است، دفن شدن در باتلاق وحشت و تنهایی
העולם, זה לא בתולה לך. נקבר ב ביצה לבד
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/664828" target="_blank">📅 09:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664825">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تمهیدات ویژه برای مراسم وداع و تشییع رهبر شهید  استاندار تهران:
🔹
مراسم وداع با رهبر شهید انقلاب در مصلای تهران، از ساعت ۶ صبح سیزدهم تیر آغاز شده و تا ساعت ۲۰ چهاردهم ادامه خواهد داشت
🔹
مراسم اصلی تشییع نیز روز پانزدهم تیر از ساعت ۶ صبح شروع می‌شود.
🔹
برای…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/664825" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664824">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBA-h8fs2QH2ajmYtq0JOHEuvZrG3oY_HaRhanneScR1LqE55rfz6rvNc7XUoYxOSPVHgGkwk57SkdbGsgB2UaHOAH68ggDh8mp-zcPpTUg3mgdf6FwXdac9dhs5Z6nE3EXm2WweASYkj0Nvy2Y-yaznHGw2Og0-cvuY9yKHsT7-pDf9jWFkZLdxi6tR0fSfnss1-nNrq0-DfkOcsaT72Mqq7Q6kfoBWnAcYy_DV6TMKrjmcYKWcMSHrkI35MvM5BWdH2ev6gG_sl5G4fMbsWDo29v9zt37oGY0L6e91KrBCV030nABRe3b8_KXV0aDTOv5u7POSe-Au_lLKVxSfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطرناک‌ترین جاده ایران، جاده روستای ناندل در آمل
🔹
از جاده هراز تا بالا ۵ کیلومتر مسیر که ۶۰۰ متر ارتفاع میره بالا یعنی به اندازه دو تا برج میلاد
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/664824" target="_blank">📅 08:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664822">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3314d934e.mp4?token=lXUXVXrmmQZj8xrmkDJtU0AmcT-hQWRdk2rxdVgw1KWuZfeOnWFuB92IyTn0EbG37Y1-h8uVhCLc2A4V3gTpPcC3WPT9iRfmZefF1GKo9tX_tr0NAw1nu5SqQWiNIasfRg0JQ4QUCoJgxBVlrXRnzfWHc4Ko5XIMJ8INEYHxOmUc0n-l0StPVkwCvmMuxq-Vy8_WihdW9hDyz_LFs50MVBUsFqEgwo6cdyQhkWhkU51ly_cdGoLcQsfZ3hJLq2U-lNqlWyPeUORJpfqkCzYFKsq5RFaHh0U4pZqCN1-tXD1t8TcbHcI_9sxdDkbfVl4F1GEEdhoq_3DHsytywLe3KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3314d934e.mp4?token=lXUXVXrmmQZj8xrmkDJtU0AmcT-hQWRdk2rxdVgw1KWuZfeOnWFuB92IyTn0EbG37Y1-h8uVhCLc2A4V3gTpPcC3WPT9iRfmZefF1GKo9tX_tr0NAw1nu5SqQWiNIasfRg0JQ4QUCoJgxBVlrXRnzfWHc4Ko5XIMJ8INEYHxOmUc0n-l0StPVkwCvmMuxq-Vy8_WihdW9hDyz_LFs50MVBUsFqEgwo6cdyQhkWhkU51ly_cdGoLcQsfZ3hJLq2U-lNqlWyPeUORJpfqkCzYFKsq5RFaHh0U4pZqCN1-tXD1t8TcbHcI_9sxdDkbfVl4F1GEEdhoq_3DHsytywLe3KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش احساسی دختر ایرانی به کودک سیاه‌پوست؛ ویدیویی که از ۱۰ میلیون بازدید گذشت
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/664822" target="_blank">📅 08:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664820">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46e47cbd0.mp4?token=IP9poB-rfFcL9B9wI8NmW9a5jpsV2_LZ4vY6mvcdKm8cW-BaoBPaoSelJkXSQdMhjVvQ4KkxX6FrNLa60mTCRJdNJaeTV_KEnfVlArvcWoqQh3rhvNTc-XidWXG1AM__SKbogEbiR8-vl9PEtFihMZLiU2IspgABm_5iBz5Nne7x7fn5o8Akjm9z50fX6ECb8ZKx0HtYXqYvoi2gXd3zbRYMIDosk6kDnT4b8sSdGWmN2aKxeiDRTdgDcOAT5nH92nQVi-2lUrFseT5N01DNP7ADzk7duNV_ldez6oK8mhirBf5JoCJsspwY5cqSgGe3rxYq9v540lLEUfKSyRMIcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46e47cbd0.mp4?token=IP9poB-rfFcL9B9wI8NmW9a5jpsV2_LZ4vY6mvcdKm8cW-BaoBPaoSelJkXSQdMhjVvQ4KkxX6FrNLa60mTCRJdNJaeTV_KEnfVlArvcWoqQh3rhvNTc-XidWXG1AM__SKbogEbiR8-vl9PEtFihMZLiU2IspgABm_5iBz5Nne7x7fn5o8Akjm9z50fX6ECb8ZKx0HtYXqYvoi2gXd3zbRYMIDosk6kDnT4b8sSdGWmN2aKxeiDRTdgDcOAT5nH92nQVi-2lUrFseT5N01DNP7ADzk7duNV_ldez6oK8mhirBf5JoCJsspwY5cqSgGe3rxYq9v540lLEUfKSyRMIcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این تمرین، با قوز کمر خداحافظی کنید #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/664820" target="_blank">📅 08:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664819">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd8a86337.mp4?token=hPvUU2ED8dLt6T-bAEtua5wjSlXIp91nLWNnrk_KYF-hMQNHneo5KPFURLqWiIxKbToESLlRoSFAd1q8LzOlxWsR34NaIeQWBMvss-OZgFZVtz0pG3Yrhybn1X5ChS04Jt-aPS2nESpTnGbUJACLo1JsVgOYu_vn9r_JKSKbIdvoMiSQez46spwapz51tTw2pQuIxnJjUh8bpv9gVk_3d2J2p5qYK6KfGZodeYNpaZFEv6fTXS8rA-Do4spEEeAS-PX_DsdaT6MMN3xk2U4DN0Ku1bINJFWHC7igRuVWNqP07yFzOhTJ489IrTfkWeulx_sWhKxcw-zUPw8o5yk5UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd8a86337.mp4?token=hPvUU2ED8dLt6T-bAEtua5wjSlXIp91nLWNnrk_KYF-hMQNHneo5KPFURLqWiIxKbToESLlRoSFAd1q8LzOlxWsR34NaIeQWBMvss-OZgFZVtz0pG3Yrhybn1X5ChS04Jt-aPS2nESpTnGbUJACLo1JsVgOYu_vn9r_JKSKbIdvoMiSQez46spwapz51tTw2pQuIxnJjUh8bpv9gVk_3d2J2p5qYK6KfGZodeYNpaZFEv6fTXS8rA-Do4spEEeAS-PX_DsdaT6MMN3xk2U4DN0Ku1bINJFWHC7igRuVWNqP07yFzOhTJ489IrTfkWeulx_sWhKxcw-zUPw8o5yk5UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هراس اینترنشنال از تشییع امام شهید؛ اعتراف ناخواسته به قدرت بزرگ و نگرانی از تشییع باشکوه و میلیونی
🔹
مراسمی که قبل از آغاز، این مزدوران اسرائیلی را چنین آشفته کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/664819" target="_blank">📅 08:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664817">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
مسیر عمانی هرمز با اخطار سپاه از کشتی خالی شد
🔹
بعد از گذشت یک هفته از رونمایی کریدور جدید عمانی برای عبور از هرمز، داده‌های دریانوردی نشان می‌دهد که به دنبال اخطار سپاه، این مسیر اکنون با توقف تقریباً کامل تردد مواجه شده است.
🔹
از زمان اعلام مسیر عمانی در تاریخ ۲۴ ژوئن تا پیش از این تغییر اخیر، حداقل ۱۲۰ فروند کشتی از این مسیر تردد کرده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/664817" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX5cBPHavGG-NND8d95EINvNP7MVXVOI3QECl4xKBUfNj5wb7rFrtsH2LzuLY3f7p9KMkrPqi5PrriLrMnv9XhDya2K0qsf0_9oTEksjIT89yO8_Fv49cjXzChvWqILXnNGByUgy2BMZYAjpm2WMIzdPIg1YiK64iU6bH8PBTPA8UAGXag5MqUT_4oS5tXLY8jXg6sVROCbhxZBL3pN3xFQL12Ufc8psU_icHpec829kfdE4m_Zt1G6MxATwNVZutNO80PqcL_DQ-KfGVVnTJkB5rAQwJ1JIVOq4hkiVdt60RVswaOF4FBopAyQuo1W4F0n8A8QuI6XyofN4-J8x_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدیدترین بروزرسانی نمودار مرحله حذفی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/664815" target="_blank">📅 07:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664812">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-FG7PEzVs9NDsKOxrpx7Wik8k2ttmcBmraUfVrH6aOWsX493eZr0ppwZOBJc-It1hlDApjWsCMDSusFBOXNPnhalIi-e20NPXcPgw5EW4_q4w8-Bdk4k1yBBstwW6zu17k4ycjANF_FQBtyS-5VLHkjYCRvTTDvx_JwMlDepXeI3RMef8IR5V4BNllKvo3eRI4o5euY3nhti4UvVpUup6ZtZd1Lh3lWNltVTVeH9M1Zfqq0AQwEIu5DIorF0kFKqDDWJIpeKIWupMRBdJ9_Uq54nrtTAFNmEdR4O7RWCp-US2Gh1740FeKixivakFXyzc7mrJLKtMo8fgUMvnrmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت دو پاسدار در درگیری مسلحانه با گروهک های تروریستی در پاوه
🔹
به گزارش منابع محلی، شامگاه امروز یک درگیری بین نیروهای امنیتی و عناصر تروریستی تجزیه طلب در شهرستان مرزی پاوه در استان کردستان رخ داد  #اخبار_کردستان در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/664812" target="_blank">📅 07:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664811">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سی‌ان‌ان: ویتکاف راهی قطر شده است
🔹
شبکه «سی‌ان‌ان» به نقل از مقام‌های آمریکایی گزارش داد که نماینده ویژه رئیس‌جمهور آمریکا برای حضور در مذاکرات با نمایندگان ایران در نشست دوحه، راهی قطر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/664811" target="_blank">📅 07:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K79hu-NxZFPMSG6tmG2JCUdZw5rmpiOQ9IlhODpaD7SlJLYh-LzczqnAm04lkhysMBNRdzh5761c4DH5EuxOaV4Y4HwJ3gUdYE56XcrZmh6ZoeFKoNRAI6Q8x4dFGFolDEPGUxQn5NvO8RG8MDCS3vBsxHYoRajvaY8mDBe6fW38zAgA8BwHNZ3nUWbcLoz85AH4EOf68boZFmxXTOqX8QVn_DS2um3Jff8vk15a4e4QPFL3ZGYzEAhGe3lB-80EeG1O41SKsZOiujR7J6HEs_KqCNJnhIKiXWvsFJVEb5MQKhXF2MMNGd-os9ESvCWO_ZatpdnFoLGEWijs6WZblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۹ تیر ماه
۱۵ محرم ‌۱۴۴۸
۳۰ ژوئن ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/664810" target="_blank">📅 07:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664808">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شهادت دو پاسدار در درگیری مسلحانه با گروهک های تروریستی در پاوه
🔹
به گزارش منابع محلی، شامگاه امروز یک درگیری بین نیروهای امنیتی و عناصر تروریستی تجزیه طلب در شهرستان مرزی پاوه در استان کردستان رخ داد
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/akhbarefori/664808" target="_blank">📅 01:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664807">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91cbf495a8.mp4?token=Qla8ABc6DRflUc4AjYkSg1SRp1FSBvxkIMqs4IX4Ua_BVyW2f3PH6nZjJpd7Wb6q43P-uwDBhJMeo3EkhY9lbUtOj-aSiIsV9GxS0AeS6pZaKixtOXXMGP-xYurb4hlsQswVhokXzSXyoBEampI3Pk7pgGmiVADNgGuox2jTrkUxQG67HNUedjY7F3tvWdKIV_Gnx15u-G9AGupRzJUHN3GAfbXXoaGwfcmYWQBM4X-1R1tX7_BNFOnDtnnxmthy39O8DEaoz00JsmdA-ofgDtf8p3FNTvac4sF72vqNIn7KR6jpO0VVHX0FNaTBzVDITNaEeqXghS66VatDCpDtMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91cbf495a8.mp4?token=Qla8ABc6DRflUc4AjYkSg1SRp1FSBvxkIMqs4IX4Ua_BVyW2f3PH6nZjJpd7Wb6q43P-uwDBhJMeo3EkhY9lbUtOj-aSiIsV9GxS0AeS6pZaKixtOXXMGP-xYurb4hlsQswVhokXzSXyoBEampI3Pk7pgGmiVADNgGuox2jTrkUxQG67HNUedjY7F3tvWdKIV_Gnx15u-G9AGupRzJUHN3GAfbXXoaGwfcmYWQBM4X-1R1tX7_BNFOnDtnnxmthy39O8DEaoz00JsmdA-ofgDtf8p3FNTvac4sF72vqNIn7KR6jpO0VVHX0FNaTBzVDITNaEeqXghS66VatDCpDtMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین روش برای برش میوه های مختلف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/akhbarefori/664807" target="_blank">📅 01:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664806">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c4b3af88.mp4?token=mYUuRZpGT7doAUh0CYCa1SS8PAL34x_H99SGz1GV8Gx1nKIPYFfGXh5YZh0u_MLeg4IZmSnvyq_gNmxZRJnB2drJnXhtdPlx_33g1VZcp1VndXNfbhoLeA3NbR5KMBrfMjMiJZSngq_7L5pXjZZjVbsECOkoAw8upFQTDL1p0NYCIE2kXmbfMsn9s4zdN62orjnzFfgdsaib0NhVCNWv4zsUZPTmSUXLLt1udwR7M5sXkjnbrRoHCZoFBQS4fLl54KOHpOGDEf_xvF6QDR8L1ubWamlCHAxx3HEqiLEa0BnzvDmZi9BOiip4BO_DzWF_ItPyZh2McNVWuMAZjZmBnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c4b3af88.mp4?token=mYUuRZpGT7doAUh0CYCa1SS8PAL34x_H99SGz1GV8Gx1nKIPYFfGXh5YZh0u_MLeg4IZmSnvyq_gNmxZRJnB2drJnXhtdPlx_33g1VZcp1VndXNfbhoLeA3NbR5KMBrfMjMiJZSngq_7L5pXjZZjVbsECOkoAw8upFQTDL1p0NYCIE2kXmbfMsn9s4zdN62orjnzFfgdsaib0NhVCNWv4zsUZPTmSUXLLt1udwR7M5sXkjnbrRoHCZoFBQS4fLl54KOHpOGDEf_xvF6QDR8L1ubWamlCHAxx3HEqiLEa0BnzvDmZi9BOiip4BO_DzWF_ItPyZh2McNVWuMAZjZmBnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از آماده سازی محل وداع با پیکر مطهر رهبر شهید انقلاب در مصلی تهران #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/akhbarefori/664806" target="_blank">📅 01:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664805">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
حمایت چارچوب هماهنگی از اقدام دولت الزیدی در مبارزه با فساد
🔹
«چارچوب هماهنگی» بزرگترین فراکسیون شیعیان در پارلمان عراق ضمن اعلام حمایت از اقدامات دولت برای مبارزه با فساد، آن را گامی ضروری برای بازگشت اعتماد به روند سیاسی کشور دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/akhbarefori/664805" target="_blank">📅 01:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664802">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439f50420e.mp4?token=jTOxc-bR06mCZ8r6P_c3JH0l3NMqHqs24Hxd6n104_VQpCI08shBnj5AbWSZOhE8lNGqun8604amaD1LytY8v1zlAXrf32Hu-77nEipU0PJVXt1DRK-z2GChyOX2PEuq1b4VDblGxAP9XnivanVgUt3hnr8UG1LNVbX5e3-uwpuxDWZiyGnp21tPdqBBD_JHy9bsYXM1lZXVxgRDVxSsXvcEReqlDp_RW02dAkCDi9u1ftRxlyHMmATcw770rpGle9nKPaha8ADTZbaEIPsT9-1p5qibfv5Sijl0IcX5C3MIXdZaHcgVaZcgsApBvSbFFz5GIZ1GNE1_ywp5cWsMWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439f50420e.mp4?token=jTOxc-bR06mCZ8r6P_c3JH0l3NMqHqs24Hxd6n104_VQpCI08shBnj5AbWSZOhE8lNGqun8604amaD1LytY8v1zlAXrf32Hu-77nEipU0PJVXt1DRK-z2GChyOX2PEuq1b4VDblGxAP9XnivanVgUt3hnr8UG1LNVbX5e3-uwpuxDWZiyGnp21tPdqBBD_JHy9bsYXM1lZXVxgRDVxSsXvcEReqlDp_RW02dAkCDi9u1ftRxlyHMmATcw770rpGle9nKPaha8ADTZbaEIPsT9-1p5qibfv5Sijl0IcX5C3MIXdZaHcgVaZcgsApBvSbFFz5GIZ1GNE1_ywp5cWsMWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت به کره در حضور انبوهی از معترضان
🔹
هواداران با کوبیدن طبل‌ها، شعار «هونگ میونگ بو اخراج شود!» سر دادند و به سرمربی سابق توهین و ناسزا گفتن #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/akhbarefori/664802" target="_blank">📅 00:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664801">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
حداد عادل: تشییع پیکر رهبر شهید، فرصتی است که مردم بغض در گلو را خالی کنند
🔹
چهار ماه است که پیکر رهبر شهید انقلاب در انتظار تشییع و دفن است. مردم هنوز بغض خود را نشکستند و زمان تشییع فرصتی است که مردم بغض در گلو را خالی کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/664801" target="_blank">📅 00:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664800">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750487189c.mp4?token=hgkwPdXL8KkPMJ_vDFmDrPCZH6vqgy7GxYKmMNqO4NPL1REKHSBvov2Vu2-aFI0yVyqujGy8gcEEUDQU4VGqnf4GRZWEpctKewOevFBpT5xxuO9nIbrecKQN5xRCN4dyhgSxtRfsYbrVAPXrUhPIy9oinxuqN1nnb-X60hanZeVTeLjd7rmPEbIrXplUqXc3PLBlPK3aXfqDZoO5bHlC8nmvfP0pKv-1w7Eo56QdvecQe33b0q06vloGBHJwhAX_YN4ilQ9z060gjn3n4lorLqmIUCVlzXzlKO_WSPJolWKf79YpOOaPBmvQQd7Pf8e4ejAp2zmkdxpzgAosYGOfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750487189c.mp4?token=hgkwPdXL8KkPMJ_vDFmDrPCZH6vqgy7GxYKmMNqO4NPL1REKHSBvov2Vu2-aFI0yVyqujGy8gcEEUDQU4VGqnf4GRZWEpctKewOevFBpT5xxuO9nIbrecKQN5xRCN4dyhgSxtRfsYbrVAPXrUhPIy9oinxuqN1nnb-X60hanZeVTeLjd7rmPEbIrXplUqXc3PLBlPK3aXfqDZoO5bHlC8nmvfP0pKv-1w7Eo56QdvecQe33b0q06vloGBHJwhAX_YN4ilQ9z060gjn3n4lorLqmIUCVlzXzlKO_WSPJolWKf79YpOOaPBmvQQd7Pf8e4ejAp2zmkdxpzgAosYGOfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پاراگوئه به آلمان توسط انسیسو در دقیقه ۴۲
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/664800" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChtFv6y6aE3XnoaSxxabdEb1ReKOuAv1wzVdwK99k_99-_84GxgYxlAghcyVjyEyMti87HV7KImauEnfdPURSF3dzgABL66YPdfr6nZw_RLEqhtw_ieVaLUOP5CrHEHmEJJ9HRO09RHKlUEDU1sII6E1LzG0xc8tRKrV6e6yBgAaQQg5RUgtQ-n-z1yuP9q6w4RTcIV97uFGafGTkyNNTWSNLmncFtYcgNWAt2jki_SqBVJr6CYK92OGMaE4XJ428KNNIQf8cYO44yy_uB5GcICSfW2DTuY-dkpuuJOP-CpTnrk9GYofEsyOzc3VaDo4iCXKEBcQIf5-tdSqlv7e9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVpcgOZKKyOIN7yMYWgLEkq5mOI9QSgjRavhpcmbYmLnyA4XyqveMT06aKrxb8GUptBaKgsMKipD6k_TZ3-e423chon4AN-8NOTRiVLwhLnR2xQulIUXsnS_BM2MTxJIDBntwk86IeOwU7f3y6firdXSH-979CN3wDT8JbekIMdWkeiqR3WpY2l6TdkggLiwW42LYqLVw8iwbCVKQPBjQ6xsQsa_m_ICHgAja63UrgUnW1Mong6D9zwJbC5lAdcHe_WGV7vS-D7UukjIk1uP2_NBsyQzD8InIaBqDOTvOsw6R4qijgq2W5yBB4lggB7qOtr426N7ggzp8N-0Adio3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3HSODwJ2yGO0bGPMhmIBDpOAOrfztlMTBYED7-bZ61pDycoK7Kx_opfe562Kx4BN0-vKs4Or5zdueSbZS4pCnGCVrIsa4VzF5pxs8E63VZjn42qOnYLt0fyTGEtC2DqC7mgYt3WyGxTAwZGjKmkWu3gYpxiksNpQE0b65JTm9IzQxbGxTGhz3GYlyHkkW-TfsbGNPlafiRCygHycyZkYPtBFO4g9Shm9hLYQZw6tNfJ-A8IY5s7By-RfbcpZnD5u979Gh6JSu4PNVaE8FUf4CllIQSG1V0YrVGlohxMRNNcLshWnoDue5Qs4eKUc2g_PNW9Jo8_hHz8pVPJec57sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر زیبا از ماه کامل در آسمان امشب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/664797" target="_blank">📅 00:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTZEt_Qi6aQjeanTmt9ZWPbkV2KLot_hOMn61o-799rRzbXE8rWBKOO9YSbWHgXGTzmpUooqPnLp_LxzVU8T-TG8DFHGkbwS_SSkJe1b6sgq7-qkmREIMQMd8p4s5Lkw-epHIeS0vjNtmmwbccE8CKG_H32qtREv1WDvKWnjzgoSLVAirLaP4v7u3dBjABAmzSWG7Yb0rYOMeMNqTOVpudjTabi0YpKsXUAdkko_Wqu43efvK_5Kke6FAhDs82sELpu5wfGjLJVI2tgd9RPq4gdjoszW9HXdyU13bp76a9HkDbmkUS3OSrmMf-vHo79dlz0Da3r1cjD0vr4urQSb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت رهبر انقلاب، نه یک اتفاق سیاسی، بلکه فصلی از حماسه جاودانه کربلا در حافظه جمعی شیعه و در امتداد آن است. مسئولین نظام جمهوری اسلامی باید بدانند خونخواهی قائد شهید، در واقع  خونخواهی سالار شهیدان کربلا است
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/664796" target="_blank">📅 00:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28149bc86.mp4?token=S_0RJjd4yp6z9JVndvOkMeUHgFvLqusYONgf-fAQ1DsQJKWoCdNiodKyVimmo3LVV_C-U9YW1jrzF8xTMrA9GVYr5iLT__XZD6dTt-RQj1QGNkTnBmhYJcso2YW5U6I-fVSNJXvDV6PTq7T5rCB84M20JgtQcDQVD1v_7caPoI3mOfeQH2VOqApNMOdmuJfSuK6npIGRayGaimahMSIB4XZIDXMa6iez76xgn_TdXPJHv7VtZLBmMzXm3F4Z4oKyireUbSKamapgDlnLreSgVqg6R9CPkzbIf73WpK1ERXZRWsHfFh7O2LQTuMNMwC0wmXaOxskK3vYIdgkRV-0wFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28149bc86.mp4?token=S_0RJjd4yp6z9JVndvOkMeUHgFvLqusYONgf-fAQ1DsQJKWoCdNiodKyVimmo3LVV_C-U9YW1jrzF8xTMrA9GVYr5iLT__XZD6dTt-RQj1QGNkTnBmhYJcso2YW5U6I-fVSNJXvDV6PTq7T5rCB84M20JgtQcDQVD1v_7caPoI3mOfeQH2VOqApNMOdmuJfSuK6npIGRayGaimahMSIB4XZIDXMa6iez76xgn_TdXPJHv7VtZLBmMzXm3F4Z4oKyireUbSKamapgDlnLreSgVqg6R9CPkzbIf73WpK1ERXZRWsHfFh7O2LQTuMNMwC0wmXaOxskK3vYIdgkRV-0wFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌صحنه داستان اسباب‌بازی ۲؛ شاهکاری که نزدیک بود هرگز ساخته نشود!
🔹
در جریان تولید، بخش بزرگی از فایل‌های فیلم به‌اشتباه حذف شد، اما یک نسخه پشتیبان که روی کامپیوتر یکی از اعضای پیکسار بود، این شاهکار رو نجات داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/664795" target="_blank">📅 00:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d58b8227.mp4?token=c4hYzOYY3JAcd5Gx97P0MfYwgmHq6clBoGt88KODYA71vV7Ku_0d0Z6rAhvkjMSE1dziZmZLdUjOmwaCTLuhyLvzXWElEgOEACJc1rZbrc1QoHJZd2BxFr9YNvYjnWz8RWd_ekwSheUPfhVJA2h8UJheRX2TK-aTTQJU3eCFCFTNIn_g162NXwAraKQr7p4_Z8xwAeWEKQHQ2ZMGdv-KGclOgyoS8uHxq0j6srtTZSRbRM3ns7DNPClMEEYnwEOxNgHeSemEC6goZuDA-SCwbvEgOkcebE85OWxZcF8e7saRdG4gET_s-M-7i7QqcAG3_GuAH9bLJjhHhBGBlqIrSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d58b8227.mp4?token=c4hYzOYY3JAcd5Gx97P0MfYwgmHq6clBoGt88KODYA71vV7Ku_0d0Z6rAhvkjMSE1dziZmZLdUjOmwaCTLuhyLvzXWElEgOEACJc1rZbrc1QoHJZd2BxFr9YNvYjnWz8RWd_ekwSheUPfhVJA2h8UJheRX2TK-aTTQJU3eCFCFTNIn_g162NXwAraKQr7p4_Z8xwAeWEKQHQ2ZMGdv-KGclOgyoS8uHxq0j6srtTZSRbRM3ns7DNPClMEEYnwEOxNgHeSemEC6goZuDA-SCwbvEgOkcebE85OWxZcF8e7saRdG4gET_s-M-7i7QqcAG3_GuAH9bLJjhHhBGBlqIrSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کناره‌گیری سرمربی کره جنوبی پس از حذف از جام جهانی؛ تلویزیون ملی تصویر او را تار کرد
🔹
کره جنوبی بعد حذف، سرمربی‌اش رفت و تصویرش محو شد؛ بدون توهم توطئه، بدون تهمت تبانی. فقط پذیرش واقعیت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/664794" target="_blank">📅 00:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYeMZn2r6VRIV5cplZHb_o7LeNm6Tz5cLryrmPmrDbvaxmZv4K7FULJyGot9S3jIxQoaUAzxzgtGhYjpIU1xpUVTFoGqCVJhnGFcXJe1cgc92eNWJ4lOywubsiseScYsrT8glmMX2dMwldHkHf000sXO1QgYPQeCO5v38kLXLLCiT3DggRAluocBJdZoAcSc8jx53KlM3p7YrVoPMm1Z-2agPBfQQ5-qbWn40L2q28uetXb2lpBbyeAXPNKoKphINPgoVR0b8ubKpvx_MxOmhBFS4wekjjtXEjwH-MjSHoHwbXHwTQSn7UsI_TMzftrahQ-jGCZEDSvQt5Q2TfB_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_پنجم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید بزرگوار مهدیس نظری  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/664793" target="_blank">📅 00:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5214eca511.mp4?token=iy6PVcTBo5klERhGpKvkAwj28qLAoECe0XJI6F63ulgVOgpxJmolJdPLX3JHzoqnS6P1EJWR-tsyNHqgsJs-toDOu50jXqptGmlCi59nTwmcwkqUsjhkvn48Fa_s7OHPBr9CfuuFNDha1SlRpcl__IfAB6PumPlDb5CugHzOUCWM6zlyRUorOaHtkTYIEq--M7uXOMAvRnERdrwcxOD0QefJHJEN56XFqo2XV21CgM6SP9gpAfPGPFSrpj8fMbQlfsedVmcikZPQkyvS5ytE7A0v6NqK5gmzUCxEOcGw_6HwQkPwvzkBd7G54YkFBnAMdeI2pYmx-pSKKRobFdsTag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5214eca511.mp4?token=iy6PVcTBo5klERhGpKvkAwj28qLAoECe0XJI6F63ulgVOgpxJmolJdPLX3JHzoqnS6P1EJWR-tsyNHqgsJs-toDOu50jXqptGmlCi59nTwmcwkqUsjhkvn48Fa_s7OHPBr9CfuuFNDha1SlRpcl__IfAB6PumPlDb5CugHzOUCWM6zlyRUorOaHtkTYIEq--M7uXOMAvRnERdrwcxOD0QefJHJEN56XFqo2XV21CgM6SP9gpAfPGPFSrpj8fMbQlfsedVmcikZPQkyvS5ytE7A0v6NqK5gmzUCxEOcGw_6HwQkPwvzkBd7G54YkFBnAMdeI2pYmx-pSKKRobFdsTag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس کودکان به شهادت رسیده لبنانی در حملات اسرائیل به لبنان در دستان کودکان در عزاداری محرم در شهر دیر بورن ایالت میشیگان آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/664792" target="_blank">📅 00:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664784">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnlNHMMsk7G2CO6L3diTiiX_Yu8iad7t-0GTYaJoPF72ZKKTGc69ohQPAK9zW5jN_JnmIDVmtOEJu6BXpD8Q0y1-knhfVaaKTDCz_GzHaPbViQ5t1DjKfNwQS1vNyB5zNz1ZByfqGj2eyYLFtfHwHXbqNrPHdSRAj1FSut94J_X64tEo3KwJNIYr-ouaat2XVP-PNk1hZ24XK8z4EPcMJTCVhBTCZcEOn2ombM1EtLQ30nRvxCJgLBcUTaWwSYR0wByT_cIhKbWPgAHABxogvMQFv87OaOTwIipUQXKiG80vJ3Y4nTJxE0AgRqp_MPR7e8OUUNwRzpNKZjr7pM7SnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-UYWlvj8yPgfIYp6DoMr5LoetSApTYcLYzb0fPodRz6uNLDstZ6_v8XcvsFiD3tVvr9LmcepSHWn3UyKNHQ_rC74R4oE3G2wqeUruvlbAUyo1yocWSJXG3bRFsmLwqr9_XCbEPxAK53KyVmFjKnwuhes5AqdeEO2qSA8TTOPEYfeFHNwYVsizCMN3E6qj9z1Y8i8dq6mfhd5KwBtLT95Kzr8aBpCboOaOpwM0WokoecNdUKK7MMQQ9aEWXwMED5qMl4NhxH3nhdCgNrk-zYFhhlvnsRwPMCpn1yUPQzyyFVpEA1wXpA7NFh2KeuRwvy9kOFMUOoZJKuDnPxbBvKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNBcJjMzTwBpkgtqLAREyCmDqqhJYV-1yLUfF9x8hCLQVVz7MRBckMFE6mgNFepNXMaLeP1E_XDT2Fzc__DrO1UHvScpcSM8do6ftGEKdTJF9ojHNPezgezUD2dNtbnvK5BpF0OxkjkBaIqD2Tx2hEWgfPwoOuBi4Aso6shJkhaA43OtgfiW4vpPQRC_dS9VCon49NlE2e6mw8Qz_KVKdMbkqNJ3774PuMKt4iTJ6uIxEeLjiEXka25Crh06KZ9DGXPx9fYJGY4XPEvnNWVa08PoT08bX6LLC_erw8G9O2vQD39nQZ0kW-WDMvYUMmBgY3FxE1NOlEIvAm7K67Xfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diTeBKWe70pfr4hsLJ05PBjdJfqamlzrJQD35fyq09Zpj-Y07f3Ndjum0uxuoszYr4Lpvcrn-7CrmxxD1Wn1RROdSvaM_3ku1BMjAirGTCOXtILvCpIwWx7SKhFVIRIfMms6DW39roHpr1l8l-En35uqzAw6C7iFlSbGB2p3RGN6buBoQ90T_oZK368C3LYhh3pJlA8ifU0HCtlq89P7TasVcxk96QGwGX11FCTN8uVM3dEv9tuVD2Nt2Te19aYSZH75HhlAIebbCc-Qza1Yv684SiSzUMfat-Wt8payOTyrZXtuDNuBWSijZ1XLhabUqdzeHT14GXjH4bwxpO6Fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2e6wNltHelZIJQ5-k6ZauvgwIons2Qom4RwmH50325TWkNrvK2IqGx6iS6_-E4SRJfUc6qxEkyiZJEawgHiWhMLrrF5L-EfQCaCB4Bb9TH0w4tRsXZ5ZmxWrltT9UOnUBPKM22uC2EQNNIonmjkLY9-ZKS6ayldKwaJ4IJ05h85cz41YT1gWtp1_1E9GR9FA1x9m93rTCEB4jRLu81XXOA-UhV4MluNdKHq_0wbVarwDK1vmosDpXHxa9EPstf4aMvQdjf3KCd_An2IRCMuOBskxh8TtY-WQydA9GMa0ZaFgA4j6y090oIbyXdyNhMG7YBcgPj7LVXittTzt12f4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUqGnmDAi_wRJLetNQsDluCXgZfspLVZUXBoI11E3-lMPr8XCNOkfdXKk_Q7yDFKoJcxRLZ3EcjUtd1Ye5P65Wb66EI7Pv--4rH1Zmj-_KYZAaYyjaxYTzsmPuAWmdxatnWDAEh5wIAlz4KevMMLB-kFhcGZGlIBMsEHVALDnI_iS_FRy387LPy3fJFlEK6tTERKEHWzso-gBWEXodmGomKvN3k4WQYEbhZscWCUnKEhYweLqVQdqBBxzW4q-DMgToqOUFl62qovEbNrMJggX4Re8P2jQU0GdtIFG8U23F1TELYonT943m0wz9-7PsaYTj6uLlRA5BaWQ52HZSMOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCUhamKJDdoReQbe5h8AEOrfOgxnwq-RyhPK2OwFB7semQa6phHbVbC3cofB_61d8Zwtv5Wr9qxDAh09WugKxx7r1Ela4XRQUJHbeBjcoCtmCTDPmqV97RrOvWh8ag4s_W42iRc1fHBJbGVDqAW8B4ES8dNMWRvJn9tIMCrelDrd8n4FLti00dpnYEsMqhXH7HExjICqAZmQ8O5mm_LSQo9OzQ1-Uvswf7spOJ-_gMTGxJSOyJvowp2ZYQxx1ls1nwrImQiaXhTNjzh4BXKWVSRXIO3LBRPNUDQcxiAThYPJmYWHQS30lHrxL7O_ZfDSMRTVD72qJG1i-Qt8kjem7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDZijZMdKKE0w2s3piPTnel9QneNCwwhAPyAWiUU_igY7Nd8w1AIGarhF1vCOch2Zg_cPalkMaUzpXiCCmNYrllQTUrEsa4EwWoJDoadX-BcAxMa0bTDOP5WmTElrVKfIgMq67PUdgbej8t0MX1NfJ7BDziCQWRVjRMxC-AcvAPlYPHdMcjZ6cAXvK-peUiyARKa8_HNB9hmOLmZ2zUtqMFrwKjDDiyZVlHLa_3kqRZ4QqeEJDg_HiZCsbqycuJGzgPKPBJdXs4_sUPLvQrdHpj73ObdTqrZQGvPObNPgxJlXRI3M6gWq4LxAgoC58EBSY_lobC3oGgpXbqHYMHozg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدام مواد مخدر سریع‌تر اعتیاد ایجاد می‌کند؟
🔹
سرعت وابستگی به انواع مواد مخدر به عواملی مثل ژنتیک، سن، سلامت‌روان، دوز مصرف، روش مصرف و دفعات مصرف بستگی دارد.
🔹
اما از نظر علمی، بازهم مشخص است که برخی مواد افیونی با چندبار مصرف اعتیاد ایجاد می‌کند. در این اسلایدها ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/664784" target="_blank">📅 00:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664783">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d4be0c04.mp4?token=jj0MvcVV-aNfmkSI37bDxVoyUooxo-mQ2oXc5Ap3Xwvvh80snQq6Td6c1qeP8NfaO2HuWvukcYtA5JMaAp2NvZ7qUTaLKeiWSqfLIgmbwTSB_J2um1TkEor-T0k-qIJX-rI-1JUeP3BaEaSrHoOGEmGe7em4ECIyh8urnW29ekTpHoea7ZdjgXrY9gd_yZM5OOH03sQpL_9EyZr0sLzZYgPzcxrdIxN9lHiGqWpbV8hQt_3BJOpcVnKW60ZcI-eiYVjrM3y4ux_UjeEA5LVKHT6jAmkSIis6qDTdlrx6rSfJjgBiGSgSXu6MlIz-veCc-EFa4djQpXN3XeNO_2Io_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d4be0c04.mp4?token=jj0MvcVV-aNfmkSI37bDxVoyUooxo-mQ2oXc5Ap3Xwvvh80snQq6Td6c1qeP8NfaO2HuWvukcYtA5JMaAp2NvZ7qUTaLKeiWSqfLIgmbwTSB_J2um1TkEor-T0k-qIJX-rI-1JUeP3BaEaSrHoOGEmGe7em4ECIyh8urnW29ekTpHoea7ZdjgXrY9gd_yZM5OOH03sQpL_9EyZr0sLzZYgPzcxrdIxN9lHiGqWpbV8hQt_3BJOpcVnKW60ZcI-eiYVjrM3y4ux_UjeEA5LVKHT6jAmkSIis6qDTdlrx6rSfJjgBiGSgSXu6MlIz-veCc-EFa4djQpXN3XeNO_2Io_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من با مسکن پول زیادی درآوردم؛ دموکرات‌ها لایحه حمایت مسکن را دوست دارند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/664783" target="_blank">📅 00:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664781">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
فساد بزرگ در وزارت نفت عراق؛ ضبط میلیون‌ها دلار اموال از یک مقام ارشد
شورای عالی قضایی عراق اعلام کرد:
🔹
در نتیجه تحقیقات اولیه از متهم بازداشت‌شده (معاون وزیر نفت در امور توزیع)، مبالغی شامل ۱۱ میلیون دلار پول نقد، ۴ میلیارد دینار عراقی و چندین فقره ملک کشف و ضبط شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/664781" target="_blank">📅 00:08 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
