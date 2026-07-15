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
<img src="https://cdn4.telesco.pe/file/bFnBQThKdsOYoX-fQ0ytNgyiy953ap99a7UEb2jJs2jQAL2p92ItCLrttPhsR6BWDdFyAdfAWeQNO21LedwX4V2ZllbnUWks8xVeHnCT1H4sLBW_lteinROWdxnFHDuU3B7lgXnAwr011kd6Hxl8Rgfmo6YiTx1fL1oCY0MaDP2FnJIeudDuZ2zSFJlpeW_9nxpcCN5lvageOk1SONR9Sc-uycICU1BMPum7izDFloFjGQqAI-50UYLz2M2qdGI-VpAB2XjzvixNXvxgmDTLp31gRAomm7x490UJx2diuOSuUY6I3EyKoyBrLnSd3WAhLoszFyvl2q-O79Z0HJkDBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 19:43:38</div>
<hr>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=KI23fjmS7QC8Q0wwOq0U6hHbxdtEx9bJKH_PRSWrpoprjeXqQm0vPcC4NwskZyavc-W8oHvAveBx0rbUYjbfX1AOSJ3fofdkqe_TpFgg1LxmFEgIC8QF00rz6SD26f5nlQqiBd8O9pb0FXvSKnmMOVmzX_rsuL-VdieY7LCy2Sthncmu88krStuvdUf_ds0Uq_CQM3TUxf_lKxAEjYJPe_5dBfcRnDwiWbGYTn3UduIoGsxIIqqYc4r07cPTyUjzYc3fwVEALVe24eZJ_oqEga2y9U4iG9C9fAP-wvVZ3WiTNQBQszSSfqF8T-aK_sFnxLucVXeVhFgbLUYphnLRHIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=KI23fjmS7QC8Q0wwOq0U6hHbxdtEx9bJKH_PRSWrpoprjeXqQm0vPcC4NwskZyavc-W8oHvAveBx0rbUYjbfX1AOSJ3fofdkqe_TpFgg1LxmFEgIC8QF00rz6SD26f5nlQqiBd8O9pb0FXvSKnmMOVmzX_rsuL-VdieY7LCy2Sthncmu88krStuvdUf_ds0Uq_CQM3TUxf_lKxAEjYJPe_5dBfcRnDwiWbGYTn3UduIoGsxIIqqYc4r07cPTyUjzYc3fwVEALVe24eZJ_oqEga2y9U4iG9C9fAP-wvVZ3WiTNQBQszSSfqF8T-aK_sFnxLucVXeVhFgbLUYphnLRHIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMaQb5iODscw4fSyTOQdYljwmSq8rOB0_KAkwAchCMUFELaKeu4sj2KIXvJBFcRO4jNO8nUz3mTxGuIRtlxHW2iNPPHzcvK5NbahsSBhiEj-Vv0PpUhQEmmun5EvhkG76A_N5A-qWRedbWmSkO1N6MDiboi6lwv7pphKVxaReHNnkeVF7yle3iDu4P1Pzt01ET7NdRk1nEBY6F8695jmJPeqtIzVZmRpw1Mvs-BzCpTgFU4S1cTykIkmkdFole4o7Wnwfa4tk0AQ0ve4V-Ov72-_Qhxzhi6J_F1Ww6Idb_8mOPZhI8RUrOBih_R3kbWvs1PVp74zumT2Yfh4MaHGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Iv9tJny44ivgS_gX_qjDCSLi19XS9wCTNDSvuFe6H2k2A_347P1efYGNCE8-4wbLd3IjaZ8ceOxhvqUQGus5t5WmlZiwFWeqRBFKi1AjRJOxu_SeZ7pegvA8JaOqUaECK6nBmQeu_0v8KBl_oRzg2xOxO3OHOVv17cTNpkGdYwc0LQVqn5TCZtuRKoGcsw3wTOAwgFHVUcvCleQyrsoh00ynq3YnTnod1wkcLVk3IdJdI537Tgp5wrIaSizOkLaJFFnvg6yLlq3SfG-JPhI0SYrF-n308KOSOLZj_Px0J-MjFqZrhmCi0hwpjUZvSPRyjrPhrKBnpHoVxaVwPtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bZSRQN0_-i1IBfNceXCS3m1cslXegyECZ2VqCPfX5HY4t8EeTiKbDG5i_DHiThRcEUiPYYh5mUj9CtT4XiXAzEdkC4LOap6MvoCzpFU7lYMeURcoV43bVXdvvHTOWoswQlgx5n_lnYUpwgLMKet_qFdp8bc_pUuuuqfXLqCtAW6sU5lsIPlmtm0Veg0s21w0qQESmU3pYCIbiFCpCnIJREFT1k3J8SeIwEIhkk_M-qgsmuOt4Ol1NAjA5JM44gE2xcMNcy4LWNIz2LkCYzj9Gg3hGuW5GujQjQRTD8dWuoXJLDznwj8t0_Kan0IQc7b61u2Z70x0zV37-5pWrnsxOQetezIhK-WZaojfmaSGX1PXJRQrhn9f10lSzthamRfYE6c0BxLmcS36b-CJc6f7u7dApHvaWBMxs-NsYRW_PezkWyYFuoTgIaC_AvomAZJWs3FGsMzlDoNAVMKp1TQuiYkYodaVPRUxV6ONhENiIZoKdMtSZgKMKOGvvYL1ndV_0BM6A47fVS5YiPLwtxXwT6hiiNdY6uTB9X012Zt8-CoYXxBUzJFrDRf3geH4mrkTAOTuwjC1ZVER4UnJmjSzIoFu2TDhiohWLcUhqO-2Sl33nSOG0m-oeOJuWWU72nO7fWs87nGvP6DW2Sn7Rbag-FhNhN3kYj06W_p6Irv8igg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bZSRQN0_-i1IBfNceXCS3m1cslXegyECZ2VqCPfX5HY4t8EeTiKbDG5i_DHiThRcEUiPYYh5mUj9CtT4XiXAzEdkC4LOap6MvoCzpFU7lYMeURcoV43bVXdvvHTOWoswQlgx5n_lnYUpwgLMKet_qFdp8bc_pUuuuqfXLqCtAW6sU5lsIPlmtm0Veg0s21w0qQESmU3pYCIbiFCpCnIJREFT1k3J8SeIwEIhkk_M-qgsmuOt4Ol1NAjA5JM44gE2xcMNcy4LWNIz2LkCYzj9Gg3hGuW5GujQjQRTD8dWuoXJLDznwj8t0_Kan0IQc7b61u2Z70x0zV37-5pWrnsxOQetezIhK-WZaojfmaSGX1PXJRQrhn9f10lSzthamRfYE6c0BxLmcS36b-CJc6f7u7dApHvaWBMxs-NsYRW_PezkWyYFuoTgIaC_AvomAZJWs3FGsMzlDoNAVMKp1TQuiYkYodaVPRUxV6ONhENiIZoKdMtSZgKMKOGvvYL1ndV_0BM6A47fVS5YiPLwtxXwT6hiiNdY6uTB9X012Zt8-CoYXxBUzJFrDRf3geH4mrkTAOTuwjC1ZVER4UnJmjSzIoFu2TDhiohWLcUhqO-2Sl33nSOG0m-oeOJuWWU72nO7fWs87nGvP6DW2Sn7Rbag-FhNhN3kYj06W_p6Irv8igg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd3yTUNjUOWKdAe59-Yx4yY48MA6mLKAnx56xVdFzJfZj-SJgRA9gDIa3I__7HypgYOO9Zd9-ucfYhaI-U3YPDuDOESL_lcpFvkFvF35hYXBJNzNdeWMg5lWCsyvggI7OHojJNWxJkM8hBYY9XgnrzACqG9I4Pw_qfNlnmwI8VLIDqHBzkeogvkCYVFn7CY40Ohy9fHcrmON6NWXkOrFVQttiNCTnsyZ7DDnO3YaHjmLUPsekRD7GhuwOKX5rOExEEctZ-n8JTmNItZqWJ_T7PK-OvHcXEy7Um6ypO-t110Wppmz4Lb3FRKomj6dDsCgY8s4b_NLMYvriugQvqh3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcCyQG41YszjXc6zE-HIRQFIHIAlVAN4ecqLm255KzmGmUU35FssMsPaqF4SlavnYeuF4lBVN6SbpZjkqubX9DaEHox4LRor6HGqOkptQAq2DfqGYnKicxsdaibEQ0YoqMXFudle4DknVYdOb4o8wrwKPkjfxSg9nOjbby7yaVrv-hNdnoQmkCoVqSlajw1w93TnByOv8dwHiAr-CfTaaBklVkdS94okxA30iCOwJA-yS9960I20Jr7Dse-o3Rcirki_zLirQvq-HB057n7riwbt9RwkIO9IUcrv4703H1MzHeqa0CzS9smd8TZlS5Wvo015u_kImpJMtjgcXVHibe_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcCyQG41YszjXc6zE-HIRQFIHIAlVAN4ecqLm255KzmGmUU35FssMsPaqF4SlavnYeuF4lBVN6SbpZjkqubX9DaEHox4LRor6HGqOkptQAq2DfqGYnKicxsdaibEQ0YoqMXFudle4DknVYdOb4o8wrwKPkjfxSg9nOjbby7yaVrv-hNdnoQmkCoVqSlajw1w93TnByOv8dwHiAr-CfTaaBklVkdS94okxA30iCOwJA-yS9960I20Jr7Dse-o3Rcirki_zLirQvq-HB057n7riwbt9RwkIO9IUcrv4703H1MzHeqa0CzS9smd8TZlS5Wvo015u_kImpJMtjgcXVHibe_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=KIZqWIToUzGnJhKmw4nD0sMVeY1f0oEQh5JIY1nLqY3231xQTzZeoxpkmTEaY123tsKh_cog2q3fUO4LPPbwkibGd9q_tR2tq0SjC_86WqRtMgEMmT8WeuWX3c1FqOQvZuc4IqwY-eIMFI0Yoy5b3LZVrPCkP5Xm9bYr5cWzrc9Lg6UoHYYlcs-UUA3xWVDQZmeDaWeiZlDKXpTpbfQy0Nv2feRsFx0un2Vrn_35qXjDRiaHElNVTJHGmWULPaj8xp0Dd9B051W4F_UysTDcd5xETlmE-ZHnLzzhnXry5DYKJHO-Up4dwFGGkhQnJjpdOGu8_n3VPyrxs3Fu1ZFCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=KIZqWIToUzGnJhKmw4nD0sMVeY1f0oEQh5JIY1nLqY3231xQTzZeoxpkmTEaY123tsKh_cog2q3fUO4LPPbwkibGd9q_tR2tq0SjC_86WqRtMgEMmT8WeuWX3c1FqOQvZuc4IqwY-eIMFI0Yoy5b3LZVrPCkP5Xm9bYr5cWzrc9Lg6UoHYYlcs-UUA3xWVDQZmeDaWeiZlDKXpTpbfQy0Nv2feRsFx0un2Vrn_35qXjDRiaHElNVTJHGmWULPaj8xp0Dd9B051W4F_UysTDcd5xETlmE-ZHnLzzhnXry5DYKJHO-Up4dwFGGkhQnJjpdOGu8_n3VPyrxs3Fu1ZFCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uukUbxq61Kc79KDOGiiAtbEmFRYZw5TL4_2BBsuM1eIVLrPUetfbacuT6ldWCpehbdl5_2EDMCO-NZYpDIN7M19sMs6Q315cushn4qcTCtAbnlw0SaRCgcmFP-Q0pRx2IzxQpYyiN0FtxNtcPslSvFVCQE2xuBjxczkY3R0cA1PC1DvOkWH1Uqv4ZvAdkvvF7YmZbAtPNVffIuYX5kOtmB1acRZLXfkQEL4RVNsIQ4Nfq9tF7kwKa30JTOS9TjHoD_Yh_S8_1yV1H-cWWPgEJRKETn1TysLIyE5ZAs9Hydnrlf-XtiIp2ectbTCS6zh6n4tF2ulfvlnB8N8dUVJVrij3gLkCIuHwzaSLrZRRgKiWtOm2WifkC7uaLX-AxWJ_V4oi-tND-NlKRxoNoBpaYj5iRb14uJ0W_Xa6bFvSwiFihlandHb7LLsJKEbnEUvVqUg3okPPVqOwdCHuO-99cbvtVyJXl9K8H5gQAxm1HZBIII_jh6lftfxk7bab6FpS7a4x-zT89_Dn0sYa2_k1Sknkw0BvhsIiwVZWEsPRwN7LtvKMYIKu3Trx0OklwXIqkXd6UYwXjBMJR-d2zIz9iKl_VFDJxQ7B8_RGDB40b4ZLjb0-XfTdrduFlkvb79TUQC0mQFIQ2vOt3fb9QHIFuBWaigFWo5bHSJSENFIvar0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=uukUbxq61Kc79KDOGiiAtbEmFRYZw5TL4_2BBsuM1eIVLrPUetfbacuT6ldWCpehbdl5_2EDMCO-NZYpDIN7M19sMs6Q315cushn4qcTCtAbnlw0SaRCgcmFP-Q0pRx2IzxQpYyiN0FtxNtcPslSvFVCQE2xuBjxczkY3R0cA1PC1DvOkWH1Uqv4ZvAdkvvF7YmZbAtPNVffIuYX5kOtmB1acRZLXfkQEL4RVNsIQ4Nfq9tF7kwKa30JTOS9TjHoD_Yh_S8_1yV1H-cWWPgEJRKETn1TysLIyE5ZAs9Hydnrlf-XtiIp2ectbTCS6zh6n4tF2ulfvlnB8N8dUVJVrij3gLkCIuHwzaSLrZRRgKiWtOm2WifkC7uaLX-AxWJ_V4oi-tND-NlKRxoNoBpaYj5iRb14uJ0W_Xa6bFvSwiFihlandHb7LLsJKEbnEUvVqUg3okPPVqOwdCHuO-99cbvtVyJXl9K8H5gQAxm1HZBIII_jh6lftfxk7bab6FpS7a4x-zT89_Dn0sYa2_k1Sknkw0BvhsIiwVZWEsPRwN7LtvKMYIKu3Trx0OklwXIqkXd6UYwXjBMJR-d2zIz9iKl_VFDJxQ7B8_RGDB40b4ZLjb0-XfTdrduFlkvb79TUQC0mQFIQ2vOt3fb9QHIFuBWaigFWo5bHSJSENFIvar0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgL8F0WQAHw2bRtcWGoPLrN68cjCVvQASKkc20M9PZOiwtiQFPfF3P1JF_WwFafDIhpYNP56xpgtisC9EtLMuZlqQxcabtKOhNz-zfS_VBiN2jn6fbdZnakWv7a8pG34612RUh6gqnFWJC9RWE_Ht3Wj6KGVu4u6SKa4mlgnaKV4Er9vHxRTXvlj9xcIXe4yv_ME5EHc4wSZTH8WcPCtRBcBulgzd0VpOUnx6W73GAUguUBcJK5rW7ge-2jB6pfqgAG8Mssbv9QK8iMKyrl5iqQ9et4ducq5xxWdGgvexY2nm0Kj39GTFgFC26TuUGeu69ZBfgkTNT6xfMVPPKAulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMtQpgqKReoQfynZcgc0MAOK6T1LWbnAqVCmU3H0is_Fo0WO574sn7NYgOTzxeCbkhzbjpfeilAPf_VblR0zgrDhIsz9wk2uvIFAFYmQjeYEoADljOeScRvXzF06OiGymr8rxuXoriGKZeS1KRxPxDBehGhJ6LY_SzJwDGp36FnAwowtpBgDqrs64jvELkz54UUi9-zqA3SgYt-qWHe75C4UjyMMdW9BPPpRtZ8K2mSa60ssIJbF6_RnIC7-7FYg4E1NkQlKO7m2SZXqRFlQ5SigwPSXvzYhS9yKimyQih6JQemhnU_qtzy8FVkWXfU2O7qm1dr5tOExPe8udvIe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=S5xXhbEjKCJsB__D8UchXoPehz5H5V2HJTd3KPP0FJ6z7tWpZIfstaV_6aHt5FKG0bh_dMgI_ECpMCPq1Jlv72-7eR-QQBUKT_nt3VgPyZziNWT3hXZ3oNOCnV4nXP7lU8WjewwyeJetV8h7cr9xPA-AlJg4x2qvkfElmgtGzmRjpofXhWWCy1vaxoBdx1ytdniDQbfhlRloJLx1mZ5ehLnua3hdBmM0zYEFZeBs_DTrmx2gus3uS2vA02_nRgdhyzN_fIDx6UUquU8oa9niCczQmUdbm9GhJvktA3adgnm_dJz9K8I12zRR6oWHeJFxkgLm_3deSihAbLN0Tw37GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=S5xXhbEjKCJsB__D8UchXoPehz5H5V2HJTd3KPP0FJ6z7tWpZIfstaV_6aHt5FKG0bh_dMgI_ECpMCPq1Jlv72-7eR-QQBUKT_nt3VgPyZziNWT3hXZ3oNOCnV4nXP7lU8WjewwyeJetV8h7cr9xPA-AlJg4x2qvkfElmgtGzmRjpofXhWWCy1vaxoBdx1ytdniDQbfhlRloJLx1mZ5ehLnua3hdBmM0zYEFZeBs_DTrmx2gus3uS2vA02_nRgdhyzN_fIDx6UUquU8oa9niCczQmUdbm9GhJvktA3adgnm_dJz9K8I12zRR6oWHeJFxkgLm_3deSihAbLN0Tw37GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=NF_6oUCPn0BV3S8mKbcg86QuBkyRAKuBStVuJU3kEX37p9pCusoOj9Jh6uczG-2g8D5FgXkfC2bJ92urGKwAobl87XqsYlAkKYrI7EdRNwURU0MqcwR71j7SDSaKchZPZTnUtnN5W-n0ry46d5NrCqmuM5YdFSktcFO5KmZsh6Iv5ROsULTwpIY86dzRxXSJltFQxBW-3_xyaTmud6rmKeUEunozKjg2aA54qTu2eVDTmaiVcKgjpkzsxtV8q3duPIJhUP3zwubU54V7NTCrmc1s-PVPlM3CrOjWTRYsCmJzyEPTZMnnGRAbZm3CRUojF-O4YGFW04WgyE9pgVMCSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=NF_6oUCPn0BV3S8mKbcg86QuBkyRAKuBStVuJU3kEX37p9pCusoOj9Jh6uczG-2g8D5FgXkfC2bJ92urGKwAobl87XqsYlAkKYrI7EdRNwURU0MqcwR71j7SDSaKchZPZTnUtnN5W-n0ry46d5NrCqmuM5YdFSktcFO5KmZsh6Iv5ROsULTwpIY86dzRxXSJltFQxBW-3_xyaTmud6rmKeUEunozKjg2aA54qTu2eVDTmaiVcKgjpkzsxtV8q3duPIJhUP3zwubU54V7NTCrmc1s-PVPlM3CrOjWTRYsCmJzyEPTZMnnGRAbZm3CRUojF-O4YGFW04WgyE9pgVMCSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=J1UyMRNGoB9A2K5jLwz92TxKZVSf7esypNzLpeYTdw1fQ6dr78mJYQArbpZxRsGDqKYIxiXSzqW9YVHtkuDy0KN5IUPHBvdre6VIGNfZ7Kyd7nTHDXMi9tdfreTdzEeBf-EEe_BEErl7QtuFF_iteqfGkqDSoGOFslXWqcvCYGdd8qP3_5xgDNnauwFXheI2o6s7O8pPy1CXxzTnu4ND1uZQDWeddyvK6V6lpgBFkupVgbJfWKkpHSdLXpbcl5-XTtVdz4pMNF5o4KTtqftGDppEY1DN-L9UvjKl6cSccfob1DTqhsI1d9bvs_TKmkhKwTzBEin3Jxbej0DizA7rKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=J1UyMRNGoB9A2K5jLwz92TxKZVSf7esypNzLpeYTdw1fQ6dr78mJYQArbpZxRsGDqKYIxiXSzqW9YVHtkuDy0KN5IUPHBvdre6VIGNfZ7Kyd7nTHDXMi9tdfreTdzEeBf-EEe_BEErl7QtuFF_iteqfGkqDSoGOFslXWqcvCYGdd8qP3_5xgDNnauwFXheI2o6s7O8pPy1CXxzTnu4ND1uZQDWeddyvK6V6lpgBFkupVgbJfWKkpHSdLXpbcl5-XTtVdz4pMNF5o4KTtqftGDppEY1DN-L9UvjKl6cSccfob1DTqhsI1d9bvs_TKmkhKwTzBEin3Jxbej0DizA7rKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=I4sRwziSIcacoPJvv3AC4ABuCtdgT9VBpvQTIeRj1ygrtLHE5DJiBSzP2T7LYxxSfsgWfy33eFP2Vh8wCUUe6yhAbpXJ7dsUzMSD5fgIc5A67XaD1XsHcknyckZVWam7PL6hGJ5vrwcGq6jfahZJ3c8X0SIoN-9jAZEdxVmq6jjYa7VyOlqeMjYQTncqvICzpOH3HGqYNdzWH22ukMrgUsJh0xHG1SV158TDcLDOiPdS8Mi2Eykjq_PgrOXPnnMMPTeNpIOOAhAmfS3fmaa3vcmISln2VQQIk6pTcETduWbwDa3HPSIgMzupF446K9Y_F4C73OtJ9YREL-mNpzTlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyVBRDWJ-X8VRyEb2qOMQntcEN2h8dBJ0PGr8yDjnhmJ9e8dRzlLT1F6QQSMfGm6zbp2MTx7DX1cdXv1j3rxLI-ufgJFopr62mftNTfj23yhIqV2orB4d0HzAJ0vGvRCXP5N-Bo4Bj730AplDj1i2hIlMlNIPUX6LAZqQK7GGZG9gv79sOX0CoOoM33l8eqL6WiFQKSkb10b7iSRVp1pb6VTXdIu0zKpEomLSRCN8yVv7xN-hZlv1wiGsxh9G6E73YqG8uQjJepOVJ_abmlei5KlQItlx842RMrTpE8EeQ8ZwnxvECIbbv25U4h9OHkzHh5ZxbtK-UlTEgk-td09cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy0zozCTvQx2odrg_73rIhpPCHWm1MO0oIz9HtHyraN7tqxBQQxBIb76Z9ZzGrtiwuQ1BVu5Tip1E77I44WyZ3mxxSkeQGiHkvBmwr1RKlrV2yPipcQe7Gj6sXwaJIKGP5yXXhVtqbQ4t6luVzqk9DW0U--K-kuXsLJPaSnjr5--dqJTWc7CpGwux1lH65PINCLqqKZZDSi0GtAIp0Dr1dwF27VU002Ka5IUayI2lvtWmun3SosynULjbZDcRQ3cwPMAA4kR8uVdJT_Bovwj3Re2oCyHjRWFWxCUIGCLgkQdtRTPj9oDrLOeyJVmhlj7tofdxI8jzNTqNS4ODB6rbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=b8aql_Y3psX5nSlofYdIZkf2d54QTBk_snLDu0cUnJrZkAdOScYL3_b4bJf4RIv6HMmtLNKl3vEa2-Co77dMPDyNc-B9XZldBKg1DHPXhllo4GRGhe3z9FExsegB8atAEm_DEQVoSyGjmvI1908oh5QX6Luv98xy-mCwIvrH6zMQRPplAr1I7DujGgZxobbZdJ2VsGTvaRmCMVtYv0j0pY5wtttX2oqOSww_FvQ3i7kwi0J0RVD6Kk2HdKMV5aRWqWtcCF2-iBiEfpSDIHWCzc035c-5fcvMWFmztmnJteZbLAMmFOqP8bMEkplq8rg21W1vo5VTaFROsZjAaZP0hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=b8aql_Y3psX5nSlofYdIZkf2d54QTBk_snLDu0cUnJrZkAdOScYL3_b4bJf4RIv6HMmtLNKl3vEa2-Co77dMPDyNc-B9XZldBKg1DHPXhllo4GRGhe3z9FExsegB8atAEm_DEQVoSyGjmvI1908oh5QX6Luv98xy-mCwIvrH6zMQRPplAr1I7DujGgZxobbZdJ2VsGTvaRmCMVtYv0j0pY5wtttX2oqOSww_FvQ3i7kwi0J0RVD6Kk2HdKMV5aRWqWtcCF2-iBiEfpSDIHWCzc035c-5fcvMWFmztmnJteZbLAMmFOqP8bMEkplq8rg21W1vo5VTaFROsZjAaZP0hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=KC3u_71MH5qUO-V5cSVZI3qtI2bUWVUT2LotalWSwlDoMK0IkGwCPolFnaXQ1gKVEDZi_0orfQ3IZcW2VoJANE32nFw60q1WaHQPgFoj-8abTrQJ-v95NPbfITBaOZ7IXYbB_XSaRiCBEZ7YVK9SBd4PTg6jLlEF7bSDnKQoM-iRoswvGjWz1YS9V5Bx6J-QqTNQcXYOiuHRL8E_TPqDcEs0zjeiYI5Sz_avGTVYk56Awkomj4KxoQI7Yxr-GPBEqGP802wChIhdoiJNRAYlCt1C58wF0egC2dwR2EMwWl5uvVoBaiYDegn5zChn2-j4R0wFLkKxnkECwfUfKkJMb4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=KC3u_71MH5qUO-V5cSVZI3qtI2bUWVUT2LotalWSwlDoMK0IkGwCPolFnaXQ1gKVEDZi_0orfQ3IZcW2VoJANE32nFw60q1WaHQPgFoj-8abTrQJ-v95NPbfITBaOZ7IXYbB_XSaRiCBEZ7YVK9SBd4PTg6jLlEF7bSDnKQoM-iRoswvGjWz1YS9V5Bx6J-QqTNQcXYOiuHRL8E_TPqDcEs0zjeiYI5Sz_avGTVYk56Awkomj4KxoQI7Yxr-GPBEqGP802wChIhdoiJNRAYlCt1C58wF0egC2dwR2EMwWl5uvVoBaiYDegn5zChn2-j4R0wFLkKxnkECwfUfKkJMb4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=qnwIY9ZVqU0d8dVR9UrHnJIpNuy4qAmlaAH98CDzMmiCyC0uxJGTI0yrSPdN1jKdX0qTvCN9e6gaPMVgOkmcpCZmtOV2nYzLNM4e5hwtbCrDqvr-ntHz0An3d94zJtodMB7wAoBezijvxjVd7rurijSK7IBhlYDX860XhBJkbc1l8DRRFrlD-8OyLBoZzSTj9yMKxgU768YLQu7GAb_tJe-zdlgjOpHrKmYFx6z9fUjlwSZynRIPvN3c0RkGUuxkwxch5odsYoM7xrmKY803T8TzpnyLCt66XPPOwe7kAlcziuwC2WXMeoYM4c1kE9GuC3roKY4Tc33NSQuf6NQHzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=qnwIY9ZVqU0d8dVR9UrHnJIpNuy4qAmlaAH98CDzMmiCyC0uxJGTI0yrSPdN1jKdX0qTvCN9e6gaPMVgOkmcpCZmtOV2nYzLNM4e5hwtbCrDqvr-ntHz0An3d94zJtodMB7wAoBezijvxjVd7rurijSK7IBhlYDX860XhBJkbc1l8DRRFrlD-8OyLBoZzSTj9yMKxgU768YLQu7GAb_tJe-zdlgjOpHrKmYFx6z9fUjlwSZynRIPvN3c0RkGUuxkwxch5odsYoM7xrmKY803T8TzpnyLCt66XPPOwe7kAlcziuwC2WXMeoYM4c1kE9GuC3roKY4Tc33NSQuf6NQHzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhID3zfPqecu7tcxT4SZfX0EQHWFW29uv5EuC5uKDiXuJ57hC0Pky3z19mK5Yolz8caWYl7AkquqhJEXnppyWAFFJxuvOxVR-Nqt_w6kqNhB7D3qmwptEUs03lb6KrYw6HPRA3Hn6OHdq5_IPgumpQbtVzml-87VINpOQRm-7QzXgBPvCV_h-zDPkJ-hAENs4bOYyBOSBvzZ7Eflc14h3OVSFMH0Ajr4KvXnGetfU6KQ_jVhOIOlAzQjMBOUq7DMETlz0AoS5JN4SGwawxqJRMwbTAPk4mT7kKhf-5mvhhDRW17SqEyLKKOq4S5Ps8sP7bGCHdjKAblazzjBEKYDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
ترامپ به فاصله ۲۴ ساعت، از ایده گرفتن ۲۰ درصد سود از کشتی‌های عبوری از تنگه هرمز کوتاه آمد.
«به لطف نیروهای نظامی آمریکا و همه اعضای قدرتمندترین نیروی نظامی جهان ــ با فاصله‌ای بسیار زیاد نسبت به دیگران ــ تنگه هرمز برای تردد همه کشتی‌ها باز است، به‌جز کشتی‌های ایران. و این هم به خاطر رهبری دروغگو، خشونت‌طلب و شرور ایران است که این کشور را به سوی نابودی کامل سوق می‌دهد.
بنابراین، ما
یک محاصره کامل
اعمال خواهیم کرد، اما
تنها علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هرگونه محموله مرتبط با ایران حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده‌ای که با رهبران خاورمیانه داشته‌ام، تصمیم گرفته‌ام
کارمزد ۲۰ درصدی بازپرداخت به ایالات متحده
را با
توافق‌های تجاری و سرمایه‌گذاری
که کشورهای مختلف حوزه خلیج فارس در آمریکا انجام خواهند داد، جایگزین کنم.
این سرمایه‌گذاری‌ها عظیم خواهند بود و در عین حال برای خود آنها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q83R3ltuq7r8LuY7JfLU4Gu8ywplhg5KC8NbUyMhotYkAbNB_drlio45RnwRtvMCX9QaH3P08ETs95gntj7_bGK2IlawO0vmdL-aeoqjUJ0jEEDCVI3zHd5FAqba0yIsDgJxqf2zY4_QDdOJpGCKg3gr6VHfCmdNA0mViM4QF5rgvhbuhu_vauOowObIfCyu-baUFQH0X6ztZUmNPhr5KbMzPJ0CCtT-tAFHxJOvdKgqc0MIsZlu1VQ_65f2i3lp2TPX81hRh81HweF_zLDlLqPTcDcAoX6vm4ZD0LsCshAWcGchbtOB5qWu7PwkLY-qARGjy1kFGHJyhdpSyPcZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=MZGzRpj8q9kjQhBtBda_NNr_2GcQxFzBclHpdtLFoItplLBSMPwzenp1C59iOco8m9fgh-ISFEEJMQeiPGCWHAEskFALw_dH65_TNeoaQEVa6aO12tXMjF3bZ2ogyvDilhzcsrOhU9HWHP8cT0huwYfO2AUEhRHI8CZJF_fXVYmVWu_NwgFfKg6NTdnm-KsnnucN9E0Nb27lBT62YHptS5Vem_9Ygf25eLVjfZoaa6nF0y-ZaDs9AHApjertE0w06JJeexVYw8nW-eOE0VeR6CZwpOfZe_dHod47-X1fSn0P2l1HaXRU7s42mY7seYCNUCBffdlFSEGrBLyc_mwh8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=MZGzRpj8q9kjQhBtBda_NNr_2GcQxFzBclHpdtLFoItplLBSMPwzenp1C59iOco8m9fgh-ISFEEJMQeiPGCWHAEskFALw_dH65_TNeoaQEVa6aO12tXMjF3bZ2ogyvDilhzcsrOhU9HWHP8cT0huwYfO2AUEhRHI8CZJF_fXVYmVWu_NwgFfKg6NTdnm-KsnnucN9E0Nb27lBT62YHptS5Vem_9Ygf25eLVjfZoaa6nF0y-ZaDs9AHApjertE0w06JJeexVYw8nW-eOE0VeR6CZwpOfZe_dHod47-X1fSn0P2l1HaXRU7s42mY7seYCNUCBffdlFSEGrBLyc_mwh8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoYnaRpGM56l6pE-zpeqL0DroP8ddu_6eQb2KOA1scPp-UzmJRMlvAuomwWBlJVVuJRZ8Yauhxu7UXH8y_gmpHHCaxaf5JtF3hfUnXVpYGyrCXsu6ZW7_hmlsz2kK4a_ifuAmSpjzwixSYca8u0OvV2CNGBwY_yZ4cng0GneqVvrquDd0Qb3dlqgCzc7_mB3bqVTjMWozFoQl4LFciGY1CalxBzZz53qLh7Dr2aGEvok66vW-_m0JoDsu0ohfUscb-RvOCgBkmSVVzuMcou5Sje9_T_EThNTzsnYl_-ELQRJWP5w3VIU6KieX9mz2oW0FxZ5wu8qaPsg5c9W_9MUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrY7WjgWrub7tq0AamY8g78Q-FpAvzsBWxNplTFWJ49sujoliCVCbztspmZmwASdgGbWrnvn2-Y8QMjzLA9Nf5oBzWqUk6FG8jW_5YrH5JgnRbxO8HUKVPxRFKyMRqn46pY_3FcShMvCRlDZG7fqORB3xHxATpYBiQOqVVAgShJ-Y5huUYMSp6nn8ycbBKRng8m5n5wJwtPG1vX-i4HytK43q8tQD89WJQWzRdCnxSTmN52hepo-ojekuE_dCc-1xbQ6QaOnqaKxrtbWdbynoTbynrO9xG5AjQY-QvasmGw4ea66wnfpt5I4bIaW-Dt1cFIcfqAeKGkxo36xzOc6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
حمله به آبادان و ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔺
امروز سه‌شنبه ۲۳ تیرماه،
در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان
و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔺
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه
اعلام خواهد شد.
🔺
جمهوری اسلامی در این ۴ شب و صدها مورد حملات، هرگز اعلام نکرده که چه تاسیسات
و مراکزی مورد هدف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=TF6_NENzJ9VXa6e9cpdsInrWXrUdu_kdw-IypLKPivQfnS5_dmr8zWu0iTuCBzHGDley7Ukn1t2hiGwDwW2ZOqyHpst4n62y3kOAbmMT9OuDIQYyUHb6u-vlWLgAEtsUFO6NzdiWwgJXDvW6htdrQr3CT6Bo_XzTg_PeK8qG3K_PZddhFUGgXEuz1OHoPACnP-Ff3GVr-7fvm4g4B0MYfRgNDuT_2avbBlGC7NUg-qazUpUjYv8-G-l9TtUKItkXxJvi64BpOHCGVKYeFfnyfTpdiDvk4carrELWgMBwImk8tfU5guuDdmgnsTaKsr2mOlacWySBDVIjbecoVIisWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=TF6_NENzJ9VXa6e9cpdsInrWXrUdu_kdw-IypLKPivQfnS5_dmr8zWu0iTuCBzHGDley7Ukn1t2hiGwDwW2ZOqyHpst4n62y3kOAbmMT9OuDIQYyUHb6u-vlWLgAEtsUFO6NzdiWwgJXDvW6htdrQr3CT6Bo_XzTg_PeK8qG3K_PZddhFUGgXEuz1OHoPACnP-Ff3GVr-7fvm4g4B0MYfRgNDuT_2avbBlGC7NUg-qazUpUjYv8-G-l9TtUKItkXxJvi64BpOHCGVKYeFfnyfTpdiDvk4carrELWgMBwImk8tfU5guuDdmgnsTaKsr2mOlacWySBDVIjbecoVIisWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wfp0iy4XsYYoFnY6DIBQnvrveZtzKcw4OKk4eNcIc4uu7jhQXvklcKNOxwWNs78ycjI5bHK3vDjJ7uTclIM8T9PsWYAjxwdgVvoAB6qpkyuqv05SvwzQCQMhnK9uVgFRo9sNYVVhN1uJb4LAwjg02_RvRd7HEtwBfWG0vkPsiiAjbeK4bPasxPK6I8cMnXI6LZs_NSNf6VffS8rfnAojbPSaz1JRWNKGdk4DHc8KozKP-vO6vTVwkiyWKJF3etSgpvru3zk6p7U1Zy80kZ_jSyV8KKuUbw4uh0244sc_a3az8qVXMH_Vz9mKeXzF8O_8Vb6-VCGmUzH67DEyRvtZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSeQVXtCw8G9wGoRYkZNvYfqWnGdGJUMmib3ki6Y8Y3M72q5ZsUXZp7JhWQyN7Vlytfn2-G5LkHau2oVJP463cw7i8Kh4JsixzQojlqcvvHdABLJq1FThF62jg-9KmzZ6r0Qi99vRb6B-zTxcD2RAfF2HUnBSuUfPTSNtVL_S2PLWGAOxbkTTI3AMv1RUAZn995T543feX_ZGS4Bu9dgWpu_5Y0ZAsM7d8_jxz6Wo3jlhiGzSCFZCmqDhlEBurEziIFG6uAAmFCyZFK5hbg9fySSHzMmmpnA-w0Rr9F-qSFHysRKD7eTuTDIIlAqVhSwNEzPQ3XZ6bfCU6isFnEYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.
در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!
مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی) نیز در این حملات مشارکت دارند.
🔺
دفعه قبل هم که امارات در پاسخ به هفته‌ها حملات جمهوری اسلامی به جنوب ایران حمله کرد، مقامات ج‌ا تا چندین روز نگفتند که کار امارات بود.
الان هم برخی از این حملات مثلا دیشب، با حملات دقایقی پیش مشخص نیست کار کیه.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=H5qgdq-LR_SQItQ4h501Bji5XGiP2pZ4K01r1TKA-l7Ule_sgIOF6_rOjrIffTyHM6dUy8eN7e62uIlGE1GJTY6SyQYmypwHmDelsaSJWFdUWzB53wT80iqyedNtUZbEuZ-CaYQerv7fo5pzR2SxfrArl59WGKsKIaTZDQIiaFCO12WFRkFAXFm4GKVLJXiaQWj2VPmT3a7uEd8lNB1O3dKAG-NQr1moCL_tVX7486qk7HLJkK6fF0W6JcQjn2haUf-dEAiwZWfOvOVg2PYZW-XaBOoxil4blJ8m2pnFnBOgPucq9HaNx0HI07aFGndJQTRF5hBdqfiBhZ5lQmmYPqGhJ3Hci3CYzbXimSOUhVPntWiMIiUwT0fPg8ELI8jxJHlKptXRsMvAoKHHiQaTzYebro4RdU9ZduKO6Wt7S85S9gopSIVBKyzMlDEIFpY41C4N4T0af3_FNOJJXg8PprAZcIz2SWrYmXBjx1hsynsGa-GIlbiXop3e3sMxkIa0oTFKuQgBbBvZ8duJHA1hFE76s4oGP7a57bAAj1-hf3s-Q5UFngRe1iapjSgI1aMdnzkLj4-khT9Q-O8s4CTbVVUTu1ULXJ-q1qC8p6nEMtd5ugU7yO51yaxN56w19yW3jy7ku8lqDFVuF2Z1eFOTiZpfnM7fUrVzcg8Xp4STug4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=H5qgdq-LR_SQItQ4h501Bji5XGiP2pZ4K01r1TKA-l7Ule_sgIOF6_rOjrIffTyHM6dUy8eN7e62uIlGE1GJTY6SyQYmypwHmDelsaSJWFdUWzB53wT80iqyedNtUZbEuZ-CaYQerv7fo5pzR2SxfrArl59WGKsKIaTZDQIiaFCO12WFRkFAXFm4GKVLJXiaQWj2VPmT3a7uEd8lNB1O3dKAG-NQr1moCL_tVX7486qk7HLJkK6fF0W6JcQjn2haUf-dEAiwZWfOvOVg2PYZW-XaBOoxil4blJ8m2pnFnBOgPucq9HaNx0HI07aFGndJQTRF5hBdqfiBhZ5lQmmYPqGhJ3Hci3CYzbXimSOUhVPntWiMIiUwT0fPg8ELI8jxJHlKptXRsMvAoKHHiQaTzYebro4RdU9ZduKO6Wt7S85S9gopSIVBKyzMlDEIFpY41C4N4T0af3_FNOJJXg8PprAZcIz2SWrYmXBjx1hsynsGa-GIlbiXop3e3sMxkIa0oTFKuQgBbBvZ8duJHA1hFE76s4oGP7a57bAAj1-hf3s-Q5UFngRe1iapjSgI1aMdnzkLj4-khT9Q-O8s4CTbVVUTu1ULXJ-q1qC8p6nEMtd5ugU7yO51yaxN56w19yW3jy7ku8lqDFVuF2Z1eFOTiZpfnM7fUrVzcg8Xp4STug4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI_tZVjSjJ_0_5skJpjsVAkD5WX6Z_98fWGx2YbhVRKfRgFeog_Pa--dy50HKG6JlNO6NhDqwkuabNT8HXgrwNntMCmX8Os2XvjG57uSg27Z1pNpieNn8EplTKskS9exlBPUUyMsvSKIK4k903aeS_waB8fSDXFlOR-z9inJ8jt5AleId5qlecajkX3xqqGdHdUAd3F2VHuoiRMI3ai9OAyJTtRcmYoIoctoxkn2byI2hpKA7GoALcTJyc3KiWgsulKV7BmDLWsZLm9Ldwio-UFx6md2T2K6BOsOVuj2cLhTL54fIEMPwHrYcIwG-3QPuoMy_CZgKMZVP7Moh6uNdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EUmj3GPPLLGNowfHuFQpLLyjkxkBNW906OSPpS8nWrk2X8-uz4Hh1Fh1MFPn3xjLsCiqb4Jxg9ieVrx72HFfL67_CfhXBW-jvqwAc27GMJMckqnfC9nkIQ6ccJl9jlBP99DqUQd8jE2qgOosdQ1rZhPXkjqRA_eDwAGmEM9kl97c1syW3ZtlQuun9OLGvaS-AuBzD-o2SkazQ3Mq79SPlS0tczZm0KDmFoRmRgvsjTyA44PZv9owU7h1IB6I6RwBybVLxs1l_rzTLAyU-TyBOLAsiCoBmBv09ePeF5_VnyvmTmXhJWkrJjHylafdIsijCnlQhjE09MYbKVJ5pOa5w3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EUmj3GPPLLGNowfHuFQpLLyjkxkBNW906OSPpS8nWrk2X8-uz4Hh1Fh1MFPn3xjLsCiqb4Jxg9ieVrx72HFfL67_CfhXBW-jvqwAc27GMJMckqnfC9nkIQ6ccJl9jlBP99DqUQd8jE2qgOosdQ1rZhPXkjqRA_eDwAGmEM9kl97c1syW3ZtlQuun9OLGvaS-AuBzD-o2SkazQ3Mq79SPlS0tczZm0KDmFoRmRgvsjTyA44PZv9owU7h1IB6I6RwBybVLxs1l_rzTLAyU-TyBOLAsiCoBmBv09ePeF5_VnyvmTmXhJWkrJjHylafdIsijCnlQhjE09MYbKVJ5pOa5w3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=Gome0L__qSdFnow5AhddlnmLt6y_hhessZoTPCcBXI0xzf_yfXNbHXzn6l4VYeOa__STcIkCuKPtjPoUTiiJzrrS7pzBJwf6V2Q4YH9TUijVdpM5GVXk85_De7zBHElG121eqjk3taqUBYix9hUr5rY-DmNNrhCWZO5MkoaAzh15DKGBrTmwdXmBZ6hjcyq774uG6mH1NFOOJHKoKuMnGiFap2xAom_mH7VS0n-TCZ1YMQbjpqRR6fEeHQaZx3D1Lbh_iU_Q0L2AOAzFHH0ZxR1XeNRRGQ-3pUvYycsejZij893GPVwaC4baobrxvuJh0KePR1dDPf95XJu-ouO1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=Gome0L__qSdFnow5AhddlnmLt6y_hhessZoTPCcBXI0xzf_yfXNbHXzn6l4VYeOa__STcIkCuKPtjPoUTiiJzrrS7pzBJwf6V2Q4YH9TUijVdpM5GVXk85_De7zBHElG121eqjk3taqUBYix9hUr5rY-DmNNrhCWZO5MkoaAzh15DKGBrTmwdXmBZ6hjcyq774uG6mH1NFOOJHKoKuMnGiFap2xAom_mH7VS0n-TCZ1YMQbjpqRR6fEeHQaZx3D1Lbh_iU_Q0L2AOAzFHH0ZxR1XeNRRGQ-3pUvYycsejZij893GPVwaC4baobrxvuJh0KePR1dDPf95XJu-ouO1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2Zqi3hjO34ebac8qNRp_5AjuDOCF6fnPGUTCaCitJeh-Z8Zpgg1kYMuJZ9z0aimbxeziyOvqfvY65SgHvwlWTw-pkCQf38-_a5LX2pUN984hLAL0EOkJqh7v81hwencC2D1ZYajilGhNraf9YdUkIqT_h5j8wugLlmN9YS9XqHw6ZZawXg6rhz1-quLgUsCWMVzeG8ZeneNIVy6LSQOqBurJouTLpdLc3c6HiEUad12bwN0xluNOGw_0mFT-F0FKmbt-NNclZ1OkJl0pSn5CfyhS7J2Vvbs8F88gzVDIpvoi05u9GHsgc9thOBoauekwX81aAmrYgFhpt0bNS9mAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=tzeqalavEQQjUdbLMY5iHZgogHl-Des8XJK_cD9s7fRp2Tb7aiGmnqjeM8U5hN2OwP8gm-4fCTqY7VCuP92n_md96EAROS5NSylq1Hc-cERyDceDnnou1x3BZG5Dz8asujzOqZ_pXCG24XTx-WqR-1iBqh3T93EYE6TdzcpBZ5owhu5r4PkgHzMmb_mhSudHZWd4_MXR93u8vm1Wq2Yx0jH8UspDcmzPRcHLpJrrrGiM19b2WdXdzWU4uVXHV54zvmw4_XnbjajI1b7ROntUXPkZ517umIM3DKDgVQ3Vvi1yJ-ABOHHhpSU2LN-VPqD4XI7q15KUpzLM7ljAC8bQIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=tzeqalavEQQjUdbLMY5iHZgogHl-Des8XJK_cD9s7fRp2Tb7aiGmnqjeM8U5hN2OwP8gm-4fCTqY7VCuP92n_md96EAROS5NSylq1Hc-cERyDceDnnou1x3BZG5Dz8asujzOqZ_pXCG24XTx-WqR-1iBqh3T93EYE6TdzcpBZ5owhu5r4PkgHzMmb_mhSudHZWd4_MXR93u8vm1Wq2Yx0jH8UspDcmzPRcHLpJrrrGiM19b2WdXdzWU4uVXHV54zvmw4_XnbjajI1b7ROntUXPkZ517umIM3DKDgVQ3Vvi1yJ-ABOHHhpSU2LN-VPqD4XI7q15KUpzLM7ljAC8bQIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=OJLkEJ3swpDHUolveMRrz-aWAcoBUNpERXWKTCxVUBAeJ_5CDUl3dNKWqB0RPqZAOzhzeccvGJObppgBoqDdhW0KjXLr2El43egcpS41HjwrX5ksH0QQO_I8nNsy4RP4zDGW25yn-qhEmF5zr4FOXoLs9SwBn24k5sHY56-YC4xENCF7Vp4qnbKe_7MOsrtWxAbXAZW6lTRfoKqA8z63TM0C1mugMpkSto2hnAOFNkpUjbOdh914Unfe8PD_kxFGsASORY_e3IR934DxxMQwJ4md8c_qr5lLSyfoYxTc-yZHPsqjI2ZrNXtrvr3yendUnLA-Q1t501KO_3OAM2EEZaKT2-mwIcTDz_MEK5mGLRs13iB9ISWKp_upDO9vLJAntfPna9wVzjTIluRwpWU8umHuAEUhViShN44DuTm7IKBv7yRd00iqRtaHdHTIcGyLMJu1SsgnJQf_SDtVYzWrI06fRyp9lT4wgcKe5-iJEREzhf9a7p6PFhavObmCWT4dneYIzlvj4zmI7w1L4r4nlag3c4RiUKFqBJ0RC173cR773lDArTBzsYy0f1QBagVoB5AMCvUUN6qm25MJAKPVeF0jguDZkrFfF68raw2mwfoCspuzx0M7PYfZQ0sRWJwj9u7f9h0Wxo9N7FEQIupE3FadEc_UQUMmOg7hhthReFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=OJLkEJ3swpDHUolveMRrz-aWAcoBUNpERXWKTCxVUBAeJ_5CDUl3dNKWqB0RPqZAOzhzeccvGJObppgBoqDdhW0KjXLr2El43egcpS41HjwrX5ksH0QQO_I8nNsy4RP4zDGW25yn-qhEmF5zr4FOXoLs9SwBn24k5sHY56-YC4xENCF7Vp4qnbKe_7MOsrtWxAbXAZW6lTRfoKqA8z63TM0C1mugMpkSto2hnAOFNkpUjbOdh914Unfe8PD_kxFGsASORY_e3IR934DxxMQwJ4md8c_qr5lLSyfoYxTc-yZHPsqjI2ZrNXtrvr3yendUnLA-Q1t501KO_3OAM2EEZaKT2-mwIcTDz_MEK5mGLRs13iB9ISWKp_upDO9vLJAntfPna9wVzjTIluRwpWU8umHuAEUhViShN44DuTm7IKBv7yRd00iqRtaHdHTIcGyLMJu1SsgnJQf_SDtVYzWrI06fRyp9lT4wgcKe5-iJEREzhf9a7p6PFhavObmCWT4dneYIzlvj4zmI7w1L4r4nlag3c4RiUKFqBJ0RC173cR773lDArTBzsYy0f1QBagVoB5AMCvUUN6qm25MJAKPVeF0jguDZkrFfF68raw2mwfoCspuzx0M7PYfZQ0sRWJwj9u7f9h0Wxo9N7FEQIupE3FadEc_UQUMmOg7hhthReFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUdJrGtmzT9TnK0xawonUDNopKA3pwm-0mmTMlHTlr4lDhohxktVnnGH787AyztFbOg_go83Vm5OZbySMRJI-Zhx4w6lgdAa6EzltDzuP_q1Sc7efM0NIDX89w7Gb99xlpzpP-bvy66vYlu4eS3Ks-1ig_QLVVK0OMF98EO2WbmD7punwjOd5I20zCSgNE2iM5A6mtxQ340HQNkpR3krrc5KDwbxuRH4O-KurXo8aGGUUYSyqiW3FzGQyKBD9UozxVVjyFERk7Ge5S2DQU9iV2qyRp9Z_UNDDy1hf1xlj7pLf1EQcz-mYuDcanIuuKjg0JvTbCpFYRovOF6Gc-s9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXBoam6iqbBGYENBc4RSuN00KmGzEtWO37ESsZJ17n3MoHxzhcp46RvtIvt-PZcGOG6vtOhNc_b1cbp_Kaas-UxUpKlHSjt3OuLIbD6IpN5XhAiDymwMEwm-8E7gFgkrJY7QPgq109VFaQYUUSfG-h_qK7RGBVKtgMPdKykEfqml8w5kFWSKKEH_OmT8-QZfzwlEQaEo2tu-x1hdEx86hZiLJWvxVRLuci8JVu4pvhUhlv1AK-etgVJg71s7mZwtZnh5a2BgK_Hvh2AgvsVHbA7BUoP21cuvwHVWmv30s7xgaZLkjvCFMqbNX4GWLuh8-LwUkBK5E__-ZPDm4jYfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsalbOT5psUoDQbSWhfpnAaxy8sctl7nL3jPscWsC_8hY6jNDdxEe2DJJnRMpMP9eCHZDCGdnYALEOqaq4khTMCT8q9IKSHbI4qePn5KtUvL40TfXGePz4m5IEIe8KaFeehFjY_fz7a-_0E4dPYKTGkt5ggPr-MYbfRQKUhoZTAYJpMasjNNxowOwDUWYBwa24GYKT4h1hjem-ur4NG6N5rCme-TDQmKyXf9nOO3lrEnPiPxna28GzQIuSXQl8cjASGwk8U_BH6UHzUgiG5GVx290Uoe6D1kGsXc0cZ8FvX7quc36dofM7LQav404kWcThNS7BElveTHwe0sll26Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auSgEgD4IeK9t0jbNCTc6MCfsQVFDtpUk0NfMzKOJi93TIXdY8_YJMdYAQlCEZsl3xE5y8170PxnI1beNb4lm0A7A4dEGxR--Nh30B82XtFLrY0WmYjOnav1voCeWjvNeuzPqtY8dqzU5i22S1GfLtFDNQXJkqfeQf0dww-OzfXAsM8jCuY70xZS3US3f92c4rFIoVecLXArEZeAXHwkEZBxY7jUwowULvEeMM0UQoxMTkanMKGau4SBwHtr4266ffMt-X8pH3rx5-K-eOM3CmiksdOsZAW4qRhGN1lGpreWRRo_ZKTFeJec8hS2DfRDStA2EQxApYwGx8t4oNQ6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou6kSc5VTZxUUr9e2YhXxnSGHbr-xghsN40gtsXBwoHlo2XvBNUO2cVvEctz0FbfTn6gc0s1_3WmkvDVKqLVKoKfn_zdLbTfiwqkyUHSYx8vJHo9yyI5Zeb5j786C292W8sbxCMYn6citManpeAcmY1GHQ_jZBZKbCz0USp46fSv3Jo-sz9nbntozWpMJnui9aMoYE_NDP3rBnRdJqkMoSNLG6Fin-4Y4F9mu7e9fD-ibfwWcTs1b-eVhUtpY8W_JvTG1Y42mM8QT6ph-jjoWmsKvEQ8Fbrb5ysuyPcAIGrvisC7-KfjsbilceUOW0taLbqSUuO-atS0NciI1BA7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»
شخص امیر قطر به تهران رفت،
همراه با نخست وزیر قطر و وزیر خارجه  قطر،
اما برای خامنه‌ای،
سطح هئیت قطری به رئیس مجلس
تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم
شخص خامنه‌ای شد!
از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی که قطر برای
خامنه‌ای و رئیسی قائل شد،
خودش به تنهایی یک توهین به خامنه‌ای بود!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTzhpJNuzB09AJ35M9LTIhUgd8FfKFMZJ37Efo53F4VRyt5faEr51p2Afzu32-cfYVw6rdV15MgtuUcEcRurcejFjdHRtmQE7qt32joj1RcpcrHTGMxfo4Uv-AoagvVsS4YZ7O4HHXm-lwLMJ0soX97JeYoJ75mP_5JtwMwAxOruiw_zWn_Jyq9qyRIa8zT43MwjDEsOqDTytRHDWo9rt9RJRefyS--Ch0zGuDFcBU2e9tUTRwVdEvG6042O2xrbppsVaJLY85VRw_NDQWu65mWEmbg17NpkRWEPw3rDsiXFRBaAd1o3-5OHlhCFGEG5DfmJSRsvkHP104RpuX1gnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که در دو روز گذشته
توسط جمهوری اسلامی مورد هدف قرار گرفته.
عمان، قطر، بحرین، کویت و اردن.
عمانی‌ها از حملات جمهوری اسلامی
بسیار خشمگین هستند.
عمان همواره یکی از دوستان ج‌ا در منطقه بوده  اما حملات مداوم ج‌ا
به این کشور باعث شده تا سران این کشور از ج‌ا خشمگین شوند.
🔺
بعد از اینکه در آخرین روزهای جنگ ۴۰ روزه نیروی هوایی امارات دست به عملیاتی در جنوب ایران زد، ج‌ا کمتر به امارات حمله میکند.
🔺
عربستان هم در میانه جنگ ۱۲ روزه به طور رسمی و جدی به ج‌ا هشدار داد که دست به حمله متقابل می‌کند و ج‌ا نیز رویکرد خود را تغییر داد
.
🔺
ج‌ا در هفته‌های اخیر بر بحرین و کویت  و بعضا قطر و عمان تمرکز کرده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qiUeP6S7BFk1pSL8KZqpYDGBJp5CASvCca0WUyh3SXXMsY8r9YwqN1potVUE-mgm_kt8BqcFH2SqsX-rj9hVcu0oGUNsh0_4rwJxMqH2DH6TWoMA3hDLAmBjoTFWPSmJTYfCc9ieuZcU9bZEsCi_PfiPF9ZJS0fDMw7L_LRzxAPUkou-vHz-4HyOCOB6n3hFwQMe9yStbwjl4X1JrfKG0gPMHFI7CWiI6AVYS8eBkSy9N4cOI_QuunDbJVVOWHzM0eI8f_UZsX_wfePvoWGnO4A0-l05i1fOkHHOgY5TrHBHdFZPEPQYpuvB16z_c424fJKgOM3CozGZWVlQZSuhZiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qiUeP6S7BFk1pSL8KZqpYDGBJp5CASvCca0WUyh3SXXMsY8r9YwqN1potVUE-mgm_kt8BqcFH2SqsX-rj9hVcu0oGUNsh0_4rwJxMqH2DH6TWoMA3hDLAmBjoTFWPSmJTYfCc9ieuZcU9bZEsCi_PfiPF9ZJS0fDMw7L_LRzxAPUkou-vHz-4HyOCOB6n3hFwQMe9yStbwjl4X1JrfKG0gPMHFI7CWiI6AVYS8eBkSy9N4cOI_QuunDbJVVOWHzM0eI8f_UZsX_wfePvoWGnO4A0-l05i1fOkHHOgY5TrHBHdFZPEPQYpuvB16z_c424fJKgOM3CozGZWVlQZSuhZiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pgY6E4esY17_z-NAnvZfmseBmRNBEh3EacCYB4y5cBvaeo3Zu7zwo_mNbXJheURaeR__EFz7ov5kaUf0NCIHIEsMrxMGH8p5DdM-3Zj3osVIZQet98qqo_GYfYfuNiITdzm8aDsvnQwuoagJOdw2Prx5Mlo7Gux8Dr6bYxhvWgs_Dai8jWDwYUnXp-Kym9RdD28kH1WUKAWg2PBZ4ZG1GTeh4i0Kt4MzA48n5qTdtyR52MLKN2cykyV2YsSrnSc6Slp-N7M7CuqPQ55vB4PvJAxXgdRcVTuAayQUZBecw0YpHEQicfzI_vnruQjLDk4QjRuG9QRBiSOuEfTC7n9BFxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pgY6E4esY17_z-NAnvZfmseBmRNBEh3EacCYB4y5cBvaeo3Zu7zwo_mNbXJheURaeR__EFz7ov5kaUf0NCIHIEsMrxMGH8p5DdM-3Zj3osVIZQet98qqo_GYfYfuNiITdzm8aDsvnQwuoagJOdw2Prx5Mlo7Gux8Dr6bYxhvWgs_Dai8jWDwYUnXp-Kym9RdD28kH1WUKAWg2PBZ4ZG1GTeh4i0Kt4MzA48n5qTdtyR52MLKN2cykyV2YsSrnSc6Slp-N7M7CuqPQ55vB4PvJAxXgdRcVTuAayQUZBecw0YpHEQicfzI_vnruQjLDk4QjRuG9QRBiSOuEfTC7n9BFxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ارتش آمریکا شب گذشته به ۹ شهر
در استان خوزستان حمله کرد : اهواز، آبادان، ماهشهر، بهبهان، شادگان، دزفول (پایگاه چهارم شکاری)، امیدیه (پایگاه پنجم شکاری) اندیمشک و خرمشهر
🚨
بندرعباس، قشم، جاسک و سیرک
در خط ساحلی و «خنداب» در استان مرکزی نیز شب گذشته مورد حمله قرار گرفتند.
🚨
جمهوری اسلامی نیز به اردن،
کویت و بحرین حمله کرد.
🔺
ویدئو : ارتش آمریکا این ویدئو
را از حملات دیشب خود منتشر کرد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=ug6ykdmwPUWeLnK9GslUyvKxRakBS1RU9_zKkTuILlty6p3biLJ8qmdfdu6lN2eHxDMylFRrABs0b7anQY_ToYA7zV7_QQ92ads9PAMXzLSiGHCToIXqvBbz44yPLy-w9bgugbSZItIzIed7Cpf31yAupdQmYv-bk7pchZLGIa7KYTmECtPMy3KPWcTi2x8A9kwUMGp-dJ4mjOCxOFfYzAjSTvlRLbAzNuVTXrqfQwHHRnDfmGtYVZ5RNPK8640QSZg49qMdz37Q_tcYfAeczvlqGgenorsOTikF35omDlKUJVcat_G_wfPghTSquld4PcavdK4RksyZDpA_aQcM9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=ug6ykdmwPUWeLnK9GslUyvKxRakBS1RU9_zKkTuILlty6p3biLJ8qmdfdu6lN2eHxDMylFRrABs0b7anQY_ToYA7zV7_QQ92ads9PAMXzLSiGHCToIXqvBbz44yPLy-w9bgugbSZItIzIed7Cpf31yAupdQmYv-bk7pchZLGIa7KYTmECtPMy3KPWcTi2x8A9kwUMGp-dJ4mjOCxOFfYzAjSTvlRLbAzNuVTXrqfQwHHRnDfmGtYVZ5RNPK8640QSZg49qMdz37Q_tcYfAeczvlqGgenorsOTikF35omDlKUJVcat_G_wfPghTSquld4PcavdK4RksyZDpA_aQcM9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=gIpvoLsxfyb2a3TpZ42-NXBAUuoLlmhiY52GCxa9nQqAcjgvRKVOqd0pvl8YcliRxYuD9ZZlErbzauz77QI0ZpNeLMWK21S-lZ5WvLwE2mfkzeZ1iRieBKhDr3nzE7bx-MGck36lIpN23ul2XY_gz2XTAhb3J4YEHKAZHKXsjCgEqOCsk9QhimDki6W9_vpCYQB61392uDG66lvOm9uyO_cSXhxfzEgWEMSC8I0-iTn2RDEdOe52HRfQPBc8ka4fmFHzoWEPtfkIxGB-Y8tLdlEVjxQypUw2iFstxGu-im0sWd818AOxkxJ-6UhdCNpf5Lj6-bjVnJ2tD47SFCxKNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=gIpvoLsxfyb2a3TpZ42-NXBAUuoLlmhiY52GCxa9nQqAcjgvRKVOqd0pvl8YcliRxYuD9ZZlErbzauz77QI0ZpNeLMWK21S-lZ5WvLwE2mfkzeZ1iRieBKhDr3nzE7bx-MGck36lIpN23ul2XY_gz2XTAhb3J4YEHKAZHKXsjCgEqOCsk9QhimDki6W9_vpCYQB61392uDG66lvOm9uyO_cSXhxfzEgWEMSC8I0-iTn2RDEdOe52HRfQPBc8ka4fmFHzoWEPtfkIxGB-Y8tLdlEVjxQypUw2iFstxGu-im0sWd818AOxkxJ-6UhdCNpf5Lj6-bjVnJ2tD47SFCxKNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=jLmpE0ESqiU2e41orQWeg0pY6nfInYBhLgNMuQevWBPGWO-iSUi0VoUcw7UE59i31X2GzVmikfQRMjSFQoX5_MltWC9hNB35BUnyQSypxXL0DLHIYdpx1bHkh_Pq3wwEC0ttSY3sCuGjZO6IfE95YuFzwOAxutnq0YYCU0NJF932jPjE-D58nlXNtcu8Q6dVo5nitM6E3jq7cNCM9wXWDtQrBG3gQfmYjInq0idjJIgybkOAcHFz-5kEWoIy16yqvZ-U6qcoXz0yPD-6p04orPhh8HwIW6R3z0CrZ6MmgkZT-IKc6v1nvuW8WpwbNgOTlJZbbxX2hJHlNaH_YLzM4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=jLmpE0ESqiU2e41orQWeg0pY6nfInYBhLgNMuQevWBPGWO-iSUi0VoUcw7UE59i31X2GzVmikfQRMjSFQoX5_MltWC9hNB35BUnyQSypxXL0DLHIYdpx1bHkh_Pq3wwEC0ttSY3sCuGjZO6IfE95YuFzwOAxutnq0YYCU0NJF932jPjE-D58nlXNtcu8Q6dVo5nitM6E3jq7cNCM9wXWDtQrBG3gQfmYjInq0idjJIgybkOAcHFz-5kEWoIy16yqvZ-U6qcoXz0yPD-6p04orPhh8HwIW6R3z0CrZ6MmgkZT-IKc6v1nvuW8WpwbNgOTlJZbbxX2hJHlNaH_YLzM4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=ktEwVplvIRAxCtUPJrdVsS6f-Fhr0JeNkMWIK-r_rrMDUqKFzf8EsoQN3xA8zYdDgS_mrr2J5ophR1ulfGZUj9LHFgidz36JEkeDVdD3Tv5T7pYwEsGKg4gMFHOOmD0sIarwamUIxwtG40_7-D6iIFZY2NLkTzF4UMqeU5zJM7HX6wASmxDSDBnrDF1H5ZnEeGnBvVQB8Z8tW8yIeV7sckmZfUyVA1OJEzB8l9v9yVjQwDFuFeMJ5EPu1s3Hd3bYQVm70RcwigvLbXRAxDo_UuR1wA2bhr1i2YG48ufF2A7cK116neNlo_d8kdyHo9coE3_4naxne7anwatU9Xd4ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=ktEwVplvIRAxCtUPJrdVsS6f-Fhr0JeNkMWIK-r_rrMDUqKFzf8EsoQN3xA8zYdDgS_mrr2J5ophR1ulfGZUj9LHFgidz36JEkeDVdD3Tv5T7pYwEsGKg4gMFHOOmD0sIarwamUIxwtG40_7-D6iIFZY2NLkTzF4UMqeU5zJM7HX6wASmxDSDBnrDF1H5ZnEeGnBvVQB8Z8tW8yIeV7sckmZfUyVA1OJEzB8l9v9yVjQwDFuFeMJ5EPu1s3Hd3bYQVm70RcwigvLbXRAxDo_UuR1wA2bhr1i2YG48ufF2A7cK116neNlo_d8kdyHo9coE3_4naxne7anwatU9Xd4ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvrihjWUASX79C69hhpNdCdIAHR7XwT3Tun0wv0qY8T94oNWiCgxA6Yg8FakahFUgrOKe2aLBle3z9bJy-wIlnRjYdapt9biAMNUXMaSI156IEhQtDP-enkLUxuDjRMU__UeRlHtPNh1Zln0URI0UkDPN793ULIBHJzEwcDI7iERMryOtKxyanZ1U_DJBuRUUkAMC9TSv0UXSPp1bdp8E9jjN1AzBw41fmwvTVmqs0WRb2VFITOt0jEknOH4cMZxa4w2FEEaYV3Lghig_3Dv8M-j4grJy5Onj-r-0ZBu7g4VGtxgIOw9cRQ5ON1EI6NE-qUh3DF_BWkk2b4NPh-xJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crpYwy1mQbuP5Vb2olL5Ef2f3qvmtwTgitsIdyA39PrXOur9clFY5YYPAVxKoZH67zFmgLK3a_Hi1dkZ4rDvYFmjsiv9guxmdBc_hUgKtZjMqXl92Y70tAI4vaubpXKWMUWrgETOiyVsAxgEKA3KNyFjTTmerkYlxaeCG1cK2Jz8YL7PjyPcgyZsa1IyROq-MQBdVoWDte0Q7VFahQ46_fcYubt5FjPEbDfKrMYUZwAlyKSVF9MQER0TqSvueNJ_xYx0_oCeFVtTBJzhFyK4DzR1xtNBMRRdlQzQszRo0v6lJM8leKlvA4ddKsZ6idzOWawTN5ejN8m1eUH0-pWwSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=i-OGQt6tgjqHZBgRXeLj9J0kGIYHypQZFNvuORXezA6TAYmNp-Q-TGmFFNZuVjJ1qqTjXcYiIjlCJSvQMoSUNHFxI1fvGYGmffZ1A7kbJYX0lb_yhlu-BoQ2wK615AoGknqC9nMR4iegUMnF9NVekF31HlNn0SdxWXs2WVXqJFQaHV9QYrbzd9Oyq3tO_jcr-l8XRXluHxLEZaY_rFn67JYfHZHvULN0wg0fMCoD24Nv_Rs2l05_O0f8dWPuEEQoQ7m8_bAcdXfXCO-psr98OKHOfoHDKu4KIt3QBDzAgt2sAdagXXD2es34Z1tE_BS6HpIifUBX9vA1Ml9PIc37bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=i-OGQt6tgjqHZBgRXeLj9J0kGIYHypQZFNvuORXezA6TAYmNp-Q-TGmFFNZuVjJ1qqTjXcYiIjlCJSvQMoSUNHFxI1fvGYGmffZ1A7kbJYX0lb_yhlu-BoQ2wK615AoGknqC9nMR4iegUMnF9NVekF31HlNn0SdxWXs2WVXqJFQaHV9QYrbzd9Oyq3tO_jcr-l8XRXluHxLEZaY_rFn67JYfHZHvULN0wg0fMCoD24Nv_Rs2l05_O0f8dWPuEEQoQ7m8_bAcdXfXCO-psr98OKHOfoHDKu4KIt3QBDzAgt2sAdagXXD2es34Z1tE_BS6HpIifUBX9vA1Ml9PIc37bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqN0yN2hIvdgp9mm_-ZlojBcXe8bcwMvhObrvPae5ZbvZUYbOgDDJ4Aoz-WmxDuGU4qXAk_bfuvVAzYw7nIw_yA7nja679znyz7RWzBMiApyyvcnC9L2GA9DYMNELADHVU9dyexNPqLlecMxBJG7sRp1Zvr65utWRfPxvfEzChkkPR0wg_IudHy6LHey9Wua0o9hoqx-cxuNNbb8DZfxJ6DnNzEIbHpCsCASZwYHmpphC9H8DeYV4Kcs8dlMuzXYnyfpRJd6VqA1BlwamNE4PXBXZT6uq8iMBI3qhMo69l43Ne3bXrj3NETB4QyyAKn0zQIXUQHzYbe8UPO1NqaTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=d0oIDXr6mlVZw72fsrzG2fuf_Bopc5OLI_Jz_adBOzNnppErm8RGz7Iyv8YuUmJPyGR19gkeaQw-7W3RIroqkgIcTj7EAA-IgK8byL9zC2t43Xn5RdfMz68kcWLnDFWw0nzJA7oWQRXJKStqLdOulnlCg9lRuxoQ1ovQkxHfEJsnnW3IA_QM11Er4i41i-kbIWQgmSYPxTGOelNmAhRt7JpKqNTuv6sSok2-iy5Grv5u7J6s6YLjq8casl4OqVyvKZWi8RGxfL9wR-tVNC1NKlbmEgQZcQljV6jCrXJX8I0DurK7rqX6H6t0f5vWrsRplyDckufV2mWWdW4srRaTSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=d0oIDXr6mlVZw72fsrzG2fuf_Bopc5OLI_Jz_adBOzNnppErm8RGz7Iyv8YuUmJPyGR19gkeaQw-7W3RIroqkgIcTj7EAA-IgK8byL9zC2t43Xn5RdfMz68kcWLnDFWw0nzJA7oWQRXJKStqLdOulnlCg9lRuxoQ1ovQkxHfEJsnnW3IA_QM11Er4i41i-kbIWQgmSYPxTGOelNmAhRt7JpKqNTuv6sSok2-iy5Grv5u7J6s6YLjq8casl4OqVyvKZWi8RGxfL9wR-tVNC1NKlbmEgQZcQljV6jCrXJX8I0DurK7rqX6H6t0f5vWrsRplyDckufV2mWWdW4srRaTSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMyzmg-xc7JcE3KZqip6fNiE6uROHXA0GrT0iK680L1wvk-p7kUuwMObtLszyHUTpb2_G9fregX5beaenLzP84_WSNaUydWcI2-ntpgXGRvYjFUGkheNRUDL07A8epzJQ01uALGujEzrjtsDejNIMgKdkfo0NLp-tSiVC-8LHCnqXs750_nWio6MCcqmlAr8k9RKnrfHVTLbDN0qm07ynlVQd1sJraJ4itPPCTPkcNvsy0stfxTvpAm8ciKqFwazWiA4Tkew6p-cnW-JsNnJW5AgWYLvujwiL15e-81yzlI0_iR7YCS35kbjPZjbWofoOcIGV_Vw1FS0Rn8xQaI_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dznKyVQNYPX65nzKzLgXYzvhFpWyAcIlcMmopqVQtT09gCJsvO-863UU-m9jHAfO0YLrKfHL9rr9hMEwnU83PGi3q6CU3ZTHTGt-pTjuAymtpGaV26H3Zc0ka8NoF61eSi5qRDsVVom5NgvVsIMqynWCJ_xrBN4M-qfwmRQO0qyNSNXyASUvJEh7_MbjUB-nzq_DC-rJCTCH_00oQWYw_oX6BHlC9KMNtnbo9PAj-hdGSjlc9OEqsu0WfPzheNwnyyKl60W77th9SHBoEUZaGYOdK7FJA44hIuVMNq3KZq5dQh0tR1btYrk6cjWPCbbsv9XmCFaThi_bsQSKYfx9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhHP4CK9xaaaDsSQAeYcJU90TRVfraUdCJ3EiqG5E-pYMM9Gky9Gq857AYT81n3y7aUvWOmN3ejoOAhuc1dv1YkWfwEXXUPgOI6KQKCKyxam5Cs4I4gbqQOMoKTjPoituyy9rKVbZ9s7GU1AfNlT0Cc0qH88-3sr4W4XYnduOoNJqM6G-Tyl0LJ_rV99f7_kwExvkoc8lawe5C3ESuN08Mf1uBf8esLDcy5izUN0rjB8TgEYyNHvCvHViYITXnzfO-sTuef81ZndOrpgSNe6lep3AUtazgK3HY8Pzfdyy3SPAy9lxL37saOf0UsMYf6RR0rtNvXr6vzzwnPZvE6UtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIRXCmIEW8pvgdTuD_wL6k-PoPy_88SL7Luqe_6jwjZSbJBbvKnF6NOQzxvaliPGrT3B6Vqh1Ex7sts6KozG3fJ7b66U21A1jziZEFLUpTbbtK9KF7SsxaktksmHrf3Q9LfqAvp88XxUNAsEeyP-v4pNjjlrQ-ET67f2AtEBItH-5pzEcdD1W6_Q7Z7aYkeeLjIPSIADiXvLriViK_Ji9AjUInFeGi6PcRGkhAVVCgR3wqDdSAiS1XeSICBjhvpxaoaixKin2sqpks4cXKvRXHMvblgKAoCQ2S__SRPhsjtnzsaJ20KpCw_-l0VuuZJ7FS2Fy5wfqd3dFD_z4daTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pfqep-RVv1nfJt-49Cgd3V33oshfWm_xXAE9_f4PYSKWe6n_Kjyl-GuRVIPXT0fnn48V06dk0xnFjnVX1LEi3DyaE6ALkLaYHNvF8jBM5oQzkpSRbXXak4P7Z-l4-fk0fCtBo8OM0zkESwt9El5C5QSfe2GfRseNjMZdwIE5h6mi3CtOSPdoum8abgO87JlMgcSqP1-bW1EcqM1QFme1sAfx2gU_Bde9yGOYnGgabV7n5xIzr5bcMUpOql8B8DbRwArh8mLeOX0bKU85revzQ3GrgW6bTtkeQoa566dUYzRiHi4eztdBBJIHfp8AW7xWppiURcHLOP5QaittG6oByA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQh-EcgS7GH79xz7-mmpSiZcCRTCIYDlfyiD_ekdm_0mol12u1ECoKK-yxsALIEoxnFgMmIUySH_c5O_DOJxNMXkBJNpgWM8DeY4Poo_ef2THlHxiPwiOPPYKUGnGa-oKvHCs73RPEptTTKOyG18r9MDMoTaFtfF8rc29nIsnwtUiArsnGPMXrob11-IbEJdHw3E01QzoSwhfYyU2Flb1-MPcwYmJKcdHIQ1Ou7VPkkQ9d51LwDkiHGFsU97MOmIgOEQkLF4ivN-t2_bTj3AQZOqpvhpr68VXDW9VXgqeBMETeyHmRbHAxcXdg3hKaRHbz9uyHH5ryiO2hBirTsVcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0JUPLObGSwxv0vTHaWvpnlPA3d0VX8vDyPsix97X35HG7jpSkI6bib2V_Y9YBME6AXv6aEIYL9VWEJVU40wrQ3b_qMh9-JvOrOQzZ2ZYIfn95usWUaXPzgFhQHrDJw4QpHj0RRVpDtCp6rD5Js26-CDgtbDxQPX2_GVXMk-UhdfNM6eq3umfhkjvZf6hQa65m9frzVPFh3DH30aJjFhtaxZJ8e9AC6Prm7xL1vTD_DOcQq0yf_o_PeovE7G4qyrjbYYuK2fuiwo1YSff2HApKUvInTnmdNZqcJtLIofaJhtEUp6gFyZf2xFPic6UUlFZukgY4RlNazw9TA7ocKhOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVnqtEHOorJH0Mb-sQOUKxh38Li6-Mf4ogVF02rdQAMx9-ieBdY130S81rsH1y6JRdGdaPXypJaU_mcQCdGvk4WygjVpUtx8McWjdd2iRgYt1aPDYdgeUHRl7DJfv_VTlobjeyUOpQLavxWlZ-cIu6ATktUJZy4IvIfBZHJ7f84TUC1nixA-AO102pyki2evUFOfCRhDAwQ5g0M_VN2KPNVdTwllnTq3yCooL0l9D82r-9Er8uP2K_T0Mf6LPjV96Qjuzg-KJ03Who6B-UsvGqlVzT2H9QKkxNzYwaovyvHyW2MXGW-t6XH-Vzn5eB1kVFveU6Myca0NBaUIjvLP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkE2C0J0aQ6C1_8MyWzapXZhCwo85tVQHCOJOXyL8oVJdWoPAUl2NpAlHyhJnHp3YHvbuspK2vJzha-bEm5MB724x4WbDKxsmiEES3TBjavvQvkwBt_JeIXmFWazBMXUvIoJE1ogSPLSz4gucphdyr-m1KMqa1XV8kgk4imdtnBf4pUCeU9ClLjPYqaYvLIMxEVvj9v6MnayN6T0MEFYgw8uYhHW_HBzcm9laikIOnmbmrlcIAkumdTThtuC44W5Vs1VY3d71cxn1w-UFopos_a_fVvGJMkZI91HhJFjY-oVn24kxVMwyupx7EWQmIcf3w95pZ0nMnCgsuEceqxrhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex4Y9oGq4RrEyeX9DlyHE4NQ003cTSIwQtscKz787dqnxq2jDGwGm6OuoCs1hOD2CbAKS4XG-iHb2_rD4upuBPyKVCgshGwrF-kN3fDPuJtrkS657wibZIY3TgdHb8IuEBNmC5OWt7c3lEjr14xykPR-2XrOZGjwjMdLb-PCV04w-gOkvDQ0dO0AOdZP_LVmSilv8sftsTHA30VgRsQkJTEDnJr3fVR2I1yw7MM0tg5CTXPJbTANCyNYfMVN0A-hzu-Ezfw76-I3wua4-6eoquKB0RY-FcvNIU7GbSPbJpjSRqqsGVAz578_mNKeNyCsIyvIBtYmFbB_dmJKoRfxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzFHjB7kh3tbqvQLG5SSkHG_uPWQL4ovoQNMGIanXAGkg9tcoDyk4IUmK7la9kqMrftKTqsgUqSNzid5WN6MEWrJK0CWvnJhodfg5T87PIZ3TXStfmhWQTlGqdIkdWcsooz-dVBhNF30mAjDvAkKRST_kQImiBGQ--LEbOLCBnY51jHV2Engi-gUU2WlkizwL_aDZ1l8kjqDrQCPKDyx4O-wThNs7b4pEAsOQVe4CXHM3XTOOmaSM4soQW-E_4QOv73JTI7X9vFescFoaF6LSPC3MmuuuEa5ucCehD-gvVLc6_xxQeu7YUuh3uonKcg8AgzKwRPqHjvshJk1XIM4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=XS2DHqxQiai4MYKf25KKXzE0l1Wmd5b0C-7y9d4sceeOMQUJRKFbXDRv0QWIOPe6hbD-KiOqEjm0CTa3siPT7vn5vCAhKedeJA3JlK_x9Ijrju41ePL5HqjNwH6A_rkIT0Y_7_ynABdNvt8aVV3MsPhDgt3HK5DIITrIbId3GBaXW2mQY6x4KntBOX60vyLf8dDXqXVTFTxAWctGOulUl1xcSE8qV47Qsn15YeSfYLI6zcNHxUVFv4zr0ZKgv0pxCxO8J6gNpWmVT2FkQW3hs1JJF07TdctkAfud160W2mVjNmiIR_8mscty70Gp_WPK1aKwzDjrwxrSYSZa3oqmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=XS2DHqxQiai4MYKf25KKXzE0l1Wmd5b0C-7y9d4sceeOMQUJRKFbXDRv0QWIOPe6hbD-KiOqEjm0CTa3siPT7vn5vCAhKedeJA3JlK_x9Ijrju41ePL5HqjNwH6A_rkIT0Y_7_ynABdNvt8aVV3MsPhDgt3HK5DIITrIbId3GBaXW2mQY6x4KntBOX60vyLf8dDXqXVTFTxAWctGOulUl1xcSE8qV47Qsn15YeSfYLI6zcNHxUVFv4zr0ZKgv0pxCxO8J6gNpWmVT2FkQW3hs1JJF07TdctkAfud160W2mVjNmiIR_8mscty70Gp_WPK1aKwzDjrwxrSYSZa3oqmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
