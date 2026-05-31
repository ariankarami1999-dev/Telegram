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
<img src="https://cdn4.telesco.pe/file/LFcuQXxrf274e7JT5cOiGo5yQyWuJw5afbfTOptWp3lSN3CrQeIKnUsonMOYbJL8CUv-8HFeFHswsF-atpVCPdGK_cFux9kDymmZnY9RPzW7xE5kUxnNtvGoucj9tQMFM9BhdpgVMg24mKAUkQ_C1Gazr7AFWkEu3Dka5OGgn_W0FoCdAzsyhiqusGo13bS18ZHDh-o3ZslMEqqOTHNS61pqWJY1vaZXD_eQbtjTH9nb_ehqrTT8TxzC-Ikl_I2jzmTeRz7iKL4TclgE-CPtcMKMi_5lkMFJHhux7l4Cpff0Ql9rTSO44G5iPRHTFBDFt3Go5AlKDj8b4aBS3nsxVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 283K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 16:27:18</div>
<hr>

<div class="tg-post" id="msg-13039">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سی‌ن‌ان: ایران ۵۰ ورودی از ۶۹ ورودی تونل‌های تاسیسات هدف قرارگرفته موشکی را باز کرده است
@withyashar</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/withyashar/13039" target="_blank">📅 16:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13038">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سی‌ان‌ان: برای وارد کردن آسیب به تاسیسات موشکی ایران باید از سلاح‌های بسیار پیچیده و بسیار گران‌قیمت استفاده کرد، اما عملیات بازیابی با فناوری بسیار ساده‌ای انجام می‌شود، فقط با بولدوزر
@withyashar</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/withyashar/13038" target="_blank">📅 16:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13037">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">متن چکیده نسخه ۲
بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی
شاهزاده گرامی،
این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و ایجاد مسیر عملی برای آینده ایران ارائه می‌شود.
در شرایط کنونی، جامعه ایران تحت فشارهای شدید اقتصادی، اجتماعی، امنیتی و سیاسی قرار دارد و در کنار آن، یکی از مهم‌ترین چالش‌ها، نبود یک ساختار منسجم و قابل فهم برای سازماندهی ظرفیت عظیم مردمی و تبدیل آن به یک نیروی هماهنگ است.
⸻
1. ضرورت ایجاد ساختار یا پلتفرم سازماندهی ملی
مطالبه گسترده مردم، ایجاد یک ساختار یا پلتفرم منسجم است که بتواند:
نیروهای مردمی داخل و خارج کشور را شبکه‌سازی کند
وظایف و نقش‌ها را مشخص و قابل اجرا نماید
از پراکندگی و موازی‌کاری جلوگیری کند
مسیر فعالیت گروه‌ها و افراد را شفاف و هدفمند سازد
امکان هماهنگی عملی در سطح رسانه‌ای، اجتماعی و میدانی را فراهم کند
⸻
2. انسجام و اتحاد میان جریان‌های مختلف مخالف
درخواست جدی جامعه، ایجاد سازوکاری برای
همگرایی و هماهنگی میان گروه‌ها، جریان‌ها و افراد مختلف مخالف حکومت
است تا:
اختلافات مانع حرکت مشترک نشود
یک محور هماهنگ‌کننده واحد وجود داشته باشد
انرژی سیاسی و اجتماعی هدر نرود
⸻
3. ضرورت اعلام چارچوب زمانی و نقشه راه عملی
یکی از مهم‌ترین دغدغه‌های مردم، نبود زمان‌بندی روشن برای مراحل مختلف حرکت سیاسی است.
مطالبه عمومی این است که:
سناریوهای مختلف به‌صورت شفاف و مرحله‌بندی‌شده مشخص شوند
برای اقدامات جمعی،
چارچوب زمانی تقریبی یا بازه‌های مشخص تصمیم‌گیری و اقدام
اعلام شود
مردم بدانند در هر مرحله چه انتظاری باید داشته باشند و نقش آنها چیست
همچنین بخش مهمی از جامعه خواستار آن است که در صورت وجود شرایط مناسب،
فراخوان‌های مشخص، هدفمند و زمان‌دار
برای اقدامات جمعی و هماهنگ صادر شود تا انرژی اجتماعی به‌صورت پراکنده و فرسایشی از بین نرود.
⸻
4. آمادگی میدانی و سازوکارهای حمایتی در شرایط بحران
بخش قابل توجهی از پیام‌ها بر ضرورت ایجاد سازوکارهایی برای حمایت از مردم در شرایط بحرانی تأکید دارد؛ به‌گونه‌ای که:
شبکه‌های حمایتی و سازمانی امن شکل گیرد
هماهنگی میان نیروهای مردمی افزایش یابد
آمادگی اجتماعی و مدنی برای شرایط حساس تقویت شود
هزینه انسانی تحولات احتمالی کاهش یابد
⸻
5. شفافیت در ساختار مشاوران و تیم تصمیم‌سازی
یکی از مطالبات مهم، شفاف‌تر شدن ساختار مشاوران و نقش افراد در حلقه تصمیم‌گیری است تا:
جایگاه افراد مشخص باشد
اعتماد عمومی تقویت شود
از ابهام و چندصدایی غیرسازنده جلوگیری گردد
⸻
6. معیشت و وضعیت اقتصادی مردم
در کنار موضوعات سیاسی، بحران معیشتی یکی از اصلی‌ترین فشارهای روزمره مردم است.
درخواست عمومی این است که در کنار برنامه‌های کلان،
راهکارهایی برای کاهش فشار اقتصادی و حمایت از اقشار آسیب‌پذیر در دوره گذار
نیز در نظر گرفته شود.
⸻
7. ارتباط مستقیم‌تر با جامعه و گروه‌های مختلف
مردم خواستار ارتباط فعال‌تر، مستقیم‌تر و مستمرتر میان رهبری اپوزیسیون و بدنه اجتماعی هستند تا:
ابهامات کاهش یابد
اعتماد افزایش پیدا کند
و امکان هماهنگی واقعی میان گروه‌ها فراهم شود
⸻
جمع‌بندی
در مجموع، پیام مشترک این مجموعه دیدگاه‌ها چنین است:
جامعه ایران آماده تغییر است، اما این مسیر تنها در صورتی به نتیجه می‌رسد که با انسجام، شفافیت، ساختار اجرایی روشن، نقشه راه قابل فهم و ارتباط مستمر با مردم همراه باشد.
⸻
درخواست پایانی (از طرف نماینده جمع)
در پایان، اینجانب یاشار به عنوان نماینده جمعی از این دیدگاه‌ها، با نهایت احترام درخواست دارم امکان
ارتباط مستقیم برای انتقال دیدگاه‌ها و هماهنگی بیشتر
فراهم شود و پاسخ این پیام برای اینجانب ارسال گردد.
راه‌های ارتباطی جهت پاسخ
پاینده ایران ، جاوید شاه
@withyashar</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/withyashar/13037" target="_blank">📅 15:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13036">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/withyashar/13036" target="_blank">📅 15:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13035">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خودمو یادم رفت
🥲</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/13035" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13034">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoheil</strong></div>
<div class="tg-text">یاشار چرا درخواست اینکه با خودت حرف بزنن تا اینارو بگی رو نداریم ؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/13034" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13033">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenyamin Qaem</strong></div>
<div class="tg-text">پس این متن چه اشاره ای به تو داره؟
ما میخایم یاشار با شاهزاده در ارتباط باشه</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/13033" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13032">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHannaee</strong></div>
<div class="tg-text">جاوید شاهم بگو یاشار</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/13032" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13031">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/13031" target="_blank">📅 15:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13030">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">متن چکیده شده نسخه ۱
⸻
بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی
شاهزاده گرامی،
ایرانیان داخل و خارج از کشور، با وجود تفاوت دیدگاه‌ها و تجربه‌های متفاوت، در یک نقطه اشتراک دارند: امید به عبور ایران از وضعیت کنونی و رسیدن به آینده‌ای آزاد، باثبات و شایسته ملت ایران.
در سال‌های گذشته، اعتراضات و جنبش‌های متعدد با هزینه‌های سنگین انسانی و اجتماعی همراه بوده و بخش بزرگی از جامعه همچنان در وضعیت فشار اقتصادی، ناامنی روانی، سرکوب سیاسی و ناامیدی نسبت به آینده قرار دارد. در کنار این شرایط، فضای سیاسی اپوزیسیون نیز از نگاه بسیاری از مردم دچار پراکندگی، نبود انسجام و فقدان نقشه راه عملی و قابل سنجش است.
مطالبه اصلی بخش بزرگی از مردم نه صرفاً شعار، بلکه
وجود یک ساختار روشن، قابل فهم و اجرایی برای گذار سیاسی و دوران پس از آن
است؛ ساختاری که بتواند اعتماد عمومی را حفظ کرده و انرژی اجتماعی را به مسیر مؤثر تبدیل کند.
در همین راستا، مهم‌ترین پیشنهادها و خواسته‌های مشترک به شرح زیر جمع‌بندی می‌شود:
1. ضرورت ارائه نقشه راه روشن و مرحله‌بندی‌شده
بخش بزرگی از جامعه خواستار آن است که مسیر حرکت، شامل اهداف کوتاه‌مدت، میان‌مدت و بلندمدت، به‌صورت شفاف مشخص شود؛ به‌گونه‌ای که مردم بدانند در هر مرحله چه نقشی دارند و نتیجه نهایی چگونه تعریف می‌شود.
2. ایجاد ساختار منسجم و شبیه «دولت در تبعید»
پیشنهاد شده است یک ساختار هماهنگ و چندلایه شامل بخش‌های مختلف شکل گیرد؛ از جمله:
رهبری و شورای مرکزی تصمیم‌گیری
تیم‌های رسانه‌ای داخلی و بین‌المللی
تیم‌های سیاست‌گذاری و برنامه‌ریزی اقتصادی و حقوقی
شبکه‌های ارتباطی و سازماندهی اجتماعی داخل و خارج کشور
تیم تحلیل و نظارت برای ارزیابی عملکرد و اصلاح مسیر
ساختار مقابله با جنگ روانی و عملیات اطلاعاتی
هدف از این ساختار، کاهش پراکندگی، افزایش کارآمدی و ایجاد یک مرجع واحد برای هماهنگی فعالیت‌ها عنوان شده است.
3. شفافیت، اعتمادسازی و گزارش‌دهی
یکی از مطالبات مهم، شفافیت در عملکرد، نحوه تصمیم‌گیری‌ها و مسیرهای حمایتی (از جمله مالی و رسانه‌ای) است. ارائه گزارش‌های منظم می‌تواند اعتماد عمومی را تقویت کرده و مشارکت مردم را افزایش دهد.
4. استفاده از ظرفیت همه اقشار و تنوع اجتماعی ایران
درخواست شده است که نمایندگان اقوام، اصناف، متخصصان، جوانان و گروه‌های مختلف اجتماعی در ساختار تصمیم‌سازی حضور داشته باشند تا احساس نمایندگی و مشارکت واقعی در میان مردم تقویت شود.
5. سازماندهی مشارکت مردمی در داخل و خارج کشور
بسیاری از پیام‌ها بر ضرورت ایجاد شبکه‌های منسجم مردمی در حوزه‌های رسانه‌ای، اجتماعی، مدنی و حمایتی تأکید دارند تا انرژی عظیم پراکنده در فضای مجازی و میدانی به یک مسیر هماهنگ تبدیل شود.
6. تمرکز بر انسجام به جای پراکندگی
یکی از نگرانی‌های جدی، تعدد صداها، اختلافات درونی و نبود فرماندهی واحد در جبهه مخالفان است. درخواست عمومی این است که انسجام، هماهنگی و وحدت عملی جایگزین فعالیت‌های پراکنده شود.
7. ضرورت فعال‌تر شدن ارتباط با افکار عمومی
بخش قابل توجهی از مردم خواستار ارتباط مستمرتر، روشن‌تر و مستقیم‌تر رهبری اپوزیسیون با جامعه هستند؛ به‌گونه‌ای که ابهامات، پرسش‌ها و نگرانی‌ها بدون فاصله زمانی طولانی پاسخ داده شود.
8. آینده‌نگری برای دوران گذار و پس از آن
در کنار موضوع تغییر سیاسی، مردم نسبت به آینده پس از آن نیز دغدغه جدی دارند؛ از جمله ساختار حکمرانی، عدالت، فرصت‌های برابر، توسعه اقتصادی، و جلوگیری از تکرار تمرکز قدرت.
⸻
در جمع‌بندی، پیام مشترک همه دیدگاه‌ها این است که:
جامعه ایران آماده تغییر است، اما این آمادگی نیازمند سازماندهی، شفافیت، برنامه‌ریزی و یک محور هماهنگ‌کننده قابل اعتماد است.
در پایان، این مجموعه نظرات با نیت خیرخواهانه و از سر دغدغه برای آینده ایران ارائه می‌شود و هدف آن تقویت مسیر همبستگی ملی و افزایش کارآمدی حرکت جمعی ایرانیان است.
پاینده ایران
@withyashar</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/withyashar/13030" target="_blank">📅 15:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13029">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/withyashar/13029" target="_blank">📅 15:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو: عملیات زمینی در لبنان را گسترش می‌دهیم
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد به ارتش این کشور دستور داده است دامنه عملیات زمینی در لبنان را گسترش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/13028" target="_blank">📅 15:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اسرائیل هیوم: ترامپ به دلیل ترس از شکست در انتخابات میان دوره ای جنگ را متوقف کرد و بعد از انتخابات جنگ را ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/13027" target="_blank">📅 15:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">صدای انفجار در قشم مربوط به یک مین شناور بود که در حال حرکت به سمت یک کشتی بود و آمریکا منفجرش کرد
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/13026" target="_blank">📅 15:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdieh</strong></div>
<div class="tg-text">سلام اقا یاشار ،لطفا به اون اقا یا خانومی که بلوچ هستن بفرمایید  که  من یکی از اون افرادی هستم مه هر ماه برای مردم سیستان پ بلوچستان کمک میفرستم و واقعا ذوسشوت دارم چون واقعا مظلوم واقع شدن و از دیروز که فهمیدم که ۲۴ الی ۴۷ ساعت اب ندارن  انقدر حالم خراب که انگار منم الان اونجام  ،قلبم به درد میاد براشون ،بلوچ هر چی بگه حق داره از بس توو این سال‌های اذیتشون کردن</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/withyashar/13025" target="_blank">📅 15:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13024">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/withyashar/13024" target="_blank">📅 15:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓟</strong></div>
<div class="tg-text">یاشار اگه حوصلشو داری‌ میتونی برای کسایی که جدید اومدن ویس هایی که مهمه تحلیلش برای رسیدن به اون درکی که باید برسیم رو پین کنی که با دیدن پین ها دسترسی سریعتر داشته باشن</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/withyashar/13023" target="_blank">📅 15:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from..</strong></div>
<div class="tg-text">مردم ما هیچ اتحادی باهم ندارن اقایاشار از مردم کشورم خیلی دلخورم، من ی بلوچم، الان حتی توو همین مجازی هرکسی ک منو ببینه فقط توهین میشنوم فقط چون بلوچم واقعا خیلی دلم شکسته از هموطنای خودم  اخه چرا مگ ماها ایرانی نیستیم مگ ما چیکارشون کردیم،  ماهم سالهاست داره جوونامون بچه هامون کشته میشن سال هاست زیر ظلم این رژیم هستیم . اصلا قبل همه این داستانا با تمام بدبختی ک داریم  تنهایی جلوشون وایسادیم هیچکس نبود، ازتون میخوام این پیاممو بزارین تو چنلتونن
🙏🏼
تازمانی ک ماها از همدیگ بدمون میاد حتی این رژیمم عوض بشه این کشور هیچوقت درست نمیشه</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/withyashar/13022" target="_blank">📅 15:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">روابط‌عمومی ۳پا : صدای انفجار در بندرعباس مربوط به خنثی‌سازی مهمات عمل‌نکرده است.
@withyashar</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/withyashar/13021" target="_blank">📅 14:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13020">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیویورک‌تایمز: ترامپ شروط توافق احتمالی با جمهوری اسلامی رو سخت‌تر کرده و نسخه اصلاح‌شده رو برای بررسی دوباره به تهران فرستاده.
طبق این گزارش، اختلاف‌ها به‌ویژه بر سر آزادسازی منابع مالی ایران ادامه داره و واشینگتن تلاش می‌کنه با افزایش فشار، روند مذاکرات رو تسریع کنه.
@withyashar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/13020" target="_blank">📅 14:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/13019" target="_blank">📅 14:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13018">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPari</strong></div>
<div class="tg-text">به عنوان خردادی میگم حالا که موضوعش پیش اومد
😂
ما اخلاقمون دقیقاااا همون عربس که داره مسافر میبره قاهره
کار خودمونو میکنیما ولی پستی بلندی زیاد داره مسیرمون</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/13018" target="_blank">📅 14:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13017">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دم کسایی‌که حمایت میکنند گرم
🙌🏾
❤️‍🩹</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/13017" target="_blank">📅 14:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm</strong></div>
<div class="tg-text">ی روز درمیون ب صد نفر میفرستم</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/13016" target="_blank">📅 14:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13015">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm</strong></div>
<div class="tg-text">لینک کانال تلگرامتو</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/13015" target="_blank">📅 14:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چیزی ‌نیست صدای
“واریز ناموفق: موجودی کافی نیسته!”
@withyashar
🤣</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/13014" target="_blank">📅 14:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صدای انفجار در قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/13013" target="_blank">📅 14:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چندین گزارش صدای مهیب در بندر عباس
@withyashar
🚨</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/13012" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
دونالد ترامپ ( ۷۹ سال )
۲۴ خرداد ۱۳۲۵
🇺🇸
مارکو روبیو ( ۵۵ سال )
۷ خرداد ۱۳۵۰
🇺🇸
پیت هگست ( ۴۵ سال )
۱۶ خرداد ۱۳۵۹
@withyashar
😃</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/13011" target="_blank">📅 13:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13010">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARSALANVK</strong></div>
<div class="tg-text">یاشار در داخل ایران فاز مردم مثل آب و هوای خردادی هاست واقعا!!! مودی و اصلا مشخص نیست مردم هم خودشون چی میخوان!!!</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/13010" target="_blank">📅 13:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13009">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/13009" target="_blank">📅 13:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13008">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">https://youtu.be/tRWhvFylQtk</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/13008" target="_blank">📅 13:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سلام خواهشا بگید مگه چندسالتونه ک جام جهانی 1997 هم دیدید..نمیخوره بهتون ک سن بالا باشد</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/13007" target="_blank">📅 13:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13006">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-text">سلام خواهشا بگید مگه چندسالتونه ک جام جهانی 1997 هم دیدید..نمیخوره بهتون ک سن بالا باشد</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/13006" target="_blank">📅 13:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الجزیره: [جنگ آمریکا و اسراییل علیه ایران]، فضایی را ایجاد کرده است که در آن هر دو طرف احساس پیروزی می‌کنند و بنابراین تمایل دارند در مذاکرات احتمالی برای امتیازات بیشتر تلاش کنند و این امر تلاش‌ها برای کاهش تنش را پیچیده می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/13005" target="_blank">📅 12:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13004">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حالا چرا اینا الان نشون دادم ولی کم میذارم؟ یکی این که نگن پس فردا یاشار اومد اینجا، نمیدونم فلان جا بهش پول داد… بدون اینا رو داشت و ول کرد تازه و درس دوم این که بدونن که میتونست بره برای خودش عشقشو کنه کنه، ولی نکرد و قید همه چیز رو زد حتی‌سلامتیشو …. اونایه دیگه خون مردم رو تو شیشه میکنند و هزار جور کار می کنند که تهش شاید بشن این ! شاید !</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/13004" target="_blank">📅 12:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13003">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حس میکنم تریدری
🌚</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/13003" target="_blank">📅 12:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13002">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-text">حس میکنم تریدری
🌚</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/13002" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13001">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فعلا میرم بیرون  یه کاری دارم  به اخبار‌ ادامه میدیم منم یه هوایی بخورم انقدر عصبی نشم…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/13001" target="_blank">📅 12:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13000">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLtpU7EGbgdv4RKZ-Dpui0-0NgRWYn2-57AOm-Z8MJIADBgMPR04pPcrTIyVhOF1-QqFj0Op3kIa4QGPEZ130dxC8uQ7QQMNbUqif_IbysRTNcgHG9icAr6KsD_EazBbRKQ1imgUelJHAgNlSOtXp7IeBLYRP1UR4TdkOKNTe0JuJi6zItHYFrq4xhyQ78zzNsHbzeiemGC9OY-cqYaNx0d7LJOfns6FOOG5YXQ-mjsyPWWWrQ3DOfUkia5qVto2EgkHplLnRRM5D26HgRA9sARhWo1J77TBwolF-_FceUyz6yoNyDdpOEVZH-v6cCqx1i50Z5woJotJpM5Wx2eK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم SVR و G63 البته یه بنتلی GTC W12 و یه مازراتی MC و یه لیموزین بنز ۶ در و یه SL fabdesign هم دارم ، ۶ تا کلا
🥹
حالا به وقتش‌میبینید</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/13000" target="_blank">📅 12:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12999">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مشروب یه کالای‌ مصرفیه ! کل اون مشروبا ۱۵۰۰$ بشه پول یه ماه یه کارگر معمولی اینجا ، البته نه کل مشروبام تو کمد هم باز‌ هست
🤣
…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/12999" target="_blank">📅 12:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFarham</strong></div>
<div class="tg-text">یاشار میشه شغل اصلیت بگی خواهش میکنم‌جواب پیام بده خیلی مشتاقم بدونم اون همه مشروب چطوری کار کردی خریدی
💔</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/12998" target="_blank">📅 12:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12997">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b74ad7b47.mp4?token=sQTaoBc83pBFM3bYjrbGJQs-jMFPgVPK8SOd-s1SCa4d8uC7aOHxPttz2s-3jJvR2JoARwsrW-UaXe6WEkTNzgafejmH4lJEhUzfnWTwjILBb4BOaYPkm_Uv7_10UXDVuCmFHJY5btSf4pmbPKP0cApBQBK4ScAhtAnoj73iAPg2CU4gzKxizVc2s7Uogo3iPV9ZTHuESxDIklui6Q8r_YZXyo46Bhy5cUUfDHCufOpu7jPl9B_0uebOLxdqCO7_mEygYoTAnskC16oCSAMfvIb-ex_1wduIjrHToz_biq7-d_gUv3akeAUFFAdIKpjFux9qHeT3zSTc4XvoSuP0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b74ad7b47.mp4?token=sQTaoBc83pBFM3bYjrbGJQs-jMFPgVPK8SOd-s1SCa4d8uC7aOHxPttz2s-3jJvR2JoARwsrW-UaXe6WEkTNzgafejmH4lJEhUzfnWTwjILBb4BOaYPkm_Uv7_10UXDVuCmFHJY5btSf4pmbPKP0cApBQBK4ScAhtAnoj73iAPg2CU4gzKxizVc2s7Uogo3iPV9ZTHuESxDIklui6Q8r_YZXyo46Bhy5cUUfDHCufOpu7jPl9B_0uebOLxdqCO7_mEygYoTAnskC16oCSAMfvIb-ex_1wduIjrHToz_biq7-d_gUv3akeAUFFAdIKpjFux9qHeT3zSTc4XvoSuP0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/12997" target="_blank">📅 12:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12996">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/12996" target="_blank">📅 12:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نیویورک تایمز:  ایران خواسته های واشنگتن برای تسلیم کردن ذخایر اورانیوم غنی‌شده‌اش را رد کرده است
.
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/12995" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12994">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/12994" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12993">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/12993" target="_blank">📅 11:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12992">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromkamyar</strong></div>
<div class="tg-text">یاشار خیلی حرف های درست و حسابی میزنی دردش اینکه هنوز یکسری هستن که حرفاتو قبول ندارن چقدر باید هزینه بدیم تا همه بیدار شن؟</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/12992" target="_blank">📅 11:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/12991" target="_blank">📅 11:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEmmmmmaaaadddf</strong></div>
<div class="tg-text">داداش ما باید فحشت بدم جواب بدی</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/12990" target="_blank">📅 11:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/12989" target="_blank">📅 11:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/12988" target="_blank">📅 11:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehran</strong></div>
<div class="tg-text">درود یاشار جان احتمال داره دوباره متحد بشیم برا خیابونا</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/12987" target="_blank">📅 11:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/12986" target="_blank">📅 11:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARVIN🏎️</strong></div>
<div class="tg-text">درود یاشار جان خسته نباشی
♥️
این حرف که میگن مردمو مسلح کنن باعث جنگ داخلی و سوریه و عراق شدن میشه رو نظرتو میگی راجبش
🙏🏻
♥️</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/12985" target="_blank">📅 11:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12984">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">@withyashar
SCARY MOVIE</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/12984" target="_blank">📅 11:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12983">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from2585</strong></div>
<div class="tg-text">درود
موافق پوریا زراعتی نیستم
جولانی تروریست بود
مردم ما معترض عادی‌ن
دست به اسلحه نیستن
برای متن نوشتن برای شاهزاده مخالف نیستم</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/12983" target="_blank">📅 10:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12982">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/12982" target="_blank">📅 10:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12981">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/12981" target="_blank">📅 10:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12980">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-poll">
<h4>📊 نظر شما در مورد فراخان اینترنتی ۱۱:۱۱ دقیقه شب</h4>
<ul>
<li>✓ شدیدأ انتقاد لازمه اپوزیسیون و تمام مشکلات رو همون اول بگو</li>
<li>✓ ایجاد ارتباط و اشاره ریزی به مشکلات برای شروع  (راه خودت)</li>
<li>✓ اصلا هیچ نگو اینم کنسل کن ( من تندرو هستم ‌یا عرزشی )</li>
<li>✓ من اصلا سیاسی نیستم فقط تماشا میکنم ، فل فل دلمم🫑</li>
</ul>
</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/12980" target="_blank">📅 10:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12979">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/12979" target="_blank">📅 10:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12978">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/12978" target="_blank">📅 10:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12977">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89c68ff2f2.mp4?token=QqzHKIH0aqNIvHiH_WObuzwGA2mSPBCBov9RPDFCvpuyoVWARWmUYpOXrW8NOZRkX4Nw9D1slTTFXyAR8a99MtXk6fpwiqo6m_X8vV7ZPjgF7Lx2kj3jNkqP5TbfTw3ZdUGOQrnvSEgBznGyyT1YRJ7BSrtw-vvKYAe2oL-iHw6ehdqHItDCtJvfmAfWxhINJlG3Op8YhSVNG1r29kY43rrrOE_xYRuunijyZrXh41ajkkbVrNl1XqLspYEk_A5tSoRY9zMPz1B93SgT3C7AK-MGjAcAfg_cjZLioP4eG1lb78fpMbEATHPH5r4UFBSdX45eQCQXwER_w6xDPthcbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89c68ff2f2.mp4?token=QqzHKIH0aqNIvHiH_WObuzwGA2mSPBCBov9RPDFCvpuyoVWARWmUYpOXrW8NOZRkX4Nw9D1slTTFXyAR8a99MtXk6fpwiqo6m_X8vV7ZPjgF7Lx2kj3jNkqP5TbfTw3ZdUGOQrnvSEgBznGyyT1YRJ7BSrtw-vvKYAe2oL-iHw6ehdqHItDCtJvfmAfWxhINJlG3Op8YhSVNG1r29kY43rrrOE_xYRuunijyZrXh41ajkkbVrNl1XqLspYEk_A5tSoRY9zMPz1B93SgT3C7AK-MGjAcAfg_cjZLioP4eG1lb78fpMbEATHPH5r4UFBSdX45eQCQXwER_w6xDPthcbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوریا زراعتی مجری اینترنشنال: اپوزیسیون ما رویا فروشی میکنه و وعده هاش دروغ بود
ما به کسی مثل جولانی نیاز داریم نه رهبران فعلی اپوزیسیون
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/12977" target="_blank">📅 10:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12976">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ارتش اسرائیل: کنترل قلعه الشقیف در جنوب لبنان را به دست گرفتیم.
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/12976" target="_blank">📅 09:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12975">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/120549a54c.mp4?token=vhkF4l5KxlGNfZuONtw3MHcXbFWoEkfBc8VVlyAk5IC7iGGZz_DN6XB0x5X5hEKdVjhNtJSZ7blexJq1e-plSrvg0cvjs4WsbtIZC_1Q0mT_78Lkc5DNzStd0I3mZ4MOHcwrMaczmH7GdanAyLIr4XnGULbpeBT7vyntAwW7ToLvFDpzsk2WjGbuuszEU0oEA_pmSZKD3YXgouyaXUwN5AFKahoH4aK60keIpE_lm5CUD0K4EpPmN1e1KQC0Pu0VvI8T-WV-mNkyi6PTtVZemfA4KX8gkPL5g9XoNi-vaBGWiHpgg_1pttdAQ7-2kpYHySWA4B7yhs2JhbJIaxtqMSo-yb4johCmGbMR2ENDvLpF8Q9MjiK_ujdzZr4AsYtOxvpM-r8eGY1HEWYTiZCQIMATrLx2STpLg0_z2QrZ4gYQWLQUsogJ4_OM9RZ78efR0s_75ml0oN1a-AWYvwbvqtse7JRUAivKWknQgcjl9-zBpfGq1jM2QMkTUb-wPxfWlGRbSD_Sgrd6sF8QxA9UgMfOOomItk4U5DeWeWUMzxQRbqhbd55J67s6RQcHbfLv3dR4fkr1UXGokfWrA7_Fxn67YnRqlUMaWONqlOgpp7YYqMxjGF6NqYVhh2Yx69bqSlr_1AO0gdRScid3GYGWx8CYpAAaewMvshi0I0M5SLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/120549a54c.mp4?token=vhkF4l5KxlGNfZuONtw3MHcXbFWoEkfBc8VVlyAk5IC7iGGZz_DN6XB0x5X5hEKdVjhNtJSZ7blexJq1e-plSrvg0cvjs4WsbtIZC_1Q0mT_78Lkc5DNzStd0I3mZ4MOHcwrMaczmH7GdanAyLIr4XnGULbpeBT7vyntAwW7ToLvFDpzsk2WjGbuuszEU0oEA_pmSZKD3YXgouyaXUwN5AFKahoH4aK60keIpE_lm5CUD0K4EpPmN1e1KQC0Pu0VvI8T-WV-mNkyi6PTtVZemfA4KX8gkPL5g9XoNi-vaBGWiHpgg_1pttdAQ7-2kpYHySWA4B7yhs2JhbJIaxtqMSo-yb4johCmGbMR2ENDvLpF8Q9MjiK_ujdzZr4AsYtOxvpM-r8eGY1HEWYTiZCQIMATrLx2STpLg0_z2QrZ4gYQWLQUsogJ4_OM9RZ78efR0s_75ml0oN1a-AWYvwbvqtse7JRUAivKWknQgcjl9-zBpfGq1jM2QMkTUb-wPxfWlGRbSD_Sgrd6sF8QxA9UgMfOOomItk4U5DeWeWUMzxQRbqhbd55J67s6RQcHbfLv3dR4fkr1UXGokfWrA7_Fxn67YnRqlUMaWONqlOgpp7YYqMxjGF6NqYVhh2Yx69bqSlr_1AO0gdRScid3GYGWx8CYpAAaewMvshi0I0M5SLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اصلاً نباید وارد ماجرای ایران می‌شدیم، اما...ما تا حد زیادی کاری به ارتش ایران نداشتیم، چون فکر می‌کنیم ارتش‌شون تا حدی میانه‌رو هست.
اما افراد دیگه‌ای هم دارن که میانه‌رو نیستن؛ اون‌ها رو از بین بردیم.
ببینید، دو تا موضوع وجود داره: اول اینکه تنگه باید فوراً باز باشه و رفت‌وآمد در اون آزاد باشه؛ هیچ عوارض یا هزینه‌ای نباید گرفته بشه.دوم اینکه ایران نباید سلاح هسته‌ای داشته باشه
همین. قضیه به همین سادگیه. بعدش هم ما از اونجا خارج می‌شیم.
ایران الان تو موقعیت خیلی بدیه؛ ولی احتمالاً بزرگ‌ترین سرمایه‌شون همین رسانه‌های فیک‌نیوزه.
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/12975" target="_blank">📅 09:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12974">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ادعای اکسیوس: دو مقام آمریکایی گفتند، ترامپ خواهان این توافق است و انتظار دارد آن را به زودی نهایی کند، اما مصمم است چند نکته را که برای او اهمیت دارند، به‌ویژه در مورد مواد هسته‌ای ایران، تقویت کند
درخواست ترامپ دور جدیدی از رفت‌وآمدها (یا مذاکرات رفت‌وبرگشتی) بین طرفین را آغاز کرده است که ممکن است چند روز به طول بینجامد.
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/12974" target="_blank">📅 09:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12973">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسرائیل هیوم: ایالات متحده به نفتکش‌ها و کشتی‌های حمل گاز مایع قطر اجازه داده است پس از پرداخت پول به ایران، تنگه هرمز را ترک کنند
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/12973" target="_blank">📅 09:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12972">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آکسیوس‌: ترامپ در جلسه اتاق وضعیت روز جمعه درخواست چندین تغییر در پیش‌ نویس توافق آمریکا و ایران کرد که باعث آغاز دور دیگری از مذاکرات شد که ممکن است چند روز طول بکشد
ترامپ خواستار زبان قوی‌ تری در مسائل کلیدی ، به‌ ویژه در مورد مدیریت و انتقال ذخیره اورانیوم غنی‌ شده ایران و همچنین برخی مفاد مربوط به بازگشایی تنگه هرمز است
موافقت‌ نامه فعلی شامل تعهد ایران به عدم دنبال کردن سلاح هسته‌ ای و دوره 60 روزه برای مذاکره درباره محدودیت‌ های هسته‌ ای و رفع تحریم‌ ها است ، اما ترامپ به دنبال شرایط مشخص‌ تری است
ایران هنوز متن نهایی را تأیید نکرده و مقامات آمریکایی انتظار دارند پاسخ تهران ممکن است چند روز طول بکشدrیک مقام ارشد دولت گفت : یک توافق حاصل خواهد شد ، اما خاطرنشان کرد که جدول زمانی نامشخص است و ممکن است از چند روز تا بیش از یک هفته متغیر باشد
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/12972" target="_blank">📅 09:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12971">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فارس : براساس برنامه‌ریزی‌های انجام‌شده، حجاج ایرانی از فرودگاه جده به شش فرودگاه شامل تهران، مشهد، زاهدان، شیراز، گرگان و اصفهان منتقل خواهند شد.
نخستین پرواز بازگشت حجاج روز ۱۱ خردادماه(دوشنبه) از جده به مقصد تهران انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/12971" target="_blank">📅 03:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12970">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عجب سکوت مرگباری …</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/12970" target="_blank">📅 01:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12968">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">@withyashar
JangHub</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/12968" target="_blank">📅 00:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86254cf93.mp4?token=e2c48k4EDbfefq45sFCS8ECSElUbL89_uS7-E3PTZi3F_xmqyUhErB7p6QlfYxAGzgT4WGPqZWDZ_HOGlhKZh_Qtf5hX3kllc04Ir6y3J5y0iFmsxq37iign5tZteAddV4kt3tvnNTQ5VTACA9KjtHY77WQVHJZ8KurUNH7bq1_-XcUh4tX0ybRBca5dpcXn3rZTPvebv-whtfPv9xaISnkjBavf9hSUgW5kFJ0ETk01BLGsqgTpn7ua4xlsaeyxe_cUzkCDm3w28-gNdNww0L_LYh0CErGbbgZ_rFLoMfNsb6q2umpdPDyyVhQbjN9PrGxeyFQunRFaDzJMw-K_gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86254cf93.mp4?token=e2c48k4EDbfefq45sFCS8ECSElUbL89_uS7-E3PTZi3F_xmqyUhErB7p6QlfYxAGzgT4WGPqZWDZ_HOGlhKZh_Qtf5hX3kllc04Ir6y3J5y0iFmsxq37iign5tZteAddV4kt3tvnNTQ5VTACA9KjtHY77WQVHJZ8KurUNH7bq1_-XcUh4tX0ybRBca5dpcXn3rZTPvebv-whtfPv9xaISnkjBavf9hSUgW5kFJ0ETk01BLGsqgTpn7ua4xlsaeyxe_cUzkCDm3w28-gNdNww0L_LYh0CErGbbgZ_rFLoMfNsb6q2umpdPDyyVhQbjN9PrGxeyFQunRFaDzJMw-K_gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای کانیه وست :
کنسرتم در استانبول رکورد ۱۱۸ هزار تماشاگر را ثبت کرده و به بزرگ‌ترین رویداد استادیومیِ بلیت‌فروشی‌شده در تاریخ تبدیل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/12967" target="_blank">📅 00:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12966">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89387a1183.mp4?token=mnS9EF6WIm5kMAq-SHOIcAnSdMY1P6OwGGD1BjZqs7NPOloY5EiLMTezdnCrk1-ZMYee8I7D_tFKaFyBfM9UREimWOgUuFPqbbhkcmwxmUCQ5aSqzol7qwniqJ3-PCmvYD1SLlFA9G0VROnDTl6gc5SKmkxf0kVkJ4RAMPuz2cTfw2WrNt3pVohABsE0FecoKX9BJkHac9FM6o9kZanwmGuA1yejsxVbAvWeKdw2ksFtiJBvzeqgPvzbqmSNqqaElwdQuO5Re3634paUWVrtxGlRklmJTxzE5Rw9tT3BUctK99H_Idq3UsZfC0ICCMY-_-7duFQOlXyB-HOBVJKHlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89387a1183.mp4?token=mnS9EF6WIm5kMAq-SHOIcAnSdMY1P6OwGGD1BjZqs7NPOloY5EiLMTezdnCrk1-ZMYee8I7D_tFKaFyBfM9UREimWOgUuFPqbbhkcmwxmUCQ5aSqzol7qwniqJ3-PCmvYD1SLlFA9G0VROnDTl6gc5SKmkxf0kVkJ4RAMPuz2cTfw2WrNt3pVohABsE0FecoKX9BJkHac9FM6o9kZanwmGuA1yejsxVbAvWeKdw2ksFtiJBvzeqgPvzbqmSNqqaElwdQuO5Re3634paUWVrtxGlRklmJTxzE5Rw9tT3BUctK99H_Idq3UsZfC0ICCMY-_-7duFQOlXyB-HOBVJKHlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی :
۴۰ هزار ایرانی برای تنگه هرمز یا برای یک توافق هسته‌ای کشته نشدن.
ما باید فشار روی رژیم رو ادامه بدیم تا نتونه منابع مالی لازم برای تأمین و پرداخت به نیروهای نیابتی و مزدورهاش رو فراهم کنه.
اما بهترین راه برای اینکه کار به حضور نیروهای خارجی در زمین نکشه اینه که به مردم ایران کمک بشه تا خودشون اون نقش رو بازی کنن
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/12966" target="_blank">📅 00:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12965">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رییس سازمان عقیدتی سیاسی انتظامی:
حکم قاتلان خامنه‌ای رو باید در ملا عام اجرا کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/12965" target="_blank">📅 00:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12964">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6mHoWnfAqBpfyZT8dJI_IyOKtNcvV6n1_VDZh4qvGER554ZtwBkqVi_TJeWOqlyYOonFNwj2tYzRsJeL9qGaHJBkfXOvILE0oIilPBrn6nmLyGPI2owMCEIKrwsWvkgoJkdL8ztZkxVm_adfw7rhJXmMkxA7RMfo5qKbpr49mJwTAqW4jrXp8Ojls8_EmtERdnTlyGlp4w07TxSSysXxjcjKgUHdJyMt4soqf9B04itNoplfc2W6pwN0fjoNnX3ZWKu5rxtNMkRr5Yt6AZNvsZRycj1ObMcyu3wOgfCScWN0C--Ufesrss5PE6vobD8nBwYhUkHF568q7bwq17Cxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث
🤣
:
«یکی باید برای پاپ توضیح بدهد که شهردار شیکاگو کاملاً بی‌فایده است و اینکه ایران نمی‌تواند سلاح هسته‌ای داشته باشد!
رئیس‌جمهور دونالد جی. ترامپ»
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/12964" target="_blank">📅 00:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12963">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31f4e3fc3.mp4?token=LikChH1HoR7qpy9--Uuhv-e80Octzhu3MA6BZCJVzRUD0UqeS6UX1vhC89BFW-Exmn4j6O7pVjqr-SZ00GWNSsWe8arTnjsT8rX7QVRQxR4yXCfN4skdb_4Y-mhe3iAqlQPp4AnIkJ9ViBC5bUKbbn5woJa7pNdEY1iQR3uxv_VY4e6oe7nwh-OoxmO4t8J1piWxjnfwVmlnKh6r0FAYW1xcW8Kl2etJe68nWOEVhqyeES7w0DTxi0FbJZeWwCBgFjf5DPtC0KX7UlRvWSAUcAotvou7yIJhU0Sw1lGXdwXJuO7yPoz4D96N_An-yVLlwGkSDUQA8jGbox3teTtB-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31f4e3fc3.mp4?token=LikChH1HoR7qpy9--Uuhv-e80Octzhu3MA6BZCJVzRUD0UqeS6UX1vhC89BFW-Exmn4j6O7pVjqr-SZ00GWNSsWe8arTnjsT8rX7QVRQxR4yXCfN4skdb_4Y-mhe3iAqlQPp4AnIkJ9ViBC5bUKbbn5woJa7pNdEY1iQR3uxv_VY4e6oe7nwh-OoxmO4t8J1piWxjnfwVmlnKh6r0FAYW1xcW8Kl2etJe68nWOEVhqyeES7w0DTxi0FbJZeWwCBgFjf5DPtC0KX7UlRvWSAUcAotvou7yIJhU0Sw1lGXdwXJuO7yPoz4D96N_An-yVLlwGkSDUQA8jGbox3teTtB-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا:
کشور من از همه طرف ضربه خورده؛ از داخل توسط همین رژیم، و از بیرون هم به خاطر پیامدهای بی‌فکری خودش. با این حال، جمهوری اسلامی هنوز سر جاشه.
بعضی‌ها توی این جمع ممکنه اینو نشونه‌ی قدرت رژیم بدونن. من اینجام بگم که اینطور نیست.
این فقط نشونه‌ی اینه که دنیا هنوز نتیجه‌ی درست از چیزی که داره می‌بینه نگرفته.
پهپاد شاهد فرقی نمی‌کنه کجا باشه؛ چه یه ساختمون مسکونی، چه یه میدان اعتراض تو تهران، چه دفترهای تجاری تو دبی.
پهپادهایی که آسمون شهرهای اوکراین رو تاریک کردن، توی همون کارخانه‌هایی ساخته شدن که زیر نظر همون رژیمی هستن که توی تهران برای شکار معترض‌ها، توی خیابون‌ها پهپادهای نظارتی فرستاد.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/12963" target="_blank">📅 23:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12962">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پست جدید بوگاتی شاه   https://www.instagram.com/reel/DY-ObumIJEK/?igsh=MjQ5cGt6dWo0dGg= کارای اداریش رو انجام بدید
💥</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12962" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12961">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">در پی حملات سنگین حزب‌الله، به بیمارستانی در شهر نهاریا در شمال اسرائیل دستور داده شد تا بیماران را به تأسیسات زیرزمینی منتقل کند.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/12961" target="_blank">📅 23:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12960">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شاهزاده رضا پهلوی:  با جمهوری اسلامی توافق نکنید، بلکه به آن پایان دهید.
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/12960" target="_blank">📅 23:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12959">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید! حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !…</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/12959" target="_blank">📅 22:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12958">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzpX1cuGt6QF6uWQBCJkebiK5fgWpJNzqvVJGQdLXr28e5lV1oGwYP1kTybJ_Aaoht7e0wHXCxNwP7YYlrc4I18S2xCDdtRT3I6qBHdrIsUijq-iqcAygxNY8YRSdslxgDHmDqJpZHT8lSU0Sqjg1GLhe9LnNrv2sFebqaODnUvpwyCYHQ9XNbGVm3nGt20kCKOeloresopHqi3IgH867dgzjIhtCCJmqen9K9rkkb8gbGr9rY3ECKXkzDX-AeZjOvDVNKbTBKW1tSZyCH8m_No_Y-d3YKkvmcsEilWYTlCCsMoOO1qyDw1VzYwnu41UalOaC92MOuvS_c7tbTz-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ادعای آمریکا در جریان این جنگ، دست‌کم ۱۶۰ شناور دریایی ایران را غرق کرده است. هر یک از این شناورها می‌تواند منبعی بالقوه برای آلودگی باشد. وقوع یک نشت جدی در تنگه، مهار آن را بسیار دشوارتر از حالت معمول خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/12958" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12957">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12957" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12956">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKiasha</strong></div>
<div class="tg-text">یاشار امشب ردبول رومی خوری؟</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/12956" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12955">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سنتکام اعلام کرد کشتی تجاری Lian Star که از یک بندر ایران خارج شده بود پس از 20 هشدار توقف و عدم توجه آن توسط یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت و در دریای عمان توقیف شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/12955" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12954">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پست جدید بوگاتی شاه
https://www.instagram.com/reel/DY-ObumIJEK/?igsh=MjQ5cGt6dWo0dGg=
کارای اداریش رو انجام بدید
💥</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12954" target="_blank">📅 21:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صداوسیما جزئیات غیررسمی از یادداشت تفاهم (ایران و آمریکا) را منتشر کرد
‌
یکی از مهمترین محورهای توافق (ایران و آمریکا) بازتعریف قواعد عبور و مرور در تنگه هرمز است
‌ایران مرجع انحصاری تشخیص ماهیت شناورهای عبوری است
هر شناوری که محموله آن تهدید آمیز تلقی شود یا بهره‌بردار نهایی آن در خصومت با ایران باشد به عنوان کشتی تجاری شناخته نمی‌شود و اجازه عبور از مسیرهای تعریف شده را ندارد
تعیین مسیر حرکت و تعیین هزینه خدمات ناوبری در حوزه تصمیم‌گیری ایران دیده شده
‌
هر شناور موظف است اطلاعاتش را در اختیار مرکز مرتبط با نیروی دریایی قرار دهد و فرم‌هایی شامل جزئیات محموله مالکیت و مقصد را تکمیل کند
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/12952" target="_blank">📅 21:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الجزیره: ترامپ برای جلوگیری از جنگ با ایران پیش از جام جهانی بسیار مصمم است
او همچنان برای دستیابی به یک توافق موقت با تهران تحت فشار است، اما پیشرفت فوری بعید به نظر می‌رسد
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/12951" target="_blank">📅 21:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شبکه ۱۴ اسرائیل : نتانیاهو، قراره به‌زودی یه جلسه امنیتی برگزار کنه تا درباره نحوه پاسخ به شدت گرفتن حملات حزب‌الله تصمیم بگیره
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/12950" target="_blank">📅 20:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/12949" target="_blank">📅 20:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/12948" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌊</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/12947" target="_blank">📅 20:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromhydrus</strong></div>
<div class="tg-text">درود میشه یکم ویس بدی دلمون گرفت :)
❤️</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/12946" target="_blank">📅 20:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrggfoTJWwFjBRWQOFVOd2dtybeXmLkX6coa10PKQxqxPoOS-nnv24oVOI06r81XW_RzFztJRyKk6fImzSGD6UDHzNQJhRcZguccubHiNvYxr7101ibnIHOLgg74Gxgs8bb3553L5JGs2c8FQ2mG90T1-nko1HwSwOjICN8_GPYovIfM_JHvDqckLK6PdxYowDOjtSO8lHt7278ZaKWx0JPBG9Qm-A3VW8YvR7B-DdPZfgbv9pwwYYEPEdBChyYxVkzZlSPwNnziYDb3RkeGxn7KuRsOebFYgeDwTjVn-eSLtVpm3tI5MZvn62LK_eXtTD1KOiDOaCY6ToHaoLzLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: پنج مرحله سندروم ترامپ هراسی
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/12945" target="_blank">📅 20:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نماینده سیستان و بلوچستان در مجلس :
برخی از مناطق زاهدان ۲۴ تا ۴۸ ساعت آب ندارند. ادامه بحران آب، استان را با چالش‌های امنیتی و اجتماعی روبه‌رو می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/12944" target="_blank">📅 20:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سخنگوی فدراسیون فوتبال:
روزبه چشمی به‌دلیل مصدومیت جام جهانی را از دست داد
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/12943" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12942">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تلگراف: دو ژنرال قدرتمند، احمد وحیدی و محمد جعفری، با هم متحد شدن تا قالیباف رو از قدرت برکنار کنن.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/12942" target="_blank">📅 19:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12941">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، گفت مردم ایران برای ساختن آینده کشور خود آماده‌اند و از جهان نمی‌خواهند آینده ایران را برای آنان رقم بزند، بلکه خواستار آن هستند که جامعه جهانی در کنار ملت ایران بایستد.
او در بخش دیگری از سخنانش، با اشاره به خروج اجباری خود از ایران در ۱۰ سالگی، گفت که با وجود گذشت ۴۷ سال، هرگز امید خود را به آزادی ایران از دست نداده و همواره صدای مردمی بوده است که امکان بیان خواسته‌هایشان را نداشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/12941" target="_blank">📅 19:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12940">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654bf3851d.mp4?token=Hj5j_wE4B42GqG3CXZDJlo9L-ajKNW4cpXfAQVFDDrfnoHRLLYqk2E3RIkss3m6P2c6MFc0eYH8cktmmvrcxqdQfGn__3gsbegzlPhJ824GJLG7ZsANfDlqKCxJbT6YuTNUPnF-O1WPSRGW1u8u9DXDof6KS54pdQ5oWSL2rPvvINB7miud4SxWFV_VhHGe5BSVWDyiDe9AVyGBoZ66WUoCg8bsFk_F6Ec0AQ5fHTBCqT-9DZKiLj1J9J2n4uipEzOVimCY6sumI-75Mdfo9YUXbaLhXywSCbl0YIXKJnGRIR4v_rTCTjKbZqGRD4vNrkFDiXl9xBeS-5FowLJIqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654bf3851d.mp4?token=Hj5j_wE4B42GqG3CXZDJlo9L-ajKNW4cpXfAQVFDDrfnoHRLLYqk2E3RIkss3m6P2c6MFc0eYH8cktmmvrcxqdQfGn__3gsbegzlPhJ824GJLG7ZsANfDlqKCxJbT6YuTNUPnF-O1WPSRGW1u8u9DXDof6KS54pdQ5oWSL2rPvvINB7miud4SxWFV_VhHGe5BSVWDyiDe9AVyGBoZ66WUoCg8bsFk_F6Ec0AQ5fHTBCqT-9DZKiLj1J9J2n4uipEzOVimCY6sumI-75Mdfo9YUXbaLhXywSCbl0YIXKJnGRIR4v_rTCTjKbZqGRD4vNrkFDiXl9xBeS-5FowLJIqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مک‌اننی از فاکس:
بلومبرگ گزارش داده است که حملات موشکی ایرانی چند آمریکایی را در یک پایگاه هوایی کویتی زخمی کرده‌اند. فکر می‌کنید اوضاع در چه وضعیتی است؟
مایک جانسون، سخنگو:
دیشب با رئیس‌جمهور ترامپ صحبت کردم. او کاملاً در جریان است. فکر می‌کنم رهبری جدید ایرانی‌ها می‌خواهد این درگیری را به پایان برساند.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/12940" target="_blank">📅 18:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12939">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy0rODX9aKJjSkCHub7CD8w7Hxbye56JqQGZVzvfMAxXZUtty8yo3rvzyjVkjRTN_urOk3TRBFXldsrbrSR39insIbuwcl4RE1JRTHH6cbHUmvHpgK6ucODwy1GUlBhJTyEO_WK0Kzqe3w6_6jt4hZwtVa34hfyhhiP9bPbqequGoB4w3wA9R_SvSbCEkbKvgD246__iKGW-N3itGf1EfM2KYjFc4h2XNjY6PeBQrXrNnC21iD-fLdkuRKGqNt1mEKM10Vi7WRT3HE_7t3TbNC-dGUS2SWQq_rb-Qm4yTbID9qHTcZl0HKxjcws6lGjFycrtpILg0n1vpWhadaMCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می‌رسد که ناو آبی/خاکی یو‌اس‌اس باکسر (lhd-4) قرار نیست در حوزه مسئولیت سنت‌کام  مستقر شود. ناو آبی‌خاکی کلاس واسپ نیز امروز از بندر سِمبانوان در سنگاپور حرکت کرد؛ اگرچه اکنون به سمت شرق در حرکت است.
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/12939" target="_blank">📅 17:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12938">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست «امنیت دریای سیاه» در اودسا در جنوب اوکراین، گفت که دنیای آزاد هنوز متوجه ماهیت جمهوری اسلامی نشده است.
شاهزاده رضا پهلوی درباره تلاش برای توافق با جمهوری اسلامی با امید به ایجاد ثبات، گفت که یک سگ وحشی در نهایت دست شما را گاز می‌گیرد.
او افزود: «پهپادهایی که اوکراین را هدف قرار می‌دهد از سوی جمهوری اسلامی تهیه شده و با همان پهپادها مردم معترض خود را در خیابان تعقیب می‌کند تا تک‌تیراندازها آن‌ها را هدف قرار دهند.»
شاهزاده رضا پهلوی گفت که تهران و مسکو معماران مشترک هرج‌ومرج در جهان هستند.
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/12938" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
