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
<img src="https://cdn4.telesco.pe/file/nFutMZfjMrMT3yVCbXjtQ-e2zPnVYKJKXiy9tVp4mU3NybvMEWqBlNE7-N6ZgEOHYYoeSfjKUAUVA7EeCNzDhXbkLiD_hSqnRIrdFTexqbB772YkSS4C0QSFF4zbt7IcUwCuK3H0QFwuuHfI97nURvzHwe3Ci2u4KLwJmOQUsgd714ZYD9FdVkmQZiLfTphEDtMqBYOm3xNINCtEQ2e5wazvoNxe4qeBgK7W6XFM-zKvIm3HVIitroARjIzFDhNqUKStTIKD_aj7J9apa1K1zIAVjEOsKJDypKpgaXzIW_-peq5FgsP3Y8Z8wA_p4lKGo0nGEntvDR4oob9swOjMCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 22:46:24</div>
<hr>

<div class="tg-post" id="msg-18383">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SBoxxx/18383" target="_blank">📅 22:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18382">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">در ساعات اخیر، ایالات متحده شروع به استقرار مجدد هواپیماهای تانکر سوخت‌رسان در اسرائیل و خاورمیانه کرده است.
— خبرگزاری اسرائیل</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/18382" target="_blank">📅 20:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18381">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">واکنش غریب‌آبادی، معاون وزیر خارجه به تهدید ترامپ به حملات بیشتر:    با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می‌فهمد   کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه در شبکه اجتماعی ایکس نوشت: اظهارات امروز ترامپ،…</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/18381" target="_blank">📅 20:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18380">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">واکنش غریب‌آبادی، معاون وزیر خارجه به تهدید ترامپ به حملات بیشتر:
با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می‌فهمد
کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه در شبکه اجتماعی ایکس نوشت: اظهارات امروز ترامپ، از توهین به ملت ایران تا تهدید به حملات بیشتر، نه نشانه اقتدار، بلکه اعتراف به شکست سیاستی است که سال ها بر زور، تحریم و تهدید بنا شده و نتوانست ملت ایران را به زانو درآورد. با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می فهمد!</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/18380" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18379">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ:  اردوغان، طرفدار پروپاقرص نتانیاهو و اسرائیل نیست.  اما او در آن جنگ دخالت نکرد.  او می‌توانست به راحتی وارد آن جنگ شود، اما به درخواست من، از آن جنگ کناره‌گیری کرد.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/18379" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18378">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ:
اردوغان، طرفدار پروپاقرص نتانیاهو و اسرائیل نیست.
اما او در آن جنگ دخالت نکرد.
او می‌توانست به راحتی وارد آن جنگ شود، اما به درخواست من، از آن جنگ کناره‌گیری کرد.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/18378" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18377">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  به نظر من، جنگ با ایران دوباره آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/18377" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18376">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/18376" target="_blank">📅 20:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18375">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/18375" target="_blank">📅 20:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18374">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/18374" target="_blank">📅 20:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18373">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/18373" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18372">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ درباره ایران:
می‌دانید؟ ممکن است من کشته بشوم.
من هدف شماره یک آن‌ها هستم.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/18372" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18371">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  آنها با نرخ تورم ۳۵۰ درصدی مواجه هستند. زمانی که جنگ آغاز شد، این نرخ ۵ تا ۶ درصد بود.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/18371" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18370">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:
آنها با نرخ تورم ۳۵۰ درصدی مواجه هستند. زمانی که جنگ آغاز شد، این نرخ ۵ تا ۶ درصد بود.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/18370" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18369">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ در آنکارا:
شرکت‌های لاکهید و راین‌متال از همکاری خود برای ساخت سامانه‌های موشکی تاکتیکی ارتش خبر دادند.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/18369" target="_blank">📅 19:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18368">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -   تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/18368" target="_blank">📅 19:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18367">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -
تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/18367" target="_blank">📅 19:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18366">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بر اساس بیانیه روابط عمومی ارتش ۸ نفر از نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در پی حملات بامداد امروز رژیم آمریکا به بندرعباس و بوشهر به شهادت رسیدند.  سروان علی معینی از پایگاه شهید یاسینی بوشهر، ستوانیکم علی مهدی‌زاده، ستوانسوم حامددورای، استواردوم…</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/18366" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18365">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYHVQOxLXAX_Tm3QR6_Qd0DIaSeEROK1tQJcYp04ZpML90zKoCmoCMvyfdJilmd15TmH0MoUswAjq76UWvIzrgdgR5cEKs7IJRYryDR3Y5M0AzBb-DulWvB_-P3dZK-KK112bVYezx3ZgK7EG4-h3jaSM1GGkjrSup02p8EY0p8VIm_VdkkIn8nGPXy2ILrSJKKgGA2rb-_IsKE3fRH4ieqUrOPv9CcezHk1t-kiN6WmhTzYwJe5QQbgFVkTOxNBUKlw_FKZAWdEB0OUmWlzpvV7uV6gQjmMEyegu5xgUt6ssjtabDjtzdvlB1LoTn86JTfDdc_eYR2kaXWFRwKDVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس بیانیه روابط عمومی ارتش ۸ نفر از نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در پی حملات بامداد امروز رژیم آمریکا به بندرعباس و بوشهر به شهادت رسیدند.
سروان علی معینی از پایگاه شهید یاسینی بوشهر، ستوانیکم علی مهدی‌زاده، ستوانسوم حامددورای، استواردوم امیرحسین قاسمی، استواردوم علیرضا زارعی ثانی و استواردوم علیرضا بالیده از پایگاه شهید عبدالکریمی بندرعباس و ناواستواردوم شهاب امیدی بزی و ناوی محمدجواد روانفر از منطقه یکم نیروی دریایی ارتش، در این حملات، به مقام شهادت نایل آمدند.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/18365" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18364">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ درباره احتمال اعزام نیروهای زمینی به ایران:
«چرا باید الان وارد عمل شوم؟ زمانی وارد می‌شوم که یا آن‌ها کاملاً از بین رفته باشند یا توافقی حاصل شده باشد.»</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/18364" target="_blank">📅 18:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18363">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqyS4znHnCzzOIgym0BPjfnKTXTV299sLgScUWM9nbn60GXjdSGALjcG6NYbMlbiCbGQbKJiKLZhKJ7IyI40bLIqyn4PxrrZTOtS3U23tjl3wI521UhKS5GlhG4QhOA7CJ1d7jyawO2A9q8hjsmz37cfoLJ508Fmo_YNMM4DdN0TJKuOu7gnPaIlrI2SmL_bfOOAeG0Kp0OVoslxvQ_2eifGzZMj6RJbATT2O-_uUHJmxtYBtGJBqpRLqNu4frImmApd2rV6OaVpBmr26Rr_KsxAcT3WNknveXdI7SQiS2HdQEokG8ZGsxR17-OSVpah5VBCGiQ7BRdO5PXisNbOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در سطح بسیار بالا قرار دارد و ریسک گریزی آشکاری در بازارهای مالی جریان دارد.</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/18363" target="_blank">📅 18:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18362">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywebm08La6ODIBt7AafPreafvpUsDvTbo7UX-mmPZ2bAyoMoCJM1U_2LjRPafo_e4N_AJgCqDAy51KIYTm8eBWWwiPdW2EA-IwbaL1RVVuq2ofc1QQa-Gw2rMaaEvRPPWhHKFV4vZpcvW2pyvBFkNZaO66mI2hE57kitW1moAhupeEk0l7KnMICLYvoiWEsW9G19fav9rmVg1eZVvJrGzjmwnqiHSOmf12goQ0IBeefluhVZRN4RlDdCiR9N_9QPIflPH_FYkkQrYMTyb00zcqWNVVqRJK2qbG3D6-JqVbpwd1NcMJyaM3W0B9NFTz3CbbNpPOmiO0T8Qa0csTIb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/18362" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18361">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏یک مقام امنیتی بسیار بلندپایه اسرائیلی دقایقی پیش در مصاحبه‌ای اعلام کرد:
«دور بعدی تقابل با ایران، آخرین دور خواهد بود. ما از ابزارهایی استفاده خواهیم کرد که تا به امروز به کار نگرفته‌ایم؛ موضوعی که حکومت ایران برای بقا در برابر آن با دشواری جدی روبرو خواهد شد.»</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/18361" target="_blank">📅 18:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18360">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">— دونالد ترامپ:
«به نظر من، اسرائیل نیروهای خود را از جنوب لبنان خارج خواهد کرد.»</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/18360" target="_blank">📅 18:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18359">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/18359" target="_blank">📅 18:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18358">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ فکر می‌کند اسپانیا عضوی از BRICS است !  در دوره دوم ترامپ، مشاوران و نزدیکان ترامپ قطعا نقش برجسته تری خواهندداشت.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/18358" target="_blank">📅 17:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18357">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ:
جمهوری‌ اسلامی ژاپن دیشب ۱۱ تا موشک به سمت ناو هواپیمابر ما شلیک کرد.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/18357" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18356">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ در مورد ایران:
احتمالاً امشب دوباره به شدت به آن‌ها ضربه خواهم زد.
به آن‌ها یک اخطار کوچک می‌دهم.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18356" target="_blank">📅 16:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18355">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پیروزی های ارتش طفرنمون روس ادامه دارد…
اوکراین می‌گوید امروز یک جنگنده سوخو-۳۵ روسی را در جبهه شرقی سرنگون کرد.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/18355" target="_blank">📅 16:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18354">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7979bdf1.mp4?token=N1VVQUAkzfs0b4ftIn9WgGj32nmYhrhlcDtTznsrViPdIZbYPt5DvI2M5w2jes1evweDfOu1VztTPITq_5c63F2mXzrhmWH2d21-f9RoJYCfkrUcSGlAst9Oxb_wDINZB4WPUxE3Sql4D70Hgg0tkrfABDN3aByCX3K_XP9a7SzA2AkpbUA-qifOfjr0BL_3_6PU-Fc5b8Q7jXYh6keAnyAMVVIKAg6Vr8F2Vye8mU4MNFhXIW15Uc_cNx08JM4I1NQ7Di-uZpGQ1-6TcFcfsU6ndngBLCejf0LIO8tp8kvzA56J1iOMEhHH-hKIH2tPPqcNHWYNVYs1olGX0z7ijQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7979bdf1.mp4?token=N1VVQUAkzfs0b4ftIn9WgGj32nmYhrhlcDtTznsrViPdIZbYPt5DvI2M5w2jes1evweDfOu1VztTPITq_5c63F2mXzrhmWH2d21-f9RoJYCfkrUcSGlAst9Oxb_wDINZB4WPUxE3Sql4D70Hgg0tkrfABDN3aByCX3K_XP9a7SzA2AkpbUA-qifOfjr0BL_3_6PU-Fc5b8Q7jXYh6keAnyAMVVIKAg6Vr8F2Vye8mU4MNFhXIW15Uc_cNx08JM4I1NQ7Di-uZpGQ1-6TcFcfsU6ndngBLCejf0LIO8tp8kvzA56J1iOMEhHH-hKIH2tPPqcNHWYNVYs1olGX0z7ijQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بح بح!  موشهای نیل به دامان طبیعت برگشتند</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18354" target="_blank">📅 14:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18353">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">باور کنید برخی هستند که  مطمئناً این چرندیات امثال شریعتمداری و رسایی را ترجمه می کنند برای ترامپ می فرستند.  شریعتمداری و رسایی اگر هدفشان ترور ترامپ است چرا خودشان اقدام نمی کنند؟!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18353" target="_blank">📅 14:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18352">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9gIbo-TFyd64qPPHqZxlk3oWcPja-BSAkf9BDD9eKp0cWD8B3gTkPjpSKQL_ka650xpJaYju1IGl3rqCw18plF19AsrVUYhYKdmgYFcrOt_QA36UHrV276rP7xSZKK9tPRWMvDi0RhcjAV7vLkMeTPoWRd9rfOjJCIwdwox3eTxvPzINgyWBwm9vMnrUkshTk-W04aNKzgLkKunh_8AHNm9AmoxxaSkUb2HBFIzqQpuxXikpKYhCU71x2vD58ny6K-Slj5-zmpD3ewNhv2IYWj1Lw2J-4Ub12EvHQfnDDJyg-cnQO8gNLbZuAgKOktBNSE2mpeEYHTaOgCtqkxBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:  «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18352" target="_blank">📅 14:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18351">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تا این لحظه،
هیچ منبع معتبری
(از جمله رویترز) خبری درباره
هدف قرار گرفتن نفتکش آمریکایی شورون (Chevron) در دریای سیاه
منتشر نکرده است.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18351" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18350">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvOBW064LWBrKuqd4UV4lFyoGbBIXmuFtspCH0OOtliMLk7Aw-W3jbxxBay4sxysjRg8BF15DsiWldBalJ6mbE0QSBm4C-iEb0DEoTZ645Bao-YDMeW9_XoCr0JcfjPDGY7y5-kws9G6lbrg-KUMQCa8zdJNRI1LZKFNa7fcLLOPz1wVtJd4apaGuSLR2260SizGszOLF8jBQwPzxf0_IdSPnvNu31wbJXcX4vhYYKD03e2VtJayxSJ15AuTtOAl6td6za8Or3asLTkG9faOgfDNCnwSLKi1DTQ4yTsCBxQliPNBXm1_6E4qbRmtsykywzXBtaJCgJja4gyxsjtqVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت برق کویت خبر داد که درپی برخورد ترکش‌های موشک‌های شلیک‌شده به‌سوی این کشور، تعدادی از خطوط انتقال برق آسیب دیده و از مدار خارج شده‌اند</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18350" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18349">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزارت برق کویت خبر داد که درپی برخورد ترکش‌های موشک‌های شلیک‌شده به‌سوی این کشور، تعدادی از خطوط انتقال برق آسیب دیده و از مدار خارج شده‌اند</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18349" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18348">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca74a7b8d5.mp4?token=OLp_kwqqHDeusqQqZD5N36n3TBPsqF8brcU7kZ9NbwzYpb0279EE30arYMA2hqBol6WYg6RxAryWc8CaHj_Qnz-cwmDzm9yarESDfllHry7BScb9BWgpeKngkwwKVBNZBGu6yA5o-SRLg5iyyG9Izjs5jRIY8lJTlsSJHka3dUygeoRKZwDYH8-q6cTA6z-P210qcOgBW15fcWEKwBh2Bj5WeHJh_yj-qFxGDQt3hjuxEIJUjxAU3iW1cn7ItuCHm_4mIwXArFFptUmYPbKHrDgxopDfKTW6-KM_4EKqixa-5BYQsT_Pz7BqQBV0XLMHkVVmBzStvW1AxglWezynfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca74a7b8d5.mp4?token=OLp_kwqqHDeusqQqZD5N36n3TBPsqF8brcU7kZ9NbwzYpb0279EE30arYMA2hqBol6WYg6RxAryWc8CaHj_Qnz-cwmDzm9yarESDfllHry7BScb9BWgpeKngkwwKVBNZBGu6yA5o-SRLg5iyyG9Izjs5jRIY8lJTlsSJHka3dUygeoRKZwDYH8-q6cTA6z-P210qcOgBW15fcWEKwBh2Bj5WeHJh_yj-qFxGDQt3hjuxEIJUjxAU3iW1cn7ItuCHm_4mIwXArFFptUmYPbKHrDgxopDfKTW6-KM_4EKqixa-5BYQsT_Pz7BqQBV0XLMHkVVmBzStvW1AxglWezynfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18348" target="_blank">📅 14:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18347">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عراقچی را در ایران فحش می دادند در عراق بشدت بزرگ داشتند!
فکر کنم عراقی ها چون دیده اند فامیلش عراقچی است فکر کرده اند ولی خب.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18347" target="_blank">📅 13:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18346">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ:
«ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18346" target="_blank">📅 13:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18345">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان درباره تن ماهی پرسیده بودند؛
به نظرم زود است و می توانید از مرداد هر هفته پله ای بخرید.
تصور می کنم هنوز ذخایر نفتی آمریکا پر نشده و انبارهای مهماتشان هم.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18345" target="_blank">📅 13:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18344">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فوری | اردوغان: موضع قاطع ترامپ در مورد تلاش‌ها برای دستیابی به توافق با ایران قابل تحسین است.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18344" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18343">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ :   تفاهم تمام شد، نمیخواهم تعاملی کنم</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18343" target="_blank">📅 12:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18342">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKNDzJLcIBtU2Zq8z6NLsKyNjr7rShIRdFYMMHuKFjxu2X4J8S1J7MC2RVvWEEGMLSHiyRhNNMFraz1s5FKFICjSNQ7xl3Cdk-22hTByNeASGhhrVvpW3LIYnw-Wl4MsT7w5NQf1jpJ0sfEvK6KN3LV5Ma7Sh87cvA7PZIPtdx9Tavu6YbVUVFrG0tOO8mY90BZznNW239113PysgNqmjv-o6SZiZ1UcOi_Zic5avrDEMcRKBAdztANaAL3ekDl1rO3ErsSzodNtvd0mQp4OAHGe9IoZ4hJew0lcd9Rw64Dl5Y24-iL_vjTciEMIANcqs-nOHTEcrldSAieKW9jzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جولانی به آنکارا، ترکیه، سفر کرد تا در اجلاس 36ام ناتو شرکت کند.  قرار است او با ترامپ دیدار کند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18342" target="_blank">📅 12:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18341">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18341" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18340">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO1YKH_VHAvuuXPrGEhPpaCEKylG8dXuqXUlIWVuve-I3M0_XoJMPeG9RUipvP22CxvF20M5pQveTCDzrUsoygcgNpGkn8e81CXF6JWV6TVVOBAvuS7qDPHtnNKyTRb5n2LdEx6iEymykdGhGPsf3k4nzr3A8pdanC-u7fg_zT3T83wfmGOV9dEjXXyz2UBQPhGjjmrv5Np-0T0_TEBzw-NifCgmmb7LGDZmSEp33pykIoiVO8LakwKjb-unzwr1dNlJrhfefMMHScEk9MXM6L0qx_WvIoYlLPKU71qEqOme9wrjZy0chIWxArOefo2IuqRpZZFavQFnoj8HrAdVZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پهپاد آمریکایی توسط پدافند ایران سرنگون شد.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18340" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18339">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وقتی در اجلاس ناتو در ترکیه این چنین صحبت می‌کند یعنی یا به من کمک میکنید یا گور پدر همه تان !</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18339" target="_blank">📅 12:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18338">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ:   با اسپانیا حتی صحبت نکنید. آنها کاملاً ناامیدکننده هستند.  آنها آدم‌های بدی هستند.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/18338" target="_blank">📅 12:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18337">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید  همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18337" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18336">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این خبر از دید من مهم است و می‌تواند منجر به ورود باند جولانی به لبنان بشود</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18336" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18335">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:  آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.  شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18335" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18334">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFiEVzqyzVLXp_7O_3pd5NeYh1M8tfcxNg7hYyd7zPnZNLv6UdvidThEULXN1ibUVI7ursiiqwGEDsHTYn-S3sSnu2pduVF8Liys8IWVoOGPMh0yK52MMqC0i33OT2dOfxSV5RbQPusreQiBYW_-akCDx-9QkrDxZMOniwiOhpY0e2V29WXK-PfsjTmBk2o5KnklgYo7qw5Yaubq-cB11H9MNbiuUhKNYsoJgYFdn-77R3DSkLH2HyvrcGGsty-uzkWIv738RGA5Xo7Yij_ombSqxcyKjgZBi8oCh-ffsTpZptUfZoX9QSctgZLqs5MU_tOjIdLVdp3RMjXRuSDASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در سطح بسیار بالا قرار دارد و ریسک گریزی آشکاری در بازارهای مالی جریان دارد.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/18334" target="_blank">📅 12:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18333">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ درباره اردوغان:
به نظر من، اردوغان هم از ایران خوشش نمی‌آید.
اردوغان شخصاً فردی عاقل است، و به نظر می‌رسد که ایرانی‌ها رفتارهای غیرمنطقی از خود نشان می‌دهند.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18333" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18332">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:  آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.  شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/18332" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18331">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:
آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.
شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟ چون آنها نمی‌توانند قدرت را به دست بگیرند، زیرا کشته شده‌اند.
آنها آنها را کشتند. هیچ‌کس نمی‌تواند قدرت را به دست بگیرد، زیرا آنها سلاحی ندارند، در حالی که طرف مقابل مسلسل دارد. و سپس آنها به کشتار ادامه می‌دهند. رسانه‌ها این موضوع را پوشش نمی‌دهند.
من به مذاکره‌کنندگان عالی‌رتبه‌مان اجازه خواهم داد که در صورت تمایل به صحبت ادامه دهند، اما من این موضوع را بعید می‌دانم.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18331" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18330">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ :
تفاهم تمام شد، نمیخواهم تعاملی کنم</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/18330" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18329">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مواضع جدید ترامپ درباره ایران:  «آنها یک مشت آشغال هستند. من اصلاً از آنها خوشم نمی‌آید. ما وقت زیادی را با آنها تلف کرده‌ایم. آنها بی‌کفایت هستند. ما فقط باید کار خودمان را بکنیم. آنها می‌خواهند رهبر ایالات متحده - من - را از بین ببرند. من سال‌هاست که نفر…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18329" target="_blank">📅 11:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مواضع جدید ترامپ درباره ایران:
«آنها یک مشت آشغال هستند. من اصلاً از آنها خوشم نمی‌آید. ما وقت زیادی را با آنها تلف کرده‌ایم. آنها بی‌کفایت هستند. ما فقط باید کار خودمان را بکنیم. آنها می‌خواهند رهبر ایالات متحده - من - را از بین ببرند. من سال‌هاست که نفر اول فهرست آنها هستم. ما باید سرطان را زود از بین ببریم. من اینطور احساس می‌کنم.»</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18328" target="_blank">📅 11:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18327">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">️خبرنگار:واکنش شما به حملات اخیر آمریکا به ایران چیست؟
مارک روت، رییس ناتو:به نظر من، این اقدام کاملا ضروری بود. ایران، آتش‌بس را نقض می‌کند</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/18327" target="_blank">📅 11:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صدای انفجارات در بوشهر</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18326" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18325">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سپاه پاسداران در پاسخ به حمله آمریکا، یک حمله هماهنگ موشکی و پهپادی به ۸۵ هدف نظامی ایالات متحده از جمله ناوگان پنجم، پایگاه هوایی علی الصالح در کویت و بندر سلمان انجام داد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18325" target="_blank">📅 10:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18324">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18324" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18323">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chTs4s7jjkVwGzc0mRxkfo33gtuubuBFQlWmq2RIqcVs06xA_jO8RLwi1JzRFUabLnCPqRwwA117oAcYLET9Pu5N9Sdkskl_2XjQ_6gQvuTP3zOV46BuZ8QqWihp6XIVEs5Ejr1iJ7otNyyYM1ogzWjAu_P4QFy8sQkLIgIRgbs9b8E3abwQpMJh-wtQkHhLsqdWc3iuuKTr5oURWB3tnYMNJ1L3BPjK0Ra-ix1Q2tLKTcgh1YYBaz-3C_NXRlktbtPFo4fuN60H3zkPZa3wTfJQH1T6h6HAqJnUUZSWOS8k63CBj5wVxp9I1njc3m99waqg03DyTQwfeUOhh1Rh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18323" target="_blank">📅 10:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18322">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">CNN:
وزیر دفاع ایالات متحده پیتر هگستت‌ در روز سه شنبه سفر اول خود را به اسرائیل انجام خواهدداد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18322" target="_blank">📅 02:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18321">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M39h7fW4tY48QVWW9wpg3hs8y7LPvmHEppTIrDgs2mj_gOdhQUvPVhPNG0R14phqC75wDlJUbcw2d0MX1m0NcIonaX4BhZIWVBmz3EfWRiFB275ckzhxPy8yW7zxqCChq83AkMApFXuC2V2VG_PTb707CklN4GjgiY9C9YTIr3sgwraTylT6ROZA6yGM9FCs3nShmgDsC3X-coJXDdM5eGMy2n8TaXhLOtG37ow5q-wJA7KNIyYVaDf7jg7mXikYS_WzP6CC4JLPF_GeClZiVD-6fZcqm6Kw9__iMO3UAvYVB9NMFVnonFS3GtrnKfApf8w_h3mww2N6aFs9Kg7-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی گفته بود حالا که ترامپ در ترکیه است او را ترور کنیم! ترامپ هم از همان ترکیه دستور حملات را صادر کرد!  ایشان را بیدار کنید خودش برود دکل سیریک را نگه دارد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18321" target="_blank">📅 01:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18320">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حملات ناوهای جنگی آمریکا در ایران، اهدافی مانند سامانه‌های پدافند هوایی، سیستم‌های نظارتی ساحلی، موشک‌های زمین به هوا، موشک‌های کروز ضدکشتی و محل‌های پرتاب پهپادها را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18320" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18319">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مقام آمریکایی به CNN :
حملات به ایران برای تنبیه‌ست!
نه مقابله‌به‌مثل؛ و این حملات فعلاً ادامه خواهد داشت.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18319" target="_blank">📅 01:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18318">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNOYUSLqlSClSzveqpbmxLNlwhwzC929iWczbdOVFBuyrDvnl2e31MfeoFNUEkTmA5BsqmxnuKNqmnG1Ysx-1zkJ-z5S8n-PSbvXimEi1lB2EhX8xtrr9SvEbRcZbMyC5onfeFxIRDhseJceoy3Aac-9QJmfPM6-8h9b031sNIAPmiFlETArqiNPPt6ref8a6p6pB0gANPBqTxI88exRVdNcCoOxKA-QajS0SJ8v5irLGtXQWjyY2YN6BCSstbEobIepyszSVCRDbnRViXLfaJ10ialNW5_DlijKa6LBiZzKVUX2f5IXNRpMdXQvKbN7btgcIOb9FeIv7Tx17UQ1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18318" target="_blank">📅 01:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18317">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782b3ef401.mp4?token=BUO170QQcb4DscjLuSH9xqTJxXCnzn4TzPs8hrTF1P1JyA3g8pVecFeSegC2lQamuJzaRkstphqFZ3F4Cm8SynKi_4wTC9hCwLGBzqpZ6jFagq6_PygL_ZnTCcZrESrWF-Lwb6NYJ-5CTVkijLVl-jyRKGMKP0LOUpGVMrbWebZ9pBdEcSnJ-RVCwPCQYUxcW12EdZRM9h7X2WewnNp6iJaFvMAxGKxroVag6-ptvG2ZBBK2PT-JFZ4cE95DQqJgJxQf5PlDGAxYhFl96ebxL0tB2Ncbz2btvrnnYsQBGkvCYVuIpjLB1GeGVvI10BuxWnwNHJXFkRqpiwEjh3akWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782b3ef401.mp4?token=BUO170QQcb4DscjLuSH9xqTJxXCnzn4TzPs8hrTF1P1JyA3g8pVecFeSegC2lQamuJzaRkstphqFZ3F4Cm8SynKi_4wTC9hCwLGBzqpZ6jFagq6_PygL_ZnTCcZrESrWF-Lwb6NYJ-5CTVkijLVl-jyRKGMKP0LOUpGVMrbWebZ9pBdEcSnJ-RVCwPCQYUxcW12EdZRM9h7X2WewnNp6iJaFvMAxGKxroVag6-ptvG2ZBBK2PT-JFZ4cE95DQqJgJxQf5PlDGAxYhFl96ebxL0tB2Ncbz2btvrnnYsQBGkvCYVuIpjLB1GeGVvI10BuxWnwNHJXFkRqpiwEjh3akWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی انفجارات پیاپی در بندرعباس!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18317" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18316">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نفت را بای داریم پدرسگ ها</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18316" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18315">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18315" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18314">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18314" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18311">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رسایی گفته بود حالا که ترامپ در ترکیه است او را ترور کنیم! ترامپ هم از همان ترکیه دستور حملات را صادر کرد!
ایشان را بیدار کنید خودش برود دکل سیریک را نگه دارد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18311" target="_blank">📅 01:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18310">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu3yRNrdVxRmsSrnq3fFsNpKEGYxmvq4CebDQ0vrgychGvbcT0jKV6HDPZ4Ilx-IvhfIfcHp2isUBRls7MccpIoGdg7E00Pz0Hsk3-vAM9WO3j4rS2ANKX3oDyh3hSlHxoxFhaE0_rULDww1JYkrJNJsY3lp0PWg9nV0E7HWRPMTICLJTYnkzMWjX2iSK5MBbeHaWVVAr4FBldmutT0kHgQ6AqM2mmEj_BkHqS6KMc62JUAmAbttnjkB0ScecwACQiUmZnqYznKAEe9bMItl0RwJSxGEZWcRc0MLoJ3f_9b_Flk-aPfaWSZQyBHsx8xIwAFNVrNJ2EL38MzwB2BVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه دکل سگ جانی است خدا میداند</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18310" target="_blank">📅 01:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18309">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbw6nsNb225r5axf_YCVMB03Gn5yI1RQrzlb7207TAr_fNZIqFIoTnYibj17iipby8VnBcYGSeB48zKm37MWyLxQdu8l0ZvBGrVCf_-jtsgmOJLCKhAQNp7e_dGQg-65Qzyp4upuuJvyL_dkmLG1wXjdZOBaieu2VpjOSJMfQFA79nYHezr61ZdQAhWm-F4HtzIK7g-qnEVEVYDW4YMzJAY0VmGM8BbdKVzXx3iWtcVkt60wBMiLs8PVvvGrbjyjlHeE_FDr44gKhIyFA5OFViT2EkZ-_4Q6bPSyTQzRCOt6mgW1UCwg7VjzF7xht7hjv4uVfGa-tVTieMAslQdi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویری از انفجار در پایگاه دریایی سپاه</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18309" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18308">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">باز  هم اشتباه محاسباتی منتهی باز هم از طرف ما!  بارها دیده اند ترامپ اساساً اهل محاسبات نرمال و عرف پذیرفته شده و اجماع-محور نیست باز خریت او را تست می کنند.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18308" target="_blank">📅 01:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18307">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">باز  هم اشتباه محاسباتی منتهی باز هم از طرف ما!
بارها دیده اند ترامپ اساساً اهل محاسبات نرمال و عرف پذیرفته شده و اجماع-محور نیست باز خریت او را تست می کنند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18307" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18306">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اژدهای بندر را بیاورید ببینیم منشا صدا کجاست</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18306" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18305">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گویا ارتش آمریکا اشتباهی یک هواپیمای پاکستان را زده و سقوط کرده است</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18305" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18304">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سنتکام می‌گوید ایالات متحده پس از حمله ایران به سه کشتی تجاری در تنگه هرمز، حملات گسترده‌ای را علیه ایران انجام داد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18304" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18303">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">منابع محلی گزارش دادند که آمریکا به یک دکل مخابراتی در محدوده سیریک حمله کرده است</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18303" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18302">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18302" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18301">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسراییل هم شرایط را مناسب دیده و شروع به پیشروی با زرهی در جنوب لبنان زیر پوشش آتش هوایی کرده</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18301" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18300">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18300" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18299">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.
فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.
سپاس</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18299" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18298">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آن 2 بند اول هم که از هنوز از تنبان توافق گشوده نشده صرفاً در برابر بازگشایی تنگه هرمز بوده.   به زبان ساده تر، یعنی ایران تنگه هرمز را بست که از کله زرد امتیاز بگیرد، اما او یک محاصره دریایی در پاسخ اجرا کرد. حالا ایران امتیازاتی را که می خواست نگرفته اما…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18298" target="_blank">📅 23:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18297">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دکتر محسن رضایی:   کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18297" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18296">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دکتر محسن رضایی:
کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18296" target="_blank">📅 23:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18295">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر خارجه ایران:   کشتی‌های تجاری که مسیرهای هماهنگ‌نشده‌ای با ایران دارند یا دستکاری ردیابی کشتی را انجام می‌دهند، با خطرات مواجه شده و تلاش‌های ایران برای تسهیل عبور ایمن از تنگه هرمز را مختل می‌کنند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18295" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18294">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یکی از این تعهدات  این است که کشتی هایی را که از مسیر عمان میگذرند میزنیم تا بفهمند مسیر جنوبی ناامن است و از سمت ما رد شوند</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18294" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18293">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر خارجه ایران: ایران در حال انجام تعهدات خود بر اساس تفاهم‌نامه در مورد اقدامات لازم برای مدیریت تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18293" target="_blank">📅 22:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18292">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18292" target="_blank">📅 22:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18291">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18291" target="_blank">📅 22:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18290">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایالات متحده مجوز فروش نفت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18290" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRed Lion Corps(M)</strong></div>
<div class="tg-text">بازی فوتبال تیم مصر و آرژانتین، چیزی تو مایه های جنگ یوم کیپور برای مصری ها شد. کمی اولش داشت خوش می‌گذشت بهشان که زمین و زمان بهم ریخت</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18289" target="_blank">📅 21:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بح بح!
موشهای نیل به دامان طبیعت برگشتند</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18288" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرنگار سی‌ان‌ان:
«ترامپ در حال بررسی دادن اف-۳۵ به ترکیه است».
نتانیاهو
:
«این تعادل قدرت در خاورمیانه را نابود می‌کند. من این کار را نمی‌کردم».</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18287" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18286">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18286" target="_blank">📅 20:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18285">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امروز پوتین با لباس نظامی با رسانه ها گفتگو کرده و عملاً می خواهد از اعتبار و جایگاه خود دفاع کند.  حس خوبی ندارم....</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18285" target="_blank">📅 20:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18284">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb88acd05.mp4?token=KIw_aktGL2M4be-JRTlnrwuNZerd10-tbo_gv42bJMB3WuBGCoqHrEPoZN7dNnFH_lDgea3tzJoWkSubBOZvrGx1a5G4yoAgx-OwSJwb92bGsbye_aLflqeGqCKx14sXduiIBGav1BnLDPULA12RrC0lsjaQWjAnGMbulS9e8Hqs373MROGLfRjDPA-m_GoWc2zXnIKrAFEiImBgvr-ozrCAPo8ANvanl9Ti1iyoBsOwvHWojHIBjzc0qBznT7KDZyd0JfageC8EK45lHAcqxRi3MOs8d_TZDOT-hqwwivCudRY3B-oQv2itvoiKJzl1rdeJsNmiujU-rngStG_LGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb88acd05.mp4?token=KIw_aktGL2M4be-JRTlnrwuNZerd10-tbo_gv42bJMB3WuBGCoqHrEPoZN7dNnFH_lDgea3tzJoWkSubBOZvrGx1a5G4yoAgx-OwSJwb92bGsbye_aLflqeGqCKx14sXduiIBGav1BnLDPULA12RrC0lsjaQWjAnGMbulS9e8Hqs373MROGLfRjDPA-m_GoWc2zXnIKrAFEiImBgvr-ozrCAPo8ANvanl9Ti1iyoBsOwvHWojHIBjzc0qBznT7KDZyd0JfageC8EK45lHAcqxRi3MOs8d_TZDOT-hqwwivCudRY3B-oQv2itvoiKJzl1rdeJsNmiujU-rngStG_LGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک تروریست و یک شیفته تروریست در حال امردبازی</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18284" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18283">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دبیرکل ناتو در مورد ترامپ:  من از این مرد خوشم می‌آید.  به نظرم کاری که او برای ناتو انجام می‌دهد خبری عالی است زیرا، بله، یک تهدید روسی وجود دارد، اوکراین وجود دارد، بنابراین ما در هر صورت مجبور بودیم در اروپا گامی برداریم.  اما او چیزی بود که برای ایجاد…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18283" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18282">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">روته، نماینده ناتو در آنکارا:  ما روز سه‌شنبه در مجمع صنایع دفاعی، ده‌ها میلیارد دلار قرارداد جدید را اعلام خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18282" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
