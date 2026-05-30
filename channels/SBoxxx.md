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
<img src="https://cdn4.telesco.pe/file/QPCFZDM268wG53G2FFpmJPVExrP1hjVcuaDXzWcStIBorCPoqhRu5D9j_JTxOz7Wx97g-UrpZsjoIi2bcnCNYdTf9tUamO428NznTp-vXcw5d38owClXXmCJkNNDJJGYynJtRSoTe0irNWuO0pW2to-TNvid0q2GR2ari6g2lUj9JHf-1tY6fknTWVp1luwrvAKrXAT-RD1tAydPUuD4SQEXvwt-XP8xX5X9-4gC9OPGfITmAEuwvzkR8uksFGxYZh91b3hhp11i6SggjAQakhubqly1nNsbZvXQvuZ7luUNEd816ByIBCpTLhBrZmjeEcyDqrpD2lZzpF3EgNbCyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.86K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 20:41:57</div>
<hr>

<div class="tg-post" id="msg-16781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تا الان فکر می کردم فقط صیغه ساعتی وجود دارد...
سبحان الله؛ ویزای ساعتی را هم دیدیدم در این زندگی اما قهرمانی توفان سرخ آسیا را در همین آسیا نه!</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SBoxxx/16781" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حالا خوب است به این ویزا ندهند
😂</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SBoxxx/16780" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔵
بحران ذخایر استراتژیک در واشینگتن؛ تاجیکستان کلید حل بن‌بست تسلیحاتی آمریکا در برابر ایران
⬅️
گزارش‌های اخیر رسانه‌های آمریکایی، از جمله
ان‌بی‌سی
نیوز (NBC News)، از نگرانی عمیق مقامات دفاعی این کشور پرده برداشته است. بر اساس این تحلیل‌ها، واشینگتن در صورت تداوم یا تشدید درگیری‌های نظامی با ایران، با چالش جدی تخلیه زرادخانه‌ها روبرو خواهد شد؛ بحرانی که ریشه در کمبود شدید فلز راهبردی «تنگستن» دارد.
🔹
تنگستن که نقشی حیاتی در تولید مهمات سنگین و تجهیزات نفوذکننده نظامی ایفا می‌کند، از سال ۲۰۱۵ به این سو دیگر در داخل خاک آمریکا استخراج نمی‌شود. اکنون با جدی‌تر شدن سناریوهای تقابل نظامی با ایران، پنتاگون برای حفظ توان بازدارندگی و عملیاتی خود، ناچار به جست‌وجوی شتاب‌زده برای یافتن منابع جایگزین شده است.
🔹
در این میان، منطقه آسیای مرکزی به کانون توجه راهبردی واشینگتن تبدیل شده است. پیش از این، دونالد ترامپ شخصاً بر قرارداد تصاحب ۷۰ درصد از سهام میادین بزرگ تنگستن در قزاقستان نظارت داشت، اما به دلیل زمان‌بر بودن بهره‌برداری از این معادن، آمریکا اکنون به دنبال گزینه‌های در دسترس‌تر است.در همین راستا، نگاه‌ها به سمت تاجیکستان معطوف شده است.
🔹
همکاری‌های اخیر دوشنبه با کره جنوبی برای استخراج از معدن «میخورا» با ظرفیت سالانه ۴ هزار تن، به عنوان یک راه تنفس برای صنایع نظامی غرب نگریسته می‌شود. کارشناسان معتقدند تنگستن تاجیکستان می‌تواند به‌طور مستقیم یا با واسطه (از طریق کره جنوبی)، نیازهای مبرم ارتش آمریکا را پوشش دهد.
🔹
هدف نهایی این تحرکات، علاوه بر آمادگی برای سناریوهای جنگی در قبال ایران، قطع وابستگی کامل به چین در زنجیره تأمین مواد اولیه نظامی است. واشینگتن بر این باور است که بدون تأمین پایدار این فلز از منابعی غیر از چین، حفظ پتانسیل رزمی در برابر رقبای منطقه‌ای همچون ایران، در درازمدت غیرممکن خواهد بود.</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/16779" target="_blank">📅 18:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16778">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">- مشاور ارشد رهبر عالی ایران، محسن رضایی:
همان‌طور که پیش‌بینی شده بود، رئیس‌جمهور ایالات متحده برای سومین بار به دیپلماسی خیانت کرده است.
با ادامه محاصره دریایی و مطرح کردن مطالبات بیش از حد در مذاکرات، او یک‌بار دیگر ثابت کرده که تمایلی به مذاکره ندارد و اهداف دیگری را دنبال می‌کند.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16778" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16777">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پییت هگست، وزیر دفاع ایالات متحده، هشدار جدی به چین صادر کرد
پییت هگست، وزیر دفاع آمریکا، در نشست امنیتی شانگری-لا در سنگاپور (۳۰ می ۲۰۲۶) سخنرانی کرد و نسبت به تغییر اساسی در رویکرد ایالات متحده به امنیت منطقه‌ای و همکاری با متحدان هشدار داد.
هگست تأکید کرد که امنیت منطقه آسیا-اقیانوس آرام برای مدت طولانی بیش از حد به قدرت نظامی آمریکا وابسته بوده، در حالی که بسیاری از متحدان هزینه‌های دفاعی خود را کاهش داده‌اند.
ایالات متحده از متحدان خود انتظار دارد حداقل
۳.۵ درصد از تولید ناخالص داخلی (GDP)
خود را به امور دفاعی اختصاص دهند.
کشورهایی که هزینه‌های دفاعی خود را افزایش دهند، از مزایایی همچون تسریع فروش تسلیحات، افزایش تبادل اطلاعات و گسترش همکاری‌های صنعتی-دفاعی بهره‌مند خواهند شد.
وی با لحنی قاطع اعلام کرد که متحدان و شرکایی که از پرداخت سهم خود در دفاع جمعی خودداری کنند، با
تغییر روشن و اساسی
در نحوه همکاری و تعامل ایالات متحده مواجه خواهند شد.
هگست چین را به‌عنوان چالش استراتژیک اصلی بلندمدت آمریکا معرفی کرد و بر لزوم ایجاد «تعادل قدرت پایدار» در منطقه تأکید ورزید تا هیچ کشوری نتواند بر همسایگان خود سلطه یابد.
وی از گسترش فعالیت‌های نظامی و رفتارهای تهاجمی چین در منطقه انتقاد کرد.
این سخنرانی نشان‌دهنده سیاست دولت ترامپ مبنی بر فشار بر متحدان برای تقبل بار بیشتر دفاعی و اتخاذ رویکردی قاطع‌تر در قبال جمهوری خلق چین است.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/16777" target="_blank">📅 11:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16776">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">توهم خطرناک جنگ مدرن.pdf</div>
  <div class="tg-doc-extra">328.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/16776" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مقاله ای طولانی اما بسیار خواندنی از اکونومیست درباره تحولات جنگ مدرن و خصوصاً بحث استفاده روزافزون از پهپادها و ریزپهپادها.
اشارات گسترده ای به جنگ اخیر ایران شده که خواندنی است.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/16776" target="_blank">📅 10:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGHVQHVvkATE2DQ225e3UpPKSZGmfi9Cu4gW5SuHGUtZHc54QvqHcJ1MGQsv1CkeutGHGT8BHhIBJ5lqoVg8KixS_LepOwOuUchHgvS9-8-Ln8qttd7cjasRoVZEKOIUk8gftYTZtPkqU_mRjRT6KKUbxoz3K5VCU2LyeptThlxrpual4cFw8yaFCsygK4WJJEKJ3DuRh6sORyUob6DZmm0xtMV16r-KHkIuNFp7v__B9mTy7D7pcY8257dsn6a4Pxe87HElnigEQjIIs05bU424kKcCegQbqV14NtpbS8Y1xJjL-LJ1woKZkpuMmdXSufAUPQYh3W2Gtx50oJ73eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام هدفگیری شناورهای ایرانی در جنوب تنگه هرمز از سوی ارتش آمریکا</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/16775" target="_blank">📅 09:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این فاکستانی ها هم فعلاً ظاهراً بلای خاصی بجز 100 مورد حادثه تروریستی که اصولاً در پاکستان از بارش باران فراوان تر است دامنگیرشان نشده اما فی الحال لیندسی گراهام گفته به آنها مشکوک است و الّا و بلّا باید به پیمان ابراهیم بپیوندند!</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/16774" target="_blank">📅 08:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16773">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پاکستان از 3 سمت تحت فشار است:  — هند ( که همین دیروز اعلام کرد عملیات سیندور را تمام شده نمی داند) — افغانستان (که هر روز شاهد برخوردهای مرزی در مناطق پشتون نشین پاکستان هستیم) — ایالت خودمختار بلوچستان که در آن نیروهای BLA با حمایت مستقیم هند ( و شاید ایران)…</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/16773" target="_blank">📅 08:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16772">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/16772" target="_blank">📅 07:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16771">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بزنید زیر میز!  ما هم پشتتان هستیم!  حیدر، حیدر!</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16771" target="_blank">📅 23:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16770">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">چرا میخند؟!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16770" target="_blank">📅 22:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16769">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بزنید زیر میز!
ما هم پشتتان هستیم!
حیدر، حیدر!</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/16769" target="_blank">📅 22:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16768">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این توافق شایسته جایگاه ما به عنوان یک ابرقدرت نوظهور نیست!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16768" target="_blank">📅 22:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16767">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نیویورک تایمز:  بحث رئیس‌جمهور ترامپ در اتاق وضعیت نزدیک به دو ساعت طول کشید، اما او به توافق در مورد یک توافق جدید با ایران نرسید، طبق گفته یک مقام ارشد دولت که با شرط ناشناس بودن برای بحث در مورد مباحثات داخلی صحبت کرد.   دولت احساس می‌کند که به رسیدن به…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/16767" target="_blank">📅 22:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16766">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نیویورک تایمز:
بحث رئیس‌جمهور ترامپ در اتاق وضعیت نزدیک به دو ساعت طول کشید، اما او به توافق در مورد یک توافق جدید با ایران نرسید، طبق گفته یک مقام ارشد دولت که با شرط ناشناس بودن برای بحث در مورد مباحثات داخلی صحبت کرد.
دولت احساس می‌کند که به رسیدن به یک توافق نزدیک است، اما سایر مسائل همچنان حل نشده باقی مانده‌اند، به ویژه آزادسازی وجوه مسدود شده ایران</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16766" target="_blank">📅 22:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16765">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تو شیر پیل افکنی !
بزن که خوب میزنی !</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16765" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16764">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تحلیل استاد خانعلی زاده از توافق ایران با آمریکا!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16764" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16763">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2CIEmHScFVW8VRd4dXj8yi5I4ys-kIWG_PTaNMr4-EPbBkUU4tHi3a-tTIP74CQU6F0MH1iGqITNbSAhLrETbZs8N1nkN6V-QuUIOe0EkUrRGRiYydhhbDlu4zgWicJ_uAf3YY_mssb-5ApRS0ZXVEEYZm9o_yXD84l5G3omxeRJJ2RXZ0RxbTYHITTWDSB2LUgOtpH1E5ctufAed43yy-gpvXq4Mg0VC_u77sYMDBbfvCjsu4yKHIQq8WXNS3xy52XnL6LZrT9XT6W-S-CH30o2SVTlrj70a1MZGEcJoj1FObZef8ftpe2ICWJFqviYrI3o3H8G3-_SEvAkIp-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل استاد خانعلی زاده از توافق ایران با آمریکا!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16763" target="_blank">📅 22:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16762">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نقش پنهان امارات در جنگ شامل ده‌ها حمله به ایران
به گزارش وال استریت ژورنال، امارات متحده عربی ده‌ها حمله هوایی علیه ایران را از روزهای اولیه جنگ آغاز کرد و تا روز پس از اعلام آتش‌بس ادامه داد،
درگیری عمیق‌تری که تاکنون در کمپین هوایی تحت رهبری ایالات متحده و اسرائیل شناخته نشده بود.
محدوده این حملات شواهد بیشتری از تمایل فزاینده این کشور به محافظت از آنچه به عنوان منافع استراتژیک خود می‌بیند ارائه می‌دهد و آن را از برخی از همسایگان خود در منطقه خلیج فارس متمایز می‌کند که رویکرد بسیار محتاطانه‌تری نسبت به تهدید از سوی ایران اتخاذ کرده‌اند.
این حملات با هماهنگی ایالات متحده و اسرائیل انجام شد که هر دو اطلاعاتی را فراهم کردند، افراد گفتند.
اهداف شامل جزایر قشم و ابوموسی در تنگه هرمز؛ بندرعباس، پالایشگاه نفت در جزیره لاروان در خلیج فارس و مجتمع پتروشیمی عسلویه بود‌ه است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16762" target="_blank">📅 22:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16761">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فعال شدن پدافند در قشم!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/16761" target="_blank">📅 22:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16760">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ:  محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/16760" target="_blank">📅 18:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16759">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ:
محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/16759" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16758">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">کمیته امنیت ملی مجلس ایران:
قصد نداریم اورانیوم غنی‌شده را به کشور ثالث منتقل کنیم اما شاید آنرا به کشور رابع ارسال کنیم.
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/16758" target="_blank">📅 15:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16757">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcaQoMdSKCL-vTBR5lUBLrLIV6xJxbgWr5qy8PWCxgMwFK2s5cXps7sOasuUXv-GnmTSF_GUM8qEHI_dB1D9UGHFYMKUaW7iT-PYfHfZ1wLfXzrSJ059JIjs6euZ6nmXlrb5lOJsGQzijkNMsaPK2xVBhN1kECVw0RUMtZ35IX1vCGmA1bkxyOZFh3fa2XvuLQPQ2HMuKZb7UnkJT1GxxHJA3r3bIl6PbpzLWrPuR1Y0lLEwGbtEo4YUHfF6j-UlFX_y5LFpOyjMrBHvNxExDF_r6VIzKtvWN-zVHhS92LgvrT9mtuQ9KOsW8Wumll9yBp_nM0AsbWlb0326zIaX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره عملکرد پهپاد شاهد-136 در جنگ اخیر
جنگ اخیر نشان داد که پهپادهای خانواده شاهد همچنان یکی از مهم‌ترین ابزارهای تهاجمی ایران به شمار می‌روند، اما بسیاری از ادعاهای مطرح‌شده در فضای مجازی درباره عملکرد آن‌ها نیازمند تفکیک میان واقعیت‌های تأییدشده و ادعاهای اثبات‌نشده است.
پهپاد شاهد-۱۳۶ که در سال‌های اخیر به‌طور گسترده مورد استفاده قرار گرفته، از سامانه‌های ناوبری ماهواره‌ای و هدایت اینرسی برای رسیدن به اهداف خود بهره می‌برد. برخلاف برخی ادعاها، استفاده از ناوبری ماهواره‌ای در این پهپاد فناوری جدیدی محسوب نمی‌شود و از ابتدا بخشی از طراحی آن بوده است. آنچه می‌تواند یک تحول مهم تلقی شود، استفاده از ارتباطات داده‌ای پیشرفته، انتقال تصویر زنده و هدایت لحظه‌به‌لحظه تا زمان اصابت است؛ موضوعی که تاکنون شواهد مستقل و عمومی کافی برای تأیید گسترده آن منتشر نشده است.
در جریان درگیری‌های اخیر، گزارش‌هایی درباره استفاده از نسخه‌های پیشرفته‌تر پهپادهای شاهد منتشر شد. برخی منابع از نصب دوربین‌های اپتیکی بر روی این پهپادها و افزایش دقت آن‌ها سخن گفته‌اند. از نظر فنی، افزودن دوربین به چنین سامانه‌ای کاملاً امکان‌پذیر است، اما ادعاهایی نظیر «اصابت صددرصدی» یا «نابودی قطعی همه اهداف انتخاب‌شده» با واقعیت‌های شناخته‌شده جنگ مدرن سازگار نیست. هیچ سامانه تسلیحاتی در جهان، حتی پیشرفته‌ترین موشک‌ها و مهمات هدایت‌شونده غربی، دارای نرخ موفقیت صددرصدی نیستند.
یکی از مهم‌ترین ادعاهای مطرح‌شده مربوط به آسیب دیدن یا انهدام یک فروند هواپیمای هشدار زودهنگام آمریکایی (AWACS) در پایگاه پرنس سلطان در منطقه الخرج عربستان سعودی است. منابع ایرانی این حمله را موفقیت‌آمیز توصیف کرده‌اند و برخی تصاویر ماهواره‌ای نیز نشانه‌هایی از آسیب به یک هواپیما را نشان داده‌اند. با این حال، جزئیات کامل حادثه و نوع دقیق سلاح به‌کاررفته هنوز به‌طور مستقل و قطعی تأیید نشده است.
در خصوص سامانه دفاع موشکی THAAD نیز گزارش‌هایی از آسیب دیدن برخی تجهیزات و رادارهای مرتبط منتشر شده است. با این حال، ادعای نابودی کامل چندین آتشبار و خروج دائمی آن‌ها از خدمت هنوز از سوی منابع مستقل تأیید نشده و نیازمند شواهد بیشتری است.
در مجموع، داده‌های موجود نشان می‌دهد که پهپادهای شاهد همچنان توانایی ایجاد خسارت‌های قابل توجه و نفوذ به برخی لایه‌های دفاعی دشمن را دارند. با این حال، بسیاری از ادعاهای مطرح‌شده در شبکه‌های اجتماعی و کانال‌های خبری غیررسمی درباره عملکرد این پهپادها، فراتر از اطلاعاتی است که تاکنون به‌طور مستقل قابل راستی‌آزمایی بوده است. تحلیل دقیق تحولات نظامی مستلزم اتکا به شواهد مستند، تصاویر ماهواره‌ای معتبر و ارزیابی‌های مستقل است، نه صرفاً ادعاهای تبلیغاتی طرف‌های درگیر.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/16757" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16756">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خلاصه دیدگاه موسسه مطالعات جنگ درباره اهمیت راهبردی کنترل تنگه هرمز در دکترین جدید بازدارندگی جمهوری اسلامی:
مقامات ارشد ایرانی در ماه‌های اخیر بار دیگر بر اهمیت راهبردی تنگه هرمز به‌عنوان یکی از اصلی‌ترین ابزارهای قدرت و بازدارندگی جمهوری اسلامی تأکید کرده‌اند. در این چارچوب، علی‌اکبر ولایتی، مشاور رهبر جمهوری اسلامی، کنترل ایران بر تنگه هرمز را «اهرم نهایی» و «ضمانت واقعی» پایداری هرگونه توافق احتمالی میان ایران و آمریکا توصیف کرد. این موضع‌گیری نشان می‌دهد که تهران، پس از تضعیف بخشی از توان بازدارندگی متعارف خود، به‌ویژه در حوزه موشکی، بیش از گذشته بر موقعیت ژئوپلیتیکی تنگه هرمز به‌عنوان یک دارایی راهبردی تکیه می‌کند.
از نگاه ایران، ارزش تنگه هرمز صرفاً در موقعیت جغرافیایی آن خلاصه نمی‌شود، بلکه این گذرگاه یکی از حیاتی‌ترین شریان‌های انتقال انرژی جهان است و توانایی تأثیرگذاری بر امنیت انرژی بین‌المللی را در اختیار تهران قرار می‌دهد. کنترل یا اعمال نفوذ بر جریان کشتیرانی و صادرات نفت در این منطقه، برای ایران ابزاری جهت ایجاد بازدارندگی، افزایش قدرت چانه‌زنی و محدود کردن گزینه‌های نظامی آمریکا و متحدانش محسوب می‌شود. در واقع، تهران تلاش دارد کنترل بر تنگه را به‌عنوان بخشی از معادله امنیت منطقه‌ای و یکی از پایه‌های نظم مطلوب خود در خلیج فارس تثبیت کند.
در همین راستا، مقامات و رسانه‌های ایرانی بر لزوم مدیریت ترافیک دریایی در تنگه هرمز تحت «ترتیبات ایرانی» تأکید کرده‌اند. برخی گزارش‌ها حاکی از آن است که ایران در مذاکرات غیرمستقیم با آمریکا خواستار به‌رسمیت شناخته‌شدن نقش محوری خود در مدیریت امنیت و عبور و مرور دریایی در این آبراه بوده است. این دیدگاه در تعارض مستقیم با سیاست سنتی آمریکا مبنی بر تضمین آزادی کشتیرانی در آب‌های بین‌المللی قرار دارد.
هم‌زمان، اختلافات اساسی میان تهران و واشنگتن درباره موضوعاتی نظیر برنامه هسته‌ای، لغو تحریم‌ها، آزادسازی دارایی‌های بلوکه‌شده و آینده حضور نظامی آمریکا در منطقه همچنان پابرجاست. گزارش‌های منتشرشده نشان می‌دهد ایران تلاش می‌کند پیش از ورود به توافقات گسترده هسته‌ای، امتیازات اقتصادی و امنیتی مشخصی دریافت کند؛ موضوعی که از نگاه آمریکا می‌تواند بخشی از اهرم فشار واشنگتن را تضعیف کند.
در فضای داخلی ایران نیز برخی رسانه‌های نزدیک به ساختار امنیتی، بر ضرورت تبدیل دستاوردهای نظامی اخیر به دستاوردهای سیاسی و راهبردی پایدار تأکید کرده‌اند. در این چارچوب، تثبیت نفوذ ایران بر تنگه هرمز به‌عنوان یکی از مهم‌ترین ابزارهای قدرت ژئوپلیتیکی کشور، جایگاهی محوری در محاسبات راهبردی تهران یافته است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16756" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16755">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رسانه اسرائیلی یدیعوت آحارونوت گزارش داد که اسنادی که توسط سرویس اطلاعاتی موساد اسرائیل در ۱۳ ژوئن ۲۰۲۵، در مرحله افتتاحیه «عملیات شیر در حال صعود» منتشر شد، نشان می‌دهد که عوامل ایرانی آموزش دیده توسط اسرائیل و نه خود عوامل موساد اسرائیل در داخل ایران فعالیت می‌کرده اند.
طبق این گزارش، این عوامل در اسرائیل آموزش دیدند، به زندگی عادی در ایران بازگشتند و منتظر فعال شدن بودند. در بهار ۲۰۲۵، تیم برنامه‌ریزی مشترکی از موساد و نیروی هوایی اسرائیل به آنها مأموریتی برای از کار انداختن یک مرکز دفاع هوایی ایرانی دادند که به عنوان بخشی از تلاش‌ها برای تضمین برتری هوایی اسرائیل بر تهران تلقی می شود.
این عوامل از طریق مسیرهای مخفی قاچاق با پهپادها، موشک‌ها و تجهیزات مأموریت مجهز شدند. آنها مختصات نهایی و دستورالعمل‌های استقرار را درست قبل از عملیات دریافت کردند تا خطر نشت اطلاعات به حداقل برسد.
در آن شب، سلول‌های مرتبط با موساد دیگری نیز فعال شدند، از جمله عواملی که به هدایت حملات علیه مقامات ارشد نیروی هوا و فضای سپاه پاسداران و مختل کردن سیستم‌های دفاع هوایی و موشک‌های بالستیک در تهران و غرب ایران کمک کردند.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16755" target="_blank">📅 11:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16754">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شب گذشته شهر شیعه نشین مرجعیون در جنوب لبنان توسط ارتش اسرائیل تصرف شد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16754" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16753">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">CNN:
پس از حملات ایالات متحده و اسرائیل که در طول جنگ راه‌های دسترسی به «شهرهای موشکی» زیرزمینی ایران را مسدود کرده بودند، حداقل ۵۰ تونل دسترسی پاکسازی و تعمیر شده اند.
تصاویر ماهواره‌ای نشان می‌دهد  که ماشین‌آلات سنگین در حال برداشتن آوار و باز کردن ورودی‌ها در چندین سایت موشکی هستند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/16753" target="_blank">📅 09:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16752">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو:
در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/16752" target="_blank">📅 09:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16750">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خبرهایی دال بر فعال شدن پدافند اصفهان!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/16750" target="_blank">📅 00:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16749">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2azqt48Q49M7RDeHvZ1_5hhuxxBUgVZu-p3UxE46b6yHYFIcru3SBd8AE5kuP-fNxd7JZUW-iBKfAWX8LydrahRX3wapR8PpGYkzhc1HRGFTr5TVKy2YfKRYVvIn5XxiKk0qnphYDTbmT0aKU1AY-qeGcTBG6CNswUbqUmyTbz4sKPA2MaQ0S86GABeBpZzQn1VNlMo1Lkdi6VFatPpi1ZsuVthl54qSL48NENiM9151z67TiHqJOcmXakVblHkf4sUrJ6mmN1_rWiVPVT28SoesrVmF7RDegYu3ZGTpsZSyndapA5nEgX22K4oBLfQbKUp_D1MRNG3oo6D6LCb5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16749" target="_blank">📅 23:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16748">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تسنیم گزارش داده که مردم بندرعباس نگران نباشند، منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا مربوط است!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/16748" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16747">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تسنیم گزارش داده که مردم بندرعباس نگران نباشند، منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا مربوط است!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/16747" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16746">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/16746" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16745">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">باز گویا در هرمز تبادل آتش داریم!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16745" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16744">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">باز گویا در هرمز تبادل آتش داریم!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/16744" target="_blank">📅 23:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16743">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOwnETMifRUMLHST-24UJxeN5Pw05oAQNahvGOv13RUTydxI43sWdJLP2jpUypztrYe-ejxImpBjgzhIlCzt1nmaBiGxX-7cGcVwtvi4szzyaL3f4iDffWv9hmGCixyfze8Vje4oz-BmAGfQiUc0gG8WJmNAq67B518xlMb1S2Df84DuRrtSLM8sC1oca-60hwOCCGBl8x6lDpQaN8FroIxm4PzM_rRs6fStPgEG8bVUZZyFTGUSH6HFj73t_GSyK2G2Lien6L2H3NBxnqxeNdwscmYOYJ95Wtm0rAtDDU3SxObFpj1NA6myVNcibPktFTwFZJ9LZJ5k8tGHzYW1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/16743" target="_blank">📅 20:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16742">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این عمانی ها هم بدبخت‌ها یک بار زمان شاه از شر کمونیسم نجاتشان دادیم ولی ۲۰ سال است که سر‌‌ پرونده هسته ای رنده شده اند!  اینقدر که اینها پیام آوردند و بردند، ۱۲۴ هزار پیامبر نکردند</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16742" target="_blank">📅 18:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16741">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:   «من این را به‌طور خاص به عمان می‌گویم؛ ایالات متحده با هر کشوری که به ایران در وضع عوارض در تنگه هرمز کمک کند، قاطعانه برخورد خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/16741" target="_blank">📅 18:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16740">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ تهدید به منفجر کردن عمان کرد.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/16740" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16739">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X16-1U5wGYcnooJsrExLLBN8ja_C704cfx28NcTcDrXSlMvdUkNlG4cOv1Qv1xO2asA-ouYtQJe2ebg0EKcXqOf7G8GtcVdy22EofdE5CiZ759-uIboMSh58PyKCgVW1gWpIG0xiQGtCxtUdZf8gyKnMkNtM0SlRmmp_r_CKKNFtQKW5zAgj0rrJXT6wQJ2ky5W7OOv2arXohe2OLGP-HcV70_GUfg7MlEt30yAB5D1mVy2rwBfbGIiT3mdAiFJ3L-6-fV6Ys9qIQZh6ZTy54FQQEMF4AFuVScT4V_Ru1n4osG0iBJLSPUpZiehMvWGZ2FKs4AQ5DhSj42aK-5jZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#VIX
— H4
شاخص ویکس از محدوده ای که جنگ شروع شد پایینتر آمده و کانال را هم شکسته.
سوگمندانه بازارها ما را به یک ورشان هم حساب نمی کنند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/16739" target="_blank">📅 18:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16738">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/16738" target="_blank">📅 17:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16737">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نتانیاهو:
باید مأموریت در ایران را کامل کنیم و تقریباً روزانه در این خصوص با ترامپ صحبت می‌کنم.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16737" target="_blank">📅 17:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16736">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شرایط توافق شده :  هیچ گروه مسلحی در جنوب رودخانه لیتانی وجود نداشته باشد  کنترل ارتش لبنان بر جنوب  سلاح‌های حزب‌الله محدود شده یا ‌حذف بشود</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16736" target="_blank">📅 16:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16735">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ریچارد فانتین تحلیلگر ارشد سیاست خارجی آمریکا :   محتمل‌ترین پایان این جنگ داغ، یک توافق محدود است. سپس مذاکراتی طولانی و شاید بی‌حاصل آغاز خواهد شد. جنگ سرد از سر گرفته می‌شود. و آمریکا و ایران در انتظار دور دیگری از درگیری در روزی دیگر خواهند ماند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/16735" target="_blank">📅 14:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16734">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/16734" target="_blank">📅 14:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16733">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ماکرون و احیای آرمان شارل دوگل  در تحولات اخیر، رئیس‌جمهور فرانسه، امانوئل ماکرون، اقداماتی قاطعانه انجام داده که یادآور میراث شارل دوگل است و خود را به عنوان یک رهبر کلیدی در دفاع و خودمختاری اروپا معرفی کرده است. پیشنهاد ماکرون برای گسترش بازدارندگی هسته‌ای…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/16733" target="_blank">📅 14:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16732">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2md1Ns6hjvzvNtlPIHJ06w5QK6_2sMFfPV0H9KU_KdGanIpsLFt7t6w3d5mY2tnYi09yYo54QfUGKFVLX0wNcu3FX84TYCSmsLnXWps1hW8oux4CTpp7OWTiiFhhBt8iWctxxUToOcKb0yrRdPDf6anD8mRAOu96WIMH3hImpsS0vjmd2QPQ5HXMhQvRWFqzV8c7GZGGBN_WUexZHozwjm9OC4Qru_nOnKlfkI6K-sLT0vN6WrvhHmSQIc4pguPS083XML7WPohZgn0UC-fKDfkbHAdFgkUWTZhsBMuf3jsSTG8CpMq8EiwNqIk7SzgaY2bbmcgKvxVU1MNzA3Mlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی خودارضایی مبارک!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/16732" target="_blank">📅 13:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16731">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اگر دولت ما آن بالا Short کرده بود تا الان خسارتش جبران شده بود.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16731" target="_blank">📅 11:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16730">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">#TOTAL — H4  حدود 250 میلیارد دلار از ارزش بازار کریپتو پودر شد.  اکنون به کف کانال رسیده و اگر فروش هست باید تریل کرد یا کلاً تسویه.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16730" target="_blank">📅 11:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16729">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8MDABHKtf95Cg-U1EsMShN0N8cI6AooZm-eUOlYFmkHbv-txKZQIK-EVfmDYYl2TLWsDYDjO00K1qbbegqpopPXb6qN2OIYWysqIByzebYyFrXyazuHcD1B7Vz2vNSAfWFdoz8RMlz2WqFFoWXnZuMAHkIazGOWJDidI0--0mt4bn1PWI1PPUYdaqDReYfK4DdljMcC_nbxTsnSCY8EMzVvbg0_9aEfhcWHSYAtnR2pRK2kqIq5mipkfhzOWQuZAw8o2MP0USlcl6p2u2mp7hKhmVnfG_qJlr_OQaNc2S4CESAA_2DJeOgiHD4jZoApimAd3z7NmUUQZ3CcXLXjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TOTAL — H4  تایم پایین تر</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16729" target="_blank">📅 11:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16728">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/16728" target="_blank">📅 09:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16727">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89cfb8e810.mp4?token=XiKPAgf-PPuZlQiF7o8axnusf7a8tEDyAG66jochbjQcaS6CJZTdY8kIoeJkVXru9nV7iAMnPp3ICuk9qZPd2d6wi1p6xEHrUN_DtXswADErP17Ex8pFyZm6Ns7Rawp9x5JNsSFnZY2fladqS7VsMAXy460FAKP_OgW57PSVhjCdaaqs3ndmJbolm2vJB3NpZJoPKqtmAQ-Nvr4pHIrfZyBEAtTU-s5Nw8xMAkWojAoLmEzcFH-Y8-uRzCJWsp-doLON3FjC0OOiqRPl5AwMWtc_rfmTOgkwRPi6yfDGP9V4UNYtfFcVc3-p8iTookOSYrrWe0l0jsA36-uPB1GCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89cfb8e810.mp4?token=XiKPAgf-PPuZlQiF7o8axnusf7a8tEDyAG66jochbjQcaS6CJZTdY8kIoeJkVXru9nV7iAMnPp3ICuk9qZPd2d6wi1p6xEHrUN_DtXswADErP17Ex8pFyZm6Ns7Rawp9x5JNsSFnZY2fladqS7VsMAXy460FAKP_OgW57PSVhjCdaaqs3ndmJbolm2vJB3NpZJoPKqtmAQ-Nvr4pHIrfZyBEAtTU-s5Nw8xMAkWojAoLmEzcFH-Y8-uRzCJWsp-doLON3FjC0OOiqRPl5AwMWtc_rfmTOgkwRPi6yfDGP9V4UNYtfFcVc3-p8iTookOSYrrWe0l0jsA36-uPB1GCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب الله زندگی شیعیان لبنان را با پیوند زدن سرنوشت شان به حیوانات اخوانی حماس به گه کشید</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16727" target="_blank">📅 09:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16726">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی
از بازی است
از دید من.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16726" target="_blank">📅 09:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16725">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وضعیت گروه هواداران پروفسور رائفی پور</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16725" target="_blank">📅 08:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16724">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCwaPtzWs18lu5Uvryx12hplKVXzoLi7Rr5rhsfXS7MHNKY18KAf10vHHPTXuC4971zg3CPBFx0KzRRRqhiBHrf5hUk5DbAhVoyZ8mdnTLbOk3gD8hSVghVxvRBypWuvwbo_2npJmxuDmZoReqqtFqUxiDiu9z979OvugcLSJnYcRUE1MopfEMwYh5o93e9429TouvQhmaxu61Zu1nDowoCCAqa0pOtWn_s3_SG9pxBaB2YEVe64-5i8UCkm3oIRJdh-ToggOH924NDpKNHXljYsunYPyHsThLNKXOXhgGTX7uYEwyv15wCmlvqNLU-x20bZ-iwCeJMrjM5Qu05G6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت گروه هواداران پروفسور رائفی پور</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16724" target="_blank">📅 08:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16723">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVVSzMjc2UemnbFzqbxmPiWf7t9ZgR4jvkmUjGu6Z9nH3r17mJ_d8BdwMF-a0mMCTGImK8Gz5hftLxIfh0DJsq6jLR5SmWD8uDltgJzxyxQnwJtsjyaNFOszd4JKuya-LHt-9aVB3fdqH_AESV_nBWDnhwpKFGH-PpUlYD5xklfACUr5r0joOlnBeCQpAsYWNqZIvllUBQ7xuvggpwhgxE1oCUw6dVn13BcL1J6avo5EGZBhLRz21DfCsuPjzaFeta7edi0G2BBqJ3TQ33IR3PLonSUUzyJWrA4jTjefPQvduEADAqAkF3ICdPcrU9A4osRX0KS8CjpNiRq0ej6mPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خیلی هم الکی نبود و سپاه یک پایگاه هوایی آمریکا را در کویت زد.  ولی هنوز موج 4 هستیم
😆</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/16723" target="_blank">📅 08:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16722">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک منبع آگاه نظامی به خبرگزاری تسنیم گفت: ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.   در مقابل، ارتش تروریستی آمریکا به زمین…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/16722" target="_blank">📅 08:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16721">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCtEwCQAnlxhWhzBi1JKsJNb8sjbcIO_pBGTb0C2tM8vsOBxESw0nRIw_AcXe1XE8-JOsd--ehDuIuCY7-g2LMKt80x7y8JXNTui1lhlecOqQH4wcnd5wm2Dk835kKUUoPcVw1B85fLwMqSxrIPNW1N5c6Ioy5LLd4F2L6IfBLhwSycB_mDAca8SbqKchove0_zBItSxBI243_np6zaTVCmTz4kdo99FwfIfUQcG2FtTGy5FPtlJC-MM6gg8plSe-pdYWZ9u9RylAon3o3QoRJyeZSTXEGBY_Ka-wVrYuJ4kB8qOpziirbq8_HyWLUnYOjAqYBWh0jUvZKOZaiklKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران یک موشک بالستیک از خوزستان به سمت پایگاه هوایی علی السالم در کویت پرتاب کرد که توسط سامانه پاتریوت مستقر در پایگاه رهگیری شد.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16721" target="_blank">📅 08:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16720">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ایران یک موشک بالستیک از خوزستان به سمت پایگاه هوایی علی السالم در کویت پرتاب کرد که توسط سامانه پاتریوت مستقر در پایگاه رهگیری شد.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16720" target="_blank">📅 08:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16719">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این قسمت بیانیه عملاً یعنی خیلی دنبال تنش نیستیم ولی خب.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/16719" target="_blank">📅 08:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16718">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع‌تر خواهد بود و مسئولیت و عواقب آن با متجاوز است.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/16718" target="_blank">📅 07:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16717">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سپاه پاسداران:
به‌دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیۀ فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدأ تجاوز، در ساعت ۴:۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع‌تر خواهد بود و مسئولیت و عواقب آن با متجاوز است.
و ماالنصر الا من عندالله العزیز الحکیم.
روابط‌عمومی سپاه پاسداران انقلاب اسلامی</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16717" target="_blank">📅 07:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16716">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الکی است و امروز یک توافق امضا می‌شود که البته در چهارچوب همان موج ۴ ارزیابی کنیدش</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16716" target="_blank">📅 07:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16715">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سبحان الله!
یک نفر که مشخص است از 28 فوریه تا امروز به نت جهانی دسترسی نداشته و صرفاً در بله و ایتا غسل می کرده در دایرکت پرسیده که استاد با این 300 میلیارد دلاری که از آمریکا میگیریم احتمال نمی دهید دلار تا 100 هزار تومن پایین بیاید؟!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/16715" target="_blank">📅 01:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16714">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ تهدید به منفجر کردن عمان کرد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16714" target="_blank">📅 00:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16713">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:  • آتش‌بس دائمی در همه جبهه‌ها • خروج آمریکا از منطقه • عدم دخالت در امور ایران • رفع کامل تحریم‌های اولیه و ثانویه  • آزادسازی وجوه مسدود شده • +۳۰۰ میلیارد دلار غرامت بازسازی • کنترل و مدیریت ترافیک دریایی…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/16713" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16712">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:  • آتش‌بس دائمی در همه جبهه‌ها • خروج آمریکا از منطقه • عدم دخالت در امور ایران • رفع کامل تحریم‌های اولیه و ثانویه  • آزادسازی وجوه مسدود شده • +۳۰۰ میلیارد دلار غرامت بازسازی • کنترل و مدیریت ترافیک دریایی…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/16712" target="_blank">📅 23:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16711">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:  • آتش‌بس دائمی در همه جبهه‌ها • خروج آمریکا از منطقه • عدم دخالت در امور ایران • رفع کامل تحریم‌های اولیه و ثانویه  • آزادسازی وجوه مسدود شده • +۳۰۰ میلیارد دلار غرامت بازسازی • کنترل و مدیریت ترافیک دریایی…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16711" target="_blank">📅 23:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16710">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:
• آتش‌بس دائمی در همه جبهه‌ها
• خروج آمریکا از منطقه
• عدم دخالت در امور ایران
• رفع کامل تحریم‌های اولیه و ثانویه
• آزادسازی وجوه مسدود شده
• +۳۰۰ میلیارد دلار غرامت بازسازی
• کنترل و مدیریت ترافیک دریایی در تنگه هرمز</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16710" target="_blank">📅 23:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16709">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترور جدید اسرائیل در غزه</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16709" target="_blank">📅 23:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16708">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXZGm8DvfnJMHQGr9PIFhJkISzoOwF6nY21KKdjHb5czyEQjMudepwgeBX2ZwviAsUqZWZ8VVB7_od9qX41qtV2vAAgronHT1PuJYYOAQOtkbMR9QAMcdet03rvbzWG-mtSfLCg9m-9MIv2ppUlFMZXwqXyGMf9rhrWuRr35dnLE9g6VS1GkA9w77RSlK0HUynvXLv-qwKFMDlI18iXEiUUYeFGBTD4qL5cDCwyEZy7qQ5HE0vni6uESOl5kyhDBsjCEbzeokQZwD20oBO8rw_MdRmsWX8TEMIL_rp0THGGQ8spzve8ImlcgQpAsJWP6rHVSpWmejiyjyYOcfxMP7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16708" target="_blank">📅 22:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16707">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e42f7252.mp4?token=Supq8dYCFewi0tbvJ-gZZGrnoYbYp6wg2k-_oGqBzf0qkd8hAH97KsZBnYFRgx1IWiDKOsAbr-q1-mz7hg6ae0_fpIQDreVbrztWc2G4XJ7orJG2PEGVEYpqC3wYUGpNREjTJvUIf48Nuza0LqjeypLusx-ePGfRhwqpIL_JWboVvz20Z7WEad5siStmdylerq3luezJ2VvRBTDgvD4M88c9Mk-C1ZrcFMrbP3JJblg-hfsc9psmVwMB7Xx84OuKo348S5kg0dvfWdwb4q2fDOy9aS_4-FWhghcg_19nSVwk6pQyvS__kME6azwxGLRzzRedgrbaPyZUkKOr3HW_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e42f7252.mp4?token=Supq8dYCFewi0tbvJ-gZZGrnoYbYp6wg2k-_oGqBzf0qkd8hAH97KsZBnYFRgx1IWiDKOsAbr-q1-mz7hg6ae0_fpIQDreVbrztWc2G4XJ7orJG2PEGVEYpqC3wYUGpNREjTJvUIf48Nuza0LqjeypLusx-ePGfRhwqpIL_JWboVvz20Z7WEad5siStmdylerq3luezJ2VvRBTDgvD4M88c9Mk-C1ZrcFMrbP3JJblg-hfsc9psmVwMB7Xx84OuKo348S5kg0dvfWdwb4q2fDOy9aS_4-FWhghcg_19nSVwk6pQyvS__kME6azwxGLRzzRedgrbaPyZUkKOr3HW_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ تهدید به منفجر کردن عمان کرد.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16707" target="_blank">📅 22:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16706">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این‌گونه_دکترین_نتانیاهو_برای_ایران_فروپاشید.pdf</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16706" target="_blank">📅 21:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16705">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ : سومالیایی‌ها، همه‌شون کلاهبردارن، خیلی هم خرابن، ماگرفتیمشون و داریم روشون فشار می‌ذاریم
☑️
@persiannbloomberg بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/16705" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16704">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c71816eb9.mp4?token=t5jdl07aDqUXd3uvauy2syOCcLKyYz0FsnY8_M-pfH6V79YgOCEMS0l1HvrwXlaLFBf0jwDJwaKw-O7IIyAUD95v4uj_pUV3JYAshI-jkd-UZ9AAs8dmjtZ9ti6_11SS0ZKNH9wzJJhOC-DFSM5to69tKasfAVjZ_-sWDd8cGcYjlS96t441LSKOWwxOkkXwBPX9p0WLOPOcAdlY69WCtGqVy7Ki95XQJp1JjqhCEuocwmE6O5wxkkN3LxvqpRJ76atvCRxs4sXfdpkntPHXPg6NPH3G9BDQrvem92iqF_Iwk0lmCTPMQl-rBE3lpwLyofS-E0l-FfmSvHaSqFeISw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c71816eb9.mp4?token=t5jdl07aDqUXd3uvauy2syOCcLKyYz0FsnY8_M-pfH6V79YgOCEMS0l1HvrwXlaLFBf0jwDJwaKw-O7IIyAUD95v4uj_pUV3JYAshI-jkd-UZ9AAs8dmjtZ9ti6_11SS0ZKNH9wzJJhOC-DFSM5to69tKasfAVjZ_-sWDd8cGcYjlS96t441LSKOWwxOkkXwBPX9p0WLOPOcAdlY69WCtGqVy7Ki95XQJp1JjqhCEuocwmE6O5wxkkN3LxvqpRJ76atvCRxs4sXfdpkntPHXPg6NPH3G9BDQrvem92iqF_Iwk0lmCTPMQl-rBE3lpwLyofS-E0l-FfmSvHaSqFeISw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : سومالیایی‌ها، همه‌شون کلاهبردارن، خیلی هم خرابن، ماگرفتیمشون و داریم روشون فشار می‌ذاریم
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16704" target="_blank">📅 19:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16703">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ:
ما از نتیجه مذاکرات با ایران راضی نیستیم،
مذاکرات رضایت بخش نیست.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/16703" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16702">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2VCOVg6mcJE0YeOVN366QiXxVudvGnWDVKKGnhB-02tAJ22n9Xw9N6rcIBg7-obXC0nvFMYEB0lB_hnCtMgC26uhzhQjbQTeeLQLv-aGIHgFYWooCA4Ucw0n6iyqxMfDhEcaPoCP8yCqU5LxrpgmY2DQmC5Srsa8m_v9sM6hp7lAQnTrUfx9Vef4HpCcRKtbyeuR7MUPqzhJWqS2IYCkJRc3nXtOxGAGcjy2mjoHEX8rBecmVgcDIeApQkOGDx5Tl8_MuGfbwHTSJRZG0dSw-9nf1C8J95bu5IpRT0na4aNq1oZrdPjrriIJBDtS8cjCXjizCawK6qa33Kv1FNiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16702" target="_blank">📅 19:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16701">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls0jse3aLBju_Me5X9fcNS_FCVmNLTYOKNGE4VrJqDxN4s_pKdmM7h-XJxCqr9kiDnhiEtdgFYiFewjRGu8ehGIrXEy95TgAwVZ4KUfWJf5qLyWsO9qLIvg74zxUtQ6LTlXhH7l3xGdTDpIqetQuYxO8Y2e0VC6f73MhacEdfTZCXZ0BWFBv_-FYH5DiYlTqKrPIDsQ6xQAwE-WBRDqqTvx5VtAQSnF2BrNZ_085MtYFU_pmDgnBTBLLhXHXYermk0b0eJRwqbF-zJWRpHqIzHCX320eYbOKVaukSefMsbVqGgRmFlpBrDNkMSLgfDuVw8uTDD1orR_3oYeMbhfsng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#US10Y — H4  فعلاً موفق شده با این سیرک امروزش مقداری نرخ بازده و نفت را همزمان سرکوب کند.   خواهیم دید چه خواهدشد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16701" target="_blank">📅 19:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16700">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کاخ سفید: مذاکرات به خوبی پیش می رود</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/16700" target="_blank">📅 19:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16699">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش اسراییل دستور تخلیه سراسر جنوب لبنان را صادر کرد!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16699" target="_blank">📅 17:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16698">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">«مسیر ترامپ»: وعده ساخت از سال ۲۰۲۶  وزارت امور خارجه ارمنستان سرانجام زمان‌بندی مشخصی برای پروژه TRIPP اعلام کرد که به «مسیر ترامپ» معروف شده است.  طبق اعلام وزارتخانه در پاسخ به درخواست کتبی SputnikARM، فاز عملیاتی پروژه از سال ۲۰۲۶ آغاز می‌شود.   راستی،…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16698" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16697">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaOQJ3yj7UNg4kYjAYYxU-t9Cr9aVJ6qMnNPaYQBgdxoz09QwYw2aCrDJpzrhArQ7ei1xXvQZbtwOBejhZmRVzLJWrB-nE2tScxik-Y1sDmZo8h_qfSSfNJ9Ndx1J1liuxRR2G0_KGXFw_r4gkBuQ57aNJ4mWd5YopbjH8AvONb7IcqREPq8BG5YbZjGLukB6Rf0SKTPB7-8ZlqrEE-nPJSQIrKYXloiIfiscP_WS_h2JVJ8PuGuyCUxBGXb4dsVS5mp8bZxgutFoJsAladC14ZoIkqifZbFwi9p17LO3Gy-VNsFwubRsQWQVzMGmysx_HWTxSKReFnzzHVo9wzliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسراییل دستور تخلیه سراسر جنوب لبنان را صادر کرد!</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/16697" target="_blank">📅 17:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16696">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ایالات متحده طبق یک نسخه غیررسمی از تفاهم‌نامه، متعهد شده است نیروهای نظامی خود را از مناطق اطراف ایران خارج کند.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/16696" target="_blank">📅 16:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16695">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش‌ها حاکی از آن است که آمریکا و اسرائیل در تلاش برای پایان دادن به قیمومیت اردن بر مسجدالاقصی در بیت‌المقدس و جایگزینی آن با یک نهاد چنددینی تحت کنترل اسرائیل هستند.   این طرح پیشنهادی امکان دسترسی گسترده‌تر یهودیان برای نماز و اعطای نفوذ به اسرائیل بر…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16695" target="_blank">📅 14:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16694">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">این‌گونه_دکترین_نتانیاهو_برای_ایران_فروپاشید.pdf</div>
  <div class="tg-doc-extra">162.7 KB</div>
</div>
<a href="https://t.me/SBoxxx/16694" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه
مقاله Israel Hayom
درباره علل ناکامی عملیات نظامی آمریکا و اسرائیل ضد ایران</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16694" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16693">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCZk1KtWcIo8Vnxgx2jhxtpDrINjOrpZGNM5jBHBgQ6K369sVpcp0n8vHYJf6s2WGjhce4nKPf14Q28HPW38dlQn8b4MEQx0kv5aFPb-G8840ut0p2tSGreyplMwiTT9xGfqYpPRF6uSGeSqPb_rwLuGjts-ZTclwC8za0N3Rr9D5837EYpGCTldgBrW1LA8h2KyVGC2D9dWBWApZ_q27yQicaKzZdoD2hBUzdPq7CO5KPeAawNGC7RE5bb63o7Cx0bc3PXfEoa2vI4ONOPxSXwJE0sEcBlBzACuiNxuqe9EEEycqVKM7ht3xCFb88kPkk8KoT9-JgD59kxdeBRqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گوشه ای از قدردانی کاربران روبیکا نسبت به مسعودپزشکیان پس از بازگشایی اینترنت بین الملل:</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16693" target="_blank">📅 12:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16692">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کره جنوبی قوانین ترانزیت نفت خام ایالات متحده را تسهیل می‌کند  آژانس گمرکی کره جنوبی دوشنبه اعلام کرد که رویه های قانونی واردات نفت خام ایالات متحده که از طریق کشورهای ثالث به کره جنوبی ارسال می‌شود را تسهیل می‌کند تا همچنان واجد شرایط بهره‌مندی از مزایای…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/16692" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16691">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16691" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16690">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWdM4bC-cKeBR3bHk5m0hdB6H_Mph7xCGl6Svtijs4DPlqNllLXSXW94iqkgdLlDnX3zXNahz7BeSLwS-SKBYyuQogebJ_ORWyM0D4QAm5CD4cSd6f8AlB7ez_goGvDs9WhDA1L3EPROp8dI8Mv_YCD2M8wDfmksPPtpWrRP1I8K_H42nIf0Bj4c0Nwudk6EdjBQoZmotL1ItwtiMbghw6X6RRW-QjXStgAUmIfchniipohI_NhnwAaZ_CEaqCGkdjNCwzoL7ZbSES8I4oUy3XY96je3XwF3xB9e-mtTAUplbJ7ssHj03wpUlJQyzu4mfb4VbniL2YPZ089K3ppjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها حاکی از آن است که آمریکا و اسرائیل در تلاش برای پایان دادن به قیمومیت اردن بر مسجدالاقصی در بیت‌المقدس و جایگزینی آن با یک نهاد چنددینی تحت کنترل اسرائیل هستند.
این طرح پیشنهادی امکان دسترسی گسترده‌تر یهودیان برای نماز و اعطای نفوذ به اسرائیل بر رهبری مسجد و خطبه‌های نماز جمعه را فراهم می‌کند</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/16690" target="_blank">📅 09:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16689">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja0IZRRd5DxQgUFqOAqmEixzcbToYC7w6OcSWd4p-u4rEpf4hfjXTI6278F00NeMLDTge6GXhg6Ifcc0kY72A06_gzgbuM7JGL09hgJPGDworDZnv4tFXfqNYiJfIF_jzXpg4VDR5E6EOdZqZ7OoXHRiJ60UyByiCZFUpxF_YOpz2eoCL_CXgJAU18D-w12EoD50iK6vx5SH3Vsrx2OCLlEwmjd__VzKeqLtzy0JW-nLKuvVvd2No9kCjPwF24ZNTpTZR64jizO1rMTztOKv3nlwAkwbblQKpB9zyXKUI495gC_qKOc_IBZqqHrukXBZdb0OPx2Ws7FVSESn07KhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه در حال بررسی محدودیت صادرات گازوئیل و سوخت جت است، زیرا نرخ پالایش به پایین‌ترین سطح چند ساله در پی حملات فزاینده اوکراین رسیده است.
به شرکت‌های نفتی توصیه شده فروش فرآورده‌های نفتی به بازارهای خارجی را محدود کنند. تصمیم برای ممنوعیت صادرات گازوئیل و سوخت جت در مراحل پیشرفته است اما تاریخ آن هنوز تعیین نشده است</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16689" target="_blank">📅 08:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16688">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG4PbQEvy0eWKp9Hc9N_OmgxB0zBGvAuiSuM8Nz9v6oBM-mbzr4cd2zgGr814NcQGX4fymelTBm7ljXA09Bv7izKEQgwCGlQtP8VayxIlxixY0YoCUDzUMRNPrrxoBJI86KT6RoG0PJcc1x20U_RVtSW2MINHT3oKdH8jWRxYQomijgNzj5gAr2VqElNPsy0Oo0HRNoUMToMgLfVYPaI3FPwTJ98uxTVMUGEUQG_2bkyUd7McPIpMLCMXMaQ5zY_iMELxE4FArwZ9BFdfw9rA9kXi8Bbh9kK_nZHy1Q1hEiesCvuZN6zGcnq9kx25kWgeUurOPR9j1eym784UdPstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از درگیری‌های چند شب گذشته در تنگه هرمز و اطراف آن، احتمال ازسرگیری سریع ترافیک عادی در این آبراه حیاتی در بازار شرط‌بندی پلی‌مارکت کاهش یافته است.
اکنون معامله‌گران احتمال بازگشت ترافیک به حالت عادی تا پایان ژوئن را تنها ۴۲ درصد پیش‌بینی می‌کنند</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16688" target="_blank">📅 06:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16687">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpjalvQeGycWNrhor3Jd046jlJmwdTCw1_ffsl6Qh3GEC5XRYKxp-z-OVPcyAeniBC--JIXLUQDRa6SVbEh2O7QAe7GL03kfdtC2_5ORYvBJBwHG3rhissGswsRmjODcMiPGiaM5pu0J6UM4BkyQoFluuRWxrkdkl8jbPBi4PqMqb1lkSNej04cfEaRdXkycF5g_2bXZDorFgR8dPqlZhTlD03gq3TqwfmIZW27MC3F1_MM6GPQf10RGFGjRfDjV8Pe7Q0OwEM5fmsI6QOi39wZp8EZ9BwXkZqDz9zw8UgCtBKy_cXYbJIXRpsRyjPlbaEbQkk-hBnGSTgy3LXohnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:  عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16687" target="_blank">📅 23:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16686">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مملکت خر تو خر</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16686" target="_blank">📅 22:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16685">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFOaHqHdpyQTFN2WSz09U7D2IJDxwqZ7abKcSYxMbjB0a3tS7tuvHyRiMGllkuEIdYG5-AnS4FaYoElSE_RjfQyqghKSW5rpTRPYAIjOiW8GXstBqEb7SjXEZY0Ss0GciIOc0u-M6-M6GJEHuORdLWGRnbyRM-IMdUWQCEFCXVNpz-eMy5XT4Xr8wHi8h47XKG8FAzYp8MllMJtisEtkN5SMzZ0UWhGvPccrVH-51dSLrJDsMzcZmRBdMP9nD6QCpeT4bAW2kZDZVBIep9L5lomGdGzdE7Hr2KeZD7CAG34g6pM7bMEK0-sjSvZk5u6kcJnPkzLAvk6jlBIbcP5wFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانه پدافندی کوتاه‌برد ایرانی «مجید» در رژه نظامی ارمنستان در ایروان به نمایش درآمد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16685" target="_blank">📅 22:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16684">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45eb7047af.mp4?token=iR8QNUkBbE1XpNwMR9cLZlq7YUG8DPbx_xnl6jb0ykuNFN3iFR-UCM0yz7BPJTcOJYz2JKhZSlbEndJaaWB2wP1Ami3k5XLivgo8kIK_YDKSj0NBVqdhkhElZBlYlF3IGd6kBFdHdFaf1YFPZTlyfkDYpjc-2W0bqqnkRE5EpIPfHNIt-hRf7hkA8pLjmvvjzA7aJFC_lyjrBsxOtNA409pPwlgW9hHs3aH1ZQGk9a407Tm5E8k9fKjpMfkv2d9ju_KJoJV_8wHe8Dm0M8Lsmy1deuhk8f3KNpvd4f3iRfDoPtYdFZB1Ue_njCMQTMqdp-ozUEF8sJ4XpLfFp7K9OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45eb7047af.mp4?token=iR8QNUkBbE1XpNwMR9cLZlq7YUG8DPbx_xnl6jb0ykuNFN3iFR-UCM0yz7BPJTcOJYz2JKhZSlbEndJaaWB2wP1Ami3k5XLivgo8kIK_YDKSj0NBVqdhkhElZBlYlF3IGd6kBFdHdFaf1YFPZTlyfkDYpjc-2W0bqqnkRE5EpIPfHNIt-hRf7hkA8pLjmvvjzA7aJFC_lyjrBsxOtNA409pPwlgW9hHs3aH1ZQGk9a407Tm5E8k9fKjpMfkv2d9ju_KJoJV_8wHe8Dm0M8Lsmy1deuhk8f3KNpvd4f3iRfDoPtYdFZB1Ue_njCMQTMqdp-ozUEF8sJ4XpLfFp7K9OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
خبرگزاری CNN :  کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16684" target="_blank">📅 22:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16683">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭕️
فضای دیجیتال ایران ، پس از تجربه طولانی ترین خاموشی سراسری اینترنت تاریخ مدرن جهان ، از امروز به صورت تدریجی درحال برگشت به حالت قبل و فیلترینگ مدیریت شده است</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/16683" target="_blank">📅 21:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16682">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گویا آمریکایی ها عملیات اسکورت کشتی ها در تنگه هرمز را از سر گرفته اند</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16682" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16681">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62edae59af.mp4?token=UG83a7QrDmn-JkIs5oARNi20HNou3kPJ6GuWfnJ7BMNDfD99yEw3TTo6u26RqHZDLJlmxjUyXe7ULOAjwu2NJDJdcEtKcb-ccTkFbPK_ZYE9J-_SzvXfwqWQp-tXPHdeRlY65_1YVvRSq-7giXqSVENwXUn0JZROX4Rrxgfwzs5QB7GY-Pz-0Td9GNPs_brqh9NR8W0dbKJvp66gD-n96DtLXqeXiDxoaP3AxQgxVdhh8ZEtEWX_eUvk8O-p9LDg0Iy_Othgw9rRbuN1W6vebY27pCnZBikeNmIw4GKVCeM2D1upzsGoP8lI37anZ6MWEGAw2aBwVhVV9YK6H0MMvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62edae59af.mp4?token=UG83a7QrDmn-JkIs5oARNi20HNou3kPJ6GuWfnJ7BMNDfD99yEw3TTo6u26RqHZDLJlmxjUyXe7ULOAjwu2NJDJdcEtKcb-ccTkFbPK_ZYE9J-_SzvXfwqWQp-tXPHdeRlY65_1YVvRSq-7giXqSVENwXUn0JZROX4Rrxgfwzs5QB7GY-Pz-0Td9GNPs_brqh9NR8W0dbKJvp66gD-n96DtLXqeXiDxoaP3AxQgxVdhh8ZEtEWX_eUvk8O-p9LDg0Iy_Othgw9rRbuN1W6vebY27pCnZBikeNmIw4GKVCeM2D1upzsGoP8lI37anZ6MWEGAw2aBwVhVV9YK6H0MMvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🙌
@TweetyChannel
| علیچی</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/16681" target="_blank">📅 19:06 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
