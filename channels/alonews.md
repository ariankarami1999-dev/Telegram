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
<img src="https://cdn4.telesco.pe/file/Q5Nx13nVKqasMosJi2mG6wDrE9levHdQiWiZ8Bf7Q_UVUMyQ_fTzwUBWIvmnnUdu8GMAxH_9PdxSi5p7Bid3EwcqpUxf-qy6Vf466aPKv5ikdFLrPf4Vt5zzR_lIS9U7d0Mj_0QZY5iUMj_hp7vfw7yXuZLW7_or8D_6_N04sZgfBeCO3H-ni_C5en4G38aQPpG6C7P6r2X0XWswWLOdbXjp5AqN6AGTzNevyxDEsslF1VpR9-cCArnrvDDG-EiqkWUadLRrh-n7KD65DzJbqajgC-uQj2MMiJWT4PxK07ekUByF1UQdLLRYASfMNR3K-pOgbGmF6Nf9h0PIQqxVXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-150604">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnttKbbEf-msLIidQbO7DdtAVA1gTGxxFXbn81PC4tUsdpbYV5K6cFyPDKAtJoRq_eSq3249aR9-axFSM_WMHrx_WxrVI9HiKd9lmemzMGjivfNPgo5FaHNYYcY7IMCohOxaNRM48uXYuHP3JwU3OFFrtgzymtcTfGjF_90ikgljJ86dHb9EzN7SsBfRq1L-zrDlrWYYs5NkQs9W6MNxJZIfDMtNEAe6nYCDKQNw6yauXCfT2Uzjj4U2Z7L20uAirBRWtivU6f_YLn-Le1okZe6QEc9f4FZ0d_9gjR5o7etlBSdq_F3l-_sQ7YlGr6y2CalfpAAKE-qiGJVaYfrUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امضاهای کارزار درخواست ابطال اعتبارنامه رسایی از ۷ هزار گذشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/alonews/150604" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150603">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خانعلی زاده: عراقچی آن‌قدر در نیویورک ماند تا نهایتا با دستور مارکو روبیو، او را اخراج کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/alonews/150603" target="_blank">📅 18:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150602">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
مدیرعامل فلای دبی: به درخواست مقامات، پروازهای خود به تل آویو را موقتاً تا اطلاع ثانوی به حالت تعلیق درآورده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/150602" target="_blank">📅 18:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150601">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مکرون: گروه 7 قصد دارد ظرف چهار ماه تا 100 میلیون بشکه گازوئیل و نفت خام آزاد کند.
🔴
گروه 7: در 20 روز اول، عرضه گازوئیل از سوی این گروه و شرکایش به میزان زیاد و زودهنگام افزایش خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/150601" target="_blank">📅 18:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150600">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
آکسیوس: دیپلماسی ایران و آمریکا همچنان در بن‌بست است
🔴
به گزارش آکسیوس، مذاکرات ایران و آمریکا همچنان با بن‌بست روبه‌روست. بر اساس این گزارش، ترامپ به‌دنبال دستیابی سریع به یک توافق گسترده است، در حالی که ایران مذاکرات آهسته‌تر، غیرمستقیم و توافق‌های محدودتر را ترجیح می‌دهد.
🔴
آکسیوس می‌گوید بی‌اعتمادی میان دو طرف پس از اتهام‌های متقابل درباره نقض تفاهمات قبلی افزایش یافته و فشارهای داخلی نیز مواضع دو طرف را سخت‌تر کرده است
🔴
طبق این گزارش، ترامپ نیز نسبت به امکان دستیابی به توافقی پایدار با ایران تردید بیشتری پیدا کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/150600" target="_blank">📅 18:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150599">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njkn7ZDsqMITkX1kUX-Q0yY0ND3v1parsV7sAfnD0Yx-MRHyuols1S2Xu8ytU_wupE3Ozp1MSiy9Tl_DgATn5_JMGcTOhktYodzL4QR3rGg2M7GkfOxA502Br0gTL-GRrpIia4acYSYmRrT-ezMxiauD4MXGKDlPgVrX1WZzkrOmakj3BqFRjdrPx702a7y0CLbqDBi2z4c6yx3ovL1u_xj7qEdW-dxCvNPV0MvltwjSKBPox25PrUNRc-2LtNDYGgAUdShWTTUNyCCRSTlJQVv_LrDrLggFFi3zbpltGQMRE5c_94Ehm6PCn2cxMfsfeWqoO5w6DCVyci19-_0SyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از تسلط بر منطقه بنی محمد، حوثی ها به سمت الزعازع در شهرستان الشمایتین در استان تعز پیشروی می‌کنند و بیش از پیش به التربه، آخرین مسیر تدارکاتی بین تعز و عدن، نزدیک می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/150599" target="_blank">📅 18:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150598">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHnbcrurtZ7eXB0RfDftuzRZXwkfmIMMzqLsQHkYDqDCZaQ2Mc-qFKD-0zqSODYWIHxJj3SNEy3ZZ9J0OfuvmHu7Zg8k6U27sv_j8F9NmdvYNMZjjeO89l38Hhli3Pn0lEsyBhhqkbpj-KKtdAWgTiI2bgRwcBKv8PIIj76HQctRib8gEbdtfKYPEmyX-cQZHU-KyN8WsE0DVMcVHC3IUJ8z9NzV2EDEJBOH8TljaWkwU-viaeS7xhb8hb51IKq_2E6ZbP3uVABy5dJYmyl1cZgSuYsjR1IqXGQPkDoYsODGpw2Sm7zcPehdByuJKRxW9MOe7kpwexo4RbC6t8NEXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت ۹۸ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/150598" target="_blank">📅 18:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150597">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=SfZJ8KBMsfx9rRD8C9c9tHX881-GZ1mefqDFl8P2PhOSekFABsDTt-wZzE5AP-uSJVsOX_pcnBZWhTAVh5alx-vhaJRp8hDApBTs8gLf8YHe6oTJDeuZI_GOwAZSqvPc5txiqThivSnZTYrg7VPmPkyyZyWg3O_bycWoZqPrvIvgUrxGUoeVxK5ok5NHmQVW-gBnGOAeIZNoNSJjSCzMgrVEs4VKarc6PI3FNm6JpWV8cLpk4e68Q0J6VZ3u4NcqwjvuDKXz-kp537A1hQICeMWztUYh2y3iCOLd_BUKs-FdaBadFULVxpzIASzM4twWxwM9M4hFPkX59jmLyUEhng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=SfZJ8KBMsfx9rRD8C9c9tHX881-GZ1mefqDFl8P2PhOSekFABsDTt-wZzE5AP-uSJVsOX_pcnBZWhTAVh5alx-vhaJRp8hDApBTs8gLf8YHe6oTJDeuZI_GOwAZSqvPc5txiqThivSnZTYrg7VPmPkyyZyWg3O_bycWoZqPrvIvgUrxGUoeVxK5ok5NHmQVW-gBnGOAeIZNoNSJjSCzMgrVEs4VKarc6PI3FNm6JpWV8cLpk4e68Q0J6VZ3u4NcqwjvuDKXz-kp537A1hQICeMWztUYh2y3iCOLd_BUKs-FdaBadFULVxpzIASzM4twWxwM9M4hFPkX59jmLyUEhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه اخوند تو تجمعات شبانه: در پیروزی ما توی جنگ و ابرقدرتی ایران تو کل عالم شکی نیست؛ الان دعوا فقط سر میزان ابرقدرتی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/150597" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150596">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری / ترامپ: «اروپا همین حالا موافقت کرده است که مقدار عظیمی از ذخایر انباشته گازوئیل خود را آزاد کند.
🔴
این فرایند فوراً آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/150596" target="_blank">📅 17:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150595">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سپاه : آماده‌ایم به هرگونه تهدید یا حمله، فوری و شدیدتر از عملیات وعده صادق ۲ پاسخ بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/150595" target="_blank">📅 17:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150594">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
بانک مرکزی: بازار ارز رو مستمر رصد میکنیم و در صورت ضرورت اقدام خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150594" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150593">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
انفجار جدید در تنگهٔ هرمز
🔴
شرکت اطلاعاتی امبری اعلام کرد یک نفتکش با پرچم پاناما هنگام عبور از تنگهٔ هرمز «هدف اصابت یک پرتابه قرار گرفته و ستون‌هایی از دود درحال خروج از آن است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/150593" target="_blank">📅 17:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150592">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
قیمت تتر در صرافی های رمزارز ایرانی به بیش از ۲۶۱۰۰۰ تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/150592" target="_blank">📅 17:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150591">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کارشناس صداوسیما: تهران رو دوباره با سنگرشکن می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/150591" target="_blank">📅 16:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150589">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
حمله با سلاح سرد به یک روحانی در رشت؛ ضارب متواری است
🔴
سرهنگ عیسی روشن‌قلب، فرمانده انتظامی رشت اعلام کرد یک روحانی در یکی از محلات این شهر توسط فردی ناشناس با سلاح سرد مجروح شده است.
🔴
به گفته وی، پلیس در جریان تحقیقات به سرنخ‌های مهمی درباره متهم رسیده و تیم‌های تخصصی با هماهنگی مرجع قضایی در تلاش برای دستگیری ضارب متواری هستند.
🔴
مرکز درمانی وضعیت فرد مجروح را مساعد اعلام کرده است. پلیس گفته علت و انگیزه این حمله پس از دستگیری متهم و تکمیل تحقیقات اعلام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/150589" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150588">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: بیش از ۶ کشور خواهان پیوستن به توافق مکه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150588" target="_blank">📅 16:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150587">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نخست‌وزیر قطر، شیخ محمد بن عبدالرحمن آل ثانی، امروز با وزیر امور خارجه ایران، عباس عراقچی، تلفنی گفتگو کرد و به وی تسلیت گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/150587" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150586">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c27ba562.mp4?token=J0s0nSW-HRdVaDVZeEZ4MgA5zdsSejOuY0AoCBauZoX8MqUSfDrpvWz77Z83tgz4HORV8c9sjPdim07D2ziqGLqhTh8QX7XQ2s2KDtHp9Gtz7i0o9gUQENes0xFlOdwTZdAQkM82EpY2wxoYnq8Z1k5VeBRgkLCQO_2HdrFjksFqW8NXoCYldLL6z00P013j8R57vmaOeQR4CP1szmKLn-K5YFfOWsfkEcNoGpIfEmpKLKpLSnCn5y5sHDgc5Xjacw_NS97ruxdrWfD_aCv0oR5A6n1q_awnsLJPxnI5u92_4YGxN6CctK9XjpVzkvGKkWzM3XqcKhAS6aFZddRBIrQWq7y0y96hW-NBTvM_VlSg-n_gNts2EAP6J3O2ezdmFixwko1An9-PYaCMEwBfd617ccPEo7l5u_vpCPoaQxyfaVZ6Fk5mJRDv_TVzqF3_-kJ-g7HeAT-apetpC6fDOigVY-tljsgqpkNYs2roGSRNcWcyfuSwRdBTvl1KDbEfjU6maeNzxZKPvwK0k8z5tx7eupKQ4Cn1U92tfVun5YJ0FrSWzws2nScNGXu5fszi0nIUcHYmKuhEbjnP9GVavEQB9h2Z00CH_JCY3k9UNbeONIYKdwCBqRZrBfnjGBj2QoI1ZkLRcFW2lIe4n1nzY13ewwRK_GuisafbD21rFoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c27ba562.mp4?token=J0s0nSW-HRdVaDVZeEZ4MgA5zdsSejOuY0AoCBauZoX8MqUSfDrpvWz77Z83tgz4HORV8c9sjPdim07D2ziqGLqhTh8QX7XQ2s2KDtHp9Gtz7i0o9gUQENes0xFlOdwTZdAQkM82EpY2wxoYnq8Z1k5VeBRgkLCQO_2HdrFjksFqW8NXoCYldLL6z00P013j8R57vmaOeQR4CP1szmKLn-K5YFfOWsfkEcNoGpIfEmpKLKpLSnCn5y5sHDgc5Xjacw_NS97ruxdrWfD_aCv0oR5A6n1q_awnsLJPxnI5u92_4YGxN6CctK9XjpVzkvGKkWzM3XqcKhAS6aFZddRBIrQWq7y0y96hW-NBTvM_VlSg-n_gNts2EAP6J3O2ezdmFixwko1An9-PYaCMEwBfd617ccPEo7l5u_vpCPoaQxyfaVZ6Fk5mJRDv_TVzqF3_-kJ-g7HeAT-apetpC6fDOigVY-tljsgqpkNYs2roGSRNcWcyfuSwRdBTvl1KDbEfjU6maeNzxZKPvwK0k8z5tx7eupKQ4Cn1U92tfVun5YJ0FrSWzws2nScNGXu5fszi0nIUcHYmKuhEbjnP9GVavEQB9h2Z00CH_JCY3k9UNbeONIYKdwCBqRZrBfnjGBj2QoI1ZkLRcFW2lIe4n1nzY13ewwRK_GuisafbD21rFoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، در مورد حادثه مربوط به شرکت هواپیمایی فلای‌دبی: با گذشت زمان، ابعاد این ماجرا روشن‌تر می‌شود.
🔴
این فرد تحت تاثیر اندیشه‌های رادیکال اسلامی قرار گرفته بود. او قصد داشت با هواپیما و مسافران آن، حادثه‌ای را رقم بزند.
🔴
ما در حال بررسی هستیم که آیا او توسط کسی فرستاده شده است، و هر کسی که او را فرستاده باشد، باید بهای بسیار سنگینی بپردازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150586" target="_blank">📅 16:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150585">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQaOiQCQycQzOJsrE9im5dpJ4FCoG2ll_a5F2dg4R8vnOOHjhw1ZE4rjrNnLfZk5OieFnjVg7mryiK9--q9ZBuvOwTaCB_c7ku7FAsmU9zZygJJh2DmnMtWXCmKndNVMAhr6EAg57SXDIKT5EV0NkvbzGmlXU4rUx-u_xYBEOknrPPdIcR_lQv8-bHN8nmiulRT3hVxjLrFjpxHM5W_kdSEwBJvwyNRLCeBgRQKy9G8g3hb-6zp8Tb9xBapQfhvAkqXzi7yj7AggKTASCDGAXv8mA2ZgGCL9PQI-lFmbnmWdA8vDxx2v0QDvH0-2YubNaRcAjck6YzUiVWEiIY8hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: توافق با کره جنوبی همچنان رو به بهبود است
🔴
ترامپ اعلام کرد: «بسیار خرسندم که اعلام کنم توافق با جمهوری کره همچنان رو به بهبود است!»
🔴
او افزود: «۸.۴ میلیارد دلار برای پروژه‌ای جهت افزایش برداشت نفت» اختصاص خواهد یافت.
🔴
ترامپ تاکید کرد: «تولید بیشتر نفت و گاز به معنای سلطه انرژی آمریکا و تضمین امنیت انرژی جهان در آینده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150585" target="_blank">📅 16:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150584">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b27a0f37.mp4?token=DcaKEQW9ythfN5ibPQWJvG84-485QIv8Y1e9CGmG8heXxtZ9_BnYsJrVeM_RSMaEvyWdCtoIvbR-iTcCKvDcZtMnrJW6vpVp9PvGxmbE5DdNW5TUmdocGKrYkJ5dWT7yQB4YbIMgLqVYwTmAJXLhBmcpXo8niPjQNdq-dSisFqoYlZLHv1gCNGoEhK9fgjDO1GtXrm8YzM-O0Mog8JrB4Cs4OSoXdKliQF28kkCgjslj29hNOaVwCdTEZ5CvaLvFqoHjDtnafBq2-qH6z5DsGX_QUUO1IaGx3PCducz5afZ20l_dc6pm2dCNy7V_MuICYCkjZgL2lddTTrDdnQgwWSsAMJyoYuM52ke41GPnCysJtAwWVsjCou18tBeGuHkHKrO_evpNzH57tdmw0fFfdaYB4ruXPIC-bizHLBXxgobDDqBLiDzO2BEfWb46M3HiU6cVkMpWReUA5xgbxb160S_m9JJze5EOKwAytROSa34sG7L4RAOVoX7LDBorpDE5ENrsg1F6ZkKQcQlffFsXM750waoPS5QX6pYDaEZHESrxiI73JUSrzI1dQA5x3Hb9E5uH5kgfy9Yx6B750R9rBxGgAAPNlvfWEHsuXtbCSZmtY-uO6QPTXldASw2v-kI-Encff8P2rEQ_QN6dp7QlP5MTTt-mqppJicT1l7UOVEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b27a0f37.mp4?token=DcaKEQW9ythfN5ibPQWJvG84-485QIv8Y1e9CGmG8heXxtZ9_BnYsJrVeM_RSMaEvyWdCtoIvbR-iTcCKvDcZtMnrJW6vpVp9PvGxmbE5DdNW5TUmdocGKrYkJ5dWT7yQB4YbIMgLqVYwTmAJXLhBmcpXo8niPjQNdq-dSisFqoYlZLHv1gCNGoEhK9fgjDO1GtXrm8YzM-O0Mog8JrB4Cs4OSoXdKliQF28kkCgjslj29hNOaVwCdTEZ5CvaLvFqoHjDtnafBq2-qH6z5DsGX_QUUO1IaGx3PCducz5afZ20l_dc6pm2dCNy7V_MuICYCkjZgL2lddTTrDdnQgwWSsAMJyoYuM52ke41GPnCysJtAwWVsjCou18tBeGuHkHKrO_evpNzH57tdmw0fFfdaYB4ruXPIC-bizHLBXxgobDDqBLiDzO2BEfWb46M3HiU6cVkMpWReUA5xgbxb160S_m9JJze5EOKwAytROSa34sG7L4RAOVoX7LDBorpDE5ENrsg1F6ZkKQcQlffFsXM750waoPS5QX6pYDaEZHESrxiI73JUSrzI1dQA5x3Hb9E5uH5kgfy9Yx6B750R9rBxGgAAPNlvfWEHsuXtbCSZmtY-uO6QPTXldASw2v-kI-Encff8P2rEQ_QN6dp7QlP5MTTt-mqppJicT1l7UOVEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«می‌دانید چه چیزی شگفت‌انگیز است؟ اول از همه، برخلاف تمام پیش‌بینی‌ها، ما سه سال است که در هفت جبهه در حال جنگ هستیم.
🔴
برخلاف تمام پیش‌بینی‌ها، اقتصاد ما با قدرت در حال رشد است و در میان سه اقتصاد پویاتر جهان قرار گرفته است.
🔴
و برخلاف تمام پیش‌بینی‌ها — و این مهم‌ترین نکته است — ما در حال پیروز شدن هستیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150584" target="_blank">📅 16:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150583">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: نباید هیچ‌گونه هزینه‌ای برای عبور از تنگه هرمز دریافت شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150583" target="_blank">📅 16:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150582">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
امام جمعه اصفهان: مردم آماده فدا کردن جان خود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/150582" target="_blank">📅 15:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150581">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: کمیته دفاع سیاسی استراتژیک، طبق توافق مکه، به زودی در رياض جلسه برگزار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150581" target="_blank">📅 15:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150580">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Thaqleg6gxah6VFR8RSodcGIj24DFaqUAJ0g9QHR-ubdUvblCXpSpcYuDJVvm0KuYZKI_UR7uwapA5qlSD2n8_UDkW1Ez0FwlqGgPhQ9raofwPb8R6TAqJpM0UBitmqq4kIqc29lGmxcHORL_REWJyqCzbDznF3DM9Vl3wCsASOQl5zP23ONWIp96W1YU9KIXg878fyJPWudprAHuqpJgz3G4C6tby4pVwMNLpdmKd6I9qWm6KdmNs9r3rlT89pp44H4cJkouJkpK4czeCBzPvuQz7wu8jHxF0z-EeLK2t5QWKJmDy1ePfuNwkYF0OrJEFIhnIHsRKLttUaxLrhlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقاشی روی دیوار سفارت امارات در تهران:
🔴
این صدا از آن‌چه فکر می‌کنید، نزدیک‌تر است!
🔴
شب‌بخیر امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/150580" target="_blank">📅 15:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150579">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDg83clZqiV3rxXtbkXDQXQU7uQgaVJV9rE7gO71Wo_OUWOlCGWjIDKetX_Gr2rFTkNom_FguFw8NpZJrPtiwb4GM0T5PySoIgPStQz1qBaqJDc0n-RDlOaHMyLV5fNbXnnBvLbalAyeggKqZ7hey9yUE9WCRGaNnsViRiQnlvIDFJKdeptdeXGzNfTdYfZXDeKUdmgYOPZBKEoibk7ruTdxwO2gJS5MriPgdun19Vy8OwDWeNcnJDYjxpsPBWKGeRu4dR9PBmVhYEvgjfp8sseuJXSj0JBMLCBkIwnQhAKNtPb53nkxNufzZoK_PSCocBTOHxiWkhn_7hW7COnvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای باری نظامی بریتانیایی نیز وارد عربستان سعودی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/150579" target="_blank">📅 15:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150578">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pE-g3hAzeHomF3qhhS0AQ2rEE9J7uUfSiNhZTaHXjvomHeLMf49wouPTobZg5U47aq1FQ7V6VN5rm7D7cs3dmMkTA1Dryey6wKeJ-sU6_BvU-wacV9LGDfXAhrU03gMODnUqiAAys1ftaUiyArLqP2iEGTx6yI4VtQJaV0bjW9VoIHa4XhOzJp_6TrIVLEtR3t3ZowwCMW3V-X1O0e290xXZQIRDLgl4MZyixBpRRsw5HmFK0UV8BxvI52pFECrIxeJxxgEQSWgQHte6HW2srUayJVZEf-iXwDekqX3Du7vCK8db54DahUdjHuUBPyMHky85OTS1lFM7XyafVtOMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داماد سرخونه حسن روحانی: وقتی شما پوشک می شدید، روحانی و قالیباف و پزشکیان در خط مقدم جبهه بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150578" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150577">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دلار 260هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150577" target="_blank">📅 15:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150576">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDR94LJtw4bHpRtDtNKmDQ5oMwYSKBJynr6FrKIa86fZrAWq13WcdfIMdgP7l6HgJY6K6hXj0wI-Pd6azEXPhPQ4gjK7oZzETD_yKmwXH6AWJk6sG-ntxJU26jVXqkcJtknVRfyjPCiufhCIvoyYHllfGh6mxQNlm4si7BkZYvBWoiE7LLGDsQpUfT_NjmNmWH1KJf5SpDIqOelnQ-UauvmN7hUIyC18nUGuDbD2Thy_fdE9mOfSmhhk92TC7_aAR4RYT-zn6FxooI80G3hOq-IxmthDqWf_ozGetYIPYUuP_kotU0f41BTALj1po0XOuPo5KBHYUiUSf0p4GYOQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: آمریکا تا ۲ماه دیگه بیچاره میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/150576" target="_blank">📅 15:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150575">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فایننشال تایمز: ترامپ در فکر حمله آخرالزمانی‌به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/150575" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150574">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25ae8f78b.mp4?token=udcFnfZpVfK41NDwJqsvmw8GHDplNRF6wEx8MHZFHT6JBGEohZBb-eP72mH8m4FJE7LRDESMwGLgJnLxru1CnmqyraSaQ7xafNcpv9szHB6fGtx2tEcO4sJ2PvreVRIxkTEaGbYES5FGZEWyWpRkIQmwD0qZoTQc0uds8qFNBo1nGwRYcc3zKvdGy_CbSv18KGj7ku3XOOJhWnQozjYTDPKQK13ewE3bRTAdzLvmdpmxczYGHwqQrsYG2957FTE-kAuDqr4NG7noBG6d7J9PvHyVt0UJoGNX0vOwQk4agoQ-ZGUlJNLFFOOee7PFcpUxvTp_GvIjYYHh1C2KglRM9CZR4Pad3RCxtTddx-q3-VXReZmSLtNO4BPwN_PKanpn_b0Cu8N200h2oO0gZh5yDGk9nOgrRnALyBH2Xdj3CddQ2M5h_Z243f3o2SGfp6p6k_5bacH5FuAWbyWEh7KyYsxtoEGxaQTOC4AKOmZFsUwoVMg8bN7OY37CrDm_7eyXrkl3rm1XdelKvZcF2F1AjppVKqhSXAG5SfaAIJEYhrmeiJBnPZcwRnAwhrMYeSiVtXPIvbsNrtFWvMPIOjhAkAeLVSYncesG6w4ot4EikvN8lckB5_abr27BC2lk7QEuOoUu8M75EUOEEhlm3JUqsFrtBWQfkj3lv_7d0TbP8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25ae8f78b.mp4?token=udcFnfZpVfK41NDwJqsvmw8GHDplNRF6wEx8MHZFHT6JBGEohZBb-eP72mH8m4FJE7LRDESMwGLgJnLxru1CnmqyraSaQ7xafNcpv9szHB6fGtx2tEcO4sJ2PvreVRIxkTEaGbYES5FGZEWyWpRkIQmwD0qZoTQc0uds8qFNBo1nGwRYcc3zKvdGy_CbSv18KGj7ku3XOOJhWnQozjYTDPKQK13ewE3bRTAdzLvmdpmxczYGHwqQrsYG2957FTE-kAuDqr4NG7noBG6d7J9PvHyVt0UJoGNX0vOwQk4agoQ-ZGUlJNLFFOOee7PFcpUxvTp_GvIjYYHh1C2KglRM9CZR4Pad3RCxtTddx-q3-VXReZmSLtNO4BPwN_PKanpn_b0Cu8N200h2oO0gZh5yDGk9nOgrRnALyBH2Xdj3CddQ2M5h_Z243f3o2SGfp6p6k_5bacH5FuAWbyWEh7KyYsxtoEGxaQTOC4AKOmZFsUwoVMg8bN7OY37CrDm_7eyXrkl3rm1XdelKvZcF2F1AjppVKqhSXAG5SfaAIJEYhrmeiJBnPZcwRnAwhrMYeSiVtXPIvbsNrtFWvMPIOjhAkAeLVSYncesG6w4ot4EikvN8lckB5_abr27BC2lk7QEuOoUu8M75EUOEEhlm3JUqsFrtBWQfkj3lv_7d0TbP8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع آمریکایی: تیپ ۷۵ رنجر ارتش آمریکا طی روزهای اخیر، تمرینات فشرده‌ای برای نفوذ و پاکسازی تونل‌ها انجام داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/150574" target="_blank">📅 14:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150573">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzypHmTPsOoou_J8EgarnZ696EkaOUreBRkJ6I3QcLCkztWQnL7uC5yC_zK08c-Oc_-2iRi0ObySi9GCpQNRUBLJI0XJsMP4DZC8lGLFCEWY3F2JQ1czFioKjzdvHDTikZnScHp45mPUOD0MQYlNVwTVeJrMT0M6AJgO0mL9kfatMc49Ru6RC_6bQq4_f3IZyixssGEQemfEospNBc7faBllqVZ8YHb_0tPC6HjJP0dHQqTuMWd_VGU4RHGx7T2P53bQ84DkC28iQnxmeI7mkwJ0Vs9u2GjnFjjWM5BnE_rRsJ76JZdKZ4aMFeqzo6zzLw6mT6w2squdDE2nei-4oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایتن لوینز، خبرنگار آمریکایی: حوثی‌ها ممکن است واقعاً عدن را تصرف کنند و دولت یمنِ مورد حمایت عربستان سعودی را به‌طور کامل شکست دهند!
🔴
اگر این اتفاق رخ دهد، ایران عربستان سعودی را محاصره خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/150573" target="_blank">📅 14:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150572">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awMYFDkfS4Zum0SUuZjC3ZZquV-cTuUxkI-vDlfV1O7J_QTAtTYXAiC7XW8Lc6ZAJ0uLFRGFdSU9kr89Xtki9qB5s0pHorK2HuhfQEBARu7nfJcxplK6nssJg-Fz5WLhmRnazb3UIG4Loh4JyfkomddDuwkCQRVvX231SKrJTICII3wc_m0DwD32ysG5HG_WoS9VYd7b8fSlXwGbWklQAHl-rgYfvv-KMJTK4Fdit-owD__pnScmhj7QFjDw5Yk37MNfCOKzXXIFc4VEJxM4fB12PDrAbPCsjIA7c2GBrLx_K1GXZJhAGowXrRz6ZqWcuQG2bpoueMkFx8SCs8VYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقتی میگیم کشور دست نظامی‌هاست یعنی این! گزارش رئیس سازمان برنامه و بودجه به سرلشکر صفوی
#کره_شمالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150572" target="_blank">📅 14:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150571">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
دیروز تو اصفهان زندانیای سابق با این لباسا و سلاح سرد اومدن تو خیابون و علیه رضا پهلوی شعارهای توهین آمیز دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/150571" target="_blank">📅 14:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150570">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIDzPdBHWG-eizd2RCbd7koBN9Kf_OduWjCxV2cSPcv8gozgcraeBrtnrw6wLE3vm1lvmhqumbNaQ2yImHQkNLu03Md7PK01297F8AfSTq296xjMOdVoWt_jqF0HHBdrrEMNulDGObBPosKhmgCl2BNDAkdYWParXoAAmsm5clIeslGhtyZ-C19uMTFcbhc3ZuWzbBVovfI33K-Tix8H5AiVwTFS1OCTgCc6_YYnVybnQhmA07OfCePoliAYo-OfmINQPGYzSbn8UxkWKpA-_aycJVd39MPmV9Na0-LAUItNBkuGnkszf0GB00tqhuy15rCMh3_r1VQk5SrUpqHkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقدی: انتقام حتماً گرفته میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/150570" target="_blank">📅 14:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150569">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوست داری از بازار نوسان بگیری؟ بیا
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading
کانال vip هم رایگانه
✔️</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150569" target="_blank">📅 14:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150568">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
دلیگانی، نماینده مجلس: باید امارات رو تصرف کنیم و باید نتانیاهو رو تو امارات ترور می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150568" target="_blank">📅 14:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150567">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ca4cea2f.mp4?token=fnY9xl72WtpKf4eHnsIVE8kksiUSSt6SpZv1v73FoqyrHbS8HvjFZEJtNScPo2bsoI8QBBgDS7fhUmnuVT7ZCzdqo5qX-rZzjJB4CXQD3SZTAB_1bMHqQKQM-WnXTf9qvAUYScWjpLhzdZ8EQMUV1jB0jDifuAsgdhwUlrO9dDlh4gQL9Fr8aObDhzXbn5i3FX7KSKnCkFIazLPp0qESKy6hyViqmpkoxOtDthu285bw2xpzw11VAwzuyy4ll74UzHvcD6JGMkJP8B7v25nVal16k5YYXYdqhCBt-1NU_7JLW2if36K1u4c9E_ShIMLCTCXBtXg6iFSbvOwMC8WXQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ca4cea2f.mp4?token=fnY9xl72WtpKf4eHnsIVE8kksiUSSt6SpZv1v73FoqyrHbS8HvjFZEJtNScPo2bsoI8QBBgDS7fhUmnuVT7ZCzdqo5qX-rZzjJB4CXQD3SZTAB_1bMHqQKQM-WnXTf9qvAUYScWjpLhzdZ8EQMUV1jB0jDifuAsgdhwUlrO9dDlh4gQL9Fr8aObDhzXbn5i3FX7KSKnCkFIazLPp0qESKy6hyViqmpkoxOtDthu285bw2xpzw11VAwzuyy4ll74UzHvcD6JGMkJP8B7v25nVal16k5YYXYdqhCBt-1NU_7JLW2if36K1u4c9E_ShIMLCTCXBtXg6iFSbvOwMC8WXQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگ زمینی تو راه ایران؟
🔴
ارتش آمریکا رسماً گفته نیروهای خنثی‌سازی هسته‌ای همراه رنجرهای هنگ 75، یه تمرین برای تصرف و پاک‌سازی یه تأسیسات هسته‌ای زیرزمینی انجام دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/150567" target="_blank">📅 14:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150566">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
هر گرم طلای ۱۸عیار 26میلیون تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150566" target="_blank">📅 14:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150565">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / ترامپ: شاید پیش از انتخابات میان‌دوره‌ای، وضعیت اضطراری اعلام کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150565" target="_blank">📅 13:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150564">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wrg5joykiJsSgkgRzZEFnzjlrRY2I_dpuYs95B0k-7MYNMURieFYRoo7eMkwMl8tlJ4MVzqcOidsQd5Ne_rVm7mZUEnppPPG4UqXpU_l6r5KCWgVqDR2byV0E9BCBSMVsqSyLJeXtr34Ts49_ePBcrcq-CQDHu2qeUSrOwZi9XXeGil_sgx1kO81a7PBKscdOKSh2m6KBFpnT_otxZx18A6Am-Jvfr_Kle4MCSoWNhB0TIyVEordaoyaiNA6W7Emo67m5cdZfHkWWDqk8h1HflLLEAsZB1D6OPfnHk0p4EWOeDgEKTMrE4FodETUaR8a18zp_qhb10kEMeqN2KcAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روسیه یک فروند هلی‌کوپتر Mi-8 خود را با اتش دوستانه بر فراز اوکراین سرنگون کرد.خلبانان این هلی‌کوپتر کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150564" target="_blank">📅 13:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150563">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dieLaWpyJHUbaIutbEJMsnBqSWtlzHoPKtBDuAHe_YMbm-LiTG-JI8rOOdXFJrMGk3lWxdc77HN0ebo1iwk5-JUMGMx73o07J-ST5trVkxAOZwhAWdO70wXijTWgflBQTj8ULxR-C1Uoj7tUXZDEfrHpXhcJlw20dOR9P9nmM9lMQFaSaGTa21_yrypLGxmdHokONcXWgpXYBQPDJ40t-Y0xe-5lw6VOpUxy2i_SNimQSh-AV4QLeYDABKmbi2qsDIgSg9RphI9W2iNDiSnXVOh8NMGh_cXOopvhi81s91o6N5qz1qEVG6MlxlwRgB_KmIVMmOVLk4I2jmZwoAQTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیران دفاع آذربایجان و ترکیه، زاکر حسن‌اف و یاشار گولر، در شوشا دیدار کردند و بر برنامه‌های خود برای تعمیق همکاری راهبردی نظامی میان دو کشور تأکید کردند.
🔴
دو طرف همچنین درباره رزمایش مشترک «قدرت اتحاد-۲۰۲۶»، همکاری‌های فنی-نظامی، آموزش نظامی و امنیت منطقه‌ای گفت‌وگو کردند و بر تلاش‌ها برای حمایت از صلح پایدار در منطقه تأکید داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150563" target="_blank">📅 13:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150562">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
معاون وزیر راه و شهرسازی: ما برخلاف آمریکا که همه‌چیز رو تحریم می‌کنه، با افتخار اعلام می‌کنیم آسمان ایران بازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150562" target="_blank">📅 13:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150561">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عضو سابق شورای اطلاع رسانی دولت: پزشکیان به این نتیجه رسیده که وزیر نفت باید تغییر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150561" target="_blank">📅 13:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150559">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEoldkRRIF5Hyw0W2i8N8VHrVlXtujXRlcWGB_hqSrNr7OQCcOx5zZMOm6rzej-Cm8_Xs5oWehrAZlcWjKDQJ4_kHEq83iXDxO-L3LVNJDYwRykBTlcWiDEyfu7lybmuRb2A_lnf0KsJ-WkQG18tCRFFHorhSa33iWCsOn452RQt9VYHA-saBzHbNeGJ9gfp6OphNHVnKdFoOWtjQ3AzANiDhHzbVHTh_uv07MTB1a8_tyqYcNsgSbg-hGXG5H1DjHOO0r16HPZMug464TOS2A9Ep33TOB4_7nF5qxt5XN7CrOxXBckK-W6dJiinW776POjrLGeiwORF8CUDo3gqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک برای دومین بار:  اینستاگرام فقط واسه دختراست، اگه پسرید باید اینستاگرامتون رو پاک کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150559" target="_blank">📅 13:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150558">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBmSoNyaMG8N2ZHfHzwByBNSiy5Y_Hv9PooiAurNxfs1xR7goQDQ-6y_6sCmTAMM2DhfoxGuheYAaxmABcD2ibXsCVHCfcfNTuxwD7Rwjm4vyWQWBJmfoS8Hr5M17iMDA4jIFQ7ovZhDg9MF-o6pj6Ch9Ezc4MIlFjvKofMkkktbcYhJ0cPL_ybfbezFual1FHYHx2FgG_p1Rff5ceyZwGtjYLLcfhd7TufIBLookLp7v0FkO_yiG9CcyMmOAg8MBRMlU0_x02CXvdFRx1Ya3YPc2c3HMz4gCeRIAr5_r7blzolMNOCjPexq9Db8Q0paSQW6m2f7n9of4EYDq1tmLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی: در جانفدا ثبت نام کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150558" target="_blank">📅 13:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150557">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل: ایران قوانین را نقض کرده و هرگز حاضر نیست از جاه‌طلبی‌های هسته‌ای خود دست بکشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/150557" target="_blank">📅 13:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150556">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
هواپیمای نظامی سنگین پگاسوس B762 ارتش آمریکا هم اومد خاورمیانه !!!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/150556" target="_blank">📅 13:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150555">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پالتیکو: اتحادیه اروپا برای استعفای «فردریش مرتس» از سمت صدراعظمی آلمان آماده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/150555" target="_blank">📅 13:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150554">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز: فرانسه پیشنهاد آزادسازی ۱۰۰ میلیون بشکه گازوئیل و نفت را ارائه داد
🔴
منابع آگاه از پیشنهاد فرانسه برای آزادسازی ذخایر گازوئیل و نفت کشورهای عضو آژانس بین‌المللی انرژی با هدف کاهش قیمت در بازارهای جهانی خبر می‌دهند.
🔴
بخش عربی خبرگزاری «رویترز» پیش از ظهر امروز (جمعه) در پایگاه اینترنتی خود نوشت که بنا به گفته یک منبع آگاه، کشورهای اتحادیه اروپا در پاسخ به فشار آمریکا بر کشورهای این قاره برای عرضه حجم بیشتری از ذخایر گازوئیل خود در بازار با هدف کاهش قیمت‌های رو به افزایش سوخت، پیشنهاد فرانسه برای آزادسازی مقادیر بیشتری از ذخایر گازوئیل را مورد بررسی قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/150554" target="_blank">📅 12:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150553">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXP7UU6vnjLF62IuQalOghNKPeQ5UeHujm-V6rR8Zd6Bg_R_z9swZO_cnTYcHjzf1OUldNEPdRDnZPmu8uQ5VQqvNhTefY54MhBF0-ZjXW_dE2YY-fSyQat61mkUIOwE9On6b5GWoWL3lM0lfzM_1MX9jUbHgNIRq3CBXD-NPhi_hBNIQE6GiPb3_33bOCCIitD6B5rOSpTLp_-37wa9XVANG-rmMCMkhi1TqAJBMSkpmqSm7fXPBJ8nA9gXIoBQBL3suzYxqe54MVCnExlFpIp7nJn_dmXqfwxyon7sqFdqN6YwjavzUkzO5LBTd1ICJ9csYsmgx4oBYzpL1KSW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، ستونی از دود غلیظ را که از میدان نفتی عین دار در شرق عربستان سعودی (یکی از مهم‌ترین و بزرگترین مناطق تولید متعلق به میدان نفتی غوار) به هوا برخاسته، نشان می‌دهند. این حادثه احتمالاً در نتیجه یک حمله از سوی نیروهای یمنی رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150553" target="_blank">📅 12:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150552">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8hHFjVPcghe8Mj773utqZMUW-Dkvk_gWotw9Yarue1wpRie_yTQ7Y7jn_R606yiJjxpnZGjhslpsecHcyPhUqAwksY7vzS2EffjTxSSC6dzKvIoihlmcmP--UniKalkiTO4aJe3w5v1E2hWDsjXVax0SFrziyNiIr1pUVPlhxVpN6nEJzM22wteEtAPe9M1nJwnpaK01AGhAPkRvEFkcBKHFNde5-m5PgOTUvQLIasluOQOb9YOcTE4vG5TAH2o_37gpKQkWcii5G1hn3ZbVkxQsHit2t5JXhV58S9uumwRf-LbC8COrHNgGmKdmAsDx-FigsbjjDJUD-GyYg1I_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی عربستان سعودی حملاتی را علیه مناطق حیفا، الکدحه و سامع در جنوب شهر تعز انجام داد تا از پیشروی ارتش یمن جلوگیری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150552" target="_blank">📅 12:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150551">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDOE_1WNxkCm0gWTxwIE2Rx75Kh9ucKcmMMFfarjP0O3xv-Sx1rWuugSEbqhUR62YB4MhGbxs6IHIiLJDDuR89NuyvKaOEjrPPkJ0UFPtg4tt2tCLqNjsKDLZ0pRfXbNQyb9grZntIwNfoTluc_vkBGx-kVwFT6axD8X6r-b2vHMU6-idVo4XmGxpvKEa-HJnzGlOt_Fi_-pclNVIBo4NYTXL-sJLarUeJSOp4meHYgmoKlu5T7OdtT5PcvPynLKK9hL5uKTBZHd5kk4ZfS9U0CQlJs3_NzAi4G7-QUdqGVrIsKFDumh7jDjIb6U4tmjDL8ToTEcva1o8Xb8V4uYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: حجم صادرات گاز طبیعی مایع از تنگه هرمز در ماه سپتامبر به بالاترین سطح خود از زمان آغاز جنگ با ایران رسید. در این ماه، ۱۳ محموله از قطر و ۶ محموله از امارات متحده عربی صادر شدند که مجموعاً ۱۹ محموله گاز را تشکیل می‌دهند. اگر این روند تا ماه اکتبر ادامه یابد، ممکن است شاهد بازگشت حجم صادرات ماهانه به ۲۵ درصد از سطح قبل از جنگ باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/150551" target="_blank">📅 12:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150550">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
امروز، سالروز «جمعه خونین زاهدان» است
🔴
آن روز بعد از نماز جمعه، تجمع‌هایی در اطراف مصلی بزرگ زاهدان و مسجد مکی شکل گرفت و در ادامه درگیری و تیراندازی نیروهای امنیتی رخ داد. بر اساس گزارش کمیته حقیقت‌یاب سازمان ملل، اطلاعات معتبر از کشته‌شدن ۱۰۴ معترض و رهگذر در آن روز حکایت دارد؛ این نهاد آن را بالاترین تعداد کشته‌شدگان در یک روز از اعتراضات ۱۴۰۱ دانسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150550" target="_blank">📅 12:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150548">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z84jKeXMJRfoD2fsX7ji5d85rQ7vYhYS-aajvV3Mh6flyoBi1cQB0IS_7PWkQDUxhdKRbxcwLnsR31JWFAQ8lIWGjOgzh7T6LdTfs5_keLVTQtffELGOJd_0gJnY_slt7-sK-fiHBaisX5O8dTqpsGq-VFOwlv1AaI27HzJiZ2UvzAu-162_WOsGqeKkdXzxWkirPPTjE2VPNM6jfmCP8YR1y4E_DLYFrcXhCYhmTbSHo3Z0_5eBrdW7mjZhHG84GzBeroREp6_brrBUNihJwOYsYuNzq15UuTEvMRm6GpXHNqojVfX9mI2-KErCnM1aJ9uttfSi7Aqp2-187aEAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
در اغتشاشات و کودتای فرانسه تاکنون هیچ کسی کشته نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/150548" target="_blank">📅 12:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150547">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219d012c04.mp4?token=C2KM9NvddSQ2ixIyIop6ogsnrsWWA4f2CWlns6qGXUZVfhnqcD7sFSWfG5-w3bvlWaq3XKX8oY01Qm0FvdH9ZtoQGbgmy4sHrQnUQgwId6JxUnFd0Ka6ssRAOeunZKmY2swEGBi-8j7JrddV6dy-bEZZSNoZ0z6jbildFVzVgk4gN-AX8huJS2yn3POXvDSNBIrSB5ksgfkI9-Zzt0qgoWLDujhy6YefqWNOdNJA1nzN2HIEGZeNgWeYHgN6nKKTSNGlZuLMTJedEqair5G-OjXzMVsTWM91pD2bX9WbGCH6H7lYNLgzjSP_-ALGvEbBFhStg2xRPyl0g7Xmw1CBZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219d012c04.mp4?token=C2KM9NvddSQ2ixIyIop6ogsnrsWWA4f2CWlns6qGXUZVfhnqcD7sFSWfG5-w3bvlWaq3XKX8oY01Qm0FvdH9ZtoQGbgmy4sHrQnUQgwId6JxUnFd0Ka6ssRAOeunZKmY2swEGBi-8j7JrddV6dy-bEZZSNoZ0z6jbildFVzVgk4gN-AX8huJS2yn3POXvDSNBIrSB5ksgfkI9-Zzt0qgoWLDujhy6YefqWNOdNJA1nzN2HIEGZeNgWeYHgN6nKKTSNGlZuLMTJedEqair5G-OjXzMVsTWM91pD2bX9WbGCH6H7lYNLgzjSP_-ALGvEbBFhStg2xRPyl0g7Xmw1CBZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار هم اکنون 259,900 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150547" target="_blank">📅 12:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150546">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnlfXLQMpbBF0Dur27mDR1-TClqHOJkD27zzyv-qUeY0WIJPMK_YxbrKEvhpjHaUdREajTRsl_NYilDCsonJy2w4u8UkW-C5HzwYrFV0EKongA5merPhjiPIwGIBbWHHnA1s9KYb1XN_r5yQlAzNalsRvEKOgO73FNpF5XmTNHYnyB4F1Lq0ohJ7wtxTtxFTqqHEWzhGYabezsWO_w3IvZxZo-QpdIvrFidZJtCY-I9tJsXNRzYyiwgIrwHSVtvMCqjyjQLL0mPTvwCGOyyq4opcjKIm5kZDK2WRpcQ_VN91j9THOIf4WdjReZ8sAmQCNsCQIcKGaY3LTEJh_lmYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین دوباره ۸۶,۰۰۰ دلار را پس گرفت و در تنها ۶۰ دقیقه، ۱۲۰ میلیون دلار از پوزیشن‌های شورت لیکویید شد. در همین بازه، ۴۰ میلیارد دلار به ارزش بازار کریپتو افزوده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150546" target="_blank">📅 12:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150545">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بزرگ‌ترین خریدار LNG جهان: انتظار نداریم LNG قطر به این زودی به بازار بازگردد
🔴
فعالان بازار نگران زمستان پیش رو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150545" target="_blank">📅 11:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150544">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8bbc2f536.mp4?token=b7DiUYyaUXZoGXChUYADgq-75gwqnkbPD8FgEqlAhxMdkGySzqo7snu3EniOspIqcoA3VNVlCQZAVrJznls_Xhke_HeWoZCFGJnWK2fKuiyl6oKakAj3eN6NGJ8VaMcNSwNv8m2o_ClpHdFLuFR7QGU3IHx4p8fkFPrE7KY2gTnDK4NQ4YdYfP3hdpbpvD_LdqQCCgKXDO74QftYbjWmmauTg5OYChkDPSjlZBAJc14HOBMMagRjQEbR77uabQ09M7h6vu9Lo4uHR-gxOYMAygot68MDaN1ygf8jZNypDmDO0a1qAVCaBZx3Cv5GmoCIAoo3cCFVAUAvG4sOTX8Hhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8bbc2f536.mp4?token=b7DiUYyaUXZoGXChUYADgq-75gwqnkbPD8FgEqlAhxMdkGySzqo7snu3EniOspIqcoA3VNVlCQZAVrJznls_Xhke_HeWoZCFGJnWK2fKuiyl6oKakAj3eN6NGJ8VaMcNSwNv8m2o_ClpHdFLuFR7QGU3IHx4p8fkFPrE7KY2gTnDK4NQ4YdYfP3hdpbpvD_LdqQCCgKXDO74QftYbjWmmauTg5OYChkDPSjlZBAJc14HOBMMagRjQEbR77uabQ09M7h6vu9Lo4uHR-gxOYMAygot68MDaN1ygf8jZNypDmDO0a1qAVCaBZx3Cv5GmoCIAoo3cCFVAUAvG4sOTX8Hhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: وقتی به پرونده‌های منتشرشده اپستین نگاه می‌کنید، فقط یک چیز کاملاً روشن است: بله، این دونالد ترامپ بود که جفری اپستین را به پلیس محلی معرفی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150544" target="_blank">📅 11:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150543">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC0QJlLjzttiD2sUB79HHxOKNI5NzYh4G3hz9o3g0juvwYhViuYaYT4lxdAG-VvZ9peCOgu_u88WmBGCasytOz0imL_6JzXo2c1qpbOpI8kDKjfipBP3B_YS8-42oHie7JX_5W0heqgnjn9GyCP3IH1t9L7rqo0ZwmqpxqRe_W5Bcf3K5kD6Tb_lMv8cxgCBsLfN5rq521K2U4I4kpeOXrnv4yiMNTJf01_lvvETqbtpDyzdJfzRUtBEwQ9XGhR00pMWvbbODa6ouszp0V6SdoUe6nfkNTbRdFscgCFryviXrA1GI1MY0Ge3wpx_UdjKaVmo7Vx6_5xOnCCd-l9XuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جکسون هینکل: سفر مخفیانه نتانیاهو به امارات مقدمه‌ای برای جنگ روز قیامت علیه ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150543" target="_blank">📅 11:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150542">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148764d5c.mp4?token=kRWssItUgRAOh7PEfxHV1gzUOlKEYhY9UqzCD8Q8novXcIqDFD1-rxUuzvaGdRONoWCQSEPH146BMY4FEec26AGc_-Twk55T0dnKnX7M0QcJnVPUtYx0-1LSKo_-uA9emlutu0mwWYJrk7l5bQtqn7wCQo6nePlBzLrARvKcJc2bBNpm_2sDYWYfwREGolyjsYRJbfNhPToQd2q8Ji8i-O_ESi9JTnRKpdgTHPaKwQn7ve8_ns8NS5whGeKKpQzwrk8yGnV3QHMuO03cQL5EJSmk6CJyqjjet1LDKItJiW7T_PFDvKwNr6LvhblgySEuRMRV9KbR30siz1rZkqigpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148764d5c.mp4?token=kRWssItUgRAOh7PEfxHV1gzUOlKEYhY9UqzCD8Q8novXcIqDFD1-rxUuzvaGdRONoWCQSEPH146BMY4FEec26AGc_-Twk55T0dnKnX7M0QcJnVPUtYx0-1LSKo_-uA9emlutu0mwWYJrk7l5bQtqn7wCQo6nePlBzLrARvKcJc2bBNpm_2sDYWYfwREGolyjsYRJbfNhPToQd2q8Ji8i-O_ESi9JTnRKpdgTHPaKwQn7ve8_ns8NS5whGeKKpQzwrk8yGnV3QHMuO03cQL5EJSmk6CJyqjjet1LDKItJiW7T_PFDvKwNr6LvhblgySEuRMRV9KbR30siz1rZkqigpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور برزیل: ما اکنون نفت در حاشیه استوایی کشف کرده‌ایم/ ترامپ از شدت حسادت، تلف خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150542" target="_blank">📅 11:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150541">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
معاون فناوری وزیر ارتباطات: با این روند، در بحران بعدی مجبور می‌شویم علاوه بر اینترنت، برق را هم قطع کنیم!
🔴
به دلیل نفوذ استارلینک
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150541" target="_blank">📅 11:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150540">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2b8312ee49.mp4?token=dHZI-_RnPY9tH1t6RQWSqp8075d4WQSOOQuianzHthnL4N4x_nmY-LdK0mMicKOq6WbH-MwMUXcXzHpgXY8r0gaLOmXm4NNnQi31f3g5OOuGcVPQ85DFkNd_ecePS6rU26LYx02s0DF5dXRy0GMVNLdRw85cJ9BxH8BsRui539x7-avtZX4FFUHzqJrbd_oNlS3emYJqSnHoMFZGOX58ZXgbpCKlJrDxg9H7pf1OAsMsLTxvc0RHZD6PDW_asvKFh7Ji4lRBBu593Zdpt_HcO4dqlftY1EShxObIeAb9m8BQaIBCyXuRpG4u8ICB3wyzB-S-t_h_E1hwnS-mQUmJwKYRO78xGPVBtMtROVfPniXnDSlyoeJKiMgRSSHzhFsp-cRllTfpBTqic2pUIgj5ND0g_Y0dxLGM2DC1_PL1fIg1PjVFAmWalXzxJXAHsIehFBc-r5bJmXhRjFjvSZRbNx2Fe1BPBY8XhlMbsVLTqOw3vULTbBcVXGJv2Z2FKQgoyshFuFXdqSH5mR2rC5qcsb-beuo8iv5Iy7cjyPbTg5l2e3AzPzOxvm5ssHSZZ-CQP11AWRjQj4vJcWBqenfgZkmrOcQ9lpqvUeno7qn6GbMBuKArmE8dk5UhJKTpo1by5AGO2ZZYaOm-SbtGbfaYjI4yrsUV3MR9IA6kOTeN3LI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2b8312ee49.mp4?token=dHZI-_RnPY9tH1t6RQWSqp8075d4WQSOOQuianzHthnL4N4x_nmY-LdK0mMicKOq6WbH-MwMUXcXzHpgXY8r0gaLOmXm4NNnQi31f3g5OOuGcVPQ85DFkNd_ecePS6rU26LYx02s0DF5dXRy0GMVNLdRw85cJ9BxH8BsRui539x7-avtZX4FFUHzqJrbd_oNlS3emYJqSnHoMFZGOX58ZXgbpCKlJrDxg9H7pf1OAsMsLTxvc0RHZD6PDW_asvKFh7Ji4lRBBu593Zdpt_HcO4dqlftY1EShxObIeAb9m8BQaIBCyXuRpG4u8ICB3wyzB-S-t_h_E1hwnS-mQUmJwKYRO78xGPVBtMtROVfPniXnDSlyoeJKiMgRSSHzhFsp-cRllTfpBTqic2pUIgj5ND0g_Y0dxLGM2DC1_PL1fIg1PjVFAmWalXzxJXAHsIehFBc-r5bJmXhRjFjvSZRbNx2Fe1BPBY8XhlMbsVLTqOw3vULTbBcVXGJv2Z2FKQgoyshFuFXdqSH5mR2rC5qcsb-beuo8iv5Iy7cjyPbTg5l2e3AzPzOxvm5ssHSZZ-CQP11AWRjQj4vJcWBqenfgZkmrOcQ9lpqvUeno7qn6GbMBuKArmE8dk5UhJKTpo1by5AGO2ZZYaOm-SbtGbfaYjI4yrsUV3MR9IA6kOTeN3LI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تایوان نخستین ۲ فروند از مجموع ۶۶ جنگنده F-16V Viper خریداری‌شده از آمریکا را تحویل گرفت.
🔴
این جنگنده‌ها در پایگاه هوایی چیهانگ (Chihhang) در جنوب‌شرق تایوان فرود آمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150540" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150539">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
آکسیوس: گروه آمفیبی، نیروی دریایی پیاده‌نظام و گروه اعزامی دریایی سومین گردان تفنگداران دریایی، از پایگاه دریایی سان دیگو به سمت خاورمیانه حرکت کرده‌اند.
🔴
آن‌ها حدود دوازده فروند جنگنده F-35B و همچنین حدود 2200 تفنگدار دریایی آمریکایی ویژه به همراه خودروهای جنگی پیاده‌نظام و نفربرهای زرهی را به همراه خواهند داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/150539" target="_blank">📅 11:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150538">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7isMjVT7pg4IsiRjKDHu40udm-bqNge2Fb5ckOis3rtHBmae9SaMXnPnKm45QurGgM1CQtJvuDicYr2W6MKp-QJrFjgtiKbsUkqkC7_1kieT10GUTqs_HsJgogctxIHTx4WMfYXgsmdfkArtr1UleUMm4ngNvhnQWauRK6Oo2wOANRMyMrvI0i5Qlth8DDCkaaQIZk2Y3dp2Tf3YxjMwpRy9rAKnwJhstaoWCGM2fxTf6G91fNPAsK_0-gLMx20xn7vLx9j4YgfofrR4Lf76XTRPBYcjuIAUXJVRY9kwAkKkBN5iI0Z6Tlnfy9aFMcwXeRgLjBIZQK5Pk4McKH4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطر: دوحه حمله حوثی‌ها به یک ایستگاه توزیع برق در مدینه را که برق مسجدالنبی و تأسیسات غیرنظامی را تأمین می‌کند، به‌شدت محکوم کرد.
🔴
قطر بار دیگر بر همبستگی کامل خود با عربستان سعودی و حمایت از اقدامات این کشور برای حفاظت از حاکمیت، امنیت و تمامیت ارضی خود تأکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/150538" target="_blank">📅 11:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150537">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYIiBrRgXYN0tz3OEzh8rBKEMfKC6BkhDRVrzMEWSy1ekd3ejFZvneo53SzACBbJxtFRbpzQzloEx-cloet7eSRguhevSSPAli96ciMYlFMiV2xJ0CyWfS22jFV3jSERkWh0n5Bj1oiFonLy6-nF2kkHNsYQMIMLcdvcuxAcA9-PccQO6cZ8_kaFMfUgbZ3jIKfxZCc4Oh6vtfIPBYL2CfrdEE7hcyYWmHRhxptAnDeeSsHrjS1po0mRBBIb7C6VQ--K2sZXPgYfrr7r9YTkbW55ZuqSnnPNSLf7-vrXJ7-njepHtTOHhG-1-CKtyBu0FYoBmzPGtXepSew1w7YfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای آمریکایی مدل E3، که برای شناسایی زودهنگام تهدیدات هوایی استفاده می‌شود، دقایقی پیش در آسمان شهر ریاض، پایتخت عربستان سعودی، در حال پرواز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150537" target="_blank">📅 11:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150536">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
لغو پروازهای شرکت «العال» اسرائیل برای بازگرداندن مسافران از دبی
🔴
خبرگزاری فرانسه گزارش شرکت هواپیمایی «العال» اسرائیل اعلام کرده است که پروازهای برنامه‌ریزی‌شده امروز برای بازگرداندن اسرائیلی‌ها از دبی را لغو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150536" target="_blank">📅 11:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150535">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
یکی از تاثیرهای بستن واردات خودرو گرون شدن خودروها بوده !!
🔴
پژو ۲۰۷ اتومات فول رو دارن ۳ میلیارد و ۶۰۰ به بالا اعلام میکنن !!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150535" target="_blank">📅 11:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150534">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a884a3e7.mp4?token=Lc25ODFScD19HBS9xy0bzTFyQdvnIzm6AsR5JqtGFC-olQYRjtZ2zT5GQ0IDVmx0HUfGExOWlPKxTWUUNMe3L2y2L_eiHcljMtKjLe05--Lqle6eY3L7XCVd4Z7YjeS71eecnVU9Ddq7VG3ZQWWJ1kP6j1q4AdbhBu8TvnVhoVf11H23ueTYjb6y-70ffNVxOHjfyYs9Ced8NI259bB1KZKOBKEQZhlBrF9ivdcyD5xYX7yhLrAa9lUBOfr1bbwlnXZiH5D3gQSkjWKWHwHlzAWNgdQ7fTdO1M7jT5FyqdlcvajClXtF8donPzvRxLJ713K3MSVQtRRWRA2QvKuMZporYOlpWSxjrfAPNz6JczIU8k595Roz39fqES4FhQcAOtYR3vnor1wVzg6TPhLRAuf5Ua5FQRw7-MGQT63ilKdMuxjJjiM8CR9Td6FHQwplruvwRa-_Y9MnjROCrPar74gBcHiRHVNJuoqGVO0ZRfTFCrDnbhpF8oVLXf8HusiVfE9by9q03mWl9tr0sFqbY1PId_pbBez_La4stDQhFdE2Qpoq_r0vEBzcauvMFcEqCeVjgRqGArQvtIbxq7moopyYBpVqACB4xuR_uHL3m-qQjIe84Fg1JcQJNpTqdajKAbMiQwSeTIJtdFzPyChsTs15DSUMdwVj_X--RNAj0xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a884a3e7.mp4?token=Lc25ODFScD19HBS9xy0bzTFyQdvnIzm6AsR5JqtGFC-olQYRjtZ2zT5GQ0IDVmx0HUfGExOWlPKxTWUUNMe3L2y2L_eiHcljMtKjLe05--Lqle6eY3L7XCVd4Z7YjeS71eecnVU9Ddq7VG3ZQWWJ1kP6j1q4AdbhBu8TvnVhoVf11H23ueTYjb6y-70ffNVxOHjfyYs9Ced8NI259bB1KZKOBKEQZhlBrF9ivdcyD5xYX7yhLrAa9lUBOfr1bbwlnXZiH5D3gQSkjWKWHwHlzAWNgdQ7fTdO1M7jT5FyqdlcvajClXtF8donPzvRxLJ713K3MSVQtRRWRA2QvKuMZporYOlpWSxjrfAPNz6JczIU8k595Roz39fqES4FhQcAOtYR3vnor1wVzg6TPhLRAuf5Ua5FQRw7-MGQT63ilKdMuxjJjiM8CR9Td6FHQwplruvwRa-_Y9MnjROCrPar74gBcHiRHVNJuoqGVO0ZRfTFCrDnbhpF8oVLXf8HusiVfE9by9q03mWl9tr0sFqbY1PId_pbBez_La4stDQhFdE2Qpoq_r0vEBzcauvMFcEqCeVjgRqGArQvtIbxq7moopyYBpVqACB4xuR_uHL3m-qQjIe84Fg1JcQJNpTqdajKAbMiQwSeTIJtdFzPyChsTs15DSUMdwVj_X--RNAj0xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : آنها به سمت کمونیسم می‌روند. آنها سوسیالیسم را پشت سر گذاشته‌اند. بدترین افرادی که تا به حال دیده‌ام، در حال اداره امور هستند.
🔴
اما اگر جمهوری‌خواهان در مجلس نمایندگان و سنا پیروز شوند، من به تمام شهروندان بزرگسال آمریکا، به هر نفر یک چک ۵ هزار دلاری خواهم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150534" target="_blank">📅 11:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150533">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6HXa84hH8SwrG3iEcu0Xzs2j_mepGDbV4fv19YGWtDscvBdxO_r_akZMX6OPz8PpLdtXywo7kt7iF3-Hhq47hZBiW516NhjxL9RskyhxNMIdt5r40CiMTfkmM_phNGCkzmAcaoykhYCouXy82fe4FtoeU3AyAR5Ak95GLpNyNimycoHCDDqRAIcgVp1HIY0BLmx12ZvfKJGyQ8_pBJhsl9SX2AOlacXAbhkjjJec7zYads4S1M-TNlwkDm_qE9ChoEhs39q6SYHFVCERmzF4GIo2IuN7tco_xgCBvHLAXL_6egsKAEQSL6h_YeZnGuDiOBvpGijWgZV34yxCQ2qLXU5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6HXa84hH8SwrG3iEcu0Xzs2j_mepGDbV4fv19YGWtDscvBdxO_r_akZMX6OPz8PpLdtXywo7kt7iF3-Hhq47hZBiW516NhjxL9RskyhxNMIdt5r40CiMTfkmM_phNGCkzmAcaoykhYCouXy82fe4FtoeU3AyAR5Ak95GLpNyNimycoHCDDqRAIcgVp1HIY0BLmx12ZvfKJGyQ8_pBJhsl9SX2AOlacXAbhkjjJec7zYads4S1M-TNlwkDm_qE9ChoEhs39q6SYHFVCERmzF4GIo2IuN7tco_xgCBvHLAXL_6egsKAEQSL6h_YeZnGuDiOBvpGijWgZV34yxCQ2qLXU5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، درباره حملات ژوئن ۲۰۲۵ به ایران:
🔴
«آنها درگیر مواد مخدر بودند، اما در عین حال روی برنامه هسته‌ای کار می‌کردند. اما این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، به‌شدت هدف حملات قرار گرفتند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150533" target="_blank">📅 11:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150532">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfWZu-1RFyScViHrf50tS02jq5rLitwVnHzCCvKrM0ePcjaR7wKzFcpfaxu0wcz_1NqF4RniWpH8_1kz8730MAREFK13S6sLp0Gcfw_55p1MPsBVPJDvMu0Tr6ZIWlKWVK_zEEn7y3PFCGU6bgeYaWAhyE3q8f9z4iF3o2JoLxd5QREjHcpIKOQvhzo9XnMJFO51j6gs2FOmb8UX1VxG_G05cIBBTogGfk2sNdkF-LQmLQX0gWIjxarAKjK6lZSqRH4YXkyAvjy0VYjdlf4Mk5lzJFPsY5Wn7v_vVb-Z9Gi-6ExqV0aUS-Pj7TFg-MhiHNwzLW66E5VYnejJFVZxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت سنگاپور برای اینکه آمار ازدواج بالا بره یه سایت همسریابی راه انداخته که فقط افراد بین ۲۱ تا ۳۵ سال می‌تونن توی این سایت ثبت‌نام کنن، این سیستم فقط یک نفرو بهتون معرفی می‌کنه تا الکی وقت‌تون تلف نشه و درگیر انتخاب‌های زیاد نشید، هر کسی رو هم انتخاب کنید و باهاش قرار بذارید، هزینه دیت اول رو دولت بهتون میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150532" target="_blank">📅 11:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150531">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc84ea8cfb.mp4?token=UW_qD5JSiuGV1O_5J6fIsSZi0huJH0w5VoZ60LQAI2VU7xJ2eDxUKsu9lhukiXchD8_2KtL_LtHvT81Hqb77PB8YG_TaoNGAW5ctkAwTsEQaP7q2tFdR2SbgQarF4thIpVW1uB4NE6JwAWDwq0-1InbV0chLhhqZIk9mCxKbxzm6nVIvjN-DHNz3pNcCFXrhiiCVMgpj76BYA17wWV-kNYCAFrDCPifsAwVr3tybC8R5Nx1ZAOmLDuNMUSdOr7gMdtCgJwUZI28NKJ_j-zNyusdnB0XvUuIV6au9WPKt12PqJiy3M8bozZ_RzpqaAB2SPmN0QOTui3JX_7vqvcMTzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc84ea8cfb.mp4?token=UW_qD5JSiuGV1O_5J6fIsSZi0huJH0w5VoZ60LQAI2VU7xJ2eDxUKsu9lhukiXchD8_2KtL_LtHvT81Hqb77PB8YG_TaoNGAW5ctkAwTsEQaP7q2tFdR2SbgQarF4thIpVW1uB4NE6JwAWDwq0-1InbV0chLhhqZIk9mCxKbxzm6nVIvjN-DHNz3pNcCFXrhiiCVMgpj76BYA17wWV-kNYCAFrDCPifsAwVr3tybC8R5Nx1ZAOmLDuNMUSdOr7gMdtCgJwUZI28NKJ_j-zNyusdnB0XvUuIV6au9WPKt12PqJiy3M8bozZ_RzpqaAB2SPmN0QOTui3JX_7vqvcMTzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «ما همین حالا در عصر طلایی آمریکا هستیم. ما داغ‌ترین کشور در سراسر جهان را داریم.
🔴
ما دیگر به آن جهنمی که برای مدت طولانی در آن زندگی می‌کردیم بازنخواهیم گشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/150531" target="_blank">📅 10:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150530">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb92e856.mp4?token=DErAwM-y8_G9X2t38MJA60HwcyAdGGE9zrKZH-fAseliNWzM-jAwDLdkrrE_V5BFBSQD2gpW491DP0opAdhC25gxufZh1NpKxM6oa2fe1VkdZjQnLL8VRdIDLf-Ktu5SGrMZ0mDHsCCLi8Tuq_MO3cmMHUCiW-DDjhSt3No3ZDKm-Cx--enoCf9_o6Y1mVH20EMmOxlWx39fdu-aFfvGoGqeWyiHkFUEK2tet8YNpBR5_VgHVdPzeyMbpyVvpsULUKMUkPWlviQB5UHxJg_4Uy-mhqy4yR3PM-DAfh7cA_MO9fv0LxYsyNGfpLNYsCf7Sth5UlgMq4Jk5_AC8fOyEmobPW0hMuwuAiqRolx58i08xRWNwFvwEEZJWQkgoz9RXZXoqytg0B4o-rI2MIb2PPLa_Bbo9xd1rNiVIzpWeQ2eqdgTrBmUA7U_C8O4QwjOHWmrXTpXcDluzMxvAK1JkVLKoxrgnrRvZtBsvbnokxTcY08WBMFQGorhD41hTQyJBqp0CGt4WCobWDpUpI1_n9wlV47PRLUpPjACYdwR9AfAeCCdeELFpLFD-u1_XIb9lmOcpt74nS_6KepejTmwIjQnvzb6QH5Qr078geqvvgMhh9WQbX2AN2xWdc31EC4uG2z57SyHEJc8Z68x8cQN0VI_4u_lCgOp7ajSrkJpS3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb92e856.mp4?token=DErAwM-y8_G9X2t38MJA60HwcyAdGGE9zrKZH-fAseliNWzM-jAwDLdkrrE_V5BFBSQD2gpW491DP0opAdhC25gxufZh1NpKxM6oa2fe1VkdZjQnLL8VRdIDLf-Ktu5SGrMZ0mDHsCCLi8Tuq_MO3cmMHUCiW-DDjhSt3No3ZDKm-Cx--enoCf9_o6Y1mVH20EMmOxlWx39fdu-aFfvGoGqeWyiHkFUEK2tet8YNpBR5_VgHVdPzeyMbpyVvpsULUKMUkPWlviQB5UHxJg_4Uy-mhqy4yR3PM-DAfh7cA_MO9fv0LxYsyNGfpLNYsCf7Sth5UlgMq4Jk5_AC8fOyEmobPW0hMuwuAiqRolx58i08xRWNwFvwEEZJWQkgoz9RXZXoqytg0B4o-rI2MIb2PPLa_Bbo9xd1rNiVIzpWeQ2eqdgTrBmUA7U_C8O4QwjOHWmrXTpXcDluzMxvAK1JkVLKoxrgnrRvZtBsvbnokxTcY08WBMFQGorhD41hTQyJBqp0CGt4WCobWDpUpI1_n9wlV47PRLUpPjACYdwR9AfAeCCdeELFpLFD-u1_XIb9lmOcpt74nS_6KepejTmwIjQnvzb6QH5Qr078geqvvgMhh9WQbX2AN2xWdc31EC4uG2z57SyHEJc8Z68x8cQN0VI_4u_lCgOp7ajSrkJpS3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من می‌گویم: «می‌دانید، تعرفه کلمه موردعلاقه من است.»
🔴
و رسانه‌ها حسابی به این موضوع واکنش نشان دادند و گفتند: «پس خدا چه؟ همسرت چه؟ خانواده‌ات چه؟ مذهب چه؟»
🔴
بنابراین حالا تعرفه را به پنجمین کلمه موردعلاقه‌ام تبدیل کرده‌ام.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/150530" target="_blank">📅 10:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150529">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb897effec.mp4?token=BYLK2vrqCsT1iMvwjgY7b7jrzg7wSmphPJl8R4kG_Sbqw1eqUajktejxRsFDYjQsUkwwN-0wdtc7Ycdzk8ujf9bT19w6xxj1HdolZ6mNq-_ffOfPx9VVzvVQ9bp3Dk8lmsHXfelWutYGkPq2ILkUP-VZDSIbz98n6atwcCEelc5aPPZ2vwuUhUKIEOzTXnvR3VkTTkheWhXnfNKIDy3_bCJaOWzwZ6YOSPYijoIkZxfcfTaxemq4XTr0nM9AdUmJBc7-On6sUb9jNOog-KOStbOZoBJMfGE7623Hdrc3mPt3pPSCDUzCuJV0ahUtGPXhz21jwkaoYW5tk4xk6vD2obk3NYY7iy5UdipxUuflwZZYTfHQeJ_1rOqVvSF90UoztszI3JPzoZZDd-dHTUeR5Yu0dNabPlEESWJ-1ptBtq-xe41hbxmKYd6pqnnuQxY6bvvwDyfwab0GsCnj2ruCylWWu8MDI9jHVxV-w5AoXeEqdD1UTUU6ZsO9dMg7wb-MfA9YdwfPfTQlPeoles2diZ0R7khqQNKL2-KF_Qzq-HOLo-_dEcqgZw3dJ2CssmCqtOHTDVSnnVEVkjtiiefwUrvlJPyg1dFFqR9GWPdAoGaVQm3g-dgFwpvm-pGXJp-XRCgP_8pwg_SGmPPZS86F5i4bsVTmCJutGIMDZHK1Lgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb897effec.mp4?token=BYLK2vrqCsT1iMvwjgY7b7jrzg7wSmphPJl8R4kG_Sbqw1eqUajktejxRsFDYjQsUkwwN-0wdtc7Ycdzk8ujf9bT19w6xxj1HdolZ6mNq-_ffOfPx9VVzvVQ9bp3Dk8lmsHXfelWutYGkPq2ILkUP-VZDSIbz98n6atwcCEelc5aPPZ2vwuUhUKIEOzTXnvR3VkTTkheWhXnfNKIDy3_bCJaOWzwZ6YOSPYijoIkZxfcfTaxemq4XTr0nM9AdUmJBc7-On6sUb9jNOog-KOStbOZoBJMfGE7623Hdrc3mPt3pPSCDUzCuJV0ahUtGPXhz21jwkaoYW5tk4xk6vD2obk3NYY7iy5UdipxUuflwZZYTfHQeJ_1rOqVvSF90UoztszI3JPzoZZDd-dHTUeR5Yu0dNabPlEESWJ-1ptBtq-xe41hbxmKYd6pqnnuQxY6bvvwDyfwab0GsCnj2ruCylWWu8MDI9jHVxV-w5AoXeEqdD1UTUU6ZsO9dMg7wb-MfA9YdwfPfTQlPeoles2diZ0R7khqQNKL2-KF_Qzq-HOLo-_dEcqgZw3dJ2CssmCqtOHTDVSnnVEVkjtiiefwUrvlJPyg1dFFqR9GWPdAoGaVQm3g-dgFwpvm-pGXJp-XRCgP_8pwg_SGmPPZS86F5i4bsVTmCJutGIMDZHK1Lgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «ما با همه چیز برخورد کرده‌ایم. با تورم مقابله کرده‌ایم. قیمت‌ها را به‌شدت پایین آورده‌ایم. آنها این قیمت‌ها و همه این مسائل را به ما تحویل دادند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/150529" target="_blank">📅 10:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150528">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c42cae8a.mp4?token=TjPzdjXLv0Y1ZwHzkeLb91gxFtjYVMfma1ppc69PPYHwDbjGtuh7Rg9mlqkNl57o_u_Wt3nSzVPAIIyUOP6GMNxMiEbjt-qU_VbUfMVm49uTfuaPgNgM91SieGAgnlqfWiwMw0QMUWph8fqmlGLIrg6DlGs6_lDjTO92P60qEFbjCvLyMf9lvTNKOvzVmiQXvn4MJQC5SG9haa0jvkBM0LiwNM_1WYjnobQd0AGAYTcRaeto0Hi8m7lQyFFhGuW_li5VrLILWaKXAFIOkZMVwieP2jZr4CD7jTGX9p8O8fw9cYSYgdNNI6XOR8y7nJs7_Sxwuno5jJVim202DBniykESeV8rTCJvkEOU-PQO1z9YeBVAP4uKCNiTRvxgfV7OMteqmhBjxmtkuVidD8uackT3JiCGGlg2REpOMv8LbJDsJT5wtuEc9RrxRrwPk1_xKeF2gmrTmjFhy2OaSNqScRlnH_4_fZU7OWTA0YdMScY7Kjj8Q0DSZYM___r0UU172trnUe0hTI4TY6Y9xQWn22dx5i5Kr-DoLY2j8eMTcTpIcTR6UCW2SpkPNuGe9bTUlxH1ppAcdWJz62xnNMiUO8y2wg_V8utaQzUTJl0-HN060Z8u3QyHTauMlpJozAXWc07SCuwGDkUxJZ9oDaN2eLdUtKUX82KGMs3D2AL1rLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c42cae8a.mp4?token=TjPzdjXLv0Y1ZwHzkeLb91gxFtjYVMfma1ppc69PPYHwDbjGtuh7Rg9mlqkNl57o_u_Wt3nSzVPAIIyUOP6GMNxMiEbjt-qU_VbUfMVm49uTfuaPgNgM91SieGAgnlqfWiwMw0QMUWph8fqmlGLIrg6DlGs6_lDjTO92P60qEFbjCvLyMf9lvTNKOvzVmiQXvn4MJQC5SG9haa0jvkBM0LiwNM_1WYjnobQd0AGAYTcRaeto0Hi8m7lQyFFhGuW_li5VrLILWaKXAFIOkZMVwieP2jZr4CD7jTGX9p8O8fw9cYSYgdNNI6XOR8y7nJs7_Sxwuno5jJVim202DBniykESeV8rTCJvkEOU-PQO1z9YeBVAP4uKCNiTRvxgfV7OMteqmhBjxmtkuVidD8uackT3JiCGGlg2REpOMv8LbJDsJT5wtuEc9RrxRrwPk1_xKeF2gmrTmjFhy2OaSNqScRlnH_4_fZU7OWTA0YdMScY7Kjj8Q0DSZYM___r0UU172trnUe0hTI4TY6Y9xQWn22dx5i5Kr-DoLY2j8eMTcTpIcTR6UCW2SpkPNuGe9bTUlxH1ppAcdWJz62xnNMiUO8y2wg_V8utaQzUTJl0-HN060Z8u3QyHTauMlpJozAXWc07SCuwGDkUxJZ9oDaN2eLdUtKUX82KGMs3D2AL1rLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا: «لطفاً فرض کنید من هم در انتخابات شرکت می‌کنم. فقط فرض کنید، چون نام من روی برگه رأی است.
🔴
اگر پیروز نشویم، در نهایت من را استیضاح خواهند کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150528" target="_blank">📅 10:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150527">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کرملین: برای مسکو، توقف ارسال مهمات و سوخت به اوکراین از طریق دریای سیاه، مسئله‌ای مهم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150527" target="_blank">📅 10:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150526">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
«شاید چیزی که بیش از همه به آن افتخار می‌کنم، همین آمار مربوط به فقر باشد.
🔴
وقتی درباره نرخ‌های تاریخیِ پایین فقر صحبت می‌کنید، یعنی افرادی که در خانواده‌هایی شبیه خانواده من بزرگ شده‌اند، فرصتی برای دستیابی به رؤیای آمریکایی پیدا می‌کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150526" target="_blank">📅 10:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150525">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
«تحت رهبری دونالد ترامپ، آمریکایی‌ها سرانجام واقعاً پول بیشتری در جیب خود نگه می‌دارند؛ بیش از آنچه دولت و تورم از آنها می‌گیرند.»
🔴
حالا بعضی‌ها خواهند گفت که هنوز کارهای بسیار زیادی برای انجام دادن باقی مانده است. البته که همین‌طور است.
🔴
بایدن ما را در وضعیت بسیار بدی قرار داد، اما ما پیشرفت‌های زیادی داشته‌ایم و اگر به تلاش خود ادامه دهیم، می‌توانیم پیشرفت‌های بسیار بیشتری داشته باشیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150525" target="_blank">📅 10:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150524">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3bfa2209.mp4?token=He6HFk9ldvKIFfh_NKlhGwnWDQ7VSL0sHMXldnU3z02PNQUu2Anp3Sus6xf988qdl-BOxoteqWy7MDFDh_4NO2AXi0-JoDyUJe17kUWCWMrZSRMOUHroH2RNk8x30fnJvs01QPiQJaQXjkkLwc1TcQSoRC-QkiQQGNwrVqzMUgJRvYMMFBOg7T8lRov5gRY1tcKAid6NcltpNj5vK0RMFAo4cuzcEp2q2R8H7kZzHt425cBzrmmpxWuNBzlpVGwS59aT-HhdHIjCGXyyOabOYXAsUSeR0dzxZZa1PBSQaK9p3VArjmLZuI_ke5imB4F-mzm2omoXI6m_BXLz2w_JOZefGTZlcknTKDn_GAYAU4Y1lPhYepoh5vWUoGfcI2kiif_aEU6b-91an9vGoIBTKQ201zTqCQNWAin_ReSqJ10fkqpo9ToPQAeCncp6wm1d1zKoXuhezeq3UANmjK7ye0bRwRjzgtlby0hccE_PD44FbMmy2nFWOBZzBkMZRsV-kA-2mjDMoGziRItAN9ZVavziV6RAS05lDv8FpIGYN4iSdCK7TN1LopFt3rTyJYsQJ1vy5-_ibPZaj2rTbsM0vI4BWDL7p_xwcCV5_wndkwo3oI7CEtQWqS-HlRsmVtYijVL4sJOsW-2U0jxAw16Z51XCBP8g1oNU-RaWMHNTPAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3bfa2209.mp4?token=He6HFk9ldvKIFfh_NKlhGwnWDQ7VSL0sHMXldnU3z02PNQUu2Anp3Sus6xf988qdl-BOxoteqWy7MDFDh_4NO2AXi0-JoDyUJe17kUWCWMrZSRMOUHroH2RNk8x30fnJvs01QPiQJaQXjkkLwc1TcQSoRC-QkiQQGNwrVqzMUgJRvYMMFBOg7T8lRov5gRY1tcKAid6NcltpNj5vK0RMFAo4cuzcEp2q2R8H7kZzHt425cBzrmmpxWuNBzlpVGwS59aT-HhdHIjCGXyyOabOYXAsUSeR0dzxZZa1PBSQaK9p3VArjmLZuI_ke5imB4F-mzm2omoXI6m_BXLz2w_JOZefGTZlcknTKDn_GAYAU4Y1lPhYepoh5vWUoGfcI2kiif_aEU6b-91an9vGoIBTKQ201zTqCQNWAin_ReSqJ10fkqpo9ToPQAeCncp6wm1d1zKoXuhezeq3UANmjK7ye0bRwRjzgtlby0hccE_PD44FbMmy2nFWOBZzBkMZRsV-kA-2mjDMoGziRItAN9ZVavziV6RAS05lDv8FpIGYN4iSdCK7TN1LopFt3rTyJYsQJ1vy5-_ibPZaj2rTbsM0vI4BWDL7p_xwcCV5_wndkwo3oI7CEtQWqS-HlRsmVtYijVL4sJOsW-2U0jxAw16Z51XCBP8g1oNU-RaWMHNTPAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا
:
«الان وقت آن نیست که بخواهیم درباره
همه مسائل کوچک و جزئی گلایه کنیم
.
🔴
ما باید کارهای بیشتری انجام دهیم؛ به همین دلیل لازم است دو سال دیگر به ما فرصت بدهید تا بتوانیم نتایج و دستاوردهای بیشتری برای مردم آمریکا رقم بزنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150524" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150523">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: قبل از دستگیری مادورو از هوش مصنوعی مشورت گرفته بودم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150523" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150522">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f5adc6d9.mp4?token=F9o5wZyh0IBhIPba8xftAuvYKJdteHx925dMZ5TWu-r5n6t4GwKKZ4T3-4xjo0itlfWKDSurSgKQFBcKGhVlURaurKoz0H_Vp_2rRJeoaInbK91U88qHXD1sfrXTZy0Ax0a1lcVGyMHbkcT-Nu5R7YqXMRZZFjDOamJXweUoiHUKL7rA4x7ejixKSsPkdxTKUmur3YU7BFfPh4ed8vDaHqFtTmHOQcFo0bj4-XOEDoS1gJRhr4BGomfNuQdWs4INaBrTT5jxldoNDExSwt8zqxSExL6QyDRgiDEBX173nZUMoSYVItDbLjHpowSHNk19BMSWT7DSVFg9zr728aMjdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f5adc6d9.mp4?token=F9o5wZyh0IBhIPba8xftAuvYKJdteHx925dMZ5TWu-r5n6t4GwKKZ4T3-4xjo0itlfWKDSurSgKQFBcKGhVlURaurKoz0H_Vp_2rRJeoaInbK91U88qHXD1sfrXTZy0Ax0a1lcVGyMHbkcT-Nu5R7YqXMRZZFjDOamJXweUoiHUKL7rA4x7ejixKSsPkdxTKUmur3YU7BFfPh4ed8vDaHqFtTmHOQcFo0bj4-XOEDoS1gJRhr4BGomfNuQdWs4INaBrTT5jxldoNDExSwt8zqxSExL6QyDRgiDEBX173nZUMoSYVItDbLjHpowSHNk19BMSWT7DSVFg9zr728aMjdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انفجار نامشخص در فرودگاه تفناز در حومه شرقی ادلب، سوریه، رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150522" target="_blank">📅 10:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150521">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKpFwqVshtdkm7dxthIu5vYCpG0ODGPUzA7Dwg2Lf5GM98H2iY2TIXEZ7pr5v84Jpp0XoQcKdMkIzYoP02lHIqDzyiTna7bkg241KaKZ0MPjeDvsF3s5pe8MnE4GwxFY4BiTFQb0xV7IzYm6v6Nu-Ob1NU5YepbP6jVW9wQ04JRrrywBU0TU5PK4DUiKEh7rs-Re6abCerBc6kyuFPWSfjebT2KBeF9XrHEqWgp1euM7LL9l-dn-WwnMdOR0ppXuZkDJDyedpmhSfri-Cm20K6e6n29DVA57TbMLVhG4zrs1ClfYy7uJjoRL8LGh95WlhIrd1N3NhmB1fBE2Y8YvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک آتش‌سوزی در نزدیکی سواحل عمان مشاهده شد، که احتمالاً مربوط به یک کشتی هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150521" target="_blank">📅 10:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150520">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8147803e67.mp4?token=ufbpfD3LkFIY7aEz8IcueOrtLfJG7jPkJsU-ol-jqv_7qaoqvleTKYtlzpeBWbsMlYbfGl8yaM93lxsHUFvxDQxcm3vHPsk7pcC_DeeLJGJ_B4qaI1o3BSLWlYhRcaRIEDiXySacS-ZZO4f9q5L0tTC8_9y31BH32Vexhg7IFFpoL67uDZGFePzs6IZZVpwlM5sk3PtjBu2obGTz-gKpyFSuiPVk_IVL1yzoPAq0OJbwM20PzAGL87pD0F_tzIXPwFVQfkFaY9GrvOLZnIhYVNCMAem3yQefb6NgePNPD7brKLjLrQ5YUp2xk5erxdz24edtcyg_NX76QQnYYkywG6QCVNNgkYUOK8KB5z82sYrag06IQTnrMueXH0Wx8o_vxp25ozQJPctiZsFP9U7XjFXzKLIzPGse_YoRHLahAYmvff_L45LZuMwKqYl1yTv0G03cbnEab03nKnLhGRQSiE-eZIl81DbRrYs6WLrqL6m0ecYVAtPbHWv7FzZs5U4YPgVdW4jaME4knaWSN7ZP4fb8Y78ZeNz1uvOWrE0cH2rLpigdri-wFiebWDbU8SqJiikgqWynFG-Rkl1idFkINQbGQHIdbXNES4_8ptP9JUXDIwA6T9jmV9sZQLNJpx4wrecTUDcjl_UFQdqZUf0NZWD7K1EE5_iT4hapLvYVETk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8147803e67.mp4?token=ufbpfD3LkFIY7aEz8IcueOrtLfJG7jPkJsU-ol-jqv_7qaoqvleTKYtlzpeBWbsMlYbfGl8yaM93lxsHUFvxDQxcm3vHPsk7pcC_DeeLJGJ_B4qaI1o3BSLWlYhRcaRIEDiXySacS-ZZO4f9q5L0tTC8_9y31BH32Vexhg7IFFpoL67uDZGFePzs6IZZVpwlM5sk3PtjBu2obGTz-gKpyFSuiPVk_IVL1yzoPAq0OJbwM20PzAGL87pD0F_tzIXPwFVQfkFaY9GrvOLZnIhYVNCMAem3yQefb6NgePNPD7brKLjLrQ5YUp2xk5erxdz24edtcyg_NX76QQnYYkywG6QCVNNgkYUOK8KB5z82sYrag06IQTnrMueXH0Wx8o_vxp25ozQJPctiZsFP9U7XjFXzKLIzPGse_YoRHLahAYmvff_L45LZuMwKqYl1yTv0G03cbnEab03nKnLhGRQSiE-eZIl81DbRrYs6WLrqL6m0ecYVAtPbHWv7FzZs5U4YPgVdW4jaME4knaWSN7ZP4fb8Y78ZeNz1uvOWrE0cH2rLpigdri-wFiebWDbU8SqJiikgqWynFG-Rkl1idFkINQbGQHIdbXNES4_8ptP9JUXDIwA6T9jmV9sZQLNJpx4wrecTUDcjl_UFQdqZUf0NZWD7K1EE5_iT4hapLvYVETk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:پادشاه عربستان سعودی گفتند که ایالات متحده زیباترین کشور در جهان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150520" target="_blank">📅 09:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150519">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f2907c5a.mp4?token=MUG0R7RK6ERYoAVzBUxzZ5Yy4Z99sDYu5T2KTOQKVnx00ZyZD8zFFT0nXy6xIIz2XnwJo2fF0jGLODPovu4CyD7FjvvDgA2-i_OKV7ryc3QfOiy-gJ_tQn41qHzFU3MlRelY84AQ49qBfBAE-XcVOEwR0sbOLbBhA6gZ86fIXT56BgzAYrAxiJkqgS02QmZsMROfGacLjYH1asgUkVaW8kxmS69d6GzSWafKczQr-60WaUxEPxRzxlXGZTgYborOluT4PAowiKV077jCCast3K0HBtY2jCxKqv8RPS7NeqsUtLio9bEBNSZ2CFQUOi7OPgwgRrEiRGrjTVFWHB8XZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f2907c5a.mp4?token=MUG0R7RK6ERYoAVzBUxzZ5Yy4Z99sDYu5T2KTOQKVnx00ZyZD8zFFT0nXy6xIIz2XnwJo2fF0jGLODPovu4CyD7FjvvDgA2-i_OKV7ryc3QfOiy-gJ_tQn41qHzFU3MlRelY84AQ49qBfBAE-XcVOEwR0sbOLbBhA6gZ86fIXT56BgzAYrAxiJkqgS02QmZsMROfGacLjYH1asgUkVaW8kxmS69d6GzSWafKczQr-60WaUxEPxRzxlXGZTgYborOluT4PAowiKV077jCCast3K0HBtY2jCxKqv8RPS7NeqsUtLio9bEBNSZ2CFQUOi7OPgwgRrEiRGrjTVFWHB8XZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد عملیات "شب پره" علیه ایران:آنها تمام بمب‌هایشان را پرتاب کردند - و این بمب‌ها مستقیماً از مسیرهای هوایی به این کارخانه‌های مواد مخدر اصابت کردند. در واقع، این کاری بود که آنها انجام می‌دادند. آنها سلاح‌های هسته‌ای داشتند و مواد مخدر قاچاق می‌کردند. آنها به شدت به این کارخانه‌های مواد مخدر، که در واقع "کارخانه‌های هسته‌ای" بودند، ضربه وارد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/150519" target="_blank">📅 09:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150518">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBYnj02DaCOnqlGjIygHaMfyG8Iii6SjJGlUNfl8EkrTLSH9YZMHtNb3o4duAvX7EqKAZiocZwviIIT5ukq6Q1J9kS92-6ghJjGEy2s4tS_po0DCySEIiiRoPDuaT4iaWQd9DSU2rzBzdNPlCOHUg0vNMLezdLQ8fq8YDDXUgVqynzqhPdB5u9d13v7n27x6KbqvOzc_IqUGQdTQA0yZHsGjmRx0i3UuhdN4PcvR83sPmzYnZuHZaumrl-CwdRYkKvSftlAGW04UqywCxkg9hZGPp4MLe9m1iLbQKsqq-ZKZZW6i1EtdmrWi0pRSDe65tuffw0LZZa1j_cMCrZtKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتخب ماه سپتامبر رویترز |تصویری متفاوت از دیدار ترامپ و شی
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150518" target="_blank">📅 09:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150517">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXD7UvUD16ZN-FLhm_w4wgmAbWDOgqDq_pS_J_yjBEbJ15JizdebH5JI57D_7BghPbDanWrytTVtpZmlcdAQbYtVcc8LBn9wMm7UcBmoRAY6R62nn0td4WK9bftwUUJajRJzZzPFQLcFFhkzwDe6H1SuuApHRuMmxUjWxD47kl7oCB1BS6f7HSW7lLzY7oyQ0U6ahLJPuAM7NYLvu0OzJA4f7xqOim8Sm4r6v-Df6db1KLMhT9mOuJfKBaXPVGJ8pmwxVbrIGuLqm8X9mfmSF7e3ca52wopiJRMqiEU5w5hKJ_ZlYO4Gw-veBIFdzXsT4Mc6gstHjsT-S7gC8_I62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای امنیتی عربستان سعودی در مکه فردی را به اتهام ایجاد مزاحمت برای رهگذران و ایجاد رعب و وحشت بازداشت کردند.
🔴
مقام‌های سعودی اعلام کردند که نیروهای امنیتی بلافاصله به این حادثه واکنش نشان دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150517" target="_blank">📅 09:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150516">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d51a563f90.mp4?token=LC39vjds6Mb0tYqCbv2NAHsVq8MLz8Qy4XBb86U7zDo5z90t1J2tFVECSGgYIu0vbMtpBWBz4Pt-fgyN6nEITiig3J_SVrJu3ERDqKmBlHTUdZjk5OoywIeQRvfnoXahVtI2RDWQv6_DKwiJu_7Wuxw4FAC4IiizU9k2dcAj9aHxV3VcARH93MSzJlKsjwpyGkgELyn87F4Vt9keHE6zGi4EPIrjcuxCa9AEM3gp5r19foM2FNrnk9fkXNM5BKNsg3p7gKsAm0yrw-nMYmqD9bnrJP6yINj80ZfVDfluqeSrxsnoYEFqfLehc0l0k6zf5gYOADZkMqoh4grf8lLx3rcY4ieeEDuGjpCcJGaAdjX17pIpyi2GL2JvknE2K5t2xxVr0H9NHwUof-jptMKDGrbPalbNCW3eimNF4qpwTBcG-ari1MkZEav07jxoR_EIbXG42XuxA0A_qkkxw14wjuK79alOM9SDawkg4_hF9uOSA80cwoP0-qh2TMqlOasYvq49r34QMyrG5_bNuvcsPPTTCO5nmEQxRDWsvmyhRt9tzQr8s_8ujgJaMEp366hJ_ru5oD1A4dLo88VrVN332Tg3MMbrqHu0w-Gtcr2jaNP5X1quKKwyxrwJ0B6dBG3z__o6mIXYNur05iyj2NrmDHeuyMS-wKvFICPA9MkNflU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d51a563f90.mp4?token=LC39vjds6Mb0tYqCbv2NAHsVq8MLz8Qy4XBb86U7zDo5z90t1J2tFVECSGgYIu0vbMtpBWBz4Pt-fgyN6nEITiig3J_SVrJu3ERDqKmBlHTUdZjk5OoywIeQRvfnoXahVtI2RDWQv6_DKwiJu_7Wuxw4FAC4IiizU9k2dcAj9aHxV3VcARH93MSzJlKsjwpyGkgELyn87F4Vt9keHE6zGi4EPIrjcuxCa9AEM3gp5r19foM2FNrnk9fkXNM5BKNsg3p7gKsAm0yrw-nMYmqD9bnrJP6yINj80ZfVDfluqeSrxsnoYEFqfLehc0l0k6zf5gYOADZkMqoh4grf8lLx3rcY4ieeEDuGjpCcJGaAdjX17pIpyi2GL2JvknE2K5t2xxVr0H9NHwUof-jptMKDGrbPalbNCW3eimNF4qpwTBcG-ari1MkZEav07jxoR_EIbXG42XuxA0A_qkkxw14wjuK79alOM9SDawkg4_hF9uOSA80cwoP0-qh2TMqlOasYvq49r34QMyrG5_bNuvcsPPTTCO5nmEQxRDWsvmyhRt9tzQr8s_8ujgJaMEp366hJ_ru5oD1A4dLo88VrVN332Tg3MMbrqHu0w-Gtcr2jaNP5X1quKKwyxrwJ0B6dBG3z__o6mIXYNur05iyj2NrmDHeuyMS-wKvFICPA9MkNflU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر حمید رسایی، نماینده مجلس در تجمعات شبانه: افتخار میکنیم‌ که آقای رسایی بعنوان یک معترض به بی قانونی و دستکاری متن بیانیه مجلس و تقلیل دادن شأن مجلس به وسیله‌ای برای تطهیر یا تعمیر آبروی از دست رفته شخصی رئیس مجلس الان در زندان هستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150516" target="_blank">📅 09:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150515">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c89d377a6.mp4?token=JmDlfPSiAp2o9U7TW8MtsK_UuaCvrQGLdONQDHWmfGZOZYaTYuGqsnFt1mlijmy88GebuVf3bXYH0v_q64xDI_jZDnulvH-M7x3lMb1SSLQ76zUyxz9zyYEVI_cV_kuEQctqKIrpD5pv5F6McXXd2arYP71akPK46uwJ2bVL4p2gUBhShHuQNJWIa7pP_QnZBBNtCgZBcIOfby8QMcu61XhOOm67SqMgOcK_IUinVrWAXbLOHqjXhQsqPrhiJNBFyYfZxA1HlDnXKeyrTr6GMQTJiNLfhfuSdycQ4FkCBtNsw-aM9X3POSSPc4EPw3GzOfIdyV59NCMslAuPT94lQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c89d377a6.mp4?token=JmDlfPSiAp2o9U7TW8MtsK_UuaCvrQGLdONQDHWmfGZOZYaTYuGqsnFt1mlijmy88GebuVf3bXYH0v_q64xDI_jZDnulvH-M7x3lMb1SSLQ76zUyxz9zyYEVI_cV_kuEQctqKIrpD5pv5F6McXXd2arYP71akPK46uwJ2bVL4p2gUBhShHuQNJWIa7pP_QnZBBNtCgZBcIOfby8QMcu61XhOOm67SqMgOcK_IUinVrWAXbLOHqjXhQsqPrhiJNBFyYfZxA1HlDnXKeyrTr6GMQTJiNLfhfuSdycQ4FkCBtNsw-aM9X3POSSPc4EPw3GzOfIdyV59NCMslAuPT94lQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی: «یکی از چیزهایی که به آن افتخار می‌کنم این است که ما در یهودی‌ترین شهر ایالات متحده آمریکا زندگی می‌کنیم.
🔴
هیچ فرد یهودی در شهر نیویورک مسئول اقدامات دولت اسرائیل نیست
🔴
اگر می‌خواهید کسی را پاسخگو بدانید، باید سراغ افرادی بروید که این تصمیم‌ها را می‌گیرند؛ یعنی نخست‌وزیر و دولت اسرائیل. همچنین باید نقش و مسئولیت ما به‌عنوان مالیات‌دهندگان آمریکایی را نیز در نظر گرفت، با توجه به اینکه می‌دانیم چه میزان میلیاردها دلار برای ارسال بمب‌ها هزینه کرده‌ایم و همچنان ارسال می‌کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150515" target="_blank">📅 09:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150514">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f877c2bb.mp4?token=oEpe0RpNdTE3gFjwXNeFH7fLZlxvjdoAyZzy49AaXKMhdcOiP0vuhN1n6yq9EujY9xsChjJvwv3jA7dRpnC48JjqnTWe5kmcU-KUKJLE1ZZ2GbWPCq-H8AsGCNN3fvR1tTwBrnONn2LcHjs4FDbJl7Gb_8pUEvBPtgsVXKn-QyqhrNE2noN8-xtPkla_f2Kj7FDSAQDsX1DZaNJWyHdpSDSl9JDfjM9B3-wUI4XD3sUg_N8KS-IL-Zlz0RZ1liTj-YhsBnqx2ALf7gnFKOUkHBO2Lx1g_l2OTHrEsI4TatMqJDKiyOExEv58fatz5_-_QmhRYYLWkofmXxMt2YPg4JAJyCJWEcWskw2J_lAB11qal_IsvnxRliY5A9jiFZ8NFm45KimXflSgG6gD0-4ZitOFWuHoBbHL4dqE0ApwFHetq0lUjeLCBI9yE04ijtqR4KfJbOg0PRDWPdmR67g5GTSasaj_SUTR3UEQJN45wa72rbub-p2YD4CFNWwCN_rE_L1tKQf6LsHopz-wILGlZqFThKhg0QMRAz0JmlBGACURDY1MJ_aWi1DzNLpi1VpcfBwZ20DxLXLwV3Wi6UDvAavGE1PSnGKCGauSZx3O8qHE7h3vZNEawIbWkex5PQ0iv9NvPjFr9BqLTtoT1KECxgkWkHtuyyjqiO8V9nIYdlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f877c2bb.mp4?token=oEpe0RpNdTE3gFjwXNeFH7fLZlxvjdoAyZzy49AaXKMhdcOiP0vuhN1n6yq9EujY9xsChjJvwv3jA7dRpnC48JjqnTWe5kmcU-KUKJLE1ZZ2GbWPCq-H8AsGCNN3fvR1tTwBrnONn2LcHjs4FDbJl7Gb_8pUEvBPtgsVXKn-QyqhrNE2noN8-xtPkla_f2Kj7FDSAQDsX1DZaNJWyHdpSDSl9JDfjM9B3-wUI4XD3sUg_N8KS-IL-Zlz0RZ1liTj-YhsBnqx2ALf7gnFKOUkHBO2Lx1g_l2OTHrEsI4TatMqJDKiyOExEv58fatz5_-_QmhRYYLWkofmXxMt2YPg4JAJyCJWEcWskw2J_lAB11qal_IsvnxRliY5A9jiFZ8NFm45KimXflSgG6gD0-4ZitOFWuHoBbHL4dqE0ApwFHetq0lUjeLCBI9yE04ijtqR4KfJbOg0PRDWPdmR67g5GTSasaj_SUTR3UEQJN45wa72rbub-p2YD4CFNWwCN_rE_L1tKQf6LsHopz-wILGlZqFThKhg0QMRAz0JmlBGACURDY1MJ_aWi1DzNLpi1VpcfBwZ20DxLXLwV3Wi6UDvAavGE1PSnGKCGauSZx3O8qHE7h3vZNEawIbWkex5PQ0iv9NvPjFr9BqLTtoT1KECxgkWkHtuyyjqiO8V9nIYdlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی: «حدود ۶۰ هزار نفر از نیویورکی‌هایی که به ترامپ رأی داده بودند، در این انتخابات به ما رأی دادند.
🔴
در فضای سیاسی امروز، وقتی می‌خواهید درباره کسی قضاوت کنید و او را کنار بگذارید و بگویید: «او به آنها رأی داده، پس دیگر نمی‌توان با او صحبت کرد»… افراد زیادی هستند که فقط به دنبال کسی‌اند که شرایط واقعی زندگی‌شان را تغییر دهد.
🔴
بهتر است وقت خود را صرف گوش دادن به آنها کنید، نه اینکه برایشان سخنرانی و موعظه کنید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150514" target="_blank">📅 09:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150513">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نیروهای یمنی: در سه ساعت گذشته، 20 حمله هوایی علیه مواضع حوثی ها در مناطق مختلف استان تعز انجام دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150513" target="_blank">📅 09:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150512">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
شنیده شدن صدای انفجارهای شدید در ریاض پایتخت عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150512" target="_blank">📅 09:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150511">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فرماندار خارکیف: در ۲۴ ساعت گذشته، حملات روسی به ۱۳ منطقه از استان، ۶ مجروح و خسارات مادی به بار آورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150511" target="_blank">📅 09:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150510">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgexABhoLGp1m-GSZhZ6Ud2FM8nIjKFYrFzbyr_FunzPatFvluzBf1qQc7lmvD9dhBLyIY5Yw2M4ZuZm7fOnEJlUXKkfLHdMyb6uAGj7kiM3R7utkJGGFiUtCpWtQtCJk9ScwEjjpYMR36oeTwaU_XSPGlX7r1Io6z-jinmsC63BQKeg0HHKIZXo6gsKP-rWTO9UqDukiFbkkGqtTd1AEAFyUAtRAelA0GJvwA74aPsx0AAhMqECW07aVQ46uJ3_YhfnphAl1kAKmLETKNOhnOnepIZLgKkkilupDM_yD6OACGfGAEXhwknFKHAzlIQufxdgfHbvbgOwAu0AusLiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان دریانوردی بریتانیا (UKMTO): گزارش‌ها حاکی از آن است که یک نفتکش در تنگه هرمز هدف اصابت یک موشک ناشناس قرار گرفته و دچار آتش‌سوزی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150510" target="_blank">📅 09:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150509">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
آکسیوس: آمریکا دو پاتریوت دیگر برای حفاظت از تأسیسات انرژی به عربستان و قطر فرستاد.
🔴
آمریکا برای حمله به ایران به آسمان عربستان نیاز دارد؛ ریاض بدون حفاظت از تأسیسات نفتی بعید است موافقت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150509" target="_blank">📅 08:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150508">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: ایران در ماه سپتامبر هیچ نفت خامی را در نفتکش‌ها بارگیری نکرد. دولت ترامپ در حال قطع مهم‌ترین منبع درآمد ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150508" target="_blank">📅 08:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150506">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n7sCc5vq7k39F5dpta32uOP6tJRDrxxZHZyENOC_-MAe4saJ_f7E2fI0rY8rZPQE7cR4GSRt0WN8PRbuE_8HuPwDnX-VBtqQ6fKCnFtgCZTrpSqLUpKFS2QjO_EDTYgYtCKoE_x_NpZ1PihJJvMfDHZl607bv1qeJ899hBenTyAylSd3f9G6HHkeQqf9UnIFDrOX0Fvtl3yMZUczM6N6NRJmNVaP_VBD2MCv5fgzPn7C8__w3GxLMPpBN8L1LatU_pK03_t9fDVsKe3MC5MRNcnr18Fp56oyKsID0mjVkeJVtN9PFpm51QiKHZ8_UF8Jm8XNxU8e0Pj7Z7rpipL6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rbO3uPHmDdTBKTD6ITHJuJTEf8EzWj77HjWyhaWAE7MCAv1QxDkagenySX4zqmd0OIO2ULYMmA_pRcIFk5tMU_WAe7JNANAysEUEkF6J_Xl1AacZypu9SG5X3WksC6yj0DNRPNQn38L2yI5mBklj74v7Y12U-zEgInBzTVK2NMhj0lrAotyLreHmaivQvY4EqNSDQzDu29O35VqBQTudFrh4fLuVZgBCvx1ngPaU52eXyqQ_Sz1YHcwzUFZcs1NgHWIg3WrE-XZMmRxbt7AKlrpLKtqXq0C65FHgSZPZ2ypPYhQUH16KXtRjFF2R2pFedaYLxVz_8QEOdhWq-euK-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از حرکت ناو تهاجمی «یو‌اس‌اس ماکین آیلند» به سمت خاورمیانه خبر میدهد!
🔴
تصاویر ماهواره‌ای Sentinel-2 که روز ۲۹ سپتامبر ثبت شده، ناو تهاجمی آبی‌خاکی USS Makin Island (LHD-8) نیروی دریایی آمریکا را در حال حرکت در اقیانوس آرام به سمت خاورمیانه نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/150506" target="_blank">📅 08:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150505">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GbjPMQHVxENkyWwymjliUikm7riMuY6Krqp0emtl_d4P0wDw3QEpDgGILNsvyB2f_HZxf8Czf3w1v6EoxbxmZ_3L_m5KYjFOBVXscJEAJo1Icv_jsxmyNbBHPI1phzSoq6JPSs6yoEnrSSVB9xoN5dl5f4oanAcCO9p5xC_O92RksRC2Ik00qiePX9y4VdQUwt4nBPbYxvf4lBfkTcBOqPkgbpgZCGNMz-0ki-GrMvedGxpTdJ2Db37BykA7EWp8siS8qeLhO6GF693ftCrH8BF2A6CeWr1fQjOu_4d_1EUy1feLD4tMkdC8tQK-Mh37cHCRbgBJPj9lDfpK0hKPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما: همه هنرمندا و خواننده ها دارن برمیگردن به ایران؛
رضا پهلوی
هم میتونه برگرده و به عنوان یه شهروند عادی زندگی کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/150505" target="_blank">📅 08:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150504">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: ایران رادارهای پیشرفته‌ای ندارد و گاهی اوقات سعی می‌کند مین‌های دریایی کار بگذارد، اما ما معمولاً آنها را قبل از اینکه بتوانند مستقر شوند، از بین می‌بریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/150504" target="_blank">📅 07:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150503">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8c69aba0a.mp4?token=am1mqfcQDDFV_OlG-LNz2-8Ur5q0J1mEchj1DTmdmwa7N7YSHQa94rvQJzDEQX3XTN0mfwIs3abtsP8jdjZa_DPCpAK34BoRuivyF90qotkCNforFYrZsf97ahL2fiKVjhpnTTt9YeTOn0buLj-0jNiZHcmgYppd-m6plWNDPqVCs0Cc4tRSuc81vkPwI4Myx2t0hP6yiHbBmf8NGE_lCZYXhTD64v67mCgebrcQHkQHZX4fS5yx-hwe9kjw50-YO5AgDEC6pnsRh-R5j_XziHtff-sHoFoUTmELMw7ta53lBsWuPdBNl47ytqR4susOJERhjhoMZnnEbRNLG8m-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8c69aba0a.mp4?token=am1mqfcQDDFV_OlG-LNz2-8Ur5q0J1mEchj1DTmdmwa7N7YSHQa94rvQJzDEQX3XTN0mfwIs3abtsP8jdjZa_DPCpAK34BoRuivyF90qotkCNforFYrZsf97ahL2fiKVjhpnTTt9YeTOn0buLj-0jNiZHcmgYppd-m6plWNDPqVCs0Cc4tRSuc81vkPwI4Myx2t0hP6yiHbBmf8NGE_lCZYXhTD64v67mCgebrcQHkQHZX4fS5yx-hwe9kjw50-YO5AgDEC6pnsRh-R5j_XziHtff-sHoFoUTmELMw7ta53lBsWuPdBNl47ytqR4susOJERhjhoMZnnEbRNLG8m-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: رهبران و رؤسای‌جمهور ایران دیگر در میان ما نیستند، اما ما تلاش می‌کنیم با فرد فعلی [در رأس حکومت] با ملایمت برخورد کنیم.
🔴
بالاخره یک زمانی باید با یک نفر وارد مذاکره و تعامل شویم، درست است؟
🔴
اما ما نمی‌دانیم پس از رفتن اکثر رهبران ایران، با چه کسی در این کشور طرف هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/150503" target="_blank">📅 07:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150502">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27eb1079ee.mp4?token=KtXJEPGza-zIlLH5-Nat0GCxpyUB_uktgz90pNmpj33cNvzzotmTmv5MTFrfQqEu5bcfYGe16JJk4FvE14H2u_BwbFxsVOwQnhD7EEDgUJkNfekGDOo0OwtkzsDUzFaRq6y_hUKgu0io5pIWdnXrcY1dFrLU_GQ5itqzamYpsha0vlebbM2AWigaI5qIIem09vO47QjKWMB1KTCllCRBejUeE2kM3VCaf8KG9kpYOnDsD58V6r3EymbuXQ0c46gJCLyWqTY1ixkiMXUPvAOBz7Bz8IFdU_WeNl1AUc25Sv0QTzB_8IM_nXA445dVW2CQfWjSMl_psXAABU8ij_wwMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27eb1079ee.mp4?token=KtXJEPGza-zIlLH5-Nat0GCxpyUB_uktgz90pNmpj33cNvzzotmTmv5MTFrfQqEu5bcfYGe16JJk4FvE14H2u_BwbFxsVOwQnhD7EEDgUJkNfekGDOo0OwtkzsDUzFaRq6y_hUKgu0io5pIWdnXrcY1dFrLU_GQ5itqzamYpsha0vlebbM2AWigaI5qIIem09vO47QjKWMB1KTCllCRBejUeE2kM3VCaf8KG9kpYOnDsD58V6r3EymbuXQ0c46gJCLyWqTY1ixkiMXUPvAOBz7Bz8IFdU_WeNl1AUc25Sv0QTzB_8IM_nXA445dVW2CQfWjSMl_psXAABU8ij_wwMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ:
«ایران آماده تسلیم شدن است. ما همین حالا می‌توانیم خیلی راحت پیروز شویم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/150502" target="_blank">📅 07:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150501">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromver2 vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hqg5sNg3n1zHcBW8-unG4xg8dvUBIIrhUCEjb_rikTq-q7tQXfM1YG4eFHrqtAP747aPQUtFBK1wgwi3zfp6n_-wf9Nl90giLh67P89_zJa1FPs3Up8W_5ldKU2RuKpwSg1UcYYCaNUgFBNzlxiNUBZY3OtIE4ntCdDOxwfc8Z2UPUdnaBOUGyDxMdTME47xWUI8Gdh1YXxXapY9N2tIeT-u0MRRczLBZ4UHDRnIC_1Sv8-dWpbm8OJ6qbh7DgZj-hQO8_NCHXdYXrgRzEh3Ur7ktsgeZlM93ogm-9eYB8Q2t2KHBxxf1-TQ3ZoHViTaSj_GoBOugJktfuJo2ESEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط هزار تومان!!
🚀
--------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
قدرتمند ترین سرور ها در جنگ
💥
سرویس های تانلی بدون قطعی
💥
سرعت بی نظیر و IP ثابت
-------------------
💬
تعرفه ها
🔸
سرویس ver2
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود ver2
▫️
تک کاربر — 200,000 تومان
▫️
دو کاربر — 250,000 تومان
▫️
سه کاربر — 300,000 تومان
🔸
سرویس ver2 ویژه
▫️
10 گیگ — 40,000 تومان
▫️
20 گیگ — 80,000 تومان
▫️
30 گیگ — 120,000 تومان
▫️
50 گیگ — 200,000 تومان
▫️
100 گیگ — 350,000 تومان
🔸
سرویس اختصاصی
▫
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 300,000 تومان
▫
100 گیگ — 600,000 تومان
▫
200 گیگ — 1,000,000 تومان</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/150501" target="_blank">📅 01:20 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
