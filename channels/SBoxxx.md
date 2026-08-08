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
<img src="https://cdn4.telesco.pe/file/t7FhTv1KmtKa1IUFLCUpfxEHhHJef8GZrlRJVi5hP6R89rZ1v9b6B1lXcWKriyr6-kyNgSaQIJvLOrSwpr7qIZ28iHG1orMENuVbTh4m_tRRN5_qOYuuKKF88CbKIhV2srua8k4GTTmmmqyEYF29lzXhBp5BbDWYm0iWSKCwOuMmtgNYk6IKXhsy-qOApGXc67gmPGOOLfnaQAPViDS5HKyAVwXCe_-qbLcueveL-LoeMDc8a9Vtw5h0Ad4T2vDLAJ2ESLNl8MNOxFglDJLrX5Qg-LkUOsScj4HxAG0VT4vLaKG9MBPuASBjkQp0UE-j7uMh2WPVe6xj-qXOWG3hQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 16:56:40</div>
<hr>

<div class="tg-post" id="msg-19802">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسرائیل و کلمبیا پس از به قدرت رسیدن رئیس‌جمهور جدید در ۷ اوت، روابط دیپلماتیک و اقتصادی خود را به طور کامل بازسازی خواهند کرد.  دو کشور سفیر تعیین خواهند کرد، الزامات ویزا را لغو می‌کنند و کلمبیا قصد دارد سفارتی در اورشلیم افتتاح کند.  منبع: i24</div>
<div class="tg-footer">👁️ 310 · <a href="https://t.me/SBoxxx/19802" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19801">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امارات متحده عربی اعلام کرد که یک تانکر نفتی متعلق به شرکت ملی نفت ابوظبی (ADNOC) که امروز در حال عبور از تنگه هرمز بود، مورد اصابت موشکی قرار گرفت.
این، چهارمین حمله ایران به یک تانکر اماراتی در این هفته است.</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SBoxxx/19801" target="_blank">📅 15:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19800">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رئیس جمهور صربستان، الکساندر ووچیچ:
ما قصد داریم یک کارخانه تولید پهپاد در اینجا در ماه سپتامبر افتتاح کنیم، اما این کار را با همکاری شرکت‌های اسرائیلی انجام خواهیم داد. ما این کار را با اسرائیلی‌ها انجام می‌دهیم.</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SBoxxx/19800" target="_blank">📅 15:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19799">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بشدت به همین سناریو که 2 ساعت پس از آغاز جنگ اشاره کردم، ایمان آورده ام. تقریباً تردیدی برایم نمانده که مدل «فروغ جاویدان» صدام را این بار نتانیاهو با پژاک و گروههای مشابه ش میخواهد اجرا کند.  نکته بدتر اینکه در صورت موفقیت این طرح و با ورود نیروهای شبه نظامی…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/19799" target="_blank">📅 14:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19798">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">این ژاپن بزودی بدجور موی دماغ چین خواهدشد.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/19798" target="_blank">📅 13:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19797">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iauS3Esw1qSkqil29lBv2YBZLsCD4Ytglt4TYvb5VCBZem0lPGpVutxTWBHFIx_NRHD3VLAn-qxO2aZAzmdtFfKzSbd-G0RiXFXG5ey1QIZ4GHrZWI9OT2IxnR41UR5oCcueaBkpbhOmiuGqFojWfJoJGCKwYVgHKbryNVxhj6OGRQVtnfkPx8TU4PYuW4lVnF3TaW8bUBzTuCS0DSR8sbDbREcCfQD1jbX8583FpzTbpTnx-KS1ZznfFFZ0ZZl4figu32LPL2oCim_rBwoURnpmvuPqSm9FQSxo-nD-WjIM3k_NTwQs6VZO3bSyWCktbSG4GdhubMExAsEDN6L24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟
در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در نگاه نخست می‌تواند یک راهکار جذاب برای دور زدن محدودیت‌های دریایی و کاهش وابستگی ایران به مسیرهای صادراتی سنتی باشد. با این حال، بررسی دقیق ظرفیت‌های فنی، اقتصادی و لجستیکی نشان می‌دهد که راه‌آهن هرگز نمی‌تواند به‌طور کامل جایگزین صادرات نفت دریایی ایران شود؛ اما می‌تواند به‌عنوان یک مسیر پشتیبان، بخشی از درآمدهای نفتی تهران را حفظ کند و اثر تحریم یا محدودیت‌های دریایی را کاهش دهد.
نخستین نکته مهم، تفاوت عظیم میان ظرفیت حمل‌ونقل دریایی و ریلی است. صادرات نفت ایران پیش از تشدید محدودیت‌ها عمدتاً به چین انجام می‌شد و حجم آن در مقاطع مختلف حدود ۱.۴ تا ۱.۸ میلیون بشکه در روز برآورد شده است. انتقال چنین حجمی از طریق راه‌آهن نیازمند زیرساختی بسیار فراتر از ظرفیت فعلی شبکه ریلی منطقه است.
یک نفتکش بزرگ VLCC می‌تواند بیش از 2 میلیون بشکه نفت را در یک سفر جابه‌جا کند، در حالی که یک قطار نفتی معمولی بسته به ساختار واگن‌ها حدود ۲۰ تا ۷۰ هزار بشکه نفت حمل می‌کند که اگر سقف این محدوده یعنی 70 هزار بشکه را هم درنظر بگیریم، در روز به حدود 25 قطار نیاز است تا معادل یک روز معمولی صادرات نفت به چین حمل کند. بنابراین برای جایگزینی صادرات دریایی ایران، باید روزانه ده‌ها قطار نفتی در مسیرهای طولانی بین ایران، آسیای مرکزی و چین حرکت کنند؛ موضوعی که با ظرفیت فعلی خطوط ریلی، پایانه‌ها، گمرک‌ها و مرزهای زمینی منطقه عملاً امکان‌پذیر نیست.
در مورد مسیر افغانستان نیز باید میان «امکان راهبردی» و «واقعیت عملیاتی» تفاوت قائل شد. ایران هم‌اکنون دارای اتصال ریلی به افغانستان از طریق خط آهن خواف–هرات است، اما مسیر کامل ایران به چین از خاک افغانستان هنوز یک کریدور تجاری با ظرفیت بالا محسوب نمی‌شود. بخش‌هایی از طرح‌های اتصال افغانستان به آسیای مرکزی و چین همچنان در مرحله توسعه قرار دارند. بنابراین افغانستان در آینده می‌تواند به یک پل زمینی مهم تبدیل شود، اما در شرایط فعلی توان انتقال میلیون‌ها بشکه نفت ایران را ندارد.
مسیر واقع‌بینانه‌تر در کوتاه‌مدت، استفاده از شبکه ریلی ایران به سمت ترکمنستان، قزاقستان و سپس چین است. این مسیر از نظر زیرساختی نسبت به مسیر افغانستان آماده‌تر است، اما همچنان با محدودیت‌های جدی مواجه است. یکی از مشکلات اصلی، تفاوت میان محل تولید نفت ایران و محل مصرف در چین است. بسیاری از خریداران اصلی نفت ایران در چین، به‌خصوص پالایشگاه‌های کوچک موسوم به «تی‌پات‌ها» در استان شاندونگ، در مناطق ساحلی قرار دارند؛ در حالی که مسیرهای ریلی زمینی بیشتر به مناطق داخلی چین دسترسی دارند. بنابراین حتی رسیدن نفت ایران به خاک چین لزوماً به معنای حل مشکل انتقال آن به پالایشگاه‌های مصرف‌کننده نیست.
با وجود این محدودیت‌ها، نباید نقش اقتصادی صادرات ریلی را دست‌کم گرفت. هدف ایران احتمالاً جایگزینی کامل صادرات دریایی نیست، بلکه ایجاد یک «حداقل جریان صادراتی» برای جلوگیری از قطع کامل درآمدهای نفتی است. حتی انتقال ۱۰۰ هزار بشکه نفت در روز با قیمت ۶۰ تا ۷۰ دلار، می‌تواند سالانه بیش از دو میلیارد دلار درآمد ناخالص ایجاد کند. اگر این رقم به ۲۰۰ یا ۳۰۰ هزار بشکه در روز برسد، اهمیت اقتصادی آن برای کشوری تحت تحریم بسیار بیشتر خواهد شد.
البته هزینه انتقال ریلی بسیار بالاتر از حمل دریایی است. نفت باید از مناطق تولیدی جنوب غرب ایران به پایانه‌های ریلی منتقل شود، سپس از چند مرز عبور کند و در مسیر با هزینه‌های گمرکی، تغییر استانداردهای ریلی، بیمه و ریسک تحریم مواجه شود. به همین دلیل، نفت صادراتی از مسیر زمینی احتمالاً با تخفیف بیشتری نسبت به نفت دریایی فروخته خواهد شد.
از همین رو، راهبرد منطقی‌تر برای ایران شاید انتقال مستقیم نفت خام نباشد، بلکه تبدیل نفت خام به محصولات با ارزش افزوده بالاتر مانند فرآورده‌های نفتی، سوخت‌ها و محصولات پتروشیمی و سپس انتقال آنها از طریق راه‌آهن باشد. حمل محصولات با ارزش‌تر، از نظر اقتصادی بسیار توجیه‌پذیرتر از انتقال میلیون‌ها بشکه نفت خام با قطار است.
در نهایت، اهمیت اصلی این پروژه بیشتر ژئوپلیتیکی است تا صرفاً اقتصادی. هدف ایران احتمالاً ساخت یک شبکه جایگزین برای جلوگیری از تبدیل شدن تحریم دریایی به یک ابزار خفه‌کننده کامل است. اگر تهران بتواند حتی بخشی از صادرات خود را از مسیرهای زمینی حفظ کند، اثرگذاری فشارهای دریایی کاهش خواهد یافت. در این شرایط، تحریم یا محاصره دریایی دیگر به معنای توقف کامل صادرات نفت ایران نخواهد بود، بلکه تنها هزینه و دشواری صادرات را افزایش می‌دهد.</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/19797" target="_blank">📅 12:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19796">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUAOcz10u-uV8R_m11buX_Vr929ZfI2Iyb3CU_lakKWaQL1Eye39PJhtd0_jljfKaQ9-GZdtx7Idwp7NqrGwQHYU8u_pwpLbub3R7USVPrMRIO4633FyVjHS3pZ7DFGXbthulSGnS0u_g3UJRbClt7Si-Gcya_i5XUw_U4uEBeS39O9dI6xt4LSPSxgyl7j00Af6zeOAIUxeP03vSh7L0fW_z6ndsV0XzWJrWaduve7Omb7T9D-PDt0X3vWg1WIxvHPvgmZYoT3j5DRyr2WOXyNhk1xPZeWeepfqCgr4Yh8ZyvGp6YpPE2BGKM9JpvhPGr12mMMIXO12HHiteRasMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد که البته بخشی از آن به دلیل تقویم اقتصادی (گزارش NFP) است.  انتظار یک افت اصلاحی در طلا می رود.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/19796" target="_blank">📅 12:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19795">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سوال خبرنگار:   مانند مه ۲۰۲۵، زمانی که وضعیت جنگی بین هند و پاکستان وجود داشت، آیا ترکیه و عربستان سعودی فقط حمایت کلامی ارائه می‌دادند اگر چنین چیزی دوباره اتفاق می‌افتاد، یا با سلاح از پاکستان حمایت می‌کردند؟  وزیر دفاع پاکستانی عساف: هر چه این توافق‌نامه…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/19795" target="_blank">📅 12:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سوال خبرنگار:
مانند مه ۲۰۲۵، زمانی که وضعیت جنگی بین هند و پاکستان وجود داشت، آیا ترکیه و عربستان سعودی فقط حمایت کلامی ارائه می‌دادند اگر چنین چیزی دوباره اتفاق می‌افتاد، یا با سلاح از پاکستان حمایت می‌کردند؟
وزیر دفاع پاکستانی عساف: هر چه این توافق‌نامه شامل می‌شود، قطعاً به حوزه عمومی خواهد رسید. همان‌طور که قبلاً گفتم، قطعاً به عرصه عمومی آورده خواهند شد.
اما این توافق‌نامه تنها امروز امضا شده است و فکر نمی‌کنم مناسب باشد که در حال حاضر جزئیات آن را بحث کنم.</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/19794" target="_blank">📅 11:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VffoJk5VQHAUhEac4FjGo9JaLolq3AghUuE1yDcq5gp6PLOkpS0FhTQbpiOMiQ-CtYNd0EibCKsf2Cjjancb1AURTczy0V6f0G0EA9PrCN8VOP9KKvL51ishEOJlizWuWvd1mT5beQDA4NLHcOWV7SOyeelMKwJ3yEyEn0zWs_Un3nNsNL8B79o7wSLd-5im4n_VqeS3wA7MWES5o9yn2ILzhDqbX3TMgoPJpVqe6KW20t25vVcCjG36IjFQ5XJQ92bLQoGj6cY9eTJyW6IKWLauyTwVNQEs3r_9SMihk2Vg3uiVSJDzzYgtWtmPvzdZJjymiWBRRh9NF2pt8mxF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده توانسته صادرات نفت ایران را فلج کند – فایننشال تایمز
این روزنامه با استناد به داده‌های ماهواره‌ای گزارش می‌دهد که ایران حدود یک هفته است که در جزیره خارک نفت خام را در نفتکش‌ها بارگیری نکرده است.
این جزیره اصلی‌ترین پایگاه ترانزیت نفت کشور است. اسکله‌های بارگیری خالی هستند و ترافیک نفتکش‌ها متوقف شده است که نشان‌دهنده طولانی‌ترین دوره بی‌فعالی در مجتمع ترانزیت جزیره خارک از آغاز جنگ است</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19793" target="_blank">📅 07:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مقام آمریکایی گفت که توافق مربوط به بازگشایی تنگه هرمز نهایی شده و در مقابل محاصره دریایی ایران نیز برداشته می شود</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19792" target="_blank">📅 01:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19791">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس‌جمهور ایران، مسعود پزشکیان:
من نه تنها از شهادت نمی‌ترسم، بلکه آن برای من یک پیروزی بزرگ است.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19791" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19790">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">402.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19790" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 21</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19790" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19789">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رسانه های اسراییلی:
محسن رضایی جزو اهداف ترور است.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19789" target="_blank">📅 20:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در عصر اقتصاد دانش بنیان، تنگه بندی و گردنه گیری تنها منجر به انزوا و تیپا خوردن خود عامل می‌شود و اندونزیایی ها خیلی سریع فهمیدند که این لقمه برای دهانشان بزرگ است ولی خب.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19788" target="_blank">📅 19:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انصافاً ببینید کشورهای منطقه (خصوصاً عراق و کویت که راهی جز هرمز برای صادرات نفت ندارند) برای گریز از اخلال ایران در هرمز چه می کنند.  خط لوله کرکوک—جیحان که الان هم فعال است.  خط لوله شرق—غرب عربستان به ینبع برای خود سعودیها فعال است و گویا عراقی ها و کویتی…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/19787" target="_blank">📅 19:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVxLlwFHwUCjqiMhCllb3j8TwY6repdRYJL8S5nzU8UxYMqgBRh7woxx98XibAZLqQ5rZzZ_lbzYPON3cVvef_otFRZNfmr2meYoyDpqbv9VFtLnm4N-Ys9cL7XVinWM4duuO9wyx3e6GiiNBuz_vLQFDs4YmH8d3xdj-_IfqBA2ybk8sOkRS9uwbVDdJ73tOkg7zYw8Q47Mg-UKm_vrPWFMSQtljGFoxsKwQdckrD7G2Us5-1tS30R6Asp0wSfaxcS4xAA0PwagibxycBkrz0CoWsq-BGCwX-ANFvA5h7zyHKz0CfMpmWf0Tl-B-ErhKvZjs3HHLkom8suUvseWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#VIX
با شاخص های سهام در سقف و نفت کنترل شده، همه چیز برای ماجراجویی دوباره ترامپ آماده است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19786" target="_blank">📅 19:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19785">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VviX_gtYT2zcytMnLujQbDF_jXpwHVFfrmvJsy4qOIyTRX1WCaO5aTdTxRidsnJr5nmX1-jfLxsWH44Z3TUGeV2Bz72qWyKseGT4CTmAKCe4jD7-TEALu4uRhqiVh87uIkPR6MGk7O5ggXaleTA5hcjeGgFAGa4pBdpKb61s8dwo37cna66K1l74eJWNzrQgBEp9GcGV1KFckE9hlxU4O-podr4OgK9SPCbwqLnEkXuWyZg7Q4fUvdqjr-YFZ3oIo1PHJzBn4QGb29ow3ysgTcR0LuWhHbGYMXcq04Jb4qaKRbuZETaU_tgnWODXbjc4P4KQIU68BvzH8n2-cO9_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD — H4  میتوان چنین ساختاری برای طلا متصور بود.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19785" target="_blank">📅 19:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ریاست جمهوری ترکیه:   هرگونه حمله مسلحانه به هر یک از کشورها، از جمله ترکیه، عربستان سعودی و پاکستان، حمله به همه آنها تلقی می‌شود</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19784" target="_blank">📅 18:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMkWA7TqdXNkb-msjKqL2PFcuDGoR1vI1v2AS2OYCperHpT2eVC7WR2rZXlGSlrTAB36tpRETBV7TrnApE02yeZ1AKMiPKO5Iv1Yd2BGt3k-LF42XrDKZlpqct2cKZy7OpA6G1bpSs5ezm1vWBjUqTIWRfuRrf4xVoms3aIlstrl_5fsVzCq8482Z31DuDlIp_dKk2fSZ7-UZwrtN5rUKN12ZzcwcHf4VtIRCoAxeXeegsx_nDdnziS870B7u0Z8GoRyysB08OrGndIUFYV1tLebb_sHV3pNZvL8u-M-QlF25qW1HmJ5sK6HZXauLUjG2zbULkpGvZd6DyZn3xihMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریاست جمهوری ترکیه:   هرگونه حمله مسلحانه به هر یک از کشورها، از جمله ترکیه، عربستان سعودی و پاکستان، حمله به همه آنها تلقی می‌شود</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19783" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">💙
تبریز
💙</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19782" target="_blank">📅 17:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اسکات بسنت در مورد ایران:
ما آن‌ها را از گلو گرفته‌ایم و آن‌ها تورم غذایی ۱۵۰ تا ۱۸۰ درصد دارند و نمی‌توانند به سربازان حقوق بدهند.
فکر می‌کنم به زودی، شاید حتی امروز یا فردا، قرار است یک توافق را ببینیم، یک آتش‌بس ۳۰ تا ۶۰ روزه و تنگه باز خواهد شد.
قیمت‌های انرژی باید کاهش یابد.
منبع: 12 News</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19781" target="_blank">📅 17:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تحلیلی برگریزان از خرازی درباره پاکستان، هند و چین!</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19780" target="_blank">📅 15:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b35e228b4.mp4?token=Bg53vp1VTpjas3K1lsXRv_0ddaS0FW3XxaQU7OF3ScgFldg4U0dFS8XnaUjFDJWPYsUGdKq_ovK76pHacYCdsCii7hJJrnwZKP7svMPsmBIv91BgRNM6iUj1_15jfNLcuyRwJ3IJVbNJNhEl-8n39Yj5K73OL5Uo_il6OT6v4IcgcWdlqMhLU2R-oRtKSKIvoGyUNtr8RD7p-a1_KT1D5LhTeKkSIQAT8yub-rV5x-pACVPaOj-KKWiQvTurAniQ4Xj66AbqlD6RkvR5uHqEnqHD0stzFQe1di1g6P8f7mKl-vR0aRzeJyKTID2uWl9ot9dnu-qsvdRgubuDsrVZqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b35e228b4.mp4?token=Bg53vp1VTpjas3K1lsXRv_0ddaS0FW3XxaQU7OF3ScgFldg4U0dFS8XnaUjFDJWPYsUGdKq_ovK76pHacYCdsCii7hJJrnwZKP7svMPsmBIv91BgRNM6iUj1_15jfNLcuyRwJ3IJVbNJNhEl-8n39Yj5K73OL5Uo_il6OT6v4IcgcWdlqMhLU2R-oRtKSKIvoGyUNtr8RD7p-a1_KT1D5LhTeKkSIQAT8yub-rV5x-pACVPaOj-KKWiQvTurAniQ4Xj66AbqlD6RkvR5uHqEnqHD0stzFQe1di1g6P8f7mKl-vR0aRzeJyKTID2uWl9ot9dnu-qsvdRgubuDsrVZqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلی برگریزان از خرازی درباره پاکستان، هند و چین!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19779" target="_blank">📅 15:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارتش یمن بیانیه مهمی صادر می‌کند
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد که نیروهای مسلح این کشور به زودی بیانیه‌ای درباره عملیات منحصر به فرد نظامی خود صادر می‌کند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19778" target="_blank">📅 15:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19777" target="_blank">📅 15:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نکته جالب اینکه مهلت حشدالشعبی به دولت عراق فردا پایان می یابد و یمنی ها هم حملات خود را به سعودی تشدید کرده اند!  یعنی اگر فردا این پیمان دفاعی میان ترک‌ها و پاکستانی ها و سعودی ها امضا بشود، از پسفردا باید شاهد حملات متقابل اینها به حشدالشعبی و حوثی ها باشیم.…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19776" target="_blank">📅 15:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ماده اصلی توافق مکه یک بند دفاع جمعی است.  هر حمله مسلحانه علیه یکی از این سه کشور به عنوان حمله علیه همه آنها تلقی می‌شود.  هدف آن تقویت بازدارندگی جمعی در برابر تجاوز و تقویت همه جنبه‌های همکاری دفاعی میان این سه کشور است.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19775" target="_blank">📅 14:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نکته جالب اینکه مهلت حشدالشعبی به دولت عراق فردا پایان می یابد و یمنی ها هم حملات خود را به سعودی تشدید کرده اند!  یعنی اگر فردا این پیمان دفاعی میان ترک‌ها و پاکستانی ها و سعودی ها امضا بشود، از پسفردا باید شاهد حملات متقابل اینها به حشدالشعبی و حوثی ها باشیم.…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19774" target="_blank">📅 14:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19773">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها می‌خواهند معامله‌ای انجام دهند. ببینید، واضح است که نمی‌خواهند مورد حمله قرار بگیرند. آن‌ها می‌خواهند معامله‌ای انجام دهند. بنابراین، خواهیم دید.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19773" target="_blank">📅 13:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19772">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 21</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 21
جمعه 7 آگوست 2026</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19772" target="_blank">📅 13:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پیشروی بی سابقه حزب AfD در آلمان
حزب موسوم به گزینه جایگزین برای آلمان در نظرسنجی‌ها به بالاترین حد تاریخی خود یعنی ۲۸ درصد رسید و فاصله خود را با ائتلاف CDU/CSU افزایش داد، در حالی که حمایت‌های محافظه‌کارانه به پایین‌ترین سطح خود از سال ۲۰۲۱ سقوط کرد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19771" target="_blank">📅 13:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19770">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgHznJOgVHJctobDKN8TeFM03_St5uGd1M3-w7t184FTdiZJza9DPvfu2Kj0BVhIudcHtZYQuRG_O81G2SjR8x63YAWIGAEYxOzJ0qcaZdEcfW5g--V0bc8XMbpgr_1RONN_xPE_Wq0G1vy7v4dz1f-bi1-gMYbLIMLjapn47Vnx0nuShzFl5ER0wrn76YMnCvTROQJaQswrKKOr9iHihYpEkVukfS37-3hKmKpRs-XB_RNOzY9sFSoXPdcEGjSdoO7jp1rS1xAApbcnZvPcwwXJsFBkEOmBwnvj05EPkYEbCj4niFhLq32aAJgM6fNWCYAUg5omMky66GttucvRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد که البته بخشی از آن به دلیل تقویم اقتصادی (گزارش NFP) است.
انتظار یک افت اصلاحی در طلا می رود.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19770" target="_blank">📅 11:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مسئول ارشد سابق در پنتاگون و مدیر ارشد در مرکز اسکروفت در مورد ذخایر تسلیحاتی ایالات متحده:  «محاسبات مربوط به مهمات برای ایالات متحده بسیار جدی است،» او گفت. «با هر عملیات هوایی علیه اهداف ایرانی و حملات تلافی‌جویانه بعدی ایران، ایالات متحده توانایی‌های حیاتی…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19769" target="_blank">📅 11:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDDh12GTCoscDN9_lBzdG3g5Eo5iCxyuZBdRiuaOoI3ikJXvOCyTlZBJcjtZL6rJwi1mGkmvE4G6RUl01o0Gb8WHVgNXysFJrbtVNhBrbnhW-eTR2A_xawlyPFkliVLsUkYkWSDTdiaKqm2oF0BY9C0LEIYVPFQqlVABkHTqF7gfVuXn6lyAxUMy0ZNTN3LzERZBN913G3P6XI4GhoeYp0-OPzjuKyRHZJzkQfd-YUxEw2lDxB2smNSWnzxha4eLHyUBOLDkyhYJQXTP2iJNyQm_rVuc5k2FdmB4TUrEPX6KV0Sc5mAVFPaiJQHSSmsQd6MfrotU8r0-hDvlmvjI3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه قرار دارد. پیش بینی می شود طلا امروز مقداری افت اصلاحی داشته باشد (با توجه به رشد GRI از دیروز) اما دوباره به سقف (4300) حمله ور بشود (با توجه به افت میانگین شاخص GRI در روزهای گذشته)</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19768" target="_blank">📅 11:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19767">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزارت دفاع آمریکا، قرارداد ۵۸ میلیارد دلاری برای سیستم پدافند هوایی پاتریوت به شرکت لاکهید مارتین اعطا کرد.  این قرارداد به ارزش تا ۵۸.۶ میلیارد دلار، مربوط به موشک‌های رهگیر پاتریوت است و تولید این سیستم را تا سال ۲۰۳۲ افزایش می‌دهد. این اقدام در حالی صورت…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19767" target="_blank">📅 11:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نکته جالب اینکه مهلت حشدالشعبی به دولت عراق فردا پایان می یابد و یمنی ها هم حملات خود را به سعودی تشدید کرده اند!  یعنی اگر فردا این پیمان دفاعی میان ترک‌ها و پاکستانی ها و سعودی ها امضا بشود، از پسفردا باید شاهد حملات متقابل اینها به حشدالشعبی و حوثی ها باشیم.…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19766" target="_blank">📅 03:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترکیه، عربستان و پاکستان در آستانه امضای پیمان دفاعی سه‌جانبه   رجب طیب اردوغان، رئیس‌جمهور ترکیه، روز جمعه راهی عربستان سعودی می‌شود تا در نشستی سه‌جانبه با محمد بن سلمان، ولیعهد سعودی، و شهباز شریف، نخست‌وزیر پاکستان، یک توافق دفاعی مشترک را به امضا برساند؛…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19765" target="_blank">📅 02:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19764">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عجیب است!  الان دیدم در 17 مارس امسال — یعنی اوج جنگ 40 روزه — پنتاگون در حال نهایی کردن طرح استفاده از کلاهک های کوچک هسته ای به عنوان یک گزینه معمول جنگی (با حساسیت کمتر نسبت به جنگ تمام عیار هسته ای) بوده است.  لینک</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19764" target="_blank">📅 02:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoJcd1pZ3i5ufdJR5LsmbfEl_wJWvp-4pizU6DI2goaXFyLA8h1EapfRCEVV7Q-xDVTuOuGrh1Wvo-hliZXqtTbrRSZxCRV8sbBB1-FZyzJjLZSvTXatbrwt13XR9D9Pr4f-KEED01kqvfll53oaYkgCmvO7JXrzc87qiimLEAVPyd15hP4nsMWr0zCzOTLZm2PBw7y--uDcwnBUME1w63r5nr13mQ5gNFlgvdjlP2GGr6Gk4xG6XOX2goNIw7n4GkC2uunqWN6I_qhzls24sc1wQxW-8yROsD0kzpD13KiD0mJk7VjAyne8n0DAvKqUuwnQVyOE9LWQ9UIr1J6g3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19763" target="_blank">📅 02:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19762">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترکیه، عربستان و پاکستان در آستانه امضای پیمان دفاعی سه‌جانبه
رجب طیب اردوغان، رئیس‌جمهور ترکیه، روز جمعه راهی عربستان سعودی می‌شود تا در نشستی سه‌جانبه با محمد بن سلمان، ولیعهد سعودی، و شهباز شریف، نخست‌وزیر پاکستان، یک
توافق دفاعی مشترک
را به امضا برساند؛ توافقی که می‌تواند به شکل‌گیری یکی از مهم‌ترین ترتیبات امنیتی جدید در خاورمیانه منجر شود.
این توافق سه‌جانبه که بنا بر گزارش رویترز قرار است در جریان دیدار رهبران سه کشور نهایی شود، در شرایطی شکل می‌گیرد که جنگ ایران و افزایش بی‌ثباتی در منطقه، معادلات امنیتی خاورمیانه را وارد مرحله تازه‌ای کرده است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19762" target="_blank">📅 02:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19761" target="_blank">📅 01:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19760" target="_blank">📅 00:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فرانسه یک پیشنهاد  را به هند ارائه داده تا یک توافق دولتی-دولتی برای خرید ۱۱۴ فروند جنگنده "رافال" برای نیروی هوایی هند، به ارزش تقریبی ۳.۲۵ تریلیون روپیه (حدود ۳۴ تا ۳۹ میلیارد دلار) منعقد شود.
بر اساس این طرح پیشنهادی، حدود ۲۰ فروند از این هواپیماها مستقیماً از فرانسه به هند ارسال خواهند شد تا نیازهای فوری برطرف شوند، در حالی که ۹۴ فروند دیگر در هند تولید خواهند شد.
یکی از اولویت‌های اصلی هند، ادغام سلاح‌های تولید داخل، به ویژه موشک هوایی به هوایی "آسترا" است.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19759" target="_blank">📅 00:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به گزارش بلومبرگ، یک مقام ارشد سعودی اعلام کرد که گزارش‌های اطلاعاتی معتبری وجود دارد که نشان می‌دهد حوثی‌ها، شبه‌نظامیان عراقی و سپاه پاسداران انقلاب اسلامی ایران در حال هماهنگی برای انجام حملات به عربستان سعودی هستند.
این منبع، این گزارش‌ها را "شگفت‌انگیز" توصیف کرد، زیرا این موضوع در حالی مطرح می‌شود که ریاض در تلاش برای کاهش تنش‌ها است و مدعی است که مذاکرات به طور مثبت پیش می‌رود.
این منبع همچنین افزود: "عربستان سعودی در اتخاذ تمام اقدامات لازم برای پاسخ به هرگونه تجاوز، تردید نخواهد کرد."</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19758" target="_blank">📅 00:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پس از خلع سلاح نیروهای وابسته به دولت اشغالگر ترکیه (انحلال سازمان تروریستی ارتش ملی سوریه)، اظهارات خشمگینانه ای از سوی «وزیر خارجه» ترکیه، هاکان فیدان (Hakan Fidan) صادر شد:   «کلیه عناصر مسلح در سوریه موظف به تحویل سلاحهای خود هستند.»</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19757" target="_blank">📅 23:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پس از خلع سلاح نیروهای وابسته به دولت اشغالگر ترکیه (انحلال سازمان تروریستی ارتش ملی سوریه)، اظهارات خشمگینانه ای از سوی «وزیر خارجه» ترکیه، هاکان فیدان (Hakan Fidan) صادر شد:
«کلیه عناصر مسلح در سوریه موظف به تحویل سلاحهای خود هستند.»</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19756" target="_blank">📅 23:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شنیده شدن انفجار در قشم و بندرعباس</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19755" target="_blank">📅 23:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiqqY8LTvEAQ6L_xeJ_WVDz-o7cfeEHAPg_7rbav8aQQndFj_P32KyrIukNnycvgShUex6sr4LvlLTSGRzprgiHbxAQtF8ZUG-RkxOHpAU_Ap0w5E8wHWzjWfoLSMU5CTqiEOobXYora5bcKWYxuRvpE8UpnL97hVMQtJVyAuEfOigMKZr4QXovloe19rNaX1gnhReKP2mpoUEg7cLJ2q0YFOfvehoH-muLJG8TerjlYppcgcogymkywVeLRsOwCpLpO36EkVsQfiMD2SmvsVxygvpjcFBt0BBYttZqLO_caunVlXFYx0OuF6Dq_uVRIKT0TkpcePfLBrkkDWtnonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19754" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شنیده شدن انفجار در قشم و بندرعباس</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19753" target="_blank">📅 21:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">منابع فلسطینی گزارش می‌دهند که حماس، واحدهای سازمانی، فعالیت‌های مخفیانه و عملیات امنیت سایبری خود را به ترکیه منتقل می‌کند، در حالی که قطر به میزبانی رهبری این سازمان و فعالیت‌های عمومی آن ادامه خواهد داد.  — روزنامه جروزالم پست</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19752" target="_blank">📅 21:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انصافاً ببینید کشورهای منطقه (خصوصاً عراق و کویت که راهی جز هرمز برای صادرات نفت ندارند) برای گریز از اخلال ایران در هرمز چه می کنند.  خط لوله کرکوک—جیحان که الان هم فعال است.  خط لوله شرق—غرب عربستان به ینبع برای خود سعودیها فعال است و گویا عراقی ها و کویتی…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19751" target="_blank">📅 21:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19750">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIXIV2jdbqc2Qqkt2k-Ma0tzZupitjxE0MZdOIgT-cjUert1NNyyS8W6Clp02wMa3M7wXIIdmm7aroH2xb6D7f7KhoSyNYw6D6sekhyXE5OYvz-PiVZ9fmDmfy88xEEKGlIFyrMyU6mteBK03r-D-C2iIVv61krRF2NOJvXBOWUbvbGTJ-qRXZRMWbjxquCu7Y1WeLGY4XLxuVC1V0AQfE5EFO8Fk_Y-oj2Od60PeRUd59UV8NyPD6HB5WWNKMqE1DHPdlfzTmwkLMO12zN0hA_xUxR16GI7eiABzZ0Wh4AkNOl4Gw95Fo3hQGYykgZIm1OZkdmyxF2mVCLw7ZFdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19750" target="_blank">📅 20:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19749">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaREQp55BmqiLM-fS8scNj9dYSURG65yl4nCH9aLPPev59681p6BBqlKryZgkDxazbKCo5KwaeYOjpZVEhBBJnhyfJZkB-7E9p_DYfbLKTCXrj6vQc2QNgJX9_gxnY-K51Xa3DpY3-44xhRoWhf_-XtMm3y5_JPypkC3dS_fOTr6GYVncb8V21K3PXDORE5fHVY7vklgVlWyxAE0yIt7vKRtlULjZ_lQHgy6mcB6xd5Y7nwnaLgodtsZ8UxMRdSrGj8eLtBFh_54hyrJCJh5mr-q02vlGuXRNIDcz254ULtRI5bfNNYAoZif_KKpS_9WCDn_jbTBgdQ-6xwLI-86ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعید میدانم ایران چنین طرحی را ارائه کرده باشد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19749" target="_blank">📅 20:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19748">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WanzgP3bTnA5hVB2bClMghxOj-szFMn5eX6euKw99A0NR2ip2lrd7kwH3_SCcOKpYwVaY5-kON2UXG9Ly58PCuELmscbTUoJYAmNl3VssnuY-xCdBac9qHwKDw7tUwfPdn-rcgIxwTj3djO33s_exeMFkiFWDPnosXsx1rtr1XA2TN2CWGJLAgYXCswTfWO5UYf-Evrx4Dr0E3unqyf21yWJ10NxWGdxXq8sIlDLLlFndLxcbDSC4cbfueJf0-4Ih6XNb9IgvG0RdTh7dsLORud97kWYQmbhlUjf88dELPaXX9f4jLqrcljSWxY3V4wN99hD5Pi7UFn1s7l_nZkKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من نمیدانم این اظهارنظر منتسب به سردار وحیدی درست است یا نه اما اگر درست باشد اصلاً زمان مناسبی برای اذعان به داشتن سلاح هسته ای یا حرکت در این مسیر انتخاب نشده.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/19748" target="_blank">📅 20:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXsfScFte6xVfi9mF18YwTwZSh7K5UTFhiWB44lchyE46aTYn7_aPqEUF33j08haa11-iOVtBYx4Z_w1CO8VU0sM96vBTU1otkYW7nhhgVJhawLxhm-4vOknQHyVj0Mq4hi2wVI5WtFqt5C-TqpODw0l5wy4kSfN4Ktu_MjF1x3OJKAEXRetjHgoPk3zUZPObdcLLU6Lu-aXY5W3-vebut-YkNj9wot6gl7dcwG5LQtynosXCT_3WrWEmVVz3fwjZ_YzsRfU-bOdbqL9_Z0a2B_BSiJwHZvGWFVy-aiTumnnQ2wXagMJVoJrDZDIyEk-7CNoSH94TDPAAkpcY8g3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6LhDpBALlpzIps4XCBygr8dXBgP8205lrqfOfiY0T5MKmAvTDh8OCwSNZUyrMlQRYNkwxx3dXU6NQ-3zhVT9l1V8XcRkaQyZiPoaFrjfNLGEXLbAUjHvXA1I3qbzVIzPWTO-HkDAQBQvHRorktwPgooJRXbGyV_4K4e2X9UHYjNKEpc9L5A-lpNFspONDudEh8M_j1tOvjg99a1efSYB_4Xd4vka72Kcnmlct_z80QUyfxo0LhW8SIHN41wmWSO4WfZWpIVTnNlcfkyV1GEYW9F86eK4Ztxhu3NRKbmVUx5RZ9QumE5z971s9i0uKnjJiBQF_P4ZYSy3HfsPRTJRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نمیدانم این اظهارنظر منتسب به سردار وحیدی درست است یا نه اما اگر درست باشد اصلاً زمان مناسبی برای اذعان به داشتن سلاح هسته ای یا حرکت در این مسیر انتخاب نشده.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19746" target="_blank">📅 19:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V960z_sy0uZzuUtyIAB2UaOP2kdKhX9yG1S-u7_flfbcMma4G3tBO1B5vEh39OL1F-F2IfKsWUA0WSYPYibb7p9M-NAUA0MityENPQb-dwq-kfg-pyphYuMiSMVYEEon6DVnRFPmFYbKXOPsoQc4JytjLr2K7elik0zJeU4syQW70TeWyyuezq1xOefHR6Dj0UKi2eO3Gkjuo97gFkutENH-PsLj1OqI8vpKQVAADY1l7d1TmsQLuMTy8Pw-jHdJJQH2xKwARrBI7O3fbmO2vsQMu9KdJ36PdLf71gMGmkHc4hfDZQfeRWXkeUwVugw_XP-LdPosOjIffDlSVr8aGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19745" target="_blank">📅 19:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جزئیات متن اولیۀ طرح راهبردی مدیریت تنگه هرمز
🔹
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.  براساس این طرح:
🔸
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19744" target="_blank">📅 19:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جزئیات متن اولیۀ طرح راهبردی مدیریت تنگه هرمز
🔹
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.
براساس این طرح:
🔸
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی و سایر کشورهای متخاصم از تنگه هرمز ممنوع می‌شود.
🔸
محموله‌های مرتبط با رژیم صهیونیستی، اعم از نظامی و غیرنظامی، حق تردد از این منطقه را نخواهند داشت.
🔸
شناورها یا محموله‌هایی که در اقدامات علیه جبهه مقاومت نقش داشته باشند نیز مشمول ممنوعیت خواهند بود.
🔸
کشورها و اشخاصی که به ایران خسارت وارد کرده‌اند، تا زمان جبران خسارت، مجوز عبور از تنگه هرمز و خلیج فارس را دریافت نخواهند کرد.
🔸
برای قانون‌شکنان، جریمه‌های سنگین از جمله تا ۲۰ درصد ارزش محموله، پیش‌بینی شده است.
🔸
دولت موظف خواهد شد با همکاری نیروهای مسلح، مسئولیت‌هایی مانند هدایت ناوبری، نظارت بر تردد شناورها و حفاظت از امنیت و محیط زیست خلیج فارس را برعهده بگیرد.
🔹
این طرح همچنان در مرحله بررسی کارشناسی قرار دارد و مجلس از صاحب‌نظران خواسته پیشنهادهای خود را برای تکمیل آن ارائه کنند.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19743" target="_blank">📅 19:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الفاتحه مع الصلوات</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19742" target="_blank">📅 19:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به جایی نخواهدرسید.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19741" target="_blank">📅 19:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5a791a91.mp4?token=MxTSy2FSSTZZiGBihP6_mSqm8NVmZ2-joysf7gYBTPfnditOQ_sKKERbijmDzWv64M3iy8VsQQpwYu1KUS1wBaaV1KuD93XHzIJHVCJbjiCHwlT2ygjuqxJqNhpgNS245HaNrV8LTzEj8jhaAw5izm6VP964umU055rcRZnz2SdvG6x4zsE9wLoQx4hE3qFZkxNlMKK-T2Wfy496doEn1IlXCdQgemFhCbArxxVbEhJGmBgCmm8A3434LozSWu3HQ3eGrqjbP17Dw1vkfIHHw4tJXTGUzFENUJ4V4QpFD_dZnd97zuNachpTduA10d-ErF5RTW3xlYuB48vivigOdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5a791a91.mp4?token=MxTSy2FSSTZZiGBihP6_mSqm8NVmZ2-joysf7gYBTPfnditOQ_sKKERbijmDzWv64M3iy8VsQQpwYu1KUS1wBaaV1KuD93XHzIJHVCJbjiCHwlT2ygjuqxJqNhpgNS245HaNrV8LTzEj8jhaAw5izm6VP964umU055rcRZnz2SdvG6x4zsE9wLoQx4hE3qFZkxNlMKK-T2Wfy496doEn1IlXCdQgemFhCbArxxVbEhJGmBgCmm8A3434LozSWu3HQ3eGrqjbP17Dw1vkfIHHw4tJXTGUzFENUJ4V4QpFD_dZnd97zuNachpTduA10d-ErF5RTW3xlYuB48vivigOdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط ببینید و اگر وضویتان باطل نشد رییس جمهور را دعا کنید</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19740" target="_blank">📅 18:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
دستور الزیدی برای آماده‌باش نیروهای نظامی و امنیتی عراق
همزمان با نزدیک شدن به پایان ضرب‌الاجل مقاومت اسلامی عراق به دولت برای پاسخگویی به حمله آمریکایی‌سعودی علیه مقرهای الحشد الشعبی، دستگاه‌های امنیتی و نظامی عراقی به حالت آماده‌باش درآمده است.
‎</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/19739" target="_blank">📅 18:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بیانیه صادر شده توسط نیروهای مسلح یمن
به نام خداوند بخشنده مهربان
خداوند متعال فرمود: {هیچ تجاوزی جز بر ستمگران نیست.}
دشمن جنایتکار سعودی در ادامه تجاوز و محاصره خود علیه مردم عزیز یمن ما که نزدیک به ۱۲ سال است ادامه دارد، شاهد تجمعات نظامی گسترده سعودی در مراحل پایانی خود بوده است که هدف آن تشدید درگیری علیه استان‌های آزاد شده و مردم یمن برای منصرف کردن آنها از موضع خود در مورد پایان دادن به محاصره ظالمانه است.
بنابراین:
نیروهای مسلح ما یک عملیات نظامی گسترده و دقیق را با هدف قرار دادن مراکز تجمع نیروهای دشمن سعودی در مناطق الرویک، العبر، الثانیه و سایر اردوگاه‌های متعلق به لشکرهای اضطراری اول و سوم، با استفاده از تعداد زیادی موشک بالستیک و پهپاد انجام دادند. این عملیات منجر به موارد زیر شد:
* کشته و زخمی شدن صدها مزدور دشمن سعودی.
* انهدام و آتش زدن تعداد زیادی از اردوگاه‌ها، مراکز تجمع نیروها، انبارها و تسلیحات دشمن سعودی در منطقه الوادیعه در شرق کشور.
* انهدام تعداد زیادی از خودروهای نظامی موجود در اردوگاه‌های هدف قرار گرفته.
نیروهای مسلح یمن به دشمن جنایتکار سعودی نسبت به هرگونه اقدام تجاوزکارانه علیه کشور و مردم ما هشدار می‌دهند و عواقب هرگونه تشدید اوضاع را متحمل خواهند شد. به گمراهان و فریب‌خوردگان در میان مردم خود توصیه می‌کنیم که اردوگاه‌های دشمن سعودی را ترک کرده و قبل از اینکه خیلی دیر شود به خانه‌های خود بازگردند.
به مردم عزیز یمن در تمام استان‌ها اطمینان می‌دهیم که نیروهای مسلح کاملاً آماده مقابله با هرگونه تشدید اوضاع هستند. از همه مردم خود می‌خواهیم که هوشیار باشند و با هرگونه تجاوز سعودی مقابله کنند و به مراکز تجمع نیروهای سعودی در هر کجا که باشند حمله کنند.
ما به استراتژی «محاصره در برابر محاصره» تا زمان رفع محاصره کشورمان ادامه خواهیم داد.
خدا ما را کافی است و او بهترین سرپرست، بهترین محافظ و بهترین یاور است.
زنده باد یمن آزاد، با عزت و مستقل!
پیروزی از آن یمن و همه آزادگان این ملت باد!
صنعا، ۲۳ صفر ۱۴۴۸ هجری قمری
صادر شده توسط نیروهای مسلح یمن</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19738" target="_blank">📅 18:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19737" target="_blank">📅 18:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حملات سنگین اسرائیل به جنوب لبنان آغاز شد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19736" target="_blank">📅 16:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیروهای انصارالله یک پایگاه نظامی متعلق به نیروهای "دفاع وطن" که به عربستان سعودی وفادار هستند، در منطقه "الودعیه" را مورد هدف قرار دادند که در اثر آن دستکم ۵۰ نفر کشته شدند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19735" target="_blank">📅 16:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19734">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اسرائیل و افسانه تجزیه ایران  در ایران امروز، مدتی است که افسانه‌پردازان، بی‌ وقفه تکرار می‌کنند که اسرائیل در اندیشه تجزیه ایران است. چگونه ممکن است کشوری با جمعیتی نزدیک به یک‌نهم ایران، مساحتی حدود یک‌هشتادم، در فاصله بیش از هزار کیلومتری هوایی و نزدیک…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19734" target="_blank">📅 13:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اسرائیل و افسانه تجزیه ایران
در ایران امروز، مدتی است که افسانه‌پردازان، بی‌ وقفه تکرار می‌کنند که اسرائیل در اندیشه تجزیه ایران است.
چگونه ممکن است کشوری با جمعیتی نزدیک به یک‌نهم ایران، مساحتی حدود یک‌هشتادم، در فاصله بیش از هزار کیلومتری هوایی و نزدیک به سه هزار کیلومتری زمینی (آن هم با چند کشور مهم حائل بین راهی)  قادر باشد کشور ـ تمدنی چند هزار ساله را تجزیه کند؟
این در حالی است که موضع رسمی اسرائیل نیز چنین ادعایی را تایید نمی‌کند. بنیامین نتانیاهو در رویکرد علنی خود، از جمله در سال ۲۰۲۶، شایعات مربوط به تلاش اسرائیل برای تجزیه ایران را رد کرد. خوب یا شوم، رویکرد رسمی بی بی متوجه جمهوری اسلامی است، نه تقسیم ایران.
ولی اگر روزی همبستگی ملی ایرانیان چنان فرسوده شود که کشوری این چنین کوچک و غیرهمسایه بتواند سرنوشت ایران رقم بزند، دیگر  مساله، قدرت اسرائیل نیست؛ مساله، ضعف درونی ایران است. هیچ قدرت خارجی، حتی اگر ابرقدرت باشد، نمی‌تواند کشوری را تجزیه کند؛ مگر آنکه شکاف‌های داخلی، پیش‌تر پایه‌های آن را سست کرده باشد.
از همین رو، روایت «اسرائیل در پی تجزیه ایران است» بیش از آنکه یک تحلیل استراتژیک باشد، افسانه‌ای سیاسی است؛ افسانه‌ای که گاه برای بزرگنمایی تهدید بیرونی و به حاشیه راندن مسائل و کاستی‌های درونی ساخته و بازتولید می‌شود. تاریخ نیز یک درس روشن دارد: یکپارچگی سرزمینی و مردمان کشورها را پیش از هر چیز، همبستگی ملی، مشروعیت سیاسی، حکمرانی کارآمد و رضایت شهروندان حفظ می‌کند، نه صرفاً ترس از دشمن خارجی.
#یدالله_کریمی_پور
#karimipour_k</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19733" target="_blank">📅 13:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 20</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19732" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 20
پنجشنبه 6 آگوست 2026</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19732" target="_blank">📅 13:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyOXZxLjRkmuQIHz9jyZCzjSc2mXPSS9Fxz-dvweN5_UkFeXho_1KCjFV80NmdsLcI0tuVTlRBSP0iWJz7no7kNnljtDMimFDXkw_Wb-mC38skoD6XS5goi0I5N1uSibIWhLNWsGk83te1MJK0csXfUrJ52nAMQbR5Y2VHjZD3NxhZzTj_KuKHc39jsVgGjxJtTdsTCuvXPglMaARHvwB_RC8tWKgiIlEtSXDb3NO0HJtuG6wISQsP-JWYcPvNQNJoBX2ofT_m7xQGOoRkFa4RcrwaHbPlx_Tqz6V9rD7DmnL_i86tEK21IzM2Lu0XuDi-geo5YyTqC9AlZatFl0WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/19731" target="_blank">📅 12:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFCJWxlD_T-ff5H_LEJEvxPPDQgNTgjl3rf9tYED85KCHpeBiSuKvzUPWjkTQzBciTPeWhCIBpIqmd-C8F9EUZ6aKFkZTLiJOCj6tqYXpX8aPPHB5pwVk4Laqk8-F-8VvHHKDdp0G3TZBeEj-jLrMVFxs1Pu5_kpN_sJtOnnfpvif98oOaYIFZB6z-ZuWSksjSkPKiS-bhodKpazxcJbcvIlyQFUVq3H4R23d_Os-UKBvBlTkWLUbmhjPn9uSmmC9IgdtbQbVjDHxH_KBQL3nG1C8PiMNSajSyy2sm44dTQCGSfFb5bOFdTPCdGkfpiiBye8-ElqPfgKemJOhUhPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود با دیدن این عکس، ترامپ از نابودی زیرساخت های ایران صرف نظر کرده است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19730" target="_blank">📅 12:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHqxbqYzMws50cfqKSz5nqVvEKCDPtJuWEWxHq4_r-pIRJnd7cU090qz-W40NOcYlTfg5pzUZRHdniK7347aAEYSgsSAYZhHYlebm8rtUyeTz7MwQNSidoIcR1-ZKzNQ_1vt65sHgWiX0iaeHs0xZI5Epiqb5MMyGjqvAoZxcXqzQUWbVWCMWOQpj9qzmoiANtCwQjlDe21hHASWPBvVUyavzvCaff5zWT7f_44Ywz-u1FIkFcGe1ZNvkmleafpNRVI50iMO-fneVbI3mF-9m5S9uity0Fr-1MvnUBsn9YlMUDIN3bT_S3ieb0PVnH7t6OgdpMXcDTXexouDMxoSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه قرار دارد. پیش بینی می شود طلا امروز مقداری افت اصلاحی داشته باشد (با توجه به رشد GRI از دیروز) اما دوباره به سقف (4300) حمله ور بشود (با توجه به افت میانگین شاخص GRI در روزهای گذشته)</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19729" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سبحان الله!  هندی ها حتی در باشگاه های بدنسازی شان هم ممکن است غرق بشوند!  (ماشالله چه بدن هایی هم ساخته اند در باشگاه)</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19728" target="_blank">📅 10:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d8645934.mp4?token=U6K5rOQ05xUCB-vaJoG3P8jpdA0EZvEBTpEYPpd0xI5knShcoRtcXu5mBqoPuXDZ3KgxMvp1aZXZXafQJ1IV1h6KeflGiN_wl8M0pQudHJ_VbBZjVoTSS5ccZAfhoqp3RyDnR-bDZiEwZdAow0wMBzUi1dtVXrcUlzhKHBMKxMbxQ1DF_kbbbumDrCEJ6U63RHvYocoJxYJ9c2gZWjB0E2tzl30efN_rEjVmePR2jVNRF615vbMKTc32UJ-N0KiUZbGOF7zzUncrTqkpZTj9VrWpZeidFhqeMYx2LGXJXxE2bsaxPrmG8p9PTWmI2YCsGy0bz2su20dnQlW_Pr3eXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d8645934.mp4?token=U6K5rOQ05xUCB-vaJoG3P8jpdA0EZvEBTpEYPpd0xI5knShcoRtcXu5mBqoPuXDZ3KgxMvp1aZXZXafQJ1IV1h6KeflGiN_wl8M0pQudHJ_VbBZjVoTSS5ccZAfhoqp3RyDnR-bDZiEwZdAow0wMBzUi1dtVXrcUlzhKHBMKxMbxQ1DF_kbbbumDrCEJ6U63RHvYocoJxYJ9c2gZWjB0E2tzl30efN_rEjVmePR2jVNRF615vbMKTc32UJ-N0KiUZbGOF7zzUncrTqkpZTj9VrWpZeidFhqeMYx2LGXJXxE2bsaxPrmG8p9PTWmI2YCsGy0bz2su20dnQlW_Pr3eXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جنگ تمام هم که بشود باز هندی ها غرق خواهندشد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19727" target="_blank">📅 10:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
ما گزارشی از حادثه‌ای در ۹ مایل دریایی جنوب شرقی کومزار در عمان دریافت کرده‌ایم.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19726" target="_blank">📅 04:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ در مورد ایران:  ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.  ما در حال صحبت هستیم. ببینیم چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19725" target="_blank">📅 01:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19724">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.
ما در حال صحبت هستیم. ببینیم چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19724" target="_blank">📅 01:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPZx5aEdB4DlG_NBMhoxLv4PPZH1BEU0x0b0Ai9cU68FiETPDuxo75tpiCwrbgNyS5Df81J6sCiBAwgjaAyi9dGVypDE-Nojz_E2mzw6_-07aeIDQ4qZ26jkanWl2XsRjHKxXqq4--eRGzL_LY8jyxm1MUXvn9l_a3TEMN-TLH9CYRaJB1itgny9-g9EUyxEO5iSrS463K4IbHFa5lG33cslw79Uk0wBHkmhrDXqJbm90RchrsXQFbvpwqyzOfjaWMsDuU8MMcDHoJeOqspjF6LA_9dx7nzveCurhawSd8hrzTOj3vwdyYsqVbd_PETVbYWXqk6mrmKEFoQQKqmEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD
— H4
میتوان چنین ساختاری برای طلا متصور بود.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19723" target="_blank">📅 23:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19722">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqhuiX2r-ehkUBEz15L6QCestFJWRA_G48kknQM20mK8ew3dH3XAZTCUFFlNcFVJEVTIu_iBkLKNZmYVjJIexmLlQhJvEPNvfKUgfRYPy-Ap1Dp0jX3JsRSHzic3Aq2K3ogWTsokgCCS4p0TC_45jg09Wq-X4iioqDji_-4aMDuOGb5_7nC8kOeKaLf6dXw-tJx5axu0TBqq5GlNLFwgs4K4RIKbgtwSXmQWxGiapFRI5F_OrY5IUXZZcSG0-_Gjeg-J60gHTh5mMuV1YDhpxYGdOqcux-pkJGJJtpvQMgHUAS6cZUCE_949T8Zqd5auvo5bXSOm06o-g_t4gdnc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح پایینی قرار دارد و ادامه جو ریسک پذیری پیش بینی می کند.  (شخصاً با توجه به اینکه:  — عمده رشد امروز در سشن آسیا روی داده — پس فردا گزارش NFP داریم — اعتمادی به توافق ایران و آمریکا ندارم  اینجا خریدار نیستم و پله ای…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19722" target="_blank">📅 22:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رئیس‌جمهور ایران، مسعود پز‌شکیان:  هر چقدر هم که فکر می‌کنم، نمی‌توانم هیچ دلیل منطقی پیدا کنم که چرا آن‌ها رهبر، فرماندهان و دانشمندان ما را به قتل رساندند.  بسیاری از فرماندهان و دانشمندانی که به قتل رسیدند، حتی صاحب خانه هم نبودند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19721" target="_blank">📅 22:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19720">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رئیس‌جمهور ایران، مسعود پز‌شکیان:
هر چقدر هم که فکر می‌کنم، نمی‌توانم هیچ دلیل منطقی پیدا کنم که چرا آن‌ها رهبر، فرماندهان و دانشمندان ما را به قتل رساندند.
بسیاری از فرماندهان و دانشمندانی که به قتل رسیدند، حتی صاحب خانه هم نبودند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19720" target="_blank">📅 22:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19719">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLeh-j43DMZi8an8Tk53Cmx8y7B_DSV01UB6yD5DHdaWfAa7BgDWh9PV34gmtOjC17YEoj-tCc2vNuCbTzogH7rC9p3UsXmCLFZdyC8SxyTdwE9SXz7DkWefVTVOsewB9o41bCZPL1271NeMFy1O0otRxc1DrCiGMK5SB9X1MNJY3pqAOyROrERvMIlzz03w3sHveHDy3F_G5y5RgaJGaRR0KsOW8D2yDZxSJOQMbwCDTuSaXZSAY96znEXMFMqtDuD6RxMtI6D1D0ndp0uNRSqbhmxVbvJLZFb7ZZUWxlvmprsuKKCw9P5ste7JcTESaRU7PJj445Jh5vPN5wthFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19719" target="_blank">📅 21:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19718">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">روسیه به طور فزاینده‌ای از موشک‌های پدافند هوایی S-300/S-400 در نقش‌های حمله زمینی استفاده می‌کند که تهدیدات شبه بالستیک سریعی را ایجاد می‌کند که رهگیری آن‌ها دشوار است.
طبق اطلاعات استخباراتی اوکراین ذکر شده در تحلیل، روسیه حدود 200 موشک RM-48U تبدیل‌شده را در سال 2025 تولید کرده و قصد دارد بیش از 480 موشک را در سال 2026 تولید کند.
این موشک‌ها دقت کمتری نسبت به اسکندر دارند اما تعداد اهداف پرسرعتی را که اوکراین باید در برابر آن‌ها دفاع کند، افزایش می‌دهند.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19718" target="_blank">📅 21:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19717">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">غریب‌آبادی:   موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19717" target="_blank">📅 21:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19716">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">غریب‌آبادی:
موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19716" target="_blank">📅 21:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19715">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فوری | معاون وزیر امور خارجه ایران: پیام‌هایی از ایالات متحده دریافت کرده‌ایم که نشان می‌دهد این کشور آماده است تا به تعهدات خود بازگردد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19715" target="_blank">📅 21:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19714">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فوری | معاون وزیر امور خارجه ایران: پیام‌هایی از ایالات متحده دریافت کرده‌ایم که نشان می‌دهد این کشور آماده است تا به تعهدات خود بازگردد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19714" target="_blank">📅 21:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19713">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رائفی‌پور:   ایران به اردن حمله کرد و ۶ جنگنده اف ۳۵ را نابود کرد چون قرار بود به مراسم اربعین و مواکب حمله کنند</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19713" target="_blank">📅 20:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19712">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رائفی‌پور:
ایران به اردن حمله کرد و ۶ جنگنده اف ۳۵ را نابود کرد چون قرار بود به مراسم اربعین و مواکب حمله کنند</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19712" target="_blank">📅 20:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19711">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">منابع عربی گزارش حمله موشکی به بحرین را منتشر کردند - خبرگزاری مهر.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19711" target="_blank">📅 19:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19710">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">منابع عربی گزارش حمله موشکی به بحرین را منتشر کردند - خبرگزاری مهر.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19710" target="_blank">📅 19:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19709">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19709" target="_blank">📅 19:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19708">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgwTd4RHh7pDTh-f4wvJHA5UdPhvNeHaAtCbkO1x7itSXPJIDLgxTekIanr1Fg49GGV9kee_XngZNPCcKMALHpwxP_57OUX5mk7npxgjekiORH91d6Eg6_DiiAOkZnawZMWSvPn4dveZHxS5oPs5BpGYyU9iyLGEF4GRNO9qp6WNuYetbjmX9lqQe1NtMb36xL7xLWNE7s-XTqx_Qw3-kqW-KnPnY87sRoTiXSsnS0tSdQjXUUCiGSPcxMxPBTrGHngcz8Z3nbYkL-W8eBhKi-94zMVgP2ng4pe6azpoYr6PVf93MGpOzhpavumNi7kwB1L8V1mgJh_K2IK6cSYx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
طرح جدید اسراییل برای ساخت
پایگاه‌های نظامی در جنوب لبنان
روزنامه هاآرتص گزارش داد که رژیم صهیونیستی حدود ۲۳۰ کیلومتر مربع از خاک لبنان را همچنان در اشغال دارد و قصد دارد بر روی ویرانه‌های روستاهای تخریب‌شده، پایگاه‌های نظامی جدید احداث کند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19708" target="_blank">📅 18:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19707">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19707" target="_blank">📅 18:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19706">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">طبق وب‌سایت وزارت خزانه‌داری ایالات متحده، ایالات متحده تحریم‌های مرتبط با ایران را لغو کرده است.  منبع: رویترز</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19706" target="_blank">📅 18:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19705">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فوری | یک مقام ارشد ایرانی به الجزیره گفت: هرگونه بستن یا باز کردن تنگه هرمز به اقدامات واشنگتن بستگی دارد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19705" target="_blank">📅 18:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19704">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">طبق وب‌سایت وزارت خزانه‌داری ایالات متحده، ایالات متحده تحریم‌های مرتبط با ایران را لغو کرده است.
منبع: رویترز</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19704" target="_blank">📅 17:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19703">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">منابع فلسطینی گزارش می‌دهند که حماس، واحدهای سازمانی، فعالیت‌های مخفیانه و عملیات امنیت سایبری خود را به ترکیه منتقل می‌کند، در حالی که قطر به میزبانی رهبری این سازمان و فعالیت‌های عمومی آن ادامه خواهد داد.
— روزنامه جروزالم پست</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19703" target="_blank">📅 17:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19702">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پیش‌نویس قانون ترکیه برای حمایت از خلع سلاح و بازگشت به زندگی عادی اعضای سازمان پ.ک.ک
ائتلاف حاکم ترکیه، روز چهارشنبه، یک پیش‌نویس قانون را به پارلمان ارائه کرد که هدف آن پیشبرد روند صلح با حزب کارگران کردستان (پ.ک.ک.) است. این قانون شامل حمایت‌های قانونی برای بسیاری از اعضای سابق این سازمان و تعلیق مجازات‌های زندان برای برخی از افرادی است که به عضویت در پ.ک.ک. متهم شده‌اند.
این قانون‌گذاری، که انتظار می‌رود در اواخر این هفته توسط پارلمان تصویب شود، به دنبال پایان دادن به درگیری‌های دهه‌ها طولانی با تسهیل بازگشت هزاران نفر از اعضای سابق پ.ک.ک. است که در حال حاضر در شمال عراق مستقر هستند.
بر اساس این قانون پیشنهادی، سازمان اطلاعاتی MIT ترکیه مسئول بررسی و تأیید خلع سلاح این گروه خواهد بود، در حالی که یک کمیته متشکل از معاون رئیس‌جمهور، چندین وزیر و رئیس MIT، بر روند تسلیم و تحویل سلاح‌ها نظارت خواهد کرد.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19702" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
