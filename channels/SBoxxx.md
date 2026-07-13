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
<img src="https://cdn4.telesco.pe/file/aYLsSkJqCX775jxd-LIct-m1OcXMFrAqZBTsImVIA2OqVLCNAzdSdwDdrG9mWZgxnMl16j-0lVLFULfh_tVlDbnUKGg_b2n71ktSYk0zaBDeCq2HHfdwVVDbss82rWzFH6dclEWCvPgr8wbd0Omlz9OUF0tgjMsOayWJ43bkhp68d_CSTlBCgYFgXcfjbKF6JOPXPXHcboN-WKlEU7WkrBKvSdLUWkhgkqL6Ml2EolbZFE-ZfKSMzDC47LutCt1H0UW7ZaPzl7PT2dapnDdU8gaxvV_c3fBFGFL8nALSNAcRz9kmlEz0FXFQvjb8SpqkoGx9Z-P4HeG7RqjrVyF55A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 17:39:15</div>
<hr>

<div class="tg-post" id="msg-18675">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ستاد مرکزی خاتم‌الانبیای ایران:
ما تحت هیچ شرایطی اجازه نخواهیم داد که ایالات متحده در مدیریت تنگه هرمز دخالت کند؛ نه اکنون و نه هرگز.</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SBoxxx/18675" target="_blank">📅 16:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18674">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ در مورد ایران:
خمینی رفته است. پسر او ۹۰٪ رفته است.</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SBoxxx/18674" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18673">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ:
ما دیشب ضربه خیلی سختی به آن‌ها زدیم. هر بار که آن‌ها یک پهپاد می‌فرستند، ما ضربه خیلی سختی به آن‌ها می‌زنیم. اما ما یک توافق داشتیم؛ چیزی که هیچ‌کس نمی‌داند این است که ما یک توافق داشتیم، کار تمام شده بود، و بعد آن‌ها توافق را شکستند. آن‌ها همیشه توافق را می‌شکنند. ما تا به حال ۱۰ بار با این افراد توافق داشته‌ایم. بنابراین ما فقط قرار است ضربه خیلی سختی به آن‌ها بزنیم. و ما این تنگه را حفظ خواهیم کرد و احتمالاً آن را اداره می‌کنیم، ما تبدیل به "نگهبان تنگه" می‌شویم؛ شاید اسمش را بگذاریم "فرشته نگهبان تنگه". و ما باید هزینه‌ای که برای این کار می‌کنیم را پس بگیریم. وقتی این کار را انجام دهیم، پولمان را پس خواهیم گرفت چون کشورهای دیگری که طرف ما هستند بسیار ثروتمندند. و از ما انتظار نمی‌رود که این کار را مجانی انجام دهیم، برخلاف کاری که سال‌ها انجام دادیم. می‌دانید، ما برای ۵۰ سال یا بیشتر از این تنگه محافظت کردیم و هیچ‌وقت پولی بابت آن دریافت نکردیم. آن‌ها همه پول‌ها را به دست آوردند و ایالات متحده فقط... می‌دانید، هیچ... شگفت‌انگیز است. ما هیچ‌وقت سودی نبردیم. ما مجانی از آن محافظت کردیم. اما حالا که می‌خواهیم از آن محافظت کنیم، قرار است بابت محافظت از آن پول بگیریم، پول زیادی هم بگیریم. ما فقط می‌خواهیم هزینه‌ای که برای انجام تمام این کارها و به خطر انداختن نیروهایمان صرف می‌کنیم، جبران شود. اما ما در واقع مردم را در خطر قرار نمی‌دهیم، ما واقعاً داریم نجاتشان می‌دهیم.</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/18673" target="_blank">📅 16:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18672">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ :
ما قصد داریم‌ حملات جدی تری علیه ایران انجام دهیم</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/18672" target="_blank">📅 16:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18671">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ:  ۵.۲٪ از روسای جمهور کشته می‌شوند و  به ۸.۵٪ با گلوله شلیک می شود.  رئیس جمهور بودن خطرناک است.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/18671" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18670">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/18670" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18669">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
ما تنگه هزمز را حفظ خواهیم کرد. احتمالاً آن را اداره خواهیم کرد.
ما نگهبان تنگه خواهیم شد و وقتی این کار را انجام دهیم، برای آن جبران خسارت خواهیم شد.
ما به مدت ۵۰ سال از تنگه محافظت کردیم و هرگز بابت آن پولی دریافت نکردیم. ما بیهوده از آن محافظت کردیم، اما اکنون پول درخواهیم آورد.</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/18669" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18668">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">در‌ این صوتی وضعیت خر تو خر یمن را توضیح داده بودم .</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/18668" target="_blank">📅 15:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18667">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/18667" target="_blank">📅 15:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18666">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/18666" target="_blank">📅 15:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18665">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/18665" target="_blank">📅 15:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18664">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">به نظر می رسد زمان حمله نیروهای مورد حمایت سعودی یا امارات به حوثی ها نزدیک است.</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/18664" target="_blank">📅 14:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18663">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :    تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/18663" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18662">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :
تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/18662" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18661">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/18661" target="_blank">📅 13:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18660">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.   زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.  اکثر این پناهگاه‌ها…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/18660" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18659">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.   زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.  اکثر این پناهگاه‌ها…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/18659" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18658">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvcIyyd2Q__rRdJSHnF3aZNtDfOnaCZiAtPk2E3bq0ciVcHjbYyJSMQwUwXMVbZ7ON9r0pnlkAf9SVIIjJKAeORcu_ChP_5TaAi7XyTKMp7bpo0vHtfgZ6a5ON1Y5RbvEzS-OIwRKztBPz1mOk-f8UyJsgXUzWOxUThzv2jS0GL1t68D-j0Q660SJlIXWFwqk9LmZfW0LGrhk_MVNPxmhlIOkvosXeUf14o5ji3y4wTiphF-1MJYk_Xota-Ylk2e3gKRHMTRCKnU-f9KGUfEsyRyBqIdT4ahslOJ6BlsOmOFbJ-tCQUUNeErb51VptzslQsHojdzynn1YGLq4RHHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.
زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.
اکثر این پناهگاه‌ها برای اهداف روزمره مانند سالن‌های ورزشی، زمین‌های بازی، استخرهای شنا و حتی فضاهای تمرین برای گروه‌های موسیقی راک مورد استفاده قرار می‌گیرند، اما می‌توانند به سرعت به پناهگاه‌های اضطراری تبدیل شوند.
منبع: The Times</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/18658" target="_blank">📅 12:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18656">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732e84f6ce.mp4?token=ghouzx5HHj4Tzdp1WtZUzIE2kAG_fgUvzWuHnVenq1gvS4JgHdoYUfvSh16JyntBd86r4AvhP7KDNPAsZqe30QZzvEjqrQbOGq-97Q8z3DpXGBXorZO_nigBslbTpW65R_XzyAJ-UwsqRY_x3bXN3aAEFi3R94w4MPB2-BuF1wqgKkF7DOGI3vEFgNOvIocSzsIBznCB2eWcBNd961K9r5-X32rmM632IBtfLKw4x4-j1xrLTtC_2wQ5UGWbgPP8MIk8_bXQf_6Lb3s3YlkBWvBDAQ46zyZsvcSwXgWq5m1AtldDSkOTyWLYdcvJ8xZ_xZql-eF2Sa3yIuk9PePOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732e84f6ce.mp4?token=ghouzx5HHj4Tzdp1WtZUzIE2kAG_fgUvzWuHnVenq1gvS4JgHdoYUfvSh16JyntBd86r4AvhP7KDNPAsZqe30QZzvEjqrQbOGq-97Q8z3DpXGBXorZO_nigBslbTpW65R_XzyAJ-UwsqRY_x3bXN3aAEFi3R94w4MPB2-BuF1wqgKkF7DOGI3vEFgNOvIocSzsIBznCB2eWcBNd961K9r5-X32rmM632IBtfLKw4x4-j1xrLTtC_2wQ5UGWbgPP8MIk8_bXQf_6Lb3s3YlkBWvBDAQ46zyZsvcSwXgWq5m1AtldDSkOTyWLYdcvJ8xZ_xZql-eF2Sa3yIuk9PePOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قاسمیان: شما نباید بگید آآآمریکاااا بی دوووووو ، باید بگید آمریکا بی دو. یعنی باید با تحقیر بگی
✍🏻
exxon
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/18656" target="_blank">📅 12:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18655">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/18655" target="_blank">📅 12:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18654">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/18654" target="_blank">📅 12:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18653">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5052358e.mp4?token=u_rbwdTj-lUOM8nl4-ckzIeWGaZT99gzkIXQkABpp_Tfi833--DXxXuSIg5SNKwwFs7Zd9l-3X7bLrnrVYsIjToMeRHgXSlAzhyOH8QULlTu_O1W4N_WmYDR58wIWeG6PWGV7af17kweAtSFwgFDe0E38OYC5irjjd4lx9YbYcfePTw2-X3QgNpDbQEMNJBLxgIJg2Xk7EPMZkKDmiB6ZXMISIBb4e4kTasE8wG7AnJyBtBzslczRoJbx5eW1k_O-KsWTKOypNwgMkof1PFt9Gdx7vQRUMaNoolq7MgEK-SNBTcOTWt8HpSlgRxDVK19u1aToJzhFxdSD_wE30R1GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5052358e.mp4?token=u_rbwdTj-lUOM8nl4-ckzIeWGaZT99gzkIXQkABpp_Tfi833--DXxXuSIg5SNKwwFs7Zd9l-3X7bLrnrVYsIjToMeRHgXSlAzhyOH8QULlTu_O1W4N_WmYDR58wIWeG6PWGV7af17kweAtSFwgFDe0E38OYC5irjjd4lx9YbYcfePTw2-X3QgNpDbQEMNJBLxgIJg2Xk7EPMZkKDmiB6ZXMISIBb4e4kTasE8wG7AnJyBtBzslczRoJbx5eW1k_O-KsWTKOypNwgMkof1PFt9Gdx7vQRUMaNoolq7MgEK-SNBTcOTWt8HpSlgRxDVK19u1aToJzhFxdSD_wE30R1GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/18653" target="_blank">📅 12:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18652">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
حسین شریعتمداری، مدیرمسوول و نماینده ولی‌فقیه در روزنامه کیهان، در یادداشتی، بابت مرگ لیندسی گراهام، به عزراییل، گلایه کرده که چرا:   «پیشدستی کردید و قبل از ما حسابش را رسیدید... از خدا اجازه می‌گرفتید و کمی صبر می‌کردید تا این عنصر پلید را با دست خود راهی…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/18652" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayLIkfIx1ooRdBC4H_KvkjQa2MZGRocfeveaDyXp2isMHSQMuBiov8cOP5JNuyLA7-gn2g3VzZaQz9RlUbfOngtTgViPg6z8VoNg882iaLRuzn-QgoSDehpjHsWUdACxaugL9GQEaeDVwc3zwKoJuqGCcGEBZ3aaWmjtcPXlZBs2gQqkdQtEXX3e-qW0D3IvjoVHlvUyGtiDJkDriLKTz5cVJGEZdnPM9uxH_3o3dvQHFcFYyDE8IrLACO-YLE84J57MJ0erAGT-9NYV6WFbGm3YLpS5NukWukpFm8Vc9vNTym0tr4ZFtumxIvwybuNzTmm1FVbYflIIiP28m73W-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حسین شریعتمداری، مدیرمسوول و نماینده ولی‌فقیه در روزنامه کیهان، در یادداشتی، بابت مرگ لیندسی گراهام، به عزراییل، گلایه کرده که چرا:
«پیشدستی کردید و قبل از ما حسابش را رسیدید... از خدا اجازه می‌گرفتید و کمی صبر می‌کردید تا این عنصر پلید را با دست خود راهی جهنم کنیم.»</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/18651" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18650">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9aEH-peW-N-PtvNRav7sQUDO39cso2QuvMf8Z3Mt8fysfN2n0FsO2Dsr6tozV9Y6BfjkZdBlQYa5_5MY3vw9mOlPxNNVg6vTb6KxgnsHKPXyptgkFviNdgnXnwcuZMnZfkbHabPus0SWATLcikpercr77-x1bMu4zbroundlD-iA7lGTKZox622qdOX5_jXuWIwfxipJw9P1PvRmBl-x9qBBk-53WOcjHMSXkH1KvE9zEBcA0sQmImSLYQgS54jTtgMlr2YYEqUykfUsIHXHyIvzPS7-nENbXphgIp0ZTjnmr9SmA9GTs5QXOnSl10ZmJ2k0LIxhc_rMROTNBymvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در این لحظه کاهش اساسی یافته و کاهش تنش ها را پیش بینی می کند.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/18650" target="_blank">📅 11:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18649">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سومین پرواز از سوی دولت روسیه از مسکو به سمت ایران به پرواز در حال انجام است.  هواپیماهای توپولوف ۱۳۴ معمولاً برای انتقال افراد مهم و مقامات رده‌بالا استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/18649" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران در مورد فوت لیندسی گراهام:
عزرائیل عدالت را جاری می‌کند.
برای چنین فردی که میراث زندگی‌اش سرشار از کینه و حمایت از تجاوز بود، چیزی جز یک سابقه تاریک در ذهن مردم باقی نخواهد ماند.
مرگ این سناتور پرخاشگر و با دهان گزنده، قطعاً قلب هیچ فرد آزاده‌ای را آزرده نخواهد کرد.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18648" target="_blank">📅 11:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18647">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به نظر می رسد نیروهای آمریکایی دیشب از مهمات ویژه برای تخریب تونل‌ها استفاده کردند تا یک پایگاه موشکی زیرزمینی را در نزدیکی شهر دزفول، در پایگاه چهارم شکاری نیروی هوایی  مورد حمله قرار دهند.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18647" target="_blank">📅 11:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18646">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سنتکام:
موج دیگری از حملات را علیه ایران به پایان رساندیم
تامپا، فلوریدا —
فرماندهی مرکزی ایالات متحده (CENTCOM) در ۱۲ ژوئیه موج جدیدی از حملات تهاجمی علیه ایران را به پایان رساند و با استفاده از مهمات دقیق، ده‌ها هدف در چندین مکان را هدف قرار داد تا توانایی ایران در ادامه حمله به کشتیرانی بین‌المللی که از تنگه هرمز عبور می‌کند را تضعیف کند.
نیروهای CENTCOM به سیستم‌های دفاع هوایی نظامی ایران، سایت‌های راداری ساحلی، توان موشکی و پهپادی و قایق‌های کوچک حمله کردند و برای اولین بار از هواپیماهای جنگنده ایالات متحده، کشتی‌های دریایی، پهپادهای حمله هوایی یک‌طرفه و پهپادهای حمله دریایی یک‌طرفه استفاده کردند.
تنگه هرمز یک مسیر دریایی حیاتی برای تجارت جهانی است. ایران کنترل آن را در دست ندارد.
نیروهای ایالات متحده برای اطمینان از اینکه آزگان دریانوردی برای کشتیرانی تجاری باقی می‌ماند، حتی با وجود تهاجم بی‌دلیل، آزار و اذیت، تهدیدات و اعلامیه‌های خودسرانه مداوم ایران، آماده و مهیا شده‌اند.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/18646" target="_blank">📅 10:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18645">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آغاز خاموشی‌های برنامه ریزی شده در کشور!   مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:   این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/18645" target="_blank">📅 10:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18644">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آغاز خاموشی‌های برنامه ریزی شده در کشور
!
مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:
این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/18644" target="_blank">📅 10:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18643">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3qa8sbUT3oN76nmpYpv-9gZbB8CcTDPoEk0-RCuK-I1ci5U25eS07vKFl93CkOAswjfYTlAltyR2bPYU3k3NHiEG3e-XlYHePLgatQjOX7Nbg0zRQOFXsnJvNCJcSysmZT0SsAajOXV-OHdJb0-oSrmX1R8wm2oZ_yVq5P2C8vnj159eEZbZig1C2GU-wr1dSIxwrBjHln8-BpsoZ1RXzp_dY3LcCaKq6-9Jl-W7eVq0m3TqFbLcMtvF9Vg7U-76YyTyeU2c0z-eTaDhu_cfJNDwunXguO5pd0kDAgd3A7Qj8zYn4mNgGZ0f3IheZrOgfidLQh2fZLpwTgPyGAbeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در این لحظه کاهش اساسی یافته و کاهش تنش ها را پیش بینی می کند.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18643" target="_blank">📅 09:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18642">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 6
دوشنبه 13 جولای 2026</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/18642" target="_blank">📅 09:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18641">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18641" target="_blank">📅 09:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18640">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18640" target="_blank">📅 09:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18639">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frjksNYnjzZtJCjGXP_JEw_VzsWLcmdC8OnG__8GLoouOLyrgegahpTKxwE9WvaC-JMx103zn-tvnZ86h2J7Yw26OwaLnVbh-fztljar3QUEtNfqsTrFtsNdSD27VYf3b0B0LI4wcb2rwO89j96sNU4T2j2OvE0ea2fGJNQ3if-K_FTjvQohR9MlyPTuzgSuYJmmZZG80KCZp9jPvhmUlx8wHKLhf9abijxLdHPk17vp00l22kFfbEFkOffWmY_KMSpZrUHTPdlL1nvuT2wTqSTT9wMn_eiTMMdNKzw15GgRTznSpiobfFl2aoRpc6qkVme-2kCuiGgvueZT_iyYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گستره جغرافیایی حملات دیشب آمریکایی ها</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18639" target="_blank">📅 08:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18638">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">— سپاه پاسداران:
«در مرحله چهارم عملیات «چشم در برابر چشم»، نیروهای زمینی قهرمان سپاه پاسداران پایگاه موشکی زمینی به زمینی ارتش ایالات متحده در کویت را هدف قرار دادند و دو پرتابگر موشکی هیمارس و انبارهای مهمات را آتش زده و به طور کامل نابود کردند».</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18638" target="_blank">📅 08:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18637">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده اعلام کرد که برای اولین بار از شهپادهای دریایی انتحاری  برای هدف‌گیری دارایی‌های ایران استفاده شده است</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18637" target="_blank">📅 08:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18636">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سومین پرواز از سوی دولت روسیه از مسکو به سمت ایران به پرواز در حال انجام است.
هواپیماهای توپولوف ۱۳۴ معمولاً برای انتقال افراد مهم و مقامات رده‌بالا استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18636" target="_blank">📅 08:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18635">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آمریکایی ها دارند با هیمارس و از کویت، شهرهای خوزستان را شخم می زنند!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18635" target="_blank">📅 02:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18634">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMqw2isu9uvoblZFWPiQzvyUFN3fllO-f-UHoHs94ED8XwS7dcED7EXBuOQ8cj_4EHnBWHEeR-7wCa9chWn5KuIUMnezdLHiTd1osR1Y7kFKDvPjMw05-WkHw2BAk--qNaIpJC03lQaxNPWRSrGA7TlRebyzxcgQQLEUSGVirsz7RVbyZIFLlj7AnEZHm94nOGX9MUdlIotOZJ31vAMAHClAXMoydJ7kvcx6y_g1UKfhqWr7Whr-KjU1o90U3tlc8tewmJKwc_v7nOnNWN7PUHZgb6SEo4fqcI-1Nb9Ci1nHVph7M82XtXH2gxdUdju2UnOopvA1OmvF0JU4h-7J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربها وقتی میفهمند دوباره ما برای آزادی قدس داریم خودشان را میزنیم!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18634" target="_blank">📅 02:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18633">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  هشدار فوری به تمامی شهروندان و ساکنان کویت، بحرین و امارات متحده عربی:  با توجه به تبعیت حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای شلیک موشک‌های زمین‌به‌زمین به‌سوی ایران، از شما می‌خواهیم نهایت احتیاط را…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18633" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18632">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
هشدار فوری به تمامی شهروندان و ساکنان کویت، بحرین و امارات متحده عربی:
با توجه به تبعیت حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای شلیک موشک‌های زمین‌به‌زمین به‌سوی ایران، از شما می‌خواهیم نهایت احتیاط را به خرج دهید.
در صورتی که هرگونه سامانه یا سکوی پرتاب موشکی در نزدیکی مناطق مسکونی خود مشاهده کردید، لطفاً در اسرع وقت آن منطقه را ترک کنید. همچنین از پایگاه‌ها و تأسیسات نظامی آمریکا فاصله بگیرید و از نزدیک شدن یا عبور از اطراف آن‌ها خودداری کنید.
از تمامی شهروندان و ساکنان درخواست می‌شود این مناطق را فوراً تخلیه کرده و بدون هیچ‌گونه تأخیر به مکانی امن و با فاصله مناسب منتقل شوند تا جان و امنیت خود را حفظ کنند. ما پیش‌تر بارها و به‌طور صریح به حاکمان شما درباره خطرات ادامه این مسیر و به بازی گرفتن سرنوشت مردمشان هشدار داده بودیم.
با این حال، آنان تصمیم گرفتند به مسیر تبعیت کورکورانه ادامه دهند و تصمیماتی را اجرا کنند که نه بازتاب‌دهنده اراده مردمشان، بلکه تحمیل‌شده از خارج از مرزهایشان و در غیاب هرگونه حاکمیت واقعی است. بنابراین، مسئولیت کامل تمامی پیامدهایی که در نتیجه این مسیر به وجود خواهد آمد، بر عهده آنان خواهد بود.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18632" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18631">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سنتکام:
ساعت ۵ بعدازظهر به وقت شرقی امروز، نیروهای فرماندهی مرکزی ایالات متحده آغاز به انجام حملات بیشتری علیه ایران کردند تا توانایی آن‌ها برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که به صورت آزادانه از تنگه هرمز عبور می‌کنند را تضعیف کنند. فرمانده کل قوا دستور این حملات را برای پاسخگویی نیروهای ایرانی صادر کرده است.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18631" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18630">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.  همین</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18630" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18629">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجاراتی متعدد در نزدیکی شهر سیریک در ایران شنیده شد: تلویزیون دولتی.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18629" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18628">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bc32908f.mp4?token=GN4m7Vm8AkIQ7uil_-jGh90QyEV6yenjUbRNAu81_x6poMa74bKm6khYHdTvjnOZUIjAlu5pSPokdsCk4GP11yUe5uwBbue2mJIkFhKXL11L3IPHmngzyNuy3xMsXEpZZsmQ00wNBHOgr1p5Un1CM8xrTLVAH-zZ8GbDAMbq0LbmtMZvitQ7Htx42ZYNvnV9gDgRdEnN-bVxbFZ9itnhbR3HNTqnImnfxrR5T2raK203qevIc_CNjoP9zmgwJ0R0_jlj3P86-X2upXruK0iQj58pNno6zQX5FNN7fI2Kb-LFQ3egMIH1l6SaSPS-l0zGkyc5loCms6FdyQ1sLngy_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bc32908f.mp4?token=GN4m7Vm8AkIQ7uil_-jGh90QyEV6yenjUbRNAu81_x6poMa74bKm6khYHdTvjnOZUIjAlu5pSPokdsCk4GP11yUe5uwBbue2mJIkFhKXL11L3IPHmngzyNuy3xMsXEpZZsmQ00wNBHOgr1p5Un1CM8xrTLVAH-zZ8GbDAMbq0LbmtMZvitQ7Htx42ZYNvnV9gDgRdEnN-bVxbFZ9itnhbR3HNTqnImnfxrR5T2raK203qevIc_CNjoP9zmgwJ0R0_jlj3P86-X2upXruK0iQj58pNno6zQX5FNN7fI2Kb-LFQ3egMIH1l6SaSPS-l0zGkyc5loCms6FdyQ1sLngy_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا این  هواداران نروژی و انگلیسی را دارم میبینم یک جوری فوتبال میبینند انگار هیچ چالش و مشکل دیگری در زندگی شان نیست!</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/18628" target="_blank">📅 00:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18627">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سنتکام:
🚫
ادعا: تبلیغات ایران امروز ادعا کرد که سه نظامی آمریکایی در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✅
واقعیت: هیچ گزارشی مبنی بر کشته یا مجروح شدن نظامیان آمریکایی در این منطقه وجود ندارد. تمام پرسنل در وضعیت سلامتی هستند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18627" target="_blank">📅 00:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18626">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">منابع عربی از کشته و زخمی شدن چندین سرباز امریکایی در پی حملات سپاه به مواضع آمریکا در کویت خبر  می دهند!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18626" target="_blank">📅 00:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18625">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این هم یکی دیگر!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18625" target="_blank">📅 23:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18624">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پست جدید ترامپ !</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18624" target="_blank">📅 23:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18623">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_FkUujY9QTfrTUpcwxEC-9zBhDwlUL_GYacqQKasxRp8LURMyh8OjYdb_LLFpXncOr_83GT4dtIccv6xZwQtyRVIUzWHnTMbu3djdlpbMS6DJ8WhbMOJ0o2dNIPcafFia5S9ub-nHc4bZEN4so1DrArt6x9eV3vtA3q3YalxGBi_vqDm0oNEtcN2mieqY2SlCAU0Zx_q9gHTjYwIsquuia3-5I13Ax6AMZ0SQxC_hEm9eNoA1eG-8n9-bUUdyiaL2tKmcv9waIl52upWo7NKegRJVjucuGDdt-Ud62TjVd9ywQxeA62GLZZZQdbZ4FAnCaFW6aFZwDiBbCdyGfOwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ !</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18623" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18622">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TesCO57q7__Cj76KRByiBZjtGmuoFyEgyYhqIff-wPfb8UHXlyTl3ZBJgi5mCTIBTk9iKSwNty4r474YkSP3jpMSozxaKWC-WqC8TiHwV2b6RBW9k71DUxrJHQK4Kx5GojSbN2pj9sgJLQpwZk3GW1U1pY1gnFVxwVyiBPFPfzJdT14hJSl0lKBl1Qbj1Lc_rsRziAHKKFrMiVfzD0cf29eFm4h51MDeVsQ6Mg0g6bSQAg8QFYCOHjUMU108T2XeStaeHT2mcupkNvR_XDwaq4tctTyQDR0sqsXRQYNMTTplE99IiVci9fa8U_p0Qa3FBRDY2Xs1sonAiYu3zCF9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.  ارزیابی‌های فعلی حاکی از آن…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18622" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18621">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منظورشان همین هفت هشت هواپیماست.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18621" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18620">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjZD8oMDKAunFdBBqAYRumxXfdeGD2jcYvsyNWLMP3qqe7b8r5DlsV2yTpzqpwhwde97SnVyMD9bm7YAiFpcXN0sknXdmiyejEJGw75_y5Mor9OM7SJ7GvRk6johrSLR9LDIreu1hUBF8aLkmyEW5OapMflN9Tg8eym1h_9Uwr12ePqjYIjlDyhDSgAS_Aj54shf6Cqh8SGpIoL8Ra6FSFokWTbQFESRTo7e2fq5tgQ5a4IEojzLqfRryETCWnqCAz57u51shQRaB_7g5T91bwl2ysXSaaPY2tcVBCnW0wCjIwAhEa99I0wDovfxTrCXjPhY0kL_W4URe-SkM-CCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده های ارتش جمهوری اسلامی ایران بر فراز حریم هوایی مناطق مرزی غرب کشور به پرواز درآمدند</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18620" target="_blank">📅 23:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18619">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آسمان کشور در حال کلیر شدن...</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18619" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18618">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خداوکیلی این چه زندگی است....</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18618" target="_blank">📅 23:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18617">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHWNGk71IgrEJGXn8i_LkuFuniyTx3ZvcAJB-aCuBith8UqSmvHO1UBENDP-2it3pBzLZlryfEcmqPqcI5MfvHg-ihdwtoZS4nlW1mpl0xKiamZ-m04EXFB1TFneTsJCW5K03HPE_rF5qWKhy3GctCiWoYQGBgRWhOoIsfcNyS9qKwj5o2dLOtJomyPzwzuXQPiDF2aaAcQHkP9O1UVD_PojwLU1pZ92ZeErGV0tcPRd_aGxoWqlfgWM3C5fG1YP6kUD4Q4_cDuR6t1KC8DyIgtiqN88YM2LkCGyC00jdfy1Dkz7TMkXT72kvm4wB-hsmPsVos3uvLLwqdyg23T8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.  ارزیابی‌های فعلی حاکی از آن…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18617" target="_blank">📅 23:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18616">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.
ارزیابی‌های فعلی حاکی از آن است که احتمال حملات نظامی در دو تا سه ساعت آینده وجود دارد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18616" target="_blank">📅 22:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18615">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18615" target="_blank">📅 21:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18614">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">لازم به ذکر است که جناب خضریان عضو کانال ما هستند و پوزیشنهای سنگین Long روی نفت دارند</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18614" target="_blank">📅 21:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18613">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گفته می‌شود ایران در جریان سفر ترامپ، رئیس‌جمهور آمریکا به ترکیه، تلاش کرده است او را ترور کند.
اطلاعات ارائه شده توسط یک منبع خارجی که به مقامات آمریکایی در مورد این توطئه ادعایی هشدار داده بود، باعث شد تا در آخرین لحظه، هواپیمای مورد استفاده رئیس‌جمهور در پرواز بازگشت به واشنگتن تغییر کند.
— یدیعوت آحارانوت |</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18613" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18612">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تکرار حرف مدیر Secret Box از سوی دکتر خضریان:  علی خضریان، عضو کمیسیون امنیت ملی مجلس:   مسئولان دستگاه دیپلماسی ایران در دنیای موازی زندگی می‌کنند  آمریکا و ترامپ می‌گویند که ما از توافق‌نامه خارج شده‌ایم و آتش‌بس تمام شده است بعد مذاکره‌‌کنندگان ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18612" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18611">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اینها هم رسماً بیکار هستند. خود ترامپ دیروز گفت از دید او آتش بس تمام شده و دیشب آمریکایی ها جنوب کشور را شبیه جنوب لبنان کردند آن وقت اینها می گویند این کار نقص بندهای 1 و 5 یادداشت تفاهم است!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18611" target="_blank">📅 21:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18610">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">لابد دیده ایم آزادی قدس از دست یهود سخت است گفته ایم کویت و بحرین را از دست خود عربها آزاد کنیم.  به نظر من که ساده تر و بهتر است.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18610" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18609">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ادامه پرتاب موشک از ایران</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18609" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18608">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvtxG9cM5P648ZHzISep3HWmQSHEO2cOmKE2vU-Psfnal3TsWU-v5TMDJyLDHKfIL9s2rbZSR6SKlTunbSBopE2ZZzYBJk9cbrj1zD4pbKI1gGCL-RXgt2stDMpmxJKfv1GxNtwhOicTv4xpOQiK8y4XOc1Pe61uwmkCug6GG7w1_mxlxYZAzopOu7BmQzCXoNJqpKUBhm1CrziducvqmhrsGGYaF1EYYGZnLsKhDd0lvvoYhHwdgVlD_TmqIzD_LtCA2ghxL4c4Hf1ywsHX10VDF6Dxj3rM7uCyzhjrR-rrrAkFer7d5afkYjufF6Os82T1sYWUIPfimCDtEykCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی این حرامزاده هم دیشب سقط شد
مردی که قطر‌ را به مرکز ترویج تروریسم اخوانی تبدیل کرد و از حامیان اصلی حماس و القاعده‌ در سوریه هم بود.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18608" target="_blank">📅 19:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18607">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">منابع عربی از کشته و زخمی شدن چندین سرباز امریکایی در پی حملات سپاه به مواضع آمریکا در کویت خبر  می دهند!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18607" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18606">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دود غلیظ پس از برخورد موشک های ایران به جایی در کویت</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18606" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18605">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">در حالی که سنتکام میگوید تنگه هرمز باز است، اژدهای بندر نظر دیگری دارد!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18605" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18604">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18604" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18603">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeefUr7yjYBy703P-TovZ2YuSwHPZEHpvLy4Zu-e997rSBpv4ZN0Tz_PtyBfWE0_6xMwImfojz7bPsSsKt49NkWDK8yb3geB-2-YUyleFQjlIQeRe5AeKdIKabBFH7S6THt0gBi4ncPOs3M12jMHkYBUyFfNo6FH9UmiUxyzpIL9uwXZmcD0vFJnFirfDYFcnUEq1lNWvZCsUzbt9oV_ETL3fsNaxIPO1-LGcsChgeLOoy-ad924D84hpOaq7YjF8kFRfnYmr3JxkXPaWl9IzQiOz2d-e0N5g42M7am5mCJDXewMzxhGL9XJE5qHEXqYtD9WopFLJz-CBsQECJwqyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18603" target="_blank">📅 19:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18602">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.  همین</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18602" target="_blank">📅 19:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18601">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">لابد دیده ایم آزادی قدس از دست یهود سخت است گفته ایم کویت و بحرین را از دست خود عربها آزاد کنیم.
به نظر من که ساده تر و بهتر است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18601" target="_blank">📅 19:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18600">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.
همین</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18600" target="_blank">📅 19:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18599">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1TY3uPCQnQX6zKotkfLeOHDOThAUrSdnLVCtHTEBiv-ZpGwYYi_UgexSnDiNEHkU_nkRTqxDB0Ab4RkVkzLamH0kL--tPfkvinDD6KUUgY2prMamtQ8NcNJ1BhSeNvkyy0no-Zx3hlWHWHYn3rciH0v4n2fLTncI8wKbLcKnKxwBPZJhtJ4tgQlbwZL8Q-OPG0PTNzQQmld90_cPTd4JO3b5qJ_U1AaqKrkGssZkNw6JynPwE71Crcn9QWr93DQ8SeI1JkSFha7sqSkt6pPOFfncXqMkT1nB4R9CE_CpAqHEuNLEKuEF_MTr6CzjEO0dWVRz3b0Zy1j1i1gfcnT1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18599" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18598">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18598" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18597">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ :  آنها (ایرانی ها) دیروز با توافقی موافقت کردند که از نظر ما کاملاً ایده‌ آل بود،دیگر هیچ برنامه هسته‌ ایی در کار نبود و از همه‌ چیز دست کشیدند  اما پس از آن، اتاق مذاکره را ترک کردند و کمتر از یک ساعت بعد، یک پهپاد به سمت یک کشتی شلیک کردند</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18597" target="_blank">📅 17:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18596">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرنگار: تنگه هرمز باز است یا بسته؟  ترامپ: «تنگه هرمز باز است و من نمی‌خواهم در مورد آن صحبت کنم چون می‌خواهم به یاد لیندسی گراهام باشم.  قبل از تماس تلفنی به شما گفتم.»</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18596" target="_blank">📅 17:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18595">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18595" target="_blank">📅 17:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18594">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18594" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18593">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDp1mPelWvPLPHFF3NkT6CKLnH_aqiOA5OBFlscKP-uf6iLNiQ76WObJxd0fgPi7KQpIcnQoH8YlCqt1wL7Y3P0P7EN7RQH8WlvYL5-puAaMFsoFjOmVaUIGIOcOYegAUFUO_Ukb5eqPeE6sEdwlhSwUIvjviBBzaAYJPK-bvvNE0qheYTTK41hGepVWI7VO-UX8XrH_4cFkV7rzd5l5bjBEAhXEHGMvQzKmlx3SSgGX_uXSaLTYX49FlYXvCQnBNxnOYnUjZvDCB8Z_7_KOn8xV-TKwOhx7w4lT7780jYlxEQA_dUBRbjZoh9r8HQ4fbULIFHAmqFnVI9W0nvMIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18593" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18592">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان یک آبراه بین‌المللی باقی می‌ماند. نیروهای ایالات متحده مستقر و آماده هستند تا اطمینان حاصل کنند که این وضعیت حفظ شود.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18592" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18591">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">توانیر: کاهش ظرفیت شبکه برق به دلیل آسیب‌های گسترده‌ در جنگ
‌
مدیرعامل شرکت توانیر:
حدود ۴۲۰۰ مگاوات از توان شبکه برق کشور کاهش یافته و بیش از ۲ هزار نقطه از شبکه دچار آسیب شده‌اند.
با وجود فشار مضاعف گرمای تابستان بر شبکه، عبور کم‌چالش از روزهای پیش‌رو در گرو همراهی مردم است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18591" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18590">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekLK7kZaXeQmbTlIKMgikPCxvB_-N3FPgGujNnMs0hPsywCRNui8CrMIIL1kauSarp0I8w52s38wobbGjClT6vBsLONquZD8kzrR-72rQiX5OxShppSubD2u-SLVToHA43EgkF8j5Cs8Q_4uOBgVqUp2uQ-0ue_yfgtKPVkHvUc1xaLfreTpJEcaVH8ykc5ya4FMcXguPeOgvRF4vdFsuBfTGH49wuQrNjasECR7A37VvsqKrmsqLx1afXU8S_w7TVd5Ns4tD3npdeAgH0stdZR4JEaTt2wZOuPR44aR3nd33Dq733qNdk_3sZsTL7UO4hvqs-Xv68Swjwgpduei4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان:   ما از ایران درخواست می کنیم به ارزش های اخلاقی و فرهنگی که دو کشور را به هم وصل می کنند، احترام بگذارند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18590" target="_blank">📅 16:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18589">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18589" target="_blank">📅 16:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18588">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18588" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18587">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18587" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18586">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تنها راه نابودی اسراییل این است که با آنها رابطه سیاسی برقرار کنیم و بعد عباس آقا را بگذاریم سفیر دایمی مان در اورشلیم !</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18586" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18585">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18585" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18584">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یعنی وسط کویر لوت هم یک قایق کاغذی کاردستی پنج سانت و ده سانت چپه بشود چند هندی گم می شوند!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18584" target="_blank">📅 15:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18583">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یک شهروند هندی پس از حمله ایران به یک کشتی تجاری در نزدیکی سواحل عمان گم شده است.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18583" target="_blank">📅 15:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18582">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">من که قانع شدم.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18582" target="_blank">📅 15:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18581">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عزت‌الله ضرغامی:   علت مرگ لیندسی گراهام دیدن تشییع جنازه میلیونی  امام خامنه‌ای بوده.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18581" target="_blank">📅 15:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18580">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18580" target="_blank">📅 15:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18579">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قول میدهم هر ۱۸ نفری که گم شده اند هندی بوده اند</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18579" target="_blank">📅 15:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18578">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">طبق گزارش‌های دولت منطقه‌ای که به رسانه (SCMP) استناد شده است، دو خلبان نظامی چینی، از جمله یک فرمانده تاکتیکی ارشد، ماه گذشته در حین تمرین‌های پروازی خط مقدم کشته شدند.
پکن که به ندرت تلفات نظامی را به‌طور عمومی افشا می‌کند، علت مرگ این دو خلبان را اعلام نکرده است و هنوز مشخص نیست که آیا این دو خلبان در یک حادثه کشته شده‌اند یا خیر.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18578" target="_blank">📅 14:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18577">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479291fcd2.mp4?token=nmmFYpVWNLkofKq96QcI1r94uFu_FpyuRgUN-hYktBzCYpWHAj3m57EAjq_yPVDidOxlOQpNqaMl4gTXXkElSA7baIbjPGyImQanWDuEfpMIB93kdsYNkDl0ElVbYksHGi7VQ9bukhZahYpbvpk8-R74kVd3tn2XC99ehx0bMDog8zjN8uvZ2GxrAfhO5YvNtdpMMmh1iKqOwC6m_mVG2AJBU8cxMfuzzxfFAcx5h14qnxM2p2cAfxe62mw6ZbDuE9OnBajuzNakuslQs38wc5ejD9RmNt6IMk0bmlAOZpWc9WHf5yoWUIU9YIS8ag_W2Ewh2E1jCosBTB1lfeJ2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479291fcd2.mp4?token=nmmFYpVWNLkofKq96QcI1r94uFu_FpyuRgUN-hYktBzCYpWHAj3m57EAjq_yPVDidOxlOQpNqaMl4gTXXkElSA7baIbjPGyImQanWDuEfpMIB93kdsYNkDl0ElVbYksHGi7VQ9bukhZahYpbvpk8-R74kVd3tn2XC99ehx0bMDog8zjN8uvZ2GxrAfhO5YvNtdpMMmh1iKqOwC6m_mVG2AJBU8cxMfuzzxfFAcx5h14qnxM2p2cAfxe62mw6ZbDuE9OnBajuzNakuslQs38wc5ejD9RmNt6IMk0bmlAOZpWc9WHf5yoWUIU9YIS8ag_W2Ewh2E1jCosBTB1lfeJ2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر جام جهانی در ایران برگزار می شد!</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/18577" target="_blank">📅 14:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18576">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M955qWRG8iZ-bhGlI4hHCh0W-0sCPEp6lP7tw938nZ-qhaf5VFiVHw4otf9k9QNXqNbUc8uXEq5lHZemufJlDTOjPdFFuOg5pMtfiAFAMcwwYIpoOJ-tr7i2RrZYuWQjMtSsntOIfcPKmv10ju4SwCLjEznLeQv-IvRBhlEQtdKgu0E36Jm2DdyRJtyauREv8sEaYTfZiYKYxmu_H-LxSFSEvdd_Sv3kV8z2BpUk2Svx4yfeyQg9s9-Oek26oefq4XczpoaKD6EWGD4oe4Mu_pFB6JVfL_BQA4WZgH1Uao7VawPGVmsC7aPud8zNU5BroS9j_MXS32eYIb25MP6pFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18576" target="_blank">📅 13:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18575">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18575" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
