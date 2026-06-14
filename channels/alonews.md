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
<img src="https://cdn4.telesco.pe/file/uCVdvWSDkQODwAOmJb-g6QbP0m0HQFHmxtnM6sCoAA1bxKjjXG_8093pOXGRdESjfMyLPAkoII7rPicFnG47zm36b6gTLarRFlm7iR5yWABDvznaYOVpu5x_2nTR7zftdIO_xuuoC9laJM3mOXa2x8OTVsEzVlGQrz9GH2BIHJqNZVik2dmKNHlfJVHVgaRW6hY75H45lXh8Hl4g8M_M6WfKJOiJDxBsPAqLQrHDiXRW-MbYiHNJxKlXia4hr2FnVxOZwKqOPZzSsJ4Lr8qaTxiRe-l7WQZbVjGgcXNGS0zLQIlpAP7H6gqRk7Unwn4JBx_9Neo7Vg-G9UIlXGBBPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 980K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 13:31:37</div>
<hr>

<div class="tg-post" id="msg-127830">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد ایرانی : طبق پیش‌نویس توافق با آمریکا، ایران قبول کرده دیگه دنبال ساخت یا گرفتن سلاح هسته‌ای نره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/alonews/127830" target="_blank">📅 13:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127829">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eeb7fe4ee.mp4?token=HoHwqf4GriS-zRk-oQUSN2WY_KNlsdRhVEyvRtgPqM_CBKLQMIHDY-ANwEoEVFM6xw5YfdS7IRmiYQmIipaBPAtUkFi_b-1crY4YjhW8pKrHFDZVmdU3qCVwBpn1HVSuAq0LmI-XtoWiysiLqyS2bX87Fc-3BKFhzKTAQ8Yzcb2vunRdo4pUYVxQ0sI0VdiyJd30r5-MechkhmdXFXYBoYEWBlTCh-frnmvmJ064FJ6CNEtsMiLj04bVAnSFSybpM-epq-fE9aD5bPqxyY0HjZVUAn2HmQ2vNoLfODhJnLFYRamBQE9zTNDikEvb0NGpI_7_NeJQszQaMqpZ8ItygQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eeb7fe4ee.mp4?token=HoHwqf4GriS-zRk-oQUSN2WY_KNlsdRhVEyvRtgPqM_CBKLQMIHDY-ANwEoEVFM6xw5YfdS7IRmiYQmIipaBPAtUkFi_b-1crY4YjhW8pKrHFDZVmdU3qCVwBpn1HVSuAq0LmI-XtoWiysiLqyS2bX87Fc-3BKFhzKTAQ8Yzcb2vunRdo4pUYVxQ0sI0VdiyJd30r5-MechkhmdXFXYBoYEWBlTCh-frnmvmJ064FJ6CNEtsMiLj04bVAnSFSybpM-epq-fE9aD5bPqxyY0HjZVUAn2HmQ2vNoLfODhJnLFYRamBQE9zTNDikEvb0NGpI_7_NeJQszQaMqpZ8ItygQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا سیما: پاکستانی‌ها برای میانجی‌گری به ایران نمی‌آیند، بلکه مرتب پیام تهدید و‌ ترور می‌آورند
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/alonews/127829" target="_blank">📅 13:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127827">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFbUzisM3rspx6KVrBM9UOfuK4xk21seAarxGKt8j8k4YnC8SVj5De_Vz3JgzzhTGEpXzjnBH5uPmclAaXVc4U_19ejVw5Pmnlv4tP-3lbKa5i-bl6e5g1OH2TllSaRUZLKyrwO5Mf88e_FRw_-XLb0aVODrqFpoihFETRrzLgdlQS35dV57-oQjIMp-9uVW_LrRv4muzTxxdV7FufWNjiE6pneNxBWTpm968S_hna1IW5-4NcVgO7xYU4qVuH2uzVJdxLLAAZuxVZIICnU9CL9jLvyaEzCcHjfs_C2cji7v44btl7Wrxu0SA0bFahL2AzrlG2Fh7lQ1hvj_EykAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXE13sSTfAiOJjBPaPjm22PTLnA3uJ3lRiAf1vlaVPsamcsG7EdiKZfhnkh3CXPz99hQO0xUQeC6invNwKj-e-6J8H53eUbOV48ZcxX0CKW6PZIg5eOxMNg3cY98YwKEVTIEq-vPFaN410X0_798r_52V4d0fPYG4AztNNvukuz4G5O041bWLkgRFdOu1O1JV6ncx1oNYKYUO05CvcYddLJ6WZO9QFhWJR1AMvQ_unqKot8GTjGbx9Cder7ef1f1feKzMFServkMYhFc3uI3tf-zA6AnNzJ5Tyez_CU-DpqPSS6a8Clu-_KbnZGdupvc0khOULh8orKRhPAlsN511Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صندوق سرمایه گذاری قطر اعلام کرده بعد از گلی که دیروز بوعلام خوخی در دقیقه‌ ۹۵ به سوئیس زد، ۳میلیون دلار به همراه یه رولز‌ رویس فانتوم آخرین مدل به ارزش ۵۵۰ هزار دلار پاداش خواهد گرفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/127827" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127826">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شرکت نفت و گاز پارس: چاه جدید فاز ۱۱ پارس جنوبی وارد چرخه تولید پایدار گاز شد
🔴
افزایش تولید از فاز ۱۱، در بالا رفتن سهم برداشت ایران از این میدان عظیم گازی اهمیت ویژه‌ای دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/127826" target="_blank">📅 13:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127825">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
جزئیات متن تفاهم ایران و آمریکا از زبان مشاور رئیس تیم مذاکره‌کننده
🔴
مهدی محمدی، مشاور راهبردی رئیس تیم مذاکره‌کننده جزئیاتی از متن یادداشت تفاهم ایران و آمریکا را تشریح کرد که به شرح زیر است:
🔴
۱. توقف درگیری‌ها و تضمین‌های امنیتی
🔴
در گام نخست، توقف کامل عملیات نظامی علیه ایران و لبنان و جلوگیری از هرگونه اقدام نظامی جدید در دستور کار قرار دارد. همچنین طرف آمریکایی باید تضمین‌های لازم را برای جلوگیری از تکرار تنش‌ها ارائه کند.
🔴
۲. آزادسازی دارایی‌ها
🔴
براساس چارچوب مورد بحث، بخشی از دارایی‌های بلوکه‌شده ایران در ابتدای اجرای توافق آزاد خواهد شد و همزمان روند تعلیق برخی محدودیت‌ها و تحریم‌های اقتصادی آغاز می‌شود تا امکان افزایش مبادلات اقتصادی و فروش نفت فراهم شود.
🔴
۳. رفع محدودیت‌های دریایی و تجاری
🔴
یکی از محورهای اصلی توافق، تسهیل تردد کشتی‌های تجاری ایران و کاهش محدودیت‌های دریایی است. هدف این بخش، بازگشت تجارت دریایی ایران به شرایط عادی و رفع موانع موجود در مسیر حمل‌ونقل بین‌المللی عنوان شده است.
🔴
۴. مذاکرات هسته‌ای در مرحله بعد
🔴
در متن مورد مذاکره، مسائل هسته‌ای در مرحلۀ نخست توافق قرار ندارد. براساس این چارچوب، ابتدا باید تعهدات اولیه طرف مقابل اجرا و راستی‌آزمایی شود و سپس گفت‌وگوها درباره موضوعات هسته‌ای وارد مراحل بعدی شود.
🔴
۵. لغو تحریم‌ها و بازسازی خسارت‌ها
🔴
در مرحلۀ نهایی، لغو تحریم‌های اولیه و ثانویه آمریکا و همچنین پیش‌بینی سازوکارهایی برای جبران و بازسازی خسارت‌های ناشی از جنگ و فشارهای اقتصادی مورد توجه قرار گرفته است. این بخش از مهم‌ترین مطالبات ایران در روند مذاکرات به‌شمار می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/127825" target="_blank">📅 13:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127824">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نیویورک‌ تایمز: تهران معتقد است ایالات متحده آمادگی ورود به یک جنگ گسترده دیگر را ندارد و دونالد ترامپ ترجیح می‌دهد به توافقی برسد که تنش‌ها را کاهش داده و ثبات را به بازارهای انرژی جهانی بازگرداند. این موضوع به ایران فضای بیشتری برای مانور می‌دهد و احساس نیاز آن به دادن امتیازات بزرگ را کاهش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/127824" target="_blank">📅 13:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127823">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
آی۲۴نیوز عبری: امروز ونس و قالیباف طی جلسه مجازی تفاهم نامه را امضا خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/127823" target="_blank">📅 13:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127822">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نیویورک تایمز: جنگی که آمریکا و اسرائیل طی ماه‌های گذشته علیه ایران انجام دادند، به اهداف راهبردی اعلام‌شده در آغاز آن دست نیافته و در عوض واقعیت سیاسی و امنیتی جدیدی ایجاد کرده است که ایران را به کشوری مقاوم‌تر و آماده‌تر برای پذیرش ریسک تبدیل کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/127822" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127821">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ایوو دالدر، سفیر پیشین آمریکا در ناتو معتقد است که ایالات متحده در شرایطی که تمایلی به ورود به رویارویی مستقیم با روسیه ندارد، به فاصله گرفتن از اروپا ادامه خواهد داد.
🔴
به اعتقاد وی، آمریکا آگاهانه و فعالانه در حال جست‌وجوی راه‌هایی برای ایجاد یک نظام امنیتی مستقل از اروپا است.
🔴
دالدر افزود، ایالات متحده از بیم واکنش احتمالی روسیه، نه تنها استقرار سامانه‌های تسلیحاتی دوربرد و دقیق را در خاک کشورهای اروپایی متوقف کرده، بلکه متحدان اروپایی خود را نیز از تجهیز به چنین سامانه‌هایی بازمی‌دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/127821" target="_blank">📅 12:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127820">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دو پهپاد حزب‌الله امروز صبح به یک منطقه نظامی در شمال اسرائیل نزدیک مرز لبنان حمله کردند، طبق اعلام ارتش اسرائیل.
🔴
ارتش اعلام کرد که در این حادثه هیچ زخمی گزارش نشده است و موضوع همچنان در حال بررسی است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/127820" target="_blank">📅 12:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127819">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t30KPqxoC--gNUq4SNExYrkAp08-7VXTa6DHcyzcYeVa5a08jSQdA6rf-oijJb15L4PXH3Nvt46QjSnBr7_0hzV_7ZWPH6odsTW_dELIa1w0s6DgBnaX4R3J5MfWCfSwZicY8pIn_yna6FSKZrfDUvH04eav6Azp10GcwFa5qVzfuMLod6mkLUOSNbxDIHmIxv8-YDdUgIcWtDoLhzgAgfZG32IUhTTXsqAkwfOcMEt8rCQiiiY2g7vC2BXR_L2IoRr5ALKJkvsrPJW11VyyNsVDVWGm7nm6oAfEULddclNREWk9WTNOavtjQcPGRsJumqSnZFonv8xND8Q73dnYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مانوک خدابخشیان - تحلیلگر سیاسی چندسال پیش، قبلِ درگذشت :
- اورانیوم رو میدن توافق میشه - بازی تازه شروع میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/127819" target="_blank">📅 12:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127818">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کانال ۱۲ تلویزیون اسرائیل: توافق آمریکا با ایران، اسرائیل را به حاشیه رانده و موضع تهران را تقویت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/127818" target="_blank">📅 12:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127817">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKf7hbHjLxy5AcOp1ds_bP4r7nmTxT2AJT_lVHW-dYqla1a1anY1dNqwrXgamtaHf5MGNN4BDGUh-fSd1HYNFmyfhaXuwgYbvD3zPgeQU9tMrXiD4WwU0f_K4YO_CcFT_uuDwt_UgPEaCgyqFCwRwx_AbqW9M-xbr6Jy4TMar-RJXKVUsoqLZUZ6u5yZY2Ijm50eBpmmtzeMRR5p-H33KimSowgqsx5JYOxp_7HDsmbAVmwPaMMZpuNC4-4KXQVAuDskcd1HFIxGpq7ulLc-AiOs7OuWhPed5Kckq7VZFa5rO_PMmnG7n9ehijAamX8JbJvdDY75_6DOCU7vgPiTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/127817" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127816">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
یائير لاپید، رهبر اپوزیسیون اسرائیل به روزنامه بریتانیایی تایمز : اسرائیلی‌ها در وضعیتی از یأس و بدبینی غیرقابل تحمل زندگی می‌کنند.
🔴
نگرانی در اسرائیل به دلیل عدم تحقق اهداف اعلام‌شده جنگ حاکم است.
🔴
روابط ما با ایالات متحده به‌شدت آسیب دیده و دولت آینده باید این خسارت را ترمیم کند.
🔴
ما از زمان ۷ اکتبر تاکنون این میزان یأس و بدبینی را در میان اسرائیلی‌ها مشاهده نکرده‌ایم؛ سطح ناامیدی به حدی رسیده که قابل تحمل نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/127816" target="_blank">📅 12:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127815">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار ناشی از مهمات عمل‌نکرده در تبریز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/127815" target="_blank">📅 12:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127814">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1101d09a88.mp4?token=p0ON-Yuq935EcvRPcJPlR5ho5JprCP4MwjRsalUc_DQixSN8n1byqNuyLH4iB2zbiZARxI1XS6hls-eSTTqz3EtZtSujD_W0XsL0rluO-TJRGs_nYV80f4M7OWCdeZHSfYvkzweg5Nwn9anggz2fIwzdMkIbCf_6tm2OxKQZD35zT2qbqgZVFppJmuJ8A4QuE17u3o1Y6e4yXAkRsdd_ZzMBmsNIqUVtt-KnfSTT7_u3rQWNr-8NjzXYKCessZevrOR0cSiqwTPp5T-XBAdvGXllcP_k9c0dpGr3YYN294yR9sFif_8BS2pPD_pjTxlHf-2lqhJUZ1c_BVJ6pXp4hjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1101d09a88.mp4?token=p0ON-Yuq935EcvRPcJPlR5ho5JprCP4MwjRsalUc_DQixSN8n1byqNuyLH4iB2zbiZARxI1XS6hls-eSTTqz3EtZtSujD_W0XsL0rluO-TJRGs_nYV80f4M7OWCdeZHSfYvkzweg5Nwn9anggz2fIwzdMkIbCf_6tm2OxKQZD35zT2qbqgZVFppJmuJ8A4QuE17u3o1Y6e4yXAkRsdd_ZzMBmsNIqUVtt-KnfSTT7_u3rQWNr-8NjzXYKCessZevrOR0cSiqwTPp5T-XBAdvGXllcP_k9c0dpGr3YYN294yR9sFif_8BS2pPD_pjTxlHf-2lqhJUZ1c_BVJ6pXp4hjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو پهپاد حزب‌الله امروز صبح به یک منطقه نظامی در شمال اسرائیل نزدیک مرز لبنان حمله کردند، طبق اعلام ارتش اسرائیل.
🔴
ارتش اعلام کرد که در این حادثه هیچ زخمی گزارش نشده است و موضوع همچنان در حال بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/127814" target="_blank">📅 12:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127813">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
داداستانِ استان اردبیل :  یه تالار تو اردبیل به خاطر برگزاری عروسی مختلط پلمب شد و صاحبش هم بازداشت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/127813" target="_blank">📅 12:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127812">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
عصر ایران: کسانی که با مذاکره مخالف‌اند و از جنگ دفاع می‌کنند حاضرند لباس رزم بپوشند و نه در جنوب لبنان با اسرائیل ، بلکه در همین جنوب ایران خودمان با دشمن بجنگند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/127812" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127811">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fb367f9b.mp4?token=Hrqe6VpEjIBylHag_FmzlosYuR2fe3HAlhJlIl_gXCkeRNwnkyvFcHk7eH2Jo0YEJTLCezAK4FYbqhIoag4h005NRKsndRcEeggjqUQq5r_sjz-AEFQyF4cioCqn-L6vCehktnylFAsa20Vh7nxoYvOWQHxHoR7_TSaTgRl3aEALOwCie2uhuueZoml1mKNmD6My5kJo5eOwY5y46LfaDvto9d4Mk8XWJjOVQvy8S6PtqAGHvLaBm_RylI7k0miTWINiCSfo-GFfestPkKUubGR9o0oWC16WJmhwpSVe0DHsEU3aMostDT9Bhjndw3YYsEUkOetrZbCBKVqRCBcg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fb367f9b.mp4?token=Hrqe6VpEjIBylHag_FmzlosYuR2fe3HAlhJlIl_gXCkeRNwnkyvFcHk7eH2Jo0YEJTLCezAK4FYbqhIoag4h005NRKsndRcEeggjqUQq5r_sjz-AEFQyF4cioCqn-L6vCehktnylFAsa20Vh7nxoYvOWQHxHoR7_TSaTgRl3aEALOwCie2uhuueZoml1mKNmD6My5kJo5eOwY5y46LfaDvto9d4Mk8XWJjOVQvy8S6PtqAGHvLaBm_RylI7k0miTWINiCSfo-GFfestPkKUubGR9o0oWC16WJmhwpSVe0DHsEU3aMostDT9Bhjndw3YYsEUkOetrZbCBKVqRCBcg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قابل توجه جبهه پایداری
🙂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/127811" target="_blank">📅 12:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127810">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FGblJBS7RUVv0NCTnci4auumSk1BGNy5T30RLzZ1-EvjcLeSVE_idbLC2lQZ_xLMsc9Td8RTsBZksb91OA2UbxMbshDd7sTvwcroqRvS5G7zGFUIIdNCFijCUNCuftqb27nmlttGyUDJS3Yog1WqnvmsMF73XoAmK74xE0UU7DVIhF5M5vbWb4PX4ePykWHARsrodabp81DWr8jr_moo1O9YE8cgSpBBtkXVFuHxeA6vkNjF5GAjQIo-8lf5XiYe2mHq-nFviVr8CHZ_I9Me84Hd9puXL3rnFaZKQuzLB99yVhVH7HjQQmJKIAhAjgHyrIIopMOiIBJHv8qmJMtFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کودتای تندروها علیه مجتبی
‼️
🔴
جلیل محبی: اگر رهبر هم قبول کنه ما قبول نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/127810" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127806">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47e6bdbbb.mp4?token=ZJj-LALVngoaFplAORmRx-U_WIqmPweDfrayYSYhhxxAd9MfvLeyWzaM3nk-XWvhAuB4pCHmwc1xP3vLQFzB7mT3xptiikds2Xc48NnrMSAM6JmaR09bL_YywCh2_uzHemCOHLcnoVqUvw1V7l3Aw5y2fuH1-t5SNudQNvgp7hF_3bzBRrha1ibJqZQOtZWhQnhP0wbj5HFR8fWRMY_u5qWbkegzVF4r0FNQbJ6QJ-EzC8m4E_xv6nT-BaXMKpZ5FcX9uVSUUCmJ_TiUgmms4aNu5tTe2NTYp-RoxMshnfBO6jTDS5NFr_wVeiaIyWxpNp1KP-2qII4LwQJDzP7cYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47e6bdbbb.mp4?token=ZJj-LALVngoaFplAORmRx-U_WIqmPweDfrayYSYhhxxAd9MfvLeyWzaM3nk-XWvhAuB4pCHmwc1xP3vLQFzB7mT3xptiikds2Xc48NnrMSAM6JmaR09bL_YywCh2_uzHemCOHLcnoVqUvw1V7l3Aw5y2fuH1-t5SNudQNvgp7hF_3bzBRrha1ibJqZQOtZWhQnhP0wbj5HFR8fWRMY_u5qWbkegzVF4r0FNQbJ6QJ-EzC8m4E_xv6nT-BaXMKpZ5FcX9uVSUUCmJ_TiUgmms4aNu5tTe2NTYp-RoxMshnfBO6jTDS5NFr_wVeiaIyWxpNp1KP-2qII4LwQJDzP7cYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین تأسیسات نفتی
روسیه
رو هدف قرار داد
🔴
حملهِ پهپادی به یه مخزن بزرگ نفت، تو یاروسلا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/127806" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127805">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
آخرین قیمت دلار: ۱۶۹.۵۲۰ تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/127805" target="_blank">📅 12:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127804">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نخست وزیر انگلیس کیر استارمر: صبح امروز دستور حمله به یک نفتکش ناوگان سایه روسیه که قصد عبور از تنگه مانش را داشت، صادر کردم
🔴
این عملیات موفقیت‌آمیز ضربه دیگری به روسیه وارد می‌کند و به کسانی که به جنگ اوکراین دامن می‌زنند یادآوری می‌کند که ما اجازه پنهان شدن آنها را نخواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/127804" target="_blank">📅 12:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127803">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بلومبرگ: ایران احتمالاً در طول آتش‌بس سلاح‌های پیشرفته روسی را به ذخایر خود اضافه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127803" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127802">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3fd105e87.mp4?token=pEKsDdjt_76Eab0uB9RCKzNgOlGKIws79lcEAV8f-AGf8dsUNJOLSkZue7TOJKwyYCAHK8KRxvrvl-OHu6HC143DluZB-zDYc_ntnmJW-5VUWlFWCuSMKV4XsbfSbILdgTDuDfHY47rGBAXwOll9n_tDQzvL3AsSu3s_z2VIqR31FL94Ako1o2KMbUKgM6CPiC14tsJCdOlTgCsf9MYyIe3yKU26ZxISLY051L3UC7zSGTIpQS_IQuWux2GD79EXp4Q9jee2AMnwTcX4udMqePaO92TyFyuxrNxbcvBR2S3zNn3MiJnfQFzqzu1BIHONSk-spfXjkiW3kv0t7E-Wyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3fd105e87.mp4?token=pEKsDdjt_76Eab0uB9RCKzNgOlGKIws79lcEAV8f-AGf8dsUNJOLSkZue7TOJKwyYCAHK8KRxvrvl-OHu6HC143DluZB-zDYc_ntnmJW-5VUWlFWCuSMKV4XsbfSbILdgTDuDfHY47rGBAXwOll9n_tDQzvL3AsSu3s_z2VIqR31FL94Ako1o2KMbUKgM6CPiC14tsJCdOlTgCsf9MYyIe3yKU26ZxISLY051L3UC7zSGTIpQS_IQuWux2GD79EXp4Q9jee2AMnwTcX4udMqePaO92TyFyuxrNxbcvBR2S3zNn3MiJnfQFzqzu1BIHONSk-spfXjkiW3kv0t7E-Wyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترافیک تنگه هرمز نشان دهنده عبور کم تعداد کشتی ها از مسیر جنوبی تنگه مطابق مسیر آمریکا
🔴
نکته قابل توجه گشت زنی دو شناور نظامی آمریکایی در تنگه هرمز ، البته نوع این شناورها مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127802" target="_blank">📅 11:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127801">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6-JJcU7KWd6KTYDFz1o1rzT8kdz3MrWI7Jx6KdUcnHoqZTo5KQjIRf77u-TZAd382ZT_Qzf6PBJNtPbPKckxuM5ECCJ8-EMCxMnnvibRYoX7ZWW0o_rSdPlyT0sGYRue3inM5b4Dcj0p1ALdQHawNeLA0xvyS69tg3AicMWBCr75yc6lioBHr2mmo76YnMbfkA4OvkCHaIhOApE4oJf4cUjZnwW-Nq9PatNWdN3AdTCJ5AplaSCYjtPMP2QjYtDADn3AKPdSqwGzCF5vTA5G1Uf-Gba6XFYBeCIWT1CqBPojFHxK1Wml5Rw127-r4Ruse_M8nunaKTWznRBsEvR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ امروز ۸۰ ساله می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127801" target="_blank">📅 11:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127800">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8WlNmP5uiSlTmFuMcQY82aErgWhlwufgCHGoyGhVa1T10XS_BWyg2Uiz-4SidXO7T49rwbOQItqxAu9AFM5wWS0V0W3CYBUZ27t8w8SgpeCMmprnJP9x_-wZBxvyP1wrCyo3SgaWZ7N_OMyVS1jU0ySZTIcMONqtRJg3KlzrDyn0gqB7719VIfNVNlzRSwz8jfIsmhqVsEZEaYqxOzd-HQ_r6GNwEsCadIMO-eQ6TniF9T6S7UwejTD-Vw3-07OOGir1Hxq4PpmXWTjfdectGfFHa6Pr6e82j1Atp2HHQ2H72AgEd0ewMYkCI9BRy84VFOR2LVcMml4LivD8ByuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایندیپندنت
:
ذخایر نفت آمریکا به پایین‌ترین سطح در بیش از ۴۰ سال اخیر رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/127800" target="_blank">📅 11:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127799">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مشکل خدمات بانک‌های تجارت و صادرات رفع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127799" target="_blank">📅 11:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127796">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXif8_hhZxUtDFyDliBov9hY1SPcZAsAYKZbTOJAQxW4yE7wdOvRN0lUUzBWfHRlNYKeVdxU7IA3-gHs5RsFVHzVyD4ilKvnhMsk1YV6DZC97s4l2quPmzRSbKrwFkdGAkuF5t8SL4AmKuAbj4JchydypHa5sQ3v1J8Idqsgz1INRMhIJGeEFEcrDlzNpRefKi3ONGnmMAHzGObjFessMx7r-s-A2EB4cMqzMB1B6nWn4XAglLFLLXB-aGyLh8r16NDd2DNnP_MYnqYPBmPRFFB3xEfjRSHGbGlYRNf0mpcm9vYtUMnO8Ws8GNLZ3U06aVLis-w7wkiBTGgY_viBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FL6WJV5C7XSID0Fu1W3yTrJeFF4qJHR_Lry_NOo2JrT5euMsABCvq4NlbKeAPrGyNSh_8LakMu1YdDLzgJ0zYHHCIkFBbMn2aXfUzvicHDI8T7TTKQAp_C30qo0kmUZGtXmQWlDlluoayr2n_mZEsqUVs7L03ayH0m5sxpg6Dmx665DSrDNH4lKKBQdTQ3Y8ZcxGeoHWgflIgsfCBL0ebePdB8vi1nCohP89e0RnFWZh60Ft_k0EngnrLVrWnMU1tzXsq1InhqrzSX1kAKoyMH9lB1j4J5hisZiUPYcZm-9MWH5nmIWB5XX6c-DlQUQW_YmdL_FOD4hu_VtupcGtBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86af934eb1.mp4?token=eCRbepeXGxyRxBYE05gB654RCgbgeFvtcP55WSJCDtzOp3nyN_UE0mrEqeNJeIk1s3vwCUO1wqBgP0BYHA8222LEBfIdpinbohS10M8WxnXz6Oj_JmCTPwOzoj7nhIS7clj5gcRVZOLY0awUjYdzLsmtY4J9ldTnEJp9fcUyBArxE520H8KYTop6Zjek2m2z69GD1EDB9D02M1xUFJRS9TNw71WmWGMFk6c1YfcDMw3gNTgp5q3nCFWRvSZWqGEiOdGAwe__jq9PkWDL6Pj5HSATcNr-0RHFcsgarmYAfVNH2j2CDxfl7_B9aET0Xpf_7UtdRBvVBDz0MMn11A4NIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86af934eb1.mp4?token=eCRbepeXGxyRxBYE05gB654RCgbgeFvtcP55WSJCDtzOp3nyN_UE0mrEqeNJeIk1s3vwCUO1wqBgP0BYHA8222LEBfIdpinbohS10M8WxnXz6Oj_JmCTPwOzoj7nhIS7clj5gcRVZOLY0awUjYdzLsmtY4J9ldTnEJp9fcUyBArxE520H8KYTop6Zjek2m2z69GD1EDB9D02M1xUFJRS9TNw71WmWGMFk6c1YfcDMw3gNTgp5q3nCFWRvSZWqGEiOdGAwe__jq9PkWDL6Pj5HSATcNr-0RHFcsgarmYAfVNH2j2CDxfl7_B9aET0Xpf_7UtdRBvVBDz0MMn11A4NIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ به لُبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127796" target="_blank">📅 11:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127795">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
منابع العربیه: قالیباف و ‌ ونس توافق صلح ایران و آمریکا را آنلاین امضا می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/127795" target="_blank">📅 11:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127794">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: نخست وزیر و وزیر امور خارجه کویت ابراز امیدواری کردند که واشنگتن و تهران به زودی توافق را امضا کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127794" target="_blank">📅 11:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127793">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
خبرگزاری فارس : جمهوری اسلامی هنوز تصمیم نهایی خودشو درباره تفاهم‌نامه، اعلام نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/127793" target="_blank">📅 11:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127792">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ایهود باراک، نخست وزیر اسبق اسرائیل:
توافقی که به‌زودی میان ایالات متحده و ایران امضا خواهد شد را می‌توان در یک کلمه توصیف کرد: بد. و در دو کلمه: بسیار بد. و اسرائیل بهای غرور و کوربینی نتانیاهو را می‌پردازد، و حتی بهای مانورهایی را که او تلاش کرد علیه ترامپ انجام دهد.
🔴
ایران قوی‌تر از قبل بیرون آمده است؛ در مقابل، اسرائیل پس از شوک هفتم اکتبر دستاوردهایی کسب کرده است، اما ضعیف‌تر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127792" target="_blank">📅 11:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127791">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع آگاه: تیم مذاکره‌کننده قطری صبح امروز، به عنوان بخشی از تلاش‌ها برای دستیابی به توافقی برای پایان دادن به جنگ، به تهران سفر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127791" target="_blank">📅 10:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127790">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkmH9RM7AqVzTu1jXeY5p_6iyYwkG0Sx5GfhJCSDrFPO5O1PnS58Nwpn77C8uN0ON18pODtyTjqRT_yqIKTI5FsD28Djsk-1ebKKgB6bL_QpM11fUiW-Xblb9t2OVxxSBeJ4gJdz7Ox9QucYcBDiT_JJ8Smk8eajk8GLspK-wVktzGGO97hRg8HVCToUXqTxHR1xbaz1mZPoS5Ds4-C4n5ToZVl8xqIX0znrN-OEQINOKgle7T-nksuoelwu93Gs6TNHylglqT68fc-fWzbbDWmI5EcntoSNqpnHnYCbnxSbcFC4eDomXqGISdxnLESGPb1VpU02-XN_2zJXjICNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامران غضنفری نماینده مجلس پس از تهدید مسعود پزشکیان به استیضاح: آقای عراقچی غلط کردی دور دوم برای مذاکرات تعیین کردی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127790" target="_blank">📅 10:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127789">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سی‌ان‌ان: مذاکره‌کنندگان قطری برای نهایی کردن تفاهم راهی تهران شده‌اند
🔴
شبکه آمریکایی به نقل از یک منبع مدعی شد که مذاکره‌کنندگان قطری صبح امروز در هماهنگی با ایالات متحده به سوی تهران پرواز کرده‌اند تا به تسهیل روند نهایی‌سازی توافق (یادداشت‌تفاهم) بین ایران و آمریکا کمک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127789" target="_blank">📅 10:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127788">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
العربیه: امروز نشست مجازی میان هیئت‌های آمریکا و ایران برای امضای توافق صلح برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127788" target="_blank">📅 10:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127787">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
الحدث: پس از امضای توافق، محاصره بنادر ایران برداشته خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127787" target="_blank">📅 10:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127786">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
الحدث:یک نشست مجازی میان هیئت‌های آمریکا و ایران با حضور میانجی‌گران پاکستانی و قطری برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127786" target="_blank">📅 10:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127785">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اسموتریچ، وزیر دارایی اسرائیل: به ازای هر حمله‌ از لبنان ۱۰ ساختمان در ضاحیه باید تخریب شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127785" target="_blank">📅 10:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127784">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزارت دفاع انگلیس اعلام کرد که نیروهای انگلیسی صبح امروز در کانال (احتمالاً کانال مانش) به یک نفتکش متعلق به «ناوگان سایه» حمله کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127784" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127783">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
گروسی :نظارت و راستی‌آزمایی آژانس در هرگونه توافق هسته‌ای احتمالی ایران و آژانس نقش محوری خواهد داشت و این نهاد با هماهنگی شورای حکام برای آن آمادگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127783" target="_blank">📅 09:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127782">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
الجزیره: ایران هنوز تصمیم نهایی خود درباره تفاهم‌نامه را اعلام نکرده
🔴
می‌توان انتظار داشت که توافق امروز نهایی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127782" target="_blank">📅 09:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127781">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247968d991.mp4?token=OxjzbqNdh5j6R7sP3JhB6Au8P7DNEtog1s86MNCwzG2Z6gSJ3i4K23ARuLonJE8EYfKIEyf_OO4nejLUOBGSEssXaFLf-Su-Qw3h5op9E5XovmSlpIexchgFEGI8THleaYimSj198NvROVAAp-Lcb7btNYQVk2Pg4PgjvZnFf9xbUmduBcT5DwCwDpprOzOqNza8y8tObHz0H8DS6sgZOBgDCtxMDKOC0rUQaU-6uiWIuVeFrXr_Z7MSTHrtJV3HeGbusQMG-VJWpKQqDVHaIJxJbMPaA4mUC_8mShfsE6gQcOOlx4XNMdP1bs2LK9q2YIMrfemwq64gsP7omySwPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247968d991.mp4?token=OxjzbqNdh5j6R7sP3JhB6Au8P7DNEtog1s86MNCwzG2Z6gSJ3i4K23ARuLonJE8EYfKIEyf_OO4nejLUOBGSEssXaFLf-Su-Qw3h5op9E5XovmSlpIexchgFEGI8THleaYimSj198NvROVAAp-Lcb7btNYQVk2Pg4PgjvZnFf9xbUmduBcT5DwCwDpprOzOqNza8y8tObHz0H8DS6sgZOBgDCtxMDKOC0rUQaU-6uiWIuVeFrXr_Z7MSTHrtJV3HeGbusQMG-VJWpKQqDVHaIJxJbMPaA4mUC_8mShfsE6gQcOOlx4XNMdP1bs2LK9q2YIMrfemwq64gsP7omySwPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمید رسایی: اجتماعات خیابانی فقط با محو کردن اسرائیل از روی کره زمین تمام خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127781" target="_blank">📅 09:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6NrvdvI6Vux3q_1Mb-pl0T50NIUg7yjx9DvCuMWAjs2EkhyqrG_J5h98NDRZtHxVrY_aIfUO1fzPJi7Cya2iRe3TTo99fn8mHSutyZCmKWsSuAaz9CYX-5MSVHOExe22NlCJfyzFjJFiIPsH0zVbfV0uNId20o3BjucINAFQYB6v936uzYTU1ALMU-Zai4qdYKT5YXwjDfdegeCWsxUrMHE2KaS8JycV916eGaA9qYu-m2F8Del-mX0u4p1Bgxvv8ySWFyyPb2FbkCTP7I7dbuNs2I4-3a3KNzYdPwQurIAIrAIh4AiQBfLZ3tnRTYgRX2KxoFRzClaNcWx9AWBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۱۰۳ هزار واحدی شاخص بورس/ یک واحد تا کانال ۴.۸ میلیون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127780" target="_blank">📅 09:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127779">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: نخست وزیر و وزیر امور خارجه کویت ابراز امیدواری کردند که واشنگتن و تهران به زودی توافق را امضا کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127779" target="_blank">📅 09:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127778">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک مقام بلندپایه در دولت آمریکا: معتقدیم به توافقی عالی و بسیار مستحکم دست یافته‌ایم
🔴
ایران تنگه هرمز را بدون دریافت هزینه مجدداً باز خواهد کرد
🔴
محاصره آمریکا هم‌زمان با بازگشایی تنگه هرمز لغو خواهد شد.
🔴
مرحله بعدی بر عملیات مین‌روبی در تنگه هرمز متمرکز خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127778" target="_blank">📅 09:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127777">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsMHwhlSml3mpbkc303s9eEjIIE-tJXnQtX8YT_tUskqZMBI7eclEIGCcuCGFl0vTMM2Ac5aQ2e5Rtavv5D5jeMe2CZv2LpQzCDDDMcREF6yTZNU2CN7GpghuFiE3gxrja3o54V48uw0iS0-GkGoC9GRn3PzR1AQXSC4iMfi7KbQmbMMHtxF3-06f4qKAxqbsj53WsO1PRnBOAgC9y15Sl2TfRqOKKqOD19C-X3v35ONRhlx17ODEcq-fYYPj9ffPXv_jHlj_xqJ1_JSPCH90rNWNHP1JeE5b8vUfVeJTZvorz5iHrQ8Hu4U-SXkGJTckx-sOHtgqIwmYcTwA6_6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127777" target="_blank">📅 09:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127776">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
آغاز توزیع کارت آزمون‌های سمپاد و مدارس نمونه دولتی از فردا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127776" target="_blank">📅 09:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سازمان هواشناسی امروز (یکشنبه) برای مناطقی از شمال غرب کشور و ارتفاعات البرز رگبار باران و رعدوبرق پیش‌بینی کرد.
🔴
این شرایط فردا (دوشنبه) در برخی مناطق شمال غرب، شمال شرق و استان‌های ساحلی دریای خزر تداوم خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127775" target="_blank">📅 08:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزارت علوم: تمامی امتحانات دانشگاه‌ها که زمان برگزاری آن‌ها با مراسم تشییع رهبر  تداخل داشته باشد، به زمان دیگری موکول خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127774" target="_blank">📅 08:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCHKPR98hCtlG2RujwmlIdQXMDhRVz5cVlzld7LGH_UhYuSC1dvIaFjjd492x7uYrzJ8lWqJWW5ct3QDjTuu7Lbw0EJRQhlfnK_oHwNooZxoBpuuDvGkyo_kctxx31Uk8fHCz_MsEIuF8yLch9Pr9mvMKLHkAHBLBDym7Czk7W2XmHYNFRN9gx_EkmBjD29T1YFZx3peInu3o4sNozdUnJbRyITM64AoB8lHD8JFKAUfZYnXlGBTb_NuTsjwJj9mwBiGm4ZLBORAV8eXuCAj_8LGJinSGJVf8ajSoniDypNIdjz5yC1ZUDjnL55Ho-idRc2Y2DJgrd7IcxDOZ4P8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه کره شمالی: تأکید و اصرار آمریکا و کره جنوبی بر خلع سلاح هسته‌ای این کشور، بی‌فایده است.
🔴
خلع سلاح هسته‌ای موضوعی مختومه و برگشت‌ناپذیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127773" target="_blank">📅 08:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ می‌گوید توافق صلح روز یکشنبه امضا خواهد شد، اما ایران درباره زمان‌بندی آن تردید دارد
🔴
نیویورک تایمز نوشت: یک مقام ایرانی تلاش کرد انتظارات را تعدیل کند و گفت هیچ برنامه‌ای برای امضای توافق در روز یکشنبه وجود ندارد و ممکن است این توافق در روزهای آینده به امضا برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127772" target="_blank">📅 08:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
انفجار کنترل‌شده در محدوده مبارکه اصفهان انجام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127771" target="_blank">📅 08:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
کابینه امنیتی اسرائیل امروز تشکیل جلسه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127770" target="_blank">📅 08:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c5f37363.mp4?token=bLdRZlZoyBAxA3lrqh5zW8EQfJdPIDK_Vi-zhw7dFT839nFeHKl6_7mmlj9xYWLeNfKwtEPQDWNWOHHekzH8tHUg81hH_W1CrsovOg0TjO_FUMrhNSRcq8nIEGGGx9tZkLHACdOnEIYvUeifqMXEnVF5d6wl8WLMudkvmhqXO3jT_aL0EnDwCteeQV-fVFbhiop_1hZf_1KXTL6TW_-zmJFv6geMj3AmZdx8B7Hte9zjfapskk_DblZobwfmk2hncIWUGnEIE5jrf-PuiehcVY25SdJGhi8JoQ87Mb8I66dNmbHpOyo1c6G40sTF-HwKh_KN_srLPzdBT-Ju4Zy-BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c5f37363.mp4?token=bLdRZlZoyBAxA3lrqh5zW8EQfJdPIDK_Vi-zhw7dFT839nFeHKl6_7mmlj9xYWLeNfKwtEPQDWNWOHHekzH8tHUg81hH_W1CrsovOg0TjO_FUMrhNSRcq8nIEGGGx9tZkLHACdOnEIYvUeifqMXEnVF5d6wl8WLMudkvmhqXO3jT_aL0EnDwCteeQV-fVFbhiop_1hZf_1KXTL6TW_-zmJFv6geMj3AmZdx8B7Hte9zjfapskk_DblZobwfmk2hncIWUGnEIE5jrf-PuiehcVY25SdJGhi8JoQ87Mb8I66dNmbHpOyo1c6G40sTF-HwKh_KN_srLPzdBT-Ju4Zy-BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت:یک فروند جنگنده اف/ای-۱۸ هورنت متعلق به ارتش تفنگداران دریایی ایالات متحده روز شنبه در جریان یک پرواز آموزشی معمولی در نزدیکی دریاچه ریم‌راک در ایالت واشنگتن سقوط کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127769" target="_blank">📅 08:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بریتانیا در رتبه‌بندی جدید ناتو در جایگاه ۳۱ از ۳۲ کشور عضو قرار گرفت و تنها بالاتر از ایسلند (که فاقد نیروهای مسلح است) ایستاد.!
🔴
این ارزیابی میزان پایبندی اعضای ناتو به اهداف مربوط به توسعه و نوسازی توان نظامی را بررسی می‌کند و همچنین توان ارائه برنامه‌های واقع‌بینانه برای تحقق اهداف دفاعی این ائتلاف را می‌سنجد.
🔴
طبق این گزارش، بریتانیا همچنان با چالش‌هایی در زمینه نوسازی و افزایش توانمندی‌های نظامی مواجه است، هرچند دولت این کشور امیدوار است با ارائه یک طرح سرمایه‌گذاری دفاعی جدید، جایگاه خود را در آینده بهبود دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/127768" target="_blank">📅 08:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فاکس نیوز در خبری مهم اعلام کرد که ایران تنگه هرمز را در عوض لغو محاصرات دریایی آمریکا باز خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/127767" target="_blank">📅 03:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127765">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNqCB-Ayma5ZePXfL-merplQBGeq8jdT4XVV5mmaEm5G6IyMBB2uhEQ7Vom4HEIBdVOqQH_JlRQA7SWGHWLO5_2-DE6wK2GywxfZfnj2moBLK05iEDW3ZgNtSIF5nZUtL-WdguADzyIXS5MWyfNlE0aZzmDLCcXg5j04mkIb5XuBz2JEORzYqBU6oPSBSNnE5edW9DcbLi0QRRuBfdllQoBPtybh7dLhPOy4RHKpqW9rPWd1eZCS-g-XermTUSOQzqkxiChpDRU95uWd05Pv4VksxoKVMG-jZUSiPW7nl73wlTq5qNJ9LIF0vcueEdgMQn3oat5_KKFFkT2mmCFjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wk_STw7e5Qjns_JJb0AnGNHwbOe7xlF7Tr8EJoZVskLIRwPUImhWN-7_x_lYENsp9ONvWXW1XlyXKKmZy9ydRKdo1833bJ0BgzAnyHDbW-kQ_sNqAus2Mpi6scnVnkQPkImIf2yM-0buaHx7gck_bA17H-xlN1yn8wpjWgJiBezx6kvMhI_djRCY3LloghZXkBJ1XcpEWITirW69XzuXnbM9D53W4inCD9nWHyrXDrRyKRH-FuAWUfnWbSxvWtM6FVZCXnPHC4GpxP6DhP1_LuR9Hr2Xrq7lebxWA7OjSU1_-puCX1RiHW1XwtfIAm9w7WVnO-S-q2isU0QI2AYqng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
امشب تولد‌ ۸۰ سالگی پرزیدنت ترامپه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/127765" target="_blank">📅 01:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127764">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee53f0561.mp4?token=N8mqst9JiX9jW-VLrTj4BfwmJFQ7G6N3vAJ7R1UWJMC2GwhFH_C9bJjqTGBjdSY5zqns5U-R8f341YieLzKHwsO1afgjITTpbcFyTgNTCrmWCS-WDMhi4BaC-N_A-6IG-ZTsiEclNlYmltzGpDsz33KhzRxnD8XbQH4Z77uIDF2szuiCGlvjudKl8J17TyxggGPt24TZk7yg4HmhtUBj-fEtUbolbavOMztuo-zhXjHOeMle_v8_IZh0YIcHRN8WvrYQ3FgJaJ0KrzFhOoV2jC14uYP7Log8ZI-2zYA8ayjAWWqTzk6VlcWFSOh41b_RhAfdZABlyZqfSLBvJgrnQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee53f0561.mp4?token=N8mqst9JiX9jW-VLrTj4BfwmJFQ7G6N3vAJ7R1UWJMC2GwhFH_C9bJjqTGBjdSY5zqns5U-R8f341YieLzKHwsO1afgjITTpbcFyTgNTCrmWCS-WDMhi4BaC-N_A-6IG-ZTsiEclNlYmltzGpDsz33KhzRxnD8XbQH4Z77uIDF2szuiCGlvjudKl8J17TyxggGPt24TZk7yg4HmhtUBj-fEtUbolbavOMztuo-zhXjHOeMle_v8_IZh0YIcHRN8WvrYQ3FgJaJ0KrzFhOoV2jC14uYP7Log8ZI-2zYA8ayjAWWqTzk6VlcWFSOh41b_RhAfdZABlyZqfSLBvJgrnQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما: خدا شاهده همه اماما اهل مذاکره بودن و با دشمن‌شون گفتگو میکردن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/127764" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127763">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWpN1jWdnhdmz-KPXvzsbTpmv5Auibe6DMG201pbDydgek4Om539X2g53FrxP88lCgQm7JWPmfD9SUpk7HhDsRw942luriEoXBlQGHUxt3-UVLL4CT3hjHdq9xZX59P8msxX9GrATu2_rKjovkgeYE3bZo4fqlE_w46QKzvqi4Iy2l_RPN1YhYvUNskkCMmCB-hcrq-vVM6gO37bEAe1OwPsHwBlHkgnm0FM45dnS55YfmtxLCa8d9j9LdVdI1qvksnE0eXDkrlxKgTTS6qgDz-k0-urOuQDyS3sxM20b08PQ_Gom7WuTfXbtSqLN4bt2UHRdWtDhypiK-PexeZaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور: میتونیم رمز ارز به نام علی خامنه‌ای بسازیم تا همه بخرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/127763" target="_blank">📅 01:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127762">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
آبروریزی تندروها در همدان
🔴
صابرین: ساعتی پیش در همدان و در مراسم شهید شادمانی درگیری رخ داد؛ عده‌ای خاص با برخوردی تند و ناشایست (مخالف مذاکره) مانع از سخنرانی بقایی و حاجی بابایی شدند و حتی به فرزند شهید تنگسیری نیز اهانت کردند!
🔴
دختر شهید شادمانی سمت آقای بقایی رفت تا از دلجویی کند اما این افراد در مراسم شهید شادمانی به دختر شهید اهانت کردند و علیه او شعار بی شرف دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/127762" target="_blank">📅 01:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127761">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiv5GNsPFY5X2htjIqd3suAbqA6-DTVjoGzViKBy5BhKAryVGyu1cq3FHnv1JKyMdBK221jzxSP_EM_sabkBaoKdzxTMAFpNcLkQc7JBFV5eWFTa3lzIOV_ZUbiKMr58WIxgwlZ61X1T5bUCddC3yJxAbIRN-Ap5aPn8w-HG5jhv8oNHCefBi9lqa1OVFnX5TRBsA2Km-OWlSgO38GwauGxm4EsbyFQh4Vt1jUdUPd16QEoTrR8kwfv4dm4-JsuqhHHBJtpw-cBdauVl75SuEHM8VVhgp3YdcrLrC0lI_qOZonxCQ1onb53lnYrquzcvnwLODXtR2g555IemJuuysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش‌ها حدود ۱۰ فروند ترابری c17 از کشورهای منطقه بارگیری کردند و عازم اروپا شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/127761" target="_blank">📅 01:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127760">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adca31cc4f.mp4?token=d7IOuGbyktLAqaPtrFyJLjCR013skRZpYew57YsBe7N6XXrPpuPd-k3bHxLqz9Bjwnw71rgkBn3uLTNZRebyfQei089w2DhCoQfepH9IEwnmVxjPNIIbdbERs9Y60FWQWe5bQfJgvhB4fu6MHzXwDVNFhGI3fDLTjJFLsDoyFNYSKl3B5hxcNK1Ike9T6JMJ7qFsNkY0Z8WYy5LCCmpJ5BaxJoOeG-FTXPuhCTSb40ZB1fYYCtBE7_gvLcEn2U7wQqSWl6-CBd2iq77ptBjgkyUIYPPIK1AEHQ0dlEcBV4uKGxcCZTTWQP2Bntpq2R9ypQXEwiehhQxkn6U5MGsO-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adca31cc4f.mp4?token=d7IOuGbyktLAqaPtrFyJLjCR013skRZpYew57YsBe7N6XXrPpuPd-k3bHxLqz9Bjwnw71rgkBn3uLTNZRebyfQei089w2DhCoQfepH9IEwnmVxjPNIIbdbERs9Y60FWQWe5bQfJgvhB4fu6MHzXwDVNFhGI3fDLTjJFLsDoyFNYSKl3B5hxcNK1Ike9T6JMJ7qFsNkY0Z8WYy5LCCmpJ5BaxJoOeG-FTXPuhCTSb40ZB1fYYCtBE7_gvLcEn2U7wQqSWl6-CBd2iq77ptBjgkyUIYPPIK1AEHQ0dlEcBV4uKGxcCZTTWQP2Bntpq2R9ypQXEwiehhQxkn6U5MGsO-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های یکی از لیدرهای شلوغی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/127760" target="_blank">📅 01:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127759">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h1RnV0xb_yd0Gl9xfQNk_v1QITQTFVVF-BrqB2ACUGMh8hrkW8AHfx07T1skLiZRHW_nS1jzfgMZrpdOOUJMwUQ-RPxUjrxbZfWfoJPg04omYNmsJf-GjtAo15QOpFihD262rVuhyDXx4Qb0cAy6ioSUahTPiYbNuCkY1NGrckfyO070_T4R02KSbaJpZzej91AXOsp8JhurrMPrHHtMluFsaA8S-mq6tF3VOCJ5kvqUTYk8glClRTcgCmKbIoF8pV8GEencbeMR80ae_APL-d2OYS7eOOrO62p3JW0j8GVIdpHTmy33mrjSJy1j8kqS_qGEvsyk9xT_Uh8vJ3NtaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فقط عباس میتونه جوری توافق کنه که:
جمهوری اسلامی ناراضی باشه
مخالف جمهوری اسلامی ناراضی باشه
اسرائیلی‌ها ناراضی باشن
آمریکایی‌ها ناراضی باشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/127759" target="_blank">📅 01:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127758">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خروج تعدادی از هواپیماهای سوخت‌رسان آمریکایی از فرودگاه بن‌گوریون!
🔴
تصاویر ثبت‌شده در روز شنبه نشان می‌دهد که شماری از هواپیماهای سوخت‌رسان آمریکایی پس از ماه‌ها حضور، فرودگاه بین‌المللی بن‌گوریون را ترک کرده‌اند.
🔴
تنها تعداد اندکی از هواپیماهای سوخت‌رسان آمریکایی در محوطه فرودگاه باقی مانده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/127758" target="_blank">📅 00:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127757">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz5UfQ_X5OIFh_F8HEgGCaSXXSNE_j38NIGoc427ZdU4g9McX3GNzc2vRi6t44GyBUtz2TomvvZBTm9xHN35UWlwdXGAlTsFiXre2FMVlLx3H5zfS44HQT90ewFnmJaFw7cMDHhEEdN1_RJu5SQ2DYNUXTUXQmoQBE0N34_WnsMBYc7V9dW-B_OU9pYlm0aZz74L76TAgaECs9yF4Lqjr7-pjyhLlghKGsaAZ2GG1_II7UPWygC45nn77xfM0J6g99FR0KheQhsZzJcThprsLpgK91LOJcpU26JwaIbTsd5oZDBvgth_Acz6GRfzKBmtH9M_PrVgIycCw64U4KUnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین طاهری مداح در میدان انقلاب: تندروهایی که امروز شلوغ‌کاری کردن هم ردیف طرفدارای پهلوی هستن که شلوغ کردن، باید مطیع رهبر بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/127757" target="_blank">📅 00:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127756">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=MztnWDCwSiWYBiA1FNl0IngH3jDHSS_API8kuoSnHXaBihEzJ6KaSWH04_q1EDPJ0xiOAF3URmSTm50Kb1sUYpuzm9ciKvFLVJq9pNTIhgqTPdIxA2bOr7vPyfJhRr7uXu-bfJ7tOHkzb6Wm-8JT2hIhHqZZn9-ci_MYKU2cmLAYe1wzkF-_E-OLLWQGplavuKKlcJpoNQa1UAKvKV8VAvfdktqTYFDK-5yX6rQXC6Y9_toYWDK3gGAYmZMrFLkznRdGFUfSuDHcv_HsK8DGPpa7BLWjK89C54iUIypKBa3CR2lO1RxW1vasN9uslLYIPksbtBr0jAq2oUtRqHmsoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=MztnWDCwSiWYBiA1FNl0IngH3jDHSS_API8kuoSnHXaBihEzJ6KaSWH04_q1EDPJ0xiOAF3URmSTm50Kb1sUYpuzm9ciKvFLVJq9pNTIhgqTPdIxA2bOr7vPyfJhRr7uXu-bfJ7tOHkzb6Wm-8JT2hIhHqZZn9-ci_MYKU2cmLAYe1wzkF-_E-OLLWQGplavuKKlcJpoNQa1UAKvKV8VAvfdktqTYFDK-5yX6rQXC6Y9_toYWDK3gGAYmZMrFLkznRdGFUfSuDHcv_HsK8DGPpa7BLWjK89C54iUIypKBa3CR2lO1RxW1vasN9uslLYIPksbtBr0jAq2oUtRqHmsoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار در تجمعات امروز: اگر چیزی امضا شه، مسئول باید کشته شه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/127756" target="_blank">📅 00:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127755">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olonb5p5FTwg5Jh8sTWqF_SdS039boGqfCcxKbGGfydrOJ5-9C7QEYHdIfsoWq8oHBGuY4LHqg_bdjHb7ueiClltNm9aXO1oI6UqRy1AF3Z0HTgr8zRwEyuSTrsPeN9RG9SUzdYFRDl_5DguZgmnuUhwyfbIkhTJpUe1CGkIS9ruMzfqDCYyBVghr0d5lAHu8YxxXallMmUAaYNC3Gne47IiNCbPQeth_GuU_ikmgLQxK476A9XE4JkM1HwTgD7CSSC89KthPAVkGq7JZ5b2zsEp3Y_XU0Jp2No4QFtlyXL-HI5zob696RN2Ij_dMrxhY3OQT6UkNYFh0zv-q4ESzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح از روبیکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/127755" target="_blank">📅 00:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127754">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt_xwQDbesDzyUIDPyhuooPTQoDwZ4NmxjwmeHmSUJE-LGtG4YZlepgD_3wiypWOSr20833LEkMA-C2pBJxmEa8TSrSxc3CcsAFcOeS_ZDAomMLgOHEedbb2VUbs7M8WmHulJom0qXKaR7aidDRcd5D0nx4nrxXmamUZK2_R-FMP_C1DUn2Vapp6lj4Bf6rcFeungr8E6T3CDWTRsHtMRrUdNaVmx2WwnTkQhBnBKfxy9N2fHT5IdlzeXZUHxevxWRNvhg3GxnfZBuBgwcAjEZl8L3HeWiRVlLia_19psEQ_C8YbCcW-aEipo6vTIG_wxonJJU9smSSJulnCyYFOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست یک کانال مطرح عبری در تلگرام در واکنش به تجمعات پرحاشیه امشب:
خشم بی‌سابقه‌ای در این ساعات خیابان‌های پایتخت ایران را فرا گرفته است. هزاران معترض حامی رژیم به درگیری‌های مستقیم با نیروهای امنیتی برخاسته‌اند
🔴
وضعیت بحرانی – فریادهای مستقیم علیه رده‌های بالای حکومت:
معترضان در تهران سد ترس را می‌شکنند و خشم خود را مستقیماً به مقامات ارشد رژیم معطوف می‌کنند. فریادهای شدید توهین‌آمیز اکنون در خیابان‌ها علیه وزیر امور خارجه عباس عراقچی و رئیس پارلمان محمدباقر قالیباف شنیده می‌شود.
🔴
توافق با آمریکا در خیابان های ایران به عنوان «توافق تسلیم» شرم‌آور و خیانت کامل تلقی می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/127754" target="_blank">📅 00:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127753">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
واشنگتن پست:
قطر به ایران پیشنهاد یک معامله مخفی علیه اسرائیل و آمریکا را داد که بر اساس آن ایران به قطر حمله نخواهد کرد و در عوض قطر تولید گاز را متوقف خواهد کرد تا قیمت انرژی را افزایش دهد و غرب را برای پایان دادن به جنگ تحت فشار قرار دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/127753" target="_blank">📅 00:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127752">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d50508a6c.mp4?token=dswS1tVGta5DiLNl5QyxOCAHU46JH79IqXOnju0Xl3_iRto0f9tt6QFiZ6geQ7lGO3Yo_rtJ_G-TnotuzOYNYv4nV6YA8uHtYQH2rZWDRgYn7EX0vyfRjzwebsiUEd1wmDNuQ7A1coR0x495__81sPGNrC8lIfOw-Aqw9dJjGwdDPyNAZfcGD04yeTf09sHm8FlW-J66kzHVc3nNxrd4HQXLPM2UQ9Txe9MxScDP5RbSkt_yKz5QvAwkvW8bUiD1WGWHablsb5WtT6tuwvzTDVOxbzhAEv_PTZ0t_R3rpsFfXILaG4ilEVBafDSfcIA9ayZz_8xSwEB7J4135i2cwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d50508a6c.mp4?token=dswS1tVGta5DiLNl5QyxOCAHU46JH79IqXOnju0Xl3_iRto0f9tt6QFiZ6geQ7lGO3Yo_rtJ_G-TnotuzOYNYv4nV6YA8uHtYQH2rZWDRgYn7EX0vyfRjzwebsiUEd1wmDNuQ7A1coR0x495__81sPGNrC8lIfOw-Aqw9dJjGwdDPyNAZfcGD04yeTf09sHm8FlW-J66kzHVc3nNxrd4HQXLPM2UQ9Txe9MxScDP5RbSkt_yKz5QvAwkvW8bUiD1WGWHablsb5WtT6tuwvzTDVOxbzhAEv_PTZ0t_R3rpsFfXILaG4ilEVBafDSfcIA9ayZz_8xSwEB7J4135i2cwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نبویان، عضو کمیسیون امنیت ملی مجلس که متن نهایی رو دیده :
با امضای این توافق، رسما مستعمره آمریکا می‌شیم!
هر بار که ترامپ بند جدید اضافه کرد، آقایان عقب‌نشینی کردن و گفتن چشم.
تنگه‌ی هرمز بلافاصله و بدون محدودیت و عوارض، باز میشه؛ حتی واسه اسرائیل.
مواد هسته‌ای باید رقیق بشه.
کوچک‌ترین غنی سازی بخوایم انجام بدیم، قبلش باید از آمریکا اجازه بگیریم! حتی واسه ساختن دارو و برق و...
آزادسازی پول‌های مسدود شده؟ معلوم نیست.
منفعت ایران از صندوق 300 میلیارد دلاری؟ معلوم نیست.
رفع تحریم ها ؟ معلوم نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/127752" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127751">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
گویا تندروها فردا هم فراخوان دادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/127751" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127750">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به وای نت:
🔴
این یک توافق بد است. هیچ‌کس از آن راضی نیست. آنها می‌فهمند که این برای ما خوب نیست و به منافع اسرائیل آسیب می‌زند.
🔴
چیزی که نگران‌کننده است این است که اسرائیل نمی‌تواند تأثیر بگذارد و صدایش شنیده نمی‌شود.
🔴
این عمدتاً یک «توافق جام جهانی-جشن‌های ۲۵۰ سالگی تولد ۸۰ سالگی ترامپ» است.
🔴
هدف این است که برای همه رویدادهای بزرگ فعلی در آمریکا کمی آرامش بخرد. واقعاً چیزی نیست که دوام بیاورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/127750" target="_blank">📅 00:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127749">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
انتخاب: تو مشهد کلا ۱۰۰نفر تندرو تجمع کردن اما هیاهو راه انداختن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/127749" target="_blank">📅 00:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzEsmktzPhrhW9COwK8T2W_aaKLUgeBOvjzLyy9ZrpXTZM_xS0rF0BSxB2nVSBGxjiBUIs5S9Fm3AkQ9HQAzVgR1Vgp34Rjv__N1W-iFA_Pt8oJfNtnt6Dp48fRCQxtDftby1Vj2MOYCkaEfPO9OF_Ttbij7K-TUT8RgO_nk_2DyYnClVsYvWlwzIYTjNVFC9oQerfN0IaPvV6LliCVTxSOwQGOJUvGq56pWgtXO7T0JARP1qWe8ZF1BzXiu4DCGNOsh_9A5vDZyWfW1iq4h_cVWLdMnJXnvEF44RkWW-4JzVygPL7BuAw31pgPqlxHXeR0MgyibEZ_vbrC6gtVh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس گرای ادامه شلوغی‌ها داد
🔴
۸۰ درصد شرکت‌کنندگان توافق را به ضرر کشور می‌دانند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/127748" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127746">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVujUNxuCJBLsaO5F0ymjgY5_lBg-RTh8iwN42yY4g6O3_M6BxiI_7JfmZAghR33v_Gh5fNyUmFVP9ekDx16gtknMx1VsQEWkhIwua5IYNOUN88uOFM24OaLfNQjcC0JEqiXn0ewfqLYt4YmM1hK2SNLpf4VLluMoljlZk3uExdlxeXfS0jv2YzJPxKMEQ2E0nV-KnKnIRDc8kVg6j0Fc-o6XvGCY_BGsLgzLgq-ug3jLYiJ0JgIN76wXIlNurM1KSTBaExZbyj4Rux7uNRID8Fc9zzBrtcS2UmdFngNAscdk0iYkvQ1HuHRNWmnxk5RMrlsaSG9IplsjZK-kkQBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiF0NT9QiaNEhiqyGVcuhUt6WbTfWqEROMdvvleCadlWmo-y5-yV0QbMJtMOv7ZC-MBjpAiCW7LHlKY9U5HZJhhdyLWELkdmn7tx0evZyyt3Vcfu1VIFr0sx5cJZhC6EpLtJ7UPuqjxkA55cBGOSzWLOtKMGiOiEjSPVFbqd-3yfRtYKqA--mIRnv-qQoN_YU3mhAqyXwj8o_02hexaHLayXB82PQ2Msnz4RJsw8fJ0cFrDm8RsuwHNlSddZNFVveU-fUlL8xLXAajIwqSM_CkmQnn92lEOYQ6-0drkrNByODLyB8QKt3PXbuJrrZrfngVSy7K8lYIVcu8hBL_NtkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
درگیری به روزنامه‌ها کشیده شد
🔴
دیس و دیسبک دو روزنامه نوبنیاد و سازندگی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/127746" target="_blank">📅 00:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127745">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f489787669.mp4?token=Ag2SeiIjOZhDpqHXt6rdzCENrJgjuHQid_DBQRKcKGdNkYGBpRWCXbAH4nKI-_ZZ-xOfzOSaNseP7lSbnVCrTopedRpRhM9M1hABQyDHuFGPbdzWU2gMTYL6sUTdD37aIQ_0t2zw_Le2CqEvNGLMZ6aluhx-H1Y21wOjafbHYrFZE9ddQY2uL_vrXZrG6nimnC8VilKTNkk53j0mzfpIzCokXJmnRQhnqXFy1UYFKkfI1s0gT6dU_E71zmELPu5hhqXiK_Ojolrdjqkb2hR6YK8AeLUBQBWBS8ta1fZa7rXXY2TvZRyAZhHCP1e-35VaCk3ETdANH_BPl0B3Dhddhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f489787669.mp4?token=Ag2SeiIjOZhDpqHXt6rdzCENrJgjuHQid_DBQRKcKGdNkYGBpRWCXbAH4nKI-_ZZ-xOfzOSaNseP7lSbnVCrTopedRpRhM9M1hABQyDHuFGPbdzWU2gMTYL6sUTdD37aIQ_0t2zw_Le2CqEvNGLMZ6aluhx-H1Y21wOjafbHYrFZE9ddQY2uL_vrXZrG6nimnC8VilKTNkk53j0mzfpIzCokXJmnRQhnqXFy1UYFKkfI1s0gT6dU_E71zmELPu5hhqXiK_Ojolrdjqkb2hR6YK8AeLUBQBWBS8ta1fZa7rXXY2TvZRyAZhHCP1e-35VaCk3ETdANH_BPl0B3Dhddhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار مرگ بر قالیشاه در تجمع پایداری‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/127745" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127744">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEJofdPjyWLf7f1q3ovBukaASmkSdTKw35wHseI23UiSIAP36LfpV7AlO2EYqyETZBRzxStrhCYTfihj5RFbHnuQCLFf0ov4EJW3IMJw-FdtIwzhclrhD2aOQ9oGnFEoBWRw59TwaCyDQKCwgD4j66q4aYIFf444EmFW_ZCL0Z7niWDVAUFtoNzmT7MJBGeomDDJfm2KzQbk6MZbbJG6GYrp4TG6ObuLvaT5B92y-e8kqpvCkFzwpsBiVrvvbdUpPowzqYmvt2_4KR7IYWJXQ3R6TxpGRRQr6LWyA5i3IYD74DVZ52jJnRHDnFWNfE7QpBgPCg1xh0Qrw94QQ-mEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیافه یه پایدارچی رندوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/127744" target="_blank">📅 00:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127743">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🤴
رضاشاه روحت شاد
🔴
فقط تو میدونستی این جماعت چه احمقین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/127743" target="_blank">📅 00:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127742">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrxvYrsEyyCIxtXPYw-hLlBMZ6AOaD3A6Cp7DCRsZlmvNz0aVGT6tXXFWMwriW4e39LW9kcnhvldLKZjYplQI4yv4FoAOSE00ObbCvxyTFqtXY3leteF3kcen2zlF9ciMfOeG_1p-VB2GgkkJ8XzXQ1aFWKY2zLrx85piDhC0iNZ_IvOghXgVcXzMOS61cPnQAGzWRst_mjeewZewqTKrZUaah7orq-pYhHdyDlgwm49wadeejiPknYpC3X6_Vh7Zaf-jhlS-21yuPWVJy86b2bhqJmp7UxJSxzvRdtZTCUXbwVDQwtXm0sN8UtJ_-YIMFhGLcqPQjOX42HEpaF7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت کامنتا
😂
🔴
من خودم بسیجیم ولی الان بحث بحث انتقام رهبر شهیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/127742" target="_blank">📅 00:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127741">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJe1D66iYL9QYCTVhovtuRG2kh2WCJd4DE5BCL9RskZ4Q9f1VK3E1Y0svmGFckvY1i_ORsi44m99zX8mzcocIqJhPIl38xFQE_a7TM9VrYxkJOhWkJsUWE2HLn_KbXJGih_h4LoQmBRAPt9chWU9LaoOTTce5FwDOO6YthBJnrelf3EM6u2Q46llbVhzXPn_udBF6OiMneBs9E-uHH7i6ciLOb8WaraqdEEcFSEfx4RcrX-ITPVFnEh_sOgGan2Ealxf4NqYpV_kPo7hkPiQZQhvBD7ZgmU_P8Rq3jFn3HithlEkz-DW3ZwZBwqjMYQQisGULx95rHf7RtzJXtwGwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: آمریکا پیروز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/127741" target="_blank">📅 00:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127740">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نکات ایمنی برای تندروها:
۱ـ چفیه نذارین، ماسک بزنین به صورتتون.
۲ـ عطر مشهد و گلاب نزنین تا شناسایی نشین.
۳ـ اپلیکیشن بله، ایتا و روبیکا رو برای ساعاتی حذف کنین.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/127740" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127739">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خطاب به تندروها:
🔴
هر کی ناراحته از ایران میتونه جمع کنه بره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/127739" target="_blank">📅 00:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127738">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6743285f93.mp4?token=LtEBfEvNec1kqkaelHYbqgDDcJnj-HVx9HhUPEHmdjFij5s5tHeDpO4mPeeZEmR8-3zLR6_gLIiVmzaREXkQM_QhvD4nAiVH5OEfTnZHRgkuO9_2lkvC9B8MsBP2XPQ3d9tVhWNKpkGbjWH9amqv3wNBF_0SpU8TGR4L9hG21F__ykbeM91Q7gBDU63kjm-Tne7t4VsA_BY051gAvGVBSr98EXh65sIhD3r1EL34pDbVl7Hvc5E9NdS1DpQaSwexY1kHsAq31AL9CD5g30k2YNH2_TgTLV2-6qLCeC6rWomV0I0VNo-v5pgjt3q2WKjFCqon5pzW7oO_cPXWzePo2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6743285f93.mp4?token=LtEBfEvNec1kqkaelHYbqgDDcJnj-HVx9HhUPEHmdjFij5s5tHeDpO4mPeeZEmR8-3zLR6_gLIiVmzaREXkQM_QhvD4nAiVH5OEfTnZHRgkuO9_2lkvC9B8MsBP2XPQ3d9tVhWNKpkGbjWH9amqv3wNBF_0SpU8TGR4L9hG21F__ykbeM91Q7gBDU63kjm-Tne7t4VsA_BY051gAvGVBSr98EXh65sIhD3r1EL34pDbVl7Hvc5E9NdS1DpQaSwexY1kHsAq31AL9CD5g30k2YNH2_TgTLV2-6qLCeC6rWomV0I0VNo-v5pgjt3q2WKjFCqon5pzW7oO_cPXWzePo2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از مخالفان توافق:
بر پدر و مادرتون لعنت غرب گراهای بدبخت. عراقچی خاک بر سرت. مردم دارن سکته میکنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/127738" target="_blank">📅 00:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127737">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLN1rG3Ip4mkWP3iKflowQ-qmGnxx717qGguP__FlHzNEjNonQjjDDtjo_RX3EBmoyl8pMqof6RR9msiAmTSwqYkyK5MMkZhFp73va4yEr1aZ_sA94nUuHXuZ6AVW_SzIJb1Af0XOlUd1Xmh09hGCc8-krQa0DF2qc-LIiMARm8MS1tOIvFDcg-sMFfe0It3uYuKEr1xYi6i_8hKjWBXRJsiW-i8eT-xMQsQFbEI3bbejYg8mqN-OYFwaZ7TgzHx8p3L_GY6rrOiUJsD_UOxFbdU957rudaeg4qqycR7rMZrkBzv4x3XQgyyd2HF5gcuZ-KcLeJ57VvEQqfzDuZ4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ملت درحال تماشای درگیری تندروها و امنیتی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/127737" target="_blank">📅 00:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127736">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">فرزند جمهوری اسلامی و جان فدای انقلاب
عبدالله محمدی ۸۰ ساله ۸۰ ساله ۸۰ ساله ۲۴ خرداد قم عزیز
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/127736" target="_blank">📅 23:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127735">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
شعار مرگ بر قالیشاه در میدان انقلاب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/127735" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127734">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zx4D8a9crJUbIMvbcleUg9jNQzirZAAnczDX9pQOn45KYt7rG0C_wdEjOAjoCAnYgZavn4DzCaegKV43sMFJEVF_BsKqxOCa53E-Mn57kORW-6NIPi82Fh7fD5JsSk5Fu32BPgs8AU3GcuNzhPjfI4se8gD4PUHiKcOp5fiWpX0pvgYjtZXAx6kb53EPbFiLM8xrMZoM__mr0wrwbh5pM_oGFHyY53UHSJm2fHEwduVQVLOpC49DkaTGYyytA3iKTszXhOnxVJexLJzaaNxqgIwCTqzsMGIavxEiDbHSseu-to1QgeZyWAbDj2T0VZyi5d8B7hP9fCPZCAryFJG8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر عجیب دیده شده در شلوغی‌های امشب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/127734" target="_blank">📅 23:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127733">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
گزارش‌ها از درگیری اغتشاشگران در قم با نیروهای جان برکف امنیتی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/127733" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127732">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کم مونده تندروها شعار:
لاحکم الا لله خوارج رو بدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/127732" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127731">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
طبق گزارشات تعداد زیادی از مردم در گردان‌های امام علی ثبت نام کردند تا با اغتشاشات امشب مقابله کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/127731" target="_blank">📅 23:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127730">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPtsKPv1x7DL804zlPXQN5piaJ69U3n0Tk7Vhd4874cZgMk_VpAPYwU3m1OvD0pkseIgHzEX236185a2oe0X961uO95tvz6lEJoTQAcM8FqZDSoHygXUHOjaGOW6-Ro_dK0Oera5BkSCq3JEu48ka_9Af4gfM1hSvxgw1xzkwDR10PNWOjGgCUxSla8nA-0wcgFyFpydbyc_cWxX1zuIosckpFYCTr3nnKSM-vwZuYCz2A6TlTbQcMDowrOhH7-z18HY5wokgbiGx8OX7qeYlbGdNnpaMsCu2STuO3EdxOZJK4vlD1eP91oNFVCVHEIrQ8jpglNiuBQuzkssYz1vkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: تصویری از دو لیدر شلوغی‌های امشب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/127730" target="_blank">📅 23:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127729">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تندروها
❌
بولشویک‌ها
✔️</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/127729" target="_blank">📅 23:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127728">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
گزارش‌ها از اغتشاش تندروها در قم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/127728" target="_blank">📅 23:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127727">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
گزارش‌ها از اغتشاش تندروها در قم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/127727" target="_blank">📅 23:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127726">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
حجت‌الاسلام نبویان: با این توافق جمهوری اسلامی مستعمره امریکای کبیر خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/127726" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127725">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
شعار تندروها در میدان انقلاب: نه اینوری نه اونوری جانم فدای رهبری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/127725" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127724">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شعار تندروها در میدان ابن سینا تهران: قالیشاه حیا کن ریاستو رها کن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/127724" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127723">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سازمان ملل درمورد سرکوب اغتشاشات امشب تندروها ابراز نگرانی کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/127723" target="_blank">📅 23:39 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
